$(document).ready(function(){
    $('#submit_button').click(function(){
        var P1=$('#P1').val().trim();
        var W=$('#W').val().trim();
        var MX=$('#MX').val().trim();
        var MY=$('#MY').val().trim();
        var A1=$('#A1').val().trim();
        var R=$('#R').val().trim();
        $.get('CalculateFormula1/',{
            P1:P1.trim(),
            W: W.trim(),
            MX:MX.trim(),
            MY:MY.trim(),
            A1:A1.trim(),
            R: R.trim()
        },function(data){
            $('#value_of_L').text(data['L']);
            $('#value_of_lambda').text(data['lambda']);
            $('#equation_no').text(data['equation']);
            $('#result_pane').css({'display':'block'});
        });
    });
});