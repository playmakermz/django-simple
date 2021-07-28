document.getElementById('form-buku-empty').addEventListener('submit',function(e){
let title = document.getElementById('title-empty').value;
let description = document.getElementById('description-empty').value;
let author = document.getElementById('author-empty').value;
let year = document.getElementById('year-empty').value;
let isComplete = false;
let id = document.getElementById('id-empty').value;
KEY = 'tasks'
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

document.getElementById('form-buku-empty').reset();

e.preventDefault();
deleteEmpty(title)
location.reload();
});// akhir function 
//====================
//FUNCTION RENDER EMPTY 
//=====================
// ======================================
// FORM-BUKU-VIEW
// ========================================

//====================
//FUNCTION RENDER EMPTY 
//=====================
