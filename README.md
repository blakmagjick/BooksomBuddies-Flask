# Booksom Buddies 

## Project Description

## Links
Deployed Site: https://booksom-buddies.herokuapp.com/ \
Frontend Repo: https://github.com/blakmagjick/booksombuddies-react \
Backend Repo: https://github.com/blakmagjick/booksombuddies-flask

## Technologies Used
Flask/Python, React/Javascript, SQL, Postgres/pgAdmin, HTML, CSS

## Installation Steps
- Fork and clone the frontend and backend repos. 
- In the terminal, in the directory for the frontend: ```npm install``` in order to install dependencies, then ```npm run start``` to run server.
- In the terminal, in the directory for the backend: ```pip3 install``` to install dependencies, then ```python3 app.py``` to run server.

## User Stories
- As a user, I want to be able to create a profile.
- As a user, I want to be able to add books to a wish list, so that I can easily look at the list while I'm out book shopping.
- As a user, I want to be able to edit my profile, but no one else's.
- As a user, I want to be able to go to the forum and talk to other users about books, so that I can get some ideas of what to read next, and/or talk about what I love/hate about books I've read.
- As a user, I want to be able to easily add books to my profile without manually adding the information myself.
- As a user, I want the app to look pretty and professional.

## Wireframes
![Screen Shot 2021-11-22 at 12 47 30 PM](https://user-images.githubusercontent.com/6404196/146621061-57698632-7b7d-446f-8ba6-24a3204a9754.png)
![Screen Shot 2021-11-22 at 12 47 25 PM](https://user-images.githubusercontent.com/6404196/146621084-8e7ee3e4-83b2-4c36-a4e4-d29916b43294.png)

## Entity Relationship Diagrams
<img width="659" alt="Screen Shot 2021-12-17 at 4 34 49 PM" src="https://user-images.githubusercontent.com/6404196/146622621-bd78018f-284b-4b35-a3d4-73a1b60d6f78.png">

## MVP
[x] Login/Logout functionality \
[x] Forum to chat with other user's about books \
[x] Add books to user's profile via Open Library API \
[x] Stylized

## Stretch Goals
[ ] Book recommendations by genre \
[ ] What I Want to Read Next section \
[ ] Leave notes on books, that only user can see \
[ ] Add books to a Wishlist \
[ ] Optimize viewing for mobile \
[ ] Dark/Light mode

## Suggested Functionality From Test Users
[x] Original Poster can delete any comments on their post \
[ ] Default user pic used when someone doesn't add one \
[ ] Send out an email after registration to confirm it went through \
[ ] Have user messaging - if someone tries to login and they haven't registered before \
[ ] User messaging on the frontend if username or pw is wrong \
[ ] Ability to upload photo from computer


## Bugs/Unsolved Problems
[x] When someone who doesn’t have a profile logs in, the Create New Profile component doesn’t show up until the page is refreshed \
[ ] Each child in a list should have a unique "key" prop warning \
[ ] Move the Create New Profile to top of the page \
[ ] Mixed Content: The page at [...] was loaded over HTTPS, but requested an insecure element 'http://[...]. This request was automatically upgraded to HTTPS, For more information see https://blog.chromium.org/2019/10/no-more-mixed-messages-about-https.html \
[ ] Cookies issue with Safari browser


## Future Features
[ ] Add ISBN to Book Model \
[ ] Amazon Affiliate link \
[ ] Forum shows list of posts by title, and all information comes up when clicked \
[ ] Have single profile pages with more information than just the All Profiles page \
[ ] Add other users to a friend's list \
[ ] When clicking on abook for more info, you can see what other users have that book

