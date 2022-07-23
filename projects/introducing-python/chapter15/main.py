import subprocess

# ret = subprocess.getoutput('date')
# print(ret)

# multiprocessing によるプロセスの作成
import multiprocessing
import os

def whoami(what):
    print(f"Process {os.getpid()} says: {what}")

if __name__ == "__main__":
    whoami("I'm the main process")
    for n in range(4):
        p = multiprocessing.Process(target=whoami, args=(f"I'm a child process {n}",))
        p.start()

