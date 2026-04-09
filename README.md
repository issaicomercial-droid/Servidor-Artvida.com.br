# 🚀 Central do Servidor WSL2 - artvida.com.br

Este diretório contém as configurações e ferramentas para o seu servidor caseiro rodando em WSL2 e exposto via Cloudflare Tunnel.

## 🌐 Endereços Ativos

| Serviço | URL Pública | Porta Interna | Descrição |
| :--- | :--- | :--- | :--- |
| **Site Principal** | [https://artvida.com.br](https://artvida.com.br) | `8000` | Servidor Web (atualmente teste em Python) |
| **Acesso SSH** | `ssh.artvida.com.br` | `22` | Acesso terminal estilo VPS |
| **n8n Automation** | [https://n8n.artvida.com.br](https://n8n.artvida.com.br) | `5678` | Painel de automação de fluxos |

---

## 🤖 Como me conectar de outro Computador (Acesso Rápido)

Para configurar e acessar este servidor em qualquer computador Windows novo, basta rodar o nosso script de automação:

1. Baixe o arquivo `ACESSAR_SERVIDOR.ps1`.
2. Abra o **PowerShell** na pasta do arquivo.
3. Execute o comando:
   ```powershell
   powershell -ExecutionPolicy Bypass -File ACESSAR_SERVIDOR.ps1
   ```
*O script verificará o cloudflared, instalará se necessário, configurará o seu acesso SSH e conectará você ao servidor automaticamente.*

---

## 🤖 Como me conectar de outro Computador (Acesso Remoto à IA)

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
- `.gitignore`: Arquivo para evitar que logs e senhas subam para o Git.

---

## 🐙 Controle de Versão (Git)

O projeto já está inicializado com **Git**.
- **Para ver o que mudou**: `git status`
- **Para salvar uma alteração**: `git add .` e `git commit -m "sua mensagem"`
- **Para subir para o GitHub**: Peça para eu te ajudar a configurar o `git remote add origin <link-do-seu-repo>`.

---

## 🔒 Segurança
O acesso SSH remoto está protegido pela infraestrutura da Cloudflare. Para conectar de um novo computador, siga as instruções no arquivo `PASSO_A_PASSO_PAINEL.md` sobre a configuração do arquivo `~/.ssh/config`.
