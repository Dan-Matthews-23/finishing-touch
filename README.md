SETUP

I have used tutorials given by the Code Institude to set up this project. Specificaly, this relates to setting up base and index.html. The file and block names are identical, although it should be noted that familiarity across all students' projects at this stage is to be expected.




## Local Legends

[View deployed site on Heroku]()

[View Local Legends on Github]()

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

![Local Legends Index Desktop](/media/images/concept/user-stories)


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


### Webpage layout

#### Master Template

The Master Template, called base.html, will be used as a template for all pages in this project. It will hold the header, footer and nav bar.

![Coolers Palatte](/media/images/concept/base.png)

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


#### Index

The homepage will consist of a selection of the top four most popular products. In the concept stage I will create a skeleton layout of the page and fill it with placeholder images and text. 

Homepage Design: ![Homepage Design](/media/images/concept/concept-index.png)


#### Register and Login

I have used Django Allauth to provide functionality for Megabytes. I have adapted the templates for customised experience


Homepage Design: ![Homepage Design]()

#### Profile

The user will have one profile page where they can view previous orders and update their personal information

Homepage Design: ![Homepage Design]()

#### Order History

The user will be able to view all of their previous orders


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


