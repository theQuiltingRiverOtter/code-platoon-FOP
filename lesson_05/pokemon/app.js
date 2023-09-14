document.querySelector('button').addEventListener('click', getFetch)
const pokemonName = document.querySelector("#name");
const pokemonImage = document.querySelector("#image");
const pokemonType = document.querySelector("#type");


async function getFetch() {
    const choice = document.querySelector('input').value.toLowerCase();
    const shiny = document.querySelector("#shiny")
    const url = 'https://pokeapi.co/api/v2/pokemon/' + choice
    let data = await fetch(url)
    let pokemonInfo = await data.json()
    const name = pokemonInfo.name;
    const sprites = pokemonInfo.sprites
    const image = (shiny.checked) ? sprites.front_shiny : sprites.front_default;
    const type = pokemonInfo.types[0].type.name
    pokemonName.innerHTML = capitalize(name);
    pokemonImage.src = image;
    pokemonImage.style.width = "150px";
    pokemonImage.style.height = "150px";
    pokemonType.innerHTML = capitalize(type);
}


function capitalize(name) {
    return name[0].toUpperCase() + name.slice(1, name.length);
}