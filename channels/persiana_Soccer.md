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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 400K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmxILp82VtwEiRvr_2I-93QhOy2cBdb-1bN0wdQVHeNyTcOtUWlihLf_KiJi3XoEOMdrYPLCbsliXh_JeJO5DwL8mqu_vX5l1MHFpv_zTcFD6-7hoPwQrIZ46FYSzyKlg0Y1sNvWks6qZVoqFoj6KLJrnQX742FdKdN46KarJc6i8SnkjXKEX5-9q-z9gZzxW0SQnaRCyUW5QiXqZ8OmTBcDvxxh2z2pkDEu6kuv0YIvxainnFrcGtrXNyjAAIORI8SPgCOtgo3hmng1iBLb1BRCoro8kd4CTTRsjsH0W48rqQ8cUBpQVKhljIq-jyYgk6vYkcyV7EpDMqKa3021jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hn8GotJOuoA06MNofoTdGrcKO8z9M6-3-GOViPUmCdKWSAC_vAqHm2FdDU0J9zC5pHGCa3frZy08z5G7NqbKP6YWxDbGTypSeFwfSmSM-uN5YJ8XP7Vq8InF7pXUPEXKwJ6DL3up-MZ8kYf2ANqejX_lMajF8mQ924VDAEZw2_iygs0AghLIBriH_CcNrVXaO-hSEyraaLZvR9C6YjOu5YLYn68wnH-N7Yysj8hYHOxqRZU4sS62whMopp_Q6elboc4d5vrAULY4_AIAYmgA-TGOP4mlACE6H2gjRK9xWppeUa5LJ5w5fvuidr6AXTBeGR6OejDY1pFqPT2vlubzOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lcc0t9k96vliflTKXIpVxoCqQCu1BB89jGCjs0pEvKpmlVbRwhbLy5PCPUfJFU4ZBJqh8U5vl9CstWz4oIXsGMr-3Zvq9dMEUEK--oFIe53ZyZMA9dpXW6Yu0BHOQmzu35s6sEvLelr7Z5uYpXMAYqmJ2jL7_R1BCsAWpIHSJ1fjNsxnnbKpx_qj9JZqtkxE5VslfVrXC2DWHQT_M7am_JDha5GMK1xvjf1-X3dbs07tw_B4PXDG0HUdVQGtkncc2hcFHTCdh8IOOoowsByQ4Zf7Uw8Vyo5mUuneAMEd7cri3f41KQs59EMgyI_p63IUIrHFugf8t4nxi_x9uh6PuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=irfEk36vfg0kebpPfkuVUnibF25VbsGLjkBuFItMasl5QBmlhA8FH_GBN0HJ_0g9-TNa8ho7LAdwNkT_g5XNUdPktu4Cpn9TFTD7iwJGr8_uvO0xRjrFYkgkqLDpLrQFEeb3NhXK5LPWFa-YPY4bEvdc6lVtEbdHvUcN5uVypr-YvfMPD8s5IrXsdN9WkqYgYvY5iQDS3Gi9tF8xw28_JBWjieGa1C639O0DDEqARRfqrKNivtD7mEU7zXBb7wZFcc1bR55E8zgrXEgXgzAyk1l8hEAOFAE7YwqVouwqpoKxnBd1NtvreJP-H_y_rWT5tr5vjQMcMLkW-Gasamb5JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=HQMfzxYTQ2XPwvBbbzS804laVzynC2GKxHYbYZkDDduLfFo92cejAhy4nw3o0d6upGkvYkElxuRaYbl47NQndd9K0-gULSyVpy_2lacvNvBifAZ7SyBjZ_0zo1GHUe6SF2s3TnRUMR1pli7-c0qCmdEI2-rqY5zS2s5YVLcsvpMhXIOdiq6fuam-2LUEQMsppFDhF6jZ8wdM1mQEaRiZhp8ND1oKF3hUvtJHQ5f5yMN3meFm4fdRjD_3wlhEWzIiBAe0XjLwuOyuj3msjXGF1JaLHhMkRVrVQ8L7NKHQB8bGYx3hspF73EDuI6DN48F3Qe4UfFB_012olkbjsz_P2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3BCl6ykH5YGCgxMEh_4K0TRd171MUdj0E5Nl3CivPrkb2CcZMCdV7dG-Jn1ekSj4ciFQn1xA1ZIVyNlv0aiDwXWIW71ByK7H0L6z5RTluj7uQ3ygmcBqg2vrvFs3T7y6jMXLY4pJv50N_fas2PSRrj1mqa9TM7xVimNNoSFB2piEuhfFaTEWGog5SRxZhWxEezfFrIc-l0CvWtIktU9QBC7p_tR43OitQMoRYXWOhLF_Og7UIul-6hbKLz9lf7saq4bIDnfx_BzItMh0L3s3Rs0xttLV2_759qZKHEW9n2IJOtRsPevTiJOppKnZks4tNRSKRtnRP36bHUjDLuqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWZn5cqNnz4PNhBh86r-u_sDa5cLG_dfbXVpnifSq--3M9SdgUh8nUGdXeursNUFt3JNVq-D1HkupZSIV4-Z0zAYuu2A1i2uxRpWJDUDW0Qi34Jc7iMN007uF-PK1v5WU6GBnG_x4s0CQTinWdfdxUe23NfxE-8fqmUNy5ofI0MQOmq3KTZ4uHZykDweKFCO9tIJXfLeqgSWiOGYaxzK55I4igj764hta7HJ43Qt6XerCwYf3iIC8V2yjK0YbKxFMGzNhx_6EAD2FeuLkVqAjnE3oNyFZNaBOM4QT3YY2EG1vQobZWz5IDGinkx2UiEHXDeMGwgtul1evWfqytJp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25017">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4aktiPfGYEJqqqF2zt0OWgDZiblXQ74KbFESfuNmw9oCMbEV8fYssf9cq7ABpQ5ykvFSqfHThuNeUru4xpa1WQUxYGsqm95gmuvRJR5p0FroDmrhWtatHTjVJePehiBcEhydvo2Uif3Lq3mp7RhGEDc9MMokeQIaKadNIo6MvPYHIlBks3ZH1R_KHlHiK5lKd8Ul0uimPuDga3YTZI-4e6gQcmkNFIs32_vdLPBXrQ0SctEWbYilGlV2DpYv53dnEP39Yc20ufD-6VGhyXkgFKG--bzQFCbJXPQ9fgplr3NuW4MRK3OUGjORH6Ye2LzjKBLoTYUTpKxn3wSibFkzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0V-iDXcbPe5_sifhEYA2zmQIg14ir4cdxjhdsadIilaWaq0JhomwLeGeVuRG4vH1KU6stPkXfg7lZNhg376obs6SHl8kWmYmW8W_PoXmkhDD5HXzFB8hVLTSCYBkK8cv9mBrovc3RJodLG7fsfreh5iUH-NaW5SyyXP4Sxx-x7Ml1GWNuEfwWakN6tq30sQs6pHlbggfSv0tB15xgzFNQb0PPnO8yLzTHhqd53H-eSN5a2CMYG1SEv9Wc9Y-TUxtjfJCOhyb6b3Zww4gRAXRzkLrKIqd9XS8G8V9KZv72hN3zlq_nAooFqO-KEOb9trPHvnImgZKbxYz-hRvAaesQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🆚
🇳🇴
🗓️
۱۴ تیر
⏰
۲۳:۳۰
برزیل
🆚
نروژ
📌
صعود برزیل یا شگفتی نروژ؟
⚽
🔥
پرافتخارترین تیم تاریخ جام جهانی برای ادامه مسیر قهرمانی به میدان می‌آید، اما نروژِ آماده رویای حذف یکی از بزرگ‌ترین مدعیان را در سر دارد.
👀
⚡️
برزیل صعود می‌کند یا نروژ تاریخ‌سازی خواهد کرد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/25017" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7yzuM_Vq_11Gi2HwTup0obqume3FrTnnRo2oZNFk3o4oaI88-xF6xGAiNafQFsr43wsbQlaZubkyz1buQ22q1E3ycbJMzP58WVvE-kNmB1osKiZbKqN7Rmh06DKQSLYSozvBqGbg4MLNdR7eDztQa1WIpjq1nmhzWftDRzLnI1iCvzayMZMxykQhgzx7mcqbtwcdsRoVvsyEqBBzevgo1twpN5YNyZf6iY8TyoOocsVGIOWsJhQN7EQUOAoccX9YzIFGRNJCdLePsHX8xc6Jkc439YJon_uO_O7lwJ08w6e3gOs6_79r6kco5FJVFdEEkEAdd4nr03Dq1AgHky-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRizUKVIekKdzQ5XNQdGnahA2_5udmQ4AT8JPuzHWKtUQl4FcDQw_4DnKfutsXiwwyCBWCrftOYcpVlTSw0q9m0DhZEN4ZCwjbKBBky2WAzjUF_NT6kSuERWwIseyJTZReTTKntgiesZLjBR812uKm3V49_wenCzlWszyGewPixGVsQtkoOhySCwkv1OV8tZ32R4aDW15SWNJ-FMG9qjvZByQq1saLw8HaW2mRn9mGYvPNzLh8BnUD1qhPUeg2f9ZmCJ9sXsz0pWHojjpufI0BKIKOdoR2oQlgKAdL50wrr-MDwljfmf88-GKZuOPrnCJNY97ZELFyS6ImvGP3Qstg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUzfQZVh9DeHt4Zqq41m21n9XKP4o27yXG2jqw6H5li6UNkkWODjxUg-qEGM4gFxKKoHHhEER5N_XrtnpiKtlaZkM_1HNyZcEIJ8HyQd5VlnUwq7XGGjO44XoTB2F_-6BxPoDgKrFc4tuAtHD0D955D7BeMV5lWL38P3a_ZRGJj-buD99eYLYEXbcsZqZOUt7Yw6QpZ2AgTMHJ391bQdPBefaC78te0cX_13SCP7sXW1C0y1-Q-93pPeCceFUiEgx2aMJks6ivSHTvzu8Qtxs4rIVJc8RVdMO78-kSRAYzKpoBKikjl0_or4s00PxEVC0g_UHQjGICR09wKN1P0D-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQEaVbdm8aShl7X1P06dXha9WUZ1p_pDhFu5HZwVMWmvgPJim4jT2CqMVrpM5svmLacD7v3FthiotDs2sYjhVeYAzJHelBRNTyDdCs4tB9DzuD4iOYOj5HwfxS3tUSNzAyGJREwsaoQdgsin-AzS_5Ay3MopQ4chXTqLtOxf9A75zToaoaOCpjsqWZIalNOQq33G1-7dstPalBa8swS8G62fFma_t2MGESxqDzQp9NGnv4GeF2x23fgF38M4mJKp2xtCR4Efvnhy3s99KovjapCcDUj61R-FI-c0tu6WHvKL2l_FZ1EVdD0D0wMyTAEgT0WsoK1aTgqQDERVE3agkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZezubLZX1YI8vZR1YoCpCdrG0S6XCF85YnQUpM7dGvyFdbBZRwjViR5f6JIDaYN-jqqy64cMY-KBGYLl76nOC4olzxW2YvS-Q5XaYzvrG1aopqdgnMdt4T6vaCQ4nrmqF-ytFTWdGclde7uyKY6ODIvtLf2S0I2Go7KTow5BaENfV8SzizTupyNMmK9iC-9lk4tj9_voL-T_RTYiX2txxp1fPryD77NzOBBdLcvQnsV0mBXA0whSXHsf66nsMgWHDqf9_SVjwVSvCHyWgi3ebjuPolWXNqZtrvBVSNRJgR-9fWDB_xvvj7eYBkp5_jkKq6paLS6IxwOKuGt5qfz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_EqWEh_JmLDbzE64tkTOXEKXnUnkrw0xD6dPvOXxLtQ5OiYnMiEuwAGoN9_09G5ASyXZx5PCuPXLZJdoFImvwYnY7WA1WVi1nib0WAujBXmKpwRRtxasdAcSj-v4gt1SNmjHzDF57bFgW5UZzr9VwoiIvYnbC0ivxog53MRjwV2WRAeSI5qaD2MTcUUSijn3iQL87-sX-3jcYISQXagVMMv3Fphjsm8vYV5_dX2DTSAvOD25ErYwbmROdIBwTVm8rsPlXT-JZAqX93QaXT5dZZUcTkTC0DFcw5AzGOz-HtKwxW7onFOCEY6izxFDT_-GwDq60WPqHVl7OAvwZBFCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=kujPf6jTiDH7rz2ddLxAWzj9QnP_PYW5WvaMZspq23VQw8ps5eUqhA2huZ9qD_bzzPc48GUALZ3X0ZAFp08yoZEYNhggXl4JMcP4IYUUcTxsxRmbkcxe3WhBF3GW5OlUjwWo8ET19AdEmVSXfhxoyrQQr9qxHCb1Zc6xvCxlexFi6ZwM5gK6sTMdOTcaINfmTsMt-kNa0FWyBxUvjxtL1wS_WNmbOVFXP7_hZKq0vjiJ4VngmLsE8-Ul_mJa9U1NqIhEwXPGotJiYs739KcsTLGsOr0BIvHGD1VU_thoft2twPhlxY71AW36fzMK_1ryvqJLK5RHeeWueNrTdrDppA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=kujPf6jTiDH7rz2ddLxAWzj9QnP_PYW5WvaMZspq23VQw8ps5eUqhA2huZ9qD_bzzPc48GUALZ3X0ZAFp08yoZEYNhggXl4JMcP4IYUUcTxsxRmbkcxe3WhBF3GW5OlUjwWo8ET19AdEmVSXfhxoyrQQr9qxHCb1Zc6xvCxlexFi6ZwM5gK6sTMdOTcaINfmTsMt-kNa0FWyBxUvjxtL1wS_WNmbOVFXP7_hZKq0vjiJ4VngmLsE8-Ul_mJa9U1NqIhEwXPGotJiYs739KcsTLGsOr0BIvHGD1VU_thoft2twPhlxY71AW36fzMK_1ryvqJLK5RHeeWueNrTdrDppA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d8JtSqga4xT20xMPv3iCFAoXnTN8tW_8gbfr3T6udbWssmHMUws4z2GlFZs6fCEuKYuwrYEC3LESZW1bWdxF7mAGxi8_CJeuazpwQNCaJ1TMtxI3r05tcNvhHH9prEdB8YzzSc2insFM-5AV-XeAs-4_rcmaqx_ugrqwOJg0VUdFydog5hZCdkKzmYHEz6e3Bkuhvi7ae89ZMeD_ty23z-ljmuN-RM-cpmuxf6x8Gawnb8wqMpi_p6A6VcO1b59xGCzL5qJJ-jD5a1sPyxg0csJrzbLzoZgiM6ET-FLzOVlpLBXrOIJ-iz65GI22ybZI8BoaG8pSqYnlAl7zIh6V5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=kGFdw6fDmZXAcGCHqbAY6zPs_NcyziwwsxYX0YOD8DRTgPB0Ze-SNPucfGL4QTV1j_JKOSGOXuj4PxUvS1pjn9sKm5fUEf3NfZqW4fu29IrWqwkPFEptW_VzWRk19ORr2r_4LyRaHdI22AXqscVlnWJSDlo7Yjpg08jNdjaLKsyCF8YLaSFrFk7fEVgZECYIGEZ_ImL41kc8P2yRt7MO5kj-qaU11n1xN4fpx_YmAQ13CZ4RiLwDPB_30qZrAD8VZ9BNVTvqht6_QcBqz-wSWcfPKrJRFjsCcnokzbesWPXEf1JOjX91jJ2FMz90EDFEAaS0wHmqKGvG_-DQM8zOxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=kGFdw6fDmZXAcGCHqbAY6zPs_NcyziwwsxYX0YOD8DRTgPB0Ze-SNPucfGL4QTV1j_JKOSGOXuj4PxUvS1pjn9sKm5fUEf3NfZqW4fu29IrWqwkPFEptW_VzWRk19ORr2r_4LyRaHdI22AXqscVlnWJSDlo7Yjpg08jNdjaLKsyCF8YLaSFrFk7fEVgZECYIGEZ_ImL41kc8P2yRt7MO5kj-qaU11n1xN4fpx_YmAQ13CZ4RiLwDPB_30qZrAD8VZ9BNVTvqht6_QcBqz-wSWcfPKrJRFjsCcnokzbesWPXEf1JOjX91jJ2FMz90EDFEAaS0wHmqKGvG_-DQM8zOxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KswPZoadMJUOI7vjpvSJ7s-pklcV2ckr6CiHbYWkUJbyu3rhrzT15T03NjM_f_whAjBq7HARHSC2GPqcH3d9L1c5ULo0sxRc2lu0ZAWUnEHAjpoVK9uGBG96V11qt40ndWTtQYh-7KA0XSvexYrUANUgszlB-nvpdHBU5b797yAmnD44G6mQFmtRd2hwhDJRDcOuiF-uOh5MwzDZAHCr0wKGQ1CJpUSHR-Uu-248z2BjSvp-yqwvPyC1KB-yHc5fBKrSx7vmwoiwQSMAj7COFN42ZdWw2qriwknpNtrKkqvmFKQdsCpMNY_j0ehJ2-U27T5B5xxa28HvFbDSsStYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8CBiNpCKfiRwcFWsbl1npo1sqLMSIArPSm7VO0XCv-4CDPfx6AKXJqiljVDLjlVTIlhc819yWLsqSj6hclR3RuN8J85T9RzQg2VUXtOR15NrlwrJsFRmmJ6H5te-BKPfH7b3pAYKn8pp8c_RhoV8-bCFo-I4UgFw8obeO14DOczcm-EIL1vENm_Iy-RGc-0rulsViora2gRLbLDiPwAKLgxcYL9vyLlw1eUYAuf4Dy0tTTlGq9LJx3v6fLQbiK4bxXwrNyve-PQyAlIBZFG8W-E4uVVzNe8p0IJ5b53frCQSl-ySyUeAz8t3bnFXmdqCIJ4QSc1SEfEHVT01L-jxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=MTNLyuLn5z79axGpwTySNPoOczCnsHPddoxDFsJFl4jqP606OTtnwQZjJNmvEQRM53MHrW6189lMUgjdexwLl3tn1PBENZMHaX8mjDGik9q0Bxeoy81VaGw687mw0VvIJ0Mkyq4BWVBzy20Edgz1HBMUqorsVf4QD64Mde2942U1iA0K1bIQsIIL_UHYeSH7ur6SAwasnSZ98sEkGugE7nL7ECBXtRoPlFizpk2Dp_YC5aJP3d5Wc5lhvQsK67ZjgLxZVLwzIOq0FHdjo0ymzVU26oXpbxqMMgNQwEMtJSdjVOSxCherBHrOu3x92nT5lLuUa_77bQGmG6y_1pSwOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=MTNLyuLn5z79axGpwTySNPoOczCnsHPddoxDFsJFl4jqP606OTtnwQZjJNmvEQRM53MHrW6189lMUgjdexwLl3tn1PBENZMHaX8mjDGik9q0Bxeoy81VaGw687mw0VvIJ0Mkyq4BWVBzy20Edgz1HBMUqorsVf4QD64Mde2942U1iA0K1bIQsIIL_UHYeSH7ur6SAwasnSZ98sEkGugE7nL7ECBXtRoPlFizpk2Dp_YC5aJP3d5Wc5lhvQsK67ZjgLxZVLwzIOq0FHdjo0ymzVU26oXpbxqMMgNQwEMtJSdjVOSxCherBHrOu3x92nT5lLuUa_77bQGmG6y_1pSwOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25002">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7Ne1b6qeSd8FZ4XbVimCDZDV_JuvDrsoq8P36OOiby84apJcLQLzcfxQkzqTKBOqsl6gGEOxbvO2Y-jWTxquDOLF3hu_DJBb123XnP9ynCMOsRzRqWId_uDoj18uXlzL1iBqDVEVDFl4kte51cLUrFw8N5B7RfGnkKOiyJaM8Iwx7xSSKrDVfx-TqC7qnQiTMxIM4Fm5lzZGUXOuc7sRY6NydH3UI7EYU317tnSsnXmZXpQ5h45gGSdPjD-q87FVjEqApHpz5FoAPgUucF1vxcT81rX30objscuJcHSKdkIZ-sFBbI5ZjTcn88yWzdx6aYzRvteLNGP8IAK3i0ckA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25002" target="_blank">📅 15:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25001">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUgXgPSSLAdj9Qthp75kLfe406gd8zm8lUD0qFCLDq9NzDbihVbancAqlGceKV1QbjAWCSPLm-pWSCB982AWcj4ZtvJ5fKv2cFbj5JITXQY8hLAJIvT-tCH-sfq_iqYktgUZ_lAWkihGwzGpjwFxCDIxNxVPzpFus089sota3Vn9_tMiLNcEdZ4nMkOcKpHfxMjT9TatH5uIXKS4Sjkr1UasdfSHOAAPnnLlBLl9InmCeyQGEEWDO10K92aky9vn59Se-QsTNqe50BI13BikV1W4rtKCjeatSEnR0a1BlEMvBOvJGvrEb3rnAAS8UIzmb8myT2_R4SFDv52O5vqoWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25001" target="_blank">📅 15:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25000">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfSCZucNivh8XtU3oNP7ZtcgVm4LNBwIzBfgFTSyRIYoiYVoT3orOVTm0YLieSpW7CvcMS2rxEuNszuUFsEXH9B2_s7yoHclhPGtoT9ACLb-2o52qvwmp4oxgRUeH2LlZaVgMquQS-pvDlcjekOwHKnCzGmTHWf3emgONq0wgtBbD1Y8M3FkyeaqNYoZFDKq398ULsPiwUQHpAHX83Iw1PpWcfJp4JBYCiaZ89b1Z_LomInJnJytysvOE9T-wQ5AHFl8IVNBVDxGZhJF9jVgKDac_x1wWBBsbGqOCG-qrPEPgJ2K9Vsah-q4bxNhdGFe0Dt9MLILIYTyEE_ENMzBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/25000" target="_blank">📅 15:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24998">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrfBVJFM1OWcumRFVkccCILv3UviL1-KgiXGBzdukLM0uyjkUXiiMk8nf7bwe_vidwCPYku47JqT-OyGkARENbd1lkJvKnduEcTAoLa9aDIUQ4CF_chSCdYkcNxSs4cfy7AfjKgEY971Dgiq7CZ2aae8Y1FalFVjdXBiAzh8zp01GL4BO_tBLiDjPpNT5E7ue1KFhF1NzXaBsgk593UIqe1uAop64yZg_SBuSVKG47FmreampD1VbDlgG995no_n0xuURHMDz7VERKkKuQXCpa2in4A9RMzHlEbKYT1DKbeeggGxLU-X4-gXsIknKLJip-kz5X-j9zGXm7Rmpl_Gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SsssX5qLjuVizx9YsZcjYQEtPMU-axmk7XBofX3ergAeEei0M_Mx2uVPjwUXkyLbevNjq70GyVYqakFsnTFICnvlzDa8GbZVkKMRhf-UPWQeDpQ31ABdE84B61g0swb_5dSQjtsLWx7woYve4xN4kcveNx8a4_F2RsEaVzLShUUhXXP_qso1xOs0tYRsV42aH7u-dbXuKS-imenNtJxTMxd_Nru8XyiqyHYCxUnFeaCQB7xth2ZKcSdv8fE7recNic2NoqEde4OU-gGQboIYeVmyrnuYnVgmV8zQGW2Lqqo0yR7hIy3lSnZm7mOz_EnZcmzs1wENqXFfeyB2tl9TgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم
؛ سال2006 در چنین‌ روزی؛
جواد نکونام پس از جام‌جهانی 2006 به‌تیم اوساسونا پیوست و به نخستین بازیکن ایرانی لالیگا تبدیل شد. او طی هفت فصل حضور درتیم اوساسونا 197 بازی انجام داد و ۳۱ گل هم به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24998" target="_blank">📅 15:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24997">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkmzarUcy37GRuW-IryboSepL9zD-1MPJHcHl0cP7FYhiRRVey8Y-5VON5_pIZAU3NYETt_2gchJNLT0wpNCvvlG8RvJzFbgohCMaJnLJCEfs8CZTpiZk5Q8lSrH3PftBcZvDWCuALqtY2JacqR3EhpjZrRgOWr5obqNJTssPR2tJUGfHubMU3zKrM_E_IVpyZxbIjJIQNUGR5b4mzouTpbA_YzRFc2usbpKf2mi72rVRcKgUdAIz8fPahgjOQz6lxacRj6mJObrWL_Xifye5a8rkN8KZJPna_UnDjgx8HxEWLZQ_gRuljAoF4bmEYCUIqEbfcl98X52tPLJrkItew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
تایید خبر شب گذشته پرشیانا؛ با اعلام باشگاه‌گلگهر مهدی تارتار از این‌تیم جدا شد و بعنوان سرمربی‌جدید باشگاه پرسپولیس تهران انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24997" target="_blank">📅 15:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24996">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lS5k0IlrS_P1Tvrb7a_x8eyoAWKnoMbHBKcnu9CxTUafTOMhhm45LXH_7Fo1AiYE6dtg38lLyVM4M22WGzyc57nVliOQddpEVbqU9jMIv8u-GqL_DOltJFGt8JUMzGWJmXphOsBj1Jn1yioxwgX5kkrOl3Jh9HlGYLV0WkPKzQC4g53i0qCzcf7VRM8WXSBl2qNvMobTCgJAIyIp87LedEd-Hj4V5DsYNN6_loFWIVTkjVabojGk4OoRDLhxNYVb8pJSrOsZ8SVw-tf2LzTZiJyJHYP7lmhU0czwoLGpygIiinMnpkYqXP1QU4PFzGKtcF_gkKs-hliZq-h8OCJyPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24996" target="_blank">📅 14:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24995">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-ebxrj-W_JazLpoueCxwAony-_RPTIqCCXH2f0kvA2VLMmvK3BNU84ndKJ8XY0RWa36Hozk0jyFXtWNHe8UeJAMo0iyjXL_Ue577Fs61ilHmBlwIHN8xHbt7W-MxfIZrgMYbf47I8v7We_hWVpc5HudI8froNL7gb2c7nZvARdtBFa_Hcc5PwfVeh_FQGWrbkTEyDAkME4-ymANd8Qj9kFiSgiFZ9idIgbhWp_KMJ9l71Vm9zwlFtZbvwOFw1HMdW8BvwX7OeTTiQNYATegIPUhEzAS1IgjI_4WVHfAII9JSh5jJ9FmxYx_RC8Z0lcHR2ophGaaYWefIp1fSE48AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛ از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24995" target="_blank">📅 14:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24994">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWTa4pK7g26Pk4KEnAX1vv4eb8CtM_MGVOYyf6e5xWc3RRH17Qzxebp1PgV-ZDUDaqAijY5hId4h0nSkYVXh5ygsHOp8BkqmkAiVIYFUe-1GOsJc_sjyC3eAK2c-pUoLvITrkSOM1DKm8B_swWQHi9vn7fXjE1Xin83kWb1IbuTQ2ESuof4ifKgnPDnc4tjhEdKOhhQBfLkbqAH0P1t-5zcP0zNfuXEkQ25973-6uiEYmIkewrXWd4pjn-a02hoXWdvx1pHH4psLKzOmDaM5KKg0JOfUFdWgBJtxarOjCpXauYF72Num9__9enaFQ2eYv1_TBOllVbVgOoTv5PytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24994" target="_blank">📅 14:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24993">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pboEtNtmdQ4dEgkdkSKREXestPB5RFwpRKgygzfe3v_S_rqVvAv9Ph5CG-rebqqX-hUyFOxihM6A8_qlsNcWwvRYroNpjFhQygxHLiBSi_XKSd-D_H54Ji-x82x1k_ws9gPkMfFZGU7KjslV8TI6Yk4v0ttoicJH4F8UtYfKZhCX9ONd8Co9s9BIBMtw4rmFBTmvoNX8utacstyxIw92cr8hG7Zc2NJ_fbSOGixBQhrgxWelG3vuDdhpOSGL5kbM1TbyfPHXramak0T-6FNRA2ijK53KpMoOrsJ6Je1rYviIZ9shpmuuBkUZAGxkyKUAn5LPhIHoDDwdHxy47vK28g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار عصر امروز مبلغ 20 میلیارد تومان به حساب باشگاه گل گهر سیرجان واریز خواهد کرد و با عقدقراردادی1+1 ساله‌راهی پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24993" target="_blank">📅 13:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24991">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxdOSjnZzBuAYWqP5C1ZgidK_xVWwc68wgts-7zBfaUi1QpKWm9qTZ9I1my0lTo2Lvf1MMtKDLfvlaW_mgMCbAGOxPXJ6bGfrxpSRQmnFu4eIBtuk4otCS-Ci9VkUnpYTgnM8PdlAISGk8PGQ6bD7RQpu4xqfztDprrtWn9srk4cmBa7GPSKa8gwK87PCy0yU4nvn3YJA3bFScjiweRDV_xvOAW2w7EesRX49qrMGPFv46gVTYpZK1L0BGYDlc7V8jdGE5F8QmC-43WL_eoEKZWrshwrRuNGyd6OVj6c-akalLOTFds1eKvbsVneYZHaziP17-gfXuG2JdGmX1EVBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24991" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24990">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEnTNAzMVpp_7k2aTTcQFk7oeiu1f9ygvctyBUqyJ6PnYIqjH8WSDNpu3QGHOY0Yuvu2E5MS__D7ZmKIzyE0c_mvqAJ9264Xxl_0LAjU-IFOpwLEc_lIOZzLb5ejBzru84OUMCOW9UZmYWDLoCLIleuaWIad7F8YyyT5ipKLllCnjum5TxrNHfCnR3WOsgioQrFbWVzBpGD3xMKAEoXNK7_YNNLVZss_i5UYPELOywmKuAJvWeMiIgMQ1itp9CCxz3il8jRxdWLEVKGSKIH-0929O893X5tFWE9rdILxPV3AiEyihLn_1k6RjlnbMx00Sks5WVkO4Ixof7Znp72LCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24990" target="_blank">📅 13:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24989">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVAa5BXRTBYjlsT9RKn43o5zQaZJ4N8Pnk4noVOoLBhUgL_HN7gs8GjSPDG5-uyXyltqb2J2NuWvhdPMRsJFtxEiiFUA7zhZy4aVB7GQKv3-JA6ncigxNW52k0_iSoNyy6V_3Z2f3uItpqvUiiaHatzAVaoaygwAQXO4pXOHE-wwsW3Tt2UQQ6ato-2raxjo1a3FRKvZ61YuTlZdWJVt9KNoid02263mJDSKT8sNAg5kk6ZKTED4uBK_guUIRDo8G_n7KuCF5oJp79WOCV4d52gGlKeCXxbQxm4DFF8fwPVHywpJy5WpcYtPkJYtK65m-ZlgYQTpwwiqsWx25rSQbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌رومانو؛فدراسیون‌فوتبال‌آلمان با ناگلزمن سرمربی خود قطع همکاری کرد. یورگن کلوپ اصلی ترین گزینه سکان هدایت ژرمن‌ها در یورو بعدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24989" target="_blank">📅 13:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24988">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scH8ShAdeCD9RiC5lzvoDSHawCU5g55Swj7lC94vRh-uiiXcLKsom6gztmlRkB0O_0LksrWfu-QnTJnmj6AZht8Q5Ctdfy_tdjKVIIRAf0ob-m2oMh478FEdSVul4RSZ4pzpuN1d7HS1D9FcQxXgF6jXk-ZkbVr4bLOB8furlBNq-77lPQPdiechIcoFlzMQtTKEeZidJTfuWtPqEbNNC6T5N3nhNTvxz8EzJluMpCpyCK-c4aNzu-8HKv06m5jlWHTHjJj8rMvTkxYb5vK5heYICHH_JtD9XJVxrqgx1aopmcfIpIX3H078pQ7_erS2hy8boBZLfeqgo3wQ-dj0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار امروزاگه‌بتونه‌رضایت نامه‌اش رو از گل گهر بگیره سرمربی پرسپولیس میشه. در غیر این صورت مدیریت‌سرخهاسراغ مجبی حسینی میروند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24988" target="_blank">📅 13:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24987">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll9EkuL7IdocoWceTlaodEcn9fK6wHuH88evM051Tiuyj-PzlmEODelRs5ZqG9rQJKT_zqUre9lfWPSjMPJ7Kr2FxTT1jz_q15-zBQS34SroEBXemslozZP6X8kJirpm4tEHKCUBHRRj5RZwIwvb0WfKUgkHfaSe2ALurcp4NKdjSgnZcyJgUr_S--byCZPtfLNzK0gyWPCtchOmQi8EqWX5mjzwyMkrisArzFWNOHneg6dZToCJJQLMoxiFbENCXU7V5QZNzXB9rn4TXXeoD7Elh-SBBoXtUbOdA-heC7MtEhWBP09-k48uHsO_sahm89Ud3l6x2jlFz62VBpOxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24987" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24986">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXhm6rqbVOMki8trwzCMxJ0g9RXbn5fteE_dod8aFlfGWc_z8CiQLusoTTiOKn77Tw8EhICTwjjRQjJOHltPkfqU7-gp0PpenYN_zSo4JQWkx4sux8dqrfGHQISWO_3JW2vca9T9_ytpMOEiTtFlsrM4LHyPKhgBF4pjQRQ-9pgeNy4-mqT9Jq_MATOtlGXgJL3evvfhZ09Tks0hZu1Kodz5vNCWDx68Z0FCnSjxKnYH56qJ6Dwr5XAB_cvu6D8yaw0A73DsRu72eDQU296Xoe8w-oCglJMOtUrDLpZbksYnx2fZemSw5hfgERq-A-3kbEJgTmMiQInfrWunU-1vNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24986" target="_blank">📅 12:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24985">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Pp1Z33V7uo_TxAEWETGNG8jluLvVNMvQgZ-XXiqa79PONKJRP7bbOL6eHIc8JQdH8Kqe4buLdAX4K0EpqgmqPvp8Dq3uhHXbY3G2yOTm80AgluMKCZM5FWzQzclobFcr_lPlwrxwI9HZ6141bEU1WlEaCrXzwgxz-4KrXAwmxpFjBq9fDta3OU79bTyeY1bqYLIYJWXJM0lryHvevymniwEuLHbwxPsI53gU007lxOM-LZMNz2F0VcHWc1df5IluP6kLh-naG7NRAHXiF70_wB4GYEoZkWSQZIhXWdoIaYmpIOQw3Kb5wnXXPJrg-aGmmuxC3fNxIGgmwPNGwKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ طبق‌آخرین اخبار دریافتی پرشیانا؛ عصر امروز جلسه نهایی بین مهدی تارتار و مدیران‌گلگهربرای‌فسخ قرارداد برگزار میشود. همانطور که شب گذشته نیز خبر داد مهدی تارتار به مدیریت تیم پرسپولیس اعلام کرده خودش رضایت نامه‌اش رو از باشگاه سیرجانی…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/24985" target="_blank">📅 12:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcR_MFCiFCQh1m-jFR8XqTfFkcbzlXVTXYBGDH_WoJDyc-0J3LaAmyvHzG-3BGKM2OvRnUGQrprwcxBMfv8-63YEMxuWv4oVWZ8oVDiEBehsjcF5_9xaAPBgCuwKtevBhKM3YU-1HKg9HbKxsbyotmQ92u256O26hK19m5aplcuGqkqk4v2vtjuBCzeNPRRZ8MiQ6jFF2UV5KO_GLEJ3TnYcw5RsETmMefdelGRjoRpELAUFNZto3uAPvhDmAC-L6cRY451YZdjuXSoFHdHX4rfZ1JCLjeZY6DcgvJFPXQw62hpmVSGp_rFJMKtQrqzITnijdd2aYMF0LDYeyfAuXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edUEARLR7BC2eSBZVcfEIvxmO0anx_gfo1yyO2CwbMDokkFVMheygb31bLxBCmI98sk-AShozVvwNq8XxjFA_kscThSVdOJSJ_5cydHr_ZuhNUXOVtucbZ7leMO9pggr3VBUkd7e2fhGboD0iDkeRfsRDPZEO2UTIK4-sW5iwkVtqLiQ38uncsxFWRIYUAazQ14GXV7FsJhM0HGplzN8by-hjgF7QJ2UTi11o_D-Opsv7bUlwwoWuQ6Xfd_6w49ECH744c0XyCcV-Hutv-yOZ6kbf52WPlFJicEXrrx4UrOAV7PHJJMrfo54tGQYeKXIRpIU0UsT7V5EBYp1peMTrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIbfXvFJgpYY12qXE6WE5kRB2xjTYC6DiluQQjjSS1X5BwU1k5FvfDtvH0_CMKklwITuasZaqJ675jUZaU1SVNwxO9sOw3LJlrVKNb2aVrWtI6s0hs2AQj9zf97_IFzh1YEBCkDMaSPkGdVLnLTx-m2M7UrECNHcULEUwraR7NHYg-b0GPD-WmUsL-SvFZCkiHURutqU5_siRZisNSR0mezLLOU9nQlk1c48I1gr0CbpxrDXJ5pnv9uPvpLFnuzjCfqaoEMWc2Z-xymtZ4jd4lS6KdO3WF5sdDqXsMYfBh0PDrmK8DSTKTlqmCnHGR3OopShGGYsNJwgP2lgEjkobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_hbBr2zBMkVlrwOaHlttxGWE7jE8Hi7ne5uEzUIasMj1Tca9f3cWFHz20f9wggv0Ruimc5RnAsqbeCqlwUbmShZTk8tTZdBXLaXWIWxUugxYpFJImS6HCM56ZuaiTvmkOC8s0K61A8apUThdzLzDKcxb1AQYS0u_Cu1pM75f2tlRWjBSbriPrfwZ1q1jM0bujo_KYmfNgHsSJ3AcMy9HPKCyI8NRUAz8eVvf7buW6hhKeIXRje-nNu_1ueaH2W815ogA9p_LMduS5QmCPcQt5Gwm0YCiXMMPRdTtSqTtD7LN-CjLmqOAIka-eePzC5HxYklTKSNp4CEBv8Dd7R9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=Im98KbNkejEORgxkwuTGPz8cRSk7d1Sap7psNDhGhXY5bpOEVF1EYXYIOfZiRMtRc89PdnvXePP4BuRH2HEFZEORAtFTHlNkqkncuV9xpxkQftzRmtQdSrODZPTXeh9M9kQNFWUuZ1mOtpX2UsDXUqsOW2irzzQ6oWgOmoC-VYoGH5Kt6_vl8S9CDKfF5WNuC0nviPesC7QsH3ImUobF-3-UPi5PsGEcjE_jAL1RB4cvNIAmDimTFUh4aOcuUNConj9Oc78cjWxk6sXJuQRR1dvlkQTeJ5QQQv0VRdcuzycKElMkXkTYdLlCcH7uxqZ5BDIGhUvZ3gWfS6k6mNTbXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=Im98KbNkejEORgxkwuTGPz8cRSk7d1Sap7psNDhGhXY5bpOEVF1EYXYIOfZiRMtRc89PdnvXePP4BuRH2HEFZEORAtFTHlNkqkncuV9xpxkQftzRmtQdSrODZPTXeh9M9kQNFWUuZ1mOtpX2UsDXUqsOW2irzzQ6oWgOmoC-VYoGH5Kt6_vl8S9CDKfF5WNuC0nviPesC7QsH3ImUobF-3-UPi5PsGEcjE_jAL1RB4cvNIAmDimTFUh4aOcuUNConj9Oc78cjWxk6sXJuQRR1dvlkQTeJ5QQQv0VRdcuzycKElMkXkTYdLlCcH7uxqZ5BDIGhUvZ3gWfS6k6mNTbXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i323R-mxMYwF8Q6grYd5q5UvpAiYZMu3ttj7sFDAdwC1n19sLJxntmeNqBUf-IL6DoX3FIh6ZfdIXd-lGib91VFZtyp-Pl7_cqfbGY6l2KnkfgSQyRLr5lItppWHYc76qxuuLXjsYgjeam4aH3BQS3DWtAgkrqgnFxHMYbr4w7oDJ9q4YTkv8Z1dnzlramAlZMw01GXk8K0-uY_OMZRuQ4M9d4E-40AcP3GzTmFVt8PKqYwHJC4h3AP9XJqQ-QgG7nzYcwYhyxFFFr-zg3VX0I4h2zh8b0zVHrqfePKFL5y2-wrvgVkpXPc9veHAyobpg9bEfOQkWix_96piDxE1RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=VxjSP3-m7FQhYKUWbuvyxQrj5boZHt7BZljY7dOaf1zRIZ5gdnm5JXkN5m6P3mHgIef-RwNN8uJjZAnHCZ19JqLJNW8JJ_sYBEH79A7utu5sQvmrHio4s9jTmseJ9897IRfeJT95skxggsKECmef2_vCuyhuSlK7s-IuQsYFqgNMW2PDH1sdycD_HqlmJO9Xf5q_ow4rC-P44PmEzsDy2UtstRbyjHmv2jUf_rTmah-gKlG8tL6aB6NUR1Qx8MW1QMGnJsNo-sx46Bycjr7ZBk1DeIzafdXJ4g9cL12KbrIbFUZcnellBq2B25D4f3QRt-UybvyNxG8_QNgmen_cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=VxjSP3-m7FQhYKUWbuvyxQrj5boZHt7BZljY7dOaf1zRIZ5gdnm5JXkN5m6P3mHgIef-RwNN8uJjZAnHCZ19JqLJNW8JJ_sYBEH79A7utu5sQvmrHio4s9jTmseJ9897IRfeJT95skxggsKECmef2_vCuyhuSlK7s-IuQsYFqgNMW2PDH1sdycD_HqlmJO9Xf5q_ow4rC-P44PmEzsDy2UtstRbyjHmv2jUf_rTmah-gKlG8tL6aB6NUR1Qx8MW1QMGnJsNo-sx46Bycjr7ZBk1DeIzafdXJ4g9cL12KbrIbFUZcnellBq2B25D4f3QRt-UybvyNxG8_QNgmen_cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmQH4rzjobHu7A-GNXRthJJvs41YWrh4QKH_JqEYfE6Cusb-9zAOeC4Gl1CQ-sCQlAlvvTY_eJd_uaIJr4X7RprCQtsJgJdkfRlKE7m_zDiuSBGGieZTCeS-WOYlPXIIJtHDUx4TFKuwkxDqgGCfqa08JrsVFCwgk8LWqf5JzbeYRb77W-7tzZnwtjQwc23xbF2l3qfkMF_bmnjoELXvwC747OGaX4hq64esSA-oK7WS4fEm8SvMP8EJ8XKnVRy6qBZjiL3YGGVxPhrtxb_eXZrq-EMyjKcGmXIPXQnOg4WVHr0pzqYoNbg_yaumoWJEOnIlLOMVAkM-GbUlbY2J4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=JZoYUBaivnlcHvJennr9SMtqmtwMOYCFtODSN92uqk2Wop8smQ-fCM_nACKJV_RFbb3B1m6NUEcx8Hy3bOHlIpwocmbTmBHLDvyUU-xwrzEenlamYW4UHsEqV-bIDx9LDQ6TY2RD08IilwDqXVCBaAD130V477rv_GssNxPT3A47Ky4V_kcHEXco3cn1UfTb5tBu4N6vxmuNkTm80LI_1gIsXwb2d2EnjPzeWvFpltQmas0ZKRxY6JcPSaCESwWSZ3NTjaGg6Vzsy8H4LH2guovgHwSZY3mslMHZ7LZPs3vMhvL8vkJUhfXElymc2APS2QZj_PS9CAT2kgsI8vjwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=JZoYUBaivnlcHvJennr9SMtqmtwMOYCFtODSN92uqk2Wop8smQ-fCM_nACKJV_RFbb3B1m6NUEcx8Hy3bOHlIpwocmbTmBHLDvyUU-xwrzEenlamYW4UHsEqV-bIDx9LDQ6TY2RD08IilwDqXVCBaAD130V477rv_GssNxPT3A47Ky4V_kcHEXco3cn1UfTb5tBu4N6vxmuNkTm80LI_1gIsXwb2d2EnjPzeWvFpltQmas0ZKRxY6JcPSaCESwWSZ3NTjaGg6Vzsy8H4LH2guovgHwSZY3mslMHZ7LZPs3vMhvL8vkJUhfXElymc2APS2QZj_PS9CAT2kgsI8vjwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JABmkFAEkbyDqBjXkhK6tyh25kMnyt7A3a9nN8DyuiB14qPjZKfb4KIjzI3qAz91L2o7Jv3oxmXFyfsM99LragRN-V4LXGlpkY4Opi7TgZKs-_6OrqCbJU2T0lWCDIYpIwIlF89KeiB7NQd2wd-LDvQYC5X7mK_E58pzr94HqnnbVgXDc2ryTvO5EWgyyXsUj6JpAn6Azn00sxDzrqEdbO81zXKCWG9gMA0B1LEc0BBL_YghLcqJpehROrSUsXD6YJOFAFJu0l9iDBqWxUM4nMyP7OIDPtO8r0MaXdWxr82ULxdUZbMZS8-Ux5E_ZExMuJJrLz--jMRkDg_JpGe7LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxO7gcQWCSYtXAdVtKLGzshhOWJaczfxlQfve-qyfUcOE4c35EbP8knJB72agOZ1ariuTkqrXTS_1PGK2vV3sclUS3bc5W7S4fQbNmoJTRcWhLxHcnBll1mtHzvSqReQfMrrpZQsK7ydTwpH6-xUiSjDsXkzwYRpsFfYad_Q6-jun64wQvY-edcTnY2TaoKFjr7tns3qR-nCdF3iubs4tHhgabXq9vnGE2zpMf2COINb64HLj07gctO6QPSne9O_Uy_22mx153Ycq_pLqiZtL2ypXzO9OhUv9Y27yJZV_NTWg8-suss_GfQRGazj470gfTwO0nsHU75mrUPMYVeTnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR2jY1IU71urxetYmsATJFERSdFCFWOqLpSVBr3TnRn29ycjgLvGxxjCDY3tBhInhAfcL0lmi8ov8hEcp-Mn_Ty7k_k_-MlzTcrwG1UszerDYwyERUaemVg-vmTFtOiprKGz5UDdA9oWz-Q6w2L4cUwjClqN_4-0QXq2uBWEIIsz0oG-_b0gM598oJkJUnbhI7bJxsHgMSmXDDFLsuazOY7vp6eYlVIDXXNXVzhN-B4mkayufH9Loax4SI4xjmFZT6LmeB9HnPDR0mLcZ6fr6KqgDFSM0hCbaI6D2z8awPNyBekkpfKnDYOwmUxU8Avacc2R8pItKvi0MBn2sz1mOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Slg_Sf3XQRGgH0vC7NvcczPw3GNfReQ_roHMSACoiT_P58ACENBMzCI63UgAtiHx9SPd351LEVZv9YwSRnxVxg8HS7stD7nFn9EX-whA3tf3VHLuZ9CRhHJ7X9h61A7WxIFV2H3qqQWqo0lw8AWa_68AoqNMSanJARAWKbNO6qQiyxe1HUxAf506Ob7wwugZERYbin0RUzm2yxoPid38B3PCReayrzVBsX5At77p1WuwcVh7GosuDiqoiNh8fF7aSbWpO6TtR4cEtvogqo9iKvq5PUOp2Vx69YJph1nb-N8-WLfU9RqKUZb1w2nihae3QO_Ejdc_jQYucuEwaKXThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv4Mh0EP5FdgeE1P5yjiqvT7iZmgRta7B_Bn_624AhdKRAvj9NtvYtWdNrqZe-hrQWLQ1zF764RJc3D6WIbesLSb6RnmpxcmnqFYQfmIslqO7zMg5CGIgn7b5U5H5Q2zWpI-QkxzmQ3RISlJr9_ZGnKtCG3ijv1nxWqKGqE91gqlbb993MVfUznbdMxeQr49RhUCnTyTlta5VeZFpCYKiK5kBVvXlvijaVdDHNIt0aq2pPHdQbRTpvkqoiQCP7Ki0tnbceXidBUuKsazOZk1712792PlzFaNixDkpUwx1nvWGlhXALow5yRix9geXt0BJMtNpD7FtldnGVCBSdkWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyIGuMJtBitu-fw28su3gWV2lcBMDZnOYpRfmTyiDiCli4f6R2Y4ls8weA04cOiN95qJjXntbJyvzCl5sK9BDd_PirMa2ReKnFcRyNteaZ4-JzcoEP2Fq45Ngbt2fZIAhSmNG2G0UDMu8miRk45EYzk4_PeFMC_BUtjnd6b-a2BBHNKhRiOOwlHlQxk4SAeFmOPFLoPJRQNU4y-bSjjAWbN_rGDDcQn9jkQbdebTERcMMvHku2pSDPdJrDI9uxWVndg2cQfA-cCH7NB4BKt6bbzKVcGeVmdDittyT705umrJXmMqM_D-QU3K1hyxuvSX3vE6p9c8ZE1xOIzwFti-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMK0W9DaaHATI5PDz5vlITy42d5ZO1fHm1L8_M-Yboe0mZpWsY-aK3IM8xHzqGruD1OLUXrDNZUfMvY71ElUw8LHnsRMPBk7MmiCdMXRfwCvOhLRDJK3dJnA6GNMWUe2uWGMJksxqHr4MrBW0MVWz4Z4ebWgRKJyC3FJp6A-KCMMNR6jacvrU7Kl0hEJkLtVB1ncmkI8fFWaQpVtxo3j6v-MdS0soShjw2bA7fs4-56-MgiE1BdWMO6oyzJNtW9QNiRarMGnTa-cKGukk_cy5zoDzVb-x3rnWykhTlrZROeQir9aHyehgimbwJRZMwhVM-zEeLfjEmIALkiEgJCq_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls6BM2qtefXdzAMoGyX7wg7H9s-MBz0wKUbW_1MmjFIuQfU3nDTRYV_38q0wVhojY52c2uYdwGSYVSKIYbDWLcHAY4ySHH_YK-QluvVhZl1ytRWWW31c2WBm06Nb4sIqW9P_nW-CgePStIEP6_ErQ5q8HoSQN0-Vi0D5bXdvzpE-szsFVxD_DV9ZsbPmoHAUa6s5yPixfhM9ptJ1nNNcg9o0GTTAa9mXGsqnHlYq_Tn8MuFI5pynbQnNWy2IWTr9x_G8Y4ndtaMnNYdm-DnGkinPeO_0haza-QQVhuJRNy4mhJ9RjWRGmwcOh2bd1qQ2QkrRGgOzSgQsWllvI8JFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrTSkhcNTbTebQcyx_TiegcWGZRtvNw8RWO5dmzJ7Dk9iXuJIkR0u-R9R54r-nW48iRLnB3mBFC3ZuPf-1_cLToz0LRV7JN5RenLuZagkbIaAOaBiZkw45Igm-Tw3O9jx3-NPyh548TCsT1DwbuQLYiJIXrdnj57-7cnaK7rrUZoartQuPD57aih4xKsU5qIt3LWLnLJ-Gpo4QJbvq2ctOI-RlvqvUiWPsmpM5XCNvMHnWHDnb1p3wN-TQiaG1PP7eaETjX6Crqr9uRtDkybltZRSqBfmYyLcO7RHmOSZoZEyGf8R2jXO145WyqRue52ZkxCRfAnurhxwi0jPG1Rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbW8-C2_h2kGKAfCdgZ995yVgg8NdaaCpvoX1e8mRJ7_TsHL7hmDcSDcoiiXOynV7AqW-eWwa7zmzbA-z-nNMIoPS7Owxc9TqVZYLKvqExqKL6YChnNcAmfJnA3kIsr0IrGvxma4aGBTlIMjyUoixwcwwrTRsiIpEJdAzbPhb6QbbzpXiwrC-PWYg71pkbka9-WVrMSAPcp5EhrV2oFxs-apg867ZN_ucAaUIy_hdG-uwfoI45B6N_vRKRrrF2WccYRx2xK5iJqkvWKmDSvjYwYsMFjvv5nImDQvWcL1Ogyv6LWTP_i9IH1xtGHQSKH32YUvyT3YPo5IWPeRs1BQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkI3EoB8qrDruvXOd-2Ed2SQLs9joepGLXdzLbcaV6cw0fJGmkl3gfY9np2VEbhTr64Ow5kjiegAAcvZTsvM3lzket_s9bAa5jhGk1dZMGCZU3VIshcS2Id0rQjUfIUDqjBya7itcvC7fchCWYW6_iBZq6AT7R8rojPPCtZSFAbEeVha_iJEwfMi8BjWF1list_E_ftyhALFeKqjGFgm0BSTGoOpSFEDgfwUwxO7M2SYwlNfQkTCHwXnnRxT9BQHFg0JAc0YeCPnIuZhSVntI7KPyboXuEjFUCxuE9237FebRvmANyZ4E-m8pndV7NgQUk2dvUjpMRBFtkVxBCO2uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsMs-AQ_HyOvJc0GlqiNoHEo8ovGsfnHZDvc8uDMm8EXKPzMzr2JURY9FKX0yoak_kFF7EmY3r1paWJX8ysK1Iv9p9ldue3bmjEnu7QRQx4MDjTZdvbNXMgFhXSVG876lvQ_M2-Sg_cTejzM9EZkopU747GSxPPkY7HmGhHuAqQ9lANOEhZDRj23Vye-L8Hew1K5q-5i6iW9UQ4QmX4c-qJU9eqxNYgZjm7k4yqcgmQEFq41Db9woKNHIdww1xh8zLe1o0sEs92cao7P2-I7L7p7U8mCRhsTv-kkTBBZlIN4CtJNob0ACCUDHiWfwHK428J8kz0BnQGc35bAX1mGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCinD-3XFO_B2mfLd5Eb8kKu60q2XOT0twb0KszscF6jRzK4SRFF8bMkmSs6kqtoEy5FZ1z8-jVLDwY3DrSE7GzhIIGHW7e-BkGB_5zHS5XkYTUMPb2KmdbimWyf78zT-ATQtIBh3O5GEelySRA9LkTtlJXM4OCz6dXvRRDxji0-KmzA_M407oOK1Ldo11idFITFdBx_xUqDq3Ok4ddL5xeAa0bWnNTeCkIm46KWfljwO3SsYsNLtmIMzLDs7Iht3kL-N5HL-q2XZBBDlHVJVTo59kt35GeCwhJFRmfQIYc-Wpz7v7MBGQl5Kktl-ajckjS_Mn8eQnKueHZ1Gw0B_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0si8UxnlKlAiJcVdkGFuhy-xqKTIl9sHYX1PGsWeD2HhfHRB2bx5tFaS8rPHH8sMAALAy5EkAX4BePLMrf0JyT6HsG2xcNmvocRelwCntKfFi4ROwzpYjECg_tOdjxIjHcAZ_rPx6icSuqeucXpLsI_vCJlsU83FhP_FbUxGjZiZn8pNI6REJqs_Vh2kd6fUhukhSwUrb9qhEuDI9OH4nb6Ge9JWS5XeA_uQhZu4TOfUGhR35bHuqO98g6nml0pksI0Z6ZsppCuQ_zEQzV5jxJaGGgTwQiw4kZkHlq9WIsqFKIGqbgJztM_BvhE_-ZtaW97EiC64EGlldTqavVCHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPqG_stTypSBPs1c1R53xD9FZB6hwm1rnTTFc22ULw0wMjkectIZYwAsenE-HeSY9LUPktmbowmDJc90s0xfQ9TzTRtjxWLhXPM9N6wSEku7FQXHUO7ON8Q6jZSx_lupQ09Rc5ZGIsmVB3WAYLM2e1aQH0E_Q8Xh4Lx0L5JN6sfeADaVF3cI1u4OQD9QPO7guKi5o2epS_JSut6DEUYgIBoPWqO7uNFgmg_3khNQqjhEtEamIr9J4EZQzwLMjxddoTNfwxSqBHOSR9RODCoxmgPbt1rqUHop26tCLeT4xR_zBLKETIlh1H-VLYtgv_rDtPrl3pjG6M92Ajd6LeTFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUJnGlMLzt740aGbH-nd2u-6MydSSmVs4_5HOSGhQe6Y7DTnyknT4EtJJxB4A343H27KnoEyHCdqSni_7AmFPvNdt-75Jb_u8zLXwm3yKx2es75bc2zqoCezNPsd8CzRDRJrQXycz6-BVBvepccYNVdWQ-4XgwXuCubt2bxSe8V28-5ziybLlHFu_SG8fTVe5aA2sNpU7leQcUDZsQXPCU7e4QEgKPtwC7-KNA4KQCHAkSys-DEd7ubnEKIuevkBgcrJKRcn-2uAahRN1AFYtZt_gbYGT-sGerL6U5izR2UWHnULlbkYhYsU0Ficm15svp-Ngp4wcBsP0L0j_YuGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTHRbLfLIG0vMhJKpKGoQIwA3ap059xk31mtwl0ZH_odSj815HK2JCTAJJ1-97phwctGzc2Ec_PZQjweYD9rwCywKwuUYB-y4qNDf8HmoxHBuSmlVngVaZkHc2FlK2_lS1ZrQdXvoTmZNMJMXUxW2UPUhHVt4F5RuB9xEvk6xjCNxBvWkh3T3G33a_DJw9WcDoQ-_yXWUZi2Hcyu3CI1JL5ovEMDyIFyjKfqIuNorluR0meDP6FgOFAN3h0QR1BxWwOKqvIhJPd_UTRlDNa7_Gyqgxv25_E724VE1-Ss14h8DkVhCK2PKvotAcioekp2wi5sg5-vB9YzQAo0tcKk3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btdw8cJfjdK6kcGezSCbGtWILxt2newwDKBO2vwoO-QSjxGuk7Tsz27UPK371W568ooS6MkgLikgTcE-8VS3NKo8kGls0hO3cszZRC3YCrXVihYOqGuwMomSCuOl2fploj1bRqAD6iSStSljn97n7p6Yg6lThgcIL_rkEVDFhROCuiRN4SPOpBEeII3-hChxgUAAwZVXfbzZYjOwsRyariHon2iN9ybQD_-F3gBbyyYplgbImzbAEELieJmiogK-Ngm46aFoThJB21PgUH5SWRh27eoJFjl04sxKxsQ8KUN47cBfc2434ECrDUm37sn78kWO8riMu-6Oe3b_UNCyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbaFAyHjl7l9Ccuc1Ng9-7SeDDnfMfvtGmcmHbTGWXzVAGSIpMxn8urSwP8XcBRtt1C_jNsD6hksfEleUtyiXxAeieWFzC_r0LpPBxi1JyNwXavP1kFnYB-Ank8jWDvtVJuEu2RgDli4gl0RdzCtdtjJup96vSX7ScBg-rqnLdxoE7RYwFVo1Us5mPGeHCxjQcjUMTVLS1_iLOk5iKdziW_hjPPfl2ZP96hcAN-jKW69jiLSepehCfDIuAuxGFT4ZCdY-zVGvLN5Jf5VgjxhCkomOYixo0-6rA0AWbUXETZBeQBg9QnJ0wJvAYD6FxU47UN5dSyv0vq-gDNIt5gbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhi07bsgC8bduDLO3cWq0824zG0vJQLSGZSsGMjl6MwyZRIgPERu2_k6N1gEKVn22X5G3hwn8dW8jmjwGZ7wpIdvq4yM13wx5bGkQZy57Yf17kPl46W3p1qIsixTfDa6mfWwaw9BexPaF6hnijM4tEIgmm4FHCK9eCyFtKwc52Ru0ZwfSc9piL_G9-UiTDm8fVKjKm_Raz2oJ5Q0pGEKA32gLcbxXrJcaCIHBbjkUO_eN4NRgys0YEvp3dfylar5iCEJUCeErHbLp9cHZ1Khxhc_0WhTLf3GxmfYLppusoNCkG2LLunw7K7jas3HLHl8tmhPppHG36DRdVLsCpM1Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oes3MO6LFOzUn2CJk-2VEXw9zAD07XXFhZ-62MZWvTrXEFIdNh4LK2k3V_OK4Ohe8ClviYy1o-KR4ltyG4-9XN_hE4lOrFfrLR1hG6AcRoOaj8rFJ4A1ocZLqrKpmyqFd6XO_lFoY0meD0qZ3HKtYeAmGQ34pvGeg-K_yK1kvE4BZkNoMD0X-1ubHLIPPPGTSDmXfrWXvMssgRaU4vErWa06q2sa8n8qSNgPVZ_Lwfdo43t_LD0ArrL6A_S-ew4g_I_nY64i1bcwpSF8dlrBgw8NZwVPeW1NVdtWRFZzgVpeBRKu_XyLLqBY3XMA2WEfI1OE5nwExEyVd4Dwi6mTpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCIcU2bujaa2yH442zbl-ZWsSKbtBIREREEvlCWA2xH4ZjmZ9G8KAq_d5XzP6z6XGupVj9jHQDDhUlozCPGIISRe2wen6mSZNpTIjfdZiR-fDULuxNnKyWufBtKs8e-lI9h4WKQkWT4B29wlAtPxzqwtpU-SEq_LGff1Dx8D8YPUhkcPToP-Qn0oLlwt8x3QivZ3imXVFH_xk-4dPHivmK7to9VwqqEiABynQx1gxn0HY7T5Bw9ITSFZQIr1ZM9gw70gAa-CJQIQboVBATf_29QDORmiIB6uv6msLvbpQUA5pOulqedlGZ3L6pWmyftIQFXniXJyjynOoY7Kf1QoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCa0DvoBJsX-rzV1pRJ1_FLQiXjY8F2va0KHf41Q4iYi_nNsK3z-VTbghXPtKSeH4Ivi4cO0AVQothPPzXxzsyDBHHabZ94q-iw8VDoTYUtBvhQfZEA8sIlLftoN-VMzKAQ3JxsLtwRuZ6bHg5LflcsslTGS4EmqWReX6VCxN6jlyUZWyUpy0nNdDEgFoISBmB9Xol_svt7YipdXhbuWsNSwmJnLHA2T6VS19wWOOUAbOJofSMl_DCsY92DXkZE7KONJ99iLtn_VyT7C85Ksl3Db7eQ0a88_qt1PhRUO4zodKNtIaU-yHWyvKGGsdn3ZhF2Fn1Sqva9KyVMhdoGLEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlSo4fUAeRgytFYTRl1fPaeXRkXcjXAnQpwwEJwDO0rmfP2RpodSblARmHTtTSYY95112H-T_05qpinj5YMRrj49lscc5s6Pjxm0i-Aj0WPFLO0lsdkKEQrJpw20kJCeB--J_KEdVVmwn44IMLMyofbUlvlT6X9PJSg1VQptPD2_gJ8v4hIcwMpIn3DzjFBf9dEhSLIYNNQfm7cH9PNK7L798yUfXHCZKWHVMBsIv6qzBl4PnpXk0iJEwxdbe4e11ozTEAK61K7B4L5J8VlbV-q00Uve1KNspV1nG5tRv9y1WEZ19rgrg7XlQ0irpUthIC8GL0TyrHCq9LwCXsbWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ja6NkXq_4pHpRmMdgN_-PyY3IcPVPXY0PSig1X5n1VSi0ZlsCHdlCb51xlk8LGeBi1oXk8UMLTkd_LFZDQciYuUCWKDsYQaB7N7RKcEp4Mukst89Wd5jcy514bt3XmD50kxWjW3tFciKCa1izME0EmoZzmGJPIz4ZqJNEMDvetgisIgoNM1DmdmcOCTv1ptKKRCvBmL-NMr99a8ee4x44HUH4C0OJsqeP0BoNydYgOogXkvYw5hbGzI-HKI7WgqPLbmxbPXP63GH59mB3KvRrtpZFMSfOiI07FvuwVBgmwkDR03WM2LNKyy4Z9PHJhc09-hdzNkHJpTQcGn5pisYjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pe2rP9Ejl_VuaFykgnVI93HsMts9xEGNnHT0GJAe3afjkdiF8brdSs91UoNmboNQXDh4py85fKqLlPcQhN-3BWN123txSJSk8YrdFWWPGZrom3kx9Qp_DSXC0N5FG7PA-Ukx4EeYeKRUBFbFf_buxn9mhBQBdof2G45-e8aeahgK6grbWoJy2HBSE5uvMezf8KmenN2Di5X0pXLkgKmMq4TCR9euahoTNkXLLDemnx-d_S2clICeHgTFTDO8LV9CneUFGLktHLDSD4QrUUJ79PXD3qVWQ_XLRKDbkQPX7v2Q8sndUuHOcAjjhj-1Ru3ZgCxz7TuP2hdDrYLw5i5wpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frascqHU5_3VViaKF57Lx4rGJwineVMPposkX6yY-MS_ioBfyQHN0mzrG-9L3OdjRbBcgmghzUb4QJPNnMj8n1bfoj1NFP5ll6Z7kpYv4iYnpQjO96A9ESQc7aC6ePMlMCZrdyDhgdEHKQxui4fUZz84Gqluqy51X60NTJFNJG5WR6jeZ-eWIfcaWOA2yPPj7eekZHD8Qh22mBixlW_XNRQQz7f9mDpYjRQsn7DqrdaGDymo-UeTOyMSsQw-Q1XiJeJuj5F2Bn2Hr5HOTK1PBiuS9dNXEMN8Xc3jqCIIh_8qn_5wAtbb3bkGM3nwpg4ogyy9KVNjSD_N64FNSWmS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyLG07DBduoY6CmCf6BfWF9TY6wPGrdGI8h_xHdMqHnJnkh9SpXQCF8bD2CcAAFDWMhme3iUWLaeQAjh-a-w83hdD1lcTIKLif_oBGpN0Ht-Q5UT3DCe-fup6YPK0TptO6dhC8Bh-iKp-fninZLJHW7IcdPTLQSKraNQlGCVDGAUSDRCkWOPWfALHOyaN9kYu1FSIj0ExsGJ4_31CK8NOs5n4IFjZ-jhFtKnbaFr95ydQ8F0QRBhXSQDMj_iqrThJK0mfTGfVQSeUQ-brmLsB5eNEQUOvU4VfqrtGwteRfQncgygT3xW3nD7jjVcHBiH5KX9wVtimPA5SAWLzXDe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmDR5psPtIr_SZO59SEa74ZW7UrRabFHSU408V15if2BVBbFZ5M1M8qRipkvDEc74x7EZOYDmaqXOREero0578LNTHKj-WzSLHeu4BImW2efRjlrqPKB-M1NFFveW0RImcbl6FchCqSHvQKMGqjCYRAtEm_ckmEeCxaIodjaalbWZF-N4QPzZsrHCqdFh10u5Uvr1OTn1-_ztRhFfrdIAoeKzs5U4FlvVj7ON2a6dgmwVQNxKQVCwFWbaquPieZsLwJN-30neJ4mv-EeonG6Cf1XhE5lgtCdyX_tVhmzAd586tox8W0Z1HCBg0Pzre7ms0ZLSV2frWyLKOFwgpIvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc30SpuxcRPq6ljaN1lrwfYu0n_AjswEIIR0Y4LNGKjFqilBzaglFVK9IAnBetWv3oP2KZkMatErkBOvFz5ZgVs30n08bGX6EDUSl3J5bFNtXhsAMTyR3mUeRShLPjQvQlo5qzuDgUaw58ZrpLQgMMd0_HIzibEkUyS046KRbkA7MdsNRlSNOCYPjoiC8PkQx1nItGCwLPkMUTURT7sX1FIHllhfZoGUwbic7EsqWzn1xvaeTq6h4IdrWa3StZRiYqYv8gs8nz7vwHkQ1NlI9fVjud2apblBvb4zSidwV6hIeNCM8sgCRD_r_hlu96MVo8eYEdkPuy_kg50dM5DAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBJtnRp78cB8pr2ACTv1wwntYVBWRV_kxvrNetNX_22y3axvUBZ8GPzYqBnrH1-9IqCXgNvpU8TcDxSsRdzWoYcB9wDvk8e5ZCUwQAG96py66_JnZzwAetI0jSncGbCwm5kPHKlqqDof5lwqkzGLrQeJ9nMLx9cAkR3W53WfHa4TWw5ggIn-Xm7IrinsCzsh2nwy1RpBt5FKNwt6wCitVtgABSuz8OPdpW9eMCkbEFMK_ajQMWzmaPUYxgbDsyKxB5_2eytAHPRueF6_9s3sYSh30JJFfaAt_b9CNZen2N1a4smg7Tza3ECpKhkauwiSjRpcrIrpOgmnzgMyc270GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bhzIbYRELmQvHnXZI35Gp0EylfzrWwwbE13QfYN5YNgnr1bYLWYQ3fBdub9BAabcgCVxygg9uJi4I68BXDQM2PTxbRyqnjUYJAGVLm61uDc3xmHjn4v3XDZszsqRkZ2YvgPHRUUPTMds9r3-243bNMpWEUYEIQtTTjbWP6qhFjiFsZtHGSk71hHSiZINIWkun6TF6oehioexKYV5re61EL_9rlPqYNr9CizQBRH_1_RL-bQG7AhYR5yJeGw6wVRLrb-U_APhe0IefG5e-lXUyevpQYdPNSAECTaJeGmTLdi3V2Ai7qkpH9EhUxHmPvARGIYFqS520Fi3dRzDfpCqkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ar7Fi4qeX23lvlPwiq9t5fmNuToWfpx1EvX2gEEnBsjCNhPAEuiUnfNoBt_52Oq3oBtgUvtMnP2BXEGJQoFZa8L4dzC7aRkihalGWb-GElAyHV4WnIp-Kv0F0QUfzXlLvOkGqeB_Txi32I1aB_9r5Axz4t5fERtpGRJW7MPgG8JsBqNSC-Hq8A4L2MAGDfPmP-R_ZODbdDh2jerJIgYaAEoqpN6MRMNBMarvnJ0uGIzNskuczlnvw9R3FNSmO9nk4AAg0GR10MW-F_mOw96K3IxIuhiOZ8JzXQ-i5nCfcqQFZ4z__9cbUbrd19c_APX_RnJ3bQjdr5kO4VIGNlw4Nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=Ju_D5eFYKwFhpqXjIy3yVMjRGmayFO5bllBn5sLsvySjw5cYCOzQA2p_dOInoWV4zMMrTIcQ-vv3jozUUqMl9fO2yWWYSafENh5tRw1IO8BdM2c7rjhFceIYYTWYCS6bjVhPcMzfdtmxePWpNdXon-4yhD7ntfaiVWYjaQtY3JIqSFF0C3fPRiPUQbNeAQjq5M4acvUzWGpV49YOln48SeT8UbNOarsv8d2YVAdCtJji3OP61CsPeFuBoaB2Q8G8dxo_whOixnIIkdzYvtdCZuRNPGFLY0P8G7lUQkVNDROnThiBCTr1OijVhp4L_FsWtODPNAUs5YEprFiRilklAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=Ju_D5eFYKwFhpqXjIy3yVMjRGmayFO5bllBn5sLsvySjw5cYCOzQA2p_dOInoWV4zMMrTIcQ-vv3jozUUqMl9fO2yWWYSafENh5tRw1IO8BdM2c7rjhFceIYYTWYCS6bjVhPcMzfdtmxePWpNdXon-4yhD7ntfaiVWYjaQtY3JIqSFF0C3fPRiPUQbNeAQjq5M4acvUzWGpV49YOln48SeT8UbNOarsv8d2YVAdCtJji3OP61CsPeFuBoaB2Q8G8dxo_whOixnIIkdzYvtdCZuRNPGFLY0P8G7lUQkVNDROnThiBCTr1OijVhp4L_FsWtODPNAUs5YEprFiRilklAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuDYgYgeQSVRxYddlRWJ8SqN8QkKXoEQk25a87Ildb-ukNFIQm72Bs_ofvvqxY7fNhFANytD87UkIjcddQX2JKf0Yk_Wk-3qSotUYadNHaW88qRJgyT0xGdZQjR8fsvz_60zkNPbwabsdHrVYpT3abGIODVCQVm3fMl_Zwh_REpbo3bmDjKEuOHhsC4JDmzw10I1coZCgOjRxOTXxUcNrA-LBb6kV7zZ5Vs3mSnxRu9T2QLy_E9z0WegR2mZ2iXzLg0Cc0eRtghR17Nb96CSuftq227gCBofVIhUE6D_MBizQh7e4aiI_4R8gzAoTjXi59SQQSNF38x2U1_ozDZXog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9J08o_nN8xE8vX-K33GlG9aeqW3-siqWeK5OyOmWG8g-irOd8iLhTMdruSmRHppW-rbwrGf6joOY5hCdXYtB7hH1aHA_-wR-M1DNaavdClbDXF_q5J427E3i47faqpbfBAWlFA7gJm7X3AQHdHW556MjmCXm-2xzm-I-02WQqR4yUUCpUN_9uXTjlE4KUSU238E2VoQ9rTkEmWLwMvBw8lvIa5_1as5F06SOSDjhpIPagVloRn3QIVjsxTmzSoWcm-A8-68e53lmV5FC0-A-UEC2PKrnJ0ZIH3zXY2Z-QAl_57K3fI5lKjlEJDjY651OlcEjqOtFBVW38C2Ec6mdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1-jp-L1EMelSH2UAyHqsA4iyygsjOGZpD_u-ObvMzOp-yaknKLV9zCRp8TZ-1GOab6C9vULK9qakizkIfChvI-nWIO5Dro_skjlunXZoKn3XH9cUqpDhbJXxpSkM9lKh9z2d0Vst4BLk-S9dA529dlAZNkqFyQsPwvkq0OIz6WxagLzAulI40M4XyCRflbdQCn4ScxTFSHTSbJd7FFiivI6eyvvzfd8I1y3RY0CH5xkcUlmoLFp94HMQkjAdyvarl1c99V4AiqKmHBW6VP7EbinrLPw-aAQcQ88U_nZtWXupEuoPCCcyTc0nyNma5SQsdvV9Bt7KrQ4B69-S10Aug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awkrMTxa_2y8pylq_nssOzS9zH6xDqCW-DbKvBeQWijnTxEwaKGPLwNv2BopHBuljnjmWDuTXvRK5-wbcw9vykhxwyDRXR6gUGMFmpLaKE4LIXdbqfHFQ_KpP1Ms_BKs3IG-dOEuF0-I3aTdss_7R-MIvfhXXF8A4I7wlQR1c24K04ZBiEBGJq1D_wF4yojx2cuVWMbVCWd9vYp4bO6ELpB7IPQK9h1xxfqBU-McoicF0vQdZD2h6hLZZKUiKCyKILWBGn2x0ng_Er9cu5KO7zPYBHDe3P2WfImLZinoIBXMatYF1b0F1uIXFI_9lco8qQmCfbKtI1mikVh65mFgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVbg4lDS1C5f9M6i5NE_X_mNlhlLGmV4hCOo92aaIIUnltWaoErUETjcJiHg0_xE-qvAdQF8jlhAFL2DPWo-VsKpIzYn9e6WNPwnotHe-hfqd9wai3tKXM8qoIv45diRnImk06T8AyRzZK3Jbhl5xd2qDys-orCbE_bqhkKfx2F3PPSDVm2RP5m9dxPegEbaDp1Z2IhoGySzXpWFV9fG5pJP8Ns8z194-gyNFvrRG82cbylF6fUzjNFSuGm5ImqW9xCjgmnFbX7yBQdjCpp_BZmmUi7XhW3nplEiVKYKkM-fyKdAzRvX3XDs0S-3hswaKc6-MAR40Yy37Q1lrvGlyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=YI10982WhIuLtCu7GRTsfmfnyCPp23Zin5z1GdsJA6PcB2K0BQJQDfF5GhtIK4_rkvgeE7R7mGxpftd28ughuDJWzv-Er3MjZG0lV5dxbvD4qLGJR1odizWFrNzMKe3PAQ-FVOS5sovUbQo-1FAnZpnNVPchvVR1rexlcTZO_waRsakz5KKK9dX5H_3rAM-bV8Tqw4MYgkRGyncEcmYG5FclzHidjt8outwQxsDWyYHDP2TpHghTW6xDtY-fKoGiCThEypN7sFhpwsSee4slJk839TdWcYpfoKJ4nqVnHcJmOWtBe34oRwcM_LpujzEJ3rA3DdfFlJdZz04KkpnjmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=YI10982WhIuLtCu7GRTsfmfnyCPp23Zin5z1GdsJA6PcB2K0BQJQDfF5GhtIK4_rkvgeE7R7mGxpftd28ughuDJWzv-Er3MjZG0lV5dxbvD4qLGJR1odizWFrNzMKe3PAQ-FVOS5sovUbQo-1FAnZpnNVPchvVR1rexlcTZO_waRsakz5KKK9dX5H_3rAM-bV8Tqw4MYgkRGyncEcmYG5FclzHidjt8outwQxsDWyYHDP2TpHghTW6xDtY-fKoGiCThEypN7sFhpwsSee4slJk839TdWcYpfoKJ4nqVnHcJmOWtBe34oRwcM_LpujzEJ3rA3DdfFlJdZz04KkpnjmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=FwfkFI9OFk5hn6BgmiL5mMLwhKyAvprbnAe7cTLp4eeWGNIy1vByTIcvC7fGqRoIYc1squ3SWvXkdCHsMPdmk7pf5-o7okY9FLOeIj0-brijOqdtv0aW28xrWHnncHUyS4Orc37vLPclcBIUeLTXZLisGf3frOOVv_Q_ZY7rDjTfQyuxv5u3cvf3xppYT2INS5NjChOGv_4yCv01DR4kNQ0SNm5lfCcD5SNGNyUHcJcAbdqEaGoMf70t5t1aZE3QOrCdZpvdowRhnIHKFRsajc-DtgAWoUcGPXWT0CYcGnBVSjAUi2GNwJpKXhw-LbmrAyCIYcfx-yzfJI_Lts1sGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=FwfkFI9OFk5hn6BgmiL5mMLwhKyAvprbnAe7cTLp4eeWGNIy1vByTIcvC7fGqRoIYc1squ3SWvXkdCHsMPdmk7pf5-o7okY9FLOeIj0-brijOqdtv0aW28xrWHnncHUyS4Orc37vLPclcBIUeLTXZLisGf3frOOVv_Q_ZY7rDjTfQyuxv5u3cvf3xppYT2INS5NjChOGv_4yCv01DR4kNQ0SNm5lfCcD5SNGNyUHcJcAbdqEaGoMf70t5t1aZE3QOrCdZpvdowRhnIHKFRsajc-DtgAWoUcGPXWT0CYcGnBVSjAUi2GNwJpKXhw-LbmrAyCIYcfx-yzfJI_Lts1sGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYRPSsTHH0HB5dFYr_-xWvWEz-xd__-P4YFcGyX7W9I-8s3MYmE2XdRXucexeKd9TjeXg5yNKnzTlS6F_XVnqUZGqkNMmcazBjwa_Ynj6CyxiZ5x_OvWFVZu5Y-D6Zsvp6KFnjhnOBUw1GOpWe1xBBecLmtkZr7GrtZAIC1ZFOLQQ3OPqDn2YW58QBnTL5pDV9_KV2UfYouE4yjy8Gk91nIYddldmb28Dg4N5hCUMbkEo1iSYLBFSrFh-EvYV1JSHump-Kta1zkoRSBlGbX7EsJxbRiMqGaMQrCWjrazGmiT42s_wX8biCqqycDgBGA_sKGfA-ByPucP84SRAfNSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5yp6KX_Fw_XxvmmmWnNHnvPr26ifSWCxbgJfXfLb5_j0Bw0oq6K5fWqwb24807vBWLUtbODJcpgsrU4N14SGS8laGW2UOfF0bH6NfdJR0NtAHmAvH-sFA66koR3urNnvKdqKkI4DX9FcSlPvy2kpw9J8uxDiWmDelpIjpVDUPkycTDeME35n-LbL7C3pIXU9gdI4WiNfGL_nSgPeVA4E_oqYUpl4W1FIG7qA8yt4BaUVdxPO7MdghDauF06-dGGtON2O8fffj_5k1gbfS3RCJxSPCMuu4BYgUjgrhygm2hGlq6pfVwqCoR2X-gkfJJ-leHbKQtY_2z76e25pILKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFt4TBAB2ql8sP1GanJKkl4dzsK0-TfnM3yc9okN9j8X5FO4Ixwv7RgZkoJtCvRNulnGmQ9WQxW4UEPi-m2lloSe4L_jGIbx33PS3t1NhDfga6h71C411DH_sx5INr7srxQfWydIoiDhwGcZwGH6ZtJ-Kb09V6M6jV1-Pa5tfZDulpRjlrrOLZPFmP57KE1DnZ0a0tuaT_HMA0DStMufWgUcWWLKrFx2LHcghmNtnFWRPZKqLUb6n_V1e-aO1-acL950mtd-eMxKvq4lqp8zzg1PKCwXKmnGThL7XHo4siGXVi_o88E0hCSXJvmdKqpPjCNm2MaPN1r6J2JWlv8GhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiM8bSZTrL-zks3Md7a8E_3dTo7-E1N-cojEzqfrbGSf0B3U06zqm9xE2r1NX-GDaq9UTP11NuvOmfZW2IVuxp-tUdMZi-3pU57VOoEzrgJg0L05j6hwESlM3qWUw5bfCcCV-8zBq4Ex9GVQxICE8yx90-wxwsnMGqvxsmT4qnGNT1sQ0HN62x4b8T2vfmw-QDidMwf3K0qDnQnMwoyroIbcWLY4_l6PrGGgNu36y02klnGIEgxV-xmIlKZIlkdUnCcxdzbhQuLSrI8KU0XxaAzOl4qh1uJJbqWo_wcg-Z22t8ta-eGtjGZhsDukzd3Sy6LN2wXMzFBc2lvwxNH_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDIvQsang9imymxW9k4wpSTodzrOJa1H0U7vJpep-9usrkDgkN0q9u_4IuckIFXGAzcxzt6F4Zb5h46jzEhvgoHkpMzBNZgSkULyjm05NaTnkpz4D6AzXnHEHXvMm9So3eL4toMKwlPq32N6GbtHpWxMikET2tm8EEwnkOMOMIXmT9iGhNANaXLDLVCb9POvTMpQVUdLvTnEhuDLNyTRTGz6fgdOKySSo_ycE5k4iiMgn4uJH8bVDpGk00lKPCSnji7UOaqi8kzghYYOO91h-REX_HCBVqhkw61jvxWt9PLI3bC5InnWJ9qcb03u9OmFIaLA6G95TFQAJRPGvs2Lbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OX5Oia74D2HpRGH4GtHo1qGHkvKPVi6v-sJuICdXm8y5JPrn5TTE7LZtumZORRM0Jh1MQMRoRYbMz1TuC_W1P8EoDAbVHVMjgtyxJQ5RiJLaSq49xZC6em2UQVQHhvHLQFRV7-ns1I_2NW0imF2atlyNbUxQ3T_bywc4ZYCVhV6Uf70xPchXrKZGKqgKnjHb6z_b4whRVZz7bN7VF6glo8z2j7GGot_Ig-BNoUdExpUkmNXLlQSUQ8F8dBQfsAlvwiF-acEdBeXt23xV0k-pxgYNXmXizJLsc_UQHdYoCMCd1DmSW8eQYsQFPryW2i8Ui0zrOMh5RQn0XlyfXhF4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFAZ6OryZGcHQe_hz5ooPP8c7vVD_W8THk-U6gmz2ej3ESrZB5mfAb6k95FOmTL4a0T1a7nVn7trgMa4qdQSCovWcH8RhsQQIrTsYuO8ruvFqEVcKq2WhvHV2pEOkAtkqZNsBsP4q37ws53EWo5pZ6Wp6eH9RwJ5g30DIqjDGs4iYX75LsHOQW2N5YYKrUjdaGcAhVNtubaHfI20RMRvZUFVKeAyR-6FvkiDQs6X-LymW_cCLaqQcktHvxi4Hcry18C8euh09T7AqfvlWc2YwoMPn2SN2RUrDOJLtcJoTObEYFhPjaiWA4mimo9V58e-afTsqlRm9Y648GAe01xLfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=nzvLz3YoPn9VqHRc3M3H2Y5OrDMzwuEB04yesl4cUlE17Df9m0s_5wqiATbKVDoZDoaCqVJ8tjHghayhkTN4dusnC8zwnE8joiOozBPllfcG4busSUrJevUEvh0yHjp8i3we7EQ_H6mb05aL0xcLHdM_D3ZRmY1hbbpnICnVN_Iw45HW4nRPurKAk-et8yIKmZqRuqn_4AYacTBn5LQR22Ku3pIkMPsB4edDrT3cAzKDicAVHj3qBpPEbFB3-7TLU0ZJzGxciVHBYjVzkxWC0mP6cV91m08yLRPEYDWaN7HpXQJyKnXLwZS8QKBDfdtMijvSl3u7bU_HJSZsuh37tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=nzvLz3YoPn9VqHRc3M3H2Y5OrDMzwuEB04yesl4cUlE17Df9m0s_5wqiATbKVDoZDoaCqVJ8tjHghayhkTN4dusnC8zwnE8joiOozBPllfcG4busSUrJevUEvh0yHjp8i3we7EQ_H6mb05aL0xcLHdM_D3ZRmY1hbbpnICnVN_Iw45HW4nRPurKAk-et8yIKmZqRuqn_4AYacTBn5LQR22Ku3pIkMPsB4edDrT3cAzKDicAVHj3qBpPEbFB3-7TLU0ZJzGxciVHBYjVzkxWC0mP6cV91m08yLRPEYDWaN7HpXQJyKnXLwZS8QKBDfdtMijvSl3u7bU_HJSZsuh37tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDsE9YNJeEw37ke4tSnDWvuDYBexO2a_rOlMWNu642fxfxQw0hOghZmcBDveI23r5Di4Ey7lGudXkgkJag8-4MX4UrFKQW9dBNQeDqv7sLDYj1VemnbOiKXiMuSu8q2xBzxBD3Uckd06whAY8Azyu0O67Y9ts5WJ6UxldOtB1UwTkRb1MfCtFn6G3bex__rciL74qKhBg9pSl37Pa5WMbBs4UQewLGFF4wKfI81kdSFa2KGvZGhj_t97MuWkV2AhbJJBkyYSraPWRq2qGcGvY2ad8rDQSzdlVVPQpx5SxaNEv8Vk1jXn_1QG-Vx1eG7Pxn4gemW2iHfD-r7zjWfSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gThpzwCCCayLmb7vnA8Nn1dyZ-paYoVwGYBb8HC25TrHAC192z74L50b1A4h7LZm7NOK8jUktCCrROsd-oO-8GLmGe_yWSkx3eaUg5U60aNg5f0i-wB-295admBRkdCON0Q6PvYbx6WSANlIj20fpJMclXl-Vi964IS4YiQ1lnwNWFWl2lBeiL8n41x-NHYSygNFNHs8A4KprnQmyfsLsrlrMRyXwvics7AYKZnpuD_eej1k59UrTpc1StiUrW-FWKlWhBZPHH0BBOuw00UFe_rjGkbRqvvEEZeuhZZSzzkvoumleWGnD88sfKJ0et-9vzWaQcAAjYtVtM2BU7xqrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=QGGGC20ap99OXI9xW23pV-WXGow5HJF_83FXEIco1lcKcQxXHD-vwRbwDsqQ4AexIDt2uRAZ0WzTJ1lunjJyyPrarksgf3SCKNcTH0rr33oT793qz8N6IJLGL6Pf_G28L1iTYCD29-bZi1fwIDA3BiWT1oQBH4l7vuMbG1XE00GeI1OhHcDF49zAz54KbKcucC3umd7GMuhuht0ydfYTI10Wc_4-xK6azPP4mTWtnANV8W6846bL5RpY5C20646M8Imuh_0R9LjLEvnRWbkU3tDtV7FWw3RFOXtRqNfsNbvypL3572tWMve-GgHcZveASzPC-8cF2B3nU6qF2jSFow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=QGGGC20ap99OXI9xW23pV-WXGow5HJF_83FXEIco1lcKcQxXHD-vwRbwDsqQ4AexIDt2uRAZ0WzTJ1lunjJyyPrarksgf3SCKNcTH0rr33oT793qz8N6IJLGL6Pf_G28L1iTYCD29-bZi1fwIDA3BiWT1oQBH4l7vuMbG1XE00GeI1OhHcDF49zAz54KbKcucC3umd7GMuhuht0ydfYTI10Wc_4-xK6azPP4mTWtnANV8W6846bL5RpY5C20646M8Imuh_0R9LjLEvnRWbkU3tDtV7FWw3RFOXtRqNfsNbvypL3572tWMve-GgHcZveASzPC-8cF2B3nU6qF2jSFow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=P0Ab3Dxvk2tRBoUOovVFFy9KGMNpwJxKldUug3K8d4CnzGNCBn9Mlw1tEL4B1S7296KPlVrcrQYMf5Jef7g81dd87QaLjP7dJQUAw7mamA-yAt7smHL2smVKcjjj3khMCw_vhpcvVTXiCtRmpg-9u1fSH-CJNeZTbdhn4mrvSCu5ZPHXw-XkogoXazF_sL2g8bQzP17_iTIAPbETk_Vbb2Sschkl01uUcWqypICB6Tp6MDztgVQRGwEPVa6H94MvM1Eav3xJhU62U9zSVEcQc-CnSrjivblICGxvncTXF71sS3lEtG2X9xxgm5QKMkKO0UlUWfS2d0goBVVbJXB0ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=P0Ab3Dxvk2tRBoUOovVFFy9KGMNpwJxKldUug3K8d4CnzGNCBn9Mlw1tEL4B1S7296KPlVrcrQYMf5Jef7g81dd87QaLjP7dJQUAw7mamA-yAt7smHL2smVKcjjj3khMCw_vhpcvVTXiCtRmpg-9u1fSH-CJNeZTbdhn4mrvSCu5ZPHXw-XkogoXazF_sL2g8bQzP17_iTIAPbETk_Vbb2Sschkl01uUcWqypICB6Tp6MDztgVQRGwEPVa6H94MvM1Eav3xJhU62U9zSVEcQc-CnSrjivblICGxvncTXF71sS3lEtG2X9xxgm5QKMkKO0UlUWfS2d0goBVVbJXB0ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpZPh97PFcPi9hsMM-2KlW0C91zY_24Ux4LAEaWuIj8CbommN2sWIwWp1gmZyACD8FGCgaeWp7MV7tcxjA0iO_B-oWqsePSpeBuGq6XPUnVTZed1qzvZdUu4G_aBmMywi1rmIqM5tk547pmVxXxlWNypa6ZKWO8LF90HNPPDrLHztbwusxDoxXIkk7NKV1ZP-GwCJ7eqsEY--gzhFgQA_oEeWruT01J50zfYHLroFdNYtugfAzjBYjBFtQ8H-ROxU03FM2oT1-Ni4Hg8lcykW6zrGs2IsCfFWLal-ooEn3IZjzpiNAqkd8TvWF7OCPXlHkKj5Ocd-WzLZF8vE0wQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
