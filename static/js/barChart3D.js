

// layout the page with the selected subject id
function barChart3D(data, yearChosen) {

	const month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];



	// clear tablespace
	var barChart = d3.select("#viz3");
	barChart.html("");



	anychart.onDocumentReady(function () {
		// set chart theme
		anychart.theme('lightBlue');
		// create data set on our data
		var dataSet = anychart.data.set(data);

		// map data for the first series, take x from the zero column and value from the first column of data set
		var firstSeriesData = dataSet.mapAs({ x: 0, value: 1 });

		// map data for the second series, take x from the zero column and value from the second column of data set
		var secondSeriesData = dataSet.mapAs({ x: 0, value: 2 });

		// map data for the second series, take x from the zero column and value from the third column of data set
		var thirdSeriesData = dataSet.mapAs({ x: 0, value: 3 });

		// map data for the fourth series, take x from the zero column and value from the fourth column of data set
		var fourthSeriesData = dataSet.mapAs({ x: 0, value: 4 });

		// map data for the fourth series, take x from the zero column and value from the fourth column of data set
		var fifthSeriesData = dataSet.mapAs({ x: 0, value: 5 });

		// map data for the fourth series, take x from the zero column and value from the fourth column of data set
		var sixthSeriesData = dataSet.mapAs({ x: 0, value: 6 });


		// create bar chart
		var chart = anychart.bar3d();


		// turn on chart animation
		chart.animation(true);

		// set chart padding
		chart.padding([10, 40, 5, 20]);

		// set chart title text settings
		chart.title('New Samples Taken in ' + yearChosen);
		// set titles for axises
		chart.xAxis().title('Date');
		chart.yAxis().title('Number of Samples Taken');

		chart.yScale().minimum(0);


      	chart.yAxis().labels().format('{%Value}{groupsSeparator: }');
		// set yAxis labels formatting, force it to add % to values



		// create first series with mapped data
		chart.bar(firstSeriesData).name("A+");

		// create second series with mapped data
		chart.bar(secondSeriesData).name("A");

		// create third series with mapped data
		chart.bar(thirdSeriesData).name("B");

		// create fourth series with mapped data
		chart.bar(fourthSeriesData).name("C");

		// create first series with mapped data
		chart.bar(fifthSeriesData).name("D");

		// create second series with mapped data
		chart.bar(sixthSeriesData).name("F");


		// turn on legend
		chart.legend().enabled(true).fontSize(13).padding([0, 0, 20, 0]);

		chart.interactivity().hoverMode('single');
		
		// set tooltip settings
		chart
			.tooltip()
			.positionMode('point')
			.position('right')
			.anchor('left-center')
			.offsetX(5)
			.offsetY(0)
			.format('{%Value}');
		
		chart.zAspect('10%').zPadding(20).zAngle(45).zDistribution(true);
		
		// set container id for the chart
		chart.container('viz3');
		
		// initiate chart drawing
			  chart.draw();

    });
}
