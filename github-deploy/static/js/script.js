// LOGIN PAGE SCRIPT
document.addEventListener('DOMContentLoaded', function() {
  const loginBtn = document.getElementById('loginBtn');
  const guestLogin = document.getElementById('guestLogin');
  
  if (loginBtn) {
    loginBtn.addEventListener('click', function () {
      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value.trim();

      if (username === '' || password === '') {
        alert('Please fill out both fields.');
      } else {
        localStorage.setItem('loggedIn', 'true');
        window.location.href = '/'; // Redirect to Flask home
      }
    });
  }

  if (guestLogin) {
    guestLogin.addEventListener('click', function (e) {
      e.preventDefault();
      localStorage.setItem('loggedIn', 'true');
      window.location.href = '/'; // Redirect to Flask home
    });
  }

  // Filter banks by type
  const bankTypeSelect = document.getElementById('bank-type-select');
  if (bankTypeSelect) {
    bankTypeSelect.addEventListener('change', function() {
      const selectedType = this.value;
      const rows = document.querySelectorAll('#banks-table tbody tr');
      
      rows.forEach(row => {
        const bankType = row.cells[1].textContent.trim();
        if (selectedType === 'all' || bankType === selectedType) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  }

  // Logout functionality
  const logoutBtn = document.getElementById('logoutBtn');
  if (logoutBtn) {
    logoutBtn.addEventListener('click', () => {
      localStorage.removeItem('loggedIn');
      window.location.href = '/login';
    });
  }
});
