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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 258 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 301 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 364 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 494 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 614 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-931">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینترنت خانگی وصل شد
✅
@danialtaherifar</div>
<div class="tg-footer">👁️ 726 · <a href="https://t.me/danialtaherifar/931" target="_blank">📅 16:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-930">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کاملا حس عقب ماندگی تو حوزه AI بهم دست میده وقتی که مطالب جدید رو میخونم و تغییرات سریع رو میبینم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 824 · <a href="https://t.me/danialtaherifar/930" target="_blank">📅 12:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-929">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMqvcXr1y6NaJ2PuJIkZ0Rryj2EA0ik0CwvlQINTTPIUr4H4utp9vMZbcLf1z-FaFu8udpc3V_6aLCyyn06BnyHHF8uzZmUBqDjQ2_g5PLALdXrJVzoU8-QA_ruirIhhZvAKD57GmOdmIvpPwaLr3MsRxNjka5SUpdak5ZK8Un1MOKol6Rn8-dJFca5SoooWZ9g2BI7MHAaL9SRkl1zWgi9omocxGLOgBEGp-6E7P6qMGfep9EQUiIfdYm9xiDd27EpGDjhFKjFnRSKUxy6237xkRzarbtmtp1D8lbMpHwCf8oM5EtGb9K3vJ5Xs78rxX8Gt5qMnjtbz_0p3s8Gf3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آپدیت هسته مارچ 2026 شروع شد.   بختت ایرانی...  @danialtaherifar</div>
<div class="tg-footer">👁️ 859 · <a href="https://t.me/danialtaherifar/929" target="_blank">📅 13:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-928">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده   @danialtaherifar</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/danialtaherifar/928" target="_blank">📅 20:51 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-927">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_ER2ZT8WV6tcGFcuZR6KDGF-PR-IXrz9C0N7nCG91HfHTT_BDpiBYj4g2S7dEhh4jY1dbm5p1DkSm6j28TzrksjafWTEwU2J0k9S9nf4l9t4dR0CaMWyhTrlDLxKgvcrPkydUTyir2yuDKcAKX--7ohfGr0LSMCESCxecmVork5bflO6H2otzVENMEC826_pr47liCHjgqzDWTadSlU6W2aFqLS1hb0ZLfSP__PXdTQ6Ncd14T_Qlr9-KyQIb-by9mXEgSyyf-1fK8G-X4_oPMZXcY5Q9tXVCIPBruErOE-I3K9iU9fDEMGYFJexQqg65pS-9eyyRBWJo_RpxshxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا دسترسی بات گوگل به سایت های داخلی باز شده
@danialtaherifar</div>
<div class="tg-footer">👁️ 974 · <a href="https://t.me/danialtaherifar/927" target="_blank">📅 20:47 · 01 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/danialtaherifar/925" target="_blank">📅 16:23 · 24 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJPRk8kEqYnSoAI0wNT6BcoAdS1WGRsSpu4pGfmhVH-LEtDSWh9YYCKo2Zu5gKWqEzliZ5v9AlfH3AjaksK1tLxrafDHVG2TVMpd79sPQQUSUqxTTUS817ka6tHMDm3LN-z_95AN9w3mlIUraOpkmR-SrsjzoGCxZN5ZHPaDvhLnZAU3GBEt3oxMqBWfvuBuSyz5Kh1tHbcEKZGHTjh4p2Q7zDNuiKu1VckNdG1J2_CxzgIhHpb7vdiCpkK9L8EjkbX4M0p7lAmj0VN9T5ZM2_emV__b9X5d3emo8j-y5tkFtAzUgMmC7M57UddrGhSCmFe0foUO4KeNrGK_3dL0QQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 876 · <a href="https://t.me/danialtaherifar/921" target="_blank">📅 19:38 · 29 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-920">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">در حال حاضر بیشتر VPN فروش ها کلاهبردار هستن!  مراقب باشید از هر کسی خرید نکنید، مگر از قبل آشنا باشید.  @danialtaherifar</div>
<div class="tg-footer">👁️ 942 · <a href="https://t.me/danialtaherifar/920" target="_blank">📅 14:45 · 24 Esfand 1404</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZlDD31f4yktEgqOkJJLnzrWJDi7k6N-p8ypg1mFrp1OJAXS188YqS1N1fOW1h2JbjJnieyAe_bMg2_UH5O61N7cYnPpLw6qRtM3wy09xCQnH8nH1jPVE3xPzHkg2WCQ0Gw6pQDJQPRNCmmO-mLifVGBbu9dYnoRDCDwtjdfLxNJROkOASb9u231dXksrBFZm9gekQBgnG69ttaKLtSrGbAGrM_lNFSC7nBPVjBOivHr80fY4byKcswTuBZvYjV10cwz50SX5U0e_DCp69xex7ohaulhL3OfWKPBWP-8Zc0UGqOJYX6gkruEh5Pyq6xwEgbGwuRQT0RcM7PKKMETdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCTW4WXqjnbCV8MUxcUKLQPIvlaMEkaXyMo1HW455cQsuRFWYDydqJJKva6ncpptUfOcUXbpV0atrgtIJ45-XLrXr_W1ItWJZG_5FGyXoKkR6GbkR78glqX7eLQ8AnBsBxd4i-g2AF8l_1v1MHAbC31CezIGOHCzuEmXIQgVgvOF9N0W_LV1DFIUSHdb04MTyIXaW6a40s5pLT4ALT1ulakpRybz9ite3ozcM6uaqaJSMJ0WQ6HB5gg1DL-EzxTSC5AR8yyapjAzr4di3hTnZg_kPPv2a5ZkRcFfK_c4vY_BMJ95vzt5xrroy3G7lEkEK63H2Iyv6l26sACTtd_ZRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu1_MTqTUASrIrrlPaL3pDmUf3RqEZmG9zLFMdvzz8vZpflkJyIDZgblRpsrRw51QcT5kd467hRVvlV9xgD1i87idj-rpX959h7qkkVUU253qUexzYcgB43PG0oERF9rBQeLD5nmk7qILUA8c3-9hfu9zP3K-OHF5JJ6vFTE3BI3B7zxv80gpLsPh65MNgt5OLn3Lswpno8keOFEyGFi7qA1WbHhCqh7FGnTCduXnwEmi8-luVfD4fieCWX9xZ9eJz6yl6ocyKOWxHvzXSkI6VpcAE5XRD7EsNSFUowM1MRETp9TtwsXPVQ104nZc1EtYXn3qdb0F2KsBphQzt9KeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-9n-lCNVTjagrX1Ofw08rlxIi_SprmiBpr_HHDdgXiuR9ibdq5sD5WWNoz18PEb9kSCLg-rUXn41-0uHwK6USMCRr0g2qJXoJrth9OQNGGYLh_zJpsTOmy0rpCJcIk3aGX6hqlipdKUXfVusV-WhiHCROxQmNY6RgwkgjIyp_lGG2tGEwgzV1c3Bus6NZu99v1P8yGqYNXplfZX9x7NeCRL7PlFWOcNH2wZq3yZnJ8ER2VkdoO0WYgB65ZirlHxPlkmGLkS1s_LJnuZb_QP_LffRWVKDKC3AlqmVGHANMEV1xqyI6O8zRvdM7WNLZ6Mc6kN6FSsAvTbhvp4YktXmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIthc6KhxGe7R3rufcLfe2c5M1uZcDmlTNcwxIpnAUmKQSI0Lo4GQkh5UfEmsRzDsL1ok8LPn9bBE64eW4hr7ktuASZicGkDDlUiUL8fCzryJFOSSFDGC1w3O0gzGmDkKMIVOVG0pox7iBxu2J8a4nua3rSYNKfRwpQ58dt0ZIuTSFh2sLkQZ_Pd8mGvW4e7rUHxWdPY6R7xy13iAT4PDwxkhPMUQVCRXfdP9oI1gzi6sN0AtCe-5diyaQtynfJJg-pdH-51BMDF8NESVlv5jjhnHipczwo2pRMoe2J6rkrqoLPEXT_k6OFP51dye7QVLzRiQvn-T4n_4npmvrj_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QM71xNFJmK69ARplc4963mscpeImkgdFzBzAnRl5uBKCUP9pgEAo_SfUgwZ2QsNfElI1El2L3Ih2LvWtDI1heQqJFIcLCJ8oYo9QtrblYoSA0xYutdUedCotOSWo1t_ycqbAEEvjU9Fk5WOkt_9La02TRhRnR1Mpsw4zBkJLcfY6Q5md2iVtDJAKehr90u4iLssLQHxqZYz8uVxPkQsubfrp9OihWYEwpKD0iGYrrQjKzUSOEYYi1UPyLQ4mbzu6VSXP0H7zYYBcxDvRen2xOzRRSQuiq51GGVALraznHiS-TF_EwfHB-48YtvcqzSbohgQCFLnbjRVipAFUDh388g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4PTG5he685VTAdkv_etrJtIqixxkOVQ0fh4TGI9kGwYgEeWQP2qzNr9VU-T6gNQiOaSbi4xO6Zj63eY8cw1jONqD0Zd9FnJTGvbcmFUzMBODHpzY6EMOBzqxrdWc4Pm-gN0jp_9IYWXZ-MlDRjzmPTcyrLS3TSnLyhe4w3gO63BdJePJqZVmihN2fmDb0YN0mxrXbpLtV8AyN-j8xlAqq4xL8aT7I9tTUvDOLrW6HXiF4K4RZ1ugy-Z4J5DaM5mn_atKoEMahG_6kJIpVxT_EJ5ITemM_w95PFDohiIZ_Hm13YYJahr92zTSUsfCoh-OnIFh1wwDzaXQeXhfuigog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gaehGfxC10qMQGiriuXLIorP1v-Bptcg9stgnHudhLYyoqFAd5M0D2Q-PYAE5MU1o4yQNfeGCNsPsmLCPeNK-MHRNG6F5WDaDTPRfMjECRiiltcg7LUWw2qK3M97KyPyty5jVEw0i8jovhWG-TuUMptTijVttxkHP6c5nykZ2L6MyC_b3i0hLeu6P8Yipc71RWMw4VxHbHOTgYSt-4FQ6GEuGxN5-i0LJjvNHp6VKr9DaBy-FLk_DfK5mxSWKHuejRKuoK1ak2OuRfUNiNrgvnukAZ4JGrr8s2ITmOx6W5Y4gct1zC9Ztj9DkMPIzwzzjWnGyYdIADL_LzWRJDKl6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9SOI--0536RIcV7pi9MgGZKqgsuBwlmm0oInESBBRfBpob_i6BjN_x_uRm8o1JJcCFpAbfzsafRELMduaoIJJPAYrlrUc3jqDh1InCxJu27NO2MbUbekWFbdcnOe4Fe8Ztblp4EW-hVs3Z7tOPedJCDNmMEuc9sLsZAJTPCXZWLXr8W_OxqrSmAbvdSXZC_faoe_w5SctXq1xtmpoTpZeNXunXB1Lv_cnDMRTf6ejEP8Q0CGTSV6mKb8YTY8CVQOoXdioi6jggpbHx99ejOykxCrmg5H3plLI55IsuInTwSKSaLYuk037PdpiK5EFYNgKJpLfId6Cj-8kp-uzjARw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=vt4nsjhXJguZtKAqbOwayHOfVr8KyiVTXbGBTHkYCy5nc3H8StUDTATlLrXXUKVU21QVr6cHqVURs-tgecBvQzCMufidTB6IBBinHIt277rdtyYBPiUTF9dYKaYkJ4zPzhjRcfjSifOABHU4EIlOHXA-IkOMtTST6ab0ME56hFAcHX_JH1_DToidpMs7krdshhp3BfAoHtticn1LxrMTUv0yNogffRN3_zGbYdtUstA64hl4dyQCrjIBS-pnYRxViSrKVFpMg3zblMIJ0OM7MdJEGDb0Matkn6eXGe7TSuc6vzYPAGT0g_1apPnw9vtWTEUIqvtfYoIE7lAXlxHXJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=vt4nsjhXJguZtKAqbOwayHOfVr8KyiVTXbGBTHkYCy5nc3H8StUDTATlLrXXUKVU21QVr6cHqVURs-tgecBvQzCMufidTB6IBBinHIt277rdtyYBPiUTF9dYKaYkJ4zPzhjRcfjSifOABHU4EIlOHXA-IkOMtTST6ab0ME56hFAcHX_JH1_DToidpMs7krdshhp3BfAoHtticn1LxrMTUv0yNogffRN3_zGbYdtUstA64hl4dyQCrjIBS-pnYRxViSrKVFpMg3zblMIJ0OM7MdJEGDb0Matkn6eXGe7TSuc6vzYPAGT0g_1apPnw9vtWTEUIqvtfYoIE7lAXlxHXJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUHulVM_bhcp0Nzhtw-u9-YC__RPoItDdfb4JjYTXyjNNk0TOLL97tj23ToGTLGJkKMStNj2-wuAvAQ83dvVgaHGSYIJgjisZ-t4Mu8dXHoNKpEYFrKKcLlTDbZhQ0qw4R2jkXKDUfLn8FEF0k7Ur1ziHG3AU2gpsEx4dZJtZXOKKpTcxnsXR8fpems7IvtIOwUK3FWKct3kB-seZGB-XmqGrfeh6RecCqe4Q_V2fPQCiORpLgPhZm6pE_1nHe_KNKiyRw4oTP30QoVb7HyOb4TnRNExdi-0cvW1Veir6mFDBBjd7kp4Y-eUthHuLQYgWiBmMefV3FtP2k7jqcLugw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ3yt2TFEpRriwuYxUfCBtaxLqFlWwMMVtfbIqqHh1ToRwADTgWZeL2e3JXZ5GiXC6348BFpMSqMl0kb38Ke89M2q-mM0Bvlm-meKjQGkvNnrePD27XREz_PVX0nl-rdw8O_uqGoCcWiBLki6XHYE8CbaK4HDdrVwRnbIKqbNYgvcYQKlRaLlKi0zWFPGGfKg4OPhSRWpAslRBwXm9-GngQjaj1ChI9KY-04L8spIpNQCk8abj_sHSLyEJ8xiNTYuiBHaoipQlPbPvz-iFlppz7ghHLmMvbtKpqftCbWvX2bOxuYN1meZY9_bvxLR2WGuVEJToFQkfNM7MxxBOzEUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WZP2CVXIOABPjzoTBcCwM3lQEpM6IQcrH1D6LnCYKAesBAizUGw9luW9UzlcWsPMzfC2WVkcku9VoikIkSQfr90-UDN6SdeL4e-DmLtDGGrU1GTg9Qm-Y8_aQtotc7EBNDEzXFEvw9kdTb6ivtNxDmzK_FJDGR9EhI-MAXdaN-Lj8WwN5XqXJZco1Iqylzx8q2oEJZWO8YTR6K2KY4_uqkP4qjNFtF2vIZVadfaBfpRNuvfHRY7FIy0yOdlneD_Vclo2pum7AAyuCxNIPW1eqN6hvz_LcmT1KofedEeb-nflQcwU4fECYw_7-FyRA98KKIwvJ2nUPPlEtwtoDY3wOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzSNtMLottDbNmKm6zdf2TOIdlL0xmGwSyoJtoGqJBqkz1RMUcyMLAgmQTT1yJm8C4kdDXXr29jEjQJKgiWu3ZUUFqoMzlU3100ZhkG0HQOb2gcVtLTJsdTwMKxM2QPkdPrA-7ylTQOnq4PnXb00vzarpC18mTNDYLRT-30zmjp951zN380kz4Bqq8ySJBvJSQVQYFhHuRod0_Tv3tCaFIvo1y8A3YnV6UXOgV8-06zDwadAcMMneSPGva6YQI_xPrRg9tiUb4-SIrMP_xINVoR6zQbJE9b53eRNBKkT-bnij0yfij4yo8opZPa74-hRA7yyHYs3iHeGlUrIyloSMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJToatY3P6RGKWHqEpUHqumBbNcs6krOICslO_5VNzkyI-ev1SDcXNxkJ9hwyL2ShfD16ZqWQsEKh568NthJs1aVHvlZjOTWq5bz-1dOI_MBBxZpth-cg604yCAWuqtNOwwV_7WdWWI0SFFdv4P9-wOBv9qRv-0jVXxC9TyExiafxRKW1um1Ci5YEgkn_-HH2bebhld4IhJCcQIwH_KIFJJh9FCQJTWC_E9WePikH0i-_E4SQIuNoep3V5GO8ux8pWc3_1pIJGgckfCyP3a9mXeOzFtM6Iy4weNBJG2QXr9iyUChbLAsoxPmshPhvmRiYw890E1sdBMNoD_dGBHkbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUas0ESNrAO9WnvofGKsXwQJBZ4yX4wNl-dxx5SYbCB7gymmFqtXdT-NNFDehBfaMa8_PFSVUgBC92X3gYwFt52iIbAVjEBZdLW9KDA_qLLhUJsEqQtOMRqbIiugY0ysEkqTqucZJv0Zwjm8wBxJPB_usl6vGxatGrXjBuiLteBxXyWrKhSn2fXLbAko_5Z7mwzCh4iwj26Nr6UtD1ipmtFBq17nMrZe4bsQwkZq6MXCu-DgC7_BAX3g3rb7jaTfqSaMn1wG1DjaWVmMrIhKF-IpasTEUUBxEguMMunxeVPVe6F3xvnzYTRUtUV2PngrTmGQ0HVT8g-fpI63g3UDEw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/juLskwfOsgp7Ji0lvughRJqRmcTLHORV5SVxKsYEJmkgv-CF5DVZHyOYaJ6loVj9tQuPvax580S-Is4U8dcySXIlWsJcko2MMNjV-VPYEf5t6Nw8cmHkklv_va_JaG_nOAfGC_IAJCMEe10j_UHgAp90clOZhco4_kz9-3c8KflotZXGY60aYvsNjNm4RJKIxdIvMiJBByT3VnGJ0IugPCLY5_h8-uQT80scMda3HDy_42zFWO8TdiHvAjTUuUkbSsUCYNVtHmqFPjCOoXVDqQVaEwEH0roC51kRGiGnkQ75yGIDfScWBHqW1UzS1W8fRJWOhpeR8fCGONK2gXIuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvpSOHc_gnIQpQkqIJ9Exr85e8M9IzD3u70SW11tO89eSoX7X0LOEbyE8i9VX9xj1UNaUq-ZsMcN6pGwvFlIRi0fEBP6LPXEJBYUTjctNKQZihVmxxzeQo8x_r9yTtxhKYF61B4gEE_7t2k2JsgDqeafZQ-3awvRvCcY25SVVamGlGMUmtB99ZAwT73jPJHHXD4DCY_vTOZmslQc3uHg0mzatje7piNZc9mKvp7mYu7xd8AiZ9ESeUp5vrulKmqoLCmStFQBIzS9t2IvuVMCRFJE1cJPWdmju3xQ3i2dyrrvWy5TS2a-265TCrSHB_pRPoUGvgObx7twr57y_KUQtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T671f_MFYAyIJJAxHwYc-mGC9-43jhvH9B4fMTCxEbz-iq68C8VYYBTabJZkFx5gC0AIe1cXb2g-nqAq3zbqfrJXIWyMLnysdeP07wgTCTpcpFLXHC2ohbJOF6lIrZB0L_9lXVQorJ1x-bHbaIVzBGQ3hLkQIgA9Mehlg1Gxzl8i9ZNPp8XQ52w2XYCBBwcM97auhTvFEFtGC3vcYzVAI4YS7TxGOBriDB12n-gcpZTQ29r0FdgTkXrYBg3ThkzreotlFTqq8piXXtPXsQKzBIHcoJjuCbAZekXgpBBFL50K7pSt4BtLk4x9gBHrKPRfbpGVCgy26jhiMYy3dXR4cw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDS7hBsLNPP_r9c0bkmveRQ0FI9k_-8WiPHtVeSjajnoOxtGk2X0YhZy4OJW2TUWI1h3kE0-r4r0pNzholEzvN35hC__wAFbF1KtgudDnc6_nkH2ez6H-GPEoYHg_uPfMOwmD2TS2D0-YtHTSmltneew5pruQXl1TeliPXEQdKdLmMCYhUhwa1M2tUiAI0md39UmI4DSzOa2Zuwoz-eCmXHhK0QyDe0ZAqmwtKNTjjUD9K1O46bBVPMV3yfvRFlcVoSghmDCAwD4k1mU-PeQ3pxvG00xtu1GN8xtByTEcZ8KMd7EW1_inSA18QqWlw9j0wXw3sE2BB4j4A5qDMhROA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjuUcwJGugpYb0l6Yox1TlDBjJ_716l8sEZVRdAD7b9KrNgNoB66PamxIr9NZycy7PoDa-yAJcdDBTfsJexImAOdEoSxOYw4KZBk2aBxMROlawmhBqz1kLL_AL9toS09UrHT-WiTWFPtRT_ZjBI8780CMzHxNmUc8vBbpdo3PxWHmYUIK4ew1-CI3HWLPM-4Sv5ca8u7EYZMJdJLCGlOrfA2IR6_NQ0Ly0g5iIL6I0rh2_L_WVeeIO_20eZyfta-0zBHPr5otQkOrye3x7qeIE3ocENdrMVxmnNyt8taRH59RUSE7Nm1nOqRVlxsXE6XkcOlrhGAk-COnbsg64sjXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfM1CSWIB84KO57rxIYCKng5S8mLpnCFvl8yYi9etLodqZkT9P8Is_4Aw1RVZ9hXMNi1kNyg3xJWYSqPDbCLNIrUKtDTijVxkSh7BTvIGsB6Mid74iCdnf2tNpiY5Khs-mtrMHxHCwYoi2J2C75YCzLcJio0VMeZ74ylKsCmrKmoSbQmRNHHgOFnPRHco_7ANUBPG77I_M8xse7CrNrW_JIeUyFIvbMmHalsskdNS48ZyHlTTEn8TBST9rj_vVMovqmxIYcSbKDHZBM2vsEL2ewL7VN1E-0FFftZiJu7vQzopQ6YPpF4TE7Fdyo5Gj3gprepqh5mFHbm3SWn4_zypA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CdpEtFH_GJ6YFXPQunvuTvTzr5z5c2FrZ-nCP3shWcBnDe0q9PfJi8lfpSAkFf9V5jtsrmZUjgY_VQSSyHNr2SEXYj5J_IZsAxr-Id8dGB4TTen79TD6I78OFPXd_7AjSoHH-vFnQxGvOY42RVl1_xqGN1_jGkYZgG2cNusWJc1IdNQjtXcbpB6S9xLhtjdIv-BkFdg94yHPVJ9gk_p76umJiMA7z5Laea8mG-G1zwARU98_D_4EG8jNXsWVVC4cfZjqR5g09N8GKSbXg8Mekb7sU0WPjoGX0mK1nYT3g6c-Nh1DV5DC3Z7Unu-IPiTMSo5mrRxvvdzJHGPJenmFrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kSXlEdXaaPSUptclrehdzZD3k_j0w-Cx5Vay0Gi99yMEu_Vei1B_e2akv3mXrippJ-ome5ViD_R9RJuWG17lrDdIyFS2BffCmDroq8ZQo_hXtPtEdScinrc7DE6B7wjXPkvZHZWYeSkLiIrg3RJKaeUyiKo_d6Zik-ilrVAuo8i96ybzUq1K3SLrkNRaD9jZzrfJZ-CK-3_MuG8_Op4o3MIiV1Exaqg1fB-s6Wx1R5D9ucmtoYjrU6rn8Rn6WXvXoy2ktz3lYNveNaG7Z-DNwU7h2zSTYLZfdRi26RFmRg4kdbgCcBEn69FjYuP_ZHkiYFI-HO-12x2sRSz0UkwG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTDroWrkgTOSzHeqe4ysGflz9PmeKs6L1xSrMFSm7IrwVKVwoBGxaqK9UAUMO9SjOFnM3vD-wcHk-yIdSpoEtAXcmjidUWZgXaYA2aTmMTkt3HDq9_Px_jpoMQh_G6WuwFcNFienw_vI6_pBX2ldfvpY4P1z4ZHh6LyO9SlPLuEG1saIxYb6IYj25ljYpIQrvooU5OhkYJ8mjXleECyNnn6WYXGJhpBfX0eeBqz7XPTXrzLei74bbs4i1564NdSbi0beH5NvIL-fh9Gcapcx3l8oyZ3pP8VTYLg-wRthz4UpzJuePKCtgeEWWf8yZjB1mIamdAZ2VBXvN1MI9EtiMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRSvHXOUOi_PulySyCnkNe7sRYbbL7bjah1uzgKxopCu5y2z3EhmTW7ruyiSvJVaXxS0VJhYeHaA0Rcuj1UE8ZXAfgtsq8PrvmxmlhyoPvnJi2ulhvqmGV96D5bR-iNDJCIeSM-Ihq9jMOjrz9krkBmFF1cRZj012t2KenK3wxpAIqSZBtTTr0v1fup2CwPNb_0eOAmSrID8B7wDL41QPxCIlcmfO_-qrjCrSub6O-vDnWnXVyejCwVDo80fm8g0UNN4WkQMtCGOoh0ShjgCcoLpyHi0vThuvNdYi_uXXyx0g0v-8Ib_PlYBb_-QrMWm_ONCwsm_eTczAYUT78hxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SL6NN63QEfNtUX2BzPLcnB8GQGsmQwke0wBH6oPBxOdTH1GRuK89c4XMW_Rw9ci6Z3TAipv-8Mltg2ba9P3oxbhN1AtJxiMCwvWAN32xkPuKK7eNCJsx4yrQ8khrlMOJ_yQybEYpvzRyitmK6n8NXY6d7NTSeEklUum5YPn8O11e8ruPoSXim82-0uOcCRjFUHwHqVAmkQUHj1klx4Cy9is0LhpX5yKNE09SHd7iuN75OXpkILRXPsNjzBSNPOIzXVyRN1gqQNHsiuw6pzXWDUNEYG5iyRRBNUYplwrIAa9EnCaMcIwwUmTkq_y5OfYjlabuPSej9b_Iqt_VoEDoDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmnfFozGOOQ4FmMlWoLwfmM7lTIZLrRTOrdnuVAyKNlYP2IW-d1i7CJ0D96XCEgIMo4LRr0xjAYEQhlp_3hjoszlNIm0Vrak9FLIBLvYu4mwRNf-OhHodxBiLn87fGX1XQB3KXw--hHqnOYH8QepexHGJIRlAvsfIxE32MOsHO50fMb35gj9qZqcgOfl6De_-RHYAxxnfM1ZiIofm8ROqvjl9hos-kXWlRxt2BhUhQaQ2i6n6QHYBtUJ1SeXAV0FOz7fA_rA-yiuQ8a_mPhB-mecWBsgLrZzQDyBSJwkwxMavp1XZfVkXiJLTNeKA2z4D9fFFqlkNaGyGqWRXIx8vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLl_P3Ox378z9-pDc7lMZo6oWkKWcc8kXJ1gwtbeYT71hIIclqPKjgtEk6uacD6u7fK6vTjMxv1XWTg-S-8JGWgcfiojWcji5Z9tfUIq7SHM5YSpzOlwZfemsNHKMhPMZVT515C4aNsSB8ek-L9X5jBCCNt0Rb80J5oAdZm679TwodSKhixWpc8PFDoG_V3vnmJDahYqZAxJ1G96uSUN2usDCS-kOdI_nbWalGiuqIU-FHejr6IbLEU9_UPiXhMi3kMpdLc1K0StzwscRYRT2zsfxTWu7wEHkZ6kWTGilUaBp3Chy7FaIKoMAVzp3UWWyfCYCJDWRoRJSAcbUwzNOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNfADx8QaXHGlFaulNvcGgbdTHWfA-NySuvCpYN6StLKaw_rQ7doLcAV6Ej3WvN1djNt1bnWwTIsHJGahirQAopfYlOzqEic8KgcB1bgGapnborkzbH0CO1FSbjhMmkdpyuBbkltquIKnjmyrMhancl3Z90UE6Z078_dZcm_dmfmjmItwNWJywO2HY7j4qSLt56IxY4m1nGT1bw2EHFDUqtKM4P7DvVXjfhO9ETYtZ7EP_ElgaWP0i5H2XhvJsfHcj_TaaBV7AzSDqBseglNFGMsbZRK0T_Eg1fq7XT__2PSA_0jL4cFhUyRzcFN4Cd9rN7YSp71zJlUP6GkYgdPDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of69a4UpSf5QvH_c9F4kJKjeOyOeo_Ey57d_bnScW4d80CNAFCybf7I5efsY81aw1w0Pexa7IAx3ZQrFE13AnXkhNFLipCXA09QmmIatEKBKsjPqjBAWj9AZjUKsQ4oaqiXICAfIcxRd2CSy9L2If4Jo0PCQvcXFf4nCb1B2omNx5zhEvLi7k3QM8Rm_F6vQGKzNDbUnL4X7s1DjhpxxJew8XnDtAtPFH21wxYHZLBOF5wKiabtAd5g3d0hA2nH0nJBjxKmHO190w5oE7UzPfQ6SEBWDOw08Q1BsHrcKEHB1VKItExS_vNPX4IOMPn4rdfchkGw8oT5vQrPiYALzUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 644 · <a href="https://t.me/danialtaherifar/870" target="_blank">📅 12:59 · 15 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-869">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGZ3G7j1kg3rGkFfdb5HBHi61vCfaxhavTfldqV9UkdVjFD8kwH-dUB8BmuxbobdlDIJJ2jjuEIIn7IisYqn-WYi0CEb2LYVJCe4YAbfT2QqIvvgxaa040h8xAd-vqWuhSS8BUueMaEU2c4AmzYfJIC_Dcgx8RWttP0_xaHXuNgWYHJozR5xJjjwAKrX8YvsKluLG43vSgyBBwt7ycUefK7pgZ2L_snEf0pZPBsMAOLtSoHGppl3R-uHHk1v3UoDbkxxIlx_kssqCL7138FAZAIpkCVLyR_5R3RJC08IMCeNyt5i3oFf2hSzd0fjXZLA46Nav6hZ7Aw_c-8E9EkLoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBFhrcRN5b7cd_JW9OxucottMMSr3Z_WfFW-oRfW-lTKx3pjwGs4pxwuifYBV3KhAwckSjnQda1pbq7JcyVvXTOUCMLOebOFpBe1sSJCVJ1meg8P7xz7Q5KgNPgxUyowwJMhSAFfx7QWRdQH_crep6FI7xV-enLwJ7bavHoDpo0pi1xnGT1i5eQnAEso3jVcqXEdMpVFFWLEgpKJFAX4bSvAU740oF_QSkIuxYKz8CdO2BSUsRt9t5pwiiLktsuFDfk62sBC0uvrzOADMVAsW2GK2ldVGn0-2gXyY1XFw4fZ_eXIN43zvlmfg_UvrLWkmC04EVQPFAM_HG8SyxC47g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBwqJmm_hFcIRAsaqiRfEepaFjJvVgEihcDL1yAuOTXsXRQgFQSfv2PUUTtd6xjp9ijijuCnHuHwdiMlg8IFoZhXFwq6W2gi9HIrfFNAOYvW7x8TGGgI1TSH9tL9b_07Ysvx5v888y8f0rztT45MxOl9T-cfX4p7fPCR72aDrRgsccu7pYOMLipJ2MgVCJafaETbLknaEisNcBcHSPfOrBAzoGVKu2z0aFgD-MYxBwi2rSmDUPJcH7-2gJFNrVaBKY02Ewh-DNOVukcathc8W0x7Lwl_lCw2BVrW1RO2XSW_-_M-nAV9-j6GIOj6G3hRcjp921c1mh8S-3nI150s1Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l88BFXIWN6v93StCbX2ltuzlXUzpNVAE9SsD75O6hwgN9b6kQy3v_aoyvO9KGoZSWL-6mQP1qOYKP_rMHFeH7-s7ZPO1ZuKyJZeqP9KW_mMePPIGzHknMPfs_AEi3KSxqzkxKJXFugSGN0HAqsZsuWxhAkQyY0J1gSLfWm3PmGLbLRaYrJNJNaMqPgzXPq1QbELlpGxuR-Y6AcZYiSGfL5JLazSr4rsfB2wAS4hY7Yl_9hIcbzRLha12zqn5BLP3pLJfJ9CqImsH1rHPN5kSL0jJkloIK46Gtwi365Y9G1EDGCLGh39B3KN8muf1gtwTbyxKH1RbcQ36_cqrnEPclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AJOc9fYdZb_d7z1QZLcYownHoL8DugmVR2zMZfd3QoPvP3RA6TdDI14-gIWDlRIT0tzTdZtoGmQbBECPtxWs1mo2e8PaMLK80elhFHhD2D3RUZqzBfBUlvMcRq8tSaes84m8jAuaoT-iNqrIHgkYBAgJCVfujMUferyTT9P-D9VqmeXeFsmVlwQXy80CergdURE1x5Ce1LVH5xXDIKFx_3HgBynyV1B94IMWl1yThEqaPvm7nAehHBFmoc6JmOM_qZAOyT5Rj11GkvKMlF19yYHDMtp6OKjpnEQ1hg0nVBo7oDBxOWk-1OksWhVOMRO6N97m3s-YAFt-hME65fFNnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6NUEik4wsOWIbX_5Xcbk1k0ehW_gWqd9tcFnX5kqskuMWofNp2Vvj8V28so-NB6vWpEpaeWTMe7dzUa0odIj1jFS-dqbVfhqMOEFhAgXUYizNItONnhADL08lKUSTyN4dt9jeh4uzzaxlkS-52s7CWF17ZMwNlwJXo4T5i85XsWBDhFaU1W9unhBs0GMaC22HUHn0shdO3uJn5z9JKcaMNSqY7PwMh2H8UdlNPgpxcYwnuUNoxgrMoAWJbYgWDJg9m8h74cBwSjzhmna1Wed97EVcctbXzpOkcM1HktFX5ZcuHAz58rpPHgSmwoShn5wauouRDSv3Taw7gyn_p1dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQlSTn0yt0FuFuKZQmULwznTeYvMfZzJIz4WeooB8JyB2A_JJ0mD_pV_4whV61LooV1RRbg8ZFpI3VR5c5IkQURkiK-nZwkA9ZyPpWE4dJ10ir7O1SBN8rI9AYEUFj7fSXhO9EJEKd4nHfXvbxcnoDVB-G-7Q_LvcZmqCFCk3lzOvGgjXR7qNpByZkZXXuhvF2HVGWPegovkSqW0Q6d94JqVMYMIl8OZ4Aq4cs3ZEOW-LUqwMT62dhClhc-S9iDIkXmv6AsvjA5UqIPbpIAJSEW3vOxs8RnvosBNw_T3BxPVum13Zob_cbN1KtuEwQukbq1szB36NBtCfX_ydLTnOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiDX5UaSpvj6LibS_yUGEpFBUbHGQMHcBJf_wtP1NUw-CLP8w8D4PQ8rPZyerJbk3d4WZzmJxIXaQRGtVNtnf3BROklI1JHN-RfvAQ2kZeW5AclnHwcSEj5lavNeB2KCjNyC8ZIPhw8hfr4qWTT9-_BF3ZP59Ei0WiSWCRq1myOxu9rSm2KRRldi2R_Gu0yjl5xRwAPHi0GssJF7qojK7lKS8bF9s7v8oWh4p2AlSasxgjGJkOEjJEazg5_hhWKbFX3tqNPxXXRLI7pr03TmR0gFO0Dl7oBmGJLgx-xzYYQ3NYi2taer4FAIg9LQ9LuoRWkSB1vXgXE4jCy5viUwgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BINMv8kgz-_RmMgdmJ3FpOa9uo86PFSg5wbZaL9IU6R8n7BJKiX2RUMFMBb6veR2treDp_FWrkQX3-e7ml0zwA50aBRXn9oR9o2KIE1csYH4lBc0KZJQz1EBRaIQb4DHU6cujrbaoaKOGQXvKx0nC0kBI7z8OjRk65xxIQr4nCi0aNP2Sa10ZINLOhZizOas0ymbccGE3xzHIf3JtIwzaHxBa0e3BUf9EyuRisuyP3-2QaeFGGDppeKsoR3LjcsNdcKF3fyHltEOTrU0nqxaPLMNjO7Pw9TQxio7a77v_n6lMHj55jwL3yfYXPcmXTyQ7Orpbwm0xEU-7rTG4xXCrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n3Xooi1qQfwWbdX1tEYNhBA_dlg2N2uDqGd_-me6t_uUEAZCLYbRdXwF-kC9SLgBe6tnwrC3avV8xDHwknlnK2XXCcAabpIgpvfEEu8Nmtb2Pyv9QxD2qZlMofuYgEXuhYfukNV_graLdZsJXnuU5V89CfvVwmXcFVLdN5qFSxWaKLQpxkSb7pGCScGFioQh5fnDjBe2dN7y-ez2ajluIm9_bv1O9AiZkylrMJ1g4N-dfHjgzP4rPkkFsLW3yWLPhq25ym2sj3OUztQM8Eb0sEb0IEXRyqOXUavjg-vdtWdu09xefDW0lwRHFx1IRLU9ix8UFycXOE5-R2eRx1cTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPpm1lNsPDqpjgspSJ4CqJnE4sICIQwuXu1yn5Efn1BeSudb5e-YprjdLF02vav7dGxEGKbyF7TEJSgC4bYDvu0wdiUZmnP_T3cRN2ZUDgHY-QIsCYA5fx1CGdapB456Rsf6aNx05MWWQqqD4cj1pRVb_JWA2vBAvOJvGa_OetVgZgt4AKsLCLWiI_4iLrusiN-FHMsY9OE1Y1crWdsDcb6VZFSgH04CYawWyBv4yEBvg9ztWY0ETuiEcmlssOAYK6Y1iLbm0fs_8IyLXbCIeBC78FxKfntQUwFemaCx9C4u-BpO6I_b-jKO9aUQt7JcWC6CY9DtWOMQ1AKqggxBOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7F-AyZGYI_4IkXdK4RdW7yzAQMeFc_tAoRegTc2InVs29NFxx8-AQu7-NyF0nCOjFUIRbLs45LqX3o0UgEAtr3rEx-exyxT30h_yC3XH1VPXzUgarOdYBUxRZBFTKsIw2QwtpLOOAAe96qteE5dP1-yNyP7sijMgY1nJVrxMBWBOmAnwJFNxmfYmQsMrDPs7ZzmHS6MuvZekHi_UCup6L_vyRIvOzFve681t_UqYKiWqZWnw2BNt8jLhPFCHitZjQht4th3mmYVkzmRvnirtujaEv5PpPQJkYzN6LZrEYpOfcha5jiaWhAw866Z8AigE7cBVLctp17teZMYJF1saQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AWSVOz8Y1UlulP4l5Av4lp1BQFCPidLg0_1rRmFgmPYV3Ij20Wy7b8vRDEwyxZJAbXoROh8D1FurrCpY0nUIn5DktDQi9JrF7PA4HSeXIJq5pXaiI6-0A9FeZAnePpUPY6zn-QTCv6wqDWeErcDdb3c_DWcaQ1MIG-gqgdzIzEb-A6ot4WOkNPofXrromKKwSdYDkpGXAG2hdG-3-V-n4Ox9aVi84v6CUOnsRLpFFDl59IyGYkXBTSfsaSgRUXRoR4bjP3zUpkobADyIkUdWJi9fyaQAD70ywIskQdkcE9VEDluYqvp7b1e2deym6X1xnpQsAaA6zYz3_A4-xKRImw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruOv5S7qMzkc7DiEt9Oz6c02fzNQlRu8aAV7Mx5xwoOUJdmbz1wc_BK4N2HPB0vYgyH06Fdq9Aba-FCJ8bixwJJqBS6HOvLP1fWLm9xMZRLylR-Tk9O0_ScSvvYLG68eIx4-Q3mnDSWrqga5FM_lHCmkVtxR4alLFix9VXm24RsAPv2a4BGF6ma-q72ZnFKk2JICHDiIQDhpMFxoqn03f2KSdNOFYVsZ5SQekOhmx-5mq3Q1w8aCMjLOmzHmfgjlrGUL7DAxIOJF4p2UJZ_anThn0J0FZZilEE-clp8S6L-NVFBRWmItawO7XL0c_nFWT9_KPxb167Yaef0cLShiZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-WAY8zaD4RMBxO7dUweEtinUZy2dOtEtsnT796hC81z9IBtaEQavdkeul2Dxya2n0dvNS97m2gGApRiZQ6Sdnrv6oMU4DUqD_ShNws8O4Qxurz-YJFBoDtUNcBe62u2dS2TA1mEXeGdFaVAA7LrAHKGgFYCja6tNYp3O7NDan1uLzGDcKKdaqauUjONsiBGiw3oGzqDHz-CIXd_eGMPgMov7Wv-iOep29Hv4MjR5zRuqadJ9ucVAbGOGBvRUpm1AkxL2swAmVtJ6k0GGIoq6oeZQSZ369V_utJinuNAxe9mFJDdwgWCuPEUcLd1aANAtvW4RnSKsVN7tEZ9cygGAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kR48y6QXJMPSKbms_9BC1NVcol0-rayvFRxpCuafJVXnPWyvbo18_W_szJykbNg7BqlbfEG4uvTArbz_nqa9iNdRjIAtA6F2a2vnheLQTQ8oDUMqk-s1ZWAiteDxdRigeBek8m9SjCnt9ocrZT02Vo_3gr5cWa2TkYkFw1df-fveAaJp5Y3UFQV-r9ulGG_qifGsNM-YDf6kt8g8ObWLyRMA6W8Jr03i2rRs1OudX-Zk062OYynkQHG8-bxAftWMTmD0eNkO5Tg7ntOwupDoArTofvXAi4Zw62wA0Bd-vRVjhjLNHlJPJ5b4dO3M_UDXuTdROBRsgTR_Uq1bsNoooQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdeE6AxcIFBevuVtdINlSb_eDkqWrJzapvnhtnV_GcpSZkwNbCyCmQWBnjs5UT1BrkC3S3tCl3whe7VyAS8mMFoS9Tnxcv3Oz9wl2sjK7WgNLV0CLW9cFYNd7nIdB9kjwGEuLNcAjP-8rnszbOegbuCOXJsGWpOQJk7NGcFVEa3PIzlkhhNW9s2mKXyt1H03KvBpf85X-A44v5IF4XhtBWbg3o6Cjdf2n35lQR8_mEiheX50LRNP7-PpCfr0QQudiwmfLM-n6GH2O_p4dL_DSrz5R4ywlk95dWZ7vbNfpXW17aqS05jxXKHXckVINkJ2N3kubJ3XrsvQEag7fWeIAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFELkRH7VDG75u9WioBfC5GnVy6G7NXOyOgdR7_mNdaIdqChngI_lBQ1I6qQlLzjQoXhCB8tS5nyvnc6GE1QdKDvlzJQ1woqXoEztF6E6D34KEMxid_oEKxipaarM1EyKgOWufStHZUDvWM-vO3DIBGqXgE-x5P4uEf9QViFtxexxbIlxXdEB2yWKFb9qWNEtTjimAqoVq7TPMqQUMS05Wq4Aw5g5RnHiGanBoZNWrhi5pU6snj_l5mCFztRAOudUppXGfJ4x0wI-40z-9yWtqK55vk3-cZCeGC95thQA4lRt4LS10zdDfRZPtTb_flcVVhAn1id7aaRLgrFkVtEug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifjzwxGi8vsPfO2mPqHpW_rWBMom7nXR6PGKPHYvNsVkSnnuiyzgnIiwAGB9-0sJJNg6MEgpYym0PLGQ0LpMHjWnblyQQZKo0ZQHrTPLrnYXiVqNfxZGEb1L25uFAJ2iDGx52cMMQ3EI-9ZESO7vi-C6r8Qkz76O9p9hBR2J-iwWm_7RGEMHKIl4F2HA1LWGAiY31gZX158lH8jf513xBpQT3fHZX3u2Ngj_lRwIdKGqrCOiAuuG0kgnO4J5boYHgTxHTX6uyPqRJVShIHLm6jK11VeNqQ8xbedth_oajjw1qBsP41x78kCBpvBIB5nAQUBfV54j8qTDxQYdtXAoPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jc98UKXFLxVYpl2uj-nljkgWMVZAObQjrg5p9Wp32bRZcTMgqPZyZjY9HNy_4lNdWOJY1cpHxdpGJi0JMc68lQt92_4IKQQib2sgdsgX02G7VqXcoO9BDp9p53m_6aifcp7z8-Mg1H4dv9aHzWZ2AtTEB8l13f4nKGM5Nys-aXP9HgSpoPRm3xm1E5e56uFhNq2TY4gSWPbQCtLY7qFPwalC9IAHevfDmDJ1SyzZteZ9OcQ9Ty2ZbBRGKc3uHoiCKwt440hzYu0l0N1krT8lpbxi1_IKPX2QDDrD4SJ6KI29HP_rCeWkeq6VaRt0c7HtcqpBfIDhvHl27K9eeS_ogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWIgfntNLzHrkyB7zCntApAgtBXh-Gvg2oaWUMylpcE_-dIpLjZKvi_nPIvsl1IL8Q4rI71Dx028zyHSpnPI47iP41-8Ljhx2_6EdihQWhBKcN5kX6_ZKE2SEKi3ZzGQBTGdbUn3t_FjVs0gptQJGsaVVvuAVqPxFxw_OxyhJmFCHe01Y71ozZOTD9qc4LwBhWBRnthupNM4xfW71pTeDl67-Dm7aHntBbQf9WhOIqmv_8Pp9LZ7E3SwBShwdNR7AwqPvlPakxjBlVMZWyDAjNCHXLnYYryjq5hFI4iUW0o8NkL8hTSu_blOqjg3p6iif96tbLhxrEiRU3lze0u6Bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCK38OwN1tbnRsvrnbNQ5DnR7L-UKtHN1NcXXWYpnweBYfhWXai0TbVXMA-aYKh8Aw1OaSWFRf8g-t-eBQPHZB6LOThGoNrCayZ80Go3kAIuY4Mk0SI0KQxe2x0TXY9uCiJSNic6JpJ-uUOqZqbJFdI5NwZlmjh0MVvzxG3pswW4cxmIxWQbbFixT_uDQ0fRFoT1OuYDpXMH27rFTVUn-PXzbckVJZ5NHAJLr4UlC3K2QuI04TC2oAizpzhdgwtqvAsAGgXii9KDhduY_XjH0VZgqfiU1JXXT0tkRLRhKeedBM30-IJlm1uaxr1QBZJe9-VvETDry-8hWcYU6GOqUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhHstCz7DrEGxj8vLiUxFUXwuYwuf41g-srrVg0jd-FkznorbrSh1VWQyT-Pq2LZeAs3-p5bf3xxr0rEU9Mo7Rgh-W8CW8HvtPdtLkn-Eeu6N5eX0Czjd3QVchR2bIz_9mEHHUW0GUrKZMwGCGxY-D4nR321MNK5e-IWTD4-Xk85U-Xn0DGsK43juUeFUkhX2G7GbqmSjSmCsW7ZtzRdNKkW-ZVXT3IcLwnsL0HQIg12BIweSWIwCK2WxReMhYaOCcydsji8k7Khr_z0rGEe9MR5IwlKuQ7g53qT9lqpJyaRjVQA1bH26zpSjLiaIfHP7FjVmsRjrvO4Yp9F2E0ZKA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWkFduiT9gE2HcI67nwzoiCQszkKpYHZlGQpPwoJljJ2J-MhCQmITTtQsOV-RHq0YbPEQWeMAlFi1qRJIkN7koRx0MLE6uc2mIBWITrEnptnRDeK_rdfi6CM0vE38qumEJdoLag0vfu6UeZLygHV1Dns3cMr_HjrSCkDbQ8DCjQVMgW0EDmCT4-9Qg0-cknkZLLefHCrGb7PKO3cLZqULOf3fBHb34xNhobRv06ypK-AOX-tto8jT69h4e9RLfsnyOC_QjvVIFvXXfMCTzPkxRwoyyAqxpTGzrGkZKyOSQPEXlxw9uDA6msgwc19-Pa0Qw7Yx2gtr1wOlzbNSo1q_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWxG-0f3xezAa526PPjhFp5lTHbLCtwsTQ8SG6l9mEU4qjblMufvdwzM_c5KGZqbkIBb9sX34_TFgYeDrOjS2J2ir1Oi3DIcd2U5M6sXACbfrgmOlzBMJyibeqwjk3X_YRQe8zTvN5bOUVFjtlwncGSbh6I9cvtfVO6W1hORib2vHShzgm0mC5iEkeJa3UuxQK0xjdC0jjBxr3dnDpRzRjJ9srNvNktUjZRxNnSVV90h-UAYlgccCEq7yomLbc9JySB4l6gvFRAnOFLz8n2hFQn8lg0e7yZE-veTAHNPlgOrA6tPoxZBbCDnGqd5bQrwG3OLYlS7l36L0fJNdh2SFQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EF0j9dXh4GzP3-LMI9aTBTevNBwTaD3A3LnG7H7tsaHYMH47DVSYNunem_obZCgX1ERNrtNtiY9tRDYRUMSfT3mzVY65OEBdRQg8yq-ZudvUjfjXkd7z17TyJXfrJDnwRK00HgEpUr-1kKNJVvyz3rxmRj_8jkmOH82Ey4dFXy0fR5Gg1EgwOpW9MCqqRuuW9kSPEOGYrklXfp4XDeOQYSuCSMAuuKZQNVzrurTzAinMAwYfw3Rp6WypACR_6L2X7KlLphvnJzCdnRLw88wYgTHxNBeWGulPPuAR2Dm5dd4UKlIuW1XZdM88DTrPLU8lPPADi1VmdTQCsk_CIqWZ3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=EF0j9dXh4GzP3-LMI9aTBTevNBwTaD3A3LnG7H7tsaHYMH47DVSYNunem_obZCgX1ERNrtNtiY9tRDYRUMSfT3mzVY65OEBdRQg8yq-ZudvUjfjXkd7z17TyJXfrJDnwRK00HgEpUr-1kKNJVvyz3rxmRj_8jkmOH82Ey4dFXy0fR5Gg1EgwOpW9MCqqRuuW9kSPEOGYrklXfp4XDeOQYSuCSMAuuKZQNVzrurTzAinMAwYfw3Rp6WypACR_6L2X7KlLphvnJzCdnRLw88wYgTHxNBeWGulPPuAR2Dm5dd4UKlIuW1XZdM88DTrPLU8lPPADi1VmdTQCsk_CIqWZ3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPdgbN141zrF984QcCQjidmk8MlPJLoBt2d2qrujnSbl_OxJE0IRft4QW4ZEVm8dzhpv0VMZ5C5qpJdV2ZHscboE6JnNZ6fz3fEODNy6seiECIdVFTIqffihcn-9J1RfkSzjxy51wqXAizs59tyyy3kh-1frvaIDooYzAWkvv63fuWqTWhPpoMjuCyYqX1XbSCKoHaIbXuqgL-QcOYba5BJHlRhjg3zP9xPoZUrFBt3bepzRIGfSRhYWDH8mymUtiHf2jXKW-lfdIP_VTIzxMLMHWPTBScSSwItBPasSeCh8rC1ziN5CxYpqrEPFQdXRStTmsM1S4tnmrNlB41tc5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EozXaX47PKjsyGN689cHtOcXylJcHsdyDsQskOUTIEwfqGn9XwO2rby6HtDbm7NMxosJDqcNtfY1J_pmsZHFAYtbWcaOxefu9CWUyAIlgCWHjuNfzgaJtClLw_yM3SB4oZDGteDXixJwkHLO5y7iwKl4sePbP6YLLnM6E7oMLt2fNc3zepXqbIMDtQ7Z-73iTLhTPHN8TxnOPIct4JRTa0Wn_2WIrcIAMMPQrXTJnyS1xBfxaz0ckjSgLUmlXV6BuaIECghmqiq6bBA7k8ZcSlltQ1JTX1UEvnpHu64BAA_yZqPKcHOXXWfaDcUGiSK1daWGCq9LAob-rpxAim7snw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jo1b4nR1_iaxjVJv3r-MiUGZHAgsLS8rYWFrJ-Zu9kmH4IlFcY4FBu8z20HDVtA2p-LRXbcoxIeZF4LelDED6cJittqp2jzlM0s108j3TV0RtzcLUynlqH30_MGBhmtloJ2G5x0s8Vl-xFfm-nRUWULh-OvnT08pE_hEckfo7APuglL5iWHuKCoS0wNIPyNG-0FiJbCoIYgQMkQW56Y_1DTuiZWfqulfJCaSpGwlH7tEnlxUCFQqBdo-QV3xoEt9k2lN9Dcn0rIg6s_Ob9XW5fS89XSZsnu05lheyq9PrynuezoDkE3VxQEKt_--zFHLZtaVHVXi61vO0ppP82qabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDB24f9jIpu6XT74gINAKng9-YWJOq6DzZs6o1s0sM4Szue4KKVjiaWT-fvr5ZKA5nOtlliargvhUBGkugJRaJ_w9Kijj4soHBUegBf1Iiw7lg6Fqn_2x630xIusJ7XB5W-9vT9t4_KY6-tXKXPJxO3fgMZYSKpPNzTkHiMQ802Y7mZ3BlMqWKgM4_qexCuvGBltOUUCLC3V3GM5bl7JSyfIwJXRi9wzxkZoZLMHeH0TcEuXWx_BQ1myHR5pzDwcPEfBrqMt2r79B37CJuGRnMeN1SxtkFTmCZ8qkW8pCYkKPxEu0bWDx4KwvUyZUCR6_lvkscK2oI5FNYP6vpSgtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0CHOkvOw6fpHBSU94DirBkWzyz6d9lkFyopfRdnrx-pzX-nywjuV6f6gUf-DrWrUmQw1d_T0O1ReHSx-1IuhHyyJD3bFAGW9dHCCmqbKJ6wZlRwpXLAyK972ySAYmUExTfKYcSLP6fQ0R08ECVt3H8NlHvtgq51ulGqUtRSnamQjsvpnCQYpyazY-UERSjtybdYxjF5dybEvyKRubdfLw33QsXaIFstqcEP_wUZ4ZMitdZ2F0IboqOdkuPJxp2xWRRlHXY5mci5ryTQR3G2QT7OvG082bqJ1IjtQM3ELm2yBXeYl7L9oc08gYX65zfSFm-_n1RJzoKHu7NC_Edyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q9teu17Gh86iDACsTcay56xNRCm7iyWduoe9sGIblbdR8wm26k_oKW3fQ9YN-WKNlY61WLv1c_iTeWqrRuVEMFK-OARf2zdcp_nuOd-UQJ1fIDQsGybFjyy6twGYrfWN3X_XmhZIwkW8OHXHsWS6OfbKJIU2R3UnmagMRI8gr1iKaEPmIRCgj4egEPuIHSxis32f5ojSd3-ACQKVnxixjd-ptJDBj5GwtAlRnD7dTSa3j4SxNsgTFZIKhaMw-QJUCPVzHhm6vRk1OmaCxxuk9S6zyKScOR8Zo7RZI8awFHj7VTYJ-CBMcXc0udkpctc_fFI0CJf_n8Zy3kp-7L83qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ULx_YJ3gcmbsHbFI6VNIEBtK6yqhUOOJxvlJOwlO1OsjJXRqvTGlcOHzx49NTXvouDB_aBbVEsOPX4lNehFUl0GylrqE2AGqV6IsWkNpWlNXLVotDaWMLNv6m2-agjBlWPH9odOsHipaFWvfxaQfzCjpR7043yZcsfYq_Z8TCqSfJuCNzL_1Yf3rcXvowbkh6E7jqlcLUOKHCS9neSpo-MWGYyB7JslTsabYZRx8zo8_FW-3OCYS16DsE-yAEr5pQGzR2E8FZ1bMGBExAfJ8Yy1nA76DJ0OfxFDWOadoRvBrO9rAwq7DERI5lVj9d46iADNJJS89yKVg7T4oTYJXjQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rWmKw9GN4hikXVrds1ohV6FZcVOcOs3oNROo4EyaAaPKdqAL8OdwWQZr2WZL7V31ik40J8LNka0ITx8gY98oVzhNWgpLYll7TwhQJWjnmzeMuXNTX6PkpZusRjCM7Dlu76F1jW8fpFfq0SONJWsiAl7nyeAvwHlAAMK7cof6DGCIRuTZP9T9mjbwLEZisTMjmWm_cBdohkOWKM2Gs7smPPaeypXLeycKiimCojnkAeyrFzhPgSTrTiZx6_5IjGAp-uKjw8ywFdwOHxnkBl8b_f1ISeq8F4lU93FKB1RLyWNuaTVwX0meiXavGGVgHo6QpFzDhC79tO8KE1bSP4mH-5HKUebPFnWapfTVmM-qLcog7_wCLXd0P_Ix5nkqg7lQi2ZzRvFQmWFojUqmROLcOo06wtmKRJKrtmr_E7I-Fwgbe6uqRYemCheyeVPdoA_aLCeItYv11pEs2WlVtVYBgCdHNldLZQE6HnYhWBqj5ocGZ8KZXp-wvd9Xsm4gAwBSV3drQmqg-vMFb7TNXl4o7o2i7slcYjYdl7wUY3bws907DvCy4-d3prFgFRqpcNhUR3Y7QBxnsTlYwSs8sXCJ7MCQvJvwlWZ-_fIsGspbcCNpBBfDSiCcVQAvoj88kQ0Tr_UZuqX5NCm-tzjNpvS21f2E1ANWL-b_nmtyI1aJjjI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=rWmKw9GN4hikXVrds1ohV6FZcVOcOs3oNROo4EyaAaPKdqAL8OdwWQZr2WZL7V31ik40J8LNka0ITx8gY98oVzhNWgpLYll7TwhQJWjnmzeMuXNTX6PkpZusRjCM7Dlu76F1jW8fpFfq0SONJWsiAl7nyeAvwHlAAMK7cof6DGCIRuTZP9T9mjbwLEZisTMjmWm_cBdohkOWKM2Gs7smPPaeypXLeycKiimCojnkAeyrFzhPgSTrTiZx6_5IjGAp-uKjw8ywFdwOHxnkBl8b_f1ISeq8F4lU93FKB1RLyWNuaTVwX0meiXavGGVgHo6QpFzDhC79tO8KE1bSP4mH-5HKUebPFnWapfTVmM-qLcog7_wCLXd0P_Ix5nkqg7lQi2ZzRvFQmWFojUqmROLcOo06wtmKRJKrtmr_E7I-Fwgbe6uqRYemCheyeVPdoA_aLCeItYv11pEs2WlVtVYBgCdHNldLZQE6HnYhWBqj5ocGZ8KZXp-wvd9Xsm4gAwBSV3drQmqg-vMFb7TNXl4o7o2i7slcYjYdl7wUY3bws907DvCy4-d3prFgFRqpcNhUR3Y7QBxnsTlYwSs8sXCJ7MCQvJvwlWZ-_fIsGspbcCNpBBfDSiCcVQAvoj88kQ0Tr_UZuqX5NCm-tzjNpvS21f2E1ANWL-b_nmtyI1aJjjI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fohhN_SxHDpBm9NugLuRUuSqepCAh1gjlJxcoDruJ7fLlV4XG-CN_KEaxY7XXmaIL6TwueRDV13qwqFbqWyWCbvmdoXjVvOroJVCSqPOx1lJlhBFq9DpxKSOrEKBELvYeT_4rpUGuYXr3DFdwbAejTOjJhxDoFd60btwXaphAlcLjJ5-4PSmiJEa4NlXoZag2UPhO3qARg3DpnUNbzX2ctScz5tCoHGZAMl2ck49tFp6Ajsv3XnUknmy1N9RVtvrA_QlMfqlRqNWhQuqktA3Irw1UoEQ9kg6hCa4Z69zGA1mnganQP_2cQCVnUY2V8LAF-mPnrmKE5erycUiWh4ShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sw6zCkjk7oDDcG2Lxblear4Nv1tpwy3cC67SuChHSn4xKT8T-bsfazeNt-lPE4igUD-SDLHr5vyqZ6OeIVypL0ptOS__XKlwz2PvpMK8R9lKeUDCvzg_DHVtGE9Zzh4r4kknNSZeCLlZGxOkQVbkI3JSPYb7UWBIPDx6Zl-vsT0_YGcXNYQQ0lsmvCwm0YjfUd1dn8JEbu8nRoxZyphE-ToTkW_U99cNeIH5E0CFgH0Q0u7NMWkRNn5UEDxfMp7GHJZfAvpggbUnLNrmNtgIee08SsSRhMaD9Dmpg-yv55XuVusFuA5NhhaY5uKo3-TPU0d3vUwAzZMjIxFpg8TO5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iFxSWelgQVoMHTHkYK5xQkJOynP_4KvBEQXZJmEtp497GwYUBI2El9bhiLrtrLzKyDJ0Cid0ibjYkIlsomCT1-2hIABq-__n2BG7GF2bxnsDSDoU4eaHAfjGfeAl1vF4rzMYmB0dDXHeXbGBWrCr4nO78liB0Pc5OaP74WqiLH6DGbSiOTVjgcbipbLJwsoiN4I_dopanM0pdWOdTrKGCaFKRxSU6Ny6fC90H2S17IWODecZt5OOtcTZcimbRoZdQ-NmMZB0auHVEAd3TpV5nVbJy0CpEy--GIS3cabPRz3WZoS6NJQCRgkCQu2KBIDOf5gUu-EB5j62eQ6oZYaLtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWzQp44ZD1GiTSJuboaVqHg5oMaeIoAZFD05gZ1RVKm4XMf4Hkbef-EnOCRkZPsLcJme9VBeY-j6FTzTBVQPG9zSyx0n2LKTvWS9gRXNCXf9_LBpgB2HGGxmlg92-RdIWNayUVNjFh6oheqZ91Yp_YRX1ZBgPHs5Kb4vxFNNLEGPJj3XzJaos3Cl4h2czhoqe3gCsv8l_Flc3KQ70W0auZ3g0wdB5QVVrNGYwTt8JXTKsMSmtx9s5sGQchnQ1YkYND5A5XbAQ8sy7hfiXd8N8HTuLkC4pjRW31oMuXtXNOFr4CBSkFC9B5ZxSmytSV7ySS5ARsDyOblPi2GTSoenNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J3wonp54IXDIrSZpuFvKmbxXLYx9cijY-n1KvnxHRjJjnMOe-Kwo4x4ThBEzzqCHLRuVWZt1_Pjif782BwTBJuH8DCqEcQM3wHMtEY8abvHm8yKVSkndRiwlsRJkk22PbjNHLRAZwweTbtPNnwd_mzb0fHoie4cj6bPCxA9iN6dk5xE7dbafZYLBhqvV1kqoJUcED0Ba4843FQuHTjfARryJ7U-Acc3jhJOvZVEpnDJce5Ji2drcfcDjYVVmaHqtGmbragm4JaxVHGQvaS5Lu3ilMdrr0hTR_XqNZeCUbLWqWeJn_3G-5cgHcW4BPJ6oUHi_If5DWxwPW7UVLow1sg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RN_9bXsY6kVHuXMN6EXJtXZL3LrYygl3mAog6gvCGsaHf15IcicJDpHxDIxZiQ0NmhPvyuUFYx0j-7Pd3tfB8w8r-FFb82n3aqHBJ70NN2hrcZXpLqUs9XMoOYWM-80DBYN8xuWRO9vs7BPd7wuI2noxJr14XiBe5FkkMRl1e124w_83iK60g1vcmf_5nMhGCzMUDduHkEbuusHPSamcceG7Yd-nFHd3N3wxOtt3KcyEz4m8n_sGhWJDBu4vcx3uiiQzQB9hqP2-aJYNAfG1h_VyiZ_nIKy4Hi4t0szDILDXp5GWw4aGHsSPnrdV4co8TIYFLv4GWtwDvvqeoFrRRk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0RN_9bXsY6kVHuXMN6EXJtXZL3LrYygl3mAog6gvCGsaHf15IcicJDpHxDIxZiQ0NmhPvyuUFYx0j-7Pd3tfB8w8r-FFb82n3aqHBJ70NN2hrcZXpLqUs9XMoOYWM-80DBYN8xuWRO9vs7BPd7wuI2noxJr14XiBe5FkkMRl1e124w_83iK60g1vcmf_5nMhGCzMUDduHkEbuusHPSamcceG7Yd-nFHd3N3wxOtt3KcyEz4m8n_sGhWJDBu4vcx3uiiQzQB9hqP2-aJYNAfG1h_VyiZ_nIKy4Hi4t0szDILDXp5GWw4aGHsSPnrdV4co8TIYFLv4GWtwDvvqeoFrRRk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrS0DDSGB3kdeY8_wPTGUUrZRu2p9tBRgtMKP7qn1XsI-d2r1toIUpEJl8ZsCwmqKrdvtWlejz9UlkG8zX8f_p4wKUQINFU0iBz-ZyXKWRZn21EdKMbkx2_5rcQLq8GJN6w8vQjfyTlcBbGXvoEWxn6stspBkfzxqd3E82ntx4_1uRWD3xDX7Au2V368fwWVD2xI6lbUmZIYxUrB9qq6wDhD7oxMJKJHblIJlgfKORn4z2gcXeaT3CmL6EmS7hc87pPek4j8VclDeD8Hc5fE-6XiuGC_HRixzJzrDKEkMTO32LMnxutZ7QcrWI5suM7SFL2JAZkO1Rss2IFAMZrZjQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbtTZ8bMQYUvN3xkNXv-mONrh4nv8rw8l1WQ_EqiwbPOUAm3UCUkm_3DBkRnw4caWiUAGuRZwqAyrL8MujwHjXp1QGv-ud-FL0bD6UOL3hACEEtzrPXW-tKEhZpMVtfMYIawyqhUm7t0fvmRA8fqGI0fIOPIKRO6yZYhvt2ef37ErqFJ5ItVE1gaL6hbFLhxO9g78AEiDrvkTrMmrLZKQzSjVSPOFVbCaDChg-_ssdrQsk-JPB4lC5dXH5hYEsyyUiKF9qWv-FcJ59Y7C9xeDT0l7XUkeVS5qweak5yIeacu9NeTDuxyaeE4TN73IMf9zRgZ2AhFJFpW0mT_5ooAdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWezYpLNzU9_FpnCN3nA7khpOtyJzh3Oe1J4Rymls10FZJMUmkkMQwrBnL9mG7NUN8phRnf2Fx34sgL_8obC5HNAEU4MH5_cIMjgjzTE11JYjhgUG2j3rSN6TRAdFDmyTjFfaLuO05yNKd87tKOfkzA_5nb7iMtL4HMaNt8X9mZlJZX_9mauzRUxg6oTLmjoEj7kpFxXQa0m56_zMkZNyDaYNlOIf3vSWLHGngoxWzkraUUHwME9NVBcmFKrGbkG8fEB-Coxu9fwK6DRkY3TwJueB2ehHqJQ3jKRK9kkX3IJ44RcjsFYH6tsRmGVT894EWmhHDCSVn0C55K6uXMTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-ed2cinQnHsgj6mHUBctWn7CHqOczHOiWMJB5cUfX6oMm1jWh848ZJvX-2aeD7X-7eEd3m15f13RyGOXTqlw0bHwdMx6f2tQBrpsHwM-AAXKkcfINluFLL-Mz0NGJQPjig2V5JW6GAK8w7YWzThKgNFcFE8IfuyapAUcgBnOUsZEpPg_RDMctKdJjHibmspoL87WULhfY1IR8W-fvV7eMSnL8Tit5iaBJWPhbAI37jrtaL4CQmEWD2VOTImBRQaLxMKhHgbhY8pq1rYPFm_8iHaiyJi5lPfuUOwSlM48Obfm2IdweVBLQ_FeiOnLBQZib2N-LjLKKB9-z6dvYkE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWL-bffwEeEPmun4letEUShPV2hUmsNUHgnbOfi1VB8nxoA0ymPKOZulT4WznEQUOVFpBYCHiRtMzpxn7GGiZCVmbdtfZEhzXnJUW78beZo4a3GCFfFlnpDD6VOdeDqw-f6nwDcOHDt6k6EY3HECDv8KIeX0y0cgnpwLylNEQiqhbq_RgX_-HuDp317sriSP8T0O09w23zBgNAjfRiidZArAQFDh6pm6QH-QOhXQylNPrP4j4L3xrFnEa3CM06dy8xiVcALKfTWvMaSLfEQorcXVpDP4Bo_5SJNawh7wqKPLPpTvF54T088fHQM8hd47sYS6T3SDi2VmX_sQE_phFg.jpg" alt="photo" loading="lazy"/></div>
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
