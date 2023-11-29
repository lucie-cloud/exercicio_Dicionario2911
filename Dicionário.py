# Dicionário

# Sistema de Informação - Cadastrar funcionário nome,salario

# Apresentação
print('\n\t\t\t -- Sistema de Informação Cadastro de Funcionários -- \n')

# Estrutura
funcionário = {'Nome': '', 'Salário':0.0, 'Ativo':False}

# Entrada
NomedoFuncionário = input ('Nome: ')
Salário = float(input('Salário: R$ '))
StatusdoFuncionário = bool(input ('Status: Ativo  '))

# Saída
#print ("Funcionário Ativo") if Status ['Ativo'] else print ("Funcionário Inativo")
print("*** Funcionário Ativo  ***") if StatusdoFuncionário ['True'] else print ("*** Funcionário Inativo ***")
