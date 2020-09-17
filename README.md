# Construction-and-Raw-Materials-Solutions-Full-Website

Our 3-1 project with collaboration from all teammates. This repository contains front end design using HTML, CSS, Bootstrap, jQuery (for animation), JS(for form validation) and also back-end using Django for implementing login, sign up and search. The Django functions have been modified to integrate with Oracle database using PL/SQL.

# Front end 

All the pages starting from the home page to sign up to search to catalogues have some form of animation integrated in them using jQuery functions. Since this is a brokerage site, a more appealing and elegant look helps to attract potential users. Moreover, the pages have been created with cross platform use in mind. Each of the designs and aesthetics are completely responsive. They have been tested on desktop and phone screens to check their responsive adjustments and all the pages are very much compatible in any device and screen size.

The homepage has a navbar at the top. The navbar has scrollspy implemented which means that it follows the scrolling within the page and highlights the corresponding section according to scroll position. It also helps to click and navigate to specific sections within the page without the hassle of scrolling.

The homepage is divided into separate sections. Each section has a link to the corresponsing page.

The first section takes the user to the sign up page. The sign up page has front end as well as back end validation baked in using PHP. Any error or invalid data is shown accordingly and user is prompted to insert proper data in order to fill up and submit the form successfully.

The following sections all correspond to their respective catalogue pages. Each of the catalogue pages contain a brief overview about that category of service, the number of vendors under that category, the top individuals who have worked on that field and also our top featured companies. Each of these sections, again, have been implemented using bootstrap tools so they adjust and stack according to the screen size and device. They also contain a carousel of pictures that have a sliding animation baked in to show the users our portfolio of previous works.

# Back end 

The back end has been developed using a popular python framework Django. It has a lot of pre existing library functions but most of them had to be configured manually because we were required to integrate PL/SQL programming in the database for the project that is specific to oracle database. This was the toughest challenge for our project because there are barely any elaborate documentation on implementing django using oracle database. Most of our time went on debugging and finding ways to do the simple things that were already implemented on Django but then reverse engineer those to work on oracle with PL/SQL functions.

The back end starts with the simple login module which can be seen at the navbar on the homepage. The two fields email and password are submitted through the form, checked against the existing users in the database and if matched, the user is granted a session and redirected to the homepage in a logged in state.

The sign up module works from the sign up page where a user is asked to enter necessary information. After the PHP validation on the front part, if all the data is valid, the new user is inserted into the database. At the same time, the user is also logged in to a session and redirected to the homepage.
