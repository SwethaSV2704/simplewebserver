from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<html>
<head>
<title> My Laptop</title>
</head>
<body><center>
    <h1>My laptop configuration</h1>
    <table border="5" cell panding="1" align="center">
        <tr>
            <th>system specs</th>
            <th>discription</th>
       </tr>
       <tr>
            <td>processor</td>
            <td>13th Gen Intel(R) Core(TM) i5-1335U   1.30 GHz</td>
       </tr>
       <tr>
            <td>operating system</td>
            <td>windows 11 home single language 64</td>
       </tr>
       <tr>
            <td>graphic card</td>
            <td>Integrated Intel® Iris® Xe Graphics</td>
       </tr>
       <tr>
            <td>memory</td>
            <td>16 GB DDR4-3200MHz - (8 GB SODIMM + 8 GB Soldered)</td>
       </tr>
       <tr>
            <td>storage</td>
            <td>512 GB SSD M.2 2242 PCIe Gen4 TLC Opal</td>
        </tr>
        <tr>
             <td>display</td>
             <td>40.64cms (16) WUXGA (1920 x 1200), IPS, Anti-Glare, Non-Touch, 100%sRGB, 300 nits, 60Hz, Low Blue Light</td>

        </tr>
    </table>
</center>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()