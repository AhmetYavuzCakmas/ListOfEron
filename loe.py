import os
import sys
from tkinter import *
from tkinter import messagebox

def save():
    gruop_name = "ListOfEron"
    name = name_entry.get()
    numara = numara_entry.get()
    job = job_entry.get()
    city = city_entry.get()
    alan = alan_entry.get()
    commant = commant_entry.get()

    if len(name) == 0 or len(numara) < 10 or len(city) == 0 or len(alan) == 0 or len(job) == 0:
        messagebox.showinfo(title="Dikkat Et Kral, Uyanık Ol!", message="Eksik bir şeyler var onları doldur Reis!")
    else: 
        is_ok = messagebox.askokcancel(title=gruop_name, message=f"İsim: {name} "
                                                        f"\nNumara: {numara} \nBilgiler kaydedilsin mi?")
        
        if is_ok:
            with open("data.txt","a", encoding="utf-8") as data_file:
                data_file.write(f"{name} | {numara} | {job} | {city} | {alan} | {commant}\n")
                
                name_entry.delete(0, END)
                numara_entry.delete(0, END)
                city_entry.delete(0, END)
                alan_entry.delete(0, END)
                job_entry.delete(0, END)
                commant_entry.delete(0, END)
                
                # İlk alana geri dön
                name_entry.focus()

# Enter tuşuna basınca sonraki alana geçmek için fonksiyonlar
def focus_numara(event):
    numara_entry.focus()

def focus_job(event):
    job_entry.focus()

def focus_alan(event):
    alan_entry.focus()

def focus_city(event):
    city_entry.focus()

def focus_commant(event):
    commant_entry.focus()

def save_on_enter(event):
    save()

window = Tk()
window.title("ListOfEron")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

# PyInstaller için logo yolu
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

logo_path = os.path.join(application_path, "logo.png")

try:
    logo_img = PhotoImage(file=logo_path)
    canvas.create_image(100, 100, image=logo_img)
except:
    canvas.create_text(100, 100, text="ListOfEron", font=("Arial", 16, "bold"))

canvas.grid(row=0, column=1)



name_label = Label(text="Name:")
name_label.grid(row=1, column=0)
numara_label = Label(text="Numara:")
numara_label.grid(row=2, column=0)
job_label = Label(text="Adres (okul adı/iş yeri adı):")
job_label.grid(row=3, column=0)
alan_label = Label(text="Alan:")
alan_label.grid(row=4, column=0)
city_label = Label(text="Şehir:")
city_label.grid(row=5, column=0)
commant_label = Label(text="Açıklama:")
commant_label.grid(row=6, column=0)

name_entry = Entry(width=35)
name_entry.grid(row=1, column=1, columnspan=2)
name_entry.focus()
name_entry.bind("<Return>", focus_numara)  # Enter tuşu ile numara'ya geç

numara_entry = Entry(width=35)
numara_entry.grid(row=2, column=1, columnspan=2)
numara_entry.insert(0, "Numara")
numara_entry.bind("<Return>", focus_job)  # Enter tuşu ile job'a geç

job_entry = Entry(width=35)
job_entry.grid(row=3, column=1, columnspan=2)
job_entry.insert(0, "Meslek")
job_entry.bind("<Return>", focus_alan)  # Enter tuşu ile alan'a geç

alan_entry = Entry(width=35)
alan_entry.grid(row=4, column=1, columnspan=2)
alan_entry.insert(0, "Alan")
alan_entry.bind("<Return>", focus_city)  # Enter tuşu ile city'ye geç

city_entry = Entry(width=35)
city_entry.grid(row=5, column=1)
city_entry.insert(0, "Şehir")
city_entry.bind("<Return>", focus_commant)  # Enter tuşu ile commant'a geç

commant_entry = Entry(width=35)
commant_entry.grid(row=6, column=1)
commant_entry.insert(0, "Nerede tanıştım")
commant_entry.bind("<Return>", save_on_enter)  # Son alanda Enter'a basınca kaydet

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=7, column=1)

window.mainloop()