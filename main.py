
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint,choice,shuffle
import pyperclip
import json
def generate_password():
   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2,4))]
    password_list = password_letters+password_symbols+password_numbers
    password="".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0,END)
    password_input.insert(0,password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def add():
  website=website_input.get()
  email=email_input.get()
  password=password_input.get()
  if len(website)==0 or len(email)==0 or len(password)==0:
     messagebox.showerror(title="Error",message="Some fields are missing.")
  else: 
    is_ok=messagebox.askokcancel(title="is it ok",message=f"website: {website}\nemail:{email}\npassword: {password}\nis it ok?")
    if is_ok:
        new_data={website:{"email":email,"password":password}}
        try:
          with open("user_details.json","r") as data_file:
            data=json.load(data_file)
        except:
          with open("user_details.json","w") as data_file:
            json.dump(new_data,data_file,indent=4)
        else:
          data.update(new_data)
          with open("user_details.json","w") as file:
              json.dump(data,file,indent=4)
        finally:
            messagebox.showinfo(title="success",message="Details saved successfully.")
            website_input.delete(0,END)
            email_input.delete(0,END)
            password_input.delete(0,END)
# ---------------------------- Find Password ------------------------------- #
def find_password():
  website=website_input.get()
  try:
    with open("user_details.json","r") as data_file:
         data=json.load(data_file)
  except:
      messagebox.showerror(title="file not found error",message="No Data File Found.")
      return
  if website in data:
        email=data[website]["email"]
        password=data[website]["password"]
        messagebox.showinfo(title="found successfully",message=f"Your email is {email}\n Your password is {password}\n")
  else:
      messagebox.showerror(title="Not Found",message="website not found in file.")
# ---------------------------- UI SETUP ------------------------------- #



from tkinter import *
windows=Tk()
windows.title("Password Manager")
windows.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#lables
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
#creating inputs fiels
website_input=Entry(width=32)
website_input.grid(row=1,column=1)
website_input.focus()
email_input=Entry(width=42)
email_input.grid(row=2,column=1,columnspan=2)
password_input=Entry(width=32)
password_input.grid(row=3,column=1)
#creating buttons
search_button=Button(text="search",width=6,command=find_password)
search_button.grid(row=1,column=2)
generate_password=Button(text="Generate",command=generate_password)
generate_password.grid(row=3,column=2)
add_button=Button(text="Save",width=36,command=add)
add_button.grid(row=4,column=1,columnspan=2)
windows.mainloop()