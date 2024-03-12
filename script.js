document.addEventListener("DOMContentLoaded", function() {
    const bookListDiv = document.getElementById("bookList");
    const sortDropdown = document.getElementById("sortDropdown");
    const reverseSortButton = document.getElementById("reverseSortButton");

    let sortOrder = 1; // Initial sort order (1 for ascending, -1 for descending)

    // Function to fetch and display books
    function displayBooks(books) {
        bookListDiv.innerHTML = "";
        books.forEach(book => {
            const bookDiv = createBookElement(book);
            bookListDiv.appendChild(bookDiv);
        });
    }
function createBookElement(book) {
    const bookDiv = document.createElement("div");
    bookDiv.classList.add("book");
    const formattedDate = formatDate(book["Date Read"]);
    bookDiv.innerHTML = `
        <h2>${book.Title}</h2>
        <p><strong>Author:</strong> ${book.Author}</p>
        <p><strong>Date Read:</strong> ${formattedDate}</p>
        <p><strong>Series:</strong> ${book.Series}</p>
        <p><strong>Read For:</strong> ${book.ReadForFormatted}</p>
        <p><strong>Language Read In:</strong> ${book.Language}</p>
    `;

    // Event listener for clicking on the book
    bookDiv.addEventListener('click', function() {
        bookDiv.classList.toggle('expanded');
        if (bookDiv.classList.contains('expanded')) {
            addBookImage(bookDiv, book.ISBN);
        } else {
            removeBookImage(bookDiv);
        }
    });

    return bookDiv;
}

// Function to add image to expanded book element
function addBookImage(bookDiv, isbn) {
    const imageDiv = document.createElement("div");
    imageDiv.classList.add("bookImage");
    imageDiv.style.backgroundImage = `url(images/${isbn}.jpg)`; // Adjust path and format accordingly
    bookDiv.appendChild(imageDiv);
}

// Function to remove image from expanded book element
function removeBookImage(bookDiv) {
    const imageDiv = bookDiv.querySelector('.bookImage');
    if (imageDiv) {
        bookDiv.removeChild(imageDiv);
    }
}






    // Function to format date string
    function formatDate(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', options);
    }

    // Function to sort books based on selected option and sort order
    function sortBooks(books, sortBy) {
        if (sortBy === "author") {
            return books.sort((a, b) => a.Author.localeCompare(b.Author) * sortOrder);
        } else if (sortBy === "title") {
            return books.sort((a, b) => a.Title.localeCompare(b.Title) * sortOrder);
        } else if (sortBy === "duration") {
            return books.sort((a, b) => (a.ReadFor - b.ReadFor) * sortOrder);
        }
        return books; // Default to original order
    }

    // Event listener for dropdown change
    sortDropdown.addEventListener("change", function() {
        const sortBy = sortDropdown.value;
        fetch("readbooks.json")
            .then(response => response.json())
            .then(data => {
                const sortedBooks = sortBooks(data, sortBy);
                displayBooks(sortedBooks);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    });

    // Event listener for reverse sort button
    reverseSortButton.addEventListener("click", function() {
        sortOrder *= -1; // Toggle sort order between ascending and descending
        const sortBy = sortDropdown.value;
        fetch("readbooks.json")
            .then(response => response.json())
            .then(data => {
                const sortedBooks = sortBooks(data, sortBy);
                displayBooks(sortedBooks);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
            });
    });

    // Initial display of books
    fetch("readbooks.json")
        .then(response => response.json())
        .then(data => {
            displayBooks(data);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
});
