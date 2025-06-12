# Failsafe

A Python module that executes a callback script if a password is not entered within a specified time interval. This security feature acts as a failsafe mechanism to protect sensitive systems and data.

## Features

- Configurable timeout period
- Thread-based asynchronous execution
- Customizable callback script
- Password verification system
- Logging functionality

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Files

- `failsafe.py`: Core module implementing the failsafe timer functionality
- `example.py`: Example implementation showing how to use the failsafe module
- `callback_script.py`: Example callback script that logs failsafe trigger events

## Installation

No installation required. Simply copy the files to your project directory.

## Usage

1. Import the FailSafe class:
```python
from failsafe import FailSafe
```

2. Create a failsafe timer instance:
```python
timer = FailSafe(timeout_seconds=300, callback_script='your_callback_script.py')
```

3. Start the failsafe timer:
```python
timer.start()
```

4. Update the timer when correct password is entered:
```python
timer.update_password_time()
```

5. Stop the failsafe timer when done:
```python
timer.stop()
```

## Example

```python
from failsafe import FailSafe

# Create failsafe timer with 5 minutes timeout
timer = FailSafe(timeout_seconds=300, callback_script='callback_script.py')
timer.start()

# Get password input
password = input("Enter password: ")
if password == "correct_password":
    timer.update_password_time()
```

## Callback Script

The failsafe callback script is executed when the password timeout occurs. You can customize the callback script to perform various security actions such as:
- System logout
- Screen lock
- Send security notifications
- Log security events
- Execute emergency security measures

Example failsafe callback script:
```python
from datetime import datetime

def main():
    log_file = "failsafe_timeout.log"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(log_file, "a") as f:
        f.write(f"[{current_time}] Failsafe callback script executed due to password timeout.\n")

if __name__ == "__main__":
    main()
```

## Security Considerations

1. Implement proper password validation in your application
2. Secure the failsafe callback script to prevent unauthorized access
3. Consider encrypting sensitive data in logs
4. Implement appropriate error handling
5. Use secure methods for password storage and verification
6. Regularly test the failsafe mechanism to ensure it works as expected

## Contributing

Feel free to submit issues and enhancement requests to improve the failsafe mechanism.

## License

This project is open source and available under the MIT License. 