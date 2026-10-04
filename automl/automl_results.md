# Automated ML results (KNN + LogisticRegression)

- Job name: <your job name>
- Data: ai4i-maintenance-table version 4
- Overall best model:
- Best KNN trial (scaler + model):
- n_neighbors:
- weights:
- AUC weighted (best KNN):
- Recall (macro) (best KNN):
- F1 (macro) (best KNN):

## Notes
- The wizard could not read the MLTable schema, so I submitted the job from the SDK (notebooks/02_automl_knn.ipynb).
- With KNN as the only allowed model, AutoML failed with a sparse data error, because the `type` column gets one-hot encoded.
- I allowed LogisticRegression next to KNN and report the best KNN trial for the comparison.
- Observation: what did AutoML choose differently from my notebook (K=1, uniform, AUC 0.669)?