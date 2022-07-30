function previewUpdates() {
    var in_fname = document.getElementById("fname").value;
    document.getElementById("pre_fname").innerHTML = in_fname
    
    var in_lname = document.getElementById("lname").value;
    document.getElementById("pre_lname").innerHTML = in_lname

    var in_event = document.getElementById("event").value;
    document.getElementById("pre_event").innerHTML = in_event
    
    var in_date = document.getElementById("date").value;
    document.getElementById("pre_date").innerHTML = in_date

    var in_hours = document.getElementById("hours").value;
    document.getElementById("pre_hours").innerHTML = in_hours
}