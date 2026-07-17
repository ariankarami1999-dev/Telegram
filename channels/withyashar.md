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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 401K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-18568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بر اساس گزارش خبرگزاری رویترز که از منابع مطلع به دست آمده، پاکستان در حال مذاکره برای یک توافق دفاعی گسترده از کویت است، در ازای همکاری در زمینه انرژی.
@WarRoom</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/withyashar/18568" target="_blank">📅 17:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قدیمی‌ها یادشونه من اینارو هر روز که کم میشدن قبل جنگ اعلام میکرم
@WarRoom</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/withyashar/18567" target="_blank">📅 17:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">استوری روز قبل حمله !!!
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/withyashar/18566" target="_blank">📅 17:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a267a27341.mp4?token=Hr-9yNFWeUtsRvjTmRo8ZOlZ0pfO9BsKmfWzIh-K5tvpPTFWPAO9ySNz7bwsAOsfwUaHAiEzOYiR8VkXAOxI2bR65FybgcuBWPYsCEYU2e2-Z1Yqvenc7_dvW2UW1-t1hKMk3wGdicfiJx6OtsX7y0ZYgQcl1ln2fdGFWiA6VkZxi310seH0jtP8CEB-aqBTFXz3cIFNl1cZxKSMvrKU46SQB1YKR4tZWab-tuxdPLJ0seoDRZ_TcrkwpBbVhbSz8ZgOYTHhaRmC2hmaJxmP0jVYNHhcChaArCnKvim-sTC5pGbMSbg9zLqwac3Ejh0Vusgz26HaznE4BQdemQ1aCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق تصاویر ماهواره‌ای بیش از 20 فروند هواپیمای سوخت رسان آمریکایی حاضر در قطر این کشور را ترک کردند.
چنین اقدام مشابهی در روز های پیش از جنگ نیز مشاهده شده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/18564" target="_blank">📅 17:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18563">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/withyashar/18563" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18562">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">هم اکنون جمهوری اسلامی بازهم به اربیل حمله پهپادی/موشکی کرد ، همچنین شنیده شده چندین انفجار در این منطقه گزارش و تایید شده
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/18562" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18561">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آی 24 نیوز:ایران از حزب‌الله و سایر گروه‌های متحد در منطقه خواسته است تا در حالت آماده‌باش کامل قرار گیرند،زیرا درگیری‌ها ممکن است در هر لحظه‌ای تمام عیار شوند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/18561" target="_blank">📅 16:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18560">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f38997170e.mp4?token=rINYAtLkbnkDJwv3AieCWmx3D59kcLDXO2oo9ntuDw-wEBhoY2T5UV7nq9QEXbAkNDY3DYaG1fKdYCBegauTE9xziOobaP4rophezv1dW9etPzO_bBuSz3841JlHt5eO_hpDY6GQIXYoiqhYKxAKMf_hGKrU6DJCaQn3ycP7bnIUrHCGylZHdMoQGiLuL7RmofmQzE5hlnl2rA-Oj6rIACOFGSTZjS3ZH6NKm9SeAHa40oAGEGwYLo8Z7fuBbbAUHRuRvMRr3LPCMh1r2JhkYT6imcd5-iPeHGsY-Qi4Ny2tRsmfd0Q_nFM0sgHiibGsZRwI0HiSvDKzmSAIw0ia2pqQCbqIV4iP9u2lLo69Nn8OIA0TOwLmdGMR7DdIh3G2gMxV8LtOwiWaJbUrpzuRoBLI8nMcFYZJBJqXAlvL0onh6_ew2emp4FMy2l9HVVy9OpuCZxmw08ieLD4cAuXmMd398vMI4g7gfac6F28H1-W9g_sbWGCJ0p_ZT9cOGohG4f1ItI5zI3jgRNbW9tQgkUO7seqxUVMUM5GSmaT1mvcx3ZNmhh614oA5N1to82KoWJqX0RN00NcjE_As_SPRhiuoAQgFR3TAhHvJPoPO2hNDAZc6jpu-odrAfnx8kFLXjdNALy2WXEq8oEh1LAt7Mg8f7egJj7rejESVjVZrb7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو شبکه خبر مجری زنگ زده به هتل کرون پلازا عمان و داره جاسوسی می‌کنه ببینه  چی شده
@WarRoom</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/18560" target="_blank">📅 16:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18559">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رحیم پور ازغندی نماینده خامنه ای اول در شورای انقلاب فرهنگی:
اگر جنگ نباشد اغتشاشات شروع خواهد شد!!!
@WarRoom</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/18559" target="_blank">📅 16:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18558">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سخنگوی سنتکام، به شبکه تلویزیونی الجزیره گفته است که حملات ایران به کشورهای حوزه خلیج فارس «هیچ تأثیر عملیاتی بر نیروهای ما نداشته است»
@WarRoom</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/18558" target="_blank">📅 16:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18557">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgovY54a4x0TJeC666iRV9qT6wgnTGEBkwelFlCqm1KkKExLNFV_QbQR4NzYxBaL8r-6P35boQxcJtE9_n14ft5CT0DZpW6QEDxsiHia3zYm40xvXSGjM77xUxn7LhaFdhiCuVc54OKdBYjQMob-M23suVbX4tijGenLi-58OS-J4Ku1u9FKl_m231xSpmBVqbFliDt5qPswJrM_fo1UyUWWZLBem2Fm2JStODTozwlfz3TGjjm2PlJZe9st_Mqp0WKPlLHCr33Mvf6HsSvFtRNCpb9RE_SYYFlJHgS0em8bcfTItVT75On4L2F9hkI-_zq24MRvW_EO5FyByYQ1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :سخنرانی دیشب بازخورد خیلی خوبی داشت
لایحه «نجات آمریکا» رو تصویب کنید، ممنون
@WarRoom
لایحه «نجات آمریکا» ترامپ (One Big Beautiful Bill)
است. این لایحه حدود
۳.۴ تریلیون دلار
اثر مالی دارد و شامل این موارد است:
کاهش مالیات‌ها، افزایش بودجه مرزی و امنیتی، تقویت ارتش، هزینه‌های انرژی، تمدید برخی معافیت‌های مالیاتی ترامپ، افزایش بودجه اجرای قوانین مهاجرتی، و تغییرات در برنامه‌های دولتی مثل Medicaid و کمک‌های اجتماعی</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/18557" target="_blank">📅 15:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18556">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18556" target="_blank">📅 15:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18555">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚔️
💥
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18555" target="_blank">📅 15:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18554">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آی‌۲۴نیوز: طی حملات دیشب آمریکا، هفت پل و ایستگاه ریلی قطار در ایران موردهدف قرار گرفتن.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18554" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18553">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPJ8fBmOHva7fZWCNaKAmwU8P8KxSOGNsSIGtISkBaoZejUGiusMffPnXevBD-gKhlKI6nRzrvdYnLS_x_1Aj2Eq47zX3nF28ebPb3G-tqH4CPDmXPELWZ__vyAjHrkw5dJ4PedVTohUM59d2nyPS_oeZNHFv1NdwRcFgE28rrjFGTtOhmYHP-WZBGog1FERjvdvN74Uv5-dFPBdDIrb61s-NjoSsBrLR08-0MEfpsLtWT1G2Bt_2SYSCq5rG6m_G81QbaRluSIVOKzkXVGrcFhmtjCJqqz-IiyFeF8c_Wu12jXg9RuKdpJx-HjNqPOV-m_q-ra6WmwSit1F_q8Law.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در بندرعباس مردم قایق‌هایشان را از اسکله بردند و جلوی در خانه پارک کردند!
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/18553" target="_blank">📅 15:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18552">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Remix Az Asemoon Dare Miad Ye Daste Hoori ~ Otaghe jang</div>
  <div class="tg-doc-extra">Yashar</div>
</div>
<a href="https://t.me/withyashar/18552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
@withyashar
📱
https://instagram.com/yashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18552" target="_blank">📅 15:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دولت انگلیس بعد از اضافه کردن سپاه به لیست گروه های تروریستی:
از این پس هرکس در انگلیس از سپاه پاسداران حمایت یا با آن همکاری کند، ممکن است به ۱۴ سال زندان محکوم شود!
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18551" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">المیادین: بزرگ‌ترین شرکت گازیِ طرف قرارداد با یک شرکت گازی آمریکایی در عراق هدف قرار گرفت
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/18550" target="_blank">📅 14:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چند گزارش از صدای انفجار ‌در ‌اهواز
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18549" target="_blank">📅 14:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNiJEZKBvR5ffbnpRG2vwl96dQKGXQPX8UrrwX9iGJiSJHMVosuvHpjdOS0s_WGnjbhKmhnjB-_LDr16M5IvI0YOHo_aYH5dyPdH0Ir4BCbsEK4HOZVKcfW-_aLFvW5G1_Jq01L6sNl8eXgrz1cttvJKaG699bonlAEvw4TGMLkLlv2wbGnfiDgA0xy3lZ8huqgNPkZNV-6RUOC8uxkn1G95GlpWpUpioEdTE2uzCGIkwkaekVQ80GwKv3OXC4Gzyq8ow3MW0FD9_o7Iw-1IHcaPJn7Ruh5P_N_TsOygu5A-tkB3zZ4RfU4LNqC7lmkUIsPJyCxR2mrUW_tE5afbyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در 24 ساعت اخیر سرچ «لغو عضویت جانفدا» بیش از 5 هزار درصد افزایش داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18548" target="_blank">📅 14:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44c5aeeaa6.mp4?token=bvjP9iajQRLabp0VeckbDtAJ6mBDQZ_9vQqGxhxl3KmUTD9AD_vKX0lROPRKAV2LvVhslV4G9dlPL_MiDf3DoiHJlB5OmZpfcno8HIKFx3kCpQvVL7Io9Rp2RuA_zDS5b4TBl8HW_-IyDS-6ZGaEk_lrvhs4oX3RneF27q0znJfF03hOhp2UVNDizytNtOagb1KVGunujRC0u7TI2XgBPpXK2KIcRA0M3kNSDT4x-Z-Q4HgTYkteTSgc4Fqb6ftFrXpD2YpsddyiymgF_cRakroCkiZOSR3xD_wI8jrt-j_BArm0L_ND2_K7Y12lQQsYYJrmMKSnL0eb1CNzYmVeFQdj9IQqoRGfgnGg1vPf736xOOUS6J8JX9tS66hL7Cb2suZdcOoGxGwQpvUL41cYJVho5jPcIoJzgYJB5k2BqwHLDzzTWVYssCiga1awywCDGaY0uPQPQ2SGe5vv7IJ2umvigqfFbJVtKAOy-8DDzNGVGjUt24pWQAxQbeMhX9lk6YZUDY-f64TruBRO_K9qpFnP4OsLbfkKFTd4OUNKeSxXK3QYk-nqELE5JmnHp_gXNIBGi_wHW74TMqvZxAP0uQQ_ZhWzXUvYvuTSW39cmpnWc5T8mwcC3fWC-gShnJ3oFthInQzzUtPgeVIlh3yhLIhL03nTTmNYZuCMiWbszqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44c5aeeaa6.mp4?token=bvjP9iajQRLabp0VeckbDtAJ6mBDQZ_9vQqGxhxl3KmUTD9AD_vKX0lROPRKAV2LvVhslV4G9dlPL_MiDf3DoiHJlB5OmZpfcno8HIKFx3kCpQvVL7Io9Rp2RuA_zDS5b4TBl8HW_-IyDS-6ZGaEk_lrvhs4oX3RneF27q0znJfF03hOhp2UVNDizytNtOagb1KVGunujRC0u7TI2XgBPpXK2KIcRA0M3kNSDT4x-Z-Q4HgTYkteTSgc4Fqb6ftFrXpD2YpsddyiymgF_cRakroCkiZOSR3xD_wI8jrt-j_BArm0L_ND2_K7Y12lQQsYYJrmMKSnL0eb1CNzYmVeFQdj9IQqoRGfgnGg1vPf736xOOUS6J8JX9tS66hL7Cb2suZdcOoGxGwQpvUL41cYJVho5jPcIoJzgYJB5k2BqwHLDzzTWVYssCiga1awywCDGaY0uPQPQ2SGe5vv7IJ2umvigqfFbJVtKAOy-8DDzNGVGjUt24pWQAxQbeMhX9lk6YZUDY-f64TruBRO_K9qpFnP4OsLbfkKFTd4OUNKeSxXK3QYk-nqELE5JmnHp_gXNIBGi_wHW74TMqvZxAP0uQQ_ZhWzXUvYvuTSW39cmpnWc5T8mwcC3fWC-gShnJ3oFthInQzzUtPgeVIlh3yhLIhL03nTTmNYZuCMiWbszqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت انفجاری ‌منطقه
🚨
🚨
🚨
🚨
🚨
💥
۴۰۰ هزار نفر در اتاق جنگ با یاشار!
سپاس از همراهی و اعتماد شما. این تازه آغاز راه است.
🎉
400,000 members in
@WarRoom
with Yashar!
Thank you for your trust and support. This is just the beginning.</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18547" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کپلر (Kepler) که به تحلیل داده‌های دریایی می‌پردازد: کاهش چشمگیر تردد کشتی‌ها در تنگه هرمز. دیروز، تعداد کشتی‌های عبوری به 8 رسید که کمترین میزان تردد در 3 هفته اخیر است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18546" target="_blank">📅 14:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">هم اکنون یک اسکادران بزرگ از جنگنده‌های F-16 آمریکایی با استفاده از چهار هواپیمای تانکر سوخت، در حال حرکت به سمت خاورمیانه می‌باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18545" target="_blank">📅 14:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8008a8ae42.mp4?token=AwtrzhQPvCSIA3uCm5reSXG9zuHE7IFXYigrP6r3uQXz572rJNxKdBRYlczCETb7Qce8uPxdLTRxF5tU2oUWOm5zDGhZ2mTUNgv5xrWJnxooNpkEXYoVfqNwLXCPCAPICfBPK3YcZrQpQVAkJ2a4GSxa-L_yE2V6vduK5aUS_y1_uwFKbe3e62S3ZCMcZ6gVGs50dnAF9gsGhzjkGFzteDamAXc_NzN172lGL5XM_puax8YHKXXnXvMrokCUpuOOhDO-UR2sBKbe1rqAJISkWHT8Dw1Dfpx96nqGXEmKuC7vHR9tNvohJ8Jz16-B0T2pSRpKd6J_9kjeL6xtfrSimIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8008a8ae42.mp4?token=AwtrzhQPvCSIA3uCm5reSXG9zuHE7IFXYigrP6r3uQXz572rJNxKdBRYlczCETb7Qce8uPxdLTRxF5tU2oUWOm5zDGhZ2mTUNgv5xrWJnxooNpkEXYoVfqNwLXCPCAPICfBPK3YcZrQpQVAkJ2a4GSxa-L_yE2V6vduK5aUS_y1_uwFKbe3e62S3ZCMcZ6gVGs50dnAF9gsGhzjkGFzteDamAXc_NzN172lGL5XM_puax8YHKXXnXvMrokCUpuOOhDO-UR2sBKbe1rqAJISkWHT8Dw1Dfpx96nqGXEmKuC7vHR9tNvohJ8Jz16-B0T2pSRpKd6J_9kjeL6xtfrSimIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف تانکرها در نزدیکی پلی که بمباران شده است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18544" target="_blank">📅 14:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C79NYK6W9Natm7F47m9Qk-Xpcek8nqFjI2K5k6NaOejuPXiv97qMW_BXXwv-OwoNqf_LEs2jh3XHV5NkKafQC_HSFSb5O284WeliKf68ygcmNZNm-61eZTyGO_zAJuV4F1Y1W3M51d7q2eLbTeCizn7jAuXD4p9C3pNgAW_MumC6NJEqHlbLTB4nBM0Kh7W2nwHkdRPNSkT6egUtm_rJ4tIjMG1BLE_vt0ccganqzLD1rTAyarkQnbefXICHTYlXEkVLa2VVtD7Wh5p5Q2I-SbP-quABu-XPYeA6qvcj0RDl6aAc1rjfvaiOB8YVczFGT0-vTElOC4PA9lPSNNXS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتر تا ۱۹۵،۰۰۰ تومان پرواز کرد و هم اکنون ۱۹۲،۰۰۰ معامله میشود
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18543" target="_blank">📅 13:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18542">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315ffdb490.mp4?token=WFEYCQ0Y231IzhUkiCKbPzVoI5-w52zt94KCgXguqecQwi3CfXDJmbj6WxFkaa_S8XM9VpDCl1Fzx6tcEtShcwoDxaYGaerPbC4iIXHP_ykqpz43Ktnav6SQ7HYN-uh4Y5fHVGEhQ22POc39M7DCxz8t9nyrxjdMNI0xqte05MwSMapOrgwaLXMG1ITV5Y-GEEkFlwfmEJ22oXjIIifJhdMBkPPNHIgLPbQ-s_hJDHEGM5lnAXAVRpnDJdsWLgN56awAcDh_xtSG9THMdt5eYu0vQXZr67OvpbeHVu47svRxK5KqI0pN1ByEkggrp4aCzcTYeYFGj54z3iLY6aTbhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل مسیر به گچین و بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18542" target="_blank">📅 13:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خبرگزاری CNN: ترامپ در حال دریافت گزینه‌هایی برای گسترش عملیات نظامی آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18541" target="_blank">📅 13:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18540">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ونس به NBC نیوز : فکر نکنید کنترل امنیت تنگه هرمز کار آسونیه؛ این کار حسابی دردسر داره، چون با پهپادهای ارزون‌ قیمت خیلی راحت میشه کشتی‌ها رو هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18540" target="_blank">📅 13:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سپاه: جنگنده‌ها و سوخت‌رسان‌های آمریکا در اردن و مواضع آمریکا در کویت را هدف قرار دادیم
سپاه پاسداران اعلام کرد در
موج ۱۴ عملیات نصر ۲
و در واکنش به حملات پنجشنبه شب آمریکا، با موشک‌های بالستیک و پهپادها جنگنده‌ها و سوخت‌رسان‌های آمریکا در
اردن
را در دو مرحله هدف قرار داده که به ادعای این نهاد،
چند فروند سوخت‌رسان و جنگنده منهدم و تعدادی دیگر به‌شدت آسیب دیده‌اند.
سپاه همچنین در
موج ۱۵ عملیات نصر ۲
مدعی شد علاوه بر
انهدام سکو و موشک‌های هایمارس در کویت
، با حمله موشکی و پهپادی
چندین محل استقرار نیروهای آمریکایی و «ضدانقلاب»
را هدف قرار داده است. این نهاد مشخص نکرده منظور از «ضدانقلاب» چه گروه‌هایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18539" target="_blank">📅 13:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31df15619.mp4?token=A5E8S4G2TcRYsYoLQHmYQ0F72HEENbB_1uV6dU4vYtIBy-2owkpMgv4JEe6Ca1us-3-1KkMWLMZ_vibWPND8yFxaIUnGbVjEciiAOv4vLvgrCr9sgR4xxJZj4iTJZeGBCZxTQTp5Lqx0IMDGkWWKQfLSapTvU96QX-50fnn6Ky8Rj03vNiU8uEDZsDKMV7tQ_T2lPMaFFj-HnBd1YwXQaHeL877okZN9qpoMMlMMP-rwQi6yXmwHZcT0aQXbx6kpb8SyHG0Xe7rv7vB-frGvDN70n9DBLb8LKg0_HkjVT4B-54mOUWiFzOuJ4IwhMPazpICyX9OXCu5-zOd4eyIxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31df15619.mp4?token=A5E8S4G2TcRYsYoLQHmYQ0F72HEENbB_1uV6dU4vYtIBy-2owkpMgv4JEe6Ca1us-3-1KkMWLMZ_vibWPND8yFxaIUnGbVjEciiAOv4vLvgrCr9sgR4xxJZj4iTJZeGBCZxTQTp5Lqx0IMDGkWWKQfLSapTvU96QX-50fnn6Ky8Rj03vNiU8uEDZsDKMV7tQ_T2lPMaFFj-HnBd1YwXQaHeL877okZN9qpoMMlMMP-rwQi6yXmwHZcT0aQXbx6kpb8SyHG0Xe7rv7vB-frGvDN70n9DBLb8LKg0_HkjVT4B-54mOUWiFzOuJ4IwhMPazpICyX9OXCu5-zOd4eyIxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏کل وزارت صنعت معدن تجارت این روزا:
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18538" target="_blank">📅 13:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca43767734.mp4?token=ViZKKC3vueqCYvLN2dpV8QAOQlj1qYckH5cRXSJdEaWGWB3_Ye8RSI2osfr8zUMyGfuCRCfrYWXGdTSXWuo9973x37Z-9gvqGrYaI7WwJBCFhTXEvKiBAkO5b49Ns88EZYy4Uw5xNKTyBxHNuUpMMbevH2YfxpgjiPm2BnL2v6RCF60Dx08ev72tW4nhHtFtlLMUdFYWiX3oNJXTNAzmKmsznL0USNDSnrOkSXR0JCa60AtAeokXqIY_I2BdIir5IuX_WXd0pA2k40mo_ddCYdXyENyzKwrMiSUvXZHUnA8lyYV6RLfi88kLAHFtvVXR2XnE6N1KFckbNKlmZz4FYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه هوایی  عقاب  در جنوب که در زیر کوه ساخته شده و قرار بود از جنگنده‌های نیروی هوایی ایران در مقابل حملات هوایی دشمن محافظت کند با حمله مواجه شده و تونل‌های ورودی و خروجی بسته شده
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18537" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=uVGSBrVH42d8yJDCc5m2ORGDkAUbKtw443vNyoYJEp5P2C1y4QakljZ2OI3RMV0XFKXy8V1iHyjfXLFmt2N0fWUHRq1cPN5QXR4x5AxHsxHlxejohINz-IyZn0DPbCdwIARo1WPU54FsY2tAyoMmqocWmxe6EhJ8_SzclZuKr1tluR9CuE9Ehw42cMQBEMRL60RRt-uPpFlP7eUArGcppgFcsW1y4ifg0zTpIPKxTVkVj-V8S0mfb6q0e72qr5CJABrSqgdViCn20zr5ndCbIo9G-nQJLA93iKtLF01zC4M2u9ytu_8f0Fw24H2NOYFuAkZaQ26BOdrqugu2tAggNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0c4907fb.mp4?token=uVGSBrVH42d8yJDCc5m2ORGDkAUbKtw443vNyoYJEp5P2C1y4QakljZ2OI3RMV0XFKXy8V1iHyjfXLFmt2N0fWUHRq1cPN5QXR4x5AxHsxHlxejohINz-IyZn0DPbCdwIARo1WPU54FsY2tAyoMmqocWmxe6EhJ8_SzclZuKr1tluR9CuE9Ehw42cMQBEMRL60RRt-uPpFlP7eUArGcppgFcsW1y4ifg0zTpIPKxTVkVj-V8S0mfb6q0e72qr5CJABrSqgdViCn20zr5ndCbIo9G-nQJLA93iKtLF01zC4M2u9ytu_8f0Fw24H2NOYFuAkZaQ26BOdrqugu2tAggNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت همین الان پل بندر خمیر که کامل از بین نرفته و خودرو سبک عبور میکند
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18536" target="_blank">📅 13:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند @WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18535" target="_blank">📅 12:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ادعای اینتل‌واچ: سناتور لیندسی گراهام توسط سم نوویچوک تماسی
(استنشاق، بلع یا تماس پوستی)
کشته شده است
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18534" target="_blank">📅 12:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانال ۱۲ اسرائیل : موج بعدی حملات آمریکا قراره خیلی شدیدتر باشه و‌ احتمالا تهران و بقیه شهر هارو هم بزنه.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18533" target="_blank">📅 12:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حوثی‌های یمن به یک کشتی در تنگه باب‌المندب حمله کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18532" target="_blank">📅 12:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کویت اعلام کرد که یکی از ایستگاه‌های تولید برق و تصفیه آب مورد حمله ایران قرار گرفته است، که این حمله خسارات زیادی به واحدهای تولید برق وارد کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18531" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=oY4J06yYTzxo7FNw8tiBNukVWW1stsE1trKxBxkWaxND60BT0mJAwnDBAAxjvKX_VCklHDXOJg-GRT_IiSJIMjHD5fCDPKFcBmCCTYptXYAMRnqx6V3IMU5nBVG8AjQTnAhqPrkq_bE4SPRLVi22qPhRfVBZxlIH1OpYES2mGgSRhow4uo6bEPWx5-5GvT6pigd4uhJkUpt5S_kcpXx2SLZ8RHsAwz3m4YlJ9JzOh7il5Ym00Rdph-DBUvAP-i9wGDV11IFfQcBlmBc5jeCe4cvbohgnMP2Dew2Ft6RagTkHLcdP2K_hGkb-s13aGiQSnN1DYC9JJg8-y23lDOV1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896d0f778e.mp4?token=oY4J06yYTzxo7FNw8tiBNukVWW1stsE1trKxBxkWaxND60BT0mJAwnDBAAxjvKX_VCklHDXOJg-GRT_IiSJIMjHD5fCDPKFcBmCCTYptXYAMRnqx6V3IMU5nBVG8AjQTnAhqPrkq_bE4SPRLVi22qPhRfVBZxlIH1OpYES2mGgSRhow4uo6bEPWx5-5GvT6pigd4uhJkUpt5S_kcpXx2SLZ8RHsAwz3m4YlJ9JzOh7il5Ym00Rdph-DBUvAP-i9wGDV11IFfQcBlmBc5jeCe4cvbohgnMP2Dew2Ft6RagTkHLcdP2K_hGkb-s13aGiQSnN1DYC9JJg8-y23lDOV1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون با صدا درآمدن آلارم حمله هوایی در دوحه، پایتخت قطر، پدافند مشغول دفع حملات است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18530" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آلارم حمله موشکی در پایتخت قطر دوحه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18529" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=slsX7xgOfejKc_GqUE4Yj2VsW_f2oA4ftMyiUnluGnTkJP3sfDxxusRTmRSDDRrEfrvhcaqoadjUUMX9xqAoglVUqDxU7C2jMcuxWKtqyg1NzLUhplX-nSyg1Vlt2_6BXH1DscQ37h21srix4tEF87mhN7Af6d2ys5dRKIxupbuAXDYvMeWuqITe35K3yoDg3tvRfAE7anhxlWiAG7NSm_R0rUx2zM8lNUsQ_RLGHCgQiifxHMnDUc-Rd-W5sgqzlJsNwkskrQQBN1OQG3c3Ncl3tnvACqZIq3p-aCxv_-mIi8JvX2c-MnYS1E1rWP9hM6MMOkfUptR0iOyItZJoQzIUVKA5WmxEIvrcO07ZVbc2JtTKWF2zGyStjQOMWjcy_KK_axkuSW8SHSbiEIxIZJS1r7Wzt1w1rELmLCOYycnbsqti1HUT7QM23st_tsLMNXIZapUvIE-_xqHg-bE3Qlb3u2gIrqXPq9F7GiYs_yhrbM_P9gYZXJ61RQOT33mNioQZeaf1AdFAI8C-brRS_sbB7mOGj4r7IOFql8HlagMJsPXkz2BMfAtRL6yYN-bJj1Ytxdju5eOrYrDvF6kTdl_AT6yBhGeixmGqgJaP5mDbvrpGuBJL9-7r-HXVmp3DVExpAyoEhNMk7oWsrxqo8CQOtri3A6y7Sagar1W_yvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e27b43e6c.mp4?token=slsX7xgOfejKc_GqUE4Yj2VsW_f2oA4ftMyiUnluGnTkJP3sfDxxusRTmRSDDRrEfrvhcaqoadjUUMX9xqAoglVUqDxU7C2jMcuxWKtqyg1NzLUhplX-nSyg1Vlt2_6BXH1DscQ37h21srix4tEF87mhN7Af6d2ys5dRKIxupbuAXDYvMeWuqITe35K3yoDg3tvRfAE7anhxlWiAG7NSm_R0rUx2zM8lNUsQ_RLGHCgQiifxHMnDUc-Rd-W5sgqzlJsNwkskrQQBN1OQG3c3Ncl3tnvACqZIq3p-aCxv_-mIi8JvX2c-MnYS1E1rWP9hM6MMOkfUptR0iOyItZJoQzIUVKA5WmxEIvrcO07ZVbc2JtTKWF2zGyStjQOMWjcy_KK_axkuSW8SHSbiEIxIZJS1r7Wzt1w1rELmLCOYycnbsqti1HUT7QM23st_tsLMNXIZapUvIE-_xqHg-bE3Qlb3u2gIrqXPq9F7GiYs_yhrbM_P9gYZXJ61RQOT33mNioQZeaf1AdFAI8C-brRS_sbB7mOGj4r7IOFql8HlagMJsPXkz2BMfAtRL6yYN-bJj1Ytxdju5eOrYrDvF6kTdl_AT6yBhGeixmGqgJaP5mDbvrpGuBJL9-7r-HXVmp3DVExpAyoEhNMk7oWsrxqo8CQOtri3A6y7Sagar1W_yvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خیلی وطنپرستی ‌نبین حالت بد میشه
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18528" target="_blank">📅 12:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ورود تانک‌های ارتش اسرائیل در مناطق حداتا و حاریص در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18527" target="_blank">📅 12:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18526">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">علیرضا فغانی داور فینال نشد.
فیفا رسماً اعلام کرد اسلاوکو وینچیچ، داور اسلوونیایی، قضاوت فینال جام جهانی 2026 بین آرژانتین و اسپانیا رو برعهده داره.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18526" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک مسئول در حزب کومله کردستان ایران:
شش موشک به مقر ما شلیک شد، از این تعداد، سه موشک به مکانی اصابت کردند که در آن هشت نفر از نیروهای پیشمرگه کشته شدند، و سه موشک دیگر نیز در نزدیکی همان مکان سقوط کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18525" target="_blank">📅 11:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: هفته آینده خاورمیانه تغییر خواهد کرد و همه باید برای آن آماده باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18524" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال ۱۲ عبری: آمریکا در حال تهیه فهرست تازه‌ای از اهداف در ایران است که تاسیسات تولید و انتقال برق را شامل می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18523" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فیلمه لحظه زدن پدافند کنار نیروگاه اتمی بوشهر @withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18522" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : ویدئوی منتسب به بندرعباس که راننده ای در حال رانندگی شیشه های ماشینش بر اثر موج انفجار خرد میشود، بسیار قدیمی و مربوط به جنگ چهل روزه و در مکان دیگری است من در میان جنگ پست کرده بودم
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18521" target="_blank">📅 11:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نیروی دفاعی بحرین اعلام کرد امروز چندین حمله موشکی و پهپادی ایران را رهگیری و منهدم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18520" target="_blank">📅 11:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال استریت ژورنال: اختلاف میان محافل تصمیم‌گیرنده در ایران گسترش یافت
‏ گروهی به دنبال تشدید تقابل با آمریکا و کنترل تنگه هرمز هستند و گروهی با در نظر گرفتن محاصره دریایی و تشدید جنگ نگران وخامت اقتصادی هستند
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18519" target="_blank">📅 11:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه پاسداران صبح جمعه در بیانیه‌ای از «حمله غافلگیرانه» به سوریه خبر داد. در این اطلاعیه هدف حمله منطقه تنف و پایگاه نیروهای آمریکایی عنوان شده
@WarRoom
یاشار : خوب سوریه هم اضافه میشه به حمله کنندگان از امشب</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18518" target="_blank">📅 11:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBhIegXES6v3lpoXNS-kDw_BdRcd7KYSZYOhth7oTGaKZJgsCo7H8fLlHAoGY6XRsoLISUUE-I5ISOY_4z8sAZAJzJWTv5gFiny8vvQaBXHmkb0DE6HRyHLVtrsEtI99iix-_hCs4mn6JAPnJ7kPLCIgaw2VwKL6gTBCJEmtNvDONob6PvJhCMroo5O4n6nSL2eFDBLKybxHqwuB0u2vNtWS9q0S-wI3h4d_m5TPIPOAb1MWbfR2KVR-WUAck7o8rwwvnhYlelpAhOSF0OVy7lJWALD5x99-RWF3zNfa68QVv-fCGrFDoLYEZl83CUyPB9QXpls3SBXf0_Kp6hP8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18517" target="_blank">📅 11:07 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxAIstTIriBy7VXBvAI40Kr9k9-_WcIFryactzwPsKPuvZQqMg9C8CP6S0UIn6QjwxS6er9PX_c9dv2_hP6EJ4XKR3LkieXuAITArghFyQmrwmkv7YAZo410yfnF2d6FvycPjhnTLrH2TKn56QeSBFx8kraKx1hJGZ9yRTqcpXWQbG5_MggiVK87-JB7BhNnq4_Iofpu002kIE1CkDXyzGmJJ331KJVJPG0XHulWRZB80TqEfJmj4sm8_j0P9hW8kZxdVbxd9C6N7a3tyYzBjU5dGtvHnH7GVQKQ9Tz3UQpt0hiePhKaGBhhrnRFPBjUUY-OC7IdH3NO_CVzdfksig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی اسرائیل با پهپاد،
یک مسجد در لبنان را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18516" target="_blank">📅 10:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : دیشب عباس چپقچی هیچ جا نرفت و اون یک هواپیمای معراج چارتر ایران ترکیه معمولی بوده ادمین های بیسواد دنده دادن
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18515" target="_blank">📅 10:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKa27mbgpiVBziYVXDizNd1-1NLUzfad8IlFbYsty708IfQBF5krcvBpic6tmZ5VHebhGMKQ3okOrJuoDCkjMoV4SgwFdTj9PtZ8Hv9Y2_GH6HihYT0hd563CnuiBSYNFrX_M-cFhWCgC3XQRfJErVK9lpuIkeWx8LfuxZVDzNDiDy07K2923K7snWD2NjZDh9zUCFSNrWgDvaD0w62WrAkQSOo-MR9Uz2Q7DSalx2T34oaMUbbFgMbqJJTEjCU4ZLcGvnNMjV82AbUUg_XNnloZ47OOCYUTG8slaw7_vnnhf4W3P-DFdSN3eM55_HmWOSdGywMuhlhrbevJMBGM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی قدیمی از جی‌دی ونس، معاون رئیس‌جمهور آمریکا، با تی‌شرتی دارای نماد اتحاد جماهیر شوروی در شبکه‌های اجتماعی خبرساز شده است.
وب‌سایت راستی‌آزمایی Snopes تأیید کرده که عکس واقعی است، اما توضیح داده این تصویر مربوط به یک مهمانی هالووین است و ونس در آن لباس شخصیت کشتی‌کج نیکلای ولوکوف را پوشیده بود؛ کشتی‌گیری که با نمادهای شوروی شناخته می‌شد
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18514" target="_blank">📅 10:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حمله به یک نفتکش در نزدیکی سواحل عمان
سازمان عملیات تجاری دریایی بریتانیا اعلام کرد یک فروند نفتکش در شرق خصب در نزدیکی سواحل عمان با پرتابه‌ای ناشناخته مورد حمله قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18513" target="_blank">📅 10:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسانه هی رژیم
: پالایشگاه‌های نفت و پایگاه‌های نظامی آمریکا در بحرین مورد حملۀ مستقیم پهپادی قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18512" target="_blank">📅 09:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=oKmE_dhVWRIZGGMnQes7HLh6xKHeIOTC0H82EA1or2KKLLEmOhwG3GoVndr-Lzjs4dPxNaNjLXmZwz42AdKgwYwBI-eYi89aI7h7Wh4ibLqqZ46OqCzn7sZoF9Xlp3NzEie9p3jnDaYB2u6OhZB95d9Ai5oVoPShWfoRDg1xUbHCgDucAVnh6XbLkjnkaRmmOPtS4eeQPf9Ywt75LjrnJCCbUCuA8YP3kv4zfyoXUrbsQEPsAIUBHDcI-JrZyQctnqzh4PjLY4-7mFcRKkqgb1J8e5pPHW8Qi6pTM_21cAiEK61YNSbWwmpCDwYoe84SDgEykxZiZ4k2yaVxmrKutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=oKmE_dhVWRIZGGMnQes7HLh6xKHeIOTC0H82EA1or2KKLLEmOhwG3GoVndr-Lzjs4dPxNaNjLXmZwz42AdKgwYwBI-eYi89aI7h7Wh4ibLqqZ46OqCzn7sZoF9Xlp3NzEie9p3jnDaYB2u6OhZB95d9Ai5oVoPShWfoRDg1xUbHCgDucAVnh6XbLkjnkaRmmOPtS4eeQPf9Ywt75LjrnJCCbUCuA8YP3kv4zfyoXUrbsQEPsAIUBHDcI-JrZyQctnqzh4PjLY4-7mFcRKkqgb1J8e5pPHW8Qi6pTM_21cAiEK61YNSbWwmpCDwYoe84SDgEykxZiZ4k2yaVxmrKutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد MQ-9 در آسمان چابهار.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18511" target="_blank">📅 07:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18510" target="_blank">📅 07:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=oXOd1DVL0dMTWLCm0XdYgzj0MGQ0BgvqpFmlxfsCdZyMIBcgmjjDUo37YIkkYCiqCI5AQpBswZXh5z-cmctjPQiYHG2LvcgcuzFp9H0czvwL3QNHCY1iBtaYoWcxCnZAprOtiIIlYmfPpMXF-wW9okWn6u0Hhpe2HuI539zMr4wAGbBaIDT_SmS-0Y2GBblvb5a5AlNrddaR_Zp5i-ARiLH5nZjixGBm9jC-AF2e5pMsl50O-VSd09RJyC-5Ad-tq_ewAG-IXEJlxqyQhQM89JQtDNP0jnSUlefRTw9-fZKfAJ-MmG0t6r4HCmhrVi3boWcepJd9xlInrcqr5HD9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=oXOd1DVL0dMTWLCm0XdYgzj0MGQ0BgvqpFmlxfsCdZyMIBcgmjjDUo37YIkkYCiqCI5AQpBswZXh5z-cmctjPQiYHG2LvcgcuzFp9H0czvwL3QNHCY1iBtaYoWcxCnZAprOtiIIlYmfPpMXF-wW9okWn6u0Hhpe2HuI539zMr4wAGbBaIDT_SmS-0Y2GBblvb5a5AlNrddaR_Zp5i-ARiLH5nZjixGBm9jC-AF2e5pMsl50O-VSd09RJyC-5Ad-tq_ewAG-IXEJlxqyQhQM89JQtDNP0jnSUlefRTw9-fZKfAJ-MmG0t6r4HCmhrVi3boWcepJd9xlInrcqr5HD9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشکاز لار ، جنوب شرقی فارس
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18509" target="_blank">📅 07:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766440ca91.mp4?token=J5paqaqoCjHJkGljy6Mh1kJNi8g9C8wGrxHnkMpuRcaxYhqcna_sZll1xfGJNsOw81SIgEkkme5Du9yiolUHRKaj_-MmpKyVP1lx1IG6Y7Slm3xt9EmNSQjKe5f2-IBzU9Z0BipDZl2MKjY6MfhwFlnytfb5RXXD1C_7EavF1g-gHYKevp3ZpKpmM-nEImhpL1iqtgg2fZfxAse-tyjFsCY_h8u-Uq6Ggj7bgNntiJGndLk4Y9HwcaD2Lygh1mx8RNphG9zAHxi_e3rPo6K1Jr8c663mTMMGo1lvIKz-7dW1ZUUsjjCqPxHEon0WY8D_QQMk608pEuH3lxsmeMKycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766440ca91.mp4?token=J5paqaqoCjHJkGljy6Mh1kJNi8g9C8wGrxHnkMpuRcaxYhqcna_sZll1xfGJNsOw81SIgEkkme5Du9yiolUHRKaj_-MmpKyVP1lx1IG6Y7Slm3xt9EmNSQjKe5f2-IBzU9Z0BipDZl2MKjY6MfhwFlnytfb5RXXD1C_7EavF1g-gHYKevp3ZpKpmM-nEImhpL1iqtgg2fZfxAse-tyjFsCY_h8u-Uq6Ggj7bgNntiJGndLk4Y9HwcaD2Lygh1mx8RNphG9zAHxi_e3rPo6K1Jr8c663mTMMGo1lvIKz-7dW1ZUUsjjCqPxHEon0WY8D_QQMk608pEuH3lxsmeMKycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18508" target="_blank">📅 07:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزارت کشور قطر اعلام کرد که در پی حمله ایران به این کشور در بامداد جمعه، کودکی بر اثر اصابت ترکش‌های سقوط‌ کرده مجروح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18507" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=Hhh9bTNdW8d8eq6xT7yFsqClB9LGl_ARgqJyXhnJzfKGhDSK5qV73dep30LUkGDTuE-uOH0Kfr1su_EIylpGCzQ2LoK-z9oU_f-Z-ZN_vRaDwMqbYFUxFsmpKxkWdx27U2mIe7u9ySZNxNsaLgydrJ6_K5ufG0YIbugcHs7HsihHCpx8wKFN8OPjei_cjcySQVXHtrrmR4lVk5ZEbShWOnMDBaKMXoJPP66dlm_WuNLpKllz2dnp5AF-_TtCNiHvyEtyzm6ip0g8Qz4eNEnOAeb06r3iA41VBzgL_PdfBlaxlqPqvFY-o-aOfBk5kmKaiVvockeIaRGQqzhN2WpLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=Hhh9bTNdW8d8eq6xT7yFsqClB9LGl_ARgqJyXhnJzfKGhDSK5qV73dep30LUkGDTuE-uOH0Kfr1su_EIylpGCzQ2LoK-z9oU_f-Z-ZN_vRaDwMqbYFUxFsmpKxkWdx27U2mIe7u9ySZNxNsaLgydrJ6_K5ufG0YIbugcHs7HsihHCpx8wKFN8OPjei_cjcySQVXHtrrmR4lVk5ZEbShWOnMDBaKMXoJPP66dlm_WuNLpKllz2dnp5AF-_TtCNiHvyEtyzm6ip0g8Qz4eNEnOAeb06r3iA41VBzgL_PdfBlaxlqPqvFY-o-aOfBk5kmKaiVvockeIaRGQqzhN2WpLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون موج جدید حملات خصمانه سپاه پرتاب موشک از پاوه کرمانشاه
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18506" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma30O2KQBThPbjsjnbwkSnDJ43BjYAr3TFOE3bA5HEAx_lwguGxiPq0-fha_TnoWVAjKq6--_DDMXiYH0Bin84xg_5m5SVFvrIKcXjvGP3sVRHyLsQKv4r1798BDmBGJfzvtBBKNJtcG6p5OFpdxP2wsXNcOwMok795Z9iryu7dc8FaMX99oiNt9tA2R3hymIweAsjjBIUvwWUnj-8yOb0D-djpiymuVxVhWo3FVDPhxKBGTKH45t8UDiB2xt1kuUy5VyV5TwqjXLqhPitlB2-Chtoy-d7Z9ioel1OC6lgo2pNofgEWdgvYTA5SjVTAFwv_5QQXdiJxqof0OdFlWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چیزی از برج چابهار باقی نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18505" target="_blank">📅 07:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR_CEL5cgfkhzxR1pMb9VSaSjidE6Uat2s6e4nxwkTlqM_2lIjOg86FpxBwY9Ko5oilzWH3sTXLy3eZ-PQocKf_RKSukfkLDQri4qqShNF4sUvMAorwuEFBPmUwnu2xfHskdLgM8CN-KuDrz5Lz6GTZ9xqwvF0wa0OGpjcWsShOMU4t8CMEA2i1yOql3i1uasAzTgrX0LIEg0VoHL0Vln2Y-NIz51sv1FZVPUDQU3uLzADRYWztAde72V-6Yr8FoT4sEbF4WBADmZJe3jnbxz4koM6DPbzjPhGXbN15yJ3A_t-5w9C-g5lahjbgvXkXg5mxJYw8H741lD8lhyd3wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18504" target="_blank">📅 07:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2QqgH2aheRypn9RXqMPMZDwGSkRYX1LVUw90OQuXoJEwIATU16gnkcdP0zH0EWSixfePhkpPEVx8kabvHxAauHTRrjmQ6ziArKJknDb5kO42G5jMr7Mx0L-2UJ_3WQPRgClZ8SonJB_KDRJCHkvHZgmNE_5d5utE-CEWXbGOl5LC9fgv-tUet7GrphspFW1KI2cTtgDzYvNjsRxTkXkueIPEgH7dQDMzMfrnmYpTESawG25dTMwwouJmiEq2IxmEegTbDcqil2AFxBeNWk80f7Oog5V-KiM6gRNvklzujka4L4AuZWsHAUoKj69mFmVOst8yQ-zXwSJYQPxypuMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از استان هرمزگان شهرستان بستک شهر کوهیج همین الان
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18503" target="_blank">📅 06:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=Pmrgh0jSbJa_nsNPM12cPGBHg5iXLxKA_rjMffFdZDksljlmnnD81yzYjowQOI1pdPhYPm1H4WnEU5AdRIvQSycopsQzmBqgT0Iv-07wkGI06cLCHHbLQrs6hcct0gJq2H18ghrtIT5q3E32OLVTY3uabg6aI7O6gIuAJeb7VwMSTy9EjCd76P0at6_wosFYjEQy50SFSeBAXME5YsDr0LEQqjiKQQXTEGW-NgrBVhLmn7GeQCilfMP4oaKhN9_Ego2WzwK1lxnM8vMDn8xWKPafWMzINh43VdIqAhI4lE_9MYEsG3PNigy9wNLW2t4psVQfRSSZHgWdNPOOfH6k7A7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=Pmrgh0jSbJa_nsNPM12cPGBHg5iXLxKA_rjMffFdZDksljlmnnD81yzYjowQOI1pdPhYPm1H4WnEU5AdRIvQSycopsQzmBqgT0Iv-07wkGI06cLCHHbLQrs6hcct0gJq2H18ghrtIT5q3E32OLVTY3uabg6aI7O6gIuAJeb7VwMSTy9EjCd76P0at6_wosFYjEQy50SFSeBAXME5YsDr0LEQqjiKQQXTEGW-NgrBVhLmn7GeQCilfMP4oaKhN9_Ego2WzwK1lxnM8vMDn8xWKPafWMzINh43VdIqAhI4lE_9MYEsG3PNigy9wNLW2t4psVQfRSSZHgWdNPOOfH6k7A7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ششمین شب متوالی حملات گسترده آمریکا علیه ایران به پایان رسید
سنتکام اعلام کرد
امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا (ET) (۰۵:۱۰ بامداد روز بعد به وقت تهران)
، تازه‌ترین موج گسترده حملات آمریکا علیه ایران به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی با استفاده از
جنگنده‌ها، پهپادها و ناوهای جنگی
و با به‌کارگیری
مهمات هدایت‌شونده دقیق
، ده‌ها هدف نظامی ایران از جمله
سامانه‌های دیده‌بانی ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی
را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18502" target="_blank">📅 06:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نیوز CBS : اگر ایران نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18501" target="_blank">📅 06:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بندر یدونه زد ملت نیم متر پریدن
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/18500" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">از سیریک موشک پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/18499" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حملات موشکی/پهپادی سپاه شروع شد و تمام پرواز ها رو هم کنسل کردند
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/18498" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام اعلام کرد تفنگداران دریایی آمریکا از یگان اعزامی یازدهم نیروی دریایی (11th MEU) در
۱۶ ژوئیه
عملیات بازرسی و راستی‌آزمایی (هلی برن)را روی نفتکش
M/T Wen Yao
در دریای عمان انجام دادند. به گفته سنتکام، تاکنون نیروهای آمریکایی در چارچوب اجرای محاصره دریایی علیه ایران،
۳ کشتی تجاری
را که قصد عبور از محاصره را داشتند تغییر مسیر داده‌اند،
۱ کشتی
را به دلیل عدم تبعیت از دستورات از کار انداخته‌اند و
۱ کشتی دیگر
را نیز برای اطمینان از اجرای کامل این محاصره بازرسی کرده‌اند. سنتکام همچنین مدعی شد
تنگه هرمز و آب‌های اطراف آن همچنان برای کشتیرانی آزاد و باز است، به‌جز برای شناورهایی که قصد نقض محاصره دریایی آمریکا علیه ایران را داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 184K · <a href="https://t.me/withyashar/18497" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برق مناطقی از کیش قطع شد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18496" target="_blank">📅 01:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">۷-۸ انفجار رگباری بوشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/18495" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شاهزاده رضا پهلوی در مصاحبه تصویری با شبکه آی24 فرانسه گفت، امروز پس از ۴۷ سال تجربه جمهوری اسلامی، بیش از هر زمان دیگر آشگار شده که بدون تغییر این رژیم، دستیابی به ثباتی پایدار در منطقه ممکن نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/18494" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پدافند تهران درگیر شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/18493" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18492" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سخنگوی سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر 50 هزار نیرو در خاورمیانه داریم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/withyashar/18491" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فارس: حمله به پل خمیر ۶ کشته و زخمی داشته
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/18490" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ حدود ۳ ساعت دیگه صحبت میکنه
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/18489" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBg5NhPo4FrWddp1FlCVoGTzsLsMe1w4LIB1NRxKmpAndZAXCZO5UUQDjmCncAfrHc4wgOmZHf6Ivmjow4BZ5yJAcXoTx36QGEjJNIkZHdJrkF-FSqSmqpVKj9oXRgdQq7nXhYC4X6FDOpKHOnwzGPyGOphp_zOflpsm5NrODVcqltt6ZDkLraHFidYEaPLYEWoRwXNPkE5lNHqnO0eNSXJjBQX91ks4ttehKzFYmbtgc48jhlnhHu1StHK1zWEXIdvYhSFGVQw6LWPsSbX6bO8m_0lbmNszSyyZBO5z3ppkpJKrTqo38Qpj4q01wBlgsg7prbXo1cJX_G8c1VhJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18488" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049770daef.mp4?token=pJBo0-uRwvg9UMLJQ50cOl3qz5acihS5nHcO2ltrzeSrJhIvpHm9Yxwf4L5UqbWAhldcdCYMpTJcSAPAry_N_0r1qbrrktLolBcgk25YFvzJqjNVjal9M-1cE_MNby_YfVPLoZXi-SQ5ynyotWtL4YVoRINVxQvmMbyxiXW2D9SNgyeW5rHjcar32M42Pfj76TnZjoW4RdVWCra5eOV40Gzx58TwoH_hIeY6-SlV71fr1rUqkDVolAovMdb_B3-dTrygKisMFXIa8swcCafldmpjVLriqFeGyc81AspAmF_jPEN9cG3ZVRwqbW7srTxYYO3G0bcpVrnZUE8WJ931dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049770daef.mp4?token=pJBo0-uRwvg9UMLJQ50cOl3qz5acihS5nHcO2ltrzeSrJhIvpHm9Yxwf4L5UqbWAhldcdCYMpTJcSAPAry_N_0r1qbrrktLolBcgk25YFvzJqjNVjal9M-1cE_MNby_YfVPLoZXi-SQ5ynyotWtL4YVoRINVxQvmMbyxiXW2D9SNgyeW5rHjcar32M42Pfj76TnZjoW4RdVWCra5eOV40Gzx58TwoH_hIeY6-SlV71fr1rUqkDVolAovMdb_B3-dTrygKisMFXIa8swcCafldmpjVLriqFeGyc81AspAmF_jPEN9cG3ZVRwqbW7srTxYYO3G0bcpVrnZUE8WJ931dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم زیاد از پهباد شناسایی در اندیمشک نزدیک پایگاه چهارم شکاری
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18487" target="_blank">📅 00:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">حمله آمریکا به یک نقطه در اطراف شهر بستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18486" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">برق مناطقی از کیش قطع شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18485" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاریCBS به نقل از مقام آمریکایی:
دستورالعمل‌های مربوط به حملات آمریکا به‌روزرسانی شده‌اند تا شامل پل‌ها و اهداف ارتباطی و تدارکاتی شود، با هدف افزایش فشار بر ‌رژیم ایران!
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18484" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8n6VipXQYx93QosdgYW31-_Y-APK_5d1LnP3O9-mBXwq0un2SHC52Dy15nUASSGIEbOoEVCUv6SoCGTBIxZeO8ax25NX93ZJJ2ui0elLpBOtyv2NIpZ5XEyNq3y6oOjhOioW5sMDXLsVkmhZUd9TS1_QpQKPD5SiEnrYYEs6lI7a4iy6veNMYjRPFMSNEgqJcyO_McC6M-tzOb6eBbJXBSy_Hjvbbb3Wi-E8btbvWjHJa2ycnCAyJce_6PfARPva8jO1dZkVeqFfaJMKuH-h19A9CPYpHSV2LJjyAKlqrniSMBUXboPCxRNMSnAWsyq8-EuzvGUvoY8eY3G2qKVXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه F35 رادارگریز آمریکا داره فرود اضطراری‌ میکنه
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18483" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">راه آهن بندر عباس رفت رو هوا
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18482" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قشم رو زدن ( گویا فرودگاه)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18481" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شکارچی سخنگوی ارشد نیروهای مسلح : مدیریت تنگه هرمز به قبل از ۹ اسفند بازنخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18480" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صداوسیما:تاکنون دو پل استراتژیک مواصلاتی بندر عباس، شیراز، لار و بندر خمیر بمباران شدند و تخریب شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/18479" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجار سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18478" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یاشار همین الان صدای انفجار بندرعباس کنار پارک جنگلی
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18477" target="_blank">📅 00:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=Ls0zNGAtidsKcE4rlSVw6wqyYq3WeeETknEYgxTzKxUSYYJ_FWa1MsAUIEm-83CujPN4S8H_ky2754JtmaN-DeO5SqYVL6GZHe8oeUc9q6aLbOQd6WZN79S9AYTAQ7qDoHudO1NKg7UJwvonwsr_FeVNxIX3bTupPTfTFQlNHR5rJ_FUH2HQlqVsYqYj9Squf8vO9lCP6oUOCe2C_CgobmSuuWN4PQgGOLDx-2nvLdHZK_mOqBLTUgYDJUjl4DnW6psqw1khiUVfO45L1ZwVqW9_7J9grpEtCF72ltoA6gwOTEew4GUYjhBOFet-KIJL7cK15f6dL12mTQjUBIf3CYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=Ls0zNGAtidsKcE4rlSVw6wqyYq3WeeETknEYgxTzKxUSYYJ_FWa1MsAUIEm-83CujPN4S8H_ky2754JtmaN-DeO5SqYVL6GZHe8oeUc9q6aLbOQd6WZN79S9AYTAQ7qDoHudO1NKg7UJwvonwsr_FeVNxIX3bTupPTfTFQlNHR5rJ_FUH2HQlqVsYqYj9Squf8vO9lCP6oUOCe2C_CgobmSuuWN4PQgGOLDx-2nvLdHZK_mOqBLTUgYDJUjl4DnW6psqw1khiUVfO45L1ZwVqW9_7J9grpEtCF72ltoA6gwOTEew4GUYjhBOFet-KIJL7cK15f6dL12mTQjUBIf3CYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18476" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18475" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18474" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=dus_14YT9_nXdq67cu5JudSgyB5ENrbYOaZlgd1mxeRQ8tVPcI03-qefjYpXc775LBFRYFERdi8sPdX7awsXghCUobTMA94jW_1c_sWXYQWR_gmEDVgX6mU6tF-ZX_Fr3u8jcvGEKEYHe2eDqK-5Y2042G257wP5fkJmt1U2S6sZWy4wyOAhKWpzE4dAwRELpuJFSQ9fdIMmFYdGm4gYolfbL-3X1Y9lP8ugtNobFHeXksyNlbobopriO21mmF40QmWGNF8redwy7_Zh3gGVfp-Rwf4u1tZv_yO37hznAEFDvfYvvGXvIt8Za-pXFNz249Ttnx4-ht98gAab7_1mQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=dus_14YT9_nXdq67cu5JudSgyB5ENrbYOaZlgd1mxeRQ8tVPcI03-qefjYpXc775LBFRYFERdi8sPdX7awsXghCUobTMA94jW_1c_sWXYQWR_gmEDVgX6mU6tF-ZX_Fr3u8jcvGEKEYHe2eDqK-5Y2042G257wP5fkJmt1U2S6sZWy4wyOAhKWpzE4dAwRELpuJFSQ9fdIMmFYdGm4gYolfbL-3X1Y9lP8ugtNobFHeXksyNlbobopriO21mmF40QmWGNF8redwy7_Zh3gGVfp-Rwf4u1tZv_yO37hznAEFDvfYvvGXvIt8Za-pXFNz249Ttnx4-ht98gAab7_1mQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس ۳ تا پل رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18473" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIgfTrFtQtSEnaljvHL1LgncX4nzVCf3juLaEdfWFylAp4cD5sojZjMDs23LS-vOZYnQxO17w6G8zbOF3uZO7wXY4IHqVdBnk575_MAVoFrudg3PAXeSjATIhFpArW7somB3OOWyuyJJgq1MM0ebN64Hek_sqAAjK-pQWfzk_RXuhD2aewLyO75S4HfP6wum8WxaeyY1jIhRANLzH8arus91J2H6hEak-7FB9aCrFp7rHVoXc5POTWXMQfFlQP7-RMC6yVRb8FGbTyw6tS0LLBqgD9xlyHS0YF8s1VAu7O2tAHvHgZfEVTAx46Eqxj-Cy0JgoBG1h88p0KPZ0QWzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ایرانشهر
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18472" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مهر: دقایقی پیش، صدای حدود ۶ انفجار پیاپی در حوالی شهرستان حمیدیه شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18471" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=c4oMFxQb7lgvMQyKVptvc9DIvvHQfqtwvLnt3FeXtyDXqVzu7VgS3FDfi3G5iu85cwHeE9q9vVS7eRKy2LTf_kRc8W_ltZoaRPsdLqaNpRuGLtX6E2moBe9E4c43nOgsFWJLAwdf9O0VP0plCbAhH2bfS3-UVB71EDGeGcg3tPE9wVVascwQSXivBNgLkBjm2XwjsR3I3hrvMI9fFttlsY9XOJYy8q-tE1BYEj94t_QT9ivYYXL1sSqLcRlA9R6jg7aL5-W8VJyYLVnxCwPh8cWKT1G3KsKtDLxRqGJs0bXExIGDdi9XgC1raB8S-cnnB3oLk4tr8-yrC73-xNpYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=c4oMFxQb7lgvMQyKVptvc9DIvvHQfqtwvLnt3FeXtyDXqVzu7VgS3FDfi3G5iu85cwHeE9q9vVS7eRKy2LTf_kRc8W_ltZoaRPsdLqaNpRuGLtX6E2moBe9E4c43nOgsFWJLAwdf9O0VP0plCbAhH2bfS3-UVB71EDGeGcg3tPE9wVVascwQSXivBNgLkBjm2XwjsR3I3hrvMI9fFttlsY9XOJYy8q-tE1BYEj94t_QT9ivYYXL1sSqLcRlA9R6jg7aL5-W8VJyYLVnxCwPh8cWKT1G3KsKtDLxRqGJs0bXExIGDdi9XgC1raB8S-cnnB3oLk4tr8-yrC73-xNpYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18470" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18469" target="_blank">📅 23:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18468" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
