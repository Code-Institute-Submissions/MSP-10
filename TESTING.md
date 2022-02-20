# Testing 

The following sections are the results of the testing throughout the software development lifecycle for project "MSP-5 MochaBean". This information has been included in a separate document in order to keep the [README document]() uncluttered.

# Table of Contents
1. [Testing Plan]()
1. [Testing Tools]()
1. [Sprint 1]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 2]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 3]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
	1. [Python Validation]()
1. [Sprint 4]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 5]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 6]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 7]()
1. [Sprint 8]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 9]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint 10]()
    1. [User Stories Closed]()
    1. [Unit Tests Conducted]()
    1. [Exploratory Test Session Goals]()
	1. [Potential Automation Test Cases Identified]()
	1. [Issues found/faced]()
1. [Sprint Deployment]()
1. [Final Post Deployment Testing]()
	1. [Final Compatability Testing]()
	1. [Final Code Validation]()
		1. [HTML Validation]()
		1. [CSS Validation]()
		1. [JavaScript Validation]()
		1. [Python Validation]()
	1. [General Site validation]()
	1. [User Acceptance Testing:]()
	1. [Performance Testing:]()
		1. [Issues Located]()
		1. [Warnings Located]()
	1. [Final WAVE Accessibility Assessment]()
1. [Unfixed bugs/ Improvements to current features]()


## Testing Plan

Testing will be conducted regularly alongside the development of this project. Each user story will include some unit testing of the code being developed as well as manual exploratory test sessions.

During the manual exploratory test sessions:
* Test cases will be identified for test automation
* Site functionality will be verified
* Cross browser/device compatibiliy will be confirmed
* General usibility will be assessed

Upon initial deployment of the MVP the following testing will be conducted: 
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
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
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

<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

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
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals

* I want to confirm the FAQ page loads correctly
* I want to confirm that each question expands to show the answer when selected
* I want to confirm that the shipping page loads correctly
* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

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
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
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

<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

### Potential Automation Test Cases
* Registering a new user
* Field validation - negative tests
* User login
* Switch between login and register pages
* Navigation bar updates with User details

### Issues Faced / Found
N/A

### Python Validation
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>


## Sprint 5
8th January 2022 - 14th January 2022

### User Stories Closed
* As a User I want to be able to reset my password
* As a User I want the reset password forms to be aligned with MochaBean theme

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
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

<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

### Potential Automation Test Cases
* Password reset process

### Issues Faced / Found
* No issues raised during this sprint

### Python Validation
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>


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
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
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

<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

### Potential Automation Test Cases
* Deleting account (and profile)
* View Profile details
* Amend profile details
* MochaBean Newsletter subscription

### Issues Faced / Found
* None

### Python Validation
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

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
* 

### Unit Tests Conducted
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

### Exploratory Test Session Goals

* I want to confirm that all User Stories are done to my satisfaction
* I want to identify any edge cases
* I want to identify any potential test cases for automation

<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>

### Potential Automation Test Cases
* 
* 
* 

### Issues Faced / Found
* 
* 
* 

### Python Validation
<details>
<summary> Expand for test results</summary>
    <p float="left">
        <img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
		<img src="" alt="Initial Python Unit Test"/>
    </p>
</details>


### WAVE validation
The following are the results from the WAVE validation site to verify accessibility and readability.
Note: There have been no errors raised due to the use of a pattern/texture on the body of the site.

* Home page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* About page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* FAQ page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Policies page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Shipping page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Customer Login page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Customer Registration page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Customer Profile page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Customer Amend Profile page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Customer Delete Profile page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Subscription Products Create page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Subscription Products Amend Profile page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>

* Subscription Products Delete Profile page WAVE analysis

<p float="left">
    <img src="" width="300" height="200" alt=" WAVE Results"/>
</p>



Items requiring change based on the WAVE assessment are:
* 
* 
* 



## Final Post Deployment Testing

### Final Compatability testing:

The following Gifs are evidence collected from the compatability testing of the MSP-4 project (studyWorld)

<details>
    <summary><b>__iphone6/7/8 plus__</b></summary>
    Device width: 414px
    <p float="left">
        <img src="" width="300" height="200" alt="iphone6/7/8 plus test results for "/>
		<img src="" width="300" height="200" alt="iphone6/7/8 plus test results for "/>
		<img src="" width="300" height="200" alt="iphone6/7/8 plus test results for "/>
		<img src="" width="300" height="200" alt="iphone6/7/8 plus test results for "/>
		<img src="" width="300" height="200" alt="iphone6/7/8 plus test results for "/>
    </p>
</details>

<details>
    <summary><b>__samsung galaxy s5__</b></summary>
    Device width: 360px
    <p float="left">
        <img src="" width="300" height="200" alt="Galaxy S5 test results for "/>
        <img src="" width="300" height="200" alt="Galaxy S5 test results for "/>
        <img src="" width="300" height="200" alt="Galaxy S5 test results for "/>
        <img src="" width="300" height="200" alt="Galaxy S5 test results for "/>
        <img src="" width="300" height="200" alt="Galaxy S5 test results for "/>
        <img src="" width="300" height="200" alt="Galaxy S5 test results for "/>
    </p>
</details>

<details>
    <summary><b>__Moto G4__</b></summary>
    Device width: 360px
    <p float="left">
        <img src="" width="300" height="200" alt="Moto G4 test results for"/>
        <img src="" width="300" height="200" alt="Moto G4 test results for"/>
        <img src="" width="300" height="200" alt="Moto G4 test results for"/>
        <img src="" width="300" height="200" alt="Moto G4 test results for"/>
        <img src="" width="300" height="200" alt="Moto G4 test results for"/>
    </p>
</details>

<details>
    <summary><b>__iPad__</b></summary>
    Device width: 1024px
    <p float="left">
        <img src="" width="300" height="200" alt="iPad test results for"/>
        <img src="" width="300" height="200" alt="iPad test results for"/>
        <img src="" width="300" height="200" alt="iPad test results for"/>
        <img src="" width="300" height="200" alt="iPad test results for"/>
        <img src="" width="300" height="200" alt="iPad test results for"/>
    </p>
</details>

<details>
    <summary><b>__Desktop Chrome__</b></summary>
    <p float="left">
        <img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
		<img src="" width="300" height="200" alt="Desktop Chrome test results for the "/>
    </p>
</details>

<details>
    <summary><b>__Desktop Firefox__</b></summary>
    <p float="left">
        <img src="" width="300" height="200" alt="Desktop Firefox test results for "/>
        <img src="" width="300" height="200" alt="Desktop Firefox test results for "/>
        <img src="" width="300" height="200" alt="Desktop Firefox test results for "/>
        <img src="" width="300" height="200" alt="Desktop Firefox test results for "/>
    </p>
</details>

<details>
    <summary><b>__Desktop Edge__</b></summary>
    <p float="left">
        <img src="" width="300" height="200" alt="Desktop Edge test results for the "/>
        <img src="" width="300" height="200" alt="Desktop Edge test results for the "/>
        <img src="" width="300" height="200" alt="Desktop Edge test results for the "/>
        <img src="" width="300" height="200" alt="Desktop Edge test results for the "/>
    </p>
</details>

#### HTML Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="" width="300" height="200" alt="HTML Validation Results for "/>
        <img src="" width="300" height="200" alt="HTML Validation Results for "/>
		<img src="" width="300" height="200" alt="HTML Validation Results for "/>
    </p>
</details>

#### CSS Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="" width="300" height="200" alt="CSS Validation Results for "/>
        <img src="" width="300" height="200" alt="CSS Validation Results for "/>
		<img src="" width="300" height="200" alt="CSS Validation Results for "/>
    </p>
</details>

#### JavaScript Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="" width="300" height="200" alt="JS Validation Results for "/>
        <img src="" width="300" height="200" alt="JS Validation Results for "/>
		<img src="" width="300" height="200" alt="JS Validation Results for "/>
    </p>
</details>

#### Python Code Validation Post Deployment
<details>
    <summary>Expand for test results</summary>
    <p float="left">
        <img src="" width="300" height="200" alt="Python Validation Results for "/>
        <img src="" width="300" height="200" alt="Python Validation Results for "/>
		<img src="" width="300" height="200" alt="Python Validation Results for "/>
    </p>
</details>

## Final User Acceptance Testing:

Due to the size and timelines of this project, there will not be a structured Alpha/Beta stage of UAT outside of the sprints. Instead, a selection of volunteers will conduct a time boxed exploratory sessions within each sprint once Minimum Viability has been achieved. After which feedback will be collated and transformed into defects, improvements or new features.

This feedback has been included above within the applicable sprint and incorporated into the project where appropriate.

Once the final code was deployed via Heroku, the original testers completed a final round of User Acceptance Testing (Beta).


## Performance Testing:
The following evidence are the results from the performance speed test conducted on the deployed site:
<p float="left">
<img src="" width="300" height="200" alt="Performance Results of the home page"/>
</p>


### Issues located


### Warnings located


## Final WAVE Accessibility Assessment

The following are the results from the final WAVE tests

*

## Production Shakedown Pre Submission

# Unfixed bugs/ Improvements to current features
