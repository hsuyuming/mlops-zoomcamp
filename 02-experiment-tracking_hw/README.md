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


### mlflow cmd
```cmd
cd /Users/xxxxx/mlops-zoomcamp/02-experiment-tracking_hw
mlflow ui --backend-store-uri sqlite:////tmp/mlflow.db
```

### Consideration
- training duration  
- model size
- performance


### Home work
```cmd

python ./homework/preprocess_data.py --raw_data_path=./data --dest_path=./output

python ./homework/train.py --data_path=./output 

(mlops-zoomcamp) xxxx@xxxxx 02-experiment-tracking_hw % python ./homework/hpo.py
100%|█████████████████████████| 50/50 [05:00<00:00,  6.00s/trial, best loss: 6.6284257482044735]


```
