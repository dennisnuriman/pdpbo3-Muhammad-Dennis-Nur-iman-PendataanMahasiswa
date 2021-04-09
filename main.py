from tkinter import *

root = Tk()
root.title("TP3")

main1 = LabelFrame(root, padx=10, pady=10)
main1.grid(row = 0, column=0, padx=10, pady=10)

main11 = LabelFrame(root, padx=5, pady=5)
main11.grid(row = 1, column=0)

main12 = LabelFrame(root, padx=5, pady=5)
main12.grid(row = 2, column=0, padx=10, pady=10)

main2 = LabelFrame(root, padx=10, pady=10, relief="flat")
main2.grid(row = 0, column=1, padx=10, pady=10, sticky="ns")

main21 = LabelFrame(main2)
main21.grid(row = 2, column=0, pady=5)
main22 = LabelFrame(main2)
main22.grid(row = 3, column=0, pady=5)
main23 = LabelFrame(main2)
main23.grid(row = 4, column=0, pady=5)

i1 = Label(main1, text = "Nama Lengkap", width=15, anchor="w")
i1.grid(row=0, column=0)
t1 = Label(main1, text = ":", width=2, anchor="w")
t1.grid(row=0, column=1)
e1 = Entry(main1, width=35)
e1.grid(row=0, column=2)

i2 = Label(main1, text = "Email", width=15, anchor="w")
i2.grid(row=1, column=0)
t2 = Label(main1, text = ":", width=2, anchor="w")
t2.grid(row=1, column=1)
e2 = Entry(main1, width=35)
e2.grid(row=1, column=2)

i3 = Label(main1, text = "No HP", width=15, anchor="w")
i3.grid(row=2, column=0)
t3 = Label(main1, text = ":", width=2, anchor="w")
t3.grid(row=2, column=1)
e3 = Entry(main1, width=35)
e3.grid(row=2, column=2)

i4 = Label(main1, text = "Jurusan", width=15, anchor="w")
i4.grid(row=3, column=0)
t4 = Label(main1, text = ":", width=2, anchor="w")
t4.grid(row=3, column=1)

def click():
    print(clicked.get())

clicked = StringVar(root)
choices = {"Pendidikan Ilmu Komputer", "Ilmu Komputer"}
drop = OptionMenu(main1, clicked, *choices)
drop.grid(row=3, column=2, sticky="ew")
clicked.trace("w", click)

i5 = Label(main1, text = "Kelas", width=15, anchor="w")
i5.grid(row=4, column=0)
t5 = Label(main1, text = ":", width=2, anchor="w")
t5.grid(row=4, column=1)

clicked = StringVar(root)
choices = {"A", "B", "C1", "C2"}
drop = OptionMenu(main1, clicked, *choices)
drop.grid(row=4, column=2, sticky="ew")
clicked.trace("w", click)

i6 = Label(main1, text = "Kemampuan", width=15, anchor="w")
i6.grid(row=5, column=0)
t6 = Label(main1, text = ":", width=2, anchor="w")
t6.grid(row=5, column=1)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
box = LabelFrame(main1, relief="flat")
box.grid(row=5, column=2)
c1 = Checkbutton(box, text="SQL", variable=var1, onvalue=1, offvalue=0)
c1.grid(row=5, column=3)
c2 = Checkbutton(box, text="Design", variable=var2, onvalue=1, offvalue=0)
c2.grid(row=5, column=4)
c3 = Checkbutton(box, text="Coding", variable=var3, onvalue=1, offvalue=0)
c3.grid(row=5, column=5)
c4 = Checkbutton(box, text="Tidur", variable=var4, onvalue=1, offvalue=0)
c4.grid(row=5, column=6)

i7 = Label(main1, text = "Jenis Kelamin", width=15, anchor="w")
i7.grid(row=6, column=0)
t7 = Label(main1, text = ":", width=2, anchor="w")
t7.grid(row=6, column=1)

radiobtn = LabelFrame(main1, relief="flat")
radiobtn.grid(row=6, column=2)

r1 = Radiobutton(radiobtn, text="Pria", variable=var5, value=1)
r1.grid(row=6, column=3)
r2 = Radiobutton(radiobtn, text="Wanita", variable=var5, value=2)
r2.grid(row=6, column=4)

btn1 = Button(main11, text="Open Photo File", width=52)
btn1.grid(row=0, column=0, sticky="ew")

btn2 = Button(main12, text="SUMBIT", width=52)
btn2.grid(row=1, column=0, sticky="ew")

# ============================================================================================
def about():
    top = Toplevel()
    top.title("ABOUT")

    d_frame = LabelFrame(top, text="Biodata", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    opts_frame = LabelFrame(top, padx=10, pady=10)
    opts_frame.pack(padx=10, pady=10)

    b_exit = Button(opts_frame, text="Exit", command=top.destroy)
    b_exit.grid(row=5, column=0)

    d_summary = Label(d_frame, text="NIM: 1900141", anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="NAMA: Muhammad Dennis Nur'iman", anchor="w").grid(row=1, column=0, sticky="w")

def keluar():
    top = Toplevel()
    top.title("Keluar")

    d_frame = LabelFrame(top, padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    opts_frame = LabelFrame(top, text="Apakah anda yakin?", padx=10, pady=10)
    opts_frame.pack(padx=10, pady=10)

    b_exit = Button(opts_frame, text="Iya", command=root.destroy, width=10)
    b_exit.grid(row=5, column=0, sticky="ew")
    b_exit = Button(opts_frame, text="Tidak", command=top.destroy, width=10)
    b_exit.grid(row=5, column=1, sticky="ew")
# ============================================================================================

i7 = Label(main2, text = "Pendataan Mahasiswa DEPILKOM", font=("Arial", 15), width=30, relief="flat", anchor="w")
i7.grid(row=0, column=0)
i7 = Label(main2, text = "Agar mempermudah dalam mendata mahasiswa DEPILKOM\n\n\n\n\n\n", width=60)
i7.grid(row=1, column=0)

btn3 = Button(main21, text="LIHAT SEMUA MAHASISWA", width=52)
btn3.grid(row=2, column=0, sticky="ew")

btn4 = Button(main22, text="HAPUS DATA MAHASISWA", width=52)
btn4.grid(row=3, column=0, sticky="ew")

btn5 = Button(main23, text="ABOUT", width=52, command=about)
btn5.grid(row=4, column=0, sticky="ew")

btn6 = Button(root, text="EXIT", width=52, command=keluar)
btn6.grid(row=2, column=1)
root.mainloop()