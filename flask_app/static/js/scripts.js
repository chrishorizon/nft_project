// Made with Flider.
$("#profileImage").click(function(e) {
    $("#imageUpload").click();
});

function fasterPreview(uploader) {
    if (uploader.files && uploader.files[0]) {
        $('#profileImage').attr('src',
            window.URL.createObjectURL(uploader.files[0]));
    }
}

$("#imageUpload").change(function () {
    fasterPreview(this);
});

function addShadow(element){
    element.classList.add("shadow");
}

function removeShadow(element){
    element.classList.remove("shadow");
}
