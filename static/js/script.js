$(function() {
	$(".button").each(function(index) {
		$(this).click(function() {
			$.getJSON('/commands/' + this.id, function(data) {
				//do something
			});
			return false;
		});									
	});
	$("#preset").change(function() {
		$.getJSON('/commands/' + $(this).val(), function(data) {
			//do  something
		});
		setTimeout(function() {$('#preset').val('Select...');},1000);
		return false;
	});
});