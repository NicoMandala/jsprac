const express = require('express');
const app = express();
const port = 3000;

const db = require('./models');
console.log('DB models imported:', db);

app.use(express.json());

// app.get('/', (req, res) => {
//     res.send('Hello World!');
// });

const userRoutes = require('./routes/userRoutes');
console.log('User routes imported:', userRoutes);

app.use('/v1', userRoutes);

// Sync database
db.UserBookReviews.sequelize.sync().then(() => {
    app.listen(port, () => {
        console.log(`Server is running on http://localhost:${port}`);
    });
}).catch(err => {
    console.error('Unable to connect to the database:', err); 
});
