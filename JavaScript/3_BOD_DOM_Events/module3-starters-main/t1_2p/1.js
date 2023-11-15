
const div = document.querySelector('#target');
const html =
    `<li>First item</li>
     <li>Second item</li>
     <li>Third item</li>`;
div.innerHTML = html;
document.querySelector('#target').classList.toggle('my_list');
