from sklearn.svm import SVC
from xgboost.sklearn import XGBClassifier

from pipe.img_feature import test_pca

Model_LUT = {
    'svc': SVC,
    'xgboost': XGBClassifier
}

Feature_LUT = {
    'test_pca': test_pca
}