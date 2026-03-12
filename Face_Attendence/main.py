import os
import tkinter as tk
from tkinter import messagebox
# import face_recognition
import cv2
import os
import datetime
import subprocess
from PIL import Image,ImageTk



class App:
    def __init__(self):

        # this part is creating a main empty window
        self.main_window = tk.Tk()
        self.main_window.title("Attendence Window")
        self.main_window.geometry("1200x520+350+100")

        # lets add a main login_button
        self.main_window_login_button = tk.Button(self.main_window,text="Login",bg="green",fg="black",command=self.login,height=2,width=20,font=('Helvetica bold',20))
        self.main_window_login_button.place(x=750,y=300)

        # lets add register new user button
        self.main_window_register_new_user_button = tk.Button(self.main_window, text="Register", bg="blue", fg="black",command=self.register_new_user, height=2, width=20, font=('Helvetica bold', 20))
        self.main_window_register_new_user_button.place(x=750, y=400)

        # lets add a screen to which we will add a web cam screen
        self.web_cam_label = tk.Label(self.main_window)
        self.web_cam_label.place(x=10, y=0, width=700, height=500)
        self.add_webcam(self.web_cam_label)

        # lets create a database where registered users will stay
        self.db_dir = "./db"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

        self.log_path = "./log.txt"


    def add_webcam(self,label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)

        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret,frame = self.cap.read()

        if not ret:
            return
        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr,cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        self._label.after(20,self.process_webcam)

    def login(self):
        if not os.path.exists(".tmp"):
            os.makedirs(".tmp")
        unknown_img_path = ".tmp/dummy.jpg"
        cv2.imwrite(unknown_img_path,self.most_recent_capture_arr)
        output = subprocess.check_output(["face_recognition",self.db_dir,unknown_img_path]).decode("utf-8").strip()
        name = str(output.split(",")[1])
        name_fin = name.strip()

        if name in ['unknown_person','no_persons_found']:
            messagebox.showwarning(title="Error", message=f"{name_fin} try again")
        else:
            messagebox.showinfo(title="Success",message=f"Welcome {name_fin}")
            with open(self.log_path,'a') as f:
                f.write(f"{name},{datetime.datetime.now()}\n")

        os.remove(unknown_img_path)

    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x530+370+120")

        self.accept_register_new_window_buttom = tk.Button(self.register_new_user_window,text="Accept",bg="green",fg="black",command=self.accept_register_new_user,height=2,width=20,font=('Helvetica bold',20))
        self.accept_register_new_window_buttom.place(x=750,y=300)

        self.try_again_register_new_window_button = tk.Button(self.register_new_user_window,text="Try Again",bg="red",fg="black",command=self.reject_register_new_user,height=2,width=20,font=('Helvetica bold',20))
        self.try_again_register_new_window_button.place(x=750,y=400)

        self.capture_label = tk.Label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)
        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = tk.Text(self.register_new_user_window,height=2,width=15,font=("Arial",32))
        self.entry_text_register_new_user.place(x=750,y=150)

        self.text_label_register_new_user = tk.Label(self.register_new_user_window,text="Please input Username:")
        self.text_label_register_new_user.place(x=750,y=70)

    def add_img_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure (image = imgtk)
        self.register_new_user_capture = self.most_recent_capture_arr.copy()



    def start(self):
        self.main_window.mainloop()

    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")
        cv2.imwrite(os.path.join(self.db_dir,'{}.jpg'.format(name)),self.register_new_user_capture)
        messagebox.showinfo("Success","User was added successfully")
        self.register_new_user_window.destroy()


    def reject_register_new_user(self):
        self.register_new_user_window.destroy()


app = App()
app.start()