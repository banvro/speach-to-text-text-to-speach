import speech_recognition as sr

def convert_to_text(file_path):
    r = sr.Recognizer()
    audio = sr.AudioFile(file_path)
    with audio as source:
        audio_text = r.record(source)
    return r.recognize_google(audio_text)


from pydub import AudioSegment
sound = AudioSegment.from_mp3("/home/krissroot/Downloads/hlodata.mp3")
sound.export("/home/krissroot/Desktop/testing/ffprobe/hlodata.wav", format="wav")
text = convert_to_text("/home/krissroot/Desktop/testing/ffprobe/hlodata.wav")

# some_model.objects.create(audio_text=text)

print(text, "::::::::::::::::::")