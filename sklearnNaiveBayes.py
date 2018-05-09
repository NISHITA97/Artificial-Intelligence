#implementation of naiveBayes algorithm
from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import GaussianNB
#c:\Python27\python.exe c:\Python27\sklearnNaiveBayes.py
cancer = datasets.load_breast_cancer();
print len(cancer['target']);
features = cancer['data'];
labels = cancer['target'];

train_feat, test_feat, train_label, test_label = tts(features,labels,test_size=0.2);
print len(train_feat);
print train_feat;

gnb = GaussianNB();
predict = gnb.fit(train_feat, train_label).predict(test_feat);
score=0;
for j in range(len(predict)):
    if(predict[j]==test_label[j]):
        score+=1;
acc = score / (1.0 * len(test_label));
print acc 
