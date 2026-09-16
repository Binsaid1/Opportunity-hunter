import time
import subprocess

while True:
    print("Starting Opportunity Hunter...")
    
    result = subprocess.run(["python", "bot.py"])
    
    print("Bot stopped. Restarting in 10 seconds...")
    time.sleep(10)