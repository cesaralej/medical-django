import pydicom

def read_dicom(dicom_file):
    dicom_data = pydicom.dcmread(dicom_file)
    result = {}
    result[patient_name] = dicom_data.PatientName
    result[study_date] = dicom_data.StudyDate
    result[series_description] = dicom_data.SeriesDescription
    return result
