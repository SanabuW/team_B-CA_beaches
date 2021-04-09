// //////////////
// BEGIN MAIN //
// //////////////
Promise.all([
    d3.json("/api/grades_geojson"),
    // d3.json("/api/years"),
]).then((result) => {

    var timelapse_geojson = result[0]
    // var yearsList = result[1]

/**============================================
 *  PROMISE DATA HANDLING FOR TIMELAPSE MAP
 *=============================================**/

    timelapseCreator(timelapse_geojson);

// /**============================================
//  *  PROMISE DATA HANDLING FOR TIME CHART
//  *=============================================**/
//     console.log("building dropdown from:")
//     console.log(yearsList);

//     // use ids to generate our dropdown menu
//     buildDropdown(yearsList[0]);

//     // initialize page with data
//     optionChanged(yearsList[0][0], "dry");

//     // Getting a reference to the button on the page
//     //  with the id property set to filter-btn
//     var button = d3.select("#filter-btn");

//     // Create event handler for clicking the button
//     button.on("click", runEnter);

});
