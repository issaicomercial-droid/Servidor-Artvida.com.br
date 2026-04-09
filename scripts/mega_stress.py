import urllib.request
import time
import concurrent.futures
import statistics

TARGETS = {
    "Python_Server": "http://localhost:8000/",
    "n8n_Dashboard": "http://localhost:5678/healthz"
}

def make_request(url):
    start = time.time()
    try:
        # Timeout curto de 5s para forçar falha por lentidão
        with urllib.request.urlopen(url, timeout=5) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_mega_stress(url, total_requests, concurrency, label):
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
    
    rps = total_requests / (max(latencies) if latencies else 1)
    avg = statistics.mean(latencies) * 1000 if latencies else 0
    return {"label": label, "rps": rps, "avg": avg, "errors": sum(errors.values()), "details": errors}

if __name__ == "__main__":
    print("\n" + "💀 "*15)
    print("MEGA SYSTEM STRESS (TESTE DE RUPTURA)")
    print("Concorrência: 1.000 (500 p/ cada porto)")
    print("💀 "*15 + "\n")
    
    start_all = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as orchestrator:
        # Dispara o dobro da carga anterior
        f_python = orchestrator.submit(run_mega_stress, TARGETS["Python_Server"], 2500, 500, "Python Server")
        f_n8n = orchestrator.submit(run_mega_stress, TARGETS["n8n_Dashboard"], 2500, 500, "n8n (Docker)")
        
        res_python = f_python.result()
        res_n8n = f_n8n.result()
        
    end_all = time.time()
    
    print("\n" + "!"*45)
    print("VEREDITO DE RUPTURA")
    print("!"*45)
    for r in [res_python, res_n8n]:
        status = "✅ ESTÁVEL" if r['errors'] == 0 else f"🛑 FALHOU ({r['errors']} erros)"
        print(f"{r['label']:15} | RPS: {r['rps']:.2f} | Avg: {r['avg']:.2f}ms | {status}")
        if r['errors'] > 0:
            print(f"   -> Detalhes: {r['details']}")
    
    print(f"\nDuração Total do Bombardeio: {end_all - start_all:.2f}s")
