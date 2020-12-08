import { Component, OnInit } from '@angular/core';

import { PlayerService } from '../player.service';
import { FooterService } from '../footer.service';

import { Player } from '../player';

@Component({
  selector: 'app-players',
  templateUrl: './players.component.html',
  styleUrls: ['./players.component.css']
})

export class PlayersComponent implements OnInit {
  players: Player[];

  constructor(private playerService: PlayerService, private footerService: FooterService) { }

  ngOnInit() {
    this.getPlayers();
  }

  getPlayers(): void {
    this.playerService.getPlayers()
        .subscribe(players => this.players = players);
  }
}
