$("#form-predict").submit(function(e) {

    var url = "/api/v1.0/predict"; // the script where you handle the form input.
    var data = $("#form-predict").serialize()
    $.ajax({
           type: "POST",
           url: url,
           data: data, // serializes the form's elements.
           success: function(data)
           {
               //alert(data.response.survive); // show response from the php script.
               if (data.response.survive === 1) {
               		$('#alive').modal('show');
               		$('.percentage_alive').html(data.response.percentage_alive);   
               		$('.percentage_dead').html(data.response.percentage_dead);   
               } else {
               		$('#dead').modal('show');   
               		$('.percentage_alive').html(data.response.percentage_alive);   
               		$('.percentage_dead').html(data.response.percentage_dead);   
               }
           },
           error: function (request, status, error) {
               alert(request.responseText);
           }
          });

    e.preventDefault(); // avoid to execute the actual submit of the form.
});