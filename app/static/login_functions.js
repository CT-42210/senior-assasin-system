function sendData() {
	if (document.getElementById("move_data").value.length == 0) {
		console.log("No moves to send!");
		return;
	} else {
	      $.ajax({
        type: "POST",
        url: "/update_board",
        data: { text: $("#move_data").val() },
        success: function(response) {
        		console.log("submitting to python snake");
        		 $("#silentDiv").html(response)
        		 init();
        }
      });
		console.log("submitting to python");
		document.getElementById("move_data").value = "";
	}

}