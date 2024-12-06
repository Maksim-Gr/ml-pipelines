import pandas as pd

from numpy import default_rng
from omegaconf import OmegaConf

from ml_pipeline.models.iris_classifier import IrisClassifier

if __name__ == "__main__":
    nums_rows = 10
    nums_columns = 4
    
    rng = default_rng()
    X = pd.DataFrame(rng.random(size=(nums_rows, nums_columns)))
    y = pd.DataFrame(rng.random(size=nums_rows))
    
    
    model_params = OmegaConf.create({"penalty": "12"})
    training_params = OmegaConf.create({"test_split": 0.3})
    
    
    model = IrisClassifier(model_params, training_params, "artifacts")
    idx_train, idx_test = model.train(X, y)
    
    model.save()