#用于获取一次CPU和内存

import psutil
import time

def get_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    
    print(f"[{time.strftime('%H:%M:%S')}] CPU: {cpu_usage:>5}% | 内存: {mem_usage:>5}%")

try:
    print("开始监控系统状态 (按 Ctrl+C 停止)...")
    while True:
        get_status()
        time.sleep(2) # 每隔2秒监控一次
except KeyboardInterrupt:
    print("\n监控已停止。")