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
<img src="https://cdn4.telesco.pe/file/JV41u49pICKvxhtDZUmkLpYUSvjOzg2peqlHugpy8sLZ7cnVeQil0gqkQ8gaD0G3KFCDAzTqiaCoPDQD5cxfUBXEuODQHdq0BI7Zq2vMWw5LfXu10RRY2jg0ChA4jnFPgjtbFxfYb6m1rIjovPlgvipke9PWJPyQ7tWHVkaOgPUW9BNsmoMLDuVEkcxdP5nFhNgN_KEUfIV43tWA05hHob9TdvXzxCFXYbneMgHlWm06pAkKqdfFda_CagrRRMqVKYT-ik0uA2fKUoRGt8GLRnNQ10CLkWOWJ9aQ0iPJFEb4t9O0xFVC9WNkQzTHO5NwtUs6E6q96VISXCRTYF4NxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 941K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 21:39:50</div>
<hr>

<div class="tg-post" id="msg-130224">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=Lt8VFn-WWVnHSLV4e6jYHbWZIz6gopTHLqJA7AjSzRUtEu1IOnPf1LMKfjOKSKe-_men-vZkTotwCC3y1gpOqk0WVbfgmrfGgUT8KHJdDcagGwFcdgVTNJmz7108ZsqIhlTSawFsNlN0DENJM4V7kdIBMlVe-ws06_BPcbx-bkYKnXAmn7rVICLO_PtOwiMVs0e88MW1otZ2QPF6uj0-9971l32n0r5WXd9Ovz7JBji2vRWYsHugtMR0RLQoVpQdEwXrCwiPkWUC-ApynyCW0VKiKirm6xlGi1xWTyTEeigOMSi6OELUMrUxxRTKN4qoxrNhcMuhxxsMOTQAgWJyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=Lt8VFn-WWVnHSLV4e6jYHbWZIz6gopTHLqJA7AjSzRUtEu1IOnPf1LMKfjOKSKe-_men-vZkTotwCC3y1gpOqk0WVbfgmrfGgUT8KHJdDcagGwFcdgVTNJmz7108ZsqIhlTSawFsNlN0DENJM4V7kdIBMlVe-ws06_BPcbx-bkYKnXAmn7rVICLO_PtOwiMVs0e88MW1otZ2QPF6uj0-9971l32n0r5WXd9Ovz7JBji2vRWYsHugtMR0RLQoVpQdEwXrCwiPkWUC-ApynyCW0VKiKirm6xlGi1xWTyTEeigOMSi6OELUMrUxxRTKN4qoxrNhcMuhxxsMOTQAgWJyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/alonews/130224" target="_blank">📅 21:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر دفاع اسراییل: هر دلاری که وارد خزانه ایران می‌شود به موشک یا پهپاد تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130223" target="_blank">📅 21:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، ولودیمیر زلنسکی اعلام کرد که عملیات ۴۰ روزه سرویس امنیتی را با هدف اثرگذاری بر کشور متجاوز تأیید کرده است؛ عملیاتی که به گفته او برای وادار کردن طرف مقابل به پایان دادن به جنگ طراحی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/130222" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
فوری / برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/130221" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
وال استریت ژورنال: تهران در مذاکرات با چین و مصر، پیشنهاد خود برای وضع عوارض خدمات بر عبور از تنگه هرمز را مورد بحث قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/130220" target="_blank">📅 20:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130219" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
به گزارش نشریه NRC، هلند در قراردادی به ارزش ۲۵۰ میلیون یورو، هزینه خرید ۷۰۰ موشک کروز روتا بلاک ۲ را برای اوکراین تأمین خواهد کرد.
🔴
این موشک‌ها که توسط شرکت هلندی Destinus ساخته شده‌اند، بردی حدود ۵۰۰ کیلومتر دارند، کلاهکی به وزن ۲۵۰ کیلوگرم حمل می‌کنند و از هوش مصنوعی برای تشخیص هدف استفاده می‌کنند.
🔴
مقامات اوکراینی اظهار داشتند که این موشک‌ها از حملات به اهداف نظامی با اولویت بالا در عمق خاک روسیه پشتیبانی خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/130218" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بازی جی‌تی‌ای۶ در کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه، تاجیکستان و تایوان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130217" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130216">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYysEOb_pbbzczw9oTBPiUq06YuRcdm-pBaWSx2Gn9je9A6osuDcvFj3XDQZD1pPx4IfnUN14K2QvaLhgwlj40O4tIxKBk-VlmkKBEuXyRslUVhvgGEw2T7OWcRD3u0GWcn3HvnO-koRu2zJhd5hVmRbJ4h0qO0e3Vm6BSUzUsO0z7iYRlwz2d-zmpwokzN_Ac94snGTrAOrZe5I4MkTODZNMyvcE-HdD2mvNP6L2Y_pF-i86rn1HMNtc1ZTh88-km7Ib32mewcm5DUJgaL0Ys2yIQlq0v0qm7r9fyAMhhuGRUk99pLD5II6ISXEsTsWIKcMvCkiRTae1WKs0gxLow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظر سنجی فاکس نیوز رسانه طرفدار ترامپ و جمهوری خواهان؛
🔴
موفقیت ترامپ در اقتصاد :
🔴
۳۱ درصد موافق
🔴
۶۸ درصد مخالف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130216" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130215" target="_blank">📅 20:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/130214" target="_blank">📅 20:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دبیر کل حزب الله ، نعیم قاسم: صبر ما معادلات را تغییر می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/130213" target="_blank">📅 20:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
نتانیاهو: کارهای بیشتری باید علیه ایران و حماس انجام میشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130212" target="_blank">📅 20:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=PYN-eOAu12AOtIVHmxKT2Vihm1_zc_tlF_VXd4HQPL4u8eKJsYyRxkO_wMo6EPo_J6UB-9n7sBULzjjHCsazIwPtDbh7c-cRbL1M8SqF4L8VUE1n3G-SoGOGINT9D70-XwjSFHP2j5kLAvC4zRUrcbeenNFb_PID-rNcMTsdSFjAZ7rsOqwniURitzhy7t9_GxDcvfNwB7wQqd4PE6bMhh-6mBG-7C3m1gGqsQPdfDqX1HPSIAY8X4bNXY1CRdr9gu77PM9fewzu44FTO1ju8iGVnkrUNJPS2yzfTVGtQtjh2AT6G80CWVJr6sBOAk2Hc3KDamM_PBmWos3xpfo8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=PYN-eOAu12AOtIVHmxKT2Vihm1_zc_tlF_VXd4HQPL4u8eKJsYyRxkO_wMo6EPo_J6UB-9n7sBULzjjHCsazIwPtDbh7c-cRbL1M8SqF4L8VUE1n3G-SoGOGINT9D70-XwjSFHP2j5kLAvC4zRUrcbeenNFb_PID-rNcMTsdSFjAZ7rsOqwniURitzhy7t9_GxDcvfNwB7wQqd4PE6bMhh-6mBG-7C3m1gGqsQPdfDqX1HPSIAY8X4bNXY1CRdr9gu77PM9fewzu44FTO1ju8iGVnkrUNJPS2yzfTVGtQtjh2AT6G80CWVJr6sBOAk2Hc3KDamM_PBmWos3xpfo8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔴
به هیچ وجه اجازه نخواهیم داد ایران
بمب‌های هسته‌ای توسعه دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130211" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130210">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=H4S4Vt0D1Pr4yy_Ur5vBNNigERFHydtHOenMKBaACYYKMETRP0fnK2N8XEotZd7klw056N8T0KRj_g7RTNf72QZy6CmK99S3sl90eS1A-wyCLT3-M6lWpIx8fvHiDabGgIJoTyH9Bp7BjtHa2r3KDHMzf9jUeOATdOL7GoO2rTOTsAd2CR3Hkd4xX_fy4mhornp0U_G1GtYORz5p8GnPv1EQjyttDme37953HT7uTvI5iGjhWLffYrhcwdE6cti9plcZV5XE-r3BzukNAfGbaZXms4vV7nykLea8NEKRIIWKpRJoXHpsmcTz37gdO2_BfBwtKtKk9D73uYj0ZGYNYINlvI3v1eBVb5Ei1I-LGSQ6CqJNa-QsqEHU4O--cPbgt7RZxV7XA3l3u1mB3G3sJ5_KrZB7jjQQFd6R5hMQk2FGCH5mJU9B9ZZ3npX2JFwZVX3iuYHqt9LrlgJE3jemqPoxTLt6N_q6UoRl-amD7ePTXezNZzGJqL07C8Uvsw3Rcr2ZgliH0Kdp5C6q1w5_nh6JU7HKRphwU-UD70Udbdya-qSceoNcnh6yYb-hzGq3FH1-e_St1hyvtlqjq0K6cSKqYNeNh0quVFxbIYeK8gYUJCZtBN9PNZV8AsKQJMU5x6lV9Cw2RF8YeZsRKRKmmJqiXqipb8rQ0T1tHlwqdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=H4S4Vt0D1Pr4yy_Ur5vBNNigERFHydtHOenMKBaACYYKMETRP0fnK2N8XEotZd7klw056N8T0KRj_g7RTNf72QZy6CmK99S3sl90eS1A-wyCLT3-M6lWpIx8fvHiDabGgIJoTyH9Bp7BjtHa2r3KDHMzf9jUeOATdOL7GoO2rTOTsAd2CR3Hkd4xX_fy4mhornp0U_G1GtYORz5p8GnPv1EQjyttDme37953HT7uTvI5iGjhWLffYrhcwdE6cti9plcZV5XE-r3BzukNAfGbaZXms4vV7nykLea8NEKRIIWKpRJoXHpsmcTz37gdO2_BfBwtKtKk9D73uYj0ZGYNYINlvI3v1eBVb5Ei1I-LGSQ6CqJNa-QsqEHU4O--cPbgt7RZxV7XA3l3u1mB3G3sJ5_KrZB7jjQQFd6R5hMQk2FGCH5mJU9B9ZZ3npX2JFwZVX3iuYHqt9LrlgJE3jemqPoxTLt6N_q6UoRl-amD7ePTXezNZzGJqL07C8Uvsw3Rcr2ZgliH0Kdp5C6q1w5_nh6JU7HKRphwU-UD70Udbdya-qSceoNcnh6yYb-hzGq3FH1-e_St1hyvtlqjq0K6cSKqYNeNh0quVFxbIYeK8gYUJCZtBN9PNZV8AsKQJMU5x6lV9Cw2RF8YeZsRKRKmmJqiXqipb8rQ0T1tHlwqdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من ادعای نبوت ندارم. اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقه ما و به طور فزاینده‌ای در سراسر جهان تعیین می‌کند:
🔴
قوی‌ها زنده می‌مانند. برای ضعیفان جایی نیست. آن‌ها شکار می‌شوند. آن‌ها ناپدید می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/130210" target="_blank">📅 19:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130209">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
بنیامین نتانیاهو: ما در خاورمیانه‌ای پرآشوب، طوفانی و وحشی زندگی می‌کنیم.
🔴
دولت اسرائیل همیشه قوی و همیشه مصمم است.
🔴
بیش از ۶۰ درصد از سرزمین نوار غزه تحت کنترل ماست
🔴
ما از قلهٔ بوفورت بر جنوب لبنان مسلط هستیم.
🔴
و تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهیم ماند. ما قصد عقب‌نشینی از آن را نداریم.
🔴
وزیر دفاع و من به ارتش اسرائیل کاملاً شفاف کرده‌ایم: «شما آزادی عمل کامل برای حذف هرگونه تهدیدی برای سربازان ما یا ساکنان شمال دارید.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/130209" target="_blank">📅 19:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130208">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=dekUK3jjPp2iQyddy8s4YFZcPSsReTKfD6F4HL3J44phVFrdYt3vTladYmNUIrA8H0Ajg9CoJMyqyH1AuT9DpVEXwaQ1NHynbJz44zNA-iYeCM4k98frbUbku6GbuVzpW105fINw5Q4rkon2JAQFZ31HhLQL7hwkSsCIXl4yP0keWsRX0N3FjMIQE6rRLHd8xi5weYcS3ix5BcZT00Ve60fi9x6Ez-sbDBNx5RdAMdGsT1y6FCuKBiYv2aszv-rPuDk6qkjgKoZwfB_GM3KjjZ8Ds7lC7IHkgfKZarHOXNYeRAl3E6eOapw-joYwPjdeGlGBnjb0Ye1mhK2z-OwQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=dekUK3jjPp2iQyddy8s4YFZcPSsReTKfD6F4HL3J44phVFrdYt3vTladYmNUIrA8H0Ajg9CoJMyqyH1AuT9DpVEXwaQ1NHynbJz44zNA-iYeCM4k98frbUbku6GbuVzpW105fINw5Q4rkon2JAQFZ31HhLQL7hwkSsCIXl4yP0keWsRX0N3FjMIQE6rRLHd8xi5weYcS3ix5BcZT00Ve60fi9x6Ez-sbDBNx5RdAMdGsT1y6FCuKBiYv2aszv-rPuDk6qkjgKoZwfB_GM3KjjZ8Ds7lC7IHkgfKZarHOXNYeRAl3E6eOapw-joYwPjdeGlGBnjb0Ye1mhK2z-OwQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: فقط یک فرد نابینا می‌تواند بگوید که دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
🔴
من همه آن‌ها را فهرست نکرده‌ام چون می‌خواهم شما را بی‌جهت خسته نکنم. شما اینجا زیر آفتاب سوزان ایستاده‌اید—فهرست کردن همه آن‌ها زمان زیادی می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130208" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130207">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو: ما تهدید وجودی فوری را از سر خود برداشتیم زیرا اگر امروز علیه ایران اقدام نمی‌کردیم، بمب اتمی‌ای به وجود می‌آمد که اسرائیل را نابود می‌کرد، و ما این تهدید را برداشتیم تا ابدیت اسرائیل را تضمین کنیم.
🔴
وظایف بیشتری برای انجام دادن وجود دارد.
🔴
بله، کارهای بیشتری علیه ایران باید انجام شود؛ کارهای بیشتری علیه حماس باید انجام شود. در همین حال، آنها توانایی زیادی برای مقابله با ما ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130207" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130206">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارانوت:
نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130206" target="_blank">📅 19:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
نتانیاهو: همچنان ماموریت‌هایی وجود دارد که باید در مقابله با ایران و حزب‌الله شود،از لبنان عقب‌نشینی نخواهیم کرد و تا هر زمان لازم شود در لبنان خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/130205" target="_blank">📅 19:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130204">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vx13orMq7PUNxp55ARuTGST77bEnNc_iSgYIztUUSAFKmVDJiJdkjoaaMO42YUI8HbKBal67lwnnYX62SRYON89Jq469jUvL0IZ3LFZWB0of_nL2XdtV18S6davwTSPrv_RD5CHbtXyt3d89Tkf-jo2SN9fKJsF6G84Lyi7euhvsdVnJETjS-V4NoUvc1eSau91uJjLKL2RtaiCHb6Ai1tkMbQTa7sBK27PiGFrAcyBiDAnKOmvyVu5qX1J0iRk09ToawbOl7QBmnf7oUiTTDqNBJMVeKODNRROEbS511DktXQW6x4WaZqQLN_VrTEplc-wnyguUY_YtcURwEuhPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، یک شاخص مهم در صنعت هواپیمایی آمریکا پس از شش سال، سرانجام از زیان‌های دوران همه‌گیری کرونا عبور کرده است.
🔴
پیشرفت در مسیر توافق میان ایران و آمریکا باعث کاهش قیمت نفت شده و فشار هزینه‌های سوخت بر سودآوری شرکت‌های هواپیمایی را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130204" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130203">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=CmFNhjtnF6f590aWmGuBwIAsngN09H-nfqqn5Z3mxT5MsJXdOMIdZ1b6X8IXv_ehjVE93ZygiYxWI8tkeg1ewElM3xH4EZ_FP9MW7T0HnfePo-L5GSsaHcsUel76aWAgyTheJm7XQ-KONW0grn3yIYbK3296-BZVKhzHczwwFtsDIKP0SPJp9AD_i2z-XGHJLKLGKhPHLXoWuKnRzCKkFyHbqtiD2bf4LQQtjrtsratcd66LgO-0p71MLbziH5FFU1uBxUNC0Nog7IMVYgvcP1-0OV9fR0EtAc1aoEQ1pYxreeA0CDo07XSqjbYrmXisMdxKDApMJOyskDfh71rigzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=CmFNhjtnF6f590aWmGuBwIAsngN09H-nfqqn5Z3mxT5MsJXdOMIdZ1b6X8IXv_ehjVE93ZygiYxWI8tkeg1ewElM3xH4EZ_FP9MW7T0HnfePo-L5GSsaHcsUel76aWAgyTheJm7XQ-KONW0grn3yIYbK3296-BZVKhzHczwwFtsDIKP0SPJp9AD_i2z-XGHJLKLGKhPHLXoWuKnRzCKkFyHbqtiD2bf4LQQtjrtsratcd66LgO-0p71MLbziH5FFU1uBxUNC0Nog7IMVYgvcP1-0OV9fR0EtAc1aoEQ1pYxreeA0CDo07XSqjbYrmXisMdxKDApMJOyskDfh71rigzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعزیه عجیب در فلاح تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130203" target="_blank">📅 19:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130202">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ارتش تا زمانی که لازم باشد، در «مناطق امنیتی» در لبنان، سوریه و غزه باقی خواهد ماند.
🔴
ما علی‌رغم فشارها برای خروج از «منطقه‌ی امنیتی» در لبنان، مخالف عقب‌نشینی هستیم؛ عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/130202" target="_blank">📅 19:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130201">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
مرکز عملیات دریایی بریتانیا (UKMTO): مرکز عملیات دریایی بریتانیا گزارش یک حادثه را در فاصله ۷/۵ مایل دریایی جنوب‌شرقی دهیث، عمان دریافت کرده است.
🔴
یک کشتی باری در سمت راست خود توسط یک پرتابه‌ی ناشناس مورد اصابت قرار گرفته که به پل فرماندهی خسارت وارد کرده است. ناخدا گزارش داده است که تلفات جانی و اثرات زیست‌محیطی نداشته است.
🔴
مقامات در حال بررسی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/130201" target="_blank">📅 19:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130200">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAE5KyZL0QdrA6XMpd8fE3kBTeMJuRtrTKyZK9fIhRaqCRURZmC6BI2z7aWLqcC7Bddg7frTjhIg7y3JwPs2NEn06ltYG1d-gUsP3ltw5iYk_x7Z4kWQT76fLyPPP7w7ti0urctXN1sk1sHDAutOgm2YFWJyTB3Rs-0rZiXxwqol_06dSwY1dWraprGGw3xzNVIBgtYtrJVTcR6SMjRlNBpyWgj7USBOaqWxLzb3v1Rl8HTbooRKgeh71y5SZBGo80RXEYFUk3L5VekCkIg6m6NEo9TxChda9pDMVegDlmw_h552iEKIbhyfTsxQFoODg34WiLjAJdmW04Wjz7OL8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130200" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130199">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/130199" target="_blank">📅 18:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130198">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: ایران روزانه تا ۲ میلیون بشکه نفت صادر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130198" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130197">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مقام آمریکایی در گفتگو با نیویورک پست: وجوه منجمد هرگز تحت تفاهم‌نامه حمایت شده توسط ترامپ به ایران نخواهد رسید. در عوض، پرداخت‌ها مستقیماً به فروشندگان تأیید شده‌ای که کالاهای بشر دوستانه تأمین می‌کنند، ارسال خواهد شد و نه به خود حکومت ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130197" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130196">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری / تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
🔴
طبق اعلام فیفا، هواداران می‌توانند با پرچم‌های رنگین‌کمان وارد ورزشگاه بشوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130196" target="_blank">📅 18:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130195">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل:  ما از کمربند امنیتی در لبنان عقب‌نشینی نخواهیم کرد، حتی اگر ترامپ یا هر مقام آمریکایی دیگری از ما چنین بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/130195" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130194">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
لحظه فرو ریختن ساختمانی در ونزوئلا در جریان زمین‌لرزه‌ای که این کشور را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130194" target="_blank">📅 18:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130193">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
جی‌دی ونس: یکی از بزرگ‌ترین پیشرفت‌ها در مذاکرات سوئیس، توافق اصولی برای ایجاد یک کانال ارتباطی نظامی مستقیم بین آمریکا و ایران بود تا به جلوگیری از تشدیدهای آینده کمک کند.
🔴
ادعای ونس، آن‌ها گفتند: «باشه، خوب، ما کسی از سپاه پاسداران می‌فرستیم که در دوحه با کسی از سنتکام ملاقات کند، و این‌گونه بسیاری از این اختلافات را حل خواهیم کرد.»»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130193" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130192">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
وزیر خارجه آمریکا روبیو می‌گوید «خیلی نزدیک» هستیم به «بیانیه اعلام نیت» برای خروج برخی نیروهای اسرائیلی از جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130192" target="_blank">📅 17:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130191">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد وزارت نفت عراق: به دلیل کاهش شدید صادرات نفت در پی جنگ علیه ایران، با بحران مالی حیاتی دست و پنجه نرم می‌کنیم
🔴
در صورتی که سهمیه ما در اوپک به طور قابل توجهی افزایش نیابد، مجبور می‌شویم که تمام گزینه‌های موجود را بررسی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130191" target="_blank">📅 17:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130190">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=uXxjt_LH0a03yejzVHC67lTz4E6p3s7RXKAa-gKDY1jmF5WMR4S5j9BTXZSD5spkXF9qHjKDUqRqriH3TeiwhB5NUquLQQjNxVXZXYQVmJPJwPijtpqZr9MpXIbMLK8C_ZWwgHTbvD_D0K9G5h7y3hWBBE194ihLYqtqom9BfeFjODD2UCeHlVqV63s1sFH9U9xTfVFDX1-8lSa4gCUM1s32wPVfN1OY4dykLkGo5oFZ28dF7mJsWxro0xqLGx9O7x7sREQqJPkzuiD8S5x3_mapXL5r3Qu6iXKFTM4L_sp3MYIBSMvklv7ISaFS2tLx1oFzvJ8fZG9EbCakoqyLgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=uXxjt_LH0a03yejzVHC67lTz4E6p3s7RXKAa-gKDY1jmF5WMR4S5j9BTXZSD5spkXF9qHjKDUqRqriH3TeiwhB5NUquLQQjNxVXZXYQVmJPJwPijtpqZr9MpXIbMLK8C_ZWwgHTbvD_D0K9G5h7y3hWBBE194ihLYqtqom9BfeFjODD2UCeHlVqV63s1sFH9U9xTfVFDX1-8lSa4gCUM1s32wPVfN1OY4dykLkGo5oFZ28dF7mJsWxro0xqLGx9O7x7sREQqJPkzuiD8S5x3_mapXL5r3Qu6iXKFTM4L_sp3MYIBSMvklv7ISaFS2tLx1oFzvJ8fZG9EbCakoqyLgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیش از ۲۱٬۰۰۰ نفر پس از زمین‌لرزه‌های ویرانگر که ونزوئلا را لرزاند، مفقود شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130190" target="_blank">📅 17:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130189">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رهبر انصارالله یمن: پیروزی ایران در برابر دشمنان، پیروزی کل محور مقاومت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130189" target="_blank">📅 17:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130188">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
جی دی ونس: اماراتی‌ها - که تا حد زیادی جنگ‌ طلب‌ ترین و تا حد زیادی طرفدارترین کشور در شورای همکاری خلیج فارس هستند - در حال گفتگوهایی با ایرانی‌ها هستند که قبلاً هرگز اتفاق نیفتاده است، از جمله با سپاه پاسداران، در مورد انواع مختلف مشوق‌های اقتصادی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130188" target="_blank">📅 17:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130187">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
🔴
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
🔴
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130187" target="_blank">📅 17:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130186">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کانال عبری: آمریکا ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن‌گوریون به درخواست اسرائیل خارج می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/130186" target="_blank">📅 17:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130185">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130185" target="_blank">📅 16:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130184">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=uvDUgdovuAI6w1iYyvvg8CNa9tGRlPc9Ow_i-5Gr1oCShtgWYfDbWZV5-mup3Dp2S1bhdPXFi3uJwKZOfAfJ94-PeidU7PXj-RXIFPCoBTWX-TVOwQSjSMsbc12fh8Ktch_LDLcQ-kUfIyprmN6XSN92uFyWE02OiQvfJXPAVcA_wRvXpZYnYvkOl0EpJFlduZLOjxSgRsz656y3sCuclkeevZV5n_FP_Fl6Q_3asaTwbO-y4P9QanALmN8lY_eTIg9Ctd8NAnhViCktuLjWM1K697TKNKR8ev2Nc9pzqYtSADdpGacmJaKQi6Ri7fKaUvOnc3-wDZLOTo3t-kQgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=uvDUgdovuAI6w1iYyvvg8CNa9tGRlPc9Ow_i-5Gr1oCShtgWYfDbWZV5-mup3Dp2S1bhdPXFi3uJwKZOfAfJ94-PeidU7PXj-RXIFPCoBTWX-TVOwQSjSMsbc12fh8Ktch_LDLcQ-kUfIyprmN6XSN92uFyWE02OiQvfJXPAVcA_wRvXpZYnYvkOl0EpJFlduZLOjxSgRsz656y3sCuclkeevZV5n_FP_Fl6Q_3asaTwbO-y4P9QanALmN8lY_eTIg9Ctd8NAnhViCktuLjWM1K697TKNKR8ev2Nc9pzqYtSADdpGacmJaKQi6Ri7fKaUvOnc3-wDZLOTo3t-kQgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افزایش چشمگیر تردد در تنگه هرمز
🔴
بخش عمده این فعالیت‌ها شامل ۵۳ مورد ترافیک تجاری است و شناورهای کم‌ریسک بیشترین سهم تردد در این روز را به خود اختصاص داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130184" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130183">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdW8XPJKuELKEsqDiToS7ODZC_o-O13Ggi0m0y2ALY9ZjO21OrRknhDFxO1BCdSHk77YfmOHHG0_OV35ajXenlWqfgtszvqXysiLNH1hy1T98MkPwg54fvVZ7p88_9i2eZ2jDuBPkZkEntKtHGMPqKwyb2jkeYDUi00L0I8tLROIBS00efljB2c_O-4K_G3jUiZCefDmOXhkrKdILwpsvrEwOxxmH9NJty56jkswN1HEV3gbW5IVFO8EPymtOLRmNqUwis4tNM0NGfd5NPdAaFz8GebLdViQK0NVqUQAFJLT4h01J2XX0NQAWMSh2DxnFrjcr4WrB_Wk1-lX5ItrUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه کپلر: تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است
🔴
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130183" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130182">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCk1tl0Njsx79B1U4iEirCnDoohy6vl6X7eFiXg49JQh3PWQMgAW_720NhA3XfPfwaFuoB5yjdMs924FnmHDBnu-0SGKjSVH-jrACRmXeyGpGXmbhiuu-LK_9zJvn0ltyC0nzTWyT-Y48E8zlC9msTrG-lsHrY_b5e6lAvO7uU4mfl1iGoZWbkg0KJW6LLYO2fDJXAMzp8-V5P2M35RnEwh0cybpmVZR4i2TWpLei_qm-yh1Iv2StwfiJUD4PnBqhqlim8w1Y6cu0AtBIyZGn_67KWMC6MJJMIB3-2wggk9gSvRCiMZOyaAzLwRd2oQI4O_J6AYLn08Kl-F9p8e9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی: هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130182" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وال استریت ژورنال : ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/130181" target="_blank">📅 16:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
گزارش حملات هوایی اسرائیل به مناطق غربی غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130180" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: عمانی‌ها می‌گویند که طرفدار سیستم دریافت عوارض در تنگه هرمز نیستند
🔴
دریافت عوارض عملی نیست
🔴
اینکه ونس مستقیماً در موضوع ایران دخیل است، نشان از اهمیتی است که دولت ما به این مسئله داده
🔴
در جلسه با اعراب، موضوع صندوق بازسازی ایران مورد بحث قرار نگرفت
🔴
توافقی را میخواهیم که امنیت شرکای ما در منطقه خلیج فارس را تضعیف نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130179" target="_blank">📅 16:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
هلند تیمی به ونزوئلا خواهد فرستاد و حدود ۲ میلیون یورو برای اعزام نیروهای نجات، سگ‌های جستجو و تجهیزات اختصاص خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130178" target="_blank">📅 16:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130177">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5ZGlKimQUwreejfTfTc6Sy914nYpr3QrQEowvlwBhLiVAPeCARaCOfpjzO7fWy-Cz2trhsgOvmOHMLFt1uaOD8PxyULnhKU4aN0dvnqAaU9yIca7_6Vz6_6rDXT3Kj5ZiUIKlibZ_PMczWt7BFBEBU2sZCSRLYb_Gjj2bwqOPhN4PtFcZ16-x0MTAop1wLa_xW__oCOh31f3RT4BrRqJK6eMxyp1QsEdoUYtsAT_hYwsazS1ApKXOT9eI2DAlbDJJnAhaZQ3MIzC4eXT73-WfwoVlKwJRnm6iAU2GfAuE5zx_WZJ43OIvRijsb6nNfMx-zC_K7ue4MayJLNmbAWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلطنت عمان بدون مشورت با ایران،  بیانیه‌ای صادر کرد و از ایجاد یک کریدور دریایی موقت در جنوب تنگه هرمز خبر داد(رنگ سبز)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130177" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130175">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoSceRNxJS9ZZPZRYzbYQUhNsRTxZgzrVfhe4xt9lO5oZHimmhX4pwjNNV0P8TetfeCDfr9_WQ1fVvD7XTPgqG7otZml_6qoRMqPGMOeaRu_TzVqRNBOhrL07ikiGIFjyXES5QMA-RsleuM4E9Ax75-B_EVjLsKf95JwFuuh39mPSvbSmVaZSOjEBJBomga391dnFbLpA_Ex57Zl0wt6wBnDWWqVSqiCbWMe-Go_6bEFGmTc_yWVbmJDtbo6_KWP89Cz9jOpnzcH8RaOXJDZqaCw-jKRmSkguUslia6RJHN8CKOYF1Ah3leLTQOhIp9j2y7ICXxGRMwh6nh_QB2VTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/quXYU2sebykaxjoSUx61n5V9vj7xbpx9c9XxTJ06c9r7JkpC6793g5WfcVfjE2nL7rkU7IpYnaXZaOxQIH-HyK4yWGsYZFKONU3kblNPdYBYBbUgMtT7w_zmVn9aVBhnST6oPZZc-F6plqep5LfRFC5rBQhtYKes4jUZzRD6AWAC2CzC0bYr0XkuTRIn1pqmp5KXI54rV4l7S04G5m30nUgkPC4k49eRwrs4g0dyxr3p_OCuuuA3I06YHc-X7EHSjxJc8TNg0Z2l7gSRy98LnEeKMFP8_V9IUX4bw5hdok-EHbMCBWZzCarka8-9PYtx5o26WfWgly1gtx261YnLPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قبل و بعد از زلزله‌: لا گوایرا، ونزوئلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130175" target="_blank">📅 16:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130174">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7mTNqVTzhX_Qkr9vKE0SqeXQnQZ0LGPjr7VeLQfj6vA_b9HSWA9odLwC1KXMmUhYZFE7lOuoftvF3YKrI5IVwU0o8eAbbfcM0z7mI_ryiAzsLr9rbMi5jZW_Nxobjt1uf37wFmYgnTyTDQ2ktI6mlE2vkf2ZGw6FbveKoef5EMgMDt2vozIr6xVq-0o1HilewnwYpaAEr9UTG-PwcLqxC_6Eid0ODD0PaJ_3X2w4MEsO8oAWQ5ZGuWVsF8ef9u_5ncHK4waVAw4VvgU2r7SzZtcMGMlpJ8d-1RKqCdiTLdpNm9-yVbiZBXFYWsL7yKZg-EMFds99IxZLXAv2_SjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: «آمریکا به دروغ ادعا می‌کند که دارایی‌های آزادشدهٔ ما برای خرید محصولات کشاورزی آن‌ها صرف خواهد شد. عجب!
🔴
تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!
🔴
این محصول [بی‌اعتمادی] کاملاً ارگانیک، فراوان و بومی است. اما ظاهراً آمریکا فقط سویای تراریخته و وعده‌های عمل‌نشده و حرف‌های بی‌ارزش صادر می‌کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130174" target="_blank">📅 16:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130173">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
هشدار یمن به اسرائیل: هرگونه حماقتی با پاسخ سخت روبرو خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/130173" target="_blank">📅 15:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130172">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130172" target="_blank">📅 15:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130171">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=LwE6B6BTYJ_iMXTq8p093px7XsynkgNp0pYFermjXD77Q9Rebzlxh4eS9dlNSb4UhV7wm4kBBrn2HdF44gBWer0oegARQbuCGe3I4YddW5pHdLo9yxaEXsjf0F2eVmJSLskXYn6-Bqz_chpaHYdfxBnCuNlnr9zjFiB87msKvU8KiAN_AFam-FPwGy6swvAcIxDsZE7MoRK_Nn-ggqV2VwJoMgyDtmB1bfkz_wmQcodZ6PIFjrf9a6FR5r2q99F1mA0ttzTDxxCIwA2MadbvoS2JvZmsWuD_owoli6t2W-T-9lxlR0WXju4E6wc2K4uhb0pxBwvAwPJjOcGJ3MYUWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c279c049.mp4?token=LwE6B6BTYJ_iMXTq8p093px7XsynkgNp0pYFermjXD77Q9Rebzlxh4eS9dlNSb4UhV7wm4kBBrn2HdF44gBWer0oegARQbuCGe3I4YddW5pHdLo9yxaEXsjf0F2eVmJSLskXYn6-Bqz_chpaHYdfxBnCuNlnr9zjFiB87msKvU8KiAN_AFam-FPwGy6swvAcIxDsZE7MoRK_Nn-ggqV2VwJoMgyDtmB1bfkz_wmQcodZ6PIFjrf9a6FR5r2q99F1mA0ttzTDxxCIwA2MadbvoS2JvZmsWuD_owoli6t2W-T-9lxlR0WXju4E6wc2K4uhb0pxBwvAwPJjOcGJ3MYUWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاشورا تسلیت
💔</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130171" target="_blank">📅 15:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130170">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
امروز عاشورا است روزی که حسین شهید شد، حسین اولین شخصی بود که علیه
حکومت مذهبی فاسد و نامشروع
قیام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130170" target="_blank">📅 15:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130169">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=PDCEGJvBULbwyLdMed3NPdrZ_F_CjPsY9E_N8B_WLLAjKnRRuF566j7cZ5hOI3MxW-5xMo3iKg60xICq2n_FYDReqTDnqtT04a3X9aoEUiDlKFNTTrHlXzooz7MeqK3h93slnLgR-8f5VUx7qKsWkdDCHAQs2QpK_u9KozC9ZVkLAzeGAPZdyw-O-NvAW-EQF3g_YSjnAS7YXkuqD_pRmsgeKATwSLPiwVwXceeqxyzMT2rWH1WIWjn-Tj2ZMz7Z57TZoGVgqhTZbwGmFqJ8OuBGamfXaepNmcexOU-2-ASWHwS9Mk0jxFSFe0topisxO5dwc9Z93aEpwE5M0OuKLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d1e505c4.mp4?token=PDCEGJvBULbwyLdMed3NPdrZ_F_CjPsY9E_N8B_WLLAjKnRRuF566j7cZ5hOI3MxW-5xMo3iKg60xICq2n_FYDReqTDnqtT04a3X9aoEUiDlKFNTTrHlXzooz7MeqK3h93slnLgR-8f5VUx7qKsWkdDCHAQs2QpK_u9KozC9ZVkLAzeGAPZdyw-O-NvAW-EQF3g_YSjnAS7YXkuqD_pRmsgeKATwSLPiwVwXceeqxyzMT2rWH1WIWjn-Tj2ZMz7Z57TZoGVgqhTZbwGmFqJ8OuBGamfXaepNmcexOU-2-ASWHwS9Mk0jxFSFe0topisxO5dwc9Z93aEpwE5M0OuKLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: اگر کشتی‌ها در حال حرکت باشند، ما به آن واکنش نشان خواهیم داد.
🔴
اگر کشتی‌ها حرکت نکنند، این نقض توافق است و ما با آن مشکل خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130169" target="_blank">📅 15:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130168">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
روبیو، وزیر امور خارجه درباره عمان:
روابط ما با عمان خوب است.
🔴
آنها می‌گویند که طرفدار سیستم عوارض در هرمز نیستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130168" target="_blank">📅 15:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130167">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
روبیو: ما مراحل اجرای یادداشت تفاهم با ایران را با کشورهای خلیج فارس به اشتراک خواهیم گذاشت
🔴
به طور خاص، درمورد بند مربوط به پرداخت ۳۰۰ میلیارد دلار حرف خواهیم زد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130167" target="_blank">📅 15:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
تحلیل نیویورک‌تایمز: اهرم تنگه هرمز کم اثر می‌شود؟
🔴
برخی معتقدند که خط لوله‌ها می‌توانند جایگزین کشتیرانی در تنگه شوند، اما بعضی دیگر در مورد این راهکار تردید دارند
🔴
فقط صلح با پیوندهای اقتصادی با ایران است که می‌تواند معضل را حل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130166" target="_blank">📅 15:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ونس: فروش جنگنده‌های اف-۳۵ به ترکیه در دست بررسی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130165" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران یکی از جبهه‌های مهم نبرد برای امنیت اسرائیل است‌‌ و ما نباید به دستاوردهای خود در ایران بسنده کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130164" target="_blank">📅 15:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=rzxm4hh1LrGti56MWcpz_6dS_UH5eJxCnHk0s4s1o1T43axXrCXZeb5iOxYnMuQ0Bt6ubZQWvPtXf5lEz9LXUWFxnC5FsIrqtuOh4E6PeU1B-B7bEuRLQh9ActSoouirfQfS8e0l6rD2rORaX1X4wduQ2vYFjsw73JD0b59Jq1cQpM6Ss-O2JRrc1Rc68_ISW1N9tEiRIQNRiEggp78ZWpWzdpUXDeHfbg-H3rmBQARS8-jwNC_Wa_YDP8TLO6LgLVXFHyLAa1l1xT6pOR1Xz6myReMlYM01Qg6s0hLhRAAUb4pqTyen5F6tRQv_NjfEXU2i8KfbBFXPta--K1fYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15084fec1c.mp4?token=rzxm4hh1LrGti56MWcpz_6dS_UH5eJxCnHk0s4s1o1T43axXrCXZeb5iOxYnMuQ0Bt6ubZQWvPtXf5lEz9LXUWFxnC5FsIrqtuOh4E6PeU1B-B7bEuRLQh9ActSoouirfQfS8e0l6rD2rORaX1X4wduQ2vYFjsw73JD0b59Jq1cQpM6Ss-O2JRrc1Rc68_ISW1N9tEiRIQNRiEggp78ZWpWzdpUXDeHfbg-H3rmBQARS8-jwNC_Wa_YDP8TLO6LgLVXFHyLAa1l1xT6pOR1Xz6myReMlYM01Qg6s0hLhRAAUb4pqTyen5F6tRQv_NjfEXU2i8KfbBFXPta--K1fYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: آن‌ها افرادی در شاخه‌های سیاسی دارند که به نظر می‌رسد منعطف‌تر و مایل‌تر به همکاری با ما هستند.
🔴
آن‌هایی که با آن‌ها مذاکره می‌کنیم، همین افراد هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130163" target="_blank">📅 15:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQILUwj1yQja_eaggQjVQv0unbEQ4kuetMyyJyVD62G2nLaSJ_E7Ho0Otw8rK8SNN5QKuduH5FlZZVKKiz_peoUWt3h8hukAW2kW079KSkUCoJG3R-XxRYEsFNhKh2y4Oi0larfXmjQGycTEUkz0T1nNDWBF2sNy9TZZ1AmmKKhJvpPqTpO1KNMer_eZGU9JUsA_soK13junMwP3pXzCQVZvPzvcV0k_t18OP1oPGZMRcDOr3Mijv4GVttvuXFlm3eNVkqG-a9r7rc49znny_gtZ8z4lFYEWW32V-RX45eMa3XG7DB98se0lFlW9wy_IwFiyPEfvzD1egYBXNUHj8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلیس آمریکا دو نفر را با کیفی پر از موادمخدر که روی آن نوشته شده بود "قطعاً این یه کیف پر از موادمخدر نیست" دستگیر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/130162" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130161">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
روبیو: با نیروهای نیابتی ایران صلح و ثباتی در منطقه وجود نخواهد داشت/ ایران با حمایت از حزب‌الله و حوثی‌ها در امور کشورها دخالت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130161" target="_blank">📅 15:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130160">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
روبیو وزیرامور خارجه آمریکا: ما با کشورهای خلیج فارس در مورد موضوع ایجاد صندوق بازسازی برای ایران صحبت نکردیم‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/130160" target="_blank">📅 15:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130159">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: جنگ اقتصادی علیه ایران از جبهه‌های مهم نبرد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/130159" target="_blank">📅 14:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130158">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گفت‌وگوی تلفنی وزرای خارجه ایران و سلطنت عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130158" target="_blank">📅 14:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130157">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130157" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130156">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
وزیر نفت: امنیت غرب آسیا و ثبات انرژی جهان تنها با خروج بیگانگان از منطقه تامین می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130156" target="_blank">📅 14:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130155">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر امور خارجه عمان: ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض عبور نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130155" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رئیس‌جمهور موقت ونزوئلا از افزایش شمار کشته‌های زلزله و سونامی در این کشور به ۱۶۴ نفر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130154" target="_blank">📅 14:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130153">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59328e354b.mp4?token=J6puga1EeTe-ONIeO0QVOJ4esOegF-GUA0nqpPhdL_f6mIDAlEGYu2gAxf6bMIE4fzSuM7JTIhuemFGDxWV95lQhfs5YPOia00vYme_9kZS1uQIxD2eWqEsUzM0x9nQ1hl3Jsz6G1kNOe_LDM5gq5BBijBCWniAxqEkizoc9WG2fukQMKDQFCR4gwvy3rMJYtecRxdXYxrSaFnKCpnXzV1Pl7WRUeyshF6Li3-MP6t7OKorI3vcYAiOg9G3jGkbIHA48ECk33e88WpuoxAfzjxeKFvGN-TT0Lq_2RkTV4IZ_Gq7drZP-hAcZvVR77c_1XPSrMKP-qwErWi1-rktnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59328e354b.mp4?token=J6puga1EeTe-ONIeO0QVOJ4esOegF-GUA0nqpPhdL_f6mIDAlEGYu2gAxf6bMIE4fzSuM7JTIhuemFGDxWV95lQhfs5YPOia00vYme_9kZS1uQIxD2eWqEsUzM0x9nQ1hl3Jsz6G1kNOe_LDM5gq5BBijBCWniAxqEkizoc9WG2fukQMKDQFCR4gwvy3rMJYtecRxdXYxrSaFnKCpnXzV1Pl7WRUeyshF6Li3-MP6t7OKorI3vcYAiOg9G3jGkbIHA48ECk33e88WpuoxAfzjxeKFvGN-TT0Lq_2RkTV4IZ_Gq7drZP-hAcZvVR77c_1XPSrMKP-qwErWi1-rktnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اردوغان می‌خواست برای کمک به ایران وارد جنگ شود، من نگذاشتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130153" target="_blank">📅 14:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130152">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
منابع العربیه: توافق اصولی بین لبنان و اسرائیل بر سر «مناطق نمونه»
🔴
انتظار می‌رود امروز پس از دستیابی لبنان و اسرائیل به پیش‌نویس پیشرفته، «اعلام تمایل» صورت گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130152" target="_blank">📅 14:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130151">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سرویس اطلاعات خارجی روسیه اعلام کرد که غرب به اشتباه خویشتن‌داری روسیه را به عنوان ضعف تلقی می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130151" target="_blank">📅 14:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130150">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حدود ۷۰ کشتی در ۳۶ ساعت گذشته از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130150" target="_blank">📅 13:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130149">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkMQ80PlQ6otYr89C1GxJ77hS1a2kdi53zEMa2e0du_WSQhKs77XKjSf1uHfxT2R4qhMURqVgzr50veng224jBsf6d3cOrAYCUKrD_VOJWsQXTFa0QpH364XavVx_fiGgEFSUCQhddYbLifacGLpUq8Z6Mq18iAEN1ugwDMbg9JwGj6GQYQ7nLrY4rVlT4irXhalHkeJ2QgXojEThbyxymfce7bKlTq4cY2bQYxnM6arYdIFVgX4ctIj0AV3MmRASM-btVHSFxkkWvQGjtkjzYWz-Q7oCylDRAuVgZSSuz7n1HJgljdOHp4_lyVqcwfeM9gK_rHakF5GBXNJYqSreA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکارد دیده‌شده در یکی از تجمعات و حمله به مذاکره‌کنندگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130149" target="_blank">📅 13:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130148">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130148" target="_blank">📅 13:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130147">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
روبیو: امیدوارم تهران رفاه مردم خود را در اولویت قرار دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/130147" target="_blank">📅 13:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130146">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm6yVm2kWEiV4K-gUO-6nzEytkSA6dEBXerPpt3NL1GNn1eKAkPY-zsyVAgay0mUcswzB65XH4mKNjhTwYYhOyb9v9CR79-8HgZPYvP_cezVdSWr7hi4MR71iqfjKz4smkyeTmji6OtfcgtfQvz-xqqzkuOiURStxXiK0n6m5arWNz57eZnPGCGEZ8E4Qg_HsNOURTUusLUCSYpG-ixCUSbC96r0RpjLWtJbcMC4mLFUAg3BJnVheHxiB1bUar7cCMPjOPE57B19KeepLwGUdrsTmBZDEoe83smYPrE-9c04yxK5VfxuBNuyp3paZvlEhQBZrAhkShoxFgJp6nzH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پراید صفر ۱.۲ میلیارد تومان!
🔴
پراید با وجود اینکه از خط تولید خارج شد اما همچنان نمونه‌های صفر کیلومتر آن در بازار یافت می‌شود.
🔴
در برخی موارد نمونه‌های صفر این خودرو تا قیمت ۱.۲ میلیارد تومان آگهی شده است.
🔴
اگر یک کارگر با حقوق پایه ۱۶ میلیون تومان بخواهد این خودرو را بخرد باید حدود ۷۵ ماه پس انداز داشته باشد.
🔴
آنطور که به نظر می‌رسد خرید یک خودرو از رده خارج مثل پراید هم برای بسیاری حالا تبدیل به آرزو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130146" target="_blank">📅 13:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130145">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر اعلام کرد که تیم‌های فنی کار روی جزئیات اجرایی توافق حاصل شده بین ایران و ایالات متحده را آغاز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130145" target="_blank">📅 13:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130144">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
هلال‌احمر ایران برای امدادرسانی به زلزله‌زدگان ونزوئلا اعلام آمادگی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130144" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130143">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
اسرائیل هیوم: به ارتش اسرائیل هیچ دستوری مبنی بر عقب‌نشینی داده نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130143" target="_blank">📅 13:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130142">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بهنام سعیدی، دبیر کمیسیون امنیت ملی مجلس، با اشاره به موقعیت استراتژیک تنگه هرمز اظهار کرد: وضعیت امنیت در تنگه هرمز به طور کامل تغییر کرده و این آبراه راهبردی هرگز به شرایط قبل بازنخواهد گشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130142" target="_blank">📅 13:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130141">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سی‌ان‌ان: متحدان ترامپ در کشورهای حاشیه خلیج فارس بیم دارند که توافق او با ایران سرآغاز تحولی فاجعه‌بار باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130141" target="_blank">📅 12:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130140">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/ رویترز به نقل از مقام آمریکایی: اسرائیل به نشانه حسن نیت از بخشی از منطقه امنیتی جنوب لبنان عقب‌نشینی کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130140" target="_blank">📅 12:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130139">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سازمان پخش اسرائیل: ایالات متحده به درخواست اسرائیل، ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن گوریون خارج می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130139" target="_blank">📅 12:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130138">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزیر خارجه بحرین: از تلاش‌هایی که به امضای یادداشت تفاهم میان ایران و آمریکا منجر شد، استقبال می‌کنیم| کشور‌های شورای همکاری خلیج فارس چشم انتظار فصل جدیدی هستند‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130138" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130137">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b25ff2083.mp4?token=rAICbS9boAoEAH_EdOvDCgOfdGtniRmp-fx2Iqd0OJGpVCxGbKPEVnDeGjOMAtYDbDsz3jOVp2rYlHRRNbI1jFGdN3ZXTBLg268wXnR2_UKNemR8-WPqOOuSNWnNI7f4mpznBU8ALkIWKJYq72LlrucIPhCbsBZIDHML1njtdLsBaaY_MB_81oOTQRFCvR3RXTXpM7EitAS0AnrBzi-08B-1b2Wlwn4k6I5Qx1x45LnC0njX-hbq2_LRSOvBVcGegnifYkk2hymvSoMe3L6qWGkqjitdv9tkXNM95j0qhzhwIlOKijLCR7KZbdmLx_MoPCqjzXiKAwOJR3XawgVHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b25ff2083.mp4?token=rAICbS9boAoEAH_EdOvDCgOfdGtniRmp-fx2Iqd0OJGpVCxGbKPEVnDeGjOMAtYDbDsz3jOVp2rYlHRRNbI1jFGdN3ZXTBLg268wXnR2_UKNemR8-WPqOOuSNWnNI7f4mpznBU8ALkIWKJYq72LlrucIPhCbsBZIDHML1njtdLsBaaY_MB_81oOTQRFCvR3RXTXpM7EitAS0AnrBzi-08B-1b2Wlwn4k6I5Qx1x45LnC0njX-hbq2_LRSOvBVcGegnifYkk2hymvSoMe3L6qWGkqjitdv9tkXNM95j0qhzhwIlOKijLCR7KZbdmLx_MoPCqjzXiKAwOJR3XawgVHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو در مورد ایران: می‌توانید آن را عوارض بنامید، می‌توانید آن را هزینه بنامید، هر چه می‌خواهید بنامید - این یک بازی معنایی است.
🔴
واقعیت این است که هیچ کشوری در کره زمین حق ندارد برای استفاده از آبراه‌های بین‌المللی هزینه دریافت کند.
🔴
و این هرگز شرط قابل قبولی برای هیچ توافقی نخواهد بود. رئیس جمهور اساساً در این مورد شفاف بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/130137" target="_blank">📅 11:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130136">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8db1e8129e.mp4?token=Xa9SXIBFrJl16u-aBejyvm1fLQ5B0cHJrAoEIizXzPase8-Ys8gOXlI7VCA_itq8LISUOoaME2qeuuH68VcYZGiBcypMnw8V4SKLFYWFAF_eJtVVMjEOQ9VCNUBSz9o6faQYsZYbrMt2HqLQ5kWgZPtB0_ZdfBQmVjTuhGwe92G5TKd0nbXm0FRBLJNdK3cYKrvZ_mGuHsDw5z3uUYoObGv5TYUKIbaHUyL5kUoc7UqHah67z0X_8hsDFii-_mcy6nWxNfpJUbOkzJvaqKDoIShaQuCtA7OCvN8rHhloWTn9r_3ggMVulAuI6vhbeyN06jBWUhaKQDdKBlJd-XUutQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8db1e8129e.mp4?token=Xa9SXIBFrJl16u-aBejyvm1fLQ5B0cHJrAoEIizXzPase8-Ys8gOXlI7VCA_itq8LISUOoaME2qeuuH68VcYZGiBcypMnw8V4SKLFYWFAF_eJtVVMjEOQ9VCNUBSz9o6faQYsZYbrMt2HqLQ5kWgZPtB0_ZdfBQmVjTuhGwe92G5TKd0nbXm0FRBLJNdK3cYKrvZ_mGuHsDw5z3uUYoObGv5TYUKIbaHUyL5kUoc7UqHah67z0X_8hsDFii-_mcy6nWxNfpJUbOkzJvaqKDoIShaQuCtA7OCvN8rHhloWTn9r_3ggMVulAuI6vhbeyN06jBWUhaKQDdKBlJd-XUutQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ایران: تنگه هرمز آب‌های بین‌المللی هستند. آبراه‌های بین‌المللی متعلق به هیچ دولت-ملی نیستند. این یک اصل اساسی در جهان امروز است که بدون آن جهان در هرج و مرج کامل فرو می‌رفت.
🔴
اگر در واقع بپذیریم که می‌توانید برای استفاده از یک آبراه بین‌المللی به دلیل نزدیکی به قلمرو سرزمینی خود، هزینه دریافت کنید، خب، این مانند یک بیماری واگیردار در سراسر جهان پخش می‌شود.
🔴
اگر در واقع، اکنون تنگه‌ای وجود دارد که یک کشور می‌تواند، یا دو کشور می‌توانند، یا هر کشوری که تصمیم بگیرد می‌خواهد برای استفاده از آن هزینه دریافت کند، چه چیزی مانع از آن می‌شود که هر کشور جهان در نزدیکی یک آبراه، هزینه مشابهی را اعمال کند؟
🔴
و سپس ما هرج و مرج خواهیم داشت. بنابراین این غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130136" target="_blank">📅 11:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130135">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فرودگاه امام خمینی: گروه هواپیمایی لوفت‌هانزا تمایل دارد که پرواز‌های خود به ایران را از سر بگیرد، اما هنوز زمان مشخصی برای آن مشخص نشده
🔴
ممکن است که «آسترین ایرلاین» زودتر پرواز‌های خود به کشور ما را شروع کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130135" target="_blank">📅 11:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130134">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfK5iXkuCVFkZo4oTITXkfTzs36yNQTg7VGDq9IqPXjitExnfyDStT0vNriI96jhjyrW9gpoW0t-_jp0sE3oTaFXKwNYDTlUhCTjD2P0YKWE-sBGrX2Bf6r_mS90uBZINmH96aGaVqVFUaax9b1XA1OdYLEDuOexB_oY2X2R84dH4IpQEgLRqgAcl3oB6xEqhTwTu6DX65TT0Wuj23LdPTqC7QrUP72yUb3yvY4uabLTxx_KR45UdMw6UtjVPHsXXSASOJDcCQe4oOLMim1LeN4oUjCKrKEkq2QFR9y6aWt8TRl6gyePD5ooZ0AuFgEJiiMKrn0sVFOOToqXanuUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک در پی سقوط سهام تسلا و اسپیس ایکس در معاملات روز چهارشنبه که ارزش دارایی او را به ۹۷۰.۲ میلیارد دلار کاهش داد، عنوان «تریلیونر» را از دست داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130134" target="_blank">📅 11:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
روبیو: ایران در سوئیس تعهدات بسیار صریحی داد و اگر به آنها پایبند نباشد، گزینه‌های دیگری پیش‌روی ماست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130133" target="_blank">📅 11:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=XECud9COCWBdvEMRXPDhr1OQwSvFwI91EnZKQyx7dIPDnny27plU9YeUeYrzcOH15-5Q4hOdr3AVM_MN9zzOANP6iM5xSanylNlRH4mnZflNSwWqihuiX0ObfiKYybBv01w_97rS7KmBSqATLD1hfvFaD7GYPlQ7VFIt3XfBMCb4O7ulNAng3ifKTh_Du1K4W2cfMR_qUVxwJII-0d7zDew1uMJG74LFL_HNAlvM9-MSF8bwmq1c0bC4ORMTmCK1YuYpt2CdGSyy7ao1RSaGS9JKtd290P4VFAxpDIGyF9Dk0Qu8BA7dKRA8MUayGoRwSRid0hTVrjFHg7nDXKRqfwHX8GY3uhL-fP8rSV58Ohvu41Iyl7o3shlzLCIO0FyK_a5F4lQ22ZvME59Ng15Ji2z2e3OMTypZu_IebYhHDSLKx8i7t2mcTtwV0jBllNlAGejF63dwVvYVMNA4PhrV1Lum1sZW8pNEhubWHWOwGbTu6CuwZa6OBSIVXuFEWYjg_47HPX_ACIYDb1MoM7dk56bifiFoqlb97bwsHFrEAoxc59I4ZuMprpZi9P0wW8_Knwlajt9Ueu7A4-98I3QK_jygOMr1CG8TDnrg9CRcplReYSX_0761qqT_gUbaDFGLs5TmBV3yWiSUpGBlUWQIqNsbbLp5hsmmx0D2dP75W6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c7905e956.mp4?token=XECud9COCWBdvEMRXPDhr1OQwSvFwI91EnZKQyx7dIPDnny27plU9YeUeYrzcOH15-5Q4hOdr3AVM_MN9zzOANP6iM5xSanylNlRH4mnZflNSwWqihuiX0ObfiKYybBv01w_97rS7KmBSqATLD1hfvFaD7GYPlQ7VFIt3XfBMCb4O7ulNAng3ifKTh_Du1K4W2cfMR_qUVxwJII-0d7zDew1uMJG74LFL_HNAlvM9-MSF8bwmq1c0bC4ORMTmCK1YuYpt2CdGSyy7ao1RSaGS9JKtd290P4VFAxpDIGyF9Dk0Qu8BA7dKRA8MUayGoRwSRid0hTVrjFHg7nDXKRqfwHX8GY3uhL-fP8rSV58Ohvu41Iyl7o3shlzLCIO0FyK_a5F4lQ22ZvME59Ng15Ji2z2e3OMTypZu_IebYhHDSLKx8i7t2mcTtwV0jBllNlAGejF63dwVvYVMNA4PhrV1Lum1sZW8pNEhubWHWOwGbTu6CuwZa6OBSIVXuFEWYjg_47HPX_ACIYDb1MoM7dk56bifiFoqlb97bwsHFrEAoxc59I4ZuMprpZi9P0wW8_Knwlajt9Ueu7A4-98I3QK_jygOMr1CG8TDnrg9CRcplReYSX_0761qqT_gUbaDFGLs5TmBV3yWiSUpGBlUWQIqNsbbLp5hsmmx0D2dP75W6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: همه به ما احترام می‌گذارند. دیگر کسی به ما نمی‌خندد. دو سال پیش، آنها می‌خندیدند.
🔴
حالا، ما محترم‌ترین در هر کجا هستیم. به آن فکر کنید. در هر کجای دنیا
🔴
دو سال پیش کجا بودیم؟ ما مورد احترام نبودیم. ما یک شوخی بودیم. ما دیگر یک شوخی نیستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130132" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeA40Wouu1uN9auwpSyPcygUAb0gT6YJaBxhNlp_Q96QfXlRjyHq1wgkTU-cw9i8X57YidGf_gxA0ZBvNdcwq-N70eIU0jSdSXoDbtci9WRnN4kggeGGxf_t_KLhVUuRwrMnEzsP8moWBOTC71u6sZHEdwnQxtyYqvL3-anHS88iNkIa4cPXLyf2rEE2j_oTwFJrCeCcG7tFV3-aCnI7HypWJjrO74RJraLMMQK0_ZJl1Zfnr9XV9RvKHrlkzMV6E0d9VHIkl9KQxtjg4jhlcV2GB4GWsx0z7z7oT1JCd363CDQa7_7vJsx6IoQwyudGW8SpfcAd0t91t0SZN8wcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAouDCcYF2qAe5wWbXlJNFWlCnrWQlpCWMwaRiPxD19q1Gei58gv9UBdjU0AX6SNtiBRFGIht3rVe7tRZfXwJrHgN08BX-jmZRUIRcoUUK2xuM3JRm43jf6nXqgEn2Ye8e3yluHKDE3OH_YNI4GSdX1jRTo9raQwmwKQy56axUEEuyw0IkQQ4hQou4l_YhXeIlAcpy9CMpL7RPn_iArU9Wj1AMOuEa0KGBeasvqYFUayznYl7xiSlMfYJmdjhsBxcMqK4LMZNhFhSQARDXbLZCD4BlpII11pwYHCVkUOPgNgwCOV1kA4rK7xRqTs8pPFNiwKdEyfPxp5JFG4YCZv6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ایران از عمان به دلیل صدور مسیرهای کشتیرانی برای تنگه هرمز بدون دخالت تهران انتقاد کرده است.
🔴
نیروی دریایی سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد که «برخی مقامات» - بدون نام بردن مستقیم از عمان - بدون هماهنگی با ایران «مسیر جدیدی برای تردد کشتی‌ها» از طریق این تنگه اعلام کرده‌اند. این بیانیه افزود که «تنها مسیرهای مجاز تردد» مسیرهایی هستند که توسط تهران تعیین شده‌اند و هشدار داد که هرگونه مسیر دیگری «بسیار خطرناک» است.
🔴
این اظهارات پس از آن مطرح می‌شود که عمان با هماهنگی سازمان بین‌المللی دریانوردی، «کریدور دریایی موقت» در تنگه هرمز را اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130130" target="_blank">📅 11:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130129">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldKIeNRxDD9ZD1lt7AbWysdVIOv4ylOueJ9x_LECJM2Kkx-_kQ12X1WPXUaeCoXTQ71MSrATK9yH0rsakaooYV3KHHR5KpMlvl2_sHgyoDrhVhsBT7C8yf5jG96Q21LupsJBSAXpd-iynVHAQ8UPv1imDcyRlbx_UQOpNiQsJ39XBEJmFWOSOCFJ1Lh18p76pvEEOZdpIKma2Q4L5l3zprRE-lDR0RWVxRnIqqnKDn2fXOZUMmMX7HBbcc7wKfpMx55I-cdZ5zX0uLzFtnQwiRmEQbo53aSa5Uxxrs06b0eJQpCw6VjBMoAb3T7yYTsug5_fDzgiws7z-mdT0Tr_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
🔴
این رأی، ایران را در معرض توجه قرار می‌دهد! رئیس جمهور دونالد جی ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130129" target="_blank">📅 10:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130128">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
ارتش اسرائیل از کشته شدن یک سرباز و زخمی شدن سرباز دیگر در لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130128" target="_blank">📅 10:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130127">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=Kk822ha_b-k3-ZhSpY1H5Xm-O89q9sBBLXRyrCl4ULNT81cQ_9BGGoYlPgLnrdBnO7j6jAiTI0jhQ2YFVHkG-HC_U3wDiThwnKMaahX2P0XZSnrHmgCJEy9n8FHR3_pgtv15HU0iY94eJpT9SuaBknGKZMPlodQe6QorEaFIDZBMzwJtMBFuWQ8smjpcfVAdYsijQrnr2DT_bH3zBFLhBeTw88Z3WdBE1mRi8ltK1zNFzLM7YdjnvkSKyVggkdyugRA_XlQTFwdMpCHPaZSyoPC_UUF-URfpoFHli0hKTIGTA6oQJ1akaGFoerexC-JGXhtVX5JC6vMS52re_ZSrjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fcd190313.mp4?token=Kk822ha_b-k3-ZhSpY1H5Xm-O89q9sBBLXRyrCl4ULNT81cQ_9BGGoYlPgLnrdBnO7j6jAiTI0jhQ2YFVHkG-HC_U3wDiThwnKMaahX2P0XZSnrHmgCJEy9n8FHR3_pgtv15HU0iY94eJpT9SuaBknGKZMPlodQe6QorEaFIDZBMzwJtMBFuWQ8smjpcfVAdYsijQrnr2DT_bH3zBFLhBeTw88Z3WdBE1mRi8ltK1zNFzLM7YdjnvkSKyVggkdyugRA_XlQTFwdMpCHPaZSyoPC_UUF-URfpoFHli0hKTIGTA6oQJ1akaGFoerexC-JGXhtVX5JC6vMS52re_ZSrjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در دو جنگ جهانی پیروز شدیم، فاشیسم و ​​کمونیسم را شکست دادیم.
🔴
ما باید دوباره این کار را انجام دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/130127" target="_blank">📅 10:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130126">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=tfJci6rr4m8yQ94_GFjQQUq10a-_-6_uUiUOeQgckB8_JpzPnWlvb_kxAm6WK4ZE6F9CdKqIDLsico-7ITccOf2vINgzoWVWq4u012mBP_OekXPpSsCJKAuCuEHUNLNdLpbxH1RoXwrDk0s5ll9YBOMWOYzn4dK6PXS1--QjXILWvJGB9dVarLl-mp26pf291_Yb-diKBG6CP6jQXCwpXYZD7rn0QnaSGAphSqvL17AdH2CKmcENHPQy-MARicTX29lSo5zAQ86aZsfXxOEcYWww4JC4aRN1JoGAKuAU772_hxRg21Xtx4RElsT0tiiJTK0ELgRv-z47pEtD1MwdBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd225af94c.mp4?token=tfJci6rr4m8yQ94_GFjQQUq10a-_-6_uUiUOeQgckB8_JpzPnWlvb_kxAm6WK4ZE6F9CdKqIDLsico-7ITccOf2vINgzoWVWq4u012mBP_OekXPpSsCJKAuCuEHUNLNdLpbxH1RoXwrDk0s5ll9YBOMWOYzn4dK6PXS1--QjXILWvJGB9dVarLl-mp26pf291_Yb-diKBG6CP6jQXCwpXYZD7rn0QnaSGAphSqvL17AdH2CKmcENHPQy-MARicTX29lSo5zAQ86aZsfXxOEcYWww4JC4aRN1JoGAKuAU772_hxRg21Xtx4RElsT0tiiJTK0ELgRv-z47pEtD1MwdBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما در حال ارائه بزرگترین کاهش قیمت دارو در تاریخ با اختلاف قیمت ۴۰۰، ۵۰۰ و حتی ۶۰۰ درصدی هستیم
🔴
اگر نیم درصد کاهش قیمت را انجام می‌دادید، کسی می‌گفت شما نابغه هستید - ۴۰۰، ۵۰۰، ۶۰۰، ۷۰۰، ۸۰۰ درصد. هیچ‌کس چیزی شبیه به این ندیده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/130126" target="_blank">📅 10:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130125">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
کاسبی جدید با محدود شدن تعداد و ظرفیت کارت‌های سوخت آزاد: برخی متصدیان در ازای «شیرینی» کارت جایگاه را در اختیار رانندگان قرار می‌دهند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130125" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130124">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=kMJ5yBEm_qa-6rG_kYWkq9ON9oxUnVdP4nOrLR3m4H1_ZvH2wE0-UxgBSGCTrxMGt0s86pcwRw9wz0enl3sjS0QW-dBykVbdHOQyiyd85Vx8RqpiBOclJV0ECdhKgNx3pABS9R8A8goe1RCS2Y5KkRqi9SF7Jp5MZ-8deV4kmYBBTAncqMdUyefQptGka39eurRg8kSH3xOPgeVSDFJJ-hw1Kxff4gXWAVynw15XVlKH3jGv2Q4Nk3W2OV9GgAJkOHFwsGW5zehs9Jd0UOztTGNTkKKDTsMEanLQkAAztJH5evDY2679iclplORdC7r0C3iYWwljXuY6ISEjttlP0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a188028b7e.mp4?token=kMJ5yBEm_qa-6rG_kYWkq9ON9oxUnVdP4nOrLR3m4H1_ZvH2wE0-UxgBSGCTrxMGt0s86pcwRw9wz0enl3sjS0QW-dBykVbdHOQyiyd85Vx8RqpiBOclJV0ECdhKgNx3pABS9R8A8goe1RCS2Y5KkRqi9SF7Jp5MZ-8deV4kmYBBTAncqMdUyefQptGka39eurRg8kSH3xOPgeVSDFJJ-hw1Kxff4gXWAVynw15XVlKH3jGv2Q4Nk3W2OV9GgAJkOHFwsGW5zehs9Jd0UOztTGNTkKKDTsMEanLQkAAztJH5evDY2679iclplORdC7r0C3iYWwljXuY6ISEjttlP0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسیب به ساختمان رادیو تلویزیون دولتی ونزوئلا در دو زلزله ۷ ریشتری امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130124" target="_blank">📅 10:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130123">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه‌داری آمریکا روز پنج‌شنبه مدعی شد که معافیت از تحریم‌های نفتی ارائه شده به ایران قابل بازپسگیری است‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/130123" target="_blank">📅 10:23 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
