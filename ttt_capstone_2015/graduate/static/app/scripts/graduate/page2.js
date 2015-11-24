$().ready(function() {
	
$('#id_employment_address_outside_us').change(function () {
		if ($(this).is(':checked')) {
			$('#employer_outside_us').show();
			$('#employer_inside_us').hide();
			$('#id_employment_city').val('');
			$('#id_employment_state').val('');
			$('#id_employment_zip').val('');
		} else {
			$('#employer_outside_us').hide();
			$('#employer_inside_us').show();
			//$('#address3').val('');
			$('#country').val('');
		}
	});
  
    
    $("input[name='legal']").change(function(){
		if ($("input[name='legal']:checked").val() == '1') {
            $('#legal-reason').show();
        } else {
        	$('#legal-reason').hide();
        }
    });
    
    $("input[name='policy']").change(function () {
        if ($("input[name='policy']:checked").val() == '1') {
            $('#policy-reason').show();
        } else {
        	$('#policy-reason').hide();
        }
    });

});