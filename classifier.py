import math


class Classifier:
    classes_count = {}

    def __init__(self, data_dict):
        for k in data_dict.keys():
            self.classes_count[k] = 0

    def knn_algo(self, data_dict, predict, radius):
        for k in data_dict.keys():
            for i in range(0, len(data_dict[k])):
                el = data_dict[k][i]
                el_rad = math.sqrt((predict[0] - el[0]) ** 2 + (predict[1] - el[1]) ** 2)
                if el_rad <= radius:
                    self.classes_count[k] += 1
        sorted_count = sorted(self.classes_count.items(), key=lambda x: x[1], reverse=True)
        sorted_count = dict(sorted_count)
        print("Точка принадлежит к классу " + next(iter(sorted_count)))

