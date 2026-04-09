# 🤖 Central Artvida APP

Esta é a interface web (o Chatbot) que permite interagir com a sua automação do n8n diretamente pelo site `artvida.com.br`.

## ✨ Funcionalidades
- **Interface de Chat**: Design premium e minimalista.
- **Sistema de Login**: Acesso restrito para o usuário `Issai`.
- **Multicanal**: "Plugado" no mesmo cérebro (n8n) que o seu robô do Telegram.

---

## 🔐 Controle de Acesso
- **Usuário**: `Issai`
- **Senha**: (Definida anteriormente)
*A sessão é salva no navegador para que você não precise logar toda vez.*

---

## ⚙️ Integração com o n8n
Este aplicativo envia mensagens para o n8n via Webhook.
- **Método**: `POST`
- **Webhook URL**: `https://n8n.artvida.com.br/webhook/prod-cadastro`
- **Formato da Resposta Esperada**: `{ "output": "Sua mensagem aqui" }`

---

## 📂 Arquivos do App
- `index.html`: Estrutura visual e formulários.
- `style.css`: Estilização e animações.
- `script.js`: Lógica de login e comunicação com o n8n.
