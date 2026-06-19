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
<img src="https://cdn5.telesco.pe/file/XlSyKenPPXmNxR2dMCPJzt-Efpbs88W-pHjrRzoHx7BHOklkPwBAwUzYcfW5OiUHuOa_ELyxHzadS94V3TbB9VQZV761JlUaXZqUSWXqtAR72rCIpBkfLQoFVTr_a_uB3d9wrZYz-VpT2OMrtsvLYnTphAAj0-fPHKJ_QOublKqsL3vvhjKnTp9K08u0ACbPhXVS5CLNkxlh8FT2wenB1JV3cr2K3uV0uqv5SFsaCEchBVMnV2HoB5MDFTOu1B7_XeXWlFAUCFinVwQrSVgM6UJpbq9dslaZPaDCrajWIzNyUejQmg_gyeI9yKroKSEp9lA4CdewoP7iYo0GPCXKXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 673K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 17:23:16</div>
<hr>

<div class="tg-post" id="msg-94452">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c628dc86c.mp4?token=MVVrAbWPYNHULsWXB7QJOkd_kIbB_vLv5F4mW2Pk9kvHVl1APNKAeljfP0hxibTpRsJj-MqeCrzsrm4wyb5UEdCeCrR3IUbqZbRCbBbtOYEoP2e54Bl3DX3zE1zzOsNtyR_uj_ohhvs1VuGHjle0b58H8PAeRpkwSClPWSnCYvokf-iJV96bokhsiprUXl-iGNWNlq9P6zEwGGShIkTJjAnhAA9BdDYZWDZCvSo9qJjm4oXSao7OJn1mWt5q4OiTcunVHvySoTk_zACfdW2DRyLamaCj4MFvuyIp1CXyEnsiMa5TvZPMIK6QGq1uW20NZDDuSYdn2ZIOkfrqUu4SDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c628dc86c.mp4?token=MVVrAbWPYNHULsWXB7QJOkd_kIbB_vLv5F4mW2Pk9kvHVl1APNKAeljfP0hxibTpRsJj-MqeCrzsrm4wyb5UEdCeCrR3IUbqZbRCbBbtOYEoP2e54Bl3DX3zE1zzOsNtyR_uj_ohhvs1VuGHjle0b58H8PAeRpkwSClPWSnCYvokf-iJV96bokhsiprUXl-iGNWNlq9P6zEwGGShIkTJjAnhAA9BdDYZWDZCvSo9qJjm4oXSao7OJn1mWt5q4OiTcunVHvySoTk_zACfdW2DRyLamaCj4MFvuyIp1CXyEnsiMa5TvZPMIK6QGq1uW20NZDDuSYdn2ZIOkfrqUu4SDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
🏆
این ویدیو خود خودشه :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/94452" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94451">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yl_j9jQRjYPf5QnUd3TuaAjtCj5Yv8iP2biB5Rdmk6Cu8hknSCoMtgkQf0JTpZUsM5VaKyd3KkTlLgWUQBK7_O8oXnNPbt79Zt1IlogOUtnnb7Lc2nl8zztdn9wvpMB9rWpOaiAXKN2vo3mGdArcb0lWoHDwLm533PSoKnoO8fHMV6SlhpXgyp6pAH0cPHQyaVotntbQUdzHu0Sv3Df5llb-aZfBngrdVlFgH-T-IA7HsSMChWnKUZTVn7bYCikqsyjeTDbE9TvwXdNX0UiNLa288VjPccA8TrFwtb7to14FiJaaG0v6vGtz74AtokAc3txYqUtlk_L2NT2xwo83dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تعداد کارت های قرمز تو جام جهانی‌ های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/94451" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94450">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQfu8rb0LkPPVK8KxBjPa0-MlAEiPfa5_1wF6i5niX4tD1TUw5FnVixVbD_1Ly6e4WvbIYFDgWu--d5HepgbPiFUcskB3CZTU6B4EJ0MWxDRTw5xgH1QUo81MzG1JqGV6xjNAPoiO2JeOp3etwRrEeKbR-lWFvf4xLqpoRN2JZzYecssmBzsQ1mpjCcaLzGmX3CxYNowP9lg2Kjg9vU7DtNHSbe3IRSgJ0mqWJDoTT9OS-0K8cCDX6CKFdB6KXD8s47Q9NuakNzZ_QCMF2jnAeUN_bduB1OTFXKOdxdRwXNeiq3_1datEZBoXNzVpnR6au6ufE6KIG0xkxdGlTi8uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلافوئنته :
رودری بهترین بازیکن دنیاس، وقتی ازش انتقاد میکنن عصبی میشم، چون اون از تمام هافبک های اروپا بهتره اون حتی اگه 50% آمادگی جسمانی هم داشته باشه بازم جزو بهتریناس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/Futball180TV/94450" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94449">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d969ad7b3.mp4?token=SJDKfFtB42ASULIdyJ4Xy9NvEuFssx42GZZhR-wFe5wFyIdMX5QJ7J3BeXNVdY2gZlTFALCX8CUkYwUl0s1oZYeU8bnNCs3aQCsVNL9_Zcdq9ovbsAzH_c6fQ9RXm4kfAp5Pkc6fgmhspW6ZszVqSv0kcdvq0VSXk6H3uow7YATBkAT-zXEDNcWh-CiTojWMcyQ_VOa_cTsUgdt4Afu-6OW2uxnMQC_uwFghk7nfI9wkhNmFpOIkjvA5TeafL05fhdPYKUVsYsHqD__diozkLUkF1DRYGh7xVX8M_BBqDSe86fzweyDFWf5sD-qtdlE0pO0cJkltpDiDcOgL3I_QAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d969ad7b3.mp4?token=SJDKfFtB42ASULIdyJ4Xy9NvEuFssx42GZZhR-wFe5wFyIdMX5QJ7J3BeXNVdY2gZlTFALCX8CUkYwUl0s1oZYeU8bnNCs3aQCsVNL9_Zcdq9ovbsAzH_c6fQ9RXm4kfAp5Pkc6fgmhspW6ZszVqSv0kcdvq0VSXk6H3uow7YATBkAT-zXEDNcWh-CiTojWMcyQ_VOa_cTsUgdt4Afu-6OW2uxnMQC_uwFghk7nfI9wkhNmFpOIkjvA5TeafL05fhdPYKUVsYsHqD__diozkLUkF1DRYGh7xVX8M_BBqDSe86fzweyDFWf5sD-qtdlE0pO0cJkltpDiDcOgL3I_QAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهمونای جام‌جهانی ابوطالب‌حسینی عالین
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/94449" target="_blank">📅 17:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94448">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Live Tennis</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/Futball180TV/94448" target="_blank">📅 17:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94447">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQOJmUN9uWxQpYrYwE0GMvN-EFY6SjSYW07bysfhcOlL77EsOBlhUPdM8-lz5KbAq0HJ0h8PkXSvTvs6dqtRwE1Dwd-ISu2RbWIWTUuJLHEzNU1-KVFk1jCgnnv3chIzAdbsDfq9h-eg7Jw6oX7KYsPZXTpfostnWUYV5YeP1dTSIb257sTiE-chERJnLGWj31vJaMzJy9ufNXOkZoBxeKixGx5tDS35XRCdbNMdhgAFHa453Q4vtvLrDGI1ca18UME2hIJOgj7LoFEXJQshe1vpX6oN0NcuZ5Vi7nh8_ll02kljHbz1iHkHMv1VQtIVa-Vq67GGPbqYYIrlDMSRPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوست دختر ژائو نوس بعد هجوم هوادارای رونالدو به کامنت هاش، کامنت های پیجشو بست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/94447" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c99fa3193a.mp4?token=SyI-iX3ZzHcSsh6hw4vAFKeKdVeNKBx-xUCcfXmzRmAvsS2Wef-N8qoICB8GEeidPuIs_NdJ1fAULrS9jzx9n000GPdAes_hZ_OmZc1QA4v6q6weNRXwnHYcmpf5s2jbpfygpznlbR1jofeBKUru6umYPPybwz859WvAEC38qn8zCQ9_4DF01cgb9PMn_XH2XFqz3Zu6syBf8iC_N7eZaUFG0vukxbUaGkDVivUu__6gGTLE-Hg7r_f1Yk83AfWEFuIA_Gu9Dsuxe_jGiT6JrW0meoE7rKiNLVXiAtkh_AhOKR4HoPZiAywqjKLVx7hiTiZRbWV8okGWn0nEh8lwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c99fa3193a.mp4?token=SyI-iX3ZzHcSsh6hw4vAFKeKdVeNKBx-xUCcfXmzRmAvsS2Wef-N8qoICB8GEeidPuIs_NdJ1fAULrS9jzx9n000GPdAes_hZ_OmZc1QA4v6q6weNRXwnHYcmpf5s2jbpfygpznlbR1jofeBKUru6umYPPybwz859WvAEC38qn8zCQ9_4DF01cgb9PMn_XH2XFqz3Zu6syBf8iC_N7eZaUFG0vukxbUaGkDVivUu__6gGTLE-Hg7r_f1Yk83AfWEFuIA_Gu9Dsuxe_jGiT6JrW0meoE7rKiNLVXiAtkh_AhOKR4HoPZiAywqjKLVx7hiTiZRbWV8okGWn0nEh8lwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختر فوتبالیش خوبه
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/94446" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94444">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcYh4b7wlSakAY8jTxGYtX05HKbXSlyZ-P7UwMjB9kdG0zo0nzxKfBhejRg8eE7XAbQ8JXNmZA5r1GQ9AR554-XG4FCUkIoAKpvub4cuHfdK5c8-RH_M52qA-6S5BcvDnbDiqWA2_NfAwDy4366v40kMB_VCnliNpbiMThGPlH8nCkKAXvj0AQUeek0FfAFw8bMDmy04l6TscTJM0eEpVwAI3x5kiJVO3oDKp2B5PWZRq1N5nYgJDTcDQop0i8rKCj-s_oT_-L-lGCl_Jx6kcwdZag1czWp2aFBP2yvNEG6pcTeHJ76OeLjqcNy9egqCSbk4fbtZSJmJuT6fpGTPLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
ما جام جهانی را خواهیم برد [پرتغال]، چون بهترین تیم را داریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/94444" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94443">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0dh-bdUHfmkVDoNrsDPx4fIE62GXNbgBl4pV99NJ5DNMFbt1FDKHXjyNTii2_-2w9WHP4wz8yHi_xd89WBmD9oPd3DCxMrXYGjzAxm0RGN4KB55D4gMdE5TznkiEZTanD33AR1Pe89bHZaYDKNsWFR74lSS7qnSqp_P3uAFhd_XkqOMxzNrD9AzPS5r2u09C_217CLGzn3tzM9Lbse3Xn59a-5VKP1s373wzbzaGvwKBm-7TqGnWGp2WPh9UKpDyz-5RWNkhw3tOaMNxIZDUdcLGHSdI-eI8-izYc0j4QCBeANyscFSXUOlFoF_PMZXldijT6p7sDwHE5Pstph5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
اینفوگرافی خدمات فعال‌شده پس از رفع اختلال فنی</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/94443" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94442">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c32ce413.mp4?token=UOMGhcy0SEOMPaKWrdbIauf3A-o5k_HsRwqtOkU9pyCosBujJFtEfjTMEPsLfdlPWAh85scDlbA3hL1LtwtkT6hFmsxOhKSjjwys8JjDmGXEOyatRyOgcb6cMSXZ77Tw0D-y6a9-mV236k9gHrKh6-1qhcmFEyv97n5_5s5GXZOwub1JvPhe3JAS70dHxqln-9m05Fr1bHZ6Y1n_sUhFYslVfTRwCKsAVpo3Z9vpDXl6wEWwabIybcIhM1Zv1HwN-ULWgNOadw-R7EwCJglwRh4y1KYA9xXXZGAkLavyKXdMx_pz0UjjOWe7rGaoKxEVv4C8gNRw2kLjgVhQ30i4Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c32ce413.mp4?token=UOMGhcy0SEOMPaKWrdbIauf3A-o5k_HsRwqtOkU9pyCosBujJFtEfjTMEPsLfdlPWAh85scDlbA3hL1LtwtkT6hFmsxOhKSjjwys8JjDmGXEOyatRyOgcb6cMSXZ77Tw0D-y6a9-mV236k9gHrKh6-1qhcmFEyv97n5_5s5GXZOwub1JvPhe3JAS70dHxqln-9m05Fr1bHZ6Y1n_sUhFYslVfTRwCKsAVpo3Z9vpDXl6wEWwabIybcIhM1Zv1HwN-ULWgNOadw-R7EwCJglwRh4y1KYA9xXXZGAkLavyKXdMx_pz0UjjOWe7rGaoKxEVv4C8gNRw2kLjgVhQ30i4Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خاطره حنیف عمران‌زاده از هتریک ایمون زاید و شکست مقابل پرسپولیس در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/94442" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94441">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e669850176.mp4?token=PTwMJKKoQKnyyb2-ZtyQhZSi8T5chfgESLfQVGuDz3QkTWkdYRs5GJa2MEEAdsSfSk8YkfvdWRkSStw3iuhrIynq0qbLfC-N7XYVylf6kbH2hf9GUNGA_FvzK2cSUS7UkuC9N751AgHQBYTpgE-LdjzLLTSWMWhHqO6rg9_IaXyoWvNynX7_QB1xmoPwRn14cGL9qxWS-OTUbY028qgKRWk1B7SbWTDxGgmr5CSyeHiUR94rA6lj7IMjlwWMpnzOiZSNQGnuJbVapDieuBcUaw5dzVAOQh7H2Lo3CyyqDnLV0Yv9w9a84hSfANnfUPAdwfQrVIxfg-LO-M6xPm9hEbkCzchNyUSSmc4QDhlZhTXwzqNOqNFk86FdyMKAyEWPrmpqDuTgff-ZMDiIKWpB6pBLQ9NjgTV-aK2u8Zq0GbGrzdXEu--BvdEmM3zlLJDomw7KQ5SLsv_KafJm3WzB3_bTR-OKpjsC-rLQ2JBMcXH3d4q7PuFnWddDQrTVXjAyB_pG5VHb_sYF2I1eTnr35kBdpkYbzEaPCqM76JSzWzuCsg_I8BJldJwtUljaKN9jBG1rATnbVEFMKzDnnGaTgoKBZ7w0yiizGBaf-81fYQTf5cstbrlmBpGH_Il4otLMNK1Ci-ZWVQJ9K7nH758Ttw1LZ1Mq2oLVN5m_EnviVqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e669850176.mp4?token=PTwMJKKoQKnyyb2-ZtyQhZSi8T5chfgESLfQVGuDz3QkTWkdYRs5GJa2MEEAdsSfSk8YkfvdWRkSStw3iuhrIynq0qbLfC-N7XYVylf6kbH2hf9GUNGA_FvzK2cSUS7UkuC9N751AgHQBYTpgE-LdjzLLTSWMWhHqO6rg9_IaXyoWvNynX7_QB1xmoPwRn14cGL9qxWS-OTUbY028qgKRWk1B7SbWTDxGgmr5CSyeHiUR94rA6lj7IMjlwWMpnzOiZSNQGnuJbVapDieuBcUaw5dzVAOQh7H2Lo3CyyqDnLV0Yv9w9a84hSfANnfUPAdwfQrVIxfg-LO-M6xPm9hEbkCzchNyUSSmc4QDhlZhTXwzqNOqNFk86FdyMKAyEWPrmpqDuTgff-ZMDiIKWpB6pBLQ9NjgTV-aK2u8Zq0GbGrzdXEu--BvdEmM3zlLJDomw7KQ5SLsv_KafJm3WzB3_bTR-OKpjsC-rLQ2JBMcXH3d4q7PuFnWddDQrTVXjAyB_pG5VHb_sYF2I1eTnr35kBdpkYbzEaPCqM76JSzWzuCsg_I8BJldJwtUljaKN9jBG1rATnbVEFMKzDnnGaTgoKBZ7w0yiizGBaf-81fYQTf5cstbrlmBpGH_Il4otLMNK1Ci-ZWVQJ9K7nH758Ttw1LZ1Mq2oLVN5m_EnviVqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
▶️
پسردکتر حسابی در گفتگو با ابوطالب: منم میتونستم برم دختر بازی ولی ترجیح دادم راه پدرم رو برم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/94441" target="_blank">📅 16:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94440">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c43B5sVFoEFRmvrOgnlF9QtDIcWzTz6q9TPlC_eaF1jS334FAMSSOyupEGFMrWPFxYNn6oOeqFKdSdamKg5azX9OJd7eoS5k-qQm4pNT7HN5ezUoSlTqXFiiSZRttSqo5A8Dfrnw72iWhZskG5oUz7J26Ge4hWEUHOyzvSpLRB9x0Nku162xtoZEXo6qv9t6YSEYFhc3wFAOldf-F8dGd725NX5jsC-dQoxQqSVYJnnZ74mr_Az4GpaQrp0USIaessGRyvXDpdYyH-Z44Uuz2QBBC6TDH6dH0Dutm_aYmjbL-emIBYDcZBUTN-MVhtgggJWnNJ6fs9PfXL8epcNSwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🎙
گاوی درباره انتقال کوکوریا به رئال مادرید:
خب... رئال مادرید اخیراً تغییرات زیادی در دفاع کناری‌هایش داده است! این نتیجه داشتن لامین یامال در بارسلوناست. یامال بهترین است و حالا آن‌ها کوکوریا را برای متوقف کردن لامین جذب کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94440" target="_blank">📅 16:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94439">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f110036c7.mp4?token=cAgpNmfm5A8vv_ku2fEiW5A5fo2bj98AFynts9acf_sk8tjZMgcgs_N2Ipfar8-N7z6CGXdqgwhX9cFID2SvF2ZgHZ5fJwiUzkURKTdERc9alyxfVKzC52REQ1ThYPIhykxDVHllaoVmiENX00I0R18E5ISZxUSoLbygEIaokpYU_pCJmgSEVKUuZ0zis3BI3dgTuJIHN4zbkB7ln15I6IvDWAxHKdV2dj9oXCdvEV6R6HsTCXv-gaIanws-cLdtrcTuLCYoTUK5gm-OIFmWOq861UhXolGhvpUFJM47FnyIFK8_3HzqCBTiET5C3ziYHFzxwmyikJIUZhOR2SLZVjsrKXKhm5FvE4_pmXEJHXZApRqqvErVRAtudSJzSJVCtQzba61u_qD0PumV55LMNEEBCDAx2ruYtxUrD3lgTuF1DLBIvGH-S0Lm2pQEJlJoXzRfw_eDcwMvc8KUjGH0VPWpZR8yUqO6-V78YF1Xn7kgB6H6lQNYUDPOPHkZ-NuS6dKwmXXtaMPEGWYAhFxuXhEgDl67i3fXJiPfMxM834WAezKenAxsY2VYLhJsPt0OAAK6_15kDn1WzieTucBZ0zdIANEJMQ2OSVfhdUG4dVI9Hn__pPZIhLgo7S_MeFRuQVsasU_wNaWK6iWfAtxxPLWV7jSVZOVT1iHEr8iBL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f110036c7.mp4?token=cAgpNmfm5A8vv_ku2fEiW5A5fo2bj98AFynts9acf_sk8tjZMgcgs_N2Ipfar8-N7z6CGXdqgwhX9cFID2SvF2ZgHZ5fJwiUzkURKTdERc9alyxfVKzC52REQ1ThYPIhykxDVHllaoVmiENX00I0R18E5ISZxUSoLbygEIaokpYU_pCJmgSEVKUuZ0zis3BI3dgTuJIHN4zbkB7ln15I6IvDWAxHKdV2dj9oXCdvEV6R6HsTCXv-gaIanws-cLdtrcTuLCYoTUK5gm-OIFmWOq861UhXolGhvpUFJM47FnyIFK8_3HzqCBTiET5C3ziYHFzxwmyikJIUZhOR2SLZVjsrKXKhm5FvE4_pmXEJHXZApRqqvErVRAtudSJzSJVCtQzba61u_qD0PumV55LMNEEBCDAx2ruYtxUrD3lgTuF1DLBIvGH-S0Lm2pQEJlJoXzRfw_eDcwMvc8KUjGH0VPWpZR8yUqO6-V78YF1Xn7kgB6H6lQNYUDPOPHkZ-NuS6dKwmXXtaMPEGWYAhFxuXhEgDl67i3fXJiPfMxM834WAezKenAxsY2VYLhJsPt0OAAK6_15kDn1WzieTucBZ0zdIANEJMQ2OSVfhdUG4dVI9Hn__pPZIhLgo7S_MeFRuQVsasU_wNaWK6iWfAtxxPLWV7jSVZOVT1iHEr8iBL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇨🇦
🤣
این دختر ایرانی وسط بازی دیشب کانادا حوصلش سر رفته اومده رژ لبشو معرفی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/94439" target="_blank">📅 16:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94438">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwjZcQmhOLORFe_4Hngy57Kep_jLKmwiiTnenmtrpiGe9b-uW2m-elMhOdAyA4VAXfFLURI-tv7GSEum8DVcoL2vBxOC0M6DDv7R9qzWm9SboRmgly7sfw1emK1XS_bv_XrBUvLBMYJkudqc5YZN8xD7t9eAP6p2-LIOVP1bJ80THI-F89dWNXLzvVGJL8d9wD6_vRI6YIIzOcQk2ojVieMxF9O1j97RSiFEG8Mv1zQ3yUIQU7OViqZmB3otC-ncfBjvu3JLyngT0Rr4G7YechisltcKSbrHV0XXIFnhDUflvLGr0J-jp9urmAsnHq9lEmPbRY3B4Xqe-Vg0P7qBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
دی مارتزیو:
رئال مادرید تصمیم به فروش نیکو پاز گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94438" target="_blank">📅 16:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94437">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8535ae130a.mp4?token=PrMpyWUn9_auJ-up2ioXF3Xjdsi6uQHx5tgAHMXhzPW4_OETj3EAb9IQ0iTunEhXaWl9TfP8masrDjSn4WEU3UcqsoZ_Bh6JVTvyOhfVb-Pix0Ssw6vrOgRA7kzJ7YT9PeWxBU7dHmah4AZyZkCUxQapdyDT2eZLHvHXfNIvGER0FSKYaTt_2o0Y5Ly3uuQ5SnCXnyLQRVQ6yRFqFALcu6_HsWfZ5zqzujL-xDyr1P0b7eNeIJ_HFuiUSsG0jQWMHscXb7KR6qkHST_BHHEtlTlWlxiFOIfVbd15HWLaraBj4Nvtzo6C7TK9to_fw3QNbwuFORcRe4hjTMcjgAEYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8535ae130a.mp4?token=PrMpyWUn9_auJ-up2ioXF3Xjdsi6uQHx5tgAHMXhzPW4_OETj3EAb9IQ0iTunEhXaWl9TfP8masrDjSn4WEU3UcqsoZ_Bh6JVTvyOhfVb-Pix0Ssw6vrOgRA7kzJ7YT9PeWxBU7dHmah4AZyZkCUxQapdyDT2eZLHvHXfNIvGER0FSKYaTt_2o0Y5Ly3uuQ5SnCXnyLQRVQ6yRFqFALcu6_HsWfZ5zqzujL-xDyr1P0b7eNeIJ_HFuiUSsG0jQWMHscXb7KR6qkHST_BHHEtlTlWlxiFOIfVbd15HWLaraBj4Nvtzo6C7TK9to_fw3QNbwuFORcRe4hjTMcjgAEYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
سینه‌رو محکمممممم تر بززززن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94437" target="_blank">📅 16:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94436">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac99529467.mp4?token=FagTE00aFecrtgH4M5AX0m497_F9fTBy4SdnYIaeuZNcZr-vriNmAHVXKQzcmirF83-_1o_KJyqHEyxMdSRQx_k4s06xNOMyiUmJ9Xvwi9tv_5-mzPMGTMc_QgLFyc6lyCNRxzdnNT6hsA9Q9XeOAXnsNApFWAlU9JQR60J4sXPLDLRFzyyQXoUaqV-z2rfmsMwIXxYjq9k2tnGjSHoDhc0KF_jdfEoEBzNNXPmX0ETUi5-a9HvKK8GXpVZ55N43ajdE4k3Uw5qGMgjfyiptIqgvFZ4LUHSTbeSidl-09UZrruqo-gEucdPuli_odedeTBpXsh3uGtjAaCbW9rUk_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac99529467.mp4?token=FagTE00aFecrtgH4M5AX0m497_F9fTBy4SdnYIaeuZNcZr-vriNmAHVXKQzcmirF83-_1o_KJyqHEyxMdSRQx_k4s06xNOMyiUmJ9Xvwi9tv_5-mzPMGTMc_QgLFyc6lyCNRxzdnNT6hsA9Q9XeOAXnsNApFWAlU9JQR60J4sXPLDLRFzyyQXoUaqV-z2rfmsMwIXxYjq9k2tnGjSHoDhc0KF_jdfEoEBzNNXPmX0ETUi5-a9HvKK8GXpVZ55N43ajdE4k3Uw5qGMgjfyiptIqgvFZ4LUHSTbeSidl-09UZrruqo-gEucdPuli_odedeTBpXsh3uGtjAaCbW9rUk_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی صبرانه منتظر بازی بعدی مکزیک هستم دلیلش هم به خودم مربوطه :
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94436" target="_blank">📅 15:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stQ_l3kkJj0Y5jcfXObwSWWbQyLuYUr-lP9ug7n1AeUbk1tMXv4hgDVw1L3r2g1wPpEsYFyz-3ckrqmldLpgtWN2DkIlCCi-k4nwAvbZhfTQDulYqirFNgGewhtr8cgrTS71hBYYHmpRLcUp-FPb8E6chP7kj1Ai9b67GSyO5-obVsGpq2NTBeLuH7wtfljPjp0EO_mCRj7iCU9RlrTaesrkE2tvFQVQFF1Gyvtw5hHCHyuIeoAdOnTWY5vb3isjsiWupbt-4zhzl11PekptgDTuPVePC20h8XzZH-si0T6IiwDEv1I3SI4D2hvMK-GgMs0oZiKfHlkbS9qqaC0bOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
جشن صعود مکزیکی ها؛ پشمام از جمعیت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94435" target="_blank">📅 15:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d371de557.mp4?token=iuE3zFgJhaAVFEEg9_IuMis2zM-uqAjUn6mDBLAyLRkRD4Etkua3z-sfDvDPWigKssFK1SlTfOz2sdV099mZ-t9Hfghv0WXJVeNTV9nLOzq1-WWZub5YEWISJ_7_GRziHjzPN2vYvWO1GPIpbrIJwodM5eYXsexwbQhaH3WQJ03oaZ7k1mWx7nCSvgoi2RJ_CKcXmr3eosQXCJAeHjqTSNHnMOCg8fKJUefM4L4ZJM9qtGBW0CA2cQZQl4SNkh6PBRje8g5D22BUqXOZlXuHQnPrk8ZZhBKKO4iFBOfd_XX3DR9pv-5ec8_pXZ5FCEhVxNAgQ-uyj1HbfMsrbX-SPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d371de557.mp4?token=iuE3zFgJhaAVFEEg9_IuMis2zM-uqAjUn6mDBLAyLRkRD4Etkua3z-sfDvDPWigKssFK1SlTfOz2sdV099mZ-t9Hfghv0WXJVeNTV9nLOzq1-WWZub5YEWISJ_7_GRziHjzPN2vYvWO1GPIpbrIJwodM5eYXsexwbQhaH3WQJ03oaZ7k1mWx7nCSvgoi2RJ_CKcXmr3eosQXCJAeHjqTSNHnMOCg8fKJUefM4L4ZJM9qtGBW0CA2cQZQl4SNkh6PBRje8g5D22BUqXOZlXuHQnPrk8ZZhBKKO4iFBOfd_XX3DR9pv-5ec8_pXZ5FCEhVxNAgQ-uyj1HbfMsrbX-SPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
هوادار آرژانتین بعد درخشش مسی مقابل الجزایر؛ فتبارک الله احسن الخالقین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94434" target="_blank">📅 15:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaNBJRDgpLoGd_ST3pz_iez3l1ZVzxj5naEixotYv0zEQLL4a2BLEqT2ggegOdhFt1qbbuJfvcs4WjXRHTLhA6TN9hgTf2PymhNb736QAE_-o9On5nfAklhaoBxyZmLdC_sAxzGQU5llXUfeovgUUrHUKTrbKjrTiEEwVPXljcc0dqjG1F6v16Bet7IuD4BCXCmiO24H6Uy4QZQQCOK_7OF_F3t7_vHwatzzc_OIHodfTE4azcKUNc-2QHQqp9FKvjfurBMb7c0BTc7zjZa31zzuUpH5L2YpcIKkWOxE7shS-pHbC5Ek1JOzLoCNx3VfGQYVAlqeXkKLsyz_EwT2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پیرس مورگان:
اگه کریستیانو رونالدو هم همون خطایی رو انجام میداد که مسی انجام داد، قطعا اخراج می‌شد. برای همین میگم توی برخورد با مسی و رونالدو یه جور استاندارد دوگانه وجود داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94433" target="_blank">📅 15:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu0dAnDbJ6gj0ggslCM52gqi98YdWQJb4HcgQv-uG4wOi_sCDcIu29MAG-3KpeY2-ReWMbUhHWPjqY1voXKyDrFMCEiUeCO-ySno0bLrJWd2rBWqUwIpf6f2UR_0yzHx3PWFvrewh1x1N6HZdgYrMNNs7I-7W8O3B2ZiPeImzaevSPpcceL-7mj4VYdTrDhS4WMYBSvy08VI1kztEsUEwlpoLxuxsMTOH1HnHTmM24U3kq0wLMv4ik2-vDiXUSFHBOajFlRI1fHDLrHnYsUsKEbtuE2XYopdzGBMm47W15yFYKohn56BUQ3rIvGGTOnMsig02uRvEe0SNOHA9hvYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
رومانو:
🔵
🔺
منچستر سیتی رسماً با جرمی دوکو برای تمدید قرارداد پنج ساله‌اش به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94432" target="_blank">📅 15:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMSoGG7lPgpGun8-54f65CAPFJyQKBKwIVvtoV_X2Qfy4xPLFmaEa7QxDZHx19_9l4H_6XF7Ln6IGvnYr0p8fSTCqszBq2P45epvvkihtnn-3lMrP4xXMO0e5uRsG-qpMYH3A0cnsPyDvtteQ5VIiOQucwb44-GBu_6kyDKehYOfFftKEve8lQEMi6O_pyZ0IpeQOgjPnRNTWt2Aug07HjYGnSqm2L8Cdp7K3jrE8xl4MwIxWfLhCF9Ga6ejKYGzoeyl8v_40IhTLUJbCn62k43a2SCTfjATtpEkE_xxNU2vMClIFPjqmcUZG1tOaVEfjaKX3mWU2PDvpg8Rzq_vjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
#فوریییییی
از فلیکس دیاز:
🔺
پاری سن ژرمن در رقابت با رئال مادرید برای جذب مایکل اولیسه پیشتاز است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94431" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94430">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd3fc84dd.mp4?token=Vl1hiwuw1b9DM_N8mFSWys5fsN3mS1yXddvVsvAjN7l1DZm8JmMlYtNhDx5dooE9VXNsI5aotLVSTTsOBd-XG5kJj63SePbXCANOhyFp8em9P5ZXAqfFPaO2_758IiW1uTWg9S2h8T0hSfWAVhgFZbHEScwXxQmd0XCc6G1QoHhiwWqC87uNwhttbVsId1WQqpu4beKSA94DCQJxngGbtn3HzugiDndClLwOlcauhUAiS0klROz91Pue1DLV4Ncf94SLIT76JBMPskZMy2VSQLYSOo8sYQ9MNOBPaNhNmLA6XzrNXdHYm4hTp5jK3uweBCqogvrxCugmAKidnUUdLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd3fc84dd.mp4?token=Vl1hiwuw1b9DM_N8mFSWys5fsN3mS1yXddvVsvAjN7l1DZm8JmMlYtNhDx5dooE9VXNsI5aotLVSTTsOBd-XG5kJj63SePbXCANOhyFp8em9P5ZXAqfFPaO2_758IiW1uTWg9S2h8T0hSfWAVhgFZbHEScwXxQmd0XCc6G1QoHhiwWqC87uNwhttbVsId1WQqpu4beKSA94DCQJxngGbtn3HzugiDndClLwOlcauhUAiS0klROz91Pue1DLV4Ncf94SLIT76JBMPskZMy2VSQLYSOo8sYQ9MNOBPaNhNmLA6XzrNXdHYm4hTp5jK3uweBCqogvrxCugmAKidnUUdLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
پرده‌برداری آتیلا‌حجازی از بازی‌کردن مرحوم ناصر حجازی در لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94430" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94429">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2XFLmgiacRviocpPTDJhQiluJATj1Y9ECTnXZW3YsFsYz4eqMEqaevqRFyrlVxGn_dgfmUk5FR0FfthEv6NtbSp3qw2HgGSsofhJGRaBaKNhebHMDrmXy9_AArgd_76hnhmYXmYkYRi3_xQCM2B1zJgj8hjGlmhM7evwL3FdFQWB8F1fiQ39wczXEASRaqbSXaLkGCl5WCHHebe8W8lpOr5D9q2azU-gvZ9aH5YKYddnp1AP7_ywtYLasNqqGcfatX_dWMkQn7wCzp5Evdf-BL2DY5YprEM2lT9IdFA5P_aRkiujN6hAVFY1_5vI-ojYk6F699zcxfcakV9waIieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
گاوی: «هتریک مسی؟
چیز جدیدی نیست. مسی بهترین بازیکن تاریخه و من همیشه همینو میگم. واقعیت اینه که برای فهمیدنش اصلا لازم نیست خیلی فوتبال بلد باشی؛ خودش تو کل دورانش ثابت کرده کیه. چه هتریک کنه، چه ببازه چه ببره، همیشه نشون داده واقعا بهترینه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94429" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94428">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c3b02c2e.mp4?token=Qdui06OW4fbtTZT5gBXxG-xvljxjypnO02Tj5ONeeQ6cRZDUjqLwtCo4cHnd4QkwdNLlJk1brGl8TMOf4wa7mdiDb3Z-FLRPB5mn8fYCId9mtW3KlGrr5XJ1qu1OHillwQtg-VAAd4DqQRfVl0MPyc3tLlpn2dhvTptSYFgYoq49NLoiiu565T4x47d79s23ZFPo24Ll6QjC6FE4XD4hEeAvXpUnzruEwuCHpgmRdN0A2WiZTk4WeJUIjvUOJZiiytvM15LPFhGozteB4x44j2yMaH9IEHU51C0siVcYo-NiE7szddgqacaPlT3POXBoBhj6qHIyKSnleMtNq7OxKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c3b02c2e.mp4?token=Qdui06OW4fbtTZT5gBXxG-xvljxjypnO02Tj5ONeeQ6cRZDUjqLwtCo4cHnd4QkwdNLlJk1brGl8TMOf4wa7mdiDb3Z-FLRPB5mn8fYCId9mtW3KlGrr5XJ1qu1OHillwQtg-VAAd4DqQRfVl0MPyc3tLlpn2dhvTptSYFgYoq49NLoiiu565T4x47d79s23ZFPo24Ll6QjC6FE4XD4hEeAvXpUnzruEwuCHpgmRdN0A2WiZTk4WeJUIjvUOJZiiytvM15LPFhGozteB4x44j2yMaH9IEHU51C0siVcYo-NiE7szddgqacaPlT3POXBoBhj6qHIyKSnleMtNq7OxKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انتقادات تند مجتبی پوربخش از مهدی‌ طارمی بدلیل مواضعش پس از بازی با نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94428" target="_blank">📅 15:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GEToepy0zFjv1jldJWzR7u2DV3Ggw8PL4L_nbRTNPdyDQviDTzbf_mql4Tl7povuoCead4-abpzT-79MtqKevTqzGm2bDxoFpWSlwiakPbwoEwvye0moRVYFOWGc-E5aQsyHR8558JsHN0eUDwovRMqi3wRTbOP4cqKyCcFPvKBL5u82LVskVDmIQI96zpYFpmHTDm-W-IvLks7PHpFlLeKqFeI9YB8TZOGLmSPJS7YUN65HjTTiO85REFMQL5g3YmoJC7cradpKkcYwNVwJ4rfFDgGrUqejMLy3LHLzboMN_kX2aVRbcERVapTIdnEm-RJLy3usfUoRF2d668woog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7jRJBrTljKq9TKSGXxPioNCjQVK_DS6siwrobK0SJNGppiDkPUGc3eJD89cB7LZxgPyhUO6Ug43bp3-QgBZga7J-LE8Dd2prZejfOS0u3KpSvnvUyup2bACANSnk6zQNpyAx09k4FzjJGaxZ3SXpyR_AGIiGHfj80H1TZMtr8F38I_LjMB6ilwZNRKpgIZP-azRt1u62BlMGIZ7LfOi-c0C8TkgykzERdHsBxTr9u2vApOIkk__4G6IeDZjrRc74jOnXbux09gMTGeRDs50H_JmO7AyZqhTHa3pYKn_m-TdkKmeAbu3zqeYnw8T1WIshn0cpoY7RquDmPjhtK-QRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
خواهر کریستیانو رونالدو با لایک کردن یه پست علیه برونو فرناندز خبرساز شده؛ توی اون پست گفته شده بود برونو با اینکه بازیکن بااستعدادیه، اما توی بازی‌های بزرگ و لحظه‌های حساس اون تأثیری که ازش انتظار میره رو نداره و وقتی تیم به رهبر نیاز داره، کمتر خودش رو…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94426" target="_blank">📅 14:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiI9RUFFbQskjkcOEUUjjIs5jKvZ5n4CWoREY51xw0a9Of3jEy6m5URSktprJCCmBs315iry7_mF5wzoXfLrMLUEdStIklkkzgF673vysrINdmJV7TwZ4sGJFkJ7tvyAhSmxEgA5lbt6p7A4RpU3di1P98mXqbngCuvZOEHvBvtIArOcxJ6ssQvt-aV9InuXxuExDPS6f0xnOzuZE-qKz5Iw4eaT8dDJZCVmdnu4Ws_fx6UEPfma4T-QsZUW_FB0KvqLlYawvkq7zDCJ9DDKTRTQSb1NKqydgMSCixelLXQr9o_CM1vuZyXZeIzBN_831v6Cuk1GlYlAmQ5Dtu-LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🚨
جنجال تو اردوی اسپانیا
😀
داستان اینجوری شده که بورخا ایگلسیاس میخواسته وارد کمپ تیم ملی بشه ولی مامورای امنیتی آمریکا راهش ندادن! هرچی گفته «من بازیکن تیم ملی‌ام» کسی جدی نگرفته، ازش اسم و کارت خواستن، اسمشو گفته بورخا ایگلسیاس، اونا هم نگاه کردن گفتن «کیه این؟» آخرش هم یکی از کنار خندیده گفته اصلا نشناختنش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94425" target="_blank">📅 14:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2eQXC5o-U2J2gO-fvE8ca3COuKWNh0199cU_mplXT2S14SCiJaMP5JO5YTP4jBQg63FHe3xD-E6RytCr-e_N7MoXp5rv2SGLfXc6PlxIry5ogx14A6u55gQ2h9K-UVAuI8GFX4lBAIHzsZFRaBbWOidc6YjKIveAVMp4D8Aj-WtQliCFq2x7VA7EHKhhYxmAyRCRDwq0qCciU-7nyHUVU43MHWelnUQ81cPkzrkgRKjtdcGG5GEsf4Lye4X3-_9ke8rW2SC7eQmmw9j8JNFoA55KuUJ1GM1hJncv-fb08RkmjtzrKs5YZ1xHXlD5KJjzgjiRNYMb-ebW8LqETCicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
اگه لیونل مسی مقابل اتریش گلزنی کنه، به اولین بازیکن قرن ۲۱ تبدیل میشه که در ۶ بازی پیاپی جام جهانی موفق به گلزنی شده؛ یک رکورد تاریخی دیگه که میتونه به نام اسطوره آرژانتینی ثبت بشه.
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94424" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/94423" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEcFIWGnyAL_aainzETtPcHHjBSCfFgFjJsjgf-NzCP4QOTA1kDuc73mHZxXO_uxcmyxk3xuqNY6reR99WxJR9eAwyAHfEwKj1X766lEjbS5cLj2mQsuKe9CUi4wT_tEnw1SvlFgMc76Mia2JRWKn3JvUaye9jkdBUnn0vQfsmpdb4VP76dScScFOmEJnFosZ0DqYWwRIm1fK3eH9szhgHxKbw23WqWRlHtFlXNF4K-HT8z87-JjhwQomrLy_53knbhSYh4EsWxU3_wEOdsKuCS2_ISjifOuYcrT3OQVGW0JQR8WzdRMC6bMLzraSyLAgiTcRgKwZmU1laoIyo7aCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94422" target="_blank">📅 14:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3d48b39d.mp4?token=qtM-2Fhas587llHFrgT2_p8pA9_tV2iSA6SjrNb1_wMHP9cXRjMPDUfE9IABnkb-pvsndO3HpzCLj-cLMn6-32sWPywstm7OgULjDio7a_X6yribI_fAPtVQ6mdhLdcjHw4w1GGbbskdSK26aFYDHLiwt6Dz-g_uhcpJ9JGrUDulbANbozwpQgUc4XK8vqknBozyTzkh0eevycxC0iITbGCtdmkODq6JGxlBAAJI_gXf1bKEZiHk5NTde3pUVQHOJDisxL1h0CqLwgszwGFYLYK66EbmOZHRASocM056ImBEJc-jilmZN8d458byMVZs1a-ErPdw-JqBv915Lg_2sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3d48b39d.mp4?token=qtM-2Fhas587llHFrgT2_p8pA9_tV2iSA6SjrNb1_wMHP9cXRjMPDUfE9IABnkb-pvsndO3HpzCLj-cLMn6-32sWPywstm7OgULjDio7a_X6yribI_fAPtVQ6mdhLdcjHw4w1GGbbskdSK26aFYDHLiwt6Dz-g_uhcpJ9JGrUDulbANbozwpQgUc4XK8vqknBozyTzkh0eevycxC0iITbGCtdmkODq6JGxlBAAJI_gXf1bKEZiHk5NTde3pUVQHOJDisxL1h0CqLwgszwGFYLYK66EbmOZHRASocM056ImBEJc-jilmZN8d458byMVZs1a-ErPdw-JqBv915Lg_2sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خارجی اومده موزیک‌های کشور نیوزیلند رو با ایران مقایسه کرده که در آخر ببینید واکنشش چیه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94421" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f31df64f.mp4?token=IBzA8Lr5fBVRVMzAijS8ec-_nTOtecu8yjtu8gxti3MqMW5UhCBQTf0aBEIdI_ikeObbxEfxjaqdjirjO4Q_d5HmZZ8BoTTMep0-3p6FLKHIBLrrb0PlLV6i3_QaRmkkTpRVmQTeOtCQGZgVk6J5oNRUq0Ie5XsKrS7ATK8esV4CWmscZrkJokXD1jdQTc7hc6AID3Jr2GfXOOwFe0IJ_Q34XPYvKVTOEwLrfLrh44RiMuhLuvA3vcwupNBZyZRRw5FxQlcij3LNiQ1TNovqX5J_CYe8zyg8nS3wgzcOUxXyll8UMORPKv7uq819voQ4MgSmxzig3RybjFjxnV1lJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f31df64f.mp4?token=IBzA8Lr5fBVRVMzAijS8ec-_nTOtecu8yjtu8gxti3MqMW5UhCBQTf0aBEIdI_ikeObbxEfxjaqdjirjO4Q_d5HmZZ8BoTTMep0-3p6FLKHIBLrrb0PlLV6i3_QaRmkkTpRVmQTeOtCQGZgVk6J5oNRUq0Ie5XsKrS7ATK8esV4CWmscZrkJokXD1jdQTc7hc6AID3Jr2GfXOOwFe0IJ_Q34XPYvKVTOEwLrfLrh44RiMuhLuvA3vcwupNBZyZRRw5FxQlcij3LNiQ1TNovqX5J_CYe8zyg8nS3wgzcOUxXyll8UMORPKv7uq819voQ4MgSmxzig3RybjFjxnV1lJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن فیل فودن به لیلی فیلیپس (پورن استار) میگه نزدیک شوهرم نیا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94420" target="_blank">📅 14:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1661c1c04c.mp4?token=d5TB7OT2i0uQO_1Zb245dE42EsUJDstro0qd9D5zzVTIQKumMY34xwzWrCVTT_A2r98q6rWB7pWSkuTV_h2g2dBT8LqMwrh_05_ynyfyQUfMVo34pjpLXjm5BjBUVjQH96hiztcGIT-GUFi1R7jIGzDdPZauPckxwHrJNF30z3olCKbCHeRnmrV8gOSTVgwQ1gWut896Q74NyesQl3vZDoIdPKuOqxbDYSdA2mfvySYJ_QgiiD5G2zC3v5RI2qHZNkScEmivorokWMekXnUis9ZZWsABAQ_-lEeCG22xwkrORTqQKaXFM8EueNq0FIxMenIetYkaUH7WKMVtHekM3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1661c1c04c.mp4?token=d5TB7OT2i0uQO_1Zb245dE42EsUJDstro0qd9D5zzVTIQKumMY34xwzWrCVTT_A2r98q6rWB7pWSkuTV_h2g2dBT8LqMwrh_05_ynyfyQUfMVo34pjpLXjm5BjBUVjQH96hiztcGIT-GUFi1R7jIGzDdPZauPckxwHrJNF30z3olCKbCHeRnmrV8gOSTVgwQ1gWut896Q74NyesQl3vZDoIdPKuOqxbDYSdA2mfvySYJ_QgiiD5G2zC3v5RI2qHZNkScEmivorokWMekXnUis9ZZWsABAQ_-lEeCG22xwkrORTqQKaXFM8EueNq0FIxMenIetYkaUH7WKMVtHekM3Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این تیکه رو قرار بود پخش نکنن؛ خاطره بامزه حنیف عمران‌زاده از هاشم بیک زاده
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94419" target="_blank">📅 14:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxZTwjYh6uVPFaqomURBUKsWpKgwUXVnovKNye3HCxqnC_69-E3k7erFSNTnJhjmL6t_OMju9-hLKLssivmDrxUy_JDDzowWrhjnEgN3KkQLakSibQqmMHU9Q-JtzYfbyy2q3_KgHu15tVjU_xGc_95dGgKRAJzpeWnNV-RuG-PodLKVS91-AnfjTgm7hyjzTExOAvzcpU_DWHy4QP09bdV_ThJazbC8eM0rflkoQz3OGdWbW8nuA6bij5vq_I90p-lvHAOrwj-au_N6SkD1OWQCw2D1_3sSEipst_Dg4wB2p9MwmIWEdHC7hOg3AqFOO9WsoqkVDbKMG2g2JZHxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فوری - اسکای اسپورت:
بارسلونا وضعیت میکی فن د فن را زیر نظر گرفته؛ مدافع تاتنهام هنوز قراردادش را تمدید نکرده و همین موضوع توجه مدیران بارسا را به خودش جلب کرده است.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94418" target="_blank">📅 14:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d15c801ab.mp4?token=WxM_p3OVy2IlUpL8ElwU9LlUToO4oYGHfeIiqdHQ4recdFkdLyTBB3kO34KD551pgT19XUhIdeWWfy8-2bmMU94rEXcf4jJg9VvMj7RjvGvrp7xcfzSXpWQQ6QKqlTaTh71HDbd190wYBnFrdG9vGUpS6VbdOdrgIB8vXgL8MA3yQ5cB-9duv1ofGhK0l09KlmxTOO3DC1qzBR9RyYfMGGiNu6on8Gv1Zouv4pE-CfMD3Q8PuWW9Xiq2EeFf4WRzvROyvK6AjrlqjfYvjRZ6PozPhXsanBKW074El-sbEcW8v2gvVUp4YFHlsSTNPWoJHZYhdGXQR8dTAFMc9kDk-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d15c801ab.mp4?token=WxM_p3OVy2IlUpL8ElwU9LlUToO4oYGHfeIiqdHQ4recdFkdLyTBB3kO34KD551pgT19XUhIdeWWfy8-2bmMU94rEXcf4jJg9VvMj7RjvGvrp7xcfzSXpWQQ6QKqlTaTh71HDbd190wYBnFrdG9vGUpS6VbdOdrgIB8vXgL8MA3yQ5cB-9duv1ofGhK0l09KlmxTOO3DC1qzBR9RyYfMGGiNu6on8Gv1Zouv4pE-CfMD3Q8PuWW9Xiq2EeFf4WRzvROyvK6AjrlqjfYvjRZ6PozPhXsanBKW074El-sbEcW8v2gvVUp4YFHlsSTNPWoJHZYhdGXQR8dTAFMc9kDk-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
همچنان از کراش‌زدن خارجیا روی تیم‌قلعه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94417" target="_blank">📅 14:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcSqtiMxaOJNJw49Znvy0BU7Vb-5ESBVUmrGTRpulbIV21pMoH_5-htxW8zF9xiNvyiyDwiQ-1PfgdR4ZMhLyqsNKMvK0_jrMdpQah_tHL6troMB79VOpqe_iDHEWIxl05aqVO_phME1466hkXtaDJ8r1acxAb2Xi-PPDrmJSwSHx6EzCR0hPsN8M8vB0eZ0v-jMacjfHTYkMpNBP6wbfnHkl1f0Ru8qgvUdkOeQLCDTdJqmW-TB_g-Axz2bsqBGfB3BJFm90jCV7lLPMJWR0MdVdP6S9EYLGVh2dea0PphEIPchzDH4XM_VYQXJTSr-BRJ7_1cSMvdu55a-vMc6Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ژوائو نوس: همه می‌دونیم کریستیانو رونالدو چه کارهای بزرگی برای پرتغال و دنیای فوتبال انجام داده، اما اینجا همه برابرن؛ کریستیانو هم مثل بقیه فقط یه بازیکنه که اومده به تیم کمک کنه و کنار ما برای موفقیت بجنگه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94416" target="_blank">📅 13:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43da0169bd.mp4?token=mzUwWtkGd-bQ7z7MBJKXeRiSzNTPpG8doZr5OOqBplekOnoJx7eHwXf5WhKHGRUmizwi-xZIROrlJKs3EzA33DUQwOCwA79eMeQDladlINkPl9daImXKQf9BjoaCtRz_b6RpiGDJobwn7ITMQZb-k7w1zOQkNODy9s66dJqPF4r6yUp2ZKNBHpawSv_Ui2IhuXwwXIC3USnxr6W66fKGmXYh0GbXosZ8Xg85E_o16Lvqc5QO0jqWGwGqfOwYlFE2KT6puNch266veWwf0Y11HxY3VPwqnBew8tGrlqiVmUom-7_W9tvEs81i41H2GNWAoEyCqGPJkXEtQh9XdkQOI5G3U4ExnpMXQuJHU3bE3NVMyyW8pqJayeupiM0iRX8sBDF1TayAOZQNPNxaC1bFlWUZcBWNzBvsIi6i_anVa7ZvSH4dGkvRUfk_PfZMesJpWjFLR2PHwRsSBuqZnHAYIaxNBpyN0TS-bw3m-DEj2c78F3Z5GwkfpbhtQwyMqZHu4BpqAor1MkhORhPjCL9C6yYM8iWcT6ksx3rBO0GLDUWHw-Q7maVrsBzt2MY-P0_fnsQuDrHo3YGwS9gsmT9Hu9or0VmvpGBSAQLn9S6yOmSs1CFBvkGSnSF8pOXjwfisKdmU1GGQfNSgJxvmorDW3A0JsozDag3v92WhrcHPN6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43da0169bd.mp4?token=mzUwWtkGd-bQ7z7MBJKXeRiSzNTPpG8doZr5OOqBplekOnoJx7eHwXf5WhKHGRUmizwi-xZIROrlJKs3EzA33DUQwOCwA79eMeQDladlINkPl9daImXKQf9BjoaCtRz_b6RpiGDJobwn7ITMQZb-k7w1zOQkNODy9s66dJqPF4r6yUp2ZKNBHpawSv_Ui2IhuXwwXIC3USnxr6W66fKGmXYh0GbXosZ8Xg85E_o16Lvqc5QO0jqWGwGqfOwYlFE2KT6puNch266veWwf0Y11HxY3VPwqnBew8tGrlqiVmUom-7_W9tvEs81i41H2GNWAoEyCqGPJkXEtQh9XdkQOI5G3U4ExnpMXQuJHU3bE3NVMyyW8pqJayeupiM0iRX8sBDF1TayAOZQNPNxaC1bFlWUZcBWNzBvsIi6i_anVa7ZvSH4dGkvRUfk_PfZMesJpWjFLR2PHwRsSBuqZnHAYIaxNBpyN0TS-bw3m-DEj2c78F3Z5GwkfpbhtQwyMqZHu4BpqAor1MkhORhPjCL9C6yYM8iWcT6ksx3rBO0GLDUWHw-Q7maVrsBzt2MY-P0_fnsQuDrHo3YGwS9gsmT9Hu9or0VmvpGBSAQLn9S6yOmSs1CFBvkGSnSF8pOXjwfisKdmU1GGQfNSgJxvmorDW3A0JsozDag3v92WhrcHPN6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
خاطره بامزه حنیف عمران‌زاده از کتک خوردن مقابل بی‌آزار تهرانی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94415" target="_blank">📅 13:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5j18wQjC5xmg18uGka-I20lsriOWNONM467Au4bEKHHMxSpyaBtBPHj0og1_NupufsPzNxEkcxOoI9rzUd3hm2N-W59jlYu7CYW8Hz_XKHL5TjIVeTWwAbZt85EV4WHGbLO7338RXXvpkSt6j_jZKXVl60UqoBxiLnVNKoVUCKiJ5VXjq6sac9SY8vNqSc8p6XVmjoxjOoPEQnr-paKqvOthfC_5VErWAJL8Bh_MF8MhFH3BZ0XlGc6W0TEstOyh23zM2x_mi-g-I8D06gbMkaDv8BzY5WRDjmyj_25v-zQSj9QFCH0F3BHqw28xafu2BnDw8F5lM8uepKFja1GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سانسورچی از دستش در رفته یا اثرات توافقه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94414" target="_blank">📅 13:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2UbHP35a0l9hUPbsb58t00w1RNIeE-RXCeIaUsBSmxQWtNroCa6Am3Z1HKae2gg_5YRNiRxcVtRorE9eogMIrvlSaCGqTLU6qd1_HeJOssTUh0qxPvcnBLRrfAcC_QiUeGVP3cC8VT3J7leUTmpVDPwGszhcwKSgU0ej1YaxQl9MKTVPjnuu6dZaX9tbV0vMhIlP-2GiwnpH2WI1dUrwz1uvID468TrAwvMG3WyGNnppp9wAkxg0MC9qVUl1hQMe3NQIuYVW1qQ0tJVvzIDuFoWlRFuZr6ST7q1Zp9ijJmxJsHNRgn9Ts8q9_kF8mH9R4ECo8ZUrZwTnAxA91vOKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
وضعیت فیلمبردار بازی امروز صبح کلمبیا که بعد تکل خشن خوسانوف اینجوری مصدوم شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94413" target="_blank">📅 13:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94412">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75950a2c2d.mp4?token=IzIEeXlvL_M3u4RImEASH2y5Vb42R5OZS6oS1NDEQP1ivIqBt4F5jp3xJYOSQ2S2wyZ3kp9S1XMZ7Qkw2quWRh05QcvppRVRb-hUyEeVbTtUGddg-65Z3R8rHkeu_3h_IdwjboK5O936JcitZqsCNwhG6w52crFeEsWD_sEEioA3kMHqZx01VKThADfiwoSYbH_vmXcqOCCojsLRrCattpHm3nNJ1dHZjUWbmBNaQeXhiLlYbD4U_E2YgPYTuy4GTnyic4VFZANlZpQC44FwTgsF48jlE3CPOfyybewafYcCDA1F6Co_yAUNpW3YRpfwrg_nn9Wqva46dWDIPcR8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75950a2c2d.mp4?token=IzIEeXlvL_M3u4RImEASH2y5Vb42R5OZS6oS1NDEQP1ivIqBt4F5jp3xJYOSQ2S2wyZ3kp9S1XMZ7Qkw2quWRh05QcvppRVRb-hUyEeVbTtUGddg-65Z3R8rHkeu_3h_IdwjboK5O936JcitZqsCNwhG6w52crFeEsWD_sEEioA3kMHqZx01VKThADfiwoSYbH_vmXcqOCCojsLRrCattpHm3nNJ1dHZjUWbmBNaQeXhiLlYbD4U_E2YgPYTuy4GTnyic4VFZANlZpQC44FwTgsF48jlE3CPOfyybewafYcCDA1F6Co_yAUNpW3YRpfwrg_nn9Wqva46dWDIPcR8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیک نشون داد واقعا شایسته میزبانیه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94412" target="_blank">📅 13:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94411">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7728293bb.mp4?token=hE8rj5LB-6O1mpFXFVfMrku6U7K1cZfo9ksdZeg9lZ2kjq2kaEYwifhZg8L8_3k7x57w8w0JK0rubIOBKn-d0GRaRnH9AOXUywlx9oSdDBcSrwckzd4RK0v_qpOe16BJHEeSJjhd87F_NAOjml38MzLeznEiNlpQbNwbNQvxEJtEp4hhFRZ3gaMVB_KWNkmO52myvbtMTS2MQMUrxVuV9nitWHd1NH2vnwo6XJqrI4cFBVq-magT4__GNoP5t922I1d4xbC7oSaSiNrXZADAw__PyCvIV4DzA4N8d-A0I2Je2dItNDcrb22OGGJ31Gqvd6udqRSijcDuvlwP2EBjAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7728293bb.mp4?token=hE8rj5LB-6O1mpFXFVfMrku6U7K1cZfo9ksdZeg9lZ2kjq2kaEYwifhZg8L8_3k7x57w8w0JK0rubIOBKn-d0GRaRnH9AOXUywlx9oSdDBcSrwckzd4RK0v_qpOe16BJHEeSJjhd87F_NAOjml38MzLeznEiNlpQbNwbNQvxEJtEp4hhFRZ3gaMVB_KWNkmO52myvbtMTS2MQMUrxVuV9nitWHd1NH2vnwo6XJqrI4cFBVq-magT4__GNoP5t922I1d4xbC7oSaSiNrXZADAw__PyCvIV4DzA4N8d-A0I2Je2dItNDcrb22OGGJ31Gqvd6udqRSijcDuvlwP2EBjAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی بعد از اینکه در مقابل الجزایر تعویض شد، روی نیمکت جایی نبود، بنابراین تیاگو آلمادا جای خود را به مسی پیشنهاد داد.
مسی قبول نکرد و روی زمین نشست.
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94411" target="_blank">📅 13:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94410">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04815885a.mp4?token=tj4xoNo9cWQRAd-NVJa0oJkac5AWqZ0JrEzm7NZR5m73yRxnMx_urkiKXHDtfFEpz6qvNbs_82ootCatO44WsPvmlexU-1vAngZ3H-2Nq6-anSsUBOZvbpV1N2TtiJNis5ns3Y0ZRcv7NYMCqEI81wfmWPdHE8-S33eugLbV833KmIMcsi5oqon_d8Pbdgl9GH_VtdMKc_eC4Eobka2dGbLCtIFQodVPEc2GVDSUNtgq3R_dUUjal-WAWBdohYewcups0iQNtVV7oKU1P38X5q425vi07o66H8d-DlSSlrHNbJWZQyFGfDck5EDbY-xw1teAhsSY9zoKGjsQcUJkrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04815885a.mp4?token=tj4xoNo9cWQRAd-NVJa0oJkac5AWqZ0JrEzm7NZR5m73yRxnMx_urkiKXHDtfFEpz6qvNbs_82ootCatO44WsPvmlexU-1vAngZ3H-2Nq6-anSsUBOZvbpV1N2TtiJNis5ns3Y0ZRcv7NYMCqEI81wfmWPdHE8-S33eugLbV833KmIMcsi5oqon_d8Pbdgl9GH_VtdMKc_eC4Eobka2dGbLCtIFQodVPEc2GVDSUNtgq3R_dUUjal-WAWBdohYewcups0iQNtVV7oKU1P38X5q425vi07o66H8d-DlSSlrHNbJWZQyFGfDck5EDbY-xw1teAhsSY9zoKGjsQcUJkrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
مامانا اینقدر سر به سر بچه‌ها نذارید :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/94410" target="_blank">📅 13:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afe9b255b.mp4?token=aWhUVDPB-SuSCgarwJODfu7IODWcF6nIpfr8FdT8VbUUcRpw1flM1SvN9ZACeqTCqzrQIJ4OStuxzmjHjFjOzQ69NBxgt8-moWMNY1hxie40BMFaic__o0FE8YrsrxcTRt7nRrhY_q-qagmAs-jy3ts2AeMaQfDtGwjm66y3GOUjR6tnUxBYJ7Bm1XvrjWhq1G1gKcr2Snbf4xK_RxLjRrzlnNbhBNfDuCNerXdpMhrgIkSwtQU-tQ03KDY_wy2u2MJZjLS5u9h1tftncwAOBHQ02ELLokW0ORB8VEzlBE5aI3rxts2zbCy6oPAAEDwYuSZ-HMGY_yg-gcUFcE_gYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afe9b255b.mp4?token=aWhUVDPB-SuSCgarwJODfu7IODWcF6nIpfr8FdT8VbUUcRpw1flM1SvN9ZACeqTCqzrQIJ4OStuxzmjHjFjOzQ69NBxgt8-moWMNY1hxie40BMFaic__o0FE8YrsrxcTRt7nRrhY_q-qagmAs-jy3ts2AeMaQfDtGwjm66y3GOUjR6tnUxBYJ7Bm1XvrjWhq1G1gKcr2Snbf4xK_RxLjRrzlnNbhBNfDuCNerXdpMhrgIkSwtQU-tQ03KDY_wy2u2MJZjLS5u9h1tftncwAOBHQ02ELLokW0ORB8VEzlBE5aI3rxts2zbCy6oPAAEDwYuSZ-HMGY_yg-gcUFcE_gYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من بعد دیدن 28 بازی جام‌جهانی تو 7 روز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94408" target="_blank">📅 12:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUs1LYJP6janSbng6364oaScfaZ4KVqdEY2gFLcXyr62cKYExdeTJ-gm-1Ese-_bC5C8NpoW7AMMTrR3N9emIq031qpVUXWugTQkvbDOJCsJ2BD0rPcX5iTr5q5klUHS8aTss7QO397DBUByd_7uoxX5Yq7d3TUNtmLTmpMx838S-NX2FO1Hg-Ws3V2iNG7PRDCU0we_oGnyUfVZKLP3H23QuoWXGB5NJ3Xk-nptAg16w6-08PLBq6qnAC3KuAm9GG_V8zOotuiGm8d5FyRffyy5yH6TvGRhbAGCWQAiIgopsbaOf-SR0VW5shI3ukAfYR_kTR4RgXDvqyy8Vm-tpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات ۲۰ تیم حاضر در پریمیرلیگ انگلیس فصل ۲۰۲۶/۲۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94407" target="_blank">📅 12:48 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9590a4f51.mp4?token=BwJEwxeDia8s_kuf8AI7C3RoDekObkNTLF9XrBW9Nh6vLy1fkx9Lu_Jwl3Lyv3r9B5eWqwKVL1THPTpBY9NEYuvDknm2zzIr3VMFsIhInUXwKQ6DLbrWXXRypKMP07l7bML7TOmKGNL_BffwjlccnW3k1F4019bzL-xwCWB6sr75SPPO4m9fCu-s1_Y7kb1YE0CNASKxt-vWfuEgYVVtWdyvA3b2v3qfTaE08gbTXh-KaFdTOIUqEzxx0n7OrlrCo7qeQz80mqq84ysV9OSoGjy8ASzIlkIqBWTRynUeS95BfeoWWDcPQgivihcIXZkZlx-T7gIEO6IFbYeOMdJ7TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9590a4f51.mp4?token=BwJEwxeDia8s_kuf8AI7C3RoDekObkNTLF9XrBW9Nh6vLy1fkx9Lu_Jwl3Lyv3r9B5eWqwKVL1THPTpBY9NEYuvDknm2zzIr3VMFsIhInUXwKQ6DLbrWXXRypKMP07l7bML7TOmKGNL_BffwjlccnW3k1F4019bzL-xwCWB6sr75SPPO4m9fCu-s1_Y7kb1YE0CNASKxt-vWfuEgYVVtWdyvA3b2v3qfTaE08gbTXh-KaFdTOIUqEzxx0n7OrlrCo7qeQz80mqq84ysV9OSoGjy8ASzIlkIqBWTRynUeS95BfeoWWDcPQgivihcIXZkZlx-T7gIEO6IFbYeOMdJ7TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94406" target="_blank">📅 12:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac52419b4c.mp4?token=qxGuuUrWnfCptnFzedWzM9kEugN8BU2t-eB2FLwwHg2ZXVcc4NnoERRPnChStXee2EpNuQh5P7iZV_ZGVSU5ZyeHTLDjRC7CbGC0k_DqIImdhSe3QsEWjoWHEksNQmGSd2y_fOGyao0jMLJab7Tlh0Hn97t5Oru-gJ5rcDfpu2MtQP3Ah2-6anUjON79UlKDIsSxbENcFpYrRXJSMOnNU8XCvK_oGLVoqhfXJYgILhsLWPyL9gPaiDvLuU4bpoTzB9jfIwQG3IUaraTfXPs_ghUPKRSZOomjMSD3aD0YT1OBcB6XuaA1FqW2IDnHgu1FCJmOwLzm3aTY9Bs9T3VHjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac52419b4c.mp4?token=qxGuuUrWnfCptnFzedWzM9kEugN8BU2t-eB2FLwwHg2ZXVcc4NnoERRPnChStXee2EpNuQh5P7iZV_ZGVSU5ZyeHTLDjRC7CbGC0k_DqIImdhSe3QsEWjoWHEksNQmGSd2y_fOGyao0jMLJab7Tlh0Hn97t5Oru-gJ5rcDfpu2MtQP3Ah2-6anUjON79UlKDIsSxbENcFpYrRXJSMOnNU8XCvK_oGLVoqhfXJYgILhsLWPyL9gPaiDvLuU4bpoTzB9jfIwQG3IUaraTfXPs_ghUPKRSZOomjMSD3aD0YT1OBcB6XuaA1FqW2IDnHgu1FCJmOwLzm3aTY9Bs9T3VHjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇲🇽
درک نمیکنم چرا خانومای مکزیکی موقع شادی گل ممه‌هاشون میندازن بیرون.‌ نمونش همین بازی دیشب با کره‌جنوبی
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/94405" target="_blank">📅 12:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94401">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdU8RzHZ5BCiNIFjVmVoGcWwYTQ6Z6f1CmjOxy5aP2nExKJvpgjfE1xt0lgM47vpMBHnvludIrbSYUhsg1hYxTEOJn3jua7n-OaiVkzTj5yleX7G8qUVUguYUuuRhQ7Z5_lQv7Prou9dtDisauX80uumc0I2smVW-6t9GN8XLdyF3SFL_8S_7--UWdVNXKqOGw_Q2hBBEfxvmLcMEsjTlSvz6DLfaVD91oQgjc4Cwtl_tT37Qqsgyaw9VFZgVu9B_CGHv7C6u61fxtFAzc2FwF08uvPIWNJxGQYp1NEhAthXn19TRMyh3AI8InAZ04EcW_VCxVsST0yb6QtKSqZSDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBf1qmVKlI2mkC8LABdnzpeA8F1ik27CoFoCj2XAeXK5-t-y6jTzlrMmMynBC98pak5VXTIbC7cTQLi2bshZsRHZWCRZqt5tV8HR80_6A-IpU-OT06Py2ZryJCQ9HV9rsNZ6LQPN7cWQ-eHwFo9PS1GPgbl8ZItfNQvvC3EKyzfd6K45X5CbEk-L4X6vFJyfhaNPGixMIvQZh4tx9wfxQ71DTN4VUaKHQiEpG-8eSzy0GXth79zxReoklKwFxtnMiRg4pV7ca8UwQOP5eYc1YTVsyy8qSijpegKOxeEr8Lod6zxfuBX-87HMGa9ixzTEkgXrRuo0xGIyNCX3tiSuAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXQAn-8m9Mq1-e3h83971QGCRHiAS-Gt2jkPWIbNvuVG5tae8503zR_kg_U21sXzeufhD26fCUrU2AlmmTE_8DMAyi3o605nRTNncWwrzyXouxA6uZb52kXXdvwBklM2nlRmYBwlb4k1hilAHyjL1cZP7kiqBToaozH3rLeqgNDMHD9oJtoUX_k88hLArfB2WluqvU_ElLDVL7mFrwjDBKI6lCskGdQRCUhl-MCJMkt8XcTdBXVfxMA8lzqLDLiyq1niHtnZRJb2GEO_ufrW5uaGzlL7wOce5pKNG2_pgOn0fBLKX36Frkp-nZOlu_gdp1QStoqUgXbfInJLFvKh1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jb7-zawFBnH2kcg-c6xxVbJtfkUEt2pOyvKbjsUfB1rquegDyn0k84392loL2ij85jqAYg77KZEFkmfreWnmXp2WX3n5zeVMtUx0cQOnAsXaa9gENvNNBgRumz-sZHDzEpPpas05AAMZHSq4Md8JwQawwPrk58nh1mkSOBjNW58aecwiIH4DavZqiJ6cXP6jN0-rl13JrYd1ETn41ALjVNZMPc2Paeyz3ZouN-IYYrB5vkSAc9NYbd9tRo8MhDXT5erEf-Y_USfn6fCw63LQD3D1XpbPui11WOjRy5uvyJE4PSx9ucmW215UMY7FD9JaGHIclftJoUpeZcy1Z2J7rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات منچستریونایتد در فصل آینده رقابت‌های لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/94401" target="_blank">📅 12:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94400">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2l6Gl_Y5iiBBfTNaje6FOLudv_7tYCrO4jKaz_8wcJHqPrgfxW3KeFo8cuzeDxvfi0BX8Du1Gr0FZ0ucSRRgSsmJCWQUGOFS91pXVQS_t9d6D0J0M2hXjAb_WCGORZgIck-imJvZ7Mshy3prVTkbxZfyQoB-IzuslXCWlrFGnRl4VzrnD6K_hYYcyMYV8N4rMaNiLxalaPEEMn8eOb4-0NLJ8MVDjcedRoy-HS4ItWhXuSHC8qluLL7HXCmlZgfVX8wNjf51W-l-RdNXzgrJszaj_8suFUwxYi5i4A9rWcYN7DXFYIMFWNZEb79chkjrWVCJ_oaMwdO7bveCHudtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بعد دیدن 28 بازی جام‌جهانی تو 7 روز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94400" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94397">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cYKTFbAEehP7xlCUEDt1nLP1USxicnUwpYq8tWBeBZQZ4hGWOLGi9roaiRkcjxAKjgncP6MI-f0G6sputmYp5hOfRgTKtbVoPcDxeBqKXNIcbsAJuUAOCj5uU7to7vH6TzXYpED-8JXNU9_-hYh0nwUIC_pVkFTzBDJuapbYJX19wwowxjuHTaZfsCyuuIV-SJXHYHGFEA6zFstFJIj_eINpBlOFbVeHVNtI-5BCTvjwrKpqfUkoRXM27GrMfC_PT-yYd-pk6kBbN7baGdui8Z59hmgo2G9fjWUXdo2WJ9T50wm6A4WDalgyb-Nx-b8Q7_EHgR3Q-DIKP2KXhektcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bk6tYbQOLdGnRGA91TLFQF9KsHH5a2WRuz9rqxO0T8g-Q5Hs1TvkBQDsnXZIX3SBEiy968E-fUVKsA0kR0PHd8kQcZSn237Yhf5fTiZY6JNIhQ_BCp9F2lDSCOySyCFXR7mkCafSkAqFVmAIb-pU4gbKQ4yTgcY0v6TUDV0dkJ-7re-tYRyFn18xgq9koCTIuntbqWLWJRhpgCwFk-qG0bu5-tRjhn1fFRPJ-VtzN-G1jldEo-TyXBLzsfciLCRJPfZ9iwIU5FZc3IyclBYCcMgWSg6gG2CppkasrsecC7wnsHr7F3WeeceIcZZoSgJdOWaEItWCsmwbIYKxzI8CUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N3mk1Q2eOhl_p3pk2YVhyqsKJ3kqB-vMyQWoYouwvuaRPgDR2JmwxlSJCTps4KTgQ0idtSoccLiDmS8cnT0uIo1t8NwC_5kHKuJTkRgwadekyRWn7LfS7GpoJIkqk_q-i5rHggdrX2jFCXuTiDrayhE2yOaJRTTDtVyoZm8IwCowpGpAynWDq6cBPDRWQA4wonxVIfqPf5O5oYwQg3p8EuB8QwS7HCaaEij9lEE4jRS2w1AFKsRPdAGFNrII_vCzZXGoUCCkF1dXC_x8cWrmZZOA2jdUi83_dD7w3Fl2XMZnJ_veSznFX3RkG6OBY67unk1NQ18BTd3L9_n0CIk25Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
🇺🇸
پولشیچ ستاره آمریکا: برای شادی تک‌تک مردم خصوصا هواداران عزیزمون امشب باید استرالیا رو ببریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94397" target="_blank">📅 12:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94396">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/929aa4932e.mp4?token=OkBvaTOjcrw0Sl9VFP5JsgHUzqt8KefsiPKuttfQrW_7Y8-BVth2YGSj3y6n3i4g0uCiXSXbM2Vm7mjbisIb3lFwR70t1DByTk6viTRoCXGaMC8TVZ-k9_mBRSVopT-1CpvEjsT1BoIMsGEClu9XHEaP5AM-5ibQBzT-AcYx3VxOOueBOPzAzh6AQrGJuIVHVheHKS6xT_GteIxNR34vonZEr3Diek5KQxJpPtcIW_xe-qggDA5ajFrKnFNcU2Wod7fH4IRkIqbKVQX5oKlsfc-wA1-9XbKj41zGpDrdXDshTPNQAGUsQYONPXgWfk43p7JKuQh4TGo_Qp7wDK268w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/929aa4932e.mp4?token=OkBvaTOjcrw0Sl9VFP5JsgHUzqt8KefsiPKuttfQrW_7Y8-BVth2YGSj3y6n3i4g0uCiXSXbM2Vm7mjbisIb3lFwR70t1DByTk6viTRoCXGaMC8TVZ-k9_mBRSVopT-1CpvEjsT1BoIMsGEClu9XHEaP5AM-5ibQBzT-AcYx3VxOOueBOPzAzh6AQrGJuIVHVheHKS6xT_GteIxNR34vonZEr3Diek5KQxJpPtcIW_xe-qggDA5ajFrKnFNcU2Wod7fH4IRkIqbKVQX5oKlsfc-wA1-9XbKj41zGpDrdXDshTPNQAGUsQYONPXgWfk43p7JKuQh4TGo_Qp7wDK268w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
تعجب و ترس عادل فردوسی‌پور از تعداد سگ های مازیار: میگه ده تا سگ ژرمن دارم
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/94396" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94395">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaun_Cg_2khaev24khjXCrMRm3xsgBTes_h96qdmzwz-7Wv1gKqrTlYWA-ibx399HROcK9YdtoolboMX4t3r1tcImnMUIlstKtD9qSfwFVjTOijHwC0KdV7EvP4ugL55lICDY14Wv1AtfiwpX9H2--fXMqCJp_1E10vdNGK_uAxuwGmXpvzKwhRdb0dGM2mUGcCal2bHObVU97JV9aa3Z6AaVGRKRNmkDyRAnEIDG9YW7K9W8lhb3MwRGAHLU8M-RpnZc_oWri5018_qXUACxN-5i_fzhm8Eri1PN2tPDSCISpSxgw_HjhYu76D6CI7wi-H6vy5AL92eHttWfQgm_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
برنامه مسابقات هفته‌اول پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94395" target="_blank">📅 12:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94394">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGMT16Z7daGH1f-U1Nb0C_fWVQbNiYdL8AgxYm4mlOc1kYpUB9ik57UYx1KMyP42UxR08rcd__h9JubhmZ7LZmj0Z-ivd5WmkknfBg1knCHlxlfkxiXUp33LhrF2yBROhtfMEMT8bPZ4oZLZmNDG3ZoLDadSRmyTSxETvxHRnheYcD3Uy4iN-mcWkse1rX4p8Xf5duUXyx4GiNW_ebrowCMFIlSnpepSmvyxc7CCH6rLP6IH5U18quW0y1ceH5NlorO5XHEe33kOclXajKIlAOb6WpQQCLKAm0gjiFvq7g04cihAafX9lzJpx_-_n0Tim5mpmHB9IeFOxenHUCU4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدول کامل مسابقات منچستریونایتد در فصل آینده رقابت‌های لیگ‌برتر انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/94394" target="_blank">📅 12:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94393">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6e710942b.mp4?token=DHN3RAkvbQuM6C-wisgBMwEPglMIb2tV-uFk8lnKnKm3mVQiUEa3AyciLt87OrEQZ9XR65EolRBsMHDBhp5MQ2DUm56ukMyafU3Ju8F_ffuH9KaaF8tZIQB6p5jwSbgNIIlE5J_LwUs7YWdky03A_Zgh9wg-xxX9fhm7dS7ETsu-uiTqtQSNlCpM2FvND1DnT8zu7R9Mkrp1Ni1NYXvoaXMTShx0EBzueL5PCAmPM76N2ETusXqcgA3X4ZHCRN2Urng4RO9fvxJkauvOEP2mUk7KCupPgfqtONzUeS07S3vxbTrdYWoSOfCPPlLe8S7aiujuSYKk6MYFEx662xnR6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6e710942b.mp4?token=DHN3RAkvbQuM6C-wisgBMwEPglMIb2tV-uFk8lnKnKm3mVQiUEa3AyciLt87OrEQZ9XR65EolRBsMHDBhp5MQ2DUm56ukMyafU3Ju8F_ffuH9KaaF8tZIQB6p5jwSbgNIIlE5J_LwUs7YWdky03A_Zgh9wg-xxX9fhm7dS7ETsu-uiTqtQSNlCpM2FvND1DnT8zu7R9Mkrp1Ni1NYXvoaXMTShx0EBzueL5PCAmPM76N2ETusXqcgA3X4ZHCRN2Urng4RO9fvxJkauvOEP2mUk7KCupPgfqtONzUeS07S3vxbTrdYWoSOfCPPlLe8S7aiujuSYKk6MYFEx662xnR6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
روایت ابوطالب از ماجرای پیرزن و رونالدو؛ دیدی حتی یک پیرزن هم نیومد ببینه چه رقم آدمی هستی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94393" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94392">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14ba09e5b.mp4?token=TTgViTYzFmfeVgEcZ3H-hRKCGjvPkuHQhwZuDGJSlv3O1a7ycvLBDBTY5-6AC09sZN-tSVInhAThAzoIA3eAEPQtqpwhXTsqhVXUB7vvRqnfw2WOaQ7rSwI2U0ue3u2c9VVWaHSWg9FQgR8qcZ06TDtqHKBx-MNo-Qka4OUL-8YBaseHiUAZFmK80vNb01_uS1v0U43fg1zKeao5QG6UAcQwl9Z1alEvwLp_2grgIqT106xhtAIC-QpWlkAQmybJ3L0P0jstK6YawIKej2N4aDV15ee2jPe4f1GuzY5h1c8MV6zNypILH0PtILf-8UuF6crdNPoAI3jnYqmiupvMHDBiSTBOw0rh2TJebTVHtLa2dML7ODicQ8l102C-0Xp9ohv4BPrlRbuH0DnLNetRti0P2fCbhe2WUy5GiB3DWiXi5-wQ4iGx1KKerw36vEL9xZ9MNDp6c5-J19YAkpJ5OcP7ob-F4sp4EF0T_W2mZ6gQENxN4dkIOeuFOscGGaoxbIILaaic7t0RlnVytZ1kKkI1dCfQVYGr7eY7ToiRZ-mdO-dO9KM6pWQtiW6mBGG4hzdRa7U5GuyjV2QkF5tR1LgNIoDFS_OmMT7ARvwxzU474yN8nfxMFThjWe4YkxzeOkmttNC0qx09qHQl0tzjs9NbongtOTcz293RrAf6Gmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14ba09e5b.mp4?token=TTgViTYzFmfeVgEcZ3H-hRKCGjvPkuHQhwZuDGJSlv3O1a7ycvLBDBTY5-6AC09sZN-tSVInhAThAzoIA3eAEPQtqpwhXTsqhVXUB7vvRqnfw2WOaQ7rSwI2U0ue3u2c9VVWaHSWg9FQgR8qcZ06TDtqHKBx-MNo-Qka4OUL-8YBaseHiUAZFmK80vNb01_uS1v0U43fg1zKeao5QG6UAcQwl9Z1alEvwLp_2grgIqT106xhtAIC-QpWlkAQmybJ3L0P0jstK6YawIKej2N4aDV15ee2jPe4f1GuzY5h1c8MV6zNypILH0PtILf-8UuF6crdNPoAI3jnYqmiupvMHDBiSTBOw0rh2TJebTVHtLa2dML7ODicQ8l102C-0Xp9ohv4BPrlRbuH0DnLNetRti0P2fCbhe2WUy5GiB3DWiXi5-wQ4iGx1KKerw36vEL9xZ9MNDp6c5-J19YAkpJ5OcP7ob-F4sp4EF0T_W2mZ6gQENxN4dkIOeuFOscGGaoxbIILaaic7t0RlnVytZ1kKkI1dCfQVYGr7eY7ToiRZ-mdO-dO9KM6pWQtiW6mBGG4hzdRa7U5GuyjV2QkF5tR1LgNIoDFS_OmMT7ARvwxzU474yN8nfxMFThjWe4YkxzeOkmttNC0qx09qHQl0tzjs9NbongtOTcz293RrAf6Gmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
جوونای آفریقایی برای تیم قلعه‌نویی چالش رفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94392" target="_blank">📅 12:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94391">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=W2XHC9ewBX4Fqi9haJys56KzeNk_Dq7rBaXDzePR_tRUOImOyeaZuNkxwOj1763G1YhaF_DKiqeAbdoXJGfLAfTn8dN6gL6FDbr4OGt_RsSxClWvsafZpBjyefSuCi-YmzlL8uFJMxYULoVsFo7R1Hxyddfdjs022oJcUK6qrLs0nCeoZov9wbmCx1snTgOlAQa9oU_4-UBK9OWzBep1hUnGyC3P4MiC_w7TSVAFIrMfrUC1fR0dr7abZoUzPckKwn1HuDshABHQI9LHLijQ_5yCSpBIYPbu6ZU0cVQ9rL9sEebeaV2EC_Uj0QFOiH14LTz3OVDX89iBoxpipUt-HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1025052ee.mp4?token=W2XHC9ewBX4Fqi9haJys56KzeNk_Dq7rBaXDzePR_tRUOImOyeaZuNkxwOj1763G1YhaF_DKiqeAbdoXJGfLAfTn8dN6gL6FDbr4OGt_RsSxClWvsafZpBjyefSuCi-YmzlL8uFJMxYULoVsFo7R1Hxyddfdjs022oJcUK6qrLs0nCeoZov9wbmCx1snTgOlAQa9oU_4-UBK9OWzBep1hUnGyC3P4MiC_w7TSVAFIrMfrUC1fR0dr7abZoUzPckKwn1HuDshABHQI9LHLijQ_5yCSpBIYPbu6ZU0cVQ9rL9sEebeaV2EC_Uj0QFOiH14LTz3OVDX89iBoxpipUt-HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامین رضائیان: ما در مقابل نیوزیلند لایق برد بودیم/ اگر گل اول را می‌زدیم شرایط عوض می‌شد. امیدوارم خدا کمک کند و موفق شویم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94391" target="_blank">📅 12:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94390">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول لیورپول:  • نیوکاسل یونایتد × لیورپول • لیورپول × ناتینگهام فارست • ایپسویچ تاون × لیورپول • لیورپول × فولهام • بورنموث × لیورپول • لیورپول × منچستر سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94390" target="_blank">📅 11:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94389">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۰ بازی اول منچستر یونایتد در لیگ برتر انگلستان فصل ۲۰۲۶/۲۷:  هال سیتی مقابل منچستر یونایتد منچستر یونایتد مقابل ایپسویچ تاون اورتون مقابل منچستر یونایتد منچستر یونایتد مقابل منچستر سیتی فولهام مقابل منچستر یونایتد منچستر یونایتد مقابل تاتنهام…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/94389" target="_blank">📅 11:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94388">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول آرسنال‌در فصل جدید پریمیرلیگ:  • کاونتری سیتی × آرسنال • آستون ویلا × آرسنال • آرسنال × چلسی • سندرلند × آرسنال • برایتون × آرسنال • آرسنال × لیدز یونایتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/94388" target="_blank">📅 11:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94387">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۶ بازی اول آرسنال‌در فصل جدید پریمیرلیگ:
• کاونتری سیتی × آرسنال
• آستون ویلا × آرسنال
• آرسنال × چلسی
• سندرلند × آرسنال
• برایتون × آرسنال
• آرسنال × لیدز یونایتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/94387" target="_blank">📅 11:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94386">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff097f54b6.mp4?token=Js-ZmkNTriaZfnfaYNcxrLzo2aeFo6xYA0CbLscVjLH84GLt3UYArB99NerTQS46WBQffuLydM0_xWJI4uqT-daG3usacVTrfJy7rsbF2iAMaRwMCeL3teJ47_xqt1EV3OYCME8WoOFVTxWZcyWtdyZJZP64q3q4B1UPtg7RWV_s1Q5hcnrmQvnPbE_h1ZBFN4Njg3mJ90pR8Me8e5WcUyUhKChU5fnUDdiOCvfFSE-MC99tdBidvCoiwONZuSI-c8FcoXmCuZeEQAw3LTvEze1Wias-0Zgbu3-XIe25ct3Da2jpTQ-QWciTyqfPWmIRTWzS31RM6qoAL5J_2YjmqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff097f54b6.mp4?token=Js-ZmkNTriaZfnfaYNcxrLzo2aeFo6xYA0CbLscVjLH84GLt3UYArB99NerTQS46WBQffuLydM0_xWJI4uqT-daG3usacVTrfJy7rsbF2iAMaRwMCeL3teJ47_xqt1EV3OYCME8WoOFVTxWZcyWtdyZJZP64q3q4B1UPtg7RWV_s1Q5hcnrmQvnPbE_h1ZBFN4Njg3mJ90pR8Me8e5WcUyUhKChU5fnUDdiOCvfFSE-MC99tdBidvCoiwONZuSI-c8FcoXmCuZeEQAw3LTvEze1Wias-0Zgbu3-XIe25ct3Da2jpTQ-QWciTyqfPWmIRTWzS31RM6qoAL5J_2YjmqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
هوادار ایرانی حاضر در بازی مقابل نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94386" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94385">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGua4YJ3PA9ppItsaUM0oFKtFp5EpKelLuuY8kiQW8yCnr8vb49Ww3oVoXpvMN8P2ZVvI2cr1b91A_O1Oo8idvp2dzVFm2xAjN_7B_frZ0uqGgsbKaFkQaMeetv8jZao47SiWhJRYSnVo1QPd1UAvsv_XvZqwYkV-dyeewKO9tmXwMYNLeVGPgraupl59MbfAljAAPRN-IpMv2RhQE-KmEGeQpXiCSy5mR4h5MFZmKgb9o50T2gO9PFJA4LFXOyVFCpuf0eLe7T_PG1adVmRASuBxMGVNQDttRj--6PWj3wJB_jL-20ca_xKmn7ipgQ10zRAmS-oQw8ASUaYc2AP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد بازیکنای رئال تو هفته اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/94385" target="_blank">📅 11:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94384">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r14hOOo9mJZ2-Kb9duQYRQhvo92V76SqB2GaTZCUe9sidij1dVKNDLNK5JgBaDS_Pov8WJUK1NE7JTEovOQRRLMNY3VXMJrGW4YK-9lVG5jUtkaQC67uSjNqfuAH4zKKufbzjFiLbjPnKjxN2TQyoXQlZhMWVWlIOKcRP5ixEcf22stZf8i38qYzLDxG2UUcXtyRm0enMq7_0P45H36q0YzkYvREeaROng0v_A0OXlfU6eIAd7X1W4RiVminqVdV8bx1_1n3mEEAP7Fjc9_BqJMp179G5zTKxGCy3SQ6JNv1SwauMtlgSmPZjkUCPMSFkTtF_D3bmUTfTf89OMhKdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز ایرانی دست به کار شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94384" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94383">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6GXEe0hXGAncsQrakXUl3B4giYQnUNz7bO8XdmovQvP18ELWBAWcFBLg85Gjo7mJosLIshjoMQR_zYnlYA3S-IikPD-UODJCAIoVe10VJl5OV5ov_4ChstvLHyWNOceLUMCi3FSWjO5i_0b49B-QNawUldR3Adt9vks7GY3lG8w3GSQvDfXyn8HRGSBWqnUeVVUgyUYHukcUMAknU_3QyKYpjeyGZXpGwhsd5cRnnSU5kBokjGuzkHKE98FQIb0I0xQF-s0RW57Zai8YjWdAbB5yz9xK90sH-SGGV0hfggvFTze4xgo-uYDDjcvzErumreOESDKIRs3Hz98894ifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
خواهر کریستیانو رونالدو با لایک کردن یه پست علیه برونو فرناندز خبرساز شده؛ توی اون پست گفته شده بود برونو با اینکه بازیکن بااستعدادیه، اما توی بازی‌های بزرگ و لحظه‌های حساس اون تأثیری که ازش انتظار میره رو نداره و وقتی تیم به رهبر نیاز داره، کمتر خودش رو نشون میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94383" target="_blank">📅 11:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94382">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366d6a6d70.mp4?token=HgLXAM0PYff6jlhRvYQuvXEldLUSwI0MA7-P2y-hNAYDXmV_NyHDnhBE17fHZWm8_p62VN5BxQiv3tQ4IgnlC7KnEe97xgca4k43ETPPA-5ZZYipPLx9NuXoHiTSZHqPmfZDuRNKlacceoWR05wHwYQpjQE_wyHr7aygXUaY76x17t7_YMvQmnWCj3xOtf7kYwo_F2LYsgZyFQfbPKcYWQTDyUfmP6omZAsFrPNdctAI-6abQbYSDLoKdDoOzMmzlx9AQUfSqQqXeyBn31aVfhy_SqbLVWPe93yTekjk1Oa_W9UJv7VOfOpoEHsmO_h68VIWQS3I31SOrUA0yWhilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366d6a6d70.mp4?token=HgLXAM0PYff6jlhRvYQuvXEldLUSwI0MA7-P2y-hNAYDXmV_NyHDnhBE17fHZWm8_p62VN5BxQiv3tQ4IgnlC7KnEe97xgca4k43ETPPA-5ZZYipPLx9NuXoHiTSZHqPmfZDuRNKlacceoWR05wHwYQpjQE_wyHr7aygXUaY76x17t7_YMvQmnWCj3xOtf7kYwo_F2LYsgZyFQfbPKcYWQTDyUfmP6omZAsFrPNdctAI-6abQbYSDLoKdDoOzMmzlx9AQUfSqQqXeyBn31aVfhy_SqbLVWPe93yTekjk1Oa_W9UJv7VOfOpoEHsmO_h68VIWQS3I31SOrUA0yWhilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
صحبت‌های بامزه ابوطالب از کراش‌زدن خارجیا روی رامین‌رضاییان و میلاد محمدی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94382" target="_blank">📅 11:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94381">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63043e76a0.mp4?token=ScfqQQctmOkZozb33bjXYzVsyKSAMXDZ9HV079LA53i5UOOuPfdGJp7Ls-EQzWvtZcKmc5ntYQhNPU2M9DpSMsdFcBHYRnmqxxBAdcOOyjQw0G8CnUedpvn5GP-2ou87drdcgcH30Ofa5xPFHnIOh_jbyV1Eqj6RQnjNM7503sC-zCv0mKVxcv4pWQSb95pWiysGleVWp1qEfxEBOQ-Se2ILyMTNs61zQYNAgWKQHB310F3Y6gJUcoO-Cyso_vywxekFdFQPLa7loipVbOl7eWtn6xkFNm3F6_wjtOgqittmiCoxyvbvxRL9cYfVx5v7Yjt-wSiEBQk8W4TSpKnNaw0AFrpqYeBX5MwJ4Bwu1WVnH0jtoUhraqCBCacq0bCgo9pH-w_CHheVgi4X_quQYMIsFmg9a86mrclU2P3WthTMCeWIc68RL6AmXHLtY_UMvStxqDCq4Noo3S8YqMXtii2U9oxPFj4y-E3iNoOSCofL-8t-ZnZ6SOiLjxNVvZb6bKhraHeIHnq23tF42gQ7f7xL21EQQ1gygk2ScVEOu8Re_j4e1EsuI9UqZHpogvuE3oDe_dzwjgYiO01yRxfd5avTytDaWCSYC5OLcYbq6arZyRhVnkwqBgUPXdKXIYeRZEYt9f1aq_pudKNOosrtA4dTAslzeAZQnwxX11ni0Bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63043e76a0.mp4?token=ScfqQQctmOkZozb33bjXYzVsyKSAMXDZ9HV079LA53i5UOOuPfdGJp7Ls-EQzWvtZcKmc5ntYQhNPU2M9DpSMsdFcBHYRnmqxxBAdcOOyjQw0G8CnUedpvn5GP-2ou87drdcgcH30Ofa5xPFHnIOh_jbyV1Eqj6RQnjNM7503sC-zCv0mKVxcv4pWQSb95pWiysGleVWp1qEfxEBOQ-Se2ILyMTNs61zQYNAgWKQHB310F3Y6gJUcoO-Cyso_vywxekFdFQPLa7loipVbOl7eWtn6xkFNm3F6_wjtOgqittmiCoxyvbvxRL9cYfVx5v7Yjt-wSiEBQk8W4TSpKnNaw0AFrpqYeBX5MwJ4Bwu1WVnH0jtoUhraqCBCacq0bCgo9pH-w_CHheVgi4X_quQYMIsFmg9a86mrclU2P3WthTMCeWIc68RL6AmXHLtY_UMvStxqDCq4Noo3S8YqMXtii2U9oxPFj4y-E3iNoOSCofL-8t-ZnZ6SOiLjxNVvZb6bKhraHeIHnq23tF42gQ7f7xL21EQQ1gygk2ScVEOu8Re_j4e1EsuI9UqZHpogvuE3oDe_dzwjgYiO01yRxfd5avTytDaWCSYC5OLcYbq6arZyRhVnkwqBgUPXdKXIYeRZEYt9f1aq_pudKNOosrtA4dTAslzeAZQnwxX11ni0Bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇧🇷
طرفدار ایرانی و خوشکل تیم‌‌ملی برزیل که آماده بازی مقابل هائیتی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94381" target="_blank">📅 11:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94380">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58d71cab5.mp4?token=jfdEKa4RmE42TzWPyxyfKKxCB2maHaqsCNTO4I9rSD3pbcQbyUk9-YGbjsV13LrB04eWjsrijxr4XumwEEzuqBrHMThGe5xsnUkBxkCmnLT7vYA8BNuruL0M894qsf3qQppuO7tp_xehKPDPRUUX14QWcFo0LHuAK35cK-1aYv6YVFwvyWIAzf9-3auIPuKGzFEj_o0NSJAQg4yuHEIMC4gI98u8k8s4m3H3vAEQ67wfzKVATYqV8mCtkOt1wzMdJPfwZQguer-bd3NH_K88Q7QKPiVuNTEosXJRAtMuK2h4P0G0aCTr2SRx96boF_GxkKV7kGevBt7IbL3axmFJ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58d71cab5.mp4?token=jfdEKa4RmE42TzWPyxyfKKxCB2maHaqsCNTO4I9rSD3pbcQbyUk9-YGbjsV13LrB04eWjsrijxr4XumwEEzuqBrHMThGe5xsnUkBxkCmnLT7vYA8BNuruL0M894qsf3qQppuO7tp_xehKPDPRUUX14QWcFo0LHuAK35cK-1aYv6YVFwvyWIAzf9-3auIPuKGzFEj_o0NSJAQg4yuHEIMC4gI98u8k8s4m3H3vAEQ67wfzKVATYqV8mCtkOt1wzMdJPfwZQguer-bd3NH_K88Q7QKPiVuNTEosXJRAtMuK2h4P0G0aCTr2SRx96boF_GxkKV7kGevBt7IbL3axmFJ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
جشن صعود مکزیکی ها؛ پشمام از جمعیت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/94380" target="_blank">📅 10:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94378">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b08e2881e0.mp4?token=rmTiaSUrBbt6BEoJkcfz3hFYklYJ_h8jzqModPeb92dCRYTypn7DTaQ_dMwvXlQJTJn_-uJkAb28jy6PiHPU6XYTYJny-uADjPGRJf4F0_4uESAES7da1sEBvOX5CwcOX0q3T-eseyQYKKOZUc-pJrcjfygkmCPSECXpmQchuzuHezHVbfMSMl1kyZoUWlYtfiaaxPvLH4_5Y4TT68xNbPTxYHti2LQXcVcuuKj-ORe4gdKztAN_WRwMf6tGGsuCtpAnVxPiuEM-z-tCuFgE35kLZ-tl3H9SWML6dSSh6o8kEP5owK7DjecE2I9ScejFSQcURvqh5R9k81A4WghI_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b08e2881e0.mp4?token=rmTiaSUrBbt6BEoJkcfz3hFYklYJ_h8jzqModPeb92dCRYTypn7DTaQ_dMwvXlQJTJn_-uJkAb28jy6PiHPU6XYTYJny-uADjPGRJf4F0_4uESAES7da1sEBvOX5CwcOX0q3T-eseyQYKKOZUc-pJrcjfygkmCPSECXpmQchuzuHezHVbfMSMl1kyZoUWlYtfiaaxPvLH4_5Y4TT68xNbPTxYHti2LQXcVcuuKj-ORe4gdKztAN_WRwMf6tGGsuCtpAnVxPiuEM-z-tCuFgE35kLZ-tl3H9SWML6dSSh6o8kEP5owK7DjecE2I9ScejFSQcURvqh5R9k81A4WghI_jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇽
شادی هوادر مکزیکی از گلزنی به کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94378" target="_blank">📅 10:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94377">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0828ec8da.mp4?token=nliT8YL8JLsBai5ATK0pSTJtzYpPH2EH3f0Wze4hxKqo1NJt8CHDJjNdCSmMTSrZRybfbCKN9Qua-p_SJ756PtUoe7ZCSFNOVYYNwnq-pcI1hQPlGfjz_fqf6lNM6ArocKmyTDx0oUpkYEhQ57jprQIyQnyOgKEcOkPZDmX2VmHwP8NHf9DTQCFT7FNci_lnQyVqxQZkrxkaNMeq50NX27htoIt1MGG06EV0TRzyPoiehM5_Igt87gAL5zYyP0WChmkdkcdQFUF6hihe-7cZjCR2qZT2TkUYovA5jn4i58QwvMPSIiyv0Z_r6mNy26-J2yf_j3lK-Fvb3qzDXLK64A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0828ec8da.mp4?token=nliT8YL8JLsBai5ATK0pSTJtzYpPH2EH3f0Wze4hxKqo1NJt8CHDJjNdCSmMTSrZRybfbCKN9Qua-p_SJ756PtUoe7ZCSFNOVYYNwnq-pcI1hQPlGfjz_fqf6lNM6ArocKmyTDx0oUpkYEhQ57jprQIyQnyOgKEcOkPZDmX2VmHwP8NHf9DTQCFT7FNci_lnQyVqxQZkrxkaNMeq50NX27htoIt1MGG06EV0TRzyPoiehM5_Igt87gAL5zYyP0WChmkdkcdQFUF6hihe-7cZjCR2qZT2TkUYovA5jn4i58QwvMPSIiyv0Z_r6mNy26-J2yf_j3lK-Fvb3qzDXLK64A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
🇵🇹
آقای کریس‌رونالدو واقعا زشته دختران در و داف سرزمینمو ناراحت کنی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94377" target="_blank">📅 10:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94376">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7219246c5d.mp4?token=tQ4aJ7T4Osu1sPEj36ziuiISYFK9C9lrTNixwC0hFXPo0gVFVwZlCX15BSP4pbo7gCHfDcK-4HE8q6mdnafCgdMGk3uSS8O2oofAr_QwmHbJDmj1Jk9qQ7PnxPnUNJijE15oANjaDQQJ1ePdNIuAJvV5-JPJ5tz8iG6zMSBY2ASCkAiXCeyUxP6ArtfzPoHO-iE1urpAYDTApPMRkHOuCWGvaRdIxJ3Nx7u0vdwbsWZqubBW1wvqFKr1Jkw_Zvodu_yjk5xi25CP14WQEIQ1kYSDpVuiutLQZf6bu8uQgvntXrY3mwdurOx0TqwHTypQnzlC-AwH5pvB8dBIIjBpKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7219246c5d.mp4?token=tQ4aJ7T4Osu1sPEj36ziuiISYFK9C9lrTNixwC0hFXPo0gVFVwZlCX15BSP4pbo7gCHfDcK-4HE8q6mdnafCgdMGk3uSS8O2oofAr_QwmHbJDmj1Jk9qQ7PnxPnUNJijE15oANjaDQQJ1ePdNIuAJvV5-JPJ5tz8iG6zMSBY2ASCkAiXCeyUxP6ArtfzPoHO-iE1urpAYDTApPMRkHOuCWGvaRdIxJ3Nx7u0vdwbsWZqubBW1wvqFKr1Jkw_Zvodu_yjk5xi25CP14WQEIQ1kYSDpVuiutLQZf6bu8uQgvntXrY3mwdurOx0TqwHTypQnzlC-AwH5pvB8dBIIjBpKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
💥
هوادار ازبک‌که روی رامین‌رضاییان کراش زده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/94376" target="_blank">📅 10:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94375">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d51aa3adb3.mp4?token=ScMcAfVeIE_xAvYYp3oW1vtaKXXCdX4yFfRFhzkg8nSwFCu7Ejcm_AZGEZOmPt-ClBJR2LIKiStROf0Lzc3niDRc4x0mbduB6ClyttWhKUjPlTtcYqP6-_GH34YopZSnPxpCBx2N1-lkkIdfS0ScLLMj87BIWs-BWtreVKt4uyHndtRPKjbmPgRJ7OYn2EpKOMUnoYDvs3KjMiPpdWvTFUBzqfZycRIXIMeBzNsdXsR8R8-iHvS5SuEdWNeXSMcqE4a0KIAJ6nfLnE1NnA4ZrAIAxrNEEWogtEs61LUSM_jG9asbFtYR4rurQ0MRfFr_dihHsiZl8OLIlHZ7VJaTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d51aa3adb3.mp4?token=ScMcAfVeIE_xAvYYp3oW1vtaKXXCdX4yFfRFhzkg8nSwFCu7Ejcm_AZGEZOmPt-ClBJR2LIKiStROf0Lzc3niDRc4x0mbduB6ClyttWhKUjPlTtcYqP6-_GH34YopZSnPxpCBx2N1-lkkIdfS0ScLLMj87BIWs-BWtreVKt4uyHndtRPKjbmPgRJ7OYn2EpKOMUnoYDvs3KjMiPpdWvTFUBzqfZycRIXIMeBzNsdXsR8R8-iHvS5SuEdWNeXSMcqE4a0KIAJ6nfLnE1NnA4ZrAIAxrNEEWogtEs61LUSM_jG9asbFtYR4rurQ0MRfFr_dihHsiZl8OLIlHZ7VJaTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
🇦🇷
همه را دیدم و مسی بهترین بود
آرزوی جالب خانمی ۱۰۴ ساله، که تک‌تک جام جهانی‌ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94375" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94374">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9353083f2.mp4?token=VW5NEQPthz9kIV2euOORjqt_KVpvITXKrqrBC1GJpVbUYQ3ebl8xw-exijd-IoyHPTHerXpZpiaHKGNcD0i47nuM9T7zf5QLy3ndmTaocQ59sYESCq_1NV7yyGZE3mPvbV5hPqucP-w4_vOU6Vtdjfww_5udYThmL33Iy2TPZV9Nv03aHuixsmEIOiwtK1JFRkTzwFeTb7kR_S0xs94SN3PA33QLdkxETdxh6BaIS4lFuacxgfuIs-_jZZ8jSzD5w_aoufLBO-RYjQ_11fsgT-D8Yy6hPiAkXJHv6BZC5Jg2HiJeO0udBLq5isN531r3lHuM5oeqvuqZWOQlYCj3RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9353083f2.mp4?token=VW5NEQPthz9kIV2euOORjqt_KVpvITXKrqrBC1GJpVbUYQ3ebl8xw-exijd-IoyHPTHerXpZpiaHKGNcD0i47nuM9T7zf5QLy3ndmTaocQ59sYESCq_1NV7yyGZE3mPvbV5hPqucP-w4_vOU6Vtdjfww_5udYThmL33Iy2TPZV9Nv03aHuixsmEIOiwtK1JFRkTzwFeTb7kR_S0xs94SN3PA33QLdkxETdxh6BaIS4lFuacxgfuIs-_jZZ8jSzD5w_aoufLBO-RYjQ_11fsgT-D8Yy6hPiAkXJHv6BZC5Jg2HiJeO0udBLq5isN531r3lHuM5oeqvuqZWOQlYCj3RoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
وقتی فوت‌موب آلارم گل میده ولی صداوسیما دو دقیقه بعدش صحنه رو پخش میکنه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94374" target="_blank">📅 09:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94373">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=Kj8jeyDJwzC5yFdimT9QaBzVh7P2O9vVfj-5A6MWmVZb73pOXP0bBpkSs5sV9UY_iT5CB7cLnHRmlNeHb-Cf9x2WMGEcp34Ud6jjugsLx4CgJM-61udiYbAJbS6D_hvwOUUehZj1A5uzkjbGPd6Yi4NkQXb4LTTPjMLNC8N9AjGWb_-3P7iToT7CCDf0FTyx3MC3YkLvZSHuiGv7TZ9yazuLA-i-nE-mVuurfwshd2il3neaUBpYs290ZgeC5YGITqnij_1M4F2RQlQEm-oLQ0I_f6sgkerakxeGvfriofCDaVai84Vjq0rrQTfUJOsoMhq5iaEAsJ4m7ZUIUywfGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=Kj8jeyDJwzC5yFdimT9QaBzVh7P2O9vVfj-5A6MWmVZb73pOXP0bBpkSs5sV9UY_iT5CB7cLnHRmlNeHb-Cf9x2WMGEcp34Ud6jjugsLx4CgJM-61udiYbAJbS6D_hvwOUUehZj1A5uzkjbGPd6Yi4NkQXb4LTTPjMLNC8N9AjGWb_-3P7iToT7CCDf0FTyx3MC3YkLvZSHuiGv7TZ9yazuLA-i-nE-mVuurfwshd2il3neaUBpYs290ZgeC5YGITqnij_1M4F2RQlQEm-oLQ0I_f6sgkerakxeGvfriofCDaVai84Vjq0rrQTfUJOsoMhq5iaEAsJ4m7ZUIUywfGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇳🇴
پارلمان نروژ تو جلسه دیروزش بابت برد کشورشون در جام‌جهانی اینجوری جشن گرفتن. خداوکیلی کشورو میبینی ارضا میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94373" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94372">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=raEsuY-OAHxOdFciLL92DCKha-2CsK06_TKy99EIN5yBhGYBCME_FkW6S0Ba-_jYqIquWp5cnA4P3psLqMZvWwG6CcQYLGBRxPdapMKjs3KuFFqocVL_ykKMtzvFMKZWqKFpjLVna_jQESZIY9gpBDLYaVIr_9GTU3LHELSD8tjy4zr8O8demQ_zD-srzdHxm1N3xLiEQDaf_mQGz4-uEYvQDCnaDOQvP4szz1wd8AsBfrwygsbi0Vi68oLnzrOn454yK7IUS11_UKTVRgd7f3xXBrRMnudTkJ_G9ZuxzF8SvzuAmY0nJWY0OpvnUw46vrSdc8GO__WuZ7sDWNuROg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=raEsuY-OAHxOdFciLL92DCKha-2CsK06_TKy99EIN5yBhGYBCME_FkW6S0Ba-_jYqIquWp5cnA4P3psLqMZvWwG6CcQYLGBRxPdapMKjs3KuFFqocVL_ykKMtzvFMKZWqKFpjLVna_jQESZIY9gpBDLYaVIr_9GTU3LHELSD8tjy4zr8O8demQ_zD-srzdHxm1N3xLiEQDaf_mQGz4-uEYvQDCnaDOQvP4szz1wd8AsBfrwygsbi0Vi68oLnzrOn454yK7IUS11_UKTVRgd7f3xXBrRMnudTkJ_G9ZuxzF8SvzuAmY0nJWY0OpvnUw46vrSdc8GO__WuZ7sDWNuROg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
🇫🇷
دیکتاتور امباپه تو تمرین دیروز فرانسه رفته جای دشان نشسته و عملکرد بازیکنا رو میبینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94372" target="_blank">📅 08:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94371">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN8iie3X8phX4vjlEZX9Q5BL5nyy18FBVHPvP4PV0Og0lxgU74cfVrOMIzeoXOD7vZmGzYSBrKT83yRsSc7o57NL-UGTITXgH39dF_yAN_GQvgWP0JccDHCNMxfF2r3FVH0uRrhnutT7CHc5Sddx2AznC0dbX-dJXMol7KUG5NhgDZmGIF9knztS09rdqYNASDQR8xS9NUjFuIKk0qjbXaCoLyL9jx3LR2jthVwJ2QOhp4TWFgZ1J-dK5KiT1IdqfWfIYLoSDriQytOztVN5mv4kvp-ARSaI6lbJHxsJYHFll2rU80pdd7-4BGyfMdiW31ArRyicwKVoxQTnsKyBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇦
#فووووری؛ اسماعیل کونه بازیکن کانادا بدلیل شکستگی استخوان درشت نی و نازک نی حدود ۵ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94371" target="_blank">📅 08:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94370">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94370" target="_blank">📅 08:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94369">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8Fa4uIsMvdFHymvwKToRKDqHdWAiQA-JuCUEdQCHezQ5yX6FDHhalfWGP9Zb3BXu2pmJApIvKr58SgCLCkVXbOxLzjcgKlEqEKJkRo45gCgaRQSByCkppSWmy0aA_9C9F_bVTjIQqYD5e1QkC3EKX8mlV84G_S5dkOSf-Ms6iYhFSdwMPYrzQBC892d4Kc-6Ytriz3w92yPz4V6PMDc0lZ9rGN9EpsRGxjwhladPEpIVE-4V2pWRk_fRvCVf2a35zLS-EbnFBgapUJ9eKm-D1xin8Kmw4dgTAjgV05Gc4u0AdllPs831N9K3s9rJCGB9Fs8eevp5iCijYo-qLfM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لوئیز رومو بهترین بازیکن دیدار مکزیک و کره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/94369" target="_blank">📅 06:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94368">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDqv9A7TgKiDYhZTbRLsbsQyFTOGIKdCWNuLZvWHgRJTDT4xKDowAmhfn0SOyy-6yFkSSbx1oPgGTRQs9eG05xUuVYZcmDydV4ZkrsaNLcUWhM8IZ9Xmy6eekJIDubDW2ZgHebTE9joxFB_Yo8SRYiLiBVlbsc__J7f0WY8xnxG9V4S_CUxwxci8UBF8y0LROSPlE9dC01IC1eeokhpNtgLO4th4w8tq6Zyx87dgKDNs0BvVuzaoPj3eBf1BcTZa1O3cyvKEtN0j2ytY11MREg94b8S9Ppsa7FTk2wxr8KIbuC_bFpYDxmT8GujaUqjherfkIc3Y3a3O5ONB5lQ-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه A جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/94368" target="_blank">📅 06:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94367">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anZ4pNjC2332lKmAeLXQ14R5SsxSrsv-pjjXmgQ6rW6O9PX-KoWlDPfRWEaP7Be4HUBq7XPQMpgbZvIesh56btuQQuby2Xm5-EFHlKpkEZTm3XqbQPtCTvbpjk909lrLkxWZ2_wBbDDjfxbhi9taqyh1lCh-1qYyknUFJnh3nGhvuRrE76AGJvlivtT-NyLM03pH7hvmyJIjnCD612PI59EB455p9Wf5bSfyDASWZoPjdo8IAhd_5K1nLc2eItYQD2ERfVngfZCw0fbIxbk64QEZ9v_sOPLyiCxFNp4VwZeQIswNywy-A4cQ1qDnL9SCzcLYl_q9OXPUMIqwoz7n9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/94367" target="_blank">📅 06:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94366">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10d309995.mp4?token=FnuUhDvSw7yIsDOV-TUoxzUB3tqm-bk0E7TfOsJkum3tjTM5S22mS-xnxI0iZ2N2EL0V3_OD7dcsz9FlfMQlIPNDGzesugVNOJ54fPATYXqdirZBG07lbXiohmLuziPW98767k6oe4nwRzoCB0FkCyIshEomb6FFSpAKzR8pOz-OJOq5rrkEspsyG0vxCMPRcwM1LcFktfjAuq6q0ZTnWLb88b72aBMAdPvtBXYc5v5IGOg-3-w-A2UFbvs26XW-KW7BbnisXt3tZgoHSuUlFHGR93bYtcuyvrcNEyCJlYkxIQmU2o2vx7ANcAANBD8U7a92Q-egDLjput2MQZmFQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10d309995.mp4?token=FnuUhDvSw7yIsDOV-TUoxzUB3tqm-bk0E7TfOsJkum3tjTM5S22mS-xnxI0iZ2N2EL0V3_OD7dcsz9FlfMQlIPNDGzesugVNOJ54fPATYXqdirZBG07lbXiohmLuziPW98767k6oe4nwRzoCB0FkCyIshEomb6FFSpAKzR8pOz-OJOq5rrkEspsyG0vxCMPRcwM1LcFktfjAuq6q0ZTnWLb88b72aBMAdPvtBXYc5v5IGOg-3-w-A2UFbvs26XW-KW7BbnisXt3tZgoHSuUlFHGR93bYtcuyvrcNEyCJlYkxIQmU2o2vx7ANcAANBD8U7a92Q-egDLjput2MQZmFQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل مکزیک به کره‌جنوبی توسط لوئیس رومو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94366" target="_blank">📅 05:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94364">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گلر کره رو
😂
😂
😂</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94364" target="_blank">📅 05:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94363">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مکزیک زد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/94363" target="_blank">📅 05:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94362">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/94362" target="_blank">📅 05:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94360">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bfe_MWn7hFCGlO42TFjtr0OgACo1XYtQWid7FGAtOhJkMNcclvNqV5teFAxDVbCldzR_g7ogqSCmspBpFBaHsO3iLvaavkX-0G8iqdHuLBC2FjSWHaKZ2I4UubQNdJH4zsDqwzsFBAQT5J58tBakPJ0x6pSYVZhRTcZTxa2njzvY97pUona-qa6h1lz1KB93UFDQ_NEqApy1bGYxVeoLp1S5e8SFNjHc405TTuX6kbz1wg949JOOdg3Kvam8HDlWvGXsdYmNzKXoeMMBbPkZN2w1oyKaRgB6xPHAmGviZeC8oomXLAAVcPM4DFx4QHiCmjijQhmxBdhGegbfKjdguQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NuH-TqTGYaqSm_R5bR_1As7m6N_f-D_GYvJZzJgERnPkMj9L45g5EUy_Z0LXIO9-lXQpzYwbVais7qXPTvOWRQUrirW-UyU6xVctzYwDgvsNMsymwLxP0hF524yBB2VPXjV4YPiRyDDI1qidvTPmFdGozsyYhwSHBcstwsbE2rxwRAiyrfpDuxuIzLHm6Ulpoep8Eh8FJui8dI4NPS8FbmPSV4U9MfbdKHlOsa4p8L0rVOhIDWlB4FHQDhy6L-zq_1XRz3rz6cJ6NuY5W8J-ZVFCHbcmUP1AAGafYFk234T2KlWqTfQLYoQ1kMYAROqGXjNPcCol5G_QOxEcp9im9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لاشی داری به کجا نگاه میکنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/94360" target="_blank">📅 05:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg_k_dRYgL4ui5OnRiOOrdt9OtzPm7yJQvqltGgOoYTVxbicqw3RsQM5UabcjWVrrg5YP84c05nKPkuJFSA72MEeaMUeWhf9g03G0ptXJ8tCzOXF38pWheG5JpXy1QkouyDQl4j5aZwAXor381M_jDqbNUd3vwW17ndXS4MtWXKpFrj53WYefyTYn-jUeMZiNQUMmsf7SN621ryi7c-lrgmJ7xK5iQK78JRVakmPcI7eCgsrnF0A7eziYY6fq2383fI3tO_vxic0vAPiu4UVxjGeNsX6vvo7ZMYtGwydv69VTMXV8L10WGOkytjVKuqNoV5tEZwKqpMii5gg0gRnUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کوچولو تنها کسیه که میتونه بگه از نوزادی طرفدار تیفوسی مکزیک بودم
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/94359" target="_blank">📅 05:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94358">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پایان نیمه اول
🇰🇷
کره‌جنوبی 0 -
🇲🇽
مکزیک 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94358" target="_blank">📅 05:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94357">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عجب بازی ای شدههههه</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94357" target="_blank">📅 04:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94356">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe5f007bb.mp4?token=Mw0XvUKoR8aAzT7vUvG2fxSzZdY-j4LSZXFoaShjfayS_ok6SWIh1G1zQ_XxUBi16F-6qLuwS8xQCggeJZwIaDRGdkVwxdDPGDgnqnGHJJrmdA78n_Gbcy0EeNPIEl5wFWvhKBwSox3mtl2xM0jTRf-C1R9CCSBBjZ6E9aOEcJ7uneijsKqZhh0DIQazUFwyS9oQETtb_lp95MGbSXfraBnYvaj5IOjdjGnEInWVfNoh0yFP2S9NHVrRJPXaZg9yi3EQ5F89BXmKjgiSLK2ojGv79xWiviTU9BnJfPvk799bJML-qLZ2ZCm_eGIkz--KSCij64nPzLvB4QIEzAAr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe5f007bb.mp4?token=Mw0XvUKoR8aAzT7vUvG2fxSzZdY-j4LSZXFoaShjfayS_ok6SWIh1G1zQ_XxUBi16F-6qLuwS8xQCggeJZwIaDRGdkVwxdDPGDgnqnGHJJrmdA78n_Gbcy0EeNPIEl5wFWvhKBwSox3mtl2xM0jTRf-C1R9CCSBBjZ6E9aOEcJ7uneijsKqZhh0DIQazUFwyS9oQETtb_lp95MGbSXfraBnYvaj5IOjdjGnEInWVfNoh0yFP2S9NHVrRJPXaZg9yi3EQ5F89BXmKjgiSLK2ojGv79xWiviTU9BnJfPvk799bJML-qLZ2ZCm_eGIkz--KSCij64nPzLvB4QIEzAAr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمامممم دفاع مکزیک عجب توپیو در آورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/94356" target="_blank">📅 04:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94355">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_7wlaG_6wpvjJjOO4sMBm5bG-icELz3w0sVuIbyTCGD8zoTHMDdhELZaFVryWyj4zxgc5KZwt4W_lWQU_gl3m_Smg2HBHQGJQG9nhJyN3xZtWfS8yHQMfxzPilOKj3_Cqs7AASDl2MtTCPuGJyO7sUaH57GTiRin78U-T1XCoFhgXF0XizbkIceQLe3Un0qC6qiGEf3RLM3oPLm7cPL2VCLOFsOyZU2pjdil9go2ZeX4GgY1gzZ3B0r4f1pDwu633oWcJh1ggs79o7HX-4r6BJhJ7FegH5F5R0Uw_edi37l35kkqZK_NeZn4IvCfQSy0HDBr5JTTZReJPpsGh3NWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ تنبیه و مجازات قطری‌ها توسط میزبان در شب تلخ مصدومیت بازیکن کانادا
🇨🇦
کانادا
😃
😏
قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94355" target="_blank">📅 04:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94354">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466d0061e2.mp4?token=I8J7pumC6oaZEOs2PBXiRazTL9lDGL6SCOx7aMe2pfQClaJcGI3mqtlcnM7vXlo6RpV2Te86yQb8PYxNU6rDSSh6WkULvprMHDnZjf537VURCB4cjMP65Aj3kZ6nZEiEg4ec3URR-_yh-rSGhc_7JHzcN-khKuZlI0Mo9FQ_p8dNnDQz5rvGfMfL-LOq1vFsNdVlF5cRnY4ddPaJir0qLI2pOZ1xl7f3BnInTXxVTFgHwf3LeQODtmha3fCWaVvlXrTwNOmqSHqfLCQgWbzNm6ileodtAEUrM-SS_1gjGWQ4G7sbYwcA0LiGnxLIfaHRZOBdDWOYCHEdutR4CdjiKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466d0061e2.mp4?token=I8J7pumC6oaZEOs2PBXiRazTL9lDGL6SCOx7aMe2pfQClaJcGI3mqtlcnM7vXlo6RpV2Te86yQb8PYxNU6rDSSh6WkULvprMHDnZjf537VURCB4cjMP65Aj3kZ6nZEiEg4ec3URR-_yh-rSGhc_7JHzcN-khKuZlI0Mo9FQ_p8dNnDQz5rvGfMfL-LOq1vFsNdVlF5cRnY4ddPaJir0qLI2pOZ1xl7f3BnInTXxVTFgHwf3LeQODtmha3fCWaVvlXrTwNOmqSHqfLCQgWbzNm6ileodtAEUrM-SS_1gjGWQ4G7sbYwcA0LiGnxLIfaHRZOBdDWOYCHEdutR4CdjiKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⭐
هدیه جالب یولیان ناگلزمن سرمربی آلمان به هارتموت شرزر ۸۸ ساله، خبرنگاری که هفدهمین جام جهانی خود را پشت سر می‌گذارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94354" target="_blank">📅 04:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94353">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بریم برا شروع بازی مکزیک - کره‌جنوبی</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94353" target="_blank">📅 04:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94350">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJuFXXdpLLMmZf0fS-w8teLxgpKNdAX_pmRrudgLFYlUBAJBq4AGazZWDdP1ZCGwyakqCLi63Dqwupj9Ok2FsN2BtZlJAwPQqM0ZLZ9EqGeuktxTBAtpUH6-JKlXHkWmuvcDvpkSByd-vIy3zK0-ZeXvzK2DiI64pt_KPpXntj6GmdrpcSjVwEmNZ2kjrttaW1NYGJtupbb22OhYsVRntoaCIKwl-ejvstK-5a-3buiACCUZjHv08a5CzZ7vStJT6lziAa8AFNnOVjichG2BxPmE3aGRFgNZhXzqLsiDFxZIKfkZdFt8mkGutaa1VJCMaZlt-dWWRKItNqPmymOHNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCGTkUv7FxUxrnLQ6IqVtGqqEeaZn4Jy3lxcRPjj_INxHgQeCrSw85PUUS0onrOLO0ivZvuRqX0-zmNNvHbOgkd4J67rpUIN4ODxWjMo4mx_8QIugLbeeZi8NSbo1s30lsrw7bYsPfVqSF16dnfZ2-Au7NlPOY4tUoq9SBb0e_VukGQmX_A8yMalDsW9FVBXlH9WvLhgjeZAS0RuZSLxl0XHqT6cUvyBvIu4pyT_lfsvT6Wai93YT7BLjFEWVXmGIou_qa0AzTWHRhERzmN8qJMumSPFnhJrw8gaSTlr8SJ__zDYBwJ_LT6BcMU2ANM6D6NWKT7wIPZRoXf6pcNzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWoDWQaT4MFrHM_UmPmWJ3893d-kzoSeqWFoquwnyq46-j8d4ESNzBbVX_VElz7-hSg-Bmo8wLaF2pt3NJiw2UYhuTRRTEAF7Iv5WJbLTRwwEWMWybtH4pCGxgnhG2t8udg8sHiHnrpW8GNHL6kjOa7oqh460jEUWHcW83ylbuAqaUVuGaZ1WJMpYCbnkEB-C63iCwXNxWKC8iBKSkmxpIrsHCXXC4TH2rxpLgNgCPBP5dGNEMO9PSdcwPIy7inPDy9FhZ03V_mpTa91KFuafQlYRZJnw4A_kfSixZMbDiqxqTnk-K6viJ34iSLvdfqjISB1C_N51FDn8NIA2WXn2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قهرمان دو دوره متوالی جام ملت های آسیا مقابل کانادا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94350" target="_blank">📅 04:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94349">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c256eff540.mp4?token=nc7AvhimX8aNS6XFsECbZJ6NMZkytRWtHO3vEIhSVFkoCw9ZwnFVQxBm0gt2jJ_FkH1On9E61Hf890zozIgf2nFw3d5unBrGVI2b13qEAFrpAOv9LKls8g1HvHt6pE99Nc0_TtvwIh5btkbrj9miVV6khdECK9k_OrKhW906PDosOy9pWzJcnB1gc-i16QE8yBRUJExW5_GprvtEpfMTxHmqtuK-cWWT_gvKGg1KWSfUQC6aAzsiyvNY9ocD2_TqGmE7-q3GHYYcbqALG_thB546FD-7JkJCH7wXWBfi3fRNkER6BBxBneLA5zJCuJjGvPtGUhi89I6WkiNiAGLFPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c256eff540.mp4?token=nc7AvhimX8aNS6XFsECbZJ6NMZkytRWtHO3vEIhSVFkoCw9ZwnFVQxBm0gt2jJ_FkH1On9E61Hf890zozIgf2nFw3d5unBrGVI2b13qEAFrpAOv9LKls8g1HvHt6pE99Nc0_TtvwIh5btkbrj9miVV6khdECK9k_OrKhW906PDosOy9pWzJcnB1gc-i16QE8yBRUJExW5_GprvtEpfMTxHmqtuK-cWWT_gvKGg1KWSfUQC6aAzsiyvNY9ocD2_TqGmE7-q3GHYYcbqALG_thB546FD-7JkJCH7wXWBfi3fRNkER6BBxBneLA5zJCuJjGvPtGUhi89I6WkiNiAGLFPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇲🇦
بارندگی شدید در شهر بوستون قبل بازی فردا مراکش و اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/94349" target="_blank">📅 04:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94348">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVz0huowlV8a_XBmONlrHjouu9Ik792IbNtPBb0xHLJBGRxfF5t6o5gobfcnkpWxIvmC0Ua6EcjqNLC1yInvbi_bBHAX3SaitwTR7vv8YgDOfqTEiD4cFMXwQ__H9eGpLCnFMJXyAY3UQV8fbIX0Hdyv6y5otiEB44BPYkIZFrJ0eCahrwOlvpicDRAErAzNOMm2ufgjeK7KplsYvy3z7nM7aOpb_B77U0iss0ijrYDaGlS2_SXgmASRjayG1YZBFz_OQ3EboajCHtdLgnU7q417NYAa4wnZX6R5owUZWer05XnOyfRBsyIamD6dQaugLCK2o8D4Q0RuUUGwoP0uzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جاناتان دیوید به عنوان بهترین بازیکن دیدار قطر و کانادا انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94348" target="_blank">📅 04:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94347">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h69UDBn2Vl57V8ZocVXcPA8X-Uid376RG5z6QjIs6cj8wxhKhS5YJLqnWdg1JV6SyLfD6ZntoI5ogvSxMRVgTNW0ioOvJ4fw7C3vWYwVA2nHSHi6GiC0rzC_cNE5Y8Yc46ZzvKqF3u-l37sRcX9ntHl__u_SXR8pu8Gfed7WkfJAAtZSCzGipAEsZQPYZ4N9MhPD06kNJhEf5_sz4lQHwp6YC0rvLlzUjEHCHls8aq85DD-UUiGMCve-S-bQOmFpmOi2jxrHbJyAnEUsl6W4H_Qw7-Y2Zndr-dhgwtFLoyWvjjCXa8Li56rA-CGhpoFg3mLous1bqYXrp3jEZoJQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
کانادا درحالیکه در جام‌های جهانی قبلی موفق به کسب هیچ امتیازی نشده بود در این جام‌جهانی تونسته 4 امتیاز کسب کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/94347" target="_blank">📅 04:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94346">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d24c944.mp4?token=tgTCpZrZxqIshjBCyPXCf4gGJRoMEQSk9Nss8V4-JeWxcyKgRRaWfCyMSNHHqWTJ-PdsQkIvUL3sxpAaWa6r6HE7Rvvrin3PUQ4uz1PSZl9_YxKP3HCN2K5q74vHe6ZiW8x-MUYUyTwX0g1BWiFXzuM1Yd9pd43tfG4oPThMZn0iG40ZZTBSe9HYvS-gII_SN9Ifg73WuQcucHwdzVFnchqR1X2vAP1-IRGQcaUWJ-XyxmpuJkNXLXuPwBpJV_-ivhyZP_Mac1kw_z25uzSj_uXH68qxkFAKSy8BKg8nxO-0RYSw21z-9pjHAvRTmOavilwNs-bh3V8wLzyioE4YQ3lht7HEnV-oHqx0x9wF9ziTz__fuvo7YUzgdMfGOq3RTN3r8i9Mh4uvBgo7l95aYFz6leS8f7ic3niNpW7h5jgxnSN7NfatAlA-0EM6TtJhJ09ESI-OOdKMs39hZGdQtUdZvjkkXQdQP1qWzM6rWtInq6zMx46iyUxyy7b0yBluE_Af41oxH8hTcs6xGVGBJEEtAqbvvSAQyCyYK2OgQtWFFBZCyZ_EGcu0DE9P8QXvaJ5MC1Au0hGw1v3EYnphwXFw4rfLEgN9SJyqgUBp4O7QGvs4VyJuWn6269Gu_EoMY18x3cN5-CiuDYGGLpJwupuFyXGBjt-RHhwRIth6jhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d24c944.mp4?token=tgTCpZrZxqIshjBCyPXCf4gGJRoMEQSk9Nss8V4-JeWxcyKgRRaWfCyMSNHHqWTJ-PdsQkIvUL3sxpAaWa6r6HE7Rvvrin3PUQ4uz1PSZl9_YxKP3HCN2K5q74vHe6ZiW8x-MUYUyTwX0g1BWiFXzuM1Yd9pd43tfG4oPThMZn0iG40ZZTBSe9HYvS-gII_SN9Ifg73WuQcucHwdzVFnchqR1X2vAP1-IRGQcaUWJ-XyxmpuJkNXLXuPwBpJV_-ivhyZP_Mac1kw_z25uzSj_uXH68qxkFAKSy8BKg8nxO-0RYSw21z-9pjHAvRTmOavilwNs-bh3V8wLzyioE4YQ3lht7HEnV-oHqx0x9wF9ziTz__fuvo7YUzgdMfGOq3RTN3r8i9Mh4uvBgo7l95aYFz6leS8f7ic3niNpW7h5jgxnSN7NfatAlA-0EM6TtJhJ09ESI-OOdKMs39hZGdQtUdZvjkkXQdQP1qWzM6rWtInq6zMx46iyUxyy7b0yBluE_Af41oxH8hTcs6xGVGBJEEtAqbvvSAQyCyYK2OgQtWFFBZCyZ_EGcu0DE9P8QXvaJ5MC1Au0hGw1v3EYnphwXFw4rfLEgN9SJyqgUBp4O7QGvs4VyJuWn6269Gu_EoMY18x3cN5-CiuDYGGLpJwupuFyXGBjt-RHhwRIth6jhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کمم به جو سکسی هوادارای آلمان در حمایت از تیمشون کف خیابون بپردازیم. هر چی عشق و حاله برا ایناست..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94346" target="_blank">📅 03:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94345">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgMgJlNxpALJFr2MwJy9bRDqI7N4hfG9aL5kRl_1iOfedbVT2WpvXPb_Gn_6E_wTojkDdPeM-YWeso-0CVYV1X1KjzVftCXuqGJTPQ8I650KqdDWTFwBx_VJmmUfKcM2qthCPoXu3rdjj8kxdN9awWh46o9ns5b5PvxCpYGzLHjakxqiRwOqI-fCYrSLt9gK7-CSmioun7BS1lyNvTym8uoVG1BD1m4L3-XSkQnjSJV_qw2AYjob_SaCDD08d8zsWHmrpYgD7zHtwsLUnMUY8QfpVQMcc4XYh8SKny2E5N3vrOyhLWlC0FBi_z01TR6A_afN9k8ZS45SBJR-0AfAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
این جام‌جهانی برای رامین‌رضاییان از طلا بهتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94345" target="_blank">📅 03:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94344">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R25KAut3qg8tS-aX1PpfFaGQphLAPCtcn-0xu3FKYql4hZ2IbOGlnBU13x_EgnKzWqrtqs56LMHoFtrG23HODaS9T8B7qq5oYVkj4iX24ADIJUMZ0j23ttZGm2YjAjdeofmOt_5rooOLcndD8WGVfRwhmhZXBITzOCAjF59tSSsGsmXpk5dtOcsWm0Wab6MCuL1uLxD-xnFK3mR7ZBhvHyrN-3tGGzyaowTDX_vYEZI7v22KUB-U9Ln6dMduiMFVQ9qU9-i2MRI8XWcjrbQGHTJwlAJCJVw3Nf0V7evSLep_oAVsZ5MGQR1rAZppczxuOqfWS-NNAjo4VLb4p806Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه B جام‌جهانی که تقریبا باید گفت قطر و بوسنی برای صعود باید برای جایگاه سومی تلاش کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94344" target="_blank">📅 03:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94343">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6SjNap13rBGsZ6kSTrXvsLzIw_nhQudRwmSHZW2Jv-XtL1m12sog_74-4ozzxN2yws2P2Prjf2iqmJBW6vVsf6eZQz3phGg326gmBKUjJxda3JeaGNOKtDq2t8azN5eF_8EJWpjhmC2p0F9Vov_o00B4jYrk1z_e_7zEBWukObo3sFxTkpBkJUqsa9UiOhpUKJu7OcXpL4HbXpGet-bQkJJzA2932jy-zIyooSnMDtsaxaNA_88rVzF543-XxV6jtfWmZU9lDb13zXhY48uRPkpAq5-JsayG3yzdNjNCkxWGEQgzfWKh6gTVHf2IbwuE48UF8bZMeqB6ySR-09Zgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ تنبیه و مجازات قطری‌ها توسط میزبان در شب تلخ مصدومیت بازیکن کانادا
🇨🇦
کانادا
😃
😏
قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94343" target="_blank">📅 03:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94342">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=HQOAj-QSa-ZtHPXY0nBuaKA_mU7tMDeHzEEoZ-5zS58fknLAloaPR2rwlLbZhAzR6pbNbwxNkC4CyJj-QAgKG0DdyRStyZ2FcVnv28Rjp1ixxaB5W7hL1wiquttCUYfXq7shGC-fHtNQWGkORjR7tlidhA2YWX3y8IPK80eXp6NwjbTXWLtcerYmIl4Sc21oDaQrP7wi8yYqV9JEw-jNQfqZKUIl2AtYHhh_pYWATzBinNKnu3CCFCZx0hFhi8g2-tZeXh85DCT3oPhX8RSytVzM9rpDV2GQWhJTt_e83EpfuAyLmS1R-YOhXayEf1RtC6bnwNuzw2b5ePIRLQVAlAuJ-euC6VJ31tLRbJnkACzDoQ4U05bysgkwuKXdIHJJIDNb2L2VKiuy44FyGRFnXzhyANKJT0_d0PUpyZ6c5wuQMBektn5agTNdXzsqIQhbsDodK0GJJqFWh9-N2Zxkr-VNjqkuI5kqdvSyeR2icYTXrIUfVeslSU_qG_3OhIkykAWaP7yJ9xx1VW9foBglEPNeHdm0QQkNoz7fEetsn_POF3V0C91ED-dJefDGV78JQbW327bhyyPnqySJd7uSRbWGz04N2t2FUxFfgdK7atCiwDSSvCOpdHY76VPP0cooP9O8ACSXEp92rBpMjt1TnISkpPMK8jQi9xWeDH6tX6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=HQOAj-QSa-ZtHPXY0nBuaKA_mU7tMDeHzEEoZ-5zS58fknLAloaPR2rwlLbZhAzR6pbNbwxNkC4CyJj-QAgKG0DdyRStyZ2FcVnv28Rjp1ixxaB5W7hL1wiquttCUYfXq7shGC-fHtNQWGkORjR7tlidhA2YWX3y8IPK80eXp6NwjbTXWLtcerYmIl4Sc21oDaQrP7wi8yYqV9JEw-jNQfqZKUIl2AtYHhh_pYWATzBinNKnu3CCFCZx0hFhi8g2-tZeXh85DCT3oPhX8RSytVzM9rpDV2GQWhJTt_e83EpfuAyLmS1R-YOhXayEf1RtC6bnwNuzw2b5ePIRLQVAlAuJ-euC6VJ31tLRbJnkACzDoQ4U05bysgkwuKXdIHJJIDNb2L2VKiuy44FyGRFnXzhyANKJT0_d0PUpyZ6c5wuQMBektn5agTNdXzsqIQhbsDodK0GJJqFWh9-N2Zxkr-VNjqkuI5kqdvSyeR2icYTXrIUfVeslSU_qG_3OhIkykAWaP7yJ9xx1VW9foBglEPNeHdm0QQkNoz7fEetsn_POF3V0C91ED-dJefDGV78JQbW327bhyyPnqySJd7uSRbWGz04N2t2FUxFfgdK7atCiwDSSvCOpdHY76VPP0cooP9O8ACSXEp92rBpMjt1TnISkpPMK8jQi9xWeDH6tX6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇦
گل‌ششم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94342" target="_blank">📅 03:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94341">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">جاناتان دیوید هتریک کردددددد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/94341" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94340">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گلگلگلگگلگلگل ششممممممم</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/94340" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
