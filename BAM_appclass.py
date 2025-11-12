import tkinter as tk
from tkinter import filedialog, messagebox
import os
import BAM_szimbolumok as bam
from datetime import datetime

class BAMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Szimbólum Rajzoló")
        self.root.geometry("500x500")
        self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
        self.canvas.pack(pady=10)
        self.current_shape = None
        self.show_symbol_buttons()

    def show_symbol_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        tk.Button(self.root, text="Kocka", command=lambda: self.bam_draw_shape("Kocka")).pack(side="left", padx=5, pady=10)
        tk.Button(self.root, text="Szív", command=lambda: self.bam_draw_shape("Szív")).pack(side="left", padx=5, pady=10)
        tk.Button(self.root, text="Rombusz", command=lambda: self.bam_draw_shape("Rombusz")).pack(side="left", padx=5, pady=10)
        tk.Button(self.root, text="Háromszög", command=lambda: self.bam_draw_shape("HáromszÖg")).pack(side="left", padx=5, pady=10)

    def bam_draw_shape(self, shape):
        self.current_shape = shape
        self.canvas.delete("all")
        if shape == "Kocka":
            bam.kocka(self.canvas)
        elif shape == "Szív":
            bam.sziv(self.canvas)
        elif shape == "Rombusz":
            bam.rombusz(self.canvas)
        elif shape == "Háromszög":
            bam.haromszog(self.canvas)
        self.show_action_buttons()

    def show_action_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.destroy()

        tk.Button(self.root, text="Új szimbólum", command=self.show_symbol_buttons).pack(side="left", padx=5, pady=10)
        tk.Button(self.root, text="Rajz mentése", command=self.bam_save_canvas).pack(side="left", padx=5, pady=10)
        tk.Button(self.root, text="Kilépés", command=self.root.destroy).pack(side="left", padx=5, pady=10)

    def bam_save_canvas(self):
        file_name = filedialog.asksaveasfilename(
            title="Rajz mentése",
            defaultextension=".txt",
            filetypes=[
                ("Szöveg fájl", "*.txt")
            ]
        )

        if not file_name:
            return

        ext = os.path.splitext(file_name)[1].lower()

        try:

            if ext == ".txt":
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write("Szimbólum Rajzoló\n")
                    f.write(f"Mentett szimbólum: {self.current_shape}\n")
                    f.write(f"Mentés ideje: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                messagebox.showinfo("Mentve", f"Leírás elmentve ide:\n{file_name}")

            else:
                messagebox.showerror("Hiba", "Nem támogatott fájlformátum!")

        except Exception as e:
            messagebox.showerror("Hiba", f"A mentés sikertelen.\n\n{e}")