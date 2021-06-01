# @owner pema 🔥
# file youtube_downloade.py
# initial version

#importing the module
import os
import tkinter as tk
from tkinter.ttk import *
from pytube import YouTube

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.d_video = None

    def create_widgets(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=self.master.destroy)
        self.quit.pack(side="top")

        self.textBox = tk.Text(root, height=2, width=50)
        self.textBox.grid(row=0, column=0)

        self.Download_btn = tk.Button(root, height=1, width=10, text="Download")
        self.Download_btn["command"] = self.retrieveInput
        #command=lambda: retrieve_input() >>> just means do this when i press the button
        self.Download_btn.grid(row=0, column=1)

        self.var = tk.StringVar(root)
        self.var.set("Video") # initial value
        option = tk.OptionMenu(root, self.var, "Video", "Audio",)
        option.pack(side="top")


        self.label = tk.Label(root, height=2, width=30)
        self.label.pack(side="top")
        self.progress = Progressbar(root, orient = tk.HORIZONTAL,
                                    length = 300, mode = 'determinate')
        self.progress.pack(side="bottom")


    def percent(self, tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

    def progressFunc(self, stream, chunk, bytes_remaining=None):
        # print(stream, chunk, bytes_remaining)
        size = self.d_video.filesize

        p = self.percent(bytes_remaining, size)
        # print(str(p)+'%')
        self.progress['value'] = 1-p
        root.update_idletasks()
        if p == 0:
            self.label['text'] = "Download Complete!"
            root.update_idletasks()


    def retrieveInput(self):
        inputValue = self.textBox.get("1.0","end-1c")
        print(inputValue)

        #where to save
        SAVE_PATH = os.getcwd()

        #link of the video to be downloaded
        link = inputValue
        self.label['text'] = "Downloading...."
        root.update_idletasks()
        try:
            #object creation using YouTube which was imported in the beginning
            yt = YouTube(link, on_progress_callback=self.progressFunc)
        except Exception as e:
            self.label['text'] = "Downloading error {0}".format(e)
            root.update_idletasks()
            print (e)
            print("Connection Error") #to handle exception

        #filters out all the files with "mp4" extension
        # mp4files = yt.filter('mp4')

        # yt.set_filename('GeeksforGeeks Video') #to set the name of the file
        if self.var.get() == "Video":
        #get the video with the extension and resolution passed in the get() function
            self.d_video = yt.streams.filter(progressive=True).first()
            name = yt.title + '.mp4'
        else:
            self.d_video = yt.streams.filter(only_audio=True).first()
            name = yt.title + '.mp3'
        try:
            #downloading the video
            self.d_video.download(SAVE_PATH, filename=name)
        except Exception as e:
            print("Some Error!", e)
            self.label['text'] = "Downloading error {0}".format(e)
            root.update_idletasks()

        print('download Completed!')

root = tk.Tk()
root.title('YouTube downloader')
root.geometry("500x200") #You want the size of the app to be 500x500
app = Application(master=root)
app.mainloop()
