$("#phoneInput").inputmask({"mask": "(+63) 999 999 9999"});

$('#phoneInput').keyup(function() {
    if($(this).val() == "") $(this).removeClass('active')
    else $(this).addClass('active')
})