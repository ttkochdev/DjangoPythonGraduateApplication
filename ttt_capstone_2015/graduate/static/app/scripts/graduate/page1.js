$(document).ready(function () {
    console.log("started p1 js");
    /*$('#baseUrl').val()+*/
	$('#email').change(function() { 
		$.ajax({
			type: 'GET',
			dataType: 'json',
			url: '/pwemail/?email='+$(this).val(),
			success: function (json) {
			    console.log("here");
				if (json['result'] == 'success') {
				    /*$('#email-notice').html(json['msg']);*/
				    console.log("sucess")
				} else {
				    console.log("fail")
					/*$('#email-notice').html(json['errors']);*/
				}
			}
		});
	});
	console.log("after email change");
	$('.birthdatepicker').datepicker();

    
	console.log("after datepicker");
	$('#id_internationalcheck').change(function () {
		if ($(this).is(':checked')) {
			$('#outside_us').show();
			$('#inside_us').hide();
			$('#city').val('');
			$('#state').val('');
			$('#zip').val('');
		} else {
			$('#outside_us').hide();
			$('#inside_us').show();
			$('#address3').val('');
			$('#country').val('');
		}
	});
	
	$("#id_international_phonecheck").change(function () {	    
		if ($(this).is(':checked')) {
			$('.non_us_number').show();
			$('.us_number').hide();
		} else {
			$('.non_us_number').hide();
			$('.us_number').show();
		}
	});
	
	$("#id_is_citizen").change(function () {
	    console.log("is citiz");
	    if ($(this).val() == 'yes') {
	        console.log("yes yes yes");
			$('#citizen_yes').show();
			$('#citizen_legal_resident').hide();
			$('#citizen_alien').hide();
			$('#citizen_no').hide();
			
			$('#citizenship_country').val('');
			$('#residence_country').val('');
			$('#alien_reg_no').val('');
			$('#is_international_student').val('');
			$('#alien_status').val('');
			
		} else if ($(this).val() == 'legal') {
			$('#citizen_yes').show();
			$('#citizen_legal_resident').show();
			$('#citizen_alien').show();
			$('#citizen_no').hide();
			
			$('#is_international_student').val('');
			$('#alien_status').val('');
			
		} else if ($(this).val() == 'no') {
			$('#citizen_yes').hide();
			$('#citizen_alien').hide();
			$('#citizen_legal_resident').show();
			$('#citizen_no').show();
			
			$('#ssn').val('');
			$('#alien_reg_no').val('');
			
		} else {
			$('#citizen_yes').hide();
			$('#citizen_alien').hide();
			$('#citizen_legal_resident').hide();
			$('#citizen_no').hide();
			
			$('#ssn').val('');
			$('#citizenship_country').val('');
			$('#residence_country').val('');
			$('#alien_reg_no').val('');
			$('#is_international_student').val('');
			$('#alien_status').val('');
		}
	});
	
	$('.race-popover').popover({trigger:'click'});
});