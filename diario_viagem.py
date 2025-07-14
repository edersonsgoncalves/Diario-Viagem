class RegistroViagem:
    def __init__(self, destino:str, data_viagem):
        self.destino = destino
        self.data_viagem = data_viagem
        self.atividades = []
    
    def __str__(self):
        lista_atividades = ""
        for atividade in self.atividades:
            lista_atividades += "* " + atividade + "\n"

        return f"""
\033[1m[{self.destino}]\033[0m - {self.data_viagem}
{lista_atividades[:-2]}"""
    def adicionar_atividade(self, atividade:str):
        self.atividades.append(atividade)

    def qtd_atividades(self):
        contador = 0
        for atividade in self.atividades:
            contador += 1
        
        return f"A viagem para {self.destino} tem {contador} atividades."

paris = RegistroViagem(destino="Paris", data_viagem="15/04/2023")
paris.adicionar_atividade("Torre Eifel")
paris.adicionar_atividade("Euro Disney")
paris.adicionar_atividade("Louvre")

print (paris)
print (paris.qtd_atividades())