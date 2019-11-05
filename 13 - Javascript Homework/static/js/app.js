// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

console.log(tableData);
// Step 1: Loop Through `data` and console.log each UFO sighting object
tableData.forEach(function(ufoSighting) {
    console.log(ufoSighting);
});
// Step 3:  Use `Object.entries` to console.log each UFO sighting value
tableData.forEach(function (ufoSighting) {
    console.log(ufoSighting);
    //var row = tbody.append("tr");

    Object.entries(ufoSighting).forEach(function([key, value]) {
        console.log(key,value);
    });
});
// Step 4: Use d3 to append 1 cell per UFO sighting value (date, city, state, etc)
tableData.forEach(function(ufoSighting) {
    console.log(ufoSighting);
    var row = tbody.append("tr");

    Object.entries(ufoSighting).forEach(([key,value]) => {
        var cell = row.append("td");
        cell.text(value);
    });
});

// Select the button
// implementing fuction to "submit button"      

var button = d3.select("#filter-btn");

button.on("click", function() {
    
    // clears the data of the current table        
     tbody.html("");
     // stop the page from refresh
     d3.event.preventDefault();

    var inputElement = d3.select( "#datetime"); 
    var inputValue = inputElement.property("value");

    console.log(inputValue);
    console.log(tableData);

    var filteredData = tableData.filter(ufoSighting => ufoSighting.datetime === inputValue);

    console.log(filteredData);

    filteredData.forEach((selection) => {
        // for each "element" in the selected date create a row
        var row = tbody.append("tr");
        //'unpack' the array elements using Object.entries
        Object.entries(selection).forEach(([key,value]) => {
            var cell = row.append("td");
            // adds the "value" to each row in the table
            cell.text(value);
        });
    });  

});






