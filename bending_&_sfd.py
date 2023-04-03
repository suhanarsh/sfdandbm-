import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

# define function to calculate shear force and bending moment
def calc_sfd_bmd():
    # take inputs from the user
    w = float(w_input.get())
    L = float(L_input.get())
    a = float(a_input.get())
    b = float(b_input.get())
    c = L - (a + b)

    # calculate reactions [Nm]
    R1 = (w * b / L) * (c + b / 2)
    R2 = (w * b / L) * (a + b / 2)

    # create a list of lengths [m]
    l = np.linspace(0, L, 100)

    # create lists and loop for each length of the beam
    X = []
    SF = []
    M = []
    for x in l:
        # calculate shear force and moment for each x until L
        if x < a:
            sf = R1
            m = R1 * x

        elif a < x < (a + b):
            sf = R1 - (w * (x - a))
            m = (R1 * x) - (w * (x - a) ** 2 / 2)

        elif x > (a + b):
            sf = -R2
            m = R2 * (L - x)
        X.append(x)
        SF.append(sf)
        M.append(m)

    # plot graphs
    plt.figure(figsize=(10, 10))

    # plot for shear force diagram
    plt.subplot(2, 1, 1)
    plt.plot(X, SF)
    plt.fill_between(X, SF, color='green', hatch='||', alpha=0.47)
    plt.title("Shear Force Diagram (SFD)")
    plt.xlabel('Length of Beam [m]')
    plt.ylabel('Shear Force [N]')
    plt.grid()

    # plot for bending moment diagram
    plt.tight_layout(pad=3.0)
    plt.subplot(2, 1, 2)
    plt.plot(X, M)
    plt.fill_between(X, M, color='yellow', hatch='\\', alpha=0.5)
    plt.title('Bending Moment Diagram (BMD)')
    plt.xlabel('Length of Beam [m]')
    plt.ylabel('Moment [Nm]')
    plt.grid()

    plt.show()

# create GUI
root = tk.Tk()
root.title('Beam Analysis')

# create input labels and boxes
w_label = tk.Label(root, text='Uniform Distributed Load (udL) [N]: ')
w_label.pack()
w_input = tk.Entry(root)
w_input.pack()

L_label = tk.Label(root, text='Length of Beam [m]: ')
L_label.pack()
L_input = tk.Entry(root)
L_input.pack()

a_label = tk.Label(root, text='Length of segment \'a\' [m]: ')
a_label.pack()
a_input = tk.Entry(root)
a_input.pack()

b_label = tk.Label(root, text='Length of segment \'b\' [m]: ')
b_label.pack()
b_input = tk.Entry(root)
b_input.pack()

# create calculate button
calc_button = tk.Button(root, text='Calculate', command=calc_sfd_bmd)
calc_button.pack()

root.mainloop()
#code by Suhana Arsh
#Aerospace Engineering student at R.V College of Engineering.
