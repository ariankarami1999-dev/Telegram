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
<img src="https://cdn4.telesco.pe/file/EmEZlm1nMV5hBiIdCVJFN1mdYssP2dZU2TVFB6YHsCUKj9veXIQaxJveBg5tsZSJ2roeG04ZdqRo4Zxq1RGagNBJ4z_RIlwo_vl7b7rYQPGRwgZylfzoO-coPoTygQtERN4Vns_47fXeAzkJ2MyjmVhUVFkf2zozMSWqAyF_BhemcBuxaheeGpEsIVg9RA7DCh51VjyLgxQihoRCZo6-wTjPxjhkl7k-WWtmyW2leXbHd57qMnjK1WQ0x0HBDFupHQQW1j4NfVbiIEofKzecdoriFn6Wrr0yJlfFxLz2VGQGSUiLKJtjEqukKoFdZRrx78i1bzBdDbe9gfK519QybQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 428K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 14:22:34</div>
<hr>

<div class="tg-post" id="msg-19649">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">حمله عربستان به مأرب و الجوف در یمن
@WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/19649" target="_blank">📅 13:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وای نت به نقل از مقامات اسرائیلی: بعد از آزادسازی تمامی گروگان ها، دست اسرائیل برای انجام حذف هدفمند در غزه زیاد شده و اینکار با شتاب بیشتری انجام خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/19648" target="_blank">📅 13:26 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الجزیره : چراغ سبز عراقچی به شروع مذاکرات
عراقچی: پس از بروز تنش‌هایی در هرمزگان، در جریان مذاکرات سوئیس، تصمیم گرفتیم یک خط ارتباط مستقیم ایجاد کنیم تا از بروز سوءتفاهم‌ها جلوگیری شود.
@WarRoom</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/19647" target="_blank">📅 13:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرده است که گزارشی درباره وقوع یک حادثه میان یک نفتکش و نیروهای نظامی مهاجم در خلیج عمان دریافت کرده است @WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/19646" target="_blank">📅 12:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1fWLU2EDeEz-bMSbpPzrkj0r5zMdekQak7WwDW8KDgLrDG4PBkOU4DGln7Kc-unsfM-AnO05GgzFUnuQNlyQ6nWBO79uOcJU-BmbJbu4J5Vc9umFWU52BZ73JIfqJoIZNa0HAQikfWy4BiVLQ77HGuBcAQ8nfZhrJG-Bfsuwb2HcH8QOknD-WkLzkykLupf-9qt9Q8ckeuTJRojTwLyiTAU2DxjuxqsFqpKCCgXYLbqVkgflcpUL8bc5L-5y0Au7ct7wMD5crLVlgaJZ24E3BvMfsmgHFJrxQunAhHZTl_JsrbzZP27F2AZqK8NbEEdAQ5js5jv191BZBkhezlQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرده است که گزارشی درباره وقوع یک حادثه میان یک نفتکش و نیروهای نظامی مهاجم در
خلیج عمان
دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/19645" target="_blank">📅 12:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/19644" target="_blank">📅 12:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwuexH2kQRM-eDQDb74-TPy-HqtzOk2fqatDGk36U_i8Mln9jytf04oYE7AeCuSoaEGV9iawFwrC-iZTyAXNNKbd9KDXm93VsWelmToF8MF1y5NODNkjkXyT5a-7NFifMjO5o9n63SzOEMi_UtPhp2gQO9sJuJ2_jF4ijg77NVW-FBwUPEZP8zmGs1BqSVkrJhLCrediB8wsWTnIbNZ8bWi6rwV7KRZ3jIvc6Ua8_pzXmLaTRVrQ8Bfw_SqzzRgGfRdFlrp-x9a0NNq0Z_JSe2I24HiF8NAv7WKIhTxdPiXzXfbuA48Vqu-Lq-07ozJVtfX6vnBqg1pkFgBPMaE6ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در همین لحظه برای اولین بار‌ آشکارا یک هواپیمای
C-17 Globemaster III
یکی از مهم‌ترین هواپیماهای ترابری راهبردی نیروی هوایی آمریکا و ستون فقرات جنگ با توانایی حمل ۷۷ تن بار در حال انتقال  تجهیزات/مهمات احتمال زیاد برای کرد ها در اربیل عراق است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/19643" target="_blank">📅 12:16 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فاکس نیوز: جی دی ونس امروز در جلسه شورای امنیت ملی در کاخ سفید شرکت نکرد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/19642" target="_blank">📅 10:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سی‌ان‌ان: پس از ۱۳ شب پیاپی ، روز جمعه هیچ خبری از حمله به ایران از سوی سنتکام منتشر نشد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19641" target="_blank">📅 09:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8-M4YZzAIN4T8doIuwGHKcrgOS_2nj5O5iBhmsKvLozHqLKLNNPUs3ipDgXgiB3TfbJ3e6coEwTIYkofCQhRIlsp5aPcIkFUYwWQyiraHbItaTkVJK0Ai3P6s-EiizQoMr3bSfQFbrvplB2mMd3mxWv9Z-3HWl_oT4m2X11lH8IolRvxjlx5xDSAmXa3pAj7k0oiGXK37BBV2UFqeVnLdHvDWZaAHDcVNID2HAhvHmyTmPx1HYT18EjnebgnBJpXKubQ9fJNc6vd2X2y3Ort2PLB3XYCTRbtSYju1P0SKngAarkzwakIK-7b8tdXkkwXcWcROUc06EdESqOka0yyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : عکس باراک راوید خبرنگار ارشد آکسیوس به همراه تیم این خبرگزاری در مراسم شام کاخ سفید که بخش بزرگی از اخبار این جنگ را پوشش میدن و ما رو سرویس کردند ، دیشب اصلی ها نبودند که حمله رو پوشش بدهند ، در جنگ آمریکا و اسرائیل با ایران، رسانه‌ها فقط نقش اطلاع‌رسانی نداشتند، بلکه به یکی از میدان‌های اصلی نبرد تبدیل شدند. انتشار سریع اخبار، تصاویر، عملیات روانی، روایت‌سازی، جنگ اطلاعاتی و تلاش برای تأثیرگذاری بر افکار عمومی، همگی بخشی از این نبرد بودند. در چنین جنگی، گاهی یک خبر یا روایت می‌تواند به اندازه یک حمله نظامی بر روند تحولات اثر بگذارد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19640" target="_blank">📅 09:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5168a521.mp4?token=U6lpRX4oX6zmH0CtOhUfMpO7lxJMiwDLmg5E0l5jiYTOFm_iJ9iYWHwL9NmrCG6L8rg39BkoGRG9ZIJ6Fv-Q5ceZsCBHuZfQLQxKlJUvOFbr7kxrrOMirHDkNx8652zlg4z2XPFUMMk8qgANyTprPhHU1MYernumAw1pUNV0qlK91jdNmTBkTtqJEvHeiWBb14_P5FvM-LJvqsWzAHq-kr7K9euQ_3va7-qNM6dhEfSljYIqpCxALpsRu5hNWlxj_seyJc2ywQDqsxD4Wm_JtXsV3EFmNVPv1IKiP96fTFUfI2ULqbKQTA6WE5NO3qGbK3I-KX5MKu4cwRtc_oIc7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5168a521.mp4?token=U6lpRX4oX6zmH0CtOhUfMpO7lxJMiwDLmg5E0l5jiYTOFm_iJ9iYWHwL9NmrCG6L8rg39BkoGRG9ZIJ6Fv-Q5ceZsCBHuZfQLQxKlJUvOFbr7kxrrOMirHDkNx8652zlg4z2XPFUMMk8qgANyTprPhHU1MYernumAw1pUNV0qlK91jdNmTBkTtqJEvHeiWBb14_P5FvM-LJvqsWzAHq-kr7K9euQ_3va7-qNM6dhEfSljYIqpCxALpsRu5hNWlxj_seyJc2ywQDqsxD4Wm_JtXsV3EFmNVPv1IKiP96fTFUfI2ULqbKQTA6WE5NO3qGbK3I-KX5MKu4cwRtc_oIc7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تیراندازی در ضیافت شام رئیس‌جمهور ترامپ در کاخ سفید @withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19638" target="_blank">📅 09:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کلش ریپورت : فرماندهی مرکزی آمریکا امشب هیچ حمله‌ای علیه ایران انجام نداد؛ احتمالاً به‌دلیل برگزاری شام انجمن خبرنگاران کاخ سفید و سخنرانی ترامپ در این مراسم.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19637" target="_blank">📅 09:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ در مراسم شام انجمن خبرنگاران کاخ سفید (WHCA):
«برای مثال، در دوران دولت من، آن رژیم(خامنه ای اول)که زمانی همه از آن می‌ترسیدند و بی‌وقفه به آمریکا حمله می‌کرد، سرنگون شده است. رهبران سابقش برکنار شده‌اند و حالا توسط یک دیکتاتور گِی (خامنه ای دوم) اداره می‌شود و با اختلافات داخلی دست‌وپنجه نرم می‌کند. اما من به نوبه خودم برای باری وایس در CBS News بهترین‌ها را آرزو می‌کنم.»
﻿
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19636" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19635">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92de2ca506.mp4?token=HEy5VG_lXIV77iPIKlldApEvu3m5wtzJl2fXs4vscb_RbMZAxcH776V69GTWXTJ4MItA17oO4WaR_KSs3YYQYUu8P9nDd8leIBvwp5j6be5SIMikRxvc4xNk-VpMJf2M0URv_I4K6XIbgm4E3JoyAhXBJaj32bZ8r2U-rDHo2U7TdNB2fJW7W7NfrZFFlUhdvyaiDTDdMezMTJrwAj5tcKrD_szJxFnFHJGaLVSyubW5XqqziEyee1F0oqzvcmyAo2ZaWCRNCTLjqHHA4Prx1o-E4YNPq0elXMUkwPN_UAFDz3oYOkkv42PHvrNwBMT29HZMwfGmhIlKmQUmpnnBlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92de2ca506.mp4?token=HEy5VG_lXIV77iPIKlldApEvu3m5wtzJl2fXs4vscb_RbMZAxcH776V69GTWXTJ4MItA17oO4WaR_KSs3YYQYUu8P9nDd8leIBvwp5j6be5SIMikRxvc4xNk-VpMJf2M0URv_I4K6XIbgm4E3JoyAhXBJaj32bZ8r2U-rDHo2U7TdNB2fJW7W7NfrZFFlUhdvyaiDTDdMezMTJrwAj5tcKrD_szJxFnFHJGaLVSyubW5XqqziEyee1F0oqzvcmyAo2ZaWCRNCTLjqHHA4Prx1o-E4YNPq0elXMUkwPN_UAFDz3oYOkkv42PHvrNwBMT29HZMwfGmhIlKmQUmpnnBlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به روزنامه‌نگاران:
وقتی من بروم، همه شما ورشکسته خواهید شد. مدل کسب‌وکارتان تمام می‌شود.
وقتی من نباشم، شما ورشکسته خواهید شد. کسی برای گزارش دادن وجود نخواهد داشت.
هیچ‌کس به دیگری اهمیت نمی‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19635" target="_blank">📅 08:54 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19634">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">از شاهزاده سلطان عربستان هم سوخترسان داره بلند میشه… @WarRoom
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19634" target="_blank">📅 04:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dkmc59IgapTQVZW6ugdAxeVjfBl7Sw3bPPWZF1GtCeTuMkfK0Z_9N_wX9nFEEgR-r_N5NasZdQcfEI4jePzzbUb8PdKtb5AdcBRj3ETIn_rHZ_qkocgX6LUVQCRPsFlH9gqrhS2Ch-wub9TxjpBWQvgo9ES-K1pROjjCYYxR6Bun23FvCeulnBWKnaCC0L4NZO4UFRds96qGbQHyHmG822h3teB0RyBvtA1DrHcqX8N0yj-2JieRROZUj4pOUvoXy6IbEffh_1eqm__PP0GLrR720yhnoaON_V1Bf9T50WxSmdZPzVwbkDTRmh44EiaRkzYEYQ-gi5Z-1Iej4Np4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت دو هواپیما چند منظوره بوئینگ پی-۸ پوسایدون
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19633" target="_blank">📅 04:02 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ششمین سوخترسان رو بانده پروازه در  اسرائیل @WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19632" target="_blank">📅 03:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وال استریت ژورنال: ترامپ به برخی از نزدیکانش گفته است که معتقد است
از طریق یک بمباران تهاجمی و جهنمی، جمهوری اسلامی را در هم بشکند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19631" target="_blank">📅 03:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پنجمین سوخترسان از اسرائیل بلند شد @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19630" target="_blank">📅 03:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نیویورک تایمز : نشست چگونگی حمله به ایران با حضور ترامپ داره انجام میشه و شروع شده
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19629" target="_blank">📅 03:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19628">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">با فاصله بلند شدن ۴ رمی هم داره تیک آف میکنه  @WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19628" target="_blank">📅 03:11 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19627">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اوه اوه هواپیما جاسوسی ریوت جوینت هم از خانیا یونان داره بلند میشه ! @WarRoom
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19627" target="_blank">📅 02:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19626">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19626" target="_blank">📅 02:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq1RF-beaQdVfahb9SHF61KtBX6veKkt76lSk3MXq5d9NQuIUoa3xo-9OX9QxG5c_pD537FuZH3fq7kOrUvecGPE0Yh4o_QWJdB3-9GzxY59PKJHG5VdO-YZ-7rV7hIOpEbTyN7JCqyE8iF3XyZpkeN8jWP8zkMNCPqFivYaMVpKATu2THPAyembNPgxQrf5BH3LYMLGXl4OpTKtZ2aAV5nLXHIWu4Nb6LYKugPC2-J7o1Sj0kWFKOTK-qamJpVbcw1n6tJncfUJSizT449wOMaama4uvFlDBHMeDFC4umdjtEZDKlv6ewJbOmcXC3wCIvK72VFMkusWSE7Jvfnm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه هواپیما جاسوسی ریوت جوینت هم از خانیا یونان داره بلند میشه !
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19625" target="_blank">📅 02:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_WKVyLNiuHkPr5rytR1xygqb3Ul7ThAKsYIKgI0VmIFjb3BZyJyMqGC829buIZFMCNsFvziEnBNk77oweVG01N09ypJTe8zWI65FnRbW1ahA9HgpdpwEiS0ZnZqbpJJzZgoRBgKsIsmuF66hHMfJ-4mjL3u6hpm9ynyYUqBkOkm1m3i3xkEs7abDSXdMXT0FzN0xWqDb5O-MnDFQiVI0MhUcBnRucyBFDGZYfYufYD6e5dXV4-kGI18pud4rkglpt2WOah4fGlH1RCt5HZeKWo8XJdJqTzYBQqEDWROJH55Fqmxs5l3DG-Xe17ZYKZVEhVMyM54uWJiZJPJOu5ibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از شاهزاده سلطان عربستان هم سوخترسان داره بلند میشه…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19624" target="_blank">📅 02:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19623">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هاآرتص
: تل آویو می‌خواهد تهران را به حمله پیش‌دستانه علیه اسرائیل سوق دهند و در نتیجه برای پاسخ اسرائیل، مشروعیت بین‌المللی فراهم شود.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19623" target="_blank">📅 02:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19622">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJ-En8nIm-LkcVN6o314oZOr9ZlTqoxT-nYZbcrN8bslS6ZVZWfi_sWbItBO4HsvHb7A0WFUKv0W1rSk1boQ8EHFybZAxE24VbZ3X1bYVOx_8nJckFIdLEFjOchq2PzhGKu2zJvxfcq_hHpfRwFnShVTZuC2ksHMwtKrPVc1skPAqJvN0s3HrQPQAqJZTh4RWFy3DxkIMW6MJswFqKsLoqC-9B9UPXJdjnk52-Aux7gs_JU4f5jiCvcOTg20Om3Nz15zplYkNXQX-C3v6MVV5mHLoasRRI1OBi0kCGxsd73C5CBkDVKmGmNVUG5NnRYTu7kkH3UisCZNyGlomT_7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با فاصله بلند شدن ۴ رمی هم داره تیک آف میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19622" target="_blank">📅 02:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">۴ سوخترسان دارن از اسرائیل بلند میشن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19621" target="_blank">📅 02:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتاق جنگ با یاشار : حدود ۱۵ دقیقه دیگه میشه زمان حمله دیشب
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19620" target="_blank">📅 01:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرنگار کاخ سفید: سنتکام گزارش داده بود بعضی اوقات ما به ایران حمله نمی‌کردیم ولی میدیدیم که کلی موشک در آسمان به طرف ایران میره، بعد می‌فهمیدیم که کویت و بحرین و عربستان و … در حال حمله به ایران بودن ولی به طور رسمی اعلام نمی‌کردن
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19619" target="_blank">📅 01:28 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آسوشیتدپرس : ارتش آمریکا یک کشتی تجاری را در دریای عمان توقیف کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19618" target="_blank">📅 01:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19617" target="_blank">📅 01:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19616">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کلیسای جامع ملی واشنگتن اعلام کرد مراسم یادبود سناتور لیندزی گراهام در ۲۸ ژوئیه(۶مرداد) برگزار می‌شود. این مراسم با حضور خانواده، دوستان، همکاران سیاسی و رهبران ملی برای بزرگداشت زندگی و چند دهه خدمت عمومی او برگزار خواهد شد. دونالد ترامپ نیز در این مراسم…</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19616" target="_blank">📅 01:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19615">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19615" target="_blank">📅 01:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19614">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">علی عراقی ریدم تو سرت به تو نمیرسه از چنل بدزدی ، فقط برای ایرانی‌ها آزاده
⚠️</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19614" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19613">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19613" target="_blank">📅 01:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19612">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRY6j7LcMqrtV5JTe3mcOaebHL2299ahBsMCPHVQ9eL-Zv01WiFjvXIdE_A-bAgtbVk1Sk4Z_eoEMFA1tLW3l38koUJf1Oh6eGiRQh8fPbmhD7PqfvWuy6vzfbcu5tv4DmYmq1qpSRef7Bd4dMT20ABMqtD-zsiQC8mWQAmnFuEnvT3tIJNW3V9fNFb26lK8enSKuuPSGxOujyrTdK77d4Z1dhQfhLXsHLKMNk_7z59XcBRgAe1HR6sJPVuBcYVwr5zAKmIQyhqJcVZZwWHfFqoK5yXcQwm1GctJJaBVQQGyn7kUemQ-K3SD68RoxO2m6upf_hdOqZnEhHkMTHaGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک الان
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19612" target="_blank">📅 01:12 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19611">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">@WarRoom
کارمند</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19611" target="_blank">📅 00:52 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19610">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شرکت هواپیمایی ایتالیا پروازهای برنامه ریزی شده خود به اسرائیل را فردا لغو کرد. @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19610" target="_blank">📅 00:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19609">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شرکت هواپیمایی ایتالیا
پروازهای برنامه ریزی شده خود به اسرائیل را فردا لغو کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19609" target="_blank">📅 00:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19608">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای انفجار‌ امیدیه
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19608" target="_blank">📅 00:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19607">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش صدای انفجار‌ بهبهان
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19607" target="_blank">📅 00:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19606">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19606" target="_blank">📅 00:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19605">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک تایمز: مقامات نظامی می‌گویند بمب‌افکن‌های دوربرد B-2 و B-52 در ایالات متحده در حالت آماده‌باش کامل هستند و هواپیماهای سوخت‌رسانی هوایی بیشتری برای پشتیبانی از آنها به خاورمیانه نزدیک‌تر شده
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19605" target="_blank">📅 00:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19604">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e4e60bc5.mp4?token=drbHAnEw_tNgZnuxFjNfOg4iFtwt90z46xsu92NkVrutxI0k0zBhNkeJGO-7ZMR6iKHB2tkPB6NQ9Lv71E4HL3jvPAbqBhoPVXt_MIG5QTJf8l4zuXcH7kS3JugvmeWejiyQXh8HMTteMeCTPTbq6MZ9iJvJQaiVz0JycT5AKBYSDsdb85dlVHOoT8tI13iaA_z7hPcUcEMso3QnXmoYeaujVHFCKhGDAlzItuNV9tsdXlkDOuigW86V5_WCl2PPuDBMVlvYnMW28LyyHndcX_gb_2Hi3zzZKRc0TI_sVH3WdJy00yh06b-D2k-rUvVkUXWefg8BaiTWUeh7aP0PHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e4e60bc5.mp4?token=drbHAnEw_tNgZnuxFjNfOg4iFtwt90z46xsu92NkVrutxI0k0zBhNkeJGO-7ZMR6iKHB2tkPB6NQ9Lv71E4HL3jvPAbqBhoPVXt_MIG5QTJf8l4zuXcH7kS3JugvmeWejiyQXh8HMTteMeCTPTbq6MZ9iJvJQaiVz0JycT5AKBYSDsdb85dlVHOoT8tI13iaA_z7hPcUcEMso3QnXmoYeaujVHFCKhGDAlzItuNV9tsdXlkDOuigW86V5_WCl2PPuDBMVlvYnMW28LyyHndcX_gb_2Hi3zzZKRc0TI_sVH3WdJy00yh06b-D2k-rUvVkUXWefg8BaiTWUeh7aP0PHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : ایران کی تسلیم می‌شود و واقعاً پای میز مذاکره می‌آید؟
ترامپ: شاید تسلیم شوند، یا شاید فقط بروند در یک تونل و قایم شوند،آنها تونل‌های خیلی عمیقی دارند که می‌توانند در آنها قایم شوند.
@WarRoom
🤣</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19604" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19603">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تلویزیون رسمی عربستان گزارش داد که یک کشتی عربستانی در دریای سرخ هدف حمله قرار گرفت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19603" target="_blank">📅 23:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19602">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: جمهوری اسلامی خیلی گسترده تو خاورمیانه درگیر شده و همه‌جا حمله می‌کنه.
اگه سلاح هسته‌ای داشت، حتماً ازش استفاده می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19602" target="_blank">📅 23:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19601">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرنگار: شما می‌گویید که با ایران مذاکره می‌کنید. چه کسانی در این قضیه دخیل هستند؟ ویتکاف؟
ترامپ: تقریباً همه. جی‌دی، مارکو، خیلی از افراد مشغول گفت‌وگو هستند. این موضوع خیلی مهمی است.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19601" target="_blank">📅 23:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19600">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6ukn5ku6J69AOcezU3fsug_DFasKR11cg-X1H9Bd_cx4NNBjOU0oBM_2mFHjGUHEVn-L3YZncdQQCy0gKtL_RM-nPxIKrnC1RQusX8i1fIIloP3VFkPt23e0GUoYxwrYg0A4KYMPCIKoE1dF4QaqhS-cj5CLQosDBH3csthTUHkl43Jenww7eN6_q6dKiHRl8UtMy6cVPkH1WcT9tTfLkh_bx2kq8leeXg1aWlSy-7uQzvBXE66BTDybMcXpOsBsMOKZtsgWC3xiDP3Y7gji8sL8pBZDXejuFF2CA5h9bdo4JhC6n9lIl8E2w-ni7QU643Ov5_UKbk3Uw8f_uXQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگنده های عربستان دقایقی پیش به بندر حدیده یمن حمله کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19600" target="_blank">📅 23:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">موج شکن رژیم
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19599" target="_blank">📅 23:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19597">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dfff8f4c1.mp4?token=MulTVhmAffC5mMcTN3dKpugQEC2U_v0sfhO2KU3ep13tK6-T_X9xsuPqgc5A-QYBpYWiSSiTXvq2wVnhJCpg6G_58HYZdTkdutTkGzvMkQKTdIxCwY5Ao7WUVLtLO64R-xUanxfuXLMFtK-2LU0XPvWF2u152ZPjWPnMQsHoqqYaj3F2T1W34QEhVO9no7agBvBXZ-Rr_rwQbyjSMleBIW-3XcuQsMEL2_P51yzAz_frJkgSTk9MCpHJMvDR9qy4SFIz9f-al5C8v6qhxdhID28DJgKxaS5uIetSLoYVC9KHXthArwlKjlNWQWGaKJBmPvlxrL5PJcKe1jkm5aaX1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dfff8f4c1.mp4?token=MulTVhmAffC5mMcTN3dKpugQEC2U_v0sfhO2KU3ep13tK6-T_X9xsuPqgc5A-QYBpYWiSSiTXvq2wVnhJCpg6G_58HYZdTkdutTkGzvMkQKTdIxCwY5Ao7WUVLtLO64R-xUanxfuXLMFtK-2LU0XPvWF2u152ZPjWPnMQsHoqqYaj3F2T1W34QEhVO9no7agBvBXZ-Rr_rwQbyjSMleBIW-3XcuQsMEL2_P51yzAz_frJkgSTk9MCpHJMvDR9qy4SFIz9f-al5C8v6qhxdhID28DJgKxaS5uIetSLoYVC9KHXthArwlKjlNWQWGaKJBmPvlxrL5PJcKe1jkm5aaX1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
وقتی به ونزوئلا رفتم، همه مخالف آن بودند. سپس، دو روز بعد، گفتند: "وای، این فوق‌العاده است."
خیلی‌ها همین الان هم همین را در مورد ایران می‌گویند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19597" target="_blank">📅 23:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19596">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ : همین الان که داریم حرف میزنیم ، داریم با ایرانیا مذاکره هم میکنیم
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19596" target="_blank">📅 23:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:  مهمات برای یک حمله بزرگ علیه جمهوری اسلامی ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19595" target="_blank">📅 23:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19594">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خبرنگار: شما دارید دربارهٔ منفجر کردن نیروگاه‌های غیرنظامی و پل‌ها صحبت می‌کنید. خیلی از جهانِ متمدن چنین کاری را یک جنایت جنگی محسوب می‌کند. شما هم همین نظر را دارید؟
ترامپ: به آن سؤال پاسخ نمی‌دهم. شما با کدام رسانه هستید؟
خبرنگار: نیویورک تایمز.
ترامپ: حدس زدم. نیویورک تایمز شکست‌خورده.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19594" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19593">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ: اجازه نمی‌دهیم ایران به قلدر منطقه تبدیل شود. ایران آماده امضای توافق نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19593" target="_blank">📅 23:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b48326b9.mp4?token=pipGmT-uZiiFin9Kif-d_6SDVB9LY0cQPrML-HIEEpyDNyXSleA4NCbvrpS24gqm84WkPy-bhvCW6hxoBzW0ffd7Xcl5Yo6Qt_mj-IqPBkcJc62kx3iWUGcX3OQyD4Cv4OFSuPBn8weoXZr0ULx0_ZLOCm92MB3yYj3cQh_PK9ujEokT_ndTP8VLvp5IcEemvzejw30_3IbFjhXD60A-AIPEFYMVWET61L5EIbevZXxYSTO7Si8KuMBz28iGcwHTCDguwd7BdqCRml8aV1-Jk4M9UbUVBOvHtTCqP-tFwWMNb4Bc0rv9MXxjIh5FW0oZaDXwszOi8wqQ5Hc8PI90rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b48326b9.mp4?token=pipGmT-uZiiFin9Kif-d_6SDVB9LY0cQPrML-HIEEpyDNyXSleA4NCbvrpS24gqm84WkPy-bhvCW6hxoBzW0ffd7Xcl5Yo6Qt_mj-IqPBkcJc62kx3iWUGcX3OQyD4Cv4OFSuPBn8weoXZr0ULx0_ZLOCm92MB3yYj3cQh_PK9ujEokT_ndTP8VLvp5IcEemvzejw30_3IbFjhXD60A-AIPEFYMVWET61L5EIbevZXxYSTO7Si8KuMBz28iGcwHTCDguwd7BdqCRml8aV1-Jk4M9UbUVBOvHtTCqP-tFwWMNb4Bc0rv9MXxjIh5FW0oZaDXwszOi8wqQ5Hc8PI90rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ خطاب به عربستان:تأسیسات هسته‌ای در برابر توافق صلح ابراهیم
"وقت آن رسیده که آنها این کار را انجام دهند شما دیگر مشکل [ایران] را ندارید. شما مشکل دارید، اما این مشکل روز به روز ناپدید می‌شود.
ما می‌خواهیم آنها به این توافق بپیوندند این یک خیابان دو طرفه است. این برای آینده خاورمیانه مهم است. توافق ابراهیم برای کشورهای عضو آن موفقیت‌آمیز بوده است. در مقطعی، آنها به آن خواهند پیوست این توافق هسته‌ای غیرنظامی است. بدون غنی‌سازی."
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19592" target="_blank">📅 23:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۴ : «طبق یک گزارش جدید، چند تن از مشاوران ارشد رئیس‌جمهور هشدارهای اطلاعاتی دریافت کرده‌اند که ایران در تلاش است آن‌ها را هدف قرار دهد. در نتیجه، به برخی از آن‌ها دستور داده شد که به‌دلیل نگرانی از وقوع یک حملهٔ برنامه‌ریزی‌شده، استفاده از سرویس‌های هم‌سفری و خودروهای کرایه‌ای را متوقف کنند. هم‌زمان، خودِ ترامپ نیز از سوی اسرائیل در جریان اطلاعاتی قرار گرفت که نشان می‌داد تهران در حال بررسی طرحی تازه برای هدف قرار دادن اوست.»
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19591" target="_blank">📅 22:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">المیادین: واشنگتن از رهبران کردستان عراق خواسته در جنگ علیه ایران وارد شوند و ایران هم به اربیل درباره پیامدهای هرگونه همراهی با این جنگ هشدار داده است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19590" target="_blank">📅 22:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدا وسیما :
عصر امروز ارتش آمریکا با پرتاب دو‌ موشک به یک تانکر ال پی جی که از سمت دریای عمان قصد ورود به منطقه را داشت این تانکر را به تصور اینکه قصد انتقال گاز ایران را داشته مورد اصابت قرار داد و با کشتن دو نفر از خدمه و ایراد خسارت به موتور خانه آن کشتی، آن را متوقف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19589" target="_blank">📅 22:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19588">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیویورک تایمز: ترامپ امروز با مشاوران ارشد خود درباره تشدید حملات علیه ایران دیدار کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19588" target="_blank">📅 21:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19587">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پست جدید کلیک کنید
https://www.instagram.com/reel/DbL3e_Ioe9s/?igsh=ODB2Y3BzZGJoMHUz
کپشن : ⁨ اتاق جنگ با یاشار : برای دوستان سردرگم شاید یکی از بهترین مثالها برای ماجرایی که برای ملت ما پیش اومده، فیلم گنج قارون باشه. مردمی که با ثروتی بی‌انتها خودکشی کردن. و حالا، آمریکا و اسرائیل، او را از رودخانه نجات داده و دوباره به خانه آوردند. خواستم یکبار دیگر این فیلم رو برید دوباره نگاه کنید هم صحنه های بسیار زیبای آن زمان هم برخورد و فرهنگ مردوم با هم… که در آن زمان ما کجا بودیم. سکانس هتل هیلتون هم فراموش نشدنی است. حالا پاشو و شادی کن و مبارزه کن. گنج قارون در انتظار شماست. خواستم یکبار دیگر یادآوری کنم کی هستی و کجایی تا بلندشین تاریخ سازی کنید و از این حال دربیاین!⁩</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19587" target="_blank">📅 21:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19586">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14728b7ed2.mp4?token=L1oGlPr7yhUgFv_SJvqNFzXLh6xqpUdTO85KVsljWe1mF5duLcYDHaNV1kvItnC8DHAyv6kWFCIE23HkyUomdeAcKbKNkooB28QoIamrTJd2K4iJehx0YtTEYTNevtdxWAc5bWUfj8-3hwtZSxihF75F6N_SKJYpuuMP6Rlsa0l1LxdelHmls7VLSGGdJt5j3PwnmN-8uCRyDZGoXddJyIIOuUC3x9lfAH8KJQbYlDE6N3JaJoYvoUbFKGnNOZI0RilQr62YVbY6XS_MSvwPC42TopRw9FIZifhyGKD5onneGBA-TK80Hyg923jtGLYGDGAiSzpjIlUvOP0HpAYjCIIMhwneDNx8zuawAdy-wEkHMXVOeNsn0fdtv6FBLq1nxgkiZt6r073-uFSPMgFStC2pKhnBYYq_het2A6a_QavZKbHkNd7Im_YbRQLAVMC4tmrLgxXqNQeZEEB5jascqP4A_SYkVMJ3K1mRX4_xahwWYyUMXz2CJOv43QmRP44LI1R2dCXVmVu6hEKBtsvWqjlJlfn2iTVU7QMCyE3zdjGnkIKoZmkswWWx3cyKaPZ1qsC4Qx2SVkGu6fGLrvjU0Y33t4otgiGkbuZuZ7LoIeU0ujISH1_W1uMpM4scdoD7C7G0YAmmPcNil_CQ0LvrCUbOnhgfT_Hx4KnKDU17Tmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14728b7ed2.mp4?token=L1oGlPr7yhUgFv_SJvqNFzXLh6xqpUdTO85KVsljWe1mF5duLcYDHaNV1kvItnC8DHAyv6kWFCIE23HkyUomdeAcKbKNkooB28QoIamrTJd2K4iJehx0YtTEYTNevtdxWAc5bWUfj8-3hwtZSxihF75F6N_SKJYpuuMP6Rlsa0l1LxdelHmls7VLSGGdJt5j3PwnmN-8uCRyDZGoXddJyIIOuUC3x9lfAH8KJQbYlDE6N3JaJoYvoUbFKGnNOZI0RilQr62YVbY6XS_MSvwPC42TopRw9FIZifhyGKD5onneGBA-TK80Hyg923jtGLYGDGAiSzpjIlUvOP0HpAYjCIIMhwneDNx8zuawAdy-wEkHMXVOeNsn0fdtv6FBLq1nxgkiZt6r073-uFSPMgFStC2pKhnBYYq_het2A6a_QavZKbHkNd7Im_YbRQLAVMC4tmrLgxXqNQeZEEB5jascqP4A_SYkVMJ3K1mRX4_xahwWYyUMXz2CJOv43QmRP44LI1R2dCXVmVu6hEKBtsvWqjlJlfn2iTVU7QMCyE3zdjGnkIKoZmkswWWx3cyKaPZ1qsC4Qx2SVkGu6fGLrvjU0Y33t4otgiGkbuZuZ7LoIeU0ujISH1_W1uMpM4scdoD7C7G0YAmmPcNil_CQ0LvrCUbOnhgfT_Hx4KnKDU17Tmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فشن شو کالکشن تابستانی بی بی
کت واک نمونه کارهای ۲۰۲۶/۲۰۲۷
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19586" target="_blank">📅 21:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GILlvDCLOWTp2rPt58f2b99_eCyVECTU4RT2lQRy_U8cFpiLpWWgEq5mDS4QNdTO9X2mg8GUPgRGFQVnGnVHHCgnEAOB4YiuYR46wUT6A0KtNhmpg3CStKmQ4At8TYHGgbhifSC6vd87c2TjZ9zvFM0o0NXE37iFBg9mJDDmMf7pnPkhTlEA4k7r2rv-1Z_l4lD39DvGHz7vX-rYH1-n7zwLfsf-pDC9v1U4tPxpWN0wWmu5_nC6A9ZhCbuf39waVmm-1COdLVRG2hlo3EOoelbVganW2c-Vh5uPqm-nVlLvwtz2vXdcMDhOWiobFLvSQAAkyxOz0TSVyvtOyb6IMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکبر عبدی درگذشت
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19585" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19584">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فرودگاه بن گوریون اعلام کرد که فرودگاه به طور معمول فعالیت می‌کند و توقف موقت پروازها به دلیل انجام تعمیرات و نگهداری معمول باند فرودگاه است، که از قبل برنامه‌ریزی شده بود. انتظار می‌رود پروازها ساعت ۱۱ شب از سر گرفته شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/19584" target="_blank">📅 20:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19583">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دونالد ترامپ اعلام کرد اتحادیه اروپا با جریمه‌های سنگین علیه شرکت‌های بزرگ فناوری آمریکا مانند اپل، متا، آمازون و گوگل، به‌طور مستقیم شرکت‌های آمریکایی را هدف قرار داده و این اقدامات را «غیرقانونی» و «تبعیض‌آمیز» خواند. او گفت جریمه‌های گوگل اکنون از ۱۸ میلیارد دلار فراتر رفته و آمریکا دیگر اجازه نخواهد داد اروپا از شرکت‌ها و مالیات‌دهندگان آمریکایی سوءاستفاده کند. ترامپ از آغاز فوری تحقیقات تجاری بر اساس «بخش ۳۰۱» علیه اتحادیه اروپا خبر داد و هشدار داد که این اقدام می‌تواند به اعمال تعرفه‌های سنگین و دیگر اقدامات تلافی‌جویانه منجر شود و اروپا بهای سنگینی برای این رفتار خواهد پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19583" target="_blank">📅 20:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19582">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_C-ng1QzTQvf82zlKpRIwH4Mhj6Wc6sNkJKaLEhLpQvKPLFgMplPwXvrILOHFYtpUZ_9GLRITyKODQl54P7IkTjQLwa-SwgcfeJi6lSYaEOAhSRk7ksihZPeLwQeAtvlEX2ViyUyIWdTkVaaug5-iyG7yCD7enWgg5X-AviwxYrqgt_U4mwHMDsur7LPSoMnHgOitlETtUPlJnozLeutPWGYjP-7eWZWHHEqTLWzYpyEGPxIfYZEOtkjNJ0kMq7DXxcgcWsg9sm9KBbojicZLXworYYsxXdZlQXBYBI5QSViTh9NXAFbAU-5hQ1fozbuWU73WP_E2ha_IMwNynzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : تشکر از نخست وزیر بلغارستان برای در اختیار گذاشتن پایگاه هوایی این کشور با وجود تهدیدات ایران
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19582" target="_blank">📅 20:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19581">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال‌استریت ژورنال: بحرین و کویت به‌طور محرمانه جنگنده‌های خود را برای حمله به اهدافی در داخل ایران اعزام کردند؛ این نخستین اقدام تلافی‌جویانه مستقیم آن‌ها علیه تهران بود. در این حملات، انبارهای پهپاد و موشک هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19581" target="_blank">📅 20:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19580">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مطابق گزارش‌های خبرگزاری آکسیوس، به گفته منابع، واشنگتن از متحدان خود خواسته است تا کشتی‌های پاکسازی مین و پهپادها را برای کمک به تأمین امنیت مسیرهای حمل و نقل ارسال کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19580" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19579">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آکسیوس:ایالات متحده و بریتانیا در حال برنامه‌ریزی برای برگزاری یک کنفرانس بین‌المللی درباره تنگه هرمز هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19579" target="_blank">📅 19:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19578">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W87kTUXV4dPzU-ab2b8Gucm8fz9HAAbOsCwkpjIGjBDWjVfhGvVAw4OtXct9y0mac30MkOgULZ7VmCEJ-s2MZDy8P5CcjtuHfW4QthxXteYtv_9GX6FYagzTyeMbi4aLchh1C4YFG45KgKwonpbcddOE6r_a_3qmBn5gqRbZEgp63fzK7j8JNbWjhRdmsmgah3q4-V7V8LMPJtHFw13xY7BE69rAk-qn_m7ldUFjnJhGf8ucRgowtkZbDZPTEuf4RIiJ4HMi41Bhu7_ED4UwVQTIzhzf5pbMEPCbyyQOExwYe8gkNeWOhnXNI6BGf5tmNVwGH29VMyKlr8PS7G3fMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در مورد فروش سلاح های روسیه و چین به ایران:
رئیس جمهور شی، در دیدار اخیرمان در پکن، چین، به من گفتند که تحت هیچ شرایطی، سلاح به جمهوری اسلامی ایران نخواهند داد یا نفروشند – و این اظهار نظر شامل شرکت‌های چینی نیز می‌شد. با توجه به روابطمان، من به حرف او اعتماد دارم و علاوه بر این، من نیز خدمات بسیار بزرگی به او ارائه می‌دهم.
به همین ترتیب، رئیس جمهور پوتین، با وجود جنگ وحشتناکی که در اوکراین در جریان است (رابطه همچنان مانند رابطه با رئیس جمهور زلنسکی است)، به من گفتند که سلاح به ایران نخواهند فروخت. او درک می‌کند که من سلاح به اوکراین نمی‌فروشم، بلکه به کشورهای ناتو می‌فروشم. آنها قیمت کامل را پرداخت می‌کنند و من نمی‌دانم این سلاح‌ها چگونه توزیع می‌شوند.
بنابراین، به نظر من، دو کشور بزرگ که مردم اغلب در مورد آنها در رابطه با ایران صحبت می‌کنند، در این موضوع دخیل نیستند. اگر دخیل بودند، این امر برای آنها بسیار بد بود – قطعاً به نفع آنها نبود.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19578" target="_blank">📅 18:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19577">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نتانیاهو دوشنبه آینده عازم واشنگتن می‌شود
دفتر نتانیاهو اعلام کرد نخست‌وزیر این دوشنبه اینده به دعوت ترامپ عازم واشنگتن خواهد شد.نتانیاهو روز سه شنبه در کاخ سفید با ترامپ دیدار می‌کند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19577" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19576">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52ae83427d.mp4?token=lm7Vq09pJ9-LgrnwIkAx0YYlqM1PeBcCB588i2-d1kR8mXh3pp4jG28igLf-cgliq1BHDysF2FlIr7pISiBFdL_EXVBRaLl85Nxw79Od1BJ8O8E_pw9DDt_0gb2n7BveS8wtm5zNxpMyqhu0ItpPV7LTl1NaTm4EOlOK6Wena7IYNX9NEzehZTWGLMlNvYBKl_pQZsM81-vALBsddmoXg1ql8vLslblwzlXzVEGIZB09BXGVg49cw8rOp_KB_v8CzgMy7Y25Wk1hY-8yWP2T1BxR4i9Bvr708EgrMTNfYSTFpPnQaH5RXJhGjh4ILtBXohUybtRprH9D_MYBObH9kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52ae83427d.mp4?token=lm7Vq09pJ9-LgrnwIkAx0YYlqM1PeBcCB588i2-d1kR8mXh3pp4jG28igLf-cgliq1BHDysF2FlIr7pISiBFdL_EXVBRaLl85Nxw79Od1BJ8O8E_pw9DDt_0gb2n7BveS8wtm5zNxpMyqhu0ItpPV7LTl1NaTm4EOlOK6Wena7IYNX9NEzehZTWGLMlNvYBKl_pQZsM81-vALBsddmoXg1ql8vLslblwzlXzVEGIZB09BXGVg49cw8rOp_KB_v8CzgMy7Y25Wk1hY-8yWP2T1BxR4i9Bvr708EgrMTNfYSTFpPnQaH5RXJhGjh4ILtBXohUybtRprH9D_MYBObH9kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از خواهرهای عزیزمان، دیدبان اتاق جنگ، همین الان فیلم بسیار مهمی را برای من فرستاد؛ یک اسکادران اف۳۵ (۱۲ عدد) همین الان از مهم ‌ترین پایگاه نظامی امریکا در انگلستان  RAF Lakenheath  به سمت خاورمیانه حرکت کردند، او الان این فیلم را در کمبریج حدود 25 تا 30 مایلی این پایگاه مهم نظامی ضبط و برایم ارسال کرده
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19576" target="_blank">📅 18:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19574">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فعال شدن آلارم حمله موشکی/پهپادی در کویت
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19574" target="_blank">📅 17:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19573">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی: ما آتش‌بس موقت را نخواهیم پذیرفت و تا زمانی که خواسته‌های ما در مورد تنگه هرمز محقق نشود، این موضوع مطرح نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19573" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19572">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سناتور سابق نیروی دریایی، تیم شیهی، او دستبند  دوستش که توسط بمب جمهوری اسلامی کشته شده بود، بالا گرفت و سخنرانی تندی در صحن سنا در مورد ایران انجام داد و تحسین همگان را برانگیخت. بازتاب این سخنرانی بی نظیر بود.
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19572" target="_blank">📅 17:13 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19571">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند ستاد فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای این فرماندهی، سیزدهمین شب پیاپی حملات به ایران را در ساعت ۹:۰۰ شب چهارشنبه ۲۳ ژوئیه به وقت شرق آمریکا (ET)، (ساعت ۰۴:۳۰ بامداد پنجشنبه…</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/19571" target="_blank">📅 16:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19570">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هاآرتص: نتانیاهو در تلاش است اسرائیل را وارد حمله به ایران کند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19570" target="_blank">📅 16:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19569">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0647ce42a6.mp4?token=YTD3qRlAN_pgKtBvYSMpnfZe-1WFKQAC8ajgdyzukAOuoPMZbhYV1sDhT54INWea6Zh4JQwlBlxARbdw14Iv87dS5D5KSMHYKtPqPcl7YpiFRSyw8MFbGH5zbNNct0p1Cj74WvB8hELQ7CEd9tnyfaq-KbBt0tz9cQbHRzuvjv0IBMqyVzlQDgrk9raJ5YIXBOco3n4SJIcyNzbsPrG1HxZRfTczMXyToHIJqfsxG2oskGESx2HzzlFrCWBM4rw2XDmyLV9mgTBYkeieCtSQtW0m6aY__7DKCJ6NgVN1ugVad_RnbdSj2Zn9JhzCjRzbCqZiT2rEbIFvnnQSyed1hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0647ce42a6.mp4?token=YTD3qRlAN_pgKtBvYSMpnfZe-1WFKQAC8ajgdyzukAOuoPMZbhYV1sDhT54INWea6Zh4JQwlBlxARbdw14Iv87dS5D5KSMHYKtPqPcl7YpiFRSyw8MFbGH5zbNNct0p1Cj74WvB8hELQ7CEd9tnyfaq-KbBt0tz9cQbHRzuvjv0IBMqyVzlQDgrk9raJ5YIXBOco3n4SJIcyNzbsPrG1HxZRfTczMXyToHIJqfsxG2oskGESx2HzzlFrCWBM4rw2XDmyLV9mgTBYkeieCtSQtW0m6aY__7DKCJ6NgVN1ugVad_RnbdSj2Zn9JhzCjRzbCqZiT2rEbIFvnnQSyed1hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار جدید جاسک ۱۵:۴۳
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19569" target="_blank">📅 16:17 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19568">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش ۳ انفجار‌ در‌ قشم
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/19568" target="_blank">📅 15:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19567">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گزارش انفجار ‌در جاسک دوباره الان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19567" target="_blank">📅 15:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128e32e551.mp4?token=HIZzm4apssGa51mJ-ihPTIbpdLSSt85gHgvN33371mlQUPq8lDZhyv1iXXFR-BNyXFcL4OT8EYjFiKG0puiKA_ro1UBz1GY204uv2ratpk4J_CyQkB5KOQh4rEB3HGwbZndUJAQipXCYlxjn3hlEoypebqk2dAtvVaB1empHeBsC1_HZMRjLQqa8zTI9uVqB48jY0-r_3_3lhlMWcZOTpWtUToKwXBDRQQdLN8RWO4n-9HYs_GUitnlAJwYm60t4Zj-RG9eXN-jm1NdhgnkImIGZ8SxRICWrftF2JNuYgMqsOx3R5kyjwSlY2PMLki4qjZ0t3NwjzI6vHazSt05MWHbiCexP13VCmrml5prJs1mrr2abvv33HyTrCb6htp_YnflFU9qVK7sEr6_yqHApsaMyQh0YP6wiNT-49dNbsXK3O9oLIBw-2l54asQuz85taOMG9d6FPB3NIp_6pv34cITogI7rwj4fhX2WvOGI4nVjkwAF_tN_9hBVsvnr5yePfRJ_73l44y7pjYCYih1f9zEr80U9Qn7xjdzzT-1E0M8aYXhc8gxZ488aJFHJ4Fc7_AcliB_3-QkxkGQTcnyTl3KgIilRUtBKY_d905SuY14Wdlf-58FSKrsV3oROMeS_f60uskfRjXH6rTIYDjaJpj-P7YhqWRnfFxIUj6Y0tsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128e32e551.mp4?token=HIZzm4apssGa51mJ-ihPTIbpdLSSt85gHgvN33371mlQUPq8lDZhyv1iXXFR-BNyXFcL4OT8EYjFiKG0puiKA_ro1UBz1GY204uv2ratpk4J_CyQkB5KOQh4rEB3HGwbZndUJAQipXCYlxjn3hlEoypebqk2dAtvVaB1empHeBsC1_HZMRjLQqa8zTI9uVqB48jY0-r_3_3lhlMWcZOTpWtUToKwXBDRQQdLN8RWO4n-9HYs_GUitnlAJwYm60t4Zj-RG9eXN-jm1NdhgnkImIGZ8SxRICWrftF2JNuYgMqsOx3R5kyjwSlY2PMLki4qjZ0t3NwjzI6vHazSt05MWHbiCexP13VCmrml5prJs1mrr2abvv33HyTrCb6htp_YnflFU9qVK7sEr6_yqHApsaMyQh0YP6wiNT-49dNbsXK3O9oLIBw-2l54asQuz85taOMG9d6FPB3NIp_6pv34cITogI7rwj4fhX2WvOGI4nVjkwAF_tN_9hBVsvnr5yePfRJ_73l44y7pjYCYih1f9zEr80U9Qn7xjdzzT-1E0M8aYXhc8gxZ488aJFHJ4Fc7_AcliB_3-QkxkGQTcnyTl3KgIilRUtBKY_d905SuY14Wdlf-58FSKrsV3oROMeS_f60uskfRjXH6rTIYDjaJpj-P7YhqWRnfFxIUj6Y0tsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکله جاسک ساعت ۲:۳۰ دو انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19566" target="_blank">📅 15:32 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">آمریکا: ترکیه شرایط دریافت جنگنده‌های F35 را ندارد
وزارت خارجه آمریکا در نامه‌ای به کنگره اعلام کرد ترکیه به دلیل ادامه نگهداری سامانه S400 روسی و برآورده نکردن الزامات قانونی، واجد شرایط دریافت جنگنده‌های F35 یا بازگشت به این برنامه نیست. واشینگتن در عین توصیف ترکیه به عنوان یکی از متحدان مهم ناتو، تأکید کرد در حوزه‌های دارای منافع مشترک با آنکارا همکاری خواهد کرد، اما در برابر اقداماتی که با منافع آمریکا در تضاد باشد واکنش نشان می‌دهد. این نامه همچنین ضمن قدردانی از نقش ترکیه در کمک به آتش‌بس غزه، نسبت به ادامه فعالیت شبکه‌های مالی گروه تروریستی حماس از خاک ترکیه ابراز نگرانی کرد و اعلام کرد آمریکا به هدف قرار دادن تأمین کنندگان مالی این گروه ادامه خواهد داد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19565" target="_blank">📅 15:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش ارسالی : سلام.ساعت 14:30 دو انفجار در اسکله جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19564" target="_blank">📅 14:56 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXwUwyBf0FGoWdxuyI5Km3ln3rD_cTU9tRMcvXZDEftwYDNjO4gn0wFytdKzTeOpv6-TjJbfwzgeBu8QuFyGoyH-aOj9c7We-UXHd-9s78sDl3T_Zvmcwt18kR94AXkZpBQfhrGjRo8hYUWV2pLI2W4BXBAXhhRv22S6hdCtryx7Viu5HuXLVxm7Q8Ks70SUjb6TQuA-EHk0arGdxYcepT0uHPb8xSYP0SZBwBZRV1u-vRyWeY_u_rKMk2zSzERKMHmrDEyrsG_mOPO1zhuMwZgs3P2_u5qgr6WMg1Ilj8qKOLzAx6dvg6ljAnfiCRD2QezibTy7U2xSS61veZ02eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی نقاط مورد هدف قرار گرفته در سیزده روز اخیر تا این لحظه.
@WarRoom
💥
💥
💥</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19563" target="_blank">📅 14:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه در‌ بیانیه ۵۰ : ما یک پایگاه در کویت و برج کنترل نیروی دریایی پنجم در بحرین را مورد حمله قرار دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19562" target="_blank">📅 14:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAWJgoJty0cCwf-23uCVCSxuHW-rAJwxXGn8k-4pG-RsRPTfl0L84HfXXmU-097bdevmzPNsvmPDCQfsgkLIMerQJKTdnqA6pyHLjKRyJ23oJ00bklbRzTppAvjNqFawLypDUIaUCKHV0Xhzn8MHaHwED8Xcfzt7sMCzrB2sTL-Koxy0UIs1Iz90RTo0-pjDwgmCFT8VQJfFL8sjXWfg_iR0dgUhjQLK6Il-3FkGiByolRmXjSZUnJJNWyQSlS6URuC6vIbPEKUp111xNa2ie1Zq5oFedvnl_0v4IofoCKquSjLnLSYPGogW7YRWwOGGN0u18ZygEZME5lSQ5cATXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو هواپیمای مخوف جنگ الکترونیک EA-37B کامپاس کال دو، مقر انگلستان را ترک کرده و به سمت خاورمیانه در حرکت هستند. اگر بوداپست هستید، آسمان را نگاه کنید و عکس بفرستید.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/19561" target="_blank">📅 13:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وال استریت ژورنال:  ترامپ در مورد ایران بیشتر به گزینه نظامی رو آورده و فعلا پلنی برای مذاکره با سران ایران نداره.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19560" target="_blank">📅 13:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197bdc163.mp4?token=AMQro8bIskbTecBVeOu0MtkVI9VIMPoSG9l9jImi1S4axb1FjkP8sQ7eBFCHBLul0f22kcqIedGqlJFCJsd2h4owB6kdbzXj-TM30f7qtAznITsGC6jxV_InVe9-nCmtSJkSW6pBE8A6u8H4JjoTG6c_MvuKmeRzyvMx9QfhZy_cADnL2TggnU4RovUxrBd5OawFUCnq2WWv3UQikB6uwNh2mn5VxywYMEX6veIP-sXgUdcE6Hph51YxnFODsyQfe0qsdrTOGh5Ukf6DpO-hgc7sLv3PSKrvjr-BRVWyQehZz80DV-0gKinSeiXACh2PxmmVIWT5Y7D2UZynAiOZsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197bdc163.mp4?token=AMQro8bIskbTecBVeOu0MtkVI9VIMPoSG9l9jImi1S4axb1FjkP8sQ7eBFCHBLul0f22kcqIedGqlJFCJsd2h4owB6kdbzXj-TM30f7qtAznITsGC6jxV_InVe9-nCmtSJkSW6pBE8A6u8H4JjoTG6c_MvuKmeRzyvMx9QfhZy_cADnL2TggnU4RovUxrBd5OawFUCnq2WWv3UQikB6uwNh2mn5VxywYMEX6veIP-sXgUdcE6Hph51YxnFODsyQfe0qsdrTOGh5Ukf6DpO-hgc7sLv3PSKrvjr-BRVWyQehZz80DV-0gKinSeiXACh2PxmmVIWT5Y7D2UZynAiOZsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از خارک و نابودی 4 بالگرد آگوستا وستلند 109 متعلق به شرکت هلیکوپتری خلیج فارس که آنجا پروازهای امدادی و گشتی انجام میدادند.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19559" target="_blank">📅 13:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LotJd_67FzfATDVhalkEyCJuPUxP8bgfd6x54ckpW_P0U1XRSKOr_7xJG1TN8IKUgqLJyDn3vw9jF9rGWRLx2qRzZXxKho-piX5qi4ZrMeyMFFHyyfLLralKCCS2F-XvsK8sM5JpYCnceJ0Eca7Ivbu0PihHZFZ5nYWSb0oxfuGAaUluiRE6KKowkUGN6qVGJnAjqxEhdXdZQxFDB2r8eB9ozVCCYcT0Ux1Qwo7N49ou4F9LJfr9ZZ6FE2T6A1Wcivy5aGMXuJvvOSNfPrNCGbpJfz5F28iUxfq6-GLLFi82eE4wqnnXnXK-FeygktAMMQNxlRRoWVaUCs5DQBdfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیروزآباد فارس الان
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19558" target="_blank">📅 12:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19557">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏جیک تورکس، خبرنگار ارشد کاخ سفید و نیوزمکس، نوشت که به اطلاعاتی دسترسی دارد که بسیاری از افراد از آن بی‌خبرند و با اطمینان کامل می‌گوید آمریکا برای شکست رژیم جمهوری اسلامی برنامه دارد. او افزود کارشناسان از آنچه رخ خواهد داد شگفت‌زده می‌شوند و سپس وانمود می‌کنند از ابتدا همه‌چیز را می‌دانستند.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19557" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19556">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1807f6b87b.mp4?token=Rv8WgDq3ioAEgzID9GIzXg6FaVJ-xQ4IkgVzBmjZvVFCRnGFw0ZHxnWh8FRAtGjGUNe5JP1C6wy6QqDjjgi24Y-VcblK21uJN-KJZu3ymmR4lolvJqO-lT8777F-WEdG2qi8yrM-uhNSgsgEyvoOvNqjIGy0gcviPRIKtpo2UGYP15MWpgLL0OIDFlddCqnn56QREski-6ectFX_tzXtz9Hhwj6GsF_7Evv8-2kzej4BJw8yWr76mF6OApWWN_xSc1vWVayn9C6VxiTXd7gdLKg_Iu6gehPy8ZgNXa4FSVoVt1LJCjoiEsRT7smYXmPtP5Mcl5eOksIFd3T-W5pakZp4InEIIrtYXgicPNr8wmG5a1oyaW_Y-UO_LSMc8T1JMduoPE-wkWwR3jGCn2hJBArRjiJEgQzzEjM26LI7OvkpoPdNPt9ST_qr1F1AiAKDvBn2Ny-VUJp35JeivTYHg4J9sNSgBSkFm5T8LS8PSbIeWCdjBgSFVS_AAGNZzEN1llJn9HEtOdbGqKei2AeGvwunO4j-X2G4Up9yDCHEttWrpRXTGeaeTJfL-jA-cnQ0LL8ydxMCBg8LW3mkDyI9M0p1jxzBqm0LTibBxt-1GBmQJJXbLrPck-jkgiwk7NstCBSaUdDN424w9Ys8XZH8EhAO1-uq4UMDHfI1hmrCzQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1807f6b87b.mp4?token=Rv8WgDq3ioAEgzID9GIzXg6FaVJ-xQ4IkgVzBmjZvVFCRnGFw0ZHxnWh8FRAtGjGUNe5JP1C6wy6QqDjjgi24Y-VcblK21uJN-KJZu3ymmR4lolvJqO-lT8777F-WEdG2qi8yrM-uhNSgsgEyvoOvNqjIGy0gcviPRIKtpo2UGYP15MWpgLL0OIDFlddCqnn56QREski-6ectFX_tzXtz9Hhwj6GsF_7Evv8-2kzej4BJw8yWr76mF6OApWWN_xSc1vWVayn9C6VxiTXd7gdLKg_Iu6gehPy8ZgNXa4FSVoVt1LJCjoiEsRT7smYXmPtP5Mcl5eOksIFd3T-W5pakZp4InEIIrtYXgicPNr8wmG5a1oyaW_Y-UO_LSMc8T1JMduoPE-wkWwR3jGCn2hJBArRjiJEgQzzEjM26LI7OvkpoPdNPt9ST_qr1F1AiAKDvBn2Ny-VUJp35JeivTYHg4J9sNSgBSkFm5T8LS8PSbIeWCdjBgSFVS_AAGNZzEN1llJn9HEtOdbGqKei2AeGvwunO4j-X2G4Up9yDCHEttWrpRXTGeaeTJfL-jA-cnQ0LL8ydxMCBg8LW3mkDyI9M0p1jxzBqm0LTibBxt-1GBmQJJXbLrPck-jkgiwk7NstCBSaUdDN424w9Ys8XZH8EhAO1-uq4UMDHfI1hmrCzQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهر خودرو خلیج فارس در اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19556" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19554">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بن غفیر وزیر امنیت ملی اسرائیل: به ازای هر یهودی که دشمن می‌کشد، دشمن باید متحمل از دست دادن زمین‌ها و خانه‌ها شود. من خواستار صدور دستوراتی به ارتش برای تخریب خانه‌های تروریست‌ها و حامیان آن‌ها خواهم بود. @WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19554" target="_blank">📅 11:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19553">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بن غفیر وزیر امنیت ملی اسرائیل: به ازای هر یهودی که دشمن می‌کشد، دشمن باید متحمل از دست دادن زمین‌ها و خانه‌ها شود. من خواستار صدور دستوراتی به ارتش برای تخریب خانه‌های تروریست‌ها و حامیان آن‌ها خواهم بود.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19553" target="_blank">📅 11:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19552">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه های داخلی : ارتش آمریکا امروز با موشک، مقر نیروی دریایی سپاه پاسداران انقلاب اسلامی را در منطقه زیباکنار، در سواحل دریای خزر در شمال کشور، مورد حمله قرار داد. خساراتی در این منطقه وارد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19552" target="_blank">📅 11:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19551">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سپاه تروریستی که جدیدأ با اسم ارتش جمهوری اسلامی فعالیت میکند اعلام کرد که با استفاده از پهپادهای "آرش"، انبارهای تجهیزات ارتش آمریکا را در پایگاه العدری، و همچنین پادگان‌های نیروها در دوحه و تعدادی از مواضع را در پایگاه عریفجان در کویت هم اکنون مورد هدف قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19551" target="_blank">📅 11:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اتاق جنگ با یاشار : ده‌ها هواپیمای باری نیروی هوایی ایالات متحده (سی-۱۷ و دیگر هواپیماهای سنگین) امروز از پایگاه‌های اروپایی به خاورمیانه پرواز می‌کنند.  این یک "پل هوایی" تمام عیار است که بعد از جنگ۴۰روزه دوباره فعال شده. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19550" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0_K-84rISMrgw3ImjHe3WZ5wB_9bLSemuJylgwt7udpL1qp_sv3bmTElzohBao6IR06u2X3C5jAdtZmArDf76mm5lBdltQD6tbACOufMd2TyyaeA1YaRJJsVUD1HjoZUYo9gqudY49QMtMz8hUBA5G-RDu2ftVklBXf3KQ1d-luZv-4uLzGzmsWnwZfOZDW8cbsam-FHKTpn4RDBvNrOmhx27AV0eXbBAFvCCahPVjGx85AaimU1cf4gZS7IjQ5Uf3EIsAFWXkNrYOIUqknwwYCt6axvv3xxAqm_LHU75pbNpb4Hpml_Pk1R3g7s6dAy_mEEuiCYnk70TsFJm6w5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شب گذشته، دو فروند بمب‌افکن
B-1B Lancer
از پایگاه
RAF Fairford
بریتانیا تقریباً همان مسیر پروازی مأموریت
«HEINZ»
را که چند روز پیش انجام شده بود، تکرار کردند.
در این مأموریت، یکی از بمب‌افکن‌ها تا منطقه تحت
(CENTCOM)
پیش رفت، اما هواپیمای دوم حدود
۶ ساعت
پرواز کرد و سپس به پایگاه خود بازگشت.
بمب‌افکن اصلی به بمب‌های
JDAM
(بمب هدایت‌شونده ماهواره‌ای که بمب‌های معمولی را به سلاح‌های دقیق تبدیل می‌کند)
مجهز بوده است.
ترکیب مأموریت بمب‌افکن (Mission LXIV):
B-1B “PURDY30”
با شماره 86-0107 و لقب
Dragon Slayer
(اژدهاکش)
B-1B “PURDY31”
با شماره 86-0138 و لقب
Seek and Destroy
(جستجو و نابودی)
دو فروند هواپیمای سوخت‌رسان
KC-135R
با شناسه‌های
BOBBY14
و
BOBBY16
که از
LROP
(محل استقرار عملیاتی بلندبرد)
مأموریت را پشتیبانی کردند.</div>
<div class="tg-footer">👁️ 172K · <a href="https://t.me/withyashar/19549" target="_blank">📅 10:49 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e7b5aa30.mp4?token=HEklRVqOIUIS8jkgQb0FII_K-jfKXcMQvrVPfEx5P5mKEA3w9QcQkSiU0SJja4uXKMGJB6jSkiqkQ9IjSt68GXAvRPDIk6TReUzfJFt4iRSf98ksjZnwL1NG3XjKODCLiuJoazR6uhJYnkV_TuuvuO-d4lhfdsOqmVwRM6en7f_ohiKCRwz8GGuNrwemP4t45E14JIrHdpK_SLcwpmO3e57gQo65Wjljpept7UStz5U6jFtQVSzaLuxQ5QIFMd5ARR_pq_lWV4vgHWI_JFGnRGoXD64ljZ1LlDkUVelLhbd1suKViq9A_EcnWeBGphz2S6uYuUb2ammZNJfRmo4A3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e7b5aa30.mp4?token=HEklRVqOIUIS8jkgQb0FII_K-jfKXcMQvrVPfEx5P5mKEA3w9QcQkSiU0SJja4uXKMGJB6jSkiqkQ9IjSt68GXAvRPDIk6TReUzfJFt4iRSf98ksjZnwL1NG3XjKODCLiuJoazR6uhJYnkV_TuuvuO-d4lhfdsOqmVwRM6en7f_ohiKCRwz8GGuNrwemP4t45E14JIrHdpK_SLcwpmO3e57gQo65Wjljpept7UStz5U6jFtQVSzaLuxQ5QIFMd5ARR_pq_lWV4vgHWI_JFGnRGoXD64ljZ1LlDkUVelLhbd1suKViq9A_EcnWeBGphz2S6uYuUb2ammZNJfRmo4A3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا سیزدهمین شب حملات به اهداف نظامی ایران را به پایان رساند
ستاد فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای این فرماندهی،
سیزدهمین شب پیاپی حملات به ایران
را
در ساعت ۹:۰۰ شب چهارشنبه ۲۳ ژوئیه به وقت شرق آمریکا (ET)
،
(ساعت ۰۴:۳۰ بامداد پنجشنبه ۲۴ ژوئیه به وقت ایران / ۲ مرداد ۱۴۰۵)
با موفقیت به پایان رساندند.
به گفته سنتکام، در این عملیات
مراکز فرماندهی نظامی، انبارهای نگهداری پهپاد، شبکه‌های ارتباطی، سایت‌های پایش و دیده‌بانی ساحلی و توانمندی‌های دریایی ایران
هدف قرار گرفتند تا تهدیدی که ایران علیه دریانوردان غیرنظامی و کشتی‌های تجاری عبوری از
تنگه هرمز
ایجاد می‌کند، بیش از پیش کاهش یابد
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/19548" target="_blank">📅 04:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فعال‌سازی پدافند شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/19547" target="_blank">📅 03:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش انفجار جاسک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/withyashar/19546" target="_blank">📅 03:48 · 02 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
