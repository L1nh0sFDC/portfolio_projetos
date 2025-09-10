import socket

def verificar_porta(host, porta):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, porta))
        print(f"Porta {porta} ABERTA em {host}")
    except:
        print(f"Porta {porta} FECHADA em {host}")
    finally:
        s.close()

# Exemplo de uso:
# host = "127.0.0.1"
# for porta in [21, 22, 80, 443]:
#     verificar_porta(host, porta)
