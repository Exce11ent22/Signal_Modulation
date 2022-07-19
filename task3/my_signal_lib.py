from scipy.fft import rfft, rfftfreq  # методы для быстрых преобразований фурье
from scipy.io.wavfile import write  # метод для записи сигнала в .waw файл (для себя)
import numpy as np  # удобная библиотека для быстрой работы с массивами чисел


# нормализация - процесс выравнивания громкости (если говорить о звуковом сигнале)
# нормализованный сигнал можно записать в звуковой файл
def normalize_signal(signal):
    return np.int16((signal / signal.max()) * ((2 ** 16) / 2 - 1))


# генерация синусоидального гармонического сигнала
def sine_signal(duration, freq, sampling_rate):
    time = np.linspace(0, duration, num=duration * sampling_rate, endpoint=False)  # получаем временную шкалу
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
    power /= np.max(power)   # нормализация мощности от 0 до 1
    return frequencies, power


# запись сигнала в аудио
def make_audio(signal, sampling_rate):
    signal = normalize_signal(signal)
    write("my_signal.wav", sampling_rate, signal)


# модуляция гармонического сигнала меандром
def square_wave_modulation(duration, frequency_of_signal, sampling_rate, modulation='amplitude'):
    t, p = pulse_signal(duration, frequency_of_signal, sampling_rate, True)  # генерируем импульсный сигнал
    m = []
    if modulation == 'amplitude':  # для амплитудной модуляции
        t, s = sine_signal(duration, frequency_of_signal * 16, sampling_rate)
        m = s * p  # если импульсный сигнал равен 0, то и гармонический равен 0
    if modulation == 'frequency':  # для частотной модуляции
        t, fast = sine_signal(duration, frequency_of_signal * 16, sampling_rate)
        t, slow = sine_signal(duration, frequency_of_signal * 8, sampling_rate)
        for i, el in enumerate(p):
            if el == 0:  # если импульсный сигнал равен 0, то заполняем низкочастотным гармоническим
                m.append(slow[i])
            else:  # если наоборот, заполняем высокочастотным
                m.append(fast[i])
    if modulation == 'phase':  # для фазовой модуляции
        t, s = sine_signal(duration, frequency_of_signal * 16, sampling_rate)
        for i, el in enumerate(p):  # меняем фазу при каждом изменении импульсного сигнала
            if el != 0:
                m.append(s[i])
            else:
                m.append(s[i] * -1)
    return t, np.array(m)  # возвращаем временную шкалу и модулированный сигнал
