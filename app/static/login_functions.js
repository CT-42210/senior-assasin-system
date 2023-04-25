function sendData() {
	if (document.getElementById("username").value.length === 0 || document.getElementById("password").value.length === 0) {
		console.log("ERROR! no password or username");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/login_check",
        data: { username: $("#username").val(),
                password: $("#password").val() },
        success: function(response) {
        		console.log("Success username: " + response);
				window.location.href = "/";

        }
      });
		document.getElementById("username").value = "";
		document.getElementById("password").value = "";
	}

}