etp0 = [
    '<h1>Bienvenido al Capturador de Imagenes de Rostro del Sistema STARF</h1>',
    '<h2>A continuacion se tomaran fotos de su rostro para poder reconocerlo al ingresar a sus clases en las aulas que dependan del Departamento de Sistemas de la UTN-FRT y poder realizar su control de presentismo en estas clases.</h2>',
    '<h2>Le solicitamos que por favor siga las instrucciones en pantalla a fin de poder garantizar la mejor calidad de las imagenes obtenidas de su rostro para su reconocimiento</h2>',
    '<h2>Haga click en "Comenzar" para empezar con el procedimiento para la toma de todas las imagenes.</h2>',
    '<h2>Haga click en "Reemplazar una imagen determinada" para reemplazar una imagen considerada no apta para el reconocimiento facial.</h2>',
    '<h2>Haga haga click en "Volver" para salir.</h2>',
    '<button id="btnComenzar">Comenzar</button><button id="btnReemplazar">Reemplazar una imagen determinada</button><button id="btnVolver">Volver</button>'
]

etp1 = [
	'<h1>Instrucciones durante el proceso</h1>',
	'<h2>Para lograr el reconocimiento facial durante su asistencia a clases, se tomaran 20 fotos de su rostro en diferentes angulos del mismo y diferentes expresiones faciales</h2>',
	'<h2>Durante cada foto se le dara instrucciones a que punto de la pantalla (representado por un circulo verde como el que aparece abajo) debe mirar fijamente.</h2>',
	'<div id=circle></div>',
	'<h2>Al fijar su mirada al punto de interes de la pantalla, hagalo no solamente moviendo sus ojos hacia el punto de interes, sino también su cabeza</h2>',
	'<h2>Al lado de dicho punto se le indicara que expresion facial realizará. También encontrara un botón "Tomar foto" que activara un timer de 3 segundos antes de obtener la imagen.</h2>',
	'<button id="btnComenzar">Comenzar</button><button id="btnVolver">Volver</button>'
]

etp2 = [
	'<h1 class="foto-title">Foto 1</h1>',
	'<div class="move"><div id=circle></div></div>',
]

function runPictureCapture(){
    $('#modal').fadeIn();
    runScreen(0);
}

function runScreen(screen){
	drawScreen(this['etp'+screen])
	eventosCapturador(screen)
}

function drawScreen(elements){
	clear($('#modal'))
	for(i in elements){
		if(i>0) $('#modal').append('<br/>')
		$('#modal').append(elements[i]);
	}
}


function eventosCapturador(screen){
	switch(screen){
		case 0: $('#btnVolver').click(function(){$('#modal').fadeOut()});
				$('#btnComenzar').click(function(){runScreen(1)});break;
		case 1: $('#btnVolver').click(function(){runScreen(0)});
				$('#btnComenzar').click(function(){runScreen(2)});break;
				$('#circle').css({'animation-name':'pic1','animation-duration':'2s'})
	}
	
}
