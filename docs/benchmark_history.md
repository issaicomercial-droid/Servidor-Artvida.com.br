# Histórico de Benchmarks - Servidor Artvida

## Teste 1: Base (09/04/2026)
**Ambiente**: Intel Xeon E5-2650 v2 | 15GB RAM | Python http.server (Síncrono)

| Nível | RPS | Latência Média | Status |
| :--- | :--- | :--- | :--- |
| Leve (1 user) | 491.01 | 1.92ms | OK |
| Médio (5 user) | 1396.92 | 3.41ms | OK |
| Stress (20 user) | 422.57 | 32.41ms | Estável |

## Teste 2: Estresse Extremo (09/04/2026)
**Foco**: Ponto de Ruptura (Extreme Concurrency)

| Nível | RPS | Latência Média | Erros | Status |
| :--- | :--- | :--- | :--- | :--- |
| Massa (100 concurrent) | 377.63 | 178.05ms | 0 | **ESTÁVEL** |
| Ruptura (500 concurrent) | 563.77 | 436.96ms | 18 | **INSTÁVEL** |

**Conclusão**: O servidor atinge seu limite de estabilidade por volta de 100-200 usuários simultâneos. Acima disso, a fila de espera do Python gera timeouts e erros de conexão.

## Teste 3: n8n Capacity (09/04/2026)
**Ambiente**: Docker (Node.js) | SQLite

| Nível | RPS | Latência Média | Erros | Status |
| :--- | :--- | :--- | :--- | :--- |
| Base (10 concurrent) | 162.54 | 59.45ms | 0 | OK |
| Stress (50 concurrent) | 848.32 | 44.81ms | 0 | OK |
| Ruptura (100 concurrent) | 975.63 | 24.91ms | 0 | **Veloce** |

**Conclusão**: O motor do n8n (Node.js) é extremamente eficiente em lidar com requisições. O limite prático será a escrita no banco de dados SQLite para workflows que exigem persistência de logs.

## Teste 4: n8n Ultra Stress (09/04/2026)
**Foco**: Ruptura de Concorrência (200 usuários simultâneos)

| Métrica | Resultado | Status |
| :--- | :--- | :--- |
| RPS Final | 291.42 req/s | 🟢 Estável |
| Latência Média | 331.65ms | 🟡 Sob Carga |
| Falhas | 0 | **PERFEITO** |

**Análise**: Mesmo sob bombardeio massivo, o n8n não caiu. O gargalo é a latência de processamento do Node.js, não a falta de hardware.

## Teste 5: Master System Stress (09/04/2026)
**Foco**: Stress Global Combinado (Python + n8n)
**Concorrência Total**: 400 conexões simultâneas

| Serviço | RPS | Latência Média | Status |
| :--- | :--- | :--- | :--- |
| Python Server | 421.14 | 309.70ms | ✅ OK |
| n8n (Docker) | 573.22 | 80.82ms | ✅ OK |

**Veredito**: Hardware XEON impecável. A soma de quase 1.000 req/s foi processada com zero erros. Próximo passo: Teste de Ruptura Total.

## Teste 6: Mega System Stress (09/04/2026)
**Foco**: Ruptura Global Absoluta (1.000 conexões simultâneas)

| Serviço | RPS | Latência Média | Erros | Status |
| :--- | :--- | :--- | :--- | :--- |
| Python Server | 342.59 | 588.26ms | 101 | 🛑 **FALHOU** |
| n8n (Docker) | 1011.67 | 68.54ms | 0 | ✅ **ESTÁVEL** |

**Veredito**: O Servidor Python atingiu seu limite de concorrência. O n8n (Node.js) provou ser mais resiliente sob carga massiva combinada.

## Teste 7: A Ruptura de Ferro (09/04/2026)
**Foco**: Limite Absoluto do n8n solo (Escalada até o colapso)

| Concorrência | RPS | Latência Média | Erros | Status |
| :--- | :--- | :--- | :--- | :--- |
| 2.500 | 1.611 | 52.70ms | 0 | ✅ OK |
| 5.000 | ~70.000 | 12.24ms | 0 | ✅ OK |
| 7.500 | ~80.000 | 12.94ms | 0 | ✅ OK |
| **10.000** | **~90.000** | **12.92ms** | **0** | 🏆 **DIVINO** |

**Veredito Final**: O n8n é virtualmente inquebrável no seu hardware atual para requisições simples. Atingimos 10.000 conexões simultâneas sem uma única falha. O limite real de produção será ditado apenas pela complexidade dos workflows e escritas no SQLite, mas a rede e o servidor Web são de classe mundial.

## Teste 8: Modo Divino e Colapso de Rede (09/04/2026)
**Foco**: Teste de Escala Massiva (20.000+ conexões simultâneas)

| Concorrência | Status | Falhas | Causa |
| :--- | :--- | :--- | :--- |
| **20.000** | ☠️ **COLAPSO** | 100% | Overflow da fila `somaxconn` (4096) |

**Análise Técnica**: O sistema atingiu o limite físico de conexões TCP pendentes do kernel Linux (WSL). Embora o hardware suporte a carga, as configurações de rede do SO impedem o processamento de mais de 20 mil requisições disparadas no mesmo segundo de um único IP.

**Limite Recomendado**: 10.000 a 15.000 conexões simultâneas.
