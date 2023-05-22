import time
from plyer import notification
# from PIL import Image

## This function converted the coffee-break.png to logo.ico
# def getFile():
#     logo = Image.open("coffee-break.png")
#     logo.save("logo.ico", format='ICO')

def display_notification(breakTime):
    notification.notify(
        title="Take-A-Break",
        message=f"You have been workin for 45 minutes on this computer. Kindly take a brake of {breakTime} minutes."
                f"This notification will timeout once the break time is over.",
        app_name="PyReminder",
        timeout=breakTime*60,
        app_icon="logo.ico"
    )

if __name__ == '__main__':
    breakTime = int(input("Enter the number of second you want to take the break of:\n"))
    while True:
        display_notification(breakTime)
        time.sleep(45*60)
    # getFile()
