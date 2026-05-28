# Passo 1: Abrir o arquivo de log do firewall para leitura
with open("firewall.log", "r") as arquivo:
    linhas = arquivo.readlines()

# Passo 2: Criar um dicionário para contar os bloqueios de cada IP
bloqueios_por_ip = {}

# Passo 3: Analisar cada linha do log
for linha in linhas:
    if "BLOCKED" in linha:
        # Divide a linha em partes para isolar o endereço de IP
        partes = linha.split()
        ip = partes[3]  # O IP sempre fica na quarta posição da linha
        
        # Se o IP já estiver no dicionário, soma 1. Se não, começa em 1.
        if ip in bloqueios_por_ip:
            bloqueios_por_ip[ip] += 1
        else:
            bloqueios_por_ip[ip] = 1

# Passo 4: Exibir o relatório em texto corrido na tela
print("RELATÓRIO DE SEGURANÇA - ANÁLISE DE LOGS DE FIREWALL")
print("Após processar os logs, identificamos as seguintes atividades suspeitas:\n")

for ip, quantidade in bloqueios_por_ip.items():
    if quantidade > 3:
        print(f"O endereço IP {ip} tentou forçar acesso e foi bloqueado {quantidade} vezes. Isso caracteriza uma tentativa de ataque por força bruta na porta 22 (SSH). Recomenda-se o banimento imediato deste IP nas regras gerais da rede.")