from sklearn import decomposition
import os
import numpy as np
import csv

############ 1. Read the excel file and normalize them

for i in range(1,20):

	excel = open("2016 IPO Performance for PCA and ML analysis.csv","r")

	data = csv.reader(excel)

	data_list = []

	for row in data:

		new_list = []

		for i in row:

			new_list.append(float(i))

		data_list.append(new_list)

	data = np.reshape(data_list,(len(data_list),len(data_list[0])))


	data[:,len(data_list[0])-1] = ((data[:,len(data_list[0])-2]) <= (data[:,len(data_list[0])-1])).astype(np.float32)



	for j in list(range(0,len(data_list[0])-1)):

		data[:,j] = (data[:,j] - data[:,j].mean())/(data[:,j].std())


############ 2. PCA

X = data[:,0:7]
pca = decomposition.PCA(n_components=2)
print "raw data:"
print X
pca.fit(X)
print "\nvariance ratio:"
print(pca.explained_variance_)
print "\ncomponent"
print pca.components_
New_X = pca.transform(X)
print "\nNew vector"
print New_X




"""
clf = RandomForestClassifier(n_estimators=200)

clf.fit(data[0:batch_size,0:7], np.ravel(data[0:batch_size,7]))

pred = clf.predict(data[batch_size:,0:7])


print confusion_matrix(np.reshape(data[batch_size:,7],(len(data)-batch_size,1)), pred)


print clf.feature_importances_


"""






