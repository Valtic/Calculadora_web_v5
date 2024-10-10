from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField,DecimalField,FloatField,SelectField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError


class feetMeters(FlaskForm):
    feets = IntegerField('Feets', validators=[DataRequired()])
    inchs = DecimalField('Inchs', validators=[DataRequired()])
    resultado = StringField('Resultado', render_kw={'readonly': 'True'})
    submit = SubmitField('Calcula')

class presionForm(FlaskForm):
    pres_origen = FloatField('Origin Value', validators=[DataRequired()])
    unidad = SelectField('Unidad', choices=[('Bar', 'bar'), ('Psi', 'psi')], validators=[DataRequired()])
    submit = SubmitField('Calcula')




