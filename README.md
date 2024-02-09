SETUP

I have used tutorials given by the Code Institude to set up this project. Specificaly, this relates to setting up base and index.html. The file and block names are identical, although it should be noted that familiarity across all students' projects at this stage is to be expected.


- [Local Legends](#local-legends)
- [User Experience](#user-experience)
  - [Background](#background)
  - [Key information](#key-information)
  - [About the user](#about-the-user)
  - [User Goals](#user-goals)
  - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Returning Visitor Goals](#returning-visitor-goals)
  - [Frequent Visitor Goals](#frequent-visitor-goals)
- [Design Stages](#design-stages)
  - [Stage One - Design](#stage-one---design)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
    - [Colour](#colour)
    - [Font](#font)
    - [Images](#images)
  - [Stage Two - Master Template](#stage-two---master-template)
    - [Header](#header)
    - [Navbar](#navbar)
    - [Footer](#footer)
    - [Welcome Banner](#welcome-banner)
  - [Stage Three - Skeleton layout](#stage-three---skeleton-layout)
    - [Index](#index)
    - [Register and Login](#register-and-login)
    - [Profile](#profile)
    - [Restaurants](#restaurants)
  - [Stage Four - Creating the database structure](#stage-four---creating-the-database-structure)
    - [PostgreSQL](#postgresql)
  - [Stage Five: Create and Read (CRUD)](#stage-five-create-and-read-crud)
    - [Register account](#register-account)
    - [Create a review](#create-a-review)
  - [Stage Six - Update (CRUD)](#stage-six---update-crud)
    - [Reviews](#reviews)
  - [Stage Seven - Delete (CRUD)](#stage-seven---delete-crud)
    - [Delete Review](#delete-review)
  - [Stage Eight - Creating the login system](#stage-eight---creating-the-login-system)
  - [Stage Nine - Defensive Programming](#stage-nine---defensive-programming)
    - [Is Logged In](#is-logged-in)
    - [Leave Review](#leave-review)
    - [Edit Review](#edit-review)
    - [Handle Edit Review](#handle-edit-review)
    - [Delete Review](#delete-review-1)
    - [Password Hashing](#password-hashing)
    - [Administrator Privileges](#administrator-privileges)
    - [Login](#login)
- [Features in Final Version](#features-in-final-version)
  - [Base Template](#base-template)
  - [Profile](#profile-1)
    - [Change Password](#change-password)
    - [Change Email](#change-email)
    - [Change Username](#change-username)
    - [Delete Account](#delete-account)
    - [Admin Password Hash](#admin-password-hash)
    - [Admin Login](#admin-login)
    - [Admin Portal](#admin-portal)
      - [Problems](#problems)
      - [Approvals](#approvals)
      - [Edit Restaurant](#edit-restaurant)
  - [Contact Us](#contact-us)
  - [Restaurants](#restaurants-1)
  - [Restaurant Profile / Leave Review](#restaurant-profile--leave-review)
  - [Home](#home)
  - [Register](#register)
  - [Sign In](#sign-in)
  - [404 page](#404-page)
- [Accessibility](#accessibility)
  - [WAVE Report](#wave-report)
    - [Errors](#errors)
    - [Empty Links](#empty-links)
    - [Justified Text](#justified-text)
    - [Nearby image has same alt text](#nearby-image-has-same-alt-text)
    - [Redundant Links](#redundant-links)
    - [Possible List](#possible-list)
  - [Contrast Ratio](#contrast-ratio)
- [Justifications and reflections](#justifications-and-reflections)
  - [Justifications](#justifications)
  - [Reflections](#reflections)
- [Technologies Used](#technologies-used)
- [Deployment \& Local Development](#deployment--local-development)
  - [Deployment](#deployment)
  - [Local Development](#local-development)
  - [How to Fork](#how-to-fork)
  - [How to Clone](#how-to-clone)
  - [How to deploy](#how-to-deploy)
    - [Elephant SQL](#elephant-sql)
    - [Heroku](#heroku)
  - [How to maintain](#how-to-maintain)
    - [Giving admin access](#giving-admin-access)
    - [Support Requests](#support-requests)
    - [Approval Requests](#approval-requests)
    - [Edit Restaurants](#edit-restaurants)
- [Testing](#testing)
- [Feedback](#feedback)
  - [Peer Feedback](#peer-feedback)
  - [Responding to Peer Feedback](#responding-to-peer-feedback)
  - [Feedback from previous projects](#feedback-from-previous-projects)
  - [Responding to feedback from previous projects](#responding-to-feedback-from-previous-projects)
  - [Other Feedback](#other-feedback)
  - [Responding to other feedback](#responding-to-other-feedback)
- [Future Developments](#future-developments)
- [Credits](#credits)
  - [W3 Schools](#w3-schools)
  - [Pexels](#pexels)
  - [Content](#content)
  - [Code Used](#code-used)
    - [Hamburger Bar](#hamburger-bar)
    - [Email Validator](#email-validator)
    - [Checking for numeric values only](#checking-for-numeric-values-only)
- [Acknowledgments](#acknowledgments)

## Local Legends

[View deployed site on Heroku]()

[View Local Legends on Github]()

![Am I responsive]()

MegaBytes is a fully responsive ecommerce web application designed for local residents of Sunderland as a takeaway-ordering platform. The order will be fully customizable, will allow users to chose a payment method, create an account, browse a menu, update details such as address and delete orders or accounts. 

The main product available at MegaBytes is sandwitches, although other products are available to add. 

***

## Methodology

I will be using agile development for this project. Typically, [Agile Methodology](https://www.wrike.com/project-management-guide/faq/what-is-agile-methodology-in-project-management/) is broken down into the following stages:

- Concept: Define the project scope and priorities
- Inception: Build the Agile team according to project requirements 
- Iteration: Create code factoring in customer feedback 
- Release: Test the code and troubleshoot any issues
- Maintenance: Provide ongoing tech support to ensure the product remains serviceable
- Retirement: The end of the product lifespan, which often coincides with the beginning of a new one

I will document each stage of development.

***

## Concept

### User Experience

#### Background

For several years now I've been working with a close friend to build relationships with local takeaways with a view to build a fully-functional takeaway app that allows customers to place orders, then either collect their order or have it delivered. This project will become the foundation of that bigger app and will be released and adapted for one local takeaway initially, then will be combined with other replicas of the app to create the larger business model. I intend this project to be the beginning of my career.

MegaBytes has several aims:

- To allow users to browse products
- To be able to create orders and accounts, to read information on products, to update orders and personal information and to delete orders and personal information

#### Key information

- A home page that introduces the user to the app
- A products page that allows the user to browse products
- A profile page that holds personal information, where the user can read, update and delete
- A registration and login page where the user can log into their account or create one


#### About the user

This project has been designed with two end users in mind:

- A new customer interested in purchasing products from MegaBytes
- An existing and returning customer

#### User Goals

![Local Legends Index Desktop](/media/images/concept/user-stories.png)





### Wireframes

I have designed five wireframes per web page to coincide with Bootstrap's five breakpoints: 

- Extra small <576px
- Small sm ≥576px
- Medium ≥768px
- Large ≥992px
- Extra large ≥1200px
- Extra extra large ≥1400px


Index.html / Home (Extra Extra Large View)

[Index xxl](/local_legends/static/images/wireframes/index-desktop.png)

Index.html / Home (Extra Large View)

[Index xl](/local_legends/static/images/wireframes/index-tablet.png)

Index.html / Home (Large View)

[Index ld](/local_legends/static/images/wireframes/index-mobile)

Index.html / Home (Medium View)

[Index md](/local_legends/static/images/wireframes/index-mobile)

Index.html / Home (Small View)

[Index sm](/local_legends/static/images/wireframes/index-mobile)

Index.html / Home (Extra Small View)

[Index xsm](/local_legends/static/images/wireframes/index-mobile)

### Custom Models

I plan to have two additional models that are fully customized: favourites and ratings

#### Favourites

The user will be able to browse products and then add one as a favourite. This will add that product to the user's favourites section so it can be accessed easily if they should wish to buy that product. This will be a one-to-one relationship, so a user can only have one favourites list, and each seperate favourites list belongs to only one user. 

#### Ratings

In my previous project, ratings were what the project was all about. In MegaBytes, they will be used as a useful addition but not central to the theme. They will be an added option for users when browsing for products or having purchased an item. Ratings may be a many-to-one relationship where a user can leave many ratings. 

### App interconnectivity

I have set out how I expect my apps to connect to one another based on the user journey, however this is only a plan at this point and may be subject to change in the final version. I will document any deviation from these plans

![App interconnectivity Design](/media/images/concept/app-interconnectivity.png)


### Database Design

The initial plans for the database were designed in Microsoft Access. I used this program because I was quite familiar with it, having taught its use for years. My project will use a Relational Database design. The Ratings and Favourites tables will form part of my two custom models

![Relationships Database Design](/media/images/concept/database-relation-design.png)

![Users Table Design](/media/images/concept/users-table-design.png)

![Products Table Design](/media/images/concept/products-table-design.png)

![Category Table Design](/media/images/concept/category-table-design.png)

![Basket Table Design](/media/images/concept/basket-table-design.png)

![Checkout Table Design](/media/images/concept/checkout-table-design.png)

![Ratings Table Design](/media/images/concept/ratings-table-design.png)

![Favourites Table Design](/media/images/concept/favourites-table-design.png)

It should be noted here that although the designs say 'Number' on several data types, the data types in the final product will be Integer. In addition, the 'Text' and 'Long Text' types will be limited by character limits which is not visible on these designs.

### Products Table Design

In my last project I made the mistake of creating the data models before I'd considered what was going to go in it. This resulted in many further migrations which complicated the process. This time I have created my full dataset before any changes are migrated. I will do this for each seperate model. 

[Product Table Dataset](/media/images/concept/concept-products-table-dataset-design.png)


### Layout

I will be using Bootstrap to set the layout of this project. I will be using a range of features including the the grid, nav bar and breakpoints to ensure it's responsive. 

#### Colour

I have chosen the following colour scheme for MegaBytes. The template can be found on [Coolers](https://coolors.co/)

![Coolers Palatte](/media/images/concept/coolers-template.png)

#### Font

The font I have chosen to use for this project is one called Poppins, which is part of the Sans Sarif family. It can be found [here](https://fonts.google.com/specimen/Poppins). I chose the 'Light 300' weighting as I felt that it would stand out a little more than the 'thin' preset. I have used this font in my other projects and feel it's just right on the eye.

#### Images



### Webpage layout

#### Master Template

The Master Template, called base.html, will be used as a template for all pages in this project. It will hold the header, footer and nav bar.

##### Header

The header incorperates the project title and nav bar. 

##### Navbar

I have adapted Bootstrap's nav bar for this project. It is responsive, and on viewports smaller than 993px it collapses into a hamburger bar with scroll functionality. At this stage the links do not work and are placeholder only. 

Initial design of nav bar on larger viewport:

![Concept Stage Navbar Larger Viewport](/media/images/concept/concept-navbar-large.png)


Initial design of nav bar on smaller viewport:

![Concept Stage Navbar Smaller Viewport](/media/images/concept/concept-navbar-small.png)


##### Footer

At this stage, the footer holds external links so that the user can find the project or author on GitHub, Facebook, X and Linked In.

![Footer](/media/images/concept/concept-footer.png)





### Implementing a Skeleton layout

Next will be to setup all other pages of this project using a skeleton layout with placeholder text. These are only designs and accept they may change in the final version. 

#### Index

The homepage will consist of a selection of the top four most popular products. In the concept stage I will create a skeleton layout of the page and fill it with placeholder images and text. 

Homepage Design: ![Homepage Design](/media/images/concept/concept-index.png)


#### Register and Login

The Register / Login page will be in two sections. For ease, I will be importing code from my first project as a placeholder, although I may choose to replicate the form completely. There is no code attached to the submit buttons below, only placeholder text, although data validation and formatting are present only because I imported code that I'd already written for Project One.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-b.png)

#### Profile

The Profile page will allow the users to carry out Update and Delete functions from the CRUD design. At this stage, none of the code behind the buttons or data validation work, and I would later like to add a small table for stats on how many stars and reviews the user has left. I've left this out of Stage Three design as this is something I will add only if I get time.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-d.png)

#### Restaurants

I have replicated index.html for restaurants.html at Stage Three, simply because Restaurants will be an extension of index.html. I intend on displaying all restaurants on this page, and only a random selection of four on index.

Homepage Design: ![Homepage Design](/local_legends/static/images/design-stages/stage-three-design-c.png)
















### Stage Four - Creating the database structure

#### PostgreSQL

I will be using PostgreSQL to create the structure and of the database and tables. My database structure, tables, columns and keys have all been approved by my mentor. I will be using command line interface to perform these tasks.

I created the database which was successful on the second attempt (see testing).

Creating DB using PostgreSQL Design: ![Create DB](/local_legends/static/images/design-stages/stage-four-design-b.png)

Then using the [PostgreSQL documentation](https://www.postgresql.org/docs/current/tutorial-table.html) to ensure I my SQL statement was correct, I created the users table

![Create users table](/local_legends/static/images/design-stages/stage-four-design-c.png)

I did try to enter the database to make sure the table was created successfully; however, nothing has shown. I will attempt to inset data into the table and then try to pull the data, which will show if it has worked or not. After several attempts this worked

![Pulling row from users table](/local_legends/static/images/design-stages/stage-four-design-d.png)

I used the same method to create the restaurants table.

![Create restaurants table](/local_legends/static/images/design-stages/stage-four-design-f.png)

You may have noticed some errors with the queries I've used so far. It was at this point I realised that I'd set all of my tables up incorrectly. I decided to drop my database and start again using carefully formulated SQL queries and the PostgreSQL documentation. These were my final queries, where I created the tables, inserted a test row then pulled the data from it to make sure everything (in particular the auto-increment for primary keys) were working fine:

![Create restaurants table](/local_legends/static/images/design-stages/stage-four-design-g.png)

![Create users table](/local_legends/static/images/design-stages/stage-four-design-h.png)

![Create reviews table](/local_legends/static/images/design-stages/stage-four-design-i.png)

That completes Stage Four

EDIT: I have made the mistake here of waiting until Stage Five before learning how to use SQL Alchemy. Had I learned this before Stage Four, I'd have known that creating the schema using SQL (PSQL command line) was a mistake. I should have used an SQL Alchemy model. I have therefore dropped the previous tables and started again using a models.py file, then initialised the schema through the command line as shown below.

![Models DB import](/local_legends/static/images/design-stages/stage-four-design-j.png)

Then I checked to make sure the tables were set up correctly.

![Checking tables set up](/local_legends/static/images/design-stages/stage-four-design-k.png)

I have done this using the models.py script, although this code was based on the examples given in Lesson 18: Creating the database on the Code Institute walkthrough tutorial. It wasn't possible to completely write my own code here as the syntax for this particular function is more or less identical across the spectrum.

![Modals.py](/local_legends/static/images/design-stages/stage-four-design-l.png)

### Stage Five: Create and Read (CRUD)

#### Register account

This stage will focus on using SQL Alchemy to insert placeholder data into the local_legends database with Python to ensure that everything works as expected. For this stage I have set the main route as Register, which means every time I make the python server live, I will be testing with Register.html.

The first 15 tests all failed (see tests 004 to 009 in testing readme). I had to request support from Tutor Support having exhausted the documentation and attempts to use AI. However, the connection is now working:

![Adding values to database](/local_legends/static/images/design-stages/stage-five-design-g.png)

#### Create a review

This section will focus on leaving only one review for only one restaurant. But to do that I first need to create a record in the Restaurants table so I can build the visual aspects of restaurants.html around that. I will document this as I go. For ease, I am going to use command line controls to populate the restaurants table with one row:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-five-design-h.png)

The restaurants page is now complete, and I can see a list of everything in the Restaurants database.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-five-design-i.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-five-design-j.png)

The Creating and Reading of CRUD is now complete.

### Stage Six - Update (CRUD)

There will be two ways to update details in this project; user details and review edits.

I did start this stage by creating routes for user details but realised that I would first need to create the session. To update user details, it's essential the user is able to log in. However, it's not essential for the user to be logged in to leave a review, at least not in this stage (it will be at a later stage). For now, I need to do the minimum to ensure this project meets CRUD design.

#### Reviews

At this stage I will allow a 'guest' to leave a review just so we can pass the Update aspect of CRUD. This is possible with the new Restaurants page. I will add a button to each restaurant section and attempt to pass the restaurant ID through the URL, then display the reviews for that particular restaurant. I will then allow a guest to edit any review they see for CRUD purposes (a login system will be created at a later date and will allow only the author to edit their own reviews).

This script is now operational. Observe the first review available:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-a.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-b.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-c.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-six-d.png)

### Stage Seven - Delete (CRUD)

Stage Seven will focus on the last aspect of CRUD design and will allow a guest to delete from the database. In this example I will be using edit_review.html so that the user can delete a review. At this stage I have not yet created a login system, so I will need to allow anyone to delete a review. The function will not check requests against a user ID at this stage.

#### Delete Review

In this example I will delete the first review in the table assigned to Monster Munch.

Here, we can see the review in the list.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-seven-a.png)

We click 'Edit Review' to enter the edit screen.

Then we click 'Delete Review'.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-seven-b.png)

Now we can see the review is no longer displayed. The record has been deleted from the database.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-seven-a.png)

Stage Seven is now complete. My next stage will focus on creating the login system so that I can add some validation to stop guests editing and deleting reviews.

### Stage Eight - Creating the login system

For design purposes I will be using the following login details:

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-a.png)

This stage has been very difficult to create. I tested a few different methods, but in the end, I had to settle for a step-by-step approach that forced the user to redirect to certain pages at each stage, just so I could see where it was working and where it was going wrong. I will document these stages as I go.

At this stage, the form only redirects when it detects a form submission. This redirect means that the form is working, and so is the syntax of the function so far.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-b.png)
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-c.png)

Now I've added a section to redirect if the email is matched and the query works, which it does. Next is the password check.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-d.png)

The structure of the function works when hard-coded.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-e.png)

Now it works when form submitted.
![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-f.png)

To test the sessions were working correctly, I updated the Welcome Banner to show the username when logged in, and amended the nav bar to incorporate a check to see if the is_logged_in session was set, then display Sign In / Sign Out

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-g.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-h.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-i.png)

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-eight-design-j.png)

This now completes Stage Eight.

### Stage Nine - Defensive Programming

#### Is Logged In

The permissions for this project will follow CRUD design and will be set out as follows:

| CRUD   | Guests | Registered Accounts |
| --- | --- | ---  |
| Create | No*   | Yes                 |
| Read   | Yes    | Yes                 |
| Update | No     | Yes                 |
| Delete | No     | Yes                 |

* Except to create account

While Registered Accounts will have permission to create, update and delete their own reviews, they will not have the permission to alter other user's reviews.

The next stage will centre around defensive programming.

Is Logged In is one of the sessions that is created when the user logs in. I will amend each function to check for this being set before the function executes, else the user is directed back to the sign in page.

![Adding a row to restaurants using command line](/local_legends/static/images/design-stages/stage-nine-design-a.png)

I've added this code to every function with update and delete design aspects.

I want to add another failsafe to my project, so I will amend the templates to only show the parts I need it to

#### Leave Review







#### Password Hashing



#### Administrator Privileges





#### Login


***

## Features in Final Version


### Base Template


### Profile

### Contact Us


### Restaurants

### Restaurant Profile / Leave Review


### Home



### Register



### Sign In



### 404 page



***

## Accessibility

### WAVE Report

### Contrast Ratio

***

## Justifications and reflections

### Justifications

### Reflections



***

## Technologies Used

| Programme / feature         | Technology used                                              |
| --- | --- |
| Languages                   | HTML and CSS                                                 |
| Framework                   | [Materialize 0.100.0](https://materializecss.com/about.html) |
| Colour Scheme               | [Materialize](https://materializecss.com/color.html)         |
| Contrast Ratio              | [webAIM](https://webaim.org/)                                |
| Accessibility (WAVE report) | [webAIM](https://webaim.org/)                                |
| Fonts                       | [Google Fonts](https://fonts.google.com/)                    |
| **Images**                  |                                                              |
|                             |                                                              |
| _Images_                    | [Pexels](https://www.pexels.com/)                            |
| _Image Compression tools_   | [Image Resizer](https://imageresizer.com/)                   |
| _Image editing_             | [Image Resizer](https://imageresizer.com/)                   |
| _Responsiveness testing_    | [Am I Responsive?](http://ami.responsivedesign.is/)          |
|                             |                                                              |
| Version control             | Git                                                          |
| IDE / file storing          | [Code Anywhere](https://app.codeanywhere.com/)               |
| Wireframes                  | [Balsamiq](https://balsamiq.com/)                            |
| HTML Code Validation        | [W3C Schools](https://validator.w3.org/)                     |
| CSS Code Validation         | [W3C Schools](https://validator.w3.org/)                     |
| JavaScript Code Validation  | [JS Hint](https://jshint.com/)                               |
| Developer Tools             | Chrome Developer Tools                                       |
| HTML Formatting             | [Free Formatter](https://www.freeformatter.com)               |
| CSS Formatting              | [Free Formatter](https://www.freeformatter.com)               |
| JavaScript Formatting       | [Free Formatter](https://www.freeformatter.com)               |
| Python Formatting       | [Code Institute Linter](https://pep8ci.herokuapp.com/)               |

***

## Deployment & Local Development

### Deployment



### Local Development

### How to Fork



### How to Clone



### How to deploy



#### Elephant SQL


   
#### Heroku




### How to maintain










***

## Testing

Please see [Testing Readme](/TESTING.md) for all testing for this project

## Feedback

### Peer Feedback

I have worked closely with my peers on testing this product rigorously for any errors. The feedback is as follows:

- Some of the pages do not seem to be responding well on smaller screens. The input boxes seem to come out of the container.

- The footer seems to float on Contact Us and Register on smaller screens

### Responding to Peer Feedback

I have taken the following actions in response to feedback:

- Used multiple media queries to adjust the parent container so that the input boxes are never out of the container.
- Applied a 'position: fixed' style to the main footer container

### Feedback from previous projects

### Responding to feedback from previous projects

I have taken the following actions in response to feedback:

1. Because I am partially colour-blind, I've had to build this project using a tool called [WebAIM](https://webaim.org/resources/contrastchecker/bookmarklet) to aid me in checking the contrast ratio. I continue to use alternative text.

I have also included a WAVE report, which passes all tests.

2. I have ensured that every filename contains no numbers, capital letters or underscores. Each file has been placed in an appropriate folder, and I've ensured each file is named correctly and appropriately.

3. I have ensured that along with details of all of my testing, I've included as many before and after screenshots as possible. In some cases, it wasn't always possible to include both, but these tests are clearly marked with justification.

4. Throughout the testing stages, I have included snippets of code along with screenshots of visual output of that code.

5. I have attempted to be as thorough as possible throughout the development of this project.

### Other Feedback

My mentor suggested that I display a warning to a user about the impact of deleting a review or account. I have included this just above the submit button on both elements.

### Responding to other feedback



***

## Future Developments



***

## Credits

### Content

Content for the website was written by Dan Matthews.

### Code Used

#### Hamburger Bar

I have used Bootstrap's Nav bar as a template to create my own. It can be found [here](https://getbootstrap.com/docs/5.3/components/navbar/)


***

## Acknowledgments


