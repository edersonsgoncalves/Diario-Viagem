class RegistroViagem:
    def __init__(self, destino:str, data_viagem,atividades:list):
        self.destino = destino
        self.data_viagem = data_viagem
        self.atividades = atividades
    
    def __str__(self):
        lista_atividades = ""
        for atividade in self.atividades:
            lista_atividades += "* " + atividade + "\n"

        return f"""
\033[1m[{self.destino}]\033[0m - {self.data_viagem}
{lista_atividades}
"""