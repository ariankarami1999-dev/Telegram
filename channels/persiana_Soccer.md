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
<img src="https://cdn4.telesco.pe/file/hpFo2wrsVScXtoLNBn4KgqatEA8M7NqeZ3xD9aaDmuo5kRVjzTjZ3u2Bg0i1aN9pxpQFX0w_3cLK_Fz2mO8xB4kncKvmG_JajoJ4ZRzVLoFbdr_KTR5dLLgu7kB_wpCdBKwgdtB342-rqcijAR_0NFfPB7Zi_cxfTYB2BnQkpk3-Knnn0Z6mmbcUN73u-Mi35dJaLbzpmy3HZtMsRreqwPQwHTaJGiBIL9MYVpm8qs2EP18mAQTPd4nbS0sO3W8h-14PberAHR3Ja3rj7zVTel388fxbDpficzBVu7JwYCH108nYLAB6MHThSCNpCHR59FvHy6orjsgpqFB_JWXCjA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 293K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-23525">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-nbenO_QxqIskf2QKi85qx5Eb506rPKunWpbq8WavMPwocmPboqFfndMO6keb1rjLZ2c4yVEwxfb-5wG2f1tb_IA2Ph05An1uKS8wS37exozMF-JfrDR7_ScnCVXtOfIMmMokaiblKzeslyWr2JqkpgNMsNX3oos0bX1LQKSvr1VCQSM4czfzxQcB_i-fClRCXQLA6VFVf0uP3qk7cXjYw0aAQEHdjE07HkYgh7CucfYL9dbzG21GT909QHYSe7pcfr9SwUP6TGvKKOX9hTOzbpqAwjehMkODAihEWRq7fIdlquuPvShK6_M7tlqHoGfeeFuO3tLW8sjSjF-wKbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعداز پائولو دیبالا؛ دین‌هویسن دفاع رئال مادرید هم درویژه برنامه‌عادل‌فردوسی‌پور حضور پیدا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/persiana_Soccer/23525" target="_blank">📅 18:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23524">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=YBeePY5JOP8G0ZTD1vLs25nLqX1tEJ_6zoxFMGK52mqf9gLVS1Q3oxLbJ_hgPqAkTGbLKzCBVSu2gyhXQ4JTeuM2fSgxIgJSPD3Ws3ToYq3vgadhYPON5HUvEaey4yeDBw4IiDDGwMsm6LKBCqQrasghtYdaHFCRQydw5oj7lQpDS3hS9XBNrpDMlQTvtJn5UqCT1FViWyA2U-e4X4ALJv_dRNSbMas7MvvEgUJxHhsitpC2UbNx9W-vhBBpnOxUcFF88_Yp8aUdD-P37zJr7qrvN1vMxcWM1c2Pi75NkC_1uTeJQ1OWgqGbKpqhdkWITRm87AMVfzfliWviXrZ2wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bca14044.mp4?token=YBeePY5JOP8G0ZTD1vLs25nLqX1tEJ_6zoxFMGK52mqf9gLVS1Q3oxLbJ_hgPqAkTGbLKzCBVSu2gyhXQ4JTeuM2fSgxIgJSPD3Ws3ToYq3vgadhYPON5HUvEaey4yeDBw4IiDDGwMsm6LKBCqQrasghtYdaHFCRQydw5oj7lQpDS3hS9XBNrpDMlQTvtJn5UqCT1FViWyA2U-e4X4ALJv_dRNSbMas7MvvEgUJxHhsitpC2UbNx9W-vhBBpnOxUcFF88_Yp8aUdD-P37zJr7qrvN1vMxcWM1c2Pi75NkC_1uTeJQ1OWgqGbKpqhdkWITRm87AMVfzfliWviXrZ2wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇹🇷
آردا گولر ستاره تیم ملی ترکیه پیش از آغاز بازی با استرالیا خطاب‌به‌هم‌تیمی‌هاش: یالا ما ازشون قویتریم؛ بیاید این رو از دقیقه 1 بهشون ثابت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23524" target="_blank">📅 17:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23523">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe_ZzfzUswSNNeD4H0NZdwwC14vjTAiVB1xo6JWbjJ7k36041t5OIaJPfOjZFyyXfJ56eA-Aljdr08NIC8AGqJTEYdArjVhBIIZwp26SgtfwRELSmmkTaHBbSvlgqru2xqn9RsMQpynz2thBk2k97M6f1WDLACHBT4Pzbh5ipV45r2wbNJ13byIXEUYut2qUNsfH5Ull0_wo0AD3DyPwr4uQo1zw7Ed8ngq9yyAcvAu6wvcya8Vky6QGHfmcnZwIx3Vjrfd6U6oszAclg3nuAeVxUnIMhy3ksOqWTwDfAAX-H86e_HUnnrXkmrjcS_EIHmU2RASCIKWnvp1uhpHFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/23523" target="_blank">📅 17:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23522">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk-BuEWiqlqvUpEekMzKL_a2t_kDXylWXIfU1i95FKElbVU7UaCbKtiD24GcYRaghpNITnc5r6ngDLQfY9CH-B19uzRyg0lbiA5OvbDcQ7_LdJ1ZpMuRgWI3ARiZY5vNDwlRmlROPSPgdYSHNyMClA7Hx2yDKjBhLAIXWL1mfX-dgpRP-UfzPTQvJn3K6lyNnD4fc1VYzZxj9nIvnk9J2uh0pktfDiljHxnsHL-2W_RRTRovLwp4jkBjPl19gAaYhtsn-1XtEmiFBZr7RGsGCjtZpAg6-gpT5T3SmunpM7Q1zuCmMgFKdMroTcqlqyub7Pjt68uQqkDJFpai-FNd6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23522" target="_blank">📅 17:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23521">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiuljDd4_36nRimsfwQb55t2W_kxwIvW70LHX6cxr-2eCK2F1zVNDDl4KM19DWRzbivoTFR4unViJ62BvaIZTr0pOcta8hd0uonFfyOTX1o3uF-8Y9yJ9Is7LJKqEL-rIyOBj6b-9Z9rUfUrIL-_ggxxlvmPnOlECt0M68vr8c2bFRrFNBXTA8jHM1PM-jDgBzay9-7iwGTsaT9hQdkVZmHjBltr1O9VxFHuzn_f2drXZtYK9AsovBwmXL5tgzJqgBJJhBTP3uQP4iSNjqjbJEeTL7gLK0m4YB0jvqSuqxozk9Qye_iU5vN3QCoGPb3hClxAnDrzWbiHpS9KZgG15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های دیدار جذاب امشب دو تیم ملی آلمان
🆚
کوراسائو در هفته نخست رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/23521" target="_blank">📅 17:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23520">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=GJa8oFrBry7OzQsbR4NZQKPn1Z_qdYvUrgsSP4ugD1rmFbpJBlWBPZYsojx8ChL7tRv-kO13-YeKzTmoGQkRM3XqNIJ0c-Ho0zfFFyu_Co14a9gddmRLGy_lrPPNl-18EWJRQuOwbM_JVyKkJjhuSxzRS80fOp0DIT_lncKfH8Nu-OObOOFP3Ujp9w7rGLROx8nwy8cidaXgORHwD56jhHgM865yHLvsx5RAMUtcSqewdd2Mra7xhLHqc9LFr4QF6zinWO3wdJANqwwjJopFa6Q0VvoBphk-nXX9OdllP5UMWq5RFMkZUgTj4aQgiivqqZ1WKKac1DcNJiQaPwDwIw2CJW_1BwKuEUxyQTyTheN0WERH30ZLrezbQSdjLAKWAGmp0RZ_6DzsTI0ekfo7UWeS2tLZu0GKEgjCqVi1R27Q5QY83pemQ9stcvAZ-QbXIv2EKbwdnJAOmF3Ilux4RWAPZu9Nhe7__kWyP5KTM-sHuei83P3GQUayPDMzpoWbK5ESxgfjXPj2JoKyZGFvZsLke_9dnR-1TQszlHMJLGS11D0noLeWARrO1sv8fMPNGiSC8c3cvRqwk80ouPkFgQsL1s2ynyZ7o2AY4cLVPZmiBsAm2dUPqZEtfKD5OeIP4QdD5IiQtLysXOAy5Cag7_8XUaI7N7FZpS3UTo70CVE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7870ebb64.mp4?token=GJa8oFrBry7OzQsbR4NZQKPn1Z_qdYvUrgsSP4ugD1rmFbpJBlWBPZYsojx8ChL7tRv-kO13-YeKzTmoGQkRM3XqNIJ0c-Ho0zfFFyu_Co14a9gddmRLGy_lrPPNl-18EWJRQuOwbM_JVyKkJjhuSxzRS80fOp0DIT_lncKfH8Nu-OObOOFP3Ujp9w7rGLROx8nwy8cidaXgORHwD56jhHgM865yHLvsx5RAMUtcSqewdd2Mra7xhLHqc9LFr4QF6zinWO3wdJANqwwjJopFa6Q0VvoBphk-nXX9OdllP5UMWq5RFMkZUgTj4aQgiivqqZ1WKKac1DcNJiQaPwDwIw2CJW_1BwKuEUxyQTyTheN0WERH30ZLrezbQSdjLAKWAGmp0RZ_6DzsTI0ekfo7UWeS2tLZu0GKEgjCqVi1R27Q5QY83pemQ9stcvAZ-QbXIv2EKbwdnJAOmF3Ilux4RWAPZu9Nhe7__kWyP5KTM-sHuei83P3GQUayPDMzpoWbK5ESxgfjXPj2JoKyZGFvZsLke_9dnR-1TQszlHMJLGS11D0noLeWARrO1sv8fMPNGiSC8c3cvRqwk80ouPkFgQsL1s2ynyZ7o2AY4cLVPZmiBsAm2dUPqZEtfKD5OeIP4QdD5IiQtLysXOAy5Cag7_8XUaI7N7FZpS3UTo70CVE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
پیش بینی 4 بازی امروز و بامداد فردا رقابت‌های جام جهانی؛ ببینیم چند تاش درست از آب درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/persiana_Soccer/23520" target="_blank">📅 17:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23519">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=r9b_Z0ivqXHudJ1reY57Abg77fpJAfcwQTl0SobV__tznET_OPZkkgMRTRjSEUHaQ3nzb4F-sQMLZ6oeXUokwrvNndBOLfZxuHiiRuI--F9QghxH-s6xjk-1L4VfvtzpGF781yZa26jzDOTB6rLozMY7KAMU3SL8YGwhs0Sj5iUWIviQxSwCm0Hk-yHc506-xod3dpJudffhkuQkoDxkMFN3DRVy2KhEIvB_Ugo46R8_TNi1orhlAVK3ZAKvsgNMVl4oTlWJvxGYnaA7rd68G4QUqJIw9lXwJvAdVwagZ8772xneXVlkPbJtXDVX_9i4Iwe6UiPJjeaCd0p51VmUFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc271fde7.mp4?token=r9b_Z0ivqXHudJ1reY57Abg77fpJAfcwQTl0SobV__tznET_OPZkkgMRTRjSEUHaQ3nzb4F-sQMLZ6oeXUokwrvNndBOLfZxuHiiRuI--F9QghxH-s6xjk-1L4VfvtzpGF781yZa26jzDOTB6rLozMY7KAMU3SL8YGwhs0Sj5iUWIviQxSwCm0Hk-yHc506-xod3dpJudffhkuQkoDxkMFN3DRVy2KhEIvB_Ugo46R8_TNi1orhlAVK3ZAKvsgNMVl4oTlWJvxGYnaA7rd68G4QUqJIw9lXwJvAdVwagZ8772xneXVlkPbJtXDVX_9i4Iwe6UiPJjeaCd0p51VmUFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/23519" target="_blank">📅 16:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=QpAw4of-SDgAPWlpg_I-s7FN6fx9f3z9RkhTFzADEm4CWVtf6ndZ7V0Ij9b5wc4C6_GTVgUIAtAu0FIZt0oFI93z6wGIehR8xZCzMtp8ZEdrOtfeCBgbHJXEk7F3lAgb2xDFy9Zf6ZNTgP4762Buo8isr5yRQvjusJHJ0_eFpo22AvrRTSE_mZ_Uo-2oZwmb0iPMxCsq0Cv6vi-XiSdpsUjHdFBSLbMl4-xQpx-heZz-4p75eGM7Z_bRYwLkom7Ss8ndHrQ7ZE8m78rZ8LMHbIO09wmk6ptAejIqs0OleLpDoNfrqwSD5DT0GnsKzVDgtYMIHAmwCDKB2NGR6hokBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9720dcdd27.mp4?token=QpAw4of-SDgAPWlpg_I-s7FN6fx9f3z9RkhTFzADEm4CWVtf6ndZ7V0Ij9b5wc4C6_GTVgUIAtAu0FIZt0oFI93z6wGIehR8xZCzMtp8ZEdrOtfeCBgbHJXEk7F3lAgb2xDFy9Zf6ZNTgP4762Buo8isr5yRQvjusJHJ0_eFpo22AvrRTSE_mZ_Uo-2oZwmb0iPMxCsq0Cv6vi-XiSdpsUjHdFBSLbMl4-xQpx-heZz-4p75eGM7Z_bRYwLkom7Ss8ndHrQ7ZE8m78rZ8LMHbIO09wmk6ptAejIqs0OleLpDoNfrqwSD5DT0GnsKzVDgtYMIHAmwCDKB2NGR6hokBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روایت ژائو کانسلو ستاره32ساله تیم‌ملی پرتعال وباشگاه‌بارسلونا از تراژدی تلخ و سنگین زندگیش که در سال 2013 مادرش جونش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/23518" target="_blank">📅 16:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb6SKJMqRgbGeRqQW44XN4a9ICbrZ1vz2CnUWVIv9958YhmDKTt4W2VG9hfDqZiOP7lJvbUbJlo5-oo14GozfbUa5pWUXbFqjFORwJHxrrCs19azMQpbUBqrWmOoHf58sbobjiwdvdweWoFyeVSTZDah8F29P3a0fN9-CrjiKS_7MMwThAzf4nsjfuy50JUtm2IKHXxjVdt8HzR6pC7DoQwH1TYQ46nE3EjIoj0Gid7L26Ll84cPdnK-DGjagvWMHkCej2L1BkHhFMQ9xt18w1bQjLdx0r30Xm1PTG7tchteTXQKugsrROhbaPBtwBgk_F7TtU_T_cB_k5jsvtf4dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک‌کوکوریابازیکن‌سابق‌چلسی‌ومحصول اکادمی بارسلونا به رئال پیوست؛ وضعیت باشگاه بارسلونا:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23517" target="_blank">📅 16:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOKaGLNnBvA4XwAOkXaZDSMIiN7mHFkLUyDelAqioJIy4g1vRHix3i8HCtCCbzS6JkPkDiBJFMRbfD5pEE5eBBmMlINmB2N_s0LJcHPztDhzoY1euqULlz85xPmnzVY7piG4h41F6fMKQ8EwWmn8aMYqLwCI2VvmQMG9bsog4lRRe4mNzituPtFuuHtyduTvocJ-Gplei0031sAg3xDJLr37JUOJccllcGLS_gbVbFPzoBHjZn9KqQBcQq2ya6dS3-b5lbM-e1f5jtVzzyJesyCvmA0p7QYKzPsAkePQU5F7AZNsa837nbDugY4VYCVTEJzEki61LXZy1eU2og02Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/23516" target="_blank">📅 16:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcLLGJp5hGGm2AcNYlgOxRwq65RYrFjokAjlYP67vtjgOD4vAcULxJt92mfaWoelS5cMX_DcGQgWVjG5s9II9nRPFQnqp077TGoibit4m_tj8TL9jpDsFxFFPs2rR4kVF5qevnStniPV-2w_D7oZiAppTVNCrTgH9IqqhPtm0BB7x9W0TWKkqMBsPOpLyGVY4cXANcGuZ4HsugeIsaLaTydK0Yu9G6Aip9jT86xzipy6Nv8hHCEbO7Gl17jbhDClCRg2k7EJT264IMD5rQHDyq-4WSiaiu49JCafuedEJFZYMnThPmgu-lnNS1I76Gn6zEtS6nHYYtZtnhi9awGfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/23515" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJrNGabJG7o_7DVO-Z19v9iVMLZbg3BCOQGGKZPzInEdBG9TKo_eQIamcYc4bPLcDO3IAaGNjmmwO7KDlukQSBnppq_gmu5xELH1queZOyeLe4L3r9hObaSK60fJYqcMVw3JddD71m30R5pPBdbfhdTj9UgZ14k6T5q3ZEOzIt18bOb-7RuiKPxDEOpOB8Fz5bSPrlp1GAwYW_cGG18V8oZXttkBEvxvTTR2mNhYPVO4EngYXgdEupMDBcyFIIa6F8Fqp70-HJik8_5XhcS-DheelMui2FDqtFwZoeoLtcw7XiTdV8KPhUvesr4RZ0BWdHD3FPMqBXmG_CreyVSEvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوسمار ویرا سرمربی پرسپولیس: بارها به مدیریت باشگاه گفتم‌که‌به‌قراردادم به این تیم پایبند هستم و به محض آروم شدن شرایط کشور به تهران برمیگردم. لیست بازیکنان‌مدنظرم‌رو‌به‌مدیریت‌دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/23514" target="_blank">📅 16:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4lN6KbfoeUW4_vR8KQ7-x6kqBGLWWPneeAAh4c53BJui0JXOTqdo9xuWRR-SwQd9xViOTvBme2ZcZWU1WDoWhH4yQ_R77tUY01I7JMdv4EKqS6vEpWbL0BD5IEW7Vd2CrEKoHj0gTcD-S5kkmN9EJUiB4YidWz9Xd0o2xZzLixRjpRwuDZTTIuAodtBOCIYne0WNPuA6wzwMRGlAwbaKjezRLOxMdTaWI-0n9Einolg1jG1LQpBwFuOHPQYcAYdIbXwCnxF8EtAGZOlTcSZEWc0nc_5-d7hPX0AUxLOvxE-PA2cHhhWYRoLaiQ_vMg2RIBy7Bu1E0jIR0mfWxGTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دایانه تومازونی‌اعلام‌کرده به ازای هر گلی که برزیل توی جام جهانی بزنه، یه عکس کاملا برهنه از خودش میده بیرون و اگه برزیل قهرمان بشه، با همه بازیکنان تیم برزیل یه دور می‌خوابه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23513" target="_blank">📅 15:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=m3I1Tbiaq9bKb8NMqRJI_HAidMtKObHj0d12jJzG8ulDYKEYkDBPpiKhsJp0aBFIPivZXwFSmrLMCBFSqMcsLux8v5XOu1ntnic9fz_7dwnOlv7lLKJEhY_5jtnw7bFWkZ8a971as6Y56EOkM5FPFEre31VEQUx7GdTofNerl0ecoFRhVF03ttyQFSg7F6cJD5N32nEd8l9r6ZfksqMNR7Pv-YfNZXOJakMB9ZPCdLl5sDZkb6-FurnWEcnN7s2cdjjpDe0Zadq_DiOJ1B5s16gTKky45cpCesYRc2iyi11V0mc1yN72Ofr7xZxNHjK7pnvsltbMLmetJqEs94HSOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6831beb90.mp4?token=m3I1Tbiaq9bKb8NMqRJI_HAidMtKObHj0d12jJzG8ulDYKEYkDBPpiKhsJp0aBFIPivZXwFSmrLMCBFSqMcsLux8v5XOu1ntnic9fz_7dwnOlv7lLKJEhY_5jtnw7bFWkZ8a971as6Y56EOkM5FPFEre31VEQUx7GdTofNerl0ecoFRhVF03ttyQFSg7F6cJD5N32nEd8l9r6ZfksqMNR7Pv-YfNZXOJakMB9ZPCdLl5sDZkb6-FurnWEcnN7s2cdjjpDe0Zadq_DiOJ1B5s16gTKky45cpCesYRc2iyi11V0mc1yN72Ofr7xZxNHjK7pnvsltbMLmetJqEs94HSOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
این بخش صحبت‌های ابوطالب در برنامه‌ دیشب درباره اظهارنظر رهبر کره شمالی که گفته بود عاشق لئو مسیه و دوست داره آرژانتین قهرمان شه عالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23512" target="_blank">📅 15:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=RCHxkVM3ZM-I_qrTfcbAJ-qm1qQBPuEMqoKdXqrE_EnkRVOnTqJrZjDHfVeugIn0ATJ0GkIr85AM5jY594NdXS1WULITusJpepgvLfHZOP3H2h2qHIkgAGDtrrw83nBD3WkwlNLJS3LmS7_TVJve80jX-7WzCYB9Pi45pgjNJ-ogiN-_T4eZq7mo1wQ8bzt9ZgbjINfn2v2IRiqeC1LzQGds0TDDhojoWRItq0GSx4p-kq529aRpzymmRF2Xc5fK8gx7TBHfJoUycDkFQZvwXtl80PHoTrpMidrmuDVl_7m-9dyJKfqg0wNu_fihV-i-Iu46Q1lL3GgAT4xF8takqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea5e91b256.mp4?token=RCHxkVM3ZM-I_qrTfcbAJ-qm1qQBPuEMqoKdXqrE_EnkRVOnTqJrZjDHfVeugIn0ATJ0GkIr85AM5jY594NdXS1WULITusJpepgvLfHZOP3H2h2qHIkgAGDtrrw83nBD3WkwlNLJS3LmS7_TVJve80jX-7WzCYB9Pi45pgjNJ-ogiN-_T4eZq7mo1wQ8bzt9ZgbjINfn2v2IRiqeC1LzQGds0TDDhojoWRItq0GSx4p-kq529aRpzymmRF2Xc5fK8gx7TBHfJoUycDkFQZvwXtl80PHoTrpMidrmuDVl_7m-9dyJKfqg0wNu_fihV-i-Iu46Q1lL3GgAT4xF8takqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همسر کوکوریا مدافع‌چپ جدید تیم رئال مادرید هستن که در مصاحبه ای گفته سال‌ها رویای پیوستن شوهرش به رئال‌مادرید رو درسر داشته و حالا بسیار خوشحاله که این‌اتفاق مبارک براشون رخ داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23511" target="_blank">📅 15:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23510">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzGSISfmkUuPnpPlMRYaibYh2NaXl0OgFCU02ah8ZzJMMutiS_ipPKAsLXtAhZ8G_IKsYiN3NMFdAoHXJcwe2JJ55zyfiq168cfBa8O4UtzX9ZEQrAmpYzFSYEd06WQ2rOMl3gTFONVMk9c6mkLHc7-uGUzMUIhz4HHihrLAQB77f0AV1CRwh6fIqiZJOEzJvBCnz9KgoE07ur12VgmhfqEaEebcI-evse7HWetedMHCCfTtJZq9WyooQxRb9Ljf2DowOoniIPZIN7Vq6-_wdkxYuu9V2QZi9zG-zbvY3SVrHFLeMI264oIF4SriX7z2P7QqRryvgdHlMoLPcXtjgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه‌بندی‌شادترین‌کشورهای حاضر در جام جهانی ۲۰۲۶؛ مطابق معمول ایران اون پایین های لیسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/23510" target="_blank">📅 15:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23509">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGdlrF2TCdprpSzg6hk5eEUEp8jcBrObgp2RaVXvPOcnlB2ys2SgWRzISBW9WsIgzShI-jnO-v5QIaqrxcbuTUE9fpd66Gphx7imfkuuS4vvmdIm_yQFQ5anUCQ-KKI_Ut1ePFxd3Nup6zjAcjTgMAtcpob7LZHC6D5tsEK2SNc4ItRJnuwrrXMnkeRLzkxIr86bkN5U8DAbvkreDVK0JHX--dm6ydKnv6LKcy_nWvtLR2DBaKahavhwAI74R77oIfv4NFfRLtANiJqXeYs1MpzGwWNwluBXj5atG7iYpfdqSgXj71LE7ukb492xjAPq3GMSFMXQbTFj6JtGB-gqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نیکو اشلوتربک مدافع ملی پوش 25 ساله بورسیا دورتموند آمادگی خود را برای عقد قرارداد پنج ساله باباشگاه رئال‌مادرید اعلام کرده و درصورت توافق دوباشگاه احتمال این انتقال زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/23509" target="_blank">📅 15:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23508">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=Jn0Xu8qHrfrbn1ksXO1gSs2JSGj72w9QWEuSbnIip5-vMwp2XOa39hE5yLgECUdxZ1Irso61FgSccIgZ6YalXd5yVdt19TTcA5psLt_Vak-SpbFIXGMNH-ib45qHVavIrBB0uyG-MKJ9RjdX8Ci5st4MgUw2HiyD3RtcwzI_ApcMwXSFi6QdGedygiIkg2rPN7v1WcJ1-OVtjntQfSHGDR-qwcD2r7pIxHZLDIR28bdiDibC53XfSC3OvmCF6PC8mXacDkFa04NdGifuB_ww54ymMS2gkupluabQQpBJ6UwM6t_sw1yb_k2pnqK72gGYfREDwLFvAAkZRlloS8aZ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7ff7752d7.mp4?token=Jn0Xu8qHrfrbn1ksXO1gSs2JSGj72w9QWEuSbnIip5-vMwp2XOa39hE5yLgECUdxZ1Irso61FgSccIgZ6YalXd5yVdt19TTcA5psLt_Vak-SpbFIXGMNH-ib45qHVavIrBB0uyG-MKJ9RjdX8Ci5st4MgUw2HiyD3RtcwzI_ApcMwXSFi6QdGedygiIkg2rPN7v1WcJ1-OVtjntQfSHGDR-qwcD2r7pIxHZLDIR28bdiDibC53XfSC3OvmCF6PC8mXacDkFa04NdGifuB_ww54ymMS2gkupluabQQpBJ6UwM6t_sw1yb_k2pnqK72gGYfREDwLFvAAkZRlloS8aZ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شیث‌رضایی درمصاحبه باابوطالب حسینی: همه روابطم باخانم‌هااسلامی بوده! دروغ تو کارم نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/23508" target="_blank">📅 15:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23507">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=gkwKePF1MJgGk1hhLgdJdP4gaYUZPcSL4kO0pP7gulPmSkaCke_TKefh1SyIYI993rO4YjLjbU2XqEb6hKeC37ZW6RfMuqD7GXTxQqbmiOx41EK-9SQaOaBfuJPNWCXvrFwrMYKUpbTzKrU1VhXeOzWI9Wp7eWAFTlrZW_Il7bmmIZG51OpzgMxTH9yE7f_oia5TfbDLyY7qRsY9ge7yHGh3bvKpFafV3ZOKq322gP8RUe3fKdy2-q2kAcGneCy3SKyA0JtwB6iVDM6lYmb09u8yiwgBYozTOWApmB5tNEjbx8ysz1We3rieeHD7hjwrve3e6Yl0AvFM54GdD1uZ7EbzRoa1AUfcgZZrxEZc_TPXdzqpa7d8TP4x0M8SVRm7XbDo5KVElVY1hijugBpOdfvz0S51hLYe9ktPwI96qQG03iTcO9fLq1mQCAatM1Q_tvHBmU3nVxopvuaW9eMS_cLtLv-1vDmhj9d100uLhBbYNzhKojJUD1Sm-QTj3MIaOsGxqKCgAIA9qd0l9lPbQJyqGsFZ_i_XJn2ro0A8F56DUJQCsteWg81g4erEwMXtljS5Ub3yDj5TvmxF5K8XPjDh7cO5pJzsOH2tUIerGh7f3DVwWvu5DpLEWECBiXZHIJYUzQM0T1E19_8FnFiOky1OSP1k-CHRNFnzOMA--1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0743550e2.mp4?token=gkwKePF1MJgGk1hhLgdJdP4gaYUZPcSL4kO0pP7gulPmSkaCke_TKefh1SyIYI993rO4YjLjbU2XqEb6hKeC37ZW6RfMuqD7GXTxQqbmiOx41EK-9SQaOaBfuJPNWCXvrFwrMYKUpbTzKrU1VhXeOzWI9Wp7eWAFTlrZW_Il7bmmIZG51OpzgMxTH9yE7f_oia5TfbDLyY7qRsY9ge7yHGh3bvKpFafV3ZOKq322gP8RUe3fKdy2-q2kAcGneCy3SKyA0JtwB6iVDM6lYmb09u8yiwgBYozTOWApmB5tNEjbx8ysz1We3rieeHD7hjwrve3e6Yl0AvFM54GdD1uZ7EbzRoa1AUfcgZZrxEZc_TPXdzqpa7d8TP4x0M8SVRm7XbDo5KVElVY1hijugBpOdfvz0S51hLYe9ktPwI96qQG03iTcO9fLq1mQCAatM1Q_tvHBmU3nVxopvuaW9eMS_cLtLv-1vDmhj9d100uLhBbYNzhKojJUD1Sm-QTj3MIaOsGxqKCgAIA9qd0l9lPbQJyqGsFZ_i_XJn2ro0A8F56DUJQCsteWg81g4erEwMXtljS5Ub3yDj5TvmxF5K8XPjDh7cO5pJzsOH2tUIerGh7f3DVwWvu5DpLEWECBiXZHIJYUzQM0T1E19_8FnFiOky1OSP1k-CHRNFnzOMA--1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی زلاتان و هانری، اسپید رو دست میندازند؛ این دلقک نمیدونه ایبرا خودش ختم این کاراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23507" target="_blank">📅 14:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23506">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXDZFfvy9LA0OEKfLXA7YN1h3KKCU3FvyWDeaWBYxUr3DlU9Fxii8t0nDe2iISBZwfpORfhkYfEiDQDi0PdE2uiFB0l7Vzygp7uTfXTs8bdFq1Q3RqTBOm71_DSk4DctgfAdiofbp7IChOS7sGx9l8LaiTOHHP4-wnR0V51j3BYCPLkhcaqDGmXEJOXWAK-e5OT7lbujOnaqj0bMULIO6NsrcG0blWk-u8p0HUgW7O-h3GEdnCWq-tlKHcnpb6YzoPTsHGMK0xeo99nM33PWpYjnCwTsvxGrK_C2p4-CgPJGY7ZOgf9RiLfyQarsacXeFMOwDp6niSCHy9V_wzKHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23506" target="_blank">📅 14:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23505">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5HHg518kYWUJWkWVoVnyprTlGBxUinuSvVoCLN5kIragq8OLmcKno7Fy11sRFH9gJ0d6breBwygl-8y8M9StjPjjJY47Kz6WZZoLBvkxM4GdFlf4z4FbptVKOa2mCtiuSg6Y8UMcdXWOOkFR98LmjIcaq52cTtnPRtcuEXcnSf6RVCGx7o7vUPWsF1A3uYGWdPl62ZRBbbkgdNhRZXIty8xRXZ5TwTjZIf-UH6TqbJvYfLoDQRXDDQv9avKpNFbEGlOCABfeKj36r4yi_5qfK6H9i5At2RkrauyNBiX8A2m93e2mPcLWPhuhLjUVXyYBcafiWgNXH7fpSd9nF0nyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23505" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23504">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358a407b96.mp4?token=qwJid1bKCm9Nj5r2Bsvrb2jsJI3IKD5A33srSCowwLoWFSdnwzhPj5eXiMVWo4I9TcTg6fRtl-dlvSg8e-w8cwWUOob_ha8LIdZUMsvY0K0aaJ0IoWinSdsFySY3TqiRVxmL4nxRS4PspSXPwqpWFs15R2qE_bd-KdvmSCCFpD9EfVdo0-6Od19vfj_4IezIz57wNorGuUw4NUDEJ36Ww0gsccMkFa7cf76Ru5wnIE8JcWWGYpOVx_wH0ghQ0Ynbiw-xBh7Qp-4lDcbRpnNZbK4wgYeNvE2cl_gsYznsc0ydcKZfYhPbFqHKksIZtu0EW_qk8W7ozqtq0oVMp_Vj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358a407b96.mp4?token=qwJid1bKCm9Nj5r2Bsvrb2jsJI3IKD5A33srSCowwLoWFSdnwzhPj5eXiMVWo4I9TcTg6fRtl-dlvSg8e-w8cwWUOob_ha8LIdZUMsvY0K0aaJ0IoWinSdsFySY3TqiRVxmL4nxRS4PspSXPwqpWFs15R2qE_bd-KdvmSCCFpD9EfVdo0-6Od19vfj_4IezIz57wNorGuUw4NUDEJ36Ww0gsccMkFa7cf76Ru5wnIE8JcWWGYpOVx_wH0ghQ0Ynbiw-xBh7Qp-4lDcbRpnNZbK4wgYeNvE2cl_gsYznsc0ydcKZfYhPbFqHKksIZtu0EW_qk8W7ozqtq0oVMp_Vj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
احسان‌محمدی‌مدیرکمیته‌مسئولیت‌های اجتماعی می‌گوید بخاطر اتفاقات سال 1388؛ تیم ملی فوتبال ایران دیگر در هیچ مسابقه‌ای سبز نمی‌پوشد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23504" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23503">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2-t3pGDtl3Wt2MzslM9qr38t_YdM1Ht5xvLUNPdeV-OoO8hZhpDuxtaerL7gaUrAzgeeP8Y5LsKb_YNUjefYSwJ58h_v28ssP2keoc43zDStjYkgO7T7ExWCq9W3GwE_t_jzDjCgMFmMwPMUAaprm0OkMml_8jsZrSq-iafE6g3Kkmu19yeYBtpvANmN3lAQ6mj4QzDJKVCSBbV7iBiobqV2o8BIMJBAp4QcV0HnbdULjlxZapYs1iz373t-LCIPoI6DNeq9Yy8Vx-Nd6D3Fhwey8m4uCbShfuuP75jQrjRGd-04eaEqDdUVz9OEIYwwQFBvCaJfhEOLI9P8HwpMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی های جذاااب
جام جهانی فوتبال
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
⚽️
🔥
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه ای،مطمئن و درکلاس جهانی پیشبینی کنید!
برای ورود بسایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23503" target="_blank">📅 14:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23502">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=VtUGXOInm-4nmo4L1yrcyS-oE6JcM6oyNlmFhoUUSSmobLYHxiAdqAAKvwaBK_smjDhIF0D1Qm2LhHsY8Y4VJp3rQshoCoZcMXAsKlOfOwhX8QdnLwUuqSSrcS2R8X_tkVmTreLE5xyUgGMUk7sUq1GRu4rd1vMaNASCu9DAW4wEG9b1LjsQSSxqI_e5V1hlpubDtJ5vtcP-xab1b05DTxuLBuOeI7AXTUtQrgdl-pjrUZaQ9FCT3Nfk1veWjbXR1t8M0eOUg-GiRfd4eXwwcK_x5wgU6HGRaOrJZI8Zppr_IA4w95kemfowS-dXtt-bbA1-IM_j76eAHqBrcWNDMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d283cc080.mp4?token=VtUGXOInm-4nmo4L1yrcyS-oE6JcM6oyNlmFhoUUSSmobLYHxiAdqAAKvwaBK_smjDhIF0D1Qm2LhHsY8Y4VJp3rQshoCoZcMXAsKlOfOwhX8QdnLwUuqSSrcS2R8X_tkVmTreLE5xyUgGMUk7sUq1GRu4rd1vMaNASCu9DAW4wEG9b1LjsQSSxqI_e5V1hlpubDtJ5vtcP-xab1b05DTxuLBuOeI7AXTUtQrgdl-pjrUZaQ9FCT3Nfk1veWjbXR1t8M0eOUg-GiRfd4eXwwcK_x5wgU6HGRaOrJZI8Zppr_IA4w95kemfowS-dXtt-bbA1-IM_j76eAHqBrcWNDMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
فوتبال‌فراتر از یک‌ورزش؛
بازیکنان‌آلمان برای دل گرمی دادن به‌حریف‌به‌سمت آنهارفتند و از تلاششان قدردانی کردند. کوراسائو باوجود شکست، اولین گل تاریخ خود درجام‌جهانی را به ثمر رساند و حضورش دراین‌رقابت‌ها را به یک دستاورد تاریخی تبدیل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23502" target="_blank">📅 13:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23501">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNAkAAn8s2RsrvBGFKWAjuE1QLe2p9w7LaWwcal_PKsUHWh7TIUo7Bnrl6IYcaGNdplZEIhwquWreI0LcnXmlnfhGgcw7LfnLfc_gdzPHl8W0uCq7Ox9yBInCyQ81rhzw8PkEIniTiOl1bqTTrgDj-G_6CYhKaQOZ_qJRSnv1NJDaKW4Z644NtlHibzLMSG1fnnxPV9mfBQ6lnmLEQvd2X0RUOre3811j98F2ut-Cy8SgvNktmm8rCv9S39RT6X6lmYGqFTAsekoepdssAopY_NumbR8m_UwrHZVHr_2UotZvdmCcDsF28hmxzKa4FJjYsb3B-9qdwLlwJT3DTe7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به‌بهانه‌عقدقرارداداحتمالی آموریم بامیلان یادی کنیم از این‌توییتر‌که نوشته:زنان باقاعدگی،بارداری و یائسگی دست و پنجه نرم می‌کنن، مردا چی؟ یکی از فن‌های یونایتد هم گفته: ترکیب 343 روبن آموریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23501" target="_blank">📅 13:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23500">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlM0zSXJiJIOLd3rQmbPwjatJ6JTAtzZ36pQnPS6uWwkP3q5wck0vLmePMfBv5twSHX5Bn2F2lT6E2ew1Xu5J8Oz4M-cQtvlkG3uEsUYbXu9Y7d6hUy3Fcqv4EDO3EAGt7Y4MBXAWd4avFSMylYiDa9T0yT4A25PI3na3U3FRIsl1uYR4oX29Yc9TWytzZLieZfDGHfItrIhDNUv7hSe2zrnfbA41nhQFXWBM2ra7dO7phlbVZhuRjyQwmD4cBpcEImCIhXIdA8oz7EIw3Y4KpJjNL0r9V6s0l6Bp5ci2G1KLqYzZkNnvF-1Ef-DCsUjHaPEIhwA2dns6by59AmGFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا درسایت‌خود رسما اعلام‌کرده که تا به امروز 19 هزار نفر از زنان سه کشور میزبان باردار شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23500" target="_blank">📅 13:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23499">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165e001c95.mp4?token=eLCbBjFBmih_bVLmAXKuz6tVGzJrCyGk4W6QWmE1zkdK8td3jw18MqyCEVkSdFvsuXCSe5XYdCf0xE9Lknk18ALxWOSJHNUOsoqnNu5AeToH-MhmAcfEF0hVvEur_IyCs3HZZY38ccLSf91Xrz5mZeAU47zC38pChiUH7hDKtoQuM8Nt-Sa4i4o288zOwwVm4TEdYUcAgB00a5SLfejwEUjpJOSpC-wTE-mFJGATCFxptfJLeu9XIWS4SdbCZ4eHn8eDrtOvP6wKTzV4RECcB6NQjbw2CTFUdkyExnpwhHg7Uvm5M1lGMV2Aj1ckmhDAidNfU4kVX-IITYJkYAyE8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165e001c95.mp4?token=eLCbBjFBmih_bVLmAXKuz6tVGzJrCyGk4W6QWmE1zkdK8td3jw18MqyCEVkSdFvsuXCSe5XYdCf0xE9Lknk18ALxWOSJHNUOsoqnNu5AeToH-MhmAcfEF0hVvEur_IyCs3HZZY38ccLSf91Xrz5mZeAU47zC38pChiUH7hDKtoQuM8Nt-Sa4i4o288zOwwVm4TEdYUcAgB00a5SLfejwEUjpJOSpC-wTE-mFJGATCFxptfJLeu9XIWS4SdbCZ4eHn8eDrtOvP6wKTzV4RECcB6NQjbw2CTFUdkyExnpwhHg7Uvm5M1lGMV2Aj1ckmhDAidNfU4kVX-IITYJkYAyE8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد سیانکی گزارشگر:
امیرمحمد رزاقی نیا هافبک ملی پوش تیم استقلال که الان مسافر جام جهانی شده رو من کشف کردم و به فوتبال اوردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/23499" target="_blank">📅 13:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23498">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tj7bozubG0ENHWRmucWX0CGgNmi9uxUW2GW5lbnBlA-1lxX0feOqRktV6Di_0780HEqyxrrpezIrW1juKxU5NA-AeHEhqTqhB8Fiaq_xoJkRWQsr5lzNJsAG2VbNjpMxk5_Dw3wXBkMH7HwG73-mXsvDPijJXCalH8iU9ZFdgoV_uQj3R2x5w4FBuQkeuCdR-vdSZzQl1t_qbk9kHxWF3oxovh--knskZXS4XWiA2XbS2oe4bI7Lh7FsirK44oJBNNYrs5fd3i5OU1OqtLozVqeDdPkC2rbWTrUZ1twmqJumSzSCaHXn6LQH3tK3PhHl1jKznOb9BuVCfCYzkTs5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات
|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23498" target="_blank">📅 12:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvtNR_KDBS74eJ144MYRq6JOKEvkNMMrpQLUjMLicWSkTfhQXnaBOwFu76UbiFN5V0Ql5qhtYRp9rT-LS_L7xTPQzCDfBxtpGN7MLjUgWzNFRHuLoDoPwJr9_OhRfWQb2qk9RK54-CNCiy-1vgg7_3klKDaI7-CEw14NcY1raqIrJBvT0smbDtFn_6jQ03crCqvgHhEn4Q5BO62JlPAbkD9KFSAadte-DhH0RtotiT7OSv5CUKQdflnMLe_hvW2B_YpPxNiTE_2Kb44b5o3ClnVZN8EOt4qM9D4XO5rUYzR13AS5hHprDreAQfiioMCxkpb2iQBhaVHhVb1ESslCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقای‌گل‌لطفا تو این
نظرسنجی
که تو کانال دوم گذاشتیم شرکت کنید. اگرم دوست داشتید اونور هم داشته باشید محتوای جذابی خواهیم گذاشت.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23497" target="_blank">📅 12:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV38-hHECJviZVcQltQgoQU4hmo9Mbz2r34HLcVLrP1QynCosxrwlV-4ClB7x79cJi45Ko-m0ZBzW5B49WTUz8mMO32B_Fifjeq0IiAFyWi9LckT4nTc8CJ7-nDUu6mWkOZNsrIMGcBJObBtq1RgCnuaSFcYwtwofyy2m6ra-7rv1g-B7M7NEyOuL-F8DxKZ5RHBrdtT5fH7VPXg64GsBDpw3tJcVga9822zjkutH3tWcmUwgq4X9GWp8ZTG1kei7ApPqpFUTYrMGUPpHFhg5Kim-nGcViSEP8TZvQ_w5fRmzdtRiKtREIMe3QJ2WP_2IXDXR0IKmA-9mMIlb9ITtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
تو نشست خبری شب گذشته ایران - نیوزیلند یه لحظه ارتباط مترجم با امیر قلعه نویی قطع میشه برگاش‌میریزه‌به‌مهدی‌طارمی میگه‌این داره چی میگه طارمی داره میمره از خنده‌فقط‌جلوخودش رو گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23496" target="_blank">📅 12:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23495">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=oPHnrLCLpArLrqa7P77sMnHjXT1ZvCj4W97vQGNVTGMsO8vj4Wy24Zm1GDd2cdd5UkjgXRbxLG0ONu9fxbm0dlF2lLjHMsXnilLPYm4NaNmrX_P0o4gMMxZ393ZH_dQYPR9BRWCpaMEaSkHzUaenijbdbWe7fJAt23xoH63Mcv9Ttfc7RGt2a9PWsFWiKwEZb0TKDgKXSsLSjJgmSMXO3ZcxsnQYSvSS6s8wtoa7B4_I12ykELVUIpAGyxScjSCjp8gtUlDr5KnSfNGn-0bMveWjqQgVhyI1hdEs6OTBXUl5MACmj_Ff24wV491_gKIBTj9em7Z3Wwx2P8t_Y6tocg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2c7e5ef1.mp4?token=oPHnrLCLpArLrqa7P77sMnHjXT1ZvCj4W97vQGNVTGMsO8vj4Wy24Zm1GDd2cdd5UkjgXRbxLG0ONu9fxbm0dlF2lLjHMsXnilLPYm4NaNmrX_P0o4gMMxZ393ZH_dQYPR9BRWCpaMEaSkHzUaenijbdbWe7fJAt23xoH63Mcv9Ttfc7RGt2a9PWsFWiKwEZb0TKDgKXSsLSjJgmSMXO3ZcxsnQYSvSS6s8wtoa7B4_I12ykELVUIpAGyxScjSCjp8gtUlDr5KnSfNGn-0bMveWjqQgVhyI1hdEs6OTBXUl5MACmj_Ff24wV491_gKIBTj9em7Z3Wwx2P8t_Y6tocg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/23495" target="_blank">📅 12:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23494">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aia5Zyar50u0f3jo36DurJCdpTy0wcWThTKlamU1PyeMhYZndoLCg_mtBzBC2McTbkcMAif9BcrFXlbgtpuo5Z4CKVwGGF5TqeCsDN5u-Bg1lexY8PeBtkhjggUfe_8LpzQBRMxfVaeJLMoS0Ts61Bqkf-QiUaPoupkkc2p42r9aU56k2UmtwC_TjQEJTgI8kRGs-qkTs3my8yT3L9LMt1FRZY3IHxx0Gg6KSQRswixnqwt1G8oC1ZmWO6iYMlEDjxci5duhsHI8i7Z6oTTNBMH_1-OY4dk0lJPMsYiFYpnCVzAncHSi5u5tP4Z99rMTgkAa3QmouXyJniiqzSwPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اروپا هنوز راه شکست دادن ژاپن را پیدا نکرده! سامورایی‌های آبی ازسال ۲۰۱۹ تاکنون مقابل تیم‌های اروپایی شکست‌نخورده‌اند؛ از آلمان و اسپانیا گرفته تاانگلیس و هلند. بزودی تماس سرمربیان بزرگ تیم‌ های اروپایی با ژنرال برای آموزش راه شکست ژاپن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/23494" target="_blank">📅 11:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23493">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjYttv8Dm7g-3wWf4eixA2WtRx1puevDHQRWCj9rnbTgKORKw2b5l3smInDGA66BDi6vuy-caW_zeHrLdJIe-hwsfvQ8XIf2S9QTB0P_xCP2mZXKh1MvgZLvxSOCec2c1xwxB2aIDIFCl_U2eznpgse8TrAKbJud8yLP10jDoDWXkkDDz3O6bOpZIjpsXnHUA5hQRO5-OQXuvl12MAA0vE5Go90Zze7hlXx2-QvyrrqR2QqLAB2ykOoXY-BKfupnv9A178WoT-o71LeNmme4ZBfsP-dEqrCull8YqTFDjsJroLy2c_dsTytX32OCMVmQN5tD2CE2pWlglOB9QI5TZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
طبق اخبار دریافتی پرشیانا؛ چهار باشگاه فولاد، استقلال،ملوان و خیبر باارسال‌نامه‌ای‌به سازمان لیگ خواستار برگزاری رقابت‌های جام حذفی بعد از اتمام جام‌جهانی‌بصورت‌فشرده در دو هفته اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23493" target="_blank">📅 11:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23492">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ST0zYbmkJVI89XAT75bB6KLBZVnpkdgUeke2lqz2GSunH0DZXHU_kdKwhdO6eBPtJt-lt7ymub5girHliEMFrdzLpzoQdvUPwgN4Rkokbv5XgEXb8tPh28R1pHAuBdAAKIAyYpG5xHyx2KS3oiK7kT-2FOScKvCkao6K8CqXC9MQyaS0nY-Nssud8rN02H3Duob9GAguz9eKZ7JU15TceGNcnPun201V3-vthq5yO-qT5JVuWu3KaCLqyalzqmOJVpCoRprXxR54f_Nf3PpsLdps0DGPHGmLtWgQCZ0Ix9Xx72InR35jeMSSpDtLP7yeFW_XTHaSmOHe0RFFgoHKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ نماینده کسری طاهری تا ساعتی دیگر بامدیریت باشگاه پرسپولیس در محلی خارج از ساختمان باشگاه‌جلسه‌ای برگزار خواهد کرد تا تکلیف نهایی این‌مهاجم‌با سرخپوشان‌پایتخت مشخص شود.
‼️
آخرشب نتیجه نهایی جلسه رو خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23492" target="_blank">📅 10:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23491">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9CfbSKMqTGjIkhZt88xIjh5Rmcwyf91qfhhd7l_J7c-mAwggerkfjBI6Z6DxixDL2jJiPRV_r6DwYa9c6h5eKTAdzkKG0Jw1IY3EbJSSbX5hX77nVuS9EONPGt1mn0hgpC7DQBOWmZ78dmOomEHa2YnARVj01wd3f8aAigC8Y6X8Sa9ccoM5KB-e_d-lOvKdk-BHqfeDva1rrayFb78FYmWtgN20OjCpclLEudqCyLDI5PGZ2_CD0N0l35RqueoINPOxMteO0rK98JuKO0i_NplqWmqV-vKQdnUArly2GtBVF_OG2LYsQDsXD_YwB8en3aSzk6fdTUlY39G1ybnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23491" target="_blank">📅 09:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23490">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWLlu8K2C-5vui5ULshiwauBvlvmWQvsKUVv8BVVsOBnkakGeSE9YUPjdZYo7MgOTQvMTCmLPvxa12pvFOo-t_U4oCGVSdQ3onbW2Hn3mzjDvigIYyYt0hdW4rePH3w-fA93VBFoQFF-XQ6ZVCZ23HsymJl7fBkNa3dtt68lJUPgasb9V5MFpoMx3pE4DyKHA52490XFQY3YqZuo6gAQdltOn3-Gxv46uIesilSFm4HJX3rS2g64_5jaRiuyuPeLuU-dXgXv9N4a7jN4IzMrzQWU9vb249HuJoXHj7uGPaTnZNWCRivReUeDJ--0JBhHWk4iBMFGf1RKte5lvNYRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق شنیده‌های پرشیانا؛ مدیر برنامه کسری طاهری فرداصبح‌و‌عصر بامدیریت دو تیم استقلال و پرسپولیس جلسه‌ای مهم برگزار خواهد کرد تا مقصد نهایی کسریِ 19 ساله برای فصل بعد مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23490" target="_blank">📅 09:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23489">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=FKhEPEULOlFoOQlGl1mFAUGzrwNuhF9F9CzwFO3udy2n6eHXOsG3gteDJmBbuNapytHSDO6k372f6z5n-rhswhPbpwySuqU2oZbz7gCzBE66hH2N6i4XytOtltvObs6DHRoIYdt3MACngOFXlWhhppM0pfMjq5zOLUnk_PEP_EjaQH5ldgG-4AC9Q5KYTbGgkItyfakhsIgAqUAvLpIunEIeFy76adZcKBd1xM0kAHrSmkx-28N3Gxo9Zm_G97jH1ZMQlqihnbXZk1B6O0q5jLTfFZJr0HKWnsONPULcBYKPOBoXVs2aY-JvY9JLTNWMyearLleORd4bQdZVsFzScw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c70aec3.mp4?token=FKhEPEULOlFoOQlGl1mFAUGzrwNuhF9F9CzwFO3udy2n6eHXOsG3gteDJmBbuNapytHSDO6k372f6z5n-rhswhPbpwySuqU2oZbz7gCzBE66hH2N6i4XytOtltvObs6DHRoIYdt3MACngOFXlWhhppM0pfMjq5zOLUnk_PEP_EjaQH5ldgG-4AC9Q5KYTbGgkItyfakhsIgAqUAvLpIunEIeFy76adZcKBd1xM0kAHrSmkx-28N3Gxo9Zm_G97jH1ZMQlqihnbXZk1B6O0q5jLTfFZJr0HKWnsONPULcBYKPOBoXVs2aY-JvY9JLTNWMyearLleORd4bQdZVsFzScw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مهمون‌های ویژه بازی هفته نخست آمریکا مقابل پاراگوئه در رقابت‌های جام جهانی 2026 رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23489" target="_blank">📅 09:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23488">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=r-DsNNAJAMM_EVutIg0mjlgsPJdl71JR9zkqdKlfpqhsLPbcwzQGW0lQ-xgP6F0QLpwnD9zcArz-gjZ0va16obFcnW8UqvE_eHaor_SkoX83QfspO-PUCH9vh-kwhkotdjqWOwK6C8UMqJZ6-eLayFYKRGOYkYQ2zU_m1wJILn1xoHRTGuBsHNSX2ZX4Ns-lxwQl70gL-wKtkSUw77Z6Vi2Nj4Nh1J0kRiCeU_Ig9JqpDA274-fGpTm2optSpbNOFOMZDf9sDDORO6KPxW00IBmT451tYA15EnbjgImJ_fqwpWLDHlT9ZXUzrLYuMMxrwT1sW9wRYz3RLk5wW7uNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f0fa31c5.mp4?token=r-DsNNAJAMM_EVutIg0mjlgsPJdl71JR9zkqdKlfpqhsLPbcwzQGW0lQ-xgP6F0QLpwnD9zcArz-gjZ0va16obFcnW8UqvE_eHaor_SkoX83QfspO-PUCH9vh-kwhkotdjqWOwK6C8UMqJZ6-eLayFYKRGOYkYQ2zU_m1wJILn1xoHRTGuBsHNSX2ZX4Ns-lxwQl70gL-wKtkSUw77Z6Vi2Nj4Nh1J0kRiCeU_Ig9JqpDA274-fGpTm2optSpbNOFOMZDf9sDDORO6KPxW00IBmT451tYA15EnbjgImJ_fqwpWLDHlT9ZXUzrLYuMMxrwT1sW9wRYz3RLk5wW7uNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛ سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23488" target="_blank">📅 09:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23486">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETILfhNdJ-16RKcvdetm2LphFwnetIU8xDjZHv9s7gYGWKe5sGcNCcmrfqML5MRrFVV11X5MP4t5hxtwPVP_SA7BGM4N-bE1IDhgoiXJfJGXmfzjn42Dqod-I5so6emtubOfs5wd376D9tfxp4V8nti-1FTpjyS6hn_yytV43TG16af1tTi8nNt-mBXyrNrMyRaZhhfU2c75vI6XEhnF8umGG0IwDeEgPNNHQf8tBCcCG8C5yf8Xxeh4Pd_MscHq2iptTcaNeLMGp-r2F1pTRLhl3Y7gtChsZEsO7oKF7UyALBRC9eXkJynHMj6kR1PhlltVy-hMA_OcVy8eDvz8bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ih4KBEu65O7zEALiu-XQDHOQfZ0OyWSCIXNkbv-HQeU8jLcWdqSwX9NPVZ9RAnp6F-1_CN8v6iP0hF4wvYlmcFJD5oKv1EzHt4Rj5l3hJWSZW_POHEM73O8bMoIyH_FfWHXxNasUsxAgrIgMdpvzzo1oyOQPDoM47NKWdmkji_VPhbdYsFU6E16mEngsiUNn-5gnl1NTO-qbr5cQpL5JW4sBN2jAiVfp75ZQ9LG1Uvz99j3tK1Bfj2Nm6Loc1lhtl7IPCsk859EchUALBKehiO46VTsryjIVNprEXEspdvOo8jPqE5oGUtLektdpR0GvdBj5nZK_Jgrk7OXRTifN3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23486" target="_blank">📅 09:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFLGBDcJWirK39dWWMgYTf7pW3Kl3ep-B6XoQn5SPQjxH_GMe72EO9tUgwdbU0B6CBiukFi2cp-JgAHhu8tdmqBo1zQQN2-YKRVzEW-3aFC0ihzaRIJnZDTg0UzIaMyfkikBXPRPRvwbHuawDMjQXoSUQPsBDNw_dFdx0cQfB3ec7lHo06j51el5mKuPtLJJK48nCTWeWKKw-8KEcbok76eO5OGB4Dz0toE1t2HNc6eNWzv1RexuHoomOKrKerALBV4cUVRU4gNsb9G_NQ42LQGcyHInaM6sXX5DeWzyd7x8xWkJpB1QsSRPhg98SbuEoyP1ahl1SDrzELdnm3qIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌چهارم‌لیگ‌ملت‌های‌والیبال؛ کامل شاگردان روبرتو پیاتزا کامل نشد؛ سومین شکست ایرانی‌ها در لیگ ملت‌های والیبال در چهارمین بازی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23484" target="_blank">📅 03:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quOom2dE81f6tP2ILDnobqdAIk5TOVb1wwQREu_-Es2d9laNH8rcxbOXkfvESLdAcL_o7WkuZvkfKeG0jCzSD7m-BChol518Vkp22QNUor5vuSze-zA8tkJnzx7cetB70At9SkdHtZyNlS-AaiQNA0nsr_VX0tdI0VytZJT2GwGkgXq1ihpfgeP-xCN9dW_omljDZnbis3Fvl48PuLOWeIUFgIdmcOWRBspoczU0u9mooku6XqbYrHDjvk7tZ3eZPTRri-UzyJ4-Xno4Y8HdOhVjDG_GPBCV_yh7D1GEFhVajHmoa07k4WORINVCZimCE1X8KMxO7j8AIAdK1UDwvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نماینده انزو فرناندز به سران رئال اعلام کرده که این ستاره آرژانتینی بسیار علاقمند به پیوستن به‌این‌تیمه و حتی‌حاضره دستمزدش کاهش دهد تا بعد جام جهانی شاگرد مورینیو شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23483" target="_blank">📅 02:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK_bDvNh7pLq0X1yRIrkWYE0F87XOMEmAqhPQM3Mj_hYoMd2ILshWC-3O_PKLQTgiDkoiEHlGsw-W1LwtKdAVFXv8qQ77MNkv-5s3RCzpn3Tc1OT5ZdjVBjE3_SX4DieKt90W5hKaW5_15WQkYroU5-ir5UhHIrDSF-Iza6BaoRAuYRRUj229vprjhcdOtgo93DMrJ5rKRkKVesC_q0xtHjWlJUB6avpWOpSpHqRvdx9jOM3LUIxLGd5exNohf8V6YyodcUMel-3AZ1NYeZ_O_lr-DkjQNbXK-ZEJII4P3w93eI-QkIKskZegTm68EdJRZrEsc-wkXdVa-uXeE05IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23482" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSfKqBVrSrETqtnbJXHQ6enGiuH17ecb2A0-VDRTwxn4m7k_Fad1M-K_8EgOvogCLaXJxD0Z8HCvRinX4q6bYzeDVLu7cWBv5Kl3-7Ruxh-R6XceoJcrNT5N0HUfmIaptc5pVE6y8VO3Fn01q62V07DWGkUTOKPIL5v-q4fBOtFVy_YFjQbCeTV6inhEaIW-AfWqSd7oHuHLaRFe3U6OAAE9BIc-ArxTIqIbRN8z8golaYYUI18pV7csTS07hCJyPCERskL4A_w30oyjM-_bWcPu6wOenoPhO-s6V2sDAIw8fGOpTkLcu7vQXoaTdP9er57Cs8L_RYzq6cvGC9mTIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از آغاز کار ماتادورها در جام‌جهانی تا دوئل تماشایی یاران دیبروینه و صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23481" target="_blank">📅 01:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_qaN3lHajbNa0Up2WsrJLUcLFncbxTDUy3ru3MeFVJXzO_QMpyk1tswLQ1YTLjLrBENjDKgHI5uwSxJhRSOTenistCiBCkFJLPuIhzds_NpQgBocA0WaX2pEZNHKdN2Cd8SCP1hoy36-y0i-xWRjB3T0CUQIuSs8u1bM4a7cm6kxZ8J3ZECEw-0PZ86MasLPNyiLvhzwXFL9jwPnFYikqeWCFGLXWh9Y12vz_dtH-ZAy8p518WzsKFPiXJkHVcbJQzEK8oWqtEP5Twj5QGO2n4Uuxu1v8Mb9ihz3avQNho2Uphq-5CLjeZ5iN2b2qDm0evHBSNjfPz1NsBASWPFDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
‌جشنواره‌گل‌ژرمن‌ها درشب دبل هاورتز و تقسیم‌امتیازات درجدال هلند
🆚
ژاپن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23480" target="_blank">📅 01:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=jW0KpwRA0PjOU14p4pOWSQOtifIvM7rAJMlzQkSNl6d46P83prqZ9rNe4wfXBphqFOg4UJV-0vTVR1DtdfcUXAuqc6BwfwWU8b9nIjRkIVszJ1xIYmq3BtUjww-BhvLcHWU7IjPZSlH3N9HVDfBbg0ZeDSuNi-V2Jnrh6fsH_LhHTgTicK4l6v06loV_bCAsKySu4WsvPIcD38brNGYnssQA713I_DuhC9Igrpctz3uF9dT_0DEsIi3ris4mk-zuyFMMtZFV7HFyka-9zxn7IGtFhAhxyfsv6AoIbHftkOnhYLf6NFxs3A-2CcQapJiHU6P1B5x0FFocYWmI-NUsFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9b859a0a.mp4?token=jW0KpwRA0PjOU14p4pOWSQOtifIvM7rAJMlzQkSNl6d46P83prqZ9rNe4wfXBphqFOg4UJV-0vTVR1DtdfcUXAuqc6BwfwWU8b9nIjRkIVszJ1xIYmq3BtUjww-BhvLcHWU7IjPZSlH3N9HVDfBbg0ZeDSuNi-V2Jnrh6fsH_LhHTgTicK4l6v06loV_bCAsKySu4WsvPIcD38brNGYnssQA713I_DuhC9Igrpctz3uF9dT_0DEsIi3ris4mk-zuyFMMtZFV7HFyka-9zxn7IGtFhAhxyfsv6AoIbHftkOnhYLf6NFxs3A-2CcQapJiHU6P1B5x0FFocYWmI-NUsFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌محمدسیانکی‌درباره‌درآمد گزارشگری؛
سیانکی: هر ۶ ماه یک‌بار ۴ میلیون‌برام واریز میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23479" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف لاله‌ های نارنجی مقابل سامورایی‌ها در گام اول رقابت ها؛ نماینده آسیا به شاگردان کومان باجی نداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23478" target="_blank">📅 01:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsHvZRO3pfNkfnw2koKHAlJxA3m9vwXZJAPvrBDfDG6_yrZaT9-fJPSf5FIPpB1znfdO6juW8P5lTNSidIHF6vpaYIcAScOYUnfSKBTyqa2JE29b1SO96-3wtlXY_rFnyz-iVEPlf33HHI0EVE9YvC-7Taij6g0ZXY6q2Ad5XUea8kI1fuwWHu2YA49Dz4jRvVKksy2vR04pRQTPEftmUqQlsANW2mpuSBFccNOk31jaCfk-UeVLYBCcfP-v1q3l6OXJ65HE1-pbrSG4YG2hbShVWOkaQsm2r8MiCQJQFYJWTP50a17nBz8nWB2Lxrvrezwqu4cogFgxNs5ifn_9VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23477" target="_blank">📅 01:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=MnmFYmfTZ0uDUtk4e6jrVRtjDXkKzK-uutVujTWPkzU_8S73PGL3F31Td4KWsrLKof5_nuEhpSksMYeToS1XMtr2XyM4QsNRU5_mRStq24IZ0U08LBRRAq8esz_t2XE8Nib0740M-1hV4KEzQLfrwK2WvrMusz7fbBEGUtFnoMV_dDsSP8LJDquyl7td-rYhDt0cL0t3fPozFm9IPx6ynxgYDWUn91hIKb30cdJlEY2QPdt2-vdjXPxf5z4Qml1dM3z7obkbjq9rL-wWz4k-x8NQnzs0mt7CVn5sVeBqLzOonq2526KuT9L99yDRV-xmQmrT5gz9uWWLbLWjFSG1GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78498ffe8b.mp4?token=MnmFYmfTZ0uDUtk4e6jrVRtjDXkKzK-uutVujTWPkzU_8S73PGL3F31Td4KWsrLKof5_nuEhpSksMYeToS1XMtr2XyM4QsNRU5_mRStq24IZ0U08LBRRAq8esz_t2XE8Nib0740M-1hV4KEzQLfrwK2WvrMusz7fbBEGUtFnoMV_dDsSP8LJDquyl7td-rYhDt0cL0t3fPozFm9IPx6ynxgYDWUn91hIKb30cdJlEY2QPdt2-vdjXPxf5z4Qml1dM3z7obkbjq9rL-wWz4k-x8NQnzs0mt7CVn5sVeBqLzOonq2526KuT9L99yDRV-xmQmrT5gz9uWWLbLWjFSG1GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
عادل‌فردوسی‌پور در ویژه‌برنامه امشب جام جهانی به این‌شکل‌جواب صحبت‌های میثاقی رو داد: اصلا حرفات ذره‌ای برای هیچ کسی اهمیت نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23476" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=QRjB67xLMWJqAy0hDWvBk55670HHTOQjC-ye_ofjS8pV04nBaN1idMmJKEIp3Mw3VuwYGhAMz1Cab8uDJCZrYUkE715nMwAaNi6Nbwup-6CKWjonwcGyK4cA2TdEADPo2mV8sSpK8CFs0tfE6T8BXpqSjTUF0i12zDwX9NqjC_fdU66GAe2NLiQHZdI0fC4Celqp4LDNVY2vjDvbAOtE89_3xZQPyFKi94dG_0MmNreiGfFNls7VBWEzkIIQ3AmfkbQHmGRjcDWyxC_aeoJeFR-9DZPj46C93GJSGiRhwxfFQBZdL3-kBVG91E6L_GCz23B_jjrWDaxZc85HLcsxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fa8e48e0d.mp4?token=QRjB67xLMWJqAy0hDWvBk55670HHTOQjC-ye_ofjS8pV04nBaN1idMmJKEIp3Mw3VuwYGhAMz1Cab8uDJCZrYUkE715nMwAaNi6Nbwup-6CKWjonwcGyK4cA2TdEADPo2mV8sSpK8CFs0tfE6T8BXpqSjTUF0i12zDwX9NqjC_fdU66GAe2NLiQHZdI0fC4Celqp4LDNVY2vjDvbAOtE89_3xZQPyFKi94dG_0MmNreiGfFNls7VBWEzkIIQ3AmfkbQHmGRjcDWyxC_aeoJeFR-9DZPj46C93GJSGiRhwxfFQBZdL3-kBVG91E6L_GCz23B_jjrWDaxZc85HLcsxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اسپویل‌ازصحبت‌های‌امیرقلعه‌نویی سرمربی تیم ایران بعداز دیدارفردامقابل نیوزیلند در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23475" target="_blank">📅 01:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJYVgZzY7azQd5rMSBnYWQ3FYCMpfZIO4K9WfrngECVu_rKNxbP32GfmaIegNx1Bdn-41qeRkH2KYBeNVz2jTTyMjbomuUP7OWNObCdVeJw7z1B1eMSVTt3bTyvXDvzsfKZBNvw0IXlwgKj_9_BFxN9Hzjr_ygXRtVLlozBr68sQx9C_OZpdMZR-e0S_bzgaNsyEkmQ43z8RxrTY4SNN3FubpSwhUd4ThBeai5JxB1zlguY_BQjdES5Hun-QunoKqCKcwQfT0IyX9fbwHOEN0ZUq63uVLs-ENJsIiW-PN2To8h6Tdhmsxy2JGddOeVj3mBNAPE1vVXQvWlgGl9b4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ نخست‌وزیر پاکستان رسما اعلام کرد:
🔴
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد؛ جنگ در تمام جبه‌ها پایان یافت، مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23473" target="_blank">📅 00:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTdFr2KGdidde0zj4QZ14abByBgpvZm98AI0aKMMIgX_ROwdLToeDCbJe3Be1fZBVgeVnM7WJQ7hTjOYVABX5k0PScYCTOTXHMtzUonEyA8vNHPBgMvoBdSLDnNEHmo4edtEwiOH_C-Junj-s1z2DnSoQInqpqNr3w4AORqcuTn7-SS-LY30I9h3f52gLcPnGazpxTFJl4bJWKO5zFaPj6LtCw7qobmGcehqX-0tVm7ud23wPybIH6D1-RrAkUBKm0r5I16eDCUa1fx89Ak-uMKiDJijiMY3Z0T_YEynMBGgMH8DAII6AygHywKh1k7k2OBK5tH-xhI_LLkIo9aOKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
#فوری؛ گویا دقایقی‌قبل توافق میان ایران و آمریکا رسما امضا شد. ترامپ درگفتگو با وال‌استریت ژورنال: بزودی بیانیه‌ای صادر خواهم کرد تا موافقت ایالات متحده با توافق با کشور ایران را تأیید کنم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23472" target="_blank">📅 00:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhVn3xgsYYSCCxHplcsItX7sqkkqdjssHBvVga0EUfDAgOuL_Ly3bSoDa35wSiVWVKg0sd8jXdhvQYmHbJc_IS3CM2jIDRyh4KJ2rIl2OIS53M5idXkAwtZuJeEpeRrkfsedkDe7awHmFjBegH_CwbQIi3rzI9CGKjQpXiEgmgjca5RjWhALzPazyl6cjz9sOFpvOoKgex7AP5O6Z-12eC0q5a0oYVgxiyy_mGUTS17ZSyI4tsADjhscf_7KTQ8Ivd18zh9SmCiWyEVytjvEd2rbDnrrKawYtQ8pIf9tTyLoz78ZoSapwlMuDhCZ0qXhvVOV9PEz9eJcuAU54A7y3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
انزو فرناندز در گفتگو با ESP: به سران چلسی اعلام کرده‌ام که برنامه‌ای برای موندن در این باشگاه ندارم و قصد دارم راهی باشگاه رئال مادرید شوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23471" target="_blank">📅 00:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvoKmvgoZbI1yCHwE-ihftYaClaU9DMRGir3cg85n9UsiS_c0TLNwTZxJmTnj12i1y_-muLjT64qVtXBsuK3Bm_OOJXZHxFIxBYHTIoUTb0hPyKpikNIZgZ12WPYd3Ijo3DkZpFPWs4tYv9lcS4Bczxfm9me8dujXWPdQ5BoWDPP2xeJJTgzuTogwc-6x9CZsAWspQu5KAJEhSTKDI452nPJxgs4IiN_woBLhH1tBzRGHN5YC3zkZ568MhAK9H-64An6dey8-JRlbCBK5b4U4zo6KjWh4x0EWCTkjM5vkiG_3L9IA1GMy5rajGbZuGmN1r2BWrYwT9eNz6h5X4Cxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#تکمیلی؛ رومانو: روبن آموریم تموم شروط باشگاه میلان رو برای سرمربیگری پذیرفته و گفته با هر شرایطی حاضره به این تیم بیاد. سران میلان هم گفته خب باشه بزار حالا ما بریم دورامون رو بزنیم اگه گزینه بهتری پیدا نشد با تو قرارداد میبیندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23470" target="_blank">📅 00:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8uPB49PFRxfPCE0sQ7G6t2WLF3HVf9eIPaGnCWIAPzqMtsHSXHOAKcKbbruVT8eRUJPWFiIhxTXnTlZkILF3sEZKbhx-gjt3Klki8kQXxBy4-JO5lKu0PzNltafAK5uFhtf-mucjrXLQwhaSzAlZ3-kc2tg5R3CMlBSn4OJS-Q5u5CwePN-tbJD9jLELbCHEJmXUVljFb02Mp0qiLzYztiY_2KGngRf8FdkV3FZMV6zdvkGHloEqK7CB3jDjdddghxAS5cK27cblo2ce_mM40TjFpd-RBKL-eUwneX-5ubT8pkVz6vTkKvysEsVdU-nFh4Gt0eRcpXghb8SNZn78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23469" target="_blank">📅 23:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUBythQrKXIWjDEkKVSjrpTsaVQvGCdzs3t6GVVqFE9NHE4mRCeZNyVo9XVOwO7VgIULFGbfnlrS0Sr5Fo8JfX8kaOSoBZ5Bh6BPia-Hm8r-fD036YUcBoR3Hdz09oddFEz0dYMSeKNm0FAPfyoJvrdDYYPnYgQ85YK_AyncqAEl580tLAEz5gVNTGsGpf1sqmDjw3z1FuFaN97uh8hWqv1Kt1utgYHczJyzBQpTmSRvkJyJpSA77pUDkmzzJ8mow0IviXkJn6cDFkUDO16wj0MvfWwL-OfIfhD1KXSMlR4fms48gAU78JeJ0UTNEBrIEUf_AVaT1B__UYwDjL4sbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاریخ‌فراموش‌نمیکنه بچه جون؛ یه زمانی برای یه صندلی اینجوری داشتی خواهش و التماس میکردی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23468" target="_blank">📅 23:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4VYlg9PNTxnMK6GP1X_WvjgPiN7NZ90ChdSpH6erS2sb0R9ppsjZDQ7grd54YZ6PX3VjqOnRbmDqB6YflQLtUQ8rcdR9AtW2jZb1zqQuGS6rEAzJbhgshGjYKYLaRLzqErepDp4LCYUYgTsXHI5sYRUBdocARu3mAoXd1zKk_d71RU0-HTyfO5354c0Y1gOarpwgNFaXxkH1b1FMIBBgs2K1Qk8Ba8aK--qLXMg8PQj3ZTLJDIysOiBsJJ2oaD1anX5M07BS9t3MyZ4Sc-nFCkJD0_SQLJp2TF6wxMQYetzKEFvfG38lpLs-cFsN67hrVac0z1EeyyCFJj4vY-CNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23467" target="_blank">📅 23:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=Simd2mGZUMJuAwNfR1iwKeUnd1Tzja5Keb9PDPfiCOyX4rcHIGa3o3C17Ob3pkinaMInJUk6C5pbHNCNEtJd5wpo1fd6C3NZtc_eRn2tSYjndZg4G-68QImKlQ7xjuOUbVQh4qesaA8z0Eh4MEcnCShd-EoIT8t8UPjn3PsOKSCkSTgGIs6RiBlD_-lqmIZSRmwx960WS2UuCqdOF5IZzbiSOHsPOGHBkBYMNZ21418r3oFfBDfaUPUJyYa7c95K73rRSJElaKZRkZIin6Z8_kL100MyUMDw8vHd7PaDhI6Psi42nlGDfej0ZuaglduXCUz_D6JoUih-X2vNkp9en3FqnU4kpg3HtdrXhGQ9PjhaiwVGkWZoZJJAF-st1WwKCDV653A1xxVSRznXYfasCL1uSXBh9YJc2Yht1ckSl18kLQ0hJvLhwFSX1d7xp-Cg-taiAXvO3SGb21rcGi68SBU9oAo6kt4XV7xcgyBfCTCQHCMiLO_MkUQCxiilt6pEQINAXzBgxWTs-AejXsBB8IFP23McuRQCdGPXjWB5gC7587Ete01iirjzezv1Ihnl9Ng4oAcj4oaEuorQU7B2pJ2QAzR8PSQgW5utYoA_vwoMlGVtpDBiP81wropL-3Edf8ox_LMXrPuuqQYmabM1Qc8rHtSukQqc6qThg64dEWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb4ab3ec6.mp4?token=Simd2mGZUMJuAwNfR1iwKeUnd1Tzja5Keb9PDPfiCOyX4rcHIGa3o3C17Ob3pkinaMInJUk6C5pbHNCNEtJd5wpo1fd6C3NZtc_eRn2tSYjndZg4G-68QImKlQ7xjuOUbVQh4qesaA8z0Eh4MEcnCShd-EoIT8t8UPjn3PsOKSCkSTgGIs6RiBlD_-lqmIZSRmwx960WS2UuCqdOF5IZzbiSOHsPOGHBkBYMNZ21418r3oFfBDfaUPUJyYa7c95K73rRSJElaKZRkZIin6Z8_kL100MyUMDw8vHd7PaDhI6Psi42nlGDfej0ZuaglduXCUz_D6JoUih-X2vNkp9en3FqnU4kpg3HtdrXhGQ9PjhaiwVGkWZoZJJAF-st1WwKCDV653A1xxVSRznXYfasCL1uSXBh9YJc2Yht1ckSl18kLQ0hJvLhwFSX1d7xp-Cg-taiAXvO3SGb21rcGi68SBU9oAo6kt4XV7xcgyBfCTCQHCMiLO_MkUQCxiilt6pEQINAXzBgxWTs-AejXsBB8IFP23McuRQCdGPXjWB5gC7587Ete01iirjzezv1Ihnl9Ng4oAcj4oaEuorQU7B2pJ2QAzR8PSQgW5utYoA_vwoMlGVtpDBiP81wropL-3Edf8ox_LMXrPuuqQYmabM1Qc8rHtSukQqc6qThg64dEWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جوادخیابانی وسط‌پخش‌زنده سرودملی آلمان رو خوند خداداد از خنده کم مونده که پخش رو زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23466" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی2026|جشنواره‌گل ژرمن‌ ها مقابل تیم کم نام و نشان کوراسائو؛ شاگردان ناگلزمن در ایستگاه نخست رقابتا حریفش رو هفتایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23465" target="_blank">📅 22:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR-a2Fikw3y8WS78bBqUFhb_ZLZVnNFEGqUZJE_8su92pxi3BSO8uK0stMWzSLOvhyuLpqd3Hnd0xQs41UZz7wCK-O7IVAHkJSp_cChXwQG1laAYSm3AjueAB7dZfREEkrxY50zy2yhINJuYW8iAIFArtBDBL12pGDN3CNSd0_NiVU6MvAXqeIJuho2KeLrB1wmG4CnP8M9Ie39UxcuJTEA7X24A9hMOARQheY-DW489IOsAIlFWRy7jeT9chm0W5NdqqnZVZgn2WNt4FbMFSPBYHitdqpdmD19TVapfVlHCJNhrnUTqT2fKoo2gnSEjFwoBx1RRDbadXKbmyohHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDwn0wvsI9MnuohvDRURxvsH5xjRFOS4tCk05PCBEMiWn9XansgLWwM1CfOmUowVJk3QHghw0dwQU1NRyqph_digWFz-ZFHmvddD-Ct4gzm7K91Rj0KG52IUUxdc4FUIEokWV6N8g9uCwmHo9t_KInH1JcIXOHSaXA7w1ohsr520XH2ZAGGAzP-KbnfDO8Aq9jOKQqLn5sGpDXEStHYsOvA3VF9Kx9ODh5nx9fexzaXD6Na6-MwvYI6yTpu6FhJoXmGklR5qX0TzGkjdEVmIxVugUFqrLHFv9Ox4Cjbu2UfJHbDXjtsHCrCOCxg-nuhBhVEZ_rtUusC-zS5dKIM59Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJP74-ga2DWHnvTCuDG_oQMLUeDMoSfiTBPOxOyILi4ajB-CUdy0k2kkx92FMmmYQ4HmUZhXC-VFiNwSIjsxk5oHd_2kvHqmNsSQgZoGq0jA-hR-U5K0EaFfTDa0QueHclTpg6Gf46XEMGLT8TvpxzzZTnznK9kGJktPkGDPgy8y4CVVOq0TB_-3HdJzWqyZSy5TW3SLZpNzoma6bAmmE8t4TN0PCYTtEPP-DQ29set0Y9Cl6skQBkGFFeoSoYkvG97fYluPlt5ziQJJIOLEpR32Fvsg5OpsM1Xw-0qVYwUTKRh1d_PTZ8zmnEV_GKAYaoKV_8WKVHEtuWBJNXYQXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6BkvkoKimf1AHjODqMKnvlqOZvTw-HO-lPJLVTQWyitGJzwpxBKC42BI0QjsrdKN-idHTfygLM5We1eVlwKBCVrNcunPSLLlULtOYkEw5AlVYJsVSZV7ltK9JhxRiCuCrM3FglpyjXGt49TD2gNoha2u8dEBqqnhyYe4UV9J4LZcZchpQHIi8RKM1cSqsSVCQ899QBO2NEq_xSYeCaa9iC0CzrE7q_0vcq1egK9dybTPNB6rtldummZqwiNuVO8mw69LnqKN_Cvkc9W8IrH17yAJpTR-6vh7KcYS6ITYjUnK01H0Sef70N1_38Bv6JoTRSvSNmKpguWPul-07-o9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iXeni0fAbgfu14w9Dm9l-j1b6IW4GWbAvk7JyUZUUNAd312KSCf0Y1G9uKMaUhkETwTHeob6mDk78kAUhnW49wbLNBlPxyavRpP3ODo_Yb6NcG8r7uyBC5N_74S2Pw-Spd0ZE1e_mainDfisihMzu2qrtj3dm3PCQVt5g3p02WnxuO06gBYYp4IaEoUTiwT-ruJu78AQWmw7_iy0Hp9XcyCwZmiZsH7GQu2OUfuxHL-aCXZ2C9pWlihM1XEs39PNbveZVVMS-GQrEeh__D5CVTrVhfqGN8jG-iWMvBGDXnHftKGUBf5TLY5iHc231dRJpX6ZsCQ3dkGL8sLtkNs1tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iXeni0fAbgfu14w9Dm9l-j1b6IW4GWbAvk7JyUZUUNAd312KSCf0Y1G9uKMaUhkETwTHeob6mDk78kAUhnW49wbLNBlPxyavRpP3ODo_Yb6NcG8r7uyBC5N_74S2Pw-Spd0ZE1e_mainDfisihMzu2qrtj3dm3PCQVt5g3p02WnxuO06gBYYp4IaEoUTiwT-ruJu78AQWmw7_iy0Hp9XcyCwZmiZsH7GQu2OUfuxHL-aCXZ2C9pWlihM1XEs39PNbveZVVMS-GQrEeh__D5CVTrVhfqGN8jG-iWMvBGDXnHftKGUBf5TLY5iHc231dRJpX6ZsCQ3dkGL8sLtkNs1tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pW1DfGFTgCUYEr8GCJuRRl7qHsSYRZY2q7OQAHnT84veTHnnnOcIlTiMoiZpE9hz1jgBgDKFhfkGZgYpP0t81qRUmSBiy7T6nTzxsDFjsXWvTacJ0GtU0ssoi-VbHLawBT5bSJ5pYVMzFrMNVm2rd5jW4dzbONbOTVfaQ0GFfttcSIamvYh_6wMtpTi_2CNse1YilvSvvIKPS-FVz3C7xCTkj7n1fm8nLEQPasOh7OpWiA2lp8hDQBjQ9vhircbD3tGveCdoRR99lgoJ-2cNqOZsily5yY1V9nuRFUxxMwLr7N8Nd6dvhC4_QnoFwJA2Xj07UQ3jsB7BnDl5zskBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEqw26VuGwbQyrsuvl_c_dOWKesvODMGwpec1CNjCiWLFNYka0E-bZDwMsA5Hiwn8KpMMnU8DKbfwg_ggkj3OWqG3mftZM20NESrwaGJbPtZPrEfr93p8IJ1q5Drt1ALxc3hdktCnnmJXUeWI1Ldw1omr9ixYCJ_3jIGoMpVejxzfX5AK76R9MjF_CQGJT_OKGTDvN2pEDu-9fqBU-iwN7VX2L_4GSRPHXrR3cWUQcNKzI_zOnoWA-Lewf6wwQtDSteF2jVpSwFKOBMBBfsHSxjdKKQ1FXv61j5vUCck8cgO7SFaSGHGb7eGR6-k3a3y5xS87wKw5ta4kI1hFiBBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXkEmTgDSzUSqF7Xay4zEODgtAHW8iukA7JkwtkZq_JPkWiAgb1XA_q5yLo9KDSuaI21SzI3PT5g4n-XUnR2oJ-qsLv29uwNmKfTdoSFSvWkRCpSbzc39I7-8VeH2dJNQzNRQrItHcOQNoa7tA_w6mVzNpoASSVJ2nOkha76vdyz52eqOZnQhwfd3PR3t1F7gmD87AumuGUYiZ7KAG5LWkUPCg1StJIzpv6idYyMIjoSoi-PEK3HDdAwq6EI0Dh1ETxmpktS4rpBDNlpSGIr80Hz_3pNQnTHwjPgU83D1j4S3b8KzIdrBAyR_Z7-YIJZGi4ybu2ReScn-m69cutzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wz8kmW9xbyRhMKPpm3jZLv7Pp5ULMv-OK4CIs0Ar193n09xbyr0kKlyl3Cj75dnMoMWjrsaG0JqDsYn7ptRpod5QSLq_Gh0Max4UnLUM6OjdTXh5l_XPVIIZIEz4WlJ6AV1_WG8BwuejtoQyhd9H_2Pr1odUhWX7vW8XGeM3UgEEasir-GFDM0ayMVXPAAltwQ0CuGLbnQyCYhENA7L3vEChL1WE7O-yBkvVyhFu72KvMbVwzKmk7zoU5NxYYekuKInJA0S7dy__-s6lcki5FRf3lY5wEoqEJy83T1sTjhFszu0a5d_5RyZ8FJoMFUMAwOUeXGxrJyQhiFW_yza-9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=pb-0JEfPt5ZOHt14q1cQfBiDGq03lBBmtP-U6JlMipwAHOVY_X_ipmciL_DtOiGh1G1Dm8PCVxKKQR5RjdUkKj1krkdxnOVZYINqsTRJeKB8uB64WWurO7eC7skOvh4uB19EI_nPILbwT-jn3YwIy3DyrK-4uXCxilC9XdGFg1PUXigVLt9oyzMiyHOgYO-zREzpVKsPI5Xeuq1HZDM_GfFNZa8B99F1-tj0gZVAXJqUNr2FStQxEyngH6FHTKzfM2GttFNj5Crg8VszlG3i3_c_qJooh7rkRubnI542rrIjxvcM9IQQtnzjdP3K1JH17vC3nrvGt3zYi6BmCkrL_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=pb-0JEfPt5ZOHt14q1cQfBiDGq03lBBmtP-U6JlMipwAHOVY_X_ipmciL_DtOiGh1G1Dm8PCVxKKQR5RjdUkKj1krkdxnOVZYINqsTRJeKB8uB64WWurO7eC7skOvh4uB19EI_nPILbwT-jn3YwIy3DyrK-4uXCxilC9XdGFg1PUXigVLt9oyzMiyHOgYO-zREzpVKsPI5Xeuq1HZDM_GfFNZa8B99F1-tj0gZVAXJqUNr2FStQxEyngH6FHTKzfM2GttFNj5Crg8VszlG3i3_c_qJooh7rkRubnI542rrIjxvcM9IQQtnzjdP3K1JH17vC3nrvGt3zYi6BmCkrL_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v45aN8AYp0ESujWe_36Cp9jLoQbd0swzzvBemSBu3KtJoC43DUbi3r5BboikZhVx4Q4eoNs6nkY4FxxvwqQDvOXuczUJfe_28gLu_GY8TgLHD7a_But30vM21gE87m4RMOWRHWd7xzVmLJsrAStuLP_TwFEkWTK0fOG9v9kruSNR_jqcF3h7Na_vbQphNRYKkL-x108zIpitnfmlghaIHVQ34wGTbHWmc-S7cZWKoa1YkO_BRjlr5oIWYQHVUCnkDM_8Fy_IE--Dr__u8J0qkpzEuupqHVkaJnnt0wY_WfMJEg7nB40tfCyIWOFRVtMPyBWyputpCrwvvEi6Xho9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6bBcehNq5GktDTj5St4V-CWcIay1arE2tKLw1FwqM599c4H0kRE3xdMMVEKXAZfTpQfiQfepYTIP86AQawRYQOBOUOFTYmqqTPxFNVL0qKfSyAw9GeV-EjHphfOeHDCvqhrwaYxahvadasf8TnFHxM2NGHIp_jvze53K9iSsf293Hidr4Kku0W4yC2wedI4o3ft5TE91LXxCw2t4ehzY_kmwvS59rPdcvkKyKGhL7Yp1LdsZP4mWwA63xU4bFWq93Xb59T9EhjwsTTVw-Z6dCnphNST3GYPG1HX90QMMLJhZlXg5oXJgihz_oOKHcmkx38ZdmrZswPt2WdBt-gRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpjaN8y7tmiCLxt9VM9AjUOOO3AMXmHdGRwu3ptMXy_eL8P3SvzSNGmp1zw-ZkpeArJ9Kj4gcEkmtH8DPTfGhvPdbFAZvf4icJMUsH-e3gjaNuvuVDmWi64h968vw9TMv8bW0eV67x6saVBP6ogljqflzYW_fKwUJDjWReqNoVYvkX5OszQDRxjXurmGGVYGsIRFaoHLJ9C3TJ66vkudlh8qXXF6Qm2cb3cJQ24r1AfqMDzlzJtg5oN4J7c4lAnizDWKbI691oOeH2n4vT_RZq3oyPIDXP0CH5NAoWEEwAb8910amzbFZcILap03iifcKyH7UubfoQV5G5bAbkYr4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-ZSlbiki1-JzBESDZ-pRFzezLLV7uw-eJiRy9x661y__1GdbFZ5Cch9TPlJWl8q9qV7uoutjFzLV-Aa8mI0NNkuQe36fvVA6-mOgJNjwhlmp3K_ZInVktKBbFvtH3O6MpV4v-lPQXM0yDRPDltIWGjwl7NrapQIi5WqPO3iZhasJrGq7Zw0wBJ2pa51ppj12Qgkckd4v2bcCyOYIQjpDgP-r4MZNpPbIAPMCZBtKzycQlJOV1C7QCOxySdOruFh3P1TjfARexY3l99yVG7Y2DfMR3gofVw329AOh_GZFSRD_s3m1msrEsoLS2ZdHOBd3wLUX2gnVF7p-OPFL36x6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=iWzYMMFBnPtW1XLSNlNU3m685tT8n0hZduzT30CobrdqzsZFYIv4rfBpoxnaJdTP458tmg0Bj5UAr944h5Fuu0H7jqPG6G0ihJp5dqhAQN3vQsTd9M2MYkJODTk7CyFapnflouCv20e3A4ump60dFCYrQoqNeAzJfRbxIuWW-jmWUAhjJAEgwJeW1AI5HAmbS0qbz4kMKd9WKZlFndKpWXh1niKLiMa468KaurrM5nLrbHt8m8Y6P0lRpu7PNISX1IslSykau6LQ15i4wTnVLblsAjhaqW-9clIMDOoAfKpxFczCmzDfCo5GuTlsis0hfxb2Q2H_SLpz1C7Wo-hDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=iWzYMMFBnPtW1XLSNlNU3m685tT8n0hZduzT30CobrdqzsZFYIv4rfBpoxnaJdTP458tmg0Bj5UAr944h5Fuu0H7jqPG6G0ihJp5dqhAQN3vQsTd9M2MYkJODTk7CyFapnflouCv20e3A4ump60dFCYrQoqNeAzJfRbxIuWW-jmWUAhjJAEgwJeW1AI5HAmbS0qbz4kMKd9WKZlFndKpWXh1niKLiMa468KaurrM5nLrbHt8m8Y6P0lRpu7PNISX1IslSykau6LQ15i4wTnVLblsAjhaqW-9clIMDOoAfKpxFczCmzDfCo5GuTlsis0hfxb2Q2H_SLpz1C7Wo-hDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pppdN-cf1mR12nxTdwGUV3Kyh8IcsDJBNPkEFC7BDN072LCm8fKtEhVk8qcHOKl2-uTDcYj5oSaPz_0vtBBgNvLFgWg5ocA6oZuosxAdt6n3D74tBoGiNz2gme_gmhumWowp1_Mi9-YAF7H5gUfJfyVSZL1-9biq8N9Xu5AdGuCFllxPQSRi-vnYhSUg-OeZRiu7x4CWr4vn9-UbLMFoykxZSwvpSbq5hQCaw3L01fDv9Eg_1F3KXfUMs6WfMBM3uBsyZs27jTFQjkvu5veYLGmQuvAETugSgoe--McaxGc0CnazU2-IyjO8l9I582UbjAsYn6yrL9nITfT3XJTPAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtgKBfY7_-ZD_FJ5b2CxuA_eWF_xFmq-s3zjRSnKy9IXP7OUWDqhvOZ_yYTXXDIDb5XivjwAwIDYpNO987WVBNzqV2D3xvZ_ue-DxwceJXhzslnJ9HL7gDGA8_dEhy_eUMvF_H2fZdNKYweTs0sJP1hTZ4fjKIfwD2KZpjhBVj0OWGvqzfuzE265Idr0Hy6rDESPKTVGsr5DhoIvTIsRsinbOLlFYQN2XIte_likjax0RyWXnwTzwJ_cyd65emWC8Hkxfv8nyrZSnW1nyHx7HE77IjaS8LuQHpl1vIpNPbSbAQvJWxo_gFSCRm6WiYtf4LIygbEx2eeBljZCxy-tVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrOEyaWU3UcILtvSd6UACwVxV_UMnF0VVz6i1pYWSraL_bu1NGBKFDZZHEvOpN76rqBcHgm85VJ4-GB3IkQxKC9YO47xwjzBReVdte3OmtGKSS3tIoSQrsJVwGQPVhzJdO5I-VYE4DCEQS6cqZ1oPWQpwQfj0zmYp53UDrpS6MDzSz-I8-8t97HattTt_kpyayHrt6B3leMgAaN0RSKfRE-Qmt9Ls2pQzRp1NKIxkA4PUTyFNd_7p5XM19_pFpGeuoJhahDs4S60JEZm3BOnaTLDaAdrOaTs5geCdcgsUqFI6vkmKEOSjrg5P53Sw-VPEAuRpSannRJrtjAjKhrjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=jrlvXp7_GkLww0S8NzdDMymM4_Jq3X4ijqzTg6IRYQ7LPPOo_lB0XqWsOVPL9kbS-vWZk-25AjlQWz8QmHwDYbwJaKtsUIHLhm75Wb64INMGqWW9wvvcOENPj2E-KqX1V7tPuly5Y-kOKpel8FNT__E5zrfQT1PWTIsQCnr-eflB0KFYVfItV3VFNLnFcuSmc95hN5EEP9RRXpHmKSRHGV43cyIV2sJ4VjqIB7o9xif3b7wQ2-ys3BOyqtp-EB-vu4DpRsxR75t5kzOVnWB_InVwzO5hPG3u2cyA6UkdJ18uHMJ-MRvUkx55_7atZqPkkzALS3v1sFP87ra0tOPhgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=jrlvXp7_GkLww0S8NzdDMymM4_Jq3X4ijqzTg6IRYQ7LPPOo_lB0XqWsOVPL9kbS-vWZk-25AjlQWz8QmHwDYbwJaKtsUIHLhm75Wb64INMGqWW9wvvcOENPj2E-KqX1V7tPuly5Y-kOKpel8FNT__E5zrfQT1PWTIsQCnr-eflB0KFYVfItV3VFNLnFcuSmc95hN5EEP9RRXpHmKSRHGV43cyIV2sJ4VjqIB7o9xif3b7wQ2-ys3BOyqtp-EB-vu4DpRsxR75t5kzOVnWB_InVwzO5hPG3u2cyA6UkdJ18uHMJ-MRvUkx55_7atZqPkkzALS3v1sFP87ra0tOPhgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA2npbQ_gm-yqmjNvND48PIsshHpvfcbVrRYJxwq1dD86n4QIN0w85B5ZaYkhg6QkHDD8TN8vIwV4VsZ4VbAb1KSIOzz35J8vU8-V-52vUwsnDvn2pmCab8tCbUo6FNL1rRh7RaeOKkVsCO_gMNNJj0UeY2zaPfoAUES6-k2Vkr6Oty1lGFu95CPZA8YLYoaziu6nJ6zOY0V6YqtN0B0VoqVT7QOCb_VVDnrHHiy7RYma0IbQCW9lJ-MCZjQm5F-IQpBHJhbI84XzO4SU0uWPrJulsUhkFt4BNphA0HIZMDJRzzlCSNABldo3Kx6GtPQ7nTRZ6V4ZUGGFFHEYut33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-2hJ9pAVkhE-hDx0vIrwXoLqVBOTbrXWPEOPJcpC8uehrGm59Nh8YqEif_QEMK_yyRiVF8QqUp-fDYQgNoWQ9mLLLRXB7DysOIwv16ia9napQU0EVm7SRapkPRfNsz1gaVavuEK16QijN8mOeW44GAixdKErcTk4Hsv1vs9JiHsWx06FcEhQrhuOqPScgmy07MeOTiiNK_X-vK7T6TYkg-i9Io9qpNrtvLBgxDcvTk_Irzj8TPpRthBeHqRxmL61TF13XwWhrzwThHniZGebte1ppT8uI-R8HAN5pSIawgsmZ4CTrzCMsnH8qCa59And2JTr4BcFBfyYZwBfEQ7-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQKpFrsB9kyak9iApr__rJDKg-FpdwAjT8rse_8yA-k6M-yyQiNf8ZbQQMk8K-6TETy_D4e00_nMf-8DLDLkSUnEDK5xgRuFMPIalzO9Gy3gBUiMoVRpjpSSX4hA-BSrmbNBYJcuT3q-0p6y38mWhlvJxursNDC76GD1aSR1ta_6JhAZG4QtbREiMmJCOzPmO33p01vkUoRlcwA5ptq8Uq8MlPaXKn3B1T7AunPAsoiERLzFCuYZHx1KjLd-bnYyTI8-bjtZvfcZQeq9_bpDpCOTBVa0Z0SHtkRaVnQje9m2RlVUe2NdcFPbe5QhpdBjY4yrNuVfGU99PbWjqzr1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iijMx9P6TDOj7XByiSjMNqCQxDPG11lwuxBd6I3pr6dClG0UlYpqoh1XMR5jNbgbnECORRTKvKCvknW6VXtFHoPdGd7PMaLuQRIDFgedfFFXaAIuaskTY2JltbKzEcQlgQZkBumEZjSqksuGHip4OiVASNZW92KitluOGBItBWonS05HFcK1VQqUXZd2KhSF-iZ1bsvmC_PCtVEp0WHfhpUM9hkeE0cFQ_sFJnNCTPsF8Jw42IWKti5evj8Lk61U-Usws5j5a8YJmkuzQhCj9WYQ68xO5R7xByweyzxgAaX3OEz4FKgSUzbJziLF5hBtIVjoFAv7HqmUqd4jNe5DzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyTE_jrwHM8sB_e5Vmrf5icob5sEcnrIQ08_JomIx1JpbLeBQGfXMJa-fLF35-1F-0wQdKCJnuwggyAAYMi0iKrvIz5ww9mSGLmO_X9L5IjcZQOez71O4QmK3H4_7RynyPxxvYZFcDhB35lrskOi6QJI_tqGJeUGzbEKMmKn5WHgkb4NPHlGH2rtEROIukfLLHw8veIiLSBXOYaigPp4QED11IEXGiO4PfZNdMmgT2K1Dm2zhVju_bEZtX95Oaeiowi1xHcPYJHulaZX11V4p2Z79ZU1Wf7K60Slma8WblfOGkpAVv_DVTZWm1DVPqOmpjioK77TcXVnUHOwoHKNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=JMGd1pLjdBr05dOey4SMw90EyKxIJ80-IrbMNxBT1AAoCRxXMAsZV6Nxmf4WCg_dKrGHuFzIQy52xq_fmv3w4aSj6g79Sw1pkBJzbmllBSFXD-6LmvJRZu36CL1hqCqwxRkhIZU6ND-fWRxCMTFWb6msi_Rjkxs7ktR6NsZW4zGh6hBXzfqLPnAmFPu0SoRZW3o-HRxuQb2D5iSFKyq22nJzi9AmMIBdHkGvLMm6lhAoAzWLvFFTd7J4KZlNAxHDk-B7jS2MaybJACIihwkpbdiYmyt0_YiHrHNB93rhgBeYOwINTumhjD3nNpNz06igNB0T95W0ewA6RnJarcPbZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=JMGd1pLjdBr05dOey4SMw90EyKxIJ80-IrbMNxBT1AAoCRxXMAsZV6Nxmf4WCg_dKrGHuFzIQy52xq_fmv3w4aSj6g79Sw1pkBJzbmllBSFXD-6LmvJRZu36CL1hqCqwxRkhIZU6ND-fWRxCMTFWb6msi_Rjkxs7ktR6NsZW4zGh6hBXzfqLPnAmFPu0SoRZW3o-HRxuQb2D5iSFKyq22nJzi9AmMIBdHkGvLMm6lhAoAzWLvFFTd7J4KZlNAxHDk-B7jS2MaybJACIihwkpbdiYmyt0_YiHrHNB93rhgBeYOwINTumhjD3nNpNz06igNB0T95W0ewA6RnJarcPbZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=dTh5rqGlcr9tlbIRBtZHjNwmMVK24JPHufGWXJLgevqEvmpF8x9gzXykNvwWp1tWJK0MwIDlQQ5FpiamKOumqIslu0vgVttyFLb0xxRMyKSM3_8XiQ7bFmZVdjuklUc844RkpXCwYz3LIKhgZ__oxPuNlu-3aI0mQJXLXHlP38iKR7euctEnr-3WPk-B1q8lP2VRoWYNqVCAT1ldnQBCUJ9y-NlRjS-r3peqxbBIpsI_LUG2dwxAgyNwY8_zSQEJWQ5r4YcJBqRn-Fk4__KxReMnwigYhrHh2iKMzJzsjLap0_0xt90C-sljaqCU6cvbtmRuybpPpcrkRtzKhlMoIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=dTh5rqGlcr9tlbIRBtZHjNwmMVK24JPHufGWXJLgevqEvmpF8x9gzXykNvwWp1tWJK0MwIDlQQ5FpiamKOumqIslu0vgVttyFLb0xxRMyKSM3_8XiQ7bFmZVdjuklUc844RkpXCwYz3LIKhgZ__oxPuNlu-3aI0mQJXLXHlP38iKR7euctEnr-3WPk-B1q8lP2VRoWYNqVCAT1ldnQBCUJ9y-NlRjS-r3peqxbBIpsI_LUG2dwxAgyNwY8_zSQEJWQ5r4YcJBqRn-Fk4__KxReMnwigYhrHh2iKMzJzsjLap0_0xt90C-sljaqCU6cvbtmRuybpPpcrkRtzKhlMoIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8L6v_iA-JqCmgHvZ5o2XqGAdXLaKNxqCpC3nSCU167Qde_7uruWvOWvHZke0GkFHyUIlK2WIAhUs1NqPYLZPgnyzRwBJo7WIjBNyEZtOKg4Ug4axEcfSzvQXD4S2DyjNb8pL6pIpgJoGYNAhtE77-jZ9ydg_DE97kZk-JIyto9STrqseh0Sa0UUAQlHVGFQzWMWg4ns-zglFgZv4MuoZHhGhu83q5o1KOZWiwSmkx41DuaA3ZLTFTJPn3yOYM1sOebIc9Rjx6zs12pmMjsVNE3SQiBp91VsiBMt98K-UkAZgn8Q8-i4IcpNBJ9kI3nJv-Pi0bsY6qYktHuBYV0alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=CT-TdhTkhk6we4tqtSE5coz1TIWk6qRkUL5m5m_aeK0wXAdEJTM7jf1oVZmw1N_AeGiQXLz9j0WRFUKunL8wl1pGEUqlEkuR9fSlEjfRw_EUnpRXDTmLP5muYut7AApA6L5h09DQ5FErqzJuYESBn5bwipXsj89NBkgbtT8bmiR3ikOZuZI4nzl0UcOP3riVxTPO_VWSlFRfj43O7fgNVvtANXsqNJFiF-R5JliY-VofLnmYIU-G2ubnfa7L4s1-hdiK9wNTVyfIcd0jahptoCFaM-boHZsJAp0d6Z5rB5nU-MRr2oqcXvfVTbIADQxDz4zTbHgqzuLPrCtRQVlF2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=CT-TdhTkhk6we4tqtSE5coz1TIWk6qRkUL5m5m_aeK0wXAdEJTM7jf1oVZmw1N_AeGiQXLz9j0WRFUKunL8wl1pGEUqlEkuR9fSlEjfRw_EUnpRXDTmLP5muYut7AApA6L5h09DQ5FErqzJuYESBn5bwipXsj89NBkgbtT8bmiR3ikOZuZI4nzl0UcOP3riVxTPO_VWSlFRfj43O7fgNVvtANXsqNJFiF-R5JliY-VofLnmYIU-G2ubnfa7L4s1-hdiK9wNTVyfIcd0jahptoCFaM-boHZsJAp0d6Z5rB5nU-MRr2oqcXvfVTbIADQxDz4zTbHgqzuLPrCtRQVlF2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=P6LpIIAmI3KbWUWIugNDz0ejQEqaSH7YUIU80oUhViuKQaJLWDoTNgrq0wllE_ZeZGOodNxcJQ7519WQ0u6zWfy9zEs1b2OX29JjI01Kj0rwFhIqHBqdzBA34warkmP_4_ujdvPpwarZJi8-U_XEJ0uNyorgFYYUlilvuGqyAF0D8f_Ox5Hg-ixqrjGXrnYPUNV7b3_SpBRHpxqVhcDah40168JDAo5vC0xn5TmYLLI5jty3kE4yYoX7GmtsryF8PM4TBr_dsFfBJwmHTe7osOM0V6JDlbPEBXHPPlQisvnPYKIFhBK358uzIF6YsWLrmu5u9BNgS0pRMoRpDQmYwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=P6LpIIAmI3KbWUWIugNDz0ejQEqaSH7YUIU80oUhViuKQaJLWDoTNgrq0wllE_ZeZGOodNxcJQ7519WQ0u6zWfy9zEs1b2OX29JjI01Kj0rwFhIqHBqdzBA34warkmP_4_ujdvPpwarZJi8-U_XEJ0uNyorgFYYUlilvuGqyAF0D8f_Ox5Hg-ixqrjGXrnYPUNV7b3_SpBRHpxqVhcDah40168JDAo5vC0xn5TmYLLI5jty3kE4yYoX7GmtsryF8PM4TBr_dsFfBJwmHTe7osOM0V6JDlbPEBXHPPlQisvnPYKIFhBK358uzIF6YsWLrmu5u9BNgS0pRMoRpDQmYwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm-e-tGHb8dg1SZggiHlr21FgLvXkR-qu4WH9TP81N6tJsV5P10Tzu_9k-pn1O1qHzgUbjLqTkhAl-SrIiJ5HnOIoR1m8NcGeeGrwsNnKR6dyvhA0hJGdF5UDr46yWeRqBFQrjfT5v0fIldhjSPE9eS04Ecn16pmjEcBq02HRX6JSfk3y2ZTueLmr2Gh9t0-LnsXOmXi_YJqhwNR0fUt6X6PC1NN3myrCqCQnm0ma_uTTix18vX80ePJD9gjVJCOGTuLDbV6GXIyK2_ryFdq1aPE_aolu4pYnEqVZOtdKWlNVUPB1jbF1e8cnOt_PgqgtUhLvgZV54pVh5jo2xYFLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6iiVuQst_n5fGFggNunnS2A2wp3D9HC7-ZR6xSl4Y6FirdBuJNz2VbHczWEsQbbEw7sVlzupf_sffHc9CTGLQbCYycZgSjiSIjRpTIUIA2WJ47xaU7ID4IHB_dVdvkaqimSbzV9CgtyKu6arSxtscI-4SrCa2xNk2liFhlHFSun-KTQMsOhw9sjiJDRisI_DKeS3f4tzO9DhRYI8Kh2PQvaDYBLPjR7CcGhWtEWZ8bbhpUbfrSSkkV18vDbf1hAH6LquPR4lyJwQfg89cGJ4dsb28giPT-jIGS2m_cUIjNVcPM-aqxh5tOjE7Whtskqm6X1OuhADTqVXQc77MhsMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=E_BCXaE6yng5HiV9_RpTcmR4d6c13dnyUvtisEOhwjdCQKbr-ccRkZCUVIJXCxIm4TV1jZhOTVorGGl372P7_KG2qKIvyJufGTCkH1QXmePz1uLwz-a7KEDib0Jqt2IQB_VKwvi-nKzR4hkl6mgiTaCZz2Yyb4JFg6D8_RYxGf8DONd27oXbClTJzRMzYA4_vCZHYiNvlfzEM09sxNET_KcVX1sXxEYA_1zR-pb5dJvO9CbrLOk5N6NsqOExjLpjcUVdETH7nDlQAAJjRwTqE6W0Tk658v0CWRUa34hgr5QH4E0LHABO9zkZxU_VR9jsFDjhZGVsibu7jeEibfkuFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=E_BCXaE6yng5HiV9_RpTcmR4d6c13dnyUvtisEOhwjdCQKbr-ccRkZCUVIJXCxIm4TV1jZhOTVorGGl372P7_KG2qKIvyJufGTCkH1QXmePz1uLwz-a7KEDib0Jqt2IQB_VKwvi-nKzR4hkl6mgiTaCZz2Yyb4JFg6D8_RYxGf8DONd27oXbClTJzRMzYA4_vCZHYiNvlfzEM09sxNET_KcVX1sXxEYA_1zR-pb5dJvO9CbrLOk5N6NsqOExjLpjcUVdETH7nDlQAAJjRwTqE6W0Tk658v0CWRUa34hgr5QH4E0LHABO9zkZxU_VR9jsFDjhZGVsibu7jeEibfkuFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtMFLoAezcKXFS-RhBPcQLvG4rSXwuuqknpDd3xa8avkXvAlFr7Hmu_nCqePamJHj30iOXCxorsHfcHjBvFpXXX1oOrqrCSNZAEphCGKxCJWh4PCwvXbSvtJ9SvKIcScnSDm07t_WiHHwtD7DwJBpCW9L-9ZuL_j34isrSQ59X1YZeSIC5F1wHVJm6w50CkvSWnpb5Z7XJBtUYMToK9kBrwHd0t-lgzEC3PYG8lgRN7VQZE5YBfMqjBgB39cwuN6qAxV-dezsE9QMwTbeSz_eX6y52WqGJjNToFX_paIC2ALyeRrQdhL7trs2I4cvsKJxix512AvIjhFfUnKKrgJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dt7hcK68r-eXMRRHnqCMpqdLPwbtBYN-8AtXlrQu8mPe9jue-0AFQJUOpVf6S2v0vjx03ftzWvBRHc7PqYLbrGWxABdJ1Mly1OsiNi4q0UuHAu0saoVFIq9KqV8jYtCi03c1uAdkTE4VTwm9IQfCeM2yF2Ntd6ZlHZOfFK3HTWAzuG5r7i64MnmapEeH2g9MasE_PUYT76UgM0YmuOAE1wAtz8RjdaI_0iL4v7JOhHGPOHGmAw10HmEx0UOuCXwyd-ZEKAdfU353cTX2j3OpK788mGol67jEBDZjo8Y73wZUwoICAEXcadCDeua-47t04bdyvHnv17H73oHeHaMI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWFl8EOK0Svl0-z0L1cD5mmk-iPUcOlqBRfVELzzZ1TeRjI_fjbSMaA9D_oGgdiGZlhYlzIUOo0xTy8-R30N3G0iJnxiAlSciVAniWZFurIbMkkbap1pa9x4m4P1ZBNBvmV2f8iCGEsxx06hxeLnKAEHVoIyhuLq1yATOT5N7K3thzJCTFz7NczNNPN9oXlu1kgW3-RbjN0v_sbq1cIm0CbA2DFQTPDtRM02ksliag0KVY1nazihIPF__-qeUWhKudqQckYUsaT_29JsNAnbGEMmAcxKAtsji8CejBjgAK-pX6fxbQt9_CCYqJI7ny7ijUEBcSWZjunZrXIY6VHqog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9ycdCWPXdFoQGVlU7FG_E9sVEJhBsMMnsIoIYskMc05X39qa-yWmwCpJW86TysWxiSJ5aooRZnEYsxJolIURpUXk3QdQuk4Y6iGGmcicf8pvFFRWL3J8rod2e1RgLeiVla4nLnyeTXWOM7bvtrsEfDmSplWLvOdrzWUVyMxI13fKQRzaK2I5uNVXWn4f1YlDoIOsbhmnr2gVsh7OTNtqkZuCAsIVproWe1kjdGp55q9x3WbPdHAg3VXBFDqAq1di9BX8nzKnH_k0GUKYtBzP54K-OLisJpFjbGjZvOtPDzatf8zabmh-QIS53IbJc__cQ7ZZlUFQ_RM7oVs3rdPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCug2lYE_Lg8GSGhUm4WcPW9Zi55y2BGYgg0W_IKnlkOx-gjGDgKTLRX2COMmV5du06g4E84zS31QXhQqMllMzwuF66BJabOAucdGEqCmvlIIOt59BhS7pPImXu_DSCGeWhTD1au1bw9nswBu2_CfuqpWw6yjnJthBhlge8wrM35-kiOnth5uhYeLQ6KPCKje2Ok0TszmTlePks3zF76ptwB1lLCOONXVrihwnOvTwGhqi_g_0TXqnfr_4QWnX2P9_7k2yRRl4zVQFGBDcXzjfec1UazSsVlgYsHDw6Q-Bo12PaZMJWH-yGqJ0OFp3thmKfMp3wRgRQybhVJGlgMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0EOcLAZ2uwP0ozeaVsm5lBjJvUchk3_8deluDgnsA5NNV65YY8kMmEzaFGE11QeXVZ0j0ZNTCeMMfFjO63N-hLbAFOvkEtXYZoyL6rqfwm-E1MQFCiG-tXcPsHIVPCkSUhEXrAs_sjPGbEPkTr0laBdD7LkKmlFSyC0NOFGqEphpGu9x_3-lHmuw_FG12PuADroJljiT698n0VBG47dwWM8AqCq6da60LPc2gmW43aBhBPNqcIDZ2ND8k4rRdzeTeiFADI1mXIhl5ESmsmzsS6nwWZVQjgj4mqGlxc0OG3MwoR2eR5zUeV2Mr5dKSaOYE7k_caAyEEQSuk5wx1edw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaYkpStMYFO9WUwP-w_1Kq46pcijRpWTfyb2Aed-J6ptMH0c-GTQuoEQ53lyMKPL8W6It0ZAIqEk6LuhDC_RM0DBVuzuzVCFtYy6lH7A8eqfenCfVdGbBT-AYI103DO3lwpz9i9UQct3UXok-w3pU3UaL7p-d89bkYHTcvS7aTvxGbtIkafSn6NvFhM-pIWTJSkwnMkTtIToDlSg0jpQPSZS82IH4oDAWI_UkMY36WTD96-9IFh-dG9Gveo8kn-YjfUFzCF3gF1Wbg5pcK3WLL5Crk6sY02jkGqXD8eXLIHslJkh8RKQnLy5Dvrtd8PbO22oBV_qb3mlJVCBA4T3BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9u8Yq-zU5PJrV0QCHINaSmvOZQUeTnVN1KnYwurAX7Xv80Z9P6gnKBglnR6uIVgTsTNaQoMBlKbjMm1ta_4Ub9yrIVgI9JIQGTV-JsMohhw8a-Wm4f0u6y5nIOvPDqVPg4yWpStbVDxOowg1y4Zb8KgdCM3F6TOTgFFBkGD9_kV71HYSs_abALtOr_R4nr9Q4woFOn1ybAyxb-TkOI05HD_qRFaRpGlh07Sy_4JnTkcciXQZkM8ove70AT3qWiPR16AesJnA8zVyOHjWLFUDxsoY0scFtu3ivOnoT5tH2UvlVOBQ1bgJpZCvr-hP_ub8wmqxhO0rLuWrj2T_aGd6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYbM3sXIgFNzVj6ciE_bvFZ8LxZhNBgRVoSRlzNzD2YhNbh89om4et2LyjnMPSpxylvqapkT25Sx7_OfBnaFIEiNwEfxU3nWHExFf0mvGXEPvA60Cg5qMihtWshKlvnG1oaAQn0xEvyws9j27X0ST6XjsUXdWVgslAgZ-zuFaceErksVAGYkaylo-Wi1DFYEOs6gWF9de11LiCVK6BnNG1txRBk3C_UO79Lj-Koz7YAHl_UoaMBRI3aADN53oOTmyI4lpYRxKfjmiZKWIVSM5NiCXhh4d7iDGkvBBdRRJishxoYkW88CfppUq3Uqpr12pesU5vZbBp8CutF1L0e68g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLN7gMlQBnNyYztQG4ZIRGliCGKn4U1wWB-VMS4uka-TQzGj8YBS8znyX7WVEuw0dVsRa9SKHQl9DbQ7tepinjZ1070AeZ0yTRdvsKg6zOld2QNFcWcWQC1v7-DkGsWBiVpoJzX4lI0tUHM7-yHRVSBvBbvzb2li6bmxnxXkIAaLfKfEY7hZNB5SaF64pPB93hyTS82thbgUuCSxN4bqPoOcSv8tNHMG1FN5_RYZHL9sNJ9NUgfe0h9fmKI1S1O1llKJuH24xxSFZdBNK5nJCyccullt5NL2oBjXSDUTpoxNwSDJnAY1WxytOU4kBr6J110I_vhHsujlS5o7bUs4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=u3fAelmWRVbyjayjLj1zQWagSYcgQhJcz5MMWFH0FzzcEMfnwgDF0aIohoHJ5AEtwN_758RAGCoYVJTwhZoGBlgDsAUbhZRXwt-4LRTkbU6uR-BNcJbZOLxhq8NoLSBoEEnVqQPHQoEO0VMKDigFWHMN9fDs-B7xPCoVnQE8-ly8_V52aR4IXCcZKARBszIUqR46oppM_h8c5m51OGylFA9BQ37v4MuXDQeY4TjA8l9l-0tYAR9c8y1s5hIN8XYiy3QEOmYkrAq26c246yTAS0Z63jMAuUtQf7wr5cQZfVDM6rUlKpPiZPN4Vbezr8wVJ_tL1ZWRslZhtohp_9arPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=u3fAelmWRVbyjayjLj1zQWagSYcgQhJcz5MMWFH0FzzcEMfnwgDF0aIohoHJ5AEtwN_758RAGCoYVJTwhZoGBlgDsAUbhZRXwt-4LRTkbU6uR-BNcJbZOLxhq8NoLSBoEEnVqQPHQoEO0VMKDigFWHMN9fDs-B7xPCoVnQE8-ly8_V52aR4IXCcZKARBszIUqR46oppM_h8c5m51OGylFA9BQ37v4MuXDQeY4TjA8l9l-0tYAR9c8y1s5hIN8XYiy3QEOmYkrAq26c246yTAS0Z63jMAuUtQf7wr5cQZfVDM6rUlKpPiZPN4Vbezr8wVJ_tL1ZWRslZhtohp_9arPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
