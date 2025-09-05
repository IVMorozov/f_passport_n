$(document).ready(function() {
	var hoverTimeout;
	$('.part').hover(		
		function() {			
			$('.description').html($(this).attr('description-data'));
			// $('.description2').html($(this).attr('description-data2'));
			hoverTimeout = setTimeout(function() {
				$('.description').fadeIn();
				// $('.description2').fadeIn();
			}, 300);
		},
		function() {
			clearTimeout(hoverTimeout);
			$('.description').fadeOut(50);	
			// $('.description2').fadeOut(50);		
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
	console.log(KFD_data_mass_prepare)

	// for (let i = 1; i <= KFD_data_mass_prepare.length; i++) { 
	// 		KFD_data_mass[i].loc = KFD_data_mass_prepare[i].path_class
	// 		KFD_data_mass[i].mark = KFD_data_mass_prepare[i].avg_F
	// 		KFD_data_mass[i].color = ""		
	// 		console.log(KFD_data_mass[i].loc)
	// 	}  

	// let KFD_data_mass = [
	// 		{loc: 'part city Volgograd', mark: 50, color: "",},
	// 		{loc: 'Gorodishensky', mark: 5, color: "",},
	// 		{loc: 'Sredneakhtubinsky', mark: 45, color: "",},
	// 		{loc: 'Volzhsky', mark: 91, color: "",},
	// 		{loc: 'Leninsky', mark: 54, color: "",},
	// 		{loc: 'Frolovsky', mark: 57, color: "",},
	// 		{loc: 'Frolovo', mark: 85, color: "",},
	// 		{loc: 'Pallasovsky', mark: 61, color: "",},
	// 		{loc: 'Staropoltavsky', mark: 87, color: "",},
	// 		{loc: 'Nikolaevsky', mark: 74, color: "",},
	// 		{loc: 'Bykovsky', mark: 68, color: "",},
	// 		{loc: 'Svetloyarsky', mark: 78, color: "",},
	// 		{loc: 'Kalachevsky', mark: 54, color: "",},
	// 		{loc: 'Oktyabrsky', mark: 75, color: "",},
	// 		{loc: 'Kotelnikovsky', mark: 35, color: "",},
	// 		{loc: 'Chernishkovsky', mark: 47, color: "",},
	// 		{loc: 'Surovikinsky', mark: 85, color: "",},
	// 		{loc: 'Uryupinsky', mark: 45, color: "",},
	// 		{loc: 'Uruypinsk', mark: 76, color: "",},
	// 		{loc: 'Mihailovsky', mark: 53, color: "",},
	// 		{loc: 'Mihailovka', mark: 8, color: "",},
	// 		{loc: 'Kamishinsky', mark: 67, color: "",},
	// 		{loc: 'Kamishin', mark: 85, color: "",},
	// 		{loc: 'Khletsky', mark: 53, color: "",},
	// 		{loc: 'Ilovlinsky', mark: 81, color: "",},
	// 		{loc: 'Dubovsky', mark: 74, color: "",},
	// 		{loc: 'Olkhovsky', mark: 74, color: "",},
	// 		{loc: 'Kotovsky', mark: 74, color: "",},
	// 		{loc: 'Zhirnovsky', mark: 65, color: "",},
	// 		{loc: 'Ryudnyansky', mark: 95, color: "",},
	// 		{loc: 'Danilovsky', mark: 65, color: "",},
	// 		{loc: 'Elansky', mark: 85, color: "",},
	// 		{loc: 'Serafimovichsky', mark: 57, color: "",},
	// 		{loc: 'Kikvidzensky', mark: 98, color: "",},
	// 		{loc: 'Novonikolaevsky', mark: 54, color: "",},
	// 		{loc: 'Novoanninsky', mark: 45, color: "",},
	// 		{loc: 'Nehyaevsky', mark: 8, color: "",},
	// 		{loc: 'Alekseevsky', mark: 41, color: "",},
	// 		{loc: 'Kumilzhensky', mark: 50, color: "",},
	// 	]
		
	let but_1 = document.querySelector('.but_1'),
    	but_2 = document.querySelector('.but_2'),
    	but_3 = document.querySelector('.but_3'),
		but_4 = document.querySelector('.but_4'),
		but_5 = document.querySelector('.but_5');
	
	but_1.onclick = function() {
		for (let i = 0; i <= KFD_data_mass_prepare.length; i++) { 
			KFD_data_mass[i].loc = KFD_data_mass_prepare[i].path_class
			KFD_data_mass[i].mark = KFD_data_mass_prepare[i].avg_F
			KFD_data_mass[i].color = ""		
			console.log(KFD_data_mass[i].loc)
		} 




		$('.footer_').fadeOut();
		var paths = document.querySelectorAll("path"), i;
		for (i = 0; i < paths.length; i++) {			
			paths[i].setAttribute('style', 'fill:'+base_Color);
		}
		var paths = document.querySelectorAll(".city"), i;
		for (i = 0; i < paths.length; i++) {			
			paths[i].setAttribute('style', 'fill:'+base_City_Color);
		}
	}
	color = ''
	mark_loc=0
	but_2.onclick = function() {
		for (i = 0; i < KFD_data_mass.length; i++) { 
			for (j = 0; j < scale_KFD_mass.length; j++) {
				if (scale_KFD_mass[j].mark - KFD_data_mass[i].mark >=0 && scale_KFD_mass[j].mark - KFD_data_mass[i].mark < 10) {
					KFD_data_mass[i].color=scale_KFD_mass[j].color
				}
			}
		}		
    	var paths = document.querySelectorAll("path"), i;
		for (i = 0; i < paths.length; i++) {		
			className = paths[i].getAttribute("class");			
			for (j = 0; j < KFD_data_mass.length; j++) {				
				if (className.includes(KFD_data_mass[j].loc)) {
					mark_loc= KFD_data_mass[j].mark					
					paths[i].setAttribute('style', 'fill:'+KFD_data_mass[j].color);
				}
			}		    		
		}
		$('.footer_').fadeIn();				   	     
	}	
	
	const data = {
		labels: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль'],
		datasets: [
			{
				label: 'Продажи',
				data: [65, 59, 80, 81, 56, 55, 40],
				fill: false,
				borderColor: 'rgb(75, 192, 192)',
				tension: 0.1
			},
			{
				label: 'Посещения',
				data: [28, 48, 40, 19, 86, 27, 90],
				fill: false,
				borderColor: 'rgb(255, 99, 132)',
				tension: 0.1
			},
			{
				label: 'Регистрации',
				data: [12, 35, 22, 45, 30, 50, 60],
				fill: false,
				borderColor: 'rgb(54, 162, 235)',
				tension: 0.1
			}
		]
	};

	// Настройки графика
	const config = {
		type: 'line',
		data: data,
		options: {
			scales: {
				y: {
					beginAtZero: true
				}
			}
		}
	};

	// Создание графика
	const myChart = new Chart(
		document.getElementById('myChart'),
		config
	);

	const myChart1 = new Chart(
		document.getElementById('myChart1'),
		config
	);
	const myChart2 = new Chart(
		document.getElementById('myChart2'),
		config
	);
	
	console.log(KFD_data_mass);
}) // $(document).ready(function()
