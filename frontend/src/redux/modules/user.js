
// import

// actions

const SAVE_TOKEN = "SAVE_TOKEN";
const LOGOUT = "LOGOUT";
const SET_USER_LIST = "SET_USER_LIST";
const FOLLOW_USER = "FOLLOW_USER";
const UNFOLLOW_USER = "UNFOLLOW_USER";
const SET_IMAGE_LIST = "SET_IMAGE_LIST";

// action creators

function saveToken(token) {
  return {
    type: SAVE_TOKEN,
    token
  };
}

// API actions

function usernameLogin(username, password) {
  return dispatch => {
    fetch("/rest-auth/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password
      })
    })
      .then(response => response.json())
      .then(json => {
        if (json.token) {
          dispatch(saveToken(json.token));
        }
      })
      .catch(err => console.log(err));
  };
}

function createAccount(username, password, email, name) {
  return dispatch => {
    fetch("/rest-auth/registration/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        password1: password,
        password2: password,
        email,
        name
      })
    })
      .then(response => response.json())
      .then(json => {
        if (json.token) {
          dispatch(saveToken(json.token));
        }
      })
      .catch(err => console.log(err));
  };
}


// initial state

const initialState = {
    isLoggedIn: localStorage.getItem("jwt") || false
};

// reducer

function reducer(state = initialState, action){
    switch(action.type) {
        default:
            return state;
    }
}
// reducer fuctions

// exports

const actionCreators = {
  usernameLogin,
  createAccount
};

export { actionCreators };

// reducer export

export default reducer;
