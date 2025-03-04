# Client-Side JavaScript README

---

## Overview
This document provides guidance on the client-side JavaScript implementation for the assignment. The client-side code consists of HTML/CSS/javascript, and  is served when a user navigates to the index or root of our server (/). The web server returns the frontend application via server side rendered template. 

The frontend code has two responsibilities besides the styling of the applicaiton. They are handling login process with Google's Identity Platform and sending data to the backend when a user submits votes. The main JavaScript file handling this logic is `static/firebase.js`, and the firebase config is stored in `static/config.js`.


### **__Your jobs is to implement the following:__**

1. Update the client-side JavaScript function in the [firestore.js](../cc_cloud_run/static/firestore.js) file
    - Implement the `vote` function that sends a POST request to the FastAPI backend.
    - The request should be ContentType `application/x-www-form-urlencoded` with the `team` (either "TABS" or "SPACES") as form data.
    - The request should pass an Authorization header with the value `Bearer <ID_TOKEN>` where `<ID_TOKEN>` is the user's ID token.
    - Handle the response by displaying a success message or an error message in case of failure.
2. Update the [config.js](../cc_cloud_run/static/config.js) file with your Firebase configuration.
```typescript
const config = {
  apiKey: 'AIzaSyDhwsk8Ak...',
  authDomain: '[PROJECT].firebaseapp.com',
};
```
3. Configure the Event Listeners for the Sign-In and Vote Buttons in `index.html`.

---

## Client-Side JavaScript

The frontend includes a JavaScript file `static/firestore.js` the handles UI interactions with Firebase Authentication and sends user votes to the FastAPI backend.

You should update the `vote` function, such that it makes a POST request to the backend API. 

### `static/firestore.js` Vote Function:

- POST request
- Uses the following headers:
  - `Content-Type: application/x-www-form-urlencoded`
  - `Authorization: Bearer ${token}`
- Handles the response and displays success or error messages.
- [docs](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)

### `static/config.js`
You should update the `static/config.js` file with Firebase configuration:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_API_KEY",
    authDomain: "YOUR_AUTH_DOMAIN",
};

export default firebaseConfig;
```

--- 

## HTML Event Listeners

The application includes a [HTML template](../template/index.html) that is
served by the web server. This HTML ultimately draws the skeleton of our
Document Object Model (DOM), and we need to add [event
listeners](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) on the
login/logout and vote buttons.

You should find the elements in the DOM by ID using the `document` API, and
attach an `onclick` event listener to trigger you action. The actions will be
a calling the `vote` (on the TABS/SPACES button) or `toggle` (signin / signout)
functions. The `toggle` function is already implemented.

```javascript
document.getElementById("someID").addEventListener("click", function () {
  someFunction("TABS");
});
```

