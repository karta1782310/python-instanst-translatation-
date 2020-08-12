import time
import threading
import pyperclip
import tkinter as tk
from googletrans import Translator

def start_translate(result_label, stop_event):
    btn_start['state'] = tk.DISABLED
    btn_stop['state'] = tk.ACTIVE
    stop_event.clear()
    recent_text = ""

    while True:
        tmp_text = pyperclip.paste()
        if tmp_text != recent_text:
            print(tmp_text)
            recent_text = tmp_text
            result_text = translator.translate(recent_text, dest='zh-tw').text
            result_label.configure(text=result_text, justify='left', font=("Helvetica",11), wraplength=380) 
        time.sleep(0.1)

        if stop_event.is_set():
            break

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)     
    t.start()

def stop_trans():
    stop_event.set()
    btn_start['state'] = tk.ACTIVE
    btn_stop['state'] = tk.DISABLED

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

    label_trans = tk.Label(window, text='Translation')
    label_trans.pack()

    stop_event = threading.Event()
    
    btn_start = tk.Button(frame_bottom, text='開始翻譯', command=lambda: thread_it(start_translate, label_trans, stop_event))
    btn_start.pack(side=tk.LEFT)

    btn_stop = tk.Button(frame_bottom, text="停止翻譯", command=lambda: stop_trans())
    btn_stop.pack(side=tk.LEFT)
    btn_stop['state'] = tk.DISABLED

    window.mainloop()
    

    
    