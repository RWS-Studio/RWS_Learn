function checkSoftwareVersion(){
    // for index
    let params = new URLSearchParams(window.location.search);
    let is_update_available = params.get('update-available');
    if(is_update_available == "true"){
        showUpdateAvailable();
        let wants_download = confirm("Do you want to download the new version ?");
        if(wants_download){
            window.location.href = "https://github.com/RWS-Studio/RWS_Learn";
        }
    }
    else if(is_update_available == "false"){
        showSoftwareUpToDate();
    }
}

function fillInHiddenFields(object){
    if(object == "grade"){
        let id_input = document.querySelector("#js-input-id");
        let subject_input = document.querySelector("#js-input-subject");

        let params = new URLSearchParams(window.location.search);

        let grade_id = params.get('id');
        let subject = params.get('subject');

        id_input.setAttribute("value", grade_id);
        subject_input.setAttribute("value", subject);
    }
    else if(object == "subject"){
        let subject_input = document.querySelector("#js-input-subject");

        let params = new URLSearchParams(window.location.search);

        let subject = params.get('subject');

        subject_input.setAttribute("value", subject);
    }
}
