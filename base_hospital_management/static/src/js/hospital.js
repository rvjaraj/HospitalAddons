odoo.define('base_hospital_management.doctor_kanban', function (require) {
    "use strict";


    $(function () {
        $(".toggle-create-link").on("click", function (event) {
            var $this = $(this);
            event.preventDefault();
            var $commentForm = $(this).closest('.list-group-item').find('.comments-form');
            $commentForm.toggle();
        });
        $(".toggle-comments-link").on('click', function (event) {
            var $this = $(this);
            event.preventDefault();
            var $commentsContainer = $(this).closest('.list-group-item').find('.comments-container');
            $commentsContainer.toggle();
        });

        $(".star-rating .fa-star-o").on("click", function () {
            var $star = $(this);
            var $starContainer = $star.closest(".star-rating");

            $star.removeClass("fa-star-o").addClass("fa-star");
            $star.prevAll().removeClass("fa-star-o").addClass("fa-star");
            $star.nextAll().removeClass("fa-star").addClass("fa-star-o");

            var rating = $star.data("rating");
            console.log(rating);
            debugger;
            $starContainer.find(".rating").val(rating);
        });

    });

});