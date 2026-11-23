# Student Service Request SLA Monitoring (Section B)

Streamlit deployment of the supplied midterm student service request dataset and Decision Tree modeling approach.

## Important provenance
The uploaded midterm notebook stops during EDA and **does not contain a fitted model or evaluation results**. Therefore `train_model.py` reconstructs a Decision Tree pipeline using the midterm's `SLA_Breached` target, the cleaned CSV, and pre-completion features. **Do not claim model metrics match the original midterm.** The included saved model is a reconstruction, not the original trained model.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```
To reproduce the saved pipeline:
```bash
python train_model.py
```

## Deployment
Push this project to GitHub. In Streamlit Community Cloud, select the repository, branch, and `app.py`. Do not upload sensitive real student records. Record the repository and deployed URLs in your submission.

## Model and leakage control
Training uses completed requests with known SLA outcomes. `Processing_Days`, `Status`, `Satisfaction_Score`, `Reopened`, and the outcome `SLA_Breached` are excluded from inference features. `Queue_Category` and `Submission_Weekday` were engineered in the midterm. The app requires those fields when uploading an already-cleaned CSV. Model probabilities are not calibrated.

## Limitations
The sample dataset is synthetic. The model cannot verify fairness or generalization to live requests. Predictions are for human review only; final decisions are not stored in this prototype. Access control is not implemented. Dataset uploads do not retrain the saved model.

## Verification checklist
- [ ] Test valid CSV and missing-column/empty CSV errors
- [ ] Test prediction with valid inputs
- [ ] Test each navigation page and all interactive charts
- [ ] Capture five sample predictions and five module screenshots
- [ ] Confirm public deployment opens successfully
- [ ] Compare predictions with the original model **only if that model is later provided**
