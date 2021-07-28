document.getElementById("form-task").addEventListener('submit',function(e){

let title = document.getElementById('title').value;
let description =  document.getElementById('description').value;
let author = document.getElementById('author').value;
let year = document.getElementById('year').value;
let isComplete = document.getElementById('isComplete').checked; // ?  true : false 
let id = Date.now()
let KEY_STORAGE = 'tasks'

// ------------------------------ if statement untuk true ------------------
if (isComplete) {
  
  KEY_STORAGE = 'playground'

const task ={
        title,
        description,
        author,
        year,
        isComplete,
        id,
}// end array object


if(localStorage.getItem('playground') == null){
let tasks = [];
tasks.push(task);
localStorage.setItem('playground',JSON.stringify(tasks));
} // akhir if 
    
else{
let tasks = JSON.parse(localStorage.getItem('playground'));
tasks.push(task);
localStorage.setItem('playground',JSON.stringify(tasks));
} // akhir else 
getEmpty();
document.getElementById("form-task").reset();
e.preventDefault(); 

}// -------------------- akhir if Iscomplete  ----------------------
else {

const task ={
        title,
        description,
        author,
        year,
        isComplete,
        id,
}

if(localStorage.getItem('tasks') == null){
let tasks = [];
tasks.push(task);
localStorage.setItem('tasks',JSON.stringify(tasks));
}// end 

// else statement 
else{
let tasks = JSON.parse(localStorage.getItem('tasks'));
tasks.push(task);
localStorage.setItem('tasks',JSON.stringify(tasks));
} // akhir else
getTasks();
document.getElementById("form-task").reset();
e.preventDefault(); 

} // -------------------- Akhir Else statement untuk false -------- 
});// ---------- akhir function e -------------------------

// =============================
// getTask function 
//

function getTasks(){
    let KEY_STORAGE = 'tasks'
    let tasks =  JSON.parse(localStorage.getItem('tasks'));
    let tasksView = document.getElementById('task-view');

//
// Declare Variable
//    
    tasksView.innerHTML= '';
    for (let index = 0; index < tasks.length; index++) {
        let title = tasks[index].title;
        let description = tasks[index].description;
        let author = tasks[index].author;
        let year = tasks[index].year;
        let isComplete = tasks[index].isComplete;
        let id = tasks[index].id;

        tasksView.innerHTML += ` 
<div class="page-box-02"> <!--ini untuk area buku yang sudah terbaca -->
<div class="page-box-02-item">
  <form id='form-buku-view'> 
  <h4> ${title} </h4>
  id
  <input type='text' value='${id}' id='id-view'></input> 
  <br> judul
  <input type='text' value='${title}' id='title-view'></input>
 <br> Penulis 
  <input type='text' value='${author}' id='author-view'></input>
 <br> terbit 
  <input type='number' value='${year}' id='year-view'></input>
 <br> Deskripsi 
  <input type='text' value='${description}' id='description-view'></input> 
   <br><br>
   <label style='color:red;'> click 2 kali :</label>
  <button class='' onclick='deleteTask('${title}')'>sudah dibaca</button>
  </form>
  <button onclick="deleteTask('${title}')"> Hapus data </button>
</div>
</div>
        `;
    }
}


function getEmpty(){
    let playground = JSON.parse(localStorage.getItem('playground'));
    let tasksEmpty = document.getElementById('task-empty');



  tasksEmpty.innerHTML= '';
  for (let index = 0; index < playground.length; index++) {
        let title = playground[index].title;
        let description = playground[index].description;
        let author = playground[index].author;
        let year = playground[index].year;
        let isComplete = playground[index].isComplete;
        let id = playground[index].id;

        tasksEmpty.innerHTML += ` 
<div class="page-box-02"> <!--ini untuk area buku yang sudah terbaca -->
<div class="page-box-02-item">
  <form id='form-buku-empty'> 
  <h4> ${title} </h4>
  id
  <input type='text' value='${id}' id='id-empty'></input> 
  <br> judul
  <input type='text' value='${title}' id='title-empty'></input>
 <br> Penulis 
  <input type='text' value='${author}' id='author-empty'></input>
 <br> terbit 
  <input type='number' value='${year}' id='year-empty'></input>
 <br> Deskripsi 
  <input type='text' value='${description}' id='description-empty'></input> 
   <br><br>
   <label style='color:red;'> click 2 kali :</label>
  <button class='' onclick='deleteEmpty('${title}')'>Belum dibaca</button>
  </form>
  <button onclick="deleteEmpty('${title}')"> Hapus data </button>
</div>
</div>
`;
    }
} 


function deleteTask(title){
    let KEY_STORAGE = 'tasks'
    let tasks = JSON.parse(localStorage.getItem(String(KEY_STORAGE)));
    for (let index = 0; index < tasks.length; index++) {
        if (tasks[index].title == title) {
            tasks.splice(index,1);   
        }
    }
    localStorage.setItem(String(KEY_STORAGE),JSON.stringify(tasks));
    getTasks();
    location.reload();
}

function deleteEmpty(title){

    let KEY_PLAYGROUND = 'playground'
    let tasks = JSON.parse(localStorage.getItem(String(KEY_PLAYGROUND)));
    for (let index = 0; index < tasks.length; index++) {
        if (tasks[index].title == title) {
            tasks.splice(index,1);   
        }
    }
    localStorage.setItem(String(KEY_PLAYGROUND),JSON.stringify(tasks));

    location.reload();
    getEmpty();


}

getTasks();

getEmpty();
