import csv

from models.deep.cnn import CNNModel
from utils.read_data import get_data_full

labels = ['business/finance', 'education/research', 'entertainment', 'health/medical',
          'news/press', 'politics/government/law', 'sports', 'tech/science']

X_train, y_train, X_test, test_hosts = get_data_full()

model = CNNModel()

model.fit(X_train, y_train)
print('Model trained')
y_pred = model.predict_proba(X_test)

with open('./submissions.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    lst = model.classes_.tolist()
    lst.insert(0, "Host")
    writer.writerow(lst)
    for i,test_host in enumerate(test_hosts):
        lst = y_pred[i,:].tolist()
        lst.insert(0, test_host)
        writer.writerow(lst)

print('Submission written successfully')