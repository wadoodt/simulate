import pygame
import random
import time

def main(strat):
    # 737-800
    # Initialize Pygame
    pygame.init()

    # Set up the display window
    WIDTH, HEIGHT = 1020, 1020
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Airplane embarkation simulation")

    # Define colors
    WHITE = (255, 255, 255)
    GREY = (169, 169, 169)


    class Shape:
        all_instances = []

        def __init__(self, colour: tuple, x: int, y: int, x_long: int, y_long: int):
            self.colour = colour
            self.x = x
            self.y = y
            self.x_long = x_long
            self.y_long = y_long
            self.__class__.all_instances.append(self)

        def draw(self, display: pygame.display):
            pygame.draw.rect(display, self.colour, (self.x, self.y, self.x_long, self.y_long))

    class Seat(Shape):
        TopPadd = 10
        seatLong = 10
        seatWide = 10
        seatInBetween = 5
        aisleSize = 10
        seats = []
        middle = 25
        rowCoor = dict()
        seatCoor = dict()

        plan = [
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
            [1, 's', 1, 's', 1, 'a', 1, 's', 1, 's', 1],
        ]


        @staticmethod
        def createSeats():
            for ind, k in enumerate(Seat.plan):
                Seat.rowCoor[ind + 1] = (Passenger.pasLength + Seat.seatLong) * ind + Seat.TopPadd
                left = 0
                for inx, a in enumerate(k):
                    if a == 's':
                        left += Seat.seatInBetween
                    elif a == 'a':
                        left += Seat.aisleSize
                    elif a == 0:
                        left += Seat.seatWide
                    elif a == 1:
                        seat = Seat(GREY, left, Seat.TopPadd + (Seat.seatLong+Passenger.pasLength) * ind, Seat.seatWide, Seat.seatLong)
                        Seat.seats.append(seat)
                        Seat.seatCoor[inx // 2 + 1] = left
                        left += Seat.seatWide

    class Passenger(Shape):
        initedPs = []
        passengers = []
        pasLength = 6
        pasWidth = 10
        initial_x, initial_y = 40, 1 - pasLength
        alist = [0, 5, 1, 4, 2, 3]
        passenger_n = 0
        init_has_run = False
        beginningOfBoarding = 0

        def __init__(self, dest_x: int, dest_y: int, gender: int, ageGroup: int, x_long: int, y_long: int):
            if not Passenger.init_has_run:
                Passenger.beginningOfBoarding = time.time()
            Passenger.init_has_run = True
            Passenger.passenger_n += 1
            self.number = int(Passenger.passenger_n)
            self.beginning = [Passenger.initial_x, Passenger.initial_y]
            self.current_velocity = [0, 1]
            self.stage = 0
            self.every = 100
            self.move_enabled = True
            if gender == 0:  # Male
                if ageGroup == 0:
                    self.color = (0, 0, 255)  # Light Blue - Young Male
                    self.speed = random.randint(10,12)
                elif ageGroup == 1:
                    self.color = (0, 0, 175)  # Dark Blue - Old Male
                    self.speed = random.randint(7,11)
            elif gender == 1:  # Female
                if ageGroup == 0:
                    self.color = (255, 0, 255)  # Pink (Light Red) - Young Female
                    self.speed = random.randint(9, 12)
                elif ageGroup == 1:
                    self.color = (175, 0, 175)  # Dark Red - Old Female
                    self.speed = random.randint(5, 9)
            self.every = 1000//self.speed
            self.dest_x, self.dest_y = dest_x, dest_y
            self.unpacking = None
            self.createdAt = time.time()-Passenger.beginningOfBoarding
            print("Passenger ", self.number, ' created at ', time.time(), ' from beginning of Boarding')
            self.reachedAt = None
            self.state = 'moving'
            self.waitingTime = random.randint(4, 10)
            print("Passenger ", self.number, ' waiting time in seconds is : ', time.time())
            super(Passenger, self).__init__(self.color, Passenger.initial_x, Passenger.initial_y, x_long, y_long)
            Passenger.passengers.append(self)

        def run(self, mils):
            if self.state != 'moving' or not self.move_enabled:
                return  # Exit move method if movement is disabled
            if self.y < self.dest_y - self.pasLength:
                self.update_position(True, mils)
                if self.y == self.dest_y - self.pasLength:
                    row_Reached = time.time() - Passenger.beginningOfBoarding
                    print("Passanger ", self.number, ' has reached their row at : ', row_Reached)
                    self.stage = 1
                    self.unpacking = time.time()
            elif self.stage == 1 and time.time() >= self.unpacking + self.waitingTime:
                dir = 1 if self.dest_x - self.x > 0 else -1
                self.stage = 2
                self.current_velocity = [dir, 0]
            elif self.stage == 2 and self.x != self.dest_x:
                self.update_position(False, mils)
                if self.x == self.dest_x:
                    self.stage = 3
            elif self.stage == 3:
                self.y = self.dest_y + (Seat.seatLong-Passenger.pasLength)
                self.reachedAt = time.time() - Passenger.beginningOfBoarding
                print("Passanger ", self.number, "has found their seat at ", self.reachedAt,
                      ' seconds from beginning of boarding')
                self.state = 'seated'
                return

        def update_position(self, horiz, mils):
            if horiz:
                if int(mils/self.every) - abs(self.x - self.beginning[0]) <= 0:
                    return
            else:
                if int(mils/self.every) - abs(self.y - self.beginning[1]) <= 0:
                    return
            if self.check_collision(self.x + self.current_velocity[0], self.y + self.current_velocity[1]):
                self.x += self.current_velocity[0]
                self.y += self.current_velocity[1]
                if abs(int(self.x) - int(self.beginning[0])) == self.speed or int(self.y) - int(self.beginning[1]) == self.speed:
                    self.move_enabled = False

        def check_collision(self, x, y):
            for k in Passenger.passengers:
                if k != self and (k.x <= x < k.x+Passenger.pasWidth or k.x < x+Passenger.pasWidth <= k.x+Passenger.pasWidth) and (k.y <= y < k.y+Passenger.pasLength or k.y < y+Passenger.pasLength <= k.y+Passenger.pasLength):
                    return False
            return True

        @staticmethod
        def chooser(passengers):
            chosen_passengers = []
            while passengers:
                # Calculate probabilities based on remaining passengers
                probabilities = [passengers.count(ageSex) / len(passengers) for ageSex in [[0, 1], [1, 0], [0, 0], [1, 1]]]

                # Choose a ball based on probabilities
                chosen_passenger = random.choices([[0, 1], [1, 0], [0, 0], [1, 1]], weights=probabilities, k=1)[0]

                # Append the chosen ball to the list
                chosen_passengers.append(chosen_passenger)

                # Remove the chosen ball from the original list
                passengers.remove(chosen_passenger)

            return chosen_passengers

        @staticmethod
        def passengerInitialiser(youngMale: int, oldMale: int, youngFemale: int, oldFemale: int):
            listOfPassengersByAge = []
            for i in range(youngMale):
                listOfPassengersByAge.append([0,0])
            for i in range(oldMale):
                listOfPassengersByAge.append([0,1])
            for i in range(youngFemale):
                listOfPassengersByAge.append([1,0])
            for i in range(oldFemale):
                listOfPassengersByAge.append([1,1])
            result = Passenger.chooser(listOfPassengersByAge)
            return result

        @staticmethod
        def pasCount(n: int, batch: int):
            l = list(range(batch))
            for ind, k in enumerate(l):
                l[ind] = k + n
            random.shuffle(l)
            return l

        @staticmethod
        def countByRow(n: int, batch: int):
            klist = []
            for k in range((batch // 6) - 1, -1, -1):
                for g in range(6):
                    klist.append(Passenger.alist[g] + n + k * 6)
            return klist

        @staticmethod
        def strategyCreator(yM: int, oM: int, yF: int, oF: int, strategy: int, divider=18):
            listOfPs = Passenger.passengerInitialiser(yM, oM, yF, oF)
            if strategy == 0:  # random
                for k in range(0, len(Seat.seats)):
                    a = listOfPs[k]
                    Passenger.initedPs.append([k % 6, k//6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])
                random.shuffle(Passenger.initedPs)
            elif strategy == 1:  # row by row strategy
                n = 180
                for k in range(10):
                    n -= 18
                    for p in Passenger.countByRow(n, 18):
                        a = listOfPs[p]
                        Passenger.initedPs.append([p % 6, p // 6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])
            elif strategy == 2:  # block strategy
                n = 180
                for k in range(10):
                    n -= divider
                    for p in Passenger.pasCount(n, divider):
                        a = listOfPs[p]
                        Passenger.initedPs.append([p % 6, p//6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])
            elif strategy == 3:  # WilMA
                for s in Passenger.alist:
                    for k in range(179-s, -1, -6):
                        a = listOfPs[k - 1]
                        Passenger.initedPs.append([k % 6,k//6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])
            elif strategy == 4:  # WilMA New
                blist = [0, 5, 1, 4, 2, 3]
                for s in range(3):
                    for k in range(179, -1, -6):
                        a = listOfPs[k - 1]
                        Passenger.initedPs.append([(k-blist[s*2]) % 6,(k-blist[s*2])//6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])
                        Passenger.initedPs.append([(k-blist[s*2+1]) % 6, (k-blist[s*2+1]) // 6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])
            elif strategy == 5:  # Steffen
                listt = [0, 6, 5, 11, 1, 7, 4, 10, 2, 8, 3, 9]
                for i in listt:
                    for k in range(179-i, -1, -12):
                        a = listOfPs[k]
                        Passenger.initedPs.append([k % 6, k // 6, a[0], a[1], Passenger.pasWidth, Passenger.pasLength])

        @staticmethod
        def checkSpace(passengers):
            if len(passengers) > 0 and passengers[-1].y < 1:
                return False
            return True

        @staticmethod
        def createPassengers(initedPs: list):
            if len(initedPs) > 0:
                if Passenger.checkSpace(Passenger.passengers):
                    a = initedPs.pop(0)
                    Passenger.passengers.append(Passenger(Seat.seatCoor[a[0]+1], Seat.rowCoor[a[1]+1], a[2], a[3], a[4], a[5]))

    Seat.createSeats()
    Passenger.strategyCreator(72, 36, 45, 27, strat)
    time_last_print = pygame.time.get_ticks()
    mainLoop = True

    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False
        Passenger.createPassengers(Passenger.initedPs)
        current_time = pygame.time.get_ticks()
        if current_time - time_last_print >= 1000:
            counter = 0
            for passenger in Passenger.passengers:
                passenger.move_enabled = True  # Enable movement for the next second
                passenger.beginning = [int(passenger.x), int(passenger.y)]
            time_last_print = current_time  # Update the time of the last print
        win.fill(WHITE)
        for seat in Seat.seats:
            seat.draw(win)
        finished = True
        for p in Passenger.passengers:
            p.run(current_time)
            if p.state == "moving":
                finished = False
            p.draw(win)
        if finished:
            print("Boarding ended after ", time.time() - Passenger.beginningOfBoarding, "seconds")
            break
        pygame.display.update()


main(5)
