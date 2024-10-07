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
        self.livros_por_categoria = {"Exatas": [], "Humanas": []}

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        self.livros_por_categoria[livro.categoria].append(livro)

    def ordenar_por_peso_exatas(self):
        return sorted(self.livros_por_categoria["Exatas"], key=lambda x: x.peso, reverse=True)

    def ordenar_por_peso_humanas(self):
        return sorted(self.livros_por_categoria["Humanas"], key=lambda x: x.peso, reverse=True)

    def estudar_exatas_primeiro(self):
        print("Estudando disciplinas de Exatas primeiro:")
        for livro in self.ordenar_por_peso_exatas():
            print(livro)

    def estudar_humanas_primeiro(self):
        print("\nEstudando disciplinas de Humanas primeiro:")
        for livro in self.ordenar_por_peso_humanas():
            print(livro)

    def estudar_intercalado(self):
        print("\nEstudando de forma intercalada:")
        exatas_ordenadas = self.ordenar_por_peso_exatas()
        humanas_ordenadas = self.ordenar_por_peso_humanas()
        for livro_exatas, livro_humanas in zip(exatas_ordenadas, humanas_ordenadas):
            print(livro_exatas)
            print(livro_humanas)

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
