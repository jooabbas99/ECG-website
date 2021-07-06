from django.db import models

# Create your models here.
from os.path import join


class ECGFile(models.Model):
    ARRHYTHMIA_CHOICE = (
        (0, 'Normal beat'),
        (1, 'Left bundle branch block beat'),
        (2, 'Premature ventricular contraction'),
        (3, 'Right bundle branch block beat'),
        (4, 'Atrial premature beat'),
    )
    arythmia_type = models.CharField(choices=ARRHYTHMIA_CHOICE, max_length=50,
                                     null=True, blank=True)
    patient = models.ForeignKey('Patient',on_delete=models.CASCADE)
    signal = models.ImageField(upload_to='media/')




class Patient(models.Model):
    name = models.CharField(max_length=100)
    birth_day = models.DateField()
    def get_path_upload(self,instance):
        return join("media", str(self.name), 'ECG Signal', instance)

    email = models.EmailField()
    ecg_signal = models.FileField(upload_to=get_path_upload)
    added = models.TimeField(auto_now_add=True)
    added = models.DateField(auto_now_add=True)   
    gender = models.CharField(max_length=10)
    def __str__(self):
        return str(self.name)
    
