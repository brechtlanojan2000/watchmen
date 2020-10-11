const searchInstance = new mdb.Datatable(document.getElementById('datatable'))

console.log(searchInstance)

document.getElementById('tableSearch').addEventListener('input', (e) => {
    searchInstance.search(e.target.value);
});
