# Decision-Support Workflow

1. Student or staff member submits a service request through the existing institutional process.
2. Student services staff upload authorized request records into the monitoring prototype.
3. The app validates required fields and shows missing values, duplicates and descriptive charts.
4. The saved Decision Tree pipeline estimates SLA breach risk from pre-completion request features.
5. The dashboard prioritizes requests for staff review, with the prediction interpreted as a risk indicator rather than a final decision.
6. Authorized student services staff verify context, queue conditions, SLA policies and completeness of documentation.
7. A supervisor or authorized officer records any final service decision in the official institutional system (not in this prototype).
8. Staff monitor outcomes and investigate errors or changes in service patterns.

## Actors
- Student/requester: submits request in the existing service system; no direct access to staff analytics is implemented.
- Student services staff: validates records, reviews risk and follows up on pending requests.
- Authorized supervisor: makes and records final institutional decisions outside this prototype.

## Functional requirements
FR1 Upload and validate CSV records.
FR2 View missing values and duplicate summaries.
FR3 Explore descriptive statistics and interactive charts.
FR4 Predict SLA breach risk for a new request using the saved pipeline.
FR5 View a risk-based pending request review queue.

## Nonfunctional requirements
NFR1 Provide understandable validation errors.
NFR2 Cache the saved model instead of retraining on refresh.
NFR3 Avoid public disclosure of sensitive student records; production deployment needs access controls.
