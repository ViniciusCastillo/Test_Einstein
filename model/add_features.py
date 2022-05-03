import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class add_features(BaseEstimator, TransformerMixin):
  """
  Add features to make the model have a better result
  ________________________________________________________________________________________________________________
  PARAMETERS
  ----------
  None
  ________________________________________________________________________________________________________________
  ATTRIBUTES
  ----------
  x13_max: float
      value to substitute infinity values in x13
  x23_max: float
      value to substitute infinity values in x23
  x12_max: float
      value to substitute infinity values in x12

  """
  def __init__( self):
    self.x13_max = None
    self.x23_max = None
    self.x12_max = None

  def fit( self, X, y = None):
    """
    fit the model, setting x13_max, x23_max,  x12_max
    ________________________________________________________________________________________________________________
    INPUT
    -----
    X: DataFrame
        features dataset
    y: Series
        target series. It will not be used.
    ________________________________________________________________________________________________________________
    OUTPUT
    ------
    add_features object
        add_features fitted model
        
    """
    X_ = X.copy()
    X_['x13'] = X_['x1']/X_['x3']
    X_['x23'] = X_['x2']/X_['x3']
    X_['x12'] = X_['x1']/X_['x2']
    self.x13_max = X_.loc[X_['x13'] != np.inf, 'x13'].max()*2
    self.x23_max = X_.loc[X_['x23'] != np.inf, 'x23'].max()*2
    self.x12_max = X_.loc[X_['x12'] != np.inf, 'x12'].max()*2

    return self 
    
  def transform(self, X, y = None):
    """
    add features to the X DataFrame
    ________________________________________________________________________________________________________________
    INPUT
    -----
    X: DataFrame
        features dataset
    y: Series
        target series. It will not be used.
    ________________________________________________________________________________________________________________
    OUTPUT
    ------
    DataFrame
        X with the features added
        
    """
    X_ = X.copy()
    X_['x13'] = X_['x1']/X_['x3']
    X_['x23'] = X_['x2']/X_['x3']
    X_['x12'] = X_['x1']/X_['x2']
    X_['x1^2'] = X_['x1']**2
    X_['x2^2'] = X_['x2']**2
    X_['x3^2'] = X_['x3']**2
    X_['x1^3'] = X_['x1']**3
    X_['x2^3'] = X_['x2']**3
    X_['x3^3'] = X_['x3']**3
    X_['log(x1-min(x1)+1)'] = (X_['x1']-X_['x1'].min()+1).transform(np.log)
    X_['log(x2-min(x2)+1)'] = (X_['x2']-X_['x2'].min()+1).transform(np.log)
    X_['log(x3-min(x3)+1)'] = (X_['x3']-X_['x3'].min()+1).transform(np.log)
    X_.x13.replace(np.inf, self.x13_max, inplace=True)
    X_.x23.replace(np.inf, self.x23_max, inplace=True)
    X_.x12.replace(np.inf, self.x12_max, inplace=True)

    return X_