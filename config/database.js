// config/database.

const Sequelize = require('sequelize');

const sequelize = new Sequelize('my_express_api', 'root', 'LaMaFe@1', {
    host: 'localhost',
    dialect: 'mysql'
    });

module.exports = sequelize;