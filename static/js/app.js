    /* data routes */
    const beaches_url = "/api/beaches";
    const grades_url = "/api/grades";
    const grades_dummy_url = "/api/grades_dummy";
    const latest_grades_url = "/api/latest_grades";

    Promise.all([
        d3.json(beaches_url),
        d3.json(grades_url),
        d3.json(grades_dummy_url),
        d3.json(latest_grades_url)
        ]).then(function(data) {
            console.log(data)
});


