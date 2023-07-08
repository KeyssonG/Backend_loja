#bloco de váriaveis
novo_nome = ''
nova_senha = ''
nome = ''
senha = ''
opcao_usuario = ''
departamento = ''
carrinho = ''
lista_desejos = []
deletar = ''
finalizao = ''
historico_compras = []


#loop principal do programa 
while True:
    
    while True:
        print('===== Bem vindo ao Planeta do gamer =====')
        print('1 - Criar usuário')
        print('2 - Fazer login')
        print('3 - Sair')
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            novo_nome = input('Digite o seu nome: ')
            nova_senha = input('Digite a sua senha: ')
            print('Usuário criado com sucesso!')
            continue
    
        if opcao == '2':
            nome = input('Digite o seu nome: ')
            senha = input('Digite a sua senha: ')
                
            if nome == novo_nome and senha == nova_senha:
                print('Usuário logado com sucesso!')
            
            else:
                print('Erro ao efetuar ologin, tente novamente!')
                continue
            break
    
        if opcao == "3":
            print("Login encerrado...")
            break
        
    
    
    while True:
        print("===== Menu Principal =====")
        print("1 - Exibir departamentos")
        print("2 - Exibir itens de um departamento")
        print("3 - Adicionar item a lista de desejos")
        print("4 - Remover item de uma lista de desejos")
        print("5 - Finalizar compra")
        print("6 - Exibir histórico de compras")
        print("7 - Fazer logout")
                
        opcao_usuario = input("Escolha uma opção: ")
                
        if opcao_usuario == "1":
            print("1 - Periféricos Gamers")
            print("2 - Hardware")
            print("3 - Jogos")
        
        elif opcao_usuario == "2":
            departamento = input('Selecione o departamnto: ')
            
            if departamento == "1":
                print('Teclado gamer')
                print('Mouse gamer')
                print('Headset')
        elif opcao_usuario == '3':
            carrinho = input('Insira o item que deseja: ')
            lista_desejos.append(carrinho)
            indices = range(len(lista_desejos))
            
            
 
        elif opcao_usuario == '4':
            print('=== Esses são os itens no seu carrinho ===')
            for indice in indices:
                print(indice, lista_desejos[indice])
            deletar = int(input('Digite o item que deseja remover: '))
            
            if deletar >= 0 and deletar < len(lista_desejos):
                del lista_desejos[deletar]
                print('Item removido com sucesso!')
            else:
                print('Índice inválido. Tente novamente.')
                
        elif opcao_usuario == '5':
            print('== Finalização do pedido ==')
            for indice in indices:
                print(indice, lista_desejos[indice])
            
            finalizao = input('Você deseja finalizar a compra dos itens do seu carrinho? ')
            
            if finalizao == 'Sim' or finalizao == 'sim' or finalizao == 's':
                historico_compras.append(lista_desejos)
                lista_desejos.clear
                print('Compra finalizada com sucesso!')
            elif finalizao == 'Não' or finalizao == 'nao' or finalizao == 'n':
                print('Saindo do carrinho...')
        
        elif opcao_usuario == '6':
            print('== Histórico de compras')
            print(historico_compras)
            
