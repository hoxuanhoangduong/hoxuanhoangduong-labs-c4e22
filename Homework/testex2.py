from random import choice
symptom_disease = {
    'Đau bụng': 'Tiêu chảy',
    'Đau đầu': 'Thương hàn',
    'Đau toàn thân': 'Bách độc công tâm',
}
symptom, disease = choice(list(symptom_disease.items()))
print(symptom )
print(disease)

