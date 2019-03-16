var col = document.getElementsById("collapsible");
var butt = document.getElementsByClassName("button");


butt.onclick = myFunction(){
    if(col.style.display === none){
        col.style.display = flex;
    }
    else{
        col.style.display = none;
    }
}