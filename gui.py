from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Tugas\KI\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def rc4_encrypt_decrypt(input_string, key):
    S = list(range(256))
    j = 0
    out = []

    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)]))     % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for char in input_string:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(chr(ord(char) ^ K))

    return ''.join(out)

window = Tk()

window.geometry("844x390")
window.configure(bg = "#717373")

canvas = Canvas(
    window,
    bg = "#717373",
    height = 390,
    width = 844,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    421.5,
    263.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=87.5,
    y=223.0,
    width=668.0,
    height=78.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    421.5,
    142.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=87.5,
    y=102.0,
    width=668.0,
    height=78.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    36.0,
    38.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: entry_2.replace("1.0", "end", rc4_encrypt_decrypt(entry_1.get("1.0", "end-1c"), 'kunci_rahasia')),
    relief="flat"
)
button_1.place(
    x=55.0,
    y=328.0,
    width=114.0,
    height=48.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    421.0,
    205.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    422.0,
    84.0,
    image=image_image_3
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: entry_2.replace("1.0", "end", rc4_encrypt_decrypt(entry_2.get("1.0", "end-1c"), 'kunci_rahasia')),
    relief="flat"
)
button_2.place(
    x=674.0,
    y=328.0,
    width=114.0,
    height=48.0
)
window.resizable(False, False)
window.mainloop()
