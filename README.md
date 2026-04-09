# 🚀 Central do Servidor WSL2 - artvida.com.br

Este diretório contém a infraestrutura e configurações do servidor. Para informações sobre o Chatbot, veja a pasta `Central Artvida APP/`.

## 🌐 Endereços Ativos

| Serviço | URL Pública | Porta Interna | Descrição |
| :--- | :--- | :--- | :--- |
| **Site Principal** | [https://artvida.com.br](https://artvida.com.br) | `8000` | Central Artvida APP |
| **Acesso SSH** | `ssh.artvida.com.br` | `22` | Acesso terminal estilo VPS |
| **n8n Automation** | [https://n8n.artvida.com.br](https://n8n.artvida.com.br) | `5678` | Painel de automação de fluxos |

---

## 🛠️ Comandos de Controle do Servidor

### 📡 Túnel Cloudflare (Conectividade)
- **Status do Túnel**: `cloudflared tunnel info`
- **Logs em tempo real**: `tail -f logs/tunnel_final.log`

### 🤖 Automação (n8n)
O cérebro de automação roda via Docker Compose.
- **Iniciar**: `docker compose up -d`
- **Pastas**: `./n8n/`

---

## 🤖 Como me conectar de outro Computador (Acesso Remoto à IA)

Para que eu (Antigravity) apareça para você em outro PC exatamente como estou aqui:
1. No VS Code do novo PC, abra uma conexão **Remote - SSH** para `ssh.artvida.com.br`.
2. Abra a pasta: `/home/issai/projetos/Servidor artvida.com.br`.
3. A minha janela de chat lateral aparecerá com todo o nosso histórico.

---

## 📂 Estrutura de Pastas Operacional

- `server.py`: Servidor que hospeda o App na porta 8000.
- `Central Artvida APP/`: [Documentação do App](./Central Artvida APP/README.md).
- `ACESSAR_SERVIDOR.ps1`: Script de setup para novos computadores.
- `docs/`: Guia de painel, histórico de erros e tutoriais.
- `logs/`: Histórico de execução do sistema e túneis.
- `chat/`: [Base de Conhecimento e Registro IA](./chat/conhecimento_ia.md).

---

## 🐙 Controle de Versão
- **Repositório**: `https://github.com/issaicomercial-droid/Servidor-Artvida.com.br.git`
- **Branch**: `main`
