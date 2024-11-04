# app.py
import os
import subprocess

target_address = os.environ.get("TARGET")

def main():
    if target_address:
        print(f"Pinging target address: {target_address}")
        ping_result = subprocess.run(["ping", "-c", "4", target_address], stdout=subprocess.PIPE, text=True)
        print(ping_result.stdout)
    else:
        print("TARGET environment variable not set.")

if __name__ == "__main__":
    main()
