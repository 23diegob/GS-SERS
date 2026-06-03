import random
import time

# --- CONFIGURACOES DE LIMITES CRITICOS (Regras de Negocio) ---
LIMITE_TEMP_MAX = 80.0  # Celsius
LIMITE_BATERIA_CRITICA = 20.0  # Percentual

# --- ESTADO INICIAL DA MISSAO (Banco de dados simulado) ---
missao_status = {
    "temperatura": 76.0,
    "bateria": 21.1,
    "painel_solar_geracao": 5.0,  # kW
    "consumo_sistemas": 3.5,  # kW
    "comunicacao_terra": "EXCELENTE",
    "modulos": {
        "Suporte de Vida": "OPERACIONAL",
        "Propulsao": "OPERACIONAL",
        "Pesquisa Cientifica": "OPERACIONAL"
    }
}


def simular_ambiente():
    """
    Simula a oscilacao dos dados operacionais da missao espacial no tempo.
    """
    # Flutuacao da temperatura
    missao_status["temperatura"] += round(random.uniform(-3.0, 5.0), 1)

    # Simulacao da dinamica energetica (Geracao vs Consumo)
    missao_status["painel_solar_geracao"] = round(random.uniform(1.0, 8.0), 1)

    # O saldo energetico afeta diretamente a bateria
    saldo_energetico = missao_status["painel_solar_geracao"] - missao_status["consumo_sistemas"]
    missao_status["bateria"] += round(saldo_energetico * 1.5, 1)

    # Limitadores da bateria entre 0% e 100%
    missao_status["bateria"] = max(0.0, min(100.0, missao_status["bateria"]))

    # Oscilacao aleatoria na comunicacao
    if random.random() < 0.05:
        missao_status["comunicacao_terra"] = "INSTAVEL"
    elif random.random() < 0.02:
        missao_status["comunicacao_terra"] = "PERDIDA"
    else:
        missao_status["comunicacao_terra"] = "ESTAVEL"


def processar_alertas_e_decisoes():
    """
    Aplica IA introducao / Estruturas Logicas para gerar alertas
    e tomar decisoes automatizadas de seguranca.
    """
    print("\n--- [SISTEMA DE SEGURANCA AUTONOMO] ---")
    alertas_ativos = False

    # 1. Analise Critica de Temperatura
    if missao_status["temperatura"] >= LIMITE_TEMP_MAX:
        print(f"ALERTA CRITICO: Temperatura elevada ({missao_status['temperatura']:.1f} C)!")
        print("ACAO AUTONOMA: Ligando sistema de resfriamento de emergencia e suspendendo propulsao.")
        missao_status["modulos"]["Propulsao"] = "SUSPENSO (RESFRIAMENTO)"
        missao_status["temperatura"] -= 12.0  # Efeito da acao autonoma
        alertas_ativos = True
    else:
        # Se normalizou, volta a operar
        if missao_status["modulos"]["Propulsao"] == "SUSPENSO (RESFRIAMENTO)":
            missao_status["modulos"]["Propulsao"] = "OPERACIONAL"

    # 2. Analise Critica de Energia (Sustentabilidade)
    if missao_status["bateria"] <= LIMITE_BATERIA_CRITICA:
        print(f"ALERTA CRITICO: Bateria em nivel de emergencia ({missao_status['bateria']:.1f}%).")
        print("ACAO AUTONOMA: Protocolo de Economia de Energia Ativado. Desligando Pesquisas Cientificas.")
        missao_status["modulos"]["Pesquisa Cientifica"] = "DESLIGADO (ECONOMIA)"
        missao_status["consumo_sistemas"] = 1.5  # Reduz o consumo do sistema
        alertas_ativos = True
    else:
        # Se a bateria subiu com os paineis solares, religa os sistemas
        if missao_status["modulos"]["Pesquisa Cientifica"] == "DESLIGADO (ECONOMIA)":
            print("ACAO AUTONOMA: Energia restabelecida. Reativando modulos cientificos.")
            missao_status["modulos"]["Pesquisa Cientifica"] = "OPERACIONAL"
            missao_status["consumo_sistemas"] = 3.5

    # 3. Analise de Comunicacao
    if missao_status["comunicacao_terra"] == "PERDIDA":
        print("ALERTA: Conexao com a base terrestre perdida!")
        print("ACAO AUTONOMA: Alinhando antenas reservas em modo de varredura automatica.")
        alertas_ativos = True

    if not alertas_ativos:
        print("Todos os sistemas operando dentro dos limites de seguranca.")


def exibir_painel():
    """
    Exibe os dados formatados de maneira clara e organizada no terminal (Usabilidade).
    """
    print("\n=======================================================")
    print("      TELEMETRIA DA MISSAO ESPACIAL EXPERIMENTAL       ")
    print("=======================================================")
    # O :.1f forca o Python a mostrar apenas 1 casa decimal
    print(f"Temperatura Interna : {missao_status['temperatura']:.1f} C")
    print(f"Status de Comunicacao: {missao_status['comunicacao_terra']}")
    print(f"Capacidade da Bateria: {missao_status['bateria']:.1f}%")
    print(f"Geracao Solar        : {missao_status['painel_solar_geracao']:.1f} kW")
    print(f"Consumo Atual        : {missao_status['consumo_sistemas']:.1f} kW")
    print("-------------------------------------------------------")
    print("STATUS DOS MODULOS:")
    for modulo, status in missao_status["modulos"].items():
        print(f"  * [{modulo}]: {status}")
    print("=======================================================")


# --- LOOP PRINCIPAL DE EXECUCAO ---
def iniciar_monitoramento():
    print("Iniciando Sistema de Monitoramento da Missao...")
    time.sleep(1)

    try:
        while True:
            simular_ambiente()
            exibir_painel()
            processar_alertas_e_decisoes()

            print("\nAtualizando dados em 3 segundos... (Pressione Ctrl+C para encerrar)")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nMonitoramento encerrado pelo operador.")


if __name__ == "__main__":
    iniciar_monitoramento()