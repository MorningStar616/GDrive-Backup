import React, { useState, ChangeEvent } from 'react';
import axios from 'axios';
import styles from '../styles/FileUpload.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faFileAlt } from '@fortawesome/free-solid-svg-icons';

const FileUpload: React.FC = () => {
    const [file, setFile] = useState<File | null>(null);
    const [message, setMessage] = useState<string>('');
    const [error, setError] = useState<string>('');

    const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
        if (e.target.files) {
            setFile(e.target.files[0]);
            setMessage(''); // Clear any previous message
            setError(''); // Clear any previous error
        }
    };

    const handleUpload = async () => {
        if (!file) {
            setError('Please select a file first.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await axios.post('http://localhost:5000/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            if (response.data.error) {
                setError(response.data.error);
            } else {
                setMessage(response.data.message);
            }
        } catch (error) {
            setError('Error uploading file.');
        }
    };

    return (
        <div className={styles.uploadContainer}>
            <h1 className={styles.uploadTitle}>GDrive-Backup</h1>
            <div className={styles.uploadBox} onClick={() => document.getElementById('fileInput')?.click()}>
                <input id="fileInput" type="file" onChange={handleFileChange} />
                <p>Drag & drop a file here or click to select a file</p>
                {file && (
                    <div className={styles.fileInfo}>
                        <FontAwesomeIcon icon={faFileAlt} />
                        <p>{file.name}</p>
                    </div>
                )}
            </div>
            <button className={styles.uploadButton} onClick={handleUpload}>Upload</button>
            {message && <p className={styles.message}>{message}</p>}
            {error && <p className={styles.error}>{error}</p>}
        </div>
    );
};

export default FileUpload;
