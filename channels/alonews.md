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
<img src="https://cdn4.telesco.pe/file/Q5yFJA0fRnTH-Y54-P2Dc00ivjnLrv7qktmKOANYfMwVCFpu5VkoiaHO7eDt6BXTWB6xOaFoV4A-veg0J3sU3yP0PlGB4PaKVayawmCxalVPGvNTJisykb6oBrWaag1bvWZHBIJpEPkvmOQH8wf8vqewcowDZIc6VqcgjSwINa_QutZgtTSA3nk4p9G30QY5w4k1O-8FLUpD1IpGFdD4bk77DY8P7q-rpH_xjfVaVLHIfL2YTX2d3bUuSaqPcsfzIbyjAEVZWV5t4Z_NvI7gIPJ9WEmjQ0CA1UKR6vBZXMUQUBAHyqWLNzHO3Nb4eiCVqHXby2P1fPLHTj6B6pGXCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-149176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان راهبردی و ترابری C-17 آمریکا به سمت خاورمیانه منتقل شده‌اند و چند فروند از این هواپیماها در اسرائیل فرود آمده‌اند.
🔴
این تحرکات در حالی انجام می‌شود که یک پل هوایی جدید آمریکا در منطقه در حال شکل‌گیری است و هم‌زمان گمانه‌زنی‌ها درباره احتمال حمله گسترده آمریکا به ایران افزایش یافته است.
🔴
این تحولات پس از تهدید ترامپ در سازمان ملل درباره «نابودی کامل ایران» و در شرایطی رخ می‌دهد که ایران در بالاترین سطح آماده‌باش قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/alonews/149176" target="_blank">📅 19:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uulrlvoI8IBbkw25OjhhdPLxW-kNR_Qtye79qOZk4QHuVCu1vHv9t3fIXW2J2cI3xYLmVqQcMrQvVawd-eZyRTOPKqzwV4uVRtlBwBXDvZGvQC_nRsGf5Ym3PsUOemQ7ex39YTC27cowhYC4eUCMWZxAUpAJA816mSHyl2azdnTBmfSpzm7xmCIKGd9v8mnD1eeOuPNOYEWvSU7038Es5lHxo9BUomVWp2RTnvQH5Xs3Gi_N2Ev3ND7vahgvl4PEVvdtqHi9PookeMxPGVVTAAudbzeDDmPuq9wxmNYIqlppoJAMk9ecxKoe2cOPNff33vCrgW--2zdhw44Pd2ksrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان، رئیس‌جمهور ایران، قرار است امروز ساعت ۶ عصر به وقت شرقی آمریکا در گفت‌وگویی با «برت بایر»، مجری شبکه فاکس نیوز، مصاحبه کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/149175" target="_blank">📅 19:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aa9xzHChUQL37ftE7qcK0Eg19cbPgX1JNmuqWRuj8rE0_uI8496pBwkjpMc3dc8fpy90gLyD81L0YyT_HWjr1xFl9h01LEcNvMCLtuiypKMqnNbhysQc4rLe9XAjfb-C_BaNg_T_wlvJQEzTGmLjBxdApm6g_S9KqXH4l-V8Hbn3t2fdsJu3mKWE2_dDjbkjrfaMYt2jTKFWeg5z6_fRnqGhu_7XpzcArfab1qmI6by7LVY2sfdpI2w2kIaigky1q-RDX8WEYEsJbLTgs6-A1avGHtPa0XIYtQYA3t9-2nweCSGnRvg5W225rtN5d_bIhwWjKUpmZgBm-BXjsKHQsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان در حاشیه هشتاد و یکمین مجمع عمومی سازمان ملل، با شهباز شریف، نخست وزیر پاکستان دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/alonews/149174" target="_blank">📅 18:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7NAwi5YdOxnWK5LkyKhppc0r1z1V1uQnljfy_-M3Cm8WHgP6OTVjkrwEcEvdeF85rBBlGC0sJCsuDNH2qgW0moeozIwK77KQCdbrvtbAa7iZuQYrjihPIgAYwL2IALjb7VjY2pSY6iSwdKxFoE_kZM92XjU56INW77eZuS5aCh5NJM01unwud5-TzRLj8abzpf1PYU6KKvaeMQ2-kuIj1uic1o2-9iFehg973gHsyqeqHNLdBnyEK9WMxv0xtMxaQcjrpNOwrKKrT2tpO6NLbBV3t5pGyZ8Rlaw7GEdPQ97Ag7W32-KTEr6VNRoPkntdNxBoSplthcmi-U74BEDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعال‌سازی سامانه‌های پدافند هوایی در شهر صُحاب اردن، بدون اطلاع از دلایل این اقدام
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/149173" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368d12a226.mp4?token=sNvud05c65krIj9_bvwt_upILLzU9PhYEUP5XBND4WfXF9xxK4VRsBOVH8WFOKQw_DzOWNGXuji8u5-FAnEOx75VA4ixVJcYuGD7Xcy6FhZ0tDosdR0YVqeBJvClBwYcg33rQzoko02lS_xY2xnzneMuuGYb5Lw8nOnY1sm2E3E8zDw-qrTTqTKpEpXNlA9I8JsUD4sJF5uIErzehlLrL0i79yx08qNrlbl-CUbzYvK7aJ6BAUQ5u9q7mzTJBzDHLUqalyQ9A_bwFX-0moaw0oc-8eUFdPaX3Sv5p3kPZRtT6lyFo9tzktJEN0dM4a2SCwhyEYtUeZm5Qk7Zhfk7IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368d12a226.mp4?token=sNvud05c65krIj9_bvwt_upILLzU9PhYEUP5XBND4WfXF9xxK4VRsBOVH8WFOKQw_DzOWNGXuji8u5-FAnEOx75VA4ixVJcYuGD7Xcy6FhZ0tDosdR0YVqeBJvClBwYcg33rQzoko02lS_xY2xnzneMuuGYb5Lw8nOnY1sm2E3E8zDw-qrTTqTKpEpXNlA9I8JsUD4sJF5uIErzehlLrL0i79yx08qNrlbl-CUbzYvK7aJ6BAUQ5u9q7mzTJBzDHLUqalyQ9A_bwFX-0moaw0oc-8eUFdPaX3Sv5p3kPZRtT6lyFo9tzktJEN0dM4a2SCwhyEYtUeZm5Qk7Zhfk7IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین پینگ: خوشحالم که دعوتی را برای ۱۰۰ هزار جوان آمریکایی اعلام کنم تا در پنج سال آینده برای تبادلات و تحصیل به چین سفر کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/149172" target="_blank">📅 18:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
وال‌استریت ژورنال: نتانیاهو در حاشیه سفرش به نیویورک، به دنبال ترتیب‌دادن دیداری با ترامپ بود، اما این امر محقق نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/149171" target="_blank">📅 18:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ایران و اوکراین تفاهم کردند که تماس‌های خود را با هدف جلوگیری از هرگونه تشدید تنش در روابط ادامه دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/149170" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYiU6EtyHh6QIuO5H3rGl42KSaQ6E9gJaQOKK0QOtFutlxzTXF_EF9LJFtNPV0iF7Z7bQyXNeR-wA-SnY5uhHSDkiv9U7HkGB6dNtjSHxoSu7ljybI_Li1jF872SMrjuHkDNQOUz__DQHCeDAukTpB-3zopEbnlZWTT4Ev_zz9lLY-uQL7heRJxQEQtV00egZ-NbPAgOou7zeyRoT_tqfYIkABSHN0rTYuTHIh3bJ_3rnneaAI1qlju20eFBjFazyYr-Znnbpy1O3ZLCnAwLmwFD3QUbC95zZ-1o_awjFsJOjXDcAp3HbcwpCrQUdw4i3LQPrlP6DiySAFaL84IyRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشیال با انتشار تصویرش کنار شی، رئیس جمهور چین نوشت: فقط ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/149169" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
شبکه ۱۲ عبری گزارش داد که به دلیل ملاحظات و الزامات امنیتی، هواپیمای حامل بنیامین نتانیاهو در یکی از فرودگاه‌های نظامی و دورافتاده آمریکا به زمین نشست.
‏
🔴
این گزارش در حالی منتشر می‌شود که نتانیاهو برای شرکت در نشست‌ مجمع عمومی سازمان ملل در نیویورک به سر می‌برد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149168" target="_blank">📅 18:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ و همسرش، ملانیا، به همراه رئیس جمهور چین، شی جینپینگ، و همسرش، پنگ لیویوان، در مراسمی برای تماشای گروه "گارد افتخاری بدون دستورات کلامی" نیروی دریایی ایالات متحده حضور داشتند. این گروه، که از ۲۴ نفر تشکیل شده است، حرکات نمایشی دقیق با تفنگ و تشکیلات هماهنگ را بدون استفاده از دستورات کلامی اجرا می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149167" target="_blank">📅 18:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef0b8cbeab.mp4?token=RCWAriLvLBlfthPyPjAiW8lphLhyHCJ39UsfO4RVkhCh6OOdDsnit0Q1zF63MendvprPKz7iIbcNLjI-JSYIRHD6jxdhAUCKIvZMhL2-S2JFJKP2yavNY5P2yLsTEoJq56wUKiEqS4IZGHR7pL6N0AkY3vEF9PD3XX8fnOhgYqOp7PfKzHbtfNzbQOamww8pojebOs4GdHyBa2ieWkxIJWsJbvIoYvNydWiu36G8AqOLhmbUsThNVp27LBmMuMYg_lpKT2AyICWf76nSio5Z1f_au3RE1mjq1LA3txOBgo3T2TO-0yVNTDt0OK0AdiL9ZUR-VMWTC7tATxSdzE69HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef0b8cbeab.mp4?token=RCWAriLvLBlfthPyPjAiW8lphLhyHCJ39UsfO4RVkhCh6OOdDsnit0Q1zF63MendvprPKz7iIbcNLjI-JSYIRHD6jxdhAUCKIvZMhL2-S2JFJKP2yavNY5P2yLsTEoJq56wUKiEqS4IZGHR7pL6N0AkY3vEF9PD3XX8fnOhgYqOp7PfKzHbtfNzbQOamww8pojebOs4GdHyBa2ieWkxIJWsJbvIoYvNydWiu36G8AqOLhmbUsThNVp27LBmMuMYg_lpKT2AyICWf76nSio5Z1f_au3RE1mjq1LA3txOBgo3T2TO-0yVNTDt0OK0AdiL9ZUR-VMWTC7tATxSdzE69HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ:
خانم‌ها و آقایان، دوستان عزیز؛ تحقق آرمان بزرگ احیای ملت چین و عظمت دوباره آمریکا می‌توانند هم‌زمان و در کنار یکدیگر پیش بروند.
🔴
بیایید به انتظارات مردم پاسخ دهیم و مسئولیت تاریخی خود را بر عهده بگیریم.
بیایید دوستی میان ملت‌های چین و آمریکا را بیش از پیش گسترش دهیم و با همکاری یکدیگر، جهانی بهتر بسازیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/149165" target="_blank">📅 18:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbca495c7.mp4?token=QQzjiz8COp0kDtECabkjGRC0Md5KXipUEyjZn4iR-Ud9Amhc5Yiy7EsTJTENNwHC2p_Gs8GMt6NOKrU7ToRThfM_Ozl3dTRXGcGcQsKJfmsJirFoMWfnH6uAem6zWqYPvNWQfO3T88N5YXqMlceCUD9KoqQovjv28WpBqp8Ixbr9kqrvSOc-s84a7K7WmG60LtYstOiAHU4DSDWq86Tvf8-DT2SHgWhgeMSdWijcfYEhXz8VuwhQwItxNUfgCHGb3HaylBT_L-r1brGbuKawn_q2gA-B39LcbhgTrymfPaM41AowR-8hvP5mAnVbsfJGXIuTTeIkt_4009eUFpBQ1YsfOyGyV57JNIEdjC0UIL_YSrFGzBv3uUvwKGChgGMaJr2nMcNjVrBGldVNMlBy_rt5GOwRu9qYOX0oAwCkJzly9SbYpyxHrfW_ofCV6i25ZpNmpAzc7HCUN4fS3Y8BcYzWvPFW9zYwT8HciDrTqdFdz1bgozFbl3jImxgsvmwW_JhQu5jcMSon-fwcULfYCMl9C1hxvs0hTVD9cGgXJhyqnoBuu6UsQ1bQY9EhFzBUt74xqQCdjbQ5Ft_zH-LzEPCVXBbqArH2KMnhq_Me7OhyNTjBkXLy-e93YDDLh0lp38PtD-pXNX5wKAFyfl4l2QgHNzP2K5kqjkvhavSHA0o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbca495c7.mp4?token=QQzjiz8COp0kDtECabkjGRC0Md5KXipUEyjZn4iR-Ud9Amhc5Yiy7EsTJTENNwHC2p_Gs8GMt6NOKrU7ToRThfM_Ozl3dTRXGcGcQsKJfmsJirFoMWfnH6uAem6zWqYPvNWQfO3T88N5YXqMlceCUD9KoqQovjv28WpBqp8Ixbr9kqrvSOc-s84a7K7WmG60LtYstOiAHU4DSDWq86Tvf8-DT2SHgWhgeMSdWijcfYEhXz8VuwhQwItxNUfgCHGb3HaylBT_L-r1brGbuKawn_q2gA-B39LcbhgTrymfPaM41AowR-8hvP5mAnVbsfJGXIuTTeIkt_4009eUFpBQ1YsfOyGyV57JNIEdjC0UIL_YSrFGzBv3uUvwKGChgGMaJr2nMcNjVrBGldVNMlBy_rt5GOwRu9qYOX0oAwCkJzly9SbYpyxHrfW_ofCV6i25ZpNmpAzc7HCUN4fS3Y8BcYzWvPFW9zYwT8HciDrTqdFdz1bgozFbl3jImxgsvmwW_JhQu5jcMSon-fwcULfYCMl9C1hxvs0hTVD9cGgXJhyqnoBuu6UsQ1bQY9EhFzBUt74xqQCdjbQ5Ft_zH-LzEPCVXBbqArH2KMnhq_Me7OhyNTjBkXLy-e93YDDLh0lp38PtD-pXNX5wKAFyfl4l2QgHNzP2K5kqjkvhavSHA0o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
🔴
خبرنگار :  ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
🔴
غریب آبادی : ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
🔴
خبرنگار : ولی با CNN رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید چرا با من مصاحبه نمیکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/149164" target="_blank">📅 18:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017029214d.mp4?token=LM53qgtE4-4tFdm2y_8GzDqEE-dOIl82H-mqNQShU5-TqWYB4PHIPpuPNGBycJ-Ddlvp-o0e2hvUoE0CREdM8RiK6s0HfCljwvKdYWqY6gAmV9j2AKb9cLiQz2zfOVZTJQEabgE0lReDCYzf_0J7qbs9zA5noIIxv76eLNyFI5NTYa4QGyDByNohUfHltCyo8sF23u8_0Xw2tcl7pz5xWosxzdeVdc3affVSqeyksqBlQFAuFIWCYNcRAYXn8z7sMMOfPlVqdmxbFwf6cJAfLnt5C8PsJLmMebr1IiETWofiNwRLFNFzJ_wwzNKmFZP3sC-8NYaCrzlvrJ2rmZFfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017029214d.mp4?token=LM53qgtE4-4tFdm2y_8GzDqEE-dOIl82H-mqNQShU5-TqWYB4PHIPpuPNGBycJ-Ddlvp-o0e2hvUoE0CREdM8RiK6s0HfCljwvKdYWqY6gAmV9j2AKb9cLiQz2zfOVZTJQEabgE0lReDCYzf_0J7qbs9zA5noIIxv76eLNyFI5NTYa4QGyDByNohUfHltCyo8sF23u8_0Xw2tcl7pz5xWosxzdeVdc3affVSqeyksqBlQFAuFIWCYNcRAYXn8z7sMMOfPlVqdmxbFwf6cJAfLnt5C8PsJLmMebr1IiETWofiNwRLFNFzJ_wwzNKmFZP3sC-8NYaCrzlvrJ2rmZFfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جدیدا دخترا تو ایران با این تیپ میان بیرون
نظرتون؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/149163" target="_blank">📅 18:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از نگاه مجله تی سی کندلر، محمدرضا گلزار 49 ساله، به عنوان جذاب‌ترین مرد ایران در سال 2026 شناخته شد.  همچنین گلزار جز 100 مرد جذاب جهان در 2026 شناخته شد!  [@AloTweet]</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/149162" target="_blank">📅 18:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149160">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTcMyzllyZR0SwwweXX04uFcv4hSMkSzULM6CdpBXQscBJgUhUQdilBxtqlLD6FKXCH0hzMyiVE8nlbWl38ve5hdN21MWDiDBTRgbeuiM64_WydxsG4FJH5687ps7qPClFTivfaIrx8yk-uATqiodal0RRpOmlohTTWvtlcuB4XClJAEkGixwjyzX-mbFI57VvfY8M5nQ8BsGHTaMND6pG-mn445inbcooio8yPWi38sa4SrtEUUPD10TAsod_xCZHVj_3QL4wyfP5otTZ9aVTOpI0daw9qvUg6eneWbY5SAKLn89tj5hJqq-TZHUvmBIVKz-X_kl2UuWdtYZv5yFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ابوترابی: کاش آمریکا پزشکیان را همان‌جا نگه دارد و برنگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/149160" target="_blank">📅 17:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149159">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYceVQaFPM_8_oLrn9khfM1l13RboqU5EKaWyn_axufkWMbRQsSTDuELT0aog47ZUdGEnSQtK-EPiA9THqs3ycuf2hUhnJJbpzW03cGUOenbKsns42CX3WAd9iyuvYRtvq1p7QiJ-T3U724TLxjtl97VBKJ68rW2Ih9H93qp9kzM8a-fqn0icPoqHnbEM0CJTjkH2utHt4D8Uodp-0vnHIDUWhxq7FzXzEAefW3wemxAeeIjwhW4qd4dxKavXWweLPp1k2A7VNRJ9xlQBCxKLYgoLagML3foEsVw7JcLOsz1Mx81MDsN0qOEUttUCHfjuh69jJ1IyJouWLwI--E3dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرزوی موفقیت داریم برای تنها ایرانی دسته مثبت تاریخ مسترالمپیا بهروز تابانی عزیز
❤️
🔴
مسابقات از فردا شروع میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/149159" target="_blank">📅 17:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149158">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نتانیاهو برای سخنرانی امشبش در سازمان ملل وارد آمریکا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/149158" target="_blank">📅 17:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149157">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc96fad46b.mp4?token=NfT9iXzlKiuHXNgkHHEqhtsMJXKUTWfdv29GTxV3i76jcCH_svWowhKHgWNZ49RXsZM8GuBh3gG-PeF0YY6A5LSC6l74wbckPrP-ZM6RnRtWjV0BD9E_WoNZ5J4-VtpZDS0mxuWTqbaghHvyOvcYgUVNglorWGn8Q2Yeb4ECfN4EW_m35RBPSMSluq1VBY5r834pk3d1dyn8lOo9E0gi9gJc3fEEIKJO90dfThyjXvcT_oYc0Fp3iFnP9L1pBTaeA2cvB9Bgpxzd1w2ZkFolzpsCnRR-372I062ui_Jcm4_TxJBxXKO3G1Gzqb3JXpchFyolWoS1YR8L40oC8fyJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc96fad46b.mp4?token=NfT9iXzlKiuHXNgkHHEqhtsMJXKUTWfdv29GTxV3i76jcCH_svWowhKHgWNZ49RXsZM8GuBh3gG-PeF0YY6A5LSC6l74wbckPrP-ZM6RnRtWjV0BD9E_WoNZ5J4-VtpZDS0mxuWTqbaghHvyOvcYgUVNglorWGn8Q2Yeb4ECfN4EW_m35RBPSMSluq1VBY5r834pk3d1dyn8lOo9E0gi9gJc3fEEIKJO90dfThyjXvcT_oYc0Fp3iFnP9L1pBTaeA2cvB9Bgpxzd1w2ZkFolzpsCnRR-372I062ui_Jcm4_TxJBxXKO3G1Gzqb3JXpchFyolWoS1YR8L40oC8fyJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مدارس کشور موقع آغاز سال تحصیلی دانش آموزا رفتن بالا میکروفن دست گرفتن و دارن آهنگ تیرام میس میره علی گرامی رو میخونن:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/149157" target="_blank">📅 17:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149156">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
اگر واقعاً چیزی که می‌خواستند انرژی بود، می‌توانستند از راکتورهای کوچک مدولار استفاده کنند، که چیزی است بسیار مقرون به صرفه و قابل دستیابی برای بسیاری از کشورها.</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/149156" target="_blank">📅 17:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149155">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
به نظرتون وضعیت فعلی سر بحث اتمی که طی دو دهه حتی ۱مگاوات برق هم تولید نکرده و مدام تحریم به بار آورده و چند صد میلیارد دلار هم به اقتصاد ضربه زده، مقاومت عزتمنداته است یا حماقت؟  مقاومت
👍
حماقت
👎</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/149155" target="_blank">📅 17:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149154">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
به نظرتون وضعیت فعلی سر بحث اتمی که طی دو دهه حتی ۱مگاوات برق هم تولید نکرده و مدام تحریم به بار آورده و چند صد میلیارد دلار هم به اقتصاد ضربه زده، مقاومت عزتمنداته است یا حماقت؟
مقاومت
👍
حماقت
👎</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/149154" target="_blank">📅 17:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149153">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
👈
وزارت نیرو:
پیش‌بینی‌های هواشناسی نشان می‌دهد پاییز امسال پر بارش و زمستان کم بارش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/149153" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149152">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bksAqiKPMDWXTw2nXt0TM3iMBxX8piOV7yOkr-RorflRu6T5AwKQ88_6SEDi7uqtgK4WDoyZuF76sIH6Y8dHp_1eORarhmrdXmGeBSMbYLAjuW5vgrSFTnTiKVRM3y4uvvMpjfzjk7xtS52vOEUhkfQd916ZxarkTzDDHHWRe_s4xPAHKNZ1Vgc_h2UtWyDb8_L0IyePz0OcpU8iu8D0N6q-hk3GQ7B5FYqpf6w7r0V2zA0mxOu3pBinaaBn8B46-uN7nxznV-V3c1SQYc_cbja2leOxOIKck0RCvTb-gv6WqhWrFMAWep8KeEe9BA2JIMDFf7GFPgXcUTccG2EGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سرلشکر وحیدی: از جنگ نمی‌ترسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/alonews/149152" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149151">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad942f49d.mp4?token=L_pWL0TfPXlW3MA6F8nMJPteR7NRaMueUoSCx8F-N6K1vxs-OQWOtZAddU2OJEaH2w5fWLtrvfNw5O5TmlTrak2B1FfAA_4oiy2pq9f_6Nka0_QeZkSTDBUWBGNpnvAXs5_skWVuSBew51fVbkhdwxyyp1d_C2zhP4hxNb-MumxKosWDG_iifeyn9atNO0dgGuRK2y2xPy6tz20HNA7HLst3POLMxFd1_UQqIlUa7Q9DYGvUZmlyvCrQAidogYk7bKB53wpUGE3qDnkifEB15yusWLpyOQCuFySw_CsNDPwEkcSKNh97N9kNGtF0gfmAPf9k-FIQeUgp745DoYnLeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad942f49d.mp4?token=L_pWL0TfPXlW3MA6F8nMJPteR7NRaMueUoSCx8F-N6K1vxs-OQWOtZAddU2OJEaH2w5fWLtrvfNw5O5TmlTrak2B1FfAA_4oiy2pq9f_6Nka0_QeZkSTDBUWBGNpnvAXs5_skWVuSBew51fVbkhdwxyyp1d_C2zhP4hxNb-MumxKosWDG_iifeyn9atNO0dgGuRK2y2xPy6tz20HNA7HLst3POLMxFd1_UQqIlUa7Q9DYGvUZmlyvCrQAidogYk7bKB53wpUGE3qDnkifEB15yusWLpyOQCuFySw_CsNDPwEkcSKNh97N9kNGtF0gfmAPf9k-FIQeUgp745DoYnLeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بعد از محاصره دریایی توسط ارتش آمریکا، از الان به بعد دیگه رسماً محاصره هوایی هم شروع شده:
+امروز پرواز هواپیمایی وارش قصد داشت از تهران، به دوشنبه پایتخت تاجیکستان بره که ترکمنستان و جمهوری آذربایجان اجازه ندادن این هواپیمای ایرانی وارد مرز هوایی‌شون بشه و نهایتا خلبان مجبور شد به فرودگاه امام برگرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/149151" target="_blank">📅 16:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149150">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsPFPJOKCSxXMuurBJlERBIXAIdiV937RjuWDXCKDYhlZpx-kt6MZeOwANIzjm4FeiLzFDGbbTn77npugWgAizx4wkJiAXqTUj77cQzYhkgkquCqsI1N_TEIe90FkOw6N-51z2QLdAeh-Ur15j5X-f30S2DyZvd4z8ScOvvEhIfArmo2lSuWwf_6txb0oN2dEtAou6u3T-4DZd-Cv2Ra62LygIqVQV-tHXJi4q-jhXQr6Wcvp6kGVPjG8rFbN-agVj0gJkNRB77fEHYHsds4LmzQIuwZq1nmd7VAR5xXmeqPBLPWLDDObXcJifzWP0YmqaSwJnpwA57D1AFei5WgWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در سال ۲۰۱۲
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/149150" target="_blank">📅 16:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149149">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdbH12An-mfutm7cKRZHr6U6ShfJiIYzTyZoIxQJ8MxdpcDREWiGyFBorq_eB8m1UsP4GNvYHcDIrF85W7LISfJlEgJhe2wY1zQWaSr1u6Xi_1o_zvNmkAMxA8DyJLjUQyGlKceew7aEBYVuii12dqhKgbQHqZkNXod-_gcqLbk2Hv1QsvspVlnphSiWlTGzsia1m8InHwtByGXzalwW_CCtvkatslVl6Z2e-KKN46cAKsQoMxCOG_QwWR84BL7f4J4EOTOyaKEsCjJVcI1Z03Bhj9iY1qb2QVNHwJghWpCkX4vTOGU_tUjGBkqtYMi7keK1Ym9YDppTADqRnUrSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: دیروز در فرودگاه با رئیس‌جمهور شی دیدار کردم و به‌نظر میرسه قوی، سرحال و آماده‌ست. بانوی اول شی هم، مثل همیشه، زیباست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149149" target="_blank">📅 16:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149148">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پولیتیکو: خبرنگار این رسانه با وجود دستور یک قاضی برای بازگرداندن دسترسی رسانه‌ای، از ورود به کاخ سفید منع شده و کارت خبرنگاری او ضبط شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149148" target="_blank">📅 16:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149147">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت نیرو: پیش‌بینی‌های هواشناسی نشان می‌دهد پاییز امسال پر بارش و زمستان کم بارش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/149147" target="_blank">📅 16:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149146">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آمریکا به کشورای اسپانیا، فرانسه و ایتالیا هشدار داد که بزودی ممکنه روسیه بهشون حمله پهپادی و موشکی کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149146" target="_blank">📅 15:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149145">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae691e363.mp4?token=nTEt5w6-qNbPvjVYJCUnb2YHbyVcZYeDB4VSxQymA8Zgi_dO_0N_s4gY2ONmnECAEAMaF5NaAdUzWY7es_B2CfXAN_F2yx1qrH10J4i9qeWAI698pNU_Y2K0DtkQs8NBv0Y_rcwmuGXNHxvyJ1-K0XPxKltvyjG3A4oTmLbImc6fQcu7nPBNApdvuEUq4mPmgOIzY5q1Phg8kcXo-W4pXx1iUYOm-V51KuJC2XC7-JpJ2klH7IjAZ4MlIFLfYrKDhs-FgkW_gDpmIrG3Fri5qIfI1d-GyB4MSOQy7_sH0ItY1uttWv8gL9_wdf3B5QGIWkEmI_SvIIio-0JGICnP-KAwunkXLH4ew59ZSU3aOhf7xqZ4fVzSUtIbA1KPJ1MtuDdh5N-ZHQ88-0RUMP3T-ia0VifEGCxBGx2sNUFVjV8nX38aMSG0EljGXBFdKFaohO5smJ6EAJdA7bgPMF8Vs7DZ-i8ucJPh9_SlPiASoNHuiH9FxtVVIhZ1OXEAaVgDG5wo5lPgcELHW-_slokvZLGqEm2xcKQ5l2czfXZZFO6rhkDlgcxztSBqQPu8R1SmD2znsqptBcOOlvqDL-wWpHQ8oBwe2QN8H9j3M1FVplinV-Y3v6dzJM0DIa-uDsMo44DRWfNzNKCcu2HubFg4HszjbTLGRH60GDv7E2NcAfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae691e363.mp4?token=nTEt5w6-qNbPvjVYJCUnb2YHbyVcZYeDB4VSxQymA8Zgi_dO_0N_s4gY2ONmnECAEAMaF5NaAdUzWY7es_B2CfXAN_F2yx1qrH10J4i9qeWAI698pNU_Y2K0DtkQs8NBv0Y_rcwmuGXNHxvyJ1-K0XPxKltvyjG3A4oTmLbImc6fQcu7nPBNApdvuEUq4mPmgOIzY5q1Phg8kcXo-W4pXx1iUYOm-V51KuJC2XC7-JpJ2klH7IjAZ4MlIFLfYrKDhs-FgkW_gDpmIrG3Fri5qIfI1d-GyB4MSOQy7_sH0ItY1uttWv8gL9_wdf3B5QGIWkEmI_SvIIio-0JGICnP-KAwunkXLH4ew59ZSU3aOhf7xqZ4fVzSUtIbA1KPJ1MtuDdh5N-ZHQ88-0RUMP3T-ia0VifEGCxBGx2sNUFVjV8nX38aMSG0EljGXBFdKFaohO5smJ6EAJdA7bgPMF8Vs7DZ-i8ucJPh9_SlPiASoNHuiH9FxtVVIhZ1OXEAaVgDG5wo5lPgcELHW-_slokvZLGqEm2xcKQ5l2czfXZZFO6rhkDlgcxztSBqQPu8R1SmD2znsqptBcOOlvqDL-wWpHQ8oBwe2QN8H9j3M1FVplinV-Y3v6dzJM0DIa-uDsMo44DRWfNzNKCcu2HubFg4HszjbTLGRH60GDv7E2NcAfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس، نماینده اتحادیه اروپا: دعوت آقای ترامپ از پوتین برای شرکت در اجلاس G20، شنیدن آن بسیار دشوار بود، زیرا با توجه به اینکه حتی چند روز پیش، تعدادی از افسران اطلاعاتی روسی به اتهام قتل شهروندان آمریکایی در خاک آمریکا دستگیر شده بودند.
🔴
بنابراین، سوال من این است که آیا این افسران اطلاعاتی به صورت مستقل عمل می‌کنند، یا دستوراتی از ولادیمیر پوتین دریافت می‌کنند؟ و من می‌توانم به شما بگویم که آنها دستوراتی از رئیس‌جمهور پوتین دریافت می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149145" target="_blank">📅 15:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149144">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvNCk5gj-_NoFSjq04bpxVckQywWKc9JJlMlNpw2LFrknMr4N_0x3bnf7tAwHN3aBBKot5VLkQm7D_y5GqphHkoDfsFMu4nddD2fmNPfeLZRsjmHPHznyFJPnyqnS8AzUC3nxJnJ7v6NAZOu5zqHKppiDjU5Mb7Zpq4AQrZNgyxDAeqs0rIkYqbo45_5B2evzgIsgFWNuyarVLE9NCnX2jJ3TP0vWADxcvP-4-Ewi4xfxwa_vcEMS-8HfoYXp5oGzZBB2mfgPLjJP92n_M0e9bHNBbN7tWNgFWoptJOKUly8zvIRVgzYAen2wBr1utVzZLWfrYnBsvGBbO31d8bHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: امروز روز مهمی با رئیس‌جمهور چین، شی جین‌پینگ، داریم. ابرهوش (SI) یکی از موضوعات مهم گفت‌وگو خواهد بود، اما من می‌خواهم شرایط دقیقاً همان‌طور که هست باقی بماند. موضع چین هم همین است
🔴
چارچوب کنترلی ما وزارت دادگستری آمریکاست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/149144" target="_blank">📅 15:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149142">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hZSgDpsalz5ZZD8mQ6lMoqysqsA-YpEWOh1SilnIo-UdEcP7iie2yhGgEkn7Zoms7Uq09H_deuCwn0PS25TmOeIGCxDP10kCw1hO_3L1qg_jIbxQU88S5TFwmqm-S3qJ3P5aiAREN0d-YOLsDS6fBn4LgNrbURkuSq0dbE_UTpY5qEZZI5KO0tbKD1dlHu8q30FxM_9cBtuWr-KoyWlvlRVOxHGfqkST-uy4ZhYrtv33gm14dxgGId7_Ejy4fOS-y8aq4xolMYYQSO6gIHZbxMDBlf-bOxAmUw992Ta7ifYbRCuGcsWNtNQmKJVX8ZcY5o5d70UbVPi65VlpIhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای تانکر سوخت سعودی در حال پرواز از فرودگاه جدّه به سمت جنوب و در مسیر یمن مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149142" target="_blank">📅 15:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149141">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بلومبرگ: دونالد ترامپ، رئیس‌جمهور آمریکا، و همتای چینی‌اش بر سر تمدید توافق آتش‌بس تجاری تا ۱۰ ژانویه ۲۰۲۷ به توافق رسیدند. دو طرف همچنین با وجود اختلافات موجود درباره فلزات نادر، محدودیت‌های فناوری و موضوع تایوان، بر جلوگیری از تنش‌آفرینی تأکید کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/149141" target="_blank">📅 15:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149140">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
مراد ویسی :
آخرین ارزیابی‌های منطقه نشون میده به احتمال زیاد حدود ۴۰ روز تا جنگ بزرگ و حمله آمریکا به ج.ا فاصله داریم.
تنها درصورت عقب نشینی ج.ا ممکنه شرایط تغییر بکنه!
🔴
دیدار سه‌شنبه ترامپ با سران ۱۲ کشور منطقه نشون میده اون برای جنگ پیش رو با کشورهای منطقه هماهنگ شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/149140" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149139">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی‌ان‌ان: در نشست ترامپ با سران کشورهای عربی در نیویورک، قطر و عراق با هرگونه اقدام علیه ایران مخالفت کرده اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149139" target="_blank">📅 15:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJy89jB8GqeS63hd7jcVp6-8AERXUsZh3m5WAyyw8cpP3ElpMgWF1I1Li17Oz5_-KWgIBxfgHSbxLz6-Uf2ozcnA6ShKx1gr4NvIOMv0nMw9v44GLrpuQAGQzkPUhzKMUPjhm7uWAXWDGpn5aejqPQLVFMTgaBI8GhWZvqAf1ml9vM5FCXXhvCMtPES4BiWjq3DTRsuE3aP9A11ZBjN89FhRNVBVm3sBiyTOG8HdJh7icJjPAb8ZbEnMpPCnIAwK0XBuMv0Znk4SeWNX73qvFEfixdp-67vcaZXsLvN8-AJ7J6OSC7fOZqKmftLnISgbC9Ut8i1xa-pJLRSECR3UVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنای ایالات متحده ممکن است از روز پنجشنبه به یک طرح رای دهد که بر اساس آن، رئیس جمهور ترامپ ملزم به پایان دادن به جنگ با ایران خواهد بود، مگر اینکه کنگره مجوز ادامه آن را صادر کند.
🔴
دموکرات‌ها تلاش می‌کنند تا قبل از انتخابات میان‌دوره‌ای ماه نوامبر، این رای‌گیری انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149138" target="_blank">📅 15:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149137">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فایننشنال تایمز:وزارت امور خارجه بلژیک در یک سند داخلی که به بیرون درز کرده بود، هشدار داد که ایالات متحده تحت رهبری ترامپ "دیگر متحدی نیست که در گذشته بوده است" و خواستار بازنگری روابط با واشنگتن شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/149137" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149136">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
الحدث: دور دیگری از جنگ اسرائیل علیه ایران قطعی است و اکنون تنها مسئله زمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149136" target="_blank">📅 14:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149135">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efFx_EH9jl22yBzrtmXgDCQOd6tWSu53pvK-M-kOrCHgaR43Ddz46j1Fqxp96-BTIQ6Z5FTqxKSR-Lm5JsBqAOUiObidMCI-osJrsC9mwBwDAykTBJeLrl_wzdVFy6--wbOUWZU2cYyDPD87WT6XZPT_e3f--nKGsal5_uDO2Nf5MLM7DcwKDY8IBXpQefcTR_TTTac6syomy6SofrF-oOflq9Ldz52L6JH96BsQOaw1BW2eeHRcPDhL_f7ns8PSJ5R37X2gTvBhG1YhFMrFLniByWWj3Wz9BBcAtfC4EN9ujHGGJObc9wKzwW3C5NvlspKlS3-Tl5fE2TDYj8a3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : دموکرات‌ها، دروغ به دروغ می‌سازند. جدیدترین دروغ آن‌ها این است که من می‌خواهم تئاتر فورد نام خود را به آن بدهد. آنجا بود که آبراهام لینکلن ترور شد.
🔴
چه کسی می‌خواست چنین چیزی؟ من نه! این یک خبر جعلی است که توسط MSDNC و CNN منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149135" target="_blank">📅 14:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149134">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHY-qAdzTXAnfExiHkk4LzcX0qymQoUreg-wTEhUOSNzq45Glsgom7NNjkgwDNP8FuUby0zwGYn5096ICoQeAjOThauSoBini726CgpGHTtISZxbsLIHiz3mfRXvA7EcqT9pWn3aq2t0SZ-cFZTq3sY4uGAVu0thaOEl-EqbaU8BqlJvjrN58dyZSryaH5LrqqQ_QmhFXRxuHvH-TWQXqCF6MFkjoWeplgEmoTYfKpILcK3Nyw2alA3z1TM03arA2FKx44WycZlpI2AtFzU4qrobCv9S5hy9Q5yx0r-I3iyBWFhhefyAr0VmeIGSDhWgxEpo5lDoZeADjLBeeVZEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بارگیری مخفی نفتکش‌ها در شرق عربستان
🔴
در ۷۲ ساعت گذشته نفتکش‌های متعددی در پایانه‌های شرقی عربستان در حال بارگیری نفت خام بوده‌اند، اما AIS خود را خاموش کرده‌اند تا در سامانه‌های عمومی ردیابی نشوند.
🔴
با این حال، رصد ماهواره‌ای توانسته تمام این نفتکش‌ها را شناسایی و مسیر حرکت آن‌ها را ثبت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149134" target="_blank">📅 14:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149133">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
کارشناس صداوسیما: در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149133" target="_blank">📅 14:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHEG3QTC25dl827XZRUIwXd86wzH6aR-awcBFxGjlN-GjIvcTpQUiI-azIn7XVtK1cXqsyCQFzyHQUdv01deRdL4uuqDoDOY7VzJKH107bSRJ0xsnDvDvoBzIXXu_DCDt-PMVj3JWHsZcBvZlLPXVSUYcklIJTWGxfTCsEuESlUUF9ZgvTFoYAwTqdEqwsoWmDVx-zY8B-VBFMbv8Q9EL0DesKtXgvhgMbPI1FpqH5_QH7KAklNh9KvI-HG8WPbhQVkDbWK0p2yUW1HfNHO334LlE_PAB0oc7nXc7dQ9qfhI81_EdnTFIkL62kWVB3UtBBbndsAjWHZMCvTBdPecAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njAmrjCirlVPqkg3Kfjl2MTISRztF-kAoqm753ZXhwp9gdubTULQxCFn1E8KJcInj0uAKb_eF9QwTXfd9ht5b2eX9mTJGdjE-6L7kI9QZ3L5nvvlLasQgeZsGbYDNS6S6U0di8Si5Tc0uWM6-9R8NZL9kwPX8lvbq3ZY99sWJRQB_TPK849awPAicB7yvJXiyLONV-EoCvS3W8pXoP2geFs5YKKSNAC-gq0bE3lvw3D34FuFlratHgkAUg0Anguhp6QjhH7jfX2z_X52BROKhoctosQrGQR95vx92yWFgDfZpeR6-qIptTl-qLR4zHZpsGd8fAplsLEe6gCcsZ-UcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) پیش از این، موشک‌های بالستیک را به سمت عربستان سعودی شلیک کرد.
🔴
هنوز مشخص نیست که در این حمله از چه تعداد موشک استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149131" target="_blank">📅 14:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سازمان دفاع مدنی عربستان از به صدا در آمدن آژیر خطر در استان طائف‏‌، مکه مکرمه، جده، ینبع و تبوک خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/149130" target="_blank">📅 14:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
مدیرعامل آرامکو: هرگونه اختلال در تأمین یا فعالیت‌ها را می‌توانیم «ظرف چند روز»، برطرف کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149129" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
دیمیتری پسکوف، سخنگوی کرملین:
هنوز خیلی زود است که درباره سفر پوتین به گروه ۲۰ و ملاقات او با ترامپ صحبت کنیم.
🔴
ما پاسخ خود را به این دعوتنامه در آینده اعلام خواهیم کرد، اما روسیه به هر حال در فعالیت‌های گروه ۲۰ شرکت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149128" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترکمنستان آسمان خود را به روی هواپیماهای ایرانی بست
🔴
سخنگوی سازمان هواپیمایی کشوری: به دلیل اینکه ترکمنستان مجوز عبور ایرلاین‌های ایرانی را از آسمان خود صادر نکرد، پرواز تهران - دوشنبه نتوانست در مقصد فرود آید و ناچار شد به فرودگاه امام در تهران بازگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149127" target="_blank">📅 14:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سرلشکر صفوی: تنگه هرمز هیچ‌گاه به شکل قبل بازنخواهد گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/149126" target="_blank">📅 14:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بانک مرکزی: صدور چک‌های رمزدار از سه‌شنبه ۷ مهر ۱۴۰۵ ممنوع و پذیرش این چک‌ها در سامانه چکاوک نیز از اول دی‌ماه متوقف خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149125" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
گزارش اختلال GPS در مناطقی از تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149124" target="_blank">📅 13:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFBNsudWwNq4jofOY-APW2Z2xa3OCdxBfHARkOqV-nsAcUB8ZmeyFXPMXo-EUOn5tC36rzoeZSHQGh94VQUHEliqy1_k-LaHm98ZYl6qA5I8l2ZXPnXQhtusAXkWml3OctPZKv3tonmqqo-NhprMFRNsC7D8juILYqbWYI8nbQrLagkaeO_BFEh9fNkiJ8l8BetQR3_HWahVAIMJD9yz5tYA4kAMdsmd-aFe55buRBDGa0QTZJSL_7inzIF7UHr2dNbjDvnjgCN_r0RIqZqWzGMIG5DI5FqZDcUYWiAi3ho8GaDekS911gYq-a2VL9SMTuOHDZW49yGB89gxwSrDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1Hf5ZuF0UsasXGU0NnjeUIUhQXxsQ_xNjLRPryziob43ZspAkwhxte4W6EAXO-F7UO8MhxUPih7vgt53ffxm3ADb5tR1OpsmRFjNEWNA7OxHXguHHPJooK-lVFf7fdZqCqvmOyPU9KNZperY3nQp5wvD-kl11UTmBSth-AVrMokR95-zFo6gKUTbzSsDDIWZ2nbBJ9Huiqn8OILuTS2BIftvHKjROOO-DfxfqS8c5ZUkpQGY6i3XqojZ81TPk0UkJzwNvk8AK7LD3BW4RXMZYBwIXJnMtC0dYmqXeTK0icabu1eydKfd7o-Zjo_TcXsYWvVCsWA_o2q5BrzklDnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hhbK3ynexlI-hZgefH-ctsXu5-ub9jvE5QuYHC9e00oeUgm7wUMpyDFMUa4Hg8sULy3Dc-c_FrJQ53VZnLLGnlYBHLKcE0nPo1okQ-FgACqX-0iepWJRctIvPwXbHS8fWNe1WmwfdxZwuDfnlcfl-44L-u7vDmOtqqtS6rg7HyJ9IloRC5Fm17PSdMzYD3OLP8rHO1VmRFv8UNpREnyA0mUZS7ZQ1tlvr8BAQuyUTnrnwrC-_5_79KQh0RPYezPhoglh0i3-fuSSzH3ih0yBo4NpJ89h1qJTmvs7IJHDT8wJa4PYGrfPpWi8Lb6UIb3oRokgWfMAOLHilGdjVIP7Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/149121" target="_blank">📅 13:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP5yknpy3d5HkL1frf31GLdDVH_bfFVdAX4G12R9i291ZgbOJPZPI_CM71bcGh5yiWS_bkDVa8Zg4tYRi4-Z_u5PFXg6nuH82Mn6lVhTwsDqxW1BR9yeZKHR_kZkI3JDqt135uIgx1kTZJTv0kcFGrn0kn7Av3aJywjS2e_AxBykvoAZy_ItsyCogy6w1SYZdZmJS1UkBRQY0oDgWxgwhger5SRQNtb2NI76ao6KPloRdDsonyEb4sxjs0rf486FENteFXXahRzbkQRELeq4hzi3y2idegI-2BhiiWoURlVMaURNr43puBeNHTY4gLJG0xPKbDxuG8GwLMUbNIP0MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت، ۱۰۶.۳ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149120" target="_blank">📅 13:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO7GeVPzPv1haVe0liiKDMV4rtTbpjF8QPXMuCHkkHD3nsAjQN6BNIZ3p4nFKfeHS9s69LlTNgGuLgcHEkS6_r87zQTRpG1c1ijYV_I6mpEDxTviDl2Jd7zWgIHVed7o7Y3YAdOWQ-jzujmectyPWE6l63SbfTSHO3ThzxMrW5L7PReYo4ItEM-JGLEENyi_apIUwkzikWX77UxQMspyrvgKam5Zlk5Kp3l2NIhsyeW-FcZ8ifK-nnlxm0RVlsLi0wknyYkZMF8W0SVcAf4eyPNXkvlcA7aswWRi5TLZIxMxQehUfegYf-rDg6uuIhXOQStDTYQ91F5VZFeckgAPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر جدید از حادثه امروز در پالایشگاه آبادان
🔴
صدای شنیده شده امروز صبح در برخی مناطق شهری آبادان به دلیل نقص فنی در یکی از واحدهای صنعتی پالایشگاه آبادان بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149119" target="_blank">📅 13:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
آرامکو: ۳ مسیر برای صادرات نفت داریم/ در حال بررسی ۲ مسیر جدید هستیم
🔴
رئیس شرکت نفت عربستان (آرامکو) گفت ما هم اکنون ۳ مسیر برای صادرات نفت در اختیار داریم و در حال بررسی ایجاد چهارمین و پنجمین مسیر صادراتی هستیم.
🔴
وی افزود، وضع انرژی در جهان بدتر خواهد شد زیرا قطع جریان انرژی، زیاد است نه محدود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149118" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
یک منبع اسرائیلی: ایران فعالیت‌های خود در زمینه انتقال و تقویت تاسیسات هسته‌ای خود را در منطقه کوه کلنگ در نزدیکی نطنز، تشدید کرده است
🔴
در صورتی که تهران از خطوط قرمز عبور کند، مجدداً برای حمله به تاسیسات هسته‌ای ایران اقدام خواهیم کرد.
🔴
ما هیچ فرصت واقعی برای دستیابی به توافقی بین ایالات متحده و ایران نمی‌بینیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149117" target="_blank">📅 13:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=F0dfaYHf_bu2NsTkAyWt8o2npDUYT6j_pTuwGv5s7INB1KJwWfT8WtGFS1hBLI3e1pf8epYPKbPUZnvtaj0a3pmSTYt2G86V_vhj-kowHiXwtvJwgt5I18MPs_tCb7gPFYxq6pM7YM_YEJabHRLoXH8wNPzAn8-lkvusodPxqcimUOQOePYndqdfb-ZCX0DPUIHqEtvK2QLy4b0mCT2clMRm50d3s2RnMX8g7R71xUmBqaXVBRmhLxcDuPeTWftwsQXnCZh5VADqc2dDMM580ZZjOZS5NgOFC2AT_nZDdatBgbjTkbrdN2Jlvq-d_iefjtyDMCbv8It3h7s0gW8FIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a5b9bfa1.mp4?token=F0dfaYHf_bu2NsTkAyWt8o2npDUYT6j_pTuwGv5s7INB1KJwWfT8WtGFS1hBLI3e1pf8epYPKbPUZnvtaj0a3pmSTYt2G86V_vhj-kowHiXwtvJwgt5I18MPs_tCb7gPFYxq6pM7YM_YEJabHRLoXH8wNPzAn8-lkvusodPxqcimUOQOePYndqdfb-ZCX0DPUIHqEtvK2QLy4b0mCT2clMRm50d3s2RnMX8g7R71xUmBqaXVBRmhLxcDuPeTWftwsQXnCZh5VADqc2dDMM580ZZjOZS5NgOFC2AT_nZDdatBgbjTkbrdN2Jlvq-d_iefjtyDMCbv8It3h7s0gW8FIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاکستان رسما به ده نقطه از افغانستان حمله کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149116" target="_blank">📅 13:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
پرواز ایران‌ایرتور در مسیر تهران–دبی لغو شد
‏
🔴
بر اساس اطلاعات درج‌شده در تابلوی وضعیت پروازهای وب‌سایت فرودگاه امام، پرواز امروز پنجشنبه ۲ مهر ۱۴۰۵، برابر با ۲۴ سپتامبر ۲۰۲۶، هواپیمایی ایران‌ایرتور در مسیر تهران–دبی لغو شده است.
‏
🔴
گفته می‌شود: امارات اجازه ورود این پرواز از ایران را نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149115" target="_blank">📅 13:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
پیشروی ترکیه در شمال عراق برای تصاحب اردوگاه‌های پ.ک.ک
🔴
منابع رسانه‌ای از حرکت یگان‌هایی از ارتش ترکیه در داخل استان دهوک در شمال عراق به سمت کوه‌های کاره و متین خبر دادند.
🔴
طبق گزارش‌ها، دلیل این تحرک، تحویل مقرها و اردوگاه‌های پ.ک.ک پس از خلع سلاح و عقب‌نشینی نیروهای آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149114" target="_blank">📅 13:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29ccce0989.mp4?token=AJ7Be4Lhi2uSSgfh5-Slu-76SqnT3ibG_T-KnyY917-ZET19dQY1Eg0550NGsf4RgikB7e3s1rNNzIwaEBVifURpI_d3MkxhNOXEq1Q_W5wyGn1U7cyhM8XpIKp6Ot00ZzPbMpuwZlFF9IeSh2CkShcYVLzzsoCMPTQO1gJ620h_xEyEheinbfuuUPbjYLRBQVm35_5oHdMVnxiNDwWqA1XAUE3yMN82AtNrKjEJyrAc9AfllMutNNf2UHroPtK24W0SA9tjnGEY168HJlKjA18DbqgjrGH4u0TlNtvLsaF_jF1jRH764t8gfJ0uFhafnM1RKqAWyzpBjAx6A9eUBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29ccce0989.mp4?token=AJ7Be4Lhi2uSSgfh5-Slu-76SqnT3ibG_T-KnyY917-ZET19dQY1Eg0550NGsf4RgikB7e3s1rNNzIwaEBVifURpI_d3MkxhNOXEq1Q_W5wyGn1U7cyhM8XpIKp6Ot00ZzPbMpuwZlFF9IeSh2CkShcYVLzzsoCMPTQO1gJ620h_xEyEheinbfuuUPbjYLRBQVm35_5oHdMVnxiNDwWqA1XAUE3yMN82AtNrKjEJyrAc9AfllMutNNf2UHroPtK24W0SA9tjnGEY168HJlKjA18DbqgjrGH4u0TlNtvLsaF_jF1jRH764t8gfJ0uFhafnM1RKqAWyzpBjAx6A9eUBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت درباره ایران: ممکن است تانکرهای نفتی مورد اصابت قرار بگیرند. بسیاری از آنها به مسیر خود ادامه می‌دهند. آنها به مسیر خود ادامه می‌دهند.
🔴
می‌دانید، ممکن است ایرانی‌ها سه، چهار، پنج یا شش پهپاد را به سمت آنها بفرستند. ناوگان قدرتمند ما مانع از این کار می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149113" target="_blank">📅 12:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2a4fb766.mp4?token=TQBszxj0Td8xCLyjeHXCc3baG2HMzX7cFjb55B5tFc0sf25TZf7WjFdfhWRc9k601hWoovfXYbQ5atA_S8FJO_78H30_vmixBgtNW9WqFGIF_7vNROetjEVF9JOroXy9z3e1ss8areItCRVHBMxpxewUkyzdGmCfpNuDhRlrz141aueEdQ-997uo3ZNOm04LqaueblpbQho0uGL3tvvtZe2aS_WVjf_ZITzetY_HuvB5VrTqk2ekGSW4EqP4BGMh0fgr35nkJIlC6z3Cz3c_OCT5jViwgSe9cG0HAZGp3F8DRujza1COT5UiX5ueEL7e3hq4sMMQVdPuTBXQT2N1hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2a4fb766.mp4?token=TQBszxj0Td8xCLyjeHXCc3baG2HMzX7cFjb55B5tFc0sf25TZf7WjFdfhWRc9k601hWoovfXYbQ5atA_S8FJO_78H30_vmixBgtNW9WqFGIF_7vNROetjEVF9JOroXy9z3e1ss8areItCRVHBMxpxewUkyzdGmCfpNuDhRlrz141aueEdQ-997uo3ZNOm04LqaueblpbQho0uGL3tvvtZe2aS_WVjf_ZITzetY_HuvB5VrTqk2ekGSW4EqP4BGMh0fgr35nkJIlC6z3Cz3c_OCT5jViwgSe9cG0HAZGp3F8DRujza1COT5UiX5ueEL7e3hq4sMMQVdPuTBXQT2N1hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بِسنت: ما از این جنگ در ایران عبور خواهیم کرد. قیمت انرژی کاهش خواهد یافت و قدرت خرید شما دوباره افزایش پیدا خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149112" target="_blank">📅 12:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3318463bf.mp4?token=mNpI9hwszxeYuvPi4pYu3aooK3L5TGIt3eIUNHNPgb-wAVzON-42PdKx64FYlyyNVXRGK9ynXwe14Gq0fKcnz75JH9LpuPrph3HXpq0J6lR7Yls1mv5AlHIY-YeqBbliWvv3eILucIB6-_BlpNVwDnziQ5LiiKm0bOC-TKIsKJEBO4z-9asOxs9AvfAWJ6LhwemgR6Rb6-or2efl4Q31xIh66wW2vzM7W5_Ucug8xE5v0x9pU-5DgbmNvBVUq9NottMpHJABKXk3udvTFAMagbq-M9pfdJXIy8GwvRMvXbvMZ2S5PFmHZv55H8kZFYH2axDz_dwkHRTJK-FFgEEraFGr9RAYcxDBT4hNB0OXE5ujXE64JowStak9I6kC7Dl9T49nQ_NS6XCqRQiyGvN2cqN1CGkUfn-cYn50mPq9GGIIH_0TwQ9jfxklf9Bwdp60Tb9Z27ACNBhH0BtzpiWwUPibbaXkUHcb2mGkqKDzCtzwoWKYElBHlAaiSi571NgFHsk_PCFCKzzCQGZdqFR4yOqYWj_fZvvUBJMnU5pSP8xQ9PNqGGN6xRNIgLjrqeGpY-JMqPvAirHJTwTKeeBDhC1Il26iTdYHqpbymjKE-cOIJM9WAfxRAqkKFBq3ck_uIXSfzvU_tKD7zMNqFCzW5lp4tpWEaHt1ypqLz9_ps4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3318463bf.mp4?token=mNpI9hwszxeYuvPi4pYu3aooK3L5TGIt3eIUNHNPgb-wAVzON-42PdKx64FYlyyNVXRGK9ynXwe14Gq0fKcnz75JH9LpuPrph3HXpq0J6lR7Yls1mv5AlHIY-YeqBbliWvv3eILucIB6-_BlpNVwDnziQ5LiiKm0bOC-TKIsKJEBO4z-9asOxs9AvfAWJ6LhwemgR6Rb6-or2efl4Q31xIh66wW2vzM7W5_Ucug8xE5v0x9pU-5DgbmNvBVUq9NottMpHJABKXk3udvTFAMagbq-M9pfdJXIy8GwvRMvXbvMZ2S5PFmHZv55H8kZFYH2axDz_dwkHRTJK-FFgEEraFGr9RAYcxDBT4hNB0OXE5ujXE64JowStak9I6kC7Dl9T49nQ_NS6XCqRQiyGvN2cqN1CGkUfn-cYn50mPq9GGIIH_0TwQ9jfxklf9Bwdp60Tb9Z27ACNBhH0BtzpiWwUPibbaXkUHcb2mGkqKDzCtzwoWKYElBHlAaiSi571NgFHsk_PCFCKzzCQGZdqFR4yOqYWj_fZvvUBJMnU5pSP8xQ9PNqGGN6xRNIgLjrqeGpY-JMqPvAirHJTwTKeeBDhC1Il26iTdYHqpbymjKE-cOIJM9WAfxRAqkKFBq3ck_uIXSfzvU_tKD7zMNqFCzW5lp4tpWEaHt1ypqLz9_ps4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت درباره ایران: نمی‌دانم یک هفته، یک ماه یا دو ماه طول می‌کشد، اما آنها تسلیم خواهند شد (به گریه خواهند افتاد)
🔴
هدف در اینجا می‌تواند یکی از سه حالت جهان باشد: رژیم علیه خودش می‌شود؛ ما نوعی قیام مردمی در ایران می‌بینیم؛ یا کاری می‌کنیم که ایرانی‌ها، اگر بخواهند توافقی انجام دهند، به آن توافق پایبند بمانند.
🔴
این بار، اگر توافقی باشد، به شما تضمین می‌دهم که به آن پایبند خواهند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/149111" target="_blank">📅 12:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فیلد مارشال، محسن رضایی: ما با عمان به یک سازوکار در مورد تردد در تنگه هرمز دست یافته‌ایم، اما واشنگتن مانع آن می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149110" target="_blank">📅 12:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سپاه: فردا ۸ صبح تو تهران رژه ۴۰ هزار نفری موتور سواران جانفدا داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149109" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مجله «آفریقا ریپورت»: عربستان در اولین واکنش خود به تصمیم واشنگتن مبنی بر عدم صدور ویزا برای رئیس شورای حاکمیتی سودان تهدید به خروج از گروه چهارجانبه کرد.
🔴
گروه چهارجانبه سودان، شامل آمریکا، عربستان، مصر و امارات در تلاش برای ایجاد آتش‌بس بشردوستانه، آتش‌بس و یک روند سیاسی برای پایان دادن به جنگ هستند.
🔴
سازمان ملل متحد از کشور میزبان خواست تا ویزا را مطابق با تعهدات مندرج در توافقنامه مقر سازمان ملل تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149108" target="_blank">📅 12:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9JgsNlqo0-hlnU1jmJdNU0WD9mbAfmLRQyTJZFSelgr_mE91fRmfE1lhbnDZofCIzHQzqjWcJA9UTrxsqNp3qQeJoP7foTh1N7IiFX9TnhfOWV32i9O091BV5YXuaVYU3cD8U50Y98uRim-mvv60kuX__zGqsFobOMhQIbWN97ALZr7BrEc3zeDHOF-YoMdxGpNFt01oCUcHb22EfTTURRVWf3wFZK8Yb4cX0chymu_3Ih9VR4pW3xaYzvz78IKl-ZKiHoqlC9eFWz_1gQMdBi7X2iQSQr9HSg-NWZaRHP2XSperPcIq8zoCaf8iLBL3NJ1hPPd5GBSEgnIA02RCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت ۱۰۶ دلار رو رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149107" target="_blank">📅 12:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
زلزله ۵.۱ ریشتری ترکیه را لرزاند
🔴
مرکز لرزه‌نگاری اروپا و مدیترانه از وقوع زلزله ۵.۱ ریشتری در شرق ترکیه در عمق ۱۰ کیلومتری زمین خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149106" target="_blank">📅 12:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149104">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نان هم بزودی گران خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149104" target="_blank">📅 12:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149103">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
روسیه: با توجه به تهدیدات آمریکا، بازگشت بازرسان آژانس اتمی به ایران ممکن نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149103" target="_blank">📅 12:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149102">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4432d3af9.mp4?token=dl16-h5qSbt1Q4kZm3Aay-agRbR2Psav9ZaNfvuPCPFdPYWMQS_ay5ns4H_a8eJxKT8Rqn2DS-Kn7sKAm7FHPrSWOl7QDSifBpgj1heYfudsjwJo1hUWJJmui0K78je96_VSm_L_y8NjQ3qcdVQtR5u5N3Rgef_H___YNSs8mF3nXSvQ8jOroGJnx_XMIzknWnYXGxlfvKQ-F4TFC2St1h1OqGzck9wKu367xmkXyNamupn3y8lHzJyhyeRMBh67fqdk6pXxFybNTzvNT5z-C-d6X4Ic3igCNEQTTAnkV4oiJK5MsDfcPdEej4gTruXn3Wa_9dhWPFCmPDk04irwzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4432d3af9.mp4?token=dl16-h5qSbt1Q4kZm3Aay-agRbR2Psav9ZaNfvuPCPFdPYWMQS_ay5ns4H_a8eJxKT8Rqn2DS-Kn7sKAm7FHPrSWOl7QDSifBpgj1heYfudsjwJo1hUWJJmui0K78je96_VSm_L_y8NjQ3qcdVQtR5u5N3Rgef_H___YNSs8mF3nXSvQ8jOroGJnx_XMIzknWnYXGxlfvKQ-F4TFC2St1h1OqGzck9wKu367xmkXyNamupn3y8lHzJyhyeRMBh67fqdk6pXxFybNTzvNT5z-C-d6X4Ic3igCNEQTTAnkV4oiJK5MsDfcPdEej4gTruXn3Wa_9dhWPFCmPDk04irwzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ دستور داده بود برای اینکه شی جین پینگ، رئیس جمهور چین رو بترسونن، جنگنده‌های B-1 تو ارتفاع کم از بالاسرشون رد بشن.
🔴
اما داستان برعکس شد و خودش سورپرایز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149102" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149101">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست‌وزیر پاکستان: بعد از امضای یادداشت تفاهم میان ایران و آمریکا، اتفاقات غیر قابل انتظاری به وقوع پیوست
🔴
اسلام‌آباد ناامید نیست؛ تمام تلاش‌های ما بر روی پیش‌برد میانجی‌گری و توقف جنگ در منطقه متمرکز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149101" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149100">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEaoDbWwS9VXBswTNw-yRoQlv9kMUA23NOJmM-X1wvQAsQWs6qqkb8qc1IfpDzyrZegGn3U_lOS9Td8x3OqVjTgHCU325Rd4BcyVucNyAUzYtONZC9pmui9zzNDblc5yMgtEtdOFBsrF0YOkglJL4qTb7F2KpnxTFlOXuNiCLMy3RL8edHfTykbgSDJPMY_qn15O9Xbo9-iyPWU2QPwCpUT_-zX1ooenkhyYTws_0nwyMjLtVIQx7XV_SRxsrED_lytDEbLr376bcfoyJgP9IAH5bYhauzc45CrDTl_JLEjRaR0w8h9MIIKvN_BJzFagQ27vqkpNMgHucc1dWco-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت خام برنت همچنان در حال افزایش است و به ۱۰۵ دلار برای هر بشکه رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149100" target="_blank">📅 11:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149099">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رونمایی از گجت هوش مصنوعی Muse توسط «مارک زاکربرگ» در مراسم کانکت ۲۰۲۶
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149099" target="_blank">📅 11:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149098">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
رسانه‌های اماراتی : در حملات موشکی حوثی‌ها به شهر‌های تعز و صعده، ۹۸ نفر از نیروهای وفادار به عربستان سعودی کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149098" target="_blank">📅 11:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149097">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diz1O0rGlwYmqISgb87QPeFmVtwnAhtqtgXVY5dBhSTn_83qOwsDKwhsd2-60pHUDFbdTcnaQb32FJ-zQeT0Q7juK-vBgNqVYeDuWVsqcA12ZA7f2UZODjuefDntb4ibRaIIfcH7MTlOaiM8wEtpY9AtzCC2tHEBipI92-1p6rLnPWsEuHsj3D2Jj7k-KfQ7JqvMlslIxPwSHnATAOqG5pFz-aAUHmhR84Zm4QqNM7DKRTb6qW_C_Yp-qxcFlxHffzdtBoKiVULgIaxIzihIlZNtTzK9isGPq5KdKOCfJ4AnPkSwW8q7Gbb7se5EgSu8CDG30pj5gNcmFwct71ZU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرایط امنیتی در نزدیکی محل اقامت نتانیاهو در نیویورک
🔴
پلیس و منابع آمریکا گفتند که یک گروه سه نفره مشکوک در حال خروج از یک چاه فاضلاب، تنها چند قدم دورتر از هتلی که قرار است بنیامین نتانیاهو، نخست وزیر اسرائیل، در آن اقامت داشته باشد، مشاهده شدند.
🔴
مقامات شهر نیویورک اعلام کردند که این سه مرد ناشناس حدود ساعت ۴:۳۵ صبح در حال بالا رفتن از چاه فاضلاب در خیابان پارک، مشاهده شدند.
🔴
پلیس اعلام کرد که آن‌ها با دو وسیله نقلیه فرار کردند.
🔴
پلیس نیویورک در بیانیه‌ای اعلام کرد: «با توجه به مجمع عمومی سازمان ملل و حساسیت محل، به دلیل احتیاط فراوان، پلیس نیویورک در حال انجام بررسی‌های امنیتی بیشتر با شرکای فدرال خود است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149097" target="_blank">📅 11:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149096">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
آکسیوس: ایران از طریق مذاکرات غیرمستقیم پیشنهاد داده است در صورت کاهش فشار نظامی آمریکا و لغو محاصره بنادر ایران، تنگه هرمز را ظرف یک هفته بازگشایی کند.
🔴
با این حال، آمریکا این پیشنهاد را رد کرده و گفته است ایران کنترل تنگه هرمز را در اختیار ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149096" target="_blank">📅 11:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149095">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiAGfNBKbU8kDIObu5fyr4RXZBBsuHNS-UpKmcQrl28-O3OG25TTdl7OeK8rA81t1NIQHlkuz13D48g46mPPMRQ2ZaHuzDjKvOPOgtgUziq5msyjS65HFAoFY42YPw-Sv3o9IvjdFwCUZLZqG4gG48RrNokLC4TTMlDvL4UgWb_FO7ksR41uDo6cDJ2HLk4htx4l5QyVvTWJxn_C7mXaHmOFd689Rjv2GWUDPLqYiC1SfQfRhDkUj1LSJcbk27ay5temQDvo2CX7PlWTt181zi3DvabcOpv3IjRApcCgiwlUuBpnT45fnA2Ea0U0Jbq7vBY-cxVjm0CkzoZ6l7xNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل، منطقه المنصوری در جنوب لبنان را هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149095" target="_blank">📅 11:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149094">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل خطاب به اردوغان: دست از درگیری با اسرائیل بردار
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149094" target="_blank">📅 11:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149093">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انگلیس محدودیت‌های مالی علیه ۵ بانک ایرانی را تشدید کرد
🔴
دولت انگلیس محدودیت‌های مالی علیه پنج بانک ایرانی در این کشور را تشدید کرد.
🔴
این تصمیم بانک سپه، ملی بانک پی‌ال‌سی، بانک صادرات، پرشیا اینترنشنال بانک و بانک تجارت را شامل می‌شود.
🔴
وزارت خزانه‌داری انگلیس اعلام کرد که درخواست‌های این بانک‌ها تنها در موارد الزام قانونی یا شرایط «استثنایی و فوری» بررسی خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/149093" target="_blank">📅 11:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4zlhTAEneTHi-YzI3h_Ld_fjO1eC7ADZ2ziZ68GUAJojM6-jXs_HZqTrxO-82wez-ThaAQc_UV1Y-rqBZ4XmH18JrsPDII1rFZUNv9DoGddvnoNrmqJwtrhp-3OGciSuKxaddkaV2pl7ecuZx3MyXZt-4CIDy9xAHr-Tspk9MqU9ATxhvu8pkCzzUb-WTjAZ7A0vVRC89ZrZFBBCxYlb7_zo8OCBS4tkxMM2kqL05FdNaFQUjXLuiZFDogazh-TuT_s5aD9TRNxpgWFJWnPh6YIbEIbPX0QqcVULUvatm3cAuryWZtnDrOn-1rrr-i3SAb0ypvdxelbzmdWYHwXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیشب خواهران جانفدارو بردن تو سنگر بهشون آموزش کار با سلاح بدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/149091" target="_blank">📅 11:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUk9yISP5s4rbWRIrpnfAWIzvduBGNUMDhHUKtiACbPn6vZw_7-GuwcLmfW0Sy_CC7z2x_u3WzlD9uQ7WNmJu02gVuNhBOsdX5IsOSQxcxxkv3CVAhlZ1vIUR7Smx6vtVnMRmP1eHvifemUQDCs8QTA39ceXf0cfRw_Aauo38Dg5r-kr34g3njBRpgb7HhqWH5MFIap1fGxail_J9n57A2fSvO6U4uJYf6D_7Q5ZWdDRDVb1wZGHbXYsT0NF5tZuDK5he_eKsEbWuV1iMTZMFNnLtxvkDGHFtvWkdJ5WvjHBZdhgqXevhHZz3j7G0D6H2GQ8scLKyXa8rpbfwF_nHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل: فرمانده حماس که در نگهداری ۷ گروگان اسرائیلی نقش داشت، کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149090" target="_blank">📅 11:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149086">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I-nVUw_NTYH2izcRxO_9TsbrrDij7-ZFxZrZRFDP4ddrC9yU--E5WblDRxTGgKIZU37w4cnvzh6YnuFgjmkT0v_jjiV30Mo6NIi2t5jyJuOdbu7njMaReaRVF3bQjvaFAaEwUGDYHgxKyao2xkqZPzCcMw4jln0-WF42n77RjYN0TF6pZHpg6fvXwBGDhFPcA-6x_QhxcjRHY3EHVpRIL_8wWRwa__k5SEDfDn7a87mMrI_IgXOEL-GoXqyrf-IOixgEl-LLQJYx1oqONQxve8hSyqNxPdTjg1NHHHhpvaimpavPYDyxOuxKQQtaH8qV7UOFsMeVm01XcNz3ROPc8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ArvBCEde59xIpE4EAHNax5DR9BkjoMwpDLqluLg7rir1MdAqbhSqAKWa4IFsxUhWTpLnpbTJTsC--DFrl5WSWdIiOasnn5mAOW-TAjjWhBoURwd0xL_O8Vf90_6AVezl-KnjUwUQvZfPLUWuZrQff1uLbtTBdT25V-mFxFLD2Gvl9kFpG8JtHLUbWAmfLI_lWIH4_YlCxfk8mEA_L9cyJ2cfdE_hD8szxZRmmZ3oM3ugcIkgmES9aoX_KzzP0VP-SNnDvJY0rLKL_V5k4QY2WvYTVPovS_QyIXc6Kmq974BMyF3UAynsbMnElfsLTwVi8-oBNvXQW_uEhSgNaf9nwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M8684JC7NqYSYavMbXsBqcNVWZzbnAyMKCW2CdVlZ2dAdlnkdDUWFqP9qjPpckROjTXsu3Ers-aMDLkwX6Ei1g3ynkGwYmGoRTxNFZB3rLDEPEXbm63PwrQWnK7gl4yMNCbEl1O5rwioPsCy6mj5g1TPsZkLNPHrq-5JK08P4Sc8owhf08b09dzxBSWRtqFq9GejpLWvjLnhu2hgAMxyLvbeK4OvdTHvw3Bd_bMLe659BxKn9Vsfr7HWCDcPhU09bxUYjhagBn8f2lI89QIyS0tYhjMv8Wo8usQY8N_ewriitZJVI5xAfH8L3DpZGOc3K-ovDI1oi4j2PSXNVS4SzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n4GEWsQ-pATsORuvr8eJZEUBPu76tSbzhVeK55cGqwCL4gvyYYoWLU-x2pjJKXQMrgs59sqamHXowpaS2iWEwYnkhi974fZMRPYMF1EGHU8t_cBVqkGdb_D7olbBWy2Vgr6z1rhMqvZEHfhKIYx9MhEM1_Q6QSp7HqhLa-vMKhMtFnUoew1sn3kLK1W65VyEYBHhHQUzwcn0SsCOYxF0Z3aSvM4S4j9K1tD8uKuHQ_ObqUsZD5749xOGizCjzzSoqY1LflQrK_yD4MJCyoCO1DIHHqdOjdtUTS3CsMxic5mEYCfgghLxbTHh8I5Pk8aFgeYqZjGsMqQk25BszHFcOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سی‌ان‌ان : متن کامل نامه کائو، سرپرست وزارت نیروی دریایی آمریکا، را منتشر کرده است
🔴
اشاره به تلاش‌های ناموفق برای خودکشی در صفحه دوم نامه آمده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149086" target="_blank">📅 10:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149085">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پزشکیان: در مجمع عمومی سازمان‌ملل از حقانیت ملت ایران دفاع کردم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/149085" target="_blank">📅 10:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149084">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ایران در مذاکرات غیرمستقیم با آمریکا در نیویورک به واشنگتن یک هفته مهلت داد تا با خواسته‌های تهران موافقت کرده و تنگه هرمز را بازگشایی کند.
🔴
با این حال، مذاکره‌کنندگان آمریکایی این درخواست را قاطعانه رد کردند و گفتند ایران کنترل تنگه هرمز را در اختیار ندارد و درباره اهرم فشار و قدرت چانه‌زنی تهران نیز ابراز تردید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149084" target="_blank">📅 10:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149083">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihp4AGz32DQ_b8s1PlU9IAgb27OCRIE5KfKI6DDyDLKtEHltP2y-YNTOHnf0aBlcuvG3unGMT421XR-BTA0RiOMx__nbuzpcDIM5lck-0aYMHRmnl3Fmy9Q5HX8fYO-4YT-2rwKsEIS4ahP6cHj5qw9Kh2iLd7vDhhWEVqq8jTpSJWVaE_2WqKgTpqLh6H6KXaTC_dFcOgVhHDGTXAiS9SuaE042vTJTFbGmQ9gulfyN_U9cPqa-E8ElIrgcYB1AUKL1O2rIBCcVttWDIGulXD7l9ifLuNxDlyxWiypE7gqIjUDCFRTm6TprhaGXZ9s2UdSGi_YcHzFO3WyYJ3y3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ال‌موندو: سیا به چند دولت اروپایی درباره حملات احتمالی پهپادی روسیه علیه کشورهای مدیترانه‌ای از جمله اسپانیا، فرانسه و ایتالیا هشدار داده است.
🔴
بر اساس این گزارش، روسیه ممکن است پهپادهای Gerbera را داخل کانتینرهای کشتی‌های تجاری پنهان کرده و از آب‌های بین‌المللی به سمت اهداف پرتاب کند.
🔴
مقام‌های اروپایی معتقدند هدف احتمالی این حملات، تضعیف حمایت از اوکراین، ایجاد شکاف در ناتو و افزایش نگرانی عمومی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149083" target="_blank">📅 10:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149082">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0NjR30mBx3aCTcbouSR5fHljpnpeOlB80JLMoBCV15nX4yUnonhOJMPegPqmZ__GqDaZIBvwfBM_tWpDiP9VK3gYQ3Hk5ORDNmxLaTkok50eU44rVVo2M4aBSfoJx1ZJ5c01xXs5IoCU3aZfSLZFRJygzsbE6pA4OC_rUNflOCgXmYgcMwcqLK_AWmdf-2ELVaTsaL_LCxri-0ZWw3AwXZ1o87wkuAcoTn-4nWntu4g9EMig7L5S0RxEVBEaHzo-Qan31Bnm2cM-NztIbe-3U_fyXH9FZlKY-yl5AXaz_EEMCV-ZFbmFuueIQ19k8wh0yEbXYnvGVWgp8y-5TGNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ در تروث‌سوشال:
«روز بزرگی برای بوئینگ و تولیدات آمریکایی!
🔴
امروز ترکیه و بنگلادش خرید مجموعاً ۱۱۱ فروند هواپیمای بوئینگ را اعلام کردند و گزینه خرید ۵۰ فروند دیگر را نیز در اختیار دارند.
🔴
این قراردادها به معنای ده‌ها میلیارد دلار فروش و افزایش صادرات آمریکا و حمایت از ده‌ها هزار شغل آمریکایی در سراسر کشور است.
🔴
وقتی در آمریکا تولید کنید، از آمریکا صادر کنید و از کارگران آمریکایی حمایت کنید، شرکت خود را قدرتمندتر می‌کنید.
🔴
به بوئینگ و نیروی کار فوق‌العاده آن تبریک می‌گویم!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149082" target="_blank">📅 10:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149081">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
پزشکیان: وقتی سخنرانی ترامپ در سازمان ملل را شنیدیم، نگاهمان از متنی که از پیش آماده کرده بودیم تا در مجمع عمومی قرائت کنیم، فراتر رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149081" target="_blank">📅 10:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149080">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/842589bc02.mp4?token=Br-q28gpnYDzKwxQFAwssbY86-xCyAcM32yG-qrp2HOUSFb6Z7IDF8zz7fVFLhDzZ4WnoAnYXPmdX9OCgzBMuQXJ3crJ7SE6PcmLY_FEofCJUbBz-wW2uwEpG9wRldwIavgyj9od2sDRXjS3pXOnn6YAt1HCpW9jiafKYISfUrTvN3DgaSa1TVNyITKP8nrW8iitJULuPDCAGdSTRHS9R80TXHubjVVuYb6b6VgqQ3dPwkjt2KucKYNsK6loxh67CLt66IofnKbal_ZeU20MvkGxjcAn61A8IVaMxKJO12r_gHz7Q2_vcA9Z4FAgE4FF0MLD0hzuvg16cG1TxZwnPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/842589bc02.mp4?token=Br-q28gpnYDzKwxQFAwssbY86-xCyAcM32yG-qrp2HOUSFb6Z7IDF8zz7fVFLhDzZ4WnoAnYXPmdX9OCgzBMuQXJ3crJ7SE6PcmLY_FEofCJUbBz-wW2uwEpG9wRldwIavgyj9od2sDRXjS3pXOnn6YAt1HCpW9jiafKYISfUrTvN3DgaSa1TVNyITKP8nrW8iitJULuPDCAGdSTRHS9R80TXHubjVVuYb6b6VgqQ3dPwkjt2KucKYNsK6loxh67CLt66IofnKbal_ZeU20MvkGxjcAn61A8IVaMxKJO12r_gHz7Q2_vcA9Z4FAgE4FF0MLD0hzuvg16cG1TxZwnPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله پهپاد شاهد-۱۳۶ به سوران در اقلیم کردستان عراق منتشر شده است.
🔴
این حمله در حومه شهر سوران انجام شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149080" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149079">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نیروی دریایی آمریکا: ۸ ملوان ناو هواپیمابر «آبراهام لینکلن» در جریان مأموریت طولانی این ناو در جنگ علیه ایران، اقدام به خودکشی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149079" target="_blank">📅 10:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149078">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFmH7vXY_Bm5PjlHQPZ4r11j7fYtiOuqHULkD3uatEPYXfNx8cBQgYiMDS2uJkvr6NEx37XF2N-xP4RtPtop9I48tl8QhxrKOLmaF39Y01Lwvq30LJnq7NHiTWoZ-52Q5Qa9Z9kIFmD9sxTYlmA-uux4KKCE9Ti_ghriyR17kCDyb6Vgv3bFrrbVIa5J-35Pho3pND_UPhXB3EiyA84Xi82OIwEjeZQwMSxgEtMiNpjR5vmANfVy-EDChwuNkqmgEJOrcWAKIKyZeqRlxiAvbqqZ06bKExpR8-PR5VIsDBUKI_rSM_p_sYl5NCTvbJ13HThuzgUXKiJ_ZKpkTCpD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: «این ادعا که کاخ سفید یا من می‌خواهیم نام من را بر تئاتر فورد در واشنگتن دی‌سی، جایی که آبراهام لینکلن ترور شد، بگذاریم، یک دروغ مضحک است. این خبر جعلی است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149078" target="_blank">📅 09:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149077">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
صدای شنیده شده در آبادان به‌دلیل نقص فنی در پالایشگاه است
‏
🔴
استانداری خوزستان: صدای شنیده‌شده در برخی مناطق شهری آبادان به‌دلیل نقص فنی در یکی از واحدهای صنعتی پالایشگاه است.
‏
🔴
متخصصان درحال برطرف کردن مشکل هستند. هیچ‌گونه خللی در تولید بنزین ایجاد نخواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149077" target="_blank">📅 09:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149076">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
زلنسکی: طرح آمریکا شامل آتش‌بس درباره تأسیسات انرژی و بازگشایی کریدور غلات است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149076" target="_blank">📅 09:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149075">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8b8f260d.mp4?token=dTDkLDtP8NjUZmt7EQZkHRd-0hq7jz1AJGVL3h9gRUbWZP5AUxev-JAeYuuAEppVzG6MJN03MS1L7JP7YB-iv8yhbRbk6UTOfetjhNymq0IQD4UiloflTFgU5S5mpOMGri_CKxoYbknN6lzHkVcG5Nbx6QLODEMnXvtqM7R9QyiPxpAqwRIaYVDGmNuHykewFfyXM25TE0SeSZmRAfDf8W8-x7R-OB-3nKBcAbsz24nFIkPLgpFnlCbmheE4b0auL2fBE89_qeFrbGkpWau3Y2NvCxQmAO1v1UNEcKjSm6OCI48kxjkgs_5GrOXE6iXW4s_6hozDgmURNEvV7mh6t1rdIxI1Zg20E4V7iWqRndudXpLQMxJ055rIQNfeyfQgVyvhlSubIgC4SJGJsKONUfzrO0YMSfmzrpK_0TD_WworUwMCG5hyUFp34SBfcPPlfZjmezBgYo9cdoFSrdlNet0PLNSkdsra8FzPFmsl5fLbzEFbkt9YgYE6dGZ9SQonXObDGCjG2IEE9Zoc5eOfDhe8l9EImJ6rwK-Rq8TVVk0jl_Jc12Actkc64_Og2quctCfBoqfNgwMlYf7-sX26cyHBqvcS2kO3gjSVc_gr5HfTzdCJOO9ZTRfEsc309ql-84mA0B71lUUKAxRkFPTDI-8YZFpNqxASTJ396tpksbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8b8f260d.mp4?token=dTDkLDtP8NjUZmt7EQZkHRd-0hq7jz1AJGVL3h9gRUbWZP5AUxev-JAeYuuAEppVzG6MJN03MS1L7JP7YB-iv8yhbRbk6UTOfetjhNymq0IQD4UiloflTFgU5S5mpOMGri_CKxoYbknN6lzHkVcG5Nbx6QLODEMnXvtqM7R9QyiPxpAqwRIaYVDGmNuHykewFfyXM25TE0SeSZmRAfDf8W8-x7R-OB-3nKBcAbsz24nFIkPLgpFnlCbmheE4b0auL2fBE89_qeFrbGkpWau3Y2NvCxQmAO1v1UNEcKjSm6OCI48kxjkgs_5GrOXE6iXW4s_6hozDgmURNEvV7mh6t1rdIxI1Zg20E4V7iWqRndudXpLQMxJ055rIQNfeyfQgVyvhlSubIgC4SJGJsKONUfzrO0YMSfmzrpK_0TD_WworUwMCG5hyUFp34SBfcPPlfZjmezBgYo9cdoFSrdlNet0PLNSkdsra8FzPFmsl5fLbzEFbkt9YgYE6dGZ9SQonXObDGCjG2IEE9Zoc5eOfDhe8l9EImJ6rwK-Rq8TVVk0jl_Jc12Actkc64_Og2quctCfBoqfNgwMlYf7-sX26cyHBqvcS2kO3gjSVc_gr5HfTzdCJOO9ZTRfEsc309ql-84mA0B71lUUKAxRkFPTDI-8YZFpNqxASTJ396tpksbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا: «برخی تلاش می‌کنند در امور داخلی ونزوئلا مداخله کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149075" target="_blank">📅 09:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: احتمالاً بیش از ۸۰ یا ۹۰ درصد پرواز های خارجی ایران لغو شده‌اند
🔴
حتی مطمئن نیستم نمایندگان ایران در سازمان ملل چطور قرار است به کشورشان برگردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/149074" target="_blank">📅 09:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149071">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BOC9FPdRC0W53f7Y3SHQrMjy97TuCmheLXn_2RVoarafyfUKcPz2tUtDK7flnf24OZZjiPOT7gFbbmIAJKKv5CLAJ4foOfdaPwMAl8pT-IBJkG-k2pwzwswZOnY348IZI3koOsHI7gmJxbB0tOvn7wKHjjEORy-DG3Q5l2BGvZxsV6afQRFmcg5Qh8UE3N-gCn5Pjz1VsI9Q2wYv8l5bKvyuD7uRkUjY4LIf1HfTm5JiL8IsXjCLYs_8hUWElK9BSOADiTp5fcClBS3TrI9x-8x6DVuP8N5W18aOvP8TY9jTHPGeY3Mdt_XAnYbeQjuuBABfPAeRWGlq7ptKdxaJMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SETEGBHasUUoVmhSbCFOOkC9uNUY0hJ1m0ZBCgtUz9ZMEdxJ0DV0Tjezvigf4sGMA7uxz13ElBO3vlScj-o_QpIFNXF6zdf85aiDTlfnS06BmeXSvDgUDiCp0Xum8uIcXmqX2mq59ik7WYwzhrFg9LWVpAypyn5EZ36dA4UBwmCtmdHoMJM81cyltAJLJ-GIlzcgxwGN9VTmi0kQ_4c6KO310s7V2GZ-yDioRPjro4r87wTV74ek3tMoJQ4dCf0JwRFck1GLGdtsar1UBSWR8CD9G4LdySV8H5MB4OxnLgymuSXTkF7jpebKlLGI2TpUFDMob9jeVFSWWWIGPfk5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6dAAGCj_QvVv7-1ggh_oyCpSB3dNyYKThPfnB4RWhRK_36VN1_EY6uYiR9iNjiANuZp8_ZPG4k-JWQ1subP9ZKHgzcDdXXOVVYHv0n_w32h6CjujOuN8jBcYW1-_hIx970lEzoeBUGr6okefOg2sXqjY0G0ipGr2iffM6tNnfhPXJjRTjUzvYFCrUdKYO_Gma4yNJJ9S5dW9h-PdZ9vtzQgE6GgqUrW4tIpFQ4aBIEv25t8ycy6uHAhYN_b9amealwGBmAF5VIHPHpcTd8dMxWRV9Q5CJUrX09viiJkYSECTmy3fxQQwzDzCbqgMmgeuhTcgtT6nHJvBspgvyDU0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از حملات هوایی پاکستان علیه استان قندهار در افغانستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149071" target="_blank">📅 09:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149070">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وال استریت ژورنال: چین در طول جنگ علیه ایران، قطعاتی که در ساخت پهپادها و موشک‌های بالستیک مورد استفاده قرار می‌گیرند را برای تهران تأمین کرده
🔴
پکن تنها چند روز پیش از آغاز جنگ، ۳۰۰ تن ترکیبات شیمیایی به ایران ارسال کرده
🔴
در شش ماه نخست سال ۲۰۲۶، حدود ۱۳۰۰ محموله از قطعات دو منظوره از چین به ایران فرستاده شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/149070" target="_blank">📅 09:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149069">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
انجمن داروسازان ایران: استامینوفن کدئین کمیاب شده؛این دارو اکنون به‌صورت محدود و سهمیه‌ای در داروخانه‌ها توزیع می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/149069" target="_blank">📅 09:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149068">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5877224c5.mp4?token=HapXfOV7VKeTWjEsyudAJlEzu0hljoYGpyQIr09mDYv_moUot23XPvZrXr83MX2QGIlS91gKAlaKDtLKvDjb-ZNul6_Jg4IvTQctp1mxoj2f7egKMPtsJPnbzEsj-Q5Nr_6KQ4ifgbf7cNWNA9XgcyN1DLblm4dpXKywM6yFQx8TtB1V41lrgH5pa5IEodujfRiw8hb6QGDeUFmkoCgQ6I_s8G64ajuf9qkzfbGMuAuvlNe2xTU8japqHPJgt7j5iKi3ZjMdDA1UclBnsEl4nAFOLbisP_Nzgs_m3IEa-fu1B57OlfcUIGQXnPFBcjwEbJi33KwjF4AseaZUfyiLTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5877224c5.mp4?token=HapXfOV7VKeTWjEsyudAJlEzu0hljoYGpyQIr09mDYv_moUot23XPvZrXr83MX2QGIlS91gKAlaKDtLKvDjb-ZNul6_Jg4IvTQctp1mxoj2f7egKMPtsJPnbzEsj-Q5Nr_6KQ4ifgbf7cNWNA9XgcyN1DLblm4dpXKywM6yFQx8TtB1V41lrgH5pa5IEodujfRiw8hb6QGDeUFmkoCgQ6I_s8G64ajuf9qkzfbGMuAuvlNe2xTU8japqHPJgt7j5iKi3ZjMdDA1UclBnsEl4nAFOLbisP_Nzgs_m3IEa-fu1B57OlfcUIGQXnPFBcjwEbJi33KwjF4AseaZUfyiLTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویری از هدف قرار گرفتن یک کشتی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/149068" target="_blank">📅 08:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149067">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYx0XHl4iOnRaoscR00H3YeVpXT34AW0J2NTXOXyADlpzsLBhQ5alSqug_gwiaSflZKpjchlhfT1a80d3rwaM6zUwCkO4x-0CFNnrKjUQfEKW8866ws0ydva52nTTxLjY4T_aZ2nRcsc7APxPvyPlxgbE6W9mPl4zZbaoSssfJ80wvGO3mmh-mLFggg-1vFCpNeU3spb68XKFdtQLyx9w0SAQNkltdtnEygtnTfMoD6ZIQVIeh1SC7KDdzdBe21Q57PI7UTpz64dFfSSqWYdqzJQGu-cJKNkexSd6QnTn8HaDm8LMlpwL8KW4x86blFqKzZCVLeEfBbCtC9-DCwmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار عراقچی و وزیر خارجه اوکراین در حاشیه مجمع عمومی سازمان ملل
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/149067" target="_blank">📅 08:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149066">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dfdf05f7a6.mp4?token=Vrd67Z2Lz1nLeWKiyLLNyg0g8pS9h01kWcBMtZqKlM94yEFqwEloc7e9k4drR5hl1zXolyIWnv5lzCG66csgAYKfslniNZ3uH0Eo5KuI0zdGS4GVO9mRph_JYDPFRL7AX64I_ZXmevUK1XgxA45A0h1bP-C_txEY2ouEfcaIy4pr1KDh1lZX8fqvxFiibxK6Lby0V8d8_8qe7SP6GXjSVvPfWF9IqGUEE-A-R8NRNn25Bn7kLmajGl64rppMvfFOZZbkmS3tCQbSnVcQTTFWNmLJ7TxgeTPQYOBk5CMkyTUxKNCw89YuN37ka5ilhqNqQIi-FN2MSfnwfEOOWM7vJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dfdf05f7a6.mp4?token=Vrd67Z2Lz1nLeWKiyLLNyg0g8pS9h01kWcBMtZqKlM94yEFqwEloc7e9k4drR5hl1zXolyIWnv5lzCG66csgAYKfslniNZ3uH0Eo5KuI0zdGS4GVO9mRph_JYDPFRL7AX64I_ZXmevUK1XgxA45A0h1bP-C_txEY2ouEfcaIy4pr1KDh1lZX8fqvxFiibxK6Lby0V8d8_8qe7SP6GXjSVvPfWF9IqGUEE-A-R8NRNn25Bn7kLmajGl64rppMvfFOZZbkmS3tCQbSnVcQTTFWNmLJ7TxgeTPQYOBk5CMkyTUxKNCw89YuN37ka5ilhqNqQIi-FN2MSfnwfEOOWM7vJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی پاکستان به افغانستان
‏
🔴
جنگنده‌های پاکستانی در حداقل ۳ نوبت نقاطی در شهر و ولایت قندهار در جنوب افغانستان را بمباران کردند. شهر قندهار محل استقرار هبت‌الله آخوندزاده، رهبر طالبان، به شمار می‌رود.
‏
🔴
گفته می‌شود مجتمع ملا عمر، بنیانگذار طالبان نیز هدف این حملات هوایی قرار گرفته است. به گفته منابع غیررسمی، علاوه بر ولایت قندهار، ولایات پکتیا و خوست نیز بمباران شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/149066" target="_blank">📅 08:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149065">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hns-A81VmtXstJ3hgyVoJTcWRpA-UNp8AzkgzOdZTTtXEeWoF7dy07CVz2_va8X8IYb5kocqKu23rFscx7PRDfDWf4TisRqaFTZ69QBdnyGSiUs3XvrR8pyOzVzyumTc05afYe591fph82rYfXDR_x-sXwvE8YWRBn0-g9suH2DWttZnKdXefdm1Ax7Ewa0gtY0KEwIIVOHURwvrQO3PA53LFOmfPczGOTkvxwXZnbX2Cch_bX8W60-KEqQtukiOW9tV2fcGircOZlEUDAHIEKgx2uwNETioD5d1pwknLgtqRMRIgdFOo8gLZoqeBcoQmJgKQK9WYRqBi3l_4J9pQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ اعلام کرد که با شی جین پینگ رئیس جمهور چین درباره ایران و بسیاری از موضوعات دیگر صحبت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/149065" target="_blank">📅 08:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149064">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fdf1eb3d.mp4?token=L9mL9INT4bvoMS55Kd6WURATCJw1LeS2OKs2yBEL-6MyCm_SLvcKDvpGZsKZGhMJTG8X0SYUMz_4i5A2I_fQUXRGEqytP2IpTt4eZ8E7UN3nPdKVhdmZIXF2bPZT6O4JBRTligxHgERjEZeIHutu3HJxPLogxEHVGjQ9GModFhDzT9Mk0GU3MoOIBd1mVpKWGthh5dAs-kypUt2rTQ5yi0IcV2eUAVPnvuAm0UpUMvsjhaSHFZqkK4fv1YLb83ruus_54vRxtSXqDAGz4SEC0--MXnTguRfyt0YwdIYVeESS6BsMuz6kM3BU21dWtqJZzoASqe2-dNp50OX9XfhM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fdf1eb3d.mp4?token=L9mL9INT4bvoMS55Kd6WURATCJw1LeS2OKs2yBEL-6MyCm_SLvcKDvpGZsKZGhMJTG8X0SYUMz_4i5A2I_fQUXRGEqytP2IpTt4eZ8E7UN3nPdKVhdmZIXF2bPZT6O4JBRTligxHgERjEZeIHutu3HJxPLogxEHVGjQ9GModFhDzT9Mk0GU3MoOIBd1mVpKWGthh5dAs-kypUt2rTQ5yi0IcV2eUAVPnvuAm0UpUMvsjhaSHFZqkK4fv1YLb83ruus_54vRxtSXqDAGz4SEC0--MXnTguRfyt0YwdIYVeESS6BsMuz6kM3BU21dWtqJZzoASqe2-dNp50OX9XfhM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی با همتای پاکستانی خود دیدار و گفت‌وگو کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/alonews/149064" target="_blank">📅 08:34 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
