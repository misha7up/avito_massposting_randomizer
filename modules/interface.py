import time
from rich.prompt import IntPrompt


class Interface:
    """Интерфейс программы. Отвечает за взаимодействие с пользователем."""
    def ask_user_input() -> (int, int, str, list[int], str):
        """Метод для получения параметров от пользователя.
        Печатает приглашение для ввода с помощью print(), получает данные
        в потоке и возвращает их для использования в модуле Generator."""
        time_string: str = time.strftime("%d-%m-%y %H-%M-%S", time.localtime())
        file_name: str = f'generated_data/{time_string}.xlsx'

        photo_count: int = IntPrompt.ask(
            'Введите количество фотографий, или нажмите Enter '
            'для ввода по умолчанию:\n', default=10)

        combo_count: int = IntPrompt.ask(
            'Введите количество необходимых комбинаций, или нажмите Enter '
            'для ввода по умолчанию:\n', default=30)

        prefix_name: str = input('Введите имя проекта, используемое для '
                                 'генерации (напр. «лес» или «аб/гд/ёж»):\n')

        try:
            freezed_numbers: list[int] = [int(x) for x in input(
                'Введите числа для «заморозки» через пробел '
                '(например: «1 2 3»), или нажмите Enter, '
                'чтобы генерировать все цифры:\n').split(' ')]
        except ValueError:
            freezed_numbers: list = []

        return (photo_count, combo_count, prefix_name,
                freezed_numbers, file_name)
