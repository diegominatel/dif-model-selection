import math
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
from aif360.sklearn.inprocessing import AdversarialDebiasing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

def set_configs(n_columns):
    
    adversarial_debiasing = {
        'AD' : [AdversarialDebiasing,
                {'prot_attr' : ['Group'],
                 'num_epochs' : list(range(50, 257, 7)),
                 'random_state' : [42]}]
    }
    
    decision_tree = {
        'DT' : [DecisionTreeClassifier,
                {'criterion' : ['gini'],
                 'min_samples_leaf' : list(range(1, 31)),
                 'min_samples_split' : [5], 
                 'random_state' : [42]}]
    }
    
    knn = {
        'KNN' : [KNeighborsClassifier,
                 {'n_neighbors' : list(range(3, 62, 2))}]
    }
    
    mlp = {
        'MLP' : [MLPClassifier,
                 {'hidden_layer_sizes' : list(range(5, 35, 1)),
                  'random_state' : [42]}]
    }
    
    random_forest = {
        'RF' : [RandomForestClassifier,
                {'n_estimators' : list(range(50, 500, 15)),
                 'min_samples_split' : [math.floor(abs(math.sqrt(n_columns - 1)))], 
                 'random_state' : [42]}]
    }
    
    xgb = {
        'XGB' : [XGBClassifier,
                 {'n_estimators' : list(range(50, 500, 15)),
                  'random_state' : [42]}]
    }
    
    
    all_configs = {
        'ad'     : adversarial_debiasing,
        'dt'    : decision_tree,
        'knn'   : knn,
        'mlp'   : mlp,
        'rf'    : random_forest,
        'xgb'   : xgb,
    }
    
    return all_configs