import tkinter as tk
from BAM_appclass import BAMApp

def main():
    root = tk.Tk()
    app = BAMApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()