SETUP

I have used tutorials given by the Code Institude to set up this project. Specificaly, this relates to setting up base and index.html. The file and block names are identical, although it should be noted that familiarity across all students' projects at this stage is to be expected.




## Local Legends

[View deployed site on Heroku](https://megabytes-bfd0afc9e4a4.herokuapp.com/)

[View Local Legends on Github](https://github.com/Dan-Matthews-23/mega-bytes)

![Am I responsive]()

MegaBytes is a fully responsive ecommerce web application designed for local residents of Sunderland as a takeaway-ordering platform. The order will be fully customizable, will allow users to chose a payment method, create an account, browse a menu, update details such as address and delete orders or accounts. 

The product available at MegaBytes is healthy sandwitches with full nutritional information

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

![Megabytes User Stories](/media/images/concept/user-stories)


### Wireframes

I have designed five wireframes per web page to coincide with Bootstrap's five breakpoints: 

Extra small	None	<576px
Small	sm	≥576px
Medium	md	≥768px
Large	lg	≥992px
Extra large	xl	≥1200px
Extra extra large	xxl	≥1400px


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

I will be using Bootstrap to set the layout of this project. I will be using a range of features including the the grid, nav bar and breakpoints to ensure it's responsive. 

#### Colour

I have not chosen to implemenet a colour palette in this project. Instead, the colours available will be black and off white (F7F9F9). 

#### Font

The font I have chosen to use for this project is one called Poppins, which is part of the Sans Sarif family. It can be found [here](https://fonts.google.com/specimen/Poppins). I chose the 'Light 300' weighting as I felt that it would stand out a little more than the 'thin' preset. I have used this font in my other projects and feel it's just right on the eye. I have also used Nanum Pen Script for the Chef Message to give the effect of handwriting. It can be found [here](https://fonts.google.com/specimen/Nanum+Pen+Script).


### Webpage layout

#### Master Template

The Master Template, called base.html, will be used as a template for all pages in this project. It will hold the header, footer and nav bar.

![Am I responsive]()

#### Header

The header incorperates the project title and nav bar. 

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

If a superuser, the user can create, read, update and delete products. This can be acessed via the nav bar and will only show for those who are superusers

Manage Products: ![Am I Responsive]()


***

## Accessibility

### WAVE Report

The WAVE report returned no errors and three alerts:

- Suspicious link. This refers to the 'Register' link in the index page. As this is not an error and only a suggestion, I have chosen to disgegard this suggestion. I do not feel rewording 'Register' to anything else would be appropiate. 

- Justified Text. This referes to Chef Message block being set with a 'Justify' CSS style. I have followed this suggestion and changed this to 'Centre'. However I cannot locate the second block of text this suggestion refers to as the WAVE report.

### Contrast Ratio

I have been unable to use WebAIM's contrast ratio on MegaBytes. I believe it may be a conflict between Heroku and WebAIM. 

***

## Justifications and reflections

### Justifications

#### Image use

I have opted not to use images in MegaBytes. Finding images that match the specific specifications including colour, bread type, background colour, filling etc proved too problematic. I have kept the original model structure however as this project is going to be deployed as a live project for real-world application, and when that happens we will be able to create images for the new products directly. This means there is already an image_url field in the products model ready for use. 

#### Categories

The products that the user can see on the products page all have a category_id of 9. This is because when we apply this project template to our business, other items such as sundries, drinks, add-ons will all have their own category_id so they can be easily sorted. For the purposes of this project only the one category was needed, but the structure is there for additional options.

#### Limited colour palette

I took inspiration for this project from sucessful food apps such as Just Eat. I note that their three primary colours are white, black and orange. I wanted to replicate that simplistic approach and have adopted a similar colour scheme.

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
| Contrast Ratio              | [webAIM](https://webaim.org/)                                |
| Accessibility (WAVE report) | [webAIM](https://webaim.org/)                                |
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

4. Under 'DATABASES', comment out the existing code. Type: DATABASES = { 'default': dj_database_url.parse('paste-elephantsql-db-url-here')  } 

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```

8. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.
9. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):

    ```python
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
    ```

10. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

11. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

    ```Procfile
    web: gunicorn seaside_sewing.wsgi:application
    ```

12. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
    ```

13. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

    ```python
    ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
    ```

14. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

    ```bash
    heroku git:remote -a {app name here}
    git push heroku master
    ```

15. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

16. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

#### **Generate a SECRET KEY & Updating Debug**

1. Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.
2. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/) is an example of a site we could use to create our secret key. Create a new key and copy the value.
3. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key we just created. Click add.
4. In settings.py we can now update the `SECRET_KEY` variable, asking it to get the secret key from the environment, or use an empty string in development:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

5. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

6. Save, add, commit and push these changes.

#### **Set up AWS hosting for static and media files**

! NOTE: These instructions are for setting up AWS hosting as of 5/1/23 - these may change slightly in future versions of AWS.

1. Sign up or login to your [aws amazon account](https://aws.amazon.com) on the top right by using the manage my account button and then navigate to S3 to create a new bucket.
2. The bucket will be used to store our files, so it is a good idea to name this bucket the same as your project. Select the region closest to you. In the object ownership section we need to select ACLs enabled and then select bucket owner preferred. In the block public access section uncheck the block public access box. You will then need to tick the acknowledge button to make the bucket public. Click create bucket.
3. Click the bucket you've just created and then select the properties tab at the top of the page. Find the static web hosting section and choose enable static web hosting, host a static website and enter index.html and error.html for the index and error documents (these won't actually be used.)
4. Open the permissions tab and copy the ARN (amazon resource name). Navigate to the bucket policy section click edit and select policy generator. The policy type will be S3 bucket policy, we want to allow all principles by adding `*` to the input and the actions will be get object. Paste the ARN we copied from the last page into the ARN input and then click add statement. Click generate policy and copy the policy that displays in a new pop up. Paste this policy into the bucket policy editor and make the following changes: Add a `/*` at the end of the resource value. Click save.
5. Next we need to edit the the cross-origin resource sharing (CORS). Paste in the following text:

    ```json
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
    ```

6. Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

#### **Creating AWS groups, policies and users**

1. Click the services icon on the top right of the page and navigate to IAM - manage access to AWS services. On the left hand navigation menu click user groups and then click the create group button in the top right. This will create the group that our user will be placed in.
2. Choose a name for your group - for example manage-seaside-sewing, and click the create policy button on the right. This will open a new page.
3. Click on the JSON tab and then click the link for import managed policy on the top right of the page.
4. Search for S3 and select the one called AmazonS3FullAccess, then click import.
5. We need to make a change to the resources, we need to make resources an array and then change the value for resources. Instead of a `*` which allows all access, we want to paste in our ARN. followed by a comma, and then paste the ARN in again on the next line with `/*` at the end. This allows all actions on our bucket, and all the resources in it.
6. Click the next: tags button and then the next:review .
7. Give the policy a name and description (e.g. seaside-sewing-policy | Access to S3 bucket for seaside sewing static files.) Click the create policy button.
8. Now we need to atach the policy we just created. On the left hand navigation menu click user groups, select the group and go to the permissions tab. Click the add permissions button on the right and choose attach policies from the dropdown.
9. Select the policy you just created and then click add permissions at the bottom.
10. Now we'll create a user for the group by clicking on the user link in the left hand navigation menu, clicking the add users button on the top right and giving our user a username (e.g. seaside-sewing-staticfiles-user). Select programmatic access and then click the next: permissions button.
11. Add the user to the group you just created and then click next:tags button, next:review button and then create user button.
12. You will now need to download the CSV file as this contains the user access key and secret access key that we need to insert into the Heroku config vars. Make sure you download the CSV now as you won't be able to access it again.

#### **Connecting Django to our S3 bucket**

1. Install boto3 and django storages and freeze them to the requirements.txt file.

    ```bash
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ```

2. Add `storages` to the installed apps in settings.py
3. Add the following code in settings.py to use our bucket if we are using the deployed site:

    ```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }
        
        AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
        AWS_S3_REGION_NAME = 'enter the region you selected here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```

4. In Heroku we can now add these keys to our config vars:

    | KEY | VALUE |
    | :--- | :--- |
    | AWS_ACCESS_KEY_ID | The access key value from the amazon csv file downloaded in the last section |
    | AWS_SECRET_ACCESS_KEY | The secret access key from the amazon csv file downloaded in the last section |
    | USE_AWS | True |

5. Remove the DISABLE_COLLECTSTATIC variable.
6. Create a file called custom_storages.py in the root and import settings and S3Botot3Storage. Create a custom class for static files and one for media files. These will tell the app the location to store static and media files.
7. Add the following to settings.py to let the app know where to store static and media files, and to override the static and media URLs in production.

    ```python
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

8. Save, add, commit and push these changes to make a deployment to Heroku. In the build log you should be able to see that the static files were collected, and if we check our S3 bucket we can see the static folder which has all the static files in it.
9. Navigate to S3 and open your bucket. We now want to create a new file to hold all the media files for our site. We can do this by clicking the create folder button on the top right and naming the folder media.

#### **Setting up Stripe**

1. We now need to add our Stripe keys to our config vars in Heroku to keep these out of our code and keep them private. Log into Stripe, click developers and then API keys.
2. Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.
3. Now we need to add the WebHook endpoint for the deployed site. Navigate to the WebHooks link in the left hand menu and click add endpoint button.
4. Add the URL for our deployed sites WebHook, give it a description and then click the add events button and select all events. Click Create endpoint.
5. Now we can add the WebHook signing secret to our Heroku config variables as STRIPE_WH_SECRET.
6. In settings.py:

    ```python
    STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
    STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
    ```

### Migrating to Railway.app for deployment

*Update: 29th April 2023* Since completing my diploma and due to Heroku removing their free tier in November 2022, I have migrated the deployment of this site to use railway.app. You can find instructions on how to migrate your app from Heroku to Railway in my [article here](https://www.codu.co/articles/migrating-your-heroku-app-to-railway-vf9p3kid).

Note that you will also need to create a runtime.txt in your environment which contains the version of python you are using. You can find this out by typing `python --version` in the terminal, and entering the result into the runtime.txt folder like so:

```
Python -3.10.5
```

### Local Development

#### **How to Fork**

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [seaside-sewing](https://github.com/kera-cudmore/seaside-sewing).

3. Click on the fork button in the top right of the page.

#### **How to Clone**

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [seaside-sewing](https://github.com/kera-cudmore/seaside-sewing).

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod as this will have been set up for you).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

```bash
pip3 install -r requirements.txt
```

---







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


