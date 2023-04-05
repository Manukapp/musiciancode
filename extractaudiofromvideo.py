import moviepy
import moviepy.editor

#EXTRACT AUDIO FROM VIDEO

video = moviepy.editor.VideoFileClip("D:\\Material\\LeoGuitar\\20221202_215053.mp4")
audio = video.audio
audio.write_audiofile("D:\\Material\\LeoGuitar\\oldfrenchiefilm.wav")

print("Extracted audio from video")

