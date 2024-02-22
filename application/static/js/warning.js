var warningContainer = document.querySelector('#warning_container');
var closeButtons = document.querySelectorAll('.exit-button');

if (window.getComputedStyle(warningContainer).display !== 'none') {
    setTimeout(function() {
        warningContainer.style.display = 'none';
    }, 10000);
}

closeButtons.forEach(function(button) {
    button.addEventListener('mouseenter', function() {
        this.style.cursor = 'pointer';
    });
    
    button.addEventListener('mouseleave', function() {
        this.style.cursor = 'default';
    });
    
    button.addEventListener('click', function() {
        var warningItem = this.closest('.warning');
        warningItem.style.display = 'none';
        
        // Verifica se ainda há itens visíveis dentro do warningContainer
        var visibleItems = document.querySelectorAll('.warning:not([style*="display: none"])');
        if (visibleItems.length === 0) {
            warningContainer.style.display = 'none';
        }
    });
});
