$("#priceInput").inputmask({"mask": "9999\.99"});

$('#priceInput').keyup(function() {
    if($(this).val() == "") $(this).removeClass('active')
    else $(this).addClass('active')
})