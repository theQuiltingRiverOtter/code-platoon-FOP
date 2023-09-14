const button = document.querySelector("button");
const title = document.querySelector("h2");
const image = document.querySelector("img");
const instructions = document.querySelector("h3");
const ul = document.querySelector("ul");
const input = document.querySelector("input");

button.addEventListener('click', getInfo)


function getInfo() {
  const drinkName = document.querySelector("input").value;
  //const url = `https://www.thecocktaildb.com/api/json/v1/1/search.php?s=${drinkName}`
  const url = 'www.thecocktaildb.com/api/json/v1/1/random.php'
  fetch(url)
    .then(res => res.json()) // parse response as JSON
    .then(data => {
      console.log(data);
      //   input.value = '';
      //   const allLI = document.querySelectorAll("li");
      //   for (let item of allLI) {
      //     if (item.parentNode) {
      //       item.parentNode.removeChild(item);
      //     }
      //   }
      //   const drink = data.drinks[0];
      //   const ingredients = getIngredients(drink);
      //   title.innerText = drink.strDrink;
      //   image.src = drink.strDrinkThumb;
      //   image.style.width = '300px';
      //   image.style.height = "300px";
      //   instructions.innerText = drink.strInstructions;
      //   for (let ingredient of ingredients) {
      //     const li = document.createElement("li");
      //     li.innerText = ingredient;
      //     ul.append(li);
      //   }
    })
    .catch(err => {
      console.log(`Something went wrong here ${err}`)
    });

}


function getIngredients(drinkObj) {
  const ingredients = []
  for (let item in drinkObj) {
    if (item.includes('strIngredient')) {
      if (drinkObj[item] !== null) {
        ingredients.push(drinkObj[item])
      }
    }
  }
  return ingredients
}