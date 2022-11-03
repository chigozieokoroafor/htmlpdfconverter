from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length, DataRequired
from wtforms import StringField, BooleanField, DateField, RadioField, SelectField, TextAreaField, EmailField, SubmitField
import datetime
import email_validator

#, Length(max=5)



class UserDetails(FlaskForm):
    #personal data
    fullname = StringField("Full Name", validators=[InputRequired()])
    dob = DateField("Date Of Birth", validators=[InputRequired()])
    nationality = SelectField("Nationality", validators=[InputRequired()], choices=["Afghanistan","Albania","Aland Island","Algeria","American-Samoa","Andorra","Angola","Anguilla","Antigua-Barbuda",
    "Argentina","Armenia",
    "Aruba",
    "Ascension Island",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bermuda",
    "Bhutan",
    "Bolivia",
    "Bosnia-Herzegovina",
    "Botswana",
    "Brazil",
    "British Indian Ocean Territory",
    "Brunei Darussalam",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cape Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cayman Islands"
    "Central African Republic",
    "Carribean Neatherlands", 
    "Chad",
    "Chile",
    "China",
    "Christmas Island",
    "Cocos (Keeling) Islands",
    "Colombia",
    "Comoros",
    "Congo",
    "Congo, Dem. Republic",
    "Cook Islands",
    "Costa Rica",
    "Croatia",
    "Cuba",
    "Curaçao","Cyprus",
    "Czechia",
    "Côte d'Ivoire",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "Ecuador",
    "East Timor",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Falkland Islands (Malvinas)",
    "Faroe Islands",
    "Fiji","Finland"
    "France",
    "French Guiana",
    "French Polynesia",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Gibraltar",
    "Greece",
    "Greenland",
    "Grenada",
    "Guadeloupe (French)",
    "Guam (USA)",
    "Guatemala",
    "Guernsey",
    "Guinea",
    "Guinea Bissau",
    "Guyana",
    "Haiti",
    "Heard Island and McDonald Islands",
    "Honduras",
    "Hong Kong",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq","Ireland"])
    phone = StringField(validators=[InputRequired()])
    gender = SelectField(validators=[DataRequired()], choices=['Male', "Female", "Prefer Not To Say"])
    marital_status = SelectField(validators=[DataRequired()], choices=["Single", "Married", "Divorced"], name="marital_status")
    res_address = TextAreaField(validators=[DataRequired()])
    primary_email= EmailField(validators=[InputRequired(), Email()])
    alternate_email= EmailField(validators=[Email()])
    children_ages = TextAreaField(validators=[DataRequired()])
    res_Address_kin = TextAreaField(validators=[InputRequired()])
    primary_email_kin= EmailField(validators=[Email()])
    alternate_email_kin= EmailField(validators=[Email()])
    phone_kin = StringField(validators=[InputRequired()])



    #Duty Data
    start_date = DateField(validators=[DataRequired()])
    start_rank = StringField(validators=[DataRequired()])
    current_rank = StringField(validators=[DataRequired()]) 
    salary_grade_current = StringField(validators=[DataRequired()])
    appointmentConfirmation_date = DateField(validators=[DataRequired()])
    lastPromotion_date = DateField(validators=[DataRequired()])
    faculty_dir = StringField(validators=[DataRequired()])
    dept_Unit = StringField(validators=[DataRequired()])
        
    
    #Natio = SelectField(validators=[DataRequired()], choices=['Male', "Female", "Prefer Not To Say"])
    #submit = SubmitField(validators=[InputRequired()])


class EducationalBackground(FlaskForm):
    #forinstitutions
    institution = TextAreaField(validators = [DataRequired()])
    start_year = SelectField(choices=[i for i in range(1700, (datetime.datetime.now().year + 1))])
    end_year = SelectField(choices=[i for i in range(1700, (datetime.datetime.now().year + 1))])

    #AcademicQual
    degree_distinction = StringField(validators=[DataRequired()])
    degree_date = DateField(validators=[InputRequired()])
    