import time
import pyperclip
import tkinter as tk
from googletrans import Translator

def start_translate(result_label):
    recent_text = pyperclip.paste()
    result_text = translator.translate(recent_text, dest='zh-tw').text
    result_label.configure(text=result_text, justify='left', font=("Helvetica",11), wraplength=380) 

if __name__ == "__main__":
    translator = Translator()
    
    window = tk.Tk()
    window.title('Instant Translation')
    window.geometry('300x200')
    window.wm_attributes('-topmost',1)

    frame_top = tk.Frame(window)
    frame_top.pack()
    frame_bottom = tk.Frame(window)
    frame_bottom.pack(side=tk.BOTTOM)

    label_trans = tk.Label(frame_top, text='Translation')
    label_trans.pack()

    btn_start = tk.Button(frame_bottom, text='開始翻譯', command=lambda: start_translate(label_trans))
    btn_start.pack(side=tk.BOTTOM)

    window.mainloop()
    

    
    