from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
import duckdb

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave segura

from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define the form with additional fields
class UserForm(FlaskForm):
    # Datos de Identificación
    nombre_empresa = StringField('Nombre o razón social de la empresa', validators=[DataRequired()])
    nombre_fantasia = StringField('Nombre de Fantasía', validators=[DataRequired()])
    cuit = IntegerField('CUIT', validators=[DataRequired()])
    direccion_establecimiento = StringFieladdd('Dirección del Establecimiento Industrial', validators=[DataRequired()])
    direccion_administracion = StringField('Dirección de la Administración', validators=[DataRequired()])
    partido_localidad = StringField('Partido o Localidad Est. Industrial', validators=[DataRequired()])
    actividad_principal = StringField('Actividad principal', validators=[DataRequired()])
    
    # Datos del Respondente de la Encuesta
    nombre_respondente = StringField('Nombre y Apellido', validators=[DataRequired()])
    cargo_area = StringField('Cargo/Área', validators=[DataRequired()])
    tipo_telefono = StringField('Tipo de Teléfono (Particular/corporativo)', validators=[DataRequired()])
    numero_telefono = IntegerField('N°', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    # Submit button
    submit = SubmitField('Enviar')

# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        nombre = form.nombre.data
        fantasia = form.fantasia.data
        cuit = form.cuit.data

        # Connect to DuckDB and insert data
        con = duckdb.connect('C:\\Users\\usuario\\Desktop\\Proyectos\\GUILLE\\PGB\\Formulario Flask\\coffeecms.duckdb')

        # Get the next user_id
        result = con.execute("SELECT MAX(user_id) FROM users").fetchone()
        next_user_id = result[0] + 1 if result[0] is not None else 1

        # Insert new user
        con.execute("INSERT INTO users (user_id, nombre, fantasia, cuit) VALUES (?, ?, ?, ?)", (next_user_id, nombre, fantasia, cuit))
        con.close()

        flash("Datos cargados correctamente!", "success")  # Success message

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
