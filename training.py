import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import pickle

# load the data
df = pd.read_csv('duplicateDetectionSet.csv')
df = df.fillna('', inplace=False)
# test_df = pd.read_csv('Test set.csv')

# preprocess the data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['question1'] + ' ' + df['question2'])
y = df['is_duplicate']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# choose a model
model = LogisticRegression(max_iter=1000)

# train the model
model.fit(X_train, y_train)

# save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# evaluate the model
y_pred = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))
print('F1-score:', f1_score(y_test, y_pred))

# predict on new data
new_questions = ['How can I train a machine learning model?', 'What is the best way to train a machine learning model?']
X_new = vectorizer.transform(new_questions)
y_new = model.predict(X_new)
print(y_new)
