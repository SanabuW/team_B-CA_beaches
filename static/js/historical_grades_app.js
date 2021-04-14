// //////////////
// BEGIN MAIN //
// //////////////
Promise.all([
    d3.json("/api/years"),
    d3.json("/api/grades_geojson")

]).then((yearsList) => {
    console.log(yearsList)
    // Breaking down to get only the geoJSON result
    var timelapse_geojson = yearsList[1]

/**============================================
 *  PROMISE DATA HANDLING FOR TIMELAPSE MAP
 *=============================================**/

    timelapseCreator(timelapse_geojson);

/**============================================
 *  PROMISE DATA HANDLING FOR TIME CHART
 *=============================================**/
    // create 3D bar chart
    // Result of the queries was not separated to only the api/years query, 
    //   to match data indexing of gradeBarCreator. Improvement point for later
    gradeBarCreator(yearsList);
});
