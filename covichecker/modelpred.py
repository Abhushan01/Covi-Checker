# importing libraries 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#reading data from csv file
lst=[]
df=pd.read_csv(r"C:\Users\Home\Desktop\Self-Learning\python_dev\django_dev\django_project03-CoviChecker\covichecker\Corona-report_cln.csv")


#creating designing matrix X and target vector y
X=df.drop("corona_result", axis=1)
y=df['corona_result']
#splitting dataset into training and test data
X_train,X_test,y_train,y_test=train_test_split(X,y, test_size=0.33,random_state=42)


# predictions using decision-tree method
classifier=DecisionTreeClassifier()
classifier.fit(X_train, y_train)
pred1=classifier.predict(X_test)
accuracy_dt=accuracy_score(y_test,pred1)*100
print(f"Accuracy score by decision tree method is {accuracy_dt}%")
lst.append(accuracy_dt)

# predictions using randomForest method
model=RandomForestClassifier(n_estimators=10)
model.fit(X_train,y_train)
pred2=model.predict(X_test)
accuracy_rf=accuracy_score(y_test,pred2)*100
print(f"Accuracy score by Random Forest method is {accuracy_rf}%")
lst.append(accuracy_rf)

# predictions using logistic regression 
logreg=LogisticRegression()
logreg.fit(X_train,y_train)
pred3=logreg.predict(X_test)
accuracy_lr=accuracy_score(y_test,pred3)*100
print(f"Accuracy score by logistic regression method is {accuracy_lr}%")
lst.append(accuracy_lr)



#checking for ml model having maximum value of accuracy score to make the prediction for the user
def covid_result_pred(form_input):
    if accuracy_dt ==max(lst):
        result_pred=classifier.predict(form_input)
        print("Result predicted by Decision Tree")
     
    elif accuracy_rf ==max(lst):
        result_pred=model.predict(form_input)
        print("Result predicted by Random Forest")
      
    else:
        result_pred=logreg.predict(form_input)
        print("Result predicted by Logistic Regression")
    
    return result_pred


     
