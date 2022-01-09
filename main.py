#!/usr/bin/env python
# coding: utf-8

# In[16]:


#tkinter - standard Python interface to the Tcl/Tk GUI toolkit        
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
#pyperclip - cross-platform Python module for copy and paste clipboard functions
import pyperclip

#generate a password
def password_generator():
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
          'm','n','o','p','q','r','s','t','u','v','w','x',
          'y','z','A','B','C','D','E','F','G','H','I','J',
           'K','L','M','N','O','P','Q','R','S','T','U','V',
           'W','X','Y','Z']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!','@','#','$','%','^','&','*']
    
    #list comprehension
    #choice() - returns a randomly selected element from the specified sequence
    #_ - returns the value of last executed expression value
    password_letters = [choice(letters) for _ in range(randint(4, 8))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    
    #shuffle() - takes a sequence, like a list, and reorganize the order of the items
    password_generated = password_letters + password_numbers + password_symbols
    shuffle(password_generated)
    
    #''.join() - takes all items in an iterable and joins them into one string
    password = ''.join(password_generated)
    password_entry.insert(0, password)
    #pyperclip - cross-platform Python module for copy and paste clipboard functions
    pyperclip.copy(password)

#save the password
def save_password():
    #get() - returns the value of the item with the specified key
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    #asktocancel() - shows a confirmation dialog that has two buttons: OK and Cancel
    is_ok = messagebox.askokcancel(title = website, message = 'Do you want to save the current password?')
    if is_ok:
        with open('password.txt', 'a') as password_file:
            #\n - new line character
            password_file.write(f'Website: {website}, Email: {email}, Password: {password}\n')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
#find password
def find_password():
    website = website_entry.get()
    
    with open('password.txt') as password_file:
        if website in password_file:
            email = password_file[website]['email']
            password = password_file[website]['password']
            messagebox.showinfo(title = website, message = f'Password: {password}\n')

#Tk() - allows you to register and unregister a callback function which will be called from the Tk mainloop
window = Tk()
window.title('Password Generator')
#padx and pady - a distance - designating external padding on each side of the slave widget
window.config(padx = 50, pady = 50)

canvas = Canvas(height = 200, width = 200)
p_img = PhotoImage(file = 'logo.png')
#c.create_image(x, y, option, ...)
#c.create_image() - this constructor returns the integer ID number of the image object for that canvas
canvas.create_image(100, 100, image = p_img)
canvas.grid(row = 0, column = 1)

website_label = Label(text = 'Website: ')
website_label.grid(row = 1, column = 0)
email_label = Label(text = 'Email/Username: ')
email_label.grid(row = 2, column = 0)
password_label = Label(text = 'Password: ')
password_label.grid(row = 3, column = 0)

website_entry = Entry(width = 35)
#columnspan - how many columns widgetoccupies; default 1
website_entry.grid(row = 1, column = 1, columnspan = 2)
#.focus() - this method returns the name of the widget which currently has the focus
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(row = 2, column = 1, columnspan = 2)
email_entry.insert(0, 'azadirecords@gmail.com')
password_entry = Entry(width = 35)
password_entry.grid(row = 3, column = 1)

password_generator_button = Button(text = 'Generate Password', command = password_generator)
password_generator_button.grid(row = 4, column = 1)
save_password_button = Button(text = 'Save Password', command = save_password)
save_password_button.grid(row = 5, column = 1)
find_password_button = Button(text = 'Find Password', command = find_password)
find_password_button.grid(row = 6, column = 1)  

window.mainloop()


# In[ ]:




