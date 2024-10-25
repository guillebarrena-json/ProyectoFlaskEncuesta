from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import duckdb

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Cambia esto por una clave segura

class UserForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        fullname = form.fullname.data
        email = form.email.data

        # Conéctate a DuckDB y realiza la inserción
        con = duckdb.connect('C:\\Users\\usuario\\Desktop\\Proyectos\\GUILLE\\PGB\\Formulario Flask\\coffeecms.duckdb')

        # Obtener el siguiente user_id
        result = con.execute("SELECT MAX(user_id) FROM users").fetchone()
        next_user_id = result[0] + 1 if result[0] is not None else 1

        # Insertar el nuevo usuario
        con.execute("INSERT INTO users (user_id, fullname, email) VALUES (?, ?, ?)", (next_user_id, fullname, email))
        con.close()

        flash("Datos cargados correctamente!", "success")  # Mensaje de éxito

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
