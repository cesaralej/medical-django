from django.shortcuts import render
from django.http import HttpResponse
from scripts.dicom_reader import read_dicom
from scripts.dynalogs_reader import read_dynalog
from datetime import datetime

dicom_file_path = ["data/Oncentra Prostate Image Series-US-1-001.dcm", "data/0002.DCM"]
dynalog_file_path = ["data/logs/A20230215192350_2100EX20 (1).dlg"]

def index(request):
    #return HttpResponse("Hello, world")
    payload = {}
    payload['pname'] = read_dicom(dicom_file_path[0])['patient_name']
    date_string = read_dicom(dicom_file_path[0])['study_date']
    payload['sdate'] = datetime.strptime(date_string, '%Y%m%d')
    payload['sdesc'] = read_dicom(dicom_file_path[0])['series_description']
    payload['actual'] = read_dynalog(dynalog_file_path[0])['actual']
    payload['expected'] = read_dynalog(dynalog_file_path[0])['expected']
    payload['chart_image'] = read_dynalog(dynalog_file_path[0])['chart_image']
    payload['dicom_path'] = dicom_file_path[0]
    payload['dynalog_path'] = dynalog_file_path[0]

    return render(request, 'index.html', payload)






