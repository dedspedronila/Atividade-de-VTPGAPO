agenda = []

def inserir():
    data = input("Data do compromisso (DD/MM/2006): ").strip()
    descricao = input("Descrição do compromisso: ").strip()
    
    if not data.endswith("/2006"):
        print("\nErro: A data deve estar no ano de 2006.\n")
        return
    
    compromisso = {"data": data, "descricao": descricao}
    agenda.append(compromisso)
    print(f"\nCompromisso em {data} adicionado com sucesso!\n")

def listar():
    if not agenda:
        print("\nNenhum compromisso agendado.\n")
        return
    print("\n--- Compromissos de 2006 ---")
    for i, compromisso in enumerate(agenda, 1):
        print(f"{i}. Data: {compromisso['data']}, Descrição: {compromisso['descricao']}")
    print()

def menu():
    while True:
        print("=== AGENDA 2006 ===")
        print("1 - Inserir compromisso")
        print("2 - Listar compromissos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            inserir()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            print("\nSaindo... Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.\n")

menu()
