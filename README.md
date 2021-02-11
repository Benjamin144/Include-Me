![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

<h1 align="center">Include Me</h1>

**This is my 3rd Milestone project covering: Data-Centric Development - Code Institute**

# Welcome to Include Me Book Review & Logger

## Contents
- [Introduction](#joe-roberts-Include:Me--Thirds-milestone-project)
- [Demo](#demo)
- [UX](#ux)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
- [Features](#features)
    * [Existing Features](#existing-features)
    * [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used")
- [Testing](#testing)
- [Deployment](#deployment)
    * [Deployment on GitHub Pages](#deployment-on-github-pages)
    * [Cloning the Repository](#cloning-the-repository)
- [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Acknowledgments](#acknowledgements)


## Introduction
This is a book review and recommendation site. The web application enables the user to log and review book tiles they would recommend others to read.

## The learning outcomes
Used Jinja for writing less code. MongoDb to create a database of information and Heroku to deploy the site.

## Future Development - Features
Make the site secure - by using Log in - Admin/User securtity.

## Current Issues

Search functions on home page before logging in throws error 'pymongo.errors.OperationFailure' 
Edit function broken 

## Demo

<h2 align="center"><img src="https://github.com/Benjamin144/Include-Me/blob/master/Includeme2.pdf"></h2>

## User Experience (UX) - Intro

C.R.U.D is used to navigate through the website with notifications to confirm the user profiles status.
## Wireframes = (use pdf files)

### Wireframes:

[Mobile-View]      https://github.com/Benjamin144/Include-Me/blob/master/IncludeMe-mobile%20view.pdf
[Tablet-View]     https://github.com/Benjamin144/Include-Me/blob/master/IncludeMe-tablet%20view.pdf
[DeskTop-View]    https://github.com/Benjamin144/Include-Me/blob/master/IncludeMe-desktop%20view.pdf

### Strategy

There would be a varied community of users that could attract people to the site. 

### Scope

Reduplicates of additional a book titles, and displaying them as a log entry. 
Materialises and Matierial Design is used as the front end display and MongoDB is used as a non relational database.

### Structure

1) Options to register your first name, last name, email & password, before signing up and given sign up confirmation

2) User can now add new titles from a list of genres, edit their choices or delete them & toggle read by a certain calender date.

3) A SUPER_USER profile can be added with admin privileges access the global management of genres across the site

4) An upvoting mechanism to be added (tentative)

At this point the site is under development could be subject to change in appearence.

### Skeleton 

- Single page design, based on jinja templating because the site is connected to MongoD
- Typography - I have used Monserrat
- Imagery - (TBA)
 
### Surface 

- Colours used a blue and white theme.
- Simple link based navbar and buttons across a white background, with the blue and footer colour subject to change (tentative)

## issues, that needed further development 

- connecting PyMongo authentication - **resolved** by entering correct credentials and adjustments to line spacing issues
- reducing white space around the site - **resolved** - used background image
- responsiveness in mobile devices - search field - **resolved** - with mobile queries work around in style.css, global settings with materialize.min.css fixed scaling issues
- Indices criteria between mongodb throws errors after hitting the edit button when logged into a profile. - **resolved** - by title.html npt being defined in app.py file
- Search button missing, unable to use the faciliy whn logged into a profile account - code was commented out to work on - **resolved**
- unable to run successful validation for Jinja based code functions. **resolved** by using view page source method as current WC3 dosent compile from upload
- **Unresolved** labels for identifying author, child friendly, publisher, date published nd page count, is under developed
- **Unresolved** - issues with incrementor throws error in this line of code. {% if titles|length > 0 %} 



<p align="right">
  <a href="joseph-roberts-include:me-app---third-milestone-project">Back to Top :arrow_heading_up:</a> 
</p>

### Existing Features
     
        Include:Me logo (top left) allows the user to switch back to the homepage. 
        Login - allows the user to enter a username and password and press a login button to view profile below the landing page
        Register - allows the user to enter a username and password below the landing page.
        Animated button - allows the user quick access to the activity pages.
        Other links to Logging in and registration can be found beneath the form
        A footer for links to social media can be found on the left side continually while scrolling up and down the page.
        A button on the bottom right can be used to roll the page back up the page to the start.
        When logged in or registered a 'flash' message is presented to understand your profile.
        When logged in as Admin as username you get more options to add or delete more genres to the site
        When logged in the user can add book titles to their profile, by choosing genre, and entering details of the title.
        Users have access to information on books titles posted aand can add book titles themselves

For some/all of your features, you may choose to reference the specific project files that implement them, although this is entirely optional.

In addition, you may also use this section to discuss plans for additional features to be implemented in the future:

### Features Left to Implement

- Labels for author, child friendly, date published, number of pages and publisher details missing from accordion dropdown menus.
- A visual representation of the Book
- A downloadable sample from partnering website
- A buy book link to oan external ecommerce website 

## Features II

- Responsive on all mobile device sizes and screen sizes.
- Added 'Popout feature to accordian review system.
- Animated scroll down button for easier access to registration, log in, search, and editing criteria.
- Arrow scroll up button for easier access to the navigational bar.
- Code completely modified and repurposed to suit the needs of the UX requirement concerning displayed books.
- Working connection to live MongoDB, where users can add their own record.
-  Up vote system that outputs a like / dislike feature **tentative**

## Technologies Used

-   [JQuery](https://jquery.com) 
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JS](https://en.wikipedia.org/wiki/JavaScript)
-   [JQ](https://en.wikipedia.org/wiki/jQuery)
-   [Python]{https://en.wikipedia.org/wiki/Python_(programming_language)}
-   [Jinja-Templating]{https://en.wikipedia.org/wiki/Jinja_(template_engine)}
-   [Flask]{https://en.wikipedia.org/wiki/Flask_(web_framework)}
-   [MongoDb](https://en.wikipedia.org/wiki/MongoDB)
-   [Heroku](https://en.wikipedia.org/wiki/MongoDB)


### Frameworks, Libraries & Programs Used

1. [Materialize CSS:](https://materializecss.com/)
    - Materialize was used to assist with the responsiveness and styling of the website.
2. [Material Design:](https://mdbootstrap.com/)
    - MDB Styled button and design usd for button on footer
3. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'roboto' font into the style.css file which is used on all pages throughout the project.
4. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
5. [jQuery:](https://jquery.com/)
    - jQuery came with Materialize to make the navbar responsive, calender date picker options, collapsable elements for the book recommendation, Accordian style 'Pop out' functions  .
6. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
7. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
8. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes]during the design process.

    <p align="right">
  <a href="joseph-roberts-super-arenas---second-milestone-project">Back to Top :arrow_heading_up:</a> 
</p>

## Testing - Intro

After numerous testing it is of my opinion that the operations functions well throughout the website, and there are no issues causing errors to stop the website from functioning


## Further Testing


-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/Benjamin144/Include-Me/blob/master/add_genreWC3%202021-02-10%20224757.jpg) **pass**
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/Benjamin144/Include-Me/blob/master/cssWC3Screenshot%202021-02-10%20232114.jpg) **pass**



## Gitpod set up  

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

I have tested my project using Chromes developer tools, and Light House


## lighthouse 
At the time of final testing I was unable to get lighthouse to function but I had previously looked at the results at a previous stage and they were all over 88% pass rate.
- [MobileTesting]   https://github.com/Benjamin144/Include-Me/blob/master/mobileView.jpg
- [DesktopTesting]  https://github.com/Benjamin144/Include-Me/blob/master/deskTopView.jpg

## Testing Errors - Struggling to get past these...type of error sample below:

**Fixed**       TemplateNotFound error even though template file exists, there was a formatting issue with the HTML file causing the app decorator to malfunction.
                I resolved this by acrediting the formating from https://github.com/Code-Institute-Solutions/FlaskFramework/blob/master/01-GettingStarted/03-routing/templates/contact.html
                which fixed the error. I also tried a code line, app = Flask(__name__, template_folder='template'), as an experiment to test if the app.py could find the html file, but that didn't work.
                https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists
    
### Testing User Stories from User Experience (UX) Section

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a Developer              ||  I want to understand the global purpose of the site and learn more about the potential interest and overall usefulness of the site.
        2. As a Publisher              ||  I would be interested to see a list of bestsellers for adults and children.
        3. As a User                   ||  I want to be able to search for best selling books titles.

    -   #### Returning Visitor Goals

        1. As an Developer             ||  It has a flow of functionality that is being properly understood by the user.
        2. As a Publisher              ||  What authors & titles are frequently added to the site.        
        3. As a User                   ||  Would like to check back and see what new titles are present.

    -   #### Frequent User Goals
        1. As a Developer              ||  Would like to update the site by alerting users of new include:me book recommendations, via podcasts or online classroom environments, including YouTube, Google Meet..e.t.c
        2. As a Publisher              ||  Cras vitae purus metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam s
        3. As a User                   ||  What what kind of book titles are available, via genre,..i.e Sci Fi, Fantasy, e.t.c


### Further Testing

-   The Website was tested on Google Chrome. Internet Explorer, Firefox and Opera, the screen sizes were good and images appeared to scale well
-   The website was viewed on a variety of devices such as Desktop, Laptop, iphone6 iPhone7, iPhone 8 iPhoneX, iPad, iPad Pro and Pixel 2XL
-   A large amount of testing was done to ensure that all pages were linking correctly.'#'was used where page links were not developed to their final resolution.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs
- none

## Deployment

The site is deployed published at https://include-me.herokuapp.com/ from my Herokuapp

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Benjamin144/includeme)

2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.


 git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY


7. Press Enter. Your local clone will be created.


 git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
Cloning into `CI-Clone`...

 Unpacking objects: 100% (10/10), done.


Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Connecting MongoDB ##

Connect To my Cluster which is called 'myFirstCluster'
Methods to connect your application to my cluster have been done though the URI method. The MongoShell and Compass methods are also available through the connect Modal.

Further instructions can be found in thee MongoDB documentation on their website [https://cloud.mongodb.com/]

my app runs with the env.py file but is ignored by the 'gitignore' file when being pushed to GitHub - production whilst in development stage is set to 'True' but the status will be changed on deploymening the live site

My collections on the MongoDb are within [myFirstCluster], they are named under the database [include_me] and within that, there are a collection of fields inserted into documents named:
[genres] [titles] [users]. I have developed the site around these parameters with a focus on genres, when researched, it seemed a popular choice to go with.

## Connecting Heroku ##

When I log into my Heroku account this project is named [include-me]. This app is successfully connected to [Python] with mnormal confirmation messages like:

    Building on the Heroku-20 stack
    Python app detected
    No change in requirements detected, installing from cache
    Installing pip 20.1.1, setuptools 47.1.1 and wheel 0.34.2
    Installing SQLite3
    Installing requirements with pip
    Discovering process types
    Procfile declares types -> web
    Compressing...
    Done: 61.5M
    Launching...
    Released v24
    https://include-me.herokuapp.com/ deployed to Heroku

My account is also connected to [https://github.com/Benjamin144/Include-Me] my Github page. When I navigate the the 'open app' buton in Heroku, the app loads normally without any problems.

## Credits

-   [https://courses.codeinstitute.net/courses] - Flask rudimentary code snippets used to initial Framework for Flask ongoing functionality

-   [Stackoverflow)](https://stackoverflow.com/questions/19827605/change-bootstrap-navbar-collapse-breakpoint-without-using-less) : Change bootstrap navbar collapse breakpoint without using LESS

-   [Perishable Press](https://perishablepress.com/a-killer-collection-of-global-css-reset-styles/) : Killer Collection of CSS Resets

-   [Stackoverflow](https://stackoverflow.com/questions/3059044/google-maps-js-api-v3-simple-multiple-marker-example) : code ideas and snippets 

-   [WebCifar] https://www.youtube.com/watch?v=LY1jeQGUiAICSS - Scroll Down Animated Button | Scroll More Button

 
### Media

-   [FreePik.com] Landing page image - <a href="http://www.freepik.com">Designed by pch.vector / Freepik</a> **removed**


### Acknowledgements

-   I received inspiration for this project from The Code Institutes, Project Idea (3).
    The concept of having the website perform in such a way was a result of seeing book readers deep interest in this lifestyle.
-   My Mentor Dick Vlaanderen for continuous helpful feedback.
-   Tutor support at Code Institute for their technical support.
-   The Code Institute Slack community for their ongoing insight, discussions & emotional support.