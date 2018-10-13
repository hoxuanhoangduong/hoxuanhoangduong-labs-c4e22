from gmail import  GMail, Message
gmail = GMail('hxhteng4394@gmail.com','hoangduong4394')
html_template = '''
<p>Ch&agrave;o anh ,</p>
<p>H&ocirc;m nay bỗng dưng long thể bất an, <strong>{{ disease }}</strong> .</p>
<p>Em mạnh dạn dự đo&aacute;n l&agrave; bị <strong>{{ symptom }}</strong> cần chuyền nội y .</p><p>Do vậy em xin nghỉ h&ocirc;m nay .</p>
<p>Học sinh của anh</p>
<p>&nbsp;</p>
'''

from random import choice
symptom_disease = {
    'Đau bụng': 'Tiêu chảy',
    'Đau đầu': 'Thương hàn',
    'Đau toàn thân': 'Bách độc công tâm',
}
symptom, disease = choice(list(symptom_disease.items()))
html_content = html_template.replace("{{ symptom }}", choice(symptom))
html_content = html_template.replace("{{ disease }}", choice(disease))
msg = Message('LAB1',to = 'hxhteng4394@gmail.com',html = html_content)
mail.send(msg)