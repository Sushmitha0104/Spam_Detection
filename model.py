import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pickle

# Load data
data = pd.read_csv('spam.csv', encoding='latin-1')
data = data[['v1', 'v2']]  # Adjust based on actual CSV columns
data.columns = ['Category', 'Message']

# Encode labels
le = LabelEncoder()
data['Category'] = le.fit_transform(data['Category'])

# Split data
x_train, x_test, y_train, y_test = train_test_split(data['Message'], data['Category'], test_size=0.25, random_state=42)

# Create and train model
clf = Pipeline([('vectorizer', CountVectorizer()),
                ('nb', MultinomialNB())
               ])
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

# Print classification report
print(classification_report(y_test, y_pred))

# Save the model to a file
with open('spam_classifier.pkl', 'wb') as f:
    pickle.dump(clf, f)
