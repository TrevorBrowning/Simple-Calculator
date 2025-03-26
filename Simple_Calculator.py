
from tkinter import *

expression = ""
current_input = ""
just_pressed_operator = False



def handle_button_click(ch):
    global expression, current_input, just_pressed_operator
    

    match ch:
        case '=':
            try:
                result = eval(expression + current_input)
                body_display.config(text=result)
            except Exception:
                body_display.config(text='Error!')
            return
        
        case 'C':
            body_display.config(text='0')
            expression = ""
            current_input = ""
            return
            

        case ('+', '-', '*', '/'):
            expression += current_input + ch
            current_input = ""
            body_display.config(text='0')
            just_pressed_operator = True
            return
 
        case ('(', ')'):
                
                expression += ch
                body_display.config(text=ch)
                just_pressed_operator = False  

        case _:
            if just_pressed_operator:
                current_input = ch 
                just_pressed_operator = False
            else:
                current_input += ch  
            
            body_display.config(text=current_input)







def handle_key_click(event):
    key = event.char
    if event.keysym == 'Return':
        key = '='
    elif event.keysym == 'Escape':
        key = 'C'

    handle_button_click(key)









window = Tk()
window.bind('<Key>', handle_key_click)

window.grid_columnconfigure(0, weight=1)




window.geometry("400x550")
window.eval('tk::PlaceWindow . center')
window.configure(bg='lightblue')
window.title('Simple Calculator')

default_font = ('Ariel', 14)


# Calculator_Frame (Calcualtor background/border)
calculator_frame = Frame(window, padx=25, pady=25, bd=2, relief=RAISED, bg='grey')
calculator_frame.grid(pady=(15,0))

# Header Frame (Title, Display)

header_frame = Frame(calculator_frame)
header_frame.grid(row=0, column=0, pady=(5,25))

header_label = Label(calculator_frame, text='Simple Calculator', font=('Ariel', 18))
header_label.grid(row=0, column=0, sticky='nsew')

# Body Frame (Display, Buttons)

body_frame = Frame(calculator_frame)
body_frame.grid(row=1, column=0)

body_display = Label(calculator_frame, text='0', font=('Ariel', 18))
body_display.grid(row=1, column=0, columnspan=4, pady=(20,20), sticky='nsew')
for i in range(4):
    body_frame.grid_columnconfigure(i, weight=1)

body_display.config(anchor='e', padx=10)



    # Button_Frame (Number/Operation Buttons)
button_frame = Frame(calculator_frame, bg='lightgrey')
button_frame.grid(row=2, column=0)

buttons = [
    ['(', ')', 'C', '/'],
['7', '8', '9', '*'],
['4', '5', '6', '-'],
['1', '2', '3', '+'],
['0', '.', '=',]
]

for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        btn = Button(button_frame, text=char, font=default_font, width=5, height=2,
        command=lambda ch=char: handle_button_click(ch))
        btn.grid(row=r, column=c, padx=5, pady=5)



window.mainloop()