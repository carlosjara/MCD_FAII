# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
import seaborn as sns

class TukeysOutlierReplacer(BaseEstimator, TransformerMixin):
    def __init__(self, variable):
        self.variable = variable
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        q1 = X[self.variable].quantile(0.25)
        q3 = X[self.variable].quantile(0.75)
        iqr = q3 - q1
        inner_fence = 1.5 * iqr
        
        # Calculate inner fence limits
        inner_fence_le = q1 - inner_fence
        inner_fence_ue = q3 + inner_fence
        
        # Replace outliers with nearest value within inner fence
        X_replaced = X.copy()
        X_replaced[self.variable] = np.where(X_replaced[self.variable] < inner_fence_le, inner_fence_le, X_replaced[self.variable])
        X_replaced[self.variable] = np.where(X_replaced[self.variable] > inner_fence_ue, inner_fence_ue, X_replaced[self.variable])
        
        return X_replaced



