const Sequelize = require('sequelize');
const sequelize = require('../config/database');

const db = {};  

db.Sequelize = Sequelize;
db.sequelize = sequelize;
console.log("reached 1-2 ")

// Models
db.User = require('./user')(sequelize, Sequelize.DataTypes);
db.UserBookReviews = require('./userBookReview')(sequelize, Sequelize.DataTypes);

console.log("reached 2 ")

module.exports = db;