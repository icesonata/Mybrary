document.addEventListener('DOMContentLoaded', () => {
    document.querySelector("a[class='nav']").onclick = function() {
        window.history.back();
        return false;
    };

    document.querySelector("form-comment").onsubmit = function() {
        this.querySelector("#input-username").disable = "false";
        
        return false;
    };
});