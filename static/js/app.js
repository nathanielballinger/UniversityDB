'use strict';   // See note about 'use strict'; below

var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: '../static/partials/splash.html',
             }).
             when('/about', {
                 templateUrl: '../static/partials/about.html',
             }).
             when('/games', {
                 templateUrl: '../static/partials/games.html',
                 controller: 'gamesCtrl'
             }).
             when('/platforms', {
                 templateUrl: '../static/partials/platforms.html',
                 controller: 'platformsCtrl',
             }).
             when('/characters', {
                 templateUrl: '../static/partials/characters.html',
                 controller: 'charactersCtrl',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);


myApp.controller('gamesCtrl', function($scope, $http){
    $http.get("/getGameTable")
    .then(function (response) {
        $scope.games = response.data;
        console.log($scope.games)
    })

    $scope.info = {};


    $scope.init = function() {
        console.log("Hello World from games");
    }
})

myApp.controller('platformsCtrl', function($scope, $http){

    $http.get("/getPlatformTable")
    .then(function (response) {
        $scope.games = response.data;
        console.log($scope.games)
    })

    $scope.info = {};


    $scope.init = function() {
        console.log("Hello World from platforms");
    }
})

myApp.controller('charactersCtrl', function($scope, $http){

    $http.get("/getCharacterTable")
    .then(function (response) {
        $scope.games = response.data;
        console.log($scope.games)
    })

    $scope.info = {};


    $scope.init = function() {
        console.log("Hello World from characters");
    }
})

