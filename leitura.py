def ensinar():
    pergunta = input("Digite a pergunta: ").strip().lower()
    resposta = input("Digite a resposta: ").strip()

    with open("cerebro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{pergunta}-{resposta}\n")

    print("Bot: Aprendi algo novo!")


def conversar():
    fala = input("Você: ").strip().lower()
    encontrou = False

    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                dados = linha.strip().split("-", 1)

                if len(dados) == 2:
                    pergunta_salva, resposta_salva = dados

                    if fala == pergunta_salva:
                        print(f"Bot: {resposta_salva}")
                        encontrou = True
                        break

        if not encontrou:
            print("Bot: Não sei essa resposta ainda!")
            print("Use a opção 2 para me ensinar.")

    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio! Me ensine algo primeiro.")


def listar_conhecimento():
    try:
        with open("cerebro.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            if not linhas:
                print("Bot: Ainda não aprendi nada!")
                return

            print("\n===== MEU CONHECIMENTO =====")

            for numero, linha in enumerate(linhas, start=1):
                dados = linha.strip().split("-", 1)

                if len(dados) == 2:
                    pergunta, resposta = dados
                    print(f"\n{numero}. Pergunta: {pergunta}")
                    print(f"   Resposta: {resposta}")

    except FileNotFoundError:
        print("Bot: Meu cérebro está vazio!")


# MENU PRINCIPAL

while True:

    print("\n===== MEU CHATBOT =====")
    print("1. Conversar com o bot")
    print("2. Ensinar nova resposta")
    print("3. Lista de conhecimento")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        conversar()

    elif opcao == "2":
        ensinar()

    elif opcao == "3":
        listar_conhecimento()

    elif opcao == "4":
        print("Bot: Até logo!")
        break

    else:
        print("Opção inválida! Tente novamente.")