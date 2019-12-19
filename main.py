from classes.pessoa import Pessoa, PessoaFisica, PessoaJuridica

if __name__ == '__main__':
    pessoa = PessoaFisica("000.000.000-00")
    pessoa.nome = "Diego Fincatto"
    print(pessoa)

    empresa = PessoaJuridica("000.000.000.000-00")
    #empresa.nome = "Fincattos Corp"
    print(empresa)
