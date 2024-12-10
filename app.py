from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField  # เปลี่ยน TextField เป็น StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ")
    submit = SubmitField("บันทึก")

@app.route('/', methods=['GET','POST']) #ชื่อ route
def index():
    name= False
    form=MyForm()
    if form.validate_on_submit():
        name = form.name.data
    return render_template("index.html",form=form,name=name)


#if __name__ == "__main__":
#    app.run(debug=True)
    

