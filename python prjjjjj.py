from tkinter import *
from tkinter import ttk
import time
from tkinter.tix import *
from functools import partial
from PIL import Image,ImageTk
import smtplib
import random
import datetime
root=Tk()
root.geometry("1000x800")
load = Image.open(r'treen.jpg')
load4= Image.open(r'plantmoney.jpg')
image1 = ImageTk.PhotoImage(load4)
img = ImageTk.PhotoImage(load)
load1 = Image.open(r'home.jpg')
img1 = ImageTk.PhotoImage(load1)
load2 = Image.open(r'car.jpg')
img2 = ImageTk.PhotoImage(load2)
load3 = Image.open(r'edu.jpg')
img3= ImageTk.PhotoImage(load3)
load4 = Image.open(r'piggybank.png')
image_a = ImageTk.PhotoImage(load4)
load5=Image.open(r'business.jpg')
img4=ImageTk.PhotoImage(load5)
load6=Image.open(r'personal.jpg')
img5=ImageTk.PhotoImage(load6)
load7=Image.open(r'travel.jpg')
img6=ImageTk.PhotoImage(load7)
load8 =Image.open(r'loan.jpg')
image_c=ImageTk.PhotoImage(load8)
now = datetime.datetime.now()
time1 = ''
button_flashing = True
def h_b1(obj):
    def on_enter(e):
        obj.config(background='darkgoldenrod', foreground="black")

    def on_leave(e):
        obj.config(background='green', foreground='white')
    obj.bind('<Enter>', on_enter)
    obj.bind('<Leave>', on_leave)
def h_b(obj):
   def on_enter(e):
      obj.config(background='steelblue', foreground= "white")

   def on_leave(e):
      obj.config(background= 'lightgrey', foreground= 'black')
   obj.bind('<Enter>', on_enter)
   obj.bind('<Leave>', on_leave)
def display_page(b=True):
    def flash_func(object):
        flash_delay = 500
        flash_colours = ('dark green','light green',)
        def flashColour(object, colour_index):
            global button_flashing
            if button_flashing:
                object.configure(foreground=flash_colours[colour_index])
                root.after(flash_delay, flashColour, object, 1 - colour_index)
            elif b==False:
                object.configure(foreground=flash_colours[0])
                object.destroy()
        flashColour(object,0)
    def date_time_display():
        clock = Label(root, font=('times', 8, 'bold'), bg='white')
        clock.place(x=945, y=20)
        def tick():
            global time1
            time2 = time.strftime('%H:%M:%S')
            if time2 != time1:
                time1 = time2
                clock.config(text=time2)
            clock.after(100, tick)
        tick()
        Label(root, text=str(now.date()), font=('times new roman', 10, 'bold'), bg='white').place(x=928, y=0)
    for widget in root.winfo_children():
        widget.destroy()
    date_time_display()
    Label(root, image=img,bg="white").place(x=0, y=0)
    Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white", fg="green").place(x=500, y=80)
    Label(root, text="For any queries,send an email to trustybank1111@gmail.com", font=("times new roman", 9,),bg="white").place(x=700, y=678)
    def sign_up():
        for widget in root.winfo_children():
            widget.destroy()
        date_time_display()
        Label(root, image=img, bg="white").place(x=0, y=0)
        Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
        Label(root, text="For any queries,send an email to trustybank1111@gmail.com", font=("times new roman", 9,),bg="white").place(x=700, y=678)
        name2=StringVar()
        phone_no2=StringVar()
        g_mail2=StringVar()
        password2 = StringVar()
        confo_password2 = StringVar()
        Label(root,text="Enter your name",font=("Times new roman",20),bg="white").place(x=600,y=200)
        e1=Entry(root,textvariable=name2,font=("arial",19),bg="lightyellow")
        e1.place(x=600,y=250)
        Label(root,text="Enter your phone number",font=("Times new roman",20),bg="white").place(x=600,y=300)
        e2=Entry(root,textvariable=phone_no2,font=("arial",19),bg="lightyellow")
        e2.place(x=600,y=350)
        Label(root,text="Enter your gmail",font=("Times new roman",20),bg="white").place(x=600,y=400)
        e3=Entry(root,textvariable=g_mail2,font=("arial",19),bg="lightyellow")
        e3.place(x=600,y=450)
        def con():
            name=str(name2.get())
            phone_no=str(phone_no2.get())
            g_mail=str(g_mail2.get())
            if (name != "") and (phone_no != "") and (g_mail != "") and (len(phone_no)==10) and phone_no.isdigit():
                for widget in root.winfo_children():
                    widget.destroy()
                date_time_display()
                Label(root, image=img, bg="white").place(x=0, y=0)
                Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                otp2 = StringVar()
                otp_gen = str(random.randint(1000, 10000))
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("trustybank1111@gmail.com", "#Arch1@#")
                server.sendmail("trustybank1111@gmail.com", g_mail,otp_gen)
                server.quit()
                Label(root,text="OTP is sent to your email",font=("Times new roman",20,"underline"),bg="white",fg="green").place(x=600,y=300)
                Label(root,text="Please enter OTP",font=("Times new roman",20,"underline"),bg="white",fg="green").place(x=600,y=340)
                e4=Entry(root,textvariable=otp2,font=("arial",19),bg="lightyellow")
                e4.place(x=600,y=380)
                def deposit_amount():
                    for widget in root.winfo_children():
                        widget.destroy()
                    date_time_display()
                    Label(root, image=img, bg="white").place(x=0, y=0)
                    Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                    Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                    bal_amt2 = StringVar()
                    Label(root, text="Enter deposit amount",font=("Times new roman",20),bg="white").place(x=600,y=200)
                    e5 = Entry(root, textvariable=bal_amt2,font=("arial",19),bg="lightyellow")
                    e5.place(x=600,y=250)
                    Label(root,text="*Minimum amount to deposit is ₹ 2500",bg="white",font=("Calibre",15)).place(x=600,y=300)
                    def Insert_f():
                        bal_amt = str(bal_amt2.get())
                        if bal_amt.isdigit() and int(bal_amt) >= 2500:
                            password=str(password2.get())
                            f1 = open('bank_account.txt', 'r')
                            a = f1.readlines()
                            f1.close()
                            n = len(a) - 9
                            acc_no = str((n + 9) * 100 + n)
                            f2 = open('bank_account.txt', 'a')
                            dcard = debit_card()
                            insert = acc_no + " " + name + " " + phone_no + " " + g_mail + " " + dcard + " " + bal_amt + " " + password + " "+"\n"
                            f2.write(insert)
                            f2.close()
                            f3 = open('transaction_history.txt', 'a')
                            dcard = debit_card()
                            insert1 = acc_no + " " + name + " " + phone_no + " " + g_mail + " " + dcard + " " + bal_amt + " " + password + " " + "\n"
                            f3.write(insert1)
                            f3.close()
                            for widget in root.winfo_children():
                                widget.destroy()
                            date_time_display()
                            Label(root, image=img, bg="white").place(x=0, y=0)
                            Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"),bg="white", fg="green").place(x=500, y=80)
                            Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                            my_label = Label(root, text="Congratulations!!!", font=("Times New roman", 20,"underline"), bg="white",fg="green")
                            my_label.place(x=600, y=250)
                            my_label1 = Label(root, text="Your account is created", font=("Times New roman", 20,"underline"),bg="white", fg="green")
                            my_label1.place(x=600, y=290)
                            flash_func(my_label)
                            flash_func(my_label1)
                            Label(root,text="Your account number: "+acc_no,font=("Times New roman",20),bg="white",fg="saddlebrown").place(x=600,y=360)
                            Label(root, text="Your debit card number: ",font=("Times new roman",20),bg="white",fg="saddlebrown").place(x=600,y=390)
                            Label(root, text=dcard, font=("Times new roman", 20), bg="white",fg="saddlebrown").place(x=600, y=420)
                            b9=Button(root,text="Back",command=display_page,bg="green",font=("Calibre",15,"bold"),fg="white")
                            b9.place(x=600,y=480)
                            h_b1(b9)
                        else:
                            Label(root, text="*Minimum amount to deposit is ₹ 2500",bg="white",font=("Calibre",15),fg="red").place(x=600,y=300)
                            bal_amt2.set("")
                    b7=Button(root, text="Continue", command=Insert_f,font=("Calibre",15,"bold"),fg="white",bg="green")
                    b7.place(x=600,y=350)
                    h_b1(b7)
                    b8=Button(root,text="Back",command=partial(display_page,b=False),font=("Calibre",15,"bold"),fg="white",bg="green")
                    b8.place(x=705,y=350)
                    h_b1(b8)
                def passwords():
                    for widget in root.winfo_children():
                        widget.destroy()
                    date_time_display()
                    Label(root, image=img, bg="white").place(x=0, y=0)
                    Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                    Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                    tip = Balloon(root)
                    Label(root, text="Enter new password",font=("Times new roman",20),bg="white").place(x=600,y=200)
                    e6 = Entry(root,textvariable=password2,show="*",font=("arial",19),bg="lightyellow")
                    e6.place(x=600,y=250)
                    tip.bind_widget(e6,balloonmsg="Password must contain 1 lowercase,\n 1 uppercase, 1 number, 1 special character\n and at least 8 characters")
                    Label(root, text="Confirm password",font=("Times new roman",20),bg="white").place(x=600,y=300)
                    e7 = Entry(root,textvariable=confo_password2,show="*",font=("arial",19),bg="lightyellow")
                    e7.place(x=600,y=350)
                    tip.bind_widget(e7,balloonmsg="Password must contain 1 lowercase,\n 1 uppercase, 1 number, 1 special character\n and at least 8 characters")
                    def check_password():
                        password=str(password2.get())
                        confo_password=str(confo_password2.get())
                        d=0;s=0;u=0;l=0
                        for i in password:
                            if i.isdigit():
                                d +=1
                            elif i.isupper():
                                u+=1
                            elif i.islower():
                                l+=1
                            else:
                                s +=1
                        if (len(password)>=8) and l>0 and u>0 and s>0 and d>0:
                            if password == confo_password and (password != "") and (confo_password != ""):
                                b6=Button(root,text="Continue",command=deposit_amount,bg="green",font=("Calibre",15,"bold"),fg="white")
                                b6.place(x=671,y=400)
                                h_b1(b6)
                            else:
                                Label(root,text="*Passwords dont match",font=("Times new roman",15),bg="white",fg="red").place(x=600,y=450)
                                Label(root,text="Please enter password carefully",font=("Times new roman",15),bg="white",fg="red").place(x=600,y=470)
                                password2.set("")
                                confo_password2.set("")
                        else:
                            Label(root,text="*Password must contain 1 lowercase, ",font=("Times new roman",15),bg="white",fg="red").place(x=600,y=510)
                            Label(root,text="1 uppercase, 1 number, 1 special character",font=("Times new roman",15),bg="white",fg="red").place(x=600,y=540)
                            Label(root,text="and at least 8 characters",font=("Times new roman",15),bg="white",fg="red").place(x=600,y=570)
                            password2.set("")
                            confo_password2.set("")
                    b5=Button(root, text="Enter", command=check_password,bg="green",font=("Calibre",15,"bold"),fg="white")
                    b5.place(x=600,y=400)
                    h_b1(b5)
                def otp_check():
                    otp=otp2.get()
                    otp=str(otp)
                    if otp==otp_gen:
                        Label(root,text="Email successfully verified",font=("times new roman",15),bg="white").place(x=600,y=520)
                        b3=Button(root,text="Continue",command=passwords,bg="green",font=("Calibre",15,"bold"),fg="white")
                        b3.place(x=600,y=550)
                        h_b1(b3)
                    else:
                        for widget in root.winfo_children():
                            widget.destroy()
                        date_time_display()
                        Label(root, image=img, bg="white").place(x=0, y=0)
                        Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                        Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                        Label(root,text="*Incorrect OTP",font=("times new roman",20),bg="white",fg="red").place(x=600,y=350)
                        b4=Button(root, text="Go back to main page", command=display_page, bg="green",font=("Calibre", 15, "bold"), fg="white")
                        b4.place(x=600, y=400)
                        h_b1(b4)
                b2=Button(root,text="Enter",command=otp_check,bg="green",font=("Calibre",15,"bold"),fg="white")
                b2.place(x=600,y=430)
                h_b1(b2)
            else:
                if (name == "") or (phone_no == "") or (g_mail == ""):
                    Label(root,text="*Invalid details", font=("Times New Roman", 15), bg="white",fg="red").place(x=600,y=550)
                    name2.set("")
                    phone_no2.set("")
                    g_mail2.set("")
                elif (len(phone_no) != 10):
                    Label(root, text="*Invalid phone-number", font=("Times New Roman", 15), bg="white",fg="red").place(x=600,y=550)
                    phone_no2.set("")
        b=Button(root,text="Continue",command=con, font=("Calibre", 15, 'bold'), bg="green",fg="white")
        b.place(x=600, y=500)
        h_b1(b)
        b1=Button(root,text="Back",command=display_page, font=("Calibre", 15, 'bold'), bg="green",fg="white")
        b1.place(x=705, y=500)
        h_b1(b1)
    def debit_card():
        d_card=str(random.randint(1000,10000))+"-"+str(random.randint(1000,10000))+"-"+str(random.randint(1000,10000))+"-"+\
        str(random.randint(1000,10000))
        f=open('debit_card.txt','r')
        cards=f.readlines()
        f.close()
        if d_card in cards:
            debit_card()
        f1=open('debit_card.txt','a')
        f1.write(d_card+"\n")
        f1.close()
        return d_card
    def login():
        password_var2=StringVar()
        def transaction(a,b):
            global now
            acc_no=str(acc_var2.get())
            f = open('transaction_history.txt', 'r')
            his_read = f.readlines()
            f.close()
            new_line = his_read[int(b) // 100].rstrip("\n")
            his_read[int(b) // 100] = new_line + "$" + a + ",Date and Time:" + str(now) + "\n"
            insert = ""
            for i in his_read:
                insert += i
            f4 = open('transaction_history.txt', 'w')
            f4.write(insert)
            f4.close()
        def options():
            for widget in root.winfo_children():
                widget.destroy()
            date_time_display()
            Label(root, image=img, bg="white").place(x=0, y=0)
            Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
            Label(root, text="For any queries,send an email to trustybank1111@gmail.com", font=("times new roman", 9,),bg="white").place(x=700, y=678)
            def rd():
                global image_a
                for widget in root.winfo_children():
                    widget.destroy()
                panel = Label(root, image=image_a,bg="white")
                panel.pack(side='top', fill='both', expand='yes')
                amt_rd2 = StringVar()
                Label(root, text="RD CALCULATOR", font=("Times new Roman", 46, "bold", "underline"),fg="green",bg="white").place(x=100, y=50)
                Label(root, text="Select tenure in months",font=("Times new roman",20),bg="white").place(x=150,y=200)
                Label(root, text="Enter amount",font=("Times new roman",20),bg="white").place(x=150,y=313)
                Label(root, text="Are you a senior citizen?",font=("Times new roman",20),bg="white").place(x=150,y=450)
                e1 = Scale(root,from_=3, to=60, orient="horizontal", background='white', fg='black', troughcolor='sandybrown', activebackground='sienna',length=280,font=("arial",13),width=10)
                e1.place(x=150,y=250)
                e2 = Entry(root, textvariable=amt_rd2,font=("arial",19),bg="lightyellow")
                e2.place(x=150,y=360)
                Label(root,text="*Investment tenure can range from 3 to 60 months",font=("Times new roman",9),bg="white").place(x=150,y=291)
                Label(root,text="*Minimum monthly deposit is ₹ 100",font=("Times new roman",9),bg="white").place(x=150,y=395)
                def senior_yes():
                    duration_rd=str(e1.get())
                    monthly_amt_rd=str(amt_rd2.get())
                    if monthly_amt_rd != "" and float(monthly_amt_rd) and float(monthly_amt_rd) >= 100.0:
                        for widget in root.winfo_children():
                            widget.destroy()
                        panel = Label(root, image=image_a,bg="white")
                        panel.pack(side='top', fill='both', expand='yes')
                        Label(root, text="RD CALCULATOR", font=("Times new Roman", 46, "bold", "underline"),fg="green",bg="white").place(x=100, y=50)
                        duration_rd=int(duration_rd)
                        monthly_amt_rd=float(monthly_amt_rd)
                        if duration_rd <= 6:
                            roi_rd = 4
                        elif duration_rd <= 9:
                            roi_rd = 4.9
                        elif duration_rd <= 15:
                            roi_rd = 5.4
                        elif duration_rd <= 24:
                            roi_rd = 5.5
                        elif duration_rd <= 36:
                            roi_rd = 5.65
                        elif duration_rd <= 60:
                            roi_rd = 5.85
                        else:
                            roi_rd = 6.3
                        interest_rd = monthly_amt_rd * pow(1 + roi_rd / 12.0, duration_rd)
                        final_amt_rd = monthly_amt_rd * duration_rd + interest_rd
                        final_amt_rd = round(final_amt_rd, 2)
                        Label(root, text="Amount on maturity :",font=("Times new roman",20),bg="white",fg="dark green").place(x=150,y=300)
                        Label(root, text="₹ "+str(final_amt_rd),font=("Times new roman",20),bg="white",fg="dark green").place(x=150,y=350)
                        b4=Button(root, text="Back", command=options, bg="green",font=("Calibre",15,'bold'),fg='white')
                        b4.place(x=150,y=400)
                        h_b1(b4)
                    else:
                        Label(root,text="*Invalid entry", font=("Times New Roman", 15), bg="white",fg="red").place(x=150,y=545)
                        amt_rd2.set("")
                def senior_no():
                    duration_rd=str(e1.get())
                    monthly_amt_rd=str(amt_rd2.get())
                    if monthly_amt_rd != "" and duration_rd.isdigit() and float(monthly_amt_rd) and float(monthly_amt_rd) >= 100.0:
                        for widget in root.winfo_children():
                            widget.destroy()
                        panel = Label(root, image=image_a,bg="white")
                        panel.pack(side='top', fill='both', expand='yes')
                        Label(root, text="RD CALCULATOR", font=("Times new Roman", 46, "bold", "underline"),fg="green",bg="white").place(x=100, y=50)
                        duration_rd=int(duration_rd)
                        monthly_amt_rd=float(monthly_amt_rd)
                        if duration_rd <= 6:
                            roi_rd = 3.5
                        elif duration_rd <= 9:
                            roi_rd = 4.4
                        elif duration_rd <= 15:
                            roi_rd = 4.9
                        elif duration_rd <= 24:
                            roi_rd = 5
                        elif duration_rd <= 36:
                            roi_rd = 5.15
                        elif duration_rd <= 60:
                            roi_rd = 5.35
                        else:
                            roi_rd = 5.5
                        interest_rd = monthly_amt_rd * pow(1 + roi_rd / 12.0, duration_rd)
                        final_amt_rd = (monthly_amt_rd * duration_rd) + interest_rd
                        final_amt_rd=round(final_amt_rd,2)
                        Label(root, text="Amount on maturity :",font=("Times new roman",20),bg="white",fg="dark green").place(x=150,y=300)
                        Label(root, text="₹ "+str(final_amt_rd),font=("Times new roman",20),bg="white",fg="dark green").place(x=150,y=350)
                        b5=Button(root, text="Back", command=options, bg="green",font=("Calibre",15,'bold'),fg='white')
                        b5.place(x=150,y=400)
                        h_b1(b5)
                    else:
                        Label(root,text="*Invalid entry", font=("Times New Roman", 15), bg="white",fg="red").place(x=150,y=545)
                        amt_rd2.set("")
                b1=Button(root, text="Yes", command=senior_yes,bg="green",font=("Calibre",15,"bold"),fg="white")
                b1.place(x=150,y=500)
                h_b1(b1)
                b2=Button(root, text="No", command=senior_no,bg="green",font=("Calibre",15,"bold"),fg="white")
                b2.place(x=205,y=500)
                h_b1(b2)
                b3=Button(root, text="Back", command=options,bg="green",font=("Calibre",15,"bold"),fg="white")
                b3.place(x=150,y=580)
                h_b1(b3)
            def fd():
                for widget in root.winfo_children():
                    widget.destroy()
                duration_fd2 = DoubleVar()
                amt_fd2 = IntVar()
                Label(root, text="Enter duration of FD [in days]",font=("Calibre",15),bg="light blue",fg="green").grid(row=0, column=0)
                Label(root, text="Enter amount of FD",font=("Calibre",15),bg="light blue",fg="green").grid(row=1, column=0)
                Label(root, text="Are you a senior citizen?[60 yrs or above]",font=("Calibre",15),bg="light blue",fg="blue").grid(row=2, column=0)
                e1 = Entry(root, textvariable=duration_fd2)
                e1.grid(row=0, column=1)
                e2 = Entry(root, textvariable=amt_fd2)
                e2.grid(row=1, column=1)

                def senior_yes():
                    for widget in root.winfo_children():
                        widget.destroy()
                    amt_fd = float(amt_fd2.get())
                    duration_fd = float(duration_fd2.get())

                    if amt_fd < 20000000:
                        if duration_fd <= 29:
                            roi_fd = 2.5
                        elif duration_fd <= 90:
                            roi_fd = 3
                        elif duration_fd <= 184:
                            roi_fd = 3.5
                        elif duration_fd <= 365:
                            roi_fd = 4.4
                        elif duration_fd <= 545:
                            roi_fd = 4.9
                        elif duration_fd <= 730:
                            roi_fd = 5
                        elif duration_fd <= 1095:
                            roi_fd = 5.15
                        elif duration_fd <= 1825:
                            roi_fd = 5.35
                        elif duration_fd <= 3650:
                            roi_fd = 5.5
                        else:
                            roi_fd = 5.6
                    else:
                        if duration_fd <= 29:
                            roi_fd = 2.5
                        elif duration_fd <= 90:
                            roi_fd = 2.75
                        elif duration_fd <= 184:
                            roi_fd = 3
                        elif duration_fd <= 365:
                            roi_fd = 3.5
                        elif duration_fd <= 545:
                            roi_fd = 3.65
                        elif duration_fd <= 730:
                            roi_fd = 4
                        elif duration_fd <= 1095:
                            roi_fd = 4.1
                        elif duration_fd <= 1825:
                            roi_fd = 4.25
                        elif duration_fd <= 3650:
                            roi_fd = 4.4
                        else:
                            roi_fd = 4.7
                    duration_fd /= 365.0
                    interest_fd = duration_fd * amt_fd * roi_fd / 100.0
                    final_amt_fd = amt_fd + interest_fd
                    final_amt_fd=round(final_amt_fd,2)
                    Label(root, text="Amount on maturity : Rs."+str(final_amt_fd),font=("Calibre",15),bg="light blue",fg="blue").place(x=80,y=100)
                    Button(root,text="Back",command=options,bg="papayawhip",font=("Calibre",15)).place(x=175,y=150)
                def senior_no():
                    for widget in root.winfo_children():
                        widget.destroy()
                    amt_fd = float(amt_fd2.get())
                    duration_fd = float(duration_fd2.get())

                    if amt_fd < 20000000:
                        if duration_fd <= 29:
                            roi_fd = 3
                        elif duration_fd <= 90:
                            roi_fd = 3.5
                        elif duration_fd <= 184:
                            roi_fd = 4
                        elif duration_fd <= 365:
                            roi_fd = 4.9
                        elif duration_fd <= 545:
                            roi_fd = 5.4
                        elif duration_fd <= 730:
                            roi_fd = 5.5
                        elif duration_fd <= 1095:
                            roi_fd = 5.65
                        elif duration_fd <= 1825:
                            roi_fd = 5.85
                        elif duration_fd <= 3650:
                            roi_fd = 6
                        else:
                            roi_fd = 6.3
                    else:
                        if duration_fd <= 29:
                            roi_fd = 2.55
                        elif duration_fd <= 90:
                            roi_fd = 2.8
                        elif duration_fd <= 184:
                            roi_fd = 3.05
                        elif duration_fd <= 365:
                            roi_fd = 3.55
                        elif duration_fd <= 545:
                            roi_fd = 3.7
                        elif duration_fd <= 730:
                            roi_fd = 4.05
                        elif duration_fd <= 1095:
                            roi_fd = 4.15
                        elif duration_fd <= 1825:
                            roi_fd = 4.3
                        elif duration_fd <= 3650:
                            roi_fd = 4.45
                        else:
                            roi_fd = 4.75
                    duration_fd /= 365.0
                    interest_fd = duration_fd * amt_fd * roi_fd / 100.0
                    final_amt_fd = amt_fd + interest_fd
                    final_amt_fd = round(final_amt_fd, 2)
                    Label(root, text="Amount on maturity : Rs." + str(final_amt_fd),font=("Calibre",15),bg="light blue",fg="blue").place(x=80,y=100)
                    Button(root, text="Back", command=options,bg="papayawhip",font=("Calibre",15)).place(x=175,y=150)
                Button(root, text="Yes", command=senior_yes,bg="papayawhip",font=("Calibre",15)).grid(row=2, column=1)
                Button(root, text="No", command=senior_no,bg="papayawhip",font=("Calibre",15)).grid(row=2, column=2)
                Button(root,text="Back",command=options,bg="papayawhip",font=("Calibre",15)).place(x=575,y=59.4)
            def check_balance():
                for widget in root.winfo_children():
                    widget.destroy()
                date_time_display()
                Label(root, image=img, bg="white").place(x=0, y=0)
                Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                acc_no=int(acc_var2.get())
                f3 = open('bank_account.txt', 'r')
                s = f3.readlines()
                line = s[acc_no//100].strip()
                linearray = line.split(" ")
                f3.close()
                insert="Your balance is ₹ "+linearray[-2]
                Label(root,text=insert,font=("Times new roman",20),bg="white",fg="dark green").place(x=600,y=300)
                b=Button(root,text="Back",command=options, bg="green",font=("Calibre",15,'bold'),fg='white')
                b.place(x=600,y=350)
                h_b1(b)
            def order_dd():
                for widget in root.winfo_children():
                    widget.destroy()
                date_time_display()
                Label(root, image=img, bg="white").place(x=0, y=0)
                Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                payee_name = StringVar()
                amt_dd2 = StringVar()
                Label(root, text="Enter payee name",font=("Times new roman",20),bg="white").place(x=600,y=250)
                e = Entry(root, textvariable=payee_name,font=("arial",19),bg="lightyellow")
                e.place(x=600,y=300)
                Label(root, text="Enter amount",font=("Times new roman",20),bg="white").place(x=600,y=350)
                e1 = Entry(root, textvariable=amt_dd2,font=("arial",19),bg="lightyellow")
                e1.place(x=600,y=400)
                def confirm_dd():
                    if str(payee_name.get()) != "" and str(amt_dd2.get()) != "" and str(amt_dd2.get()).isdigit():
                        for widget in root.winfo_children():
                            widget.destroy()
                        date_time_display()
                        Label(root, image=img, bg="white").place(x=0, y=0)
                        Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                        Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                        Label(root, text="Payee_name: " + str(payee_name.get()),font=("Times new roman",20),bg="white").place(x=600,y=250)
                        Label(root, text="Amount: ₹ " + str(amt_dd2.get()),font=("Times new roman",20),bg="white").place(x=600,y=290)
                        def print_dd():
                            acc_no = str(acc_var2.get())
                            f = open("bank_account.txt", 'r')
                            a = f.readlines()
                            x = a[int(acc_no) // 100]
                            line = x.strip().split(" ")
                            e_mail = line[3]
                            amt=int(line[5])
                            f.close()
                            amt_dd=int(amt_dd2.get())
                            if amt_dd>amt:
                                Label(root,text="*Insufficient balance",font=("times new roman", 15), bg="white",fg="red").place(x=600, y=395)
                            else:
                                Label(root, text="The dd has been sent to your email!!",font=("times new roman", 15), bg="white", fg="green").place(x=600, y=395)
                                dd_no = "TB-" + str(random.randint(1000, 9999)) + "-" + str(random.randint(1000, 9999))
                                dd = "TRUSTY BANK\nDEMAND DRAFT\n\nPayee: " + str(payee_name.get()) + "\nAmount: " + str(
                                amt_dd2.get()) + "\nDD number: " + dd_no
                                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                                server.login("trustybank1111@gmail.com", "#Arch1@#")
                                server.sendmail("trustybank1111@gmail.com", e_mail,dd)
                                server.quit()
                                f1 = open('dd.txt', 'a')
                                dd_entry = dd_no + " Amount: " + str(amt_dd2.get()) + " To: " + str(payee_name.get()) +" From: "+line[1]+" "+"\n"
                                f1.write(dd_entry)
                                f1.close()
                                z = int(line[5])
                                z -= int(str(amt_dd2.get()))
                                line[5] = str(z)
                                new_line = ""
                                for i in line:
                                    new_line = new_line + i + " "
                                a[int(acc_no) // 100] = new_line + "\n"
                                insert2 = ""
                                for i in a:
                                    insert2 += i
                                f2 = open('bank_account.txt', 'w')
                                f2.write(insert2)
                                f2.close()
                                insert3 = "Amount:" + str(amt_dd) + ",From:" + line[1]+",From acc_no:"+ line[0] + ",To:" + dd_no + ">" + str(payee_name.get())
                                transaction(insert3,acc_no)
                        b=Button(root, text="Confirm", command=print_dd,bg="green",font=("Calibre",15,'bold'),fg="white")
                        b.place(x=600,y=340)
                        h_b1(b)
                        b1=Button(root, text="Back", command=order_dd,bg="green",font=("Calibre",15,'bold'),fg="white")
                        b1.place(x=695,y=340)
                        h_b1(b1)
                    else:
                        Label(root,text="*Invalid details",font=("times new roman",15),bg="white",fg="red").place(x=600,y=500)
                        payee_name.set("")
                        amt_dd2.set("")
                b=Button(root, text="Enter", command=confirm_dd,bg="green",font=("Calibre",15,'bold'),fg="white")
                b.place(x=600,y=450)
                h_b1(b)
                b1=Button(root,text="Back",command=options,bg="green",font=("Calibre",15,'bold'),fg="white")
                b1.place(x=671,y=450)
                h_b1(b1)
            def encash_dd():
                for widget in root.winfo_children():
                    widget.destroy()
                date_time_display()
                Label(root, image=img, bg="white").place(x=0, y=0)
                Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                dd_no2=StringVar()
                Label(root,text="Enter DD number",font=("Times new roman",20),bg="white").place(x=600,y=250)
                e=Entry(root,textvariable=dd_no2,font=("arial",19),bg="lightyellow")
                e.place(x=600,y=300)
                def e_dd_check():
                    dd_no=str(dd_no2.get()).strip()
                    f=open('dd.txt','r')
                    s=f.readlines()
                    f.close()
                    dd_list=[]
                    for i in s:
                        dd_list.append(i.split(" ")[0])
                    if dd_no in dd_list:
                        line=s[dd_list.index(dd_no)].split(" ")
                        acc_no=acc_var2.get()
                        f1=open('bank_account.txt','r')
                        s1 = f1.readlines()
                        f1.close()
                        v = s1[int(acc_no)//100].strip().split(" ")
                        a = line[4]
                        b = v[1]
                        if b == a:
                            amt_dd_txt = int(line[2])
                            x = int(v[5])
                            x += amt_dd_txt
                            v[5] = str(x)
                            new_line = ""
                            for i in v:
                                new_line = new_line+i+" "
                            s1[int(acc_no)//100] = new_line + "\n"
                            insert2 = ""
                            for i in s1:
                                insert2 += i
                            f2 = open('bank_account.txt', 'w')
                            f2.write(insert2)
                            f2.close()
                            s[dd_list.index(dd_no)] = ""
                            f3=open('dd.txt','w')
                            insert1=""
                            for i in s:
                                insert1 += i
                            f3.write(insert1)
                            f3.close()
                            insert3 = "Amount:" + str(amt_dd_txt) + ",From:" + dd_no+ ",Payer name:"+line[6]
                            transaction(insert3,acc_no)
                            Label(root,text="DD has been encashed!!",font=("times new roman", 15), bg="white", fg="green").place(x=600, y=400)
                        else:
                            Label(root,text="*DD not registered in your name",font=("times new roman",15),bg="white",fg="red").place(x=600,y=400)
                    else:
                        Label(root,text="*Invalid DD number",font=("times new roman",15),bg="white",fg="red").place(x=600,y=400)
                        dd_no2.set('')
                b=Button(root,text="Enter",command=e_dd_check,bg="green",font=("Calibre",15,'bold'),fg="white")
                b.place(x=600,y=350)
                h_b1(b)
                b1=Button(root,text="Back",command=options,bg="green",font=("Calibre",15,'bold'),fg="white")
                b1.place(x=671,y=350)
                h_b1(b1)
            def transfer_money():
                for widget in root.winfo_children():
                    widget.destroy()
                date_time_display()
                Label(root, image=img, bg="white").place(x=0, y=0)
                Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                payee_acc2=StringVar()
                trans_amt2=StringVar()
                Label(root,text="Enter payee acc_number",font=("Times new roman",20),bg="white").place(x=600,y=250)
                e=Entry(root,textvariable=payee_acc2,font=("arial",19),bg="lightyellow")
                e.place(x=600,y=300)
                Label(root,text="Enter amount to transfer",font=("Times new roman",20),bg="white").place(x=600,y=350)
                e1=Entry(root,textvariable=trans_amt2,font=("arial",19),bg="lightyellow")
                e1.place(x=600,y=400)
                def acc_check2():
                    payee_acc=str(payee_acc2.get())
                    trans_amt=str(trans_amt2.get())
                    if payee_acc != "" and trans_amt != "" and trans_amt.isdigit() and payee_acc.isdigit():
                        f = open('bank_account.txt', 'r')
                        full = f.readlines()
                        f.close()
                        from_acc_no = str(acc_var2.get())
                        from_list = full[int(from_acc_no) // 100].strip().split(" ")
                        f3 = open('bank_account.txt', 'r')
                        s = f3.readlines()
                        f3.close()
                        a = []
                        for i in s:
                            x = i.split(" ")
                            a.append(x[0])
                        if payee_acc in a:
                            def confirm_trans():
                                acc_no=str(acc_var2.get())
                                if int(from_list[5])>= int(trans_amt):
                                    to_list=full[int(payee_acc)//100].strip().split(" ")
                                    to_list[5]=str(int(to_list[5])+int(trans_amt))
                                    from_list[5] = str(int(from_list[5]) - int(trans_amt))
                                    insert_from=""
                                    insert_to=""
                                    for i in from_list:
                                        insert_from+=i+" "
                                    for i in to_list:
                                        insert_to+=i+" "
                                    full[int(from_acc_no)//100]=insert_from+"\n"
                                    full[int(payee_acc)//100]=insert_to+"\n"
                                    insert=""
                                    for i in full:
                                        insert+=i
                                    f1=open('bank_account.txt','w')
                                    f1.write(insert)
                                    f1.close()
                                    insert2 = "Amount:" + trans_amt + ",From:" + from_list[1] + ",From acc_no:"+from_list[0]+",To:" + to_list[1]+",To acc_no:"+to_list[0]
                                    transaction(insert2,acc_no)
                                    transaction(insert2,payee_acc)
                                    Label(root, text="Transaction successful!!",font=("times new roman", 15), bg="white", fg="green").place(x=600, y=395)
                                else:
                                    Label(root, text="*Insufficient balance", font=("times new roman", 15), bg="white",fg="red").place(x=600, y=395)
                            for widget in root.winfo_children():
                                widget.destroy()
                            date_time_display()
                            Label(root, image=img, bg="white").place(x=0, y=0)
                            Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"),bg="white",fg="green").place(x=500, y=80)
                            Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                            Label(root, text="Payee acc_number: " + payee_acc,font=("Times new roman",20),bg="white").place(x=600,y=250)
                            Label(root,text="Amount: ₹ " + trans_amt,font=("Times new roman",20),bg="white").place(x=600,y=290)
                            b=Button(root, text="Confirm", command=confirm_trans,bg="green",font=("Calibre",15,'bold'),fg="white")
                            b.place(x=600,y=340)
                            h_b1(b)
                            b1=Button(root, text="Back", command=transfer_money, bg="green",font=("Calibre",15,'bold'),fg="white")
                            b1.place(x=695,y=340)
                            h_b1(b1)
                        else:
                            Label(root,text="*Invalid account number", font=("Times New Roman", 15), bg="white",fg="red").place(x=600,y=500)
                            Label(root,text="Re-enter details", font=("Times New Roman", 15), bg="white",fg="red").place(x=600,y=520)
                            payee_acc2.set("")
                            trans_amt2.set("")
                    else:
                        Label(root,text="*Invalid details",font=("times new roman",15),bg="white",fg="red").place(x=600,y=500)
                        payee_acc2.set("")
                        trans_amt2.set("")
                b9=Button(root,text="Enter",command=acc_check2,bg="green",font=("Calibre",15,'bold'),fg="white")
                b9.place(x=600,y=450)
                h_b1(b9)
                b10=Button(root,text="Back",command=options,bg="green",font=("Calibre",15,'bold'),fg="white")
                b10.place(x=671,y=450)
                h_b1(b10)
            def loan():
                for widget in root.winfo_children():
                    widget.destroy()
                panel = Label(root, image=image_c, bg="white")
                panel.place(x=380, y=280)
                date_time_display()
                Label(root, text="Loan Calculator", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=50, y=20)
                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)

                date_time_display()
                roi = 0.0
                amt2 = StringVar()
                Label(root, text="Enter loan amount",font=("Times new Roman",20),bg="white").place(x=50,y=200)
                e = Entry(root, textvariable=amt2,font=("ariel",19),bg="lightyellow")
                e.place(x=50,y=250)

                n2 = StringVar()
                Label(root, text="No of monthly payments",font=("Times new Roman",20),bg="white").place(x=50,y=300)
                e1 = Entry(root, textvariable=n2,font=("ariel",19),bg="lightyellow")
                e1.place(x=50,y=350)

                credit_score2 = StringVar()
                Label(root, text="Enter your credit score",font=("Times new Roman",20),bg="white").place(x=50,y=400)
                e2 = Entry(root, textvariable=credit_score2,font=("ariel",19),bg="lightyellow")
                e2.place(x=50,y=450)
                Label(root, text="*Enter 0 credit score for Education or Business loan",font=("Times new Roman",10),bg="white").place(x=50,y=485)
                Label(root, text="Select type of loan", font=("Times new Roman", 20), bg="white").place(x=50,y=520)
                n = StringVar()
                ltype = ttk.Combobox(root, width=27, textvariable=n,font=("Times new Roman",15))
                ltype['values'] = ('Vehicle Loan',
                                   'Home Loan',
                                   'Education Loan',
                                   'Business Loan',
                                   'Personal Loan',
                                   'Travel Loan')
                ltype.place(x=50,y=570)
                ltype.current(0)
                def choose():
                    a = str(ltype.get())
                    def home_loan():
                        amt3 = str(amt2.get())
                        credit_score3 = str(credit_score2.get())
                        n3 = str(n2.get())
                        if n3.isdigit() and amt3.isdigit() and credit_score3.isdigit():
                            if int(credit_score3) >= 0 and int(credit_score3) <= 850 and int(credit_score3) != 0 and int(amt3) != 0:
                                def saleried_home():
                                    credit_score = int(str(credit_score2.get()))
                                    amt = int(str(amt2.get()))
                                    if credit_score <= 600:
                                        if amt < 5000000:
                                            roi = 7.5
                                        elif amt < 10000000:
                                            roi = 7.7
                                        elif amt < 30000000:
                                            roi = 7.7
                                        else:
                                            roi = 7.8
                                    elif credit_score <= 649:
                                        if amt < 5000000:
                                            roi = 7.3
                                        elif amt < 10000000:
                                            roi = 7.6
                                        elif amt < 30000000:
                                            roi = 7.7
                                        else:
                                            roi = 7.7
                                    elif credit_score <= 699:
                                        if amt < 5000000:
                                            roi = 7.1
                                        elif amt < 10000000:
                                            roi = 7.3
                                        elif amt < 30000000:
                                            roi = 7.4
                                        else:
                                            roi = 7.5
                                    else:
                                        if amt < 5000000:
                                            roi = 6.66
                                        elif amt < 10000000:
                                            roi = 6.9
                                        elif amt < 30000000:
                                            roi = 7.1
                                        else:
                                            roi = 7.2
                                    calc(roi, 1,home_loan)

                                def unsaleried_home():
                                    credit_score = int(str(credit_score2.get()))
                                    amt = int(str(amt2.get()))
                                    if credit_score <= 600:
                                        if amt < 5000000:
                                            roi = 7.6
                                        elif amt < 10000000:
                                            roi = 7.8
                                        elif amt < 30000000:
                                            roi = 7.8
                                        else:
                                            roi = 7.9
                                    elif credit_score <= 649:
                                        if amt < 5000000:
                                            roi = 7.4
                                        elif amt < 10000000:
                                            roi = 7.7
                                        elif amt < 30000000:
                                            roi = 7.8
                                        else:
                                            roi = 7.8
                                    elif credit_score <= 699:
                                        if amt < 5000000:
                                            roi = 7.2
                                        elif amt < 10000000:
                                            roi = 7.4
                                        elif amt < 30000000:
                                            roi = 7.5
                                        else:
                                            roi = 7.6
                                    else:
                                        if amt < 5000000:
                                            roi = 6.76
                                        elif amt < 10000000:
                                            roi = 7
                                        elif amt < 30000000:
                                            roi = 7.2
                                        else:
                                            roi = 7.3
                                    calc(roi, 1,home_loan)

                                for widget in root.winfo_children():
                                    widget.destroy()
                                Label(root, image=img1,bg="white").place(x=0, y=0)
                                Label(root, text="Home Loan", font=("Times new Roman", 46, "bold", "underline"),
                                      bg="light grey", fg="green").place(x=50, y=80)
                                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                                      font=("times new roman", 9,), bg="white").place(x=700, y=678)
                                date_time_display()
                                bb1 = Button(root, text="Salaried", command=saleried_home, font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb1.place(x=50, y=250)
                                h_b1(bb1)
                                bb2 = Button(root, text="Unsalaried", command=unsaleried_home,
                                             font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb2.place(x=50, y=310)
                                h_b1(bb2)
                                bb3 = Button(root, text="Back", command=loan, font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb3.place(x=50, y=380)
                                h_b1(bb3)
                            else:
                                Label(root, text="*Invalid credit score", font=("Times New Roman", 15), bg="white",
                                      fg="red").place(x=50, y=620)
                                credit_score2.set("")
                        else:
                            loan()
                    def vehicle_loan():
                        amt3 = str(amt2.get())
                        credit_score3 = str(credit_score2.get())
                        n3 = str(n2.get())
                        if n3.isdigit() and amt3.isdigit() and credit_score3.isdigit():
                            if int(credit_score3) >= 0 and int(credit_score3) <= 850 and int(credit_score3) != 0 and int(amt3) != 0:
                                for widget in root.winfo_children():
                                    widget.destroy()
                                Label(root, image=img2, bg="white").place(x=0, y=0)
                                Label(root, text="Vehicle Loan", font=("Times new Roman", 46, "bold", "underline"),
                                      bg="white", fg="green").place(x=50, y=80)
                                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                                      font=("times new roman", 9,), bg="white").place(x=700, y=678)
                                date_time_display()
                                def new_car():
                                    credit_score = int(str(credit_score2.get()))
                                    if credit_score <= 300:
                                        roi = -1
                                    elif credit_score <= 500:
                                        roi = 12.99
                                    elif credit_score <= 600:
                                        roi = 9.92
                                    elif credit_score <= 660:
                                        roi = 6.32
                                    elif credit_score <= 780:
                                        roi = 3.64
                                    else:
                                        roi = 2.58
                                    calc(roi, 2, vehicle_loan)
                                def used_car():
                                    credit_score = int(str(credit_score2.get()))
                                    if credit_score <= 300:
                                        roi = -1
                                    elif credit_score <= 500:
                                        roi = 19.85
                                    elif credit_score <= 600:
                                        roi = 15.91
                                    elif credit_score <= 660:
                                        roi = 9.77
                                    elif credit_score <= 780:
                                        roi = 5.35
                                    else:
                                        roi = 3.68
                                    calc(roi, 2,vehicle_loan)
                                bb1 = Button(root, text="New  Vehicle", command=new_car, font=("Calibre", 15, "bold"),
                                             bg="green",
                                             fg="white")
                                bb1.place(x=50, y=250)
                                h_b1(bb1)
                                bb2 = Button(root, text="Used Vehicle", command=used_car, font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb2.place(x=50, y=310)
                                h_b1(bb2)
                                bb3 = Button(root, text="Back", command=loan, font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb3.place(x=50, y=380)
                                h_b1(bb3)
                            else:
                                Label(root,text="*Invalid credit score", font=("Times New Roman", 15), bg="white",fg="red").place(x=50,y=620)
                                credit_score2.set("")
                        else:
                            loan()
                    def edu_loan():
                        amt3 = str(amt2.get())
                        credit_score3 = str(credit_score2.get())
                        n3 = str(n2.get())
                        if n3.isdigit() and amt3.isdigit() and credit_score3.isdigit():
                            if int(credit_score3) >= 0 and int(credit_score3) <= 850 and int(credit_score3) != 0 and int(amt3) != 0:
                                for widget in root.winfo_children():
                                    widget.destroy()
                                Label(root, image=img3, bg="white").place(x=0, y=0)
                                Label(root, text="Education Loan", font=("Times new Roman", 46, "bold", "underline"),
                                      bg="white", fg="green").place(x=50, y=80)
                                Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                                      font=("times new roman", 9,), bg="white").place(x=700, y=678)
                                date_time_display()
                                def iit():
                                    for widget in root.winfo_children():
                                        widget.destroy()
                                    Label(root, image=img3, bg="white").place(x=0, y=0)
                                    Label(root, text="Education Loan", font=("Times new Roman", 46, "bold", "underline"),
                                          bg="white", fg="green").place(x=50, y=80)
                                    Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                                          font=("times new roman", 9,), bg="white").place(x=700, y=678)
                                    date_time_display()

                                    def iit_male():
                                        calc(7.5, 3,edu_loan)

                                    def iit_female():
                                        calc(7, 3,edu_loan)

                                    bb1 = Button(root, text="Male", command=iit_male, font=("Calibre", 15, "bold"),
                                                 bg="green",
                                                 fg="white")
                                    bb1.place(x=50, y=250)
                                    h_b1(bb1)
                                    bb2 = Button(root, text="Female or Others", command=iit_female,
                                                 font=("Calibre", 15, "bold"),
                                                 bg="green", fg="white")
                                    bb2.place(x=50, y=310)
                                    h_b1(bb2)
                                    bb3 = Button(root, text="Back", command=edu_loan,
                                                 font=("Calibre", 15, "bold"),
                                                 bg="green", fg="white")
                                    bb3.place(x=50, y=380)
                                    h_b1(bb3)

                                def clgs():
                                    for widget in root.winfo_children():
                                        widget.destroy()
                                    Label(root, image=img3, bg="white").place(x=0, y=0)
                                    Label(root, text="Education Loan", font=("Times new Roman", 46, "bold", "underline"),
                                          bg="white", fg="green").place(x=50, y=80)
                                    Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                                          font=("times new roman", 9,), bg="white").place(x=700, y=678)
                                    date_time_display()
                                    def clgs_male():
                                        calc(9.3, 3,edu_loan)
                                    def clgs_female():
                                        calc(8.8, 3,edu_loan)
                                    bb4 = Button(root, text="Male", command=clgs_male, font=("Calibre", 15, "bold"),
                                                 bg="green",
                                                 fg="white")
                                    bb4.place(x=50, y=250)
                                    h_b1(bb4)
                                    bb5 = Button(root, text="Female or Others", command=clgs_female,
                                                 font=("Calibre", 15, "bold"),
                                                 bg="green", fg="white")
                                    bb5.place(x=50, y=310)
                                    h_b1(bb5)
                                    bb6 = Button(root, text="Back", command=edu_loan,
                                                 font=("Calibre", 15, "bold"),
                                                 bg="green", fg="white")
                                    bb6.place(x=50, y=380)
                                    h_b1(bb6)
                                bb7 = Button(root, text="IITs,IIMs,ISBs,NITs,AIIMS", command=iit,
                                             font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb7.place(x=50, y=250)
                                h_b1(bb7)
                                bb8 = Button(root, text="Other colleges", command=clgs, font=("Calibre", 15, "bold"),
                                             bg="green",
                                             fg="white")
                                bb8.place(x=50, y=310)
                                h_b1(bb8)
                                bb9 = Button(root, text="Back", command=loan, font=("Calibre", 15, "bold"),
                                             bg="green", fg="white")
                                bb9.place(x=50, y=380)
                                h_b1(bb9)
                            else:
                                Label(root, text="*Invalid credit score", font=("Times New Roman", 15), bg="white",
                                      fg="red").place(x=50, y=620)
                                credit_score2.set("")
                        else:
                            loan()
                    def business_loan():
                        amt3 = str(amt2.get())
                        credit_score3 = str(credit_score2.get())
                        n3 = str(n2.get())
                        if n3.isdigit() and amt3.isdigit() and credit_score3.isdigit():
                            if int(credit_score3) >= 0 and int(credit_score3) <= 850 and int(credit_score3) != 0 and int(amt3) != 0:
                                amt = int(str(amt2.get()))
                                if amt <= 100000:
                                    roi = 21.2
                                elif amt <= 500000:
                                    roi = 19
                                elif amt <= 5000000:
                                    roi = 18
                                elif amt <= 7500000:
                                    roi = 17.25
                                elif amt <= 10000000:
                                    roi = 17
                                elif amt <= 20000000:
                                    roi = 15.35
                                elif amt <= 50000000:
                                    roi = 12.3
                                else:
                                    roi = 10.3
                                calc(roi, 4,loan)
                            else:
                                Label(root, text="*Invalid credit score", font=("Times New Roman", 15), bg="white",
                                      fg="red").place(x=50, y=620)
                                credit_score2.set("")
                        else:
                            loan()
                    def personal_loan():
                        amt3 = str(amt2.get())
                        credit_score3 = str(credit_score2.get())
                        n3 = str(n2.get())
                        if n3.isdigit() and amt3.isdigit() and credit_score3.isdigit():
                            if int(credit_score3) >= 0 and int(credit_score3) <= 850 and int(credit_score3) != 0 and int(amt3) != 0:
                                credit_score = int(str(credit_score2.get()))
                                if credit_score <= 600:
                                    roi = -1
                                elif credit_score <= 750:
                                    roi = 17.5
                                elif credit_score <= 800:
                                    roi = 15.2
                                elif credit_score <= 900:
                                    roi = 13.6
                                else:
                                    roi = 12.4
                                calc(roi, 5, loan)
                            else:
                                Label(root, text="*Invalid credit score", font=("Times New Roman", 15), bg="white",
                                      fg="red").place(x=50, y=620)
                                credit_score2.set("")
                        else:
                            loan()
                    def travel_loan():
                        amt3 = str(amt2.get())
                        credit_score3 = str(credit_score2.get())
                        n3 = str(n2.get())
                        if n3.isdigit() and amt3.isdigit() and credit_score3.isdigit():
                            if int(credit_score3) >= 0 and int(credit_score3) <= 850 and int(credit_score3) != 0 and int(amt3) != 0:
                                credit_score = int(str(credit_score2.get()))
                                if credit_score < 620:
                                    roi = -1
                                elif credit_score < 640:
                                    roi = 15.736
                                elif credit_score < 660:
                                    roi = 15.19
                                elif credit_score < 680:
                                    roi = 14.76
                                elif credit_score < 700:
                                    roi = 14.546
                                elif credit_score < 760:
                                    roi = 14.369
                                else:
                                    roi = 14.174
                                calc(roi, 6,loan)
                            else:
                                Label(root, text="*Invalid credit score", font=("Times New Roman", 15), bg="white",
                                      fg="red").place(x=50, y=620)
                                credit_score2.set("")
                        else:
                            loan()
                    if a == "Vehicle Loan":
                        vehicle_loan()
                    elif a == "Home Loan":
                        home_loan()
                    elif a == "Education Loan":
                        edu_loan()
                    elif a == "Business Loan":
                        business_loan()
                    elif a == "Personal Loan":
                        personal_loan()
                    elif a == "Travel Loan":
                        travel_loan()
                def calc(roi,pic,b):
                    n = int(n2.get())
                    amt = int(amt2.get())
                    for widget in root.winfo_children():
                        widget.destroy()
                    if pic == 1:
                        Label(root, image=img1, bg="white").place(x=0, y=0)
                    elif pic == 2:
                        Label(root, image=img2, bg="white").place(x=0, y=0)
                    elif pic == 3:
                        Label(root, image=img3, bg="white").place(x=0, y=0)
                    elif pic == 4:
                        Label(root, image=img4, bg="white").place(x=0, y=0)
                    elif pic == 5:
                        Label(root, image=img5, bg="white").place(x=0, y=0)
                    else:
                        Label(root, image=img6, bg="white").place(x=0, y=0)
                    if roi != -1:
                        Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                              font=("times new roman", 9,), bg="white").place(x=700, y=678)
                        date_time_display()
                        w = Button(root, text="Back", command=b, font=("Calibre", 15, "bold"), bg="green", fg="white")
                        w.place(x=50, y=380)
                        h_b1(w)
                        if pic == 1:
                            Label(root, text="Loan Calculator", font=("Times new Roman", 46, "bold", "underline"),
                                  bg="light grey",
                                  fg="green").place(x=50, y=80)
                            monthly_amt = (amt + ((amt * n * roi) / 1200)) / n
                            x = str(monthly_amt).index(".")
                            insert = "Rate of interest :" + str(roi)
                            insert2 = "  %p.a Monthly installment : ₹ " + str(monthly_amt)[0:x + 3:]
                            Label(root, text=insert, font=("Times new Roman", 15), bg="light grey").place(x=50, y=250)
                            Label(root, text=insert2, font=("Times new Roman", 15), bg="light grey").place(x=50, y=310)
                        else:
                            Label(root, text="Loan Calculator", font=("Times new Roman", 46, "bold", "underline"), bg="white",
                                  fg="green").place(x=50, y=80)
                            monthly_amt = (amt + ((amt * n * roi) / 1200)) / n
                            x = str(monthly_amt).index(".")
                            insert = "Rate of interest :" + str(roi)
                            insert2 = "  %p.a Monthly installment : ₹ " + str(monthly_amt)[0:x + 3:]
                            Label(root, text=insert, font=("Times new Roman", 15), bg="white").place(x=50, y=250)
                            Label(root, text=insert2, font=("Times new Roman", 15), bg="white").place(x=50, y=310)
                    else:
                        Label(root, text="For any queries,send an email to trustybank1111@gmail.com",
                              font=("times new roman", 9,), bg="white").place(x=700, y=678)
                        date_time_display()
                        w = Button(root, text="Back", command=b, font=("Calibre", 15, "bold"), bg="green", fg="white")
                        w.place(x=50, y=380)
                        h_b1(w)
                        if pic == 1:
                            Label(root, text="Loan Calculator", font=("Times new Roman", 46, "bold", "underline"),
                                  bg="light grey",
                                  fg="green").place(x=50, y=80)
                            Label(root, text="Sorry you are not eligible for this loan :(",
                                  font=("Times new Roman", 15), bg="light grey").place(x=50, y=300)
                        else:
                            Label(root, text="Loan Calculator", font=("Times new Roman", 46, "bold", "underline"),
                                  bg="white",
                                  fg="green").place(x=50, y=80)
                            Label(root, text="Sorry you are not eligible for this loan :(",
                                  font=("Times new Roman", 15), bg="white").place(x=50, y=300)

                bn=Button(root, text="Enter", command=choose,font=("Calibre", 15,"bold"), bg="green",fg="white")
                bn.place(x=50, y=660)
                h_b1(bn)
                bn1 = Button(root , text="Back",command=options,font=("Calibre", 15,"bold"), bg="green",fg="white")
                bn1.place(x=121, y=660)
                h_b1(bn1)
            def transaction_history():
                global image1
                root1=Toplevel(root)
                w = image1.width()
                h = image1.height()
                root1.geometry("%dx%d" % (w, h))
                panel1 = Label(root1, image=image1)
                panel1.pack(side='top', fill='both', expand='yes')
                acc_no = str(acc_var2.get())
                f = open('transaction_history.txt', 'r')
                s = f.readlines()
                f.close()
                v = s[int(acc_no) // 100].split("$")
                v = v[1::]
                a = "1"
                insert = ""
                if len(v) > 11:
                    v = v[(len(v) - 10):]
                    for i in v:
                        insert += str(a) + ")" + i + "\n\n"
                        a = int(a) + 1
                else:
                    for i in v:
                        insert += str(a) + ")" + i + "\n\n"
                        a = int(a) + 1
                insertq = insert.rstrip('\n\n').split('\n\n')
                if insert != "":
                    xc = 50
                    yc = 20
                    for i in insertq:
                        Label(root1, text=i, bg="white", fg="dark green").place(x=xc, y=yc)
                        yc += 35
                    b1 = Button(root1, text="Back", command=options, font=("Calibre", 15, 'bold'), bg="green",fg="white")
                    b1.place(x=xc, y=yc + 10)
                    h_b1(b1)
                else:
                    for widget in root.winfo_children():
                        widget.destroy()
                    date_time_display()
                    Label(root, image=img, bg="white").place(x=0, y=0)
                    Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                    Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                    Label(root, text="No transactions done to display", bg="white", fg="dark green",font=('Times new roman', 18)).place(x=600, y=300)
                    b = Button(root, text="Back", command=options, font=("Calibre", 15, 'bold'), bg="green", fg="white")
                    b.place(x=600, y=350)
                    h_b1(b)
                    root1.mainloop()
            b=Button(root, text="    FD calculator     ", command=fd, bg="lightgrey",font=("Calibre",15),fg="black")
            b.place(x=650, y=200)
            h_b(b)
            b1=Button(root, text="    RD calculator     ", command=rd, bg="lightgrey",font=("Calibre",15),fg="black")
            b1.place(x=650, y=250)
            h_b(b1)
            b2=Button(root, text="    Check balance   ", command=check_balance, bg="lightgrey",font=("Calibre",15),fg="black")
            b2.place(x=650, y=300)
            h_b(b2)
            b3=Button(root, text="       Order DD       ", command=order_dd,  bg="lightgrey",font=("Calibre",15),fg="black")
            b3.place(x=650, y=350)
            h_b(b3)
            b4=Button(root, text="      Encash DD      ", command=encash_dd,  bg="lightgrey",font=("Calibre",15),fg="black")
            b4.place(x=650, y=400)
            h_b(b4)
            b5=Button(root, text="    Loan Calculator  ", command=loan, bg="lightgrey",font=("Calibre",15),fg="black")
            b5.place(x=650, y=450)
            h_b(b5)
            b6=Button(root, text="   Transfer money   ", command=transfer_money,  bg="lightgrey",font=("Calibre",15),fg="black")
            b6.place(x=650, y=500)
            h_b(b6)
            b7=Button(root, text="Last 10 transactions", command=transaction_history,  bg="lightgrey",font=("Calibre",15),fg="black")
            b7.place(x=650, y=550)
            h_b(b7)
            b8=Button(root, text="Logout", command=display_page,bg="green",font=("Calibre",15,'bold'),fg="white")
            b8.place(x=650, y=620)
            h_b1(b8)
        def passwordl(c):
            for widget in root.winfo_children():
                widget.destroy()
            date_time_display()
            Label(root, image=img, bg="white").place(x=0, y=0)
            Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
            Label(root, text="For any queries,send an email to trustybank1111@gmail.com", font=("times new roman", 9,),bg="white").place(x=700, y=678)
            c+=1
            Label(root,text="Enter your password",font=("Times New Roman", 19), bg="white").place(x=600,y=300)
            tip=Balloon(root)
            e8=Entry(root,textvariable=password_var2,show="*",font=("arial", 19),bg="lightyellow")
            e8.place(x=600,y=350)
            tip.bind_widget(e8,balloonmsg="You get only three chances \nto enter correct password")
            def password_check():
                acc_no_temp = acc_var2.get()
                acc_no_temp =str(acc_no_temp)
                f3 = open('bank_account.txt', 'r')
                s = f3.readlines()
                line = s[(int(acc_no_temp )// 100)].strip()
                linearray = line.split(" ")
                password_temp1 = linearray[6]
                password_temp = password_var2.get()
                password_temp = str(password_temp)
                if password_temp == password_temp1 :
                    options()
                elif c<=2:
                    password_var2.set("")
                    passwordl(c)
                    Label(root, text="*You entered incorrect password", font=("Times new roman", 15), bg="white",fg="red").place(x=600, y=450)
                    Label(root, text="Please enter correct password", font=("Times new roman", 15), bg="white",fg="red").place(x=600, y=480)
                    Label(root, text="You have 2 more chances left", font=("Times new roman", 15), bg="white",fg="red").place(x=600, y=510)
                else:
                    for widget in root.winfo_children():
                        widget.destroy()
                    date_time_display()
                    Label(root, image=img, bg="white").place(x=0, y=0)
                    Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold", "underline"), bg="white",fg="green").place(x=500, y=80)
                    Label(root, text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman", 9,), bg="white").place(x=700, y=678)
                    Label(root,text="You can't login anymore",font=("Times new roman",15),bg="White",fg="red").place(x=600,y=300)
                    b1=Button(root,text="Back",command=display_page,bg="green",font=("Calibre",15,"bold"),fg="white")
                    b1.place(x=600,y=350)
                    h_b1(b1)
            b=Button(root,text="Enter",command=password_check,bg="green",font=("Calibre",15,"bold"),fg="white")
            b.place(x=600,y=400)
            h_b1(b)
        acc_no_temp=acc_var2.get()
        acc_no_temp=str(acc_no_temp)
        f3 = open('bank_account.txt', 'r')
        s = f3.readlines()
        f3.close()
        a = []
        for i in s:
            x = i.split(" ")
            a.append(x[0])
        if acc_no_temp in a:
            b=0
            passwordl(b)
        else:
            Label(root,text="*Invalid account number", font=("Times New Roman", 15), bg="white",fg="red").place(x=600,y=350)
            acc_var2.set("")
    Label(root, image=img, bg="white").place(x=0, y=0)
    Label(root, text="TRUSTY BANK", font=("Times new Roman", 46, "bold","underline"), bg="white", fg="green").place(x=500, y=80)
    acc_var2 = StringVar()
    Label(root, text="Enter your account number", font=("Times New Roman", 19), bg="white").place(x=600,y=200)
    e7 = Entry(root, textvariable=acc_var2, font=("arial", 19),bg="lightyellow")
    e7.place(x=600,y=250)
    date_time_display()
    b=Button(root, text="Login", command=login, font=("Calibre", 15, 'bold'), bg="green",fg="white")
    b.place(x=600, y=300)
    h_b1(b)
    Label(root, text="If you don't have an account sign up", font=("Times new roman", 15), bg="white").place(x=600,y=400)
    Label(root,text="For any queries,send an email to trustybank1111@gmail.com",font=("times new roman",9,),bg="white").place(x=700,y=678)
    b1=Button(root, text="Sign up", command=sign_up, font=("Calibre", 15, "bold"), bg="green",fg="white")
    b1.place(x=600, y=430)
    h_b1(b1)
display_page()
root.configure(bg="white")
root.mainloop()