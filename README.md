<h1 align="center">FamilyGuide AI</h1>

<br>

<details>

<summary>Backend Docs</summary>

<br>

<h1 align="center">FamilyGuide AI Backend</h1>

<br>

## About

<br>

FamilyGuide AI is an AI-powered application that offers expert advice on parenting, child development, and family dynamics. Our mission is to support caregivers with personalized insights and promote positive parenting techniques to foster healthy family relationships. FamilyGuide AI is available in both Hindi and English languages, providing comprehensive guidance for all caregivers.

<br>

## Features

- User Authenication such as sign up and sign in 
- Role Based access control
- Ask any questions regarding parenting purposes like Chat-GPT.
- Error Handling.

<br>

## Technologies Used

- Python
- Flask
- MongoDB

## Clone Repository

<br>

```
git clone https://github.com/Amanmandal-M/Parenting_Influencer_GPT.git
```

<br>

### Prerequisites

- Python 3.11.4
- Flask 2.0.1
- Pymongo 4.4.1

<br>

## Installation

<br>

```
cd Backend

pip install -r requirements.txt
```

<br>

## Start the Backend server

<br>

```
python app.py
```

<br>

##  MVC Structure

```js
├── app.py
├── configs
|    └── db.py
├── models
|    └── all_model.py
├── routes
|    └── user_route.py
├──controllers
|    └── user_controller.py
|    └── responses_controller.py
├──templates
|    └──404.html
|    └──405.html
```

Note : 

-  Before doing anything first create `.env` file and put `PORT` , `MONGO_URI` , `NORMAL_KEY` ,  OPENAI_API_KEY.
- `PORT` is for listening the server.
- `MONGO_URL` is for running database and store your data in database so put your mongo link.
- `NORMAL_KEY` is for authentication jsonwebtoken so basically this is your secret key .

<br>

## Endpoints

<table>
    <thead>
        <tr>
            <th>Blueprint</th>
            <th>Method</th>
            <th>Endpoint</th>
            <th>Description</th>
            <th>Status Code</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>user</td>
            <td>POST</td>
            <td>/user/register</td>
            <td>This endpoint should allow users to register. Hash the password on store.</td>
            <td>201</td>
        </tr>
        <tr>
            <td>user</td>
            <td>POST</td>
            <td>/user/login</td>
            <td>This endpoint should allow users to login. Return JWT token on login.</td>
            <td>201</td>
        </tr>
        <tr>
            <td>response</td>
            <td>POST</td>
            <td>/prompt</td>
            <td>This endpoint is for send question to AI and they give responses.</td>
            <td>200</td>
        </tr>
        <tr>
            <td>response</td>
            <td>GET</td>
            <td>/prompt-data</td>
            <td>This endpoint is for view all the responses of current user who logged in currently.</td>
            <td>200</td>
        </tr>
    </tbody>
</table>


<br>

## Backend Deployment URL

<h3>
    <strong>
        <a href="https://parenting-influencer-backend.onrender.com">Render</a>
    </strong>
</h3>

<br>

## ER Diagram and Process

<h3>
    <strong>
        <a href="https://url-shortener-857u.onrender.com/eWkpEFaKB">Notion Docs</a>
    </strong>
</h3>

</details>

<br>

<details>

<summary>Frontend Docs</summary>

<br>

<h1 align="center">FamilyGuide AI Frontend</h1>

<br>

## About

FamilyGuide AI is an AI-powered application that offers expert advice on parenting, child development, and family dynamics. Our mission is to support caregivers with personalized insights and promote positive parenting techniques to foster healthy family relationships. FamilyGuide AI is available in both Hindi and English languages, providing comprehensive guidance for all caregivers.

<br>

## Technologies Used

- Angular
- SCSS
- TypeScript
- SweetAlert

## Clone Repository


```
git clone https://github.com/Amanmandal-M/Parenting_Influencer_GPT.git
```

<br>

### Prerequisites

- HTML
- CSS
- JavaScript

<br>

## Start the Frontend


```js
 - cd Frontend/influencer-app
 - npm install
 - ng serve
```

## Frontend Deployment URL

<h3>
    <strong>
        <a href="https://parenting-influencer-app.vercel.app">Vercel</a>
    </strong>
</h3>

</details>



