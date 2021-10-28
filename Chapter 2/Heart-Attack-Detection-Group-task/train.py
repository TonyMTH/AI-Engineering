# import libraries
import data_handler as dh
from joblib import dump
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt


# get data
data_path = './data/heart.csv'
x_train, x_test, y_train, y_test = dh.get_data(data_path)

#Normalize data
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

#fit svm
model = svm.SVC()
model.fit(x_train,y_train)

#check initial accuracy
acc_train = model.score(x_train,y_train)
acc_test = model.score(x_test,y_test)
y_pred = model.predict(x_test)

print("Train Accuracy: {},\tTest Accuracy: {}".format(round(acc_train,2), round(acc_test,2)))

print("Recall Score (TP / (TP + FN)): {}%".format( round(recall_score(y_test, y_pred)*100,2) ) )

#save model
dump(model, './data/best_model.joblib')
dump(scaler, './data/scaler.joblib')

#plot confusion matrix
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No', 'Yes'])
disp.plot()
plt.show()
