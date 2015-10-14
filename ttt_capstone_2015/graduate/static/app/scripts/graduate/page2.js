$().ready(function() {
	
	$('#add_CEEB_2').bind('click', function(){
        $('#add_CEEB_3').show();
        $('#attendedCollege_div2').show();
        $(this).hide();
    });//end bind

    $('#add_CEEB_3').bind('click', function(){
        $('#add_CEEB_4').show();
        $('#attendedCollege_div3').show();
        $(this).hide();
    });//end bind

    $('#add_CEEB_4').bind('click', function(){
        $('#add_CEEB_5').show();
        $('#attendedCollege_div4').show();
        $(this).hide();
    });//end bind

    $('#add_CEEB_5').bind('click', function(){
        $('#attendedCollege_div5').show();
        $(this).hide();
    });
    
    $('.international-ceeb-college').click(function() {
    	$('#'+$(this).parent().parent().parent().parent().attr('id')+' .college-ceeb').val('0002');
    });
    
    $("input[name='has_legal_issue']").change(function(){
		if ($("input[name='has_legal_issue']:checked").val() == '1') {
            $('#legal-reason').show();
        } else {
        	$('#legal-reason').hide();
        }
    });
    
    $("input[name='has_policy_issue']").change(function(){
		if ($("input[name='has_policy_issue']:checked").val() == '1') {
            $('#policy-reason').show();
        } else {
        	$('#policy-reason').hide();
        }
    });

});