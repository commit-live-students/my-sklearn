import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

class my_sklearn():
    def __init__(self, path, is_header, target_variable, feature_names=None, random_state=7):

        self.path = path
        self.is_header = is_header
        self.target_variable = target_variable
        self.feature_names = feature_names
        self.random_state = random_state

        self.names = None
        self.header = 0
        pass

    def __repr__(self):
        pass

class my_sklearn(my_sklearn):
    def load_data(self, feature_subset=None, CV_subset="train", train_size=0.8):

        self.feature_subset = feature_subset
        self.CV_subset = CV_subset
        self.train_size = train_size
        pass