from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import Restarted
from collections import OrderedDict
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import zomatopy
import json, pprint
import time

email_df = pd.DataFrame()

class ActionSearchRestaurants(Action):
	def name(self):
		return "action_search_restaurants"
	
	
	def run(self, dispatcher, tracker, domain):
		global email_df
		email_df = pd.DataFrame()
		config={ "user_key":"1190678ee10064714cf325c13c20b9c2"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
        # In zomato api if price_range_index == 1 then the average cost for two <300
		#               if price_range_index == 2 then the 300 <= average cost for two <=700
		#               if price_range_index == 3 then  average cost for two > 700
		# so we will map our budget values accordingly in below code 

		
		
		
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'chinese':25,'italian':55,'north indian':50,'south indian':85, 'mexican': 73, 'american': 1}
		resp_msg=""
		restaurant_name,restauarnt_addr,avg_budget_2,rating=[],[],[],[]
		t0= time.time()
		results=zomato.restaurant_search("", lat, lon, cuisine,100)#get first 20 and filter budget later
		d = json.loads(results)
		if d['results_found'] != 0:
			for restaurant in d['restaurants']:
				restaurant_name.append(restaurant['restaurant']['name'])
				restauarnt_addr.append(restaurant['restaurant']['location']['address'])
				rating.append(restaurant['restaurant']['user_rating']['aggregate_rating'])
				avg_budget_2.append(restaurant['restaurant']['average_cost_for_two'])
				
		
		
		# sort restarants on aggregate rating
		restaurant_df=pd.DataFrame({'Restaurant Name':restaurant_name,'Restaurant Locality Address':restauarnt_addr,'Average budget for two people':avg_budget_2,'Zomato user rating':rating})
		restaurant_df['Zomato user rating'] = restaurant_df['Zomato user rating'].apply(pd.to_numeric)  
		
		if budget == 'lesser': restaurant_df=restaurant_df[restaurant_df['Average budget for two people'] < 300]
		if budget == 'between': restaurant_df=restaurant_df[(restaurant_df['Average budget for two people'] >= 300) & (restaurant_df['Average budget for two people'] <= 700)]
		if budget == 'higher': restaurant_df=restaurant_df[restaurant_df['Average budget for two people'] > 700]


		restaurant_df = restaurant_df.sort_values("Zomato user rating",ascending=False)
		rest_df = restaurant_df.head(5)
		email_df=restaurant_df.head(10)
		rest_df = rest_df.reset_index(drop=True)
		rest_df.index = rest_df.index.map(str)
		
		if d['results_found'] == 0:
			resp_msg = 'No restaurants found in the given budget. Kindly increase your budget'
			return[SlotSet('budget',None)]
		else:
			for index, row in rest_df.iterrows():
				resp_msg = index + resp_msg + "{} in {} has been rated {}".format(
                row['Restaurant Name'],
                row['Restaurant Locality Address'],
                row['Zomato user rating']) + "\n"
	
		dispatcher.utter_message("-----"+resp_msg)
		t1=time.time()
		print('Execution time for fetching {:.4f}'.format(t1-t0))
		return [SlotSet('budget',budget)]
			
			

class ActionCheckLocation(Action):
	def name(self):
		return "action_check_location"
		
	def run(self, dispatcher, tracker, domain):
		list_loc = ["ahmedabad", "bangalore", "chennai", "delhi", "hyderabad", "kolkata", "mumbai", "pune", "agra", "ajmer", "aligarh", "amravati", "amritsar", "asansol", "aurangabad", "bareilly", "belgaum", "bhavnagar", "bhiwandi", "bhopal", "bhubaneswar", "bikaner", "bokaro steel city", "chandigarh", "coimbatore", "cuttack", "dehradun", "dhanbad", "durg-bhilai nagar", "durgapur", "erode", "faridabad", "firozabad", "ghaziabad", "gorakhpur", "gulbarga", "guntur", "gurgaon", "guwahati‚ gwalior", "hubli-dharwad", "indore", "jabalpur", "jaipur", "jalandhar", "jammu", "jamnagar", "jamshedpur", "jhansi", "jodhpur", "kannur", "kanpur", "kakinada", "kochi", "kottayam", "kolhapur", "kollam", "kota", "kozhikode", "kurnool", "lucknow", "ludhiana", "madurai", "malappuram", "mathura", "goa", "mangalore", "meerut", "moradabad", "mysore", "nagpur", "nanded", "nashik", "nellore", "noida", "palakkad", "patna", "pondicherry", "prayagraj", "raipur", "rajkot", "rajahmundry", "ranchi", "rourkela", "salem", "sangli", "siliguri", "solapur", "srinagar", "sultanpur", "surat", "thiruvananthapuram", "thrissur", "tiruchirappalli", "tirunelveli", "tiruppur", "ujjain", "bijapur", "vadodara", "varanasi", "vasai-virar city", "vijayawada", "visakhapatnam", "warangal"]
		loc = tracker.get_slot('location')
		#dispatcher.utter_message(loc)
		if loc is not None:
			if loc.lower() in list_loc:
				return[SlotSet('location',loc)]
			else:
				dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
				return[SlotSet('location',None)]
		else:
			dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
			return[SlotSet('location', None)]

class ActionCheckCuisine(Action):
	def name(self):
		return "action_check_cuisine"
	
	def run(self, dispatcher, tracker, domain):
		cuisine_types = ["chinese","mexican","american","italian","south indian","north indian"]
		cuisine = tracker.get_slot('cuisine')
		if cuisine is not None:
			if cuisine.lower() in cuisine_types:
				
				return[SlotSet('cuisine',cuisine)]
			else:
				dispatcher.utter_message("Sorry this is cuisine is not avialable. Kindly try some other cuisine")
				return[SlotSet('cuisine',None)]
		else:
			dispatcher.utter_message("Sorry I did'nt get you. Please try some other cuisine")
			return[SlotSet('cuisine', None)]


class ActionCheckEmail(Action):
	def name(self):
		return "action_check_email"
		
	def run(self, dispatcher, tracker, domain):
		
		email_validate = tracker.get_slot('email')
		#dispatcher.utter_message(email_validate) 
		if email_validate is None:
			dispatcher.utter_message("Kindly enter valid email id")
			return[SlotSet('email', None)]	

		if bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email_validate))==True:
			 return[SlotSet('email',email_validate)]	
		elif bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email_validate))==False:
			dispatcher.utter_message("This is not a valid email. Kindly check for any typo")
			return[SlotSet('email',None)]
		else:
			dispatcher.utter_message("Sorry it seems like an invalid email address which you provided? Please check for any typing errors")
			return[SlotSet('email', None)]	

		
		
			
class ActionSendEmail(Action):
	def name(self):
		return "action_send_email"	
			
	def run(self, dispatcher, tracker, domain):
		global email_df 

		
			
		email = tracker.get_slot('email')
		gmail_user = 'manu.siddhartha289@gmail.com' 
		gmail_password = 'S1ddh@rth@' 
		sent_from = gmail_user  
		to = str(email)
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Restaurant Details Queried on Foodie"
		msg['From'] = gmail_user
		msg['To'] = to
		if len(email_df) != 0:
			email_df = email_df.reset_index(drop=True)
			email_df.index = email_df.index.map(str)
			
			html = """
			<html>
			<head>
			<style>
			table {
				font-family: arial, sans-serif;
				border-collapse: collapse;
				width: 100%;
			}
			td, th {
				border: 1px solid #00008b;
				text-align: left;
				padding: 6px;
			}
			tr:nth-child(even) {
				background-color: #ffffff;
			}
			</style>
			</head>
			<body>
			<p>Hi!</p>
			<p>Thanks for using Foodie. Below is the requested list of restaurants in your location.</p>
			"""	
			html = html+email_df.to_html()
		part2 = MIMEText(html, 'html')
		msg.attach(part2)
		server = smtplib.SMTP_SSL('smtp.gmail.com',465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, msg.as_string())
		server.close()
		dispatcher.utter_message("Sent. Bon Appetit!")
		return [SlotSet('email',email)]		

class ActionRestarted(Action): 	
	def name(self): 		
		return "action_restarted" 	
	def run(self, dispatcher, tracker, domain): 
		return[Restarted()] 
