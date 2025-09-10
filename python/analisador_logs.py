def analisar_logs(arquivo):
    with open(arquivo, 'r') as f:
        for linha in f:
            if "FAILED" in linha:
                print("[ALERTA] Falha detectada:", linha.strip())

# Exemplo de uso:
# analisar_logs("logs.txt")
