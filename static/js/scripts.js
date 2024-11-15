console.log("scripts.js loaded");
const loginForm = document.getElementById('login-form');

if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Get form values
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        // Basic validation
        if (username === '' || password === '') {
            alert('Please enter both username and password.');
            return;
        }

        // Make POST request to backend login API
        const formData = new FormData();
        formData.append('username', username);
        formData.append('password', password);

        fetch('/login', {
            method: 'POST',
            body: formData,  // Send as form data
        })
            .then(response => response.text())  // Expecting HTML response
            .then(data => {
                if (data.includes('Invalid credentials')) {
                    alert('Invalid credentials');
                } else {
                    alert('Login successful!');
                    window.location.href = '/dashboard';  // Redirect to dashboard
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error logging in.');
            });
    });
}
