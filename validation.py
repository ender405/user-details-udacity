# hold validation functions for date

# instructor answers

# def valid_month(month):
#     months = ['January','February','March','April','May','June','July','August','September','October','November','December']
#     if month.capitalize() in months:
#         return month.capitalize()

# def valid_year(year):
#     if year and year.isdigit():
#         year = int(year)
#     if year > 1900 and year < 2020: 
#             return year

# def valid_day(day):
#     if day and day.isdigit():
#         day = int(day)
#         if day >= 1 and day <= 31:
#             return int(day)

# my answers
import cgi
import re

def escape_html(s):
  return cgi.escape(s, quote = True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
  return USER_RE.match(username)

PASSWORD_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
  return PASSWORD_RE.match(password)

def valid_verify(password, verify):
  if password == verify:
    return verify
  else:
    return None

EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
def valid_email(email):
  if email == "":
    return True
  else:
    return EMAIL_RE.match(email)


def valid_month(month):
    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
    if month == "":
        return None
    valid_format = month[0].upper() + month[1:].lower()
    if valid_format in months:
        return valid_format
    else:
        return None

def valid_day(day):
    try:
        if isinstance(day, basestring) and int(day):
            if int(day) > 0 and int(day) < 32:
                return int(day)
            else:
                return None
        else:
            return None
    except ValueError:
        return None

def valid_year(year):
	if year and year.isdigit() and len(year) == 4:
	    if year[0:2] == '19' or year[0:2] == '20' and int(year) >= 1900 and int(year) <= 2020:
	        return int(year)
	    else:
	        return None
	else:
	    return None