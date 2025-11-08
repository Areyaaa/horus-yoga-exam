// Check if user is logged in
const token = localStorage.getItem('token');
const currentUser = JSON.parse(localStorage.getItem('user'));

if (!token || !currentUser) {
    window.location.href = 'login.html';
}

// Get user ID from URL
const urlParams = new URLSearchParams(window.location.search);
const userId = urlParams.get('id');

if (!userId) {
    window.location.href = 'dashboard.html';
}

// Load user data
async function loadUserData() {
    try {
        const response = await fetch(`http://localhost:5000/api/users/${userId}`, {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.ok) {
            const user = await response.json();
            document.getElementById('username').value = user.username;
            document.getElementById('email').value = user.email;
            document.getElementById('nama').value = user.nama;
        } else {
            alert('Failed to load user data');
            window.location.href = 'dashboard.html';
        }
    } catch (error) {
        console.error('Error loading user data:', error);
        alert('An error occurred while loading user data');
        window.location.href = 'dashboard.html';
    }
}

// Handle form submission
document.getElementById('updateForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const nama = document.getElementById('nama').value;
    const password = document.getElementById('password').value;
    const alertContainer = document.getElementById('alertContainer');
    
    const userData = {
        username,
        email,
        nama
    };
    
    if (password) {
        userData.password = password;
    }
    
    try {
        const response = await fetch(`http://localhost:5000/api/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify(userData)
        });
        
        const data = await response.json();
        
        if (response.ok) {
            alertContainer.innerHTML = `
                <div class="alert alert-success">
                    User updated successfully! Redirecting...
                </div>
            `;
            
            // If current user is updating their own data, update localStorage
            if (parseInt(userId) === currentUser.id) {
                localStorage.setItem('user', JSON.stringify(data));
            }
            
            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 2000);
        } else {
            alertContainer.innerHTML = `
                <div class="alert alert-danger">
                    ${data.errors ? data.errors.join('<br>') : 'Update failed. Please try again.'}
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

// Load user data when page loads
loadUserData();