import time

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() 
            self.running = True
            print("Stopwatch started.")

    def stop(self,output=False):
        if self.running:
            self.elapsed_time = time.time() - self.start_time  # Calculate elapsed time
            self.running = False
            if output:
                print(f"Stopwatch stopped at {self.elapsed_time:.2f} seconds.")

    def resume(self):
        if self.running:
            return

        self.running = True                
        if self.start_time==0:
            self.start_time = time.time() 

    def reset(self):
        self.start_time = 0
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset.")

    def elapsed(self):
        if self.running:
            return time.time() - self.start_time
        return self.elapsed_time

# Example usage
if __name__ == "__main__":
    stopwatch = Stopwatch()
    stopwatch.start()
    time.sleep(2)  # Simulate some elapsed time
    stopwatch.stop()
    print(f"Elapsed Time: {stopwatch.elapsed():.2f} seconds.")
    stopwatch.reset()
