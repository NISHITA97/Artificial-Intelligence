//implementation of knn algorithm
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.neighbors import KNeighborsClassifier
#c:\Python27\python.exe c:\Python27\sklearn2KNN.py
cancer = datasets.load_breast_cancer();
print len(cancer['target']);
features = cancer['data'];
labels = cancer['target'];

train_feat, test_feat, train_label, test_label = tts(features,labels,test_size=0.2);
print len(train_feat);
print train_feat;


for k in range(1,10):
    neigh = KNeighborsClassifier(n_neighbors=k,weights='uniform', algorithm='auto')
    neigh.fit(train_feat, train_label);
    predict = neigh.predict(test_feat);
    score=0;
    for j in range(len(predict)):
        if(predict[j]==test_label[j]):
            score+=1;
    acc = score / (1.0 * len(test_label));
    print acc , " for k= " , k;
