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
<img src="https://cdn4.telesco.pe/file/l2F25VWpSXTZAfmFUCSH5fyE2H9lvUDXTki1qNafgRmMwv7SYpN7V6kpB-eJr4J0enl-j4OPLYJxtPeFAGoiSnVE1ohbNBrfO2_7hqq7KIveY_g_MOmfb_Vl7e0FDdvIzG_ir3emmeAhGQnm3ZrtHA6PlgKDQ6eI_6YVSweJidtiMPePwHFlrtRIfd0XMDIJgZAQN3lzuv2pzRAynsz-kQV-aFwRvj4FOgfmgKlS7zN30jVw2QkKg-iPwalNNStOhJ2mnM9pjpuDo5S_MRuZNdDJs6vjUS_gOzwRs-vLhjdbfqoWOzOTob8IjJqqODac0g07xl_SwH2FmYvWNb4N9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 306K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 02:47:14</div>
<hr>

<div class="tg-post" id="msg-23726">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go--l6Llhrv8p6DH0umyvxuKPOmnaQ9FkXn4dELGQ7gDGB3ICSNmp7uMRm0CSUNqpqlSdzbiT-o7BoP7iz2xpUllIOrhRrVEaEXLzSwYMFg5nWYOoxGZF1SjAl5nK5Ne0PFXf3DL_jy7BfiZ1CXuK26Ude4Ra3zb5pbGloIHD2HXY9hh7VcaU14sc5bfmuP9M02lD05huzUf5IlNK3xC5VrtjOhwfxa_uYAaiy_--nUEHPy0e84SI6Gw2Qj6USn3sJ95EK4A_IZh0t8s3cbvFmJaTi8IClvW8jHKj546xrb8-rXWz-KEaNZIfFfZyaFulnDt-xo9-TEGo8v7AvowAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ محمد دانشگر به مدیریت باشگاه استقلال قول داده بزودی 18 میلیارد رو به حساب باشگاه واریزکنه و کار به‌شکایت و دادگاه نمیکشه.  قضیه از این‌قراره‌ویلایی‌که دانشگر خواسته بخره یه مبلغی روکم داشته که‌تکمیل‌بشه به مدیریت استقلال میگه کمکم کنید این رو بخرم…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/persiana_Soccer/23726" target="_blank">📅 02:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23724">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgdiupGwwGmUAKvX7kh5huTGspZ-LiYB2mD0lp4H_X0ClEHzqBkdw-dRaP7z9hlssf0BNoL7950vv1noz0jpfHyrEu6D9ULqOfv0bUKND_HTGdjvlcIKjawFDdbi5EzlE38rRM-qPZRZwlDSaifTZj71gM3G7KndAu0PqH13pBnbTZd-QbXWciswBWq6l5D2oKeMfTcOs_ZXUXJ0s7gMNZSnv_t_jT9bvvlCRJqVd2PGAIYM7BLVCYuJQ8bH8bfIZay5vvvXbYO7AiQNsP2Vg5uZO7JUABY0msQxM-RrK6Bvj0nRmPW80CNaYH7GhXNX_oh4cftjJucGEVaTviP12A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمصاف شاگردان کارلوس کی‌روش با پاناما تاجدال یاران خامس برابر ازبکستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/persiana_Soccer/23724" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23723">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDM9uyYHSLHqIrsMySUVuNA2jHBx78YGWmgDWt0N_1uBRx66gBNt8z0S6b2Uo6q5nObEg3qhh-mU3c1cu8fn3ep3LjHxFg-HISku3DOV9jBEy2FAh75Ees6G5CIHWv88DJdjcX_0b8qvqpXFUJzw6d81Y05WwCtK8c4bmRwKOIHHg4MO-91-EtIG_c-m6ruE0dOrdGlSxxYAFHPenfyRUZOsGNZoly_VKM_sjveDJEfvjFUZDXSZlSPrb_YsAWoqi8yuYfiRmUt68FlCAxd51XrMWYHONy6zTgzLy9lkv8ghTP4HOO7qAMKwM0w1MrxGYge06ysen76tIOW6LFJV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
از هتریک فوق‌العاده مسی درگام اول تانمایش‌درخشان‌سه‌شیرها مقابل کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/23723" target="_blank">📅 02:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23722">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=s066E8ekt9FstEUrrJAMNfpC-4VPcsNV-SesdsTLYD6Zoi0mxPSBCjOlgo8afPfPlQ3vGBznLhewcyF1LG9_-E0VaSmkj-3d_NVajz8_vCYK-05DguB6XO7ZKLZ8d3Z-Nd8r0M29AF2xKSBTQmtbv5WR3493Q-JIWGtVuxhzaD1U7ezluC8_ebOYrrv15z8SiQHhmRWqLEoxI1Th4ACAxqUADtJzFkAwT8-E0y6O_I6uKvPhdVjmJG1wFP431qEE65WHv4lQuT7OoTAFbd10WqTmq-GPEJm2rRaiJCjV7adR967sYuNVxKqKUrXPYFvLp0u9qMK2fEllv93We21laA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b735dd21e2.mp4?token=s066E8ekt9FstEUrrJAMNfpC-4VPcsNV-SesdsTLYD6Zoi0mxPSBCjOlgo8afPfPlQ3vGBznLhewcyF1LG9_-E0VaSmkj-3d_NVajz8_vCYK-05DguB6XO7ZKLZ8d3Z-Nd8r0M29AF2xKSBTQmtbv5WR3493Q-JIWGtVuxhzaD1U7ezluC8_ebOYrrv15z8SiQHhmRWqLEoxI1Th4ACAxqUADtJzFkAwT8-E0y6O_I6uKvPhdVjmJG1wFP431qEE65WHv4lQuT7OoTAFbd10WqTmq-GPEJm2rRaiJCjV7adR967sYuNVxKqKUrXPYFvLp0u9qMK2fEllv93We21laA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال:
بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/persiana_Soccer/23722" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23721">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=SEhQnh8J2YyocmhuulCPkwdD7I6vuJH_D8YfhlsjX_OivUlGPuXvIYnaMpKD7LDDgsCBC3lzglv90ByVJpNm0OcBvx-7gsGn4_g43fZrQ0NicCUiUhgBeiIWbeNHeJLYquRGF6oBNaOCWbXHYWUU2-ZzaX6OxJXjJ3AV5wV5xhpeKTbYqL7j1z0_BLVLVCQ09JIQvHI_hjRvH84XdxoiOFIqgq8ywt_l9CEqi_8nRl0bZFFzAlWFWhr4uQ_AIEulifOsSrWolaxAR5s73lerp3F7DVV3QMpbIBunv8miPN6uYqZKPM3cfz5dcIuLsmAJ_S6AifzDtvtxUZZiXGosJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e924ecdff.mp4?token=SEhQnh8J2YyocmhuulCPkwdD7I6vuJH_D8YfhlsjX_OivUlGPuXvIYnaMpKD7LDDgsCBC3lzglv90ByVJpNm0OcBvx-7gsGn4_g43fZrQ0NicCUiUhgBeiIWbeNHeJLYquRGF6oBNaOCWbXHYWUU2-ZzaX6OxJXjJ3AV5wV5xhpeKTbYqL7j1z0_BLVLVCQ09JIQvHI_hjRvH84XdxoiOFIqgq8ywt_l9CEqi_8nRl0bZFFzAlWFWhr4uQ_AIEulifOsSrWolaxAR5s73lerp3F7DVV3QMpbIBunv8miPN6uYqZKPM3cfz5dcIuLsmAJ_S6AifzDtvtxUZZiXGosJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی‌درگفتگو بادکتر انوشه در برنامه امشب: باورتون نمیشه ولی من دوست دختر ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/23721" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23720">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLacYe9USnsabjs_cxiVocP1ZjNUTDF7WQJERm7zCs7evWkwYMFv01lkQWEBq3tPvJ8QkrT_TZMg3KxFtCJ12HnekOmaGWs6k0iC5R1I_qJg0fFE-28CF-KlAwchPkoddsSP5T33W6VYd5Ic6i7UN35bUeb8vmLbCP4ST0q5aTg6vpFN_GdgnwHGGUQXEDMr75AiL7kT-TwwIRvAFqBy8GJaLJ9reRYYE_5DTybyFHquXP1FjmVGLEXm-dE-YhpQvpWP6YdvVGKSWRO6kvxOWCF40N-dC3HiD1gfp-a1sMOAzCvKix78wT-iGidZhlq0oDkU-1W50a49YVbp1C8ksA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون ea27:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/23720" target="_blank">📅 01:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23719">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210b9e3441.mp4?token=GjbqG5rJZnUbIlHDG4tTmPzZOSEd-M9rkVT_P3NAACLoc-FLcpxyeg4aF-K1HTd4Y7u00SMIaN9HBDuoGrLQrerjnIvQNzXvaJLBChun6s7jKx9Yf0G7FZLXHEBEVWYzueh1BWe9UNkyXABUaKBq1ohnRefCqSW6x2aztpvIp1ceV8rBPOGGWtc2wuTlN-RP8mL4GamkqEkRM9PJQCpoWxFrEZfecIzfAJaUvkzIvg7MlZsBqK8m3RPt-U0KnRyfWzlUv24LgCpWOjpL75zFHo-aavlSbx8wpSd-KRPcXrl1s9Eh0RbOuH85E2U5JAowsAbRByXOwmCA4vJnax1rZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
علی فتح‌الله‌زاده یا تام کروز در نقش ایتن هانت؟ وقتی علی فتح الله زاده در زمان سربازی فرمان آتش به جنگنده میگ 21 صادر کرد؛ فقط نگاه های پیمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/23719" target="_blank">📅 01:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23718">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23718" target="_blank">📅 01:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23717">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOS7K5h2nMgWLCuPfHWxY0Sbqka4AZkV4BhPB2ZeAsAVXiRJGWrSBQaI4PnZ2Pbu59g7eDmuf7376ExETkhUscmqS2WtSXDHzLXz8V5-_2PaIhVvcoFM4Fcwp_SJkr90Ou83Rgf3WNuCWXJFbkViIOS9Bko1PIAx23uUTPqjkSYTzY-219kI3A4wxrBbcjOX0BwWQj7Dr6vYuQYQXd8y5uoIFOOx6xvU9d0rmOn0TqiBKWWnsH5n_UTYrmmpqpwT_p0zVXPIRCNfus44nnoue7hlNGpApqSAQhzyujos2pLJKvynGKFlQjANkc_w4AiEnOn07iCg47cpQ4vMf8J02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هواداران‌تیم‌انگلیس پیش از شروع بازی امشب؛ برای ترامپ شعر ساختن، فیفا هم اعلام کرده هرکی شعرو بخونه از استادیوم میندازیمش بیرون.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/23717" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23716">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=ot9yDT5s6uHzNFy7HuqiNKoG3498c21QfYIRpWnbdI4Xz4eI6fvSjxpK7GntoxQdYllcQ6QNUkhBapUPyYJO1r1xMlhbBg2rjkTbR4AF6tyA-UGNX-ZeOp_U7n3ku5DVl9B9VAzEptO1aSPSu4bbQvQdVcL6IPcZ_zHoNhgwhRVq9bW-_gDnzrDVgahHh4kIqrviQ5feFGmwNR2QYKiSyJx2jtXMun9rMKMEM4tSfvzbZZFAB6j_jagd-k-jtYbfIkF7bbkVUQZbD0s4IuRof4X0YAc8dNbIFqXFyDXDVbPa0Zc5lg3ne_VO63nnhKn49B-WeCEfk3cMIGReKQ2Kkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d2128a8f9.mp4?token=ot9yDT5s6uHzNFy7HuqiNKoG3498c21QfYIRpWnbdI4Xz4eI6fvSjxpK7GntoxQdYllcQ6QNUkhBapUPyYJO1r1xMlhbBg2rjkTbR4AF6tyA-UGNX-ZeOp_U7n3ku5DVl9B9VAzEptO1aSPSu4bbQvQdVcL6IPcZ_zHoNhgwhRVq9bW-_gDnzrDVgahHh4kIqrviQ5feFGmwNR2QYKiSyJx2jtXMun9rMKMEM4tSfvzbZZFAB6j_jagd-k-jtYbfIkF7bbkVUQZbD0s4IuRof4X0YAc8dNbIFqXFyDXDVbPa0Zc5lg3ne_VO63nnhKn49B-WeCEfk3cMIGReKQ2Kkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌غمی‌داشت؛ یه‌روزی به‌خودت میایی می‌بینی دیگه پلی استیشن رو گذاشتی کنار و بازی نمی‌کنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/23716" target="_blank">📅 00:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23715">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lou__zhaBpNlVBPgp6ACeJ-QZk6vc5RYnahWiK_hqAR6Ljfm85Y6vilpvimpJf-t6UwotjgbiSChWDLQ2v2lCFxRfY8zjIX1vejxpO0ATKSOOYm3o3F2QVhsia743o-YJp3iM1PsPVZWVeu--xIrcJ-7f5-nngooSKZI-Ib7sM6bcDTybB2VRZkzijRenUc_SeBaGtuy3qH2DuCqXNLUgVcVgFkl3RYsJqHEM1hOsm9wz9lxETfeF_zzACuSCDzdP4xEovthzOWsFSQHLwbSnW9SpZ22slWd34tgJbq2MdycYEhzX4GLzc4o-yJgDArgsN5-Sh3dQdpkVCgI3DjXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/23715" target="_blank">📅 23:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23714">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4IVrooT1f1aDlUgTrZOznReB19w0cfScZnFvJSkLuSTBGGlm6ZYPHyICGqrKLghhi2NMJ19iVT3kXbMiOpN7OXf9u3CbWearDQZv7CPJf5MV1Lz1M0IEkKSiT6ENydt0iwg7QkXbAc-Y9_ixB_K_gplnS-_Pfs9kbZ_w5q-WGQa4PCFHBV18PsGN-Dl92-8Tb_5TBI4GgEF8G0XYCvVkxB9kyZcbjS2HvFwVVgaOme-G9mrSzpldQB8DZc8uybAWBniSPME4X5nrAcZBYwL--TSMqwCzXiBBFLyCw4rGHEkSqqzYrshI4gnEnWS8UnTPpgS1aYsYHP0iFZUjzsvGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان
؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/23714" target="_blank">📅 22:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23713">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE5IXXh90LLz9kdM6whiFT_s3tbC6RMGlDg30TN8OFEJVyBr2BK4B7aEH6kpbur2twa5UN2Vv88xDGKtSXUs_gYr2CrUz78qncleY3kIAin2Uqbe_R3Dg89Fqp3BMsdi0V_NceSvFEHo1qcTHvX_wVO3Ocq0l2SZMVIuLu1poRPKwAD7p_4dXK6qfd3Bj4ZiIjQ0-M2uENrCvvGWOAr3FywwF7doXKRTsDGpuQfgAmYnKPVEQp5dAEhaMUNlF03Gf4ttiz-jKq13xzH_o3Y9yhBviD5DR0zcckfnSm-XzDQRWWQkHnH_BlieDNLpGoasqwchHzEGQJ4E_7UTGckPpWBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c30d0c69.mp4?token=cLUtNF8rHTEuq_ks3Wdi-XD3_Ty4zKWgtXDX5TScdVps7THHRQmwKgZzn8eloGBIo0PaWnqTzFcr78hL5yi9jL0JVwOTUXD4J8dfah8Dp9F4nfPSPyLFZBs5fn7zOb49vU8QbdWam-s8FmRdyv1YoWL7GJunaScU2j3fa8tpD2njIClQlCpbmOOzD7A9kpwNfM8XtbzDFtB981Ljei5-FOcHnecCt08b_nvkfXsmBCsxnHUp91IrIKcJtwcUhU9kh4drTiRVzR-swt1amxXJ6b8ZGJPUs3UjCj8Soc5MSjm-1HClbdEvIxcSTa2vv5VoNK5Te493CRnClu80mfxNE5IXXh90LLz9kdM6whiFT_s3tbC6RMGlDg30TN8OFEJVyBr2BK4B7aEH6kpbur2twa5UN2Vv88xDGKtSXUs_gYr2CrUz78qncleY3kIAin2Uqbe_R3Dg89Fqp3BMsdi0V_NceSvFEHo1qcTHvX_wVO3Ocq0l2SZMVIuLu1poRPKwAD7p_4dXK6qfd3Bj4ZiIjQ0-M2uENrCvvGWOAr3FywwF7doXKRTsDGpuQfgAmYnKPVEQp5dAEhaMUNlF03Gf4ttiz-jKq13xzH_o3Y9yhBviD5DR0zcckfnSm-XzDQRWWQkHnH_BlieDNLpGoasqwchHzEGQJ4E_7UTGckPpWBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی؛ توقف نا امید کننده یاران کریس رونالدو درگام‌نخست مقابل یاران گائل کاکوتا.
🇨🇩
کنگو
1️⃣
-
1️⃣
پرتغال
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23713" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23712">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euuuQyDwcQX7zlxN53Dvn7nqbqJvQrsdheug2rI_K0imWh2WYee9cS8sBuQ5yiTYMJn0ReI44wM-TspzUkHSuX2jhDZvetxb-6BaddVesVA_VlnKXTZi_pcrz-e_ECe6m99M3LWPrNwotDZKCswLRAIEhSqiV_gP6OQeDhF9jwdDEEX8j9X9UKUdmIAHrBJw7bz2iK1eHN23JbVYujJ-v3Dzxf7T-prCCrODp_VrfeqzaaOykbaF5iOo9x85_1qiQjv7Km8qK9sBkkwjYrNltQSqD7wC0_tgKOG__oPiyvP28Z1QZzJMJUU4gNnj9rvldz_u0eFUSM-KeZ8M-XWltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باگلزنی‌برابر پرتغال، یوان ویسا اولین گل تاریخ کنگو در جام جهانی را بثمر رساند. این نخستین بار از جام جهانی ۲۰۰۶ است‌که‌اولین‌گل تاریخ یک کشور در جام جهانی توسط بازیکنی از لیگ برتر به ثمر می‌رسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/23712" target="_blank">📅 22:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23710">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lR-_mXngr3SxskxKd18u0xKy4oa0lmmAIausG8d0yZ2VmgcVrwGaJdkzB69-WXzjI4wWRZwR8qPvqCXH8IBQ2TqOKCsruVuR1TEVhSzI8bgpN-2nIGW5-oGYi7XByeKLEbUt-8WhecmDp2cqEovg1ItuUio47WSx-5BUVJ7g1W5hIrYCT5QXOflyiG9gd7Zo_Wu44mI7bSrFGNHhx9RrQ4GigFpHa8DIq9W_y-SmO1xzZryNRLiMystGTemVmE_ykV4bpbv_VHsJpuyQfIkZ8e8z3W3qzmX7yrKww5fGoPGWJjlUI9ww8HjZGPyAeci6IS2Y4TpjBYy-AK21BbLZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bzys081Aqfq_Jy5od3YH0z0FzhA-WNAUn-47u5rAp4WfA2_Zqb2JvQP4gQEhiuzDsErYyGN1aPN4A1aRT49mNrwpCAzo5q7NTTN6xEYfAJoQv4bzYKFwm8YblTRLK9t-yN645TV4tgkQsJ3GDUPJMNTwAm2EeJlLKzN8809bI2qKHkBNcYg0fOTfoI-8ukvCEC3xpiE-2SWxJdEFeVsf1VtQQYQeFaRBOxhpTzbxDYfD8XWB16okAOdIBfRwVgoI-bYRDfgl8bdjs1lYjtEIdMfr_P7yDt8hz0QymII6IMB0toeTEBcV5eTiF0fGxst-Fj5kdZ4szRsu6tseKKFMsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم انگلیس - کرواسی برای دیدار فوق‌ العاده جذاب امشب؛ ساعت 23:30 ازشبکه پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23710" target="_blank">📅 22:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8Mb4JZksCo-9wRixBnJ6VJURPHh-OVL20_o53ekGmZnYhBwXyIEDYVP3NptgH7Kbb8Jid8ddFI4IZkZEIYH8zITklV-aBx1odZ5I25OKPHbFs3zWvK9Bu-Dysxp8O-VdsPN38rAvKcEuj0fo1ZXEVUdibs9Z13xFmxirMM5B0Lcs7Znfyfq-g2TTQ5nnntfxiEgLfqSJ0374qhCKx9Ts2-9I9UihwNNQddOvAIA5NX1KaoibEGgIAMMvbFhprA9hq_YmvALrnuUa1QCmAVbvCwcgrdariJIPHRiQjQzgCW3_jMvZR4pVd9kJw6gL_4ZfANERSYVxzZbZzJunNq9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
رگی لوشکیا هافبک‌آلبانیایی‌ساعتی قبل با صدور رضایت‌ نامه توسط باشگاه مبدأ به تراکتور پیوست. ارزش او در مارکت 400 هزار دلاره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23709" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syonq7zymS4ehoMgebP_3xusXEc4h0Q93vgIV7hd-tS_a1vK-VaGMqyw1NTmRpV1WTWwDurclWTGz7hZMRGx7tlGVtyVaIw1efBr6m2TlnoMKSRcuq8zpkKvHvuGQBmCKEmdwAYhHUSJA3V2ij_q59ooBnnmM0NOlTDrU7x_nQNa_Pwbz4KVxPdf1e-oTmJHK1-K29lQJyP0RSFYF8h_AtzxRLbsRb573T_NpS8enhgBidVgLlSmxZEMmDcPgjlzbIwrRwqf81Kbt7MDawIUiA5h0B9CAHlLEfS74lyxz-j1zpFlRIRwVummJIvm2avpuAqxs2kVkfqJOJog54knGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/23708" target="_blank">📅 21:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaRS39G5h3S1AvA867v5gCWGJurjInEqw93YyQbhd7kU2FE4K4pHvLSMSslsZBSNIrW18q-PsNDFB0wa2vzGyPeV7-t3Y2MLK1keiNncX3AnqLCtTH1BYSVDyUerjmlAiRTXSnhrzMZDvHqtY3RE3iXfPg5jkCfYu1e-30Eqsr_zSJa3edtFGCC9pkLPaFW_eNHpcRbf9WdLshs62nvmfvMluschPTjwuUE_mWeg9BQMJE4SYapS4wJXQ2uUKOoHgJGfhkSK1LBrNqvpU0waySN8v_7EvU6LxDkAd5tce-b4r-3AkqD0RLtXMY3-v0HUJSmidfHb15CO0XJT6-wA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23707" target="_blank">📅 21:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbfaW6H7YWLHWeZQBNZsVo3WteF_IU_0ByEztxNSG5wc0Wc7OgKeo3m4hCB8cFKkC4Lnfyxl6EzqKj3n5VoBlRNlugEAF1JV4rxXppI8vrpXfSJqHSP1GexgHbOpWZNq6gTPDEwc7Vh29dqdTJyON1se24QC6zoK3c72OZl-Bv33ffAOIxMj34MhnGuDRbC_IN2g2_2gjhlXiBp10u_hWvEd2EAvovlmuixsaSa1HPPhqgwHdTHUJZtcZJu33nJ_4smcK4_b-rHIqmkwZeuSHgVzLJ-QAeJuw7-OmhB1z48hJEjSjObEaAYKAxMoVmmmjvC9zqdOs1uCTZnOW0dmFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23706" target="_blank">📅 21:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa7mX2bITL6Nd3C3J-DCS5vHs691eQAQ3qlWE7NPtROfQZ1XIm3MIABuXqMdnuRV-mxrHmZSM-tGjGvPss9jlAZz6FsyISqxS4rhzabHgxJz204t7i3pCLTkvL8XX0h7FrF3412P3F7_T2291sGG0wOzP2JkXzhldzebk3fT_jERpkMrcZYKRNuornGEWhZMUz8g15lrNhbPZv49GjczK0eQ-dDKuWAZdFQ9p80K3Pl9rrYMbJxctX0oiJHt8dGZJuZMBlm1CIGEUDfNav6RR_UrUoRnZHNzwN_Ta2Q93eXLdh83b--oELZNX8cE5EC-eERhavGvIFzH9c6_LPD17w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23705" target="_blank">📅 21:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDprcrPkt13CcdzsfOEcctL-dAkFVGleVqWsxQc7IbxJ7IyierK6LWgLe6J0EaNrgUFcDoQyFHlpL9w_nA7yxMIRI3OaxTB1Mb9LDaMkB1vhE83twCo-ge6vURj7h3RlOtTcgucGpwJWZQNDc9Nfh5Qf5iX90oAFINE1c7AhhvmpbCUuudeUaegVyNozDjBnzterj3vlRx-i3oiytk_BUAZYxIl-lTYo7FEuUw3B4qZ72skKerJtXf05PRd_uANa2aFUVX4J9Zj3166a99CLGAOEGoefyP2ZYy41OzF4mBMuVKPcassKAik0_dkybEx3eXuMKvuYbedMr_ic9Qjg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ نشریه مارکا: باشگاه رئال مادرید بزودی برای جذب انرو فرناندز به باشگاه چلسی آفر میفرسته. مورینیو برای پست هافبک اولویت اصلی‌ اش رو گذاشته برای ستاره آرژانتینی چلسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23704" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwSXe4L7NIVwcyb4x4-oof2ct5T2cglbSE4BIm0U2rZ8zbMsMrotd_JjdgaN2Jec5PDqE_Dsd5-f-LGBJiEAtGSfgj1outZOjhgW19akhcJBw1LVXGBifm9QGvvx1Dt0CxLOkONhkAGXlx5yHw3mqtdMs9AWcik2f3X9IstSFdZXQFDjWRCsH71DKKp1KLRJD4-6gFHzADVXulXlgkRECOVwhJxNaRH8WLj93aHJMbWz1D2-1ojC--jWjzJKrB5ujaIB3zKgq2DmU145R9Q3hYeCGA9IlbRlNZk-zcJTPkACoj9obiZ3pngNb26FehTppnoIBWYKRTeUP3O94QBzqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23703" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_G0dJt6PHz3pNmsOY6mHQyKjsEGIF_i9in__j3PpJ0WiZfNb3m0NrgZ7JVXv4eCi1hr_VjqufHyhOAgVlFALi1DCmirS0k_q2j9Kq_XpHwttH2Bq76Frs6Rh65dI4U6yrYC7mn57029rTbLduZ1R05AGVT_M1YjhOgiV6JwFY4Ma-r_ceL1bHV0zoMhUG9UzdPnwCfXpLdIdIHQ0GBDky4ZMWWJq7DHqCA9eNWlhdWgwlrwCTkd1WJr2lDEsn1Fs9CPITxpi5NpSBf-h3OVac4uGtrVtYm1WJs9pW6_lOk1WV_6GfgHVE2IpUVvLmIxe-81PHzITbnkERxrSpmzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23702" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyO7Y98tLjDP48s_qGd61MTty7eCF5rFhi5hQo0aTVh2CmV1q0BwvaMibkiQ7flyn2UWHl6zKCa9WjBsYQdbNlH8CaWypts2WMtXGwAJykOXJ_UHq4tZvT8-bH5da-VWv9vIOsRcIAxODXX-lEO2yWqP92ycHoJpmZyv5AxB8XWebg9rDyqgrCtGCGllPGlGckEFOtAdpM3XYIO-OBI3XRdEN8XkGHGgZwGixEAGHVyaXCVrHOLlKSiU2t-1qGql2vozdUyb9G2pmQxfH5hYBYASaiL36d9hi5EHeg8t_TyVrh90YitlDMJA6hTMqyhXDeVwa0IcE8Q6PAB6dMBtyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23701" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23700">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUlg2jk1xuvWkBe_GzdXjd0YVfhSkOVf9Mg4QFwQHMscTO7222z11KMu_3LuOC_my-dV-Cy42C8yw6D3maTCk0k0Pt-7wFG_rMer39xDeXx5b-_uEFtX1aWfItMkRbq9NJZO2rQqq6MArihDGySN1sLYcN9nj3yCuPurhF1TCR4GtU1RyCUswmNd_wa9tZfji4sLOR1TVHNuE94KWfOd1Y6azKMPxrlrIYJ6jZDrSUgXwbUvQYLZbHQJ1x2VP4JXjoAG4qu95b3SfQVUzJ22mhJRVLLtaaawK5zH33xRXAUVQLQl3NcfAkVFUIGgNUpHEwImBef1PIF3ktEm9OXXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23700" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23699">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlLtgN1mWu1E17iFKdT3Hp60T_g7g1FPwPRRA7jDivHkowAMr2SJBAFiSpuWNsFcq8lG0dYbuP_Bn_L8NOvsAdRbvHlKIJS680JsenpOcKlAXBFVhu3o2i0m9VHGPEwSzIfKZa5vzXGYxpGc-uSeoonB0bWT6YSyhLwQyQn7__HIOSS0z9rFYA6GYBZBV92HOx2pBAh2Tzj2aTHDwUA_Xsxs-OANlCFlUEb0wgdsG2iSKuNCsul2IGmNhX0x8x8csPJWyr1kFSzst9BzMisWcN0YC8GBzyKwfIg85OfLWOKIY0kAxpQZeM2SwiLQeYojDJmuvqeMtWALp99xFF1-RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/23699" target="_blank">📅 19:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gc7_O53pU1HNlwKDlmhdLQYZhQkQl6mBiuq8GYIwUGi1uyD0MIGykEhIMlKgVdtASrN8gS9z2-M_wjU0Evq31Cgq6r6w1Igj3FjpocmkK_IZFJS3dE-cqM7FplCWkkCaNlHor-DSoNdv6tC7ZDuyZ5iwvlE2gYwOjsqtfHRqielvUU3dUTf55Jkpe1hiWJOyr6Ebtu5adp3uHChEJj_qt5epbxIQteo-7VQ3h0qIwKcfXS2ZPtebGJbjy_uO0gGtkqMNeXFm-juzvl-_RfT6kcQewZPA5K9TG1CT4v-FLITRARxrktEHAswKZoiBmSLbAGOV4AbRiw-EdZO6mW9D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiRga2NFLR3n3s4jwgASyUUrXYMDNtb5pD8NYcH7TVFINmPiqbVOQcSZNAgWjF1L888HYnN7_nNvkrCSuaZ0PRUMisUxUH3dcPUXYsj3RCHa2ezPzXHKLr526T2zjVx3M296S2dAg777KC056ygBHP0ccDY6DSeAEjf8aXFYu1Um85y-nO7LpXa_PX1uG7ooll_LhXQoLzYB28Y6FsAMbQ24-YpTcQeZOwqkyN90uRLnKef25jSXR6AG-lVStSB43hWwcRTICWNGGhh7GIFuZBMCBMaeVHHwUdYLzY_Xjsj6tz3EmbVBW9AgAPDKVpASp9UXSIAsOJSIDhSqgyuH5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی 2026
؛ شماتیک ترکیب دو تیم ملی پرتغال
🆚
کنگو؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23697" target="_blank">📅 19:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7cgx146aSqW5CGX8K2yFfIh7ljXVX5WVd72hwAB_Z_hGVCZVMc4zdR7qdcbS5VkPTeFpODVgZKYtmKPfscpMM1gmQLUOmNtPOIbaKV_o9p0ixFtNHu-nLhy8UI8-LgxWZvk1wqcMkxlw7-1YUZowWLQztjYNa_nAb3c9JKHcnMDeJHMfZP7wJ-UYy4x2xtx0ii7Us46UMvpBmV7PSAd_ascPogzNQFpMb2PCEXNzw8K4cKk83D3k867w3AMmg4ITqlCOuPX-orRc_FKyWjrthSTxRSBD_txP3-FJcRhCV8wJfnn7Ss3XKuHVc85XHU7VB3PPiBaZziDIZw0_YHFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو سرمربی رئال مادرید از فلورنتینو پرز خواسته از بین ماتئوس فرناندز و انزو فرناندز دوستاره‌پرتغال و آرژانتین یکی‌رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23696" target="_blank">📅 18:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kikyCmlcmApVOiizq0S9jn8kOS6Zo9mo4YKQcLIr-Qf0aPkkwnAhycMYl7-5Zt8_p4em-fRFhfWGJnhihKKT-Jrc0R8qGoFwbtMyeSoqu5kcvNnXMFNgLf3BDo_PZGGZacEh5qcEuKQUMzQZyYtV29BMHljgaJySMyDwD4ZtI2Bed4MhCY0clHNyZ6roJ3FNzs3oOMUs9dMYmTOfnwmFVa2FNDS45IG1bqij6wJ0MSYehL5028jl1prRhzo7SDKJMjcB5y8cK1rZiMS8SvU2cGPifr2OGtkOY5O0nryHvYxLuSyI8rNICCgdD_36uslmX2Dj_pgrbjUWTSoPi3oUiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23695" target="_blank">📅 18:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbdehGEIj9a86zUqw2VP_-WoBjx0QBkjX3Z5RTW4AozgjRuSEzuS-547mi4WdtLFO5EeysWEuPq7gzTOls6OIO7g7aobODwm19OPgqx5eLCdK09CQT8g3oIinfnYEdNHbudmYiZNB5noE7xb5NgA3DtZotcmtv1FlZ_-wftDjG3ts_d007hnv4WPKsLLooio3qkorZGJsPxXckYME7YYkvkoW_DmCPFIZNfCKN43aEuqv4qv34KLcLs1rchbOFVNeL_ECrAvTdLMsjRStPAby8RNyq_MJrPpvqkCEJ3L4sZbZtoxSIFg8U7gN7gMnso7_Y07MHHX-xHxsIr48ZmSMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام ژابی الونسو؛ دنی سبایوس در رئال موندنی‌شد و او این‌پنجره‌کهکشانی‌هارو ترک نخواهد کرد. همچنین رودریگو پس‌از کش‌وقوس‌های فراوان به این نتیجه رسید که در باشگاه رئال مادرید بموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23694" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLJAeEFSfXHcu5n82pHrwFu4aOdrrUjPbxzChGS-BkrAtQlwUv8p7fswfuksRO2T__EH304TL19hw_i3vGla-Xe0Lkyq5XR14wCs6j_IXkJCRqq-HWgJxXMG5B7oe3jnbJH3--24P1Gk2fKGpwaW20urYGzG-trBuy_u_Z9o_TWsYVQiAPAwG8DZDxAzz3WMTbJGX3Nv-QeRSSAQKO2-kpqmldNCdI-8hKAg0GFC0ZyuXiPoMbfsBlyWbyEyxf8keT6WMRfveRf2u-xCLhz6IUmxkvWMd1IQ6MXbiuV3fTPQ8aHaOB6kQGXn7JP4--2-_wC1SuXaAkt-rAF35mAt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام باشگاه خیبر خرم آباد؛ سید مهدی رحمتی سرمربی موفق‌فصل‌گذشته این‌باشگاه رسما از جمع لر تباران خرم آباد جدا شد. به احتمال فراوان فراز کمالوند سرمربی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23693" target="_blank">📅 18:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=kOzU7dN1FRI6SeQliO3ZXMUCmJ_nAOLyNM0U-5cpz6B4z0BpSgxnmriGdP0HVCocke3OMcGQOsNfRYFeQJNK6GpBUuTSO2yYGTQShKqAZcbmBVrXBdtedl-cbcfgDUqUsDzRPnka4fdgst8B1s8mzwS_m_ShIOemkerOUTovnIuCa0z-NbcvnncUMRBQntG4R97uNMeFLMYm6kI1906HEOy6WewZq_lo-OSH3gXbgjEugJJHzu5unTrd2ZnpZTNOitJyimPnBO5JN7TThCG83Q4emhO-9pF44934kN6T32LbJmgLodcyv1MEaWoJgHUHyWl2HXrE7MhBkssofj2KtbhmW-SFwHbaBEatehtSP5lhwZsq_qulUUW77sl_4Ivo0NJo_LFDZMRcOrcmJmXFJtl4oLOgzpmszY0io4Jx0VjxkuzKcuQpPheBKk234F1hOPggmhPx23Ro4AF6gRFPLfnYVN-0aRwG4ZunhFktkZDmverS9G03ldYackeT9ormF5X7cgTp2iMValr4Tg7RDOo38tdlIhu-4j1lwqqlLH4UFq7TAd05gqcAwvhHBeGvg_qHUQ5t2-Y2egZDXJI40oYHNIoNi5Rs_HjBoeiqLjE-2MCE24GfB_QTM2xO593CqKmYL5LRzAD-P4RvToi4J9jgshlJPlto48XH4nKUysU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b816759b6.mp4?token=kOzU7dN1FRI6SeQliO3ZXMUCmJ_nAOLyNM0U-5cpz6B4z0BpSgxnmriGdP0HVCocke3OMcGQOsNfRYFeQJNK6GpBUuTSO2yYGTQShKqAZcbmBVrXBdtedl-cbcfgDUqUsDzRPnka4fdgst8B1s8mzwS_m_ShIOemkerOUTovnIuCa0z-NbcvnncUMRBQntG4R97uNMeFLMYm6kI1906HEOy6WewZq_lo-OSH3gXbgjEugJJHzu5unTrd2ZnpZTNOitJyimPnBO5JN7TThCG83Q4emhO-9pF44934kN6T32LbJmgLodcyv1MEaWoJgHUHyWl2HXrE7MhBkssofj2KtbhmW-SFwHbaBEatehtSP5lhwZsq_qulUUW77sl_4Ivo0NJo_LFDZMRcOrcmJmXFJtl4oLOgzpmszY0io4Jx0VjxkuzKcuQpPheBKk234F1hOPggmhPx23Ro4AF6gRFPLfnYVN-0aRwG4ZunhFktkZDmverS9G03ldYackeT9ormF5X7cgTp2iMValr4Tg7RDOo38tdlIhu-4j1lwqqlLH4UFq7TAd05gqcAwvhHBeGvg_qHUQ5t2-Y2egZDXJI40oYHNIoNi5Rs_HjBoeiqLjE-2MCE24GfB_QTM2xO593CqKmYL5LRzAD-P4RvToi4J9jgshlJPlto48XH4nKUysU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌سنگین‌پیروزقربانی به کادر فنی ایران:
من‌ نیوزیلند رو راحت با فجر سپاسی می‌بردم. نیوزیلند اگه درلیگ 16 تیمی ما بود جزو چهارتای آخر میشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23692" target="_blank">📅 17:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dYjBA6p5B5lmoLReS883mp-Jk62f_Ec6pLSX85DHwAkZdrQWpsWpAJ-XoSsu3nYOxoq6ugXCqNyUnZ8Q49CSeZwZkrJJkgeVtj6ayYOcT5vJ_cpBUJXO8OfRJ7H_lvgb7Q47zaT-s_aBpV8z1eGwnAp1hqIY7wb3oA8VtktRHjqODzU_rAF4Gj35MuobnQM58RkcVZXMbRQdsaOuzN2P5MT-ywUue98Fb0dK0pFh08k8gRryexMcmHb6AoYxIzM9W9seXyahf_0vV3d7m2yKDoa7guQ4znMfdwrWHO3c-bZZuGhPtqzuq1lEtqCSY-3ILGPteux8OhmLMZRwXbuCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLzzeM2w3lUo3cAo6F3qTGr428EqwCMOxqjMdulWAQfBeTW2NcUmfXM_B7IaTB2CN-AvBtjzIrj7P7mk1Q6-4zTz9iNHRK-V-7rjPfe4nuJnmzgnfD0QqEFecEvXZ9FFw9E4DUOguJ7roLYcZ0xDrj5AJRoWtdzQjZV3-26CyAXAi_maUBnLfOPARcO6e9aRd740CNqZH7EKuklEip6aXP5yxSqpFX2Qk4YlicrllX4qBTdAVpjlBq1N70Ya9qVmK6ShdRd5OUcgLo5NrKZpGDgnSQJV4x7j18I6mYBUqfMVkks7t5FFwHDlKY4H8nuzhleyxkEQlhQydWJWrc-lXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
#فکت؛کریس‌رونالدو فقط 1 گل تاتبدیل شدن به بهترین‌گلزن پرتغال درتاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23690" target="_blank">📅 17:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnrMEfwRyA9cVNvERH_76Cfo6jkVnGtUrVZVGC91Z9364_996P-SPm9GOUPmFUzXN4ifKpCDgHJkzFRTcSKCReDLiOkqkY9MCm2Dz3gUigErfa__yjFQnJwzjjLXjieJM_7v8LUkpVd_wwSPixWKCecn24clqpWia53eXBJ0YOb5XNEtaOl0e5mR4wn4KzALjd-9itwGALEI9XjK1uemah382iPJ8Ib6NdfC5jUtIzFQysht-qbcu4xdRIiUci2S3gaIupfe3dzS0R07gO4GtxoSyNSliTFAipK_UtGnkNXeLOFxPSFHTRFWHKc9241uHTWXyRIWt-Gs06ytcCNK_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23687" target="_blank">📅 17:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/012fc50185.mp4?token=fTri5ExyIB-vX6lPKmKL3x0QxepJ7AxJGrKiYeOrK01NBshaQmPumyurQTPsiH4rdJ392oXVTTPC0JC-E14JiWQgAhoFv91ZWo8TM59KmHrLEbc_OwMYhedR3aXFuehZDItDzjQNN7utuf_llzJj8gPpPk8yIKu-zPgRK5GOQrIeb8MndBQ0nU4ar3pDEeqDbGeeKJ-biZ_iLQiBPLozqML29DMLfqNjJjqNrWBpunIUg5aZ9yBTK4MblU4bxibVMi5_iBMEA7aEVClWVZzB5_-H_d5CvjBZReccO_yp3vhYUenUM_cuh9qQ6HDX8atF0qZvvi4NdA1ZA-E0lELVgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/012fc50185.mp4?token=fTri5ExyIB-vX6lPKmKL3x0QxepJ7AxJGrKiYeOrK01NBshaQmPumyurQTPsiH4rdJ392oXVTTPC0JC-E14JiWQgAhoFv91ZWo8TM59KmHrLEbc_OwMYhedR3aXFuehZDItDzjQNN7utuf_llzJj8gPpPk8yIKu-zPgRK5GOQrIeb8MndBQ0nU4ar3pDEeqDbGeeKJ-biZ_iLQiBPLozqML29DMLfqNjJjqNrWBpunIUg5aZ9yBTK4MblU4bxibVMi5_iBMEA7aEVClWVZzB5_-H_d5CvjBZReccO_yp3vhYUenUM_cuh9qQ6HDX8atF0qZvvi4NdA1ZA-E0lELVgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خداداد عزیزی سرپرست‌جدید تیم پرسپولیس:
من اینجا روزی چندین‌بار از حرف های جواد خیابانی هنگ میکنم. بعضا وقتا اصلا نمیفهمم چی میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23686" target="_blank">📅 16:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWODw5-a8yr1c6HfEQwsA6ZAZiWK4L8tbZ_mvGWVxf7V-H57K0RzeEMWnRwx4AbiLs-vw8RYe5T5e6GyVArjN4UTAYG0xVxohLajJFucbvfTdkKsjEIcov7I7uBhCA6kVRV40f36kb8J0BiOLcxngxnLzFdoznT5McfO6IxFZIf7BgNQKt0spCclse6MXRO-AXpkntO7I7xOrSGPJjCTlbdjVQSYoWQox6-te3CKFGUZzuvYRgrK5vods8dcxXrW_GNGwpwZCL7A57-2R4U32P6aVarwitmh6kDu3gl2voKtCdN4Ah8f0LcWlPS9FC_4lAldaXMJ3WMpqOTZkpfdaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لئو مسی در پنج بازی آخر خود در جام جهانی
🇦🇺
استرالیا؛ گل + جایزه بهترین بازیکن بازی.
🇱🇺
هلند؛ گل و پاس گل+جایزه بهترین بازیکن بازی.
🇭🇷
کرواسی؛ گل و پاس گل + جایزه بهترین بازیکن.
🇫🇷
فرانسه؛دوگل+قهرمانی+جایزه‌بهترین بازیکن‌جام
🇩🇿
الجزایر؛ هتتریک + جایزه بهترین…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23685" target="_blank">📅 16:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=oKdUM-iGAWT_L7h1xvb02bbAEf-MpwtxdAiGgF_9utvfJj_tmOCSRPcZ0s8qSyXTeIKcQCzNQ5IWaAoLt2TAVqanex1VE05jatY_mocaZ0KjpvW9GdKoJfypaKD_qbJnI2btjAmLM33xAm8EFq1LpIXkNhVsiWCfX8QVekjoLggo0BlvtRjzOleTmonNyOoOBxHTVsZI5CMlaEJ4E0u4dUSwIUcAsk6LTA4xDgMytV0_x3SaSbLp14EQIjb-E6n1Ch3lc8uhOss3Lf9wNhez_EGat7pkIZs8DxsVBSV8UFyFmtUqRfZ0kmcyvMfaBG1Zy5ow8KxN82jWL2-iUhSmCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a3b4e42ac.mp4?token=oKdUM-iGAWT_L7h1xvb02bbAEf-MpwtxdAiGgF_9utvfJj_tmOCSRPcZ0s8qSyXTeIKcQCzNQ5IWaAoLt2TAVqanex1VE05jatY_mocaZ0KjpvW9GdKoJfypaKD_qbJnI2btjAmLM33xAm8EFq1LpIXkNhVsiWCfX8QVekjoLggo0BlvtRjzOleTmonNyOoOBxHTVsZI5CMlaEJ4E0u4dUSwIUcAsk6LTA4xDgMytV0_x3SaSbLp14EQIjb-E6n1Ch3lc8uhOss3Lf9wNhez_EGat7pkIZs8DxsVBSV8UFyFmtUqRfZ0kmcyvMfaBG1Zy5ow8KxN82jWL2-iUhSmCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇶
#تکمیلی؛ آیمن حسین مهاجم تیم ملی عراق پس از ورود به‌آمریکا توسط‌پلیس دستگیر شد و بعدِ حدود هشت ساعت بازجویی آزاد شد. اتهاماتی مانند همکاری با حشدالشعبی باعث دستگیری او شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23684" target="_blank">📅 16:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34750719a.mp4?token=iI7XZ2PTzJf1n5pSJtUTROmy0GyPrh8DvZQAPaf4q4HSDanrHvSKwzVetpTLEznPx6NPspcWNv3ofhZIY8T-1BPsTGwWcqzWUbwrsSCdBeTqvJoKVNvIQ6yEHE5-yh2yqboGiyWTpQ_e5c-uFRX1Buc8Y5Pfj4QHqzW5m874Kp4aweAlN3YC5P8LAVyBKPwwZrkqOBpfwCcGhxb1qMP80lSvvK_lBFIO0Q8-EBi4mo5kutJen-2iS3f49TCreji7bztwnWtPTY93EdyZWfIR_Ovkfb9gcK9eZtT8GIXGAq7V7rcVKVPr3xnnHslaj7QwAVM5t70Ckebk73ypQJwPXarVBuM4_PnWDCCM0ZKyh07Omt4tR9geXDm61iihWMADdaO15P5srLY6Lem2UW7k_X9YsTIPpOlMOdQyrS1-8SmcWR4A90SU8prkzU6DOyYSfJz5WkSr5qSOiLVVGQWhFJLx9T9JAlj5NU8Vkp7QdaLfKfYB45too1fBkpuMtqGwhT1hoEN5d0sEjE8QnlcF4hVqqW_S5M-qB20UJBja4zwcudWLOfdrkJKe19RhaGsOIpcbi-oGvhSlxctn_MVNqBZTzJlbe2bnmR-DaRHrVjlnQ5xnm3VTgDhC2tmZViVaO1Kh_W4H3qURoEzCV8IL173GBR58_BWj8-bway7zA2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34750719a.mp4?token=iI7XZ2PTzJf1n5pSJtUTROmy0GyPrh8DvZQAPaf4q4HSDanrHvSKwzVetpTLEznPx6NPspcWNv3ofhZIY8T-1BPsTGwWcqzWUbwrsSCdBeTqvJoKVNvIQ6yEHE5-yh2yqboGiyWTpQ_e5c-uFRX1Buc8Y5Pfj4QHqzW5m874Kp4aweAlN3YC5P8LAVyBKPwwZrkqOBpfwCcGhxb1qMP80lSvvK_lBFIO0Q8-EBi4mo5kutJen-2iS3f49TCreji7bztwnWtPTY93EdyZWfIR_Ovkfb9gcK9eZtT8GIXGAq7V7rcVKVPr3xnnHslaj7QwAVM5t70Ckebk73ypQJwPXarVBuM4_PnWDCCM0ZKyh07Omt4tR9geXDm61iihWMADdaO15P5srLY6Lem2UW7k_X9YsTIPpOlMOdQyrS1-8SmcWR4A90SU8prkzU6DOyYSfJz5WkSr5qSOiLVVGQWhFJLx9T9JAlj5NU8Vkp7QdaLfKfYB45too1fBkpuMtqGwhT1hoEN5d0sEjE8QnlcF4hVqqW_S5M-qB20UJBja4zwcudWLOfdrkJKe19RhaGsOIpcbi-oGvhSlxctn_MVNqBZTzJlbe2bnmR-DaRHrVjlnQ5xnm3VTgDhC2tmZViVaO1Kh_W4H3qURoEzCV8IL173GBR58_BWj8-bway7zA2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:
که اول نظرش رو تغییرنداد و پنالتی‌نگرفت. دوم اینکه آوانتاژ داد و باعث شد کیلیان امباپه اون سوپرگل دیدنی رو بزنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23683" target="_blank">📅 15:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vvC6MaXBQEsM923EGlHQnG95JHnxWDZN_qoxXKyPACsJoz9v5LX1upTzO-OgN0em6L-yE-P38E0LW414ppY-FEt9YPcWp-7-JD0VhI49fmm0XAaPaygx_Fh-6ontf6d_5fxN1zRKyDpTZkB5QhvT5cISOHKqnmjY-8r2zF2kbMjmZ0vEQBrLpEeUW4ZgfH4Tn8IqMLOP5fyEkEgmIGIhdfwWEl0ocjazJvErtM1cPcqnBI-01dR5TF5m4CBDiuom9BYDfBULyyKxhynKyhD3hHIdm6PzL4z6Zi74dmHxgYJTVTJyGY-ySJS9RWDoVaINKPWWWpumoELk8F0qz8-R0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/167bd8b41e.mp4?token=vvC6MaXBQEsM923EGlHQnG95JHnxWDZN_qoxXKyPACsJoz9v5LX1upTzO-OgN0em6L-yE-P38E0LW414ppY-FEt9YPcWp-7-JD0VhI49fmm0XAaPaygx_Fh-6ontf6d_5fxN1zRKyDpTZkB5QhvT5cISOHKqnmjY-8r2zF2kbMjmZ0vEQBrLpEeUW4ZgfH4Tn8IqMLOP5fyEkEgmIGIhdfwWEl0ocjazJvErtM1cPcqnBI-01dR5TF5m4CBDiuom9BYDfBULyyKxhynKyhD3hHIdm6PzL4z6Zi74dmHxgYJTVTJyGY-ySJS9RWDoVaINKPWWWpumoELk8F0qz8-R0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
#فکت
؛ تعدادگل‌‌های دو شخص حاضر در این تصویر درتاریخ رقابت‌های جام جهانی رسما برابر شد و حتی ممکنه سمت‌چپیه از سمت راستیه جلو بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23682" target="_blank">📅 15:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Voz4aBbQXDgjeH4NA4IJ6aM_49KkfzzREG9jVzCgIkToZUrbzTrRZRsC7BqXdnzNKPy34NBq2oUvOTCWwbl3iUVdgC9vjfuhjypgl16Jhn2JDIVHsDUDhfKYntvy44jINIPgsSpZO45-CcvpfmwddBoS6aIyXFR5GukimmQTO9o8k4iHTVKflECVvYoQlKD88SYRyiDswYg5XsiP6tCpDzvETv0fEUy5oYIa2AumQwZl5ZVS6gYWpIZJsqiHtKc_7qsMjas5dm7Mh-YBdjiT66kIEaoKJRE0Is2S98pw0vgi6gJRADQ6R_DJOZL6ZiQWDFN6xFxSf3GsC8rKByhHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام 120 گل لئو مسی باپیراهن‌آرزانتین در بازی‌ های ملی مقابل تیم‌های ملی چه کشورهایی بوده؟
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23681" target="_blank">📅 15:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrcexn35bLD4IxT9KZJv5ri5pLy5m3b80X3bLvOYZ_V5WssKCvQNpG68Dzo29bA2jrKt5i53AFJtTpiAYzZ_GFxMYJQ9xPGE9PeDUTbFyR-uCEAfmXhRiloBDI9dmTSN3pShxz0CcHMRqZmhDFSwRy7J0nkGSO2QL6oILZa-yjB7F_fAv-_LZyjoMawXNGfj5X-DJaK5nfwacvLoEV3BgpLMEtICq1FB1SQCptXIMTMiiNm2RejFhbO_it5fEAuxTKo9x5eRxdgJrRE4SzWoSAb-H47vHdysf-2AEPPQy5oFmVy2K3ppF0Y0Rk06JxQSbjE32nRMGDSswnfRaxHcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل پین قرارداد یک‌سالش با سپاهان به پایان رسید و رسما مربی آزاد شد. مدیریت استقلال او رو به سهراب‌بختیاری‌زاده‌پیشنهاد داده‌اند تا درصورتیکه سرمربی آبی‌هاپاسخ مثبت بدهد با او قرارداد ببندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23680" target="_blank">📅 15:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdBNRZfHWae0d300VKix1kXlCGQgadTGwCHl39yLO_a2wY0kR_BaFCVpIz-YHpnVdL7AkeSep4__60QepgXhCmalEMUoluqmKMrvpo1lapujbka9Z9HeVCJI7NTXVeKFIGsZrHCkq4cV5rhQWyNG0n3Cr1AvG8u0_8Nk2Jh1KrqbW6b_flElRUDQBeGhI9rzCyKAbCit_bOTN7znFBx6J5jEBWQ6_PnnrJbSHEZCz-zK6MxEf9iaZuyhpXrmVZfXgGsh_KDFex7LjOnYFbjy5aOV4nqp6EG89OBZ-zRB1e_XRM8zfgdU11DeWq-JJOAS2uKeSfU938QlF0CQq_0P9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23679" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrZ5N24UG6rd86V7cK9j2wR-hRON4b4cOW2VBiip9gmNz6uvvxXYbYTlcTAhj41IoFOsghnIRAW23zqu0ky6VHTp4MT86cu_1Q1X6PTEqgZLWNurObQQQiBvFcoVfq40yzlEB70_R328pATjBbugHEI1gDVXSF1de-jGA3hf14T0P1g1gJ3NWVmpQzd1n2chnQ3FbkyuZoiXn124pRXNw7RgM_eTNSoJZllyUOdpJTVhKQ6S_bA-BVihoF4BRpJFOEzjWQNcFAZp06Kwv5JFwYjwTLIdZAG9fo2bMmm6u1kGuQjlFTOPebv4bRNVEfv-kap5C1zWwJPaFbttwmDK4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23678" target="_blank">📅 14:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvtkJSyVf7b7GjRa9R8BGNU6h34pITFwGBycP4wXPNSLvviV751fBxefYyFcyqnKcnQMhNtZzkFv8k0CXV3IRbmPDYKSa_0Goht2i1gYBep0Mv7BzHg5zjNEDD13A11AexxVlvWLrYmU52tI6C-Xk0WVxeVgJG98ghn_-ktbUUo1XWKuhgZny1hraNDOe_2haWS1icQaW-NdGW--RhtR8rikotYsvnB7kCI1YU1vs0fyk4fz3esWbbuqrsZyBuBT3BDsb7fkc1oY-E9KR-v7nvm-3LeuvrFXRdzELC3Oyj8tT6Zg9C5DRjWvjAAhg4cH-aqYXdNa-WJ4fMcWVFPpsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌هفته‌دوم‌رقابت‌های‌جام‌جهانی 2026؛ دیدارهای این هفته روز پنجشنبه استارت میخوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23677" target="_blank">📅 14:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK6am3OX09ylRbqnt_7V3mE146s_nhUC7fvu00IsCS0G5l52KUTKEJsw5XOPzC6b_eq_jW5eqm33Mp8upp9mpxFs84jrt7LI1F0-U8Vhb02omTZJgQ_qx228Sm16Gt2fdUGANW8hpH4eENn5d3AHj0psLqPX3CgplNrXt6g_SANMt4-1Ed7fvmm54N0RumgLxxIlKflKxhe-VpoV6jiEw0pVuz9efBrpJPxnqHZnIACPNLTSLnpgxM7NHcb-4-TnuHZTwDpCPM3tGVptTx6xPM_W5fx-LTG4AhK_65oJt5ygw9qmdiCguy2EZ544Dq7gmo8uYURJ0bCF5iYo4H3NIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبرنگارESPNاز پارتنر ژائو نوس پرسیده رویای چی درسرداری؟ گفته‌کلا دوتا رویا دارم یکی قهرمانی نوس با پرتغال در جام جهانی فعلی و دومی پیوستن نوس به باشگاه رئال مادرید در این تابستونه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23676" target="_blank">📅 13:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=S0wJ1GxkR8uMSsQu9G-8rVdD2MvVn3Wc_d8fXzEcke4FOWgGcpmoLI6GYwLE_O_JBuiO4mBmFx6HOGfFnjAE9E3q4yW7gh5Tbu58dNMMIuvA5237igqp591_CybbJyqKwY7MyA2LIQ8Keay9Y-O45JkWYR-HobjKHq_r-e9JJ0ugndqJpREhySQb-nsySfRdriOOyefpjWLoxr5yTfe9zpLGtuaYkWnUYASoS87LlVmPXs7CNXHYLwQADRJKIM6z6f5nNI0ESae3tf5StA8MELBqUILeiGmFa1J9YyLt16AEZxihjRfIBKqXSHz1Nw5L-uW3v9aJ3kL8R_yCEFtb0mQs979EEvIyl4Xh5S74o1H7We96_g9Rg9hdBQCt8FkwZsKPY__-_lnfQybbmNXNFa4TfcfSismdEmuJtyNqw66lywmZSoJ8YIiO21TVZPrIzoF5bcD1WuN4Eq5Qb9SDohnyGKrZIkvVFobeJJ4d74cyZIE5es9R8oVWJbF34JFmCy_RLAS131dxZ5wV-mNmrN645L1TJ5y-Mu-dC7WeXHBp54SMbCQAFrIo21nbSejQuZOh4CdQRNeJ0JylipUgCjc-wNcaqTa-PtDFvtIkMAm1VK1sdgkaxk_tdE3Up08YDmh0NnRnYOpm4D1N5eM04PceBvp8eUcLGe52S1YgyK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa85532cfb.mp4?token=S0wJ1GxkR8uMSsQu9G-8rVdD2MvVn3Wc_d8fXzEcke4FOWgGcpmoLI6GYwLE_O_JBuiO4mBmFx6HOGfFnjAE9E3q4yW7gh5Tbu58dNMMIuvA5237igqp591_CybbJyqKwY7MyA2LIQ8Keay9Y-O45JkWYR-HobjKHq_r-e9JJ0ugndqJpREhySQb-nsySfRdriOOyefpjWLoxr5yTfe9zpLGtuaYkWnUYASoS87LlVmPXs7CNXHYLwQADRJKIM6z6f5nNI0ESae3tf5StA8MELBqUILeiGmFa1J9YyLt16AEZxihjRfIBKqXSHz1Nw5L-uW3v9aJ3kL8R_yCEFtb0mQs979EEvIyl4Xh5S74o1H7We96_g9Rg9hdBQCt8FkwZsKPY__-_lnfQybbmNXNFa4TfcfSismdEmuJtyNqw66lywmZSoJ8YIiO21TVZPrIzoF5bcD1WuN4Eq5Qb9SDohnyGKrZIkvVFobeJJ4d74cyZIE5es9R8oVWJbF34JFmCy_RLAS131dxZ5wV-mNmrN645L1TJ5y-Mu-dC7WeXHBp54SMbCQAFrIo21nbSejQuZOh4CdQRNeJ0JylipUgCjc-wNcaqTa-PtDFvtIkMAm1VK1sdgkaxk_tdE3Up08YDmh0NnRnYOpm4D1N5eM04PceBvp8eUcLGe52S1YgyK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
عملکرد فوق‌العاده و سیو‌های محمد العویس گلر تیم ملی عربستان در بازی مقابل تیم ملی اروگوئه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23675" target="_blank">📅 13:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQYnG65yFSlWhFwk44E-IRN0-Q62SEdbsYHBVffD0_Y--H8BL2NhI_wTWcudgmLWJvA2_SqarRFLfzmeXqdH1JLKmd9nqqdh6Vypb0o675ErD3TIjsdTXYvE3EM2bqN1q2OQFpUm1f42e02_KobXvllKjc_y5ZBjoQjTYJMiK2Qf66Wm-oO2D5i-xLguUA9V8neEbBE3zKOLnkyRoiFoFSB4t_R5k3Wl4wfiqbxYy9uJNEzKDNGqaZDz9uRV8XYyGDl5oLhj1LSZhOBRVUlWdQV3qUTzB4sSL2B0uHKq_BiWttDV47LWfXuNfPwVNUPtyeHW2qbFqi1pyxqrAcQhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ آرشیو وار: خطای لیونل مسی روی بازیکن الجزایر یک کارت قرمز واضح داشت اما داور تصمیم گرفت این‌صحنه رونادیده‌بگیرد. شانس با لئو یار بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23674" target="_blank">📅 13:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2CuAUcLqku15S1D3RFouAdRBzIBsESvOgTHEQje6_k51KDvsBvsiNnSe5jqEy80NMW_znwUXNa4aCj3vEeIwjO4b8u6q8J1LB0R7uSD_fP_Iw2qaI1dgPiGSC9ZiM2kj579TPMu7HpyGN3G479KiQXa7t9PGrdJjjo8f5w1LryQ6ZKJJRd5vOp-sHsJlVg8dlEN1WmCarEuh1Z4yejw41MblnY9NSNEGwsVUOF-1X1chUIEitynJ3C2qAYcb0jDlsWr5t3moV2TIPymmQDUvBY4Vzpw1E9q3x_Qo_AWCWQKfF-fEwZ7_pYioU72jjBl7KPLz7lB-zETfkwYZ8Y3rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
خوزه‌فلیکس‌دیاز:فلورنتینو پرز میدونه برای جذب مایکل اولیسه بایدرقمی بیشتر از 150 میلیون یورو به بایرن مونیخ بدهد تا راضی به فروش این بازیکن شوند و قصد داره همین کار رو نیز بکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23673" target="_blank">📅 12:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkBRYdw-kttbQCNPB9Dt76Y0UhNMet66fKX_7NsRDDzLJH6KOUvQwYkJy5x2MsxGAVJ8myXiMUghGJwIyFbUvQaeTbfdR7o6JlRx3BCtetCatqhQW6UeI2rK-0_TG8-7f818C-yceao2XWMSgAaa4ttvFL2HgoQyfeTpAGJhkm4mKU0mjdg07yn4WDxrUCjkRCrKCYraBkLg5Jks6T675_NfsxOlgMffmi8xujb11lvSbFuc9ArzJqwaLYYrxkZYf98AurGO0-zCqxHHMRHI8TCZm7i4jvDbdJLTYO0jiK0hK3w_3KxOiFv1vfq0pDwDi_GN9mbbTTjvyFYJt8ojQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ برناردو سیلوا تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده و باشگاه بزودی پوسترجذبش رومنتشر میکنه. قرارداد ستاره پرتغال با رئال مادرید 2+1 ساله به ثبت رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23672" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkDfxQyo4_QI-o3xxPEqza37s6r3rD9w1rgOnp34zluqiDAikqusUKWDJ6vzoJ4RDAJxhlRakCDg2bXuO6sz8b-v7xL9pRRhfV_hvgYtaUF4G0l42YuVDLUajS5RNs_QnQz1r6UdSC7EtOfv6KTbrVmUNQWKxDdCEv_Ll2LUYOy5UDr7qWVs-wOvuHrf3lwEgguU8M81yqVsssZcmPvBfFHHYuPSWES0lKYWL-vUPAiGGzIbS8ADGEknJZ4nSmSB9jWL8XdCAMxBo6R3uVUuxSC4u08o2ceXrh4N4mULOaK1YeoHMqsNpYF9SUT052nfapEFWRboJZhf6ee5xk6yRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌ پیگیری‌‌ های‌ پرشیانا؛ پرسپولیس پیگیر برگردوندن یکی از ستاره های سابق خود شده. امشب اخبار جذابی رو در کانال خواهیم گفت. ساعت 23
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23671" target="_blank">📅 12:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZqIw7gtUc6vV6Ug1LDYOcVeLqZCeJpV6idk2mSR4BwLoAlDe-w2qnq7-4HHzn6QkLtKHQXjfoy1ONaSfqEmGJN8cQiVKDsVVyKV3dKT9pUEVmBeNC1dOHbZd2lmuQa6QduyDgcxXk1i4m-OAcW8Dj2u6VEmF3eKP4tHOHkn_fiNUiXhmtZEpyGv-faZfq3sHHgdy3yVN7etpCgAA9gVv-XR7pTr4Em7qzEsXZn7ebURemDmjC6-4GQq46kUOg7tPbXUE7-nvlUwjUIRhav9-cgMKfarbbd9f7QXbDnZ5lvNFt4mTf3CBe5WFqwc9UfxaYoR6hbUvYkjCjYymAdmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23670" target="_blank">📅 12:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgUKKC9-pZ4v1iuATwllLPq9HTARp7uA_qce8VXVLOFhAdUIA9cPxzrZN_tufstnfMbU3luw8AXWV6vKMR6pdeWos1HxZXKLwt3dbjIzwnMEza1hns7sXLXA8jM7HHQxE9xtJHujjt5vGTT-s1S8Q48IXbPdGGkRKbmtNXFGruaNv8FQVUvwS1wOP2c9vluGNtIMemS7ngrNLunUL1wnee4mdGGUZHyMlWP2f7Hch1568sd1eBV2ypZOHjet0lWtceiM_iksO63Q_RQ1dCZqxs4XBbk1LQr2-8yuAxIXQiZ6SIfsiyaUwh8h3tpiz4PRFHon-D8q4njYMn9eIcTyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد محبی و مهدی طارمی در پایان بازی صبح مقابل نیوزلندپیراهنشون‌رو به هوادارایی دادن که باپرچم شیر و خورشید در استادیوم بودند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23669" target="_blank">📅 12:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bB2k025FaqBemiVR4pOQ94j3uWRpxY7Q2DJ6yKmQsb5bJ1f7gzRz-63qVEbTySuB2clSoJCU-SJp2SGdr4-29JjgA9it-4pZDOZTU7be0qOyIuS_1CcKRXksxZtxvmx7MaORT0hTZOh-hEZO-8SDnYgW3pS_YR9UWvWHwjRN00rfWYfUdie8Nio2nOCQqVuA2HEcHzhV8VWU9ldW5--kPyv23Xj1TaGruZ4BKlsdQ7eNYI_hdWfNyjkaLt6KG1LqfRvnIn1jFVNlFFEa9XgEOdVGF_ZHnHgnLP1Vb7lo-SIODFYSwRJXXKmlHdoFbm0Kl2M_W6mFCPrCwz2qMGiINg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌پرسپولیس بلافاصله بعد از پرداخت مبلغ  توافق شده به باشگاه روبین کازان از کسری طاهری خرید‌جدیدخود رونمایی خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23668" target="_blank">📅 11:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arhlNx97Gew444zhKATXnC0wCbkYfH9pePg-StqzsuxtfiJK336CmToxcl8IVhCaLzDjYf3ee8OcZQbF_zk86pVzHZfmCIFDhYfVXmGZkMwdFRhLX0ETgBIm0PFT6Mlu4s5Sd5kJslefUgrVAMLJCFgMZX4WEpZbFUsOSbcMJ8yKAWpNtHJTnVnp5jSOlhQ7On6of5bnywj5M1slOt7GNRtlaT20HKtciV2YmxtgaNVUpgIBtXD4NZn8H-uNzF_OfKqDqWx0_12l205m6p5oW7y37736H6NnK1Cjhh61qcctfmmUn7wCdQlklIwziqCXwKcDYz2z8pwlx5GwruuRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
تمام رکوردهایی که لیونل مسی اسطوره کاپیتان تیم ملی آرژانتین در بازی برابر الجزایر جابجا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23667" target="_blank">📅 11:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23666">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNtiMh5FojaLdPlRBOqktru-zk-KkYZGpL4anSQaFcjBfapxpeE14miYE4vZA1z0PqWxNmQManObPvWR-IR3k678WHg6mohW4xVsGn51Ow-Qo0BEwH4t55XqNX0_8C84CsbsKz1Y1ONEN39JJVK3Ys2T3gh_WVny5n8jHFdBFUHbeIXqxsbjmKlyGuIPAgh4ff4p5xRXloS7_nBJ_6cFjw5HZm6l7yDrbaPM1rgY7xeeS99z_Wi0o_S3jaVwg-WOSDretUAzeKeS2pk8ISn4DhiHssPwX2GqBFjzTlXya8vPZGODA5RUskCfdbAB665xoMFXsqK89S36jg3F0jmL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تصاویری‌عاشقانه از زوجای‌ایرانی در حاشیه دیدار ایران
🆚
نیوزیلند در جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23666" target="_blank">📅 11:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce0v35_cNFSg_dLwoEQXmwjy6dLvzMM2lYRaTpA1f4vAo8nWVY6eUYPbEzOl_pcf9EU5CDByOx4KyyXhkfcnVxM0pagBYinRmIeItt11pd-GeJSJHpCx9EM9CoiewnOPgruOMmvWuGldhzWRCGVeVir74qgvHJwuZiWhZDVDS7AEiXlBf1wv9WLkGHA1PGg98iUB15WdBxqpz5350TzsSQshiSfz2tOi_nv95ST1tpRmm4rJ5618iCPK6g5sl_6OprEJk9jN5PBrXrvU6v-enG3NuPmj59mHs5UIfUzS0VhDbrv7a3epCWr1hwVb11QKnkS692kkLtYonDXw9BqMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
آنتونلا و پسراش دراستادیوم بازی با الجزایر؛ آنتونلا در پایان بازی اعلام کرد که بزودی همسرش رو سورپرایز خواهد کرد؛ بچه چهارم تو راهه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23665" target="_blank">📅 11:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6jMlpFTxQOAlcUbXi6RYvMWILHHMH4RsR0EmTu2VpzK7iuQJHpYs_KJaJ__4eZKgKk3BOKI3KMYhYyvk-7j30KYNYRf1U8tRfyW7npAU7p-uV53vdpFuC9GZNPxfsfMa_jkTefENgvlTWfgKcY1EEQNnhpqffiOx6PuEh5J0cd3VQOJZPK_DgjxJWKbRMT0c6dbXoz5L8rdw8X7dzM2dvVBePYmc7tT5z9JdE_EQtS3dAWTHqFRFdMUtz0lo01Rtro5DlsX2vvHPG5Uljm4LK7DIFWYee2eE0iqmDUiErYZEYIOU6Q3bisPeyDHkb5SWIhQFy1Dq-b1CTl5I7ipcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سیدمهدی رحمتی سرمربی خیبر خرم آباد بعد از اختلاف با مالک این باشگاه از هدایت این تیم استعفا داد و به احتمال فراوان فراز کمالوند یکی از بهترین مربیان ایرانی‌هدایت‌خیبر رو برعهده خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23664" target="_blank">📅 10:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9CpcJd5eFeqBi3qjZSYNWaK_-SXuLiofsvCh3D0aTHJdFFPbsceTh4CO95uRY5_ElXpdd3EF6Z3yvxvV20q6C2crzbtey2T_o8M29xVa00CMkd1ziWSLKQZVBuiaXdMJtbvWuw8Y0WiFacceBOZA1PlbMbFq9GHy1U-DvVsiUYKueXL8BpZQJd5uR_GltTM4gdfLTLLqijcr-4okB5TZ_QSQWGwuBB5U_dAnO0WnJIQsP1df01oLzBe4yhjPQ5DC0oZyRTrA_Vsx5jqHksocbuSh3kztR7xYW3WxmvkpsnVT4msVDnPWWkhGL4JTynB4hBjxWSnteHKMWtOi44vSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#فکت؛ لئو مسی با ۳۸ سال و ۳۵۷ روز مسن‌ ترین بازیکنی شد که در جام جهانی هت‌ تریک کرده. عبور از کریستیانو رونالدو با ۳۳ سال و ۱۳۰ روز.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23663" target="_blank">📅 10:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWkNhNCRzIxEIFBgFr_iZ7_ODSobftIZpiMzPRUBxN7ANMYR-bS9WgLW06BBVyQbXM_8gcaoXqirKaAXxgZCZvSbWGpxaxAoXZXmQL8jIzAFrXF9Ka20zvVOGnnWTLfLiEXqad3SFpJTEOFTdKgII6tF9ZYc8XuhzmKMSaSD4r7fojgANuQHMiWQHOj1cYcOCnf6Rs-eek7m6gPstEG1ZHKu7hKKv20kr0qJiDDGc9c3DYVhnI9NgvVT0x7Fd2kdV9HbZhQTnD4DgBSnEtirVhoCJTCLPlfJb6VnxmdPZvJuRx9pE97ll3PBXpfX7qeZRZYjvhOU3qQa7y42p_RZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMNz8Kw3TZphUWUacmxoowuME6NSNlWK0XHo0lMSIhhaxKd-Gx8wIze6p7shEn9DAtdpg7kgNs3FGWiuG4sLNXjaYeTGEfPICOEKONC7V9bD1mm7_J2fRyRSJIw8FKgOcuFh3BfnuhqWtkZ8MMyS_FZTatP7AAyS7DN88T8nbEXRd0RfDN79tx7OfeBtAMa8Ta39N_uISHH8MB8jGIEX69_voL88b1Nh6-P-De-DIWHcVV4eZqnduAUuCt3dtWph-tbuIuXq3bIfV0BrQmeTbJVtGgUHZKAkAARB-Iq8beb9WHsdgMd2Ytl9Iybqinh7eJWYyAOzY3aPZEgGC5DCTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
دو زوج ایرانی در حاشیه دیدار بامداد امروز دو تیم ملی ایران
🆚
نیوزیلند در جام جهانی که حسابی در فضای مجازی وایرال شده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23661" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=melwPWEGmyDxYD1jFTUtVIsVV1crpFWuvdYLyaLhA-nLjco40aqfWnSyNnqRwq-6ZBOaQgQfSZRo3-aZx9EPlUWTTrm4nXeO6-4dTnt4KSddszpBFtxv2JyjPRD5bZfRm_wFLet81_fMQPjguymLpqBRps9b03wL4Yab6LN1KKAV3Wo_Q6t6yIS0e10_8uqoF1mR-h9xSGIs5wmpxO77ZHTRd8SFZJl5s3XYl51KXB8Da108peKQJ1TBS1PHdtDvAy1PDDpb4Ub4ghoqGqh0mSNXwxVI842RW29MVCfTZ5TTZYxDG8saXbbb09MsLDtL4PAmh4mcENmuLz0hHfNa5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ca500416.mp4?token=melwPWEGmyDxYD1jFTUtVIsVV1crpFWuvdYLyaLhA-nLjco40aqfWnSyNnqRwq-6ZBOaQgQfSZRo3-aZx9EPlUWTTrm4nXeO6-4dTnt4KSddszpBFtxv2JyjPRD5bZfRm_wFLet81_fMQPjguymLpqBRps9b03wL4Yab6LN1KKAV3Wo_Q6t6yIS0e10_8uqoF1mR-h9xSGIs5wmpxO77ZHTRd8SFZJl5s3XYl51KXB8Da108peKQJ1TBS1PHdtDvAy1PDDpb4Ub4ghoqGqh0mSNXwxVI842RW29MVCfTZ5TTZYxDG8saXbbb09MsLDtL4PAmh4mcENmuLz0hHfNa5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
«ووزینیا»ژوزه‌مارو اوورا دیاس؛سنگربان۴۰ ساله تیم ملی کیپ‌ورد نمونه‌ای الهام‌بخش از درخشش در سنین بالا است که پس از سال‌ها تلاش در سکوت در جام جهانی ۲۰۲۶ به ستاره‌ای جهانی تبدیل شد. او که کودکی سختی را در غیاب والدین و نزد پدر بزرگ و مادربزرگش گذرانده لقب‌خود را از واژه‌ای پرتغالی به معنای «مادربزرگ» گرفته؛ نامی که ریشه در شوخی‌ های دوران کودکی‌اش دارد چراکه در بازیای خیابانی هر زمان بمشکل میخورد به مادربزرگش پناه می‌برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23660" target="_blank">📅 10:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKnsJBZWaTe4DtQAHSFF_l8dli69vJYP_ltesA3oqhcgjnTYeeQuyh3Llu8-vC5WSGRi4edk_7lNhL6HoIK5TN8qULEwaKMHNQHng6qkFiwqKxc5qEgN-6vEgCIgAGuRnsQCRBMW8iZqWJCXfXy3ynfMtqZT6yMJzIbm65TwRr1eGrFAD4x2lXXKIvNB1iX_7064pfPOij3EstxBzDYMQgX6gRVJ9H4pxefPcjDagGCBco_xeZ91_bD0XyOa8EU-X0GS2LmKPwFOnsT2GEIgYuR0UwzNrNRnmdw2FEc6oPysZvheEMjYDTAASrCxTNaFkOu3_HV8F6stRS3kObuhAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه گل‌گهر سیرجان پیشنهاد تمدید قرارداد دو ساله به ارزش‌سالانه 20 میلیارد تومان به مهدی تارتار داده و منتظر پاسخ نهایی این سرمربی کهنه کاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23658" target="_blank">📅 10:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3nLhNMTDfm-hXMp_EWMntdMnAgh3SztANFhDTSUg3ysN9AIXYQRjKvwQCy5DzS-MEOejzTtz7Xi5YoH_YL1NND2_cXtAp5Ja1TGTsRLSnFtek8QDvkHYvY7N_6NlniJG9V-L0M11FeIVj71MXXCzlZe1J-DsIEPNgLWH7WJruSr5JABCEQlUGJJHjCoLKnq1W8oerFICpI3xOTg6OXOuYdHfs5ks5FZMjKmSLI-6agKOlUHFcc5sNCYtsV_5ZxMAp7sBYb38i7q-fTp6-isfg6l9qj524azB13CU1O9Ja4hs3bN-JaeNMt5VFlEwvygFC5f9WKyTqQZwkA-wiDt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#تکمیلی؛ عملکرد کلی لیونل مسی با پیراهن تیم ملی آرژانتین در تمام مسابقات + عملکرد لئو مسی در تاریخ ادوار رقابت‌های جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23657" target="_blank">📅 10:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5KExhg-L79o06xcJK7C32b2UQrTW-lLnoPJqxMQIxEnjaaye1Y-sDMPPin3Jf5EugVmwx_JM1MLTDLlNSlDZ2c92TJ2j45UE3qe0RIUDxdqfIEoj-PEs32dtSKDz7p3TDzlk19zPdt-AiLBBoCkR3rrYOFEsDrqzVx3loUnncGyBSMN9bUjCJ0BW1DEKfX-fqCwdWrCErZKQ1jIXz3qklr66oWlNpqB2BMfRw2doonQedosw3Z6JGVUW9n6_QxKhONVtnpbDv6aEjossmKNJUEOotPxh7O5f19Caq4nqwmyA9Y7tx6Og43pXkjxMAeqKYbFEp_r0NQJPN4EdXV_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23656" target="_blank">📅 09:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⚽️
خلاصه دیدار دیدنی‌وجذاب بامداد امروز دو تیم آرژانتین
🆚
الجزایر درهفته‌اول‌رقاب‌های جام جهانی برای دوستان‌گلی که این‌بازی فوفق‌العاده رو ندیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23655" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=QhugM9EyinanNfwuQeGDDomNUUmBH_BpxQCwb8MW1bs91ZKEmftNJoZ8-dF6M4_eQl1ziFJNdgrL0Pmy2Ft561RVumpbT33_LkKjpFVAfC4vOMxhAXx2ffUB8qYxSf4zAIWyHhcWW0QG42l9YSKT0jqfQvAK-rrFsIwaO6MWM5GVvGKk5j-XAu7P0rie94nsqzECLDHR3EjYTU-_Ots6H1Mn0TDwDHHZRR0Q4xYIlq4YKnEjbhuIqZ0AhwRKr5FV9Y6kcGZrZSEyKoGLqoSvayzIgYZGW0YupOGGfp9VTMTokRcbP5fJLSWJ5z0FdY9t2CNFBEHyI2TJ_zqMgNPn8SZ9E-okdyPGvxuWAEdgLTay_I1czE7qumKWLYFz3gKzbVq9P6HI1KguEGYSp3UhYJKik1KfJ5aUbPGa1iuv-_iOKWGR0JjcAobjSPPvn5yNEDra_N-xVkVXdcHrSBkCPax4pDR2rAblF8RcoUDUzeYSCAzFFuFGNz57KNvyzguDQFCCHO5tyIaZ_BtbNT7h6F5dX_qzoEHr4fgYeTOin1bGJPCMofaVNnbkEHcxALr1xXsbPLGr345OFWw66dLU73pLrtbZjANZbdiJrSiKMTYmB92muRyNH40QRcDNMftQsH6zEXqBMPMbDTogniRM5YrdKPSFCUGrStvIuEG_frk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e7674afc.mp4?token=QhugM9EyinanNfwuQeGDDomNUUmBH_BpxQCwb8MW1bs91ZKEmftNJoZ8-dF6M4_eQl1ziFJNdgrL0Pmy2Ft561RVumpbT33_LkKjpFVAfC4vOMxhAXx2ffUB8qYxSf4zAIWyHhcWW0QG42l9YSKT0jqfQvAK-rrFsIwaO6MWM5GVvGKk5j-XAu7P0rie94nsqzECLDHR3EjYTU-_Ots6H1Mn0TDwDHHZRR0Q4xYIlq4YKnEjbhuIqZ0AhwRKr5FV9Y6kcGZrZSEyKoGLqoSvayzIgYZGW0YupOGGfp9VTMTokRcbP5fJLSWJ5z0FdY9t2CNFBEHyI2TJ_zqMgNPn8SZ9E-okdyPGvxuWAEdgLTay_I1czE7qumKWLYFz3gKzbVq9P6HI1KguEGYSp3UhYJKik1KfJ5aUbPGa1iuv-_iOKWGR0JjcAobjSPPvn5yNEDra_N-xVkVXdcHrSBkCPax4pDR2rAblF8RcoUDUzeYSCAzFFuFGNz57KNvyzguDQFCCHO5tyIaZ_BtbNT7h6F5dX_qzoEHr4fgYeTOin1bGJPCMofaVNnbkEHcxALr1xXsbPLGr345OFWw66dLU73pLrtbZjANZbdiJrSiKMTYmB92muRyNH40QRcDNMftQsH6zEXqBMPMbDTogniRM5YrdKPSFCUGrStvIuEG_frk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل فردوسی پور حین گزارش دو تیم فرانسه
🆚
سنگال‌درباره‌قضاوت علیرضا فغانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23654" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">▶️
قسمت‌‌‌ششم‌ویژه‌برنامه‌‌فان‌‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23653" target="_blank">📅 09:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23652" target="_blank">📅 09:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌مذاکراتی‌با اسکوچیج انجام داده تا درصورتیکه بنا به‌هر دلیلی با اوسمار ویرا قطع همکاری‌کردندسریعا با اسکوچیچ قرار داد امضا کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23651" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JotYYsy6ADkTUQeZDFZInf_LpTIieay9rOw-aHQSVzBlFL-CpxG6cFg3Ipx6hpaeQcygPBIQDWhc2V4W4E3FgElA_klpLv4iXgRv8jbzP2ErDqRrcA4Oilk-euuQPdc5ACxV4ynPcEUuWSY_cC4dlbGb3fekNPidFt2j45G39BrK5E7B5JRW4Z5wyn9TDHuND2J6Mz9CM6HUs8QDWtcU9DGYQa6Xd5Ywh5U0rcaKqYFxesx5N7sgDM_JgtP8sQ49GYdSNfhNHpopDxcTEV2bk_sFSzg5QVHGrR-MzTzfWyXqn_LN4Mb8Ug1Zi7ekHvHJIM9TkAjnG-B55SKBsNhMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4QioUo3MlEo5nrYMFCKJxlZ3zKQBvV7REmIB4vxe4X1XxpHNzOmB3HGjhny_SuH1I2HO21MNTVnsMiYxF9OT5O71dMj5Oa0CKa2fR9bpHDUg9QHinrR1DzNanehXIrcjzArH5UE0MAXXVtPjPwdZRA8iCIDGJUD0RoRMD4LJBq9muHtWHScAhWEVvCIfU1BEV_Ia_f71N_lVb4VrEk25bOoABbN3SkwMros4VmE5ogbC6o69lJ8mn-rTQys9m2CBfc1MKs7JRwlo18oF-UHZ3xqzEj4Fa9yODKttFAjxovXPyUI9Ivl3xKnOkTpYFHmDUNDJQ8Gw5Dnn48RPUvBYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23649" target="_blank">📅 08:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJxA6GeX_x5mcPFN8511krhDbqoOWNPWFO3Pm-tuj8JWijMKLcknGoO-gKs1JKylTUfr4UWK4lWlxX4oTiAH_gRg7t318UfP0Sxpl6PiAa-7A0mXX9rV_8K6W5aJjSb1deYnIxqugJ4uH1W986bKizn8mi2ZQA-Pf9Ik2k11-5dOiVUYm5ipIriWvG-LP9r87Z17rUC66V9WLzrLYbuIb6XXrn1Ko4Qc-68ZKMdARwE2S9C6xpMrfFdyCweOhzrsd5mZWdkKcQN-gLmbICU2Alv-gRx3c1VmeN30sJuUkV3mekQz-53t-RmtY2TLBWJHR8JUfWLzjCYASs2wW8sSqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
هتریک فوق العاده لیونل مسی 38 ساله در بازی با الجزایر؛ حالا لیونل مسی با16گل با رکورد تاریخی میروسلاو کلوزه رسید و مشترکا با او بعنوان بهترین گلزن تاریخ رقابت های جام جهانی لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23648" target="_blank">📅 08:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ پیروزی پرگل آرژانتین و نروز مقابل رقبای خود بادرخشش‌خیره‌کننده لئو مسی و ارلینگ هالند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23647" target="_blank">📅 08:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/osr3oGrqgKyFcG4VUsjX7xC7BF-zSW7WeLis05ftgtjzO4VzsUJLU1o1ZlSqy8Lf0dscR0PhUzgGsdOd1B88rfXBCM0P_Adx4_yF8aCgCmNTcuLGWKc7ONrWXkAUQt1Bq52Yr-hsOB7Wz9bt-bnORlZm5K-Ooe2Bo5zSb04L0wtDjNPc-THEIN3FSvchk6BoZd0feC5u-sE4g9_Yz9lRXo6Il3L0Ic8sEJFuPy1YHOZ3erXPIf54NsrvZ4Ro8t3yRkRzFO9PL0tPCNVXVKg_uAclW_KUPCFU__JkYBgsv4d1XmiTWQC97cv9ehEc1pZp8HZKHppy9LP_Bb6X1qKlZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk95QX8CULKQUv3tzugAhtFglOP51H8u55oW1OWRR9WA_MI_Vg4ZjjqEHPT9vbmKxI0nZFgVzrhFcPwAy5f_oVhLloul7fSeE8QLWS_GVjBmUVeZkaCX7XN51ucwPVASrw-dWVLF7WtdEAMHIqnwiLzswZkcZSRpnDPZHpFQLdYdOcLv_U8KpVr100Al37YQOjxnugAl8xZSCIEOO6slW7NGW6HN0XY8Iz3jXzsYOnSEcaVMOVjOLlujLdWPaR3pyo2d7q86P8OQQyNOAxRkTdGj9wHKTOBIhbf6QpvNHFnkkuq6vIj01TmXJ2b-ZwMAdb0FUDrWvAyWnveCS9gcvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23645" target="_blank">📅 08:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f480511b29.mp4?token=WS5NfEjRXJEIHJC_syiSqIQsWEwQ6YFj8x2vbbBnJiskjN5qh2MlmNvr6gkRVCUoallIjsKJOUF7oUhbuaWSEB7DdPsMW4HKw5Hxz7cC2BoY0NEDgEDUfWJWnq1876MrSz-ODryrZWjGppFKmwTAamcyZwrUl_MvXe6vZKaqUcggX903wD8z-SmaLSJDDm5Ddibq_CUanCmQKMEYWTPOGP1nNussjawpvgjg0dT_59lE2nYqD3ocKQbjKfoMpYCVB96ahEY49fNO4cXtoqjIEPDaso_6gYZbAKoBKSAILTchEE9D8DGs-6jkm9FWAdW-r0neWHQXAv9Rj8gstqr5VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f480511b29.mp4?token=WS5NfEjRXJEIHJC_syiSqIQsWEwQ6YFj8x2vbbBnJiskjN5qh2MlmNvr6gkRVCUoallIjsKJOUF7oUhbuaWSEB7DdPsMW4HKw5Hxz7cC2BoY0NEDgEDUfWJWnq1876MrSz-ODryrZWjGppFKmwTAamcyZwrUl_MvXe6vZKaqUcggX903wD8z-SmaLSJDDm5Ddibq_CUanCmQKMEYWTPOGP1nNussjawpvgjg0dT_59lE2nYqD3ocKQbjKfoMpYCVB96ahEY49fNO4cXtoqjIEPDaso_6gYZbAKoBKSAILTchEE9D8DGs-6jkm9FWAdW-r0neWHQXAv9Rj8gstqr5VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
خوشحالی بعد از گل بردلی بارکولا ستاره جوان تیم‌ملی فرانسه به سبک محمد محبی ستاره ایران.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/23644" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjCS68cGKlxkdU-idaPxLRIhJTHGkObDUHm_dPrz3myWKoWtCbhgdjEqoXkFaYKPf549naXgGSTSPBvviMwXrbrx_SkM3Uta6QIj_QwcrGE6afcOWh-KX4gpmljkk2dt20ttOPwb6l7SprXWpctSuEXwnwbEjFicsa-PsyYQw8JabpbwP0mFmhB6T7aaYHHvgfAj49LB-FX546B8Ie1Tr-jBMnqPsrlBU8FcuSryGlIXQMsEr5z6Fi5muy5vXG5iqLWX2D-vUn7HQLKQbnAoKZkunELYujjC_jO0csUCT2Z5DUoS2jIGgXRCOJOuAT34OdecStyF3A-SbFEKGOW41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
#تکمیلی؛ درخصوص بازیکنان تمدید هم لازمه باردیگربگیم‌که‌باشگاه‌استقلال باایجنت علیرضا کوشکی و محمدحسین‌اسلامی برای‌تمدیدقرارداد این دو وینگر جوان‌ آبی‌ها به‌مدت 3 فصل به توافق کامل رسیده است. به احتمال فراوان در بین بقیه بازیکنان قرارداد روزبه چشمی نیز تمدید…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/23643" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRXIGJtwB54x6bfJ4dpZ3iCmJprtmv211kfRLJmZAaMwGEa4jk2zYQwRajmR_duMadRWDgvly7c_kCqUkzCGf3020Y8B75c6oPqBrJW242fd7SXxZw8ZsNGutUGa3tCuS3spTnVb2lCYnreIr1QtlGjcUHZHjsSOhrUsnHrAZ4uTYhNIziX7vqgWTL7w4tl7PJyXpdCd_6vBewy59FcnU6ETq4k6wiMCBPDQJziLplplSdQzj1vPVBrw0f5__BHBjtvwLJ2aOGAsQm4QKQBTMhQSuYSe_0esjNa-v5SL0IwMFspZyeVoAioBMh1jBsDiJF3h03RMj73iUHaUNeR8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
ازاولین‌بازی‌مسی‌و رونالدو درتورنمنت تا دوئل حساس انگلیس
🆚
کرواسی
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23641" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXb-tXW_x8GJx5PPrIUT65b2zaZeHbWgYQ-YRorrKWPNyJd9SK7Pt_UaCFRB4Ga3sPgId25USFTgFwqKibNMd8nT8Y34CW0SyXoA9aT3ygXlDttlYDHbe-RESYV7p9Jeels0CZ7gZQeKyq7LBPVZ64hotmikCoqfHZj7371rv62BfM7N5_Me0v0lqBm5mYyKDglbPC-wI3KZiEQed0FmOfQvJdbYXDbv2a6DUtu9WoeYvOJPBD1I_jIDDKIICF1bjClWtAWsz3REf5ua9iQW0dPFs8AAqhVW3DO5hRRvhLoVxXVFLS5xc8Zu0HlqBEpp5vGxLUf40W9tCuFMzGGdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌‌دیروز؛
استارت قدرتمند شاگردان دشان در جام جهانی با درخشش امباپه و اولیسه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23640" target="_blank">📅 01:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn-vkKttk18SOWoUff7kQlnMVPAcQ1Ln-CSii2Fss-sFdZcvj8xx_8W3quEJcVMxr0PhMi09hfykgmnNNRArUIlm0O83xICiaUUbIkIemTcJhynythjaaQBaJNrKA-S4XUTGJNB1pRMTfWffIjkNQs4zSHkzLSx22AWXRrqGg6mSlFDA1u5L74CxYaeUS8ljA9_70ZlVyCfDwZ0M2qlrCcNJ861DrP_JstAfIghU9W0QQL4RuUO2SNIvQQRvbesFKL0CmFVShEwHJpi2AoaIrQrU7FXk_PDODNB7ODKkrrabgiARm8LybXVnj_K_OisqjyT7tbXbv-pky9LZhruycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#تکمیلی؛ جدول‌ بهترین‌ گلزنان تاریخ رقابت‌های جام‌جهانی؛ لئومسی و کیلیان‌امباپه برکورد تاریخی میروسلاو کلوزه اسطوره آلمانی ها میرسند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23638" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی شیرین و ارزش‌مند خروس ها با رکورد شکنی کیلیان امباپه و در شب قضاوت درخشان و بی نقص علیرضا فغانی.
🇫🇷
فرانسه
3️⃣
-
1️⃣
سنگال
🇸🇳
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23637" target="_blank">📅 00:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVu-LH_WghV8hoH4ymVb4yRifP-gtXeSp92tPWtZusZE4N78OoUJcwQ_inuhngbfBTjQGNN961heT2FbpGCiti7YN2naM9McSnTfAtaUFoBlBJB62E1A1NT521xJp341PD5Cnya8qkkhPzApK6eofCOowCpY7g-laai92AoFZkY0zbitY_lE3LI2eeL5cmBxC4VChsfHk_Zq6p_L33nvrUa9C_PVkf-k5cDYf3pkHVwjkbkOqLYGZdjDqhfjEX9d1bVpBabwpxlIrula3NZ7kbHqF-3waEEeTdHVmMU09Ocz7r_HbhMlcd4Yacb_l8hVYNKN0K1sh7VfQZKEO6ArRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دو تیم فرانسه
🆚
سنگال؛ساعت22:30از آپارات‌اسپرت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23636" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lelXPruf4Dt8kYJ7L6vKUvib9urNXSwmOAja_IgCnZfKng3hE6a5e2l_RV-f1Q8Ujt3IypS_Z7Kpwzyw7gJe_Nz6YkRKIGkMkotG58gHyg4N_c2Vv1mudJgTC3i_qC-lJmy2zBRUEv_1JB_VFFGG3O3KmBhDlH1dwrn4xglYizsEdOIL44qf7iWaZyWCPx6lTFpMFXEZ7Ios09e_5LDJlLWWojU3oK2xWaCe4egIgYOkVGQFjq6SubJhG2vINX5fTo_5KDND2BtUV-e4NiXwIfvjAz0BRLb4Vx8UOVM3rzpCjvtN4CGKSspgJTVCQ6t95m5j36zzyG7ps-Jn1T4c4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QmGeK-mkOqZVS1uxQ_TRXc_PNiOVgpSC6DTYJS2W-Ynmk2_x-Fp42tQSwPU7Z14U8om3kLUuB6MzyDG4bJMDSSFNM9eXgni5Lzg2Y8ZlBM1mmPEydFcvLSG0MOqAvxAaSvH1OFIkd4-HMUmrHA97aP4uwN0WTC97WAJjE-kN_EdXJ8Fw-ZOltTZwt_cSPJug1_GFNcMXt7zRQgVPexz_ANMA-iIzG9l0j7a-Okn5YTqTHgg4GUbS9g8177cYz4hhCJn1MZMijQ_FVIwci3_QAT7sqKaxw4VB6IsHvAtl5YQbt_OiOajPY1awrLrSy2J-hVcUMim4dFNtp4VxDj7NGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌اول‌جام‌جهانی
؛ شماتیک‌ترکیب دو تیم نروژ
🆚
عراق؛ ساعت 01:30 از شبکه پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23634" target="_blank">📅 00:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj_MzjvJbz_uMGxBRC-MegqOt90emnfmDmwKbupg1gg81M5XACYqTXrGyMIsu9YBtOrRzkY-JsG7fJVUjd1QQd3WfQYqUlOhqSwpnIs8xNgQrhEbmsNri1J9Qp4H9v5GgYP6IsMxVRp3Y8pG_XHPzz0q9LTFPIXSbsM7k4FkRzHQIa9UiqhvDc1dRC3Ee6mJuebSFViqHXp_bMaUaoXjFstxl3ooG6YB-Mapd2RhnGs6RQWblEsJt9kwgEyMSgVZczcF6-T5ENdfp_TvFuyI8TMsSl7ou63xQUq_Ej6kNYPPdI8ieHqqKImFgFC3Lp_xqCte_GMWgUznkT2d4cQf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو کشت…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23633" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMnjkrrCoyNzioLtgw0jcU-ClLM1Ut8WV4N0iTQ-IBzYedBd2Gx0-BaPY0xnxamuDaUe8LpZJGQZEwqGfARi49f2q1KaJFGQ2Urp2JaYYGgZJ-XSVmfHoqeE5lYi4QYDgQqKACCkNKIoJ5awI1bxqNkt_Zn5d9PtQ1jhOUEq_RkqkrkeFSAoglQsXvDATEnIC0xpTUhDG8LFbc8IX2rmEPcfqWc0gSP8VkpxtXyXxPiin3591pJsuXUvxvUgZgjhy6NgAJ6Gc9L_BL-BgbKCOLl0W1yLnSR3C8nojcobESz_B8k0cPXRbIkt39v39Q_nNZpr4LoRQMa1A6XmlW4xBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23632" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsGsd77eZwttyhEqIJbKrWQ0vH8dJniPF2nDyQJePrq2nhTtonSu-zP7FlkeAiuDunsHw3bIGi3xArQ4SFLkGc5NUZq6ZbgJxLuQGOPAz0Jyje8NM-jYMwtRn7wkTRBfgfA32R6du7j_Oy8Be1t3u7gOQ8b4ACIau3Z5m8bW7tpC2H7vDeFPOSPstcIQayaiRaKhHwjIJFpDrvo2mkJHCTa-S8ZnY-pGeHGDFjEaJDtfneEmyc3fzMwl0_31vz00qXMBxLsIP4kxpXf2i9lYPWs08kucdRh3eDLsSO5jzKJuO-sflq8O0wowaD_HeMxLbQRDVywvJgKZW2UJxXXoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ به‌احتمال‌فراوان بزودی شاهد هیر وی‌ گو رومانو برای خولیان الوارز و بارسا نیز باشیم. اکثر رسانه ها و خبرنگاران میگن که نماینده آلوارز با خود بارسلونا به‌توافق‌رسیده و فقط توافق با اتلتیکو باقی مونده که با توجه به فشار آلوارز به مدیران تیم اتلتیکو…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23631" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIe6GkmurlfyS0quKQBeLZkSz7Jp4MltbN0Wmw13j9qJGSaHZP_pWHzqR3IzflOOg29UQcR7WN1ZZHP6aU0w4xcpDWmA6pFDWFNntFpfQ1nrYNnx73DaLs2UcplxbhLQI2Oy4AOAR_bGRNDdf6aj4C7UrkpE-dqJ271l9TYxWw9HR8SBQQkE7PpMuXSG8jRDVGZqPpzWCLNmYIPclH5PXdmRipPeSp2Zetw1wzzD-ANP3xe4BOUUCsH9DPlQMTjhwQKfT00xOPEsSARrgYk4ffDqx3x73g7-4S9UV26_oonQHSuAcfaTGoUBGVGbFNxyIK_klPOuoDRVABBLfrJSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23630" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=aMVE0pZeqfLHBlXPjZif583dDNAkZmv1AT6hup93LVRmBDnCZbxkn17s7hPjOrDiyebjhU9kLUZEl9YxaUad1mSs3LRVaf2myHOwbc-DwI3OS__w-abaKsWWGsj9X-hC3tnK4Sq8pNQTpVOH7XyaASZCeMaYL1cNudQs39cTUvYaEvEQpuGjxeAiCcMHMZFUViyo7eQXtnOD6Mc_c-lZOHFzr2tRzAwk3lUczcumYewqbuSX5uz7NaoCjc5mTdCXfNkCWdeSIHEuRUvRu76upxui4vN5DNtMOF7ssB6LR-hteFyRNbHgW_G9w6C_yNUZ4fkj69H5xW66xThTUsUt5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f28c9e179.mp4?token=aMVE0pZeqfLHBlXPjZif583dDNAkZmv1AT6hup93LVRmBDnCZbxkn17s7hPjOrDiyebjhU9kLUZEl9YxaUad1mSs3LRVaf2myHOwbc-DwI3OS__w-abaKsWWGsj9X-hC3tnK4Sq8pNQTpVOH7XyaASZCeMaYL1cNudQs39cTUvYaEvEQpuGjxeAiCcMHMZFUViyo7eQXtnOD6Mc_c-lZOHFzr2tRzAwk3lUczcumYewqbuSX5uz7NaoCjc5mTdCXfNkCWdeSIHEuRUvRu76upxui4vN5DNtMOF7ssB6LR-hteFyRNbHgW_G9w6C_yNUZ4fkj69H5xW66xThTUsUt5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👤
تیکه‌های سنگین عادل به کارشناس سیاسی صداوسیما:
هرچی‌میگی برعکس میشه. بسه دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23629" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcF3blho9SYiFwX6UlTTtH5W44R8Nt2ohBbnxhiJ9aJallDvXWizuoyZCtJo6VynnF_f4L3fCRevMA-AGKb1OB6ua6oTW8ElpepqSrhLrqnSh9NBDsX0dcfD1T54gK437SrI5xuCz0lR344Z3yny89Pvo2Yk8_3hFfx-TPBYC0kGP6GZ_TA1ZyJYDY6s3yVZKkA95mU_3Hvu5tRB-vn6aUL4VI-uCKWwv7wFRUqui6d2rCiMuSNBMDrQbAialML_obpDD8jIvOepw1r2OYFpNtLikzds38nbSAo2NKcA5x-lLuGFZqkbkGjZghCTAug1DN3369R79pS33zc6M2kuRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی|توقف شاگردان امیر قلعه نویی درگام‌نخست‌مقابل‌تیم کم نام و نشان نیوزیلند.
🇳🇿
نیوزیلند
2️⃣
-
2️⃣
ایران
🇮🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/23628" target="_blank">📅 22:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVCg1I83GBBo7wJS3L29A5oqoXHCErg3kFu4YijHG_QkSq1_gAgFUs8dee_jpsmIjeazavvhHIWq-u6H5ezUpxQJ8057LLXlo18H1g79MgMHAR07v8EjzPwabhrZin58FMKMFpCX3MAGjjdPaMa3E1fIivYC4I8KEamF5sGEVTLp8z-6Bu_0o56L-K23udpRahrkofegqqsHLN2aubsq0fnK6oRERIbK9T9b9z8REnmsmqXodcqSYpyEqIz09A2tpc02JddF1qHkKd3uykrKFmIM9mg-ptP-PYcF7vhBsvYKAdYqyKd6om7k_oVMZNHP-60I1_4nGZNIZh4gBE-X8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در گفتگو با میرر: شادی گل من سیاسی است اما اینجا نمی‌خواهم درباره آن صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم میکنم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23627" target="_blank">📅 22:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThVcZ1LB_Xdeddko1iAk43eeYOYodyDGruLK0dAffrDgvXG60ZGYiDcZfkwxP78POdHjeSrBtQIXO_KC_zhf6eNsmqiduUgKBaxnPdtCf_lDcqQQjLeiP11zusFFcyFtdz7HthgkDXI0daGrWgdvFkTbmPG45hBWMKZKvIW55fxI9wBTBcATM7AzqbsBQu3jPU8kWRMJCQARxqMj-Izam5l9_h0Zev1yxWSr8GOUMLQHegdpSeHSiu-5nhjgu2pG8vcNkefetjpyE4zMeazcc3d4dEZij1DPatXQTTQCnzRAdltZ7vYyWQhlGbUSGhhGfmWU1c_9jc6KGueYB_SXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/23626" target="_blank">📅 22:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXmrLg3D20vSFpvEsvfWn7VFLs3ZQBxIOF3kwrMNufCGIvSDb2dehIceIzsPUuAtvd9x5RgkLRh9DV-x2fmdFiy_W1-sCBTdiTu3u-4_CYDPoHjsJGMzS-WgLQiGXXQfmReWLNLvf6BfEXRY5szVsTW8T92VL76Yvs8koQK7ciZDPXs-bqwje8t4LJeaLM2xZlgz1LJreXEYYnBVrDxks8HU4LjJkfWtNuZKXtW1JFJo-25s_xVfumD9kqxKZ-a7QWCu-piWnVEgf0xfYG7Ljssgx3RAsCE4ZoSbIyVJuoJIPHwHIJUuaZjtgoykoXBDymaAeZDd0fgEj0PcGobCqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/23625" target="_blank">📅 21:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kDxy7J93jOzWokuRy4eNEsFhG6X3Nz4tBg51FpGTa0-zzcn48EU7PrTrCeA6z8Hp1Gd0UdPlcxqLZfuw2BtI3VrI8oEKGHqT2kYwfG5bdJzk_J9gNRiaXKb0mJCs_X952H5f5MIgkzhNxqeZ78cHQeRWO_DL-Q6UThOKGS6-v6wQVkqIsX_BCe4_95CEeW7neCMMeCFKWEUvGwIWFXpZhdlKD1w_mXp1h56KkNjRQl5_z5-2FmHDiLKviuwSH4Jva8GKNquChH3GEEb0rAKqEr1Ppp8kWnCHE7bjAGkcTM0WDBF9BDwEu16vzdEaS0RASjwjW4NHEK6cgX2Rp057RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y397mLMoUcCsRYHbbhEp9_glBoJxhXohF9RRrwDP-92ALc8Gl3jL-ANVgR0mHwBwZV2qrxXhqmib-jhsDkQK5XhVpSrpXxZ7NZe7npEXedBxvfeHnEYeKosEwddX_345pN17xaX1SqQmAyMqFMwnFphu20LfR5RFHbWAaC1SHOXOE-tOvMfgjRlcz5L473EGbyHPd-15TpibKo54Vjc6HiuSpx3AwiK1STgbIz6ALRsitZhtp_2BPXCv6HRAK8ET_itH3D1KemKSS8EhyTho7fwOaraaCXws_9ZSjDXbYmwYaI93yxeBznF0F-bM1k27Qht9ZcT2X2ef3F7mFBQ6bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بازی جذاب امشب دو تیم فرانسه
🆚
سنگال رو عادل فردوسی پور در آپارات اسپرت گزارش میکنه. روی پست ریپلای شده اپلیکیشن آپارات اسپرت رو گذاشتیم اگه ندارین دانلودکنین کیفیت پخش عالیه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/23623" target="_blank">📅 21:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23620">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjO5Z7k0Lq8umvS74Xli9nFMYuOp0PI8mqaDbXw0gkp7aKETa5W0jf3_N9M_CJfuPoIUzZIyScchN6tT40S5DtzV-7mOoqZVxWagqz5wA_mHxqFN3YJK0E4yUwDyoNPHtraItQpLWw5N_CvHIF8AWpeCZrg4kZ8lWkIZQe-CoxTbUTWu7NTIuHTzwDMTFro7BuENw_-oyko3uzvG8howIY41yaPFW9YrFih1brJt-_nolD1EuvNyk4VIBKVZTJK6pZ4XNGRB9Kw0LG8OomHP8OjCnmhvXPZUHpuOv6f12c1Bx1srjtu8SqNPUFmICQNgLiZaNjcapB6FahzaJQR1Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/23620" target="_blank">📅 21:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23619">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOuzjX47Z-zAFHIhjFvBWLcCvhEaoIGjidb8ay8AGEzYDAnBg2EQu80fWM756oZPdokM7AJbf00IS3lN_bCZjTiVadhSPlLyIrbVSRMGdJRcCdlAfusO8ig2cK3aTqQOEW6ta7NTQMrzV-H59ZRZaZOisK5lVgIkrUZUMSRCrJ-LLJom63ujBSpw9MnFn54ZfM3HbCKZUB34Ot2H-R6eSWiQe704rJQdS8WSxJBQhBfrh_Lc7qozoZM6ieD2QFVDAjkIy2-FjvwfT9vbikq6PDVsYp2oHrOXWGKNuzdQx--GcgierClOaeSESpgpup0Lcm_Aah1WeM1S8AhfAtWIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بامخالفت تارتار سرمربی گل گهر؛ انتقال مهدی تیکدری به سپاهان در پنجره نیم فصل منتفی شد و این بازیکن تا پایان فصل در سیرجان خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/23619" target="_blank">📅 20:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/335ba40687.mp4?token=g1OITdzVgrcQ9XacJFf7MY6bTspd1BftLnznua7tDgfFRDv4KLySt0OINQapuzL3q-R8ouHoChBVTEs4SoJ0LNZERhVVEOixFRzqjMq-qCdF-sNw5IEBg5glVwrC0edJQ9KBnt5PGD_V11r7J8B3v74zqI1fyBGpYxRXQPHmQ9x4nDP7oIp55QJL246JS_LUzjn0kOFiQWAb5gC75mLJUd-Y08OmQStrLhNU1UOrjjsqRFAkvZzp9ive2BAFNp94tGwoE-JFe8uYd8k5yXpHCrYCHdK5PtRdjFWqyb9QphGMBqR1UFW21U2ETnvjShMKOjXcHFtjqCyldvIhhOESfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/335ba40687.mp4?token=g1OITdzVgrcQ9XacJFf7MY6bTspd1BftLnznua7tDgfFRDv4KLySt0OINQapuzL3q-R8ouHoChBVTEs4SoJ0LNZERhVVEOixFRzqjMq-qCdF-sNw5IEBg5glVwrC0edJQ9KBnt5PGD_V11r7J8B3v74zqI1fyBGpYxRXQPHmQ9x4nDP7oIp55QJL246JS_LUzjn0kOFiQWAb5gC75mLJUd-Y08OmQStrLhNU1UOrjjsqRFAkvZzp9ive2BAFNp94tGwoE-JFe8uYd8k5yXpHCrYCHdK5PtRdjFWqyb9QphGMBqR1UFW21U2ETnvjShMKOjXcHFtjqCyldvIhhOESfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
#تقویم
؛ 20 سال‌پیش‌درچنین‌روزی؛
لیونل مسی اولین بازی خود را با پیراهن تیم ملی آرژانتین درجام‌جهانی‌انجام‌داد. مسی 18 ساله در اولین بازی اش یک‌گل و یک‌پاس‌برای آلبی سلسته به‌ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23618" target="_blank">📅 20:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxc03IfkTSrhLxcOYxdpYWBTBSduDIzuSG68BPL4eAm1Rmt0fom1uLBHZ1hUKE9PMggFPf9Di9zqUQfkJVMKDz8Yz8PXbLF5yg2x6KXtJmsZbRc6wVUGWtfGN7kJaNK38dgnEiqyhd9C0_Dk5rn3ea-XyV5UwdhgtTDbH1taJvbgUqR7ZlYX9Y-Bq6uBbjDp812LINsZOITOj_-0hvEwIJ9ImxEU_FAVjc7o03WXyMTWoCGeL0oIHuLyeZ1lXok54rmNlwOzVyJcJgoLvqibvczG-CVcaZKyMXoprO5DROXTzb861tosuj_HbXUFC85_jRUyM8YbhKxGsesvSyFfuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
تیم ملی اسپانیا در جام‌های جهانی اخیر:  2014: تنها یک بردمقابل استرالیا و حذف در گروهی. 2018: تنها یک بردمقابل ایران و حذف در یک هشتم نهایی. 2022: تنها یک‌بردمقابل کاستاریکا و حذف در یک هشتم نهایی. 2026: توقف‌در‌بازی‌اول مقابل کیپ ورد. دو بازی بعدی مقابل…</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/23617" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCekflaL75bic0u6TLfwoN0TTsIYvx4tGIJP0TQ8n2KzeVxl10i1-BV4f9fZPK0OBoyhMTDKCEh2SzpfY6q2_EA4ijnLhwRDFgAKKC-WkFb07F84wupV2OzLRy9eRROL-vlNu0l2Za4uOfYnXk2wtn6WRlqwhlzoc134_QReJYTQ2qSGvfkEUjIGhzhjsR_VOvC0xNRYXRTYUWvtag9yehNTT46PDOGUhY3KHsDrrYvehuJmpJozL4VaMKNSCVKX5opwTWsoNkC_PkFpgJdUb6_F1f9N9ADUsCyUpiip9rqU9UEuovtJVi4aaMc5jADJ_J1Cl1gH6Gw6t4KVKzXLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی جالب و متفاوت‌از خرید مارک کوکوریا مدافع تیم جدید رئال مادرید توسط فلورنتینو پرز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23616" target="_blank">📅 20:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUeROKQQ-6xNw7jFfgJU2c8B9dNzaIXfi5WQxLMfGxod_H8LJmwai9ajKguc8iqsEv4X_idYQty9JcYODzKweBS-48gixWVBxhA72jWUkO60mM9EZOwGdy1n8fmr7OX6PD4jESbWx1CXVMgeYaGgnOVPsGafL0cFq7Qb_0sG0tauLtPqBP4BCmMNAREgbv2vn1llL9ImUpj7yE-9pZTbfHqnycPW90vJCc6fCADjkYLS-AduktEZAmvNddQsfmtdTDI3akJ79-LcRmav4U44YG5Ix0AE35SHNqnDD-qdu3HJPCq8PZ1QI4w9PkZZcrj7MaqQUg2ZQkeDTXB31vQ8ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی رسانه‌پرشیانا؛ فرهاد مجیدی سرمربی سابق استقلال پیشنهادی دو ساله از الغرافه قطر دریافت کرده و در حال برسی این آفره. احتمال اینکه گابریل پین به کادرش اضافه شود نیز زیاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23614" target="_blank">📅 19:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3hfAB_4wMSIAMPY8XkYwCmXEFfuPnW7kuMTMzWOwpYLGTsP6MyMOofWQPfPKwOoWIlIMYUZTPHlpyIhk1K3Z7n1Ds-9pEMeRXguYIbxqSLL3WSjGv8sCC8wyTDXPnMjvxFuANfnuSu5ETZyq7g2X3BlmnpNSk4gVso8uSbCfkuIHL0NsArqG38U01GAoGBtRUedpt09oH61-qCK6QDHlRvz9zP2KQg6XIB3BtT758xb7ZRRKWs_M0k-xibP1EVXXywvaDCbyjW53unSGOUHYKZ4QmgtpYzUlFQKZi2eUYlsP4Kd1XFKSDQrJI8lsLw8XRJtsgfCcPY-cODouSqkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو: روبن آموریم باعقد قراردادی سه ساله رسما بعنوان سرمربی آث میلان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23613" target="_blank">📅 19:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fz6AxHzge1I2ocuCcFWjTzHAbt-sGrv_-UsQhH54nae3vityqalvC704mbYHDHYzzT7cpA_1Nawt8CH1kFssZw7fSqWdp-eSoox9BIEY9IrHMs4hbxOWl33aHaxZgeQznksE_jrE6vMZiHkxNrdDI1iE8RJKtUsYVwi8lWzZTukOXxi18e30z8XUEsZ810k9DAYBVyxbRtWSPK3hA8ghAZJ46u9rzO9_op6CExB0BIPTIQnM31v40l82RDBAKmLtLBN8-LkJeUxdsgaiJGk-biifvWFavA3Hz4mrRz5H4FPeUu4diaapvEWR5TBeUY_cQBv16kCTm_wObOMaQdLTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
⚪️
طبق شنیده‌های رسانه پرشیانا؛
عارف علامی و آرمین سهرابیان دو مدافع میانی استقلال از فجر سپاسی و ملوان پیشنهاد دریافت کرده اند و به احتمال فراوان از جمع آبی پوشان جدا خواهند شد. سهرابیان از ابتدای مهر ماه سرباز خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23612" target="_blank">📅 19:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328fe52870.mp4?token=DOx2xdmai88N9ncPxtd_ml_tLJe5Be9CC1LgXqEI9UDtG3uySBHTAh2RPlT3jUrIxeQ46bJQ6u9SRRbheSVbKevWuwj20mbVZr_9Kf_hY33HM_QCRA6e1mPeu5UGxLvcTJVwMi-avws5CY66Aa4fZRkyZ9wviSOEk9b1WSOOlQa95iXoHyqfwVVkpVn7FI4paiXrgbJvd72Lqo3zm4urFa5dxqqrBZbQCgWSG9dQK1SwRmdE_6rBRPy8RzwKcKPtTl8shf5dypzjvKFzdV1QcjOIQbKVPgEmK1qsgzDyGl7ZNwpGrVO_B0LTvcM7Lu_puI-blFkO0NHgxqFGLznkSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328fe52870.mp4?token=DOx2xdmai88N9ncPxtd_ml_tLJe5Be9CC1LgXqEI9UDtG3uySBHTAh2RPlT3jUrIxeQ46bJQ6u9SRRbheSVbKevWuwj20mbVZr_9Kf_hY33HM_QCRA6e1mPeu5UGxLvcTJVwMi-avws5CY66Aa4fZRkyZ9wviSOEk9b1WSOOlQa95iXoHyqfwVVkpVn7FI4paiXrgbJvd72Lqo3zm4urFa5dxqqrBZbQCgWSG9dQK1SwRmdE_6rBRPy8RzwKcKPtTl8shf5dypzjvKFzdV1QcjOIQbKVPgEmK1qsgzDyGl7ZNwpGrVO_B0LTvcM7Lu_puI-blFkO0NHgxqFGLznkSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
وقتی لیونل اسکالونی سرمربی تیم ملی آرژانتین رفیق سابقش رو در کنفرانس مطبوعاتی میبینه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23611" target="_blank">📅 18:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23610">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAuSKUeKe_qZ_h2u-Dh0aELihsFm7UgLZ07OKk9M6cXKAgQdGFmmaPsoEsjwDp-As9MIeKP-M9js3CRveFCMtjWqbrKnVBovlsdss-HJIEz4WAitf1PQAfwpudA0fgQ_HIDmXTwv0deoulmHyYlLsa7BnxVux3GjxjbQnDrNUXSmfUvOethqRFr4HoAxgF2-aTk9s46DYk9b7D-8mG4l3KvKhcq5SLnRXjhvL_hxF5WXFDvpPlgC0HBdCkQfE7iOIMs482OFajRItUv4A4PpQAj8nwiOhQMzl2jquISBvk4Xvi9W_6LDfiVs2PZdqXMqNtY0_2LIrii_Bt7WAEQonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
آریا یوسفی در اردوی تیم ملی: فصل بعد یا لژیونر خواهم شد یا در پرسپولیس بازی خواهم کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23610" target="_blank">📅 18:45 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
