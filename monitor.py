#用于获取一次CPU和内存

import psutil
import time

def get_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    log_line = f"[{now}] CPU: {cpu_usage:>5}% | mem: {mem_usage:>5}% | disk: {disk:>5}%"

    print(log_line,end='')

    with open("sys_monitor.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_line + "\n")

try:
    print("开始监控系统状态 (按 Ctrl+C 停止)...")
    while True:
        get_status()
        time.sleep(2) # 每隔2秒监控一次
except KeyboardInterrupt:
    print("\n监控已停止。")