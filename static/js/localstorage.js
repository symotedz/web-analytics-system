// Sample JavaScript code for storing data in IndexedDB
const dbPromise = idb.openDB('my-database', 1, {
    upgrade(db) {
        db.createObjectStore('userData', { keyPath: 'id' });
    },
});

// Save data to IndexedDB
async function saveUserData(user) {
    const db = await dbPromise;
    const tx = db.transaction('userData', 'readwrite');
    const store = tx.objectStore('userData');
    await store.put(user);
}

// Retrieve data from IndexedDB
async function getUserData() {
    const db = await dbPromise;
    const tx = db.transaction('userData', 'readonly');
    const store = tx.objectStore('userData');
    return store.get(1);
}
