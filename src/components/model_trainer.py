import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import\
    AdaBoostRegressor,\
    GradientBoostingRegressor,\
    RandomForestRegressor

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
from src.utils import evaluate_models

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer(object):
    """docstring forModelTrain"""

    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = train_array[:,:-1],\
                                            train_array[:,-1],\
                                            test_array[:,:-1],\
                                            test_array[:,-1]
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "LinearRegression": LinearRegression(),
                "K-Neighbours":KNeighborsRegressor(),
                "XGB Regressor": XGBRegressor(),
                "Cat Boost":CatBoostRegressor(),
                "Ada Boost": AdaBoostRegressor()
            }
            model_report:dict  = evaluate_models(X_train, y_train, X_test, y_test, models)
            # To get best model score
            best_model_score = max(sorted(model_report.values()))
            # To get best model name
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score<0.6:
                raise CustomException("No best model found")

            logging.info("Best model found on both training and test dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            predicted = best_model.predict(X_test)
            r2_sq = r2_score(y_test, predicted)
            return r2_sq
        except Exception as e:
            raise CustomException(e, sys)
