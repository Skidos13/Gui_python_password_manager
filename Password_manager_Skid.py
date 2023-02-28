#password manger and generator
#this program intends to generate a password for the user 
#and store it in a file for future use
#the program will also allow the user to retrieve the password wiith a copy to cpliboard function
#the program will also allowv the user to change the password by deleting the old one and creating a new one

###imports###

import tkinter as tk
import random
import os
import pandas as pd
import csv
#backgtound color  HEX #075693
#backgtound color  RGBrgba(7,86,147,255)

#--------password generator function----------------
alphabet_low=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_high=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_char_list=['!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']','|',';',':','<','>','?','/']
number_list=['0','1','2','3','4','5','6','7','8','9']

#lets read the csv file
data=pd.read_csv("secret.csv")

#at each 3 letters an uppercase letter will be addeds
##function to generate password
def generate_password(password_letters):
    special_chars=int(password_letters/5)
    numbers=int(password_letters/5)
    password_letters= password_letters-special_chars-numbers
    password=""
    while len(password)<password_letters:
        password+=random.choice(alphabet_low)
        if len(password)%3==0:
            password+=random.choice(alphabet_high)
    for i in range(special_chars):
        password+=random.choice(special_char_list)
    for i in range(numbers):
        password+=random.choice(number_list)
    
    password=list(password)
    random.shuffle(password)
    password="".join(password)
    return password




#search function to check if the password has been generated before
def search_password(website):
    #clears the textbox
    text_box.delete('1.0',tk.END)
    #searches for the website in the csv file
    result=data[(data['website'].str.contains(website))]
    if result.empty==False :
        website_r=result['website'].to_string(header=False,index=False)
        email=result['email_account'].to_string(header=False,index=False)
        password=result['password'].to_string(header=False,index=False)
        text_box.insert(index='1.0',chars="Website: "+website_r+"\n"+"Email: "+email+"\n"+" Password: "+password)
    else:
        text_box.insert(index='1.0',chars="No password found for this website\n Try generating a new password")


    return 

#UI for the program
screen = tk.Tk()
screen.title("Skid Password Manager")
screen.geometry("600x400")
screen.config(padx=10,pady=10,bg='#075693')
#screen.resizable(False,False)
background = tk.PhotoImage(file="Skid_logo.png")
background_label = tk.Label(screen, image=background,bg='#075693')
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#labels & widgets
website_label=tk.Label(text="Before generating a new password \nPlease check if you already have a password for that website",font=("Arial",10,"bold"),fg="black")
website_label.grid(column=0,row=0,columnspan=4)

website_label2=tk.Label(text="Website:",font=("Arial",12,"bold"),fg="black",bg="#075693")
website_label2.grid(column=0,row=1)

website_entry=tk.Entry(width=35)
website_entry.grid(column=1,row=1)
#Search button
search_button=tk.Button(text="Search",width=20,font=("arial",10,"bold"))
search_button.grid(column=2,row=1)
#to add the search function
search_button.config(command=lambda:print(search_password(website_entry.get())))

#text box
text_box=tk.Text(width=50,height=4)
text_box.grid(column=0,row=3,columnspan=2)


#ask for password lenght

#second window
def Generator_window():
    


    Window = tk.Toplevel()
    Window.title("Password Generator")
    Window.geometry("460x200")
    Window.config(padx=1,pady=1,bg='#075693')

    #labels

    #website
    website_label2=tk.Label(Window,text="Website:",font=("Arial",12,"bold"),fg="black",bg="#075693",width=10)
    website_label2.grid(column=0,row=1)

    #website entry
    website_entry2=tk.Entry(Window,width=35)
    website_entry2.grid(column=1,row=1)

    
    #email
    email_label=tk.Label(Window,text="Email:",font=("Arial",12,"bold"),fg="black",bg="#075693",width=10)
    email_label.grid(column=0,row=2)
    
    #email entry
    email_entry=tk.Entry(Window,width=35)
    email_entry.grid(column=1,row=2)
    

    #password length
    password_length_label=tk.Label(Window,text="Password Length:",font=("Arial",10,"normal"),fg="black",bg="#075693")
    password_length_label.grid(column=0,row=3)

    #password length entry
    password_length_entry=tk.Entry(Window,width=2,bg="white",fg="black")
    password_length_entry.grid(column=1,row=3,padx=10,pady=10)

    #generate_passsword_textbox
    generate_password_text=tk.Text(Window,width=30,height=1)
    generate_password_text.grid(column=1,row=4,columnspan=2)

    #password generator
    generate_password_button=tk.Button(Window,text="Generate Password",width=20,font=("arial",10,"bold"))
    generate_password_button.grid(column=0,row=3,columnspan=1,rowspan=1,padx=10,pady=10)
    generate_password_button.config(command=lambda:[generate_password_text.delete("1.0",tk.END),
                                                    generate_password_text.insert(index="1.0",chars=generate_password(int(password_length_entry.get())))
                                                    ,save_credentials(website_entry2.get(),email_entry.get(),generate_password_text.get(index1="1.0",index2=tk.END))])
    

                                    
                                    
    #website_data=website_entry.get()
    #email_data=email_entry.get()
    #password_data=generate_password_text.get("1.0",tk.END)
    def save_credentials(website,email,password):
        print(website,email,password)
        list=[]
        list.append(website)
        list.append(email)
        list.append(password)
        df=pd.DataFrame([list],columns=['website','email_account','password'])
        df.to_csv('secret.csv',mode='a',header=False,index=False)
        return

    Window.mainloop()
    return


#website_data,email_data,password_data=Generator_window()





#generator_button
generator_button=tk.Button(text="Generate Password",width=20,font=("arial",10,"bold"))
generator_button.grid(column=2,row=3,columnspan=1,rowspan=1,padx=10,pady=10)
generator_button.config(command=lambda:Generator_window())

screen.mainloop()



