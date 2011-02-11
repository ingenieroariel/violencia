(function($) {
    $(document).ready(function($) {

        /*
         * violencia generic lookup para ubicaciones dinamicas
         */
        function setUbicacionName(){
            $("input[id$='-valor']").each(function(k,v){
                inline_id = $(v).attr("id").split("-")[4];
                content_type = $("#id_territorios-ubicacion-content_type-object_id-"+inline_id+"-content_type_ubicacion").val();
                valor = $(v).val();
                if(inline_id!="__prefix__"){
                    if(valor){
                        $.get("/api/territorios/"+content_type+"/"+valor+"/", function(data){
                            $(v).next('span').remove();
                            $(v).parent('div').append("<span style='display: inline-block;font-weight: bold;padding:3px 0 0 4px'>"+data+"</span>");
                        });
                    }
                }
            });
        }

        setUbicacionName();

        if($("div#territorios-ubicacion-content_type-object_id-group").length > 0){
            //id_territorios-ubicacion-content_type-object_id-0-content_type_ubicacion
            //id_territorios-ubicacion-content_type-object_id-0-seleccionador

            $("select[id$='content_type_ubicacion']").change(function(){
                element_id = $(this).attr('id');
                inline_id = element_id.split("-")[4];
                seleccionador = $("select#id_territorios-ubicacion-content_type-object_id-"+inline_id+"-seleccionador");
                $("#id_territorios-ubicacion-content_type-object_id-"+inline_id+"-valor").val("").next('span').remove();
                //$("#id_territorios-ubicacion-content_type-object_id-"+inline_id+"-valor").;
                seleccionador.html("<option>Cargando...</option>");

                var valor = $(this).val();
                $.getJSON("/api/content_types/"+valor+"/", function(data){
                    seleccionador.html("").append("<option value=''>escoja</option>");
                    $.each(data, function(k,v){
                        seleccionador.append($("<option value='"+v.id+"'>"+v.unicode+"</option>"));
                    })

                });

            });

            //id_territorios-ubicacion-content_type-object_id-0-seleccionador
            $("select[id$='seleccionador']").change(function(){
                element_id = $(this).attr('id');
                inline_id = element_id.split("-")[4];
                $("#id_territorios-ubicacion-content_type-object_id-"+inline_id+"-valor").val( $(this).val());
                $(this).html("").append("<option value=''>------</option>");
                setUbicacionName();
            });
        }//if

    });

    $("select[id*='tipo']").each(function(k,v){
            //console.log(k)
            select = $(v);
            text = null;
            temp = null;
            g=null;
            select.children('option').each(function(k, v){
                op = $(v);
                if(op.text().indexOf('/') != -1){
                    label = op.text().split('/')[0];
                    text = op.text().split('/')[1];

                    if(temp!=label){
                        if(g){
                            g.appendTo(select);
                        }

                        g = $("<optgroup></optgroup>").attr("label", label);
                        g.append(op);
                        //console.log(label);
                        //console.log(text);

                    }else{
                        g.append(op);
                        //console.log(text);
                    }

                    temp = label;

                    //console.log(label)
                    //console.log(text);
                }

            });
        });
        
})(django.jQuery);

function showPopup(triggeringLink) {
    var name = triggeringLink.id.replace(/^add_/, '');
    name = id_to_windowname(name);
    href = triggeringLink.href;
    var win = window.open(href, name, 'height=500,width=1000,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}
function getURLParameter(name) {
    return unescape(
        (RegExp(name + '=' + '(.+?)(&|$)').exec(location.search)||[,null])[1]
    );
}