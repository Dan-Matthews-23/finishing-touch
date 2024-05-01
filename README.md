- [MegaBytes]()
- [Concept]()
    - [User Experience](#user-experience)
        - [Background](#background)
        - [Key information](#key-information)
        - [About the user](#about-the-user)
        - [User Goals](#user-goals)
    - [Wireframes](#wireframes)
    - [Custom Models](#custom-models)
        - [Favourites](#favourites)
        - [Ratings](#ratings)
        - [Chef Messages](#chef-message)
    - [App Interconnectivity](#app-interconnectivity)
    - [Database Design](#database-design)
    - [Layout](#layout)
        - [Colour](#colour)
        - [Font](#font)
        - [Webpage Layout](#webpage-layout)
            - [Master Template](#master-template)
            - [Header](#header)
            - [Navbar](#navbar)
            - [Index](#index)
            - [Register and login functions](#register-and-login-functions)
            - [Profile](#profile)
            - [Products](#products)
            - [Basket](#basket)
            - [Checkout](#checkout)
            - [Order History](#order-history)
            - [Manage Products](#manage-products)
    - [Accessibility](#accessibility)
        - [WAVE report](#wave-report)
        - [Contrast Ratio](#contrast-ratio)
    - [Justifications and reflections](#justifications-and-reflections)
        - [Justifications](#justifications)
            - [Image use](#image-use)
            - [Categories](#categories)
            - [Limited colour palette](#limited-colour-palette)
        - [Reflections](#reflections)
            - [process_checkout](#process_checkout)
            - [basket_form](#basket_form)
    - [Technologies Used](#technologies-used)
    - [Deployment & Local Development](#deployment--local-development)
        - [Deployment](#deployment)
            - [Live database](#live-database)
            - [Heroku setup](#heroku-setup)
            - [Actions in IDE](#actions-in-ide)
            - [Amazon Web Service for static files](#amazon-web-service-for-static-files)
            - [Creating AWS groups, policies and users](#creating-aws-groups-policies-and-users)
        - [Local Development](#local-development)
    - [Testing](#testing)
    - [Feedback](#feedback)
        - [Peer Feedback](#peer-feedback)
        - [Responding to Peer Feedback](#responding-to-peer-feedback)
        - [Feedback from previous projects](#feedback-from-previous-projects)
    - [Credits](#credits)
        - [Content](#content)
        - [Code Used](#code-used)
            - [Hamburger Bar](#hamburger-bar)
            - [Star Rating system](#star-rating-system)
    - [Acknowledgments](#acknowledgments)


## Local Legends

[View deployed site on Heroku](https://megabytes-bfd0afc9e4a4.herokuapp.com/)

[View Local Legends on Github](https://github.com/Dan-Matthews-23/mega-bytes)

![Am I responsive]()

MegaBytes is a fully responsive ecommerce web application designed for local residents of Sunderland as a takeaway-ordering platform. The order will be fully customizable, will allow users to choose a payment method, create an account, browse a menu, update details such as address and delete orders or accounts. 

The product available at MegaBytes is healthy sandwiches with full nutritional information

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

![Megabytes User Stories](/media/images/concept/user-stories.png)

### Wireframes

I have designed five wireframes per web page to coincide with Bootstrap's five breakpoints: 

Extra small None    <576px
Small   sm  ≥576px
Medium  md  ≥768px
Large   lg  ≥992px
Extra large xl  ≥1200px
Extra extra large   xxl ≥1400px

Index.html / Home (Extra Extra Large View)

[Index xxl](/media/images/concept/wireframes/index-1400px.png)

Index.html / Home (Extra Large View)

[Index xl](/media/images/concept/wireframes/index-1200px.png)

Index.html / Home (Large View)

[Index ld](/media/images/concept/wireframes/index-992px.png)

Index.html / Home (Medium View)

[Index md](/media/images/concept/wireframes/index-768px.png)

Index.html / Home (Small View)

[Index sm](/media/images/concept/wireframes/index-576px.png)

Base.html / Home (Extra Extra Large View)

[Base xxl](/media/images/concept/wireframes/base-1400px.png)

Base.html / Home (Extra Large View)

[Base xl](/media/images/concept/wireframes/base-1200px.png)

Base.html / Home (Large View)

[Base ld](/media/images/concept/wireframes/base-992px.png)

Base.html / Home (Medium View)

[Base md](/media/images/concept/wireframes/base-768px.png)

Base.html / Home (Small View)

[Base sm](/media/images/concept/wireframes/base-576px.png)

Products.html / Home (Extra Extra Large View)

[Products xxl](/media/images/concept/wireframes/products-1400px.png)

Products.html / Home (Extra Large View)

[Products xl](/media/images/concept/wireframes/products-1200px.png)

Products.html / Home (Large View)

[Products ld](/media/images/concept/wireframes/products-992px.png)

Products.html / Home (Medium View)

[Products md](/media/images/concept/wireframes/products-768px.png)

Products.html / Home (Small View)

[Products sm](/media/images/concept/wireframes/products-576px.png)

Basket.html / Home (Extra Extra Large View)

[Basket xxl](/media/images/concept/wireframes/basket-1400px.png)

Basket.html / Home (Extra Large View)

[Basket xl](/media/images/concept/wireframes/basket-1200px.png)

Basket.html / Home (Large View)

[Basket ld](/media/images/concept/wireframes/basket-992px.png)

Basket.html / Home (Medium View)

[Basket md](/media/images/concept/wireframes/basket-768px.png)

Basket.html / Home (Small View)

[Basket sm](/media/images/concept/wireframes/basket-576px.png)


Checkout.html / Home (Extra Extra Large View)

[Checkout xxl](/media/images/concept/wireframes/checkout-1400px.png)

Checkout.html / Home (Extra Large View)

[Checkout xl](/media/images/concept/wireframes/checkout-1200px.png)

Checkout.html / Home (Large View)

[Checkout ld](/media/images/concept/wireframes/checkout-992px.png)

Checkout.html / Home (Medium View)

[Checkout md](/media/images/concept/wireframes/checkout-768px.png)

Checkout.html / Home (Small View)

[Checkout sm](/media/images/concept/wireframes/checkout-576px.png)


Login.html / Home (Extra Extra Large View)

[Login xxl](/media/images/concept/wireframes/login-1400px.png)

Login.html / Home (Extra Large View)

[Login xl](/media/images/concept/wireframes/login-1200px.png)

Login.html / Home (Large View)

[Login ld](/media/images/concept/wireframes/login-992px.png)

Login.html / Home (Medium View)

[Login md](/media/images/concept/wireframes/login-768px.png)

Login.html / Home (Small View)

[Login sm](/media/images/concept/wireframes/login-576px.png)





### Custom Models

I plan to have two additional models that are fully customized: favourites and ratings

#### Favourites

The user will be able to browse products and then add one as a favourite. 

#### Ratings

In my previous project, ratings were what the project was all about. In MegaBytes, they will be used as a useful addition but not central to the theme. They will be an added option for users when browsing for products or having purchased an item. Ratings may be a many-to-one relationship where a user can leave many ratings. 

#### Chef Message

Chef Message is a basic model accessible only to the superuser, and can be found under the Manage Products tab. It only has one element to the model. 

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

### Layout

I will be using Bootstrap to set the layout of this project. I will be using a range of features including the grid, nav bar and breakpoints to ensure it's responsive. 

#### Colour

I have not chosen to implement a colour palette in this project. Instead, the colours available will be black and off white (F7F9F9). 

#### Font

The font I have chosen to use for this project is one called Poppins, which is part of the Sans Sarif family. It can be found [here](https://fonts.google.com/specimen/Poppins). I chose the 'Light 300' weighting as I felt that it would stand out a little more than the 'thin' preset. I have used this font in my other projects and feel it's just right on the eye. I have also used Nanum Pen Script for the Chef Message to give the effect of handwriting. It can be found [here](https://fonts.google.com/specimen/Nanum+Pen+Script).

### Webpage layout

#### Master Template

The Master Template, called base.html, will be used as a template for all pages in this project. It will hold the header, footer and nav bar.

![Am I responsive]()

#### Header

The header incorporates the project title and nav bar. 

#### Navbar

I have adapted Bootstrap's nav bar for this project. It is responsive, and on viewports smaller than 993px it collapses into a hamburger bar with scroll functionality. At this stage the links do not work and are placeholder only. 

Initial design of nav bar on larger viewport:

![Concept Stage Navbar Larger Viewport](/media/images/concept/concept-navbar-large.png)

Initial design of nav bar on smaller viewport:

![Concept Stage Navbar Smaller Viewport](/media/images/concept/concept-navbar-small.png)

#### Index

The homepage will consist of an introduction, purpose and instructions of how to use. 

Homepage Design: ![Homepage Design](/media/images/concept/concept-index.png)

#### Register and Login functions

I have used Django Allauth to provide functionality for Megabytes. I have adapted the templates for customised experience

Register: ![Am I Responsive]()

Login: ![Am I Responsive]()

Logout: ![Am I Responsive]()

#### Profile

The user will have one profile page where they can view previous orders and update their personal information

Profile: ![Am I Responsive]()

#### Products

The user will be able to browse available sandwiches and choose one they would like to purchase

Products: ![Am I Responsive]()

#### Basket

The user will be able to view products they have chosen and update order details

Basket: ![Am I Responsive]()

#### Checkout

The user will be able to enter payment details so that they can purchase items. The payment functionality is provided by Stripe

Checkout: ![Am I Responsive]()

#### Order History

The user will be able to view all of their previous orders

Order History: ![Am I Responsive]()

#### Manage Products

If a superuser, the user can create, read, update and delete products. This can be accessed via the nav bar and will only show for those who are superusers

Manage Products: ![Am I Responsive]()

***

## Accessibility

### WAVE Report

The WAVE report returned no errors and three alerts:

- Suspicious link. This refers to the 'Register' link in the index page. As this is not an error and only a suggestion, I have chosen to disregard this suggestion. I do not feel rewording 'Register' to anything else would be appropriate. 

- Justified Text. This refers to Chef Message block being set with a 'Justify' CSS style. I have followed this suggestion and changed this to 'Centre'. However I cannot locate the second block of text this suggestion refers to as the WAVE report.

### Contrast Ratio

I have been unable to use Web Aim’s contrast ratio on MegaBytes. I believe it may be a conflict between Heroku and Web AIM. 

***

## Justifications and reflections

### Justifications

#### Image use

I have opted not to use images in MegaBytes. Finding images that match the specific specifications including colour, bread type, background colour, filling etc proved too problematic. I have kept the original model structure however as this project is going to be deployed as a live project for real-world application, and when that happens we will be able to create images for the new products directly. This means there is already an image URL field in the products model ready for use. 

#### Categories

The products that the user can see on the products page all have a category_id of 9. This is because when we apply this project template to our business, other items such as sundries, drinks, add-ons will all have their own category_id so they can be easily sorted. For the purposes of this project only the one category was needed, but the structure is there for additional options.

#### Limited colour palette

I took inspiration for this project from successful food apps such as Just Eat. I note that their three primary colours are white, black and orange. I wanted to replicate that simplistic approach and have adopted a similar colour scheme.

### Reflections

#### process_checkout

I had multiple problems with this function. I spent a great deal of time with Tutor Support who were not able to pinpoint the problem and advised I contact Stripe directly. We identified that this was not a problem with Stripe but with how I'd set my project up. As a result I had to implement a work-around. You may notice that the function is now wrapped in a condition that checks to see if a hidden input value is set to True. Further information is noted in 'Known Bugs'.

#### basket_form

This is also noted in 'Known Bugs' and is a bug resulting in the user having to type in their full name each time they order even if they update their profile information. Tests are ongoing to find the cause.

***

## Technologies Used

| Programme / feature         | Technology used                                              |
| --- | --- |
| Languages                   | HTML and CSS                                                 |
| Framework                   | [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/) |
| Colour Scheme               | [Coolers](https://coolors.co/l)         |
| Contrast Ratio              | [web AIM](https://webaim.org/)                                |
| Accessibility (WAVE report) | [web AIM](https://webaim.org/)                                |
| Fonts                       | [Google Fonts](https://fonts.google.com/)                    |
| **Images**                  |                                                              |
|                             |                                                              |
| _Images_                    | [Pexels](https://www.pexels.com/)                            |
| _Responsiveness testing_    | [Am I Responsive?](http://ami.responsivedesign.is/)          |
|                             |                                                              |
| Version control             | Git                                                          |
| IDE / file storing          | [GitPod](https://gitpod.io/)               |
| Wireframes                  | [Balsamiq](https://balsamiq.com/)                            |
| HTML Code Validation        | [W3C Schools](https://validator.w3.org/)                     |
| CSS Code Validation         | [W3C Schools](https://validator.w3.org/)                     |
| JavaScript Code Validation  | [JS Hint](https://jshint.com/)                               |
| Developer Tools             | Chrome Developer Tools                                       |
| HTML Formatting             | [Free Formatter](https://www.freeformatter.com)               |
| CSS Formatting              | [Free Formatter](https://www.freeformatter.com)               |
| JavaScript Formatting       | [Free Formatter](https://www.freeformatter.com)               |
| Python Formatting       | [Code Institute Linter](https://pep8ci.herokuapp.com/)             |
| Payment System        | [Stripe](https://stripe.com/gb)             |
| Login/Register System        | [Django Allauth](https://docs.allauth.org/en/latest/)             |
| Database (IDE)       | [SQLLite](https://www.sqlite.org/)             |
| Database connection        | [DJ Database URL](https://pypi.org/project/dj-database-url/)             |
| Database (Deployed Site)       | [Elephant SQL](https://www.elephantsql.com/)             |
| Cloud Hosting        | [Heroku](https://dashboard.heroku.com/)             |
| Static File Hosting        | [Amazon Web Service](https://aws.amazon.com/)             |
| Form Rendering        | [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)             |
| Django 5.02       | [Django](https://www.djangoproject.com/)             |
| Python 3       | [Django](https://www.python.org/)             |

***

## Deployment & Local Development

### Deployment

The project is deployed using Heroku. To deploy the project:

#### ** Live Database**

SQL Lite can be used in local development, however for live deployment we must use an online external database. I have chosen Elephant SQL

1. Go to the [ElephantSQL](https://www.elephantsql.com/) dashboard and click 'new instance button' .
2. Name the plan, select tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL

#### **Heroku setup**

  1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
  2. Name your app, select the region that is closest to you and then click the create app button bottom left.
  3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value.

#### **Actions in IDE**

1. Install dj_database_url and psycopg2 by typing 'pip3 install dj_database_url==0.5.0 psycopg2'   

2. Type pip3 freeze > requirements.txt   

3. In settings.py underneath import os, add `import dj_database_url`

4. Under 'DATABASES', comment out the existing code. Type: DATABASES = { 'default': dj_database_url.parse('elephantsql-db-url-here')  } 

5. In the terminal, type 'python manage.py showmigrations

6. You should see a list of migrations that are unchecked. If so, type 'python manage.py makemigrations' followed by 'python manage.py migrate'   

7. Create a superuser for the new database by typing 'python manage.py createsuperuser. Follow the instructions and note the details  

8. Replace your DATABASE code (including commented-out code) with the following:

    if 'DATABASE_URL' in os.environ:
        DATABASES = {
          'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
          }
        }
   
10. Install gunicorn by typing 'pip3 install gunicorn' followed by 'pip3 freeze > requirements.txt'
    

11. Create a file called 'Procfile' in the root directory and add this line 'web: unicorn app_name.wsgi:application'

12. Ensure both your IDE and Heroku in the Allowed Hosts:
    
    ALLOWED_HOSTS = ['{heroku site URL}', 'localhost' ]

13. Save, commit and push all changes to GitHub

#### **Amazon Web Service for static files**

Access your AWS account:

Go to https://aws.amazon.com.
Click "Manage My Account" (top right) to sign up or log in.
Navigate to the S3 service.
Create a storage bucket:

Name the bucket after your project.
Choose your nearest region.
Under "Object Ownership," select "ACLs enabled" -> "Bucket owner preferred."
Under "Block Public Access," uncheck the box and acknowledge to make the bucket public.
Click "Create bucket."
Enable static web hosting:

Open the newly created bucket.
Go to the "Properties" tab.
Find "Static web hosting" and click "Enable."
Set "Index document" to index.html and "Error Document" to error.html (these files won't be used).
Configure bucket permissions:

Open the "Permissions" tab.
Copy the bucket's ARN (Amazon Resource Name).
In the "Bucket policy" section, click "Edit" -> "Policy generator."
Set the following:
Policy Type: S3 Bucket Policy
Principal: * (allow all)
Actions: Get Object
ARN: (Paste the copied ARN)
Click "Add Statement" -> "Generate Policy."
Copy the generated policy, paste it into the Bucket Policy Editor, and:
Add /* to the end of the Resource value.
Click "Save."

   

5. Paste the following code (replace this with the actual CORS configuration if you have a specific one):
[
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]

6. Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

#### **Creating AWS groups, policies and users**

Simplified Instructions

Access IAM and Create User Group

On the AWS Console, click the "Services" icon (top right) and find "IAM".
In the left menu, go to "User Groups" and click "Create Group."
Name your group (e.g., "manage-megabytes")
Create an S3 Access Policy

Click "Create Policy."
Switch to the "JSON" tab and click "Import Managed Policy" (top right).
Search for "AmazonS3FullAccess" and click "Import."
Modify the Policy

In the "Resources" section:
Replace * with your bucket's ARN.
On the next line, paste the ARN again and add /* at the end.
Click "Next: Tags" -> "Next: Review."
Name and Create the Policy

Provide a name and description (e.g., "megabytes-policy | Access to S3 bucket...").
Click "Create Policy."
Attach Policy to User Group

Navigate to "User Groups" (left menu) and select your group.
Go to the "Permissions" tab and click "Add Permissions" -> "Attach Policies."
Select your newly created policy and click "Add Permissions."
Create a User

Go to "Users" (left menu) and click "Add Users."
Create a username (e.g., "megabytes-staticfiles-user").
Select "Programmatic Access" and click "Next: Permissions."
Add User to Group

Add your user to the group you created.
Click "Next: Tags" -> "Next: Review" -> "Create User."
Retrieve Keys

Immediately download the CSV with your user's access keys. This is your only chance to obtain them.

Connecting Django to Your S3 Bucket

1. Installation

Install necessary packages and update your requirements file:

Bash
pip3 install boto3 django-storages
pip3 freeze > requirements.txt
Use code with caution.
content_copy
Add storages to INSTALLED_APPS in your settings.py file.

2. Configure Django Settings (settings.py)

Add this code, replacing placeholders with your actual values:

Python
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=9460800',
    }
    AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
    AWS_S3_REGION_NAME = 'your-region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
Use code with caution.
play_circleeditcontent_copy
3. Set Heroku Config Vars

Add these keys/values in Heroku's config vars section, using the values from your AWS CSV file:

| KEY                      | VALUE                                              |
| ------------------------ | -------------------------------------------------- |
| AWS_ACCESS_KEY_ID        | Your access key from the CSV                       |
| AWS_SECRET_ACCESS_KEY    | Your secret access key from the CSV                |
| USE_AWS                  | True                                               |

4. Setup Custom Storages

Create custom_storages.py in your project root and add:

Python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = 'static'

class MediaStorage(S3Boto3Storage):
    location = 'media'

play_circleeditcontent_copy
5. Update Django Settings (settings.py)

Python
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage' 
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

play_circleeditcontent_copy
6. Deploy and Verify

Commit and push your changes to Heroku.
Verify static files were collected during deployment.
Check your S3 bucket for the 'static' folder.
7. Create S3 Media Folder

Navigate to your S3 bucket.
Create a new folder named 'media'.

Setting up Stripe

Obtain Stripe Keys

Log into your Stripe account.
Go to "Developers" -> "API Keys".
Retrieve your publishable key and secret key.
Add Keys to Heroku Config Vars

In Heroku's settings, create two new config vars:
STRIPE_PUBLIC_KEY (paste your publishable key)
STRIPE_SECRET_KEY (paste your secret key)
Set up Webhook

In Stripe, go to "Developers" -> "Webhooks" -> "Add endpoint".
Provide your deployed site's Webhook URL (e.g., https://your-site.herokuapp.com/webhook/)
Add a description (e.g., "Webhook for my-site")
Select "Receive all events".
Click "Create endpoint".
Retrieve the generated Webhook signing secret.
Add Webhook Secret to Heroku

Create a new Heroku config var:
STRIPE_WH_SECRET (paste your Webhook signing secret)
Update Django Settings (settings.py)

Python
import os

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
Use code with caution.
play_circleeditcontent_copy
Important: Ensure you replace the placeholder Webhook URL (https://your-site.herokuapp.com/webhook/) with your actual deployed site's Webhook endpoint.



### Local Development

How to Fork the Project

Have a GitHub account: If you don't have one, sign up for free.
Find the project: Go to https://github.com/kera-cudmore/seaside-sewing.
Click "Fork": You'll find this button in the top-right corner of the project page. This creates your own copy of the project.
How to Clone the Project

Have a GitHub account: You'll need one if you don't already have it.
Find the project: Go to https://github.com/kera-cudmore/seaside-sewing.
Copy the Clone Link:
Click the "Code" button.
Choose your preference (HTTPS, SSH, GitHub CLI) and copy the provided link.
Open your Code Editor: Use the one you're comfortable with.
Choose a Folder: Decide where you want to save the project on your computer.
Use the 'git clone' Command:
In your editor's terminal, type git clone and paste the copied link. Press Enter.
Optional: Set up a Virtual Environment (Skip this if unsure or using a pre-made setup)
Install Packages: In your terminal, run pip install -r requirements.txt

---


***

## Testing

Please see [Testing Readme](/TESTING.md) for all testing for this project

## Feedback

### Peer Feedback

I have worked closely with my peers on testing this product rigorously for any errors. The feedback is as follows:

- Some of the pages do not seem to be responding well on smaller screens. The input boxes seem to come out of the container.

- The order form does not require a postcode

- The quantity-selection div cannot be seen on smaller screens

- 

### Responding to Peer Feedback

I have taken the following actions in response to feedback:

- Used multiple media queries to adjust the parent container so that the input boxes are never out of the container.
- Applied a 'position: fixed' style to the main footer container

### Feedback from previous projects

### Responding to feedback from previous projects

I have retested all user stories, responsiveness and each element after changes were made and asked for further feedback. No errors or suggestions were offered

### Other Feedback

My mentor suggested that I display a warning to a user about the impact of deleting a review.

### Responding to other feedback

I have included this just above the submit button.

***

## Future Developments

- I plan to create functionality for users to customise their sandwich from the bread to type of filling. 

- I would like to revisit process_checkout and rewrite it so that I do not need to rely on the work-around mentioned in 'Known Bugs'

- I would like to introduce other products such as sundries, drinks, sauces when I release this for an audience

- Early on I tried to create increase and decrease buttons rather than a select box for the quantity, however I could not get this to work. I would like to revisit this

- I would like to introduce images of each product once the project is released for an audience

***

## Credits

### Content

Content for the website was written by Dan Matthews.

### Code Used

#### Hamburger Bar

I have used Bootstrap's Nav bar as a template to create my own. It can be found [here](https://getbootstrap.com/docs/5.3/components/navbar/)

#### Star Rating system

I have adapted Coding Pal Web's star rating CSS and JavaScript. The full code can be found here: https://www.codingnepalweb.com/star-rating-html-css-javascript-2

***

## Acknowledgments

Finally, I want to take the opportunity to thank and acknowledge the following for their support and patience in helping me create my first-ever project:

- [Harry Dhillon](https://github.com/Harry-Leepz), who is my mentor at the Code Institute, for their continued support and guidance.
  
- Kofi Afriyie and Meena Mengle, who are my facilitators from West Herts College, for their time, patience and encouragement in helping me develop this project.
  
- Craig Hudson, for his patience and pep-talks throughout, and for helping to test my finished project
  
- Jordan Cooper, for helping to test my finished project and suggestions along the way


