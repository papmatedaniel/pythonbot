import pyautogui
import time

def main():
    while True:
        # Lenyomja a 2 számot
        pyautogui.press('2')
        print("2 lenyomva")
        
        # Vár 2 másodpercet
        time.sleep(2)

if __name__ == "__main__":
    main()
