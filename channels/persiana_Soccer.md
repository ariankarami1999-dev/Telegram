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
<img src="https://cdn4.telesco.pe/file/F1dfKESAjAemtbSeg455lqDthi_uu8Sv7zOHVzes2MYBco25llZ6V52_JhjEBXRbxIH-ExbRFAYpNg_RzzYorGzVPPW5fqdXNgz_WrIcUKUEKDqfKF1Jx2PTGnsmt7cmis3qD71IFCaqI3JTjKgatYhu3rrWsjXFV0QFpUwNnnlqOfTS3OpeukYbaHpRgGJ4qx6M8gC5BDbu74k7i1FfNVc97SyiaXn8xz6K1llL3eiNbGZ08yVa3V2v7IvvRrc5UQgaWATUjlfWadVydeXIvhnVn4T5P28iNlUS0c0oOtS9VFyIszuDKdbTzE8YOthZa-I1AjQ9OY0a99_fzlEUbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 353K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 01:43:18</div>
<hr>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7ul91UFSyINwoTYKKR5X1u9p-HsjLjVA8k6bJVaj7tq8cF6wH7d3J7YCGCIeGOMxU_0hCEzwh0qPwKoIlpTg9vxZeGm0zR94P4KfkCqKQpLDKoYiCa9U67Z2XBNqu16FP3sf9l_sZrCZw7P7lxNagOxcTxOiZEWHSs8AhX4xgR9gkCBDNl3Nm9V_uqbVRlmY3oheLxg9fbJTZpCBBnZ5HjSjehI67plV0J2yZfssf4lsk447cG24Oy9feWTsObvAhLsrVIH0Gtc4B2fI4JYxF2Z8IF7hny2x5GZu_WZNiHGUAFFp9RdLJAXnmuV_FLsTHSWS2f5CPQY0WYxLExuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy8PnP7gG0nDb6HTT_pfu3WR-x2yOnuByrJzqUEdZznCPPz4mqLipQt1CE2rA04QvZ73u85TkCts5nrMxdV6LnAXj9fhjBcUL01hGcOnX1vNuVR6dj-pozWZ7CXXaSkORxBI2UlaUoqHyzOdIIrOpChWUsQW2cgktQS2HfYlvScyyVRDpgfLrlcY82l05WKk_h6AyXULOEJpWXDCRwNR-_rapAlneoIc1X-Sc5zgBHnx8KcEN5yb-sbO1gF7VLKFfIbJUT55DUykV4OXgfgjlmptpAx_2KLLYE6yKCAZ0F8vMrPcTzYv47XTLDR-wZtA6TolSiXSWvoHikfKjorqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzOkaN0WD0ZfIuvuFJOxJsdN4H1k-TSFgDN6Ihgizf2ICD3PgigN828hIM7gH6NT6TG38l7Bw5nhn7fN-8R5jhTjgWof2_WWF1oyd6BXL3LeYIQg4QYNncuaDBIFrHAPB8ib7IXsUgedSvts-_2pFmk-Uq0UKzGkurVrZ7AJwp01L2RRLuZqESMGwsMJjLCaH-_Kg0QvKYi3jCWEAPXuQ_Ixd-kUujZCOnE4Ap5wiHGLlDdkozDz4R_RloJSQ7fN5BuEVhvx9rvTSsTDpkWC9g9mwoV-CDVFr3lXdS0zoMs_dSumbf5ouqhxzzszXjU0jhT8n6RXFbkjmUhl9K6FDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=EmlbztiqbRDAeU639CDgApIvQAtyyd8WVlekkIloQIiI7pD-9R1W7AitoSAb8yx_OZeWSVQgwaDLZhqywX6Jj6pnckc05Mf96xmUjV5UwEx-AXQJipz74ZVcXaXFsZpIVbq1ph3P29tnROO_LbfZyPiz10VBWyRJqgS4k7XHtmufnqfCLR9G9bbdnPWm0eMVV_XQL4kjC6OPuEeYZXnDKOjqjNFnT8t8vF9vUZPFDpT3aHeqTyVpeJ6lajM7nRFd1qHDHVcE0tmKuOGOz9kaR8y1JPjGk337ouekea_-abq5eENX-ntzClH2cfRlYSWOqOBxAKgBmI9hlM4_VfEZtyOPW_ilcHukP67Z41eXiQOOAk08ShFvkZ0dg_C2nAuH-b6dahn7bC27BscBxc7SYylIBapL0_NVqX6aKJa6gQ-AmiOVbgsPiBdpM4jjE2UtCXCZmkznx2PgV7j8ipVKwQDmIRWtTRnxiDTxsJnWEK09Tf61ijmk5SLXT6AXu-EeDflPCm2GG_Navv6ag8k63NY6fG07nU7iJqrKJKjcVry4oi0W9BWYURV0sCEzv0POdCiiOdmzaBXdRh8aYzAILF6U-gc0xOt5VJZ-x4HYMBV8CzawJaXyu1CEw9r9Qo8a7XyK2L_gQ2AFDnFUXkYq8_ELdAzgYC0uN2jM3Yl0Vxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD21yl0lRgSEUGoc7j5XX644JB10mTdlV73V9tOHQtyWas-Qz5EZ3wCuKlgfZocs0OUjLVUd6eUx-1rtiPt7SulCDrGyLMaB-s8XjH0kz2YfKHSEn9qPk1RG7NLFK5YiiTS31Upoxo8th9UcrN8tXZacE-C4cCXyDKdDgPqwbNGGiO6RzD7dlUYSDLb2JLhE6GGbAg0V0I-5icxM8-1prrhGhVipeRiP37VnDSZXESWId9HbehjE9AyGgERyY_l6EUFUe2KJyFgzyoBHgFSmvW50IF30jrDcsO7zKvia9q49VVvpiVZFiVJav96Dyx54n5VYKmyeZAnkfZA8ouO85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsuwdhKTk6awCxIv-2uOhh59lYfTSRd8ZMOk1zxAAThXcN7yavTzHr8lujP33PriakNycoReYg4FtaxRC9_nHJPqnhuDgAHiIkk4qJu40LWIRBqyCgNkgZUYS2i7sGd4on9RiMGHreYBnSL1xGoyhU98xm9z_X7UAa5sxWah2jYYhaBk8nYqyWilzjlXOo1w-Xq3b4nzlJlr3j0kp0s3jeTK9F6ZhrL21kC3RILjLCufQBwAx0P_U3PBK2U-pkKlppzGpnsVAxsfoSVeMk42L5UrQNv4eeLdBssD_djYyuK1Lkpe0qSM96fzETX3VppdykT46XwvmUiLm8mDnALnBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=QsRv-H6mO4toL-ghXl9wTCvL_RyMAo14Dx7u8ywM0QV_f42hdE4tWkLX8GSgr6kDZPuIu-igepc8D0G2yIYNv0Mo9EdhqaXX7bN8nXBt1ZZ9zOYY51K92b_0Wp-_AfZmYsAHa05lJgz70DxovaneDZMV_oAGRtx-_AtliwMlXEiC9str59--qpxdDXngkXMWaa3-2qAmoqHM8iQCfZEuTpeefEB7iCCIguqMsFe-FfP8veFmqGxqBSslfbTDU70CVBfGIfnkhldWoxBpONDlHOWKFK47iwNVSo04165HWYi7uvcIQhDNiZZxdjuW8fFSC9xnydKh6x6S-3jehXBMLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=QsRv-H6mO4toL-ghXl9wTCvL_RyMAo14Dx7u8ywM0QV_f42hdE4tWkLX8GSgr6kDZPuIu-igepc8D0G2yIYNv0Mo9EdhqaXX7bN8nXBt1ZZ9zOYY51K92b_0Wp-_AfZmYsAHa05lJgz70DxovaneDZMV_oAGRtx-_AtliwMlXEiC9str59--qpxdDXngkXMWaa3-2qAmoqHM8iQCfZEuTpeefEB7iCCIguqMsFe-FfP8veFmqGxqBSslfbTDU70CVBfGIfnkhldWoxBpONDlHOWKFK47iwNVSo04165HWYi7uvcIQhDNiZZxdjuW8fFSC9xnydKh6x6S-3jehXBMLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQQA4p1MBoimqsJRiz5fMRWp8rXm83bLyX__c3AtD5C0sy-OoYyVPhxCydO3dQNsGaMDJBFmfmtpKUbgOKTmdqA7i9KH_Z6GTk6_rXuBFoicOXCLSEUbHwOK2HiiOsG252feYB91_y_b2vILIxdJ4wGAQOqyejWGAjJ2vqsG5VJvOqLnPFTvEUXRl4PDHaaXSb8PeljuqN8YVEg8ROVx9XylyqlYv6IADSRRCMIANNE3Jexw95Q58C7QtnWxrDufKZhw8ihmJaaoDvnH9M4_uND542V8qgVDlHD43aJNv-X2HO_5bBQOk6m34QIL5KqPMQMSJBYeZKXey3cDQsjTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uq0OF0aqoF0u3Y26MXkMPc69awtM8o_I-eeVvKCxVzImwLgvLDh_v7hOmWyxAo1TQA3SMlwZjuZGIPmxlrWlgUiLGeyFKyDczSVDbgkr-ZKI7kRdqs8L4fc0FAzYTniUwnBDwB0SRzRyIEtugUn4VlvK5Au61cOdba2P6MIUzvjog3aimhEtPx0CyT3_gC2Glu2x3PpUNp5N3g0OuI9em50j6MPgwUuZocPI3ycXUEOzDNlOkx1yRB50l639xiEG_oYCRf6YgB56vA7Nciflk5ruwIJVyYgSaovLQm5h_5RQxTZ7FS8K3NDR9GGc6wr-JaPwve2_vLO-PZhYM-FRdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzljHlNgf5e0XuD1bRDMiQ002qG9R4N1l2BqFv35ZBMtD72yE6hsFlZQkcsvxTXFYN3FWPOQX6D0-XdsdhIsPcI39tqBye3b-R1H-XvFQZmf7D0-qfL-KQCsMwAZ9KcxG2njFrpYg5GGroHiVKnu0McrDIvYwb6Auyu1YnL7iWY0hOXI2-5W4K-Y6ClAC4Cw7IhjE1KjyeS8-AeDlQgKVc1kKLMhjbS1QZX6HWJl9s2W96MWNrqc0ymR5MX9G7uv4uXReeY4KlfXpsjPcWup_waBv_KG52D-jW4_zS-MKid9LjpC9HtBaOICzSdHa3_dbSz0byij6RZhW2e5jLeONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
پيش بيني رايگان ورزشي در لينك زير
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=brhhSj0MjkvtSQS5rjBtM9Pt9joyDZ5CDmGHcCr5Jm-IUQHoez7IrR8H6ejIRU4ImvZgseZiwp-opa8pBuyTy3DzJlM7M9hR1WyIItcTTPEg9NFaNirpK-64CLgw9HPlCcwqbZpkUZDjqAGE8UiXRHnvibMQFuITIrCa8CkNzoLa3sA45Ak4jGtRTg4RAOb857N_puCSxYonHHXqdd8oxmKJGzAb0FAaC1E7Ujs6V_eJaOOEVeVrDE9CPmXuwthM0k6i-yZFpfr5ZVSBD2Byd8A59SwhPWN-G2-6zQJbfxY-GAAqycWFll0gdylIzrPQhb2UG5u2x31oYh17dBJJSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=brhhSj0MjkvtSQS5rjBtM9Pt9joyDZ5CDmGHcCr5Jm-IUQHoez7IrR8H6ejIRU4ImvZgseZiwp-opa8pBuyTy3DzJlM7M9hR1WyIItcTTPEg9NFaNirpK-64CLgw9HPlCcwqbZpkUZDjqAGE8UiXRHnvibMQFuITIrCa8CkNzoLa3sA45Ak4jGtRTg4RAOb857N_puCSxYonHHXqdd8oxmKJGzAb0FAaC1E7Ujs6V_eJaOOEVeVrDE9CPmXuwthM0k6i-yZFpfr5ZVSBD2Byd8A59SwhPWN-G2-6zQJbfxY-GAAqycWFll0gdylIzrPQhb2UG5u2x31oYh17dBJJSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiRQCB6HVDTk1GYm7AnULUAGeDIOpdLGC008F5EpKwZaSyGQ8hqgZgqbTslYfK--c19Ymv2mBom0TTJ9KkBjKECUbrttpTprM0dEG9TdG7J3IgW-2lzCWFFIO6_FF2YMEAuX2MLS03S84fZD-7jJ6yul1YaxDz1LP664SQpTxxBVdKYQPR57Fz8OKs5w8j4AwvkGsNjjsTenzGBeuTTL264_gMT8TRWS5AN9C6KXCfneBDyGHCD66Wwt6kO01P7q456fJYmwF2zzGF9BpbbOrKrbe3Yr7JbgYKyY2ph10PZPg46Oho0i1oQk1psWZuSGVtx5QdGYWB-9n9BMbjA1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=QnA7WQFCBbO7CuUAbWyztcukbPhyQJRvwgm5MSHd2hTJD8tswCMr-leeKcJPQ8vY1DMf1abZ5-7aaeFKNk6Cy4ZXLvMNB2qZV5Gt1q8_U4WDsAGH4zWj0EGmRcMnyua2Gg7shD_FU3r6dvL5R0uqDTY9oP7oaPqb_m4ymixPxfCqxJlf-1KwxMyLAEcLN78qZyw1Dv534NvHd1eZ8f93jM6z-r-bEHZJsqbKUj6SPzVbbkytZ3pLh82rjFRwqHtIP7DSUJco2kM4tcSeB2jlVT6h0G5TspmjLXl9fb_pLwm0A69AhrJn4JcAYdedohyAF32IvxcekyBkLgqyij8vFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=QnA7WQFCBbO7CuUAbWyztcukbPhyQJRvwgm5MSHd2hTJD8tswCMr-leeKcJPQ8vY1DMf1abZ5-7aaeFKNk6Cy4ZXLvMNB2qZV5Gt1q8_U4WDsAGH4zWj0EGmRcMnyua2Gg7shD_FU3r6dvL5R0uqDTY9oP7oaPqb_m4ymixPxfCqxJlf-1KwxMyLAEcLN78qZyw1Dv534NvHd1eZ8f93jM6z-r-bEHZJsqbKUj6SPzVbbkytZ3pLh82rjFRwqHtIP7DSUJco2kM4tcSeB2jlVT6h0G5TspmjLXl9fb_pLwm0A69AhrJn4JcAYdedohyAF32IvxcekyBkLgqyij8vFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdKkiOeWpcFAkScvjbROlAoALKZgSp-HZxGw9AlDZwUX8nGJQqCbmysz2atnVpjzMCZX3uhQrzDnV4pikDnGSz8iyrCCj9jSkDywaPTWUIw70x8M9QjctkRaXzfrBPvgFnmlbViqkpJnllUQjFpfOZlgarCVI5jLg0gyMMXFYHZ_FZPYQM9Ge6phrwEzQCmmAqalKXR8FWbmTJN6-0wtLbnZlrw6tPritJ5GaXsQCqB9x8B-Kn3Ywv0M5ia-ZxN5T64Np-S9zMmeOQ_8aV9fhQXuXSts-MwUfJCYtK-Gpnt99t0TqkUMv1hZxrZCcXI4wdRJzXwcB72VTysf_yi_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT3cBFGggEsSzzLq5qArCVIEBfpKRdc94q2tIyQ97vgeNHy5ePo7zvkGDWPuNoVQifV0enH6vnS1gDA_s6t-bZqaDbAZVKi7uFP6a95WA02L0ezgerl9tCnaaEPNUF7WF2IVE5Nj--IWIT9b-jbLqh8uy3tRwU0Fo_rl0K-hRufRoO4CSqAac3VdxjLcgHU4t23hzd1UEduIou9qevqml8UsBZpi_JyldMOPi99pow5ieOV7alGAoUr94cuFBSeWmITxhk8uO5aGhpbrFopohXDnUblaRoK3SP4t0GjCYXot57xAudItJpK9iCeaM41gtQrZ1iJl_oQNOW6NkEsHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=pSXRmNbnbTEZj2Hnl_XSODfyV-KaKrr-3dbVXGM6W6AQdNbxid_2xsRlBqbjlSpTsKgKqgw1QfGwLxyEcJtmv--6CyRX40aA4VNAWyxvxi9QAh_4alRQueD0as0olxTF1aRTo4x6H_XQIrVde2f7MJ9CLv_oNv52USQBsEnD3WMECFB6E5EEYNQ_GK1yBXom1ZPSWINmp10EbKzb0spd_RrF_LKlq7zHnciW0ZYRj3Fg4dVYD8QPQ4zwv_3ex9PxF4dhu6IvoRVB7M3g1Sm4JUGceWvJO_Jrb2SldBqKfIclabHlfwsd8vdfgsTtIAaLBPu7UdqZntE2-SpaD0xr7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=pSXRmNbnbTEZj2Hnl_XSODfyV-KaKrr-3dbVXGM6W6AQdNbxid_2xsRlBqbjlSpTsKgKqgw1QfGwLxyEcJtmv--6CyRX40aA4VNAWyxvxi9QAh_4alRQueD0as0olxTF1aRTo4x6H_XQIrVde2f7MJ9CLv_oNv52USQBsEnD3WMECFB6E5EEYNQ_GK1yBXom1ZPSWINmp10EbKzb0spd_RrF_LKlq7zHnciW0ZYRj3Fg4dVYD8QPQ4zwv_3ex9PxF4dhu6IvoRVB7M3g1Sm4JUGceWvJO_Jrb2SldBqKfIclabHlfwsd8vdfgsTtIAaLBPu7UdqZntE2-SpaD0xr7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goV0QbORaP532yl3gM8JxB1lv0wpizHpYmjv4yrdHZ16xl33u6I_ov1bUyWcd03KFmwh1KryxD4pGQvEZpfCkzuu0pPchKgpTMP0mywKdLDGOc3uoNKq1g5yEcCXXC56ZK1GNUGDsgprvnlqx87Rld7AYPzQE27JdWG9QIuN5aLISUvju5DVEVyUWLTskXGucgWJagDOdPel6VvRizz6ctukbwO3weRTKpqCODEa_oG0-dlaA2SOd5h25I6W2md11jBKoOd-Fyty85wXPk84QJmccjFdy8ReJ1LgW5PBB1KLiBX1ux1Cn9wm_8kyanAi0oqXBzlCKRZkCua_Bu0SXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
😐
پشماممممممممممم
❌
❌
❌
مکزیکیا بعد از صعود کلا کارای عجیبی کردن که یه بخشیش قابل پخش تو چنل نیست تو رباتمون گذاشتیم:
دختره رو، بدنتش رو در میاره نشون میده به همه.
🔞
مشاهده کامل فیلم
دیدن فیلم
/start
https://t.me/nod_ppbot?start=d3c61e4fde78</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24770" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=pgRK16rMNrrlsjp7aO4xcdM0o7S2Hf4FgA8dmJsYWp6LmmO2DAL1LXKVWWFFK8DPCpr-scrYhyj0IESkZrklFe8KBsLxVkTISBoxd7-AE0mXagRmNFxSNsjNtTbmQzCTFzhTazm4eBLnaL7RfddMlxBQgvw-YIwDESiPNEFIgocJkEf_21eNkKCWXf6ZxlwvjLpFeARq7jH1bXHU_RR5irawKXKbEEoa11mMZ2McTQvOLkAoinxqhVaNXz9Q90-3387F49qMvBMnXuJWIp9IqOmcFr2srG0XQSl-DpSTKMT5x-4J6MJ-P5zR4-y1UPBIg1f4J8dRga63Ns8w-fMjjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=pgRK16rMNrrlsjp7aO4xcdM0o7S2Hf4FgA8dmJsYWp6LmmO2DAL1LXKVWWFFK8DPCpr-scrYhyj0IESkZrklFe8KBsLxVkTISBoxd7-AE0mXagRmNFxSNsjNtTbmQzCTFzhTazm4eBLnaL7RfddMlxBQgvw-YIwDESiPNEFIgocJkEf_21eNkKCWXf6ZxlwvjLpFeARq7jH1bXHU_RR5irawKXKbEEoa11mMZ2McTQvOLkAoinxqhVaNXz9Q90-3387F49qMvBMnXuJWIp9IqOmcFr2srG0XQSl-DpSTKMT5x-4J6MJ-P5zR4-y1UPBIg1f4J8dRga63Ns8w-fMjjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL7mkKiJ63VSCJLA81Lv_cjpWEi-PrsW1S1sQ6PxESbBZa-rp16nVzMcKmGobFkhgfYBaWfMi6GAJ6Bcjwdj24PKb9aD8tqY-NuNEwdeezuqEAbdnD_5EPDV_ArLOCVBFZgJzS-AaHETNh6rzfl0Pddt3wo1orbGk2PQ_DsBwDISw0k_fRyxPiDhwt3lfJFHgWmysZQ94PK6mQU8VBGE7Ro5Hidi16AiDFiFrLTiARf2-542a6FB_9NIGIVGPqD8dARqq9HGqviUrBXGwuEf2l3E9Ldk50PXyVQUfpB5K70ZlTpUDV7CFP2DThfrlK6QjnCSS9UpI9cOk5QP8GkLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skCCnd6-z-6YFO6dT-QZdpN3anZ7YSXEFgrNzTFTdFKw7tFJHjQxJ8AYHg_AxbHwRGMWe4vWu7Cy8Lsz1Efa75JDxxEFJJGYRNezBiYlOHd5QHs5fQtEFiQC3gm3MiWBwYbvtiqb8Yc19c1NagJmrhgug56KEqWkxu1bkn44KKNEhe8wYEMdK6LmUlq5jNnqAKkg-gFM-X2PJCM75CwzlGXnKBjkM2inzAsNuoTaCWzjr5JCWYTfTIGhrEJNp0ql18He2i9MryilB3b6AxvZafR1lRMt20CgtcJZZMwyOqYaApleZmfA2a6jF8URM8cdPFK0mcnpV2mlS5fpB_bS1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JfAiwpHM7XFKkvI8D8H4hLWZ0BFwoQpFXU9OYYYZRMNmoUBmpdwsJKlAQK_dmanusfvynpprHAYJOewskUT0KfHtdlVzaXbGUhZm_-e9_lN0att2TuVbmGtaRIElrk5_1tQJB2SGLbKYRb1Vfmvxogzd3UW2kZfX-GqC7ZWWXxdyQQH8g-WnIP5EjnznOZNhDO9UlHgMHH_7jXGg619enjVh7A4EKIZxEA1nsQODwmGvdoE34PsdmHtk1M1vw9tGxW7830mTdSy-DahwQD6W6rvzE85AjsGeRAEY6QEZjmiwgiYV7zLBmyXKjBpj3tdn1DFDhsnCCBogs91PKJnCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TgJTDt2S5T5pbmCnxWiyYkZVoJQNwDDeWpvLZFXyes-V7VS-_pONAZfu7sL769WGed-O9WKHd4R6QUuLaRzNLN8TVfa-x_ghYGzPoV8YNiJ2xDWlPI9xfmbFUZHCdB7A8QnfyyzcfJM3LqXHgP55qr4SFZhdc8ZnnSD77IzuGUDztMbSLrzRl1WeApBIr5AL7VRlPDwiHrGLTOnIJTDGTQkxJTx2s2asDL9Bqi98cbY-nNvTUKCoCZt4I-K7Ia-DRXz1wlRsZGTWwJy9zQV7GqaHHcvsKa-alocKljazmJngylLYAJ41hG7ccA2QUJMM0REaeoO6GLxUrH4HK-RZoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=TgJTDt2S5T5pbmCnxWiyYkZVoJQNwDDeWpvLZFXyes-V7VS-_pONAZfu7sL769WGed-O9WKHd4R6QUuLaRzNLN8TVfa-x_ghYGzPoV8YNiJ2xDWlPI9xfmbFUZHCdB7A8QnfyyzcfJM3LqXHgP55qr4SFZhdc8ZnnSD77IzuGUDztMbSLrzRl1WeApBIr5AL7VRlPDwiHrGLTOnIJTDGTQkxJTx2s2asDL9Bqi98cbY-nNvTUKCoCZt4I-K7Ia-DRXz1wlRsZGTWwJy9zQV7GqaHHcvsKa-alocKljazmJngylLYAJ41hG7ccA2QUJMM0REaeoO6GLxUrH4HK-RZoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVrXXsBZu0Xll6bVqdMfgpgoqZnnv7WzxHygGx1V-zjNmjIBcr7H75qbWz6Y3SagKzyCABG1qxT96hGUyDWEqDsfEfuVLZbqPxhKKkB0CpX6mzHWKjKuuUUa09jCN7KmE4l4hQWruGBwNrubQeohoaXRrICpoS-JAIjPhQzOSTfUFOJIRWH-iakcPb12IEftHxbKlfEprNK5mnO-zTNl9sr-j1oIANCwF348tq5cW_Hm3CCQ4Pasp7n92jCGqJFRQUMfTmv8Em5Br6ODzADpUskPDatmCornXf_rZH8zsZ7fM17yr9_A5ofyaDtNHjZUDs0AIPQ7VVCUtT8X_U8yAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=MMRFQkSyNLlQ8yDgyxZ-z2vI___9HniIMRaPZYegUm433RRfk_8fB_-2rNSucdin82t0PiA5m-C12k00YySlXjdXH7SpxbU9nFchJ9objKmwooeFxZdPqnT5II9F5PqArBeV_EP1TSc7Qj5Jlx70BxS1_PohlIU8C9qn0RqqvRRwdJ7NXvn10OeCYrJc-Vk64XXSNiteb6pjXEXNWPcB5s2JQV78FS02VB9D8YGfzxBDY-r_lJvofEhlz7idQJ_XxyGCGqFsHMpW5a1wceZAMMeyzOCRze25Gez74mmxirGCQY4AZfw0zQJUSummwqfp3Zo5Q8SPZdESuMYpTM351g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=MMRFQkSyNLlQ8yDgyxZ-z2vI___9HniIMRaPZYegUm433RRfk_8fB_-2rNSucdin82t0PiA5m-C12k00YySlXjdXH7SpxbU9nFchJ9objKmwooeFxZdPqnT5II9F5PqArBeV_EP1TSc7Qj5Jlx70BxS1_PohlIU8C9qn0RqqvRRwdJ7NXvn10OeCYrJc-Vk64XXSNiteb6pjXEXNWPcB5s2JQV78FS02VB9D8YGfzxBDY-r_lJvofEhlz7idQJ_XxyGCGqFsHMpW5a1wceZAMMeyzOCRze25Gez74mmxirGCQY4AZfw0zQJUSummwqfp3Zo5Q8SPZdESuMYpTM351g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCVE6HlAWxg1NzjucKpHQrHg5zHGdtpSg22err0LnLIxi0YaICPHPJOFadFO5BhIQdoVoZ2m2fipH-jbgS010ley82XeXQqdpajpq_zcTiBaH0mCRAF72qhMqOMF_k3e_S_zs7sAXlKwlDjSn-GXgp70UakuJ4goy8KlSkVF29El3dyndnXC4Iw5S53IiqBSZbrgfMi6l2u99VCmzgOn30ehE9bJfHi0rCYLDZJs_o0LZ1NvfRDRzs0o7AbjL0pavXcrK6GYq5UWhesHZLCaOJM3DCutFIJenNUxUWm4_NSzeFpBZat57OBkrKNQouwH4ALZzQYyhd9WV33pzFlb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=kL0qjiLGHGCUT4T0lH8XdqK3q-4wWZaYxg-PtSJeUi1Q_EGsP028AStl-BBwWtUM_VRBPnSBRdlGvqTI-1WpCcT3oq5Ypp5Sjz0CZ5JhTf7K8JWe19JcMC3Whxp9Wbvr6rPjFDLe_meTbhuGvYTUmizKpAUz2e6aYXuIyBIokHr8iciKb9KjcAlHRwu_37nZfnZGPiarWDUvC8f4Dmf98CsNcN2tU_iexP8q453dRIod0pltbWm9sdY3ObrdGlvEA9LZcTZY7DwO0W8c2sCFmNwURewQRQhK0LKWkwXYnq2hLYWVHhleq6OnAVvP1TTOqJyti5eki69U2LqT2DvIwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=kL0qjiLGHGCUT4T0lH8XdqK3q-4wWZaYxg-PtSJeUi1Q_EGsP028AStl-BBwWtUM_VRBPnSBRdlGvqTI-1WpCcT3oq5Ypp5Sjz0CZ5JhTf7K8JWe19JcMC3Whxp9Wbvr6rPjFDLe_meTbhuGvYTUmizKpAUz2e6aYXuIyBIokHr8iciKb9KjcAlHRwu_37nZfnZGPiarWDUvC8f4Dmf98CsNcN2tU_iexP8q453dRIod0pltbWm9sdY3ObrdGlvEA9LZcTZY7DwO0W8c2sCFmNwURewQRQhK0LKWkwXYnq2hLYWVHhleq6OnAVvP1TTOqJyti5eki69U2LqT2DvIwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye7pbdCQVrLc1N1lqIiyUJ7FtyXPhSdjngbOwwKdDZj2Lqx2OkWzQZRXsSsIm1_YBp9yJxLenD8zvkHSmM5mV6wXhUkPqQnbgDppKdVr6KccSRx7jxCf9F1cNxm7GRIZ5Q_7f6FcPu7Z2owN1oLF39aOpBnQMj9KZLYGBrW4gShQneROTFjaEZCxNOmeTsc9VUjlyfq5BsdwsFZb7UTgOcJQtHX7iJRgtXFHiYO2elcpi9fRGJGPyhTBT2JY_NJ2X97A3KYsKA1AD5MaiUCMBCV6S4zJOt5-wu2ItzyDlOFkqjSoioIkUBRlN9t-JAvaIWL02e0g-3VlrajldVPhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTKWkkTwTjGE2_jXoAZzvfkW9JBHMgyzx4mj4QECP9TE6AZE4lpz7SctNHmgzu50PguQFzOk7QtO-FO7bhiyfffH0Qc46ON6fWzlLPMZ8CVwA9gR5dveXliJ4Rj8RIUcJWdFDJXn9tBoAI4dCD4UfALe6ZO6k0j_meCUqScEQI9kHxHgmVod6PPmOQ2tcDv6LJVVMv75tkKrse4LwFgjDBCWKwVsvuOwxrQBKMf4fTWsXBiSFxOtcQo7c0D6-MFwsL-oero8cwXVRF-y_mi6AeYyXWLIOwYVOrtHjlZmLDHgotD35MVraTz2hD-Z_W5Ynxv8jT316TDHuggLZOhLAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مسابقات جام جهانی 2026
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://halvirox9371.bar
✅
کانال تلگرامی
#رومابت
10
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/24759" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPZ0ECAd-KglmWEFVZY1mDBiPdFXafp0Kb0bPrOVXvHIOOQ0OhvlEKQyPk5Ib78EiUKsSQfb_rEO98nUSCw3cnrP0o9qsi25V-JljK4dWwGc1d-GGvN2X__OqcqTIJL13uj6SstEUA2w84xQYdmcmvJb2A_Gv1Zt6hAEaXXjiq7xPL1mpUnAjIXBaB3qwc0hCwV31vRXJ96Idnar49Hu7na0Bh38FWhIfnpS3qyZ8eKUVFxdnuF5ruuW6JGW9pG6mzIm_ZPjpAP9kqnmO3XLMNVH5E9LkyQivuvQxKg8McpVofUp8M0ZZaDP83tb43u-I2bw3vA2TC757TmxaAKhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5L20TwjVN4Kg-WsEnjGXvp7AK45ZTP1HRIX_SSLF6MAH45BbPjDsYSjsLVlNtnPgU3zAHnprYJtfjsGfBdfWFxZVaE-df0H9ClOfSUw2tCLkfHvamR5xBcOgYv9rXSSwSLaU3e1Zwmnxti0ewKTAd1LZxwrPqh8vj2UXuOyCoORa2HvfwMl7J6FHZrEqG3fJX2hzwTeKDawFGgr-PZ_-f6F229s-KbCrhug3yrvvNyuJDMiW5OjjkTniICeL7kSvEz3wUV6o7p_ZN0lqPmsAr6CAHs75beWRKKztKVRe6mYFHW0jEQhcafVK_i_PHWGAfz89RKOdrab4N_h7DA0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkTiw9gGANDHHg-HQJq__aCJ-bKJTUrvWBXDLJ-1fNnzpiETHU7cF2AeQBYNUUiqj_IrJj9qUslvpS15A80D_PBOmCPHcawKlWeU_erbIgfTf1yGclrb1wD5enNwS_2SSjm1g7FZh7MO8PdWfHeyxcovQlT6FxdfgUOQOWc3fTPq6NYv-wOHRfeBaSg4fKahPwmzfNXDY5oDY6zhCyVKlf_DT_adcQTPDcpGZUojyQ3cllI9QwWhHITfV6Q42USpALXjAbDe77uKz1ReMsfMVQ85Q_7WwU1137W5GPFCZRhF9FKLB-H_LdUUqtwicr0c7C2vXJfT8SWWQsuD_BxYnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZJEErva1UxSzScmEsp3ITxPnGZr9ngoYSCq5cII52i7KlS4j0258TDpvuZZsg-8stN9ojFHBiiy_ocnj7_YC7sJeQYMzCHRkK_52tMrRg75-x9VQluxkgSXUAh37fwT9CdUE-aFvmNYVJJYm06w8fOvRSqbd_cktvF7Yrrnq2l-TpX-UiqZs7Dpm--7NLpys7f1UJjw0ww7ZCCJS4rlpzYOIyoEMm3_wS8qOU8_cn23tOLdMOXJzpOjK1SOGttEySx-ryQdyFvGNEt4liiTKC1vJukhj_RVRz7r2qswEyUNMJTtbv0HIJBsYiTnErommquTFL2SOsXELKlN48vCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=vUTPMXYYQ86Ia6mPJ_-miqTxv4eOD52xkKDLBgTu5wMybTeYAyzIHYgxr8xED_oIGXXGoEJ919QLPoql9fA_QMFP6q5xR8xJ1KVM3oIQoGwr4QfdwKzV_-kuygcIIjxfLWpsl2XFphV4UZlMBzS6jg1Sbl5KSuKo5MWJlVqWonrDQluvyXNxPpzcXvUEJr_Y9DHGV77ory8RvSKgusk3tu_NhYg_lFnKCTReSV3HpmG926QWYWWsWkPqEgVjujqgu-mnhwlBKQbT6nzUIZISy8S4Gk_-OOwAUEaNOYZj0Nu1ZK6a3La_EOyUDBF0cf21D_jtTFB1cUbiudxqqbttan1rPo2K9fx6bucvQlbyNHiJtkBK_sIUIUIk6kxF6uGnZjC8xua27Yp-T2oEaEq2e0zp2Q9oAvkfqP-ec7ScvmImMBXnY1fJEkIpKQMDjp6WG0u-jf3azy7fACTA31EavD4EhoM_QJ3PEmLg9sNISq_VXl6Tp6l65hPke23t0DBthkSCqX97fGYOyjeUWsV8Mfr_4zmNiGVKjZhPbHZgU_uZQxAYi2CJIFXNjiP86yFI3XXA6EQv1IbprWOAzh8p1QZXJE7qxBFq6Bn3d9OaWyssRMh6lQ_6p1WluBmu92J4O1Hh5as-CrBVoJrE80GOO875OwRm2c4fkjqGrYRow70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=YslWMTEIZLSBOTS9Ds0xFM92E9mEenUsUXtOTWAU1C8L6q4IPglUH6r8Pas3hkEF9FjEbVZgeKI5xyqZa1KiqtX8JzBzyPXbWnPHo4zquHptjPpPTskb2gTlfJAs83b_u2GccYmq9OjU_LTs38CaPE436TWbXaul5Bu_-g9R2WAYtK52KHyJ8WxPL6MRc_lUnC0_LgXfABuhdh_P_RUNEran6JKTnkYwceAn5FXMVDEzfBk2uZI27jVRS988E6MTANXkm-5VMpxPiZ_0Kg33ZfDet1O_Jse8AdG7SK3iGn8oRpcGWua8DbRRQRXQvo_fgmAIdZxeAkiO89zsp8I9lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=YslWMTEIZLSBOTS9Ds0xFM92E9mEenUsUXtOTWAU1C8L6q4IPglUH6r8Pas3hkEF9FjEbVZgeKI5xyqZa1KiqtX8JzBzyPXbWnPHo4zquHptjPpPTskb2gTlfJAs83b_u2GccYmq9OjU_LTs38CaPE436TWbXaul5Bu_-g9R2WAYtK52KHyJ8WxPL6MRc_lUnC0_LgXfABuhdh_P_RUNEran6JKTnkYwceAn5FXMVDEzfBk2uZI27jVRS988E6MTANXkm-5VMpxPiZ_0Kg33ZfDet1O_Jse8AdG7SK3iGn8oRpcGWua8DbRRQRXQvo_fgmAIdZxeAkiO89zsp8I9lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku_WO5U2v2c8GlJ-oEtHPJ9Fkl3uCQMiQOJpHJ74Cvu8c_yM1V3YFyYTHwoBQVklLjmOzYTSM8Dd1bbPJ6eeINhOS1icJePVavRzDXlQLSUbvdBWpkM_xneCJf1SIqj1L6Y0mANKZjcmp3e_M8WFr4M8cVoeo4_mL8Lqs_DLxOATJ4ASSU7u_9_TOBtogNIaXUmp46JYVyEzOfGaHSDdpzyTRLQCEOEPJQitQ_tPSmhoZEfmpnoWUHbYPXnGOYV0mNAAgL34JpcxMqIKSdIu-4qYHsprNSemQkFHIBnpODOK5f3oGJ0B7IToETfQozRG0Hh-gxAWMKDcBIfRntZP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=GXwQyykQq8sGU7JQX78J1Sq64TcLyo5EjnNnWITLV291mBqRMfsV289PEK7fMNgJJEeq66peklwPi90KPx9SNVgAw-uJsUCTWaqmZJnScCkI2xPJOOZWGGegeV5ifaCjRjLt8FmnfJHGR-EPudzcTZR6NSHTohsF5tB99WXZACMrrGXsZXOLz73AQrqok5NDheJkT_virwf1LS6DXESSfner9eaQr2ZLL-djGtNF2yKBs-00PnwDjl6INekoLsVsyz6M27HH55l3QGShx4NhTRpSENzw6niEY8CSDMMSOOB2rEN3Ujn6jc9agIpG3MO5xiYspxlUkYy9TU_yHgRpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=GXwQyykQq8sGU7JQX78J1Sq64TcLyo5EjnNnWITLV291mBqRMfsV289PEK7fMNgJJEeq66peklwPi90KPx9SNVgAw-uJsUCTWaqmZJnScCkI2xPJOOZWGGegeV5ifaCjRjLt8FmnfJHGR-EPudzcTZR6NSHTohsF5tB99WXZACMrrGXsZXOLz73AQrqok5NDheJkT_virwf1LS6DXESSfner9eaQr2ZLL-djGtNF2yKBs-00PnwDjl6INekoLsVsyz6M27HH55l3QGShx4NhTRpSENzw6niEY8CSDMMSOOB2rEN3Ujn6jc9agIpG3MO5xiYspxlUkYy9TU_yHgRpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=Epy2Kvxjt7ZR4G5daZIdDcm2axYCxQeNosQyMLYEyUBLX8B14r1e6gSrdQ5DF6rnZdVnm58wiHzQRYFlVikzFAtzVqKACXd7zQheNSW8C0jbgMGuR2IieGAzADKOUmo_Io4rpO1dRrybRCUL3zRP4N9VhXHW2DWCwWBFSQee6QEtZ1TXSFtJq55YxEJZvZNmgf8oU5sg99y98Q6o3dRjmKbqnkMGHp26pg8S9fYwyNloylYotv4jHzSsHT4SR7hrRy-31Hllex4zOmLQ2Txe8VmhLrPaL8ONYPuJ8XQg7q1ktwdYeqiZFyt8Uvb5PPYgnLvBIJ5Ec02bhKv5eupZ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=Epy2Kvxjt7ZR4G5daZIdDcm2axYCxQeNosQyMLYEyUBLX8B14r1e6gSrdQ5DF6rnZdVnm58wiHzQRYFlVikzFAtzVqKACXd7zQheNSW8C0jbgMGuR2IieGAzADKOUmo_Io4rpO1dRrybRCUL3zRP4N9VhXHW2DWCwWBFSQee6QEtZ1TXSFtJq55YxEJZvZNmgf8oU5sg99y98Q6o3dRjmKbqnkMGHp26pg8S9fYwyNloylYotv4jHzSsHT4SR7hrRy-31Hllex4zOmLQ2Txe8VmhLrPaL8ONYPuJ8XQg7q1ktwdYeqiZFyt8Uvb5PPYgnLvBIJ5Ec02bhKv5eupZ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFBAS8IZFAvpIYSFjQwFKsGTBUxgGgMqfj1C-YdKujHW8o0m9_hmJ6sUQgtUAoNFpdktj06lWOFZifgiTS1jui-SO5x6KGjUBq3MXYLdIsshKt6JPSGRxxSIDnJO-lFGT7DZd0GUMf6V4WHhHgotCrxckvXMXOZ2UN8kQs0DBTVZy0rVE3-NeOVpHHh-AFu_xilh8EZ-1xiffvrSuc_Xn611k3U4jaBbUQWbDQNLl8mIV3Y0Od2lWBPlDbWhi5QXzCPqc1gHGayWMjRmhELjoscRV8wn-ORJaGW4_CrCPPnVV5M2cfBNkTVFFpS7o5D9GvExL4wyQuYDdM3djpJZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cw3BJ_y0xGfqaQ8NICrLFwiv6Z7mloAN36zMuck6fsMeJ_uvlv3nzUa77U0Ke8sD7gA5VAoUBpqtnHEdPCf5JYBnrv7lYOSbfwL0jDIwiSYVMSwG8KB6CDOfq4tEPT3EXf9AW6KeYnMbg137FdRDG3sGR-Kqe5SGu3Wk40OfaNI2jRxD7l6A6z6nVlS4BqzdNc7vh_Ck7A2OWiiIEn-yddtE01DYOIjo7zDpXscGQWDcXURFprreUJUhvQH6gKatoXweDjXXc1jcigXpo1bfLBho4_Ro1dJU-W-rIB69NiTUuMJxpD3hMiu6OHAD5nBYJsRC3A4ETZjducYsITeu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0YplsTaHE8JAb01TahYihD-8mPI3AfzfZD7pSBiuHitSVi5DjZU-1Zoy0ckPiCuFMdiKAMZhLLhiaFnaSP8Etww4Frg6pDDY-Co1s0sXz3GB7_XUCRzRlhGJ-16b1G6-3sTsGQNTcqLHLHzxdNFaiJP9EWQlGS23ErcyA0mTeWbXWltxWHmw6p4LfKbzzuVZWDuDkbMrHpcVqjZ-D72jHdi8BY3UQjiec0d42ezYxMUpZpNIxX6y0V9G6FizLhYl3k_FlNH527_9v9o29HMjTBnvkZOhv6foRc6Mw-nbh6hM4_elx676Z0SnG2WgVRE_eVz2ZPuCGj6-h_KNKNnog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H09lduqhCPmekdctObb40Yimze7Krl74oeUoatS4nszglu-NtJewveRrdLPDc_dtDHXHZD0_SpgG7lcYx32Aj1NfOWTFkcvTeth-QvqijZNtqORBAC26tmvFBwlATlPWXGxaFI892EW7IQ0tBB_bebbKVbh1uvt8Vyl_K_CKLolcVch517294G7WTkypUiiaBVwvRKRH5vDszAwL5l4HN-z-wh_2bx-UCd0tkjO-HLNnx9KQt6stxRRVEiwD42H1VaVVWDudG7R2R96xvpO8trxqGhmMMPbEl_3xy-OpWlQ-6s0mslY7mPwi7tloUt65x1YOcHo7dcJ-89fc9lXcWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=PSp2uOkgv-Dl4gEFSa6lLNSVu-coyovnbnEqssDF0qwiLKGy4lLIIhSmkb1AXKCNIHnz6hO9Vrqoxl8Oy6BtLG0-zxVrww4xBPS5OetlLg2DBdupGOOvEX5G77ZiJf_7NQYiyQbvn4s2FvHCPDLYZRxcCpLE57n66ZlAPMrrxgak3l1bhubfoJ9PoJTWBMtptW03rBoMm5INWl7EnISCDMAq9wFVo1mMjxISuvhr4lTIVUrZYtmno1EYzRxmnicq6TpobvU2uN2l3cJqtgdH6YSA2XMNRn5DOCqMQxwVVTdXPSlEkHNAJkQ1wM11YHVn_yET2__gnpMEXPNWIt2IvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=PSp2uOkgv-Dl4gEFSa6lLNSVu-coyovnbnEqssDF0qwiLKGy4lLIIhSmkb1AXKCNIHnz6hO9Vrqoxl8Oy6BtLG0-zxVrww4xBPS5OetlLg2DBdupGOOvEX5G77ZiJf_7NQYiyQbvn4s2FvHCPDLYZRxcCpLE57n66ZlAPMrrxgak3l1bhubfoJ9PoJTWBMtptW03rBoMm5INWl7EnISCDMAq9wFVo1mMjxISuvhr4lTIVUrZYtmno1EYzRxmnicq6TpobvU2uN2l3cJqtgdH6YSA2XMNRn5DOCqMQxwVVTdXPSlEkHNAJkQ1wM11YHVn_yET2__gnpMEXPNWIt2IvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTrmF1O1EQQYozH9Yr6H4Uu0Jvd0EDhzDp664aF9PPGsqF1XC3xduv0k-6GDXd2DQM4lKXfsRozUE54vcWl9tMubK-uiuiuSrhykZBRCK_r0qv2JezSZh8Lr4iRUidToCFKtYCikPA1T39hF8Ef5pesihu3gXCDs-xM7iivqsA8ndUAHDN0Co-3k0GNr1wp2y3UCgsr03hCTmgbiW4GCRQXVeQwO8j4ROmc-zQb-qspvv4F4XCDe68jIQUO0D0g3SyONB3h3XvbIcHcYl44LzzxKMVKg1TH4xfRV3_LuizcUAyxYVUhZeDwCnLnIyi6K6CtPtBNEbaxo5H0PArZ_QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EY3pTfrTDiE9VCGTdcvzyJwuOVjPptE8kvRsTaWzl-w82phUOCAaoMU-JLvXQQneE-w3AvCI9GXDnx9vNdloCfxF95DWCttu_0jsnSvPCMT1mwdjaSNu_JZBsxhWZ8Z-V9eZweBIy9wbCI2AUPUq5t_RfTDWFPXHRvUlNtPOcWlUSEZTQaVQsr-0vcnE7SSirilvlw7b10I_xzUaygraw592fMAcj32ambk_UM76JWZd7hx0XvxOa6WB9QsNni8KJ5xxD817P0bqDvp-EanvvSsZYjX5uQahxaSeuWMqQqRWBwmHF1PU_WiYMp93ZzGCiYIpUq2_9ZtYKITLcKD4mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=dHVY20UK11dxMWRzebvhF27dzOKmeNxGZV5tB85TlkfuJPtDq1Bo37WBm9FKKBXnALmaKdvikBaHDNquNegT0EIOsqrlwjPskIp-Mp6hRAPlfnskOxesSq0gLa0jJBdCKp5Z6FWaIsBjrCpd9xi7R3vHFHYEDrxXxns2jF8nyzUpH3q19zy0c3oGu6whkKOxhKPrDrqPFuEvppF7vAozoPG6QJzOwHVhy2bPunfDxBGrkZ3s7lmCMH8k-cNi-zVrfTsFzS89DaphPbReKVBSXv2PlKdangzVMMcXFn-QS7XPJ1cd97j_rJY5ysibql9qcWxmOIJpvbwfxUWMb-6rsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=dHVY20UK11dxMWRzebvhF27dzOKmeNxGZV5tB85TlkfuJPtDq1Bo37WBm9FKKBXnALmaKdvikBaHDNquNegT0EIOsqrlwjPskIp-Mp6hRAPlfnskOxesSq0gLa0jJBdCKp5Z6FWaIsBjrCpd9xi7R3vHFHYEDrxXxns2jF8nyzUpH3q19zy0c3oGu6whkKOxhKPrDrqPFuEvppF7vAozoPG6QJzOwHVhy2bPunfDxBGrkZ3s7lmCMH8k-cNi-zVrfTsFzS89DaphPbReKVBSXv2PlKdangzVMMcXFn-QS7XPJ1cd97j_rJY5ysibql9qcWxmOIJpvbwfxUWMb-6rsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL9hPodptfSlA-VMvwSPBd6_Qhk9mfJPaUjWDUkTavP0uYTWHKd1BJqnlV2cWb-uwqvmydwZ9jvVw1n7F9BWnu1Q6V2jzZoqxAvdcZ2obICkqTGConRk8_BYuxRKUTxHD5_z6L8aUAkefhXGrmuSe2N5EyNqdpEgWySTSnKJ_iSVJwNhVv97zsmEXL4XVJV38ruZKK6HxH7dy42A6Xvln7rv8n2GFQw_D_g4CkphZ4SfGqh5lneRnuXGt8Wd7NfDr-zpig4N1-v-M3GkQ8rfOhjAFt7he31rEXPyCV7KAqxXZtQlXMPZxZ3Y_OlYrVLyl_LcB4nHsmGR4zp30WgPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLzc6PWKpOlflqKy1HXSSWORc5AfZEWsIbCkN7-ve7NF2HPWVPt3wV08ZFPgUoXXEJ5pFu_lIT88NRGkOpscNkMnM8YiqvPCaK3cTTQjyFRPm8RhvVdg5zX-fYGRGc_vKzNKwFNrJlGkD7OnaJetv8tjvrtEx1K4dzBFGhSgCIES0Ah71DP_ELJOnbKnQOOa0R9MsFDhLxsv_ov8KgyXJ2I1Y21MEKD4wf8EzTNeQ7T0f7WeKQAIdUbrrras8y20BzaGLaJbfWs3M5A-6EzvqH1BDlhtpUjrm5M1ZMoFNvIyqxh8et-L4CSj2z3j2ZI6Hm-W00oUpAtyxy3sLpqg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKs4eJakPdt1PPzglHuGGAW1fgHDQxkQggOJVJIidcJ6xxT3ja0ElOSerk4Pf_gIqrfGYw2CmD9IB898w9n-rTN0tWLFzxGHnG6-WSLtPwO1Lml_ArDYwcf8h_CFI3piSUac8wHbxNPBZ0Hmw_awzMUcZgxf_ZA9r-DYE50TdWbJ4j5GQkhApOzPBsGTE-rAfKL0YFwI4TB6ACGF5wntgqII66L5aq7DWwetoaLYcx8T_w6eyICqhgsWBDPcZwg71G29S3Ys9DxXDjsPFoLCGIGeUHTI0LvfEWVAiujKtYbUvfMScqz_CuAJwsXuKKRPrMobBxYH4ZgDk3ZLkSOQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEdE4ZrnMMjcibohY4-wkOWnELZ7yaq5DsTn33KVcIgZRxvg2RIEyjWYSzbK26KWUuAkWE455MkvPh7ItMrzWBV6CXsyh9DeXKr5_bIDbZWMwVZuakb-yQrb_fiD7as0V_GCd12-KdMZz3H61jP8POsJl1yCc4MiOpEl3qIHcYZOSpXYnR_Y2ZGBaPY-S5IU3Zmvugr9fsuHBXjCqQedzdcucMKk7FGtFX_07qP_iVtFv2WZUpq-7oM6AwD53cgKM3Rrs28DgSk6Bi1VJ-qYBPZnBJwmA5xayhk0dmAMp6Kxy2QfMrIq1mxISIqTAEv1R3GmfEXTNcNREMUXFhyEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=SOZ7LjlNoIAB1mgcLkKolb-XyehK9_Fo7tF_1hKTTsGr5N23pBmR4ANd0swa8hrXiZAeTv6gy5QQfIm0ev6E2070Q_-WM_2NBf_YvKb4mSsNokiSqRHG94v4lUCDh3hku2Ml8UJTt-FYv3xg9nutqQNPIobg84ZJ9oYb-EAxUiDgPRfhkT4maH0rB2_hgZ2xxSy9B4RDR13IcyYfyP95ulbv3KJxdJkE8wgbonjn8Okwq4tEL8181V_vJw9oURXF5JAcDVyaHNZ0LRhdwkWIk9a6CVPNY_VFT7PCnYnSZfEMRVQb72PpEwIFyXgP6tVdaOjLgz9lzBPRJbteM84lXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=SOZ7LjlNoIAB1mgcLkKolb-XyehK9_Fo7tF_1hKTTsGr5N23pBmR4ANd0swa8hrXiZAeTv6gy5QQfIm0ev6E2070Q_-WM_2NBf_YvKb4mSsNokiSqRHG94v4lUCDh3hku2Ml8UJTt-FYv3xg9nutqQNPIobg84ZJ9oYb-EAxUiDgPRfhkT4maH0rB2_hgZ2xxSy9B4RDR13IcyYfyP95ulbv3KJxdJkE8wgbonjn8Okwq4tEL8181V_vJw9oURXF5JAcDVyaHNZ0LRhdwkWIk9a6CVPNY_VFT7PCnYnSZfEMRVQb72PpEwIFyXgP6tVdaOjLgz9lzBPRJbteM84lXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=gzPKo_B1PgGV62n9QKv6L4LVndE97pwlvr-2-uYLFf_olDQKHyV_fly6SDXJo7rYDaAkOEjSymGS8sMbYD7ncYTc1r9aXHXlpTJUA0quzKIUP2N4Osnrg8iRT3XNjAQEVtUhBa-4bFj2881b-7BH5ngc1-Rh4LbQDBqSYi7JXNlRrsfPbDjwre4UiLqpLB_GQH_mUNmOuvH3LbX24eLf41EPLh5rwb43wIi2lwG6hxFZ6RFz1RhqFtKFtCeN6M-HGfZKUdRRBvaI9o-wvGcoV3s6gyM2Qoo--UAuFi42V00JiorPZ1AvI18jU5eJHyJqy5GUqwQhlw77tNVbbJX2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=gzPKo_B1PgGV62n9QKv6L4LVndE97pwlvr-2-uYLFf_olDQKHyV_fly6SDXJo7rYDaAkOEjSymGS8sMbYD7ncYTc1r9aXHXlpTJUA0quzKIUP2N4Osnrg8iRT3XNjAQEVtUhBa-4bFj2881b-7BH5ngc1-Rh4LbQDBqSYi7JXNlRrsfPbDjwre4UiLqpLB_GQH_mUNmOuvH3LbX24eLf41EPLh5rwb43wIi2lwG6hxFZ6RFz1RhqFtKFtCeN6M-HGfZKUdRRBvaI9o-wvGcoV3s6gyM2Qoo--UAuFi42V00JiorPZ1AvI18jU5eJHyJqy5GUqwQhlw77tNVbbJX2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_bd4yTaI9wLaqGZ30rbzjhetAf2N_RwQ55w0L4kg7qZT55pUGdgvFRviAZnDhTnnR6SBsKOIxCvd-0GV4eDER-3ue4bnWa3jpXqiZPZd96gePrtOde6l4f47ULdlOIJWlRVt1zCXOL-Iae1kCItKxcF1j6zoh68OFjUFTq6xa1svmtQdSbDiaMtqLtBtFCyCBfq2DjDm4iMU9ShoUYTxHtKigsh9kd4pHHYl7JJkYiH3P36BHSWVv6A77kh7yM1Cq_rgxNz1K6B81GXUf6sXH4Q6CnzK5mWQIm7Ti5KrO44TanseqZwPAuQAJY7umJnfEtXiuVE6d7KhGIsDmonPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r10
@betinjabet</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxCifGSgRoSRssGvDbwAHhHUFAjYekkSnwc-8Mfrn9-F5JxqgUoPgzcxutAeXx767Yg2zPVH6MavakrYr3nFmqYx_7BocVxW01RbT7q-wS-7hsn1jibPMsyrb44n1CcoCeYGrsk_GtNvVxrfrpvac7VMWISBCXR9HxBHpI34OL7fAMDkO-g2D0908-Ocks364njIZlouL8FLD_5pOjIzNizBfCDffb457qRDX7rNd817br7LB4y9AGvK1ynYWNmQ1U8ARwZrFmsXW0srdWRnW1jJSJ4SRBDY5LSetLRYQ3WuMaX5369Gbq8ZZOjXmpy8wMuI5bwE_yQIExIFaLEjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=JwLU26acTykeeYfWxrXXI08p3p0cNJYtZ0QQtOY0lV4sqhVeHX9TaiIRu1DaBLuJnWWtPFSsVYhEusZBQeQixcExBCxWcK9Wtn8hxTo0rnGbXwEJ60dqabQ2UXOl6ksKcXW1Iv0gQggrq1kvBQoNZap1xUR0zUkSwL23Erj0QYaP_TEny6k2QYRCdbR06UnhnVWdjkQn33eYhamOKetQ6isEecq1AzWQYUiH7lg9ZjZb2d5VBZNab2mpmq2a0QKEZRf4Jj-C6-891XpYV7i6TONed5-CGq9YRNaFfBvcLREh6kv2Ut-2mecCQOBhONqICbBunNq8ol50nrr_TDaLlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=JwLU26acTykeeYfWxrXXI08p3p0cNJYtZ0QQtOY0lV4sqhVeHX9TaiIRu1DaBLuJnWWtPFSsVYhEusZBQeQixcExBCxWcK9Wtn8hxTo0rnGbXwEJ60dqabQ2UXOl6ksKcXW1Iv0gQggrq1kvBQoNZap1xUR0zUkSwL23Erj0QYaP_TEny6k2QYRCdbR06UnhnVWdjkQn33eYhamOKetQ6isEecq1AzWQYUiH7lg9ZjZb2d5VBZNab2mpmq2a0QKEZRf4Jj-C6-891XpYV7i6TONed5-CGq9YRNaFfBvcLREh6kv2Ut-2mecCQOBhONqICbBunNq8ol50nrr_TDaLlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=G-4tTUpcWM-uk-QR_DYynfkrr4GbY57DSAKaZE_YhOtYs76asEU_HMlrJdYJdmODHLL3IVv4xvot9RGd2nWktZWqJBdLIG3XHmz3y1uOTov1I_5HWvDSmU5VH6UiuTPXiLCFmmRhM69WByhSPF1mPH12rXv1sl_8lTXdTl2X4EzMfKDKs24Mr4MapfUdTohgYWxxfkJqP3vn0eGttBua_-9IAx5G44b4220us77yE8owppOLFMtCfqFwARRGXYd19ST54SzkiObSlS-eQg3XHMqC5r11ED0z5twOs1BeVk6IlK0M-tVy4GjLrwypqgZKLTsmtzZQTm1XW49UTJLgaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=G-4tTUpcWM-uk-QR_DYynfkrr4GbY57DSAKaZE_YhOtYs76asEU_HMlrJdYJdmODHLL3IVv4xvot9RGd2nWktZWqJBdLIG3XHmz3y1uOTov1I_5HWvDSmU5VH6UiuTPXiLCFmmRhM69WByhSPF1mPH12rXv1sl_8lTXdTl2X4EzMfKDKs24Mr4MapfUdTohgYWxxfkJqP3vn0eGttBua_-9IAx5G44b4220us77yE8owppOLFMtCfqFwARRGXYd19ST54SzkiObSlS-eQg3XHMqC5r11ED0z5twOs1BeVk6IlK0M-tVy4GjLrwypqgZKLTsmtzZQTm1XW49UTJLgaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUW7H8kqETRHazLHVxQrxLE5NwaD5JzqEnlk1p4vs6wOQgJyd7Z08f9-JATFKdkt9aTyPVg93blAlYxGuzOZS6Wrm4lkK68ZJXto1T-XLFz2CYWhfOouRnjxZOs5HF-UPZzlcYyDCf4p-SklnVoVNbTcr9fIuPGbRwec1bsHwq9CcW02pZf8ULUNn8FzIVgjQxRUXqJANrUwuzoZuhIJww2I3g7dOrHHPPUfh6_o41aF9yw0yHsDULMyM-3yjiQ8c27gCNo6AleOjtr-c5CkXm5-yNc5sHFIltCp1Mjggzdpm2JkFEcmtXG-4G_VQfcC7H_0E_A-G9cgP0IbasynPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eg1nCao_c0kj2bhqU1Mv_r6eX3DBi5hBZ8csN5FD_oBpwQo72evUI4Fb4Io5es8tJ6crzdvy94BzwnVR_fPxxyTgR8qZMaG856ssJACDnYxBU8FLJJGMQ4olXa8v5Bbj_h3OCeSvDjwvvhp3E4_cTfoCwZnzCWMGpn_OgagJNxGoQGRssbj1wr_j6XSyJ5C7fbwn0Xn0YTGB3QuAo0w4sKEpwjZhZ7cnmuuyZ0Ln6_gJWSx7M35XuLkeAVgWYOltswzrx-m3s1ANiDwFTrgwqyaUkfWKxEEIW4OtiBl6eIn3L8RAA077zxE4-N2eJexaZyvGwpbIz3deZnCYpMvWtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jh5kM-QnlG1E6dNZc0MjjoG2DVrzjWywkXKGeQWgS_EH3c5WfdBXRbEOJpUIuRvD6MSPHx1ePkkuh1nMlC7MTyHxSE1fcxjpnYhJEW0Tf8y8SMj-jRr2nS44CZddyoV0iHgaQEqT3N3pxsmzP9GiK7pXT4zeoRph4mF9LzSSnmFnkpsOIyMXhkZslcQflKN5d2EOn9OcT4b04wcIVHG6fbmaraVFfEA2lB6S-7lpiwS9pgI64ZwGi_C1olDXqx91FhazyBbmU9TJhKGEGX9-wL5sIJ1XKWmjDjgbs8OtnGXH-P_1V0KQYqsu8XN5iP-p4c1HIBpGNQKZDoelLGZz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDzQa0kK_Xfdp6M0S6gwBe7knADlQT_7SlamSRqfVMuXm1EmKCJNLlzqriMRzHCjUgiGqkjnrnWszzI1XXiAONQxY-ZPZhep_eNcUG63KaJaR3gdKXBc_o0XBGTNKh4GcA_i4iw0vrc1_47BpIuTWSC5tt8OdV0kyAyWB2lwmJG0ql0NuFCAk8orkWbJOcwC8ktKoJDBybsCkUOphMDRgkGskTUQVHW0iTm8grlsow8h7db3eAP_SkZ-Bf_li7v80_aCC4NK9nnYwSjakvrBika6BApz6Y-Wz2mrOXW5XR1xX5AiQFXbbBK180opWBWcsJpLukA4hSTIIRxEjY7ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=XUL4KtkoSuaQo9oE4mGtY1BcjUemD745duIZ21Zf4dBSUKuvQu_hu9RNdW5JkN7vfonodaTdVvMj7fwK7GMPdXRQw_GdPUm3GcBXYSJ3dN0HYUH6TgAtxpvZL1vKhhX1vJU54_tOthtL4yp-Xi5S6J7x4-4O4pyrbwpPYYGQOIRKi_m5A7-0Q3x4kN_BaCgjzippMGqw_kzF0T3RenT7af6ubU_3YBJeq1HyK_qAcRQKSyfoFSl__GGJUp5Be3ZzL7IQkdxJIriYjs6Fqnvug39YMCMz3pie7dnts-UroZettTGj-jwlXnhPSRtEcVsRw1WmVH-hFvCsp2iJXtZbWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=XUL4KtkoSuaQo9oE4mGtY1BcjUemD745duIZ21Zf4dBSUKuvQu_hu9RNdW5JkN7vfonodaTdVvMj7fwK7GMPdXRQw_GdPUm3GcBXYSJ3dN0HYUH6TgAtxpvZL1vKhhX1vJU54_tOthtL4yp-Xi5S6J7x4-4O4pyrbwpPYYGQOIRKi_m5A7-0Q3x4kN_BaCgjzippMGqw_kzF0T3RenT7af6ubU_3YBJeq1HyK_qAcRQKSyfoFSl__GGJUp5Be3ZzL7IQkdxJIriYjs6Fqnvug39YMCMz3pie7dnts-UroZettTGj-jwlXnhPSRtEcVsRw1WmVH-hFvCsp2iJXtZbWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH9yuuuiz8IJBOcDIV5owH_KRhBxuMoFeMDk-IlChaEMj3BctFOPKQU_BpyEYU-tD3Vxlc4sPZ5u1vWr0GtDlOx8K1zNBRaSbJaFyEWWBHVOM1ZhnasVPVFftKPeR3pozKUXHTlKE_0yBH6ldOM-P1ew9fZRr_US6fgjhK-obJ-4Vg_2jQjb5MreLJkFk4xm_GbMlNE9g-CT3g0Hb0vBnlKSAaVPSQYmnWoGGRiV9tb_4RDmE_4qUGi5MU6Rlaev_CHRZa0iCrhdjryexgK9rJdof1r3qgxlY8_APhJ4PwLki-laN11lsPvm9xjk8aB2e5Sx9I1c33Cgs19F49seAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=dW0B7sIjMZ5Zkg2uwWVZzlRv0ZT1SkCv304HvTf8tLh0yHblBj6asLlAD-DqRJMo8KNM4CQksS0vLCwRsIlZlVSQazjpKkj4v38LdppOAogLmE1p0SVfkn-RGAk9ai7UhMHOetzqcWc_JS1YI3_YlJiqCu_2l4QJZy0fPMi00W08DHptvBMTHAUUtf3iSUbaWq15E9cZ-VaYssh9v44UvKnHxa9CfL_GVABdjdCAWHxwpRweOVtAHyTOEDSw05X3QZMHxkI4cy3mOBhfg0F8emFEh7DJvejDFX8P2cvtvx51Z2YZz0T8YxlQm0ujMMSBd0PCZobXPA_I8_YCq2_hJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=dW0B7sIjMZ5Zkg2uwWVZzlRv0ZT1SkCv304HvTf8tLh0yHblBj6asLlAD-DqRJMo8KNM4CQksS0vLCwRsIlZlVSQazjpKkj4v38LdppOAogLmE1p0SVfkn-RGAk9ai7UhMHOetzqcWc_JS1YI3_YlJiqCu_2l4QJZy0fPMi00W08DHptvBMTHAUUtf3iSUbaWq15E9cZ-VaYssh9v44UvKnHxa9CfL_GVABdjdCAWHxwpRweOVtAHyTOEDSw05X3QZMHxkI4cy3mOBhfg0F8emFEh7DJvejDFX8P2cvtvx51Z2YZz0T8YxlQm0ujMMSBd0PCZobXPA_I8_YCq2_hJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbZfx-hDUmn6aAvuwRED_aXVSXIKVWkjxomA0z10yIlLyM9I5Hi4Qc7Mw8gYIvjY8AoUxxvSibt-TkywBTJHCVX-7CDmhNHaKllDO73FAwSXKxId9-x_atEbaXZxVg40tkK01UGqWSwhmB2oxUTXHgM7SZil9o6HnWdxUX7OB0tA8Xi9ujmEE2A4kc72-T-Av7NZWirURPnxlLsMfkp8nV69YdpY5ckacIyldcYodkr-YwJzFYJexyPo3wDTE7IOaagLaR525dq8fD9LbC2k-TbGilTrFEtNQwk-coc5PT6vftqLge6RmfTZtzZed5J6sVHW7fEnu3Ood_cX1lE2yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1CCh8AL0GaaJ7MPlOfUOKvCODzg6Vzm6iv7B2J_Qt9Q1Uk0s_0mHyNOufkLUkPCqHmSv_YRo77ZewJ1R1ZpqPHxd-AdYBQ-7_IytHvLHxRKKZOV83BmmepwjnQbMLdsupNkQUitRMjQcAx-rdz3EWAsn7ix02KpcC7w5YiBQKM8Xan0kmzYc0CqZfxB0laJPmsYxTaXTf4OncCmZ9fUwR-u76vvmrY8jzZ_GRELnc40dslN8EEHg7JqfPFurB88l-1mLA8YqCb9fNuO95jf2U3_pLr1P29GR5nDxptvubpEdJTMJf4npiSVpksPZp0235f_JerNhXmNJs-cOKwHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBuaD6s8j_SEVkvIY1PBJDN6xIRMuGZGeCvYNHaDCRtnSGgwyzFrC1ZBrzL29dFsY7sA4iKikqS2PHVZEVA_CIXi7deqR9y2U9tV7CMxXfJDUECvZzVy3rm32xS-0C1rTdeLwcPTa71Rut3xqs2oslZIQoCAJKq4MUFLL9sYf_fxVSCeQ6ioqoug3gxdBck_tTfxFWB1VCupqGsAN59ksIAJvWvwOm_xVYGG8NrcigD9QqA1JiFo-MZQpQ_mntYfOzcGs69O7i6_VU20lNixiOPEC1sovlHO2mFHjnPz2tWo9wheabrFdvkF1javZ8RigC41jy8todGLTXU8RMVekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKrIqh4PDOoEWvveX-8FDNdbOmOA8s2ZdShhb5nRlvH9GJ31Y_jD2XlpbwemmYzzVKYQAmdMH5MXwFupAr5Dh2jWjd0MGvNssXjcU3_HO4q6LpOK3TzKEsT-0ElgElnsCpyepw4qWBN6QJCT7TH9QSWyIHDwvbeffFCcG_PINihul-61EmPWRXGqA_09Nq4gp4bizvtgNhcFU8FtQDUjdDmdaEPq-oXVrmPTf4t_BpNmPfdfCL1uWGy0hbCqDbDUSuaBk1PxQbh9akW-cDQvb80OlGZ7Mu5gDA2cySxTMWP8KXICxkZXELzoHbuH1ipAqfnsclRF8lovvQuqY7Wa0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpuFzSXSOC8IwLtrseObtHMuDS7lB_MPUcSshDMXivyhuVqX0JJ4wWXBWPjCjMZ5XOZlQi1fZymVQQhT4s06nLMVs7CX_HdTkmJsPS5Bh8ozKtdPFnS1lxVEBDPlfGGpGww_CDGSJi-QkCxAUEx3NSbtnmHTEE-JlBg3QPKmrdYkm1azYREYqw-HF3Aov_Wi0mzuP3nSoLBGDKKDcMpM8IfPyDulckEovMx-q7EIddHUGZYIZtoyJ5qK_Pq1MF8zyAv9igY5mEjJ4EgW0A8R__4yzwO556__Smt7nX9EmDn7xD53sanPdVkAJ1vLUZD2uWEZs4LJdd9tJYQJU0IaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4qlohe0iKWrI20AZMukQwHBPADjfjJfZpFo8q3rdjjn8-HRx46FUWQiaP3s0dtjlfbpl94xNZQpn5gMpCZzfVwBucs73W_U0CvL7VIROR0QMzkjoGiMXSTumb8Z4tU1ujedFFD4hKziJ0bgvsfrQHa5-RLSBFh7gJ9BYYpLNBF02ORDKgWf97ALQjnBT_CpH-I4YVPynaIqV6b6rUjyGIbo3qNVQGenKtX9eB4b8MEDOgb_ihla0e9tJhupb4v0D_iGl13q-zg3gtSw7EgDKFLIziZKSRHbg2N8uH0PnkpPxFsdGyuf6x4EPk-P209WZgCvx4MO_p2nDCk2ng_r8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5MC8TiFvJ8RQOmvLy8-YI8Fn__bFu1vt7iwek6npxTvz__EYm7euH5td9ZZlfe_vH_8u02X0oU4lzS-9bHsuAE0kJwxHGAjcUrEQ3rWsXrPv0I2p2SjM1qIfJ7-bRKm9Fg30tN_I-kd6fKFxfDFgHsJ0J9MFKc6-QRdL1w0JLD8mPNr5dVZFw2muUUf5JGTjN72OqSnpEw4LlL-6vRQ_MfVPzUxeEaiv5Mj8G3qLQR_1C_NcczzNbyJvAumwTuzhncZ0rQuxJXjtFS6OOJEtr3-9b6r25kLJKxVUAgikYiEgWs6ANzuUUSvDp_ryR1SPxh-COuxu0krgCMumq-PmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ygt3YpjWpKnMH28KN0aaEMMvB6KLpqqU0eA9FVsz31IOgEEGTnoUM1AsmY8d7pd3wgFXsF492Vw9U5PUfyikFJh0a2kA84S_FhBOMrX_UNI-uu08FqirHUC7kmN4u_5tjahWodjON-DyYLRzjfpTLGKeQv-dLWdbxeCqFkA5Hc_GSo1n-W0kp08SRKgZ9Zm0wxDqjbpnoEGnaeHOtOC9cRM6wBiBt_SnGJMEO1EGDSwWtiFRT7IBuByYkdT1qV_c5w1PQDloxl3sAWkKqmCamT_DGpbV2EwBKmiE9A2bYn51_wLNEvW8qZVZXo2PCyL-4M2DP017TTm2I7PWZfO9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5Bfr_uc9nJ8jAktlYX1g_c5hdUXjTgvo8i8m6uyW9cZ1N_KMgbhXk9KjkXpEvlh1LZ6LWHp3a2JKHzvk_vi-n4dgUKyRTZNe3SbttGRHTeq6HfHloXMd7hhAdxyffFrS-EVpUzQ9DRm_PuhLctn67EQo1aD8HaQU007UlwA0-mrTpfSfsjcRNpOi0nJH6PZC-Fz3gNGZqaSPXKw48qIQoDONu3wbo3mb8fU7witkuK_7t_IkV0lH3GWV3mhb587YAUtcJnQFBvN7xGUHYFiRqqA0Dug46iXZQt41mDu6HxmndYFgpSGGuaRJ6Yy15VVbGUUuEKAS47w1_MYxGYXLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQkVjpGrTruQFek2rayCfKfUZlB077R16ds8cGgUQLCrP0lkXpg6jTRtyO9ti4zCGLogfgFvOeiRHGPAh4d91oDtCh7dKlRF3QhAjfLnpnNkaHRBbMssokzOSnkXmz3xGbP1xyTlP7f_giGSCuJQZSWkdByPVNVZjBKmE6rynOEI2wxkP-wqeqD-kVi_a_vtVaI1qTFRMat5vkMEqNwcu4K4jnE63nd9umVytoGsxzqHNfmHhPqVAtrcm2MoTO0sgmk7MIfdkWgGt4kIW7ysncUQkMHvZ4D3FJfu2lbJY1Hsg69ZZr6bsii10l_iwTZ-5s5WKjahAPk6IZIGagRFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBxRe1cMv60T3GlQ1funO57JHQcT0LKzhF1cvLNVRxIluAAbLS7qqkkYsegWCSfIHeiTn7V2NpUGDz72Q7hkovobFnhqPFbF38ia1KW-u74QbwTXvkcd2c8nO92tPnhUj9ryCd2SWKcGbs6bUYijcKCxAa82WLBwotqe1Yl-bE__2WUi7mow9PQxX32_b6twHC0bIumkPVnSnYVd7UL8xFbqD54r7gwrntTQWFgC-PojUrOtkY3CbVfljooE2eTvp4aIsGNszBfAgEikYL1G89OcF2Rg2U8psTPfvOmfSMwXEm9G3Tt16c8V7RG2NID8uZLxba3Le2BY1Pv7Y5NmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adn7WgCqJ6lyMbfBTKiZa39KswdANLJslNShKBshbqfAoWH5aRDWx3Yq1LSIveLuVjemQEB5b3wti7tZ5rMGFkqpfSXApcSIgI7tzk4ZoE5AmBXVceBUms5g2ULxa_VycFmy4jnl3zmHTV_xZm3W4TdDCPPeF5yamLkwAu_gZEKakBMmb3uRI2aPXWIsE64GUPvM0rOzgsAtge1Eb3dM5rjNQNBpDZ9IpfVghsOG-ZtaIJHtvDJ_nzkGjaL2jDAYpzTfUC0MGDTFNu11gYqTbw6tEpIAmG_WATTvdjnivanbAiAp6QlP1jy91Ew-u8cz_JqXoE9gnpJgk2vRK60_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpG-tqRbBopm8DKwQe3Vq5IlMhkNBDCD43bPt3mNgZZwsLZCVdAnaIvNKDbo2TXQBbF45A15Fo-42qiokhWpUTeueQyq5RisvEE8RhaldYQr079O2ly6ikNa2HEiNCNR1ArNyeIwTieH6eW6yYCOYL-drtuUQ2bUGQ2jiyw15rgrYediHxHtVR4CrbQtC22S2L495wAQAJAcgkzRsOFBQLk9pI7tWXdmslku29vlwEFLAyeuXnNpRs02LV1Ce1Au2RO8EH_YCSPkafKqGvsnnya95tOj12t6ty0VdD7Umw1Cs1j3lVuB9ESths5DCBqCWehZNr9pZVrjLIwi0FcwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIgIUQBE9qUcX7dSKEM5eK-1_fnvaa5bK7_iACr0QT4LgIxpJfZhr7bhLc_xJusR8A7XYOvYw-ws1_-bLJt7zxbnFyFk3nBOd5LtSwnkA7UGmDJYef9RfS4PJXtYbrR6QzBkCXQjcn7dB_CoW4AanUyxkry2VY3qkviSnq2B7rqp9ptBNnm2Fnppjf4w5LMZz2GSEP6R7pos2ZfyYDXvVUrmMvT8ENSM74eVdUzZOt53RUjRDBymtToGbUcfUy2OcHNNSwBWQlqr7R0wpBFyfNEdgIwpCJODqiMFDszR-aFMHn4x5gOBVt0MC5v1CEaOOcoJQ4xSg3u0Ras683NKuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKc4uM5NxID3jq0ZTUucMM6TDeagBV6EMyA3bZiVtL5lEuoKvN8SHDfsYWB-4fLsBuMp0HUq7LRKeO5puQHejHxoGXwC9hccY_zkaoGaOeqjiEb4QWEAfOEnnxPk6Ie-PbbgrIuG2ObaCtPJqWphdEFT9wlvCUVavWOI8WeMU3ELkhav3Pv-3qNFjeJZKfC5BM_xdEbz8qqBZQ0gnVqU2BV0eD8owbsxVjzNb-7njKbNvmjP1f0rWiA0FeSJYUQB3Nf6U8IjY4QoY2OIXAg1v_jqTcukW8aNfVH_Ycl1_0-PQUoJD4pPNbAMQDwwgHMjGm6UzuMu-3A5oxsdUtSxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPxsEtEkUDVA_1okSjtJuWpQCmIICHq6wwJhwQRk64uEwLfiZzHL79pUk_YnQcXTwcg1yRShZLYaKax2pVQm_JFKDxPGn0g0MMFemMFVvZ1b6rbF7RZbm3Zdxe43boASLRf16HE8mqJgYFN2Y4SBIFda4VLOKHA6OvoGJlWfLhyMH-8sHiXSJCciSh3jdS28YT8xaTIdwPrrG2WjW0Q8Hbfp4yK0BwEHDUh2wpF6Nijly83RJASTQR8UWebi8m94m08vs6lv8zUPHGJLIGie_rdE7wn4E7gHbxOLout1jSEwQZ291IvehZ0zXwyqSzYiIO0bkc6CkBiFe9nhMBEFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScL0ktHteUdnWU7ehZkROPRl-u8ostk4pVVuiJx68Zl-b6cu_QnxHShtc_l7omgsunq2FDX6NMPUpTP_YjhtVqjoR8BFPbdZtxqXjJB1SYJwAt3Xie25iTj1PDP-HaxiHst2JDhqbySNSVafWW2id1O6sovobafgZDeED2rVR1rkquDwy0QBtgx3eZFRq5ogw0vZ1dd_S3rQnBhsURi8AuifD3ERvPQA4jlMZXXzTDnYGyo6X7MoD7cv4p5bnqkrHAE71n4mr3I4JGPCM7yU1PHNLNjk-WUIRrzXhp5bjo7Qt-eSbTXDOaEfmL-h2PIQhJUJgBL4k9H0q7xvUN3BZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0AHaLo8SC7XbMbyNmhWJcZNwmt9eaHcEC86EVaHrBfScWT4ka5lAoonGalQaKCdE2ZwfH-uKOW7nIXgG0zRpKEMPIRRc8pEIoZgpn_p3FGhZnAXeuJ6QdNTQE6QJ2e5HP8uxXl9uo5GN5TzzWsHtaneJn885m0OoCmlACBpTU3W54-tUjOEqTemBYE6FEtjVK_gu2dNNbIwbDYjjq1fgbRSCaQN5pXw0J5QrHdA7chjjRr3lyq3GVewskD5fiQkjyqItquAxBxMS8XvPf2oeN-Ye4zp9Xs53BB8YnNTNU9c_sqmQp1qtOX114o0qnkpFLH75zKxHjnshv37uA9ULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=ExZT2B-6v1ZE_Lne7egnk8T2QoqDHfZ27fjnm7PgYjBEfIb13eb4K4dhJQRUpuXawwqMiKpW28PZMGAX7nTVxkETu2ipGdPHmiW8LqIIjdsDgEY-W23rfrFNchBku40RxsZg84RcKDIT4DiHsu9cA5amE7zdLuw7F9X5ERUVNjNwC87XKOU2uTZn9dPJOTgcFrqS3WqgTxegkOHkTBWw4iaWkmJGb9guxLVfpEgS57nJamdCgYTa-rbkqpnqCTFQhG6EoYLnB_0odYw_oy_l4iwnMDe091a41F-m-lojbsKy1gIgUHuAL27MTc3FCnqT8ZuogF9t0Brii4JEQz_mvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=ExZT2B-6v1ZE_Lne7egnk8T2QoqDHfZ27fjnm7PgYjBEfIb13eb4K4dhJQRUpuXawwqMiKpW28PZMGAX7nTVxkETu2ipGdPHmiW8LqIIjdsDgEY-W23rfrFNchBku40RxsZg84RcKDIT4DiHsu9cA5amE7zdLuw7F9X5ERUVNjNwC87XKOU2uTZn9dPJOTgcFrqS3WqgTxegkOHkTBWw4iaWkmJGb9guxLVfpEgS57nJamdCgYTa-rbkqpnqCTFQhG6EoYLnB_0odYw_oy_l4iwnMDe091a41F-m-lojbsKy1gIgUHuAL27MTc3FCnqT8ZuogF9t0Brii4JEQz_mvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWkbYqJ-DsgHKOFZ72AW5KI_ulep2SmcIEh_hyOuM2lDyS5ZqOpOLl3483BuKPb37ptT4d89d8QiDRfQA-g1uuUegM_KUevcTT295BN7E1cMbCI8GzDF7YLfylSsxj2j6IA_271bcdqfhzRBU-oo9SgtgU4VmcRx41yYTb7KCs3BnY9TT5exeRkkOA1MDztMhxUAc_Qnytjaji3UfHxQcaYjcwzf9YljppM_-SRPDBZGXvRQS8Ro7koAr8bVDDrQh37ipATviXnXsYsQusdggGD0sSdAWtB0WdimPSMdRb-IhERi0EnENBpv3xAJ-C6xqofIf1lWkoF2xx9RU0ViMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=N22gMjxebnSRk5xyGbcDmBS8Byi6BT3xnKuuf72WlpYxFaYqqSt17ysSGpN4ieWhbX6ngbj3cp8sD3SEwoPQSDVf_rccWdS4cQKHovt5_uBBkeQXlIqQ8JaeVuCGm3mViLzCUpEobJBVjKeAIC7o8VOgmqmtu1rT1VfcASAkYD_u5bCM_kWqNiYoE_p76CVMyv40XbHJ6kfKCLS4t7N4RFFeUzYcSlm5iJ8DB5lzFPWh-olFccwhwIZ8gsZNyhStF49M3TLMiCBChEuvzi2IUrZOis3bd0dHz5Hbbwul5ORuvREpQmDJtLWzVoZU6Wp6WR2djgN2zn9kszOAO3ElOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=N22gMjxebnSRk5xyGbcDmBS8Byi6BT3xnKuuf72WlpYxFaYqqSt17ysSGpN4ieWhbX6ngbj3cp8sD3SEwoPQSDVf_rccWdS4cQKHovt5_uBBkeQXlIqQ8JaeVuCGm3mViLzCUpEobJBVjKeAIC7o8VOgmqmtu1rT1VfcASAkYD_u5bCM_kWqNiYoE_p76CVMyv40XbHJ6kfKCLS4t7N4RFFeUzYcSlm5iJ8DB5lzFPWh-olFccwhwIZ8gsZNyhStF49M3TLMiCBChEuvzi2IUrZOis3bd0dHz5Hbbwul5ORuvREpQmDJtLWzVoZU6Wp6WR2djgN2zn9kszOAO3ElOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=QnQ1Nl6QUZ7D_ccMfIrlhTkV2tE4zzfAHaml6IM3qeoP_yReSHy3zWs8BhmVLAmmGs0DvB1pwZUoZ8RwbVBEuISfEofgpCrVwzU1R9HWUJHcHfOycCKedeFsbqQ-HLlmdviBEPTS42AmRasQt5E14ecgFEULw9lZkC5dhFHQgji1KlP81DLbe07HosCRySrdyI7p-nH6ek1N0ZhQcAUV4Pr29zGySV_eeWhqMgvl0uibaBiOtWEl_QYPGce4Vd691SC2NpGF5AtYDv18lQzU6-CU2TmZcsrRKdZDR44BApCrer97TFjgTpQAeuhS2tgRG4B9tXBY2GEYGxk0lky-fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=QnQ1Nl6QUZ7D_ccMfIrlhTkV2tE4zzfAHaml6IM3qeoP_yReSHy3zWs8BhmVLAmmGs0DvB1pwZUoZ8RwbVBEuISfEofgpCrVwzU1R9HWUJHcHfOycCKedeFsbqQ-HLlmdviBEPTS42AmRasQt5E14ecgFEULw9lZkC5dhFHQgji1KlP81DLbe07HosCRySrdyI7p-nH6ek1N0ZhQcAUV4Pr29zGySV_eeWhqMgvl0uibaBiOtWEl_QYPGce4Vd691SC2NpGF5AtYDv18lQzU6-CU2TmZcsrRKdZDR44BApCrer97TFjgTpQAeuhS2tgRG4B9tXBY2GEYGxk0lky-fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGm1YegJEQIj7-ciCAU-P0kiufSlBaROLh5jbQ8VlbaPBakCjpdCP_9u7T1-i8Dtf17xh8BfPuEc9X-Uyh-INrWXzY_8r6hVrgwc8jxELcpgaMdViwaikK44fvP7WdfA264acYKTnk9h2tCb6sb6dNlY1x55cAfoRUBiyub2xHrGv3VZrEb5ofTHYVlpy_37dQCQJwilKW9GaLH0taAKXXZw-uBg01YDPtGDtbOr3xRg20fq6dYchU02S3g6Yn_Gqd2BpemavMUplnA0fWYqkr35jq6XYxH2Vr4maEMTILrLo7o7Yv54HCJ3IodcCCry_bOntwWfNdyhIXbsW0bwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKQRXvaLTQEReiIooCJOucPQWqn-PpbHU8eiRwPYFpjanqgDSopn8hN4NjQ8wPwM_k2BhKtzrDt6Y7MTOg2bJm8nQoQS-JnzjmmXYmkqGWAsC69TLsxPYCxuaqVmMA9T3BqS03mbPyR-NBwnUbtdcwssaxBwWf2NPWpe5jWUQN9Ok6AhNhbk4TTRdeJux0uyULIzwEGkKFmpS_rbmh-xpwoRl_rw4majt51wTRExlMVjuJ4G0-TehWHWGwP8zf2Akm9gR-4Ok7opwcmhz33UcIhD5jm61ibfgUrMFn9rzVA35qfkEjoNjBK4GBavAQrpniZmIFbDQsr0A-rnFLtB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHojV2FuQD2eLLqcw8EkeUOjsrrCEhalka0DoyCoUUL5kD3F4rqgV3ACItHt7bvwOzRK1QoMmJY0h3kVJKZg4mmY5Ih8wzGUsYhvbhS6hJRnkQC5uGnTvdI7b-eplKvEg0EwG8PbmsW40WjWD5k85mqSqbsjMi63Hpfl5qeT5y8bzlwalWW9qV1MS96UzcqZm_CSmUgiSpMmE6NPSQAs0Z6AV2vyD8CiSNiNdxQxcraMmilEHQe9gHgkcCrWxbKM6wLxGT1BVb74AkucT-0g4Y7-U1h5d6ei-Cin9DqPmgFMiTyvnK4Bw-pJOSCAS0_jJt7vnRun2v_CyF0h2xhYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWKeE35vVU1iwH-JRYdQC9OCF3BtGYmZm1_Jfau6lZv8yu2jPPDbOfa4boLsQkwjYcR-Mv6UNLFPnacX4DFmECXwq9dsg_EdoYczC2NTJbwTa9k84MReZsR4hzhF1eXMlWIB2NjIhez8nCAuKiBwsozxlnJj2HDaQAcppOpbaRb3iFLoOYrVHNjcg_AajXHDSLtJQrUt6w5AVjxDzJioZL3M6pNijUQzAtJfbSbmdOOi5aU58sOmU0Ll2p0ibwfMfZUFkzub2CsSwn-zw5OjfOfSMk5GjbksVZLpBzt9zw-8Y-Sy76YX1OmlO8z3MTRVkO1XptR9mmmTSwA2RRF5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ps3DNR0lKjtcQuhNiRJ3sJ4NMhIj8CGKPNLj_UtWdQoQiyFk6xM06lvJjdSMEF2RkWaWr_I0g6H_7p9bSQEVUIswF529uhnEckR_Pv1uO2K0EAR-pSCMUSOOqTjHYdecZyvtd8TqbjykR1MPcwx4AP_jgtAnix_9Jremc6Ewx9b3xhZe_m68vj3jU70neqYfcE7cr1aogXmT2giwiXHUP-ggcx_yiysBr0Tf7bJHno2shCeABU0MieXfSut7xMyAL_PzVMRs06RWRVhObfWQAKFubBWlE6c3tXpIAB8NciGZPI9NE9fZXlm0c_BhkUFOPNBvpDX2E_HGexbW8bH-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=FL_JR8-Dd45TW317ECNXDIh6ESRjfSsr_l1ea9WH2x7ufJxvcfjo12AeS3sQDJwTkKap_gSwDwVNJzNFtg8bs2ZBekDb9kbwwk3CJ0rECxeI9nPjdQthYZgl1TLsFgBYEhKM8XULS2O2bQ7g5rrSG49_vRhf9HQCYt24PyInX3DhCh9amPDyTNg1kkN4UI8NLGpIUNTYl4F_GdUtA3HK7WpXnBkFrBsODuZsLdi7hwuzBWK5nmiu-_i2VOKEmT1aY_kDuC3Feh8H-jfcCPYP5WOoUYThYq68I9CRc-YyuNiF8hAEYMH4d3Z4W6veurxbK6UDSJkKsTlEDVcStujjeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=FL_JR8-Dd45TW317ECNXDIh6ESRjfSsr_l1ea9WH2x7ufJxvcfjo12AeS3sQDJwTkKap_gSwDwVNJzNFtg8bs2ZBekDb9kbwwk3CJ0rECxeI9nPjdQthYZgl1TLsFgBYEhKM8XULS2O2bQ7g5rrSG49_vRhf9HQCYt24PyInX3DhCh9amPDyTNg1kkN4UI8NLGpIUNTYl4F_GdUtA3HK7WpXnBkFrBsODuZsLdi7hwuzBWK5nmiu-_i2VOKEmT1aY_kDuC3Feh8H-jfcCPYP5WOoUYThYq68I9CRc-YyuNiF8hAEYMH4d3Z4W6veurxbK6UDSJkKsTlEDVcStujjeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=oB-TEonhAdbyMNI4T-mlSWeg4wzhEwXG4-btUi4MgvmjDaDRwKq0nOdzUdVXwAo9V4urdG-4eS7JGP0W6rbuWYHSMKLwHeG2B7tVhWMAVo0SGbe5fsxB2CQa6ryPCG1AxB6mkZG8Al3ZQa1zYFHmokT5rKy0azHbmZlGetUz-39ij7nOLqSy8ZnOygnu2z1f0_Ggr27LpGq5BS7IXwW9cTSi0_7_wV_7A6rDEA0arVsdINyfF57988zdVhWEnOaqMa8CUoEgKlLlI4_YulWZl9unpv96NVO09b8i5kSyobyzPdpndHYm0gpvxkxf-gmkoyoKXqPFleuO39fwisSF0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=oB-TEonhAdbyMNI4T-mlSWeg4wzhEwXG4-btUi4MgvmjDaDRwKq0nOdzUdVXwAo9V4urdG-4eS7JGP0W6rbuWYHSMKLwHeG2B7tVhWMAVo0SGbe5fsxB2CQa6ryPCG1AxB6mkZG8Al3ZQa1zYFHmokT5rKy0azHbmZlGetUz-39ij7nOLqSy8ZnOygnu2z1f0_Ggr27LpGq5BS7IXwW9cTSi0_7_wV_7A6rDEA0arVsdINyfF57988zdVhWEnOaqMa8CUoEgKlLlI4_YulWZl9unpv96NVO09b8i5kSyobyzPdpndHYm0gpvxkxf-gmkoyoKXqPFleuO39fwisSF0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3Bdm3CFJKVAY-pWJ20MH3AdhV1EejtAialNUcfKFGOQWKuNxM6bTSQ5dl0XcgnvKtCucI2utO7q4ITu6bHPiwT593gxA1LvwNa6LLiYBjKw9pOyv2DlOKfHlDYEiqbRJeKi46G6hKKx-c30yhXoJMu19P7ZPpY6pCsEtTe_7_zZm93atolH6e6qY4V4HKI99dPp3I3BC5Dc2fjC68_icHu8jQRVQWnaARqcJ8HFXdUcqG2gbqFh7lt4h9UGqhxmMhhf4Js4MAdj3CoiCm3z3zB_7PFQqfl9yasWi_4NS29LnG390pET8xdEepYilNedjffPHkYota8sR4KtgmNd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZHm-zTzZihPyPMCw5FlMIeLoWglWuZoCe8aso5pTuWPi8nNcQmVDXhm9bxU5lLPfZ1s2W-KTxbgLQypscvNQdpX-mMJxHAbHHrx8N6PvtCqlHbIMQ1b429V4xXMWSpjwMBVphTj1CFTruHvl_dacKLpkTp0hLe4shMzxdvM7UfD9xZKp8k9gxu-7WmtVI9ejgrdQ3sAcWubeLirARQVDhBFaczW1TFnUAJzhBar-q5WSiq1mJAceeltF8LZ1cGItnJaAipCb_AAHwTAZVLldq1GPkBaavnvKEh1urhr3oiOxL4AQyvW323PLwjxBmkwoEtr2HECi7BhNFP531sJ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6NHAn8ravIdRx_vQa_YSXua7wUw7RnXMKfCsmWARPzOwE3O21NUInYAdPMWrs5Ut7gktRGohBlv6YQW-pWNU2qlsZNuKCfGhWM6E8aBBk4XZFVSces5XuaGykQOfppyTWjA4TLb3Nmi6RSO0-Sini3EG43mZFw1pzxFlS2OLo3txobBree0ApdTlp0gFrwCKYt99JuMykGln5kunxMvVjVsVPq23QhQZQU3e1bk3FNtkg6LUCfIuYw0-2BTUh6ZfmP7oSJKxGnVPGjJmmid_nldsgQXFR5A63ZbRDRRZQSdkzzU_wRyj6Dm0QNqpFnA0TJhLJub_E3fXHLdYFHAWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=f28pb02p_AaVWa6zsfMozlyS7GWEbbTjNxRjJWtEy0vxlhwl5dxrnVvXovpu4YKYTy_aU_ID7DeyZSA-Q6VKvlT9jtnuzSF5dITSbuflkmFWZbYBVj7TXwbWij32zYhmzjdRdWjaod8mYHbukoZRPUOqBlC7rhFve0kixA_ypjwLaNe7g46k7UHlsYx8lsax_LmTm4Pcpce-lHlexJTEaJNt4oXXaQRw6VCdLI7g0QY8BwydojEHXdTRi_CbsPznaxzTW2D0K38XMn90GkALu-Z1E6ruCdR5gbLxwWuZ4e68MmTZzNXbt74agYbWhhjA2cXaUqT8ZQdxWbMTW6kmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=f28pb02p_AaVWa6zsfMozlyS7GWEbbTjNxRjJWtEy0vxlhwl5dxrnVvXovpu4YKYTy_aU_ID7DeyZSA-Q6VKvlT9jtnuzSF5dITSbuflkmFWZbYBVj7TXwbWij32zYhmzjdRdWjaod8mYHbukoZRPUOqBlC7rhFve0kixA_ypjwLaNe7g46k7UHlsYx8lsax_LmTm4Pcpce-lHlexJTEaJNt4oXXaQRw6VCdLI7g0QY8BwydojEHXdTRi_CbsPznaxzTW2D0K38XMn90GkALu-Z1E6ruCdR5gbLxwWuZ4e68MmTZzNXbt74agYbWhhjA2cXaUqT8ZQdxWbMTW6kmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvFsFrmUewtgpcZOOmb_rde8hXs6mNkgCRTRt1WoT3xck5sYNMXSE6i1fEDT-z7hMTOm5o4t4V1DiY5LvWXObUEdce-Ibxr_klALbnQfimD1CJj0G9KXqhiPnhcEqZv2Yk99dsjx0jeaLtp4n-QOe0Ym3xDflGgUuf60JZdnd3QIYs16P-_VMBgHYax4CRhRwzszvc6Rx2NT8AUhmovEeoJSsi2nh7CrcM-Rza6nBPrg4-fRmOPM4dinri8LwIyBBDTI7KhpAuieWhNS1GlM7hAE5lp3l59kfkroW0fdfnzgBUCHLrA283BzZIvVgg0wwbBeqtBNFViraEp9xDHFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxbBGtVSMimlS9mUVmzhIw_7KjQR3y3RLgfHvTw-yCxTF1kjCoVpKiaT9DLUXESv-VEZmFK85qVgImk20kB2_EMQ2b5V4gZnCypMLvRmKdz6Nbk2Lxm-pDcxEzBols5iHjMlgB5t69Uc6LjK0ypOh46qw7ikkFxNdpCBoX8Ez1fl6ByejaGe8NAdMeRp4WnBlUFe2BNRQd031BcgBLx5-r_1Px5itA-0xj0kM4YNSgybEWfpUSck8vPgyxJNcxRlFHFOYbCEB5bSFloDVoiQLldnrZkUQGFQ7-aI9zGsMMCuwyip9maMEpHhPa1CS6ZbpLRtRqmjt4__ZHKg-B784Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4zLsTaVJLV84k6FhXn-8k0X-HwwGwXo05hr6bU2iFC-os0YxLcjVb5SH5sPF26hnxR7KN7XJiCEYMrI59lkEeHtC0oRAHBxCOGTyNTwMl-X8gEKmfp2A9tMMlw03VG4s27vdz5eu6mB5rKtdOF_-jWh4W5L6qAJWsrFdif8Fw7lDAN8Dt06wJJ6HjVgREJVUPdXxwDiCUyGVVC5I3QfDga36XM5k_4F0QqOOegnkHTy4ImEZ_mWWXLyO52c15FSbC8FAGLMM58saDKectUNIDlARIVNkSIaaGa311RuuKFuCoFbh6kxM_z1Q4DeExYL2t5Q1bYzMlAWfFXHa_zOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
