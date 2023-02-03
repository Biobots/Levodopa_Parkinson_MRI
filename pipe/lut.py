from sklearn.svm import SVC
from xgboost.sklearn import XGBClassifier

from pipe.img_feature import test_pca

import scikitplot as skplt

from sklearn import metrics

def class2_roc_auc_score(y_true, y_score):
    y_pred = y_score[:, 1]
    return metrics.roc_auc_score(y_true=y_true, y_score=y_pred)

Model_LUT = {
    'svc': SVC,
    'xgboost': XGBClassifier
}

Metrics_LUT = {
    'AUC': class2_roc_auc_score
}

Plot_LUT = {
    'plot_roc': skplt.metrics.plot_roc,
    'plot_confusion_matrix': skplt.metrics.plot_confusion_matrix
}

Feature_LUT = {
    'test_pca': test_pca
}