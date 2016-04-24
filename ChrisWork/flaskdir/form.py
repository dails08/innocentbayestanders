from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField

class ContactForm(Form):
  name = TextField("Name")
  salary = TextField("Salary")
  submit = SubmitField("Form")