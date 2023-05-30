import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Ujjwal's Jukebox")
        self.window.geometry("500x500")

        self.current_song = ""
        self.paused = False

        self.create_widgets()

    def create_widgets(self):
        self.background_image = ImageTk.PhotoImage(Image.open("U:\songs\Screenshot 2023-05-27 211733 (1).jpg"))
        self.background_label = tk.Label(self.window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.select_button = tk.Button(
            self.window,
            text="Select Song",
            command=self.select_song
        )
        self.select_button.pack(pady=10)

        self.play_button = tk.Button(
            self.window,
            text="Play",
            state=tk.DISABLED,
            command=self.play_song
        )
        self.play_button.pack(pady=5)

        self.previous_button = tk.Button(
            self.window,
            text="Previous",
            state=tk.DISABLED,
            command=self.previous_song
        )
        self.previous_button.pack(pady=5)

        self.next_button = tk.Button(
            self.window,
            text="Next",
            state=tk.DISABLED,
            command=self.next_song
        )
        self.next_button.pack(pady=5)

        self.volume_label = tk.Label(self.window, text="Volume")
        self.volume_label.pack(pady=5)

        self.volume_scale = tk.Scale(
            self.window,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            command=self.adjust_volume
        )
        self.volume_scale.set(50)
        self.volume_scale.pack(pady=5)

    def select_song(self):
        self.current_song = filedialog.askopenfilename(
            initialdir="/",
            title="Select Song",
            filetypes=(("MP3 Files", "*.mp3"),)
        )

        if self.current_song:
            self.play_button["state"] = tk.NORMAL
            self.previous_button["state"] = tk.NORMAL
            self.next_button["state"] = tk.NORMAL

    def play_song(self):
        if self.paused:
            mixer.music.unpause()
            self.paused = False
        else:
            mixer.init()  
            mixer.music.load(self.current_song)
            mixer.music.play()

    def previous_song(self):
        pass

    def next_song(self):
        pass

    def adjust_volume(self, volume):
        mixer.music.set_volume(float(volume) / 100)

if __name__ == "__main__":
    player = MusicPlayer()
    player.window.mainloop()
