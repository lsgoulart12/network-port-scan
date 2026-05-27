import socket
import sys
from typing import List


def port_scan(alvo: str, porta_inicial: int, porta_final: int, timeout: float = 1.0) -> List[int]:
    print(f"escaneando o alvo {alvo}")
    portas_abertas: List[int] = []

    for porta in range(porta_inicial, porta_final + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            resultado = sock.connect_ex((alvo, porta))
            # connect_ex retorna 0 quando a conexão é bem-sucedida
            if resultado == 0:
                portas_abertas.append(porta)
                print(f"porta {porta}; aberta")
        finally:
            sock.close()

    return portas_abertas


def main() -> int:
    # Esperado:
    # python scan.py host porta_inicial porta_final
    if len(sys.argv) != 4:
        print("modo de uso: python scan.py host porta_inicial porta_final")
        print(f"recebido: {sys.argv}")
        return 1

    alvo = sys.argv[1]
    porta_inicial = int(sys.argv[2])
    porta_final = int(sys.argv[3])

    portas = port_scan(alvo, porta_inicial, porta_final)
    print(f"portas abertas: {portas}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
