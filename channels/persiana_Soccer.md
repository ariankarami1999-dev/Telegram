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
<img src="https://cdn4.telesco.pe/file/Lsv8vrJmWs7dCo4aRLyxfGyVD5RW8iMEp4i_borQ2Ow2SZBPiVGjf1v7ohb_dH81uHeMt0nH5ED9BoHADVlz68eo6Zdn5-sTrmRgUZ5qwQSn8iN5Qo0rxCaVYWC2Ass1mlWo1wAV_on2AE9gpmdl0KhtnjZQZBQUeKOSSTfAk_cTenZLT-Lu7BwfLxYO_heU9D0s6xt_EGcVSTuZIdWJyxhpSuLZrMFB1_bSpQBf5sMeODEfQCoKW7OphKUkzuy4kyCL58NJAonai93wkfIp1RAayTmb-3re09CV3uprefRQHlI2ZP-yJONn1KZdkmJXSXM0NK6EXKWhuXBFJajCqw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 22:28:18</div>
<hr>

<div class="tg-post" id="msg-22844">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=YiPx2i_EsV2LYhIGb2SMc5c9GM9l-nEm2rfVCujbJewgwlNwhBbgcaMM0dlIBxEdjv4JHs-76u3j9FU9xJx6HNwgbMS9tx77Yg4OWDUy1nAxU0Tpt1rhH0GuwyOV5DXdxioZ49gXpc5eFszWOAd6XKitDGYt2IUGxvS3WC_w5ysNkNuIJJoVqv9lLWcM8N-lz0-RZ8w-9iN_xzrKmS4lnZS9bSRooKcQ5_9dRhwCKNJmNC2LxSWPLUPQEuFTfhJzxcmvtSD4BxaWP52C-8SdnhSJCzUiWhOonsrym2POEcunFyotgtR-2ooR7hJCxR8KOCEymNEeJ7H9PzFQfW-OwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080305bcc8.mp4?token=YiPx2i_EsV2LYhIGb2SMc5c9GM9l-nEm2rfVCujbJewgwlNwhBbgcaMM0dlIBxEdjv4JHs-76u3j9FU9xJx6HNwgbMS9tx77Yg4OWDUy1nAxU0Tpt1rhH0GuwyOV5DXdxioZ49gXpc5eFszWOAd6XKitDGYt2IUGxvS3WC_w5ysNkNuIJJoVqv9lLWcM8N-lz0-RZ8w-9iN_xzrKmS4lnZS9bSRooKcQ5_9dRhwCKNJmNC2LxSWPLUPQEuFTfhJzxcmvtSD4BxaWP52C-8SdnhSJCzUiWhOonsrym2POEcunFyotgtR-2ooR7hJCxR8KOCEymNEeJ7H9PzFQfW-OwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ویدیویی‌از قهرمانی تیم زهراگونش در سوپرلیگ ترکیه؛ زهرا گونش بهترین بازیکن فصل لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/persiana_Soccer/22844" target="_blank">📅 22:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22843">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=vsEZ5JJxbjesoFIKxjzJm-j4oX9WGSUCLuwYuld89og4dpq3uX_G_Wjy3Th6ZzMgcOv0gwyJSmEsQanlSkCJVVKd64uhPoEbzJ7H3ECMWnWksnlUwhfiTtXmPbdcn3qpPn68JZQLwmfUJMLrEddL7LkpsQVGxUgGhFsPgMH1vF9ovIrv6d780UXfjk6L2JV9_Cyry6AELyVoN3uf8oABZ_5ou0-IWRVBtoUHrin6e78VnUGKoVNsjS_eyaynNNF1_3LvSeLWPA2FU5uhwffsf4J9JQ-6fYBxu2tZhWE02xFNCmHoGGthS85SzWuS3Y80S0FbEGTCdHarG5Dg-ABH516onWNlqaRPDlWwbLktUxfvZgkvYEXHDHPom6AYMvhd4DMIUfIGsvBx3MG1Rswv30xMOj8rtdPF0kWpcWpxFwq2-0FrkxVZDZoO_XM7t5Ik8ms4JK9APfwhpGSp3tkgd8nBM3m4oqDsPqRq7C9VFfn81lVPyloUwKbpm3b9SHARWVMpQ_LDH_Pu5rJIfhTXvKDnSliAFlJCbdlhW2OL2oF-5NZtkFe54ynfoo1-_2XLzPYLPKcyCwYdthSdDNSDMwelw259U94CQM4nnvzVehtiN9j0x8DTLZ94jIufkm1VPaU3MSInj1EfCVQFdYjMU1atMy4xxLA0qf-1ebsy04I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63cbb26f8b.mp4?token=vsEZ5JJxbjesoFIKxjzJm-j4oX9WGSUCLuwYuld89og4dpq3uX_G_Wjy3Th6ZzMgcOv0gwyJSmEsQanlSkCJVVKd64uhPoEbzJ7H3ECMWnWksnlUwhfiTtXmPbdcn3qpPn68JZQLwmfUJMLrEddL7LkpsQVGxUgGhFsPgMH1vF9ovIrv6d780UXfjk6L2JV9_Cyry6AELyVoN3uf8oABZ_5ou0-IWRVBtoUHrin6e78VnUGKoVNsjS_eyaynNNF1_3LvSeLWPA2FU5uhwffsf4J9JQ-6fYBxu2tZhWE02xFNCmHoGGthS85SzWuS3Y80S0FbEGTCdHarG5Dg-ABH516onWNlqaRPDlWwbLktUxfvZgkvYEXHDHPom6AYMvhd4DMIUfIGsvBx3MG1Rswv30xMOj8rtdPF0kWpcWpxFwq2-0FrkxVZDZoO_XM7t5Ik8ms4JK9APfwhpGSp3tkgd8nBM3m4oqDsPqRq7C9VFfn81lVPyloUwKbpm3b9SHARWVMpQ_LDH_Pu5rJIfhTXvKDnSliAFlJCbdlhW2OL2oF-5NZtkFe54ynfoo1-_2XLzPYLPKcyCwYdthSdDNSDMwelw259U94CQM4nnvzVehtiN9j0x8DTLZ94jIufkm1VPaU3MSInj1EfCVQFdYjMU1atMy4xxLA0qf-1ebsy04I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
کاشته‌های‌دیدنی رونالدو در تمرین امروز تیم ملی پرتغال در استانه شروع رقابت‌های جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/persiana_Soccer/22843" target="_blank">📅 22:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22842">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgNy45Dj87-erwcvj6Y-T5cWk31eheNP_b2YqseHYm9ujbT2vCDw33I5d1PvGT4uCiVNbdOQ9j3O6jKgdTSyj9Hmyrw36muEbhiFOdSDZzJSXBMsT_CRJlKIFNEpQ6ufAoSMQS91Amle5X3viZTXuPD3GgGFgaF9akk8Clr0-nVb9UkkacvkuqjfOjZ3o7UIKLi6xs_m-KmK-jHXVr9pouSGq4KTZeakWY77I0EbbotTiLdRgDQgQNw1g-giFfdZ5YOE6ugV3oE40sd2A8d73l8qbcg67CSKYh1fanSbnvRb8DwP3X-IHKYad1qIJHBOy5S_amA8EN3X5NsdU2rt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22842" target="_blank">📅 21:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22841">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W67U8lsoLHPmnGnEqAIWpBGKaOHs-NhndjnPDyrnw3e8yhhYMdcyAWrrpW62aGFVnP8MGEFrHIA4JK_EtRP0VTV788eH_NCciCjf2XHSlQfJaj0FgB83DHgQAi9j9SbHnr3_60fgUPv1bAYlrbigaSYiV_OtMdM_1912iwm4_kR1A-NxZqW0uCWu_l71QjjrqEg4qilwVOpDBMg8by8B-_h0MOYeR4VyYWtB8sz43H_Eu9jBITaQdJNG9RzCmO-WqtB-MkwNPeJBhJLLE4ZHTiI0ZtadYB-YnVD8nAwlr9MrW--fCGOEYK2gEV3zDc7gi3sTzFC35_X7YRtT010gQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22841" target="_blank">📅 20:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22840">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=HqsSD4RTQO2D2XkzRtmc2FIDXqot6JVq9qW2bb_u9l6cF4mhQRqspI991hRinKV77Gxji2UrF4XABa9spcfh8zXQnUVpsq7p95027GwHuKnvay6ziSabPE8eKBegKDI5tLabMwPwG2njpxsyW82zywH0MpCMwRup32T9TsuG_BUgPoDpfkj8lAwpQvY-q_BoBHP79BKBSGk86TIWbu9SVX2SPTaxxL9PebMVy_NoCcIWC2zrv_MCLk2pjt693WB_NdSCpkEULgfG-9WAQ8VoOaUiyYUvbp0Bql31xgW3jNN7AP646dTmj4LHWLGERXBFqMA0rOIH4Ti2Y8M3oCZqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c01b9049b.mp4?token=HqsSD4RTQO2D2XkzRtmc2FIDXqot6JVq9qW2bb_u9l6cF4mhQRqspI991hRinKV77Gxji2UrF4XABa9spcfh8zXQnUVpsq7p95027GwHuKnvay6ziSabPE8eKBegKDI5tLabMwPwG2njpxsyW82zywH0MpCMwRup32T9TsuG_BUgPoDpfkj8lAwpQvY-q_BoBHP79BKBSGk86TIWbu9SVX2SPTaxxL9PebMVy_NoCcIWC2zrv_MCLk2pjt693WB_NdSCpkEULgfG-9WAQ8VoOaUiyYUvbp0Bql31xgW3jNN7AP646dTmj4LHWLGERXBFqMA0rOIH4Ti2Y8M3oCZqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
@Persiana_Soccer
| Out Of Context</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22840" target="_blank">📅 20:53 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22839">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9U_06HzaKfbF-jPj1fOEKxIuXGivRBEYRVVMg4ugNSmp-0ba9hVOw0Ze9l0yYmL_io5h9xSYmsD8hjQWZ61LKkX_yjNA28WSCZuab9y3nxT6AKFbqOiTpxRLh_DZhCIemIExqGmh5q1o8s0Wokiak9ETxH8eamuugEw-LXCwpBndY-bQuc57KgcWwoC2o8WQXjg1Zui_06cmN9R9yva7xYrTQTsJl1fPAtHXECoLQrpqNnxeaBi-XWyofUzBXo8Ocj37pO6Nf86jTH4UoEo5vw3TVIInpqT1rfd0btdEL0ZLxksO7HkHQvJdOuZIriNPducqvYDFA-yGWKX6-1zhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
#نقل‌وانتقالات|ادعای اسپورت: آرن اسلات بعداز بر کناری از تیم لیورپول به گزینه اصلی هدایت باشگاه آث میلان تبدیل شده و مذاکرات بین این سر مربی و سران روسونری بزودی شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/22839" target="_blank">📅 19:38 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22838">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BatfYXnhMi-JPzR743Hxk4PHT92oglrP_CCHJHIU0R0LNfE2XxuEwAVGdel6I3BhMreZKH9V-4StnbXkZdI2NwwZ4hatadMmbHHCt_qBTRbRq6yLU08PKxqzcMpQx7QxRcFO1drNugMGPRd1x6bPh-Ntm9tzsKVQKIKhWVT9xC7NNFwol-ZFj5GUiRx3vv3OpxcRHghQT2b0ajWJ9cPWPmg_ndTWrJt3lo74Ew-Zmo33vM79udINJXOXW4SKsXyb5S_nPsaph92T0WGuZIYmDcR7dpQ80KCca4Z9Zb6mpl75o4w_gLEN__AYvVLdlZb8xRcqRkQdyhNIsjhvUiOgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/22838" target="_blank">📅 19:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22836">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1CxXafY90W-N-U6R5jwd5-Q0irGmLPceZHsQ9QAVMlPyO9xFRaLc6hizP9qzyn4h47StXYqi2k88EcVQvLlr2jowYuu0XeWcXwjGrwu0MzXZD6Ynvz1DG_HsDEG0prjvxD71OPwht5HQ8vTipTfIPrLdLkQd4-a1co6aguJ4W6a5Cpq_TEm-SyYYPZqSXBMr1WZdYhMlBK4eRDllMunCTfsV4mzXDEmrX0846dgkF_7U3Z793yuNnIFhLFuYltRqY3DTZ1B3POoVXuZnm2jgIBA-SLHwn9tAef_mitosLejyoPA7Nkpd5jZqafpJtAigxJRgjqWRkbPCC9eYCLiGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a220e76f7.mp4?token=VeDfgVLQwMNzSbSSa2lUPwsEW_eHGhpERZDCfr7Kh1HD5C2IplZ6Acd941eMlu1v52ZA2LY6NpHUW_q1IJ1We3hv8b4f5xzPJAAYmHCjzlvtY7wAfWt3bCy_e6ISeCmb3w1A0I-EmHetimONr_98u6jZECm1xoyL1IirvpHuXXQZdsjo5UQ2hWFoDj52NECTyFDEV7MaES7IGZgpuzjWPj3_jFs9vYcWH7JESwjPkVDtV5Qv-8ohogJWusELGGKuEXRwOQaLDZkz2E3q6deEd3Lz9_IcmXzoITr3X2iJAJK_fsdEZZcx_SEBeHcz8tUFQP3QOq4f-UhVpvGAFwUP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارلینگ هالند جدیدا تکثیر شده؛ نسخه هالند جونیور، نسخه هالند پیر، نسخه هالند دختر:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22836" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22835">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_3AKvuSEttRpiW6ILxrhbz_tRQTdoAxFgqq9YUQh2_a3g_Uw8jHR2eKzbdpLgMFqp4cMJ4gg7kaNDWip3KEu31CN3Szgx_FOdBDauF4R4Man1FHlSWZbd5Jf4CqivvimKc-Cs71xqg1G1PxwCEEgMXn47BltbV-KOj1gmSVfikSdgIJGJQOX7zTTNqzIbek29XZ4RDT_LcT2DY4yAMuduxukM-0zU9T4vFfa9G5ezK2J5KBfEEGzDIc3ByXlG0FKcfjJTRSnno6FSj0DRQzl0vR_YDSjdeV8CqNkpGooEZiH1jSmylv21H1D5OWAXncyjjb5CU_JNHrz0rbiFY0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/22835" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22834">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYQR5m36ZCyUzi1CZ-jr3PnJvIxuj2IBbkZkFeL7tEGekPECUxNmXAJLvV1QlX0ZVPgSNKjibqx3Lx2PjUN7xWxsxDZEAfCRsDpK3IsBKR2Uk4xjy1ymckdlU8rEbPcrcubRsQ6oldmYsf4i2Hv6XKPf17V0nIQESDXn4830WWpqVssyWnHqBN_2LMcYxJXtTVgNmoR02HZpmLs5cru6aTJu6hDHSNbgXQo_RcogoIluVmyROhG3Op0t58BuQ2p2tacArh8Fp0KiD4q7cGe4cZqpq54l7YEl84hSl2YciIhAQl08qmvBdRYhLuqW1DKe9R6oOptT0qYzDUxvYdP7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
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
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
15
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/22834" target="_blank">📅 19:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22833">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijoAa2n8dEFS2RLO7ClDU_n-ozNwtNhM6f4L1BYpey50RqkbztEmdiPGbt00sk4FELiJsD9WL5IJ8Mn2ijxXVTFZ6-ysdjIU8ckDY5f59dsy-l3ZmQ5NdMC6ppV96delNrZIiqCmkIW4l9xBcQm8X2JHyCzzhS6jMcytuLrWS3f7OacpcAxhuvCrmhViynqjZOzw2Oxg_SdpUsmSQ69N4ZEqQCRmcHdENzw-fO_JWYuPqwq1IvPxOy2_REvVz9lsstoJMr15z7ff2f_GxdaKjUEhswE_APDPMCpbd-WIZXjcfcDrqK-V-1DiyyO_F4jINXdAVodXTPzNj1XXAmDjIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا محمد دستیار تارتار در گل‌گهر: باشگاه پرسپولیس باتارتارمذاکره‌کرده واگر اوسمار برنگردد تارتار سرمربی می‌شود! او می‌تواند تیم پرسپولیس راقهرمان کند! باید چه کند تا سرمربی شود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22833" target="_blank">📅 18:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22832">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE3hFsPmyGp-nfrFVHJ8n1rHIqo6g5bq6nC_fGqJPWcdhpFIlN_ZBrO9aDB9ufAAAIlzS2U52y8DgIcftcxYn4UWB-qFg_231dj1wKNo7D-L4Rtd03nysVukYq9Thg2oVVJmiqzvyY_l0RPXI6uqP-YrkwkzZ1gTuqiBPoGjlm547Nju3Cc7gBzvH5xJBetNWN7qS5ufSM_kcl9cL6-yr8eDwbGpFiSKCZo19BFx-L3SNFIpJyrd4g5NuyZIhcyUsPlpy-HwQTqemTPiKc2ZPhclnztLyCNuZXQFGsygy5XlbZ0GtcsUsrgSG7i8RqSCV8OnKCx6YgePPpWfjm0xGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رومانو هم‌تاییدکرد؛ پرز میخواد به هرشکلی که شده مایکل اولیسه رو تو این پنجره به رئال مادرید بیاره. اولیسه شماره 11 جدید رئال خواهد بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22832" target="_blank">📅 17:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22831">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG9Wd7ulGCBm7wIvWZkHPQabOhkIizA7TfoSZatjXW2IV8C9x-941WKFTUldX-lDBwrP9XTXrTus3XdGIPnkEgx3YYtUXpnq3BIbHdwa-BKUOUTOtEzuBcr6pZGmLJAsJ7u1vz1xbbCzlnpOKvw5ZfT5zYVR_3Wl1XXlFennYza-dfbXQdmutKT_Jai5XRhA7LzZYM0tOzbl-kX3UH_xjJJuiB1ijZiIZrRMCWoIpexvWGEcnClAhw2eGUqsPZ96nvQ3UXxgeTdzQKsdTGlV1FGJK-YjvIkP2n2wkoT4LsMcYoWIPSLKgwEPXdLLyM_1dTRgy3ZFVNOcbizFSRfliQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛‌خوزه‌فلیکس‌دیاز:طبق اطلاعاتی که بدست آورد مطمئن‌شدم‌که‌منظور فلورنتینو پرز همون مایکل اولیسه وینگر فرانسوی‌بایرن‌مونیخه و روز سه شنبه پیش رو آفر 150 میلیون یورویی خود را تقدیم سران باشگاه بایرن مونیخ خواهد کرد. خودِ اولیسه هم در جریانه که پرز میخواد…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22831" target="_blank">📅 17:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22830">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNxtcBYlq-ELsdT731GzdXyPSIZe8Sc1CToVICoc9RDusXKIR-LDgV6OAm_ZBTnJQuGgKynmh9zg7gd8vie9ZdzzMN--wuIpMvNwA9LHTWoQCFsD0Rxw_pRa3WJV8cvuQvRqGE1Vl46IhQunyAh8Va-YExS80aVUwY_Fkk67LiKQwHOJE_0QVlrGwan7aWji572uIUMthCg4mvD6_RhPvyNY50nmv1jbF-tQYnxarLXyI9Xq9OGyEQaObeljgkZ4qDtC7Zzn8IertpuxCwsEp8F6lWkbg8zHHP4-HRIQ1AGcwM3DdnT4ZLJJBqPfGXxELo-1IMqXI6TQl88wXyNfcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خوزه فلیکس دیاز: علی رغم تکذیبیه شب‌گذشته فلورنتینو پرز؛ باشگاه رئال مادرید بشدت علاقمند به پیوستن مایکل اولیسه به این تیم است و قطعا در این تابستان برای جذبش تلاش خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/22830" target="_blank">📅 17:05 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22829">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/976cd07773.mp4?token=UnB11S1O74pUpV2B_0zqC3MS2DqBt24wWSy9KgbVBMJxz11eNIpMrjGldFGUn3QQ3q8HtWe3ozaOnC-6f_9peQ2ptSdE5HWW6HXi06dTrvBRwr1yBMoHbWFTWrql4_GXhcm-d94jHBs8jCl6XSjqMpxuYvi9UKDSpGAu22G7xxlvlKjuf1AvuIW3xQM9ly0gzyi7TbMAGNHl87WjQC1x89L82ywzZbsnt4ef8s957Ml_tBFYfCgOy-ifxZ-7GW1Onwr9JE6M8rpRODLTW1vJOSSl6eGVPHzN4wNmto5vuRQY9ccipiDuTlThZP8TwmyJeSVAyZVcuGAVuhrJQ_drNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین‌ابوطالب‌به‌تیم قلعه نویی:
شک نکنید این تیم قلعه نویی تا فینال جام جهانی میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22829" target="_blank">📅 16:46 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22828">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6qkZaSKlI38vCC_C0TKps5yb5OqgxMFAuoSKzRXm2BUVE5r9GBuxMV9zv28wyHIqFQqLc85dgwjQa-7jtlJLHExiAg9KuDeCbY8J0GXWoooNIpcR3yNYT6fqB0I7DiSa-0g1e4-cznephyYGYwwOSbPqpdn9o2EDHYw_sRN-eqDi0DfKMDIpADcO9rUa75DTveIMnz1JEEbBppsRPyOPqLYdEiWPAUdfCA_SwB_vLpxo01f2hG2Y__sSYDivhkrBb3lvHEqVfSb3NR40wSoJ7cshi5aVUc_kp_qoNUdU9jkPjQY320yQPSkY2qo6EQMBF-kOveOmgyF4Q1B9JPd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/22828" target="_blank">📅 16:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22827">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBQoog96Hjsl6IhJqKM6bQ2Mw_zS_R9KeNpr4bMokawatBgHNaCBQ4Wnnloo5-9tgmBGQ_w32Ihw6RawqCCrqGPOy3l9D9mxyG5DWugo804FsiyaHcqa01Wa-dDjV-y1rEoUmM5bZHpz0avaPZWeYLmQdgC4hX0IrWj-vddptnUNg8DO3EJD3Ij8aX-MkKhxa4WpA--03I4080irtaSEdae_VlC7udZflu0vspqvx3Se6lIPzqRya2I0IfiLxVNGVINKlGBdRhdc55d7BSylyswEyA9qm7Mzbq79JD5q87T3BdQKTwDm3nEUve3wtIi2IhnEo2rLR-ru_FfvAcugzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22827" target="_blank">📅 16:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22826">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=qicaGmDZe6lQdRpwaD_Co10vFRYdUAWYpwHsLMvRA_QYHi0oAzudJQUtLBCFexi5IQi-IZSldQUE6DT-_Shx0dol9ZWzdzW5h13j3WNz0nBEuJmbu5JahIMrrI9cQu2zcmCT4VZIFrQKkrLdq7C9KBnHARM-VtIWOcNs3ETz6K5jtiuUh0Ns2L-jh3Tv8PwhCvtxO0iLpLToTwAUKqQcK7SPoD1ROBwDQuL58dAf8Qrt1LTr8E2_0PctWgeK-hgBMNZsHkrty1Oj5rQ-eXOZrmhZMeXMrDEcH3bbrPftcsn6v8pPFllGYCukme9xu0TLNmM8XPdWA0jOFrFn-QHPoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7414e31a83.mp4?token=qicaGmDZe6lQdRpwaD_Co10vFRYdUAWYpwHsLMvRA_QYHi0oAzudJQUtLBCFexi5IQi-IZSldQUE6DT-_Shx0dol9ZWzdzW5h13j3WNz0nBEuJmbu5JahIMrrI9cQu2zcmCT4VZIFrQKkrLdq7C9KBnHARM-VtIWOcNs3ETz6K5jtiuUh0Ns2L-jh3Tv8PwhCvtxO0iLpLToTwAUKqQcK7SPoD1ROBwDQuL58dAf8Qrt1LTr8E2_0PctWgeK-hgBMNZsHkrty1Oj5rQ-eXOZrmhZMeXMrDEcH3bbrPftcsn6v8pPFllGYCukme9xu0TLNmM8XPdWA0jOFrFn-QHPoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22826" target="_blank">📅 16:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22825">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLkW_Ku4GGJRCN8ObjzFcJagdBOycFc8s-RPilrEotu-sInHI4CBH98gIQ42lEDO3mFJ1fvqx8s3dUE11yxzfWXfEIQjJj3vpQZKl2-aKLujT7mBf6k074-gVpsPPbUVg84XY__8X0I3UlJhTx8vV1TzjtCdCQCv8cXUBubB-Hz6Coa8NbOtjXOwDg3recsVkiFNoUT9-zZfki72Ssnl2wMuAHEQ-VbYvzH6euc6zNwTwiCLluTMCNhlfuMgW2ox-oQN4NmMzWZGfRaW1aWKGG4YUvzhO2sxw1PGkpP_FXzZK4J46GceGWAXbNyvaXpQc6dZauNJkf3MjJDZw9wlNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل هفته سوم رقابت‌های جام جهانی؛ از روز 3 تیرماه هفته سوم شروع میشه تا 7 تیرماه‌‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22825" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22824">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSXqovbSPHInvyr0AbfW6nlR9D5p9XWFrAB5TmHm84aOtZ2maA-xXks00vmwqqElGlkpk7V-CPkKZfL1udySzunGW0HktjbxOM0Tq5qwr86Xfg8BjaNS7g3I89onH3Gib-GveQYPBlZQYj8hjwkxOhVftX8Q3ywsO8vAmO3gEIK7dhZTJCOji9c-snGuI_RssdqxZSBZCyBF4hVA8fHbIZR6Mcdwq97IQ5I1USO50FSQjUFPH1nwb7QC1GZ-uy41NUDACO7_LwAxB8NnewtiTN4NtfkyhXibnOgMvUBB3aVKgS_noLhiyjSghXL2XfPhDwmkQnEiZUlgrR17LZFx9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ نشریه‌ کوپه: رابطه فلورنتینو پرز و خورخه مندس ایجنت فوق‌ ستاره‌ها خوب شده و مندس به پرز گفته هر بازیکنی بخوای رو باشگاهش متقاعد میکنم. ایجنت ویتینا و نوس همین مندسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22824" target="_blank">📅 15:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22823">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUlTqLkCFsKe39hHDOGyFmLD-WvmYlYJoQaTxNehfrEhM9YsDlD3OAjNlxI4aZOxQZfJZpY51OKkb_iXNXKeXXkqe-4_HprEgVLAm7odJo3tIbJKuZqqokMJXxSXR2Mpt5gt6N0n__x9ANeKTHuB7fVaKnIca8KZut4FUXZvZpj-XNn1Ehk2MKCMMNNcjh3wJMbERKTImZtSCKAKjJ2DOawE_dtNXCF17P5G4c1FRH_gbP-SewmrPE4PqLJfGJBORLNntSHwHQVwqf8ljYTgqdt2HlVWLXGRxxGaz9amUfi9ukDutqk9bPVhvyF4aGvi-lA77sAa2w45swTVQdHfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22823" target="_blank">📅 14:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22822">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoxIbxpO63KOHbQ1lBw1gXafGYDzXfL8l7z-UyTH2ahSeoVBmy7k_uoaUfIauBQe3yYE_9c40xeVsj2Hhk33eAHf4PNVeAIUcbNOyhsBU3QO1i_TGDwsU1OZe1nR0XDEe0IOe8yDjVXFKZCS8IXgsPzbs_x0iE2srNARVrfc5hiyuPwGTahf2ob9yZecx9klIST79SdGt2YMGrBxzmZp0KskHWeIIisvIbNxUL89SVpaYBjiWUcJyhlfIY1dbUlKTo0K22XIuYV0-JfOb_hE3j9NKR2qka8gWY8jqm5qIurZ8NHInXKyu03NKdn_F2cLxCC4lwqSG3jyk4Dznh3svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/22822" target="_blank">📅 14:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22821">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVGcYPkLYw4OJiSfSr4_1jNl4rJ6_VvSksr_zTnYxj7MRr46g7x9SwZyd4Ei_kAGWeBHQ33Zooaui195LH0jKnnSThtPj3NL4CA-ZxG4pMyNzZWdG_PahNfKiIx5yLbC5927v1Ork76odKAdcM7HTLX5N5QTcjhQfypy1gXPrEsCWiqmRQSJIqxT-ORyFc1TngtKh3hWn-c49eBFDtvtawij-ForHERG2IrTJkPRB_13Rf9brKxzHV-9rNGDtNczMsXHVIHFJ8we7xlsczLKoU1EHl5p94Q6PYMMRLb_1opyJX_MvV0TmR2cJ4faRyoyq1lJOrt67bfEhlArcJSxHihk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b9b84db0.mp4?token=F-F3CSn82dIf-7ZPFp27-gJIOsqzRXhRsgCFlEIXzXRcP-V6D9-PgWwY5vlsz3BxQ4dSh_e8MCHFiBEj-ofQq3CVWUVebLrMtVQv9JhgG2fxE7IBj7fHK4Wabu-3UEfCPtjnv-iM5XLmzMzRiHfy8lb4tDxq8wiHW9l_BYPSxpz_aoXQm7J_0rhE-U57Zif5TFC7rXV2sjouIzc-mtO6E0LA0UmV8uq7HBbGppzEjGtuWj-FT1M5vf9zyyoXrjC6FB424aDG3fyKeMfX-60BwFoehIcQtOj0CRlG2BjXQQfav60haSOyM5mtD4sUKAdZsMXw2WauX7S0P1gLgKHZVGcYPkLYw4OJiSfSr4_1jNl4rJ6_VvSksr_zTnYxj7MRr46g7x9SwZyd4Ei_kAGWeBHQ33Zooaui195LH0jKnnSThtPj3NL4CA-ZxG4pMyNzZWdG_PahNfKiIx5yLbC5927v1Ork76odKAdcM7HTLX5N5QTcjhQfypy1gXPrEsCWiqmRQSJIqxT-ORyFc1TngtKh3hWn-c49eBFDtvtawij-ForHERG2IrTJkPRB_13Rf9brKxzHV-9rNGDtNczMsXHVIHFJ8we7xlsczLKoU1EHl5p94Q6PYMMRLb_1opyJX_MvV0TmR2cJ4faRyoyq1lJOrt67bfEhlArcJSxHihk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لحظاتی‌از عملکرد خیره‌کننده لامین یامال ستاره 18 ساله بارسلونا در رقابت‌های فصل گذشته لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22821" target="_blank">📅 14:07 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22820">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhCfUhG8IoNHkSTziJvhAVr6rCQjBQeRZ29bQJlDa00btF49NO9x_XKCswhFybbA1V6YX7Src6eWZ0h3iTI06OhTTSG10-UCClFa_U6Q2jFDsgXoayr9EEv6KRHoUj_ltSzLBUgoxhojU6BZ0cTEm6g5Q1p_YEGP7LNgvc-4fyz4XSKyoe2ot22gbvE0HfSEhrPmNfm4-JcuyixGk6rGgPScOneQSThrF8qGyNG7lOqq8RG8nmC-dsNKz3EbL-2svsFiG-DV5IpUyXr0K7mtwwkVGNYez0pZkGaz0lNyr_fPZiXBXbyOd3twcP_DJ-hHp_2LR2DT60TeEH50U6LqrzLo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d7daef98.mp4?token=Iqao0qYk_lB8jhxWgssawzvqw3OD24F1XAQw7Z0GGr5ZGnwmx071T5TNfEBJOgJmYhfTRjHFWTkWGqhueMT1e9tpEn2mKR3a07aszY2NzGbfYXcx5SolVFwiVpbzC-JG6N2yiUKbQVncyEv5Hvbgv3AU2HRal3Yo0VTNNaSRj9moFOAAu3C8d8E6mRKkOG4dIoPl_d54e3Qp78IKBnuH5vFvqujPGL2SRABeEEAuxVxdcq1-EqtfpKJKko7dAqp2uBQquOEmOVnHI2lbFvUWiyIDKHlNqQ_5o8ZAZYtbK7loRQNiLmZMpwf0BSnYjRR78qEdXJd36i5_VkfXL8MfhCfUhG8IoNHkSTziJvhAVr6rCQjBQeRZ29bQJlDa00btF49NO9x_XKCswhFybbA1V6YX7Src6eWZ0h3iTI06OhTTSG10-UCClFa_U6Q2jFDsgXoayr9EEv6KRHoUj_ltSzLBUgoxhojU6BZ0cTEm6g5Q1p_YEGP7LNgvc-4fyz4XSKyoe2ot22gbvE0HfSEhrPmNfm4-JcuyixGk6rGgPScOneQSThrF8qGyNG7lOqq8RG8nmC-dsNKz3EbL-2svsFiG-DV5IpUyXr0K7mtwwkVGNYez0pZkGaz0lNyr_fPZiXBXbyOd3twcP_DJ-hHp_2LR2DT60TeEH50U6LqrzLo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
من خرافاتی نیستم ولی شما این بازی ۲ سال پیش پاری سن ژرمن با حضور امباپه مقابل دورتموند رو ببینید؛ واقعا انگار طلسم شده بنده خدا
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22820" target="_blank">📅 13:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22819">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De2mtBnfyMfNQLiGlWaVT79aF68AUyabTFFsuXIPJn_Z49JHJjUG9bgl-N2WKx-tnPt9Ri52c3nVGgPyXtCG6lbEElj1TMPD9nqzy0WOM7C4VRR5k3yvkEHuEUO6liELh6HFFDv42T1090u9clSvXDBiUzyUahhQYLXe-sj00LwWl9zSU272uyXtqgr6OFul1isfO-KyBU_5KO9BxmbubK5cemt4Wdc-jw8GSKIln3fwj5-_t9Z1ohDb4FXXkRPW7q62fkWsT2gozgib_mRqop9s-7MTDD0U-y2m9OiBO7oObLfbbF2ScxGdH0fxRXaKX61nzMzUNrYRcetXhdPDhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
#تکمیلی؛ باشگاه پیکان قصد داره درصورت توافق‌ مالی باباشگاه‌روبین‌کازان، رضایت نامه کسری طاهری مهاجم19ساله و گلزن این‌باشگاه رو بگیره و درتابستان سال آینده با رقم بیشتری به سایر تیم‌های لیگ‌برتری‌بفروشه. رقم‌فعلی‌رضایت‌نامه کسری 800 هزار یورو از سوی باشگاه…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/22819" target="_blank">📅 13:27 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22818">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqYTJPAxU5Fa2OgKr1OEH79EFQyTaiZny2Y8nnds1ETIvMCEWTcmec6iZOTPR_x-s0oTcvL99O0dXuDp0tlwLnk5BUHl0MS7-HrfkkyfpLVZpw8SAZICsfTQRiW5BMoxKp2UjiyNjg7QOV8sCX-Wz5qJwejjJZ_uwJlCKnCKc6nid8p8LtMGsf984-ALrKdRXe32D8NzC7qHntUBohX7oEhdSv5dmfco1pyRvucNSkTxV-2-WPeWllu0iQygdPa6fWEAi-qws-TZtlrVV42lkkRNhTqiEzlrjxsFnKwvD42mdcDo0qBzCBwTnV7zrOGaD-B4xTttuTnBnlW4aTTOlHKU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7913f58d6f.mp4?token=f_r-ZgaFZ_pYVDXOrndfkAa0X7MkXYQDerWnh_0lLSk06pCutAWua6fhWt1KbWCS55w8QEGqCLXFEQVzaJwKHBDBEYsCJpS8OKP7F0PEJjYCeFlDnl6hm14QGdmQXFKk2N9zoBLSJyzq0FCjTkxrxWuxoNiIyESctF1-GbjkGONOpyVgiBu5Xm4esa78wb89-CcVsh1Xh_lz5qAI4sPPc9RSM6NWO6RTI8ypxiQ7aN5rBv4eVxtB9RTpg7-vl2Nlti9fn1IchF4YPMyEZRGcoLPob-SZ7QDa3o-C4hcLDCJkYHq2X-IbRJwwXBOZFH7Sw-6f5MWIbJ8TnYpgAuQdqYTJPAxU5Fa2OgKr1OEH79EFQyTaiZny2Y8nnds1ETIvMCEWTcmec6iZOTPR_x-s0oTcvL99O0dXuDp0tlwLnk5BUHl0MS7-HrfkkyfpLVZpw8SAZICsfTQRiW5BMoxKp2UjiyNjg7QOV8sCX-Wz5qJwejjJZ_uwJlCKnCKc6nid8p8LtMGsf984-ALrKdRXe32D8NzC7qHntUBohX7oEhdSv5dmfco1pyRvucNSkTxV-2-WPeWllu0iQygdPa6fWEAi-qws-TZtlrVV42lkkRNhTqiEzlrjxsFnKwvD42mdcDo0qBzCBwTnV7zrOGaD-B4xTttuTnBnlW4aTTOlHKU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازلحظات خاص و بامزه پپ گواردیولا سرمربی سابق بارسا، بایرن‌مونیخ و منچسترسیتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22818" target="_blank">📅 13:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22817">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMeyQS_fRK_AX5sKJQ51qWl--sTK6BrVMOfs3eV2wz3J1Kn7s_yN8VUA17n-WctwFF3NBrl1Cg2Atw25GhrrR3yMkBeM1bHlDEiRCtxF_J6YXWBPgceNRMN1de8UhJQ8g1SXqNATh7p31iOfuLHgqcOnKdNhGF6ZIfVFUor37-nLpx5fUMndqk8jPswfXN_keL8nzbpL8S7iGbNTnKAgNo64j3WcMpbWRi33pD-H1gohVZ_CDvXrROpH6Bd9IrSIglviZTJy73PtvsqPKHNPhFwpWP293gFOXF9dzoKNctjO9P39rQNqgl2Hw9exoHJls_R0fMDsHmpndsbElILrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22817" target="_blank">📅 12:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22815">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=jWAuCPZcu45cSs3lw4BQjVApUNEqPxWPf8Hg9pRHgM5vksYc2whCG9dapfu48kFVPHzGxjNi5nY1tEj2BCAb6oFEqhl4PBDVbmAWKK-eewyhBuzSXk8x4AhIup4cK9QxvcRxYxFEKvsO2AVyMPPsmefBgdPawyEGGm9RZg9USq9NdRQhrCJkBlkvIT7p8aR4Eo--stH8P4QlD-2VP79pA3I8y7vTgUBoiQtNbuzJtheVhXCiPs9uvqPsTQ0gzTtWhBgpb7Z9MCatf78RF1ERC0a5TVW63ohqcjXCyi_cIH69xBtToLPukfL6n1hIjiz7dkOVpSU47VvTLYmXS0fnxTyNoY88erpOIC1lttjX9Ot_7SqDUCMvGutNkNpHqVEmxOEFezqDfGsRcOnT_VtIUkW7OF-7gkgHfDtK5JU40PbYjZICYbt516hmKktTtbl7i_esoeW0mHE-G0D3HI7di3nnQ6lxtLlT3ylALSnjCDbw0eMl8-CF_WCNDyyx-yKwCFOG3SPbkMpl6Js2YKI302IsAs-6eyb0IlqcKDKj3GS4chlHAxf_ZwSIu8RSZGMUJahoBnZBMEyj9pdg_bKdfV4IwgdBd1XP7mA1m1jfD41lJzGcVb7asx6m1h_BheSvilS3zXDHoXJauuFrx7Vi2KjEQwOh0FatsrDHmczt28o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070c28a96a.mp4?token=jWAuCPZcu45cSs3lw4BQjVApUNEqPxWPf8Hg9pRHgM5vksYc2whCG9dapfu48kFVPHzGxjNi5nY1tEj2BCAb6oFEqhl4PBDVbmAWKK-eewyhBuzSXk8x4AhIup4cK9QxvcRxYxFEKvsO2AVyMPPsmefBgdPawyEGGm9RZg9USq9NdRQhrCJkBlkvIT7p8aR4Eo--stH8P4QlD-2VP79pA3I8y7vTgUBoiQtNbuzJtheVhXCiPs9uvqPsTQ0gzTtWhBgpb7Z9MCatf78RF1ERC0a5TVW63ohqcjXCyi_cIH69xBtToLPukfL6n1hIjiz7dkOVpSU47VvTLYmXS0fnxTyNoY88erpOIC1lttjX9Ot_7SqDUCMvGutNkNpHqVEmxOEFezqDfGsRcOnT_VtIUkW7OF-7gkgHfDtK5JU40PbYjZICYbt516hmKktTtbl7i_esoeW0mHE-G0D3HI7di3nnQ6lxtLlT3ylALSnjCDbw0eMl8-CF_WCNDyyx-yKwCFOG3SPbkMpl6Js2YKI302IsAs-6eyb0IlqcKDKj3GS4chlHAxf_ZwSIu8RSZGMUJahoBnZBMEyj9pdg_bKdfV4IwgdBd1XP7mA1m1jfD41lJzGcVb7asx6m1h_BheSvilS3zXDHoXJauuFrx7Vi2KjEQwOh0FatsrDHmczt28o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
محبوبیت بسیار ارزشمند علی آقا دایی اسطوره مردم ایران و فوتبال آسیا در بین مردمان کشورش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/22815" target="_blank">📅 12:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22814">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M835wFAnIMRPFhHN_iq2D0XRF-9fmU79ZDBBul-llqOCOK7tnyalPwPG_nQBaTGrEX9jE6Q0qd02VwrzsnaN2_Kv95aneF7KPmoTZi3hKZuwO5muCZRfv1vv13HnV4t1bj-YNOUbUehkG_uzUkMCs7eGQ6fzl7f-oRtn8pRnEMm8zgygoTUpdGZMOrhbKHbd_N9AMu0c95iUeL5N39HzsSbEH6ZE39xnC50WU-H20TG4ImTkJ96W5MYbzo1zyR56BZwuLtxaRZa8ih6CurNF7XRU_su1qPI2ELtG_paISlzE0_1eLXmQgSvR8GYuNGcT6w7tDsQkFniTfmdJvk63BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با بازگشت نیمار جونیور به تیم ملی برزیل برای جام جهانی؛ وینیسیوس جونیور شماره 10 این تیم رو به نیمار برگردوند و خودش شماره 7 پوشید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22814" target="_blank">📅 11:47 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22813">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qw-gMHs_N7lXa_0iPa6OVMV_ZXFmB2hrFFKG-zp2tPFpDZb94v0-f1_wxVFMfHjtI2CpHBGmGzIBqcSXt-34kvBMXo1ygzbFqfU_NVU7VFP6zN00ZCSXRQVS8eqpT-kalByTiygf9vOBxK9Wf_tCGJhw4gF0UO0I2FobH35ffAFsZhpvwXZYvz1l5DXcofBZHOmA0UL2u9XIbvJHV1k9KJrQeO5IPgpLyUPOdbrVkSu_G9Xgb3UlLlaC2-1RylzE5dtMdiuh8g3fJwsjjqFVxJrIqJjDaFmWXGFiJzyTeCMe7Iq7orSyvqM9j4OXFbZTkdUSe1yypKJrEW4VdM8hhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت باز شدن پنجره نقل‌وانتقالاتی آبی‌ها؛ باشگاه استقلال برای فصل آتی رقابت‌ها برنامه‌ای برای تمدید قرارداد آنتونیوآدان گلر39 ساله‌خودندارند و سنگربان سابق رئال‌مادرید از جمع آبی پوشان جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22813" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22812">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ino1VpO6T0l0onYtaIZWbTJbioxJYqHJ4LEN_L2GUKch1pSsSOA5XuU6k9v2SjNOiKW9BShOyTvPmDOJ1kY_YhPhwwRLPvVESy7ahpEvC7tYHg4CEyP5iV_pABkzwBKuanw6cgkGmly6RxgvgAga0qaX-70TwFoMIviSbhHz0Hit1YoxDeRd79OdInCfKQEjk8jOVvAi-onZ_zdxwFoNUK-Wtx1UuSQSTa-6LulJ92KyAO4kZmPtJSTYxRBIfBDhn0c11tTxPYjvN9Fxe0jpddXVazwTqsmwezuaybS2-BzSmUF_R2uVPf7ESitm-7vGuEewLCXDwNeCBZg9ld5cSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
👤
طبق شنیده‌های رسانه پرشیانا؛ سروش رفیعی هافبک 35 ساله‌تیم پرسپولیس که بازیکن آزاد بشمار می‌آید از دوباشگاه‌فولاد خوزستان و ذوب آهن اصفهان افر دریافت کرده. درصورت ماندن اوسمار در پرسپولیس قرارداد سروش با سرخ‌ها تمدید نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22812" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22811">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">⚠️
خیلیانمیدونن‌که‌اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس‌خوش‌آمدگویی‌تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22811" target="_blank">📅 11:24 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22810">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq40yApUiHR4Lt6vfOvlo2EKR6dB5uNzDojaUJAxWPYxo1KKMTVVtSbsNycmsiadkQ3Mv0Y8xqBpxm9DyyfSqpVld_mjuh3TijuBvncYkdTQWG3-G6b0P_laFGaca0ucU9Qj1cdoEtpAiDVqtvv7CUB1KKNJC7BcjIkRk3xGl1qI-eGeCzRk-AEIM7S1nddU_kPBB1vqtcZ1dU7B5IULJgBuTZAm4xq3Bl5kcG2RXb_CdzaSzOqkCmbwTTpTsBneKBsb6fhb1wB6FJjH4Ikl8Yyo0SBcHdKANnXUBvZJSHMqWPU4rGLtsamhHL8WRBLFfGPLIbHBS6dnbISqbLDu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
آقا منظور پرز من بودم. شماها چقدر آی‌کیوتون پایینه. سه‌شنبه 150 میلیون‌یورو به حساب سپاهان واریز میشه و رسما میرم اسپانیا برای رونمایی.
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22810" target="_blank">📅 10:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22809">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDJLV5tZYTB2VtwmVbgXYM6etJaRVSbN-P3CPAImIeXElVY-9AgEuGb5Z1A4_AlkkIqBNCoBb3nic09cuSnc8z3qVEQUy3QDLZ2dTdCcYfyZxwQ4rKRr7k5z70-_SEnCY79FvyYWoHt74G-1A1W2MzC9c2BqTGHUNFhKTT3-GXwYtMmZCGYtVeACr6wLdZlz0GBRdbr3-5Vb8pZlELiwoDZSjMdPO3qcQ-4H67fjOYyYDo_uSUDyvEvIRR1CvQga7tiQdRccTO3ZRHVQt9O_cLF7jXJw6qJKIPBdXc39n_qEoyFGEhPJHXvadG8HcCXzYnwZ6w_Q_8SEPR9b-tD8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شماتیک ترکیب تیم منتخب فوق ستاره‌هایی که مفت جام جهانی 2026 آمریکا رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22809" target="_blank">📅 10:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22808">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLarWCe-jmfu05Sfy35tIz0ri0BtZURpmosTKw02SqnkT13Lz9BfWphp8nDS443QqhfrsOyh3fXd0106Mem5TB45bcTocspPzucvbOtBaJsQSsCfb3k49EugvbCnEzLbi62xZB2JUmAs0GrN35NcfurM7U_Aa8C74lCaraELNWbjJrnbv3aVuksnPuHYsXHA-09YktRtfHKEsiiR7MdqqCBW6TrVJALbZ6BztaDiDdJ5kKHnQOS9ZPcLzsZLdY-Ra-XZQFJeUroWGUJAaeljxKCixJLuIHAx88MDYrkYpDTlWRQkRev7X2nn4ajWLoLlPvqHDXVbeB1aJT6GkrOL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22808" target="_blank">📅 09:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22807">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iseSGdAPbwagLaYrSeC94aAmDfo4s680R9C5l5AV23h3rLltQubcNTLYLoUGS_wnZ9cJwhmtsb0bpzOcQep2rmIqCdQl6zhbK5e-poEEl4XI5Hjzd7AFpXU-6vhIMypFBFQN-ZAaSceJZpNlaO945zAAK6qOVg3jtCYsutuPNUzuyFcef5S1Vw6QnNjfetJAAbUVyFRwmHEPT8q51Y9NTJdZTvwdOlCc6n9ZBBQgwYQrYmUqFxYlK23H4eaQhe2wbsp3srIazd1agzZzYbiAH6Y1ZZTmMIWU1vaRLjSOSyDdQMbn2s4BgroVUniMbHTIoY10ByQURaKIOrazs9ZASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22807" target="_blank">📅 01:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22805">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyQQMMZIuNZK-mD7W_r6j_j-Eqr87ljDQELNFiuMK-2a5VqXjAmR-CHC8QeWdBlP6tSYWtLJl7BO9fbsAS70C9b1UBALppl9LI4CElk39uPohJCStkCpikknx9QGMp44om71vUDXyGcJVlYy8qoH4srvGF7K8N6OFJAK6UCWRtlr2Zqe5g9UR7pzCJI6gYwOZZS97jGF5uDxE0JtEwhzOYFfFtZK3ZUu9Mqby91cg1j69TxNTSULdjZxzVCRV_JckeuYTBf0hQ6q-LL0IevdO80JrvLRAFx0CVpXpyAXT3tjsr8jnslkTLdekU1zxdB5NIIC2D56DnopoXj7oAE6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22805" target="_blank">📅 01:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22804">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOoODatP19A-gMZFsKZ4IiX5ZcvLIyEAr5q36EfPdlXZMcxsEFpBx8LZlxQu_aN6TArzLiDaoVPAhwzDjUGIN5hLvaHWNKBM8mZtQ7b9iZIIGKuJyMTzWZ8mAwpOxIunxGdr844D-bMe1KKihP0w3B88LJnrbdUZNuvSo6BObwYvZpkVNfjll0xyLBYKz14FUqEDPAEUAywzzEAnuJAexn5ppwc3QUagziyKRx7DD3yhZs7sduHxbFDDegiAtlOyZ-s0AvS3lYBWD6jMbmajqFK68RDEGEkBx0O4aW5Q9HjwubWuujmNQyXgcvxea7hMCMiMatkwsCJyo1wHobxO-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدارهای‌‌ امروز؛
مصاف تدارکاتی تیم ملی مکزیک میزبان جام جهانی برابر یاران میتروویچ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22804" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22803">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iry6UC8JKN20osBSqjyQOt3usaD2BOI-T1Ms19u_YbawDVB274aXz7kfzFUFwJ6gqIWYhVdCLxqA-gSA2uaJs5XQxU5LjGGjNLai3Z6zWRSayfwwSubPb_IFEDQVaOQwIObAvRenN9EKXbrxWsyxSjQvKXk8nMaLP0HUSsmogV2GNl14dQJiX_eKf2HAzKaAV2RRc92fh-pV89DTk0m8qsdcxZ11HpQShelVxXuK1EPzq9cqbw-odSMTMA4ssP8jZDB0zwRVwFa_gA-sSUrIQ0T3RdY1nnVHoV4NnZZN1exm9o3DYEjv5l21vJGQ3EV71W4_1SjcQKATcSB4k8ltDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌دیروز؛
توقف شاگردان دلافوئنته مقابل عراق و شکست‌عجیب فرانسوی‌ها برابر ساحل عاج در فاصله کمتر از یک هفته تا آغاز جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22803" target="_blank">📅 01:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22802">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8o9eToz9UX7neE23nV1la7yAwLnatRVLiHsZ0mk0WXX4wTifoEkFODUoCuPYyW2CwskNByyktRxKrnqPayJrkePTRdm64PnrQOvYB2_J274Vl5LHSPObI5pHfIiVWSAzhk1Qcqz56aN3GmEumm89k__1OTsqqpbxSiIwMk0BfDAt4o4tjwbJV48vJKgPUWYXZ95Bvs0i7VcPMIJ7MDQPXgYpSdZrN8nBbn2murP36ONFOC-YEJfpmczowaPSg4IJ7lVFeh93mtI8aitHteR4kdEftDh3oJJp9ZZ1RyMcyL5bVOuohV0YFwqvqKGjPGJQTmXlK-QJdTRP594VnHz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ اکثر خبرنگاران و رسانه‌ها میگن منظور فلورنتینو پرز؛ ژائو نوس ستاره 21 ساله  PSG عه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22802" target="_blank">📅 01:11 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22801">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1l424PEYoYPqQEREOrpkKzlnJUQi9SMnnHJfIHzs3CAf_O2LfbNrQhB5RfUWqqwjmOY7wRWSvtEjCGW6GWvzW5DijP9dLB5NBSXHUg5ltElrHrBVjENfbQaJeplzIXEdEywm_SeetatHnMAJXaWtB3kV5VW3hzkaF5eTDF8-hecYl5fvhOOUyQtg9zdlSnZDCWYVHdcVHCnpuvghXM6OrIJL4M1cUHHcG5yZ21YXxsQ_KPxtysiKU3Sqez9vkuUxbiZ9qACrc4ipbExhZx-Y4ljkQ4W1A-VV2MHogcZiNG8L4hDLaHftsr2skhrgCaBD7WO0jZqsu-D3RJuWfZw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینوپرز رئیس‌باشگاه‌رئال مادرید: روز سه شنبه برای‌خریدیک‌هافبک از یکی از تیم های لیگ قهرمانان‌اروپا پیشنهادی 150 میلیون‌یورویی خواهم دادم. کیفیت‌این بازیکن بشدت بالاست و بارها علاقه خود را برای پیوستن به رئال مادرید نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22801" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22800">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=XMlueYQ7Ozm6PPiUkut-iyexnGraR8rTnoRn0VRWU40Ipr5Um8jXBSY5GSL7Oslmqq4QtzUA975p4KsLbGMY7ZZNV--z15YGGaNsOfuleCEoe04N7b975LmG_BSrLs03Fu94rddohcFAUCnLdFbuk5-cpnJXuUIT3scbeZNj-eM_ECuLnj_4xpwERMdJbqnOfuIhVnPQXzdXHm-V9b2n1uIT9jNrFQD1fnNc123DOpFwKwdgAEkzjTyqT_qck8mW-E_h8UC413TDqQMYAm4BjPJfmPSNXpdOGrEcgQCWk2TD53OiRIV7KGfBalJINqL_2PtI29NahW_ZnKvGPDQbQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebb6f9bc26.mp4?token=XMlueYQ7Ozm6PPiUkut-iyexnGraR8rTnoRn0VRWU40Ipr5Um8jXBSY5GSL7Oslmqq4QtzUA975p4KsLbGMY7ZZNV--z15YGGaNsOfuleCEoe04N7b975LmG_BSrLs03Fu94rddohcFAUCnLdFbuk5-cpnJXuUIT3scbeZNj-eM_ECuLnj_4xpwERMdJbqnOfuIhVnPQXzdXHm-V9b2n1uIT9jNrFQD1fnNc123DOpFwKwdgAEkzjTyqT_qck8mW-E_h8UC413TDqQMYAm4BjPJfmPSNXpdOGrEcgQCWk2TD53OiRIV7KGfBalJINqL_2PtI29NahW_ZnKvGPDQbQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22800" target="_blank">📅 00:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22799">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6hxioyLLzPTN1FKyrXWpEBsnQvqnfRdcoPmaDmGX2hiqbFNW-8nxdhRhaI8RYA6pB_B71o_7Z7JNM1dF97RFpiAMDRp4tRoUeC6qpIXEunlPER3czer6Hr2lqv7N0WuTXgm2gTXb8Scp1BGKOHfggK_P78Cc-6niADzp2OVoa5bAoIb0WHXX2UYV_8aEjUuZ1zMfBsNxNiOU7bpde-t1Tu-0CWKz74JcWtWWZh2lC3ybhYZKBn9S1qzQUi1qQ5QOhy8BBXMJm8va6DmTe6GylIR7HTkbxOr151r09DgZya3B-9iT_VdjJugoqjVtFyPBYIRZlHgVUWnd7273KSEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
برخی از خبرنگاران اسپانیایی مدعی هستن که نام‌بزرگی‌که‌فلورنتینو پرز قصد داره بعنوان خرید جدید کهکشانی ها از آن نام ببره انزو فرناندزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/22799" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22798">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=hWkDHO_l-ce-IirUyouUfsTWnqAInQwIbKHDPAgJbLpQHJX9EcANR8ch8LkZPqlGylU2pOmtqtjildIUNfBThUSuNGCeUd32rpTslNIgHnVmzjLXItmONOOptpQ-bF8AahnI0ncjl2JloJi-ElZYLOyiDi2_X0E_4jcKmWnWD7UKia1XULk8YpCnGIr6aoG7PmV6oKAR7zVUI9GnX8dHxTPOmryNlDbF6TrDbYQmftp_6zIYIXM5wwgWFqMn1yoxV3IwHKOAS6Mnrei-EazvUQ941sID6o1cL2q2tSAIt6azGfTyIO6WlZpj5IZJzw47y5cGiDTAcoRs2II0Ox84YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e2029a699.mp4?token=hWkDHO_l-ce-IirUyouUfsTWnqAInQwIbKHDPAgJbLpQHJX9EcANR8ch8LkZPqlGylU2pOmtqtjildIUNfBThUSuNGCeUd32rpTslNIgHnVmzjLXItmONOOptpQ-bF8AahnI0ncjl2JloJi-ElZYLOyiDi2_X0E_4jcKmWnWD7UKia1XULk8YpCnGIr6aoG7PmV6oKAR7zVUI9GnX8dHxTPOmryNlDbF6TrDbYQmftp_6zIYIXM5wwgWFqMn1yoxV3IwHKOAS6Mnrei-EazvUQ941sID6o1cL2q2tSAIt6azGfTyIO6WlZpj5IZJzw47y5cGiDTAcoRs2II0Ox84YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلویزیون‌کره‌شمالی‌بخشی‌ازدیدار کیم جونگ اون رهبر این کشور باتیم‌‌فوتبال زنان کره منتشر کرده‌اند. دراین ویدیو بازیکنان دوتیم‌فوتبال زنان نا‌گو‌هیانگ و تیم‌ملی زیر ۱۷ سال دیده میشوند که هنگام قدردانی رهبر کره شمالی شادی می‌کنند و اشک می‌ریزند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22798" target="_blank">📅 00:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edR_o6ZBWZbbFL_V-nQgvSWNWypMWPCFQJ83NeuoNxlYsATISilDKqS-qdmJ1ZY1XcIwpn-Yf60j5hF3UeL55fWHWyspctMnFjISK9NEOO8qBETyC8pKnQ63cxp4NzallwI9wFOQd89X67vUu5iuGwITJGagGudXRV2sxqYAOo5hjlYV3A2rbFYRDGPHEdDf4uMVirTyLBobb23kJhkqBz5-Cl46n9yGRuOsdnamWmJCFTpAubPjjwbNRxKaRQaSpRjk5Xm12dCYre9UyWfAI4PEtnLqb75--HZHEEWY4iKwO3nVF1K4A1UUTCXLhmEhAskPW83wE1G8POMAsv4tUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NclrNcRWcnjp9VmY2WSElnaLL36IK7tYp9ucKtxqH2oBvvGVH4Nl1pEQm6qchMs_Z8EtdUE9Qf_4ckwvgqQ97jN-LK-b4n4k7wvZ5Bx3GqD2dN-4iL6PYWVSv3fR2G7_mHZ_fn-CZXiTjoKFAnXqvXu0sUs9LqOLZJBhm7g0Ejp-jmpgdksTIyEnJPwxQQTqYlN4xAFzXTMQ_BbaihSbBpvSZTON6iKQiaI74f8uAF5ORazXbb8M3h498gr_Tnvt_tFKpEman0BlMdKMwBgUwdkY5jZ-pQzq-Izv8F_VGu-tyiA9tdpASxyV-fxIXWT6Ue6hcwkTU3Mb-kOLT79tAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gS_zUeFY229GXRe72PJTDXM5EpYvxqNTAWjTR69-D49SRnFG9Rz76mP0sg5-GbUgekRcSUxrrKj-wWhIDyX8IoHWvM1jyQuK3mJN68jyLS9Kuqae_F9_4icVlgBsRNYQguOLwvEG0iTe_clbXkr7tNROJ0c_IOaD8HgMYaWtZmlrIYyyoqrw2JfKsyN9DYa-tvD3PgVxHlW1sHCZKxsk9fqLTlxSu7wswEr2DUFVmH-CbnGSphJBPVQLNRRE3ZaeMcs4yjXbHvd9TtzO9mXKBgTOJj-gRqich343DG5pIyMxDBhJWUEfqO9Qv37A0Y0GdbAQT55Xoe-W1oUfd_sBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oI32QrsOLw9rZwma1x2a5L6Ju8R6V14osXhfCok_EtYqEIvjeXIPyPclnvtIy-1qsLKBzN22nKXqDgOyYKOMIb4dkOuHXg03ylQbjT9JjF19rb2EkIfBhvSQpKO4sFXOcKo3pLzwjGhYQaKsfkOuJ6hR8OoDgXqqzrEMzpizSt-QsVwleX4pNYfeB6S6g8vUDCfLWrX2V8WNWn0dfOkwf_F_YGewvNl1n70yXmx8fLE5_OhqhtgSbWIXYaJG6dVVeh9A54c3ksMy4s8fTUqN8aAN_iaTY1W2vyKgyzPB5l1HqOPz-qTupRiiTmIyOICfugir3qugo9WPnz2tW851Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eT5FPkjnfDTEbu2xa3dCNz_6TM7vuNpfemKjO68fnepR49RA8YiZqUIgieT0Q83Utilim81vVX-TTZxlU-Q8iUs_uYH_r-rTU03gymqY3iU5mVJ1i6cfUwJwcg46rDoe_hdabxlf9C-umVKBBBUM4RC-48Me7aQXjxN5vqCzHpjAJC1-UcpzSoTkRT1Xyl97hC82O-b5e-tFUtiDjPlgHHtVifCQCPTPZrlGwThauxCgiY44PNq0jpBODEascFOv_jr7zLaQln2i5PAjZTaJP5W3Siwt4ODWKwXbKCo26sAmZ-91seQMJJkLsAkNv3PNW6XkjFkqV7DPjMHGWp-rHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH19rhZEMS-anfrf2148TmWukDsEV81-3JRSoMxf23amb00N6kEJXvscMupoAwR-AbuFP5t9h_TVJtg_24BZMLNEyUmCaD1--gyUUiosWXprlUazOOYw0VSQQz3N0FXYHCPecsmJQLxO6gADs218bX0jziYjKmiOAfMnCZfZcRbJjXTBCTjZZOx1Tn_-VQYoZCDkSfN4HYGCfcKCZx-FdLZr__zGlWvSsp4xp548vo15o9eUob1u5NQEa9P2DClQBmxXo1YIhz0EcOvSJ-l1SkI2XDizlMZRwpvWvRQ0f_C1pgqonHhOXFk7uJrqHgT7ucvD8xrt-LVft2lqBXX8TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcJlCSnnYdmmu8tuZt-BIX54zbQMxMq4LMd-Txl-Uw3BdAFmo72pCNrn5C59tzoJkCJJe8iqPnhl20mQ2h0iRacAXb1j-pdLLHmOulNh8UM6I44G-0eKXP9SkzbgBOS2NFWpbPyQ7dmQe5KWGQpVY4bjgjcSdGkW3hyrhB08QSYcvVxcpISnwkd8GzpP_Z7icpI8t7uMSBG4b_h0rUSDCg7HA167ESaoz9ntH8WE-gMME6aavGqoucM_Ic86A6TFlG3tCu-RKZ6mT_HVtfYXlFwD2GOU7r9rx8T33aEaukIlUvfTbZsaU7rEQVtdkmfMvCGYUDx2WF2Ly8w5WZaeZqTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcJlCSnnYdmmu8tuZt-BIX54zbQMxMq4LMd-Txl-Uw3BdAFmo72pCNrn5C59tzoJkCJJe8iqPnhl20mQ2h0iRacAXb1j-pdLLHmOulNh8UM6I44G-0eKXP9SkzbgBOS2NFWpbPyQ7dmQe5KWGQpVY4bjgjcSdGkW3hyrhB08QSYcvVxcpISnwkd8GzpP_Z7icpI8t7uMSBG4b_h0rUSDCg7HA167ESaoz9ntH8WE-gMME6aavGqoucM_Ic86A6TFlG3tCu-RKZ6mT_HVtfYXlFwD2GOU7r9rx8T33aEaukIlUvfTbZsaU7rEQVtdkmfMvCGYUDx2WF2Ly8w5WZaeZqTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=sybEjk1cxABNUPJ4qHKBACaONfrYyN_WmS1u_knTkhM8klg11U9jhYSBs6vwp4V3FcYShKZDuaCY4cZU-fgyAdLDRE57bhktPfhYHBlFp-APwk5oflfEetlKuZ6W0owX_4oWYPkOCQfIwiET9zMTfWD__Cbv9eZm0P67cZQNHVTaWy08Cs1G1XxgJE6eIssXPRVQPrZx_3spcNZ7WmpmX4Cevn45ZSQhnOCoK_beAlzLTOITMsugSL6SRNKR-DSJ0H4yQxV3wpoZv1hUFutCDQQvYoNWr4nWn99ozul25vP6JM7OYLd7KG96cRPBV7Zgm1PVak63HigUpWmpWx-voA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=sybEjk1cxABNUPJ4qHKBACaONfrYyN_WmS1u_knTkhM8klg11U9jhYSBs6vwp4V3FcYShKZDuaCY4cZU-fgyAdLDRE57bhktPfhYHBlFp-APwk5oflfEetlKuZ6W0owX_4oWYPkOCQfIwiET9zMTfWD__Cbv9eZm0P67cZQNHVTaWy08Cs1G1XxgJE6eIssXPRVQPrZx_3spcNZ7WmpmX4Cevn45ZSQhnOCoK_beAlzLTOITMsugSL6SRNKR-DSJ0H4yQxV3wpoZv1hUFutCDQQvYoNWr4nWn99ozul25vP6JM7OYLd7KG96cRPBV7Zgm1PVak63HigUpWmpWx-voA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAjsgiRH0ioFkK1gokrasBsXq6vXmh-uc5DAX84xc-GsQyPEQSlVdtDTQNnuxzmCtNKclrFbF_kWU9XiJxalBgGtwWxQJWSUE7uXq2VyqgM8Q28ynQ4e15PtG9UYIcBPLiJOWDYz6iyKs8rAAlUE09x43Cfvyw-a83pWTOMXKh53GN3aBb15IiIvBeUUorYn2fw4wmbHS30o3L9e01jb89B4Lrhhm02PJrdHK-xDw9q95V_zX4M4S2GL0InMaVbp2GXEUqHc9xiRlyZlhZGzTZW2y_LSnWJTljpZpkuLszQUpW5WFAFY2C5tKcMmKpGirxFaxnHBwcfAM1Q2D-PQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MU7FzXxXGJT3Z-fE7absQJ7kLRy1z1ZsK2e6TTWR8An6Bab02FSduItM8RGsahbLRXXpTgkyM0zpdHAxytowv7OiHcmgQ0RFiHQX-IQuRlcx8q2ccXsMjssuNrccUFa8HmM3-pgHAwp7G5EiyswAoSP5xqCV1suGMYeGAsDVtuIyAQ6HFLXAy_rbPAvRzWl-72uicobjLxhO6BRVA0jhlrsGawtnAd5x3DzKQnkgl1nioaCO9ZFyrp-vN8XiX2M5nzpV-g_qVLbsjPfjaEfa8E5DVnkfxqZaVE4qge8wKDqwyFxIrssmK3vEqnbvl5ufu_eainVwF_sSbCIFIT6V-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJXm22mvCHbbnXPXLL8FxM2tns6LNrQj1BQ2RhNNCcvNSi68PUvQsu1aqENbACLafARs4tXPT6Pqv0p9LV1qSW3_DRMW3lVhIZwvFMo2dQyDgerFcqcLIeY1jZ_xgshkrMyOxFkOp9d0YzWEMl_E6sny9bKvGtrSJXWIEnDt7kE7-zQHuwFIP8JFf8sjG7rihn427XfBu3AbdvDRY57jUNb4_dro2KJdyI2leexsz59tGGVEaWOvI-7hxULoeaq1qm9HvckGSgG7K4bHTjq7RTefpkL9Xk5X5eWFOqvLX6iDnH3fPqeKpH243r5_X6bldgBUrRs68FlUgTF5wueF7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBD7QEK8g4tr8GrXrhxryKrJUqt43vDA68I6jkucjwouLxLeRZ5iXRbC3GNb2u9vhjn_QNSSZShRmP7r_TTAYzDvHtmejHGkt8beHS9mW4S4edQNfEY59dZLNUCR5aTOOYk7NVLVbKIkQYTAveSRFTisMg7851NfdQDaNu7r2IVnYKyBcx9xUZWH39n9BmvjZbIFVRV7IonMHkjltZ3hrxuRN-7sTlfHgSPzaHKXnwGyAWwf4USylD-aNK3paNNP_etUDQPWoak36VBVpOhJIfiMJ6u8zYwpL7JD19OLPxdYY9WIPLT0AoTDDzPftrKbN_0kxIy7gDku6QCqgHyZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9razuo4wZH2x5cyr-minb7YRNdt-QRWPwDm90cGgtViXdAkStGyCY0ohUfB-8A53P1rR7enHfyeHBNO1mWyJ7-lgNmYCdX8Xatxa9ZCfQ5imdBAZ4kDtLu-RAYbGyEjI7gvDruO1oQLn47I_0oifP2o2EGJlGs2tLYxdWM3VLwgTmg5w6hv6QbW1JqmSwfl52oAABjQYycoT8l1iiUGQ9ZyHM2xu-MreE0XpKnxD2sipyY0908Nv2LL4H99UM31qNHsoDnQRMpVANkWVRNHjcuGhrdOl8xMWUDJbgBFNT91ru_VCKjDJk5CceLgF1Vq2bKOyH4xe5TrR5NR0conpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IouZ7p77SdV7bQ694x_G0ObInY8F5DfMGUXnQYJI9oQzESKWOZFX-XusobkU_MEJBFwMRCmd-ZfvOY6kY9k6DVxLsHr2Qnj_wInA0D16y6XCNnivfJQpoLPFR0quOuqKkeXy5S97C0475gALNhmFCoIlLaWAgRKibuSmwAylBqsNPhPJlO0BTdTSnZAHbpTwXTaQhKtYqytpqqQyZniN5JY9mCLntkgHc2PhkZ_gnUXxWyLD_UT48NuG2XfBSEjZiw3Mpqzck1WT5luW8Yi4lBHZ-H6Oj9AIXdfrNNa4gznivGpk3fXmLWwdFgIC7o0NpsJx24ICAs_YURV3OyHRqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-4YwjZesvCjHymn8Q3g6ryy_V9rXIhYrKt3LmnkBATO6Izd_29ctiluf7k5JSTeziQnj1hRWRaTFIKhUXwnj26m4Sx1qO4oZV5FEOjAKhsy2PXQCv8JHj78Itx5wIcMp2Gvb8lIDvowOFwK1Warllr24xLulTc4qRwgD5Z1vfUF_zlPKcqQsyuFF5GAzkGUoJj_V2vRJJduGt4YXtpLXiwoXOuasliGY1CJ-E2KjTUJDqgbHa8YC6t4XWhhZSOscJGAQaEvjJH1R6nXrcknOKtknxzOS3pZedIJlShdUv6T-SevJJ4x7E87nG3SFev-fqkTFyakjT465lUEWUHmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNJYNoIUGYHYWeuVx2kpVlVlxlRym4POA35pqSbPF0cR0uCif1h9J4xb_fcNKVs7-cVCVQmFUel76-h5LUpQEFWx9XfwH4k-alarXTueirzQ4wiGct5VGdM0OSn-5UaZA8hXxcGn7ThFwOhwH52r2h78nn-aMeTKlR-kI23vY0Sux6qql-qgiWSS77Soup9iCZTL4_RbzEIIQAhOzViS7ZWU70Vlq4kq-bYiv9XbcqLfPf94-A8dAKhWyNhzmjim3vSdTCYjCJxdMjI6v4iO0xOYvgpQN7yERBYhYeuJg2gk3_goCWrIPYe460ZAnYZz_Fm06avjdsmTJrfyyJ86Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atxoAsNHUrwvxFfr-KpuNMvL1Xggt7YMhjPKohGEzpQGBSlKJOJxlMfvqVpjQUXuq4LFHYrBqL5oypaah_nqH5dOxp8HuRtIZpkExrlmZq_1krJXMtmg4quyMzWHzncc4d8Iu7fsf7E2GcGFrwx5jkKBrliTpbsp7aRMF0fjpXA3YWwEDnu01CIEIZYTkvGQ_t4h5PqT8i1RKPzDzTP7VhNdAJrKapNANL9jR9QILa0063qUAuZxEP7alvkncpGpNlB1vGdj_KscJxHSka3K6fZHT62AYD5IgSQiVHvseZVufBVCQ0G8UmGsH6YjMiq-50xLCQRqqvvi5TFkb9BjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5d7HhkuJyczXKqDYQl1IMs3pTqLmwadni9rJ0rwnIepVzMLBs7OBcyptm9TWhx_TJANhbZZ5Zvhwx-EanjqnwvSLTqyEgOPV9nWaOwax2fGCOh7g1ZtkUFMftGZ3A5f5ZFVQE_GhCckas9IMRE0sIOuyfd2QXe2-2LN-fufxmygF1UIYNHbiRetvtcEAqyCd8g4KqO_WpZgaci6qDU4doLRe07e7kouTIrITcL_6mFeP4OUslzt6uUOE39-A-keGTgP5TqaxYFTFb1yqGlH12sYrTW00DGJ_894COCHuNvmtVh5IPV4tpZz29Cyp0pMPfZM12_4KipcKPD1xxmuVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=DOz9xNZfzKgzs9ik1PG-_5aHNXFb36o2Ckrnp6ARdwv6UaA5MAEyXq5zsaZcFR8Y19PV-eyYUxwuxzg1NYxPVFlCDrI4Vkm88XzJbc2NzFVEGkeOFEZXgybZ5P9YuCCUEWrXBSZ5S4JZWiS81_z8ofu9y6COinqlYzL9UePdNpPFO7QCyPgA0hP5D9Qg030tu5axw0C9WeypMn5JZhukdcCWYZWhMA3_v9vzms2fm6P9hrV-TmoDXL5_VtmwEJb75FGNd9zeAju8ligJlM5ERUeWEeiBgmkGhRz99rLu_7OPKsLWxAE4IIZs0YjOy_9lMNVLCNN5ZCO_3D86fZZhZL1F9QoHqzT9lnYGhL6736QSM87EJV7NGZXQTZd3rla8LivnQckIKmhjIZPixAnoQV7Ov8ft3sgWSI7mVnelxOy2dutiPFWbBhHm4Oatdq9ZF_PXcaYW2nP6cXmeG-UJIBC0FnR0te7xJoI1wtWRKAyyD6cOHK8iFhjo62djTQo6djMC9Il5d5mgoD2V5GtA970yVNqt3muF8DftWx2TxzpMRJPvL2zEj6FFdF0yCNp8WWzqJDrwQTCN_X6BHlF024bbT_HW6taXre6KuKeX-A5SZHd9cynDRl2RG3XFmkob7ZR4H7iZu9zvZ8BG9r5eoWYu1ffcAjquEs83MkuUHJI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=DOz9xNZfzKgzs9ik1PG-_5aHNXFb36o2Ckrnp6ARdwv6UaA5MAEyXq5zsaZcFR8Y19PV-eyYUxwuxzg1NYxPVFlCDrI4Vkm88XzJbc2NzFVEGkeOFEZXgybZ5P9YuCCUEWrXBSZ5S4JZWiS81_z8ofu9y6COinqlYzL9UePdNpPFO7QCyPgA0hP5D9Qg030tu5axw0C9WeypMn5JZhukdcCWYZWhMA3_v9vzms2fm6P9hrV-TmoDXL5_VtmwEJb75FGNd9zeAju8ligJlM5ERUeWEeiBgmkGhRz99rLu_7OPKsLWxAE4IIZs0YjOy_9lMNVLCNN5ZCO_3D86fZZhZL1F9QoHqzT9lnYGhL6736QSM87EJV7NGZXQTZd3rla8LivnQckIKmhjIZPixAnoQV7Ov8ft3sgWSI7mVnelxOy2dutiPFWbBhHm4Oatdq9ZF_PXcaYW2nP6cXmeG-UJIBC0FnR0te7xJoI1wtWRKAyyD6cOHK8iFhjo62djTQo6djMC9Il5d5mgoD2V5GtA970yVNqt3muF8DftWx2TxzpMRJPvL2zEj6FFdF0yCNp8WWzqJDrwQTCN_X6BHlF024bbT_HW6taXre6KuKeX-A5SZHd9cynDRl2RG3XFmkob7ZR4H7iZu9zvZ8BG9r5eoWYu1ffcAjquEs83MkuUHJI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noxMXwWYuDIt1rkKjTNXzIX_DOwEecw0AHR4IzvOCwA3jdlJT8cKWxY5s2otGXEnZgNfiXQUnlgQ9qHGuY8VYiDco68LVS5-NohhUicaAaKt8eqOmSEe4ubT4R_CmfNWylTllZzZJVm0lfoWafEr06YIgOPA7hgw-b0RUt654LixBl-BkuIY9A8f878ls5XWgJJfTNwah-HeYnzEzKzJGn7vUD2JRJfbsu77C6eJxMpdXuKKWDJrq_Ml41gPOTgv5XUSa4UbByuecf6wqjT4590lK6EupIInYHUMx_RG5ot5KkmhKF_vjxsFWuK-mpd9efLaqXDrts04n6WxCPxQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=BrD3zunAShaDDjQB57x5rETfBqL6UTz29VUxwaCZ3JT8JIBhIwhOUwpRW635ifGGGU0ztNdkH652ZufClmydOPZCUjjgXVVliLS7QBBJdsAYRo61g8xWYqumJMDTJDxdBD39v6c50btrXocXYZjvzE2gR2RVCkyqkNnqwspii3n2gCLVJlBu2UAC0ubofZFY8A4K2CVT_jsWwW4BxTSyhAZYPoMHshjzdyXwtzHkGl6rrlpV6y7TdnzVjieEbN8GIuKF6BZx8P4fu04SCQWdyP_3hVUiISi57VLbjLYscFwK3-WFIX5GTwfZjwNDe1exnALNlfbSN9PG0kYPDURarj_gCZgKxh-StcEHwxxhVAghThO1k39d_jXFeMRuDk0LuJuDaf7z9aIP3rz8XTNRmGcurrmFzPaxd8ApYmH8fEYCfNxcmM5QevUU-sv5RUrcbTqxEFqqGHGEUs6eqOauervoaNZ-oiFa3M3zWHnQtLzEqzT8pQscVjjEo0jbDbclAnTjttDcozgnCQzaFJEVtEBt8I0MgPJM-fFDfq8Wo9Eot56EBhViZwD265Vpwep6B2PSmzHiUySgVBagwEWxqKAPFSoYTmsjusV9fkVSWPmOntC3ylZXidz77JgVauySZmSxkr575SsIXZmooxVoqHxfGtAsoWlFrtswmiYtrtM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=BrD3zunAShaDDjQB57x5rETfBqL6UTz29VUxwaCZ3JT8JIBhIwhOUwpRW635ifGGGU0ztNdkH652ZufClmydOPZCUjjgXVVliLS7QBBJdsAYRo61g8xWYqumJMDTJDxdBD39v6c50btrXocXYZjvzE2gR2RVCkyqkNnqwspii3n2gCLVJlBu2UAC0ubofZFY8A4K2CVT_jsWwW4BxTSyhAZYPoMHshjzdyXwtzHkGl6rrlpV6y7TdnzVjieEbN8GIuKF6BZx8P4fu04SCQWdyP_3hVUiISi57VLbjLYscFwK3-WFIX5GTwfZjwNDe1exnALNlfbSN9PG0kYPDURarj_gCZgKxh-StcEHwxxhVAghThO1k39d_jXFeMRuDk0LuJuDaf7z9aIP3rz8XTNRmGcurrmFzPaxd8ApYmH8fEYCfNxcmM5QevUU-sv5RUrcbTqxEFqqGHGEUs6eqOauervoaNZ-oiFa3M3zWHnQtLzEqzT8pQscVjjEo0jbDbclAnTjttDcozgnCQzaFJEVtEBt8I0MgPJM-fFDfq8Wo9Eot56EBhViZwD265Vpwep6B2PSmzHiUySgVBagwEWxqKAPFSoYTmsjusV9fkVSWPmOntC3ylZXidz77JgVauySZmSxkr575SsIXZmooxVoqHxfGtAsoWlFrtswmiYtrtM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8bgLt4Vf2QaGAGV_8iYiP4u6TnyL7-sVrPBGj73aMoayqvBBhZS52wZZpGrsK7liyQfgufnuqFw-0dGyfGWds24TFPipWDDQsCzKYhiqHNve20k7nHR24G4aXJQ1RQW9TlHkg-ol2ghnqcmw2sjga3Mb_BSKwrpHJ-77wHn23OIqUwofSWSSoj2-RoMEEDuspQ5jsg0yHTxCOpDoAHIt3w_-BA5MUH9BHQuDX9JyQk1fhIg-NrALp02huuW9Lop5EFdeVtORrdFDhviApUFNIHAEslVvUQFq52dpSknFSN9EcXL1kZNAugi6eweBj-aZxnaJ5bkoVD-SDObblj2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAisPfcK0Mxy6ZwK7hbSur1SYjuY_By0lVphXzUWk5STBk0MRJ3fPJBquWkxjl1RbBFig3C8CS1GgMkp8zAoG2mqmgjxbS6l9hKdflHEbiPEiH7fRr8C14pRcRyGZ-tKCn5waX9NRZiGXQlmD9AHimjTpQASXIouqwD8sUCVf8pJ1yHDt5IOW-zSU1ZbbPigxcfNx7iUQwtVFUsLq-SDWIGn8IfY68WfFL9mo3yvazuDQ4ByM0uPgd-KjanQ8s4uFAyptphnZDxe_vuBkyn17no8uu0UPoQRplTrinlCJslLXJjyNf1LKrdcaIaUxRDQV79d73JIeGyHRCXVlpEEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxmSG4T7vT4eHEzJykV5wf1Ath2LC8vp9dGtKmNsco9mLB6bQuRyeXMWCv2D0IU_OrdHDrBvFN7Av912Qef_ERIMFQ2eKu6881T0xaOvD-v-ydBu9wYfL-S_m5YEs--0_1q54HuY4rE4rj0VtMYeFA7b0b9ewWI23Ssd59klMDecqndiAzKqxqXZwMd9P0ymiq_QadqCBqL_04EntugEkA2DvPXA6wRXE941hW4Vvzaz0gVx-NayB57h4dhQQUtk2wZH_tKxCIgx7hBfz2eVqOw6ApnJFmyx1FJ5aj1VwXwipuY0XryjCYUnalKwlLvsEWQOrnFpHhM8tBi4rpM9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu-qcuWVLjb2S4KQQKPXHOqltwtVftEMvd7pU6szohjftYFgldnfVm-nkKgmwwdMxCsWNRZ81c7VFdYTa9W8BKEz_hAvUs_5zuXXh2Y-W6-ngrtVIguFdcG4PFVMs0oz__BQotD9uzYqCbcDMcbbhDUDHEpjkEdojT4srW73ZBXlMJBMYhztjZSikSrkCZKZyjTWLYmOWwz60XsKwqPG2drlC0lYV_3Q_D6NJUEE57IiPG9pGL0QCHAK-Ld107qJThE25KCSATnZc6e5izHZOlqyJ58CbjoAcad7rTfEBXdjBj685G7n4gTYTRKbqWNKmxXS1ctheO6gYckOAlfIpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR3bLbM-1GeqOtmZihrE6TixuPmEiWcU-28y6_OEF0hzp0fO26h5cGBfh0badUtUK2Q611JJv4LzunzIzBupEUmFLv8W6DODHUvUPi6OOvqXrs3Hd9CfJ0dKxqO0LjMiiT1l89a9AaK8DPqTlAn1h7RypaPHdjtxyBqPTnc8eSM15kqJVkEzBUyNZC50gT4PtqF7kOgHW4EqYczJnzir_WB2dxguXyOQ-rRyPzQyesCUccXqlDi517Kw0ruaeqEG4-xb1d44l-_NUfsCJFGOd9ykShb0KLHOPs9RDKhu4Ed8VgU2PpKoTR9DtVL8s6RyRQyh6_TgG3Kx-XI2lNl3EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zkp7etb-W0YO_0F60VWDKfdfKD1bPNJRCY3VCKHafwZ6pd115YGtuZlrUFn_xHwz3xhAvsqksRpU63mVvrzg0VUKgs8QBiXfsclUSY-dGbxFkQN7apJwNg7Ho6kw9oIsnFc5nTB5wIb3-MJElI3EROjxiVMKFnB3gc9qVAXHPAY-GEms7Dwqmm7Z7ffmzd9kS-qEKSXXjMYfvGIxh0QN4pdGn6cknzJ6-o4xS9rYEenyIXgut2WUK9bAyHzLzHXXVV00LgfuYvRIjb9rMelo1i7jV7_TUk0dnPQOLijUWiLPmS34CQN9bf56ZAZy0AYZw9IfSKgRPaLkg8ArALZpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZVShG_oeec11MrrSEh7CKtYtLO17NZk9T_AdhPZwCMoX9c4HYHuObeU2yBi7dNhVokvLpy5hp5gKSXU99j9C_nB9lPpe6Z7CS89zSF0dUy6qJ0EiJWFuygKv-ujTExDlNGqcH8ggG6nckbERQBOabeaYDhJOpPyFHXsUP7zxYESqyoqsLQbIEI7douO1t9fwMOH-KkJQ4l6tPi_EEBpluwHcQ90VMDgNHLkK8o0dgefnYEDMFBBUcFlmDzxFyxc_Y6J5zcK63ivRCBAwhojEEzque7T6gF1LTUU6dO04EpMjL-dbgxfNMTDgoAODSnxQMnXyOtqmbBjjul05F2ZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ut4uy5ctVlKc0qQXNBsp8aQ1HYo40KwKluFuISRRU7Bj3jG3Ld6arVO1RUeTDHTc3pvO6wRtTkgrRqaNeFece_DwPvIgr-1635vc2WaIpmcHPMsExQnuLF9nyww-GPxb_FSGysPA01GLExJ3O0DBGgikEV1k_Zw1TRV5YULoPx8v9-KClYvtYMb6BTnf5h2lS8HTuN9JpQgVM3pCrr2F3weTW8X4XkeOQ1hyp-yXEYQa8mSu-aTNvB7gJaDSYHALKvB3FOceXgM0Oe-UcSLOXy33PIZGZnBJ6QQw9eVplNUEEpdP_h_gYCBJMHRVpwqL1T1BUA9vt6Yw5e3Zjwky0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc7okzwIpfn5M1jpnk8u_d0iGqtMiGQefkHbJVUNpDknVUk0FLFZIxhmd6H1daWwLoF9djS4POTCsyflePY1XifSQdEvKa-uHfE5iUb1GvcZPc2qdRFnuFTLDlxncloDBdXJcan2GM5ZLaSmEs1hPbdFa3ea881wBWjLkpsp_KFKMQ8fJ_Ys0dOA9U-s14Zo9IR5mV9lG7hAQFMyuveU4ayr4DqAW0Fu-L9LeTK7tS5vQYkIJsp5cNpGm6_HpgS3EWJ_fE3IKMUWYWUFNvBtudk6Wsg7IaU2Sfkl3FJOCfLoF49ZMcyXB1-hjw4-BP6bxhqwBniKyUKiuGjB9mBf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdl9Xtr2w0am_VatyBktSTgFvKYXMT4rPxh4PxHe6Gb2HmaVhvrQfEXJ-FtYf6btlzEADzXr7-0QNvvNp4GRoPtcc2VanlaiO43CQg2gVfYPS3M577QLeme0BdPFxVpuAYHO4ieDWZQeWkE7w8sRz5N0J2jacqQCVc_sv_cXQCc6V_GVTtoPzvl_uaJ5UcIgTulEB2egsiOk01vnHmORgkFDNIdGau7yNT77hH_9MGcT2vyoJoGU0oBnepqKlRNEoJsYLB24Ja70gkn3Q5LFnVPS5hEFI1B6t8mLMggYuw1SrjlT4U8jRy7OEa946YrS7Yr6kskzr3-StZl6kDcZ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=oPH3bhvTw_JChsIYAQ5ghU0mBBzTVkdRvnrjUx439ZSrC6ZPFYrrOkkReLCNI6k4eX3r-XxfslzNA-Aj_NDMhYktsbBpaJFkFW5yaFKk3CXKQGvYq5zkrRc7jJ6EdlkOu8rL45veyF6Ee1CdqThZ2IKn_LKCrVTmQwFxlAmIG1T1fuCEVG5SuphaV9UHn-2NlpS8cUbq1rNFYJCTsWHIyX1ixMXGHjdqPYgJsl67QebBOHpMDy_vl2q0nhBOuPi17MpIXLTIf3jTXM73Rj9U60gLN6tmzO2LhI6UFMhgUuBmfOSFgGvzWNMReHkdQJYKduTHNM-0x8I4LgGQ_7EAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=oPH3bhvTw_JChsIYAQ5ghU0mBBzTVkdRvnrjUx439ZSrC6ZPFYrrOkkReLCNI6k4eX3r-XxfslzNA-Aj_NDMhYktsbBpaJFkFW5yaFKk3CXKQGvYq5zkrRc7jJ6EdlkOu8rL45veyF6Ee1CdqThZ2IKn_LKCrVTmQwFxlAmIG1T1fuCEVG5SuphaV9UHn-2NlpS8cUbq1rNFYJCTsWHIyX1ixMXGHjdqPYgJsl67QebBOHpMDy_vl2q0nhBOuPi17MpIXLTIf3jTXM73Rj9U60gLN6tmzO2LhI6UFMhgUuBmfOSFgGvzWNMReHkdQJYKduTHNM-0x8I4LgGQ_7EAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDuWGc4a9t0tO1otKR2jsB8ES7dFtiJ903aWExVg37piBBGPctFq5l_MoFndMxqm114KrKan3Jpm2mCxztVeIK8A2fgMK9sWQmpEZ0D1gtU0nEowfIGi4Tv2BRuh9aS5JzxHmjbyIQ9TnrYSpW0bxwAFqhVGJIzLfQ5_grOtnnklUxVjiIO6SUTMhur_S7AQjU9dq8l7lL8xsIi4dBsrizjLHXhWLClZSdC6J9CsTMIRpwleDqLjwiHyVdKiOeQll1D8b-51FPcYd8lkbVQoIu0da-eVRHIWHark1YYn4u85pcDGdL8hBtqdBSL7ooIr1y81Z4_-FN01snO-Ho3e2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe17HrjwCgDfL8PDbDANPOgawYUD0q-i2DdjUrg0Rl_2hk1Je5P4LMWRPK30m-dbmCGG9uYx7SBJ3yErclRxUWXo2CbVWJg--hLGN9Y8jaXuLO-5DNz3UJFZj_THy9KrdVx2THIdhNRdk5g6VLOJ4I8MJfWzyCUFrJg286ixm7DWJHnRE7vOpDMxmDSrUipJYT0xv5p3BkKChjx1o9mGMsL2I-acTY9__MnfmWs0UxI3YgKLVz4_nO4TYVnN7sVE6mo-UCmJX20vG_9rVTdOmq1OmvkEHA376kZul9na1KOuUp-LnvH-xKnJllFl3u-kKs-eLZPwzp5f3lY4Fl-voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhAHXOwCTWIfBqivKnNKPkGarUHpFOdMqEuM9Vzu3ivGJNs5SQssn_NQtGNGqY8pU7mqBdRoHaGXuCptfwTywyWcmuvFTj5fqXCSThR4ok42gMej_ReQhSkrw-7luYC-JrMBvEBOntPIUzj1KB1w2SSKPM0Nnyvu9B87Xm2EDi-X8lWOaj-wxAW3pJ-mM3VZjRK7uzPTC-tuzdnrpCbf3pVfqOClaJBFUcQhMOwKRbRBUu5LDPuSnUf9QkiyeRwgqI4J0B_n1UDfYJ7F41HeOSAt0I70G15JO1U4sa2qqGLkCmDDlZ2NNSrpkgS3oOraEcEf0-ClSCpABpzQCbkbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=bSCkXrSvK4zf70OE8mVMKc7YgFaZsXRNCyuh5as1rbtXYheHXd9gWbXFTFPJrV_i1qUrR-J8oiK-C5xk9-zVgj8rvy_cfBDrSeu3PX3giB4gLZBWpCN7SpMmmCt-5WUGSobDEfKkQV1OdrkRA7ivosaS301v1D716MpINNZoTzR3VS5i6LfQwncTr10QDnbwqPrTFiARMG-EJNNeLwy9q4UwCLr3izvbsZHLwwIjmiSSsoadwQgEMTbxy6PZYgayG85apcpXpLmE9u7UqO6x7WrYv3QGz5_8f2n9ialu2AmeSrDEIuPEBts2uBbMeCCirMMgcDLFfNFxoQyLG6Q1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=bSCkXrSvK4zf70OE8mVMKc7YgFaZsXRNCyuh5as1rbtXYheHXd9gWbXFTFPJrV_i1qUrR-J8oiK-C5xk9-zVgj8rvy_cfBDrSeu3PX3giB4gLZBWpCN7SpMmmCt-5WUGSobDEfKkQV1OdrkRA7ivosaS301v1D716MpINNZoTzR3VS5i6LfQwncTr10QDnbwqPrTFiARMG-EJNNeLwy9q4UwCLr3izvbsZHLwwIjmiSSsoadwQgEMTbxy6PZYgayG85apcpXpLmE9u7UqO6x7WrYv3QGz5_8f2n9ialu2AmeSrDEIuPEBts2uBbMeCCirMMgcDLFfNFxoQyLG6Q1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6vOO1aMjtCFJrE7oQWjfAMwHw9W33iTrdsI0RGeTTntRwmoV8v9GYgdbNmIL-wdc6-g_QV8yrGocNbXlV1Exgz6p_UpCS9LWL0ezthirqVoYVNSiA9euRCHlPDvyVGp6fULPXHzZc_4c6vIHqC-HZhuq1LtinzWGmifK1Ir8w0igXEprf5dYWWP4-1O2XK3RkEf_Ecyz_owgx32zyEsK7OY72v1wfP9FbhBz8F7j_A1kvQVjvyh0ZGf35zgFRj8cItuXOHrLDbHcrtt7n-9RY8d5GRncqDWx_ZZAaF8RMKM9dDNu7DQXVFimn_M9v6hGn2Mus48HLYpHEDTffbVjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaHDc6-Qkb7iELK2FcuWOhRXIS2GLssuWBwpinrDxAeFbHuQ1rWStmQo9JCnQj4RhVgHpFyXe12tGTqGFi7wdWWl1GMdG-ptXUYL0p-sE6YJBDObCe4Bx9BwDc0H0aOyob8l_gYIJRCr3vJkG8vIdam3tj664lpTaevMk9hzpFESAjUKerx_RCX1vSrTx-ELrE2E8npJzJY1peCAmy-e5P06Ux_uvVCliYh8AVbefUL6ZInTfi7y2SBof_wzNBREhNMGbHkDLrCe0wKVFKO1awJrBVNliYVmm4kZlWAze8A1eRb__W6_RsYkrFXLNRSN2syU507FXyLA_HHEGJKzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhiGdhFjNW0bUeI5rYiPjY7KpHsCfMhw_Qa4mFnEhwPRWJ5W6flL3oEtnt6sOQTpBpA1OdX7STwAVvslLu4XbSKH0oHTnPxWczptDNNMU8o2Vuze8lYQu0kDpp90qdNqqm0BUZw6qGfpcFIfiuok3Z1C_tbTKrefZJ5SJLlzleRJHkcggcAPSSCfX3CChxffIDb43EuJgGGLWr_uuv0966BnUgACHixLoOVGpyAYEIL2j_s9eUoBXWk7qIUqbN1PiHJcMfh_hSM8St5hdtIB5qL9AnKihN-D8d78muMIkhnVSJl84CKM57s_mtVo3qRBfqY6G6i-EVX27PvoGj04kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbVGhAoNlrtuvvaFXHH_-aH5VAD6ogGFqfHRXJoiaj_roEdyFl6EwpdQPmkp0RLcesD9UqLnLmlX6Yq546GDWHBdhpgXNmeUzUbmiK49z1XIM78GJsmXrpcCEoXIs51-B2Dd14A-CFC-nkHnBZQ9yMBKAV8huWX6OfXjYD6MSsiqDQlkAl0OTlWuwEEZaR3ONUI3-m-r-_rBNiDPgZIxFW5oL9RlPznTeifdSJ24o6WJCusXMTrQcU65ZSux8NIDjOJexBINt8YDbnMqZIyOnZUiSyNKK1xrDXIbrq57d7PAsa4C5PL8zPO-dXJOA-UAHkCl3V0hNpXbYz7QqazWQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ0ZDTGHoLQMKtTP_GAUzpYwETK8wgOFh9uFXoTdQKz4TgimPB978FlWUBwR7A8btnqt06tF7UGc-bivtUJTySVmaM41eyEUUmA9EmK4T6sPmHjKn0_rwqlEEg60p31O15BaQTtAqryrK82hHikso9PfAUqOYF23wbpIAXmmMuJnoiQ3H6emDUrB4zC6kVEvckLi-qd0zcwXwemhLSZ1XiN0-sJ1lVSK8tuF0bDANR7LUcoOAx3aaRV3P308DfSxohx0Lx7mWWyEjYppDeqAVcCMLWKXmSUwZSUqueP7_rRd49aQwBe0FXUvhSOyUhGy5od4l8ZuLK7PLMAWfmeD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpnsTB3YAOL0teYGAX4-IZ6-KbfSCg_88XA-aahxy5is2xeKDECAYhMDUPgQ-0wdo0dwo7493ecVP_7vQMCFGFyeCt714x8o8_AEFUi8Cb4y-CUzb2OIWrwQZ9ccb4WX6IJtNyoAg-esHQLBFygnBaSQTT_eNZ454TLAPX-15CaKkoecxS6wJ7-k8shLPg_WyO3wvrGbcoRM3b9TnwXlOVMeFYm9sJiONk1QTomQMLWtrHo12bWryOMoqFqYmV2mblWvHg4Cfjd6jurh6f0WJjblue3MbYusp6Dqx48GjYIWIlXEUFoqiai5xOH-ztOdhY3SPMx-YsgOIR14OJKXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXvY7oWeha-T4M9YTaA6lvmXir1db_EPocMfoFbpynxOpMgkW8x921hW-p9GKlRB0RAQjnWhDNH2P1B6e6PLkWi58uubbmAL1R_wlCEt91FDTuPN3dU3qP8dBqzdCw6FhlbcZW4BmverTj1f2CDETLDU4mTjqRYp4hGn8KRdrSBM0yFXsCFvf9kBL2e-EShwpMxNfYeX1WwtYxAXTNng6w2Q-Qhg2dNRtg54zKCg-QGR7eK5N547XK0pjgnNATyCuxFwDemF67vPpZOiodTl2qSZy9dVuDW3m53rJZgcuYBn_PbxZMM-RLNr23wf_GKy39hmaJ0k_tVBrDonDEj2yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=oeF5I-VdczmgXuFuBErKq81kkJ_hkjHlQdf5JDTXkkHx75W3SXS2IIv6tmhkwBN6GwKUsw1FX7G3IzjXQ5SPAxTgxW2rRdyJXPIu7oX3a3dn0H7Ip9DatSdsT-fl5SJ7tmIGu9ffFSqBR1UFjXK8XI8jCTlmuI1o1-tRVS8ynv_OPeEkzydque6g43fnb3Cv2hxah57FTVaVkNG6Voqz9BLqutA4N6BnJXB9q6I6tYxJmd59aAbYvpar9jFRY6vcZp-nZBgF6Ui5pTXIggsc421UDwvnx5ZUu72UWv8qztt_McH0oujP2K4qyx-L7B1xySdBZq9RxfXe95sl0e4oYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=oeF5I-VdczmgXuFuBErKq81kkJ_hkjHlQdf5JDTXkkHx75W3SXS2IIv6tmhkwBN6GwKUsw1FX7G3IzjXQ5SPAxTgxW2rRdyJXPIu7oX3a3dn0H7Ip9DatSdsT-fl5SJ7tmIGu9ffFSqBR1UFjXK8XI8jCTlmuI1o1-tRVS8ynv_OPeEkzydque6g43fnb3Cv2hxah57FTVaVkNG6Voqz9BLqutA4N6BnJXB9q6I6tYxJmd59aAbYvpar9jFRY6vcZp-nZBgF6Ui5pTXIggsc421UDwvnx5ZUu72UWv8qztt_McH0oujP2K4qyx-L7B1xySdBZq9RxfXe95sl0e4oYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJWB14NtTU-y_2BksPPOr458gRoizDmPxVTea4S5fyvJG2M-9UMTgbUTGc_87qxttylJgZFP3mocwgkhu3eQtyJTyCRNjpy7in5lQc-TTAdADRtOdUWfne8KDuVvhz83HmyoTE8Xjzo3B42TRzv5nY7dxkmmNG_GAU6zVH1p85jPBSwAtnKkTszGSDsmccfw8ZJ79-cVkEz8HKzAV9KxuN-TB_6dqHPA8juiuixmmh3dCPu1FuQ9fD0hnDo2McSnGBjTaxvPxK4JMUa62eUeKZCEUVENfFlZJ7M_stkPK2bV1TrHv6QnoZ-zqPr8lYdR0zqijiV2zsl7ylWD6OPibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V93Dsp6i2wQlMEongoJtXnG0uQuqyBLfBfqFSJt4HB6JDsHNiVWyWmoPguC6Vq89z8pCjH4Dtgzb70GdG0LwnyW2n-QWiyknph_9fIl3UOkvPTjXvn-g4_HrDC3HEdsUsZZXzIbJyL0Tg1Vvk9Yk7IQupUH4LRwoB156asoggTIFuEzCq5yQWaB959NFSee6fy44G0crj7CYBeEDBLMzYi-5AtIQyEJ7HVCvRza7MvfzcActOgqy7Es8joi9WTlI-5huWaNyb6OIRdz-nsiZQwFid5klDnJjYKg3GYMjG5ZBSEnMvzuvVyEJ_ZatWPbEcntpHJbwCUz6vP71NKc8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiG9wiDKpZLuedm9Z9dYvPQ5ZVlSMUr9ZsiMprNELyf9UI-c9Ki1sW11dDiaDO7snGNt2fvno1jkfpc8g1L4M-cgRSubH-cFH9o4L81kq4N-uonELgBzO3p0i19u8lb5eWDCUUEeu1f0EFoW273KJIj06rU1odQR-JrdvjjxQV8ovdWHwOkKvtLXGERg4-t8XRWDd8ge1ehhp9MK5fVD3m8jcOAra_Ve26Ot9gJ9pdq8Gt2-FjJ9DaaY1iMaqf0uojyGiRSFz_usyiOFlq4X9sdikTwa-TSDQ17pDfg8bEcyDYjOM4HtYdqqvjnIkrt5eM0S3DKqChjJWw3v-4NiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfkv5EeTw5IJRCNxkc-QmMRC8nXS_iovEQ8koPjx-VrqKrixT6MqqPeZvzX8PhSD26fXMFZatcydbznHGcB01wN9EXqnNSNbA6M41EB5qiUKcZep2vzzOYkiYs5NToXgpStAKlMH7a1O7wPuxIY0hf73G5L3jpXKPxaq1kn9_IIQFrCZf89_1KzTzJIpM8Ma4APjqyydleIraK7kOPL_39fnrV0buYIsiIMHCqCpuqVklwlplq11LSyr-jqIsxEG9rotJueJueHBwCwE9EQn46kyFvoQg72F___KplUyJtQQNieAtXX2nh1Dg_3ubOciAt3omCqQT5ntpJhoRGgtbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWr8MqDPvB0pc_oijOtmDJUZsrbLz64t2TNlV8fJ3IQeZ7OQHpTlUnOqMn6-TUrlfaAvgDKhs-du30aPMuKWUne8Dhsodf5ih1gxAJd50zirtRBT1jHERhqeESm7wIgbFAFcXSre8zPG9qyzHT7X0E7bcTA79T13vrWUFNfdOibq086xM25buzxQbikU7O5kEMDYQNLXAfqtI8LSqC8CrwuYhhSLcX8qzy09WVB1C8GA6xZX51dvdncu4iSmDxv3ndmJviwG9WK98ww6y_scdFpCTWek6v_KjPvgadMsCJT58v-3tYEW1BwmktdWxz_vuTEunBf0tPdnWJldyUQccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPh0ebEsYAOQZvNyAVS18zrSBsnR-v3sHgb9lcakPpez7hJRDIgza-omrr0p00nJThRJSgvNS6P9OSIYpSKogiWBjOvxmsRtbI8F7DaQWuiuzX3r8h-LxchQMFtk8iRoj7OzSmB-tkMN3bDQ6h2ooyG56vjrKtc9wQyt3Ftq5LQaDOUDeM1zdtmHA3VM7ozS66hepfjkBzeb8bk1uzbxAutq8BLLqgwmgGjYfuVImx4QAEJoD_LeEUs7iSwcF9jfj2FMT_CYqpdxVCgVXv4QwTXYV2LCafwCrapt41XFPcKkvny8rdPmh3qds9E0XPWDWltFeZrDfMobggwHmrgaIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=eazJi-2x-DqHreGAmv25ej9qh3pwvlswmwkaSKd3eu-22w1U7mmgIk7z3HwF6QTGJj1C3yMPHLHX1IhIOB0ktfIn1S7_AREj79LeJxitTn26-qG58QkDm4dlfYb6kbdeedPEd9dzZXKNudSERYASnIJSrcbObn6geSRbRybVweRbZ3Z6QeHiTs6Oio4hUDzYV_D50xfGa8eZT3RtPPrgt2lHjV2YGS7U-0TUFVXpylqj05OIW3SqD8IgfdcBF3Uyrr553QBH9tyDfaXdMyTR7QxoEH2k1jn6EQYmakfhvZ_gih7XvK9tsBS2vdniikOrp6Ehwaqklt9rcx43K-qNcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=eazJi-2x-DqHreGAmv25ej9qh3pwvlswmwkaSKd3eu-22w1U7mmgIk7z3HwF6QTGJj1C3yMPHLHX1IhIOB0ktfIn1S7_AREj79LeJxitTn26-qG58QkDm4dlfYb6kbdeedPEd9dzZXKNudSERYASnIJSrcbObn6geSRbRybVweRbZ3Z6QeHiTs6Oio4hUDzYV_D50xfGa8eZT3RtPPrgt2lHjV2YGS7U-0TUFVXpylqj05OIW3SqD8IgfdcBF3Uyrr553QBH9tyDfaXdMyTR7QxoEH2k1jn6EQYmakfhvZ_gih7XvK9tsBS2vdniikOrp6Ehwaqklt9rcx43K-qNcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=OaAFYnJZUIr5NpS7bjFpA3XKqoAo3JThdMQOYKtlkZImGqDXGi_0Ti2_nYleBaZXtvp2CNBdPRQCTRIzoDLTcf8UZHnJeDl0LZSKenA6Yo-7NbMm223Iqut9tsQafcuzkzXw6isIbjuys9zO-vD_MV3YvKGqRyxu90-9RTh4YiMOSK7PMK2vxhRW0voF_ctlW-BaKA0kkMm5QXHA82g0Cq4ko9r5ocXYA9cvYArX2kJYoiljygY0TEYdnexxqYWY4Y1-xas_O9D8L2s0MYf8mQwtHaABR9KmTepJvh8tUHmgeWEZ-MusHHgVIkfZYMc1hXgSGAX5ARXkqTnByM4c0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=OaAFYnJZUIr5NpS7bjFpA3XKqoAo3JThdMQOYKtlkZImGqDXGi_0Ti2_nYleBaZXtvp2CNBdPRQCTRIzoDLTcf8UZHnJeDl0LZSKenA6Yo-7NbMm223Iqut9tsQafcuzkzXw6isIbjuys9zO-vD_MV3YvKGqRyxu90-9RTh4YiMOSK7PMK2vxhRW0voF_ctlW-BaKA0kkMm5QXHA82g0Cq4ko9r5ocXYA9cvYArX2kJYoiljygY0TEYdnexxqYWY4Y1-xas_O9D8L2s0MYf8mQwtHaABR9KmTepJvh8tUHmgeWEZ-MusHHgVIkfZYMc1hXgSGAX5ARXkqTnByM4c0oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwqUBryijPGlPvnLNTyMRO7jyrJCAAaOuhMC0zlQic4VXUk39Ox5ZGjY_mZeIzrXa-A6MgdiSnjcjmI-TzBwH2qaveBVndJbMhbS7e4mzKmA56pxYdmduK5MOT2lB6o8BA9QDRwIggA21mznnybOTBbLeua_EWQmWSoUo26_Xt8q8GRWXxM2NRh_QHISzYr2Uu5625sSHn4r_YnqLqXfb80z710PVRwT2bBN9Cr_bE3IFHlgJ4JnfjGEy0Op38W8NN2lnVOgmqfBBYPyE2A3uzZ8eSw6KsypTvGKIGbKkXEsFDJj8xhM3M7zMU72mJasaiQGIX4Y_L7EvMXY4dpJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCc76EZkOryS_KukqIwFKx1ad-ELlcNh0yOQBWQcv_BCovC34DVjWtt9RKQLRLgSFsncGV6u7B7LX1Gb0fZsVT3BKssk25Qef6jlI9try9v2AJstZLRfrHlxf-atXHMNBoJ-5Zac08P7PwWx1KUXPjUR2Ug8WpGFVQ4VvA1dmNts2ZQ2HQYexT8gOq2M_d7r1Y5m91yYpMOeeg_tlS8zgZBRGn8TxlWBmyNYWAr6eFNpUSAGRPbOqoJDkP_4hd4VQkLYHeNBclWgMQ6uphTi5xSd0ReTAyI0KfbeersMqrP-VP4-qYLIF-laOci6xxySwTaufK2V-ThXiP-YHLkW7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW0PHToVj54pVHG7_t3hscHay9u7YqTX6AquGQbnoQiCqqy7GMgAo1NaEmnKbIFYSwXAeTKBGZe0S2HMJBX8MigWfNL2Yw6otju_YG44T_dZ1v7Vt2V-20T750ParVI3eHnFdibtKPpvhNfgDFFVOrkP1I40MRL4GgfVfLBsxvAVfhkiuNtL-CYHc88S19AJIsCa-_zvCHwFnF5cmizrMyCsmQ6El5Sy_5YBKWvQCAekp2seAgZMLs-Mp923Mk09c1G-XGHoeWKxIMbO7dD8J6xBoU5ZHb2Ov1knL8ueCnmEJgtziF-PD8AS-OQqBTeAZNA1a_hdM87rB6He1z-f2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=e0sD_GqA59OIms5Cv9Lkb7eA_0XSmn27HLcVE65hfRygLqiYilR15yUh6wSyNx23_H3iOYdV6LNHjvRtBtbcY1AjFmjfwytS9LRo4QX5qW6rNwEJTTPUL8qf9FRxZnDzmG37LGiMIufXg-FYvV_iQqcbaZDF5yAuzEgJD6aPF2iKy8KfdcP5mIaZnfEePWJzwhDegpMPWDRMPYVoZK1Ks1snmSMse_fccf4f0q3aThwTBkiygOU1HOqbWM_W8vPsAkXKd_0ytfPKpa1MPEYFG44ObjyLQUg6S0OpZAF-_QLiL3DX-HoAqd3fNUtIL6nU4Y71uIUPenNZzIlSSVLSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=e0sD_GqA59OIms5Cv9Lkb7eA_0XSmn27HLcVE65hfRygLqiYilR15yUh6wSyNx23_H3iOYdV6LNHjvRtBtbcY1AjFmjfwytS9LRo4QX5qW6rNwEJTTPUL8qf9FRxZnDzmG37LGiMIufXg-FYvV_iQqcbaZDF5yAuzEgJD6aPF2iKy8KfdcP5mIaZnfEePWJzwhDegpMPWDRMPYVoZK1Ks1snmSMse_fccf4f0q3aThwTBkiygOU1HOqbWM_W8vPsAkXKd_0ytfPKpa1MPEYFG44ObjyLQUg6S0OpZAF-_QLiL3DX-HoAqd3fNUtIL6nU4Y71uIUPenNZzIlSSVLSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
