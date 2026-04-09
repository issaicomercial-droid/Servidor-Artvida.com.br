# 🚀 Central do Servidor WSL2 - artvida.com.br

Este diretório é o "Cérebro" do seu servidor, contendo as configurações de rede, automação e a aplicação principal.

## 🌐 Endereços Ativos

| Serviço | URL Pública | Porta Interna | Descrição |
| :--- | :--- | :--- | :--- |
| **Site Principal** | [https://artvida.com.br](https://artvida.com.br) | `8000` | Interface de Chat (Central Artvida APP) |
| **Acesso SSH** | `ssh.artvida.com.br` | `22` | Acesso terminal estilo VPS |
| **n8n Automation** | [https://n8n.artvida.com.br](https://n8n.artvida.com.br) | `5678` | Painel de automação de fluxos |

---

## 🤖 Central Artvida APP (O Chat Bot)

Esta é a interface web que permite "plugar" o seu bot do Telegram no seu site. 
- **Localização**: `./Central Artvida APP/`
- **Como funciona**: O site envia as mensagens para o **n8n**, que processa a lógica de cadastro de produtos da mesma forma que faz com o Telegram.

---

## 🛠️ Comandos de Controle

### 📡 Túnel Cloudflare (Conectividade)
Configuração gerenciada via painel Zero Trust.
- **Status do Túnel**: `cloudflared tunnel info`
- **Logs do Túnel**: `tail -f tunnel_final.log`

### 🤖 Automação (n8n)
O n8n roda via Docker na pasta raiz.
- **Localização**: `./n8n/`
- **Iniciar**: `docker compose up -d`

---

## 📂 Estrutura de Pastas Organizada

- `server.py`: O servidor que "liga" o seu site na porta 8000.
- `Central Artvida APP/`: Contém o código visual do seu site (HTML/CSS/JS).
- `n8n/`: Configurações do Docker para o n8n.
- `ACESSAR_SERVIDOR.ps1`: Script para configurar novos computadores.
- `PASSO_A_PASSO_PAINEL.md`: Guia de configuração do Zero Trust.
- `tentativas_e_erros.md`: Histórico de diagnósticos da rede.
