import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  if (!filePath) {
    reject(new Error('Cannot load the database'));
    return;
  }
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim().length > 0);
    if (lines.length <= 1) {
      resolve({});
      return;
    }

    const studentLines = lines.slice(1);
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

    resolve(fields);
  });
});

export default readDatabase;
export { readDatabase };
