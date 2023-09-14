const image = document.querySelector("img");
const breed = document.querySelector("#breed");


fetch("https://dog.ceo/api/breeds/image/random")
  .then(res => res.json()) // parse response as JSON
  .then(data => {
    console.log(data);

    image.src = data.message;


  })
  .catch(err => {
    console.log(`error ${err}`)
  });

