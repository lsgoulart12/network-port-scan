# 🛡️ Analisador Automatizado de Logs de Firewall com Python

 Descrição do Projeto
Este projeto foi desenvolvido com foco em Segurança da Informação e Cibersegurança para automatizar a análise de logs gerados por firewalls de rede. O objetivo principal é identificar comportamentos maliciosos, especificamente tentativas de ataques por força bruta direcionados à porta 22 (serviço SSH).

A automação processa milhares de eventos de rede em segundos, isolando endereços IP suspeitos que acumulam múltiplos bloqueios e gerando um relatório executivo para tomada de decisão imediata da equipe de resposta a incidentes.

---

Tecnologias e Conceitos Aplicados
* **Linguagem:** Python 3
* **Manipulação de Arquivos:** Leitura e processamento de arquivos de texto estruturados (`.log`).
* **Estrutura de Dados:** Utilização de dicionários para contagem de frequência de eventos de segurança.
* **Lógica de Detecção:** Filtros baseados em regras de limiar (Threshold) para identificação de tráfego anômalo.

---

Estrutura dos Arquivos
* `firewall.log`: Arquivo que simula o tráfego real de uma rede corporativa, contendo registros de acessos liberados (ALLOWED) e negados (BLOCKED).
* `analisador.py`: O script em Python desenvolvido para varrer o arquivo de logs, extrair os IPs bloqueados e emitir alertas caso o limiar de segurança seja ultrapassado.

---

Relatório de Saída (Texto Corrido)
Quando executado, o script gera um diagnóstico direto e limpo para o administrador de rede:

"RELATÓRIO DE SEGURANÇA - ANÁLISE DE LOGS DE FIREWALL
Após processar os logs, identificamos as seguintes atividades suspeitas:
O endereço IP 192.168.1.150 tentou forçar acesso e foi bloqueado 6 vezes. Isso caracteriza uma tentativa de ataque por força bruta na porta 22 (SSH). Recomenda-se o banimento imediato deste IP nas regras gerais da rede."
