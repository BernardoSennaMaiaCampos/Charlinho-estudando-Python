import datetime

class Livro:
    def __init__(self, nome, peso, categoria, autor=None, data_publicacao=None, num_paginas=None, isbn=None):
        self.nome = nome
        self.peso = peso
        self.categoria = categoria
        self.autor = autor
        self.data_publicacao = data_publicacao
        self.num_paginas = num_paginas
        self.isbn = isbn
        self.avaliacoes = []
        self.disponibilidade = True  

    def __str__(self):
        return f"{self.nome} (Peso: {self.peso}, Categoria: {self.categoria})"

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def obter_media_avaliacoes(self):
        if self.avaliacoes:
            return sum(self.avaliacoes) / len(self.avaliacoes)
        else:
            return 0

    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print(f"Livro {self.nome} emprestado.")
        else:
            print(f"Livro {self.nome} já está emprestado.")

    def devolver(self):
        if not self.disponibilidade:
            self.disponibilidade = True
            print(f"Livro {self.nome} devolvido.")
        else:
            print(f"Livro {self.nome} já está disponível.")

class Usuario:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.livros_emprestados = []

    def adicionar_livro(self, livro):
        self.livros_emprestados.append(livro)
        livro.emprestar()

    def remover_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.devolver()

    def obter_idade(self):
        hoje = datetime.date.today()
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))
        return idade

class Biblioteca:
    def __init__(self):
        self.livros = {}  
        self.usuarios = {} 
        self.categorias = set()
        self.historico_emprestimos = []

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

    def emprestar_livro(self, usuario_nome, livro_nome):
        usuario = self.obter_usuario(usuario_nome)
        if usuario:
            livro = self.buscar_livro_por_nome(livro_nome)
            if livro:
                if livro.disponibilidade:
                    usuario.adicionar_livro(livro)
                    self.historico_emprestimos.append((usuario.nome, livro.nome, datetime.datetime.now()))
                    print(f"Livro {livro.nome} emprestado para {usuario.nome}.")
                else:
                    print(f"Livro {livro.nome} não está disponível.")
            else:
                print(f"Livro {livro_nome} não encontrado.")
        else:
            print(f"Usuário {usuario_nome} não encontrado.")

    def devolver_livro(self, usuario_nome, livro_nome):
        usuario = self.obter_usuario(usuario_nome)
        if usuario:
            livro = self.buscar_livro_por_nome(livro_nome)
            if livro:
                usuario.remover_livro(livro)
                print(f"Livro {livro.nome} devolvido por {usuario.nome}.")
            else:
                print(f"Livro {livro_nome} não encontrado.")
        else:
            print(f"Usuário {usuario_nome} não encontrado.")

    def gerar_relatorio_emprestimos(self):
        print("\nRelatório de Empréstimos:")
        for usuario, livro, data_emprestimo in self.historico_emprestimos:
            print(f"Usuário: {usuario}, Livro: {livro}, Data do Empréstimo: {data_emprestimo.strftime('%Y-%m-%d %H:%M:%S')}")


livros = [
    Livro("Portugues", 10, 'Humanas', autor='Machado de Assis', data_publicacao='1880-01-01', num_paginas=200, isbn='978-85-359-0000-0'),
    Livro("Matematica", 9, 'Exatas', autor='Euclides', data_publicacao='300 a.C.', num_paginas=300, isbn='978-85-359-0001-7'),
    Livro("Fisica", 8, 'Exatas', autor='Isaac Newton', data_publicacao='1687-01-01', num_paginas=400, isbn='978-85-359-0002-4'),
    Livro("Quimica", 7, 'Exatas', autor='Marie Curie', data_publicacao='1903-01-01', num_paginas=500, isbn='978-85-359-0003-1'),
    Livro("Biologia", 6, 'Exatas', autor='Charles Darwin', data_publicacao='1859-01-01', num_paginas=600, isbn='978-85-359-0004-8'),
    Livro("Historia", 5, 'Humanas', autor='Heródoto', data_publicacao='440 a.C.', num_paginas=700, isbn='978-85-359-0005-5'),
    Livro("Geografia", 4, 'Humanas', autor='Strabo', data_publicacao='7 a.C.', num_paginas=800, isbn='978-85-359-0006-2'),
    Livro("Ingles", 3, 'Linguagens', autor='Shakespeare', data_publicacao='1600-01-01', num_paginas=900, isbn='978-85-359-0007-9'),
    Livro("Filosofia", 2, 'Humanas', autor='Platão', data_publicacao='380 a.C.', num_paginas=1000, isbn='978-85-359-0008-6'),
    Livro("Sociologia", 1, 'Humanas', autor='Durkheim', data_publicacao='1893-01-01', num_paginas=1100, isbn='978-85-359-0009-3'),
    Livro("Algoritmos", 12, 'Ciências da Computação', autor='Donald Knuth', data_publicacao='1968-01-01', num_paginas=1200, isbn='978-85-359-0010-0')
]


biblioteca = Biblioteca()


for livro in livros:
    biblioteca.adicionar_livro(livro)


usuario1 = Usuario("João", datetime.date(1990, 1, 1))
usuario2 = Usuario("Maria", datetime.date(1985, 5, 15))


biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)


biblioteca.emprestar_livro("João", "Portugues")
biblioteca.emprestar_livro("Maria", "Historia")


biblioteca.devolver_livro("João", "Portugues")


biblioteca.gerar_relatorio_emprestimos()


biblioteca.avaliar_livro("João", "Portugues", 5)
biblioteca.avaliar_livro("João", "Portugues", 4)
biblioteca.avaliar_livro("Maria", "Historia", 3)


livro_portugues = biblioteca.buscar_livro_por_nome("Portugues")
media_avaliacoes = livro_portugues.obter_media_avaliacoes()
print(f"\nMédia das avaliações do livro {livro_portugues.nome}: {media_avaliacoes}")


print(f"\nIdade de {usuario1.nome}: {usuario1.obter_idade()} anos")
