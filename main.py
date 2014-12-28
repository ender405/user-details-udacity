#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
from validation import valid_month, valid_day, valid_year, escape_html, valid_password, valid_username, valid_email, valid_verify



form = """
<form method="post">
	Please enter your details
	<br>
	<label>
		Username
		<input type="text" name="username" value="%(username)s">
		<div style="color: red">%(error_username)s</div>
	</label>
	<label>
		Password
		<input type="password" name="password" value="%(password)s">
		<div style="color: red">%(error_password)s</div>
	</label>
	<label>
		Verify password
		<input type="password" name="verify" value="%(verify)s">
		<div style="color: red">%(error_verify)s</div>
	</label>
	<label>
		Email (optional)
		<input type="text" name="email" value="%(email)s">
		<div style="color: red">%(error_email)s</div>	
	</label>

	
	<br>
	<br>
	<input type="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):
    
    def write_form(self, 
    				username="", 
    				password="", 
    				verify="", 
    				email="", 
    				error_username="", 
    				error_password="", 
    				error_verify="", 
    				error_email=""):
    	
    	self.response.out.write(form % {"username" : escape_html(username), 
    									"password" : "", 
    									"verify" : "",
    									"email" : escape_html(email),
    									"error_username" : error_username,
    									"error_password": error_password,
    									"error_verify" : error_verify,
    									"error_email" : error_email,
    									})

    def get(self):
#        self.response.headers['Content-type'] = 'text/plain'
        self.write_form()


# need to fix the validation steps and figure out what to do with a null email
# need to figure out how to pass username into the redicrect to display names

    def post(self):

    	entry_username = self.request.get('username')
    	entry_password = self.request.get('password')
    	entry_verify = self.request.get('verify')
    	entry_email = self.request.get('email')


    	username = valid_username(entry_username)
    	password = valid_password(entry_password)
    	verify = valid_verify(entry_password, entry_verify)
    	email = valid_email(entry_email)

    	if (username and password and email):
    		self.redirect("/welcome")
    	else:
    		errors = ["", "", "", ""]
    		if not username:
    			errors[0] = "That's not a valid username."
    		if not password:
    			errors[1] = "That wasn't a valid password"
    		if not verify:
    			errors[2] = "Your two passwords don't match"
    		if not email:
    			errors[3] = "Your email isn't in the correct format"
    		self.write_form(entry_username, "", "", entry_email, errors[0], errors[1], errors[2], errors[3])

class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get('username')
		self.response.out.write("Welcome " + username + "!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
