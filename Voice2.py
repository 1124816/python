import speech_recognition as sr
import pyaudio
import pocketsphinx


# obtain audio from the microphone
r = sr.Recognizer()
r.dynamic_energy_threshold = True
r.energy_threashhold = 7000

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))



# recognize speech using Sphinx
#try:
#    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
#except sr.UnknownValueError:
#    print("Sphinx could not understand audio")
#except sr.RequestError as e:
#    print("Sphinx error; {0}".format(e))
#
# recognize speech using Google Speech Recognition

## recognize speech using Wit.ai
#WIT_AI_KEY = "AYZIK5YUO5AN2EHOJPIELBIU74VF43WX" # Wit.ai keys are 32-character uppercase alphanumeric strings
#try:
#    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
#except sr.UnknownValueError:
#    print("Wit.ai could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Wit.ai service; {0}".format(e))
#
