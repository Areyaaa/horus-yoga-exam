// Check if user is logged in
const token = localStorage.getItem('token');
const user = JSON.parse(localStorage.getItem('user'));

if (!token || !user) {
    window.location.href = 'login.html';
}

// Set user info in navbar
document.getElementById('userInfo').textContent = `Welcome, ${user.nama}`;

// Logout functionality
document.getElementById('logoutBtn').addEventListener('click', () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    window.location.href = 'login.html';
});

// Load users
async function loadUsers() {
    try {
        const response = await fetch('http://localhost:5000/api/users', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.status === 401) {
            // Token expired or invalid
            localStorage.removeItem('token');
            localStorage.removeItem('user');
            window.location.href = 'login.html';
            return;
        }
        
        const users = await response.json();
        displayUsers(users);
    } catch (error) {
        console.error('Error loading users:', error);
    }
}

// Display users in table
function displayUsers(users) {
    const tbody = document.getElementById('usersTableBody');
    tbody.innerHTML = '';
    
    users.forEach(user => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${user.id}</td>
            <td>${user.username}</td>
            <td>${user.nama}</td>
            <td>${user.email}</td>
            <td>
                <button onclick="updateUser(${user.id})" class="btn btn-primary" style="margin-right: 5px;">Update</button>
                <button onclick="deleteUser(${user.id})" class="btn btn-danger">Delete</button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

// Search functionality
document.getElementById('searchInput').addEventListener('input', (e) => {
    const searchTerm = e.target.value.toLowerCase();
    const rows = document.getElementById('usersTableBody').getElementsByTagName('tr');
    
    Array.from(rows).forEach(row => {
        const username = row.cells[1].textContent.toLowerCase();
        const name = row.cells[2].textContent.toLowerCase();
        
        if (username.includes(searchTerm) || name.includes(searchTerm)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});

// Update user
function updateUser(id) {
    window.location.href = `update.html?id=${id}`;
}

// Delete user
async function deleteUser(id) {
    if (!confirm('Are you sure you want to delete this user?')) {
        return;
    }
    
    try {
        const response = await fetch(`http://localhost:5000/api/users/${id}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.ok) {
            alert('User deleted successfully');
            loadUsers();
        } else {
            const data = await response.json();
            alert(data.message || 'Failed to delete user');
        }
    } catch (error) {
        console.error('Error deleting user:', error);
        alert('An error occurred while deleting the user');
    }
}

// Load users when page loads
loadUsers();