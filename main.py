from agencia import Agencia
from carro_combustao import CarroCombustao
from carro_hibrido import CarroHibrido
from carro_eletrico import CarroEletrico
from cliente import Cliente
from dados import carros_disponiveis


boole_carros_usados = Agencia("Boole Carros Usados")

# Adiciona alguns carros a agência para ter com o que trabalhar
for carros_disponivel in carros_disponiveis:
    boole_carros_usados.adiciona_carro(carros_disponivel)

while True:
    print("\nOpções Boole Carros Usados:")
    print("1. Adicionar carro")
    print("2. Listar carros")
    print("3. Vender carro")
    print("4. Histórico de transações")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            print("Adicionar carro")
            print("\nOpções:")
            print("1. Carro a combustão")
            print("2. Carro Híbrido")
            print("3. Carro Elétrico")

            tipo_carro = input("Escolha uma opção: ")

            placa: str = input("Placa: ").upper()
            modelo: str = input("Modelo: ").capitalize() 
            marca: str = input("Marca: ").capitalize()
            tipo_carroceria: str = input("Tipo de carroceria: ")
            ano: int = int(input("Ano: "))
            cor: str = input("Cor: ")
            preco: float = float(input("Preço: ")) 
            quilometragem: int = int(input("Quilometragem: "))

            if tipo_carro == "1":
                tipo_combustivel: str = input("Tipo combutível: ")
                carro_combustao = CarroCombustao(
                    placa,
                    modelo,
                    marca,
                    tipo_carroceria,
                    ano,
                    cor,
                    tipo_combustivel,
                    preco,
                    quilometragem
                )
                boole_carros_usados.adiciona_carro(carro_combustao)

            elif tipo_carro == "2":
                tipo_combustivel_2: str = input("Tipo combutível: ")
                capacidade_bateria: float = float(input("Capacidade da bateria: "))
                carro_hibrido = CarroHibrido(
                    placa,
                    modelo,
                    marca,
                    tipo_carroceria,
                    ano,
                    cor,
                    tipo_combustivel_2,
                    preco,
                    quilometragem,
                    capacidade_bateria
                )
                boole_carros_usados.adiciona_carro(carro_hibrido)

            elif tipo_carro == "3":
                capacidade_bateria_2: float = float(input("Capaciade da bateria: "))
                carro_eletrico = CarroEletrico(
                    placa,
                    modelo,
                    marca,
                    tipo_carroceria,
                    ano,
                    cor,
                    preco,
                    quilometragem,
                    capacidade_bateria_2
                )
                boole_carros_usados.adiciona_carro(carro_eletrico)

            elif tipo_carro == "4":
                break
            else:
                print("Opção inválida. Tente novamente.")

    elif opcao == "2":
        print("\n")
        boole_carros_usados.exibi_carros()

    elif opcao == "3":
        while True:
            print("\nVenda de carro")
            print("Informe a placa do carro que será vendido ou digite 0 para cancelar.")
            placa_carro = input("Placa: ").upper()
            
            carro_venda = None

            for carro in boole_carros_usados._carros:
                if carro.placa == placa_carro:
                    carro_venda = carro
            
            if carro_venda:
                while placa_carro:
                    carro_venda.exibir_detalhes()
                    print("\nConfirmar veículo?")
                    print("1. Sim")
                    print("2. Não")
                    carro_confirmado = input("Escolha uma opção: ")

                    if carro_confirmado == "1":
                        print("\nInforme os dados do cliente: ")
                        nome_cliente = input("Nome: ")
                        endereco_cliente = input("Endereco: ")
                        telefone_cliente = input("Telefone: ")

                        cliente = Cliente(nome_cliente, endereco_cliente, telefone_cliente)

                        while True:
                            print("\nConfirmar venda?")
                            print("1. Sim")
                            print("2. Não")
                            venda_confirmada = input("Escolha uma opção: ")

                            if venda_confirmada == "1":
                                boole_carros_usados.vende_carro(carro_venda, cliente)
                                print("A venda foi realizada com sucesso!")
                                del carro_venda
                                placa_carro = ""
                                break
                            elif venda_confirmada ==  "2":
                                print("Venda cancelada")
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                        
                    elif carro_confirmado == "2":
                        print("Seleção de carro cancelada")
                        break

                    else:
                        print("Opção inválida. Tente novamente.")

            else:
                print("Retornando a página inicial")
                break                

    elif opcao == "4":
        print("\n")
        boole_carros_usados.exibi_transacoes()

    elif opcao == "5":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")