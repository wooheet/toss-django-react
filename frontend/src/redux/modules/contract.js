
// actions

const SAVE_TOKEN = "SAVE_TOKEN";

// action creators

function saveToken(token) {
  return {
    type: SAVE_TOKEN,
    token
  };
}

// API actions

function usernameLogin(username, email) {
  return function(dispatch) {
    fetch("/contracts/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        username,
        email
      })
    })
      .then(response => response.json())
      .then(json => {
        console.log(json)
        if (json.status_code === 200) {
          dispatch(saveToken(json.status_code));
        }
      })
      .catch(err => console.log(err));
  };
}

// initial state

const initialState = {
  isLoggedIn: !!localStorage.getItem("jwt")
};

// reducer

function reducer(state = initialState, action) {
  switch (action.type) {
    case SAVE_TOKEN:
      return applySetToken(state, action);
    default:
      return state;
  }
}

// reducer functions

function applySetToken(state, action) {
  const { token } = action;
  localStorage.setItem("jwt", token);
  return {
    ...state,
    isLoggedIn: true,
    token: token
  };
}

// exports

const actionCreators = {
  usernameLogin
};

export { actionCreators };

// export reducer by default

export default reducer;
