import os
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocessor_obj_filepath = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(drop_first = True)),
                    ("scaler", StandardScaler())
                ]
            )
            logging.info("Numerical columns standard scaling completed successfully.")
            logging.info("Categorical columns encoding and standard scaling completed successfully.")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, numerical_columns),
                    ("cat_pipeline", cat_pipeline, categorical_columns)
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            traindf = pd.read_csv(train_path)
            testdf = pd.read_csv(test_path)
            logging.info("Read Train and Test data succesfully.")
            logging.info("Obtaining preprocessing object.")

            preprocessor_obj = self.get_data_transformer_obj()
            target_column = "math_score"
            numerical_columns = ["writing_score", "reading_score"]
        
            input_feature_traindf = traindf.drop(columns = [target_column], axis = 1)
            target_feature_traindf = traindf[target_column]

            input_feature_testdf = testdf.drop(columns = [target_column], axis = 1)
            target_feature_testdf = testdf[target_column]

            logging.info(f"Applying the preprocessing object on traindf and testdf.")

            



        except Exception as e:
            raise CustomException(e, sys)

