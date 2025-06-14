"""
Python Alarm Clock ⏰

Author: Abinash Prasana

A simple terminal-based alarm clock that:
- Lets users set a specific time (HH:MM:SS)
- Plays an alarm sound when the time is reached
- Demonstrates time handling and basic audio playback using pygame
"""

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file =  "alarm_clock.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("WAKE UP😩")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False
        time.sleep(1)

if __name__ == "__main__":
    al_time = input("Enter the alarm time(HH:MM:SS): ")
    set_alarm(al_time)