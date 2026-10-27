import numpy as np
from math import sqrt
from collections import Counter

"""
def kNN_classify(k, X_train, y_train, x):
    distances = []
    for x_train in X_train:
        d = sqrt(np.sum((x_train - x)**2))   #欧拉距离
        distances.append(d)
    np.argsort(distances)
    nearest = np.argsort(distances)
    topK_y = [y_train[i] for i in nearest[:k]]
    Counter(topK_y)
    votes = Counter(topK_y)
    votes.most_common(2)
    votes.most_common(1)
    predict_y = votes.most_common(1)[0][0]
    return predict_y
"""
class KNNClassifier:
    def __init__(self, k):
        self.k = k
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    def predict(self, x):

    def _predict(self, x):
        print(self.X_train, self.y_train)
        distances = []
        for x_train in self.X_train:
            d = sqrt(np.sum((x_train - x)**2))   #欧拉距离
            distances.append(d)
        nearest = np.argsort(distances)
        topK_y = [self.y_train[i] for i in nearest[:self.k]]
        votes = Counter(topK_y)
        predict_y = votes.most_common(1)[0]
        return predict_y


if __name__ == "__main__":
    pass


### 使用scikit-learn中的kNN（标准流程）

