Python Projects
===============
These are just projects that I am writing in my spare time to get better aquanted with python as a programming language. Definitely willing to take any criticism to help get better, so feel free to shoot over any pull requests.

weather.py
----------
	usage: weather.py [-h] -z ZIPCODE

	Show the 10 day forecast

	optional arguments:
	-h, --help			show this help message and exit
	-z ZIPCODE, --zipcode ZIPCODE
						zipcode of the area to retrieve the forecast for

./weather.py 10001

	+------------+------------+---------------+--------------+--------------+--------------+---------------+--------------+--------------+--------------+---------------+
	|    Date    | 2015.04.09 |   2015.04.10  |  2015.04.11  |  2015.04.12  |  2015.04.13  |   2015.04.14  |  2015.04.15  |  2015.04.16  |  2015.04.17  |   2015.04.18  |
	+------------+------------+---------------+--------------+--------------+--------------+---------------+--------------+--------------+--------------+---------------+
	|    High    |  42.17°F   |    63.41°F    |   54.46°F    |   52.39°F    |   54.41°F    |    55.54°F    |   51.17°F    |   61.36°F    |   67.57°F    |    61.23°F    |
	|    Low     |  42.17°F   |    41.47°F    |   44.24°F    |   37.33°F    |   39.61°F    |    42.69°F    |   42.31°F    |   46.63°F    |   49.01°F    |    43.79°F    |
	|  Forecast  | light rain | moderate rain | sky is clear | sky is clear | sky is clear | moderate rain | sky is clear | sky is clear | sky is clear | moderate rain |
	|  Humidity  |    89%     |      96%      |     84%      |      0%      |      0%      |       0%      |      0%      |      0%      |      0%      |       0%      |
	| Wind Speed |  6.61 MPH  |    3.28 MPH   |   6.52 MPH   |   2.7 MPH    |   6.46 MPH   |    6.89 MPH   |  12.23 MPH   |   7.37 MPH   |   8.01 MPH   |    7.43 MPH   |
	+------------+------------+---------------+--------------+--------------+--------------+---------------+--------------+--------------+--------------+---------------+

rps.py (Rock, Paper, Scissors)
------------------------------
	usage: rps.py

	Ready to play a game?[y/n] y
	Please choose (r)ock, (p)aper, (s)cissors: r
	+-----------+--------------------+
	|   Score   | Player (0 - 0) CPU |
	+-----------+--------------------+
	| CPU Picks |        rock        |
	|  Results  |     It's a tie     |
	+-----------+--------------------+
	How about another round?[y/n]

high_low.py
-----------
	usage: high_low.py

	Would you like to play a game?[Y/n] y
	Pick a number between 0-99: 10
	Guess Higher...
	Pick a number between 0-99: 58
	Guess Lower...
	Pick a number between 0-99: 56
	Guess Higher...
	Pick a number between 0-99: 57
	Guess Lower...
	You guess correctly and it only took 4 guess(es)!
	Would you like to play again?[Y/n]
