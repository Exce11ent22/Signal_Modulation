from my_signal_lib import *
import matplotlib.pyplot as plt


# Функция для построения графиков Сигнал + Спектр в одном окне
def plot_signals(frequencies, duration, sampling_rate, psd_lim):
    raw = len(frequencies)  # Высота полотна.
    column = 2  # ширина полотна
    position = 1  # текущая активная ячейка полотна
    plt.figure(figsize=(10, 8))  # задаем размер полотна
    for f in frequencies:  # для каждой частоты:
        plt.subplot(raw, column, position)  # выбираем ячейку на полотне
        t, s = pulse_signal(duration, f, sampling_rate, True)  # получаем временную шкалу и импульсный сигнал
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


frequencies = [1, 2, 4, 8]
plot_signals(frequencies, 5, 44100, (0, 50))