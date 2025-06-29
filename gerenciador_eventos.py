# Sistema de Gerenciamento de Eventos Universitários - UniFECAF
# Desenvolvido em Python para fins acadêmicos
# Funcionalidades: cadastrar, atualizar, listar, inscrever, visualizar inscritos e excluir eventos

eventos = []  # Lista para armazenar os eventos

def menu():
    print("--- MENU ---")
    print("1 - Cadastrar Evento")
    print("2 - Atualizar Evento")
    print("3 - Visualizar Eventos Disponíveis")
    print("4 - Inscrever-se em Evento")
    print("5 - Visualizar Inscritos")
    print("6 - Excluir Evento")
    print("0 - Sair")

def cadastrar_evento():
    nome = input("Nome do evento: ")
    data = input("Data do evento: ")
    descricao = input("Descrição do evento: ")
    max_participantes = int(input("Número máximo de participantes: "))
    evento = {
        "nome": nome,
        "data": data,
        "descricao": descricao,
        "max_participantes": max_participantes,
        "inscritos": []
    }
    eventos.append(evento)
    print("Evento cadastrado com sucesso!")

def atualizar_evento():
    nome = input("Digite o nome do evento a ser atualizado: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            evento["data"] = input("Nova data: ")
            evento["max_participantes"] = int(input("Novo número máximo de participantes: "))
            print("Evento atualizado com sucesso!")
            return
    print("Evento não encontrado.")

def listar_eventos():
    if not eventos:
        print("Nenhum evento disponível.")
        return
    print("\\n--- Lista de Eventos ---")
    for i, evento in enumerate(eventos):
        vagas_restantes = evento["max_participantes"] - len(evento["inscritos"])
        print(f"{i+1}. {evento['nome']} - {evento['data']}")
        print(f"   Descrição: {evento['descricao']}")
        print(f"   Vagas restantes: {vagas_restantes}")

def inscrever_evento():
    nome = input("Digite o nome do evento para inscrição: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            if len(evento["inscritos"]) < evento["max_participantes"]:
                participante = input("Digite seu nome para inscrição: ")
                if participante in evento["inscritos"]:
                    print("Você já está inscrito neste evento.")
                else:
                    evento["inscritos"].append(participante)
                    print("Inscrição realizada com sucesso!")
            else:
                print("Evento lotado!")
            return
    print("Evento não encontrado.")

def visualizar_inscritos():
    nome = input("Digite o nome do evento: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            print(f"Inscritos no evento '{evento['nome']}':")
            for inscrito in evento["inscritos"]:
                print(f" - {inscrito}")
            return
    print("Evento não encontrado.")

def excluir_evento():
    nome = input("Digite o nome do evento a ser excluído: ")
    for evento in eventos:
        if evento["nome"].lower() == nome.lower():
            eventos.remove(evento)
            print("Evento excluído com sucesso!")
            return
    print("Evento não encontrado.")

# Loop principal do sistema
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_evento()
    elif opcao == "2":
        atualizar_evento()
    elif opcao == "3":
        listar_eventos()
    elif opcao == "4":
        inscrever_evento()
    elif opcao == "5":
        visualizar_inscritos()
    elif opcao == "6":
        excluir_evento()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")