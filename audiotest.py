# this macro is used to extract auido from the video files. ffmpeg need to be downloaded kept in C:\Windows\ffmpeg" 
# this has to be added in Path variables. path= C:\Windows\ffmpeg\bin
#and then pip install python-ffmpeg.

import ffmpeg
for id in range (5,50,5):
     start_time = '00:'+str(id)+':10' # Start time for trimming (HH:MM:SS)
     end_time = '00:'+str(id+5)+':20' # End time for trimming (HH:MM:SS)
     print(start_time)
     print(end_time)
     (
         ffmpeg.input("C:/Users/arpuste/Downloads/KT20230712.mp4",ss=start_time, to=end_time)
         .output("output"+str(id)+".wav").run()
     )