(function ($) {
    // Fix the menu behaviour in the menubar
    $(document).on('click', function(e){
	if($(e.target).is($('#grp-navigation > #grp-user-tools > li.grp-user-options-container > a'))){
	    var pl = $(e.target).parent();
	    pl.siblings().removeClass('grp-open').addClass('grp-closed');
	}else{
	    $('#grp-navigation > #grp-user-tools > li.grp-user-options-container').removeClass('grp-open').addClass('grp-closed');
	}
    });

}(django.jQuery)); // Reuse django injected jQuery library
