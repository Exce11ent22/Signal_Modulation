import matplotlib.pyplot as plt
from my_signal_lib import *


def plot_signals():
    plt.figure(figsize=(10, 8))  # настраиваем полотно
    plt.subplots_adjust(hspace=0.5)

    t, m = square_wave_modulation(3, 1, 44100, 'amplitude')  # получаем модулированный сигнал
    f, p = psd(m, 44100)  # получаем спектр модулированного сигнала
    filtered_psd = filter_psd(p, 0.5)  # фильтруем спектр
    s = psd_to_signal(filtered_psd)  # синтезируем сигнал из отфильтрофанного спектра

    plt.subplot(3, 1, 1)  # выбираем ячейку на полотне
    plt.plot(t, s, label="синтезированный сигнал")  # изображаем синтезированный и модулированный сигналы
    plt.plot(t, m, label="модулированный сигнал")
    plt.xlabel("Time [s]")
    plt.legend()  # показыаем надписи

    plt.subplot(3, 1, 2)
    plt.stem(f, filtered_psd, label="Отфильтрованный спектр")  # изображаем отфильтрованный спектр
    plt.xlim(0, 30)  # ограничиваем показываемый диапазон частот
    plt.legend()
    plt.xlabel("Frequency [Hz]")

    plt.subplot(3, 1, 3)
    plt.stem(f, p, label="Исходный спектр")  # изображаем исходный спектр
    plt.xlim(0, 30)
    plt.xlabel("Frequency [Hz]")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    plot_signals()
