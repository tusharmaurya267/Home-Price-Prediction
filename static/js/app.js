document.addEventListener("DOMContentLoaded", function () {
    // Fetch locations and populate the dropdown on page load
    fetchLocations();

    // Attach a click event listener to the "Estimate Price" button
    document.getElementById("estimateButton").addEventListener("click", function () {
        // Get user inputs
        const location = document.getElementById("location").value;
        const area = parseFloat(document.getElementById("area").value);
        const bhk = parseInt(document.getElementById("bhk").value);
        const bathrooms = parseInt(document.getElementById("bathrooms").value);

        // Check if all inputs are valid
        if (location === "" || isNaN(area) || isNaN(bhk) || isNaN(bathrooms)) {
            alert("Please fill in all fields with valid data.");
            return;
        }
        // console.log(location,area,bhk,bathrooms)
        // Send the data to the server for prediction
        
        sendPredictionRequest(location, area, bhk, bathrooms);

    });
});

function fetchLocations() {
    // Replace with your API endpoint to fetch locations in JSON format
    const apiUrl = "http://127.0.0.1:5000/get_location_names";
    // const apiUrl = "/get_location_names";

    fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
            const locationDropdown = document.getElementById("location");

            // Populate the dropdown with fetched locations
            data.locations.forEach((location) => {
                const option = document.createElement("option");
                option.value = location;
                option.textContent = location;
                locationDropdown.appendChild(option);
            });
        })
        .catch((error) => {
            console.error("Error fetching locations:", error);
        });
}

function sendPredictionRequest(location, area, bhk, bathrooms) {
    // your server's prediction API endpoint
    const apiUrl = "http://127.0.0.1:5000/predict_home_price";
    // const apiUrl = "/predict_home_price";

    // Create a data object to send in the request body
    const data = {
        location: location,
        area: area,
        bhk: bhk,
        bathrooms: bathrooms,
    };


    // Send a POST request to the API endpoint
    fetch(apiUrl, 
        {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), // body data type must match "Content-Type" header
    }
    )

    .then((response) => response.json())
    .then((result) => {
        
        // Display the estimated price on the page
        console.log(result)
        const estimatedPrice = document.getElementById("estimatedPrice");
        estimatedPrice.textContent = result.estimated_price;
        
    })
    .catch((error) => {
        console.error("Error predicting home price:", error);
    }); 
}