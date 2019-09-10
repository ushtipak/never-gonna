from subprocess import call
from tkinter import Tk, Label

from PIL import ImageTk, Image

HONEYPOT = {
    "title": "disposition [~/cpeople/workspace-go/disposition] - .../cmd/disposition/main.go - GoLand",
    "background": "desktop.png",
    "geometry": "2560x1407"
}
PACKED = {
    "side": "bottom",
    "fill": "both",
    "expand": "yes"
}
XFLOCK = "/usr/bin/xflock4"


def lock(_):
    call(XFLOCK)
    exit(0)


if __name__ == "__main__":
    root = Tk()
    root.geometry(HONEYPOT['geometry'])
    root.title(HONEYPOT['title'])
    root.bind('<Motion>', lock)
    root.bind("<Key>", lock)

    background = ImageTk.PhotoImage(Image.open(HONEYPOT['background']))
    panel = Label(root, image=background)
    panel.pack(**PACKED)

    root.mainloop()
