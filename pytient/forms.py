from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField
from models import Register_patient

class PatientForm(Form):
    nome = StringField(u'Nome')
    rg = StringField(u'RG: 9.999.999-99')
    nascimento = StringField(u'Nascimento: dd/mm/aaaa')
    # endereco = StringField(u'Rua/Av./Travessa/')
    # numero = StringField(u'99999')
    # complemento = StringField(u'Apto./Cond./Sitio/')
    # bairro = StringField(u'Bairro')
    # convenio = StringField(u'Unimed/Agemed/Particular/')
    # exame = StringField(u'Musculo/Trans vaginal/')
    # valor = StringField(u'120,00')
    cadastrar = SubmitField(u'Cadastrar')
