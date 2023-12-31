from sys import stdin

class Car:
    def __init__(self, milage, distance):
        self.distance = distance
        self.tripLen = 0
        self.maxFuel = milage
        self.currentFuel = milage
        self.amountOfStops = 0

    def stop_for_gas(self, stop):
        # print("stopping")
        self.currentFuel = self.maxFuel
        self.amountOfStops += 1
        self.tripLen = stop

    def isGivenStopReachable(self, stop):
        if self.currentFuel >= stop - self.tripLen:
            return True
        else:
            return False

    def isStopReachable(self, stops, i):
        stop = stops[i]
        nextStop = 0
        if i + 1 >= len(stops):
            nextStop = self.distance
        else:
            nextStop = stops[i + 1]

        return [self.isGivenStopReachable(stop), self.isGivenStopReachable(nextStop)]

    def driveOn(self, stop):
        # print("Driving On")
        self.currentFuel -= stop - self.tripLen
        self.tripLen = stop

def min_refills(distance, tank, stops):

    car = Car(tank, distance)
    
    for i in range(len(stops)):
        # print(f"i: {i}")
        # print(f"trip len: {car.tripLen}")
        # print(f"currentFuel: {car.currentFuel}")
        # print(f"amountOfStops: {car.amountOfStops}")
        if car.tripLen >= distance:
            break
        reachableStops = car.isStopReachable(stops, i)
        if reachableStops[0] == True and reachableStops[1] == False:
            car.stop_for_gas(stops[i])
        elif reachableStops[0] == False and reachableStops[1] == False:
            return -1
        else:
            car.driveOn(stops[i])

    if car.currentFuel >= distance - car.tripLen:
        car.driveOn(distance)
    else:
        return -1
    
    return car.amountOfStops



if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
