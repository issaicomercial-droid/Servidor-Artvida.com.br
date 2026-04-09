import urllib.request
import time
import concurrent.futures
import statistics
import socket

URL = "http://localhost:8000/"

def make_request():
    start = time.time()
    try:
        # Definindo timeout curto para identificar falhas rápido
        with urllib.request.urlopen(URL, timeout=5) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_extreme_test(total_requests, concurrency, label):
    print(f"\n🔥 TESTE DE RUPTURA: {label}")
    print(f"Alvo: {total_requests} requisições | Bombardeio Simultâneo: {concurrency}")
    
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
    print(f"📊 RPS Real: {rps:.2f} req/s")
    print(f"🕒 Latência Média: {avg_latency:.2f}ms")
    print(f"❌ Falhas: {total_errors}")
    if errors:
        print(f"🔍 Detalhes dos Erros: {errors}")
    
    return {
        "label": label,
        "rps": rps,
        "avg": avg_latency,
        "errors": total_errors,
        "details": errors
    }

if __name__ == "__main__":
    print("⚠️  AVISO: Este teste pode causar picos de CPU e lentidão no dashboard.")
    time.sleep(2)
    
    results = []
    # Nível Massa
    results.append(run_extreme_test(2000, 100, "100 Usuários Simultâneos"))
    
    # Nível Ruptura
    results.append(run_extreme_test(5000, 500, "500 Usuários Simultâneos"))
    
    print("\n" + "☠️ "*10)
    print("ANÁLISE DE RUPTURA")
    print("☠️ "*10)
    for r in results:
        status = "ESTÁVEL" if r['errors'] == 0 else "INSTÁVEL"
        print(f"{r['label']}: {r['rps']:.2f} RPS | Erros: {r['errors']} ({status})")
