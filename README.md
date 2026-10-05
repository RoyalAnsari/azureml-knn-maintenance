# azureml-knn-maintenance
KNN predictive maintenance on Azure ML

## Results

| | Notebook | Automated ML | Designer |
|---|---|---|---|
|Algorithm|	KNN	|LogisticRegression (best trial; no KNN trial ran)|	KNN
| Best K | 1 | n/a | 1 |
| Weights | uniform | n/a| uniform |
| Scaler | StandardScaler | StandardScalerWrapper | StandardScaler |
| Test recall | 0.353 | not reported  | 0.353 |
| Test F1 | 0.397 | not reported | 0.397 |
| AUC | 0.669 | 0.9007 (weighted,cross validation) | 0.669 |
| Code written | Most | Little (SDK to submit) | Small script |
| Deployable to endpoint | Yes | Yes | No (classic components) |
|Accuracy | 0.964 | 0.82150|0.964|
Note: AutoML scores are macro/weighted averages, not failure-class scores.
 ||Answers


1. Best recall: the notebook and Designer both gave 0.353, so they are essentially the same. AutoML's LogisticRegression had a much higher AUC (0.90 vs 0.67).
2. Real factory choice: I would test LogisticRegression with balanced class weights first, because it separated the classes far better. KNN with K=1 was weak, and the notebook gave full control and was deployable.
3. Is 3.4% a problem? Yes. With K=1, probabilities are only 0 or 1, so threshold tuning did nothing. The best AutoML trials used class_weight=balanced, which supports this. More failure data or a larger K with distance weights would help KNN.