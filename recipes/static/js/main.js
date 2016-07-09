"use strict";

// menu

var NavigationMenu = React.createClass({
  displayName: "NavigationMenu",

  getInitialState: function getInitialState() {
    return {
      opened: false,
      menu: "closed"
    };
  },
  handleClick: function handleClick() {
    var menuState = !this.state.opened ? "opened" : "closed";

    // handle menu element
    document.getElementById("top").className = "navbar " + menuState;

    this.setState({
      opened: !this.state.opened,
      menu: menuState
    });
  },
  render: function render() {
    var text = this.state.opened ? "opened" : "closed";
    return React.createElement(
      "button",
      { onClick: this.handleClick, className: this.state.menu },
      React.createElement(
        "i",
        { className: "fa fa-bars", "aria-hidden": "true" },
        " "
      )
    );
  }
});

var topMenuToggle = document.getElementById("topMenuToggle");
if (topMenuToggle) {
  ReactDOM.render(React.createElement(NavigationMenu, null), topMenuToggle);
}

// subscription
var SubscriptionFormComponent = React.createClass({
  displayName: "SubscriptionFormComponent",

  getInitialState: function getInitialState() {
    return {
      disabled: false,
      name: this.props.name,
      email: this.props.email,
      submit: "Subscribe",
      url: this.props.url
    };
  },
  handleNameChange: function handleNameChange(e) {
    this.setState({
      name: e.target.value
    });
  },
  handleEmailChange: function handleEmailChange(e) {
    this.setState({
      email: e.target.value
    });
  },
  handleSubmittion: function handleSubmittion(e) {
    e.preventDefault();
    var name = this.state.name.trim();
    var email = this.state.email.trim();

    // make sure all the field are filled out
    if (!name || !email) {
      return false;
    }
    this.setState({
      submit: "Sending..."
    });

    // send request
    $.ajax({
      url: this.props.url,
      dataType: "json",
      // cache: false,
      method: "POST",
      data: {
        name: name,
        email: email
      },
      success: function success(data) {},
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
    this.setState({
      name: "",
      email: "",
      submit: "Sent"
    });
  },
  render: function render() {
    return React.createElement(
      "div",
      null,
      React.createElement(
        "h3",
        { "class": "title" },
        "Subscribe To Our Newsletter"
      ),
      React.createElement(
        "p",
        null,
        "Recieve new recipes to your inbox and get notified when there is something good that happens."
      ),
      React.createElement(
        "form",
        { url: this.state.url, onSubmit: this.handleSubmittion },
        React.createElement(
          "fieldset",
          null,
          React.createElement(
            "div",
            { "class": "field" },
            React.createElement("input", { type: "text", placeholder: "Full name",
              "class": "control", disabled: false,
              value: this.state.name, onChange: this.handleNameChange })
          ),
          React.createElement(
            "div",
            { "class": "field" },
            React.createElement("input", { type: "email", placeholder: "username@email.com",
              "class": "control", disabled: false,
              value: this.state.email, onChange: this.handleEmailChange })
          ),
          React.createElement(
            "div",
            { "class": "actions" },
            React.createElement("input", { type: "submit", value: this.state.submit })
          )
        )
      )
    );
  }
});

// render
var widgetSubscriptionForm = document.getElementById("widgetSubscriptionForm");
if (!!widgetSubscriptionForm) {
  ReactDOM.render(React.createElement(SubscriptionFormComponent, { name: "", email: "", url: "/api/v1/subscribers/create.json" }), widgetSubscriptionForm);
}

var SearchFormComponent = React.createClass({
  displayName: "SearchFormComponent",
  getInitialState: function getInitialState() {
    return {
      disabled: false,
      term: this.props.term,
      submit: "Search"
    };
  },
  handleTermChange: function handleTermChange(e) {
    this.setState({
      term: e.target.value
    });
  },
  handleSubmittion: function handleSubmittion(e) {
    e.preventDefault();
    var name = this.state.name.trim();
    var email = this.state.email.trim();

    // make sure all the field are filled out
    if (!name || !email) {
      return false;
    }
    this.setState({
      submit: "Sending..."
    });

    // send request
    $.ajax({
      url: this.props.url,
      dataType: "json",
      // cache: false,
      method: "POST",
      data: {
        name: name,
        email: email
      },
      success: function success(data) {},
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
    this.setState({
      name: "",
      email: "",
      submit: "Sent"
    });
  },

  render: function render() {
    return React.createElement(
      "div",
      null,
      React.createElement(
        "h3",
        { "class": "title" },
        "Subscribe To Our Newsletter"
      ),
      React.createElement(
        "p",
        null,
        "Recieve new recipes to your inbox and get notified when there is something good that happens."
      ),
      React.createElement(
        "form",
        { url: this.state.url, onSubmit: this.handleSubmittion },
        React.createElement(
          "fieldset",
          null,
          React.createElement(
            "div",
            { "class": "field" },
            React.createElement("input", { type: "text", placeholder: "Full name",
              "class": "control", disabled: false,
              value: this.state.name, onChange: this.handleNameChange })
          ),
          React.createElement(
            "div",
            { "class": "field" },
            React.createElement("input", { type: "email", placeholder: "username@email.com",
              "class": "control", disabled: false,
              value: this.state.email, onChange: this.handleEmailChange })
          ),
          React.createElement(
            "div",
            { "class": "actions" },
            React.createElement("input", { type: "submit", value: this.state.submit })
          )
        )
      )
    );
  }
});

// render
var SearchForm = document.getElementById("SearchForm1");
if (!!SearchForm) {
  ReactDOM.render(React.createElement(SearchFormComponent, { term: "", url: "/search" }), SearchForm);
}

// The program enrollment form
var widgetProgramEnrollmentFormComponent = React.createClass({
  displayName: "widgetProgramEnrollmentFormComponent",
  handleSubmittion: function handleSubmittion(e) {
    e.preventDefault();
    var name = this.state.name.trim();
    var email = this.state.email.trim();

    // make sure all the field are filled out
    if (!name || !email) {
      return false;
    }
    this.setState({
      submit: "Sending..."
    });

    // send request
    $.ajax({
      url: this.props.url,
      dataType: "json",
      // cache: false,
      method: "POST",
      data: {
        name: name,
        email: email
      },
      success: function success(data) {},
      error: function (xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
    this.setState({
      name: "",
      email: "",
      submit: "Sent"
    });
  },
  render: function render() {
    return React.createElement("div", null);
  }
});
var widgetProgramEnrollmentForm = document.getElementById("widgetProgramEnrollmentForm");
if (!!widgetProgramEnrollmentForm) {
  ReactDom.render(React.createElement("widgetProgramEnrollmentFormComponent", null), widgetProgramEnrollmentForm);
}
//# sourceMappingURL=main.js.map
