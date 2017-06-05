# logs_analysis
Udacity project demonstrating using python 3 to query PostgreSQL. This program is used
to query for statistics from a PostgreSQL database named `news`, which is expected
to have the table structure defined in `schema.sql`.

NOTE: If you are a Udacity Reviewer, you will not need to run the commands in `schema.sql`
the tables should already be defined for you.

## Usage

This project uses the `psycopg2` module. If necessary, this can be installed using:

	pip install psycopg2

To execute, run the following command.

	python logs_analysis.py

You will be immediately prompted for the username and password to connect to the `news`
database.

NOTE: If you are a Udacity Reviewer, you will need to use `vagrant` as the username
and leave the password blank.

	Enter username: scott
	Enter password: tiger

Afterwards, you will be presented with the following usage statistics:

	Most popular articles:
	
	"Candidate is jerk, alleges rival" - 338647 views
	"Bears love berries, alleges bear" - 253801 views
	"Bad things gone, say good people" - 170098 views
	
	Number of views per author:
	
	Ursula La Multa - 507594 views
	Rudolf von Treppenwitz - 423457 views
	Anonymous Contributor - 170098 views
	
	Days with high amount of error:
	
	July 17, 2016 - 2.28% errors
