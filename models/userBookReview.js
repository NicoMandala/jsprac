// models/userBookReview.js
module.exports = (sequelize, DataTypes) => {
    const UserBookReview = sequelize.define('UserBookReviews', {
        id: {
            type: DataTypes.INTEGER,
            autoIncrement: true,
            primaryKey: true
        },
        username: {
            type: DataTypes.STRING,
            allowNull: false
        },
        book_rating: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        user_age: {
            type: DataTypes.INTEGER,
            allowNull: false
        },
        book_genre: {
            type: DataTypes.STRING,
            allowNull: false
        },
        quote_or_review_text: {
            type: DataTypes.TEXT
        },
        favorite_authors_or_psychologists: {
            type: DataTypes.STRING
        }
    },{
        timestamps: false
    });

    return UserBookReview;
};
