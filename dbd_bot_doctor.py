import pyautogui
import time
import keyboard  # Import the keyboard module
import random

# Global variable to track whether the script should run or not
running = False

# Function to print the intro
def intro():
    print("\nWelcome to Dead By Daylight AFK Farming BOT (The Doctor Edition) by")
    print("______ _                               ___           _   _____ _     _ _ _ ")
    print("| ___ \ |                             |_  |         | | /  __ \ |   (_) | |")
    print("| |_/ / |__   __ ___   ___   _  __ _    | |_   _ ___| |_| /  \/ |__  _| | |")
    print("| ___ \ '_ \ / _` \ \ / / | | |/ _` |   | | | | / __| __| |   | '_ \| | | |")
    print("| |_/ / | | | (_| |\ V /| |_| | (_| /\__/ / |_| \__ \ |_| \__/\ | | | | | |")
    print("\____/|_| |_|\__,_| \_/  \__, |\__,_\____/ \__,_|___/\__|\____/_| |_|_|_|_|")
    print("                          __/ |                                            ")
    print("                         |___/                                             ")
    print("Go to Play -> Play as Killer and [ Press F8 to toggle Bot ON/OFF | CTRL + C to Exit ]\n")

# Function to perform right click with specified delay
def right_click(delay):
    pyautogui.mouseDown(button='right')
    time.sleep(delay / 1000)  # Convert delay from milliseconds to seconds
    pyautogui.mouseUp(button='right')
    time.sleep(0.5)

# Function to press and release left ctrl key with specified delay
def press_release_ctrl(duration):
    pyautogui.keyDown('ctrlleft')
    time.sleep(duration / 1000)
    pyautogui.keyUp('ctrlleft')

# Function to perform left click with specified delay
def left_clicks():
    numberOfClicks = random.randint(4, 8)
    for _ in range(numberOfClicks):
        pyautogui.click(button='left')
        time.sleep(1)
    time.sleep(3.5)

# Function to simulate random key press for movement
def random_direction():
    keys = ['w', 'a', 's', 'd']
    key = random.choice(keys)
    pyautogui.keyDown(key)
    delay = random.randint(500, 1500) / 1000  # Convert delay from milliseconds to seconds
    time.sleep(delay)
    pyautogui.keyUp(key)

# Function to click at specified coordinates
def click(x, y):
    pyautogui.moveTo(x, y, 0.5)  # Move cursor to current position
    pyautogui.click(x, y)

# Function to toggle the running state of the script
def toggle_running(event):
    global running
    running = not running
    print(f"Bot {'started' if running else 'stopped'}")

# Main function to execute the script
def main():
    intro()
    try:
        while True:
            if running:
                try:
                    # For 1920 x 1080 resolution
                    click(1823, 917)  # Click Ready
                    click(1819, 1022)  # Click Continue
                    click(1372, 660)  # Click Continue Popup
                    # For 1280 x 720 resolution
                    # click(1216, 612)  # Click Ready
                    # click(1213, 681)  # Click Continue
                    # click(915, 440)  # Click Continue Popup
                    time.sleep(1)
                    # Static Blast
                    press_release_ctrl(3000)
                    # Shock Therapy
                    for _ in range(10):
                        right_click(3000)  # Adjust the delay as needed
                        if(_ % 5 == 0):
                            random_direction()
                    # Adding more Randomness
                    random_direction()
                    left_clicks()
                    random_direction()
                    left_clicks()
                    random_direction()
                except KeyboardInterrupt:
                    print("Bot stopped")
                    break
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Bot stopped")


# Register F8 key press event to toggle running state
keyboard.on_press_key('f8', toggle_running)

if __name__ == "__main__":
    main()
