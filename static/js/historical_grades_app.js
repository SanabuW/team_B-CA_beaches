// //////////////
// BEGIN MAIN //
// //////////////
Promise.all([
    d3.json("/api/years"),
    d3.json("/api/grades_geojson")

]).then((yearsList) => {
    console.log(yearsList)
    //MAY NEED CHANGING
    var timelapse_geojson = yearsList[1]

/**============================================
 *  PROMISE DATA HANDLING FOR TIMELAPSE MAP
 *=============================================**/

    timelapseCreator(timelapse_geojson);

/**============================================
 *  PROMISE DATA HANDLING FOR TIME CHART
 *=============================================**/
    // create 3D bar chart
    gradeBarCreator(yearsList);



    // PREVIOUS CODE
    // console.log("building dropdown from:")
    // console.log(yearsList);

    // // use ids to generate our dropdown menu
    // buildDropdown(yearsList[0]);

    // // initialize page with data
    // optionChanged(yearsList[0][0], "dry");

    // // Getting a reference to the button on the page
    // //  with the id property set to filter-btn
    // var button = d3.select("#filter-btn");

    // // Create event handler for clicking the button
    // button.on("click", runEnter);


});
