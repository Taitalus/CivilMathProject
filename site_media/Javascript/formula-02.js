$(document).ready(function(){
    $('#submit_button').click(function(){
        var P1=$('#P1').val().trim();
        var W=$('#W').val().trim();
        var M=$('#M').val().trim();
        var A1=$('#A1').val().trim();
        $.get('CalculateFormula2/',{
            P1:P1.trim(),
            W: W.trim(),
            MX:M.trim(),
            A1:A1.trim()
            },function(data){
            $('#value_of_R').text(data['R']);
            $('#value_of_lambda').text(data['lambda']);
            $('#equation_no').text(data['equation']);
            $('#result_pane').css({'display':'block'});
        });
    });
});