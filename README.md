
**ECG Classification Using CNN-1D**



The electrocardiogram (ECG) has become a useful tool for the diagnosis of cardiovascular diseases as it is fast and noninvasive. It has been reported that about 80% of sudden cardiac deaths are the result of ventricular arrythmia or irregular heartbeats, while an experienced cardiologist can easily distinguish arrythmias by visually referencing the morphological pattern of the ECG signals.

Today's computer-based approach can significantly shorten diagnostic time and allow for e-health monitoring of cardiovascular disease at home. Due to the time-varying dynamics and various profiles of ECG signals, which cause classification precision to vary from patient to patient, even for a healthy person, the morphological pattern of their ECG signals can vary significantly over a short time, beginning to realize such computer-oriented approaches remains challenging.

This project aims to identify, compare, analyze and implement Deep learning models with ECG arrhythmia classification. We address the problem of data by comparing the benchmark dataset to run over different Deep Learning algorithms.


Website Link https://ecgclassification.herokuapp.com/


**To Install**

    git clone https://github.com/jooabbas99/ECG-website.git
    cd ECG-website
    pyhton3 -m venv ./venv
    source venv/bin/activate
    pip install -r requirments.txt
    ./manage.py migrate
    ./manage.py runserver
## Note's
- this use Tensorflow 1.5 with Keras 2.2.5 
- django 3.2 
- the minimum time for signal is 5 second 
