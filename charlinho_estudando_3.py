class Livro:
    def __init__(self, nome, peso, categoria, autor=None, data_publicacao=None, num_paginas=None):
        self.nome = nome
        self.peso = peso
        self.categoria = categoria
        self.autor = autor
        self.data_publicacao = data_publicacao
        self.num_paginas = num_paginas
        self.avaliacoes = []

    def __str__(self):
        return f"{self.nome} (Peso: {self.peso}, Categoria: {self.categoria})"

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def obter_media_avaliacoes(self):
        if self.avaliacoes:
            return sum(self.avaliacoes) / len(self.avaliacoes)
        else:
            return 0

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)

class Biblioteca:
    def __init__(self):
        self.livros = {}  
        self.usuarios = {} 
        self.categorias = set()

    def adicionar_livro(self, livro):
        self.livros.setdefault(livro.categoria, []).append(livro)
        self.categorias.add(livro.categoria)

    def adicionar_usuario(self, usuario):
        self.usuarios[usuario.nome] = usuario

    def buscar_livro_por_nome(self, nome):
        for categoria, livros in self.livros.items():
            for livro in livros:
                if livro.nome == nome:
                    return livro
        return None

    def buscar_livros_por_categoria(self, categoria):
        return self.livros.get(categoria, [])

    def ordenar_livros_por_peso(self, categoria):
        livros = self.livros.get(categoria, [])
        return sorted(livros, key=lambda x: x.peso, reverse=True)

    def ordenar_livros_por_data(self, categoria):
        livros = self.livros.get(categoria, [])
        return sorted(livros, key=lambda x: x.data_publicacao)

    def ordenar_livros_por_paginas(self, categoria):
        livros = self.livros.get(categoria, [])
        return sorted(livros, key=lambda x: x.num_paginas)

    def obter_usuario(self, nome):
        return self.usuarios.get(nome, None)

    def avaliar_livro(self, usuario_nome, livro_nome, avaliacao):
        usuario = self.obter_usuario(usuario_nome)
        if usuario:
            livro = self.buscar_livro_por_nome(livro_nome)
            if livro:
                livro.adicionar_avaliacao(avaliacao)
                print(f"Avaliação de {avaliacao} adicionada ao livro {livro.nome}")
            else:
                print(f"Livro {livro_nome} não encontrado.")
        else:
            print(f"Usuário {usuario_nome} não encontrado.")


livros = [
    Livro("Portugues", 10, 'Humanas', autor='Machado de Assis', data_publicacao='1880-01-01', num_paginas=200),
    Livro("Matematica", 9, 'Exatas', autor='Euclides', data_publicacao='300 a.C.', num_paginas=300),
    Livro("Fisica", 8, 'Exatas', autor='Isaac Newton', data_publicacao='1687-01-01', num_paginas=400),
    Livro("Quimica", 7, 'Exatas', autor='Marie Curie', data_publicacao='1903-01-01', num_paginas=500),
    Livro("Biologia", 6, 'Exatas', autor='Charles Darwin', data_publicacao='1859-01-01', num_paginas=600),
    Livro("Historia", 5, 'Humanas', autor='Heródoto', data_publicacao='440 a.C.', num_paginas=700),
    Livro("Geografia", 4, 'Humanas', autor='Strabo', data_publicacao='7 a.C.', num_paginas=800),
    Livro("Ingles", 3, 'Linguagens', autor='Shakespeare', data_publicacao='1600-01-01', num_paginas=900),
    Livro("Filosofia", 2, 'Humanas', autor='Platão', data_publicacao='380 a.C.', num_paginas=1000),
    Livro("Sociologia", 1, 'Humanas', autor='Durkheim', data_publicacao='1893-01-01', num_paginas=1100),
    Livro("Algoritmos", 12, 'Ciências da Computação', autor='Donald Knuth', data_publicacao='1968-01-01', num_paginas=1200)
]


biblioteca = Biblioteca()


for livro in livros:
    biblioteca.adicionar_livro(livro)


usuario1 = Usuario("João")
usuario2 = Usuario("Maria")


biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)


usuario1.adicionar_livro(biblioteca.buscar_livro_por_nome("Portugues"))
usuario1.adicionar_livro(biblioteca.buscar_livro_por_nome("Matematica"))
usuario2.adicionar_livro(biblioteca.buscar_livro_por_nome("Historia"))
usuario2.adicionar_livro(biblioteca.buscar_livro_por_nome("Geografia"))


livros_exatas = biblioteca.buscar_livros_por_categoria('Exatas')
print("Livros de Exatas:")
for livro in livros_exatas:
    print(livro)


livros_humanas_ordenados_por_peso = biblioteca.ordenar_livros_por_peso('Humanas')
print("\nLivros de Humanas ordenados por peso:")
for livro in livros_humanas_ordenados_por_peso:
    print(livro)


livros_exatas_ordenados_por_data = biblioteca.ordenar_livros_por_data('Exatas')
print("\nLivros de Exatas ordenados por data de publicação:")
for livro in livros_exatas_ordenados_por_data:
    print(livro)


livros_linguagens_ordenados_por_paginas = biblioteca.ordenar_livros_por_paginas('Linguagens')
print("\nLivros de Linguagens ordenados por número de páginas:")
for livro in livros_linguagens_ordenados_por_paginas:
    print(livro)


biblioteca.avaliar_livro("João", "Portugues", 5)
biblioteca.avaliar_livro("João", "Portugues", 4)
biblioteca.avaliar_livro("Maria", "Historia", 3)


livro_portugues = biblioteca.buscar_livro_por_nome("Portugues")
media_avaliacoes = livro_portugues.obter_media_avaliacoes()
print(f"\nMédia das avaliações do livro {livro_portugues.nome}: {media_avaliacoes}")
