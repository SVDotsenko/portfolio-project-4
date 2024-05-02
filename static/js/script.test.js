/**
 * @fileoverview Unit tests for script.js
 * @jest-environment jsdom
 */

const {validateInput, previewImage} = require('./script.js');

global.document.getElementById = jest.fn();
global.FileReader = jest.fn(() => ({
    readAsDataURL: jest.fn(),
    onload: null,
}));

global.Toast = {
    params: {},
    show: jest.fn(),
};

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


jest.useFakeTimers();

describe('previewImage', () => {
    test('should preview image correctly', () => {

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
        jest.runAllTimers();

        expect(mockSubmit.classList.add).toHaveBeenCalledWith('btn-warning');
        expect(mockSubmit.classList.remove).toHaveBeenCalledWith('btn-primary');
    });
});