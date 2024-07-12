import React from 'react';
import { View, Text, Pressable, StyleSheet } from 'react-native';
import { useRouter, useLocalSearchParams } from 'expo-router';

export default function Home() {
  const router = useRouter();
  const { isLoggedIn } = useLocalSearchParams();

  const handleLogout = () => {
    // Here you would typically make an API call to log out
    router.replace({ pathname: '/', params: { isLoggedIn: false } });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Template</Text>
      {isLoggedIn === 'true' ? (
        <Pressable style={styles.button} onPress={handleLogout}>
          <Text style={styles.buttonText}>Logout</Text>
        </Pressable>
      ) : (
        <View style={styles.buttonContainer}>
          <Pressable style={styles.button} onPress={() => router.push('/login')}>
            <Text style={styles.buttonText}>Login</Text>
          </Pressable>
          <Pressable style={styles.button} onPress={() => router.push('/signup')}>
            <Text style={styles.buttonText}>Sign Up</Text>
          </Pressable>
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#25292e',
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#ffffff',
    marginBottom: 20,
  },
  buttonContainer: {
    width: '80%',
    marginTop: 20,
  },
  button: {
    backgroundColor: '#ffd33d',
    borderRadius: 18,
    padding: 15,
    alignItems: 'center',
    marginBottom: 10,
    width: '80%',
  },
  buttonText: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#25292e',
  },
});
