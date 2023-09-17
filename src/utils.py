import os
import sys
import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from src.logger import logging
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        file = open(file_path, "wb")
        pickle.dump(object, file)
        file.close()
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models):
    try:
        evaluation = dict()
        for name, model in model.items():
            model.fit(X_train, y_train)
            predicted = model.predict(X_test)
            evaluation[name] = r2_score(y_test, predicted)
        return evaluation
    except Exception as e:
        raise CustomException(e, sys)
