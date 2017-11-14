import pandas as pd
from sklearn.cross_validation import train_test_split



df = pd.read_table('smsspamcollection/SMSSpamCollection',
				sep='\t',
				header=None, 
				names=['label', 'sms_message'])

df['label'] = df.label.map({'ham':0, 'spam': 1})

x_train, x_test, y_train, y_test = train_test_split(df['sms_message'], 
													df['label'],
													random_state=1)

print('Number of rows in the total set: {}'.format(df.shape[0]))
print('Number of rows in the training set: {}'.format(x_train.shape[0]))
print('Number of rows in the test set: {}'.format(x_test.shape[0]))
