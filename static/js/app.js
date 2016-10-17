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
    $http.get("http://www.w3schools.com/angular/customers.php")
    .then(function (response) {$scope.names = response.data.records;})

    $scope.info = {};


    $scope.init = function() {
        console.log("Hello World from games");
    }
    // $scope.showGames = function() {
    //     $http({
    //         method: 'POST',
    //         url: '/getGames',
    //     }).then(function(response){
    //         $scope.games = response.data;
    //         console.log('mm', $scope.machines);
    //     }, function(error){
    //         console.log(error)
    //     })
    // }
})

myApp.controller('platformsCtrl', function($scope, $http){
    $scope.info = {};


    $scope.init = function() {
        console.log("Hello World from platforms");
    }
    // $scope.showGames = function() {
    //     $http({
    //         method: 'POST',
    //         url: '/getGames',
    //     }).then(function(response){
    //         $scope.games = response.data;
    //         console.log('mm', $scope.machines);
    //     }, function(error){
    //         console.log(error)
    //     })
    // }
})

myApp.controller('charactersCtrl', function($scope, $http){
    $scope.info = {};


    $scope.init = function() {
        console.log("Hello World from characters");
    }
    // $scope.showGames = function() {
    //     $http({
    //         method: 'POST',
    //         url: '/getGames',
    //     }).then(function(response){
    //         $scope.games = response.data;
    //         console.log('mm', $scope.machines);
    //     }, function(error){
    //         console.log(error)
    //     })
    // }
})

