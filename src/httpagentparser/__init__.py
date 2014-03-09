




<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>httpagentparser/httpagentparser/__init__.py at master · shon/httpagentparser</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <meta property="fb:app_id" content="1401488693436528"/>

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="shon/httpagentparser" name="twitter:title" /><meta content="httpagentparser - Python HTTP Agent Parser" name="twitter:description" /><meta content="https://1.gravatar.com/avatar/cbdba8e11c1e7b81860385f85416622a?d=https%3A%2F%2Fidenticons.github.com%2Fb50503d74eabfc85e8ca27bb81b6d36f.png&amp;r=x&amp;s=400" name="twitter:image:src" />
<meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://1.gravatar.com/avatar/cbdba8e11c1e7b81860385f85416622a?d=https%3A%2F%2Fidenticons.github.com%2Fb50503d74eabfc85e8ca27bb81b6d36f.png&amp;r=x&amp;s=400" property="og:image" /><meta content="shon/httpagentparser" property="og:title" /><meta content="https://github.com/shon/httpagentparser" property="og:url" /><meta content="httpagentparser - Python HTTP Agent Parser" property="og:description" />

    <meta name="hostname" content="github-fe136-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 2.1.0p0-github-tcmalloc (87c9373a41) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="62F7265B:1E89:82EB39D:531CBA23" name="octolytics-dimension-request_id" /><meta content="677594" name="octolytics-actor-id" /><meta content="Offbeatmammal" name="octolytics-actor-login" /><meta content="bc9d491a441da6dd116fa5359365088213ff4e6c313ec3cf567ec792f0808fdd" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="Bn5SRQN6rt2KE/PEAOYyqkIPMfMCC3/rdnMBe8H628o=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-d648f1196659f589579aa6aaddcc78c4f8e87552.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-32987ede34015d8eaa4618614894d836adf201f6.css" media="all" rel="stylesheet" type="text/css" />
    
    


      <script crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/frameworks-855d68c505f4b08a77e4d991f11cf5d8f43250e2.js" type="text/javascript"></script>
      <script async="async" crossorigin="anonymous" src="https://github.global.ssl.fastly.net/assets/github-e6bd35a239a3a0ab82cd42cd9df317778e5a1270.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="2fe0694ce2393a8db660e33f758021ee">

        <link data-pjax-transient rel='permalink' href='/shon/httpagentparser/blob/4a5096ca7831a0933ef9fb80a5e2f108d4810f87/httpagentparser/__init__.py'>

  <meta name="description" content="httpagentparser - Python HTTP Agent Parser" />

  <meta content="89816" name="octolytics-dimension-user_id" /><meta content="shon" name="octolytics-dimension-user_login" /><meta content="1467339" name="octolytics-dimension-repository_id" /><meta content="shon/httpagentparser" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="1467339" name="octolytics-dimension-repository_network_root_id" /><meta content="shon/httpagentparser" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/shon/httpagentparser/commits/master.atom" rel="alternate" title="Recent Commits to httpagentparser:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production macintosh vis-public page-blob tipsy-tooltips">
    <a href="#start-of-content" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" aria-label="You have no unread notifications" class="notification-indicator tooltipped tooltipped-s" data-gotokey="n">
        <span class="mail-status all-read"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="Offbeatmammal"
      data-repo="shon/httpagentparser"
      data-branch="master"
      data-sha="9c766eba604df96d32c55e9719108eb661a6447e"
  >

    <input type="hidden" name="nwo" value="shon/httpagentparser" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target" role="button" aria-haspopup="true">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container" aria-hidden="true">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="help tooltipped tooltipped-s" aria-label="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/Offbeatmammal" class="name">
        <img alt="Offbeatmammal" class=" js-avatar" data-user="677594" height="20" src="https://avatars3.githubusercontent.com/u/677594?s=140" width="20" /> Offbeatmammal
      </a>
    </li>

    <li class="new-menu dropdown-toggle js-menu-container">
      <a href="#" class="js-menu-target tooltipped tooltipped-s" aria-label="Create new...">
        <span class="octicon octicon-plus"></span>
        <span class="dropdown-arrow"></span>
      </a>

      <div class="new-menu-content js-menu-content">
      </div>
    </li>

    <li>
      <a href="/settings/profile" id="account_settings"
        class="tooltipped tooltipped-s"
        aria-label="Account settings ">
        <span class="octicon octicon-tools"></span>
      </a>
    </li>
    <li>
      <a class="tooltipped tooltipped-s" href="/logout" data-method="post" id="logout" aria-label="Sign out">
        <span class="octicon octicon-log-out"></span>
      </a>
    </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="section-title">
      <span title="shon/httpagentparser">This repository</span>
    </li>
      <li>
        <a href="/shon/httpagentparser/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

        



      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="Bn5SRQN6rt2KE/PEAOYyqkIPMfMCC3/rdnMBe8H628o=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="1467339" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/shon/httpagentparser/watchers">
        9
      </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
        <span class="js-select-button">
          <span class="octicon octicon-eye-watch"></span>
          Watch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for conversations in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  

  <div class="js-toggler-container js-social-container starring-container ">
    <a href="/shon/httpagentparser/unstar"
      class="minibutton with-count js-toggler-target star-button starred"
      aria-label="Unstar this repository" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
    </a>

    <a href="/shon/httpagentparser/star"
      class="minibutton with-count js-toggler-target star-button unstarred"
      aria-label="Star this repository" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star"></span><span class="text">Star</span>
    </a>

      <a class="social-count js-social-count" href="/shon/httpagentparser/stargazers">
        103
      </a>
  </div>

  </li>


        <li>
          <a href="/shon/httpagentparser/fork" class="minibutton with-count js-toggler-target fork-button lighter tooltipped-n" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/shon/httpagentparser/network" class="social-count">26</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/shon" class="url fn" itemprop="url" rel="author"><span itemprop="title">shon</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/shon/httpagentparser" class="js-current-repository js-repo-home-link">httpagentparser</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline js-new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Code">
        <a href="/shon/httpagentparser" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /shon/httpagentparser">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped tooltipped-w" aria-label="Issues">
          <a href="/shon/httpagentparser/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /shon/httpagentparser/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>10</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
        <a href="/shon/httpagentparser/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /shon/httpagentparser/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>1</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped tooltipped-w" aria-label="Wiki">
          <a href="/shon/httpagentparser/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /shon/httpagentparser/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped tooltipped-w" aria-label="Pulse">
        <a href="/shon/httpagentparser/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /shon/httpagentparser/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Graphs">
        <a href="/shon/httpagentparser/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /shon/httpagentparser/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped tooltipped-w" aria-label="Network">
        <a href="/shon/httpagentparser/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /shon/httpagentparser/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


  </div>
</div>

              <div class="only-with-full-nav">
                

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/shon/httpagentparser.git" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/shon/httpagentparser.git" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:shon/httpagentparser.git" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:shon/httpagentparser.git" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/shon/httpagentparser" readonly="readonly">

    <span aria-label="copy to clipboard" class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/shon/httpagentparser" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>

  <a href="http://mac.github.com" data-url="github-mac://openRepo/https://github.com/shon/httpagentparser" class="minibutton sidebar-button js-conduit-rewrite-url">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


                <a href="/shon/httpagentparser/archive/master.zip"
                   class="minibutton sidebar-button"
                   title="Download this repository as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:8fd7f1fc3ce5c8b4bff73094b8f00901 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/shon/httpagentparser/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/shon/httpagentparser/blob/master/httpagentparser/__init__.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/shon/httpagentparser" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">httpagentparser</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/shon/httpagentparser/tree/master/httpagentparser" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">httpagentparser</span></a></span><span class="separator"> / </span><strong class="final-path">__init__.py</strong> <span aria-label="copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="httpagentparser/__init__.py" data-copied-hint="copied!"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


  <div class="commit commit-loader file-history-tease js-deferred-content" data-url="/shon/httpagentparser/contributors/master/httpagentparser/__init__.py">
    Fetching contributors…

    <div class="participation">
      <p class="loader-loading"><img alt="Octocat-spinner-32-eaf2f5" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" /></p>
      <p class="loader-error">Cannot retrieve contributors at this time</p>
    </div>
  </div>

<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
        <span class="meta-divider"></span>
          <span>443 lines (338 sloc)</span>
          <span class="meta-divider"></span>
        <span>11.678 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped tooltipped-w js-conduit-openfile-check"
               href="http://mac.github.com"
               data-url="github-mac://openRepo/https://github.com/shon/httpagentparser?branch=master&amp;filepath=httpagentparser%2F__init__.py"
               aria-label="Open this file in GitHub for Mac"
               data-failed-title="Your version of GitHub for Mac is too old to open this file. Try checking for updates.">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
                <a class="minibutton tooltipped tooltipped-n js-update-url-with-hash"
                   aria-label="Clicking this button will automatically fork this project so you can edit the file"
                   href="/shon/httpagentparser/edit/master/httpagentparser/__init__.py"
                   data-method="post" rel="nofollow">Edit</a>
          <a href="/shon/httpagentparser/raw/master/httpagentparser/__init__.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/shon/httpagentparser/blame/master/httpagentparser/__init__.py" class="button minibutton js-update-url-with-hash">Blame</a>
          <a href="/shon/httpagentparser/commits/master/httpagentparser/__init__.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

            <a class="minibutton danger empty-icon tooltipped tooltipped-s"
               href="/shon/httpagentparser/delete/master/httpagentparser/__init__.py"
               aria-label="Fork this project and delete file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">

          Delete
        </a>
      </div><!-- /.actions -->
    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff tab-size-8">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>
<span id="L82" rel="#L82">82</span>
<span id="L83" rel="#L83">83</span>
<span id="L84" rel="#L84">84</span>
<span id="L85" rel="#L85">85</span>
<span id="L86" rel="#L86">86</span>
<span id="L87" rel="#L87">87</span>
<span id="L88" rel="#L88">88</span>
<span id="L89" rel="#L89">89</span>
<span id="L90" rel="#L90">90</span>
<span id="L91" rel="#L91">91</span>
<span id="L92" rel="#L92">92</span>
<span id="L93" rel="#L93">93</span>
<span id="L94" rel="#L94">94</span>
<span id="L95" rel="#L95">95</span>
<span id="L96" rel="#L96">96</span>
<span id="L97" rel="#L97">97</span>
<span id="L98" rel="#L98">98</span>
<span id="L99" rel="#L99">99</span>
<span id="L100" rel="#L100">100</span>
<span id="L101" rel="#L101">101</span>
<span id="L102" rel="#L102">102</span>
<span id="L103" rel="#L103">103</span>
<span id="L104" rel="#L104">104</span>
<span id="L105" rel="#L105">105</span>
<span id="L106" rel="#L106">106</span>
<span id="L107" rel="#L107">107</span>
<span id="L108" rel="#L108">108</span>
<span id="L109" rel="#L109">109</span>
<span id="L110" rel="#L110">110</span>
<span id="L111" rel="#L111">111</span>
<span id="L112" rel="#L112">112</span>
<span id="L113" rel="#L113">113</span>
<span id="L114" rel="#L114">114</span>
<span id="L115" rel="#L115">115</span>
<span id="L116" rel="#L116">116</span>
<span id="L117" rel="#L117">117</span>
<span id="L118" rel="#L118">118</span>
<span id="L119" rel="#L119">119</span>
<span id="L120" rel="#L120">120</span>
<span id="L121" rel="#L121">121</span>
<span id="L122" rel="#L122">122</span>
<span id="L123" rel="#L123">123</span>
<span id="L124" rel="#L124">124</span>
<span id="L125" rel="#L125">125</span>
<span id="L126" rel="#L126">126</span>
<span id="L127" rel="#L127">127</span>
<span id="L128" rel="#L128">128</span>
<span id="L129" rel="#L129">129</span>
<span id="L130" rel="#L130">130</span>
<span id="L131" rel="#L131">131</span>
<span id="L132" rel="#L132">132</span>
<span id="L133" rel="#L133">133</span>
<span id="L134" rel="#L134">134</span>
<span id="L135" rel="#L135">135</span>
<span id="L136" rel="#L136">136</span>
<span id="L137" rel="#L137">137</span>
<span id="L138" rel="#L138">138</span>
<span id="L139" rel="#L139">139</span>
<span id="L140" rel="#L140">140</span>
<span id="L141" rel="#L141">141</span>
<span id="L142" rel="#L142">142</span>
<span id="L143" rel="#L143">143</span>
<span id="L144" rel="#L144">144</span>
<span id="L145" rel="#L145">145</span>
<span id="L146" rel="#L146">146</span>
<span id="L147" rel="#L147">147</span>
<span id="L148" rel="#L148">148</span>
<span id="L149" rel="#L149">149</span>
<span id="L150" rel="#L150">150</span>
<span id="L151" rel="#L151">151</span>
<span id="L152" rel="#L152">152</span>
<span id="L153" rel="#L153">153</span>
<span id="L154" rel="#L154">154</span>
<span id="L155" rel="#L155">155</span>
<span id="L156" rel="#L156">156</span>
<span id="L157" rel="#L157">157</span>
<span id="L158" rel="#L158">158</span>
<span id="L159" rel="#L159">159</span>
<span id="L160" rel="#L160">160</span>
<span id="L161" rel="#L161">161</span>
<span id="L162" rel="#L162">162</span>
<span id="L163" rel="#L163">163</span>
<span id="L164" rel="#L164">164</span>
<span id="L165" rel="#L165">165</span>
<span id="L166" rel="#L166">166</span>
<span id="L167" rel="#L167">167</span>
<span id="L168" rel="#L168">168</span>
<span id="L169" rel="#L169">169</span>
<span id="L170" rel="#L170">170</span>
<span id="L171" rel="#L171">171</span>
<span id="L172" rel="#L172">172</span>
<span id="L173" rel="#L173">173</span>
<span id="L174" rel="#L174">174</span>
<span id="L175" rel="#L175">175</span>
<span id="L176" rel="#L176">176</span>
<span id="L177" rel="#L177">177</span>
<span id="L178" rel="#L178">178</span>
<span id="L179" rel="#L179">179</span>
<span id="L180" rel="#L180">180</span>
<span id="L181" rel="#L181">181</span>
<span id="L182" rel="#L182">182</span>
<span id="L183" rel="#L183">183</span>
<span id="L184" rel="#L184">184</span>
<span id="L185" rel="#L185">185</span>
<span id="L186" rel="#L186">186</span>
<span id="L187" rel="#L187">187</span>
<span id="L188" rel="#L188">188</span>
<span id="L189" rel="#L189">189</span>
<span id="L190" rel="#L190">190</span>
<span id="L191" rel="#L191">191</span>
<span id="L192" rel="#L192">192</span>
<span id="L193" rel="#L193">193</span>
<span id="L194" rel="#L194">194</span>
<span id="L195" rel="#L195">195</span>
<span id="L196" rel="#L196">196</span>
<span id="L197" rel="#L197">197</span>
<span id="L198" rel="#L198">198</span>
<span id="L199" rel="#L199">199</span>
<span id="L200" rel="#L200">200</span>
<span id="L201" rel="#L201">201</span>
<span id="L202" rel="#L202">202</span>
<span id="L203" rel="#L203">203</span>
<span id="L204" rel="#L204">204</span>
<span id="L205" rel="#L205">205</span>
<span id="L206" rel="#L206">206</span>
<span id="L207" rel="#L207">207</span>
<span id="L208" rel="#L208">208</span>
<span id="L209" rel="#L209">209</span>
<span id="L210" rel="#L210">210</span>
<span id="L211" rel="#L211">211</span>
<span id="L212" rel="#L212">212</span>
<span id="L213" rel="#L213">213</span>
<span id="L214" rel="#L214">214</span>
<span id="L215" rel="#L215">215</span>
<span id="L216" rel="#L216">216</span>
<span id="L217" rel="#L217">217</span>
<span id="L218" rel="#L218">218</span>
<span id="L219" rel="#L219">219</span>
<span id="L220" rel="#L220">220</span>
<span id="L221" rel="#L221">221</span>
<span id="L222" rel="#L222">222</span>
<span id="L223" rel="#L223">223</span>
<span id="L224" rel="#L224">224</span>
<span id="L225" rel="#L225">225</span>
<span id="L226" rel="#L226">226</span>
<span id="L227" rel="#L227">227</span>
<span id="L228" rel="#L228">228</span>
<span id="L229" rel="#L229">229</span>
<span id="L230" rel="#L230">230</span>
<span id="L231" rel="#L231">231</span>
<span id="L232" rel="#L232">232</span>
<span id="L233" rel="#L233">233</span>
<span id="L234" rel="#L234">234</span>
<span id="L235" rel="#L235">235</span>
<span id="L236" rel="#L236">236</span>
<span id="L237" rel="#L237">237</span>
<span id="L238" rel="#L238">238</span>
<span id="L239" rel="#L239">239</span>
<span id="L240" rel="#L240">240</span>
<span id="L241" rel="#L241">241</span>
<span id="L242" rel="#L242">242</span>
<span id="L243" rel="#L243">243</span>
<span id="L244" rel="#L244">244</span>
<span id="L245" rel="#L245">245</span>
<span id="L246" rel="#L246">246</span>
<span id="L247" rel="#L247">247</span>
<span id="L248" rel="#L248">248</span>
<span id="L249" rel="#L249">249</span>
<span id="L250" rel="#L250">250</span>
<span id="L251" rel="#L251">251</span>
<span id="L252" rel="#L252">252</span>
<span id="L253" rel="#L253">253</span>
<span id="L254" rel="#L254">254</span>
<span id="L255" rel="#L255">255</span>
<span id="L256" rel="#L256">256</span>
<span id="L257" rel="#L257">257</span>
<span id="L258" rel="#L258">258</span>
<span id="L259" rel="#L259">259</span>
<span id="L260" rel="#L260">260</span>
<span id="L261" rel="#L261">261</span>
<span id="L262" rel="#L262">262</span>
<span id="L263" rel="#L263">263</span>
<span id="L264" rel="#L264">264</span>
<span id="L265" rel="#L265">265</span>
<span id="L266" rel="#L266">266</span>
<span id="L267" rel="#L267">267</span>
<span id="L268" rel="#L268">268</span>
<span id="L269" rel="#L269">269</span>
<span id="L270" rel="#L270">270</span>
<span id="L271" rel="#L271">271</span>
<span id="L272" rel="#L272">272</span>
<span id="L273" rel="#L273">273</span>
<span id="L274" rel="#L274">274</span>
<span id="L275" rel="#L275">275</span>
<span id="L276" rel="#L276">276</span>
<span id="L277" rel="#L277">277</span>
<span id="L278" rel="#L278">278</span>
<span id="L279" rel="#L279">279</span>
<span id="L280" rel="#L280">280</span>
<span id="L281" rel="#L281">281</span>
<span id="L282" rel="#L282">282</span>
<span id="L283" rel="#L283">283</span>
<span id="L284" rel="#L284">284</span>
<span id="L285" rel="#L285">285</span>
<span id="L286" rel="#L286">286</span>
<span id="L287" rel="#L287">287</span>
<span id="L288" rel="#L288">288</span>
<span id="L289" rel="#L289">289</span>
<span id="L290" rel="#L290">290</span>
<span id="L291" rel="#L291">291</span>
<span id="L292" rel="#L292">292</span>
<span id="L293" rel="#L293">293</span>
<span id="L294" rel="#L294">294</span>
<span id="L295" rel="#L295">295</span>
<span id="L296" rel="#L296">296</span>
<span id="L297" rel="#L297">297</span>
<span id="L298" rel="#L298">298</span>
<span id="L299" rel="#L299">299</span>
<span id="L300" rel="#L300">300</span>
<span id="L301" rel="#L301">301</span>
<span id="L302" rel="#L302">302</span>
<span id="L303" rel="#L303">303</span>
<span id="L304" rel="#L304">304</span>
<span id="L305" rel="#L305">305</span>
<span id="L306" rel="#L306">306</span>
<span id="L307" rel="#L307">307</span>
<span id="L308" rel="#L308">308</span>
<span id="L309" rel="#L309">309</span>
<span id="L310" rel="#L310">310</span>
<span id="L311" rel="#L311">311</span>
<span id="L312" rel="#L312">312</span>
<span id="L313" rel="#L313">313</span>
<span id="L314" rel="#L314">314</span>
<span id="L315" rel="#L315">315</span>
<span id="L316" rel="#L316">316</span>
<span id="L317" rel="#L317">317</span>
<span id="L318" rel="#L318">318</span>
<span id="L319" rel="#L319">319</span>
<span id="L320" rel="#L320">320</span>
<span id="L321" rel="#L321">321</span>
<span id="L322" rel="#L322">322</span>
<span id="L323" rel="#L323">323</span>
<span id="L324" rel="#L324">324</span>
<span id="L325" rel="#L325">325</span>
<span id="L326" rel="#L326">326</span>
<span id="L327" rel="#L327">327</span>
<span id="L328" rel="#L328">328</span>
<span id="L329" rel="#L329">329</span>
<span id="L330" rel="#L330">330</span>
<span id="L331" rel="#L331">331</span>
<span id="L332" rel="#L332">332</span>
<span id="L333" rel="#L333">333</span>
<span id="L334" rel="#L334">334</span>
<span id="L335" rel="#L335">335</span>
<span id="L336" rel="#L336">336</span>
<span id="L337" rel="#L337">337</span>
<span id="L338" rel="#L338">338</span>
<span id="L339" rel="#L339">339</span>
<span id="L340" rel="#L340">340</span>
<span id="L341" rel="#L341">341</span>
<span id="L342" rel="#L342">342</span>
<span id="L343" rel="#L343">343</span>
<span id="L344" rel="#L344">344</span>
<span id="L345" rel="#L345">345</span>
<span id="L346" rel="#L346">346</span>
<span id="L347" rel="#L347">347</span>
<span id="L348" rel="#L348">348</span>
<span id="L349" rel="#L349">349</span>
<span id="L350" rel="#L350">350</span>
<span id="L351" rel="#L351">351</span>
<span id="L352" rel="#L352">352</span>
<span id="L353" rel="#L353">353</span>
<span id="L354" rel="#L354">354</span>
<span id="L355" rel="#L355">355</span>
<span id="L356" rel="#L356">356</span>
<span id="L357" rel="#L357">357</span>
<span id="L358" rel="#L358">358</span>
<span id="L359" rel="#L359">359</span>
<span id="L360" rel="#L360">360</span>
<span id="L361" rel="#L361">361</span>
<span id="L362" rel="#L362">362</span>
<span id="L363" rel="#L363">363</span>
<span id="L364" rel="#L364">364</span>
<span id="L365" rel="#L365">365</span>
<span id="L366" rel="#L366">366</span>
<span id="L367" rel="#L367">367</span>
<span id="L368" rel="#L368">368</span>
<span id="L369" rel="#L369">369</span>
<span id="L370" rel="#L370">370</span>
<span id="L371" rel="#L371">371</span>
<span id="L372" rel="#L372">372</span>
<span id="L373" rel="#L373">373</span>
<span id="L374" rel="#L374">374</span>
<span id="L375" rel="#L375">375</span>
<span id="L376" rel="#L376">376</span>
<span id="L377" rel="#L377">377</span>
<span id="L378" rel="#L378">378</span>
<span id="L379" rel="#L379">379</span>
<span id="L380" rel="#L380">380</span>
<span id="L381" rel="#L381">381</span>
<span id="L382" rel="#L382">382</span>
<span id="L383" rel="#L383">383</span>
<span id="L384" rel="#L384">384</span>
<span id="L385" rel="#L385">385</span>
<span id="L386" rel="#L386">386</span>
<span id="L387" rel="#L387">387</span>
<span id="L388" rel="#L388">388</span>
<span id="L389" rel="#L389">389</span>
<span id="L390" rel="#L390">390</span>
<span id="L391" rel="#L391">391</span>
<span id="L392" rel="#L392">392</span>
<span id="L393" rel="#L393">393</span>
<span id="L394" rel="#L394">394</span>
<span id="L395" rel="#L395">395</span>
<span id="L396" rel="#L396">396</span>
<span id="L397" rel="#L397">397</span>
<span id="L398" rel="#L398">398</span>
<span id="L399" rel="#L399">399</span>
<span id="L400" rel="#L400">400</span>
<span id="L401" rel="#L401">401</span>
<span id="L402" rel="#L402">402</span>
<span id="L403" rel="#L403">403</span>
<span id="L404" rel="#L404">404</span>
<span id="L405" rel="#L405">405</span>
<span id="L406" rel="#L406">406</span>
<span id="L407" rel="#L407">407</span>
<span id="L408" rel="#L408">408</span>
<span id="L409" rel="#L409">409</span>
<span id="L410" rel="#L410">410</span>
<span id="L411" rel="#L411">411</span>
<span id="L412" rel="#L412">412</span>
<span id="L413" rel="#L413">413</span>
<span id="L414" rel="#L414">414</span>
<span id="L415" rel="#L415">415</span>
<span id="L416" rel="#L416">416</span>
<span id="L417" rel="#L417">417</span>
<span id="L418" rel="#L418">418</span>
<span id="L419" rel="#L419">419</span>
<span id="L420" rel="#L420">420</span>
<span id="L421" rel="#L421">421</span>
<span id="L422" rel="#L422">422</span>
<span id="L423" rel="#L423">423</span>
<span id="L424" rel="#L424">424</span>
<span id="L425" rel="#L425">425</span>
<span id="L426" rel="#L426">426</span>
<span id="L427" rel="#L427">427</span>
<span id="L428" rel="#L428">428</span>
<span id="L429" rel="#L429">429</span>
<span id="L430" rel="#L430">430</span>
<span id="L431" rel="#L431">431</span>
<span id="L432" rel="#L432">432</span>
<span id="L433" rel="#L433">433</span>
<span id="L434" rel="#L434">434</span>
<span id="L435" rel="#L435">435</span>
<span id="L436" rel="#L436">436</span>
<span id="L437" rel="#L437">437</span>
<span id="L438" rel="#L438">438</span>
<span id="L439" rel="#L439">439</span>
<span id="L440" rel="#L440">440</span>
<span id="L441" rel="#L441">441</span>
<span id="L442" rel="#L442">442</span>

            </td>
            <td class="blob-line-code"><div class="code-body highlight"><pre><div class='line' id='LC1'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC2'><span class="sd">Extract client information from http user agent</span></div><div class='line' id='LC3'><span class="sd">The module does not try to detect all capabilities of browser in current form (it can easily be extended though).</span></div><div class='line' id='LC4'><span class="sd">Tries to</span></div><div class='line' id='LC5'><span class="sd">    * be fast</span></div><div class='line' id='LC6'><span class="sd">    * very easy to extend</span></div><div class='line' id='LC7'><span class="sd">    * reliable enough for practical purposes</span></div><div class='line' id='LC8'><span class="sd">    * assist python web apps to detect clients.</span></div><div class='line' id='LC9'><span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC10'><br/></div><div class='line' id='LC11'><br/></div><div class='line' id='LC12'><span class="k">class</span> <span class="nc">DetectorsHub</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span></div><div class='line' id='LC13'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_known_types</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;os&#39;</span><span class="p">,</span> <span class="s">&#39;dist&#39;</span><span class="p">,</span> <span class="s">&#39;flavor&#39;</span><span class="p">,</span> <span class="s">&#39;browser&#39;</span><span class="p">]</span></div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">):</span></div><div class='line' id='LC16'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">dict</span><span class="o">.</span><span class="n">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kw</span><span class="p">)</span></div><div class='line' id='LC17'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">typ</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_known_types</span><span class="p">:</span></div><div class='line' id='LC18'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">setdefault</span><span class="p">(</span><span class="n">typ</span><span class="p">,</span> <span class="p">[])</span></div><div class='line' id='LC19'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">registerDetectors</span><span class="p">()</span></div><div class='line' id='LC20'><br/></div><div class='line' id='LC21'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">register</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">detector</span><span class="p">):</span></div><div class='line' id='LC22'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">detector</span><span class="o">.</span><span class="n">info_type</span> <span class="ow">not</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">_known_types</span><span class="p">:</span></div><div class='line' id='LC23'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="p">[</span><span class="n">detector</span><span class="o">.</span><span class="n">info_type</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">detector</span><span class="p">]</span></div><div class='line' id='LC24'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">_known_types</span><span class="o">.</span><span class="n">insert</span><span class="p">(</span><span class="n">detector</span><span class="o">.</span><span class="n">order</span><span class="p">,</span> <span class="n">detector</span><span class="o">.</span><span class="n">info_type</span><span class="p">)</span></div><div class='line' id='LC25'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC26'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="p">[</span><span class="n">detector</span><span class="o">.</span><span class="n">info_type</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">detector</span><span class="p">)</span></div><div class='line' id='LC27'><br/></div><div class='line' id='LC28'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC29'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">iter</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_known_types</span><span class="p">)</span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">registerDetectors</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC32'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">detectors</span> <span class="o">=</span> <span class="p">[</span><span class="n">v</span><span class="p">()</span> <span class="k">for</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">globals</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="p">()</span> <span class="k">if</span> <span class="n">DetectorBase</span> <span class="ow">in</span> <span class="nb">getattr</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="s">&#39;__mro__&#39;</span><span class="p">,</span> <span class="p">[])]</span></div><div class='line' id='LC33'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">detectors</span><span class="p">:</span></div><div class='line' id='LC34'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">d</span><span class="o">.</span><span class="n">can_register</span><span class="p">:</span></div><div class='line' id='LC35'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">register</span><span class="p">(</span><span class="n">d</span><span class="p">)</span></div><div class='line' id='LC36'><br/></div><div class='line' id='LC37'><br/></div><div class='line' id='LC38'><span class="k">class</span> <span class="nc">DetectorBase</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>  <span class="c"># &quot;to perform match in DetectorsHub object&quot;</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">info_type</span> <span class="o">=</span> <span class="s">&quot;override me&quot;</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result_key</span> <span class="o">=</span> <span class="s">&quot;override me&quot;</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">order</span> <span class="o">=</span> <span class="mi">10</span>  <span class="c"># 0 is highest</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;string to look for&quot;</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">skip_if_found</span> <span class="o">=</span> <span class="p">[]</span>  <span class="c"># strings if present stop processin</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">can_register</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[(</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">)]</span></div><div class='line' id='LC47'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">allow_space_in_version</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_suggested_detectors</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC49'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC50'><br/></div><div class='line' id='LC51'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></div><div class='line' id='LC52'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">:</span></div><div class='line' id='LC53'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__name__</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="bp">self</span><span class="o">.</span><span class="n">can_register</span> <span class="o">=</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__class__</span><span class="o">.</span><span class="n">__dict__</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;can_register&#39;</span><span class="p">,</span> <span class="bp">True</span><span class="p">))</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">detect</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span></div><div class='line' id='LC57'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># -&gt; True/None</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">checkWords</span><span class="p">(</span><span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">info_type</span><span class="p">]</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">)</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">getVersion</span><span class="p">(</span><span class="n">agent</span><span class="p">)</span></div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">version</span><span class="p">:</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span><span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">info_type</span><span class="p">][</span><span class="s">&#39;version&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">version</span></div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">platform</span><span class="p">:</span></div><div class='line' id='LC64'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span><span class="p">[</span><span class="s">&#39;platform&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">platform</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">:</span> <span class="n">version</span><span class="p">}</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC66'><br/></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">checkWords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># -&gt; True/None</span></div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">w</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">skip_if_found</span><span class="p">:</span></div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">w</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">look_for</span><span class="p">,</span> <span class="p">(</span><span class="nb">tuple</span><span class="p">,</span> <span class="nb">list</span><span class="p">)):</span></div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">look_for</span><span class="p">:</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">look_for</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC81'><span class="sd">        =&gt; version string /None</span></div><div class='line' id='LC82'><span class="sd">        &quot;&quot;&quot;</span></div><div class='line' id='LC83'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">version_markers</span> <span class="k">if</span> \</div><div class='line' id='LC84'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="nb">isinstance</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">version_markers</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="p">(</span><span class="nb">list</span><span class="p">,</span> <span class="nb">tuple</span><span class="p">))</span> <span class="k">else</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">version_markers</span><span class="p">]</span></div><div class='line' id='LC85'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_part</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">look_for</span><span class="p">,</span> <span class="mi">1</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC86'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">start</span><span class="p">,</span> <span class="n">end</span> <span class="ow">in</span> <span class="n">version_markers</span><span class="p">:</span></div><div class='line' id='LC87'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">version_part</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="n">start</span><span class="p">)</span> <span class="ow">and</span> <span class="n">end</span> <span class="ow">in</span> <span class="n">version_part</span><span class="p">:</span></div><div class='line' id='LC88'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">version_part</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></div><div class='line' id='LC89'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">end</span><span class="p">:</span>  <span class="c"># end could be empty string</span></div><div class='line' id='LC90'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">version</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">end</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC91'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">allow_space_in_version</span><span class="p">:</span></div><div class='line' id='LC92'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">version</span><span class="o">.</span><span class="n">split</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC93'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">version</span></div><div class='line' id='LC94'><br/></div><div class='line' id='LC95'><br/></div><div class='line' id='LC96'><span class="k">class</span> <span class="nc">OS</span><span class="p">(</span><span class="n">DetectorBase</span><span class="p">):</span></div><div class='line' id='LC97'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">info_type</span> <span class="o">=</span> <span class="s">&quot;os&quot;</span></div><div class='line' id='LC98'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">can_register</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC99'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;;&quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">]</span></div><div class='line' id='LC100'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">allow_space_in_version</span> <span class="o">=</span> <span class="bp">True</span></div><div class='line' id='LC101'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC102'><br/></div><div class='line' id='LC103'><br/></div><div class='line' id='LC104'><span class="k">class</span> <span class="nc">Dist</span><span class="p">(</span><span class="n">DetectorBase</span><span class="p">):</span></div><div class='line' id='LC105'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">info_type</span> <span class="o">=</span> <span class="s">&quot;dist&quot;</span></div><div class='line' id='LC106'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">can_register</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC107'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC108'><br/></div><div class='line' id='LC109'><br/></div><div class='line' id='LC110'><span class="k">class</span> <span class="nc">Flavor</span><span class="p">(</span><span class="n">DetectorBase</span><span class="p">):</span></div><div class='line' id='LC111'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">info_type</span> <span class="o">=</span> <span class="s">&quot;flavor&quot;</span></div><div class='line' id='LC112'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">can_register</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC113'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="bp">None</span></div><div class='line' id='LC114'><br/></div><div class='line' id='LC115'><br/></div><div class='line' id='LC116'><span class="k">class</span> <span class="nc">Browser</span><span class="p">(</span><span class="n">DetectorBase</span><span class="p">):</span></div><div class='line' id='LC117'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">info_type</span> <span class="o">=</span> <span class="s">&quot;browser&quot;</span></div><div class='line' id='LC118'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">can_register</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC119'><br/></div><div class='line' id='LC120'><br/></div><div class='line' id='LC121'><span class="k">class</span> <span class="nc">Firefox</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC122'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Firefox&quot;</span></div><div class='line' id='LC123'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[(</span><span class="s">&#39;/&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)]</span></div><div class='line' id='LC124'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">skip_if_found</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;SeaMonkey&quot;</span><span class="p">]</span></div><div class='line' id='LC125'><br/></div><div class='line' id='LC126'><br/></div><div class='line' id='LC127'><span class="k">class</span> <span class="nc">SeaMonkey</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC128'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;SeaMonkey&quot;</span></div><div class='line' id='LC129'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[(</span><span class="s">&#39;/&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)]</span></div><div class='line' id='LC130'><br/></div><div class='line' id='LC131'><br/></div><div class='line' id='LC132'><span class="k">class</span> <span class="nc">Konqueror</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC133'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Konqueror&quot;</span></div><div class='line' id='LC134'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot;;&quot;</span><span class="p">]</span></div><div class='line' id='LC135'><br/></div><div class='line' id='LC136'><br/></div><div class='line' id='LC137'><span class="k">class</span> <span class="nc">OperaMobile</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC138'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Opera Mobi&quot;</span></div><div class='line' id='LC139'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="s">&quot;Opera Mobile&quot;</span></div><div class='line' id='LC140'><br/></div><div class='line' id='LC141'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC142'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC143'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Version&quot;</span></div><div class='line' id='LC144'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">look_for</span><span class="p">)[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC145'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC146'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Opera&quot;</span></div><div class='line' id='LC147'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">look_for</span><span class="p">)[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC148'><br/></div><div class='line' id='LC149'><br/></div><div class='line' id='LC150'><span class="k">class</span> <span class="nc">Opera</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC151'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Opera&quot;</span></div><div class='line' id='LC152'><br/></div><div class='line' id='LC153'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC154'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC155'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Version&quot;</span></div><div class='line' id='LC156'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">look_for</span><span class="p">)[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC157'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span><span class="p">:</span></div><div class='line' id='LC158'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Opera&quot;</span></div><div class='line' id='LC159'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">look_for</span><span class="p">)[</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC160'><br/></div><div class='line' id='LC161'><br/></div><div class='line' id='LC162'><span class="k">class</span> <span class="nc">OperaNew</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC163'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC164'><span class="sd">    Opera after version 15</span></div><div class='line' id='LC165'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC166'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="s">&quot;Opera&quot;</span></div><div class='line' id='LC167'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;OPR&quot;</span></div><div class='line' id='LC168'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[(</span><span class="s">&#39;/&#39;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)]</span></div><div class='line' id='LC169'><br/></div><div class='line' id='LC170'><br/></div><div class='line' id='LC171'><span class="k">class</span> <span class="nc">Netscape</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC172'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Netscape&quot;</span></div><div class='line' id='LC173'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[(</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&#39;&#39;</span><span class="p">)]</span></div><div class='line' id='LC174'><br/></div><div class='line' id='LC175'><br/></div><div class='line' id='LC176'><span class="k">class</span> <span class="nc">Trident</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC177'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Trident&quot;</span></div><div class='line' id='LC178'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">skip_if_found</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;MSIE&quot;</span><span class="p">,</span> <span class="s">&quot;Opera&quot;</span><span class="p">]</span></div><div class='line' id='LC179'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="s">&quot;Microsoft Internet Explorer&quot;</span></div><div class='line' id='LC180'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot;;&quot;</span><span class="p">]</span></div><div class='line' id='LC181'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">trident_to_ie_versions</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC182'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;4.0&#39;</span><span class="p">:</span> <span class="s">&#39;8.0&#39;</span><span class="p">,</span></div><div class='line' id='LC183'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;5.0&#39;</span><span class="p">:</span> <span class="s">&#39;9.0&#39;</span><span class="p">,</span></div><div class='line' id='LC184'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;6.0&#39;</span><span class="p">:</span> <span class="s">&#39;10.0&#39;</span><span class="p">,</span></div><div class='line' id='LC185'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&#39;7.0&#39;</span><span class="p">:</span> <span class="s">&#39;11.0&#39;</span><span class="p">,</span></div><div class='line' id='LC186'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC187'><br/></div><div class='line' id='LC188'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC189'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">trident_to_ie_versions</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="nb">super</span><span class="p">(</span><span class="n">Trident</span><span class="p">,</span> <span class="bp">self</span><span class="p">)</span><span class="o">.</span><span class="n">getVersion</span><span class="p">(</span><span class="n">agent</span><span class="p">))</span></div><div class='line' id='LC190'><br/></div><div class='line' id='LC191'><br/></div><div class='line' id='LC192'><span class="k">class</span> <span class="nc">MSIE</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC193'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;MSIE&quot;</span></div><div class='line' id='LC194'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">skip_if_found</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;Opera&quot;</span><span class="p">]</span></div><div class='line' id='LC195'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">name</span> <span class="o">=</span> <span class="s">&quot;Microsoft Internet Explorer&quot;</span></div><div class='line' id='LC196'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot; &quot;</span><span class="p">,</span> <span class="s">&quot;;&quot;</span><span class="p">]</span></div><div class='line' id='LC197'><br/></div><div class='line' id='LC198'><br/></div><div class='line' id='LC199'><span class="k">class</span> <span class="nc">Galeon</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC200'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Galeon&quot;</span></div><div class='line' id='LC201'><br/></div><div class='line' id='LC202'><br/></div><div class='line' id='LC203'><span class="k">class</span> <span class="nc">WOSBrowser</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC204'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;wOSBrowser&quot;</span></div><div class='line' id='LC205'><br/></div><div class='line' id='LC206'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC207'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC208'><br/></div><div class='line' id='LC209'><br/></div><div class='line' id='LC210'><span class="k">class</span> <span class="nc">Safari</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC211'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Safari&quot;</span></div><div class='line' id='LC212'><br/></div><div class='line' id='LC213'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">checkWords</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC214'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">unless_list</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;Chrome&quot;</span><span class="p">,</span> <span class="s">&quot;OmniWeb&quot;</span><span class="p">,</span> <span class="s">&quot;wOSBrowser&quot;</span><span class="p">]</span></div><div class='line' id='LC215'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">look_for</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC216'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">unless_list</span><span class="p">:</span></div><div class='line' id='LC217'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC218'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">False</span></div><div class='line' id='LC219'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="bp">True</span></div><div class='line' id='LC220'><br/></div><div class='line' id='LC221'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC222'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&quot;Version/&quot;</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC223'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;Version/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC224'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&quot;Safari/&quot;</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC225'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;Safari/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC226'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC227'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;Safari &#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39; &#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>  <span class="c"># Mobile Safari</span></div><div class='line' id='LC228'><br/></div><div class='line' id='LC229'><br/></div><div class='line' id='LC230'><span class="k">class</span> <span class="nc">Linux</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span></div><div class='line' id='LC231'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Linux&#39;</span></div><div class='line' id='LC232'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;Linux&#39;</span></div><div class='line' id='LC233'><br/></div><div class='line' id='LC234'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC235'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC236'><br/></div><div class='line' id='LC237'><br/></div><div class='line' id='LC238'><span class="k">class</span> <span class="nc">Blackberry</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span></div><div class='line' id='LC239'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;BlackBerry&#39;</span></div><div class='line' id='LC240'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;BlackBerry&#39;</span></div><div class='line' id='LC241'><br/></div><div class='line' id='LC242'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC243'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC244'><br/></div><div class='line' id='LC245'><br/></div><div class='line' id='LC246'><span class="k">class</span> <span class="nc">BlackberryPlaybook</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC247'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;PlayBook&#39;</span></div><div class='line' id='LC248'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;BlackBerry&#39;</span></div><div class='line' id='LC249'><br/></div><div class='line' id='LC250'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC251'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC252'><br/></div><div class='line' id='LC253'><br/></div><div class='line' id='LC254'><span class="k">class</span> <span class="nc">iOS</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span></div><div class='line' id='LC255'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="p">(</span><span class="s">&#39;iPhone&#39;</span><span class="p">,</span> <span class="s">&#39;iPad&#39;</span><span class="p">)</span></div><div class='line' id='LC256'><br/></div><div class='line' id='LC257'><br/></div><div class='line' id='LC258'><span class="k">class</span> <span class="nc">iPhone</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC259'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;iPhone&#39;</span></div><div class='line' id='LC260'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;iOS&#39;</span></div><div class='line' id='LC261'><br/></div><div class='line' id='LC262'><br/></div><div class='line' id='LC263'><span class="k">class</span> <span class="nc">IPad</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC264'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;iPad; CPU OS&#39;</span></div><div class='line' id='LC265'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[(</span><span class="s">&#39; &#39;</span><span class="p">,</span> <span class="s">&#39; &#39;</span><span class="p">)]</span></div><div class='line' id='LC266'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">allow_space_in_version</span> <span class="o">=</span> <span class="bp">False</span></div><div class='line' id='LC267'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;iOS&#39;</span></div><div class='line' id='LC268'><br/></div><div class='line' id='LC269'><br/></div><div class='line' id='LC270'><span class="k">class</span> <span class="nc">Macintosh</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span></div><div class='line' id='LC271'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Macintosh&#39;</span></div><div class='line' id='LC272'><br/></div><div class='line' id='LC273'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC274'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC275'><br/></div><div class='line' id='LC276'><br/></div><div class='line' id='LC277'><span class="k">class</span> <span class="nc">MacOS</span><span class="p">(</span><span class="n">Flavor</span><span class="p">):</span></div><div class='line' id='LC278'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Mac OS&#39;</span></div><div class='line' id='LC279'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;Mac OS&#39;</span></div><div class='line' id='LC280'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">skip_if_found</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;iPhone&#39;</span><span class="p">,</span> <span class="s">&#39;iPad&#39;</span><span class="p">]</span></div><div class='line' id='LC281'><br/></div><div class='line' id='LC282'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC283'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_end_chars</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;;&#39;</span><span class="p">,</span> <span class="s">&#39;)&#39;</span><span class="p">]</span></div><div class='line' id='LC284'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">part</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;Mac OS&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC285'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">version_end_chars</span><span class="p">:</span></div><div class='line' id='LC286'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">part</span><span class="p">:</span></div><div class='line' id='LC287'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">c</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC288'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">version</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;_&#39;</span><span class="p">,</span> <span class="s">&#39;.&#39;</span><span class="p">)</span></div><div class='line' id='LC289'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="s">&#39;&#39;</span></div><div class='line' id='LC290'><br/></div><div class='line' id='LC291'><br/></div><div class='line' id='LC292'><span class="k">class</span> <span class="nc">Windows</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span></div><div class='line' id='LC293'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Windows&#39;</span></div><div class='line' id='LC294'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;Windows&#39;</span></div><div class='line' id='LC295'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">win_versions</span> <span class="o">=</span> <span class="p">{</span></div><div class='line' id='LC296'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 6.3&quot;</span><span class="p">:</span> <span class="s">&quot;8.1&quot;</span><span class="p">,</span></div><div class='line' id='LC297'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 6.2&quot;</span><span class="p">:</span> <span class="s">&quot;8&quot;</span><span class="p">,</span></div><div class='line' id='LC298'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 6.1&quot;</span><span class="p">:</span> <span class="s">&quot;7&quot;</span><span class="p">,</span></div><div class='line' id='LC299'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 6.0&quot;</span><span class="p">:</span> <span class="s">&quot;Vista&quot;</span><span class="p">,</span></div><div class='line' id='LC300'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 5.2&quot;</span><span class="p">:</span> <span class="s">&quot;Server 2003 / XP x64&quot;</span><span class="p">,</span></div><div class='line' id='LC301'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 5.1&quot;</span><span class="p">:</span> <span class="s">&quot;XP&quot;</span><span class="p">,</span></div><div class='line' id='LC302'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 5.01&quot;</span><span class="p">:</span> <span class="s">&quot;2000 SP1&quot;</span><span class="p">,</span></div><div class='line' id='LC303'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;NT 5.0&quot;</span><span class="p">:</span> <span class="s">&quot;2000&quot;</span><span class="p">,</span></div><div class='line' id='LC304'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="s">&quot;98; Win 9x 4.90&quot;</span><span class="p">:</span> <span class="s">&quot;Me&quot;</span></div><div class='line' id='LC305'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">}</span></div><div class='line' id='LC306'><br/></div><div class='line' id='LC307'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC308'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">v</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;Windows&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC309'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;)&#39;</span> <span class="ow">in</span> <span class="n">v</span><span class="p">:</span></div><div class='line' id='LC310'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">v</span> <span class="o">=</span> <span class="n">v</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;)&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC311'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">v</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">win_versions</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">v</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span></div><div class='line' id='LC312'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">v</span></div><div class='line' id='LC313'><br/></div><div class='line' id='LC314'><br/></div><div class='line' id='LC315'><span class="k">class</span> <span class="nc">Ubuntu</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC316'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Ubuntu&#39;</span></div><div class='line' id='LC317'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">]</span></div><div class='line' id='LC318'><br/></div><div class='line' id='LC319'><br/></div><div class='line' id='LC320'><span class="k">class</span> <span class="nc">Debian</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC321'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Debian&#39;</span></div><div class='line' id='LC322'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">]</span></div><div class='line' id='LC323'><br/></div><div class='line' id='LC324'><br/></div><div class='line' id='LC325'><span class="k">class</span> <span class="nc">Chrome</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC326'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;Chrome&quot;</span></div><div class='line' id='LC327'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">]</span></div><div class='line' id='LC328'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">skip_if_found</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;OPR&quot;</span><span class="p">]</span></div><div class='line' id='LC329'><br/></div><div class='line' id='LC330'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC331'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">part</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">look_for</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">version_markers</span><span class="p">[</span><span class="mi">0</span><span class="p">])[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC332'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">version_markers</span><span class="p">[</span><span class="mi">1</span><span class="p">])[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC333'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;+&#39;</span> <span class="ow">in</span> <span class="n">version</span><span class="p">:</span></div><div class='line' id='LC334'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version</span> <span class="o">=</span> <span class="n">part</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;+&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span></div><div class='line' id='LC335'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">version</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC336'><br/></div><div class='line' id='LC337'><br/></div><div class='line' id='LC338'><span class="k">class</span> <span class="nc">ChromeiOS</span><span class="p">(</span><span class="n">Browser</span><span class="p">):</span></div><div class='line' id='LC339'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;CriOS&quot;</span></div><div class='line' id='LC340'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;/&quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">]</span></div><div class='line' id='LC341'><br/></div><div class='line' id='LC342'><br/></div><div class='line' id='LC343'><span class="k">class</span> <span class="nc">ChromeOS</span><span class="p">(</span><span class="n">OS</span><span class="p">):</span></div><div class='line' id='LC344'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&quot;CrOS&quot;</span></div><div class='line' id='LC345'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39; ChromeOS&#39;</span></div><div class='line' id='LC346'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot; &quot;</span><span class="p">,</span> <span class="s">&quot; &quot;</span><span class="p">]</span></div><div class='line' id='LC347'><br/></div><div class='line' id='LC348'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC349'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">version_markers</span></div><div class='line' id='LC350'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">look_for</span> <span class="o">+</span> <span class="s">&#39;+&#39;</span> <span class="ow">in</span> <span class="n">agent</span><span class="p">:</span></div><div class='line' id='LC351'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">version_markers</span> <span class="o">=</span> <span class="p">[</span><span class="s">&#39;+&#39;</span><span class="p">,</span> <span class="s">&#39;+&#39;</span><span class="p">]</span></div><div class='line' id='LC352'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">look_for</span> <span class="o">+</span> <span class="n">version_markers</span><span class="p">[</span><span class="mi">0</span><span class="p">])[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">version_markers</span><span class="p">[</span><span class="mi">1</span><span class="p">])[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></div><div class='line' id='LC353'><br/></div><div class='line' id='LC354'><br/></div><div class='line' id='LC355'><span class="k">class</span> <span class="nc">Android</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC356'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;Android&#39;</span></div><div class='line' id='LC357'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">platform</span> <span class="o">=</span> <span class="s">&#39;Android&#39;</span></div><div class='line' id='LC358'><br/></div><div class='line' id='LC359'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC360'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">look_for</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC361'><br/></div><div class='line' id='LC362'><br/></div><div class='line' id='LC363'><span class="k">class</span> <span class="nc">WebOS</span><span class="p">(</span><span class="n">Dist</span><span class="p">):</span></div><div class='line' id='LC364'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">look_for</span> <span class="o">=</span> <span class="s">&#39;hpwOS&#39;</span></div><div class='line' id='LC365'><br/></div><div class='line' id='LC366'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">def</span> <span class="nf">getVersion</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC367'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">agent</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;hpwOS/&#39;</span><span class="p">)[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></div><div class='line' id='LC368'><br/></div><div class='line' id='LC369'><br/></div><div class='line' id='LC370'><span class="k">class</span> <span class="nc">prefs</span><span class="p">:</span>  <span class="c"># experimental</span></div><div class='line' id='LC371'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span></div><div class='line' id='LC372'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Linux</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Firefox</span><span class="p">,</span> <span class="n">Chrome</span><span class="p">],</span> <span class="n">dist</span><span class="o">=</span><span class="p">[</span><span class="n">Ubuntu</span><span class="p">,</span> <span class="n">Android</span><span class="p">])),</span></div><div class='line' id='LC373'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">BlackBerry</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">dist</span><span class="o">=</span><span class="p">[</span><span class="n">BlackberryPlaybook</span><span class="p">]),</span></div><div class='line' id='LC374'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Macintosh</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">flavor</span><span class="o">=</span><span class="p">[</span><span class="n">MacOS</span><span class="p">]),</span></div><div class='line' id='LC375'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Windows</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">MSIE</span><span class="p">,</span> <span class="n">Firefox</span><span class="p">]),</span></div><div class='line' id='LC376'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">ChromeOS</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Chrome</span><span class="p">]),</span></div><div class='line' id='LC377'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Debian</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Firefox</span><span class="p">])</span></div><div class='line' id='LC378'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC379'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">dist</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span></div><div class='line' id='LC380'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Ubuntu</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Firefox</span><span class="p">]),</span></div><div class='line' id='LC381'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">Android</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Safari</span><span class="p">]),</span></div><div class='line' id='LC382'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">IPhone</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Safari</span><span class="p">]),</span></div><div class='line' id='LC383'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">IPad</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Safari</span><span class="p">]),</span></div><div class='line' id='LC384'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC385'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">flavor</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span></div><div class='line' id='LC386'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">MacOS</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">browser</span><span class="o">=</span><span class="p">[</span><span class="n">Opera</span><span class="p">,</span> <span class="n">Chrome</span><span class="p">,</span> <span class="n">Firefox</span><span class="p">,</span> <span class="n">MSIE</span><span class="p">])</span></div><div class='line' id='LC387'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">)</span></div><div class='line' id='LC388'><br/></div><div class='line' id='LC389'><br/></div><div class='line' id='LC390'><span class="n">detectorshub</span> <span class="o">=</span> <span class="n">DetectorsHub</span><span class="p">()</span></div><div class='line' id='LC391'><br/></div><div class='line' id='LC392'><br/></div><div class='line' id='LC393'><span class="k">def</span> <span class="nf">detect</span><span class="p">(</span><span class="n">agent</span><span class="p">,</span> <span class="n">fill_none</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span></div><div class='line' id='LC394'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC395'><span class="sd">    fill_none: if name/version is not detected respective key is still added to the result with value None</span></div><div class='line' id='LC396'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC397'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">platform</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">version</span><span class="o">=</span><span class="bp">None</span><span class="p">))</span></div><div class='line' id='LC398'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">_suggested_detectors</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC399'><br/></div><div class='line' id='LC400'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">info_type</span> <span class="ow">in</span> <span class="n">detectorshub</span><span class="p">:</span></div><div class='line' id='LC401'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">detectors</span> <span class="o">=</span> <span class="n">_suggested_detectors</span> <span class="ow">or</span> <span class="n">detectorshub</span><span class="p">[</span><span class="n">info_type</span><span class="p">]</span></div><div class='line' id='LC402'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">detector</span> <span class="ow">in</span> <span class="n">detectors</span><span class="p">:</span></div><div class='line' id='LC403'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">try</span><span class="p">:</span></div><div class='line' id='LC404'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">detector</span><span class="o">.</span><span class="n">detect</span><span class="p">(</span><span class="n">agent</span><span class="p">,</span> <span class="n">result</span><span class="p">)</span></div><div class='line' id='LC405'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">_err</span><span class="p">:</span></div><div class='line' id='LC406'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">pass</span></div><div class='line' id='LC407'><br/></div><div class='line' id='LC408'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">fill_none</span><span class="p">:</span></div><div class='line' id='LC409'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">attrs_d</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;name&#39;</span><span class="p">:</span> <span class="bp">None</span><span class="p">,</span> <span class="s">&#39;version&#39;</span><span class="p">:</span> <span class="bp">None</span><span class="p">}</span></div><div class='line' id='LC410'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="p">(</span><span class="s">&#39;os&#39;</span><span class="p">,</span> <span class="s">&#39;browser&#39;</span><span class="p">):</span></div><div class='line' id='LC411'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">key</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span></div><div class='line' id='LC412'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span><span class="p">[</span><span class="n">key</span><span class="p">]</span> <span class="o">=</span> <span class="n">attrs_d</span></div><div class='line' id='LC413'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">else</span><span class="p">:</span></div><div class='line' id='LC414'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">attrs_d</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></div><div class='line' id='LC415'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span><span class="p">[</span><span class="n">k</span><span class="p">]</span> <span class="o">=</span> <span class="n">v</span></div><div class='line' id='LC416'><br/></div><div class='line' id='LC417'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">result</span></div><div class='line' id='LC418'><br/></div><div class='line' id='LC419'><br/></div><div class='line' id='LC420'><span class="k">def</span> <span class="nf">simple_detect</span><span class="p">(</span><span class="n">agent</span><span class="p">):</span></div><div class='line' id='LC421'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&quot;&quot;&quot;</span></div><div class='line' id='LC422'><span class="sd">    -&gt; (os, browser) # tuple of strings</span></div><div class='line' id='LC423'><span class="sd">    &quot;&quot;&quot;</span></div><div class='line' id='LC424'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">result</span> <span class="o">=</span> <span class="n">detect</span><span class="p">(</span><span class="n">agent</span><span class="p">)</span></div><div class='line' id='LC425'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os_list</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC426'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;flavor&#39;</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span></div><div class='line' id='LC427'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="s">&#39;flavor&#39;</span><span class="p">][</span><span class="s">&#39;name&#39;</span><span class="p">])</span></div><div class='line' id='LC428'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;dist&#39;</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span></div><div class='line' id='LC429'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="s">&#39;dist&#39;</span><span class="p">][</span><span class="s">&#39;name&#39;</span><span class="p">])</span></div><div class='line' id='LC430'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="s">&#39;os&#39;</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span></div><div class='line' id='LC431'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="s">&#39;os&#39;</span><span class="p">][</span><span class="s">&#39;name&#39;</span><span class="p">])</span></div><div class='line' id='LC432'><br/></div><div class='line' id='LC433'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span> <span class="o">=</span> <span class="n">os_list</span> <span class="ow">and</span> <span class="s">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">os_list</span><span class="p">)</span> <span class="ow">or</span> <span class="s">&quot;Unknown OS&quot;</span></div><div class='line' id='LC434'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os_version</span> <span class="o">=</span> <span class="n">os_list</span> <span class="ow">and</span> <span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;flavor&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">result</span><span class="p">[</span><span class="s">&#39;flavor&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;version&#39;</span><span class="p">))</span> <span class="ow">or</span> \</div><div class='line' id='LC435'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;dist&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">result</span><span class="p">[</span><span class="s">&#39;dist&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;version&#39;</span><span class="p">))</span> <span class="ow">or</span> <span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;os&#39;</span><span class="p">)</span> <span class="ow">and</span> <span class="n">result</span><span class="p">[</span><span class="s">&#39;os&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;version&#39;</span><span class="p">))</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC436'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser</span> <span class="o">=</span> <span class="s">&#39;browser&#39;</span> <span class="ow">in</span> <span class="n">result</span> <span class="ow">and</span> <span class="n">result</span><span class="p">[</span><span class="s">&#39;browser&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;name&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="s">&#39;Unknown Browser&#39;</span></div><div class='line' id='LC437'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser_version</span> <span class="o">=</span> <span class="s">&#39;browser&#39;</span> <span class="ow">in</span> <span class="n">result</span> <span class="ow">and</span> <span class="n">result</span><span class="p">[</span><span class="s">&#39;browser&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s">&#39;version&#39;</span><span class="p">)</span> <span class="ow">or</span> <span class="s">&quot;&quot;</span></div><div class='line' id='LC438'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">browser_version</span><span class="p">:</span></div><div class='line' id='LC439'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">browser</span> <span class="o">=</span> <span class="s">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="n">browser</span><span class="p">,</span> <span class="n">browser_version</span><span class="p">))</span></div><div class='line' id='LC440'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">os_version</span><span class="p">:</span></div><div class='line' id='LC441'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">os</span> <span class="o">=</span> <span class="s">&quot; &quot;</span><span class="o">.</span><span class="n">join</span><span class="p">((</span><span class="n">os</span><span class="p">,</span> <span class="n">os_version</span><span class="p">))</span></div><div class='line' id='LC442'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">os</span><span class="p">,</span> <span class="n">browser</span></div></pre></div></td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.11137s from github-fe136-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close js-ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

