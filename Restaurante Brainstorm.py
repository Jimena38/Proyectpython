from tkinter import *
import psycopg2
import random
import time
from tkinter import filedialog,messagebox

def salidaPrincipal():
    ventana.destroy()

Title = ("arial black", 25)
Subtitle = ("Cambria", 12)

ventana = Tk()
ventana.geometry("800x700")
ventana.title("RESTAURANTE")
ventana.config(bg="#FF9933")

marcoPrincipal = Frame(ventana, bd="10", relief=RIDGE, bg="#FF9933")
marcoPrincipal.pack(side=TOP)

tituloPrincipal = Label(marcoPrincipal, text="Restaurante BrainStorm", font=Title, fg="#202020", bg="#FF9933")
tituloPrincipal.pack()

subPrincipal = Label(marcoPrincipal, bd=5, text="BIENVENIDOS", font=Subtitle, fg="#202020", bg="#FF9933")
subPrincipal.pack()

#Diesño de ventana primer ventana secundaria
def ventanaReserva():
    ventana_reserva = Toplevel()
    ventana_reserva.title("Datos en PostgreSQL")
    ventana_reserva.geometry("600x600")
    ventana_reserva.config(bg="#202020")
    main_title = Label(ventana_reserva, text="Registro para reserva",
                       font=Subtitle, bg="#FF9933",
                       fg="white")
    main_title.pack()

    def guardar_nueva_reserva(nombre, cantidad, contacto):
        #print(nombre) #print(cantidad) #print(contacto)
        conn = psycopg2.connpect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='postgres')
        cursor = conn.cursor()
        query = '''INSERT INTO reservas(nombre, cantidad, contacto) VALUES (%s, %s, %s)'''
        cursor.execute(query, (nombre, cantidad, contacto))
        print("Datos guardados")
        conn.commit()
        conn.close()
            
        entry_nombre.delete(0, END)
        entry_cantidad.delete(0, END)
        entry_contacto.delete(0, END)
        #mostrar_reservas()


    def mostrar_reservas():
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='postgres')
        cursor = conn.cursor()
        query = '''SELECT * FROM reservas'''
        cursor.execute(query)

        row = cursor.fetchall()

        listbox = Listbox(frame, width=30, height=5)
        listbox.grid(row=12, columnspan=4, sticky=W+E)

        for x in row:
            listbox.insert(END, x)

        print(row)

        conn.commit()
        conn.close()

    def buscar(id):
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='reservaciones')
        cursor = conn.cursor()
        query = '''SELECT * FROM reservas WHERE id=%s'''
        cursor.execute(query, (id))

        row = cursor.fetchone()

        messagebox.showinfo("Informacion", message=row)
        print(row)

        conn.commit()
        conn.close()

        id_buscar.delete(0, END)

    def mostrar():
        mostrar_reservas()

    def eliminar(id):
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='Admin',
            database='reservaciones')
        cursor = conn.cursor()
        query = '''DELETE FROM reservas WHERE id={} RETURNING *'''.format(id)
        cursor.execute(query, (id))

        var = cursor.fetchone()

        messagebox.showinfo("Informacion", message=var)
        print(var)

        conn.commit()
        conn.close()

        id_eliminar.delete(0, END)

##########################################################
#Perte 3 Giunta Pilar
# Definimos los Valores de la comida 
        t_asado = int(textAsado.get()) 
        t_milanesa = int(textMilanesa.get())
        t_pure = int(textPure.get())
        t_ensalada = int(textEnsalada.get())
        t_papas = int(textPapas.get())
        t_pollo = int(textPollo.get())
        t_pastas = int(textPastas.get())
        t_arroz = int(textArroz.get())
        t_pizza = int(textPizza.get())
        varcostocomida = (t_asado * 1000) + (t_milanesa * 700) + (t_pure * 500) + (t_ensalada * 750) + (t_papas * 1500) + (t_pollo * 800) + (t_pastas * 1100) + (t_arroz * 600) + (t_pizza * 1500)
        entryCostoComida.config(state=NORMAL)
        entryCostoComida.delete(0, END)
        entryCostoComida.insert(0, varcostocomida)
        entryCostoComida.config(state=DISABLED)

        #Valores: Bebidas
        t_pepsi = int(textPepsi.get())
        t_coca = int(textCocaCola.get())
        t_fanta = int(textFanta.get())
        t_sprite = int(textSprite.get())
        t_aguaS = int(textAguaS.get())
        t_agua = int(textAgua.get())
        t_andes = int(textAndes.get())
        t_quilmes = int(textQuilmes.get())
        t_vino = int(textVino.get())
        varcostobebidas = (t_pepsi * 600) + (t_coca * 600) + (t_fanta * 600) + (t_sprite * 600) + (t_aguaS * 500) + (
                    t_agua * 500) + (t_andes * 800) + (t_quilmes * 800) + (t_vino * 800)
        entryCostoBebidas.config(state=NORMAL)
        entryCostoBebidas.delete(0, END)
        entryCostoBebidas.insert(0, varcostobebidas)
        entryCostoBebidas.config(state=DISABLED)

        total = varcostocomida + varcostobebidas
        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    #Funcion: activar y desactivar checkbutton
    def asado(): 
        if var1.get() == 1:
            textAsado.config(state=NORMAL)
            textAsado.delete(0, END)
            textAsado.focus()
        else: #desabilitado para escribir
            textAsado.config(state=DISABLED)
            txtAsado.set("0")

    def milanesa():
        if var2.get() == 1:
            textMilanesa.config(state=NORMAL)
            textMilanesa.delete(0, END)
            textMilanesa.focus()
        else:
            textMilanesa.config(state=DISABLED)
            txtMilanesa.set("0")

    def pure():
        if var3.get() == 1:
            textPure.config(state=NORMAL)
            textPure.delete(0, END)
            textPure.focus()
        else:
            textPure.config(state=DISABLED)
            txtPure.set("0")

    def ensalada():
        if var4.get() == 1:
            textEnsalada.config(state=NORMAL)
            textEnsalada.delete(0, END)
            textEnsalada.focus()
        else:
            textEnsalada.config(state=DISABLED)
            txtEnsalada.set("0")

    def papas():
        if var5.get() == 1:
            textPapas.config(state=NORMAL)
            textPapas.delete(0, END)
            textPapas.focus()
        else:
            textPapas.config(state=DISABLED)
            txtPapas.set("0")
#########################################################################
