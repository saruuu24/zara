import tkinter as tk
from tkinter import ttk, filedialog
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer
from docx import Document
import PyPDF2
from ttkbootstrap import Style

class SummarizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Document Summarizer")

        style = Style('vapor')  # You can choose a different theme from ttkbootstrap

        self.text_area = tk.Text(master, wrap="word", height=25, width=150)
        self.text_area.pack(pady=10)

        self.summarize_button = ttk.Button(master, text="Summarize", command=self.summarize)
        self.summarize_button.pack(pady=5)

        self.clear_button = ttk.Button(master, text="Clear", command=self.clear_text)
        self.clear_button.pack(pady=5)

    def summarize(self):
        input_text = self.text_area.get("1.0", "end-1c")

        if not input_text:
            self.show_error("Please provide input text.")
            return

        # Tokenize sentences
        sentences = sent_tokenize(input_text)

        # Tokenize words, remove stopwords and punctuation
        words = [word.lower() for word in word_tokenize(input_text) if word.isalnum() and word.lower() not in stopwords.words("english")]

        # Calculate word frequencies
        freq_dist = FreqDist(words)

        # Get the 5 most frequent words
        top_words = freq_dist.most_common(5)

        # Create a summary by selecting sentences containing the most frequent words
        summary_sentences = [sentence for sentence in sentences if any(word in sentence.lower() for word, _ in top_words)]

        # Detokenize the summary sentences
        summary = TreebankWordDetokenizer().detokenize(summary_sentences)

        # Display the summary
        self.show_summary(summary)

    def clear_text(self):
        self.text_area.delete("1.0", "end")

    def show_summary(self, summary):
        summary_window = tk.Toplevel(self.master)
        summary_window.title("Summary")

        summary_text = tk.Text(summary_window, wrap="word", height=30, width=150)
        summary_text.insert("1.0", summary)
        summary_text.pack(pady=10)

    def show_error(self, message):
        error_window = tk.Toplevel(self.master)
        error_window.title("Error")

        error_label = ttk.Label(error_window, text=message)
        error_label.pack(pady=10)

# Function to load text from a PDF file
def read_pdf(file_path):
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        return text

# Function to load text from a Word document
def read_word(file_path):
    doc = Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

def main():
    root = tk.Tk()
    app = SummarizerApp(root)

    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Word files", "*.docx")])

    if file_path.endswith(".pdf"):
        text = read_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = read_word(file_path)
    else:
        app.show_error("Unsupported file format. Please provide a PDF or Word document.")
        return

    app.text_area.insert("1.0", text)

    root.mainloop()

if __name__ == "__main__":
    main()
