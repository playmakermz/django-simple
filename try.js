document.getElementById('form-buku-view').addEventListener('submit',function(e){
let title = document.getElementById('title-view').value;
let description = document.getElementById('description-view').value;
let author = document.getElementById('author-view').value;
let year = document.getElementById('year-view').value;
let isComplete = true;
let id = document.getElementById('id-view').value;
KEY = 'playground'
const task ={
title,
description,
author,
year,
isComplete,
id,
}

if (localStorage.getItem(KEY) == null){
let tasks = [];
tasks.push(task);
localStorage.setItem(KEY, JSON.stringify(KEY))

}// akhir if 

else {
let tasks = JSON.parse(localStorage.getItem(KEY));
tasks.push(task);
localStorage.setItem(KEY, JSON.stringify(tasks));
} // akhir else 

document.getElementById('form-buku-view').reset();

e.preventDefault();
deleteTask(title)
location.reload();
});// akhir function 
