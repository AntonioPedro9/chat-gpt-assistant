import time
from speech_to_text import initialize_recognizer, recognize_speech
from openai_api import query_openai
from text_to_speech import initialize_engine, respond

def assistant():
    engine = initialize_engine()
    recognizer = initialize_recognizer()
    wake_word = "chuchu"

    while True:
        text = recognize_speech(recognizer)

        if wake_word in text.lower():
            message = query_openai(text)
            respond(engine, message)

        time.sleep(1)

assistant()
