from p1.funcoes.adicionar_plantio import adicionar_plantio
from p1.funcoes.atualizar_cultura import atualizar_cultura
from p1.funcoes.deletar_cultura import deletar_cultura
from p1.funcoes.listar_culturas import listar_culturas

def menu():
    while True:
        print("\n========== FarmTech Solutions - Agricultura Digital ==========")
        print("1. Adicionar Cultura")
        print("2. Listar Culturas e Insumos")
        print("3. Atualizar Cultura")
        print("4. Remover Cultura")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_plantio()
        elif opcao == "2":
            listar_culturas()
        elif opcao == "3":
            atualizar_cultura()
        elif opcao == "4":
            deletar_cultura()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()

