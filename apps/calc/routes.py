from flask import render_template, redirect, url_for,session, abort, flash, request,\
    current_app, make_response
from flask_login import login_required, current_user
from flask_sqlalchemy import get_debug_queries
#from apps.calc import calc
from apps.calc import blueprint
from .forms import feetMeters,presionForm
from flask_login import login_required, current_user
from jinja2 import TemplateNotFound
#import calculadoras as cal

import math

@blueprint.route('/')
def route_default():
    return redirect(url_for('calc_blueprint.acerca'))

@blueprint.route('/feetMeter', methods=['GET', 'POST'])
@login_required
def feetMeter():
    form = feetMeters()
    result= None
    
    if(form.validate_on_submit()):
        feet_origen= float(form.feets.data)
        inchs_origen= float(form.inchs.data)

        result = f"{feet_origen*0.3048 + inchs_origen*0.0254:.2f}"

        # Almacenar los campos en la cookie
        session['feet_origen'] = feet_origen
        session['inchs_origen'] = inchs_origen
        session['resultado'] = result

        return redirect(url_for('calc_blueprint.feetMeter'))

    # Rellenar los campos entre el formulario
    if( (session.get('feet_origen') is not None) and (session.get('inchs_origen') is not None) and (session.get('resultado') is not None) ):

        form.feets.data = float(session.get('feet_origen'))
        form.inchs.data = session.get('inchs_origen')
        form.resultado.data = session.get('resultado')

    return render_template('calc/feetsMeters.html', form=form,result=session.get('resultado'),title='Feet to Meters Conversion')

@blueprint.route('/pressure', methods=['GET', 'POST'])
@login_required
def pressure():

    form = presionForm()

    if(form.validate_on_submit()):

        pres_origen= form.pres_origen.data
        unidad= form.unidad.data
        if unidad=='Psi':
            result_ = pres_origen/14.5038
            rusult_str = f"{result_:.2f}"+ " bar"
        else:
            result_= pres_origen*14.5038
            rusult_str = f"{result_:.2f}"+ " psi"
        session['resultado'] = rusult_str
        session['unidad']= unidad
        session['pres_origen'] = pres_origen

        return redirect(url_for('calc_blueprint.pressure'))

    # Rellenar los campos entre el formulario

    form.unidad.data = session.get('unidad')
    form.pres_origen.data = session.get('pres_origen')

    return render_template('calc/presion.html', form=form,result=session.get('resultado'),title='Pressure Conversion')


@blueprint.route('/acerca', methods=['GET', 'POST'])
def acerca():

    return render_template('calc/about.html')


@blueprint.route("/temperatura")
def temperatura():
    return render_template("calc/temperatura.html")


@blueprint.route("/potencia")
def potencia():
    return render_template("calc/potencia_elec.html")



@blueprint.route('/convert', methods=['POST'])
def convert():
    temperature = float(request.form['temperature'])
    unit = request.form['unit']

    if unit == 'celsius':
        converted_temperature = float(temperature) + 273.15
        result = f"{temperature:.2f} °C is equal to {converted_temperature:.2f} K"

    elif unit == 'kelvin':
        converted_temperature = float(temperature) - 273.15
        result = f"{temperature:.2f} K is equal to {converted_temperature:.2f} °C"
    else:
        result = 'Invalid unit'
  
    return render_template('calc/temperatura.html', result=result)


@blueprint.route('/convertpot', methods=['POST'])
def convertpot():
    
    intput_usage=90.0

    potencia_input = (float)(request.form['potencia'])
    unit = request.form['unit']
    input_volt= (float)(request.form['voltaje'])
    intput_pf_cos= ((float)(request.form['pf']))/100

    if unit == 'kw':
        
        # Perform calculations to Kw
        converted_potencia =(potencia_input*1000/((math.sqrt(3)*input_volt)*math.cos(intput_pf_cos)))    
        result = f'{potencia_input} kw is equal to {converted_potencia:.2f} A'
        
    elif unit == 'amp':
        # Perform calculations to Amp(I)
        converted_potencia = (math.sqrt(3)*input_volt*potencia_input*math.cos(intput_pf_cos) /1000) 
        result = f'{potencia_input} A is equal to {converted_potencia:.2f} Kw'
        
    else:
        result = 'Invalid unit'

    return render_template('calc/potencia_elec.html', result=result)
