from PIL import Image, ImageFont, ImageDraw
import tkinter as tk
from tkinter import filedialog, messagebox



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Watermark App")
        self.geometry("550x200")
        self.config(bg="#D3E4CD")

        self.create_widgets()

    def create_widgets(self):
        self.image_button()
        self.text_water()
        self.quit_button()
        self.text()

    def image_button(self):
        self.upload_button = tk.Button(text="Search Image", command=self.upload_image)
        self.upload_button.config(bg="#99A799", padx=10, pady=10)
        self.upload_button.grid(column=0, row=2)

    def upload_image(self):
        self.open_file = filedialog.askopenfilename(initialdir="/", title="Select A File",
                                                    filetype=[("Image Files", ".png .jfif .jpg .jpeg")])
        self.label = tk.Label(text="Image Upload")
        self.label.grid(sticky=tk.N)
        self.label.config(text=self.open_file)

        self.watermark_img()

    def quit_button(self):
        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.grid(column=1, row=2)
        self.quit_button.config(bg="#99A799", padx=5, pady=5)


    def text_water(self):
        self.text_label = tk.Label(text="What Do You Want To Write On Your Image? :", font=("Arial", 12))
        self.text_label.config(bg="#D3E4CD", padx=20, pady=50)
        self.text_label.grid(column=0, row=1)

    def text(self):
        self.text = tk.Entry(width=25, bd=5)
        self.text.grid(column=1, row=1)



    def watermark_img(self):

        text = self.text.get()

        image = self.open_file
        image = Image.open(image)

        watermark_img = image.copy()
        draw = ImageDraw.Draw(watermark_img)

        font = ImageFont.truetype("arial.ttf", 30)

        draw.text((0, 0), text=text, font=font)

        self.save_img(watermark_img)

    def saved_message(self):
        messagebox.showinfo(title="Saved", message="Saved Successfully!")


    def save_img(self, image, ):
                message = self.saved_message()
                name = self.text.get()
                try:
                    image.save(f"./{name}.jpeg")
                except OSError:
                    return print("Could Not Find File Path")
                return message








app = App()
app.mainloop()