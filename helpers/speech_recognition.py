import speech_recognition as sr
from json import loads

recognition_options = loads(open("constants/recognition_options.json").read())


class SpeechRecognition():

    def __init__(self, type):
        self.type = type

    def recognize(self):
        if (self.type == recognition_options["MIC"]):
            return self._recognize_mic()
        else:
            return self._recognize_audio()

    def _recognize_mic(self):
        rec = sr.Recognizer()

        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print("Start recognizing [MIC]")
            audio = rec.listen(mic)
            try:
                text = rec \
                    .recognize_google(audio, language='pt-BR')
                return text
            except sr.UnknownValueError:
                return ""

    def _recognize_audio(self):
        return ""
