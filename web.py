from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<body>

<h2>KABILAN (26010850)</h2>

<table border="1">
    <tr>
        <th>Specification</th>
        <th>Details</th>
    </tr>
    <tr>
        <td>Device Name</td>
        <td>KABILAN</td>
    </tr>
    <tr>
        <td>Processor</td>
        <td>Intel(R) Core(TM) 5 210H (2.20 GHz)</td>
    </tr>
    <tr>
        <td>Installed RAM</td>
        <td>16.0 GB (15.7 GB usable)</td>
    </tr>
    <tr>
        <td>Graphics Card</td>
        <td>Intel(R) Graphics (128 MB)</td>
    </tr>
    <tr>
        <td>Storage</td>
        <td>134 GB of 477 GB used</td>
    </tr>
    <tr>
        <td>Device ID</td>
        <td>C9100A77-FB9B-4FC9-BD4B-28677DB9E25D</td>
    </tr>
    <tr>
        <td>Product ID</td>
        <td>00342-42954-11613-AAOEM</td>
    </tr>
    <tr>
        <td>System Type</td>
        <td>64-bit operating system, x64-based processor</td>
    </tr>
    <tr>
        <td>Pen and Touch</td>
        <td>No pen or touch input is available for this display</td>
    </tr>
</table>

</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()