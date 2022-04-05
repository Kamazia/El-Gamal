import tkinter
from el_Gamal import Gamal
from tkinter.font import Font

class Window:
    def __init__(self) -> None:
        self.root = tkinter.Tk()
        self.root.title("El Gamal")
        self.fontStyle = Font(size=16)
        self.root.geometry('{0}x{1}+{2}+{3}'.format(500,250,500,300))
        self.root.resizable(False,False)

        self.var_P = tkinter.Label(self.root,text = 'P =',font = self.fontStyle)
        self.var_g = tkinter.Label(self.root,text = 'g = ',font = self.fontStyle)
        self.var_S = tkinter.Label(self.root,text = 'S = ',font = self.fontStyle)

        self.value_P = tkinter.Entry(self.root,width = 10)
        self.value_g = tkinter.Entry(self.root,width = 10)

        self.lable_message = tkinter.Label(self.root,text = 'Message',font = self.fontStyle)
        self.value_message = tkinter.Text(height=1,width=44)

        self.lable_open = tkinter.Label(self.root,text = 'Open Key:',font = self.fontStyle)
        self.lable_secret = tkinter.Label(self.root,text = 'Secret Key:',font = self.fontStyle)

        self.btn_ok = tkinter.Button(self.root,text = 'Done',command = self.ok)
        self.btn_clear = tkinter.Button(self.root,text = 'Clear',command = self.clear)

        self.c = tkinter.BooleanVar()
        self.check = tkinter.Checkbutton(self.root,variable = self.c,command=self.mode)
        self.mode_1 = tkinter.Label(self.root,text = 'encrypt')
        self.mode_2 = tkinter.Label(self.root,text = 'descrypt')

        self.encryption_text = tkinter.Text(height=4,width=60)

        self.value_open = tkinter.Text(height=1,width=20)
        self.value_secret = tkinter.Text(height=1,width=20)

    def draw_widgets(self):
        self.var_P.place(x = 10,y = 10)
        self.value_P.place(x = 55,y = 16)
        self.value_P.insert(0,25951)

        self.var_g.place(x = 150, y = 8)
        self.value_g.place(x = 190,y = 16)
        self.value_g.insert(0,92)

        self.lable_message.place(x = 10, y = 55)
        self.value_message.place(x = 115, y = 62)

        self.btn_ok.place(x = 370,y = 12)
        self.btn_clear.place(x = 432,y = 12)

        self.check.place(x = 290,y = 12)
        self.mode_1.place(x = 278,y = 33)

    def run (self):
        self.draw_widgets()
        self.root.mainloop()

    def ok(self):

        if len(self.value_message.get(1.0,'end')) == 1 or len(self.value_P.get()) == 0 or len(self.value_g.get()) == 0:
            return 0

        if not self.value_P.get().isdigit() or not self.value_g.get().isdigit():
            return 0


        a = Gamal(int(self.value_P.get()),int(self.value_g.get()),self.value_message.get(1.0, 'end')[0:-1])

        #fontStyle = Font(size = 11)

        self.value_P['state'] = 'disabled'
        self.value_g['state'] = 'disabled'
        self.btn_ok['state'] = 'disabled'
        self.btn_clear['state'] = 'disabled'
        self.value_message['state'] = 'disabled'
        self.check['state'] = 'disabled'

        if self.c.get() == True:

            self.clear()

            self.decryption_text = tkinter.Text(height=7,width=60)
            self.decryption_text.place(x = 10,y = 120)
            self.decryption_text.insert(1.0,a.decryption(self.value_message.get(1.0, 'end')[0:-1],self.value_g.get()))

            self.value_P['state'] = 'normal'
            self.value_g['state'] = 'normal'
            self.btn_ok['state'] = 'normal'
            self.btn_clear['state'] = 'normal'
            self.value_message['state'] = 'normal'
            self.check['state'] = 'normal'

        else:

            self.clear()

            self.lable_open.place(x = 10,y = 101)
            self.lable_secret.place(x = 280,y = 101)

            self.value_open.insert(1.0,a.key_generation())
            self.value_open.place(x = 10,y = 140)

            self.value_secret.insert(1.0,a.x)
            self.value_secret.place(x = 285,y = 140)

            self.encryption_text.place(x = 10,y = 175)
            self.encryption_text.insert(1.0,a.encryption(a.key_generation()[0],a.convert()))

            self.value_P['state'] = 'normal'
            self.value_g['state'] = 'normal'
            self.btn_ok['state'] = 'normal'
            self.btn_clear['state'] = 'normal'
            self.value_message['state'] = 'normal'
            self.check['state'] = 'normal'

    def clear(self):
        self.value_g.delete(0,'end')
        self.value_message.delete(1.0,'end')

        try:
            self.encryption_text.delete(1.0,'end')
            self.value_open.delete(1.0,'end')
            self.value_secret.delete(1.0,'end')
            self.encryption_text.place_forget()
            self.lable_open.place_forget()
            self.lable_secret.place_forget()
            self.value_open.place_forget()
            self.value_secret.place_forget()
            self.decryption_text.delete(1.0,'end')
            self.decryption_text.place_forget()

        except:
            pass

    def mode(self):
        if self.c.get() == True:
            self.var_g.place_forget()
            self.var_S.place(x = 150, y = 8)
            self.mode_1.place_forget()
            self.mode_2.place(x = 275,y = 33)
        else:
            self.var_S.place_forget()
            self.var_g.place(x = 150, y = 8)
            self.mode_2.place_forget()
            self.mode_1.place(x = 275,y = 33)



if __name__ == '__main__':
    
    w = Window()
    w.run()