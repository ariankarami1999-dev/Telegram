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
<img src="https://cdn4.telesco.pe/file/AvrEjUeEN7UKx-Z8EXsbu19WRRQNzjKnDdbOFgqU2wW8lZr0xK40GN5WpoNyivhGzCf2mOEKD3wS-6aryX9L1x12rvLUT27xTsv2U_xxeaUSpzD5u0ZFEMxcAvpeRgcdP4uo76HwVd8NaO4LmlIeIbq9QP6rS_O_oUE2pQyWwTOpVcgwtm2qn_WFdLNBJbq0GzDk9iNK-MwORn2NxYuT0QvgQZ9k2eg5UQxaB8cD_7nxdkoGiPMRNKdGyzy9GMIQG0xUNlX1sxDjmW6MoOqMy6IXuyJyT0NrYzpE2ITHok2a9apZAzUePf6tOIuFvV43IbAbpzIbg1ZYa4TcWIZk1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 911K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-09 16:36:06</div>
<hr>

<div class="tg-post" id="msg-123712">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpg6DmNnscLTbo1OyABaJiBwuvBtmo796AQfvl74b8UmuStmcqW9C9at3Kam7WsvtAjkaouRl5LcZm9poLaLFHmkWnZO507VkbeP7_rhQnVkZ9BFX_IichcLyyK9rN4B9xxstRgQX0LbV8YZxnhdLe5kAVf8xTjhE6dezeiL09mpp4yoenm39fHt5MMAxvwG2lBL2Dcn0eVpGG-gt7jfSRTs72hmqPpbZ2uFtO_m3Q47L3E6nyQgWKUkSxjbh43rAH3m9y57xDImALxicLDZSqL169fmaRX_O4LJDjOz8G8B6-7C3u6MvJN9TgASKbBNw-e39RTZ1BGzevDqaimqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین از جمع ۱۰ دارایی برتر جهان حذف شد
🔴
تشدید ضررهای بیت‌کوین، این رمزارز را از جمع ۱۰ دارایی برتر جهان از نظر ارزش بازار خارج کرد و آن در جایگاه سیزدهم قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6 · <a href="https://t.me/alonews/123712" target="_blank">📅 16:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123711">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdzSN_NsNrXxBLAvZp30XMNskrSL8yNM366omOAhSYgPATvlJOf-OW342Y_Epxz6RdjI6H1y3ZJali6oUtU0XcyxLZhdeVfh5oFzTsiEkCqwY-3foKhguGX_jqwRfaj8zfSuFTprpB310k3NE67v3RjmZP9SsyHl9KIin5wB3GzQ5hzrvDGEPyggqdwf7-Xq_kRLkpxZu1No3Od8PoM5kIpSfRBCAfPVyCOOnSOGFOi6Be_UqYBDfgG9Vuh9vi_4WKK5283h8PmUTA_uehjzLpjRE5AwUP1f6a4PLriTPGt56n-hPrO2OVO37gBtKA1J8Jun-PDw-uOfltHC88h5Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تونل امیرکبیر امشب مسدود می‌شود
🔴
شرکت کنترل ترافیک تهران اعلام کرد به منظور انجام عملیات تعمیر، نگهداری و کالیبراسیون تجهیزات، هر دو دهانه تونل امیرکبیر بامداد یکشنبه به مدت ۵ ساعت مسدود خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/alonews/123711" target="_blank">📅 16:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123710">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOUGyIuKiQrEVjVlIdBOW3jfSMeB5vJiU9YsUmJh0vIMCV3rD9-tLnLrSLKjEU_Kq0BzNIbKJFKJCH7O-ZVK30SqlND7HaH5OvZ8PvpNkri94XdJB5ATzyXirKiwz9VDx1yALjG5S85kBFjog-taSP5wD2K3k4tX3vhBO3LapL5AgE_cgqpK0bzE4Ng3tMXuGLyWeKXZGoP2o6my-6By5IA15pREgVsLLJ5vzYEul2XGzxtnOK53pjeTMaURWYri4Lrh8IQJ2aLvP80gc60KNkmVVjgPsRjUeQmAzjrEspVJpRNoYvClD6KwagsbMTIwiY5b773haD8x8YJf8GEYww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت گردشگری:
تا هفته آینده "کارت‌های سفر" در اختیار مردم قرار میگیره که میتونن باهاش برن سفر عشق و حال و هزینش رو قسطی پرداخت کنن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/alonews/123710" target="_blank">📅 16:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123709">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31db1aaf3a.mp4?token=PWm9oBixLyctO4CTbq-HTopKU4PrvDU3V6zVIn-EKQvI9cvYizi3JjJtOMuVvz0Mgj2c0Ys0JujKT5IzDINDe9hhY4wtwOS9YULKIdzdmuImfO43Ft7yRbChzfzsSLs9u05miozdwlXLTR6d5PeBUf1kZA_bF-tQ7T659HAmfrn_-lhmn4hypI7_y1HhC-3n9VeINbD4BMGKUzIJmyzK9x6bQhXfis3cBSmbSlVCEeSzm7w4GhVHsQ8iP6SnmH82R1G8OnSZwNL7nt_MLFhKTPhVW910TWCnkO6u6m15y2E4Yu3hGFwAfKySoMckoJyKz5VQ_6xc7bngZRBxtio0ao6oj58oQG1CYs3Iv_PDyL6O_s4SfytdeQdyOZTx05mJBvL7Vx8VzLDLDA3QNX_pS_G-nOM8p1Jx5gADodGVSJILTVeRuaqvmKlFz2rwXHaSXqUJKEbmXfUYhsOZAqIdftQtfaadCumPu0TcqMuSAlZW4fDExvORdVidERJ-3UMuagDZAL1JAkhbbrBZBnCU7PiK0lovO353bwhPEa_qaYNi6rtwuqGzvkLg7HM1_Iy-mIE_3XClIDnn96T84F6u3kGV8KlR7wMxHQzjwfV5qlRYnVipYHxpjTmwFYwSsr2Ret3ytwcuSxJL1OW8976QNPM4P76SrvDytlwBMvfoYc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31db1aaf3a.mp4?token=PWm9oBixLyctO4CTbq-HTopKU4PrvDU3V6zVIn-EKQvI9cvYizi3JjJtOMuVvz0Mgj2c0Ys0JujKT5IzDINDe9hhY4wtwOS9YULKIdzdmuImfO43Ft7yRbChzfzsSLs9u05miozdwlXLTR6d5PeBUf1kZA_bF-tQ7T659HAmfrn_-lhmn4hypI7_y1HhC-3n9VeINbD4BMGKUzIJmyzK9x6bQhXfis3cBSmbSlVCEeSzm7w4GhVHsQ8iP6SnmH82R1G8OnSZwNL7nt_MLFhKTPhVW910TWCnkO6u6m15y2E4Yu3hGFwAfKySoMckoJyKz5VQ_6xc7bngZRBxtio0ao6oj58oQG1CYs3Iv_PDyL6O_s4SfytdeQdyOZTx05mJBvL7Vx8VzLDLDA3QNX_pS_G-nOM8p1Jx5gADodGVSJILTVeRuaqvmKlFz2rwXHaSXqUJKEbmXfUYhsOZAqIdftQtfaadCumPu0TcqMuSAlZW4fDExvORdVidERJ-3UMuagDZAL1JAkhbbrBZBnCU7PiK0lovO353bwhPEa_qaYNi6rtwuqGzvkLg7HM1_Iy-mIE_3XClIDnn96T84F6u3kGV8KlR7wMxHQzjwfV5qlRYnVipYHxpjTmwFYwSsr2Ret3ytwcuSxJL1OW8976QNPM4P76SrvDytlwBMvfoYc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : اون محاصره که کاملاً محکم و بدون نفوذ بوده و واقعاً فشار زیادی روی ایران گذاشته
- اون‌ها ممکنه بگن کنترل تنگه رو در دست دارن
- ولی کاری که ما انجام می‌دیم، حتی پشت صحنه، نشون می‌ده که در عمل ما هستیم که کنترل رو در دست داریم
- از جمله از نظر نحوه‌ی مدیریت اوضاع تو اونجا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/alonews/123709" target="_blank">📅 16:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123708">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
خبرنگار : آیا اون محاصره هنوز هم برقرار هست؟
🔴
هگست :
بله، محاصره هنوز کاملاً برقرار هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/alonews/123708" target="_blank">📅 16:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123707">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fd3fd2442.mp4?token=KJTzKWNCgPvrJ7Z1p1Im_ChxnMHKmlgML7o9Um6bUuzllFxsSOlrMbUYqEQKKJ1-sS5jqmE6uAOJ9zYM9p7B1KyauJkrPvx8ixYUSjwRBaFLsNkkb2p6v4h2cxzUIt5p3b29dvyhkib517wr8GvTxpIvl1myTu02bNdpW0WyTi6jYhkkfZDQTlM5BmHS5Cw0ay5xOV2QxQRb4XIzNAZlSqg77i33yX-AO6e1zNoorbR1o_0vJl9FxoqF4qIq0m_rpg7Om0vz75sCm--OLxoTeuvorQCMJ2oC1ygFbTlT7jbN99q8mEAFPxWlTBcNtucQlKmfHa8PKqUDAbZ3_24-NDe19mnrK5BXgTKlz8SOO4liHAp5cIvthHKGOwN-mPrjZk5mqo9PrOD0nu-JJ222DotR4lusLZaRWBU-JQ8yaSs8tqkrg1mKcV6KUuPAcUzqlB6YN-lBDhra7e5bnDcEqg37iUM-evvC21F-ObFXELSbwJHlthJRIkA5UX37S7H9TCV-U6-RvnVrulBC-KIVFoDeWjC9aLmi9TKWfJq858sJDQeIKj99ge2V0P9vzL8c6QblUG9N2HG8GDC1PemgckRZ0su9DsomD16OKeB6uJ1IPu7otzDoBwf0aN9J81yBWJ43EQYGu_XEmHsc40dBXAL3oyysxh3UYc57A3SK6wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fd3fd2442.mp4?token=KJTzKWNCgPvrJ7Z1p1Im_ChxnMHKmlgML7o9Um6bUuzllFxsSOlrMbUYqEQKKJ1-sS5jqmE6uAOJ9zYM9p7B1KyauJkrPvx8ixYUSjwRBaFLsNkkb2p6v4h2cxzUIt5p3b29dvyhkib517wr8GvTxpIvl1myTu02bNdpW0WyTi6jYhkkfZDQTlM5BmHS5Cw0ay5xOV2QxQRb4XIzNAZlSqg77i33yX-AO6e1zNoorbR1o_0vJl9FxoqF4qIq0m_rpg7Om0vz75sCm--OLxoTeuvorQCMJ2oC1ygFbTlT7jbN99q8mEAFPxWlTBcNtucQlKmfHa8PKqUDAbZ3_24-NDe19mnrK5BXgTKlz8SOO4liHAp5cIvthHKGOwN-mPrjZk5mqo9PrOD0nu-JJ222DotR4lusLZaRWBU-JQ8yaSs8tqkrg1mKcV6KUuPAcUzqlB6YN-lBDhra7e5bnDcEqg37iUM-evvC21F-ObFXELSbwJHlthJRIkA5UX37S7H9TCV-U6-RvnVrulBC-KIVFoDeWjC9aLmi9TKWfJq858sJDQeIKj99ge2V0P9vzL8c6QblUG9N2HG8GDC1PemgckRZ0su9DsomD16OKeB6uJ1IPu7otzDoBwf0aN9J81yBWJ43EQYGu_XEmHsc40dBXAL3oyysxh3UYc57A3SK6wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : ما فکر می‌کنیم الان تو موقعیت خوبی هستیم که این توافق رو ببندیم، و اگه ایران نخواد، باید با وزارت جنگ روبه‌رو بشه
- ما امروز حتی از روز اول هم قوی‌تر و آماده‌تریم که اگه لازم شد اون مسیر رو بریم
- ولی ترجیح ما این نیست، ایران خیلی واضح می‌دونه ازش چی می‌خوایم، مخصوصاً توی مذاکرات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/alonews/123707" target="_blank">📅 16:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123706">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbWvUiollT7guWq70fcISvKciKS2pVR5nl5oqa3xPlJcw8VB8u7hW5MlJgDxAYS-r7ycFYBpTtw9OPIflVzufdmQtbVFnDKZ52t1MPfmsnK6hw-9nOTIzA2XDOC7lY_niaTG_nd_CvuzdI4Ml7j8tkw98wbHPWmxkeUf1nJvG38B-tzSogq36qvaqTUKO41dBlCnV2siiFLMhsPLcUQK22rXb2soSusX4G05rsgZzGz6P-YvojDaBGSaTnw36DGzUmKcAMCW2XyQcXni2s3RER7irbSSTudcDOYAm-q1NE7gQPzdcZUHt-VXL1_Gc4Gg66TSPaTefbiZhYJH0eq5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هندا ۱۲۵ شد ۳۵۰میلیون ناقابل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/alonews/123706" target="_blank">📅 16:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123705">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2fefb291e.mp4?token=ojWbTpOwuEPBWHdt4otzmGf9N_XRPAQg6TRjcvs4ZgJzJ-2J1sDIeD95KWjMvm04K1deEnXlF4r0png1U6Q9D6TDBen6mQqWvNPxr-NeIkolV0SNIj8DaR7nNmkvOU5DtLs0VYaP_cxxk52yxcxVrkBHXJsmE_2y-_QgXJjwFAgF6K8Rn9HYLxwU1NqSoxke54x4Xvo0-oWO2d4c0PHFWk0UbKducaRdiDXnB79uFB5-Dex0G5i1B6nhcstjbAl4r4jkJ-0HY_FzMkHh-5YUIM14sgMVZS5LnlrJF3RGHZO_4OTlmso6Bzg3SMUvVtbG4-MOEIwODFOvhfW7Uqw3lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2fefb291e.mp4?token=ojWbTpOwuEPBWHdt4otzmGf9N_XRPAQg6TRjcvs4ZgJzJ-2J1sDIeD95KWjMvm04K1deEnXlF4r0png1U6Q9D6TDBen6mQqWvNPxr-NeIkolV0SNIj8DaR7nNmkvOU5DtLs0VYaP_cxxk52yxcxVrkBHXJsmE_2y-_QgXJjwFAgF6K8Rn9HYLxwU1NqSoxke54x4Xvo0-oWO2d4c0PHFWk0UbKducaRdiDXnB79uFB5-Dex0G5i1B6nhcstjbAl4r4jkJ-0HY_FzMkHh-5YUIM14sgMVZS5LnlrJF3RGHZO_4OTlmso6Bzg3SMUvVtbG4-MOEIwODFOvhfW7Uqw3lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما : آریایی‌ها قاتل بودن!
اینکه بعضی‌ها میگن ما آریایی هستیم، نژادپرستیه.
تمدن ما 65 هزار ساله‌ست، آريايی‌ها کلا 4-5 هزار سال پیش اومدن.
آریایی‌ها همه رو کُشتن و به قدرت رسیدن، اینکه بگیم ما آریایی هستیم یعنی ما فرزندان کسایی هستیم که نسل کُشی کردن...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123705" target="_blank">📅 16:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123704">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3x3F5j0v5pewnFDUlOL6qhX5DK1ZMjC4C4Zg0YMRB7VLij2PqwQsL5_vG1DBQuQzrtiyLz5PGNd4yc2_l3ca2FFpR26QdnAetAqFnVawLZFQ_XKGQVketGdU0bHlgUNK23fKWe4gHkEgImTPrZmAEMfAoXqhvJSc4yICdrAcPAJYbWSuDnJx0bleFizDGNywr2yAQTKa6zAJgu57PCxDmsWZTZAdjacHLj4EtlN0Hf0phq2qLUcXBezOZMjc9GyI50CITci5Cat6KHDKzAGE2eS58FkT9pGayGBoDMzfyZGDYYRYLEsJUiW8FQSauJTemkES5d8C_W4aTihEPI2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
پیراهن اهدایی امید عالیشاه، کاپیتان تیم فوتبال پرسپولیس، به دست محمد شرفی، یکی از بازماندگان حمله به مدرسه شجره طیبه میناب رسید.
@AloSport</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/123704" target="_blank">📅 16:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
در 18 دی به یک خودرو که با خانواده بود و میخواسته از تجمعات دور شه شلیک کردن.
🔴
درجه دار شلیک میکنه
🔴
سربازِ به راننده میگه برگرد برو حواسش نبود!
🤔
یعنی چی حواسش نبود؟ اسلحه دست حرام زاده میدین نتیجه میشه جاویدنام کیان پیرفلک که با رگبار بستن خودرو سواری کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/123703" target="_blank">📅 16:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123702">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdRQhsMaLZ4JGFy-DFuaUHDh2e25zZImA-KS_098A8wGPbp8KBDezZbp3_h8Hw1l95lGPY5zN5HpqYRWp5DhV-04NzMGJU7o4YyDeE76sREWJnXOJETwivMdYmVa-I65ZcqVtJRSmPs_oFWGiH3jJ_FcWVOIwSfWFJPAvop1uPJ-JqBlferTKghqzAbiHOQWaabOP2cOOPOJ5SOaDkYF7fUl9vl83R2Hk482cf5WwtEAa8zkO8KRMMfZB_xaOzYjh4EI36xxb9hgu3oQEFGXvRCZUXgDYLBqF9tSb8oYdLdrwrSiGgttEC00QpradMTq2Buq7wwRz9O9tA6R-7zcFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، می‌گوید سفیر تام باراک حتی پس از پایان دوره‌اش به عنوان فرستاده ویژه به سوریه، نقش مهمی در سیاست ایالات متحده نسبت به سوریه و عراق ایفا خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/123702" target="_blank">📅 16:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سارا فلاحی نماینده مجلس گفت: هم روس‌ها و هم چینی‌ها تصور می‌کردند که ایران توان ایستادگی را ندارد، اما توان نظامی بومی و داخلی ایران معادلات را تغییر داد؛ در جلسه‌ای که با حضور آقای عراقچی برگزار شد، پوتین صراحتاً گفته بود نیروهای مسلح شما ما را شگفت زده کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/alonews/123701" target="_blank">📅 16:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HinCgu5zf5P_-JzqvA9jqdAzlt93FibzKEiLuqocjkOYEDysGQLwblEnZ1RWE4ZRqod1gd7QvJtvJxX_jJwp97k1ENRzWobUVcYXTXF4LP0yXQ0KgbuQafRLD-d96I-nLskFCkktlD3wnqw5Ig4-j84UujmNn2T3fGXnvvQzvFeb1N4W-6brWE8oIsPt-dXkH-oPxRbmJpT4vwaQdhisKHs0t936mKLo5B3x3jTvMEkmBn4NZFJDzv0gU54693MIW0N0wTX5fHz9X-rFEKGs-URXOHSD5fxK9Ind1IW9U-ucjGVlw-5uReH4xrmSBrSgFKCUWRYRc23OMrQjFzXo8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین نقشه از وضعیت جنوب لبنان پس از تحولات نظامی اخیر اسرائیل
🔴
زرد: منطقه تحت کنترل ارتش اسرائیل در چارچوب خط زرد
🔴
قرمز: منطقه‌ای که ارتش اسرائیل پس از آتش‌بس به تصرف درآورده است
🔴
نارنجی: منطقه‌ای که تحت تهدید و حملات ارتش اسرائیل است اما نیروهای زمینی به آن نرسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/123700" target="_blank">📅 16:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibQx8oJquapCPRhUhWj6lA9fZ7PWw1GV-bkvRSKHe4txNioqCTKIY0VM6fu1PHKSRnZshfoyKzmImlVWN8S7bu_WMqGv2_7qKcGB7b_bPucHEjHKB_jeGwlB6ir6slIK7SI0Znr8ugLC5AgUM6UlFJ9u9SbrfcsApWvqGQF4PpB2yUGcbtcl8Oxn_J1Movy3eqhxXGvn8lQnRsDyn-u2PQAo_LH8dFDa_P0DELk_XS51Aay16RwUpTMInCd7faiN8jg5A3CMbil1D0x469HXC2sly6jwBnl5lnbVjAZBNYpxAnf5mFmQcbabFingL1XxdPVU2kYtvabSew0H6sXiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، به دنبال نشست ۲۹ مه کمیسیون اروپا و بحث در مورد سیاست‌های کلان قاره سبز در قبال پکن، دولت چین هشدار تندی صادر کرده است.
🔴
چین اعلام کرده است که در صورت پافشاری و پیشبرد هرگونه اقدام تجاری محدودکننده جدید از سوی اتحادیه اروپا، این اقدامات را «قاطعانه تلافی» خواهد کرد
.
✅
@AloNeqs
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/123699" target="_blank">📅 15:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/سلیمی ، عضو هیئت رئیسه مجلس : تصمیم قطعی مجلس بر قانون کردن اعمال مدیریت بر تنگه هرمز است و این طرح نهایی و تبدیل به قانون خواهد شد.
🔴
اینکه ترامپ و دیگران می‌گویند که تنگه هرمز باید باز شود، این موضوع مربوط به ماست و اجازه نمی‌دهیم که آن‌ها تصمیم بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/123698" target="_blank">📅 15:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNQkqrUXhODb-G-R99oLB-f_6fgpNIihDhPa6hHCBNmUZE4J1GkamHSEYIcFyTZmWt5z-zlB4PxsBKB2m84zN23QoBUtwfMsY1TjI_ywxpOFOjqYKRNyHQZorq5CPzKWb9WW2STahw7kV0GIub4wJ1skuoOaCHJFddGCpoz_jr0TOjCKbiJCD4XbJO-mo_qXBsuFNOLXzSEHbx2EcHpbBRaRBMH9eW3SqwSgMujIt_8bDTQpReJdFns6mCldPoFpEKpTJABlhOulGzzN-mnUKEXjmSm9codQChBWdcPl_o9HfxsYfWxe6iDBha3K55n443t6dlSoFitmCRd6UIBqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت کوین از جمع ۱۰ دارایی برتر جهان حذف شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/123697" target="_blank">📅 15:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfc9378ea.mp4?token=f2QG9UW2bJ43zlzri8iZ_jEHOaVrJCIFBQ7k3GsXUQZ6KZ9_luTyUATJEuLQTKU7rBOojF5DG5UYphTUBapYQIS5uD2W3Z4jGXUYggjpiui-Yc7BW7vbfve0yoUzsb35cQ_njcZ6-EJxR9nNb1aVSS3UZE2nlVCC-ZbE-yzvQ_2TQnP1Zmg0kWvy7-uYqIcgE1XRiWkacoKzEg5txOdU8RrjZKZdZ2lROwzcNBrSPH-Ds7Far1vW6lA-YKYwf7ijfPVb6eTFjSHvDbMR1tVLpB848ixrnjN-tp5v_U-Vz6opHkWJmi8kE5nq15tAwqllGyzCi7I_DbAStBzKqDXA4D5YVNSQZ_DiCZQrzA3J92BpOEGjipioG7M8ZQX4-ABbQE5y81Y1sK5ioo7dvpJSNnN-hFXb3zxMlMWiigM-9DOS602CqDN3Mw_uBsTuKVWSJ0wK0X86TjS7_LWilAeVo5ijmyxg3mppFTRxPfr6XoJAiNHM-Bs_38n6WhuZRzFyVwE9n2XEXgBlI7PxRzcGzYH7r0pykE-uop30dxS3xsvi_4ItmpGzQxBmEyYuRcDxepyAUl5vP1YhbRNuVpPCeoTcELXZ5oXa6fbgYEFMPZS-qiMKHT5-lkytPgkGSgJeoIVb7-wMNEI3WWDONjAdPw6jBNuPsxwdt67tDkyvsy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfc9378ea.mp4?token=f2QG9UW2bJ43zlzri8iZ_jEHOaVrJCIFBQ7k3GsXUQZ6KZ9_luTyUATJEuLQTKU7rBOojF5DG5UYphTUBapYQIS5uD2W3Z4jGXUYggjpiui-Yc7BW7vbfve0yoUzsb35cQ_njcZ6-EJxR9nNb1aVSS3UZE2nlVCC-ZbE-yzvQ_2TQnP1Zmg0kWvy7-uYqIcgE1XRiWkacoKzEg5txOdU8RrjZKZdZ2lROwzcNBrSPH-Ds7Far1vW6lA-YKYwf7ijfPVb6eTFjSHvDbMR1tVLpB848ixrnjN-tp5v_U-Vz6opHkWJmi8kE5nq15tAwqllGyzCi7I_DbAStBzKqDXA4D5YVNSQZ_DiCZQrzA3J92BpOEGjipioG7M8ZQX4-ABbQE5y81Y1sK5ioo7dvpJSNnN-hFXb3zxMlMWiigM-9DOS602CqDN3Mw_uBsTuKVWSJ0wK0X86TjS7_LWilAeVo5ijmyxg3mppFTRxPfr6XoJAiNHM-Bs_38n6WhuZRzFyVwE9n2XEXgBlI7PxRzcGzYH7r0pykE-uop30dxS3xsvi_4ItmpGzQxBmEyYuRcDxepyAUl5vP1YhbRNuVpPCeoTcELXZ5oXa6fbgYEFMPZS-qiMKHT5-lkytPgkGSgJeoIVb7-wMNEI3WWDONjAdPw6jBNuPsxwdt67tDkyvsy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هگست : ترامپ روی منافع ملی آمریکا تمرکز کرده
🔴
از ونزوئلا و مادورو گرفته تا عملیات‌های دریایی علیه کارتل‌ها و مأموریت‌های نظامی مثل «خشم حماسی»
🔴
آما آماده از سرگیری جنگ هستیم تا از منافع کشورمون دفاع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123696" target="_blank">📅 15:47 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
هگست : ما هنوز کارای جهانی‌مون رو داریم؛ مثلاً اینکه ایران نباید به سلاح هسته‌ای برسه، روش هم تمرکز داریم، در کنارش می‌تونیم چندتا کار رو هم‌زمان پیش ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123695" target="_blank">📅 15:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فیدان: اولویت مذاکرات بین تهران و واشنگتن حل مساله تنگه هرمز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123694" target="_blank">📅 15:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9608511f02.mp4?token=tViqUO9aMITwAvcpplzJf4ATRzp1NmOrwT1-cls9_q12YTzq3-ZYxkMCp-m7SfZxnMIu6Wt344j5v2V22B8dx0CZ-a4LikTb-yK0tLAK7kfWZ5WzZ2XtTwDIQQncO6wJbtwuOIf6Ak2t809hWrERSjOGW6ccyymy8qx0FRgC0R0QSHtJJv1deOYGVhT4wAgWVGHmO4OMkiDKYQdvkRGyH-FZi29Q1V4kae_5D9MMDLog-asR76p37g60GtnWAtqe_TWqYXoDnacCBv3z4iPQdbS3FbrCSOdRy66R96O1p0TbZK9vFuPFuX3U3CptBfT8So7kx_ykUq_FqY2FaEzQtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9608511f02.mp4?token=tViqUO9aMITwAvcpplzJf4ATRzp1NmOrwT1-cls9_q12YTzq3-ZYxkMCp-m7SfZxnMIu6Wt344j5v2V22B8dx0CZ-a4LikTb-yK0tLAK7kfWZ5WzZ2XtTwDIQQncO6wJbtwuOIf6Ak2t809hWrERSjOGW6ccyymy8qx0FRgC0R0QSHtJJv1deOYGVhT4wAgWVGHmO4OMkiDKYQdvkRGyH-FZi29Q1V4kae_5D9MMDLog-asR76p37g60GtnWAtqe_TWqYXoDnacCBv3z4iPQdbS3FbrCSOdRy66R96O1p0TbZK9vFuPFuX3U3CptBfT8So7kx_ykUq_FqY2FaEzQtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا؛ : آمریکا با نخست‌وزیر پاکستان و فرمانده ارتش‌شون «دوستی واقعی» داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123693" target="_blank">📅 15:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
فرانسه: درصدد ساخت یک ناو هواپیمابر هسته‌ای جدید برای تقویت حضور دریایی استراتژیک هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123692" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
انهدام مهمات عمل‌نکرده در حومه بندرعباس از یکشنبه ۱۰ خرداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123690" target="_blank">📅 15:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / وزیر جنگ آمریکا: هر لحظه آماده ایم جنگ علیه ایران را از سر بگیریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123689" target="_blank">📅 15:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d4a3df4f.mp4?token=qQrLQostDsds_KXf3dZ2WqRur9dEUYNpVtvX8ebGkfZnchRKaUost5ZRwtHi1SLJqep6cmYmLoOLO-n-iadQGYYcIzDNs2mScU1U5Ut-EwozZ7w-3AkOTxt9P5bCLF0EPPuFSWDsfLOH1ODFXcN06jq9ni9ANBwF0ZoIzCmgNBEgOAoSASICLt7Fv7sBPv229TitI7Sc8gf0VbbnotvVjqvZ_nUQKDnIx2QJ44iHU-DnfaM7EYnPVRr-d4ftghlfrPPdxJEFOWI4a1tofvIpY4KuM2BB9VmLBR8XHM4WpvS08QRRxK6uCniObnQRcA7SJCVtEr5Wp6_Dz3uloCGy1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d4a3df4f.mp4?token=qQrLQostDsds_KXf3dZ2WqRur9dEUYNpVtvX8ebGkfZnchRKaUost5ZRwtHi1SLJqep6cmYmLoOLO-n-iadQGYYcIzDNs2mScU1U5Ut-EwozZ7w-3AkOTxt9P5bCLF0EPPuFSWDsfLOH1ODFXcN06jq9ni9ANBwF0ZoIzCmgNBEgOAoSASICLt7Fv7sBPv229TitI7Sc8gf0VbbnotvVjqvZ_nUQKDnIx2QJ44iHU-DnfaM7EYnPVRr-d4ftghlfrPPdxJEFOWI4a1tofvIpY4KuM2BB9VmLBR8XHM4WpvS08QRRxK6uCniObnQRcA7SJCVtEr5Wp6_Dz3uloCGy1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: سیاست ما در مورد تایوان همان است که در ابتدای این دولت بود.
🔴
تنها تغییری که ممکن است ببینید نحوه صحبت ما درباره کل آن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123688" target="_blank">📅 15:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac83a7320.mp4?token=W7ZPgaTjRRV7AKBtZHCpxx_uS_ZFUmRvYKs2hDEOUmuQdGXfCC-qf3dXNHIeBWWi_y7bOj763gRdH5AG_PKEakVmHjIEa--nKAOV0e5IM8LpofvK_xOSNvTx5ddPEHOfWcpfP4HK-0woJYBX1JZGrC1_E_BSJltZQQND_q1-SMGj_RH9PM_l6Mig05Kpgh18TvzahPjuj588c1zKjlMQq9WM_ZWeHS42vbcHA15ezmNR3E2lfWcpIX9fX3YZY171LRACl7N9H-WPUpakKkaTz1il4R32qqzu5Z-lf2hSmZ16JsxnipXVGEe_zOXiDlORup_d1QT6rU1ULNWUVmephQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac83a7320.mp4?token=W7ZPgaTjRRV7AKBtZHCpxx_uS_ZFUmRvYKs2hDEOUmuQdGXfCC-qf3dXNHIeBWWi_y7bOj763gRdH5AG_PKEakVmHjIEa--nKAOV0e5IM8LpofvK_xOSNvTx5ddPEHOfWcpfP4HK-0woJYBX1JZGrC1_E_BSJltZQQND_q1-SMGj_RH9PM_l6Mig05Kpgh18TvzahPjuj588c1zKjlMQq9WM_ZWeHS42vbcHA15ezmNR3E2lfWcpIX9fX3YZY171LRACl7N9H-WPUpakKkaTz1il4R32qqzu5Z-lf2hSmZ16JsxnipXVGEe_zOXiDlORup_d1QT6rU1ULNWUVmephQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگست درباره ایران: ایران می‌خواهد بگوید که کنترل تنگه را در دست دارد، اما این ما هستیم.
🔴
و همه چیز پشت صحنه نشان می‌دهد که وقتی صحبت از آن می‌شود، ما کنترل را در دست داریم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123687" target="_blank">📅 15:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
واشنگتن پست: افشای پیام‌های داخلی؛ تلاش پنتاگون برای استخدام سربازان به عنوان تماشاگر در مسابقات UFC کاخ سفید
🔴
بر اساس گزارش روزنامه واشنگتن پست، اسناد و یادداشت‌های داخلی نشان می‌دهند که پنتاگون در حال جذب و استخدام نیروهای نظامی است تا به عنوان تماشاگر در رویداد مسابقات UFC (هنرهای رزمی ترکیبی) دونالد ترامپ در محوطه کاخ سفید حضور پیدا کنند.
🔴
طبق مفاد این پیام‌های داخلی، پرسنل نظامی متقاضی باید شخصاً هزینه سفر و اقامت خود را پرداخت کنند.
🔴
علاوه بر این، داوطلبان برای واجد شرایط شدن و حضور در این مراسم، باید معیارهای سخت‌گیرانه و مشخصی از آمادگی و ظاهر جسمانی را دارا باشند.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123686" target="_blank">📅 15:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس: یک سوم ظرفیت تولید گاز در جنگ اخیر از دست رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/alonews/123685" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💔
خانواده امیرمحمد شاه‌کرمی ۶۰ روز تمام دنبال پسر ۱۴ ساله‌شان گشتند؛ تا اینکه پیکرش را در سردخانه کهریزک پیدا کردند.
🔴
در این مدت حتی با گوشی امیرمحمد با خانواده‌اش تماس گرفتند و وانمود کردند که او بازداشت شده و زنده است.
🔴
خواهرش از لحظه دیدن پیکر امیرمحمد…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123684" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKg5oLSKO5VGxJ3XKz8mVbWgf9c4KtEEslN6-N0-nWRb6EXhYL4h3o161UhlYftPy9SlR5sQxylOwgF2x5sU3jWb4jt_7Imy0o92YJg-cB90aZaRush9YywjSle3cScg9J5a9U5HIIsH0DeEyq4vvBqUeV5s7ub7TU06JbL4GdWRCnJzwz7t1PALOxBBqFDkGZsb8JF_jV9yMstcFi_IdYbtKPfWqspQnL57xopXWKGx5L__NaEoUnozB_RR2subO-J3CS1Rk1OznFdD8MzkcjmlERVWylnSC6GX0xyyRBtDByV57WLrdhv6Sf3U_fvUPXjaK4PJPe6t-zMZbb5ANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل حملات هوایی را به حومه شهر شوکین در جنوب لبنان انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/123683" target="_blank">📅 15:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
امنیت دریایی عمان: هشدار به کشتی‌ها برای احتیاط پس از رصد جسمی مظنون به مین در غرب منطقه عبور ساحلی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123682" target="_blank">📅 15:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سلطنت عمان: ما در آب‌های سرزمینی عمان جسمی شناور را مشاهده کردیم که مظنون به مین دریایی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123681" target="_blank">📅 15:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
رئیس‌جمهور لبنان، جوزف عون، و نخست‌وزیر نواف سلام در دیداری در کاخ بعبدا درباره حملات مداوم اسرائیل در جنوب لبنان و تلاش‌ها برای تضمین آتش‌بس گفتگو کردند، طبق بیانیه‌ای از ریاست‌جمهوری لبنان.
🔴
این دو رهبر توافق کردند که ارتباطات را برای پایان دادن به آنچه که آن را اقدامات محکوم‌شده اسرائیل توصیف کردند، تشدید کنند. این دیدار همچنین شامل ارزیابی مذاکرات واشنگتن بین هیئت‌های نظامی لبنان، آمریکا و اسرائیل بود که در آن طرف لبنانی تعهد خود را به اولویت دادن به آتش‌بس مجدداً تأکید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/123680" target="_blank">📅 15:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
روسیه سفیر خود را در ارمنستان برای مشورت فراخوانده است، با استناد به تلاش عمیق‌تر ایروان برای پیوستن به اتحادیه اروپا، طبق گزارش آژانس آنادولو.
🔴
این اقدام نشان‌دهنده افزایش ناامیدی مسکو از چرخش غربی ارمنستان است که در میان روابط پرتنش بین دو متحد سنتی تسریع شده است. ایروان به طور فزاینده‌ای به دنبال روابط نزدیک‌تر با اتحادیه اروپا و نهادهای غربی بوده است، تغییری که روسیه آن را به عنوان چالشی مستقیم برای نفوذ خود در قفقاز جنوبی می‌بیند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123679" target="_blank">📅 15:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123678">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcs16yEQdjGUQG7s1PeInVeZh-tqERIjYEcSwdvsvniqsGqVwjxvIHcYZ8ZPqxMJaKvvjIhGq-yY5iZA5HN71dVhlIwyE-HuXq1gu3wwmphyjIOnmam6ANlV35ybuYi7HGSps0ritVY7ICiQtbev8QBVdnYTB5oP1FuCfbA2hP3Zof2Bu4LAM6buKRjwzwVuIc2EguTPIbyJ8ueYvzhx8BuV8m_Sk3gTJGAr24YDEORuI7ewR2QKovTQfFSGm23L4SBssn1BUY5bjxjHH4V854d89DeZjiOnOe9HwY2dPxVx5aSRm3LbwpYM_A-mwavd0I5lSyQ-sWScfQh9dGBNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی خطاب به وزیر خزانه‌داری آمریکا: به جای هارت و پورت اضافی به فکر تعظیم باش!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/123678" target="_blank">📅 15:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
ارتش لبنان اعلام کرد که دو سرباز پس از هدف قرار گرفتن داخل یک وسیله نقلیه توسط پهپاد اسرائیلی در جاده آبا (نبطیه) به شدت زخمی شدند.
🔴
آنها برای درمان به بیمارستان منتقل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123677" target="_blank">📅 15:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uM_0XM47puM8NFig5JDFHf45-Bkm537WPN_3kjOrFe9ZoVPgLiWUfQWDC6G-xYN44HZS42p2WAf1z0HOJug_ybIsPPcPMWKGfWVPi-2glzIDl6z3-vBEypoEP9AHHLubWKDIj_wacopERFg18BmqhR8VPH91bx-7dLDixk_IqXJF_JJXK6KOR-uCS1l7IyQIaxQ7WCZmqufr6E42uBoJ0ZRhmVwlA1PK0Dix6KOawOUllXWGDthr7r05K4WrmDW5Sw2fzukWeXjcEVyw4335XNliBO938ujcwIZ5HW3pdnEru3pmq-Yu3Kn7vmHdeAt3z3xxT3uDFE78jnWsf-UeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UjtqcGJhiwjJAz1PmqX_5p_q2lHQxCjH3aBGYEXt_07_ICv22P-naicoI9UWu7lUO85lOD08WKEJLJ89AfSKkpxYhle-g8pOZcKEK7W1wr3-Q2o3BddGAKD58u8G3uGIIjspSzu4Kh2S3Wr23-6myKmLd69aq0JDbZbKcrrLzBpMxIjB3Xq2w29LO4Ul2199678J-NEibv6QSDCjsueFN8nZm7SHtnwgOCXXyng0lBNpRAp2pKxFksqKTP06kJR3i9puUhseOQGA7fmslNuZCLDDbS9lo1dRG01FdN9k4SPvVcfQ9I-cay0-wnxlGR9vClfXb-qsoBeJ0h4avVG6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MA6_XI0fiB55zkKqm7w3USQmcEURYjmPyMXW2PfrjjtyI9d-ud2atIZbyHT0GwTsdaIw0hduWdT1mB1WVU-NlmOkbrju_pYtkKKetwFf2FonRwWyMAJV1f9-vEzIj8Ux6OO6r1eckJcoGk2-N0AITPRVO2BwImRGSNuPuLhSyjwawPIcQmorEJ6pT1wsDpOwhZC0HqyWeL2GwNRC13UDKoEYZHDx8-_aSkv8cY0eWBZwTCrClvgbukFxbj_RCtnBTEpu0OZ3WLjtrRM919et6jptrWLhgmUfIeaZuN0UdpMP_KYWSmK-oGd7IsLYTYMeAGUcDymN6Q_cqZhVAAuvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E96o34KAgujcYtmdSMvyeoSEBM4vPNvbTmbtTt4QhiAYGxr3arMrM23ieyVPZcBld-ByMHzlai0PUMJRsa7Z03PtbHhOJSNFCvvUEvfjb1caqcE9qJqeaxLZysG0em85yNtg3aJ0N6l0bpdCopMyzEQH9pJhAaA9r98CeBQ_i22-dToV-kbD1UaNo5uTfmDbYDg6chH35Gwc1_hapAuYfSpw8SCc1Nh3vJUA0bkr2mTRyrENFUDwUwTG0wBNgzkJqS4awD-OZ3dkiE7WMIoYBfkhqTOiLWyuhlEjTFOwyvl3EKLflCcG-qFWnK13RVSWoJLo1MMim0GS2Kn42pmfJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش سودان یک پهپاد رزمی CH-95 ساخت چین که توسط نیروهای پشتیبانی سریع تحت حمایت امارات در نزدیکی ربک پرواز می‌کرد را سرنگون کرد، تصاویر لاشه آن موشک ضد تانک Blue Arrow 11 آن را ظاهراً سالم نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123673" target="_blank">📅 15:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا:
هرجا که توانسته‌ایم به اوکراین کمک کنیم، کمک کرده‌ایم.
🔴
هرجا که توانسته‌ایم اروپا را قادر سازیم تا بیشتر عمل کند، این کار را کرده‌ایم.
🔴
اگر به میزان پولی که هزینه شده نگاه کنید، اروپا وارد میدان شده و اوکراین در این فرآیند دست‌کم به همان اندازه (اگر نه بیشتر) مؤثر بوده است.
🔴
بنابراین، ما می‌خواهیم آنها بتوانند از خود دفاع کنند و راهی پیدا خواهیم کرد تا مطمئن شویم می‌توانیم به آنها کمک کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123672" target="_blank">📅 15:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">💔
خانواده امیرمحمد شاه‌کرمی ۶۰ روز تمام دنبال پسر ۱۴ ساله‌شان گشتند؛ تا اینکه پیکرش را در سردخانه کهریزک پیدا کردند.
🔴
در این مدت حتی با گوشی امیرمحمد با خانواده‌اش تماس گرفتند و وانمود کردند که او بازداشت شده و زنده است.
🔴
خواهرش از لحظه دیدن پیکر امیرمحمد…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123671" target="_blank">📅 15:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce3370eb3.mp4?token=KyvofjRa3_9z4Acf5OaCyYGFbAt5w6CarK5RFpyWsguQpvsmiiKciDlBBkJbKnePIJ83cQTmfyYuIppG-1vHtwqIRhU1T8wbSAaI_69DqemgCu6EJ6ZEJa6LCxci8GtElGWv22lYKqzdy2VW4nJqgoQ-sQp05Q8KgOo5UYwvuV2kuJhM9QhUQF90xiR3wpXXPkunEQj9BCCRYeXJrzznNdLMCKFT0m7cLpLXPmFxiNwYxJiZSIw01CrIrpVcVidHNl-kq2To6tGHTNPxkqeC-58tMiIF_AJ0fec_3e_0gXqXcZRcgV6gwIASodIotdYpC2akwp7_f5ebJQBGf1QReoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce3370eb3.mp4?token=KyvofjRa3_9z4Acf5OaCyYGFbAt5w6CarK5RFpyWsguQpvsmiiKciDlBBkJbKnePIJ83cQTmfyYuIppG-1vHtwqIRhU1T8wbSAaI_69DqemgCu6EJ6ZEJa6LCxci8GtElGWv22lYKqzdy2VW4nJqgoQ-sQp05Q8KgOo5UYwvuV2kuJhM9QhUQF90xiR3wpXXPkunEQj9BCCRYeXJrzznNdLMCKFT0m7cLpLXPmFxiNwYxJiZSIw01CrIrpVcVidHNl-kq2To6tGHTNPxkqeC-58tMiIF_AJ0fec_3e_0gXqXcZRcgV6gwIASodIotdYpC2akwp7_f5ebJQBGf1QReoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث: آنچه در بودجه سال ۲۰۲۷ رئیس‌جمهور ترامپ خواهید دید، سرمایه‌گذاری ۵۶ میلیارد دلاری در تسلط بر پهپادها است.
🔴
ما همچنان از آنچه اوکراین در میدان نبرد انجام داده است، می‌آموزیم.
🔴
ما چیزهای زیادی از اوکراین و نحوه عملکرد آن‌ها یاد گرفته‌ایم.
🔴
قصد داریم نه تنها هم‌سطح باشیم، بلکه بهترین در جهان در این زمینه باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/123670" target="_blank">📅 15:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی: ما گفتگو و تبادل نظر حداقلی (با ایران) داریم، اما در حال حاضر بسیار محدود است.
🔴
دیدگاه آنها (ایران) این است در حالی که درگیری ادامه دارد، زمان برای از سرگیری همکاری کامل فرا نرسیده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/alonews/123669" target="_blank">📅 15:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWie38ey8b4W4ojcC02Y2h4BAVuALasu9bY9wccF47Xx1ODtKU2DeybGFLcEpemZAAHDb7r6fHcMB4TynYhpC83qNitXsC1vkdGITshrH8tBhh_JnwTtyUQZZAXZZVeokHKb5b7Mal81BC-Yj34wANmnT20M0lvOZmuafu4Xk3yUABIP4e4VrCWJG4TQu-yPGei3vdNaZxukaeizNTULmwoBaHNBDRQ26okRQg_EJL0BzxCHXhYDLIjsaAZ2jxJHYn7iB5qNntEGdAnEusMsd7B-TJJL_Te1zlEidZ6kvYqtrlwlkS8B-9aPdgl6TszqOmScPz3Ww9DsuFNjaSP9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت برنج در ماه می ۲۰ درصد رشد داشته که بیشترین میزان در دو دهه اخیر بوده است
🔴
به غیر از افزایش شدید قیمت کود تحت تأثیر جنگ در خاورمیانه، شرایط آب و هوای سخت در کشورهای آسیای شرقی هم چشم انداز تولید برنج را تیره کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/123668" target="_blank">📅 15:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / وزیر جنگ آمریکا: به محاصره دریایی ایران ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/123667" target="_blank">📅 15:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
ما گفتگو و تبادل نظر حداقلی (با ایران) داریم، اما در حال حاضر بسیار محدود است.
🔴
دیدگاه آنها (ایران) این است در حالی که درگیری ادامه دارد، زمان برای از سرگیری همکاری کامل فرا نرسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/123666" target="_blank">📅 15:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
الجزیره: وضعیت امنیتی در تنگه هرمز هنوز «بحرانی» است
🔴
هیئت عملیات تجارت بریتانیا اعلام کرد که سطح تهدید امنیت دریایی در تنگه هرمز به دلیل اقدامات محاصره‌آمیز، همچنان بسیار بحرانی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/123665" target="_blank">📅 15:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123664">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d88485ba.mp4?token=qPQyek4Ps0VzXQUfcTP-COHpN3fScAJecUGgk6FNth3z3Q2kQFrbKXlueZL7dvfneiugRy_N0VJINoN-CNPPPS9XSRqeqSpXWZB2ktNg-dbF1wu-4NIKFG4qTZLMZtkSruHuto343HeO_SGwkSOQz2tUGjyxGPJJnboVzM_6HGp6uJT3eh-ugKI3QiGwRqG8i6PfnbT1gp8dXAzC7NsF5Poa0ySBlYDhbgN1BtvhXmTodb_1rBxsE2oqEcSrBLNmQgYbSnmOHxPeRo0RVoV7rC0Nr4OAyJouLkD6mUCV6bPF_4-OKemlqm48Cz6zVdY8IIP1k88iROVPKdWP8goeYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d88485ba.mp4?token=qPQyek4Ps0VzXQUfcTP-COHpN3fScAJecUGgk6FNth3z3Q2kQFrbKXlueZL7dvfneiugRy_N0VJINoN-CNPPPS9XSRqeqSpXWZB2ktNg-dbF1wu-4NIKFG4qTZLMZtkSruHuto343HeO_SGwkSOQz2tUGjyxGPJJnboVzM_6HGp6uJT3eh-ugKI3QiGwRqG8i6PfnbT1gp8dXAzC7NsF5Poa0ySBlYDhbgN1BtvhXmTodb_1rBxsE2oqEcSrBLNmQgYbSnmOHxPeRo0RVoV7rC0Nr4OAyJouLkD6mUCV6bPF_4-OKemlqm48Cz6zVdY8IIP1k88iROVPKdWP8goeYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
خانواده امیرمحمد شاه‌کرمی ۶۰ روز تمام دنبال پسر ۱۴ ساله‌شان گشتند؛ تا اینکه پیکرش را در سردخانه کهریزک پیدا کردند.
🔴
در این مدت حتی با گوشی امیرمحمد با خانواده‌اش تماس گرفتند و وانمود کردند که او بازداشت شده و زنده است.
🔴
خواهرش از لحظه دیدن پیکر امیرمحمد در سردخانه و شیون مادر و پدر ویدیویی منتشر کرده و نوشته: «برادرم خوابیده بود؛ سرد، بی‌صدا…»
🔴
امیرمحمد ۱۸ دی از خانه بیرون رفت و دیگر هرگز به خانه برنگشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/alonews/123664" target="_blank">📅 15:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123663">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری /  منابع ارشد نظامی لبنان به آناتولی می‌گویند نیروهای اسرائیلی از رودخانه لیتانی در جنوب لبنان عبور کرده و به حومه شهر نبطیه رسیده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123663" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123662">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بلومبرگ: تداوم چالش‌های اقتصادی روسیه به‌رغم جهش قیمت نفت خام و لغو موقت تحریم‌ها
🔴
بر اساس گزارش بلومبرگ، جهش و افزایش شدید قیمت نفت خام که در پی جنگ ایران رخ داده است، نتوانسته اقتصاد روسیه را از بحران نجات دهد.
🔴
این گزارش اشاره می‌کند که حتی لغو موقت تحریم‌های ایالات متحده علیه نفت روسیه نیز برای دور نگه داشتن اقتصاد این کشور از مشکلات و چالش‌های جدی کافی نبوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/123662" target="_blank">📅 14:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123661">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
صداوسیما: سامانه آرش‌های کمانگیر که چند شب قبل یک پهپاد اوربیتال را ساقط کرده بودند، دیشب نیز پهپاد اسرائیلی را بر فراز جزیره قشم سرنگون کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123661" target="_blank">📅 14:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
العربی الجديد به نقل از منابع رسمی لبنانی: جلسه پنتاگون دیروز هیچ پیشرفتی به ویژه در تثبیت کامل آتش‌بس نداشت
🔴
اسرائیل تا کنون بر ادامه عملیات خود و ایجاد منطقه حائل در جنوب اصرار دارد
🔴
درخواست‌های از سمت اسرائیل وجود دارد که در شرایط فعلی قابل اجرا نیست
🔴
ارتش لبنان بر اولویت آتش‌بس و عقب‌نشینی اسرائیل برای گسترش نفوذ در جنوب و اعمال کنترل خود تأکید دارد
🔴
ارتش لبنان در جلسه واشنگتن وجود موانعی را که مانع اجرای طرح محدودسازی سلاح می‌شود، تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/123660" target="_blank">📅 14:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اسکورت هوایی پوتین در آسمان آستانه از نمای کابین جنگنده قزاقستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/123659" target="_blank">📅 14:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41fc124551.mp4?token=eYSft-OTIlM4ID6oSIn707U7WlOlad0WK4rLA5sTdaD3MY6vUP6v9QwQAeT-biR6eEuvKjfw7Pc8abexrbVT59-9XBMcjQfeun_JeiWKD-1JMh2QPvrIAoPLUpIGl8fh_jnc82xcgwJpmtreHxdE_1OHBwjWsvas55ze3o2M9xUb16al2-zhmzrahlg4RWaWRR9XFkDlPQAb9VgLN6WeC_tWHGskss83ihYpi-0DDCWYWVxZNVs1_PyD_9hJYQK3-9nDxNVS3WL6zap4HRKX854w5rwnSsEAhrEHAT42t25fVGQxcVxqIbx0CMsta7W8M8gJ_2WBxa1n15TstCyMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41fc124551.mp4?token=eYSft-OTIlM4ID6oSIn707U7WlOlad0WK4rLA5sTdaD3MY6vUP6v9QwQAeT-biR6eEuvKjfw7Pc8abexrbVT59-9XBMcjQfeun_JeiWKD-1JMh2QPvrIAoPLUpIGl8fh_jnc82xcgwJpmtreHxdE_1OHBwjWsvas55ze3o2M9xUb16al2-zhmzrahlg4RWaWRR9XFkDlPQAb9VgLN6WeC_tWHGskss83ihYpi-0DDCWYWVxZNVs1_PyD_9hJYQK3-9nDxNVS3WL6zap4HRKX854w5rwnSsEAhrEHAT42t25fVGQxcVxqIbx0CMsta7W8M8gJ_2WBxa1n15TstCyMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در شبانه‌روز گذشته ۲۰ کشتی با هماهنگی نیروی دریایی سپاه از تنگۀ هرمز  عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/123658" target="_blank">📅 14:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_qjeMvfJx0-BNt8CrbabKBn3B-ljsr9v0et_sU5lRuEvZE_yD6-0rBl3prFj3dPJi8srcSC0IR2_mLaT_O8oGubLtzQOUXIfyU0vpxZ4uTRJhxAfW8VySm2mBuXNVJsw5tMYBrMVMiXH1ISdNjIOqM_9UE7j9yQbralG7a95e8G1AD1FbMwobA59_ArPDjaVjBbiv01NxoWLoGzAT8xRjqXJBxxsddiMlpRQDT6If88jsBSg1SPJhxX_0tODbMfw9K_0bfpVqKPxG49MQZRdSCQ62r_Ti2lD7fPoJUzrL3q07nGQ9uSzjjDpTRQUF38kmsdNvT9drNp9I4yhK4Prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای اسرائیل چهارمین هشدار روزانه را به ساکنان جنوب لبنان به ویژه این شهرهارا صادر کردند: المرونیة، اللوبیه، مایدون، انصاریه، زفاتا، تفاحیتا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/123657" target="_blank">📅 14:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EruCxHiXcEJO1oZmu8DQgLrMFPBQEhKGzEBu32CAyTM-dzzx5CyjSbDtcT_9xybgNaLbE6VjGzcWadW3WdQmEHNU7-CRUeiIGDYc2HssSdohZpk8zGlpFFcQ3OoI2Wb5tZZH9gA5BEm9IQlVw4joHBQ3UCJbMkp27uWaWBJP-y5OWYIvfOZZYA8JPjcJo3L8zIlVcHIgRAdidWN1rebrCNk4xR7Jz2hD4dsBKJpAwyWiFkauPc2ZKRWaqT1H4kQf8r1ECCtlggDG0YAgLXfJPqvUJryi3aj88yWm-uJMCY681bxIKBJH1oT0_cMAD-hNqjpVyoAL8AxU6bKWHKacSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123656" target="_blank">📅 14:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
وال استریت ژورنال: عربستان سعودی در اوایل آوریل به طور خصوصی به واشنگتن شکایت کرد که ده‌ها حمله تلافی‌جویانه امارات متحده عربی به اهداف ایرانی — از جمله تأسیسات نفتی در بندرعباس و عسلویه — در حال به خطر انداختن زیرساخت‌های انرژی خلیج فارس توسط حملات متقابل ایرانی و افزایش قیمت نفت است.
🔴
ریاض از آمریکا خواست تا ابوظبی را تحت فشار قرار دهد که این حملات را متوقف کند و به تلاش‌های دیپلماتیک بپیوندد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/123655" target="_blank">📅 14:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123652">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/MLS-YP_DzMnTVDKTScW6LD3ItZmvKOveBzJ3-uhP8zLD9MN92sBWAVw29-3VNPcsJx0vfk3gqKBrpOquPmqzrsFwgaNADVUfkIOklk9oe_29-EfSJV0Ob1v6wmbuJ899lDuj7dK1VEGUXagfT5hfdkW2YjrPMZyx993ype2LNoegNeSGVI6l7ucg6YL1VgBoEp3Qp1fx8BebFWn2Da6-buR6p8bl-mWtqEGpl37GzPZxMLIX88z-pWQqJ1byUEcBnebSC3fkDc3MiF29jlqD5EMaNXw_Ai7IQwZHAqI_HXAwMnM6wSXY9Vl1lojiH4aJmSbvBgD_Z5G-ojYTaqq64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/A5U3p5mkJIrD6V1r7rDADtOl6XIVnU_QG_9KsbpRT0M385rp9Y9Vj3qCPtZMGIPNJbZNTOZas75JN4MEh9E_Y9otYt86sjicRNxdRSr8XMTmkNodzDt0LUNkrMg2ucL16PSIQ7ozfSlWbawaImPJMVJEr5fyJ6oNE_ANJtIpKYvJ0DgnVZjBb9cKEKPm-cIII8LhSQsAgPDTgwTFWZE0VU42dmmutAe7CgPjTZn1_ku_nCp-8f_DV3eS3Iwzl8r03WVtOLCHb1CnUFmat2bzNNVUcMwVOJ37cvSOtJC1s5owMSraeZiMm0_qAv51yLd9-6OZ1m_y-Cjs3vWE6TSv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Boeu14ZiThqYRLu9md6OL6MU0B8Tp80P7QaKFgAENJx9WutDMmemlyetMF6SeXS_fBwSJZ6KUNngiGw8T9_VSeny2BAhZfXVyshnwPFpBm4DidPENH5gpjQFAE4zKbBvFJf-PDDp5yY5kDzhuholB8yWMG9JsMAlgECkenH-I3-n6SB9kqwJPnMPt99hyAg8ir6IUH1pcvb1iS4b8GvQwcJGdy8yqNhYFesZ3qR_clQTU1VqpzXdU6Gv-37JGov71RzMYkAWbbpTlkKdBmDbWb8jLCQoWV1otG3yeAp2udfWf07XzTeiwM3lymrq_Hj58aWqhppo9Ov5D_YaCTtJJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک سامانه پدافندی میان‌برد سوم خرداد که توسط نیروهای سپاه در کرمانشاه در حال بازیابی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/123652" target="_blank">📅 14:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123651">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قطر: عوارض موقت عبور از تنگه هرمز قابل مذاکره است
🔴
شیخ سعود بن عبدالرحمن آل ثانی، معاون نخست‌وزیر قطر، امروز در یک کنفرانس دفاعی آسیایی در سنگاپور گفت که قطر با هزینه‌های قانونی دائمی برای عبور و مرور از تنگه هرمز مخالف است، اما عوارض موقت قابل مذاکره است و می‌تواند به احیای عبور و مرور عادی از این آبراه‌های کلیدی کمک کند.
🔴
معاون نخست‌وزیر قطر همچنین گفت که دوحه در تلاش است تا روابطش را با آمریکا و ایران متعادل کند و به دنبال اجماع در شورای همکاری خلیج فارس بر سر یک راهبرد جامع در قبال ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/123651" target="_blank">📅 14:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123650">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نیویورک تایمز: پیش‌نویس توافق آتش‌بس بین آمریکا و ایران شامل یک «برنامه بازسازی» و «صندوق سرمایه‌گذاری» است که بخشی از آن توسط ایالات متحده اداره می‌شود و در صورت توافق نهایی به ایران وعده داده خواهد شد. برخی از منابع آن‌ها اعلام کردند که این صندوق ۳۰۰ میلیارد دلار خواهد بود و جزئیات بیشتری در مذاکرات بعدی مورد بحث قرار خواهد گرفت.
🔴
گزارش شده است که مقامات ایرانی پیشنهاد داده‌اند که شرکت‌های آمریکایی، مانند شرکت‌های نفت و انرژی، اجازه سرمایه‌گذاری در ایران را داشته باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123650" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123649">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اداره عملیات تجارت دریایی بریتانیا (UKMTO) گزارش می‌دهد که سطح تهدید امنیتی دریایی در تنگه هرمز به دلیل محاصره همچنان بسیار بحرانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/123649" target="_blank">📅 13:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123648">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
کریدور جدید ایران–پاکستان به شبکه ترانزیتی چین متصل میشود
🔴
گزارش‌ها حاکی است کریدور تازه‌فعال‌شده میان تهران و اسلام‌آباد که بر پایه توافق حمل‌ونقل جاده‌ای سال ۲۰۰۸ دو کشور شکل گرفته، اکنون شش مسیر زمینی را از بنادر اصلی پاکستان شامل گوادر، کراچی و بندر قاسم به گذرگاه‌های مرزی تفتان و گبد در ایران متصل میکند.
🔴
اهمیت این پروژه در اتصال آن به کریدور اقتصادی چین–پاکستان (CPEC) عنوان شده است. از طریق این مسیر، ایران میتواند به شبکه ترانزیتی حدود ۳ هزار کیلومتری متصل شود که غرب چین را به اقیانوس هند پیوند میدهد.
🔴
همزمان، ایران نیز پروژه راه‌آهن چابهار–زاهدان را با پیشرفت بیش از ۹۰ درصد دنبال میکند. این خط ریلی که قرار است در سال ۲۰۲۶ به بهره‌برداری برسد، بخشی از کریدور شمال–جنوب محسوب میشود و بنادر جنوبی ایران را به روسیه و آسیای مرکزی متصل خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123648" target="_blank">📅 13:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123647">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عملیات انهدام مهمات عمل‌نکرده در سنندج از فردا یکشنبه ۱۰ خرداد به مدت یک هفته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123647" target="_blank">📅 13:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123646">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس: کشتی‌های روسی و چینی از «شرایط ویژه و رفتار مطلوب» برای عبور از تنگه هرمز برخوردار خواهند شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123646" target="_blank">📅 13:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
یک منبع نظامی به الحدث: وضعیت در جنوب لبنان نگران‌کننده است و وضعیت "در حال از کنترل خارج شدن" است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/123645" target="_blank">📅 13:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مسافرت قسطی هم از راه رسید...
🔴
وزارت گردشگری: تا هفتهٔ آینده کارت‌های سفر در اختیار مردم قرار می‌گیرد.
🔴
مردم از طریق این کارت می‌توانند هزینه‌های سفر خود را در درازمدت به‌صورت اقساطی پرداخت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123644" target="_blank">📅 13:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
معاون امنیتی فرمانداری بندرلنگه: به‌دلیل خنثی‌سازی مهمات عمل‌نکردهٔ دشمن تا ساعت ۱۷ امروز، احتمال شنیدن صدای انفجار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123643" target="_blank">📅 12:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123642">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM08AJ4I0_5xqVFPDSFdrTFdvu9ndkoyKeEq3pXaFiDvHrw4829tWIh6oRuLlENkt0Gd5TTTNwaEjw4ijPkMhTg0P5zfaihrjCgaLQ01NBizZ_f-X1LqvXbaz_jtw_JlTDwFcW64hlo605Ym19CjKYIuhdSnV4DH_RhpHTMQV1UBte6xrFPHrREFor-vFTTx_8sM6H_Ur4wcAcORpr3Ca0JHGBYrnUpBz9hDytduuflP2iT5k7O04F-gr_1Nwg2O7vymDT76mkeA9fW51ZWn5znf7YC_7p8v3qwIRoomSVbE9OArwNFVLtSgzY45E8TH5ATSAlGDfU-LC7RYzFhMBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای نیویورک‌تایمز به نقل از مقامات آمریکایی: تندروها در ایران مانع توافق هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123642" target="_blank">📅 12:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123641">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
هاآرتص: تهدید به استفاده از زور نظامی علیه تهران اکنون تأثیر و قدرت کمتری نسبت به گذشته دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123641" target="_blank">📅 12:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123640">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCknAN2PrJU5eWLYynGsl6wRyZ0ye5-7fXdsy2HWvlgNRrSAE4sZk7K-TNzK04ZNBcu0u7yxkwx46LuQ2ao3BJOahbuOJRbkpnTa7p3tunbO2hecqCp3hB-v77T2wKkYds3DRdnz8KCFeePPNkOIt50vsDqe4QHCn8Y5ZEpxPwK2SS9Sf00hQpCiRhnkp6tVUbZ2P_o3bhAR0-WuQtwt5NfKarvaMGrGRCVOtWbUJNBmsGoZg-_mVOa_Akzdodb_tXhpjAxJa_L_5py5ZiiuzSYdBq0O4JA0IZpQ-9E_AKLJ8EiouHJkGTYEeh07Qh6Kmz4moBe_bWIg28rltODUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های ماهواره‌ای نشان ‌می‌دهد یک کشتی فله‌بر ایرانی به‌نام کیوان با عبور از محاصرهٔ دریایی آمریکا به سواحل ایران در نزدیکی بندر امام خمینی رسیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123640" target="_blank">📅 12:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123639">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ULgEqqjGaZfJCdB3ddG4VJY3T_u-KXYeWT_R1-u_dswQsqkIexxjlnVFEz32bVjrcJeMOT18Robki9p2KQ6GSI9IR8rWx_9NEAdpzXYc9WeSAFhHnM75IUGE1nEI8N8ZkyDoN92Y2-XRgm8VmkBlt-9OFY3-8o_Y-uTc7PKJUXAw5kBYIS5nygwVZGldQ32sXLyFutzpLbG-bOfb4LhsPSPQpQyBdMQrTNe9m1GGsq9sbv22GMLNlJ-gfHVUPcWlOlyxF8cbalyfKv68jlTAN5l9gZq6s4SBSm-dRRkLTty_n2ao1K_DoKJGu3ji4IEGT3weQGCTsooP11fMucYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای اولین بار در تاریخ بورس ایران، هیچ سهمی منفی نیست!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123639" target="_blank">📅 12:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123638">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: محاصره دریایی ایران از همین حالا برداشته خواهد شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123638" target="_blank">📅 12:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123637">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
یه مقام آمریکایی به الجریزه : ترامپ هیچ توافقی با ایران رو امضا نمی‌کنه مگر اینکه به نفع آمریکا باشه و خط قرمزهاش رعایت بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123637" target="_blank">📅 12:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123636">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
فیلد مارشال  محسن رضایی: رئیس‌جمهور آمریکا برای بار سوم درحال خیانت به دیپلماسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123636" target="_blank">📅 12:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123635">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: هنوز هیچ چیز نهایی نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123635" target="_blank">📅 12:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123634">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
از امروز محدودیت‌های چک برگشتی و لحاظ شدن بدهی‌های غیرجاری وام‌های زیر ۷۰۰ میلیون تومانی در امتیاز اعتباری، پس از پایان مهلت سه‌ماهه بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123634" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123633">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ارتش : انهدام یک فروند پهپاد «اوربیتر» در منطقه قشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123633" target="_blank">📅 11:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123632">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERULZZbaRpiekOyZr_hrXI7Xs9WW53UhJiJQbRhaaVHtCIHUEvtI-KHJNixadKaDfrqKEHLitydHubVsdj5TSdUu4YK7Uf66OOjhts-kdBleqhOZRdrX71K8LGmM9zxkHQs2rCOMuxV961XNlT4C3NYWQSf1rLMK8J3gX6wJY-qhU8tKdVUULrbcrmJjEhkre0FpG2uINmB1nEBlhB8Rya1oUDUCnj0CFXh6JK47XGJp-Jt4bf4SxnqdfOsKkKN7R6PGDD4BZogWko3si0xquRXFBpBunONQPWln-BpVJgSj87BUMPIlZ2nU5f0YBVUbjwJ9rymMNhOjbGXzQuQidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسین شریعتمداری: ایران باید فورا از طریق یمن تنگه باب‌المندب را ببندد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/123632" target="_blank">📅 11:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123631">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کلش ریپورت: روسیه سفیر خود را از ارمنستان فراخواند و خواستار مشورت شد و همسویی روزافزون ایروان با اتحادیه اروپا را دلیل آن اعلام کرد.
🔴
روسیه تهدید کرد که در صورت ادامه حرکت ارمنستان به سمت غرب، عرضه گاز و نفت بدون تعرفه را قطع خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123631" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123630">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uvur-BL2z1Ome_-JA2huRcS9ZQzS_RGOctZLnJGaXq6F_eQ7K66iGuE9qfFtichht9XAf7oMvR_2KYFNBebHryx_sEeWCwQk7HHUHcpKdVmQTJjcAn7XSLP677UlX0doCsYSxB-x0rVpw8ArHlmTHChck_97kDBSs96S69SqR200VoTBTVsGjvDRv9IK8y8bwwsS_y5bH6yjICaGgAkInZ6FF0mQRpS5PV-9nkZ1N2KQlfCi2UXF2ssLm57bDCeFCc0e4BsbUmDsWy-2u5V7rA1AGwUrKBumKvuTmHHH9tSA7Cv7dpS6VxNIXrBnpyPqFy-Wz2-JOSReAz5pYC0DCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۱۲ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123630" target="_blank">📅 11:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123628">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ut1ZuRahZTmw6UpveiuJgdUKV1__cJeY90RngHjouyLKxevZt6Dx19xNCLuvYfnrPIpDYDwAYvBanepqz_C9sjDOzh2fq7V_9JS6K4tXh7Hz8DqQLO8IEQREAuqF887a0LfP3_bK3bi5HhQA8XFW8plD6i3y2ea3SjjrIzlUXGrzdK5jmCJGV6ShcO2qlY6OI6FOxjc9t1oNsYbouHK7Ia7N3qQdEDKcnEY7uAJGjHrit0FguNKfOVYqVZg3JWJkjtxyEuxZssm-iz4sxscEK1jubijtkd-7z_A8XwvSIyGAF5_gy1CvWUW4g4H6a4_iKoNUXCBqvIXhwRqddxBY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egE3-_S8I3grCnN6nm_aMvokeXCVgKNl7z_6zwb8HuJZMR5MX_5_oMTJpFXpkAnV4BpSpGDbtjCBbgk3OZJ4S6EWe848I3RA5a-NSGC_k_HAmphweAB1nqPZG9XHYCcBU50ncJ7ft24_eCdGDFw9SgHoy-CDRw9UeUUCCXsob8GD9_Xd11kxQ__wa7HY2FTYIVjxl-6y4Pv_CVj0UhNomhhPt1LIqIgdbdEmM7TzwCJ4Kir5uZKFBx_rK_ia2cnaWs_UQGCRJogaQ4PBXbheH4sGYnOn1XpjCeLkwF4cMjgzZ1AE4Sjm2tq5CJH9ub8QWlhLwdwa1zT8nKi4N74tJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به مواضع حزب‌الله در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123628" target="_blank">📅 11:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123627">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB5eYdLoCIPc2ZiVgpZn-Kdhvoh2W8HoH4unSy2nj5V9nzaW1OMsZjwY_RA15hKzlZ2eE1Xs0N5OWFI8j3DG47eYjkoG5LFeKXcNBA4gZqiYEgrLP5LMAA885QxbMZ4RRZSt1GJYQ04hdqiZj8klFuQDjU_C4MxM13jSt4ZQpxuXFGfZfX5PnFLvmmXY4I0PrmEmSOAaQ5_wprl1bJtVop3easOTnr6pwrIfIrCJ6iGg2Le6hq1rchrJRw12ky8KYlwti1ngSKdZL7cPdJVOkjB-ao81B1APiLB4PTMlyi1LH1AOieE2RM4oqLR6fnjKw8cb5NIyXkkZCaEXAERopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: جنگنده اف-۱۵ای آمریکا، ماه گذشته با یک موشک دوش‌پرتاب چینی در ایران سرنگون شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/123627" target="_blank">📅 11:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123626">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRq9HKBnQYZuLgmaC-s_4I8OUIgV2J--2middLtjBanYubyUXY7Hm89EknJsJGLx4HdZiCXYFKeUETugX-QE2eyJQHoEUR-TFv9ViCcGgTMUE7iLXoHeB_FkROHP-GroI0rlpZOtq5pFXwriiui5SOmqrzsI5nDoUsmZNFGADneT0fErGAXTjF8z7M-miM0zL8xP8d1qDXUGKIpJ68zbYkcQfX8D-Kj85IZPpSfiZZuk7b1m_p4vuKN94Aa7NDoMKFyh0S7-NP4kGFWN8lvgeat4E8HG2EVxFw0Feg7tokhW9QYi-hg3l-5NGrOyWnoCJ2TMsEQwi1S54PQyevZeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید آخرین معاینه پزشکی ترامپ را منتشر کرد و اعلام کرد که رئیس‌جمهور ۷۹ ساله در «سلامت عالی» با عملکرد طبیعی ریه و سیستم عصبی قرار دارد، هم‌چنین قلب او ۱۴ سال از سن او جوان تر است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123626" target="_blank">📅 11:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123625">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کنکور سراسری به همراه آزمون پذیرش دانشجومعلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123625" target="_blank">📅 11:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123624">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
مقام ایرانی به الجزیره: هنوز هیچ چیز نهایی نشده است
🔴
او مدعی شد تیم مذاکره‌کننده آمریکا چارچوب حرفه‌ای و اخلاقی مشخصی ندارد و مواضع و خواسته‌های خود را به‌طور مداوم تغییر می‌دهد.
🔴
این اظهارات در حالی مطرح می‌شود که گزارش‌های مختلفی از ادامه مذاکرات، تبادل پیام‌ها و تلاش میانجی‌ها برای کاهش اختلاف‌های باقی‌مانده منتشر شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123624" target="_blank">📅 10:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123623">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
نیویورک پست : آزادسازی منابع ایران مشروط به بازگشایی تنگه هرمز و پاکسازی مین ها است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/123623" target="_blank">📅 10:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نفت برنت بیش از ۹ درصد ریخت و طلا با رشد ۰.۸ درصدی به ۴۵۹۳ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123621" target="_blank">📅 10:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز در جنوب اصفهان، احتمال شنیدن صدای انفجار در این منطقه وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/123620" target="_blank">📅 10:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123618">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f402cf90.mp4?token=mdPjLfFxs4MHhL2kS0P8lNmyQwRpRew_7l8pjRjTxe7Ew8g9BG8LZ0jDa4shUaU_JHIlauFJdIBWyOtWZCz5iXLe9RRUomjOjKcWPFmb3X0EfNKn94h5sGFJuqGppR10UUkX75tZ4dEMAg0NqqfkZjhqYPrDQw0xvrEwA1KlUH_uOwyISPNk3fwiNEq7Au3j9qoJo6tHYBIWgCQReOrn0QbqBqcmN8AUqYFARO7qngiKMTf9U0zGVvJkvUGBWNvaBjyfG4BGYJv8r5Nc8HpCbjK7e0ij7_5MtTzYglfwunH_wt-i0GMGGnO_dIWxzEjKYwsmglit8re5zpo6cHS0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f402cf90.mp4?token=mdPjLfFxs4MHhL2kS0P8lNmyQwRpRew_7l8pjRjTxe7Ew8g9BG8LZ0jDa4shUaU_JHIlauFJdIBWyOtWZCz5iXLe9RRUomjOjKcWPFmb3X0EfNKn94h5sGFJuqGppR10UUkX75tZ4dEMAg0NqqfkZjhqYPrDQw0xvrEwA1KlUH_uOwyISPNk3fwiNEq7Au3j9qoJo6tHYBIWgCQReOrn0QbqBqcmN8AUqYFARO7qngiKMTf9U0zGVvJkvUGBWNvaBjyfG4BGYJv8r5Nc8HpCbjK7e0ij7_5MtTzYglfwunH_wt-i0GMGGnO_dIWxzEjKYwsmglit8re5zpo6cHS0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک راکت حزب‌الله به مرکز کیریات شمونا در منطقه گالیل پان هندل، شمال اسرائیل، لحظاتی پیش اصابت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/123618" target="_blank">📅 10:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123617">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سی‌بی‌اس: انتظار نمی‌رود که ترامپ پیش از تصمیم‌گیری درباره فروش تسلیحات آمریکا به تایوان، با رئیس‌جمهور تایوان، لای چینگ-ته، تماس بگیرد.
🔴
تماس برنامه‌ریزی شده توجه‌ها را جلب کرده بود زیرا هیچ رئیس‌جمهور فعلی آمریکا از سال ۱۹۷۹ به طور مستقیم با رهبر تایوان صحبت نکرده است.
🔴
ترامپ قبلاً گفته بود که قصد دارد پیش از اتخاذ تصمیم درباره بسته تسلیحاتی با لای صحبت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/123617" target="_blank">📅 10:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123616">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8SkFqQkaaPI81iElY4Trn5IuS_WVuOQYFN6v4GPmx2mkUhgaIgS3oe6bGypP0EMvbKjnsj28E-6gMdpplyfhJKfeU1cOdvkk73z9DxZaeO2XHDSsWLS73GkUppL7TcRve7W5O6bx0Viwfp7B2D5RIXxIuQ2hbO6x-gwg92esNcnWdYTncsq3VxLOBJU7rYhJHJ9Iv3xixerF0SN1oC8NrOJ1S8zcwzZte3fA0Wn-i-JyKMWO9GNGJ8fg9cw1bYQlN5XZX9nisUKt4V1hsJBG5xYCzGBw4nIjiESb9O3MEDz4a7O9FtcdFq_pADbr7fPSux9mzo1TlJU7ZUyIAbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل یک وانت را در بزرگراه حبوش - دیر الزهرانی، جنوب لبنان هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/123616" target="_blank">📅 10:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123615">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK39WVVjf3A9Wcn04iDHiokdJUk5uHLocNQpwkACS9inDwHom_cn7c6iWtNJtWp3rGlwA58EAuetS_hs9tcv5Szy1-yY7eZ92-KxPsaJlyU5V2FCulNEPW3PlMlg9VVwc7_4lO1DKLIVcK6LK2xERYh089s4JfkwLQeMd4C0_m26Hi5nizAzCkAZo_hABSOMioTC6zqNO-3Sm_ujUHkhlUJ5vRwgHKq5rHW1XmlTDxgkD5lPgzd9UjHYgjK3Y0t8LKFNu-FBwpApQp4lzmZ-0iB-OZNMf7rSmWC-gMf-wtrtZ4-UT9xFywpWEXHnvQhjgiPGE224g-tMDxnZCKIQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: پنج پرسنل نظامی آمریکایی و پیمانکار پس از آنکه آوار ناشی از موشک بالستیک فاتح-۱۱۰ ایران که رهگیری شده بود، پایگاه هوایی علی الصالح کویت را هدف قرار داد، مجروح شدند. یک پهپاد MQ-9A ریپر نابود شد و دیگری آسیب دید. جراحات تهدیدکننده جان نیستند؛ این حادثه پیش‌تر فاش نشده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123615" target="_blank">📅 10:11 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123614">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/123614" target="_blank">📅 10:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123613">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbkAwx6y61UBYlSsWN9oksp-UrHLyBe7aqXNQ8GZgmTAmyqF_mn4veQqISqW4k8_72DOTZ9ljjqCpTslW0ChHibzHz5RidBsUXicnoUeFSGI0cxdjWaevu2bf0lJgKKL0R1mLnVWn9zL_NMzOVRfqf6uWUBpsLkQN3UVZgCpLtGFWs763wzyHwm_LFDtUiedhHpFGf1ELTJbv5tPOUPo1GfH2Oi7iXKpggxEFYFjRIB8YkaIb1S4w6T27udJhSvBbJtTZ3qF0DsSA5ZifIRlRaj-r9qzjKCOy_ggV0LmK1SZKadFxljPKNZjrALhiMf6ByCfVgb4SkUtNO0f99nJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای وال استریت ژورنال: موج کوچکی از کشتی‌ها در تاریکی مطلق در حال عبور از تنگه هرمز هستند و بدون چراغ یا سیستم‌های ناوبری خودکار و با کمک ارتش ایالات متحده، از این آبراه خطرناک عبور می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123613" target="_blank">📅 10:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123612">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ابراهیم عزیزی رئیس کمیسیون امنیت ملی مجلس ایران در گفتگو با ریانووستی: ایران همواره برای شرکای خود احترام ویژه‌ای قائل بوده‎ و خواهد بود.
🔴
روسیه و چین به عنوان شرکای راهبردی ایران در موضوع تردد شناورهایشان در تنگه هرمز مورد اقدام مثبت بوده و خواهند بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/123612" target="_blank">📅 10:04 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123611">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
پزشک ترامپ: «دست دادن مکرر»، علت کبودی دست‌های رئیس‌جمهور آمریکا است
🔴
این یک اثر شایع و خوش‌خیم است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123611" target="_blank">📅 09:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYqBnTrbowObkldddFrzFrBkqGlwARlD91RtCD9Bus-2RCY38Uzrhe5oE5le3Li0PlcBxf7HF9kAKyI4qbyQAHZQmjONsaFajZt-4R0IhDhGFJ901DzusatiVf8Q38J-pg8d9UAYulss1FT-48GH4paXBMJTuQX1yVCzCjd4bSjLp5oOZsIU1Bij1awZRFdVJ7NkJjRypdi7H9DJxBT2fUgjJHVVYbnKqdEOKF6uOEMO8NjT3wKUvTynK5CZvvyqIPir3lGzKJIX-85tQQyhxenNoC_DldDm38j7Q9xsAzbiUmJJxRYi6Kgn8Qb0tkBfh1EmG9VGEjrM_Cw5SjNVtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توجه‌ها به شبه‌جزیره مسندم؛ نزدیک محل عملیات نیروی دریایی آمریکا
🔴
گزارش‌ها و تصاویر منتشرشده توجه‌ها را به منطقه شبه‌جزیره مسندم در عمان جلب کرده‌اند؛ منطقه‌ای که در نزدیکی محل برخی عملیات‌های اخیر نیروی دریایی آمریکا قرار دارد.
شبه‌جزیره مسندم به دلیل موقعیت راهبردی خود در نزدیکی تنگه هرمز، یکی از مهم‌ترین نقاط ژئوپلیتیکی منطقه محسوب میشود و تحرکات نظامی در اطراف آن همواره مورد توجه رسانه‌ها و تحلیلگران قرار میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123610" target="_blank">📅 09:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t71FlFG5CK7W9zcZbHc-dK4i0cBh4opiCpuDwvtxcPck9UbXRimZv-pyNrENX_4mEBzd6A1Fhdki-K5c5CTRgTcxgdQBJoReheZE9rpAO0bNm-8eGbRl5_wkQnhLc9fCL3lK6YIrfMm2gM_B2SqN96RlwRA3bpmZiepBqhpR22A0HC-RQkibKjHKY5bfVTOSY5dx6zfaA1XFBu17T1PiPrXoEKlFr81iZDwekA4AQkpp5g3k9yNg3M4PuWkvlJ3fHR2Kqpcp34j6tpOdukFOB79ouwAXCp50c5aBrCjnDBiqXBgsyryx6iZb6lYfAbxUg1nPRGMOrfV4_JAuEmRw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sRMJp48Osaho0LijCQMiSTZZJ40oQAJDo0YlgoHh__RxClNXw_g4Id5VaQZJ6zg5lE-qy-7QgUDLrMfhbkHEWwMV0RL30iT4yfkRlh81VpuUdk4bIYtoO_3k1-5K0fG7HdEdxzDg2l7rCWKgsHfoj4p9QNpPOW90tp-lzjT9t10JgJZv7HB1qdS_n00fGOBQDPWPbiEh_1fx9Bww1KLv6LgBTCDEX0a1ziU5KnxtwcKLj6h2jEPtrZukxZRnPLUjUYKsbIkDONIf2GPpU5XaNoR6O7ekz7qgSoXHXyrdRE08Y3VI1Cs3G9Dgpxlj5fycBzu-j1og6Msxpnlo_wnBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروی دریایی آمریکا: کشتی‌های تجاری از تنگه هرمز دوری کنند
🔴
فرماندهی مرکزی نیروی دریایی ایالات متحده (USNAVCENT) روز گذشته با انتشار یک بیانیه فوری دریایی، به مالکان کشتی، بهره‌برداران و دریانوردان نسبت به آنچه «عملیات نظامی خطرناک در جریان» در تنگه هرمز خوانده شده، هشدار داد.
🔴
در این بیانیه ادعا شده که ایران در تلاش برای «کنترل غیرقانونی» این آبراه استراتژیک از طریق آنچه «مین‌ریزی خطرناک و غیرقانونی» خوانده شده، است؛ اقدامی که به گفته سنتکام، کشتی‌ها و خدمه آن‌ها را در معرض خطر قرار داده است.
🔴
بر اساس این بیانیه، به تمامی دریانوردان توصیه شده است که از «طرح تفکیک تردد» در تنگه هرمز اجتناب کرده و در عوض، عبور خود را با «مرکز همکاری و راهنمایی نیروی دریایی ایالات متحده برای کشتیرانی» هماهنگ کنند.
🔴
در بخش پایانی این بیانیه، هشداری قاطع مطرح شده است مبنی بر اینکه هر شناوری که در حال انجام فعالیت‌های مین‌ریزی یا پشتیبانی از آن مشاهده شود، در چارچوب آنچه «دفاع مشروع» خوانده شده، از سوی نیروهای آمریکایی هدف قرار خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/123608" target="_blank">📅 09:46 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: نگرانی به حقی در مورد تقویت تاریخی ارتش چین و گسترش فعالیت‌های نظامی آن در منطقه وجود دارد
🔴
یک شبکه قوی‌تر و خوداتکاءتر از متحدان آسیایی برای حفظ تعادل قدرت، ضروری است
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/123607" target="_blank">📅 09:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123606">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
بلومبرگ
:
چین خبرنگار نیویورک تایمز را به دلیل مصاحبه با رئیس جمهور تایوان اخراج کرد
🔴
چین در حالی که پکن کمپین خود را برای منزوی کردن تایوان در عرصه جهانی تشدید می‌کند، یک روزنامه‌نگار نیویورک تایمز را به دلیل مصاحبه‌ای که این روزنامه آمریکایی با رئیس جمهور تایوان انجام داده بود، از این کشور اخراج کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123606" target="_blank">📅 09:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123605">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: نگرانی به حقی در مورد تقویت تاریخی ارتش چین و گسترش فعالیت‌های نظامی آن در منطقه وجود دارد
🔴
یک شبکه قوی‌تر و خوداتکاءتر از متحدان آسیایی برای حفظ تعادل قدرت، ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/123605" target="_blank">📅 09:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سی‌ان‌ان: اسرائیلی‌ها می‌گویند ترامپ در جنگ با ایران، ما را زیر اتوبوس انداخته
🔴
نتانیاهو، کوشنر و ویتکاف را به خاطر هدایت رئیس‌جمهور آمریکا به سمت پایان دادن به درگیری‌ها، سرزنش می‌کند
🔴
اسرائیلی‌ها درک نمی‌کردند که جنگ می‌تواند به تغییر رژیم در واشنگتن منجر شود
🔴
شاید نتیجه این درگیری، روایت سیاسی نتانیاهو را پیش از انتخابات پیش رو، پیچیده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/123604" target="_blank">📅 09:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-123603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رکوردشکنی گرما در مازندران؛ دمای دشت ناز به ۴۷ درجه رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/123603" target="_blank">📅 08:59 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
