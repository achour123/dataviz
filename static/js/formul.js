$("#rien").on("click", function () {
    if (this.checked) {
        $("input.group1").prop("checked", false);;
        $("input.group1").attr("disabled", true);
    } else {
        $("input.group1").attr("disabled", false);
    }
});

$("#sympt").on("click", function () {
    if (this.checked) {
        $("input.group2").prop("checked", false);;
        $("input.group2").attr("disabled", true);
    } else {
        $("input.group2").attr("disabled", false);
    }
});


function validateForm() {

    let score = 0;

    if (document.getElementById("fievre").checked) score += 1;
    if (document.getElementById("respiratoire").checked) score += 1;
    if (document.getElementById("diarrhe").checked) score += 1;
    if (document.getElementById("cephalees").checked) score += 1;
    if (document.getElementById("douleurs").checked) score += 1;
    if (document.getElementById("odorat").checked) score += 1;
    if (document.getElementById("appetit").checked) score += 1;
    if (document.getElementById("fatigue").checked) score += 1;

    if (document.getElementById('etranger').checked) score += 1;
    if (document.getElementById('voyage').checked) score += 1;
    if (document.getElementById('contact').checked) score += 1;

    if (document.getElementById("hypertension").checked) score += 0.5;
    if (document.getElementById("diabete").checked) score += 0.5;
    if (document.getElementById("maladieRespiratoire").checked) score += 0.5;
    if (document.getElementById("renale").checked) score += 0.5;
    if (document.getElementById("immunitaire").checked) score += 0.5;
    if (document.getElementById("fumeur").checked) score += 0.5;


    if (score < 3) {
        swal({
            title: "Vous etes en bonne santé",
            text: "Veuillez portez votre masque et utiliser du gel hydroalcoolique",
            icon: "success",
            button: true,
        }).then((value) => {
            document.forms['reg_form'].submit();
        });
    }
    else if (score < 5) {
        swal({
            title: "Vous etes un facteur de risque",
            text: "veuillez respecter l'auto-confinement à domicile",
            icon: "warning",
            button: "ok",
        }).then((value) => {
            document.forms['reg_form'].submit();
        });
    }
    else {
        swal({
            title: "Appelez 190",
            text: "Restez a la maison",
            icon: "error",
            button: "ok",
        }).then((value) => {
            document.forms['reg_form'].submit();
        });
    }
}

