function toggleSidebar() {
    const el = document.getElementById('sidebar');
    el.classList.toggle('-translate-x-full');
    }
    
    
    // small helper for language switch to submit the form
    function submitLang(formId){ document.getElementById(formId).submit(); }