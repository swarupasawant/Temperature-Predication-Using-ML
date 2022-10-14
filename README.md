# Temperature-Predication-Using-ML

Temperature prediction using machine learning models - Laao and Ridge,KNN, SVR, Decision Tree and Ensemble Techniques through a comparative analysis using the data during the period 2006 to 2016. The experimental results are evaluated using r2 score, Mean Absolute Error (MAE), Root Mean Square Error (RMSE) and Correlation Coefficients (CC). Random forest regressor model gives 94% accuracy by using this as a base model we create prediction model and deployed on Heroku.

Heroku link - https://temp-prediction-model.herokuapp.com/

ML Workflow 
1. Collection of the data
2. EDA : Identify and correct missing data points/anomalies 
3. Prepare the data for the machine learning model by cleaning/wrangling
4. Establish a baseline model
5. Train the model on the training data
6. Make predictions on the test data
7. Compare predictions to the known test set targets and calculate performance metrics
8. If performance is not satisfactory, adjust the model, acquire more data, or try a different modeling technique
9. Interpret model and report results visually and numerically

Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation


pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

HEROKU_EMAIL = xyz@gmail.com
HEROKU_API_KEY = <>
HEROKU_APP_NAME = ml-demo-app
BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase




