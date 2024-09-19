todas_pecas=[]
def cadPecas():
    import os
    print('Cadastro de peças: \n')
    while True:
        try:
            nome=str(input('Peça/Acessório: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
        
    while True:
        try:
            quantidade=int(input('Quantidade: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
    
    while True:
        try: 
            esp=str(input('Especificações: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
    os.system('cls')
    print('\n',nome,'\n',quantidade,'Unidade(s)\n''Especificações: ',esp)

todos_car=[]
def cadVeiculo():
    import os
    while True:
        try:
            marca=str(input('Marca: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
    while True:
        try:
            nome_car=str(input('Veículo: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
    while True:
        try:
            cor=str(input('Cor: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')    
    
    while True:
        try:
            ano=int(input('Ano de fabricação: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
    
    
    while True:
        try: 
            placa=str(input('Placa: '))
            break
        except ValueError:
            print('Tipo de dado inserido inválido ')
        

    os.system('cls')
    # print('Veículo: {} {}\nCor: {}\nAno: {}\nPlaca: {}'.format(marca,nome_car,cor,ano,placa))
    
    uni_car={
        "marca": marca,
        "nome": nome_car,
        "ano_de_fabricação": ano,
        "placa": placa
    }
    
    
    todos_car.append(uni_car)



def show_car():
    import os
    nome_escolhido=input('Qual veículo acessar? \nNome: ')
    os.system('cls')
    try:
        print('Carro acessado: ')
        for i in range(len(todos_car)):
            chassi = todos_car[i]
            nome_car = chassi["nome"]
              
            if nome_escolhido == nome_car:
                print('Marca: ',chassi["marca"])
                print('Nome:' ,chassi["nome"])
                print('Ano:' ,chassi["ano_de_fabricação"])
                print('Placa:' ,chassi['placa'])
    except:
        print('Veículo não encontrado. ')    



cad_todos=[]
def cadPessoa():
    
    contatos_lista={()}
    import os
    erro_msg='Tipo de dado inserido inválido '
    
    while True:
        try:
            nome=str(input('Nome: '))
            break
        except ValueError:
            print(erro_msg)
        
    while True:
        try:
            idade=int(input('Idade: '))
            break
        except ValueError:
            print(erro_msg)
    
    while True:
            
            cpf=(input('CPF: '))
            if (cpf.isdigit()) and (len(cpf)==11):
                break
            else:
                print('Digite um CPF válido ')
        
    while True:
        
        tel=(input('Telefone: '))
        if (tel.isdigit()) and (len(tel)>=8):
            
            contatos_lista={(nome,tel)}
            contato=dict(contatos_lista)
            break
        else:
            print('Digite um telefone válido ')
    print('Nome: {}\nIdade: {}\nCPF: {}\nTelefone: {}'.format(nome,idade,cpf,tel))
    print('Cadastro realizado com sucesso. ')
    

    os.system('cls')
    
    
    cad_pessoal={
        "nome": nome,
        "idade": idade,
        "telefone": tel,
        "cpf": cpf 
    }
    
    
    cad_todos.append(cad_pessoal)


def show_Cadastro():
    import os
    
    nome_escolhido=input('Qual cadastro acessar? \nNome: ')
    os.system('cls')
    try:
            while True:
                try:
                    for i in range(len(cad_todos)):
                        pessoa = cad_todos[i]
                        nome = pessoa["nome"]
                            
                        if nome_escolhido == nome:
                            print('Nome:' ,pessoa["nome"])
                            print('Idade:' ,pessoa["idade"])
                            print('CPF:' ,pessoa['cpf'])
                            print('Telefone: ',pessoa["telefone"])
                    break
                except:
                    print('Cadastro não encontrado. ')
                    break   
    except:
        print('Cadastro não encontrado. ')

def excluir_Cadastro():
    import os
    excluir_nome=input('Qual cadastro deseja excluir? \nNome: ')
    for i in range(len(cad_todos)):
        
        pessoa = cad_todos[i]
        nome = pessoa["nome"]
        if excluir_nome == nome:
            del (pessoa["nome"])
            del (pessoa["idade"])
            del (pessoa['cpf'])
            del (pessoa["telefone"])
    os.system('cls')
    print('Cadastro excluído com sucesso. ')


def excluir_Veiculo():
    import os
    excluir_nome=input('Qual cadastro de veículo deseja excluir? \nNome: ')
    
    os.system('cls')
    
    for i in range(len(todos_car)):
        chassi = todos_car[i]
        nome_car = chassi["nome"]
            
        if excluir_nome == nome_car:
            del (chassi["marca"])
            del (chassi["nome"])
            del (chassi["ano_de_fabricação"])
            del (chassi['placa'])
    print('Cadastro de veículo excluído com sucesso. ')