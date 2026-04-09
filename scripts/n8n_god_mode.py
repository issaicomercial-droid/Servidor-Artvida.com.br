import asyncio
import time
import socket

# Configurações
HOST = 'localhost'
PORT = 5678
PATH = '/healthz'

async def make_async_request(semaphore):
    async with semaphore:
        start = time.time()
        try:
            # Conexão TCP direta para máxima performance e baixo consumo de RAM
            reader, writer = await asyncio.wait_for(
                asyncio.open_connection(HOST, PORT), 
                timeout=5
            )
            
            # Request HTTP 1.1 mínima
            request = f"GET {PATH} HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
            writer.write(request.encode())
            await writer.drain()
            
            # Lendo apenas o status code (primeira linha)
            line = await reader.readline()
            writer.close()
            await writer.wait_closed()
            
            if b"200 OK" in line:
                status = 200
            else:
                status = f"Error: {line.decode().strip()}"
        except Exception as e:
            status = f"Error: {type(e).__name__}"
            
        return time.time() - start, status

async def run_god_mode_step(concurrency):
    print(f"\n⚡ MODO DIVINO: {concurrency} conexões simultâneas")
    
    # Semáforo para controlar a concorrência exata
    semaphore = asyncio.Semaphore(concurrency)
    
    start_time = time.time()
    
    # Criando as tarefas
    tasks = [make_async_request(semaphore) for _ in range(concurrency)]
    
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    
    latencies = [r[0] for r in results if isinstance(r[1], int) and r[1] == 200]
    errors = {}
    for r in results:
        if r[1] != 200:
            errors[r[1]] = errors.get(r[1], 0) + 1
            
    total_duration = end_time - start_time
    total_errors = sum(errors.values())
    error_rate = (total_errors / concurrency) * 100
    avg_latency = (sum(latencies) / len(latencies)) * 1000 if latencies else 0

    print(f"🏁 Ciclo concluído em {total_duration:.2f}s")
    print(f"📊 RPS Teórico: {concurrency / total_duration:.2f} req/s")
    print(f"🕒 Latência Média: {avg_latency:.2f}ms")
    print(f"❌ Falhas: {total_errors} ({error_rate:.1f}%)")
    if errors:
        print(f"🔍 Detalhes: {errors}")
        
    return {"concurrency": concurrency, "error_rate": error_rate, "avg": avg_latency}

async def main():
    print("🚀 INICIANDO ESCALADA PARA A SINGULARIDADE (GOD MODE)...")
    
    current_concurrency = 20000
    all_results = []
    
    try:
        while current_concurrency <= 70000: # Limite físico do protocolo TCP (~65.535 portas)
            res = await run_god_mode_step(current_concurrency)
            all_results.append(res)
            
            if res['error_rate'] > 5.0:
                print(f"\n💥 COLAPSO ATINGIDO EM {current_concurrency} CONEXÕES!")
                break
                
            current_concurrency += 10000
            await asyncio.sleep(2) # Pausa para o SO liberar sockets TIME_WAIT
            
    except Exception as e:
        print(f"\n⚠️ Ocorreu um erro crítico no script: {e}")

    print("\n" + "="*35)
    print("RELATÓRIO FINAL: ALÉM DO LIMITE")
    print("="*35)
    for r in all_results:
        status = "ESTÁVEL" if r['error_rate'] < 1 else "COLAPSO"
        print(f"C: {r['concurrency']:5} | Lat: {r['avg']:7.2f}ms | Erro: {r['error_rate']:5.1f}% | {status}")

if __name__ == "__main__":
    asyncio.run(main())
