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

    Promise.all([
        d3.json(grades_url),
        d3.json(latest_grades_url)
        ]).then(function(data) {
            console.log(data)

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
