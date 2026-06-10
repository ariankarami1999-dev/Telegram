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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 01:54:22</div>
<hr>

<div class="tg-post" id="msg-936">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
یه خط اینترنتم دانلود میده و آپلود تعطیل در حد کیلوبایتی، اون یکی شبکه فقط آپلودش کار میکنه و هیچی وصل نمیشه
🤦🏽‍♂️
@danialtaherifar</div>
<div class="tg-footer">👁️ 263 · <a href="https://t.me/danialtaherifar/936" target="_blank">📅 01:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-935">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
دسترسی از خارج به سایت‌ها برقرار شده .
@danialtaherifar</div>
<div class="tg-footer">👁️ 306 · <a href="https://t.me/danialtaherifar/935" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 368 · <a href="https://t.me/danialtaherifar/934" target="_blank">📅 13:53 · 16 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 496 · <a href="https://t.me/danialtaherifar/933" target="_blank">📅 16:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-932">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
از وقتی اینترنت به اصطلاح وصل شده، من قطع تر از زمان قطعی ام :/
کلافه شدم!
@danialtaherifar</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/danialtaherifar/932" target="_blank">📅 21:22 · 08 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxVCtei9VdjHskVo_JvCZ_Cx5zrGUJU56NnrWVpTMS78PDQpj8gHQzSmlE7y3oEell0lI3VLRz2CoF4VP0wZ1wzFxAQnlqKBB_4A3GsbjZ30kyvaCQWdmxpWXAJ3AYVMZvWVnz3jqyJ_hEWyMjpmyf7ga8w7CXTv7IEwJvMsUw3IQ96ETRa9oySpPYsA0mgMyiqz2CD_K7eEGHkGYEGREsO0fJ9JF5qw6UYHEYlgHSUAAwQMz64kHrAVt8TG1INBSD-ioCktudLwK3PBrcygfxf-odaWbz5ar7JWfhrMeyIRo3EP7rqOiCqc3f-tUDzTkNwL6HKOSOrcjDJrh65o7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 913 · <a href="https://t.me/danialtaherifar/923" target="_blank">📅 13:26 · 07 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-922">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
از دیشب پیامی در فضای مجازی دست‌به‌دست می‌شود مبنی بر اینکه ارائه «اینترنت پرو» توسط همراه اول آغاز شده است؛ موضوع را بررسی کردیم.
طی تماسی که با پشتیبانی همراه اول داشتم، مشخص شد که این سرویس در حال حاضر فقط برای مشترکین سازمانی و اصناف ارائه می‌شود. در واقع سازمان‌ها می‌توانند فهرستی از اعضای زیرمجموعه خود را ارائه دهند و سرویس تنها برای آن افراد قابل تهیه خواهد بود.
در حال حاضر برای عموم کاربران چنین سرویسی ارائه نمی‌شود (و امیدواریم هیچ‌وقت هم نشود؛ وگرنه رسماً با پدیده «اینترنت طبقاتی» روبرو خواهیم شد که بازگرداندن آن به شرایط عادی، بسیار دشوار و شاید نشدنی باشد).
@danialtaherifar</div>
<div class="tg-footer">👁️ 968 · <a href="https://t.me/danialtaherifar/922" target="_blank">📅 17:39 · 06 Farvardin 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksEhz8V5yu0xnS6xTa3t_4HE0pqsn8kFoXVQVrRrnTfh-UUlpC0HVbRllqkqEKRf6dyXtiiVVyn12-DgnYohtzY6V7_dXzVafTki_R9Y1S7FR2KKPkVJwj4v9Sya50IMWMy08Neeo_Fr_rHvYcA3a2HuzIKx8xtCw6Uyu6XJAUBeeWmTYkVZRGnLCccaw5SQuyezlQr0wtSW9gSSIDyL7X7vSnc5QIKmIgi9rpJebKUeh7KeOPnLJcDQL56V8y_nz2Og1Eo5v9EVzFrJWTZc6lGba8YktM_aNK8G1YQ4bzftdV90P6SWrWESqZ06bbDt2U8HdQsZB3KQH1Spn1h8Kw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D97ZznU4Iuqqr_Lu-JAjjM8pWwW9xY6TkZdo15u3g-45Ws0EV-aYOXXivq6Qqp3ItkDsG0Vld_A5RrJUEw0CMc5TYAzM8Qz5gXwwDfiPjol83wpdsGW0KGOTRboI_449muNTvEcDwG09Y_AZ2AVw9lpe8t0KTQHy2UBto1xc32OsBFtl30sUj-M1A6MlBRGpPwDJJGMq3XGULKB7fS2yfhj95bEPSkdk0h8_vhT2MXbAjoLDxEmlskzxuoeW5Rto7II68CoIfqtrrV4SHbBWJJ3MdCmAL0vo1jYpTns8TTg0y4StVDW-FmP-uM8a1CyNjer1sRepeL_dU7D1HAbRpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMrmtHu89Z8UcgQbFzQgunlfHmmilL7ZkqZWByQ-doAnSmr1SuOzBhtIvgr0XhdYfeRGmNcYXWLQjEaoOZA9m7h5nWrfP3-qCsYVin9LiGYosfv62Vh0D9-Z4KQ3ylZhb8DWy3K2VfciUOCX0h2vX0R_ru-dDEjsLa6oXRWMxkHTSg-iBfYQhB-q8ni65sDBYrtYoFIz-uUWol0RRsRcuepfbYut-qI58A3BB3zz42Gfm67CqcaWYlOKLVprc5fXCKLZYH_mF347wpl9IMA0x4iym6xvd3lJMitr7ojVTfF4BUERd-Hcwdyq35ycPKsbyHpbU57F76L8NNBwkH9u1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNq6_CcpFXfk_njR5CanLYr4dqPLCost4huft-iCbfzsvOZIfJrJqEqTQIxc135xkykzoMXW5g65zZKFoQ6ysOZH0jBJRSIvkUIGOsJ1fP15FcddwmCZkW73xf51rf5PZpwTHUKuV8T3eSjgARs8pmB9Yg_xehM7ZMWlJzWXlMP_pzM6EBgqhc0lphCABETkTHqFWJ0IjmGkiT7EArJuSoAcKYuQXY5GORLYZBQXSbwPkxP8KKtOnsiRSfrqy8eBX9_BmEPd9I4e4APloaWLhHvkmCFGo9k4QWxu38hrIHInDixYbkrWdN-lgZNNPED1AfwL1TxC9jxpOEwrnvkh_Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFQwGOiCn3LC5H8uBgA8qLE1Bt-hkzOUHc8WHRZHKqr_plasOJGh6iBMzYtxrKlDlpo7MFx81LnCwAZaQlXZausI3GkRLTC3FFJbP4a_E91Fgs0zEwKNMuVngnM7wniMlEAH-QKIKoJQElrqdcOmM3CrEqQaHhmIAxnB7zEbwJVGalBiLO0F4td7LNMAYjf7zqyF_xNkUTC_Hmcw0Q7LnXKsc7qlpIAl3h8VewI7aQu83ig_AfxQMgBZQRE047Lr42m4S2MnpAfzuoUPJjWY6srT0vkTb9kHgSiYJuN3HnoDYqPV18wg_HybtsumhhFONoA4sP0O4jEQyuFbmJ98tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcBbYOjVZjcjz-h-fBrxoRsaKBBR3rUXeYgC9WIKSC4IzEWGSd6yXWLWkZzsrBJBEPfKwMpzFPv10kSLEHtmlPaujU2DCS-_66zZG18Mj8bunHuHBZvK6-mQX_7qsCJspW4eSjFWBG9jK4661wztUQpS888_OyvZbO2LuSuvydBU0e4_k4gmgPCXlCUmy3-ILAdZT-Ru86BggT1Ywlq15HP1lmmezQaLLRInX3Kw7JuIERlKaPMAztXn724aaoT-7_C2sPMJWIk2IdSXhXzzhLsX3JM6xOUUqOPw61UtvCV8rGOR8cm7KtKzE9e8P7go3ibIO-ftTBtPLGxxuM8z7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xuit1ddgo4FAmZyMEgmaQa3YJ4_Am6HViFJ8y3zbe529bzEcVXMxKcRsOH81zoeRh89p2X8fZAyduYgz8T7aRpoSCQBJLMYDfeWM5doGQu0DupeE-CyMqshPIkDFDevDsAUb29dyCi4kSPc-FNL0RC3nGhcYLoqDS9zXpmR1RF9hVp-0G0SaEgbll0HWJLHazgsTjH9fk1EnVI_usz6jVFGH-JD7OW7nN2j7U0BMKGn7VKbKaD376xgHZTGGbZpay9sgtZbA_NszPomLADGy7YmxvE1I1C5RNHYK3H34g8QhhcOgd7o2bHL01XTfKKJ0KmKKWywXcom2KfoZeThhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCKMkzg-gOJI_0sAUw123kkyPrkU_wwhAgwCA9fBl3FijIEYZwwgRMiEsNXEv2TUrzSzmr8qZrZcMj9cnY3-razB9YDwndkotkKz_-gqE_PwkM5fbRdjwYR2dRvjt5tTr7ofO-EBkjIXec2GwSSEsz2tnIIVXmZuJ6n44OFia8Pcqr37buy_JDS9B4KEfhldSPDkBrQCyjtCBI8MYp97-EQEJFBE8PeL7FAi0OKDAUhFxaD-NxN5Kb7V_2ThBHdI046HDfUNT2MsAi3oDHj0DJVVCmPMKIpXGbjt_YnqJWU_Hx9-eDVpbnrbCl4qBJv_TCFa9IOb5uWgbN2LohRFPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN_oMtIE-tQ24Pri8p_0zxpdiRw7UBNeOVCYDpB0DhuoLR0zKd2aRwvGN6xEJEO9UNmHJtbg0YfZCTAiLziFM4HF8dy7LSTRHkMrHaPNxKjhNPBN6r9V14xcNxrQ4Sw0xxOF8RDGjASVbZeHnsMQsnpZCcWvu4DQuputxk1go-lJbDBEl7Cg-rfPoyAT7ZNcM-2nj-25-dBG4JB1zE0JtnxoHS-Vem1LwO9hB_MhksahQISJ60uZsJ8nmcFoIgA1AB-OsDxXfjKabzfv9uUCIOXWXoW9rgv-GDD_KXW2ZmRdGW3SILiwehwrhnABnwarPNXtrcwhMkg-IBLXg7ac3w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3745059056.mp4?token=BZTFJ1zv9Fq-fgC6kkmCt7lNL4Ig9XuG8iFyuV3B4fYUoVxTnaOFzoug7yTozRG5OU1A6I53DIYbBatqCwFgpYJLMxCIUlaTKmxUDHByxhLmCKhQU9M-bYPu7HuzezUyr04Oan4iQp1AgPSkqFc_4_Uri03RBU7QX5BvXYzYi0vFoYpLATTYTgJ1aS6ZNQzA-tvePnl-lcMekcFi4EDDQEiuuFG3O4rTGAl2GHS-3YsXUZt0BnWjgUp87cpxqKVpXcDecYdccLBLtnlV0KVjoTG45LP4B_74cAffTbBbkBOs7PwyJcqvQvcHb6LY-mchv5MZH-DHpXT6PxOeMv688Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3745059056.mp4?token=BZTFJ1zv9Fq-fgC6kkmCt7lNL4Ig9XuG8iFyuV3B4fYUoVxTnaOFzoug7yTozRG5OU1A6I53DIYbBatqCwFgpYJLMxCIUlaTKmxUDHByxhLmCKhQU9M-bYPu7HuzezUyr04Oan4iQp1AgPSkqFc_4_Uri03RBU7QX5BvXYzYi0vFoYpLATTYTgJ1aS6ZNQzA-tvePnl-lcMekcFi4EDDQEiuuFG3O4rTGAl2GHS-3YsXUZt0BnWjgUp87cpxqKVpXcDecYdccLBLtnlV0KVjoTG45LP4B_74cAffTbBbkBOs7PwyJcqvQvcHb6LY-mchv5MZH-DHpXT6PxOeMv688Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDGnU4unpxZfV9m5z13LD6rm6iCxc15iH2s5A7uqimxx0fe5DcpMkVtSz7FnfYBNinsx0Pf9vXylrOaKbB7TCBLcajmzJNX6om_YwIgvTLXEQM-dAYWKhSdnNClqLy6KH8yuF1scw7wM2XWGyNuKytdi5TzuHqsn8cu8FO59v3NTukR2nxj_TDoyLpikflwPB-F5GfIp2ttHjNpJQEjXp13yWGm1G4XhX0-zCqxcPG6x6Ur7fdk98rS4Yq54yxbAMCwwPTwjiofkYbtnYWwz6OR8-kAZkkTlTK0SxWMAbVc9RSae5jeyLZ_C9toqB-0RnvKbRX0uyItdh-sZZG1hag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGdguVCUHuN6dMDs-GSlwa5oKI9qaXbbd9nEyqsBarELQJ6BNnr4_Bx5U6LrnUoS7jZRJmXfwq9LLXsdcuf0Zn4QG7JsF1Xp-8Gzs4WURCS71-JB5fza8bjE0XYyZxRSFTsUXLpw8BToRX0dc9bvVhZKMCAVruEO3xr0I9wD807H09fCN2j5zVT-2htAg1gYVFyCii4kNMiY9sVBHLPJFFrGCB4-F3RIr-KttWBfpdkgKp2s5snmt9uXgKiH0kfmun8lO4nhRXvIkzi99j21ua-hQsFK5jmxs7UsZ7eDX0rZacza2WbHt_gjAGYkJU85tFnhxssRrEWoQ0Z00nMH2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuurrZNerCBEQnygU_eli_l9ff_msRqXOzecKXTGRV6FbEUq2F492MszLAuanh_LtB3vgfVSz_94fugZayN9SS4mVuAYFiSIeWRxGmcoVR6MsCzGlpnrseG2n15uWxEJtTYQK93hZwJ-p0YIxf3GPC6TCOY5hDr3Dv6u4LvdrvyNWQSxfeZoP99EOwGP-MeupvcP7ahMKf-bY4zYMkJ_-vmc2PHJvvZv2VqbtZrIG1LZthUuAQAmyZm-hjyI5L3wdgvUBjajEE-h0wXjP98qcYJPr8LRoKOFuTnzaIfD_ONgyoUxSlk-970EKyyCRl4rvD8BteAdb8qbD2W_VeD4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pc9Pki0GDfy_ZBi4mGkcOIdHbrw4uXQtkgYi9FqiOuC9LyRz2CU3esq8mTjvNZm6NDfm1_pgmZUgR2615PnH1MrZdE6blieYc2DYJACSA_BkV6zi9B4OX3rbnPbTs8iMCRsGaSUz5qC1HXOiB0AB5DuvV6XjCDpUVR8RS1T5_obuK4RsOcy5mkFmDLWVc6Qqz1nY1OZuiTPzpwZUQ7-_hDUSIWxQN1CrHJKPIokh4zJZOvlYjD9JJuxFtG8AuXEgf7fbJ9jWiFHz2TnG6jqElBPw-MKXLQIGZuNXO5TIyMA7s_QPZXQ4BeBRj3VxBv4Kt3g9yduyU-vzdokVwrfHfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-j2XgTjhaNJNJ9kEW-twYvCyCAGJ4ZL4Zps_YPpVVMnGI70Mx7o-wmEb0AS5-MIE5LTKf6Pf-Hw8L54YksyEuCr4Eo1106b7yuvcoXaqeaz9v9QG9Dms8HQ1vg7jczqYunNKqryzKzDBRB4gatKznbeQDFbsoq0D4zQajxqptn9uaxFpucLhPa30kNVTsMq6xGBdWBGEY0Elg4rE7611RZ9ADwKILEh6wME_TvHP3oD-1V70ROl5UVHCijCi_6RgADGVlPDutukZbWsErk4mzahTF4n46UkQj2FblY-SKZw4D-R_x5fZQlc8HRCCGFj9imz-vAy92CzE_B4E10Zjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHc8YxaDZdRRZJILYUZP6z45xAldwlFnl7dRwl14yEQXPHENLbv13KwOUNA0pHtTs6tBhPd7phO9m1BsKr5b5fHjfx-J065QjP3AqeCDl2KF5Kh6BENw4nAzCZNnv53h-fyjSSxsA-U421795X8YHU_iTjcapLWhDxn8CJzvafq439VGAhcwmNRbMnNEXgYrXr4wSDNZRxXndNMAQiImWfzldJ-scBHgvwbsU5kxHT62gUUgIaWdvTVTkJBWeDFDzY-XZEIjSVQXgHIxWXQr1Z_xcmhSNwBHtCKpU_U2WZoNQ_ZIQxEOblgkTXixE-o_RLeR9M3MP6WU7nXiV0BE1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_085VqRvzpKhLPjIBDSh3OJ5ms5xFNIbEawbHpLOXtbmcP2j-17ecEhoTrtTf5RBPw0kGswPv9CCJMyMTYVJ6F_p5TpASG474VeJB2EikD8uXpNm6Ziwrb3cr_oD6JtGNF3JbShbcaWO_Hd5WM-e1m20EgsfWNPX84xMCekAF7_62X8yI91cM4W4kBAPX9giJYW283BRnW9KGQOOl7EiPBmLun27hdqJzi3fdr2E-nze8NWqDh-QEMRoEbqRdAWUlTNdbx5BMSPFnyTvltQC8dEwjMm4LaPhly2r-Bb1tNiG4VKIMWM5-B9QjxewBSAlEt7cEk67DwqNItKeJhfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UYYx3jctoSJvN3sFx05sw2bw0q0y8DV4ri4o7wZSMVq86Mkh2YV6F9FBZ_WgeuEddfD6UFuHtyE-UkorF9dsrGNSioRgGxSl5jGDirh7yQQo1dJxxX_hGktPnddo7LucQWigkM9OKowWGKGtFtyNzn1RA1iKUTtJ_GOiloKvYnwfP8Ymp7A_JmEpLW8GnFQa5ARqwtMetLV8PXC3DwCHgELJYuSlnEtSmt5LtDMMY75Vonrf1N-lhXg9W51SpdVQHfdkZa5-5H5D4BAJyM0-ltXRJGCCxU1FeuVv9F4OagboKEpdasho1BPCnxuELycuBTTeaGo9g85JZy6VeiA1GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPKy_3ClRPQ_K_pVrOvKSggqOEg0zYTDzGHPENJR3MeXSOm2tibBVW31JiyPp6ZoXapCQqIn1hopn2pPdMWTPOYbcwjfOX3niiQcXiZDHJ7ynX1LOMYT15TuMllSHF8eJzghdbMvRm8O2pO_RFt-RovRHVMw7whpmWWGXpK6kDYDLs4gh4i7lzIXb5rMhZRt_-umM96VsdraBjuvaZ-fpXowp1euRiaHxy6Lehndf0MlwjCFILwG8jQWzPPGMMRJD8Q8RdAGWAWEGVn7QNvPk4BP5SJallmvi1ArGkCqtoyDaNM582hhM1HtDTPUD0rQzanNay-OK3hD3sN6DTWkSA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5CdSQt9H-g1jwaZ6FJAehrz3v05eJ4MABXY2leeyz23Qp7qEJo22xyi6UJdtynumwzcVYAfWB50ZSMTojal2KgtmO7qCzD7su8yNDNNU3QIzn7lWZyBjsr-bWid1hQHmnvEa62fuCfaC1nXeinolhYrSbr5SSfQVJNw0eQNAdJddlQZl2pj1A98Jhyr77F1TOHFN1mm5zHndF_aPRoC1FeoPftHNOO_rhMLdxe8CxPstjUDXx6qk8P780E5h4ijKTxrxcHlvPABzqhDQJ5vLjfzivOU9KM-iE3D4kXYgbkvmowY0WSRSwifu5uiUmqn7K5UUQj2yKZ90omULF_pOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_ipzDAK__MfA50QCv8UvpGUFNbGRItuf0MDliC8xnzf5wu9a_OORtYddTxF-s3TzRkxWn-X_ZDnHNbmcIhnZfCBxLntMRAiOrAqVboto6ZdjsfY-_z7s3hd_A_zIPp2DwTPRlJlNWDP16B3eDor8fvlvj9O-Z5DyLn3EkXM0LKMK32tts4EJiBf92WbZPHAfKatpoCr5QkDGG1vOdLZQd3pNmJKgNu3IVGCNIRAEuzL_gjnjMUGO4Tm_5Yk3GDDFhRfsY92eXRtVt_7l1PTWYjpl6qWAuvJ1qrW7E4D1bzAbEeuqx8pm_rpU9oz_TBv-uhOYZu2Z8_KewjSfDOSSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNShSX1zCQDPZd62UFKLtI5h6Qz5lSXN_7InTjEYBdJdBZxoH8WtOV8du9VYjypBxNL6zkZlwHfl1Gub3QykEngediEHrASI5v0qBH_aUX5Yaqb--aSDm8D1J68_XTabwMd7HF4QtVBJF6x4AMzZTTv1jHkRY8Z-zWodu5S6j7iZG-rsvYSHcVGSRCPTPBKLwyKTEM1FvHgXvopGGE5YgPsBIZuWQrgGqWEiOOfSYZMzEuHdYTRO26gRj40jgBU_e6SYhS6RsrhkBJKcEoIOWJkXY9cP-TU3Jtw9DPJ8E_JeoiShAY8CMsygfdXa-K0h-nS1zZBCz2-wD_7TmUAElQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tizgPQGJkJooB_jZwWwELAeNZMw6wjYNoCv2_H2I8BMi-pccT80rk_maVfeJxt65qEddWMcl8w0rudvopmKNvfCJwPJ9ZNnNfSSZsuRGwfH4IcgLcNO5ljIW67-lmV5ySFs0JYlbg89Rg50f-gf9cabvhjEJSf76B54QYVAdjGMlYDqGCUpyvfWPD_FoiqVmR8YBlDe6qdLRWMN9Q0KJJNr3p0Bc6wJXitu0KTDP5eJZWFtK_yl0OjcoLk72qeoF8CMsz0UStoGcwMk5sKysIZXqMeO_N6P1NB5ee8_vMSVuKn2mIRrSSqU1--oVV_oXftA-AbdkigduMFo-q7Y1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jDGM8-1YMXFyDNR2rju7LEF2PX9Obv8139PiOPNSvbViY9SSTr2pBKbnrqi8SenFWfRB7GqeG1XLeINVGon89nyLuLBf05SgXEqzwQx-R_PSDgASFdHsN_-wjTTQ8V_CciEnLpSmMcZU75xCdJhL25EobeBdRolkPGyvTahuONAgMbyHjo3WDXjlePbdIPLvC2GCmuc1IkxVdOFqUgnyjkhmO3PGJO9mK8YlxVE8tlUfvXHEBrtF2jMUHldLwPz8xQUpOfsUA7thD013XjMjiKp-JwRAStKrrtAi3elsKjqd9W7-cTifKuwVA6VvyjJcv7v9jd3PmottfEas298PNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S57XgdpmbwofRRMBEQy7TBkr32-4l9jiS32Cb7uKJBJRTUVeWM-lkcSnGo_8IZWYbDupaKzESJXl1DwqZyKODH9X8pw723XhfwKoQb-a7fui5B1XnrzsI8BBqzMRkAYJEkLW5uMNMSYcrdkqxFwMkAaKITx556lb9vEs9rqPHQzZ0zN3DPqhcGDVRxy3a2Ts__rLoI9rOA-8W8Ay0AEB7f9C5AX2Amh3OzEGNyLik2SI_l-TypL_TjCTdwVHpotuzQMjSJlRhjuI_a1gPwHjSXN1nDzQqZ5cmHt8pmOHF4QxfCRlT2z04DOXJLqqy_tg9Z7xMVz1-pgXdsW-PVt5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RU65KtAABXtWV6ahf9RoULLnVOl-TwzUD-86eeFflMusKP52DnswC3q1CkM83a7BoL3MQPiWwtY07jufnfXysxkbG1fuJK381pKuKMVc5OlKsJOUQ_2RiWCFLNF1E2O27PgVvGC-S2qg6rCFOPF6mworuHUmDoL9vK5oW7FsoFU4Ea3GOdvtdjmUOOIBFjagyUcZDrJhiWK8lI4aYdJNmAhkdTf6Mo7-St089gAFdVzpPA5EAwjNorZRLMBBboILkkHVfRTANAxygDLSzjoEMQd858LKRsqgpgNZ2zolPSijSKC44gd1VHr1CVcDHgt-LOW84crS0tQ5GBVKdTf78A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2VxoTPCXsiSh1lckXfRChuxBSGd_xyPojsCbsCUAt3BzM454rUGafRwqrFN8NEUP1bk5w7SwOYDhkV2YHqkIYZ_NxEKcsjONhoW6GtIqhIw1P6va9Sq2zUsKQ-Vhcdlyxd0DWOc5k_2iCIUd84EiUj2cALLJWxTuKpC0EtBAQSQPAk8MQ2PFyQHUKxaAmd8XZhpku7Ih1-ehu9F7uyjZoe1RZ15Hz1iOT5UOOLjXVCmEFLvPcCpNkJCxbuPxHy-qsMzK_XG97JD-cxr4-4Emp92D5dgKI4D5_pJsLYIM5SHyWdkQoI-zrK91lFfqC-T8VUdE1gYTR5wsVGI4PphQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
سهم جستجو (Share of Search) چیست و چگونه محاسبه میشود ؟
📌
سهم جستجو (SoS) درصدی از تمام جستجوهای مرتبط با نام برند در بازار است که به برند شما اختصاص دارد. برای محاسبه آن:  1. تعداد جستجوهای نام برند خود را در یک بازه زمانی مشخص بیابید.  2. تعداد جستجوهای…</div>
<div class="tg-footer">👁️ 782 · <a href="https://t.me/danialtaherifar/874" target="_blank">📅 16:20 · 21 Ordibehesht 1404</a></div>
</div>

<div class="tg-post" id="msg-873">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPN77a6KcGxm8orlSKKO0iQT3zehH3-jX2gDTd9z-FnNLMhko6ZKS4-R7VyQVgKwqUoOHqgNJ49gtpvkTC6JzHTvqFvA0tdnuMfKT8G1t_ERf6aqmJcqrBZG2-xXqK_mr_Pfdsskdo3Ru6DqDFhTSN_7pCv_QXrIExneNiMM-CuZrJczhqoPG09pjB0HM6xUgACnDKfLX2mA8fTNRqIdi5C0fAOhtTMH0E1uX0ahMk_hJKukR62FaGzMnXM5Odch5oQ1lj2XtzbhHcTF_-gf7huJSjLIEwmr3dcMKZfOJP67qbuFqjq5GNUmsnWsOO1yo8vfr83HzzQOIW7yhqy_9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXNsQx7MV7d_wb3ZMZZp14MRRee0bvjimhd1V_07bb6VwnC66Q6Oi7u123AqqDFFXWVBWrmsV-P_HzYMjJTGhnY5C9hoffvFCyWBX9JHyXBUvMhgCA6ux2EuO5RjxtubAULf8WJbupe14w-16q5NPgvJAk_hRjnUb0e2Y6o38QYs92ytcA4UdU55d1VdCr5oSqYgkwi9vc2-0AfmMESsg6eIZmNAOIG-rptpuOHTnfvxJA86NIKxVPsIMFrin3gTUWnmoqAwVlFNCza7F6TYQEdn-4zp_MSAXqPN73c1PPkxjfw7sAopARfipSNUptNZMOwt-LrQGzIgpLFg6-GwbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsqTU24lZ00t6CJak1NUrAqX_uddmZ7XTMiNNAfMAxcjpYTKW37DUQzS5gq_myj8fAPgy-nWvJBb5XWXv4JF2TgiYrASJcXvLdR5HgqHa1zbjCRC25avmpeyxtMtvgxla13k0BiYXuwfDTYEjNn4ne75T_MhOIZXuXWbNv_ghWPv0X2YvV0trOV9JC85IoRea8z1O3wPsKvP_qDGwr539xHP3lBS0KK73G5ntPVoIfsUB8DFts73A9KIVB1Ny8AKHKhll36rC0G8Ib_T_QriV5YFA0Jp-yNtG3HqgrSqSSlB_oLAfh4nQ2cTfBMRitcJGAioYPm9AfmOB1NahApjww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzV5GXTASFMOviM9qI8spDRMuN6tgc8i9IkFMR5F6l89aDm19T2bOAGA0gTAPVsCm6useo-Rrm6dkWO9_R8Yk3tccVWAvjML5YJRVoY0YfeHX-ZoT1AOW77MG8-SUDVWrnhr98-3hZNBgGq_OOYCKs3byWH4q5erszBnaYgddPKRmsHisLrNNC4r-TEGw_3PfiDN6xzXGUHhrbmkagszcTTx1oCwRk7J2SDI9l_6zN_Q56Zds89OxjX_AM_1vizwXRrNUj6zkr2IhRk2-Ld2jr2XtLe24DocnLHgDzlX4u9vXdg5KFV5-8076ukCTRjQLi2qUAF51zrhJNVCTGYMiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKNXTGKuGFj1tGtTu7wv7UzsqH4x741IHHJd_YIuAzVe-2eK8QJWIbLYn7TgRn1O8oP7ve963PnHyqpSFS3qs_cKo-VI7MDc2Z1gVYFE5xT3ebQxKsxWkzKmzmUSdGBUmvfoq3q1NfKsOhby34u44Al54142BlDcuIlfD0GaAbMBO_1wAFwtyQHb7UVx4n9yHd_DS0JRuUgnKpjhCBDYo_XiOsMQHU6wP_eAa8t5vo69cMHJaBdesthPPbWbtHrM6n6TR2lXRGLt-L2TcKHXeBld39EAVAcpzdlBDOc2NzOJy1xDXLGd_kbuoB8tAA61jANYEN_P2J9wLnUfiAAXrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXIgxTU_S4Mjlm-aXzieQ4koXcUL11lvPs1bqJjYom30WUlQTqzZV4PP1UodGBq3RnLNxXp4Jio22crc3LCTrd-nUZVHR7Chbn1WVovdWj90FP3IAAOJQD0Ui_M-H-_A8cjv92OKNCbDIrn44NVp-X_6YNQsb1cDazusa4-rKQt3LGXy5K9In398WCd4f1SFBtYgTDWy1mf2qEJ7twWDeOo_qcuzy0oeFCBWQtPTewxX8MABfQZJdtPKhLT0K3QeYhl-bLyULHH05_WH2rC_ZIZfMEN3k9S4QK7DRKrcqZblv4Hqlt906qpT6fNHkIXvwnWYKFtPS8Yf2s4pcQQgKQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHRKbHesOLwT8_5RvqjNWsgXpyRQWNzYoh9ODkChRqBDSWly3f5NojDdTpoHe5i4TMOAWUQgc9XiQ_sGUXT6XeSTjS9MD-9-F6Jfy-jIuImXLOkXKDRsOcCLP4Y0loLzx2hjxbr6IjEAuLdrwrgRlzphdsx9fcZ6xAASZRacZvgVIgpiDzicy7JrnpWnEC6esN4ejfWmWZLkxFSN_mCnTA1-FWnvsWnio1ogTVg_AajxXtNHb3smsr7d3QhhLdHLkW0JEj1g387ybdBDJMPe1HtfUnUFsc-vak3QLUNq1IwfYgXsu_Yndt-YFvjdCroVE_vQParNNLjKOmKqn_60Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pdydUlxGnDZx8RsThMUrpPJmaYwG16UXheajH75fL0HtDQeKjuFum6A_qV4OLOgRFEXFn2DI1QVnQNbvzexymVrJ5aYhkO5pRK_bjRYXz0z3H52bqCwzkyNzSKfqdQk8k6Cr_-F01poI023q0VK8fvmYt9ge79v-oNwTby7y1KDfpPzdMuAMOFMORl8vtdCoHtxRl0LGShXowj0vwsOJXw22AcpiwD_8pX8bHoq6yaRZoR1SOA1S_BudgrgkBOwVJoAic7bej4uDB6Y8KkjXFRpBUAET7gHhds737Y8VhMfXjBJTQJThUoD5_1C570QTk3vqXA4d4SJ6zbZB7YvHCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JaRxYIGB6apEEsPG3im6YHpN1xjFULJj11HdYQPVHETz15xO7GPTO15SLfalRWj8WqHdHKPBZJaUb2i2XQhJ8gjQ_9ZprdqZ0iUUJ214nj6Ea2iYUhUzgObPVxjLvxuo4hCqxN0MeQaNHPzo5CVK8H8KT2XFBb6pBFWRuccruC4grkEiGCkT_ctdGSHGmr_JlUYKBNQmRMd75L7lQsB_NtFnjyFV4epyU_NI7SB1K6h7NL4aB8IXrIxJu2J8yCwrpdPnXxmxQttgblhdn21pFnCNHDTRFd7kdaifnRb8f2CY8iodwugv3kpd44BPiR2YYEPeMrXXYpvDHWtvE-cbfA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0Il84QB6KpGXeqJJzyxiQ_jAHUc6zLbY40TtXCJaGkC5H38nvQXzHgrsJ2E4QPo0dHZsBJ4nL-JTHNHGBDUD2Y-vymYi2t_maQy6-QaYCV27z9yYwpqrAuRaRpn4QuGreQwMV2NQTNsiLt0v7T7nQInghPIV7ahszILhSMv_9MwnL0-t-SC269Q0zUP3Al2KMb7JdcQ1LFQvuazXakkqaWEwXA4uP4JvAPh7fLobrZ_rs_fMyZ4wBDGDDYdGDH0Mu6uqfGbrSoDMMl3fkJmjb-p1Xv1r1ulQS3A9IzKhyLBRVQ1-8VbXiqsJOM_YoXU8O-QQFMzjTNpaLqS8vBn8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeQfiU3_g4dthKE8tDWjoMPK2pgKOe6F31k1BsAvSpb65aplNWhWTd1H4DAOnSsiR2vcl-VGAg5mns0dH6aDd4WUokzaWvOyQEUvbmSkeB_Xx1TJwKHnZDc3GI98ehR8hPsZy6P0q91f7hI8E66MkS5MEXKjEfBSAFej6AhiRNLn10MxfnzS0695y7ELSH82eBKDWweXVbkg_Ac0N8U6cnh0wJj6aaObE35WWAYTNWFqvcK7s5gp2Msr8zk8jgsB3TpIB36s-235pXE6fUbEvkN_sUjF8MkZeTr036mqguFf4Wscz0V6RkPb0_XY6zzDC7pM1gnEOeb6_KoTqud8ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gro7ywO3vY0tAJz5WjPHtns_P2cvduaFIsmwpBbQD5Hqvz0m_ysz0Vuxu3sC15_wYKpV16UR3mg2MFABIx39jLP8rhQMuYaj5vGaiGLSCOSXAOmMpgd_-IN7INJbHTj9KD-wHcQNGgkF4Sp4OTlbWsJdETKSn1m4AvsYnV4wjSTWjjeRKlGJeqI4wXql10Wdy63zhv-Jnwm93X3MN-KMqwqsNtr2YThbrrFNrjNTtE2Wn93u3WadmfkNb87_sfNkbVfhVXTJ5fR9E39naSioBfqEwuicQvsx-UVCYMuy0r0kvqO6WSia6GJKb1U4RZbAkJQ23PM7_2UfDuIC1s7-RQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzNdr9pTKV0zAsZ1KBebD5inlsG-WgqW6YR8K8ycpUf1naZcHJtNERGeB3mTk0xnUAeHT-yQNtl0YpY455cgvdjfMf0sDzZYjA_3qKXfOxuc3iawW3zrYQ-7QqgSuuxj4Vj2tQxEPIR7rrNjOBctGXsLc9C0p_RZyIl-4IqvrUiTh8BJCK0T5uqTCnJLKFrQ8yyNEzImTf4U0kwlXSR6B3EkLYkbaFjOUotl1_WfWr0pPTuwWCiV4y3gQVYDoxJJdL_bf0Cs5-JMGqkmTwNK5FLLb0lbur5JrfLorHnAFbbB9iHLsP7u0tFBUSPabHIvFuVumzwKo7u8hjVkPi2l2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smgfF12ZzUobiuxVKXMkp6nDcBWLISgTFmXGL7Rky2gznpHFwU228J9Mg6vxcKbNPIqu10WyfS7pTbIv2Ar7wg-O9mvtmR3w6wJWVxdfBTXhChr2rrKowI_Von7YhwL6wPvmSKlUWEs3sPVBnmqsyUhiRNb4Bc93wb3XSLqjRtJ4li54J16oGMYYqdH9Y4SoFcFDj0MNeRFQO_DBvQRBlFSat1aaQCNkfn7XsUVSWSz3NFwA8obg3bEl5CyMfmJC5BpLlNbdG1M7ukBbfeQcKGyMHXMaTg0C9lQEfmfv_R9nFbi7aoL0vM0ETdLl8n96iYSp0_MBh7mFLxnoBjFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgvIbkyhnGEnryJVLPaxG9Q7lPfhbpfMJEJb0K4QcnpHTMiDvGclwWp6GRGAoZ66ibYfWzDty7d6-qxjUcXLIlO9_QzomcUuCxWHM29ctHa9M-w_7Sl83iavF-0T9UVNC_BFccunZ0wItiGyV8pJzUck2zlVFYl--Zu-ORFgjQXGHMsgGWZYtR41cNkSkzOByKyHk6B3Kjll9ikwhliHSr2voYXUxg9kFy_YXKQ9tl9OTvvDav-Wm2TgYb1DwtZycPbjmfYhQYsvfUE-sitxCoNPQXh99UrD9pWBAgGLCZj-lYqqCZQK1oh2CsPhA3zuhFn_vxeW3twia6F9i1l7ag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FAWF4Ii0Djut7QlSyIZn9RnIlWcI4bqwj76Q6ZzakhvXewm7nHDOM-BtHFa9me8Ri3jws3yV4WgDgK3YPNfrcoZZJEnnkP0SUAN2cPFCbQaz6jNBNqRn1PpxTC9OHj6Exoor_fkLZTeVartrwZmA00fKHkeJJln6pOkSE_ESAWhstIKa_zx6E1KwLra-A_IPE77ExrRq7aBwPdNM6hdA396yNzp0iotwpO5JNXlxAceRmGXLyVmA-oKCGnTX6GYo6ystyZok8uAO6nMzYpJfpK6S3dSr6yARl5EztcowqPy7mGntgyOUVXvunWXfbUC20RsJ9ZkepYOubUe8hVzwgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/odOVtI_WNlJmbIsMSCJ1YpsmzSmn1tJ9vEieh2XCbq99J1yajLsnXsHtbWRJ8s8WXstUBAdzeAaQFs4s33mddvxgGZjkXpwfWZFGhylc7iOvqs0ELv7lJbJiS2KGeho-_sEo8x9XTI-XPzKAMj4n0Yfobhx58uMrImhdI7J-BNgBjqZIZPzRP_WYtW54n_BfgduJg5jj3MCJY3MbKO6U9oUKfj5Y47QlYKyRDg4gYEFaA70L1Xf_ULP4KpKm_ZhRRBgt5OPbls00VRJwgad-obl-vMDnMTj9I2nTcq6Y_-t4Xc3oR8rmD2dYihCDClbLWzvgNRCU-SvZnlat0bLkxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mc3-D1AZL7fiE4wW0KSRFyAIMm4sI9Tk3x1TOZ_oaGqWj2p8WfbqdeS4mTC6geuyVJ1vipb1IIkPLeh7zxhMOWJ5FQoTzrnJ49rqsk3XkhOQIyQLGygzW_xn0vLmRqcphhU018saE5iDlCeHJ5X1j9otGflglmqpziz0rFRQYa_DeJzSJiIKyAt78m6NIoN8AHaM6JnkBwjEQ9HoFNu-vTY7Bs95w_6s6Q2fPjyBXr5z9BPAkCAOiOQxjQQNYViGalRJX4YxG-sh5k9sFQiSysG8S47kfJvm4UH2KHAgWEhmrbYtp_r5wlsqfEWgr-bAGkqVqatWjd6vbKnzFBic4w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLToYMuL0s9vaHVyeKWlOTAUJubnTrh2mqLAgBqgoOA2-E2W916GyCxPfQ8tSS49EBOvzfY7ilpY90ij79vlEJ5PAsj4Lc3N6VAwn-CCbhln6cwgzEN45i5cpNluHoZaI94LUE_EpRogF0JWuoeQJfup5GG0Jlk0XDG4WIXjgDNRYrY-AsJO1gc3Zhfp2gm1B73Z3bbNRvoG5BkrrXv0TyImSooU7s_8Phg3vKe9TItx9xwfXUUI0v5rXqNMYZ80F1ljg7ogW_K9gKfZpIs9wquELy0Tb-v5npupA8Icp4c09csRqKgFO4Ba2h9GhOqzNyMvkUlkllTkOL-bCE-u_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f4qPR5OxpxbfYoM1jwp8usQczGjk3RTG999q2Av35WbM8n2L34qiN_NLgCb8lRWhF1Qzc-1azDkMkr3oV0sE_oAjaoTGeq49UeUSBZKDBUZwAnaEHgLVvksGp3HG0jpiP3__4W2mREdabbV7wnsr_EzYVNnlAIPE7H5L15tERQBD1CdJmGTj0_Od8wI6ayZwDDuKcbMTXSGjsu_-ACgCYiHsywewEUBkay0Dyajs_89HGhSUHHME0dnu6cG_4NLHIU97FHlT927Pp5oFYIktXaDRqYk_AjABvhPzsKmsLgoP5u1YYeRdwFnT-JgftRwxPMfcAkNoKb-KnRs6PdG2mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMgdO5rIXEgSUan6JVMwueAJqtSgMJ2KXM9CksYdLnatPOfcLBFRFHKFJR1rnODtrEHpnxSOQHPgti1rUsR4KV1VhN53sH7jSNv58wouGEbcabLqWcFN5d3aNIZJnFTlRj3LsZ4E1xCxJdOQJ56uueB3-MAI9SmLbVdJIr7r6Gvf8VPbauTg_dZMEbMd31TtWVfpR9M8EMuDdM1W0lGnbDuKmrtof-EWdukG-IEdjFvRX9a54QnJCJhS5S46JLqPMuIuQO0UpQ2SZ7mG9VoTdVMewplVmi8w1JTtcFoptb9yI8tLQko55cFpDinL6wMK_dgB9-UhsKfwwTsZhhMUPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0ZRjDNREvyHASpX8i2bCYx3QJThqcrHyeZ7ND_xa3ULR57RRBH60KFau33TILx_haGxRTGXkhzIzDj9smZQCYTuLVgOOdGYBCXrNp84eODd9safvBOKO9Xoptx1-fMcGPnUhZa51Xs6siWMHmj2_s27X2GV6DKWt2ZYqall97YrQPOe82Q6eqTkz2lgYmwfFVvO1RRIVqkuu8VDr5edpMKCPZIRhMHgI25xTySeUUa3NYqaQ-KzqkRCpjr7-rQaQf6UR2YeB-qDQEImca4uE5oq_GZbK04MFFcmvU_nKhT_wC793VsVty5ApPyj3H7ic4V-P3gAAo0DkhfUIUJ9Wg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RE8Dvs-X5jnWf16WnMttZ8QrW9p80ROvTfljltQ7gZm_LUEPn8lTqgdwa4Y6LG3penyCnNq-4iZSuSHmmaB_dpvhzNsv7Ff3eo_rLYuxbxEck5huG7OBj1pf_9czxqvT1F_n_HdTX-o8lhzGRO3yHZYLnUyNTARdZ5a4nNMZWexTax5ipH0vkRqVnjgtp2aDTtFijZbAERU585jJpKi2_fMgkHfHqTlr-NN6vmt5kbnxonJja7F8vsbyhMqoFsx-AWVKPJOdmIINzMS-TR9LkVsCOxmqzmgd3AUw2RoPjMHlgyMX1yCOvADwjEESjmUfdtxF3NbwCwPTqm30fGyMcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jn4cSMBlz0T42HFo5X0lvNZXzZbPjVpz9rZ_JuqOdeaIQTstwWY1B527wLJEHqf-LQ1PFLicqM_2-sZ7MqVbcmfiPytZej-6yVdwxGzmDgpQIGux7jZCt1yFaij5oAyciYdP4gRM13xQb7rfkBkhsL-64XFuxGJjkl5Olrnama8qS6cCo1gUBTpU3AHXyHXFPv3Wutf3KDfXzpfiSN6Lof0LwqufgbI1y0H0Kibddyn4OXmMXmDcjimm17jcKGnStj3GbYEoC9FtliuIr7WPm7Sfd6ALH7RHBlQutXYaX5-aGzf0cBJYu-W0LrSZhIrU4LYC-d4MjFIN1d9sqRIYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aDB1pPknONISWITr_wXhddrwcZbinwIj_WncPPlVXyUDIYsCcXySzpRg7OMbSWJ7PitB0pQXug80kVXIVovKgYsSSJR5EPCTP2Iq5RzOybgXw73G73PFOaEGs8sqPejQTZFcyjSIcEDdgEJSMlqXe32OSOv2prmunbyWsWLxtqnkx33522D3GZ6-_lgLlvtgLDjk1eqkH9ESKfsQRoGDQoXiYaakkm-5OKuwr4ZzFzqU_7xfhGwOLc5jTxb0egDQ2NnczzDXeVmMmMOE5WPH56rqyE7ODi9_Fpv3-recnGQIKf-8QV1_EwVhEnnRxTFhUtpfv7Fmbnwm9fd92pEJtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBUjnbP8PY3m3ZOaMGkZZHSkLArHiAbGY_hWdqnU7IdqLJg1JvAXPGZLG1tE_EUsWoY8hJNXw8OIHoi7JlO03edHGrfvHJ2L6uCTEwGIjml9qQ55FQ_oWgQM9qeaq1Rizs0gmtNGMDR-euGqNif4SO7lDxH35vb3aYBpamcQBwYZ1WNlaJD_nk23-LL0whbwKsjDx6P96bTSIhho3vPSWHvoF0vS8Rw3Mz3399f05twGzY1PJyGYVZLj8X4SEx5k5WJsFjiQXbglIDVANBoRPAp4gIpBhA9jTfp0Lk8zefmxNiH01TNffWSyuz-HP4BlZQR_2EybOpMkSRwe-FlAGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ftrri1ZcBZTaPBUcntCchQ4hziAzN417mT0Vkw9MezmvPr8uZh6xImrXzI549ClDCjuz9uwoHu_d23itvZxpWo-3xcf3bOn9xHzOWf8Gq45Jh8J1qASVzThDBUlF6Zz6ZCq1WyI7NZQ_bjzabciwu6PaI7Gsu9AVbE1STKTzsJH7aUqmjl9uA91o2fTM7yJ9FbqQInvWjk6_jwLuUGbq5JaBCojyeYlmedG0GLl0lUt1s0GyIgBjRZ7P-M-DR3OMr-Wi3u5dHtm5DJsrHEUsdpukgh_fxtlj8_xORb6sR7lCeQOdbM7zzZG8nLqXmIjA8m2X8B8vUE8DE8pBCo0unA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh59WdFRDGbifaJuUV-7dncWq8fEN5dNQ4g2dBf1XYwwV7ptBZXi2Xo2L_aboVrEFw1aflGENvFf8IDH_h9XGNi--VLK92mTUlK6hp6kO294dNnAAfWSKeRiY2ivy_T8N4Cmu55X8DUD2Rv8Z7VFEICxu9ohx1GcNWN56Q2nP5YpxuB5efmaj1rStjMJiHRo3h2QBHKV3Eby6okk1De1K2tHivT9guTW_Az-O3DH2haPPr-hMvACdCkuFe2crl2RdzVmFpkgUXZJ9gdb57ZB4Kq_tdMZ15fdqFI-kbKETVXfVhTe8KJn80PczSqve8YNjKKhRZAlxWz3LT6nOEJxxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5I4QobxHUgD5G3YlSEOiFF11W6xpDHI0buiCDnia8gvysPmDRCfOzu2hFAmA_GrsohESUVW_mScAaPgbLPSXBr0BX0Lz3i-nh9u1B_Z6PAX45r-iZFxtcih8CiCPVZeyEnPVpGOlp87rvSxJnMp6PvTIJXTzKazPyfvf6XLWIirO00qTt3gEGhJQtpXHHmxCjY9jNlP0fy8jMAMR1uObRIDxELju70PV-x-EszmZDMTHjoj9EA-LdfqUDSacXdBKfnJ5cMsnbLXtL98_nWix2HFA6DqWB9_rHBWhWFbxHc9BtXr9otYhjmC9w29FRWjBbMde-5AsMOcQl3WdlhY7Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/6689285f08.mp4?token=TSovFvMKyTYX11hHdSNZkCrFrfvRdzW9NcWL4_o-LBVqd5JBMMOtN-HcyCwQeAObDWLW6nWa7CKiIpCy7yEJOIg34NUVeZ9_rkH7duiZXoueDGjbiwRLQcoDhwm35KdP4l2LLscdv3R2x1To2QOBNpzwjnGRlN6jJ_mQ4KDgL2jOrZTowRKwKtCudqTZMCsWJcRAPbyeeLB_Ex15q4HLp3MGRwXu6YB6Dm88K29L64R-YOCsFMLTR_wXFdngwc4qx3qOd75FgfGGbcGkHdRtixU0m9fGAZ_PMwBe2h4ifuMMQnrXND8SRqqPI9yx-ATNd1zWOwYWIawl_IanJcliJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6689285f08.mp4?token=TSovFvMKyTYX11hHdSNZkCrFrfvRdzW9NcWL4_o-LBVqd5JBMMOtN-HcyCwQeAObDWLW6nWa7CKiIpCy7yEJOIg34NUVeZ9_rkH7duiZXoueDGjbiwRLQcoDhwm35KdP4l2LLscdv3R2x1To2QOBNpzwjnGRlN6jJ_mQ4KDgL2jOrZTowRKwKtCudqTZMCsWJcRAPbyeeLB_Ex15q4HLp3MGRwXu6YB6Dm88K29L64R-YOCsFMLTR_wXFdngwc4qx3qOd75FgfGGbcGkHdRtixU0m9fGAZ_PMwBe2h4ifuMMQnrXND8SRqqPI9yx-ATNd1zWOwYWIawl_IanJcliJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tprcCJtQc7dPEM5XjGW-N8CrNKHKk0CDJpjABNgq98XBHD-GgwqFyByvFxvu1RZoTNEjld80NaZ1rR6H1t9W35B1jlFVW14Rp-1XcI8wNH19YJvNT4kK-O3VfrQDDt0Z_3dOZB8KqDoFelR5MdRhe9TisgewHxFJ_84Ar65p56e9zsqndv9gzy0POOknYl8eP1VM0c4V9pA4MQvRCqPmqzL8Sn_XwM-WqbioQ98CDkAJS-h2jbt7o6HnxQAOcpz60Bzm4bPmWMlSjQdGgpp3g1q69Zd_uObXD2lLBOJUpVSlzJDk6JR7GHutlzOduChpr_cKjwkKfNf3vE9wusXazg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EIAwsQ3L_pyfLQFMq8hlxK_sN8bPBIiKtnyc-SC6VvSl7oB3dSEaxWVqBN1h2iO7J4EB60D2Ka7i0ZWu5CZnYQVENNeruxqB2Yk1AMYQ3S-kDWkSOSiP35JT74M3wohhcyp8qJehzqWleUsKFZN9sNhmBFlx_t8ENtO90_3V6XHK_QrguAYOTgSzcQ0e4BMDWDWAI3qk9MGsEQ7tWQ72UCXKDiGM4V8QP6hrZrezn8_Do1ESR6lvd-Tux53GfSLQ54CBj9ObP4PA1o8ckaFN3dmda09yEFVo00wWqJxTnzX-degUHXJHCq-UgBjJqu_mYgT3Nqb0YQU760ONon6iuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bXdLenizPtjw2L8DNWJdIfa8qomCsvUF8LUFUsfA74bg9JSJD5j8O019eF9qNkyJV4kJ088QzzWdHcv4iPaSy7xkhOpoMjA_h-Knw-z1B3A-XKwuz_6xZ1XN8O088dctXUjKEm878doPYNzDESlczlur9MkEkSNqr5QpJKmqrD2Wf5HB4V3IskGKlH_jNkFPrKZOhZPOQMRxlOVxwLp61sp_MWiHoSnRPA9AX8PCCCP05wcVP0YTbe607WRDvle-8eQ2JWJEnkgFc21L_5Y-AdHmmJ7G6HnKguwwHx1iFvQmUimrl4NX-wov65UZ3JDPJbBLGaNtCBTmeTDgjalOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5kiiE89Lhn7p-O9lQUkbbA5zw0UL4Fl45hCdw8FUNcIzDriLiOFp9TD24Gt9sl4jopdfZxrA7fagWE-OlQZbPXWjgHDUEmZt6g9kyL473DV7SeSHRe8JvCD4g7cT5Q7g-qLuidmyfaYxhUj7mAFVesZc_sM-zT3QthBfvcQKlSTlMdYwSpOTtUF0FZuraoxWUUyz2ZJUBsQa1NVEJmKixebyM6KNgHTOlYhMiWeLYlDEHaEVDeCBYAQu4pntFW2NGerF0YziCyHhyrLQ3rXTcmKhTSzSLP71dcuiVve1DZTbFxSbyO46vEKoTSwao61k5C_R0k2xsBfoDtLEGuWoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uulePKPCmTiwLXGgABbh0E36ixwBLxfv2aupBhJ_0mLdMoI3SfZ4WevS5gAGS2xxlZWj-pm_6E_e-edQ3nSKpt_yXWGY8o7zeXclgMgPTKB-mtYBEBtT7VtlTGspO9aU6YVwTm4mnB_nWpLAGly5K4w4nQqUq9QTCL1vSIhkk-7iFYp_8FYJKyr7Nx3F2N1Ju34CV6tArnwCfNUt2H4lb_Uf6-h7yh_LrF11HPC8HMRX6A7gp6zfIhrqhM2Ao5oPkItIRvGrgrCj8Ie4mSxpYEH9wrGaKgcXjOpfX8EcK-xxTdz9buDHADcOIYNH7Ij_UgZ61jZjj_pYrw6LjEvAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmj-VhnaHjuGTSS27IBsXxTaY18yXzfEblfJyQb9SI2kthAxLay-oEzJpUrIb71UWn2Jhku3CCtjclt4PwuGRtvh3Z1OZnaZdogeVebFD1Ff-eQAj_kt-aLp5kA65xVw8PIgKAqtbr7PJWgwbaLVbfOKjtHEvsTb9itYbizIDsxzZj4ePrOD6Qqg3gG_jRruTLQGAED6UpNfGmHUMIFvWhdm7gGzAe-gukX-FqpsjvECNuFolukz--tjtJtXlbujgf-ipvLmrRK-WT1akZyjeqjKuVB9t5EAIwGyxXvOSJOHQJ5-4q8sdCc29iRH2n9UjHyEQvVig_sXY8zRaXoQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VksnNLp_peAOpztwBYB7yyIseu9PJ77fkzOENvPmTpBEPpArYN0-swYBM__4vzp7zENeX52z4dy-Xy_VxWa9HpvUuE0CjIlLN16PvsTweJmMsb863i2rnCQU1iKfYNIfhodIc_TxaHw2r6nxR9JN-WhwGjf1Xn1kOXj6KSkI14VaO1DfbRjKVuVB2QvoURDajQbXLGtktlLGO3fVPpEvbhk5G_sCqhX4TVo5D5kQ-uAtBWfjy2LW3AhfqTXKvMU86F1tFySvFHMy2FOiFswo4CaI_5qysALijINty8LwdvxzENTMO5qFBtd2aKO7H4iiZ313JuxRuzV7ND5ysXtApA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=jV6pXsKhlcswwkUv2t7Ine2sn68ONlinbJlq6Byp6qe0v6B75768lP73wcf4D8TlZrJx4Pt76S0f0dp-JL3T9SzeWHuixEPZkQlzlhhZlHWB7l_1XLnhfOeFGyDC7nDU1n5pfD-yjjN-bSgVUQ1SvloB8HyaVMJo0HeQCTPtZqNV1h7IB-EieuPfo13FgBWeQtCOARl61qVKby5_0UpDS-ImkdnwkYPgH-eUOURCr2DIojA8AJvYAf_P5BaN2S9yfAFs_qgu8bTsLfpjhdKgdAYOk_-w29rKqhp3n2JMP3Y1fxSNnCYgIW71MTNe5fdmf6wSPNUCKl5J-EbuumXzeb4xXzaYS4HBHaHEH918AjOT1se1zsHDQNuUSwVAxoqBDy7UqbS5e24PHnK6v5r227ST3wyDQ4KByp4lFmHn3nKkjJi4cjnk8o-BXtrYZ9klwLLjELzfXe4emimQAq6NbiD_tBACyESsehzcmPgqCGndpcCN7fz9SUzUFNwqRujrL1PFiZqBnRUJqaSgIPeR3kaHMu0aPoWFphcLoMJCpYnFi6CppwOuWkyvzcmNAVoan0Dnkvu8BW8XfhvsdSOlScM8TlN23Aoe0X3fEEZWen_hBJeKPNVAn7ZnMtz6L1DqIH9VR13hzXOY-8HSzMDNspxA7sJ7PL5mwvp_MdA0MTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac627b8433.mp4?token=jV6pXsKhlcswwkUv2t7Ine2sn68ONlinbJlq6Byp6qe0v6B75768lP73wcf4D8TlZrJx4Pt76S0f0dp-JL3T9SzeWHuixEPZkQlzlhhZlHWB7l_1XLnhfOeFGyDC7nDU1n5pfD-yjjN-bSgVUQ1SvloB8HyaVMJo0HeQCTPtZqNV1h7IB-EieuPfo13FgBWeQtCOARl61qVKby5_0UpDS-ImkdnwkYPgH-eUOURCr2DIojA8AJvYAf_P5BaN2S9yfAFs_qgu8bTsLfpjhdKgdAYOk_-w29rKqhp3n2JMP3Y1fxSNnCYgIW71MTNe5fdmf6wSPNUCKl5J-EbuumXzeb4xXzaYS4HBHaHEH918AjOT1se1zsHDQNuUSwVAxoqBDy7UqbS5e24PHnK6v5r227ST3wyDQ4KByp4lFmHn3nKkjJi4cjnk8o-BXtrYZ9klwLLjELzfXe4emimQAq6NbiD_tBACyESsehzcmPgqCGndpcCN7fz9SUzUFNwqRujrL1PFiZqBnRUJqaSgIPeR3kaHMu0aPoWFphcLoMJCpYnFi6CppwOuWkyvzcmNAVoan0Dnkvu8BW8XfhvsdSOlScM8TlN23Aoe0X3fEEZWen_hBJeKPNVAn7ZnMtz6L1DqIH9VR13hzXOY-8HSzMDNspxA7sJ7PL5mwvp_MdA0MTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhQE660ovxUDzZYGoUayMelzugVuUDZO45AUwtPzfx4T6xCcOr7RORUGKVvdLE3-6pjMB8OtISgOSWV97G9VMNL79kv_TMWGzBbimZJmQoCzE0ggWap2lqm-urVw8GSxkCt33OztU0plUCUJ4GDQ46r1jLTnD3U_9NF5FMkAue0iOQRtt0kW8ki52KE-FfJMCpxWW3xKYVrdux_Dw29y24PN6vPeSxao4bdV-8vrmYgwdKvBW6IykEicnZAo71L-tBBtGUxyUYnQiWIJilGJwiULNFM4r7DHN4x1ep3L5eUZzkH1z865mUikOhYKZMvF8jV0I48O6iAbEr5Vo-Xctw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSSvDWbfZyrWuoGPWkWm-qQ7oXYQmlJ0AeWY-EM9KUAffpUZ1bqd8_gFmE0SVmuUABm7YI6_j2ci2n_hV3Q7WL9dEgTROazXkbA2JSOcqCLm7QeisYw4Wsy-YdEf_v6GJrATYPTXhzSC0qFtxcsar9Wnh1u07pF7l_pSlfTCE6dH7nCKXOz8hgE64hjGazWcMS1JKb8UfWeEKoKM89opCOcGGtP68HCFJ_AnkL1pfQaDSnr0hv7oEDUzzegma4Gnn0-4-hEfLUl4GRMdbK-hfq9a_s9aM7-ZG5u0C8UImx080H_hLcEsI_YPwrolAQyis6WsmhNCX5bIb1EmggQZrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gvt92M-2e9EMkVSZTleoOHByFO-WzsYdjeR5gB5SWGHO4f88ph8MWShx-pMLtuEjkHD2yoP0gKLFv9A_dGJt5U2XXFbylxFyopsROdV4zu3md_h169Xy-ZCOy76c38nRy0Pw4TCvjePhc687GftNdu7DC_XekbqzeZJfL6qYKwnkoHcHkqS1TYjTtQW-Ufo2dmXOV7FIgCGDmnjk_i3Bv6IrTSs1n6bQeD7rp5ggsAzgVCVSjSuy04ofLqcbqgQM-_lduPFP9uwGlQOHxnQ-yQahCSOxkJlI4xjDwGGTF_F3eIxNWpwui_-EPynqULHw6aGVyGIpp6SojwfdAEXAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hHNaiesbkXUTPIQGwLHfPzffVRoKAD_RFaJsuXCAyHqC6CpS9B2PFeIfjzJDqC5gCfGos79r-9eQj_K9SakHSCzHFsPcLTL9zv5tYYxoDbuOMdJY0DONpB_ke7kat6l0_A2odvXMIrhtbIM9JXxZQr24aBvHaflYzHrWMflfZ7gPne0PCINB_tqXDy0JqnN7DBTl-ulSG5ibJgYmND8llR4KDUAYg1DmmeL9jxAypvdtRM4_gcR4vw-T4K18G4yRWfxMTKDy-1qAVaDnpDophzoKbpOq0AA-n0S_7Dq_rECOds_m9r8xYKevujAxiTDPVPZJj0eR8XtwB-_DtVuZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VuZbq5NIRWsLErGy_PeEOsTt5zQSGqq9OTi8QGG-Wj1q4xHOvBLFU2SSGGfQCWkqW6cNKcbMGJ81_mPavoKLNk__SB8ppkATNcRNc-H1Hto9hyZ6CtOlpYb4r-XaSacZ5XkZ6BEtqDv_qL775bhEH3n1B8kwaR9gll7CMOKZCLen3FbFVUSNpgQ_zRKvVR_RUTCXUBWKyjNvC1cQWsU-Vtpt62rn8MyC1Zcxwey5A5lhbt6ZufmxvDweCEflXtesKO2QRqJr6hmKzqvoby8308DdxUjDOIxRd3tWjrAZDYh-7rXRNpiL4QEYECFgQnVO2NwGdeLbU5nr2diINMZl5Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0S8AV3vCdADTOM42Izx6RN91W4bLlLk_zHybl78kkMXwcni1Chn5Y5zNJYXDckT_l_K2qrGdWa6Zda2l4NTbLF38pBUV7_zW23d7S0QhASORXCpZOxLkXZzSovoaWCnCvwOXgQzx8Aanyao-s0Dp-KHjqogdhSkRLgyMrtqOeRrjUPXfcTa7rQe377Mqq0tKujhOMeuArIB9PQRolwtwOjRnDeYajQMb-nRguUpvDcU3JUxqUrGo3DXKlQGDBi8olbxbE0stU-fO4S96MDAVmxBB8CNTpyx7muD_AgHxCMW_gHysC1oX9myGHoMY8n7-YeHpbPGwzSycmqunUdiWlxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b061b44c.mp4?token=Q32PofLLWu3zCveDqhzZa2cC17jdkYMqysLz6Vwy65ApwMrAzhNoCW9rcUN8iQFliSi59o96RuBwoOWtxLC1fkJ28YEli9veFQZu1o0sj9MCaYGlrX6V2AWugvdMLV0vwI93XKOJani4E2Hu0hNuNIQzGLRPbuAtGEWbKBvt2bvEUMBlanwK7nabOweR5cjsXTc1MrpelqNpmneoYoLFQzSwwrEdFpGKfLAwkP1GVt2tMcHaFTG72_2Bj6m6vp_QtrzozRFBx5T5Y5r1PfIq6NROj2lfaeyXtKws0yPCBB2nzUGsTJs1DWEJYjyXBUEVzAGIZOfkHIHbZ7FPqfqw0S8AV3vCdADTOM42Izx6RN91W4bLlLk_zHybl78kkMXwcni1Chn5Y5zNJYXDckT_l_K2qrGdWa6Zda2l4NTbLF38pBUV7_zW23d7S0QhASORXCpZOxLkXZzSovoaWCnCvwOXgQzx8Aanyao-s0Dp-KHjqogdhSkRLgyMrtqOeRrjUPXfcTa7rQe377Mqq0tKujhOMeuArIB9PQRolwtwOjRnDeYajQMb-nRguUpvDcU3JUxqUrGo3DXKlQGDBi8olbxbE0stU-fO4S96MDAVmxBB8CNTpyx7muD_AgHxCMW_gHysC1oX9myGHoMY8n7-YeHpbPGwzSycmqunUdiWlxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHYvQ3VgmMmd9uO_G-GRw2YKXkzdaSH-GiFGbbcQr1Los-qCV-DJbMShgKVjs9_iBgdmp2W6pGvndslkU6HptOI89wWWu8xe9jgLJxd82SIRIcPRNYw9YR87G1vC777k_SrxI-yD8LqSp9LThDjlh90yMVD24iydeZ0T7r3fH3W6HctBDb6MVoNUIY3NA68z4f5Mro5qbFBez0BtGHKKPzBw8joqXcMM7wUobA0OC7Tj8P1sGRJORYzMs56EzO-3w0ezaIo-oJxIJtx_5rP4Uc4oVO86_UHf6Jn3BSVhLy1Fy5X9QBtEYXnBXiaqmeLe8iX55hrgTFeA5zaS6oKWgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWyBjgpNefGvELgCSMF_3quuPR-FwoZjaYkse9kVT-nVPiakWyl38CM7yzIFQVXco8QJlgHFBY3KfNNICQVngPF6vhGFMs-_CIt3tyNFlaPjLrr8wvktR9z3HNiz3rBZ8u12KMVSI66v7ULOoVSJ8BsJE6YdcjUQmkoMDL3ir4Umri0REJRtRxDKOwGd3j-yaZKAIe6HWfnWWN_M93jYHUdQPWgOriL1SNqllnPDIFPjmTbPzn29nWNSDlCNSFsuxhagwlkrA4Wx9n-bROHI3td0byTnyVCsYys0epoJ-cXWWn-A7_jJIGjsAmcFxzzsHzhcGIZ-4UMupV8EllQxFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4E72YmWv7FKh0TH6OJCSAtfZpuvG3DbqI9kRkOBBlRvDbVso0dNMss0HNx7iYuunzLoDyuOgOMRgiGqN3FsToZu-BT8ZQuUpSTgTVLFZz5MbmPPJ3lUyLlcQ5KZ_JlttFJ92v4MZvP51Kz2IKhr7aez96etGdOXBFcws_lHzLgk1mFPXPDWD9_68PghlI37O8xAiqB9yINutWsrAM0_AuzDW6orOE_RiQt7bmByk84BB4K4doEQ5DyFNhBf6wlTb62Ramv_21Y1hR5RcFFvgFd33QeKPghnme5NyKkQcIb7rQZ169wP4CHyOwXIw1ZHsELQROXfL94xC3L2L8yMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9gDQmJ-SJEmMyOUdcBxUnFq597CT35arDswjC81SrT2VcZxzUAY8F1e9_xM87eJkEkcuc0KlM6TNBSw8t6bONFUdD5txjwxr9SBxRB1YXbumLKWVKMyOHiyLl38yIp7NhohTNCmltqUqihm3YYwMAoNrEPvjtTSiUUj9ffU0uMeRWRf1AW91m1dCsMRmTMWTvZffLI5by3cZ2Q9BBbRadsqDzVZuc2iDDpSJxs7xt0Tw0Qy96peMedsTAMmqV_1q3S_y3s4lal0Lpqh1JJkWtbddWGRUs-7fk-dPVmczJDgqEgh_cEsekHAYWeRkvwUCaz7wMmdPaoqnKKA5wpuDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RSSFzy4utOC2jgp5fs6xCmyRQKxUXXFrj_zhtRQxnfY7EnTf5kJsJ4p1jxjcR7UCUtILKav15CrOaGJSxueNLypgFogmaE_bOc7GELa_eGsg6wqly_NjJoGlyEjFnuKoFtVgnqjcJN1jomvhBKlD0WX8CGDsXX3Fr1_KRXG9FU4YFZiWUAyiEmSV_QuNKmO22oTMKZ9xah3e7dzKCHkxR92tJkNAkyspTz3F1tO3c8QOr0GUDosrHIYuWOT2uPzpEoA6YuakxYGWk9A_ryrxNmGD2Nzz6wi0jUmyjTlXcn47xjU1NBstTYiCDJzOy6tG4-OeNuwCIvQd64uL3O2Amg.jpg" alt="photo" loading="lazy"/></div>
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
