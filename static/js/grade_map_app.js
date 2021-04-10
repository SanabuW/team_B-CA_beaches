/* data routes */
const beaches_url = "/api/beaches";
const grades_url = "/api/grades";
const grades_dummy_url = "/api/grades_dummy";
const latest_grades_url = "/api/latest_grades";

//     Promise.all([
//         d3.json(beaches_url),
//         d3.json(grades_url),
//         d3.json(grades_dummy_url)
//         ]).then(function(data) {
//             console.log(data)
// });
function grade_changer(letter_grade) {
//for each value
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






var layers = {
grades_layer: new L.LayerGroup()
};

var myMap = L.map("latest_grades_viz", {
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

const newMarker = L.ExtraMarkers.icon({
	prefix: 'fa',
	icon: "fa-water",
	iconColor: "white",
	markerColor: m_color,
	shape: 'circle'
})
return newMarker
};


// const marker_template = L.ExtraMarkers.icon({
//     markerColor: 'blue',
//     shape: 'circle'
// })
// // Layer control
// var overlays = {
//     "Latest Grades": layers.grades_layer,
//   };

Promise.all([
	d3.json(latest_grades_url)
	]).then(function(data) {
		latest_grades_obj = data[0]
		//for each obj in the array
		for (var i = 0; i < latest_grades_obj.length; i++) {
			latest_grades_obj[i].dry_grade_num = grade_changer(latest_grades_obj[i].dry_grade);
			// latest_grades_obj[i].wet_grade = grade_changer(latest_grades_obj[i].wet_grade);
			// latest_grades_obj[i].annual_summer_dry = grade_changer(latest_grades_obj[i].annual_summer_dry);
			// latest_grades_obj[i].annual_winter_dry = grade_changer(latest_grades_obj[i].annual_winter_dry);
			// latest_grades_obj[i].annual_year_wet = grade_changer(latest_grades_obj[i].annual_year_wet);
			grade_for_icon = latest_grades_obj[i].dry_grade_num;
			var newMarker = L.marker([latest_grades_obj[i].latitude, latest_grades_obj[i].longitude], {icon: icon_generator(grade_for_icon)})
				.bindPopup(latest_grades_obj[i].name1 + "<hr> Grade: " + latest_grades_obj[i].dry_grade)
				.addTo(layers.grades_layer);
			newMarker.addTo(layers.grades_layer);
			// L.marker([latest_grades_obj[i].latitude, latest_grades_obj[i].longitude]).addTo(layers.grades_layer);

			// L.marker([0,0], {icon: icon_generator(grade_for_icon)}).addTo(grades_layer);

			// L.marker([latest_grades_obj[i].latitude, latest_grades_obj[i].longitude], {icon: icon_generator(grade_for_icon)}).addTo(grades_layer);
		  }
		  console.log(latest_grades_obj)
});












// function buildPlot() {
//     /* data route */
//     const url = "/api/grades";
//     d3.json(url).then(function(response) {

//       console.log(response);

// //       const data = response;

// //       const layout = {
// //         scope: "usa",
// //         title: "Pet Pals",
// //         showlegend: false,
// //         height: 600,
// //               // width: 980,
// //         geo: {
// //           scope: "usa",
// //           projection: {
// //             type: "albers usa"
// //           },
// //           showland: true,
// //           landcolor: "rgb(217, 217, 217)",
// //           subunitwidth: 1,
// //           countrywidth: 1,
// //           subunitcolor: "rgb(255,255,255)",
// //           countrycolor: "rgb(255,255,255)"
// //         }
// //       };

// //       Plotly.newPlot("plot", data, layout);
//     });
// }

// buildPlot();

