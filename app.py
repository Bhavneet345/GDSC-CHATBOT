from flask import Flask, render_template , request
from main import GenericAssistant
import google_scrape

app = Flask(__name__,template_folder='templates')

@app.route('/', methods= ['GET', 'POST'])
def home():
    res = ''
    message = ''
    if request.method == 'POST':
        assistant = GenericAssistant('intents.json', model_name="test_model")
        assistant.load_model()
        message = request.form.get('size')
        res = assistant.request(message)
        if res == "I don't understand!":
            res = google_scrape.any_answer(message)
        
    
    return render_template('index.html', botResponse = res, userMessage = message)

if __name__=='__main__':
    app.run(debug = True)