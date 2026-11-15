"""Runs the exact homework cases and writes evidence and report from actual calls."""
import datetime
import json
from pathlib import Path
from decision import DEFAULT_OPTIONS, MODEL, BASE, decide, ranked

CLASSIC = 'A patient has a sore throat, fever, swollen lymph nodes and no cough.'
NONINFECTIOUS = 'The patient reports mild throat discomfort immediately after shouting at a concert. There is no fever, no swollen lymph nodes and no other symptoms suggesting infection.'
AMBIGUOUS = 'The patient has a sore throat and says they feel slightly unwell. No other information is available.'

def main():
    cases = [('Test 1', CLASSIC, DEFAULT_OPTIONS),
             ('Test 2', CLASSIC, ['High likelihood', 'None of these', 'Low likelihood', 'Medium likelihood']),
             ('Test 3', NONINFECTIOUS, DEFAULT_OPTIONS), ('Test 4', AMBIGUOUS, DEFAULT_OPTIONS)]
    cases += [(f'Test 5 repeat {i}', CLASSIC, DEFAULT_OPTIONS) for i in range(1, 4)]
    records = []
    for name, patient, options in cases:
        print(f'Running {name}', flush=True)
        result, raw = decide(patient, options)
        records.append({'name': name, 'input': patient, 'options': options, 'result': result, 'raw': raw})
        Path('test_results.json').write_text(json.dumps({'model': MODEL, 'endpoint': BASE, 'temperature': .2, 'seed': 42, 'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'runs': records}, indent=2), encoding='utf-8')
    base = records[0]['result']
    differences = {o: records[1]['result']['probabilities'][o] - base['probabilities'][o] for o in DEFAULT_OPTIONS}
    max_order = max(abs(x) for x in differences.values())
    none = records[2]['result']['probabilities']['None of these']
    confidence_drop = base['confidence'] - records[3]['result']['confidence']
    repeats = [r['result'] for r in records[4:]]
    spread = max(max(r['probabilities'][o] for r in repeats) - min(r['probabilities'][o] for r in repeats) for o in DEFAULT_OPTIONS)
    observations = (f'Option-order maximum absolute difference: {max_order * 100:.2f} percentage points.\n\n'
                    f'None-of-these behavior: {none:.2%}; meaningful threshold defined before evaluation as >= 10%: {"PASS" if none >= .1 else "FAIL"}. '
                    'This threshold is an exploratory homework criterion, not a clinical standard.\n\n'
                    f'Ambiguous-case confidence: {records[3]["result"]["confidence"]:.2%}; baseline: {base["confidence"]:.2%}; '
                    f'confidence decrease: {confidence_drop * 100:.2f} percentage points; lower confidence: {"PASS" if confidence_drop > 0 else "FAIL"}.\n\n'
                    f'Repeatability: maximum per-option range across the three Test 5 runs: {spread * 100:.2f} percentage points. '
                    'Same seed (42), temperature (0.2), model, and prompt were used; this measures fixed-setting repeatability only.')
    lines = ['# Actual test results', '', f'Model: {MODEL}. Local endpoint: {BASE}. Completed: {datetime.datetime.now(datetime.timezone.utc).isoformat()}.', '', 'Seven real Ollama calls; no expected probabilities substituted.', '']
    for record in records:
        result = record['result']
        lines += [f'## {record["name"]}', '', record['input'], '', f'Option order: {", ".join(record["options"])}', '', f'Top choice: {ranked(result)[0][0]}. Confidence: {result["confidence"]:.2%}.', '', '| Option | Probability |', '|---|---:|']
        lines += [f'| {o} | {p:.2%} |' for o, p in ranked(result)]
        lines += ['', f'Normalized sum: {sum(result["probabilities"].values()):.12f}', '']
    lines += ['## Comparisons', '', observations, '', '| Option | Test 2 minus Test 1 (percentage points) |', '|---|---:|']
    lines += [f'| {o} | {d * 100:+.2f} |' for o, d in differences.items()]
    Path('TEST_RESULTS.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    failures = []
    if max_order > .000001:
        failures.append(f'Changing only option order shifted probabilities by up to {max_order * 100:.2f} percentage points.')
    if none < .1:
        failures.append('The explicitly noninfectious example did not reach the predefined 10% None-of-these threshold.')
    if confidence_drop <= 0:
        failures.append('Confidence did not fall for the ambiguous case.')
    failure_text = ' '.join(failures) or 'No behavioral criterion failed in this small sample. This does not establish accuracy or clinical safety.'
    report = f'''# Decision

How likely is a bacterial / strep infection based on a short synthetic description? Options: Low likelihood, Medium likelihood, High likelihood, None of these.

# What Worked

Seven actual local {MODEL} calls returned valid probability maps and confidence values. All returned probabilities were validated and normalized. The app displays ranked percentages, a top choice, confidence, JSON, and a bar chart. Full inputs, raw outputs and settings are in test_results.json; results are in TEST_RESULTS.md.

{observations}

# Where It Failed

{failure_text}

The most important limitation is that valid JSON and plausible scores do not establish calibrated infection probabilities. There are no diagnostic labels or ground-truth clinical outcomes in these synthetic examples. Low likelihood and None of these overlap conceptually; the prompt's noninfectious interpretation is a design choice. The study uses one model and seven calls, with a fixed seed, and cannot establish broader reliability.

# What a Clinician Would Need Before Trusting It

Independent representative labeled validation data, an agreed target diagnosis and option definitions, calibration and uncertainty evaluation, clinical review, subgroup and safety evaluation, reproducible model versioning, and appropriate privacy and governance controls. Missing history, examination findings and diagnostic evidence cannot be recovered from short text. This prototype provides no treatment advice and has no clinical validation.

# Conclusion

The homework demonstrates a local text-to-JSON decision pipeline and measures its behavior on the assigned synthetic cases. It does not establish diagnostic performance. Educational prototype only. Not for clinical decision-making.
'''
    Path('REPORT.md').write_text(report, encoding='utf-8')
    print(observations, flush=True)

if __name__ == '__main__':
    main()
