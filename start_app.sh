#!/bin/bash
# ---------------------------------------------------------
# SCRIPT DE INICIALIZAÇÃO BLINDADA - SERVIDOR ARTVIDA
# ---------------------------------------------------------

# 1. Esperar 30 segundos (Garante que a rede e o Windows terminaram de subir)
sleep 30

# 2. Forçar sincronização de relógio (Evita erro de SSL/Túnel após o PC acordar)
sudo service docker start

# 3. Subir o Cérebro de Automação (n8n)
echo "Iniciando n8n (Docker Nativo)..."
cd "/home/issai/projetos/Servidor artvida.com.br/n8n"
docker compose up -d

# 4. Matar processos antigos do Site (Porta 8000) e subir o novo
echo "Iniciando Site Principal (Porta 8000)..."
cd "/home/issai/projetos/Servidor artvida.com.br"
fuser -k 8000/tcp || true
nohup python3 server.py > logs/server.log 2>&1 &

echo "---------------------------------------------------------"
echo "✅ SERVIDOR ARTVIDA TOTALMENTE OPERACIONAL!"
echo "---------------------------------------------------------"

# 5. Manter o processo vivo para o Serviço do Windows não fechar
tail -f /dev/null
