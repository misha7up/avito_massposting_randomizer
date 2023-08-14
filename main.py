from modules import design, generator
from PyQt6 import QtWidgets
from pandas import DataFrame
import time
import sys
import os


class Application(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.btn_save_to_file.clicked.connect(self.save_data)

    def get_data(self) -> (int, int, str, list[int]):
        """Метод, собирающий данные с полей в GUI PyQt
        и записывающий их в нужные параметры. Возвращает список
        параметров для дальнейшего генерирования и сохранения."""
        photo_count: int = int(self.spin_photo_count.value())
        combo_count: int = int(self.spin_combo_count.value())
        prefix_name: str = self.tedit_prefix.toPlainText()
        try:
            freezed_numbers: list[int] = [int(x) for x in
                                          self.tedit_freezed_numbers
                                          .toPlainText()
                                          .replace(' ', '').split(',')]
        except ValueError:
            freezed_numbers: list = []
        auto_open_file: bool = self.checkBox.isChecked()
        return (photo_count, combo_count, prefix_name,
                freezed_numbers, auto_open_file)

    def generate_data(self) -> DataFrame:
        """Метод, отвечающий за генерацию данных.
        Использует данные из элементов PyQt, полученных в методе
        get_data(). Возвращает сгенерированные данные."""
        (photo_count, combo_count, prefix_name,
         freezed_numbers, auto_open_file) = self.get_data()

        GEN: generator = generator.Generator(photo_count, combo_count,
                                             prefix_name, freezed_numbers)

        return DataFrame(GEN.generate_cells()), auto_open_file

    def save_data(self) -> None:
        """Метод, отвечающий за сохранение данных.
        Получает данные путем вызова метода generate_data(),
        после чего сохраняет их в .xlsx файл, присваивая
        уникальное значение с текущим временем."""
        data_to_save, auto_open_file = self.generate_data()
        current_time: str = time.strftime('%d-%m-%y_%H-%M-%S',
                                          time.localtime())
        file_name: str = f'Data_{current_time}.xlsx'
        try:
            data_to_save.to_excel(file_name, sheet_name='Data', index=False)
            if auto_open_file:
                os.startfile(file_name)
            else:
                QtWidgets.QMessageBox.about(self, 'Успешно',
                                            f'Сохранено в файл: {file_name}')
        except OSError:
            QtWidgets.QMessageBox.about(self, 'Ошибка',
                                        'Невозможно создать файл. Проверьте '
                                        'наличие папки generated_data!')


def main() -> None:
    app: QtWidgets.QApplication = QtWidgets.QApplication(sys.argv)
    window: Application = Application()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
