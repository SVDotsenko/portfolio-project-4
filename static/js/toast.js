const Toast = {
    toast: document.getElementById('liveToast'),
    setToastMessage(message) {
        Array.from(document.getElementsByClassName('toast-body')).forEach(e => e.innerText = message);
    },
    setToastColor: {
        RED() {
            Toast.toast.classList.remove('text-bg-success', 'text-bg-warning');
            Toast.toast.classList.add('text-bg-danger');
        },
        YELLOW() {
            Toast.toast.classList.remove('text-bg-success', 'text-bg-danger');
            Toast.toast.classList.add('text-bg-warning');
        },
        GREEN() {
            Toast.toast.classList.remove('text-bg-danger', 'text-bg-warning');
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