from interface import input_bar
from interface import grafic_frame
from model import size_window
from interface import solution_view
import numpy as np
import sympy as sp
import re
from model import size_window


vacio = False
mode_3D = 0

graficas = 0

def operaction():
    global y_values
    global x_values
    global vacio
    global graficas
    vacio = True
    global Z
    global mode_3D
    
    operation = input_bar.text_bar.get().strip()
    
    y_values = [None] * 200
    x_values = [None] * 200
    
    operation = operation.replace('e', str(np.e))  
    operation = operation.replace('π', str(np.pi))  
    operation = operation.replace('^', '**')   
    operation = operation.replace('ln', 'np.log')
    
    operation = re.sub(r'(\d)([xy])', r'\1*\2', operation)
    operation = re.sub(r'([xy])(\d)', r'\1*\2', operation)
    operation = re.sub(r'√\(([^)]+)\)', r'(\1)**(1/2)', operation)
    
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    
    try:
        expr = sp.sympify(operation)
        graficas = graficas + 1
        
    except Exception as e:
        solution_view.label.configure(text="Syntax Error")
        return
    
    x_values = np.linspace(-100, 100, 4000)
    y_values = []
    Z = np.zeros((len(x_values), 1))
    threshold = 40
    
    
    x_values = np.linspace(-20, 20, 100)
    y_values = np.linspace(-20, 20, 100)
    X, Y = np.meshgrid(x_values, y_values)
    
    if 'y' in str(expr.free_symbols):
        
        Z = np.zeros(X.shape)
        threshold = 40
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                x_valu = X[i, j]
                y_valu = Y[i, j]
                try:
                    result = expr.subs({x: x_valu, y: y_valu}).evalf()
                    if result.is_real and abs(result) <= threshold:
                        Z[i, j] = float(result)
                    else:
                        Z[i, j] = np.nan
                except Exception as e:
                    solution_view.label.configure(text="Syntax Error")
                    Z[i, j] = np.nan
        mode_3D = mode_3D + 1
        if size_window.grafic:
            grafic_frame.actualice_grafic(X, Y,Z)
        
    else:
        i = 0
        for x_val in x_values:
            try:
                result = expr.subs(x, x_val).evalf()
                if not "x" in operation:
                    formatted_num = format_float(result)
                    solution_view.label.config(text=formatted_num)
                else:
                    solution_view.label.config(text="")
                
                if result.is_real and abs(result) <= threshold:
                    y_values[i] = float(result)
                else:
                    y_values[i] = np.nan
                
            except Exception as e:
                solution_view.label.configure(text="Syntax Error")
                y_values[i] = np.nan
            i += 1
        
        Z = np.zeros_like(x_values)
        if size_window.grafic:
            grafic_frame.actualice_grafic(y_values, x_values,Z)

def format_float(num):
    formatted_str = "{:.15g}".format(num)
    if '.' in formatted_str:
        formatted_str = formatted_str.rstrip('0').rstrip('.')
    return formatted_str
