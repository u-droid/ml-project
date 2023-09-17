import os
import sys
import pickle
import numpy as np
import pandas as pd

from sklearn.metrics import r2_score
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        file = open(file_path, "wb")
        pickle.dump(object, file)
        file.close()
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        evaluation = dict()
        for name, model in models.items():
            param_grid = params.get(name, {})
            logging.info(f'Training model {name} using param grid: {param_grid}')
            gs = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
            gs.fit(X_train, y_train)
            logging.info(f'Model({name}) Best Params: {gs.best_params_} Best score: {gs.best_score_}')
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            predicted = model.predict(X_test)
            evaluation[name] = r2_score(y_test, predicted)
        return evaluation
    except Exception as e:
        raise CustomException(e, sys)
