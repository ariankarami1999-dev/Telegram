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
<img src="https://cdn4.telesco.pe/file/NN4HfmiDHW0sqdnzSg7OUi4qHOzjbIdiVVC_KKl3ycV5uKohRGQ9O2m4FnlHP_x8PWY6wNz1m2xFs3IiwlRVrazdN256QAxqVpP2VhLgLoBZ9YehYMVfNFp8_EYGjNmrSzO0fXN6e7pQUr4D_GMvoAtrpNQ_jNhKr3T7oBlDA3QHzGqLgoRU9zwH45RKTlopK5AlbRE_trmUvGH-zD39t1eHNTjKGBLhUTH3KyFCjCVm8yIwJNQZ0TAY6P2TLVc7qZ0ZtZvQk1lnMeaGXod6v7XfOIruruDk3REBXePd5iSLyRAzWqXSJLDwB_L0zz3XrEHbn3iK2OQK3TxYG5RIxg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 975K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 16:18:26</div>
<hr>

<div class="tg-post" id="msg-138163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ونس پس از چندروز غیبت، در دیدار نتانیاهو و ترامپ در واشنگتن شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/alonews/138163" target="_blank">📅 16:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcNf5BlndsXQmCNG7eX5nuHn4_W02FygxgfZ4PBj0kDBGWQuqqMqGMDU3DGmQOAyzeVNPtPeWrNzrkvwOAH52NF0JlKuTmQEqGYtUo_UEO6ELHhk6ERYkCRScHByBQOw1YYH7wx_vqzdnYFyF90aMNYRPKC6H-ShjPn7ZHq-RzHMnlhqNbgnLQ6j1yXg7UynmO9Khd4PlPLcugPnAeLTYIjq0I4AaUxr6voyFNuXxkXZmhc-ygh_t3Q67C7BFHayBARHcSI9L4HxV9iF05uIEYO7b15nW16HAYJj3aJybV_hYSRatEa4H5qkvvxMjZN1v3EeURy8nP3guTr-vOlUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک دیپلمات ایرانی
:
تهران می‌خواهد پیش از انتخابات میان دوره.ای کنگره در نوامبر آینده به یک توافق جامع با آمریکا دست یابد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/138162" target="_blank">📅 16:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ به دنبال توانایی‌های اخیر اوکراین در زمینه پهپاد‌ها و مقاومت این کشور در برابر روسیه، دیدگاه مثبت‌تری نسبت به زلنسکی پیدا کرده
🔴
در عین حال، رئیس‌جمهور آمریکا نسبت به پوتین بدبین‌تر شده
🔴
ترامپ به فناوری‌های دفاعی کی‌یف نیز علاقه نشان داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/138161" target="_blank">📅 16:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ایموجی خنده تا اطلاع ثانوی برای غم‌ ملت غیرفعال شد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/138160" target="_blank">📅 16:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N0rH2srbHYD_btDzZ1sbD0gWA6C6VOh3Emn0rqUpxrIjNQLiOscGkAFP4AGnAsgqZ2QQmU_pscaZHhlJ3YJSLlbJjx0vGlA6q6HDlFoyVNvwldo9BXPmZeg2k5B68fjRlNzLD1rAutgCrMZwBgCoIEnYCfy-opQAG8zFk3ncSqZ1w4uf9T_K-lDaYmN_sslK8hryY3wp7M1qSbHgsEx64Qgs7TEkh5UIRGSP9fxUWDUxdkSkVyCFCXae3y2KxDB42ozKKDnlogZG-4q_FPr3vJ5VFKNkkMxgCiV3EhhWaTaNZ6nLBDqDMCw0-wkZgao8qz4j1Iy_TNzVhneR2aKSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استوری شهرزاد همتی خبرنگار روزنامه های شرق و هم میهن برای اعدام دو جوان کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/138159" target="_blank">📅 15:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4fb160c7.mp4?token=g3iWvyTjZhZ_FOCPgjimN9iDKIgOxqv2upRETEzwEcglJqenOxnUa2wQBei1Y-DSmi8TV2vm8yd8az-DCRSQHo0CrKiLNcS8uFtlr63_lzs_wk-rMSvBOLnXAzMN1uuPHitIPf-AMNSgfdWrOgPOfC9EJsjXGLxqFTVE__bTtRhiAtuodSZBggHXn0kvuE1lMJd8QGycAn6xlPX_iKB0kAvMq3IdlomL8Acclab63Vzi1JWnyVb_UpKY34uBHpdhoN9jfzWOkfFXhuaROeXNcM7XS2DANXrxB9S2DrzlaSlkoc1SW_UAJp1nMAhYTvCM241hmXUSnhByV9_fceKQpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4fb160c7.mp4?token=g3iWvyTjZhZ_FOCPgjimN9iDKIgOxqv2upRETEzwEcglJqenOxnUa2wQBei1Y-DSmi8TV2vm8yd8az-DCRSQHo0CrKiLNcS8uFtlr63_lzs_wk-rMSvBOLnXAzMN1uuPHitIPf-AMNSgfdWrOgPOfC9EJsjXGLxqFTVE__bTtRhiAtuodSZBggHXn0kvuE1lMJd8QGycAn6xlPX_iKB0kAvMq3IdlomL8Acclab63Vzi1JWnyVb_UpKY34uBHpdhoN9jfzWOkfFXhuaROeXNcM7XS2DANXrxB9S2DrzlaSlkoc1SW_UAJp1nMAhYTvCM241hmXUSnhByV9_fceKQpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبر کشته شدن آناهیتا آذر که از دیشب تو رسانه ها در حال دست به دست شدن بود، توسط خود ایشون تکذیب شد.
ایشون گفت از کسانی که اولین بار این خبر رو پخش کردن شکایت کردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/138158" target="_blank">📅 15:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نخست‌وزیر عراق وارد ترکیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138157" target="_blank">📅 15:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
طبق گزارشات متعدد اوپراتور های تلفن همراه به اینترنت بین الملل ضریب ۲.۷ دادن یعنی مردم اگه ۱ گیگ اینترنت مصرف کنن اونا ۲.۷ گیگ ازشون کم میکنن و اینطوری بسته های اینترنت با سرعت چند برابر تموم میشه تا مجبور بشید زود به زود بسته بگیرید...
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138156" target="_blank">📅 15:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کاش سگ توله‌های فاسد مسئولین هم اعدام‌ میشدن، هر گوهی بخوان میخورن و صدای امت معکوس هم درنمیاد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138155" target="_blank">📅 15:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqci7KeZl6lkCE0rpcKTtS5zOn2o-DHq6thRyqHS2UdnsZlgLDl1MKgy2z4Cvb2pkIbEm7vQPGA6EHOvJ6_GidCA-Oz4IWfnOmEuYt7JknVr9M_etkfgtSOMNGCC3BlGMsKUaSMXZNTKQvcwTkXfenSwxuZcrmm949y5nTG2KbmahlHSX70oFlCi0ui-c-iQ_CXNMEwDIpVIlouJcWnI_4t9VbLq_jSghlVjHgwOTgZQJky4zj_o77zWMa6FSX2FatZOb8nTWH6AR25SQfdjrXHSKoL4d2V-vpeVtnkgEgJ65l9fBQPxRG3TiH-i7VtpaKcSF2YV0HmHM2h3zYhA2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWv3PUdxCYxgbKfkL3qxeUI0Mn4hTXlPMVI8THGumFLAELF_NrkUVyyGbsFpU2c0guRxYb7HUam1asTKaO4fR-W_SPDsmTl2srAjSl-Ql8R-83fhDpDaWn1jOEdK-KZrU35vKvAFEBuZPShBYZCdebPHrlt_GIIVlzNt7p710VJ0cNy9jq7hyGJ8Rko3Sth7rfGoLBUPpcvjSVxab78uHUNNi7VMrheDUb6fbZ0mTxy5lBMJ2z2DHWJFSdv_6s-hB3tthy5hTrFc2bYRIgixy1WzcN12zLs_uzN4-75XAUb9vZZaM73qlR8pUiyXq-0X0DRegunLsg0qRXOax8jKUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعدام سه جوان دیگر
‼️
🔴
علی دشتی، قائم حسینی و امیرحسین ملکی هم در پرونده میدان علیخانی به اعدام محکوم شدن و از خانواده هاشون برای آخرین ملاقات خواستن راهی زندان بشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138153" target="_blank">📅 15:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138152" target="_blank">📅 15:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رویترز: کشورهای خلیج فارس با دریافت داوطلبانه عوارض عبور ایران از تنگه هرمز موافقت کردند
🔴
کشورهای خلیج فارس از طرح ایران برای دریافت داوطلبانه عوارض از کشتی‌های عبوری از تنگه هرمز حمایت کرده‌اند.
🔴
خبرگزاری رویترز به نقل از یک منبع در یکی از کشورهای خلیج فارس این خبر را گزارش می دهد.
🔴
این طرح توسط عمان پیشنهاد شده و هدف آن جبران اختلالات ایجاد شده در تجارت نفت پس از عملیات نظامی آمریکا و اسرائیل علیه ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/138151" target="_blank">📅 15:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
معاون برق و انرژی وزارت نیرو:
محدودیت برقی ۴۸ شهرک صنعتی بزرگ کشور از دو روز به یک روز در هفته کاهش یافت و برای حفظ زنجیره ارزش صنایع، محدودیت‌های تامین برق واحدهای فولادی تولیدکننده اسلب نیز کاهش چشمگیری پیدا کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138150" target="_blank">📅 15:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3870346ca.mp4?token=oozE14epcpD310bFkc-mBgTzcgidwMZpttbnLXI2z0WnF1hWhEqxKGER2orUyefbnNwcH60NwhhF493Vq3kE6k0FP_yjiSjfLjzLL9LElWA2fflKWf32TtdHyGVyeBJW1IBC2alad0h7y49-1BvjfwAGgk2Jlj417uvcnHd5N4DkNwDmSfRCIgAp56tFqFkDZzmjMP1Ot5V_0UNbHigxQc1BynCtch0g6mMCmEpa-Q8MgL5SRJwvp-gxrzDW8sWmUJCNkrTDVTY7tlzgCIF2RLoRwOQFM_i63kAlmCkCIDlwncznK630VPHIBxzvpDQo0WyTbzOY5RsfwRhtScTJVb3_faq4CAc3zqAaQwNbcsOGTXhpPX-3HHQghEjL6GwLzb6mTL3WO7_VlCwJF0ebZHujCG3G-x1Ru81hChbkIxoVTY455mDT-bHzhM4mzTBEHgNDWkfq6Y2F5G3CUYM34Wt1l0fbdaGqn4gOUb8ue2TAKFHjoPcro9juj3Ee2mYCSvGlRthU0K6TgBcXmaqFQYL-A7qf3JwhLN2xH83_HMZJeWaLKRtj_F9eb0y6PbFoF-626P_t7YhINXZdlRl0Acr32a0OpqheM7dTPJhNPy5JRwhLoENWQEcWwxDCNJnxiOgPnfg47QuQRnHJs3yUceOj-aphCZXyvdUDYZmM0Rc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3870346ca.mp4?token=oozE14epcpD310bFkc-mBgTzcgidwMZpttbnLXI2z0WnF1hWhEqxKGER2orUyefbnNwcH60NwhhF493Vq3kE6k0FP_yjiSjfLjzLL9LElWA2fflKWf32TtdHyGVyeBJW1IBC2alad0h7y49-1BvjfwAGgk2Jlj417uvcnHd5N4DkNwDmSfRCIgAp56tFqFkDZzmjMP1Ot5V_0UNbHigxQc1BynCtch0g6mMCmEpa-Q8MgL5SRJwvp-gxrzDW8sWmUJCNkrTDVTY7tlzgCIF2RLoRwOQFM_i63kAlmCkCIDlwncznK630VPHIBxzvpDQo0WyTbzOY5RsfwRhtScTJVb3_faq4CAc3zqAaQwNbcsOGTXhpPX-3HHQghEjL6GwLzb6mTL3WO7_VlCwJF0ebZHujCG3G-x1Ru81hChbkIxoVTY455mDT-bHzhM4mzTBEHgNDWkfq6Y2F5G3CUYM34Wt1l0fbdaGqn4gOUb8ue2TAKFHjoPcro9juj3Ee2mYCSvGlRthU0K6TgBcXmaqFQYL-A7qf3JwhLN2xH83_HMZJeWaLKRtj_F9eb0y6PbFoF-626P_t7YhINXZdlRl0Acr32a0OpqheM7dTPJhNPy5JRwhLoENWQEcWwxDCNJnxiOgPnfg47QuQRnHJs3yUceOj-aphCZXyvdUDYZmM0Rc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌زمان با ورود بنیامین نتانیاهو، نخست‌وزیر اسرائیل، به واشنگتن برای گفت‌وگو با دونالد ترامپ، رئیس‌جمهور آمریکا، گروهی از معترضان با تجمع در مسیر حرکت کاروان موتوری وی، علیه او شعار سر دادند.
🔴
معترضان با در دست داشتن پرچم‌های فلسطین، شعارهایی از جمله «لعنت به تو، بی‌بی» و «جنایتکار جنگی» سر دادند و خواستار بازداشت نخست‌وزیر اسرائیل شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138149" target="_blank">📅 15:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHwMA5KJO-cbwAyh4zPQWLMeQxSu2p2pbO0s9Z_NU2foADZlsDo2av_5UwvQaNn2oqYu3B_1jPgR3T4HUap2ZNmnbjLYHHUiVdIZd5x8FmBwyMx8UUmfiCEl6zUan__shzqE7iftAB7D6A9eb6ut8iNFt4xvrJ8NFSVuDXec4LGAx5AVRKj7OZ1gBnVczy8x4LuH63uOF3L2KcjppKpEptxHjYgFZcF_ISTVP6yFEzekQUYKiQRgzlY6APrf_pFyuLCi9owcMlljaDabrY4VD9tAz6PS5nIuXGomtisFIMmEyGfkHmzF0A6zcFWBwSvhPwWR1y6jkY4KcE4PrfaMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی الزیدی، نخست وزیر عراق، همچنان به سفرهایش ادامه می دهد.
🔴
او پس از سفر به آمریکا، ایران و عربستان حالا به زودی به ترکیه سفر می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138148" target="_blank">📅 15:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138147">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بانک مرکزی از ثبت تورم ۵۷.۷ درصدی در دوازده‌ماهه منتهی به خرداد ۱۴۰۵ خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/138147" target="_blank">📅 15:47 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
نکبت 57 بوجود اومد چون چپ نفهم فقط میخواست با فلاکت زندگی کنه ولی بعد از آوردن خمینی آفتابه بدست به ایران، خودشون از کشور فرار کردن رفتن تا مردم ایران سالها در رنج و بدبختی با یک مشت بی عقل دینی زندگی کنن و هر صبح با صدای اذانشون کسی رو در این خاک اعدام کنن.
🤔
تخم انتقامی که در دل این مردم کاشتید، تا تک تکون رو اخته نکنن، ایران رنگ آرامش رو نمیبینه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/138146" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138145">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229e970aee.mp4?token=UX7x12zY6DWwbDt8SGPsqMvn3QCudPx10nMsLDvWjN60KQZwzoFhK4pCrPfRgTqq0AKo9PZUyohlSuEuo4wzZDb7Iwza1qzWXWOXTMADJtB4UCu0IzCiBmPLNFHFAvxOsLdgmewq7OTDYv5v8aHAQW_OA_H6jjb682rnfRZrBLz__pibqe7n46gpzzeNtr0D5G-YgJIgm1wUj6fD5GFMYRJ2ryCNR6I77qH9-Xol6ma85TsLsC00sjJfMA4gJsnt_Cmaa9G5Xsy_yTvw9771ShQQzps7LuGH3P71ndI_MRVVn99i0RH3fiNb0Z31FeX6ft0ykjzt-aDLqKrDPT9YVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229e970aee.mp4?token=UX7x12zY6DWwbDt8SGPsqMvn3QCudPx10nMsLDvWjN60KQZwzoFhK4pCrPfRgTqq0AKo9PZUyohlSuEuo4wzZDb7Iwza1qzWXWOXTMADJtB4UCu0IzCiBmPLNFHFAvxOsLdgmewq7OTDYv5v8aHAQW_OA_H6jjb682rnfRZrBLz__pibqe7n46gpzzeNtr0D5G-YgJIgm1wUj6fD5GFMYRJ2ryCNR6I77qH9-Xol6ma85TsLsC00sjJfMA4gJsnt_Cmaa9G5Xsy_yTvw9771ShQQzps7LuGH3P71ndI_MRVVn99i0RH3fiNb0Z31FeX6ft0ykjzt-aDLqKrDPT9YVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امت معکوس جدول‌های مقابل کافه‌های خیابان سنایی تهران رو تخریب کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/138145" target="_blank">📅 15:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ffba1ed79.mp4?token=NEnE1KwgS2dJi4x6uYYJsJLYuh4_TTyCLiw2TnknD9sLM8xRsoXRluMX5E_JX5vZzeHlwi_cMLu78TUlSwOjsZ7TYHxRLRfAqNZrGlmqmK4J1eq0L4CbuKXv_WnSyGnuugpqKAua2DBKRJI8Igrr9O00g1jEEDI9HdcL2FgdbL7BFlZcdC9TMslK30k8NQiCL0HXQywOimNNwrJIMhTIzqYn77zeexJYATuqXz84NXieHyZSTw30DMpxOynZVkQ3kYTPjC7GrcE0es0umyOYdy259UqTBKZlrHvTxlyBmS5HE4NGGDqcpgZva63mKIHFnfzq1YOmpXe0cZk91OjLwK8FqS-G_4OrsYzpoh45BQF7T05wfiQorB0kZ1ayfVHU8m31IkmRaBhcHVnAJEefll4AyQtu8g6aNco9MjZ7jGfaa7AxNwu5xrRV6Jrlr3X83Bf_KqRoQmz9O0-pmDypmOodU1U3ePq4o1VR6vEh3hZgjKwdt-ADJcyjltns1ViHWK5b7rE8ZKUkrlR-1yhkAnxyjwquLZ16RPdK6f1k42u_4y7XIr7pg0c_ftctjZi7xNRbRzdzRS6qBU-QQ-FjQbYcikPKsZCdNLXffPGasaFp55JdOUSLEKSW2TgyLqnIF-p0Ha2l-cDLh9O5tjqlBnX5-oyeMu1CVnd0dJf9gDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ffba1ed79.mp4?token=NEnE1KwgS2dJi4x6uYYJsJLYuh4_TTyCLiw2TnknD9sLM8xRsoXRluMX5E_JX5vZzeHlwi_cMLu78TUlSwOjsZ7TYHxRLRfAqNZrGlmqmK4J1eq0L4CbuKXv_WnSyGnuugpqKAua2DBKRJI8Igrr9O00g1jEEDI9HdcL2FgdbL7BFlZcdC9TMslK30k8NQiCL0HXQywOimNNwrJIMhTIzqYn77zeexJYATuqXz84NXieHyZSTw30DMpxOynZVkQ3kYTPjC7GrcE0es0umyOYdy259UqTBKZlrHvTxlyBmS5HE4NGGDqcpgZva63mKIHFnfzq1YOmpXe0cZk91OjLwK8FqS-G_4OrsYzpoh45BQF7T05wfiQorB0kZ1ayfVHU8m31IkmRaBhcHVnAJEefll4AyQtu8g6aNco9MjZ7jGfaa7AxNwu5xrRV6Jrlr3X83Bf_KqRoQmz9O0-pmDypmOodU1U3ePq4o1VR6vEh3hZgjKwdt-ADJcyjltns1ViHWK5b7rE8ZKUkrlR-1yhkAnxyjwquLZ16RPdK6f1k42u_4y7XIr7pg0c_ftctjZi7xNRbRzdzRS6qBU-QQ-FjQbYcikPKsZCdNLXffPGasaFp55JdOUSLEKSW2TgyLqnIF-p0Ha2l-cDLh9O5tjqlBnX5-oyeMu1CVnd0dJf9gDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
فروریختن یک مرکز خرید بزرگ در ژاپن در پی وقوع زلزله
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138144" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138143">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
روزنامه هیل:  عربستان سعودی هیچ نشانه‌ای از پذیرش شرط تازه دونالد ترامپ مبنی بر عادی‌سازی روابط با اسرائیل در ازای اجرای توافق هسته‌ای با آمریکا بروز نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/138143" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138142">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1cQdip1xkgLVyDyCrdFLwu4ZnHP6M1YjsjAL8ATO7uLkdHxvljATPo7mSbtF-11ht3Vrvfu8xGVbXCpr1DnGwzo1WXvlFhYPzalSfFPMCO_hSv8htmR7ER-hkJBbWmtz-P-m0CegAIQVxS6WbHB87mr7zrky2_Cd8Z4DaDXLVIBI5cf5HBLii9Qo7hIqlsnyQfzCsj21xqeYyRrxwLsGqTya-_oO_svMmQ2pUPS1SZcL-jqdk1IYN1G2TnECruVbQaL0s1Ps7Dl15sOTFujOqM0MI4jdZxLDaOmSHpV9AvhHFH0lhFyZW9A05-S-Xp-mV3mI3qvUtp_z9tS4uL14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عضو شورای شهر تهران مدعی شد: شنیده‌ام ۴ گزینه در حال تحریر و تدوین برنامه‌ای تحولی برای سازمان صداوسیما هستند.
🔴
تاریخ هفتم مهرماه، مدیریت پرچالشی به پایان می‌رسد که دولت، مجلس، جریان‌های مختلف، حتی بخش جدی سازمان و مردم منتظر پایان آن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138142" target="_blank">📅 15:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138141">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نیویورک‌تایمز: وارث اسرارآمیز ثروت جفری اپستین کیست؟
🔴
کارینا شولیاک، دندانپزشکی که به عنوان آخرین نفر، پیش از خودکشی اپستین با او صحبت کرد
🔴
اپستین اندکی پیش از مرگ، سهم بزرگی از ثروت خود را به این زن واگذار کرد، از جمله اینکه یک انگشتر الماس به وزن ۳۳ قیراط را «به عنوان مقدمه‌ای برای ازدواج»، به او اختصاص داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/138141" target="_blank">📅 15:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA1iqpyZz15aJ-Yi6AMlv3rdsG2CdUQRLS7I572jjl1uLPvI7iH_doxd9CS6bNDYiJV2aevAJTvTNAnzsveqjAuPXM0zswMHqQ1oK9Zu_5uZxp3ARXqs2KDokGsIPPt4PzD_A55aqVyJVLNm9pGmAimFkPJVCVEr9SMhHXHhIuGvvXKQ2BJjjKuQPhbnPOi0oFw7ywKu6Ccrp1XFLPle_B54WIxPEGUk3NNyg6Bz_jTb2SQECnH0Tx1XOOdGubnRXaHmQlNNVyjWGR_aa7O1aRNBEk77h9eBvIN50fwAgJ5_xvRZCZjA9CPvke06rdPfkSerRqZWH72-QpuF9xtapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در آپدیت جدید اینستاگرام می‌توانید یک نفر را به‌عنوان «یادبود» یا همان وارث انتخاب کنید تا بعد از فوت شما، بعضی کارهای پیج را انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138140" target="_blank">📅 15:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIKXCKkvx4dbJ6aeqO4IqU7dZoUyjruinq6FyXEH_t8kIqD801r19FjwhRFsGriZ0mj3-2u7jjrXVMNBqghAiZih8zoLvoyuPSBL8JxdnrdFj5qCZwxn_72sqg5MTRyGGIDs5lL9McLS9gzUFCVM5bJPew-JunRuKiaj6tcvskm6FR03Rn-VuyMctc4dmYF62YUw5airCqS4WeF0LiiP19mmyPM003vKjv48LpxsxxE7utPSHert8fhOWqXyCCiaNEeL3C4bNHKCF5sQpL4_7MoWdh4uA2EJYR91uedRc0AbAE9cwYnpckxWdtvPXMZf4kzMJoFfwvfraun2IC0LAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۸۷ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/138139" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزیر ارتباطات: اپراتور های ایرانی در عراق را برای رومینگ تقویت کردیم و اینترنت برای زائران کاملا رایگان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/138138" target="_blank">📅 15:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سی‌ان‌ان‌ به نقل از مقام کاخ سفید: ترامپ در کاخ سفید با زلنسکی و نتانیاهو به طور جداگانه و پشت سر هم دیدار می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138137" target="_blank">📅 14:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ادار‌های استان کردستان فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/138136" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رویترز: آرامکو پالایشگاه جیزان را با ظرفیت ۴۰۰٬۰۰۰ بشکه در روز، پس از حمله انصارالله که به تأسیسات این پالایشگاه از جمله مجتمع گازی‌سازی و مخازن ذخیره‌سازی آسیب رساند، به طور موقت تعطیل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/138135" target="_blank">📅 14:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قالیباف: تمرکز مجلس و دولت بر امور مهم و فوری باشد
🔴
تأمین معیشت مردم در دستورکار حاکمیت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138134" target="_blank">📅 14:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
الجزیره: ایران در قبال وضعیت در تنگه هرمز «انعطاف‌پذیری» نشان داده‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/138133" target="_blank">📅 14:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138132">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8Fz-WkLizPWwUVq_DbLIvX_g7F1uGyy-4hs4AVDXlmUFRaVnYYjgXNsp3SLk-AUuvmoyr3MO8P2PRkDHJkID-e5gOZnJBbbQNtd7Y_8aQIRh5LT4_2uMInNZd0eCfRMJPK-lT2W755ljNMB4CUlmlSSNp5mDOh1MnekE3zhQmux_hOMMRKZKnBDy7FfIc-P0wCIFmdX_HHa-d7RFW8Tqew1KZ8FahA7oUYF424Q-x0BqFdoHs3BkIQDszAfVi8NDK8O4Y3xOnjdSWZbpiKNDw853zTHU6x6ZxWUlqJrlAVrfwTc0LQRWtcrXbD5zxqO7GfFjhOowx1rAS2ulsoCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: سپردن کار به مردم و اعتماد به نسل جوان باید دستور کار روابط‌عمومی‌ها باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138132" target="_blank">📅 14:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138131">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AElMRRdk1oMEIIG6L8HJwz1gt6nDlqMU3Q8MbyLMgfQtkbcCREW4yFsDKBHd3sLyQblLugLWpforGCFpJGoUY_31LgxweA5ymH43j_PXcpYGNGHEmqVWpYaHn2zzSMZ6df7e56SlzB-Ir12eJfXrHmrIwmqW9ZjJW4lsMfYPfd4OVpBGrtjtSCupCA6S-6jW5cZ-4-Ed36D464o9oacnnR0jLe-4Vaxgeb1scNFQEm0-hK1U2IkuD87pnbxG9Gfv_BPb04FqGc_7Xmx6O6EFbMFmssKv4CXwetRLhr81Y0kcwkDnYTpSATrztbFmt5bIAAJd-BwGKR-l0dGZNsD1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال‌های پایش اوکراینی ادعاهایی را منتشر کرده‌اند مبنی بر اینکه ایران ممکن است در روزهای آینده تا سه موشک بالستیک به سمت اوکراین شلیک کند.
🔴
وزیر امور خارجه ایران گفته است که این حمله "نمی‌تواند بدون پاسخ بماند" و نمایندگان مجلس هشدار داده‌اند که کی‌یف "درک خواهد کرد" که ایران چنین اقداماتی را نادیده نمی‌گیرد.
🔴
موشک‌های بالستیک میان‌برد ایران، مانند غدر، امید، سجيل و خرمشهر، از لحاظ فنی می‌توانند از شمال ایران به خاک اوکراین دسترسی پیدا کنند و سامانه‌های پدافندی پاتریوت اوکراین در برابر آنها با مشکل مواجه خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138131" target="_blank">📅 14:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
تایوان در طول تمرینات نظامی سالانه خود به نام "هان کوانگ" که از تاریخ ۵ تا ۱۴ آگوست برگزار می‌شود، انتقال تولیدات نظامی و تبدیل کارخانه‌های غیرنظامی به کاربری نظامی را آزمایش خواهد کرد. این اقدام در راستای آمادگی برای احتمال حملات احتمالی چین به مراکز دفاعی و لجستیکی انجام می‌شود، طبق گزارش رویترز.
🔴
این تمرینات، سناریویی را شبیه‌سازی می‌کنند که در آن چین از تمرینات نظامی روتین برای پنهان کردن آمادگی برای یک حمله استفاده می‌کند، که این امر باعث می‌شود تایوان به سرعت سطح آمادگی رزمی خود را افزایش دهد.
🔴
این تمرینات همچنین توانایی ارتش را در توزیع تولیدات صنعتی، انتقال کارخانه شماره 202 سازمان تسلیحات در تایپه، بسیج تولیدکنندگان غیرنظامی و حفظ مسیرهای دریایی حیاتی از طریق عملیات مشترک نیروی دریایی و گارد ساحلی، مورد آزمایش قرار خواهد داد.
🔴
سرعت اینترنت سیار نیز کاهش خواهد یافت تا میزان مقاومت در شرایط جنگی و در صورت اختلال در ارتباطات، ارزیابی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138130" target="_blank">📅 14:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت ایمنی کره جنوبی : روز سه‌شنبه نشت فسفر سفید در داخل یک پایگاه هوایی بزرگ نظامی آمریکا در پیونگتائک، استان گیونگی در کره جنوبی رخ داده و برای ساکنان نزدیک آن توصیه تخلیه صادر شده است.
🔴
طبق گزارش سازمان بهداشت جهانی، این ماده بسیار سمی اغلب در سلاح‌ها استفاده می‌شود و می‌تواند در تماس با اکسیژن مشتعل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138129" target="_blank">📅 14:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
معاون اداره‌کل حفاظت محیط زیست خوزستان: آتش‌سوزی امروز ۶ مرداد در نیزارها و پوشش گیاهی خشک حاشیه کانال زهکش المهدی رخ داده و خارج از محدوده تالاب هورالعظیم است.
🔴
تاکنون هیچ آتش‌سوزی در محدوده تالاب هورالعظیم گزارش یا مشاهده نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138128" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
حماس: هیئت مذاکره‌ کننده ما عازم قاهره شد
🔴
انتقال به مرحله دوم طرح «ترامپ» از محورهای مذاکرات در مصر است
🔴
هر گونه توافق جدید باید محدودیت‌ها از زندگی روزمره فلسطینیان را کاملاً رفع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138127" target="_blank">📅 14:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
معاون توسعه مدیریت و منابع استانداری مرکزی: ساعت کاری تمامی دستگاه‌های اجرایی استان مرکزی در روز چهارشنبه هفتم مرداد از ساعت ۷ تا ۱۱ صبح تعیین شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138126" target="_blank">📅 14:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138125">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
نتانیاهو به دستاوردی رسید که چِرچیل نتوانست.
🔴
او ترامپ را با ما متحد کرد تا علیه ایران اقدام کنیم، به طوری که آمریکا را متقاعد کرد قبل از وقوع یک حادثه مشابه پرل هاربر، وارد عمل شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138125" target="_blank">📅 13:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138124">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teXAQIMKSKL95NFznXgJ93Y8nVtrNAoWIXRKMoRn9Tu6ejMlX61HDw0dLfZSKRZ7i9ibjIciY3BjRErTAZj4M9Ux6c35Kxoaizf_WMn2JY3UwssiMH1wR9zf8QorBF2vmDXpGTRngcfTmj71b46doeCrqkmUQXBSzBnJrs6YhwOPkjAHr_NUpUCv6pxe1HdJPzTTxPah04VcvSB7Nrrfay8o0AY4_OBYwbkw6p_JnOm00-M1BwMl3sf_ZwZCCKe1Yh4ZwHsQ1Vb5LWV_CHNO6ZyBW-udHRqo9YFFATXavdU-VFadGmXnEjhqINeplEauVwpdFkRnfnBchqFTOfSovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی : تصمیم به عدم تشدید تنش پس از جلسه کاخ سفید در روز جمعه گرفته شد. دو منبع اعلام کردند ژنرال دن کین (رئیس ستاد مشترک ارتش) و جی‌دی ونس (معاون رئیس‌جمهور) نگرانی خود را از تشدید جنگ ابراز کردند.
🔴
کین به ترامپ هشدار داد که اگرچه ارتش قادر به اجرای گزینه‌هاست، اما پیامدهای منفی از جمله کاهش ذخایر مهمات وجود دارد.
🔴
کمبود مهمات یکی از عوامل کلیدی در تصمیم‌گیری ترامپ و تیم امنیت ملی بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/138124" target="_blank">📅 13:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138123">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f005de3ae2.mp4?token=fO-r5D9lTVmOREOLNk4sGNjLz-oIhLSEXbuNYQlxi44g4ywX2g2Po76ZBaTDS27M0s-pVejZqSpfcJAhmDKEPIur9xvKspiHo_FRLc9_d5v9aVHTu7iHlD5fd0W2JtKPbGksdpZJq8Ree1wNYsSWXmgq6A_gzuezTvu-vvomPYLzEAXBPcF9bFQPfCjPoRPMIPpDn0Q4pwe4XGHva7i2tkTE3uuTtbgJnwFqMrfBhWYO6jZ7vQOJNmj55U06q1A9YWxM5bSC59TzixsIepqhgKREH9hPZR62ExrK6-pfrNDS6VMv-eCVQEkaOhLoNQNnSiByfP80Ej9qJimQvyiVWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f005de3ae2.mp4?token=fO-r5D9lTVmOREOLNk4sGNjLz-oIhLSEXbuNYQlxi44g4ywX2g2Po76ZBaTDS27M0s-pVejZqSpfcJAhmDKEPIur9xvKspiHo_FRLc9_d5v9aVHTu7iHlD5fd0W2JtKPbGksdpZJq8Ree1wNYsSWXmgq6A_gzuezTvu-vvomPYLzEAXBPcF9bFQPfCjPoRPMIPpDn0Q4pwe4XGHva7i2tkTE3uuTtbgJnwFqMrfBhWYO6jZ7vQOJNmj55U06q1A9YWxM5bSC59TzixsIepqhgKREH9hPZR62ExrK6-pfrNDS6VMv-eCVQEkaOhLoNQNnSiByfP80Ej9qJimQvyiVWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش ها از وقوع انفجار های مهیب در مسکو پس از حملات پهپادی صبح امروز اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138123" target="_blank">📅 13:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138122">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز: در غزه، ما نه تنها آنچه را که زیر زمین است نابود می‌کنیم، بلکه تمام خانه‌ها را نیز ویران می‌سازیم.
🔴
امروز، تقریباً ۷۰ درصد غزه ویران شده است.
🔴
بیست و چهار روستای لبنانی، صدها سال قدمت دارند — ما تمام ساختمان‌ها را نابود کردیم، نه خانه به خانه، بلکه کل روستاها را.
🔴
نابودی آن‌ها به پایان رسیده است. باید درک کنید: ۱۵,۰۰۰ تا ۲۰,۰۰۰ خانه در تمام ۲۴ روستا نابود شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138122" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138121">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/000767d83f.mp4?token=OtubK-VkenvJOuxZBcLPhcVyd-LU3nxUtyVzEkg0vimQNxp7s27utYOjAlm1U4GDAOeICWXzC9StXy27eXOje0s7L_J6tAD7HtW-bYe_Edgi2KeI7-_WUc8hxYHact58NUCQfQwMapiarZATkT8yDQV-GtVTGRy3CiDwjKsIl6H7Y4Zb55rwrD9EZX_O2mKH9ck65Z-5xEpE-5-pvFEyGphxkl9guPuBGQpF2gQ_ORNRgov10hIXBeDsv1yYfQhoqalr7Bv2D2RIwH3oU-xB9bD_Lt5h_tK4YkSYH_VaijhU1PavhAjE9hahIAFjtIOlGoDuYpH67j2JtiQZBeINMJnHbOfDIkFGAmwxWKZFt3Q0AP2HkkeJGEStC-1-OAVFC7q22spgaRG2SVA03-GSCzdSsD2pWvv7WfFTLEroO9CdjT5SJ4IOY8DRRszEttZQpTjH52rHAOkfxMPNgkN0bu1w2nF2rMpghplrh8pTIwk7EVUJdXqwfJL_bIuDStk0ZrzCMpgubY5qXooPQK3h0mYa1KFF6tAoktcetXbNNcIW3TfIJrEqYKALZBPQUWryC9It_JPdsa3yTHXsXN952wMGO3z4phwB585I_UMlch99Q5rOyIRfPIx9qWek2fCbdwk7588O4HTi30Fqb7Kt70bisayxE0Gwyrez_3O7U2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/000767d83f.mp4?token=OtubK-VkenvJOuxZBcLPhcVyd-LU3nxUtyVzEkg0vimQNxp7s27utYOjAlm1U4GDAOeICWXzC9StXy27eXOje0s7L_J6tAD7HtW-bYe_Edgi2KeI7-_WUc8hxYHact58NUCQfQwMapiarZATkT8yDQV-GtVTGRy3CiDwjKsIl6H7Y4Zb55rwrD9EZX_O2mKH9ck65Z-5xEpE-5-pvFEyGphxkl9guPuBGQpF2gQ_ORNRgov10hIXBeDsv1yYfQhoqalr7Bv2D2RIwH3oU-xB9bD_Lt5h_tK4YkSYH_VaijhU1PavhAjE9hahIAFjtIOlGoDuYpH67j2JtiQZBeINMJnHbOfDIkFGAmwxWKZFt3Q0AP2HkkeJGEStC-1-OAVFC7q22spgaRG2SVA03-GSCzdSsD2pWvv7WfFTLEroO9CdjT5SJ4IOY8DRRszEttZQpTjH52rHAOkfxMPNgkN0bu1w2nF2rMpghplrh8pTIwk7EVUJdXqwfJL_bIuDStk0ZrzCMpgubY5qXooPQK3h0mYa1KFF6tAoktcetXbNNcIW3TfIJrEqYKALZBPQUWryC9It_JPdsa3yTHXsXN952wMGO3z4phwB585I_UMlch99Q5rOyIRfPIx9qWek2fCbdwk7588O4HTi30Fqb7Kt70bisayxE0Gwyrez_3O7U2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:شین بت در برابر تهدید بسیار جدی ایران که علیه نتانیاهو و رهبری سیاسی و نظامی اسرائیل متمرکز است، محافظت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138121" target="_blank">📅 13:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b128a10dae.mp4?token=XeJRGuyeNHeuj9PPDVqXIPq-G3IECamvSspJBm7pppTbRUIhh5AyZ1V6i_IuyuPDQ7RvqGrc6Rut0a5-DYiHGcTd6Ee1Lv8Dow03aAOEW-uiuUmugXJ5eWXh9i7XJlZ6bLQUwP0Ui2n9RVKM5aLj3quV6Z3UOzcaB6fxau4HXN8WEVFvCG2ND0Z29TZ38j7inZHskNrXj_O1Rz-JVP_IMilV31iEz2ZcgiuWupjVRgA3gO2jishxhzp4957L3O3vcI-q8dRUi4c0Wg5M1_I8OLMLsGOWHhHuzup_9Jad858Dkm0D0a223alnTALy29a24jHgitRGxtyupq8rNknxT6Hb2Vo_7wJKpTNxjoa8W9poIwB2KL087ecKBu-lAAcsgq1uDkfYCHB-vIR8fllsn24t1P8bUSmYaGGNUVTeXXZkCSq4kJl10ywWAZj3FejV9BcvzKh6a8sroU1jxw2Z5aEfddSUmPyyiUN16SkvegzqqMiBTJmWBqdfzP17aoIPrMPWA0sLQEGbneKqhfcUs8JN_cKNQMvj0v3Fx_1OkXf1vphz1Mu4C8uE47X18v0RNEKEGkfSD0-dBv9riMf_sRI90JaL5nxp9UjarS9OJ8tId6DZobnfpm7aoTKHSsvSUOQF_7V3F0g0sO8miUvxEdAwiaWJ1Ap0dbYY6UvjQdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b128a10dae.mp4?token=XeJRGuyeNHeuj9PPDVqXIPq-G3IECamvSspJBm7pppTbRUIhh5AyZ1V6i_IuyuPDQ7RvqGrc6Rut0a5-DYiHGcTd6Ee1Lv8Dow03aAOEW-uiuUmugXJ5eWXh9i7XJlZ6bLQUwP0Ui2n9RVKM5aLj3quV6Z3UOzcaB6fxau4HXN8WEVFvCG2ND0Z29TZ38j7inZHskNrXj_O1Rz-JVP_IMilV31iEz2ZcgiuWupjVRgA3gO2jishxhzp4957L3O3vcI-q8dRUi4c0Wg5M1_I8OLMLsGOWHhHuzup_9Jad858Dkm0D0a223alnTALy29a24jHgitRGxtyupq8rNknxT6Hb2Vo_7wJKpTNxjoa8W9poIwB2KL087ecKBu-lAAcsgq1uDkfYCHB-vIR8fllsn24t1P8bUSmYaGGNUVTeXXZkCSq4kJl10ywWAZj3FejV9BcvzKh6a8sroU1jxw2Z5aEfddSUmPyyiUN16SkvegzqqMiBTJmWBqdfzP17aoIPrMPWA0sLQEGbneKqhfcUs8JN_cKNQMvj0v3Fx_1OkXf1vphz1Mu4C8uE47X18v0RNEKEGkfSD0-dBv9riMf_sRI90JaL5nxp9UjarS9OJ8tId6DZobnfpm7aoTKHSsvSUOQF_7V3F0g0sO8miUvxEdAwiaWJ1Ap0dbYY6UvjQdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز، اعتراف کرد: امروز شجاعیه وجود ندارد، جابلیا وجود ندارد. تمام آن مکان‌های وحشتناکی که به یاد دارید دیگر وجود ندارند.
🔴
رئیس فرماندهی جنوب به من گفت: «من خانه‌هایی را نمی‌بینم، من سواحل را می‌بینم.»
🔴
ما غزه را نابود کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138120" target="_blank">📅 13:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138119">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102fae8e7f.mp4?token=TzOQBGOTGjySXr-csYQeWNXJCzJGwd5TGymrtyOLcdMR8YTaxR5dopA7kwdK_sumIYfMtcq2oX02DofhF0uWBYe7xxYXvLnxppe0Rbw1gE6Hg3fINkVcJjGx_nYdy468hlGVKZTzVWKSyr4YpOw0y-4-OM-ZFHFfCWm_OdDZwjDdfHPuAf5rEylCKQYMmBTN5lPLEuzR6cOmSd3n2DLb6O1JxNvfowXrN8382w1Hc69RjkRIyieYxJRx-9grfYfQ_ci-4yJXlj4ba6HElp-NW7u4UcjhbUWEx0jn-B3fdSJkFB20eUqyi0HMSj5VAGvuwPm7PGHRhd2wITbmqf2I0ystIUpn8MMRXrcaBzj0h7qewQ0w_5XLvk2TckEpPXWasnqvW0tA8Qmz8YU230r23hJ4a7LvZ9uu6XY94-Vb6go11TH8En0zO_vzi-gu9j8KX9GQ6w28TVGXYC25BLROdKRwKeZ659vT_aL1Qw_T16iBYPhFqGn5tY6xaW2nEr6BEMOksdEk6o8miQdkTIXvMqUDlMrFz9Jg-GbGsJu8QPQBugYKWIs80d892y5MMkX4KDrirBtVOoUWJA8abj8EiAo6vaJlw64a-kke-n9LzMtlPsRf2eQehY0EruKnulsmCIBz3FGJr9ja6AFdkDeggkGG-ghJFYNr9b9vbO1sbbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102fae8e7f.mp4?token=TzOQBGOTGjySXr-csYQeWNXJCzJGwd5TGymrtyOLcdMR8YTaxR5dopA7kwdK_sumIYfMtcq2oX02DofhF0uWBYe7xxYXvLnxppe0Rbw1gE6Hg3fINkVcJjGx_nYdy468hlGVKZTzVWKSyr4YpOw0y-4-OM-ZFHFfCWm_OdDZwjDdfHPuAf5rEylCKQYMmBTN5lPLEuzR6cOmSd3n2DLb6O1JxNvfowXrN8382w1Hc69RjkRIyieYxJRx-9grfYfQ_ci-4yJXlj4ba6HElp-NW7u4UcjhbUWEx0jn-B3fdSJkFB20eUqyi0HMSj5VAGvuwPm7PGHRhd2wITbmqf2I0ystIUpn8MMRXrcaBzj0h7qewQ0w_5XLvk2TckEpPXWasnqvW0tA8Qmz8YU230r23hJ4a7LvZ9uu6XY94-Vb6go11TH8En0zO_vzi-gu9j8KX9GQ6w28TVGXYC25BLROdKRwKeZ659vT_aL1Qw_T16iBYPhFqGn5tY6xaW2nEr6BEMOksdEk6o8miQdkTIXvMqUDlMrFz9Jg-GbGsJu8QPQBugYKWIs80d892y5MMkX4KDrirBtVOoUWJA8abj8EiAo6vaJlw64a-kke-n9LzMtlPsRf2eQehY0EruKnulsmCIBz3FGJr9ja6AFdkDeggkGG-ghJFYNr9b9vbO1sbbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل، اسرائیل کاتز:
محور اخوان المسلمین محوری است که با گذشت زمان می‌تواند به همان اندازه خطرناک شود. ترکیه و قطر بخشی از آن محور هستند.
🔴
اخوان المسلمین نه تنها علیه اسرائیل عمل می‌کند، بلکه برای سرنگونی رئیس‌جمهور السیسی در مصر و پادشاه عبدالله در اردن نیز تلاش می‌کند.
🔴
این همان چیزی است که ما می‌بینیم. شاید ایالات متحده آن را متفاوت ببیند، اما ما مسئول منافع خودمان هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138119" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کاتز ، وزیر جنگ اسرائیل: امپراتوری بزرگ ایران که مغرور بود و به دنبال نابودی اسرائیل بود، فروپاشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/138118" target="_blank">📅 13:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkJfslyxquzvdW2sJ7fGMDMnlXeQFkk5Cdp4NCZlRE3JflXrB7FVyl49_4UIpED1fYRF1iRwjp5Ae_bLAcKt8W6-HGy_ANyPFqU5Wa8SbnyiN6-wVn1OY-N9t9KFtDzvQZowgo3isAgHAahSbVAlJFFJP1sL3lVBzrLjUu00ABBaQErVQ974e3hHT9quyfc7ZrTMvzogOVyOAq0cANpO8_07v2HjSbbxLOi2INPW8ZZvUSwkIDtJ6g5cagYnVT8n7AQU3YY7vxdAJjo8nKL7C6JzfyXFhC5hCikAvbHrhZ6oppG7szcfl0Jcjbf5ynambFEKW6SvKZQ-yqZ9XgkveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست ‌وزیر عراق عازم ترکیه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138117" target="_blank">📅 13:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
کاتز، وزیر دفاع اسرائیل: ما دو بار به ایران حمله کردیم و برای بار سوم هم آماده‌ایم
🔴
ارتش اسرائیل هم دستور گرفته و آماده‌ست که حتی به‌تنهایی به ایران حمله کنه
🔴
البته الان تنها نیستیم و آمریکا هم کنار ماست، باید دید واشنگتن دوباره وارد عملیات می‌شه یا از…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138116" target="_blank">📅 13:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کاخ کرملین:حمله اوکراینی به یک کشتی ایرانی، به منزله حمله به ایران تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/138115" target="_blank">📅 13:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
رئیس کمیسیون انرژی اتاق بازرگانی: در پی حوادثی که در جنگ ۴۰ روزه برای کشور رخ داد، روزانه بیش از ۴۵۰ میلیون متر مکعب کسری گاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138114" target="_blank">📅 13:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ما به شدت خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138113" target="_blank">📅 13:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نتانیاهو و ترامپ امشب ساعت ۱۸:۰۰ دیدار خواهند کرد. این دیدار بدون حضور خبرنگاران برگزار می‌شود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138112" target="_blank">📅 13:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فایننشال تایمز ادعا کرد؛ چرخش ژئوپلیتیک بن زاید؛ امارات در حال احیای کانال‌های دیپلماتیک و اقتصادی با ایران است
🔴
ابوظبی به دنبال تنش‌زدایی با تهران است
🔴
گفت‌وگوی مستقیم سران امارات و ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/138111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: ما به شدت خواهان حمله به تأسیسات انرژی ایران هستیم، اما ایالات متحده در حال حاضر اجازه این کار را نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138110" target="_blank">📅 13:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwOJz1ABdlswHBb0PCdqVW7ZpLsIOWh_KJ5Q_MdR9YaTXdgimTDXdqd_0B4FOmlOIQVtD1WehvIAWwR5JPH1faTcSub5WJaYHvskkv8z1mSWdSmw_vwGGR0bpw0Kw6uI2aEWCuH5bt9Thay7gRWT81bx3ba0o7Y43bAdKPmqbkfa1mkoQCNN1qhZwqXTXOPM9K7XqrClUilCMDmTj285EjzPbTOjc_mNUe2nVOhe9psShjqjwUzC0OCKXg7kdXLiPCu-l-dFtoTscberj569ESK0jyUmU-WSvshnJ7W-asNeezAgjOofjGi18U-reCGaYwVm4Mi5NJuStC-O3Fh5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ هکتار از مراتع و جنگل‌های بخش مرکزی سردشت در آذربایجان غربی طعمه حریق شد که پس از پنج ساعت تلاش، این آتش مهار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138109" target="_blank">📅 12:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
طبق گزارش شبکه i24، عراق در روزهای گذشته، ۲۰ پهپاد به سمت اسرائیل، اردن و عربستان سعودی پرتاب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138108" target="_blank">📅 12:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۵۷ هزار واحدی به ۵ میلیون و ۱۰۹ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/138107" target="_blank">📅 12:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84bdc994db.mp4?token=RuJBtulgomzXY6DBJXA6F0rT6pi1uC58Q4rN0Rn_gyUeI_0ZXbXl5fNtbNMt_QXMLHrGVtf24U85LHAKLaxZmURDWnxui67CaYa0QJtLDYXZ4NUp_67rxd33DLEkAfq_QboyYXJV4n5f63edlUd4-cTb0K1_4EeaJ5ZFTC0Tcx0RQx7NQ1JUg45ER3RauC68nZ4185apQe4g-QRrx_Ihzj_kp-78kreMq8NuCjzUd2B6D1-4t2HybgGooMbEX-638fqKs14kGlcDySAMAqcM_tJRxkM6aP4qF-9kfm_7qqxrF7_3175kBP1L8txbM49BNjWfqNBPG1UQG2WGw80ukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84bdc994db.mp4?token=RuJBtulgomzXY6DBJXA6F0rT6pi1uC58Q4rN0Rn_gyUeI_0ZXbXl5fNtbNMt_QXMLHrGVtf24U85LHAKLaxZmURDWnxui67CaYa0QJtLDYXZ4NUp_67rxd33DLEkAfq_QboyYXJV4n5f63edlUd4-cTb0K1_4EeaJ5ZFTC0Tcx0RQx7NQ1JUg45ER3RauC68nZ4185apQe4g-QRrx_Ihzj_kp-78kreMq8NuCjzUd2B6D1-4t2HybgGooMbEX-638fqKs14kGlcDySAMAqcM_tJRxkM6aP4qF-9kfm_7qqxrF7_3175kBP1L8txbM49BNjWfqNBPG1UQG2WGw80ukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل، الی کوهن: ما دخالت‌های ترکیه در سوریه را نخواهیم پذیرفت.
🔴
اگر ترکیه پایگاه‌هایی در سوریه ایجاد کند، ما نیز اقدام خواهیم کرد تا پایگاه‌هایی را در داخل خود سوریه ایجاد کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138106" target="_blank">📅 12:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138105">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل، الی کوهن:
عربستان سعودی به صلح با کشور اسرائیل بسیار بیشتر از آنکه ما به صلح با عربستان سعودی نیاز داشته باشیم.
🔴
امروزه، همه کشور اسرائیل را به عنوان قدرتمندترین کشور در خاورمیانه می‌بینند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/138105" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040423a442.mp4?token=UDQupKi4R5YehTsqjk0y6TP6n0Pid0o7dN-n77c0Iaxyb5TlY4PxgXh0y5TN9PZikg73YK8ZVtFF5EXSXuPggrjWp6GJSWa_pij0ZJ4HFzgjyYMbKCbA_XHLNTkeeAdWoBhVlUt3zATMw_jeLi1Le7ISJpNF1z5Fx8Q6FuALELhbnbfaUv-QcaECE0i5i4R2-U0CnIEGQ_yIn2lh33cb35UHDjOaG-yJndxfeA8WMOLGtmalwlvGhCHmnFEJKwvJneV1IWwFHNdc0kf4n9cdiGnQLQFPYeNp-Xss4Yw53NwQqmDQ3EPJU4tYcVq_WvudXQxSYC6Bk0MVlaDB42tAZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040423a442.mp4?token=UDQupKi4R5YehTsqjk0y6TP6n0Pid0o7dN-n77c0Iaxyb5TlY4PxgXh0y5TN9PZikg73YK8ZVtFF5EXSXuPggrjWp6GJSWa_pij0ZJ4HFzgjyYMbKCbA_XHLNTkeeAdWoBhVlUt3zATMw_jeLi1Le7ISJpNF1z5Fx8Q6FuALELhbnbfaUv-QcaECE0i5i4R2-U0CnIEGQ_yIn2lh33cb35UHDjOaG-yJndxfeA8WMOLGtmalwlvGhCHmnFEJKwvJneV1IWwFHNdc0kf4n9cdiGnQLQFPYeNp-Xss4Yw53NwQqmDQ3EPJU4tYcVq_WvudXQxSYC6Bk0MVlaDB42tAZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از زلزله ۷.۱ ریشتری در ژاپن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138103" target="_blank">📅 12:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نایب‌رئیس مجلس: افزایش قیمت بنزین منتفی است/ جابه‌جایی سهمیه در دستور کار دولت قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138102" target="_blank">📅 12:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138101">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
استانداری کرمانشاه اعلام کرد مراکز آموزشی و ادارات این استان، چهارشنبه، ۷ مرداد بخاطر گرمای هوا و مصرف انرژی تعطیل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/138101" target="_blank">📅 12:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138100">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3Y_M-5Pqx_UPKBFrA4vqGc_68v40zJnhe8M8H1dN4N9R-Fql09AgYvyofBBxCnKIyCdQrqiirNdPN9D5A3J3LtT6wXRvlXcqOgq4d9LuCbZnLhxhj6ugfBwedPoiEcCygJ94tozToBzosRGp3YMtv3C2sm0heX-3iNM_0uaysJlTVj8I9Un1cpwPjljELDQxq4iWHghXIt42l968GBWO-9vez8IYsaOQklgD66vpu5hsN8rHU6Sw5MGao4J1CMDkaWMODqHYeCx8H6XHctNiPVPyBkUwFJ79hqZSG4Y_sVgOJdI6q-MmtTsWDoPC8gQalBdkM_ic25UBBgQT6gC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی، فعال سیاسی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
‏
🔴
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138100" target="_blank">📅 12:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138099">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
یک‌چهارم نفت دنیا قطع شد
🔴
براساس گزارش روزنامۀ وال‌استریت ژورنال، حملات نیروهای مسلح یمن به کشتی‌های مرتبط با عربستان در دریای سرخ و تنگۀ باب‌المندب، ریاض را با یک معضل راهبردی جدی مواجه کرده و مسیر جایگزینی که برای دور زدن تنگه هرمز ایجاد کرده بود را نیز با تهدید روبه‌رو ساخته است.
🔴
وال‌استریت ژورنال می‌نویسد اختلال همزمان در دو آبراه استراتژیک تنگه هرمز (۲۰ درصد) و باب‌المندب (۵ درصد)، حدود یک‌چهارم (۲۵ درصد) از عرضۀ نفت خام جهان را مختل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138099" target="_blank">📅 12:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138098">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-LCK59m-C5HtecA81gACXJvgL4dj2WjmONulkrJLn2kV99tGwbDoZfra18Q-XvN7cNZqxNUHSN_5dZq_TR45z2jCZnRF7JDjntQOcXNkc1LCCO2f60H3TKPhqF6nns6-7MSBhpWzX3Wuuvzj7WVWIuFvtcZ3uDea0YoWQmxqVXC_9WBw26xLSz5_Xu6pBUJUjqHoMd_Sb5ZxOWurdUy4sdUOXDCdhOzHfuFwE_FP8p3UCAAX6ImbVb-5cqfaVQgIqwDtv8Rz-2Bovoox8KsR6MwzT4OYtgKnAqIEYZ_9dn0f1UVLbQhDfn1FQnQx6vLIPDaRLmNRZoDQdSfa49lig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع روسی: اوکراین تا پاییز امسال توان شلیک موشک بالستیک جدید به مسکو را خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/138098" target="_blank">📅 12:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138097">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
صبح امروز جلسه شورای هماهنگی مجلس شورای اسلامی با حضور قالیباف، اعضای هیئت رئیسه و رؤسای کمیسیون‌های تخصصی تشکیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/138097" target="_blank">📅 12:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138093">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=j9-eGtH_mvhrA41FlnyqOVQ7xjUMbeSkO488vAYlTLHtv8aSe7_divK3sDVAAZToX-Gefdd6lpWkTsyKIPTvmqeuqdH_xXTqo7Q4eCEC_KZ-FXpA-7GQa4wnLWWr_1fV55XIvcVSfjebmG25mVHFIo8lUFlSHVcnBYU8KgL6kyLEGM_hoe45Kp510HuspKE9gYpIi3oq-brjHpC8poKPq61y9LFyQbJL4acCCFvqfoW2JmD8sc3p4mNJLeoX2ln9jmEo3CJou2gPZZjxYEXcHG_XGrJ3mlvyYmIM6VzbkDcdo3gYgiLHFrqJ6D6WnvpwPP-xYMedMT-fc5WS57ejFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d321b0eb.mp4?token=j9-eGtH_mvhrA41FlnyqOVQ7xjUMbeSkO488vAYlTLHtv8aSe7_divK3sDVAAZToX-Gefdd6lpWkTsyKIPTvmqeuqdH_xXTqo7Q4eCEC_KZ-FXpA-7GQa4wnLWWr_1fV55XIvcVSfjebmG25mVHFIo8lUFlSHVcnBYU8KgL6kyLEGM_hoe45Kp510HuspKE9gYpIi3oq-brjHpC8poKPq61y9LFyQbJL4acCCFvqfoW2JmD8sc3p4mNJLeoX2ln9jmEo3CJou2gPZZjxYEXcHG_XGrJ3mlvyYmIM6VzbkDcdo3gYgiLHFrqJ6D6WnvpwPP-xYMedMT-fc5WS57ejFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب بیش از ۴۰۰ پهپاد اوکراینی مناطقی در مسکو را هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138093" target="_blank">📅 12:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138092">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رم میزبان مذاکرات جدید لبنان و اسرائیل تحت نظارت آمریکا
🔴
قرار است ظرف روزهای آینده، پایتخت ایتالیا میزبان دور جدیدی از مذاکرات میان لبنان و اسرائیل با نظارت آمریکا برای بررسی عقب‌نشینی اسرائیل و اختلافات مرزی در جنوب لبنان باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138092" target="_blank">📅 12:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138091">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c84fdbd6c.mp4?token=l0akeusgIbO9Z8QwXMbgvkUfyWLIgkUf-gO4ttMkAhyGu-VewVkTCq5ajkXou85N_yHSvZ2TPYq5SE7XkyQ89M8-sd0LzpPzWyOsf-SWtSw-QPggNXX3VbV2IeS9RRYX1LBsobAl7g8-QqE0ERx-8IZulED2Bv5ecvXi9Mr63ltahcXfGniGEaTqESN-cdVb8vwkvUwWNDoslPcFbBDpy084be_Lxt8jeXKQ6TsAcjzqIwqYlTFJHW2CiFBYgQsC8c2D1s5CWFs53YiTbc-pChmeDt7PTi7QQHnbk0-AZA33rCUSgCasZgnzyMCYoC0Ew6lU7ITp0ZbTNIPHkNMdDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c84fdbd6c.mp4?token=l0akeusgIbO9Z8QwXMbgvkUfyWLIgkUf-gO4ttMkAhyGu-VewVkTCq5ajkXou85N_yHSvZ2TPYq5SE7XkyQ89M8-sd0LzpPzWyOsf-SWtSw-QPggNXX3VbV2IeS9RRYX1LBsobAl7g8-QqE0ERx-8IZulED2Bv5ecvXi9Mr63ltahcXfGniGEaTqESN-cdVb8vwkvUwWNDoslPcFbBDpy084be_Lxt8jeXKQ6TsAcjzqIwqYlTFJHW2CiFBYgQsC8c2D1s5CWFs53YiTbc-pChmeDt7PTi7QQHnbk0-AZA33rCUSgCasZgnzyMCYoC0Ew6lU7ITp0ZbTNIPHkNMdDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجرانی: تحریم ما را به سمت تراستی‌ها برد؛ یکی از تالی فسادهای تحریم که به کشور ضربه وارد کرد
🔴
تلاش تیم دیپلماسی ما در امتداد میدان برای رفع تحریم‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/138091" target="_blank">📅 11:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138090">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
مهاجرانی، سخنگوی دولت: هواپیمایی که به‌تازگی خریداری شده بود در فرودگاه بوشهر مورد اصابت موشک قرار گرفت و تنها قسمتی از دم آن باقی ماند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138090" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138089">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2bb5e80a.mp4?token=IqQi2OXTycT-e1PAoIPslj9ilE57AjQ_dP91UyeC8EEnODKFoRAc8bY6g5h1qS4LpZkCn-AEAXaMJeCnWIvbmGkY7frjQc7XJPKb7AgUqAF_rz8q-gAIdFaYloDyLLcNSrDm7V0O-MR0AoWtr_noBwsrp-9gIoK8RWvJXfSTPnFrIT0R7fHxGsPM_YYJd7fs-YohUgIL_B3u3Wz-EWexJEPN3zi5PoiyunMSqr0ixne4CgoxJR7SJdwPowviLbxVrPBfgIOnWXpDEcpzw6q-DuBlJt5nyv37UxleUayAWR9upx4-0H460eK7TtEGTe7RtBTSfGgnUpIgqb1QCM9eXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2bb5e80a.mp4?token=IqQi2OXTycT-e1PAoIPslj9ilE57AjQ_dP91UyeC8EEnODKFoRAc8bY6g5h1qS4LpZkCn-AEAXaMJeCnWIvbmGkY7frjQc7XJPKb7AgUqAF_rz8q-gAIdFaYloDyLLcNSrDm7V0O-MR0AoWtr_noBwsrp-9gIoK8RWvJXfSTPnFrIT0R7fHxGsPM_YYJd7fs-YohUgIL_B3u3Wz-EWexJEPN3zi5PoiyunMSqr0ixne4CgoxJR7SJdwPowviLbxVrPBfgIOnWXpDEcpzw6q-DuBlJt5nyv37UxleUayAWR9upx4-0H460eK7TtEGTe7RtBTSfGgnUpIgqb1QCM9eXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کپلر: طبق داده های مسیر یابی تردد کشتی‌ها از تنگه باب المندب در روز دوشنبه به 28 کشتی افزایش یافته که بالاترین سطح در چهار روز گذشته است، در حالی که تردد از تنگه هرمز همچنان پایین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/138089" target="_blank">📅 11:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138088">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
الجزیره به نقل از رسانه‌های آمریکایی و انگلیسی: سفر فعلی نتانیاهو به آمریکا، حساس‌ترین سفر از زمان آغاز جنگ علیه ایران است
🔴
ممکن است که تل‌آویو در جریان این سفر، خود را ملزم به ارائه امتیازاتی در چندین پرونده منطقه‌ای بداند
🔴
اولویت‌های ترامپ و نتانیاهو دیگر به اندازه ابتدای جنگ، با یکدیگر هم‌خوانی ندارد
🔴
بزرگترین چالش پیش روی نخست‌وزیر اسرائیل، تغییر عمیقی است که در نگاه آمریکایی‌ها به اسرائیل ایجاد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138088" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138087">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رویترز: عمان سازوکار جدیدی برای مدیریت هرمز پیشنهاد داده است
🔴
رویترز به نقل از یک منبع خلیج فارس مدعی شد: عمان پیشنهادی برای سازوکار منطقه‌ای مشترک برای مدیریت تنگه هرمز با هزینه‌های داوطلبانه به ایران ارائه کرده است.
🔴
براساس این پیشنهاد، ایران به تنهایی کنترل آبراه حیاتی را اعمال نخواهد کرد.
🔴
این پیشنهاد برگرفته از تنگه مالاکاست؛ کسانی که از این تنگه استفاده می‌کنند داوطلبانه به ناوبری، حفاظت از محیط زیست، جستجو و نجات کمک می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138087" target="_blank">📅 11:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138086">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
مهاجرانی: مرکز هواشناسی بوشهر چیزی از آن باقی نمانده است
🔴
کسب‌وکار های گردشگری به شدت آسیب دیدند
🔴
فرودگاه بوشهر به هیچ عنوان قابل استفاده نیست و باید از اول ساخته بشود
🔴
۱۲ دستگاه پل و ۲ دستگاه تونل آسیب دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138086" target="_blank">📅 11:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138085">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
کانال 12 اسرائیلی در پوشش خبرهای سفر نتانیاهو به آمریکا، از برنامه ویژه تیم او برای اعلام خطوط قرمز اسرائیلی در قبال مذاکرات با ایران خبر داده است.
🔴
در این گزارش ادعا شده است که یکی از ابتدایی‌ترین خطوط قرمز، وجود هر گونه اورانیوم غنی‌شده در ایران است.
🔴
ارتش اسرائیلی به آماده‌باش جنگی سطح قبل از درگیری درآمده است.
🔴
کارشناسان اسرائیلی، ادعای نگرانی از کمبود و مشکلات ذخایر موشک‌های سیستم‌های دفاع هوایی در منطقه برای توجیه توقف حملات آمریکا را مضحک می‌دانند و از چنین کمبودی بی اطلاع و از ادعای درباره آن شگفت‌زده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138085" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138084">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
روزنامه «نیویورک‌پست» گزارش داد، بنیامین نتانیاهو در جریان سفر به واشینگتن قرار است اطلاعات و ارزیابی‌های امنیتی مربوط به سایت ایرانی «کوه کلنگ» را به دونالد ترامپ ارائه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/138084" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oHgfExZehoAdmroZmudyv8gfplerZXG__INEftx4KUD0XW_4vEhREgtMdVY6Vxyk7nhOt9fEWE8yM7jt2MbdUMWLIibe2F9XlY3q2os2PNkGt2UH05MgjmNWa4b24PQRCVZnaauudvXyeULlmULfVkdyUbalhLYTYuGBxo68n2RZJXq4M4p0bhhHw_eTVMZleW_xlHNYVrBHkmSvpONQd6qpEvP12oi5K_HS_Y56IMEya_EF4eh2j4AR8lRBnGiG-4Zw9bSRq8bC5miMx4f0dSGqL3iArIXpaCvMITT6jOPYdolVCr4aLAHf4eeETrGuo6SZkoCA6WsF8bLJbg_ylQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/IN3aqCkIbRnl1am7Oiyq-LPKhs_3d34SxeV-KNNVMkXTYVAG2vhL4KU8RjcgwACEq_XM3tLBWBDSKbc90prqrLcE7ygIusqvFAx9oGRF680KsszGiu0gtLATogA33VcRgOl3ZFY3Pz3Eq1dpSl1qd9V_GCpwLX857HebUldR8IPucya8PhNsluYwMOZ_Ipr9qAylBa1TNgOEbQTMP-rsRuU7fdnSQ5sIgnIL02oOLq4VfEB1Srvb_NMehKz4ZZD31WPC6hYbWzI5_GwTr8PQzm5vjH17t3l7ogetS4mZjw_oWT_dqse9_zWKuC7Py8t2RIIFo6RVEIZoLfuHpf-Yog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
فووری: کریستیانو رونالدو قراره به عنوان تهیه کننده و بازیگر وارد دنیای سریال‌ها بشه!
طبق گزارش‌ها، رونالدو توی سریال فوتبالی «
Day 1s
» که با همکاری «
متیو وان
»، کارگردان فیلم‌های Kingsman ساخته می‌شه، حضور داره.
داستان این سریال درباره زندگی یه ایجنت معروف فوتباله و «
دیمین لوئیس
»، بازیگر سرشناس انگلیسی و ستاره سریال‌های "Homeland و "Billions"، نقش اصلی اون رو بازی می‌کنه.
«
تیری آنری
» و رپر معروف «
Dave
» هم قراره توی این پروژه حضور داشته باشن.
جالب اینجاست که خود کریستیانو رونالدو هم علاوه بر
تهیه‌کنندگی
، قراره توی این سریال
نقش‌آفرینی
کنه.
فیلم‌ برداری این سریال هم الان توی لندن در حال انجامه و قراره به زودی منتشر بشه.
@AloSport</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138082" target="_blank">📅 11:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab6c540c9.mp4?token=E4FxLigNOsyu0dTSSVmxhioMETk5Gsg06dzRPny6dZk_aanNI3Q0TOCtFxY1RZSq45ZKY4b2rEKqWPnDOo180GmSuEuh1MKRQzf8JlQ73ze9UV1MedmFwAsuDEOktf3sb_IG11ABC1fBWXB8U3VyzG2lqV2onc4Gfih4ELnI8Pe6NC3LGYbc7g1ONiLYWhXzxTX4G2NGtKAA-f_jREwWQ0dg6y0k0xJf6PV9qB_bhpOvOhVMvRowmPBomgMftXnxsyMC1UQyFNniZfO8X9xssQBBT4SB59eamWjOXBdUk-J-TRBaZqj8UaJKSFOSF3M1khgurulfC_qsJM27d8BBvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab6c540c9.mp4?token=E4FxLigNOsyu0dTSSVmxhioMETk5Gsg06dzRPny6dZk_aanNI3Q0TOCtFxY1RZSq45ZKY4b2rEKqWPnDOo180GmSuEuh1MKRQzf8JlQ73ze9UV1MedmFwAsuDEOktf3sb_IG11ABC1fBWXB8U3VyzG2lqV2onc4Gfih4ELnI8Pe6NC3LGYbc7g1ONiLYWhXzxTX4G2NGtKAA-f_jREwWQ0dg6y0k0xJf6PV9qB_bhpOvOhVMvRowmPBomgMftXnxsyMC1UQyFNniZfO8X9xssQBBT4SB59eamWjOXBdUk-J-TRBaZqj8UaJKSFOSF3M1khgurulfC_qsJM27d8BBvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بهمن ننگین 57 حمله عنقلابیون به پادگان ارتش و سوزاندن سربازان و کشتن افسران ارتش.
🔴
اونموقع این اغتشاش نبود؟ اموال عمومی نبود؟
🤔
از شما حرام زاده های عرزشی دروغگو به عنوان بیناموس هایی تو تاریخ یاد میشه که حشدالشعبی، فاطمیون، حزب الله، حماس رو به وطنتون راه دادید تا به ناموستون رسیدگی کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/138081" target="_blank">📅 11:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ادعای «العربی الجدید» به نقل از منبع آگاه ایرانی:
🔴
تحرکات دیپلماتیک برای کاهش تنش در منطقه و دستیابی به راه‌حل دیپلماتیک در روزهای اخیر شتاب بیشتری گرفته است.
🔴
در دو هفته گذشته، پیشنهادهایی از سوی میانجی‌ها بین دو طرف مبادله شده، اما هنوز به پیشرفت چشمگیری منجر نشده است.
🔴
تبادل پیام‌ها بین تهران و واشنگتن به طور مستمر و بدون وقفه و از طریق بیش از یک کانال ادامه دارد.
🔴
تهران به واشنگتن ابلاغ کرده است که پیش از پایان محاصره دریایی آمریکا و بازگشت این کشور به اجرای تعهداتش، اقدامی برای بازگشایی تنگه هرمز انجام نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/138080" target="_blank">📅 11:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrnKP_hSVKBJqvfxuoWLUIHKYZYJkQ2Z1AfuRiO-SKFPzcjrLrswhA3gKX_VllJ4DxostEn7byaP2ToSQJX9VWhAUfod_MtHinLp5IqJdl7FTR4nO00uP5KOCyoaRSyTtx0MZJaxkWV2vM7jzntRZ8m0VRTuq4WETkNsNX313nEDKJdrync6nUa-GP07Ot97N1QOhXvgc1zI1rr9uroZgTfx-cSUH-occp-ZgX88Be_47CaZepmHN92XsrzsLJ9JMLPX0d8Q7Q2qiipHC1_ByksgEDbdKwcA6HWH1kMXdlhXLrXt4g1YzNy7eqNG6GeCLQjXKcrR9N2WsHqPOtVnNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وقوع زلزله۷.۱ ریشتری در ژاپن
🔴
زمین لرزه ای به بزرگی ۷.۱ ریشتر جزیره کیوشو در ژاپن را لرزاند.
🔴
در این رابطه هشدار سونامی صادر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/138079" target="_blank">📅 11:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138077">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gXVxN7bUvi8FYi-ZeCJc6Di_Kf6J_PqkHfpXBa6Liow1ViixNj91cPPJFtyDVf7EP6_TtgyAJqlOjUbKGJbz-xZQmGhuBtOMbxmVQLXqDtcRPa0YqNBCvqFcjmQBAzO6asVlEE5R4ABJdkNkCw-sTepAXbgxrAWtbwVUO9TLIday4Y2tw0IHInSQ93EpgVHqL7NS_i8FZWk_wWqxud0xRr64I2kPY2LxMgOHHiqID37H2RHgNoHOde17W3AlptwAk2dG9wcfWU0Zr-RAEfQO7MjnzDEPxsyfTy7ASVIyeVc7IPBOp4bdPYncIzQGEwcrO-hfd2p26p5YVqWKxff5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pBTcixgJCQlE9GB9Q8mDQR068HA9ehiXQAuCO9Zd-MyB7bOm27FbdrtKiZlxCs0Qbbh-exc99EwlZNR2FOtOi_I1ud9rUX_x73WIXMEIfzy0ItxOhHU3oLaybrfc-mZPFaUWoIkF82UPwZWV9V7X0gV_irtwAZHGuuT7NLy318WGrVMh_jxsEttrESVR2mg2a4vk8DqRAwb2dWy-iUF-ofX-lf7WG0rlnGiDJRs71vIuWvbjF2W5Z_O6xjpbschQeIu5FUD0G3O_THBSppC99KtOeqVKMNVciYQvOn67v4_pTVHyHSViEW05_jZ3oq2VLIpx8XEqxInqCSD5Jk8a3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛ زلنسکی درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138077" target="_blank">📅 11:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138076">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de200d8a.mp4?token=Nr4_0HOc9mxzdvycDq140LnfNxnaRYhQBH6R7R-hA8oY3VMBPJrXDXG37Lt8JAjt8LI8zc3FGlavmWK3uUHyeS4y8M4zBOoAJ7HE6GY7NUblkW5tz8Fq_R93G2Sx1smE6NaY2_Vr_O70pSx44Fb0Mv6Bq38E69ReMIWR6LbSQcFcWvNwzrbA_Gw3U2IRMw7oyFDeqOMNukPKx4uZsfVZR1viaMlZYO5OT00FGbiUwugrI6mw-X0d_z01NAB8xwnPI1mKcq0t7lTeeK5ylmSAW8522u-fbHbTNumQa2TjC02u1US8Y77TzFbVAWjralEplX_r2AyhoWxUUg7J0Ftsgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de200d8a.mp4?token=Nr4_0HOc9mxzdvycDq140LnfNxnaRYhQBH6R7R-hA8oY3VMBPJrXDXG37Lt8JAjt8LI8zc3FGlavmWK3uUHyeS4y8M4zBOoAJ7HE6GY7NUblkW5tz8Fq_R93G2Sx1smE6NaY2_Vr_O70pSx44Fb0Mv6Bq38E69ReMIWR6LbSQcFcWvNwzrbA_Gw3U2IRMw7oyFDeqOMNukPKx4uZsfVZR1viaMlZYO5OT00FGbiUwugrI6mw-X0d_z01NAB8xwnPI1mKcq0t7lTeeK5ylmSAW8522u-fbHbTNumQa2TjC02u1US8Y77TzFbVAWjralEplX_r2AyhoWxUUg7J0Ftsgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برشی از یک مناظره/جمهوری اسلامی تنها با زور اسلحه و کشتار باقی مانده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/138076" target="_blank">📅 11:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138075">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=VwPQu2r23XTFUBfEZEJauEgcQ4u3wm_MHtptKTbbAKLrGR1D6qtAKorherpytxBO9EAfvrRraUdXP5hUqKXMH94G_-VvGGJA8fj8QziZS9FLNEdYhO9_mfmw8KuKs8CSN37sEFFdvrNGvPfSLFpG6S3yn9BEPf3uX1JjLtdS3Nz5uHj3n5uEK1aN-vmB6f4NWWtQmtyzse2a_WsxnNYrk2dEwTKjZIHytPFr0-A-Z00HLepyQrzzF0JQTdq1BzOiV4p2czVhNFRFLbMtFRH-Ox21WuGxB13ebXangJ7fYTMNos1JZAMHYflm3GsM8zrr406TLhtGWcbL21A4pSoGVlCggY_MlUJ65x8By7Q4LRaGADyCYq1Us5i7QGzFILod3ifMeEbwSiND3xrsE1He6VvF1vY433kq-YBwvoD2pSi3HwWaaBUxBu6DhbAWbij2SU9vCVEWq7qnZmVd0T59qrQ2XY7eXat_x2cQtaiVYSOT6ymt9KigddGRL157DRoiGZ8fsl717tjo-meQS0cv8zkuXIaKE7CtvGcpIcX9iizQ5K0hhN-34jm3fP0ru2dyhCuaTPAVDeLNIvMY4mzo9Xdm24-bg5Dv0v3UQRwxpPalzmWr7rydYA0X5u6-L9ZMzTBOyO6gex-8vjdO9pCsWjnx23CT1cXLU0-oVrR8NhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=VwPQu2r23XTFUBfEZEJauEgcQ4u3wm_MHtptKTbbAKLrGR1D6qtAKorherpytxBO9EAfvrRraUdXP5hUqKXMH94G_-VvGGJA8fj8QziZS9FLNEdYhO9_mfmw8KuKs8CSN37sEFFdvrNGvPfSLFpG6S3yn9BEPf3uX1JjLtdS3Nz5uHj3n5uEK1aN-vmB6f4NWWtQmtyzse2a_WsxnNYrk2dEwTKjZIHytPFr0-A-Z00HLepyQrzzF0JQTdq1BzOiV4p2czVhNFRFLbMtFRH-Ox21WuGxB13ebXangJ7fYTMNos1JZAMHYflm3GsM8zrr406TLhtGWcbL21A4pSoGVlCggY_MlUJ65x8By7Q4LRaGADyCYq1Us5i7QGzFILod3ifMeEbwSiND3xrsE1He6VvF1vY433kq-YBwvoD2pSi3HwWaaBUxBu6DhbAWbij2SU9vCVEWq7qnZmVd0T59qrQ2XY7eXat_x2cQtaiVYSOT6ymt9KigddGRL157DRoiGZ8fsl717tjo-meQS0cv8zkuXIaKE7CtvGcpIcX9iizQ5K0hhN-34jm3fP0ru2dyhCuaTPAVDeLNIvMY4mzo9Xdm24-bg5Dv0v3UQRwxpPalzmWr7rydYA0X5u6-L9ZMzTBOyO6gex-8vjdO9pCsWjnx23CT1cXLU0-oVrR8NhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری تسنیم روز دوشنبه با انتشار ویدیویی حاوی اطلاعاتی درباره فروشگاه‌های مورد علاقه ملانیا ترامپ، از کسانی که آن‌ها را «آزادی‌خواهان جهان» نامید، خواست بانوی اول ایالات متحده را هنگام مراجعه به این فروشگاه‌ها به قتل برسانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138075" target="_blank">📅 11:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138074">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dec70a1e2.mp4?token=vJYFJhOp5FX2suVy0sYOqKJUpE5w_1w70ZYmZE7i7gTVLP9QnVKeiTtcWMcVh6E1BybQbiwJ-Fn0NgPKVI2zy4FqluNoQIi1Gv7BR3KXFNTZEiwtj0B27Oa4RDcZOmzLkwnJvNBr7SqsGdxBTEONqOcf9QzoCCuf28LnSALhQu0coGmXNzwa4C_sXnXWNAWgRM4tRbMWRf6WUnCxnmeNbnShzLxMhYKnHlO0xs6nxoJuCbtAsmvnoKooNA9QCtYWWEB_aP8JUDcgy4eSS0FtQDhO9UzpiGnbvIzmsSvQWaXrUxXIwbq1yFsv1xp1Sbx2V8yi9JaEjR39ij5r9tGoqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dec70a1e2.mp4?token=vJYFJhOp5FX2suVy0sYOqKJUpE5w_1w70ZYmZE7i7gTVLP9QnVKeiTtcWMcVh6E1BybQbiwJ-Fn0NgPKVI2zy4FqluNoQIi1Gv7BR3KXFNTZEiwtj0B27Oa4RDcZOmzLkwnJvNBr7SqsGdxBTEONqOcf9QzoCCuf28LnSALhQu0coGmXNzwa4C_sXnXWNAWgRM4tRbMWRf6WUnCxnmeNbnShzLxMhYKnHlO0xs6nxoJuCbtAsmvnoKooNA9QCtYWWEB_aP8JUDcgy4eSS0FtQDhO9UzpiGnbvIzmsSvQWaXrUxXIwbq1yFsv1xp1Sbx2V8yi9JaEjR39ij5r9tGoqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدون شرح از یک حجری
🔴
پ.ن: راهکار ساده هست زن سیبیلو نگیرید تا با دیدن اشخاص دیگه مشکل براتون پیش نیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/138074" target="_blank">📅 11:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138073">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
توهین‌های داماد دوزاری علیرضا پناهیان به آیت الله سیستانی مرجع اعلم شیعیان جهان!
🔴
پ.ن: آیت الله سیستانی بزرگترین مرجع ۲ دهه اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/138073" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138072">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0JBF-SWymhEYVEG6riYkO0UJ6EKHmvOHeF7wLCBocaejsbdwb2HlJ_cD9xC8EnIQ46XVEuM5Op-HefggEetYtZKlLOEcW_wHg3AFM4mI-KF8448HCbUCxpc519UtWzGf8WsfzNC6kVXdKAuk0CL7eM1kdYahkmujrRg4gesqH0VDuXXgAaDzrwVI8ds1DjGOREJZqgBs2rU8ZGkMurioer0FrLRXcColZjA6h9HHRkg--2WcoWJSEwSNriuFEyuBCW5bRsFYR4i2wb1J4j9SQvIia7MA8ITlW5XIwKlO6LupGYxStZ2YmpVsjvMfy0kb-c5XWoMcWi-nEJMyDe8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل به جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/138072" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138071">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a635b8a91.mp4?token=ZRqzEZePQ_hgeH-6u2GseBXvoqtiac7is8iVy1MC044eldbKIZlIQTgUZ9OCB29e3_D030POXBjXA_rnhwZV0jvz1ntY5FKtk7gGsKQNvaKYwHFZ6K6p1vafVW1UtunkenbfrRAyJxeLC9YRGDSEgQD9_PA8FS3_f3SnE7141PEuBIC8wqqdQ2lTaAwf5KgjhTz8b9T4ieyWXsDKODWEWZqgpyQ_mf6ckyhil6mAjRvDVgdVzl5T4CgsRcaHfPTr_1WxHmNmIIqAlt76du1SvXZrg-57CuGCRIfBtZNAa5D9-0JruUDqmSqO2AzvlUIXOxDGuQXG49EnVr54pyBjDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a635b8a91.mp4?token=ZRqzEZePQ_hgeH-6u2GseBXvoqtiac7is8iVy1MC044eldbKIZlIQTgUZ9OCB29e3_D030POXBjXA_rnhwZV0jvz1ntY5FKtk7gGsKQNvaKYwHFZ6K6p1vafVW1UtunkenbfrRAyJxeLC9YRGDSEgQD9_PA8FS3_f3SnE7141PEuBIC8wqqdQ2lTaAwf5KgjhTz8b9T4ieyWXsDKODWEWZqgpyQ_mf6ckyhil6mAjRvDVgdVzl5T4CgsRcaHfPTr_1WxHmNmIIqAlt76du1SvXZrg-57CuGCRIfBtZNAa5D9-0JruUDqmSqO2AzvlUIXOxDGuQXG49EnVr54pyBjDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت: قیمت بنزین سهمیه‌ای تغییر نمی‌کند/ هیچ تصمیمی برای افزایش قیمت بنزین غیرسهمیه‌ای اتخاذ نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138071" target="_blank">📅 10:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138070">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iBjSuA4mtTu4hJ2j-jecRfck71BU0HliIcvy1tsroA9Xz4VXl2GGAayAzYsFsmVpptnDkOk0TImze5ybmp8Li8fGEK4nQsmwuSU42PUnNkre_Imjh4pSfXNEfUFkkpKmx2KUIS47YDJE-fc0zvXZu2t65PQhZDyyAzE_yCbBLCKDIXMrwTX_KhD0PMX0L18Sfx3aezr4Nq-N7jz5-MyvOgNNoCrU5K2IBWEfiPPPq3xmEJuI5wqAfpa69UIjqi8Nb7dSLocCXEvKgL-TrASHORDZho-c8TCx84sesHSCn8CjZ_pfyOKzGljx_GR3JCT2awiGB93hZhoOQfPi4EUYlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
احتمال یک آتش بس پایدار با ایران تا پایان ماه جولای ( تا یکشنبه هفته بعد) با یک جهش بزرگ در پلی مارکت به ۵۵ درصد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138070" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138069">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
سخنگوی دولت: فرودگاه بوشهر از مدار خدمت‌رسانی کاملاً خارج است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138069" target="_blank">📅 10:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138068">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فعال‌سازی سامانه‌های پدافند هوایی در نزدیکی پالایشگاه‌های نفتی بقیق در عربستان سعودی، به دلیل حمله با پهپادها
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/138068" target="_blank">📅 10:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138067">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
حزب‌الله: با حمایت ایران، لبنان رو آزاد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/138067" target="_blank">📅 10:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138066">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is-nCTwDiC1dyJ8CW6fZkT5iYgk_aEQSncYcLcMVERdiIReF3A7QJpoVXnA7SpAy_mTXl2ibihHlsg4-nqkqdzALnohPgqWIGUbgLUT5By9QUqFquuKV3uzVZk4chPdlprhh_NPQFEko_M9wgXDcjHxC93tbUQeeazvQpHEMtzVWCD7x4G5Om-27pAyGTIoOCLYKTplbytq-I88Pbo864hFZwliPrkC5FJf_BDjbCHYKS1v10Tl3AEUlAwSh632zja84TPZHFyCRPpmCb0RyPeRxkH63mirhYlBjGfrQZQlutKnPZIV1hxwLFZIpxlgMhvWei1NyrZ0Rs0T9nwQnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پوتین: شناورهای تندروی ایران در درگیری با آمریکا عملکردی موثر داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/138066" target="_blank">📅 10:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138065">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xi0z2olPOru5T6lzabN-93BsG73kRMm2ueqFbleS_QvmifINHWfL5HIkyEsx-_KkHrf5aelOm1mkISXTjYlOlKA9kYNcKSvnwXKfOTJHNpO7PpLWG4G-HD6pH-pjro5LIntYlKQn36CJClYH8W9mSkBK4JkzNvAovikwUkEyxDfS0Q497RoON2oYjL0LV0WovCHlCt5oLEc_1Zk00oPtJOCcZhfkDlTHb8ZgnPEjHNYJe68qKfiQlAddiJbuDzapZERgMKe0rGpUFSxMe4jdjD2JU5GSBMoCo2R0sHFIW6uQFK4Rw933odv0QpHsiZ0F6UH_qkD1yn9aKt6nGOFxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش مارک لوین به اعدام و سرکوب مردم در اصفهان:
🔴
با این نازی‌ها مذاکره نکنید. مردم رو مسلح کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/138065" target="_blank">📅 10:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138064">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
فرمانداری امیریه : دلیل انفجارهای امروز امیدیه انهدام مهمات عمل نکرده‌است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/138064" target="_blank">📅 10:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138063">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سفیر ایران در روسیه با اشاره به هماهنگی مستمر تهران و مسکو در حوزه‌های امنیتی و دفاعی، از تداوم تماس میان نهادهای مسئول دو کشور درباره حمله اوکراین به یک کشتی تجاری ایرانی در دریای خزر خبر داد و بر ادامه همکاری‌های راهبردی ایران و روسیه تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138063" target="_blank">📅 10:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138062">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وال استریت ژورنال: هدف از مذاکرات ایران و عمان، توافق بر سر مسیری در تنگه هرمز است که کشتی‌ها بتوانند از آن عبور کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138062" target="_blank">📅 10:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138061">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
همشهری: ۱۵۵ نماینده در نامه‌ای خواستار اجرای قانون برای جلوگیری از رشد بی حجابی شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138061" target="_blank">📅 10:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138060">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N00bbxHiaGk6JOYkPD0FU3brdMwI8imTA9zm23NGPMJx1mnPtUxjZzfbHE_bVAHd6kBOTwyMqfmGIBSgCWk6VRf5Uu-Nzhuee7bK_PadeFrdYVPXTnvfqLF14pd2YToyOPZdTa5RcqNW2S4MOVIlniqxS1p_hc9otQwWXtouCpRDhnMxD6FonQs5IDC0077L4VpdA1sniU_50vnkNv9093gd-_Ig3Vu_hq3cIj23xlsD8vkxdNgNP0syIx4M0XnkDIeGnlGT0wxDYf9-iQn6g15qwEFOpJj4MPr2JOZ8erAOrqV4X9CqfFjl-Gh0-itpWlXA4MEy8BGreqiy-MWQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش وال استریت ژورنال: دونالد ترامپ، رئیس جمهور آمریکا به طور فزاینده‌ای در مورد چشم‌انداز اوکراین در جنگ علیه روسیه خوش‌بین شده است در حالی که پیش از این به مدت بیش از یک
سال به مشاوران خود گفته بود که کی‌یف در این جنگ شکست خواهد خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/138060" target="_blank">📅 09:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام ارشد کاخ سفید گزارش داد که دونالد ترامپ امروز میزبان بنیامین نتانیاهو خواهد بود و دو طرف درباره جنگ با ایران گفت‌وگو خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138059" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
کیهان: صحبت از «مذاکره» و «حل بحران از طریق گفت‌و‌گو»، اگر خوش‌خیالی نباشد، ساده‌اندیشی محض است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138058" target="_blank">📅 09:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138057">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وال استریت ژورنال: مرگ لیندسی گراهام و مشکلات جدید اسرائیل
🔴
مرگ لیندسی گراهام، اسرائیل را با مشکلی بزرگ‌تری در آمریکا مواجه می‌کند، زیرا واسطه‌ ماهری مانند او، به هموار کردن اختلافات ترامپ و نتانیاهو درباره ایران کمک می‌کرد.
🔴
جایگاه اسرائیل در میان دموکرات‌ها و جمهوری‌خواهان در حال افول است و دیگر کسی مانند لیندسی گراهام با آن وزن سیاسی که دوست نادر اسرائیل باشد، وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/138057" target="_blank">📅 09:27 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
