import random
import math


class Generator:
    """Класс для генерации данных. Входные параметры:
    1. photo_count - количество фотографий для генерации (т.е.
    количество чисел, используемых в генерации комбинаций);
    2. combo_int - количество комбинаций, которые необходимо сгенерировать;
    3. prefix_name - название "пути", т.е. префикс, используемый для генерации.
    Поддерживает разделение слэшем: слово/слово/слово;
    4. freezed_nums - цифры, "замораживаемые" при генерации.
    Например, при [1, 3] цифры 1 и 3 в создаваемых комбинациях
    всегда будут на своих местах."""
    def __init__(self, photo_count: int, combo_count: int,
                 prefix_name: str, freezed_nums: list[int]):
        self.photo_count: int = photo_count
        self.combo_count: int = combo_count
        self.prefix_name: str = prefix_name
        self.freezed_nums: list[int] = freezed_nums

    def generate_nums(self) -> list[list[int]]:
        """Метод для генерации всех возможных комбинаций из поступаемых цифр.
        Используются параметры photo_count, freezed_nums, combo_count
        из класса Generator. Для генерации используется рекурсивный подход.
        Возвращает список формата list[list[int]], который содержит комбинации,
        отвечающие всем параметрам."""
        count_of_nums_to_generate: int = (
            self.photo_count - len(self.freezed_nums))

        if self.combo_count > math.factorial(count_of_nums_to_generate):
            self.combo_count = math.factorial(count_of_nums_to_generate)

        nums: list[int] = [x for x in range(1, self.photo_count + 1)]
        num_combos: list[list[int]] = []

        while len(num_combos) < self.combo_count:
            random.shuffle(nums)
            freezed_is_ok: bool = True
            for freezed_number in self.freezed_nums:
                if nums.index(freezed_number) != freezed_number - 1:
                    freezed_is_ok = False
            if (nums not in num_combos) and freezed_is_ok:
                num_combos.append(list(nums))

        return num_combos

    def generate_cells(self) -> list[str]:
        """Метод для создания "ячеек" из комбинаций, полученных в методе
        generate_nums(). Добавляет префикс и создает список ячеек,
        которые в дальнейшем будут сохранены в Excel. Возвращает
        список формата list[str], где str - готовая уникальная комбинация."""
        combos_with_prefix: list[str] = []

        for combo in self.generate_nums():
            cell: str = ''
            for number in combo:
                cell += f'{self.prefix_name}/{str(number)}\n'
            combos_with_prefix.append(cell)

        return combos_with_prefix
