function timelapseCreator (grades_geojson) {
          // Function to change string grades into a numerical value
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
          var timelapse_layers = {
            timelapse_grades_layer: new L.LayerGroup()
          };

          var gradesMap = L.map("grades_time_viz", {
            center: [37.4131, -120.2870],
            zoom: 5,
            layers: [
              timelapse_layers.timelapse_grades_layer,
              ]
          });

          var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
            attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
            maxZoom: 18,
            id: "light-v10",
            accessToken: "pk.eyJ1Ijoic3dhc2hpIiwiYSI6ImNrbWh6YW80ajBjZG0yb3FteGR4dm40dWoifQ.GIb3ngQ1Ooc4eRYJLd4zLg"
          }).addTo(gradesMap);

          lightmap.addTo(gradesMap);



          // Begin use of Leaflet-timeline plugin
          // Function to define creation of markers
          function beachfeed_callback(data) {
            var getInterval = function (beach) {
              // Define the span of time each marker should stay displayed
              return {
                start: beach.properties.time_millisec,
                end: beach.properties.time_millisec + 172600000,
              };
            };
            // Create slider control
            var timelineControl = L.timelineSliderControl({
              formatOutput: function (date) {
                // Truncate the date display for the time controller (Would display the full datetime to the second by default)
                return new Date(date).toString().slice(4,15);
              },
            });
            // Create the actual markers in a L.timeline() layer object
            var timeline = L.timeline(data, {
              getInterval: getInterval,
              pointToLayer: function (data, latlng) {
                var hue_min = 140;
                var hue_max = 0;
                // Dynamically assign a hue based off the numerical grade
                var hue =
                  (data.properties.dry_grade_num / 15) * (hue_min - hue_max) + hue_max;
                return L.circleMarker(latlng, {
                  radius: 10,
                  // Use HSL coloring using the dynamically set hue
                  color: "hsl(" + hue + ", 100%, 50%)",
                  fillColor: "hsl(" + hue + ", 100%, 50%)",
                }).bindPopup(
                  data.properties.beach_name
                );
              },
            });
            // Adding controls to the interface
            timelineControl.addTo(gradesMap);
            timelineControl.addTimelines(timeline);

            // Adding timeline layer to map
            timeline.addTo(gradesMap);
          }

          // Cleaning/formatting geoJSON data to prepare for marker layer creation
          for (var i = 0; i < grades_geojson.features.length; i++) {
            // Create a new key "dry_grade_num" and insert as its value an int corresponding to the letter grade
            grades_geojson.features[i].properties.dry_grade_num = grade_changer(grades_geojson.features[i].properties.grade);
            // Pulling date format from postgreSQL outputs a string, whle Leaflet-timeline requires millisecond time. Converting string to millisecond time
            var time_var = new Date(grades_geojson.features[i].properties.time.slice(5, 16))
            grades_geojson.features[i].properties.time_millisec = time_var.getTime();
          }

          // Execute creation of vizualization
          beachfeed_callback(grades_geojson)

            console.log(grades_geojson)
        };