from scipy.fft import rfft, rfftfreq  # методы для быстрых преобразований фурье
from scipy.io.wavfile import write  # метод для записи сигнала в .waw файл (для себя)
import numpy as np  # удобная библиотека для быстрой работы с массивами чисел


# нормализация - процесс выравнивания громкости (если говорить о звуковом сигнале)
# нормализованный сигнал можно записать в звуковой файл
def normalize_signal(signal):
    return np.int16((signal / signal.max()) * ((2**16)/2 - 1))


# генерация синусоидального гармонического сигнала
def sine_signal(duration, freq, sampling_rate):
    time = np.linspace(0, duration, num=duration*sampling_rate, endpoint=False)  # получаем временную шкалу
    signal = np.sin((2 * np.pi) * time * freq)  # f(x) = A sin(2PI * t * f) - без учета смещения фазы
    return time, signal  # возвращаем время и сигнал (по сути значения по оси Х и по оси У)


# генерация импульсного сигнала
def pulse_signal(duration, freq, sampling_rate, unipolar):
    t, s = sine_signal(duration, freq, sampling_rate)  # получаем синусоиду
    s = np.sign(s)  # на основе синусоиды, создаем сигнал со значениями +1 или -1, в зависимости от знака синусоиды
    if unipolar:  # если нам нужен однополярный сигнал
        s = (s + 1) / 2
    return t, s


# получение спектральной плотности мощности сигнала
def psd(signal, sampling_rate):
    signal = normalize_signal(signal)  # нормализуем сигнал
    frequencies = rfftfreq(len(signal), 1 / sampling_rate)  # получаем диапазон частот, которые возможно передать
    # сигналом с текущей частотой дескритизации
    power = np.abs(rfft(signal))  # получение спектральной плотности мощности при помощи быстрого преобразования фурье
    return frequencies, power


# запись сигнала в аудио
def make_audio(signal, sampling_rate):
    signal = normalize_signal(signal)
    write("my_signal.wav", sampling_rate, signal)