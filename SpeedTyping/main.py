import threading
import time
import tkinter as tk
from tkinter.constants import DISABLED, INSERT, NORMAL
import random
# from typing import Text


characters_numb = 0
trigger = True
sec = 0
paragraphs = []
selected_para = ''
def readFile():
    global paragraphs
    with open('paragraphs.txt' , 'r') as file:
        paragraphs = file.readlines()

def timer(timer_label):
    global sec, trigger
    min = 0
    isec = 0
    while trigger:
        time.sleep(1)
        sec+=1
        isec +=1
        if isec%60==0:
            min +=1
            isec =0
        timer_label.config(text=f'{min}:{isec}')

def startTyping(timer_label,text_area,start_button,user_text_area):
    global trigger, characters_numb
    trigger = True
    start_button.config(state= DISABLED)
    user_text_area.config(state=NORMAL)
    user_text_area.delete("1.0", "end")
    characters_numb = len(text_area.get("1.0","end-1c"))
    if characters_numb > 0:
        th1 = threading.Thread(target=timer, args= (timer_label,))
        th1.start()
        

def speedCalculation(output_label,user_text_area,start_button):
    global sec, trigger, selected_para
    start_button.config(state=NORMAL)
    user_text_area.config(state=DISABLED)
    correct_words  = 0
    trigger = False
    min_percent = sec /60
    characters = user_text_area.get("1.0", "end-1c")
    words_entered = characters.split(' ')
    para_words = selected_para.split(' ')
    number_of_words = len(words_entered)
    for w in words_entered:
        if w in para_words:
            correct_words+=1
    characters_numb = len(characters)
    accuracy = (correct_words/number_of_words)*100
    accuracy = round(accuracy,1)
    if characters_numb > 0:
        typing_speed = (characters_numb/5)/min_percent
        output_label.config(text=f"Total Char: {characters_numb}\n{int(typing_speed)} WPM\nAccuracy: {accuracy}%")
    else:
        output_label.config(text=f"0 WPM")

def nextRound(text_area,user_text_area):
    global selected_para
    selected_para = random.choice(paragraphs)
    text_area.config(state=NORMAL)
    text_area.delete("1.0", "end")
    user_text_area.delete("1.0","end")
    text_area.insert(INSERT,selected_para)
    text_area.config(state=DISABLED)
    user_text_area.config(state=DISABLED)
    
    
# startTyping()
def main():
    global paragraphs, selected_para
    Window = tk.Tk()
    Window.title('Word Counter')
    # Window.geometry('640x500')
    Window.minsize(height=640,width=500)
    Window.config(padx=20, pady=20)
    # Text Areas
    text_area = tk.Text(width=30,height=20, font= ("Time_New_Roman"), wrap="word" )
    text_area.grid(column=0,row=0)
    selected_para = random.choice(paragraphs)
    text_area.insert(INSERT, selected_para)
    text_area.config(state=DISABLED)
    user_text_area = tk.Text(width=30,height=20, font= ("Arial"), wrap="word")
    user_text_area.grid(column=2,row=0)
    user_text_area.config(state=DISABLED)

    #Labels
    timer_label = tk.Label(text='   ', font= ("Arial", 18))
    timer_label.grid(column=1,row=0)
    output_label = tk.Label(text='', font=("Arial", 18, "bold"))
    output_label.grid(column=1,row=4,pady=5)

    #Buttons
    start_button = tk.Button(text='Start',width=10, command=lambda:startTyping(timer_label,text_area,start_button,user_text_area))
    done_button = tk.Button(text='Done',width=10,command = lambda:speedCalculation(output_label,user_text_area, start_button))
    next_button = tk.Button(text='Next', width=10, command= lambda: nextRound(text_area,user_text_area))
    start_button.grid(column=1,row=1,pady=5)
    done_button.grid(column=1,row=2,pady=5)
    next_button.grid(column=1,row=3, pady=5)




    Window.mainloop()

if __name__ == '__main__':
    readFile()
    main()
    # readFile()