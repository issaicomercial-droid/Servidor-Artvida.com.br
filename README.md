# 🚀 Central do Servidor WSL2 - artvida.com.br

Este diretório contém as configurações e ferramentas para o seu servidor caseiro rodando em WSL2 e exposto via Cloudflare Tunnel.

## 🌐 Endereços Ativos

| Serviço | URL Pública | Porta Interna | Descrição |
| :--- | :--- | :--- | :--- |
| **Site Principal** | [https://artvida.com.br](https://artvida.com.br) | `8000` | Servidor Web (atualmente teste em Python) |
| **Acesso SSH** | `ssh.artvida.com.br` | `22` | Acesso terminal estilo VPS |
| **n8n Automation** | [https://n8n.artvida.com.br](https://n8n.artvida.com.br) | `5678` | Painel de automação de fluxos |

---

## 🛠️ Comandos de Controle

### 📡 Túnel Cloudflare (Conectividade)
O túnel está configurado como um **Remote Managed Tunnel**. A configuração de DNS e Hostnames é feita diretamente no painel [dash.cloudflare.com](https://dash.cloudflare.com/).

- **Status do Túnel**: `cloudflared tunnel info`
- **Logs do Túnel**: `tail -f tunnel_final.log`

### 🤖 Automação (n8n)
O n8n roda via Docker Compose para facilitar a manutenção.
- **Localização**: `/home/issai/projetos/Lançar Servidor/n8n/`
- **Iniciar**: `docker compose up -d`
- **Parar**: `docker compose down`
- **Ver Logs**: `docker compose logs -f`

---

## 📂 Organização do Projeto

- `server.py`: Script Python de teste para o site principal.
- `n8n/`: Diretório com as configurações do Docker para o n8n.
- `tentativas_e_erros.md`: Histórico de diagnósticos da rede.
- `PASSO_A_PASSO_PAINEL.md`: Guia de configuração do Zero Trust.

---

## 🔒 Segurança
O acesso SSH remoto está protegido pela infraestrutura da Cloudflare. Para conectar de um novo computador, siga as instruções no arquivo `PASSO_A_PASSO_PAINEL.md` sobre a configuração do arquivo `~/.ssh/config`.
