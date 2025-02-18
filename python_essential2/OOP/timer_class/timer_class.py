class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{str(self.__hours).zfill(2)}:{str(self.__minutes).zfill(2)}:{str(self.__seconds).zfill(2)}"

    def __check_time(self, minus=False):
        match (minus):
            case True:
                if self.__seconds == 0:
                    if self.__minutes == 0:
                        self.__hours = (self.__hours - 1) % 24
                    self.__minutes = (self.__minutes - 1) % 60

            case False:
                if self.__seconds == 0:
                    self.__minutes = (self.__minutes + 1) % 60
                    if self.__minutes == 0:
                        self.__hours = (self.__hours + 1) % 24

    def next_second(self):
        self.__seconds = (self.__seconds + 1) % 60
        self.__check_time()

    def prev_second(self):
        self.__check_time(True)
        self.__seconds = (self.__seconds - 1) % 60


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
