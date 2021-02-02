import re
import time
import threading
import pyperclip
import tkinter as tk
from google_trans_new  import google_translator

def thread_it(func, *args):
    t = threading.Thread(target=func, args=args)
    t.setDaemon(True)     
    t.start()

def start_translate():
    stop_event.clear()
    btn_start['state'] = tk.DISABLED
    btn_stop['state'] = tk.ACTIVE

    recent_text = ""
    while True:
        tmp_text = pyperclip.paste()
        reReturn = re.compile(r'\r|\n|\r\n') # https://zhuanlan.zhihu.com/p/34004051
        tmp_text = re.sub(reReturn,'',tmp_text)
        if tmp_text != recent_text:
            recent_text = tmp_text
            result_text = translator.translate(recent_text, lang_src='en', lang_tgt='zh-tw')
            label_trans.configure(text=result_text, justify='left', font=("Helvetica",11), wraplength=380) 
            print(recent_text+", "+result_text)
        time.sleep(0.1)

        if stop_event.is_set():
            break

def stop_trans():
    stop_event.set()
    btn_start['state'] = tk.ACTIVE
    btn_stop['state'] = tk.DISABLED

if __name__ == "__main__":
    translator = google_translator()
    stop_event = threading.Event()

    window = tk.Tk()
    window.title('Instant Translation')
    window.geometry('300x200')
    window.wm_attributes('-topmost',1)

    frame_top = tk.Frame(window)
    frame_bottom = tk.Frame(window)
    frame_top.pack()
    frame_bottom.pack(side=tk.BOTTOM)

    label_trans = tk.Label(window, text='Press Ctrl+C to select words.')
    btn_start = tk.Button(frame_bottom, text='開始翻譯', command=lambda: thread_it(start_translate))
    btn_stop = tk.Button(frame_bottom, text="停止翻譯", command=lambda: stop_trans())
    btn_stop['state'] = tk.DISABLED

    label_trans.pack()
    btn_start.pack(side=tk.LEFT)
    btn_stop.pack(side=tk.LEFT)
    
    window.mainloop()
