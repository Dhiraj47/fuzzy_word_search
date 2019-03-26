# fuzzy_word_search
webseite link: http://dhiraj47.pythonanywhere.com/search/

This application is build on python(3.6).

To run this application on your system you will need following:
i) Django  (pip install django)
ii) fuzzywuzzy  (pip install fuzzywuzzy)
iii) levenshtein  (pip install python-Levenshtein)

How it works:
i) First user have to type/search a word in the input box where word length should be equal and greater then 3.
ii) on keyup event it calls an ajax request.
iii) Server takes the keyword and find the appropriate matching words related to string and return the response in JSON format.
iv) When frontend receive the data in json format it populates the result in a 'div' tag.
v) On clicking a particular, it populate the result to inputbox.
vi) after hitting enter or pressing search icon user can make a google search of that word.
