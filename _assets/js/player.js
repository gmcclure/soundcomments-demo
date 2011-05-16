$(document).ready(function(){
    var provider = null;
    var sound = null;
    var player = null;
    var controller = null;

    TimeSide.load(function(){
        provider = new TimeSide.SoundProvider();
        player = new TimeSide.Player('#storyplayer', { image: '/_/js/timeside/ui/demo/waveform.png' });
        controller = new TimeSide.Controller({ player: player, soundProvider: provider });

        if(sound){
            provider.setSource(sound);
        }
    });

    soundManager.url = '/_/js/timeside/ui/lib/';
    soundManager.flashVersion = '9';

    soundManager.onload = function(){
        sound = soundManager.createSound({ 
            id: 'test',
            url: 'http://localhost:8000/_/sound/cemetery_nights.mp3',
            //url: 'http://soundcomments.thirdstone.net/_/sound/cemetery_nights.mp3',
            autoLoad: true
        });

        if(provider){
            provider.setSource(sound);
        }
    }

});
