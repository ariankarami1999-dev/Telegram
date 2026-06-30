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
<img src="https://cdn4.telesco.pe/file/R-Gx3Mz_-1VjddNgHpdHQYlLi50S90lyzFtJoT9VcsHiidNeojEi7Kja1faHJacZt63hd-dLI-JnWxoG2Q9lTETruhOCxHMEKzyF7WpPHgpU9gQNbSy2FcxtsaYvRRc2xFyojbHkHZLZvJ25l92iYaPrVoBD981nMoYXhtDPmOLXkDX1DzZrbNV9iiK9sosTd5rv2VMSSOk1hkwOhvQdhRg_qE1qQBtKaLXmV0UKeWUeCqrNnVz348Nge5nco1Ait1EdAR4a_LtYvJ5mFyufSUfl8V5iwUIpSgE_BpKAtG3bHyV7Le6IggbrTHNLlKFBVB1XUdr3GBUBp86EMUhAfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 02:18:09</div>
<hr>

<div class="tg-post" id="msg-131181">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131181" target="_blank">📅 01:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131180">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکریپتو اسمارت | Crypto Smart</strong></div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/131180" target="_blank">📅 01:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131179">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skJOU6Rc8EXQmQv_TdEfyflzjzIl5v7sBjSneMdDv_UCdxfxCQd4S_8eVCAdJKMnHpnsZdIiwL5zOzSix_emb6CcbZ_XmkN5cogafCYCZ7p0AwSBWFgBX16bz58GdZ5jJAjPC25tEvP9fbbtlB2FBEqvUZ1QKAuCEwXY8m2s5_0zc_CF957YY443L4aFgSokNIya060YAIXQUN39zQKJyYANrvNLof9Rcnt-NKgYm48sYdlWqGveB3ccSQ26kt957bMIuaRS8a2b3jMIBY-8ttq_xwZYtrlA79ruxlDo6fzjlToc4Gq-s3_D8JgOQwAHDaa_2Oq_cPYMsMidMupfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه سرایی پیج تیم ملی از ریدمان قلعه نویی
تنها سرمربی بدون شکست ایران در ادوار جام جهانی، مرد خودتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/131179" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131178">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfEm8lOE09nvbMPDYHSGYu1iUAhOXVJXh7DRw0YB9UYaiq34F4A8YaPwbS8V4GkaXy45czLOjVljKSPzOj1kl5yBXKsrLOMPOjhweDeFJ0MJUijjoWOFdxVKgUR9u1wy7ANjHz0CaHb67Zwf_OGoBDjPNXILB7VnxVgdIj97CSeUCS0Ay0D86FF6HB5_Wy3afaPidDg5BD8fUK95IgJRcFENF9ChRO8tyR8lSCMr6Oja92oCmdelprdnklQX2Jx8Yu2qeB1M-dUknm5hymz0QmiBACDV4aZpxCy1E65LiWK45bAwAb6p5nbySqpzij93P-1zpm5Mknz6DSLGPTAbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ترامپ:
ترامپ از وقوع جنگ جهانی سوم جلوگیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131178" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131177">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_OADxOZeg47RvVcMlLvdJntaD4NKo_u0EgQjlOVHvsO4ODFEr1esNNIg2_Zc8HnJHR8GnN_NfTAOwCD9uY87zTulSWCfN7mqcHDdl929rhdvp8Cs8smTT6D2Uhrq-9dSCt5KMR1VHK_GovNZu6xIcxJ5bJaZqrWShNRTKGIKKVjvhGiUvJ3vo9k2j5wyBTYzn9nOZ6qlc7FWysgDsdFC3-zoQSaJfFix826JrE4379hGT_zm9JRQTw9XzBQidp0v5xnLEwmgjDjwwznUv3D9pKy6FqqYIMBQBFMw2fv4pDzZ1_8e3kUHlpBtjF3GhFPI7dfIei43M0I96lvb4ca0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طوفان توئیتری طرفداران قالیباف علیه جریان خوارج، از دقایقی قبل هشتگ
#اخراج_جبلی
در توئیتر ترند شده تا این شخص منفور از ریاست صدا و سیما برکنار شود
🔴
سالهاست صدا و سیما در انحصار یک جریان طالبانی است و تقریبا مخاطب قشر خاکستری را از دست داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/131177" target="_blank">📅 00:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131176">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnlH666UkMW3f-GTKawSPtzKi2AQNuznZ_XSjE_VGW7l91v5iPQvTPqF3rr3iEfQp8Qwjteb3TM423-jM-ThG765_ln1xxUi6JH4J-bnjobxigGojVvA-AIGieyGt8Dh5WGUh7CGuXUTGX9vYAw5PydC-zvEy9Eu94gGbCx83gvfL4MdrT7R93e6tix0oQoxGkSRyOeo9FgauDPl1FadVUlFajeAu7g2g8aUBUiOGRsPrNUp9afRjq35rwxAAPbf-yEjOVitpulH2ciWmliGLs1ZoTJsGmDqRrOaM1UgdbnBvOhL3slGnk5cqk0a7utecYVZe934L8ejaDVH09tTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری:قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/131176" target="_blank">📅 00:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131175">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=c_Z7owsqCkPIyKtrnPWkqSoc5cdhtYWksfmDLG_gnFz3DMu23JExdwo4TKfpkZImGrAfXvnFJFDyqp33igv3KQYsNAwIqdm0rRoPkRpYV5cQIFI2YlvuCWtMsvsb5q7PZSH35W1iWfmvh1LZS4nB0LuCmX8KCQHxkzSemHwN6cnoJgOGhkYoj0p8Zgih_lCuQBsOdYXd0__NogKDJgybdAs7BqDG4WNZTa4eNDECkK7k8OP9Y_ohvNe1ixfFZmq3r-yaP56KPDYbhka7J6-30d95d8XIl524VQkmq8sLhbjo7qnLxEpxXpjGGkXavPw4TUGVbENxb82qyfo3sS-XRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=c_Z7owsqCkPIyKtrnPWkqSoc5cdhtYWksfmDLG_gnFz3DMu23JExdwo4TKfpkZImGrAfXvnFJFDyqp33igv3KQYsNAwIqdm0rRoPkRpYV5cQIFI2YlvuCWtMsvsb5q7PZSH35W1iWfmvh1LZS4nB0LuCmX8KCQHxkzSemHwN6cnoJgOGhkYoj0p8Zgih_lCuQBsOdYXd0__NogKDJgybdAs7BqDG4WNZTa4eNDECkK7k8OP9Y_ohvNe1ixfFZmq3r-yaP56KPDYbhka7J6-30d95d8XIl524VQkmq8sLhbjo7qnLxEpxXpjGGkXavPw4TUGVbENxb82qyfo3sS-XRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حال بچه‌های کنکوری خوب نیست...
🔴
یعنی مسئولین این صحنه‌ها رو می‌بینن و سکوت می‌کنن؟
🔴
سهمیه برای ۸ نفر المپیادی ردیف شد...
🔴
ولی برای کنکوری‌های ۴۰۵، با این همه فشار و آسیب روحی
🔴
کسی به تعویق امتحانات  توجهی نکرد.
🔴
کاش یه سهمیه اعصاب و روان هم برای کنکوری‌های ۴۰۵ وجود داشت...
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/131175" target="_blank">📅 00:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131174">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGBbyYKcBnGi5dkoQNrY9A93fXnXIRy-vyUQaoST-DkVNUNqbLkc2Sexuz0Oug6EpxvcaR_pkh4Qx_PhjEHdbDQhghOxYqYlq7oebspHDYt4gLFWipwDGX158TUWyjeIVOellMGecfGqu4y1EFuNJRMSGaNHgVRVWI5-LAu6ghi1VgiAwyPZrG71XZOYMW6d-yEu3FJlsR-KOXEXUxy1VuFhLACK7RoLtAi-Jg6NQHxjmRP6vTRVVRwpodZ_YFCLvSbVquhUNdVm7EKCphsPEo0iepXNgbWv3Pwp6uES2uWuqaIeoT_rhxIyfL3GsNP2TK9rU2m87Jh3CDhXp62DTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: قالیباف امشب خیلی حرف زد، بقیه حرفاش فردا شب پخش میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/131174" target="_blank">📅 00:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131173">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196a09733.mp4?token=ipmTeB0ZMx8TdQ37oeh2i_CL3_S782ltqomEqpylnjr9dAb7ZIgvD5m7EzgwCuGShEAu-pWH6V8Rgwb32DRtN4XJ2Ag4tKtyUa1Sy-KcPsgZ_deXqgd41nazsyY2lB4waNy4-IdUfOh0TcVddRF5ATGC6SzvD-0-F8ek5POkHqaKRS3zXOVMxSxeGpcazn-IqTYltC4bZmcznl1EOC0ASG06EYrXLXuJNAm-8yUtXt-F2GyVUHOHQ7MbAhxzoiKxPNLHSylXq0M1XKXjFgxXaC2pNzGuGII2ydCIeB8Dm4L03AHefqATv-THSavPZ_BlGdNEhJeBY0qJ-CFqzJD_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196a09733.mp4?token=ipmTeB0ZMx8TdQ37oeh2i_CL3_S782ltqomEqpylnjr9dAb7ZIgvD5m7EzgwCuGShEAu-pWH6V8Rgwb32DRtN4XJ2Ag4tKtyUa1Sy-KcPsgZ_deXqgd41nazsyY2lB4waNy4-IdUfOh0TcVddRF5ATGC6SzvD-0-F8ek5POkHqaKRS3zXOVMxSxeGpcazn-IqTYltC4bZmcznl1EOC0ASG06EYrXLXuJNAm-8yUtXt-F2GyVUHOHQ7MbAhxzoiKxPNLHSylXq0M1XKXjFgxXaC2pNzGuGII2ydCIeB8Dm4L03AHefqATv-THSavPZ_BlGdNEhJeBY0qJ-CFqzJD_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش سانسور شده صحبت‌های قالیباف در صداوسیما: قالیباف: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوپک صادرات نفت انجام می‌شود.
🔴
۲۰دقیقه از این مصاحبه توسط صداوسیما سانسور شده است !
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/131173" target="_blank">📅 00:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131172">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دولت ونزوئلا : یه کودک ۳ ساله رو از زیر آوار، بعد شیش روز نجات دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131172" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131171">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روزنامه «العربی الجدید»: تلویزیون ایران به‌طور ناگهانی گفت‌وگوی زنده با محمدباقر قالیباف، رئیس مجلس شورای اسلامی، را بدون ارائه هیچ توضیحی قطع و پایان داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/131171" target="_blank">📅 23:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131170">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ونس: ما باید از طریق بازرسی‌های مداوم، برچیده شدن برنامه هسته‌ای ایران را تأیید کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/131170" target="_blank">📅 23:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131169">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو درباره غزه: «مهاجرت داوطلبانه» از غزه همچنان روی میز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/alonews/131169" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131168">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
نتانیاهو درباره ترکیه: اردوغان درباره تمایلش به نابودی اسرائیل و کنترل دوباره اورشلیم صحبت می‌کند.
🔴
فکر می‌کنم فراموش کرده که ۴۰۰ سال حکومت عثمانی به پایان رسیده است. امروز یک دولت قدرتمند اسرائیل وجود دارد.
🔴
او باید آرام شود. ما اجازه نمی‌دهیم کسی وجود یا امنیت ما را تهدید کند، و فکر می‌کنم نشان داده‌ایم که چه توانایی‌هایی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/131168" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131167">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ونس: نتیجه مذاکرات مستقیم لبنان با اسرائیل، احترام به تمامیت ارضی لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/131167" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131166">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e7b409e3.mp4?token=WYTHXDV1pGXjQkJv08GC8uFM0lK3Vd4j9ZAHTFi0GMzrKGUqH5LKQow213DVjMHIsol5A4Sxw_zZbqLAkSOBAZ4yUGbOPPkscsm3czMAuuwJ8q2rStH_Loc2tu_zGIKrmoRoyOKaS1Fwqrgdn-92yLONqFjmvakWYW-g42XGPkDXiFYF7utHqklCpzDDKc79EvDkxlOjCeqOoTA4wUhEwHig4w4kodsOmbxwWJnwCAKlqOoQjuAmAW6eYOCRhSBNjNiN0jnVdLnT1Q00iIpurFbXj5zJxL4iKsYH75lDDFb_Z5O3usKGvs2ns43IgIzljIhR0m8qS1HGUkAooqlHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e7b409e3.mp4?token=WYTHXDV1pGXjQkJv08GC8uFM0lK3Vd4j9ZAHTFi0GMzrKGUqH5LKQow213DVjMHIsol5A4Sxw_zZbqLAkSOBAZ4yUGbOPPkscsm3czMAuuwJ8q2rStH_Loc2tu_zGIKrmoRoyOKaS1Fwqrgdn-92yLONqFjmvakWYW-g42XGPkDXiFYF7utHqklCpzDDKc79EvDkxlOjCeqOoTA4wUhEwHig4w4kodsOmbxwWJnwCAKlqOoQjuAmAW6eYOCRhSBNjNiN0jnVdLnT1Q00iIpurFbXj5zJxL4iKsYH75lDDFb_Z5O3usKGvs2ns43IgIzljIhR0m8qS1HGUkAooqlHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیر رولکس : ما نرفتیم مرحله بعدی ولی کلی دست آورد بدست آوردیم اینم عزتی بود که خدا به ما داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/alonews/131166" target="_blank">📅 23:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8Uy4WHoQso6dlFVOmquP3AsT7efBz83CAYLiWc4qnEjXfPiEPL_qp1H-iiSdLz3wM1F1eZn8_g2soHdlabNz5WZz1OFyGlvAxAB2kciCRSzXNeZ91KTkSPooC-SxBqxbLLPxkHaPzAlwq7JGNbdGTIXoGubuRRWIZMdn9KysouzvOvgRn5XLRwgk9SwnRzfw0f80jcsfTiHm887rIKrmDh0-xQutDe6agMsFHCoBoyFCg9yIMyHvLamBbLtLXr5mEjiUXnee62lcDlqB0MIiXCR5VXzYvIO8s_HbVWb3udt_7_mT6MCurnT5wwaU10yRaGmodiDeu-BCWRIE3bQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ApR3KCW6s1U5k9vXeN69MI8JJoNAA68RgrK8H--HOlRVoeAosvT_Y3I3yDvv-0mO8_a--tqml5qa-oBqJ7t9B-qiAAMM0XXJZkCjcCWXDBArOQ3zrpPevTTC-MdDtnDqIMFun03pvKxS_qttxh6uR_jt3eUIQcJSAdXhv0rppvGg0FAbAsdsaCBOrAtYrpBEAVbfXkOCbiE2L5pNi3CO0tz5ZZUwhqXBvRj4eHbnI7BXMQ3dfVNMA_0CRGGTWeQ1ZlBNI62tk77Tk13kySzBIV49pXpPwQ75coS8IaCyjWcwbA8sMYTD5Pbidx_VsjPYX4E9Ufs7-fFHO1YdZWXoEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fx6K8A70ZAve7YgjaX54hfQJAXPUSGGjpWFmb6gltw0wFhYee1PVX10e78O2QfuxBZ4T8OCjHUOP0Asz2MPlE_BxncYLFG9onYjmInL49RBIiuCaGCsZUxFjStuzn72Ui5hiTfvwAfYlnepwuoRlw4lId85ZPsFD_WiYtmB62PB8OdSPoMEKwpe-hfZ-a7K6gjVTiO68Y1-vI-ShzdkOb6LU1e7UxMzUk6CduXXmgqwBr_0M3_SUnPvTP3btTeqh-dW3G_hwKET4XUWXpO1wSRtdwt_uALkZH8nGsV_blhnn9esm4JhRFhgth-jogPLWSd7WOInIzHaoZuJ6DdcS-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMEBwwnCvB3s_8f1rEpD7PKykNuYfCmOGGYg8fDMM1ggRDo_Lmj5WdB75cI2AmhHmCW9St2f2Mk5dlh483N1ZUdeqa6q8719HFjSoiguNTQTg_xvWMp5FxeL3xO8jYY3Q-ecWy56U7sb9PvSoLlzEAdleaHP689RKmwpAlB16W22g-tUBmP2whYrqFMKwdMcnY5ZNpHmldzGH6UFhQQ57Wc0G7psGpS-s4UOVncjKg3BpWAXH14EPAz9fxMQFPW51EUoc3nMenfIiAc_hf2E6Z1ACxSW7v7J1bseTN4NG48L16MKJjMO3mmN-DhnUQkEtsdVDqecAvwwY6RtPr0XmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hz3v163jz-yeRiGnoh7sKgXN2GDK-OkhaHseWtqCTXXn4keZ7rl3G0bXl6sENJMg0OdTyMfz1JVWmdd3d9EmKKT3ZXtyCyhR2VMh5sjlbsKLAEfgFl2beMEBCZ8IUw0geRLkT8aPD6sLMP3NtJjKgKwAdmQfuw0INMuGnCFYmJQvcx8DWVEEiuvOrUrinZIyuHYVMuR8jEi9lHCEzLney-Baj310MOXlhvj9pZGe0Dq7U8yBAgk6DnrikMNra2LR9hSCENQujbtinj0oCRJDSjP7KI0lt27T7C3N3XkhSKMWfrbeMK3vLnVNIEzhvoiYLWS49crTdc6asPMVLrfdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckFvUQ5J8UdBz15QOOHacJg5XxwNDEoyL0m4tUP6004s7MCXZ6gHZ3zYBGqvWZYJxGnWlzg3sROjB_HnWpwTypp66tfyzkTPhQbYIAGgWhS9Yy4Zyh9WcZwsm4Zn2-NkBpHGO_sg3eqZW34ldor89Q5A0bTgJ6-dz1FaIEDpF3hDJ32dhhYSFb7zf-afkX3WMYZHb1-4OiMCUXMVKHeVWK8GIMiM6RyWV71vwESO7hfSdptB7fN0d4zkHpTR239XjSxcCDsa_-6RA0OYLMzUsd_TbLT-i8hLUw0vDJpylW4nI3hYCn9S_K52k48dMvFzuqyJQcR_QzBYadPKew7roQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKhyjqFsHW5efpKb9WcUFAk3FfhAmXZpETBtAHeipnLrovciJ2q9ieajP01DxmmEiC9RuBnekbS472xO3Jw30FFuSnjsk4efr2zB9sjp-T7pzd4oW6J8UzqKyHKM2fkOKQnabTeW2nnRaPDSLM6qNs8VQoAPu9HZQy_dg7o0GZKQUxwNhiZ6yBndEwOwjx6dIAEEXxnYtVbSwGzJ7_QTriDfNQuZJpXEC6cR96pShOMuiytgYo290yJ249AGRF3LgpaQnMPQVdRpW9OfLUqI14Uak_TW7qZvu_Lky7JHclwPt1h7VvLHORmGfbO39uJHgNaqtM1r9K2BMfucfVUeTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2621eaae.mp4?token=RgX5a6J2j70EHT2VkE9r4OAlCRX30zkVxcgVngU8GOu_tgf6hwHwuilCV9m1vY2V_aP6DgIIoSIcHej0QsrWgudMAK58yx1Suo-UTMFDt6_hPNyRCbRr1Bcn9DG6I8wepoty0Bsk9zK6zNEVwHANJwzcdAGuNmXyOMrYza2INui24I3wFYDy23GtLAtV1jvYuVC-OfAiaihXcDtLE9YCx6lc3pterXqYcGsSZDyrc5Hzfky2uGF6X97XuH3zkqCV8bW2iyTkPjesbAgQuZkkUz4P60rJ-Kj3VsnuL40cqYP85qig2ss4HXIiCFpUrho7MAkZkK7hqb1rHAFILmfmf682T_VFjJ_1hNIF6CgeHvq4anhrsE-YNLDXCezLX5Qfuq4yCy6axe4GoMNsn6lkwl4aNzwfslwAAB-mY0yB5GqbavPvIovtwX-OGLyJ2ZVZEDFm4lmd-rEV1TWzjB3wXdy-9BGNWIguWrML9jm1zdowwYmRvPpqCqjemUckVNTaXPkLq5Uqfngdnt_cRrLDAA0kv0Zl3CZIFNAUpI9WjnW6UFpl314JL36loEqGK9rLlBpKA35XrTWpghjoo6N-7zLHHhC7qp6fJvVND_u1uzd905PrBOMYAxuyDO7nwmr7055gzkA4xzCoafObTlzm-RDqDzW_0kZfdybfS6GWupI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2621eaae.mp4?token=RgX5a6J2j70EHT2VkE9r4OAlCRX30zkVxcgVngU8GOu_tgf6hwHwuilCV9m1vY2V_aP6DgIIoSIcHej0QsrWgudMAK58yx1Suo-UTMFDt6_hPNyRCbRr1Bcn9DG6I8wepoty0Bsk9zK6zNEVwHANJwzcdAGuNmXyOMrYza2INui24I3wFYDy23GtLAtV1jvYuVC-OfAiaihXcDtLE9YCx6lc3pterXqYcGsSZDyrc5Hzfky2uGF6X97XuH3zkqCV8bW2iyTkPjesbAgQuZkkUz4P60rJ-Kj3VsnuL40cqYP85qig2ss4HXIiCFpUrho7MAkZkK7hqb1rHAFILmfmf682T_VFjJ_1hNIF6CgeHvq4anhrsE-YNLDXCezLX5Qfuq4yCy6axe4GoMNsn6lkwl4aNzwfslwAAB-mY0yB5GqbavPvIovtwX-OGLyJ2ZVZEDFm4lmd-rEV1TWzjB3wXdy-9BGNWIguWrML9jm1zdowwYmRvPpqCqjemUckVNTaXPkLq5Uqfngdnt_cRrLDAA0kv0Zl3CZIFNAUpI9WjnW6UFpl314JL36loEqGK9rLlBpKA35XrTWpghjoo6N-7zLHHhC7qp6fJvVND_u1uzd905PrBOMYAxuyDO7nwmr7055gzkA4xzCoafObTlzm-RDqDzW_0kZfdybfS6GWupI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل اعلام کرد که سامانه دفاع هوایی گنبد آهنین پس از یک سری آزمایش‌های گسترده که با همکاری سامانه‌های دفاعی پیشرفته رافائل انجام شده و شامل درس‌های عملیاتی از جنگ و عملیات اخیر علیه ایران است، ارتقا یافته است
🔴
این سامانه ارتقا یافته در برابر تهدیدات پیشرفته از جمله راکت‌ها، موشک‌های کروز و پهپادها آزمایش شد، این آزمایش‌ها همچنین شامل سناریوهای عملیاتی مشترک با سامانه رهگیری لیزری پرتو آهنین بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/alonews/131158" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پولای بلوکه شده مال دولت سیزدهم(رئیسی) بوده است، مصاحبه اش در صداوسیما قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/131157" target="_blank">📅 23:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
گفتگوی قالیباف نصف و نیمه در شبکه خبر قطع شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/131156" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131155">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=GDrMoQINpV3Wf0PdFkQK5z8qbEUV9ZVUzYjbDH39cbcV9bLq8k2PotLJJECNrRcjzR4Tlqg5kdSzLVM6XTRO1LSd3W-AW6Ky8NE4D4y0gogmzv8VzhBfKDW29n6L5f3UYGNxoB4rl7nr37vdAP8rR4GnOZwGjhbxK4I_36kZ27MFYA7fWUXN7QNa_mCCSUM_PRBbcOz-ZiTpS4vfj4L29WScQcGK-h-KIj161aE6vXoRjpizgXwG46mL2B0hUEdvQPuHvpssv7Qeps3NdayJKqu6rda7kTPs-ky0cFO7B2DCPmcfNn4ekj6jkILvA133NsVyoi9ENRmUmXyYgi_kHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=GDrMoQINpV3Wf0PdFkQK5z8qbEUV9ZVUzYjbDH39cbcV9bLq8k2PotLJJECNrRcjzR4Tlqg5kdSzLVM6XTRO1LSd3W-AW6Ky8NE4D4y0gogmzv8VzhBfKDW29n6L5f3UYGNxoB4rl7nr37vdAP8rR4GnOZwGjhbxK4I_36kZ27MFYA7fWUXN7QNa_mCCSUM_PRBbcOz-ZiTpS4vfj4L29WScQcGK-h-KIj161aE6vXoRjpizgXwG46mL2B0hUEdvQPuHvpssv7Qeps3NdayJKqu6rda7kTPs-ky0cFO7B2DCPmcfNn4ekj6jkILvA133NsVyoi9ENRmUmXyYgi_kHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: رئیس‌جمهور آمریکا گفته پول‌های بلوکه‌شده صرفاً برای خرید غلات آمریکایی آزاد می‌شود. این چقدر صحت دارد؟
🔴
قالیباف: واقعاً هیچ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/131155" target="_blank">📅 23:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131154">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b26e4e44f.mp4?token=AQB8JB4gVJwfIL60i33nDIZi5Y5szw6Ag3_yS1UCQlcn-_5b_cPJdAVMOuOtrsiSUmOZTHQTYTQCPBD9q0inT9LlE2ID3EKnGVQLETB-4XoAl46gF-uE_dWfpgDchUk5ZnvfP5VPjWEmkQ0nTi9aarEDiwfuJEhjxhfb40wvcPe1zRVQMSR1L9zXjkYE_IqN27UivUF3QhacoN3_Nk6c205v-Kd6DwolX-UGLleR_9XrJLPvm0KM2pzP5BDYZKezE5J2omp2TnXnERdDwldy26_OhVxlINws3T-Wh0Cc-2WaVeve5SSCDLs8KLfR0CLOtiTcg64Xh1Ri3sbeWDR9zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b26e4e44f.mp4?token=AQB8JB4gVJwfIL60i33nDIZi5Y5szw6Ag3_yS1UCQlcn-_5b_cPJdAVMOuOtrsiSUmOZTHQTYTQCPBD9q0inT9LlE2ID3EKnGVQLETB-4XoAl46gF-uE_dWfpgDchUk5ZnvfP5VPjWEmkQ0nTi9aarEDiwfuJEhjxhfb40wvcPe1zRVQMSR1L9zXjkYE_IqN27UivUF3QhacoN3_Nk6c205v-Kd6DwolX-UGLleR_9XrJLPvm0KM2pzP5BDYZKezE5J2omp2TnXnERdDwldy26_OhVxlINws3T-Wh0Cc-2WaVeve5SSCDLs8KLfR0CLOtiTcg64Xh1Ri3sbeWDR9zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/131154" target="_blank">📅 23:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131153">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گفتگوی قالیباف نصف و نیمه در شبکه خبر قطع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/131153" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131152">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f975bb897.mp4?token=d4PMU43_6ajd9d4sK4fHXC6SQKYu4zzWqJNkdZfsdM-BryXlht2A9uYMZKcJJmOKEAXVNdO6HLZrrxgWLIm9uvU0NAnBqBhcPZ9n9xR_RLvGGetN4oqB0q091ZjwDbq0xbz0lCqLKq_4xdipsyJ0HXLeMFfgGqEmBMJQr_29K1bGvmr4pModUazeXIucush6z3oF6xcDWx7EIMCPHKfNpmB0xuRLS2AlyqtH6cL8N6vn8HIqkVuhvx4okRVJfVF_lqfwG1h4BpzhmT7aeVP82ZAMl3NmaHc29678-MFDClotHbdCsqJNXF2hmLHT-23bfTzuLptl6Xxv1Ao4_16lSToNhlw7krLlfoYefw2FO2LQOYHzjm67XJO-ODADzhKnxFZNbzK9c_3VV4ullpb1kHtGyj4-FUHaoGko3V01gRSQKbNEA-eXKBf1-C2vDvG34sAK-Pdb4q8b2xS20OiJDQDJMoqDrKJa2yb0k0IOMLFfhqinGveN54GAbyIw0RfrIhqummV822bPpU0i9PHOAcshjzsOmYqGSHtnEHZNsVNKoTKeueBOtDXGvg7iKlFKvBCPawAzmxDQykRQzLKtzzhP4FbcvsHRXWOB5A2p9mTxcGjFZJ34ekofXzZDAnWcw67xC-YLRMzZr-9z8_IXfHccR0BXbCk4d1l7G0nuOtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f975bb897.mp4?token=d4PMU43_6ajd9d4sK4fHXC6SQKYu4zzWqJNkdZfsdM-BryXlht2A9uYMZKcJJmOKEAXVNdO6HLZrrxgWLIm9uvU0NAnBqBhcPZ9n9xR_RLvGGetN4oqB0q091ZjwDbq0xbz0lCqLKq_4xdipsyJ0HXLeMFfgGqEmBMJQr_29K1bGvmr4pModUazeXIucush6z3oF6xcDWx7EIMCPHKfNpmB0xuRLS2AlyqtH6cL8N6vn8HIqkVuhvx4okRVJfVF_lqfwG1h4BpzhmT7aeVP82ZAMl3NmaHc29678-MFDClotHbdCsqJNXF2hmLHT-23bfTzuLptl6Xxv1Ao4_16lSToNhlw7krLlfoYefw2FO2LQOYHzjm67XJO-ODADzhKnxFZNbzK9c_3VV4ullpb1kHtGyj4-FUHaoGko3V01gRSQKbNEA-eXKBf1-C2vDvG34sAK-Pdb4q8b2xS20OiJDQDJMoqDrKJa2yb0k0IOMLFfhqinGveN54GAbyIw0RfrIhqummV822bPpU0i9PHOAcshjzsOmYqGSHtnEHZNsVNKoTKeueBOtDXGvg7iKlFKvBCPawAzmxDQykRQzLKtzzhP4FbcvsHRXWOB5A2p9mTxcGjFZJ34ekofXzZDAnWcw67xC-YLRMzZr-9z8_IXfHccR0BXbCk4d1l7G0nuOtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس درباره مذاکره کنندگان جمهوری اسلامی ایران: یکی از چیزهایی که درباره ایرانیان هم شگفت‌انگیز و هم کلافه‌کننده می‌یابم این است که می‌گویند «نه، نه، مذاکرات صلح در جریان نیست»، در حالی که مذاکرات فنی بین ایالات متحده و ایران درباره توافق صلح در جریان است. این یک تاکتیک مذاکره‌ای ایرانی و یک ابزار بلاغی ایرانی است که من آن را درک نمی‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/131152" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131151">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd90a566a.mp4?token=Czm4sQw_mjeKOhPuydPy0YYqa62SeArFIZNIJOuaz6JR8kpCMl5jov6KcsWsKjc091MJPM25xt7b6sQ6vrXYoxAYbrHoAGb1nd2fU0YRG80u_Jz2vf06fbfB06vWUkXoecJ0gwdifFGXIT9b2GLLR8zhyY3A5ZzZBueBaBQ2VeMdqNqVb5uouRkx8OcuoDsgUltU7ySIx5lp9rqvlYYLH1SgacNhYMmCI7BPG3Uqeq2TZYjso3VtWDHkV_JSUfivmFgkg2A4OqD9AlfoWcg-ga3ujTQTH8OK9woqENSP-M8qZDhY6TkYCshDO7EPbTGkBMWeeflF9aWbOTWqKhbQ0H5tzVmS0kGwVsdMixdfobl-vv_JF_i6m4Wlvglulh_jRZs6ZhfqoIEbfViAJKkTLhzvOs-DS6iK9LZVA99_P6RmA-ZAzBFRZyqULgLhJhST1YIqrZs48Cnh5hvHn2YnYCvtGlCvGXxKzddo7SgOO5zGB6wkbAiK3SN_VBZAuU9MKt5pRpu9Zklg04mX9F-5oAigA28B66PGJ1XMSzYarib9MWZ4gsFH02MSV-Syg1sslI3rKEyUH1rpj5c_7MESDWfPf4w8ciEK1PpsDmRPDpNUfoFYi-q3Vp0gmLS6qoaFPC3kr2c6KGl8fkT1Q6uyz6j2f9Jv_FRVClQu7DQ8cNY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd90a566a.mp4?token=Czm4sQw_mjeKOhPuydPy0YYqa62SeArFIZNIJOuaz6JR8kpCMl5jov6KcsWsKjc091MJPM25xt7b6sQ6vrXYoxAYbrHoAGb1nd2fU0YRG80u_Jz2vf06fbfB06vWUkXoecJ0gwdifFGXIT9b2GLLR8zhyY3A5ZzZBueBaBQ2VeMdqNqVb5uouRkx8OcuoDsgUltU7ySIx5lp9rqvlYYLH1SgacNhYMmCI7BPG3Uqeq2TZYjso3VtWDHkV_JSUfivmFgkg2A4OqD9AlfoWcg-ga3ujTQTH8OK9woqENSP-M8qZDhY6TkYCshDO7EPbTGkBMWeeflF9aWbOTWqKhbQ0H5tzVmS0kGwVsdMixdfobl-vv_JF_i6m4Wlvglulh_jRZs6ZhfqoIEbfViAJKkTLhzvOs-DS6iK9LZVA99_P6RmA-ZAzBFRZyqULgLhJhST1YIqrZs48Cnh5hvHn2YnYCvtGlCvGXxKzddo7SgOO5zGB6wkbAiK3SN_VBZAuU9MKt5pRpu9Zklg04mX9F-5oAigA28B66PGJ1XMSzYarib9MWZ4gsFH02MSV-Syg1sslI3rKEyUH1rpj5c_7MESDWfPf4w8ciEK1PpsDmRPDpNUfoFYi-q3Vp0gmLS6qoaFPC3kr2c6KGl8fkT1Q6uyz6j2f9Jv_FRVClQu7DQ8cNY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس در مورد جمهوری اسلامی ایران: ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/131151" target="_blank">📅 23:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d179f44d.mp4?token=KX85XL4P-J1MmMoIkaH9xgW84B9dxGa2r-7epkCTLo5MameG2GMj-_HIVUEKmYLlCnUfeODbgpILaHiXiCpQtmQwJBZgNTnGW0s7Gi_Mr57R0Pvy9aRixek5VyQmZPnbL5l1nvDZC-peWcPhC50uTMU_qAa0MEkVJ54szg0PiekhrIOCxtP309RaYflPMoqiAEfPo1qvwCtz8508m5wNfEZHdLXbZ2OCnyLLyw7OBCMraCeppWx9tbhIDb8jM9ZiS2f_ZGZ1F32s0fNWxw1wrPnP_K43fJ4ip59dqMbCHzIe1bYPWF8PHSk4HVk5ggVXrd8-LPN_mI4eeZKTQACYqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d179f44d.mp4?token=KX85XL4P-J1MmMoIkaH9xgW84B9dxGa2r-7epkCTLo5MameG2GMj-_HIVUEKmYLlCnUfeODbgpILaHiXiCpQtmQwJBZgNTnGW0s7Gi_Mr57R0Pvy9aRixek5VyQmZPnbL5l1nvDZC-peWcPhC50uTMU_qAa0MEkVJ54szg0PiekhrIOCxtP309RaYflPMoqiAEfPo1qvwCtz8508m5wNfEZHdLXbZ2OCnyLLyw7OBCMraCeppWx9tbhIDb8jM9ZiS2f_ZGZ1F32s0fNWxw1wrPnP_K43fJ4ip59dqMbCHzIe1bYPWF8PHSk4HVk5ggVXrd8-LPN_mI4eeZKTQACYqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات جنجالی منان رئیسی، نماینده مجلس در صداوسیما درباره بندهای تفاهم‌نامه
🔴
برخی از بند های تفاهم‌نامه آنقدر ضعیف امضا شده که اصلا نیاز به نقض نداره و خودبه‌خود ایده‌آل آمریکا است/ در سند امضا شده که آمریکا باید مشخص کند پول های آزاد شده را کجا باید خرج کنیم/ آمریکا غلط کرده به ایران بگه پولشو کجا خرج کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/131149" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
قالیباف: تنگه هرمز بزرگترين ابزار قدرت ماست، باید از این نعمت الهی به درستی پاسداری کنیم.
🔴
باید روز به روز رونق تنگه هرمز را بیشتر کنیم
، محدودیت را باید برای آمریکا و اسرائیل بگذاریم اما تردد باید بیشتر شود.
🔴
باید به دنیا نشان دهیم امنیت اینجا روز به روز بیشتر می‌شود و حتی هزینه بیمه کشتی‌ها کاهش یابد.
🔴
برخی می‌گفتند رفع تحریم وعده سرخرمن است، رفع تحریم‌ها انجام شده و نفت ایران ۲۰ درصد گران‌تر فروخته می‌شود و پول آن به حساب واریز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131148" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/131147" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/131146" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قالیباف: به خاطر مشکلات سیاسی با من قالیباف حقوق ملت را از بین نبرید
🔴
کسانی که حرف ترامپ فاسق را قبول می‌کنند یک‌بار حرف برادر دینی خود را هم بشنوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/131145" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
قالیباف: حاکمیت تنگه هرمز با ایران و عمان است و تردد در تنگه با ترتیباتی است که ایران مشخص می‌کند البته ما با کشورهای ساحلی خلیج فارس تبادل نظر می‌کنیم.
🔴
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید و این آب‌های سرزمینی ما است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/alonews/131144" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131143">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قالیباف: در متن تفاهم آمده است که عبور از تنگه بدون هزینه فقط برای ۶۰ روز است، این موضوع به دلیل اصرار کشورهای منطقه و کشورهای ساحلی خلیج فارس بود و عمدتا برای کشتی‌هایی است که با آغاز جنگ به دلیل بسته شدن تنگه در آن منطقه بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/131143" target="_blank">📅 22:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131142">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قالیباف : اگر از اجرای آنچه مورد بحث قرار گرفته است خودداری کنند، ما نیز برای جنگ آماده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/131142" target="_blank">📅 22:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131141">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قالیباف: غنی سازی حق ماست، خط قرمز ما در این حوزه مشخصه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/131141" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131140">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قالیباف: بعضا می‌خواهند مدیریت و ترتیبات ایرانی در تنگه هرمز را رعایت نکنند و طبیعتا ایران عکس‌العمل نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/131140" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131139">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قالیباف: از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/131139" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
قالیباف: در آمریکا روبیو موضوعات را یک‌جور دنبال می‌کند و ونس هم جور دیگر دنبال می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/131138" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131137">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔴
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها  در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/131137" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131136">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
قالیباف: الان هیچ مذاکره ای نداریم. سفر به سوئیس هم برای گفت و گو درباره اجرای بندهای ۵ گانه بود. در گفت و گوها ما نتایج مذاکرات قبلی را پیگیری می کنیم تا محقق شود.
🔴
پس از امضای یادداشت تفاهم اسرائیل تهاجم سنگینی به لبنان داشت و به دنبال اشغال برخی نقاط مهم بود تا تفاهم با مشکل مواجه شود.
🔴
این اتفاقات باعث شد به سوئیس برویم و در آنجا موضوع اصلی که پیگیری کردیم آتش بس لبنان بود. بعد از این پیگیری ها، حجم حملات به لبنان قابل مقایسه با قبل از آن نیست.
🔴
یک کمیته مشترک بین ایران، آمریکا و لبنان ایجاد می شود تا حاکمیت ملی لبنان را محقق کند، سفیر کشورمان نیز نماینده ما در این کمیته است.
🔴
این که تلویزیون تحولات لبنان را برجسته می کند خوب است اما گاهی به این موضوع هم اشاره کند که شرایط لبنان چطور بود و الان چطور شده است
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد. کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/131136" target="_blank">📅 22:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131135">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
قالیباف: آمریکا در یادداشت تفاهم متضمن شده که در لبنان جنگ پایان یابد و لبنان بر سرزمینش حاکمیت داشته باشد و ما دنبال اجرای قطعی این موضوع هستیم.
🔴
نسبت به اجرای تفاهم‌نامه مصریم
🔴
ما هم درحال گفت‌وگو هستیم و هم اگر تفاهم را اجرا نکنند آماده جنگ هستیم و عکس‌العمل نشان می‌دهیم.
🔴
ما در سرزمین خود کمتر درگیر آن هستیم. تنش‌های ما گاهی، همان‌طور که دیده‌اید، شب‌ها اتفاقاتی رخ می‌دهد
🔴
گاهی می‌خواهند عبور و مرور در تنگه هرمز را با ترتیبات ایران نپذیرند و اقداماتی خارج از توافق انجام دهند.
🔴
طبیعتاً جمهوری اسلامی متعهد است که عبور و مرور در تنگه هرمز حتماً در راستای آن تفاهم‌نامه انجام شود.
🔴
اتفاقاتی که این شب‌ها در خلیج فارس رخ می‌دهد را نقض تفاهم پایان جنگ می‌دانیم و حتماً به آن عکس‌العمل نشان می‌دهیم. در آخرین نقض آتش‌بس، مقرهای آمریکا در بحرین و کویت هدف قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/131135" target="_blank">📅 22:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131134">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
قالیباف: محاصره دریایی خودش جنگی غیرقابل وصف بود که با تفاهم برداشته شد./ما داریم دوران گفت‌وگو را دنبال می‌کنیم برای تحقق ماده ۱۳ یادداشت تفاهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131134" target="_blank">📅 22:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaxnJAB2AyJk4YIqf4ARI3Z9etV2Ab-woro2vBarVcvYe_yRpjfVldqjvFm5XSVQPiN8t6fQe5fFIPfc8GKkkiURjwMPQcxnTGogbZw0mWLAYCshNuGqhqEgui0wnlChioNb0_qLWbOJ-HRFk2LKnUZdlg2tkdyr5fnx9LNR6K9vBSXMGw_ksWKrBl0sIFNd49LbssMdHJCGIkFZjKEmMxklzwE-6TjdUH63g0L1mCRaxJvf5YDO-_g4bfCfriBbUphmI7WlotnUQZfopHpSjGwAPm0utVzQo9-7n49DFKqv7R0S-Wcaa2T2AgeQkO-cgRa-YHH4U39332t8_IxzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ عراقچی به سخنان وزیر امنیت داخلی آمریکا: به جهانیان ثابت کردید که شایستگی میزبانی یک تورنمنت بین‌المللی را ندارید!
🔴
مارک‌وین مولین، وزیر امنیت داخلی آمریکا، در واکنش به حذف تیم ملی ایران از جام جهانی ۲۰۲۶ مدعی شد که پس از قطعی شدن این نتیجه «از خوشحالی رقصیده است».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/131133" target="_blank">📅 21:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131132">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ارزیابی ارتش اسرائیل این است که حماس از نظر انسانی و لجستیکی برای نبرد بعدی در نوار غزه آماده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/131132" target="_blank">📅 21:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131131">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
دولت ونزوئلا : تعداد کشته‌‌های زلزله به "۱٬۹۴۳" نفر رسیده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/131131" target="_blank">📅 21:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131130">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ9CvICBO13ea9AQsw_CKCRofPGEf-mkis_BhSr3EUvlIo5V5YFv2T33WB3oRIg7tVvqedWzthbjxN7D7pkUTn0aYF_Ot7te_N3Vuk-nedYak9fHkAY2f1sT4v86cstX25oxkHU8GU9UbfQomFRQnXaW-em9ViFa0QLckbSrkWcY4roXx8I8ujyebAvU6THsdPI_X-FnvRgu8BQDJy3537Z_xocDd4JG-Br4DrvlgaDjCRq9BZ7a8uvmerC-c6JkoWe_EUrJg_OLPC0h1XYy_lpggwc4o8HwHFaA3POe4D1EPN3BNFGzeTumKGf2NY4CAFh_1w2MeD6pmOqmgAvnpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه ترامپ  به چینی ها بعد از رای دیوان عالی کشور: من می‌خواهم رئیس‌جمهور شی و کشور بزرگ چین را به خاطر پیروزی بزرگ آن‌ها در تابعیت تولد تبریک بگویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131130" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131129">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
تانکر ترکرز: ایران از زمان رفع تحریم‌های آمریکا، ۵۰ میلیون بشکه نفت صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/131129" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131128">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
سی‌ان‌ان: با تعلیق موقت عملیات در تنگه هرمز، تا کنون حدود ۲۵۰۰ دریانورد از تنگه تخلیه شده‌اند و بیش از ۸۵۰۰ نفر همچنان در تنگه سرگردان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131128" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131127">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXIyJuFkqmMsQZ5NVt-N4hYHU8AdHvaFz7oIW4xC7aduBX65pP4bRo2WbyMWZeO0RAqj7HA0MNjIiOXv5pvlbFLtWPeGWFlQAJOFsEoqTVPJVZ7B3isr-YEj0-VcTupS_S-dkCzO_EPTWmlytpewTPXxptAaalJNdu2K_YYQPIQqLn5v2LSwl2TvSQdacPV3opKPFGapaffuJYETO_vVS-b4XDXmej77pm6tLLyeCy5iLiaE51hbi1FU8AX83Vn84mCfRGH2jH5uN-kScNHPXDlRSaX-3-NR2W_7HBuBG43eDsyeD3rxscQjzsxuHGrw7e6rNBwzfFoF0cHbdecn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌های 6 سال پیش یه رستوران شمال تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131127" target="_blank">📅 21:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131126">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
پرتاب موشک کروز Kh-59/69 از جنگنده-بمب‌افکن سوخو-34 به سمت اودسا، اوکراین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/131126" target="_blank">📅 21:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131125">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بلومبرگ: پاکستان پس از اختلال در صادرات قطر که این کشور را با کمبود فوری عرضه مواجه کرد، یک محموله اضطراری LNG خریداری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/131125" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131124">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
صدا و سیما: استعفای وزیر نفت تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/131124" target="_blank">📅 20:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131123">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: برای ازسرگیری تردد در هرمز منتظر اجازه ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/131123" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131122">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
در پی شکایت ایران‌ خودرو، تردد خودروهای پلاک منطقه آزاد انزلی در خارج از محدوده تعیین‌ شده، لغو شد
🔴
تفاهم‌نامه‌ای که به امضای ۵ استاندار رسیده بود، با یک شکایت و یک ابلاغیه، به تاریخ پیوست؛ حالا پلاک انزلی در جاده‌های همجوار، «خارج از محدوده» محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/131122" target="_blank">📅 20:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131121">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بر اساس اعلام رئیس کارگروه آرد و نان اتاق اصناف کلیه نانوایی‌های بربری و سنگک مناطق ۱ تا ۳ تهران آزادپز شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131121" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131120">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=YGW9KX6xyNKhEzFL0XXf1cX8p3Ho9Zp_ezaMtSZ7WINEUWdovrLYpmEaJVIwARcG5xVVm9LCJ-sIWP9Tt_fvjpXk8OqmG_Obt65JyvLP3NFNHAhIp1eliEu7V7Jeuvqj8dPxbcq3D1KRoIqyIsq8UVB4RvG1NPTYi24d900F_j-CiSptzkQF455CHt8XeVdnUHemw6lz9Foq5JS9rtDotwt7DoOXoo_WuJ_T1Y60ZA0ty1U30RRGlZGqZnbIw6Nn9W4sc2IUQGlyEF1TVsm2vzC-ei1aO0CjtLxiOInYD8dEl9A0srLNkGR65EgMv3aTJO8lV2RaBnyGXX3WeVbdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=YGW9KX6xyNKhEzFL0XXf1cX8p3Ho9Zp_ezaMtSZ7WINEUWdovrLYpmEaJVIwARcG5xVVm9LCJ-sIWP9Tt_fvjpXk8OqmG_Obt65JyvLP3NFNHAhIp1eliEu7V7Jeuvqj8dPxbcq3D1KRoIqyIsq8UVB4RvG1NPTYi24d900F_j-CiSptzkQF455CHt8XeVdnUHemw6lz9Foq5JS9rtDotwt7DoOXoo_WuJ_T1Y60ZA0ty1U30RRGlZGqZnbIw6Nn9W4sc2IUQGlyEF1TVsm2vzC-ei1aO0CjtLxiOInYD8dEl9A0srLNkGR65EgMv3aTJO8lV2RaBnyGXX3WeVbdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحات سازی روسیه در منطقه ولگوگراد اصابت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131120" target="_blank">📅 20:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131119">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/131119" target="_blank">📅 20:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131118">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQ0uhMG0Tva3Ddkky9aKtPWo7p7TpX9HvUr1jq-NlW7MHzFU_9SPraS9V_nQarFmIyJHZU7tyeqDAThGxsNoBtuvwBepDm4yXPHBxrBo66BKykhSbfk6-InVzO6jmagohXCaC_9qgpUOgzcF1MieXYP01i0DMrJ_RZYGIOmBkQ1DtwytNOg7YnetmxLPWxuAE4dhoY3Hiq0zFQwN3sXKLsdcU8dwcNfUJqpDPxOm4F0j3WMCpoz9qU0LtKXNtDfIuJKKMrJHWaVoMlu6DdhxPtlRseafBxP26kAMUJpZci7dzOmqgmmC3ujTuwUrIk7AC8jpZ0kvjNT67EHghY1e_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: دیوان عالی کشور حق تابعیت از طریق تولد را تأیید کرد که برای کشور ما بسیار بد است، اما ما می‌توانیم به راحتی آن را از طریق قانون‌گذاری در کنگره جبران کنیم، با حمایت رئیس‌جمهور که اکنون در این فرآیند تعیین شده است.
🔴
هیچ اصلاحیه طولانی و غیرقابل مدیریت در قانون اساسی لازم نیست! کنگره باید از امروز شروع به کار کند برای پایان دادن به حق تابعیت از طریق تولد که پرهزینه و ناعادلانه برای کشور ما است.
🔴
آن‌ها حمایت کامل و مطلق من را خواهند داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131118" target="_blank">📅 20:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131117">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔴
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔴
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است.
🔴
‌ سخنگوی وزارت خارجه: تاکید داریم که توقف جنگ باید محقق شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131117" target="_blank">📅 20:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131116">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131116" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131115">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtqw0jLcmRd3PF47eYbim4PAYhDhPdYKnx_kOTC1rKIROturMDwwPVOL6faqq9Uc2gG29Q37wBj8TIILwLgWRfvBy1KNoB1c4aWhT9fCmQTnoKYRjNzcn28j6qqu3sUu84RxcseM7S973G4_4eA5_m6NDNNZpQkWttRWBC7lDCdtU-t_CwRmtuyoV1prqC26Xr5GqXXWFdMo0QOOosQWagIVDbvR3FYEdsm-DXnRKAVWmP8HdsZvrQY3qvAG7cYjQGGH8y1j6Cds3DtQz8hVYnFq909GD7cWT8BW7dkEYw4gntEHuOAJoqTpWaUhYzkQ7aQtJimGGl4XB0n65YoIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131115" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131113">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egsfGvL4grXNUxHSq9XAvmTjff-27MgtysKmrTwGlHYEhK5oIps9yACjIObr6ZONR_uBMIm3oE30iDj-Y5g7iSeY1PikC6528tp3BQoWt9lDbmXjbWEu4Vwn3PqLUKUTLjN8hSvTpYbhRKncYCzJdsnfE-xK2_oMYxN00QPFt0Ri73BxUfiAkWCDQSemy5QfLmF8VQRU7LopV-XgWYzS03M9cHQdhGoPw_yF7fjm-sV-Q16kd1XejO48lW5J1h5_i6M6ct7BKzEROwXdl0AljuY56nUHtEsn2qDZPtFQaOTC758tY8viPNgDItOgwYoCikiDzcgberDYQiBQpwdIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR_7Hii8lRzGp6fs_yZ2aNajOOXWeunB-gcB2nerznr_WgX07CY2BATFJpfV7SHVC-nM1UFBUaSGppFhPZIA7r8TE9Kcz8vONqEIesYIbwecfa2ZXd2y56GIMROjhv6gEnSJADYvhGnmzdlHVEEL_IosctffBVyNghv2y68FspP6FyE6y1Ex0sk5ni3y7GAEckBC8vLASpNIECzOxXOoSEn1DpjGwhoDNeu_20czCbDO_Vy_dR5lFXOx98MR-3Gbs8ct9PMvdw8Hq1PsDmnDHvnERgaqwV1Yld2s7XMY_f-1n3tIDexQD_mjQngsAcXs3PGt1pnSdTGfXvxPEboMrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان امروز پیش از ظهر در مجتمع ریاست جمهوری در آنکارا با رئیس سیاست خارجی اتحادیه اروپا کایا کالاس و هیئت همراهش دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/131113" target="_blank">📅 19:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131112">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بر اساس مصوبه شورای‌عالی بورس و اوراق بهادار و در اجرای تصمیم هیئت دولت درباره تعطیلات سه‌روزه ابتدای هفته آینده، بازار سرمایه ایران در روزهای ۱۳، ۱۴ و ۱۵ تیرماه فعالیتی نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/131112" target="_blank">📅 19:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131111">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رئیس پارلمان عراق: پارلمان، دولت و وزارت خارجه عراق با هرگونه حمله از اراضی عراق به کشورهای همجوار مخالفت کرده‌اند.
🔴
عراق منافع مشترکی با آمریکا و ایران دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/131111" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131110">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdKCY5EgPZqHZ0P1jjzr_izVZ4BUou2zmwmSKZUhh5Fn1iP_U09fcv9580Ivj-ipx7RkZdsU_5S_Tx7pcOM8dhBSz683gMbR2ieWi-I1wjTzjcBjLGdthOsUD592yaU40UDfgicKfSc2JrxquhqchpkSKAKnUSQ7UoS45uR14NCWsh2gQ5aGQKo4TgXbku3Hy0aruVHEPMbLQUlqx_5gMVTXbQ9c4o_Xh2vyBZtETJp0CpMHlv_S-qwm35HVZZ6xXcEc7bnq0TCX2QAd9Y11xaaOzxGhFvSzvvf0HVGid-yCLsUMudnnqmX7dZfRuzABptE0QE1xDTzNSshNbyncPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، جرد کوشنر و استیو ویتکاف در چارچوب مذاکرات جاری میان ایران و آمریکا وارد دوحه شده‌اند. با این حال، قرار است دیدارها به‌صورت غیرمستقیم برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/alonews/131110" target="_blank">📅 19:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131109">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=CZ20-7JzBepBTJOxCQQ65uBLoWFrFS8u8VPlmsmekgCjN80zApMm1cNi0hb_qqD3evmhODqJTb1lywH-dimIKl1PbBEF-9PDijG7cc32I6fLRmnjzeMS2FYyKK9zrwIkaIw8FTL4brKrxXAh1IkJnk_3Yi1I6p_X72MMSVui2foJyvXaAqsFJRHtdeRHJ02k-J7GO4uK5zQ8AV2ebGNy8i9auA91tdmKM5InNgrm2RSWfOz35eYmHJqA59g6lsxUkEYwkKUufy_AWkqVbsGOMkUVH40fo1rvp7zOSIAyFLJua-sSMjQGG5qjzpF_-ZU4f2tdqM42EhJzYwP3IkNtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=CZ20-7JzBepBTJOxCQQ65uBLoWFrFS8u8VPlmsmekgCjN80zApMm1cNi0hb_qqD3evmhODqJTb1lywH-dimIKl1PbBEF-9PDijG7cc32I6fLRmnjzeMS2FYyKK9zrwIkaIw8FTL4brKrxXAh1IkJnk_3Yi1I6p_X72MMSVui2foJyvXaAqsFJRHtdeRHJ02k-J7GO4uK5zQ8AV2ebGNy8i9auA91tdmKM5InNgrm2RSWfOz35eYmHJqA59g6lsxUkEYwkKUufy_AWkqVbsGOMkUVH40fo1rvp7zOSIAyFLJua-sSMjQGG5qjzpF_-ZU4f2tdqM42EhJzYwP3IkNtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/alonews/131109" target="_blank">📅 19:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhfnwumjoWkckZCNrXtDxik893lz2opYjPuCfBIS-RGZFu1erW3TjlEmoBuruX0btTTeiNfa0iBnTGvm0gVIaUhO_iUZS4cN7C80uhxuNR0Px1KDXu-oPrbHUlVwH518COqzMXSMOFoZp-Kj6J5AGA1FGap77e1xRRhZevnePTDG6nC-RUYQEGPobvqZya3Kbi4hIYYkkY4tY2_UB0fdylQoMq5L9GUFtII1N99NylmaeMMbHYSqblhHszu3BqopaF445bztDjeSs86yQBv1UQgWPglUQGV5dCJ17ViDnmW6ZuUSmWZENidw3DJAxL_2We_NDStZyNrcvRv5cGFtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UEtCpFIu5ID1m2sENckPEnnh4rqQzxjU84H9_28QEMcrY3EQiyrNt_yyto9gUA268vgc-baXVfTlT330OwhsL0HZvZIur5bY8d4VVbTY08NXyB3GaxAme1t8vZPmUD4XfjJwSq0l8unwIJ_v29M7ZfGZFSPaGnG87FZoxPZ6I3L7A6BsYFFGWUtWfYbTaWaQg1gKoEfzaDsiOEEe_EBTBVZGvqWoH5kjeH5GSEUc7CJTaTGicMNM8eadD2crfjwgQ3lAHQCaXCSv5CTeKYsIKZLu63sVpBmRbHk95m8dCXM3Z2etMdz8eF7QXIAiScVenjxbe8IGaN3hzXprw6tbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEcfFh2PP_ygbrCESG_DhAUTSy3Y7LAB_C5wPR11WKTsbxADKYR7Q77fl7F7WH2cBH0K3uOekpH511r1-uqpjQJCFuC6BGEj-Cru8A4DREbdoFIAcQILWFFYrsMYnyUQ-2sj3T638nJrVGkJXvuxCozZ7XfyIrunh-kkVkoGZA1nU7JgY1bEj4mRadPiy_mkL9hK8LZpxH9aMeXF1KkXoOe03hFIS5M1mKxftdZuLQ2MZFYnA1mRwz2Nr4scg1t_khvBihA4g5J8w069XEaiQjoPchbLEz_jft9LK-UIawXMsknuXjiuVyAaf2E0cD6796xe--VC48CXcb9YY2bEZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنتکام عکس‌هایی از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/131106" target="_blank">📅 19:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131103">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kI6iZb-nUiWUK_qVHOHvmhQQtQlLjb5ZuUhvMVTa3NQL2BlnJpG_PadCB49hLDTeUmPOIhflNvEGf5FDMbZ6us3y3e0LmB-zA3RYLIugf7OS7qY5C9c_iviWN8AmQOTXNZRkP2SV3ckTU9Ckm-b6xqBXKpAVXTTRvvpfr3lx9agByWLAUXlrJW-yOmn3LDrwzuqi-q6-P52I3eB9WcHoCNMpIvmoxoyW-X88zDFEMDyejQJ4wX7zCZ_DOA68atrBCXXqjGBnJmVsu5NpJMAlx6mOK0OCp2vf6nCrBT7TNMH3wotKByjlxLvpXbVcF5lUGXjasxDmbuKa-5kqfmpA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vRU_xTyM-sGaeW-_p28EEPrz3myIdypxbvpU5kStTx2W-i-rfMt9URJ9zmk_AOxuEylk2t4CglHyitS71MruMVD68HLXPyun6FSfS3miK7jB--H_a6EUwQKpprXhlBh9GTPY-kJzvj6ueeyzoZYEF1hbbYb8rZKLrtK7relasXaJlAg6HXdbrH0JyIGWNnATP6VZZi5NRvqxIqbmQH5mBnXAhf1WTaItCMNo9_Hdp6qLKILLZGAWuRjD_LHIFDK1JFDnyFZe40ll9nO4OpISJQTsDtBTnDVYLSgf1wb84XkmcXwF_6bNTKTxbgkEbJEQzC2GE3tKIscgYHUSAOwxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnG99bJ0NfV1lRdqeUOgWN8I-CxPYgkwdKPvfBdsXw95KtzjPOddaK2e80wK4_xBWpVOPKzu9vThU2UzqDmbog7YUoK0Wedr3Q6hMCwZbJxmdYA-kkhn_fMsHAp_AV8TjY4Wa1RueA9acnXMqNYzSSWgv1QeEtav05NQzoBKXiIU4DkyR2dd0SvpXRBgmJLJEZjn7cgp78BKujDvpzoYWY28bCTWLCu0U00vvPx7mxv0UfoAij-Kn4R5t0iL6d2yy-0j8bDvU-Ng23whxejNZf1AdkCzQShEBcXCDUzJv84HE8V_7MuFgLTt123uk_0-fSTvO2SUOwzopHlgCQ0nxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروهای امنیتی عراق همچنان به منازل نمایندگان عراقی میریزن و کیلو کیلو پول از خونه‌ها درمیاران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/131103" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131102">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e16fea3ee.mp4?token=laiLU7PRmoswRx5DqRMdA3wdpiZay6tgLLOAgdTrIha9HvoI9mQNi8nxGQT4fGVebHATdPpEdupnPdpxyfSjLLdq1RogtxS8gDwEs63-1VCzyj_hlYbqpA4BW-68Sq_9Jzyp6oRVsaF5A2olSipupaqleBBbLyoxqmwgw9B-VJb1qYBogL369RLMi60827gelo0ugYcMd3R29H_WQjqcX0R8b4TfoLNhMcm3Q5P0PifCKYL2TiiLdTnprGz_sl_p3qYdaKnTlOEAPvjkeTtxT5bz3Z6LPJYRax_j5INN9ltCsKnixvEmkQmKZHMWGMJxB80TZZwRMnW_JHl3tnFarQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e16fea3ee.mp4?token=laiLU7PRmoswRx5DqRMdA3wdpiZay6tgLLOAgdTrIha9HvoI9mQNi8nxGQT4fGVebHATdPpEdupnPdpxyfSjLLdq1RogtxS8gDwEs63-1VCzyj_hlYbqpA4BW-68Sq_9Jzyp6oRVsaF5A2olSipupaqleBBbLyoxqmwgw9B-VJb1qYBogL369RLMi60827gelo0ugYcMd3R29H_WQjqcX0R8b4TfoLNhMcm3Q5P0PifCKYL2TiiLdTnprGz_sl_p3qYdaKnTlOEAPvjkeTtxT5bz3Z6LPJYRax_j5INN9ltCsKnixvEmkQmKZHMWGMJxB80TZZwRMnW_JHl3tnFarQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که شهر مجدل زون در جنوب لبنان در اثر اقدامات ارتش اسرائیل تقریبا به طور کامل ویران شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/alonews/131102" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131101">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHRvskUhkkOWi2loNjHxNVd7lx5k11lcViB36g0pz7vjjr7fNAtdqDmUHOwcJ57YYCWAOdANLcKM2MH97eL2x_Dw44eOYmyzuhwR2EUp42JrjLnujSBrP3_sBiEtWqOKkKw62MUtF_u7oogTDiQa_ct4LQYicXAGpIDPdepxwzPGpCDeI10o1CLzxQl-dz0otTBRUY0HYaCXUEuht4uTGx_O4BUXdTTHx_AWYW_XfecCfQKLiX9gZxtrIlnk45FkMQ5662wBB2kzig5lsct6iImJcpaAOhShP1bo85cgztpNwsgMbXYc-9DOTJdtcryXZboDJKe4-PbsyT2m_p2Z2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شین بت اعلام کردند که حمله‌ای اسرائیلی در غزه دیروز محمد فتحی عبدالحی ابو فخر، فرمانده گردان یابنا در تیپ رفح حماس را کشت.
🔴
طبق اعلام نظامی، ابو فخر اخیراً در حال جذب نیروهای جدید و تلاش برای بازسازی توانایی‌های گردان برای حمله به نیروهای اسرائیلی بود.
🔴
ارتش اسرائیل همچنین گفت که او فرمانده‌ای باتجربه در حماس بود که دو دهه به عنوان چهره کلیدی در شبکه قاچاق سلاح گروه فعالیت داشت و بر تلاش‌ها برای وارد کردن سلاح به نوار غزه نظارت می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131101" target="_blank">📅 19:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131100">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا: موسسات مالی وابسته به حزب الله از جمله بنیاد القرض الحسن و مقامات ارشد آن را  به لیست تروریستی افزوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/131100" target="_blank">📅 19:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab2996fef.mp4?token=ILSrXVX5-2qFVKNnHecJUho-6aKny_PrMv5DYUmLlVhuxOhDw3tUYNOcX0h2AJ2_0dk_j-5G5Dz7zeVXHMaMa8TZAwRksCmgdPCEjhFrW_XXCcrqqhQXKzUTB0IuCjvj5fUh0DNsF4GSyk10Q1OofQUb-Lyh2PFfA4tEf8VEZRCq9gmCdXDnrDVKQEB_jVZIMbQ7iYlYWw7AfPz7Z8-2gyt4Er4NDtepAbxxA6OeQC-3HgE8u_IzPj0JrxEj2q4Rzn3aDtCpzIiK8ddRAbT30QuK2Gqcu6Bk8BsFLf91cd2ohlxubfbI7bjcyaYxXZYzNgikAjkv-B7ircbmfHE5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab2996fef.mp4?token=ILSrXVX5-2qFVKNnHecJUho-6aKny_PrMv5DYUmLlVhuxOhDw3tUYNOcX0h2AJ2_0dk_j-5G5Dz7zeVXHMaMa8TZAwRksCmgdPCEjhFrW_XXCcrqqhQXKzUTB0IuCjvj5fUh0DNsF4GSyk10Q1OofQUb-Lyh2PFfA4tEf8VEZRCq9gmCdXDnrDVKQEB_jVZIMbQ7iYlYWw7AfPz7Z8-2gyt4Er4NDtepAbxxA6OeQC-3HgE8u_IzPj0JrxEj2q4Rzn3aDtCpzIiK8ddRAbT30QuK2Gqcu6Bk8BsFLf91cd2ohlxubfbI7bjcyaYxXZYzNgikAjkv-B7ircbmfHE5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت 6 بمب FAB-250 و FAB-500 شلیک شده توسط جنگنده‌های روسی به سمت مواضع ارتش اوکراین در جبهه خارکف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/131099" target="_blank">📅 19:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزیر امور خارجه عراق: ما مخالف گسترش جنگ هستیم و هدف قرار دادن کشورهای خلیج فارس را رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131098" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نتانیاهو: لبنان اسرائیل را به رسمیت میشناسد و اسرائیل نیز لبنان را به رسمیت میشناسد، به ایران و حزب‌الله میگوییم از اینجا خارج شوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/131097" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfXFXHEwfdAO2vtDTONGGZiN2OnxOVCDo1tYi9SjtZXtUse7BpRi5OprGfmcsEodaO6sNKoY0h86akTf7AD3YPC7mGEMpjWbJdzFzub7NS6JfdmAiw5EEHF1n10ESvLJeLjrV-UaP65E1wFG50wRcQqeFPvo9eIZ7HFfOkOSwm12LRBMUz6IBXFRDsw9M9R8mPsS6q5VdG45AP7SWilsxcVfMi7cUMDnYOn_4BeTHxpvfkBBZstDO67u0HvV6saGPd_ZOzZ_a1swS4uRyXExNgY0b2u-3m2jtWSL4QxBQCaddMVjuUZJb8LTCsjuBU6IfvOWapiLBoC3ir-VyaYbIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق تروث سوشال: دیوان عالی کشور همین حالا محدودیت‌های هزینه‌های سیاسی را برداشت! یک پیروزی بزرگ برای جمهوری‌خواهان و، مهم‌تر از آن، برای متمم اول قانون اساسی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131096" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxnbhBQdheFndifWixMffRAaRy_-3nAyaFO1UmbCRZv9M7IY3lU5gF6_LlOI54nUjvOX88YoZb46hyPiypo4ctZERuhC8e10Im9EwSBeFcNfnI5HGQixEni3L9OuirvHXh8jPXnSBChCOqkqNI1hOSlEb1lTbUOIwfSw80dnp42OZ5GdD6C9MUxPGnhE2-25XQikbATGCbqeYlH03-oaqtA94g92gzVMoy8jmZUETjozJJZDZGU0MwUlWP102mT443DpQXmvYiacjUFXgJHv36Vrto9vgZGS_iCwaKLkCpsbrION63wmV9SZgGuxRsrAdrruCLz5ED2AqtIcaHSgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده حکم داده است که ایالت‌ها اکنون می‌توانند از حضور دختران و زنان ترنس‌جندر در ورزش‌های زنان جلوگیری کنند و احکام دادگاه‌های پایین‌تر را در موارد ایالت‌های آیداهو و وست ویرجینیا نقض می‌کند
🔴
انتظار می‌رود این تصمیم بر قوانین مشابه در حداقل ۲۵ ایالت دیگر تأثیر بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/131095" target="_blank">📅 18:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxDpwWZm5I7AguIVhhMfmbznHuL7hahPyFERrYOU96lWK18sUa90zMYGDFpeQ_C8cr_EtG5WpS1Jn7i3lQJ3DJUcCeJw8uwhg7PEMtg1GxjYu64dyyshUeR3zKyD42-BX8J-kMk6twx_4LZECEeM9KF1RSgKnjFnrJpK4rEtdSwSXzUTd6CWfzYnbh6m0fUaRJwhmIBCl1JQgTzqB4sghZxo4eiBGt0shVwMfFLb8t0L2F0WfVMQSUCHV_5fc6sLqOSuxhBf_-1Q62BrpsWUqzJJWt_zU0thWQ2bwmRW9oJkvMMUInd6FMtN6If_R30ND-WW_EPjdvi4pcLiEn56Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131094" target="_blank">📅 18:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d0469c5f.mp4?token=cDxaTQUfDTs0doTvaPw2JyyA4iQeLcKbQbXDqghUpOuvbgtLGd4cjV5xQOlSwrZ_zsE9_p9cXIYsawHp8EVMcRWV5eshTAekZnqRt8fj3ceTgyVyw9y-6lhJkI1bqZeAg3D_Q__ix9Ai1u3CMPOx0AOqA02SC5gm8aPXhorC8xEBRVHsal88wiCiNFs5BitCO2w9zFWTTJSd-98WKWb-azUtRX-MuZXplakfjXxbzi8KaE8ZXOWM20gTCj3WgOEAlsofwgjZD-r7fAzb6uqmnoDpQ-sJdCV02FJlUJGEEdBDwSQ1tIG6UqVqYR7jX-XQ49dE4tr378djcy9ksz6XE37SwVkG_53Akw9o4lh7MB0NtsunokgZgbgiO4Ncbqf3_Egjqql_6gxX1tvVQRmtOIPBouUrK86DN0xJPY1MegEtVonl5HiqTIBb-zodPJ140snGJj5mSFhDm70wuhEbFpTkks5J4qniSuAjyj6W7nuAkmnpP0Mmw8-ufW6nSV9hmud1gZOygliFS_8YfRIXnk_lNFHYKx1E5TeNWJkcN-1uGF9xYTfKm9LNZCKppXDfNvWD7yw_O0KJkNEFxabXZXm2bTg4hcJrvEzT5joXD74ESm5JlWxnWa8q-rFwqkSd3Yh11mDNXgO-gZnzcWKncVi_LBtpMP6riGcOXbWSDtY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d0469c5f.mp4?token=cDxaTQUfDTs0doTvaPw2JyyA4iQeLcKbQbXDqghUpOuvbgtLGd4cjV5xQOlSwrZ_zsE9_p9cXIYsawHp8EVMcRWV5eshTAekZnqRt8fj3ceTgyVyw9y-6lhJkI1bqZeAg3D_Q__ix9Ai1u3CMPOx0AOqA02SC5gm8aPXhorC8xEBRVHsal88wiCiNFs5BitCO2w9zFWTTJSd-98WKWb-azUtRX-MuZXplakfjXxbzi8KaE8ZXOWM20gTCj3WgOEAlsofwgjZD-r7fAzb6uqmnoDpQ-sJdCV02FJlUJGEEdBDwSQ1tIG6UqVqYR7jX-XQ49dE4tr378djcy9ksz6XE37SwVkG_53Akw9o4lh7MB0NtsunokgZgbgiO4Ncbqf3_Egjqql_6gxX1tvVQRmtOIPBouUrK86DN0xJPY1MegEtVonl5HiqTIBb-zodPJ140snGJj5mSFhDm70wuhEbFpTkks5J4qniSuAjyj6W7nuAkmnpP0Mmw8-ufW6nSV9hmud1gZOygliFS_8YfRIXnk_lNFHYKx1E5TeNWJkcN-1uGF9xYTfKm9LNZCKppXDfNvWD7yw_O0KJkNEFxabXZXm2bTg4hcJrvEzT5joXD74ESm5JlWxnWa8q-rFwqkSd3Yh11mDNXgO-gZnzcWKncVi_LBtpMP6riGcOXbWSDtY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو تو منطقه‌ی حائل لبنان : تا وقتی حزب‌الله اینجاست و ما رو تهدید می‌کنه
🔴
نیروهای ما هم اونجا می‌مونن، به نیروها هم گفتیم هر تهدیدی دیدید، همون لحظه اقدام کنید
🔴
به کاری که با شجاعت انجام دادید افتخار می‌کنیم و بهتون خیلی افتخار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/131093" target="_blank">📅 18:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
امارات ممنوعیت سفر شهروندانش به لبنان را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/131092" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=jd-Lwyd_-rA5aWHRpEZUds_EjMlu9OrWGOgAGCBob4dRnuFUHrFmWJlywuB-aJe-Nfxxmxorhytdax4ko12SGEzgIie9sre1AALaCf0jNwAf2HNJ5XexOwe_N5cTvB6GCFNOnSjs1a9pPYRCE9NJiGdLu0v9EawPtztPHINO2CF2f6N7gb4tSkblJLqEABSh-Ye_MIo37hKsrjhcWioc2zFM7EbofYnjQKQrPwT_9b8FE0zELYPZYD1T5azrHWHmlFxx_hK9DfhPcFD90Tj0V26EO3IIsbaByPR5VvcbGmvqOsIXpl6GnyKR3GkcA4LDbqOjTG7Yioe4iO74-IoDng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=jd-Lwyd_-rA5aWHRpEZUds_EjMlu9OrWGOgAGCBob4dRnuFUHrFmWJlywuB-aJe-Nfxxmxorhytdax4ko12SGEzgIie9sre1AALaCf0jNwAf2HNJ5XexOwe_N5cTvB6GCFNOnSjs1a9pPYRCE9NJiGdLu0v9EawPtztPHINO2CF2f6N7gb4tSkblJLqEABSh-Ye_MIo37hKsrjhcWioc2zFM7EbofYnjQKQrPwT_9b8FE0zELYPZYD1T5azrHWHmlFxx_hK9DfhPcFD90Tj0V26EO3IIsbaByPR5VvcbGmvqOsIXpl6GnyKR3GkcA4LDbqOjTG7Yioe4iO74-IoDng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در شهر حیفا با صدای انفجاری بسیار قدرتمند منفجر شد که موج آن در سراسر منطقه «کریوت» احساس گردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/131091" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prz36HrrKFqZelhDKlM2Pn2gcTQY6LFddS0CVkjgpTh90iKk8XoDrUAP8IxLYM2oAsPzzuWKLcJP1i-z3_6Tus6vEPBQrwf_ez6-z5W4zG0H9JCAYCNc6klTlY9gKYreOT91AN9tJNot3LizjrGOdxLpt0riYi0BhiLy_igE_QWZn6cPoOV2rwgEJVklP-YHikCdorMGftJ5p4t5Dy9_od3XsyKFAomSFOwDSpi1hIpwz1_FJOkqFDk4Xsdm6iE1PR8-DuKh8Ls0LzP8AVICCO7xJ5K_DqBKzHnuFuaMuDVvhr-j7JMCGhhgjitnfXTzd5PMw6Fj-60DOTpY1r6Fbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/131090" target="_blank">📅 18:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایران و عمان، علی‌رغم مخالفت آمریکا، در حال پیشبرد طرحی برای وضع کارمزد خدماتی برای کشتی‌های عبوری از تنگه هرمز هستند
🔴
عمان این طرح را رسماً به واشنگتن و سایر متحدان غربی ارائه کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/131089" target="_blank">📅 18:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131088">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=LscqjLFTuX-rN_wDGsCQhisXW7JsPf6ww5gx5sqvl5qLoQPoGjwJaYVXvb4EqUnDXBINu7bnLt4IslUPdle_ot_XSEy0ESVlTNG3C5J3OJhcYJimtMLxe3UEWuq0ZHQfc0_PQI1oJItnOi1Q89dkwz0NQ32mvxXaZ9-cDHELEl5fr9mqdGEuIR-DzMZnSC7K9CRsIMd0q-OxkOzj-59IcCOZvl5Z9NmGKpd1o5RmlzD5wo0ZllEYlGG4bgjBfzuQzLo8FaQno7Wk2Ubxej5Bl2iqGZTKhMwTgA6Ms8Cuo-soAy3MOGtS44TDXV61TCrJSSnSE5zm8muhXjfg40IdJqKf9s2v82jCuZfNHYcz1OKDl-6_HiRehMwTasfwudkzk34IdVXJK_RveCRgZzPjqXAOr-DN9dTun_I4boB9EvbPvRpmr1554vk6DVBbCiDlqoK8X6GWhuPHHGff38sYQKzvq0iDxzBwkRz9-KIqWMYKw-dUMpVz9OwPY3CfAzNp4AeyS5FwAEzzSqntqiuyl8ePoSx-kIcr4e74R7MTYKcmMDCa4y7DucEOYFU6KSQxN4GfUfVnT3cWRr12m8EIDyDU8kk91hh6E7FAbqiqGJPI6JGeMeci9-cf6AG0y0_aiuYs5rV844xX8ibjoTCODV7S0ECWWDdiO6FJAe-bpU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=LscqjLFTuX-rN_wDGsCQhisXW7JsPf6ww5gx5sqvl5qLoQPoGjwJaYVXvb4EqUnDXBINu7bnLt4IslUPdle_ot_XSEy0ESVlTNG3C5J3OJhcYJimtMLxe3UEWuq0ZHQfc0_PQI1oJItnOi1Q89dkwz0NQ32mvxXaZ9-cDHELEl5fr9mqdGEuIR-DzMZnSC7K9CRsIMd0q-OxkOzj-59IcCOZvl5Z9NmGKpd1o5RmlzD5wo0ZllEYlGG4bgjBfzuQzLo8FaQno7Wk2Ubxej5Bl2iqGZTKhMwTgA6Ms8Cuo-soAy3MOGtS44TDXV61TCrJSSnSE5zm8muhXjfg40IdJqKf9s2v82jCuZfNHYcz1OKDl-6_HiRehMwTasfwudkzk34IdVXJK_RveCRgZzPjqXAOr-DN9dTun_I4boB9EvbPvRpmr1554vk6DVBbCiDlqoK8X6GWhuPHHGff38sYQKzvq0iDxzBwkRz9-KIqWMYKw-dUMpVz9OwPY3CfAzNp4AeyS5FwAEzzSqntqiuyl8ePoSx-kIcr4e74R7MTYKcmMDCa4y7DucEOYFU6KSQxN4GfUfVnT3cWRr12m8EIDyDU8kk91hh6E7FAbqiqGJPI6JGeMeci9-cf6AG0y0_aiuYs5rV844xX8ibjoTCODV7S0ECWWDdiO6FJAe-bpU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوباما در مورد ایران
:
ما تمایل داریم فراموش کنیم که هر جنگی - بار آن بر دوش مردم عادی است، مردمی که فقط سعی در زندگی کردن و مراقبت از خانواده‌هایشان دارند.
و بنابراین اگر بتوانیم از جنگیدن در منطقه جلوگیری کنیم، این برای مردمی که آنجا زندگی می‌کنند خوب است.
اگر تنگه هرمز دوباره باز شود، امیدوارم که به مرور زمان این موضوع به مردم عادی کمی تسکین از قیمت‌های بالای بنزین و قیمت‌های انرژی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/131088" target="_blank">📅 18:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=YCq2atLtZzNr2uAFPIV5d_ALZw2eOKCDs2UaiUh3WigwvN6a3eCmao8-vgmZP1lV3Mld2csEfJ8_nM69ulRCl7jrMruycTG41JzzRMwCkpuBo_pZzcTWS5KMikcV4YTt9i61mleTEneXjHbD_30gq1Vca4bV--v0F8gkdOT9HtdBh4z0Cjs7cHvNqII23J7IPQyefYQosCcbaii-KjNwAhTMpEMGF0YnJ4Wa2JukYlx207exTTPEMuIvEgWwOV-t2imiBkdCtHFzuKcuJHwXgsJBqEE0abflcl609l8c-B-qJvuzBjCNuLzlfRc8yZR2DV2xj2akmzJbPwMLFq0Isw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=YCq2atLtZzNr2uAFPIV5d_ALZw2eOKCDs2UaiUh3WigwvN6a3eCmao8-vgmZP1lV3Mld2csEfJ8_nM69ulRCl7jrMruycTG41JzzRMwCkpuBo_pZzcTWS5KMikcV4YTt9i61mleTEneXjHbD_30gq1Vca4bV--v0F8gkdOT9HtdBh4z0Cjs7cHvNqII23J7IPQyefYQosCcbaii-KjNwAhTMpEMGF0YnJ4Wa2JukYlx207exTTPEMuIvEgWwOV-t2imiBkdCtHFzuKcuJHwXgsJBqEE0abflcl609l8c-B-qJvuzBjCNuLzlfRc8yZR2DV2xj2akmzJbPwMLFq0Isw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
در طول درگیری ایران، اقتصاد آمریکا به پیشرفت خود ادامه داد. اقتصاد بسیار قوی بوده است.
ما حدود ۱۷۰٬۰۰۰ شغل در ماه ایجاد کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/131087" target="_blank">📅 18:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=O01zHwnOAW5j8Vl9k2ESwaSnITEM2uYBWoKaWUx3n_kWqsIyjJTH1ZBaOpUBXq9-46ZEC_nJA82OFukBB9e80lLBHiDzSFiz6IkYAeUyInROJhYoKpkdWLFoDQuvOKrbFAl5Brx0MR1r8HJyex313QEdN8kE3UWKDX_PcPH36H4uzuvPxgUCuGofHQi8MAQI1NN-eR21Ow-ElBTJOqF6TnfD6iVjyEZ880_dC_gtdLjGuxILRSvaj1bxgverz0iYZqTJpF00IS1KAyg-ZK3tsrLaWH5-NTcQxc5fdfmjGHpZVuQ51k9A-4WUIJ56zaGcC-KlAdJ5XS5VEcCvdAuYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=O01zHwnOAW5j8Vl9k2ESwaSnITEM2uYBWoKaWUx3n_kWqsIyjJTH1ZBaOpUBXq9-46ZEC_nJA82OFukBB9e80lLBHiDzSFiz6IkYAeUyInROJhYoKpkdWLFoDQuvOKrbFAl5Brx0MR1r8HJyex313QEdN8kE3UWKDX_PcPH36H4uzuvPxgUCuGofHQi8MAQI1NN-eR21Ow-ElBTJOqF6TnfD6iVjyEZ880_dC_gtdLjGuxILRSvaj1bxgverz0iYZqTJpF00IS1KAyg-ZK3tsrLaWH5-NTcQxc5fdfmjGHpZVuQ51k9A-4WUIJ56zaGcC-KlAdJ5XS5VEcCvdAuYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی:باید طی روزهای آینده روند جاری را ارزیابی بکنیم و بر اساس آن تصمیم بگیریم که به چه شکلی و در چه زمانی مذاکره برای توافق نهایی را شروع بکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131086" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
العربیه: ایران تا پایان هفته 3 میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131085" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxdsGxtLc2XtDy2JX2acKgxruNj0hhyT6Ry3ablgpXLzjm35kO2XUlDgJDNDzJVGFNQFyjBKhcFrAq-7kcwEpakU8mvvjVmbwp1b9vyvvmtCwjNnnr7Dij7LcSjXipYouboZNzIYuF1E8uVu3_rIClml7sq3fdzop50mWy8takmhqlGywUP6YW1_sqIMvoVtkctuIeowj7HVBAWSpdUazPQbR6eSe7LAtP1FTyD9yUiZrf_CHmqiat-Yj5_64FKsJJqfxv1NbTSHb5bPIT_3nmvY5ZE3XKNwbRFQAqkB77NeddVB5L2jokgbHc_0RX4uBEcETTlrNamJfOJ6uLYxnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مجلس رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/131084" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsJfBQ3kbjMm-FDOTgqA6oGdIiVu4XUsbdrkyjhIJWysJp4FbjzWN5ajNrhdk1Euhzayr-Jrsbr-UPjuueAYxzT99JyFwjCDGlewi7SSo-0PbFqGQWWdG-qPK9390iar9EuFikTNY1C6g4RZYomwVfv9mb__cNvfSE5my8VbEXd_zay4sTYG-L7_Zdu30xuFLDPhg0KlUeHcD8aB1AyVo4AXYbZqpSWaYYd5FMM6_RzYZZ72zg28dMmhueALPB-3h-UTbCSHavFv35YsXvIlxikYr3YFos89WAFzMRDT_CPsJz6ppJAM-QrJ1uWHjEPVBIWPLStYxxuFnS1LRLJ1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: با وجود معافیت تحریمی کشوری جز چین نفت ایران را نمی خرد و از بازگشت تحریم های ما می ترسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/131083" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEqfU5ZGltMfk-hA6zLheg6f0rVMESz6drg_8a3sNnubSHbxOWwivr_fr8xs5rlZchMzsmVjrm59XSHJgS_FNVU044hCIV4izkwITkjDyzyh65b71yp39aKMrPUmyGZguR2t1JdIFdtItbL4LVnyxYuDIDVvWRAqKG4sbm3liADc1f7aS6kZiSBngJWiis-UIAQIHToQH8wkbqSLrrO6e7GPZEgW6ovwx-hbZPwgANd2plZZS_IOkdvz03zLlG3hg8iJs4fCyqnSTjiqH6ZS1847s2Z1hwYGXPyftk_63wlWFin646dwdiPGENfNTgK9P-RiH9NapwTHDcXTRsateg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو مراسم قرعه کشی جام جهانی هر مربی تیم بزرگی با قلعه نویی عکس گرفته تیمش حذف شده (هلند و آلمان) حالا مونده دوتا تیم دیگه که آرژانتین و اسپانیا هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/131082" target="_blank">📅 17:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=qQBFXGCfsS1wcuvkQg1Rk8spPOqvz7WoDiuQEzs7m8U92oifuuqj1HhdjEYUYtsyTuPjGGqTvsy9D72Czm_BClwywIlLqN_tg0Czl_EPRRSWZ0RbtD1-CQ3EA2YYAuS4p4U8M-lfkNatTSorVlIjv23bNF1btF3pvsz3bjl-O4SE-1r4g_ji7NokIwP2SnOjBsci4SK-4-RA8X2CQbcleUOzOuMutJx3VrJ9MCdE-D2NnqvIcvJJpDZkqeVRKLjLes9wZhEDM160KDoJkWDIVu_HbtKvCBfUYGg5n6PN6znDfDMFJFylMCjMdaS758Ca4vdceFZi5U2GIKwSlVQlfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=qQBFXGCfsS1wcuvkQg1Rk8spPOqvz7WoDiuQEzs7m8U92oifuuqj1HhdjEYUYtsyTuPjGGqTvsy9D72Czm_BClwywIlLqN_tg0Czl_EPRRSWZ0RbtD1-CQ3EA2YYAuS4p4U8M-lfkNatTSorVlIjv23bNF1btF3pvsz3bjl-O4SE-1r4g_ji7NokIwP2SnOjBsci4SK-4-RA8X2CQbcleUOzOuMutJx3VrJ9MCdE-D2NnqvIcvJJpDZkqeVRKLjLes9wZhEDM160KDoJkWDIVu_HbtKvCBfUYGg5n6PN6znDfDMFJFylMCjMdaS758Ca4vdceFZi5U2GIKwSlVQlfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهین زشت حسن آقامیری به شاه عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131081" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IM7aMVEZyFTlEhbyNVOxRmVe8aNbbKdIGyDT9MiuwGqGWxHNaBrSlBZ1sX4WdaZU0XXDzMa2-n0swoglhLFt4KT0i9aS50eh7tN_H1a2GroJ11YAfMTucvQnmjvUW_coW9Q0vSqbiBVhJ_WM0PXqRwwN62lNITZiLGj2_-7OXzV0opYsCwFZBcVkL2kTpZU3BTrvmuQFVbhMH6Gb3LzljcjBD1k-Ww4DohZE3m6fMa3Ty5tdbmKVT7Rp83yPN_VXIg5w5glH0FefABtsLV73ZDAnamHX8qTvPOLRlSu61Y0EJBZiplfKJK2iaEll_YmGNwOVhdz__b8qsgXZu1zS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: نتایج تیم ملی عالی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131080" target="_blank">📅 16:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=XnzbDBU_yjQc1ulUh-tuuId8dbK7uZqeRJuFsIIyGzE1iRoPZYC9tVW-zHl0il4anwdeXK0sOErPq9_E6xhx1CSHLVizaHYu2K9n-BU_oLNlWwx00I43wRHDzpgo7YZmtwQ8Mt8-2e_QBl7pjPHItyd4RrIU9wnWxcYdbw-rrYKkxulMT3S1LiLjBuOZCwbtl_aUkqXEyk0Ify287s34rRO8cQGIm6QNHWip6p5m-t0csz_DUm9fzZ30nnrZ4TzxJsxFzkUfFz23c-YqjzdtUssizQMFZ31sqJvDE5aZ359mOoUCEhLcENB9dyUVEqbuvztEYvhodEF3NRFAcZxsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=XnzbDBU_yjQc1ulUh-tuuId8dbK7uZqeRJuFsIIyGzE1iRoPZYC9tVW-zHl0il4anwdeXK0sOErPq9_E6xhx1CSHLVizaHYu2K9n-BU_oLNlWwx00I43wRHDzpgo7YZmtwQ8Mt8-2e_QBl7pjPHItyd4RrIU9wnWxcYdbw-rrYKkxulMT3S1LiLjBuOZCwbtl_aUkqXEyk0Ify287s34rRO8cQGIm6QNHWip6p5m-t0csz_DUm9fzZ30nnrZ4TzxJsxFzkUfFz23c-YqjzdtUssizQMFZ31sqJvDE5aZ359mOoUCEhLcENB9dyUVEqbuvztEYvhodEF3NRFAcZxsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر کلمه دلیل؟ تجربه، آیت الله خامنه‌ای توسط مشاور قالیباف در آنتن زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/131079" target="_blank">📅 16:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بقایی: مردم عراق برای حضور در مراسم وداع و تشییع پیکر رهبر شهید در کشورشان لحظه شماری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131078" target="_blank">📅 16:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی ۲۵۰۰
ممبر از کایی ۵۰.۰۰۰
⚡
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/131077" target="_blank">📅 16:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
خبرگزاری تسنیم : روز دوشنبه بورس ایران تعطیل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/131076" target="_blank">📅 16:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=Rax-IVzGy2aA6uJ1yZU2oBVmRStCPaQMvRgXzl92Qaj9nf1GNiTyFVeQVhnWx1HdgcxyJJ_vtVtqfuUZxd9N6QuvLaK0kXuumcXukPg5CRkbJsorRV4qIjWwUXdcNeLM1SokKWSLZc3k3VmNS9Vl6PCb91x7ha0rIJX0RhefRXhoMAxpqrtROLAl-ZO7PRlZv-rb0kNrtxSPnGku7ekHoRynSV1WjcakYxfKM0LuuYv1CzZVo2iyHYv2E4wKGhbBpHC783wJukU23W1vmq30bEQIAjdYgL3N3NDaH8nawdF2h1nSM8GPYFKnc-lrOJDJwmfKQlifg8OfgsKbTetJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=Rax-IVzGy2aA6uJ1yZU2oBVmRStCPaQMvRgXzl92Qaj9nf1GNiTyFVeQVhnWx1HdgcxyJJ_vtVtqfuUZxd9N6QuvLaK0kXuumcXukPg5CRkbJsorRV4qIjWwUXdcNeLM1SokKWSLZc3k3VmNS9Vl6PCb91x7ha0rIJX0RhefRXhoMAxpqrtROLAl-ZO7PRlZv-rb0kNrtxSPnGku7ekHoRynSV1WjcakYxfKM0LuuYv1CzZVo2iyHYv2E4wKGhbBpHC783wJukU23W1vmq30bEQIAjdYgL3N3NDaH8nawdF2h1nSM8GPYFKnc-lrOJDJwmfKQlifg8OfgsKbTetJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای نظامی اوکراین امروز صبح مرکز ارتباطات ماهواره‌ای دوبنا در منطقه مسکو روسیه را هدف قرار دادند.
🔴
این سایت که بیش از ۵۰۰ کیلومتر از مرز اوکراین فاصله دارد، برای شناسایی و هماهنگی فعالیت‌های نیروهای روسیه در اوکراین استفاده می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131075" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آقای قالیباف به‌عنوان نمایندهٔ ویژهٔ ایران به چین سفر می‌کند و ترکیب هیئت همراه و جزئیات سفر به‌زودی اعلام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131074" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به فاکس نیوز: پس از رفع تحریم‌ها، هیچ‌کس به جز چین نفت ایران را نخریده است. ایرانی‌ها نتوانستند نفت خود را به دلیل ترس خریداران بفروشند
🔴
ایران تلاش می‌کند نفت را با قیمت‌های پایین‌تر بفروشد و سود آن اندک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/131073" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=mYpw00_zA8RPIJ6TDGsNPekOrvtjG0woTIX_T05nUgO4EddVFWlvBRz_1pxIR-SxjG48eZ_eO8yi_oH2QnXuBvvnxs6uUOQ3K3H794-q_ikF1xfA2jJpjWufcrsUg4vJUHCuuUDBWqKpdrJikLfuXBaFh-JLRUCQKR0Jb_XYYLLIKLuDEhwQ3l24rz_UTFgMj9XQwkJfO7PG2lQHnk_Zb9b8bghkR365ZRslMmdkdi6KTuJm-b_7lp4ywsaWViTDzfoHgkV0gndPgG9cArXY4zmYg3hERSGvfjok1MnP0m_Lir3LXFIwgkRW75LZdAqatr8Af2ozzqBo3ZHFVXfwow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=mYpw00_zA8RPIJ6TDGsNPekOrvtjG0woTIX_T05nUgO4EddVFWlvBRz_1pxIR-SxjG48eZ_eO8yi_oH2QnXuBvvnxs6uUOQ3K3H794-q_ikF1xfA2jJpjWufcrsUg4vJUHCuuUDBWqKpdrJikLfuXBaFh-JLRUCQKR0Jb_XYYLLIKLuDEhwQ3l24rz_UTFgMj9XQwkJfO7PG2lQHnk_Zb9b8bghkR365ZRslMmdkdi6KTuJm-b_7lp4ywsaWViTDzfoHgkV0gndPgG9cArXY4zmYg3hERSGvfjok1MnP0m_Lir3LXFIwgkRW75LZdAqatr8Af2ozzqBo3ZHFVXfwow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: ما هیچ درخواست رسمی در خصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم.
🔴
اگر درخواستی دریافت کنیم، آن را بررسی خواهیم کرد، اما تاکنون چیزی دریافت نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/131072" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=AMARR6_MNGXyhbOWGiQp7gFpcWRuqzjXZslalWlbO5wZVrMa0OroITUDGHq1L1B2nATe_eY0_qCN23vHOzcY2Q5JDxxynxhCNUr7OOWY3BgTlF0_i6LP4tGi7MdSijOyzgsjE2-42zQqvrz8Z_Hd0KqDjqPoEqZTplDNTRtyUaPkHRhOXSqw39cq5KLC9QcS-_swmWmqhd7bZ_h8sOhsUAq3qdkZG3ljQYPLRgDIZnyF4fZ0aHgI1PTYvWs6iwBFRanHbBBadZA2d5R7IXdb669Hwf-yjyDn5vdxDGQMcSOMlA_lLtxCemieF-UYGSwp3WPJhWr-vcUjpPq2HDjNbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=AMARR6_MNGXyhbOWGiQp7gFpcWRuqzjXZslalWlbO5wZVrMa0OroITUDGHq1L1B2nATe_eY0_qCN23vHOzcY2Q5JDxxynxhCNUr7OOWY3BgTlF0_i6LP4tGi7MdSijOyzgsjE2-42zQqvrz8Z_Hd0KqDjqPoEqZTplDNTRtyUaPkHRhOXSqw39cq5KLC9QcS-_swmWmqhd7bZ_h8sOhsUAq3qdkZG3ljQYPLRgDIZnyF4fZ0aHgI1PTYvWs6iwBFRanHbBBadZA2d5R7IXdb669Hwf-yjyDn5vdxDGQMcSOMlA_lLtxCemieF-UYGSwp3WPJhWr-vcUjpPq2HDjNbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: رقص و جشن مقامات آمریکایی به خاطر عدم صعود ایران به مرحله بعدی جام جهانی، تمام استانداردها و هنجارهای پذیرفته شده میزبانی را نقض می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/131071" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131070">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با تنگه هرمز، تکلیف کاملاً روشن است. بند ۵ یادداشت تفاهم، مسئولیت جمهوری اسلامی ایران را به‌صراحت بیان کرده است.
🔴
بنابراین، روندی است که آغاز شده، تداوم خواهد داشت و قطعاً جمهوری اسلامی ایران به‌خوبی می‌تواند این روند را بدون نیاز به مداخله هر طرف دیگری انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/131070" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131069">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
قیمت کولر ۳ برابر شد !!
🔴
مهدی بستانچی، رئیس انجمن تولیدکنندگان سیستم‌های تهویه مطبوع ایران: کولر آبی ۷۰۰۰ از حدود ۴۰ تا ۴۵ میلیون تومان آغاز و در برخی مدل‌ها و برندها تا ۸۰ میلیون تومان نیز افزایش پیدا می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/131069" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
