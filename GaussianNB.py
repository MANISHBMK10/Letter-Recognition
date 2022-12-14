import pandas as pd
from yellowbrick.classifier import ConfusionMatrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

#Mention ur path
#url = "https://drive.google.com/drive/folders/1B8VZqUnNsaJ_hrE2CcyRFipI753O7kxd"
path= r"C:\Users\SRAVAN CHAITANYA C\Desktop\Letter - Recognition\letterrecog.csv"

names = ['class',
         'x-box',
         'y-box',
         'width',
         'high',
         'onpix',
         'x-bar',
         'y-bar',
         'x2bar',
         'y2bar',
         'xybar',
         'x2ybr',
         'xy2br',
         'x-ege',
         'xegvy',
         'y-ege',
         'yegvx']

dataset = pd.read_csv(path, names=names)

# shape
print('Dimension of data set',dataset.shape)
 #print(dataset.shape)

# Generate various summary statistics
print('statistics of Data set\n',dataset.describe())

#group by class
print('class distribution',dataset.groupby('class').size())


# histograms
dataset.hist()
plt.show()

array = dataset.values
print("array",array);
X = array[:, 1:17]
Y = array[:, 0]

print('X matrix dimensionality:', X.shape)
print('Y vector dimensionality:', Y.shape)

# split the data into a training set and a test set
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=0.20,
                                                                                random_state=10)
print("X_train:\n ", X_train)
print("X_validation:\n ", X_validation)
print("Y_train:\n ", Y_train)
print("Y_validation: \n", Y_validation)


gaussianNB = GaussianNB()

cm = ConfusionMatrix(gaussianNB, classes="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(','))

# train the model using the training sets
cm.fit(X_train, Y_train)

cm.score(X_validation, Y_validation)

# predict the responses for test dataset
predictions = cm.predict(X_validation)

# accuracy classification score
print("Accuracy: ", accuracy_score(Y_validation, predictions))

# compute confusion matrix
print(confusion_matrix(Y_validation, predictions))

# text report showing the main classification metrics
print(classification_report(Y_validation, predictions, digits=5))

cm.poof()
