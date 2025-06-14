"""
Simulated File Downloader with Multithreading

Author: Abinash Prasana

This program demonstrates multithreading by simulating parallel file downloads.
Each file download is represented by a thread, and the total download time is randomized
to mimic real-world asynchronous operations.
"""

import threading
import time
import random

class FileDownloader(threading.Thread):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def run(self):
        print(f"Starting downloading {self.file_name}......")
        download_time = random.randint(2,6)
        time.sleep(download_time)
        print(f"Finished downloading {self.file_name} in {download_time} seconds.")

def main():
    files = ["Dcoument.pdf", "Photo.png","Music.mp3","Video.mp4","Data.csv"]
    threads = []
    print("\n ---- Starting downloads ----\n")

    for file in files:
        thread = FileDownloader(file)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("\n ---- All downloads completed ----\n")

if __name__ == "__main__":
    main()