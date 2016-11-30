# Code2040 Technical Assessment

The next step in the Code2040 application process is the Technical Assessment. The Technical Assessment is an API challenge with the goal of showcasing our coding abilities by completing 5 programming challenges presented by Code2040. In order to complete this challenge I chose to use the Python programming language.

<HR SIZE="1">

<h3>Step I - Registration</h3>
In this first challenge the objective was to connect to the registration endpoint, http://challenge.code2040.org/api/register. 

The registration endpoint expects a JSON dictionary with two keys, token and github. This JSON should be sent in the body of your HTTP request.

For token, pass in a string with the token you see above. For github, pass in the URL of the repository you created in the last step.

<h3>Step II - Reverse a String</h3>
In this step the objective is to reverse a string provided by the API. For example if the API says 'cupcake' I would send back 'ekacpuc'.
POST a JSON dictionary with the key token and your token value to this endpoint: http://challenge.code2040.org/api/reverse

This endpoint will return a string that your code should then reverse, as in the example above. Once that string is reversed, send it back to us. POST some JSON to: http://challenge.code2040.org/api/reverse/validate

Use the token for your token. Use the key string for your reversed string.


<h3>Step III - Needle in a Haystack</h3>
In this step we will now be working with collections.

We’re going to send you a dictionary with two values and keys. The first value, needle, is a string. The second value, haystack, is an array of strings. You’re going to tell the API where the needle is in the array.

Grab that dictionary from here, again by POSTing your token: http://challenge.code2040.org/api/haystack

Locate the needle in the haystack array. You’re going to send back the position, or “index,” of the needle string. The API expects indexes to start counting at 0.

POST your results to: http://challenge.code2040.org/api/haystack/validate

Use the key token for your token. Use the key needle for the integer representing where the needle was in the array.

<h3>Step IV - Prefix</h3>
In this challenge, the API is going to give you another dictionary. The first value, prefix, is a string. The second value, array, is an array of strings. Your job is to return an array containing only the strings that do not start with that prefix.

Note: The strings in your array should be in the same order as in the original array. POST your token here: http://challenge.code2040.org/api/prefix

Once you’ve built your array, POST a dictionary here: http://challenge.code2040.org/api/prefix/validate

Use the key token for your token. Use the key array for your array.


<h3>Step V - The Dating Game</h3>
This last step involves working with dates and times.

The API will again give you a dictionary. The value for datestamp is a string, formatted as an ISO 8601 datestamp. The value for interval is a number of seconds.

You’re going to add the interval to the date, then return the resulting date to the API. POST your token here: http://challenge.code2040.org/api/dating

Then POST a dictionary with your results here: http://challenge.code2040.org/api/dating/validate

Use the key token for your token. Use the key datestamp for an ISO 8601 datestamp string.
