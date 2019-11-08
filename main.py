from snowboy import snowboydecoder
import sys
import signal

interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    print('hotword detected')
    return interrupted

model = './snowboy/resources/models/snowboy.umdl'

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5, audio_gain=1)
print('Listening... Press Ctrl+C to exit')

detector.start(detected_callback=snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
