const loginContainer = document.getElementById('login-container');
const appContainer = document.getElementById('app-container');
const loginForm = document.getElementById('login-form');
const loginError = document.getElementById('login-error');

const chatWindow = document.getElementById('chat-window');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

// URL do Webhook do n8n
const N8N_WEBHOOK_URL = 'https://n8n.artvida.com.br/webhook/prod-cadastro';

// Verificar se já está logado
if (localStorage.getItem('isLogged') === 'true') {
    showApp();
}

function showApp() {
    loginContainer.classList.add('hidden');
    appContainer.classList.remove('hidden');
}

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: user, password: pass })
        });

        if (response.ok) {
            localStorage.setItem('isLogged', 'true');
            showApp();
        } else {
            loginError.classList.remove('hidden');
            setTimeout(() => {
                loginError.classList.add('hidden');
            }, 3000);
        }
    } catch (err) {
        console.error("Erro ao autenticar", err);
        alert("Erro de conexão com o servidor local.");
    }
});

// Lógica do Chat
function addMessage(text, sender) {
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('message', sender);
    msgDiv.innerHTML = `<div class="content">${text}</div>`;
    chatWindow.appendChild(msgDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, 'user');
    userInput.value = '';

    try {
        const response = await fetch(N8N_WEBHOOK_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                message: message,
                user: 'Issai',
                source: 'central-artvida'
            })
        });

        if (response.ok) {
            const data = await response.json();
            const reply = data.output || "Comando recebido, Issai! Processando no n8n...";
            addMessage(reply, 'system');
        } else {
            addMessage("Erro ao falar com o cérebro n8n.", 'system');
        }
    } catch (error) {
        addMessage("Erro de conexão com o n8n.", 'system');
    }
});
