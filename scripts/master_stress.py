import urllib.request
import time
import concurrent.futures
import statistics

# Configurações
TARGETS = {
    "Python_Server": "http://localhost:8000/",
    "n8n_Dashboard": "http://localhost:5678/healthz"
}

def make_request(url):
    start = time.time()
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_target_stress(url, total_requests, concurrency, label):
    latencies = []
    errors = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request, url) for _ in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            latency, status = future.result()
            if status == 200:
                latencies.append(latency)
            else:
                errors[status] = errors.get(status, 0) + 1
    
    rps = total_requests / (max(latencies) if latencies else 1) # Simplificação da duração
    avg = statistics.mean(latencies) * 1000 if latencies else 0
    return {"label": label, "rps": rps, "avg": avg, "errors": sum(errors.values()), "details": errors}

if __name__ == "__main__":
    print("🔥 MASTER SYSTEM STRESS INICIADO!")
    print("Disparando 400 conexões simultâneas (200 p/ cada serviço)...")
    
    start_all = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as orchestrator:
        # Dispara os dois testes ao mesmo tempo
        f_python = orchestrator.submit(run_target_stress, TARGETS["Python_Server"], 1000, 200, "Python Server")
        f_n8n = orchestrator.submit(run_target_stress, TARGETS["n8n_Dashboard"], 1000, 200, "n8n (Docker)")
        
        res_python = f_python.result()
        res_n8n = f_n8n.result()
        
    end_all = time.time()
    
    print("\n" + "="*45)
    print("RESULTADOS DO MASTER SYSTEM STRESS")
    print("="*45)
    for r in [res_python, res_n8n]:
        status = "✅ OK" if r['errors'] == 0 else f"❌ {r['errors']} ERROS"
        print(f"{r['label']:15} | RPS: {r['rps']:.2f} | Avg: {r['avg']:.2f}ms | {status}")
    
    print(f"\nDuração Total do Ataque: {end_all - start_all:.2f}s")
    print("Check-up de Hardware: Execute 'docker stats' e 'top' agora.")
