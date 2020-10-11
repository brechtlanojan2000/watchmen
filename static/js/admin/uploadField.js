$('input[type=file]').change(function (e){
    var file = e.target.files[0];

    $('.form-file-text').html(file.name);
    $('#image_view').attr('src', URL.createObjectURL(file));
})