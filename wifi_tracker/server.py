#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                                 WIFI Tracker                                  # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Enter and track good locations to work remotely from that have good wifi.             #
#                                                                                       #
# Setup & Requirements:                                                                 #
# rename project folder e.g. wifi_tracker: cd wifi_tracker                              #
# Install Virtual Environment on Windows: py -3 -m venv venv                            #
# Activate the environment: venv\Scripts\activate                                       #
# Install Flask: pip install Flask                                                      #
# Install Flask WTF: pip install -U Flask-WTF                                           #
# Install Flask Bootstrap: pip install Flask-Bootstrap                                  #
#                                                                                       #
# initiate/launch server:                                                               #
# $env:FLASK_APP = "server.py"                                                          #
# flask run                                                                             #
#                                                                                       #
# launch server in debug/development mode                                               #
# so it updates with changes requiring only browser refresh:                            #
# ctrl + c                                                                              #
# $env:FLASK_ENV = "development"                                                        #
# flask run                                                                             #
# in browser, view at path in terminal, usually: 127.0.0.1:5000                         #
#########################################################################################

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-your-own-flask-key-can-be-anything'
Bootstrap(app)


class LocationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    location = StringField("Location on Google Maps (URL)", validators=[
                           DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM",
                        validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[
                                "☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=[
                              "✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=[
                               "✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_location():
    form = LocationForm()
    if form.validate_on_submit():
        new_data = [form.data[item] for item in form.data][:7]
        new_row = ','.join(new_data)
        with open('location-data.csv', newline='', encoding="utf8", mode='a') as csv_file:
            csv_file.write('\n' + new_row)
        return redirect(url_for('locations'))
    return render_template('add.html', form=form)


@app.route('/locations')
def locations():
    with open('location-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('locations.html', locations=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
