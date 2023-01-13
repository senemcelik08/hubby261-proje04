import tkinter as tk
from tkinter import Label
from tkinter import Button
from tkinter import Text
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import feedparser

url= ('https://www.cnnturk.com/feed/rss/news')

haberler=feedparser.parse(url)

i=0
for x in haberler.entries:
    if i < 10:
        i += 1
        print("..................")
        print(i, ".haber")
        print(x.title)
        print(x.link)
        print(x.description)
        print("")
    else:
        break

root = tk.Tk()
root.title("Bugünkü haberlerden haberdar olmak için kelime bulutu oluştur")
root.configure(bg = "Turquoise")

label = Label(root, text = "Lütfen bekleyin...", font = ("Arial", 12), bg = "Turquoise")
label.pack()

def create_wordcloud():
    i = 0
    text = ""
    for x in haberler.entries:
        if i < 10:
            i += 1
            text += x.title + " " + x.description
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    label.config(text = "Kelime Bulutu Oluşturuldu!")

create_button = Button(root, text = "Kelime Bulutu Oluştur", command = create_wordcloud, bg = "Turquoise")
create_button.pack()
root.mainloop()




