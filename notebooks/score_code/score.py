import os, json
import mlflow
import pandas as pd

def init():
    global model
    model_dir = os.environ["AZUREML_MODEL_DIR"]
    # MLflow model folder dhoondhein
    for root, dirs, files in os.walk(model_dir):
        if "MLmodel" in files:
            model = mlflow.sklearn.load_model(root)
            break

def run(raw_data):
    data = json.loads(raw_data)["input_data"]
    df = pd.DataFrame(data["data"], columns=data["columns"])
    return model.predict(df).tolist()
