

google.charts.load('current',{packages: ['corechart']});
google.charts.load('current', {packages: ['gauge']});


function drawChart()
{
	$.ajax({
		type: "GET",
		url: "./log/assignment3.csv",
		dataType: "text",
		success: function(response)
		{
			chartData = $.csv.toArrays(response, {onParseValue: $.csv.hooks.castToScalar});
			var rows = chartData.length;
			var chartArray = [];

			var gdata = new google.visualization.arrayToDataTable([
				[ {label: 'Data', id: 'data', type: 'date'},
				  {label: 'Temperature', id: 'tempData', type: 'number'},
				  {label: 'Humidity', id: 'humidity', type: 'number'}]
			]);

			for (var x = 0; x < rows; x++)
			{
				gdata.addRow([new Date(chartData[x][0], chartData[x][1], chartData[x][2], chartData[x][3], chartData[x][4], chartData[x][5], chartData[x][6], chartData[x][7])]);
			}

			var options = {
				title: 'Temperature Data & Humidity Log',
				curveType: 'function',
				legend: {position: 'bottom'}
			};

			chart.draw(gdata, options);
		}
	});
}

//Main program execute function
function go()
{
	drawChart();
	setInterval(function(){
		time = new Date();
		console.clear();
		console.log('Chart has been updated: '+time);
		drawChart();
	}, 60000);
}

