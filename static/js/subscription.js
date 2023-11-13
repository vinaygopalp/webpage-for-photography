 
document.addEventListener("DOMContentLoaded", function() {
    const radioButtons = document.querySelectorAll(".radio");
    const subscribeButton = document.getElementById("subscribeButton");

    subscribeButton.addEventListener("click", function() {
        let selectedOption = "";
        let selectedPrice = "";

        for (const radioButton of radioButtons) {
            if (radioButton.checked) {
                selectedOption = radioButton.id;
                selectedPrice = radioButton.getAttribute("data-price");
                break;
            }
        }

        if (selectedOption && selectedPrice) {
            // You can use selectedOption and selectedPrice as needed.
            console.log("Selected Option: " + selectedOption);
            console.log("Selected Price: " + selectedPrice);
        }
    });
});
 