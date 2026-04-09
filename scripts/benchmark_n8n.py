import urllib.request
import time
import concurrent.futures
import statistics

# Alvo: Dashboard do n8n para medir a capacidade do servidor Node.js/Docker
URL = "http://localhost:5678/healthz" 

def make_request():
    start = time.time()
    try:
        with urllib.request.urlopen(URL, timeout=10) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_n8n_benchmark(total_requests, concurrency, label):
    print(f"\n⚡ BENCHMARK n8n: {label}")
    print(f"Total: {total_requests} | Concorrência: {concurrency}")
    
    latencies = []
    errors = {}
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request) for _ in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            latency, status = future.result()
            if status == 200:
                latencies.append(latency)
            else:
                errors[status] = errors.get(status, 0) + 1
                
    end_time = time.time()
    total_duration = end_time - start_time
    rps = total_requests / total_duration
    
    avg_latency = statistics.mean(latencies) * 1000 if latencies else 0
    total_errors = sum(errors.values())

    print(f"🏁 Concluído em {total_duration:.2f}s")
    print(f"📊 RPS: {rps:.2f} req/s")
    print(f"🕒 Latência Média: {avg_latency:.2f}ms")
    print(f"❌ Falhas: {total_errors}")
    if errors:
        print(f"🔍 Detalhes: {errors}")
    
    return {"rps": rps, "avg": avg_latency, "errors": total_errors}

if __name__ == "__main__":
    print("⏳ Iniciando Benchmark de Capacidade do n8n (Docker/Node.js)...")
    
    # Teste 1: Carga Base
    run_n8n_benchmark(50, 10, "Carga Base")
    
    # Teste 2: Stress
    run_n8n_benchmark(200, 50, "Carga de Stress")
    
    # Teste 3: Ruptura
    run_n8n_benchmark(500, 100, "Busca de Ruptura")
