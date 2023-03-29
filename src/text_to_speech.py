import pyttsx3

def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")

    return engine

def respond(engine, message):
    print(message)

    engine.say(message)
    engine.runAndWait()
