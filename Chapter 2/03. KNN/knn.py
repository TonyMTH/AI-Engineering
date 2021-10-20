import numpy as np
class KNN:
    k = 1
    X,y = 0,0

    def __init__(self,k):
        self.k = k
    
    def fit(self,X,y):
        self.X = X
        self.y = y
        return self

    def __get_eucledian_distance(self,v1,v2):
        return np.linalg.norm(v1 - v2)

    def evaluate(self,y, y_p):
        return sum(y == y_p) / len(y)

    def __predict_one(self,x_test):
        dist = []
        for id,y in enumerate(self.y):
            dist.append([y,self.__get_eucledian_distance(self.X[id],x_test)])
        y_items = np.array(sorted(dist, key=lambda x: x[-1])[:self.k])[:,0]
        y_items = list(y_items)
        return max(set(y_items), key=y_items.count)

    def predict(self,x_test):
        y_pred = []
        for x in x_test:
            yp = self.__predict_one(x)
            y_pred.append(yp)
        return np.array([int(i) for i in y_pred])
