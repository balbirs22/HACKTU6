function selectCourse(courseName) {
    localStorage.setItem('selectedCourse', courseName);
    window.location.href = 'enrollment.html';
}