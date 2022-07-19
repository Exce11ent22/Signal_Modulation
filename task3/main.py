import matplotlib.pyplot as plt
from my_signal_lib import *


# Функция для построения графиков Сигнал + Спектр в одном окне
def plot_signals(types, duration, frequency, sampling_rate, psd_lim):
    raw = len(types)  # Высота полотна.
    column = 2  # ширина полотна
    position = 1  # текущая активная ячейка полотна
    plt.figure(figsize=(10, 8))  # задаем размер полотна
    for t in types:  # для каждого типа модуляции:
        plt.subplot(raw, column, position)  # выбираем ячейку на полотне
        t, s = square_wave_modulation(duration, frequency, sampling_rate, t)  # получаем временную шкалу и модулированный сигнал
        plt.xlabel("Time [s]")  # Значения по оси Х для сигнала
        plt.plot(t, s)  # выводим график в текущей ячейке
        position += 1  # переходим к следующей ячейке

        # аналогично для спектра
        plt.subplot(raw, column, position)
        f, p = psd(s, sampling_rate)
        p[0] = 0  # обнуляем спектр в районе 0 Герц
        plt.xlim(psd_lim[0], psd_lim[1])
        plt.xlabel("Frequency [Hz]")
        plt.stem(f, p)
        position += 1
    plt.show()


if __name__ == '__main__':
    types = ['amplitude', 'frequency', 'phase']
    plot_signals(types, 2, 1, 44100, (0, 30))
