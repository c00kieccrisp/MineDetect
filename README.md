# Crypto Mining Detection Script

## Description
This script detects potential crypto-mining activities on virtual machines by monitoring:
- **High CPU usage**
- **Suspicious processes** (e.g., with mining-related keywords)

## Features
- **Discord Webhook Integration:** Sends alerts as Discord embeds.
- **Customizable Thresholds:** Modify CPU usage and keyword filters.
- **Continuous Monitoring:** Runs in a loop to scan processes periodically.

## Requirements
1. Python 3.x
2. Install the required libraries:
   ```bash
   pip install psutil requests
   ```

## Setup Instructions
1. **Prepare the Script**
   - Download the script to your system.
   - Open the script in a text editor.
2. **Configure Discord Webhook**
   - Replace the `DISCORD_WEBHOOK_URL` variable in the script with your actual Discord webhook URL.
3. **Run the Script**
   - Navigate to the directory containing the script.
   - Execute the script with the command:
     ```bash
     python script_name.py
     ```

## Script Watermark
Created by `c00kieccrisp`. All notable sections and outputs include the author's tag.

---

**Note:** Ensure the script runs with appropriate permissions to access process details on the host system.
