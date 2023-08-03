from modules.generator import Generator
from modules.interface import Interface
from pandas import DataFrame


def main():
    """Основной метод программы:
    1. Получает на вход данные от пользователя, вызывая метод
    ask_user_input() из модуля Interface;
    2. Генерирует данные с помощью создания экземпляра класса Generator
    и передачи в него полученных данных;
    3. Сохраняет получившиеся данные в файл с помощью pandas."""
    (photo_count, combo_count, prefix_name,
     freezed_numbers, file_name) = Interface.ask_user_input()

    GEN: Generator = Generator(photo_count, combo_count,
                               prefix_name, freezed_numbers)

    data_to_save = DataFrame(GEN.generate_cells())
    data_to_save.to_excel(file_name, sheet_name='sheet1', index=False)
    print(f'Сохранено в файл {file_name}.xlsx')


if __name__ == '__main__':
    main()
