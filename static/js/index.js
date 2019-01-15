$(document).ready( function() {

    $('#image-file-url').on('change', function () {
        var imageObj = new Image();
        imageObj.onload = function() {
            drawImage(this);
          };
          imageObj.crossOrigin = "Anonymous";
          imageObj.src = $(this).val();
    });

});

function drawImage(imageObj) {
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');
    var imageX = 69;
    var imageY = 50;

    context.drawImage(imageObj, imageX, imageY);
}