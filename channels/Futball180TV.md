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
<img src="https://cdn5.telesco.pe/file/Fd4sep041-ilQNu3R6IIKNWK40mdLlzA8aN0zC60LGxl3lgi8uJIfh5qDA8HpLoiWCjtbijxMsXJLbUZ89p_kP1yeMkKv4p5nxmSJJLyx0USWAyFIHdbnhVH-Es1Wf4CKCb7LHy2j89fOrrpvUtLI2qf2ypzdNgHfQe0CSwhzay6FGXGz2lovEnbhkeXLYP9z1VCROc7dPLmRPB9HlWo-ak1dfipvW-QY5KK6Fd6hndKQmkxKep_KlEmwnuK8a03ohqY-0LZyEPXxr560xX3o5feJo1trd0x-_Ip0CGo0kyB4Jx0kmhw0pU71sga17_ebxUqwysDbBWC6MJ9-Nl5eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 476K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 00:05:28</div>
<hr>

<div class="tg-post" id="msg-103406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swUFrPWEox8Bai0gsxNeNMjqZbYT-PDsz46tZnFjx1GWMPJo1voBk01rH4i-BOPPZIZEtlT4Y9pEiQJxNeow87MgNpASaNaz1YgQvneQlWvbzXKlt7hzl0TGDul4ridmnlbakjyuFjLRnCKkjGRk_jsSHyte4ScYlNjD-BYhFEfTZoB2npoBGlWCnfXFL5yvQGYfh4P6muGOFdgY2V0n6NrRfMkQac04oXd3odCncwIjCFWCheICg1jLmEWKewxmCzopcBuhiVOXGDLzWFY8UnHk82nmuJrn0EOo9PiGpcFC6YxycV618WNE1E3n9sA3kIbELMc5CTbgse20R3wUWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
کسری‌طاهری بازیکن نساجی با عقد قراردادی به تیم‌فوتبال سپاهان اصفهان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/103406" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103405">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkfCBra3R6l4GPKGYHh9X4MB5jzk8YscQnOnc2pvv8hPR0P32ygdqKbRZqggO_AN4LYt4Xt0jIiom8fA2y7XQwsh0hPWVOWyQEqmxXGZBGP5hIGb989zgrs5KJ3FIU-8gY1kuqtRrNI54XQPxLiioeU8LPM6fW1BhTO7R5JlzwxPrZL_mPvKG4GWyTTcT4IiC06_1VuulL-Sr_oL4lFFtoMN1bd6mF7YxhUtmMpDmFz_okcH4-dn4naASZW3E6S5iDGaNxn-eVzeyxfaQUjFGK9iRWKGEDxwlouaQmtJUV5XdccBSAKJRLaJLq05zGbHJQbUWsw7k280g2Zgq5fUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
ستارگانی که ‌تو لیگ آمریکا و عربستان بازی میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/103405" target="_blank">📅 23:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnQqt0q6Odg7peH-GC9AV6Wju3O_iwFinQkxw1IT5f_uvCUqKNkQafMne_Lo7cWpfFHp4HCk9MiiTynyQwAeOq_vwIVAH3eMRawQSU_gC2L0MuS0Ab5GAcB6yN_O6CvD4TrmA2vC78HQM0eNuOZ-EbHR0Bp_SloCTACWPy-hXZJ9ozsBVBpDY3_4pDKnQSmWOHCpLdW4gd3fcwYuWmdFkElJ5NIqQC7P7dYw7cwz3K2O4ACoabor6fpsNTWzMGnRKCsWJCUwcAkUWPIpXXKcQ_e9g0RrwCSWt9Lag0mGyiE7z3ISic_m55DL6-Sg9Jdp2ZZXZpthKa1y0euLny6Tkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باشگاه کورنتیانس برزیل اعلام کرد که بخاطر مشکلات مالی توان تمدید قرارداد با دیپای‌ ستاره هلندی خودش رو نداره و این بازیکن پس از دو فصل از این تیم بالاجبار جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/Futball180TV/103404" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmTQXJhuWc9HYT5t5222jzqcEHm9i3cwa4Xt5LQV_4QbumKhN8D_W6RJ5dld2WuVN8t1Qr-cV1XMXPlNz3AotblWMyHOqk-6jNxmEwwA-Lpo4Wh_71JA6asKQVz97uT-YwWxek-a_4TD2-__v1Q0hYEDiUUJAY4cgx6O1dAgrkhyufAJk-bcKl98gyksHFK1LxXHD_IpSaWoi14Yg-cRo350xOEmN9dnthrz4mTXrdjBDpJGlXRQMrDSqJnotgZI_NrYB3DZh0WdYyvR_ngaXA7sz57Sti_95MP1UD9-HBdVa6cyJ15ftkMzL2dlrs5-WZU3aMBEZfv8eX5rWoPFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
🎙
مورینیو (در مستند جدیدش) درباره اسطوره لیونل مسی:
او یک کابوس همیشگی برایم بود.
☠️
☠️
☠️
ما چه کاری می‌توانستیم انجام دهیم تا جلوی او را بگیریم؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/Futball180TV/103403" target="_blank">📅 23:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUo-T6O_HQfhtJUiUGeJh3ZDSIDt6_r51Pya6TZIYqI6fN-CL3ekyHBhyuxx-qXYIY3NboTcvi9rmhKVFyR0Inc8g8mN0GL6lI_YAnXRoXj8QewNZDB3Hwq6QZmVSB8WaYn2NktFcHYUOE6MznwdEeP24TSo-NotjdQjRZ_RUbP-BtcNZJpbUZnjbEn_2MqKzO6nenPsf7dXXEUaOU5SlVanYaPBp-B-up-PXUjmjN1Q-7R_hCLCjKfyNqFK7BXSuCtRlWk9MecwoThGZNe-Yijrq3oHeWOTrtlRZin3aBVO2rtv-RSLf6azqkV4NKr3jj-BDyB16UwKDmXZgxzU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رونالدو و جورجینا رسما زن و شوهر شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/Futball180TV/103402" target="_blank">📅 23:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu2fYgHoJqeSjP_S_Qn6CSlVoyZcJ-dZDNn_fZp-WC9zD6hxQXdwcDY9BtUycCV_pm4gnn1EzORmZqejHZuLyeZTXlRPtrlejFmwuX-S-3TjvEX_lmoUY6GxzOPotUH41_IpYog_1xTFPYpDzuTpkK1v5e_R03L7wCQiugL20I6RrasuM9wqModAt8_zack-uc3B6w8TXWwkUUJDHB_P8S5yP2Vu3NzLC6uT3oQx4mEt_2rUD__gCk4r2Gw6xPuZ0IZZa7NVoaA7vJDoVPPWmeiaSA-2WdIsuP9f5ED4qBwfrlLrLTMkbCjRKrD6f8ErAitNKPU5kBqPJw_NolhmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: چلسی برای فروش انزو فرناندز به سیتیزن‌ها رقم ۱۲۰ میلیون پوند میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103401" target="_blank">📅 21:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M93KxMN6wktTspCLvoJqivnl_F2kE1Xo2JnxLhs46fdLPtzJcEsJUm4Dp3KRm_nSJ7gJMmTmQEQhQ1dqdbULur67c-F0b65aIKuSWmThNdqOIHVoaIcxNuwvlUmW7g7qaH-dImLY3IYlQxAsUV2WsYCfzmkvIiOMUdjXQFaLE0ti0YMSqjT8ooeRA-KFeR-Q0D8PspWewHnEoH4LdDAsuFN9iHKBuEa7L_cZvVNqDlnBcZQPbY4-jpc-izbsqo8D0-1HNLJ0-VlUzFSgjOJyenG5yOuZ6Uz_oaHLjBJdjDTMi1hYsnqcKgajorrtWsvgi4RK_MAx7BkbCFOsVl8MKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
لیست ۱۶ تیم نهایی لیگ‌نخبگان آسیا؛ استقلال در سید اول و تراکتور در سید سوم قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103400" target="_blank">📅 21:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/km_KLNVY6uWoCZW77W8-YLgjPdJq92HCD0fBhcthc95mR_p25ICoB2IzQ_5MNxJQCM_vavaIxqzaiGanBqUhaJvEu6G-IVagQCUOcawzhsHduxdF_NIh9h_YiXUCzpcB-nsaPdpoaXxLHegY7sJde5sAoe0LkLzNiZbmhqjSxsgPiusFMvXgJstEePoDrd5r28E1masnJMjC0Et4MBr8QnJLOSs948Y_rMsY6yb3PeH7NROyjwKFqB5HlhSGM-zw9Nmx-g0t1NcRMJDX1SRIJ0m_pqVH4mD9ZBlmwVXGd9Er0lMH7uzRXzGwAXQsDsEV4tpq8BOHsfZIGOl_h_jZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فوووووری
از روزنامه اکیپ
:
🔻
باشگاه موناکو بدلیل مصدومیت پل پوگبا قصد دارد قرارداد خود با این بازیکن را فسخ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103399" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx_ZD5BMFtOpVNUNVWAFB74htLzfc7JfFIlnVrJq7epK9N0wKNohA4PXUZoRQc2Jm7Wq9MMKBxPT9vYaCdS2PWJdcALsHJJLMzW6CaN5-CAJ4mv05vMX3OXpTmFZ4dtZo91zNg2UU8BeX-tgksrhW6lfayvRj5_ek42u_DuEJKI1foviAZ_mHaITebdNC7ePTa0HU7gOSD286NzRcrsNKesGqm8m1tp4g1ww0XTWUBnigy6pXXbLmPniC_1g-mWKcurPrzKSw_UtNHbgSquLJJsL-9zKQ8W6ixp-VbUur2yxFdNbgpSfCckdvwwA_xx2M_MvynBjeRyPsggpWymtnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ویتینیا:
توپ طلا باید به یکی از بازیکنان پاریس برسه و انتخاب من کوارتسخلیاست،‌اما نباید بازیکنانی مثل امباپه و هری کین رو ندید بگیریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103398" target="_blank">📅 20:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNbZDwmhgBXZZUdS9eJ5IX0dQerxzddL67-mqqaVf3md_Sss1FmWPmK7x64KKMq-BtyqmXHCZkUS4poZ2zdBCCr4MX5Ibg_zIYMhykxAxuB3k6AZO9_l9j46WhfqA-1ho1rw-VeJHtvqFM9Xy9l0-mK-VNohdNzsrCvz9fkOfxjlq7uZQPoSCx47itv_IigNhS9F7wvueMJ0v4-ji5wWhCbuCyxd4FTGwJOjqx_X9vCyPlygS30oXzfYB8aOeJDQ_fDnDDMPQQSYdiKeiYcD_FhhfnmHZ4WvB3RCopCeiDQz8SopSGaXqZYxAbg_8igekD6p3TqC15cg0s9uWV2Clw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103397" target="_blank">📅 20:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103396">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5xBB-Pu6evBA4Y5K5UhvEDpW08jhECEbiB69uwuON5KTfpVlfanPckTw3LcivWOPi743xs83Q4iX7T90xUuaYocsTmuoxk9Mle5svAAYYP-CAs5IXAW7BwssaNDa6Mt_PbCz4T_6peRpFOUtfxW1UMQEUCA00v4yJv6-28U_wE2nOHqZ3TdcWiOLXloehvhR20s2cQsTWAmznZVdlmgNuZESEbkPMqEDKvwNYyUCUJxIvcBqf5xcTaeFnr3Zryi-2isO60AtUvnWaaO0uHD8eXU99cXsIk-8SRQ6--Fa7GNz-bk16Lmk_FRF3Qb6ze3yq4P2MhTs3ruPHK1DB4b8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚽️
باشگاه پاختاکور ازبکستان با برتری مقابل الحسین اردن راهی مرحله گروهی لیگ‌نخبگان آسیا شد. مرتضی پورعلی‌گنجی در این مسابقه برای پاختاکور حضور نداشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/103396" target="_blank">📅 20:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG8Q1o3f5arS_SYSqpyMkwvtrR2dJZkuSX8FOPMpHzkrsygDOl8W5bP4qduAOoVvuC1y1QoDu4gPmTNpGcVq3krBMsTXiZbWVNOLkqQXX9cLGy2VUaZk7o3XqkFI56GNB7dJiigMz2NG36qAGJrt0eTNHXkH8BWa8bH8r2Qm8ijEmHZnD1b9z8FkohU-Sm9rwhziMaDmsxOqVoWLBAeL1v-lcenoZYvtYljPnLjsbZqYpC3XQOQO19o-DWiiLbIb2cmipa4Wrlhmge0ISgcFoZCtAB3P_3HKDT_-hevzUctPSQ2ZLh080AJc202QEqHBGqAoK4-NI3tWryOgVGnjQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبتای جالب مورینیو دربارهٔ کاسیاس در مستند جدیدش که از نتفلیکس پخش شده:
"اولین سه باری که با ایکر، کاپیتان تیم، صحبت کردم، اولین چیزی که بهم گفت این بود: «اومدم درخواست کنم به بازیکن‌های تیم ملی تعطیلات بیشتری بدید.»"
"دومین بار که باهام صحبت کرد ازم خواست تمرینات رو یک ساعت عقب بندازم، چون ساعتی که من می‌خواستم تمرین کنیم، توی مادرید ترافیک زیادی بود."
"سومین باری که با هم صحبت کردیم، بهم گفت: «ما نمی‌خوایم به هتل بریم. ترجیح می‌دیم روز بازی همدیگه رو ببینیم و مستقیم بریم ورزشگاه و بازی کنیم.»"
"خیلی زود متوجه شدم که حسابی لوس و نازپرورده شده بودن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/103395" target="_blank">📅 20:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3eRJM_8L1Rp88KxSXGcCSHlYr0I82zP3tC3VLlu3RuqXCTo0SnxmsN-DRADtjE3nm84cPUPWtnK4X-dQGoQaSDP_5L5zwBJAl80wRFWx6McyAq-kNMfJe-sxk8zN1hCBLbHFdoj5Hzzs982nCNxUUNECVKaSNy5mIXMwjFwYzqKVecn4Dw80_FRyFVYiJwCtrFODEQSBXLkWjZr-nNmx4ey1oV5bJw4-3i4HQr3Ou80Fm_bFrV2WaITnVBzY_VN_PEJnVj2L7qWRbtJcq7Kyk-BHl0-_hUoJUuwNlMeOIZhVagtp7P7IONuQ0ahFW8RYKKGudN5zI97ZcoPSGkIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار خط حمله اصلی رئال مادرید در فصل گذشته:
🔺
وینیسیوس جونیور: ۵۳ بازی، ۲۲ گل و ۱۴ پاس گل.
🔺
کیلیان امباپه: ۴۴ بازی، ۴۲ گل و ۷ پاس گل.
🔺
یان دیومانده: ۳۶ بازی، ۱۳ گل و ۱۰ پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103394" target="_blank">📅 20:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PrlVx7ejCrgxFu61ssdFGN-eGB3BrYwjB2j7wLnRS45s7NT6kFw6WHi6yEaTzJE-cTWiVwFSucI9UN7GBbTOyV3HG8qDzz8EoJ9C-GAzNP-W6qaGOncPmNdcPOT4BjM8sySYSZafX2H5N9P0q5J1rWUgFkJJnfDdUMJaet_LIQ9qydXNWwYlHvPMPFQlMfaJOfcF9Rj-gtsBZiG-elgFkBlF2FNV8bcaaLTxwBpuuzqBMM8BsULbEcdXE3X1Zj1oxflhlntWqENYCKKKHkdey1M8sSK6m_-TGzpfKFlFGLQy_oDzaMe3jbsGzH9hEKy-E8robyZEFeQAyYsR59f8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jJsnhAZGEqmF9BG-QVAkewsSKZsnFPx37TnRld-NNnYWaHpFE6jp4Me-kaihn3TUlUd_Off7u3IZPA7hqjExkzW4b956apLfG2LImwOjJlL_X_9hzXuMAbTYS9Wr8wIbOePAPpL_ShYhyko5KrJXRgZMvG-QZZC3eIHWstus-M78E9DdglZLwuctXlLULUb9GQwmhAxkTu0lkaw7rFv4i5bLZH5UUTXQDBlq51Kt02zhiG6-9kmLIUi1vEFO9c9C8j9Xjil1y5rfte-Oj93bZMoMhhKXivdrAlpA7K22vc-Ue2dAT8z659_Ijgv2A4MY9hKjEDGtTU5zzps9n9kbxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👟
تبلیغ موزی پدری برای آدیداس
🍌
♥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103392" target="_blank">📅 19:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPN_UYa0vO9YtK6kkOSmctg-js2sc5GHFdOWHd0DoqVoIPAXPaKXiGXlmkFRvx07-HrADk979ksEJNvHbZao3gjkz_X9Gm5NgEBK-0JoqS9ZJp1QDLNJJlUi4fqgljmyaJOo61E2DzY5jcTdwkQymBi2vGdRh2cbJkcA3znMOlCrA1xW-XKSpCuagq84ulZ4z5MfMCuXA0omVUDu56nYMLVtxhlY684OxrJYVkk-dL17IwggT5qT35RuBees866UV5YNBFe2qW1wSGw0dWnnCzLYQPiHbe-w6O_8IVK1s8fc5MpFdRynYo_DG-MSJyPYheXTWUZdinSe4jsAJjQErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوست دختر جدید گارناچو؛ خارج از زمین فوتبال اوضاع واسه گارناچو خوب پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103391" target="_blank">📅 19:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=Zr9b3-rLVwXwbIraAs9V0QvBT6vMx4rWO7yjSTMYGG-I_reuNbhM_NVqxSAFeMaxdGxVOJOxtJSTRrZERVxi6mKjONdGHU8jCMBC08Vl8HVVWywvoRUnYZJX7ZiHvBUIDYmKvlqrpZbodYNIockaOBQw0N0M7AM2w0b_x1l3qiLEwzZrTH07iXDF-QkLHnEG-qrtabWCZ6iASm1bf4snWIwO2jkttttduI8_n_4llkXDhfhnxDQ0KrGS7YLiq1PYt91J2RKQVi-ATB0nzZH5xp-c_BZTOTOKA6PUQ1zz77qs4j02scs7KpVi09uOGmQfrC92sKoBkCh6r9mHg7ui8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf2ed3bb71.mp4?token=Zr9b3-rLVwXwbIraAs9V0QvBT6vMx4rWO7yjSTMYGG-I_reuNbhM_NVqxSAFeMaxdGxVOJOxtJSTRrZERVxi6mKjONdGHU8jCMBC08Vl8HVVWywvoRUnYZJX7ZiHvBUIDYmKvlqrpZbodYNIockaOBQw0N0M7AM2w0b_x1l3qiLEwzZrTH07iXDF-QkLHnEG-qrtabWCZ6iASm1bf4snWIwO2jkttttduI8_n_4llkXDhfhnxDQ0KrGS7YLiq1PYt91J2RKQVi-ATB0nzZH5xp-c_BZTOTOKA6PUQ1zz77qs4j02scs7KpVi09uOGmQfrC92sKoBkCh6r9mHg7ui8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
کالوین فیلیپس هافبک دفاعی سیتیزن‌ها با قرارداد قرضی یک ساله به شفیلدیونایتد پیوست
منچسترسیتی در سال 2022 برای جذب فیلیپس 50 میلیون یورو هزینه کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/103390" target="_blank">📅 19:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYGT89NqmJOXEgfs5zb4SEfEhVVLl-l9J5dBf922vWvJFVg3ttCVXUIFqClvTMFNZCkMYGwdWIyZZ9tIiwWfQueJLR4nEn2oBwrT0vGu0TMDFgK-RIHlOAqUl6xz9-TUiGriJ_T8u9lWEDp2CKF1Jw-yCE_2Y6u4jWmI0Py5d1MX970OzkwuZn1tOcLb_gjS96pdSHtdQuDXS8E9qjsWjuwokOuXYVdBQG0Qfu9vnakyrjph0GskpjceFuzjQDRSB0jVbyMP-0R6icJyw5TiB3qT47oGAc4d1-uczg2dRUeVD17HY5qVAiXPziJd3W3Nl81RRI8rtM3QZ241Dg9Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/103389" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🇦🇷
خولیان آلوارز بعد از تمرین صبح، مجددا به مقر تمرینی اتلتیکو برگشت اما این بار به همراه ایجنتش
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/103388" target="_blank">📅 19:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIyqRnuaqNfs9UJ7QIVhOqmweFeqghdRzOiuV6wuRtqJuOhAUdoxkZVlY-9wOZ23-6mFSFlceOktyFzX9xMmT1DDTCUf6pVf8z5Vlr_4oFLZF0LmNWRoxELK3s9mgdQpbC0fT3D2k9L0GmIS_7IeG0ZyLgFk1rhskQ1PsN0p4JgCoUiaKTYEX5HAvupsPa1dWGR53tIvqiAUvIpjK6lSzXCiuNITxO1O0DmQRoeeXUY3x2mPT-ipvaVGYEfYQAI6J9ReIAVoNGfczu9YbgphvZbiMyHMb9hpWBywvkTh_VXg0xA9AWxMzfjVdFkCkTH1Bn6R2rOlYGJGi3-TFfvq1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NTjiQIxKRwzesVPo8GN150nmYVohTSf6md-JUgXWXq6MoRUSqJardRf2DZ_f3zFZ1nAbLvRfnenEZh55Sh9uAQzUaS00DKDRy9--IhRMRs0x_ftmeRsH4f7Q2GGOXBgoIo_37WGRzGILhcdP6EORWDp2b7CVu8pZ_KSGe8MkYDZRz71BAUQHRZm7Syv6HZfh_Oy9x5tOvEutz5fqEF3g2enUaI91-SZyBlTUGdTmO4M2Tb1v1giaN2vGEHk4Hi83vZHMckF6WxDzSpXAg8oorarATDjOWKjYYNjBf6-Dq0EYVVjhpMzg8RIxoXnONi6HYN_gxpz3sMgq6hAoeaEU1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
امباپه و استر اکسپوزیتو در ایبیزا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/103386" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVWPAuM0R4LdMnCkG45NGcjsSzlUkK8hMraOAhHfw6f7n_E8hPMVLq5rupwoAan7Arm_gGXMr4BpQRLvjueyMEHN8XRMaZ20mkNpll6cTNu2xHkhS1gD2xfcc6X3LmyAm5UW1k9ssIjt5gu2d_d92irGopB7kpNgqoLfKwg7XNBz9YBkX3vPQiCMx7x9gA4WZiB0ysUuGbT5ZlgRUUm6jdxHr8XtzzzqjEEdcA7xOQK7Ht99_EnoWddc9IghYb9wOfg4DoPHyN2m_9HdjpcBUGsaZ8gwJBCGsg1oJogXaYYdEbZnIFbMFy1xUYU_kOjTAJFdbCnD5Z89FkxZIpl1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
واکنش روزبه سینکی به صحبتای دیشب رضاییان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/103385" target="_blank">📅 19:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103384">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIZD5bYHrQJi5JY8jjF6Ow-k5oHhmFmgvq1K90NKM_d6SnqxcK0Udt1tO04TRem4rLG2sBMiBX22OLNeQm_KQeRg2jKq4V6mZ-vl2gBfswPMnTR6sZNgFxrKthSNMBDsM1ciBPPYYTr0x9EsV6DvqTvoToPeDB3H_9-xlPu-YDFh5VFBG915UM3P2Ia_bJPqZxdCB8owzCwMNo-MFTTvHeQaodI68UVA3_f1lw18RJCoeVPfQGSFRBJXGDjZjcyyk1L91rrx6YpLWQ873wL82ac20mnLaWVeQAd1OrmWtp1X53TpeUtXW96hPIcAMobambQFiw7OZc7kD0YOAFqfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🎙
ویتینیا درباره جایزه توپ طلا:
🔺
‏
"به نظر من، طبیعی است که یک بازیکن از پاریس، مانند کوارتسخلیا بعد از فصل درخشانی که در لیگ قهرمانان اروپا داشت، یا دمبله بعد از فصل فوق‌العاده‌اش، یا فابیان که همه جام‌ها را برده است، این جایزه را ببرد. به نظر من، رقابت بین این سه بازیکن خواهد بود و من به یک بازیکن از پاریس در توپ طلا رای خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/103384" target="_blank">📅 19:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103383">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=eEVOHPjFgjtLbYoXvUkIK27Q2WzHCY72LgDTZ_e-InLiaB1TZsi8bVuoW0VyaPfykP_qTaezs0M8yBx4_2vyuY9CCykJmMU6hC-7W6nK4HhwkZPj9mSw59DvAhawhvzT0W9jxdweqQCY2pkNfQXneo7jUKL1RkFCCiJgGSeRx7ajB1xq7yim2lYYHH4N0Kcwe2uiWYTlr1JFomw8B7wDp-uY_tOkRHlXc4Y4CJB4UYa7tiXC4e1V5_rpRyOs6UKHO7EiYPrl7Vr9gD0-4VI22HpMdoxlH1M5DYLHxCvum1OtEuPK0MCW0qAuF7lR1l_7bJk3H-9ymrxY_X2oebwOY1jaOganfFnu4n5KKwe3aFyS-TS6xyi_BlrID-4zR-Oi6KRtSPwbmfVp4nJ16AsIi6HczZUgTXcPcZyOMQv8P9ndx0a8cC78VTWoy1oq42kTZmWGkDbUcuwNE21brIoNSbl8zlGwbyGzgySBgV2HKKQdtgsRG4qQKiFPQkk5O7ztnbIfediyaZNExoMAVkknavFkW6_KexIN6clJH-c8sYblEaXDU6XFipEl4KM0fhZnKe7tWYNW7I71SbTN72GBL0pRi6G_KGxC3TluSL307N-AHGyflT4tELKsay7Rv8pOlCkD06vdzqyx7Vc-0nChWlcF9nQqjErlJLNUZZxJ2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63fe3eb369.mp4?token=eEVOHPjFgjtLbYoXvUkIK27Q2WzHCY72LgDTZ_e-InLiaB1TZsi8bVuoW0VyaPfykP_qTaezs0M8yBx4_2vyuY9CCykJmMU6hC-7W6nK4HhwkZPj9mSw59DvAhawhvzT0W9jxdweqQCY2pkNfQXneo7jUKL1RkFCCiJgGSeRx7ajB1xq7yim2lYYHH4N0Kcwe2uiWYTlr1JFomw8B7wDp-uY_tOkRHlXc4Y4CJB4UYa7tiXC4e1V5_rpRyOs6UKHO7EiYPrl7Vr9gD0-4VI22HpMdoxlH1M5DYLHxCvum1OtEuPK0MCW0qAuF7lR1l_7bJk3H-9ymrxY_X2oebwOY1jaOganfFnu4n5KKwe3aFyS-TS6xyi_BlrID-4zR-Oi6KRtSPwbmfVp4nJ16AsIi6HczZUgTXcPcZyOMQv8P9ndx0a8cC78VTWoy1oq42kTZmWGkDbUcuwNE21brIoNSbl8zlGwbyGzgySBgV2HKKQdtgsRG4qQKiFPQkk5O7ztnbIfediyaZNExoMAVkknavFkW6_KexIN6clJH-c8sYblEaXDU6XFipEl4KM0fhZnKe7tWYNW7I71SbTN72GBL0pRi6G_KGxC3TluSL307N-AHGyflT4tELKsay7Rv8pOlCkD06vdzqyx7Vc-0nChWlcF9nQqjErlJLNUZZxJ2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
رختکن جدید و سکسی استادیوم نیوکمپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/103383" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103382">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=lwAR6ogj9kefnDiJ6eilirTODkdnBEXFd85LYhIgMnVaDwUwe9sOH5tsB7KSsxuvuNE2MKawzHrj6R0h0_BtYki8h3psih-6e_zzHr60MyWNY3XikBxH90xgBVEfSuyeMI_oZqPOeLIScIfn7AUNrAiT7-nzux3bPi0w4EHHFjivnZUYrDz7cZx8ixfdQ5eeGceCqAVvfdWeDP4cZiITiw26gXlG4_ZUrbHF-GnTbccZsiImj0aOn_uYIk9SRamCvtdKtob1mLp0gRpM3TcFY8esSAiQ-GdFv864AVzYYDo0DmcUasqqtHDBCEtJpoVV4-5Jv7BM96VqrnzJ7dHr-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bbef9d0be.mp4?token=lwAR6ogj9kefnDiJ6eilirTODkdnBEXFd85LYhIgMnVaDwUwe9sOH5tsB7KSsxuvuNE2MKawzHrj6R0h0_BtYki8h3psih-6e_zzHr60MyWNY3XikBxH90xgBVEfSuyeMI_oZqPOeLIScIfn7AUNrAiT7-nzux3bPi0w4EHHFjivnZUYrDz7cZx8ixfdQ5eeGceCqAVvfdWeDP4cZiITiw26gXlG4_ZUrbHF-GnTbccZsiImj0aOn_uYIk9SRamCvtdKtob1mLp0gRpM3TcFY8esSAiQ-GdFv864AVzYYDo0DmcUasqqtHDBCEtJpoVV4-5Jv7BM96VqrnzJ7dHr-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز زمینی چه کوفتیه
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103382" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103381">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/Futball180TV/103381" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103380">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCN4aTXl8Yv9IGGrIJMJQ18p4uHySyUg59twt97w0HlKTaN6NPOCwzlCEBiP9ZRC3x8FsUm2rDrfDtqW5tCZ2Q69NxOwM5usnSFWm7V3ZGExzevJ8sm06_v538fDPP-0XYQ1fIzhIUNTkv3qcKG6MAmtxC1Kxi839P06CZSlPblZx3QLIDtJ1J0R5Mxh0u4gPxGwJ3WehwChKVoq7qd9tQKTnxmvRuURuGZ9YyP1x_IAUbPIjOalc8WNL_Ie5vlRcLTnKlbSBpZHGQcRTxdn-Xv09KiQADgVjltkncSTT5qVev2GExOqpkzw4x4x4N1Y53xtcfkSY0HuaKyYngIoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/103380" target="_blank">📅 19:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103379">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9cfdabf9.mp4?token=bXC7Gwd3hX5CCHKrAcXr6JGFs_1E3H0uyjIu-R4DHIwgf2KYVZyRTRzQVxB82JojMcvQXLkm8TD_6_ot14MlPLwnjL2ogEs_NLukP_PIRsws4w4FZ9hHuSMLltLX76s7WCjtRw3tn2QVt2RIlU6HJ4kDQALF7-JBQDg7Lq7lkYgkhQlo1fA2cYRToj-P15z_z-D7OnMbaPE24ae5lnv_gOzxepVrMlRDsmIoCfatXoqoFW68x4lxDGnhPXS4KhMe8okCRlQJ5PnxSoAVLrO5OxRosAdJjnxNnAgRgbCuSRRgt270hXy9ncWnEXiuhLOMj4yzKGc3AEXMpScakNF6sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9cfdabf9.mp4?token=bXC7Gwd3hX5CCHKrAcXr6JGFs_1E3H0uyjIu-R4DHIwgf2KYVZyRTRzQVxB82JojMcvQXLkm8TD_6_ot14MlPLwnjL2ogEs_NLukP_PIRsws4w4FZ9hHuSMLltLX76s7WCjtRw3tn2QVt2RIlU6HJ4kDQALF7-JBQDg7Lq7lkYgkhQlo1fA2cYRToj-P15z_z-D7OnMbaPE24ae5lnv_gOzxepVrMlRDsmIoCfatXoqoFW68x4lxDGnhPXS4KhMe8okCRlQJ5PnxSoAVLrO5OxRosAdJjnxNnAgRgbCuSRRgt270hXy9ncWnEXiuhLOMj4yzKGc3AEXMpScakNF6sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدترین چیزی که بارساییا میتونن امسال تو چمپیونز لیگ تجربه کنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/103379" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103378">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPwUQSEWjvOaj_crCjVi9IeKQ7p6tUCGe1tV9fAW_Q5X8jj2aojlSw79mLPveJqbUyCOcNJo2du0sPEOV0mGaAU15DBpalSG0frLz21OtXrjLmu1JZvnuce6_D29iq4ZROeoc1TZB8qWCHJcD6W1d3_-gt0ZjInk_ECbaB3Ln34kgOzPR-TSb_6lCanmTLIT47CC84SoAkzF8Cy_OgkltP4kyNtcNoJYN6qG-Xx2fVyPOxTYI2jvA-Uxm07xRg4O9t1bMjuCCwchPwA5uTEoP4It4J6Ej2227CRPy2uHSmObDkN_5wm4sIaGVTNQdsWK4dg3rfRiOhjMhGoSw6uy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینی رودیگر از امباپه و وینیسیوس دریبل نمیخوره ولی میزاره گولر بهش لایی بزنه.
⚽️
@Futball180TV
| بایرام حقگو</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/103378" target="_blank">📅 18:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103377">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=hHveOCTuoCKLJR-E5Aa5faf3xagTQqYJXkFoijZ1OiCVKR4MrAFlpEgkv93ujN4ruKVrZ5JMKepAYIOU3m-73xm0H8f-NEGmts0LlZ9idv6a870Bjyx5HBA8-WHQtX_aodzTtoJDFE-KnDMgza7aBmp9bd8yugZNUHewlq3yXEWvI7sEq1JxMNz3CWKLv4zjLGMhyS-uEzCnUQNwoa1lRSGjs_vNdjSCwzxdPDfYYoGrtRwvEQpD9O6EaJIQPjztyhTuH7QOaiYbmcQ4csYlV4T56xHInKqUoZEBg0M9xvt4d6rotzwhqxYZHGpyVlkolyphgy5zwDfSi2PEyQmCNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad153bb5d9.mp4?token=hHveOCTuoCKLJR-E5Aa5faf3xagTQqYJXkFoijZ1OiCVKR4MrAFlpEgkv93ujN4ruKVrZ5JMKepAYIOU3m-73xm0H8f-NEGmts0LlZ9idv6a870Bjyx5HBA8-WHQtX_aodzTtoJDFE-KnDMgza7aBmp9bd8yugZNUHewlq3yXEWvI7sEq1JxMNz3CWKLv4zjLGMhyS-uEzCnUQNwoa1lRSGjs_vNdjSCwzxdPDfYYoGrtRwvEQpD9O6EaJIQPjztyhTuH7QOaiYbmcQ4csYlV4T56xHInKqUoZEBg0M9xvt4d6rotzwhqxYZHGpyVlkolyphgy5zwDfSi2PEyQmCNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
محتواهای فاخر صداوسیما درباره فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103377" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103376">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f850200c.mp4?token=Wwu9RCGBO_OSXSnU_cQSb7B82k7kZDRoUKB3vuDhGWmrHmgY6XYfeKWISqubcWih_76vobycykKGE_8xuaZnGkCkMQXSd_2HZ5NVhCbpIhTQqagYg1exUPYwa7_WFsWH7otcqW9nfEkHQ5adScp10WIww61Z3osH5knrUCbIoJkgAqws-kYAmbq6w8ejuzYoOZulHeFxaUa8mUp0ywUVB2lvGBayd_thWPuO5SHY4wF0GYyW-W4nvMXCWn1_0sWIthdXhscjygddKCTYQZRaU_JkyIn55lIqYgBfxcDpR36EFAvBDYWtNa6BCWMMobiR7tLnugMNb_yY5M1_MZii92VgJV6MeW_O9NWalymHZzCbsoAAWxU-IaT8m3em0-HDmpvaVQwx1INu__4wSWfGx50lDh1OLJmCGen2InrMNQz2-ffyxJktwj84a3MijOwHdrdv0rIPdcuu4-VBo_LDTmy2r1XUYLx7UuF6ZFybIWLuAu_qq5LPOCkk2TQpNSdqtc-3A3jtak_4Z5SvSBbpLsi4DXzYjGsFVID01OKzGyAonXl71SUvv9HIjZg7Bx7jAyK3PQjBZp1yyt1KRiaKP6ez6rqlwNhqmRokUaIRgLkIIKH2elAn5veLP9JY17bGjDr0IfaYm_yiq_FNo70MseDRTWWg7_PZgYh1kbcq5M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f850200c.mp4?token=Wwu9RCGBO_OSXSnU_cQSb7B82k7kZDRoUKB3vuDhGWmrHmgY6XYfeKWISqubcWih_76vobycykKGE_8xuaZnGkCkMQXSd_2HZ5NVhCbpIhTQqagYg1exUPYwa7_WFsWH7otcqW9nfEkHQ5adScp10WIww61Z3osH5knrUCbIoJkgAqws-kYAmbq6w8ejuzYoOZulHeFxaUa8mUp0ywUVB2lvGBayd_thWPuO5SHY4wF0GYyW-W4nvMXCWn1_0sWIthdXhscjygddKCTYQZRaU_JkyIn55lIqYgBfxcDpR36EFAvBDYWtNa6BCWMMobiR7tLnugMNb_yY5M1_MZii92VgJV6MeW_O9NWalymHZzCbsoAAWxU-IaT8m3em0-HDmpvaVQwx1INu__4wSWfGx50lDh1OLJmCGen2InrMNQz2-ffyxJktwj84a3MijOwHdrdv0rIPdcuu4-VBo_LDTmy2r1XUYLx7UuF6ZFybIWLuAu_qq5LPOCkk2TQpNSdqtc-3A3jtak_4Z5SvSBbpLsi4DXzYjGsFVID01OKzGyAonXl71SUvv9HIjZg7Bx7jAyK3PQjBZp1yyt1KRiaKP6ez6rqlwNhqmRokUaIRgLkIIKH2elAn5veLP9JY17bGjDr0IfaYm_yiq_FNo70MseDRTWWg7_PZgYh1kbcq5M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
مرتضی فنونی‌زاده رازی رو افشا کرد که امیر قلعه‌نویی در جلسه‌ای که با علی پروین برگزار و در تمرین پرسپولیس شرکت کرده بود، فقط یک امضا تا سرخپوش شدن فاصله داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/103376" target="_blank">📅 17:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103373">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=nnC2HKQ65I5Bxb4-NvlhXBRe7wzHbuiARMXFJJ2ptXx_EGGcYpVlEwJFeFJJTyZ0ZW2vUB9zkxckEyPcDlvScBbAgm9AErsW4h8i3O7inwX-Lfqdgs-X4P_MZvjbORtcLYURmBg62XlIxQBM8VKHndmVMtSepl-M-gZHrN1UoZitFOpAst2iqxQgXqOQ7Rw1EK99xkb5Fb8kh_ro7IlafiQ4eK252t0LhkCWr8xyyscYp7jJ9hOdf1Y6PhLJqzCFgD4DAY9U3_5N4V3vZgzlowXFdVEYkxQgEPsCI-xBU1mddDyi99BIgqWDZh7TpAFoq14qw-HiMXrWkeNRDhvnsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83944eb6b.mp4?token=nnC2HKQ65I5Bxb4-NvlhXBRe7wzHbuiARMXFJJ2ptXx_EGGcYpVlEwJFeFJJTyZ0ZW2vUB9zkxckEyPcDlvScBbAgm9AErsW4h8i3O7inwX-Lfqdgs-X4P_MZvjbORtcLYURmBg62XlIxQBM8VKHndmVMtSepl-M-gZHrN1UoZitFOpAst2iqxQgXqOQ7Rw1EK99xkb5Fb8kh_ro7IlafiQ4eK252t0LhkCWr8xyyscYp7jJ9hOdf1Y6PhLJqzCFgD4DAY9U3_5N4V3vZgzlowXFdVEYkxQgEPsCI-xBU1mddDyi99BIgqWDZh7TpAFoq14qw-HiMXrWkeNRDhvnsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبر بسیار بباید پدر پیر فلک را
تا دگر‌ مادر گیتی چو تو فرزند بزاید...
نام و یاد استاد محمود فرشچیان گرامی‌باد
🖤
برشی از صحبت‌های استاد فرشچیان در دانشگاه هاروارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/103373" target="_blank">📅 17:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103372">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUW_yyBVq_D-QMLA3gWw0wsHoQO3VdvRHQC3DHVNK15LVt11FHuQxQ8Qjm13_iE7Pf2vF2C0-qnY2YNaQVmVUg5dbBhOCx5LVQpXgkx_UB17Bg-N-TCsl_S_yr2j4QVoM2PC16rcZmxkaBIID58Mun6rjbOkAF5SdNEZoiM0LgDlC6jzcB-sWoGOMR2bNCSr290vab6wz4W-pgu_1YEm5xaQriHFJH_TQbDfbfQBZoEEfD3tsP2pAxjbge2DVtTqRvRlwONOENQL9m6tIKGuCByp-R-ZEERltdMmp52Nc-W7jHaeij1j9v1ipj603BGz1R_XslYlFN8X5aD7zdZQ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
❌
بیانیه رسمی باشگاه بارسلونا: رونی بارداگجی رباط پاره کرد و به زودی جراحی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/103372" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103371">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-eCj6SIqb2uhAET3xAWDiz9oQl3KnYd5Ie2-5YnqkF1YKGOP10g0oGeVT6IKSRyfMLieq_eDkYLsXN6l9j56uIaDEVScyQrD-Sn8OrIDkXC7P94xDXZT_ZsSik7TDlZEmT28GAmePSGNCtdt-wes843CGjzngaDF9QxOIG2k-MVG-EQzuENIq0mXgqSzy6P3yKC5nvuUXfq2diH7IX2hcpusQLjk2gYi_70S9C0uB9Gh3bQujFzyeO1YuKnm03rybUpmiRruNE4QHaPN0SRDrwyWkdiTuYwpn3OVGemP28v_X3uNNDn0HN11UxcAfwXb8nSE60zJllTBqtN4_yYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فنرباغچه همه استعدادای بگا رفته اروپا رو تو یه تیم جمع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/103371" target="_blank">📅 17:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103370">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N56nUWWQMdCYsJ-oLmyRQBNMWi8f2U1VLA4GC2FXjXVyNsXuRlrNIXx_OnrxosC6YlJCZeQ27H60ZeVKtqvf9HE2tMq0K_uNgMB46ftIuQ3-qLf9zQjSWxPVaHNc0fCVl9YzAJxa3cbsxitfwcOjRk0xjJstrPEYAGplNAJJrnol8y2i8-AnMKbKssXt0yeSikGqlF3ePBC3cZ9mS_QCF8SZD3_RFfJOyHrst8KySf-GiyWMBfi7eHCsPulSXf8TE2KC6i0d5zemHq5gjZwNn7xgXujp1QvLZEKvQHR6avP13vXaep5D3zLkUkmDrnTsK2RF82_HtZvuRCDMB_PwXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
لونین دروازه‌بان رئال مادرید بهمراه همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103370" target="_blank">📅 17:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=UolY6FxOkUG1ti7Yo1SNEdhzbIKrFxs5d8r5LmLQKCDmKO-a8z27mCdgp63tY0SgWzWrglyRsfd26b_wkZ5I8uQOCRrDFxoILm90w2Y6xfG25PfxsOo69aqBaB0wb4M72tqCkFkAFhjwQ0HLsaltOHCqcR3kInnI9t7L2a5K_42gMg9o2e808tHe7fA2JUWgwLODr5WWDQKzW-xeCZfB2nMf42OzPkdI-SW7yS3LmzgD-e-PnTGe4fS5v6mM6LME_ryhFcbNrHel9vDVLjoJwk0GR8s4miKNVfg_XqwqgYlNdJd5WSQ1a7lkKoit8404-xUpsIPc3XmWry5lxBQain-zqabYOWsLtFfL4J0JxJ773DV7LNGVYEuja1IQ1MXWPzETQvCguQT8kNRv2yfj5p9ac2HiIEDJZzID8uQY_onxjiHNDn42Sm7sY24HrJIlzxXfsHqiy864w7falz0ep7XODTy-e2FWjO-f8eqGbepbt3JmYorg38-9Tq6pTdpE4TrbM8y4WBvcxJvF8WOsynOccqe6hpN8RKwcfU249XkYJGeCoaovaYDZQPmRdszVNNoMA54n9S4AYukPLpRgMhM9Lk-Gm1_xY5dZlWhcBZa0-zlKdHk92ZbAotEktOOe6XJ-pTzIKbcM1u4PiRkk5HavHaSVWYqVz3BRY8qApb4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9fc92de2f.mp4?token=UolY6FxOkUG1ti7Yo1SNEdhzbIKrFxs5d8r5LmLQKCDmKO-a8z27mCdgp63tY0SgWzWrglyRsfd26b_wkZ5I8uQOCRrDFxoILm90w2Y6xfG25PfxsOo69aqBaB0wb4M72tqCkFkAFhjwQ0HLsaltOHCqcR3kInnI9t7L2a5K_42gMg9o2e808tHe7fA2JUWgwLODr5WWDQKzW-xeCZfB2nMf42OzPkdI-SW7yS3LmzgD-e-PnTGe4fS5v6mM6LME_ryhFcbNrHel9vDVLjoJwk0GR8s4miKNVfg_XqwqgYlNdJd5WSQ1a7lkKoit8404-xUpsIPc3XmWry5lxBQain-zqabYOWsLtFfL4J0JxJ773DV7LNGVYEuja1IQ1MXWPzETQvCguQT8kNRv2yfj5p9ac2HiIEDJZzID8uQY_onxjiHNDn42Sm7sY24HrJIlzxXfsHqiy864w7falz0ep7XODTy-e2FWjO-f8eqGbepbt3JmYorg38-9Tq6pTdpE4TrbM8y4WBvcxJvF8WOsynOccqe6hpN8RKwcfU249XkYJGeCoaovaYDZQPmRdszVNNoMA54n9S4AYukPLpRgMhM9Lk-Gm1_xY5dZlWhcBZa0-zlKdHk92ZbAotEktOOe6XJ-pTzIKbcM1u4PiRkk5HavHaSVWYqVz3BRY8qApb4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
▶️
لوئیس سوارز ورژن ترسناک و جوان آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103369" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITZFn9Clgfwkm8a-fQZSRUe0jGYErWxJ-7b-8vRLnZfnzOwxBW8RpXvzweeQsNG2KrZhB7QCwbmGkArNoqG4pLnXm_JB20qaZnVylAOREGnP3bxy47t4Uk7_MkwH8W2dKWXLI4te7rLhJLcTi8cjpExF4yu9Nhgr3qHsowMouNAS3C9epOdVlUuc1WIz8NKQVLNghmo8fz9PD-WS39lHTOzRcmwF1ALCI7ehMJlW8mCY3yUdWOkQYuyNiMZzkT2R0i2Nreqr1jx-dQ2oHTU2qRpNBBRP24OMNxySfMGOX8uUOvh9J1CXPKWJFBdLUTv4lisgSbA0E08xsvxJDsN3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
رومانو؛ باشگاه بشیکتاش، پیشنهاد نهایی خود را به دوشان ولاهوویچ ارسال کرده است تا در ساعات آینده به توافق برسند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103368" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=NAYL2TeT9KAOOyxMQIqE9s5q4kzNUt3M8lpMFb0FzWu-BhGQsoaSCI3Dg3Wh4nCn4m_h71PDAr_Y4s6b3MbU-yCbYYvC4hYPp_RDIyv-_ooUdqXSM2XPS7WhJAHtHVc-v-PTBaIY2twDjWVpjI-BJLS9-l1zioLN__LD90ChyLKVGT6H_kNb92U5wAIHJA0Lyn2XluxdH9tLftyLmwow4GohZVaIasUYMuWnkZaxvJGU84Wh-XjHaqR4sWQt4y9j78G_5IsQOLXUO87-JfsJqrsDfUUH8JaCraPx4LJUCWSnAxs0Rc55IA0XEkBTiZLYy7_0TgIeL-0pqOO_d8TY8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b011d4118.mp4?token=NAYL2TeT9KAOOyxMQIqE9s5q4kzNUt3M8lpMFb0FzWu-BhGQsoaSCI3Dg3Wh4nCn4m_h71PDAr_Y4s6b3MbU-yCbYYvC4hYPp_RDIyv-_ooUdqXSM2XPS7WhJAHtHVc-v-PTBaIY2twDjWVpjI-BJLS9-l1zioLN__LD90ChyLKVGT6H_kNb92U5wAIHJA0Lyn2XluxdH9tLftyLmwow4GohZVaIasUYMuWnkZaxvJGU84Wh-XjHaqR4sWQt4y9j78G_5IsQOLXUO87-JfsJqrsDfUUH8JaCraPx4LJUCWSnAxs0Rc55IA0XEkBTiZLYy7_0TgIeL-0pqOO_d8TY8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
پشمام؛ روایت یه وکیل از جنجالی ترین پرونده خیانتی که داشته: زنی که از انگلیس پا میشه میاد ایران برای خیانت به شوهرش....
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103367" target="_blank">📅 16:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcFayvvg1l1blujTUDRIhpSLlga98UNHTYpJbW0dRv9braaWDFooc4mOnYUn7TjeezK_I9L1ZupwWL6csDR3aM630OR5rHGhRDA9sNKByEkrCcdMqVTz8-a3fkTI5SNQ-OlCuBwsl3qoUNC5vUqAN7YyihUdCyiEi3ZrAQjRBbvMZW-U9JsNIHpXFH3xBlTJGbpmJb45o3C-qu4ZbxDF6xu7YPuE84PLxj381p8lsKxQfaVxdHZwkFPeM-2Soo7V40EhNepaBhQUo5onKE_VVt668zXFM_O_suoMJuZWpsobO5HkwXpcbI5gQajpAScaqbRxj-4altHZKE3GsDP5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
آلوارز در تمرینات اتلتیکو مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/103366" target="_blank">📅 16:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2UC70vMnGniwCw7VB79EH2eGDvLEIlVwOgrxjXZ4ZNlaLBrlCviCd_mwL9Tm3KewgmFQb0MMxkZepat3xfH98wOafBX6cGPW8xUfKB2D-KTyivp04KHCNFw9B7xBUjVaWXDJp9J7zZ5nJ4yewQA3z_hNQbs-fucNvzCZWSUlz5iZahj0DzrTXgh-Qbg_EXOAouxGDDqeA4WfPI7tCH0oZcWq5LCpf8jKrDcAmuZk6N5H5OzhR2FA9qmUKYkVN2VrfnFZbBaulQZcU_3ycB-ResPTTOudDKFGCjxNvWPks26ugSergwItKRBwxDqaU4ALNBzoH0ph6UjKo1TQlltFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇸
لیست نفرات رئال‌مادرید برای دیدار فردا مقابل دپورتیوو لاکرونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/103365" target="_blank">📅 16:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=QuT-mgg-UQ9Fgwc3U6Go9qQ2r7oSHIP2GzuPx_0u2U791OtXq4PCArl0UwbiQ_8wQyt69Y0xZKeI0yg9Djws1n2dDScQyY5BhBkfQkXmR29hiOkyr1LBjtBysjt1RYKoiZ8IIC5KRzwe9AU7vD4_fKVrnIEIkG6gSC1HMLkyHwC-QOTCl1xxh3zXQmzPf4kjeQ2p9RswCzKkGayVSDRQSkYONPebuokBwJNMc_RbURwEAZFI6GfTzeZbmDH33L_ogIFOm0aFLoHQZm7l-lrMdf66MZgKrrNGL1AaiRsF0hnSXOBODqAD4WT39UP_2EARBtt1LLE62GfAvDzoZHUYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2091ae4f3.mp4?token=QuT-mgg-UQ9Fgwc3U6Go9qQ2r7oSHIP2GzuPx_0u2U791OtXq4PCArl0UwbiQ_8wQyt69Y0xZKeI0yg9Djws1n2dDScQyY5BhBkfQkXmR29hiOkyr1LBjtBysjt1RYKoiZ8IIC5KRzwe9AU7vD4_fKVrnIEIkG6gSC1HMLkyHwC-QOTCl1xxh3zXQmzPf4kjeQ2p9RswCzKkGayVSDRQSkYONPebuokBwJNMc_RbURwEAZFI6GfTzeZbmDH33L_ogIFOm0aFLoHQZm7l-lrMdf66MZgKrrNGL1AaiRsF0hnSXOBODqAD4WT39UP_2EARBtt1LLE62GfAvDzoZHUYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رفاقت ورزشکاران
💞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/103364" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Ht_QswgzMLV6UKWxQEzflSSlcceAhNVyYD_isYUjQ_Yjw494zDH2na-VO6Jpt_6MgIMO4ARm3zBXvZvGUvlXRaPnl-Ai2nMH76FHZix5w57rOwSc38uv8tUEyV-JgEnx5UUMWoiCRX9wYu2Y1EdnlT98XH44XYedsqgZqMzFylX8o-WdKTcFz8MjPa-_emrOqBb2x94msuxVbylmNLAn6T3KlDwNq_rj0NaScCWtlxSJtdVdC1VhbEgoEtlTojBdylYBnI3YxztrqZQtUDTJ35LvyZ2YfoP3EDmMUyLxXMd9Un07L2hp2z_wEc7eEqOFEGRK3ZlLgyZLxtlPKQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا: پسرا وفادار نیستن.
پسرا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/103363" target="_blank">📅 15:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFpOVJGeqUzrMiauv70EY0zceCmlnCnvRZBM7Ea-aw_PupmWFdgPKRJVGJkf57c3mMwT2FfQ5ReuO_kj7xzth3LgDYMpXyuFBqjnf5LW561V8ZIPIAM0kKKi8T_80EHqRUfZgteTeY3lX1D_AvNM-DQDXG5BrXD2Ol05aCpIZAdafid0V3Bo2GW_6QbR2XWGvtI48XFoJUtSkfZ5xAxftuBQHZJPwdSonj81xipQft7uvatqTpgoq2g4R97c7GrCuwe9m-d9axqf7JiW28trCn9k0Qzrkp1gYiXZqIbfzBiuDUuq0Uey4sCoWZFFET8ePh7nCuWVe4VbqylDN1KloA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✅
فابريزيو رومانو:
اینتری‌ها میخوان هر جور شده اسپنس رو به میلان ییارن. اون میخوان این انتقال رو با کمتر از 40 میلیون یورو نهایی کنن و مذاکرات بین دو باشگاه به زودی از سر گرفته خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103362" target="_blank">📅 15:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=EeGGPe6AjWiAkmkXx4LqTOxF_PrgRlFhP4lTAKuN5jhCe5WR_VSwtsbshPZCgQquoW0CH8P5rcaynGIA7-YJAAW0dpbYQWS8jvwvq6osHQkZa8-9hZLF7IB1doixQlfGFjWQHq_Pe528dwjLHr6h32OSm1R0-Kwb_8wd2rdPpTTZUjKgp00B9r2d4RLFTKelDCbhbQ-2KwAEZ_B0TF4YxfN41ZOaL315T7cEjaACvYFj1Im1hKfDinariY3zXXJczOBYfwT7rY9BfnLAvUPpg_vxaOHZfg7ImVb3hGi1ZXhZhzLJ7Q838yBUTQkM-onmk9DdwBi_RFEnitG5KYyKyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bea6d735e.mp4?token=EeGGPe6AjWiAkmkXx4LqTOxF_PrgRlFhP4lTAKuN5jhCe5WR_VSwtsbshPZCgQquoW0CH8P5rcaynGIA7-YJAAW0dpbYQWS8jvwvq6osHQkZa8-9hZLF7IB1doixQlfGFjWQHq_Pe528dwjLHr6h32OSm1R0-Kwb_8wd2rdPpTTZUjKgp00B9r2d4RLFTKelDCbhbQ-2KwAEZ_B0TF4YxfN41ZOaL315T7cEjaACvYFj1Im1hKfDinariY3zXXJczOBYfwT7rY9BfnLAvUPpg_vxaOHZfg7ImVb3hGi1ZXhZhzLJ7Q838yBUTQkM-onmk9DdwBi_RFEnitG5KYyKyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل و دستای پشت پرده فوتبال
😂
خنده بازار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103361" target="_blank">📅 15:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsGQY9ozOkQYydFzLY5YVdvCZdhFJyH_3U29I9_LI43bEZmJ-u-tyjipxGtuF7mRZ7WXmKeaVFX89rnsjPXsIKXVOnSqew3sAIkwVoajNRa6l-PfjjUZ1QrUnkvEcSngqbpRLZrKgyhZVYK6IqsNPf0vDbZctK_uBT3fJuARKU89_iHt8GKTckybzkbiC8rd0Xf4A6jzdc7Q2DJrTKTxSEZjdfUZovKo0eLbOFhd_14-zCoGt_6_0Yahv017jsz-fXnGmD-IpGA5evw6B8inw2fnfzYttnCLDMCgVrAgpS94CClznN36XDJ5Z9ApjxEgipbCwyY-NQujT7TbjbuIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو: فلیپس با قراردادی قرضی از منچستر سیتی به شفیلد یونایتد پیوست.
𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103360" target="_blank">📅 15:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRm9yt2BPEI3i-UYsZAcn0syX_HAxCR4zs8p1vLJOcffOWqKYHsl4Wy9aMJlDsefdMvz9LbWutts-mNRQeNLmQjno5LzEYsm3OjnUCTLU5gMBr9zYU9umPs2vy4hGbhPtfFMOGOcDgAUlbKWyj8jhyockqqlFNlts7HHFX_0FwJhwdijdYDhlOz4lhjteEpD96BJiVUsPbK4Bdd-BFiuDGDEd_tcqlsDUSDBwBPbuJMT60nF49EA9646DKHAjN5k9zFnZEkQ0g-9gT3Bm5tU2pq4jJPXPc_Snd-uWJvvcZwBHa9h4BkAaIlqddknFp-kIFJfK-pAqZyC_Cw7rfpXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔹
خط دفاعی یوونتوس در فصل 2016/17 لیگ قهرمانان اروپا فقط 2 گل خورده بود تا اینکه در فینال به رئال مادرید رسید..
⚪️
اونا تو فینال 4 گل خوردن و جام رو تقدیم رونالدو کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103359" target="_blank">📅 15:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Q78oXehsHLOThOpiEMrWc-Ekq5axqG1VuZzXSka4gPOuXbnFtyRI3HzAvS65E4E0Q3UHQnmzmCjYoYCBKvst7hwiw-xqaqtF1ZSbSg8pZ9tOb5Yomv5RaljLAC5xVsw4zBgR7YTmX3jLYZW7hJn2WIjOf_fMwAJHvxrmkVBGnetST8OvZ2FS0fvhIRY8Mk5aLvmsX6k-C-lyXha_GzOPWq9WXhg80r4lZBI67_k9c2CouBkPV2XQRBHj88IXBB6XS10qEG2Zbs1Gy0gRIfGzN-GpliRt2gtgv611L9vseQRoHNrRi5fhJS_Rdx3tfD6ABKJApIL2t1vQeawDw6q9jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1146b9d2c3.mp4?token=Q78oXehsHLOThOpiEMrWc-Ekq5axqG1VuZzXSka4gPOuXbnFtyRI3HzAvS65E4E0Q3UHQnmzmCjYoYCBKvst7hwiw-xqaqtF1ZSbSg8pZ9tOb5Yomv5RaljLAC5xVsw4zBgR7YTmX3jLYZW7hJn2WIjOf_fMwAJHvxrmkVBGnetST8OvZ2FS0fvhIRY8Mk5aLvmsX6k-C-lyXha_GzOPWq9WXhg80r4lZBI67_k9c2CouBkPV2XQRBHj88IXBB6XS10qEG2Zbs1Gy0gRIfGzN-GpliRt2gtgv611L9vseQRoHNrRi5fhJS_Rdx3tfD6ABKJApIL2t1vQeawDw6q9jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تعریف و تمجید ستاره‌های سابق از لئو مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/103358" target="_blank">📅 14:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfxlXhm5V9CLVIb0FdIGzkjFiY3Xhj84B076Z86Ivi5eOSHwO5nyOV9qMIUUbwPokUQ52UyRb8zsRs8UzNgu3rB45S-DcBqD-oFHnFr0QEihWILNswNDavDMdl4mSh9EguJtb37vgHtxxBbkrBsyqd4c_WpzHwLO9uN1_hf9EWWkgo4Au9bcie4r20PA19jCzq1dDJ7UbM93gDtUbVFIypW_NOtsnykdY1tHJq3xpKzg6BiBol1KAm7v2wxBytNuxjYi4AQl_4BP4yvaQuEVBFVZyN4aOO0jOeGJbHTiwDhqpnOSVgBGmRkqJ5_HmLn2wcmYathaeQYz8sMAUsSLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103357" target="_blank">📅 14:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=gBZJJ-1l30sqou2IkV3Si2purOSZBmHDYR5dZN3VfFdbzESuZ2g4XDFSlM7bhV7Nd4OJAKXgl6hJsJWs5nxZWg99wAhpRLTbeqDFAl7bZSTsnfVHLjik-6kd7dKRXxACkiaV7zbmolLr8xmRtptqSfG39HQ3kT7r8VnId-J6awrShcFuB32kt4uxWoHlGGPkTzWRx8cceviRlbjA_t2syBAxZs-n8xCCfxgzRxitcZBVHu0Qh_jNj78nCTrfJGJ1dhic1POWqNQzzayD9MDAIWUcInA7P7CNOVC5W8EGkv_1ZNeSHe_oF1O2a98GiMK5H3dQaUCoGK-zCc-AfQg5DJDdE3fhVM1i2LVdix-U3AQilQ9wSqv-j1btrE8y0MxHrpTWnwWIGIUl35hf6loTYB7XSxU6HxqtaaNRILHfrtu_-3UzD1cwYyf2QWdVXaW_d8wUqQQrLMdXS0D7o8u__yQueW6SPjyKCApH9imxCX1AQ_tHu7Mi6_YqaLRr41LsjausmjprPulex0IIVkOBFZIB6MgOqSLhoCdaJJzASEs4kI4_2CYIAMHfnCEce8N0SsXLma68opmrXBpRkbPvGBXeB_GuAIN8v1xBCOdvTl6KjfUke9HqrELq9sFHwCRMa-X31-PY3_wLJbLPjaEiawkS467-ax9d7kp1HY5p47E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/befb00f0c7.mp4?token=gBZJJ-1l30sqou2IkV3Si2purOSZBmHDYR5dZN3VfFdbzESuZ2g4XDFSlM7bhV7Nd4OJAKXgl6hJsJWs5nxZWg99wAhpRLTbeqDFAl7bZSTsnfVHLjik-6kd7dKRXxACkiaV7zbmolLr8xmRtptqSfG39HQ3kT7r8VnId-J6awrShcFuB32kt4uxWoHlGGPkTzWRx8cceviRlbjA_t2syBAxZs-n8xCCfxgzRxitcZBVHu0Qh_jNj78nCTrfJGJ1dhic1POWqNQzzayD9MDAIWUcInA7P7CNOVC5W8EGkv_1ZNeSHe_oF1O2a98GiMK5H3dQaUCoGK-zCc-AfQg5DJDdE3fhVM1i2LVdix-U3AQilQ9wSqv-j1btrE8y0MxHrpTWnwWIGIUl35hf6loTYB7XSxU6HxqtaaNRILHfrtu_-3UzD1cwYyf2QWdVXaW_d8wUqQQrLMdXS0D7o8u__yQueW6SPjyKCApH9imxCX1AQ_tHu7Mi6_YqaLRr41LsjausmjprPulex0IIVkOBFZIB6MgOqSLhoCdaJJzASEs4kI4_2CYIAMHfnCEce8N0SsXLma68opmrXBpRkbPvGBXeB_GuAIN8v1xBCOdvTl6KjfUke9HqrELq9sFHwCRMa-X31-PY3_wLJbLPjaEiawkS467-ax9d7kp1HY5p47E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
لحظه‌شماری بارسایی‌ها برای جذب رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103356" target="_blank">📅 14:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhl9my3YTuZ_esiWAizt_3IYbjmwsulO4F8GFip_0R2NYO60OYi3djQ-YnLY4RczwtTkpTMZT90JdaCmCexEIj4GmGz0SF3bHgjcwdYkwyAhJHWfNhID1q1lYf7NmVX1cmiDYKrpoO56OyhZv0aCU02ciS7N85vNCooCvyfyEp6reMh-QDUNVpqwlCPAQe2Bf8ZRkPD6tlkhjfVJaUn9d0RIbR6nWY2aSrF2o7QS8BfcPzv5T-Ffjzth0h9Pk3XcWNWoeGYD5DnC-QX4zOf7FZIMIxFj9enDhn2TrKFBLUF_rTxJLd1e1XXFT24cxWM19_yv8WzOduMcoyIyomJmhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دو تیم ایتالیایی که برای آخرین بار قهرمان لیگ قهرمانان اروپا شده‌اند:
🔴
2007: میلان
🔵
2010: اینتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103355" target="_blank">📅 14:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103353">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
#فوووووری
از رومانو: دیگه مثل سابق قصد حضور فعال در اخبار نقل‌وانتقالات رو ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103353" target="_blank">📅 13:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103352">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO2PIRfkUJJRsMt58kTSUJvuAH6vuaYXwi2fmen6Fxom3FH5VY8VP0aKsMLQvodGn9UO26vwKaonAXeZmrSCoh-IRkgltT-BNpX3rb14yZt8t8W_JQaOmf-cOJNSJnC3yWBrnOCYfpnokLDdGxImbaHoylId_G6fX7uW2UqzhDHqLFkbwedQR_DhzXuKJjNj2NPNsoiMnhuCmFwYKuVj1s14r_tv9slRAq2enT-ealyJb642rI3G2M_EOGHz59JmYX_VHRxP6-YYVWLNuH35QiUYKH0Gyow82eTomhXeDw-noDSy8PGA2pCijs99AaHeCn_c66ef3UafMCeJIHBuWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
😆
سال 2021 قبل از بازی منچستر یونایتد و لیورپول، لیورپولیا میدونستن که هوادارای یونایتد میخوان جلوی اتوبوس تیم رو که داشت به سمت اولدترافورد میرفت بگیرن و نذارن تیم به ورزشگاه برسه.
🔻
برای همین لیورپول یک اتوبوس خالی رو در مسیر هوادارای یونایتد فرستاد، در حالیکه بازیکنان و کادر فنی لیورپول به طور مخفیانه از یک مسیر دیگر به ورزشگاه رفتند.
🔻
نقشه‌شون دقیقاً همون‌طور که میخواستن پیش رفت و هوادارای یونایتد اتوبوس خالی رو متوقف کردن و حتی لاستیک‌هاش رو هم پنچر کردن، بدون اینکه اصلاً خبر داشته باشن اتوبوس واقعی لیورپول خیلی آروم و بی‌دردسر از یه مسیر دیگه به سمت اولدترافورد رفت. لیورپول تونست برای اولین بار بعد از هفت سال توی اولدترافورد یونایتد رو شکست بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103352" target="_blank">📅 13:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103351">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=BdzZl5kCap5N4CMlMlsNtTvIItTYjNE-w_JJsdkv97Xuzy9vYLGzbZ4INMh0GV_NQmD059u4eqkScIzc7b8U0YlG--67i6Kbmgl7hr5MzJP6x3AuIJ_pJmVfM3Pl628ra0D3xrb9qpmR2KJvIVu0hgwWr2SfptIn1AC2caJn5eFGmxOZ7V787ug2A20P2pYf26YyUcEqcZEFSZCwDfTVkm5ceC5jk_8OHgZRJLT41krgE1CLdMfM5mk-4zMq3MKVvps8bERz_fPsPjJUoiQsi-2W8gujxPZTocE2vyMVtkjwzNpty5cF8jQvGr-QkeO--HCqd9oymTo85GL4MKGxqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9708df2d85.mp4?token=BdzZl5kCap5N4CMlMlsNtTvIItTYjNE-w_JJsdkv97Xuzy9vYLGzbZ4INMh0GV_NQmD059u4eqkScIzc7b8U0YlG--67i6Kbmgl7hr5MzJP6x3AuIJ_pJmVfM3Pl628ra0D3xrb9qpmR2KJvIVu0hgwWr2SfptIn1AC2caJn5eFGmxOZ7V787ug2A20P2pYf26YyUcEqcZEFSZCwDfTVkm5ceC5jk_8OHgZRJLT41krgE1CLdMfM5mk-4zMq3MKVvps8bERz_fPsPjJUoiQsi-2W8gujxPZTocE2vyMVtkjwzNpty5cF8jQvGr-QkeO--HCqd9oymTo85GL4MKGxqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مقایسه مراسم معارفه در تبریز و ترکیه؛ فاصله جغرافیایی زیاد نیست اما فاصله سخت‌افزاری کیلومتر‌ها دیده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103351" target="_blank">📅 13:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIrN9xX0Zw8EUeaxmeOsV8ist_DkTIgoa4LeHarpjzv_VmjMU-g1L12CAQrMEhNArr5HyFvTIwgXn9HoNwQHH2R77xLhIGWIgjDs-l91e4wCofvyPgxBZu8CrIqVdm7xafRv-EKEN0VkCApXccKrY1_hIq20HNrtrzwSltZQ2QYxsOuUsj7hOdbn-olZ9ARulUsaI5qd8lWi_3q9cpUragFoCfBU3z0Pf40hNM6CdY2N0KPSUsU_gk2HTfa8JKpPpjfNGodXsPXBHLwq5Z_HSl8wCpitqTjuZGtRttMWZt3crRS-gWoxsFP01RVCNZsT-OelHoMEr8no2u7UlOjO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ ورود خولیان آلوارز با وکیلش به محل تمرینات اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103350" target="_blank">📅 13:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=MucmOacTlP7ZGyCw6dqt4JJEvEcvvM4_Cg_u2nlqj_aFvOg99Hu5HvoTqlYq2yUVKqyZR2fBmbi_WFVASVfx-cW6WK8rfxCAfbf6fX3ua2KW2qYJB3nObw42yOhzW5kmcC4bOGBFel50GdWM7tP298UxQm4icasCfiCy4CLzBs06ONRVUwUpFZyoY0At0h-sYcijmeQ3pAIQqv7G85E6G0pmzXfJupv2I5ZxfmklQ_uTbz-gK-rq6ZyQApmX2rF322qdtWcDhI-MdPVJVraKefv8QuM_SHngYVmvRmV-UACI2EDGgjcL93Rb-NCdINbokcOYgnvfXDx-oy7AaCXu5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/705d7fe27d.mp4?token=MucmOacTlP7ZGyCw6dqt4JJEvEcvvM4_Cg_u2nlqj_aFvOg99Hu5HvoTqlYq2yUVKqyZR2fBmbi_WFVASVfx-cW6WK8rfxCAfbf6fX3ua2KW2qYJB3nObw42yOhzW5kmcC4bOGBFel50GdWM7tP298UxQm4icasCfiCy4CLzBs06ONRVUwUpFZyoY0At0h-sYcijmeQ3pAIQqv7G85E6G0pmzXfJupv2I5ZxfmklQ_uTbz-gK-rq6ZyQApmX2rF322qdtWcDhI-MdPVJVraKefv8QuM_SHngYVmvRmV-UACI2EDGgjcL93Rb-NCdINbokcOYgnvfXDx-oy7AaCXu5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🚨
‼️
تاج: قلعه‌نویی اول با ما ۱۸ میلیارد تومان قرارداد بست بعد قراردادش به ۳۰ میلیارد تومان رسید. ۷۰ میلیارد هم برای جام جهانی به قلعه‌نویی پاداش پرداخت کردیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103349" target="_blank">📅 13:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو؛ سوزوکی به پاری‌سن‌ژرمن   HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103348" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqWOz8SdKcnAfeLwo0Nm4q7DvInh9IzJulM90ysMJtBYV0o_88W1Jrmz2haF1m0ieZ4YIPogTXRKCMkpi5jJDApPwo5u3lhBslvaG1Ehsx17bp-FxOr0GMV22LlNlcOs1wHgApGqyNJnalh0aC5S2sYKFN8gHzCrL0g_SC15RTT7Ml2sO09Os4iv3jmOh6SnqNmB1PxnEwmTCAGC5oMPXgYZyn05msVcdSRUDNZxuQOCRj-ecOXhTYond8OAp9alqgkgy2U4Al-I3dbBUstGAwYbHQlWvl0d3dHwR6trDbWKAFVJlhm9cRLryj6LvlbvLt5YUV-l-9vvceRLnqkGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103347" target="_blank">📅 12:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ-yXGhcsg7VjR9ltvrqwgJUDt5m3ZNgo_VLfSq5O0-GMP0plzovhtpFfdJ_ynJUHhGvx9FPlDbPNsBeBXEQfccZD3njL0L4SEl-fJV-Hq-kxG3lZta6RXCXAok03tuW7YlnWMx_FkgnuqYDkidAkF1m6oSWpyqiJGfBao_kghk55QVLOXtOuZHpNCvcO986jtelQPsoMPE057g_Cvq66du-cEWJbOFgqmoEhhug6aHoRduJdfOjriPhflCTlLo_PtZrNKEYYELHaqrThRRtMx7IOYHrpE6F64F3yTxWb0WV0YNrsUOsKTGz8Pl9PyTWm-65n_AS76qIEnM1Cw6ZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
✅
هاوکینز: باشگاه پاری‌سن‌ژرمن با مبلغ ۳۵ میلیون یورو موفق به جذب سوزوکی گلر تیم‌ملی ژاپن از باشگاه پارما شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/103346" target="_blank">📅 12:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از بن‌جیکوبز:
🔺
منچسترسیتی اگر بخواهد با انزو فرناندز قرارداد ببندد، باید رقمی بیش از ۱۳۰ میلیون یورو به چلسی پرداخت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103345" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LshF0JEsg1k3pW54jPwIXk53V0mtNkpN3vgSj13gV3a0EY-QCXBcLZjQEwkpPjEIsS56Kj9st3ngMoFvkffk9KndKmUZjd3uavpX1YuPAHNh3DhWV2sEZ36acAjgp6TOtLmzivCXtFg84TgkKm_uTO3NzwTHZcLo9wo0FyBXpke5_M3_b4MslyQC_hW2SlC43A-GTsj2sIl4kr5o0WnVaZ_AFoHRHdUGsj_uL5fpqJEvyEM-aDRbLBBcMYuOoxVTveaSsyw4FUOT7f8x3KSI_kxP2Y5oa9IORLjlABA7h6GEU7YUlFlMrWDnZY3qiSrhi9gqTi-LVkZwSmm3Ybjcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📱
استوری کنایه‌آمیز سیدحسین حسینی
که احتمالا مخاطبش رامین‌رضاییان هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103344" target="_blank">📅 12:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUEaeV_2ioUf8Wpwx8A7FfBzoMdc2_Gs40DJspKYeXnfqp7ivTIbGTaNf3zh3jdwxS023f7XITlGdFf3QrzzRMi4ZNu1X_Uf79YCXqnLLsb3DXVSOKuBwX3Og_fzdlezgDOWanoDizG8Qirdr1w4fwacgs3YwwJr3pK_RnjjjtwL5OVU4EoIZDc3RgMdLPQnp94HsBFHKsiR5WFuwrsWoRzJRCF9tj_cDw-sWRX-PPw-sruZ9vFvHFIDLuOUvrR25QepOm0b61GEM72BnZ3xR2CV1LXjgPgqgI_FyfR5Z4lbDrV9spakYKt0xIu5WMCdI8tQrKzvsAAOzCJN9Jc8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQdYGzRKDRkICaft145KsjKAaXou0p_qdQc9JJ61BcY8k0WaJFop0eq_PWqUTMrcBa6AJe-ZpFYeP3nV35HEKhFoNMDIN9kociMDWvNhqmX3dSANPsF6vykgiMx_wxZVAUTwiw4tVxMis3kjWbzSpBmqNiJqOckVXZfZheAxizg9nGqcpyKIsVEj_1Sl0eKUYSIc_3uITBWHIWPDWBoptvLGfo20orVYkar66V0nlqmnCHm2_SXCZsrxIqpVU84tICz1Qc5pGLSU9UPbYLvOgVz2gafd70qd8IH8cysCiHnLVG16C5GkEV5UYI48pZcBkqV7VIZrlpqYLQOWFG4YCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇫🇷
لیست پاری‌سن‌ژرمن برای دیدار سوپرکاپ اروپا فرداشب مقابل استون‌ویلا انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103342" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyb0O03rAUd6aj_XMH3CcZ7Gk9wwCOIkl2Hzex5FZCiROOsh6VuHgQ0ox_zxvPpdfiurZCI5pVKeN6WpvZ6M0hds8soQJmbji89wlXZNyAennwdLyttSt9mQMsxjEzQD_C8bSxg4th1uZy-YX8kRuapIVHCpRzp1A-2z4YU8HN-YZy0RKiJ-nMrUWKaCjVWe6rTmVTDRpbKcPKc8u5kUPK8FV-iIuA1lSpbY9LIFXW-0Z8M8sH2J94DXcvj1Z3SygsqnEKR6_O7781usWHH6cQEAUSjVyvfiBLFT6oTs0RiWLQJMKwjo0xKVLs77b7rpyFEU1EuOgoFYHopzv4333Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما اصن تیمو ببین..
بهترین بازیکنا رو تو هر پست داشتن ولی طرف اینقدر عقل نداشت که مسی رو هافبک بازی میداد. همه جوره این تیم تکمیل بود ولی فک کن قهرمانی لیگم حتی با درخشش فردی بازیکنا میگرفتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103341" target="_blank">📅 12:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC5ND-IpMpJopsMOoc3C5UDzYMJZF-Dtww5OJWRLS2xPHMjMK7qgOaRc-5x0pMxy5vJuMK2eQlsShi5F_v5YUsFR4khhwXX8C7hOoOJi-txGeVt0yFNA-rF4thnlUyuwa2dxaGxL90KMpPSVAc7afy4siN-O9PJpXypCvZdoNtX6usXdBFSGnAz6DXCQwowi4l2COE9Hu-_BNl3f8Siw9nac9NFGyoA_0jJf4W-gN4yNoig2_x6NVbfSY4A5PYOwaT4td-ojw4Er7L185RPtQk74K7ldLh_zqQ_b9L6saCYOttUcbQrCeJ1YusSCdScr4B6MOpQGyKojbRkkx__qZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
روملو لوکاکو به فنرباغچه:
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103340" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnAoaeHgTkxVzvmJQzqwsGcVedPLSCRN7kwM3abX741_lZuXifVkwE_FSx1-Qy87k4s2gN8eWKaU2ae0QbDN6m3djVzxecBBiWH_F8-W2zttjgNYTdmsEi5qImLNtfAfc0czGVdPW7I_dwPuDU5tL-jUdPdOQLKueJBJHgr0jrEJzdmLYuCnPi7WyO626rpPvfzzFqmlHsOf7oO_tz6M2w_H0uJtswBHM4QJUXcihVbT6SRj7VNAWhnP8mE1Ew8WsXZtUrYfCorqfclHBgV6ThnWMh4-qSEXz_ag50kPG2QMmoC6sNLMVDghS9G5YqlQQ9yFMsNy12hSS1hFrhBviQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
مقایسه بازیکنان خط‌حمله وحشی بایرن‌مونیخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/103339" target="_blank">📅 12:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYzaQQ9UW0Q0KGDo86gOVTZfTLiKpq-UQ1aAnU3pRM2JmFU4RZ-lSmAE4skcRf31Z6cTlLYJJB6YUx-Lep_lT-PmKf4vYRkPA91uj-OM5BlXccR4KfrXObrdTlgvyTXSZsCvPTAgQUWEJIQUnOQE_K5mjj_o0ewa8j_Gm9pwnGIQeOa4dOD9EGhVSmHTLH47rsQMQrDvdKMwCdr_zqicUh1JI5nK65Rb_DfQmdjnhG_qTwq1CJdc2ZYC3jIo_ywGGy8_1fMTjf7Eg86KzBloUC4jLTstC2iFHDxx8AQqPLtnipZWpwSe-TNXUav0GIN4BGEfCVeWo1PZiTlAXcqesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
پیراهن دوم و سکسی دورتمند برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103338" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSi_Z441lT1zDhdDnslyYKxniEYjf3N6DSNfinvEtKxoWNTY5CGFJLLfwZd2Vpsz3cIoVMZmjioBhCogmBeo1B4P_Y2NPInsdv4VV_dzm-rE02j1Q5p_Q1cRyY04ZE4A0OBw_O0iHI1_apNc1MSWUfFnRTO5539TKsLrAgy6ho5xdqozHy6n3TIxWmtxiNPhrSg2xyAoIOcRuN5e_ZxccxbWghFo8E5iTvy35ra5UxdlczQ8DCNJexZxb1yYJ8y3rhmL4o5hcgGBrdUU_1ZPzaxpxGlP5RzD_V2rQAgR6dIY4u9pTjngwShhFKvkd-r2GWtFhUssEtHskw9o1m2CBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری بامزه جواد کاظمیان
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103337" target="_blank">📅 11:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=CGi0oysZR3eMk9a-rR-2V_X3_iIte_tid2vjFksNJ2vF3wSOwfYaIBW2HJPNw8120ZqTM4sqW3GOvdBQb8AwwGZTA12RySA-gGBJ2_vAshRqff6sOZhto_X0VOX2cWUZtf10aKvz_Crbrfwi3sz2Rereeom04_r7SbJgLin4AqKaxPB4_X8auB_emjeDCXfjbkqdz1VA_ZL9vc5acddDCoZgjQyrbzhtQgUIpLy5MsIfB6PPBa_e3tKuUBJNAIMKsl08cB5O3f8XuslYCderDBaa5dypqwH6n-4V4IIXhuN9XNgBRJYTVRSjKeSPG5THxYZzJmweN35KPYoAum2-oSicI3FBBYl51-1_i3ZFZoq4HIk5Ky3fDQf1ykAqyCGPiqyK2zZLRHQL2mRzXvpvsd0e9dXCyzDlz_1kxnBrkEElzTMarFb5ZF5xKIMRlCqm9aqKgCY940us625lr0H55Zys1R_CDXZ9cPc02sBBpN6B5a1UI30j2kIwGUtA_QHuZC_iXjnzqIEh4UdZcWeM4YJ63VZcvMbijJkpPIMlTmPzxna3oE2LF8wiGXKBfM94PNASTg1fC1eWtNP9lukAxUjzkN1At06fj4c_JWvLdjNhyZyyFgOi8zNtVZniekyZioa2njzVXSmPhpRgLP9KfXtOBNZk4wqmQisxhjuLGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d8c12332.mp4?token=CGi0oysZR3eMk9a-rR-2V_X3_iIte_tid2vjFksNJ2vF3wSOwfYaIBW2HJPNw8120ZqTM4sqW3GOvdBQb8AwwGZTA12RySA-gGBJ2_vAshRqff6sOZhto_X0VOX2cWUZtf10aKvz_Crbrfwi3sz2Rereeom04_r7SbJgLin4AqKaxPB4_X8auB_emjeDCXfjbkqdz1VA_ZL9vc5acddDCoZgjQyrbzhtQgUIpLy5MsIfB6PPBa_e3tKuUBJNAIMKsl08cB5O3f8XuslYCderDBaa5dypqwH6n-4V4IIXhuN9XNgBRJYTVRSjKeSPG5THxYZzJmweN35KPYoAum2-oSicI3FBBYl51-1_i3ZFZoq4HIk5Ky3fDQf1ykAqyCGPiqyK2zZLRHQL2mRzXvpvsd0e9dXCyzDlz_1kxnBrkEElzTMarFb5ZF5xKIMRlCqm9aqKgCY940us625lr0H55Zys1R_CDXZ9cPc02sBBpN6B5a1UI30j2kIwGUtA_QHuZC_iXjnzqIEh4UdZcWeM4YJ63VZcvMbijJkpPIMlTmPzxna3oE2LF8wiGXKBfM94PNASTg1fC1eWtNP9lukAxUjzkN1At06fj4c_JWvLdjNhyZyyFgOi8zNtVZniekyZioa2njzVXSmPhpRgLP9KfXtOBNZk4wqmQisxhjuLGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
برخی از جذاب‌ترین گل‌های آردا گولر ترکیه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103336" target="_blank">📅 11:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری
از اسپورت: سه باشگاه آرسنال، بایرن‌مونیخ و پاری‌سن‌ژرمن به جذب ژول‌کونده علاقه‌مند هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103335" target="_blank">📅 11:30 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=DFsvKBcp0XghDCn7LiEO5G1akNBMUUinAN5u9NPunLdortdcIKLpgza-lvIBr-C0sypIweo_Kizc0fdME3wz557llUOhbwywTRmsq_qMpg0OLwFWHyieLc44D3-rxQYOuWVEdLUBktYt9PMPv1FNsauhfbbXVrp61pjpwPFiuFCeysS8AQhoEcvFEtI9hEQQlQ4d3HGhwMrXXAuE_jvYEFzl1TZKrDs0MhHaWwMp64iec2zz9i43sIs4I9kBc2MRaiVfzZ4rDlkCRFvxNnxr1g4m07lmkHTZuyDee3whOVwqo75MqD22pLCw1c98FKrfXRpDf2osqAQLE3tqBw25eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dfe7c98c.mp4?token=DFsvKBcp0XghDCn7LiEO5G1akNBMUUinAN5u9NPunLdortdcIKLpgza-lvIBr-C0sypIweo_Kizc0fdME3wz557llUOhbwywTRmsq_qMpg0OLwFWHyieLc44D3-rxQYOuWVEdLUBktYt9PMPv1FNsauhfbbXVrp61pjpwPFiuFCeysS8AQhoEcvFEtI9hEQQlQ4d3HGhwMrXXAuE_jvYEFzl1TZKrDs0MhHaWwMp64iec2zz9i43sIs4I9kBc2MRaiVfzZ4rDlkCRFvxNnxr1g4m07lmkHTZuyDee3whOVwqo75MqD22pLCw1c98FKrfXRpDf2osqAQLE3tqBw25eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ترشتگن در اولین بازی خودش برای آژاکس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/103334" target="_blank">📅 11:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=hyynVqke6N2BIqaPZJl5JDVZ5BDJa286Njo-j6QGWKazDiYu2BbxUq1KnBDUKjdPBszEk37g5CksX22PVIyr-HFq3JBSCtwlvLEOIBE1TR4NIpDQvzzbJwBO-B7zaFTjLTrcq8HErm7rDScLr_fx5Ju7AVOORqF4TMtG-bBmmYF1RrECNujVbAMD8Pe7ele6Kkze0R9aYjwZXvzAjTM1GQLYu6L6UCPzZZuy84gsn6ZKYFztZH-ca6tACG8nyuUS0ROFqpMCB4nPRrbJKx0OHZmPAZWOPuVNd37qOeteJ_AsSZ7zjGUVYqtCRClD28T_LLVfuV4oUHnBCGccYVhByA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3329c503a4.mp4?token=hyynVqke6N2BIqaPZJl5JDVZ5BDJa286Njo-j6QGWKazDiYu2BbxUq1KnBDUKjdPBszEk37g5CksX22PVIyr-HFq3JBSCtwlvLEOIBE1TR4NIpDQvzzbJwBO-B7zaFTjLTrcq8HErm7rDScLr_fx5Ju7AVOORqF4TMtG-bBmmYF1RrECNujVbAMD8Pe7ele6Kkze0R9aYjwZXvzAjTM1GQLYu6L6UCPzZZuy84gsn6ZKYFztZH-ca6tACG8nyuUS0ROFqpMCB4nPRrbJKx0OHZmPAZWOPuVNd37qOeteJ_AsSZ7zjGUVYqtCRClD28T_LLVfuV4oUHnBCGccYVhByA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
لحظه انفجار در جایگاه CNG یکی از نقاط استان کرمانشاه که با کشته‌شدن یک نفر و زخمی شدن ۳ نفر همراه بوده!
❌
دیدن ویدیو مناسب برای همه افراد نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103333" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=B7GzQxMU2uL72AeRI2gRYODa-5leIihUZAVp8pxGdtF0Fvn-A1x4lgv6jAq6e3ME7cdQEfSOYx07VYo4f5r7kwGtAUovsubOCfYn3WptIF8iDlpF4Z2ic-6zeBtuBbU_cNtFpxBGkWI-rv9OebFTQOYt9VbqfQeDOnKl1jRZmN2LC_AdBJ21C978qQjiLudQsoP3EJnrdsovs0e35b9oI_R7LLDCHOTUG9LxH_Y4UFswUoefTwwRUcjelwxHjuYiDTVl0UX42QkPfAE6IOEOpinhPTSPbO8sxlIQTFFGYqbgY2lHayQZpgZUkF2N5QPYPHMDGtrZYNWgegTYVAmitQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdc7b28e6.mp4?token=B7GzQxMU2uL72AeRI2gRYODa-5leIihUZAVp8pxGdtF0Fvn-A1x4lgv6jAq6e3ME7cdQEfSOYx07VYo4f5r7kwGtAUovsubOCfYn3WptIF8iDlpF4Z2ic-6zeBtuBbU_cNtFpxBGkWI-rv9OebFTQOYt9VbqfQeDOnKl1jRZmN2LC_AdBJ21C978qQjiLudQsoP3EJnrdsovs0e35b9oI_R7LLDCHOTUG9LxH_Y4UFswUoefTwwRUcjelwxHjuYiDTVl0UX42QkPfAE6IOEOpinhPTSPbO8sxlIQTFFGYqbgY2lHayQZpgZUkF2N5QPYPHMDGtrZYNWgegTYVAmitQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
❌
تصاویری از صحنهٔ گروگان‌گیری دقایقی پیش در خیابان ولیعصر تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103332" target="_blank">📅 10:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=MXydRqRkQrhJo_2t7kx0v5Ns0vWe3oGkOaXfL3JVJ30nWJRb36yCFSzp_kLDBNAQagEhSXgxbKAr5Ci05Tk_5fMyZuIKZ8YISNEw-EbcC185D03qOdy6qGsydq2Wo_0EvMLZWqoVZBUnUDqwc5mUonsG1AJGqgYI84pZyQXWlDw9B5gvsJFKq0XvZT-oppxOPdZ8aXwhlIvlM7db5YybihdGrPJsQsj5Fkdtqat-UaW3RNzn0tRHUbNV4ym7X01AshWrz5kw4zglge0r78V6oCzQLTTRNcZvpbRzGB4CFvGm0sBP_gA-5Rh5MIXYyH5vdPXo9nQCe9EbAZvRkNNDgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3e540db5.mp4?token=MXydRqRkQrhJo_2t7kx0v5Ns0vWe3oGkOaXfL3JVJ30nWJRb36yCFSzp_kLDBNAQagEhSXgxbKAr5Ci05Tk_5fMyZuIKZ8YISNEw-EbcC185D03qOdy6qGsydq2Wo_0EvMLZWqoVZBUnUDqwc5mUonsG1AJGqgYI84pZyQXWlDw9B5gvsJFKq0XvZT-oppxOPdZ8aXwhlIvlM7db5YybihdGrPJsQsj5Fkdtqat-UaW3RNzn0tRHUbNV4ym7X01AshWrz5kw4zglge0r78V6oCzQLTTRNcZvpbRzGB4CFvGm0sBP_gA-5Rh5MIXYyH5vdPXo9nQCe9EbAZvRkNNDgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چرا همسرت همیشه صورتشو میپوشونه؟
🎙
عثمان دمبله: همسر من یک زن بسیار مذهبیه، پوشوندن صورت تو اسلام اجباری نیست، اما اون واقعا بهش پایبنده گاهی بهش میگم که حداقل صورتتو تو جمع نشون بده، اما اون همیشه به من میگه: عثمان من میخوام فقط تو صورت من رو ببینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103331" target="_blank">📅 10:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YovHjvjDzXCRIYspgEhEGa5h6shyw6GnXu6FM2TFvjR-5HCyehX1i4slngrEsxRD_sQiunU5vlcOYef_45zh_nq0BMXdFRRVpQjqhviWpRFgtJHy_Dw4nBG_1xgsHyIZ6fuSOzX27O--hHgd_JntOH6TtubEjDD7F9KhIuwNBPPor3rHvpPSt4KDzJTbIjGoJo-idTVBk0k_de6Z_E86d9jpcoUzCLlGTPYS77KL7dNYXWyjbp-CNhGCckCxqjaZQk5-LQaMyOe6xDJgiTJQ2hroKws4DFVNv4rCQj-lq1Yckq1q64RL7TbaMz2WPDMOzVyssyo2LjB4ahCn5_VUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
کوپه: ولاهوویچ می‌خواد به بارسلونا بیاد اما دکو و فلیک اعتقادی به او ندارن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103330" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/103329" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/103329" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGupVjJGMuRQrEyiPekX36jgidDgOIo6xfglFSDQ0h9sqBQuqQVnAtyweOVV8BVy-Xy8IvSyTTJtMsrQinrwO4fCjs_pw4YnEB0t3cSiZmjiaBVILCfnHXPOD9kjEpKjOwE5prznT5NwY_jYuwKIwY7ZDvQfq91hlsVM4Rs0mmB88sksJbzcBzTbFTVhgmmNyEgjM5ZEMODXlOng6LkjmjWbcoGsEA6veCQNiS9eDL1Xfq9t1rWqFgcrTjuUFjXtUMMudtMJOd51UBre2EBRTSZwqfE0mttGwhdjVvsFbGWegPTQREZPEfC5oJjuVKf3IS3GqTFMCU-Yi6r6GgYTaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/103328" target="_blank">📅 10:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgZhv30MsOAkEEEQCG99S46GHdEAIQWOX5Dt0esVIK65VQrUpBt2_V3VIREahuercTg1st8YlNte4_dVg-g1dr_etJvj4NyKUOetSKEvo-Tddxij_N2q2NhbHGCvEKZVvty7_vkokHG94kiQhQ0rGOVcdpe0sugh6LziOYWeAIkcHFoRcjuKjFzAfYYoL3IQYTdYBnrCWN2bVuKcRQg85ufsW1BvR0rAE1SuEvXv2wVCA4_erfINDsA122TdkI2ot98RjBC9kji-iF7RCBvjlxlkkOQrKx_WZ3GA7PSjE7FkmfGnR6f7X-noHMNHLZBZUN_8y4I232QemGyE0QEF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔺
دیاریو اسپورت:
بارسلونا اقدام برای جذب لائوتارو مارتینز رو تکذیب کرده و گفته در حال حاضر لائوتارو گزینه جایگزین خولیان آلوارز نیست و باشگاه اصلا روی جذب او کار نمیکنه و گزینه‌های دیگری مدنظر هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/103327" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=sYy-IErrlKVzmGl-8Ibgv_nEVo-x7HyxH4GUkrtaDqXIiw9m9HKBmq5ICWWS6JUgDkCC9mWCu-y379w3Pncqo1C86CSwPRnfY7d2mOTfE3IGmaHB5vCSaOgqP5SZ-5J5PAtzQoLX7zunmac13EI4LRUwmGi08rI8gJxh33Q9aNaJR0hItP_ORRXOrfTkhmaDuH69jjttRYwW_-3Gc27Nl7TmGp5-o7vll-kMd_9hsrmCbOTrGfRV_1qXYaeTVzG9kbcMmcCF-DmnamVcYJCG2i1-2nBRm1z-BqfMQKhQJbz6HNM_buMlfpV0soPAqJ0dshHUOu_s71s7sSPs_zkb_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54347f49a9.mp4?token=sYy-IErrlKVzmGl-8Ibgv_nEVo-x7HyxH4GUkrtaDqXIiw9m9HKBmq5ICWWS6JUgDkCC9mWCu-y379w3Pncqo1C86CSwPRnfY7d2mOTfE3IGmaHB5vCSaOgqP5SZ-5J5PAtzQoLX7zunmac13EI4LRUwmGi08rI8gJxh33Q9aNaJR0hItP_ORRXOrfTkhmaDuH69jjttRYwW_-3Gc27Nl7TmGp5-o7vll-kMd_9hsrmCbOTrGfRV_1qXYaeTVzG9kbcMmcCF-DmnamVcYJCG2i1-2nBRm1z-BqfMQKhQJbz6HNM_buMlfpV0soPAqJ0dshHUOu_s71s7sSPs_zkb_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
😐
سقوط آزاد جرارد پیکه تو مراسم فوتبالی که دیشب دعوت شده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103326" target="_blank">📅 09:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XATEdCgjFt5T5YipB_HrbkLXma-N25xQ-cSwAO_UNwP25l5wtpfh1Korn_y2cAEgB3rxRHmLjMoppgv0UTCYFhpbEo6xqjhAJPYNzuVNJCKp-W8G9Ezp2VfgrSopuPkltxUeWGmnZA2Yoy2EQpKGOL8aIOVo44Z2p_-m8qEwP1CZpurvNRO-hyUDQh0Kpx_6xInML9MCcRPxEH9YEn0K9RYfMv6_Zif4tUfl5mGeSQdqWtVqGymbER0v402-GAbsWVJIgMQ6p-f54RHMYT6Go0LX_156Wjjao5qPpkiWBkFqjsnko3m7jpqBh5dD1KeI6-7t1GDQG2Y4B00HNPuhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
در ژانویه ۲۰۲۵، بالای لوگوی پاری‌سن‌ژرمن هیچ ستاره‌ای نبود... اما حالا دو ستاره روی لوگوی باشگاه دیده میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/103325" target="_blank">📅 09:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3hug-1SJCk9zkpNUbDq49Ir3r_TtgP6Raf4wXNzAGHldj-rIGvqu_WTelxCwxAtDwIlXuohGzq5YLgRNLk7vcOrteFbt8Twq559G6RforjR20u7fDAYIcM7qp9yDCE0NtI2leBan5fO740RWUlLatiuN8JfZQBFXtP5vz13xW7O5FaFXKQFk1RhUoLuPfS6erddcQ6xLW6pBzrv2b1t2M9_2nrgR1td1sjWGwJCGyXnxJroExNJ9bZJDHJw_1_I2BbM_KNC6MDlceRSohlsoMsej9ptB_89QPGWGMB7THT4czqUU35oFyFoH_wsLTc4DMilvDtviKIJdZParXoiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
اسامی داوران هفته‌اول پریمیرلیگ ایران
🔵
استقلال - مس‌شهربابک/موعود بنیادی‌فر
🟡
سپاهان - چادرملو اردکان/امیر عرب‌براقی
🔴
پرسپولیس - شمس‌آذر/بیژن حیدری
🔴
تراکتور - پیکان/کوپال ناظمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/103324" target="_blank">📅 09:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPLEvNcPuTKZghqE7_nI409Xl6eQdJ9qQ4epyCnzylldxjQjutGHjCGJmrfL0LcR-pHV5vlxieoa3mOgmtqHPanPxSczNJK-twurNJzaoA03uXlX-1xCvRfz1fiBhQP0sTUM_jEK-ltZQg-mWmOcz8ve19-1KBhkR491dO_YlJ9pb3eS30BMQEBas9b2krc5642KB6-14SiHAIZHgju0_TbrVrpX43y33gxPmZHXNHCDGSaB0fPBwbi-bXH6cmkrbxgu-CZXmb8TZ38o0ztyTHT2qe61emPZpLDSGxpzBpRKgBsKwYd7FQqRHTOV4ULIVI9IhCHdcCjifmDOig02QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
گلت تو فینال جام جهانی؟
🎙
فران تورس:
من 99 بار از 100 بار توپو بیرون میزدم ولی چشم ‌49 میلیون انسان به من بود و باید گل میکردم‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103323" target="_blank">📅 09:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbfNON912o-xvns0VyuG1jVrnYRABlOlK9IHAS1412iTjoBntaH6XeG5pAn5b8dTQpOM2ygN-UXXQPBKRClMRQlufDmhcOeB5DN7Q6PMtU8n91j0ZHl-GRmjKqPZfuTvr82wXBEvwpsdiPOMIJPYTqhlXC8yl-kteZgCSvewTYxy-VkbvJvMTxhgPD1n_0cUiKfSJHD-4Im6eTotpcS76V_pCMngDeC9ucNC1R6vS79TE3fddOJriWNWWsajmkYWyS423qLsEiaBQJQt-dv6Q9QLIRM_IKiknTt9k7HCA8wgd3V78mP035WEWcTMFZOwblo9NwyW4e4zGUSTTJd-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
❌
پائولو مالدینی توضیح داد چرا پپ گواردیولا پیشنهاد هدایت تیم ملی ایتالیا را رد کرد:
مالدینی تاکید کرد که موضوع اصلا پول نبود؛ پپ بعد از سال‌های پرفشار و دیوانه‌وار حضور در لیگ برتر انگلیس، فقط احساس میکرد به استراحت نیاز داره و به همین دلیل پیشنهاد ایتالیا رو نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/103322" target="_blank">📅 08:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P5-B6hUPkLVFIONG-LzFx78ugokyil6jcj_yS1eTHHRdp6OvFW0G6Y3ccdBXL_9NhPUHCoDO_z_Wy2vNZD2HYQMeXW5XKC4Lsm_pXhCewGOK5ncfu3aSQiQBSR5U60RfdYd4p1jf_4dbyP5wt0qR9kI-yNFg3bnvRZo7hSmaC4RzdJUU_YJlp5_R2RdJYCX8wep5q5wfqQb1QB_if_mSSUAf_oZsalrlA64X7Q_NCsFRwFTyQbDeJ37kmn1evoeH6NW3Yi_dnbDTvJttefaqHRexQL5uLbCYZ3C_3OSNnbfAz3rEPEOqfGalvbZ1k8n7FnGZ9HLhFHJMnNKywrk3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewaOXQZ_OX8e26rRwoiArpo5UH0uwKx--vEhFmustJKoPm_kSDVlrPmH_H6Y6Vv147S7mgQhiUxavebXvHgm4X1DdDijtbUZzXptxL2Ec2UeO8L7arE1UW6wYJVWrVq5uB1CbvhHF_TiGCqj-SEtNThkdLdKaVv7AIZNd9aVvh6CHcH1YdHmwMJo4fu9g6_9WH7oojDDqlJ60zp3lM7aTYCUCVOyKrgqe_R4iudSLu_f9rqs5JQOcUFmh2hmtr4Uhht7BD3HRyIofTldeXbioMml_NEtf_Vu8DRsN9kg4A_54afin-11Ts2YkBIxs1n_Rvgmq15ryOGCztNv16H7sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
⚪️
کریستیانو رونالدو فقط طی ۵ ماه در هر دو باشگاه، هم آقای گل رئال مادرید شد و هم یوونتوس.
🔺
۲۸ گل برای رئال مادرید
🔺
۱۶ گل برای یوونتوس
فقط توی ۵ ماه حضور در هر تیم، بهترین گلزن اون تیم شد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103320" target="_blank">📅 08:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1nLx3RzdQjLbOyUlFNlPgjrSU-hLdXq_dVeUpiXIGkxxww6-qatn4ylHdf4Jbn_e0fYfAhcQtP_aW0RPNdzCA38RJy2zuvBe7GgI016FXeJPb-wnMyXBnW0vfUPu01SBN13HLQoYA5sayz1q9mNsTdi1-x2EvAM4aF4lMLr7Crub3AXS0Pw46HObPA_Bh9EedgN4Ur7e5XmL0LB5gHoQJFbEPJ70d-tOAhPv5WCT3OzxIMEnWEPYtZrhKKnLPIrGSfntroakksXAl9OAnQL7E-kCjUFN8GsEmSrDdoTwDxC5Doh3Xv0aaZyNIpkZj_n6RmkMqH4_Tb1Dtsmf_arWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
⚽️
ترامپ:
فدراسیون بین‌المللی فوتبال (فیفا) مرتکب یک اشتباه بزرگ خواهد شد اگر به هر دلیلی، به فکر جایگزینی رئیس، جیانی اینفانتینو، بیفتد. او فوق‌العاده است. او به تازگی موفق‌ترین جام جهانی تاریخ را، برای چهارمین بار، برگزار کرده است. اگر او برود، دیگر موفق یا سودآور نخواهد بود. از توجه شما به این موضوع سپاسگزارم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/103319" target="_blank">📅 08:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-qq2MkViB9XND40kbUy2ImebWWaEZKkZiecwQN-arZn34s-O7J5u-5e0Jd2GKwJfageFwzYgzUSy2SjchYVKdZny_gluR0pkFL5qPaZFhjGrCdOF6YETVLhyTjSjloXRsjhSRGbWMiYwTlwVFn5mP__xYUjdx1FCQCy1ocJmEtpJq45n39tVvv3sEJOKmFGEaefnzvof_L8CbsAn0NTb4uQnnYe3GtpaO35b1UcHyfv529Hd98hmBq4HdZDmmWzPdGLX26jwYcKYUAYsqK68AwsgzAgy92DfHQstSZzUzCp8UcPj3UkvGSYqEE5aZiksjkhUF_-dLjm4tlX4TiI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
شایعاتی درباره رابطه لامین یامال با کِلی ریالس کونئو، مدل ۲۸ ساله کلمبیایی، در شبکه‌های اجتماعی منتشر شده، اما تا این لحظه هیچ عکس یا ویدیوی مشترکی از این دو کنارهم منتشر نشده و نه یامال و نه کلی ریالس این شایعه رو تایید یا تکذیب نکردن؛ تنها نکته‌ای که توجه کاربران رو جلب کرده، دیده نشدن اینس گارسیا، پارتنر یامال، در تعطیلات او در کلمبیاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103318" target="_blank">📅 08:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103317">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSqgBwpcMqjQmZRL_hyzagz4BZ77ISHeMFi6wD08pSnZb158IJn6mVuQnIwP0H6mXqaV9OkNSOV3nPwMGL9BChaVFj7gVUuFrqzYIvbU3bdjOBKxQrxae_x3ahhnmVGD0WC546Z3Pnhj28pBUSy3DDc7c5hIraVVtN74C_6kikCRIvdXvcw9qGr1Ri0yzwNlQ9DT4epAxeTY7wjo-E7cN3L_dzAPHhGBYLeNdP9r2UzPHXCcuFCpk0-AW232YnPWXHGkV4TNdBBiuBRqYGHTVwiXX2NTmMu7YVxcVR4DulOlFBC3cwfU2UiKiNZI-EYNpmzJN4Y2f6pU7NZOBp_2tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
باشگاه رئال مادرید واسه فده والورده پیشنهاد دریافت کرد. اما خود والورده حتی حاضر نشد هیچ گزینه یا پیشنهادی رو بررسی کنه و از همون اول تصمیمش این بود که در رئال مادرید بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103317" target="_blank">📅 08:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103316">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49775a0c61.mp4?token=axWxg1_jN4LR10fkHX7-HeuO3WZyzZOudNQx7KJ4_HyVuUUJVjtcottLfXaeGwnF-FI6JoR9c4_K5qjpJzR4daQSDWiGZ2Nv6YA5HyLMsWmJhPQJR4VI8Cmf9TCLpBlrt1LWjF-NS3MF6Ipt_BevnvZ7NmxD03ARuP_s5hKyNC27eRs6CLeKJeIxS4mwOOn1HGU1FQZe1Ik-iKTRLGTkWHl3oAH0sW0fAVBKk0ZjIuBRTy5-Vh2BlXEs-xRX8RACHoGL1dGPSjOUZqtfpzOEQ9NQBfHFJ4o2zOe9A5tqdUuaMRv7G-dsM3pnbAa2sPnXpD88XCoeiL_OqJlILgY8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49775a0c61.mp4?token=axWxg1_jN4LR10fkHX7-HeuO3WZyzZOudNQx7KJ4_HyVuUUJVjtcottLfXaeGwnF-FI6JoR9c4_K5qjpJzR4daQSDWiGZ2Nv6YA5HyLMsWmJhPQJR4VI8Cmf9TCLpBlrt1LWjF-NS3MF6Ipt_BevnvZ7NmxD03ARuP_s5hKyNC27eRs6CLeKJeIxS4mwOOn1HGU1FQZe1Ik-iKTRLGTkWHl3oAH0sW0fAVBKk0ZjIuBRTy5-Vh2BlXEs-xRX8RACHoGL1dGPSjOUZqtfpzOEQ9NQBfHFJ4o2zOe9A5tqdUuaMRv7G-dsM3pnbAa2sPnXpD88XCoeiL_OqJlILgY8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
⚽️
رامین رضاییان: ما هم بلدیم تیپ های خاکی بزنیم به خدا ما هم بچه روستاییم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/103316" target="_blank">📅 02:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eedc94ace.mp4?token=U6rlPUTUPEGMINsl4hZeTf7tL-BYE3FTt8O4ztTPlwm6YHUk9MrA83CzcGSWlEGbeXmzKFCcaQw3u8zOPDzHt3Kc0voESkvvAPl5Yg33vPCXPGwHLpp2xhMdA4J8PU3QnRdltELQ_OGNK3BemTd-Gak4eJ62sxEJWQouJaR0DdPghUiXRRECuowfhJHy57mvoAmarVWk8hTYk2KilbsdOGJLo7nsdk4nHn1cmBOFjll1H5C3uIyssO3lSoTP1z98EoD_Ue1hjqD3C5mw_1L40yHX3ZobZOBwdDHW_xuGr4Py1AYeYtiqzWhkDo5MRicIMiiOl44cKv48xdacosibJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eedc94ace.mp4?token=U6rlPUTUPEGMINsl4hZeTf7tL-BYE3FTt8O4ztTPlwm6YHUk9MrA83CzcGSWlEGbeXmzKFCcaQw3u8zOPDzHt3Kc0voESkvvAPl5Yg33vPCXPGwHLpp2xhMdA4J8PU3QnRdltELQ_OGNK3BemTd-Gak4eJ62sxEJWQouJaR0DdPghUiXRRECuowfhJHy57mvoAmarVWk8hTYk2KilbsdOGJLo7nsdk4nHn1cmBOFjll1H5C3uIyssO3lSoTP1z98EoD_Ue1hjqD3C5mw_1L40yHX3ZobZOBwdDHW_xuGr4Py1AYeYtiqzWhkDo5MRicIMiiOl44cKv48xdacosibJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
👤
رامین رضاییان: مذاکره با کادیز اسپانیا؟ صحبت هایی بوده است/  در 48 ساعت آینده تیم  جدیدم را مشخص خواهم کرد. خودم دوست دارم در ایران و هیاهوی فوتبال ایران باشم تا مردم از هیجان رامین استفاده کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/103315" target="_blank">📅 02:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
▶️
👤
صحبت‌های شنیدنی و تلخ این جانباز عزیز؛ امیدواریم برسه دست اسطوره علی‌آقادایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103314" target="_blank">📅 02:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e8aa4ed3.mp4?token=P42nBBsJEsK7jmuif7v5IwYt07k9ixG-fslMjzHAmO7lMbhH-0dDBbvuEPb2KZwB0psFtKo21DwI3XQWn4aSXd2ux8pV2DETug0f0d9cb4VouM_5gD0GyhpzCFQ41QGMpVM54bzp66ioSmnuxGU2_Gmclz4cSBScYmJoARkF9xUItLBKCzkA3Qo5rFMaLgJ9HJJNknLMujsnoHn7oB7E0UTFR7bcbHdtoxJoXaFr67hG7WylP_9EZHEntODx-UmicwMzOEpudXXDGjOt77ioYtomlRbgMmdTivJVoYo14xrdM_cFp3VpvJZZUvdMJqsqVCztxHPkBTALWI-prLVMXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e8aa4ed3.mp4?token=P42nBBsJEsK7jmuif7v5IwYt07k9ixG-fslMjzHAmO7lMbhH-0dDBbvuEPb2KZwB0psFtKo21DwI3XQWn4aSXd2ux8pV2DETug0f0d9cb4VouM_5gD0GyhpzCFQ41QGMpVM54bzp66ioSmnuxGU2_Gmclz4cSBScYmJoARkF9xUItLBKCzkA3Qo5rFMaLgJ9HJJNknLMujsnoHn7oB7E0UTFR7bcbHdtoxJoXaFr67hG7WylP_9EZHEntODx-UmicwMzOEpudXXDGjOt77ioYtomlRbgMmdTivJVoYo14xrdM_cFp3VpvJZZUvdMJqsqVCztxHPkBTALWI-prLVMXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🔵
رامین رضاییان: مشکل با آسانی و حردانی؟ من برای یاسر آسانی آرزوی موفقیت می کنم/ من همه بازیکنان استقلال را دوست دارم. با همه بازیکنان استقلال ارتباط خوبی دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/103311" target="_blank">📅 01:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5-9t3pM1vzIyz8opMrDgz5UHC-9J87w6mDTKu7iiYhPHe9Hpc53gfnooI19hmSEqKHOpdE1bQotxxDQRIZWhQSjX9m5yGp9Wodl1W-hi5QwYbY5-QFg7PULO-tQGtXm-Kbz944CXYZ6VnlzNkAVPHcpoxq_O0UztJ57Ouwajda1EmB3QeZbloxh5VKW9FLCt8Ln9Lsfp9Lq_Dom0Pdzm6xoMMbBmilqz_z0cm81ofo4DFsr_ukciKjjEO3tGUKKgCp84CxY3ZyXohYOhXHXvK1bSLd4Oyaw9Uu5BsguGvROjKrzA2TDPvRrGi8sPtOGND6Evh8zHkXsSIxmbGx64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری کنایه‌آمیز لحظاتی‌پیش یاسر آسانی با صالح حردانی، هم پست و رقیب رامین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/103310" target="_blank">📅 01:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103309">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b865ccd71.mp4?token=Q-IeXVs6wVCytKXLYpKExONTWVmDWmUdcM0gO8TTPh6WyqQ0u5RzGhRleifD1zeWKe0SGDqyKruuHmYa0Qcipmo4NVohTqO3Mds4U0ibcNDf7yQnVM_SzjqYwAtDDdu4tr7pMAzp0RIbNQTn6W0Rk8WlibgefIz7l9nsmWvJ6hhmkZlz_U2dl3yWAyRx_nbZQzuEvCTNBf9rdNxOB-WCUwFhMNrr0o6N3WV6cUwHV710Na64a4zRov9IFPJKt-s-lSdXGdw7H2ZWZJfWWXOav9bhjI1cuxYGwEADHgkgjY0TXQWtkRDU21ANess321JNJYblY-L-TEr2YrecB0tQ31MHX-kj4LXrpAa4KOlxHY9rYQBTf0Yd0VjK6Fk0FqVhezntH03di9VpW7hihj3X9iS1PyeHytTxwgR9kPa_Onh3I-30se2xPQPsepeP0X5K2ci5IP4cHBSr5WK-Yw9KZrViD6zy_d-VF6L9vH6bPQSJU62eTbcKeOR4goukh-kB6OefSEBvQFm3BQdyugO4RFoFdYnZvpRCSN0UCHPV1bBXAUmIMqWfwoh6r1Dnzkubs71Is_OeDylRAee0x_fVrXWhCydZw0DloxmqtXaFndQtCF4lOT3Vcl8FF91wqWDlZY0FK0wZZcYsSsYaG2bpsoUEJtKdL5IwqM36cTB-u6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b865ccd71.mp4?token=Q-IeXVs6wVCytKXLYpKExONTWVmDWmUdcM0gO8TTPh6WyqQ0u5RzGhRleifD1zeWKe0SGDqyKruuHmYa0Qcipmo4NVohTqO3Mds4U0ibcNDf7yQnVM_SzjqYwAtDDdu4tr7pMAzp0RIbNQTn6W0Rk8WlibgefIz7l9nsmWvJ6hhmkZlz_U2dl3yWAyRx_nbZQzuEvCTNBf9rdNxOB-WCUwFhMNrr0o6N3WV6cUwHV710Na64a4zRov9IFPJKt-s-lSdXGdw7H2ZWZJfWWXOav9bhjI1cuxYGwEADHgkgjY0TXQWtkRDU21ANess321JNJYblY-L-TEr2YrecB0tQ31MHX-kj4LXrpAa4KOlxHY9rYQBTf0Yd0VjK6Fk0FqVhezntH03di9VpW7hihj3X9iS1PyeHytTxwgR9kPa_Onh3I-30se2xPQPsepeP0X5K2ci5IP4cHBSr5WK-Yw9KZrViD6zy_d-VF6L9vH6bPQSJU62eTbcKeOR4goukh-kB6OefSEBvQFm3BQdyugO4RFoFdYnZvpRCSN0UCHPV1bBXAUmIMqWfwoh6r1Dnzkubs71Is_OeDylRAee0x_fVrXWhCydZw0DloxmqtXaFndQtCF4lOT3Vcl8FF91wqWDlZY0FK0wZZcYsSsYaG2bpsoUEJtKdL5IwqM36cTB-u6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: کوچک تر از آن هستم که بخواهم بازوبند تیم استقلال را بر بازویم ببندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103309" target="_blank">📅 01:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103308">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e54f7dedb.mp4?token=RtOEaB4zI24HTMs_wEVTuctduBCEEW6bKRjrDVYG48CtJUBk2KJhmIhBNKVx2f2bdDysI2jSDdpkwouY61tz-xqe2PL0RtPYpmhnq8Yj9QLn3BsQxTzYOMpXUnZEEe_YrXRsQa-D22-VK17-xG34xbrJBMwcNqGc-ox2D4YVPVSkOLaBux2NEQxssNuSIeYBOuPUzf6K4mz7NMFJoQuHA9X7HiOovONxUf_XNsVuqF03BDyngkzrZB7WlfOYAUTILSBG-E2lIhc5xBnDiYvkso7HfcPwqRXPDV1K5qI0NYXsQqWD6E1erCmHvOdhe3kziKx7hh9WIyBopE2QqLwJv2m_hulA_6nL1CwL6sQ_Uj4qeauYUEGtcP10H-MzQdLozLYTJ02drvYycKe3DJApMJoM3RQJSRu4eN2wGYadkaRVzp9494CincT1hzrO8jXxZwbEnMTaO2YqpWtokXFpjHyVeVJefCwOgapvL0gNgWAXW6lRgMu57W8PtsSmb4HX-wC2Fx2bd_iaSe3VNLT2YLew3MWOQ-EpoxXPO-iQptGpoD16GQiao8boOvjwXbkJFVT4afnY15XLEMz1xzEuWjuRh8gQQpvOuGKy_hFidwY0unkXexnmETA9BrC5BtkWUvpi4IBGqrP4wy0GDiKLHpiL3Z7AVi4HXBZzKUHNdkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e54f7dedb.mp4?token=RtOEaB4zI24HTMs_wEVTuctduBCEEW6bKRjrDVYG48CtJUBk2KJhmIhBNKVx2f2bdDysI2jSDdpkwouY61tz-xqe2PL0RtPYpmhnq8Yj9QLn3BsQxTzYOMpXUnZEEe_YrXRsQa-D22-VK17-xG34xbrJBMwcNqGc-ox2D4YVPVSkOLaBux2NEQxssNuSIeYBOuPUzf6K4mz7NMFJoQuHA9X7HiOovONxUf_XNsVuqF03BDyngkzrZB7WlfOYAUTILSBG-E2lIhc5xBnDiYvkso7HfcPwqRXPDV1K5qI0NYXsQqWD6E1erCmHvOdhe3kziKx7hh9WIyBopE2QqLwJv2m_hulA_6nL1CwL6sQ_Uj4qeauYUEGtcP10H-MzQdLozLYTJ02drvYycKe3DJApMJoM3RQJSRu4eN2wGYadkaRVzp9494CincT1hzrO8jXxZwbEnMTaO2YqpWtokXFpjHyVeVJefCwOgapvL0gNgWAXW6lRgMu57W8PtsSmb4HX-wC2Fx2bd_iaSe3VNLT2YLew3MWOQ-EpoxXPO-iQptGpoD16GQiao8boOvjwXbkJFVT4afnY15XLEMz1xzEuWjuRh8gQQpvOuGKy_hFidwY0unkXexnmETA9BrC5BtkWUvpi4IBGqrP4wy0GDiKLHpiL3Z7AVi4HXBZzKUHNdkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
رامین رضاییان: من یک سال برای پرسپولیس رایگان بازی کردم/ برانکو من را نخواست
سالی 2.5 میلیون دلار از الدحیل گرفتم/ دو ماه حقوقم را بخشیدم به پرسپولیس بروم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/103308" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103307">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926f821e41.mp4?token=Y77CVMH3Yd8khlIbqBJQ9VQtvNowQrYko1Afcr6EjfFtNlesXa0_3fmBIN-jXKPocmQUkr23FNGTmR1kycciDJ1ivrhPhC1Z8h1Q_bSdQ0bSfKYZ1nZqaIw2a47ixZ3yf0N9SGanB0lypuK81KAA-kKkl0VgYfyIvHoPCphgZ6LAZjGGoA5Hb4dwAnCjp3ICeLevekof60D8zIQTusIBAWQAkogjEupzh8YQKNPYh2p4oVEir4kjw7z64MEgVHZHNoLoYYeJ6MWOsJNJKm0O4EiY0YPVA0jEreiLsGrXReEKXK-KT9Y6JHkZEbXDI7iAJc6qz18xDdKqFIrKLKqF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926f821e41.mp4?token=Y77CVMH3Yd8khlIbqBJQ9VQtvNowQrYko1Afcr6EjfFtNlesXa0_3fmBIN-jXKPocmQUkr23FNGTmR1kycciDJ1ivrhPhC1Z8h1Q_bSdQ0bSfKYZ1nZqaIw2a47ixZ3yf0N9SGanB0lypuK81KAA-kKkl0VgYfyIvHoPCphgZ6LAZjGGoA5Hb4dwAnCjp3ICeLevekof60D8zIQTusIBAWQAkogjEupzh8YQKNPYh2p4oVEir4kjw7z64MEgVHZHNoLoYYeJ6MWOsJNJKm0O4EiY0YPVA0jEreiLsGrXReEKXK-KT9Y6JHkZEbXDI7iAJc6qz18xDdKqFIrKLKqF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: چه کار کنم که سنم 35 سال است ولی اندازه یک بازیکن 25 ساله دوندگی دارم؟ چرا همه زوم شدید روی رامین رضاییان؟ چرا می خواهید فوتبال من را زود تمام کنید؟ چرا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/103307" target="_blank">📅 01:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103306">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f842dcdc91.mp4?token=AXDlQQLf9RmWfME5hdzvz8WnY6CEdElVHBARVUj4tfnS4eZ498-TO4PwQzoWOOdsM9y45ZzYjhdXcZNmC-aaBlkRwrXofImQ3lai52xCt_lnzyDw_oINeeVg3Byp-tUJ70dDAKHPsKkBOE_XI00L2IooKa3Ao84uwKQBPSwGvw8L-sdOrHpp678CfxNbKr_fF3Ki_uqEGd3vtX97SjUWUOQwYtFZ6KwexrRnvggV7DaOCABt5zjQ4ifFXCv-mOlOS8kzCdNWdro_BaUL0sdgKbTp30qhkEIHn1SYdgFp5wInm9l1PsSbySg3B0niuhu4bF4l4rFIyvrmBHwd13rbHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f842dcdc91.mp4?token=AXDlQQLf9RmWfME5hdzvz8WnY6CEdElVHBARVUj4tfnS4eZ498-TO4PwQzoWOOdsM9y45ZzYjhdXcZNmC-aaBlkRwrXofImQ3lai52xCt_lnzyDw_oINeeVg3Byp-tUJ70dDAKHPsKkBOE_XI00L2IooKa3Ao84uwKQBPSwGvw8L-sdOrHpp678CfxNbKr_fF3Ki_uqEGd3vtX97SjUWUOQwYtFZ6KwexrRnvggV7DaOCABt5zjQ4ifFXCv-mOlOS8kzCdNWdro_BaUL0sdgKbTp30qhkEIHn1SYdgFp5wInm9l1PsSbySg3B0niuhu4bF4l4rFIyvrmBHwd13rbHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
رامین رضاییان: مگر می‌شود بازیکنی مثل من اخلاق نداشته باشد و 8 سال در تیم ملی باشد؟ چرا دل من را می شکنید دلم شکسته است چرا من را جلوی هواداران می گذارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/103306" target="_blank">📅 01:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103305">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abb1415693.mp4?token=YaJ2dj7jY1JLwYFNcouj2bkmFzpscoc_sxY0lzNjNLOn-6KpPapwOY8eQ-IM9py0JrUAfNeCg3QRvPEmY-C21rq7RtOW_v7815geLTMllpMrbRiEumHhX9UDAwpvIIvoimLsCHFMdcmCDuJqUwpxaOHYiAYpn1Ls7nvDbsHPr56QNqmYOQAbdZ5YYOqPK_8q2QMo8OfcNTG5ZwOr2o-HG87QhbbV2-hwXvEY9CezboGAbhPORU6nDCOfkOq_dyOLUkVmwKzpbEiK4nlSy_Z0aynRR0oBl_XjneFlhZTlsVwDGYr-pjxY2RNDIfI1HEVbdUm3gWWbi9z36qMbtgz6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abb1415693.mp4?token=YaJ2dj7jY1JLwYFNcouj2bkmFzpscoc_sxY0lzNjNLOn-6KpPapwOY8eQ-IM9py0JrUAfNeCg3QRvPEmY-C21rq7RtOW_v7815geLTMllpMrbRiEumHhX9UDAwpvIIvoimLsCHFMdcmCDuJqUwpxaOHYiAYpn1Ls7nvDbsHPr56QNqmYOQAbdZ5YYOqPK_8q2QMo8OfcNTG5ZwOr2o-HG87QhbbV2-hwXvEY9CezboGAbhPORU6nDCOfkOq_dyOLUkVmwKzpbEiK4nlSy_Z0aynRR0oBl_XjneFlhZTlsVwDGYr-pjxY2RNDIfI1HEVbdUm3gWWbi9z36qMbtgz6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🙂
رامین رضاییان: روزبه چشمی 7 روز پیش با من تماس گرفت گفت چه خبر؟ گفتم هیچ کسی از باشگاه استقلال با من برای مذاکره تماس نگرفته است، روزبه گفت من شب با آقا سهراب صحبت می کنم خبرش را می دهم، هنوز که هنوز منتظر زنگ روزبه هستم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/103305" target="_blank">📅 00:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103304">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/853e2a52d7.mp4?token=nSH_QH_RVeZJaKotMDjJsjxo4Do4V6UxzFhznIkpSNCiPtQuXdzhVMNg3-8RoVZ7xZgqwlbM3WAuwImhQ29O8LzD00oZ1T9ck7sdpNtQQ7PsrrF2gCzEjIcoeHI_jFouiBpMY5uooHNwRUvoM5RhOeeasNqKX0KD3cVPW-1cRHjyEjtYBOEyoCA_aVH3rQkg5RLT6Sm27ff2SOH7UriWKbJf96w3Fw5mD_QTx-S-bY7e0o1HLuP2I8lInQGJphEYp13GKCn7rG77lAvJSWzilLXy697r4x-Zdg7dV6B8hUKrOz3uuzJBuoArYC1RLRlRkI7CEmkdKeB6d67YIzwncQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/853e2a52d7.mp4?token=nSH_QH_RVeZJaKotMDjJsjxo4Do4V6UxzFhznIkpSNCiPtQuXdzhVMNg3-8RoVZ7xZgqwlbM3WAuwImhQ29O8LzD00oZ1T9ck7sdpNtQQ7PsrrF2gCzEjIcoeHI_jFouiBpMY5uooHNwRUvoM5RhOeeasNqKX0KD3cVPW-1cRHjyEjtYBOEyoCA_aVH3rQkg5RLT6Sm27ff2SOH7UriWKbJf96w3Fw5mD_QTx-S-bY7e0o1HLuP2I8lInQGJphEYp13GKCn7rG77lAvJSWzilLXy697r4x-Zdg7dV6B8hUKrOz3uuzJBuoArYC1RLRlRkI7CEmkdKeB6d67YIzwncQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
😐
رامین رضاییان
وسط برنامه پا شد لباسشو نشون میده میگه ببینید بخدا نه مارک نه هیچی، منم بچه کف خیابونم فقر کشیدم، ببخشید اگه یا تیپ و استایلم دلتونو شکوندم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103304" target="_blank">📅 00:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103303">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0631b46480.mp4?token=eGfBPO3t47fhEAzuz8_w3nEzgROe1EE7x3GL-5I2P_ieQi4YInc6lvt4bKL9QGrKTPrBP83Hpg7ERIN45ZIh-4OCqICGDv1ELYJOdTW0X81fquVfHAyMeBvxqUXLdMlaWPoM5Gzb0ixVZayv_K-_qf-QZXmu6uEmh3Okcy3UoSjXbegaI6445nM7pEKBvfL4pLorHHAHJ5dUx68kKM7XV_Bes7kwok1j7GrAO22z_yKyacyVBfLvbe8DIA9pvuyFhYUFugn3QgwPdH_9alE7auXBHDDO_HsDO6yn5HPFCL5_GAa5ZIPkAnTLb7v-bEIuUNIQp_mT-Lw1wx8QG_t8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0631b46480.mp4?token=eGfBPO3t47fhEAzuz8_w3nEzgROe1EE7x3GL-5I2P_ieQi4YInc6lvt4bKL9QGrKTPrBP83Hpg7ERIN45ZIh-4OCqICGDv1ELYJOdTW0X81fquVfHAyMeBvxqUXLdMlaWPoM5Gzb0ixVZayv_K-_qf-QZXmu6uEmh3Okcy3UoSjXbegaI6445nM7pEKBvfL4pLorHHAHJ5dUx68kKM7XV_Bes7kwok1j7GrAO22z_yKyacyVBfLvbe8DIA9pvuyFhYUFugn3QgwPdH_9alE7auXBHDDO_HsDO6yn5HPFCL5_GAa5ZIPkAnTLb7v-bEIuUNIQp_mT-Lw1wx8QG_t8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
رامین رضاییان: من قراردادم را با استقلال فسخ نکردم؛ باشگاه استقلال با من فسخ کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/103303" target="_blank">📅 00:53 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103302">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0b3587c2.mp4?token=Rt0jz9Km-P8b4uQoPaC5CBcOMcg-b04vpnRcUACx6HuqEjjjfzotxfKDvE3-3L-vYS9K29Kwm_iJA6g3fb8A1yyQvz9eFhI5H_rTqu28MTcDE8mAyz2YjxfqQbLj9d9aqxBfdvo9nYjJoKvNpE2UNpLX6j9jxdNYuxh8_M0TcPBDPusUHqGmlF0_o66Fa5tcSYxnphMl9dVcR0oIuHfwZtHixGsbCAyHhD4nWeoalPx-CkVKPz6tngs81ol-iBhOOzosOaatyiVcARfpWJf4naS4P8DnTxG9puiPfCbx1X4C4VDpd581iCS78wqUpqqpvx0juN5hfvzIOfAZKmPcgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0b3587c2.mp4?token=Rt0jz9Km-P8b4uQoPaC5CBcOMcg-b04vpnRcUACx6HuqEjjjfzotxfKDvE3-3L-vYS9K29Kwm_iJA6g3fb8A1yyQvz9eFhI5H_rTqu28MTcDE8mAyz2YjxfqQbLj9d9aqxBfdvo9nYjJoKvNpE2UNpLX6j9jxdNYuxh8_M0TcPBDPusUHqGmlF0_o66Fa5tcSYxnphMl9dVcR0oIuHfwZtHixGsbCAyHhD4nWeoalPx-CkVKPz6tngs81ol-iBhOOzosOaatyiVcARfpWJf4naS4P8DnTxG9puiPfCbx1X4C4VDpd581iCS78wqUpqqpvx0juN5hfvzIOfAZKmPcgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رامین رضاییان: آقای تاجرنیا با وکیل من صحبت کرد و گفت من رامین را دوست دارم ولی..
میثاقی: ولی سرمربی استقلال رامین رضاییان را نمی خواهد
رضاییان: خب این را نمی توانستید تلفنی به من بگویید؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/103302" target="_blank">📅 00:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66453415a0.mp4?token=MdUscSalQsgMWoerbbVpjZEbyQxnGpiaG3B9dy1M68jrGURnvlwkAp1bE20KQAIFTHODhEGNmY7vE_iiUXwlmBAycecg1x9q-89a_5U4qZdEX3MSsY_EqCVJLcqCVwp0lYixlW4HRrYRviGT9xzymmAfgk3L5hpPDVpmgLmdQpKw0cEYvxOwt7OJAZ051QsHbfzJ6uSzhSIdD_u0cC6tj2R1dLzfat7xiw4UjiE95Om3MhE4_DHD6vJotSM7Bm_E8gKXcz_B4F_AaTVjbfyjyT6k5GqoKPV7TX72CddxVR82wiE0ren2EqRTytU9z5SfgBD5w4OKpxY_asJ8AdGLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66453415a0.mp4?token=MdUscSalQsgMWoerbbVpjZEbyQxnGpiaG3B9dy1M68jrGURnvlwkAp1bE20KQAIFTHODhEGNmY7vE_iiUXwlmBAycecg1x9q-89a_5U4qZdEX3MSsY_EqCVJLcqCVwp0lYixlW4HRrYRviGT9xzymmAfgk3L5hpPDVpmgLmdQpKw0cEYvxOwt7OJAZ051QsHbfzJ6uSzhSIdD_u0cC6tj2R1dLzfat7xiw4UjiE95Om3MhE4_DHD6vJotSM7Bm_E8gKXcz_B4F_AaTVjbfyjyT6k5GqoKPV7TX72CddxVR82wiE0ren2EqRTytU9z5SfgBD5w4OKpxY_asJ8AdGLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🟠
🔵
رامین رضاییان: رفتنم به جام جهانی را مدیون باشگاه فولاد هستم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/103301" target="_blank">📅 00:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c728b778f4.mp4?token=DvDMHrFIBXiWOGI0fDlXfRshFJKt5j5z011G9kIge_MRpuE7fKpGQ95a1SXnwv0r7POP5UpO53c0EP0V9-qhkdt6n36uSvhinTTKjz1JcH2m81wbAvp52EjJZ7O6Cz8n0EsK1PvFmyvJNFA5q_CGbWxVgqcH07AP1M2ehT6JoStcXH6G8jVQjKg0uX4nGEEHdgfgE7KdPN6ojTPLS04tWm846yJWPQRp1IhjkebVeYWkt4MMh6O3BIgTIS0_BYXlavkRMfSO_UHPurw_ZJMXTVm9b2PHfa_pbEjGSXIPfJY9l7Ud8eqKB10P623bmUI_KiGT-tjrurNfPC37_6FwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c728b778f4.mp4?token=DvDMHrFIBXiWOGI0fDlXfRshFJKt5j5z011G9kIge_MRpuE7fKpGQ95a1SXnwv0r7POP5UpO53c0EP0V9-qhkdt6n36uSvhinTTKjz1JcH2m81wbAvp52EjJZ7O6Cz8n0EsK1PvFmyvJNFA5q_CGbWxVgqcH07AP1M2ehT6JoStcXH6G8jVQjKg0uX4nGEEHdgfgE7KdPN6ojTPLS04tWm846yJWPQRp1IhjkebVeYWkt4MMh6O3BIgTIS0_BYXlavkRMfSO_UHPurw_ZJMXTVm9b2PHfa_pbEjGSXIPfJY9l7Ud8eqKB10P623bmUI_KiGT-tjrurNfPC37_6FwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🟠
رامین رضاییان: آقای گرشاسبی مدیرعامل فولاد برای جذب من با پای خودش به باشگاه استقلال آمد شاید هیچ مدیری این کارا را نمی کر
د
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/103300" target="_blank">📅 00:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103299">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKc2HT2EyMfX-GmsPmNLYYye59WmOoOS3lIIVbYuK_WLhYwJ2tczmStmpCnTNUTCSG_9fK5HyYWRMsEoN9wV5MHyUaIj9bPF7YJI2tJfiOBknHpDwObtN-er3u558wpgrEgi4VXlQZqO160Cw8C-FhfBq-pQclz29IWyqVkdbrui4keSAYX7aK8yAQYgbDEcGlXLTDizTmUhtF50SAaZME-76dmlkbjJ4g1DaL84_NvJLwPcMX13PtkZ4xb9zigedEiYPgRfIJx6EByBXpwBqa778bnfpORb5jFvscCrSKGGkbr25h7GZzqT1RkxL-M7EAoe8A6A9D5qHh6Na7ovvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔵
#فوووووری
؛
🔺
هلدینگ‌خلیج‌فارس اعلام کرد که سهام باشگاه استقلال بزودی به چند شرکت یا شخص متمول هوادار آبی‌ها به فروش خواهد رسید. مذاکرات در این زمینه آغاز شده و بزودی نتیجه نهایی به مردم اطلاع‌رسانی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/103299" target="_blank">📅 00:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103298">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9ef8ef85.mp4?token=UtJCIlEVlALKYtOoXcCGGla3ObOJ2t4DV2i3O5gnwkeB3XUwCvimpEEy3T4lgtrYoRfOkBTREbJm7bzH_3bt31nBctb4SbI1_u1CauBpj1qCGKTzAeVoPGXOekdaBQ2Oa8GhsI4qphJQ0Dk_jSgVY6ZUL2N7td2k6m9jF346har5yDqwf0wUADQ0J76Yl4-VjwDnr2ilxUvvq9R9jBA1MKdyatXIBvrDsBXEewnK410yq9x4uiPdGzuiQN_ypPIGsscvWgDlIGcmym3huc5MI9DMmPek3kzY09cfGO7Dk8B5LEIpgHjG4Q0tBqggSaX4zip3o2sIwNi2pl-rj-zbug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9ef8ef85.mp4?token=UtJCIlEVlALKYtOoXcCGGla3ObOJ2t4DV2i3O5gnwkeB3XUwCvimpEEy3T4lgtrYoRfOkBTREbJm7bzH_3bt31nBctb4SbI1_u1CauBpj1qCGKTzAeVoPGXOekdaBQ2Oa8GhsI4qphJQ0Dk_jSgVY6ZUL2N7td2k6m9jF346har5yDqwf0wUADQ0J76Yl4-VjwDnr2ilxUvvq9R9jBA1MKdyatXIBvrDsBXEewnK410yq9x4uiPdGzuiQN_ypPIGsscvWgDlIGcmym3huc5MI9DMmPek3kzY09cfGO7Dk8B5LEIpgHjG4Q0tBqggSaX4zip3o2sIwNi2pl-rj-zbug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
✅
رامین رضاییان: با جان و دل برای استقلال زحمت کشیدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103298" target="_blank">📅 00:03 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
