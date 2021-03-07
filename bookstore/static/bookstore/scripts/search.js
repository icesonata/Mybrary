document.addEventListener('DOMContentLoaded', () => {
    // Direct user to item info page
    document.querySelectorAll('.item').forEach(element => {
        element.onclick = () => {
            location.href = "/item/" + element.dataset.isbn;
        }
    });

    // Append query string to the URL before submitting
    document.querySelector(".search-bar").onsubmit = function() {
        var query = `?q=${this.querySelector('#query-string').value}`;
        var curURL = this.getAttribute('action');
        this.setAttribute('action', curURL + query);
    };
});
