document.addEventListener('DOMContentLoaded', () => {
    const selectedJob = JSON.parse(localStorage.getItem('selectedJob'));
    document.getElementById('job-title').textContent = selectedJob.title;
    const stepsList = document.getElementById('steps-list');

    selectedJob.steps.forEach((step, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = `<input type="checkbox" id="step${index}" onchange="markComplete(${index})"> ${step}`;
        stepsList.appendChild(listItem);
    });
});

function markComplete(index) {
    const checkbox = document.getElementById(`step${index}`);
    if (checkbox.checked) {
        checkbox.parentElement.style.textDecoration = "line-through";
    } else {
        checkbox.parentElement.style.textDecoration = "none";
    }
}

function goBack() {
    window.history.back();
}
