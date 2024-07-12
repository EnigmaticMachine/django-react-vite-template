import React, { useState } from 'react';
import { View, TextInput, StyleSheet, Pressable, Text, Alert, ScrollView } from 'react-native';
import { useRouter } from 'expo-router';

export default function Signup() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const handleSignup = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/signup/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          username,
          email,
          password1,
          password2,
        }),
      });

      const data = await response.json();

      if (response.status === 201) {
        // Signup successful
        Alert.alert('Success', 'User registered and logged in successfully');
        router.replace({ pathname: '/', params: { isLoggedIn: true } });
      } else {
        // Signup failed
        let errorMessage = 'Signup failed';
        if (data.errors) {
          errorMessage = Object.entries(data.errors)
            .map(([key, value]) => `${key}: ${value.join(', ')}`)
            .join('\n');
        }
        Alert.alert('Signup Failed', errorMessage);
      }
    } catch (error) {
      console.error('Signup error:', error);
      Alert.alert('Error', 'An error occurred while signing up');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={email}
        onChangeText={setEmail}
        keyboardType="email-address"
        autoCapitalize="none"
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        value={password1}
        onChangeText={setPassword1}
        secureTextEntry
      />
      <TextInput
        style={styles.input}
        placeholder="Confirm Password"
        value={password2}
        onChangeText={setPassword2}
        secureTextEntry
      />
      <Pressable
        style={[styles.button, isLoading && styles.buttonDisabled]}
        onPress={handleSignup}
        disabled={isLoading}
      >
        <Text style={styles.buttonText}>
          {isLoading ? 'Signing up...' : 'Sign Up'}
        </Text>
      </Pressable>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    justifyContent: 'center',
    padding: 20,
    backgroundColor: '#25292e',
  },
  input: {
    backgroundColor: 'white',
    paddingHorizontal: 15,
    paddingVertical: 10,
    borderRadius: 5,
    marginBottom: 10,
  },
  button: {
    backgroundColor: '#ffd33d',
    padding: 15,
    borderRadius: 18,
    alignItems: 'center',
  },
  buttonDisabled: {
    backgroundColor: '#cccccc',
  },
  buttonText: {
    color: '#25292e',
    fontWeight: 'bold',
  },
});
