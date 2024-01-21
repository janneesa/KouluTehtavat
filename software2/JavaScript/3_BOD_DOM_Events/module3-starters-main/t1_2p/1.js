const div = document.querySelector('#target');
const html =
    `<li>First item</li>
     <li>Second item</li>
     <li>Third item</li>`;
div.innerHTML = html;

// Lisätään luokka "my_list" div-elementille
document.querySelector('#target').classList.add('my-list');
