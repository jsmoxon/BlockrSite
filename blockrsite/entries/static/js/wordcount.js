$(document).ready(function() {

	$('.word_count').each(function() {
		var input = '#' + this.id;
		var count = input + '_count';
		$(count).show();
		word_count(input, count);
		$(this).keyup(function() { word_count(input, count) });
	    });

    });

function word_count(field, count) {

    var number = 0;
    var matches = $(field).val().match(/\b/g);
    if(matches) {
        number = matches.length/2;
    }
    $(count).text( number + ' word' + (number != 1 ? 's' : '') + ' approx');

}