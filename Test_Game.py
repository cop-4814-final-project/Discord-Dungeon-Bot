import unittest
import BattleSequence

class TestGame(unittest.TestCase):
    def test_Game1(self):
        self.assertIsInstance(BattleSequence.char1, BattleSequence.character)

    def test_Game2(self):
        self.assertIsInstance(BattleSequence.randomEnemy(), BattleSequence.character)

    def test_Game3(self):
        self.assertIs(type(BattleSequence.enemy1), BattleSequence.character)

    def test_Game4(self):
        self.assertLessEqual(BattleSequence.char1.health, 100)

    def test_Game5(self):
        self.assertEqual(type(BattleSequence.char1.level), int)

    def test_Game6(self):
        self.assertEqual(type(BattleSequence.char1.getName()), str)

    def test_Game7(self):
        self.assertEqual(type(BattleSequence.char1.getBattleclass()), str)

    def test_Game8(self):
        self.assertTrue(type(BattleSequence.enemy1.getStats(4)), int)

    def test_Game9(self):
        self.assertTrue(BattleSequence.boolLevelFlag, True)

    def test_Game10(self):
        self.assertTrue(BattleSequence.tempBattleClass, ("warrior", "ranger", "castor"))

    def test_Game11(self):
        self.assertTrue(BattleSequence.char1.battleclass, ("warrior", "ranger", "castor"))

    def test_Game12(self):
        self.assertIsNone(BattleSequence.battleSequence(BattleSequence.char1, BattleSequence.enemy1))

if __name__ == '__main__':
    unittest.main()