import json
import requests
import datetime

token = "36c6de4f84921a4de705fe11639cd100"

def register():
	github = "https://github.com/abeljrenteria/code2040_py.git"
	url = "http://challenge.code2040.org/api/register"
	
	# Creates a dictionary 
	info = {'token' : token, 'github' : github}
 
	# Sends JSON dictionary to api and retrieves respose
	response = requests.post(url, json = info)

	print (response.text)

def reverseStr():
	url1 = "http://challenge.code2040.org/api/reverse"
	url2 = "http://challenge.code2040.org/api/reverse/validate"
	info = {"token" : token}

	# Sends JSON dictionary to api and retrieves the string
	response = requests.post(url1, json = info)
	o_g_string = response.text

	# Reverses the string
	string = o_g_string[::-1]

	# Updates the dictionary 
	info = {"token" : token, "string" : string}

	# Sends the updated dictionary with the reversed string back to API
	response = requests.post(url2, json = info)

	print (response.text)

def needleHaystack():
	url1 = "http://challenge.code2040.org/api/haystack"
	url2 = "http://challenge.code2040.org/api/haystack/validate"
	info = {"token" : token}

	# Sends JSON dictionary to api and retrieves both the Array and String
	response = requests.post(url1, json = info)

	data = response.json()
	needle = data["needle"]
	haystack = data["haystack"]

	# Finds position of needle in haystack array
	position = haystack.index(needle)

	# Updates dictionary 
	info = {"token" : token, "needle" : position}

	# Sends the updated dictionary with the position back to API
	response = requests.post(url2, json = info)

	print (response.text)

def prefix():
	url1 = "http://challenge.code2040.org/api/prefix"
	url2 = "http://challenge.code2040.org/api/prefix/validate"
	info = {"token" : token}

	# Sends JSON dictionary to api and retrieves both the Array and String
	response = requests.post(url1, json = info)
	
	data = response.json()
	prefix = data["prefix"]
	arrayReq = data["array"]

	# Creates an array 
	new_array = []

	# Goes through the given array and finds the strings that do not start with the prefix then 
	# stores them in the new array
	for a in arrayReq[:]:
		if not a.startswith(prefix):
			new_array.append(a)

	info = {"token" : token, "array" : new_array}

	response = requests.post(url2, json = info)

	print (response.text)

def datingGame():
	url1 = "http://challenge.code2040.org/api/dating"
	url2 = "http://challenge.code2040.org/api/dating/validate"
	info = {"token" : token}

	# Sends JSON dictionary to api and retrieves both the iso8601 datestamp and interval
	response = requests.post(url1, json = info)

	data = response.json()
	datestamp = data["datestamp"]
	interval = data["interval"]

	# Changes the string datestamp to a datetime object
	date = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
	
	# Has interval using timedelta class of seconds to be able to add to date
	seconds = datetime.timedelta(seconds = interval)
	new_date = date + seconds
	# Changes back to datestamp string
	new_date_str = new_date.strftime('%Y-%m-%dT%H:%M:%SZ')

	info = {"token" : token, "datestamp" : new_date_str}

	response = requests.post(url2, json = info)

	print (response.text)

def main():
	register()
	reverseStr()
	needleHaystack()
	prefix()
	datingGame()

main()
