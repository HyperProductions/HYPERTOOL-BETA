import psutil

def run():
    print("\n=== PROCESS VIEWER ===\n")

    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    print(f"{'PID':<10}{'NAME':<30}{'CPU%':<10}{'RAM%':<10}")
    print("-" * 60)

    for p in processes[:30]:  # sadece ilk 30 process
        print(f"{p['pid']:<10}{p['name'][:28]:<30}{p['cpu_percent']:<10}{p['memory_percent']:<10.2f}")

    print("\nToplam process:", len(processes))
    print("============================\n")