import tkinter as tk
import random

random_num=random.randint(1,100)
life=7;guess=0;compare="";result=""
def num_guessing():
    global random_num,life,guess,compare,result
    # print(life,guess,random_num)
    try:
        guess+=1
        life-=1
        n=int(num_entry.get())
        if n==random_num and life!=7:
            compare="Equal"
            result="You win"
            guess=0
            life=7
            random_num=random.randint(1,100)
        elif n>random_num and life!=0:
            compare="Smaller"  
            result="Again enter"
        elif n<random_num and life!=0:
            compare="Greater"
            result="Again enter"
        elif life==0:
            compare="Not equal"
            result="You lose"
            guess=0
            life=7
            random_num=random.randint(1,100)
    except Exception as e:
        compare="Error"
        result="You need to enter the number between 1 & 100"
    life_span.config(text=str(life))
    guess_num.config(text=str(guess))
    label_compare.config(text=compare)
    label_result.config(text=result)
        
root=tk.Tk()
root.title("Number Guessing")
root.minsize(800,500)
label_guess=tk.Label(root,text="Guess:")
guess_num=tk.Label(root,text="0")
label_life=tk.Label(root,text="Life:")
life_span=tk.Label(root,text="7")
enter_num=tk.Label(root,text="Enter number between 1 & 100")
memory_num=tk.Label(root,text="Number in the memory:")
label_compare=tk.Label(root,text="")
label_result=tk.Label(root,text="")
num_entry=tk.Entry(root)
submit_button=tk.Button(root,bg="red",fg="black",text="Submit")

label_guess.grid(row=0,column=0)
guess_num.grid(row=0,column=1)
label_life.grid(row=0,column=2)
life_span.grid(row=0,column=3)
enter_num.grid(row=1,column=1)
num_entry.grid(row=1,column=2)
memory_num.grid(row=2,column=1)
label_compare.grid(row=2,column=2)
label_result.grid(row=3,column=0)
submit_button.grid(row=3,column=3)

submit_button.config(command=num_guessing)

root.mainloop()
