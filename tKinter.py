from tkinter import *
a=(input(''))
b=(input(''))
c=(input(''))
d=(input(''))
f=(str(a+'x')+str(b+'+')+str(c+'+')+str(d))
ws=Tk()
ws.title('Python Guides')
ws.geometry(f)
Label(
    ws ,
    text='Life means lot more \n then you know',
        font=('Times',20)
).pack(fill=BOTH,expand=True)
ws.mainloop()