import tkinter
from tkinter import *

mainWindow = tkinter.Tk()
mainWindow.geometry('640x480')
mainWindow.title("Encryption by cipher method ")
mainWindow.config(bg="silver")

text = StringVar()
# shift_value = StringVar()


# class Encryption:


    # def __init__(self, Text, Shift):
    #     self.Text = Text
    #     self.Shift = Shift

# def encrypt():
#     Text = text.get()
#     Shift = int(shift_value.get())
#
#     encrypted_text = ''
#     for char in Text:
#         if not char.isnumeric():
#             ascii_offset = ord('A') if char.isupper() else ord('a')
#             encrypt_char = chr((ord(char) - ascii_offset + Shift) % 26 + ascii_offset)
#             encrypted_text += encrypt_char
#             txt.insert(0.0, encrypted_text)
#         else:
#             encrypted_text += char
#             txt.insert(0.0, encrypted_text)
#     print(encrypted_text)
#     return encrypted_text
#

def encrypted():
    txt.delete(0.0, END)
    Text = text.get()
    Shift = int(shift_value.get())
    result = ""

    # traverse text
    for i in range(len(Text)):
        char = Text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + Shift-65) % 26 + 65)
            # txt.insert(0.0, result)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + Shift - 97) % 26 + 97)
            # txt.insert(0.0, result)
    # print(result)
    # print(Shift)
    txt.insert(0.0, result)
    # return result

    # @staticmethod
# def encrypted():
#     input_value = Text
#     shift = int(shift_value.get())
#     encrypted = Encryption(input_value, shift)
#
#
# # @staticmethod
# def decrypted(self):
#     input_value = self.Text.get()
#     shift = int(shift_value.get())
#     decrypted = Encryption(input_value, -shift)


# obj = Encryption(text, shift)
# Title
label_0 = Label(mainWindow, text="Encryption", width=25, font=("Times New Roman""bold", 30), background="silver")
label_0.grid(row=3, column=5, padx=300, pady=15)

# Text Entry Label
label_2 = Label(mainWindow, text="Write a word for Encryption", width=10,
                font=("Times New Roman""bold", 14), background="silver")
label_2.grid(row=7, column=5, ipadx=200, ipady=50)

# Text Box
entry_1 = Entry(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
entry_1.grid(row=8, column=5)
# shift
shift_value = tkinter.StringVar(mainWindow)
shift_value.set("3")
shift_option = tkinter.OptionMenu(mainWindow, shift_value, "1", "2", "3", "4", "5", '6', '7', '8', '9', '10')
shift_option.grid(column=5)
# Encryption  button
b1 = Button(mainWindow, text='Encrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown', command=encrypted)
b1.grid(row=10, column=5, padx=305, pady=15)

# encrypted_output = Label(mainWindow, font=("ariel", 24), fg="black", bg="white", textvariable=text)
# encrypted_output.grid(row=12, column=5)

# Decryption button
# b2 = Button(mainWindow, text='Decrypt', font=("Times New Roman""bold", 10), width=12, height=2, bg='silver', fg='brown')
# b2.grid(row=11, column=5, padx=305, pady=15)

# output
# output_value = tkinter.StringVar(mainWindow)
# output_label = Label(mainWindow, font=("ariel", 24),width=10, fg="black", bg="white", textvariable=output_value,)
# output_label.grid(row=13, column=5)

txt = Text(mainWindow , width = 37 , height = 12 , wrap = WORD)
txt.grid( row = 11 , column = 5)
mainWindow.mainloop()

##################################################################################################### GITHUB code 1 ##################################################
#
# from tkinter import *
# import tkinter.messagebox as tmsg
# root = Tk()
# #"window width x window height + position right + position down"
# root.geometry("600x400+200+200")
# root.configure(background="#3C3F41")
# root.wm_iconbitmap("lock.ico")
# root.title("Caesar Cipher v.1.1")
# text_value = StringVar()
# key_value = IntVar()
#
# def encrypt():
#
#     string = text_value.get()
#     string = string.upper()
#     ptext = string
#
#     k = key_value.get()
#
#     if k > 26 or k == 0:
#         warning="Key Should be Less than or Equals to 26! Try to enter Key value from 1 - 26"
#         tmsg.showwarning("Invalid key Enter", warning)
#     else:
#         with open("encrypt.txt", "a") as f:
#             f.write("\nPlain Text: " + str(ptext) + " Key: " + str(k) + " Encrypted Text: " )
#         for i in string:
#             #print(i, end = " -> ")
#             p = ord(i) - 65
#
#             c = (p + k) % 26
#             c = c + 65
#             final = chr(c)
#             print(final)
#             with open("encrypt.txt", "a") as f:
#                 f.write(final)
#
#         k = str(k)
#
#         with open("encrypt.txt", "r") as f:
#             show = f.read()
#         Label(root,text="Encryption", font="Times 14 bold",fg="#FFFFFF", bg="#3C3F41").grid(row=4,column=1)
#         Label(root, text=show, fg="#E8EAED", bg="#3C3F41", font="Times 12 italic").grid(row=5, column=1)
#
# def decrypt():
#
#     string = text_value.get()
#     string = string.upper()
#     ptext = string
#
#     k = key_value.get()
#
#     if k > 26 or k == 0:
#         warning="Key Should be Less than or Equals to 26! Try to enter Key value from 1 - 26"
#         tmsg.showwarning("Invalid key Enter", warning)
#     else:
#         with open("decrypted.txt", "a") as f:
#             f.write("\nEncrypted Text: " + str(ptext) + " Key: " + str(k) + " Decrypted Text: " )
#         for i in string:
#             #print(i, end = " -> ")
#             p = ord(i) - 65
#
#             c = (p - k) % 26
#             c = c + 65
#             final = chr(c)
#             print(final)
#             with open("encrypt.txt", "a") as f:
#                 f.write(final)
#
#         k = str(k)
#
#         with open("encrypt.txt", "r") as f:
#             show = f.read()
#         Label(root, text="Decryption", font="Times 14 bold", fg="#FFFFFF", bg="#3C3F41").grid(row=4, column=3)
#         Label(root, text=show, fg="#E8EAED", bg="#3C3F41", font="Times 12 italic").grid(row=5, column=3)
#
# def encrypt_win():
#     root.geometry("1000x400")
#     new_win = Toplevel(root)
#     new_win.configure(background="#070E16")
#     # "window width x window height + position right + position down")
#     new_win.geometry("400x300+800+250")
#     new_win.maxsize(400, 300)
#     new_win.minsize(400, 300)
#     new_win.title("Encryption")
#     new_win.wm_iconbitmap("lock.ico")
#     # Heading
#     Label(new_win, text="Caesar Cipher", font="Helvatica 20 bold",fg="#E8EAED", bg="#070E16", padx=10, pady=5).grid(row=0, column=1)
#     # subheading
#     Label(new_win, text="Encryption", font="Helvatica 12 italic",fg="#E8EAED", bg="#070E16", padx=10, pady=0).grid(row=1, column=1)
#
#     # Plain text
#     Label(new_win, text="Enter text to Encrypt",fg="#E8EAED", bg="#070E16",font="comicsansms 10").grid(row=2, column=0)
#     #text_value = StringVar()
#     text_input = Entry(new_win, textvariable=text_value, fg="#E8EAED", bg="#3C3F41").grid(row=2, column=1)
#
#     # Key
#     Label(new_win, text="Enter Key",fg="#E8EAED", bg="#070E16", font="comicsansms 10").grid(row=3, column=0)
#     #key_value = IntVar()
#     key_input = Entry(new_win, textvariable=key_value, fg="#E8EAED", bg="#3C3F41").grid(row=3, column=1)
#
#     # Button
#     Button(new_win, text="Encrypt!", bg="#5DADE2", fg="#F4F6F7", padx=10, pady=10,command=encrypt).grid(row=5, column=1,pady=10)
#
# def decrypt_win():
#     root.geometry("1000x400")
#     new_win = Toplevel(root)
#     new_win.configure(background="#070E16")
#     # "window width x window height + position right + position down")
#     new_win.geometry("400x300+800+250")
#     new_win.geometry("400x300")
#     new_win.maxsize(400,300)
#     new_win.minsize(400,300)
#     new_win.title("Decryption")
#     new_win.wm_iconbitmap("lock.ico")
#     # Heading
#     Label(new_win, text="Caesar Cipher", font="Helvatica 20 bold",fg="#E8EAED", bg="#070E16", padx=10, pady=5).grid(row=0, column=1)
#     # subheading
#     Label(new_win, text="Decryption", font="Helvatica 12 italic", padx=10, pady=0, fg="#E8EAED", bg="#070E16").grid(row=1, column=1)
#
#     # Plain text
#     Label(new_win, text="Enter text to Decrypt", font="comicsansms 10", fg="#E8EAED", bg="#070E16").grid(row=2, column=0)
#     #text_value = StringVar()
#     text_input = Entry(new_win, textvariable=text_value, fg="#E8EAED", bg="#3C3F41").grid(row=2, column=1)
#
#     # Key
#     Label(new_win, text="Enter Key", font="comicsansms 10", fg="#E8EAED", bg="#070E16").grid(row=3, column=0)
#     #key_value = IntVar()
#     key_input = Entry(new_win, textvariable=key_value, fg="#E8EAED", bg="#3C3F41").grid(row=3, column=1)
#
#     # Button
#     Button(new_win, text="Decrypt!", bg="#5DADE2", fg="#F4F6F7", padx=10, pady=10,command=decrypt).grid(row=5, column=1,pady=10)
#
#
# # TODO: MAIN
# Label(root,text="Caesar Cipher", font="Baskerville 18 italic", fg="#E8EAED", bg="#3C3F41", pady=10).grid(row=0,column=2)
# Label(root,text="Select anyone of the following", font="Times 16 italic", fg="#E8EAED", bg="#3C3F41", pady=5).grid(row=1,column=2)
#
# # Lock Image
# lock = PhotoImage(file=r"C:\Users\Dayan Ahmed\Desktop\Cipher\locked.png")
# Label(image=lock,bg="#3C3F41",pady=5).grid(row=2,column=1,padx=5)
# Button(root,text="Encryption", font="Baskerville  16 italic", fg="#E8EAED", bg="#3C3F41", command=encrypt_win).grid(row=3,column=1,padx=15,pady=5)
#
#
#
# # photoa = PhotoImage(file=r"C:\Users\Dayan Ahmed\Desktop\Cipher\unlocked.png")
# photoa = PhotoImage(file=r"C:\Users\Vishwajeet\Pictures\Saved Pictures\Second_doubt.png")
# Label(image=photoa,bg="#3C3F41",pady=5).grid(row=2,column=3,padx=5)
#
# Button(root,text="Decryption", font="Baskerville  16 italic", fg="#E8EAED", bg="#3C3F41", command=decrypt_win).grid(row=3,column=3,padx=15,pady=5)
#
#
#
#
# root.mainloop()

############################################## GITHUB code 2 ##############################################################################
#Modified Caesar Cipher
#Code by Shibu Mohapatra
if __name__ == '__main__':
    from tkinter import *
    def main():
        txt.delete(0.0,'end')
        str = ent1.get()
        key = ent2.get()
        crypto = var_chk.get()
        if crypto == 1:
            encrypted = ''
            i = len(key)
            f = 0
            for x in str:
                if f == i:
                    f = 0
                indx = (ord(x) + int(key[f])) % 256
                if indx > 126:
                    indx = indx - 95
                encrypted = encrypted + chr(indx)
                f = f + 1
            txt.insert(0.0,encrypted)
        else:
            decrypted = ''
            i = len(key)
            f = 0
            for x in str:
                if f == i:
                    f = 0
                indx = (ord(x) - int(key[f])) % 256
                if indx < 32:
                    indx = indx + 95
                decrypted = decrypted + chr(indx)
                f = f + 1
            txt.insert(0.0,decrypted)

    root = Tk()
    root.geometry("300x300")


    #Creating Widgts
    message = Label(root , text = "Message:")
    keyBtn = Label(root , text = "key:")

    ent1 = Entry(root, width = 37)
    ent2 = Entry(root, width = 37)

    var_chk = IntVar()

    rb1 = Radiobutton(root , text = "encrypt" , variable = var_chk , value = 1)
    rb2 = Radiobutton(root , text = "decrypt" , variable = var_chk , value = 2)

    bt = Button(root , text = "Submit" , bg = "blue" , fg= "white" ,  command = main)

    txt = Text(root , width = 37 , height = 12 , wrap = WORD)


    #Placing them on screen
    message.grid(row = 0 , column = 0 , sticky = E)
    keyBtn.grid( row = 1 , column = 0 , sticky = E)

    ent1.grid( row = 0 , column = 1)
    ent2.grid( row = 1 , column = 1)

    rb1.grid( row = 2 , column = 0)
    rb2.grid( row = 2 , column = 1)

    bt.grid(row = 3 , columnspan = 2 )

    txt.grid( row = 4 , columnspan = 2 , sticky = W)

    root.mainloop()