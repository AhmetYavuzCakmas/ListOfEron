import os
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def show_menu():
    """Ana menüyü göster"""
    # Tüm widget'ları temizle
    for widget in window.winfo_children():
        widget.destroy()
    
    # Menü başlığı
    title_label = Label(window, text="ListOfEron", font=("Arial", 24, "bold"))
    title_label.pack(pady=50)
    
    # Butonlar
    add_button = Button(window, text="Kişi Kaydet", font=("Arial", 14), 
                       width=20, height=2, command=show_add_form)
    add_button.pack(pady=10)
    
    search_button = Button(window, text="Sorgula", font=("Arial", 14), 
                          width=20, height=2, command=show_search)
    search_button.pack(pady=10)
    
    exit_button = Button(window, text="Çıkış", font=("Arial", 14), 
                        width=20, height=2, command=window.quit)
    exit_button.pack(pady=10)

def show_add_form():
    """Kişi ekleme formunu göster"""
    # Tüm widget'ları temizle
    for widget in window.winfo_children():
        widget.destroy()
    
    # Canvas ve Logo
    canvas = Canvas(height=200, width=200)
    
    # PyInstaller için logo yolu
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    logo_path = os.path.join(application_path, "logo.png")
    
    try:
        logo_img = PhotoImage(file=logo_path)
        canvas.logo_img = logo_img  # Referansı sakla
        canvas.create_image(100, 100, image=logo_img)
    except:
        canvas.create_text(100, 100, text="ListOfEron", font=("Arial", 16, "bold"))
    
    canvas.grid(row=0, column=1, pady=10)
    
    # Labels
    name_label = Label(window, text="Name:")
    name_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)
    
    numara_label = Label(window, text="Numara:")
    numara_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)
    
    job_label = Label(window, text="Adres (okul adı/iş yeri adı):")
    job_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)
    
    alan_label = Label(window, text="Alan:")
    alan_label.grid(row=4, column=0, sticky=W, padx=10, pady=5)
    
    city_label = Label(window, text="Şehir:")
    city_label.grid(row=5, column=0, sticky=W, padx=10, pady=5)
    
    commant_label = Label(window, text="Açıklama:")
    commant_label.grid(row=6, column=0, sticky=W, padx=10, pady=5)
    
    # Entry'ler - global değişkenler olarak tanımla
    global name_entry, numara_entry, job_entry, alan_entry, city_entry, commant_entry
    
    name_entry = Entry(window, width=35)
    name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
    name_entry.focus()
    name_entry.bind("<Return>", lambda e: numara_entry.focus())
    
    numara_entry = Entry(window, width=35)
    numara_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
    numara_entry.insert(0, "+90 555 555 55 55")
    numara_entry.bind("<Return>", lambda e: job_entry.focus())
    
    job_entry = Entry(window, width=35)
    job_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=5)
    job_entry.insert(0, "Meslek")
    job_entry.bind("<Return>", lambda e: alan_entry.focus())
    
    alan_entry = Entry(window, width=35)
    alan_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
    alan_entry.insert(0, "Alan")
    alan_entry.bind("<Return>", lambda e: city_entry.focus())
    
    city_entry = Entry(window, width=35)
    city_entry.grid(row=5, column=1, padx=10, pady=5)
    city_entry.insert(0, "Şehir")
    city_entry.bind("<Return>", lambda e: commant_entry.focus())
    
    commant_entry = Entry(window, width=35)
    commant_entry.grid(row=6, column=1, padx=10, pady=5)
    commant_entry.insert(0, "Nerede tanıştım")
    commant_entry.bind("<Return>", lambda e: save())
    
    # Butonlar
    button_frame = Frame(window)
    button_frame.grid(row=7, column=0, columnspan=3, pady=20)
    
    save_button = Button(button_frame, text="Kaydet", width=15, 
                        font=("Arial", 10), command=save)
    save_button.pack(side=LEFT, padx=5)
    
    back_button = Button(button_frame, text="Ana Menü", width=15, 
                        font=("Arial", 10), command=show_menu)
    back_button.pack(side=LEFT, padx=5)

def save():
    """Kişi bilgilerini kaydet"""
    gruop_name = "ListOfEron"
    name = name_entry.get()
    numara = numara_entry.get()
    job = job_entry.get()
    city = city_entry.get()
    alan = alan_entry.get()
    commant = commant_entry.get()
    
    if len(name) == 0 or len(numara) < 10 or len(city) == 0 or len(alan) == 0 or len(job) == 0:
        messagebox.showinfo(title="Dikkat Et Kral, Uyanık Ol!", 
                           message="Eksik bir şeyler var onları doldur Reis!")
    else:
        is_ok = messagebox.askokcancel(title=gruop_name, 
                                      message=f"İsim: {name}\nNumara: {numara}\n\nBilgiler kaydedilsin mi?")
        
        if is_ok:
            with open("data.txt", "a", encoding="utf-8") as data_file:
                data_file.write(f"{name} | {numara} | {job} | {city} | {alan} | {commant}\n")
            
            # Entry'leri temizle
            name_entry.delete(0, END)
            numara_entry.delete(0, END)
            city_entry.delete(0, END)
            alan_entry.delete(0, END)
            job_entry.delete(0, END)
            commant_entry.delete(0, END)
            
            # İlk alana geri dön
            name_entry.focus()

def show_search():
    """Kayıtlı kişileri sorgula"""
    # Tüm widget'ları temizle
    for widget in window.winfo_children():
        widget.destroy()
    
    # Başlık
    title_label = Label(window, text="Kayıtlı Kişiler", font=("Arial", 18, "bold"))
    title_label.pack(pady=20)
    
    # Arama kutusu ve buton
    search_frame = Frame(window)
    search_frame.pack(pady=10)
    
    Label(search_frame, text="Anahtar Kelime:", font=("Arial", 10)).pack(side=LEFT, padx=5)
    search_entry = Entry(search_frame, width=30, font=("Arial", 11))
    search_entry.pack(side=LEFT, padx=5)
    
    def search_data():
        """Arama yap"""
        filter_text = search_entry.get().strip()
        load_data(filter_text)
    
    search_button = Button(search_frame, text="Ara", width=10, 
                          font=("Arial", 10, "bold"), command=search_data)
    search_button.pack(side=LEFT, padx=5)
    
    # Enter tuşuyla da arama yap
    search_entry.bind("<Return>", lambda e: search_data())
    
    clear_button = Button(search_frame, text="Temizle", width=10, 
                         font=("Arial", 10), command=lambda: [search_entry.delete(0, END), load_data()])
    clear_button.pack(side=LEFT, padx=5)
    
    # Sonuç sayısı göstergesi
    result_label = Label(window, text="", font=("Arial", 10, "italic"), fg="blue")
    result_label.pack(pady=5)
    
    # Listbox ve Scrollbar
    frame = Frame(window)
    frame.pack(pady=10, padx=20, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox = Listbox(frame, width=90, height=15, yscrollcommand=scrollbar.set, 
                     font=("Courier", 9))
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    def load_data(filter_text=""):
        """Verileri yükle ve filtrele"""
        listbox.delete(0, END)
        
        if not os.path.exists("data.txt"):
            listbox.insert(END, "Henüz kayıt yok!")
            result_label.config(text="0 kayıt bulundu")
            return
        
        with open("data.txt", "r", encoding="utf-8") as data_file:
            lines = data_file.readlines()
            
            if not lines:
                listbox.insert(END, "Henüz kayıt yok!")
                result_label.config(text="0 kayıt bulundu")
                return
            
            # Başlık ekle
            listbox.insert(END, "=" * 110)
            header = f"{'İsim':<20} | {'Numara':<18} | {'İş/Okul':<15} | {'Şehir':<12} | {'Alan':<12} | {'Açıklama':<15}"
            listbox.insert(END, header)
            listbox.insert(END, "=" * 110)
            
            count = 0
            matched_lines = []
            
            # Filtreleme yap
            for line in lines:
                if filter_text == "" or filter_text.lower() in line.lower():
                    matched_lines.append(line)
                    count += 1
            
            # Sonuçları göster
            if count == 0:
                listbox.insert(END, "")
                listbox.insert(END, f"'{filter_text}' için sonuç bulunamadı!")
                listbox.insert(END, "")
                result_label.config(text="0 kayıt bulundu", fg="red")
            else:
                for line in matched_lines:
                    parts = line.strip().split(" | ")
                    if len(parts) >= 6:
                        name = parts[0][:19]
                        numara = parts[1][:17]
                        job = parts[2][:14]
                        city = parts[3][:11]
                        alan = parts[4][:11]
                        commant = parts[5][:14]
                        
                        display = f"{name:<20} | {numara:<18} | {job:<15} | {city:<12} | {alan:<12} | {commant:<15}"
                        listbox.insert(END, display)
                
                listbox.insert(END, "=" * 110)
                
                # Sonuç mesajı
                if filter_text:
                    result_label.config(text=f"'{filter_text}' için {count} kayıt bulundu", fg="green")
                else:
                    result_label.config(text=f"Toplam {count} kayıt gösteriliyor", fg="blue")
    
    # İlk yüklemede tüm verileri göster
    load_data()
    search_entry.focus()  # Arama kutusuna odaklan
    
    # Alt butonlar
    button_frame = Frame(window)
    button_frame.pack(pady=20)
    
    back_button = Button(button_frame, text="Ana Menü", width=15, 
                        font=("Arial", 11), command=show_menu)
    back_button.pack(side=LEFT, padx=10)
    
    refresh_button = Button(button_frame, text="Yenile", width=15, 
                           font=("Arial", 11), command=lambda: load_data())
    refresh_button.pack(side=LEFT, padx=10)
    
# Ana pencere
window = Tk()
window.title("ListOfEron")
window.geometry("700x600")
window.config(padx=20, pady=20)

# İlk olarak ana menüyü göster
show_menu()

window.mainloop()
