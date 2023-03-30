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

        self.main_frame = self.create_main_frame()

    def create_main_frame(self):
        main_frame = ctk.CTkFrame(
            self.window, width=480, height=180, corner_radius=10)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        return main_frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
