// Function to translate letter grades to numerical values
function grade_changer(letter_grade) {
    var grade
    if (letter_grade == "A+") {
        grade = 15;
    } else if (letter_grade == "A") {
        grade = 14;
    } else if (letter_grade == "A-") {
        grade = 13;
    } else if (letter_grade == "B+") {
        grade = 12;
    } else if (letter_grade == "B") {
        grade = 11;
    } else if (letter_grade == "B-") {
        grade = 10;
    } else if (letter_grade == "C+") {
        grade = 9;
    } else if (letter_grade == "C") {
        grade = 8;
    } else if (letter_grade == "C-") {
        grade = 7;
    } else if (letter_grade == "D+") {
        grade = 6;
    } else if (letter_grade == "D") {
        grade = 5;
    } else if (letter_grade == "D-") {
        grade = 4;
    } else if (letter_grade == "F+") {
        grade = 3;
    } else if (letter_grade == "F") {
        grade = 2;
    } else if (letter_grade == "F-") {
        grade = 1;
    } else {
        grade = 0;
    }
    return grade
}


// Preparing map elements
    var fin_grades_layergroup = {
        final_grades_layer: new L.LayerGroup()
    };

    var final_grades_map = L.map("latest_grades_viz", {
        center: [37.4131, -120.2870],
        zoom: 5,
        layers: [
            fin_grades_layergroup.final_grades_layer,
        ]
    });
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "light-v10",
        accessToken: "pk.eyJ1Ijoic3dhc2hpIiwiYSI6ImNrbWh6YW80ajBjZG0yb3FteGR4dm40dWoifQ.GIb3ngQ1Ooc4eRYJLd4zLg"
    }).addTo(final_grades_map);

    lightmap.addTo(final_grades_map);


// Function to translate grade values to different colors for icons
function icon_generator(grade_info){
    var m_color
    if (grade_info >= 13) {
        m_color = 'blue'
    } else if (grade_info >= 10) {
        m_color = 'green'
    } else if (grade_info >= 7) {
        m_color = 'yellow'
    } else if (grade_info >= 4) {
        m_color = 'orange'
    } else {
        m_color = 'red'
    }

    // Definition for markers using Extra-markers plugin
    const newMarker = L.ExtraMarkers.icon({
        prefix: 'fa',
        icon: "fa-water",
        iconColor: "white",
        markerColor: m_color,
        shape: 'circle'
    })
    return newMarker
};


/**======================
 *Map code for timelapse
 *========================**/
    // Preparing map elements
    var layers = {
        grades_layer: new L.LayerGroup()
    };

    var myMap = L.map("grades_time_viz", {
        center: [37.4131, -120.2870],
        zoom: 5,
        layers: [
            layers.grades_layer,
        ]
    });

    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "light-v10",
        accessToken: "pk.eyJ1Ijoic3dhc2hpIiwiYSI6ImNrbWh6YW80ajBjZG0yb3FteGR4dm40dWoifQ.GIb3ngQ1Ooc4eRYJLd4zLg"
    }).addTo(myMap);

    lightmap.addTo(myMap);

    function icon_generator(grade_info){
        var m_color
        if (grade_info >= 13) {
            m_color = 'blue'
        } else if (grade_info >= 10) {
            m_color = 'green'
        } else if (grade_info >= 7) {
            m_color = 'yellow'
        } else if (grade_info >= 4) {
            m_color = 'orange'
        } else {
            m_color = 'red'
        }
    }













// API routes to pull data in
const latest_grades_url = "/api/latest_grades";
const grades_geojson_url = "/api/grades_geojson";


// Handling the data and building markers
    Promise.all([
        d3.json(latest_grades_url),
        d3.json(grades_geojson_url)
        ]).then(function(data) {
            latest_grades_obj = data[0]
            for (var i = 0; i < latest_grades_obj.length; i++) {
                // Converting letter grades to numerical values
                latest_grades_obj[i].dry_grade_num = grade_changer(latest_grades_obj[i].dry_grade);
                grade_for_icon = latest_grades_obj[i].dry_grade_num;
                var newMarker = L.marker([latest_grades_obj[i].latitude, latest_grades_obj[i].longitude], {icon: icon_generator(grade_for_icon)})
                    .bindPopup(latest_grades_obj[i].name1 + "<hr> Grade: " + latest_grades_obj[i].dry_grade + "<br>" + latest_grades_obj[i].grade_updated)
                    .addTo(fin_grades_layergroup.final_grades_layer);
                newMarker.addTo(fin_grades_layergroup.final_grades_layer);

            grades_geojson_obj = data[1]

// Preparing map elements
  var layers = {
    grades_layer: new L.LayerGroup()
  };

  var myMap = L.map("grades_time_viz", {
    center: [37.4131, -120.2870],
    zoom: 5,
    layers: [
        layers.grades_layer,
      ]
  });

  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "light-v10",
    accessToken: "pk.eyJ1Ijoic3dhc2hpIiwiYSI6ImNrbWh6YW80ajBjZG0yb3FteGR4dm40dWoifQ.GIb3ngQ1Ooc4eRYJLd4zLg"
  }).addTo(myMap);

  lightmap.addTo(myMap);

function icon_generator(grade_info){
    var m_color
    if (grade_info >= 13) {
        m_color = 'blue'
    } else if (grade_info >= 10) {
        m_color = 'green'
    } else if (grade_info >= 7) {
        m_color = 'yellow'
    } else if (grade_info >= 4) {
        m_color = 'orange'
    } else {
        m_color = 'red'
    }
  }


            }
    // Testing output
    console.log(latest_grades_obj)
});