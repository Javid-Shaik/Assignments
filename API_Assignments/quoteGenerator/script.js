// Select HTML elements
const quoteTextElement = document.getElementById('quote-text');
const authorElement = document.getElementById('author');
const newQuoteButton = document.getElementById('new-quote-button');

// Function to fetch a random quote
function fetchRandomQuote() {
  // Replace the API URL with the URL of the quotes API you want to use
  fetch('https://api.quotable.io/random')
    .then((response) => response.json())
    .then((data) => {
      // Update the HTML elements with the quote and author
      quoteTextElement.textContent = data.content;
      authorElement.textContent = `- ${data.author}`;
    })
    .catch((error) => console.error('Error fetching data:', error));
}

// Event listener for the "New Quote" button
newQuoteButton.addEventListener('click', fetchRandomQuote);

// Fetch the first random quote when the page loads
fetchRandomQuote();
