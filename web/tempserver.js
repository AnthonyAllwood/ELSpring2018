//This code utilizes the built-in nodejs web server in order to run the index.html file in any browser

//Load the http module to create an http server
var http = require('http');
var fs = require('fs');

//Port variable = 8080
const PORT = 8080;

//Read from index.html file
var html = fs.readFileSync('./index.html', ["utf-8"])
{


	http.createServer(function(request, response)
	{
		response.writeHeader(200, {"Content-Type": "text/html"});
		response.write(html);
		response.end();
	})
//Listen on port 8080
	.listen(PORT);

	console.log("Server running at http:/137.140.166.32:8080/");
};
