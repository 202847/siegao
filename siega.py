import heapq  # Importa o módulo heapq para gerenciar a fila de prioridades

class ProntoSocorro:
    def __init__(self):
        # Inicializa a fila de espera como uma lista vazia
        self.fila = []

    def agendar(self, nome, prioridade):
        """
        Agenda um paciente na fila de atendimento com uma determinada prioridade.
        Prioridades válidas:
        - 1: Crítico
        - 2: Grave
        - 3: Leve
        """
        if prioridade in [1, 2, 3]:  # Verifica se a prioridade é válida
            heapq.heappush(self.fila, (prioridade, nome))  # Adiciona o paciente na fila com prioridade
            print(f"Paciente '{nome}' agendado com prioridade {prioridade}.")
        else:
            print("Prioridade inválida. Escolha 1 (Crítico), 2 (Grave) ou 3 (Leve).")

    def chamar(self):
        """
        Chama o próximo paciente na fila de acordo com a prioridade (1 > 2 > 3).
        Se a fila estiver vazia, exibe uma mensagem informando que não há pacientes.
        """
        if self.fila:  # Verifica se há pacientes na fila
            prioridade, nome = heapq.heappop(self.fila)  # Remove o paciente com maior prioridade
            print(f"Chamando paciente '{nome}' (prioridade {prioridade}).")
        else:
            print("Nenhum paciente na fila.")  # Fila está vazia

    def excluir_todos(self):
        """
        Remove todos os pacientes da fila de espera.
        Se a fila já estiver vazia, informa ao usuário.
        """
        if self.fila:  # Verifica se há algo na fila
            self.fila.clear()  # Limpa a fila de espera
            print("Todos os agendamentos foram excluídos.")
        else:
            print("A fila já está vazia.")  # Fila já está vazia

def mostrar_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\n=== Menu ===")
    print("1 - Agendar Atendimento")
    print("2 - Chamar Próximo Paciente")
    print("3 - Excluir Agendamentos")
    print("4 - Sair")

def tratar_opcao(opcao, pronto_socorro):
    """
    Lida com a opção escolhida pelo usuário.
    Chama os métodos correspondentes da classe ProntoSocorro.
    """
    try:
        if opcao == 1:
            # Solicita os dados do paciente e agenda o atendimento
            nome = input("Nome do paciente: ").strip()  # Nome do paciente
            prioridade = int(input("Prioridade (1-Crítico, 2-Grave, 3-Leve): "))  # Prioridade
            pronto_socorro.agendar(nome, prioridade)
        elif opcao == 2:
            # Chama o próximo paciente
            pronto_socorro.chamar()
        elif opcao == 3:
            # Exclui todos os agendamentos
            pronto_socorro.excluir_todos()
        elif opcao == 4:
            # Sai do programa
            print("Saindo... Até logo!")
            return False  # Sinaliza para encerrar o loop principal
        else:
            print("Opção inválida. Tente novamente.")  # Opção fora do menu
        return True  # Continua o loop
    except ValueError:
        # Captura entradas inválidas, como letras em vez de números
        print("Entrada inválida. Certifique-se de usar números onde solicitado.")
        return True  # Continua o loop

# Execução principal do programa
if __name__ == "__main__":
    ps = ProntoSocorro()  # Cria uma instância da classe ProntoSocorro
    continuar = True  # Variável de controle para o loop do menu

    while continuar:
        mostrar_menu()  # Exibe o menu
        try:
            # Solicita a opção do usuário e executa a ação correspondente
            opcao = int(input("Escolha uma opção: "))
            continuar = tratar_opcao(opcao, ps)  # Processa a opção escolhida
        except ValueError:
            # Captura entradas inválidas no menu
            print("Por favor, insira um número correspondente a uma das opções.")
