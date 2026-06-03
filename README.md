# Sistema de Telemetria e Monitoramento Espacial Autônomo

## Integrantes do Grupo

Cristhian Henrique Clementino - RM: 574117

Diego de Oliveira Brandão - RM: 569773


## Descrição do Projeto
Este projeto constitui a entrega oficial da Global Solution 2026 para a disciplina de Soluções em Energias Renováveis e Sustentáveis, desenvolvido por alunos da turma 1CCPW.

O software consiste em um sistema computacional inteligente projetado para receber, interpretar e exibir dados simulados de telemetria de uma missão aeroespacial experimental. O núcleo da aplicação foca na gestão da sustentabilidade e eficiência energética da nave, aplicando estruturas lógicas para a tomada de decisões e respostas automatizadas de segurança diante de incidentes críticos simulados.

## Funcionalidades e Requisitos Atendidos
A aplicação foi construída em conformidade estrita com as especificações exigidas no escopo da avaliação:

* **Monitoramento de Dados Simulados:** Processamento em tempo real de variáveis dinâmicas cruciais: temperatura interna, status da comunicação de rádio e nível percentual da bateria.
* **Balanço de Sustentabilidade Energética:** Cálculo computacional contínuo que confronta a geração de energia limpa (proveniente dos painéis solares em kW) contra o consumo de potência ativa exigido pelos módulos da nave.
* **Geração Automática de Alertas:** Disparo de sinalizações imediatas na tela caso o ambiente atinja patamares operacionais perigosos (temperatura superior a 80.0°C ou energia abaixo de 20.0%).
* **Tomada de Decisão Autônoma (Inovação):** Mecanismos inteligentes que atuam de forma automática para salvaguardar a missão: desativação programada de subsistemas secundários (como pesquisas biológicas) para reduzir o consumo de kW ou interrupção instantânea da propulsão principal para viabilizar o resfriamento de emergência.
* **Interface Otimizada (Usabilidade):** Painel de visualização estruturado de forma puramente textual no terminal, limpo, sem o uso de caracteres informais (emojis) e padronizado com formatação de precisão numérica (uma casa decimal).

## Sistema

O ecossistema do script utiliza estritamente as bibliotecas nativas da linguagem Python (`time` e `random`), o que anula a necessidade de instalação de dependências ou pacotes externos através de gerenciadores.

---

### 3. 💻 Código-Fonte Final Completamente Corrigido (`telemetria.py`)
*Este código já está configurado com as atualizações de dados fixadas em **1 segundo** (`time.sleep(1)`). Dessa forma, quando você for realizar a gravação da tela, as variações de falha de conexão e superaquecimento acontecerão de maneira rápida na tela, permitindo concluir o vídeo dentro do limite máximo de 3 minutos.*

```python
import random
import time

# --- CONFIGURAÇÕES DE LIMITES CRÍTICOS (Regras de Negócio) ---
LIMITE_TEMP_MAX = 80.0  # Celsius
LIMITE_BATERIA_CRITICA = 20.0  # Percentual

# --- ESTADO INICIAL DA MISSÃO (Banco de dados simulado) ---
missao_status = {
    "temperatura": 25.0,
    "bateria": 100.0,
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
    Simula a oscilação dos dados operacionais da missão espacial no tempo.
    """
    # Flutuação da temperatura
    missao_status["temperatura"] += round(random.uniform(-3.0, 5.0), 1)
    
    # Simulação da dinâmica energética (Geração vs Consumo)
    missao_status["painel_solar_geracao"] = round(random.uniform(1.0, 8.0), 1)
    
    # O saldo energético afeta diretamente a bateria
    saldo_energetico = missao_status["painel_solar_geracao"] - missao_status["consumo_sistemas"]
    missao_status["bateria"] += round(saldo_energetico * 1.5, 1)
    
    # Limitadores da bateria entre 0% e 100%
    missao_status["bateria"] = max(0.0, min(100.0, missao_status["bateria"]))
    
    # Oscilação aleatória na comunicação
    if random.random() < 0.05:
        missao_status["comunicacao_terra"] = "INSTAVEL"
    elif random.random() < 0.02:
        missao_status["comunicacao_terra"] = "PERDIDA"
    else:
        missao_status["comunicacao_terra"] = "ESTAVEL"


def processar_alertas_e_decisoes():
    """
    Aplica IA introdução / Estruturas Lógicas para gerar alertas 
    e tomar decisões automatizadas de segurança.
    """
    print("\n--- [SISTEMA DE SEGURANÇA AUTÔNOMO] ---")
    alertas_ativos = False

    # 1. Análise Crítica de Temperatura
    if missao_status["temperatura"] >= LIMITE_TEMP_MAX:
        print(f"ALERTA CRITICO: Temperatura elevada ({missao_status['temperatura']:.1f} C)!")
        print("ACAO AUTONOMA: Ligando sistema de resfriamento de emergencia e suspendendo propulsao.")
        missao_status["modulos"]["Propulsao"] = "SUSPENSO (RESFRIAMENTO)"
        missao_status["temperatura"] -= 12.0  # Efeito prático da ação autônoma
        alertas_ativos = True
    else:
        if missao_status["modulos"]["Propulsao"] == "SUSPENSO (RESFRIAMENTO)":
            missao_status["modulos"]["Propulsao"] = "OPERACIONAL"

    # 2. Análise Crítica de Energia (Sustentabilidade)
    if missao_status["bateria"] <= LIMITE_BATERIA_CRITICA:
        print(f"ALERTA CRITICO: Bateria em nivel de emergencia ({missao_status['bateria']:.1f}%).")
        print("ACAO AUTONOMA: Protocolo de Economia de Energia Ativado. Desligando Pesquisas Cientificas.")
        missao_status["modulos"]["Pesquisa Cientifica"] = "DESLIGADO (ECONOMIA)"
        missao_status["consumo_sistemas"] = 1.5  # Reduz o consumo global do sistema
        alertas_ativos = True
    else:
        if missao_status["modulos"]["Pesquisa Cientifica"] == "DESLIGADO (ECONOMIA)":
            print("ACAO AUTONOMA: Energia restabelecida. Reativando modulos cientificos.")
            missao_status["modulos"]["Pesquisa Cientifica"] = "OPERACIONAL"
            missao_status["consumo_sistemas"] = 3.5

    # 3. Análise de Comunicação
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


# --- LOOP PRINCIPAL DE EXECUÇÃO ---
def iniciar_monitoramento():
    print("Iniciando Sistema de Monitoramento da Missao...")
    time.sleep(1)
    
    try:
        while True:
            simular_ambiente()
            exibir_painel()
            processar_alertas_e_decisoes()
            
            # Mensagem e sleep configurados para 1 segundo para dinâmica fluida no vídeo
            print("\nAtualizando dados em 1 segundo... (Pressione Ctrl+C para encerrar)")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nMonitoramento encerrado pelo operador.")

if __name__ == "__main__":
    iniciar_monitoramento()

