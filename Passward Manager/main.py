from tkinter import *
import json
import random
from tkinter import messagebox

##################################   Password Generator   ############################

def Generate():
    small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    rand_small = [random.choice(small) for i in range(0, 3)]
    rand_capital = [random.choice(capital) for i in range(0, 3)]
    rand_number = [random.choice(numbers) for i in range(0, 2)]
    rand_symbol = [random.choice(symbols) for i in range(0, 2)]

    Password_list = rand_small + rand_capital + rand_number + rand_symbol
    random.shuffle(Password_list)

    Password = "".join(Password_list)
    Password_entry.insert(0, Password)


##################################  Save Details   ###################################

def save_details():
    website = Website_entry.get()
    Email = Email_entry.get()
    Password = Password_entry.get()
    Dict = {
        website:{
            "Email" : Email,
            "Password" : Password,
        }
    }
    if(len(website) == 0 or len(Email) == 0 or len(Password) == 0):
        messagebox.showinfo(title="Check Detals", message="Please filled all the details.")
    else:    
        Confirmation = messagebox.askokcancel(title=website, message=f"Your enter details : \nEmail : {Email} \n Password : {Password} \n Are you want tosave?")
        if Confirmation:
            try:
                with open('information.json', 'r') as object:
                    data = json.load(object)
            except FileNotFoundError:
                with open('Information.json', 'w') as object:
                    json.dump(Dict, object, indent=4)
            else:
                data.update(Dict)
                with open('Information.json', 'w') as object:
                    json.dump(data, object, indent=4)
            finally:
                Website_entry.delete(0, END)
                Password_entry.delete(0, END) 
                Email_entry.delete(0, END) 
                Website_entry.focus() 

################################   Password Search    #################################

def pass_search():
    website = Website_entry.get()
    try:
        with open('Information.json', 'r') as object:
            data = json.load(object)   
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f"No data found.")
    else:
        if website in data:
            mail = data[website]['Email']
            Pass = data[website]['Password']
            messagebox.showinfo(title=website, message=f"Email : {mail}\n Password : {Pass}") 
        else:
            messagebox.showinfo(title='No record', message=f"This {website} record not found.")       


##################################      UI      #######################################

window = Tk()
window.title('PASSWORD MANAGER')
window.config(padx=50, pady=60, bg='black')

canvas = Canvas(height=300, width=400, highlightthickness=0, bg='black')
Img = PhotoImage(file='logo.png')
canvas.create_image(200, 80, image = Img)
canvas.grid(row=0, column=1)

Website_label = Label(text='Website ', fg='white', bg='black', font=('jetbrains mono', 12, 'bold'))
Website_label.place(x=50, y = 190)
Website_entry = Entry(width=24)
Website_entry.place(x = 140, y = 190)
Website_entry.focus()

Email = Label(text="Email ", fg='white', bg='black', font=('jetbrains mono', 12, 'bold'))
Email.place(x = 50, y=220)
Email_entry = Entry(width=35)
Email_entry.place(x=140, y=220)

Password = Label(text="Password" , fg='white', bg='black', font=('jetbrains mono', 12, 'bold'))
Password.place(x=50, y = 250)
Password_entry = Entry(width=24)
Password_entry.place(x=140, y = 250)
print(Website_entry.get())

password_generate_botton = Button(text='Generate', relief=RAISED, command=Generate)
password_generate_botton.place(x=298, y=250)
Add_button = Button(text="Add", width=42, relief=RAISED, command=save_details)
Add_button.place(x=52, y=280)
Search_button = Button(text='Search', width=6, relief=RAISED, command=pass_search)
Search_button.place(x=302, y=190)

window.mainloop()