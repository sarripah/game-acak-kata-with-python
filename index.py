from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import ImageTk, Image

def start_main_page():

    window = Tk()

    window.geometry("600x600")
    window.configure(bg = "#e2dad7")
    window.title("Acak Kata")
    canvas = Canvas(
        window,
        bg = "#e2dad7",
        height = 600,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    def show_option():
        window.destroy()
        from levels import pilih_menu

    def message():
        tkinter.messagebox.showinfo('About','Kelompok 8 :\n2110511045_Nayla Zayyannafisah Abida\n2110511052_Azriel Dwi Mahendra\n2110511060_Saripah\n')

    background_img = PhotoImage(file = f"F:/Coding smester2/Game Acak Kata/Game Acak Kata/main/background.png")
    background = canvas.create_image(
        286.5, 400.0,
        image=background_img)

    canvas.create_text(
        305.0, 108.0,
        text = "ACAK KATA",
        fill = "#fffadd",
        font = ("Winkle-Regular", int(48.0)))

    info = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\main\info.png")
    b0_info = Button(
        image = info,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = message,
        relief = "flat")

    b0_info.place(
        x = 214, y = 338,
        width = 160,
        height = 48)

    keluar = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\main\keluar.png")
    b1_keluar = Button(
        image = keluar,
        borderwidth = 0,
        highlightthickness = 0,
        command = window.destroy,
        cursor="hand2",
        relief = "flat")

    b1_keluar.place(
        x = 214, y = 421,
        width = 160,
        height = 48)

    mulai = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\main\mulai.png")
    b2_mulai = Button(
        image = mulai,
        borderwidth = 0,
        highlightthickness = 0,
        command = show_option,
        cursor="hand2",
        relief = "flat")

    b2_mulai.place(
        x = 212, y = 253,
        width = 160,
        height = 48)

    window.resizable(False, False)
    window.mainloop()

start_main_page()