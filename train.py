import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
print("Loading dataset")
CSV = "indian_job_listings_dataset.csv"
df = pd.read_csv(CSV)
df['combined'] = (
    df['title'].fillna('')+ ' ' +
    df['company_name'].fillna('')+ ' ' +
    df['description'].fillna('')+ ' ' +
    df['requirements'].fillna('')+ ' ' +
    df['salary_range'].fillna('')+ ' ' +
    df['employment_type'].fillna('')
)
X = df['combined']
Y = df['fraudulent']
vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)
X_train, X_test, Y_train, Y_test = train_test_split(X_vectorized, Y, test_size=0.2, random_state=42, stratify=Y)
print("Loading Model")
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, Y_train)
Y_pred = model.predict(X_test)
acc = accuracy_score(Y_pred,Y_test)
print(f"Accuracy Score: {100*acc:.2f}%")
print("\n Classification Report")
print(classification_report(Y_test, Y_pred, target_names=["REAL JOB", "FAKE JOB"]))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(model, open("model.pkl", "wb"))
print("model, vectorizer saved as pkl to avoid retraining")
