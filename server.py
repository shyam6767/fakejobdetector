from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# load both pkl files once when server starts
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

@app.route("/health")
def health():
    return "ok", 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    
    # vectorize input text
    X = vectorizer.transform([text])
    
    # predict
    prediction = model.predict(X)[0]
    
    if prediction == 1:
        result = "FAKE"
    else:
        result = "REAL"
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))