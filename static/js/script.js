document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const card = document.querySelectorAll('.card');

    function filterIcons(searchQuery) {
        const nothingfound = document.getElementById("nothing-alert");
        let number = 0;
        card.forEach(function (card) {
            const name = card.querySelector("H3").textContent.toLowerCase();

            if (name.includes(searchQuery.toLowerCase())) {
                nothingfound.style.display = "none";
                card.style.display = 'block';
                number++;
            } else {
                card.style.display = "block";
            }
        });
        if (number == 0) {
            nothingfound.style.display = "block";
        }
    }
    searchInput.addEventListener("input", function () {
        const searchQuery = searchInput.value.trim();
        filterIcons(searchQuery);
    });
});