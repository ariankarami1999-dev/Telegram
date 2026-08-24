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
<img src="https://cdn4.telesco.pe/file/Vudf0qAZ4gUSTsbCjpCpF7eKWp9LfcqgjQTS7l5wOSM5QNnmP4mSMIWyWH3vrW43ijb93b8lxUTnkffcOhhmSuJASK1PRRC1syAVDwYenII-yVEY2lJ6JXp7hQrNBndbLwgDu9_o4T2yLK1rOy5fTCsss8MTgcCvXULT-40MnkXh3sEbnZPQdxFu17AaCN_JmLv1erLpgdqvX2VxZPovFaqX89su2MIqcq_dAs3R2ED9QjtgTWlTNUoqKxGFKnrVGCIpOJk_YbsBlL3us6KQW__dpyhAaAVYUXryG4N0bNwnEB_gnzUb0_Qlrzxd-G4fhR0UtRXBbM8tOpOkVp-MJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 06:58:57</div>
<hr>

<div class="tg-post" id="msg-138853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🟢
تنها فقط تا پایان دوشنبه برای بونوس ویژه SCARABTEMPLE فرصت باقی مانده!
🔵
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
🔵
شارژ بیشتر؟ اسپین بیشتر!
🔵
هر چرخش، شانس دریافت جوایز نقدی
📌
فرصت محدوده؛ زمان زیادی باقی نمونده!
🔗
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SorkhTimes/138853" target="_blank">📅 01:30 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138852">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
مخالفت با معاوضه و انصراف پرسپولیس یا مصاحبه ساختگی ؟
❌
❌
فراز کمالوند در واکنش به مصاحبه منتشر شده از سوی وی پیرامون پیوستن ابوذر صفرزاده به  به پرسپولیس به شرط معاوضه با بازیکن مدنظرش به رسانه باشگاه خیبر گفته:
❌
❌
من هرگز چنین مصاحبه‌ای انجام نداده‌ام…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/138852" target="_blank">📅 23:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138851">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c596c40e2b.mp4?token=mQ9eVEbTlIEV7-BwmbwSiLjm4gBz74hFMFYpq8-nV8vOgQtqR_RcZxH_IwnROxbGSF6IuGD5wlVcHHfSYeYdQIeQByu9Br_ZGVJftzFPAacQprzCewWq0N3QCpW5BYU_9GNiF7jgWLKOFd84C-J056BaIWhoVvXVeE3Thzvl4YVinb16zo2_FScc2WzgdoIhVJvlsc7NbcI1QgpKfM2GhoFE_WjyWnumi--3nVFF5vsiopvhRAH4rr37FcM-3RWZ5Jsd2lrAjZnuOZDC3KWcvfzxqwsBqdETF9G95GfFD4W1QFF1d2yir6bJ1gm7OkBdGhfwmpLSI6E5O9yhCfxq2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c596c40e2b.mp4?token=mQ9eVEbTlIEV7-BwmbwSiLjm4gBz74hFMFYpq8-nV8vOgQtqR_RcZxH_IwnROxbGSF6IuGD5wlVcHHfSYeYdQIeQByu9Br_ZGVJftzFPAacQprzCewWq0N3QCpW5BYU_9GNiF7jgWLKOFd84C-J056BaIWhoVvXVeE3Thzvl4YVinb16zo2_FScc2WzgdoIhVJvlsc7NbcI1QgpKfM2GhoFE_WjyWnumi--3nVFF5vsiopvhRAH4rr37FcM-3RWZ5Jsd2lrAjZnuOZDC3KWcvfzxqwsBqdETF9G95GfFD4W1QFF1d2yir6bJ1gm7OkBdGhfwmpLSI6E5O9yhCfxq2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخی هواداران ترتر جلوی هتل پرسپولیس جمع شدن و دارن سروصدا ایجاد میکنن تا مانع استراحت بازیکنان پرسپولیس بشن!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/138851" target="_blank">📅 23:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138850">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه؛
🔻
سرگیف و علیپور زوج خط حمله
🔴
بیفوما فیکس خواهد بود
🔴
اورونوف نیمکت‌نشین
🔻
تیکدری دفاع راست
🔴
عیدی دفاع چپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/138850" target="_blank">📅 23:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138849">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
رونمایی از کیت دوم پرسپولیس به یاد کودکان مظلوم میناب
پ.ن نظرتون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/138849" target="_blank">📅 23:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138845">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O7BW4Ww2_9AbtN_oDaGo5hAm8el-Mekb5Y5LNTZjvepmQhJrIOEsPlQ74By51ehzT7eXH_NeHBaidYcY2_2GfAhXO5sBiq0MLtmHEvgsbWLKX1XDsRk05Cc_pTGKhXmt0e99niqbW73y1EVCTVbqQsvu37pNaL9sUdvdFWgcoyBpu0EEuG4YCiirWxcgRr868jHfRT31QpDZb1nPzbf7c7Sx6VMA17UY3lgdC6fqzI0dDZOrUJ1qkyIjRLje0jWDqmzqyyJzTzpYgHHZiBZI1FGC1Z1zCFeM7slO5SClZK7U6DDAPjG6B9AN-TkleprPotyF0OfQZ3duEtww26uhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ucMdS_-RwEJggPysVhC6JcGPwcts7GazrTtVSUegVPeBBcSQJvA6jAHWUT5gkBXMg01C-SHKJhlWADkknZvvRLWlRxrLmWnxCCNdoKGNs7C8IHMP4-gOqbyRxxrD5LH-OVW2NUU-eiCo4bGEngbhdqKr9BVfCde4f2kWjK00U4JqA0ThGlsT14Iz93L9-cMAzY1JL3mKyX1r54avL7gkYZXL7Qga_m70FhXjdpZBMHF1Lvm-9IF1XLbxMxBaZKTqbBkO3smsR38UXT9pJ92mfP-L1g2wpxWqXBe6Z9T4YQKMbt7n9bzyXOjGDc-kxE1eC3q4uFpiOThNdQ_OLaEbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hYEiccYGsY3sy3BCFL0q5z5owwTmXsYZdzPR_ywF3rnzvABcLQo-y9JQyKWHvqKjpYDHXQ2qqb7vOjyfLRQMlPUVUAymVWt-Q5Qzg7SXaY3jpiCToGmd1T_F8ctY9VygwZX2t0FWBNdRDON-iadrD7zw4GIge310k9UP3TIGhaFDGq7Jf4E4nW9V_EC9BDg9wmCx-KbpJwyAaZMc4ot8gj14zNpLv3Ki2WG11-dBA8SESbjAL2wyKDyF21KXhk5yNHNMKCTdgZ0QHvzPgZedTgb5gsDuFE0HiKCCqysrJPbFHt53pucRTNOjJMG8D6Vx9n1YWbO8IP3Vriykcwtaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1E1bsVW8R5DW2R_3fe9rrvD9qAY9Uvzl6FM5DxgJSjwUdRT_E7pdB8SKd-bHqP6BJzC-0LdSHZdLYq-3ClKf92-J8DKALbzVcbevNCKd9kOxV3hIzzDkp1W8NZqxT-ZesYrUrswZrfPb9um7-mosQREKb7WjjsD1rCF8HbxNRYjWvSrau79Og5nGf4wXijJxdLb83c2Kkg9aA5ds4WKVPdn0Bsb7Z4DVoGsdEYFHiQe7mRSbpcv4eGGIm_l1N-2aYWM3v8OPGAE0A1ZP5sTlIR2kY90jO1R42kX6naqLes_FBk3eagbR50oVikQ5tuG7R09gNd3tHy2Yz0AHC2UOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
💢
پیراهن فصل‌جدید بعد از ادیت نهایی رونمایی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/138845" target="_blank">📅 23:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138844">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🔴
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید فوتبالی:
🔴
نیازمند
🔴
تیکدری کنعانی زارع عیدی
🔴
پورعلی خدابنده‌لو
🔴
بیفوما محبی
🔴
سرگیف علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/138844" target="_blank">📅 23:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138843">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/138843" target="_blank">📅 22:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138842">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
میثاقی: کمیته انضباطی شکایت مس شهربابک و نساجی مازندران رو رد میکنه و گفتن آسانی مشکل نداره و هرکسی اعتراض داره بره cas
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/138842" target="_blank">📅 22:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138841">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138841" target="_blank">📅 21:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138840">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPBMsjpyVmc_aIOg1eAEHkW50pnV3_0VPbQy69-nP5r0ZqJzTLjdOaFWaqZMRR1k-bjZCVPI-tCCcVkFs_WgMsVEOLealbOXwkgOKpq2j5KlHFjFCsEp1ojnlk9woRXV1cCzrdQaRVqmOxDXECVFNtVSddkPK78yq77_oSHnlDSANxD58h-lfSgW6DNCNCJns03QMUZtIG14g9KGC8ZK0IMRMKo48yx3BFNEj3wNuGn0RPhQ6wEXjrPntyxWzdaavzhOOf071BWbqu7qGtjuLL6ZhzG7VkP9s0G6Jr_v05pdH5EJyuTasbdbVtlrnzrb1i7sSkQDtixxMZVqMa0XvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام ترانسفرمارکت؛
علیرضا عنایت‌زاده به صورت قرضی به مس شهربابک پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/138840" target="_blank">📅 21:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138839">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0i0rPmV1W0yhgM3PcyIttsWxISnGZVXYfkzp1FhYPZKfDzazoaDLaIHFlKuWimjLTaBTBnC8ulUOiyuV7IDOs1pB-3LGKbPj8X8RVQBYvgFyKrdJMHjhJ3zsAcVvAV9j8mPY_PdPuxyi_ioYksm33giC9BCILAseB2UW8ClNCcNSiawLcyLA3n3xBavh9ykj-kuJY5ZAauzLCycqIpexR0aRn44WLeg2KYsPJqVtso_9Hbs8RPhs3MUakHtBsx2S2Zypcy0cGlWOvkZv93yIsGbS437lhVjeo1oFDzGHsjOmps8RVDMRqo5gcuUymR93QvmC-vekgDwO7kKSKla-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
نتایج بازی‌های امروز هفته 3 لیگ برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138839" target="_blank">📅 21:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138838">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
❌
کیسه دو بر صفر از سپاهان جلوعه.....
❌
❌
سپاهان خیلیییی شخمیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/138838" target="_blank">📅 21:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138837">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
ترکیب احتمالی پرسپولیس مقابل تراکتور از دید فوتبالی:
🔴
نیازمند
🔴
تیکدری کنعانی زارع عیدی
🔴
پورعلی خدابنده‌لو
🔴
بیفوما محبی
🔴
سرگیف علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/138837" target="_blank">📅 21:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138836">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✔️
✔️
✔️
✔️
۷۲ ساعت سرنوشت‌ساز برای پرسپولیس؛ تلاش برای جذب گزینه‌های نقل‌وانتقالاتی
✔️
✔️
در حالی که تنها ۷۲ ساعت تا پایان پنجره نقل‌وانتقالات تابستانی باقی مانده، باشگاه پرسپولیس تلاش می‌کند پرونده جذب گزینه‌های مدنظر خود را نهایی و ترکیب تیم خود را تکمیل کند.…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/138836" target="_blank">📅 21:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138835">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
حضور هیچ بازیکنی در ترکیب پرسپولیس تضمینی نیست و تارتار از روی عملکردشون در تمرینات ترکیب میچینه/ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/138835" target="_blank">📅 21:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138834">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYcppC6Dilw2TCqwz8SG7vZAVYD--6jOcqNC2m6RDRJKOYg7jx498ziumzqHZpzSkNfO53B2X8D-eu1Gr5PlqjW9AL652IkI4j6iM-mLOXkmof2-hqz9SxcrFlIetv4u0mZfrI07qfzvji8uuWp_cw8vCm0KoPStDwmiklQTvd6aivziiw6S2q1YjzV6bM_xQziHyKkXcbEVzlO1oMIqtGnPHKUEXjb2vhhIX22lWmV2HE-9vHfLaHmGP19d1ZYFkLMQROwqJGxaarBQ_9dsts-f4AEBlZRsFkSwGzwjXTsu2S07qy9VMeYSSNnIirLjlBrTGInNdP35kCH3JlYLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تنها فقط تا فرداشب فرصت برای بونوس ویژه بازی Scarab Temple باقی مانده!
🔵
کاربران اسپورت‌نود می‌توانند با هر بار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود ‌اسپین رایگان کازینو دریافت کنند.
🔵
هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد! با هر چرخش، شانس برنده شدن جوایز نقدی را دارید؛ جوایزی که بدون هیچ قید و شرطی مستقیماً به موجودی اصلی شما اضافه می‌شوند.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/138834" target="_blank">📅 21:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🤝
🤝
🤝
کمالوند، سرمربی خیبر: ابوذر بازیکنی است که به کار پرسپولیس می‌آید
✔️
✔️
ابوذر صفرزاده از خریدهای خوب امسال ماست و من به باشگاه اعلام کردم تنها به شرطی که مانع جدایی او نخواهم شد که با پرسپولیس برای خرید یک بازیکن جدید به توافق برسیم.
✔️
✔️
ابوذر بازیکنی…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/138833" target="_blank">📅 21:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
با اعلام فراز کمالوند سرمربی خیبر خرم آباد ابوذر صفرزاده به پرسپولیس خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/138832" target="_blank">📅 21:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
تارتار:
🗣
🗣
فیفادی که نیست‌؛ به تیم امید که هیچی به هیچکس بازیکن نمیدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/138831" target="_blank">📅 20:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/138830" target="_blank">📅 20:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
نکونام:
❌
تارتار با گرفتن سهمیه آسیایی با گل‌گهر کار بزرگی کرد و حضورش روی نیمکت پرسپولیس هم نشون میده که واقعاً لیاقت این جایگاه رو داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/138829" target="_blank">📅 20:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138828" target="_blank">📅 20:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
✔️
✔️
وضعیت عمری امیدوارکننده شد
❌
❌
وضعیت محمد عمری که در دیدار مقابل استقلال خوزستان دچار مصدومیت شده بود، بهبود پیدا کرده و شرایط این بازیکن امیدوارکننده‌تر از روزهای گذشته است.
❌
❌
عمری امروز تست نهایی پزشکی را پشت سر خواهد گذاشت تا مشخص شود می‌تواند پرسپولیس…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/138827" target="_blank">📅 20:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
❌
❌
فوری از عطا حسینی فرد نزدیک به تراکتور:
✅
هاشم نژاد و ترابی به بازی پرسپولیس نخواهند رسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/138826" target="_blank">📅 20:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
حسینی قشنگ داره بازی و برای کیسه در میاره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/138825" target="_blank">📅 20:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
سیدحسین حسینی: این توپ ها تازه به لیگ آمده و هنوز به این توپ‌ها عادت نکردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/138824" target="_blank">📅 20:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
▶️
⚽
به گزارش رسانه «سرخ تایمز» جذب محمد قربانی به دلیل مخالفت باشگاه الوحده به انتقال او به باشگاه های ایرانی منتفی شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/138823" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
با اعلام فراز کمالوند سرمربی خیبر خرم آباد ابوذر صفرزاده به پرسپولیس خواهد پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138822" target="_blank">📅 18:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✔️
✔️
✔️
پرسپولیس به دنبال جذب ابوذر صفرزاده مدافع چپ سابق تارتار در ملوان بندر انزلی/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/138821" target="_blank">📅 18:51 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
❌
فوری؛ بیانیه کمیته انضباطی علیه استقلال تراکتور و گلگهر: ندادن بازیکن به تیم ملی در هر رده سنی به هر دلیلی تخلف حساب میشه و حضور بازیکنان حاضر در لیست در اردو ملزمه و هر تیمی سرپیچی کنه باهاش به شدت برخورد میشه و بازیکنان از حضور در لیگ برتر محروم میشن و…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138820" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
❌
❌
استقلال، تراکتور و پرسپولیس اعلام کردن قرار نیست بازیکن به تیم امید بدن! با این حساب ۱۰ ۱۲ تا بازیکن از این لیست خط میخوره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/138819" target="_blank">📅 18:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138818">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🤥
🤥
#شنیده ها
👀
مهدی تارتار قصد دارد در دیدار مقابل تراکتور از سیستم 3 دفاعه برای مهار شهریار مغانلو و حسین زاده استفاده کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138818" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/138817" target="_blank">📅 16:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
✔️
پرسپولیس تا پایان نقل و انتقالات ۲ بازیکن دیگه جذب میکنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138816" target="_blank">📅 16:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_xLmgR4h845oydL3Vu_fknOD4ITyEW7N_vSbjpjG1bkyJW8mwKvHRQqenWVoh7cmCIkY4WJ6h-RPwADI9a4gp4bTBLBpIpCDeQRrshCBUuJOaIndt8xUJilfnClTOrxnoFbhkl7_LkeCTZwmIkaD7I5hoFr_Z8Ji9xbZwz40VA_3KRSrzxem1YTPO0a9m8y4Pu4AD2ciWnsrRBnd0sF00FBLfAA6xcb_g1elzNMysoo24yTagUbrBaUA6YxanqTSGfGf6rOV4Pbd7QyVAMDYqT3QKCeoQPBPsiv1UhXmIZ64RiH0Cm3DPI7TJDJ4dBbOz_raNtQclUkNKCdrGjX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
همه شواهد و مدارک حاکی از سرباز شدن علیرضا صفربیرانوند پس از بازی با پرسپولیس است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138815" target="_blank">📅 14:55 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138814">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
مدیریت پرسپولیس در تلاشه تا ۷۲ ساعت آینده قربانی و امیر جعفری رو جذب کنه
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/138814" target="_blank">📅 14:47 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138813">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
✔️
خبر سرباز بودن بیرو به هیئت فوتبال آذربایجان شرقی ابلاغ شد
👍
بر اساس آخرین استعلام هیئت فوتبال آذربایجان شرقی از سازمان نظام وظیفه، معافیت تحصیلی علیرضا بیرانوند تا اول مهرماه ۱۴۰۵ اعتبار دارد، اما طبق مقررات فعلی، او تا پایان نقل‌وانتقالات (چهارم شهریور)…</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/138813" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138812">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/138812" target="_blank">📅 14:45 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138811">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlcmGbQ0mQbzymOACX8pPDttkYKPm_GhKj2M_qoYZu3QxgwdCubZId3q-3kSMi6PKmhTr_cW5m_-nZMmcrfolpntWER1c4OFcd8og_0AnWUA98iw7SxQDrWyzDX5a2twb-Oclnf5lcHqSdSRMVq0eEtji0oLKK0drWZBtXNWYqaXDGZ6n2zHb4xwM19SBLpI26yM27zkB7CG-oK1eGmPCZGlkD0rxI4kt4246oyFn-JRku-Y44Q8x9fFRTPoZoa8nYP9JxHo7qhNRJNcMQwDsp9iKN5-eDMPoXDeMpe5xALEBoqmI0pl4UxN2Zxq7wvu5T6KQG2TslFrsV5FoxuIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد مدعیان در شهر قدس!
استقلالِ آماده مقابل سپاهانِ مدعی؛ یک بازی حساس که می‌تونه معادلات بالای جدول رو از همین هفته تغییر بده!
[
استقلال
⚽
🆚
⚽
سپاهان
]
🔵
بونوس ویژه بازی Scarab Temple در اسپورت‌نود، کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/138811" target="_blank">📅 14:08 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138810">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/138810" target="_blank">📅 13:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138809">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/138809" target="_blank">📅 13:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138808">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
مدیریت پرسپولیس در تلاشه تا ۷۲ ساعت آینده قربانی و امیر جعفری رو جذب کنه
🔴
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138808" target="_blank">📅 13:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138807">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
پرسپولیس همچنان در به در دنبال مدافع چپ ..این معضل ادامه داره.. کسی برای جذب نیست ...رایزنی ها ادامه داره ///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138807" target="_blank">📅 13:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138806">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/138806" target="_blank">📅 13:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/138805" target="_blank">📅 13:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
باشگاه الوحده امارات جواب آخرین نامه پرسپولیس رو هم نداد و به نظر میرسه قربانی در الوحده موندنی شده / فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138804" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138803">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✔️
✔️
الوحده با 3 بازیکن تهاجمی به توافق رسیده و تا زمانی که لیستش و خالی نکنه امکان عقد قرارداد جدید نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/138803" target="_blank">📅 11:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138802">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🇮🇷
عکس یادگاری یحیی گل‌محمدی و علیرضا منصوریان در حاشیه دیدار دوستانه دهوک و الطلبه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/138802" target="_blank">📅 11:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138801">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✔️
✔️
خبرنگار اسپورت امارات: قطعی شد محمد قربانی از الوحده جدا خواهد شد و به ایران باز میگردد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/138801" target="_blank">📅 11:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUPOHUBpEjIM8XSlIHDuss0JFgA-OzZs2J5AgtThFaXxS9j2NukX9geKBGhzge2j9Db5x3vlMuff1th-05_ke9fwAY_VuZfMXOtigKjkmlwMlFSO8smM3bkEVSaR6rXUgSyzY9S8tAEVd3yjupMqgivC5PmWeN7F7AvPgECWWDzEGJkns7sUEqeYKD2yontFG7ayXxQxne9ASOmfgGOUiLbXiTotHZPGHOON0z3tLBwORSlavpfw137cKaxmuiKbfeohLOuRxzF9Q1ajCzOiv5qdvLt31eXxrdZdOD8byxE0jmXNIlYiTUZwytL8-8GVwSZWZXVan8k16Bl9d3LeWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایجنت دنیل گرا:
✔️
«دنیل به قراردادش با پرسپولیس پایبند است و بعد از پشت سر گذاشتن مصدومیت، با تمام توان برمی‌گردد.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/138800" target="_blank">📅 09:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
العازی‌ خبرنگار اسپورت‌ امارات:
👀
🇮🇷
محمد قربانی دراین پنجره‌ از تیم‌الوحده‌امارات جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/138799" target="_blank">📅 09:28 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری
🚨
العازی‌ خبرنگار اسپورت‌ امارات:
👀
🇮🇷
محمد قربانی دراین پنجره‌ از تیم‌الوحده‌امارات جدا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/138798" target="_blank">📅 09:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rxb8QtoRC1-xnrlHnT5X8ujRpFiErA0MZ3R6l0CizPP4-Z4ErYts9PCFinDdq6TE5XupETu8f0psDBkyMgU23tMAwbNybE2FOA8K0CNP8HIfMfUjd_Dx-gS9KcfPIlXWrpq9xYGi2QtZK1SPHq0guiOEQx8g_Cp_aqRBu9dFZIrpc9ql7f6m7dN8pmuRMAUZdBajPw_Kka2hVMrgFaShlxx525HoHqckm_imrKHYLl3Z-QZLnpkb5lmElBnsypL0RE6FQGslW31d_Zcnt6BnCV9NTY6h3HuvB_A_fBpzxMivf896-M8zYXdB0AxtrfQiidD4-PS4NZAC5USV6XvXTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/138797" target="_blank">📅 09:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138796">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkXL7lKf9LGPXnS4N0QLENa9LF93IJEVg3-1QqXQO2g_5pg2LkXT1CfR5j9WGRZ7hhaS0x97rpC1l_i3pG0V4p63iqzPfUW2yBNs2Rf-plo7t9zTfvOok3kahXU334wVHrUVa7JIMh25Bi7wbq4HLcHfC_bbXKRQ_oPgCXnyQBs7q6r8fYFrYew3c6KMQFlCk4zWjcGQ7Bz0j3llqlnoZyn74JogM5lskxNEHiJ8w_v6439RZg1jTu273KaflhgT2DP3_ZYJ8H2smpJ7khZnFiinQ9lHWQBBsP3Q_2MEsB2pmL3kszLNUman2BU1PYsQaHGBHqB1zAxmV5AAawM04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه بازی Scarab Temple
🔵
کاربران می‌توانند با هر واریز واجد شرایط، متناسب با مبلغ واریزی خود برای بازی Scarab Temple چرخش رایگان دریافت کنند.
در عکس فوق شرایط دریافت چرخش این بونوس ویژه توضیح داده شده! هرچه مبلغ شارژ بیشتر باشد، چرخش رایگان بیشتری دریافت خواهید کرد.
🔗
آدرس ورود به سایت اسپورت‌نود:
👇
📌
نسخه جدید سایت:
Sportn5b2.com
📌
نسخه قدیمی سایت:
Sport90.bet
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/138796" target="_blank">📅 01:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/SorkhTimes/138795" target="_blank">📅 01:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
پرسپولیسی‌های تراکتور:
🗣
علیرضا بیرانوند - شجاع خلیل‌زاده - فرشاد فرجی - دانیال اسماعیلی‌فر - مهدی شیری -صادق محرمی - محمد نادری - مهدی ترابی -شهریار مغانلو
🗣
تراکتوری‌های پرسپولیس:
✔️
مهدی تیکدری - پویا پورعلی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138794" target="_blank">📅 00:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/138793" target="_blank">📅 00:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138792" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
✅
✅
فقط تا چهارشنبه پنجره نقل و انتقالاتی بازه و تکلیف قربانی باید معلوم بشه.بعد از چهارشنبه دیگه فقط میشه بازیکن آزاد گرفت   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138791" target="_blank">📅 23:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
انقلاب در الوحده پس از دو شکست!
🔴
مدیران باشگاه الوحده پس از دو شکست پیاپی در شروع لیگ دست به اقدام تاریخی زدن و در یک روز با سه بازیکن خارجی سطح بالا توافق کردن و به زودی از اونها رونمایی میکنن
🔴
با توجه به جذب این سه بازیکن به زودی دو بازیکن خارجی از…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138790" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم!
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138789" target="_blank">📅 22:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138788">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
انقلاب در الوحده پس از دو شکست!
🔴
مدیران باشگاه الوحده پس از دو شکست پیاپی در شروع لیگ دست به اقدام تاریخی زدن و در یک روز با سه بازیکن خارجی سطح بالا توافق کردن و به زودی از اونها رونمایی میکنن
🔴
با توجه به جذب این سه بازیکن به زودی دو بازیکن خارجی از…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138788" target="_blank">📅 22:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138787">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=Dngry_LEAO52Q2iXPtW21_zyRDgB6ENFX3J-sxKptRiiFptHlH3MRjDCAdf_Ivyr2WrP9Bp-wNpwRKV6A16ghTUoCVnrwbDB1yV4GpkRUvOD8oRRJPKks2deeSwPU5DfMPgRjYi_JCDksWuETzbmTITeauqGkPdvDHsNP7xj8ADSPr7u7MfVHPR74u189FHi0DWRku5SKT7PfXkwIugw06PR-5qmrhixxojyc_RDux81pePwqg1SJa8I3-frVm_OlyPI_3jV0zJLotcIbnu5mU0co9FeCut0hHA-I3nn4NgW4jB6MukPYmyIDjL1zpzBTbeqRasqCrlp7Zp8Ux0lng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1145503d.mp4?token=Dngry_LEAO52Q2iXPtW21_zyRDgB6ENFX3J-sxKptRiiFptHlH3MRjDCAdf_Ivyr2WrP9Bp-wNpwRKV6A16ghTUoCVnrwbDB1yV4GpkRUvOD8oRRJPKks2deeSwPU5DfMPgRjYi_JCDksWuETzbmTITeauqGkPdvDHsNP7xj8ADSPr7u7MfVHPR74u189FHi0DWRku5SKT7PfXkwIugw06PR-5qmrhixxojyc_RDux81pePwqg1SJa8I3-frVm_OlyPI_3jV0zJLotcIbnu5mU0co9FeCut0hHA-I3nn4NgW4jB6MukPYmyIDjL1zpzBTbeqRasqCrlp7Zp8Ux0lng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
علی قلی‌زاده: امیدوارم سال آینده در پرسپولیس باشم!
💬
فصل گذشته تمام کارهای انتقال من به پرسپولیس انجام شده بود اما ناگهان ورق برگشت/ باشگاه لخ‌پوزنان امروز یک‌رقم می‌خواست و فردا رقم رضایت‌نامه را افزایش می‌داد/ به هرحال این ماجراها بین باشگاه‌ها طبیعی است/ امیدوارم سال آینده در پرسپولیس حضور داشته باشم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/138787" target="_blank">📅 22:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138786">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/138786" target="_blank">📅 22:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138785">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFv5J9oUfc8MyzwJNOLNd7e56jmVItSWBnShZxF9-IC-aLPpmERjpZfdl53OGYjXKGx7es6VBP_efqSNjZRc4Dbje9h9kQ_XQoF--QunEx7wwWUoWpdDV1dYpjOjnz8KmWNiwQ71eOA6RDUZxSsy1GxXIsBYDMxsyA00NsuaXD5PoKtca-Bt4JZ8yakOhS5LUWJpsZ4B5d91YgxUnwdGxbyWBgcmEMWY4c-8VNQ2Ddfbmstf93JDAX-SbobztvKYZzIdJVCeBujOxSio9lRL997AWGIoPjM_vKUM3QkO3Aoz1UTjaIwyrw2p9hEDZzDb6nUGAGA_uk72IvcEp6TdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بازگشت آقای خاص؛ شروع دوباره کهکشانی‌ها!
🔥
- رئال مادرید در اولین آزمون فصل، مهمان اسپانیول؛ آیا مورینیو با ۳ امتیاز برمی‌گردد؟
[
اسپانیول
⚽️
🆚
⚽️
رئال‌مادرید
]
🎁
بونوس ویژه بازی Scarab Temple در اسپورت‌نود، کاربران می‌توانند با هربار شارژ حداقل ۱ میلیون تومان، متناسب با مبلغ شارژ خود اسپین رایگان کازینو دریافت کنند.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138785" target="_blank">📅 22:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138784">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💢
💢
🚨
مدیران باشگاه الوحده امارات پس از شکست در دیدار امروزشان به دنبال جذب دو بازیکن خارجی جدید هستند و از همین روز از نماینده محمد قربانی دعوت کرده اند فردا برای جدایی و فروش این بازیکن به باشگاه برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/138784" target="_blank">📅 21:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138783">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/138783" target="_blank">📅 21:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138782">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
✔️
رسمی شد؛ مهدی طارمی به الوصل امارات، حریف استقلال‌ و تراکتور در لیگ نخبگان آسیا پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138782" target="_blank">📅 21:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138781">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wb-8LZYwYqnsPs3Jy7OGqnFmvsGqG3312u6JrQQyq8gQBPsWWDBgS2-TGCVeqg0vb5fEkLbM7LoMEVQlg_IKDp0NpNfj5pK1Zf9kTz8dEt50fZwQ6byXrQ_3zpvY4vu8wmNg8VNOjZcWcnVgxffllIRJz9ytDyMWpHucoGXinb7Q3yRCyJeBq9RHqa2A2P8kOdF7byepImMy3daChCyqNQ0aSSGF2loJWsWR_RFFNr2yGB5avv-JB8vAZJfa-j7TpU2GecsmWhumJfL7rFxmV72fVhB4JwS_ujYeeD-uZpEZAFXkyElNFdfBCelb6Frq7DUY87tN8GYcT6FJr-UAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138781" target="_blank">📅 21:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138780">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrgPAIct_N87KxPqQLUKwmDu4ZrULSahKPRWhQhpwQ34-yprKAB2LnP2doDXYmTHpJ_xeu1-fED9-y57AAZ76wFoLv1HZEFmiCwgCnLV2GsCYNg04vdBroOB7Bb2xjtQV7YbQFY_S70fwxNxAoTcdojFQB8VSyCqO0RzLBl-OAS-JXkKb79PZZYdg_AZ_NZbf9jIeS7vuET71_6vJaMda1TAOXKHmiJDTowftAelTWgZjgbb4beP4wkSYWTS8wUFQJg487haAkaN6agdWmK_-SjFO2i_LRgjK7AjPwRIPmCOQ2Jw6zDKJBlOw2T_luwx0vGZ35q01-m99C-OAdk5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔹
سمیه آوج، الهه افشاردوست، سمیه اسماعیلی و کیمیا عباس‌زاده با امضای قراردادهای خود به تیم بانوان باشگاه پرسپولیس پیوستند.
🗣
✍️
همچنین قرارداد الهام عبدالرحمانی نیز برای دو فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/138780" target="_blank">📅 20:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138779">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138779" target="_blank">📅 19:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138778">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
❌
لیست تیم ملی امید برای شرکت در مسابقات آسیایی ناگویا اعلام شد
🗣
🗣
دانیال ایری، پوریا لطیفی فر و پوریا شهرآبادی از پرسپولیس به تیم ملی امید دعوت شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138778" target="_blank">📅 18:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138777">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dk93kMKNHeAmIjN7yppHy3wk6QC-_k68hdAvzKBnVQLOkpJ1H8q9WMfPgqvFf2nm98PNMVOsSQJLewBYfyvhlu51EYKgAOSpDCMH3njdO5aRJNeXCNofl06yzhP6XZ0t6NhRGtRe9k8uEXEvhedQfgbyhAdcOQQtmFyIB40SVfMfYlTyBVhyFzZx1Jjlc6dLQ_os5dqxkJ1KeoNdlZGsGHNffNvZ_Q2JyMAJ8Rv5eEqw-VaJSafQHS05Ej_V-P5xXvJO-rucah1nJskfRdXqNkjayz-x5nxO-plgr86pizdDGpkHvRNMs2IKRsd7919C2WgBck2W_MsilqMNAoZqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هواداران ملوان در واکنش به سرباز شدن علیرضا بیرانوند، کمپین نه به بیرانوند را راه انداختند!
👍
👍
👍
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/138777" target="_blank">📅 18:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138776">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔄
🔄
بازی با پرسپولیس آخرین حضور بیرانوند در تراکتور؛ بیرو در راه فجرسپاسی!
✔️
✔️
علیرضا بیرانوند به گفته مسئولان نظام وظیفه باید از اول مهرماه راهی خدمت سربازی شود. این در حالی است که بیرانوند اکنون در تراکتور حضور دارد و نقل‌و‌انتقالات تابستانی فوتبال ایران…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138776" target="_blank">📅 18:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138775">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
امیر عرب‌باقری داور دیدار تراکتور و پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138775" target="_blank">📅 18:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138774">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
✅
فووووووووووووری
🚨
انتقال امیر جعفری به پرسپولیس کنسل شد و گل گهر مخالفت کرد  / ورزش سه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/138774" target="_blank">📅 15:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138773">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚽️
⚽️
⚽️
⚽️
از بین ابرقویی، تیکدری یا عیدی یکی دفاع چپ پرسپولیس مقابل تراکتور خواهد بود/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/138773" target="_blank">📅 15:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138772">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
فوووووووری / فارس :
❌
جدایی رزاق پور از فولاد منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/138772" target="_blank">📅 15:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138771">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
✔️
رسمی شد؛ مهدی طارمی به الوصل امارات، حریف استقلال‌ و تراکتور در لیگ نخبگان آسیا پیوست.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138771" target="_blank">📅 15:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138770">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/SorkhTimes/138770" target="_blank">📅 15:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138769">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند هیچ راه فراری برای نرفتن به سربازی نداره و قطعا مهر ماه سرباز میشه
😂
/ تسنیم  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/138769" target="_blank">📅 15:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138768">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/138768" target="_blank">📅 14:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138767">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGhCmDReKJmL_rRP7W-OW_Bpz1YNSO7hBjt9TNHyh2qIZYuGwvgU_5tTScTPMJC5n_pEmCbEU8Eidsze7VKekrmNvsDlvG5p4kSvHBR5wmEROmmBqnkVpOfP5wIRbyD2fMGLa-cYExOL8frtidPGmX-m-ArANi8PE_I7-oXgWzC97RZ7lv0TmASiDGPudNDxEnCJQEK3M_z2HigWeytyo8uGLuIu4zLjSSeTOsCcbKfxXsxy6Y12LH5JjSVHwV8p01N9E652giGHY4kaVZknPNv9tIF0y1fU2MhIwX8uI7Tukf74HzFWBrjYpNKniFc-rSeZODF3vSFUwT8sKz8WbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندن خدمت سربازی در تیم نظامی وجود نداره. علیرضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور فرصت داره راهی ملوان با فجر بشه چون پنجره بسته بشه دیگ نمیشه.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/138767" target="_blank">📅 14:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138766">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
❌
فووووووووری
🚨
محمد عمری به دلیل کشیدگی از ناحیه آرنج دیدار برابر تراکتور را از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138766" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138765">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/138765" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138764">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
🔻
🔻
میثاقی: احتمال داره حسین زاده و بیرانوند به همراه تیم ملی امید راهی بازیای ناگویا شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/138764" target="_blank">📅 13:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138763">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
بخش رسانه‌ای تیم ملی: مسدود شدن سایت و برنامه فوتبال 360 عادل فردوسی پور هیچ ارتباطی به سرمربی تیم ملی ندارد و ایشان نه شکایتی کرده نه هیچ عملی انجام داده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/138763" target="_blank">📅 12:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138762">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
قدوسی: علیرضا بیرانوند گفته نه تنها سربازی نمیرم بلکه نیم فصل با استقلال برای فصل آینده قرارداد میبندم
😀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138762" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138761">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu0fHOtR0LkM5gG7ZV_PZHeR4TgXRKEiwa_hcCT6z7CCNj9QVCdlAEfYsrmGUCn3lTTCflUqePee1KH4DsyRfT0L8OnTlNf-dz12D35iN-XO-9Q7DbwBYk1oLJW_bOIZX1hNrlAvO1bfjbdGbTa0KVjl0peY6ETFZbmoVZ9_0J9EacnbWD7KXQ9fEuOXxgrTISiKQ-j9MhJU66_URbVZJhYFpseAJkIrc1akwfmHAwN1k4814oJ8NJtMfYgyNILWPDpleU8at7BzMzPEL2Jkvyw8KQv6ZFh7hBY7LEB5a92rQXEAM2mN68r7mdw_jWYO4yPPUb5eSsA400W00elV_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نبرد غول‌ها برای اولین جام فصل!
دورتموند در خانه مقابل بایرن؛
- امشب کدام تیم جام را بالای سر می‌برد؟
وقتشه پیش‌بینی‌تو ثبت کنی!
⚽️
فینال سوپرکاپ آلمان
[
دورتموند
⚽️
🆚
⚽️
بایرن‌مونیخ
]
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🌐
نسخه جدید سایت:
Sportn5b2.com
🌐
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/138761" target="_blank">📅 12:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138760">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=RpsqEnZziy7ENehipevR6RsSZZOG4izSkkBOhRMJrxaGXzxTeXHkp8kYUYbmyT992bcs7w_3skwQ99s356cyn4xLb7WAtGGhrF2u7ELuOjsjaMQ4gfsPwHsa7l5SGZ42GaDhh-Rh1YLkQiNka27fx-xSeMcvQsMsoctOz_yNQVHXqacug-VAgPeXFo7pGKJ-bT23JdTnRNm7BX4zZzJvlA6Z9irPPuOnySl3N_oqE6ALujSbKV5xawySI14TWF0AYjETtfigdDAQw7QCJZDuI2mb7AzrhsHcXWUxU2mAqRqBvPWL-lFs7thgdSfl7o1HckawcE1e5Jr-gjkmYUzc1BPXAVFDEgq54VoJJvQGXqFc2MPRFqC3S5FaEraQl9xSzvpENlUhfiGvdFysmTI9ix3qpSKQ-KxLtK8bctH75qYrewmv7Xzj0A90cUFK3DKa5qizYTi8Mr1eUxziGo-VryeKfmX73-d4ehTEV22P16uOliEhgIA7KgTqv6KHok5jiJtPgp7yCZ7nywuA57NwqsA406ESAk-TKu0FBswFygmX_6SfAj8YkZQTGRUcnfXy60k-YSQ6UUgXtMym_nSyoc5YKjxRWJITUv19z2si1_H6_BZ1A8Rak0QCeOJpEc1Tr4-GyFXQZs5pWW01-l95zDl0zP_rtuJxgUPJOfKYF28" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e244643a2.mp4?token=RpsqEnZziy7ENehipevR6RsSZZOG4izSkkBOhRMJrxaGXzxTeXHkp8kYUYbmyT992bcs7w_3skwQ99s356cyn4xLb7WAtGGhrF2u7ELuOjsjaMQ4gfsPwHsa7l5SGZ42GaDhh-Rh1YLkQiNka27fx-xSeMcvQsMsoctOz_yNQVHXqacug-VAgPeXFo7pGKJ-bT23JdTnRNm7BX4zZzJvlA6Z9irPPuOnySl3N_oqE6ALujSbKV5xawySI14TWF0AYjETtfigdDAQw7QCJZDuI2mb7AzrhsHcXWUxU2mAqRqBvPWL-lFs7thgdSfl7o1HckawcE1e5Jr-gjkmYUzc1BPXAVFDEgq54VoJJvQGXqFc2MPRFqC3S5FaEraQl9xSzvpENlUhfiGvdFysmTI9ix3qpSKQ-KxLtK8bctH75qYrewmv7Xzj0A90cUFK3DKa5qizYTi8Mr1eUxziGo-VryeKfmX73-d4ehTEV22P16uOliEhgIA7KgTqv6KHok5jiJtPgp7yCZ7nywuA57NwqsA406ESAk-TKu0FBswFygmX_6SfAj8YkZQTGRUcnfXy60k-YSQ6UUgXtMym_nSyoc5YKjxRWJITUv19z2si1_H6_BZ1A8Rak0QCeOJpEc1Tr4-GyFXQZs5pWW01-l95zDl0zP_rtuJxgUPJOfKYF28" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
حضور پرسپولیس در مرکز پزشکی و فیزیوتراپی فدراسیون کشتی
✔️
بازیکنان تیم فوتبال پرسپولیس پس از دیدار برابر استقلال خوزستان، با حضور در مرکز پزشکی ورزشی و فیزیوتراپی کمپ تیم‌های ملی کشتی، به ریکاوری پرداختند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/SorkhTimes/138760" target="_blank">📅 11:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138759">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
در صورتی که انتقال ابوالفضل رزاق پور به پرسپولیس کنسل بشه، امیر جعفری گزینه بعدی دفاع چپ خواهد بود / تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/138759" target="_blank">📅 11:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138758">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">💢
💢
🚨
مدیران باشگاه الوحده امارات پس از شکست در دیدار امروزشان به دنبال جذب دو بازیکن خارجی جدید هستند و از همین روز از نماینده محمد قربانی دعوت کرده اند فردا برای جدایی و فروش این بازیکن به باشگاه برود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/138758" target="_blank">📅 11:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138757">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
❌
آب پاکی فدراسیون فوتبال روی دست تراکتور، پرسپولیس- تراکتور، بدون تماشاگر
✅
✅
عضو کمیته استیناف فدراسیون فوتبال: کمیته استیناف به‌عنوان مرجع نهایی صدور رأی در ارکان قضایی فدراسیون، حکم کمیته انضباطی مبنی بر برگزاری دیدار تراکتور و پرسپولیس بدون حضور هواداران…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/138757" target="_blank">📅 11:03 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138756">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
شایعات : تارتار میخواد مقابل تراکتور یه ترکیب سر و پا هجومی بفرسته تو زمین  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/138756" target="_blank">📅 09:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138755">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
حسن اکرمی داور بازی پرسپولیس و استقلال خوزستان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138755" target="_blank">📅 09:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138754">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0Zre_gpwuEhWaUmglSgjMcXGtRE-gm8VdD62z33AEWu2mX4gWUd0JdgmAwWxhoQLbQBZK7TO_yr7jCgiyKApU_rYrJzusHGonCOD6QtmMB2_BUZus9Xv0sYp4If-CMqtdLp6HKRPchARj6xYtt46-tl3-ObYJD5wHfAXDbT75fr7dXw3h0udAMn_iNZqOTdJDv1J681BsbM2c5Cn2ufqe2oeskZxG9qrEo8W5CeRreRTKk1rVTEbYmOW9tH65VXSG9XtEVIU5M0JeWcqbYOxpJtGokLPeQsxcjbb2CeobhBEJMSFiR4DFbqxzuA2mRJubtPHqDlBLPChFKuUZnejQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
صبح بخیر ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/138754" target="_blank">📅 09:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138753">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">7️⃣
وقت چرخشه! | SCARABTEMPLE
🎰
همین حالا با هر بار شارژ حداقل
۱ میلیون تومان، اسپین رایگان متناسب با مبلغ شارژ
دریافت کن!
💰
شارژ بیشتر؟ اسپین بیشتر!
🎁
هر چرخش، شانس دریافت جوایز نقدی
⚡️
اسپین‌های بیشتر، فرصت‌های بیشتر برای کشف جوایز بازی
😳
👾
اسکرب‌تمپل
، با یک سیستم اسپین پرهیجان و جوایز متنوع:
👇
🔵
نسخه جدید سایت:
Sportn5b2.com
🔵
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/138753" target="_blank">📅 01:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138752">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❤️
❤️
❤️
سهیمه خرید لیگ برتری پرسپولیس در نقل و انتقالات
⏺
1_مهدی تیکدری نژاد
⏺
2_سید مجید عیدی
⏺
3_محمد مهدی زارع
⏺
4_سید ابوالفضل جلالی
⏺
5_پویا پورعلی
⏺
6_محمد مهدی محبی
⏺
7_دانیال ایری
⏺
8_ خالی...
🌏
سهیمه بازیکنان آزاد فیفا:
⏺
1_خالی…
⏺
2_خالی…
⏺
3_خالی……</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/138752" target="_blank">📅 00:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138751">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
‼️
فووووووووووووری
🚨
ورزش سه: سردار زاهدی بار دیگر در ارتباط با ما اعلام کرد علیرضا بیرانوند سرباز شده و از مهر ماه ( یکماه دیگر ) باید به خدمت مقدس سربازی اعزام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/SorkhTimes/138751" target="_blank">📅 00:39 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
