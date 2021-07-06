from django.shortcuts import render 
from django.shortcuts import get_object_or_404
# Create your views here.
from .prediction.utilts import segmentation, filter_data, predict_model_class, scale_data, read_signal, plot_ecg_results
from .models import Patient,ECGFile
from django.views import View


class apply(View):
    def post(self, request):
        fullname = request.POST['fullname']
        email = request.POST['email']
        gender = request.POST['gender']
        birthdaytime = request.POST['birthdaytime']
        file_ecg = request.FILES['file']
        patient = Patient(
            name=fullname,
            birth_day=birthdaytime,
            email=email,
            ecg_signal=file_ecg,
            gender=gender,
        )
        patient.save()

        signal = read_signal(patient.ecg_signal)
        filter = filter_data(data=signal)
        segment = segmentation(data=filter[0])
        print(len(segment[0]))
        print(segment[0])
        results = predict_model_class(data=segment)


        for i in range(len(segment)):
            plot_ecg_results(segment[i], results[i], patient.id)
            image_path = f'./media/signal_class/signal{patient.id}{results[i]}.png'
            ecg = ECGFile(arythmia_type=results[i],
                          patient=patient,
                          signal=image_path)
            ecg.save()
        ecg_result = ECGFile.objects.filter(patient=patient)
        context = {
            'ecg_result': ecg_result
        }
        return render(request,'result.html',context=context)

def apply_ecg(request):
    patient = Patient.objects.get(id=id)
    signal = read_signal(patient.ecg_signal)
    segment = segmentation(data=signal)
    filter = filter_data(data=segment)
    results = predict_model_class(data=filter)
    return render(results)

def home(request):
    return render(request,'index.html')
