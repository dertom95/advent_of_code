from stopwatch import Stopwatch
from adv01 import process_adv1

watch = Stopwatch()

def run_advent(func,text):
    watch.start()
    result = func()
    watch.stop()
    time = watch.elapsed()
    print(f"{text} Result:{result} (took:{time})")

run_advent(process_adv1,"Advent1")




