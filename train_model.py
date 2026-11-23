from pathlib import Path
import json, joblib, pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from modules.data_processing import FEATURES,CATEGORICAL,NUMERIC,validate
root=Path(__file__).resolve().parent
raw=pd.read_csv(root/'data/cleaned_student_service_requests.csv')
df=validate(raw)
df=df[df['Status'].astype(str).str.lower().eq('completed') & df['SLA_Breached'].isin([0,1])].copy()
X=df[FEATURES];y=df['SLA_Breached'].astype(int)
if y.nunique()!=2: raise ValueError('Both outcome classes are required for this training dataset')
pre=ColumnTransformer([('categorical',Pipeline([('impute',SimpleImputer(strategy='most_frequent')),('encode',OneHotEncoder(handle_unknown='ignore'))]),CATEGORICAL),('numeric',SimpleImputer(strategy='median'),NUMERIC)])
model=Pipeline([('preprocessing',pre),('classifier',DecisionTreeClassifier(max_depth=5,min_samples_leaf=5,random_state=42))])
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
model.fit(X_train,y_train);pred=model.predict(X_test)
metrics={'accuracy':accuracy_score(y_test,pred),'precision':precision_score(y_test,pred,zero_division=0),'recall':recall_score(y_test,pred,zero_division=0),'f1':f1_score(y_test,pred,zero_division=0),'confusion_matrix':confusion_matrix(y_test,pred).tolist(),'training_rows':len(X_train),'test_rows':len(X_test),'version':'reconstructed-decision-tree-v1','note':'Reconstructed from uploaded incomplete midterm notebook; original fitted model unavailable.'}
(root/'models').mkdir(exist_ok=True);joblib.dump(model,root/'models/trained_model.joblib');(root/'models/metrics.json').write_text(json.dumps(metrics,indent=2))
print(json.dumps(metrics,indent=2))
