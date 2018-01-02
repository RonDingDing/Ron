
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from watchdog.observers import Observer
from watchdog.events import *
import time

class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        with open('D:/1.txt', 'a') as f:            
            if event.is_directory:
                f.write("directory moved from {0} to {1}\n".format(event.src_path,event.dest_path))
            else:
                f.write("file moved from {0} to {1}\n".format(event.src_path,event.dest_path))

    def on_created(self, event):
        with open('D:/1.txt', 'a') as f:   
            if event.is_directory:
                f.write("directory created:{0}\n".format(event.src_path))
            else:
                f.write("file created:{0}\n".format(event.src_path))

    def on_deleted(self, event):
        with open('D:/1.txt', 'a') as f:   
            if event.is_directory:
                f.write("directory deleted:{0}\n".format(event.src_path))
            else:
                f.write("file deleted:{0}\n".format(event.src_path))

    def on_modified(self, event):
        with open('D:/1.txt', 'a') as f:
            if event.is_directory:
                f.write("directory modified:{0}\n".format(event.src_path))
            else:
                f.write("file modified:{0}\n".format(event.src_path))

if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler,"d:/dcm",True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
