$(document).ready(function() {
	$('#searchbutton').on('click',function(e){
		e.preventDefault();
		var input_string = $("#searchbarre").val();
		$.ajax({
  			url : "http://localhost:8080/api/"+input_string,
            type: "GET",
            success: function(data) {
            	console.log(data)
            	$('#retour').html(data);
            },
        });
        return false;
    });
});
