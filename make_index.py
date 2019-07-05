import os
directory = 'Dalaran/'
os.walk(directory)

pre_body = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dalaran Guild Index</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>"""

directory_list = [x[0] for x in os.walk(directory)]

with open(f'index.html', 'w') as outfile:
    outfile.write(pre_body)
    outfile.write('<ul class="list-group">')
    for i in directory_list:
        outfile.write(f"<li class='list-group-item'><a href='{i}/Latest_links.html'>{i}</a></li>")
    outfile.write('</ul>')
    outfile.write('</body>')
    outfile.write('</html>')

# TODO:
# Make this output pretty
# Write in order of ranks
# Make a cutoff for each boss killed
# Right now, Guild ranks are self-referential and manually input.
# Needs an index page to get ranks but we need ranks to output on the index page

