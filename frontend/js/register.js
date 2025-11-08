document.getElementById('registerForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email = document.getElementById('email').value;
    const nama = document.getElementById('nama').value;
    const alertContainer = document.getElementById('alertContainer');
    
    // Basic validation
    if (!validateEmail(email)) {
        alertContainer.innerHTML = `
            <div class="alert alert-danger">
                Please enter a valid email address.
            </div>
        `;
        return;
    }
    
    if (password.length < 6) {
        alertContainer.innerHTML = `
            <div class="alert alert-danger">
                Password must be at least 6 characters long.
            </div>
        `;
        return;
    }
    
    try {
        const response = await fetch('http://localhost:5000/api/users/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password, email, nama })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            alertContainer.innerHTML = `
                <div class="alert alert-success">
                    Registration successful! Redirecting to login...
                </div>
            `;
            setTimeout(() => {
                window.location.href = 'login.html';
            }, 2000);
        } else {
            alertContainer.innerHTML = `
                <div class="alert alert-danger">
                    ${data.errors ? data.errors.join('<br>') : 'Registration failed. Please try again.'}
                </div>
            `;
        }
    } catch (error) {
        alertContainer.innerHTML = `
            <div class="alert alert-danger">
                An error occurred. Please try again.
            </div>
        `;
    }
});

function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}