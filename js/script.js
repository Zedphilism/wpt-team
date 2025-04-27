// Random background image changer
document.addEventListener('DOMContentLoaded', function() {
  const backgrounds = [
    'images/background1.webp',
    'images/background2.webp'
  ];

  const randomImage = backgrounds[Math.floor(Math.random() * backgrounds.length)];
  document.body.style.backgroundImage = `url('${randomImage}')`;
});

