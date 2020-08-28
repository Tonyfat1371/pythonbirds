class Pessoa:
     olhos = 2

     def __init__(self, *filhos, nome=None, idade=49):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
     def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    toninho = Pessoa(nome='Toninho')
    jose = Pessoa(toninho, nome='José')
    print(Pessoa.cumprimentar(jose))
    print(id(jose))
    print(jose.cumprimentar())
    print(jose.nome)
    print(jose.idade)
    for filho in jose.filhos:
        print(filho.nome)
    jose.sobrenome = 'Jerônimo Silva'
    del jose.filhos
    jose.olhos = 1
    del jose.olhos
    print(toninho.__dict__)
    print(jose.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(jose.olhos)
    print(toninho.olhos)
    print(id(Pessoa.olhos), id(jose.olhos), id(toninho.olhos))



