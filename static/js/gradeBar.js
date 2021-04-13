function countGrades(data, yearChosen) {

	const grades = ["A+", "A", "B", "C", "D", "F"];

	var dataCounts = {"A+": {"Jan": {"dry": 0, "wet": 0},
							 "Feb": {"dry": 0, "wet": 0},
							 "Mar": {"dry": 0, "wet": 0},
							 "Apr": {"dry": 0, "wet": 0},
							 "May": {"dry": 0, "wet": 0},
							 "Jun": {"dry": 0, "wet": 0},
							 "Jul": {"dry": 0, "wet": 0},
							 "Aug": {"dry": 0, "wet": 0},
							 "Sep": {"dry": 0, "wet": 0},
							 "Oct": {"dry": 0, "wet": 0},
							 "Nov": {"dry": 0, "wet": 0},
							 "Dec": {"dry": 0, "wet": 0}},
					   "A": {"Jan": {"dry": 0, "wet": 0},
							 "Feb": {"dry": 0, "wet": 0},
							 "Mar": {"dry": 0, "wet": 0},
							 "Apr": {"dry": 0, "wet": 0},
							 "May": {"dry": 0, "wet": 0},
							 "Jun": {"dry": 0, "wet": 0},
							 "Jul": {"dry": 0, "wet": 0},
							 "Aug": {"dry": 0, "wet": 0},
							 "Sep": {"dry": 0, "wet": 0},
							 "Oct": {"dry": 0, "wet": 0},
							 "Nov": {"dry": 0, "wet": 0},
							 "Dec": {"dry": 0, "wet": 0}},
					   "B": {"Jan": {"dry": 0, "wet": 0},
							 "Feb": {"dry": 0, "wet": 0},
							 "Mar": {"dry": 0, "wet": 0},
							 "Apr": {"dry": 0, "wet": 0},
							 "May": {"dry": 0, "wet": 0},
							 "Jun": {"dry": 0, "wet": 0},
							 "Jul": {"dry": 0, "wet": 0},
							 "Aug": {"dry": 0, "wet": 0},
							 "Sep": {"dry": 0, "wet": 0},
							 "Oct": {"dry": 0, "wet": 0},
							 "Nov": {"dry": 0, "wet": 0},
							 "Dec": {"dry": 0, "wet": 0}},
					   "C": {"Jan": {"dry": 0, "wet": 0},
							 "Feb": {"dry": 0, "wet": 0},
							 "Mar": {"dry": 0, "wet": 0},
							 "Apr": {"dry": 0, "wet": 0},
							 "May": {"dry": 0, "wet": 0},
							 "Jun": {"dry": 0, "wet": 0},
							 "Jul": {"dry": 0, "wet": 0},
							 "Aug": {"dry": 0, "wet": 0},
							 "Sep": {"dry": 0, "wet": 0},
							 "Oct": {"dry": 0, "wet": 0},
							 "Nov": {"dry": 0, "wet": 0},
							 "Dec": {"dry": 0, "wet": 0}},
					   "D": {"Jan": {"dry": 0, "wet": 0},
							 "Feb": {"dry": 0, "wet": 0},
							 "Mar": {"dry": 0, "wet": 0},
							 "Apr": {"dry": 0, "wet": 0},
							 "May": {"dry": 0, "wet": 0},
							 "Jun": {"dry": 0, "wet": 0},
							 "Jul": {"dry": 0, "wet": 0},
							 "Aug": {"dry": 0, "wet": 0},
							 "Sep": {"dry": 0, "wet": 0},
							 "Oct": {"dry": 0, "wet": 0},
							 "Nov": {"dry": 0, "wet": 0},
							 "Dec": {"dry": 0, "wet": 0}},
					   "F": {"Jan": {"dry": 0, "wet": 0},
							 "Feb": {"dry": 0, "wet": 0},
							 "Mar": {"dry": 0, "wet": 0},
							 "Apr": {"dry": 0, "wet": 0},
							 "May": {"dry": 0, "wet": 0},
							 "Jun": {"dry": 0, "wet": 0},
							 "Jul": {"dry": 0, "wet": 0},
							 "Aug": {"dry": 0, "wet": 0},
							 "Sep": {"dry": 0, "wet": 0},
							 "Oct": {"dry": 0, "wet": 0},
							 "Nov": {"dry": 0, "wet": 0},
							 "Dec": {"dry": 0, "wet": 0}}	 	 	 		 		 
					}
		
	var yearStr = yearChosen.toString();
	var date_list = [];
	var year = "";
	var month = "";

	for (var i = 0; i < data.length; i++) {
		date_list = data[i].grade_updated.split(" ");
		year = date_list[3];
		month = date_list[2];


		if (year == yearStr) {
			if (grades.indexOf(data[i].dry_grade) != -1) {
				dataCounts[data[i].dry_grade][month]["dry"]++;
			}
			if (grades.indexOf(data[i].wet_grade) != -1) {
				dataCounts[data[i].wet_grade][month]["wet"]++;

			}
		}		
	}
	console.log(dataCounts);

	return (dataCounts)
}



// layout the page with the selected subject id
 function optionChanged(yearChosen, whichGrade) {

	const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
	const grades = ["A+", "A", "B", "C", "D", "F"];

//	var api_str = "api/count/" + yearChosen;
	var api_str = "api/grades";

 	Promise.all([
  	// read in the JSON study data 
	d3.json(api_str)]).then((gradeData) => {
		  console.log(gradeData[0]);

		var counts = countGrades(gradeData[0], yearChosen);
		console.log(counts);
		// var data = []
		// gradeCounts[0].forEach(item =>
		// 	data.push({x: month[item[1] - 1], y:item[0], heat:item[2]}));
		var data = []
		for (var i = 0; i < months.length; i++) {
			month_list = [];
			month_list.push(months[i]);
			for (var j = 0; j < grades.length; j++) {
				month_list.push(counts[grades[j]][months[i]][whichGrade]);
			}
			data.push(month_list);
		}


		console.log(data);
	

		barChart3D(data, yearChosen, whichGrade);


	});

}

function runEnter() {
	// Prevent the page from refreshing
	d3.event.preventDefault();


  	var dropdownElement = d3.select("#selYear");

  	// Get the value property of the input element
  	var yearChosen = dropdownElement.property("value");

	var radioElement = d3.select('input[name="gradeType"]:checked');

  	// Get the value property of the input element
  	var whichGrade = radioElement.property("value");

	optionChanged(yearChosen, whichGrade);


}

function gradeBarCreator(yearsList) {

	console.log("building dropdown from:")
	console.log(yearsList);
	// use ids to generate our dropdown menu
	buildDropdown(yearsList[0]);

	// initialize page with data
	optionChanged(yearsList[0][0], "dry");

	// Getting a reference to the button on the page
	//  with the id property set to `filter-btn`
	var button = d3.select("#filter-btn");

	// Create event handler for clicking the button
	button.on("click", runEnter);
}

