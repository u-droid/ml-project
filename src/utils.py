import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException

def save_object(file_path, object):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        file = open(file_path, "wb")
        pickle.dump(object, file)
        file.close()
    except Exception as e:
        raise CustomException(e, sys)
