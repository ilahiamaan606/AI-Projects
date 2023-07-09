document.getElementById("submit-btn").addEventListener("click", generateJoke);

function generateJoke() {
  var word = document.getElementById("word-input").value;

  // Make a POST request to the server endpoint
  fetch("https://joke-generator-kbj7.onrender.com/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ keyword: word })
  })
    .then(response => response.text())
    .then(data => {
      // Display the joke received from the server in the joke-container div

      var jokeContainer = document.getElementById("joke-container");
      jokeContainer.textContent = data;
    })
    .catch(error => {
      console.error("Error:", error);
    });
}
