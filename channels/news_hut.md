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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 218K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 14:07:51</div>
<hr>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=YdgQzL6lSgoQ4_9-j3avo_aH9ugoOntoBkWIjCIB2BRvoRTGbMFVlltvDaLouWo3SSME1nyfnyR3X-ojtmVnTWcqC2CUEtACYHaZoiftCzbscYIXljMg-x289Yr_5ZIdJtrjKj4po2raGbDPUlgRzHP3CttUfMqGEQu4mLFvtJC0WxAJMr8ASEsoDQXLZBNVNiOQYoNOjpRoYLAV-huez6PpcGSOaLOirAwt3zF5Nf6eyVlMbV_jQRtlOh-vDBpPhxj5xbEUeIKtPaZ0FLnwteHLyqDnbevs8uokuWxVwB7K3aHidJBak9AO1U1YADsnb7sw2E02Wiz2ZIvAP04LxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=Tk9H2xyG7qZdF1Bpd2Pn-XzT1m-oEg5R3e2YSCndA31DLL-3Q7vCtk2EHoUQvAiHol0J9EJVq5WTFqwboj_WApb6NTXnEzlq_p8FCxsy7RANR7rM7G6-XS5eOytQCTi3x4WktQbDh9zkC89prVn4JKg383U9uxAun-p0-Jjshq2HQCBbe85cCQkm0v4deBHOrIyL2tRuAYW3CTw-Blt3zO1L-EQfIOsnLH72GUZYLlR06oG9Dt9WM4I9yDjGJpzDsDG9OAt3ojk-Io9HDE7bT-cFV7N048tpvxQ4PUM8zdS8i0avrJUKq6G7B_LzsbTqd2dODzEy-RMgT5KKLve89g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C210IUSQPHmJrC0gHd6J40wi18_0DQ_Dd6BhKb3cnIjAhlUtpkoQg80Q62fOjF7tS8cblSsaJb5CYjuRssu-GAEoDmdJXcBHGlvQN7JzzAMYdLlp3GLSW7DzvF-0CUVjIWoRh96rwcO7nMJztamMoVsY1okB52jONOZC_5Id50unheNuA4pssY5mIHyeWzJs-WXuFO2khaOGD7IimuQrquAZ52ZRJWpGtV1c2y0XKsyNHiE6FSNbZMUyTDF_DaQFrm4w3cXo-gwIWA0NN_hLMB_ts3qjcmVPsE7aUDMWSWlRUM6Q6ONHYZOfLFdXnJhnioMqUctZVEnsqb_YQuB5OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNcoPS50F0sYADlqbDiN-3LaXvD32AzvGmd-rt4QAV-FHU1OoyHRDv39BOr2Gl44qM5xq8oVr6F0pufSzEQ2liUFMsHgW6e34iNXrC11HmsPptFJ_wHNt7mU-hn_isSiUPOiZEA3d71_1dHO8HH9XmtFNXgxbOlqQxAu29JE41LFzaPlsDG9BymSx8yhgG82B-RBCEzIYskSFRZWaOnOoabDh2d3Vo_wz6r7icfFh49eUNlkPAkvKwIKTUyRSz8s5A0AxEH5Tioy9z7WVH2vAk8XgMkDsLlx3tBHSJfGabBdzPKN6pR0HlSG5IzsUxtAjCrGLLSjAvWnDXjIKo8JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=eK1YlnYAPK6X7bno0JjDP7Rm-NVer74xLu_puONCFoD05Y3oC4xm8NUGeC4VGpMlOMK_F2HrngOMBWoKVGzY0hseWkyfVLXbb0Eb7QcEQd-0kXBerhft509p5Z20VtGIgBeFwWl1MPag4-p6Ne7owyYeKZaxcku5S9ZyGWUftlWSku3zkH-dVUadWdtyuUuvB1U0UuIh7NigZlZxje6912ot_M3m-OPNXXvIWO6exqqbF7-VMH0vAPKJbJ_jUKz9-wHpuip8We8F9OOW0kvmoL9f62YKFgZw3ifbAHQTbAb8aJLHqzlVAcV9U_rC44JjFuFvcmAfpoMHEK_Vvb_kdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=ZTW3mOHtqn8YK7SFQHXpc4fytArdbaQzwq7FEyTUw9FBeXUbBuwvPk4PudRedEUTKJAdeH621esbnDpe3UXeh--TQBh_WznuV35A2ctm4XIriMyPn8JIAROvUjD3kK48RW5Zmc6HvSNkZ7EJngi1RgAmHgqh8km71Q7nxtXTGso6Jt00upKD3XpIyaN__7ecN33Y0VxCs1phoUECdrE23eTSHsRxTrAFRK7Tv9tni9lORmnCvDj-XpNx-nC7JMeTyxnVhx9GtdWl-ulk-goATDDbF3rrBbjBPlCYop4Z7bu2M-dQiES3XwLSy-rOcG9otEeq6cMosW5iYFPdWoJCqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=ZTW3mOHtqn8YK7SFQHXpc4fytArdbaQzwq7FEyTUw9FBeXUbBuwvPk4PudRedEUTKJAdeH621esbnDpe3UXeh--TQBh_WznuV35A2ctm4XIriMyPn8JIAROvUjD3kK48RW5Zmc6HvSNkZ7EJngi1RgAmHgqh8km71Q7nxtXTGso6Jt00upKD3XpIyaN__7ecN33Y0VxCs1phoUECdrE23eTSHsRxTrAFRK7Tv9tni9lORmnCvDj-XpNx-nC7JMeTyxnVhx9GtdWl-ulk-goATDDbF3rrBbjBPlCYop4Z7bu2M-dQiES3XwLSy-rOcG9otEeq6cMosW5iYFPdWoJCqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WItXzxUAhs0C0v3xZ8i-b-74oknf_rUmjP-LRZYPTsQClfFcW5mkfUAi5fpi5AU83AIMsyJ6ze9xvxE3B8MyFO10CGbY92K989LIxm9msUwNKFldN2g5JvkvFpCUBfxbsKnXXZTgk2bDVOImTAwJo92wppILUQJcO4z0teDxt-BDfoNpol6epPSPKDvEXt3oFBibaxqgPkDoRncv5kTVj8ORgyBjVy2bqeiEL_biscxyfiWDGzMTDkrA1JVzsvt5_G1NTQIAc7EcoxKeMuAloJpY53Q7DTd1grvgEJqYrfz9CjqbBzUs9Orhj7RgoOQdPxxAVoslM9J6TbKton9BKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=B8Tu7NTum4EEWas_eCrZ1Al1rdqDXKNbIgk5zUUm60IGn_r_iDOwkukh9LYXhNEBZp75y3eso_ro5gmG4ZD1I2C_bEynKgLveWUlmJPowPx-R3M9FRheI3HqzLOPhJ4O2hDn8nC0rSOXd8meVt2BzupYVkC6M28bsEfniuiA58esicqRJF993vURTySQDyGa_1_tI7vLBBeu6gq1WCxMvRFvi5MtTGhkHmjeUSYnBB6eIk0n3UaGQ4-F_nnPEebL-44bOR1OnS-Qkn1Iqgfa3oAbkaKq-fwgAv5PUADmitmx_E_7ki5pxo5DHMYFUbAwexnhxe2I_NdrrGtihwTvmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=B8Tu7NTum4EEWas_eCrZ1Al1rdqDXKNbIgk5zUUm60IGn_r_iDOwkukh9LYXhNEBZp75y3eso_ro5gmG4ZD1I2C_bEynKgLveWUlmJPowPx-R3M9FRheI3HqzLOPhJ4O2hDn8nC0rSOXd8meVt2BzupYVkC6M28bsEfniuiA58esicqRJF993vURTySQDyGa_1_tI7vLBBeu6gq1WCxMvRFvi5MtTGhkHmjeUSYnBB6eIk0n3UaGQ4-F_nnPEebL-44bOR1OnS-Qkn1Iqgfa3oAbkaKq-fwgAv5PUADmitmx_E_7ki5pxo5DHMYFUbAwexnhxe2I_NdrrGtihwTvmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=s_OkyTTfulyonQgAnanz1q8DOYwvyrFnPomeKQdeBYKfzqCYIszer9c3Dyi_5j47gP5pwxetTnaTxOS5XQyDQUWK7a-wdW7ixLQBI5sxj00TtiLyRCH9T6cgQfXixsq5NHjtjYaC1gBYQwF3-1i4jgvrmyPvyxooHztt7Cbnf7_omb4mvSLmh2h7gjgmtNWMrTZtjBWfE0NPTMtdrtR5U-IxMZRsc-64Yr083EfwTRr6I-R2gf8rLbXzQorp_8zx9735It8kfWWWN1c0YykS7FVsQnfU9LILqWlka22lpzR7C3ZX5W5D7EHA02qjrE4hJWSaqMrkSKe_vnibeMDuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=s_OkyTTfulyonQgAnanz1q8DOYwvyrFnPomeKQdeBYKfzqCYIszer9c3Dyi_5j47gP5pwxetTnaTxOS5XQyDQUWK7a-wdW7ixLQBI5sxj00TtiLyRCH9T6cgQfXixsq5NHjtjYaC1gBYQwF3-1i4jgvrmyPvyxooHztt7Cbnf7_omb4mvSLmh2h7gjgmtNWMrTZtjBWfE0NPTMtdrtR5U-IxMZRsc-64Yr083EfwTRr6I-R2gf8rLbXzQorp_8zx9735It8kfWWWN1c0YykS7FVsQnfU9LILqWlka22lpzR7C3ZX5W5D7EHA02qjrE4hJWSaqMrkSKe_vnibeMDuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=bSR-ZNF9MOJcYVzynvSgf7fpFOQBNFdmBYLYg4CSTfkraq7ZlngRDPMRYYTgs2kP1AuibWUciw7PXP4kMdgmP8VI3b4rEtQQiAgihlt1naWL667qIZOQ0UUZL7VoQ-PmLT6OMUlM4E1pH7mwkM0vDBAvRLUJ8KaU_6gS21sPjdy5LWx1JEbybpiRmZ9oqJaDeqUOxrlwbakcYIvPisn5KfSl7MT67t0uVFmXWsuPtOlN5clK0lXkiYuBinZFgdKghXE5sAvw8pulKDMQ7YjGwCv6of9OaIc5rCu95k3gHDbjJOkdjr8ht5oqpWzvUuo5aWRtWIUU0UcP74Kt6foF6w" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=bSR-ZNF9MOJcYVzynvSgf7fpFOQBNFdmBYLYg4CSTfkraq7ZlngRDPMRYYTgs2kP1AuibWUciw7PXP4kMdgmP8VI3b4rEtQQiAgihlt1naWL667qIZOQ0UUZL7VoQ-PmLT6OMUlM4E1pH7mwkM0vDBAvRLUJ8KaU_6gS21sPjdy5LWx1JEbybpiRmZ9oqJaDeqUOxrlwbakcYIvPisn5KfSl7MT67t0uVFmXWsuPtOlN5clK0lXkiYuBinZFgdKghXE5sAvw8pulKDMQ7YjGwCv6of9OaIc5rCu95k3gHDbjJOkdjr8ht5oqpWzvUuo5aWRtWIUU0UcP74Kt6foF6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2poLvlAaWWu83sUYsl2H6a3_dut-XOxw6UK5mCqv9BtVOBI_C-Cd0f6VMF15bHHmMIDfQWDM897nGqj3A5A4kANixoNEByXITqm7lUUYnTWMh9ymm6naOd6s2FrAX2kRYt6unUF7moxdl_vtxPBCwzAJUJpuhP-oWZSOrJY_BYY4PZoHKBDcqWVLBJxw1C9i9fnoPTcCnYHF-2s5HvYNnEOVwwtzFhZTvmS-B2sOtdWgVM929zXZjhGRmuLLCE0NpiynKYIVvf7ItzoQnh26i7FJ_wu7IlSlVGa4wGRFd8lPDECxSoxXwuqbWAiGjMVgxOSQr0lVSNhYP-xYafNoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSaXKLl7uEX8YYWhB52ttyi9-Vo7Tr1iKDJdvb8UcEGO6RznbNU-zN3vbKFuUAO56CkGfRuxQcj4Hix7YBE42lspg0UDkJzHxYUFz8DWH9mSXXtogjR5NT9gq_11_pavsrMRKsuqY7B4v3KDgRcEUq6gFbkGHlkIuq7NsLH3EiieCn3T7KaJZsTAVYpJa-BMgk3he3r-lCE0j3TL0ytGPYBCBU-nJACdq-5G0pTUrLD5i4-ETfShI34ttL9MuQ9Bg7htVYXpMgokM7JYD626MhhCCpAgxySHT7gC_JPnj7kvbvKfO41bcP5lnaYVrvre6tiNlbe_SXOJU-C8sCNdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgE6tdiIO6zxzayIUb-pT1BlZ9MI1P-T6TsgsGPO0pbvuSXH4yvM5IQmc3G8LZGQTlqk5keWaElcdxLOJDn6uo25gBXksliow_MFZ2StGGRteWfRHQyOYB5ecVw_vJ_ECptrYPRTzpQ40bG-1uYOeTnwo7BYI993Df187knH8FtkD8KEzfpPWlRfdWQVH0ZAyqVM7PjfiUHFKM3WyLhR2xcqGT5J1vo7dps_YXEA05TPoqe0Bj1tflIRpFvoQRTDD_fwRl_KJnApnVgPZiafJDJe_ZR4z_1KMIgV5LkGvZBJjsGS6GcHLluDX7sbSB2sbv-wGQTY2eadAm9nAj4Klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_d_2QmW3cpakyvRQzatnluYExQ4ICIFCWDwX1lyZOP29uDhjPCrXcpjNNJx7-sZUmfCPH3CAKvCOS1oYXp0so6Z4sRs5mswzkFxe9cR6sU31cUHdFFA-bvSdagLZmbSnafocvn_ha-2J0KMtLiPusZBX_PQfEk4m3zxa5c3SugWDkAFzivKzjDjgNWwwr3wYqPny7-IhKqFlrXXPgHKHgqsD-CrcDPSrLBNPddKY-z2KDU3-Rd0onpwlHnvWLIOmblAKCPGB_VqVM206QeKIAjqdA1iYdBUXQmer7U3HqI8pS03eknobf-6riGItnUAZDsS7c-p18Pk1QKYbmYdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66966">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=QCODCCLiZyVsDpy9ZM4Y-Uek1u35h2nGSFfdnUBx1Xp6eBtOExHZxJJwaJEEVanKCC589FBYW__OGa4UQjz81WzGCuxKba3iUoYz0dGCJ4DBc4OzzrZTZ1mTY4OohaQh0bD_y1M6D8ug6wSwhNbGBqKolXVMERJORDV-OOstC4n4IaKIn69ot3rT21MTUuK_UP_0h6cBpA8bAeR1pzqmhKWybIxoCbz1KfLPnLdFOMXzoHBwkY8-mtF6mxyh9S7algRD8qy313xQDlDdStxCgHCgtJ9bG6L_lLVcPG3mRCbc1BQw5GSXy_8uqU-O_PJ0wccd40csYhLPw6HrYylbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a2e94ef.mp4?token=QCODCCLiZyVsDpy9ZM4Y-Uek1u35h2nGSFfdnUBx1Xp6eBtOExHZxJJwaJEEVanKCC589FBYW__OGa4UQjz81WzGCuxKba3iUoYz0dGCJ4DBc4OzzrZTZ1mTY4OohaQh0bD_y1M6D8ug6wSwhNbGBqKolXVMERJORDV-OOstC4n4IaKIn69ot3rT21MTUuK_UP_0h6cBpA8bAeR1pzqmhKWybIxoCbz1KfLPnLdFOMXzoHBwkY8-mtF6mxyh9S7algRD8qy313xQDlDdStxCgHCgtJ9bG6L_lLVcPG3mRCbc1BQw5GSXy_8uqU-O_PJ0wccd40csYhLPw6HrYylbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66966" target="_blank">📅 07:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66963">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ریدم تو هرچی الجزایریه، دقیقه ۹۳ گل زدن و تیم منتخب ج.ا صعود کرد #hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66963" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66962">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باااازی مساوی شد، دروووود بر شیرمرددددان الجزایرییی، فرزندان برحق رباااح ماجر #hjAly‌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66962" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66961">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ریده شد توش و اتریش زد
😂
با این نتیجه منتخبِ ج.ا صعود می‌کنه #hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66961" target="_blank">📅 07:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66960">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66960" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66959">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Hbcfdde5il5B0uyatE-LcFh8559iDy9BmB8kUsgwz9YWhopdHeuL5gCuxH9XsNlMdWJK8qcoDF35qzqdr8nnMXR9Ab9bEmY0-i_lPq8iZxHfHs4Hdi_yMJJaFJF5f_U_QdAhTEpMdsAY-v1TSV_NbIBcFkRc4pMp0VHeMzgUy8FTQWoMQNyTzugbCMi2QMPoT0Qlg889X9tfVCzyNnrlKPP7N6caKbLEOEbygqCaNnL4hVxf8O6bd2qCwsGaakfHv9LBxbL6YjS2lqFrYTlX6e1G9UplzdGWt2bBQVbtzAp-tVEtDh0zbpQQaiEByStGTxzuFkm8DIihZEBlB35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/66959" target="_blank">📅 06:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66958">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66958" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66957">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qTaYzhQ7hXhw1vW3PnyyyUuKT9E3mfkyw4e2Obf3OI2dlyyFyC7TyhoRenlftuUHREwxPwTF53fnQEgI-pH1xpPtUg2P-C3Xd-nl4gUosoxRLAS9icxGgtJ5DqJZ-8whMrJ0q9_EM8wkpcM3NOEzYoyO6ujoSwEQeCGzHOU-z2hG4wCZe8Ts6dyuZj9RWbBnD2lJiq25gSxcgVbQq4SqMZ8ZGkLBdkvDVh8i3J7M_M-sVC7sTfWGh3JNVro4EQQfwP5DkJCozOmfFCTmUC60LuI747w8km9UPOT1DiCbt3IxfWltOuEKw7YplqPkpIbIpB9HoNcnhTBVsWeRkuOuCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66957" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66956">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
❌
صداوسیما:
جزئیات عملیات امشب نیروی دریایی سپاه علیه دشمن آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66956" target="_blank">📅 02:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66955">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
❌
مقام آمریکایی:
ارتش آمریکا سامانه‌های پدافند هوایی، انبارهای نگهداری پهپاد، موشک‌های کروز، رادارهای هدایت آتش، توانمندی‌های مین‌گذاری و سامانه‌های موشکی زمین به هوا را هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66955" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66954">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات هوایی امشب به اهدافی در ایران به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66954" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66953">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
خبرگزاری مهر:
شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66953" target="_blank">📅 01:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66952">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
نیروهای آمریکایی و بحرینی ۹پهباد ایرانی را که به سمت نیرو‌های آمریکایی در بحرین شلیک شده بود سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66952" target="_blank">📅 01:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66951">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز:
حمله کنونی آمریکا بزرگتر از حمله ای است که دیشب رخ داده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66951" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66950">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A88N4T4pvo_jiBIyW1KhyPdRx0C6lUpWXM1a2eao1yW1Kr-5AfORmQGPxZ5OBV65EQO5H2vPXcEMTvB8u2havJIG6mZ7zSHb-v0sSealZ9v6O3PXhDb4rdR7Ed72CDVXYoh9SRuL_1VykfHW5VKxpXvu5y01oGT2LURVsN6UfK5OubqBFcgPBfsUmA_KeO9urDUcIoubeOj3oVrNrD3z9FFT2FLqWblQ4N9dfcqgGM727QIcv-2MJJC9UGHOh_Kf-e5i07Tmp8ELp9obSYxw0iPoTn1r9BZJXawBYflyV8veLKMBGXrRj32gnFdwsdo6P2vCPyqrEDA1DF_ovTFMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛سنتکام:
پس از حملات دیروز ایالات متحده در پاسخ به حمله ایران به کشتی ام/وی اور لاولی، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند باشد، اما وقتی نیروهایش ساعت ۴:۳۰ صبح به وقت شرق آمریکا یک پهپاد تهاجمی یک‌طرفه را به سمت کشتی ام/تی کیکو شلیک کردند، این فرصت را از دست دادند. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز با بیش از دو میلیون بشکه نفت خام در حال عبور بود.
نیروهای فرماندهی مرکزی ایالات متحده امروز در پاسخ مستقیم به ادامه تجاوز ایران به کشتی‌های تجاری، حملاتی را انجام دادند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و قابلیت‌های مین‌ریزی ایران را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66950" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66949">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
صدای انفجار در سواحل سیریک
دقایقی پیش مردم در سواحل و محدودۀ ساحلی منطقۀ طاهروییه سیریک صدای چند انفجار شنیدند.
همچنین اهالی مسن در قشم نیز از شنیده‌شدن صدای چند انفجار در این منطقه خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66949" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66948">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmYq-4c7nuu38RydXJNJcxrt_2iDNIvonEroP_Iz-uYgDcA3nkvN1SN3B7ZwaeBU_KJA7JURSN9vsWMMGQtnXvykJaqNJiAxc3D3ZGdU-7Li06koLvVlizFZ-LJ5-G7hM3CFsR4TZd_0p_M0K30EM3L5cQoDFipT5m_owQ5bACz8tg-BPoOeej5eLdcaU-FC0uCf1d-rZxtFcjjQxK7b5xr8CpKzfBIPngHiWwY2us-4WgzGW1T5bLolk5IvTIL-8ZlEC0NQpGg2QN6wdkimK1CXCyKLN3AjaqfIOcaZy4cdgmTAz--3h6EYzJvJTbmvuB0AGjD9pfnNKKfbArcmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
باراک راوید اکسیوس:
یک مقام آمریکایی اعلام کرد که ارتش آمریکا در تلافی حمله صبح امروز ایران به یک نفتکش تجاری، در حال انجام حملاتی به اهداف ایرانی در منطقه تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66948" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66946">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما:
شنیده شدن صدای چند انفجار در سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66946" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66945">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDLG4IX43CIeWq0Ioo1OWWTSJNDDFFlYXX3GcSgcivJJmMDvQOhOEMknB9CcF-RyZDX5HpRM2uMuqoNehKTvrelk4qpbt77pNUcM9J946N4epU_kccO03kt3gohmkNDZ391jkXHnlmPH-vqYdLzJp08m6BbgUP1eRp-ze7IlzDSKkBo_ppvzVrdbYOkV_fhzIVQXJO6hbcmAY3RbbaxM7IyyIttRT5NykD2B2KOqS1vsAyb7AuwRTXobvS9b8AIFJs4hp7ZXKGxjAv1Y3ZF6KBKrdJBp95wlBmdhqa3iBDwbZEo_GwxOXMXNblCIx-f0NnTZGUsq0o_TpdvmFd1lgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
به گزارش وال‌استریت ژورنال، یک مقام آمریکایی اعلام کرده است:
🔴
در جریان حمله روز شنبه به بحرین، دو پهپاد ایرانی شناسایی شدند.
🔴
یکی از آن‌ها توسط سامانه‌های پدافند هوایی زمینی سرنگون شد.پهپاد دوم بدون اینکه هدفی را مورد اصابت قرار دهد، در منطقه‌ای دورافتاده از یک فرودگاه به زمین نشست.
🔴
این مقام همچنین مدعی شد که:
یک پهپاد ایرانی به یک نفتکش حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز برخورد کرده است.
🔴
نیروهای آمریکایی نیز دو پهپاد دیگر را که به سمت کشتی‌های تجاری در حرکت بودند، رهگیری و متوقف کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66945" target="_blank">📅 00:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66944">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=vxPILOBHOxgLpYh17lYRHXz70b7RD7jlN5r5yvCRK9hdfvlWmmdNnaYCOwR7KcscWImlAh35Tp88cVHBMCEpPQkm_E5TeP6gug0C3_-w89UyJCvEP75sSMcpxwIsUFtGiQHCIhw27FXSxGuLJjwWknsZ8zz2Hjd4-q_GRPcG1jR6ZTYWxktd60mtMS5iG728Tj1hbk72N7ClWVuMN58T31oe3CUOUXnTHYQH8JMb9pJptBkci-HuOBiFPoIs_WqFH9qC57bRHEPadSnnSl3vpd6Y095lyW1UCCG3QyeROObspfJg-j82VysGTV2acn1plvZTVOEg6y2ARLiFWv_BBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6515f9747.mp4?token=vxPILOBHOxgLpYh17lYRHXz70b7RD7jlN5r5yvCRK9hdfvlWmmdNnaYCOwR7KcscWImlAh35Tp88cVHBMCEpPQkm_E5TeP6gug0C3_-w89UyJCvEP75sSMcpxwIsUFtGiQHCIhw27FXSxGuLJjwWknsZ8zz2Hjd4-q_GRPcG1jR6ZTYWxktd60mtMS5iG728Tj1hbk72N7ClWVuMN58T31oe3CUOUXnTHYQH8JMb9pJptBkci-HuOBiFPoIs_WqFH9qC57bRHEPadSnnSl3vpd6Y095lyW1UCCG3QyeROObspfJg-j82VysGTV2acn1plvZTVOEg6y2ARLiFWv_BBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدئوی مسخره کردن خوشحالی بعد گل آفساید شجاع خلیل‌زاده توسط مصری‌ها به سرعت در فضای مجازی در حال وایرال شدنه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66944" target="_blank">📅 00:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66943">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=VAhixyIDxronvba-TluvJEfVNpmE-h2gMd8t51E7ySBxuOi3IazoFTE4Ra0jsi6N4NtcCfE-ukMqpGjn5UV6Xcu69TshR71voPFiAZDH5iBmpmjFkMr5nfYZep8-f5mmWPbqEmbj7vguvQoaxRalJzaq3uuz70hXTkagy1vcSOiiWuQdHA5luTkbERuXffMukM7YEy3VplpI6ChXsbwPD2u3dHVodU26yh88yFX86w0IwSWKQUBeTbNniaO-s07I5tgng_Uhgm_M82gyIGDvgziy9vv6skiRGDkW8FbAuHfXPzViJZV46SRCu244YDfewjyi7hjS7ivbUKw5jsbD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4f9e086cf.mp4?token=VAhixyIDxronvba-TluvJEfVNpmE-h2gMd8t51E7ySBxuOi3IazoFTE4Ra0jsi6N4NtcCfE-ukMqpGjn5UV6Xcu69TshR71voPFiAZDH5iBmpmjFkMr5nfYZep8-f5mmWPbqEmbj7vguvQoaxRalJzaq3uuz70hXTkagy1vcSOiiWuQdHA5luTkbERuXffMukM7YEy3VplpI6ChXsbwPD2u3dHVodU26yh88yFX86w0IwSWKQUBeTbNniaO-s07I5tgng_Uhgm_M82gyIGDvgziy9vv6skiRGDkW8FbAuHfXPzViJZV46SRCu244YDfewjyi7hjS7ivbUKw5jsbD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
صادق خرازی: یک سرویس اطلاعاتی خارجی مدعی شده کمال خرازی در بیمارستان هدف ترور قرار گرفته!| کمال خرازی را به صورت استنشاقی در بخش عمومی ترور کردند
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66943" target="_blank">📅 00:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66942">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02e1890541.mp4?token=WLM3mIqL8A6IcreADiw_gP8Jn-f4ikkU3nVCD0VbWZGhUcIUmQ39polKVIaEDzKg48qhWNbMrvAzeeoqPAQY5xvmlLuW85FHZ0js1hzKd5vuqJ1R3tFkGYNixJTFVWB-rcmPpa-WDCHQQBi3WDLO4Kgd4crCF97eLc_I6zWdaagzz0Lqhxv0twHt572xzBKVxg89tD9kPQxILxf8IWXyTyqCZ1NIwFR-yd_wNKdnEluLeitYTXaVG7aQXTEg5ERNXRcwyuqyCHU-Ox4Wc5YDKoc0NLiIFGsq8P6ztomdMV_c_8BLw9L0dFRe2nWlXqbyib7Ij0Z9AGqCEvunb_wI7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02e1890541.mp4?token=WLM3mIqL8A6IcreADiw_gP8Jn-f4ikkU3nVCD0VbWZGhUcIUmQ39polKVIaEDzKg48qhWNbMrvAzeeoqPAQY5xvmlLuW85FHZ0js1hzKd5vuqJ1R3tFkGYNixJTFVWB-rcmPpa-WDCHQQBi3WDLO4Kgd4crCF97eLc_I6zWdaagzz0Lqhxv0twHt572xzBKVxg89tD9kPQxILxf8IWXyTyqCZ1NIwFR-yd_wNKdnEluLeitYTXaVG7aQXTEg5ERNXRcwyuqyCHU-Ox4Wc5YDKoc0NLiIFGsq8P6ztomdMV_c_8BLw9L0dFRe2nWlXqbyib7Ij0Z9AGqCEvunb_wI7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف گرفت رو تندروها؛
اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66942" target="_blank">📅 23:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=Hx_TxoR-dBzJ4ymwfbaeIm6wDNRsWDP05iyir88DAGhxkDGzqU3DJTk4SeEEG5bnGjFZYUqXBB5RxLXr3WUahHPKjukP2A9c8swoXkDX-KsEA-RyYAIu51RUJrjQ5WHZsD032kz3UdFJ2RhpwsmuiIHUT5rKUY3gfN_UJoifwMTNZRcXIwcYx0T2hU6wUz5_3J8UarN31dwWQ30KSiezkjiN9LYK7LAwVpeM__d_4fghsngMIcEmur58gUAPuPpKdL91qeVedwx8fc_TkoYgKpvbtSLrDb9zxVsfhs5Pvb6d7rUqF57yyhZzNxuvyoJT_ZLVdZNvXn2AHZMsspkgGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=Hx_TxoR-dBzJ4ymwfbaeIm6wDNRsWDP05iyir88DAGhxkDGzqU3DJTk4SeEEG5bnGjFZYUqXBB5RxLXr3WUahHPKjukP2A9c8swoXkDX-KsEA-RyYAIu51RUJrjQ5WHZsD032kz3UdFJ2RhpwsmuiIHUT5rKUY3gfN_UJoifwMTNZRcXIwcYx0T2hU6wUz5_3J8UarN31dwWQ30KSiezkjiN9LYK7LAwVpeM__d_4fghsngMIcEmur58gUAPuPpKdL91qeVedwx8fc_TkoYgKpvbtSLrDb9zxVsfhs5Pvb6d7rUqF57yyhZzNxuvyoJT_ZLVdZNvXn2AHZMsspkgGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDd767GmzqQRedf5AG22AMJcTDFTOt2ywPgWyAiJlL08ixfGAOVWetWlREVOcSaCZhKGU0sDTLI8RzrWONiomwjUr0lg4IeKHPSEFojU1umT2t8s658ggUWyklXDPtIsEpbd8ISM6xDA49-azNXQj-0WLR8LQvt1nuay3DMCOpgKbSTyvNc0uP_062rvtndDl7ZYOVRPonysw-miQmrFYm_yXtk60477gZxbX8UZggOawwMSYKxTjFdp4cQoFpINzBqHJK3J-hiQjoBh2Q7sMZy-Z5I0neJWYQ_TczVNTeVdLAw4CMt911K7bCP0DIZ5OzwX6VLfXSZj-McfQRgSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nrt6vIlxDysn8OhdGuWyrDVrWQkSgyOIZZx1MxA-cdF5Nf_V1P8PEBNHcuUmTP9cqjLYpXhqNalf_08yJ1URf1p5CR6WC6PzZiEajGv7UNvYbPyEcHKmaSY6bNNNWeqm38YQZE7zar4GyqV_1tONhJGqIx21hdczdK6_sFge0-9v9zZ6SddAcDyAtGoGOyvg6As3xEmmoFQGdy32ak9_gAzM1M566WehqiBQ6juRbJ5Qpqcejonz5ozIEvT93nLU-R4jdpRjUsrB6XQM8leGExx0S92FvOKa_yLVcdkFe8bz2U7asgjDaxSXuZ5LVab14GWrfbZVSpRW-GZW-veZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7jvkLtRps3s36X2tkcb5MvrWJIjO2UAJ_1wrPUWRf3ISOwwX8L7E4pEXMWu_cBq8ofB0oZs4W6Ng640pf101HlCDhQHKMTFAghcIiN_Tv4rsVH-z5eD2Rr2-Q8MDSab4Ek2ArjACGAEcDjU4tUMx6j_k_asR572mVonepl21-hfkQkazaqLEJ2Bfg9G4yW9ZacVPXe-utIx9lYx5zU9GsswERl1UYCnT8Isg8CRGGmTgSc-TrWhrG5qayfAScqujmpYBURX6yV1SIZDNwQPWt1UiVcaZggt6_6MKmOr41NaaNjwSu49cxG3gz2yBrjESDY_OsjQEyi2DUsTQW3vbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9jWTkzZzs0ubTj7s8mNpy0sRQBQbRCwdUcSPuq5e4OwpwruxKLmfRqh5wbIo2yJMmQqKDjRgvEyE6ul65jtCi0vPCjs1OW_pKnKgLGx0osd9kqRGAxKcTyLBJ_W9ZJyKfFm8u6S3sVhyjLKHVQZaAKwH4yFmUCG0EvYBZzfIlOXBwHtzv6lEYJ5NdoGSIvqjUeT_vnQN-Dk884VwRDqy7iZk2NGnPHmscxipkcQe2wjLEpIxFT4cElltxgEaAZc3bJHV7w-XR6BgGFuM5haupvXi3T_pGdJyIQ60gj5rOr6_qlh4agpTIXtBdbMFISeenMtqZ6oOgIRU5m-HjrU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quxvzbJAjYCCk7ecuy_ywPjqHeKQDxqHJ8BVnqc7FkU0kNqinZLdE82eZOMb3FO2eSP7GvPgrB7KXueTDm2OH0s5a24-2YJYyDkpRDS8gN4BDXrW_hDrpgy7warZOTxGUpedHV6ZpJM0LBbnb5zEDI20DfVx0V6vwrudPqfyGBRcEOtm6WQDrFwohpyGsAyq5PpNP7gU-Jwimf5bfVgDRsF8L_5m8pfguFlUN92dK3dbrcrmFkkRhTvgU5p3JpMB3WYUZ3lat2BUEHW3mupHBWG6xCVa25_XRvQj1XFVQDsOT7AVzJrlYo4IHfF--2-kY6hzovOFb3na_x3EJXk5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=i3AYLX4ltcoINkSTW8wWMyde5GPg6gpspowaLYCStUBDmlsYgbvDu4vaxUmMqkxg3JwWJHr93sxU64QpJyGG3ZIc4W7exEKI85MKiSzucQb_4C03Vxy3DJigZw_4ksMFSIi8fEAwWUeteeP7nu6XDjZ3rErl9hcMyyFsb0-58NRPNAyCelVrFYO43oKdQxJmp6zAJgoF2sDrQR9U9f2CnJvk0C9v87RCIfZ_6q49HEzCy6yi6pY8wUiD8VBGHivIPhPcZGjAf4yVqfgnLbp2Fb9Jx4uZ8Bp_av-GFZEc6UNdVj0GfZyxQLPQcx5KcktIQXzgOfYdghygfWGhNwD7aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=i3AYLX4ltcoINkSTW8wWMyde5GPg6gpspowaLYCStUBDmlsYgbvDu4vaxUmMqkxg3JwWJHr93sxU64QpJyGG3ZIc4W7exEKI85MKiSzucQb_4C03Vxy3DJigZw_4ksMFSIi8fEAwWUeteeP7nu6XDjZ3rErl9hcMyyFsb0-58NRPNAyCelVrFYO43oKdQxJmp6zAJgoF2sDrQR9U9f2CnJvk0C9v87RCIfZ_6q49HEzCy6yi6pY8wUiD8VBGHivIPhPcZGjAf4yVqfgnLbp2Fb9Jx4uZ8Bp_av-GFZEc6UNdVj0GfZyxQLPQcx5KcktIQXzgOfYdghygfWGhNwD7aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=RKvNrbRJJZYuFADsCWA8WdUW4Q35hjuZYWdbQ_W9encjw7bznPrnSzrhu1VdaoVQkuSMi2GUmN9q-abn8v125cjm4qVcCsXPXsbGO4rwH5w2QnhNjVxq7To6saQknIoRRu5pcdynI7xyprJ-PQaeQkNQOJob-YbgkKAbMw-GhkmMYgCJYff3lXmRuJojUTHhcUkHvAIEZGPX0xAcFlKAZ_SU08vJ0OnUA9tDUO7cDP3MIoYrB70IU5x7Pg-VvxY3OR4itlexTrRlu51kDV6ZXfL1qGmg8iiqXA7x5AG35WF5DFrlsGZoJB1agHoM5lynbhP5t9B2dt0YSSuEkhiwpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=RKvNrbRJJZYuFADsCWA8WdUW4Q35hjuZYWdbQ_W9encjw7bznPrnSzrhu1VdaoVQkuSMi2GUmN9q-abn8v125cjm4qVcCsXPXsbGO4rwH5w2QnhNjVxq7To6saQknIoRRu5pcdynI7xyprJ-PQaeQkNQOJob-YbgkKAbMw-GhkmMYgCJYff3lXmRuJojUTHhcUkHvAIEZGPX0xAcFlKAZ_SU08vJ0OnUA9tDUO7cDP3MIoYrB70IU5x7Pg-VvxY3OR4itlexTrRlu51kDV6ZXfL1qGmg8iiqXA7x5AG35WF5DFrlsGZoJB1agHoM5lynbhP5t9B2dt0YSSuEkhiwpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=BuncUGel37kD-DxHD0vyxPJY9qhQa3ZdtUm0co9AEdBC-81BCjwLjxr5Xa4JDIUgLezZEWKBCq41cFOWqNNMLQSPAfZIaoiFtlhsHKuHL4kuGsI5G1Yp3TUVXubxL-7sWIsyH9T3dChF-v6iWoYBS4IELjgHOGVZtbh20Ajx9dPXe4attG413B0cMlOD1GVW4yUy5Qt_NvVAwjpI26mGGXyRtkzB3yASRUkkT1XA_N_fbqff73Z90U0XEf-ismAKpG9QlHp4WUiLgcFuhnCqy1jQD8fmBrI83kExmyBira4eYnGc6Z1_W6_mxOKhFd6qT2viKo7we2Jggpc-t1Jcaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=BuncUGel37kD-DxHD0vyxPJY9qhQa3ZdtUm0co9AEdBC-81BCjwLjxr5Xa4JDIUgLezZEWKBCq41cFOWqNNMLQSPAfZIaoiFtlhsHKuHL4kuGsI5G1Yp3TUVXubxL-7sWIsyH9T3dChF-v6iWoYBS4IELjgHOGVZtbh20Ajx9dPXe4attG413B0cMlOD1GVW4yUy5Qt_NvVAwjpI26mGGXyRtkzB3yASRUkkT1XA_N_fbqff73Z90U0XEf-ismAKpG9QlHp4WUiLgcFuhnCqy1jQD8fmBrI83kExmyBira4eYnGc6Z1_W6_mxOKhFd6qT2viKo7we2Jggpc-t1Jcaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krxVMbbD-b9Fwuz5FsKZYNm3kNf1p5lhEfLs70-VF1Kcg2WBkBzfKOssYd6S-PqKQpZtZAGXN1rBW6az7gcvP2VfMV-ADOhTaPteip8aY1MMIz_oaE-bK4qLWJnsbBh1oWAuvUeAlYNKnDowL0AJVZjHiQLVMJeL-QnU3fTpC2onudC2Yu-rl57_R3Ka7wJooaA7zrkae1DiLZ1s8N_eBKt_I7D8afpybqyk2VQFr04OqFZK_flbrl31s0FLIuqS5OKCBeqT0MYg1OOH-WMl_oQLWPf2QIj1w-mrS2CskYHYqNukBhFxyOyfDBdlCO6O8sTZzow5CPtENpsoAzuDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=KxpFhRe-YIhXuHDwdGLE5hcYyt77i1-O109anE2BBx6c0qNjYgNInuLCpHJrEiTxQVMAoY5C306aBxq8ax_vkFuXUNrpT3_qinlPVdUFayt5oakRgfelAaZr2E35mgj10pg_c4zwZFSCB7kTS8jST183pMPAkuDBj3buBXa5S2uL2PTQVdMIDuruTk5gOuZdJ4V-ueeuEBliL6MzSg9lWD1xARNgG6wCPoF5pGW4tIn5LM7SlpdBhEu8yDhCtZVYyldJGteU-IJw8jOzM5EusJMc03acwcApDXZfnQBBi9AV0cEz4n5soAS3rOYKuXIh1YuOKVope7-gij8yLBw1-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=KxpFhRe-YIhXuHDwdGLE5hcYyt77i1-O109anE2BBx6c0qNjYgNInuLCpHJrEiTxQVMAoY5C306aBxq8ax_vkFuXUNrpT3_qinlPVdUFayt5oakRgfelAaZr2E35mgj10pg_c4zwZFSCB7kTS8jST183pMPAkuDBj3buBXa5S2uL2PTQVdMIDuruTk5gOuZdJ4V-ueeuEBliL6MzSg9lWD1xARNgG6wCPoF5pGW4tIn5LM7SlpdBhEu8yDhCtZVYyldJGteU-IJw8jOzM5EusJMc03acwcApDXZfnQBBi9AV0cEz4n5soAS3rOYKuXIh1YuOKVope7-gij8yLBw1-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=ZxiF7__bl8LeOtPsdC1wg_UQZTkwTeIpgINLQSOpTK0YJCRNGNzqKkfBbPGi9MvJf-oK9nmhlZ8ns7KlmWXZAEVxC5vgii7tb0v95DOYWkRjo3cxFfzu0pH0MY0CfK44tQkwmNGgkQ7zXCXzqItYHPSCqQAm5-oHf2LJKhoECxmrZlnYk-KbqCSJJXZIKy9vm7M56onj5uZxjtFRK7y2G5S2pC320-lYaKw38y3r7NR-tuoJhD3cMFO0QMFSOPw1JkElIxiJeq2OCKRF1HieSCdNgfeRH6QcdMte4kRxorKEX9TeQg9E_xgtAk6VDoK5uWxbJtTga4h81xqefvYDdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=ZxiF7__bl8LeOtPsdC1wg_UQZTkwTeIpgINLQSOpTK0YJCRNGNzqKkfBbPGi9MvJf-oK9nmhlZ8ns7KlmWXZAEVxC5vgii7tb0v95DOYWkRjo3cxFfzu0pH0MY0CfK44tQkwmNGgkQ7zXCXzqItYHPSCqQAm5-oHf2LJKhoECxmrZlnYk-KbqCSJJXZIKy9vm7M56onj5uZxjtFRK7y2G5S2pC320-lYaKw38y3r7NR-tuoJhD3cMFO0QMFSOPw1JkElIxiJeq2OCKRF1HieSCdNgfeRH6QcdMte4kRxorKEX9TeQg9E_xgtAk6VDoK5uWxbJtTga4h81xqefvYDdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=Mf4DcsHlONkB121uvyU74yWOXJswlVw6lRHbwOI5-0kRt76vyJP9MIKjgN7uU7n7ah4tu3JNdXSdMTGSucULHrxVMNPHRvlL9VR7OJ7zdcs42oUlDrfWFkpKBZhXlfmTYfVceCFJnj_4-7fTScs_be2hPjlHcuGkrJg0RUUbMguEHzKPc97ZBCXcTu9qMdk6Wgnbistp3R1emfUBLk0fyMaZZFx7yaU6pseHzjiCihHSo6qwEg-b87ZQ4zWfk-uv_WeJybMiJMeuFEJpaKR0CKseHg1y1TZfgviVMWSYYZ9_kLkUWvCIpjIjIm_bFIMVg8cKogsq9bFNHJVmu2qKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=Mf4DcsHlONkB121uvyU74yWOXJswlVw6lRHbwOI5-0kRt76vyJP9MIKjgN7uU7n7ah4tu3JNdXSdMTGSucULHrxVMNPHRvlL9VR7OJ7zdcs42oUlDrfWFkpKBZhXlfmTYfVceCFJnj_4-7fTScs_be2hPjlHcuGkrJg0RUUbMguEHzKPc97ZBCXcTu9qMdk6Wgnbistp3R1emfUBLk0fyMaZZFx7yaU6pseHzjiCihHSo6qwEg-b87ZQ4zWfk-uv_WeJybMiJMeuFEJpaKR0CKseHg1y1TZfgviVMWSYYZ9_kLkUWvCIpjIjIm_bFIMVg8cKogsq9bFNHJVmu2qKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=fb_MpmmDL3DK4FtBWp5E29BZcmIwt0K4bgiTzmN7CNDYQ62gMveKbrw26Ypc-Snq4nOJIu9qBmjVpI1xsR7kIWIhU-pd6gA6RcgUjjmRR3_1ayzTewNio0MVcT_3LBhbal_7PND62FEV51VRwfDHejlB6UGsjQI16ZYj-OUB6LmVCJ_BhLK2_tfMdHQahJIe-HLmIRj_Z7FLhjlgubbITZ2xxt5hoL-I7YDTvizOkGBm_AuRnxCOmfdYWWZfSLaabEmTx4OOFvEJUXgkWa8U59jOf_oJyu-tgCEN6Tso-m-PJudqfARtAjAGxLNQcx7lko88yprwH7tsFIdBcHXnUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=fb_MpmmDL3DK4FtBWp5E29BZcmIwt0K4bgiTzmN7CNDYQ62gMveKbrw26Ypc-Snq4nOJIu9qBmjVpI1xsR7kIWIhU-pd6gA6RcgUjjmRR3_1ayzTewNio0MVcT_3LBhbal_7PND62FEV51VRwfDHejlB6UGsjQI16ZYj-OUB6LmVCJ_BhLK2_tfMdHQahJIe-HLmIRj_Z7FLhjlgubbITZ2xxt5hoL-I7YDTvizOkGBm_AuRnxCOmfdYWWZfSLaabEmTx4OOFvEJUXgkWa8U59jOf_oJyu-tgCEN6Tso-m-PJudqfARtAjAGxLNQcx7lko88yprwH7tsFIdBcHXnUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaqBZ0Yl_ZU9IPiBXlvddH7ojWVukILHJe1z8EVseVIRMUWx20lVlpIzFtbra6hMrnvG9aKD9KJFQmIoRGy5U819BgZXND_FwqpkHwocu_fZLNgA5HqOVRoMDQ-RgCCBpfHvsX8fcVGqFPx0EEeeHxsOk1C-jcI3eVX6WzDm8LM7VaWOWE619sfu0BBpaRjdb4hqkWk6PBTel4e7H7ZJ-L9s9y58Flfiy7AYoFDAIrJ3HSgoqrchjKIVme4vfmfumg9eW8_2Z-1frfY0XZxKHPfqt_BHcolHaijxhr7r2ENchIpmJP2X5_pNXgHrJ2OgOeReeQZw9pscv1if0-Mjkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hm5gILOfIv_JBxPCzELhteLiE4pJwgSxtPd_0H0qHtT4etGD4qG32EUPU569I5wesbbBDG_AmZpVfdiEexjowhDH_tVshZzkD3U1BibYVOMPw-_ktBscSp251F0exS5q5OzKsuo0Llk8Jpa64i1up8DpIGGJWB5S4lvqkRXu-5rWJgmAG9acRwzhZOMrti2jrUEYjHZ12HEL3lVVYCRgn6a0l3pg-3VloFsEaJU_NQJR6Ya9m4OzeK4k3fPf7E9YRJN13xjnnWzhzAxQrNF7_VUbY3vsNiYBOHA3s8sFdpI8a3-_kMzEuff5C0PvDSAgItQjcnT991zgJhcyKekrDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igMZy28Bwhl_JKPHz4TRuIN9fLyvaHF0WtYbbzkukInqJf_hJ1kq7-zFGuIJEUgh9Qo92b6j4iqJbNztaN-uhdvikbGK5sjb2AtMhKbLzJ1PnKOhH3SaHJdZB1GOvXNvCsv9i1CDs5K6MI8ioCg6nTw3JXPxMx3C9DubdjuXZ2BYylLZUZ65UAvJ-L0SKuoz4zu2n7VATsdBCu7_IrxZugFvrza2E7r4uzPou4Rn4ozJICNSAUsYrKsIcdVVk5i2bwq5fZuL6RGuhGwXyS0qL67zU5xdR2srqxDKpq6qUh_ojCNfDxC9MSZj1LXo_DiExBd_DhnGZ83z95iwTKgBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=uS3stVF40d7HcMMVEl2i5pBGCr3Ni-C2lW4-lXj5eGUAiRSoq5j4YYgsM4JRS3Gh5rH3bVmcZg7TvK5fp4EmVHl-T3L-e0B_HNPEj5-AhUhbrN9JDrik3uFJA2WN5lmmQZjYZejLsTEOpQWU6QebPd8xRAizXLEY4brTvnQMD1_OHAeS7iXcou9hUVNVk6x4Z589MU_jFfVGzlPfNihEeKEKrF1n9kOyKC7-6jNBrokbDEKx7KyuLXv4dmuqXMnwyDRdHpLCF-WgGU5TCB6cmy9_7kfRSCfALTOA4rfdWjChpCtDD7EC3oZH5qXamI68KTEnxI9Evle1ACgrdWQ9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=uS3stVF40d7HcMMVEl2i5pBGCr3Ni-C2lW4-lXj5eGUAiRSoq5j4YYgsM4JRS3Gh5rH3bVmcZg7TvK5fp4EmVHl-T3L-e0B_HNPEj5-AhUhbrN9JDrik3uFJA2WN5lmmQZjYZejLsTEOpQWU6QebPd8xRAizXLEY4brTvnQMD1_OHAeS7iXcou9hUVNVk6x4Z589MU_jFfVGzlPfNihEeKEKrF1n9kOyKC7-6jNBrokbDEKx7KyuLXv4dmuqXMnwyDRdHpLCF-WgGU5TCB6cmy9_7kfRSCfALTOA4rfdWjChpCtDD7EC3oZH5qXamI68KTEnxI9Evle1ACgrdWQ9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=HkQlKPAPMKcJeBc5ActjmzB79X9ZUR825JLDx05T_47dJkWtdfmu6IVnm3thOtjpvMDwkPpuB7s56qKFapEYHFDLTHZt2sqM_qfElC8YsV6oKe-ikDhV0A-vHdLnv75U5BgbK5iVz3n2yvpEnMp6yVoUfTxUrLi-EOtoj-obgRB6yTpCQIAWT77XwsjShCqldCRv2Fc7ZUkItp8pNCIcRes4XBMsDvBTVO4r8wtjQYy51-Tbf3E4LwIVGMOfaTswlOIYadUO7yiyRBoktSspJE6yA5J9vUhl9WO7JKIlOq3iLzZTR5gTSVpMx654mhIjkuvonvBQlvb5HYuBlRii-R_VBmPCzWkoAhSVKgM-oj8pidpapw1FYCWcDt-MAB1dsQUsNSHni5GuYzNX33xggNh_K04JeEXxUkFOiRSLfLwTrSnMioJBa26BqPkAtFSoSAec0-BqeJp6KkE7WeiUvLfVTKnxh3Gh-fyfvlwZD4_lkcPaeGKn6lgWXxjyRGgAluye89FJMKtRbszzVJaM3DEdLGmv2v8HmcPzxnvKZ_RGsRZldkPYrsdfgbbaW3YWkB66_KUDia9dSWJye3gU_zlbPDNZUgk6GWlFFjf1IIJ-mbnNNubve4hsjbv3vosiSET46Z7hMWiqcxjDXCe2jv_ReGYBp6HPeXbosGIz9Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=HkQlKPAPMKcJeBc5ActjmzB79X9ZUR825JLDx05T_47dJkWtdfmu6IVnm3thOtjpvMDwkPpuB7s56qKFapEYHFDLTHZt2sqM_qfElC8YsV6oKe-ikDhV0A-vHdLnv75U5BgbK5iVz3n2yvpEnMp6yVoUfTxUrLi-EOtoj-obgRB6yTpCQIAWT77XwsjShCqldCRv2Fc7ZUkItp8pNCIcRes4XBMsDvBTVO4r8wtjQYy51-Tbf3E4LwIVGMOfaTswlOIYadUO7yiyRBoktSspJE6yA5J9vUhl9WO7JKIlOq3iLzZTR5gTSVpMx654mhIjkuvonvBQlvb5HYuBlRii-R_VBmPCzWkoAhSVKgM-oj8pidpapw1FYCWcDt-MAB1dsQUsNSHni5GuYzNX33xggNh_K04JeEXxUkFOiRSLfLwTrSnMioJBa26BqPkAtFSoSAec0-BqeJp6KkE7WeiUvLfVTKnxh3Gh-fyfvlwZD4_lkcPaeGKn6lgWXxjyRGgAluye89FJMKtRbszzVJaM3DEdLGmv2v8HmcPzxnvKZ_RGsRZldkPYrsdfgbbaW3YWkB66_KUDia9dSWJye3gU_zlbPDNZUgk6GWlFFjf1IIJ-mbnNNubve4hsjbv3vosiSET46Z7hMWiqcxjDXCe2jv_ReGYBp6HPeXbosGIz9Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teQUCChxXF8nNjZeJSQ3XqTr3znzmdCegG6BuZ8kRiP5VairixgPYYIE4nMulr7BkznRWgufedFJpBmUh0wvF5np6CQephZtxoqdoghGCYc7XA5n_Y5z43VFvhD90_n-davVNOchEPm53_-i-qgsDhcXxfg-J0hBSyLd0w6gUXSUjA0-SLyGaflTyUSMap_k7tHbjgM56D6OxhAU7S_CpUOYYreq2KbaFoyFma0JmV2L5YtOBetrWaF3OHPr2zYCEzGD83XM2iWF-Gc6e0EvwJoOfc2cxXbLt6e1T22i92cn0EbveTh4LPLSyexPnRxhItie6Wd6N8hir5YUZQbN3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNrtd4k9Fu6cthNvxNPSAK1GkZ9sWnKcCWETs_caJiOy6bH633bkToO7KPHm-vSzWad_FyshMxmI_3y4S0amwY_68rSLsoL94XvIczH_3CwiFAR-47NVj2Exrexcc3ZjfMpc5ISg69dx8H426mqpR1PpzAjzme2ZmRoiRaMnMJpVX35wWU8CiABs5_DQ5u2lKuuI295A4np4jYp--2kjjqJJR8hZbefTxU7iYJ3VTu8LEVrMkD5zTKLjtynPHPhxRHer9Tqgj7oHrpICv9yI-FSDrUC2egNjD4lYXvicpfXDAUW4fIlqUoGrmDSn1bUxSvTjAhBUo8C6rmE6XdoQLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTiKiD508ukznKZx9x2yY15tmlzxQGeAcBXxkkxq3yJK7U9wTQLWvfZ6UJn7mRU5Vpza5Kciy66JA9bLNzhamFrKcHgSP5LDg4q7c3QwQ5L_HznUsMeWzoneMpQ8PPn_r7ff6fGB5yzRgDVHrvehumi7hEbmxqXE75PKcCZUfk92ApHRedTcbFi5L28BwGfoBveifZbGnxSL84tJ_NNQvbgQd68uJecpHvFuf3V73QCWhZaBVI0s45tndVmn1ILFX0WjvpT9PKbEG-cLLZsAOSYZGiBggdK6kNplnE3lgBwMY932hWJFZX6RtfTheSOO_PVxrtwh5GSBm8T2xBSmTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=Mytb51G9YiKGderIiJ8f--M8O7iyXo2-xfur1gEz3bBdPSEcvjdtR09XPCpTHKY-kO78v3XTwYDlzlN66Utx_CAhj57WPRZTslPQMYJzKZKqB0nyilE3Y857jWyGTlKJFX11wnM2Lq5ooJM34SHm82pyQXdYqlNo7cFyu5MlPkWt3CG7BkrXMxkoj1-N2zdpCPlHJIBkZrjsJWwOCjYHdhrbD7mYIO5igNHhKWTTpM1pD3A5RFDohCAsg5dcXerRQk--1UykOYHdR1UWuhAqfQVcTd6iea1JM5VAPv22BrMTBrSzfmbbMV85ME8-BkGX-Di0u2v8acxDCBnU_NSOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=Mytb51G9YiKGderIiJ8f--M8O7iyXo2-xfur1gEz3bBdPSEcvjdtR09XPCpTHKY-kO78v3XTwYDlzlN66Utx_CAhj57WPRZTslPQMYJzKZKqB0nyilE3Y857jWyGTlKJFX11wnM2Lq5ooJM34SHm82pyQXdYqlNo7cFyu5MlPkWt3CG7BkrXMxkoj1-N2zdpCPlHJIBkZrjsJWwOCjYHdhrbD7mYIO5igNHhKWTTpM1pD3A5RFDohCAsg5dcXerRQk--1UykOYHdR1UWuhAqfQVcTd6iea1JM5VAPv22BrMTBrSzfmbbMV85ME8-BkGX-Di0u2v8acxDCBnU_NSOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4gfQiorcSJOgA9ws2tEqe3k6Vd-S9fsWM7XxILIqcYpz7gLnf5hOJM0rQ5nbeIyhQWlYEapV4Qw2jrYKiDy8do0H5dwQuyELac8FhGik5jnYCZjZBV7cZbCKWZ239dO34-iHNbc7skUDisOOl1yjD2bXNFKeLjAV-Q5lSVC8qoZWNXY3BMQxVcl4HC3V4f-V0AUR82qlqWg2PRt4D-v7nFTuR96G8b7mLNzDJUvz3xEKX4ayBfao2-CN9xEnSqrEKrlBLr7Wx9K0F-b_NDTPOlXXH6YuuE9YIswCGilYhARKWBwjlOBmQS2IEdrLDcI3bFdfhYRYrCOfZC26aBKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=AuU2N9WqovH8MFDbMPqY7TPNhHyIdP7i-e9tYz0k_atCbgsyFNVzNn4xj15TMzGS4hxvT4R2QBbP51wejLzX0V2G35LvwnCUc6nBlw-3mQXx7oA1-fiDW3ETxAL_nOtzNAv-3-HPP_dhUWmBC-NXlA1hGQey6ut4WwA96qzkB_-uP2zcKBceOpUl6QLKHWxRFWspRPaUNrgbts64mJV-xVNAuGMzKgpkm9-A7S0rF_3aXGhYIzSFsbh5bl4Ek_gkekZLPfxwRo4Ujd6CYwCSecunb0DEd18XMvFP40l66u8iPP0mR698-Sal4W58zTCofSw3sZmCRPA7VCwRCMYM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=AuU2N9WqovH8MFDbMPqY7TPNhHyIdP7i-e9tYz0k_atCbgsyFNVzNn4xj15TMzGS4hxvT4R2QBbP51wejLzX0V2G35LvwnCUc6nBlw-3mQXx7oA1-fiDW3ETxAL_nOtzNAv-3-HPP_dhUWmBC-NXlA1hGQey6ut4WwA96qzkB_-uP2zcKBceOpUl6QLKHWxRFWspRPaUNrgbts64mJV-xVNAuGMzKgpkm9-A7S0rF_3aXGhYIzSFsbh5bl4Ek_gkekZLPfxwRo4Ujd6CYwCSecunb0DEd18XMvFP40l66u8iPP0mR698-Sal4W58zTCofSw3sZmCRPA7VCwRCMYM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=WJioABpIZNw9-s3QXG5Fgkgg7wom6YWl104re4bRJLXifTVnDLnrba2vIo5pyxSnjaFtaS_FTQ9V8qDPY-ehB0hWA0OwuY16kuDfrmAFDcyGYEjpzgnwHLgZjWDktDZD-A-NlJvXKzH2YwZGqwrp8CGY37oCw89aKX6f4tvOrLKzxpVsChhSLzAK2g3Ra7Yp59-3d5RmC4ZR_54YbX3-fZEaLu2gEJbYbH2ykOvzCfVeimul4KIn4ymRahAg_w4xpWGSXYlUIE2B05VV3Ioi6xvXOqQcTgS0l1au6fpwh3B1yYMEMKGNQvXcDCMu35kGsaXT3B-6wslbcmTzpqLC9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=WJioABpIZNw9-s3QXG5Fgkgg7wom6YWl104re4bRJLXifTVnDLnrba2vIo5pyxSnjaFtaS_FTQ9V8qDPY-ehB0hWA0OwuY16kuDfrmAFDcyGYEjpzgnwHLgZjWDktDZD-A-NlJvXKzH2YwZGqwrp8CGY37oCw89aKX6f4tvOrLKzxpVsChhSLzAK2g3Ra7Yp59-3d5RmC4ZR_54YbX3-fZEaLu2gEJbYbH2ykOvzCfVeimul4KIn4ymRahAg_w4xpWGSXYlUIE2B05VV3Ioi6xvXOqQcTgS0l1au6fpwh3B1yYMEMKGNQvXcDCMu35kGsaXT3B-6wslbcmTzpqLC9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=Y4w2pizqjt6nXjJb98IX1ueEuqagP4VAoO-aZqMMqqA0dxV6IqNYPyuMQzbr5PRPUztkKpqGRRjztNrPwl3dmqLkr4xGxUwgdHT-j9HDvliq8tPBpEUT79yl9D9PcFrIOTJsH1Hrz3PTdYXN8FUYeY_LlQtLvvzn_0arAI_tz6cX0ndvYkXm4GMYBaWjYUcHljmO9xhZPeJZcz-ChgNd7PwuFWtZsyrn7DLqLukAnd83feyy5T2CjEbC8wevL-a38Haf7J3uiKfoJPhRiFImQRi9g2O0AaJLJejNYYxSBW6SylMZV1-aop485-Be6sd4xC1VE7qzq6yuYad2ISO3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=Y4w2pizqjt6nXjJb98IX1ueEuqagP4VAoO-aZqMMqqA0dxV6IqNYPyuMQzbr5PRPUztkKpqGRRjztNrPwl3dmqLkr4xGxUwgdHT-j9HDvliq8tPBpEUT79yl9D9PcFrIOTJsH1Hrz3PTdYXN8FUYeY_LlQtLvvzn_0arAI_tz6cX0ndvYkXm4GMYBaWjYUcHljmO9xhZPeJZcz-ChgNd7PwuFWtZsyrn7DLqLukAnd83feyy5T2CjEbC8wevL-a38Haf7J3uiKfoJPhRiFImQRi9g2O0AaJLJejNYYxSBW6SylMZV1-aop485-Be6sd4xC1VE7qzq6yuYad2ISO3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sNX4BvdkpjaNYpdzdsZ9wgf9fQf3Y5D290qOM3tc3PqgEcsqBf2ecklx0WogLNMVFO8N-VOBV2KaeNrnaRQ71pOXWhgN9v2XrBvQy48etklRoxfF-Ab9x2bZzql-4qbcWV5GBGsEKfUIX32wdp9PW77H7Oa0Mb2h5JwxuEZ1L7SoMORPAkzEecVsXnd2XYakcmtl_O9PrV7_nVWggtINjC_VUEJNTwyM_qmkj7HnL3I3Glmz8u2acrZ1IPr4KIBUXYSHxa8Krs7235CoN_sGyP_L-1wVIsPjC0QkBZTOL0vCmzGpsUTbBC1l_EL-0D4n8MLE-8T8SDROH_w4TpDA_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=mvK8cR_8Y4XiMZJ38wpG0pC13_v-HEJdt4JlC5TLIRC9n85eECMNksKmhvYjKqcDX1ukb7P2ZMWprLzfHUvtOD4LuspofBwhzHdzcOK5LItcF-PNbuysSNe01ZRI-tkcdIQIzdyvyZ4X_5GuoDzEXCXQyxq-7wk5vHMAFdAhwLdcFqQN8po5_nYCcN0FxyQ0LBwzJ2SNb59idVC_kgoXwSZdvp51JnUwdKwz5iGKkSCcIPw48fpqQu-iLldrpag_SlNM-i7z7HBJYqigE3sFL5YsnUbfOFiYZL7SDCYiHQ8j7nzEIRTdARCGTKkgAgh89uUSuKdzixEMCvSphrKMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=mvK8cR_8Y4XiMZJ38wpG0pC13_v-HEJdt4JlC5TLIRC9n85eECMNksKmhvYjKqcDX1ukb7P2ZMWprLzfHUvtOD4LuspofBwhzHdzcOK5LItcF-PNbuysSNe01ZRI-tkcdIQIzdyvyZ4X_5GuoDzEXCXQyxq-7wk5vHMAFdAhwLdcFqQN8po5_nYCcN0FxyQ0LBwzJ2SNb59idVC_kgoXwSZdvp51JnUwdKwz5iGKkSCcIPw48fpqQu-iLldrpag_SlNM-i7z7HBJYqigE3sFL5YsnUbfOFiYZL7SDCYiHQ8j7nzEIRTdARCGTKkgAgh89uUSuKdzixEMCvSphrKMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMEaCq8PaJRzvsoqUUyzGPrZnndUKJ9IVnKQIxD02Ue9OBVcAHwOrWWQ9IaCMbMTTnaZ_ITEwaGuFzAYS08nDqCDrR1Qh_IItPzlvwldxxK-lXHPtgOFRJs4GfGaJnds4BYIC0ebd9huC9imsNJs8W8j9aaGgx88SAobW2myguIEFbINQTOkLXRY2huL-DEsI9Xcyu53RCHAmsf1pY7xnddA0vzjpExlj4fhCNgy1J2xWt05r10YDIoAyqL4uvfsdKPZIsHJ0MzKJgJskgjTfroES6zgN04uI33yOfBtxvLb8cMdrnt0qiNiQ-9-5f9o8iyEp6q5XI4nw5Qa7NCs9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=U699_LRa-1afBISUucSPitiH4F-u_9M5ADLGbDWjYb6z2LFnTcKLrFolfv1lvCyukn-5Qiqs1w7SPayJo3KVpdaHEjVM8opbatjRt3PcULptByvHoHr0gvZGAW37qigeZYb2ARxfu9KB2WAzl1WaGJLpluCR1lVtBN8pM6mw2QOtuvJ1D2PzHS5VxNjaZol47tjW4UH2cMD18l6UzPiNDpnWppMnuzDcSJf9gaoNVzk8lkovZ7gVORjGBHNTQSiY-gSS9rPqLTQb_qnxc2XnUQ28ViT968yr8Nn_iDY47XpCtwU77gIr5qw-KHy_kM3qIgV2OhZ5rsRDVl_7E22g7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=U699_LRa-1afBISUucSPitiH4F-u_9M5ADLGbDWjYb6z2LFnTcKLrFolfv1lvCyukn-5Qiqs1w7SPayJo3KVpdaHEjVM8opbatjRt3PcULptByvHoHr0gvZGAW37qigeZYb2ARxfu9KB2WAzl1WaGJLpluCR1lVtBN8pM6mw2QOtuvJ1D2PzHS5VxNjaZol47tjW4UH2cMD18l6UzPiNDpnWppMnuzDcSJf9gaoNVzk8lkovZ7gVORjGBHNTQSiY-gSS9rPqLTQb_qnxc2XnUQ28ViT968yr8Nn_iDY47XpCtwU77gIr5qw-KHy_kM3qIgV2OhZ5rsRDVl_7E22g7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRXqboyCIdZ98YOasVH7Xve3iORw73Xi3md7JP7EgMwqIIW4Xgc0NHvvJ7r-_hU3pJl9YywFXGnzFwn9E9nfsJDEK4A7uZRc_Y6H-coQvUxAOJdilshzyKLyrGGs5_bw1q3msegzZMz573TFW200EdLvuXwat1Y7eUTjpNKV0Syd4lml9AKB0tHT2P4P_t90AuXoysjs8T0PUAO0dzEXzzuJDaEYH49u--yt8AuJn5_3p8CpjHYySDl8PEs5ZNW2KUXvneUyXJALMG1biU1Vv8K8XzpILSzbdk99MAKlqx16M41z0Gw_Ody8-MgL1tXIJHqVFhBUN0NDPTnzFleWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=jiQZ_J5P4-S-nTs5jniVbDeOBdWWgRrQP9azZ_LpK98lw2ByydQ1ilkQlH06nTxO7BoX7o3UwHBM2qmJX7rnKOsPnOLmrJSMcFmgHOtlP5b7a0Up48NNzMAVj9yrzZM0IMpoVqHjU8QGKCqY7_E-MKF4QUF6qpZFqJC_yHllYLh65InuMcb-DISc4o_m0O821myDBsK1faUnUy9kLXf3-QDD1I5pIuOa4RR_2Io8nTX1q1n3u_7neBifIldrRfXrG8p67v_nQw3ggq7TV7UPLsigOrMAnP_T4Ly6tsAvfYrBRgjwbV-c4Rp9WNoWXiIftBp33s9OAnzB-dqF9H3c4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=jiQZ_J5P4-S-nTs5jniVbDeOBdWWgRrQP9azZ_LpK98lw2ByydQ1ilkQlH06nTxO7BoX7o3UwHBM2qmJX7rnKOsPnOLmrJSMcFmgHOtlP5b7a0Up48NNzMAVj9yrzZM0IMpoVqHjU8QGKCqY7_E-MKF4QUF6qpZFqJC_yHllYLh65InuMcb-DISc4o_m0O821myDBsK1faUnUy9kLXf3-QDD1I5pIuOa4RR_2Io8nTX1q1n3u_7neBifIldrRfXrG8p67v_nQw3ggq7TV7UPLsigOrMAnP_T4Ly6tsAvfYrBRgjwbV-c4Rp9WNoWXiIftBp33s9OAnzB-dqF9H3c4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=nkd9dAfCNbqpYNS2L9wFUxGqcZXv4SYZVfsadNBpQ4LCv6iLeLhamCQJc5MeRY3gVBaB10mqKNL9zu0BwK5FsaIyqC5ZnRhwf7y0tU0t0uOFiTSDBWv9_6KKwypPgeEtOqhGNdlC9R7-CymN7PXyJ6p6XsWqtRB2bb7O1dFD1srWPbH4wBCxNQ0krwCmARWHARY_18NU-E8F1d5arrVBNyzCUF_ARhvsSBf0sSVM7HjxJlUtOT6HlfGo5OA4hlXwuJXuaGwfYHs0CB8PwbdPmHzjcZBaz2U3s4G2LAxjJVNZEwDCFWajzKCOGvcE1AowA9tGPbR6x9NciTIq1qUUKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=nkd9dAfCNbqpYNS2L9wFUxGqcZXv4SYZVfsadNBpQ4LCv6iLeLhamCQJc5MeRY3gVBaB10mqKNL9zu0BwK5FsaIyqC5ZnRhwf7y0tU0t0uOFiTSDBWv9_6KKwypPgeEtOqhGNdlC9R7-CymN7PXyJ6p6XsWqtRB2bb7O1dFD1srWPbH4wBCxNQ0krwCmARWHARY_18NU-E8F1d5arrVBNyzCUF_ARhvsSBf0sSVM7HjxJlUtOT6HlfGo5OA4hlXwuJXuaGwfYHs0CB8PwbdPmHzjcZBaz2U3s4G2LAxjJVNZEwDCFWajzKCOGvcE1AowA9tGPbR6x9NciTIq1qUUKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhQAu3aNh2TpkOt54KKs0MKpGFonUNJtUS49M6_oVWdKFWpT1Cw_T2_hYMouB0XviZio3Xs1AkE9z_IQ80GzadwgEPjXPCbfJJfUkuf-zOxP7zOcehctlVGKLbKQqSv-Qje0DyeXOH4ps4oMeLkP2Ee9q-kPgbAYil0Rp6-ggm9zZstVTccV5KhbfgETPxA4sBTIbj1qL1f6rt-EB1WIzDTnWwvTg_UsU9e54tKQejBVtjmDzYWZ0y91LH2ARix3TdxDwgch24AZ8ifiz8vILcveiqK21Ew3fxXRkZjoCJrK_3m-Pxu9uLBB3YdGnoKVc127AWxVQFtmuOtmYfIOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=sUGkcMXu5J--4LXxJTCXg3XAPoK52xVpebaKR7Fh_U4v9tHrCTipadXS9v3CmmaAJBzuscvTQUtI2PzdLkDL8gxRk1NLh9OH-REUCUKvAPxwFd_ng9D4HBDqrAV5iWhYushSbvIccqPWcOV6gyihNPW5yHB7GwOHT2ohdzDXW487OzEcWn6s_Zhnpjd-zq4arjOrpOqODfllxyRGj8eOZBTu70vqGG1521TSl9IXur5qxnbMX5o3AbslNQWVpWLfI-8zfKbWG3AlpDcl7Fr8YyDzmDm8HWQKrHTLMKj2dhGORyauUtWUMrtFmIK_OgJOrFpV_u6N5XeGoC43iwMzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=sUGkcMXu5J--4LXxJTCXg3XAPoK52xVpebaKR7Fh_U4v9tHrCTipadXS9v3CmmaAJBzuscvTQUtI2PzdLkDL8gxRk1NLh9OH-REUCUKvAPxwFd_ng9D4HBDqrAV5iWhYushSbvIccqPWcOV6gyihNPW5yHB7GwOHT2ohdzDXW487OzEcWn6s_Zhnpjd-zq4arjOrpOqODfllxyRGj8eOZBTu70vqGG1521TSl9IXur5qxnbMX5o3AbslNQWVpWLfI-8zfKbWG3AlpDcl7Fr8YyDzmDm8HWQKrHTLMKj2dhGORyauUtWUMrtFmIK_OgJOrFpV_u6N5XeGoC43iwMzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIEPpUpV7KA2Qa2lAmRXzsh227ZcXzM_9btxs1detdyqadbU6j3b6iozziQGz14ppknbA0RAEHZaKWg12-u35Dp1e5OY6nfw_pluFO7hrrs_BkoszxJU1sIiPI-79mFjSCvLs2Ns_alFRAVgdhg0AiTi59fc51uB7KA2pPmzLbgaLJhiIL0t-d3K68QKt8EA_wTC89QrH_svDdKK83hr-aMWfuUGsRP9dIm8LRG9nYAxn5FQzAoMOn_fvFwkVPwovM9FvyOcT8ERhjKlPpCLQ_yTV_IrpozdpI5IE1QEQx5_sTWz5kaZqUyY4MOlNfTIrw5s0aVa02E5Yz9w9MVTaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=I5GPMwvr66L9ZjdMB0QPvvhzeh5AwcylZQIq-8cjjmuVflkE_6-VzCR4Ju3UKAFOXjZnMrB3AFmCA_1JQWvwEEa5fu8cC6mmMWdtpARlcTOvebvmkqcoCjMtUAGGFIlA28H8U1vYUI-PaBi2nDSHdFmMGZy_n1zz19zR6ZKx_Bfl9YCMYsaXt7eyvOzsf9Bod4dqodXffqHLFldkKV05kSZ2Y7-D6BOGo_fej5MUXz8paW9ZUg9QhyLvOdvzVrXwkhRCVHwpBeUvjsZNB_AVTquUghIYKWSttrsC8bd5e0_zDFSwitQaGYvhu1IX7nMay-mvTlbuuMqURK9XY5N1pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=I5GPMwvr66L9ZjdMB0QPvvhzeh5AwcylZQIq-8cjjmuVflkE_6-VzCR4Ju3UKAFOXjZnMrB3AFmCA_1JQWvwEEa5fu8cC6mmMWdtpARlcTOvebvmkqcoCjMtUAGGFIlA28H8U1vYUI-PaBi2nDSHdFmMGZy_n1zz19zR6ZKx_Bfl9YCMYsaXt7eyvOzsf9Bod4dqodXffqHLFldkKV05kSZ2Y7-D6BOGo_fej5MUXz8paW9ZUg9QhyLvOdvzVrXwkhRCVHwpBeUvjsZNB_AVTquUghIYKWSttrsC8bd5e0_zDFSwitQaGYvhu1IX7nMay-mvTlbuuMqURK9XY5N1pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPZBiF8qAEn8J3GiRaKurJYyjyQffAEXe3qSNTw2-mbSdt0nMo2Q1GsTthZ2Tr1rStwlQv32sw6lsCIN0mVY71AYIATRDsjj06u6aNl5xTrJv4G9vuOv5scKVoKI-DuXAN40jXaNtZrp6VnzCOF-BtbpMmUdwalUm980g2rjc8jPlAhPHJ_hGYGTmCqznX3tic3Gzzu_Ri2IgM8_beiLHig1msX6npWjPQ13L0h49296dekDzOIuWhajMExPlNMAbwB1BWt1hHHUGd6PzSGl_1BC51tFfwymZNBPHJLubZdH15CtHWkRH269nybeyqKTLlI4U_ccNhFZT4E71yXcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSqyhIW5LAng_xKfe7w5eLJlNMUSJ7LCQj8Y-0-yc_v1wG5DUDruSqz27ByGF12qgd4jzkL0pOT2lUM3LJcf7lgKgwhgKk82RinE_71gzriaFgFtOULyOhfkN_9A5FNPJJDHbWR5lFYKQAEaPuhNq1CsbN2J9gWAq6Q-WVUn92o1w6Xux7xU6mrNB05ontb1jP7hvLw1gPvjz8_ZZNRnketicutVJNeuxpGsyEsTQt4HCRAqYEsIC3jRZDpNPhjqszqLkYYPlRMKAA5SYBMqE-h8gZNVT-Yosi0CWlan583c2DuDvDi55OYU8A8yUO_5P00khwGRPg94VA2gJH3NTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KDkSjQ2FhO54YU0BKSaEmyRRnWHYutMlKO-h0W0QevKzBBCLN8_kyn6EdI-iyFnjAHh_5rGMiDR59L0rD6oq8ANn8Jo5zFknQrknjVf7jaN_j_Ir2obS6uVCSGGM1qu5fjM47ssuHF3umnDpwyoDY3BfEa3hf3qonsgNyZTIifHP02scpFIizyItlzWhI-0xMokivuLY8nSEvPla-nsx40rxAnrzrRojR0qksXc-Dh2cTEJKktKZglR17A84OAxVZZ6VTk6rVVV2gBDHJ2aerCfGL54UzdcUH-pI3pFIdW7E1HLGT5ToXz8mGQs7ZHd6M1zoTU0FTN5hX6oiFzs57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAtw_z9pm8QSQ1vJ19YNy6b3FKSkjZMz3PAqJGHlFjQ852qF72auWVhwUZpgji4l6fU-CkfReXa0AYRcssKssgMTtGMsLvFgGDmRrak91WEiWfCu1J1MojndL77F_pWw3I3p5t051yEktB9e35reR6mHgwerkmCJvK0oEAXoLQ6gUlZAlMvFPD9gO05tBJV0mUa2rubc6aZavQnuYAOGTx1zOvW_cfCIsosCix2IUOpAQ2QI1mDM5B0SGQ85q2UsXwXDfLQ_Z1Dz_lMzi20KEQN-0fcjcrFjM2snwcFeYTUwcGnEkBMm9WHlJkxWlNpXPvMLZKuKxHmSHGiBK18pmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3I9ZLntyZ1R-Ak9XcGW6Gpp7Xaila4tUk__ZA3z4xEdsBuCRs6GPeTJIJL4xmxc0run4zQXmYHpMk0zHZrJIFkBrgAlkRxwSwX1zLJ3cXHkm78IkhZSa7kkTAhaE0b5fevpZdTk8yg0NVPuQPibKQba_q7f73G5kr631RtB9309Uah3erpgj60UrSrBstszp9r2MtC-mqA_umIqO5D6Q5rbGeORtzI13RX3-dypbDkfBMNmx9Fz9MMFxs-fhOaeEBaTpEjleskdZCSnIpUEuQy3-jTDTUaatIiIst1I1w8E1Ze2DItElHCpEHyScSSogsTq7OvRuo4He3JjuTxJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5RVnlJhmwdlcmmu4swl1nEaAbcaLd15vCJ6wSkXP4ENAakBw0yVKkIhm6ZErNfSCp1d73FIan1aqif0Df0eoBumQerxNx7ecGWAIRpK8mIYg59aHZ_PuykQEYKdaKw4sLPwTHQXS1m810TjnmkVNVizUfUSNrYQ5tiWUuBJjT-LuE9nh6aaqmrlXyZeWctRRIBTSJehIBv1fUKCoIhgQKYP8F1jqGtu9qU5VmqK7wni7cXaswpYTKQZTKTZePstHviwBY6zUiV2i4spvu2F-zL7mOwJpdwJhBjh6yRLLe1Ck9mWxwgVSMCDkYo_4-SDj2EgYFvMZBgAn0e9KqBomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
