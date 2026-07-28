import { courses } from "./data.js";

// =====================================================
// HTML Elements
// =====================================================

const courseGrid = document.querySelector(".course-grid");

const loadingMessage = document.getElementById("loadingMessage");

const loadButton = document.getElementById("loadCourses");

// =====================================================
// Task 45
// Fetch using Promise (.then())
// =====================================================

function fetchUser(id){

fetch("https://jsonplaceholder.typicode.com/users/" + id)

.then(response=>response.json())

.then(data=>{

console.log("User Name :",data.name);

})

.catch(error=>{

console.log(error);

});

}

fetchUser(1);

// =====================================================
// Task 46
// Async Await
// =====================================================

async function fetchUserAsync(id){

try{

const response=await fetch(

"https://jsonplaceholder.typicode.com/users/"+id

);

const data=await response.json();

console.log("Async User :",data.name);

}

catch(error){

console.log(error);

}

}

fetchUserAsync(2);

// =====================================================
// Render Course Cards
// =====================================================

function renderCourses(courseArray){

courseGrid.innerHTML="";

courseArray.forEach(course=>{

const article=document.createElement("article");

article.className="course-card";

article.innerHTML=`

<h3>${course.name}</h3>

<p><strong>Code :</strong> ${course.code}</p>

<p>${course.description}</p>

<p><strong>Credits :</strong> ${course.credits}</p>

`;

courseGrid.appendChild(article);

});

}

// =====================================================
// Task 47
// Simulate API Delay
// =====================================================

function fetchAllCourses(){

return new Promise(resolve=>{

setTimeout(()=>{

resolve(courses);

},1000);

});

}

// =====================================================
// Task 48
// Loading State
// =====================================================

async function loadCourses(){

loadingMessage.style.display="block";

const result=await fetchAllCourses();

loadingMessage.style.display="none";

renderCourses(result);

}

loadButton.addEventListener(

"click",

loadCourses

);

// =====================================================
// Task 49
// Promise.all()
// =====================================================

Promise.all([

fetch("https://jsonplaceholder.typicode.com/users/1")

.then(response=>response.json()),

fetch("https://jsonplaceholder.typicode.com/users/2")

.then(response=>response.json())

])

.then(users=>{

console.log(

"Promise.all",

users[0].name,

users[1].name

);

});

// =====================================================
// Task 50
// Reusable Fetch Function
// =====================================================

const spinner = document.getElementById("spinner");
const notificationList = document.getElementById("notificationList");
const errorBox = document.getElementById("errorBox");
const retryButton = document.getElementById("retryButton");

async function apiFetch(url){

    const response = await fetch(url);

    if(!response.ok){

        throw new Error("Unable to load data. Please try again.");

    }

    return await response.json();

}

// =====================================================
// Task 51
// Load Notifications
// =====================================================

async function loadNotifications(){

    spinner.style.display="block";

    notificationList.innerHTML="";

    errorBox.innerHTML="";

    retryButton.style.display="none";

    try{

        const posts = await apiFetch(
            "https://jsonplaceholder.typicode.com/posts?_limit=6"
        );

        spinner.style.display="none";

        posts.forEach(post=>{

            const card=document.createElement("div");

            card.className="notification-card";

            card.innerHTML=`

                <h3>${post.title}</h3>

                <p>${post.body}</p>

            `;

            notificationList.appendChild(card);

        });

    }

    catch(error){

        spinner.style.display="none";

        errorBox.innerHTML=error.message;

        retryButton.style.display="inline-block";

    }

}

loadNotifications();

// =====================================================
// Task 52
// Loading Spinner
// =====================================================

// Spinner automatically appears before loading
// and disappears after loading.

// =====================================================
// Task 53
// Simulate 404 Error
// =====================================================

async function loadBadAPI(){

    spinner.style.display="block";

    errorBox.innerHTML="";

    retryButton.style.display="none";

    try{

        await apiFetch(
            "https://jsonplaceholder.typicode.com/nonexistent"
        );

    }

    catch(error){

        spinner.style.display="none";

        errorBox.innerHTML="404 Error : Unable to fetch notifications.";

        retryButton.style.display="inline-block";

    }

}

// Uncomment to test

// loadBadAPI();


// =====================================================
// Task 54
// Retry Button
// =====================================================

retryButton.addEventListener("click",()=>{

    loadNotifications();

});

// =====================================================
// Task 55
// Axios CDN already added in index.html
// =====================================================


// =====================================================
// Task 56
// Axios API Function
// =====================================================

async function axiosFetch(url){

    const response = await axios.get(url);

    return response.data;

}

// =====================================================
// Task 57
// Axios Params
// =====================================================

async function loadUserPosts(){

    const posts = await axios.get(

        "https://jsonplaceholder.typicode.com/posts",

        {

            params:{

                userId:1

            }

        }

    );

    console.log("Posts of User 1");

    console.log(posts.data);

}

loadUserPosts();

// =====================================================
// Task 58
// Axios Request Interceptor
// =====================================================

axios.interceptors.request.use(config=>{

    console.log("API Call Started :",config.url);

    return config;

});

// =====================================================
// Task 59
// Fetch vs Axios
// =====================================================

/*

Difference 1

Fetch

Needs response.json()

Axios

Automatically parses JSON

---------------------------------

Difference 2

Fetch

Does not throw errors for
HTTP 404 / 500

Axios

Automatically throws errors

---------------------------------

Difference 3

Fetch

Built into browser

Axios

External library with
Interceptors,
Timeout,
Automatic JSON parsing,
Better defaults.

*/
