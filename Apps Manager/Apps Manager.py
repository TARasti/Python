from tkinter import filedialog, Text, Scrollbar
import tkinter as tk
import os

#   Variables

trigger =False
selected_apps=[]
app_name=[]
previously_clicked = None
ADDRESS=''

#   Add file Function

def Addfile(frame):
    available=False
    for widget in frame.winfo_children():
        widget.destroy()
    file=filedialog.askopenfilename(title='Select File' ,filetype=[('executable', '*.exe'),('All Files','*.*')])
    if len(selected_apps)!=0:
        for app in selected_apps:
            if app == file:
                available=True
        if available!=True:
            selected_apps.append(file)
            app_name.append(os.path.basename(file))
    else:
        selected_apps.append(file)
        app_name.append(os.path.basename(file))
    buttons(frame)


#   StartFile Function

def StartFile():
    global ADDRESS
    if ADDRESS!='':
        print(ADDRESS)
        os.startfile(ADDRESS)

#   Function for file Selection

def Selected(event):
    global trigger,ADDRESS
    global previously_clicked
    button=event.widget
    if button['bg']=='#266150':
        button.config(bg="#DCE1E3",fg='black')
        ADDRESS=''
    else:
        button.config(bg="#266150",fg='white')
        name=button["text"]
        for app in selected_apps:
            if name in app:
                ADDRESS= app
    
#   Update Frame

def buttons(frame):
    global app_name
    color='#DCE1E3'
    for name in app_name:
        button=tk.Button(frame,text=name,bg=color,font="Arial")
        button.bind("<Button-1>", Selected)
        button.pack(fill='x',padx=20,pady=2)

#   Remove Files

def Remove(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    global ADDRESS
    for f in selected_apps:
        if ADDRESS ==f:
            selected_apps.remove(ADDRESS)
            app_name.remove(os.path.basename(ADDRESS))
    buttons(frame)


def Searching(search,label):
    for widget in label.winfo_children():
        widget.destroy()
    value=search.get()
    value=value.lower()
    for v in app_name:
        if value in v.lower():
            label.config(text=v)
    

# Main

def main():
    col='#5C5F58'
    root = tk.Tk()
    root.title('App Manager')
    root.geometry('640x640')
    root.resizable(0,0)
    root.config(bg='#DDAF94')
    w1=tk.LabelFrame(root,bg=col)
    w1.pack(fill='both',expand=True,pady=10)
    canvas=tk.Canvas(w1,bg=col)
    canvas.pack(side='left',expand=True,fill='both',anchor='center')
    scrollbar=tk.Scrollbar(w1,orient='vertical',command=canvas.yview)
    scrollbar.pack(side='right',fill='y')
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    frame=tk.Frame(canvas,bg='gray')
    # frame.place(relwidth=0.9,relheight=0.9,relx=0.1,rely=0.1,)
    frame.pack(fill='both',expand=True)
    canvas.create_window((0,0),window=frame,anchor='center')


    # search
    search=tk.Entry(root,width=30)
    search.pack()
    search_button=tk.Button(root,text='Search',command= lambda : Searching(search,label))
    search_button.pack()
    label=tk.Label(root,text='Found result',width=25,height=2)
    label.pack()
    canvas.create_window((280,0),window=search)
    canvas.create_window((400,0),window=search_button)
    canvas.create_window((280,50),window=label)


    startfile=tk.Button(root,text='Run File',command=StartFile,height=2,width=30,bg=col,fg='light gray')
    startfile.pack(pady=2)
    addfile=tk.Button(root,text='Add File',command=lambda: Addfile(frame),height=2,width=30,bg=col,fg='light gray')
    addfile.pack(pady=2)
    removefile=tk.Button(root,text='Remove File', command=lambda: Remove(frame),height=2,width=30,bg=col,fg='light gray')
    removefile.pack(pady=2)
    buttons(frame)
    canvas2=tk.Canvas(root,height=10,width=640,bg='#DDAF94')
    canvas2.pack()
    root.mainloop()

    

    
if __name__ == "__main__":
    if os.path.isfile('save.txt'):
        with open('save.txt') as f:
            tempapp=f.read()
            tempapp=tempapp.split(',')
            app_name=[x for x in tempapp if x.strip()]
    if os.path.isfile('path.txt'):
        with open('path.txt') as f:
            tempapp=f.read()
            tempapp=tempapp.split(',')
            selected_apps=[x for x in tempapp if x.strip()]

    main()
    with open('save.txt','w') as f:
        for app in app_name:
            f.write(app+',')
    with open('path.txt', 'w') as f:
        for app in selected_apps:
            f.write(app+',')