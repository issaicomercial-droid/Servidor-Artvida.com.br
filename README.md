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

### 🤖 Automação (n8n - Docker Nativo)
Agora o n8n roda **nativamente no Linux**, sem depender do Docker Desktop.
- **Iniciar**: `docker compose up -d` (dentro da pasta `./n8n/`)
- **Status**: `docker ps`

### 🛡️ Blindagem e Resiliência (Boot Automático)
O servidor está configurado para ligar **sem login do usuário** via Agendador de Tarefas do Windows.
- **Script de Boot**: `start_app.sh` (Sincroniza relógio, inicia Docker, n8n e Site).
- **Tarefa Windows**: `ArtVida_Server_Boot` (Modo S4U - Oculto).
- **Log de Inicialização**: `logs/server.log`

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
