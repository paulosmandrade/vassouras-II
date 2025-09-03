//document.querySelector('.toast').style.display='none';
var toastElement = document.querySelector('.toast');
if (toastElement) {
    toastElement.style.display = 'none';
}

 const toastDetails = {
    timer: 5000,
    success: { icon: 'fa-circle-check' },
    error: { icon: 'fa-circle-xmark' },
    warning: { icon: 'fa-triangle-exclamation' },
    info: { icon: 'fa-circle-info' }
};


const notifications = document.querySelector(".notifications");

const removeToast = (toast) => {
    toast.classList.add("hide");
    if (toast.timeoutId) clearTimeout(toast.timeoutId);
    setTimeout(() => toast.remove(), 500);
};

const createToast = (tipo, message) => {
    if (!toastDetails[tipo]) {
        console.warn(`Tipo '${tipo}' não encontrado em toastDetails_login. Usando 'info' como padrão.`);
        tipo = 'info'; // Define 'info' como fallback
    }
    const { icon } = toastDetails[tipo];
    const toast = document.createElement("li");
    toast.className = `toast ${tipo}`;
    toast.innerHTML = `<div class="column">
                          <i class="fa-solid ${icon}"></i>
                          <span>${message}</span>
                      </div>
                      <i class="fa-solid fa-xmark" onclick="removeToast(this.parentElement)"></i>`;
    notifications.appendChild(toast);
    toast.timeoutId = setTimeout(() => removeToast(toast), toastDetails.timer);
};

// Seleciona todos os elementos .toast e cria as notificações
const toasts = document.querySelectorAll(".toast");
toasts.forEach(toast => {
    const category = toast.getAttribute("data-category");
    const message = toast.getAttribute("data-message");
    if ((category != '') & (message != '')){
      createToast(category, message);
    }
    
});