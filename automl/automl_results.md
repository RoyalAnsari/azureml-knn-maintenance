# Automated ML results (KNN + LogisticRegression)

# Automated ML results
- Job name: knn-automl-abdullah
- Data: ai4i-maintenance-table version 4
- Allowed models: KNN, LogisticRegression
- Result: all 10 trials were LogisticRegression; no KNN trial completed.
- Best model: StandardScalerWrapper, LogisticRegression
- Hyperparameters: C=1526.4, class_weight=balanced, multinomial, l2, newton-cg
- AUC weighted: 0.9007
- Observation: AutoML's KNN does not accept sparse data (one-hot `type`), so it
  was skipped. The top 3 models used class_weight=balanced, which helps with
  the 3.4% failure rate.