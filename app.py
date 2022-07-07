import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from flask import Flask,request,render_template
from sklearn.svm import SVC
ps = PorterStemmer()

app = Flask(__name__)
def transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    words = []
    for i in text:
        if i.isalnum():
            words.append(i)
    y = []
    for i in words:
        if i not in stopwords.words('english'):
            y.append(i)
    final_text = []
    for i in y:
        final_text.append(ps.stem(i))
    return " ".join(final_text) 

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('spam_classification.pkl','rb'))

@app.route('/',methods=['GET','POST'])
def predict_loan_status():
    if request.method=='POST':
        message = request.form['v2'] 
        transformed = transform(message)
        vector_input = tfidf.transform([transformed]).toarray()
        result = model.predict(vector_input)
        if result == 0:
           result = "Spam"
        else:
           result = "Not Spam"
        return render_template("input.html",predictions=str(result))
    return render_template('input.html')
if __name__ == "__main__":
    app.run(debug = True)       
