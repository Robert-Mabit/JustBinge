var accordions = document.getElementsByClassName("accordion");

for (var i = 0; i < accordions.length; i++) {
    accordions[i].onclick = function () {
        document.getElementById("myHeader").classList.toggle('is-open');
        document.getElementById("mySmenu").classList.toggle("is-open");

        var content = this.previousElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
            document.getElementByClassName("accordion").style.background = rgb(35, 35, 35);
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
            document.getElementByClassName("accordion").style.background = rgba(255, 255, 255, 0.065);
        }
    }
}