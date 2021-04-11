$(function() {
	var $BALLOON = $('<div class="balloon-wrapper">'+
		'<div class="balloon"></div>'+
	'</div>');


	var $SPLASH = $('<div class="splash"></div>');


	function spawnBallon() {
		var $balloon = $BALLOON.clone();

		$balloon.css({
			left: (5 + Math.random()*90 + '%'),
		});

		var radius = (Math.random()*20 + 20);

		$balloon.children().css({
			width: radius,
			height: (radius + Math.random()*10),
		})
		.addClass('balloon'  + Math.ceil(Math.random()*7))
		.click(function(event) {

			var offset = $(this).offset();

			spawnSplash($(this).css('width'), $(this).css('height'), offset.left, offset.top);

			$balloon.remove();
		});


		$('body').append($balloon);

		// after 30s remove ballon
		setTimeout((function() {
			if ($balloon)
				$balloon.remove();
		}), 30*1000);
	};

	function spawnSplash(width, height, left, top) {
		var $splash = $SPLASH.clone();

		$splash.css({
			width: width,
			height: height,
			left : (left + 'px'),
			top : (top + 'px'),
		}).delay(1000).queue(function(next) {
			$splash.remove();
			next();
		});

		$('body').append($splash);
	}

	spawnBallon();


	var start = Date.now();

	function update() {
		var now = Date.now();
		if ((now - start)/1000 > 5){
			start = now;

			spawnBallon();
		}

		window.requestAnimationFrame(update);
	}

	window.requestAnimationFrame(update);


	if (window.localStorage) {
		var birthday = window.localStorage.getItem('birthday') || '{}';
		
		var today = new Date();
		birthday = JSON.parse(birthday);

		if (!birthday || !birthday.wished || birthday.lastWished < today.getFullYear()) {

			var $birthDayModal = $("#birthDayModal");
			$birthDayModal.modal('show').delay(500).queue(function(next) {

				var $modalBody = $("#birthDayModal .modal-body");
				var offset = $modalBody.offset();
				var width = $modalBody.width();
				var height = $modalBody.height();

				var i = 0;

				for (var i = 0; i < 30; i++) {
					setTimeout(function() {
						if ($birthDayModal.hasClass('in')) {
							spawnSplash(20, 20, offset.left + Math.random() * width, offset.top + Math.random() * height);
						}
					}, i*500 + Math.random() * 300 + 1000);					
				}

				next();
			});


			birthday = {
				wished : true,
				lastWished : today.getFullYear()
			}

			window.localStorage.setItem('birthday', JSON.stringify(birthday));
		}
	}
});