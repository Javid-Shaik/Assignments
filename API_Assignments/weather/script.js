
const apiKey = '64fa318339616fe22c15b4e188882312';

// Select HTML elements
const dataElement = document.getElementsByClassName('weather-dat');
const locationInput = document.getElementById('locationInput');
const locationButton = document.getElementById('locationButton');
const locationElement = document.getElementById('location');
const temperatureElement = document.getElementById('temperature');
const descriptionElement = document.getElementById('description');
const iconElement = document.getElementById('icon');
const clearButton = document.getElementById('clearButton');

let lastEnteredCity = '';

// Function to fetch weather data
function fetchWeatherData(city) {
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

  fetch(apiUrl)
    .then((response) => response.json())
    .then((data) => {
      const { name, main, weather } = data;
      locationElement.textContent = name;
      temperatureElement.textContent = `${Math.round(main.temp - 273.15)}°C`; // Convert from Kelvin to Celsius
      descriptionElement.textContent = weather[0].description;
      iconElement.innerHTML = `<img src="http://openweathermap.org/img/w/${weather[0].icon}.png" alt="${weather[0].description}">`;

    })
    .catch(descriptionElement.textContent = "Sorry Data Not Found!",  // if the entered city is not valid then show that no data is available.
    locationElement.textContent = '',                               // and clear all the fileds
    temperatureElement.textContent = '',
    iconElement.innerHTML = '',
     (error) => console.error('Error fetching data:', error));
     lastEnteredCity = city; // irrespective of the validity of the city name store the last enteredd city.
} 

// Event listener for the button click
locationButton.addEventListener('click', () => {
  const city = locationInput.value;
  if (city !== lastEnteredCity && city ) {  // if the city entered is not same as the last city then only call the function
    fetchWeatherData(city);
  } else if(city===lastEnteredCity) {  //if the city in the input field is already on the screen then no need to call the fetch function
    console.log("Enter new city");
  } else {
    alert('Please enter a city name.');  // if the user doesn't entered any city then ask him to enter a city name
  }
});

// event listener for clearing the value in the input filed
clearButton.addEventListener('click' , () => {
    locationInput.value = ''
})
