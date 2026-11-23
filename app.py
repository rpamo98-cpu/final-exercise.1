from pathlib import Path
import json,joblib,pandas as pd,streamlit as st
from modules.data_processing import validate
from modules.exploratory_analysis import render as eda
from modules.prediction import render as prediction
from modules.dashboard import render as dashboard
st.set_page_config(page_title='Student Service SLA Monitor',page_icon='📋',layout='wide')
root=Path(__file__).resolve().parent
@st.cache_resource
def load_model(): return joblib.load(root/'models/trained_model.joblib')
@st.cache_data
def default_data(): return pd.read_csv(root/'data/cleaned_student_service_requests.csv')
model=load_model();metrics=json.loads((root/'models/metrics.json').read_text())
st.sidebar.title('Student Service Monitor')
menu=st.sidebar.selectbox('Module',['Home','Dataset','Data Analysis','Prediction','Dashboard','System Design'])
uploaded=st.sidebar.file_uploader('Upload a CSV (optional)',type=['csv'])
try:
    data=validate(pd.read_csv(uploaded) if uploaded else default_data().copy())
except Exception as exc:
    st.error(f'Dataset validation failed: {exc}');st.stop()
if menu=='Home':
    st.title('Student Service Request Monitoring')
    st.write('SLA breach prediction and staff decision support based on the uploaded midterm project.')
    st.warning('The original notebook was incomplete and contained no fitted model. This app uses a reconstructed Decision Tree pipeline trained on the supplied cleaned CSV; performance is not verified against original midterm predictions.')
    st.write('Model version:',metrics['version'])
    st.write('Model limitations: synthetic dataset; associations are not causal; predictions can be wrong; authorized staff make all final decisions.')
elif menu=='Dataset':
    st.header('Dataset Upload and Validation')
    st.success(f'Validated {len(data)} rows and {len(data.columns)} columns.')
    st.dataframe(data.head(50),use_container_width=True)
    st.write('Missing values by column');st.dataframe(data.isna().sum().rename('Missing count'))
    st.metric('Duplicate Request_ID values',int(data['Request_ID'].duplicated().sum()))
    st.metric('Duplicate rows',int(data.duplicated().sum()))
elif menu=='Data Analysis': eda(data)
elif menu=='Prediction': prediction(data,model,metrics)
elif menu=='Dashboard': dashboard(data,model)
else:
    st.header('Systems Analysis and Design Integration')
    st.subheader('Functional Requirements')
    for x in ['FR1: Staff can upload and validate CSV records.','FR2: Staff can inspect missing and duplicate values.','FR3: Staff can explore interactive statistics and charts.','FR4: Staff can enter new request features and view model predictions.','FR5: Staff can inspect a prioritized pending-request review queue.']:st.write(x)
    st.subheader('Non-functional Requirements')
    for x in ['NFR1: Validation errors must be understandable.','NFR2: Saved model inference must not retrain on each refresh.','NFR3: Sensitive records must not be published without authorization.']:st.write(x)
    st.subheader('Actors and authority')
    st.write('Student services staff: review uploads, predictions, and queue; authorized supervisor: record final service decisions in the official system. Students: submit requests through the existing service workflow, not this staff-only prototype.')
    st.image(str(root/'assets/use_case_diagram.png'),caption='Updated use case diagram')
    st.subheader('Analytical decision workflow')
    st.code('CSV upload → schema validation → data exploration → saved pipeline → risk prediction → staff review → decision recorded in official service system')
    st.caption('This prototype does not implement authentication or write final decisions to a database. Access controls must be added before production use.')
