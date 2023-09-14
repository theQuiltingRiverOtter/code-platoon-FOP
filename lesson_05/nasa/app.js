const todayBtn = document.querySelector("#todayBtn");
const otherBtn = document.querySelector("#otherBtn");
const submitBtn = document.querySelector("#submitBtn");
const allPics = document.querySelector("#allPics");
const form = document.querySelector("#getForm");
const image = document.querySelector("#nasaImg");
const loading = document.querySelector("#loading");
const images = document.querySelector("#images")
todayBtn.addEventListener('click', getToday);
otherBtn.addEventListener('click', showForm);
submitBtn.addEventListener('click', getOtherDay);
allPics.addEventListener("click", getAllPics);



baseURL = 'https://api.nasa.gov/planetary/apod?';
apiKey = 'api_key=GMQInfiIXgwjqHxYTM77CZJQwB0NRfcEAeyCNDy3';

function getAllPics() {

    const items = { ...localStorage }
    for (let item in items) {
        const newImage = document.createElement("img");
        newImage.src = items[item];
        newImage.alt = item;
        images.appendChild(newImage)
    }

}

function showForm() {
    image.src = ''
    image.style.display = 'none';
    form.style.display = "block";
}

async function getToday() {
    form.style.display = "none";
    loading.style.display = 'block';
    image.src = ''
    const res = await fetch(`${baseURL}${apiKey}`)
    const jsonRes = await res.json();
    const imageURL = jsonRes.url;
    localStorage.setItem(`today`, imageURL);
    image.src = imageURL;
    image.style.display = 'block'
    loading.style.display = "none";


}

async function getOtherDay() {
    loading.style.display = 'block'
    const choice = document.querySelector("input").value;
    const res = await fetch(`${baseURL}${apiKey}&date=${choice}`)
    const jsonRes = await res.json();
    const imageURL = jsonRes.url;
    localStorage.setItem(`${choice}`, imageURL);
    loading.style.display = 'none';
    image.style.display = 'block';

}