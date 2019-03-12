
#!/usr/bin/env node
//This file uses ajax to read the assignment3.csv file as text. It also utilizes the jquery-csv library in order to convert its contents to an array.
//This is essential in order to establish the chart for displaying the temperature data.

function readCSV()
{
	$.ajax({
		type: "GET",
		url: "ELSpring2018/code/03_blinker/log/assignment3.db",
		dataType: "text",
		success: function(response)
		{
			chartData = $.csv.toArrays(response, {onParseValue: $.csv.hooks.castToScalar});
			console.log(chartData);
		}
	});
}

