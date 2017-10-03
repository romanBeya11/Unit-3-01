'''
Created by: Roman Beya
Created on: 3-oct-2017
Created for: ICS3U
This program determines whether or not the number guessed by a user is the correct number stored as a constant in memory
'''

import ui

# constants
number_stored_in_memory = 5

def calculate_number_of_students_touch_up_inside(sender):
	# determines whether the input is equal to the constant number stored in memory
	# input
	number_guessed = int(view['guess_textfield'].text)
	# process
	if number_guessed == number_stored_in_memory:
		# output
		view['output_label'].text = "You guessed the correct number: 5"
	
	
view = ui.load_view()
view.present('sheet')
