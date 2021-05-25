#!/bin/bash

DB_HOST=$1

# Set these variables to the username and password of a database user:
# with permissions to create users and databases
DBADMIN_NAME=$2
DBADMIN_PASSWORD=$3

# Set these variables to the name of the database to be created for the TIBCO Spotfire
# Server, and the user to be created for TIBCO Spotfire Server to access the database.
# Note that the password is entered here in plain text, you might want to delete
# any sensitive information once the script has been run.
SERVERDB_NAME=$4
SERVERDB_USER=$5
SERVERDB_PASSWORD=$6


echo $DB_HOST

echo $DBADMIN_NAME

echo $DBADMIN_PASSWORD

echo $SERVERDB_NAME

echo $SERVERDB_USER

echo $SERVERDB_PASSWORD
