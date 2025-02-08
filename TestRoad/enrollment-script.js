document.addEventListener('DOMContentLoaded', function() {
    const courseName = localStorage.getItem('selectedCourse');
    document.getElementById('courseName').value = courseName;

    const form = document.getElementById('enrollmentForm');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const fullName = document.getElementById('fullName').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;
        const experience = document.getElementById('experience').value;

        const enrollmentData = {
            course: courseName,
            fullName: fullName,
            email: email,
            phone: phone,
            experience: experience
        };

        // You would typically send this to a backend server
        console.log('Enrollment Data:', enrollmentData);
        alert('Enrollment Successful! We will contact you soon.');
    });
});