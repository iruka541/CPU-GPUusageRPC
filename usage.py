from pypresence import Presence
import psutil
import time
import GPUtil

CLIENT_ID = 'client_ID'

rpc = Presence(client_id=CLIENT_ID)
rpc.connect()

def update_presence():
    cpu_percent = psutil.cpu_percent(interval=1)
    
    gpus = GPUtil.getGPUs()
    gpu_percent = gpus[0].load * 100 if gpus else 0

    rpc.update(
        details=f"CPU Usage: {cpu_percent:.1f}%", 
        state=f"GPU Usage: {gpu_percent:.1f}%" 
    )

while True:
    update_presence()
    time.sleep(2)
