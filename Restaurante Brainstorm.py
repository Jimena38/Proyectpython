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
