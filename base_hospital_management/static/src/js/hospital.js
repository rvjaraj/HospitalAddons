/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';

publicWidget.registry.DoctorKanban = publicWidget.Widget.extend({
    selector: '#main_template_create, #main_template_show',

    events: {
        'click .star-rating .fa-star-o': '_oneClickCheckBox',
        'click .toggle-create-link': '_oneClickCreateLink',
        'click .toggle-comments-link': '_oneClickCommentsLink',
    },

    init(parent, options) {
        this._super(...arguments);
        console.log('init')
    },

    start() {
        const res = this._super(...arguments);
        this.checkbox = this.el.querySelector('#exampleCheck1');
        return res;
    },

    _oneClickCheckBox(ev) {
        const star = ev.currentTarget;
        const starContainer = star.closest(".star-rating");

        Array.from(starContainer.children).forEach((child) => {
            if (child.dataset.rating <= star.dataset.rating) {
                child.classList.remove("fa-star-o");
                child.classList.add("fa-star");
            } else {
                child.classList.remove("fa-star");
                child.classList.add("fa-star-o");
            }
        });

        const rating = star.dataset.rating;
        starContainer.querySelector(".rating").value = rating;
    },

    _oneClickCreateLink(ev) {
        ev.preventDefault();
        const commentForm = ev.currentTarget.closest('.list-group-item').querySelector('.comments-form');
        if (commentForm) {
            commentForm.style.display = commentForm.style.display === 'none' ? 'block' : 'none';
        }
    },

    _oneClickCommentsLink(ev) {
        ev.preventDefault();
        const commentsContainer = ev.currentTarget.closest('.list-group-item').querySelector('.comments-container');
        if (commentsContainer) {
            commentsContainer.style.display = commentsContainer.style.display === 'none' ? 'block' : 'none';
        }
    },
});

export default publicWidget.registry.DoctorKanban;
