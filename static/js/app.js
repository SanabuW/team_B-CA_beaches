/* data routes */
const beaches_url = "/api/beaches";
const grades_url = "/api/grades";
const grades_dummy_url = "/api/grades_dummy";

// Creating map object
var myMap = L.map("mapviz", {
    center: [34.019625000000000, -118.510699000000000],
    zoom: 8
});
  
// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
}).addTo(myMap);

// Read in beach data and get marker clusters
Promise.all([
    d3.json(beaches_url)
    ]).then(function(data) {
        console.log(data);

        var markers = L.markerClusterGroup();
        console.log(data[0][0].latitude);
        // Loop through data
        for (var i = 0; i < data[0].length; i++) {

            var beachdata = data[0];
            
            console.log(beachdata[i].latitude);
            
            if (beachdata) {
                markers.addLayer(L.marker([beachdata[i].latitude, beachdata[i].longitude]).bindPopup("<h4>Beach Name:" + beachdata[i].beach_name + "</h4><hr><p>" + beachdata[i].address + ", " + beachdata[i].city + ", " + beachdata[i].state + " " + beachdata[i].zip + "</p>" + "<p><b>Activities: " +  beachdata[i].activities + "</p>" + "<p><b>Amenities: " + beachdata[i].amenities + "<b></p>"));
            }
    
        }
            
        myMap.addLayer(markers);
});

// function createMarkers(response) {
//     var markers = L.markerClusterGroup();

//     // Loop through data
//     for (var i = 0; i < response.length; i++) {

//         markers.addLayer(L.marker([response.latitude, response.longitude])
//             .bindPopup("<h4>Beach Name:" + response.beach_name + "</h4><hr><p>" + response.address + ", " + response.city + ", " + response.state + " " + response.zip + "</p>" + "<p><b>Activities: " +  response.activities + "</p>" + "<p><b>Amenities: " + response.amenities + "<b></p>"));
//     }
            
//     myMap.addLayer(markers);
// }
