import tkinter as tk
from tkinter import ttk
from randomunsplash import WallpaperManager
from randomunsplash import wpaperdConfig

# Future project not functional

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.app_name = "Random Unsplash Wallpaper Utility"
        self.title = self.root.title(self.app_name)
        self.root.wait_visibility(self.root)
        self.root.attributes("-alpha", 0.7)
        self.root.configure(bg = '#181A1B')

        self.label = ttk.Label(self.root,text=self.app_name,justify="center",font=("JetBrainsMonoNL NFP SemiBold",16),background="#181A1B",foreground="#F1F1F1")
        self.label.pack(padx=50,pady=50)

        self.root.mainloop()
        
       
def main ():
    app = App()

if __name__ == "__main__":
    main()

