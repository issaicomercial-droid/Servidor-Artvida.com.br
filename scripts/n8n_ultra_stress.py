import urllib.request
import time
import concurrent.futures
import statistics

# Alvo: Dashboard do n8n (ponto de maior carga de processamento/sessão)
URL = "http://localhost:5678/" 

def make_request():
    start = time.time()
    try:
        # Timeout curto para forçar a detecção de gargalo
        with urllib.request.urlopen(URL, timeout=15) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_ultra_stress(total_requests, concurrency, label):
    print(f"\n☢️  ULTRA STRESS TEST: {label}")
    print(f"Alvo: {total_requests} requisições | Bombardeio de {concurrency} conexões/s")
    
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
    print(f"📊 RPS Final: {rps:.2f} req/s")
    print(f"🕒 Latência Média: {avg_latency:.2f}ms")
    print(f"❌ Falhas: {total_errors}")
    if errors:
        print(f"🔍 Detalhes de Erro: {errors}")
    
    return {"rps": rps, "avg": avg_latency, "errors": total_errors}

if __name__ == "__main__":
    print("🔥 Iniciando Bombardeio de Concorrência Máxima...")
    # 1000 requisições com 200 usuários batendo na porta ao mesmo tempo
    run_ultra_stress(1000, 200, "Nível de Ruptura SQL/API")
