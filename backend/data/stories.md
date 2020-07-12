## complete path - Full sequence
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location 
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "higher"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "higher"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted


## complete path 2 - With no email in the end
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_check_cuisine
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "lesser"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* deny
    - utter_goodbye
    - action_restarted

## complete path 3 - location specified initially
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "between"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "between"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 4 - Cuisine not available
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Bengali"}
    - slot{"cuisine": "Bengali"}
    - action_check_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_check_cuisine
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "between"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "between"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 5 - Unavailable Location deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kerala"}
    - slot{"location": "Kerala"}
    - action_check_location
    - slot{"location": null}
* deny
    - utter_goodbye
    - action_restarted

## complete path 6 - Unavailable Cuisine deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mughlai"}
    - slot{"cuisine": "Mughlai"}
    - action_check_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* deny
    - utter_goodbye
    - action_restarted

## complete path 7 - Unavailable Location continue
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bidhannagar"}
    - slot{"location": "Bidhannagar"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "between"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "between"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 8 - Unavailable Location and cuisine continue
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bidhannagar"}
    - slot{"location": "Bidhannagar"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - utter_ask_location
* restaurant_search{"cuisine": "Bengali"}
    - slot{"cuisine": "Bengali"}
    - action_check_cuisine
    - slot{"cuisine": null}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "lesser"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 9 - Budget not suitable deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* deny
    - utter_goodbye
    - action_restarted

## complete path 10 - Invalid email in the end
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "higher"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "higher"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"s@hotmail"}
    - slot{"email":"s@hotmail"}
    - action_check_email
    - slot{"email":null}
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 11 - No search needed deny
* greet
    - utter_greet
* deny
    - utter_default
* deny
    - utter_goodbye
    - action_restarted

## complete path 12 - Location and cuisine given altogether
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "higher"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "higher"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 13 - Location and budget given altogether
* greet
    - utter_greet
* restaurant_search{"budget": "cheapest", "location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - slot{"budget": "lesser"}
    - action_check_location
    - slot{"location": "Bangalore"}
    - slot{"budget": "lesser"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - slot{"budget": "lesser"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 14 - cuisine and budget given altogether
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "budget": "costly"}
    - slot{"cuisine": "American"}
    - slot{"budget": "higher"}
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "American"}
    - action_check_cuisine
    - slot{"cuisine": "American"}
    - slot{"location": "Lucknow"}
    - slot{"budget": "higher"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "higher"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 15 - mail given initially on asking
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "between"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "between"}
    - utter_ask_to_email
* affirm{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 16 - Location,Budget and cuisine given altogether
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "costly"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "higher"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"budget": "higher"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "higher"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 17 - Unavailable location specified initially
* greet
    - utter_greet
* restaurant_search{"location": "Kerala"}
    - slot{"location": "Kerala"}
    - action_check_location
    - slot{"location": null}
 * restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_check_cuisine
    - slot{"cuisine": "Chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "between"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "between"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 18 - Unavailable Location,Budget and cuisine given altogether
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Rishikesh", "budget": "economic"}
    - slot{"location": "Rishikesh"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "lesser"}
    - action_check_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"budget": "lesser"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* affirm
    - utter_ask_email_id
* send_email{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## complete path 19 - Location,Budget and cuisine given altogether with email initially
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "budget": "costly"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "higher"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - slot{"budget": "higher"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "higher"}
    - utter_ask_to_email
* affirm{"email":"sid321axn@hotmail.com"}
    - slot{"email":"sid321axn@hotmail.com"}
    - action_check_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_send_email
    - slot{"email":"sid321axn@hotmail.com"}
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"budget": "lesser", "cuisine": "chinese", "location": "Kolkata"}
    - slot{"budget": "lesser"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - action_check_location
    - slot{"location": "Kolkata"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* send_email{"email": "sid321axn@gmail.com"}
    - slot{"email": "sid321axn@gmail.com"}
    - actions.ActionCheckEmail
    - action_check_email
    - slot{"email": "sid321axn@gmail.com"}
    - action_send_email
    - slot{"email": "sid321axn@gmail.com"}
    - action_restarted

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser"}
    - slot{"budget": "lesser"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* deny
    - utter_goodbye
    - action_restarted

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - action_check_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "lesser"}
    - slot{"budget": "lesser"}
    - utter_top_5_restaurant
    - action_search_restaurants
    - slot{"budget": "lesser"}
    - utter_ask_to_email
* deny
    - utter_goodbye
    - action_restarted
