**GitHub link to SEPlan** \
https://github.com/Donovan9617/SEPlan

**NUS Orbital SEPlan** \
SEPlan is a one-stop platform for NUS students who intend to go on SEP to obtain resources, contribute reviews, map modules, plan timetables, and connect with exchange alumni. Built using Django, JavaScript, and Bootstrap, we aim to create a user-friendly platform for students to ask questions and receive quality answers about SEP universities, modules and the module planning process in a timely manner.

**SEPlan Application** \
The Home Page is an aesthetic dashboard with routes to "Forum", "Reviews", "Modules" and "Messages". There are also other SEP related sections such as "SEP Announcemenet" panel, "SEP Results", "SEP Planner", and "SEP Destinations". 

A system administrator may upload important announcements, openings or information sharing sessions pertaining to SEP universities via the Django Admin Interface. Users will be able to view them from the "SEP Announcements" panel in their home page, as well as toggle between pages via pagination features should the post get too long. For each announcement, there is a "save for later" button on the right, enabling users to save announcements of SEP details that they are interested in or deem important. These saved announcements are displayed when the user clicks on the "Saved" navigation item on the top navigation bar. The "Print" navigation item enables the user to print the current page. The "Logout" navigation item enables the user to log out of the system. The "SEP Results" section shows the progress bars for the user's SEP application, progress of Module Selection, and deadline for SEP Application. These progress bars can be editted by the system administrator over time. It also enables the user to view the results of their SEP application. The "SEP Planner" section displays a shortlist table of the user's choice universities, modules the user plans to take in each, and modules the user plans to map over from NUS. Below that, the user may view a calendar with different coloured event markings to help with the planning and preparation process of SEP application. The "SEP Destinations" section comprises an aesthetic doughnut chart with the corresponding proportions of SEP destinations available for students. These proportions can be editted by the system administrator if the numbers change over time.

In the Forum route, a user can begin new discussion threads on their SEP topics of interest, such as partner universities, modules, the module mapping process, etc. In future stages of development, this action can be done by clicking on the "New Discussion" button. The user may also attach files to their queries. Upon clicking the "Post" button, the thread is added to the library of forum posts available for other users' viewing. We will also be allowing users to vote and comment on individual discussion threads.

In the Reviews route, a user who had just returned from SEP may write a review of their own SEP experience, including the learning environment at their SEP university, the modules they managed to map over, and the living environment and favourite pictures at their overseas destination. Upon clicing the "review" button, an alert thanks the user for submitting the review, which is then added to the library of reviews available for other users intending to embark on SEP. As reviews are categorised by partner universities, a user looking for information about a particular partner university can easily find all the reviews about it together and directly contact the reviewer by clicking on the "message" button should they require more information. Users are also able to view their history of reviews and have the option to delete their past reviews.

In the Modules route, a user can easily find modules from partner universities that can be mapped to their corresponding NUS modules. After entering an NUS module code into the search bar and clicking the "search" button, a list of partner universities with mappable modules, along with their module names and codes and a "plus" button, would be displayed. On clicking the "plus" button, an alert informs the user that he has shortlisted this overseas module and university into his SEP planner table in the home page. If there are no modules which map to the entered NUS module code, no results will be displayed.

In the Message route, a user may start a conversation with another user by using the search bar on the left to search for their username, or through the "message" button in the review platform. Chats with other users are listed to the left while the main flow of conversation with a particular user is displayed on the right. By displaying the username and faculty of users, a user is able to ask questions for faculty-based SEP and have them answered in a more personal and informative manner. Additionally, users from the same faculty intending to embark on SEP to similar countries may easily form groups and connections.

**Tech Stack** \
Languages: Python, HTML, CSS, JavaScript \
Framework: Django, Bootstrap

**Technical Proof of Progress** \
To view our website on your own system, please run the following steps to install the necessary packages in your terminal:
Django: pip install django (Windows) / pip3 install django (Mac)
Git: https://github.com/git-guides/install-git
To run server: pip install psycopg2, then pip install django-heroku (Windows) / pip3 install psycopg2, then pip3 install django-heroku (Mac)

Using a source-code editor, clone our Github repository by running this command in your terminal: git clone https://github.com/Donovan9617/SEPlan
Change directory by running these commands in your terminal in order: cd SEPlan, cd orbital
Once in the directory orbital, run this command in your terminal: python manage.py runserver (Windows) / python3 manage.py runserver (Mac)
Copy and paste the URL of the development server into a web browser and add "/sep" to run the page.