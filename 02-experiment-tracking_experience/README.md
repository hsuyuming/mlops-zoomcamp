### ML Experiment - Relevant information
- source code (Which version of your code)
- Enviroment
- Data (What data this version associate with )
- Model
- Hyperparameters
- Metrics (e.g: Accuracy,... )

### Benefit (Try to automate the process)
- Reproducibility
- Organization
- Optimizatoin

### MLflow (Opensource for ML lifecycle)
##### main module
- Tracking
- Models
- Model Registry
- Projects
##### tracking module help you organize your experiments in each run
- Parameters (e.g: path of dataset)
- Metrics (e.g: accuracy, f1...)
- Metadata (e.g: tag, developer name...)
- Artifacts (e.g: any file you used to train model)
- Models (e.g: lock your model)
##### extra information mlflow will log
- source code
- Version of the code (git commit)
- Start and end time
- Author


### metaflow cmd
```cmd
cd /Users/xxxx/mlops-zoomcamp/02-experiment-tracking_experience
mlflow ui --backend-store-uri sqlite:////tmp/mlflow.db --default-artifact-root=/tmp/mlrun  --artifacts-destination=/tmp/mlartifacts
```

