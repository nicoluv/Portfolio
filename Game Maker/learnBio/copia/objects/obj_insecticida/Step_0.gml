/// @description Insert description here
// You can write your code in this editor

if keyboard_check(ord("W"))
	y -= playerSpeed;
if keyboard_check(ord("A"))
	x -= playerSpeed;
if keyboard_check(ord("S"))
	y += playerSpeed;
if keyboard_check(ord("D"))
	x += playerSpeed;
	
if target != noone{
	if instance_exists(target)
	{
		if distance_to_object(target) <= attackRange
		{
			if canAttack = true
			{
				canAttack = false;
				target.hitpoints -= irandom_range(damage-5,damage+5);
				alarm[0] = attackSpeed;
			}
		}
	}
}
