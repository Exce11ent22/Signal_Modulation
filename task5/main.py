import matplotlib.pyplot as plt
from my_signal_lib import *


def plot_signals():
    plt.figure(figsize=(10, 6))  # настраиваем полотно
    plt.subplots_adjust(hspace=0.5)

    t, m = square_wave_modulation(3, 1, 44100, 'amplitude')  # получаем модулированный сигнал
    f, p = psd(m, 44100)  # получаем спектр модулированного сигнала
    filtered_psd = filter_psd(p, 0.5)  # фильтруем спектр
    s = psd_to_signal(filtered_psd)  # синтезируем сигнал из отфильтрофанного спектра

    plt.subplot(3, 1, 1)  # выбираем ячейку на полотне
    plt.plot(t, s, label="Синтезированный сиграл")  # изображаем синтезированный сигнал
    plt.xlabel("Time [s]")  # подписываем ось
    plt.legend()  # выводим информацию о графике

    plt.subplot(3, 1, 2)
    plt.plot(t, sos(s), label="Применение фильтра Баттерворта")
    plt.xlabel("Time [s]")
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t, filtered_to_impulse(s), label="Отфильтрованный импульсный сигнал")
    plt.xlabel("Time [s]")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    plot_signals()
