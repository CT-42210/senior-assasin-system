function sendData() {
	if (document.getElementById("username_input").value.length === 0 ||
        document.getElementById("password_input").value.length === 0) {
		console.log("ERROR! no password or username");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/login",
        data: { username: $("#username_input").val(),
                password: $("#password_input").val() },
        success: function(response) {
        		console.log("Success username: " + response);
        		if (response == "False") {
                    $('.alert').remove(); // remove any existing alerts
                    $('body').prepend('<div class="alert alert-dismissible alert-danger fade show" role="alert">' +
                        '<strong>Oh snap!</strong> ' + "Incorrect username or password" +
                        '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');
                } else {
                    window.location.href = "/";
                }
//				window.location.href = "/";

        }
      });
		document.getElementById("username_input").value = "";
		document.getElementById("password_input").value = "";
	}

}