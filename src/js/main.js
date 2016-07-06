"use strict";

// menu
var NavigationMenu = React.createClass({
  getInitialState: function(){
    return {
      opened: false,
      menu: "closed"
    }
  },
  handleClick: function(){
    const menuState = !this.state.opened ? "opened" : "closed"

    // handle menu element
    document.getElementById("top").className = "navbar "+menuState;

    this.setState({
      opened: !this.state.opened,
      menu: menuState
    })
  },
  render: function(){
    const text = this.state.opened ? "opened" : "closed"
    return <button onClick={this.handleClick} className={this.state.menu}>
        <i className="fa fa-bars" aria-hidden="true">&nbsp;</i>
      </button>
  }
});

var topMenuToggle = document.getElementById("topMenuToggle");
if (topMenuToggle){
  ReactDOM.render(
    <NavigationMenu />,
    topMenuToggle
  );
}

// subscription
var SubscriptionFormComponent = React.createClass({
  getInitialState: function(){
    return {
      disabled: false,
      name: this.props.name,
      email: this.props.email,
      submit: "Subscribe",
      url: this.props.url
    };
  },
  handleNameChange: function(e){
    this.setState({
      name: e.target.value
    })
  },
  handleEmailChange: function(e){
    this.setState({
      email: e.target.value
    })
  },
  handleSubmittion: function(e){
    e.preventDefault();
    var name = this.state.name.trim();
    var email = this.state.email.trim();

    // make sure all the field are filled out
    if (!name || !email){
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
      success: function(data){
      },
      error: function(xhr, status, err){
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
    this.setState({
      name: "",
      email: "",
      submit: "Sent"
    });

  },
  render: function(){
    return <div>
      <h3 class="title">Subscribe To Our Newsletter</h3>
      <p>Recieve new recipes to your inbox and get notified when there is something good that happens.</p>
      <form url={this.state.url} onSubmit={this.handleSubmittion}>
        <fieldset>
          <div class="field">
            <input type="text" placeholder="Full name"
            class="control" disabled={false}
            value={this.state.name} onChange={this.handleNameChange} />
          </div>
          <div class="field">
            <input type="email" placeholder="username@email.com"
            class="control" disabled={false}
            value={this.state.email} onChange={this.handleEmailChange} />
          </div>
          <div class="actions">
            <input type="submit" value={this.state.submit} />
          </div>
        </fieldset>
      </form>
    </div>
  }
});

// render
var widgetSubscriptionForm = document.getElementById("widgetSubscriptionForm");
if (!!widgetSubscriptionForm){
  ReactDOM.render(
    <SubscriptionFormComponent name="" email="" url="/v1/api/subscribers/create.json" />,
    widgetSubscriptionForm
  );
}

var SearchFormComponent = React.createClass({
  getInitialState(){
    return {
      disabled: false,
      term: this.props.term,
      submit: "Search"
    };
  },
  handleTermChange(e){
    this.setState({
      term: e.target.value
    })
  },
  handleSubmittion(e){
    e.preventDefault();
    var name = this.state.name.trim();
    var email = this.state.email.trim();

    // make sure all the field are filled out
    if (!name || !email){
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
      success: function(data){
      },
      error: function(xhr, status, err){
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
    this.setState({
      name: "",
      email: "",
      submit: "Sent"
    });

  },
  render: function(){
    return <div>
      <h3 class="title">Subscribe To Our Newsletter</h3>
      <p>Recieve new recipes to your inbox and get notified when there is something good that happens.</p>
      <form url={this.state.url} onSubmit={this.handleSubmittion}>
        <fieldset>
          <div class="field">
            <input type="text" placeholder="Full name"
            class="control" disabled={false}
            value={this.state.name} onChange={this.handleNameChange} />
          </div>
          <div class="field">
            <input type="email" placeholder="username@email.com"
            class="control" disabled={false}
            value={this.state.email} onChange={this.handleEmailChange} />
          </div>
          <div class="actions">
            <input type="submit" value={this.state.submit} />
          </div>
        </fieldset>
      </form>
    </div>
  }
});

// render
var SearchForm = document.getElementById("SearchForm1");
if (!!SearchForm){
  ReactDOM.render(
    <SearchFormComponent term="" url="/search" />,
    SearchForm
  );
}
