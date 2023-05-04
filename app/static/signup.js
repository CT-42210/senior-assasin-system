function sendData() {

    var csrf_token = document.getElementById("csrf_tokenS").value

	if (document.getElementById("username_input").value.length === 0 ||
        document.getElementById("password_input").value.length === 0 ||
        document.getElementById("email_input").value.length === 0) {
		console.log("ERROR! no password or username or email");
		return;
	} else {
            $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
            }
        });
	      $.ajax({
        type: "POST",
        url: "/signup",
        data: { username: $("#username_input").val(),
                email: $("#email_input").val(),
                password: $("#password_input").val() },
        success: function(response) {
        		console.log("Submitted to python response: " + response);
        		  if (response == "False") {
                    $('.alert').remove(); // remove any existing alerts
                    $('body').prepend('<div class="alert alert-dismissible alert-danger fade show" role="alert">' +
                        '<strong>Oh snap!</strong> ' + "Credential Error!" +
                        '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>');
                } else {
                    window.location.href = "/";
                }
        }
      });
		document.getElementById("username_input").value = "";
		document.getElementById("password_input").value = "";
		document.getElementById("email_input").value = "";
	}

}