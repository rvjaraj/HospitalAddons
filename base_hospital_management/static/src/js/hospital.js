odoo.define('base_hospital_management.hospital', function (require) {
    "use strict";
    $(document).ready(function () {

        var toggleCommentsLink = document.querySelector(".toggle-comments-link");
        var commentsContainer = document.querySelector(".comments-container");

        toggleCommentsLink.addEventListener("click", function (event) {
            event.preventDefault();
            if (commentsContainer.style.display === "none") {
                commentsContainer.style.display = "";
            } else {
                commentsContainer.style.display = "none"; // Corregido "noe" a "none"
            }
        });
        console.log(toggleCommentsLink);
    });
});
