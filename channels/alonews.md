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
<img src="https://cdn4.telesco.pe/file/jW6S-yCiFaKFmxA6l3b4xDlSAI0NDTvuToXB99bn-rwSRY0DCw4KkswGTKG-TYHbPE_3nkr69dqX6pKg6D6aGRQSUwghNo9Zi7nbr2dt38UBQr-Qh8bj1Qrt4XDC_F_tBebH10Kcpwyx3NaPml8yLjpUEeLcI1MeNG7nZqoWT9vEK7jSoUZp-lhYlXCI9hXQgA-62GScjRlZlJFUgs58QMfaPsD3zdJ43VlwSgx-CyXVz8pf3FQuUjz_4ECkSIwWr46UbJe7Dxy_tTuSyCIUbDy9q-abTSWO-t3BWmdIJaKHbxCI-PrUKuFWD6vHlIJhh48VpIwqoh1gC2aKCZj9oA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-126710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iIGuoGirqsyMz_r4ecCxroA72vgx9vace8z5ncfDwzzgUD6bHUq96V26Rv0-ZrKStapDg7T-41ZpIxwTSO4ylecMQ8JHrfs8xddz-dv7R68TrC6yy_4Swt-lT-A-pj-m7uzOWpw5KLtaON0h3lBeLJoc4T3m1ihqQvex5zjTZzZxQXwY2blR5Huq6KUJMNu7seHo2kRpl92I6S-1OOpl5THwJ3dMKT-t_BfBS8d5nZw8Ebu0krQTA0kDv8Vq9Gd60XBqxPutNz8epPHVKdG19EjK4v18hzrXbEVrbeuKP1LSUJImSd5lOiacTjdR9OmHr9TxwvAy-_Jjvi1WQRKGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZpWeGKN5G6pmyJk_YA42BOjJjnY7J6oUpE90j7mb48nqITkRaXPCdxTKdgIYZlV38P-wQYCpmNivkeMMNuveKQSkbFvaAm4zKA6Mb0LT6GRJbDWBnOjh40BKPew9DMw_U_y3R2385_PfgZ4xxxFJtDLyQ5EmtCE4IvaR3qf3lvs2V8-Y_z34QyWl-ZpqRPOzNVUInrOQWIqdf6lBWTPXYMKTWDZVoKT8LTFUKI7tq5l8LpOZis8Lmn0x3V4n8My6CsGMaDmMBhe5Wzd721iM52seWNy4PD9Nx1H231Aye7aHx_oOWHs7EAs175CkVrQ_Vbbkwd4YrD6rNE5TKclDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bgPaGrsy5yi3gJDGjjgBhbYY8xf3YZk-aYqyQR3V2VBS3opsEKLLRk0QuC-9quACx7DUOqFEwHQMj0ySCseqtm6Pon7dl0Y1CEa2fr25Nvt23NmktRPbWpThVujtiL-4GmyMrxu9x-vAudajXufHnpfoVG4rpLuSfw2w85DIA_R7xTq-AcGnLqrpkX5lNOZYdT3gw11feUkHdnVDuPvPLUMLDFxpNCqJ1DVS4vNVrusGthXX4HTMFdQPSUscD_7_UY3BzZ3pm5jV4Zby3MV5iZd4I-d47EYqqiDrKJAT-s2Oj4T-je0oCl1tgIT6vOGWEPybRsCM9KLgkMs9PG7Qeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M7A2PBP6iT0AdPndopgPF6hbYjshN9hsIy1MH9ugTBUIu-ft6Sh_zbSjT60IOA27w_iDGw7v58ATZAHV7ws7FtQwR8T5G3L8nD8c9yUZW40haG3tg8FKH3I0wEoxg6TBiT2X-YSDLYVi7DAm66BPmAWaOWlZnDOPLIDsCUuW3srimGSoPUhRnIHTV1NcHBIa6nQDzdhnZ8sLQfkVogulTIhEM4x_INrTQj1hmX-bgeQEA_e2F-wefMuIzSbNwqnsnNaZ3zrQm92jE1IeFj4PMOOdZMPqDSOj0FwlX_BGFrmhDJIy_kdsuYMiTuf8_4eg1RvNvV8PXkrlX4ORHctv7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات امروز صبح اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/126710" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ارتش اسرائیل: هشدار فوری به ساکنان روستای انصاریه در جنوب لبنان برای تخلیه و رفتن به شمال رودخانه زهرانی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/126709" target="_blank">📅 10:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی گزارش داد که ایران دست‌کم ۴ موشک بالستیک و چند پهپاد به سمت پایگاه‌های آمریکا در منطقه شلیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/126708" target="_blank">📅 10:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e7c0550f.mp4?token=oAVFUSBMyGN-eNO9f__tjhAaGwiMdaHREApF5H6gQrKSjCJvEbXzOf5JvSoEodlpLj6kNTl6bNwAAYetfqU7n7G7TszrJuUqihAsjZPFG3eTobfHJBVx8fxQqY2BpOD3yFg1OjG-D6TggeAUzDhRxDyelayXK3YZuumO6RkFeVi5ON12150trQ8q76y7Hkbgyc-8dY5YBx_B4B-_3VmiWNeyhrEpyZoV7BArfIWbzbeDbKoTVAABctG3eI6DLW108NmZjfYyVb-kP3WN0FcNEI-r1JIAHKHnd7o8dee128fhLW06IIUjbcqIcsPWeP9VeE0xKAn98P2gv2Apo6d7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e7c0550f.mp4?token=oAVFUSBMyGN-eNO9f__tjhAaGwiMdaHREApF5H6gQrKSjCJvEbXzOf5JvSoEodlpLj6kNTl6bNwAAYetfqU7n7G7TszrJuUqihAsjZPFG3eTobfHJBVx8fxQqY2BpOD3yFg1OjG-D6TggeAUzDhRxDyelayXK3YZuumO6RkFeVi5ON12150trQ8q76y7Hkbgyc-8dY5YBx_B4B-_3VmiWNeyhrEpyZoV7BArfIWbzbeDbKoTVAABctG3eI6DLW108NmZjfYyVb-kP3WN0FcNEI-r1JIAHKHnd7o8dee128fhLW06IIUjbcqIcsPWeP9VeE0xKAn98P2gv2Apo6d7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله  آمریکا به مخازن آب آشامیدنی بخش بمانی شهرستان سیریک هرمزگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/126707" target="_blank">📅 10:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک مقام آمریکایی در گفت‌و‌گو با شبکه سی ان ان مدعی شد: حملات آمریکا با هدف ارسال یک پیام هشدار به ایران انجام شده است. معتقدیم حملات آمریکا روند مذاکرات برای پایان دادن به جنگ با ایران را مختل نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/126706" target="_blank">📅 10:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا:یک کشتی تجاری گزارش داده که در جنوب غربی بندر بلحاف یمن، یک قایق کوچک حامل ۶ فرد مسلح به آن نزدیک شده است.
🔴
به گفته این سازمان، بین قایق مسلح و تیم حفاظت مسلح کشتی تبادل تیراندازی رخ داده و در نهایت قایق از محل دور شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126705" target="_blank">📅 09:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از پلیس آفریقای جنوبی گزارش داد که در تیراندازی در ژوهانسبورگ، دست کم ۱۲ نفر کشته و ۹ نفر زخمی شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/126704" target="_blank">📅 09:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ade34d5585.mp4?token=AZn8Zh7Tsme5nbD1tKVxSqopGZyNH_D97iWCjMpg0DlFXwuzl2ds2oK6CAwTEKDlU-93rBwjSbcPu7s8L40yk_6HK47RRtttFGkcrgB7WU2RCXWzcwVZ8EmUmLSNb_nlKAP0rphWnjvw-Dpbc2j--_ZKcBzE70O1tO8EOdejUTAgMsumcSqZdL3vAyYn7eLyInPEYqAR3R_3wDEttYkw7MWYEPYYQqVgUQWH5pfKu0OaaRTY7O8rwJAiPbTFZt68wg6Ne7YUKNn8tAIlcD3xFB3OsOc-z8t5GjNOHiNoKoqZm45qBet5gQfaSYdMCHqX8lqrjwzOfXmnPWBirk2wHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ade34d5585.mp4?token=AZn8Zh7Tsme5nbD1tKVxSqopGZyNH_D97iWCjMpg0DlFXwuzl2ds2oK6CAwTEKDlU-93rBwjSbcPu7s8L40yk_6HK47RRtttFGkcrgB7WU2RCXWzcwVZ8EmUmLSNb_nlKAP0rphWnjvw-Dpbc2j--_ZKcBzE70O1tO8EOdejUTAgMsumcSqZdL3vAyYn7eLyInPEYqAR3R_3wDEttYkw7MWYEPYYQqVgUQWH5pfKu0OaaRTY7O8rwJAiPbTFZt68wg6Ne7YUKNn8tAIlcD3xFB3OsOc-z8t5GjNOHiNoKoqZm45qBet5gQfaSYdMCHqX8lqrjwzOfXmnPWBirk2wHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی عجیبی از یک انفجار اتمی در بندرعباس که ساعتی قبل در پخش زنده شبکه خبر منتشر شد!
🔴
در حالی که خبر درباره سازمان توسعه تجارت ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/126703" target="_blank">📅 09:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7YX7ThFoqaDoX1fjNseEUBvog4K68kvBudnUywaLA0y1-bcw_pLk5u06wG41yJ2q8wOYADO_ig3N-VMLylBuTh9ZkQZswTee90twf1PuhYeW1qL9_YmqGuLr0Hu52n7QMZE609NS7paJp8bGFAAxRG-cKTkHsGC_vKwr4uoDOHQnGS7RA0SkAV8HBqGvfa9XtZo7G3QMCWD6VSczLJPMHlBQzk5WLIvGZdpYUj5hRLYrRipMmdc2ERdGsNIJm6mX16V7u32l3mRLJttElbCCuZ-XF3Wmkt6k_xae1BwETS15fXiHJN512oAcW8Gs3U9Q9YeY_ZZ13JXK_elBFMW-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پالایشگاه نفت سامارا روسیه پس از اصابت پهپاد‌های اوکراینی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/126702" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
شاخص کل بورس در این دقایق با عبور از  ۴ میلیون و ۶۰۰ هزار واحد رکورد تاریخی جدیدی را ثبت کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126701" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126700">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شبکه عبری کان: عربستان سعودی نزد ایالات متحده به رفتار «اسرائیل» در لبنان اعتراض کرده است
🔴
عربستان سعودی گمان می‌کند که نتانیاهو، تلاش می‌کند از طریق جبههٔ لبنان بر تحولات و اوضاع منطقه تأثیر بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126700" target="_blank">📅 09:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126699">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMCLzDU78uPWaxyfW86JVPkGcMaQ_24H8CsdLiAZx2Ft1lIhaGqvy-bNJXrkcmAQ96-aJXx8ldIwXtD96MubS1YsS1OJsvrzNLheweJ1aW8BJ9WEXO4X3TL3hEBXH38I5qjUzCz-Jt23rvAlhtEymuZFue3fd9UVXUCCBcaklgdmmYr14AhIls8LQCPhBN_we_Gfw5v7403btdASJmph9UOiaCF_fvGfH8xwaSVdCKJKvyh38YT0FQ38Kr2DS_vhR_rRj83IqvTrM68ocX8m1g_E4ioOKseNusC1MJHAi6D0Ek5c8dKdUMOfp-RVSORrYdBQ_bgKdROXp1vZdZloew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که فاکس نیوز از آخرین آرایش سنگین‌ ناوگان‌ دریایی آمریکا در منطقه برای "محاصره دریایی ایران" منتشر کرده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/126699" target="_blank">📅 09:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126698">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی نوشت: ترامپ تمایلی به حمله به ایران نداشت، اما پس از توصیه وزیر دفاع و رئیس ستاد مشرک، نظرش را تغییر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126698" target="_blank">📅 09:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126697">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی ۳.۲ ریشتر دریای خزر حوالی شهرستان آستارا در استان گیلان را لرزاند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126697" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126696">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وزیر علوم: سهمیه جنگ ۴۰روزه در کنکور ۱۴۰۵ قطعی شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126696" target="_blank">📅 09:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126695">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گفتگوی تلفنی عراقچی با وزرای امور خارجه ترکیه و عربستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126695" target="_blank">📅 08:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126694">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
طالبان افغانستان: در پی حملات هوایی ارتش پاکستان به سه ولایت افغانستان، دست‌کم ۱۳ نفر کشته و ۱۴ نفر زخمی شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126694" target="_blank">📅 08:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126693">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEtc40SLGiBla0mOMod9pfccmvVYRQ-nFB_xTKHCFncxy-3MzCNv0MiMHh2BKi0LROqiuy4udC7Qn5Sop7G3iQL4V7kfMhjeudAo9eiWA6UVdCXDIXXhG7a1meXzXJm-xuVHEWdfZw-R2UuADi7ViV9wuBbCnW-ue0E0dQx47GzvuZ5BFTfF4g5hH-4KTPe8RA3WW42zHnSfp6l8_COPKEnawQ19AVWVWVm1eG__w1wXnC1pkOFuPgeazSZEOQHgYItgB9RTablOBUXmIMSYJim6CT8WZDAvdrEZE8ZrN8GRvlqC3tWNe8CdcdMjTLNjMv1I4K6ucUYGYgSs2ib15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منجیل که تابستون پارسال داشت کامل خشک میشد به لطف بارشهای فوق‌العاده تو سرشاخه‌های رود قزل اوزن کاملاً پُر شده و الان ۱۰۴۰ میلیون مترمکعب ذخیره آب داره، ۱۰۲٪ بیشتر از پارسال این موقع!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126693" target="_blank">📅 08:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126692">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b1ee28a.mp4?token=oHn1hpBK8bKkFtPs43V1i84jfhlCmPJGalSn3phzgAHAgfk8kj7iWvdX-k8e9etx3XYL7esaqv_4-oGcj2sczI14n6MxHsJTxhKaDVRKUYYtJV8Ha_pTw83QjGW3chraJwz7ePY2TI3BcVnfak7s3rJJNhUTo0onmykC9tVqqLGn4we4VEAff5zjYmSz_yMzpxzQB1F1N3URiF5OTD_rHSGhkP2KsOK2KsAhKAgT_JjAnwIWTX2i0cAn2xfU3SaZwkSr-lHACc6MgzhAF6-5vx6g9XM78wGLRf4Xr9yc72-7b-Qq2DH4f6CnCta43BjcV5gRNtgJd83NM9D7GPYulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b1ee28a.mp4?token=oHn1hpBK8bKkFtPs43V1i84jfhlCmPJGalSn3phzgAHAgfk8kj7iWvdX-k8e9etx3XYL7esaqv_4-oGcj2sczI14n6MxHsJTxhKaDVRKUYYtJV8Ha_pTw83QjGW3chraJwz7ePY2TI3BcVnfak7s3rJJNhUTo0onmykC9tVqqLGn4we4VEAff5zjYmSz_yMzpxzQB1F1N3URiF5OTD_rHSGhkP2KsOK2KsAhKAgT_JjAnwIWTX2i0cAn2xfU3SaZwkSr-lHACc6MgzhAF6-5vx6g9XM78wGLRf4Xr9yc72-7b-Qq2DH4f6CnCta43BjcV5gRNtgJd83NM9D7GPYulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت موشک‌های ایرانی به مقر ناوگان پنجم نیروی‌دریایی آمریکا در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126692" target="_blank">📅 08:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126691">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vI3ME9siwK8N9rPB9VxcoqmT7nNeYpBsLD0akRtMVeRifFKWYTX8at6MZb8O5xOlI9NffqhAixWW3O_TJZZM24Ef7YDEyRLPwJQrQxsxjYPPUdtVPCYX_dOZQKmuy4S0cpy0jXrOd2t51BD15H9tWMQxhVu0DXBzVbFap6RozQTFfOE5ooHzGSXRw70_IGAQ2LTfwpEOkOPcCelmGlMUifViwAFN6K7ei7OPbck8YS8nX739lGo6ARClEMau63VT6UaQD8FBTvd3v3B7e6scuEmU-g8CxvEurNOu1I2fPBi4qwXIaZs7GTwfTdbweTLWOvTo8Fs1TjI191qpoDq9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه جدید وزارت خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126691" target="_blank">📅 08:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126690">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
مهر: منابع خبری از شنیده شدن صدای چند انفجار در شمال عراق خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126690" target="_blank">📅 08:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126689">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک مقام آمریکایی: ۲۰ نقطه در داخل ایران هدف حمله قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126689" target="_blank">📅 08:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126688">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیروهای مسلح اردن: پنج فروند موشک ایرانی که به سوی پایگاه الازرق شلیک شده بودند را رهگیری و سرنگون کردیم. در پی سقوط بقایای موشک‌های رهگیری‌شده، هیچ‌گونه خسارت یا جراحتی ثبت نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126688" target="_blank">📅 08:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126687">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
تصاویر شلیک موشکهای سوخت جامد و مایع دوربرد قدر و عماد و خیبر شکن به سمت اهداف امریکایی در منطقه در پاسخ به تعرض بامداد امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126687" target="_blank">📅 08:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126686">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پاکستان: عمیقاً نگران وضعیت جاری منطقه و درگیری‌ مجدد هستیم؛ دیپلماسی تنها راهکار مسالمت‌آمیز حل مساله هسته‌ای ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126686" target="_blank">📅 08:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126685">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ارتش اسرائیل: به هدف قرار دادن زیرساخت‌های حزب‌الله در جنوب لبنان ادامه می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126685" target="_blank">📅 08:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126684">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9fb4f38b.mp4?token=avCgK-5sC8oUTTvPz8EJ6X5IaoT2KcxEwlcWKJHdxat4qv2vUTzdy8Z4OMZKMeFkD3m4cY8XuXwRIEys6On3Fy9EfzNOAkgtx9jmx_chXngTZmSlfqOOB7gm6Ehe3Fv-fo3PsF2DK-6kccww4MWeMBHjiKtCHveiDCqXzRbIx6udQYp3oPoP1C-EIDl4mmyTu_fR1AsggGwbOzyBFgH6VY9Fsourwl9NffA5W3NCw93jfrSgM2p3RnLilvZZgjV7RNZwEVRP7Qqp5FIPFF5FR57cGl-eI8J1MmFmkNPOrZHwN9bBz-5_woXPVOFq_yis8ucuI0N03vEzknPp_jVAwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9fb4f38b.mp4?token=avCgK-5sC8oUTTvPz8EJ6X5IaoT2KcxEwlcWKJHdxat4qv2vUTzdy8Z4OMZKMeFkD3m4cY8XuXwRIEys6On3Fy9EfzNOAkgtx9jmx_chXngTZmSlfqOOB7gm6Ehe3Fv-fo3PsF2DK-6kccww4MWeMBHjiKtCHveiDCqXzRbIx6udQYp3oPoP1C-EIDl4mmyTu_fR1AsggGwbOzyBFgH6VY9Fsourwl9NffA5W3NCw93jfrSgM2p3RnLilvZZgjV7RNZwEVRP7Qqp5FIPFF5FR57cGl-eI8J1MmFmkNPOrZHwN9bBz-5_woXPVOFq_yis8ucuI0N03vEzknPp_jVAwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از حملات آمریکا به ایران، یه تیکه از سریال «وست وینگ» رو تو تروث سوشال خودش پست کرد؛
که تو اون سکانس رئیس‌جمهور بارتلت میگه؛ اگه یه آمریکایی کشته بشه، ما جوابش رو در حد همون حمله نمی‌دیم؛ با یه فاجعه تمام عیار برمی‌گردیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/126684" target="_blank">📅 07:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhYk4PQqtD5xFirkU10GTBrSJemPfbw1GN4D-RyOMgOZH3FW0ERmKIvHLovswzoAQmRwVs84ule3WY19PeulA5sGKYnEK9J4JU2ySEIe_mflC4Yf-cFtiN5lNwhlRP5_M8d0IJbi9-Lpm03nZEwUmWZjueRQFpYg7sWqNPUsdt8sSRJZZNkATl8azre5jmpmHT-d_Xt9CbvuJIVKE3SIBhOwM1p561N-nIz56esKNn-4H--gJ8U7wIxkHPqf-ALaPRcYfKWzRTppr3E1TMaVNl8nWL02tuGDe9Hef76RWKlfLVtYGffWRNf17uaa838yDJPRN_t8TjjJsewpmwA33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLzWnK0nw6ViN_Sm-fSfj2OoYf95E6nuP1cfHjMJEte-aN8H82E8_Q-PMkpsIvP_hL7XLX4h_h4d_0RlaBahCMTLpECSDMPzl1psc6z2tamFsNZgAPpJahb1f8h9WAvmzONxvCqR0ykftMoZD9LOzFYFiSM3Tozn3YdlvMoKGslBWeqRVIe-wSgDxqvB8uy-UMutLvF7uosODaDUFsPr0vnBvF5SFgeEI1pG129aE0soR3h0Enw-mFcgPFyAueNfnXwAhWtBAxpLYLw34L4bd1C5ofRd2Jlza4_yIUEvc0YMX72PsYAaNp88jcx5P4UwPBCcVcWwcpE1v1jsj3sDDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکس‌هایی از فعالیت پدافند هوایی بر فراز بحرین در حملات ایران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/126682" target="_blank">📅 07:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/38746437b0.mp4?token=NyU1CitJjy0feVpmJjXUhMJ31CLCCznZ81f7Kvpawf0-TZA8ptXQjxZnlVv-zKH2VsImdzeNgdS9C3QAtFI5JMM8pG81JzmI1J5Yy0J7W6fnjeHLNaLRFcE8wHLeST--34XDMRLQ9cZUzm0JKPmq10hIn6-ZFRTCNQUD5dX-YWmG3xGSDCgrJaNrlIc7cvb4m8FKZL09oC3JBBhP8sA9KiAuEKquPA4nO-Zgs4Qf4ZZSstqpL66ZKzANh0EBE1YUWN4HKcoMiVSgpb1lXGcBsZHJoR44aWwO6OmpJ4Mxy7o5juzutBTR8vl6R3mHhQVFGrP1QbCollPqjhMOMc3Odg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/38746437b0.mp4?token=NyU1CitJjy0feVpmJjXUhMJ31CLCCznZ81f7Kvpawf0-TZA8ptXQjxZnlVv-zKH2VsImdzeNgdS9C3QAtFI5JMM8pG81JzmI1J5Yy0J7W6fnjeHLNaLRFcE8wHLeST--34XDMRLQ9cZUzm0JKPmq10hIn6-ZFRTCNQUD5dX-YWmG3xGSDCgrJaNrlIc7cvb4m8FKZL09oC3JBBhP8sA9KiAuEKquPA4nO-Zgs4Qf4ZZSstqpL66ZKzANh0EBE1YUWN4HKcoMiVSgpb1lXGcBsZHJoR44aWwO6OmpJ4Mxy7o5juzutBTR8vl6R3mHhQVFGrP1QbCollPqjhMOMc3Odg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه اصابت موشک ایرانی به پایگاه ناوگان پنجم نیروی دریایی آمریکا در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/126681" target="_blank">📅 07:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFhnQg_0BgITk5zldh5CoOEFci3TGrQIhXqLGFDS3p4tGltPc2-ktl64XaYSObCGpji0W8xnSLpHMdWLqd1mTtJkKYzJI5YCRxSDXbtIL-Hypgf4AX0Gq55ave0jJbiUi4Hnq8Gw5Gfcxo_QOzLVHPYdDa2s8YHeCPFwN6mNucpJzpJSfbYqlQsfdCo87pZVMYSIyt5J3pzojKyfmKVyosghlIdmdUuccHdo_gng3OGaO3QXKC51ynHdC-6prZ_0MNrQ9u9e-4_bhw6IA-IOw3T9lqe3yIS7c3kVW8DJiQsyh25C5QOR3q0YdtF5fI9KhNf7EbSHMEwqkLbuP4d87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به نیویورک تایمز
: ایران اوایل چهارشنبه چندین موشک و پهپاد به پایگاه‌های آمریکایی در سراسر خاورمیانه شلیک کرد و تقریباً همه طبق ارزیابی‌های اولیه آمریکا رهگیری شدند.
هیچ تلفات آمریکایی گزارش نشده است.
هیچ خسارتی به پایگاه‌های آمریکا از حملات ایرانی تأیید نشده است.​​​​​​​​​​​​​​​​
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/126680" target="_blank">📅 07:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صدای انفجار در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126679" target="_blank">📅 07:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hx6pZTGan9hSD0zaLZe637kkoULY7mmxe-20ON5B1EZyzZBzj0A_sfcmDdcetDhaYmTktlgYx6REr4vG_fHkXG2GVsL88PSF1iSrUjzrR932oCOQBHVX1yM6v1Yxb8QZaSKja2aE1SM1dWHjvVnywcscsTNoS4rnOMy09ycgfNKzXgrLIRyuDT84dHp0HWx2MhLOIjyNvCaowaOVdD2u68TVpOpyaWRu8Qj_5312688EolU3roYCVWuSBnt__DgZg3HQwQeGslr2S3Zoob_sxYvQVkscJIFBNwaQ0yJO8ICMYMkMI5-VLMVu0zzI9_WtpVEaitkvjYSSTmwducxLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نامحدود فقط 90 تومن
😍
فقط ۵۰ نفر اول
❤️
✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 90 تومن
🏷️
✅
این آفر فقط برای ۵۰ نفر اوله رفقا
✅
💥
بدون محدودیت حجم
⬇️
⬇️
⬇️
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/alonews/126678" target="_blank">📅 02:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7bc9515c9.mp4?token=G30Dp3OpH73E_V3UechCfylmm8MYk7Oxne-2V18e8xcuvOgVofGGHdSDKGKYOCzSmPD9X4SVTAhDsC4wFiurx0XjiVxSB7Xt2MsHdGdde4wiRdIx9dbrzTgnDe4-XSJV7wfT0fc86eTCE1n_n3j97VbKad6zzBmBI85LB6k0OxwoC-51YokpHGg695WvykW_cAOB6xa8tLyVuXs7km9LbJrJGCVRPYXNPYssZiIIBF03Wzf07Z2LvdUMK9FolF2OXzzXTMLresyOhBDNvS-Z2L-moZi4ycezonlPZiTXlWNydL1URj5q-o-B_xZ6xRjGnuWlilU8_f3gu-NWnbi-zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7bc9515c9.mp4?token=G30Dp3OpH73E_V3UechCfylmm8MYk7Oxne-2V18e8xcuvOgVofGGHdSDKGKYOCzSmPD9X4SVTAhDsC4wFiurx0XjiVxSB7Xt2MsHdGdde4wiRdIx9dbrzTgnDe4-XSJV7wfT0fc86eTCE1n_n3j97VbKad6zzBmBI85LB6k0OxwoC-51YokpHGg695WvykW_cAOB6xa8tLyVuXs7km9LbJrJGCVRPYXNPYssZiIIBF03Wzf07Z2LvdUMK9FolF2OXzzXTMLresyOhBDNvS-Z2L-moZi4ycezonlPZiTXlWNydL1URj5q-o-B_xZ6xRjGnuWlilU8_f3gu-NWnbi-zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حملات اوکراین به روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/126677" target="_blank">📅 02:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دو مخزن آب در بخش بمانی شهرستان سیریک در جنوب ایران هدف حملات هوایی آمریکا قرار گرفتند و طبق گزارش صدا و سیما، آب آشامیدنی در این بخش اکنون قطع شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/126676" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eakYz2LhuV78jvPgJ7q5xKc2Y4WcjfL29HeL7ZNx0vEGbltCK2EJdSfP9vW2edx7zknSuOgEFV8BPQbW4ihui6d5VtbPgNeJ2WJFFidIo3skheBFk-cw3SrtRjeu238lLMcNUcwKXjHnVqXZO5FAJQeroaP-Bt5JiN9oRj1Bw6kKWMs3ajssRIntC8XeWdoRDl-vC_tS8DdRAMTITJVw7YaENNVGGA6koZJ9gpGpYc_dDBJ1QEmgGQbrFv4HhW9g00O1hxgLHs7rfnsdpp1FpbVSbr8za_C64IwLZUWckDKD5VHKxCaVfpt_FwxEDP3x7swZXtmzFTS7Q2RyZHiw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/126675" target="_blank">📅 02:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_BJ95VtkqP_vGUR4FxVSnIKAqBq_slZbZdXK992NNldHmAp5l9a3et5RhSwyBGdweLH36oVf__dODMQuJk7q1bCtE3cKG-Sm17Op4r3zDW6lSWJcbZ5u0OQrtnIF3y3yLdPTSL7q3IdDpt3KanrrsCICsXTMzmzmwI3MULltGS4FOIFvoUJTAIP3wSPItQyWECWrHTUpmOmCRiqM35rqLUOeYR0hKGJw5gyjKWthnfVtOJTLy0E_RWM2IuITALmfOt3PoH48zgoInw1Qv7Gq3p72SWgkHO0cgBSkxzBhOAy2tKckRXpKi1jg2Ynk33f-Jyz6uPwUEzfKdgT1d0jwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی : با اینکه توی میدان جنگ شکست خورد، آمریکا باز هم تصمیم گرفت اراده‌مون رو امتحان کنه
- نیروهای قدرتمند مسلح ما هم هر حمله یا تهدیدی رو بی‌جواب نمی‌ذارن
- اگه می‌خواید سالم بمونید، از منطقه‌مون برید
- تاریخ خلیج فارس پره از سرنوشت‌های تلخِ خارجی‌هایی که چشم طمع داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/126674" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
اسرائیل هیوم: ارزیابی اسرائیل این است که ایران به کشورهای خلیج فارس حمله خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/126673" target="_blank">📅 02:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کاخ سفید: ما معتقدیم توافق با ایران بسیار نزدیک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/alonews/126672" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پولیتیکو به نقل از یک مقام ارشد در کاخ سفید: هیچ تغییری در شرایط بوجود نیامده و آتش بس کماکان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/alonews/126671" target="_blank">📅 01:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری/ گزارشات از حملات توپخانه ای عربستان به یمن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/alonews/126670" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
گویا اسرائیل به سوریه هم حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/alonews/126669" target="_blank">📅 01:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
هم اکنون خاورمیانه:
🔴
حملات آمریکا به ایران
🔴
حملات اسرائیل به لبنان
🔴
حملات پاکستان به افغانستان
🔴
حملات ترکیه به عراق
🔴
حملات ایران به بحرین و کویت و امارات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/alonews/126668" target="_blank">📅 01:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
هم اکنون حملات ترکیه به شمال عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 90.4K · <a href="https://t.me/alonews/126667" target="_blank">📅 01:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69604724c6.mp4?token=SyJTwHOSOGzWUCP0dchGfH-zvSBnwyUlNhEN2QBYqDFMyvEoV0ycpubO4kpIho20rA1QT4LBHAh_nmAJAdslQmJuAb0xkxmrq17u3Elc5zX7hsK9_NVM6rhfLB-422vst819QkwNXH2lQAc4FRYPdWS85q60hVWHzcfqX6u-YvZuceG9IUKOeBPcc5e1KIGfYoOcogc56-Il80HYh7FPQVDzRa1yY6sPNysbChO7eB-aHW8XQj78kOwfmYoodZywOUXvRIVqS3BqJrtczbG5dNZqe7k9dzAu1qGXDgaEaUk-TkxQ48_MN3M8htk8hTRVIadvV8DSNSb0_-dITNC4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69604724c6.mp4?token=SyJTwHOSOGzWUCP0dchGfH-zvSBnwyUlNhEN2QBYqDFMyvEoV0ycpubO4kpIho20rA1QT4LBHAh_nmAJAdslQmJuAb0xkxmrq17u3Elc5zX7hsK9_NVM6rhfLB-422vst819QkwNXH2lQAc4FRYPdWS85q60hVWHzcfqX6u-YvZuceG9IUKOeBPcc5e1KIGfYoOcogc56-Il80HYh7FPQVDzRa1yY6sPNysbChO7eB-aHW8XQj78kOwfmYoodZywOUXvRIVqS3BqJrtczbG5dNZqe7k9dzAu1qGXDgaEaUk-TkxQ48_MN3M8htk8hTRVIadvV8DSNSb0_-dITNC4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیده شدن پهباد شاهد سپاه در آسمان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/126666" target="_blank">📅 01:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/alonews/126665" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رسایی: اینترنت قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/126664" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوووووووووری/گزارش انفجار در بحرین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/alonews/126663" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری/به بیروت هم حمله شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/alonews/126662" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
سید مجید موسوی : ‏و ما النصر الا من عند الله العزیز الحکیم
✅
@AkhbareFouri</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/126661" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
فاکس نیوز: از جمله اهداف حملات آمریکایی‌ها در ایران، سامانه های پدافند هوایی و تاسیسات راداری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/alonews/126660" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
گزارش حمله هوایی پاکستان به چند پاسگاه مرزی افغانستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/126659" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما دلیل این خدمات باکیفیت ماست برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot @tvpnshop_bot</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/alonews/126658" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
فوری/قطر و کویت حریم هوایی خودشون رو بستن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/126657" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری/به بیروت هم حمله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/126656" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/آغاز حملات ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/alonews/126655" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecDS7ZWBiS8EFTzoB9idAjbqhCRgg5Z0N43VylpYPTP8eCcxxLJsaoTfXLt9mzfJIt9nhiBmbvud_AGrwV-QvmhMlzSLch4U-rDJPVU2XKmj8w8WFy00z8GNMoORoOo6R0FNQgtXh30fNcWVFgVKkUkZMCcHOw2rKw94x_V3IIcBquI9YrQnvhELhbQa8hUVupnOozdtRSYrV7RPnqQ4D4PUhYVNnDiObs9XqcpbbkUIWKJvpA6AakcPKaYYQdjmuxKHXNfJwSKFduH7eXZ1vZm-ehaW7zT2OtFNQCkUp3qk-krI-d5hYd45L1NJNpI5QLpvnXZca6_iLtzaY9AKXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور فیلد مارشال محسن رضایی:‏
پاسخ ایران به حملات آمریکا اجتناب‌ناپذیر و احتمالا قریب‌الوقوع است.
🔴
علاوه بر پایگاه‌های آمریکایی در کشورهای حاشیه خلیج فارس، جغرافیای محاصره نیز می‌تواند جزو اهداف باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/alonews/126654" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ3JuJwazGW0lj9mYh03Cr7c9ZT1lL4Qcz1SJKOfobUfHtbp5KVkGnJvJeI4x2wT64Q1TI3o1Ew8OlGw_JEMiA5CATNYuGG0fUyY8e6Jfjlnz0WmFi9FjJHM-gvBBCuJXTsIPeExejIz2asy_ddTop58OB-IwGcZlZlVLe5IopKxSIvr7zFeKaXBQjxQn2JIRnLC6x9jmvCtVP0swRUEzR2AZSPsPgTLiICDgpWElwLJCeZNy8RrpMoM4gjzErxPFWeW_GlYGap2Fy3YIkmOtej3vhfnEzXYSbyN2hYk8M8vKLH861e-bOmqVb8T5feN9bbpvauFozrQhsIMrBHcBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ارزون ترین قیمت ، با کیفیت ترین سرویس
🌐
❤️
فقط گیگی 2t ، نامحدود 290t
💫
🔔
آره درست شنیدی گیگی
🛍
2
🛍
تومن
👀
5 سال اعتبار ، 5 سال همراهی شما
دلیل این خدمات باکیفیت ماست
برای جبران این لطف و محبت
☑️
❤️
👇
تست و تهیه اشتراک
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/126653" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
فهرست اولیه اهداف آمریکا:
🔴
پایگاه دریایی سیریک
🔴
پایگاه دریایی جاسک
🔴
موقعیت پدافند هوایی بندرعباس
🔴
باتری موشکی ساحلی میناب
🔴
باتری موشکی ساحلی قشم
🔴
بندر قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/126652" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
6 انفجار در قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/126651" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هم اکنون ترامپ به ABC درباره حملات ایران: فکر می‌کنم پاسخ دادن بسیار مهم است، آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم
،
🔴
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند،من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/126650" target="_blank">📅 01:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
صداوسیما: حملات موشکی بزودی انجام میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/alonews/126649" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
علی قلهکی خبرنگار امنیتی :
بنظر می‌رسد آمریکا در حال آماده‌سازی افکارِ عمومی برایِ «اقدامِ خاصِ نظامی» است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/alonews/126648" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126647">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
انفجار در میناب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/alonews/126647" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126646">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تاکنون 7 انفجار در سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/126646" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126645">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/126645" target="_blank">📅 00:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💢
فووووووری/هم اکنون تحرکات موشکی شدید سپاه ماسداران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/126644" target="_blank">📅 00:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
حملات ایالات متحده با موشک‌های کروز تاماهاوک انجام شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/126643" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
رسایی: اینترنت رو قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/126642" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwlho6-BXXLoKLEP9AsnciJvR4VznoS9SGKI14UWkuJ1JNUN_9HDOwWUGNmAk3Byv9Wpk2kwtd-xiTPNchrzMsZ4-hHccQI3gW2QT6jbybzk3qTW_Br8Z3Q2L0DtmPkDZLHNT2U18D5vjSIKEbpXWNbattnEq7HnNebv9noIsyXOYvDAgds1L45g5qWNSLcQ36Sj5-Z1Q3c-cmeBoYrEbjo4v8S93KoN8SZzdjsoizJWD3u2Q7mexDeyaYKVEhtjpDJijuXxCyu08SBRTbbYo-yyfZxb0RZ7U0k-711Dmh53gYFrI2VcHzVTBzlkjgGiKCrcE2lKh9G0McPdOkStmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/alonews/126641" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126640">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/126640" target="_blank">📅 00:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
صدای ۴انفجار در محدوده بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.5K · <a href="https://t.me/alonews/126639" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126638">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/ایالات متحده رسما حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/alonews/126638" target="_blank">📅 00:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126637">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/انفجار در جزیره سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/126637" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126636">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از هدف قرار گرفتن پایگاه شهید راهبر در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/126636" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126635">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری/گزارش‌ها از حمله به بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/126635" target="_blank">📅 00:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126634">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVqgPt-aJPhHRjSuHGT7wlbXONsvk0YSwnba2hS_Nb6hrwv4UJGPhPNcSXAtHwPqN63dc-puz_skW42PYgmJxH16hYzGjp6D4yMif99c-ND0oIGF1i-7BjWx1UG3ZK8kWp0vJJokYj1aKSoTkCtcyAQzCno4QDFQy8sUVLPPED4cHlHZwJvdGrjbfBM-PIIQsTQvdECP5kX2yuXVj9EIjnvpjvapbalbpchrgbeJsHPEZeU8E3Jy-HYutkm4IY1vwZ--KrbTBBjHR3PbPTWP-0JPTMj9HJRhWvnx3WvokNkCRI0S1KTxDp8-PsCgZmPoE_3MosxBMnssfFk5urLkWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقارت تمام عیار قبل از جام جهانی
‼️
تیم جمهوری اسلامی فردا در دیداری دوستانه به مصاف تیم زیر 21 ساله‌های شهر تیخوانا مکزیک خواهد رفت
هیچ تیم ملی‌ای حاضر به بازی با تیم جمهوری اسلامی نشده
@AloSport</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/126634" target="_blank">📅 00:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoxcCLKiIQTawI7U_KuwxM1EL1E6_ZbWNVNr9jgIo0MYynCJ7RJIP77AkBN97242c24RrZD6jYL8G6MDwzoT6xDmT0l1kaWWtNqmcjW3gqwL3F0yNbkWvyvYIot1xFy5NZKu-oGqmuGgXYANGmVSHPxEIGUZdvNwPk2OoxA3Jv6XtZiWdxq5enxEIOnwMx1x4_lA--0fxgDyGXlm1UWnQFDSW0JDkWFDCDuIlcdc2M6lzaTlYdTRmQk7ELtT_lLoEaHdCAmEGEG_Nja34RsvqBzzgNtj45de_5H2x4yDVtEKrGpErgG7njadjBUxxB6lArwfEgvku5GMoPrry92I7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب الله به شمال اسرائیل حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/126633" target="_blank">📅 00:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HexiL6AbEYYtrdDnB1RI76G-kZWsyGAsrXBDldDkdSWqtQFn2P2dBn20YC6vJ-vErgeQuuyUSuB_lbUMu8DfQup0eJyvwg62VZFgIaDQp-p-_zeS_flbpDi1cekGG0hnnRxdnfWKhR-6ERpDJl4iA-gp9h1HukisEjMbb2VkEplHddDR3KEVXTdcdL16fQfjZLCzR2o6VEvnhPI0YyZM7l8HOUIyilHkhXaYThun-hEqCeUOEyf9PwEFxXefvj342x-bnRzt5RAyw18uQ7Z-5ENFFMknk88mvhBUFQlf3IchO450EPwJqufJDH66XE3C1Vj4NnaLXaeN_fCWVlYQ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/126632" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💢
فوووووووووری/پرواز شدید جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/126631" target="_blank">📅 00:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
شبکه خبر به نقل از منبع آگاه نظامی: هیچ عملیات نظامی هجومی هوایی در تنگه هرمز در ۲۴ ساعت گذشته انجام نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/126630" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126629">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
مسکو در واکنش به رای شورای امنیت سازمان ملل به بررسی بازگشت تحریم‌ها علیه ایران : ما به شورای امنیت اجازه نخواهیم داد که تحت پوشش کمیته تحریم‌ها، تصمیماتی اتخاذ کند که محدودیت‌هایی را بر کشور‌های عضو اعمال کند
🔴
چین: تلاش برای بازگرداندن تحریم‌ها علیه ایران فاقد مبنای شورای امنیت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/126629" target="_blank">📅 00:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpi6eOZXbV3SoGY6q3tddKKvuvK9PDZoaQ_PIki-5SHS7wgpKnqS8pzsEJ6md37jCtc7bqX9jUL1P9pOpXgI95Rc1e8DIYMfsIIYQ57VUpQQZb8RqJqZQkYSBhPrqLyOWhCIrHTWjgql8iNfNyobmLcwJZsRTUbQsZNPjxGA9mbpK_oNKxQl2WW7xrdExc4y9B_IbTf5wjjiqEgzlYstqB9ool-4ndJtdSnPO_P7yt1V-uyCPGwL9JuahsQSBXiiOKotdNFJDodmNy5RMOMO0NWD7-YIfhRawuowdAVmibfziCLFq9H5-eCmHOCtQG6EWEQiR5TP1nX2-JoYAXk_Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس: به هر اقدام آمریکا پاسخ سریع و قاطع خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/126628" target="_blank">📅 23:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر خارجه انگلیس: خواستار مذاکرات موفق ایران و آمریکا هستیم
🔴
می‌خواهیم شاهد پایان سریع و موفقیت‌آمیز مذاکرات بین ایران و آمریکا باشیم.
🔴
تجارت جهانی از طریق تنگه هرمز باید به سرعت از سر گرفته شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126627" target="_blank">📅 23:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126625">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
جی‌دی ونس: به توافق با ایران نزدیک هستیم؛ شاید هفته آینده، شاید چند ماه دیگر...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/126625" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126624">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ترامپ به واشنگتن پست گفت که محاصره باعث شده ایران «بسیار فقیر» شود و گفت آن را تا زمانی که لازم باشد در جای خود نگه خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/126624" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126623">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دونالد ترامپ در گفتگو با وال‌استریت ژورنال، درباره حادثه سقوط بالگرد آپاچی گفت که "مسئله خیلی مهمی نیست" و افزود که خلبان حالش خوب است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/126623" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126622">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری /شلیک موشک از خاک یمن به سمت اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/126622" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126621">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری/ خبرنگار: شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
🔴
ترامپ: من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/126621" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126620">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ترامپ درباره ایران به ABC: یک نفر باید همه آن زیرساخت‌ها را بسازد، پل‌های جدید، فلان چیز جدید، نیروگاه‌های جدید... آنها از یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/126620" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126619">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ: به زودی پایان جنگ و پیروزی آمریکا بر ایران را اعلام میکنم امسال جام جهانی خوبی خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/126619" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126618">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوری /شلیک موشک از خاک یمن به سمت اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/126618" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126617">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هشدار فرانسه در شورای حکام: جمهوری اسلامی ایران مقدار بسیار زیادی انباشت اورانیوم غنی شده در اختیار دارد و مشخص نیست چیکارش کرده و کجاست، همکاری فوری جمهوری اسلامی با آژانس بین‌المللی انرژی اتمی ضروری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/126617" target="_blank">📅 23:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
روزنامه نیویورک پست گزارش داد که هزینه بالگردهای مدل AH-64 «آپاچی» بیش از ۳۵ میلیون دلار برای هر فروند است و ادعا کرد که این بالگردها در سراسر دریای عمان و تنگه برای اعمال محاصره به عملیات مشغول هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/126616" target="_blank">📅 23:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
گزارش ها از شنیده شدن صدای 3 انفجار در نجف عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/126615" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126614">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
معاون وزیر خارجه ایران به الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
🔴
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
🔴
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/126614" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126613">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ به ABC : حمله اخیر اسرائیل به ایران لازم نبود، ولی انگیزه‌های اسرائیل رو می‌فهمم
🔴
به نتانیاهو گفتم کاری نکنه که به مذاکرات با ایران ضربه بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/126613" target="_blank">📅 23:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126612">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XByIAMyTquELZaHV3mtRAqst4AvIjIswb303NgLz1s9H-QxsXR4bPcjFdlHI47cQyZpstfsjHUXHMwrTwli5cLqCamhNrah0zEpv8rRS0H7hbKvqjDdviEtXDWbRXwRb5LdiaBNQ2YggEqkJOUCV0MaCxRq9psgrcOnu7xouwSbbia-1CJ6YBqnbbtwL0vLOGceTuxFC7x_KNzJhjRZD-Cw3mKhprW7zejVqkJyZ2FDPfWthTKWjab4avW-2cbCd4gNIX34_Ngy7oEUpsUOhgzSyMvE97nXO9isBYTLgJ1aiZ4kQ4l-TGzUR_93jy7gGinm04sDQM56WVYU0D_WDbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: تردد کشتی‌ها در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/126612" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126611">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8De1FvncBvqU77SS18uq5q545EkNzv_Qu-fgjrtngMd-f6XLPOwesipRnkEpuez1fi3TwveKr7-H2Wka2yJ8-jb58jVFVopAnS3IZnkFyoFGWJHniU6Xy2y6fFun65zueyKaVJN6WDK6AfwIGMXuR2V2oLcGOyulG0B8IYEpyGofKSYc8kQu5FzajZZlSkAb5IjJJno9mZdwmo5sTgbobUIK1DAINcZMNdm9hwLePMph2a7jHXMkNDWe8xf6YnU7pWH7ix6yJAgwwfq0sPeQp4v9SXjPGWIXchpoVvkzK46nku9lEDykHfD0hb4ODX392ocjZmfPDR9XLq1m8yeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های کشتیرانی: صادرات سوخت جت عربستان سعودی به اروپا از سطح پیش از بسته شدن تنگه هرمز فراتر رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/126611" target="_blank">📅 23:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6J1vdJE56NeTnn3IO5CPj6vkD9Bojph7RdB4sviII7cGF9NsrGgR5XC5W9URHMt1ddjYWgdwh_wCFipGgumavhcWU_VAuvvs0-CLgI11st7QUcPHeb2efCUbEq5ZzM6dw663-ukAbxHpRlOcKFCSa3D9tcZ2FT5ZASZA2cYHdFt5ntfEvPk508OEeXV6Uo19iZz-W5Vacq1li0Ygf452OT3ffU3mflwNeH20HZaMVhFY0iqJe1Rfe7S05TOcS7GfbnypGbrAT4lI4YjTqqASbLsmrYAKx1F7nh5Y8W9potyQ2gGtzUA8wNCQIylDXeYH-3e0uMXxbFpikP-PA_r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی آمریکا هم‌اکنون هفت فروند هواپیمای سوخت‌رسان را در منطقه خاورمیانه به پرواز درآورده است.
🔴
از این تعداد، شش فروند در مجاورت خلیج فارس در حال انجام عملیات پروازی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/126610" target="_blank">📅 23:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126609">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
طبق گزارش ها تهران در حال حاضر شاهد اختلالات گسترده در GPS و خطای سیگنال‌های ناوبری (Spoofing) است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/126609" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
