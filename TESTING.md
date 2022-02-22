# Testing 

The following sections are the results of the testing throughout the software development lifecycle for project "MSP-5 MochaBean". This information has been included in a separate document in order to keep the [README document](https://github.com/Sphere42/MSP-5/blob/main/README.md) uncluttered.

# Table of Contents
1. [Testing Plan](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#testing-plan)
1. [Testing Tools](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#testing-tools)
1. [Sprint 1](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-1)
1. [Sprint 2](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-2)
1. [Sprint 3](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-3)
1. [Sprint 4](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-4)
1. [Sprint 5](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-5)
1. [Sprint 6](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-6)
1. [Sprint 7](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-7)
1. [Sprint 8](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-8)
1. [Sprint 9](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-9)
1. [Sprint 10](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#sprint-10)
1. [WAVE validation](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#wave-validation)
1. [Final Post Deployment Testing](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#final-post-deployment-testing)
	1. [Final Compatability Testing](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#final-compatability-testing)
	1. [Final Code Validation](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#final-code-validation)
	1. [General Site validation](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#general-site-validation)
	1. [User Acceptance Testing:](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#user-acceptance-testing)
	1. [Performance Testing:](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#performance-testing)
1. [Unfixed bugs](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#unfixed-bugs)
1. [Improvements to current features](https://github.com/Sphere42/MSP-5/blob/main/TESTING.md#improvements-to-current-features)


## Testing Plan

Testing will be conducted regularly alongside the development of this project. Each user story will include some unit testing of the code being developed as well as manual exploratory test sessions.

During the manual exploratory test sessions:
* Test cases will be identified for test automation
* Site functionality will be verified
* Cross browser/device compatibiliy will be confirmed
* General usibility will be assessed

Upon initial deployment the following testing will be conducted: 
* All available unit tests
* Manual shakedown of all functionality
* Performance testing of site loading
* Device and cross browser compatibility
* WAVE web accessibility tests
* WAI color contrast assessments (of the final colours and patterns)


## Testing Tools

The following list of tools have been utilised during the testing of this project:
* [screen to gif](https://www.screentogif.com/)
 * Used for Evidence collection
  
* [unittest - Django built in unit test application](https://docs.djangoproject.com/en/3.2/topics/testing/overview/)
 * Used for python unit testing

* [WAVE Validation](https://wave.webaim.org/)
 * Used for python unit testing

* [WAVE - colour assesment](https://juicystudio.com/services/luminositycontrastratio.php)
 * Used for python unit testing

* [HTML Validator](https://validator.w3.org/)
 * Used for python unit testing

* [CSS Validator](https://jigsaw.w3.org/css-validator/)
 * Used for python unit testing

* [PEP8 Python Validation](http://pep8online.com/)
 * Used for python unit testing


## Sprint 1 
11th December - 17th December 2021

### User Stories Closed
* As a Developer I want to see the base Django app has been created

### Unit Tests Conducted
No Unit Tests were built as part of this Sprint

### Exploratory Test Session Goals
* I want to confirm that the base project has been created
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
No potential Automation Test Cases were identified during this sprint

### Issues Faced / Found
No Issues were faced / found as part of this Sprint

### Python Validation
No Python validation occured during this Sprint


## Sprint 2 
18th December - 24th December 2021

### User Stories Closed
* As a Developer I want to see the base html templates in place
* As a User I want to view the initial landing page for the site
* As a User I want to view the store policies

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_19.12.21_1.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_19.12.21_coverage.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_23.12.21_1.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_23.12.21_coverage.PNG" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals
* I want to confirm the inital landing page loads correctly
* I want to confirm the Policies page loads correctly
* I want to confirm the Navigation bar has been updated for the landing page and policies pages
* I want to confirm that the base templates load as expected
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
* Landing page loading as expected
* Policies page loads correctly
* Policies page loads from footer navigation

### Issues Faced / Found
* None located at this time


## Sprint 3
25th December - 31st December 2021

### User Stories Closed
* As a User I want to view the FAQ page
* As a User I want to know what the delivery/returns policies are

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_26.12.21_1.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_26.12.21_2.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_26.12.21_coverage.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_27.12.21_1.PNG" alt="Initial Python Unit Test"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_27.12.21_coverage.PNG" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals

* I want to confirm the FAQ page loads correctly
* I want to confirm that each question expands to show the answer when selected
* I want to confirm that the shipping page loads correctly
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
* FAQ page loads and questions expand
* Shipping page loads

### Issues Faced / Found
* Initial issue while creating the Database for users, there was a conflict between the customer model and the django defaul user model. This was resolved by changing the custom app name to customers.


## Sprint 4
1st January 2022 - 7th January 2022

### User Stories Closed
* As a User I want to be able to log in
* As a User I want to be able to know more about MochaBeans
* As a User I want to become a member
* As a User I want to be able to log out

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_07.01.22_1.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_07.01.22_2.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_07.01.22_3.PNG" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals

* I want to confirm that I can Register as a new User
* I want to confirm that if the register form is invalid then error(s) will display
* I want to confirm that once registered the user is directed to the login page (and not automatically logged in)
* I want to confirm that as an existing user I can log in
* I want to confirm that if the login form is invalid then error(s) will display
* I want to confirm that there is a link at the base of the register form for existing users to go to the login page
* I want to confirm that there is a link at the base of the login form for new users to go to the register page
* I want to confirm that as a logged in user the username appears in the nav bar along with a placeholder dropdown menu
* I want to confirm that as an annonymous user, a login button will appear in the top nav bar
* I want to confirm that the About MochaBeans page loads and there is a link in the nav bar
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
* Registering a new user
* Field validation - negative tests
* User login
* Switch between login and register pages
* Navigation bar updates with User details

### Issues Faced / Found
N/A

## Sprint 5
8th January 2022 - 14th January 2022

### User Stories Closed
* As a User I want to be able to reset my password
* As a User I want the reset password forms to be aligned with MochaBean theme

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_14.01.22_1.PNG" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals

* I want to confirm that when I request a password reset an email is sent
* I want to confirm the email sent has a reset password link
* I want to confirm that when I have reset my password I must use the new password to log in
* I want to confirm the password change screen contains password validation
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
* Password reset process

### Issues Faced / Found
* No issues raised during this sprint

## Sprint 6
15th January - 21st January 2022

### User Stories Closed
* As a User I want to be able to delete my account
* As a Developer I want to implement the following customer model / database
* As a User I want to subscribe to the MochaBean newsletter
* As a User I want to be able to view my current details (Profile page)
* As a User I want to be able to update my details
* As a User I want to subscribe to the MochaBean newsletter

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_1.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_2.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_3.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_4.PNG" alt="Initial Python Unit Test"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_5.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_coverage.PNG" alt="Initial Python Unit Test"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/unit_testing/python_21.01.22_coverage_1.PNG" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals

* I want to be able to delete my account (and profile)
* I want to confirm that a profile is created with a User registers
* I want to view my current profile details
* I want to confirm that if my profile details are empty, upon first visit I will be redirected to the update page
* I want to be able to update my details
* I want to be able to subscribe to the MochaBean newsletter
* I want to confirm that if I am already subscribed to the Newsletter I cannot add my email again
* I want to be able to unsubscribe from the newsletter
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
* Deleting account (and profile)
* View Profile details
* Amend profile details
* MochaBean Newsletter subscription

### Issues Faced / Found
* None

## Sprint 7
22nd January - 28th January 2022

Due to other commitments no progress was made during this time

## Sprint 8
29th January - 4th February 2022

Due to other commitments no progress was made during this time

## Sprint 9
5th February 2022 - 11th February 2022

Due to other commitments no progress was made during this time

## Sprint 10
12th February 2022 - 22nd February 2022

### User Stories Closed
* As a User I want to know if I payment was successful
* As a User I want to select a subscription
* As a logged in User I want to pay for my subscription
* As a logged in User I want to view my current subscriptions
* As a User I want to contact Customer service
* As a User I want to know if my payment was unsuccessful
* As a staff member I want to delete a product
* As a staff member I want to amend a current product
* As a staff member I want to create a new product
* As an Admin User I need to setup stripe payment service
* As a User I want to leave feedback/review
* As a Admin user I want to setup a "fake" facebook account
* As a user i want to see a custom 404 page
* As a User I want to view available subscriptions

### Exploratory Test Session Goals

* I want to confirm that if a payment is unsuccessful I am notified
* I want to confirm that I can select a subscription product
* I want to be able to enter payment details to purchase a subscription
* I want to confirm that if a payment is successful I am notified
* I want to view what subscription I have purchased
* I want to be able to contact customer service
* I want to confirm that as a staff member I can create/amend/delete products
* I want to confirm that as a staff member I can cannot purchase a subscription
* I want to confirm that payments are processed via stripe
* I want to confirm that I can see all available subscriptions/products
* I want to confirm I can leave feedback
* I want to confirm the customer 404 page is display were required
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

### Potential Automation Test Cases
* Create/amend/delete/view product-subscriptions
* Confirm payment process
* Contact/feedback forms
* 404 page loads

### WAVE validation
The following are the results from the WAVE validation site to verify accessibility and readability.
Note: There have been no errors raised due to the use of a pattern/texture on the body of the site.

* Home page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/home.PNG" alt="WAVE Results for home page"/>
</p>

* About page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/about.PNG" alt="WAVE Results for about page"/>
</p>

* FAQ page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/faq.PNG" alt="WAVE Results for FAQ page"/>
</p>

* Policies page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/policies.PNG" alt="WAVE Results for policies page"/>
</p>

* Shipping page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/shipping.PNG" alt="WAVE Results for the shipping page"/>
</p>

* Customer Login page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/login.PNG" alt="WAVE Results for login page"/>
</p>

* Customer Registration page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/register.PNG" alt="WAVE Results for register page"/>
</p>

* Subscription Products page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/products.PNG" alt="WAVE Results for products page"/>
</p>

* 404 page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/404.PNG" alt="WAVE Results for 404 screen"/>
</p>

* Feedback page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/feedback.PNG" alt="WAVE Results for feedback page"/>
</p>

* Reset Password page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/reset_password.PNG" alt="WAVE Results for reset password page"/>
</p>

* Reset Password Complete page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/reset_password_complete.PNG" alt="WAVE Results for reset password complete page"/>
</p>

* Reset password email sent page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/reset_password_sent.PNG" alt="WAVE Results for reset password email sent page"/>
</p>

* Newsletter Unsubscribe page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/unsubscribe.PNG" alt="WAVE Results for the newsletter unsubscribe page"/>
</p>

* Newsletter Unsubscribed page WAVE analysis

<p float="left">
    <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/wave_testing/unsubscribed.PNG" alt="WAVE Results for the newsletter unsubscribed page"/>
</p>

## Final Post Deployment Testing

### Final Compatability testing:

The following Gifs are evidence collected from the compatability testing of the MSP-5 project (mochabean)

<details>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/chrom_log.gif" alt="testing with chrome"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/chrom_purchase.gif"  alt="testing with chrome"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/edge.gif" alt="testing with edge"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/firefox.gif" alt="testing with firefox"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/nest_hub.gif" alt="testing with nest hub"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/pixel5_nav.gif" alt="testing with pixel 5"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/pixel5_user.gif" alt="testing with pixel 5"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/device/surface_duo.gif" alt="testing with surface duo"/>
    </p>
</details>

#### HTML Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/404.PNG" alt="HTML Validation Results for 404 page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/about.PNG" alt="HTML Validation Results for about page"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/faq.PNG" alt="HTML Validation Results for faq page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/feedback.PNG" alt="HTML Validation Results for feedback page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/home.PNG" alt="HTML Validation Results for home page"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/login.PNG" alt="HTML Validation Results for login page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/password_reset.PNG" alt="HTML Validation Results for password reset page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/password_reset_complete.PNG" alt="HTML Validation Results for password reset complete page"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/password_reset_sent.PNG" alt="HTML Validation Results for password reset email sent page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/policies.PNG" alt="HTML Validation Results for policies page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/products.PNG" alt="HTML Validation Results for products page"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/register.PNG" alt="HTML Validation Results for register page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/shipping.PNG" alt="HTML Validation Results for shipping page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/unsubscribe.PNG" alt="HTML Validation Results for unsubscribe page"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/html_test/unsubscribed.PNG" alt="HTML Validation Results for unsubscribed page"/>
    </p>
</details>

#### CSS Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/css_test/css.PNG" alt="CSS Validation Results for only css"/>
    </p>
</details>

#### Python Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/customers_forms.PNG" alt="Python Validation Results for customes forms.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/customers_models.PNG" alt="Python Validation Results for customes models.py"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/customers_tests.PNG" alt="Python Validation Results for customes tests.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/customers_urls.PNG" alt="Python Validation Results for customes urls.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/customers_view.PNG" alt="Python Validation Results for customes view.py"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/mochabean_tests.PNG" alt="Python Validation Results for mochabean tests.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/mochabean_urls.PNG" alt="Python Validation Results for mochabean urls.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/mochabean_views.PNG" alt="Python Validation Results for mochabean views.py"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/subscriptions_forms.PNG" alt="Python Validation Results for subscriptions forms.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/subscriptions_models.PNG" alt="Python Validation Results for subscriptions models.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/subscriptions_tests.PNG" alt="Python Validation Results for subscriptions tests.py"/>
		<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/subscriptions_urls.PNG" alt="Python Validation Results for subscriptions urls.py"/>
        <img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/python_test/subscriptions_views.PNG" alt="Python Validation Results for subscriptions views.py"/>
    </p>
</details>

## Final User Acceptance Testing:

Due to the size and timelines of this project, there will not be a structured Alpha/Beta stage of UAT outside of the sprints. Instead, a selection of volunteers will conduct a time boxed exploratory sessions within each sprint once Minimum Viability has been achieved. After which feedback will be collated and transformed into defects, improvements or new features.

This feedback has been included above within the applicable sprint and incorporated into the project where appropriate.

Once the final code was deployed via Heroku, the original testers completed a final round of User Acceptance Testing (Beta).

## Performance Testing:
The following evidence are the results from the performance speed test conducted on the deployed site:
<p float="left">
<img src="https://github.com/Sphere42/MSP-5/blob/main/static/images/readme/performance.PNG" alt="Performance Results of the home page"/>
</p>

### Issues located
- The stripe payment checkout only allows a very small number of calls/activations per minute. If this limit is exceeded it will attempt to open a new tab with an error message
- Edge and firefox have varying virtical heights. therefore the high has been extended to suit all browsers


# Unfixed bugs 
- Django default User authentication process is case sensitive for Usernames. While this does increase the availability of Usernames available to members, it may cause some confusion when logging in. Therefore a future feature will be to adjust the Username field to be case insensitive. Currently the placeholder text for the field indicates case sensitivity.
- On the Product Update page the fields are the default Django form fields due to issues displaying existing information. Defect allow to go to prod and it is not effecting customers
- Login/Register screen length is slightly longer then required on some devices due to incompatibility across browsers


# Improvements to Current features
* Ability to sent the Newletter
* Ability for User to amend subscription
* Ability to delete subscription without deleting the account
* Ability for staff member to pull a list of all product subscriptions
* Currently only card payments are accepted via Stripe - addition of PayPay/Crypto in the furture
