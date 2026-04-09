import urllib.request
import time
import concurrent.futures
import statistics

URL = "http://localhost:5678/healthz"

def make_request():
    start = time.time()
    try:
        # Timeout curto de 5s para detectar a "morte" do serviço
        with urllib.request.urlopen(URL, timeout=5) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_step(concurrency):
    total_requests = concurrency * 2 # Testamos o dobro da concorrência
    print(f"\n⚡ Degrau: {concurrency} conexões simultâneas")
    
    latencies = []
    errors = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(make_request) for _ in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            latency, status = future.result()
            if status == 200:
                latencies.append(latency)
            else:
                errors[status] = errors.get(status, 0) + 1
                
    avg_latency = statistics.mean(latencies) * 1000 if latencies else 0
    total_errors = sum(errors.values())
    error_rate = (total_errors / total_requests) * 100

    print(f"📊 RPS: {total_requests / (max(latencies) if latencies else 1):.2f}")
    print(f"🕒 Latência Média: {avg_latency:.2f}ms")
    print(f"❌ Falhas: {total_errors} ({error_rate:.1f}%)")
    
    return {"concurrency": concurrency, "errors": total_errors, "error_rate": error_rate, "avg": avg_latency}

if __name__ == "__main__":
    print("🛸 INICIANDO BUSCA PELA SINGULARIDADE DO n8n...")
    
    current_concurrency = 400
    all_results = []
    
    while current_concurrency <= 2000: # Limite de segurança p/ o script não travar o host
        res = run_step(current_concurrency)
        all_results.append(res)
        
        if res['error_rate'] > 1.0:
            print(f"\n⚠️ SINGULARIDADE ATINGIDA EM {current_concurrency} CONEXÕES!")
            break
            
        current_concurrency += 200 # Aumentando de 200 em 200 para rapidez
        time.sleep(1)

    print("\n" + "="*30)
    print("RESUMO DA SINGULARIDADE")
    print("="*30)
    for r in all_results:
        status = "ESTÁVEL" if r['error_rate'] == 0 else "RUPTURA"
        print(f"C: {r['concurrency']} | Lat: {r['avg']:.2f}ms | Erro: {r['error_rate']:.1f}% | {status}")
