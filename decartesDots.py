import classifier


def input_point():
    x = int(input("Введите координаты точки по значению x: "))
    y = int(input("Введите координаты точки по значению y: "))
    coordinates = (x, y)
    user_class = input("Введите класс объекта: ")
    return coordinates, user_class


class DecartesDots:
    data = {}
    unclassed_point = tuple()
    radius = 0

    def __init__(self):
        while True:
            point = input_point()
            object_class = point[1]
            if object_class not in self.data:
                self.data[object_class] = []
            self.data[object_class].append(point[0])
            answer = input(
                "Хотите ли Вы еще добавить точку? Если «да», то введите «y», если нет, то нажмите любую другую "
                "клавишу. ")
            if answer != "y":
                break
        self.unclassed_point = tuple(map(int, input("Введите координаты точки неизвестного класса: ").split()))
        self.radius = int(input("Задайте величину радиуса ближайших соседей: "))

    def classify_Point(self):
        which_class = classifier.Classifier(self.data)
        which_class.knn_algo(self.data, self.unclassed_point, self.radius)
