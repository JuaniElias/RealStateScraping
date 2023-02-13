const popper = window.popper;

import { createPopper } from "@popper";
const popcorn = document.querySelector('#map');
const tooltip = document.querySelector('#tooltip');

createPopper(popcorn, tooltip, {
  placement: 'right',
});