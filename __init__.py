from main import GenericAssistant
import google_scrape

assistant = GenericAssistant('intents.json', model_name="test_model")
assistant.load_model()
#assistant.train_model()
#assistant.save_model()

done = False

while not done:
    message = input("Enter a message: ")
    if message == "STOP":
        done = True
    else:
        res=assistant.request(message)
        if res != "I don't understand!":
            print(res)
            ch=input("Are you satisfied with the response (y/n)? : ")
            if ch.lower()=="n":
                google_scrape.any_answer(message)
        else:
            res = google_scrape.any_answer(message)
            print(res)