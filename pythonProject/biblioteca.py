class BlocoDeNotas:
    def __init__(self):
        self.notas = []  # Lista para armazenar as notas

    def adicionar_nota(self):
        nota = input("Digite a nova nota: ")
        self.notas.append(nota)
        print("Nota adicionada com sucesso!\n")

    def listar_notas(self):
        if not self.notas:
            print("Nenhuma nota cadastrada.\n")
        else:
            print("Notas salvas:")
            for i, nota in enumerate(self.notas, 1):
                print(f"{i}. {nota}")
            print()

    def remover_nota(self):
        self.listar_notas()
        if self.notas:
            try:
                indice = int(input("Digite o número da nota que deseja remover: "))
                if 1 <= indice <= len(self.notas):
                    nota_removida = self.notas.pop(indice - 1)
                    print(f"Nota '{nota_removida}' removida com sucesso!\n")
                else:
                    print("Índice inválido.\n")
            except ValueError:
                print("Por favor, digite um número válido.\n")

    def menu(self):
        while True:
            print("-------- BLOCO DE NOTAS --------")
            print("1. Listar notas")
            print("2. Adicionar nota")
            print("3. Remover nota")
            print("4. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.listar_notas()
            elif escolha == "2":
                self.adicionar_nota()
            elif escolha == "3":
                self.remover_nota()
            elif escolha == "4":
                print("Saindo do bloco de notas...")
                break
            else:
                print("Opção inválida. Tente novamente.\n")


