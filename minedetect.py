# Script for detecting crypto mining activities on virtual machines
# Created by c00kieccrisp

import psutil  # Library for system monitoring
import requests  # Library for sending HTTP requests
import time  # Library for time-related functions

# Discord webhook URL
# Replace with your webhook URL
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_id/your_webhook_token"

def send_discord_embed(title, description, color=16711680):
    """
    Sends an embed message to the Discord webhook.
    Created by c00kieccrisp
    """
    payload = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color  # Default is red (0xFF0000)
            }
        ]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("Embed message sent to Discord successfully. - c00kieccrisp")
        else:
            print(f"Failed to send embed message to Discord: {response.status_code} - c00kieccrisp")
    except Exception as e:
        print(f"Error sending embed message to Discord: {e} - c00kieccrisp")

def detect_high_cpu_usage(threshold=80):
    """
    Detect processes with CPU usage exceeding the threshold.
    Created by c00kieccrisp
    """
    high_cpu_processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['cpu_percent'] > threshold:
                high_cpu_processes.append(proc.info)
        except psutil.NoSuchProcess:
            continue
    return high_cpu_processes

def detect_suspicious_processes(keywords=None):
    """
    Detect processes with names containing mining-related keywords.
    Created by c00kieccrisp
    """
    if keywords is None:
        keywords = ["miner", "xmrig", "minerd", "cryptominer"]
    
    suspicious_processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name']):
        try:
            if any(keyword in (proc.info['name'] or '').lower() for keyword in keywords):
                suspicious_processes.append(proc.info)
        except psutil.NoSuchProcess:
            continue
    return suspicious_processes

def monitor_and_notify():
    """
    Monitor for suspicious activities and notify via Discord webhook.
    Created by c00kieccrisp
    """
    while True:
        # Detect high CPU usage
        high_cpu = detect_high_cpu_usage()
        if high_cpu:
            description = ""
            for proc in high_cpu:
                description += f"**Process:** {proc['name']} (PID: {proc['pid']}), **CPU:** {proc['cpu_percent']}%\n"
            send_discord_embed(
                title="⚠️ High CPU Usage Detected",
                description=description,
                color=16776960  # Yellow
            )
        
        # Detect suspicious processes
        suspicious = detect_suspicious_processes()
        if suspicious:
            description = ""
            for proc in suspicious:
                description += f"**Process:** {proc['name']} (PID: {proc['pid']})\n"
            send_discord_embed(
                title="⚠️ Suspicious Processes Detected",
                description=description,
                color=16711680  # Red
            )
        
        # Wait before the next scan
        time.sleep(30)  # Adjust the interval as needed

# Entry point for the script
if __name__ == "__main__":
    # Created by c00kieccrisp
    monitor_and_notify()
