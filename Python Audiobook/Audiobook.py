import pyttsx3
import PyPDF2

book = open('Investor.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Total number of pages in the respective audiobook are: ", pages)

#Creating pyttsx3 object
speaker = pyttsx3.init()
speaker.say("Welcome to the book The Intelligent Investor")
for num in range(14, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()

    #changing he default rate
    rate = speaker.getProperty("rate")
    speaker.setProperty("rate", 130)

    #changing the default volume
    #volume = speaker.getProperty("volume")
    #speaker.setProperty("volume", 1)

    #changing the default value
    voices = speaker.getProperty("voices")
    #male voice has index 0 while female voice has index 1
    speaker.setProperty("voice", voices[1].id)

    speaker.say(text)
    speaker.runAndWait()