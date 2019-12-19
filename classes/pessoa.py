class Pessoa:
    nome = "Indefinido"
    idade = 0

    def __str__(self):
        return '<{}: {}>'.format(self.__class__.__name__, self.nome)

class PessoaFisica(Pessoa):
    def __init__(self, cpf):
        super().__init__()
        self.cpf = cpf

    def __str__(self):
        return '<{}: {}/{}>'.format(self.__class__.__name__, self.cpf, self.nome)

class PessoaJuridica(Pessoa):
    def __init__(self, cnpj):
        super().__init__()
        self.cnpj = cnpj

    def __str__(self):
        return '<{}: {}/{}>'.format(self.__class__.__name__, self.cnpj, self.nome)