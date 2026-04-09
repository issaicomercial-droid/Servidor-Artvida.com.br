import urllib.request
import time
import concurrent.futures
import statistics

URL = "http://localhost:5678/healthz"

def make_request():
    start = time.time()
    try:
        # Timeout agressivo de 3s para detectar gargalo real
        with urllib.request.urlopen(URL, timeout=3) as response:
            response.read()
            status = response.getcode()
    except Exception as e:
        status = f"Error: {type(e).__name__}"
    end = time.time()
    return end - start, status

def run_iron_step(concurrency):
    total_requests = concurrency + 1000 # Carga de volume + concorrência
    print(f"\n🦾 ESCALADA DE FERRO: {concurrency} conexões simultâneas")
    
    latencies = []
    errors = {}
    
    # Usando uma abordagem mais eficiente para alta concorrência
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
    print(f"❌ Falhas: {total_errors} ({error_rate:.2f}%)")
    
    return {"concurrency": concurrency, "errors": total_errors, "error_rate": error_rate, "avg": avg_latency}

if __name__ == "__main__":
    print("🔥 BUSCANDO O PONTO DE COLAPSO (IRON RUPTURE)...")
    
    current_concurrency = 2500
    results = []
    
    try:
        while True:
            res = run_iron_step(current_concurrency)
            results.append(res)
            
            # Se a taxa de erro for > 5% ou latência > 2s, paramos (ruptura)
            if res['error_rate'] > 5.0 or res['avg'] > 2000:
                print(f"\n💥 RUPTURA ATINGIDA EM {current_concurrency} CONEXÕES!")
                break
            
            if current_concurrency >= 10000: # Limite de sanidade para não crashar o host Windows
                print("\n🏁 LIMITE DE SEGURANÇA DO SCRIPT ATINGIDO (10.000).")
                break
                
            current_concurrency += 500
            time.sleep(2) # Pequena pausa para o SO limpar sockets
    except KeyboardInterrupt:
        print("\n🛑 Teste interrompido pelo usuário.")

    print("\n" + "="*35)
    print("RELATÓRIO DE RESISTÊNCIA FINAL")
    print("="*35)
    for r in results:
        status = "ESTÁVEL" if r['error_rate'] < 1 else "INSTÁVEL"
        print(f"Conc: {r['concurrency']} | Lat: {r['avg']:.2f}ms | Erro: {r['error_rate']:.2f}% | {status}")
