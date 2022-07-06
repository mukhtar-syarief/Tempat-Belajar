// Give the service worker access to Firebase Messaging.
// Note that you can only use Firebase Messaging here. Other Firebase libraries
// are not available in the service worker.
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing in
// your app's Firebase config object.
// https://firebase.google.com/docs/web/setup#config-object
firebase.initializeApp({
  apiKey: "AIzaSyAUiwsMmiL7i-4Rc5rKdPDqofZaTwaGSgw",
  authDomain: "shopeepdc.firebaseapp.com",
  projectId: "shopeepdc",
  storageBucket: "shopeepdc.appspot.com",
  messagingSenderId: "965437735150",
  appId: "1:965437735150:web:998128ede86088c500f3ff",
  measurementId: "G-SEKXGDXY48"
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();

// Handle incoming messages. Called when:
// - a message is received while the app has focus
// - the user clicks on an app notification created by a service worker
//   `messaging.onBackgroundMessage` handler.
// messaging.onMessage((payload) => {
//     console.log('Message received. ', payload);
// });