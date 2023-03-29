import speech_recognition as sr

def initialize_recognizer():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

    return recognizer

def recognize_speech(recognizer):
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        return text
    except:
        print("Não entendi o que você disse.")
        return None
