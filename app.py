import os # 沒用到，Lint 會抓
import subprocess # 用來示範之後的 SAST 安全問題

def run_command(cmd):
    # 這是一個危險的寫法，容易被 Command Injection
    subprocess.call(cmd, shell=True)

def say_hello(): 
    print("Hello") # 縮排不一致或格式問題
    
password = 'admin:123456' # 硬編碼密碼，SAST 會抓