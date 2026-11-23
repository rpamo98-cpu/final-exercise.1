# FINAL LABORATORY EXERCISE 1-B — Submission Guide

## Contents already prepared
- Original `MIDTERM_EXAMINATION.ipynb`
- Cleaned CSV, Streamlit application and modular Python source code
- Reconstructed fitted Decision Tree pipeline (`models/trained_model.joblib`) and evaluation metrics
- Five sample predictions (`FIVE_SAMPLE_PREDICTIONS.csv`)
- SAD requirements and use-case diagram (inside the app and `assets/`)
- Deployment report draft (`DEPLOYMENT_REPORT.md`) and instructions (`README.md`)

## Important qualification
The provided midterm notebook did not include a completed trained model. The included pipeline was reconstructed and trained using the supplied CSV and a Decision Tree classifier. Its metrics are **not** verified against a saved original midterm model. Do not claim otherwise.

## Steps you must complete yourself
1. Open terminal in the extracted folder. Run `pip install -r requirements.txt` then `streamlit run app.py`.
2. Test Home, Dataset, Data Analysis, Prediction, Dashboard and System Design.
3. Capture screenshots of five working functional modules (Dataset, Data Analysis, Prediction, Dashboard, System Design) and five sample prediction runs. Put images in `screenshots/`.
4. Push the repository to your GitHub account, then deploy on https://share.streamlit.io with `app.py` as entrypoint.
5. Paste your **actual** GitHub URL and deployed Streamlit URL below and in your submitted report.

GitHub repository URL: __________________________
Streamlit deployed URL: _________________________

## Verification checklist
- [ ] CSV upload works and missing columns display an error
- [ ] Empty CSV is rejected
- [ ] At least three interactive charts display
- [ ] Prediction accepts valid inputs and produces a result
- [ ] Five sample prediction screenshots captured
- [ ] Dashboard review queue visible
- [ ] SAD use-case diagram and requirements visible
- [ ] GitHub repository URL works
- [ ] Streamlit deployed URL opens successfully

Never publish actual sensitive student data. The prototype does not implement authentication or final-decision database writes.
