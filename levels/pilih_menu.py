from tkinter import *

def menu():

    def start_game(args):
        window.destroy()
        if args == 1:
            from Options import Animals
            Animals.main()
        elif args == 2:
            from Options import Body_parts
            Body_parts.main()
        elif args == 3:
            from Options import Colour
            Colour.main()
        elif args == 4:
            from Options import Fruit
            Fruit.main()
        elif args == 5:
            from Options import Shapes
            Shapes.main()
        elif args == 6:
            from Options import Vegetable
            Vegetable.main()
        elif args == 7:
            from Options import Vehicles
            Vehicles.main()

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

    background_img = PhotoImage(file = f"F:/Coding smester2/Game Acak Kata/Game Acak Kata/levels/background.png")
    background = canvas.create_image(
        286.5, 400.0,
        image=background_img)

    hewan = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img0.png")
    b0_hewan = Button(
        image = hewan,
        borderwidth = 0,
        cursor="hand2",
        highlightthickness = 0,
        command = lambda: start_game(1),
        relief = "flat")

    b0_hewan.place(
        x = 225, y = 111,
        width = 150,
        height = 40)

    tubuh = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img1.png")
    b1_tubuh = Button(
        image = tubuh,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = lambda: start_game(2),
        relief = "flat")

    b1_tubuh.place(
        x = 225, y = 173,
        width = 150,
        height = 40)

    warna = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img2.png")
    b2_warna = Button(
        image = warna,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = lambda: start_game(3),
        relief = "flat")

    b2_warna.place(
        x = 225, y = 235,
        width = 150,
        height = 40)

    buah = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img3.png")
    b3_buah = Button(
        image = buah,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = lambda: start_game(4),
        relief = "flat")

    b3_buah.place(
        x = 225, y = 297,
        width = 150,
        height = 40)

    bangunDatar = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img4.png")
    b4_bangunDatar = Button(
        image = bangunDatar,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = lambda: start_game(5),
        relief = "flat")

    b4_bangunDatar.place(
        x = 225, y = 359,
        width = 150,
        height = 40)

    sayur = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img5.png")
    b5_sayur = Button(
        image = sayur,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = lambda: start_game(6),
        relief = "flat")

    b5_sayur.place(
        x = 225, y = 421,
        width = 150,
        height = 40)

    kendaraan = PhotoImage(file = f"F:\Coding smester2\Game Acak Kata\Game Acak Kata\levels\img6.png")
    b6_kendaraan = Button(
        image = kendaraan,
        borderwidth = 0,
        highlightthickness = 0,
        cursor="hand2",
        command = lambda: start_game(7),
        relief = "flat")

    b6_kendaraan.place(
        x = 225, y = 483,
        width = 150,
        height = 40)

    canvas.create_text(
        89.5, 62.5,
        text = "Pilih Tipe",
        fill = "#000000",
        font = ("Winkle-Regular", int(24.0)))

    window.resizable(False, False)
    window.mainloop()

menu()