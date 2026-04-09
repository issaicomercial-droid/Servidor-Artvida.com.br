# Script de Acesso Rápido ao Servidor ArtVida
# Uso: powershell -ExecutionPolicy Bypass -File ACESSAR_SERVIDOR.ps1

$Hostname = "ssh.artvida.com.br"
$User = "issai"
$ConfigPath = "$HOME\.ssh\config"
$CloudflaredUrl = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.msi"

Write-Host "--- 🚀 Iniciando Conexão com Servidor ArtVida ---" -ForegroundColor Cyan

# 1. Verificar/Instalar Cloudflared
if (!(Get-Command cloudflared -ErrorAction SilentlyContinue)) {
    Write-Host "[!] Cloudflared não encontrado. Iniciando instalação..." -ForegroundColor Yellow
    $TempPath = "$temp\cloudflared.msi"
    Invoke-WebRequest -Uri $CloudflaredUrl -OutFile $TempPath
    Start-Process msiexec.exe -ArgumentList "/i `"$TempPath`" /quiet /qn" -Wait
    Write-Host "[OK] Cloudflared instalado com sucesso!" -ForegroundColor Green
} else {
    Write-Host "[OK] Cloudflared já está instalado." -ForegroundColor Green
}

# 2. Configurar SSH
if (!(Test-Path "$HOME\.ssh")) { New-Item -ItemType Directory -Path "$HOME\.ssh" -Force | Out-Null }

$ConfigEntry = @"

Host $Hostname
  ProxyCommand cloudflared.exe access ssh --hostname %h
"@

if (Test-Path $ConfigPath) {
    $CurrentConfig = Get-Content $ConfigPath
    if ($CurrentConfig -notcontains "Host $Hostname") {
        Add-Content -Path $ConfigPath -Value $ConfigEntry
        Write-Host "[OK] Configuração SSH adicionada." -ForegroundColor Green
    } else {
        Write-Host "[OK] Configuração SSH já existe." -ForegroundColor Green
    }
} else {
    Set-Content -Path $ConfigPath -Value $ConfigEntry
    Write-Host "[OK] Arquivo de configuração SSH criado." -ForegroundColor Green
}

# 3. Conectar
Write-Host "--- 🔓 Conectando ao Servidor ($User@$Hostname) ---" -ForegroundColor Cyan
Write-Host "Digite sua senha do Linux quando solicitado:" -ForegroundColor Gray

ssh "$User@$Hostname"
