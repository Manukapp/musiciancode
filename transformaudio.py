from pydub import AudioSegment

#TRANSFORM m4a to wav files

m4a = "D:\\Material\\Nina\\Voice 028.m4a"
wav= r"D:\\Material\\Nina\\Nina2.wav"

#wav = "D:\\2018-2019 releases\\2022\MasterFinal\\Rap\\Manukapp_Remix_On_Air.wav"
#mp3 = "D:\\2018-2019 releases\\2022\MasterFinal\\Rap\\Manukapp_Remix_On_Air.mp3"
#aif = "D:\\FL STUDIO PROJECTS\\sem1_2023\\CORAZONDEMELON_mixing\\CORAZONDEMELON_master3_19-02-23.wav"
#mp3 = "D:\\FL STUDIO PROJECTS\\sem1_2023\\CORAZONDEMELON_mixing\\CORAZONDEMELON_master3_19-02-23.mp3"
track = AudioSegment.from_file( m4a, format='m4a' )
file_handle = track.export( wav, format='wav' )

print("Successful audio conversion")