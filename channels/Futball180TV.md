<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn5.telesco.pe/file/VS9ycGDwkyM_LDGem8vnhrOOE_jlRKoWlSvqrL5s9crBUtc3-N1H-8ySSq4148fhEGpNwbvHMVLnC_1szn2mA1JbssfugsO3mb2CPgqS_plD4h6oSqDVO-klBkDNRey1aXTvw5yuANzyF_B0HDPYU825v4W9jnSkSLpYzBQYGJQvIVYas2oMig9nyFIe08Q5nS46tJExidY7wJtlb3nbRkSjRW9X-FwoSpk0FkeQi7UygY3t22kaMe-7XP0ZyjjdM9AAWkYXVbPbTVkRzKifefZUmYEXV50atURcd48OhDXcTlAna_SA5ANxVBmDUULS2GseMjcOHjxRyykyIg2j8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 423K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-105817">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=KlNw6YP9RXnuQUWFz_arBzJNCdY_9u9cRaY1yaLYX0n6svjb1ERIorYY9DLwoxO447YP-aLy92Cv3rUOfxuJk4QE6D5NT50RLEEfe8CKafNr1y_4v60xi5JlPjdjhSYtGL74Pdkca0yZ8QWyFMY4602V3hRwbTcHBtwtVkwa-bXc03vzr3wh6a2uJk6A_idYoXgSuZDIsojSpKQi2_IdL7SGnzGeV9UCG8nsq-7TLii9Oio0FLKFQe2iKQYQbphmLsVUopFvkY0Uq4pMGN2qtt6qfRYAZzDh6o8hjWbUw8887gNWea8omx5vRKrpXyOw5W0CdFpjdhWpEoVyZ9g1XwWaRVyLVmKKca5XVkxt0aRX1-KI8pQ6y3_TpVqP4DNPG_WneKY9SO1EKWn8cDfDqBzr4PkmHyS23AyV4oROPq3TRfAIetjyr75ZquyUmtu958lIrYB57jwL53OSYhacICrpmrjQnsYBVzFq66xhgTxsXttako99FM6BSajByPcVQJonm8jtlEqtg4q6bg5I0kKYL_PXpO4Zd03bvWE8xr6Ky0ix9D14yUqdY2YaIZDdEZ0G8JzkWZ3Wvy9OcmxbIXYOrdjOz14L1Gc4KD99XE6YzjNSwx_Ns1FSMxIyfZ3YjKBfn3Rwq2So9Nl4p_lmEr5d1QzVx88D5kpY_HX2k-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
گل اول پرسپولیس به ذوب آهن توسط علیپور(43)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 309 · <a href="https://t.me/Futball180TV/105817" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105816">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بالاخره پرسپولیس زدددددددد</div>
<div class="tg-footer">👁️ 612 · <a href="https://t.me/Futball180TV/105816" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105815">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">علیپووووووووور</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/Futball180TV/105815" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105814">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 305 · <a href="https://t.me/Futball180TV/105814" target="_blank">📅 19:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105813">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd555c5d54.mp4?token=Ic4rU9CKooaXU1yW19uIrfTz39rsr6Phj813DuLnwgLJb-Joz07GU2md9TIqYDgS8qsPidDaHFsBaniIizKH3dRBjB_moex0bVLGnG19YbmEZh4v1OedHB6MxwYAl4GCj7-Rkieoy2PicQdYl2F4KWukluxgHJEc7zCAr_KXEizDbAOlu0udpko1gRR99VnNSkGpS1RUcwYDNSpxtoLbLHkDtgPymrO0rHfm7i04OdLI6QXaX96U-mKd7D0Ox6IyDOhm0JTJJlyC4BtQum18Wq2kxkH33yMR9z6SWatsaRGPSS1-oC82kqwtcenoVwyrIXVIHqAohm34kTpeHMoyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
واکنش جالب عبدالله ویسی به خراب شدن موقعیت گلزنی تیمش مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/105813" target="_blank">📅 19:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105812">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21d11818e.mp4?token=O-kzBmCV8Asm1ZJcmmeXOyPsPNl-YQokiKK03x8M2L3VKbgtqcMZ9KxGT9AeSWJgbDZh9SfFCwZak1S6uCixW6EvjG26HTHF66esDx5SU-F6qiq5wjTUMrXb0vZ4uKpyWHzsN0OJ6ik3TNp5B9QERHgmUotLAluiLgpXAaS1owcIsqtmR1oUwg54iQYX33pLS5Oe6HuJtV91_Jgw0ZMD1De3SrwyN3ILy7yL9oC8ZGfjj6klWZFyH3FVVV44m8loQB0ce_r45Z7xh8ozyLhII0sx1X0S7UdjxrZOB40t_MGD3Bhki-HiuiGmOIw3Z1E-N9PVbjjJIbpuZZKwdu7XiBBy3I2bacNzHTdaekQD00iXyVxu4RtXmQOs0qeiOD3Mz2uyzD-INzp7IaCxsaHQh_GlaxIvr9jD3CPCYQI416IS0zhSkkhn_JxrjDayQ2G8tTysb1r2yZFu_HqwYChAM_Krx6H-b4t2d-LImL60VD-VbiMKeWvHrDjtGcKAz43Oh81SmeIa4aqAZXcXqp9jeA8gANbGPJVJmbIJu1vipZaCpEk219XCa_oP9S71qkB5CDZRpNU0ReQCMnSIaD334BClSvjigVPc5Eb6xiP_4Xma-qL16B5N92MRLzVrHplqIMBA5gAzdf6LPUJnxQKGwgEAFiUnP2ZMAIYXWBTzCO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت سوزی عجیب رحمان جعفری مقابل دروازه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/Futball180TV/105812" target="_blank">📅 19:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105811">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8676bf1957.mp4?token=HW_JumWO6gcAW7rVCqWsgw_adCOcwW5lZ3cyiduP0d5dAYQHObwG2hHsgKo-AJ_xQ1jnWooSorstEvM8qOKvZ_PGEH6dslBp0J7-_9zIklvBETWMztmtzEhnT5r7ATOqHudBYJ8z_NO11VB7Cdu8fHXUij1Lcv2TRtBPZvdZwuQaTZ2gLLwj7e9fN8I3t55h79LV-kk5zvcuQRFkZtPw1SMQWrPX1fAK70deyCauPeLMfRxLeKhu_L2JiwbXpXVQefRinYX4Dhuo_YE8GsGyo4r3tKIX4-tTUSFnmRAY_0xcUA6shyGmZLM7dLTyjg3hdjXG5WAGGZq79WSaLz18dZNtCPRxk1bgmr0_mPevP7Kul0DO4g2a_uaX9MAl5d4T-kOfwa9TmUHqQqOwe7-l_-uhNFUKpMyLx_sb5nv7BW8lbV7j-U6LxyHhMWPic2tKhl7O1aPFaCt4BtNrOZl8zzJDnA68SpiEHBvBdVtj6xtiUItcnzhuTQRq-Xrf-uMNMju0EHhqqy3gPo5WII0gdFnfoHl-HekSL251P4ehFYr7Al0IvyNxIXb0yB8IPFXgz1c3-d2t6gWFxN7zfGqdgRDV2ik-1A8ERqhAXuiezjjnrFwF3lsKbrTOU6jYFUfPzKoj5ngllnivj0aYZECalHZF1GjFTJIwBaqeH5sjHT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🎙
عایشه‌گل جوشکن، بازیگر و خواننده ترک، در گفت‌وگو با مجید واشقانی در برنامه «رُک» از ماجرای آشنایی و ازدواجش با همسر ایرانی‌اش گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/Futball180TV/105811" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105810">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ0Gh6rzJWFxxT5u5qYT-JsFEsesnjqmWlVypnGSr1UjoG5Kb-eKm50TwnwVeC6h1XMADROBtvpwl39TDB_Z2JR-OBl_YMm4NgkUxN73BxuozC2enz0Z34T43KmWLHD2xur2ttZGveB7qy6btvcDqttrBoObDXAtwfR3ywmDzlLeVKeVh75EoX5C77_YFsH0EaX-ZaLl3AtbKx_jI3p87lgmjV3eXZwlXJ_tpBvTn26FASiyySQrxV1cO3QUZSVcPiPyy597y_lw3g626RgnS3T9o8RDJKBYyLBeMSOyIom53brLQBuWkBmKEox8bJ2EN9PMZh6GERbRUjdL4m02rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/Futball180TV/105810" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105809">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ7sDUS6sKJuCjo_harl7wGl-eVae0kvM0RizmpbhhQ2NC34ou_ZeStF6p-1LbS8h_4rQjMpLflqGv9raD5rl8vP8q9uYZkXFLuM2D0X6YEacEeX-ODo6gCte5J-ENnePNRmdxXv2BCSa1NQ-DbQkMx9pne-gpO0YCnoxwE9rxCuKz7iYT2pj5mecDldPunEEe3OCFQZDe9Pq5VO9M4tHNxiiTtUuxL6m6kf4QzmIGBUTUhyqNO54NEUEOzxiy8zqlm0AXAk_ojEqbJai-n_oH82Bxggd1QZLKMTeMb6E2I7eOmGeTyS0cONreb1fnxvA4jvvAiD-EEIWqX77j49lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🏆
اگر حق رای دادن را داشتید، به چه کسی برای جایزه توپ طلایی رای می‌دادید؟
🎙
کیلیان امباپه:
🔴
من برای خودم برای جایزه توپ طلایی رای می‌دهم. این یک جایزه فردی است و باید دید که بازیکن در سطح فردی چه دستاوردهایی داشته است.
🔴
برخی می‌گویند که من یک فصل بی‌نتیجه داشتم، اما من هرگز برنده توپ طلایی را ندیده‌ام که تمام معیارها را داشته باشد. آیا بازیکنی وجود داشته که به طور یکپارچه توپ طلایی را برنده شده باشد؟ نه. این بدان معناست که همیشه کسانی هستند که فکر می‌کنند بازیکن شایسته آن نیست.
🔴
اینکه من بهترین گلزن تاریخ جام جهانی هستم، چیزی است که در ذهن مردم باقی می‌ماند. اینکه من بهترین گلزن تمام تورنمنت‌های بزرگ هستم، جایی که بهترین بازیکنان بازی می‌کنند، لیگ قهرمانان اروپا، جام جهانی، نمی‌دانم آیا کسی قبلاً این کار را انجام داده است یا خیر.
🔴
من کسانی را که با من مخالف هستند درک می‌کنم، زیرا این یک دیکتاتوری نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/Futball180TV/105809" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105808">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32837e6be8.mp4?token=cI2rgbKxTonIdp22QEAUcpo9-QriJ7InDVMNWe--SMlLnED4COeCeC5pNTLQyJQJ-QZkBIQCixHmUVzha1HFJ_y1Y2Xq1HMG0J8en1fuxAQ0Yc1wB4Wk8seR1vSktiPmH_4EXLnaR9ff6Ja1WWB2vASu7pRRJ0wYtU65WZrPqcGK041l5oYAKItD6JwxOyzpxpqBcYWb-pFtx9VBMPhpC44FVyw1Wa4eUn0OQROgqjcZTBax53wy6RkjLaYrmOfjAJa9NzswfY-I8pcDqgSYR9upwm2-CSopHvZniJqvH_IA7_1ORYkXAD70J-FgfkXgH4fhvQYMQiuTKn28Hb2-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
بازشدن پرچم 6 از سوی هواداران پرسپولیس و کری برای استقلالی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/105808" target="_blank">📅 19:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105807">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OBLXf3P-jrh5pADKrlXbBuhNqSfuptC9Al8Ko_7DZ3KqQw2fUZ0FjqbR9n5H_YunQ93tk8z2yLOd5l6JVHZZ5b5EoBC3JTBGo5uyMTfXg6fxYZ8bscWXM8XNCnLWk24v5hzrst7ExCTqzHOqgVCBYu58tkCml86_0Da1NLWnsc83oul0rXgjAsULqJBnBSkrIZSrHvxUx8pd9cYjqJK15KlY7tj3TXpuoEENo-v-DOxLybo62LPzxozE0mV4m2rPg95j-uezlTpUHjtoBfOdF6EO5cbhWVa0VZ16e6WMDuSFeIoaTKJXVPqGmta-QOKElWjQNADNtfgz0SJwAph5ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/Futball180TV/105807" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105806">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105806" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/105806" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105805">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4au16FRUIpVzLDDVRZRo9WrPuJnRDq2OGDzUD_54dWENce3dYgjtQaVY5L85g-yYgqwtA8a6iMWkt3C5otJNdD6Hrijs7jcl8BsDXrYCWq7h9B8SNYUyUtUlhZYmtHQKg4M7JSkAG6ULWZ9B8dwf6yDLatEgpHAc7FlL1w_zIXQcjYhHIsSWZukajQlEOd16JFJYMlZvsjAe-rm2uzjHdrifxjISd4jk6iMGyGT1xEDv9cm2BEaY0tq0J54bakdhLeX1LefCoCgrq6infbdkWfYTb8XCYMghvfRqjNaEn2iFh2T4r8eMifJ3zWOlausina6VUWCsDsukeT-A-qxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/Futball180TV/105805" target="_blank">📅 18:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105804">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeAIjcaPSDb4z7Sx1d_0bdEl3GazV1_yWbWT2qkUxsdYdXyspSXrQ2A-gORq6B3IQj4kO07aD8eQ_dSFJ4mYtRFphGUiZ33f8cu9o1v6YqcZDL4yYDZjtjKmiOHibTl2l1TH6UVv647Ja5-0Oj1mSah68R93NNr6WYPusqPeidGCl8WO-5k-LsvymeFnyFyMnY9ziZQJDb6wa9qK96E5FWK8hu3rexXTtnpMKBJcmTEoJ1NoQFXEAmENUczBiPEzanoy-v2KeuEiMyuCTl5AXZVPUhXfafP5c197cTlezPmfmjkk4Ick9C78hNQu5PPbz6sx1wAeE3o6jnwuA0QCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
شماتیک ترکیب پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/105804" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105803">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b66914acac.mp4?token=aRFmDZmb2lXdExf1uH7W4xncv_eALs7ugalpoZ4Yt3Uo11GhEIQoe-EPpvNIaSFNVz6AyWdJ8la-4T0kne4u-16vfLEIum39CmROdvNnuR4_oxfTcR6P4xFl4V7c4qXQTqNfW_evcYKJ4ldBw10t7gWlzqKLD4sZlJqW_EX8golY_itN_b1dCy1S0VPsY4e53OTtRmDdooVXQizwX45dnquZAxHnYKzgy7AHjba5cbYmMTwxPawxsDfnFz7DSam9IPdDgtOQ3Zxexds-sdDTi9XPjMSuEVDbw7EnDoqXKVKf7N135Ucd558m3MsPuGyXLOfUYNfYqZe968IhbIja6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇺
🇪🇸
خولیان آلوارز در مراسم عکاسی UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105803" target="_blank">📅 17:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105802">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdea9220e8.mp4?token=CsisuHAoNrZyEirsKQdYno_40xdYTPAqnFYSRDHt-8zC2YpU65sPGgA5XUXZrVesBeD9iSXxuh4r_aKxBcPny8uzQBI-I7353ktwfWKb7V97p7POYW4eZj5Psf_ACpOMXeb1Kx4B4N6IYP41TU4et36YqdHElMJGsBBNlUjz-4ER5w5bwZOTfT_cuZWvTPiLVKlIgEvGqtHhETV6Yr_glZWGCRkyfgD3GEeEyhKv2IEBcNv7qP3q45dZL7Kyc3Rq5unugs-cO72-cqWXdeowa5lFyy1inpliiXzUTXPYqJ0F6MtMRCIaJk7ksz1ZDjDP0la7IgTV_zRNAe9_Yyjc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
💙
پژمان ماندگاری مدیر رسانه ای استقلال: با صالح حردانی در ارتباط هستیم هم من هم باشگاه، ولی باید زمان بگذرد تا اتفاقی که بین باشگاه و حردانی افتاده است حل شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105802" target="_blank">📅 17:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105801">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e983fd5a.mp4?token=EM4TLBeEMQn-1E0panmcW4eZ-IYx1Mabukbj6Okng5H_u431QCyVuHnaMWT1UypJeUijZpfwEZe3MUc_4bD5VxA2lQxVr72KFGFxC9DdVAcjUfphQib8zqXPd1YVnWDes04e9IE_5hOtO1aIg2bViTTsKX07EbxdjyssDir6-xKP1JIMKpgRmKMD-3ivb739XdJi9EEARbHjSgeQU0oqlAYYn2LAzCehN3-KC5Nxx_QCa6AOetsDZW_o2SRS9pzHfNWlaAjRIniKrQKrHWi4m9TDypem39mChSKv19Iqxj_yngcSciRX1oWGB3N91kGBcDweJzoGGDZsLINbK3MkGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
💙
پژمان ماندگاری مدیر رسانه ای استقلال: در خصوص ماندن یا بازگشت صالح حردانی جلساتی در حال برگزاری است اجازه دهید خود سهراب بختیاری زاده در این خصوص تصمیم نهایی را بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105801" target="_blank">📅 17:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105800">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e25adb5.mp4?token=P2-HON9MhJ32qGhMRMffskdayOqNuIZPTzogvmIKgee6qD7k7MwWNUGH1VamMxXY4x8xW-zHmcPsLiuDbCBNteBsrjCXyAV4RfG9YCaLhmXoLl6zSEVHyZ3GHuTf3aB5u3Dr19kCKHJZVE1QqcFrG7CnTL5k4oDElXKBVi4AQrb9razmc7QGM15p-cKCnRMAfcjpQXQR8yNuSb3uECv3ueSudBLHYicN9ElpjRXe4RaV7nxlHIqLubhY61oPS-F3OPXK-8VZ0tbSsnhLzh6dkhguzpSSwphDh8q_cDfbpL8gaELVCroZUYttUPWREi09m6eonkzoXDWRgeOLFsd7Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پژمان ماندگاری مدیر رسانه ای استقلال:
🔺
مصاحبه پخش شده از بهاروند در خصوص قهرمان لیگ تقطیع شده بود/ آخر مصاحبه می گوید که هیئت رئیسه فدراسیون فوتبال می تواند دوباره در خصوص موضوع قهرمانی لیگ بررسی های لازم را به عمل آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105800" target="_blank">📅 17:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105799">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75db3430f.mp4?token=CCBPyMk66kYdDQK_IJ9tAALuKWMyAC-jWb3w6-1nQm5t9Bv8lOGLJpv8X5GOYf7fXc0E1d_p6jON7bmeFix67Ee42shv_wQlEa_vw_h5dPoSGTk1oo9EJovy4cYF5t8qwNuMwo4SY6e0ZK0Mt6ChTqWQ89N5EOIdCdPpfxy_6N1rFk7aJG5NbEGVv0rbc_T__gSsFlx4ZzRrbBYPKpFgeS_W7GHIWGldNIFhsXrjWxCP21UBtOWlJAMozJcN8ccKohPihthsavhdvBnDnUkQALgNS95f8BxL-gJcTrUl4T13G1USKNQuA7OrST-4x1iqsSqQgigbFJ6wbuPEgcedsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
هوادار پرسپولیس
: ای کاش خداداد عزیزی سُر می‌خورد و آن گل را نمی‌زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105799" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105798">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65105bf5a.mp4?token=RIz0g9GR5U6fs0JmXAgRLUhGhp78iMeDSjQ56FgBUBllXspoMM129D9Ifgaz7W2vu2AA9gQ9eIYmFRHRYlVcavp8agoAkxgCiqVJZLhhz08z7NP9NP6A-gJouxElrJBZ9o0L3NIIFv0bZ8r2jC8SPq9lnkPFZwvcRjaqzDAgrY0fYpqLoIss0tQOy-lszsvnZ9OX1LDdSr2bL-HxJde6yiBBy2fI0KV-o6nDBQ4bpKZk4Zh8CAmIi6Hp2qqus4q86Th3D_SGbl7hXu4Ejo1rnsereQNeqGGTuKWtBdtYjiwZwh28GE0_nPCgPspwYtCnyXhzC-jbHyvyLgtZLSjvOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون‌شرح :)))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/105798" target="_blank">📅 17:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105797">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce531ef9e.mp4?token=WC70BD_FUEeQyMf_yk8rzbA510to-y1aAImnqAH-BjnnihBpN0m-qgxt9I6TqZUuPDKEV7KF20JrTOLiZvSK0iEQrch2b-nRUgNjVoJM7BZRGAgXBAsNDZnGQL69xds0fiywycs-ViC8X0o6pp_iwK5kRc68cxgQk1OsDP3yJT4gygPSxvJVeHaYQSoQcLKXNPz_92y8lm2FIVMnrZt_kQN_tl8h9ahv2xniHEq3-2L4abXsiYsng24unVUS9azgSSN4miqnmRJMrMJdQCs9yKSyXBPPg4kauqeoMgaSrPikabsVfUURJn6RBmkZuOP1exlo6JaX2QJ78qGXLbbryw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بعد از دعوای خداداد عزیزی و عالیشاه آدم ناخودآگاه یاد این صحبت‌های اسطوره علی‌دایی میفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/105797" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105796">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc7d165fd0.mp4?token=idxTSOrbrC-9ugVWC2k7Cb01-a-iKYh8CjiNuy2RFjLWbnyz5XN3qmjuBHVYcqyvnxCOkVxMJzbDUDjNBHoR2nWsPmKCvpQBmq4jISREmjtXp3B6Ao3Lxm-xar2Lxid4MbiarwpHonwiiqmOeVWx7K0QUGNN94KZFAM6KAKUrUdEV9rXFFyRAgZU3oc1mDXdrUzH5ohn_EKgeSuHdP2GostTzJl_C4LdiTDmcuurOd0Rt-DBXCjRL98JdfiyYm-Q0Gyat8bRiYRVdTho64hgU5Q1i219a8z_jBs9YXD7j1qQTH9wJu9pO6e0ljWH55wq0tLDAMIWO9XbbBZwJ4Qlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
بزرگی و مردانگی یک بزرگ‌مرد، با حرف‌های پوچ و توهین‌آمیز یک آدم بی‌سواد زیر سؤال نمی‌رود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105796" target="_blank">📅 16:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105795">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=TS21B9WSvZHOKWuOSKZ5RpOtJy1sXCNiNxbLCzD76EMEj6cp0uAvfclnB8ZFRv-WlAX9wFnaak7gNVvfIYsXiELZqQ5f7t-G5ixNaVEtJ9AzzVqzk4PYFiam7NwSghMKFiFjxlBTKjeYv3JNFKSUZy51C8vJ6WeMRGrt7Yl0oyH5raB4gZrv3NqmyL1AdFOJDYzC71g-lyGaiVBXIZVjGY3AaR896sEE1ABO920qvFcTA_gys3OvDVGQoIaXwUYke1Q0hMEM41c9afI6KRyyH14H09FJXDEPrnnfXCgAnvksA9-L9v1NiNCkOaNeyUBjU8snlc8Ne3cyCXi8Z__bcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/608b5b0627.mp4?token=TS21B9WSvZHOKWuOSKZ5RpOtJy1sXCNiNxbLCzD76EMEj6cp0uAvfclnB8ZFRv-WlAX9wFnaak7gNVvfIYsXiELZqQ5f7t-G5ixNaVEtJ9AzzVqzk4PYFiam7NwSghMKFiFjxlBTKjeYv3JNFKSUZy51C8vJ6WeMRGrt7Yl0oyH5raB4gZrv3NqmyL1AdFOJDYzC71g-lyGaiVBXIZVjGY3AaR896sEE1ABO920qvFcTA_gys3OvDVGQoIaXwUYke1Q0hMEM41c9afI6KRyyH14H09FJXDEPrnnfXCgAnvksA9-L9v1NiNCkOaNeyUBjU8snlc8Ne3cyCXi8Z__bcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای خداداد عزیزی و امید عالیشاه از این زاویه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105795" target="_blank">📅 16:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105794">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNcLHH0wJeJYyZAwNuOFl-zR8TsXlAOaRSlRYZspFK4Ju7rI2hNXA__D-_yfh0itfz85KVRl7Mx463LxHMOJUIvP_sY2tFcRW0LqILIkANtw0hwQ8Q91lnbOkEr3YCtGc-9kJN9VEMVm0FrooUC9_VwLWq_IySOlLkGsMIdplQx5GQNx9Is9Ara5NKHaC4Y_cUIqiugNyqkfuK2sJMgJ_Y826B675NU-IguIu2gOn7qfSPg81sDnq9ehqeo9ThWcFrvaeQ1No3OMlpMTEvPtE8PSjbGRzO3uwQ9rBhApVVqIbHvUc7PmrPC14OYcVrQfxxVxZFX3ppZdMACzPeMLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
هوادار جذاب و شیک تیم‌الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/105794" target="_blank">📅 15:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105793">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72559f2230.mp4?token=hqPwtHSwuzqUUsf3TSOi_hkwltRBvkpEdCemLVwvzPWu-Fi27k1wWy4OxfABSZkCgHqEwqIJkrtQsQQ2YwLXAxq2RLQHjcE67QPMrWhbIOpJRnXP9uT_mB_0Xa6jhpXTlYl4bmr1UItAesMRLATjwVDzLotYXB6b0CVPJzvA7F9c8nX_RK8UyiO4ZMZeCseaR5tndqiUEz-7mBiI2SlsfNxT34SzMNwsenwvP_7coydSKogrFfkGcNMAHKrYFE-dWcRV6fdV9sNfswVKX8BI_YOYUt-lYMrJDzBgvCR3NIqxwFzeVsA7-BF5xA7ZSrMaYaBlO8FrXjaBTiO7T6Gpcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
جوری که دیشب هواداران والنسیا هنگام تعویض شدن پدری ستاره بارسلونا تشویقش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105793" target="_blank">📅 15:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105792">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2073e1633f.mp4?token=ApgOskQhJ73cndw7DOeAsGOanB4kU4SmvPte4EjiMJsnVWEtTO2teKdy8aMo1U_5iIHd1IWu9XWFfkOFwGiVV2Yrn_ZF5OG72TCF1iKNkHkiEo6a6mYkTCoSIG6KhC8QEeQTSQvkM5W8_L9XXZwNMP0YqIPMblkMVEsocXebFik5cW4mFnDWuHKwEWcNdZvPMdnVhZQNlCeeROL1F_9G9pjxCCgLWEljgpjmVgdA_TJmEGal42SuJ6VuMynNsSVw56EctyTdaBunNbMnNEVlA-E3J5Fqi9BdI-7RqQmSeOnktlW_kGFojZpaapWJ-6EPv0qZfuhZs0OjmOwDJuUmOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇪🇸
وضعیت شاهکار این‌هفته بارساییا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105792" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105791">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEeP5VKMc2hPVC6IabNwvAlYVQlivA7SmmQWPunl8EvHE5hjAWkjPQ8rrSc0jYDNg39oYm8lrKKRc2tuDuL1yO0iKCZt4vzhR2EChVjgn02VxFnj3tve3_Q_WMZI869kUzgEmLSWBifmOdTrAhQKDKS-0KYpHwu1e9vPfXk_Nj-gah4KUniFAPrRqnLSm42qK0r7uIcxlUPp0VDvY1fwi2Nocp2qP5O-GWSCKRoDIV2BdcJARUSZNm0Cx4OH2LSNCki1bToy6jO67WdQS2gdmXFkEcCTBuDTNKzqXR_lGxzwCtU5PiDieNMWladgC089AB-qb-HD1aqoqMNjT_t_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد بازی‌های لازم برای رسیدن به 300 گل
:
🇦🇷
مسی: 365 بازی، 300 گل
🇳🇴
هالاند: 384 بازی، 300 گل
🇫🇷
امباپه: 398 بازی، 300 گل
🇵🇹
رونالدو: 499 بازی، 300 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105791" target="_blank">📅 14:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105790">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7j1rB590KW0zz2ODRRTCdLfEjrpL1un8u_d7NcHsX0Fm5HrANGHqBQz13vZaLK0tGwY5YVNKpJLAYC0ct_e3vo2RXw5MbRHOtdV5ZT71-XaYVEnc6k-kxjKNENtyMiQ2sawZ46BTEvuLnB00wkoF5Qs6dnr-7t5iYuSLVpud5YqLMUkpUD122Mx57e6ZxPQnqNU2DIfO2Uf36T-BQRakhZOseHeUyz6g3ZtXH3zLqBLrk38sZjQaWHHYoZddS0gP6ayxE479QwHSZmFWrt-mRrQGixOScLPWi0vCgbJBfeB9nm-Jn9wDIqbWVOlLvhQnwS7-MHR2-yK-NFdHqJk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇭🇷
🎼
لیست تیم‌ملی کرواسی برای فیفادی با حضور لوکا مودریچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105790" target="_blank">📅 14:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105789">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iY4WNgi4sIDFAE9O4OEJLneMFN7s0UIie-FHjcXa5nAngaZc3twKDM4H7aYvKvJC-2rrcC6m1SsAFNHlCi6nPAhSsvWe22PwautemaeRH-QVdbqiqVEAPWVwXIYpS3whtdJOsTBtz8XwamJ-vJ6LHt9hWGYupITe24fqzfk_pWi9kFj8PLx1g85L_Ix4w2XFljv2FpN2kS3y4YZT505Mbx0Ay0hH9ecS_3fz516GwamHTjEEjCXCpqeG1xmzC3jDdpcYe7ox2z1yzE2EGS3FuTKQHd_WUl2l3H8fzcXAz9jD_02dQbKQmhtr7A328I3F8srCfLlni31S25GjFVUlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
این تنها سومین بار در دوران حرفه‌ای امباپه است که این بازیکن هم موفق‌به گلزنی نمی‌شود  و هم چهار موقعیت گلزنی بزرگ را در یک بازی از دست می‌دهد.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105789" target="_blank">📅 13:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105788">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d2063588.mp4?token=DAPl5WeuE6O5TlXkOQAgopDsSgyBzpPonUecw12TqYt5eAjnTZn40coDi304q_6kCJl8HpwGueJjbSHZQLYv0CnqP8bCFg9ieKN8rq-3YxZc-lKvBCApt3BXHJ8UqEWOdULKfHa3xCUI4vdq3mwONMwtELY2vre7XNAehDPGdyr8kW7sBSF4TztgY_-v_dHGACVM--QxTLOKevQl478ruJcpp_o3GC2PgH2oikP2_-4G8FlO6jkXlJx0BxK55LvM9zuTTog6-sa_SaNATc2MrzlitirvfLa9sULBWe9ko6YmBQPCboED_fx5EjMhR5ZWzfdCBsQkv2ao7GppfpM6TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
😂
امین‌رضایی یکی از اساطیر سندروم‌داون در دیدار با علیرضا منصوریان در بغداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105788" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105787">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/737dc646bf.mp4?token=PLnzUcmKhMWBMwMiAXYrtckTzJp-Qr1kgOL3uJCXbzPKZshE58_qty4MLxONLgRFGaR2sWgHABa2L3VZmElfBVj8surjMrBzOoXCnbjYJ5L2ee0iF_3V79bu2nCZDo8wQ28Ga3pZ99U_Vhn5klvEn6YJZTq5VJxG-2T-ll5ZTSl0lSftkIw50290EHHzJSS4UDqpN29UWTBOn50C_yNbnhuE5NXnNAmV1euwDD_4uSRDOcz8ab6XFAjoHvVUFCpMHn-EDqV4bch6WVMvzuePj_njpwJkrGiLlyTDeTysVaLA9dGjGthao8qsN9xYChROVyvv0-omwWyl15fdggmUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
حمایت جالب هوادار استقلال از امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105787" target="_blank">📅 13:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105786">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ca5c3fb8.mp4?token=gbekEcge7Dk7k3WkhaA7srWnjM9Iyg3HI4V4PSxAAAi-6a0b0OgjIS8rKEtyH47ANQG9yxsUO2Da6XDDjv1qWpezXtqOO5Oc1UXNxln6-RhhFGqWdZ3OEBxkUbu6VVYdrjaYZz8mPXa-P6yvm4nKtDkOdrSUFOAXWAB9-D91qtm5067E6ZWXek_BWPyHyjxmL3VkKShOvHHxQjToIB-DQs0ZATCcD1P28OdbjHFzVEtFPXrtE73HOpsnClYGmkx9MzHlgycX_B_B_H3ZRDPNyBe8VOOh-Jt7HyaeWn689-AlXOPIAQmdmwLobk7BXPeG68CJtaM7QYs5y2VwpD5goA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی سمی همسر دیوید بکام با ظاهر عجیب محصول کشاورزی شوهرش
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105786" target="_blank">📅 13:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105785">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeahcx8a1D-gytwELJMjEir1eU8s09D4dWm6WRNoF8AbgqGIkQY_GAnskQ43qZtaUbr8VhxHuYREUwSh2ClgFoQGS6BBS8dRRlcQLMS8-7Dkt0AMCvisfKRE4AHNwmIQrAFTk5tDv7CctB1N6y1QSUy05mZ_GxZUeVuysjWPdsHNnhwkpPhpGbCzdPv9thsfNkH9X_uFEfR6JvDOjStlJRga4XP9G-xSIfUFRZc2upUsl7Em7lnz-hoK6qZoVpeLrj4i01-Q4XjzkIZOG5CLFpH-o9fO8ar46wzEfLID0ap0P7EPD4WLo2TIdeKwGQjr-AO4wC5J-iXRGvtCynYoyszo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4072bbde8.mp4?token=vUf93SBCNoh5c4MkDWPI8skDLwwsPcOChsY-lAbSlZvNzdnGt2fCtVGyRo1mUdhhCN4pC8bWCb79a6Iqkuf8Ubj_TzWl6V9A5eGq1bw_jPm7y4PN_bjk69XfRXknv8U6ET6MGsk-E2ad3UBK-iDgFlm5wn5_s24X0JdFhRgZZfLHDSoMXM1hfaorNVJw6DKggk-NtXLkZMKbHm8ADjSUfbPiqJpGdFvg55yPIieY9HIB-NH5V-4S3NTRCOid9Kh6Kq_Spa8M0oOlUQeWMH3G-tw6f9v38HY2tanXNPyzh1B58-1K-a_tC-QidEtdGiCvN29TsBOG5FdAAiAL8UeKeahcx8a1D-gytwELJMjEir1eU8s09D4dWm6WRNoF8AbgqGIkQY_GAnskQ43qZtaUbr8VhxHuYREUwSh2ClgFoQGS6BBS8dRRlcQLMS8-7Dkt0AMCvisfKRE4AHNwmIQrAFTk5tDv7CctB1N6y1QSUy05mZ_GxZUeVuysjWPdsHNnhwkpPhpGbCzdPv9thsfNkH9X_uFEfR6JvDOjStlJRga4XP9G-xSIfUFRZc2upUsl7Em7lnz-hoK6qZoVpeLrj4i01-Q4XjzkIZOG5CLFpH-o9fO8ar46wzEfLID0ap0P7EPD4WLo2TIdeKwGQjr-AO4wC5J-iXRGvtCynYoyszo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
فرشید باقری، بازیکن پیکان: خوشحالم در پرسپولیس شاگرد گل‌محمدی و مطهری نشدم. اینکه بعد از جدایی به همه جا زنگ بزنند و من را خراب کنند، حرکت درستی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105785" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105784">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZataCB-NXxPzs080VhekdxbfOFkR1aT6vQcGGjMSza2KdeB8eeUrMB7FbNdMmZXMhqfWSGKajRGIYiHYWdKdss4xs-8pw1RdHKYzFrMs2hOfuv5WaI7brt688MASbjCpOnz1XPGZUOYiw8pr-hapXCKYCCdx1wKXQ0xdO8YkTFUoiXaVbyBaxMeBnAjYmG1ZoaYOqz3VTaAMB2RcwotU7s5WsPLj9ci5_hoA3iJUJnLCGoT8ihpL8JTqU8j62Qn2de4duQlR69-8egonQQctEYxePXuE6-3SxAywWpGY-R7mW5l1RpYcBbXHeQEJm1dakM04jknS76WQNRkMenHcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
👩‍💻
💡
یه راهنمای فوق‌العاده کاربردی برای دوستانی که با برنامه‌های آفیس سروکار دارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105784" target="_blank">📅 12:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105783">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=dA0KMcRWufHOWHGTYDVYr4B1O8Byeov50Wvj8CugmH9Mukolz061fd9rSgT1epo0_LH0CK_ElLVm0UmYkp1qfJOXnz3r_3XxeqvJCaIQHb2MrQjwbRJBy4UlsLE1u0KijFxhrr7aVWGo_-X1gqVZxBtIvHVjwciqLcf9xzm2OsBzkeNxnROvbj6z4H50FGij99n1EybR4HQ3fft53xuBpAHsv9x2DXg5Lfe6wYi3WN2SRQao6sWLZo9Vl3aDEky2JjRhQv9Nb09ttZjyiGXMlKsCicKKeOL-iB3Uyaz9pKvx2NMA7joP2doofmthma5N5AXnKoWSW_w3zQLx2yqWmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4331728b0.mp4?token=dA0KMcRWufHOWHGTYDVYr4B1O8Byeov50Wvj8CugmH9Mukolz061fd9rSgT1epo0_LH0CK_ElLVm0UmYkp1qfJOXnz3r_3XxeqvJCaIQHb2MrQjwbRJBy4UlsLE1u0KijFxhrr7aVWGo_-X1gqVZxBtIvHVjwciqLcf9xzm2OsBzkeNxnROvbj6z4H50FGij99n1EybR4HQ3fft53xuBpAHsv9x2DXg5Lfe6wYi3WN2SRQao6sWLZo9Vl3aDEky2JjRhQv9Nb09ttZjyiGXMlKsCicKKeOL-iB3Uyaz9pKvx2NMA7joP2doofmthma5N5AXnKoWSW_w3zQLx2yqWmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد آلمانی بعد از شروع فوق‌العاده در لالیگا و ۴ برد متوالی و ۱۷ گل زده: تقرببا بی‌نقص بود، چون هیچی بی‌نقص نیست و همیشه جا برای بهبود هست!
بارسای تقریبا بی‌نقص هانسی فلیک در صدر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105783" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105782">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105782" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105782" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105781">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncLzYKXSELUGDffKfePQ7uS-9gglwHsr6K27_SGmIAihJLpwwzrLLjhQfvQUU8cHZyMAn-GF3zNz8OEepQbzfxG3zedK2zB8TygRFXSO6JXZL4KLfMD-j8cs887RTFNKPEIQnhr7Uzq05zhjNCD6CX9VaYYoPzuFQx0owDOiidsgPc0c2Ni2lvcOIe30yzYVRRhrZm-9gVdIb4uR6Wm8z-G2PPJLBj0sDdv5AplC7_WnXbT6joLXgzefc7qlppK2VYkDl0dO_kIzIlpekPkmnOaQH8MwyqqbLMa6qPXJQcXqdc1K_XW4kr0L0lXs_0bPdB8X24lh-aTgdQDa_AxhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105781" target="_blank">📅 12:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105780">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1732fa7bfa.mp4?token=jH22a_UhXhBYICG4mzaS3WNiFAsXM_H4pITRyQ8mcXlDrvvw4A5RK5xpm6ZtFosTt7_fwFOQv0cG-oZJGnMdp8COV9mFT_bInMw0xgGvwqm-ekHrPqwwUVGpAO9ThCksY-Oob4jIDP3jMcSCNX98fuh3OhP73gHCOg0L7Fok1tXRlONKzLMRIkIunEGR3NTi2MboHFqCLD6KYpJqqEzdW1h0ZCDraGyPbqb8DpFiHUE6eXzTxHSXa136p3fCOIGgTgve3B-K93du9jYvvxtvlyMdl-ugqSsJXPoOrelxKDrJKvGKZF_QbmxnpGZ3S5Gg6WczMrvRTXYMpKOxMnSE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لندن مطابق سالیان اخیر قرمزه
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105780" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105779">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be20a40432.mp4?token=VUhdI5ds0ShRbl21JPSRahTtjQqW_y8u6_IYHani-7Q947oYHsUXIdQDuONjLuoZMzC4hfZc1Lq1koYUjB2npoL2BypLJzB1mTljfOIUo2fLynn23N1IjcIg3eevfx40k7vytNkLlw8Pd-J_0L_aWUROk5ED3Xw4Q83Te8ebA3JH4nTorUOjU-ox8oTEkaTT4AozgUlZ82M6EBwafmtuN6yqZ1FN3j15pjFCkRaAKlYaJocHxeWQCWyEjIlsYjH_39xE6oqoaFCWcjPoRxO02HVyov2-JSXUonF0zMaWz-AF3WasepUUOW2fDsKYgcea_4myEbp42is69CV0cTt4mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
⚡️
ویدیو بسیار‌کاربردی از بات‌های جذاب تلگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105779" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105778">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/872be66f89.mp4?token=Ygk8AtFl5mEZT1F2TwB9IP31dQlIATQQ7iB0fv9njX_KFkHr9Tr7A0VWPKr0HitpSLOSXoMzNZmoNLyoOJycPQurjzsVy-HjDUd_DuumMS4RyhcqnfWNYzVlqgGMltdP2n7PxHLkjNQANnv8h2fZ-wgixhCe5tLJlkC6C5VIjy4WKXIoJquEo8zUHYmaTkm6DpBPojHPVlNwIR2aYLQ98fWGakdZx0gjiNJng4HVGx18nXdl0-bUivLk8Y1Nbwf0j4DkvcmTETs7QHgoQQeo7cMIML2TuP5Z6x7L553KLCWIXu7jtsOBvQAp3tnKxSwRd1amOqhvZtUUwhaQo7XzNoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
هایلایت‌درخشش دیشب لامین‌یامال برای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105778" target="_blank">📅 11:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105777">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQw368piiEKlYeEqlpodWoA46zsH8sJXkAu0p-Lxl-lWn6y62JXl9Cnte5MDc7xs8jC25JzuGDmSnzA1RTSn3i1TejJnOK63n2zOGVBJY-zsUsxTY__MkG8EgwbtCorudKeYCgE8TfT0fmcROnoO5CffQoxTmBkzaKPShw5ywshTVmPiIfux8FmJpEWJRoAZe_oewOMj6QYhKhA282FHGmuzq3vdvnHwGo7V183HcCwXa6VG1pkIEW65RVyw5CxCRo0PdxZEMSUR2O_ZJWKi77utcI1oOu_VhDy84KCPpmvPxNHJCpLj5cneE_pqTzDmi_mZYZqaD1Tf8Am_VMcjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💸
بالاترین میزان حقوق در بین سرمربیان جهان؛ هانسی‌فلیک بهترین سرمربی فعلی جهان در بین ۱۵ مربی اول لیست قرار نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105777" target="_blank">📅 10:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105776">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
⭕️
با اعلام سازمان‌لیگ ایران، فصل‌گذشته لیگ‌برتر بدون معرفی قهرمان به پایان رسیده و جامی به استقلال تعلق نمی‌گیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105776" target="_blank">📅 10:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105775">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=EiOn1qHGKe7gDZF-E33RPqegWoSVmZwfu0gMxRt-xe45mZLx1R6J1c845yw4-xEEAxjqViHRj990mxjEfnAqdvzSKgbNQHzkArgVyfsDnqDw7-eJanSe-REmlLCnZ0md4dLe34Y3vf2XlBahJIVyMiJm2qufX2p8O65UKZImJW8jiPONvOOmY3DI0jKjvmJ3EU50fjZjMhWlTRHw5WRJc1GcjZT_xuSuVLGGEuZGj3ukGpLWajp98EPQv8CB0JcE9mBkwGKhikkLwRoQc3OUPka_w0z7gWjOtF48wcZ47s5gXYPEgaElnFpC_ClOGgz6oBm9VHSxd3qtPeBc1euRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60f25ffc.mp4?token=EiOn1qHGKe7gDZF-E33RPqegWoSVmZwfu0gMxRt-xe45mZLx1R6J1c845yw4-xEEAxjqViHRj990mxjEfnAqdvzSKgbNQHzkArgVyfsDnqDw7-eJanSe-REmlLCnZ0md4dLe34Y3vf2XlBahJIVyMiJm2qufX2p8O65UKZImJW8jiPONvOOmY3DI0jKjvmJ3EU50fjZjMhWlTRHw5WRJc1GcjZT_xuSuVLGGEuZGj3ukGpLWajp98EPQv8CB0JcE9mBkwGKhikkLwRoQc3OUPka_w0z7gWjOtF48wcZ47s5gXYPEgaElnFpC_ClOGgz6oBm9VHSxd3qtPeBc1euRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😢
🇮🇷
هوادار روشن‌دل تراکتور خطاب به شجاع خلیل‌زاده: به قرآن خیلی جدی میگم راموس ناخن پاته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105775" target="_blank">📅 10:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105774">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=TFKbOfpC2Gylnyy9_hkMRPVVhsjh_75SkC_KTybPBzXXWPXSCPDVoOkFFILAbxnHu8jr5mh_Ipe1U2SPnYnsErvIjkwpFA8DbSR-Oo1QzeTW2ekSybxdv22xJc0cNvhApjBRPn2Zh4GC-ZfMTIjztBzZu102BP3gumMsE7Al25NbaJhfBlkYBA4aL_OkAXb2A4rNeDY7mFQrL3beOiEKZpcprcZ0wddglWv-socJkNnNAPCUaKbRHZ8f9_-6F3JaV_R_84Bh4n_yTPBqW3tJ5R-PlcTu6ldZl2X-O8RAZNbZE2A3ZJx6_3zqCrwL6_0rKF36pARw4IzVqh7pZWdTDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ab9d20b35.mp4?token=TFKbOfpC2Gylnyy9_hkMRPVVhsjh_75SkC_KTybPBzXXWPXSCPDVoOkFFILAbxnHu8jr5mh_Ipe1U2SPnYnsErvIjkwpFA8DbSR-Oo1QzeTW2ekSybxdv22xJc0cNvhApjBRPn2Zh4GC-ZfMTIjztBzZu102BP3gumMsE7Al25NbaJhfBlkYBA4aL_OkAXb2A4rNeDY7mFQrL3beOiEKZpcprcZ0wddglWv-socJkNnNAPCUaKbRHZ8f9_-6F3JaV_R_84Bh4n_yTPBqW3tJ5R-PlcTu6ldZl2X-O8RAZNbZE2A3ZJx6_3zqCrwL6_0rKF36pARw4IzVqh7pZWdTDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه تند رسول مجیدی به فحاشی خداداد عزیزی: والله اینطوریا هم نیست که همه جامعه فحاشی کنن
…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105774" target="_blank">📅 09:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105773">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=D80knjKSa_Wtso7RibQjukHChCz0JXL1OHnPoa2ZlaI-64eq_W4tlxIz20i934hT9iJLfQwDb7btghwp-q19t9pSeC02cOGOMGtUYC9uNURoOFEEGCBPZOzvqU9GzTHiP7bEvlOpag-u5i84KZ7HPNdmu2zfpAC86_tOvSOgTw71wAxBDvXBdt1-75e2GGPPUC4ls9-483M8PJYob5NsJMpR5dHh7NsiV0TXJJnZfiVyOBSMzdys3y_wCtEEW12vT2XPk2UrjegYSxODeZYmNkrK6gR-HlVGCltou_zq9sYco5uu_g2eTWvlAUlQv_y2XOk0O6rTVWPWVcaCAl5sCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbdf6e4f5.mp4?token=D80knjKSa_Wtso7RibQjukHChCz0JXL1OHnPoa2ZlaI-64eq_W4tlxIz20i934hT9iJLfQwDb7btghwp-q19t9pSeC02cOGOMGtUYC9uNURoOFEEGCBPZOzvqU9GzTHiP7bEvlOpag-u5i84KZ7HPNdmu2zfpAC86_tOvSOgTw71wAxBDvXBdt1-75e2GGPPUC4ls9-483M8PJYob5NsJMpR5dHh7NsiV0TXJJnZfiVyOBSMzdys3y_wCtEEW12vT2XPk2UrjegYSxODeZYmNkrK6gR-HlVGCltou_zq9sYco5uu_g2eTWvlAUlQv_y2XOk0O6rTVWPWVcaCAl5sCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت تماشایی دیشب رودری در بازی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105773" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105772">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6-eLitZcRDaQtlulGUXmcPM2bcn_y7lR2WLmN3TW-h8YVj624jN0hYVl2O4RpfPShOxKFFQeIEu6vDRd2NglHeiRv6iDGbvp0v7QNQlWCwil6Ja9eBZAI5pYniyOj4nyv3raocWyWvBdEhd6-F2Ky7vOezALlHvv3kRuC4XTeh0i4tdtykY2Fx_XaFvgRTwRzLeu0wkTXNR9vo_4MP5yxiscv_DH5RAeFgNM4I1DoUwIvMVBhmGyvaoac0pUjob1GAG87J8uaW5RIvCP0WYR-nx1EF3peHwbQDh8NdTOiS8t3aYZbjejifgFr8vK07YXWqwKK_nCfr0Mk_rvtoeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105772" target="_blank">📅 09:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105771">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=Puyu1tXgmaXrRXJh0VVKaPAj3SV4mrsOlqvdwQgk3hdiOota2X29PO4mCdRESmdAAJAwvbD0PoCGtWKa_DFREgCQa7ofxsMuqfQfcZkqn8OtP8DZ6Xt6TSQDuZOB0EvedVDZ00qrtcdfJwNBTll3KsyjYv_detP_pAlrf8ahL7piP_89T9E3fWKGLq38o90nfqseDx4GHpAUevifP6181zQ1uSU_Gasz2MCYLbsUsK1Yr-QkqeFQaxJrdFaFBS5mI1GA591NXdtDalRxL9zPlEZGk6LZ8DCnJadf8MJMl4yKUxUdIkzpaNqz7IQ5UwAT8n1XgkK301c_E_llN7EV9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5650c1b3.mp4?token=Puyu1tXgmaXrRXJh0VVKaPAj3SV4mrsOlqvdwQgk3hdiOota2X29PO4mCdRESmdAAJAwvbD0PoCGtWKa_DFREgCQa7ofxsMuqfQfcZkqn8OtP8DZ6Xt6TSQDuZOB0EvedVDZ00qrtcdfJwNBTll3KsyjYv_detP_pAlrf8ahL7piP_89T9E3fWKGLq38o90nfqseDx4GHpAUevifP6181zQ1uSU_Gasz2MCYLbsUsK1Yr-QkqeFQaxJrdFaFBS5mI1GA591NXdtDalRxL9zPlEZGk6LZ8DCnJadf8MJMl4yKUxUdIkzpaNqz7IQ5UwAT8n1XgkK301c_E_llN7EV9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران آرسنال دیشب حسابی از خجالت مورگان راجرز بابت عقد قرارداد با چلسی بجای آرسنال دراومدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105771" target="_blank">📅 09:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105770">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=Ybny9rFkpzWH64EU23fxpPFhG6RmCxmclCkNXcO2xCuahuMSqP0lR_9tStXtr5X8Y9mgVX6p_UlCuWkDkuZe6xJReLmQRlZumxp8X-n7JZZ0XCEvtpgGBgORuZU0az-nq8gjCK8hJgMLGDkOo6bF7e8nC5Y_uolBKgtMBhOwd1rkSVS2cMjHpI-JQncABgyOs3ihzqGm2SXfKAoaqWAtUiZU_8eh3UQxV1A15J_hj3c4agp37F5EkVRgTZfFDC-u5oAu6aE2IoZEWsYhrK4sT7JfJYOhGny80Mk8w8HAg7Bg0rpXALSlmXaCjgZuo1oc_4cS_udhdepiU67Rvy_k3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e6028a7c.mp4?token=Ybny9rFkpzWH64EU23fxpPFhG6RmCxmclCkNXcO2xCuahuMSqP0lR_9tStXtr5X8Y9mgVX6p_UlCuWkDkuZe6xJReLmQRlZumxp8X-n7JZZ0XCEvtpgGBgORuZU0az-nq8gjCK8hJgMLGDkOo6bF7e8nC5Y_uolBKgtMBhOwd1rkSVS2cMjHpI-JQncABgyOs3ihzqGm2SXfKAoaqWAtUiZU_8eh3UQxV1A15J_hj3c4agp37F5EkVRgTZfFDC-u5oAu6aE2IoZEWsYhrK4sT7JfJYOhGny80Mk8w8HAg7Bg0rpXALSlmXaCjgZuo1oc_4cS_udhdepiU67Rvy_k3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله شدید وحید قلیچ به خداداد عزیزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105770" target="_blank">📅 08:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105769">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105769" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105769" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105768">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjJcXfc7PBbsulDmJrr6LLhAPqdV3RDdptwEfT7fkswwWmgINi_H91LezdbQXLt8L_WtrIkoFSY_yzlbzYv2rZ4Lcnz56Zva1Sccuk-uPRIzBXaXSQZMDD-52sRPckGBAStSRxLe2bCkHCfPTfUg3GcLdjlXL_rlXnLH4ZyXhe0n1XxFl7OinNzdpPur9wUhxJR-hv3P5AGbY9UiD76i4mEis3rtJysGPrj9XW9ETputT2sjSr0gPQo-qGwAbAvI7Hw40VFyldfONFFELGBz1mYWZktCj3I-46ej_Lb3eX1zmveopQzt77TI86dX_iDNh53G5ey3br9uUxCWzq3ojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105768" target="_blank">📅 00:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105767">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105767" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105766">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=rB8-ARWLaKEzQ9KEQY3wm4uKzQ95cspBJennnTLUfPH7N6lL7byZNnH428l9_Ob9xDYcdOXUvpdjg30Nx_trks44SPPma9YRwo6STpQWpVlaARD_u1SVXBc_a0sSc71lFQMBlGOul6ohI8zWsd4_oHMk0p2Xes62QICzFestfRy6rTwO4mqmvrgK87klMfuknJHBXjdlMh34yZPEm3L2f0aDtErVGruBAGHhIP6Nypi6WclLsn7dQrkGfdsB8Iv_m-2n0FnVBvdAwub_MJMq4uGfLw01-pkCxz4SBUrZ8CA9bczJQoVpph2vqjrd6RHyrn4yENa5u1xuamCijC3CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e26f7c6c2.mp4?token=rB8-ARWLaKEzQ9KEQY3wm4uKzQ95cspBJennnTLUfPH7N6lL7byZNnH428l9_Ob9xDYcdOXUvpdjg30Nx_trks44SPPma9YRwo6STpQWpVlaARD_u1SVXBc_a0sSc71lFQMBlGOul6ohI8zWsd4_oHMk0p2Xes62QICzFestfRy6rTwO4mqmvrgK87klMfuknJHBXjdlMh34yZPEm3L2f0aDtErVGruBAGHhIP6Nypi6WclLsn7dQrkGfdsB8Iv_m-2n0FnVBvdAwub_MJMq4uGfLw01-pkCxz4SBUrZ8CA9bczJQoVpph2vqjrd6RHyrn4yENa5u1xuamCijC3CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
🇮🇷
سجده جیمی‌جامپ امشب نقش‌جهان با پرچم استقلال مقابل سیدحسین‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105766" target="_blank">📅 00:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105765">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Euv0MaNobX4O2MI4wNMG496ZI7d8FsU4eFRfQCdnpd_EauZoQTAl391hRO7Jo8JORCR0oK6n6HA2K1mMOFu3erk75zRdBNhSCk4YzSQDiY1fsBKocfIhpLYyuKePGBohGQGZt7Uc-Fpv3UJX1HZH0GfsHtm7sMpLXwEzDfetrMtrBrbsjNb_kUenxpPu2hTNp5HATIUWw9zpKrRxxkFtq1yaNMJOK_VzCFqtAV0iLD4g_lsXY9I5mBE-7q9CKzdC_Mrhfv-VYF4zd_FALPvCHH7QnDdw5nw-tYmAXUbIvWsun8o3QkOZcyVcJrNj-WRh-PMezRVxt6C8BbSJadI1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یووه لحظات آخر مساویو زدددد</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105765" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105764">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105764" target="_blank">📅 00:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105763">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=MSaYAnQd4MMZM1GppG_Y8kBRBi3WQQ3OV6vH1Xal_O1t7SwiluPBhJ4Znx-7Q6UrfTE29r9_9CGIubr7x2x4KVJtq_yVqJYi6P3NyWJErPlI4XP7KXF-hmy-xd-nRI4QJ3GOF4jkEQHDKUO69dT6m_a7YRLAvhlkfb1vMFmET9lllmpxtRRMdAV-eYOAqECQVIQyMfPk429PY8k3JsW0-evhPQjKHBr0I0Ujb_Lq6rio5_68Lwf-5qb11k-XO7LIWE3v5qjAu8nY2kVBBo8cLaDzAtVc78aN3ASBQpWBDCPY3MMZ6HobFqnTZshEHEfBBWUMxKtP7vj3lIw3s3GylA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a702f2c4b3.mp4?token=MSaYAnQd4MMZM1GppG_Y8kBRBi3WQQ3OV6vH1Xal_O1t7SwiluPBhJ4Znx-7Q6UrfTE29r9_9CGIubr7x2x4KVJtq_yVqJYi6P3NyWJErPlI4XP7KXF-hmy-xd-nRI4QJ3GOF4jkEQHDKUO69dT6m_a7YRLAvhlkfb1vMFmET9lllmpxtRRMdAV-eYOAqECQVIQyMfPk429PY8k3JsW0-evhPQjKHBr0I0Ujb_Lq6rio5_68Lwf-5qb11k-XO7LIWE3v5qjAu8nY2kVBBo8cLaDzAtVc78aN3ASBQpWBDCPY3MMZ6HobFqnTZshEHEfBBWUMxKtP7vj3lIw3s3GylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول میلان به یوونتوس توسط سیسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105763" target="_blank">📅 23:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105762">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105762" target="_blank">📅 23:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105761">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=uEQ1UDYvyW1ccS5RysolhJrF2IwUd92w81KPtL-X_shVHibgza_iaXK7S2nzEmtLpmox_t6E7berzkmHNheObqG6wPywc57e9k6Y8N7kdK1XR6atRiwHhmN4SnNaWHPfbcvoktAd2kqj8RLZr9sRi4OAlWgqaOVnk2vH6r-tEvyLMnuwoCTwKCa5XnerVFLydqrgEeCqqTndMUVM_1GxMnvVm0obJ_q6bk85Tnq4etYjoZAXNTjy_ud_QnJCBXda0loYCWOz2MHGymFHAuqSHnw3Y6QFyhZVNpysyksHBR5l5PCjIQOkrhSPUtbOe2kxEE5Dt0xGgbvbHkGlfrFmQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02ce7af3d1.mp4?token=uEQ1UDYvyW1ccS5RysolhJrF2IwUd92w81KPtL-X_shVHibgza_iaXK7S2nzEmtLpmox_t6E7berzkmHNheObqG6wPywc57e9k6Y8N7kdK1XR6atRiwHhmN4SnNaWHPfbcvoktAd2kqj8RLZr9sRi4OAlWgqaOVnk2vH6r-tEvyLMnuwoCTwKCa5XnerVFLydqrgEeCqqTndMUVM_1GxMnvVm0obJ_q6bk85Tnq4etYjoZAXNTjy_ud_QnJCBXda0loYCWOz2MHGymFHAuqSHnw3Y6QFyhZVNpysyksHBR5l5PCjIQOkrhSPUtbOe2kxEE5Dt0xGgbvbHkGlfrFmQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
واکنش عارف حاجی‌عیدی به جنجال در بازی با استقلال: والا یه ۱۰ نفر بهم فوش ناموسی دادن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105761" target="_blank">📅 23:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105760">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=nwioSKSdolqezthpb55UEr7iVkUVQH7C2h6wxBnMxazYG_06nPFtRrrfLLQhKzJalci1bSOL-iHBGNUUjLUNxTlDUgVWp1DxGqHPBGy1B9h0BArIGx6f2Q2xSVyDEIWkkNCFqqQU0pGB80SmPq0YaOPTWz_1A1c-OqZHIbHpUk5XIf9IH879_gcQsDPqyM5QFS7YATbIdsDltGcBDjUXApmqVWe3FMxv3KdxsQhxaR4bErc1w2Bf0ez-MChRFA6bjS2sHcfJ5isGAW28xiP5A9VLST2f-6KcXcM_NLyDG9zHhjEQPbYfrTDxQdI6LqyXN3jZft7XlSqRsu4ys-XttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1098753ac8.mp4?token=nwioSKSdolqezthpb55UEr7iVkUVQH7C2h6wxBnMxazYG_06nPFtRrrfLLQhKzJalci1bSOL-iHBGNUUjLUNxTlDUgVWp1DxGqHPBGy1B9h0BArIGx6f2Q2xSVyDEIWkkNCFqqQU0pGB80SmPq0YaOPTWz_1A1c-OqZHIbHpUk5XIf9IH879_gcQsDPqyM5QFS7YATbIdsDltGcBDjUXApmqVWe3FMxv3KdxsQhxaR4bErc1w2Bf0ez-MChRFA6bjS2sHcfJ5isGAW28xiP5A9VLST2f-6KcXcM_NLyDG9zHhjEQPbYfrTDxQdI6LqyXN3jZft7XlSqRsu4ys-XttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش پیروز قربانی به پخش آهنگ "نصرالله معین" در نشست خبری بعد از بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105760" target="_blank">📅 23:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105759">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
🚨
🇮🇷
🇮🇷
محمد خلیفه: تفاهم‌نامه بین استقلال و آلومینیوم خیلی صددرصد نیست چون ممکن است استقلال مرا نخواهد یا یکسری اتفاقات بیفتد. حتی اگر قرار شد بیرانوند به استقلال بیاید، با او رقابت می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/105759" target="_blank">📅 22:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105758">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=KhUMfLY8bKZHZ1n-ZD8IuxWKGDos0ZPg5GloZZK0SwTuqkj0mhdS7SkNig2gQCz7ONvo2yHWaPGNLGTMxYORYf9mZ99nAEwtWCr9lqjb8g2nLIxl8Y_qtjA3Tg-hbYgX-xLCpsbws2QMPKdjIePO_C5qsfv-ySyz4W50V9sXMGZPNiQJEfejrV3YN3xAFc8plj3P-qPrSc7NDT28QYsGhd18j5gKTx6A3GFfnrEduMbU2cTQ5dAi-bMuSPL1wcUhp3n2HpJ87GPgr8ltZzlGEpHnlc2j6UOBUMVQ6MoN52H0Te3QVAfX97oHqSjCMOHakEw5tDhgw09BRQJoYUa7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b9ee8002.mp4?token=KhUMfLY8bKZHZ1n-ZD8IuxWKGDos0ZPg5GloZZK0SwTuqkj0mhdS7SkNig2gQCz7ONvo2yHWaPGNLGTMxYORYf9mZ99nAEwtWCr9lqjb8g2nLIxl8Y_qtjA3Tg-hbYgX-xLCpsbws2QMPKdjIePO_C5qsfv-ySyz4W50V9sXMGZPNiQJEfejrV3YN3xAFc8plj3P-qPrSc7NDT28QYsGhd18j5gKTx6A3GFfnrEduMbU2cTQ5dAi-bMuSPL1wcUhp3n2HpJ87GPgr8ltZzlGEpHnlc2j6UOBUMVQ6MoN52H0Te3QVAfX97oHqSjCMOHakEw5tDhgw09BRQJoYUa7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
پیروز قربانی: من به توافقات قبلی کاری ندارم، خلیفه و گودرزی رو نیم فصل به استقلال نمی‌دم
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/105758" target="_blank">📅 21:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105757">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXvxYO64qKVhYbW-8TaXhMjsVtrxWWQZSqsHgOfwjZtgQqCkpwtqTFV8_AdRKoPx9hzfsgmeRYy7pAjVOs6HmEj5Tjsf-fGSQFkiW5kwGggG6_BOXFAzISdsGiRlXYEYf_nUtkHLu5kY8EKK-yz7nXm2lOOOSftZfRKUsUFApqlAkXK9sZSB0UJtGRWUy-j6j-NzwH3wZUdvd0EtkRJ_n8ydqlRp_U4iYkGRgKjDAMquNMuhYL2LQlyCR5lM2PN002peuJ3E3cU-VlODa7ycu7OvAh1G0mH9lcTfJKifTiBB2UAkYTPP6WyqoOKptNV-9N56j-Q6jnwfQKH5ITXJSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فکت
؛ آرسنال در ده بازی متوالی لیگ‌برتر مقابل چلسی شکست‌ناپذیر بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105757" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105756">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
🚨
💙
بیزاتی مربی استقلال: ما هم از نتیجه خوشحال نیستیم. قطعا مشکل گلزنی را حل می‌کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105756" target="_blank">📅 21:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105754">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=L8GlpZ2kW-duBpQsdTprfVM3FFHs9buGOvP0gpC_MAbLAoFFjdya8rlNWoT2SAUlpm9W2myDnoKsj-AQKnUx7AVA7FdaMzY9gB4UK62QFAEpmZfruBrePdY3wdxQ47sPVDwDz4otXOPNi06xFPUm6r-8z55wkgV0zD8Wyu0r4fKZd7Tig61SA45u-MHNu_XmhGkbokyEOYEP3npFMrexUEG-Ss-LHC-_EDVyQOGjEd8-gQAJdErlK_o1ZiHndSQXsWi0CdsUn8VYLJ8mcDPsbgwCrxSqPdxmfMkrcNnM7WCxJJAUOphZ3TIECTzR8ZMBLd2h57sIQiIeJ6F6AIE10g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d4a38935.mp4?token=L8GlpZ2kW-duBpQsdTprfVM3FFHs9buGOvP0gpC_MAbLAoFFjdya8rlNWoT2SAUlpm9W2myDnoKsj-AQKnUx7AVA7FdaMzY9gB4UK62QFAEpmZfruBrePdY3wdxQ47sPVDwDz4otXOPNi06xFPUm6r-8z55wkgV0zD8Wyu0r4fKZd7Tig61SA45u-MHNu_XmhGkbokyEOYEP3npFMrexUEG-Ss-LHC-_EDVyQOGjEd8-gQAJdErlK_o1ZiHndSQXsWi0CdsUn8VYLJ8mcDPsbgwCrxSqPdxmfMkrcNnM7WCxJJAUOphZ3TIECTzR8ZMBLd2h57sIQiIeJ6F6AIE10g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
⭕️
نرخ سوم بنزین به مبلغ 10 هزار تومان تغییر کرد؛ سهمیه اول و دوم بدون تغییر
سخنگوی دولت جمهوری اسلامی: نرخ کارت جایگاه سوخت از بامداد ۱۷ شهریور به ۱۰ هزار تومان افزایش خواهد یافت.
در جلسات کارشناسی اعداد متفاوتی گفته می‌شد اما چون رئیس‌جمهور به مردم قول داده بود همان ۱۰ هزار تومان تعیین شد.
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومان همچنان بدون تغییر ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/105754" target="_blank">📅 21:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105753">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDB7L1An7lCNMD4kyPhtvF6UpUhArhE7HxO4rlc980HSs54hS7z9wWlCwLTBiclg5_fgLjnF25FITKCjq5otQmMUUNIKRVMyD3IPat5RObl3a5rEms8CekjqrpURYkpoHGGktRVIWGN4wHwZ0A4NM-b3RS93QNCXvIaeK4RrUr1Uc-UCbHzbpEuDnXpFth3yfYS6CzzvsR-HciUcl_Y1YmeojC1oCOGkia-4BwMo5iFDaEpYwTxcKH-rShAweS9-ovH_QBkoC9yqmoPNm_xr4i71tUlRr4mbg4NyCldHu5ldfXmGp2HwthSw-7l0E06w-uTdYiqMU_K2vT5S4RrOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/105753" target="_blank">📅 20:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105752">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW08QMxxV-xjOaFcJIHvy7WN6kBE-9L1hscQ-IBdPoeFQcJK0wmp1rBfs2iqXUp2ZwFUGbQBcGLzp6UcQV7_5pLFzWUwD8-kpNyALwiPlH-_SEI6Tzhj5lLpIsR1mwlOzuBfIG8h-XJReOEz-xVmX3rRZPOAKRCit1cYjsVZkYdgF9UivZisLef8dTx9B4XyhrMmuIjF80ef6IZHik1TDwQrB8819IactIGhw85JGp-S48UcLx9nEPMyAUTDJtjFDcG6FriXt2LkwS4Sx2rkv_qSyqsDabpjOwpdwjE6THkwqCHIY4N7b_j_HiiNcVQs2cODwZZctMnZBKYZwxbkLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم‌لیگ‌برتر فوتبال؛ به یاد دوران مساوی‌های متوالی با فرهاد مجیدی؛ استقلال و سهراب در آستانه به صدا در آمدن زنگ خطر قرار گرفتند!
🇮🇷
استقلال
😏
-
😏
آلومینیوم
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105752" target="_blank">📅 20:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105751">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105751" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105750">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مرحوم ماشاریپوف برای استقلال به زمین اومد</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105750" target="_blank">📅 20:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105749">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=BQy72FchukHLc5jgFZG4yciH853SNFLC7VjojdYNX0M6a__mlYiY59DM9lHwlyp9hqaFSl7xj6mYK26tXOda5Set6XLkU1NqowbvvUyqct_h3yBLkamGgBqTg-KyElAIPAPlSRBiYxIDdp91i7SJp-qWRSyB6eAU1TyAw_6avvzDFyskbrWAaepkom_7KJg3cw-OvWAnMWbluiSTbnB1G4MYNznvcMURwNFgoV0PiknyznFkybEYGKXLYyR0odYv7mSlrqKGB2o6mrDpJZSYinXN5WYqdf1xyK5ujzWTJc-q_06zpufpoQEDYOQoy6yMaQfwMrmnC7k8Nawt-Ubm8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5e1fcdc1.mp4?token=BQy72FchukHLc5jgFZG4yciH853SNFLC7VjojdYNX0M6a__mlYiY59DM9lHwlyp9hqaFSl7xj6mYK26tXOda5Set6XLkU1NqowbvvUyqct_h3yBLkamGgBqTg-KyElAIPAPlSRBiYxIDdp91i7SJp-qWRSyB6eAU1TyAw_6avvzDFyskbrWAaepkom_7KJg3cw-OvWAnMWbluiSTbnB1G4MYNznvcMURwNFgoV0PiknyznFkybEYGKXLYyR0odYv7mSlrqKGB2o6mrDpJZSYinXN5WYqdf1xyK5ujzWTJc-q_06zpufpoQEDYOQoy6yMaQfwMrmnC7k8Nawt-Ubm8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
😆
گزارشگر اراک: محمد خلیفه ما رو یاد جوانی‌های مانوئل نویر میندازه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105749" target="_blank">📅 20:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105748">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d287258445.mp4?token=DaW7fHK7JNXC3Cnlcl3orIJA6kks3u67KSQdtR-xGdVf55ZJiaMxtlaucXULBKsHnKi47_Va5j3kPjgep2K1sgObjPWbjKTUJudu17JMM1baaLmhU4YgdMLbjAhMJEdCXl_ddAW_9DvrHD2dB7kRQ7S2Bba2pjy4LSutQL5v1nOfQLWn7vXjybvvxssP687N64g9v9MyBpcLk5T32sL2ffV9EDEDIvTN7jzejys4m4qEn8HBHuVtSpJToIkFz4fKMMxGCzoZGsiWulHN1TEwtvAFXDa7rdBvKevXP9N5LJRx0Hyt-cxCBHH7fdgUgyiYPOE3Z-00xGGK1IQcvyE0ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d287258445.mp4?token=DaW7fHK7JNXC3Cnlcl3orIJA6kks3u67KSQdtR-xGdVf55ZJiaMxtlaucXULBKsHnKi47_Va5j3kPjgep2K1sgObjPWbjKTUJudu17JMM1baaLmhU4YgdMLbjAhMJEdCXl_ddAW_9DvrHD2dB7kRQ7S2Bba2pjy4LSutQL5v1nOfQLWn7vXjybvvxssP687N64g9v9MyBpcLk5T32sL2ffV9EDEDIvTN7jzejys4m4qEn8HBHuVtSpJToIkFz4fKMMxGCzoZGsiWulHN1TEwtvAFXDa7rdBvKevXP9N5LJRx0Hyt-cxCBHH7fdgUgyiYPOE3Z-00xGGK1IQcvyE0ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
استقلال از کوووووون آورد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105748" target="_blank">📅 20:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105747">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استقلال داشت سوپرگل میخورد
😐
😐
😐</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105747" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105746">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105746" target="_blank">📅 20:23 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=nNmWFAST0SyMgmLqbY2X4lwXo2sY4xUIuY5d_LHYyIswHeSOnovmk0EiJZy8fWQUDmb8qO5tp2xikLSDOcDe6GuBWN8GAyZV0h1RIWz8-jEtfRojFAi-4RXhaLNYQj5eUD39Joxd3KmhAlJWYv4fa-cj2ECp_SmnamimYL0cK1WBEi62_43ibdFQsrUtOgCwXL2eSTOJ085J_Uo9aLNC0NAxx-eeBLw83UVX2SqsgqixAXxEYQ-z6103mGZZP8mxUkQbn-NCFtn672EpDCtFBWX-WQb-LEhlkHEIYhDmfOyAvl0spcUJNLR0GxSmMAKVP5AO-gs7aiAxqA7YN-5Pbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0209e41e.mp4?token=nNmWFAST0SyMgmLqbY2X4lwXo2sY4xUIuY5d_LHYyIswHeSOnovmk0EiJZy8fWQUDmb8qO5tp2xikLSDOcDe6GuBWN8GAyZV0h1RIWz8-jEtfRojFAi-4RXhaLNYQj5eUD39Joxd3KmhAlJWYv4fa-cj2ECp_SmnamimYL0cK1WBEi62_43ibdFQsrUtOgCwXL2eSTOJ085J_Uo9aLNC0NAxx-eeBLw83UVX2SqsgqixAXxEYQ-z6103mGZZP8mxUkQbn-NCFtn672EpDCtFBWX-WQb-LEhlkHEIYhDmfOyAvl0spcUJNLR0GxSmMAKVP5AO-gs7aiAxqA7YN-5Pbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌اول سپاهان به استقلال خوزستان توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/105745" target="_blank">📅 20:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=Uo9f0eovBRcRlFALyC3DS4UvzOwpVE7YxWmtX-sfyeVxPJfOiNfLLcuP0moK0c6FQF2biO07mijoTKNI2BwIF_-gu9STXFAp1TZDcQllegyk6V_DHP-Rnf5kLLROG_6K1xBvygFk3QK7l6JqVm1cOWcgNmer7M8kqK2aA-qyv9zU_S6pKJFkiChmjK-T4KPdcfczCuwRk-vXjIx4DpM4f_kTzqhp3q-m9OBvH2jJ9nMPKoTP2GtKiMhKTmW3_HRVRXarX87-zkGE9HBaP2G6zfCWv_dXdA2QZfUES9Nv4zza5gTAcf_N5pG54yMociZGm0tm7Ctomu32wxXw64Cz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cb815a8901.mp4?token=Uo9f0eovBRcRlFALyC3DS4UvzOwpVE7YxWmtX-sfyeVxPJfOiNfLLcuP0moK0c6FQF2biO07mijoTKNI2BwIF_-gu9STXFAp1TZDcQllegyk6V_DHP-Rnf5kLLROG_6K1xBvygFk3QK7l6JqVm1cOWcgNmer7M8kqK2aA-qyv9zU_S6pKJFkiChmjK-T4KPdcfczCuwRk-vXjIx4DpM4f_kTzqhp3q-m9OBvH2jJ9nMPKoTP2GtKiMhKTmW3_HRVRXarX87-zkGE9HBaP2G6zfCWv_dXdA2QZfUES9Nv4zza5gTAcf_N5pG54yMociZGm0tm7Ctomu32wxXw64Cz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌دوم آرسنال به چلسی توسط مارتین اودگارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105744" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اودگارد گل دوم آرسنال رو زدددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105743" target="_blank">📅 20:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGrTZ-D1zbuqfuUMLQQ9Lr_AO4UKPPErNrwlh3BYfn6BXRwlw7cORxlXmMoS4BVxUfYnk_buCSfANY1D129p1mZobRxwryfKZX--SC8UGkgnPfZ8ObS84EuA-qBR8IjapqKYFJS7g0ZiQ4zPRO5iG5meSUeSB2jsG10lnO-1OhkbVceErKD-UoeK6wan979nl2Yxfr20Te7g573QU0bkS3xt-k3hsB6tKvyPT4e2So_wOsfbT_pgb7jleKyIoQB-lIuDfv0SW-Q0G3WwqJOSQTzp4q1F3ARAW6kRPCn_Bw5xHj6ku5WOUHLAALy_wSxY8qV2__VAIni72WZSG7hvhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🌟
مربیانی که بیشترین تعداد پیروزی را در بارسلونا کسب کرده‌اند، پس از انجام 80 بازی در لیگ:
🥇
1- فلیک (63)
🥈
2- انریکه (62)
🥉
3- گواردیولا (61)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105742" target="_blank">📅 20:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105741">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szi2xWmkeAzWn_ZYsUKtOiy6PViERjruNFGZK5UtMXswLf0ETx-B5basS3UxxTWGXMYOMgrn1jklp0G7kSJJQ7M9Q3VX-OKR55hxYBtOdQ3Y5ONs4bmMn-2n1zz0fDHl-uELiUKP-3l4ssOzbG9kSKaqv9VumJHJLiCYa2dXcw_gtIsbmqLZaKNu3U8NIuyVDTzB-LGGWS3Lg5C8bGakPFPnYTpOnV2h4UpyGfb9A71AAStOBLlTE_TMzcgywmFfJLyNLTm7O57odAxBck_oymCi6sss7t1SPDnvzcNLAXaorUkqzwALw92welRUNEtApjDg93hMS7I9Tfqq0HgwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
هفته‌چهارم
لالیگا| خفاش‌ها اسیر درخشش فرمین و یامال شدند؛ نمایش فوق‌العاده شاگردان فلیک در مستایا
🇪🇸
والنسیا صفر - بارسلونا پنج
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105741" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105740">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=YQl1D5uNIVW_BkkyJNXCEZ6vAt38DcmsMfMDbvsjnkPDHjUETImwt9Zdx5uYYv241UlrzZFsypYn6VrE2v-387MdBT1JvSJrXmri4f6b9G238JX3IM9VKCONc6UyVvu9jX-xIvWNtVlJlrjBoOcxVoBV48fkvHMKpLlh25RjGRjkX1cpAsHIoPkrX1bcJO6EAFyVSiILNEtjm3aP0D1-8gTpw-sxd5DDnU2UV9cqSf9RWL92JA4O0XqvIGgGO14Ig1ccCsYWyyxCFbIf50poFwF-RMMOZORKgb4yRMSLjbutnFdSdprYuoUzSIq8HvCxfW6ugregVNcTsb2GXjRs8qQL1Eqo1MfQPmTHP-05ghDi_DOZ2rsa6trxIDXbAYU_oujMvxyqDggSokBV1_MO5xpSXw7-C2CYiv__A9VFbbHhyrpMUF7PMr1WwQ9MkLPjKz72xjBmWTcbJ1N_yLnVlVKyWCHYvjDU0iDbBlzBh2-v7Pt3zstw1NHFSX8EMrFnh5uyY8Mkxff4Qlbwtasn08PTSUxxFWaZx4rZW90WtzvoTOig7jrWRLWXluUjJticIW0bWgxdoblqtCsJRrlxvNCwjxYr3Fiv8xWU_yBB31F6ESuuCO3xY1Z3n9996f-7-7fovdiQdn9FkEm7UZz0Gv3GRcYgsvgjGnM1UotaZsI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e47c1a3826.mp4?token=YQl1D5uNIVW_BkkyJNXCEZ6vAt38DcmsMfMDbvsjnkPDHjUETImwt9Zdx5uYYv241UlrzZFsypYn6VrE2v-387MdBT1JvSJrXmri4f6b9G238JX3IM9VKCONc6UyVvu9jX-xIvWNtVlJlrjBoOcxVoBV48fkvHMKpLlh25RjGRjkX1cpAsHIoPkrX1bcJO6EAFyVSiILNEtjm3aP0D1-8gTpw-sxd5DDnU2UV9cqSf9RWL92JA4O0XqvIGgGO14Ig1ccCsYWyyxCFbIf50poFwF-RMMOZORKgb4yRMSLjbutnFdSdprYuoUzSIq8HvCxfW6ugregVNcTsb2GXjRs8qQL1Eqo1MfQPmTHP-05ghDi_DOZ2rsa6trxIDXbAYU_oujMvxyqDggSokBV1_MO5xpSXw7-C2CYiv__A9VFbbHhyrpMUF7PMr1WwQ9MkLPjKz72xjBmWTcbJ1N_yLnVlVKyWCHYvjDU0iDbBlzBh2-v7Pt3zstw1NHFSX8EMrFnh5uyY8Mkxff4Qlbwtasn08PTSUxxFWaZx4rZW90WtzvoTOig7jrWRLWXluUjJticIW0bWgxdoblqtCsJRrlxvNCwjxYr3Fiv8xWU_yBB31F6ESuuCO3xY1Z3n9996f-7-7fovdiQdn9FkEm7UZz0Gv3GRcYgsvgjGnM1UotaZsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌پنجم بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105740" target="_blank">📅 19:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105739">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-OCgMs8N53VLhrqIGi1r9u_sJ0ZGfAABeTRZ-mDfZ196TQ3ioqtH99Yx1uFniPK3a7b6wKFDgLC5TjE2PM1_dL2apSkUbdDXn31kKN8pkXObzd2F-eiyEhz1w5R0sCaf1Q4eF1cD8QGtytv6rooip0JBlCi6zJvU_voA6PKol50r_rT0s1nRqeXq1shvGZkIB1SawLkwLPVgIh0xY7Tx5wNkJEkO6r5ptggpT55g6orFOitGW2IFIKi_ceOD4rJXX2qelOQu0b2GjUiykqzEerqVX0mNhCG4YXaoVeBMw48naOQqp8c2gO4HN--cVrGN_fwbG1JoH31QV7StVkbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚽️
لامین یامال به صدمین گل یا پاس گل خود با پیراهن باشگاه بارسلونا رسید.
فقط در 19 سالگی!
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/105739" target="_blank">📅 19:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105738">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">لامین‌یامال زدددد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105738" target="_blank">📅 19:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105737">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بارساااا ۵۵۵۵۵</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105737" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105736">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105736" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105735">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=EnJGMxIyZZsaqGrMnXBfsmqiquiZU-GkhKzCZuexGOQARX_C5LxO8__eTEkrkxpGe6dRMlR21QADFw26_tXid2t6rZpLxWwHLySyQPZbd8norxemZH_YPWQ-FXyrk3s7Gn2r60_GiHR7yhYZ1tgrN25u09scfjlR128RmuL2ea-pNBz4WAS2jlCnxNsWTjA7YA8mSpW7JxCN6vC2F9ClOODUOsKMyszM-iE6Z7s0z-jaBIsWO6TUDYEHL9y67OUYs81vyGfeagbOfQnrJSbfhhRLsy9BSElfsSeMmRGPA7R_2pJ5HkIkEy7mXz6mu8L1f9PtGd4lVe-MEef8vZ5jh4TGvr48xwM4rV_leINw_XCNUZBDzOfByJsq1lLmKEHQYRx6v1CSGngQoiTTDGfP_NGKm3jhf6jMxabNDFO9_qjdRIwuJlnaeM_nnuz7v2DFMlLBUSOq30YcJBGOlQApyGPwKiOZpHyktmqiJG8or8wdbVHtaLSSpG25mwxrMhDt3w-YimIyo4yLaAKF6OVnGHbdtMZtGujadnFhI2F4D182FjBQoDaiHBXcLU_1ETooJdlTP1YPVj9LSyOQmZnwlj7FBom1n8TMcodeY2VmGxTe2o87mqdNadYlcI_2SjoNLKtVHeF3zy3IYdLIWHP_yEAKH74iyMUfGh-hQTnGBmo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db8af8559a.mp4?token=EnJGMxIyZZsaqGrMnXBfsmqiquiZU-GkhKzCZuexGOQARX_C5LxO8__eTEkrkxpGe6dRMlR21QADFw26_tXid2t6rZpLxWwHLySyQPZbd8norxemZH_YPWQ-FXyrk3s7Gn2r60_GiHR7yhYZ1tgrN25u09scfjlR128RmuL2ea-pNBz4WAS2jlCnxNsWTjA7YA8mSpW7JxCN6vC2F9ClOODUOsKMyszM-iE6Z7s0z-jaBIsWO6TUDYEHL9y67OUYs81vyGfeagbOfQnrJSbfhhRLsy9BSElfsSeMmRGPA7R_2pJ5HkIkEy7mXz6mu8L1f9PtGd4lVe-MEef8vZ5jh4TGvr48xwM4rV_leINw_XCNUZBDzOfByJsq1lLmKEHQYRx6v1CSGngQoiTTDGfP_NGKm3jhf6jMxabNDFO9_qjdRIwuJlnaeM_nnuz7v2DFMlLBUSOq30YcJBGOlQApyGPwKiOZpHyktmqiJG8or8wdbVHtaLSSpG25mwxrMhDt3w-YimIyo4yLaAKF6OVnGHbdtMZtGujadnFhI2F4D182FjBQoDaiHBXcLU_1ETooJdlTP1YPVj9LSyOQmZnwlj7FBom1n8TMcodeY2VmGxTe2o87mqdNadYlcI_2SjoNLKtVHeF3zy3IYdLIWHP_yEAKH74iyMUfGh-hQTnGBmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
گل‌چهارم بارسلونا توسط پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105735" target="_blank">📅 19:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105734">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=Jdv1SivxkWh266nGw42JeMu2g4oqh0HwiSt1eLMDKEymKxR8h6EghrM6LcobsNj5pZcQq3vqfEF9ffYEG-q5fwtKFSUZct7NBFJ6Tr7i3ufm9xIN-3QHZFnzdTIF8Tk3pCAH-w7F1_IXYFo89Vt0qWc3LZNdMBhMq_4v2-fRB7elfqE87Y79kW24bdDKxdzmqiAKwgxX40MP88wCGY5KpxnjKcmOAis7GwHHElQsXGplhvy1-EV3HJyknhA1Bm_KeQ5Ivzkopa3gXnneiPqOr10DW56ixejx0TR0D0oyVmdCP8D1qDwA_lznqeKuICqkAxgiPLx3I8pgViAZqPBxJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50ec1141f.mp4?token=Jdv1SivxkWh266nGw42JeMu2g4oqh0HwiSt1eLMDKEymKxR8h6EghrM6LcobsNj5pZcQq3vqfEF9ffYEG-q5fwtKFSUZct7NBFJ6Tr7i3ufm9xIN-3QHZFnzdTIF8Tk3pCAH-w7F1_IXYFo89Vt0qWc3LZNdMBhMq_4v2-fRB7elfqE87Y79kW24bdDKxdzmqiAKwgxX40MP88wCGY5KpxnjKcmOAis7GwHHElQsXGplhvy1-EV3HJyknhA1Bm_KeQ5Ivzkopa3gXnneiPqOr10DW56ixejx0TR0D0oyVmdCP8D1qDwA_lznqeKuICqkAxgiPLx3I8pgViAZqPBxJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا حضرت محمد خلیفه
😐
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105734" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105733">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یا حضرت عباس پشمامممم ریختتتتت
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105733" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105732">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">محمد خلیفه چه توپی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105732" target="_blank">📅 19:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105731">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پشمامممممممم
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105731" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105730">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XZOrXlSbzdIBw38w6YY0iR9hYtygso8zrXOeCiA-h_yCJRDpNpJ-I7uRRC682fcfBr5wRR-3s1BwxY6DjisnYWqtRt9r3Qa41a6bDrqpCGbB0iskC3Qq8wkDO_eAkJHv85uItoXXyU1DvtTIc2hkeJ0Se1hPK6KZXJVPpY9Y-yzk_GX8FYXS2SnYk2xDo5IbOPgLDja6xwAxv35G7zysaiZBQRQ6S755etDZCRAfUyYr--e0X0R1SvjwdHIV9a8y4RHdIkJeczKw-n1YhVWn8_M2WP2Nz0ucoX7-7FZsCgCDJ38bmsjSv8ayFONEDQaIyRelH2thWX6Z49F7ATqXbLE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89f570dcbd.mp4?token=U9xmNVFzb3gslgwufpzbjP131UVzQhoTWeCsCWkW2xsjR2gvnVXs-BQ6YQSYox8yI5vcMyfBOXVSCeluvxRcaNhsyDwEAVCuijJA8Vv8Vo-stDvW0lvgdXgSTtoOyR2TA_JI7ZaKqrPsJDvXEcijQCjr8USZJQLDjGaGDrTCswVPyyE-6FUwpxjTloxBQf1IF4_e8_9rRDM1s6V9tw-wXm--sLzrWQ7kv1ObgQXlzd2GfBiWi5wwBwlac9Ey8F1-wjbpq7v84dpxfHe29pSRMwkYdmUztSBP1aLZxHbx9kBvYA89KWscWvShNil8iwyAPu5SxmcX2kjc9-32YfB8XZOrXlSbzdIBw38w6YY0iR9hYtygso8zrXOeCiA-h_yCJRDpNpJ-I7uRRC682fcfBr5wRR-3s1BwxY6DjisnYWqtRt9r3Qa41a6bDrqpCGbB0iskC3Qq8wkDO_eAkJHv85uItoXXyU1DvtTIc2hkeJ0Se1hPK6KZXJVPpY9Y-yzk_GX8FYXS2SnYk2xDo5IbOPgLDja6xwAxv35G7zysaiZBQRQ6S755etDZCRAfUyYr--e0X0R1SvjwdHIV9a8y4RHdIkJeczKw-n1YhVWn8_M2WP2Nz0ucoX7-7FZsCgCDJ38bmsjSv8ayFONEDQaIyRelH2thWX6Z49F7ATqXbLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی آرسنال به چلسی توسط هاورتز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105730" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105729">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گل چهارم بارسلونا توسط پدری</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105729" target="_blank">📅 19:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105728">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هاورتز زددددد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105728" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105727">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آرسنال مساویووووو زدددددد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105727" target="_blank">📅 19:26 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105726">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/581a696d28.mp4?token=RGmsIp0tSuBvO7k_Z3sLRUWqCM9Xk5jXwm5CQPgK7K6-h5pl7hpxL9YK3pRXRMxK1-nQ_vLD34fOweFeXLQQKNUe4VzJYetgX343-n0fEzG7f67J-7I8QNDJj_YQqrci8VcW9oK6b99wMqwNXkCT-WPb0RtTrxQwXgWXN4wcZGL35-3l3isFhMjc2NoFg1L18spkWU_2chCmrI-WQlHe12DO38rTbefmFw6Z-ECu40pUg1cKv7UkR-TqmIHfepsplJbtLnTtSq7lLc8EianuG_sakEQ8jqUUTFtQvoVWa1BO1NSK2wZ28X51QZrxvhjgQXAGVKTO9m4GuhXdsTdAJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/581a696d28.mp4?token=RGmsIp0tSuBvO7k_Z3sLRUWqCM9Xk5jXwm5CQPgK7K6-h5pl7hpxL9YK3pRXRMxK1-nQ_vLD34fOweFeXLQQKNUe4VzJYetgX343-n0fEzG7f67J-7I8QNDJj_YQqrci8VcW9oK6b99wMqwNXkCT-WPb0RtTrxQwXgWXN4wcZGL35-3l3isFhMjc2NoFg1L18spkWU_2chCmrI-WQlHe12DO38rTbefmFw6Z-ECu40pUg1cKv7UkR-TqmIHfepsplJbtLnTtSq7lLc8EianuG_sakEQ8jqUUTFtQvoVWa1BO1NSK2wZ28X51QZrxvhjgQXAGVKTO9m4GuhXdsTdAJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول چلسی به آرسنال توسط مورگان راجرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105726" target="_blank">📅 19:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105725">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=jDSEIKOoMpQnw_PgCSud2t_Kc0mRrO-e6pzadukm_MzpD4l_gL-Z-zp1QtuLA-pnT_xaCZXyEFflMW5iH8uQjGdCM_28022fn_rr_I6VvzT2mcJ6EASDMMOWpdKpVmzBNIJrVpqVF6kuvlSorXeOcgs4UjLTCN_XyftqCzMKaaU2nvKeDYneN5fJFRIxN8HJsw239WX_tpbCBrZ5lqTXUA5H--W0tF0CefU_KLAh9bYNQkdrUiRVWf7hkT8WGSJsb4fmmDIwqajRogsqYxhw9-BizgCfTxh8q-bQJtiB8nFvfoN-nCP5FOtByCfrl-Ynh0ShRI2Z7xgJxTm-w9ADpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31943b0e62.mp4?token=jDSEIKOoMpQnw_PgCSud2t_Kc0mRrO-e6pzadukm_MzpD4l_gL-Z-zp1QtuLA-pnT_xaCZXyEFflMW5iH8uQjGdCM_28022fn_rr_I6VvzT2mcJ6EASDMMOWpdKpVmzBNIJrVpqVF6kuvlSorXeOcgs4UjLTCN_XyftqCzMKaaU2nvKeDYneN5fJFRIxN8HJsw239WX_tpbCBrZ5lqTXUA5H--W0tF0CefU_KLAh9bYNQkdrUiRVWf7hkT8WGSJsb4fmmDIwqajRogsqYxhw9-BizgCfTxh8q-bQJtiB8nFvfoN-nCP5FOtByCfrl-Ynh0ShRI2Z7xgJxTm-w9ADpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به والنسیا توسط رافینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105725" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105724">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بارسا هم سومیو زد رافینیا</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105724" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">چلسییییی یکی به آرسنال زدددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105723" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRFOJqBADrPG3rzB8jfNm1XctYjvtj70BLBv6GDtMOs3iPnMRc9knAyx7noBSsVxpZGXDdoM2GrMJOqdzATybbQlzgAoSW3AT_dtPfCKWA8qRbr8a93P_txpXoVVtFIiXEh496cNgyt1gzM7hnWI_VQElntO2i7GCRo6ssC6EBDp0CmiH9_rSFOSFIQxnYQa4WHs7DsITyleeUlOU2D516RHor70-a63AqKkSAsgP8nq7wPpCZP00exRtSE4Sk8-T6U1LLsFPK7vlXjvjVGXfdwkulYbylAZ9v9toNH4xuISjUV1NMcdLP70X5QDLivRLiRvRkEsc6GeJQypEjjKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رد ناخن حسین کنعانی‌زادگان روی گردن و گلوی عارف‌آقاسی؛ لامصب چه جوری چنگ انداخته
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105722" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn6WojrFXWtjG4Zpxn7RJmcVScm3yHvVsYW64bdLtoMaDwD6p9T_3Rl_TGo54PPXHRhmn4NYSuWg9G9rY-oRuaxOnbCgYp65favh2Zw_70-1uBGqmHvZbbiMpfTn3gix3AgGssTnGypkc5NwLBGj_O6LQjxyEVa-yPQLNaUs0xPFRxSz4FEScPdMhOqcq9BhGWcMcBr7X1fndRaZwn_is0XxuEsToY-3ztFeb_LiisdAUoTMFRooWxeDdXjV2KFP_C3_4Es808rZ1pqsgXj-_IlYvjH5egIfDoHKrGdjttkqY_YCKgjNBu87ND-SEbHeJlA1ZrJjr7wD8EuOnf3pfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اریک‌گارسیا در بازی امروز بارسا بدلیل سر به سر شدن با رودری دچار شکستگی بینی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105721" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwOfDMgdNg4OzFQXEO-qovjXMRlbRO7XmA1l8ae26SB0SCiBqxRtFK5tgFyKmJWMYFNEeHm-BVSnbpDu3HRjDvJpJ-C8eAXOI7dL8959YuQxD1PhDNSwbG4HeaHG7NVIyEsASEM1TbMF9Q4SInd1orNxjlb8dodMfS8Cj6xftGlVKV_Ts5Q1uHAZRchRyhKTtlYM9MI-h2hfjAZiA9yyVoVozJJvhJxfw9y8esP1In4AL10_n7CWTa1L5ZV5jkZK7OnezztaI_4PWe66SghumkoiiFZxPpWtpQ3X-uAFCvM2j26p6DsKeRK2yhqbn2SyQdOQ9wL41vbOcJGi3xm_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل‌اول بارسلونا به والنسیا توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105720" target="_blank">📅 18:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105719">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90fe998947.mp4?token=eqOB531aIV72pxZhJ0iPq0VYgMo9EShBWsHNBU8d0yEBseKssk6IG27gU2M_q8o-WcTB7ZKsIb02Sk_UW_vjiarCIBoO7cKdKtd2sMQ4ib1WQ3TLuX-n1xERn6TuXkxrYZIbdLT9HzONHL5i-0KyOlU4fC6Nlp2IUMWHu8MhpJISEwe4GoQKA6JNK1txF08zYz6u_RgXe2BTqlwfeaVbwtNbkXMVLSNE7BbGNbeZL6ihYdAKb1jK56SIhM1T6Yn9Xrkff6LQFyN-yJshfgGkSlw35GEw77OSliQdyaNH4HMm2kVXnwS22GxU6s3Y1QRDocqPk9X-JpTtp2ifTCNqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90fe998947.mp4?token=eqOB531aIV72pxZhJ0iPq0VYgMo9EShBWsHNBU8d0yEBseKssk6IG27gU2M_q8o-WcTB7ZKsIb02Sk_UW_vjiarCIBoO7cKdKtd2sMQ4ib1WQ3TLuX-n1xERn6TuXkxrYZIbdLT9HzONHL5i-0KyOlU4fC6Nlp2IUMWHu8MhpJISEwe4GoQKA6JNK1txF08zYz6u_RgXe2BTqlwfeaVbwtNbkXMVLSNE7BbGNbeZL6ihYdAKb1jK56SIhM1T6Yn9Xrkff6LQFyN-yJshfgGkSlw35GEw77OSliQdyaNH4HMm2kVXnwS22GxU6s3Y1QRDocqPk9X-JpTtp2ifTCNqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
سوپرگل دیدنی در ثانیه های پایانی؛ گل دوم اورتون به منچستر یونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105719" target="_blank">📅 18:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105718">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e19464327.mp4?token=MEYLemz_nGYEozaxte36SelxWaKOaNJHtnA2AKPOMcZiVGKlooj03uJIgu2dquxPZ93YOW5_GUFhtgbAy6CeLGtCTlXO8Bui2Ghd_NGb3pXVwkTFNj6HjznAWQkbJK7eLX6HzYJTrW2ltFZ9b8vBqDgp5JV4QGFmKL7sYCfoE_gSejHapx3jG810PJyCcUqAvg-xYOrQgash81TfsNTk78gwF12z6DFYRi5nOHPl7vIM8Tp2qGvD1u9zCgvbwzTrdJMKasN9ycEK8U853B4C53QNKx6p9pgb1HIuuOA6XCbCqD4BjTVyoDhruGNlwYEmcUhn4ZMWbBED8vFpNZb1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e19464327.mp4?token=MEYLemz_nGYEozaxte36SelxWaKOaNJHtnA2AKPOMcZiVGKlooj03uJIgu2dquxPZ93YOW5_GUFhtgbAy6CeLGtCTlXO8Bui2Ghd_NGb3pXVwkTFNj6HjznAWQkbJK7eLX6HzYJTrW2ltFZ9b8vBqDgp5JV4QGFmKL7sYCfoE_gSejHapx3jG810PJyCcUqAvg-xYOrQgash81TfsNTk78gwF12z6DFYRi5nOHPl7vIM8Tp2qGvD1u9zCgvbwzTrdJMKasN9ycEK8U853B4C53QNKx6p9pgb1HIuuOA6XCbCqD4BjTVyoDhruGNlwYEmcUhn4ZMWbBED8vFpNZb1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم منچستر یونایتد به اورتون توسط بنجامین ششکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105718" target="_blank">📅 18:28 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105717">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گل دوم هم یونایتد زدددد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105717" target="_blank">📅 18:19 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
