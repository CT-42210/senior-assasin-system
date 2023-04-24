function sendData() {
	if (document.getElementById("username").value.length == 0 || document.getElementById("password").value.length == 0) {
		console.log("ERROR! no password or username");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/signup_check",
        data: { username: $("#username").val(),
                email: $("#email").val(),
                password: $("#password").val() },
        success: function(response) {
        		console.log("Submitted to python response: " + response);
        }
      });
		document.getElementById("username").value = "";
		document.getElementById("password").value = "";
		document.getElementById("email").value = "";
	}

}