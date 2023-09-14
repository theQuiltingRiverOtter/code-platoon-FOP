const botScore = document.querySelector("#botScore");
const addOne = document.querySelector("#addOne");
const subOne = document.querySelector("#subOne");
const reset = document.querySelector("#reset");

addOne.addEventListener('click', addCount)
subOne.addEventListener("click", subCount)
reset.addEventListener("click", resetCount)


localStorage.setItem('count', 1)



const getStr = localStorage.getItem('count')
console.log(getStr);
botScore.innerHTML = getStr;



function addCount() {
    const getCount = Number(localStorage.getItem("count"));
    localStorage.setItem('count', getCount + 1)
    botScore.innerHTML = getCount + 1
}

function subCount() {
    const getCount = Number(localStorage.getItem("count"));
    localStorage.setItem('count', getCount - 1)
    botScore.innerHTML = getCount - 1
}

function resetCount() {
    const getCount = Number(localStorage.getItem("count"));
    localStorage.setItem('count', 1)
    botScore.innerHTML = 1
}