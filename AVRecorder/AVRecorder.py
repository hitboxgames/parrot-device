import time
from datetime import datetime
import threading
import subprocess
import os

from AudioRecorder import AudioRecorder
from VideoRecorder import VideoRecorder

def record_time_block():
    file_name = str(datetime.now()).replace(" ", "_")
    
    start_AVrecording(file_name)
    time.sleep(240)
    stop_AVrecording(file_name)
    
def start_AVrecording(file_name):
    print("Starting threads...")
    video_thread.start(file_name, tmp_dir)
    audio_thread.start(file_name, tmp_dir)
    
def stop_AVrecording(file_name):
    print("Stopping threads...")
    audio_thread.stop()
    video_thread.stop()
    
    print("conversion starting")
    cmd = "ffmpeg -i {1}/{0}.wav -i {1}/{0}.h264 -c:v copy -c:a aac -strict experimental {2}/{0}.mp4".format(file_name, tmp_dir, final_dir)
    subprocess.call(cmd, shell=True)
    print("you did it bastard")

def main():
    print("init main")
    global video_thread
    global audio_thread
    global tmp_dir
    global final_dir
    
    #tmp_dir = '/home/raulfaife/Desktop/temp'
    #final_dir = 'home/raulfaife/Desktop/Recorded_Videos/mp4/'
    
    tmp_dir = os.path.expanduser('~/tmp_media')
    if(os.path.isdir(tmp_dir) == False):
        print("Can't find tmp media directory, creating...")
        os.mkdir(tmp_dir)
    
    final_dir = os.path.expanduser('~/media/')
    if(os.path.isdir(final_dir) == False):
        print("Can't find media directory, creating...")
        os.mkdir(final_dir)

    
    video_thread = VideoRecorder()
    audio_thread = AudioRecorder()
    
    time.sleep(2)
    
    while False:
        record_time_block()

if __name__ == "__main__":
    main()
