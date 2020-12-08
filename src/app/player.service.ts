import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';

import { FooterService } from './footer.service';

import { Player } from './player';
import { PLAYERS } from './mock-players';

@Injectable({
  providedIn: 'root'
})
export class PlayerService {

  constructor(private footerService: FooterService) { }

  getPlayers(): Observable<Player[]> {
    this.footerService.add('PlayerService: retrieved player data');
    return of(PLAYERS);
  }

  getPlayer(id: number): Observable<Player> {
    this.footerService.add(`PlayerService: retrieved player id=${id}`);
    return of(PLAYERS.find(player => player.id === id));
  }
}
