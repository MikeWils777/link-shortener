from tkinter import *
import pyperclip
import pyshorteners

def url_shortner():
    shortener = pyshorteners.Shortener()
    url_short = shortener.tinyurl.short(main_url.get())

    #set the global short_url
    short_url.set(url_short)

def copy_url():
    #copy short url on clipboard
    pyperclip.copy( short_url.get())

if __name__=="__main__":
    root = Tk()
    root.geometry("700x500")
    root.title("URL Shortener App")
    root.configure(bg="#116562")

    main_url = StringVar()
    short_url= StringVar()

    Label(root, text="Enter The Main URL", font="Times").pack(pady=5)
    Entry(root,textvariable=main_url, width =100).pack(pady=5)
    Button(root, bg="blue", text="Generate Short URL", command =url_shortner).pack(pady=5)

    Label(root, text="The Short URL ", font="Times").pack(pady=5)
    Entry(root, textvariable= short_url, width=50).pack(pady=4)
    Button(root, bg="blue", text="Copy the Short URL", command= copy_url).pack(pady=5)
    root.mainloop()