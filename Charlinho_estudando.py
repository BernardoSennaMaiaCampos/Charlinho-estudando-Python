class Livro:
    def __init__(self, nome, peso, categoria):
        self.nome = nome
        self.peso = peso
        self.categoria = categoria

    def __str__(self):
        return f"{self.nome} (Peso: {self.peso})"


class RotinaEstudos:
    def __init__(self):
        self.livros = []
        self.exatas = []
        self.humanas = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        if livro.categoria == 'Exatas':
            self.exatas.append(livro)
        elif livro.categoria == 'Humanas':
            self.humanas.append(livro)

    def estudar_exatas_primeiro(self):
        print("Estudando disciplinas de Exatas primeiro:")
        for livro in sorted(self.exatas, key=lambda x: x.peso, reverse=True):
            print(livro)

    def estudar_humanas_primeiro(self):
        print("\nEstudando disciplinas de Humanas primeiro:")
        for livro in sorted(self.humanas, key=lambda x: x.peso, reverse=True):
            print(livro)

    def estudar_intercalado(self):
        print("\nEstudando de forma intercalada:")
        exatas_sorted = sorted(self.exatas, key=lambda x: x.peso, reverse=True)
        humanas_sorted = sorted(self.humanas, key=lambda x: x.peso, reverse=True)
        
        max_len = max(len(exatas_sorted), len(humanas_sorted))
        for i in range(max_len):
            if i < len(exatas_sorted):
                print(exatas_sorted[i])
            if i < len(humanas_sorted):
                print(humanas_sorted[i])
    
    


livros = [
    Livro("Portugues", 10, 'Humanas'),
    Livro("Matematica", 9, 'Exatas'),
    Livro("Fisica", 8, 'Exatas'),
    Livro("Quimica", 7, 'Exatas'),
    Livro("Biologia", 6, 'Exatas'),
    Livro("Historia", 5, 'Humanas'),
    Livro("Geografia", 4, 'Humanas'),
    Livro("Ingles", 3, 'Humanas'),
    Livro("Filosofia", 2, 'Humanas'),
    Livro("Sociologia", 1, 'Humanas')
]


rotina = RotinaEstudos()


for livro in livros:
    rotina.adicionar_livro(livro)


rotina.estudar_exatas_primeiro()
rotina.estudar_humanas_primeiro()


rotina.estudar_intercalado()

