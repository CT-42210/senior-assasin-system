function sendData_basic() {
	if (document.getElementById("username").value.length === 0 ||
        document.getElementById("password1").value.length === 0 ||
        document.getElementById("team_name").value.length === 0 ||
        document.getElementById("user_address").value.length === 0) {
		console.log("ERROR! missing_data");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/settings",
        data: { username: $("#username").val(),
                password1: $("#password1").val(),
                team_name: $("#team_name").val(),
                user_address: $("#user_address").val(),
                password2: $("#password2").val() },
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
		document.getElementById("username").value = "";
		document.getElementById("password1").value = "";
		document.getElementById("password2").value = "";
        document.getElementById("team_name").value = "";
        document.getElementById("user_address").value = "";

	}

}

function sendData_admin() {
	if (document.getElementById("username").value.length === 0 ||
        document.getElementById("password1").value.length === 0 ||
        document.getElementById("team_name").value.length === 0 ||
        document.getElementById("user_address").value.length === 0) {
		console.log("ERROR! missing_data");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/settings",
        data: { username: $("#username").val(),
                password1: $("#password1").val(),
                team_name: $("#team_name").val(),
                user_address: $("#user_address").val(),
                password2: $("#password2").val() },
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
		document.getElementById("username").value = "";
		document.getElementById("password1").value = "";
		document.getElementById("password2").value = "";
        document.getElementById("team_name").value = "";
        document.getElementById("user_address").value = "";

	}

}