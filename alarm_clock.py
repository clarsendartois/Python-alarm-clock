import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

frame_fg_bg_color = "#323232"


class AlarmClock:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("500x200")
        self.window.resizable(0, 0)
        self.window.title("CLARSEN: Alarm Clock")

        self.main_frame = self.create_main_frame()

    def create_main_frame(self):
        main_fram = ctk.CTkFrame(
            self.window, bg_color=frame_fg_bg_color, fg_color=frame_fg_bg_color)
        main_fram.pack()
        return main_fram

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    alarm_clock = AlarmClock()
    alarm_clock.run()
