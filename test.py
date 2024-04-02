class TestBoard:
	def __init__(self):
		# Initialize player 1 and player 2 zones
		self.player1_monster_zones = [None] * 5
		self.player1_spell_zones = [None] * 5
		self.player1_extra_monster_zones = [None]
		self.player1_deck = [None]

		self.player2_monster_zones = [None] * 5
		self.player2_spell_zones = [None] * 5
		self.player2_extra_monster_zones = [None]
		self.player1_deck = [None]


	def display_board(self):
		print("Player 1's Board:")
		print("Extra Monster Zones:", self.player1_extra_monster_zones)
		print("Monster Zones:", self.player1_monster_zones)
		print("Spell Zones:", self.player1_spell_zones)

		print("\nPlayer 2's Board:")
		print("Extra Monster Zones:", self.player2_extra_monster_zones)
		print("Monster Zones:", self.player2_monster_zones)
		print("Spell Zones:", self.player2_spell_zones)

	def summon_monster(self, player, monster_card, zone_index):
		if player == 1:
			if self.player1_monster_zones[zone_index] is None:
				self.player1_monster_zones[zone_index] = monster_card
				print("Player 1 summoned", monster_card, "to Monster Zone", zone_index + 1)
			else:
				print("Player 1's Monster Zone", zone_index + 1, "is already occupied.")
		elif player == 2:
			if self.player2_monster_zones[zone_index] is None:
				self.player2_monster_zones[zone_index] = monster_card
				print("Player 2 summoned", monster_card, "to Monster Zone", zone_index + 1)
			else:
				print("Player 2's Monster Zone", zone_index + 1, "is already occupied.")
		else:
			print("Invalid player number.")

	def set_spell(self, player, spell_card, zone_index):
		if player == 1:
			if self.player1_spell_zones[zone_index] is None:
				self.player1_spell_zones[zone_index] = spell_card
				print("Player 1 set", spell_card, "to Spell/Trap Zone", zone_index + 1)
			else:
				print("Player 1's Spell/Trap Zone", zone_index + 1, "is already occupied.")
		elif player == 2:
			if self.player2_spell_zones[zone_index] is None:
				self.player2_spell_zones[zone_index] = spell_card
				print("Player 2 set", spell_card, "to Spell/Trap Zone", zone_index + 1)
			else:
				print("Player 2's Spell/Trap Zone", zone_index + 1, "is already occupied.")
		else:
			print("Invalid player number.")

	


board = TestBoard()
board.display_board()
print("\nPlayer 1's Turn:")
board.summon_monster(1, "Blue-Eyes White Dragon", 0)
board.set_spell(1, "Mystical Space Typhoon", 0)
print("\nPlayer 2's Turn:")
board.summon_monster(2, "Dark Magician", 0)
board.set_spell(2, "Mirror Force", 0)
board.display_board()