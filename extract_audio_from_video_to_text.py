"""
Extract audio from video and convert to text
"""
import speech_recognition as sr
import moviepy.editor as mp

# Step 2 — Video to Audio Conversion
clip = mp.VideoFileClip(r"Python_Crash_Course.mp4")
clip.audio.write_audiofile(r"Python_Crash_Course.wav")

# Step 3 — Speech Recognition
# Size of wave must be less than 10Mb
r = sr.Recognizer()
audio = sr.AudioFile("Python_Crash_Course.wav")

with audio as source:
    audio_file = r.record(source)

result = r.recognize_google(audio_file)

# Final Step — Exporting the Result
# exporting the result
with open('recognized.txt',mode ='w') as file:
    file.write("Recognized Speech:")
    file.write("\n")
    file.write(result)
    print("ready!")
