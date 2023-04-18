import math as m

def Funciones(num):
    radianes = m.radians(num)

    seno = round(m.sin(radianes), 2)
    coseno = round(m.cos(radianes), 2)
    tangente = round(m.tan(radianes), 2)
    exponencial = round(m.exp(num), 2)
    logaritmo = round(m.log(num), 2)

    return f"Seno: {seno} grados, Coseno: {coseno} grados, Tangente: {tangente} grados, Exponencial: {exponencial}, Logaritmo: {logaritmo}"


    