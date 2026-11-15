# Decision

How likely is a bacterial / strep infection based on a short synthetic description? Options: Low likelihood, Medium likelihood, High likelihood, None of these.

# What Worked

Seven actual local llama3.2:3b calls returned valid probability maps and confidence values. All returned probabilities were validated and normalized. The app displays ranked percentages, a top choice, confidence, JSON, and a bar chart. Full inputs, raw outputs and settings are in test_results.json; results are in TEST_RESULTS.md.

Option-order maximum absolute difference: 40.00 percentage points.

None-of-these behavior: 5.00%; meaningful threshold defined before evaluation as >= 10%: FAIL. This threshold is an exploratory homework criterion, not a clinical standard.

Ambiguous-case confidence: 60.00%; baseline: 92.00%; confidence decrease: 32.00 percentage points; lower confidence: PASS.

Repeatability: maximum per-option range across the three Test 5 runs: 0.00 percentage points. Same seed (42), temperature (0.2), model, and prompt were used; this measures fixed-setting repeatability only.

# Where It Failed

Changing only option order shifted probabilities by up to 40.00 percentage points. The explicitly noninfectious example did not reach the predefined 10% None-of-these threshold.

The most important limitation is that valid JSON and plausible scores do not establish calibrated infection probabilities. There are no diagnostic labels or ground-truth clinical outcomes in these synthetic examples. Low likelihood and None of these overlap conceptually; the prompt's noninfectious interpretation is a design choice. The study uses one model and seven calls, with a fixed seed, and cannot establish broader reliability.

# What a Clinician Would Need Before Trusting It

Independent representative labeled validation data, an agreed target diagnosis and option definitions, calibration and uncertainty evaluation, clinical review, subgroup and safety evaluation, reproducible model versioning, and appropriate privacy and governance controls. Missing history, examination findings and diagnostic evidence cannot be recovered from short text. This prototype provides no treatment advice and has no clinical validation.

# Conclusion

The homework demonstrates a local text-to-JSON decision pipeline and measures its behavior on the assigned synthetic cases. It does not establish diagnostic performance. Educational prototype only. Not for clinical decision-making.
