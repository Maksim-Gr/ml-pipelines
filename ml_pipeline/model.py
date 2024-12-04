from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pandas as pd
    
from abc import ABC

class Model(ABC):
    _model: None
    
    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, value) -> None:
        self._model = value
        
    @classmethod
    def load(self) -> None:
        pass
    
    @classmethod
    def train(self, X: "pd.DataFrame", y: "pd.Series") -> None:
        pass
    
    @classmethod
    def evaluate(self) -> None:
        pass
    
    @classmethod
    def create_report(self, artefact_path: str) -> None:
        pass
    
    @classmethod
    def save(self) -> None:
        pass 