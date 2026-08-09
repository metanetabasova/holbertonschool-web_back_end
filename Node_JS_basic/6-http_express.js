import express from 'express';

const app = express();
const PORT = 1245;

app.length('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(PORT, () => {
  console.log(`Server runnig on port ${PORT}`);
});

module.exports = app;
export default app;
