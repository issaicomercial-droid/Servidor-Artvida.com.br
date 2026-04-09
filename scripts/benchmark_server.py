import urllib.request
import time
import concurrent.futures
import statistics

URL = "http://localhost:8000/"

def make_request():
    start = time.time()
    try:
        with urllib.request.urlopen(URL) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = "Error"
    end = time.time()
    return end - start, status

def run_benchmark(total_requests, concurrency, label):
    print(f"\n🚀 Iniciando Teste: {label}")
    print(f"Total: {total_requests} requisições | Concorrência: {concurrency}")
    
    latencies = []
    errors = 0
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request) for _ in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            latency, status = future.result()
            if status == 200:
                latencies.append(latency)
            else:
                errors += 1
                
    end_time = time.time()
    total_duration = end_time - start_time
    rps = total_requests / total_duration
    
    if latencies:
        avg_latency = statistics.mean(latencies) * 1000
        p95_latency = statistics.quantiles(latencies, n=20)[18] * 1000 # p95
    else:
        avg_latency = 0
        p95_latency = 0

    print(f"✅ Concluído em {total_duration:.2f}s")
    print(f"📊 RPS: {rps:.2f} req/s")
    print(f"🕒 Latência Média: {avg_latency:.2f}ms")
    print(f"🕒 P95 Latência: {p95_latency:.2f}ms")
    print(f"❌ Erros: {errors}")
    
    return {
        "label": label,
        "total": total_requests,
        "concurrency": concurrency,
        "rps": rps,
        "avg": avg_latency,
        "p95": p95_latency,
        "errors": errors
    }

if __name__ == "__main__":
    results = []
    # Nível Leve
    results.append(run_benchmark(50, 1, "Leve (Sequencial)"))
    # Nível Médio
    results.append(run_benchmark(200, 5, "Médio (Concorrência 5)"))
    # Nível Stress
    results.append(run_benchmark(500, 20, "Stress (Concorrência 20)"))
    
    print("\n" + "="*40)
    print("RESUMO FINAL")
    print("="*40)
    for r in results:
        print(f"{r['label']}: {r['rps']:.2f} req/s | Avg: {r['avg']:.2f}ms")
