# $ youtube-dl -f 18 'https://www.youtube.com/watch?v=JJmcL1N2KQs'
import moviepy.editor as mp

my_clip = mp.VideoFileClip(r"Python_Crash_Course.mp4")
print(my_clip)
my_clip.audio.write_audiofile(r"Python_Crash_Cource.mp3")
