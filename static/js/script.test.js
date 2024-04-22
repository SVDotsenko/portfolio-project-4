/**
 * @jest-environment jsdom
 */

const {validateInput, previewImage} = require('./script.js');

global.document.getElementById = jest.fn();
global.FileReader = jest.fn(() => ({
    readAsDataURL: jest.fn(),
    onload: null,
}));


describe('validateInput', () => {
    test('should validate input correctly', () => {
        const mockInput = {
            value: 'test',
            classList: {
                add: jest.fn(),
                remove: jest.fn(),
            },
        };
        const mockButton = {
            disabled: false,
        };
        document.getElementById.mockReturnValueOnce(mockInput).mockReturnValueOnce(mockButton);
        validateInput();
        expect(mockInput.classList.add).toHaveBeenCalledWith('is-valid');
        expect(mockInput.classList.remove).toHaveBeenCalledWith('is-invalid');
        expect(mockButton.disabled).toBe(false);
    });
    test('should handle invalid input correctly', () => {
        const mockInput = {
            value: '123',
            classList: {
                add: jest.fn(),
                remove: jest.fn(),
            },
        };
        const mockButton = {
            disabled: false,
        };
        document.getElementById.mockReturnValueOnce(mockInput).mockReturnValueOnce(mockButton);
        validateInput();
        expect(mockInput.classList.add).toHaveBeenCalledWith('is-invalid');
        expect(mockInput.classList.remove).toHaveBeenCalledWith('is-valid');
        expect(mockButton.disabled).toBe(true);
    });
});

describe('previewImage', () => {
    test('should preview image correctly', done => {

        const mockEvent = {
            target: {
                files: ['test'],
            },
        };
        const mockSubmit = {
            classList: {
                add: jest.fn(),
                remove: jest.fn(),
            },
            focus: jest.fn(),
        };
        document.getElementById.mockReturnValueOnce(mockSubmit);
        previewImage(mockEvent);
        expect(FileReader).toHaveBeenCalled();
        setTimeout(() => {
            expect(mockSubmit.classList.add).toHaveBeenCalledWith('btn-warning');
            expect(mockSubmit.classList.remove).toHaveBeenCalledWith('btn-primary');
            done();
        }, 1000);
    });
});