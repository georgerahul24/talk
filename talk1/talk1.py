"""This package is a text to speech synthesiser"""
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty(
    "voice", voices[1].id)  # changing index, changes voices. 1 for female
rate = engine.getProperty("rate")  # getting details of current speaking rate
engine.setProperty("rate", 135)  # setting up new voice rate


def talk(speak)->None:
    """A function for text to speech functionality"""
    engine.say(speak)
    engine.runAndWait()
    del speak


def multithreadtalk(speak)->None:
    """A function for multithreaded text to speech functionality"""
    # Still in prototype
    # for multi threading else the runtime error of loop still running will come
    try:
        engine.endLoop()
    except:
        pass
    engine.say(speak)
    engine.runAndWait()
    engine.stop()
