#用于获取一次CPU和内存

import psutil
import time

def get_status():
    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    mem_usage = memory.percent #只提取百分比数据

    print(f"CPU使用率：{cpu_usage}%")
    print(f"内存使用率{mem_usage}%")

get_status()