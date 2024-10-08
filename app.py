
from tkinter import  *
from tkinter import  ttk #Combobox widget is created using the ttk.Combobox class from the tkinter.ttk module.
from googletrans import Translator, LANGUAGES 

#function for translate the data ans store in variable
def change(text="Type",src="English",dest="English"):
    text1 = text
    src1 = src
    dest1 = dest

    trans = Translator()
    trans1 = trans.translate(text,src=src1, dest=dest1)
    return trans1.text

#function for get the data
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = sor_txt.get(1.0,END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)



#To create a main window Tk used
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='cyan')

#for the label at the top 
lab_txt = Label(root, text="Translator", font=("Time New Roman",30,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame =Frame(root).pack(side=BOTTOM)


lab_txt = Label(root, text="Source Text", font=("Time New Roman",15,"bold"),fg="black",bg="cyan")
lab_txt.place(x=100,y=100,height=20,width=300)
  
#for creating text box
sor_txt = Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,values=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("English")

button_change = Button(frame,text="Translate",relief=RAISED,command=data) #relief=RAISED gives some  3d effict 
button_change.place(x=170,y=300,height=40,width=150)

comb_dest = ttk.Combobox(frame,values=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("English")

dest_txt = Label(root, text="Destination Text", font=("Time New Roman",15,"bold"),fg="black",bg="cyan")
dest_txt.place(x=100,y=360,height=20,width=300)
  
#for creating text box
dest_txt = Text(frame,font=("Time New Roman",15,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

#mainloop() is an infinite loop used to run the application.
root.mainloop()
