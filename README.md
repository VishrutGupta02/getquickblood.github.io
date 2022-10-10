# getQuickBlood.com

### Vishrut Gupta
### Delhi, India
</br>

### <ins>Video demo</ins>: click [here](https://youtu.be/bUveZLK9bkQ)
<br>

## <ins>***DESCRIPTION:***</ins>
The coronavirus pandemic was an unprecedented global pandemic. It drastically affected us and everyone around us. It had no vaccine or cure for a long time and the lack of medical products such as medicines, injections, oxygen tanks, and blood worsened the situation. I made 'getQuickBlood.com' to work as an online blood bank that connects people in desperate need of blood with those willing to donate it. One may need a blood transfusion if they have lost blood from an injury or during surgery, or if one has certain medical conditions including Anaemia, Certain cancers, Haemophilia, Sickle cell disease, etc. Also, one cannot use just any available blood as multiple tests need to be undertaken before one can use someone else's blood and sometimes even hospitals prove ineffective in helping to find suitable blood donors. I have made 'getQuickBlood.com' in an attempt to help such people in dire and urgent need of blood. I am also working to collaborate with hospitals and other blood banks to popularise the website so an increasing number of people can benefit from it.\
The website makes use of python, CSS, and HTML languages.\
Moreover, javascript has been embedded from bootstrap for styling.\
Display and storage of data is done using SQL commands.\
The major styling including the backgrounds, fonts, colors, etc was done at the end; followed by making the website look responsive on all kinds of devices whether it be a mobile or a laptop.

</br>

## <ins>***STRUCTURE***</ins>
The website has 5 major web pages and 1 database. There is also a header present at the top of all pages to help in easy movement across the website.

</br>

### _STATIC_
>The static directory is a directory of static files, like images and CSS, and the database used in the website.\
The database has 3 tables: donors, compatible, and waitlist.\
‘donors’ contains a list of all the information about the donor as provided by them. It includes their first name, last name, blood group, email, mobile(optional), age, pinched, state, country, any optional additional information they want to give, and their passwords.\
‘compatible’ contains a list of all the various blood types and the blood type that they are compatible with. This table is used when sending a query to select data from the donors table when a receiver comes for blood.\
‘waitlist’ consists of the data of the people who have given their names for the waitlist. It contains their full name, blood group, email,  mobile(optional), pin code, state, and country.\
'styles.css' file is the CSS file that contains the styling of the various elements of the HTML sites. It has already been linked to all the HTML files.

</br>

### _TEMPLATES_
>It is a directory containing the HTML files that form our pages.\
It contains index.html, donate.html, help.html, helpdata.html, waitlist.html, collaborators.html, delete.html, and faq.html.\
All of them together ensure the smooth working of the site.\
We shall learn more about them and their use in the ‘working’ of the website.

</br>

### _app.py_
>It will have the Python code for our web server.

</br>

### _requirements.txt_
>It includes a list of required libraries for our application.

</br>
</br>

## <ins>***WORKING***</ins>
The website first opens with the index page(index.html). It has the option to direct us to various parts of the website as per consumer needs. One can go to donate blood, request blood, see the waitlist, know more about the website and its success by visiting the collaborators page, or for any doubts, visit the frequently asked questions page. We will discuss all of them in detail in the following paragraphs.

</br>

### _Requesting blood_
>To begin, let us consider probably the most important aspect of the website, the recipients' page.\
If the user clicks on ‘Request help’ on the index page then they will be redirected to ‘help.html’. Here they will first be asked to fill in all the appropriate details. There is also a check pre-installed for different data and a scroller has been provided for selecting blood group.\
Once this data is submitted, then the user is redirected to ‘helpdata.html’. On this page, the user is shown the suitable donors from our database available for the recipient. The suitability of data is determined by a variety of factors.\
First, the compatibility of the blood group is checked. Then of the people with compatible blood groups, the data is displayed by filtering it based on country and state and then sorting it based on pin-code. If no donor with a compatible blood group is available from the same country, then all the available data is shown after filtering just on the basis of blood group.\
At the bottom, there is also a question asking whether the user got the required help or not. If the user selects ‘no’ then their name is added to the waitlist.

</br>

### _Waitlist_
>If the user clicks on ‘See waitlist’ on the index page then the 'waitlist.html' page is displayed.\
It can help someone anonymously help others in need without actually registering themselves on the website. Since the website has been made for the sole purpose to help people so whether someone registers themselves to help or not is of little importance if they are ready to donate anonymously by directly contacting the receiver.\
Also, if a new donor comes whose blood group is required by any one of the people in waitlist, then all those people will be sent an automated email giving them details of the new donor and then their names will be cut off from waitlist.

</br>

### _Donating blood_
>Having more and more donors is an essential part of the website.\
If the user clicks on ‘Donate Blood’ on the index page then they shall be redirected to ‘donate.html’ where we ask for the required data of the user.\
Certain criteria such as an age group of 18 - 65 have to be met for one to be able to donate blood. We have tried to inculcate some of these checks on the website before asking for blood but still, lab tests need to be done before the final transfusion of blood.\
There is also a test conducted to make sure that the repetition of passwords does not take place when a donor is registering themselves.\
If all the details are accepted then the data is inserted in the 'donors' table of our database.

</br>

### _Collaborators_
>If the user clicks on 'See collaborators and donors' on the index page then the 'collaborators.html' file is displayed.\
This page contains a list of the organizations and hospitals we have partnered with. A greater number of organizations and seeing the names of known organizations would help people gather their trust in the product and use its services. Also, these hospitals and blood banks would send people to this website when, god forbid, they deem unsuccessful in helping the patient.\
Another part of this page is the list of generous donors we display.\
Furthermore, if any of the donors enters their password in the field given in front of their name then their data shall be deleted from our database. A confirmation is also asked before the data is deleted.

</br>

### _FAQs_
>If the user clicks on 'FAQ' on the index page then the Frequently asked questions page (faq.html) is displayed.\
Here we answer some of the general questions that we think might arise when a user accesses the website.

</br>


responsiveness
