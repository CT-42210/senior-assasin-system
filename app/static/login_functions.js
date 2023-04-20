function sendData() {
	if (document.getElementById("username").value.length == 0) {
		console.log("No username!");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/login_check",
        data: { text: $("#username").val() },
        success: function(response) {
        		console.log("submitting to python snake");
        }
      });
		console.log("submitting to python");
		document.getElementById("username").value = "";
	}

}