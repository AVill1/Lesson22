from model.human import Human

class Analyst:
    @staticmethod
    def count_adults(humans):
        count = 0
        if not isinstance(humans, (list, tuple)):
            return -1

        for human in humans:
            if isinstance(human, Human) and human. is_adult:
                if human.is_adult:
                    count += 1
        return count
               # count += 1 if human.is_adult else 0

    @staticmethod
    def count_alive_people(humans):
        count = 0
        if not isinstance(humans, (list, tuple)):
            return -1

        for human in humans:
            if isinstance(human, Human) and human.alive:
                if human.is_adult:
                    count += 1
        return count