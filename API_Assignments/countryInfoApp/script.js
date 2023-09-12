// Select HTML elements
const countryInput = document.getElementById('country-input');
const autocompleteList = document.getElementById('autocomplete-list');
const countryName = document.getElementById('country-name');
const countryCapital = document.getElementById('country-capital');
const countryPopulation = document.getElementById('country-population');
const countryRegion = document.getElementById('country-region');
const currencyElement = document.getElementById('currency');
const countryFlag = document.getElementById('country-flag');

// Function to fetch countries from an API
function fetchCountries() {
  fetch('https://restcountries.com/v3.1/all') // Replace with your API URL
    .then((response) => response.json())
    .then((data) => {
      countries = data.map((country) => country.name.common);
    })
    .catch((error) => console.error('Error fetching data:', error));
}

// Function to fetch country information
function fetchCountryInfo(countryName) {
  fetch(`https://restcountries.com/v3.1/name/${countryName}`) // Replace with your API URL
    .then((response) => response.json())
    .then((data) => {
      const country = data[0];
      countryName.textContent = country.name.common;
      countryCapital.textContent = `Capital: ${country.capital || '-'}`;
      countryPopulation.textContent = `Population: ${country.population || '-'}`;
      countryRegion.textContent = `Region: ${country.region || '-'}`;
      currencyElement.textContent = `Currency: ${country.currencies ? Object.keys(country.currencies)[0] : '-'}`;
      countryFlag.innerHTML = `<img src="${country.flags.png}" alt="Country Flag">`;
    })
    .catch((error) => console.error('Error fetching data:', error));
}

// Function to display autocomplete options
function displayAutocompleteOptions(filter) {
  const filteredCountries = countries.filter((country) =>
    country.toLowerCase().includes(filter.toLowerCase())
  );

  autocompleteList.innerHTML = '';

  filteredCountries.forEach((country) => {
    const option = document.createElement('div');
    option.textContent = country;
    option.addEventListener('click', () => {
      countryInput.value = country;
      autocompleteList.innerHTML = '';
      fetchCountryInfo(country);
    });
    autocompleteList.appendChild(option);
  });

  if (filteredCountries.length > 0) {
    autocompleteList.style.display = 'block';
  } else {
    autocompleteList.style.display = 'none';
  }
}

// Event listeners
countryInput.addEventListener('input', () => {
  const filter = countryInput.value;
  displayAutocompleteOptions(filter);
});

document.addEventListener('click', (event) => {
  if (!autocompleteList.contains(event.target) && event.target !== countryInput) {
    autocompleteList.style.display = 'none';
  }
});

// Initialize countries array and fetch countries
let countries = [];
fetchCountries();
