const gridContainer = document.getElementById("icon-grid");

const rows = 10;
const columns = 10;

function createGrid(): void {
    if (!gridContainer) return;

    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < columns; col++) {
            const gridItem = document.createElement("div");
            gridItem.className = "grid-item";
            gridItem.textContent = "🔲";
            gridItem.dataset.row = row.toString();
            gridContainer.dataset.col = col.toString();

            gridItem.addEventListener("click", () => handleGridClick(row, col));
            gridContainer.appendChild(gridItem);
        }
    }
}

function handleGridClick(row: number,  col: number): void {
    console.log('Clicked on Row: ${row}, Column: ${col}');

    fetch("/handle_click", {
        method:"POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ row, column: col}),

    })

        .then((response) => response.json())
        .then((data) => console.log("Server Response:", data))
        .catch((error) => console.error("Error:", error));

}

createGrid();