const getClassFromMessageTags = {
    'debug': 'text-bg-secondary',
    'info': 'text-bg-info',
    'success': 'text-bg-success',
    'warning': 'text-bg-warning',
    'error': 'text-bg-danger'
};

const Toast = {
    toast: null,
    setMessage(message) {
        Array.from(document.getElementsByClassName('toast-body')).forEach(e => e.innerText = message);
    },
    removePreviousColor() {
        Array.from(Toast.toast.classList).forEach(className => {
            if (className.startsWith('text-bg-')) {
                Toast.toast.classList.remove(className);
            }
        });
    },
    setColor: {
        danger() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-danger');
        },
        warning() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-warning');
        },
        success() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-success');
        },
        secondary() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-secondary');
        }
    },
    setColorFromMessageTags() {
        const messageTags = document.getElementsByClassName('message-tags')[0].innerText;
        Toast.removePreviousColor();
        Toast.toast.classList.add(getClassFromMessageTags[messageTags]);
    },
    show(seconds, setDefaultColor = false) {
        if (setDefaultColor) {
            Toast.setColorFromMessageTags();
        }
        new bootstrap.Toast(Toast.toast, {
            animation: true,
            autohide: true,
            delay: seconds * 1000
        }).show();
    }
};

document.addEventListener('DOMContentLoaded', () => {
    Toast.toast = document.getElementById('liveToast');
    if (document.getElementsByClassName('toast-body')[0]?.innerText.trim().length) {
        Toast.show(3, true);
    }
});