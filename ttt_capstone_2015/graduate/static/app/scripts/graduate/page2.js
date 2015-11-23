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