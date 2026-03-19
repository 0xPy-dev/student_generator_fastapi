document.getElementById("form").addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const data = Object.fromEntries(formData.entries());

    const mapped = {
        Marital_status: Number(data["Marital_status"]),
        Application_mode: Number(data["Application_mode"]),
        Application_order: Number(data["Application_order"]),
        Course: Number(data["Course"]),
        Daytime_evening_attendance: Number(data["Daytime_evening_attendance"]),
        Previous_qualification: Number(data["Previous_qualification"]),
        Admission_grade: Number(data["Admission_grade"]),
        Gender: Number(data["Gender"]),
        Age_at_enrollment: Number(data["Age_at_enrollment"]),
        Scholarship_holder: Number(data["Scholarship_holder"])
    };

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(mapped)
    })
    .then(res => res.json())
    .then(res => {
        document.getElementById("result").innerText =
            "Результат: " + res.prediction;
    });
});