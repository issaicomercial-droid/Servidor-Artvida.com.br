# 🧠 Base de Conhecimento IA - Servidor ArtVida

Este documento serve como a "memória" de todas as decisões, configurações e arquiteturas implementadas pela IA em conjunto com o usuário Issai.

## 📅 Histórico de Criação: Abril 2026
**Objetivo**: Transformar um ambiente WSL2 local em um servidor profissional capaz de hospedar aplicações web e automações (n8n), acessível de qualquer lugar do mundo.

---

## 🏗️ Arquitetura do Sistema

### 1. Camada de Rede (O Túnel)
- **Tecnologia**: Cloudflare Zero Trust (Tunnels).
- **Problema resolvido**: Contornar o CGNAT/ISP (Sigmanet) que impedia a abertura de portas no roteador.
- **Protocolo**: HTTP2 (estabilizado para evitar bloqueios de UDP).
- **Domínio**: `artvida.com.br`.

### 2. Camada de Acesso (SSH "VPS-Like")
- **Hostname**: `ssh.artvida.com.br`.
- **Configuração**: Tunelamento TCP na porta 22.
- **Cliente**: Automatizado via script PowerShell para permitir acesso instantâneo de qualquer PC Windows.

### 3. Camada de Aplicação (Central Artvida APP)
- **Interface**: Chat bot minimalista (Apple-style) em HTML/CSS/JS.
- **Servidor**: `server.py` (Python customizado) rodando na porta 8000.
- **Segurança**: Login exclusivo para usuário `Issai` com a senha definida (`@Paitan1234`).

### 4. Camada de Automação (n8n)
- **Plataforma**: n8n rodando em Docker Compose.
- **Endpoint**: `n8n.artvida.com.br`.
- **Conceito**: "Cérebro Multicanal" - uma única lógica para Telegram e Site.

---

## 🛠️ Configurações Técnicas Críticas

| Item | Valor / Caminho |
| :--- | :--- |
| **Pasta Raiz** | `/home/issai/projetos/Servidor artvida.com.br/` |
| **App Folder** | `./Central Artvida APP/` |
| **Tunnel ID** | `f43e91ca-0c8e-4874-b140-630df4fb4922` |
| **User Linux** | `issai` |

---

## 🐙 Versionamento e Git
- **Repositório**: `https://github.com/issaicomercial-droid/Servidor-Artvida.com.br.git`
- **Fluxo**: Commits granulares para cada funcionalidade (SSH, n8n, UI, Security).

## 🚀 Visão de Futuro
1. **Integração de Estoque**: Conectar o Webhook do chat ao banco de dados real.
2. **Novos Usuários**: Expandir o sistema de login para múltiplos colaboradores.
3. **SSL/TLS**: Totalmente gerenciado pela Cloudflare no "Edge".

---
*Assinado: Antigravity AI (Sua parceira de programação)*
