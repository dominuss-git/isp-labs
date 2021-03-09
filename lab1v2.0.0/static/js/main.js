let element = document.getElementsByClassName("wrapper__todo");

for (let el of element) {
    el.children[2].addEventListener("change", () => change(el))
} 

const change = (el) => {
    if (el.children[2].checked) { 
        el.classList.add("wrapper__todo-active");
    }
    else {
        el.classList.remove("wrapper__todo-active");
    }
}
