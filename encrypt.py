import base64
from tkinter import *
from tkinter import messagebox


def main_screen():
    global screen
    global code
    global text1

    def encrypt_text():
        password = code.get()

        if password == "1234":
            screen1 = Toplevel(screen)
            screen1.title("encryption")
            screen1.geometry("400x200")
            screen1.configure(bg="#ed3833")

            message = text1.get("1.0", END)
            encode_message = message.encode("utf-8")
            base64_byte = base64.b64encode(encode_message)
            encrypt_message = base64_byte.decode("utf-8")

            Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = Text(screen1, font="Roboto", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, encrypt_message)
        elif password == "":
            messagebox.showerror("Encryption", "Input Password")
        elif password != "1234":
            messagebox.showerror("Encryption", "Invalid Password")

    def decrypt_text():
        password = code.get()

        if password == "1234":
            screen2 = Toplevel(screen)
            screen2.title("decryption")
            screen2.geometry("400x200")
            screen2.configure(bg="#00bd56")

            message = text1.get("1.0", END)
            decode_message = message.encode("utf-8")
            base64_byte = base64.b64decode(decode_message)
            decrypt_message = base64_byte.decode("utf-8")

            Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
            text2 = Text(screen2, font="Roboto", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, decrypt_message)
        elif password == "":
            messagebox.showerror("Decryption", "Input Password")
        elif password != "1234":
            messagebox.showerror("Decryption", "Invalid Password")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    screen = Tk()
    screen.geometry("375x398")

    # icon
    image_icon = PhotoImage(file="gamindad.png")
    screen.iconphoto(False, image_icon)
    screen.title("MyPCTAPP")

    Label(text="Enter text for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=10)

    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial"), show="*").place(x=10, y=200)

    encrypt_button = Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt_text)
    encrypt_button.place(x=10, y=250)

    decrypt_button = Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt_text)
    decrypt_button.place(x=200, y=250)

    reset_button = Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset)
    reset_button.place(x=10, y=300)

    screen.mainloop()

main_screen()



