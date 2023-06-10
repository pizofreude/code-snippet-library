fetch("/api/data")
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.error("Error:", error);
    });


// This is JavaScript code that fetches data from an API and logs it to the console.

// The fetch function sends a request to the specified URL and returns a Promise that resolves to the Response object representing the response to the request.

// The first then method extracts the JSON body content from the response object.

// The second then method logs the data to the console.

// The catch method logs any errors that occur during the request.