import React from 'react';
import FileUpload from '../components/FileUpload';
import styles from '../styles/Home.module.css';

const Home: React.FC = () => {
    return (
        <div className={styles.container}>
            <FileUpload />
        </div>
    );
};

export default Home;
