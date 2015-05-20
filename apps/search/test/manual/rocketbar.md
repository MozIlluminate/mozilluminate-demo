Feature: fxos.rocketbar

  Scenario Outline: fxos.rocketbar.search-provider
    When I search "<search term>" using <search provider>
    Then The search page of <search provider> that searches "<search term>" is shown correctly

    Examples:
      | search term | search provider |
      | star trek   | Yahoo           |
      | star wars   | Google          |
      | Dr. Who     | DuckDuckGo      |

  Scenario: fxos.rocketbar.launch
    When Tap the rocketbar 
    Then The rocket bar search window opens

  Scenario: fxos.rocketbar.close
    When Tap the rocketbar 
    Then Wow! Rocketbar appears
    When Tap the "close" button
    Then The rocket bar search window closes

  Scenario: fxos.rocketbar.explode
    When Tap the rocketbar 
    Then Wow! Rocketbar appears
    When Repeatedly tap the rocketbar, furiously
    Then The rocket bar will explode (Just kidding)
