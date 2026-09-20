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
<img src="https://cdn1.telesco.pe/file/f2-cPe6gRJAy8VjabVf1BNRDNRgcwXbT9UJWzv4jpTNa66ARVhdUvcojSYrtQePDtH1SJCt7shY_3S4vA6z33-3tfWdoVHRVQDbcF1yeJ2CGxPbNDbeLxrzvgiXlZ03Py25GYR2jDRukaXdjO1RwooXnybYusq93GvIRkKXnqR5fI_IYcWcANtqbgnxrXnmDWpzlIVRV-bBIHuEutby2nlL6d0vw82gzFBZri-MqVjPl7ZV1lhz2vBTgICYwj9y34efQ_0r5MG45rvk1n371yRtk6Qgu3nJ4IvjRh6PIaHy9ZWVDP15jE-3TJhdWIRBULEbm1YdLz7xHbsP7SBp8gg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 04:00:47</div>
<hr>

<div class="tg-post" id="msg-5278">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OxNEs-Uqmc7ALFBtmvVFtg-E6HVtIa2a_YdW0FvbGlD9VosPH6UeR1bjykLG8iyQ2D3jo9pck5HdjwhuCm2OIQUEw9LOMuJCYjt_BZfU0u7B_HR000ae1vHmV2QP9_e427dIZafVgmp0n7HET0tzRu-ans_Q5noUmCYOJgRm08-5Obf14q5sg5_KsuWMPcLviXqbC5TtAwfgEwFKj_8SPiHDcjd_i_4cczXmZBbh7jx2QvWu-ULC7ptSu8BjNMZfl8-HG0ji00Mrb6zmrLkjDMxdSrcCCnkBvZmZyj2wAyX6Py0Hqh-ZDKfh_Jxq9zYhGrCpfZZBNTxtyvfM0UOOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیلی که توییتر رو دوست دارم:
(اون روبیک Graph خیلی خفنه فردا می‌ذارم فیلمشو)</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/MatinSenPaii/5278" target="_blank">📅 23:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5277">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به زودی برای پروژه‌های اوپن سورسم هم آپدیت میدم بچه‌ها
هم Aether gui هم اسکنر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5277" target="_blank">📅 21:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5276">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کسایی که ری‌اکشن
😁
می‌زنن آخر این ویدئو مسج رو دیدن
😂</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/MatinSenPaii/5276" target="_blank">📅 20:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5275">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=XbhhmcoBaBoMM7YATVKEvJXQf6NoPCXlsCYVZJXeLggsgu5fp8tyjJTNgQVWCcGVEiPsw1LPYeZ7F2UldAeZvKsyQp3sPJNpP5xQMFSctuWf4Loikxy0ZYpurxw7FTYDpGhxmyndZWtmXT1A9VjLgBalG9I5xKR-3U0uDrI3KRwT9rKWywasuKVbTITGtZJYsxKAM731rhzErmKcUR9tSPvOu7WYwrs0FLZyoBiRIKVX60BQr0YxT_etryXTSjOrMip2DhMm-Fd_RKWStTxvgs0IqtmOY9wRQvJ7yP1yixnO6ByWvx74jMN1kqO3h7Q0hzN4oreZKPkJ_F_45vgbCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/760da1b5cb.mp4?token=XbhhmcoBaBoMM7YATVKEvJXQf6NoPCXlsCYVZJXeLggsgu5fp8tyjJTNgQVWCcGVEiPsw1LPYeZ7F2UldAeZvKsyQp3sPJNpP5xQMFSctuWf4Loikxy0ZYpurxw7FTYDpGhxmyndZWtmXT1A9VjLgBalG9I5xKR-3U0uDrI3KRwT9rKWywasuKVbTITGtZJYsxKAM731rhzErmKcUR9tSPvOu7WYwrs0FLZyoBiRIKVX60BQr0YxT_etryXTSjOrMip2DhMm-Fd_RKWStTxvgs0IqtmOY9wRQvJ7yP1yixnO6ByWvx74jMN1kqO3h7Q0hzN4oreZKPkJ_F_45vgbCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/MatinSenPaii/5275" target="_blank">📅 20:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5274">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">از اینجا می‌تونید به عنوان میهمان وارد شید: https://live3.eseminar.tv/ch/wb182512</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5274" target="_blank">📅 19:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5273">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/MatinSenPaii/5273" target="_blank">📅 19:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5272">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91ae01bef.mp4?token=C4iy03cL0WP-5loQEIs7rYL_09i9OuQ-IMOtCLXXSYZC6ZwV_7oiVQZn8X-iNfvBv_AhbR_LWkzHzOgHwGLlm61GWN3-Tdar1mGnUPwkRjKdERhQVU-Y5GNv-BtxFlqBCfI9-iHKG2nzIkqd06H9Zd2WRx6EiRSmBI_X9ygUZc7W5BbAN3KitLIOd4o3v35Md9WoRlxfEmZb1OaGX1O5FzB7iKWFPQ7awkvQcY6o_X6g60GcTQWc5o_MqbOxa6LEvPmUdMtS2ZGjAj3zXye6DKDgfrUKZPOC1sSJmjB4KM86HJUXfIrF4iYa17IZZA_cDLFW3Hqqw3hvSzBRSLp3-W3uczXkwYNO78Id1QcuDj88gLXQL6qkue5ctvrd51q1jyTt3q_03Qz-fR4uej0flBU5REDI24pUXM47rxg5g86zE1dnfqaaKxQYFVz72gK3RmZtDT1t-1p1uSt1-jj2mGEhuyq2P78xeZGYJ6gTnI_K4M4RkzkvqUvD5WmFhEEHMO02iggukv8ZnP0CQNKnTHEvc8PDA6CKs_Ohlokf7l3Z4tjN3cf7Y1jCSrwNeDy3-9G8PWCR2qsqrqEl6c715AaRLpnHrU1-IRY0ABQdTA5xohBcfSuICKZKLzQhoZUjA0wcrSu6FW6sNqJAJU8GlzSfRaaRYvRBVUxtcGsBFZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91ae01bef.mp4?token=C4iy03cL0WP-5loQEIs7rYL_09i9OuQ-IMOtCLXXSYZC6ZwV_7oiVQZn8X-iNfvBv_AhbR_LWkzHzOgHwGLlm61GWN3-Tdar1mGnUPwkRjKdERhQVU-Y5GNv-BtxFlqBCfI9-iHKG2nzIkqd06H9Zd2WRx6EiRSmBI_X9ygUZc7W5BbAN3KitLIOd4o3v35Md9WoRlxfEmZb1OaGX1O5FzB7iKWFPQ7awkvQcY6o_X6g60GcTQWc5o_MqbOxa6LEvPmUdMtS2ZGjAj3zXye6DKDgfrUKZPOC1sSJmjB4KM86HJUXfIrF4iYa17IZZA_cDLFW3Hqqw3hvSzBRSLp3-W3uczXkwYNO78Id1QcuDj88gLXQL6qkue5ctvrd51q1jyTt3q_03Qz-fR4uej0flBU5REDI24pUXM47rxg5g86zE1dnfqaaKxQYFVz72gK3RmZtDT1t-1p1uSt1-jj2mGEhuyq2P78xeZGYJ6gTnI_K4M4RkzkvqUvD5WmFhEEHMO02iggukv8ZnP0CQNKnTHEvc8PDA6CKs_Ohlokf7l3Z4tjN3cf7Y1jCSrwNeDy3-9G8PWCR2qsqrqEl6c715AaRLpnHrU1-IRY0ABQdTA5xohBcfSuICKZKLzQhoZUjA0wcrSu6FW6sNqJAJU8GlzSfRaaRYvRBVUxtcGsBFZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه! به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید: https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5272" target="_blank">📅 17:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5271">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدل Jev واقعا چیز جذابیه!
به زودی راجب این دوستمون هم ویدئو داریم. تا اون موقع می‌تونید این ویدئو رو ببینید:
https://youtu.be/2z-7pIj57f8</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/MatinSenPaii/5271" target="_blank">📅 17:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5269">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hyu4olEskT6rpq1hTPhZhZ69WzW2Xcrn-N_M2BFCIYABjmLwxjy7tQ5ZclhocMz2nwMRozHEzIsgjUWbxHAt13zT0NpW2pQKgW3Rz1dy4iAsglqmjh6jYAAc3GWDwXcyAWdUrSd-tLWEru3gMp9nibMFZv0gU5Tya_Rw2E8rMcmMIIDhuz7wp23J1h-4xKjxL-tAx1qngtfx-kKuuVLY-JlEVUz6oGqo6dX3wtjB9zAqgoki2SvpytVxMOw5NnXlhWdge4V8GHOJ5839a6v9X-EYw32jeSwA1-3G_eCTucuOXrjHUz_FJPpD-0Q4zLFpfte4WAVHmlIgjbhwUtW62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EKcVedojF1zaUOFmEndq38MiGgfWjYHAK5Kxwl-1K_VjdU1-i-C5VoLrBFGTZyHjzivBPfX-R6By5Kh2lSVW7o7HfLiW6LTfwa08CGNd-qpY1Gats10WiaOkxj9wnll3347twSnhsWdAbHQEQ0uG8xi8pFHYTCbPe-8Z4LFW1rDh6_RqDgpmjHnBDOpC5-CuVmiU9kcDWKckh8PS3j6ipW7u0RUrpXuwiKzsE29D4zsVjGJEUjzwvPEDumeDv1xy7mV_6mhCq2opfe04DEbTqQZPAXwT6sWF7S4EZIHaUDjTEXlZUXRUXvA6O8JYITpGMkuFtm4aNEEYvtjlPnTd7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه برنامه نوشتم برای اتوماسیون بررسی کامنت اینستاگرام با AI(با مصرف توکن بسیار پایین، ویژه هندل کردن تعداد بالایی کامنت) با امکاناتی که شاید جالب باشه واستون امروز توی وبینار BoxAPI میریم سراغش و بهتون توضیح می‌دم چطوری نوشتمش و چه شکلی فرآیندش از ایده تا درآمدزایی طی می‌شه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/MatinSenPaii/5269" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5268">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/diLyjPRVKb-l-1xE1L6R8ILxQah0QHjRU0bwVPyxFoJR1lIpc5s38f1uRfG_1PabOfuwNp1N42JY_KTK81_C_-eA-f9XmOg6GWz-PH_KLpBymyEdW5fvVM3higI-BD5WS6BP6BToD9rNmvXlZulUfLNXHbX2Pg_C4alztlrExGq3t2poexAvzg1-Xpza77TR25QMJBkqiMHl-RnHNof_DXJ-j2cY4c2D6liNmIczL_f12K9LjE0OTdrn0I47x6gIND1nyf96i3llGf-1yRrlHFRU5f1QnaE2X9l57Elq7kG8FfbQHIaYNlLE7lBAN_ihNdEDvlyIep3A0FVa-zVoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Z.ai
مدل GLM-5.3 FlashX رو عرضه کرد؛ نسخه فوق‌سریع 5.3 Flash با سرعت 200tok/s!
​• کانتکست: 1M
• مالتی‌مدال نیتیو
• اجرا روی بیش از ۱۰۰ هزار تراشه چینی ​انتخابی ایده‌آل برای ایجنت‌های کدنویسی و تسک‌های بلادرنگ.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5268" target="_blank">📅 21:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5267">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kgUxxTTrxzLWgth1D4LrvTzeH_qR7QM38TyQ5cgKQQbdkcHEX3Cfig-_rjIFdKX-7_Qcimdd6NvhRnJSJlDT12N0Mdf5GMHcvBWHgsRRLqSnqcQ_oJRlcWGrXojWPbnLoCSuypHMwQSe2Y7DuPCfYYsaRZiiSI1UrY-0JswsnXbyDf89TnMPVLNETfeVERNYlECtY9ApKpBSgqltltfcWyq9aaMwkM6js7Tbw0aVLbPFquzXMvqacFPXv8mIPN-P_lbVQm3lwUSDoHSwcASgexpXcdsKmFeqn_kF8HeXhtDrRT9byrYGl6MSWceTPCpUCcaS_ePBsvsqJ78qseVA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همینه که میگم API نمی‌صرفه
توی 40 دقیقه، از پلن 20 دلاری کلاد که با این روش:
https://t.me/MatinSenPaii/5201
گرفته بودمش، نزدیک به 15 دلار معادل Raw API مصرف شده. اما کلا 7 درصد از محدودیت هفتگی من رفته. 4 هفته هم داریم، 15*100 و تقسیم بر 7 و ضرب در 4(هفته) تقریبا میشه 850 دلار استفاده. با یه پلن 20 دلاری. هرچند محاسبه‌اش به این سادگی نیست اما یه دید کلی میده
(با پلن 250 دلاریش تقریبا نزدیک به چند ده هزار دلار سوزونده بودم قبلا)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5267" target="_blank">📅 21:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5265">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nh1paAsYUSaag3fetimsJGQepB4DD6VJuo9ESIGyxnsJjEMv1YfoCePzDZIbZu-tuJF5gS9F9Msv-r7HuDtwEN-upuVdML6AwmKmegro-soqDALxTebduI_pLGyNzAQKiz3tdsfKCxI5kORSyvdP6keCliKVPu-OHJ2kWVgLBoqcoJr9wOR9MEGUJ3F5pCYuWGimjPioUjIIFTmR6FzDUDDRTvgTbg_6aOTaXoFD01I9YFiCJ19Eso-Fac4iGM5OWT33XKCLwmxoxyLAeKlRcq63QZdqF3sZavssBIEc5Xt8LWh4ryVrdPntIWMtyU-puTU0nLSzxpN9uDfLwmxkhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ipdXB0KMZluAOz5zvuGN3E5nWfeNBksTWou-e242CVU0RrKUriDn-Gri7e-04WKbYTQkhiXtaPz5UljQw-izfKGgI947VoLpeJtbtOFs52nhDLJ6tOgz0LxS1gXmKIGcL1IpPoR0R0jjZgLE6gtgzNMJHGJKFd-OGHyHNlbR8uCE88j0dHX7K8eOkZy0cGE_OErn3QzG993s67EYyaJAz0TzWImtRDD6_zuo_XKs5P1lf-J7K5VdwrWvlSkHSGcR2jAGF14S7Yl_iM1OaVTlymJZLYOd6yD4vWURPU555U1h4uept34iKyBSLBLNYR7z-mNXqGt5_2jEYTY2ZSKE0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5265" target="_blank">📅 21:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5264">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZH5sZTfu9aG616JKfGoO4itDqn_lTezG4UIBikLPPPxp7zPTpWliTpCOUr-iOZHHXUdTVumCy6EPQnq7nyCMPn3_EJCq8HuSCDoGe2gDLLaZ1L1_ODvNYy0kypZKZwsqwxV69pjLLX08hAep7DmX4S2OgAxX4Up2cY9AYpEHdh6LIcwEyj0W3WMMAAP0A8xlWSjJhGz7tX6sKVlIkj4nyhNgbyQQvt51QgLu1SHUPMdsQ6x620XnuhZY8XN8-X1Vp0JucsM0k3yRLRRyOARhs746r2MMKJhSwvQMyhdTGj86Ca9oVBwmusoPzGrv_lM1Ov7EiWh9fGZBFi5lvP1Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا توی آپدیت جدید گوگل کروم می‌تونید تب‌ها رو به صورت عمودی ببینید
راست کلیک کنید اون بالا توی فضای تب‌ها و گزینه‌ی Show Tabs Vertically رو بزنید</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5264" target="_blank">📅 20:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5263">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یه خبر عجیبی که دیدم، هشدار درباره‌ی حملات زنجیره‌ای به توسعه‌دهند‌ه‌های Rust بودش. به‌گفته‌ی تیم امنیتی crates، یه سری مهاجمِ ناشناس، توسعه‌دهنده‌های شناخته‌شده‌ی Rust و صاحب‌های crateهای محبوب رو هدف گرفته‌ن؛ معمولا با دعوت به یه تماس کاری یا پروژه‌ای، و بعد تلاش برای سرقت حساب‌ها و انتشار بدافزار
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5263" target="_blank">📅 20:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5262">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Rq80dU6Igxdnm9ceGT8VglT2aCMgqr1gv9bIfLBfX-n4FC6BnMcKNCYlhsVYgZSbjVkTZppu9Xpo7IP-P4FWi7s3yKwHRk6wFqbg9gZtojDXko5-DOMeiz-8-yrI2gyOJx7wT1mumNHQ-GxAgrr-IfOw84nXs-WPQlo8fVnELtt6DbviiEe-jdwICprAkX3B-SnmJKt3WWgAzdixB7qJi33HMo9fQsb0LYudBhEu_5Kow_10gzVWSR00ReLv2TUzSYd5jJWQ6YQLzBsXLZE9nyFkR5WO1EEXwApOxV70OZekNrYQJL4hkTzqTsaYTeN6G-BNt71CmpTLyk1Rvt0NhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا در خدمتتون هستم بچه‌ها</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5262" target="_blank">📅 16:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5261">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/K3ZANOgo2IJBfyCe6G8QRmGL4zVdLCGEN_6LohHFJuBZUe_3jbOxZU402OuccwfIq9bTl_XbxOLyFVERaxHNWCXS8KZ1KitV_0egGIzWbN_6zaP1bzjiPALRn_qCnNmTIbGsRoITyzsBaYKYf5W8uAOktdFKcxsphJFoqHZ-WzXfaIHKH46BW3UUswv6Eo6WDhbirRDf2IQPAAVU_hJDGFEncIF4SFq-Q7MskdyCEPkMkXLTyHjBf-L-jSF29tNSMEWZxwEwn-hKo7EGasR6-aX8_-49fU7ONG-7oiqqgrBtSREFP-03-u3aJAEEllzag1zZDer0qnRsui3CCnVmbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
;کاتن روتر
چیست؟
کاتن روتر یک ابزار سبک برای مدیریت چند سرویس DNS Tunnel روی یک سرور است.
خیلی ساده بخواهیم بگوییم:
فرض کنید چند سرویس مختلف دارید، اما فقط یک سرور و یک IP در اختیار دارید. CottenRouter درخواست‌ها را دریافت می‌کند و بر اساس دامنه، هر درخواست را به سرویس مربوطه می‌فرستد.
یعنی چند سرویس می‌توانند از یک IP و پورت عمومی ۵۳ استفاده کنند.
⚠️
توجه: CottenRouter خودش VPN یا تونل ایجاد نمی‌کند؛ بلکه سرویس‌های تونلی موجود مانند CottenDNS، MasterDnsVPN، StormDNS و SlipGate را مدیریت و مسیریابی می‌کند.
🔗
لینک پروژه:
https://github.com/TaJirax/CottenRouter
پیش‌نیازها
برای نصب به این موارد نیاز دارید:
یک سرور Linux با IP عمومی
دسترسی SSH و root یا sudo
دامنه یا زیردامنه
سیستم‌عامل پیشنهادی: Ubuntu 20.04 به بالا یا Debian 11 به بالا
روی ویندوز مستقیماً نصب نمی‌شود؛ باید روی سرور Linux نصب شود.
نصب آسان
ابتدا با SSH به سرور وصل شوید:
ssh root@IP-SERVER
سپس دستور زیر را اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
بعد از نصب، پنل مدیریت را باز کنید:
sudo cottenrouter tui
استفاده خیلی ساده
در پنل بازشده:
با کلید Space سرویس موردنظر را انتخاب کنید.
با کلید i نصب هدایت‌شده را شروع کنید.
با کلیدهای Enter یا e دامنه و پورت سرویس را تنظیم کنید.
با کلید s یک سرویس را Restart کنید.
با کلید v اطلاعات اتصال و مسیر رمزها را ببینید.
با کلید x یک سرویس را حذف کنید.
تنظیم دامنه
برای هر سرویس یک زیردامنه جدا بسازید و همه را به IP سرور متصل کنید:
cotten.example.com
→ CottenDNS
master.example.com
→ MasterDnsVPN
storm.example.com
→ StormDNS
feed.example.com
→ thefeed
در پنل، همین دامنه‌ها را برای سرویس‌های مربوطه وارد کنید.
بررسی وضعیت سرویس
برای دیدن وضعیت CottenRouter:
sudo systemctl status cottenrouter
برای بررسی سلامت:
sudo cottenrouter healthz -config /etc/cottenrouter/config.json
برای دیدن لاگ‌ها:
sudo journalctl -u cottenrouter -f
به‌روزرسانی
برای نصب آخرین نسخه، همان دستور نصب را دوباره اجرا کنید:
curl -fsSL
https://raw.githubusercontent.com/TaJirax/CottenRouter/main/scripts/install.sh
| sudo bash
نصاب تنظیمات قبلی را نگه می‌دارد و در صورت بروز خطا امکان بازگشت خودکار دارد.
📌
برای اطلاعات کامل‌تر، راهنمای فارسی پروژه را ببینید:
https://github.com/TaJirax/CottenRouter/blob/main/README.fa.md
اطلاعات این متن بر اساس راهنمای فعلی مخزن نوشته شده است.
@whitedns</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5261" target="_blank">📅 23:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5260">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha  1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن 2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده) 3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5260" target="_blank">📅 23:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5259">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا روی Open Code یه مدل جدید Stealth ناشناس به صورت رایگان اومده به اسم Union Alpha
1- خیلی‌ها قدرتش رو در حد Opus 5 و مدلهای Frontier گزارش کردن
2- گفتن که سرعتش وحشتناک بالاست(الان به خاطر استفاده سنگین مردم یه کم کند شده)
3- و گفتن تا می‌تونید توکن بسوزونید
🙏
🔥</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5259" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5258">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاید که به کار آید https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5258" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5257">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPgHkOx3PopDBVfFhBrXqDtiiMYL4sGVY-Nk8d1kkU59PjVwSUifBWrCw61aEl_YA1tkRSmu4i14hbeRC5h6waZ5RaAMOohvenDIWaXkLihJeXaIFd8xIUVXFSdQ0gZGrCjymgfNdJDgYe1dQRXuZX1BMFQTBDgPwoZ9eFEhE6CUdp-_YqTOjv9xztb3tPVdoMlqhXV_zH72RSqjaLjjHQobtuT1os97M84EHCAdm5NCDW17xhFE21qGGwsOrqiRzKW3bHqzuX0jJnPF4dvzPQvTT7AqL9wo0hVfd4g6dBqrcy5SW4LrT-6AHDdqtK5_doaUiCyrS1GFxW9nBcDBEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید که به کار آید
https://eseminar.tv/wb182503</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5257" target="_blank">📅 17:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5256">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجامعه آنتی گرویتی | Antigravity Community</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv173ViwPuKeKqza-jtMmGVKT6mj4SrI82N0ogSWza7rjuZf2_bUQn6DKM-wzHIwlM79ba5WAJky_ANdz3VZRKugLV9iHA9rBpj69lACxB8uzmuUWoLXGkc4rYqz0Gd9A64ZzYPVL4VzlmhSwBHbdbJdB5lS1taNEt1RAjst3hpb7oKzTg_xY6z_i3pBVjaYJFWDhcsEpXK0nKgTmVaAfoeRDJ3GQfJhj_4pxkG3NYfS9lkGcpxtvJKqc6Afc_R4dedLOc-K6OS2QZWkx5jnpsQsUPOaibL80ejwR0KcSjiDq0dfXRyS_E5SxCG6iNZ5T32XMLQpaYkN7iavpoIWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
راهنمای جامع حل مشکل ارور ریجن (Region Not Supported) در Google Antigravity
یکی از آزاردهنده‌ترین ارورها در استفاده از آنتی‌گرویتی، خطای عدم دسترسی بر اساس کشور و لوکیشن است. این بررسی‌ها در دو لایه (سمت اکانت گوگل و سمت کلاینت نرم‌افزار) انجام می‌شوند.
در ادامه تمام روش‌های تست‌شده و قطعی برای رفع دائمی این مشکل را بررسی می‌کنیم:
---
🚀
روش اول: تغییر رسمی و دائمی کشور اکانت (توصیه شده)
گوگل در دیتابیس مرکزی خود برای هر اکانت یک کشور مرجع (Country Association) ثبت می‌کند. برای تغییر دائمی آن:
۱. فیلترشکن خود را روی یک کشور مجاز (مثل آمریکا، آلمان یا امارات) بگذارید.
۲. وارد لینک فرم رسمی گوگل شوید:
🔗
https://policies.google.com/country-association-form
۳. با اکانت مورد نظرتان لاگین کنید. کشوری که در حال حاضر به اکانت منتسب است را مشاهده می‌کنید.
۴. روی گزینه تغییر / بازبینی کلیک کرده و با توجه به لوکیشن IP فعلی‌تان، درخواست تغییر کشور را ثبت کنید تا به صورت دائمی اعمال شود.
---
🛠
روش دوم: پچ کردن کلاینت نرم‌افزار (Bypass بررسی ریجن در اپلیکیشن)
بخشی از چک کردن ریجن و اعتبارسنجی‌ها مستقیماً داخل کلاینت نرم‌افزار انجام می‌شود. به کمک پروژه متن‌باز
Open Antigravity Patcher
می‌توانید این محدودیت را سمت کلاینت خنثی کنید:
⭐
سورس‌کد و راهنمای پروژه در گیت‌هاب:
https://github.com/AvenCores/open-antigravity-patcher
• این پچ محدودیت‌های منطقه‌ای کلاینت را بازنویسی می‌کند.
• برای تمامی سیستم‌عامل‌ها (macOS، Windows و Linux) در دسترس است و با اجرای اسکریپت راه‌انداز آن، برنامه آماده به کار می‌شود.
---
💡
نکات بسیار مهم و ترفند تست پایداری VPN:
۱.
تست کیفیت فیلترشکن قبل از باز کردن نرم‌افزار:
قبل از اینکه Antigravity را باز کنید، ابتدا وارد وب‌سایت رسمی جمنای (
https://gemini.google.com
) شوید و یک پیام کوتاه بفرستید. اگر چت بدون ارور لوکیشن پاسخ داده شد، یعنی فیلترشکن شما بدون نشت IP (IP Leak) کار می‌کند و با خیال راحت می‌توانید آنتی‌گرویتی را اجرا کنید.
۲.
استفاده از حالت TUN / Global:
مطمئن شوید فیلترشکن شما روی حالت TUN فعال است تا ترافیک برنامه‌های غیرمرورگری دسکتاپ را هم به‌درستی هدایت کند.
---
⚡️
سوییچ سریع بین چند اکانت:
اگر برای عبور از محدودیت‌ها چند جیمیل مختلف دارید، با ابزار
Antigravity Account Switcher
می‌توانید زیر ۳ ثانیه و با ۱ کلیک بین اکانت‌هایتان سوییچ کنید:
https://github.com/m4tinbeigi-official/antigravity-account-switcher
@antigravity_iran</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5256" target="_blank">📅 11:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5255">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlRoP5fJq5ksgzXuYQR6bTkFmGUJmVeufjHvAYzh6GBHEl891Fz-ARLriyJOoZ4cRlsi3szfVcgnpkupHG6OE06TirCvaffM3FrybSvbU8uzkFkUef-JRlFIOqi9SYCxoy7pHZsBBjBuj7OKiArDEPejECGwXJznJIYH_dvvb8ZfKlV17d9ACBKTHa5t7yFJQhS_57a9waF2YMnXNftFv8Gg7l72x3LnHVsyeegsv6-rjp2UOVoZ0isPfY7ZL2LOe3UgkkFdKK0B2ieM_hf214FR3M6hrA9qi2rPumwQEY_tgdL5UtRrowaqXdbTzGLPcwxzZ-uHAiAPgBbH7uvPXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
اگه ویدیوی دیروز درباره GitHub Spec Kit و Spec-Driven Development رو دیدید، این ابزار هم می‌تونه کنارش خیلی کاربردی باشه.
اسمش to-spec هست و کارش ساده‌ست:
✏️
شما با Agent درباره فیچر، مشکل یا چیزی که می‌خواید بسازید صحبت می‌کنید، Agent کدبیس رو هم می‌شناسه، بعد "to-spec" از همین Conversation و Context موجود یک Spec ساختاریافته براتون می‌سازه.
یعنی لازم نیست بعد از نیم ساعت بحث با AI دوباره بشینید همه‌چیز رو از اول تبدیل به Requirements و Spec کنید.
⚙️
برای نصب
npx skills add https://github.com/mattpocock/skills --skill to-spec
🔗
لینک
💬
به‌خصوص اگه دارید با روشی که دیروز توی ویدیو درباره Spec Kit گفتم کار می‌کنید، این می‌تونه یک راه خوب برای تبدیل گفتگوهای اولیه‌تون با Agent به نقطه شروع یک Spec تمیز باشه.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5255" target="_blank">📅 09:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5254">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔸
مخزن OpenUI: ایجنت به‌جای متن، خودِ صفحه رو می‌سازه
تا حالا مدل AI بیشتر جواب متنی می‌داد. این پروژه کمک می‌کنه مدل مستقیم UI بسازه؛ یعنی دکمه، کارت، فرم و چارت، همون لحظه روی صفحه ظاهر بشن. اسم این کار Generative UI هست و OpenUI یه استاندارد باز برای همینه.
توی کار روزمره اینطوری به درد می‌خوره:
تو می‌گی چه کامپوننت‌هایی مجازن، مدل فقط از همون‌ها استفاده می‌کنه، و خروجی‌ش هم‌زمان که می‌آد روی صفحه render می‌شه. برای چت ایجنت، نسخه‌ی آماده‌ی React داره. اگه با Cursor یا Claude Code کار می‌کنی، skill هم داره که راه‌اندازی رو ساده‌تر کنه.
نظر شخصی: این ابزار طراحی توی Figma نیست. برای وقتیه که می‌خوای ایجنت واقعاً رابط کاربری بسازه، نه فقط توضیح بده. اگه داری یه chat هوشمند با خروجی بصری می‌سازی، این پروژه کاربرد داره.
لینک GitHub:
https://github.com/thesysdev/openui
✍️
CallMeDiegoJr</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5254" target="_blank">📅 00:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5253">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5253" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5252">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خب ته و توش رو در آوردم، این دوستمون یه یوتیوبر/برنامه‌نویس به اسم Matthew Miller هستش و یه چالش جالب شروع کرده: «انقدر Vibe Coding می‌کنم تا به درآمد سالانه 1 میلیون دلار برسم.» طرف تقریبا هر روز لایو می‌ره و جلوی بقیه روی محصول خودش به اسم BridgeMind کد…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5252" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5251">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5251" target="_blank">📅 21:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5250">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BZS6bd0l0cLsbiYP77YXzs6kbX609rngocHIbi2uHQZwsPhzmXq4UiHYs2oaABdtv_FTg9PgBt4FdOGWtZmsXoLiAEZxQZTaOZGy7GfKHTlD4x7kYgxEOZ8xV_h74BqIr8wKkJ6VNXM6oEkkKhrUNsJNYHUPlBEux2DipuB1FRoxSAetPXIwEjR30gatdEyM5ZHSqDuGNDQks6w9UUZH6JqVaJ6UHivc-cv87YXh3rIwzfRiBe1TWX1lVU3-eqoQE-Gv6c9fcMz4EHpx-vmkAFFWDaWCYmQaqJHE1qyVRi8iMI7Jbk5zOSq7WJAkl9MIZ27iBsTNaMSk1JGyiSbTqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایب کد کردن یه اپ تا زمانی که 1 میلیون دلار در بیاریم: تا الان 237 هزار دلار arr داریم
🤡
برم ببینم پسره چه رمزی زده، میام بهتون می‌گم</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5250" target="_blank">📅 20:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.  بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.  یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5249" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">شرایط اقتصادی رو درک میکنم ولی دنبال توکن مفت و ارزون می‌گردین خیلی حواستون باشه.
بالای ۹۰ درصد سرویس‌هایی که توکن مجانی یا ارزون میدن و اتفاقاً مصرف بالایی هم دارند شدیداً مشکوکن.
یادتون باشه دارین محیط اجرای ایجنت‌تون رو به این ارائه‌دهنده‌های inference وصل می‌کنین. می‌تونن با فرستادن tool call جعلی اطلاعاتتون رو بدزدن. و ثابت هم شده که از این قبیل کارها میکنند.
کل تریس‌هاتون، رد کامل تعاملات و اجرای ایجنت رو هم به شخص ثالث می‌فروشن و اون‌ها هم دوباره به بقیه می‌فروشن. کافیه یه API key یا اطلاعات حساس توی این تریس‌ها باشه تا به فنا برین.
اگه نمی‌تونین توضیح بدین یه سرویس چطور می‌تونه توکن رو این‌قدر ارزون بفروشه، سمتش نرین.
✍️
PsyopBaz</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5248" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5247">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nvA02JR5N7FJQ_maIA550DxgnMeMLzNFYWdHDVlHbgwG3NRO4p2-zwSk7ADeQG49BTxKT3YIybB0LWGubmXCYDq0sB0sKNUTk9nzNtjd4iNXWMU7RCFQ5mcrkPeP0S_9ts9j1IpkAltmfTDItdtIvr5_PxIpc1qJfJxwg3Ptay-qRLc1kvgghaJ4b0UURUt3yI1Ph_2mFO3JhIl0W0TL-rY_HgR1RQVsCkhk9zxkjBtqYVTN5XAL9bvmSAFGe433QDhEs9wa4IExKqrrFgokwq7zxmhST8m_vvrncKfBPD0kFlJs1_PoXlsB4tLgTVZFyr1nE3iWyLSis-rrcuqouQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی این قانون رجیستری رو من نفهمیدم که نفهمیدم که نفهمیدم.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5247" target="_blank">📅 17:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5246">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">متأسفانه گویا Railway داره اکانت‌هایی که با ریپو هرمس، ایجنت ساختن مسدود می‌کنه. سیاست‌هاش احتمالا عوض شده.
دنبال راه جایگزین هستم که بشه دورش زد یا از پلتفرم دیگه‌ای استفاده کرد</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5246" target="_blank">📅 16:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5245">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛  اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5245" target="_blank">📅 15:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5244">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L3FEuCofz4E1LVM_7-5xKYgYahyBLVVzfPEibRTSbfVaGfUzj5Yi51YaTavxlcWRdUNxRjcfAZB_7dO1kk_F-c2EUnWrGJxFxKLfdlJlxRtXOt7hq3uOcDi05OfMnpfij9ikineobOjzNEUYTRLRx_neDHkl5QilRGqQNzGXTSHhp3U6g7p8m6-iF5qv6EbLPJZ89k6dU137q3I4GKRId6Ew3Vcnmy4UTaLUcd-ivcJrEDp2Zb3ze9-Ly0_JuBLmaCYRsX3_koXHMepGClE77Tr833Dg-bbHM80a3xBPFMnzoC8ghcqMLHW_0p5I04NAc-abA8-ryYnGZHPirwruTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5244" target="_blank">📅 23:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5243">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5243" target="_blank">📅 23:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5242">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TdUXqq0okASp3qmNTPitYw7gjLtE6CKW-e9hvE8ksH1Tzgr_8cyVy62lOV9yQA2y9KopECF0pes_xeCaV8FczEesYWS2MGhRpL1ZGglQMlZsb0M--rYqstvMYK6X0wre5e8XdP7Nsstji84oknHcpvC-kkduemCuniZZMjOwA2N8sFqwPskxEf5clYiJj-JCwRSPoD_P0RTQAYpwGAOaAVb22DlLsKrGSHG8HmPPM8F08NKy_H8eq7qD-s2wxb5NsrmowZ6f1qwmo21jNYTp6MWCSREP39VD-S95w-41Z05LFGeLctOapgWspZiXmyYKWIxJzLCCXTFQWplWkUxAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش Spec-Driven Development با GitHub Spec Kit
✍️
توی این ویدیو باهم یک پروژه رو دو بار می‌سازیم؛ یک‌بار با یه پرامپت ساده و کلی جزئیات ناگفته که تصمیم‌گیری درباره‌شون رو به AI می‌سپاریم، و یک‌بار با GitHub Spec Kit. بعد هم روند ساخت و خروجی هر دو رو کنار هم مقایسه می‌کنیم.
منظور از «توسعه مبتنی بر مشخصات» اینه که قبل از پیاده‌سازی، روشن کنیم دقیقاً چی می‌خوایم بسازیم، چرا و چه انتظاری ازش داریم. ابزار Spec Kit گیت‌هاب کمک می‌کنه این مشخصات رو تدوین کنیم، براشون برنامه‌ی فنی بچینیم و کار رو به تسک‌های قابل‌اجرا تقسیم کنیم؛ بعد کدنویسی رو بر اساس همین مسیر پیش ببریم.
برای من، بخش مهم این روش فقط کد نوشتن نیست؛ اینه که بیشتر به داستان محصول فکر کنیم: کاربر چه مشکلی داره؟ قراره چه مسیری رو توی محصول طی کنه؟ از کجا بفهمیم چیزی که ساختیم، واقعاً نیازش رو برطرف می‌کنه؟
💬
حتی اگه برنامه‌نویس نیستید، ولی با کمک AI ایده‌هاتون رو می‌سازید، پیشنهاد می‌کنم یه نگاهی به این ویدیو بندازید. با یک مثال عملی بررسی می‌کنیم که وقت گذاشتن برای روشن کردن خواسته‌ها، چه تفاوتی با شروع مستقیم از «کد بزن» داره.
⏯️
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5242" target="_blank">📅 23:10 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5241">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده. برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5241" target="_blank">📅 22:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5240">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خوش‌شانس بودم که آدم‌های خوبی رو توی زندگیم پیدا کردم. کسایی که با خوشحالی من خوشحال می‌شن و توی غمم شریکن. کسایی که چند ماه هم باهاشون صحبت نکنم، میدونم از صمیمیت بینمون کم نشده.
برای همه‌تون، همچین خانواده و دوست‌هایی رو آرزو می‌کنم
❤️</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5240" target="_blank">📅 22:30 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5239">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نمی‌دونم حکمتش چیه روز تولد من با روز جهانی برنامه‌نویس یکی شده
🗃️
مرسی بابت تبریکاتون
❤️</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/5239" target="_blank">📅 00:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5238">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WwbJM2Hw6vR2IFg6FS-qrJn_PoaWmSilXiATyizo7SnEgTP-fXZ-rLCiQ6HlOZItIqmw6px42SBLpN6Ve6yLrt6D8DCY7T9OdgcDmrxw4IYxGad8eVt9tXzurGsRhEtjhehImtV27jMVh53GcWdmJ4aBh92-66RMw1Bwax6HEwMB_Iu62OQZEW94JPDIQcVesrM2-pP1CtpCLnkMmgC8-hzRnclvTqQRaBAgr-0vr85Dx6GfsxHkZY6Q4F3gxcn-Q-EfG5jJk4_tPUEudJ5hc012AQvIgNrLt0fy6xHEAWlMDkx98UtIlS3szN5FMWw4F5KiY1aFcvW_eclNy23Mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Claude بهتره یا ChatGPT</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/5238" target="_blank">📅 00:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5237">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Gvd4FPs_yBYNM-DNefuq1OjPkIgL89lKSgyWhavTCxXeoY5Q4PasD8W758pCpGllXDRqL5j_LiW8KYR7XSeF7StQs8kV-T3f9l0QCfgLaf-AU5doppE_JIz40AtjkLHYSIrixMXcXi8rQ7K0-hBEmtYA9EEPdguP_HoFEf4QZwsDkYGxcd7cG8PPEfgN2OMw-yMdaw9FWs8EXUTUFN-P8jgCrMAPvlL6-JOGHQIKCVqi65zWyJGPewZ8-PL76H3bw7HRRZHUEy7T4YvG3HUM1pT3bdsRLJijv-ZDpi5iMJ2Bp1QZlml3gfT1SsJ_fOwFH2nvagMh81vW-tNRcy4ujg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Gvd4FPs_yBYNM-DNefuq1OjPkIgL89lKSgyWhavTCxXeoY5Q4PasD8W758pCpGllXDRqL5j_LiW8KYR7XSeF7StQs8kV-T3f9l0QCfgLaf-AU5doppE_JIz40AtjkLHYSIrixMXcXi8rQ7K0-hBEmtYA9EEPdguP_HoFEf4QZwsDkYGxcd7cG8PPEfgN2OMw-yMdaw9FWs8EXUTUFN-P8jgCrMAPvlL6-JOGHQIKCVqi65zWyJGPewZ8-PL76H3bw7HRRZHUEy7T4YvG3HUM1pT3bdsRLJijv-ZDpi5iMJ2Bp1QZlml3gfT1SsJ_fOwFH2nvagMh81vW-tNRcy4ujg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/5237" target="_blank">📅 00:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5236">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.   این قسمت پلن های امسال هم ضربدر خورد.   فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/MatinSenPaii/5236" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5235">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tBDHzjvyjWYmc_J9dENH16uyS9okBW0gYIEu3oaAYJQHuFrw0iqPmoGMauoD_6024fyZYLJLt7K0OcEy_cl-0d4zUZU6HrYBkfZSDXKjVefDC7f5XDo8tHgg4e0m5ZPpCqM5MpODduIJoNrl0vZRjyC_dG_P8k4gffbJxekLRPZoHu2WqmlSDJnWTJc4hkVLxUQLbiHPnlTWf_ITcagN5M-BVl9b3nDtKRyOOhixBdkJGOeFR8gl9zZr_k-FC57yCdvNzh3Bv7wlYXC87IlitdYu8VYJckwjG-lRd2YgpMbSOeJXaWE8W3fsUJsns4bSmsfXunLcUYyAbJsSXv1nMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دیگه اسمش زندگی نیست... تقریبا دیگه نمیشه سیستم خرید.
این قسمت پلن های امسال هم ضربدر خورد.
فقط تلاش کنیم زنده بمونیم.
✍️
0xKaveh</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/5235" target="_blank">📅 12:57 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5234">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pYa2yQGBkE0wPXTnfQ1xv0NxesGFl3wysW2j55w8D3NlYI9eG0mgSNH0MpU02wqSZ1OEf9Msi5MAATdtNd890Pvxp0JPSQxw7YyduiP2CQqS9u3TctGNYOUkFqZucjMQfnyK3lwwYjFVLP2X8U63eyhX_IHuQTaXfh9_RzUofCz6_-7nL1PJ2slCR1fsAPJwnD-_J5yc3OaAVkkyggytkCbuI2Z2zDRwCrPR7fDleqvcvRpwThM-goS-P508BBvRl9bxHK-edYYjuDXTeeflODRovQJoOax-jcUxMOutpQY9qA89je9Vo7I1Aln1ForlCuJgqLfymCLAaNaEOh059g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت Freestyle.sh می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.  برای ساخت حساب مجازی هم می‌تونید از طریق MPay اقدام کنید.  مشخصات سرور رایگان:  RAM: ۸ گیگابایت HDD: ۳۲ گیگابایت CPU: ۴ هسته…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/MatinSenPaii/5234" target="_blank">📅 00:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5233">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tyAURxY61S9xPoNsxj1yoIQyeqD8Hrk4DG7sYxV2zrQ1sbQvO-7RAHcSlA3HwN7awyrJP9mfktZjPJfCGElAjEJDeI1qGT5nc48TLJPPPFo1XLiX2EYAGludElcYnp3VNbpg5uTleWeZipb-v_SvaqEe6T6RukL6ttxDl4wjIhFQdG9mOfcCJF9wV4YZmJz0oUVtd_TReOQ5JHcjd_fszGnF6G2A-8s3kZRlqAYmXXVSI6brC1siYfAADXgmlyH-rQOY7_zKNdOvFBlBbOy422F9CH5K5MgUObQtd45h52gPokYGQTopUcyM0OJknfF89b8_pXSzQYPujoGud8--nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از طریق سایت
Freestyle.sh
می‌تونید یک سرور رایگان بسازید؛ فقط کافیه اطلاعات حساب‌تون رو وارد کنید. هیچ هزینه‌ای از شما کسر نمی‌شه.
برای ساخت حساب مجازی هم می‌تونید از طریق
MPay
اقدام کنید.
مشخصات سرور رایگان:
RAM: ۸ گیگابایت
HDD: ۳۲ گیگابایت
CPU: ۴ هسته مجازی
مناسب برای تست، پروژه‌های شخصی و راه‌اندازی سرویس‌های سبک
🚀
من روش هرمس نصب کردم
👀</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5233" target="_blank">📅 00:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5232">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یکی از صحبتامون توی استریم با یزدان دقیقا همین بود که ما هنوز نمی‌تونیم سقف پیشرفت AI رو بسنجیم؛
برای همین اکثر نظرات به ظاهر کارشناسانه هم در حد حدسن. و نه باید شما رو بترسونن(حرف‌های ترسناک که ai ترمیناتوره و دنیا رو میگیره
😂
)، نه باید خیال شما رو راحت کنن(حرف‌های خوشایند که نه بابا ai جات رو نمی‌گیره)</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5232" target="_blank">📅 00:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5231">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم. اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/5231" target="_blank">📅 00:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5230">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=rorbnQNxRrF90X4V2hqpY4ZgVnsq1vfNpUl98ZRv5PX_ceozuRRq4urCwM127h7RVUEwWWHUqWYMmGwD-VQ05OmnGsK0zHQHrn7P5_EodJB_MYMgkYqCQbAbyzMubOqijn_1O8tv1o_U6GneeuyTIXeNvKwv_eiW4GiQS8hXoWjLUwnmdry8q6mbALeX-zO21A_2UihrXstBVBL6XiC8owFoCXaSgX7NaIIh5jSnqyRUY9u5ME4QsvG4KOPe-C-rD83ovRYUmKBAYLeztJXe2dQ_EDAMRN6PwT_QV3HftT5Tcmi3uGMcwYYLo11JvFoL6uoCUdU1iFTLpRvir2kVbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dad69f2160.mp4?token=rorbnQNxRrF90X4V2hqpY4ZgVnsq1vfNpUl98ZRv5PX_ceozuRRq4urCwM127h7RVUEwWWHUqWYMmGwD-VQ05OmnGsK0zHQHrn7P5_EodJB_MYMgkYqCQbAbyzMubOqijn_1O8tv1o_U6GneeuyTIXeNvKwv_eiW4GiQS8hXoWjLUwnmdry8q6mbALeX-zO21A_2UihrXstBVBL6XiC8owFoCXaSgX7NaIIh5jSnqyRUY9u5ME4QsvG4KOPe-C-rD83ovRYUmKBAYLeztJXe2dQ_EDAMRN6PwT_QV3HftT5Tcmi3uGMcwYYLo11JvFoL6uoCUdU1iFTLpRvir2kVbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راجب این ویدئو که فکر کنم مال نیم‌چت پادکسته، حرف‌های زیادی دارم که بزنم.
اما اکثر صحبتا نه کاملا غلطه نه کاملا درست</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5230" target="_blank">📅 23:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5229">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زلزله خاموش چین در بازار مصرف هوش مصنوعی
🇨🇳
طبق جدیدترین آمار ماه اخیر OpenRouter (۳۰ روز گذشته)، ۷ مدل از ۱۰ مدل پرمصرف جهان چینی هستند و نبض اقتصاد توکن را در دست گرفته‌اند:
​۱. DeepSeek V4 Flash
🇨🇳
۲. Tencent Hy3
🇨🇳
۳. GPT-5.6 Luna (OpenAI)
🇺🇸
۴. DeepSeek V4 Flash (نسخه دوم)
🇨🇳
۵. Nemotron 3 Ultra (NVIDIA)
🇺🇸
۶. GLM-5.3 Flash (Zhipu AI)
🇨🇳
۷. GLM-5.2 (Zhipu AI)
🇨🇳
۸. Tencent Hy4 Preview
🇨🇳
۹. MiniMax M3
🇨🇳
۱۰. Claude Opus 5 (Anthropic)
🇺🇸
حضور قدرتمند Tencent، DeepSeek و Zhipu نشان می‌دهد جنگ AI دیگر صرفا سر ثبت بالاترین بنچمارک نیست؛ بلکه جنگ قیمت نزدیک به رایگان، مدل‌های فوق‌سریع سری Flash، و مقیاس عظیم توزیع است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5229" target="_blank">📅 21:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5228">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv-_oZAu4bovs3SjIHhaKX1dk6bwsxoIhZ9_d4SE330u3BjwZERKhEOcIb3MH03Z0LP8zap2Fz_edzHscKRnYifgZwI2OqMH7R3gC0UZFMTSd_WgKO0rEkNuowX35T8B_xcXk1K3ScsUigGrL61BuuC3VESHuYZOnbxi9rqXshvrlC-5GNJdVZs2mEvXF36jjYyW8zoWgq1MjcAD0RvaUj1vspll7Qscl1wG-2vH548y0vm1Hj_OsWODIgHjW5VTaw41Srt4dbQGLTJbiSvINQpMl2BXB1V4MMyA0vfbCFwwFOGck-v9wvnAM2fBMuMch0XpW1X9rQbPMLQYCrUpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاخره آپدیت کلاینت منتشر شد.  هسته شو تغییر دادم و Aether‌ آوردیم. MASQUE H3/H2 Warp/gool پشتیبانی می‌کنه قابلیت Chain هم داره با سایفون. برای شرایط سخت خیلی کار شده که راحت متصل بشید (حالت اسکن و Obfuscation رو تغییر بدید)  نزدیک یکی دو ماه فقط توسعش طول…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5228" target="_blank">📅 20:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5227">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkbP2dUzcrRyxn7B16lH6UmZ1GBRhAPNncuaS2jQbSQXoz2O2VCKm_ds10zTECTSiX3MwFWPerzlfpnrmTlExgY8IT54zVyLFT9EYCFfRr5Wf82ZC6_zb63ctqZcZroY02z5Wg4pTgmaNUU_o6hXxB6u0GKaROY-g9lORTbez6Cj40BT6vioRnhvXFLV8IlTS2QwLUQTMxuj47Um_U35Jh-7iEBXmqNAGR7cdgHair2r-reyuWFXXVQsbhjTbKo0_CxwWmO3D4l1vGXyadzQ4tL04f4aelZW06-kdbxQN8iuFif3J7KqUHeDviR5HjqZAMcQkdoF-r8XcCx_aZ0yrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد خیلی اخبار رو تر تمیز بهم میگه. از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...  انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام،…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5227" target="_blank">📅 18:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a5ZL8Zbe4ygMAQMcCRq3OIRaM8MUlLG9C67Pzd92IHptiU3iW3WyaOR6xXfAMJ75qS-1mt8ACpPtZIAju_vFRm6SB5CpK6Rbb3slB9MDD8DhrPSpBbEex-aOnSyGPjWLn2UZGXekW09K1UwM-OulechYT4ax6PHPGbWU-1TKj8OzROEX7cT5BM2txK0ZNV0x9DProOT_9NKhlIVI8XMqRMWA38TbCiQ1KuTVLCkNhyInTCUUI2My-OniLKz6nHZfX87sSy1ojIIh1BZ3xP2MdnDf1XjyFyPC_3Gyst2tSJ4xTNJkq4Ptb-toXDopD-Ccb9k1kpD7QrREBO2UagB78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jAMtdYyZlFK8sm8Ou-mj-0YggfPJke7ROK5vJ4tyriMoAZCYqGBMdkGTB8fERqZtdncUFQ39UgMJhBypRkJUNIX4Nv89sEaqJLSptHkNI54gKvyPyOZ7PWza1NagclDTaOQfpUBMXu18-ALBwLHrtNI0qeVlZCOrZJX7ZcfX0fjVrXHtWv5BrtVsFyWbWspn3Us5upx-6XvTLhPcacQDv5BMaasKcP0gNMq_vUoZYY7hMVT3lRruPGvC4i8nph_437dhdhPKp7VTNyPcr4f0nrx1w_COVZcyy55kP81_4N8svETtxOrPv1fno6h7Ni-m7bipeUuZPyPxr1SY5E5BGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اپ DreamBeans بالاخره فید من رو حاضر کرد
خیلی اخبار رو تر تمیز بهم میگه.
از اخبار تکنولوژی و ai گرفته، تا معرفی سایت فیلم و یه کم پیشنهاد آشپزی و سفر و...
انگار که جادو می‌کنه
😂
دقیقا چیزایی رو میگه که توی ذهنمن
چون عملا دیتا سرچ گوگل، جیمیل، یوتوب، عکس‌هام، جمنای و همه چیزم رو میدونه و همزمان ترسناکه و باحال</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5225" target="_blank">📅 18:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtKRwlac2hTNEJWBniY_LutGzjZUz9qyObLQ4eLz6mEuEarZ0UeX71Jjt0zV_DqY8Qnf7amXu7YnfBrd8BLIQgZevCVzdtIxiuVGj_XgPzmnC4WzQO0_DzTp3vNU4L2csnP3Suu7DtSyNle122zHXSBI2xyZAnU4t7J9DT8L9-qfRgosfXbaKG6-7gpgBptG84tA6FnbHAXhcWDDWnueRE5OgncF8L_WnFVhiLVbo4RH8xiMVxQKemZeshsklx5UPbRx9od9DvKJawdbyEklkNYoqO-yL3XFI-sXdvIXnGzZwNkWHMij3gkD6fZ3DuxXNN1nixRfiDKUaLyTm08-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5224" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جدای از اون مسائل، اصلا یه چیزایی از این اسناد در اومده، عجیب غریب! ترجمه‌ی ai: گزارش نشون داده که یه کاربر Kimi اومده داده‌های نظارتی چین رو ریخته توی مدل تا براش تحلیل کنه ببینه یه آدم خاص رفتار غیرعادی داره یا نه. این بنده‌خدا احتمالاً فکر می‌کرده درخواستش…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5223" target="_blank">📅 16:53 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1NHsEHkYTl344YpAjZvPBNDkI0Gmv6gDlV6IPtm--zeCSrVG3SNvFsOAF61YzvT1P98qeumpMQcY7pVAIp9ZvQ5gjL6IjWrn6W4cUx-fv4X2atnc5SFLX-WThv1tTnYETHFlWVAB9rByHg4ZPmjrK-XDktxEpgzrYhs7bGXmyMlyUTxf_YbcQm7v1tNUBFowyMqjOIzrtp167CLG7WhEdex02nRmvDfp5V8BKXsXSrkd5wgHMWZ50uylX-HVyVfuANUDxwX_hVOSqOGLivpdnxdl9hg4p16MggEPYVSjeezhUn-M1Tjg6oGpsOCqLi4bzk2jMv9UqO2EykvZ6cOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5222" target="_blank">📅 16:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=jPmFO9BStzFDPWQDLGQG4csBL9o8AEzlLg1x16-wUPXuobZoHoVaoa9Ton6d1kWE_TWLmJbM0IEPUWVmo6qiclKXOph4Yw99h3OwGjVtURi5vLZDKMzYyyxKbaoiNlCtpyc_o6ukUzmlV5BJR93Z5QZbIHFH9RA47oZCzMKmoHJD40syxYzp-SspMyKWz-T1JY9iDp_kmfYs6Xk-Cl9zV7_sxG-ukgvtGvJlLz0GlMMIZ2gcMDVnGjZlQpGP5tid929kPCAbTqjoCAuHD2kPVdaP5q5htRp3CZKBHvXIEmqc44ELA0GHK3GGk6F4YtevJL5NrMFybU-81gDXdjJaBg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=jPmFO9BStzFDPWQDLGQG4csBL9o8AEzlLg1x16-wUPXuobZoHoVaoa9Ton6d1kWE_TWLmJbM0IEPUWVmo6qiclKXOph4Yw99h3OwGjVtURi5vLZDKMzYyyxKbaoiNlCtpyc_o6ukUzmlV5BJR93Z5QZbIHFH9RA47oZCzMKmoHJD40syxYzp-SspMyKWz-T1JY9iDp_kmfYs6Xk-Cl9zV7_sxG-ukgvtGvJlLz0GlMMIZ2gcMDVnGjZlQpGP5tid929kPCAbTqjoCAuHD2kPVdaP5q5htRp3CZKBHvXIEmqc44ELA0GHK3GGk6F4YtevJL5NrMFybU-81gDXdjJaBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZhemlFnWUZTvdW4PhWIBfQQXngoN5phMUxa4qRy7p3eaFSO7862eiW_ZhZbhYJuI0tcS2KOMj2z0OP-XtpFlRIHEs0FmSz8zzK_R_GYTHIZuIsWgyGCEv7yB7dbYXkVTVvpQhCjopF9uPoND57koR1ffDWS0URTuc7w9r8bmUJO0wAiYu27T3OSqu0DFTQIup3quXp7qUixDMxVao64Em4uGPl6HxDBBPnrXQNkD-tSBmxQSuNBZyqYHsHJP0dEndiNPqCkgKYH8pCEltgVMOusioNmZstyPaBa_RQhwNe2t4RPGuJfDR0Dlh0HB9p5KzTWX2JsScrUqLukXMLSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ToSXO-wndT616himhpCT81oeEQUJhrQcdTEhMKwExm2ftcIKDUMPYRkB5zq9jD5ZnWSeDQ0noziil6-iA1DTtoMfBL-1FixRh-ERNDRDhLjCrwRanHZ0-96LISDmdSxc5kvXQPqaJkR1ge3nJiNZhSPcecytiifwykZyedF1gQQDGKSa18yNQC2b-w0Mo5Do3gbai2sNtdIHJEVJW5DN6fGM2FoVRztVtxdftUc5v0f_aKRN874IU3y386uau_FYrULE6n_hX3Y5u-tP0P1uB9oO9w3SPGZpCi60jV17bl0nuBR3Gn1koa_zINfX90H8enWhJ7EmTW55FooXXQ9BAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K1ltpZ8s80xqySH8Nh9FRmfYKD-JO2-TL0dlBWsr8XXdFrHZPQL5TBQDF-BGB8wrPmtdoXIYWuvZKBMfyJlLco9sNoCick-BgFKQWI-1VRUAqcb2Nr-fiuFvQB-DZFA1XTOpg5SnPTa_4rEfXoXb7ttVfdkTx28AWlTL_Qz2BI_EihwnBApRS9rAUeDci14nwL9co21mh1XKYbvobODrVwhZJzXSJ4NZ0_4syHG9b9J4WIXy9tCMJosq8FU4oTBbC8_7oKjcUPCmFWNY8LUu5Gyd4YQWvUbGTULCKCnCLQriK4cOhhftqW1LnN1VLCxsgqbR3k9i0GdiCe8yq7nNag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK39qPUmeFqYjU9eZJUlAFAofPs6ifUDDHgbaX21Lcpz3jbwUHBNfkF8L3uCKlwlEB8VdslzdN9ikck-7vKyPj93npj_tJbZrwdoCxhkCRYBBtqSKyvBl6kM2O4A1nDlKBs-zMEZCyXeIR9HpN6nqTRZ85cBuAcKp2sFC8IAfM-IyvP6NBwEks-FCiQEsw_sk1WUhdC_ogUKLsZobr9aLqsUtjjXpysvxD4e-yr0GSDVSNDyKEmgoahZTrbGm1cBXIw4YNT2wGulXRRhVrwGhjMJEiuSy8HI425MUtzVaa9RArpvURl6VJoPcvoCXplmh-gb4QREFCB9ZzYtQn8bNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyBr926Wpzbs8eJH6HyX21GRio4aoecMXMYvDu8abiBiILAsmvS7PQtyCoC329ZYWsknAiGToz13OspSOP24ACuqzHJqCgorA8bg6SIx1f9buF0tGFyJIJd_6axIV1wKqDJdQLcKizM0loEdlhkxLfH93LkaugXsCUCBOOU6LaCq4G1EJ45SKO_xRwYLFF3WZEohdvc1uztoCJz2ybdTPBR1vdnaCPbhP1qNWLWjE4sV_2fQUXR36TtF87iCmkMiSnovzMyy4Dq24IqAr2Sa7EnFGXPsQGdCuT_mfAyN_Bt513prZU4ummixEWJkbMVwoyvTRrqIwOL1KkzjQq4pug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ng0aSWTZopZN-KNCoAq5GIROGtC956mpMQk0OAvvpxWrk8auALdXAA9Dpt0OxZyKg7A488LcDoVZY89JgjRaJkmcNS0I9r-UdhzpvD-VvsYaMQW0EfaTPJE7Iu7ZGUt0nfoK3IrDSaZfrOtnv8wAb1N2iIhJHDnq0yxVqa56MRA1ZkrrokZLM2ggOLwQdW9SqCT9tz0smo-wyFx-trsJ-ACPFxy4gRtE8qCdAVJqM_zzm3mSn-QzDkcTqZygMlHYSjr6wBuokZrTNnC7PbQltndagFYlpbR0qRR9JdjL9zO5MKeVfPknJrThXr4H6ofwkacsZTcFYZRomKvFZOAavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZETt4iVUU_w3SIkAF4aZoyE4ZoH_Nc-dbua9CO4sqEHNGWSg3y0BwdyWsBOAPq7BKaCH3ZL_avH_3TCjyUpM4xM9O9JAEyGrhJzMWvZJM3kwMzwq5DuhUAtVo8W39RUx4G62YKn2cuFsX5FlilsDQ8cRxDRau1jEzCEvVVhHRd7lIh78XXnNvzvYxXiBrdSYpjNPDv7PiJFOKo_OQlJ1UjreSPyWB_iLndjSQ9MG0MWAoflHMBI6Z9bnbEQ8XiREvYemMBkboJO48sx6IAWrKWkL85IVc-uvvZrdYP30-C_OFG8TMVGHiUnfaee1p22MXKbzYW1iHhdHDlNnX000Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QFkUJBAR76ZoxtVRsNyRttE6mveKM61jiBiwa9ar_m6rcOhsWGNb2D7-_FhyYHB9TF10U5lIvgpH9rhT2CFqJ7KeaGiGOjEzMBVnPfTW9mbQAVbHPR_wcCcHK1CLkhBhA2uCNVwGCAbfKqXuPp_-HGb3eO7xPEeRGyikl94_hiE_uRQa5IRSQmFPanozMTsUOjTtqfktMfmbvAAQRzlptptUw3iG73yITTfgu6DAAdAzly_7DLE0EAYBVTPnUKE2akJHPrFj7FKWgXASQN1WleUhyTvbYvxY6xvv67G1LnMUSVIrYuSydm-ZbGJSKEYVRwVzSrcZkfTyvl7boLK6Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=SGtKsRw9u3bNK6OV5prCCUfdKdTVVlLtwp_gDblRMyqCCvABcriKhtL3NZ1m5ePmkqOAB-QWKfKKayTpTf6keXtKbmkV5hxBAGjkVwDlY64kZUUxr2yRWwPrBNmZbqNNiV4msMefo98vz0iR6pdphwzfmC0JWjJNNkGg3PB5nt7HHT1HCciDkUPRoN7PWJxFDDmMBlmSo6_OOtSjzJAWMM8nmMUE2AREsUZhE93fNABCHSQiP22sxG7qRjrKdvX8Rmkr2DgOmk_tqonk1cTVg8jzrujJzAm97-D3lFeKuKv-o_-ynE4XNhBrSQXYDN0XCjUga4wVMyWB5e61QyDfPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=SGtKsRw9u3bNK6OV5prCCUfdKdTVVlLtwp_gDblRMyqCCvABcriKhtL3NZ1m5ePmkqOAB-QWKfKKayTpTf6keXtKbmkV5hxBAGjkVwDlY64kZUUxr2yRWwPrBNmZbqNNiV4msMefo98vz0iR6pdphwzfmC0JWjJNNkGg3PB5nt7HHT1HCciDkUPRoN7PWJxFDDmMBlmSo6_OOtSjzJAWMM8nmMUE2AREsUZhE93fNABCHSQiP22sxG7qRjrKdvX8Rmkr2DgOmk_tqonk1cTVg8jzrujJzAm97-D3lFeKuKv-o_-ynE4XNhBrSQXYDN0XCjUga4wVMyWB5e61QyDfPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pRPbzkXPsAF9pB4JemFyUecGrar2_gJnGWcY5FVUuN1uZbXM5_chSB_QnmkjHMAOj_e9S6dcBXwoY19ro0Eoe9lml38WFhiaY9Vh_l30BhwJCWB6M82rxvS9ABsw3JrvJsXhRiLTurVoxkWXwbCNutKWyiLe8o92DHQQOYn5iJ2qJW8iwwmWMfcb5mR9FoSOIV_9rlc6m6r31woVmTUbIcdycOMcGtT_OXWyEmag4C3CsLlIVDimFDaTva1952fNK72izATV-rVMC-SMtk6hYZiVfhyDLAChxpM2-7m8QQPp2OSrTBAqNUMw73lVP06hNn0Lr8cEYLW608tNznMMDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h6CVra5b8KNv-7lvwGPFHNtf8uHGikSOoSKQqVy6wcgVBccwRPHE3oYseAHBCxtMcMIu0md3BXxcrke_-nmWcTyLcbKRY_GqW5bytxNcvrEYUcDEP5D9WWeQt9QQ3UeuCF7oKxZ9Rg5c02ohP-ReSQFz3DavWM59uUe3wfr4ebuPtWL6TfJeQia6SMMQPKD_sdMP6Q8QJKXo3L5MIP9CHQGenoztGZ5_Ys-ekJsC9PwJVCVkSBj_5KQXzyge-wTbWJOphQGrbdQVK5XDuWBke1j4wUUAU8AEYhrdWGQ_jWba9hbl0jAEtUHxJxzUSPUU60-fGT7UVkmuGrkp-U4NRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3jDG59bdgIfoK54QK1o2prBuC9ZDdyuwt2yGebsdChkCX3fpNIrOyS6vtnOHwaCUdvTBWlO6-I9CzsmL4oPVwE7SgTIESUWTCIzB-IC8YBkdgL_5V39LQ89pgWwcKJiED4yX8p10kmRd5_bv75ElWI0JiwyG3tI9-77BeBl4MQa-phsPqjjrO4b7i61wbOgZLL_KvkftZ7f5zeevi6w27_TGK-JruKmgeJl35LczoHIoKsmf3hIuaHU75u1u3wVRsF0mzCV04T0Cw5P_6tHukMefzuwhkjt6shprFxWvSp-gj30bSWNqAzTSeIa9TJI5_-JqN7cLJysxoPJijS0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chnKHNrvblf9F8GJ0DRLcoSqo9eAHw8H9sQZDmbjO_ISVWS0m79n3A61roy1uocaWn-LcAnmXw4QtYN0Z-ect0ICPF7GoeozFSABFsRHP0bbFxH9BfM1agGqPfvL7CVcMpnJRqzaiDeSIbckhT0cyu3fLMsd4Nwkrz7pxYaGbGei4s3sJWHluKDfXi-209MFNBA8ezTPTT-uhzse3brmFSea95rd8qZsdUYvlWykNSznnZxOkN8e7pjEJntWoh2uACvgAM7indd9A1u_VImJuTPfuAJUg9n7O3r2TPu7HBiaWVyLTnR_iAY4_upe0esFZGzJORWj9yxcPDft_pdV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b9uCtqw0xo5NIsL_hRlobaOr2nXp-PkV-Z0uUQhlgiDMU7jdu5DzuS0f3WXsP33MO6AK9FrfmtJz3OsoXf8Wu-b1vbUe_80Oz0-h_HuNvMzxEAcUMLbCWymQFmWtLq6h1lbY9DTTz6ukt-Ytm4HYbKvExf97NUDhiEkvaItOy2_jK0Pt47V4a0MLWbJAydRdqk8hVc1unJLJ-948tdYy5JLMXRpGEqsC4RBy8FL1A_fIXS_7vlY1g5mmwLy1ocE8BIUjgAGwVbzj9zYSu0W-FyI_hrgHOvWuGid_ybyZAlmubQT2ooHiBwm3zHDbg9BpCDDM6RQ8XS6zVs8LVSchuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qJRH6kFC8_WITUBBKSy8q7_9fEfEUZyZLtgkxB-8Dc2NpCNGseWd9yxl3IbhviQ3_NXeB1i6pbJL-ScPchIkyM7j291fgJDfjpHy4-Mr97uGLzaU1n7aSWD4u2ltIrU2me9YN9U_BMXiMaeg6tmHs2S8jL4sNgQsQamc6Nse34szeop15sxW0so5uekNQNtP8158tkRFzeLw_9AZxrm4kZn7uzR8qV4PL8o4acIpSl4y0TZzRKLPQdUdsTGfKHh2RR6hmK9U8y28wNDLzlKBj0aXCXkOFwpRkxk7eNG0cD2cTIHOetTg9pjyffgeGZLFHlaJyqD7xUzimlIQPd3FBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q_hx8sgP5XJNCzWeO0jfQ00K2xQZ2hdkYymVwpTBPcUDSgbOvGFb3q7VEd7VyaNJ-heHFOMKB2_UOZWNs5Lv-RmGkerDRtCvSE_NQkuhl3DUj5jwaBCEbpynF62OzkzxYEecyNRFyuqZuPhRQhnli-Bi-g0Kc1rUpcVgiLbm0b7_posCwgG9kr8qnPtSGMduKeK1oUhdD93MCcKniiA3jBxh7_mrBvrieVykOtD2K4RAA2F_vnLhsW73XGCAtRRxfNVdn0KxOamBRaOv1vXQQOwAt59lOApE-PMLZPVkuQ7-4jow_OKa7vJanhxB4CK4kt1eZ1KQvJl-6DSjaUD54A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UwaNQqZlbOwS_hKaiVOwXb1JC4pKT78YjBWysp_xI83b4Zp9pGR2EZkqRlM1k9hWhDLAIZPPmWrqU_ZJgmaD-8e0HHlXdffpKMHNEyM2YnPi16WwovMTtZ1nQL4BJlxzlIXMqgEPci1Xl_5nTS5MC6N8OdbrbYTsd-rKEgst3ADgwbCc32TL5lMi58HavN63vffFVD-9fQKZNxb8rrRCF8IrIVBCJTbVMMZLtBDXG-hwJE1luqYe7Ur7b6Sw6Mrkn2a8Y4jhv76mLvt6SfQ8cFLINDp50GDpfT3wFQZPMIN7Z71b66aOaNWaQ1MV3Ttru30c26MVPpcKofHrN7oMBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FMkqKwpRHI6Ey4BjyEyXFwWGB_UrZxtukM06dMuWL6I47J4v6wybbyR5qmdNks22UOaTTsVQba2M2Ml0wGwJ7fgr7eVWkXKGxgoUxq4GNSsjJjpq2W7uOF2V-Z4t8ptg9K84FrtOUURas-r0zJ3hxttYgp7gPDXNJGbmREI1-idMT1vzAJyQowA_aAm_0yrbnpGQnVLqD43xWO0aA3HkrZ2SuJHfmGDKfQgohXcJkNbeAPiBiQ8GrkJhWjWDa1LdbfaYJVp86BsQ4dIRPH8hW1f-Eb-tG6KCViWtKJN_TAYlCm9NPLWhg-CKYdet6T9wXiVK9IwJi_eSaXNeSuiXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bIOwlQyNQV6chyA5k_I8vZpIKEL2FMT51cQB1qyJ6Sn4ptaFddFpgpa3MwREYxGxdYkvO4zVL1oIjOxaeVw99a3FOZ1dO0Oa5CEw4LtwRQkYSBHuke2p5WUoFxvGSCDhKU8iIpj03_idMoniKMliTAxo5fy-Zf3g60w96_DRIzJLNBU7fStb4mrPMROrPglB2axh4qZ3dT7HxmjpqshHY8CZl4jtzBVHKQjCDvx8_ha7AYnnKk1egM7FR64rF73qB5C5jafaJc2iE8hBeZQHFJsyKcOnzmKsZ2y8gS5devnsubSD_KXzrP_Sl1Hxn1tmpWnPiqVYlPc1dRa9wPRylA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CKM4Tndqy8vH4F8-XvTFCBX87f7cnNO3qHHVE0zhxXFx7P6c_8GDMXdX7Ia4K8hP9gMhnD0XNF-VpwI2uB5A5m7yQRa-Vjt36dMcZBo9TdSXU_BPsg8HeuaoGU2KxUNBAGAf5x3SHNK-bT0zowkXBA4q-oAJnHRgX6i_ng9ngyVOLUAyPms3U7nF2t92Xt0FIQUNa35d40rzgevsGRk76l3we97HY7Dt8_ATPexDV-_juwogcNOgNqJz5Hf27ZMLCtpjuwwRbrIbGJJXYE70TYvmzYQUdEKQrX0w3tBBJm-1vMmqn42hPeeXRhEVjPKCS1pX3OWuXqJfWjO4KXT-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=KAB0QUVKEWC5H5OKZhK1GMW-kIhJO66cFEQ2Ox_BJ5LWF_IeaZozJ_S_q13TG_9RjUjwjJIRhYaeYrqJY8FnGpBwwaCG00kQIW2q_FMak0FrGZFAT-eg6Xdzh04v9cRJRyKqZUpvFCOBtGpgydVPMnZyJQjpTPmE4Feq-WerMyMeDxqY33wTWruaHFIWhzii_AJ81IIHBrNtnOWEXbo104ESxqqbvfDedhyw-W2FY2ZKgpq0k-p4ouNLvb7FehT4z6N2Q0_7_DQ-rFliwQcTmMotkf5wq7rDIDZqF73LOjO44rDpmZxsJRfhQam7Ix_S7d-9qSwt47Lr6cECl2pi5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=KAB0QUVKEWC5H5OKZhK1GMW-kIhJO66cFEQ2Ox_BJ5LWF_IeaZozJ_S_q13TG_9RjUjwjJIRhYaeYrqJY8FnGpBwwaCG00kQIW2q_FMak0FrGZFAT-eg6Xdzh04v9cRJRyKqZUpvFCOBtGpgydVPMnZyJQjpTPmE4Feq-WerMyMeDxqY33wTWruaHFIWhzii_AJ81IIHBrNtnOWEXbo104ESxqqbvfDedhyw-W2FY2ZKgpq0k-p4ouNLvb7FehT4z6N2Q0_7_DQ-rFliwQcTmMotkf5wq7rDIDZqF73LOjO44rDpmZxsJRfhQam7Ix_S7d-9qSwt47Lr6cECl2pi5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CIzN5qIzDcW9u9w8kQwqDe4BJJdv3U9d6sE1_XDSy5_w_H_y3ebqKksajcyuepfuFh2JwCEGl8uIo_kDNTHCXcBD1gwFj_KlEwH4rlbJkyphg8lvRKgWTG8euE2LtDpa2cERAvmXiGBq1d5w5FwMo3LX5a2kQUNNY5mAMUqu740J8sA3lXL8SA4n0CKm4R7kX8VeA-s0To3aFFC8z9YYK2r5x4UpPvLyczo7nRoKui6VkBTZp9wG_UkkLuvBnDFNXgwpd7Y2v5DKbFPk7YXabf_3q46wEKbz7kLRBvjDJrtmAiQl8nXlb-7D4p40LweZeN8umXEp4EFTLkwSA246fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kmNkRxAzIs9EsUAvMHl3YD-osrhXJXdfQMq66asIItYZ6jQpnrhYmTz4AigPq6pXjFFdlESJ2KZEP_S4qkkZ0SSBB_31eZPk5Tyg9twRne96NnGJwOzO8vGQV7O-MHzk6f1sHSxot8GAVIHTpGoVBvymj4GNOMNdNWx4zKHts_p1hmt0NFI3sgC5zLxfnbloP-ItWkcS4b_cXl1ONYu9iuAjc_Dg6jgeNpqqhciHCjSVkwHCARxw3dvF5KH48jkJA4zNrjjt9D07UpXLEpwTIetOXs4yr-GZmGjuoN6fk_yf9HZPKe1KTH6gh1wHTTFvDSx9EAxgFTavmgaQtX_eZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z8OmCGWJWeOCtmrS1rLMsbf75F1LWszvkGQo-xc9RQTNXj3ZN9UGm7cZyDn9QbtEhCezu4vifZAA3NK7zQ4v6TzvM-PcscW7gIAX4yuIaFKilMhpaPb41pWJNlAxFRtRWvNjOuFi3Fuya9vDHXMYYKXtzXaeX3xrSHR7iVEAleJXHI_9N-ItQVd85j6w26Fn39RvAAXGbegfhFEaBI6rIBxPY_cD_MlTW3pDXKfL4N_VjPDiMNYHxWv-VWNth-HsK3-tCpELGXyQxMRdOm3luYSmKFK6uLnnFw2YGfFBaOr-6qLVxiuWBEo6XEMSVSPAX3faYsbMFaPl0orQZXsIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4P78H2vCc9q4dEHS-BsNFY9FrYWaRzuPthXVw8KwNEzPFeqVSdkcGz10YAmY4rB1jpV4LLbBCZf26Azyo7aP2WwMjqi2rFKlIBxUxQk_3YVGDKnrmfwOMKdwzSgaAYL-uMfMowm5wP9nJAqDWGukHqz27K9mBzdk2bnonLUpkmNV87usavTr1QSt1EgC3VxuzCissTDpYVaWT2AELbxSRCHG32cPMby3v45M4RZkHSokzbWsK8UoNb21IqhTekpfVqKz_sOdwZPaj9XRbEFpzxKp7yEpNfEYRjGMD1Qb4TrABSfMBgrbg5JLdIg5ab0LNDs31-eNtL2LC3Mfv2D6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NFwoklGZ7ygaN-YRnzfvYcY1Q7yhTxSjaecMDRTY8kL-o0-yrFn8RvzKvpa3Ki7ry2eLMkO68Q7H0HaaQbML0iZZxdpAUsplLqB3rdT199vGlo5T_l2iksdqigHiuqXcH33H6rqL2rQhpNwZX-vrW1XBa2uKs5O0blO3mw70Gyk56rhqUmjAg4RzO7li-tGWWiHpED_hEmbhrXQQzoBWTEIHn9491fGhG5GDz4CrqKO9nLrUuOedbKjWUSmfJ3BWilstHE49Q_jpm7rt4OvhSUGgh06aemUvtzDpJuDlZBUVWCcKpAN5v1eiuBDHRTrpe7ofqAsAOZgInrdLl6aEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUsjojbYsOU_KkwcELO4ka4hKFhRGuS-jSDVhWYisqsHC2YRn2dm2Eds85r9mhb5XJ_gjRIPhqGhapUzKIaxEJxEWeGxFG9xfSK-IUYwhkF5f7JO_eSJSlxDNQH8kmn7jq6SEolCqa9GGFcig6vIuEmK-uMn5tH1yaNuzfqsWytaPBJiMgO5PwFaFP0xagnLaDOo7e3-okQ-DPFuucIyJcD171kB46muiVW9g7sBmn4E3cPTDhYy-hI56dp_NzbAyaulq4rdGSfTedPlpjCVWHwAenwjO6FesDefV6UNkvGn9NnhqHlWRDSsVxJs28U_w4LKM-Kwym9zVQ5mE59Siw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HC3CS2gQXHxw9BuE2WENQza4pioSnmRcjJk_wJ81pP1MBXjpH1_V6_RDuunv0FXCTdrDBMx5IztG0S_zPEXNQV43KYPsdYGecG72mblD7NZBfgw-QjdtHptEavBzTO5p9ks9hfd6RM-80ZXSTUSNUMiVBUvvciGvHPAaSm7vonoMnIFNalst2APfJWh6NQTSomugHDhTJAUmaSvY7T9xR52UldXL8SzSqWJHjG5biHesakeUdJ0FxsjRBdsRMwSnfajlwHusH9lAK7hlf2glbLYnXkaAKDujIyO7Y2auTXAIpnZhFDcAG4mzGozMOGcgpQtAkPIq4wsq7PIYyESZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ivqHGdAMQgaiBQWtDx8GF3NzCC2H2BgKCyrrUiSZEPfOdchkCT-WmCbxfPRn1XJAYtMUSD0WMRcfHbUonKCzmQjw4VO270uF4JHn2bnOZJNSfHyBbnQp2TQhzRCzZuypbf_xdyOLKd-2yZxVPI22Hs3w9h0orSuW0VPEb8tT2AyV7ZkTKPi1D6Yzt4wAlYEVOCrfYgnzfNzy9FDKb8p7HdHque57JsuOhxKPgVx-X03XsXtLJKD17Ky7BxgzR-ty07krX_dq-xzjaSf4tYKr32FzZ27zL6D6zjn_1YoOFryRyqKVu5cziJQDyzcqa2oFGK33_upiZ1dEIPRyXHZ4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FvFnEOjYeqoU16tPuogoAXZN-H_HyIFa4obrVHy94lX0CLpZKplpvE7bavOdA9zv6lZxxEpg10v7Rt_TWkusaW7Nst_OPzk0AjYvlvgGquj9tzryPnkdt6_a0jYfPcRBbT-Sf1afiPPaBDOxqPHcXHw3r1of6NPbhvhgH8U1oaZsamrNBQ0s7JYbumyOWxAH-H81IakD-O_B8eXOPaDTLzQmV3tBYQNd_mpF5zz1qlt8VkUhHYsRBZ8LNm-8_JB404U5xw33b0FKlvvKnBAMVPjupNrnCcmKPzMLJGuM_zU6UIBTF_TJVr93N-NqvLBD_lmLJ1Nrd9rF_gyH5FXU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OX02Hq82maTEpKFe9o6xs2DAMvDY__GKzrQyBFEYBEx3pOQjckBOsgEEMle-DaJ9WPx-AwxoncT971vJe99aNEGRQxLRlf4aKWgaluMUuyZdr6KnheJiBK0WtDQdY8kRQNGH7gMtHrNCs1-4gxlPC032D_YyfG31dfihEWO9uWKUY1iC15FiQEDL2XHfbJidSXuD7mUEsbFe4qvBTVFkvCnsH4Yf3Za6NXvttX0ccdEayTcySwArd8WdOX89SRnj5tAcHfq9mp55IYM6EARsYHNUjOcm7-Glz4kXbQ9Yd1LLS4ZIYtejSRS16aovPTHpkrd20UQzYWEEfxZA3Fnp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H4q4tEXI_b4nyuzmcHKcFtO1j1LGPSweJXuR_sLEBIOOrDRQAaPi-2BkAXltkRmaS4yv9CV1KtLq5CU7P_TPzR9L4IZW-xJlr57J25WqAHpDF4BKgGSa3ZEomfc29EOuwG-gz8wvC0SlBSgLmawmppDFK6m-kVxTEtPHUb9vRoorgqFor-byoktoqXiFO5OdQHv-QVADmSOWDsoKEkAa_Yo0T9JRvwjDax5whEeYLtrB1FoqFnu2JdTKHsA9e2_M1JYjJ-KVBvg96xTONjF_1mno9lkvJrmGnZ9FSNVQAfo7vxivwLWCsjaUrxOtYHlTDFjr0Zgm7NLMC7ox1sjIFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
