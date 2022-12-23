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

function setCookie(cname, cvalue, exdays){
    const d=new Date();
    d.setTime(d.getTime()+(exdays*24*60*60*1000));
    let expires="expires="+d.toUTCString();
    document.cookie=cname+"="+cvalue+";"+expires+";path=/";
}
function deleteCookie(cname){
    const d=new Date();
    d.setTime(d.getTime()+(24*60*60*1000));
    let expires="expires="+d.toUTCString();
    document.cookie=cname+"=;"+expires+";path=/";
}
function getCookie(cname){
    let name=cname+"=";
    let decodedCookie=decodeURIComponent(document.cookie);
    let ca=decodedCookie.split(';');
    for(let i=0;i<ca.length;i++){
        let c=ca[i];
        while(c.charAt(0)==' '){
            c=c.substring(1);
        }
        if(c.indexOf(name)==0){
            return c.substring(name.length,c.length);
        }
    }
    return "";
}
