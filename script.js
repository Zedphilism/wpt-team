// Random background image changer
document.addEventListener('DOMContentLoaded', function() {
  const backgrounds = [
    'images/background1.jpg',
    'images/background2.jpg'
  ];

  const randomImage = backgrounds[Math.floor(Math.random() * backgrounds.length)];
  document.body.style.backgroundImage = `url('${randomImage}')`;
});
