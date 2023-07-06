from PyPDF2 import PdfReader
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    newVoiceRate = 135
    engine.setProperty('rate', newVoiceRate)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    book = PdfReader("Four-Steps-to-Forgiveness-William-Fergus-Martin.pdf")
    pages = len(book.pages)
    # for i in range(3, pages):
    for i in range(3, pages):
        pg = book.pages[i]
        text = pg.extract_text()
        print(text)
        speak(text)
        time.sleep(3)
