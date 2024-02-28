import pygame
import time
jjjsjsj
def play_arm_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sound.mp3")  
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10) 

def set_alarm(alarm_time):
    current_time = time.strftime("%H:%M")
    print(f"Current time: {current_time}")
    print(f"Alarm set for: {alarm_time}")

    while True:
        if time.strftime("%H:%M") == alarm_time:
            print("Wake Up ")
            play_alarm_sound()
            break
        time.sleep(1) 

if __name__ == "__main__":
    alarm_time = input("Input the alarm (HH:MM) : ")
    set_alarm(alarm_time)
