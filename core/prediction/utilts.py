# import pywt

# import ecg_plot
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from os import listdir
# from biosppy.signals import ecg , tools
# import os

# import scipy
# from sklearn import preprocessing
# from keras.models import Model, load_model
# import keras
# from django.conf import settings


# def compute_wavelet_descriptor(beat, family, level):
#     wave_family = pywt.Wavelet(family)
#     coeffs = pywt.wavedec(beat, wave_family, level=level)
#     return coeffs[0]


# def segmentation(data):
#     signals = []
#     count = 1
#     peaks = ecg.hamilton_segmenter(signal=data, sampling_rate=300)[0]
#     peaks, = ecg.correct_rpeaks(signal=data,
#                              rpeaks=peaks,
#                              sampling_rate=300,
#                              tol=0.05)
#     for i in (peaks[1:-1]):

#         diff1 = abs(peaks[count - 1] - i)
#         diff2 = abs(peaks[count + 1] - i)
#         x = peaks[count - 1] + diff1//2
#         y = peaks[count + 1] - diff2//2
#         signal = data[x:y]
#         signal = scipy.signal.resample(signal, 300)
#         signals.append(signal)
#         count += 1

#     return signals


# def scale_data(data, lower=0, upper=1):
#     '''scales passed sequence between thresholds

#     Function that scales passed data so that it has specified lower 
#     and upper bounds.
    
#     Parameters
#     ----------
#     data : 1-d array or list
#         Sequence to be scaled

#     lower : int or float
#         lower threshold for scaling
#         default : 0

#     upper : int or float
#         upper threshold for scaling
#         default : 1024

#     Returns
#     -------
#     out : 1-d array
#         contains scaled data

#     Examples
#     --------
#     When passing data without further arguments to the function means it scales 0-1024
    
#     >>> x = [2, 3, 4, 5]
#     >>> scale_data(x)
#     array([   0.        ,  341.33333333,  682.66666667, 1024.        ])

#     Or you can specify a range:

#     >>> scale_data(x, lower = 50, upper = 124)
#     array([ 50.        ,  74.66666667,  99.33333333, 124.        ])
#     '''

#     rng = np.max(data) - np.min(data)
#     minimum = np.min(data)
#     data = (upper - lower) * ((data - minimum) / rng) + lower
#     return data


# def filter_data(data, sampling_rate=300):
#     sampling_rate = float(sampling_rate)
#     # filter signal
#     order = int(0.3 * sampling_rate)
#     filter_data = np.zeros((len(data), len(data[0])))
#     for i, (xrow) in enumerate(data):
#         filtered, _, _ = ecg.st.filter_signal(signal=xrow,
#                                               ftype='FIR',
#                                               band='bandpass',
#                                               order=order,
#                                               frequency=[3, 45],
#                                               sampling_rate=sampling_rate)

#         scaled = scale_data(filtered, lower=0, upper=1)
#         filter_data[i] = scaled
#     return filter_data


# def predict_model_class(data, model_path='./core/prediction/model_cnn1d_scaled_final_sequential.h5', load_weights_path='./core/prediction/CNN1DbestEpochMin.hdf5'):
#     data = np.array(data)
#     x = data.reshape(len(data), data.shape[1], 1)
#     print("x", x)
#     model = load_model(model_path)
#     print("model")
#     model.load_weights(load_weights_path)
#     print("load_weights")

#     results = model.predict_classes(x)
#     print(results)
#     return results


# def read_signal(csv_path):
#     data = pd.read_csv(csv_path)
#     return data.to_numpy()

# def plot_ecg_results(signal, signal_class, s_id):
#     ecg_plot.plot_1(signal, fig_height=15, fig_width=5,
#                     line_w=1, ecg_amp=1.5, title=signal_class)
#     ecg_plot.save_as_png(
#         f'signal{s_id}{signal_class}', './media/signal_class/')
