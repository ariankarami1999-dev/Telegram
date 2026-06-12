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
<img src="https://cdn4.telesco.pe/file/pzGnC89cWHWwgTakiB4-wYMV4MyEG5q8n517ACjJFe8O_y54u4s-Lv2UGk_ADIvsibavbNG2EdUiWb0-0Zd1dA1eSfDWYioGeDqKSi98Xukxr6zrOQA8Q8EnJDc8_I4mj1iUHVgMOrpTkmMGxwel5cEihli0FDNhhuRw3eAeq1aEG-r_SHBX6vMJ7tKWh8SoI3I1BlBM0ShmqhfiX71uSsRpX-eOZF7AtVDjIrcmNHg6mC6N7J5xhg6kHTDmzQ_nchD3aJ3TtkTaksHSjRxKu-5vMY6_D0dcq3h5zqVLUkD0PUZmKKmsmCvH70T6XP--ky0-_gjoj5nb3_rD9t4yyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 17:28:34</div>
<hr>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=XWacPQYgIJBBwGem_7XIWsaVyxBJwVmSZIClwSbViI6F3AC_DhTojFwTHxdA_R-J098zwhxzt6ymuiyfESX0qYPpqn2kuVh7tsZx45je_dmWm2CZp3aNe3mHOA-Wx0mbs_HndA0epk7ITdVpsotoJV6O1oF4KDLazQ7YEuhWu1fBLizdwKsdRV0fgXmfiPDrutLkCqaSHrlUL0t44gMUF1tOXLOXo3o3tvd-N3QJsLwgnXdPnPr8kY6tt50iMX217km6x0SWRKv2hgMbJmf5FzhH-rZB8NuHj34lGHFnWdnCaGKSaODxSiNF2vj23QEpxTLM1EsA7e-J0RNhFsfH0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ یهو ریج بیت مودش فعال شد گرفت رو مذاکرات و رسانه‌های ایرانی:
شرایطی که ایران به اخبار جعلی فاش کرده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده بود ندارد.
آنچه گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره داشتن یک توافق، هیچ ربطی به حقیقت ندارد.
افرادی بسیار بی‌شرف برای معامله کردن.
با آنها، چیزی به نام معامله با حسن نیت وجود ندارد.
شگفت‌انگیز! همچنین، حمله پهپادی کاملاً دفع شده آنها دیشب علیه کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
بهتر است هر چه سریع‌تر خودشان را جمع و جور کنند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/funhiphop/77717" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PeDRJIGSC4Vf8jMD2v2MpydKvGZAc2H9T9oAQS51xnEmQpLPJKTpVbiWnSW7r6MUB5tExajKJVQCkXIku6v49zTiMPZz8brRZBCOuK4u0J65qZUIbSBEZMNG4miMpd_hJZ84vypva3xEdxqAoXwFQQwF2zCAvvgz7CacMewmBHq7n7r2tTmmKfDF0aOB9qvKvPh-MeMyS5y7X9T9HpVlfCfMqB3Tzhu_uMuWjaiwybdKzMClYdzY5ChgJ7cWA1hd-y5Q_5a7bvFZVJHqwWhaOqdyvq2k3cuIvAZU0_cxmYv4lh2U-X5r6-NgUPk_swtpNn7zJbNnpsmAB1vbo0-vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ارباب سعی میکنیم درست بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/77716" target="_blank">📅 16:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/77714" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من تازه فهمیدم چرا علیرضا منصوریان کچل بود، خواهراش کنده بودنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/77713" target="_blank">📅 15:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrD1mehQK486aw7woypXQWNoo1q6XNm7oXicsstdu0WTud0BGve033zjA15W-GFZwDhH7nENx9y3sS9k9kCvP600pBDHpYjkrotUuWbXTe5eHOKtkbaCkTE1IThwhk_I8ivtagqnIw1tkwIvWW8cv0sAQeAQdghsGupU05OaHGHTDqmz_WA7r62uYj_Pyp5LzVjxzHALyPgTgRCPwo6GwFS4il9XHDeWwv75OCsGc77S3ABS32SHv_tbcZFHjt8zY2xEtNnKmT8xFVSd_4OVZ03-upChKzTZXJ6uoV6TkFNqyiVPARkeoi0vAjJqTuk9daMp3ryf7TnO8gKfeGSGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/funhiphop/77712" target="_blank">📅 15:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=tQUDXRVGQivrfeR-ywMullHUJimyb1z7Kh1yeXLy0NLXaSYvRqqkR98m8dLLQgd67oKGK_7KTimsjTWMXglJqL7gm7NEcrOIocQqTJP_8GKAJuVaiEfc1GXOBpLcmajmm2VTzOO-maF096M47Uuds78W0vWFx45cBZxvKMp318B4enBlDMTEOQ4SRbCbi5uLxQ6_h_S00qeGaykQ5O98klGyEqqy4GgbaDcWckBAMxGTU_mHrxZxL2sOB6mHFXPsko9y73Xnv2sSvPZtt0SQL42HU8anyouOzIrJoqoopuMtZkspY7HopIGSwC23LCcjj5R4jFWEFDgVCWsuEwcAWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=tQUDXRVGQivrfeR-ywMullHUJimyb1z7Kh1yeXLy0NLXaSYvRqqkR98m8dLLQgd67oKGK_7KTimsjTWMXglJqL7gm7NEcrOIocQqTJP_8GKAJuVaiEfc1GXOBpLcmajmm2VTzOO-maF096M47Uuds78W0vWFx45cBZxvKMp318B4enBlDMTEOQ4SRbCbi5uLxQ6_h_S00qeGaykQ5O98klGyEqqy4GgbaDcWckBAMxGTU_mHrxZxL2sOB6mHFXPsko9y73Xnv2sSvPZtt0SQL42HU8anyouOzIrJoqoopuMtZkspY7HopIGSwC23LCcjj5R4jFWEFDgVCWsuEwcAWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توهین بسیار زشت صهیونیست‌ها به رهبر معظم انقلاب.
🔹
صهیونیست‌های ساکن سرزمین‌های اشغالی که فهمیده‌اند کار جز کودک‌کشی بلد نیستند، اینبار در اقدامی توهین‌آمیز یک مقوا با سیمای زیبای آیت الله سید مجتبی خامنه‌ای به همراه رنگ‌های مختلف را در رژه روز همجنس‌گرایان نمایش دادند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/funhiphop/77711" target="_blank">📅 15:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEf_R2xfFXHH4qgITV7WSigJqlD9ot3FTGZIDqm9tOqa8vwDWqkm8PVjnIxBbiEsFgAaGK1w8AHvDD7GEwCiyeWSy7cjBfKZE1Ka_SRP9lWTHLXHAWcRd_nKKPlLNUPhfOzmPSj57uuJ4MBxwahF-RhajSWdJMvOhoE8rrDnOtCBas-Wu0b2gQG-puYCioPqW6ldGgVyQzlxXIQUR5WhvCFthQ4B-SaRWJbsYtmvWoKkxgRVs_C5g0pfgRol7GoaaeyJ52cp84E9gLtIUiq3DLm-zDUz349kJgkVCErpZRomgYZvSWUXoOROZhohUM33mQDN9LiE0FCzJIAnnwCzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رشید_مظاهری
را فراموش نکنیم
رشید مظاهری دروازه‌بان سابق استقلال و تیم ملی پس از حمایت از مردم بازداشت شده و ازش هنوز هم خبری نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/77709" target="_blank">📅 14:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBW9ijgjTUicSpMQEw95ynPPTJXC8g0cp3cUIjxEAFlPzdfrRSOqkkexjCjEAnLcDjQhNshIk7NO9vkLHywwZrD_ng0oiy2ytfQOHc4ZJFh_cSUfL2iT_SkF-Eui5w7Y1ZgNu3veVYx03OaKTSALw9x2U7j1aC0twscPsND1MdZeBdsX54ovfForvpZwMxBgqkhRjCjqpX1-ZZAKAVukJId7w0oPz_0hHtPA4ZWjad13Veyn_fDfgP6DiKEF5K0Yo9XIcMPkjAowUQf3a_ifhHyG-i0WkC3KiO7wG4xt73CVbZofR7xt3UYab0lwgeP_ikpIt9gUxm-J4oNg3RWlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77708" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojCVAsb8VY-J8aIwG_cqOF_DjZ4zYYyjcytDc6xB9q3ryCZ6cD3BH4PyExqJqkqscZUNDXCPz02YDyK8ppQnjx9w9vSlxoM6Jr76mgSV0zXVXsqGN6VbhHzErjCzxPwmM-wtZXz6OuV43E9Ywx9HCGPw01afTlnXvypk8TeBtQ33BFJ_QQ9wgkL8fQXLlqJA-yF2vQuChLuvtYiQhXpOIsXpgUAdeCL94fzHfIUcHhUbp1xS43mEJzwLp_XzRUFKCoHv26uW8JqXnijAW0Cpdhug6X38p5zZ1y3w1vbPlrsJ2ZEzC0uR0LLXF--oA2YBuIvfwQlrvkymXgexdWJ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیسو
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77707" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد: ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77699" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد:
ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی که منجر به لغو حملات آمریکا به ایران شد.
تنگه هرمز پس از امضا به طور کامل بدون محدودیت یا عوارض باز خواهد شد.
هر دو طرف متعهد می‌شوند که در این ۶۰ روز علیه یکدیگر یا هر کشور منطقه‌ای دیگر اقدام نظامی نکنند.
این پیشرفت در مذاکرات پس از تمایل آمریکا به آزادسازی ۱۲ تا ۱۵ میلیارد دلار تحت نظارت قطر
برای خرید وسایل بشردوستانه
ناشی شده است.
یک مقام ارشد آمریکایی گفت هدف استراتژیک تغییر رژیم «فعلاً» کنار گذاشته نشده است.
انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.
بند آتش‌بس لبنان همچنان باز است: آمریکا مایل است به اسرائیل اجازه دهد به تهدیدات نوظهور پاسخ دهد، در حالی که ایران خواستار آتش‌بس کامل است.
مذاکرات آینده ظرف دو هفته (مطالبه آمریکا) یا ۶۰ روز (مطالبه ایران) به محدودیت‌های موشکی، حمایت ایران از نیابتی‌ها، خروج آمریکا از خلیج و تضمین‌های بین‌المللی خواهد پرداخت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77698" target="_blank">📅 13:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فوری
پیت هگست 44 تا پرس سینه رفت و ویدیو شو منتشر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77697" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اسرائیل بمباران جنوب لبنانو از سر گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77696" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYNr52KS1rjtk6mc6sfJgQF-XH-tO0KOYNKve0D3YQ3iNVkepVJPoWbiLMm2DusBpU8Rl4w2MAIvAPXyBxVpLVzFoezQ_iU4YSKbNGwvU6EPWEA81DgKWXhwFs082oPhr_DK4Ss4ziDJUIYbzcXaC0ASHUPyngax7EqQYIeSmIm2pfuCZcZ-JdJZPXhdPKQut_3x2KX_7uGbUIcpXGaAW5j_hFYrroNXQaYGfXNvdRLwdQu3HWo3VhDFoQBpOK7N2qznAkADrdPA56TeUJlncE4AwxWTPrTaUVw3crrtwQYKuhFz7sZxhL5qZyAl330pH-YbZIXgEP78UJ9_PCYj3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش اسلامی سال 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77695" target="_blank">📅 12:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77694" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzjrJM7kIDdZkEcv_jEo6S1NUSdR9AgcBWXzpI345tJ-X22xCikCLv2vBi9dnlQ3vLhUSY2UCIqsl64obL48zMooO6x-XmsP_SdEtyoS1TBXx-5uOUYU9vffJCnNXoqMniNA9yzVWpOdbWibPvwpyHWnSffUEAy8gCzofNextaDXdpYxfqSvBEN6owCND2bYvA5luZMfptmraNviDgLJg1E_k305tUit7NrP1Xt2Q77qWBg2IAShHc66IuLm5bLjD6Lr4HnutSu5QkQRB3vBM6mi4glYNwxfNeJ8h3re33UMftFGkIyXiXjBiFbzdlJUGITsVoApnRVf64apT3R1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77693" target="_blank">📅 12:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77691">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfHchuibUaMoYi_WjebWBItH1G9qFXty2OVsnIy3mF4pmEOTLX48818_4PDFNw4v7wjPM8AGq7mclviRILVpMS7JfJc0g5Y5fO5wMHwoGSRI5owWuvMex6bB8ZPJXSwaC_BgG8JwDPlIvltXyRxXigjq2upgCALSq_DAdTUDvvQUmjLXHN5B8WED73dj5FckgJCbbEJsO74wYZF00eCr3aMtXlJBf0X-vJG8BF-ki20a2JB9GK8TD4rA0x9cyaaf9R7ahl6g9x0-YBG8iw89BWhZncSEh1Trj1OaMVzkkcQuryQB--wQAfyRppNC7A2om-8-PaQLXm0Po2kI-AeWeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهران منصوریان ساعت 11:08 صبح رو بهت بخیر میگن.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77691" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77690">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VI37lA54W2--nKfOSwV1bIZAv3yF5xluy4UCjeG2uRAygc2-euDxGoJLxsqISS2TBj_ME8XzqHAXEs0fyGSohIr6xiiO9sOuFJ2RLPH3THa6evtb1VC90yMowh3tPCuTtv0tRrVlVxan0bsbszZ45JtdKxA0TIzg1_8qaL28F39wbjcsTDjAfah6K9aLGhw3PPHlETP1bghYn7P76B-5HE73UkD3sG68_elgNLZFIf5gp-sTB5--lQ_lSIH1vTwpcVqc0RZXauO5T_ty10uUZA8QF5OhrmosR4zRZS_fgDRzdVIvF5aJF4qLF3furch63bUQV6WGGTXDqPUkZ1ODIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاحیه جام‌جهانی
❌
فیلم سوپر BBC
✅
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77690" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77689">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77689" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77689" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77688">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxbhcZzaHw6tzTkspw6yoMw9RTya--yqUcdgXlcIMTg8BaNUfCOEBeGuJy7a2ilQgS96kkNEjKo_JniqXp1BUeP_nKHGMycRSDg7I2lrNCFjToVdnzScRM0Wd2Quy6MgsiRYjZY9gV5ouRJ8nvUXFMzH_K7G7o1rdbPUnhCLbrQBfmDAelyu3WWnXPPX9GJHahOEo9eabnXh7UHvRDHbrXaVq3hr-0rKP3VSKkadoDfARU8Dr8RsfMy5VQ-W5xQOeF9gbdRg-ZghcvXXhYrFOniArEVYHANHtSP4ANaccpggeTyMxt2VekMXsEXq73G9-sQfbLiVabUvdjiwwMOShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r22
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77688" target="_blank">📅 11:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77687">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شاهکار جدید جواد خیابانی:
خلیج فارس خاک ماست
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77687" target="_blank">📅 10:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=R1OguoUZM3bZCHf317jZdiaXvsO1oTDxcXSzslUcl5e8yl_xdi8daMcnDnZJDu3qKy74h_b3xsi6cmUO_kgypPmGrQQV9Qv8d94MvzmHcAld6tpqMoT6HHBpCTlnAxJfodXBSExB8mfBkYUSJpt4SCJxxav2vVBkyFsZO-ZsDoGvCpSDZ0-cOAfT7pVPt8tVFy-d-kFEpXACQxKunEj63qUtoQGKWErkB-tcd5D6KsjP0RMZLVAyy61ZsJVJusfBadhPXKFL24RAhPx1_ccbZCe4LtVNW2CwWGJSILBhhJYGUKWDg4KJhp15FWlRD54maOC6OAuxChMpuq9wGuGFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcee0eb614.mp4?token=R1OguoUZM3bZCHf317jZdiaXvsO1oTDxcXSzslUcl5e8yl_xdi8daMcnDnZJDu3qKy74h_b3xsi6cmUO_kgypPmGrQQV9Qv8d94MvzmHcAld6tpqMoT6HHBpCTlnAxJfodXBSExB8mfBkYUSJpt4SCJxxav2vVBkyFsZO-ZsDoGvCpSDZ0-cOAfT7pVPt8tVFy-d-kFEpXACQxKunEj63qUtoQGKWErkB-tcd5D6KsjP0RMZLVAyy61ZsJVJusfBadhPXKFL24RAhPx1_ccbZCe4LtVNW2CwWGJSILBhhJYGUKWDg4KJhp15FWlRD54maOC6OAuxChMpuq9wGuGFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77686" target="_blank">📅 09:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=f6AnBKxX-j8AB7EDZojnQVYFvqHzJPEVffj19FoLfUbuDHnfST5Js2oytksWkO1uMDdHjswOUeLVHa_9QQjEyaFqDNM8hLeWICb76IDGxufQ5lx8e4ic-nCpXHg8KuxXzWrp5RdP04Alp8Feq4Ml1oDEx_93q_E6Vm_8ZuLuWEBDsmNo4jRzSEQ7oPO4s0mamy8W6WMudzmacNrWIqmylbOg6-sBHdjol1uRXNnULPherdy0yM6lwjGx9KWcDzc2WiHhzMgHLPdM7J0YvRaH79C9CizTgbY4UM-M70KrWJRIQ7a3HJwsKzOjr5bMJbUluYJCO6f639t1UD94t55TZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b774ac8b5.mp4?token=f6AnBKxX-j8AB7EDZojnQVYFvqHzJPEVffj19FoLfUbuDHnfST5Js2oytksWkO1uMDdHjswOUeLVHa_9QQjEyaFqDNM8hLeWICb76IDGxufQ5lx8e4ic-nCpXHg8KuxXzWrp5RdP04Alp8Feq4Ml1oDEx_93q_E6Vm_8ZuLuWEBDsmNo4jRzSEQ7oPO4s0mamy8W6WMudzmacNrWIqmylbOg6-sBHdjol1uRXNnULPherdy0yM6lwjGx9KWcDzc2WiHhzMgHLPdM7J0YvRaH79C9CizTgbY4UM-M70KrWJRIQ7a3HJwsKzOjr5bMJbUluYJCO6f639t1UD94t55TZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه بنده خدایی هم به توافق اوباما که بدون ریختن یک کیلو بمب، حدود ۱۰ هزار کیلوگرم اورانیوم رو از بین برد می‌گه شکست مفتضحانه ولی خیلی جدی معتقده ریختن چند هزار تن بمب و بگا دادن کل اقتصاد جهانی یه پیروزی تمام عیار بود چون بعدش ایران قبول کرده بهش قول بده که سلاح هسته‌ای نداشته باشه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77685" target="_blank">📅 07:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrPU9VyT0U7GI94a7685QUHNF3n18UJIIJNL5zheb3jw3HYADZI6EWiNpGfTRzRB5jar6-86ozA2RmH1ZEYPhY1hQ8FL5WG33HZ0Jfmjf26YBnPD-fyFjGzLJWYFKRNb7y-pyT5MeTOjeQfWi8y8IQmpaMuOJIWkh2BCUwaGuKI-JAdXuyPDf8-A7o69FEIcGQw6ooE1E6Mtez5q3vw7lczSp-xENdJXJOXzQgfI7sqorjQmhkmy-H4NClThfVkipO8UVmoeRazn4bAKhmrI51GiW31MH_MAffs3MyydZt-EyRmHpi7GNw2UT0oJXtCCJp_Vf8itIBWe6I7RUSA4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمنا می‌کنم هر کجای این کشور نابغه پرور که هستید همین الان متوقف شید و سعی کنید یه مدت تحلیل و تفکر و کلا اینجور چیزا رو بذارید کنار ممنون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77684" target="_blank">📅 04:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یه کودن زاده‌ای هم نیم ساعت پیش اینارو گفته بود ولی از شدت کصشعر دلم نیومده بود بذارم:
ما امروز جنگ با ایران را به پایان رساندیم و آنها موافقت کردند که هرگز سلاح هسته‌ای نداشته باشند، چیزی که ما بر آن تأکید داشتیم. این هدف اصلی بود.
این ۹۵٪ از هدف ما بود. و، آنها این کار را به قدرتمندترین شکل ممکن انجام داده‌اند.
ما، آه، با ایران توافق کردیم.
معامله بزرگی انجام دادیم. هیچ سلاح هسته‌ای وجود نخواهد داشت.
اه، نیروهای ما خیلی زود شروع به بازگشت خواهند کرد.
تقریباً، اه، تقریباً کامل شده است.
ما هر چیزی که می‌خواستیم را گرفتیم. نکته بزرگ این است که هیچ سلاح هسته‌ای در ایران وجود نخواهد داشت.
آنها بندی داشتند که توسعه نخواهند داد. من گفتم، «خرید چطور؟» آنها گفتند، «خب، ما آن را پوشش ندادیم.» پس دو روز بعد آنها با آن هم موافقت کردند.
ما هر چیزی که می‌خواستیم را گرفتیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77683" target="_blank">📅 03:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عرازشه ای که میگید آمریکا نباید فوتبال و سیاست رو باهم قاطی کنه پس میشه بگید دقیقا سردار آزمون چرا دعوت نشد؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77682" target="_blank">📅 02:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvfoyzgtK6cYldmsBbA7RtJB4SwcIuaETDbIiAvDsk7mP4l-Gy4QkVww6ayLxNWAOXCpoC7oSUFcTlRQ2ilao3NyLW_Su8g0s5VvJJ08ZGGVwefShfJGsVWLbdAQuefBY3EA-KCAYCK_jQGezVH0Mcy49_-UNN98fh6hQzWFAsd9msaR2DyQkrvQFOxSOOGdtMIuiaha2mjpqI3JvkIkfwfX1enelhHUchvj83R13pghQmkXk0Fy5oXpx--bc9IgxNKAKuCQu-7wLZH6OdQFYZJmLebZxrouBnlCsWRJctT6cGI5SaRa5_GZ0th7KMsXSAS2oNMAJWZJyAIdkjDEzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست ترور بیکینی باتم اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/77681" target="_blank">📅 01:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">میناب انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77680" target="_blank">📅 01:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77679">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تسنیم: متن تفاهم تا این لحظه در مراجع ذی‌صلاح  ایران به تایید نهایی نرسیده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77679" target="_blank">📅 01:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77678">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چه علاقه‌ای به گوز داری مشتی</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77678" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77677">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازم گوز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77677" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77676">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77676" target="_blank">📅 01:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77675">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asLXtMthjpwc0c_zxieGZlAKyPrZRzu0JXCjwoPAQ3jp9csHS3TxSQJTmr5jLsPBZTp_pq91joR6AfN5ZH54h_kzoUvXuQYnPfNjYQDk875_-8C7ux_qoXcp_zGC8RXgUxHG7C66p0jSihvMPoIcUzqXyc9FAXWi7SOvxmvJtZflHtlqQMRRC6Rc13IyO6S8zcsnsO3yiR_mQhTfajNIgDsdJl6Fyl1RRboxpr0Q57gVoGqJhwKVmOk6PsuY0S7cI1VioHAH3WkPEmLfNHwCm8jDEeKDJLDMhWVioqE8KFfZjSsRf8P-zOJcBf4zNx_PqU4CsMIDRI5dKIMwV5pqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه اواکس هم داره فعالیت میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77675" target="_blank">📅 01:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77674">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پرواز سنگین جنگنده های آمریکایی برفراز عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77674" target="_blank">📅 00:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77673">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گناوه صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77673" target="_blank">📅 00:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77672">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درگیری ارتش امریکا و سپاه در خلیج فارس
تایید نشده هنوز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77672" target="_blank">📅 00:56 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام فریب جان هم اکنون صدای توافق از خونه همسایه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77671" target="_blank">📅 00:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77670" target="_blank">📅 00:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام فریب صدای 2تا گوز قوی از سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77669" target="_blank">📅 00:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77668">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خبرنگار: آیا رژیم ایران عوض شده؟
دالگخیز: بله، نه یک بار بلکه دو بار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77668" target="_blank">📅 00:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77667">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">3 تا توافق رسان KC-135R هم از اروپا دارن میان خاورمیانه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77667" target="_blank">📅 00:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77666">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسانه های مختلف خبر توافقو میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77666" target="_blank">📅 00:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77665">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الان یعنی با قاتل
حضرت سید علی خامنه‌ای
💔
، قاتل خانواده‌ی رهبر جدیدمون
💔
قاتل سردار سلیمانی
💔
، قاتل سید مقاومت حسن نصرالله
💔
، قاتل شهید فقید اسماعیل هنیه
💔
، قاتل دانشمندمون محسن فخری‌زاده
💔
، قاتل سردار حسین سلامی
💔
، قاتل سردار محمد باقری غلامعلی رشید
💔
، قاتل سردار موشکیمون امیرعلی حاجی‌زاده
💔
، قاتل شهید فریدون عباسی
💔
، قاتل شهیپ محمدمهدی طهرانچی
💔
، قاتل سرلشکر شهید احمدرضا ذوالفقاری
💔
، قاتل سید امیرحسین فقهی
💔
، قاتل شهید اکبر مطلبی‌زاده
💔
، قاتل سردار سرافراز عزیزمون علی شمخانی
💔
، قاتل فرمانده بی‌بدیلمون محمد پاکپور
💔
، قاتل سرلشکر عبدالرحیم موسوی
💔
، قاتل سرتیپ عزیز نصیری‌زاده
💔
، قاتل عزیز اطلاعاتیمون اسماعیل خطیب
💔
، قاتل شهیدان غلامرضا سلیمانی
💔
و مجید خادمی
💔
، قاتل سردار سرافرازی که بر بستن تنگه اصرار داشت یعنی شهید علیرضا تنگسیری
💔
، قاتل رئیس جمهور آینده شهید بزرگوار علی لاریجانی
💔
، و قاتل شهیدان دیگر مانند محمد کاظمی
💔
، حسن محقق
💔
، داوود شیخیان
💔
، محمدباقر طاهرپور
💔
، بهنام رضایی
💔
، اسماعیل احمدی
💔
، علی‌محمد نائینی
💔
، مهدی رستمی شمستان
💔
، سعید برجی
💔
و منصور صفارپور
💔
توافق کردن؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77665" target="_blank">📅 00:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77663" target="_blank">📅 23:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77662">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
فقط برای مدت محدود
💢
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۴ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
---
📦
20 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۴۹ تومن
📦
30 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۷۲ تومن
📦
50 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۹۹ تومن
📦
100 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۱۶۹ تومن
📦
150 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۳۹ تومن
📦
200 گیگ | ۳۰ روزه | بدون محدودیت کاربر --->
❗
فقط ۲۹۹ تومن
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77662" target="_blank">📅 23:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77661">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvzTrinj1cKhMXS69P41LPtTj61n9mCbsBrm11iqVTn_0xPFRXKiDgyHy7jlWE1WhKUQdiPXU172TWXngR4UIbl8CWkKYGxp-lFcafoXc-tIiqhexTcp9kfvO3_O3ywN6KVNvVMta0PusD2Xbx0g3rfNektCfeLGeKRoOFbmmF7xoEG7JcslG8ruYEi2kQDuytQgmgqJUS-mxE1VhyFCa5EMV_cq2qKCL865kIkWjXPiRjaeAa6F2-_svoF1toC7rOz7PARBnjk5I4LywLsPz3d-2I6OppElc-jUNjJuiq4tvwTiWlCLPLkfjbKHqoDPWic4dJWLIQM3kCW3CjTjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77661" target="_blank">📅 23:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77660">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">انشالله بازی کشور کوردستان با مکزیک
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77660" target="_blank">📅 23:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77659">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromcина</strong></div>
<div class="tg-text">این برای امشبه؟؟؟؟؟</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77659" target="_blank">📅 22:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77658">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=SqC-i4lOdtN-TTAg9p5XDMZrlagK4CruAVfJvBxd0cgDwbbq6eyT0p21nYTWfoFwXPlKALBvshqzmQLOeIM66M7g7lO9-bLn_0oeakD2CBedQiO-aYlq4c_XVBfCbVI3lFzXGObD9Ed_f0svL2KDCZ5aOR5MeZggo8j3cGTysIXCiVfYfaO6nPiXrfo2p__Xy14Ix-Vac4zISto0Sjsqpkgbtud1kX_1pdn8z8hcoULfyWPiokGlt9PEW9xuJA4obestBJRhkaOOtaif6XsK9ZOxddEAFzmCP67G-AIEsGZlPl4xb6K0ymySqmqzY0f8ZRGOW0Y3tg9S2kkCdy2dnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ed6deedd.mp4?token=SqC-i4lOdtN-TTAg9p5XDMZrlagK4CruAVfJvBxd0cgDwbbq6eyT0p21nYTWfoFwXPlKALBvshqzmQLOeIM66M7g7lO9-bLn_0oeakD2CBedQiO-aYlq4c_XVBfCbVI3lFzXGObD9Ed_f0svL2KDCZ5aOR5MeZggo8j3cGTysIXCiVfYfaO6nPiXrfo2p__Xy14Ix-Vac4zISto0Sjsqpkgbtud1kX_1pdn8z8hcoULfyWPiokGlt9PEW9xuJA4obestBJRhkaOOtaif6XsK9ZOxddEAFzmCP67G-AIEsGZlPl4xb6K0ymySqmqzY0f8ZRGOW0Y3tg9S2kkCdy2dnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته  باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77658" target="_blank">📅 22:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77657">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جدی مکزیک همیشه تو جام جهانی ها تیم قدری بوده و مدعی ها رو به دردسر انداخته
باید ببینیم این جام جهانی هم همین روند رو ادامه میدن یا نه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77657" target="_blank">📅 22:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77656">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">توووی دروازه
مکزیک گل زد
اولین گل جام جهانی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77656" target="_blank">📅 22:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77655">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جام جهانی شروع شدددددد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77655" target="_blank">📅 22:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77654">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqHaj9mjjeZSTeZ53c3nAWpREtY8igG7LReMvl3YiM2IePK0YdoBpW65wQveApjJ_iGwpPeivbvsWNQQBckUKUWWJ6wz978X9PHRs4c_KXeU3EPdNjudc7qMKul3xUpvDqpQ-c4PIUNzs5hWcl_wIZLOSVab4xvpLubTJViMgwvnrefSHS4FEkStiV8hEvQKTHMVe4ApNydXhFTG0JGbE5lQCuLs4lR3-k-qCsaL4caCG_sSwkhwyNsSYuJJZjca0i4vBhOmiokieKdsxnYE_pcFUZ64iOSWvpGwLfKoTRuh76GjJHMYkhxYBp5BcGbATtZ8GJqwp3jGNOaxoCioeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس هنوز نمی‌دونه توافق نهایی شده:
من از نمایندگانی بودم که خلیج خارگ و نیروهای پشتیبان آن را از نزدیک دیده‌ام؛ پای ناپاک شما به آنجا نخواهد رسید و اگر بیایید، زنده باز نخواهید گشت.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77654" target="_blank">📅 22:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77653">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77653" target="_blank">📅 22:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77652">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دالگخیز
🔙
عمو ترامپ  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77652" target="_blank">📅 21:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77651">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز: امیدها برای یک پیشرفت دیپلماتیک پس از آنکه تیم ملی میانجی‌گری قطر روز چهارشنبه بدون پیشرفت در مذاکرات تهران را ترک کرد، کمرنگ شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77651" target="_blank">📅 21:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77650">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ به نیویورک پست:
توافق مورد انتظار برای آغاز مذاکرات هسته‌ای با تهران «تقریباً کاملاً نهایی شده است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77650" target="_blank">📅 21:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77649">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دیبالا هم از خودشونه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77649" target="_blank">📅 21:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ریدم
عادل فردوسی دیبالا رو بعنوان مهمون اورده برنامش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77648" target="_blank">📅 21:31 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77647" target="_blank">📅 21:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه: بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77646" target="_blank">📅 21:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juG2IV81LYT0XvVTW8A7HTUIgupgD-ig63EQm_TqyHkfJdEpNvZ3Ep6FDIoXbEfoKRtXRZpuPlKBFxgbxYgmlxIpVn1F1q4EI4iutqVYZANYIJ41qQb61vbIOeI32fRusDD99cJ8Zn9nOG5ht0s6le9ZljdZjwkWAhS_7ttO-JXNdTCziVr-6lLK0uLUk12ruOFIqkttijQSalBp1pv_5pjaXp3oNsfw0r9wjPVAs7P_Hq0Wb1rGmqYhs1c6nazbSzC1drSxpWdNXyohefmK1bmznEoOCflZfks6TA_94abCjn0vOxoYvqW9jvmm0Sst9XYHFMCmdNdNP8H5Vyx_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ حملات امشب رو لغو کرد چون مذاکرات داره خیلی خفن جلو می‌ره و به زودی مکان و زمان امضای توافق رو هم اعلام می‌کنه:
بر اساس این واقعیت که مذاکرات با جمهوری اسلامی ایران به بالاترین سطح رهبری ایران منتقل شده و تأیید شده است، من به عنوان رئیس‌جمهور ایالات متحده آمریکا، حملات و بمباران‌های برنامه‌ریزی‌شده علیه ایران را امشب لغو کرده‌ام.
مذاکرات و نکات نهایی، هم از نظر مفهوم و هم با جزئیات کامل، توسط همه طرف‌های درگیر، از جمله ایالات متحده، اسرائیل، عربستان سعودی، امارات، قطر، ترکیه، پاکستان، بحرین، کویت، اردن، مصر و دیگران تأیید شده است.
محاصره دریایی تا زمان نهایی شدن این معامله به طور کامل ادامه خواهد داشت — زمان و مکان امضا به زودی اعلام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77645" target="_blank">📅 21:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">07. Pashmam</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/77644" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">06. Adama</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77643" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/77643" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05. Khatereh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77642" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/77642" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">04. Setareh</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/77641" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">03. Tehran</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/77640" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77639">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">02. Beef</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77639" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/77639" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77638">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">01. Dor Dor</div>
  <div class="tg-doc-extra">Maaniac</div>
</div>
<a href="https://t.me/funhiphop/77638" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/77638" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77637">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBPIG8t8_6ZtTuNlxoKAeRDHknEg1Gh25z_VsN2Ep01z_KlAplDLNmzou7s2_vrDbV9rjzA4wjUWaWn68Wj9O5NuAXmAdBJZcO6SLPfFX7TgQlAHQUrFKJFVQayaOXGsc_iBwjxfkzfkSf_bUJiBCQji_Ct6g5vbHsvsUlpkMCgGHbhTBFmghsiQQnkIWGod8Vh2EX1zRB_xgNKBXcD8NjKscR0LT9XK_4jc1PIL61eLdCoK7Mj7DFVbINhmg2T5zK9qTCb8hhnt-NMeCnqPuepklcdohtkCnZAWZAjhs4GnCoXfpbtbaWrq_63t1TSRZ03F1lwH1Eh59ZLDX5KpLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید مانیاک به نام تیریپ تو تهران منتشر شد
📺
YouTube
🪀
Spotify
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77637" target="_blank">📅 20:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77636">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بالاخره بعد مددت ها یه ترک خوب از تیجی شنیدم، همونم خودش نداده لیک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/77636" target="_blank">📅 19:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77635">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6C_W325YT1jMXAEolSzh01dnsmTPrWfMGJYb4eyG5cDpP7Suq6RQPiqnj9hs7Yx0xUUiwnPNfnfvySPEsk-5inzBPWjMcfN9s3kMwdBWdriNbzReMyfEV8J8_Zvd1pbWNslMwoOqdSRFdZ0ACymVDLxak1tjMJDuocNjRq_IkJjSjNVtITFtWQJnF81toLeBPWUj6NE-66oA0u842rw9hYWRWPDDM3z8jkpguY8Dz-5u2pDo_3pY-WtM_fYFMwFFRMRY1MhOqH5H88wMd1IK2DaS6qf5qATscELMWvTNH7phcGRKMoo80H1VLC5niP3KAoDHRYn-_G6nkNYC9E4Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندساله که اسم توییتر عوض شده و شده X ولی گوشیه من هنوز توییتر نوشته، حس نوستالژیک و قشنگی داره‌
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77635" target="_blank">📅 18:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77634">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رامین بچه کونی:
برای اتفاقات روی سکوها آماده هستیم و نمیذاریم بازی با انگلیس تکرار شه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77634" target="_blank">📅 18:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77633">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">با اکانت توییترم که کنار اسمم
🇮🇱
🎒
🇮🇷
🇺🇸
هست،
توییت زدم وطنم وتنم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77633" target="_blank">📅 18:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77632">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRoUaAulSrSk9qA1Vhl6yJvJCxv1p1C6DeBOi1LOTHNL1ZMWHvEWlntj07gKXO-VoPPRwwraOphiKlj9a7Xbh_Elz8Pd2xKPFchjlYKapU3ib7Qv6xTm3jFdf5oIhcZqAUPOwk2OVUTuX9ccRCJhFq82tCzZ07h8AlxNIA_0VYhQQ-gJEcOdJDtC7cd0amS-QLe32TlgS3bEAjrvixaxWJikXpz03HfN3r0Gl3KAo39UQK6wLAXZkH2A5TP_4lRU9WwIfOMYcRqArYp4HD2Xs7gI6cks7H4B3wdft9pyEuZWlB0GnpgJMLSM8xwyyJW74EycHYHQLU6R3MgRW5_5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جون عزیزتون این چطور پزشک شده</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77632" target="_blank">📅 18:03 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77631">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqwF4IdKqZWWUjuNyktVE9PzgnZl5_YPCRaoPNP2-Y8cO4WmMmwSc-8QoeltoxcgpYn9REW57jZmBrVQFDHqNStU9s5aNnhBTs3Szq5bcw6PnI5cUAH3o_YUkRqzxizrjQ7hHSRskQ4hBDpn4sOHMbEdjCoa42IMrrzaC8C7uvmwW-WSNYa8Or-Q0jfIqnU6k1j3Hs8ZBsYK2P0AP80FuxGCIdciV22moIJxLLOjzEY_QMx0rm39zweOmgwDfnXOBeAyPQrOW0UD6TxtLAfmRZaEbJdeW9l3vWUpzgB6ffTpB_iM1XXtYzzKY-RxxlDVk3eFAuzIozswM1VmFhHrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام اسراییل برای حملات امشب لیست ترور داده !!!!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77631" target="_blank">📅 17:45 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77630">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8OhNf8brfQ07JImlpnZN5aavaWeVBr0g6Qj2Ns6UXvg3yDlRnCczYNZd9zArg4tedvLd3S0aMbFmIJvJpoZzP36EwFLTrcyr6IS2yFq0wGD05SE9n4qLHb1rTPW3ZlksBDZ7_3yfD5trgTpPp1i8bTZg17kiOGFoaj56suDOzjTH6AeznYiDk_W-GfEMTK4W9P5YGyk4mwju5PPwJgmT3tcVYrA2UmpoiHYgkHzJ5aPFYYJ5RhEmEQmKDCPWBPYUNxUX2Yr-R1WIUyb47P1j2B8-e9kGQv72u9SZxiaKbOHrSSm87TWuR59uQ2sFH_CfD6ggkzXs76OFa65wNMwQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد خیابانی : اسم اصلی من جمشید هستش نه جواد.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77630" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77629">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77629" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77628">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFwoj05myVxO8CsKJPEVNkDA_-KjpPmrIN_BD6TyrS7Vv8UbPmFoJs0ok6pymKAuHmLebstu7uGxNtG1_GQuLfoffhYrcHZkHifIA3ongaSWY2l-bh0UWXoZ9oX__IcVLLdCEbJ1GQhCTArWafohErlCWEe0HYC46Uzg7l07mYR_HQD9Es5JpKmsuzD46lRmyWSjiOCSlqZ0JLLQ3wi6JINZE7nWSrBTTkISDSTMaEarMuK4CmAp3AU_f_NPqgIKB9zRH9D9EIZ7BlGATAEJTy9Gq-poJT2SJcCEhR-nChDQuVeSfFZPxMcfj6TlyOeHl6nm00u09FOIPLZYTW6YpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g21
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77628" target="_blank">📅 17:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77626">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=nXMvSiDQRJJnQmmDfqB94p3pxbjWFQLe7SmJuav3HpnNjkdGLJNhupO-9eniD3fQxK30bpll97RA_0dUGYV6k23X0DTKgBEK8HQj2O3rNYMbNj6EMgZY4-JcyLeQcZMlMlDOiiZpOpm_HsGen9vtU6UoRAfn9gszrcDM2nW1T0jM_PZDXPUDLXtM1tSO5qmxQ9JWJwCvnkEHKKKLBMP1TTtDG71S-A2slfrWLlfITwYxEXo8Z0WQrWALlE2Ih9lJhhNhfJp4TxQe7P5Q06CEqaDxyiH5ao4skam-97kgrrVHsCgh-baU1pGaMuA4DDHVFLGa_G8QB5wR6ksiV3k7vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/683daff4c0.mp4?token=nXMvSiDQRJJnQmmDfqB94p3pxbjWFQLe7SmJuav3HpnNjkdGLJNhupO-9eniD3fQxK30bpll97RA_0dUGYV6k23X0DTKgBEK8HQj2O3rNYMbNj6EMgZY4-JcyLeQcZMlMlDOiiZpOpm_HsGen9vtU6UoRAfn9gszrcDM2nW1T0jM_PZDXPUDLXtM1tSO5qmxQ9JWJwCvnkEHKKKLBMP1TTtDG71S-A2slfrWLlfITwYxEXo8Z0WQrWALlE2Ih9lJhhNhfJp4TxQe7P5Q06CEqaDxyiH5ao4skam-97kgrrVHsCgh-baU1pGaMuA4DDHVFLGa_G8QB5wR6ksiV3k7vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درباره مدت زمان جنگ با ایران:
من دوست دارم همین حالا یک توافق انجام دهم، کمتر از 3 یا 4 هفته باقی مانده است؛ وقتی این کار را انجام دهید، می‌توانید یک قدم جلوتر بروید.
نمی‌دانم آیا آمریکا تمایل دارد کاری را انجام دهد که من واقعاً ترجیح می‌دهم انجام دهم یا نه (تصرف خارک). ما در دو جنگ 13 سرباز از دست داده‌ایم؛ هیچ‌کدام در ونزوئلا نبود، و ما کشور را تصرف کردیم. در ایران 13 نفر از دست دادیم.
در ویتنام، صدها هزار نفر از دست دادیم. آنها دیوانه می‌شوند چون من سه ماه در ایران بوده‌ام؛ من آن کشور را ویران کرده‌ام.
آنها به من گفتند که شما گفتید سریع‌تر از جنگ با ایران خارج می‌شوید. خوب، الان وضعیت بسیار بزرگ‌تری است چون ما بهتر از هر کسی که انتظار می‌رفت در چنین زمانی آن را انجام دهد، کار کرده‌ایم.
ببینید، ما 19 سال در ویتنام بودیم و کار را انجام ندادیم چون رهبری مناسبی نداشتیم، صادقانه بگویم. اگر من بودم، آن جنگ را ظرف 3 الی 4 ماه تمام می‌کردم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77626" target="_blank">📅 17:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77625">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=QVmmlmMRFb9y_6q2amH494P4KmLoF9YSrYjdLdJz3sEOxhljWucPq1CCRXn6kQ0yrS2-tddd-_TSZHzdgR3mdRBkll_PAm_D_CTnLTuX3a53igFyEgcIMapB9LbAZpHywwvBRwIVQ0f8F-oaz3I1S0Elj9ZVtzRlUM3x79KyT1OIP9H3mqxtsqhOn8RBHYEP-O6fBTifwTc4fkhHfGf2PFk9O0y33SOlmNfXXw3-4A4zYPReEBfSykgI38WgOkVtnChyU5TBJ06q3jx8jZaUD3v8CLR9lZBrDgku_5FalJy494sw9E9Dkbq-kl9Kbi4HB07E2N8XmrDK5d-cSWgkng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6599e2d096.mp4?token=QVmmlmMRFb9y_6q2amH494P4KmLoF9YSrYjdLdJz3sEOxhljWucPq1CCRXn6kQ0yrS2-tddd-_TSZHzdgR3mdRBkll_PAm_D_CTnLTuX3a53igFyEgcIMapB9LbAZpHywwvBRwIVQ0f8F-oaz3I1S0Elj9ZVtzRlUM3x79KyT1OIP9H3mqxtsqhOn8RBHYEP-O6fBTifwTc4fkhHfGf2PFk9O0y33SOlmNfXXw3-4A4zYPReEBfSykgI38WgOkVtnChyU5TBJ06q3jx8jZaUD3v8CLR9lZBrDgku_5FalJy494sw9E9Dkbq-kl9Kbi4HB07E2N8XmrDK5d-cSWgkng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز درخصوص ارسال سلاح به معترضان ایران از طریق احزاب کرد عراق:
ما در واقع به آن‌ها سلاح فرستادیم و صادقانه بگویم از کردها بسیار ناامید شدیم؛ کردها ما را نا امید کردند.
من با این تصمیم مخالف بودم. می‌دانید، من می‌گفتم، «نه، باور ندارم که آن‌ها سلاح‌ها را تحویل دهند.»
فکر می‌کنم آن‌ها سلاح‌ها را برای خود نگه داشتند و فکر می‌کنم این یک ننگ است. اما من این را به یاد خواهم سپرد؛ کردها! من این را به یاد خواهم سپرد...
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77625" target="_blank">📅 17:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77624">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ee5717647.mp4?token=KCwxeZX-RPYbs1anBqMWoMIr7rNeleqjoUioK6j8Txm0f2cfvqJ-hg4DopVnBNNamYn8gTYTzO48xOSsphbMOXuthKWeXXBZ_smByRy3fzXAT-RP_AQYa7Nb3-vIjyTjIQGOWADDcvVTvNh4AKmTIGRnebFOQHn1Zb6PITwsbd7jATNHoeNmhL3low04_4rdlVzpTidpDJrDzpPKqyaCTKnqA0AhlhnPju_Q_WFtSdN-KtJ88b1gqCEFJ9u18gGlHrinozbXuDtwVpr9DuUfj_0w69iYS6ffsGLmTJNEHAbeGixH0ESWOp9rVVnj1qMTM3Pn7WrLWYlNNpqQHwtBzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ee5717647.mp4?token=KCwxeZX-RPYbs1anBqMWoMIr7rNeleqjoUioK6j8Txm0f2cfvqJ-hg4DopVnBNNamYn8gTYTzO48xOSsphbMOXuthKWeXXBZ_smByRy3fzXAT-RP_AQYa7Nb3-vIjyTjIQGOWADDcvVTvNh4AKmTIGRnebFOQHn1Zb6PITwsbd7jATNHoeNmhL3low04_4rdlVzpTidpDJrDzpPKqyaCTKnqA0AhlhnPju_Q_WFtSdN-KtJ88b1gqCEFJ9u18gGlHrinozbXuDtwVpr9DuUfj_0w69iYS6ffsGLmTJNEHAbeGixH0ESWOp9rVVnj1qMTM3Pn7WrLWYlNNpqQHwtBzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز گفت:
امشب بمباران‌های بیشتر و قدرتمندتری (در ایران) خواهد بود. بزرگ‌تر، بزرگ‌تر و قدرتمندتر
فراموش نکنید، ما تمام سامانه‌های پدافند هوایی آن‌ها را از کار انداخته‌ایم و آن‌ها هیچ چیزی برای دفاع از خود ندارند.
منظورم این است که ممکن است سلاح دوش‌پرتاب یا چیز دیگری داشته باشند؛ اما در کل آن‌ها هیچ پدافندی ندارند.
آن‌ها تمام شده‌اند؛ اما روزنامه‌ها و رسانه‌ها از نوشتن آن خودداری می‌کنند. ما می‌توانیم فردا وارد ایران شویم؛ می‌توانیم سرباز بفرستیم. من نمی‌خواهم نیروهای زمینی داشته باشم، اما اگر بخواهم، می‌توانیم گروه کوچکی از سربازان را روی زمین بفرستیم و کل منطقه را تصرف کنیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77624" target="_blank">📅 17:00 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bfcc7606c.mp4?token=FGb9ybx3quYWl81kheyiZq2tdrdDx6W1J2IHYWE2wIJQTLnO4iSsqEwhCipugf4lJySa0kJkhiHnEdYcUubh5Jw2A6kWhoK6jFpD3WbnjZ677EE-fgP-9djxT178Nzgd5uy3kpIMPt6rPj4MT0yNegs7v82FxgubyVbHO2wkD6f-eFMuuVxLUiuIWD86xFNs9n0wKfu8vpQybZQPSD9idyhv83D2mqmzb887xWfXRNOjVWU3SNahkp6l_6a4FwHTcsGniKcZWov52DyOc0kFV0euLQo-Xb6SM7YlghY547H5-8WyPd63upRzSc373lCw1WOf4UXKjCyVjCAzUue8-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bfcc7606c.mp4?token=FGb9ybx3quYWl81kheyiZq2tdrdDx6W1J2IHYWE2wIJQTLnO4iSsqEwhCipugf4lJySa0kJkhiHnEdYcUubh5Jw2A6kWhoK6jFpD3WbnjZ677EE-fgP-9djxT178Nzgd5uy3kpIMPt6rPj4MT0yNegs7v82FxgubyVbHO2wkD6f-eFMuuVxLUiuIWD86xFNs9n0wKfu8vpQybZQPSD9idyhv83D2mqmzb887xWfXRNOjVWU3SNahkp6l_6a4FwHTcsGniKcZWov52DyOc0kFV0euLQo-Xb6SM7YlghY547H5-8WyPd63upRzSc373lCw1WOf4UXKjCyVjCAzUue8-oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهور آمریکا در مصاحبه با شبکه فاکس نیوز:
پیام من به مردم ایران این است: آن‌ها می‌ترسند چون اسلحه ندارند، و طرف مقابل اسلحه دارد، و آن‌ها اعتراض می‌کنند و تیر می‌خورند.
رژیم ایران حداقل 40,000 تا 50,000 نفر را کشته است و مردم می‌ترسند. می‌دانید، وقتی یک مسلسل روبروی صورت شما باشد یا وقتی چهار تک‌تیرانداز در چهار ساختمان مختلف به سر مردم شلیک می‌کنند، برگزاری اعتراض سخت است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77623" target="_blank">📅 16:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار: یکی از چیزهایی که دیروز مطرح کردید این بود که اهداف بعدی، پل‌ها و نیروگاه‌های برق خواهند بود؛ آیا این مرحله بعدی است  دونالد ترامپ: ترجیح می‌دهم این کار را نکنم چون وقتی این کار را انجام می‌دهی، مردم هم آسیب می‌بینند. مثل اینکه شنیدم شما به آب اشاره…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77622" target="_blank">📅 16:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4e5f9e8c.mp4?token=URqvyIe4NefWLtjCWOttMR34jW1OwvqFuNUkEDnpo7KjHURUFbGpzAATPR24QBW958b06jcc-SRtFFuYt4xrtMK3ukQs314kOFlJ-GFySQuge1rhSWTmzKm5nyKuxCVoB4Rn9c6T6kUxy01AO0jheZYlf3i2E9BNEG3Nb67dcQYUnatUGHZx2oNiU0ZQNqh9bdXBWvyc7LVppXVaA6whc5LHNsquxaLwE3-dEeUIUEsEnlXWjxWQ7gOam8Ti5Xg_xgkkGWkb4tyBDJRESzImR5VUxwGP5G2bW90vQMS8JRJhRu6YvXHeo5K4fhVFguH7AdFc-uIe2IToUpPTelJYbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4e5f9e8c.mp4?token=URqvyIe4NefWLtjCWOttMR34jW1OwvqFuNUkEDnpo7KjHURUFbGpzAATPR24QBW958b06jcc-SRtFFuYt4xrtMK3ukQs314kOFlJ-GFySQuge1rhSWTmzKm5nyKuxCVoB4Rn9c6T6kUxy01AO0jheZYlf3i2E9BNEG3Nb67dcQYUnatUGHZx2oNiU0ZQNqh9bdXBWvyc7LVppXVaA6whc5LHNsquxaLwE3-dEeUIUEsEnlXWjxWQ7gOam8Ti5Xg_xgkkGWkb4tyBDJRESzImR5VUxwGP5G2bW90vQMS8JRJhRu6YvXHeo5K4fhVFguH7AdFc-uIe2IToUpPTelJYbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: یکی از چیزهایی که دیروز مطرح کردید این بود که اهداف بعدی، پل‌ها و نیروگاه‌های برق خواهند بود؛ آیا این مرحله بعدی است
دونالد ترامپ: ترجیح می‌دهم این کار را نکنم چون وقتی این کار را انجام می‌دهی، مردم هم آسیب می‌بینند. مثل اینکه شنیدم شما به آب اشاره کردید. آب واقعاً برای آنها یک خسارت ویرانگر است. من می‌توانم این کار را در یک دقیقه انجام دهم، اما مشکل این است که مردم قادر به نوشیدن آب نخواهند بود، بنابراین نمی‌خواهم این کار را انجام دهم.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77621" target="_blank">📅 16:49 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ باز از حکومت ناامید شد داره خایمالی مردمو میکنه</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/77620" target="_blank">📅 16:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77619">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">چرا فرستادی واسه کردها؟ میفرستادی واسه بلوچ ها</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77619" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77618">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: کار برای ایران تمومه. امشب بمباران بزرگی انجام میدیم. اونا میتونن پرچم سفید رو بالا ببرن و بگن ما تسلیم شدیم، آمریکا بزرگترین قدرت دنیاست، الحمداله. واقعاً دوست دارم همین الان با ایران توافق کنم. هدف بعدی ما پل‌های ایرانه. من نمیخوام اینکارو انجام بدم؛…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77618" target="_blank">📅 16:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77617">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: کار برای ایران تمومه. امشب بمباران بزرگی انجام میدیم. اونا میتونن پرچم سفید رو بالا ببرن و بگن ما تسلیم شدیم، آمریکا بزرگترین قدرت دنیاست، الحمداله. واقعاً دوست دارم همین الان با ایران توافق کنم. هدف بعدی ما پل‌های ایرانه. من نمیخوام اینکارو انجام بدم؛ چراکه باعث رنجش مردم میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77617" target="_blank">📅 16:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77616">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این ترامپ مادرکونی هروقت تهدید کرده نزده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77616" target="_blank">📅 16:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77615">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بنام خدای رنگین کمان، تولدت مبارک کیان.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77615" target="_blank">📅 16:16 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77614">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUE8jAlzslFRgDFPU94kI3RMpMsd1wuY8av99-ZkWxdi7DY-ppVImJeAsnE2eQCbkqQNAvPyY34oUaciDwhwVROE76G9m706DH0rXvaZ8BE_J4daeaXJEh5ymOlHhJAazqW6AUE0_bi_Rj23NLNhdhZueLbJX2CEDquBo1hgMRfiRBRgYSYWe5pGJ0cncCRTQ-rLeBvxEN_Gtc-UTZfcq4hJXxMHWlm3L-b8UHJqczxTlb3fXAc0EDkODzSJ_BSfo2Z3tjzoJ7XSPaiVGE-w3Wpx9oEEoyei_7Wv-MlmfqnP4eqz9Dvn_lr0l-gdDm_forPSVokSHClKX_7nnjxX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنام خدای رنگین کمان، تولدت مبارک کیان.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77614" target="_blank">📅 16:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77613">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ:
ایالات متحده امشب بسیار سخت به ایران (که نیروی دریایی، نیروی هوایی، رادار، پدافند هوایی و تمامی دیگر اشکال دفاعی آن، به همراه بخش اعظم توانمندی تهاجمی‌اش از بین رفته است!) ضربه خواهد زد. در زمانی نه چندان دور در آینده، ما جزیره خارگ و سایر نقاط زیرساختی نفت را تصرف خواهیم کرد و کنترل کامل بازارهای نفت و گاز آن‌ها را به دست خواهیم گرفت؛ بسیار شبیه به کاری که با ونزوئلا انجام داده‌ایم، که به شکلی عالی هم برای ونزوئلا و هم برای ایالات متحده آمریکا در حال نتیجه دادن است. از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77613" target="_blank">📅 15:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77612">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADDSLIcqlKG_0D5HtUlY7wHssZYPop89xjL1oU_Woq8CbNGgRmRLnX_Q9HyOE97hQhA8fhZTcBLngbrkxx5_Vo3-UVxEKEq7KtYX23kS8Yh0nMCTd1vv7-a4K188C4L1o3jmRg2nTi-Hghu36FLxBBurzWRw5H4sUQeHnXhcC-6diV3sqcCsCu4G30EcQSSzgCGPDP3O9l8f_UrcNP9tSQZuEhkfOYy00sd5eeQdj73XS0A6edQdC4PJhwo4oWLwIP1c0_oHEvnU0HkgwvQqHvsYM_Zt_fB36-TtdDc18gQlMsMCQYxkMV-KJMeqHLntsO6WWq1BAeN3Qf_NxBIhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای جام جهانی آماده اید؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77612" target="_blank">📅 15:43 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77611">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtfgolENpkoz5Eb0CUEyeGuz-WL8Y-T3l_wP_kdC30ZuiGl0A_mXn2vhQjAyJ1_TY_8LKhQOPtyp3QyWRnJa3PSACiJ9PtUVIyfBb7FzWv3E-qoFrBHj7VFgZBLsvEdnTr8WiYO2duQEHigLTlrq-QMq6S6fBYbwcdwDwFfeqMOGEFXQCsnbxANCMIYraQeNWkIiQMmjlGj1LGyA9eL6rAmlCH3mwbw5wPWcRkpV6E4_60LWpv5cn4KNtpBCJItbWsoC96TQLqvLawtQILXX1Pj4JOo7KGM4xdXx4U6tiRKKE1hePooAHv_k8EWjN4u-0-ndcyvA70Ub1BpYgniGlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77611" target="_blank">📅 14:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77610">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVDmU8u01lHnzRHVqwyfZMuETvPa3395CZhSmcJq-QL5JNTh_3_STXMyw1YIeXDsVsp39pbU8fC2RT_dIbpKyTM0TGf3CrmzFo1Hd9CPf5WiWnaF3HwPIt8rk2oMkoLP165zclGQPX6QkGmc56o0709sZl5Yugq4ezJFvVz-kXN_ufCeRlhbSQEjdbdgseimHGBcH8WCb6_t0_BHARA6nx2lb7lyP-gv_5kjlHzE2mllYCt52mN4Sm6ZY9hsBjdk1fc2p-1GNToO8d1H2i3sOTm2DIZNdWWbKhpMlY93AT9odmCtMm0qDMawK8QLZd4976CVaO5iy-llWPinu7cfYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب داشتم این صحنه رو کابوس میدیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77610" target="_blank">📅 13:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77609">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQIeFyheYGk2cDo6B5NYFBQvpfBoFORXMB-wj40uzOz7LCQ3mQAoQgu02E1gScqU4NwZVjfXNMC2nUmTFVVQqlHPM6-PcTwv_BkCELEEK2xjImKE-sE1fTfUwacW4tcgg-jT2dQBn0jUdCDxhmTi42vUobuP7yuzHO1r5L-5uYllcdNLZIeYRL7jRDM0YanZw3unmVNcfyENUz66MqL9KI4W2Vqlg8SNiV_xvsvLkQ1tKMqhJoKUOf3k-WwOqMx1AwAHO9FUDztvJUZWTPjmXvaOQ7koQifi5u8JR-ILVp3DGxTaNg74CzgUWBeldSIRjxNZJPghcRKqijFG8qx03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 گیگ فقط گیگی 2/800 تومان
💥
💥
💥
100 گیگ فقط گیگی 2/990 تومان
💥
💥
💥
50 گیگ فقط گیگی 3/600 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77609" target="_blank">📅 13:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77608">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک خبرنگار آمریکایی:
ترامپ از تبدیل رژیم در حال بررسی سوییچ سیاسی به تغییر رژیم کامل است او معتقد است جمهوری اسلامی هیچگاه ممکن است حکومتی اهلی و عاقل نشود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77608" target="_blank">📅 11:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77607">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نقض نقض نقض، تا روز آخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77607" target="_blank">📅 11:34 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
