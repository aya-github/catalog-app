# Catalog App
This is a Python program for an catalog. Logged in users can create, read, update, and delete items under categories in a database. Non-logged in users can view the catalog.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to run](#how-to-run)
* [Features](#features)

## General info
This project is an assignment for Udacity's Full Stack Web Developer Nanodegree Program. The purpose of the project is to learn CRUD and 3rd party authentication & authorization.


## Technologies
* Python 3
* Flask
* SqlAlchemy
* Bootstrap 4


## How to run
1. Install VirtualBox from https://www.virtualbox.org/
2. Install Vagrant from https://www.vagrantup.com/
3. Download the virtual machine configuration from https://github.com/udacity/fullstack-nanodegree-vm
4. Open terminal in catalog folder
5. Start a virtual machine by the command "vagrant up", and log into it by "vagrant ssh"
6. Run the python file lotsofteas.py to populate database
7. Run tyhe python file application.py
8. Open localhost:5000 in your browser


## Features
The web app allows logged in user to create new items, edit and delete items in categories. Users can login using Google signin.
