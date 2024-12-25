from stopwatch import Stopwatch
from adv01 import process_adv01
from adv02 import process_adv02
from adv03 import process_adv03

global_watch = Stopwatch()
watch = Stopwatch()

def run_advent(func,text):
    global_watch.resume()
    watch.start()
    result = func()
    watch.stop()
    global_watch.stop()
    time = watch.elapsed()
    print(f"{text} Result: {result} (took:{time})")

run_advent(process_adv01,"Advent-01")
run_advent(process_adv02,"Advent-02")
run_advent(process_adv03,"Advent-03")

print(f"\nAll Tests took {global_watch.elapsed_time} secs")



