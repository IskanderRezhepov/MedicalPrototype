# Actual test results

Model: llama3.2:3b. Local endpoint: http://127.0.0.1:11434. Completed: 2026-11-15T12:22:35.122281+00:00.

Seven real Ollama calls; no expected probabilities substituted.

## Test 1

A patient has a sore throat, fever, swollen lymph nodes and no cough.

Option order: Low likelihood, Medium likelihood, High likelihood, None of these

Top choice: High likelihood. Confidence: 92.00%.

| Option | Probability |
|---|---:|
| High likelihood | 54.00% |
| Medium likelihood | 45.00% |
| Low likelihood | 1.00% |
| None of these | 0.00% |

Normalized sum: 1.000000000000

## Test 2

A patient has a sore throat, fever, swollen lymph nodes and no cough.

Option order: High likelihood, None of these, Low likelihood, Medium likelihood

Top choice: High likelihood. Confidence: 90.00%.

| Option | Probability |
|---|---:|
| High likelihood | 80.00% |
| None of these | 10.00% |
| Low likelihood | 5.00% |
| Medium likelihood | 5.00% |

Normalized sum: 1.000000000000

## Test 3

The patient reports mild throat discomfort immediately after shouting at a concert. There is no fever, no swollen lymph nodes and no other symptoms suggesting infection.

Option order: Low likelihood, Medium likelihood, High likelihood, None of these

Top choice: Low likelihood. Confidence: 95.00%.

| Option | Probability |
|---|---:|
| Low likelihood | 80.00% |
| Medium likelihood | 10.00% |
| High likelihood | 5.00% |
| None of these | 5.00% |

Normalized sum: 1.000000000000

## Test 4

The patient has a sore throat and says they feel slightly unwell. No other information is available.

Option order: Low likelihood, Medium likelihood, High likelihood, None of these

Top choice: Medium likelihood. Confidence: 60.00%.

| Option | Probability |
|---|---:|
| Medium likelihood | 60.00% |
| Low likelihood | 20.00% |
| High likelihood | 10.00% |
| None of these | 10.00% |

Normalized sum: 1.000000000000

## Test 5 repeat 1

A patient has a sore throat, fever, swollen lymph nodes and no cough.

Option order: Low likelihood, Medium likelihood, High likelihood, None of these

Top choice: High likelihood. Confidence: 92.00%.

| Option | Probability |
|---|---:|
| High likelihood | 54.00% |
| Medium likelihood | 45.00% |
| Low likelihood | 1.00% |
| None of these | 0.00% |

Normalized sum: 1.000000000000

## Test 5 repeat 2

A patient has a sore throat, fever, swollen lymph nodes and no cough.

Option order: Low likelihood, Medium likelihood, High likelihood, None of these

Top choice: High likelihood. Confidence: 92.00%.

| Option | Probability |
|---|---:|
| High likelihood | 54.00% |
| Medium likelihood | 45.00% |
| Low likelihood | 1.00% |
| None of these | 0.00% |

Normalized sum: 1.000000000000

## Test 5 repeat 3

A patient has a sore throat, fever, swollen lymph nodes and no cough.

Option order: Low likelihood, Medium likelihood, High likelihood, None of these

Top choice: High likelihood. Confidence: 92.00%.

| Option | Probability |
|---|---:|
| High likelihood | 54.00% |
| Medium likelihood | 45.00% |
| Low likelihood | 1.00% |
| None of these | 0.00% |

Normalized sum: 1.000000000000

## Comparisons

Option-order maximum absolute difference: 40.00 percentage points.

None-of-these behavior: 5.00%; meaningful threshold defined before evaluation as >= 10%: FAIL. This threshold is an exploratory homework criterion, not a clinical standard.

Ambiguous-case confidence: 60.00%; baseline: 92.00%; confidence decrease: 32.00 percentage points; lower confidence: PASS.

Repeatability: maximum per-option range across the three Test 5 runs: 0.00 percentage points. Same seed (42), temperature (0.2), model, and prompt were used; this measures fixed-setting repeatability only.

| Option | Test 2 minus Test 1 (percentage points) |
|---|---:|
| Low likelihood | +4.00 |
| Medium likelihood | -40.00 |
| High likelihood | +26.00 |
| None of these | +10.00 |
