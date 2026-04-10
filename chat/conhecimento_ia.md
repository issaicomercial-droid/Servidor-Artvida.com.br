# 🧠 Base de Conhecimento IA - Servidor ArtVida

Este documento serve como a "memória" de todas as decisões, configurações e arquiteturas implementadas pela IA em conjunto com o usuário Issai.

## 📅 Histórico de Criação: Abril 2026
**Objetivo**: Transformar um ambiente WSL2 local em um servidor profissional capaz de hospedar aplicações web e automações (n8n), acessível de qualquer lugar do mundo.

---

## 🏗️ Arquitetura do Sistema

### 1. Camada de Rede (O Túnel)
- **Tecnologia**: Cloudflare Zero Trust (Tunnels).
- **Problema resolvido**: Contornar o CGNAT/ISP (Sigmanet).
- **Protocolo**: HTTP2 (estabilizado para evitar bloqueios de UDP).

### 2. Camada de Automação (n8n - Docker Nativo)
- **Plataforma**: n8n rodando em Docker nativo no Ubuntu 24.04 (Noble).
- **Migração**: O Docker Desktop do Windows foi descartado para garantir autonomia total no boot.

### 3. Camada de Resiliência (Blindagem Nível 4)
- **Tecnologia**: Agendador de Tarefas do Windows + Script Bash.
- **Boot**: O servidor sobe automaticamente na tela de login do Windows via logon S4U (User: `issai`).
- **Persistence**: Script `start_app.sh` lida com o "keep-alive" via `tail -f /dev/null`.

### 4. Camada de Aplicação (Central Artvida APP)
- **Interface**: Chat bot minimalista (Apple-style) em HTML/CSS/JS.
- **Servidor**: `server.py` na porta 8000.
- **Segurança**: Login exclusivo para usuário `Issai` (@Paitan1234).

---

## 🛠️ Configurações Técnicas Críticas

| Item | Valor / Caminho |
| :--- | :--- |
| **Pasta Raiz** | `/home/issai/projetos/Servidor artvida.com.br/` |
| **Script Início** | `./start_app.sh` |
| **User Linux** | `issai` |
| **Docker Engine** | Nativo (Ubuntu 24.04) |

---

## 🐙 Versionamento e Git
- **Repositório**: `https://github.com/issaicomercial-droid/Servidor-Artvida.com.br.git`
- **Fluxo**: Commits que documentam a evolução da blindagem e resiliência.

---
*Assinado: Antigravity AI (Sua parceira de programação)*
