    /* data routes */
    const beaches_url = "/api/beaches";
    const grades_url = "/api/grades";
    const grades_dummy_url = "/api/grades_dummy";

    Promise.all([
        d3.json(beaches_url),
        d3.json(grades_url),
        d3.json(grades_dummy_url)
        ]).then(function(data) {
            console.log(data)
});


