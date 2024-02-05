from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():
    win = Tk()
    app = LoginPage(win)
    win.mainloop()
class LoginPage:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Resturent Managment System")

        self.title_lable = Label(self.win,text="Anup Resturent manegment System",font=('Arial',35,'bold'),bg='Pink',bd=8,relief=GROOVE)
        self.title_lable.pack(side=TOP,fill=X)

        self.main_frame=Frame(self.win,bg="Lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=350,y=200,width=650,height=400)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightpink",font=('sans-serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame=LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="Lightpink",font=('sans-serif',18))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        self.entus_lbl= Label(self.entry_frame,text="Enter Username:",bg="lightpink",font=("sans-serif",15))
        self.entus_lbl.grid(row=0,column=0)

        username=StringVar()
        Passward=StringVar()

        self.entus_ent=Entry(self.entry_frame,font=("sans-serif",13),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1)

        self.entus_lbl= Label(self.entry_frame,text="Enter Passward:",bg="lightpink",font=("sans-serif",15))
        self.entus_lbl.grid(row=1,column=0)

        self.entus_ent=Entry(self.entry_frame,font=("sans-serif",13),bd=6,textvariable=Passward,show='*')
        self.entus_ent.grid(row=1,column=1)

        def check_login():
            if username.get()=="admin" and Passward.get()=="1234":
                self.billing_btn.config(state="normal")
            else:
                messagebox.showerror("Error",f"Invalid Login!!")
        def reset():
            username.set("")
            Passward.set("")
        def billing_set():
            self.newWindow = Toplevel(self.win)
            self.app= Window2(self.newWindow)
    

        self.button_frame=LabelFrame(self.entry_frame,text="Options",font=("Arial",15),bg="lightpink",bd=6,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=550,height=80)

        self.login_btn=Button(self.button_frame,text='Login',font=("Arial",8),bg="grey79",bd=5,width=10,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=60,pady=4)

        self.billing_btn=Button(self.button_frame,text='Billing',font=("Arial",8),bg="grey79",bd=5,width=10,command=billing_set)
        self.billing_btn.grid(row=0,column=1,padx=60,pady=4)
        self.billing_btn.config(state='disabled')

        self.reset_btn=Button(self.button_frame,text='Reset',font=("Arial",8,),bg="grey79",bd=5,width=10,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=60,pady=4)

class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1080x750+0+0")
        self.win.title("Resturent Managment System")

        self.title_lable = Label(self.win,text="Anup Resturent manegment System",font=('Arial',35,'bold'),bg='Pink',bd=8,relief=GROOVE)
        self.title_lable.pack(side=TOP,fill=X)

        bill_no=random.randint(100,9999)
        bill_no_tk= IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()

        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty= StringVar()
        cone = StringVar()

        date_pr.set(datetime.now())

        total_list =[]
        self.grd_total =0


        self.entry_frame=LabelFrame(self.win,text="Entry Details",font=('Arial',15,),bg='grey79',bd=6,relief=GROOVE)
        self.entry_frame.place(x=100,y=90,width=400,height=600,)

        self.bill_no_lbl=Label(self.entry_frame,text="Bill Number",font=("Arial",12),bg="grey79")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nam=Label(self.entry_frame,text="Customer Name ",font=("Arial",12),bg="grey79")
        self.cust_nam.grid(row=1,column=0,padx=2,pady=2)

        self.cust_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=cust_nm)
        self.cust_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_con=Label(self.entry_frame,text="Customer Contact ",font=("Arial",12),bg="grey79")
        self.cust_con.grid(row=2,column=0,padx=2,pady=2)

        self.cust_con_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=cust_cot)
        self.cust_con_ent.grid(row=2,column=1,padx=2,pady=2)
        
        self.date_lbl=Label(self.entry_frame,text="Date ",font=("Arial",12),bg="grey79")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=date_pr)
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)
        self.date_ent.config(state='disabled')

        self.item_pur_lbl=Label(self.entry_frame,text="item Purchased ",font=("Arial",12),bg="grey79")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=item_pur)
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qun_lbl=Label(self.entry_frame,text="Item Quantity ",font=("Arial",12),bg="grey79")
        self.item_qun_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qun_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=item_qty)
        self.item_qun_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl=Label(self.entry_frame,text="Cost of one ",font=("Arial",12),bg="grey79")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent= Entry(self.entry_frame,bd=5,font=("Arial",12),textvariable=cone)
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)

        def default_bill():
            self.bill_txt.insert(END,"                Anup Resturant")
            self.bill_txt.insert(END,"\n            Near Post Office, Salanpur")
            self.bill_txt.insert(END,"\n              Contact- 8918300922")
            self.bill_txt.insert(END,"\n ===============================================")
            self.bill_txt.insert(END,f"\nBill Number: {bill_no_tk.get()}")
            
        
        def genbill():
            self.bill_txt.insert(END,f"\nCustomer name: {cust_nm.get()}")
            self.bill_txt.insert(END,f"\nCustomer Contact: {cust_cot.get()}")
            self.bill_txt.insert(END,f"\nDate  : {date_pr.get()}")
            self.bill_txt.insert(END,"\n ===============================================\n")
            self.bill_txt.insert(END,"Product Name\t\t Quantity\t   PerCost\t\t Total")
            self.bill_txt.insert(END,"\n ===============================================")

            self.add_btn.config(state='normal')
            self.total_btn.config(state='normal')
            self.save_btn.config(state='normal')


        def clear_fun():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")
        
        def total_fun():
            for item in total_list:
                self.grd_total=self.grd_total + item
            self.bill_txt.insert(END,"\n ===============================================\n")
            self.bill_txt.insert(END,f"\t\t\t      Grand Total : {self.grd_total}")
            self.bill_txt.insert(END,"\n ===============================================")
        
        def reset_fun():
            total_list.clear()
            self.grd_total=0
            self.add_btn.config(state='disabled')
            self.total_btn.config(state='disabled')
            self.save_btn.config(state='disabled')
            self.bill_txt.delete("1.0",END)
            default_bill()
        def add_fun():
            qty=int(item_qty.get())
            cones=int(cone.get())
            total= qty*cones
            total_list.append(total)
                               # (END,"\nProduct Name\t\t Quantity\t   PerCost\t\t  Total")
            self.bill_txt.insert(END,f"\n{item_pur.get()}\t\t   {item_qty.get()}\t      Rs-{cone.get()}\t\t Rs-{total}")
        def save_fun():
            user_choice=messagebox.askyesno("confrim?",f"Do you Want to save the Bill{bill_no_tk.get()}",parent=self.win)
            if user_choice > 0:
                self.bill_content =self.bill_txt.get("1.0",END)
                
                con=open(f"{sys.path[0]}/bills/"+str(bill_no_tk.get())+".txt","w")

                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success!",f"Bill{bill_no_tk.get()} has been saved!",parent=self.win)
            else:
                return
        

            

        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Options",bg='lightgrey',font=("Arial",14))
        self.button_frame.place(x=20,y=250,width=320,height=300)
        
        self.add_btn=Button(self.button_frame,bd=2,text="ADD",font=("Arial",12),width=6,height=2,command=add_fun)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.gen_btn=Button(self.button_frame,bd=2,text="Generate",font=("Arial",12),width=8,height=2,command=genbill)
        self.gen_btn.grid(row=0,column=3,padx=35,pady=2)

        self.total_btn=Button(self.button_frame,bd=2,text="Clear",font=("Arial",12),width=7,height=2,command=clear_fun)
        self.total_btn.grid(row=0,column=5,padx=2,pady=4)

        self.total_btn=Button(self.button_frame,bd=2,text="Total",font=("Arial",12),width=6,height=2,command=total_fun)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.save_btn=Button(self.button_frame,bd=2,text="Save",font=("Arial",12),width=8,height=2,command=save_fun)
        self.save_btn.grid(row=1,column=3,padx=35,pady=2)

        self.reset_btn=Button(self.button_frame,bd=2,text="Reset",font=("Arial",12),width=7,height=2,command=reset_fun)
        self.reset_btn.grid(row=1,column=5,padx=2,pady=4)

        self.add_btn.config(state='disabled')
        self.total_btn.config(state='disabled')
        self.save_btn.config(state='disabled')

        


        self.calc_frame=Frame(self.win,bd=10,background="RosyBrown1",relief=GROOVE)
        self.calc_frame.place(x=550,y=90,width=430,height=255)

        self.num_ent=Entry(self.calc_frame,bd=10,background='lightgrey',textvariable=calc_var,font=("Arial",15),width=33,justify='right')
        self.num_ent.grid(row=0,column=0,columnspan=10)

        def press_btn(event):
            text= event.widget.cget("text")
            if text =='=':
                if calc_var.get().isdigit():
                    value = int(calc_var.get())
                else:
                    try:
                        value = eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text == 'C':
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()

        self.btn7=Button(self.calc_frame,bg="lightgrey",text="7",bd=9,width=10,height=1)
        self.btn7.grid(row=1,column=0,padx=1,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8=Button(self.calc_frame,bg="lightgrey",text="8",bd=9,width=10,height=1)
        self.btn8.grid(row=1,column=1,padx=1,pady=1)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9=Button(self.calc_frame,bg="lightgrey",text="9",bd=9,width=10,height=1)
        self.btn9.grid(row=1,column=2,padx=1,pady=1)
        self.btn9.bind("<Button-1>",press_btn)

        self.btnadd=Button(self.calc_frame,bg="lightgrey",text="+",bd=9,width=10,height=1)
        self.btnadd.grid(row=1,column=3,padx=9,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn4=Button(self.calc_frame,bg="lightgrey",text="4",bd=9,width=10,height=1)
        self.btn4.grid(row=2,column=0,padx=2,pady=2)
        self.btn4.bind("<Button-1>",press_btn)

        self.btn5=Button(self.calc_frame,bg="lightgrey",text="5",bd=9,width=10,height=1)
        self.btn5.grid(row=2,column=1,padx=1,pady=1)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn6=Button(self.calc_frame,bg="lightgrey",text="6",bd=9,width=10,height=1)
        self.btn6.grid(row=2,column=2,padx=1,pady=1)
        self.btn6.bind("<Button-1>",press_btn)

        self.btnsubs=Button(self.calc_frame,bg="lightgrey",text="-",bd=9,width=10,height=1)
        self.btnsubs.grid(row=2,column=3,padx=1,pady=1)
        self.btnsubs.bind("<Button-1>",press_btn)

        
        self.btn1=Button(self.calc_frame,bg="lightgrey",text="1",bd=9,width=10,height=1)
        self.btn1.grid(row=3,column=0,padx=1,pady=1)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2=Button(self.calc_frame,bg="lightgrey",text="2",bd=9,width=10,height=1)
        self.btn2.grid(row=3,column=1,padx=1,pady=1)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3=Button(self.calc_frame,bg="lightgrey",text="3",bd=9,width=10,height=1)
        self.btn3.grid(row=3,column=2,padx=1,pady=1)
        self.btn3.bind("<Button-1>",press_btn)

        self.btn_mul=Button(self.calc_frame,bg="lightgrey",text="*",bd=9,width=10,height=1)
        self.btn_mul.grid(row=3,column=3,padx=1,pady=1)
        self.btn_mul.bind("<Button-1>",press_btn)

        self.btn0=Button(self.calc_frame,bg="lightgrey",text="0",bd=9,width=10,height=1)
        self.btn0.grid(row=4,column=0,padx=1,pady=1)
        self.btn0.bind("<Button-1>",press_btn)
    
        self.btn_dot=Button(self.calc_frame,bg="lightgrey",text=".",bd=9,width=10,height=1)
        self.btn_dot.grid(row=4,column=1,padx=1,pady=1)
        self.btn_dot.bind("<Button-1>",press_btn)

        self.btn_eql=Button(self.calc_frame,bg="lightgrey",text="=",bd=9,width=10,height=1)
        self.btn_eql.grid(row=4,column=2,padx=1,pady=1)
        self.btn_eql.bind("<Button-1>",press_btn)

        self.btndev=Button(self.calc_frame,bg="lightgrey",text="/",bd=9,width=10,height=1)
        self.btndev.grid(row=4,column=3,padx=1,pady=1)
        self.btndev.bind("<Button-1>",press_btn)

        self.bill_frame=LabelFrame(self.win,text="Bill Area",font=("Arial",15),background="cornsilk2",bd=9,relief=GROOVE)
        self.bill_frame.place(x=550,y=350,width=430,height=340)
        
        self.y_scroll=Scrollbar(self.bill_frame,orient='vertical')
        self.bill_txt=Text(self.bill_frame,bg='ivory2',yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()


        
        
if __name__== "__main__":
    main()
