const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const database = process.argv[2];

    res.write('This is the list of our students\n');

    fs.promises.readFile(database, 'utf8')
      .then((data) => {
        const rows = data.split('\n').filter((line) => line.trim() !== '');
        const students = rows.slice(1);
        const byField = {};

        students.forEach((student) => {
          const [firstname, , , field] = student.split(',');
          if (!byField[field]) {
            byField[field] = [];
          }
          byField[field].push(firstname);
        });

        let output = `Number of students: ${students.length}\n`;

        Object.keys(byField).forEach((field, index, array) => {
          output += `Number of students in ${field}: ${byField[field].length}. List: ${byField[field].join(', ')}`;
          if (index < array.length - 1) {
            output += '\n';
          }
        });

        res.statusCode = 200;
        res.end(output);
      })
      .catch(() => {
        res.statusCode = 200;
        res.end('Cannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245);

module.exports = app;