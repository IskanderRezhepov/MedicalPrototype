# Synthetic infection decision homework

Educational prototype only. Not for clinical decision-making.

The class decision is: **How likely is a bacterial / strep infection based on a short synthetic patient description?** Default options are Low likelihood, Medium likelihood, High likelihood, and None of these.

## Install

Use Python 3.10+ and an existing running Ollama installation. In this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ollama list
```

The default model is the already installed `llama3.2:3b`. If necessary, install it with `ollama pull llama3.2:3b`. The app permits another installed model name. If Ollama is stopped, start it from its application or with `ollama serve`.

## Run

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open http://localhost:8501. Enter synthetic text, edit the options (one unique option per line), confirm synthetic data, and press **Run Decision**. Never enter real patient information.

The Python client sends the text and option order to local Ollama at 127.0.0.1:11434 with a JSON schema, temperature 0.2 and seed 42. It validates every option and numeric range, rejects malformed or missing values, rejects zero totals, and normalizes valid probabilities. Confidence remains the model's independently reported confidence. The interface ranks percentages and displays a bar chart and raw/normalized JSON. No cloud inference is used by this code.

## Tests

```powershell
.\.venv\Scripts\python.exe -m unittest -v test_validation test_app
.\.venv\Scripts\python.exe run_experiments.py
.\.venv\Scripts\python.exe verify_live_app.py
```

The experiment script runs the exact five assigned tests (seven model calls total), saves raw and normalized responses in `test_results.json`, and generates `TEST_RESULTS.md` and `REPORT.md` only after successful calls. Test 2 compares option probabilities by label, not position. Test 3 uses a predeclared exploratory threshold of at least 10% for meaningful None-of-these probability. Test 4 checks a strict confidence decrease. Test 5 reports per-option variation for three identical runs. Behavioral failures are observations, not reasons to replace model outputs. Execution errors stop the script. Reruns overwrite generated evidence; preserve submitted files if needed. The optional `verify_live_app.py` performs one additional real model call through the Streamlit form and checks that the result table, confidence and chart render.

## Limitations

Scores and confidence are uncalibrated model outputs, not measured clinical probabilities or accuracy. Synthetic cases have no diagnostic ground truth. A fixed seed does not guarantee determinism across hardware or versions. None of these overlaps with Low likelihood and is defined here as a noninfectious explanation outside the infection framing. Option edits change the task. Input confirmation cannot technically detect real patient data. No patient data should ever be entered. Results apply only to the recorded model, prompt and small set of synthetic examples.
