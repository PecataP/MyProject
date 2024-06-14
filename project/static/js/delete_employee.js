document.getElementById('deleteForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission behavior

    var idValue = document.getElementById('id').value;
    window.location.href = '/delete_employee/' + encodeURIComponent(idValue); // Redirect to the constructed URL
});