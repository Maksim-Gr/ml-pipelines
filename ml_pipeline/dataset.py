from abc import ABC

import pandas as pd


class DataSet(ABC):
    _name: str
    _df: pd.DataFrame
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value) -> None:
        self._name = value
        
    @property
    def df(self) -> "pd.DataFrame": 
        return self._df
    
    @df.setter
    def df(self, value) -> None:
        self._df = value
        
    
    @classmethod
    def load(self) -> None:
        """Implemented in Mixin"""
        pass
    
    @classmethod
    def save(self) -> None:
        """Implemented in Mixin"""
        pass
    
    @classmethod
    def preprocess(self) -> None:
        pass
    
    @classmethod
    def feature_engineering(self) -> None:
        pass