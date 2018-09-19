time = input("Time spent on the road:")
acceleration = input("Acceleration: ")
distanceinput = input("Distance: ")
time = int(time)
acceleration = int(acceleration)
distanceinput = int(distanceinput)
speedlimit = 60

speed = acceleration/time
duration = 0

while duration <= time:
    duration = duration + 1
    speed = speed + acceleration
    distance = int(speed * duration/10)
    print("duration:", duration, "Distance", "*" * distance)
  # if duration == 10:


if speed > speedlimit:
    print("The​ ​person​ ​went​ ​over​ ​the​ ​speed​ ​limit.​")
else:
    print("The person did not go over the speed limit.")

if distance >= distanceinput:
    print("The person reached the destination")
else:
    print("The person didn't reach the destination.")


