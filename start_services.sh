#!/bin/bash

# Script para iniciar os serviços do Servidor Artvida no WSL2
# Localização: /home/issai/projetos/Servidor artvida.com.br/start_services.sh

PROJECT_DIR="/home/issai/projetos/Servidor artvida.com.br"
LOG_DIR="$PROJECT_DIR/logs"
TOKEN="eyJhIjoiNjdjYTU2ZDdlZTRlNmE3YTg4M2U0NmUyZWM4YWE2YmYiLCJ0IjoiZjQzZTkxY2EtMGM4ZS00ODc0LWIxNDAtNjMwZGY0ZmI0OTIyIiwicyI6Ill6ZGhPVE5rWmpBdFpHVXlZUzAwWXpReUxXSXpOVEl0TkRRME5EWXhNR00wTkdSbCJ9"

echo "🚀 Iniciando serviços do Servidor Artvida..."

cd "$PROJECT_DIR" || exit

# 1. Iniciar Python Server (Porta 8000)
if ! pgrep -f "python3 server.py" > /dev/null; then
    echo "🟢 Iniciando Python Server na porta 8000..."
    nohup python3 server.py > "$LOG_DIR/server.log" 2>&1 &
else
    echo "🟡 Python Server já está rodando."
fi

# 2. Iniciar Cloudflare Tunnel
if ! pgrep -f "cloudflared tunnel run" > /dev/null; then
    echo "🔵 Iniciando Cloudflare Tunnel (artvida.com.br)..."
    nohup cloudflared tunnel run --token "$TOKEN" --protocol http2 > "$LOG_DIR/tunnel_final.log" 2>&1 &
else
    echo "🟡 Cloudflare Tunnel já está rodando."
fi

# 3. Verificar n8n (Docker)
if docker compose -f "$PROJECT_DIR/n8n/docker-compose.yml" ps | grep -q "Up"; then
    echo "🟣 n8n (Docker) já está rodando."
else
    echo "🟠 n8n (Docker) parece estar parado. Iniciando..."
    docker compose -f "$PROJECT_DIR/n8n/docker-compose.yml" up -d
fi

echo "✅ Todos os serviços foram processados."
echo "Para ver os logs do tunnel: tail -f logs/tunnel_final.log"
echo "Para ver os logs do server: tail -f logs/server.log"
