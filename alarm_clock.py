import tkinter as tk
import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class AlarmClock:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("500x200")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Alarm Clock")

        self.frame = self.create_frame()
        self.button = self.create_buttons()

    def create_frame(self):
        frame = ctk.CTkFrame(self.window, width=480,
                             height=180, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        return frame

    def create_buttons(self):
        self.create_edit_play()

    def create_edit_play(self):
        photo = tk.PhotoImage(file=".\img\\play.png")
        button = ctk.CTkButton(self.frame, text="",
                               image=photo, border_width=2, width=10)
        button.place(relx=0.5, rely=0.5, x=-20, y=45)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
