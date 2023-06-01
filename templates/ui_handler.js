class CRUDHandler {
    host = "http://127.0.0.1:9000"
    filterParams = { hello: "hello" };
    renderList(data) {
        let content = document.getElementById("content");
        content.innerHTML = ""
        if (data?.data?.length > 0) {
            let trTemplate = ""
            for (let obj of data?.data) {
                trTemplate += `
                <tr>
                    <th scope="row">${obj?.table_code}</th>
                    <td>${obj?.table_number}</td>
                    <td>
                        <span style="cursor: pointer;" onclick="editTemplateObj('${obj?._id}')"> Edit </span> &nbsp;&nbsp;&nbsp
                        <span style="cursor: pointer;" onclick="deleteObj('${obj?._id}')"> Delete </span> 
                    </td>
                </tr>
                `
            }
            content.innerHTML = `

            <table class="table table-dark">
            <thead>
                <tr>
                    <th scope="col">Table Code</th>
                    <th scope="col">Table Number</th>
                    <th scope="col">Action</th>
                </tr>
            </thead>
            <tbody id="table_body">
                ${trTemplate}
            </tbody>
        </table>
                
            `
        } else {
            content.innerHTML = `
            <div class="alert alert-danger" role="alert">
                No Data Found!.
            </div>          
            `
        }
    }

    request(req, callback) {
        fetch(req)
            .then(function (res) { return res.json() })
            .then(function (res) {
                callback["obj"][callback["fun"]](res);
            })
    }

    listTable() {
        let req = new Request(
            `${this.host}/table?` + new URLSearchParams(this.filterParams).toString(), {
            method: "GET"
        }
        )
        this.request(req, { obj: this, fun: "renderList" })
    }

    addTable() {
        document.getElementById("content").innerHTML = `
        <form action="#" onsubmit="addTable(event)" method="post">
        <div class="form-group">
            <label for="exampleInputPassword1">Table Code</label>
            <input type="number"  name="table_code" id="table_code" style="width: 300px;" class="form-control" placeholder="Enter Table Code" required>
        </div>
        <div class="form-group">
            <label >Table Number</label>
            <input type="text" name="table_number" id="table_number" class="form-control" placeholder="Enter Table Number" style="width: 300px;" required>
        </div>
        
        <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        `
    }

    tableAdd(data) {
        this.request(
            new Request(
                this.host + "/table", {
                method: "POST",
                body: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json"
                }
            }),
            {
                obj: this, fun: "listTable"
            }
        )
        window.location.href = window.location.origin + "/#listTable"
    }

    tableUpdate(data, objectId) {
        this.request(
            new Request(
                this.host + `/table?tabel_management_id=${objectId}`, {
                method: "PUT",
                body: JSON.stringify(data),
                headers: {
                    "Content-Type": "application/json"
                }
            }),
            {
                obj: this, fun: "listTable"
            }
        )
        window.location.href = window.location.origin + "/#listTable"
    }

    deleteObj(deleteId) {
        this.request(
            new Request(
                this.host + "/table/?" + new URLSearchParams(deleteId).toString(),
                {
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json"
                    }
                }),
            {
                obj: this, fun: "listTable"
            }
        )
    }

    renderEdit(resp) {

        document.getElementById("content").innerHTML = `
        <form action="#" onsubmit="editObj(event)" method="post">
        <div class="form-group">
            <label for="table_code">Table Code</label>
            <input type="number"  value="${resp?.data?.table_code}" name="table_code" id="table_code" style="width: 300px;" class="form-control" placeholder="Enter Table Code" required>
        </div>
        <div class="form-group">
            <label for="table_number" >Table Number</label>
            <input type="text" name="table_number" id="table_number" value="${resp?.data?.table_number}" class="form-control" placeholder="Enter Table Number" style="width: 300px;" required>
        </div>
        <button type="submit" class="btn btn-primary">Update</button>
        </form>
        `
    }

    editObj(objectId) {

        this.request(
            new Request(
                this.host + `/table?tabel_management_id=${objectId}`, {
                method: "GET"
            }),
            {
                obj: this, fun: "renderEdit"
            }
        )

    }

    load() {
        let hash = window.location.hash.replace("#", "") || "listTable";
        hash = hash.split("-")
        console.log(hash);
        this[hash[0]](hash[1]);
    }
}

const crudHandler = new CRUDHandler();
window.addEventListener("load", () => { crudHandler.load(); });

for (let navLink of document.getElementsByClassName("nav-link")) {
    navLink.addEventListener("click", load)
}
function load() {
    setTimeout(() => {
        crudHandler.load();
    }, 5);
}

function addTable(event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    let data = {
        table_code: formData.get("table_code"),
        table_number: formData.get("table_number")
    }
    crudHandler.tableAdd(data);
}

function editTemplateObj(objectId) {
    window.location.href = `/#editObj-${objectId}`
    crudHandler.editObj(objectId);
}

function editObj(event) {
    event.preventDefault();

    let formData = new FormData(event.target);
    let data = {
        table_code: formData.get("table_code"),
        table_number: formData.get("table_number")
    }
    let hash = window.location.hash.replace("#", "");
    hash = hash.split("-")
    crudHandler.tableUpdate(data, hash[1]);

}
function deleteObj(objectId) {
    let userConfirmation = confirm(
        "Are you sure you want to delete!"
    )
    if (userConfirmation) {
        crudHandler.deleteObj({ tabel_management_id: objectId })
    }
    else {
        console.log("Not Delete", objectId);
    }
}