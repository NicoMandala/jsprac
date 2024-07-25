const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const userBookReviewController = require('../controllers/userBookReviewController');

console.log('User controller imported:', userController);

router.post('/users', userController.createUser);
router.get('/users', userController.getAllUsers);
router.get('/users/:id', userController.getUserById);
router.put('/users/:id', userController.updateUser);
router.delete('/users/:id', userController.deleteUser);




router.post('/reviews', userBookReviewController.createReview);
router.get('/reviews', userBookReviewController.getAllReviews);
// router.get('/:id', userBookReviewController.getUserById);
// router.put('/:id', userBookReviewController.updateReview);
// router.delete('/:id', userBookReviewController.deleteReview);



module.exports = router;
