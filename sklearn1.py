from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn import svm

#c:\Python27\python.exe c:\Python27\sklearn1.py
wine = datasets.load_wine()
features = wine.data;
labels = wine.target;

print "no of entries=" , len(features);
for featurename in wine.feature_names:
    print featurename


#print features;
#print labels

train_feat, test_feat, train_label, test_label = tts(features, labels, test_size=0.4);

clf = svm.SVC();

clf.fit(test_feat, test_label);

predictions = clf.predict(test_feat);

score=0;
i=0;
for p in predictions:
    print p, test_label[i];
    if(p == test_label[i]):
        score+=1;
    i+=1;
print "score=" , score;
print "len= ", len(predictions)
print score/ 100.0;

