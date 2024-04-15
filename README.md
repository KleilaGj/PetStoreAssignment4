# PetStoreAssignment4
Team members: Leila and Tahirah 
Team name: DREAM TEAM!


Previous CFG degree projects were all previous assignments, including working with JavaScript, Python and SQL.

Git hub will be used to allow Tahirah and Leila to work together on this assignment sending codes to each other and being able to edit them. 


~.gitignore is used to specify which files and directories should be ignored by Git when tracking changes in a repository. It allows you to exclude certain files or patterns from being committed to the repository. view image below to see visual representation of .gitignore being created.
![gitignore ](https://github.com/KleilaGj/PetStoreAssignment4/assets/162932410/223570d0-1eb5-4f84-8838-87fb1c7fd4a0)

~requirements.txt file is a text file that lists the dependencies or packages required for a project to run. each line in the file typically specifies a package name and it's version number. It helps ensure that everyone working on the project is using the same versions of the required package. view image below to see visual representation of requirements.txt being created. 
![requirement txt](https://github.com/KleilaGj/PetStoreAssignment4/assets/162932410/bf767c11-b0d7-4de1-a24c-78739c427c81)


**Pet Store API**
The PetStore API allows users to interact with a pet database and place orders for them. It provides endpoints for retrieving pet information, placing orders, and retrieving order details.

*Installation*
To run the PetStore API, Python and Flask should be installed on your machine. You can install Flask:
    - [x] open command prompt on your machine
    - [x] type: pip install flask

~~Config~~
**Configuration**
* Add your username on the 'user:' line with your MySQL username
* Add your password on the 'password:' line with your MySQL password

Running the API <sub>How to run the API</sub>
- GO onto your project directory and run this command:
  python app.py

- This starts the Flask development server
- Now you can access the API endpoints from your browser

***Endpoints***
GET /pets: Retrieve a list of all pets.
GET /pets/<pet_id>: Retrieve details of a specific pet.
POST /orders: Place an order for a pet.
GET /orders/<order_id>: Retrieve details of a specific order.


**<sup>Testing</sup>**
Test the API using Postman or Curl






