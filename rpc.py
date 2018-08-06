import subprocess

#subprocess.run(["net rpc shutdown -I 192.168.1.95 -U pv1%mi666nus$"])

subprocess.run(["net", "rpc", "shutdown", "-I", "192.168.1.95", "-U", "pv1%mi666nus$"])
