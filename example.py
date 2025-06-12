from failsafe import FailSafe
import time

def main():
    # Create failsafe timer with 5 minutes (300 seconds) timeout
    # Specify callback_script.py as the failsafe callback
    timer = FailSafe(timeout_seconds=300, callback_script='callback_script.py')
    
    # Start the failsafe timer
    timer.start()
    
    try:
        while True:
            # Get password input from user
            password = input("Enter password (type 'quit' to exit): ")
            
            if password.lower() == 'quit':
                break
                
            # Update failsafe timer if password is correct
            if password == "correct_password":  # Implement proper password validation logic for actual use
                timer.update_password_time()
                print("Password verified. Failsafe timer has been reset.")
            else:
                print("Incorrect password.")
                
    except KeyboardInterrupt:
        print("\nExiting failsafe program.")
    finally:
        timer.stop()

if __name__ == "__main__":
    main() 