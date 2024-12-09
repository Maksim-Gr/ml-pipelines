from typing import TYPE_CHECKING

if TYPE_CHECKING: 
    import logging
    from  omegaconf import DictConfig
    
    from ml_pipeline.model import Model
    
from ml_pipeline.models.iris_classifier import IrisClassifier



class ModelFactory:
    def __init__(self) -> None:
        self.models = {"iris_classifier": IrisClassifier}
        
        
    def get(
        self,
        name: str,
        model_params: "DictConfig",
        training_params: "DictConfig",
        artefact_dir: str,
        logger: "logging.Logger",
    ) -> "Model":
        return self.models[name](model_params, training_params, artefact_dir, logger=logger)