# import libraries
import data_handler as dh
from sklearn.tree import DecisionTreeRegressor
from joblib import dump


# get data
x_train, x_test, y_train, y_test = dh.get_data("./insurance.csv")

# fit model
clf = DecisionTreeRegressor(random_state=0)
clf.fit(x_train, y_train)

#save model
dump(clf, './data/best_model.joblib') 


print(clf)