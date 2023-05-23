
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
import os

class SuperCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        root.geometry("844x444")
        master.title("super calculator")
        root.iconbitmap(icone)
        root.configure(background='white')
        self.master = master
        self.pack()
        self.create_widgets()


    


        label = tk.Label(root, text="desinvolvido: por joao otavio e valdemir  ")
        label.pack()

        label = tk.Label(root, text="pesquisa: leonardo, julio e ronei  ")
        label.pack()

        label = tk.Label(root, text="Para feira de ciências da escola Madre Tereza   ")
        label.pack()

        label = tk.Label(root, text="turma 202   ")
        label.pack()

    def create_widgets(self):
        # Cria o notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Cria a aba da calculadora de física
        self.calculadora_fisica = CalculadoraFisica(self.notebook)
        self.notebook.add(self.calculadora_fisica, text="Força")

        # Cria a aba da calculadora normal
        self.calculadora_normal = CalculadoraNormal(self.notebook)
        self.notebook.add(self.calculadora_normal, text="Normal")

         # Cria a aba matematica
        self.Matematica = Matematica(self.notebook)
        self.notebook.add(self.Matematica, text="ñ.primos")

         # Cria a aba 1grau
        self.pgrau = pgrau(self.notebook)
        self.notebook.add(self.pgrau, text="primeiro grau")

        # Cria a aba CalculadoraQuimica
        self.CalculadoraQuimica = CalculadoraQuimica(self.notebook)
        self.notebook.add(self.CalculadoraQuimica, text="con")


        # Cria a aba rpm
        self.CalculadoraRPM = CalculadoraRPM(self.notebook)
        self.notebook.add(self.CalculadoraRPM, text="RPM")

        # Cria a aba raiz
        self.haha= haha(self.notebook)
        self.notebook.add(self.haha, text="raiz")

         # Cria a aba mcu
        self.MCUCalculator= MCUCalculator(self.notebook)
        self.notebook.add(self.MCUCalculator, text="MCU")

        # Cria a aba tep
        self.tep= tep(self.notebook)
        self.notebook.add(self.tep, text="tep")

        # Cria a aba tep
        self.Grav= Grav(self.notebook)
        self.notebook.add(self.Grav, text="grav.uni")

        # Cria a aba tep
        self.Mas= Mas(self.notebook)
        self.notebook.add(self.Mas, text="massa")

        self.mec= mec(self.notebook)
        self.notebook.add(self.mec, text="mecânica clássica")

     

class CalculadoraFisica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Criando o campo de entrada da massa
        self.label_massa = tk.Label(self)
        self.label_massa["text"] = "Massa:"
        self.label_massa.pack(side="left")

        self.entry_massa = tk.Entry(self)
        self.entry_massa.pack(side="left")

        # Criando o campo de entrada da aceleração
        self.label_aceleracao = tk.Label(self)
        self.label_aceleracao["text"] = "Aceleração:"
        self.label_aceleracao.pack(side="left")

        self.entry_aceleracao = tk.Entry(self)
        self.entry_aceleracao.pack(side="left")

        # Botão de cálculo da força
        self.button_calcular = tk.Button(self)
        self.button_calcular["text"] = "Calcular"
        self.button_calcular["command"] = self.calcular_forca
        self.button_calcular.pack(side="left")

        # Resultado da força
        self.label_resultado = tk.Label(self)
        self.label_resultado.pack(side="left")

    def calcular_forca(self):
        massa = float(self.entry_massa.get())
        aceleracao = float(self.entry_aceleracao.get())
        forca = massa * aceleracao
        self.label_resultado["text"] = f"Força = {forca}"

class CalculadoraNormal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Criando o campo de entrada
        self.label = tk.Label(self)
        self.label["text"] = "Digite um cálculo :"
        self.label.pack(side="left")
        

        self.entry = tk.Entry(self)
        self.entry.pack(side="left")

        # Botão de cálculo
        self.button_calcular = tk.Button(self)
        self.button_calcular["text"] = "Calcular"
        self.button_calcular["command"] = self.calcular
        self.button_calcular.pack(side="left")

        # Resultado
        self.label_resultado = tk.Label(self)
        self.label_resultado.pack(side="left")

    def calcular(self):
        calculo = self.entry.get()
        resultado = eval(calculo)
        self.label_resultado["text"] = f"Resultado = {resultado}"



class Matematica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Criando os widgets
        self.label = tk.Label(self, text="Digite um número e Verifique se É Ou Não É primo:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Verificar", command=self.verificar_primo)
        self.button.pack()

        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def verificar_primo(self):
        # Obter o número a ser verificado
        numero = int(self.entry.get())

        # Verificar se o número é primo
        if numero <= 1:
            resultado_texto = f"{numero} não é primo"
        elif numero == 2:
            resultado_texto = f"{numero} é primo"
        else:
            for i in range(2, numero):
                if numero % i == 0:
                    resultado_texto = f"{numero} não é primo"
                    break
            else:
                resultado_texto = f"{numero} é primo"

        # Atualizar o resultado na interface do usuário
        self.resultado.configure(text=resultado_texto)

class Ativo(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Essa é a aba Ativo")
        self.label.pack()           

class pgrau(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_a = tk.Label(self, text="Valor de a:")
        self.label_a.pack()
        self.entry_a = tk.Entry(self)
        self.entry_a.pack()

        self.label_b = tk.Label(self, text="Valor de b:")
        self.label_b.pack()
        self.entry_b = tk.Entry(self)
        self.entry_b.pack()

        self.button_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        self.button_calcular.pack()

        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.pack()

    def calcular(self):
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())

        if a == 0 and b == 0:
            self.label_resultado.config(text="Equação indeterminada.")
        elif a == 0:
            self.label_resultado.config(text="Não é uma equação do primeiro grau.")
        else:
            x = -b / a
            self.label_resultado.config(text=f"x = {x}")


class CalculadoraQuimica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.mass_label = tk.Label(self, text="Massa do soluto:")
        self.mass_label.grid(row=0, column=0)
        self.mass_entry = tk.Entry(self, width=10)
        self.mass_entry.insert(0, "0")
        self.mass_entry.grid(row=0, column=1)
        self.mass_unit_label = tk.Label(self, text="g")
        self.mass_unit_label.grid(row=0, column=2)

        self.volume_label = tk.Label(self, text="Volume da solução:")
        self.volume_label.grid(row=1, column=0)
        self.volume_entry = tk.Entry(self, width=10)
        self.volume_entry.insert(0, "0")
        self.volume_entry.grid(row=1, column=1)
        self.volume_unit_label = tk.Label(self, text="mL")
        self.volume_unit_label.grid(row=1, column=2)

        self.calculate_button = tk.Button(self, text="Calcular", command=self.calculate_concentration)
        self.calculate_button.grid(row=2, column=0)

        self.concentration_label = tk.Label(self, text="Concentração:")
        self.concentration_label.grid(row=3, column=0)
        self.concentration_result = tk.Label(self, text="")
        self.concentration_result.grid(row=3, column=1)

    def calculate_concentration(self):
        try:
            mass = float(self.mass_entry.get())
            volume = float(self.volume_entry.get())
            concentration = mass / (volume / 1000)
            self.concentration_result.config(text="{:.3f} g/L".format(concentration))
        except ValueError:
            self.concentration_result.config(text="Erro: insira valores numéricos")

class CalculadoraRPM(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.diameter_label = tk.Label(self, text="Diâmetro (mm):")
        self.diameter_label.grid(row=0, column=0)
        self.diameter_entry = tk.Entry(self, width=10)
        self.diameter_entry.insert(0, "0")
        self.diameter_entry.grid(row=0, column=1)
        self.diameter_unit_label = tk.Label(self, text="mm")
        self.diameter_unit_label.grid(row=0, column=2)

        self.distance_label = tk.Label(self, text="Distância (mm):")
        self.distance_label.grid(row=1, column=0)
        self.distance_entry = tk.Entry(self, width=10)
        self.distance_entry.insert(0, "0")
        self.distance_entry.grid(row=1, column=1)
        self.distance_unit_label = tk.Label(self, text="mm")
        self.distance_unit_label.grid(row=1, column=2)

        self.time_label = tk.Label(self, text="Tempo (s):")
        self.time_label.grid(row=2, column=0)
        self.time_entry = tk.Entry(self, width=10)
        self.time_entry.insert(0, "0")
        self.time_entry.grid(row=2, column=1)
        self.time_unit_label = tk.Label(self, text="s")
        self.time_unit_label.grid(row=2, column=2)

        self.calculate_button = tk.Button(self, text="Calcular", command=self.calculate_rpm)
        self.calculate_button.grid(row=3, column=0)

        self.rpm_label = tk.Label(self, text="RPM:")
        self.rpm_label.grid(row=4, column=0)
        self.rpm_result = tk.Label(self, text="")
        self.rpm_result.grid(row=4, column=1)

    def calculate_rpm(self):
        try:
            diameter = float(self.diameter_entry.get())
            distance = float(self.distance_entry.get())
            time = float(self.time_entry.get())
            circumference = diameter * 3.14159
            distance_per_minute = (distance / time) * 60
            rpm = distance_per_minute / circumference
            self.rpm_result.config(text="{:.2f} RPM".format(rpm))
        except ValueError:
            self.rpm_result.config(text="Erro: insira valores numéricos")  


class haha(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Digite um número:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self)
        self.button["text"] = "Calcular raiz quadrada"
        self.button["command"] = self.calcular_raiz_quadrada
        self.button.pack()

        self.result_label = tk.Label(self)
        self.result_label.pack()

    def calcular_raiz_quadrada(self):
        try:
            numero = float(self.entry.get())
            raiz_quadrada = math.sqrt(numero)
            self.result_label.config(text=f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido.")  




class MCUCalculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Add label and entry for radius
        self.radius_label = tk.Label(self, text="Raio (m):")
        self.radius_label.pack(side="left")
        self.radius_entry = tk.Entry(self)
        self.radius_entry.pack(side="left")

        # Add label and entry for velocity
        self.velocity_label = tk.Label(self, text="Velocidade (m/s):")
        self.velocity_label.pack(side="left")
        self.velocity_entry = tk.Entry(self)
        self.velocity_entry.pack(side="left")

        # Add label and entry for time
        self.time_label = tk.Label(self, text="Tempo (s):")
        self.time_label.pack(side="left")
        self.time_entry = tk.Entry(self)
        self.time_entry.pack(side="left")

        # Add button to calculate position, velocity and acceleration
        self.calculate_button = tk.Button(self, text="calcular", command=self.calculate_mcu)
        self.calculate_button.pack(side="left")

        # Add label for position
        self.position_label = tk.Label(self, text="")
        self.position_label.pack()

        # Add label for velocity
        self.velocity_result_label = tk.Label(self, text="")
        self.velocity_result_label.pack()

        # Add label for acceleration
        self.acceleration_label = tk.Label(self, text="")
        self.acceleration_label.pack()

    def calculate_mcu(self):
        # Get values from entries
        radius = float(self.radius_entry.get())
        velocity = float(self.velocity_entry.get())
        time = float(self.time_entry.get())

        # Calculate position
        position = radius * math.cos(velocity * time / radius)
        self.position_label.configure(text="Posiçao: {:.2f} m".format(position))

        # Calculate velocity
        velocity_result = velocity
        self.velocity_result_label.configure(text="Velocidade: {:.2f} m/s".format(velocity_result))

        # Calculate acceleration
        acceleration = -velocity ** 2 / radius
        self.acceleration_label.configure(text="Aceleraçao: {:.2f} m/s^2".format(acceleration))                                


class tep(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Criando os rótulos
        lbl_forca = tk.Label(self, text="Força (N): ")
        lbl_distancia = tk.Label(self, text="Distância (m): ")
        lbl_tempo = tk.Label(self, text="Tempo (s): ")
        self.lbl_trabalho = tk.Label(self, text="Trabalho (J): ")
        self.lbl_energia = tk.Label(self, text="Energia (J): ")
        self.lbl_potencia = tk.Label(self, text="Potência (W): ")

        # Criando as entradas
        self.ent_forca = tk.Entry(self)
        self.ent_distancia = tk.Entry(self)
        self.ent_tempo = tk.Entry(self)

        # Criando o botão de calcular
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)

        # Colocando os componentes na janela
        lbl_forca.grid(row=0, column=0)
        self.ent_forca.grid(row=0, column=1)
        lbl_distancia.grid(row=1, column=0)
        self.ent_distancia.grid(row=1, column=1)
        lbl_tempo.grid(row=2, column=0)
        self.ent_tempo.grid(row=2, column=1)
        btn_calcular.grid(row=3, column=0, columnspan=2)
        self.lbl_trabalho.grid(row=4, column=0, columnspan=2)
        self.lbl_energia.grid(row=5, column=0, columnspan=2)
        self.lbl_potencia.grid(row=6, column=0, columnspan=2)

    def calcular(self):
        forca = float(self.ent_forca.get())
        distancia = float(self.ent_distancia.get())
        tempo = float(self.ent_tempo.get())

        trabalho = forca * distancia
        energia = trabalho / tempo
        potencia = energia / tempo

        # Atualizando os rótulos com os resultados
        self.lbl_trabalho["text"] = "Trabalho (J): " + str(trabalho)
        self.lbl_energia["text"] = "Potência(w): " + str(energia)
        self.lbl_potencia["text"] = "energia (J): " + str(potencia)




class Grav(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_massa1 = tk.Label(self, text="Massa 1 (kg):")
        self.lbl_massa1.grid(row=0, column=0)

        self.ent_massa1 = tk.Entry(self)
        self.ent_massa1.grid(row=0, column=1)

        self.lbl_massa2 = tk.Label(self, text="Massa 2 (kg):")
        self.lbl_massa2.grid(row=1, column=0)

        self.ent_massa2 = tk.Entry(self)
        self.ent_massa2.grid(row=1, column=1)

        self.lbl_distancia = tk.Label(self, text="Distância (m):")
        self.lbl_distancia.grid(row=2, column=0)

        self.ent_distancia = tk.Entry(self)
        self.ent_distancia.grid(row=2, column=1)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular_gravidade)
        self.btn_calcular.grid(row=3, column=0, columnspan=2)

        self.lbl_resultado = tk.Label(self, text="")
        self.lbl_resultado.grid(row=4, column=0, columnspan=2)

    def calcular_gravidade(self):
        try:
            massa1 = float(self.ent_massa1.get())
            massa2 = float(self.ent_massa2.get())
            distancia = float(self.ent_distancia.get())
            gravidade = (6.67430 * (10**-11)) * (massa1 * massa2) / (distancia ** 2)
            self.lbl_resultado.config(text=f"A gravidade é: {gravidade:.3g} N")
        except ValueError:
            self.lbl_resultado.config(text="Por favor, insira valores numéricos válidos.")  





class Mas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_formula = tk.Label(self, text="Fórmula química:")
        self.lbl_formula.grid(row=0, column=0)

        self.ent_formula = tk.Entry(self)
        self.ent_formula.grid(row=0, column=1)

        self.lbl_massa_molar = tk.Label(self, text="Massa molar (g/mol):")
        self.lbl_massa_molar.grid(row=1, column=0)

        self.ent_massa_molar = tk.Entry(self)
        self.ent_massa_molar.grid(row=1, column=1)

        self.lbl_qtde = tk.Label(self, text="Quantidade (mol):")
        self.lbl_qtde.grid(row=2, column=0)

        self.ent_qtde = tk.Entry(self)
        self.ent_qtde.grid(row=2, column=1)

        self.btn_calcular = tk.Button(self, text="Calcular", command=self.calcular_massa)
        self.btn_calcular.grid(row=3, column=0, columnspan=2)

        self.lbl_resultado = tk.Label(self, text="")
        self.lbl_resultado.grid(row=4, column=0, columnspan=2)

    def calcular_massa(self):
        try:
            formula = self.ent_formula.get()
            massa_molar = float(self.ent_massa_molar.get())
            qtde = float(self.ent_qtde.get())
            massa = qtde * massa_molar
            self.lbl_resultado.config(text=f"A massa de {formula} é: {massa:.3g} g")
        except ValueError:
            self.lbl_resultado.config(text="Por favor, insira valores numéricos válidos.")            





class mecânica_clássica(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.criar_interface()

    def criar_interface(self):
        # Adiciona a Calculadora de Física
        self.calculadora = CalculadoraFisica(self)

    def calcular(self):
        # Chama o método calcular da Calculadora de Física
        self.calculadora.calcular()

class mec(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(self, text="Calculadora de Física")
        titulo.pack()

        # Primeiro cálculo - Velocidade
        frame1 = tk.Frame(self)
        frame1.pack()

        label1 = tk.Label(frame1, text="Velocidade")
        label1.pack(side=tk.LEFT)

        self.entrada_distancia = tk.Entry(frame1)
        self.entrada_distancia.pack(side=tk.LEFT)

        tk.Label(frame1, text="m").pack(side=tk.LEFT)

        self.entrada_tempo = tk.Entry(frame1)
        self.entrada_tempo.pack(side=tk.LEFT)

        tk.Label(frame1, text="s").pack(side=tk.LEFT)

        botao1 = tk.Button(frame1, text="Calcular", command=self.calcular_velocidade)
        botao1.pack(side=tk.LEFT)

        # Segundo cálculo - Aceleração
        frame2 = tk.Frame(self)
        frame2.pack()

        label2 = tk.Label(frame2, text="Aceleração")
        label2.pack(side=tk.LEFT)

        self.entrada_velocidade_inicial = tk.Entry(frame2)
        self.entrada_velocidade_inicial.pack(side=tk.LEFT)

        tk.Label(frame2, text="m/s").pack(side=tk.LEFT)

        self.entrada_velocidade_final = tk.Entry(frame2)
        self.entrada_velocidade_final.pack(side=tk.LEFT)

        tk.Label(frame2, text="m/s").pack(side=tk.LEFT)

        self.entrada_tempo2 = tk.Entry(frame2)
        self.entrada_tempo2.pack(side=tk.LEFT)

        tk.Label(frame2, text="s").pack(side=tk.LEFT)

        botao2 = tk.Button(frame2, text="Calcular", command=self.calcular_aceleracao)
        botao2.pack(side=tk.LEFT)

        # Resultado
        self.resultado = tk.Label(self, text="")
        self.resultado.pack()

    def calcular(self):
        # Realiza os dois cálculos
        self.calcular_velocidade()
        self.calcular_aceleracao()

    def calcular_velocidade(self):
        distancia = float(self.entrada_distancia.get())
        tempo = float(self.entrada_tempo.get())
        velocidade = distancia / tempo
        self.resultado.configure(text="Velocidade: {:.2f} m/s".format(velocidade))

    def calcular_aceleracao(self):
        velocidade_inicial = float(self.entrada_velocidade_inicial.get())
        velocidade_final = float(self.entrada_velocidade_final.get())
        tempo = float(self.entrada_tempo2.get())
        aceleracao = (velocidade_final - velocidade_inicial) / tempo
        self.result


filename = "pum.ico"
for root, dirs, files in os.walk("/"):
    if filename in files:
        # Se o arquivo é encontrado, você pode usar o caminho absoluto para adicioná-lo à janela do aplicativo
        icone = os.path.join(root, filename)

        # Cria a janela do aplicativo
        

        # Define o ícone da janela
        

        # Inicia o loop principal da janela
        

        # Quando o arquivo do ícone é encontrado e a janela do aplicativo é criada, o loop de busca pode ser interrompido
        break      


root = tk.Tk()
app = SuperCalculator(master=root)
app.mainloop()
