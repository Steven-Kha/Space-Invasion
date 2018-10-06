# animation time
# def update(self):
#     self.now = time.time()
#     self.sec = self.now % 60
#     if self.iterate == 0 and (int)(self.sec) % 2 == 1:
#         self.image = pygame.image.load(self.skull[1])
#         self.iterate = 1
#     elif self.iterate == 1 and (int)(self.sec) % 2 == 0:
#         self.image = pygame.image.load(self.skull[0])
#         self.iterate = 0
#
#     self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
#     self.rect.x = self.x
#
#
# put
# these in the
# run
# game: clock = pygame.time.Clock(),
# put
# this in the
# while loop in run_game: clock.tick(62)