import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

import numpy as np
# load the trained model to classify sign
from keras.models import load_model

model = load_model('test1.h5')

# dictionary to label all traffic signs class.
classes = {1: 'Speed limit (20km/h)',
           2: 'Speed limit (30km/h)',
           3: 'Speed limit (50km/h)',
           4: 'Speed limit (60km/h)',
           5: 'Speed limit (70km/h)',
           6: 'Speed limit (80km/h)',
           7: 'End of speed limit (80km/h)',
           8: 'Speed limit (100km/h)',
           9: 'Speed limit (120km/h)',
           10: 'No passing',
           11: 'No passing veh over 3.5 tons',
           12: 'Right-of-way at intersection',
           13: 'Priority road',
           14: 'Yield',
           15: 'Stop',
           16: 'No vehicles',
           17: 'Veh > 3.5 tons prohibited',
           18: 'No entry',
           19: 'General caution',
           20: 'Dangerous curve left',
           21: 'Dangerous curve right',
           22: 'Double curve',
           23: 'Bumpy road',
           24: 'Slippery road',
           25: 'Road narrows on the right',
           26: 'Road work',
           27: 'Traffic signals',
           28: 'Pedestrians',
           29: 'Children crossing',
           30: 'Bicycles crossing',
           31: 'Beware of ice/snow',
           32: 'Wild animals crossing',
           33: 'End speed + passing limits',
           34: 'Turn right ahead',
           35: 'Turn left ahead',
           36: 'Ahead only',
           37: 'Go straight or right',
           38: 'Go straight or left',
           39: 'Keep right',
           40: 'Keep left',
           41: 'Roundabout mandatory',
           42: 'End of no passing',
           43: 'End no passing veh > 3.5 tons'}

# initialise GUI
top = tk.Tk()
top.geometry('640x480')
top.title('Traffic sign classification')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)
# define_image
bg = PhotoImage(file="stamp-2338306_640.png")

# create a canvas
my_canvas = Canvas(top, width=640, height=480)
my_canvas.pack(fill="both", expand=True)

# set image in canvas
my_canvas.create_image(0, 0, image=bg, anchor="nw")


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = np.expand_dims(image, axis=0)
    image = np.array(image)
    print(image.shape)
    pred = np.argmax(model.predict([image]), axis=1)
    sign = classes[pred[0] + 1]
    print(sign)
    my_canvas.delete("some_tag")
    my_canvas.create_text(320,150, text=sign, font=('arial', 20, 'bold'),tag="some_tag")


def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path))
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b_window = my_canvas.create_window(10, 5, anchor="n", window=classify_b)
    classify_b.place(relx=0.79, rely=0.46)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        my_image = my_canvas.create_image(320, 240, anchor="center", image=im)

        sign_image.configure(image=im)
        sign_image.image = im

        show_classify_button(file_path)
    except:
        pass


upload = Button(top, text="Upload an image", command=upload_image)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload_window=my_canvas.create_window(320,350, anchor="center",window=upload)





#sign_image.pack(side=BOTTOM, expand=True)
#label.pack(side=BOTTOM, expand=True)
my_canvas.create_text(250,50, text="Know Your Traffic Sign", font=('arial', 20, 'bold'))
top.mainloop()
