# Passo a Passo: Configuração via Painel Cloudflare (Zero Trust)

Este método é o mais estável para usar seu domínio `artvida.com.br` no WSL2.

## 1. Acesse o Painel Zero Trust
1. Entre no [dashboard da Cloudflare](https://dash.cloudflare.com/).
2. No menu lateral, clique em **Zero Trust**.

## 2. Crie o Túnel
1. Vá em **Networks** -> **Tunnels**.
2. Clique no botão **Add a Tunnel**.
3. Escolha **Cloudflared** e clique em Next.
4. Dê um nome ao túnel (ex: `wsl-servidor-artvida`) e salve.

## 3. Obtenha o Token (O que eu preciso)
1. Na tela "Install and run a connector", selecione **Linux**.
2. Escolha a arquitetura **64-bit**.
3. Abaixo, aparecerá um comando que começa com `sudo cloudflared.exe service install ...`.
4. **Copie apenas o Token**: É a sequência longa de caracteres alfanuméricos que aparece no final desse comando.

## 4. Configure o Hostname Público
1. Vá para a próxima aba: **Public Hostname**.
2. Clique em **Add a public hostname**.
3. Preencha:
   - **Subdomain**: (pode deixar vazio para usar o domínio principal)
   - **Domain**: `artvida.com.br`
   - **Service Type**: `HTTP`
   - **URL**: `localhost:8000`
4. Salve a configuração.

---

## 5. Me envie o Token
Assim que você tiver o Token, cole ele aqui no chat e eu farei toda a instalação técnica no seu Linux automaticamente.
