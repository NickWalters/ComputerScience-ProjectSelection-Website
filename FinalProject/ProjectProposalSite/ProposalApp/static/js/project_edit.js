
    function addElementAfter(div, title, node){
        var referenceNode = document.getElementById(div);
        var newNode = document.createElement(node);
        newNode.id = title;
        if(title != "Blank" && title != "Blank2"){
            var text = document.createTextNode(title);
            newNode.appendChild(text);
            }
        referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
    }

    function addChild(div, title, node) {
        var referenceNode = document.getElementById(div);
        var newNode = document.createElement(node);
        newNode.id = title;
        if(title != "1" && title != "2" && title != "3" && title != "4" && title != "5"){
            var text = document.createTextNode(title);
            newNode.appendChild(text);
        }
        referenceNode.appendChild(newNode);
    }

    addElementAfter("div_id_prerequisites", "Will the project contact be at UWA?", "label");

    addElementAfter("div_id_description", "Blank", "div");
    document.getElementById("Blank").className = "row";

    addChild("Blank", "1", "div");
    document.getElementById("1").className = "col-6";
    addChild("Blank", "2", "div");
    document.getElementById("2").className = "col-6";

    addChild("1", "Add Extra Supervisor", "div");
    document.getElementById("Add Extra Supervisor").className = "btn btn-primary";
    document.getElementById("Add Extra Supervisor").style.marginRight = "10px";

    addChild("2", "Remove Extra Supervisor", "div");
    document.getElementById("Remove Extra Supervisor").className = "btn btn-danger";
    document.getElementById("Remove Extra Supervisor").style.display = "none";
    document.getElementById("Remove Extra Supervisor").style.float = "right";

    addElementAfter("div_id_IP", "Blank2", "div");
    document.getElementById("Blank2").className = "row";

    addChild("Blank2", "3", "div");
    document.getElementById("3").className = "col-4";
    document.getElementById("3").appendChild(document.getElementById("div_id_chemical"));
    document.getElementById("3").appendChild(document.getElementById("div_id_civil"));
    document.getElementById("3").appendChild(document.getElementById("div_id_elec"));
    document.getElementById("3").appendChild(document.getElementById("div_id_envir"));

    addChild("Blank2", "4", "div");
    document.getElementById("4").className = "col-4";
    document.getElementById("4").appendChild(document.getElementById("div_id_materials"));
    document.getElementById("4").appendChild(document.getElementById("div_id_mechanical"));
    document.getElementById("4").appendChild(document.getElementById("div_id_mechatronic"));
    document.getElementById("4").appendChild(document.getElementById("div_id_mining"));

    addChild("Blank2", "5", "div");
    document.getElementById("5").className = "col-4";
    document.getElementById("5").appendChild(document.getElementById("div_id_oilGas"));
    document.getElementById("5").appendChild(document.getElementById("div_id_petroleum"));
    document.getElementById("5").appendChild(document.getElementById("div_id_software"));
    document.getElementById("5").appendChild(document.getElementById("div_id_other"));

    addElementAfter("div_id_IP", "Please indicate all disciplines for which the project is suitable:", "label");

    var number_of_supervisors = 1;

    document.getElementById("div_id_supervisor2Title").style.display = "none";
    document.getElementById("div_id_supervisor2FirstName").style.display = "none";
    document.getElementById("div_id_supervisor2LastName").style.display = "none";

    document.getElementById("div_id_supervisor3Title").style.display = "none";
    document.getElementById("div_id_supervisor3FirstName").style.display = "none";
    document.getElementById("div_id_supervisor3LastName").style.display = "none";

    if(document.getElementById("id_supervisor2Title").value != "" || document.getElementById("id_supervisor2FirstName").value != "" || document.getElementById("id_supervisor2TLastName").value != ""){
        number_of_supervisors = 2;
        document.getElementById("div_id_supervisor2Title").style.display = "block";
        document.getElementById("div_id_supervisor2FirstName").style.display = "block";
        document.getElementById("div_id_supervisor2LastName").style.display = "block";
        document.getElementById("Remove Extra Supervisor").style.display = "block";

        if (document.getElementById("id_supervisor3Title").value != ""|| document.getElementById("id_supervisor3FirstName").value != "" || document.getElementById("id_supervisor3TLastName").value != "") {
            number_of_supervisors = 3;
            document.getElementById("div_id_supervisor3Title").style.display = "block";
            document.getElementById("div_id_supervisor3FirstName").style.display = "block";
            document.getElementById("div_id_supervisor3LastName").style.display = "block";
            document.getElementById("Remove Extra Supervisor").style.display = "block";
            document.getElementById("Add Extra Supervisor").style.display = "none";
        }
    }

    document.getElementById("Add Extra Supervisor").onclick = function(){
        if(number_of_supervisors == 1){
            document.getElementById("div_id_supervisor2Title").style.display = "block";
            document.getElementById("div_id_supervisor2FirstName").style.display = "block";
            document.getElementById("div_id_supervisor2LastName").style.display = "block";
            document.getElementById("Remove Extra Supervisor").style.display = "inline-block";
            number_of_supervisors += 1;
        } else if (number_of_supervisors == 2) {
            document.getElementById("div_id_supervisor3Title").style.display = "block";
            document.getElementById("div_id_supervisor3FirstName").style.display = "block";
            document.getElementById("div_id_supervisor3LastName").style.display = "block";
            document.getElementById("Add Extra Supervisor").style.display = "none";
            number_of_supervisors += 1;
        }
    };

    document.getElementById("Remove Extra Supervisor").onclick = function(){
        if(number_of_supervisors == 2){
            document.getElementById("div_id_supervisor2Title").style.display = "none";
            document.getElementById("div_id_supervisor2FirstName").style.display = "none";
            document.getElementById("div_id_supervisor2LastName").style.display = "none";
            document.getElementById("Remove Extra Supervisor").style.display = "none";
            number_of_supervisors -= 1;
        } else if (number_of_supervisors == 3) {
            document.getElementById("div_id_supervisor3Title").style.display = "none";
            document.getElementById("div_id_supervisor3FirstName").style.display = "none";
            document.getElementById("div_id_supervisor3LastName").style.display = "none";
            document.getElementById("Add Extra Supervisor").style.display = "inline-block";
            number_of_supervisors -= 1;
        }
    };
