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
<img src="https://cdn4.telesco.pe/file/O09Lk02bvORMsBNhKxcrzcS6JO_t9OhFhUGZzyXHFAaeWk8H75L9eCD6euCTu_RzMCd6EswLcEf8s4pU1TRwG6muryiXD7ynJAKVYrCHPW4cxAsjBNPUrHf8qgSOLeINL6EK19GMDZWL15idwssn-QmBIAIfH8vX2pg_qV-1V6knavnUh1sZ3CyTQS2Yt6ZRrOIR7mHznp5pal8vckfZ5LIenvGbBhTWQHJ-kVaYanqN0S6CYSp6jLsh-2zyE_tN2W9o7jBmw9usF4ILXr5JdZ6HSBAsjbXKLzTpBuHp_n2h2oQjkkvOVBirPB-RBS0mCER6xZzxzt7GdzXXUsnWWw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 450K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 09:42:44</div>
<hr>

<div class="tg-post" id="msg-22652">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/847f998c3f.mp4?token=Mjti-r586keYWRn75cPGfNhfx9LrvUE11ExCM7p-A-uJNDaEPYNmerfdffkU3enBcd65RR2mhZAiSoA-B5G1zIUgRlO42gvCbfDiQ9w_xwX-AMPnw_spRMxfqt4m84eNTXqzw7b-o4bJZZCtVNTMm3udydCCr0aMpMqhDmDjPQxP1zjel4PkPQnsjz9h6w6HId-DRznd5SO7XQoZTdaz22qPDy9sz0LnAosoLOzzIXJK9RJHfC_shBXOKbu0Fym92k53UGx4x-nOQWs5cvlQZFUR6BsZF_vgosJCMm22JTVOocD8fTxZcFrzvOGFwQFhogYUCvaUKRvvC_sO1E-13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/847f998c3f.mp4?token=Mjti-r586keYWRn75cPGfNhfx9LrvUE11ExCM7p-A-uJNDaEPYNmerfdffkU3enBcd65RR2mhZAiSoA-B5G1zIUgRlO42gvCbfDiQ9w_xwX-AMPnw_spRMxfqt4m84eNTXqzw7b-o4bJZZCtVNTMm3udydCCr0aMpMqhDmDjPQxP1zjel4PkPQnsjz9h6w6HId-DRznd5SO7XQoZTdaz22qPDy9sz0LnAosoLOzzIXJK9RJHfC_shBXOKbu0Fym92k53UGx4x-nOQWs5cvlQZFUR6BsZF_vgosJCMm22JTVOocD8fTxZcFrzvOGFwQFhogYUCvaUKRvvC_sO1E-13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : نفتکش «M/T Riesco» پنجمین نفتکش ایرانی که امروز هدف حمله آمریکا قرار گرفت پس از حمله در دریای مکران (عمان) غرق شد.چهار نفتکش دیگر بر اثر اصابت موشک به موتورخانه‌هایشان از کار افتادند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/22652" target="_blank">📅 05:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22651">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مقام آمریکایی ‌به رویترز گفت: «وضعیت تمامی نیروهای آمریکایی مستقر در اردن مشخص است و آنها سالم هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/22651" target="_blank">📅 04:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22650">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارشهای بسیار از صدای انفجار در کنگان ، انگار از طرف بندر دیر بوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/22650" target="_blank">📅 04:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22647">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MDk0NzgyMzU1OTg1NTY1?story_media_id=3824690341744932317&stkn=MWF3bWE3bnlhMWkwcw==</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/22647" target="_blank">📅 03:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22646">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/22646" target="_blank">📅 03:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22645">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/22645" target="_blank">📅 03:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22639">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ارتش اردن : ایران در جریان حمله به پایگاه هوایی موفق السلطی، ۲۰ موشک شلیک کرده و پدافند هوایی این کشور ۱۸ موشک را رهگیری و منهدم کرده است، در حالی که دو موشک باقی‌مانده از «مراکز جمعیتی» دور افتاده‌اند.
هیچ تلفاتی در نتیجه این حمله گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/22639" target="_blank">📅 03:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22638">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpzKpZuY9w8h2tJoFLFVUbzxInL3fA2loj_HkU7Lyy005Y4UemhGgT3YG7wkccRSzMIu7QHJZnujHmWhtPk6nrRyEXeduLOZ0bURapKaE2I8UcY3R_2oYmDdhVhqrxuX-VlyUhaSpbPZryYQCre-Gax938z0-CmH6SCiESp2mz12e9GUk8Agpc3exII08CgSRF-v9S4Cz_dfy1mMUlM6D_6QFqEdd9hARKlIlvOWH9_qPqbuVbKnNkxaaT5saEi-R7iNWErczCRDFRwFneMM0_vNaHIbpbwU6nalBT7T6vPsH5E9fDV1SI1dEXBuiFhF6r4lJTLNLUXI97g_3T1o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران اعلام کرد در واکنش به اقدامات آمریکا علیه نفتکش‌ها و شناورهای ایرانی، نیروی هوافضای سپاه با موشک‌های بالستیک به دو ناوشکن آمریکایی
DDG119 - USS Delbert D. Black و
DDG53 - USS John Paul Jones
حمله کرده است. سپاه مدعی شده این دو ناوشکن که به موشک‌های کروز و سامانه پدافندی Aegis مجهز هستند، در این حمله آسیب قابل‌توجهی دیده‌اند. همچنین تأکید کرده به اقدامات آمریکا پاسخ خواهد داد و نسبت به «خطای محاسباتی» هشدار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/22638" target="_blank">📅 02:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22637">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/22637" target="_blank">📅 02:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22636">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/22636" target="_blank">📅 02:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22635">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ویدیو حملات به اردن توسط سپاه
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/22635" target="_blank">📅 02:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22634">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/22634" target="_blank">📅 02:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پرتاب موشک جدید از‌ تبریز
@WarRoom</div>
<div class="tg-footer">👁️ 97.2K · <a href="https://t.me/withyashar/22632" target="_blank">📅 02:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بیانیه شماره ۱۳ سپاه: آشیانه تعمیر و نگهداری، آماده سازی و محل استقرار جنگنده های F-35 ،F-16 ،F-15 و شلتر جنگنده ها مورد هدف قرارگرفت
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/22631" target="_blank">📅 02:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/541f997a69.mp4?token=Tx6THX9xBkCC9N7Ehk091XApc6gt6x6Xffne1J1eNNKS7ggqQt7TXogpbhwPZGSdixdrhuQy57gwY_QzNOrKHkYs-Y-LX-t-4ddT_bMUKT8NssyjK0K3hB46-KPREjOyIFm1A61ZM4KW33iwljb7bxCdchlMDARD7qDLGdkjRoEELiLayFclhUbANzj1c-XQO7CtJ4c0qWXfKCMC-nqEhSHeIYFwp0j6s5cRxaYoOsCXW1-57UuuODCKAeQ-UPDEvWkjKdcI35HGPgPaybBdM_0JOVEyW9oI-16nRUFyCe0e8Bi89diCRIEL3ZYvrc_vvTkTCkI9wLQ2AMUVZ-pnKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/541f997a69.mp4?token=Tx6THX9xBkCC9N7Ehk091XApc6gt6x6Xffne1J1eNNKS7ggqQt7TXogpbhwPZGSdixdrhuQy57gwY_QzNOrKHkYs-Y-LX-t-4ddT_bMUKT8NssyjK0K3hB46-KPREjOyIFm1A61ZM4KW33iwljb7bxCdchlMDARD7qDLGdkjRoEELiLayFclhUbANzj1c-XQO7CtJ4c0qWXfKCMC-nqEhSHeIYFwp0j6s5cRxaYoOsCXW1-57UuuODCKAeQ-UPDEvWkjKdcI35HGPgPaybBdM_0JOVEyW9oI-16nRUFyCe0e8Bi89diCRIEL3ZYvrc_vvTkTCkI9wLQ2AMUVZ-pnKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه، درباره ایران:
ایران همچنان به تلاش برای حمله به کشتی‌های نیروی دریایی ایالات متحده ادامه می‌دهد و هر بار که این کار را انجام می‌دهند یا سعی در انجام آن دارند، نفتکش‌ها را از دست می‌دهند.
امروز دوباره شاهد این موضوع خواهید بود.
@WarRoom</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/22630" target="_blank">📅 02:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شبی پر خرج برای رژیم جمهوری اسلامی
سنتکام : ایران از این نفتکش ها به عنوان بخشی از یک شبکه مخفی چند میلیارد دلاری برای تامین مالی سپاه پاسداران و عوامل ایرانی در منطقه استفاده می کند.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/22629" target="_blank">📅 02:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم  نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت…</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/22628" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/22627" target="_blank">📅 01:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم  نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت…</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22626" target="_blank">📅 01:55 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اتاق جنگ با یاشار : تمام اطلاعات و تحلیل ها و نام کشتی ها درست خبر رسانی ، پیشبینی و تحلیل شد و با اختلاف چندین ساعته امشب به اطلاع شما رسید !
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/22625" target="_blank">📅 01:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سنتکام : ۵ کشتی زدیم
نیروهای سنتکام در ۸ سپتامبر، پس از آنکه سپاه پاسداران انقلاب اسلامی طی دو روز گذشته دو بار یک کشتی جنگی نیروی دریایی ایالات متحده را با موشک‌های بالستیک هدف قرار داد، پنج کشتی نفتکش ایرانی را منهدم کردند. کشتی جنگی ایالات متحده با موفقیت از حملات ایران جان سالم به در برد و به گشت‌زنی در آب‌های منطقه‌ای ادامه داد. هیچ پرسنل آمریکایی آسیبی ندید.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22624" target="_blank">📅 01:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22623" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار خلبان جنگنده آمریکای به کشتی HORIZON برای تخلیه موتور خانه در ۱ دقیقه
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22623" target="_blank">📅 01:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0NvqLkWbRUo8s6vC0RiIB-5B2UubPOXvcGJCUt-btKY6LDQzC8Hj2Ib9XmvbQF7rtpPXKwnMsJZR5mBzBUJVVhg6BUAzsUNXzI0I7Dgjp11P1NJazFxRYWz_EVP5O8OvLTLA6gZ1NlSnf8ohpLgQLLsYgQNtMG9l8cXdnma9WcJpt7_YcMQoMRdfKyDp-dRmYbwSukFXzHYhvCh74-hEhbfYeWQZ9725SgyndgsWQFmwS2Jf0kZZCeDCcFa9JSaAT4XIRR29Py1vDmyfKIWFKx7H3RB08ulABZkisrrKUunxs6QaC_bm7qA3tpQkpT_h_3ScSCD1yYtCCNF083q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتی دیگری‌که امشب هدف قرار‌گرفته احتمالا
HORIZON
است که با نام هرمز هم شناخته میشود با کال ساین 9hek9 که به نظر میرسد مربوت به امپراتوری Hektor  همان حسین پسر شمخانی باشد
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22622" target="_blank">📅 01:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22619">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تنها خدای واقعی زمان است</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/22619" target="_blank">📅 01:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22618">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixFTak6PEVWeitsIDaJJFDrDpuI-gZ4SyXcJwgYFLHtTBLF5WXCes1w9eMhbvxDDRJ_DHFCyrOBOd1GjZ0S0UFMm3UTnal4c-qQ-xbO_4sB4SdN277b81z4_NwCTi6CUrrS__ZFnUzB4N1N4VDu2g4K1p0Zb2-qOXWYUXxCN1rLbPoVdiXpI4UagrLqMODOdaP34PijpCI4NvlCZewevSXpyYSN8baevm4qin4MWWKLfsRtzSyWLr5dBuJcACH5UpAdEQoptIIuQvMURHp_U_9f5LbbKgTkBz-fOZuXP3AhwVo9LDuknEJvezN2zcHmpoOEKQjFBGrMK2qZFfEfMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بروجرد پرتاب موشک ناموفق بود و ترکید !!!
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22618" target="_blank">📅 01:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22617">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff90ac3f79.mp4?token=Xp5U3J9b64q6OK12sKC_m14PCMn5K_0qaiytiTugxzb2WKzWwbn1erOLKlV2pGTpxleamKiHP0Nv-3EoVpqkMeDn7B9mvgBnOMew2ONjJOl_YPKHbp68mxql0-i0LUxZXp2bgtLEXfLKARX6jEuyOKVrjdF6Ytk4RvErjTV8zqflSV0fa0FuO7cSIZEb1Lo2J22yQcbpxfmqVxJdExbTuyIGIkDdwbcvb77hnbknk6zrs1OxUE9EooGkE1t5rTxB8E90_Jrcm91NZK5hNE9QvnzOm_6GB7jhuBy4Zx_dIQivWkvBixVyhaj8yf7rviJ9YQtMtFi6CKlXx7qemfPgAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff90ac3f79.mp4?token=Xp5U3J9b64q6OK12sKC_m14PCMn5K_0qaiytiTugxzb2WKzWwbn1erOLKlV2pGTpxleamKiHP0Nv-3EoVpqkMeDn7B9mvgBnOMew2ONjJOl_YPKHbp68mxql0-i0LUxZXp2bgtLEXfLKARX6jEuyOKVrjdF6Ytk4RvErjTV8zqflSV0fa0FuO7cSIZEb1Lo2J22yQcbpxfmqVxJdExbTuyIGIkDdwbcvb77hnbknk6zrs1OxUE9EooGkE1t5rTxB8E90_Jrcm91NZK5hNE9QvnzOm_6GB7jhuBy4Zx_dIQivWkvBixVyhaj8yf7rviJ9YQtMtFi6CKlXx7qemfPgAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرجه موشکهای خوشه ای بر روی اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22617" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22616">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سپاه به اردن موشک خوشه ای زد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22616" target="_blank">📅 01:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22615">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7a6210ca1.mp4?token=nnLIpJvFiyCVGRCZ6-XzO0J8F5A3X-5Zj6uaVRn90vrhyzXV3xCvA6jhhYxnK1JfCblFrE9lg-_jd-XN6wzvOFXTsSvt3d3_3IIuBKI-z9I-SvPM7WK0MoG3irebChvbLPmqn3ln7wgPAvf34HzgrkHzINDLKUTSve1mg-MnG1cCWe7ddwrddlgHsfl8VDfhXV9sjreVgorlc9ZPwmXhkGbPT9N-KaNGePHNU21QkBcVBJo_vSFK4-1Q5BxkWaf4auXMUofRWh-Sh4ekgYGvaiY5wo1hrfvpgrgJEOn4CTwev2jEbnjywszPnI0au-Q5uwY8YkhzDhP8eU7SRRx7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7a6210ca1.mp4?token=nnLIpJvFiyCVGRCZ6-XzO0J8F5A3X-5Zj6uaVRn90vrhyzXV3xCvA6jhhYxnK1JfCblFrE9lg-_jd-XN6wzvOFXTsSvt3d3_3IIuBKI-z9I-SvPM7WK0MoG3irebChvbLPmqn3ln7wgPAvf34HzgrkHzINDLKUTSve1mg-MnG1cCWe7ddwrddlgHsfl8VDfhXV9sjreVgorlc9ZPwmXhkGbPT9N-KaNGePHNU21QkBcVBJo_vSFK4-1Q5BxkWaf4auXMUofRWh-Sh4ekgYGvaiY5wo1hrfvpgrgJEOn4CTwev2jEbnjywszPnI0au-Q5uwY8YkhzDhP8eU7SRRx7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحدید سپاه : مرتبط با آمریکا، در منطقه تنگه هرمز و خلیج فارس شما در معرض هدف قرار دارید دستور میدهیم که خدمه و مهمانان خود را تخلیه کنند اگر تمایل دارید [در اینجا بمانید]، مسئولیت حفظ امنیت خود و خدمه‌تان بر عهده خود شماست.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22615" target="_blank">📅 01:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22614">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d364bd4e.mp4?token=JIfxNa_UlsyFYSje50mRrr8OMP_hagCiTqA-hdtB2qrRDqe-2y-O4ZtyzsgQ5-C_1yUZ-avsCPkhQSpwLfUBsQBOICEls-Hfr5fqihHe_03G7L-lWEJZW832pVgD2Smf6FM_-2Rs5ZLghDcahj1YPTy4IjusdXe_MZGJgNaH3C4pHc2q6fVjzHGqywgX2mtFPjMOEFDgRvUY01fRCVMb1hYqDrc88iTRsE9fJxpQPuNJcNJ_I8BetK1wASRaguDK0345zyCl8KrRy-ynG-dDvUr96hf9IHmMjJpwszQxpHgzm9Ky_EeNSnCkad_j3Gjs17FwiDcQG01JD64bz2ugJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d364bd4e.mp4?token=JIfxNa_UlsyFYSje50mRrr8OMP_hagCiTqA-hdtB2qrRDqe-2y-O4ZtyzsgQ5-C_1yUZ-avsCPkhQSpwLfUBsQBOICEls-Hfr5fqihHe_03G7L-lWEJZW832pVgD2Smf6FM_-2Rs5ZLghDcahj1YPTy4IjusdXe_MZGJgNaH3C4pHc2q6fVjzHGqywgX2mtFPjMOEFDgRvUY01fRCVMb1hYqDrc88iTRsE9fJxpQPuNJcNJ_I8BetK1wASRaguDK0345zyCl8KrRy-ynG-dDvUr96hf9IHmMjJpwszQxpHgzm9Ky_EeNSnCkad_j3Gjs17FwiDcQG01JD64bz2ugJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ قم حرم زیارت بود که موشک پرتاب شد
😂
✌🏼
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22614" target="_blank">📅 01:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22613">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21c8f0d7d.mp4?token=L6zLLS8EufT1xQNnPvlzD89a9up9doBIOpxVUm4yvUllWWY9uD56AqUwjoLw7KgMv93qRpKVSh8P9EdJgu8w_LM4YBdDO59QHakAJL7YGm4rvjE3rFZStDpVhdA6F882Kn9w-I8Vb6km2FJMD4bEFdcHAJq_EJ45V266_zFkAbv5RtVpaNNa3ApTpvKRZW5BUUmJZ5LjocYf3ns_5HV56p_0yz6J1ZsCXQGzjh9u8nlmcNukg_0lyI3sMdkinn7V3MxRBsUZsiNHBWxcr79a9-dwUftg--JL2eC19KLlF6iJntFD80v9wnmD9I30_qlsAYce_1F0507u2aGMt2NW5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21c8f0d7d.mp4?token=L6zLLS8EufT1xQNnPvlzD89a9up9doBIOpxVUm4yvUllWWY9uD56AqUwjoLw7KgMv93qRpKVSh8P9EdJgu8w_LM4YBdDO59QHakAJL7YGm4rvjE3rFZStDpVhdA6F882Kn9w-I8Vb6km2FJMD4bEFdcHAJq_EJ45V266_zFkAbv5RtVpaNNa3ApTpvKRZW5BUUmJZ5LjocYf3ns_5HV56p_0yz6J1ZsCXQGzjh9u8nlmcNukg_0lyI3sMdkinn7V3MxRBsUZsiNHBWxcr79a9-dwUftg--JL2eC19KLlF6iJntFD80v9wnmD9I30_qlsAYce_1F0507u2aGMt2NW5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب یک دسته موشک از‌خمین
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22613" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22612">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a496403d.mp4?token=ZfcolB2Tm8W-iqGuS5hheM3A5Db84QijlzQ05gGIT2lSvC5U4mis_C7ek_uPjGWfiMY2itVCEtYsBpAf-AAvlX9w-dMUtj4aOw7AIEpT1tDPx92ttzcsSr7G1oMNwlkP1_CvOJ0DxBUb5RE_xc_fduFtLxQ4PZ_p7pItiQX7a43eG79mjo1BATprKLtLbwZTLMiau_nof3FDDI3Dldk7RY76GaNzCAxgvet7KfI3Ru1spOFLXypqS5VNLxI3t-vTjWkSZsAqDdslR158ov6OUog5tX1iE9sKt-7_Q0aEMdyp4sI9ziQh2SbbGgfAf0JXCXpijDJmafSbN5iIyPaX2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a496403d.mp4?token=ZfcolB2Tm8W-iqGuS5hheM3A5Db84QijlzQ05gGIT2lSvC5U4mis_C7ek_uPjGWfiMY2itVCEtYsBpAf-AAvlX9w-dMUtj4aOw7AIEpT1tDPx92ttzcsSr7G1oMNwlkP1_CvOJ0DxBUb5RE_xc_fduFtLxQ4PZ_p7pItiQX7a43eG79mjo1BATprKLtLbwZTLMiau_nof3FDDI3Dldk7RY76GaNzCAxgvet7KfI3Ru1spOFLXypqS5VNLxI3t-vTjWkSZsAqDdslR158ov6OUog5tX1iE9sKt-7_Q0aEMdyp4sI9ziQh2SbbGgfAf0JXCXpijDJmafSbN5iIyPaX2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22612" target="_blank">📅 01:02 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22611">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bbb709c43.mp4?token=jZQq0-Q98EJxwDyK8Al0YhWvujuFMG2RWeCF4D-Hus3mbR3llhCA7SpF8xTGVp-_Ty3HfEAXeZWbOPd1gMLh_1ekfnQwYxpa2UAfT2OwsveHmsZbbQ4uuZnUcUHMTFyXuIOuIEk3CBHkAHd9r9GrZ_FlNAnvxJLbp-sEFk-Uox7a6TofkNNL3i000Gi7VJwGEKKOTlRYLxBjxD7r94Pja9zf9SQA03y3RRjnhpMfW12vqvaTTqYj1ys9DrAU73cAOaAC5Kg1NQJrmFoz3xAUyGrcmCpEftj06_VM02ox1Aitin2Zk5JYFO0umlhaOikBumKeOT8xoeQidrpLn15c-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bbb709c43.mp4?token=jZQq0-Q98EJxwDyK8Al0YhWvujuFMG2RWeCF4D-Hus3mbR3llhCA7SpF8xTGVp-_Ty3HfEAXeZWbOPd1gMLh_1ekfnQwYxpa2UAfT2OwsveHmsZbbQ4uuZnUcUHMTFyXuIOuIEk3CBHkAHd9r9GrZ_FlNAnvxJLbp-sEFk-Uox7a6TofkNNL3i000Gi7VJwGEKKOTlRYLxBjxD7r94Pja9zf9SQA03y3RRjnhpMfW12vqvaTTqYj1ys9DrAU73cAOaAC5Kg1NQJrmFoz3xAUyGrcmCpEftj06_VM02ox1Aitin2Zk5JYFO0umlhaOikBumKeOT8xoeQidrpLn15c-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون پرتاب دو موشک از اصفهان
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22611" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22610">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22610" target="_blank">📅 00:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22609">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارشها حاکی‌است چهار نفتکش ایران توسط جنگنده های F18 هدف گرفته شده اند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22609" target="_blank">📅 00:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22608">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22608" target="_blank">📅 00:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22607">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22607" target="_blank">📅 00:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22606">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/withyashar/22606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">اخطار اولیه  نیروی هوایی آمریکا و تاکیید به هدف قرار دادن موتور خانه و و دادن ۱۰ دقیقه زمان به خدمه برای ترک  محدوده موتورخانه
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22606" target="_blank">📅 00:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش حمله موشکی آمریکا به سومین نفتکش ایران در سواحل شهرستان جاسک
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22605" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تحلیل ساده
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22604" target="_blank">📅 00:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22603">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دلار ۲۲۹،۲۰۰ تومان (سقف تاریخی)
تتر ۲۲۹،۲۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22603" target="_blank">📅 23:59 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22602">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش پرتاب موشک از کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/22602" target="_blank">📅 23:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22601" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار صداوسیما:
ارتش آمریکا به نفتکش دوم در نزدیکی آب‌های جاسک حمله کرد.خدمه هر دو نفتکش با قایق نجات در حال انتقال به سمت ساحل جاسک هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22600" target="_blank">📅 23:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22599">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پس برم زیر سماور رو روشن کنم
🤣</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22599" target="_blank">📅 23:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22598">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رویترز: امشب در سراسر خاورمیانه آماده باش جنگی است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22598" target="_blank">📅 23:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22597">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مقام آمریکایی به وال استریت ژورنال: ایران دوشنبه، برای دومین بار، حمله‌ای را علیه کشتی‌های متعلق به نیروی دریایی آمریکا انجام داد
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22597" target="_blank">📅 23:37 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22596">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سپاه : به تمامی خدمه نفتکش ها در محدود اسکله های کویت و بحرین که میزبان آمریکایی ها و شریکشان هستند اخطار می دهیم شناور خود را چه در لنگر گاه و چه در اسکله ها سریعا ترک نمایند چرا که مورد هدف  قرار خواهند گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22596" target="_blank">📅 23:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22595">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کامنت برای ترامپ
https://www.instagram.com/reel/DdCe4x2B6Qc/?comment_id=18626069959030735</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22595" target="_blank">📅 23:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22594">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه پاسداران اعلام کرد حملات موشکی جمهوری اسلامی علیه پایگاه‌های آمریکا در خاورمیانه به‌زودی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22594" target="_blank">📅 23:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22593">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مقام آمریکایی به فاکس‌نیوز : نفت‌کش‌های ایرانی را در نزدیکی خارک و جاسک هدف قرار دادیم.
این بخشی از تلاش گسترده‌تر برای اعمال فشار اقتصادی بر ایران است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22593" target="_blank">📅 23:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22592">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسانه های رژیم : دو تانکر نفتکش در خارگ و یک نفتکش ایران در جاسک هدف حمله آمریکا قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22592" target="_blank">📅 23:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22591">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22591" target="_blank">📅 23:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22590">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک  @WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22590" target="_blank">📅 23:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22589">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رسانه های رژیم تازه تایید کردن</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22589" target="_blank">📅 23:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22588">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">منابع محلی خارگ اعلام کردند که این حمله خوشبختانه هیچ‌گونه خسارت جانی به‌ همراه نداشته و کارکنان نفتکش در حال تخلیه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22588" target="_blank">📅 23:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22587">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22587" target="_blank">📅 22:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22586">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صدای انفجار جدید از جاسک (ممکنه جاسک پرتاب دفاعی رژیم باشه)
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22586" target="_blank">📅 22:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22585">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش انفجار مهیب در تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22585" target="_blank">📅 22:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22584">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏I24NEWS :  نیروهای آمریکایی در تنگه هرمز به نفتکش‌های ایرانی حمله کردند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22584" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22583">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22583" target="_blank">📅 22:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22582">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4IToL8PTdtxTQMVLy5jQf-WUXgqG3buWZFRRuuW9ZkILY9KzhqXeRWiMQ7xhF-05q21TvtVJJL1f8hdO8rd1A_TwgvBIgY4f8c2xLEdIafpCBdqvOiCIpvTxt4wdJDU1015yEUdGiZhdsjnGlk8AUhpUtl2r1RJfx4hShh5AbG6RW_MrR0gp8t6pVPnqZkCye-lFnkP49cVVAeeP3mJHwIxb89fPQvmNUGFhWlxaxbEHlsEyHyN0P6ZkFib5IuT0aQESIYY1blJeCH4ZSC5FgAluBCZM5wBB-T3Gi8DhTke9e5eBs64IKOuILFkI8fP3bzA9qCkU6QJd305cHfn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد @WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22582" target="_blank">📅 22:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22581">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22581" target="_blank">📅 22:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22580">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22580" target="_blank">📅 22:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22579">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFThhiHq1b5d8SYMuXxvoo1K2DIfJf1sGlCBGXQiMIxfMrirVjqBOgQWvp4pdG9_xDw7zJ6_AM8OjQXhuVTnCmdFDxiy4_CPcAWqa8CLolSmFoJQX7AFjm2GRvE_OveQ4PvlyKSYiwy2Q55ybN3lHqcZOXb6FxTtq7DmbNwwG-YpAaWJxGM-E83D0Wh0aADG-8Yy-FkRubxoVAeCD3Lzwh_Qvwias2F5u6z2eukWESw09DQbW_S8SCjxJ7Wf_FH5ms1tplEt0Ks86hu2D2Gw9LNL_LsqwRzIap0ahbrkQEyUI6SoNTL6RsUHWwKcVgvarMLbgPQpuxMnL2be4XPy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تانکر دریا» در لنگرگاه خارگ در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22579" target="_blank">📅 22:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22578">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22578" target="_blank">📅 22:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22577">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22577" target="_blank">📅 22:20 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22576">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدای انفجار ها در محدوده لنگرگاه جزیره ( محل نفتکش ها ) بوده و خارگ در ارامش کامل است تا این  لحظه @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22576" target="_blank">📅 22:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی سنتکام :
یک فروند زیردریایی بدون سرنشین ما روز گذشته طی یک ماموریت نقشه‌برداری از آب‌های سرزمینی دچار نقص فنی شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22575" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22574" target="_blank">📅 22:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش های زیاد تایید نشده ، خارگ آمریکا داره ۲ تا نفتکش رو میزنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22573" target="_blank">📅 22:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22572">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c17de1b0c.mp4?token=Ex5bQXyKkRLKERvFLR1eUwICMILZzfyawhWcQwSanPvUyx5hCooeGx7_QLUZQSxDmGaDyi3OgtyrWWWrwECQ7bD-7egbhcmNLE6RTh1WYB0LhEuZ8CDHa2XDvCCQMeOqf2xt2HMQqyFwxNBiKG4rl1Mc4a_APcI6DDwgOH2EAKSinULOo40XO1NRaZgWIp19GbvLU77UDTwCB9FqRXaWYY_ryKG5_HztBMsYBf_FGPbHXVfaNA3j17_rYHk2pFH7iaZvkP16EvQ9nEjXDlvOmhYN0EHH9epTQRv_OBXk9JbxcWTLgNBezwbQQjxPPDhp1gs4h9kk1inT5nrneX_P3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c17de1b0c.mp4?token=Ex5bQXyKkRLKERvFLR1eUwICMILZzfyawhWcQwSanPvUyx5hCooeGx7_QLUZQSxDmGaDyi3OgtyrWWWrwECQ7bD-7egbhcmNLE6RTh1WYB0LhEuZ8CDHa2XDvCCQMeOqf2xt2HMQqyFwxNBiKG4rl1Mc4a_APcI6DDwgOH2EAKSinULOo40XO1NRaZgWIp19GbvLU77UDTwCB9FqRXaWYY_ryKG5_HztBMsYBf_FGPbHXVfaNA3j17_rYHk2pFH7iaZvkP16EvQ9nEjXDlvOmhYN0EHH9epTQRv_OBXk9JbxcWTLgNBezwbQQjxPPDhp1gs4h9kk1inT5nrneX_P3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: یک زیردریایی نظامی آمریکایی بیش از یک روز پیش در خاورمیانه دچار نقص فنی شده بود. بر این اساس، ادعای سپاه پاسداران مبنی بر اینکه یک زیردریایی بدون سرنشین آمریکایی را در منطقه توقیف کرده، صحت ندارد و این شناور پیش از آن دچار نقص فنی شده بود. با این حال،…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22572" target="_blank">📅 22:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22571">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رویترز: یک زیردریایی نظامی آمریکایی بیش از یک روز پیش در خاورمیانه دچار نقص فنی شده بود.
بر این اساس، ادعای سپاه پاسداران مبنی بر اینکه یک زیردریایی بدون سرنشین آمریکایی را در منطقه توقیف کرده، صحت ندارد و این شناور پیش از آن دچار نقص فنی شده بود.
با این حال، آمریکا تاکنون به‌طور رسمی از دست دادن این سامانه را تأیید نکرده و مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22571" target="_blank">📅 21:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22570">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22570" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22569">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22569" target="_blank">📅 21:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گزارش های زیاد از صدای ۲ انفجار در جاسک
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22568" target="_blank">📅 21:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22567" target="_blank">📅 21:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HacEWxun-V2-UU1vtg_fEigsAgXlJW4y9xaYYevwKAQSb0fwWQHdatbywXxxHmGeyJSYB-IRDPkIgwchQs0EL5NAiH1yvf0MsgsQgorBn8q48cTvKBNYcMYBjclqHttUAyMXJs-cIYAJh0aUz1lKjslDmrzrVQvg-EXmVtdIR0Ow3-XQYDGkmy2sXys7zBYSt_uoPnmwaRxxO03O-Ul-IS2GsZs6uCwXVVzgWXPIv8xlAV_LPRGB8Xh0ga2e7sZVMhmcyoDU22N3WR7YvvDWb533hwK-nS_1WKPQVXXw0oB97jHNNwtg2O_pnqPBjur8WRzn1JaPMmsCQ6UcXH3Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپل فردا، چهارشنبه ۹ سپتامبر، رویداد ویژه خود را برگزار می‌کند و انتظار می‌رود از آیفون ۱۸ پرو، آیفون ۱۸ پرو مکس و آیفون اولترا؛ نخستین آیفون تاشوی اپل، رونمایی شود.این رویداد
ساعت ۲۰:۳۰ به وقت ایران
آغاز می‌شود. آیفون ۱۸ معمولی، آیفون ۱۸e و نسل جدید آیفون Air احتمالاً در مراسم فردا معرفی نمی‌شوند و عرضه آن‌ها به بهار ۲۰۲۷ موکول خواهد شد.
نام «آیفون اولترا» برای مدل تاشو هنوز به‌صورت رسمی از سوی اپل تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22566" target="_blank">📅 21:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=KUydvXxSAhxyTm8MhR8uVpIOeUPYHJS8RZOeaiK9OYrgG7IIawHj2JVTdahm4_IzldcTulItr6oIInvN4LOkegTTZgAT6x78x8Kk2QGERI2aWvBt7blszVONOz_PJ0kx8zw_EM-WKQKQ84-vTh16X6xVzD6XV3pyHhCAFcw9YiPhonQF4ODUT8t31K_fiA3SLB14YmvY7rljUTPeAypJ5Ah6g0NFxoV9eZvDGNbKPuu-zAGQf-NTS-1T8f_jUYp9sSrm0iFbcoW08ogJJcVZkxKc8ScGVthy_hrEwbjO_puzbytAP6lVc8kv1gqxIuaNVergJslTrdBbrpOkulB3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c4dcb0a04.mp4?token=KUydvXxSAhxyTm8MhR8uVpIOeUPYHJS8RZOeaiK9OYrgG7IIawHj2JVTdahm4_IzldcTulItr6oIInvN4LOkegTTZgAT6x78x8Kk2QGERI2aWvBt7blszVONOz_PJ0kx8zw_EM-WKQKQ84-vTh16X6xVzD6XV3pyHhCAFcw9YiPhonQF4ODUT8t31K_fiA3SLB14YmvY7rljUTPeAypJ5Ah6g0NFxoV9eZvDGNbKPuu-zAGQf-NTS-1T8f_jUYp9sSrm0iFbcoW08ogJJcVZkxKc8ScGVthy_hrEwbjO_puzbytAP6lVc8kv1gqxIuaNVergJslTrdBbrpOkulB3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و…. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22565" target="_blank">📅 20:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoorena</strong></div>
<div class="tg-text">سلام یاشار رفتم خونه پدربزرگ دیدم هی داره پزشکیان رو فحش میده بعد فهمیدم بخاطر پست هایی که مخصوص دارن گرونی رو میندازن گردن دولت پزشکیان به همراه همه این بدبختیا انگار این گرونی بنزین یه پروژه هست دوباره برای هدایت خشم مردم به سمت دولت و نه رژیم مردم باید خیلی هوشیار باشن</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22564" target="_blank">📅 20:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=kZNtUom0V43qW93O8XAvms_dJlqdtkokfhr9KTerliSZWt3s1S31cLnLb9NSg8PZeEA7Cmi4sSdy4jSeG51sQtB0XAAP_zSrRa3dbv-aykAoyr5XyErU6-aO_8xr9WPdHY6kMh0F8v2NRtmKMR9L4d_nb5dYcOAq_wA6tqm2u59ACcvYK0sjjsoZTzWb46UyBQ9rBxdZkjpk0fjoaJyusJJXG4sxMBJUAl0dGxDL1NTMEWOYDZg7cmQspYf9e9-J24kSpPl5Yg0N2DaQT4odm3-DeAvY4mZadvvvN0XG0PXvYgBbOD2J6prO-Pt3ZrE7cDWZWxb4HTID3kCNMemdtI4AMUY_2ItD1kYxw5-DwooLOdntV8LFmqBaa0fAEXN2u9qPTFQyY4IE3qKcSx77zUl1eLEW-hAxnJzZh7h-lDadenB9Cfs9VrUQiLVgWyu1X_VrAZ8cmiIOA8YH25tZe7LmzzhSzWlJMxMWTWEBmX4PhF2RoyEUzMeJZ42Q7cii5y0esVuXFhFRYy6wNInliYrXkIS_sauyi1z-wQvJ135Jfj7T98zHanjZ1c0l7fJpexx7FNr_aQLbJrps7T7YJ-qjHnH5f5p_RK3vhUv3ETa7mjH8Fz0wXiGlCQGjinP8krAGIfYO1pU9LY4o-_wM08z0FRufFDdgUb50DCeo1Ko" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cadaeb8025.mp4?token=kZNtUom0V43qW93O8XAvms_dJlqdtkokfhr9KTerliSZWt3s1S31cLnLb9NSg8PZeEA7Cmi4sSdy4jSeG51sQtB0XAAP_zSrRa3dbv-aykAoyr5XyErU6-aO_8xr9WPdHY6kMh0F8v2NRtmKMR9L4d_nb5dYcOAq_wA6tqm2u59ACcvYK0sjjsoZTzWb46UyBQ9rBxdZkjpk0fjoaJyusJJXG4sxMBJUAl0dGxDL1NTMEWOYDZg7cmQspYf9e9-J24kSpPl5Yg0N2DaQT4odm3-DeAvY4mZadvvvN0XG0PXvYgBbOD2J6prO-Pt3ZrE7cDWZWxb4HTID3kCNMemdtI4AMUY_2ItD1kYxw5-DwooLOdntV8LFmqBaa0fAEXN2u9qPTFQyY4IE3qKcSx77zUl1eLEW-hAxnJzZh7h-lDadenB9Cfs9VrUQiLVgWyu1X_VrAZ8cmiIOA8YH25tZe7LmzzhSzWlJMxMWTWEBmX4PhF2RoyEUzMeJZ42Q7cii5y0esVuXFhFRYy6wNInliYrXkIS_sauyi1z-wQvJ135Jfj7T98zHanjZ1c0l7fJpexx7FNr_aQLbJrps7T7YJ-qjHnH5f5p_RK3vhUv3ETa7mjH8Fz0wXiGlCQGjinP8krAGIfYO1pU9LY4o-_wM08z0FRufFDdgUb50DCeo1Ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، گفت: «وقتی بچه بودم و در کارولینای جنوبی زندگی می‌کردیم، خانه‌مان نزدیک یک مرداب بود. در حیاط‌مان مارهای سمی زیادی داشتیم. اگر سر مار را قطع کنید، مار مرده است؛ اما خودش نمی‌داند که مرده. بنابراین باید مراقب باشید، چون سر مار هنوز می‌تواند شما را نیش بزند و دمش هم ممکن است تا غروب آفتاب تکان بخورد. اما وقتی خورشید غروب می‌کند و هوا خنک می‌شود، دم هم دیگر از تکان خوردن می‌ایستد.
مار ایرانی، یعنی رهبری ایران، هنوز نمی‌داند که مرده است؛ اما مرده است.
»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22563" target="_blank">📅 20:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : آمریکا نمایشگاه هوایی زده رو تنگه
حدود ۱۰ سوخترسان ، پی۸ ، پهپاد و….
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22562" target="_blank">📅 20:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22561" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار ۲۲۹،۰۰۰ تومان (سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22560" target="_blank">📅 19:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22559">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt4egQONHJlNZpL1aZEhqNcdnTbW74sYPLoHCUE-YZw5EUrKLe5va8jQMRgIUSdbCcjqrySEGOZ_V5bRif598C1fLBYD066FLctbZtZCZX7cBTwl6_-AC0I08DBtWIsvHNmcOWhlgjrkPQcXsw-spWnC-kZD_OxiPDqZq-8RATKoptw16PynctXoGiAT7CElh-aKbT81xuUWcx3cKVxKzDkfAjq6jSZA-mID5Znu8LO1B3XnKHiHqhe1llfZljKDXfmsLIn4UeFdq6gz4weIysbT2gEGTuwfw3sF5L1RabN-i0_LJqfaBzm9biFMrjaAwdaZ17O6VeP6b99fUAkiQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا اعلام کرد هرگونه همکاری مؤسسات یا شرکت‌ها با صنایع هوایی ایران، می‌تواند به خروج آنها از تجارت جهانی منجر شود + لیست تمام شرکت های هواپیمایی‌تحریک شده
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22559" target="_blank">📅 19:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22558">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه مدعی به دام انداختن یک شناور زیرسطحی بدون‌سرنشین آمریکایی در دهانه تنگه هرمز شد. گزارش‌ها احتمال می‌دهند این شناور از نوع Dive-LD ساخت شرکت آمریکایی اندوریل باشد؛ رباتی حدود ۳ تُن با توان ۱۰ روز فعالیت زیر آب و عملیات در عمق ۶ هزار متری که برای شناسایی، نقشه‌برداری، کشف مین و پایش کابل‌ها و خطوط لوله استفاده می‌شود. در صورت تأیید، دسترسی ایران به فناوری و حسگرهای این سامانه می‌تواند اهمیت اطلاعاتی و نظامی قابل‌توجهی داشته باشد,
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22558" target="_blank">📅 19:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22557">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eab716e17.mp4?token=E6YFej-nDFjkeF-SMSAmMBRs_tZPNHCOkUQo9B5g8slHT0ikEACXwEKWEiL9TJabZlrKpt2XVUQ4B_v_xk_W1Mr_VDmXtMA5CW1rmAVascFQ65LdpHVhKMk3dv8CHXJFiCngLgFS8l1XuXjKho5vqIM7vHFdHH89ivZgLT692vedGK_SkwRW9AB3jGI9XXcx85QqFuhgIMaYniP67GMJnVDLEAtwkJVSzabqF0SEI-tcsSVkrH0GOQl8jE_5VPj29VCwZD6d-bi__i-wkb4TJr8E9lKqKlthjnyGOq_jIUKpzJyyjyvhQJhgH74kOm-BQk64PN7aGpiYNyz1SbcE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eab716e17.mp4?token=E6YFej-nDFjkeF-SMSAmMBRs_tZPNHCOkUQo9B5g8slHT0ikEACXwEKWEiL9TJabZlrKpt2XVUQ4B_v_xk_W1Mr_VDmXtMA5CW1rmAVascFQ65LdpHVhKMk3dv8CHXJFiCngLgFS8l1XuXjKho5vqIM7vHFdHH89ivZgLT692vedGK_SkwRW9AB3jGI9XXcx85QqFuhgIMaYniP67GMJnVDLEAtwkJVSzabqF0SEI-tcsSVkrH0GOQl8jE_5VPj29VCwZD6d-bi__i-wkb4TJr8E9lKqKlthjnyGOq_jIUKpzJyyjyvhQJhgH74kOm-BQk64PN7aGpiYNyz1SbcE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی‌بی‌اس نیوز: خلبان آمریکایی جنگنده‌ای که در جریان جنگ در ایران سقوط کرد، برای نخستین‌بار در برنامه «۶۰ دقیقه» درباره این حادثه و عملیات نجاتش صحبت خواهد کرد.
این گفت‌وگو قرار است
یکشنبه آینده
از شبکه CBS پخش شود و جزئیات تازه‌ای از ماجرای سقوط جنگنده و فرار و نجات خدمه در داخل ایران را روایت کند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22557" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22556">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شاهزاده رضا پهلوی در واکنش‌به پدر یکی از جاوید نام ها که به زندگی خود پایان داد؛ از روان‌شناسان، روان‌پزشکان و درمانگران ایرانی خواست برای حمایت فوری، مستمر و محرمانه از خانواده‌های جاویدنامان پیش‌قدم شوند. او همچنین از هم‌میهنان خواست منتظر درخواست کمک نمانند و اگر خانواده‌ای از جاویدنامان را می‌شناسند، به سراغشان بروند، احوالشان را بپرسند و در کنارشان بمانند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22556" target="_blank">📅 18:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22555">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c20f289d7.mp4?token=poPg5udJKO-hdX1atLLZoWFBMqkYsuqvlOv5Ce8qD4VY076IRrWjUGVHjVLEHWr5VA_l5owuSIlEVSVeRVm00XV1h1sH8FnvDuV9SrUorzRI0gjXWMJ0bsF_GYGbrq8AxsNfj7EuM2HJHsBm1R6st7YomB5Ig96LUW7BSF6oLVuxGzcQuBdXGMwIzwYvtExSA-I5C_vm_mw1C4mXBCtaGywRRI3IsRmK891nVbjpxHdiwv-TKPEQlw_LYW9SrLh1Mz8XH4ED1AaElIEu58FfpS8i_uYjMx_QjDfaqIr-RxVOAh3GJz6_2r4xzYw-efbatGNHwo_JDXSE6zku4GdfwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c20f289d7.mp4?token=poPg5udJKO-hdX1atLLZoWFBMqkYsuqvlOv5Ce8qD4VY076IRrWjUGVHjVLEHWr5VA_l5owuSIlEVSVeRVm00XV1h1sH8FnvDuV9SrUorzRI0gjXWMJ0bsF_GYGbrq8AxsNfj7EuM2HJHsBm1R6st7YomB5Ig96LUW7BSF6oLVuxGzcQuBdXGMwIzwYvtExSA-I5C_vm_mw1C4mXBCtaGywRRI3IsRmK891nVbjpxHdiwv-TKPEQlw_LYW9SrLh1Mz8XH4ED1AaElIEu58FfpS8i_uYjMx_QjDfaqIr-RxVOAh3GJz6_2r4xzYw-efbatGNHwo_JDXSE6zku4GdfwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ایران دیگر هیچ شانسی برای دستیابی به سلاح هسته‌ای ندارد و تحریم‌ها علیه آن مؤثر بوده و نتایجی فراتر از انتظارات به همراه داشته است.
ما الان داریم می‌جنگیم چون ایران می‌خواست سلاح هسته‌ای داشته باشد و خیلی به دستیابی به آن نزدیک بود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22555" target="_blank">📅 18:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22554">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بلومبرگ: نخست‌وزیر جدید بریتانیا با استفاده آمریکا از پایگاه‌های نظامی این کشور برای جنگ با جمهوری اسلامی مشکلی ندارد و این موضوع را تأیید کرده است
، دولت بریتانیا در چارچوب همکاری نظامی با آمریکا،
اجازه استفاده از پایگاه‌های بریتانیا برای عملیات مرتبط با درگیری با ایران
را داده است. این موضوع در حالی مطرح شده که نقش و میزان مشارکت نظامی لندن در جنگ با ایران همچنان مورد توجه است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22554" target="_blank">📅 18:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آمریکا ۲۸ شرکت هواپیمایی ایرانی را تحریم کرد
؛ دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا سه‌شنبه ۱۷ شهریور،
۲۸ شرکت هواپیمایی ایرانی، ۷ شرکت مرتبط با بخش هوانوردی و یک تبعه مصری ساکن امارات
را به فهرست تحریم‌ها اضافه کرد. از جمله شرکت‌های تحریم‌شده
آتا، چابهار، ایران‌ایرتور، آسمان، کیش، کارون، قشم، سپهران، تابان، زاگرس، وارش و فلای‌پرشیا
هستند. همچنین چند شرکت در
امارات، بریتانیا، ترکیه، مالزی و قزاقستان
به دلیل ارتباط با ماهان‌ایر یا شبکه‌های مرتبط با آن تحریم شدند. آمریکا همچنین
مجوز عمومی G-1 ایران برای صادرات مجدد موقت برخی هواپیماهای غیرنظامی به ایران را تعلیق کرد
و هم‌زمان مجوزهای جدیدی برای پایان دادن به برخی معاملات مرتبط با هوانوردی غیرنظامی صادر کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22553" target="_blank">📅 18:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تهران و کرج صدای رعد سنگینی شنیده شد همه نیم متر پریدن و فک کردن حمله شروع شده
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22552" target="_blank">📅 16:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خبرگزاری رسمی کره‌جنوبی،
یونهاپ (Yonhap)
، امروز گزارش داده وزارت دفاع کره‌جنوبی اعلام کرد یک تیم تحقیقاتی برای
ارزیابی وضعیت امنیتی تنگه هرمز و بررسی شرایط منطقه
اعزام شده است. سئول همچنان در حال بررسی گزینه اعزام نیرو برای مشارکت در تأمین امنیت کشتیرانی در هرمز است، اما
هنوز تصمیم نهایی درباره اعزام نیروی نظامی گرفته نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22551" target="_blank">📅 16:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22550" target="_blank">📅 16:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InXFCrw2u5E4VQ6DaPZ2fdNnYybm6iFl_IDaGO3J252uEtPGU6wqhzA6XOFfJrCgPKlYk4x6jJ9VGRAYVfBATHbK4BcsfHlhj8bqFB2GLYWWL8ma5A-qRmaF9B0cVY2W2embCLm08fV559GLFMqe-CrzJKLTQnZ_j9qswY6fjIzPyBGwhJ4UOtE6sGHYdXyLGaAfk-BKshEutlSzbHBriGVJ6l3a6x5iI-ByStcSuzZd6RjwEnL1SC8vqaYGR2ZH2XuhDNM3ui0sLpXhw0bp7J7RHfKSWUeHtUIL8j4Th2J-mKy7lBKZ2XHPpKtMACTLIKR2b-6WYPYFXN9FLkq0kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش های بسیار از صدای انفجار از محدوده زندان قزلحصار و هم اکنون عکس و رؤیت ستون دود از این محدوده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22549" target="_blank">📅 15:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22548">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ihWKxgSITWR6q0qB_T_q96vobtgajqsxo7So_7YnzrPqi3HHr8lv0LeYhUeRWlqitvfDzrcWqVoS2JTqXA6qzV6qV2O-7ZsEwdgtCjWSmo75tNhPSdnsQ42fIYubBGxH-FK9jqss0BxJvQ__-Oz7HT1QCdcHKXwohTz2CIFAty1jJcNAfpl7_ogJzkCdatIYKbmDr5CTBgxk0PQ-AZ1ar5WoI0VBD4oCylX_veaNlSu-rBa6ovA0lhi-VXbt9ENCUrsqz2oAE6jfqXujB11X4g4lQSCKZ4W3Xi7RDrbaTPvjSGDaNZlSfBDI2xdcIgpwiyZVhyvWqd1Pm73L1s6-5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">غرب شمال غزه هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22548" target="_blank">📅 15:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22547">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پزشکیان: نسل جدید با دستور همراه نمی‌شود؛ باید با او گفت‌وگو کرد
نمی‌توان صرفاً دستور داد و انتظار داشت نسل جدید از آن تبعیت کند. او تأکید کرد تحول در نظام تربیتی باید متناسب با شرایط نسل جدید و با نگاهی آینده‌نگر باشد و حل مسائل جامعه نیز به
تقویت گفت‌وگو و استفاده از ظرفیت‌های مردمی در مسجد و محله
نیاز دارد. وی همچنین گفت آنچه امروز در جامعه دیده می‌شود، برونداد نظام تربیتی کشور است و برخی فرصت‌ها برای تربیت نسل جدید در دوران کودکی و نوجوانی به اندازه کافی مورد استفاده قرار نگرفته است
@WarRoom
یاشار : این نسل شیک پاسارگادی خر نمیشه
🫶🏻
✌🏼</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22547" target="_blank">📅 15:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رویترز : دولت انگلیس امروز قوانین جدیدی برای تشدید فشار اقتصادی بر ایران ارائه کرد؛ این اقدامات
بخش‌های انرژی، فلزات، بانکداری، بیمه و کشتیرانی
را هدف قرار می‌دهد و محدودیت‌های تجاری و مالی علیه تهران را گسترش می‌دهد. همچنین اختیارات لندن برای تحریم کشتی‌های مرتبط با ایران افزایش یافته و
فرود هواپیماهای ایرانی در انگلیس ممنوع خواهد شد، مگر در موارد استثنایی
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22546" target="_blank">📅 15:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDvx4NO6IDT_GfeYfsXuAZIu44D6X9-SkseKwXTuFAL-DwuDwBCeFovUsw9a5wfjbIFKqYLmcXRER1skp6jmc6WkbBJdj5dO-baoBkm8EqBj5RD0lJ1mOim_OPdwzDBa2zu53rsbqDKZqJJJCDUm8ZnMk-VnrRGCHzqlk-EA3zQ_6IrD-StU__ISWbG1z4lEDtOW5qf0IBrmSlguAjFOo248tc7NDuI0gzGiR0HeDJPNftpvGN7ImXveSi_I2IEDTCZyWB5O1SYa93-vH54H6FbabCFhIJW-0cCeb4cX7uTLHxh06g0K7BUxXBzJk5Br5c8uqEReZJofE0maX1qWFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش عبدالرووف اسحاقی، فرمانده بسیج پارود در سیستان بلوچستان به هلاکت رسید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22545" target="_blank">📅 15:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ecqt_oA015W84Ha7WSquugjUpm-py04OZx-69FLU_pgK2jmlHrGXq2Nc29Amx2TyAvXwJdjvJRcm87NBqYaZbqSjTBaFvr7e6XSLy6Uu-8iuWIPezwRD4mbYR7whqsCrDIlGjhsVs7cGn9A_Itxm-LY7zVJ6SJfB4__XWXkMCJsojMk9aM0OeUm--g6oLt0aI4eJSX8XS_ld9x2FLdEPXL_gCWXLfLucid83c2ordcVGj_FHLqe8hgatJ5MFnV-ZN0GwQAmDRNZjRA0b1PU57bCd574nvv28dRnmCJNOy4UiMbGn4EwVTV_Z2zKnFlwQ3tcUE9HVwm7r8Lgpcvo67g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک بالستیک از کرمان به دریای مکران
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/22544" target="_blank">📅 14:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaDzhkZunR4IZK-38WkXteWUTdvVnDzPRNGdfYm1YQXVQDzLGhQsx0O7ifbYc7uN1QzR4pOkGO6nS4RzAKwCxYvEhc0TxqUDGcLaJl0NgME_BJIPKzcd1vHAKDrLIkmGYMZdJBHrFexUomRxaPCIoxr96ooufCK1zTcBU05EOf8YpChDrWVt6r-aU9GPv409Ys6DlZov3zNsQTDh7Mg7h0nCffSf8A4sI0bdQdkPCuJh1jvWVQNDG1hwKbp85Wong8i3XvBJjK9woITied9HhJxeAK_uVmABV298e8-O-XJEXSAwOqNqmI1iK521sb7q6PAMfFT38fth-6mDDMVuHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از کرمان به سمت تنگه هرمز، نقشه و عکس ارسالی
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/22543" target="_blank">📅 14:35 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
