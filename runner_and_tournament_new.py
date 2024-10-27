class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            this_round_finishers = []       # список финишировавших на данном круге
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    this_round_finishers.append(participant)    # Добавляем того, кто финишировал
                    # finishers[place] = participant        #
                    # place += 1                            # Закомментим неправильный код
                    # self.participants.remove(participant) #

                # Добавим свой код:
            if this_round_finishers:    # Кто-то финишировал
                if len(this_round_finishers) > 1:   # Если больше одного, то отсортируем по убыванию пройденной дистанции
                    this_round_finishers = sorted(this_round_finishers, key=lambda p: p.distance, reverse=True)
                for i in range(len(this_round_finishers)):  # Обработаем текущих финишёров:
                    finishers[place + i] = this_round_finishers[i]      # Запишем их в общий список согласно пройденной
                                                                        #                                    дистанции
                    self.participants.remove(this_round_finishers[i])   # Вычеркнем из списка бегущих
                place += len(this_round_finishers)  # Сколько мест заняли финишёры текущего круга


        return finishers
if __name__ == '__main__':
    part1 = Runner('Усейн', 10)
    part2 = Runner('Андрей', 9)
    res = Tournament(90, part1, part2).start()
    print(res)
    print(res[max(res.keys())].name)      # [p_[1].name for p_ in res.items()])
