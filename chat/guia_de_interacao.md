# 🤖 Guia de Interação com a IA - Projeto ArtVida

Este guia é para você (o usuário) ou para qualquer outra IA que venha a trabalhar neste servidor no futuro.

## 🔑 Como Retomar o Trabalho
Ao iniciar uma nova sessão, peça para a IA ler o arquivo `/chat/conhecimento_ia.md`. Isso dará a ela o contexto completo da infraestrutura sem que você precise explicar tudo de novo.

## 🛠️ Regras de Ouro do Servidor
1. **Nunca use `localhost` no Windows**: Sempre use o domínio `artvida.com.br` ou configure o túnel. O WSL é um ambiente isolado.
2. **Docker Primeiro**: Sempre que possível, instale novos serviços via Docker dentro da pasta raiz para manter a organização.
3. **Segurança do Túnel**: Se o acesso SSH cair, verifique primeiro o status do serviço `cloudflared`.

## 💬 Estilo de Comunicação
O Issai prefere:
- Explicações passo a passo.
- Organização clara em pastas (Central Artvida APP vs Servidor Config).
- Documentação atualizada a cada mudança significativa.

---
*Este documento garante que o conhecimento não se perca entre as conversas.*
