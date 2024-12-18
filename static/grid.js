var gridContainer = document.getElementById("icon-grid");
var rows = 10;
var columns = 10;
function createGrid() {
    if (!gridContainer)
        return;
    var _loop_1 = function (row) {
        var _loop_2 = function (col) {
            var gridItem = document.createElement("div");
            gridItem.className = "grid-item";
            gridItem.textContent = "🔲";
            gridItem.dataset.row = row.toString();
            gridContainer.dataset.col = col.toString();
            gridItem.addEventListener("click", function () { return handleGridClick(row, col); });
            gridContainer.appendChild(gridItem);
        };
        for (var col = 0; col < columns; col++) {
            _loop_2(col);
        }
    };
    for (var row = 0; row < rows; row++) {
        _loop_1(row);
    }
}
function handleGridClick(row, col) {
    console.log('Clicked on Row: ${row}, Column: ${col}');
    fetch("/handle_click", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ row: row, column: col }),
    })
        .then(function (response) { return response.json(); })
        .then(function (data) { return console.log("Server Response:", data); })
        .catch(function (error) { return console.error("Error:", error); });
}
createGrid();
