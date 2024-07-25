const db = require('../models');
const UserBookReview = db.UserBookReviews;

// Create a new review
exports.createReview = async (req, res) => {
    try {
        const review = await UserBookReview.create(req.body);
        res.status(201).json(review);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

// Get all reviews for a user
exports.getAllReviews = async (req, res) => {
    console.log('Get all reviews for a user:' + req.query.username);
    try {
        const reviews = await UserBookReview.findAll({ where: { username: req.query.username } });
        res.status(200).json(reviews);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

// Get a specific review by ID
exports.getReviewById = async (req, res) => {
    try {
        const review = await UserBookReview.findByPk(req.params.id);
        if (review) {
            res.status(200).json(review);
        } else {
            res.status(404).json({ error: 'Review not found' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

// Update a review by ID
exports.updateReview = async (req, res) => {
    try {
        const review = await UserBookReview.findByPk(req.params.id);
        if (review) {
            await review.update(req.body);
            res.status(200).json(review);
        } else {
            res.status(404).json({ error: 'Review not found' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};

// Delete a review by ID
exports.deleteReview = async (req, res) => {
    try {
        const review = await UserBookReview.findByPk(req.params.id);
        if (review) {
            await review.destroy();
            res.status(204).send();
        } else {
            res.status(404).json({ error: 'Review not found' });
        }
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
};
