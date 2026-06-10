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
<img src="https://cdn4.telesco.pe/file/Jo8ADfoEWCSBUh0dkaaPbIFUwHpQr4MD-hKdOMfm3gAptnJRo8p9Dv_uHyLlnQXKhHym02VWkCXl9OSLgT3t9e1S6SHzAMZsIyFAuq5bd8zjjrDm9VvjKOH3O5N85tLzEtTb_gCCiHXz0W3aMSSU82YB_dYeb_6NC9E2FTQUkNg8B7MdW-XWGQB7bwdW323qQUGKOu2UsmANNrPnOvvtqMfgja8iiWkIqfDJiONizzjDu7OnoHBFkbqAE-W7tCBrW8Nt8emvyRRIgCsjJMjzF0i4Rkpb6ADHqEjK3tKPVM2qqiHTtH6EA5n8d7C_2JtN4RvgyMVc2SkqTPo-7nszWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 دانیال طاهری فر | آموزش سئو و دیجیتال مارکتینگ</h1>
<p>@danialtaherifar • 👥 1.55K عضو</p>
<a href="https://t.me/danialtaherifar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 آموزش سئو + دیجیتال مارکتینگارتباط با من :@danial_taherifarسایتdanialtaherifar.irکانال یوتیوب :www.youtube.com/c/DanialTVخرید اکانت و بک لینک :https://danialtaherifar.ir/shop/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 254 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 297 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-934">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=UC8bY5GrT9Mvs3vPxklC2DiXviEtAsGTFM50kqzyFaaCuvpL5fpvA7pb1lbJPX8A75_VqzERfhxcYPCcLbArrSSmsygdZb59OkCCi8b_2qbMXmJkGKC48jV-l9_vi3GemV5lOpUmBlrgGxMHh1obhB1V0xkMbmij67nKQpOB-i6fDjOVGE26jiyzHa-C0rQeX-DqabB0IB_AycRDcY0048tQ1OPXolOsyl1kmzOvwkWiy6O45iQJEcpnMe5KCCxQmCSSEQw8ZzlOEIvBrH62OyAQyiZpBsHYemZc-lvt83LcaJeX5lRhHta_FTs_KCdQNbO8Li9jMQV67NiQNnYUsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27ed35fe78.mp4?token=UC8bY5GrT9Mvs3vPxklC2DiXviEtAsGTFM50kqzyFaaCuvpL5fpvA7pb1lbJPX8A75_VqzERfhxcYPCcLbArrSSmsygdZb59OkCCi8b_2qbMXmJkGKC48jV-l9_vi3GemV5lOpUmBlrgGxMHh1obhB1V0xkMbmij67nKQpOB-i6fDjOVGE26jiyzHa-C0rQeX-DqabB0IB_AycRDcY0048tQ1OPXolOsyl1kmzOvwkWiy6O45iQJEcpnMe5KCCxQmCSSEQw8ZzlOEIvBrH62OyAQyiZpBsHYemZc-lvt83LcaJeX5lRhHta_FTs_KCdQNbO8Li9jMQV67NiQNnYUsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گوگل از قابلیت جدید «Search Profiles» برای ناشران و تولیدکنندگان محتوا رونمایی کرد
🔍
گوگل قابلیت جدیدی با نام
Search Profiles
را معرفی کرده است؛ ویژگی‌ای که به ناشران، رسانه‌ها و تولیدکنندگان محتوا اجازه می‌دهد حضور خود را در نتایج جستجوی گوگل بهتر مدیریت کرده و محتوای خود را در یک صفحه اختصاصی به نمایش بگذارند.
📌
این پروفایل‌ها به‌عنوان یک هاب مرکزی عمل می‌کنند و آخرین مقالات، ویدئوها، پست‌های شبکه‌های اجتماعی و لینک‌های مهم یک ناشر یا کریتور را در یک مکان جمع‌آوری می‌کنند. کاربران نیز می‌توانند از طریق دکمه
Follow on Google
آن‌ها را دنبال کنند و محتوای بیشتری از آن‌ها را در بخش
Google Discover
مشاهده کنند.
👥
در فاز نخست، این قابلیت برای ناشران و تولیدکنندگانی فعال می‌شود که در حداقل یکی از شبکه‌های اجتماعی اصلی دنبال‌کنندگان قابل‌توجهی داشته باشند. طبق اطلاعات منتشرشده، حداقل شرایط شامل 100 هزار دنبال‌کننده در YouTube، Instagram یا X یا 300 هزار دنبال‌کننده در  TikTok است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 358 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-933">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2PqOn8jpXhdh3-wBzemlZrqIDcIvYX8gwggOaODVR4fMcPvbj81tZHQuRdbg_ACr-1aBeJKmLqdrh24V7_1hjLinDyMUSbdzZ3juJLSt-wriXbbYUYO3jLKrQmArqNyRcY8HXT8NoK0jHMdwg0tSsB9ALbR_yhbPamYEDUEjcFwXEjNyy-Bo00o6dhhfmu86NwafJ1HuzUTfrDAWVnjVKHe3r_b3eOvK-Rd5XBaFuWSG-2_kOzleH7qj7KU1gJd4pZxrw3fPnLp7XGVOevzC9uTqaa4aNY3MT_0J8uIV_9z7DvXF5btNk_82dSlZCPo9P5ZFZ_A1axYJw_HIbwTxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل گزارش عملکرد AI را به سرچ کنسول اضافه کرد!
گوگل رسماً از قابلیت جدیدی در Google Search Console رونمایی کرده که به مدیران سایت‌ها و متخصصان سئو اجازه می‌دهد عملکرد محتوای خود را در نتایج مبتنی بر هوش مصنوعی گوگل بررسی کنند.
📊
این گزارش جدید اطلاعات زیر را نمایش می‌دهد:
✅
تعداد Impression صفحات در AI Overviews
✅
میزان نمایش صفحات در AI Mode
✅
حضور محتوا در قابلیت‌های هوش مصنوعی Google Discover
✅
صفحاتی که در پاسخ‌های هوش مصنوعی گوگل نمایش داده شده‌اند
✅
آمار تفکیک‌شده بر اساس کشور
✅
آمار تفکیک‌شده بر اساس دستگاه (موبایل، دسکتاپ و تبلت)
✅
داده‌های ساعتی، روزانه، هفتگی و ماهانه
🔍
نکته مهم:
این داده‌ها علاوه بر گزارش اختصاصی AI، همچنان در گزارش کلی Performance سرچ کنسول نیز لحاظ خواهند شد تا تصویر کامل‌تری از وضعیت سایت ارائه شود.
⚠️
فعلاً این قابلیت فقط برای گروه محدودی از وب‌سایت‌ها فعال شده و گوگل قصد دارد پس از دریافت بازخورد و انجام تست‌های بیشتر، آن را به‌صورت گسترده منتشر کند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 491 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 613 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 725 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 823 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMqvcXr1y6NaJ2PuJIkZ0Rryj2EA0ik0CwvlQINTTPIUr4H4utp9vMZbcLf1z-FaFu8udpc3V_6aLCyyn06BnyHHF8uzZmUBqDjQ2_g5PLALdXrJVzoU8-QA_ruirIhhZvAKD57GmOdmIvpPwaLr3MsRxNjka5SUpdak5ZK8Un1MOKol6Rn8-dJFca5SoooWZ9g2BI7MHAaL9SRkl1zWgi9omocxGLOgBEGp-6E7P6qMGfep9EQUiIfdYm9xiDd27EpGDjhFKjFnRSKUxy6237xkRzarbtmtp1D8lbMpHwCf8oM5EtGb9K3vJ5Xs78rxX8Gt5qMnjtbz_0p3s8Gf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 857 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_ER2ZT8WV6tcGFcuZR6KDGF-PR-IXrz9C0N7nCG91HfHTT_BDpiBYj4g2S7dEhh4jY1dbm5p1DkSm6j28TzrksjafWTEwU2J0k9S9nf4l9t4dR0CaMWyhTrlDLxKgvcrPkydUTyir2yuDKcAKX--7ohfGr0LSMCESCxecmVork5bflO6H2otzVENMEC826_pr47liCHjgqzDWTadSlU6W2aFqLS1hb0ZLfSP__PXdTQ6Ncd14T_Qlr9-KyQIb-by9mXEgSyyf-1fK8G-X4_oPMZXcY5Q9tXVCIPBruErOE-I3K9iU9fDEMGYFJexQqg65pS-9eyyRBWJo_RpxshxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-926">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">درسته که سرچ گوگل باز شده، اما هنوز سایت‌های ایرانی رو نمیبینه و عملاً همچنان از اینترنت حذفیم!
😞
🚫
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/926" target="_blank">📅 18:34 · 27 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-925">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/syPBXAWR9fwS-FeIaiy_UAa3FoI8mgeu4ffOhAr7Qemng2egYYqzn1qYRxKeLvFGwy9uqMG9E6oLXPy0a77fhU5F0ZhdB4j2RgxiWtlGNNojKuDqi80fCoEc2CCAc6oqFh_8i2wfwy04_SAcyjgtK9KFDbE2XEg20Qb66y62vwOd751RXN3ifHPFjk2i6x2RLndJDmL56tx8kBKLQjGEaWr8aNLywfLyoAkUHb49det9iUQoqWZ40jvGzesTlqsNpKkz-dKFY1PTInbKME1oIcL2GYz9TtrZMqxKLml9BkFNbyxuOjI1P7gU-FyTWgmLM9D86je-oVeOS4qa9GvadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
ظاهرا دسترسی به یک سری دیتاسنترهای بین المللی برقرار شده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-924">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQwusuJPQ8bXQyi9bsG6oo86k_692V85aq_obFBf-88zgP_gLqDjPuP-2UpHyTjZI1Pqshgg3R0yWhVwrxqY5o0RrwDKWJV__PMOhX95K5KO7tPDydQ1Lj_ZIx3afpdRlfl-wbdDl0AdRjP74RT5J9DrrGhFiV1PJCCOa-JdFv7yv7jkvVBqnioRdwcXua3kMDJCVBdKOpVRgqc2sKgjmOTX4bmyZvG80WD0OJE0W5upbZwPPjCPtecMy-eBU5iC58jRjSkEQxPEwDrk9bGRHPQ517imRcwJHtIs6PF0eto6MCE1uMfukcuaZ2SwAWVL_s5fT_GyrbVTQvitIJp8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبدیل ضربان قلب کسب‌وکارهای اینترنتی به یک «خط صاف» صفر...
💔
ما کسانی هستیم که زندگی‌مان، تخصص‌مان و آرزوهایمان به این «ریسمان نازک» وصل بود.
این فقط یک نمودار نیست ... این، فریاد خاموشِ میلیاردها تومان سرمایه، هزاران ساعت کار و تلاش و امیدِ صدها نفری است که در این مدت، نابود شده‌اند.
ما یاد گرفته بودیم با الگوریتم‌های گوگل بجنگیم، با رقبا رقابت کنیم، با «محدودیت‌های فنی» دست‌وپنجه نرم کنیم؛ اما هیچ‌وقت یاد نگرفتیم چطور با «قطع شدن» نفس بکشیم.
بیش از یک ماه گذشت...
یک ماه از روزی که «دسترسی آزاد» به اینترنت، تبدیل به یک «رویای شیرین» شد.
آقایان مسئول! این اینترنت، برای ما «تفریح» نیست؛ «نفس» است. برای کسب و کارها، برای فروشگاه‌ها، برای خدماتی‌ها... برای همه ما.
#قطع_اینترنت
#سئو
#دیجیتال_مارکتینگ
#سرچ_کنسول
#کسب_و_کار_اینترنتی
#ایران
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/danialtaherifar/924" target="_blank">📅 13:42 · 11 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-923">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5bCv8M-f1reZC8d9NvUC9QFXpb1IzLWcH6p4Fbl8X1I5PZ00Xv_mVfZxEv1gCEHoPMe5a24l0FWNyImITm6WD0Bcc0J_Y0xSRhyxzAU0UQ-7crfdpqFtJ00pU7MoAogc4iz6MBxPrs29YVsDTEa7tWuceg5q8tkJxcGNE6YJK8e_268Kn4jmKbk8z4PVZZ1MOG-EDctfYwO4P9B-OyYmE0287cThz4nKubz9b_epeDENxk97JG3VfRg0ynRVT1Q2zHKKaKL_Tcc2GUCJ0wPkNHrpNsJB43p_c4UcpsQiglU9G1BlWGiUN4TLN_GO-ZwDLK6M-uYzfLjzVizKF20Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.
بختت ایرانی...
@danialtaherifar</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 967 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-921">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درود عزیزان
نوروز رو به همتون شادباش میگم
❤️
امیدوارم که سال بسیار خوبی در انتظارمون‌ باشه و بعد از سال سختی که گذروندیم، کسب‌وکار دیجیتال حسابی رونق بگیره و یواش‌یواش درهای بین‌المللی به روی کسب‌وکارهای ایرانی باز بشه. سالی که در پیش داریم،میتونه فرصتی باشه برای جبران، برای یادگیری بیشتر و برای رسیدن به اهدافی که شاید سال پیش دور از دسترس به نظر می‌رسیدند.
سال نو مبارک و ایامتون به کام.
با آرزوی بهترین‌ها، دانیال طاهری‌فر
@danialtaherifar</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-919">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!
مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/919" target="_blank">📅 12:47 · 15 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-918">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGNd1ORBHTRxdqX1gSjY5goIyRbgsnqbT1piA7qqO6WsvdawHtP7tIeMu54yi4tk8MaefH7aYY3YUS6vItZufL0Sowe3amdQyu1DwJ8Bfd0aM_GRLisC21j5NyIf-Ge4wRYvlrh5QpiLqZsTQmxoXbL3zSXcG0enZUJa2tmj-lEMli98VRxGjhY1lPFLDEpS2-ck6s1U3D03M1zlFjyyz8W62-mmWX2Nj3RlbyBsuxU3RqVwWG45-ufCmihGMhvTNdb4ODXdGKBaV7spuWAfb3T1E2qJ953wRsOdV18yFetSXZXJFSwnf-_OJy5k0U1jo1ov5DPQIVkOhTX_vRTdvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اینم کسب و کاره ما داریم؟
با هر ماجرایی باید صفر بشیم! باید کلی استرس بکشیم.
امیدوارم این آخرین قطعی اینترنتی باشه که تجربه می کنیم
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/danialtaherifar/918" target="_blank">📅 00:47 · 14 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-916">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C3yOguqT5dOyq-nVInWCLBnhPfUGbWfaxauJ6n17VvzaFIBdw86F4AB6jk5mHXkU9YKgkQB_spH-FTUrbEWzdhgEd3wnLyp48vkJIPByE1Tz5hNgaeNMG76Glc4qivHPgC_ZQ2OyL497N8IN6ijT_XMx1uKTaXIIVV3S-7bb5Gxy_Vcy-UXeJkge0AnB0PO0VNTKJ-dWWnQTfn9T6WGIujrrRyuzQlRO-rGw9-UzdXp_CIH6Oz5b8qEqb4sXcnyWYjqU5ZKHE0tPdyBZj9OYIGRxehjE23-CgoGkySspPHI0zpLwMsI7gaQyydrtwtVNYc8nO5-oiCBf7Rdlm7mhJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIYtcp0rbsoCRAlr8tz8p-CCanLp7v4PT5u-J4p9p6BQFuiuImjGHCFrsMkY8RP_l00wfeLfjTI78ZOF8s1c5zySVl1anUuCjUugAkmHOzfvvxB7700RRxjh93USYqSFjpFgLQkoTk_n67QGE-pHcJRtBERkJxTuzXPvGEpOW_S3FeQr_Fo7BbWTeVdiPaK_GACVkW3AVfG66-72vkQaTf3r3qicRtxIQoUSavVy3BqfPAzzk7evpHwtFkh6F7GzaKYyCLMgDy76D5Q6C1xvlM_qE1No_1HYhyBEUA8_77pYUKszw--weNxMi14FHT3Q4fPBknCaaO-ezxvRF8kFNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/danialtaherifar/916" target="_blank">📅 13:01 · 10 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-915">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3KqKlMJ_bTW_2RCo2sJUoy_Fjmc_Q2yLep6LCmS81bLIrTlfa5gw512yNY4auWHsT1GAubRPuZa3PdF5xiJF_px_y41tZK9475kxWsYydDYv1ml_w1Q7-2s5dcIF9Cq86X7Oq1-KkdUFZhrV8SfYl_Kp5I-jjVGqB_C1qz-YRa7l-CnSleDn8uHOx--ksfzDKRrYHbqQRpfFFtIIPRZAdScLvvrBNua6XMtyzX31OSokpFdtF768mHb4bu21asSLTvIsPSIuILRCCzAXFumVL9CSEKNZvdpCgX54wG_26RlguyT00P4MhxY8yIjGBaVpR-_9JShCrBjSENa7CpdJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
دسترسی گوگل به هاست ایران باز شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/915" target="_blank">📅 13:21 · 08 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-914">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
❗️
بعضی از هاستینگ‌ها از شرایط به وجود اومده نهایت سوء استفاده رو بردن...
از هزینه های 40-50 میلیونی بابت ارائه خدمات ویژه، تا مجبور کردن مشتری به خرید سرور اختصاصی برای سایتی که ۲۰۰ آیپی روزانه ورودی داشته ...
منهای این الان شروع به تبلیغ پیامکی کردن یه عده برای این موضوع، بعد سایت خودشون فقط یا از ایران باز میشه یا از خارج !
در کل مراقب باشید ازتون سوء استفاده نشه، وقتی که عصبی و تحت فشار هستید راحت ‌تر کلاه سرتون میره
@danialtaherifar</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/danialtaherifar/914" target="_blank">📅 21:08 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-913">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :  استفاده همزمان از  دو هاست ایران و خارج برای یک سایت   @poinair پوینا</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/913" target="_blank">📅 20:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-912">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمتخصص وردپرس | پوینا</strong></div>
<div class="tg-text">حل مشکل سئو هاستای ایرانی :
استفاده همزمان از  دو هاست ایران و خارج برای یک سایت
@poinair
پوینا</div>
<div class="tg-footer">👁️ 666 · <a href="https://t.me/danialtaherifar/912" target="_blank">📅 20:37 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-911">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🛑
از دقایقی پیش دسترسی نت همراه به سایت‌های میزبانی شده در خارج کشور(آلمان) باز شده.
اما همچنان بات گوگل به سایت های داخلی دسترسی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 883 · <a href="https://t.me/danialtaherifar/911" target="_blank">📅 10:28 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-910">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAPf4qwLXeUsafByJQkGPjJ7c304mfUNUJj4q4OL2S3_Qk0k5fR2IppLmtIXomnlpHw__lXFqyRvqLTM84hIZLxbulKBkdQdJ3gN2_N_qJP7cT5pWH6mlGHJ8UWDRTKo4JZHS-ojbCTJfLoeQox7waudoLBS4w26CdNaSnNwAXzSc8rlG80ZQvF4-f_9TvbKrsuicIhj3RNaJUJOOqoJBDMq9A4xRZ5Tm7KSgvIYRE5RWAVRO3pDStfAhcpSXU3dcYDBp96MNUueYjwo_3lYYb96jygvFNqaZ2Xm2C4R-gAotOTi78I3ga9Pb9NnGmFbv_SecptOk7Q6XqZwmyXpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه سرچ کنسول سایت های میزبانی شده در ایران و خارج از ایران:  نکته جالبی که تو این تغییرات به چشمم اومد این بود که سایت هایی که رتبه‌های عالی داشتن بیشتر آسیب دیدن و سایت های رده سوم در سرور ایران هم موقتا رشد گرفتن و بالا اومدن، که البته با توجه به قطعی…</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/danialtaherifar/910" target="_blank">📅 00:38 · 07 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-909">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🟢
راهکارهای رفع مشکل سایت‌هایی که داخل ایران میزبانی می‌شدند و از نتایج گوگل حذف شده‌اند
برای این موضوع چند راه‌حل وجود دارد، اما رایج‌ترین و عملی‌ترین آن‌ها عبارت‌اند از:
1️⃣
راهکار سازمانی (Enterprise)
استفاده از CDNهای Whitelist‌شده که معمولاً فقط به اشخاص حقوقی و شرکت‌ها ارائه می‌شوند.
2️⃣
ایجاد Mirror از سایت
ساخت یک کپی کامل از وب‌سایت روی هاست خارج از ایران، به‌منظور دسترسی بدون محدودیت گوگل.
در این روش DNS به‌صورت هوشمند تنظیم می‌شود
ترافیک داخل و خارج کشور از هم تفکیک می‌گردد
⚠️
به‌دلیل اختلال در ارتباط مستقیم بین سرورهای داخل و خارج، معمولاً امکان سینک دائمی وجود ندارد یا این کار از نظر فنی زمان‌بر و پرهزینه است.
برای اجرای این روش، با پشتیبانی هاستینگ خود تماس بگیرید و درخواست سرویس GeoDNS بدهید.
3️⃣
(در صورت دریافت مجوز از سرویس‌دهنده، اعلام خواهد شد)
❌
نکته مهم:
در حال حاضر برخی سرویس‌دهنده‌ها در حال بازگشت به دسترس هستند؛ بنابراین پیشنهاد می‌شود از انجام تصمیم‌های عجولانه خودداری کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 815 · <a href="https://t.me/danialtaherifar/909" target="_blank">📅 17:04 · 06 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-908">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
❕
رئیس اتاق ایران و چین: تجار می‌توانند روزانه ۲۰ دقیقه با حضور ناظر از اینترنت استفاده کنند.
مضحک‌ترین خبری که این چند روز دیدم.</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/danialtaherifar/908" target="_blank">📅 14:56 · 05 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
رفع مشکل کندی پنل وردپرس در زمان قطعی اینترنت
اگر از سیستم مدیریت محتوای وردپرس در وبسایتتون استفاده می کنید، در شرایط قطع اینترنت به دلیل داشتن درخواست‌هایی به سایت های خارجی احتمالا کندی پنل به صورت بسیار اعصاب خورد کن رو تجربه می کنید.
دو تا راه حل واسه این موضوع هست:
۱- مسدود کردن ریکوئست های خارجی در مرورگر با زدن کلید f12، رفرش کردن صفحه، انتخاب درخواست های خاجی(از جمله فونت های گوگل و yoast و ...)، راست کلیک کنید و زدن گزینه block request  (محیط dev tools باید باز بمونه)‌
۲- از طریق فایل wp-config.php کافیه که کد زیر رو در کانفیگ قرار بدین تا تمام درخواست های خروجی رو متوقف کنید:
define('WP_HTTP_BLOCK_EXTERNAL', true);
و اگر دامنه بخصوصی رو نیاز دارید که در ایران میزبانی میشه و در دسترس هست، دامنه را در کد زیر جایگزین کنید و بعد از خط بالا قرار بدین:
define('WP_ACCESSIBLE_HOSTS', 'torob.com,*.danialtaherifar.ir');
با آرزوی موفقیت
❤️
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/danialtaherifar/906" target="_blank">📅 14:51 · 02 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmzPz244zhzV1CpcugPus7ormD-FE7uBS-__sIqKZBhJwu9xwDBJDXn6HQYrPvZRbSSZwgtPbcdVNKsdjQ3FiHyS0OPs8Dl-TNDlyhgMxgke6bT_fQyaOvUia_kDLKgk_Vs2sZe3hgmLBJlSTz-HAcXcxT3_zwlFkJzLMpSWEPjvYOeC34s2D8eXVnTCd8HW80GkROVODxLPGM4_7LjynWa5Gq1xB1zClECkE7VJ2j8_DXUcWsPNBDLL_R2hoCzCKlVrg19Gh60PAVVngxgGQaUQcoiJxJydJ5EIcNSheUywBjEyfbgvokF6VWz6hJV-uSOf-ZFIsmGtO5CGLxZOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل)…</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/danialtaherifar/905" target="_blank">📅 15:46 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">متاسفانه اکثر سایت هایی که در ایران میزبانی میشدن ایندکسشون به صفر و نزدیک صفر رسیده ...
💔
اینکه بعد از اتصال اینترنت چه رفتاری با سایت ها میشه دقیقا مشخص نیست، اما به دلیل اتصال یک‌طرفه‌ی گوگل(و در دسترس قرار نگرفتن سایت های میزبانی شده در ایران برای گوگل) سایت های رقیبی که خارج از ایران میزبانی میشدند در دسترس‌تر قرار گرفتن، حداقل به یوزری که خارج از ایران بوده پاسخ میداده و هیستوری میساخته...
فکر می کنم بعد از اتصال مجدد برای پس گرفتن جایگاه‌های قبلی باید بجنگیم و تلاش کنیم و احتمالا فورا به رتبه های قبلی برنگردیم.
در کل باید صبر کنیم و ببینیم چی میشه، خیلی دقیق نمیشه چیزی گفت چه اتفاقی میافته و فعلا راه حلی برای این موضوع پیدا نکردیم و از ارتباط با دیتاسنترها هم به نتیجه خاصی نرسیدیم.
ضمنا به دلیل همه‌ی این محدودیت ها تغییر Dns دامنه های ir  هم میتونه چالش های بدتری ایجاد کنه، پیشنهاد میدم کار عجولانه‌ای نکنید.(ممکنه کلا سایت هم برای داخل و برای خارج غیرقابل دسترس بشه)
به امید روزهای خوب
🌺
@danialtaherifar</div>
<div class="tg-footer">👁️ 679 · <a href="https://t.me/danialtaherifar/904" target="_blank">📅 15:27 · 01 Bahman 1404</a></div>
</div>

<div class="tg-post" id="msg-903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX9BPAGdYKX_tJK_Q2u666rItD74lAf403BOm5550INPzem0jrPn5YqzMtsxU1eFr_fKwy-LOZ9bkxoRGYMrE7Zhqwr0jGg24GAHO040jXiLrmQK7IzRsX-8iTVoZnG3ojB3gbfwJnHfWxbrKU-S1ZXKwmYBReBMRXSwdP6oyoh8A0c7FDQBb4H2hrKVYyAPAI8FoXnE3KIdbv2vfnPCcdYZvuPuyQvVyYyDyZ1RP3z4Qvg7aS0lvb3FtJxqaKitZhYX6aJNEo2jZc_nPPP9UNsaxLCl8dpyBilD4oaO3PMbL54hqHre9IK_IOLcaQHcrGsywTjvpcwrsPC6MyJVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایم‌فریم‌های هفتگی و ماهانه به سرچ کنسول اضافه شد.
از این به بعد می‌تونید روندهای بلندمدت رو راحت‌تر ببینید و تحلیل تکنیکال بلندمدت روی نمودارهای سرچ کنسول انجام بدید.
😄
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/903" target="_blank">📅 07:40 · 19 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-899">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwyP4l55Ya7Dk_S_p4z0bzZSIYI3iT6eeeC5PIlLIOls_6AlO7FiOlnnlicpcoMLjM-25G0-oM424IYlsSV0bnZBkn3gNjfgkjkgRPTMgFLdK7sMRFSS3HCCfO9zvMw3EaV4FEuVrI88ZqGZjX5YHTl1HuSOUIPEXkN0A0vlibEU-kcm_-ssHRRCUR6GSY8mqEeV79Rg8fyaJds0HP4rcWX3Tbv7yT9ujmQeoUPl4Y3HorAGFuIzS1axsm_GX7UTEuXib3DrngohYfSqtL_GXWOxxlCixRNoQ2dN9-kWzFv_R1OzXK5_mcyWM_5VlowPNIjSa2buG24_EpvAxiXWKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMoOBzO8V8sSRRMUeA8sr9DPUycvcjiPQtTlBD-8sI6zEfVAYPVwiVkC2a6Ue5w2NJMdXWLh51K34l-UnWHQbIAgwhMxDbBnhXEVxVbNw5wQc-pCyjQs_omAJfJnlbP5YPMdD_urQmsVlWr0CesD2OXOkIX-xuo_6CaKOnp3x1dSpyL0LetzXng_PrW2uwzp3L5TZp1wqRMF9vtFkTStN3NIY0ApSpH9933ItXHg0XNeJOPDEYu7I0m7ir-MH3uh65JVjSnLmcHRtNxvLRRwHCh-xa3uW_26ReWo75hLv7Wl57dwMRa71MWNVD-U_5x_rT14JOoh-61rwFAtpy47Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjarKx0WtKQZ3RYaAQtZNVovECVOrH8_iYNoSvP16_nmSo0nyQmeHT2pEDvzrS91SVL46oZvDSlhwr7li_N795NZCBed8QAkUO4tNheGkfzZO-iLebwIOpV4CpC6lnwt0wWkcv4-AnTUHLpfDFm6xbnDnXiEcLmK-w19xkDloqXUlRoGJOMrdLUcIrVe6sYKJUSRRnBkZF9YVWIHECc1bUUmOBDf8upkQDMwT1sZwLDX8-uYpJoc4yazjLvOPy472KqqnplC7-f5efAr4S4NG5LdJ2tczt9TTFntzkG9VnScsJ-LvpBDnFfyJBZas5NRNsAI0U8LrLxg6mE5BFkM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LB6Juhf8MOS_pA-LOYr4XS5_ZjvVvsiN2J1Wc08fDNmvVruiBMJctV_a2CWf-gHvEWCRoD73ASA6cOg-txiO3Ahb-a8tuyCoB9qNN01H1zui3qFkp1BMpifYzhyxFCDQNsfxrGCO_3rlVV1_xHIsJTpy5dL1Yk_GbnSfpiIhU7zm4sv4r0b1DPvHrrcz5gf38KG-g9ILXldcTu5HVokEwxzAxsyJ43UAf8AHnUTFUN7R1DeSKa9r9XW8cMLkWxer9dpo6BaiTWMoiCS45giCPbHw8SIKB2peewtq3gVUkmAbqu2NNLZa3vfi59z8UuyOp_F8etj7J6qcAyRjhwLFxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن فیلتر «Branded Queries» به گزارش Performance سرچ کنسول
🔸
گوگل به ‌طور رسمی اعلام کرد که قابلیت جدیدی با نام فیلتر پرس ‌و جوهای برند (Brand vs. Non-brand Queries) به بخش Performance در Google Search Console اضافه شده است.
🔹
این ویژگی که توسط دنیل وایسبرگ (Daniel Waisberg)، از تیم Search Relations گوگل، در رویداد Search Central معرفی شد، اکنون در حال rollout تدریجی برای همه حساب ‌هاست و طی چند هفته آینده برای تمام کاربران در دسترس خواهد بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 973 · <a href="https://t.me/danialtaherifar/899" target="_blank">📅 12:21 · 16 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-898">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwLwmDDAFewQDMcjG1UgvKuhr3OxOL89uppQvWqDGy55PYLGXy5OrU80c6SK5Ft7iUfzlT1mIb9O5eMrUg_wVhjIa3nUFnY34iumiaKTqTD6c1CRdPL-y7H_RHKbPpt6sMoe9tAEtGuB4BJEmCh-ZV9GibWII_sa6UHDA7ruPn_5Jo-EP1REkyub6qDTLFvrk8BdP1ZnqmKLRw-IQPw37TIwyfgHFX_Kh5pHsElsEMqQAR4DdVARiq_nTUKhFQMTQ3JAxpNBBEUYNv5Wd5zKMNa9zZDAzQpWJSB1grshM0PUaEtHcBCPDMbZ27sTJRSOAZyzjRFbqMkVuuzFhPX33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قابلیت تولید اینفوگرافیک به Google NotebookLM اضافه شد
این تصویر حاصل پردازش سه ویدیوی یوتیوب انگلیسی‌زبان توسط سرویس
NotebookLM
است که آنها را به یک اینفوگرافیک آماده تبدیل کرده.
با اینکه ایرادهای جزئی در خروجی دیده می‌شود، اما در مجموع نتیجه کاملاً قابل قبول و کاربردی ارائه می‌دهد و می‌تواند برای تولید محتوای سریع بسیار مفید باشد.
#AI
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/898" target="_blank">📅 12:33 · 11 Azar 1404</a></div>
</div>

<div class="tg-post" id="msg-897">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=mJRyxVTCbkmd2WGsRKjGamYGY1kLa2F2dXFqcsVbbCZRXj5NKcBdWx3wiC3f6vKS-4D2O_aLsRXzF33lV1PDv01r_LigRLIkwzuf2jh02K5ZxfXnLB7XDfpUnAwGnEFCVx19zNngIFYK-1ftVlJLBAumU_9cYpRFuKWQZ7qWrI5Mh5T1vUOE89QJBifOa4Z2eZY3A_OvRrbbkt8YyfcOWlSVKh8AnMuGOC44AhKy_24yod-axlkvN_Z3_mZX5i6OBs8k6RlwDZdidIRkkgUG7uP-ieTNqXeRd5YgjvU5OJzGAv5ucWpE1XUKPNyYGtQ4cnUUwJSFtDgswjC3zdg0Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=mJRyxVTCbkmd2WGsRKjGamYGY1kLa2F2dXFqcsVbbCZRXj5NKcBdWx3wiC3f6vKS-4D2O_aLsRXzF33lV1PDv01r_LigRLIkwzuf2jh02K5ZxfXnLB7XDfpUnAwGnEFCVx19zNngIFYK-1ftVlJLBAumU_9cYpRFuKWQZ7qWrI5Mh5T1vUOE89QJBifOa4Z2eZY3A_OvRrbbkt8YyfcOWlSVKh8AnMuGOC44AhKy_24yod-axlkvN_Z3_mZX5i6OBs8k6RlwDZdidIRkkgUG7uP-ieTNqXeRd5YgjvU5OJzGAv5ucWpE1XUKPNyYGtQ4cnUUwJSFtDgswjC3zdg0Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
اضافه کردن Note به چارت سرچ کنسول گوگل
😉
در آپدیت جدید سرچ کنسول گوگل میتونید به راحتی در بازه های زمانی مختلف Note دلخواه خودتون رو اضافه کرده و ذخیره داشته باشید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/danialtaherifar/897" target="_blank">📅 17:00 · 26 Aban 1404</a></div>
</div>

<div class="tg-post" id="msg-896">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkX186eesjftxNvdVYAlSaU5RLUCbI1QHfZLTN1LxgeBV8rf6bhg1ES7r_VdXlI9F7AMxBJkQI1TpoehfllnPWNQKRs3Al0_twMNHKQET9wUCoA_RVcAWCX84ZEmrJsVTjliSEafYtQ9VHqsPiewjjOFCH12JqSqSaO96vRYJv4k85mWx_8FZ9qeUf3hMkmeZ4q3DrPdv-Twu9yYgE4Al9Wjs9FBW56SMJ10-2xbxsc9BWToqu0sdNHap22Z14_2nCW8axhUQQ6k9nz0hvqPxnjtCkqQoTuygMWn7kqYZShPl-JtUs_n104t4zLYmwyxNMlwP6_napm48Ap1s7Fopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
برای دیده شدن در AI Overviews چی کار کنیم ؟
برای حضور در پاسخ‌های خلاصه ‌شده هوشمند (AI Overviews) نیازی به AEO یا GEO نیست! فقط همون سئو کلاسیک کافیه.
📈
سئو معمولی = سئو AI
گوگل تأکید کرده که AI Overviews و حالت AI Mode هم با همان ساختار سئو سنتی کار می‌کنن
🧠
کیفیت محتوا مهمه، نه منبع
محتوای تولیدشده توسط هوش مصنوعی یا انسان، فرقی نداره؛ مهم اینه که «کیفی و قابل اعتماد» باشه
🔄
هوش مصنوعی در همه مراحل سئو دخیل شده
از کرال شدن با گوگل ‌بات تا رتبه‌دهی با RankBrain و MUM، AI به‌طور عمیق در فرایند نقش داره
✅
ویژگی‌های AI Overviews مخصوصه ولی پایه‌ها یکیه
فرآیندهایی مثل "query fan‑out" و "grounding" برای دقت پاسخ‌ها استفاده می‌شن، اما تم همه‌شون سئو سنتی هست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/danialtaherifar/896" target="_blank">📅 18:46 · 02 Mordad 1404</a></div>
</div>

<div class="tg-post" id="msg-895">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">😧
یک نکته مهم قبل از خرید بک لینک های سایدبار که باید بدونید
✌️
زمانی که بک لینک سایدبار در کل صفحات داخلی یک رسانه رو خریداری می‌کنید، اگر اون سایت فرضا 100 هزار صفحه ایندکس شده داشته باشه، بعد از حداقل 3 ماه با ابزار های مختلف مثل اچرفس و سمراش و ... متوجه میشید که احتمالا بین 20 تا 30 هزار بکلینک رو دریافت کردید (ممکنه این عدد کمتر یا بیشتر باشه)، حالا چرا بک لینک های کمتری رو دریافت کردیم در صورتی که اون سایت 100 هزار صفحه ایندکس شده داره ؟
به غیر از موارد تکنیکالی مثل نرخ کراول و ... ممکنه زمان ببره بک لینک ها در ابزار ها و سرچ کنسول ثبت بشه، متاسفانه برخی رسانه ها با روش های مختلف و به کمک
جاوااسکریپت
بک لینک شما رو فقط در یکسری صفحات سایت به
صورت رندوم
نمایش میدن !
برای مثال شما بک لینک
دانلود فیلم جدید
رو ماهانه از یک رسانه با قیمت 5 میلیون تومان خریداری کردید، برای تست وارد یکی از صفحات خبر میشید و میبینید بک لینک شما وجود داره، اما اگر
رندوم
وارد صفحات دیگه بشید، بک لینک شما دیگه نمایش داده نمیشه :)
رسانه ها برای اینکه تاثیر منفی کمتری با فروش بک لینک های سایدبار یا سایت‌واید روی سایت خودشون داشته باشند از این روش استفاده میکنند.
اسم رسانه خاصی رو نمیبرم، اما در خرید این مدل بک لینک ها حتما دقت کنید، بابت هزینه ای که می‌کنید ضرر نکنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 926 · <a href="https://t.me/danialtaherifar/895" target="_blank">📅 10:52 · 31 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-894">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdGWJnI83_JhZMg-1b00CqQ-obHdXdnCEQiySr6vgyPZaBEk_XMkGdue9GU0wqJWL13qXlzy8Hc9he0pE5dV1-U-Qeb0R1aIkINjNAUtGgfJvZ5LW0bn-w0kaQMhikWpD0XB0CRWF4IbL-CWYGDTbb-A_vbyY2p1G2AkExJI-ONvDPmdB_aeE2LRB0BoP84Bm7lxDDAx83G-lyKjcF6PN6jAd8RncfgUNvOizrd_mE2CoUWbI5IBYSKtwvFfMUOwMMYqsocYuBMWzFcWNArJLGTuMTyy6FOHfyaELHvycj3XHM492dQgRf72AVDXFu7p1pqLB21oPAjyuMnwc7dweg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بررسی آپدیت ژوئن ۲۰۲۵ گوگل: چه اتفاقی افتاد؟
✅
گوگل آپدیت اصلی رتبه ‌دهی خود را بین ۳۰ ژوئن تا ۱۷ ژوئیه ۲۰۲۵ منتشر کرده است. یک تغییر گسترده برای نمایش محتوای مرتبط‌تر و با کیفیت‌.
🔍
چه چیزی در این آپدیت متفاوت بود؟
طبق تحلیل‌ها، این آپدیت برخلاف موارد قبلی، ترکیبی از چند فناوری پیشرفته مثل:
✅
MUVERA (مدل‌های ارتقاء‌یافته بازیابی اطلاعات)
✅
GFM (مدل گراف-محور برای ارزیابی اعتبار محتوا)
رو در الگوریتم گنجانده تا گوگل بتونه:
🔸
محتواهای مفید و مبتنی بر تخصص رو بهتر تشخیص بده
🔸
ارتباط معنایی عمیق‌تری بین کوئری و محتوا برقرار کنه
🔸
تولیدکنندگان محتوا با درک عمیق‌تر از موضوع، ارتقاء پیدا کنن
📌
چی باید بدونی ؟
اگه افت داشتی، محتوای بی‌کیفیت یا قدیمی رو بررسی کن
الگوریتم روی «مفید بودن» و «رضایت کاربر» تمرکز کرده
توی سرچ کنسول دنبال نوسان ترافیک باش
واکنش سریع نکن! اول تحلیل کن بعد اقدام
@danialtaherifar</div>
<div class="tg-footer">👁️ 776 · <a href="https://t.me/danialtaherifar/894" target="_blank">📅 18:37 · 29 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-892">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QZuYE4iks6p5NEQjKpt2KQ2oA4ksXwmk8xazhLziKvXXCvJMIEmD9AoenIyOGA9j2jdQ1XvVMr1EvxESgzSL0JqZI8LEfCJ8F43qppfExVH1qxgo18MfiABAIcu_K3HRZQMtEdaKvwIy_hJR9e6MiTbJlIau5lCQedMwtY6Yw6KpqQU3ZIWDEBXUuxLWASHW8ZtFMTtaz3GfuQZ7_Y63WpJAR1JiNdzbOnviGMmyCihTU8f_U_ycNBmu3BScT-KZdW-e3nF5ZOPJ1ZXj_b98U4KJDVAtEdN4zMK4YSp5oj-0laN1Rax3lfI-s3XE2lxJgOHDVZd-e9GBx-uz0G9ttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rXQ_EVTTPr1u6HFQDoSk5ayImAbTMCNTGD_7pjQoIva6pSvCJTcgav1pltCszoZOAi_fp2JAqZp7N6LiYTL-EWi8Xy4980HI3EAFFzVSpPFzO8jzIbz-l3wWEwmR9DkQzhcleYrK-pK9PQzhqG9n9Ex1A5Vp9A7COrXYRkWi3eClYqMM6cG_EAn2non8tXfS-fwSqIAJpfKHFsFrCuT55Zm0_BCBYVxGca2J0KDX0tvuiYOqbSYG5FGVez-BzNiArWuYeQr8SA03_hYgIqEk5mMG4IrtKvDW3UBdwZ1ath-XjfMyRbBJR9cYIVo53isNxBMJT6yo2fsf5Yb9e-TRsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن بخش Insights  در سرچ کنسول گوگل
🔍
گوگل به ‌تازگی از نسخه جدید گزارش Insights در کنسول جستجوی گوگل رونمایی کرده است. این گزارش که پیش‌تر به‌صورت آزمایشی ارائه شده بود، اکنون به‌طور کامل در داشبورد اصلی GSC ادغام شده است.
❗️
چه اطلاعاتی در این گزارش ارائه می‌شود؟
1. عملکرد کلی سایت
2. پربازدیدترین صفحات
3. کلمات کلیدی برتر
4. دستاوردهای محتوایی
5. تاپ کشور های بازدید کننده
6. ترافیک سورس های مختلف
🕐
این ویژگی به ‌صورت تدریجی برای تمام کاربران در حال فعال ‌سازی است. اگر هنوز آن را در پنل خود نمی‌بینید، طی روزهای آینده دوباره بررسی کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 797 · <a href="https://t.me/danialtaherifar/892" target="_blank">📅 18:43 · 24 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-891">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📌
چطور "اعتماد کاربران" روی رتبه سایت ‌ها اثر می‌گذاره؟
یه پتنت جدید از گوگل منتشر شده که داخلش یه نکته خیلی مهم گفته شده:
«
👀
گوگل داره رفتار واقعی کاربران رو دنبال می‌کنه تا بفهمه به کدوم سایت‌ها اعتماد دارن!»
یعنی چی؟ یعنی دیگه فقط محتوا و بک ‌لینک و سرعت سایت مهم نیست...
✅
اینکه کاربرا واقعاً به سایت شما اعتماد کنن و اون رو به بقیه پیشنهاد بدن، یه سیگنال رتبه‌بندی قدرتمنده!
💡
چطور کاربر، سئو رو تعیین می‌کنه؟
📌
گوگل از مفهومی به‌اسم Trust Signal استفاده می‌کنه، یعنی سیگنال اعتماد. این سیگنال‌ها از کجا میان؟ از رفتار واقعی کاربران توی نتایج جستجو! مثلاً:
🔸
روی کدوم سایت کلیک می‌کنن؟
🔸
چقدر زمان تو اون سایت می‌مونن؟
🔸
آیا اون سایتو به بقیه لینک یا پیشنهاد می‌دن؟
🛠
ایده خفن گوگل: دکمه اعتماد!
توی این پتنت اومده یه دکمه فرضی به اسم Trust Button طراحی شده که کاربر می‌تونه با زدن اون بگه:
👌
«من به این سایت برای فلان موضوع اعتماد دارم!»
گوگل این اعتمادها رو جمع می‌کنه و ازش یه "رتبه اعتماد" برای هر سایت می‌سازه.
سایت ‌هایی که بیشتر مورد اعتماد قرار بگیرن، در نتایج بالاتر می‌رن!
🔝
📈
یاد بگیر چطور اعتماد بسازی!
✅
محتواهای واقعی، کاربردی و انسانی بنویس
✅
کاری کن کاربر حس کنه که وقتش تو سایتت تلف نمی‌شه
✅
با جلب رضایت کاربر، اون رو به یه طرفدار وفادار تبدیل کن
✅
کاربران خوشحال = سیگنال اعتماد قوی = رشد رتبه در گوگل
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/danialtaherifar/891" target="_blank">📅 16:02 · 10 Tir 1404</a></div>
</div>

<div class="tg-post" id="msg-890">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adg0BlQnYeN-BXntz1GNdbD3noCzJk8H5-1IgVB94dC2CEj71q1K9W9ka3yvrMwsqyl5vFRkIZZV4x5riLM3yRMP4_Ym5fuLisL8p-FnsokkcFkut1QqkZRw5d_yhpp0FvENkTX5H_jn3KZovlz3FYLvu4Q56WxWzu8tE1Ui2_plZ0CUEKL9NG9cmn1Vlc8agoBNw3N8gfenngYMRY5-ISabXv3ebEU2zSbOf1Bb19SgaQrDXur7H4r3dAtAeyDxkl_w4rDRKNNzr1isp3XZQee3p-G_6PtjoT0MqU7zvdX1oNcomIzYHFHAlzC6BvUVTv-idu3wW7bxDzldwgCeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
گوگل: ترجمه خودکار رو دیگه با robots.txt نبند!
📰
گوگل به ‌تازگی بخش‌هایی از مستندات robots.txt خود را حذف کرده که قبلاً توصیه می‌کردند برای جلوگیری از ایندکس صفحات ترجمه ‌شده خودکار، از robots.txt استفاده شود. این تغییر باعث هم‌خوانی بیشتر مستندات فنی گوگل با سیاست‌های مبارزه با اسپم شده است.
❓
چرا چنین توصیه‌ای قبلاً وجود داشت؟
هدف اولیه این بود که سایت‌ها بتوانند صفحات ترجمه‌شده (اغلب توسط ابزارهای اتوماتیک) را از دسترس ربات‌ها خارج کنند تا از ایندکس محتوای مشابه جلوگیری شود.
اما اکنون گوگل این راهنما را حذف کرده، چرا که ترجمه خودکار همیشه نشانه محتوای اسپم نیست و نباید به‌صورت پیش‌فرض توسط robots.txt بلاک شود.
گوگل حالا تاکید دارد که تضمین کیفیت ترجمه (کیفیت انسانی یا پس از ویرایش) اولویت دارد، نه محدودیت‌های فنی.
استفاده از متاتگ <meta name="robots" content="noindex"> برای کنترل ایندکس
یا استفاده از attribute هایی مانند notranslate برای جلوگیری از ترجمه خودکار و کاهش اشتباهات ایندکسینگ.
@danialtaherifar</div>
<div class="tg-footer">👁️ 919 · <a href="https://t.me/danialtaherifar/890" target="_blank">📅 11:25 · 22 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-889">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqmpXw5CS5zVZm9o7jTIN6owFLrfeXrSb25PW4TYr61eVqkrzf4bLBhcfl2_Bwbmy4es7NQ_mIGPGvJSEjUPa1LGm2Mkkhdbn89qhjN_2IqoW4fbce_E1gDUv-PE9rispSBjmbIPRtQ-MRh3qCHXTZnIrVP033NQPUu-NhVTS7RBNnejKELIkAYxcjrSV6b1Ygk9-iVpy0bIKhl5L_E3cIVgsIg4O_GVagqaBK4DbBuZSmPGKTBiK5vI5AkNi_HziFm1Jp7PclCYHQqJJwNpJtdStd_qA2VO_uKX0mNe0nS8mquVFclFUrIK6Ff6BGgwInfQjo4PQ3ZlTbM1S-0-OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
نوسان شدید رتبه‌ گوگل در ژوئن ۲۰۲۵
🌪
در ۴ ژوئن ۲۰۲۵ شرایط بسیار ناپایداری در نتایج جستجوی گوگل مشاهده شد؛ ابزارهای معتبر رتبه‌ بندی مثل Semrush, Mozcast, Sistrix و متخصصان سئو متوجه نوسان شدیدی در رتبه صفحات سایت‌ شون شدند.
❓
آیا بروزرسانی رسمی بود؟
خیر، تاکنون گوگل تایید رسمی نداده که یک آپدیت انجام شده باشه، آخرین مورد رسمی، بروزرسانی هسته در مارس ۲۰۲۵ بود. با این حال، از آن زمان تقریباً هر هفته نوسان دیدیم؛ این بار اما شدتش بیشتر و زودتر در هفته بود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 741 · <a href="https://t.me/danialtaherifar/889" target="_blank">📅 12:03 · 19 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-887">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mo1eyb0Aof5SXTTTFjtrK4lLTsPfi1WK7bZ5v2B4MZ0H-AY3nuZMJnQdjG4ehtqog2-RpcSBfjDob-Dvf9m9T8sj4l4YKcYdpCrNnCWO0Xmp1UQIqZwxa3s7pR8anKrJtnlbX_oLTlIWcFdOzfP4Q9jR4ey_e7ECMIYIwewmGQfDnt8rw-buE3arTnSexos2k8UsBd8so11Ov1XfKW7UAsDkajeF9JoH5LXVvC3sAyYkEQCByuPhpZvC5XOPIrWbWRE-TpzxDVW-71OUBa94ssmSPzG9hYc_vUicjXlvR4pNqGU2tjVqYdmOWoUUZFeHIUBWc_YjgRn_nt-5sVRklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbzX1YV74O-SUv9nzE0b0sfDrfWz45vMn3zM2zfxSSi9MAirwFd_1pEDSwU_lokCDQ6gZ3f3JWNuQarEuRSWvDaWDGd2mtXB69AcrufhblBLELYrqa9S1uqguuM7mLDBVxcrrzBGWQeeCfhf5mJ1PpnsuSUxP-v1RjCzUoc2YVtWVUFKegzdfMIyvC1MQ76VohpVMpJ3tMPiT1ybNbQvut5FNQihS68X-0gQfTAU97wzPHhUL5W2m4X8RzQwLsR0hfibjSA6VKkLMfs2tg3I2dQvI4SIivl8CnvQjD3ctm_b1wINeHnzQZPeOJW2VeRYXeUFvf6jLonJfj2NNS9mow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📢
آپدیت جدید گوگل برای داده‌های ساختاریافته Event و Recipe
گوگل به ‌تازگی مستندات Structured Data یا همون داده‌های ساختاریافته رو برای دو بخش مهم یعنی رویداد (Event) و دستور پخت (Recipe) به‌روزرسانی کرده، تغییراتی که می‌تونه روی نمایش سایتت توی نتایج گوگل اثرگذار باشه.
👇
🔸
تغییرات در داده‌های ساختاریافته رویداد (Event)
✅
گوگل حالا به‌طور دقیق‌تر توضیح داده که چه نوع رویدادهایی می‌تونن در rich result بخش "Events" نمایش داده بشن.
❌
مهم‌ترین تغییر: ویژگی‌های مربوط به «رویدادهای آنلاین» دیگه پشتیبانی نمی‌شن!
📍
فقط رویدادهایی که در محل فیزیکی برگزار می‌شن و قابل رزرو برای عموم مردم هستن، شانس نمایش در نتایج Google Events رو دارن.
🔸
تغییرات در داده‌های ساختاریافته دستور پخت (Recipe)
📌
گوگل رسماً اعلام کرده که ویژگی image داخل داده‌ی ساختاریافته Recipe،
هیچ نقشی در انتخاب تصویر نهایی در نتایج جستجو نداره
😮
🔍
اگه میخوای تصویرت توی نتایج نمایش داده بشه، باید:
✔️
تصاویر با کیفیت، سبک و بهینه داشته باشی
✔️
باید alt-text و context مناسب برای تصویر قرار بدی
@danialtaherifar</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/danialtaherifar/887" target="_blank">📅 15:07 · 16 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-886">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajCLOMBddM1gszgTbsrfe5Rs2cJhotASPk7FnbpRvmwW-xlBg7JfOKz6CNKr2rbA6kmN7T3O95Mtx1cDxCqXK9-EC3a6Bix2NUv63aTz9cUieO5DEasrEOk9sQshKWo4at-NB0-fZ78Dy9J6JGWFZ-I_TgPOOsdxie6uYHCy1wbfGs4JSTB2rbwRSs2DO0rdHUU3Kbym9aONQwUFQV58yRNdcAqKk1PdWca6t2Vw3z-wS7q92qtURK72jNfK3ak1xTpERLIuO4MJE1wirIiD8WAqbWRUVNryYK1Qt7OxGI3ORbGn9KTSKS-Ahojf6diKtIqGibRxHH1wW0DoXukYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل سیگنال‌ های زمینه‌ای رو به نتایج جستجو اضافه می‌کنه
📌
‌ پتنت جدید گوگل نشون میده که قراره جستجوها خیلی دقیق‌تر و هوشمندتر بشن! دیگه فقط کلمات کلیدی مهم نیستن، گوگل حالا به شرایط و رفتار کاربر هم توجه می‌کنه!
📍
گوگل به موقعیت و زمان هم توجه می‌کنه!
فرض کن شب جمعه ساعت ۸، سرچ می‌کنی "پیتزا"
🍕
گوگل ممکنه بفهمه دنبال سفارش آنلاین پیتزا نزدیک خودتی، نه تاریخچه پیتزا!
😳
یا اگه بلیط یه فیلم رو خریدی و بعد اسمش رو سرچ کردی، احتمالاً دنبال تریلر یا نقدشی، نه یه بلیط دیگه!
🔁
بازنویسی هوشمند کوئری‌ها
🧠
گوگل با استفاده از داده‌های مختلف (مثل مکان، زمان، سابقه سرچ‌هات) می‌تونه کوئری‌ تو بهتر بفهمه و حتی یه نسخه دقیق‌تر ازش بسازه تا نتایج بهتری بهت بده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 661 · <a href="https://t.me/danialtaherifar/886" target="_blank">📅 14:06 · 14 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-885">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔍
جستجویی که می‌فروشد!
🤔
تا حالا فکر کردی چرا بعضی از سایت‌ ها با اینکه رتبه‌ی خوبی تو گوگل دارن، باز هم فروششون تعریفی نداره؟ یا برعکس، یه سایت شاید رتبه اول نباشه ولی همیشه مشتری داره!
🧠
واقعیت اینه که رتبه بالا فقط یه تکه از پازل موفقیت در سئوئه!
📌
این 4 تا نکته بهت کمک میکنه که بیشتر بفروشی
:
👇
1️⃣
هدف جستجوگر رو بشناس!
فقط به کلمات کلیدی نگاه نکن، بفهم چرا کاربر اون عبارت رو سرچ کرده. مثلا "کفش مردانه" یه جستجوی کلیه ولی "خرید کفش مردانه راحتی" یعنی آمادگی برای خرید!
👟
🛒
2️⃣
محتوایی بساز که بفروشه!
یعنی چی؟ یعنی محتوا باید مخاطب رو به قدم بعدی هدایت کنه:
ثبت‌ نام
📩
، خرید
🛍
، یا تماس
📞
. نه اینکه فقط اطلاعات بده و ول کنه بره!
3️⃣
داده‌ها رو جدی بگیر!
با Google Analytics و ابزارهای سئو بررسی کن که کدوم صفحات بیشتر تبدیل دارن. شاید یه مقاله تو رتبه ۳ باشه ولی دو برابر بیشتر بفروشه از رتبه ۱!
4️⃣
تجربه کاربری = کلید تبدیل
!
🔑
سرعت سایت، طراحی زیبا، دکمه‌های فراخوان (CTA) واضح… همه اینا کمک می‌کنن بازدیدکننده‌ها تبدیل به مشتری بشن.
🧭
🎯
فرمول طلایی موفقیت در سئو:
رتبه خوب + محتوای هدفمند + بهینه‌سازی تبدیل = فروش بیشتر
💸
🗣
پس دفعه بعدی که داشتی رتبه‌ات رو چک می‌کردی، این سؤال رو هم بپرس:
"این رتبه داره برام پول می‌سازه یا فقط دلمو خوش کرده؟"
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 809 · <a href="https://t.me/danialtaherifar/885" target="_blank">📅 13:22 · 07 Khordad 1404</a></div>
</div>

<div class="tg-post" id="msg-884">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔍
نگاهی به سیستم‌ های رتبه‌ بندی گوگل
👇
این اطلاعات نگاهی نادر به نحوه ارزیابی کیفیت صفحات، سیگنال‌ های محبوبیت و نقش داده‌های مرورگر Chrome در رتبه‌ بندی نتایج جستجو ارائه می‌دهد.
🛠
سیگنال‌ های ABC: پایه‌های رتبه‌بندی
گوگل از سه نوع سیگنال اصلی برای تعیین ارتباط محتوا با جستجوی کاربر استفاده می‌کند:
A – Anchors
: لینک‌هایی که به صفحه هدف اشاره دارند.
B – Body
: وجود کلمات کلیدی مرتبط در متن صفحه.
C – Clicks
: رفتار کاربر، مانند مدت زمانی که در صفحه می‌ماند قبل از بازگشت به نتایج جستجو.
🔹
این سیگنال‌ها به صورت دستی تنظیم می‌شوند تا الگوریتم‌های رتبه‌بندی قابل فهم و قابل کنترل باقی بمانند.
📄
کیفیت صفحه: معیاری ثابت و مستقل از جستجو
کیفیت یک صفحه، که نشان‌دهنده میزان اعتماد و اعتبار آن است، به طور کلی مستقل از جستجوی خاصی است. این معیار به صورت ایستا در نظر گرفته می‌شود و برای همه جستجوهای مرتبط اعمال می‌شود. با این حال، در برخی موارد، اطلاعات مرتبط با جستجو نیز می‌تواند در ارزیابی کیفیت صفحه تأثیرگذار باشد.
🤖
سیستم eDeepRank: استفاده از مدل‌ های زبانی بزرگ
سیستم eDeepRank از مدل‌های زبانی بزرگ مانند BERT برای تحلیل محتوا استفاده می‌کند. هدف این سیستم، تجزیه سیگنال‌های پیچیده به اجزای قابل فهم‌تر است تا مهندسان گوگل بتوانند دلایل رتبه‌بندی صفحات را بهتر درک کنند.
🔍
سیگنال محبوبیت مبتنی بر داده‌های Chrome
یکی از سیگنال‌های رتبه‌بندی، که نام آن در اسناد محرمانه باقی مانده، از داده‌های مرورگر Chrome برای ارزیابی محبوبیت صفحات استفاده می‌کند. اگرچه جزئیات این سیگنال مشخص نیست، اما وجود آن نشان می‌دهد که رفتار کاربران در مرورگر می‌تواند بر رتبه‌بندی نتایج جستجو تأثیرگذار باشد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 817 · <a href="https://t.me/danialtaherifar/884" target="_blank">📅 14:38 · 31 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-883">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/danialtaherifar/883" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📌
پتنت Site Quality Score چیه؟
🧠
پتنت شماره
US9031929B1
یکی از روش‌های گوگل برای سنجش کیفیت کلی یک سایت در نتایج جستجوئه!
💡
تو این پتنت، گوگل با استفاده از نسبت بین:
🔍
تعداد جستجوهایی که به یه سایت ختم میشن (مثلاً سرچ "ویکی پدیا")
👆
و تعداد کلیک‌هایی که روی اون سایت تو نتایج زده میشه، یک امتیاز کیفیت سایت (Site Quality Score) محاسبه می‌کنه!
✅
نتیجه ؟
افزایش جستجوی برند + نرخ کلیک بالا = امتیاز کیفیت بالاتر = رتبه بهتر تو گوگل!
@danialtaherifar</div>
<div class="tg-footer">👁️ 719 · <a href="https://t.me/danialtaherifar/883" target="_blank">📅 17:13 · 29 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-882">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpJ9gScxNaDu8s2_oiZo8Oj5lFVeBOjINl6On90u5Ei3Mj6Q1xipMPz60F9Sj13sluZEnwVEc05tPdsVPycRaxSdoD5hpNrCUcBQp80BEFIwG7vzYBRk3IELifzQrsXnBqVrMPI_x44tUiqgtSB_OWY0hq1PQBTTsbGd-Wn1oGfoUNCPXlNAUZZ6YEHI4I7pMpY5hGoP4OYaITY2J9mDWu8qkELXjuVFuYUCgAD9WB5nb3UjX2oedBIlYQxvXhaaKY-tGL48p8axr3rR3U84C-2Itkweo3xV1gnt0UGHWGP7x5nVFV29LKegl1P7mAZ6MOhVmqPU7ZXVMOaKMGizsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رتبه‌ی یکسان برای همه لینک‌ها در بخش AI گوگل
📈
گوگل بالاخره تایید کرد که لینک‌هایی که توی بخش پاسخ هوشمند (همون AI Overview) در نتایج جستجو نمایش داده می‌شن، همگی با هم یک موقعیت یا رتبه در کنسول جستجو ثبت می‌شن!
🤔
یعنی چی؟
یعنی اگه توی یه AI Overview چند تا لینک از سایت‌های مختلف نشون داده بشه، همشون با هم یک Position حساب می‌شن. فرقی نمی‌کنه لینک اول باشه یا سوم؛ گوگل بهشون یه رتبه‌ی مشترک می‌ده.
🔍
چرا این مهمه؟
📉
ممکنه باعث بشه نرخ کلیک (CTR) سایتت بیاد پایین! چون:
خیلی از کاربرا جوابشون رو همون توی AI Overview می‌گیرن،
و دیگه روی لینک‌ها کلیک نمی‌کنن!
😕
📌
گوگل چی میگه؟
الان هیچ دیتای جداگونه‌ای برای AI Overview توی Search Console نشون نمیدن.
همه لینک‌ها با همدیگه یه رتبه دارن.
فعلاً هم برنامه‌ای برای تغییرش ندارن
😬
@danialtaherifar</div>
<div class="tg-footer">👁️ 820 · <a href="https://t.me/danialtaherifar/882" target="_blank">📅 15:14 · 27 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-881">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cveXFN-oQ_51GjXu3-b-tGew0F5tDUrjnVLqLEAs0goqmnRBhsxsDxraioqGi8beu3hZ-tgIregfTwdvct37kEA9B6Pt42d0kI1go_NEmk7AXGvwm95GAXaxpjSuQrFvObqN97bdKCKa6QxOxhSCbMdu-RTMlfics2ARSpwfgDuCL2omAh0Huwqps_6A5NHWfMhl1jzS3rOm6Dav1Tr3X7HGG8mhUQViqfNm6UoNELK91YbIh--pyXnFBMOB8YLIsh-GICCpIU79y2aW2_0YjocNh79waLYyQgYOYxn6nezf_MP8lCpSeNhjexE9u0Om6hpJO7PntgrwikMKWfHkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل: Navboost یک سیستم یادگیری ماشین نیست!
در تازه‌ترین افشاگری‌ها پیرامون سیستم‌های رتبه‌بندی گوگل، یک نکته بسیار مهم روشن شد:
سیستمی به نام Navboost که تصور می‌شد یک الگوریتم هوشمند باشد، در واقع هیچ ربطی به یادگیری ماشین (Machine Learning) ندارد!
🔍
اما Navboost دقیقاً چیه؟
👨‍💻
به گفته‌ی دکتر اریک لِهمن، از مهندسان سابق گوگل:
بیشتر شبیه به یک جدول عظیم از داده‌های کلیکی کاربران برای کوئری‌های مختلفه؛ اطلاعاتی مثل تعداد کلیک‌ها، امتیازات و چند فاکتور ساده‌ی دیگه.»
🔸
یعنی به‌جای اینکه تصمیمات بر اساس هوش مصنوعی گرفته بشن، این سیستم صرفاً داده‌هایی مثل "چه کسی روی چه لینکی کلیک کرده" رو جمع‌آوری و نگهداری می‌کنه.
🧠
سیگنال‌ های رتبه‌بندی؛ دستی نه هوشمند!
🧩
بسیاری از سیگنال‌هایی که در رتبه‌بندی نتایج جستجوی گوگل تأثیر دارن، به‌صورت دستی توسط مهندسان تنظیم شده‌اند.
گوگل از توابع ریاضی مثل sigmoid و مقادیر آستانه برای ساخت این سیگنال‌ها استفاده می‌کنه؛ نه از مدل‌های پیچیده‌ی هوش مصنوعی (جز در مواردی مثل RankBrain و DeepRank).
@danialtaherifar</div>
<div class="tg-footer">👁️ 602 · <a href="https://t.me/danialtaherifar/881" target="_blank">📅 17:42 · 25 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-880">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA-I6r7BgB9Xh-UoH_Nk_Wsot5m8iOArSqTpKDa7xA_OcdAq3UMC1ipQnnSjQc19dT_pHNa5Uz-WV7wW2zh7LQ50mWg72OC-PNj8ZJpHrWCH-i2e245q941PKKdOrWGNsDbbcs8yFTzrN8CnhJnJE10dlY96rNTgh5mtqXBPtE1kgf_ilP1OXJRh5ITQvZRkW5A64qZW6kVV1_PnztDBATuubUgENB8BDZZ4Qjs1Q0bq_0v2TYNRzaxFNK-Ww4cxmxNk56mmJn2mhwn9G0BOMjGqpNLFE9sGl5mMF9LuHTTNYDbTMwZNvWeA4OZnaZl_Z30CJnpzzwfcvY2jO9oQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
چطور توی Google Discover بیشتر دیده بشیم؟
🔹
۱. محتوای با کیفیت بنویس
📌
فقط نوشتن کلمات کلیدی کافی نیست، محتوات باید واقعا مفید، مرتبط و جذاب باشه تا گوگل بهش توجه کنه.
🔹
۲. از عکس‌های باکیفیت استفاده کن
🖼
عکس با عرض ۱۲۰۰ پیکسل یا بیشتر؟ عالیه! چون باعث میشه کارت تو Discover بهتر دیده بشه و نرخ کلیکت بیشتر شه.
🔹
۳. موبایل فرندلی باش
📱
بیشتر کاربران از موبایل استفاده می‌کنن. پس سایتت باید سبک، سریع و بدون مشکل تو گوشی لود بشه.
🔹
۴. داده‌های ساختاریافته فراموش نشه
🧩
با استفاده از
Schema.org
به گوگل کمک کن بفهمه محتوات در مورد چیه. همین یک کار ساده باعث رشد دیده‌شدن میشه.
🔹
۵. حتما E-E-A-T رو جدی بگیر
🏅
هر چی اعتبار سایت و نویسنده‌ت بیشتر باشه، گوگل بیشتر بهت بها میده.
🔹
۶. سراغ ترندها برو
📈
محتواهای داغ و به‌روز توی گوگل دیسکاور شانس بیشتری دارن. اگه خبری یا موضوع جدیدی هست، سریع پوشش بده!
اگه می‌خوای تو Google Discover بدرخشی
💥
باید محتوای فوق‌ العاده جذاب و تجربه کاربری عالی داشته باشی.
@danialtaherifar</div>
<div class="tg-footer">👁️ 694 · <a href="https://t.me/danialtaherifar/880" target="_blank">📅 19:13 · 24 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-879">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔎
چارچوب Triple P در دنیای جست‌وجوی هوش مصنوعی؛ حضور، ادراک و عملکرد برندها
🌐
✨
📌
در دنیای دیجیتال امروز، موتورهای جست‌وجو با کمک هوش مصنوعی به سطحی رسیده‌اند که فقط نمایش لینک نیستند، بلکه تجربه‌ای هوشمندانه و تعاملی را برای کاربر خلق می‌کنند. حالا دیگه وقتشه برندها با رویکرد جدیدی به سئو و دیده‌شدن نگاه کنن!
👀
اینجاست که چارچوب Triple P وارد می‌شه:
✅
1. Presence (حضور)
🔹
آیا برندت تو نتایج جست‌وجوی هوش مصنوعی حضور داره؟
🔹
تو مدل‌های جدید AI مثل Gemini یا ChatGPT، دیده می‌شی یا نه؟
📍
حضور برندت تو پاسخ‌های تعاملی خیلی مهم‌تر از قبل شده. دیگه فقط لینک اول گوگل کافی نیست!
🧠
2. Perception (ادراک برند)
🔹
چطور مخاطب وقتی اسم برندتو تو پاسخ‌های AI می‌شنوه، نسبت بهش حس پیدا می‌کنه؟
🔹
آیا برندت قابل‌اعتماد، معتبر و پاسخ‌گو جلوه می‌کنه؟
📢
هوش مصنوعی بر اساس داده‌هایی که از برندت داره، درباره‌ات نظر می‌ده! پس محتوای درست و دقیق تولید کن.
🚀
3. Performance (عملکرد)
🔹
آیا حضور و تصویر ذهنی برندت در نهایت باعث کلیک، خرید یا تعامل می‌شه؟
🔹
چقدر از پاسخ‌های AI به سود واقعی برندت منجر می‌شن؟
📊
حالا دیگه اندازه‌گیری عملکرد تو جست‌وجوی AI فقط به کلیک محدود نیست، باید ببینی خروجی چیه!
✨
چرا چارچوب Triple P مهمه؟
چون در عصر هوش مصنوعی، برندهایی که فقط به سئو کلاسیک تکیه می‌کنن، عقب می‌مونن. برندهایی برنده‌ن که در جست‌وجوهای هوشمند هم دیده بشن، درست فهمیده بشن و نتیجه بگیرن!
📣
اگه هنوز به‌روزرسانی استراتژی سئوت رو با تمرکز روی AI Search شروع نکردی، الآن بهترین زمانشه!
@danialtaherifar</div>
<div class="tg-footer">👁️ 638 · <a href="https://t.me/danialtaherifar/879" target="_blank">📅 12:17 · 23 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-874">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJvDsIy5PuYVNp-EE92NeOedca8WcbO_GgLiJ6Jq2qYAHEhmWtfiM6iKK6u4lrncWkT4Qc8z1QchEqUGGjOvUE2xdKtS3E5ki5AWzLi05ILkrq8ob1tfCEZp7sbKhkHMzCTH5y2YZRpMXD2s5uPbiGMNWIIVf34BNk0cMxvwuoOIO1uX30j1LG1GAxyMyGC1QG3GoGqkWJlKYnaCrQ35976ULrpNc9EqJslkXPEHpGjuI7470BNC7Br-he7rN6kFecxGgGx3ovRpD-vqQ0NKDyedYI20JBs7c486iFZM61o_L8X3-Au3RQgOPnvlgh2pvgifQZNOx-eUjUdmAMSCSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4Bb-EZZpmaQ3IKlshOuvhh6VAukpYl72sU_qSffCRXSzjWhqc8nYJEhTU9fPY8oRmHFKJKPO1KczOk47lOSabXXjxTK5OUpa1003e8FDWckj8zoahVmnAAC8CBnwfxHdImY_ITYa4crslCBQ7ELqMszITL-_KK_bEo8knQhsIcxAeLdy6p0ZXrHMEhZxHKY9xjB2DTdp-tasH_XbKh-dlPYPe9tVJ4nCbL5XuLf3Eqz0nBBpUh9DnQntTHnBlWQaMsdj-etaqzOVqAy-6B8yB4bprUWP7oz4eG-pvE5IaU4nc1ThT1YTrbqIEaJdeG7KrD-AV4iBi9HSJK-RZwX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoabTEl08T6WtvIppluJcaNFoe44OWAmAvPfEQs_G1YMitSnSGXslETLcWQh_f9ezYWNUuezWBO_X2Wqvsln2nvBCoP9h54VvT0mZ1lGjv7xrDpmTUvKmcPzQzOwgO375DB_bkDdFNgU-jx_F1vf7a_VZ73LOCwbclG2o-zp8G2nUOolSysEasH15C7LlrUpB6Y4LIvGSYBUm7TnD8Brb9zIXXoZDuCgaFcnHhEvSorg6w0ukICjAhfcJAJKXhyBZx2DweGMPP2OFD4s-IoSHM0LqBGcxVdt7d2-_FSX0_nt4WWpPhGR29KlP8NEHxEONMOtA5vT8kpB68AbhgBwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fHffnwO7h3ie3geSYD7Xjx5GKChKa52L8o8ZUGphKMqdMaUJQYFkxPv1tpydXTR4N7-Cur83WBaiKdyDtX4dCnUhllqA-hqRqaV5ub9bjiqFzrjAqPfUuyVYnJX3OC1zBSFQoezahLxFQhJyQaH4oLWgUcz_Muqfy9S0U6Q2ZW4dPr4F5I3dYQ96fTBwwIeLp4vF5OhV6Ln1I_vkJ16juoQWE1YEutzin1esNbkD2Sru0tD13jAN9s1niMPYJbE4lt6sdzc86NZgQS4iWp7GVT0bSeo9e1m999UBWDHLR7UNKzAKNLmQ8m31Gg_sia5wyRI_XxPDExrSUba2mKKqbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KyMgEHndRbYsPOzhZNfP5wc29Dg7sDDVz7n51-nmD92nvHQCc_op_ZoUKG5LW2QHFIW9FL75Mveeyho4PkWqIafcBcuFG_o3UYx0z4y6Ea2jqGZ5sGEQfKeNZoT7Zyp2G-c_C6NohgNWpwBFFX72a7PEf98VAUD5KG9p6lBvb0SIH6eETfQBm5gr7tPeGiBRIj9N4-qPFWh28rif5hY7Yp-HvArZ2cRXZw0C74sBkq-3lvloVcVO7fAOjRDAtjDWlwMu-QWx9aT-0IeTsz9ZLJghEvsj_Y0yQah3j-COajFznznA9MAm_OdeIn53V3nUR24hDvmeawNLaK5XkcYGFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1sT65d4fA0moq9Ai1Rem3GOi853yR2-0Jnl7DoDPpo0evGujAIur0EXXfgQqtzbW2U8ANgJxKPtgGV281OE18WQrnnNb4-Z6Xy4iegPw_o0r0ahENBwnUfpR-boED1LpMVZaJDsvBcc006fZXXIyiUtqokdtjacBzdyQY_Qx4SSb6coAfJ6Anpa1CSd-7yHsEN_4UruZR6tSzHGNPMiMfhnaZMI2D43ZGo16kRpDlZaH7aYMFK75L2UbBSNfi_47mR_3q8sWLGn1fpT0cfFXLDCaUCtOT3qtbUB1xgPNPA1JnLP08rgEEnKU_8BopG4EN5DNwSX5pfd-RNbktcD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:
1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.
2. تعداد جستجوهای نام برندهای رقیب را نیز جمع‌آوری کنید.
3. مجموع جستجوهای برند خود را بر مجموع کل جستجوهای برندها تقسیم کرده و در 100 ضرب کنید.
🎯
مثال: اگر برند شما ۲۰٬۰۰۰ جستجو و سه رقیب اصلی به ترتیب ۱۵٬۰۰۰، ۱۰٬۰۰۰ و ۵٬۰۰۰ جستجو داشته باشند، سهم جستجوی شما:
20,000 ÷ (20,000 + 15,000 + 10,000 + 5,000) × 100 = 40%
💡
چرا باید بهش اهمیت بدیم؟
🧠
بهت کمک می‌کنه بفهمی جایگاه برندت تو ذهن مخاطبا کجاست.
📈
یه شاخص عالی برای پیش‌ بینی رشد یا افت بازار در آینده‌ است.
🔧
می‌تونی استراتژی‌های سئوت رو بهینه‌تر کنی و رقبا رو پشت سر بذاری!
@danialtaherifar</div>
<div class="tg-footer">👁️ 577 · <a href="https://t.me/danialtaherifar/873" target="_blank">📅 16:16 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-872">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS9v9z5qVvYEiywVMx3w4OQI9WWK6mPevrY6fGiyFP2FYG-Vx09_wgRZE1QKBVJQvsE3BnVhhcAu431jMxiCDfmeTUT9tdYT3J1Ui-EAGh2xfNgSL5SYER4TN5NWNA0lUPmf7xAaNdD8BX9GiBpxabRkfPuxBcg32ZuBT3p-_JGwMoIDYD-mzzoGl_d2aAUDTWUgRmseKKF9OUrKlvH6FZg765Rs5lFGfWCV2h8bRCS_ymK6pFbdblm_L6ThHhMQx0f-K091NAU22veAKr5-WUzCtX7HxJI3VAqVlyyW13KuyVTvEXr1VeqlLKn0aNFLre-n2m8bOF1EchZFAF6FLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
نحوه استفاده از پارامترهای زبان و کشور در جستجوی گوگل
اگر به دنبال راهی هستید تا نتایج جستجوی گوگل را بر اساس زبان یا کشور خاصی مشاهده کنید (مثلاً فقط نتایج فارسی برای ایران)، گوگل راهکاری ساده اما بسیار کاربردی در اختیارتان گذاشته است. کافی‌ست از دو پارامتر ویژه در انتهای لینک جستجو استفاده کنید.
🛠
تنظیم زبان و کشور در URL جستجو
&hl=کد_زبان → مشخص‌کننده زبان رابط کاربری (مثال: &hl=fa برای زبان فارسی)
&gl=کد_کشور → مشخص‌کننده کشور هدف (مثال: &gl=IR برای ایران)
💡
مثال کاربردی:
https://www.google.com/search?q=دانلود+فیلم&hl=fa&gl=IR
🎯
مزایای استفاده از این قابلیت
✔️
مناسب برای تحلیل سئو بین‌المللی و بررسی نتایج در کشورهای مختلف
✔️
مشاهده دقیق‌تر نتایج کاربران در زبان‌ها و مناطق متفاوت
✔️
قابل استفاده برای تولیدکنندگان محتوا، بازاریابان و متخصصان دیجیتال مارکتینگ
✔️
بدون نیاز به تغییر تنظیمات مرورگر یا حساب کاربری گوگل
@danialtaherifar</div>
<div class="tg-footer">👁️ 588 · <a href="https://t.me/danialtaherifar/872" target="_blank">📅 18:11 · 20 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-871">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu2pY-UynyTplEF5SGjHJNn6VBkH1GpgQ2sxTDYAOhxSiHsBZBQAQQz4YhwjpAGWzQ7VbQ_KK8E7AGmHoEp7VtBZe31Fjedbhcu1ZgrjzFpWMPePX0v21upoc5ZvwUQYDH4IBRcDA51iM-xV3EnFHD10Kmewtqrs59zZ6ox4GGPDMNewUhXiK4IZJiaHnqJ-pS4LGj2Cu001a84lukwn9XnILLxOfyyj2m0ekbbD_GJ9aElMnAuotTeLSNSzkKGIZ0Wkb-ik0WonYPsH_uHFtmdTBavgMm2C4mwoCWt0ShPzKCnxNC9no6B0QbW88qUsy4ooCTnR7zleOirQFMwMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گوگل علیه محتوای فیک E-E-A-T وارد عمل شد!
گوگل توی آخرین آپدیت دستورالعمل‌های ارزیاب‌هاش، تمرکز ویژه‌ای روی مقابله با محتوای تقلبی و مخصوصاً محتوایی که به‌دروغ نشون میده تجربه یا تخصص داره (E-E-A-T) گذاشته!
🧠
چه چیزایی تغییر کرده؟
🔹
محتوای دارای تجربه واقعی اولویت داره
🔹
اعتماد مهم‌ترین عامل برای رتبه‌بندیه
🔹
تولید محتوا با هوش مصنوعی بدون بررسی انسانی = خطر سقوط توی سرچ!
📌
نکته مهم برای سئوکارها و نویسنده‌ها:
اگر تجربه واقعی، منابع معتبر و شفافیت نداشته باشی، گوگل دیگه باهات شوخی نداره!
😅
@danialtaherifar</div>
<div class="tg-footer">👁️ 698 · <a href="https://t.me/danialtaherifar/871" target="_blank">📅 13:08 · 17 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-870">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7XC-v-6-xLrtuivPBYFnEzOREaMjgS1CF3GYfPycgIKSms9Gc52ilxp7bXLosgxMViMdKvMYXD3UmoI9LBXE80q1T5b0rA5sMfugz09ZuiaTfAL7JqEZDOZHfu1jf7kzd_Dnl4hbUTFpmm9ao4U_tdDNxKDWDIj-l6eu_Erbvf3suwrSz-OGNw5UePA9xyy7YVzVO-Nt2Pup4qFhW8NyxbIrQCwJHdq-y3oPNdXgzeEp2_hGIMi4QvaZLz051TKJAqxy9_qtgS26eTYBtUsa5a3Q52tADRINaLfKss2iOh-w2BZW3eojMbtJmL45X9HbeAm0EjMLMqTOQXwRD7YuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
رندرینگ سمت سرور در مقابل سمت کلاینت: توصیه‌ های گوگل
👨‍💻
رندرینگ سمت سرور (SSR) چیست؟
در SSR، محتوای صفحات وب در سرور تولید شده و به‌صورت HTML کامل به مرورگر ارسال می‌شود. این روش به موتورهای جستجو امکان می‌دهد تا محتوا را به‌راحتی ایندکس کنند، زیرا نیازی به اجرای جاوااسکریپت در مرورگر نیست.
🧑‍💻
رندرینگ سمت کلاینت (CSR) چیست؟
در CSR، مرورگر ابتدا یک HTML ساده دریافت می‌کند و سپس با اجرای جاوااسکریپت، محتوا را تولید و نمایش می‌دهد. این روش برای برنامه‌های وب تعاملی مناسب است، اما ممکن است موتورهای جستجو در ایندکس کردن محتوا با مشکل مواجه شوند.
📈
توصیه‌های گوگل:
گوگل اعلام کرده است که هیچ مزیت خاصی از نظر سئو برای SSR یا CSR وجود ندارد. مهم‌ترین نکته این است که محتوای سایت به‌گونه‌ای باشد که موتورهای جستجو بتوانند آن را به‌درستی ایندکس کنند.
🔹
اگر سئو برای شما اولویت دارد، SSR می‌تواند گزینه مناسبی باشد.
🔹
اگر به دنبال تجربه کاربری تعاملی هستید، CSR را در نظر بگیرید.
🔹
در برخی موارد، ترکیبی از هر دو روش (رندرینگ ترکیبی) می‌تواند بهترین نتیجه را ارائه دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 643 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7s9zpNTndIUf7Cb7xLYZxRKzhCr5-5C1a9v-CADUKFpl_JRMgKhL7QycHIMFHO33PbVoi2z3fyyrcUt-965UW29onX-GRjnshfCfvV-NQVWiVa8fn7PtWNK-Na2i56q7ZlZyrBMjZhq6drMbJvSEWMZG5uX5dyTnaeaX5zbzqtnXxRW3M6oYqXcxFl8YYy7zCuseb1YzWLOEdvqVu33rmjYWieRhN5EMrp2XhmiXuIkchwklP37Gfr_78Dv710zvEZ_xnvd7kZq0Kq-erU8U5XqCqtsjD2m4D_j4sULnvRbyg1G4vrRuPt4MpiYkdFRhc-tfX2m42WUh8M4YnIDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎧
ابزار NotebookLM گوگل حالا در بیش از ۵۰ زبان در دسترس است!
📢
گوگل قابلیت «خلاصه‌های صوتی» (Audio Overviews) را در ابزار هوش مصنوعی NotebookLM گسترش داده و اکنون این ویژگی در بیش از ۵۰ زبان مختلف، از جمله فارسی، اسپانیایی، پرتغالی، فرانسوی، هندی، ترکی، کره‌ای و چینی، در دسترس کاربران است. ​
🎙
این ابزار با تبدیل منابع متنی به گفتگوهای صوتی شبیه به پادکست، به کاربران امکان می‌دهد تا اطلاعات را به‌صورت شنیداری و تعاملی دریافت کنند. با استفاده از پشتیبانی صوتی بومی Gemini، کاربران می‌توانند خلاصه‌های صوتی را به زبان دلخواه خود بشنوند.​
🌐
برای تغییر زبان خروجی، کافی است به تنظیمات NotebookLM رفته و زبان مورد نظر را انتخاب کنید. این قابلیت از سال گذشته در بیش از ۲۰۰ کشور راه‌اندازی شده و گوگل قصد دارد با دریافت بازخورد کاربران، آن را بهبود بخشد.​
✅
همچنین، گوگل این ویژگی را به چت‌بات Gemini و Google Docs نیز اضافه کرده است، تا کاربران بتوانند انواع بیشتری از محتوای نوشتاری را به صورت صوتی دریافت کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 711 · <a href="https://t.me/danialtaherifar/869" target="_blank">📅 14:16 · 10 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-868">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byHkcM8ea_XXv0cC41j81Pq2P1H0xJTL_FN3OkwJ-I_GygaFBMQBW2jsTPyC4I1GFMYeW3XHF0Nq3b39Sed7YfS2cVTdyRxC_qqlEuQeXplTXAXrRpd47HTBu5tseqHVkqjsxQzBU-sWriuJ_Db4x5KTRwrwqwbPzxzaQkp6wsUKJoWsXP9GBC0_3f2EW1ijA0pGyCmrknzwlMg4g3-_G5nTtaqnNye5fl-1-xa2mITLV3FFwjDZuPlL7eIRqEYl_yZt_DtNpcKcLk62Z4mG9Y1w3j9Jbr9_sS0OinoZjtCYFP43qK82cLomo4KL0jSbPKYbbVReC9XOV4ZBqOk8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
جان مولر: آپدیت تاریخ XML Sitemap تأثیری روی سئو ندارد !
🗣
جان مولر، تحلیل‌گر ارشد گوگل، اخیراً تأکید کرده که تغییر خودکار تاریخ‌ها در نقشه‌ سایت XML (تگ <lastmod>) بدون تغییر واقعی در محتوا، نه تنها به بهبود سئو کمک نمی‌کند، بلکه ممکن است فرآیند شناسایی به‌روزرسانی‌های واقعی را برای گوگل دشوارتر کند.​
❌
کارهایی که نباید انجام بدید:
فقط تاریخ‌ها رو آپدیت نکنید اگه محتوا تغییر نکرده.
ابزارهایی که اتوماتیک تاریخ‌ها رو عوض می‌کنن، فایده‌ای ندارن.
گوگل می‌فهمه که محتوا واقعاً تغییر نکرده!
✅
چی کار کنیم؟
فقط وقتی که محتوا، لینک‌ها یا دیتاهای صفحه تغییر کردن، تاریخ رو عوض کنید.
نقشه سایت رو با تغییرات واقعی همگام کنید، نه مصنوعی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/868" target="_blank">📅 12:27 · 09 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-867">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN01GvtB4AtMI5kPEwCagqmodObEFSb_HSRJ1SlNtF23aIDi6IhGsoWaVD00sc-HW6SuBKyBp0m6ZZ71FYzr44Gj62fqi_y8b_dD-JwFBShGv39sZAJqSkwVBMo8xvpDcYqTLoomH-QUDHCj48AHvWFTR_mHJXmxAt0fZPzbXdtB9WnrfqKKGbe86WKvLZj3FzU4LSmfpJY094hJ6YjdkKDaMWVhagKfYxrh2K5GT6Lal6NJFbO_jRHWyXJ2_ppAZmgI4xkk2gP2-0R3NHaoNk0TQkAcJwnAyOPdngmnGFT5e__GuO4aYqfAJVNzYutM-rUEOuUK-pJOdFiyErmfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
گوگل مستندات Google-Extended را آپدیت کرد: کنترل بیشتر روی داده‌های آموزش AI!
🌐
این به‌روزرسانی به ناشران کمک می‌کنه دقیق‌تر تصمیم بگیرن که آیا داده‌های سایت‌شون برای آموزش مدل‌های آینده Gemini و Vertex AI استفاده بشه یا نه.
✍️
گوگل اکستندر یک user agent است که به وب‌سایت‌ها امکان می‌دهد تعیین کنند آیا محتوای‌شان می‌تواند برای آموزش مدل‌های Gemini و Vertex AI استفاده شود یا خیر.
با مسدود کردن این agent از طریق فایل robots.txt می‌توان جلوی استفاده از داده‌ها را گرفت.
🔹
نکته مهم: Google-Extended تاثیری روی رتبه‌بندی جستجو یا ایندکس شدن سایت شما نداره.
@danialtaherifar</div>
<div class="tg-footer">👁️ 639 · <a href="https://t.me/danialtaherifar/867" target="_blank">📅 18:41 · 08 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kkj3cXhH6o1qPnqfAbylqfC6OKFXyteIjLKmu9I2nCsR61WrfWmc7nKIDP5x32Tf0bwQPlnK-_jDaHIURTdyygl_8sL9UzeoA4JCQAKOBVE8jwTaVOotGHcDsapo-hFSOhBAy4JoZxarxLJAapI6pMud_L9Vx4i9j-287qxPczwwXST_O2J9sbtK-UEbu7tXtgq_TaE4LOFo-Sb5Ol3cWPGNj7QS2YmXzZRWUh4uiQoCxFp8686rTpy0-hlmsgsh86CCXaLIay_3k6LiLx42CnN6BOg5VvgcOWrQG0Ldm7Lunba8NR8Yaiq_bw3J_Fq-_M8k8rn9WF2xZk161gJ0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6F4ud44tizXFOBNx8Gk_b9c9SA_ozumD2OyPRMfoA_o48A1-7k0HKflTzds7exI8lc1sEBpDoXKJ1412LEiRS8RsBbmTpPgdO01JNIsXZOmAs3FemBv9ZCmcBFRvOsSXX_AkclxiQjmIGuQWGaqAGkJu2NfBAj4z44LMElCP5vXLQ9C-drPqsQ5rAUZXRBr448Kt-ZlFZ-zp45kUbUIivpnbPB-iCJAHvRnpbJBe6XeETYa-8zmMI1isb7IRB9K_Kgcb7eqLy_aZ-SC0HwcNKca0FE3tdKeb4_ochqTZDbY1DbAYd_qLnx4xYhUiEEiO3RuUHb2w9fv99oRj59Idg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
نوسانات شدید رتبه‌ بندی گوگل در چند روز گذشته !
📈
طبق گزارش‌های جدید، دوباره شاهد نوسانات چشمگیر رتبه‌بندی در نتایج جستجوی گوگل بودیم! این تغییرات درست بعد از نوسانات هفته‌ی قبل (۲۲ و ۲۳ آوریل) رخ داد و باعث شد خیلی از وب‌سایت‌ها افزایش یا افت چشمگیری در ترافیکشون تجربه کنن.
😵‍💫
🔍
ابزارهای مختلف مثل Semrush، MozCast و SimilarWeb هم این جهش ناگهانی رو تایید کردن. حتی بعضی از مدیران سایت‌ها از کاهش ۷۰٪ بازدیدکنندگانشون خبر دادن!
😬
👀
در حالی که به‌طور معمول هر هفته نوسانات کوچیکی داریم، این بار دو بار در یک هفته چنین شدت نوسانی خیلی غیرمعمول بوده.
💬
بعضی‌ها در انجمن‌های تخصصی گفتن که سایت‌هاشون از گوگل دیسکاور حذف شدن یا ترافیکشون افت وحشتناکی داشته؛ در مقابل بعضی‌ها هم رشد خوبی تجربه کردن.
📅
نکته مهم: هنوز خبری از آپدیت رسمی جدید گوگل در سال ۲۰۲۵ نیست (به غیر از آپدیت اصلی مارچ ۲۰۲۵).
📌
اگر سایتتون تغییرات عجیبی داشته، بدونید تنها نیستید! این نوسانات بخشی از بازی گوگله.
😉
@danialtaherifar</div>
<div class="tg-footer">👁️ 665 · <a href="https://t.me/danialtaherifar/865" target="_blank">📅 20:42 · 07 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-85SENZ6CQKrxq0qazjrL-jqRi5dx-OquOTUjzy3POsT_jlHBU92d7jVL7z3-hhkCt4YIPToyivjjMY5CrEqrKu48CtCrWlhlLTEjoOsEdocIq2p4Kq27yw21rCPRqH6pR_nrtDteZB2KI0HnSJZ9brkxms8jZ3KYaaI9j5GjWqt00FDC1SFU4oExb2j4dO1KdXNWnRluZxctgOiwtXDAt2d1wqXNtNXfx075Ev4GnXxMVtn6y7d0JaMjjdDHIkw3qiV583gPxNP6NREZOXVnKA6wVpojptSpKMdpFRtzXQF5S12I6FcPBkFtpNxAv4Wv0exCUhBmHBvnCcXjJESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گوگل در حال تست URL آبی در نتایج جستجو است!
🔍
گوگل اخیراً در حال آزمایش تغییرات ظاهری در نتایج جستجوی موبایل است؛ به طور خاص، رنگ URLها که معمولاً خاکستری یا سبز بودند، حالا به رنگ آبی تغییر کرده‌اند!
👀
بعضی کاربران متوجه شده‌اند که در برخی جستجوها، آدرس سایت (URL) به رنگ آبی و در کنار عنوان لینک نمایش داده می‌شود، چیزی که پیش از این رایج نبوده.
🧪
این تغییر همراه با جابجایی محل نمایش URL و نام سایت انجام شده:
در بعضی موارد، نام سایت در بالا و آدرس URL در پایین نمایش داده می‌شود.
در برخی موارد دیگر، URL درست زیر عنوان لینک می‌آید، و نام سایت حذف شده.
📱
این تست‌ها فقط در نسخه موبایل گوگل دیده شده و هنوز مشخص نیست آیا به صورت دائمی اعمال می‌شود یا خیر.
📢
هدف گوگل از این تغییرات احتمالا افزایش خوانایی نتایج و بهبود تجربه کاربری است. البته هنوز بازخورد رسمی یا اطلاعیه‌ای از سوی گوگل در این باره منتشر نشده.
@danialtaherifar</div>
<div class="tg-footer">👁️ 543 · <a href="https://t.me/danialtaherifar/864" target="_blank">📅 14:10 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GttGUYf4-y_li-a49g4Tx6nlnqPyRbuB3-6XC7mTWIj3hXMKwUFgux1yofwPVWDACKOMBUMTN1n9kKTY005DJwK_TYHYrWIPpIOMqyHe68f-joGncdRAjFpy93Fm2SXmhyeVTkRtH2DJYDcdGMtrJ3QD2e1ktbU4AzntV7OPT_di0qiHN5aqe0kz62QNSO6GHU85KywBtOB9wh-C3RnyihtStQkTggb4zd5PgIecr55a6i9DcASs0STmFrBjHwWe9B5uwNluUnqrBFnHbqiHv4LSStOVOWmRUC19ku7vwW1-XQ1D112glOetBjCXvHkdHF0zIBeHQM_3mZlEFH92Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
گوگل: استریم تصاویر برای سئو مناسب نیست!
🔍
جان مولر از گوگل توضیح داد که استفاده از تکنیک‌های استریم تصاویر (مثل قرار دادن عکس‌ها از طریق کد Embed به جای آپلود مستقیم) می‌تواند باعث شود تصاویرتون در نتایج جستجو ایندکس نشوند.
👨‍💻
در واقع وقتی تصاویر رو به این سبک بارگذاری می‌کنید (مثل ویدئوهای یوتیوب)، گوگل نمی‌تونه اون‌ها رو شناسایی کنه و در نتایج نمایش بده.
➖
نتیجه؟ کلی ترافیک احتمالی از دست میره!
🚫
📉
✅
اگر براتون مهمه تصاویرتون توی گوگل دیده بشه، بهتره روش سنتی آپلود مستقیم (JPEG, PNG و...) رو استفاده کنید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 542 · <a href="https://t.me/danialtaherifar/863" target="_blank">📅 09:57 · 06 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOY_Hz4Whzgp5pNARyFuaaOhDUP0aZRFQ3OY3P6oEwR3ZIIfa5oUWZbBtzLYtdl-0OlH98NKbrz3j4RwUe7ZJcA1DtA4as0ahlEg822hQmcDmKdIqoj01pUB-6s3RSd23G4ty0VirOMAWMUgVhJaGfCiS8ZZsK9w8ud2FN6PEA5bkF77y8lM75VO0okXjYHmdhHcbdlKHULJA-OllowYO-bZXX0mhPOQ2loYzAjFX5ma-2LFoONrTCjQ_RaX-LVM0OCpDYuQom7fgLkPhQ6dEVJ3fjZq6avX-0KXdjbWJRWYK8bY3AO69Q_3MdYQfejKHn5qlj2ynC-Nf0liHNMVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گوگل تأیید کرد: داده‌های ساختاریافته باعث بهبود رتبه سایت نمی‌شوند​
📢
در تازه‌ترین اظهارنظر، جان مولر از گوگل اعلام کرد که استفاده از داده‌های ساختاریافته (Structured Data) به تنهایی تأثیری در بهبود رتبه‌بندی سایت‌ها در نتایج جستجو ندارد.​
🧠
داده‌های ساختاریافته چه کاربردی دارند؟
داده‌های ساختاریافته به گوگل کمک می‌کنند تا محتوای صفحات را بهتر درک کند و در صورت تطابق با معیارهای خاص، امکان نمایش آن‌ها در قالب نتایج غنی (Rich Results) مانند کاروسل‌ها، بررسی‌ها و دستور پخت‌ها فراهم شود. ​
⚠️
نکات مهم:
استفاده از داده‌های ساختاریافته تضمینی برای نمایش در نتایج غنی نیست؛ فقط امکان آن را فراهم می‌کند.
استفاده از انواع غیرمستند داده‌های ساختاریافته تأثیری در بهینه‌سازی جستجو ندارد؛ زیرا گوگل تنها حدود ۳۰ نوع از آن‌ها را در نظر می‌گیرد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 667 · <a href="https://t.me/danialtaherifar/862" target="_blank">📅 18:41 · 02 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhawSOahP41z_LdMsePx2RIHvy5IYD5nE4IMHcJEQ80XLvFYZ0_NxOKGZ7rzAD28YAK5RC-7AmhJpPJdC3Aetanu8KORH5Hlan-snb96YujjHBbJz2rrwPfgzjxyMUqIJwcEtYTFSQsc_4hROkvmIEHCdY-RK_UB-NILqoqNIMygiSu7Mtpd2VUPmNly98OYkm-lsPq0b5lVFGRZZ3Abcc9xLCFNQGutGF5htrTAXGVbnKtcbkVtyLcD4DCpQPOKwNhrrfEuE89CxMVXwpNd3hBAo5yD6dzicsXsPqZXDjCLQGO3pvnOVS2XFuJeRCjfXQpkhUZfZHeCL_HRya1AEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔍
گوگل: فایل LLMs.txt به اندازه تگ متا کیورد بی‌فایده است!​
📄
جان مولر از گوگل اعلام کرد که فایل LLMs.txt، که به‌عنوان راهی برای هدایت خزنده‌های هوش مصنوعی پیشنهاد شده بود، در عمل بی‌فایده است و آن را با تگ متا کیورد مقایسه کرد که سال‌هاست توسط موتورهای جستجو نادیده گرفته می‌شود.​
🔍
فایل LLMs.txt چی بود اصلاً؟
یه سری از متخصصا و کمپانی‌ها پیشنهاد دادن که ما بیایم یه فایل به اسم llms.txt روی روت سایت بذاریم، تا مشخص کنیم چه مدل‌های زبانی (مثل OpenAI یا Anthropic) اجازه دارن محتوای ما رو بخونن یا نه. در واقع، یه چیزی مثل robots.txt ولی مخصوص هوش مصنوعی‌ !
🤖
📌
فایل LLMs.txt  به‌عنوان استانداردی برای کنترل دسترسی مدل‌های زبان بزرگ (LLMs) به محتوای وب پیشنهاد شده بود.​
📌
جان مولر اظهار داشت که این فایل توسط خزنده‌های هوش مصنوعی بررسی نمی‌شود و تأثیری در سئو یا کنترل محتوا ندارد.​
📌
تجربیات کاربران نیز نشان می‌دهد که پس از افزودن این فایل به سایت‌هایشان، هیچ تغییری در رفتار خزنده‌ها مشاهده نکرده‌اند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 681 · <a href="https://t.me/danialtaherifar/861" target="_blank">📅 22:51 · 01 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-poll">
<h4>📊 🎯دوست داری بیشتر در مورد کدوم موضوع توی کانال صحبت کنیم ؟👇</h4>
<ul>
<li>✓ 1️⃣کسب درآمد از گوگل ادسنس</li>
<li>✓ 2️⃣سئو آف‌ پیج (لینک‌ سازی، PR و...)</li>
<li>✓ 3️⃣سئو تکنیکال (Core Web Vitals، ایندکسینگ و ...)</li>
<li>✓ 4️⃣سئو آن‌ پیج (محتوا، تگ‌ ها، ساختار صفحات و ...)</li>
</ul>
</div>
<div class="tg-footer">👁️ 690 · <a href="https://t.me/danialtaherifar/860" target="_blank">📅 09:21 · 30 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🎯
اخطار
گوگل: محتوای تولید شده با هوش مصنوعی در پایین‌ ترین رتبه قرار میگیرد
🔍
📢
در یک به‌ روزرسانی مهم، گوگل اعلام کرده ارزیابان کیفیت موتور جستجویش (Quality Raters) موظف شده‌اند تا محتواهای تولیدشده توسط ابزارهای هوش مصنوعی را نیز بررسی کنند و اگر این محتواها کم‌ ارزش، بدون تلاش انسانی یا فاقد اصالت باشند، باید پایین‌ترین رتبه ممکن را دریافت کنند!
🧾
تعریف رسمی گوگل از هوش مصنوعی مولد
"هوش مصنوعی مولد (Generative AI) مدل‌هایی هستند که می‌توانند براساس داده‌هایی که آموزش دیده‌اند، محتوای جدیدی مانند متن، تصویر، موسیقی و کد تولید کنند."
گوگل تأکید کرده که این ابزارها می‌توانند مفید باشند، اما در صورت استفاده نادرست، به‌ راحتی منجر به تولید انبوه محتوای بی‌کیفیت می‌شوند.
🛑
تمرکز جدید گوگل روی محتواهای کم‌ ارزش
💥
گوگل ساختار بخش‌های مربوط به محتوای خودکار را بازنویسی کرده و به‌شکل جدی با محتواهایی که:
تنها برای جذب ترافیک تولید شده‌اند
فاقد ارزش افزوده برای کاربر هستند
فقط ترکیبی از اطلاعات تکراری‌اند
مقابله خواهد کرد.
📌
حتی اگر چنین محتواهایی توسط انسان بازنویسی شده باشند ولی نشانه‌ای از تلاش واقعی، تجربه تخصصی یا هدف مفید برای مخاطب در آن‌ها نباشد، باز هم امتیاز پایینی خواهند گرفت.
📍
جمع‌ بندی مهم برای تولیدکنندگان محتوا، سئوکارها و مدیران سایت‌ ها
🟢
استفاده از هوش مصنوعی ممنوع نیست!
🔴
اما اگر بدون دقت، بازبینی و بدون ارزش واقعی باشه، رتبه سایتتون در خطره!
🛠
پس: هوش مصنوعی + تجربه انسانی = محتوای موفق
💡
@danialtaherifar</div>
<div class="tg-footer">👁️ 873 · <a href="https://t.me/danialtaherifar/859" target="_blank">📅 09:34 · 29 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-857">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHgaln03IO09yDFTW3_GMobPUqQ2zCShM7CDyQJGHY1vfjhA2oBZRQ2r_BsUywfDtVswk7EpO47Y--4E8yJ2FWfW6foUjNlw_WvAUMzw_WcTVZL03Ro20k2sBp5V7WKNKTkk22R6I-tdi5gLkqNr8cDmkgMmeQs23v1OGErX9c0m2KYK3BCduRy7r8-V_hWbKDsVC_jqbjIufnFKccu6jAl3uh9A_GK5uASj8z8H4ryNrKh4HX_yryB0NNzC-50YoQeyEKY-_7fXIzt5KOCD1N3bJhSFinHCpLUaTm8XB4vMvwZYhkA_uzwjLrqj1MlBJpo8gynKkpceWbNCIDqFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7OusdCh2ofzqVOK3dsQAsr54eUo5TuXIjKBTcFS0onXW2u5cGBd0o29-rmva9Eni9UL8CU9kcDpA4AH40wu8ziZvhuvCTM-83ZGxA27HwUyNzyEOs7zRq-qcT-ConlZXb4pb8YJPfHTQIvug2kQxg0gpQE2L5PHkO5koEaW95OB8f_dTpVNH4Gql_vvEYPzcf3TpV-FuNcBpcEKSeUi4ZG2JORJ3tzYdzlfW-VTMNHwp0WcQgJylBygwttXZlnxNEon66EmNSh7vYB6GwNwIvhn1pTQ6Tp_MyG6V_Tg32yCPjCsBKgCRjJTqCTx-5by8m3YZOeBynr2pb3w0IweZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
دسترسی به داده‌های ساعتی در API سرچ کنسول گوگل برای ۱۰ روز گذشته فعال شد!​
گوگل به‌ تازگی قابلیت دریافت داده‌های ساعتی را در API سرچ کنسول خود فعال کرده است. این ویژگی به کاربران امکان می‌دهد تا اطلاعات عملکرد جستجوی وب‌سایت خود را با جزئیات ساعتی برای ۱۰ روز گذشته دریافت کنند.​
🆕
چه چیزی تغییر کرده است؟
پیش‌تر، گزارش‌های عملکرد در سرچ کنسول فقط داده‌های ساعتی ۲۴ ساعت گذشته را نمایش می‌دادند.​
اکنون، از طریق API، می‌توان داده‌های ساعتی را برای ۱۰ روز گذشته دریافت کرد.​
برای استفاده از این قابلیت، باید از بُعد جدیدی به نام HOUR در درخواست‌های API استفاده کرد.​
همچنین، مقدار جدیدی به نام HOURLY_ALL به پارامتر dataState اضافه شده است که نشان‌دهنده داده‌های ساعتی (که ممکن است ناقص باشند) است.​
💡
چرا این ویژگی مهم است؟
این قابلیت به مدیران وب‌سایت و متخصصان سئو امکان می‌دهد تا نوسانات ترافیک و عملکرد سایت خود را با دقت بیشتری بررسی کنند و در صورت بروز مشکلات، سریع‌تر واکنش نشان دهند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 810 · <a href="https://t.me/danialtaherifar/857" target="_blank">📅 11:20 · 23 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vk6H3BlVi46qc-wYFXXtJAyL0fEuld-HJuQGYNQu1wn967kRldQzUL8uVEdWMdpzp7omaDbzQArwP2NFyZI3YgPt4axEoqEpVv7RVfiY0b0RIVhfFa1xSMczgtnE8TEpPPktLsNWCJVmPIvP9d5e7RV3d7ujjXim4k344yHwqbCwgV1PRAyOEwbKa-CPAGKS1crkTil77CBxoeZ17mU2MQu7Ui1q2Wn69938uLuRSwjRStILwvnUst3L1bNrx3JDdZ7d2s8I5RHTsfJ3uzUXIHoSsadTk8BnFfWAaWmtOH1lfZrDD9bZ_pY8aK-DWcRVxL9HKcWu6qvemdI_VqNjVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIn4wCls8jXBpB5UGb2gMWjnrul91ykcmQ2X1CkKU6JLU4KWGnFdw5MtUfny5Y1DW_OejKExJ1sIpJdWEDADH-E-LXdgNTVy264l6Pm-Fbw-Ymzyx6ua4zh51qkfUoAwjbQnWuJbVNHqZU1_RAiR9RVxoEKipoae-8QgWje2YkzWBzSFBPfOZbBT-hWLYRdrUYhcB2zs827GWF1YRGw2E0-qYmoH0GQGQYqkVM39R8KHzipXKV7tZtl6cG7vLZv1zTU9Kxx_aPkpZWf2aFToVC5L96q1wRpQJ2DMZg68F4vCrhI0A2Ne8NNGVR5P4OopuPR2CdrFwBJzpHdHCYoAjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📉
نوسانات شدید رتبه‌ بندی گوگل در ۹ و ۱۰ آوریل ۲۰۲۵​
در روزهای ۹ و ۱۰ آوریل ۲۰۲۵، شاهد نوسانات قابل‌توجهی در رتبه‌بندی نتایج جستجوی گوگل بودیم. اگرچه گوگل هیچ به‌روزرسانی رسمی را اعلام نکرده است، اما ابزارهای مختلف بررسی آپدیت های الگوریتمی مانند SimilarWeb، Cognitive SEO، Accuranker، Wincher، Algoroo، Mangools، Sistrix، Data For SEO و SERPstat از وقوع یک به‌روزرسانی تأیید نشده خبر میدهند.​
🗣
واکنش جامعه سئو
برخی از متخصصان سئو از کاهش شدید ترافیک ارگانیک و افت رتبه‌ بندی را گزارش کرده‌اند. یکی از کاربران اشاره کرده است: "رتبه‌بندی‌ها به شدت کاهش یافته‌اند و ترافیک به طرز قابل‌توجهی افت کرده است."دیگری اظهار داشته: "به نظر می‌رسد به‌روزرسانی اصلی هنوز در حال اجراست؛ نباید به گفته‌های گوگل اعتماد کرد."​
با توجه به عدم تأیید رسمی از سوی گوگل، اما شواهد نشان می‌دهند که تغییراتی در الگوریتم رتبه‌بندی رخ داده است. برای مدیران وب‌سایت‌ها و متخصصان سئو، مهم است که عملکرد وب‌سایت‌های خود را در این دوره به‌دقت زیر نظر داشته باشند و در صورت لزوم، استراتژی‌های خود را بازنگری کنند.​
@danialtaherifar</div>
<div class="tg-footer">👁️ 802 · <a href="https://t.me/danialtaherifar/853" target="_blank">📅 14:56 · 22 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwAugtsplHx5BeSFk1B5qGfga0msNKm_fiU7n40DsKAmeEqUMoxeGdNW60UsXMaxAApFS09qCkXgq2acTQNXQURv0ff33Q5X0GmOSGSeOT9QqnrSjW1USlU7yAbfsEvMIQbt2MCrC6ifdeL-gO2JjYBLOB2uIwdZ392aoiaMor9U9H6IsxvT8U36ucBqm0qOVNx6_guQ_xnDX94l0qDBDmpzlDcOzwCgb_3POFjoogzGLj8FOBFUi3lIdGu_LZ3U35RoA05aM8vVqc-a3WugmK-ouaRdUrFgxaWEcdXMM0qmtdQOyKKK74ebpGKeoc1xvyVwHeP5RdRdbBxNtq8DwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🔍
گوگل دیسکاور به دسکتاپ می‌آید: تغییر بزرگ در صفحه اصلی گوگل
🔔
گوگل اعلام کرده است که پس از سال‌ها آزمایش، قصد دارد گوگل دیسکاور (Google Discover) را به نسخه دسکتاپ صفحه اصلی خود اضافه کند. این خبر در رویداد Search Central Live در مادرید به صورت رسمی اعلام شده است.
📱
گوگل دیسکاور یک فید محتوایی شخصی‌سازی‌شده است که تاکنون فقط در دستگاه‌های موبایل در دسترس بود و به کاربران کمک می‌کرد محتوای جدید و مرتبط با علایقشان را کشف کنند. حالا این تجربه به دسکتاپ هم می‌آید.
👀
در هفته گذشته، برخی کاربران در ایالات متحده مشاهده کردند که گوگل در حال آزمایش نمایش فید دیسکاور در صفحه اصلی دسکتاپ خود است. این نشان می‌دهد که گوگل به دنبال ارائه تجربه‌ای یکپارچه در تمام دستگاه‌هاست.
📊
این تغییر می‌تواند تأثیر قابل‌توجهی بر استراتژی‌های محتوایی ناشران و سایت‌ها داشته باشد، چون دیسکاور یکی از منابع مهم ترافیک برای آن‌ها شده است.
🎯
با این به‌روزرسانی، کاربران دسکتاپ هم می‌توانند به‌راحتی به محتوای تازه و شخصی‌سازی‌شده دسترسی داشته باشند و لذت تجربه‌ای مشابه موبایل را ببرند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 585 · <a href="https://t.me/danialtaherifar/852" target="_blank">📅 12:36 · 21 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📊
✨
چطور گزارش سئو بنویسیم که مدیر بازاریابی (CMO) عاشقش بشه؟
نوشتن گزارش سئو فقط نمایش اعداد نیست، بلکه باید داستانی بسازید که نشون بده سئو چطور به رشد کسب‌وکار کمک می‌کند. در ادامه به چند نکته مهم برای گزارش نویسی اشاره می‌کنم.
1.
🚀
نتایج تجاری، نه فقط داده‌ های فنی
مدیر ارشد بازاریابی (CMO) معمولاً با واژه‌هایی مثل "ترافیک"، "لینک‌ سازی"، یا "موقعیت کلمات کلیدی" ارتباط برقرار نمی‌کنن. اون‌ها می‌خوان بدونن این عددها چه تأثیری روی درآمد، برند و رشد کلی شرکت دارن.
✅
به جای این‌ که فقط بگید "افزایش ترافیک داشتیم"، بگید:
«ترافیک ارگانیک باعث افزایش ۲۵٪ سرنخ‌های فروش شد که منجر به ۱۵۰ هزار دلار درآمد شد.»
2.
💵
از ارزش مالی صحبت کن
باید نشون بدید که سئو به لحاظ مالی چقدر به صرفه‌ست. مثلاً:
🔸
هزینه جذب هر مشتری از طریق تبلیغات = ۱۲۰ دلار
🔸
هزینه جذب از طریق سئو = ۲۵ دلار
🔍
اینجوری نشون می‌دید سئو باعث صرفه‌جویی واقعی در هزینه‌ها میشه.
3.
📈
تمرکز روی محتوای برتر
به‌جای ارائه لیستی از تمام محتواها، فقط چند محتوای موفق رو هایلایت کنین. بگید:
«این مقاله وبلاگ ۳۵۰ سرنخ ایجاد کرد، به رتبه اول در گوگل رسید و در شبکه‌های اجتماعی ۵۰۰ بار به اشتراک گذاشته شد.»
4.
🧠
از زبان CMO استفاده کن، نه زبان سئوکارها
🔴
نگید: «Domain Authority این سایت ۷۰ بود.»
🟢
بگید: «ما از یک سایت معتبر لینک گرفتیم که باعث رشد رتبه ما در نتایج شد.»
زبان ساده، قابل فهم، و متمرکز بر نتیجه = موفقیت گزارش شما.
5.
📅
تغییرات را در بازه زمانی مقایسه‌ای نشون بده
مثلاً بگید:
«در مقایسه با ماه گذشته، ترافیک ارگانیک ۲۰٪ افزایش یافته و نرخ تبدیل از ۲٪ به ۳.۵٪ رسیده.»
نمودار و ویژوال هم خیلی کمک می‌کنه!
6.
📌
پیشنهادات عملی ارائه بده
فقط گزارش نده، بگو چه قدم‌هایی باید برداشته بشه. مثلاً:
✅
«اگر بودجه لینک‌سازی ۳۰٪ افزایش پیدا کنه، می‌تونیم تا سه‌ماه آینده ۵ رتبه در نتایج گوگل صعود کنیم.»
جمع‌ بندی
🎯
مدیران بازاریابی به دنبال تأثیر واقعی سئو روی رشد شرکت است. گزارش شما باید نشان دهد:
🔹
سئو چطور به درآمد کمک می‌کند
🔹
چه نتایج قابل اندازه‌گیری‌ای به دست آمده
🔹
قدم بعدی برای پیشرفت چیست
با این سبک گزارش‌نویسی، نه‌ تنها توجه CMO رو جلب می‌کنید، بلکه اعتبار تیم سئو رو هم بالا می‌برید
💪
@danialtaherifar</div>
<div class="tg-footer">👁️ 584 · <a href="https://t.me/danialtaherifar/851" target="_blank">📅 21:58 · 20 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTElXvulzKxetXWKDKsv1UYz4ChENvXewONIn4Q1UxG87sUZDtvOKJaLy6Yc_nTHtGbg6XwDZzSURShpZY4uoCqIKzClKkpVNrtA_-tSTcz0cj9YbTPAII949QJMA94vP_mCE2tIPpF28RZn4ifYK2EHUhJigzkWRllEkrC3B3iTYm7jktXeZVvajVAm8BOaZxwoxuu7zlkTJDOV3YSl2jNfZzsqJS7reRMqEdDzsnGY6hUdFoIgqAtvCOYzBmrQSoTWgeZhz0FL1MPj_PEblgc7KoqBZclyEovV0XLzP2NRGBroX2He5oJiZOqKL0fUi5SsVGx_JxJ8fqp_Y3QAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoCFoRxR5QxhoP7-rPNYDwvwXqt0aDwNdsx3j_lhCVeGEIk76kN39WCeJsP-ttoLbhD_BdAHs9rQ0rhrgR3vcG_ShHNNN7ucUwFU3RK_jzWALuyw8O9DrKYn2M3MbpgwMvxJRqpso4RfU98iLodoNlfIsDyLqcCf4t-y2NdBZgbv_39ju78128m9Ti_ev1QyRF7UqcHnxuJEPS903zrmZtX0pW3shJLrJH0O7_xR1gJ_ZNaow6VfSkF6Dm6gLaAuruPl8ToeVcV6DbTv6FmdS5O29dAZ6QFTZY29fxt00CSvjH1ZkLdG8mkufPIm_Z4XpfKqR4lQcbJj8zMOByoF1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
ویژگی جدید گوگل: نمایش موضوعات مرتبط در جستجو!
🔍
📚
✨
🔎
گوگل در حال آزمایش قابلیتی جدید به نام "Relevant Topics" یا "موضوعات مرتبط" است که در پایین برخی نتایج جستجو نمایش داده می‌شود. این قابلیت کاربران را تشویق می‌کند که فراتر از جستجوی اولیه‌شان، موضوعات مرتبط بیشتری را بررسی کنند.
📱
سچین پاتل (Sachin Patel) یکی از کاربران شبکه اجتماعی X (توییتر سابق)، اولین کسی بود که این ویژگی را مشاهده کرد و اسکرین‌شاتی از آن منتشر کرد.
🔍
وقتی او عبارت "SEO" را جستجو کرد، در پایین صفحه نتایج، بخشی با عنوان "Relevant Topics" ظاهر شد که لیستی از موضوعات مرتبط با سئو را نشان می‌داد.
📂
در کنار این لیست، گزینه‌ای با عنوان "Show more" یا "نمایش بیشتر" وجود داشت که با کلیک روی آن، موضوعات بیشتری نمایش داده می‌شد.
🛠
این بخش می‌تواند به سئوکاران و تولیدکنندگان محتوا کمک کند تا متوجه شوند گوگل چه موضوعاتی را به عنوان مکمل جستجوی اصلی در نظر می‌گیرد.
💬
فعلاً گوگل این قابلیت رو به‌صورت محدود و آزمایشی نمایش می‌ده و هنوز معلوم نیست چه زمانی به‌صورت رسمی برای همه کاربران فعال خواهد شد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 673 · <a href="https://t.me/danialtaherifar/849" target="_blank">📅 23:56 · 18 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔥
گوگل به‌ روزرسانی هسته‌ مارس ۲۰۲۵ را تکمیل کرد!
🚀
🔍
📢
پس از ۱۴ روز به‌روزرسانی Core Update مارس ۲۰۲۵ گوگل، چند روز پیش به پایان رسید! این به‌روزرسانی که در ۱۳ مارس ۲۰۲۵ آغاز شد و در ۲۷ مارس ۲۰۲۵ تکمیل گردید که تغییرات مهمی در الگوریتم‌های جستجو ایجاد کرده است. اگر شما هم در این مدت تغییراتی در ترافیک سایت خود مشاهده کرده‌اید، این به‌روزرسانی می‌تواند دلیل آن باشد.
🧐
🔄
🔎
جزئیات کامل به‌روزرسانی Core Update مارس ۲۰۲۵
🔹
تاریخ شروع: ۱۳ مارس ۲۰۲۵
🔹
تاریخ اتمام: ۲۷ مارس ۲۰۲۵
🔹
مدت زمان اجرا: ۱۴ روز
🔹
هدف: بهبود نمایش نتایج جستجو با تمرکز بر کیفیت محتوا
🔹
نوع: این به‌روزرسانی به‌عنوان جریمه عمل نمی‌کند، بلکه صفحات وب باکیفیت را ارتقا می‌دهد.
🔹
گستره: یک به‌روزرسانی جهانی است و بر تمام زبان‌ها و مناطق تأثیر می‌گذارد.
🔹
تأثیر: برخی از سایت‌ها تغییرات چشمگیری در رتبه‌بندی تجربه کرده‌اند.
📌
تأثیرات این به‌روزرسانی بر وب‌سایت‌ها
🔥
برندگان:
✅
سایت‌هایی که محتوای باکیفیت و اورجینال دارند، شاهد بهبود رتبه‌بندی شدند.
✅
وب‌سایت‌هایی که تجربه کاربری (UX) بهتری ارائه می‌دهند، افزایش ترافیک داشتند.
✅
سایت‌هایی که از محتوای تولیدشده توسط کاربران (UGC) به‌درستی استفاده می‌کنند، امتیاز بهتری گرفتند.
⚠️
بازندگان:
❌
سایت‌هایی که محتوای کم‌کیفیت یا کپی‌شده دارند، کاهش رتبه داشته‌اند.
❗️
📉
❌
صفحات دارای تبلیغات بیش‌ازحد یا تجربه کاربری ضعیف، تأثیر منفی دیده‌اند.
❌
وب‌سایت‌هایی که از روش‌های قدیمی سئو (مانند تکرار بیش‌ازحد کلمات کلیدی) استفاده می‌کردند، ضربه خورده‌اند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 901 · <a href="https://t.me/danialtaherifar/848" target="_blank">📅 17:31 · 12 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔍
تحول به سمت جستجوهای بدون کلیک
📉
بر اساس تحقیقات اخیر، بیش از ۶۰٪ از جستجوها بدون کلیک خاتمه می‌یابند. این یعنی کاربران دیگر نیازی به ورود به وب‌سایت‌ها برای یافتن اطلاعات ندارند، زیرا پاسخ‌های خود را از بخش‌های مختلف SERP مانند (Featured Snippets)، (Knowledge Panels) و (Instant Answers) دریافت می‌کنند. این موضوع باعث کاهش چشمگیر ترافیک ورودی به سایت‌ها شده است.
🔎
چگونه گوگل ترافیک را درون خود نگه می‌دارد ؟
گوگل با توسعه قابلیت‌هایی مانند:
✅
نمایش پاسخ‌های مستقیم در نتایج جستجو
📌
✅
پیشنهاد‌ های Google Suggest
⌨️
✅
باکس‌ های نالج گراف (Knowledge Boxes)
📚
✅
نمایش اطلاعات کسب‌وکارها در گوگل مپ
📍
✅
و حتی قابلیت خرید مستقیم در نتایج جستجو
🛒
در تلاش است تا کاربران را درون پلتفرم خود نگه دارد و از خروج آن‌ها به وب‌سایت‌های دیگر جلوگیری کند.
🚀
استراتژی‌های مقابله با کاهش کلیک‌ها
1️⃣
بهینه‌سازی برای (Featured Snippets)
با ارائه پاسخ‌های دقیق، خلاصه و ساختاریافته به سوالات کاربران، می‌توانید شانس نمایش سایت خود را در باکس‌های ویژه گوگل افزایش دهید.
🔝
2️⃣
تمرکز بر برندینگ و ایجاد آگاهی از برند
اگر کاربران شما را به عنوان یک مرجع قابل اعتماد بشناسند، مستقیماً به سایت شما مراجعه خواهند کرد. حضور پررنگ در شبکه‌های اجتماعی و تولید محتوای ارزشمند می‌تواند به شما کمک کند.
💡
3️⃣
استفاده از داده‌های ساختاریافته (Structured Data)
با اضافه کردن اسکیما مارکاپ (Schema Markup) به صفحات خود، گوگل را قادر می‌سازید تا اطلاعات وب‌سایت شما را بهتر درک کند و در نتایج جستجو نمایش دهد.
🛠
4️⃣
ایجاد صفحات تعاملی و کاربردی
اگر کاربران پس از ورود به سایت شما تعامل بیشتری داشته باشند (مانند مشاهده ویدیو، خواندن محتوای کامل)، گوگل این را یک سیگنال مثبت در نظر گرفته و سایت شما را در رتبه‌بندی بهتر قرار خواهد داد.
📈
5️⃣
تنوع‌بخشی به منابع ترافیک
به جای تمرکز صرف بر ترافیک ارگانیک، از روش‌های دیگر مانند بازاریابی ایمیلی، تبلیغات پولی، فعالیت در شبکه‌های اجتماعی و استراتژی‌های محتوایی ویدئویی استفاده کنید.
🎯
🌟
با پذیرش این تغییرات و تطبیق با روندهای جدید، کسب‌وکارها می‌توانند در دنیای جستجوهای بدون کلیک نیز موفق باشند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/danialtaherifar/847" target="_blank">📅 18:03 · 06 Farvardin 1404</a></div>
</div>

<div class="tg-post" id="msg-846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔹
🚀
گوگل قوانین جدیدی برای استراکچر دیتا و بازگشت کالا اعلام کرد!
🔍
گوگل اخیراً الزامات داده‌های ساختاریافته (Structured Data) برای سیاست‌های بازگشت کالا را بروزرسانی کرده است. این تغییرات بر نحوه نمایش اطلاعات در نتایج جستجو تأثیر می‌گذارد و فروشگاه‌های آنلاین باید سریعاً اقدام کنند!
🛒
📊
💡
چه چیزهایی تغییر کرده است؟
✅
شفافیت بیشتر در نمایش اطلاعات بازگشت کالا
🔄
🔍
✅
ضرورت استفاده از استراکچر دیتا برای سیاست‌های بازگشت
📌
📊
✅
نیاز به مشخص کردن مدت زمان بازگشت، شرایط و هزینه‌ها
⏳
💰
نمونه به‌ روز شده از JSON-LD برای داده‌های ساختاریافته سیاست بازگشت کالا که دقیقاً مطابق با مشخصات جدید گوگل است:
"hasMerchantReturnPolicy": {
"
@type
": "MerchantReturnPolicy",
"applicableCountry": "CH",
"returnPolicyCountry": "CH",
"returnPolicyCategory": "
https://schema.org/MerchantReturnFiniteReturnWindow
",
"merchantReturnDays": 30,
"returnMethod": "
https://schema.org/ReturnByMail
",
"returnFees": "
https://schema.org/FreeReturn
"
}
🔹
بخش merchantReturnDays: حداکثر تعداد روزهایی که مشتری می‌تواند محصول را بازگرداند (در اینجا 30 روز).
🔹
بخش returnFees: مشخص می‌کند که آیا بازگشت کالا رایگان است یا هزینه دارد (در اینجا Free یعنی رایگان).
🔹
بخش returnMethod: نحوه بازگشت کالا (در اینجا Mail یعنی ارسال پستی، می‌تواند "InStore" هم باشد).
🔹
بخش returnShippingFeesAmount: هزینه ارسال برای بازگشت کالا (0 دلار یعنی رایگان).
📢
این استراکچر دیتا باعث می‌شود گوگل بتواند سیاست‌های بازگشت کالا را به‌درستی در نتایج جستجو نمایش دهد و تجربه بهتری برای کاربران ایجاد شود.
@danialtaherifar</div>
<div class="tg-footer">👁️ 971 · <a href="https://t.me/danialtaherifar/846" target="_blank">📅 10:28 · 25 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfUmUejUfML2Lke6B52hnGq3hFadK1_tBmX8Vml9Anfov7lktPxhfZ6hcJl9JLcQ4M5MotWo1JZCmGBQ2iYFiKrkS2m42eXhrXYOcqDMLOx3fH06d70jcl85z1f5AKWXy4LKtyQFayOuOP8BRboj0bTc2h6MMwcV5wfWtku1pzMYkzhOTMlBQOq5utCgUO7ycjlTC8b1oeYNGx3zNw_B3yh6kS-tXmgDzMjApwowWjjunyIrmbbcs6y6BQv4ahd5P1QCZBxPwRUiDu9ST7CEOfF4yalUfUmnPSrnBodEm2_1JsIGv-eR3nn6mIrFqwxpTKKlOr0IvoVF91rjkPKBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل آغاز آپدیت هسته‌ در مارس 2025 را اعلام کرد
📅
گوگل از چند روز گذشته فرآیند انتشار به‌روزرسانی جدید الگوریتم هسته‌ای خود را در ماه مارس 2025 آغاز کرده است. این تغییر مهم به‌تدریج در حال پیاده‌سازی است و انتظار می‌رود طی چند هفته آینده به‌طور کامل اعمال شود.
🎯
هدف از این به‌روزرسانی چیست؟
⚖️
گوگل اعلام کرده که این به‌روزرسانی با هدف بهبود تجربه کاربران و ارتقای جایگاه محتوای باکیفیت طراحی شده است. به این معنا که وب‌سایت‌هایی با محتوای ارزشمند، مرتبط و کاربرپسند از مزایای بیشتری برخوردار خواهند شد. در مقابل، سایت‌هایی با محتوای کم‌ارزش یا پر از کلمات کلیدی نامرتبط ممکن است با چالش‌هایی روبه‌رو شوند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 716 · <a href="https://t.me/danialtaherifar/845" target="_blank">📅 08:36 · 24 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-843">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO8LIW2ymSa-YH-ZxSaLG47CRvHK5MznaYjt2u2Ar2PaEpcNrvePvPmrHhKI8xIk9GVLTrrtUjphUy3WzDmdB3ZXKYkD84aA4XxkdqOhIu6MbgosA2pTYz7ded97U_0NxPil0XOL37BAaCykBtefN6j3YONXCJM1u8OrPjGrIiAjZiFP6YNrVv1ri84qgBN4WRvWGMU9v6BIS5zAc7ThWM1WEgi8Rc662YgaxQwv9INMJ8BC9t1QK5KAmWCqbp4x02YJP23iFcg6aW7NifoJIczjpJPZUVwtiAknly2qRpPyefDlrD5KaSHLs--sxzLQ2Kf9SZX-8Ar0xMzXSLRHTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
🚫
ریدایرکت کردن صفحات 404 به صفحه اصلی کار درستی نیست!
📢
مارتین اسپلیت
، یکی از کارشناسان گوگل، به تازگی در مورد یه اشتباه رایج سئو صحبت کرده: ریدایرکت کردن صفحاتی که خطای 404 (صفحه پیدا نشد) دارن به صفحه اصلی سایت.
💬
به گفته‌ی اسپلیت، این کار نه‌ تنها کمکی به تجربه کاربری نمی‌کنه، بلکه می‌تونه برای سئو هم دردسرساز بشه! وقتی یه صفحه خطای 404 داره, بهتره به جای ریدایرکت به صفحه اصلی، یه صفحه اختصاصی 404 طراحی کنید، که کاربر رو راهنمایی کنه یا اون رو به یه صفحه مرتبط بفرستید.
❓
چرا این موضوع مهمه ؟ چون گوگل می‌خواد بفهمه محتوای سایتتون چیه و
ریدایرکت بی‌منطق
می‌تونه سیگنال‌های اشتباه به موتور جستجو بفرسته. این کار ممکنه باعث بشه صفحات ارزشمند شما ایندکس نشن و سایتتون دچار مشکل بشه!
🚧
@danialtaherifar</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/danialtaherifar/843" target="_blank">📅 13:33 · 19 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-842">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzCzEFDE_hmJVAyvaARfKm9gyJFdGhOw0WIWPs_FQGyo2QqhjWYUvYT61kljJJidpbizd-LZXV1b61POn2aoi8TLNaIo_vFrMWrkjMP-DROUO6gHzy23d7TdPSTvJE4f13QRIk3pKN4N3qeej-57hq0gW71tW0aKXzT55yIQ984IP53JK9fy4mhFJPRnhq6aSF5uYEmqnzKQXqxAqALUmUjb3s20tRnty2gafAOQlmClctte3jgDPv349Mg5QsRf53i943ys2jmE6mdne663DrslN07Qd5vJGEG08vNVUAdmGEYTyja28IL7FRruzRIizGbpEPsMJTBmRPozmjafOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
هوش مصنوعی AI Overviews گوگل، دشمن جدید سئوکاران؟!
🔍
تحقیقات اخیر نشان می‌دهد که با افزایش استفاده گوگل از
هوش مصنوعی (AI Overviews)
در نتایج جستجو،
نرخ کلیک (CTR)
وبسایت ها به‌ طور قابل‌ توجهی کاهش یافته است. این تغییرات می‌توانند تأثیرات مهمی بر استراتژی‌های سئو و بازاریابی دیجیتال داشته باشند.
🔹
نتیجه؟ کاهش ترافیک سایت‌ها و چالش جدید برای سئوکاران!
🚨
💡
چگونه در این رقابت حضور داشته باشیم ؟
✅
محتوای ارزشمند و تعاملی تولید کنید
✍️
🔥
✅
بهینه‌ سازی برای AI Overviews را جدی بگیرید
⚙️
🤖
✅
از داده‌های ساختاریافته (Schema) استفاده کنید
📊
🔗
🌐
با توجه به تغییرات اخیر در نتایج جستجوی گوگل و افزایش استفاده از هوش مصنوعی، ضروری است که کسب‌ و کارها و وب‌ سایت‌ها استراتژی‌ های خود را متناسب با این تغییرات تنظیم کرده و به
بهبود تجربه کاربری
و
ارائه محتوای با کیفیت
تمرکز کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 769 · <a href="https://t.me/danialtaherifar/842" target="_blank">📅 12:40 · 17 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-840">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMhXyvXz4Qa6FeyoBODCwuzfPmKQJVNaE52KJRxafrROZmxOxgTv8VTmd4Sqk3_5HnMvx7HBQWxnqr-TXbTGlXp0QgXPAtF00TStSpnIQJTOJB72_23FRG0fQGCN4d7OpQOxbp_LnDg5m1si0M3h-hCROSSvCU58Cfo0irqbh-8N_PU-amOlyRKoDr5dUJqEuQW7YHidTqVJ3SWIyhBX1KfQFWZgxEa2UYPEk1e6O84xZvfRD-i0UrTv8c2wdvLqdUj18hxpvV6TkiI9p0LOsks2Dnq_baUPhWxlR0GLWurr5YhNCtmzGkCNtyQYoebF5Fk5E_6tR1mGbcOZ6fEQrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7zy-HuUsIi3mhvOUrjDP4ds9WdwwRd9IhxYPlZ5prbtEbtnH2gkQCVjQTqGGqKNiyk-xPZude_THQHYHQ_HYJG69POVZA-vHUDNEucxB4nz35EFnIpE2xh_HqTuQUkjBYbAz7I84jAhmKB3sl82RnMRCdVSXCrI6tOB5sAk4mGPU1LN4KM2aEBR-5j3ZqmaKu6gcQU5tm7ZxiG4RNXtaQpLmEN9JxoKLy6NvDGc2SdziHC1kOyaVr44tMb3IJvEg6cuXyAJnJ_V9JUtY3njeR3UBKdD1HWNz_LDpJfwxVDsuU8SEPZ61x2v_HPxfvu-cKbJIBXnHwzF252Ghop3Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎯
گوگل مستندات تگ متا ربات‌ها را برای اضافه کردن "AI Mode" به‌روزرسانی کرد!
🔹
گوگل اخیراً مستندات مربوط به تگ متا ربات‌ها را به‌روزرسانی کرده و حالت جدیدی به نام "AI Mode" را معرفی کرده است! این ویژگی با بهره‌گیری از هوش مصنوعی، تجربه جستجو را پیشرفته‌تر و دقیق‌تر از قبل می‌کند.
✨
این قابلیت از مدل هوش مصنوعی Gemini 2.0 استفاده می‌کند و توانایی ارائه پاسخ‌های تحلیلی، دقیق و چندوجهی را دارد.
📌
کاربران از طریق یک تب اختصاصی در صفحه جستجو به این حالت دسترسی دارند و می‌توانند اطلاعات گسترده‌تری دریافت کنند.
🔍
چه کسانی می‌توانند از AI Mode استفاده کنند؟
🔹
این ویژگی فعلاً برای مشترکین Google One AI Premium و برخی کاربران منتخب در آمریکا از طریق Search Labs فعال شده است که از این قابلیت برای ارائه اطلاعات خرید نیز استفاده می‌کند تا تجربه کاربران را بهبود بخشد.
🌐
https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag#directives
@danialtaherifar</div>
<div class="tg-footer">👁️ 609 · <a href="https://t.me/danialtaherifar/840" target="_blank">📅 15:37 · 16 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-839">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIWzyuwBCmfFcnVmX9KzgsE8uUbv44t66QzvKuxEIMv1OhMk5P2t8mb_VnvrpttlliYRGyW3Cb_NXcK5fAdK0Oo8xyVJAk0L3tL9Chol7Nx_oT2XPns2YWalKQ-pdLagiPyPquKrTNOfE-oAwr0K_PWDTPCJijjVfl3hl8fzG-HYx68hLmXoyNwuiNV3N3Rmi19dEsGQ2jZrOQDzGyxcZ2-Uh6PNAyGK4CKaBKEN3Zim9a_tDkiCoUEBzjbsgoReMf9wfahKWNOQ6UmVg9CoO4cPxz-ZSQQ5oC3gUI8dCaKr-MpC8lx3Kjzj77vJ_LWgqhvH5rDz9WXJdY7sOWeGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل اکنون سالانه بیش از ۵ تریلیون جستجو را پردازش می‌کند!
🚀
🔍
افزایش چشمگیر جستجوها:
بر اساس داده‌های داخلی گوگل تا ژانویه ۲۰۲۵، این شرکت اکنون بیش از ۵ تریلیون جستجو در سال را مدیریت می‌کند.
📈
رشد قابل‌ توجه:
در سال ۲۰۱۶، گوگل اعلام کرد که سالانه ۲ تریلیون جستجو را پردازش می‌کند. این افزایش به بیش از ۵ تریلیون نشان‌دهنده رشد مداوم و قابل‌توجه در حجم جستجوهای گوگل است.
🤖
نقش هوش مصنوعی:
گوگل با استفاده از فناوری‌های هوش مصنوعی، تجربه‌های جستجوی غنی و چندرسانه‌ای مانند AI Overviews، Circle to Search و Lens را ارائه داده است. این ابزارها به کاربران امکان می‌دهند تا به‌صورت طبیعی‌تر و دقیق‌تر آنچه را که می‌خواهند بیان کنند.
🛍
افزایش جستجوهای تجاری:
با معرفی AI Overviews، حجم جستجوهای تجاری افزایش یافته است که فرصت‌های بیشتری برای کسب‌وکارها فراهم می‌کند تا با مصرف‌کنندگان ارتباط برقرار کنند.
این دستاورد گوگل نشان‌ دهنده تعهد مداوم این شرکت به
بهبود تجربه جستجوی کاربران
و
پاسخگویی به نیازهای متغیر جامعه دیجیتال
است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 621 · <a href="https://t.me/danialtaherifar/839" target="_blank">📅 18:57 · 15 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZrgbwo4NGLVBmiNa-zXhfoUCO5lRMo8zjOJXGUNsf4r8PzYyp1Lg1iCWauYLseJmdsj_tbEzA1im5Ywg6fldGpP2E3jr62dZzaNgdczBnfoZkYTYgm_ZIuP43L0hiA6dV-uyFv0Vkxwkl3wYb85Y9cWbYFBZvEU653swI1dMK2pAkwqYC4C3ApnDo8l_HMyn8UJn6Iy-0FWJRn6t2CoQQ_uoz4jJbyktOhDZz_2nJjaZmytkSuzVVLLXgy3IowV6rYdkPFi-LftdW6cZdZLCY8sIcQaFyHrnQ5SqZj0d4xj3FFQpdd4aywjZ14XWqXLVUsk2gg9X9uBZYqcVU2lNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل در برابر محتوای کم‌ کیفیت اما خوش ظاهر سختگیر می‌شود!
🚨
🔎
بسیاری از سایت‌ها با استفاده از
محتوای تولید شده توسط هوش مصنوعی
،
بازنویسی‌ های سطحی
و
اطلاعات عمومی
سعی می‌کنند رتبه خوبی در گوگل بگیرند. این نوع محتوا معمولاً ظاهری حرفه‌ای دارد اما در عمق خود،
چیزی جدیدی به کاربر اضافه
نمی‌کند. گوگل با استفاده از الگوریتم‌های پیشرفته، این محتوا را شناسایی و رتبه آن را کاهش می‌دهد.
📉
⚠️
محتوای ضعیف چه ویژگی‌ هایی دارد ؟
❌
استفاده از جملات کلی و بدون اطلاعات دقیق
❌
تکرار مطالب عمومی که در سایت‌های دیگر وجود دارد
❌
عدم ارائه پاسخ‌های عمیق و مفید به سوالات کاربران
❌
استفاده بیش از حد از هوش مصنوعی بدون ویرایش انسانی
❌
هدف‌ گذاری فقط روی کلمات کلیدی بدون در نظر گرفتن نیاز کاربر
✅
اگر می‌خواهید در رتبه‌های برتر گوگل بمانید، محتوای شما باید
ارزشمند
،
کاربردی
و
واقعی
باشد، نه فقط
پر زرق‌ و برق
!
✍️
📚
@danialtaherifar</div>
<div class="tg-footer">👁️ 662 · <a href="https://t.me/danialtaherifar/837" target="_blank">📅 09:11 · 14 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📢
تحول بزرگ در سئو: حرکت به‌ سوی سئوی معنایی و وکتورها !
🚀
🔍
🔥
گوگل دیگر فقط به کلمات کلیدی توجه نمی‌کند! با پیشرفت سئوی معنایی، موتورهای جستجو از وکتورها برای درک ارتباط مفهومی بین کلمات استفاده می‌کنند.
🧠
🔎
وکتورها: راز درک هوش مصنوعی
🤖
وکتورها ابزاری ریاضی هستند که هوش مصنوعی برای درک و سازمان‌ دهی اطلاعات فراتر از متن ساده استفاده می‌کند. به جای تکیه بر تطابق دقیق کلمات کلیدی، موتورهای جستجو اکنون از vector embeddings استفاده می‌کنند که کلمات، عبارات و حتی تصاویر را بر اساس معنای آن‌ها و روابط‌شان در فضایی چندبعدی ترسیم می‌کند.
🌐
🔗
🎯
به این صورت فکر کنید: اگر یک تصویر ارزش هزار کلمه را داشته باشد، وکتورها نحوه ترجمه این کلمات به الگوهایی هستند که هوش مصنوعی می‌تواند آن‌ ها را تحلیل کند.
🖼
➡️
🧠
💡
برای متخصصان سئو، این‌گونه می‌توان تشبیه کرد: وکتورها برای هوش مصنوعی همانند داده‌های ساختاریافته برای موتورهای جستجو هستند، روشی برای ارائه زمینه و معنای عمیق‌ تر.
📊
🌐
چگونه وکتورها جستجو را تغییر می‌دهند؟
🔄
با استفاده از
semantic relationships
,
embeddings
و
neural networks
جستجوی مبتنی بر وکتور به هوش مصنوعی این امکان را می‌دهد که هدف کاربر را به جای صرفاً کلمات کلیدی تفسیر کند.
🧠
💬
🔑
به این معناست که موتورهای جستجو می‌توانند نتایج مرتبط را حتی زمانی که یک کوئری شامل کلمات دقیق از یک صفحه وب نباشد، نمایش دهند. برای مثال، جستجو "کدام لپ‌تاپ برای بازی بهترین است؟" ممکن است نتایجی را نشان دهد که برای "لپ‌تاپ‌های با عملکرد بالا" بهینه شده‌اند، زیرا هوش مصنوعی ارتباط مفهومی این کلمات را درک می‌کند.
💻
🎮
📸
وکتورها چگونه به هوش مصنوعی کمک می‌کنند که محتواهای غیرمتنی را تفسیر کند؟
عبارات عامیانه (مثلاً "دندان روی جگر گذاشتن" در مقابل "تصمیم سخت گرفتن")
💬
تصاویر و محتوای بصری
🖼
ویدئوهای کوتاه و وبینارها
🎥
پرسش‌های جستجوی صوتی و زبان محاوره‌ای
🎙
📌
خلاصه: وکتورها در حال انقلاب در نحوه درک و رتبه‌بندی محتوا توسط موتورهای جستجو هستند و نتایج جستجو را مرتبط‌تر می‌سازند، حتی زمانی که کلمات دقیقاً تطابق ندارند!
🔍
✨
آیا برای این تغییرات در نتایج جستجو آماده‌ هستید؟
🤔
👇
@danialtaherifar</div>
<div class="tg-footer">👁️ 610 · <a href="https://t.me/danialtaherifar/836" target="_blank">📅 11:49 · 13 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔍
اهمیت Customer-Centric:  راز موفقیت در سئو
💡
✨
در Customer-Centric SEO به جای اینکه صرفاً بر الگوریتم‌ های موتور جستجو تمرکز کنیم، تلاش می‌کنیم
نیازها
و
انتظارات واقعی کاربران
را در اولویت قرار دهیم. با بهینه‌ سازی تجربه کاربری، ارائه محتوای ارزشمند و تحلیل مداوم رفتار مشتریان، می‌توان
ترافیک پایدارتر
،
تعامل بالاتر
و
نرخ تبدیل بهتری
کسب کرد. در ادامه، مهم ترین رویکرد های تجربه سئوی مشتری‌ محور رو بررسی می‌کنیم:
1️⃣
تحقیق عمیق درباره کاربران و سفر مشتری
🎯
✅
درک نیازها، مشکلات و سوالات کاربران قبل از تولید محتوا
✅
بررسی پرسوناهای مشتری و تحلیل داده‌های جستجو برای یافتن موضوعات پرتقاضا
✅
استفاده از ابزارهایی مانند Google Analytics، Google Search Console و ابزارهای سئو مانند SEMrush و Ahrefs برای تحلیل رفتار کاربران
2️⃣
ایجاد محتوای ارزشمند، کاربردی و مرتبط
📝
✅
تولید محتوا با تمرکز بر نیازهای واقعی کاربران نه صرفاً برای رتبه گرفتن
✅
استفاده از فرمت‌های مختلف محتوا مثل متن، ویدیو، اینفوگرافیک، پادکست و محتوای تعاملی
✅
ارائه راهنماهای جامع، پاسخ‌های دقیق به سوالات کاربران و محتوای همیشه سبز
3️⃣
بهینه‌ سازی تجربه کاربری (UX) و رابط کاربری (UI)
🖥
✅
ناوبری ساده و کاربرپسند برای یافتن سریع اطلاعات موردنیاز
✅
دسته‌بندی شفاف محتوا و استفاده از CTA (دکمه‌های دعوت به اقدام) بهینه‌شده
✅
ایجاد تجربه‌ای یکپارچه در همه دستگاه‌ها و توجه به دسترس‌پذیری (Accessibility)
4️⃣
بهبود سرعت سایت و بهینه‌سازی عملکرد فنی
⚡️
✅
افزایش سرعت بارگذاری صفحات برای کاهش نرخ پرش (Bounce Rate)
✅
استفاده از فرمت‌های سبک‌تر تصاویر (WebP) و فشرده‌سازی کدهای CSS و JavaScript
✅
بهینه‌سازی کش سایت و استفاده از شبکه تحویل محتوا (CDN)
5️⃣
تمرکز بر بهینه‌سازی موبایل (Mobile-First SEO)
📱
✅
طراحی سایت به‌صورت Mobile-First با رعایت اصول ریسپانسیو
✅
حذف عناصر اضافی که باعث کاهش سرعت در موبایل می‌شوند
✅
تست سایت در ابزار Google Mobile-Friendly Test
6️⃣
اعتمادسازی و افزایش اعتبار سایت (E-E-A-T)
🔒
✅
نمایش نظرات مشتریان، گواهینامه‌ ها و نشان‌ های امنیتی
✅
ایجاد صفحات درباره ما و تماس با ما برای افزایش اعتبار
✅
استفاده از لینک‌ سازی داخلی و خارجی معتبر برای تقویت سیگنال‌های E-E-A-T (تجربه، تخصص، اعتبار و اعتماد)
7️⃣
سازماندهی و ساده‌ سازی محتوا برای اسکن سریع
🔍
✅
استفاده از تیترهای مناسب (H1، H2، H3) برای ساختاردهی بهتر محتوا
✅
استفاده از لیست‌های شماره‌دار و بولت پوینت‌ها برای خوانایی بهتر
✅
ایجاد بخش FAQ (سوالات متداول) و خلاصه‌های کلیدی برای کاربرانی که سریع اسکن می‌کنند
8️⃣
بهینه‌ سازی نرخ تبدیل (CRO) برای CTAها
🎯
✅
طراحی دکمه‌های دعوت به اقدام (CTA) واضح، برجسته و ترغیب‌کننده
✅
تست A/B برای بهینه‌سازی نرخ تبدیل و بهبود مسیر کاربر
✅
ایجاد صفحات فرود (Landing Pages) جذاب و کاربردی
9️⃣
استفاده از داده‌ها و تحلیل مستمر برای بهبود عملکرد
📊
✅
بررسی رفتار کاربران با ابزارهای تحلیلی و شناسایی نقاط ضعف
✅
آزمایش و بهینه‌ سازی مداوم بر اساس داده‌ های به‌دست‌آمده
🔟
استفاده از مدیا و گرافیک‌ های جذاب برای تعامل بیشتر
🎨
✅
ترکیب متن با تصاویر، ویدیوها، اینفوگرافیک‌ها و نمودارها
✅
استفاده از تصاویر سبک و جذاب برای بهبود تجربه کاربری
✅
بهینه‌ سازی ویدیو ها با قابلیت نمایش سریع و کم‌حجم
⚡️
با اجرای این رویکرد، نه‌ تنها سایت شما برای کاربران مفیدتر خواهد شد، بلکه گوگل نیز به دلیل ارائه تجربه بهتر به کاربران، وبسایت شما را در رتبه‌ های بالاتر نمایش می‌دهد.
🚀
@danialtaherifar</div>
<div class="tg-footer">👁️ 670 · <a href="https://t.me/danialtaherifar/835" target="_blank">📅 10:49 · 12 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">📢
هشدار گوگل درباره خطای "Noindex Detected" در سرچ کنسول!
🔍
گوگل اخیراً درباره خطای "Noindex Detected" در گزارش پوشش ایندکس سرچ کنسول توضیحاتی ارائه کرده است. این خطا نشان می‌دهد که گوگل یک صفحه را شناسایی کرده اما به دلیل وجود تگ noindex، آن را ایندکس نکرده است.
⚠️
چرا این اتفاق می‌افتد؟
🔹
اگر این تگ عمداً برای جلوگیری از ایندکس شدن صفحات خاص اعمال شده باشد، جای نگرانی نیست.
🔹
اما اگر ناخواسته اضافه شده باشد، ممکن است باعث حذف صفحات مهم از نتایج جستجو شود.
✅
راه‌حل‌ها برای رفع این مشکل:
1️⃣
بررسی سرچ کنسول: از ابزار URL Inspection استفاده کنید تا ببینید آیا صفحه موردنظر دارای تگ noindex است یا خیر.
2️⃣
حذف تگ noindex: اگر صفحه باید ایندکس شود، تگ noindex را از بخش هد (head) HTML حذف کنید.
3️⃣
بررسی فایل robots.txt: از آنجایی که گوگل دیگر از دستور noindex در فایل robots.txt پشتیبانی نمی‌کند، نباید از این روش برای جلوگیری از ایندکس استفاده کنید.
4️⃣
کنترل متا تگ‌ها و هدرهای HTTP: برخی مواقع، دستور noindex در هدرهای HTTP تنظیم شده است. مطمئن شوید که این تگ به‌طور تصادفی در تنظیمات سرور اعمال نشده باشد.
5️⃣
بررسی دستورات جاوااسکریپت: برخی اسکریپت‌های جاوااسکریپت می‌توانند به‌طور دینامیکی تگ noindex را به صفحه اضافه کنند. بررسی کنید که کدهای جاوااسکریپت باعث این مشکل نشده باشند.
6️⃣
بررسی تنظیمات سیستم مدیریت محتوا (CMS): برخی CMSها مانند وردپرس، جوملا و دروپال ممکن است گزینه‌هایی برای جلوگیری از ایندکس شدن صفحات داشته باشند. این تنظیمات را چک کنید.
7️⃣
بررسی تأثیر CDNها مانند Cloudflare: برخی شبکه‌های تحویل محتوا (CDN) مانند Cloudflare ممکن است بر نحوه ایندکس شدن صفحات تأثیر بگذارند. پیشنهاد شده است که موارد زیر بررسی شوند:
🔸
بررسی Transform Rules: ممکن است تنظیماتی وجود داشته باشد که محتوای صفحه را برای گوگل تغییر دهد.
🔸
بررسی (Response Headers): بررسی کنید که Cloudflare تگ noindex را در هدرهای HTTP اعمال نکرده باشد.
🔸
بررسی کش (Cache): گاهی اوقات کش Cloudflare نسخه‌ای از صفحه را به گوگل نمایش می‌دهد که دارای noindex است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 672 · <a href="https://t.me/danialtaherifar/834" target="_blank">📅 14:38 · 11 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOIlsAyGDMg4IEuykR4iyZh3ibp_NdwtsNeic7tBZh87EwsiS-rZWU0F_FfdUs3f7KPFuu0hsoZHfvBKD92P3pwZWkox5fBdSK-40rigOMn3YQ06XpmP0aqlQHtu8M_xdZm0wKlXElehYlqOq_N5dVcuZsTgvuWEHW68HvN-kDYjeiARLNhkvx4SE4Np5ls8f95oi92EEYzAlJnSdAsWm8ait_WpMVEcmEid0pySqG1pWCTT4x-YLVjoRYB1_tfhNm0sQabVZModshF1O4cTBJC1moU4Q6_6RPv_b1rQ8azzE2sey1TDj291ZFIB4GdWo3ZVnt-PYY-aKp0_xCuOEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نرخ‌ ایندکس شدن صفحات در گوگل بهبود یافته است!
🚀
📈
داده‌های جدید نشان می‌دهد که گوگل در حال ایندکس کردن صفحات بیشتری است.
این تحقیق که بر روی بیش از ۱۶ میلیون صفحه وب انجام شده، نشان می‌دهد که نرخ ایندکس شدن گوگل بهبود یافته، اما هنوز بسیاری از صفحات ایندکس نمی‌شوند و بیش از ۲۰٪ از صفحات نهایتاً از ایندکس خارج می‌شوند.
🔍
آیا صفحات شما ایندکس نمی‌شوند؟
اگر صفحات شما در مدت ۶ ماه ایندکس نشده‌اند، احتمالاً دیگر ایندکس نخواهند شد.
🔧
ابزار IndexCheckr
که برای نظارت بر وضعیت ایندکس صفحات طراحی شده، به وب‌سایت‌ها این امکان را می‌دهد که به‌روزرسانی‌های مربوط به ایندکس صفحات خود را دریافت کنند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 656 · <a href="https://t.me/danialtaherifar/833" target="_blank">📅 11:18 · 10 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YydkmMJpWUpHOTA3PbU4G6fqR-tkOj3vYxDU_QwuJeeFcYk-lgVR02DJFqnKB2je0UuiZRakgvDoY42YGqO_arQUvK6Ps_jJal3qrXfkb-wGTV7fmdyu24Oc_Uh6nLMALtp-ZXvhwlP57dH8vOa4Ip12C9J3rtTNycJKwI3gJ7XIK67VNSen4NF6xZZlpzeMDw7UX0eILFO4jdqf0oYrjM5Lvd0e56nPSDPWyr95nJ2ME2p4HZHpaiyHPV_OokmxKiERCaTUvnOrIYL2leyys_idzUKpjIESYzrfSg9oLjcwkcbSTiKh_IVzQ8v9qE5vg1rj9Yp0ooqZHTgm8V9i_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
گوگل نسخه جدید Google Ads API v19 را منتشر کرد!
🚀
🔹
ویژگی‌ های جدید و تغییرات مهم:
👇
✅
🎥
تولید خودکار ویدیوهای بهبودیافته برای کمپین‌های Performance Max – ایجاد ویدیوهای با کیفیت بالا به‌صورت خودکار
🎬
✅
🗑
حذف موجودیت‌های مرتبط با فید – استفاده از دارایی‌ ها (assets) به‌جای Feed، FeedMapping و FeedService
📂
✅
🖼
پشتیبانی از تصاویر پرتره ۹:۱۶ در تبلیغات Demand Gen – نمایش بهتر تبلیغات در فرمت عمودی
📱
✅
🔗
بهبود DataLinkService – امکان به‌روزرسانی و حذف لینک‌های داده‌ای یوتیوب
🎥
✅
✈️
هدف‌گذاری برای جستجوهای سفر در همان روز – جذب کاربران برنامه‌ریز لحظه آخری!
⏳
✅
🚫
حذف پشتیبانی از VIDEO_OUTSTREAM – این نوع تبلیغ دیگر در API موجود نیست
❌
✅
🎨
به‌روزرسانی دستورالعمل‌های برند در Performance Max – قابلیت تنظیم رنگ‌ها، فونت‌ها و سایر ویژگی‌های برندینگ
🎭
✅
💬
پشتیبانی از message assets – بهبود تجربه کاربران در تعاملات پیام‌ رسانی
📩
✨
این تغییرات به تبلیغ‌کنندگان و توسعه‌دهندگان کمک می‌کند تا کمپین‌های مؤثرتری اجرا کنند و نتایج بهتری بگیرند!
🚀
💰
@danialtaherifar</div>
<div class="tg-footer">👁️ 701 · <a href="https://t.me/danialtaherifar/832" target="_blank">📅 19:35 · 09 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sa0b9pDESiDPzGbwdwqd10fP_q6rNHLAK_z1Ab-78AiqlM75JZXweCGvR8mX4sE122xT6C0XtA9Fctl0zx036lWzhlOvzmi-PyVNlbI5MpjUlL3IrYbYzsnJ_ZQU1RD5Ks8z6A21rwfJgs8AV7hn6uf3DI-DthPBZvIhFsUG0j2QhiSNInmTyS1b1fKYzphtGcjg5MaGS0gFY1J6Vf-9avwYdldTV_LXFchK01GHTszhd-R5CaM3o3yNAjNtbxIsJcUe2YUq4zaYSB-kBeXJ9il7j2NIrAedwklKQz6-ZmRctaOvSeDOiHX3DK_w3DYvrJZmAAqxEEqgPyCgD4vqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=sa0b9pDESiDPzGbwdwqd10fP_q6rNHLAK_z1Ab-78AiqlM75JZXweCGvR8mX4sE122xT6C0XtA9Fctl0zx036lWzhlOvzmi-PyVNlbI5MpjUlL3IrYbYzsnJ_ZQU1RD5Ks8z6A21rwfJgs8AV7hn6uf3DI-DthPBZvIhFsUG0j2QhiSNInmTyS1b1fKYzphtGcjg5MaGS0gFY1J6Vf-9avwYdldTV_LXFchK01GHTszhd-R5CaM3o3yNAjNtbxIsJcUe2YUq4zaYSB-kBeXJ9il7j2NIrAedwklKQz6-ZmRctaOvSeDOiHX3DK_w3DYvrJZmAAqxEEqgPyCgD4vqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
گوگل با ۶۰ لینک در AI Overview!  آیا کسی روی لینک های پیشنهادی کلیک می‌کند؟
چند هفته پیش گزارش شد که گوگل در حال آزمایش AI Overviews جدیدی است که با Gemini 2.0 تقویت شده و شامل بیش از ۶۰ لینک می‌باشد!
😱
در روزهای اخیر، کاربران بیشتری این تغییر را مشاهده کرده‌اند، اما سؤال مهم اینجاست:
📌
آیا کسی حاضر است روی این ده‌ ها لینک کلیک کند؟
📢
وقتی AI Overview فقط ۳ تا ۵ لینک دارد، ممکن است کاربران یکی از آن‌ ها را باز کنند، اما وقتی تعداد لینک‌ ها ۴۰، ۵۰ یا حتی ۶۰ عدد باشد، تعداد کلیک بر روی لینک های پیشنهادی ممکن است به صفر برسد !
🤔
به نظر شما این تغییر به نفع سئو است یا به ضرر آن !
@danialtaherifar</div>
<div class="tg-footer">👁️ 833 · <a href="https://t.me/danialtaherifar/831" target="_blank">📅 14:26 · 07 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McbY9LF1XlwF1C9eGMOshxG-8GjRxlTu3xg4pejTep1ucDgFmDBdakRrFa6k0T8CXe8VOh1mmStHieru99T1tFft4j_4Z11aEIQiQedp6R0Hqh_WXrRG96MDxTeKCNVRx1icCML3X_q6E_5EwpLsdm9jz7_RSzxjqCgQ80yck9G2S9pVxVaEPw0xVN6F2j5OU0PxG78ZB-JisbVrnWRcdUzibA_4dG3JYRstZ0bXQknVvMe4XkpiMhjHL-KKjKupqQRYgO7KfX0M4WCYfZSDDOdZM9JsfquNJidg55Y0_9yL8yRZl3EE_rnMgV6-Q2emcn1kzqnuAtWZ0Bz2neNWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
زلزله در نتایج جستجوی گوگل ! تغییرات جدید در رتبه‌ بندی
🔥
📢
نشانه‌هایی از یک آپدیت جدید در الگوریتم گوگل!
🔎
ابزارهای مانند Semrush، Mozcast و Advanced Web Rankings تغییرات شدیدی در رتبه‌بندی‌ها را گزارش کرده‌اند.
📉
برخی از وبمسترها از افت ناگهانی ترافیک شکایت دارند، در حالی که برخی دیگر شاهد افزایش ایمپرشن اما کاهش کلیک‌ ها هستند!
👀
هنوز تایید رسمی وجود ندارد، اما همه چیز نشان می‌دهد که گوگل دوباره دست به تغییرات اساسی زده است.
📌
شما هم تغییراتی در سایت خود داشتید ؟
@danialtaherifar</div>
<div class="tg-footer">👁️ 874 · <a href="https://t.me/danialtaherifar/830" target="_blank">📅 12:28 · 06 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
چطور محتوای خودمون رو برای گوگل دیسکاور بهینه کنیم؟
گوگل دیسکاور ماهانه بیش از ۸۰۰ میلیون کاربر فعال داره! حالا تصور کن اگر وب‌سایتت توی دیسکاور نمایش داده بشه، چه حجم ترافیکی می‌تونه جذب کنه!
😍
اما چالش اینجاست که هیچ راه قطعی و تضمینی برای ورود به Google Discover وجود نداره. با این حال، گوگل یه سری نکات رو معرفی کرده که می‌تونن شانس نمایش محتوای شما توی دیسکاور رو افزایش بدن. بیاید ببینیم این نکات چی هستن
👇
🔹
۱. تجربه کاربری (UX) رو جدی بگیر!
متأسفانه توی خیلی از سایت‌های ایرانی به UI و UX اهمیت زیادی داده نمیشه، درحالی‌که گوگل عاشق سایت‌هایی با تجربه کاربری خوبه! پس حتماً روی طراحی و کاربرپسند بودن سایتت وقت بذار.
🔹
۲. از تصاویر باکیفیت استفاده کن
محتواهای تصویری جذاب و باکیفیت، شانس ورودت به دیسکاور رو بالا می‌برن. یه تصویر خوب می‌تونه بیشتر از هزار کلمه حرف بزنه!
📸
🔹
۳. قوانین محتوای Google Discover رو رعایت کن
گوگل دوست نداره محتواهای غیرشفاف، گول‌زننده یا پر از تبلیغات باشن. پس رعایت این موارد ضروریه:
✔️
شفافیت محتوا (Transparency)
✔️
بدون کلیک‌بیت (No Clickbait)
✔️
بدون تبلیغات بیش‌ازحد (No Excessive Ads)
✔️
بدون اطلاعات نادرست (No Misinformation)
✔️
بدون محتوای نامناسب یا جنسی (No Sexually Explicit Content)
✔️
بدون الفاظ رکیک و توهین‌آمیز (No Profanity)
🔹
۴. امنیت سایتت رو تأمین کن
🔒
سایتی که امنیتش تأیید شده باشه (مثلاً با SSL)، امتیاز بیشتری از سمت گوگل می‌گیره و اعتماد کاربران رو هم افزایش میده.
🔹
۵. سیگنال‌ های EEAT رو تقویت کن
اگر گوگل حس کنه محتوای سایتت حرفه‌ای، معتبر و قابل‌اعتماد هست، احتمال دیده شدنش توی دیسکاور خیلی بیشتر میشه.
با رعایت این نکات، می‌تونی شانس ورود محتوای سایتت به گوگل دیسکاور رو افزایش بدی و از این منبع قدرتمند، کلی ترافیک رایگان جذب کنی!
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/danialtaherifar/829" target="_blank">📅 11:08 · 01 Esfand 1403</a></div>
</div>

<div class="tg-post" id="msg-828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRGU768EvTha1WRdnlBxfmw9xC4fB16lBiD5tADDwlQjKM0RfsqmNf8DXhCm51X6bjsf5sIIARGdzPJMjcUc9tAm57WS_sylFBqhmgGGh05kAnTsnSOR66LppIeaO0QRvXgUCYF6_b9rmhs4foOjdGmOOliCiLUQArXbyCIcC7WGeqireZEpckJzenfgav8c-0uN6AhITFYMZsLt_GQ4FOmGJTFQ7vxPVa55fxZBn1y3mI8ohJlIEWG_D_KidN0Y-hNKmbDyzNNZxtkFHIsZyivMh3hDQhh_KB9FTupaf3JqFkikVfADH2pJKjqJp_bYHcCvpYocrRbBfbSu_ipGcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مسدود شدن اکانت آنالیتیکس سایت های ایرانی
⚠️
اطلاعیه رسمی گوگل؛
‼️
اخیراً فعالیت نامناسبی در ارتباط با حساب Google Analytics شما شناسایی کرده‌ایم. بنابراین، ما دسترسی به اکانت‌های شما را به حالت تعلیق درآورده‌ایم، و همانطور که در بخش 14 شرایط خدمات Google Analytics بیان شده است، خاتمه سرویس Google Analytics و شرایط مربوط به اکانت‌های شما را آغاز کرده‌ایم.
⛔️
نکته؛ اگر اکانت دیگر سایت های شما مسدود نشده، در تنظیمات اکانت تایم زون رو روی کشورهای همسایه قرار بدید.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/danialtaherifar/828" target="_blank">📅 23:54 · 20 Dey 1403</a></div>
</div>

<div class="tg-post" id="msg-827">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GoogleBot-ips.json</div>
  <div class="tg-doc-extra">16.2 KB</div>
</div>
<a href="https://t.me/danialtaherifar/827" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
لیست آیپی های گوگل بات، آپدیت 8 اکتبر
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/danialtaherifar/827" target="_blank">📅 12:50 · 22 Mehr 1403</a></div>
</div>

<div class="tg-post" id="msg-825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KO8N1-w7rv-aqAHw_SjGHSn_kDdjN-Z_YFp6_5SwYHH3UP1JBrw2co2QEEpstG9wjHPqwHSxv6IzKtddpwYh2f5u7pUdN948WsWgQ5aAypdv5xOcRbe4bvBhirKf1_BjPtovm9y4AhY_1bI1c9hBDEGafW8tfzgTk8q6qzsSdXHWhmI2eJzDQCdc_frey_VcVliqhWL1GYB84Ffucd8HvSuqVJY4LAf1WDSWQlue4qGXS6ZZsjY_woln4yxeDi6guniFwZwQvvGngzcTl650HY6xoZKTxQhpcGSl0nyAbWysjLmiSM8obusRb1wwOo82PL6FCNf_uCx4YPPO0a2YjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUI8R1OqxYd0wMdkcFFDIlxFIvDxDh8-SVH_KmAoUUnA4j1uxXyaheqQHMk5xBubW8m_P-B4N1fb57UzIV-pBokFLbbFz9h2cqNv0YKyU-L34ZF5SQQv-mdGYgyHbKQKtw69TpwrQK-Gi96ujkU1xutI-45dxJjDVZSCy9kN0DaoWwRw0l_okhuZbaQyxbPw9VUuDAZ9BWF3CtUOp1BbLr6F6vbknp4n2jInKJjoYpJPrAAGjtQEZt9pGergS3dqotmEwIuwY7Wir-P88Yym_XYuc7XvqBjpgRLgi7BE1osEBerGQ-knLJrQSR01o8NiD7LRMtIHTNRX0BXN3KyPxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
گوگل در حال تست نمایش قالب ویدیویی جدید در نتایج جستجو است
♨️
در این تست گوگل، باکس ویدیو ها و تصاویر آن کوچک تر نمایش داده میشود.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/danialtaherifar/825" target="_blank">📅 11:21 · 23 Tir 1403</a></div>
</div>

<div class="tg-post" id="msg-822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2ST0CMbo9QOYAFB4cm1LtxKggwXTX6revxDP8aDreeS3RTXCX83YRHKlclaIRSSUXSdOb3motVQ0bWwNxUh6OKeFwU7t3ivi3kA4jlvLKzBthnQQYV19F_sYXpEdoTuK_HWyi-zZJcdG8akGdK9EAbvOmVqYmesV-wF0t2v7I3p7DrLdKx46Msl3WOCqX_NPY2QwdUbAh6WYZ515fmaOFtzTXKtJC1azxPDlpuKBkJBfS9ObbNlTQTG39jj8-uqLRNU2jem1COepmng6Dy4E8mqUOHZdKZnj3EJbMfpRihJ7udcygkTLBatNkjUjDwlFH85IRpsuhzrm8NLxF2x8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TV-dw_cMPPIMElWzY1lFSNlwoccC6jMa-vX1Dg8FI3s-2M0VNxlo-t9c09FdDhAwkR8cpVKMnt3QWveE11nxDKcmTWCAgvDGC3LYGlFz-OLxfjaUdp287c1UlHFHymBr5S70pzcD1N5Xww19pF92onVAdIgc8r8DGngWlT9YCS0Dovhp6w87-nvSnl_VYV57PKGGy_p6VDYVwL6wPKHge9CrcS-b-7hlbDboPWXYnAH8MRmArUkZangXVeH9LGvH1NQaocmyY8OKoxCMNH0-ujTUsCVRAAiqTnrFEDZtF4XyJNXMzEkMV53MfOT_4kzi6doZE2ZJJHYKQNuiEXInXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkvprV-e-nvVpSpCQjLigRBImlp2OVA0Ff17htPC6EEFOoB-S1U9t9klTr_arlP2XARVPunlBaFGS0onCnoseH9s5lqWCELt11vnlzG0I5RgwwS4rsa7ShA5g0zfAJlmhP1wVZnwD1sOrEdrVSur3TOAcOlbndDCs7mglEVazt1VXF0WHk4pebS4uh2NW67qUKZMYDehBdM-RupyiA-k342CUXSs38RaOvjW-phF0Fqv10qjvtC9t-oVz89QMwkyItDrHxYAWYbnp0Bsraadwp1fNFkZh1P8KUPEuI9eFe1Q4hxJQLAZidRve33hfMAeaTL5CnHxDGvV4an6pyN33w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
وضعیت ناپایدار الگوریتم های گوگل در چند روز گذشته !
🗣️
تغییرات زیادی به ویژه June 5th در نتایج سرپ ایجاد شده که نشان از یک بروز رسانی جدید و نوسانات شدید در نتایج گوگل هستیم اما هنوز گوگل این نوسانات و آپدیت جدید رو تایید نکرده است.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/danialtaherifar/822" target="_blank">📅 15:46 · 17 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Ls18rXEwGwMH16JoGLf1iJXLbdsNAV9xkU3JkuVSWF_ZbfCvNsIz5Qsylr70J7unj_jczQeNsr4GBp6jyH5VKHnKpphfbEz8ohLGUhyni_5Zrss5KYP6yJZK5fcVPWHvXZLKwUPs6OL3IdrQICJrbN1WYIu-IFCv_pGAxAzwBy8L83Ldu7xTvb7t-3xbBHOYlOL3QvW_FJZ364ITXrhuDTIZV3kPbLuMasrVCPtyTecaaomGzcqPqyjtsa_kRyuIt-1F81NfRqtz_SsB9RCHjQlW7deWrrZZkPXS2DTIF1_FgcWZV33Qo2yl0XP96VapAEHsjHGseMEuU9XAoc_7iF220rogR6BZChbph6BtGk3xTb9fCsjqOQmUfz767PFT8Yv0ia58tR67N6WN9Snel2FgJbNgvZ0q3VpYSfErQrptB-PUsMpmYAP1Y2B5mGjxVvSzGvZCgqOGLQ_xV7YbQ2_M3UGwqeoae-FCsUNw5O4AHsd2e2SYOhI-IyQahVua7O2tvAhXQPz742LPCY9xNTbCs2u8F3dtpzcC56d4Ffg0sJxAW1e5ojd-bv9vg2QznnzF0Gv2VU7ICkCq43R_ge15O4K9WlinKn_080WcmpKfCF1qqHbBGhFHVMRWwJiV3N_jyKnfEn4WXx2PLLnZOcJRVbWXTJMtWyWQ6wSt9p8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=Ls18rXEwGwMH16JoGLf1iJXLbdsNAV9xkU3JkuVSWF_ZbfCvNsIz5Qsylr70J7unj_jczQeNsr4GBp6jyH5VKHnKpphfbEz8ohLGUhyni_5Zrss5KYP6yJZK5fcVPWHvXZLKwUPs6OL3IdrQICJrbN1WYIu-IFCv_pGAxAzwBy8L83Ldu7xTvb7t-3xbBHOYlOL3QvW_FJZ364ITXrhuDTIZV3kPbLuMasrVCPtyTecaaomGzcqPqyjtsa_kRyuIt-1F81NfRqtz_SsB9RCHjQlW7deWrrZZkPXS2DTIF1_FgcWZV33Qo2yl0XP96VapAEHsjHGseMEuU9XAoc_7iF220rogR6BZChbph6BtGk3xTb9fCsjqOQmUfz767PFT8Yv0ia58tR67N6WN9Snel2FgJbNgvZ0q3VpYSfErQrptB-PUsMpmYAP1Y2B5mGjxVvSzGvZCgqOGLQ_xV7YbQ2_M3UGwqeoae-FCsUNw5O4AHsd2e2SYOhI-IyQahVua7O2tvAhXQPz742LPCY9xNTbCs2u8F3dtpzcC56d4Ffg0sJxAW1e5ojd-bv9vg2QznnzF0Gv2VU7ICkCq43R_ge15O4K9WlinKn_080WcmpKfCF1qqHbBGhFHVMRWwJiV3N_jyKnfEn4WXx2PLLnZOcJRVbWXTJMtWyWQ6wSt9p8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
فاکتور های رتبه بندی گوگل لو رفت !
🗣️
این فاکتور های رتبه بندی توسط یک فرد ناشناس در گیت هاب منتشر شده است و میتوان به نحوه عملکرد الگوریتم های گوگل از طریق API های منتشر شده به آن دسترسی داشت.
⚠️
بسیاری از موارد لو رفته جز فاکتورهای رتبه بندی هستند و برخی نیز اهمیت چندانی ندارند.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/danialtaherifar/821" target="_blank">📅 11:48 · 09 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFZzCTEVHRLDN92SXzepLCFSmn3MxXLvxJIOPZQe3pMJdZgiQJqkbzWSvgBbAgxLcYqmzp5A8AwfSbjF0boURHDXdpxFIdE7OHdTBQQYv17Nkh1-mfR9MK8W1GBmN-0K2mJK-pkUj2eIrMLZmTqCpEsF1OgsSbw3vnfXDvCFSMMWpIJOW5TmZ0qh4VFuFShbtpU7weWLh8f_FD-dp26jUeUVePGLajR5XiVNZCT0ZyRnFK-HjcMzd5jXNBoWqbtcVHjSvGt1iJ5cE0wA_4o-EfpLc8vCWV9VqYgGNowWB9gA1YF8TgRoWZktiXiIWBTMlwRlmjSfjJqayxx0KlUcZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QNsOTBr8TXpm0DIFt0YPEGUHuqNtqjEHjLV8b9Dr0ntvy37fNnhmDj8eBnLB5r4gZvDxVgHBNdE7d0yY6amlqfr1ViitIcQTQB4TJzp-_1JDSPQ6L0rIDAkEc-Cn6MkHVZIE7lootWLSqFB8lw-OzxNa_eYcvxwUpKnIWFaWZ8MogcO85cT8ghvbdRxHeSOoPzUP0AoTVG3pJb3irq9E1zDdj2FPfIsUgum7r6TRcZeI7OsuCdC7scJL-aTDQVTIOCW2ZXgqbYASczeJ3S6NqTxCYIqYkqwhsqbvzW1wqaDNqU24fwxIJHUrez508BPk1j2eVTFWtQQN7RyJnF4Leg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖥
جریمه های اخیر گوگل مربوط به Site Reputation Abuse نیست !
⚠️
گوگل تأیید کرده است که تاکنون هیچ اقدام الگوریتمی برای (سوء استفاده از شهرت سایت‌ ها) فعال نشده است. در صورت اجرا، این اقدامات فقط بر محتوای توهین‌ آمیز و ناپسند تأثیر خواهند گذاشت، نه بر کل سایت‌ها.
👀
لیلی ری، متخصص سئو،
اسکرین شاتی
در توییتر به اشتراک گذاشته است که کاهش قابل توجه ترافیک وب‌سایت Groupon از تاریخ ۶ می را نشان می‌دهد. با این حال، سالیوان تأکید کرد که هیچ به‌روزرسانی رسمی منتشر نشده است که این کاهش رتبه را توضیح دهد. این اطلاعات نشان می‌دهد که هرگونه کاهش ترافیک اخیر به دلایل دیگری بوده و به اقدامات الگوریتمی جدید مرتبط نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/danialtaherifar/819" target="_blank">📅 12:10 · 06 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-816">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CujOg83KdmdUWoZJPnuY3F0cZQbzwVocImpoKD1h-CO5XSwWqJ8-BlDqR1iU7ph6VlmJKF6iPqwXX61e2WFBi4-gfHeQuIWtlrxQ-kyowh3x5_eIP-dohHMkPcmYCt1JlLPHpgN4bePMzC5NvdxaOdOw7NpekL5m7JfY_ML4N4tPILp6HHi5CmmXPL91A7vW4QLRrkAwoM9kDLkVB6kGPTz2YGRJ_zbnG8NSmQkQ8Ars2s9flpw6Xbm2w1xxpH-v4wXG6SUyHGT_-fySSDbH9ynB_QmSS6QGx91UhoZqna4LHGuo9CO-aJZTiBbRi6z9FdQtqBbLHzdCRZfEgb38Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeUSTvWhEwUKNmwaJ7SbJcUMS9ZkZGd4jkXsUbfWzMBYS8V2M0KGpvzTQd2RkPi_EbE0Do9j3rWABseMgpBXaQGWm2uOHo64HgDygGGH-54SWCeMFUmRSR-m_NGbR8LXG4qNPos8h9TYuVlxxhzLOtubn9tiZ-13ZR0zTsNElQjn9azvkvCJnLiNMhMmGomC3XNAfrrjRjdf_qlZejeVmw1SWD9L43CRNbDoMV31vy-lIleQucJoOkPom2xAa719eCy0snlR8qIFW6LgZCbpTVuBjfGHdbG110Zi9bRp1_oZL3uKfhvameYknrnpcb9U3w6lwCh7XJcOfO83XxrrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDyjm-rUVCfMAYI5o4FXcYmhK6M66eZrV520ZOD-XvdUJ4bJn11S82-Yfpn7DUzjvBDRK6HSA3gQ62YG50gDezx0bCjV9sIXXTC-cJKWVzwOvXRphWlCZGQRGhllpIAaxB2SX0xsNwmhTKZEXSNvHm3JEaHTPSqxUCb4jx5CvB2IE5pA7jGHNNXM-y9JcZrWMtv9ckrig-MU__6sVQtCAFmEx2VkqmJfCPLQXNB-XYng77GS7BS4vUzk0UWAYVYbsLiqUqZUvhcTuVFtd4y992wwBFyGSwXVODz1sJrmxjfhyrEwLHsCJsSTWp0NR3D4mGHDnODcRPPsV-VwmScyeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😄
وضعیت Google AI Overviews در پاسخ برخی سوالات در آپدیت های اخیر
⚠️
سوال اول:
health benefits of running with scissors
/ فواید دویدن با قیچی برای سلامتی، اینجا گوگل این سوال رو تایید کرده و حتی گفته برای قلب هم بسیار مفیده.
⚠️
سوال دوم:
health benefits of taking a bath with a toaster
/ فواید حمام کردن با توستر برای سلامتی، اینجا هم گفته اره یه راه برای کم کردن استرس هست و باعث میشه آروم بشی.
⚠️
سوال: سوم:
How Many muslim president has the us had
/ ما چند رئیس جمهور مسلمان داشته ایم؟ اینجا هم در جواب گفته بله باراک اوباما مسلمانه در صورتی که مسلمان نیست.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/danialtaherifar/816" target="_blank">📅 18:18 · 05 Khordad 1403</a></div>
</div>

<div class="tg-post" id="msg-815">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUazd4IrgN63-inVWm2j1v067Ts3CVDuXfDqE8f1k8cGF3_L5vx_-mArNuJ1motZxNNnUtutgmeRq4EsqDr9DcGdFGk15-CeYewKd5HZETH0ugRBKWZDyFiaig57L4WDX9B7wRQXUqxgyDR8Xvvx7KevxTQMXqOzTwFjTAnQCIc6kxkmYKc81xY-AlgDk8lGgVOl25fbO0b1dk_IHA0LUaMmFpnbtGhSjKrXE_2ekysyE0v01BUuwJOdzQoDpZl1b1TE2M9SHIy25Xjrc9lvHuq4UYu3ptmiO8A5tpwsV0sjhKnan43V7AQBFm8bKcBq7uG3JcNiPOSpOhFOkKRARSO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=kXrgneLHSCpWE-P8-wtPWFRBvOFlX70_V7QsSIc2VWQssYHiOFea6ymJR_MNpR1DIGrju_8x6lcRwR_7jvowVF3P4JRby5Tjb9e6mWWJw-VFr65ZsGXtldlVcN0Jk1i1XTXC8M3NPYADJMyHdgVsRlmfmCFkXmnWg3ddkJ4EsnpwveQXq-nlQ7jGXha5_9OOiNh0-69QFmdhPUG-YpZKHLDxhYuqKRluUfCEm51XdxJSd_iXHjf2mWbnnJtbj6QdSHqfGPzxOKxkrfc-X7JbxgwjJ7y3NdDPRTVVeqvwRuOTItlmljIhvkyTq_wg9Le6ux4Kz0Iw1NEbo_eRBGbzUazd4IrgN63-inVWm2j1v067Ts3CVDuXfDqE8f1k8cGF3_L5vx_-mArNuJ1motZxNNnUtutgmeRq4EsqDr9DcGdFGk15-CeYewKd5HZETH0ugRBKWZDyFiaig57L4WDX9B7wRQXUqxgyDR8Xvvx7KevxTQMXqOzTwFjTAnQCIc6kxkmYKc81xY-AlgDk8lGgVOl25fbO0b1dk_IHA0LUaMmFpnbtGhSjKrXE_2ekysyE0v01BUuwJOdzQoDpZl1b1TE2M9SHIy25Xjrc9lvHuq4UYu3ptmiO8A5tpwsV0sjhKnan43V7AQBFm8bKcBq7uG3JcNiPOSpOhFOkKRARSO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖥
بررسی وضعیت سلامت رپورتاژ با اسکریمینگ فراگ
👇
🔗
یکی از مهم ترین اقداماتی که باید در کمپین های آف پیج خودتون انجام بدید، چک کردن وضعیت سلامت رپورتاژ است. در طول اجرای کمپین های مختلف لینک سازی ممکنه محتوای رپورتاژ پاک بشه و یا نوایندکس و حتی در برخی موارد دیده شده مدیر اون رسانه، لینک‌های داخل رپورتاژ رو حذف کردند که در بلند مدت میتونه تاثیر منفی روی سئو سایت شما داشته باشه.
✅
برای بررسی این مورد کافیه مراحل زیر رو در اسکریمینگ فراگ انجام بدید:
1. در منوی اسکریمینگ فراگ روی گزینه Mode کلیک کنید و روی حالت List قرار بدید.
2. در قسمت Configuration > Custom >  Custom Search / روی ADD کلیک کنید و در قسمت Enter Search query نام دامنه خودتون رو قرار بدید.
3. به صفحه اصلی نرم افزار برگردید و لیست رپورتاژ های خودتون رو در یک فایل txt قرار بدید و آپلود کنید. حالا میتونید وضعیت HTTP status، Index و لینک های داخل رپورتاژ در بخش کاستوم سرچی که مشخص کردید مشاهده کنید.
#اسکریمینگ_فراگ
#آف_پیج
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/danialtaherifar/815" target="_blank">📅 10:42 · 26 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-814">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzYdJYiYQ2cpbxoin2OdxAKT5Acz0xOrWwjo2IMq9nQ85SoV1dHYJVDzbAM0PNzUUYQXY4NFGl7iBOVU7oh5nEyx0JiyKEnR9MwHxH6QnhdC_auIIYbPolp6jyL4gHQJJiXP26DOQa_tygMW6Sv9vQRXnfQLxm9n_kpECg0gWCEOckyfYjEIRVLbJffgPsDxAtdhMECFr9p3tH8YAIebQLBFhP9c3oCA80dlVvXYmmeeRyXzCFdwtNQZPMF7epHKL23wTFvPUuXpEhMye6dNWOa9qpTNk8IuEOlLwXtuogepNxJ51sNMkv5eRQ5RPI1zF62v_RAr3RwA2z6RSkgQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گوگل لینک های اسپمی که به صفحات 404 و 410 داده شده را نادیده می‌گیرد
🖥
جان مولر: بک لینک های Spam که به صفحات 404/410 داده شده لینک هایی هستند که به حساب نمی‌ آیند و کاملا بی‌تاثیر هستند و نیازی به disavow کردن این مدل لینک ها نیست.
#News
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/danialtaherifar/814" target="_blank">📅 09:54 · 05 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-812">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkNVLm5CJkefqvpqDXjTZF6cieEMYfLSubPqhRk5FNZ9hVFzKJBSN_EbIv0U7aSjWtUqwUoLxhhGna5AAApsqIVN-IC2RosZ3sCBDCQb1AGtIrTPFR47TQ7kzUXWNOyh6If8XexzTpbu_mN6iN2-MPPpb4tnQ4e5REIkLROeYV0dWzzqWI1JWzwNo9f7c8xs0oiYTE3A6drIhLI38kU0rhT-LK83vKOMrEKsiKERQQBH4rUtqBEVtcahwxzy0LjTdJc2z7_W45TfInt7YjsIecy1yOEf4Igyn_dIiQYdkdDw6CgX9kYUF1py4h7YkBzXQPXGyApPerPIEPJlZfI38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
گوگل: بک لینک ها مانند سابق دیگر اهمیت چندانی ندارند !
🖥
گری ایلیس میگوید که گوگل برای رتبه بندی صفحات به لینک های بسیار کمی نیاز دارد، شواهد بیشتری مبنی بر اینکه لینک ها کمتر از هر زمان دیگری در تاریخ سئو اهمیت دارند، ثابت شده است.
✅
گری ایلیس در کنفرانس اخیر خود در مورد اینکه چگونه گوگل واقعا به این تعداد لینک نیاز ندارد و چگونه گوگل اهمیت لینک ها را کم کرده است، اظهار نظر کرد و گفت در طول سال ها اهمیت لینک ها را کم کرده ایم.
⚠️
اما داکیومنت ها می‌گوید گوگل از بک لینک ها به عنوان یک عامل مهم در تعیین ارتباط صفحات وب استفاده می کند اما در آغاز ماه آوریل، جان مولر  توصیه کرده است که فعالیت های مفیدتری نسبت به لینک ها در سئو وجود دارد.
🤔
چرا گوگل به لینک‌ها نیاز ندارد ؟
دلیل اینکه گوگل به لینک ها اهمیت بیشتری نمیدهد، احتمالاً به دلیل میزان درک هوش مصنوعی و زبان طبیعی است که گوگل در الگوریتم های خود استفاده می کند. گوگل باید به الگوریتم خود بسیار مطمئن باشد تا بتواند به صراحت بگوید که به آن نیازی ندارد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/danialtaherifar/812" target="_blank">📅 13:54 · 04 Ordibehesht 1403</a></div>
</div>

<div class="tg-post" id="msg-811">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">shape-of-design-@danialtaherifar.pdf</div>
  <div class="tg-doc-extra">1.8 MB</div>
</div>
<a href="https://t.me/danialtaherifar/811" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">The Shape of Design
امروز می‌خواهم با شما درباره‌ی یک کتاب بسیار جذاب صحبت کنم که به نظرم هر کسی که به طراحی وابسته است باید آن را بخواند. این کتاب “شکل طراحی” نام دارد و نویسنده‌ی آن فرانک چیمرو است.
این کتاب فقط یک سری از ترفندها یا فهرستی از کارهایی که باید انجام دهید نیست. در عوض، چیمرو به بررسی فرآیند طراحی می‌پردازد و در این راه، چند سوال مهمی را مطرح می‌کند که همه‌ی ما در یک نقطه از مسیر شغلی‌مان به آن فکر کرده‌ایم.
شاید بپرسید چرا یک کتاب طراحی را در یک کانال سئو معرفی می‌کنم؟ دلیل این است که سئو و طراحی به شدت به هم وابسته هستند. طراحی وب‌سایتی که برای کاربران جذاب باشد و همچنین موتورهای جستجو را جذب کند، نیازمند درک عمیقی از هر دوی این حوزه‌ها است.
پس اگر شما هم مثل من علاقه‌مند به یادگیری و رشد هستید، این کتاب را از دست ندهید. امیدوارم لذت ببرید!
▫️
این متن را Chatgpt نوشته
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/danialtaherifar/811" target="_blank">📅 17:35 · 13 Aban 1402</a></div>
</div>

<div class="tg-post" id="msg-808">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UGuQ0yArGr5SftFu62pwqSekSdAK09h3yFNRXL9GZJ2aq7Sxhv4ut4e-rc-dImtkUmLBASSrC076cR4wkgnBFn7GddGwNfcBTEoa7061QPR_Qmo3CrIZwC8Tj5bhXV0UkOjC_rO7SHrpXBd8IaTtSlYkvZ7Q_saAy69QiIizwK0l_xGcHppPjuKCa_LkxiTJhkmjxH2yXsvRLLqDn6LPmxJO2wwA1Jb_zpExP56q06_bGVW_j5pqP0KP6eLJd6X09mcJ6KDTkwE_Hv1eYd8S8Jcx3kELhgTQwOygcdK6rUM_U8clne7tEBgxGtJlkXMx0zEzGvr6FbGBze1y3VHiTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tZauLgWueYMzSoOFnoNSHl0z4vGwi7M8odPdHglSpoW58upYRh3kiwlaqTMMN5YnZZ8rTkFOyi8ReSirZL6pWr6GDv9_98tbtedfKXuAO_78330HWOWEYWQZCUTZGtkZU1PVYwRpphQTQolljMd3nk-3YYBzvfbXNoOxw8AWAJHuL_jNh4j090gdbIAvDHaDbTKaQjr8b0XaeGugqfrfrJjR50pmEbA5xQvdxa-GTCgurOqMTiQXoAEh6b0imeif4S1dhfpPqlXqn_o0BboFovwFFx-82KSS4bRTLBx_PIrMGiZnn7W4eLhVY9lf2XXzhh2fqQnfTLZMM_72H14b7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6KKsl8YRO0nrWCWS0Fcpavq4YAeBAcibb8gHHg_gFI0Q5RjWOtV8o-7R8gOJxhD1bGpALVtF6M73LTywtR3bXZ8yc2pmcfLswDZRYYXE6CG4sSc0oJa6FmhUUa0fqwtzrMeNcvwyfk1ogjrsfPzOIfGdKo-qkDarVrlZAJuO0jRgXcmn5uRu_DtNNB-H0PzBfkOT1q8BY5hMSzutkuMf8498MTLyDS_4zhMXAYcIYLxYD9Ze-97zcj0wJqKj6JX0oXd7mdbvzuyznEhvzcLqMf3-ZQeATVl9GlWv2basJ4LSuSEriTbHVYSY5Ok3sBLphOXLAndRe252XIH2tMDvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
اضافه شدن استراکچر دیتای قیمت خودرو در گوگل
💢
داده‌های ساختار یافته جدید خودرو به وبسایت های خودرو اجازه می‌دهد تا موجودی خودروی خود را برای فروش در گوگل به کاربران خود نمایش دهند. همچنین کاربران می توانند در این فیچر جدید فیلتر هایی مانند مدل ماشین، وضعیت فروش، تصاویر خودرو و قیمت آن را بررسی کنند.
⚠️
در حال حاظر این فیچر برای مناطق ایالات متحده در دسترس است، اما  در نسخه موبایل و دسکتاپ نمایش داده می شود.
♻️
به علاوه گوگل در سرچ کنسول، گزارش جدیدی از این ریچ ریزالت را برای نظارت بر مشکلات و ارور های این داده ساختار یافته جدید راه اندازی کرده است که این گزارش موارد معتبر و نامعتبر را برای صفحات دارای داده‌های ساختاریافته برای نشانه‌گذاری فهرست خودروی شما را نشان می‌دهد.
@danialtaherifar</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/danialtaherifar/808" target="_blank">📅 11:47 · 26 Mehr 1402</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
