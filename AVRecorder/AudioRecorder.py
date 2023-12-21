import threading
from subprocess import call

class AudioRecorder():
    
    def __init__(self):
        print("init audio")
        self.file_name = 'default_name'
        self.p = None
        command = 'killall arecord'
        call([command], shell=True)
    
    def record(self):
        print("started recording audio")
        command = 'arecord -D plughw:1,0 ' + self.file_name
        call([command], shell=True)
        
    def stop(self):
        command = 'killall arecord'
        call([command], shell=True)
        print("stopped recording audio")
    
    def start(self, file_name, file_dir):
        self.file_name = '{}/{}.wav'.format(file_dir, file_name)
        
        audio_thread = threading.Thread(target=self.record)
        audio_thread.start()