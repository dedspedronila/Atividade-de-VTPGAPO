agenda = []

def inserir():
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()
    
    # Cria um dicionário com os dados e adiciona na lista
    contato = {"nome": nome, "telefone": telefone, "email": email}
    agenda.append(contato)
    
    print(f"\nContato '{nome}' adicionado com sucesso!\n")

def buscar():
    nome = input("Digite o nome para buscar: ").strip()
    encontrado = False
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            print(f"\nContato encontrado: {contato}\n")
            encontrado = True
            break
    if not encontrado:
        print("\nContato não encontrado.\n")

def deletar():
    nome = input("Digite o nome para deletar: ").strip()
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            print(f"\nContato '{nome}' deletado com sucesso!\n")
            return
    print("\nContato não encontrado.\n")

def listar():
    if not agenda:
        print("\nAgenda vazia.\n")
        return
    print("\n--- Lista de Contatos ---")
    for i, contato in enumerate(agenda, 1):
        print(f"{i}. Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")
    print()

def menu():
    while True:
        print("=== AGENDA ===")
        print("1 - Inserir contato")
        print("2 - Buscar contato")
        print("3 - Deletar contato")
        print("4 - Listar contatos")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            inserir()
        elif opcao == '2':
            buscar()
        elif opcao == '3':
            deletar()
        elif opcao == '4':
            listar()
        elif opcao == '5':
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

# Executa o menu
menu()
