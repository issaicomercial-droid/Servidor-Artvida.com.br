# Registro de Tentativas e Erros - Servidor WSL2 (artvida.com.br)

Este documento registra todas as tentativas de expor o servidor WSL2 para a internet, para garantir que não repitamos falhas e que encontremos a melhor solução.

## Histórico de Tentativas

### 1. Tentativa: Quick Tunnel (TryCloudflare)
- **Data**: 2026-04-09
- **Comando**: `cloudflared tunnel --url http://127.0.0.1:8000`
- **Resultado**: **FALHA (Connection Reset)**
- **Diagnóstico**: A operadora (Sigmanet) parece estar resetando a conexão TCP durante o handshake com o servidor de túneis rápidos da Cloudflare. É um comportamento comum em ISPs residenciais que usam filtros de segurança ou CGNAT agressivo.
- **Lição**: Túneis rápidos (sem autenticação) são facilmente bloqueados pela operadora.

### 2. Tentativa: SSH Tunnel (localhost.run)
- **Data**: 2026-04-09
- **Comando**: `ssh -R 80:localhost:8000 localhost.run`
- **Resultado**: **FALHA (Permission Denied)**
- **Diagnóstico**: Falta de chave SSH configurada no ambiente para o serviço.

---

## Próximas Estratégias (A seguir)

### 3. Estratégia Recomendada: Tunnel Nomeado (Via Cloudflare Login)
- **Data**: 2026-04-09
- **Ação**: Iniciado comando `cloudflared tunnel login`.
- **Status**: Aguardando autorização do usuário no navegador.

### 4. Estratégia de Backup: Protocolos Alternativos
- Forçar o uso de `--protocol http2` ou `h2mux` no `cloudflared`.

### 5. Estratégia de Backup: Ajuste de MTU
- Reduzir o tamanho dos pacotes para evitar fragmentação no roteador residencial.
