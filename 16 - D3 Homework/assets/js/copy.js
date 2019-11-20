  // Import Data
d3.csv("assets/data/data.csv").then(function(censusData) {
    //console.log(censusData);
    // Step 1: Parse Data/Cast as numbers
    // ==============================
    censusData.forEach(function(data) {
        data.poverty = +data.poverty;
        data.healthcare = +data.healthcare;
        data.age= +data.age;
        data.ob
      });
      
    // Step 2: Create scale functions
    // ==============================
    var xLinearScale = d3.scaleLinear()
        .domain([8, d3.max(censusData, d => d.poverty)])
        .range([0, width*0.8]);
    
    var yLinearScale = d3.scaleLinear()
        .domain([0, d3.max(censusData, d => d.healthcare)])
        .range([height, 0]);

    // Step 3: Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    // Step 5: Create Circles
    // ==============================
    var circlesGroup = chartGroup.selectAll("circle")
    .data(censusData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "15")
    .attr("fill", "teal")
    .attr("opacity", ".5");

    var text = chartGroup.selectAll()
   .data(censusData)
   .enter()
   .append("text")
   .attr("x", d => xLinearScale(d.poverty))
   .attr("y", d => yLinearScale(d.healthcare))
   .text(function (d) { return d.abbr; })
   .attr("font-family",  "Arial")
   .attr("fill", "white")
   .attr("font-size", "10px")
   .attr("text-anchor", "middle"); 

    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height *1.3 / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .attr("font-weight", "bold")
      .text("Lacks Healthcare (%)");

    chartGroup.append("text")
      .attr("transform", `translate(${width*0.7/ 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .attr("font-weight", "bold")
      .text("In Poverty (%)");
  }).catch(function(error) {
    console.log(error);
  });