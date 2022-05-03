# Teste_Einstein

In this test I need to create a classifier using a given dataset. 

When I look the dataset, I saw the features don't have correlation with the target, this make me choose nonlinear models to test (K Nearst Neighbors, Random Forest and XGBoost). 

To choose the better model I use RepeatedStratifiedKFold as cross validation and GridSearchCV to test different parameters in different models. Also, I added new features using math's transformations because the data only have 3 features with no correlation.

The best result was an 83% of the ROC AUC using XGBoost and I create a pipeline of this model to be available to develop.

However, the results against the test set are not very better than the Dummy Classifier. The only advantage is the better results when we see the results open by target options.

I think is needed to understand better the problem with the client and try to find other features and better models.
