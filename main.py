import pyttsx3
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Initialize the Tkinter window
Tk().withdraw()  # Prevent the Tkinter window from showing

# Open file dialog to select PDF file
book = askopenfilename(filetypes=[("PDF files", "*.pdf")])

# Open the PDF file in binary mode
with open(book, 'rb') as file:
    pdfreader = PyPDF2.PdfReader(file)  # Use PdfReader for modern PyPDF2
    pages = len(pdfreader.pages)  # Total number of pages in the PDF

    # Initialize pyttsx3 for text-to-speech
    player = pyttsx3.init()

    # Iterate through each page and read aloud the text
    for num in range(pages):
        page = pdfreader.pages[num]  # Access the page
        text = page.extract_text()  # Extract the text from the page
        
        # Check if there's any text before speaking
        if text:
            player.say(text)

    # Run the speech
    player.runAndWait()
