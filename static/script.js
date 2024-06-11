// _____________________MODAL______________________
// Get all elements with class "grid-item"
document.addEventListener("DOMContentLoaded", function() {
    // Get all elements with class "grid-item"
    const gridItems = document.querySelectorAll('.grid-item');

    // Get the modal elements
    const modalOverlay = document.querySelector('.modal-overlay');
    const modalText = document.querySelector('.modal-text');
    const closeButton = document.querySelector('.close');
    const leftArrow = document.querySelector('.left-arrow');
    const rightArrow = document.querySelector('.right-arrow');

    // Variable to store the index of the currently focused grid item
    let currentIndex = -1;

    // Add click event listener to each grid item
    gridItems.forEach((gridItem, index) => {
        gridItem.addEventListener('click', () => {
            // Update currentIndex
            currentIndex = index;
            // Get the additional info within the clicked grid item
            const additionalInfo = gridItem.querySelector('.additional-info');
            if (additionalInfo) {
                // Update modal text with additional info content
                modalText.innerHTML = additionalInfo.innerHTML;
                // Show modal overlay
                modalOverlay.style.display = 'block';
            }
        });
    });

    // Add click event listener to close button
    closeButton.addEventListener('click', () => {
        closeModal();
    });

    // Add click event listener to modal overlay to close modal when clicked outside
    modalOverlay.addEventListener('click', (event) => {
        if (event.target === modalOverlay) {
            closeModal();
        }
    });

    // Function to close modal
    function closeModal() {
        // Hide modal overlay
        modalOverlay.style.display = 'none';
        // Reset currentIndex
        currentIndex = -1;
    }

    // Add event listener for keydown event
    document.addEventListener("keydown", function(event) {
        if (modalOverlay.style.display === 'block' && currentIndex !== -1) {
            if (event.key === 'ArrowLeft' && currentIndex > 0) {
                gridItems[currentIndex - 1].click();
            } else if (event.key === 'ArrowRight' && currentIndex < gridItems.length - 1) {
                gridItems[currentIndex + 1].click();
            }
        }
    });

    // Add event listener for left arrow button
    leftArrow.addEventListener('click', () => {
        if (currentIndex > 0) {
            gridItems[currentIndex - 1].click();
        }
    });

    // Add event listener for right arrow button
    rightArrow.addEventListener('click', () => {
        if (currentIndex < gridItems.length - 1) {
            gridItems[currentIndex + 1].click();
        }
    });
});

























// ______________SORTING_______________
document.addEventListener("DOMContentLoaded", function() {
    let sortOrder = 1; // Initial sort order (1 for ascending, -1 for descending)

    document.getElementById("sortButton").addEventListener("click", function() {
        // Get the selected sorting option
        const sortBy = document.getElementById("sortDropdown").value;
        // Toggle sort order
        sortOrder *= -1;
        // Sort the grid items based on the current sort order and selected option
        sortGridItems(sortOrder, sortBy);
    });

    // Function to sort grid items
    function sortGridItems(order, sortBy) {
        const gridContainer = document.querySelector('.grid-container');
        const itemsArray = Array.from(gridContainer.children);
        
        itemsArray.sort((a, b) => {
            let valueA, valueB;
            if (sortBy === 'Title') {
                valueA = a.querySelector('h2').textContent.trim().toLowerCase();
                valueB = b.querySelector('h2').textContent.trim().toLowerCase();
            } else if (sortBy === 'Author') {
                valueA = a.querySelector('p:nth-child(3)').textContent.trim().toLowerCase(); // Assuming author is the third <p> element
                valueB = b.querySelector('p:nth-child(3)').textContent.trim().toLowerCase();
            } else if (sortBy === 'ReadFor') {
                valueA = parseInt(a.querySelector('.read-for').textContent.trim()); // Assuming class name for ReadFor paragraph is 'read-for'
                valueB = parseInt(b.querySelector('.read-for').textContent.trim());
            }
            return order * compareValues(valueA, valueB);
        });

        // Reorder the grid items
        itemsArray.forEach(item => gridContainer.appendChild(item));
    }

    // Function to compare values for sorting
    function compareValues(valueA, valueB) {
        if (valueA < valueB) {
            return -1;
        } else if (valueA > valueB) {
            return 1;
        } else {
            return 0;
        }
    }
});