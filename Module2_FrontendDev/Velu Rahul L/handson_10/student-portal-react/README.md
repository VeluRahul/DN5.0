# Student Portal

Digital Nurture 5.0

Module 2

Hands-On 10

---

## API Layer

A centralized Axios client was created.

Files

- apiClient.js
- courseApi.js

Advantages

- Single Base URL
- Authorization Header
- Response Interceptors
- Request Interceptors
- Standard Error Handling

---

## Redux Toolkit

Implemented using

- configureStore
- createSlice
- createAsyncThunk
- Selectors

Advantages

- Centralized State
- Async API Handling
- Loading State
- Error State

---

## Global Error Handling

Implemented using React Error Boundary.

Fallback UI appears whenever an unexpected runtime error occurs.

---

## NgRx Concept

Component

↓

Dispatch Action

↓

Effect

↓

API Call

↓

Reducer

↓

Store

↓

Selector

↓

Component

---

## Pinia Advanced Pattern

Implemented Concepts

- defineStore()
- Async Actions
- Store Reset
- storeToRefs()

---

## State Management Comparison

### React + Redux Toolkit

Advantages

- Easy Async Handling
- Huge Community
- Redux DevTools

Disadvantages

- Slight Boilerplate

---

### Angular + NgRx

Advantages

- Enterprise Ready
- Predictable
- Excellent for Large Apps

Disadvantages

- Steeper Learning Curve

---

### Vue + Pinia

Advantages

- Minimal Boilerplate
- Very Easy to Learn
- Excellent Reactivity

Disadvantages

- Smaller Ecosystem Compared to Redux

---

## Conclusion

Redux Toolkit is ideal for React.

NgRx is ideal for enterprise Angular applications.

Pinia is lightweight and best suited for Vue applications.
