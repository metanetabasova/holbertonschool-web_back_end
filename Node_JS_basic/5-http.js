const http = require('http');
const fs = require('fs');

const DB_FILE = process.argv[2] || '';

const countStudents = (dataPath) => new Promise((resolve, reject) => {
  if (!dataPath) {
    reject(new Error('Cannot load the database'));
    return;
  }
  fs.readFile(dataPath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim().length > 0);

    if (lines.length <= 1) {
      resolve('Number of students: 0');
      return;
    }

    const studentLines = lines.slice(1);
    const responseParts = [`Number of students: ${studentLines.length}`];

    const fields = {};

    studentLines.forEach((line) => {
      const studentData = line.split(',');
      const firstname = studentData[0];
      const field = studentData[3];

      if (firstname && field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    Object.keys(fields).forEach((field) => {
      responseParts.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    });

    resolve(responseParts.join('\n'));
  });
});

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const responseText = 'This is the list of our students\n';
    countStudents(DB_FILE)
      .then((data) => {
        res.end(`${responseText}${data}`);
      })
      .catch((err) => {
        res.end(`${responseText}${err.message}`);
      });
  }
});

app.listen(1245);

module.exports = app;
