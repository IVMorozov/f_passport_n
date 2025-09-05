$(document).ready(function() {
	$('.footer_').fadeOut();
	$('.footer__').fadeOut();
	var hoverTimeout;
	$('.part').hover(		
		function() {	
			var descriptionText = $(this).attr('description-data'); // Получаем текст
			var imageUrl = $(this).attr('description-data-img'); // Получаем путь к изображению
			$('.description').html('<p>' + descriptionText + '</p><img src="' + imageUrl + '" alt="Описание изображения">');
					
			

			hoverTimeout = setTimeout(function() {
				$('.description').fadeIn();
			}, 300);
		},
		function() {
			clearTimeout(hoverTimeout);
			$('.description').fadeOut(50);	
		},
	)
	base_Color = "#bf2523"
	base_City_Color = "#006400"
	color ="#8994f7"
	

	let scale_KFD_mass = [
			{Level: '00', color: "#ca2323ff", mark: 10,},
			{Level: '01', color: "#ec1008ff", mark: 20,},
			{Level: '02', color: "#e13500", mark: 30,},
			{Level: '03', color: "#eb5700", mark: 40,},
			{Level: '04', color: "#f39708", mark: 50,},
			{Level: '05', color: "#f2b10f", mark: 60,},
			{Level: '06', color: "#f3d317", mark: 70,},
			{Level: '07', color: "#c9dc26", mark: 80,},
			{Level: '08', color: "#90bd31", mark: 90,},
			{Level: '09', color: "#308a45", mark: 100,},		    
		]

	let scale_CHN_mass = [
			
			{Level: '00', color: "#f2b10f", mark: 20,},
			{Level: '01', color: "#f3d317", mark: 40,},
			{Level: '02', color: "#c9dc26", mark: 60,},
			{Level: '03', color: "#90bd31", mark: 80,},
			{Level: '04', color: "#308a45", mark: 100,},		    
		]
	
	
	// console.log(KFD_data_mass_prepare)

	let KFD_data_mass = [];
	let FG_data_mass = []; 
	let CHN_data_mass = []; 

	for (let i = 0; i < KFD_data_mass_prepare.length; i++) { 
			KFD_data_mass[i] = {}; // Инициализация объекта для каждого элемента
			KFD_data_mass[i].loc = KFD_data_mass_prepare[i].path_class;
			KFD_data_mass[i].mark = KFD_data_mass_prepare[i].avg_F;
			KFD_data_mass[i].color = "";
					
			FG_data_mass[i] = {}; // Инициализация объекта для каждого элемента
			FG_data_mass[i].loc = KFD_data_mass_prepare[i].path_class;
			FG_data_mass[i].mark = KFD_data_mass_prepare[i].avg_FG;
			FG_data_mass[i].color = "";	

			CHN_data_mass[i] = {}; // Инициализация объекта для каждого элемента
			CHN_data_mass[i].loc = KFD_data_mass_prepare[i].path_class;
			CHN_data_mass[i].mark = KFD_data_mass_prepare[i].avg_CHN;
			CHN_data_mass[i].color = "";	
		}  

	let but_1 = document.querySelector('.but_1'),
		but_2 = document.querySelector('.but_2'),
		but_3 = document.querySelector('.but_3'),
		but_4 = document.querySelector('.but_4'),
		but_5 = document.querySelector('.but_5');
	
	but_1.onclick = function() {
		$('.footer_').fadeOut(0);
		$('.footer__').fadeOut(0);
		var paths = document.querySelectorAll("path"), i;
		for (i = 0; i < paths.length; i++) {			
			paths[i].setAttribute('style', 'fill:'+base_Color);
		}
		var paths = document.querySelectorAll(".city"), i;
		for (i = 0; i < paths.length; i++) {			
			paths[i].setAttribute('style', 'fill:'+base_City_Color);
		}
	}
	// color = '';
	// mark_loc=0
	
	but_2.onclick = function() {
		
		$('.footer__').fadeOut(0);
		$('.footer_').fadeOut(0);
		for (i = 0; i < KFD_data_mass.length; i++) { 
			for (j = 0; j < scale_KFD_mass.length; j++) {
				if (scale_KFD_mass[j].mark - KFD_data_mass[i].mark >=0 && scale_KFD_mass[j].mark - KFD_data_mass[i].mark < 10) {
					KFD_data_mass[i].color=scale_KFD_mass[j].color;
				}
			}
		}		
    	var paths = document.querySelectorAll("path"), i;
		for (i = 0; i < paths.length; i++) {		
			className = paths[i].getAttribute("class");			
			for (j = 0; j < KFD_data_mass.length; j++) {				
				if (className.includes(KFD_data_mass[j].loc)) {
					mark_loc= KFD_data_mass[j].mark;					
					paths[i].setAttribute('style', 'fill:'+KFD_data_mass[j].color);
				}
			}		    		
		}
		$('.footer_').fadeIn();	
	}		
	
	but_3.onclick = function() {
		
		$('.footer__').fadeOut(0);
		$('.footer_').fadeOut(0);
		for (i = 0; i < FG_data_mass.length; i++) { 
			for (j = 0; j < scale_KFD_mass.length; j++) {
				if (scale_KFD_mass[j].mark - FG_data_mass[i].mark >=0 && scale_KFD_mass[j].mark - FG_data_mass[i].mark < 10) {
					FG_data_mass[i].color=scale_KFD_mass[j].color;
				}
			}
		}		
    	var paths = document.querySelectorAll("path"), i;
		for (i = 0; i < paths.length; i++) {		
			className = paths[i].getAttribute("class");			
			for (j = 0; j < FG_data_mass.length; j++) {				
				if (className.includes(FG_data_mass[j].loc)) {
					mark_loc= FG_data_mass[j].mark;					
					paths[i].setAttribute('style', 'fill:'+FG_data_mass[j].color);
				}
			}		    		
		}
		$('.footer_').fadeIn();	
	}

	but_4.onclick = function() {
		$('.footer_').fadeOut(0);
		$('.footer__').fadeOut(0);
		for (i = 0; i < CHN_data_mass.length; i++) { 
			for (j = 0; j < scale_CHN_mass.length; j++) {
				if (scale_CHN_mass[j].mark - CHN_data_mass[i].mark >=0 && scale_CHN_mass[j].mark - CHN_data_mass[i].mark < 20) {
					CHN_data_mass[i].color = scale_CHN_mass[j].color;
				}	
				if (CHN_data_mass[i].mark >= 100) {
					CHN_data_mass[i].color = scale_CHN_mass[4].color;
					CHN_data_mass[i].color = "#09f13fff";
				}
			}
		}		
    	var paths = document.querySelectorAll("path"), i;
		for (i = 0; i < paths.length; i++) {		
			className = paths[i].getAttribute("class");			
			for (j = 0; j < CHN_data_mass.length; j++) {				
				if (className.includes(CHN_data_mass[j].loc)) {
					mark_loc= CHN_data_mass[j].mark;					
					paths[i].setAttribute('style', 'fill:'+CHN_data_mass[j].color);
				}
			}		    		
		}
		$('.footer__').fadeIn();	
	}

	but_5.onclick = function() {
		window.location.href = "regionreport";
			
	}

}) // $(document).ready(function()

document.addEventListener('DOMContentLoaded', function() {

    // Функция для получения CSRF токена из cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');




    const toastElList = document.querySelectorAll(".toast");
    const toastList = [...toastElList].map((toastEl) => {
        const toast = new bootstrap.Toast(toastEl, {
            delay: 5000, // 5 секунд
        });
        toast.show();
        return toast;
    });
});


