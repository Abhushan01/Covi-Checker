# Covi-Checker
<i>Web Application to predict Covid-19 test results using Machine Learning</i><br><br>
<b>In this project, we deploy Machine Learning algorithms to the Django web Application, where users can easily enter their symptoms and get their Covid-19 test results.</b><br><br>
The novel coronavirus disease 2019 (COVID-19) pandemic caused by the SARS-CoV-2 continues to pose a critical and urgent threat to global health. 
The main motivation for this project is to ease the diagnosis of COVID-19 based on available data and to reduce the burden on healthcare systems.<br><br>

We train different Machine Learning models on a dataset containing the most common clinical symptoms of Covid-19, (such as sore throat, shortness of breath, headache)
and other factors like age, gender, test-indications, whether the patient have been in contact with a confirmed Covid-19 patient, or have visited foreign countries recently, and their test results for Covid-19. 
The Dataset used in this project is provided by the Israeli Ministry of Health.
<br><br>The following Machine Learning Algorithms are trained in this project:
<ul>
<li><b>Decision Tree:</b><br>Decision Tree is a Supervised learning technique that can be used for both classification and Regression problems, but mostly it is preferred for solving Classification problems. It is a tree-structured classifier, where internal nodes represent the features of a dataset, branches represent the decision rules and each leaf node represents the outcome.</li>
<li><b>Random Forest:</b><br>Random Forest is a classifier that contains a number of decision trees on various subsets of the given dataset and takes the average to improve the predictive accuracy of that dataset. Instead of relying on one decision tree, the random forest takes the prediction from each tree and based on the majority votes of predictions, and it predicts the final output.</li>
<li><b>Logistic Regression:</b><br>Logistic regression predicts the output of a categorical dependent variable. Therefore the outcome must be a categorical or discrete value. It can be either Yes or No, 0 or 1, true or False, etc. but instead of giving the exact value as 0 and 1, it gives the probabilistic values which lie between 0 and 1.
</li>
<br><br>
After training the ml models, we calculate the accuracy scores for the respective ml models. The program then chooses the Ml model with highest accuracy score and use it to make predictions for the data entered by the user.
<br><br>
The backend logic, including the Machine Learning program is written using Python programming Language. The Ml program is then imported into the views.py file to be accessed easily by the web application.
For Frontend part, I have used Bootstrap v5.0 and plain old CSS, which I linked to the template files through static method.<br><br>
Following are the screenshots from this project:<br><br>
<b>Home Page:</b><br><br>
<img src="https://raw.githubusercontent.com/Abhushan01/Covi-Checker/main/1.png" alt="home-page"><br><br>
<b>About Page:</b><br><br>
<img src="https://raw.githubusercontent.com/Abhushan01/Covi-Checker/main/2.png" alt="about-page"><br><br>
<b>Predictor Page:</b><br><br>
<img src="https://raw.githubusercontent.com/Abhushan01/Covi-Checker/main/3.png" alt="predictor-page"><br><br>
<b>Result Page:</b><br><br>
<img src="https://raw.githubusercontent.com/Abhushan01/Covi-Checker/main/4.png" alt="result-page"><br><br>
<b>Help-Center Page:</b><br><br>
<img src="https://raw.githubusercontent.com/Abhushan01/Covi-Checker/main/5.png" alt="helpcenter-page">





</ul>
