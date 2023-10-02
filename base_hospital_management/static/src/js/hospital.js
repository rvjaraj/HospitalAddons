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

        var $starContainer = $("#star-rating");

        $starContainer.find(".fa-star-o").on("click", function () {
            $(this).removeClass("fa-star-o").addClass("fa-star");
            $(this).prevAll().removeClass("fa-star-o").addClass("fa-star");
            $(this).nextAll().removeClass("fa-star").addClass("fa-star-o");
            var rating = $(this).data("rating");
            $("#rating").val(rating);
        });
    });

});