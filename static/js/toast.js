const Toast = {
    toast: document.getElementById('liveToast'),
    setToastMessage(message) {
        Array.from(document.getElementsByClassName('toast-body')).forEach(e => e.innerText = message);
    },
    removePreviousColor() {
        Array.from(Toast.toast.classList).forEach(className => {
            if (className.startsWith('text-bg-')) {
                Toast.toast.classList.remove(className);
            }
        });
    },
    setToastColor: {
        RED() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-danger');
        },
        YELLOW() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-warning');
        },
        GREEN() {
            Toast.removePreviousColor();
            Toast.toast.classList.add('text-bg-success');
        }
    },
    showToast(hideAfterSeconds) {
        this.toast.classList.remove('hide');
        this.toast.classList.add('show');
        setTimeout(() => {
            this.toast.classList.remove('show');
            this.toast.classList.add('hide');
        }, hideAfterSeconds * 1000);
    },
    init(hideAfterSeconds) {
        document.addEventListener('DOMContentLoaded', () => {
            if (document.getElementsByClassName('toast-body')[0]?.innerText.trim().length) {
                this.showToast(hideAfterSeconds);
            }
        });
    }
};

Toast.init(3);