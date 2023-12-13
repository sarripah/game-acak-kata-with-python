from tkinter import *
from random import *
from tkinter import messagebox
import time

VEGETABLE_WORD = ['OWLERT', 'IOOLKBR', 'OLK NAGBU', 'RONC', 'MITUN', 'EORTGN', 'AIKPPAR IJUAH', 'EAASLD',
                  'UAMJR', 'AAWBNG YBBMOA', 'KANGENT', 'UBLA', 'PPAARIK ERHAM', 'OMTTA', 'KONGNGSI', 'AANGCK OOLNGP', 'BALOK',
                  'OLK', 'AACBI', 'AANGWB UTPIH', 'IBU', 'ETUMBKAR', ]
VEGETABLE_ANSWER = ['WORTEL', 'BROKOLI ', 'KOL BUNGA ', 'JAGUNG ', 'TIMUN ', 'TERONG', 'PAPRIKA HIJAU ',
                    'SELADA ', 'JAMUR', 'BAWANG BOMBAY', 'KENTANG', 'LABU ', 'PAPRIKA MERAH', 'TOMAT ', 'SINGKONG', 'KACANG POLONG',
                    'LOBAK', 'KOL', 'CABAI', 'BAWANG PUTIH', 'UBI', 'KETUMBAR', ]

ran_num = randrange(0, (len(VEGETABLE_WORD)))
jumbled_rand_word = VEGETABLE_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        from levels import pilih_menu
        pilih_menu.menu()

    def change():
        global ran_num
        ran_num = randrange(0, (len(VEGETABLE_WORD)))
        word.configure(text=VEGETABLE_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def cheak():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == VEGETABLE_ANSWER[ran_num]:
            points += 5
            score.configure(text="Poin: " + str(points))
            messagebox.showinfo('Benar', "Jawaban Benar.. Pertahankan!")
            ran_num = randrange(0, (len(VEGETABLE_WORD)))
            word.configure(text=VEGETABLE_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Jawaban Salah..Coba lagi!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Poin: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=VEGETABLE_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Poin tidak cukup', font="Winkle")

    my_window = Tk()

    my_window.geometry("600x600")
    my_window.configure(bg = "#e2dad7")
    my_window.title("Acak Kata")
    canvas = Canvas(
        my_window,
        bg = "#e2dad7",
        height = 600,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"F:/Coding smester2/Game Acak Kata/Game Acak Kata/gameplay/background.png")
    background = canvas.create_image(
        286.5, 400.0,
        image=background_img)

    fotokeluar = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\main\keluar.png")
    b1_keluar = Button(
        image = fotokeluar,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        relief = "flat",
        command = my_window.destroy)
    b1_keluar.pack(anchor='nw', pady=15, padx=10)

    score = Label(
        text="Poin:- 0",
        pady=10,
        bg="#ffffff",
        fg="#000000",
        font="Arial  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#ffffff",
        fg="#000000",
        font="Winkle  50 bold"
    )
    word.pack()

    get_input = Entry(
        font="Winkle 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack(pady=(15, 20))

    cek = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\gameplay\cekjawab.png")
    submit = Button(
        image = cek,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        relief = "flat",
        command=cheak
    )
    submit.pack(pady=(15, 20))

    change_img = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\gameplay\gantikata.png")
    change_btn = Button(
        image = change_img,
        borderwidth = 0,
        cursor="hand2",
        highlightthickness = 0,
        relief = "flat",
        command=change,
    )
    change_btn.pack()

    answer = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\gameplay\jawaban.png")
    ans = Button(
        image = answer,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        relief = "flat",
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="#ffffff",
        fg="#000000",
        font="Winkle 15 bold",
    )
    ans_lab.pack()

    kembali = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\gameplay\kembali.png")
    lab_img1 = Button(
        my_window,
        image = kembali,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat",
        cursor="hand2",
        justify='center',
        command=back
    )
    lab_img1.pack(pady=20, padx=10)

    my_window.mainloop()
