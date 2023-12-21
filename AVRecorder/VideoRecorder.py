import threading
import random
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import datetime
from time import sleep
from subprocess import call

class VideoRecorder:
    def __init__(self):
        print("init video")
        self.file_name = 'default_name'
        
        command = 'pkill raspivid'
        call([command], shell=True)
        
        self.camera = Picamera2()
        self.video_config = self.camera.create_video_configuration(main={"size": (1920, 1080)}, controls={'FrameRate': 30.0})
        self.camera.configure(self.video_config)
        self.encoder = H264Encoder(framerate=30, enable_sps_framerate=True)
    
    def record(self):
        self.camera.start_recording(self.encoder, self.file_name)
    
    
    def stop(self):
        self.camera.stop_recording()
    
    def start(self, file_name, file_dir):
        self.file_name = '{}/{}.h264'.format(file_dir, file_name)
        
        video_thread = threading.Thread(target=self.record)
        video_thread.start()
