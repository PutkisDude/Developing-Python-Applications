#Author Lauri Putkonen
#2. Create class Clock and it's subclass AlarmClock. Test clocks in main.
#There has to be ticking and alarming methods...

class Clock:
    def tick(self):
        print("tic tic tic..")

class AlarmClock(Clock):
    def alarm(self):
        print("Wakey wake")
        print("BRRRRRRR")
        
print("The watch created:")
watch = Clock()
watch.tick()

print("\nSnooze created")
snooze = AlarmClock()
snooze.tick()
snooze.alarm()

#OUTPUT:
# Watch created:
# tic tic tic..
 
# Snooze created
# tic tic tic..
# Wakey wake
# BRRRRRRR
