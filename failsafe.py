import threading
import time
import subprocess
import os
from typing import Callable, Optional

class FailSafe:
    def __init__(self, timeout_seconds: int = 300, callback_script: Optional[str] = None):
        """
        Initialize password timer
        
        Args:
            timeout_seconds (int): Time interval requiring password input (in seconds)
            callback_script (str): Path to the callback script to execute
        """
        self.timeout_seconds = timeout_seconds
        self.callback_script = callback_script
        self.last_password_time = time.time()
        self.timer_thread = None
        self.is_running = False
        self._lock = threading.Lock()

    def start(self):
        """Start the timer"""
        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.is_running = True
            self.timer_thread = threading.Thread(target=self._timer_loop)
            self.timer_thread.daemon = True
            self.timer_thread.start()

    def stop(self):
        """Stop the timer"""
        self.is_running = False
        if self.timer_thread:
            self.timer_thread.join()

    def update_password_time(self):
        """Update the last password input time"""
        with self._lock:
            self.last_password_time = time.time()

    def _timer_loop(self):
        """Timer loop"""
        while self.is_running:
            current_time = time.time()
            with self._lock:
                time_since_last_password = current_time - self.last_password_time

            if time_since_last_password >= self.timeout_seconds:
                self._execute_callback()
                break

            time.sleep(1)

    def _execute_callback(self):
        """Execute callback script"""
        if self.callback_script and os.path.exists(self.callback_script):
            try:
                subprocess.run(['python', self.callback_script], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error executing callback script: {e}")
        else:
            print("Callback script not specified or does not exist.") 