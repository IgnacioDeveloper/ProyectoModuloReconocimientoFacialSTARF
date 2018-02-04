var args;

$("main").ready(function(){
	var path = window.location.pathname;
	var subUrl = path.substring(4);
	var entidad='', tipo=null;
	if(/^[0-9]+$/.test(subUrl.substring(subUrl.length - 1))){
	    subUrl = subUrl.substring(0,subUrl.lastIndexOf('/'));
	    console.log('Number Detected');
	    console.log(subUrl);
	    switch(subUrl){
	        case "alumnos/modify" : entidad = "alumno";tipo = 1; break;
            case "usuarios/modify" : entidad = "usuario"; tipo = 1;break;
            case "alumnos/consult" : entidad = "alumno";tipo = 2; break;
            case "usuarios/consult" : entidad = "usuario"; tipo = 2;break;
            case "alumnos/eliminate" : entidad = "alumno";tipo = 3; break;
            case "usuarios/eliminate" : entidad = "usuario"; tipo = 3;break;
	    }
	} else{
	    switch(subUrl){
            case "alumnos/add" : entidad = "alumno";tipo = 0; break;
            case "usuarios/add" : entidad = "usuario"; tipo = 0;break;
            case "alumnos/list" : entidad = "alumno"; break;
            case "usuarios/list" : entidad = "usuario";break;
        }
	}
	if(tipo === null) prepareListado(entidad);
    else if(tipo === 0 || tipo === 1 || tipo === 2) prepareFormulario(entidad,tipo);
    else prepareMessage(entidad,tipo);

});


//FORMULARIOS

function prepareFormulario(entidad,tipo){
        $(".forms").fadeIn();
        $('label').after('<br/>');
		customGeneralItems(entidad,tipo);
		switch(entidad){
			case "alumno": prepareAlumnoForm(tipo); break;
			case "aula": prepareAulaForm(tipo); break;
			case "camara": prepareCamaraForm(tipo); break;
			case "comision": prepareComisionForm(tipo); break;
   			case "materia": prepareMateriaForm(tipo); break;
			case "clase": prepareClaseForm(tipo); break;
			case "usuario": prepareUsuarioForm(tipo); break;
		}
	}

function customGeneralItems(entidad,tipo){
    var titulo,textoBoton1,textoBoton2 = "Cancelar";
    var entidadesMasculinas = ["alumno","usuario"];
    switch(tipo){
        case 0: titulo = "Nuev"; textoBoton1 = "Guardar Informacion de"; break;
        case 1: titulo = "Modificar informacion de"; textoBoton1 = "Guardar Cambios de"; break
        case 2: titulo = "Consultar Informacion de"; textoBoton1 = "Editar Informacion de";
                textoBoton2 = "Ok"; break;
    }
    if(entidadesMasculinas.indexOf(entidad)>-1){
        if(tipo===0){titulo+="o "+entidad;}else{titulo+="l "+entidad;}
        textoBoton1+="l "+entidad;
    }
    else{
        if(tipo===0){titulo+="a "+entidad;}else{titulo+=" la "+entidad;}
        if(entidad!="aula")textoBoton1+=" la "+entidad; else textoBoton1+="l "+entidad
    }

    $(".tituloForm").html(titulo);
    $("#button1").html(textoBoton1);
    $("#button2").html(textoBoton2);
}

function prepareAlumnoForm(tipo){
    $('#id_legajo').addClass('mediumNumber');
    $('#id_nombre').addClass('onelineDescription');
    $('#id_apellido').addClass('onelineDescription');
    $('#id_mail').addClass('onelineDescription');
}

function prepareAulaForm(tipo){

}

function prepareCamaraForm(tipo){

}

function prepareComisionForm(tipo){

}

function prepareClaseForm(tipo){

}

function prepareMateriaForm(tipo){

}

function prepareUsuarioForm(tipo){
    $('#form-type').addClass('small-forms');
    $('#id_codigo_usuario').addClass('tinyNumber');
    $('#id_nombre').addClass('onelineDescription');
    $('#id_apellido').addClass('onelineDescription');
    $('#id_username').addClass('onelineDescription');
    $('#id_password').addClass('onelineDescription');
}


//LISTADO

var selectedRow = null;

function releaseSelectedRow(){
    if(selectedRow !== null){
            selectedRow.classList.remove('selected');
            selectedRow=null;
    }
}

function getRowCount(){
    return $('.listado table.lista tbody tr:visible').length - 1;
}

function filter(){
    var criterio = $('.listado .searchBar > #inputCriterio').val().toUpperCase();
    var campo = $('.listado .searchBar #selectCampo').find(":selected").text().toUpperCase();
    var numColumna;
    console.log(campo);
    releaseSelectedRow();
    $('tbody tr:first-child').each(function(){
        $(this).children('td').each(function(index){
            if($(this).text().toUpperCase() === campo){
                numColumna = index;
                return false;
            }
        })
    })
    $('tbody tr:not(.headers)').each(function(){
        $(this).children('td:eq('+numColumna+')').each(function(){
            console.log($(this).text());
            console.log(criterio);
            if($(this).text().toUpperCase().startsWith(criterio))
                $(this).parent().show();
            else
                $(this).parent().hide();
        })
    })
    $('.listado .searchBar #lblResultado').html('Resultados: '+getRowCount());
}

function prepareListado(entidad){
    $("#btnCerrar").click(function(){location.href="../index"})
    $(".btnVolver").click(function(){location.href="../index"})
    var columnas;
    switch(entidad){
        case 'alumno': prepareListadoAlumno();break;
        case 'usuario': prepareListadoUsuario();break;
    }
}

function prepareListadoAlumno(){
    $(".listado-title").text('Listado de Alumnos');
    $(".btnAdd").click(function(){location.href="../alumnos/add"})
    $(".btnModify").click(function(){
        location.href="../alumnos/modify/"+$(".listado tbody tr.selected").attr('pk');
    })
    $(".btnDelete").click(function(){
        location.href="../alumnos/eliminate/"+$(".listado tbody tr.selected").attr('pk');
    })
    $("tr:first-child td:nth-child(1)").html('Legajo');
    $("tr:first-child td:nth-child(2)").html('Nombre');
    $("tr:first-child td:nth-child(3)").html('Apellido');
    $("tr td:nth-child(1)").width('2%');
    $("tr td:nth-child(2)").width('5%');
    $("tr td:nth-child(3)").width('5%');
    $("#selectCampo").append('<option>Legajo</option><option>Nombre</option><option>Apellido</option>');
}

function prepareListadoUsuario(){
    $(".listado-title").text('Listado de Usuarios');
    $(".btnAdd").click(function(){location.href="../usuarios/add"})
    $(".btnModify").click(function(){
        location.href="../usuarios/modify/"+$(".listado tbody tr.selected").attr('pk');
    })
    $(".btnDelete").click(function(){
        location.href="../usuarios/eliminate/"+$(".listado tbody tr.selected").attr('pk');
    })
    $("tr:first-child td:nth-child(1)").html('Nombre');
    $("tr:first-child td:nth-child(2)").html('Apellido');
    $("tr:first-child td:nth-child(3)").html('Username');
    $("tr td:nth-child(1)").width('5%');
    $("tr td:nth-child(2)").width('5%');
    $("tr td:nth-child(3)").width('5%');
    $("#selectCampo").append('<option>Nombre</option><option>Apellido</option><option>Username</option><option>');
}

function eventos(){
    //BOTONES GENERALES DE VOLVER FORMULARIOS Y MENSAJES
    var oldURL = document.referrer;
    var curURL = document.URL;
    oldURL="../"+oldURL.substring(oldURL.indexOf('mr/')).substring(3);
    curURL="../"+curURL.substring(curURL.indexOf('mr/')).substring(3);
    console.log(oldURL);
    console.log(curURL);
    console.log(oldURL.substring(3));
    $("#oldURLdata").val(oldURL.substring(3));
    if(oldURL.length>0 && oldURL.substring(oldURL.lastIndexOf('/'))
        !==curURL.substring(curURL.lastIndexOf('/'))){
        $("#btnCerrar").click(function(){
            location.href='../'.repeat(contar_caracter('/',curURL)-1)+'mr/'+oldURL
        })
        $("#button2").click(function(){
            location.href='../'.repeat(contar_caracter('/',curURL)-1)+'mr/'+oldURL
        })
    }
    else{
        $("#btnCerrar").click(function(){location.href='../index'})
        $("#button2").click(function(){location.href='../index'})
    }
    //LISTADO
    $('.listado table.lista').click(function(e){
        releaseSelectedRow();
        selectedRow = e.target.parentNode;
        selectedRow.classList.add('selected');
    })
    $('.listado table.lista').ready(function(e){
        $('.listado .searchBar #lblResultado').html('Resultados: '+getRowCount());

    })
    $('.listado .searchBar #btnBuscar').click(function(){
        filter();
    })
}

//MESSAGES

function prepareMessage(entidad,tipo){
    if(tipo === 3) prepareDeleteMessage(entidad);
}


function prepareDeleteMessage(entidad){
    var mensaje = 'Esta seguro que desea eliminar';
    $('.messages .tituloMessage').text('Advertencia!!!')
    $('.messages #button1').text('Si, deseo eliminarlo')
    $('.messages #button2').text('Cancelar')
    switch(entidad){
        case 'alumno': mensaje+=' al alumno </br>Legajo: '+args['legajo']+', Nombre y Apellido: '+args['nombre']+' '+args['apellido']+' ?';break;
    }
    $('.message-content > h3').html(mensaje);
    $('.messages').show();
}

//USEFUL FUNCTIONS

function contar_caracter(caracter, cadena){
    var counter=0;
    for(i=0;i<cadena.length;i++)
        if(cadena[i]===caracter)
            counter++;
    return counter
}

eventos();