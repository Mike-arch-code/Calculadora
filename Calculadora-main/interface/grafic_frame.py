import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from interface import input_bar
from mpl_toolkits.mplot3d import Axes3D
from model import operaciones
import numpy as np
varibles_y = []
varibles_x = []
varibles_z = []
legendas = []
var3d = []

def grafic(container):
    global window
    window = ttk.Frame(container, borderwidth=1, relief='solid')
    window.grid(row=0, column=0, sticky='nsew')
    window.columnconfigure(0,weight=1)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    window.rowconfigure(1,minsize=10)
    

    return window

def actualice_grafic(y,x,z):
    global varibles
    global legendas
        
    if operaciones.graficas > 0:
        if operaciones.graficas < 10:
                varibles_y.append(y)
                varibles_z.append(z)
                varibles_x.append(x)
                legendas.append(input_bar.text_bar.get())
        else:
                varibles_x.pop(0)
                varibles_z.pop(0)
                varibles_y.pop(0)
                legendas.pop(0)
                varibles_y.append(y)
                varibles_z.append(z)
                varibles_x.append(x)
                legendas.append(input_bar.text_bar.get())
    def dibujo():
        
        
        if operaciones.mode_3D >0:
            var3d.append(len(legendas))
            
            plt.close('all')
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')
            ax.set_zlabel('Eje Z')
            ax.set_xlim(-10, 10)  
            ax.set_ylim(-10, 10)
            ax.set_zlim(0, 20)  
                

            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            toolbar_frame = tk.Frame(window)
            toolbar_frame.grid(row=0, column=0, sticky='ew')
            
            
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            toolbar.pack(side=tk.TOP, fill=tk.X)
            canvas.get_tk_widget().grid(row=1, column=0, sticky='nsew')
                
            window.grid_rowconfigure(1, weight=1)
            window.grid_columnconfigure(0, weight=1)
            window.grid_columnconfigure(0, weight=1)
                
            
            frame = ttk.Frame(window)
            frame.grid(column=1,row=1,sticky="nsew")
                
            for i in range(operaciones.graficas):
                ttk.Button(frame,text=(legendas[i]),command=lambda i=i:borrar_grafica(i)).grid(column=1,row=i+1,sticky="nsew")
                ax.plot(varibles_x[i], varibles_y[i], varibles_z[i], marker='', linestyle='-', markersize=3, linewidth=1,label = legendas[i])
                ax.legend()
        else:
            plt.close('all')
            fig, ax = plt.subplots()
            
            ax.grid(True, linestyle='--', color='gray', linewidth=0.5)
            ax.axhline(0, color='black',linewidth=0.5) 
            ax.axvline(0, color='black',linewidth=0.5)  

            ax.set_xlabel('Eje X')
            ax.set_ylabel('Eje Y')
            ax.set_xlim(-10, 10)  
            ax.set_ylim(-10, 10)

            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            toolbar_frame = tk.Frame(window)
            toolbar_frame.grid(row=0, column=0, sticky='ew')
        
        
            toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
            toolbar.update()

            toolbar.pack(side=tk.TOP, fill=tk.X)
            canvas.get_tk_widget().grid(row=1, column=0, sticky='nsew')
            
            window.grid_rowconfigure(1, weight=1)
            window.grid_columnconfigure(0, weight=1)
            window.grid_columnconfigure(0, weight=1)
            
        
            frame = ttk.Frame(window)
            frame.grid(column=1,row=1,sticky="nsew")
            
            for i in range(operaciones.graficas):
                ttk.Button(frame,text=(legendas[i]),command=lambda i=i:borrar_grafica(i)).grid(column=1,row=i+1,sticky="nsew")
                ax.plot(varibles_x[i], varibles_y[i] ,label = legendas[i])
                ax.legend()

        def borrar_grafica(pos):
            
            for widget in window.winfo_children():
                widget.destroy()
            legendas.pop(pos)
            varibles_z.pop(pos)
            varibles_x.pop(pos)
            varibles_y.pop(pos)
            if (pos+1) in var3d:
                operaciones.mode_3D -= 1
            operaciones.graficas = operaciones.graficas - 1
            dibujo()
    dibujo()