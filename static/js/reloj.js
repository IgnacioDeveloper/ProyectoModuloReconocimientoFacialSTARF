var lblReloj,serverTime;
(function(){
	iniciarReloj();
})();

function iniciarReloj(){
setTimeout(function(){obtenerHoraServidor();},5);
}

function ejecutarReloj(resultado){
	//Fri, 07 Apr 2017 16:53:14 Formato Resultado;
	//April 07, 2017 17:32:42 Formato JS;
	serverTime = new Date(resultado);
	setInterval(function(){
		serverTime.setMilliseconds(serverTime.getMilliseconds()+1000);
		mostrarHora(serverTime);
	}, 1000);
}

function traductorMes(mes){
	switch(mes){
		case "Jan":return "January";
		case "Feb":return "Febraury";
		case "Mar":return "March";
		case "Apr":return "April";
		case "May":return "May";
		case "Jun":return "June";
		case "Jul":return "Jule";
		case "Aug":return "August";
		case "Sep":return "September";
		case "Oct":return "October";
		case "Nov":return "November";
		case "Dec":return "December";
		default:return "undefined";
	}
}

function mostrarHora(serverTime){
	$('#lblReloj').html("Fecha y Hora del Servidor: "+serverTime.getDate()+"/"+(serverTime.getMonth()+1)+"/"+serverTime.getFullYear()+" "+serverTime.getHours()+":"+serverTime.getMinutes()+":"+serverTime.getSeconds());
}

function obtenerHoraServidor(){
	var resultado = "";
	$.ajax({
	   url:'/mr/ajax/get_time',
	   type:'post',
	   async:false,
       data:'',
       success: function(resp){
        ejecutarReloj(resp)
       }
	})
}