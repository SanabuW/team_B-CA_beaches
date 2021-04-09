function buildDropdown(yearList) {
	// locate the target for the dropdown values
	var dropdownTarget = d3.select("#selYear");

	// loop through the ids and add them to the
	// dropdown menu as options
	for (let i = 0; i <= yearList.length; i++) {
		dropdownTarget.append("option").attr("value", yearList[i]).text(yearList[i]);
	}
}