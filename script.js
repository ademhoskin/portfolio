//Waits for page to load before executing
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('nav ul li a');

    //Click event listener for the nav bar links
    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            // prevent default behaviour
            e.preventDefault();
            //get id of link target element
            const targetId = e.target.getAttribute('href');
            //select target using received id
            const targetElement = document.querySelector(targetId);

            //Scroll to target using smooth animation, uses offset of 100 to go to heading
            window.scrollTo({
                top: targetElement.offsetTop - 100,
                behavior: 'smooth'
            });
        });
    });
});
