const socket = new WebSocket('ws://localhost:5000')
let usermessage = '';
let splitdata = [];
let n = 0
let Contacts = [];
let chatType = ""
const commands = [0,userAuth,2,3,4,5,6,7,8,9,10,11,UpdateContacts,ChatUpdate,UpdateContacts,UpdateContacts]
function excecutecommand(command, info) {
  
  if (command == "1") {
    userAuth(info);
}
if(command == "2")
if(command == "12" || command == "14" || command == "15"){
  UpdateContacts(info);
}
if(command == "13"){
  ChatUpdate(info);
}
}

function userAuth(info) {
  document.getElementById("IdDisplay").innerHTML = info; 
  if (info != ''){document.getElementById("InputId").style.display = "none"
    document.getElementById("InputId").style.height = 0;
} else {
  document.getElementById("IdDisplay").style.display = "none"
    document.getElementById("IdDisplay").style.height = 0;
}
}

function UpdateContacts(info){
  Contacts = info.split(" ")
  console.log(Contacts)
  scroll(false,false)
} 
function scroll(left,right) {
  if (left == true){
    right = false;
    n = n-1;  
  }
  if (right == true){
    left = false;
    n = n+1;  
  }
  console.log(n)
  document.querySelectorAll(`#Scroller > :nth-child(n)`).forEach((element, index) => {
    element.innerHTML = Contacts[n + index];
  });
}
socket.onopen = () => { 
    console.log('WebSocket connected');
    readid()
    genkey()
    GetContacts()

};
socket.addEventListener("message", (event) => {
  i = event.data.indexOf(' '); 
  splitdata = [event.data.slice(0,i), event.data.slice(i+1)];
  console.log(splitdata); 
  excecutecommand(splitdata['0'], splitdata['1'])
});

function getip(){
  usermessage = '0'
  socket.send(usermessage, String);
}

function readid(){
  usermessage = "1"
  socket.send(usermessage, String);
  }

  
  function saveContact(){
    usermessage = document.getElementById("search").value;
    usermessage = "16 " + usermessage + " Contacts";   
    socket.send(usermessage, String)
  }

  function savebyKey(){
    usermessage = document.getElementById("pearch").value + " " + document.getElementById("pearchey").value;
    usermessage = "19 " + usermessage;   
    socket.send(usermessage, String)
  }

  function saveGC(){
    usermessage = document.getElementById("search").value;
    usermessage = "16 " + usermessage + " GroupChat";   
    socket.send(usermessage, String)
  }

  function initPrivChat(){
    usermessage = document.getElementById("search").value;
    usermessage = "16 " + usermessage + " privateChats";  
    socket.send(usermessage, String)
  }
  
  function sendkey(){
    usermessage = document.getElementById("search").value;
    usermessage = "6 " + usermessage;  
    socket.send(usermessage, String)
  }

  function sendmsg(){
    usermessage = document.getElementById("messageElement").value+ " "+ document.getElementById("publicHead").innerHTML;
    usermessage = "8 " + Contacts.indexOf(document.getElementById("publicHead").innerHTML) + usermessage;   
    socket.send(usermessage, String)
  }

  function sendmsg(){
    usermessage = document.getElementById("messageElement").value+ " "+ document.getElementById("publicHead").innerHTML;
    usermessage = "4 " + usermessage;   
    socket.send(usermessage, String)
  }
    

var elements = document.querySelectorAll("#contactButton");

elements.forEach(element => {
  element.addEventListener("click", () => {
    socket.send("13 " + chatType + " " + element.innerHTML);
    HeadUpdate(element.innerHTML)
  });
});

function ChatUpdate(info){  
  console.log(info);
 document.getElementById("public").innerHTML = String(info);
 
 }
 function HeadUpdate(info){  
   console.log(info);
  document.getElementById("publicHead").innerHTML = String(info);
  }

document.getElementById("writeId").onclick = function(){
usermessage = document.getElementById("userID").value;
usermessage = "2 " + usermessage 
socket.send(usermessage, String)
getip();
genkey();
};

socket.onerror = (error) => {
  console.error('WebSocket error:', error);
}; 


//IGNORE BELOW
//const fs = require("fs");
//fs.readFile(file.txt," "))
//                      ^any encoding
//console.log(event.data, event.origin)
//onmessage = (event) => {
//let hickorydock = event.data
//console.log(event.data, event.source);
//splitdata = hickorydock.split(" "); 
//console.log(splitdata);
//document.getElementById("ServerDisplay").innerHTML = event.source;
//};
//addEventListener("message", (Re) => {
//  console.log(message)
//});
//socket.onmessage(message) = () =>
//document.getElementById("SendMessage").addEventListener("click", fs.writeFileSync(parcel.txt, usermessage, "utf-8"));
///{}
function genkey(){
  socket.send("3")
}
function GetContacts(){
  socket.send("12")
  chatType = "Conv"
} 
function GetGroupContacts(){
  socket.send("14")
  chatType = "GC"
} 
function GetPrivContacts(){
  socket.send("15")
  chatType = "Priv"

} 


document.getElementById("Conversation").addEventListener("click", function () {GetContacts()});
document.getElementById("Priv").addEventListener("click", function () {GetPrivContacts()});
document.getElementById("GroupChats").addEventListener("click", function () {GetGroupContacts()});
document.getElementById("ScrollRight").addEventListener("click", function () {scroll(false,true)});
document.getElementById("ScrollLeft").addEventListener("click", function () {scroll(true,false)});
document.getElementById("sendmsg").addEventListener("click", function () {sendmsg()});
document.getElementById("addButton").addEventListener("click", function () {saveContact()});
document.getElementById("sendButton").addEventListener("click", function () {sendkey()});
document.getElementById("privButton").addEventListener("click", function () {initPrivChat()});
document.getElementById("keyprivButton").addEventListener("click", function () {savebyKey()});