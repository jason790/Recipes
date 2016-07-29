"use strict";

import Autosuggest from "react-autosuggest";

console.log(Autosuggest);
console.log(Autosuggest);

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
    <SubscriptionFormComponent name="" email="" url="/api/v1/subscribers/create.json" />,
    widgetSubscriptionForm
  );
}

var SearchFormComponent = React.createClass({
  getInitialState(){
    return {
      disabled: false,
      term: this.props.term,
      submit: "Search",
      value: "search",
    };
  },
  handleTermChange(e){
    this.setState({
      term: e.target.value
    })
  },
  getSearches(){
    return [
      "Name",
      "Name 2",
      "Recipes",
      "Healthy",
      "Vegan",
      "Fruits",
    ];
  },
  matchSearchToTerm(){
    return true;
  },
  sortSearches(){
    return getSearches();
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
      submit: "Sending...",
      url: this.props.url
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
      "searchInput": "Type something",
      "value": "Type something to search",
      submit: "Sent"
    });

  },
  render: function(){
    return <div className="search-form">
      <form action={this.state.url} itemprop="potentialAction"
        itemscope itemtype="http://schema.org/SearchAction"
        onSubmit={this.handleSubmittion}>
        <fieldset>
          <label htmlFor="q">Search The Website</label>
          <input
            type="text"
            name="q"
            ref="value"
            value={this.state.value}
            onChange={(event, value) => this.setState({ value })}
            onSelect={value => this.setState({ value })}
            id="q"
            autocomplete="off"
            placeholder="Healthy, sweet, etc."
            maxlength="40"
            itemprop="query-input"
          />
          <button type="submit" name="submit">Search</button>
        </fieldset>
        <fieldset>
        <Autosuggest suggestions={getSearches}
                   onSuggestionsUpdateRequested={this.onSuggestionsUpdateRequested}
                   getSuggestionValue={getSearches}
                   renderSuggestion={renderSuggestion}
                   inputProps={inputProps} />
        </fieldset>
      </form>

    </div>
  }
});

// render
var SearchForm = document.getElementById("SearchForm");
if (!!SearchForm){
  ReactDOM.render(
    <SearchFormComponent term="" url="/search" />,
    SearchForm
  );
}

// The program enrollment form
var widgetProgramEnrollmentFormComponent = React.createClass({
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
  render(){
    return (
      <div>

      </div>
    );
  }
});
var widgetProgramEnrollmentForm = document.getElementById("widgetProgramEnrollmentForm");
if (!!widgetProgramEnrollmentForm){
  ReactDOM.render(
    <widgetProgramEnrollmentFormComponent />,
    widgetProgramEnrollmentForm
  );
}
