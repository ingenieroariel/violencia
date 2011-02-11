/**
 * GRAPPELLI UTILS
 * functions needed for Grappelli
 */
 
var django = {
    "jQuery": jQuery.noConflict(true)
};

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

(function($) {
    
    // dateformat
    grappelli.getFormat = function(type) {
        if (type == "date") {
            var format = DATE_FORMAT.toLowerCase().replace(/%\w/g, function(str) {
                str = str.replace(/%/, '');
                return str + str;
            });
            return format;
        }
    };
    
    // datepicker, timepicker init
    grappelli.initDateAndTimePicker = function() {
        
        // HACK: get rid of text after DateField (hardcoded in django.admin)
        $('p.datetime').each(function() {
            var text = $(this).html();
            text = text.replace(/^\w*: /, "");
            text = text.replace(/<br>.*: /, "<br>");
            $(this).html(text);
        });
        
        var options = {
            //appendText: '(mm/dd/yyyy)',
            showOn: 'button',
            buttonImageOnly: false,
            buttonText: '',
            dateFormat: grappelli.getFormat('date'),
            showButtonPanel: true,
            showAnim: '',
            // HACK: sets the current instance to a global var.
            // needed to actually select today if the today-button is clicked.
            // see onClick handler for ".ui-datepicker-current"
            beforeShow: function(year, month, inst) {
                grappelli.datepicker_instance = this;
            }
        };
        var dateFields = $("input[class*='vDateField']:not([id*='__prefix__'])");
        dateFields.datepicker(options);
        
        if (typeof IS_POPUP != "undefined" && IS_POPUP) {
            dateFields.datepicker('disable');
        }
        
        // HACK: adds an event listener to the today button of datepicker
        // if clicked today gets selected and datepicker hides.
        // use live() because couldn't find hook after datepicker generates it's complete dom.
        $(".ui-datepicker-current").live('click', function() {
            $.datepicker._selectDate(grappelli.datepicker_instance);
            grappelli.datepicker_instance = null;
        });
        
        // init timepicker
        $("input[class*='vTimeField']:not([id*='__prefix__'])").grp_timepicker();
    };
    
    // HACK: add no-wrap to table-elements.
    grappelli.initTableElements = function() {
        $("td input.vForeignKeyRawIdAdminField, td input.vFileBrowseField, td a.add-another").each(function() {
            $(this).parent().addClass('nowrap');
        });
    };
    
    // changelist: filter
    grappelli.initFilter = function() {
        $("a.toggle-filters").click(function() {
            $(".filter-pulldown").toggle();
            $("#filters").toggleClass("open");
        });
        $(".filter_choice").change(function(){
            location.href = $(this).val();
        });
    };
    
    // changelist: searchbar
    grappelli.initSearchbar = function() {
        var searchbar = $("input#searchbar");
        searchbar.focus();
    };
    
    grappelli.updateSelectFilter = function(form) {
        if (typeof SelectFilter != "undefined"){
            form.find(".selectfilter").each(function(index, value){
                var namearr = value.name.split('-');
                SelectFilter.init(value.id, namearr[namearr.length-1], false, "{% admin_media_prefix %}");
            });
            form.find(".selectfilterstacked").each(function(index, value){
                var namearr = value.name.split('-');
                SelectFilter.init(value.id, namearr[namearr.length-1], true, "{% admin_media_prefix %}");
            });
        }
    };
    
    grappelli.reinitDateTimeFields = function(form) {
        form.find(".vDateField").datepicker({
            showOn: 'button',
            buttonImageOnly: false,
            buttonText: '',
            dateFormat: grappelli.getFormat('date')
        });
        form.find(".vTimeField").grp_timepicker();
    };
    
})(django.jQuery);

