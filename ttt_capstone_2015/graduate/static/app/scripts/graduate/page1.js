$().ready(function() {
	$('#email').change(function() { 
		$.ajax({
			type: 'POST',
			dataType: 'json',
			url: $('#baseUrl').val()+'/graduate/send-application-password/email/'+$(this).val(),
			success: function(json) {
				if (json['result'] == 'success') {
					$('#email-notice').html(json['msg']);
				} else {
					$('#email-notice').html(json['errors']);
				}
			}
		});
	});
	
	$('.birthdatepicker').datepicker({
		minDate: new Date(1900,1-1,1), maxDate: '-10Y',
		dateFormat: 'mm/dd/yy',
	    changeMonth: true,
	    changeYear: true,
	    yearRange: '-100:-10'
	});
	
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
	
	$('#phone_outside_us').change(function() {
		if ($(this).is(':checked')) {
			$('.non_us_number').show();
			$('.us_number').hide();
		} else {
			$('.non_us_number').hide();
			$('.us_number').show();
		}
	});
	
	$("select[name='id_is_citizen']").change(function () {
		if ($(this).val() == 'yes') {
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