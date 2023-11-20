import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import nltk
from newspaper import Article
from ttkbootstrap import Style

nltk.download('punkt')

class ArticleSummarizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Article Summarizer")

        style = Style('flatly')  # You can choose a different theme from ttkbootstrap

        self.url_label = ttk.Label(master, text="Enter Article URL:")
        self.url_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.url_entry = ttk.Entry(master, width=40)
        self.url_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        self.summarize_button = ttk.Button(master, text="Summarize", command=self.summarize)
        self.summarize_button.grid(row=0, column=2, pady=10, padx=10)

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=15)
        self.output_text.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

    def summarize(self):
        url = self.url_entry.get()

        if not url:
            self.show_message("Please enter a valid URL.")
            return

        try:
            article = Article(url)
            article.download()
            article.parse()
            article.nlp()

            summary = article.summary

            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f'Title: {article.title}\n\n')
            self.output_text.insert(tk.END, f'Authors: {", ".join(article.authors)}\n\n')
            self.output_text.insert(tk.END, f'Publication Date: {article.publish_date}\n\n')
            self.output_text.insert(tk.END, f'Summary: {summary}')

        except Exception as e:
            self.show_message(f"Error: {e}")

    def show_message(self, message):
        messagebox.showinfo("Message", message)

def main():
    root = tk.Tk()
    style = Style('vapor')  # You can choose a different theme from ttkbootstrap
    app = ArticleSummarizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
