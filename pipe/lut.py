from sklearn.svm import SVC
from sklearn.linear_model import Lasso, LinearRegression
from xgboost.sklearn import XGBClassifier

from pipe.img_feature import gen_pca, load_radiomics

import scikitplot as skplt
import matplotlib.pyplot as plt

from sklearn import metrics

import numpy as np
import seaborn as sns

import functools

def class2_roc_auc_score(y_true, y_score):
    y_pred = y_score[:, 1]
    return metrics.roc_auc_score(y_true=y_true, y_score=y_pred)

def plot_r2(y_true, y_score):
    return sns.regplot(x=y_true, y=y_score)

def plot_confusion_matrix(y_true, y_score):
    mat = metrics.confusion_matrix(y_true, y_score)
    mat = mat.astype('float') / mat.sum(axis=1)[:, np.newaxis]
    return sns.heatmap(mat, square=True, annot=True, cmap=sns.color_palette("Blues", as_cmap=True))

Model_LUT = {
    'svc': SVC,
    'xgboost': XGBClassifier,
    'lasso': Lasso,
    'linear': LinearRegression
}

Metrics_LUT = {
    'AUC': class2_roc_auc_score,
    'r2': metrics.r2_score
}

Plot_LUT = {
    'plot_roc': skplt.metrics.plot_roc,
    'plot_confusion_matrix': plot_confusion_matrix,
    'plot_r2': plot_r2
}

Feature_LUT = {
    't1_pca': gen_pca,
    'gm_pca': gen_pca,
    'wm_pca': gen_pca,
    'test_radiomic': load_radiomics
}