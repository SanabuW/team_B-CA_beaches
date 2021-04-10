function timelapseCreator (grades_geojson) {
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
            } else if (grade_info >= 0) {
                m_color = 'red'
            } else {
                m_color = 'black'
            }
          }


          function beachfeed_callback(data) {
            var getInterval = function (beach) {

              return {
                start: beach.properties.time_millisec,
                end: beach.properties.time_millisec + 172600000,
              };
            };
            var timelineControl = L.timelineSliderControl({
              formatOutput: function (date) {
                return new Date(date).toString().slice(4,15);
              },
            });
            var timeline = L.timeline(data, {
              getInterval: getInterval,
              pointToLayer: function (data, latlng) {
                // var hue_min = 120;
                var hue_min = 140;
                var hue_max = 0;
                var hue =
                  (data.properties.dry_grade_num / 15) * (hue_min - hue_max) + hue_max;
                // var color_val
                // if (data.properties.dry_grade_num = 0) {
                //   color_val = "hsl(0, 100%, 50%)"
                // } else {color_val = "hsl(" + hue + ", 100%, 50%)"}
                return L.circleMarker(latlng, {
                  radius: 10,
                  color: "hsl(" + hue + ", 100%, 50%)",
                  fillColor: "hsl(" + hue + ", 100%, 50%)",
                }).bindPopup(
                  data.properties.beach_name
                );
              },
            });
            timelineControl.addTo(gradesMap);
            timelineControl.addTimelines(timeline);
            timeline.addTo(gradesMap);
          }


          for (var i = 0; i < grades_geojson.features.length; i++) {
            grades_geojson.features[i].properties.dry_grade_num = grade_changer(grades_geojson.features[i].properties.grade);
            var time_var = new Date(grades_geojson.features[i].properties.time.slice(5, 16))
            grades_geojson.features[i].properties.time_millisec = time_var.getTime();
          }

          beachfeed_callback(grades_geojson)

            console.log(grades_geojson)
        };