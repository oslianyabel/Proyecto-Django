const btnToggleDarkMode = document.querySelector('.btn-toggle-dark-mode');
const body = document.body;
const btnLogout = document.querySelector('.btn-logout');
const taskForm = document.getElementById('taskForm');
const taskList = document.getElementById('taskList');
const taskList_public = document.getElementById('taskList-public');
const filterSelect = document.getElementById('filterSelect');
const filterSelect_public = document.getElementById('filterSelect-public');
const sortByDueDateBtn = document.getElementById('sortByDueDateBtn');
const sortByDueDateBtn_public = document.getElementById('sortByDueDateBtn-public');
const sortByPriorityBtn = document.getElementById('sortByPriorityBtn');
const sortByPriorityBtn_public = document.getElementById('sortByPriorityBtn-public');
let btn_cambiante = document.getElementById('btn_cambiante');
let titulo = document.getElementById('titleInput');
let descripcion = document.getElementById('descriptionInput');
let titulo_menu = document.getElementById('titulo_menu');
let cont = 0;
let select = -1;
let form;