import googletrans
import speech_recognition
import gtts
import playsound
recognizer =  speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language="hi")
    print(text)
    
translator = googletrans.Translator()
translation = translator.translate(text,dest="ar")
print(translation.text)
convertedaudio = gtts.gTTS(translation.text, lang="ar")
convertedaudio.save("voices.mp3")
playsound.playsound("voices.mp3")