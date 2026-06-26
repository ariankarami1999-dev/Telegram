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
<img src="https://cdn4.telesco.pe/file/AE87toM8i7I9Ik1m3PaE6sNXKVe3IRgfBmbi12Bb4NiikBVO8P3-lUz3eKg4XT15Ou3140QyTohdD_np1ZuiaGpf5-ljR30M9-N-nPwN2Pjlmb42z3JogbkAM8cvdQLziDvBZmim1rYzk5umJp4UQZJtmwWQ2M0pdxQLEdOD7mgojhHtKTyde_zUXWeeGRkIYjBCcsTfwODpJkk0Z3a4T5-sUVRegbcSKF9Z2RG0G7IcBp3YH4voAytJO8Vjjmc6_6ynvy6VXyEuusMso3AjmKOKWZBywJXFLUojiU0ngNNUI3sCHghz5U4Xu0tFmk9tbyxHCMoXRPyZDGim97q_2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=mvPEUuA9R4oRc96JqMWkU_qpS-ynxrR_MZnrkMBzD3WnQ1uxmxuQlUW4CEumcUpIjTdSrsj-v7HBn5IKsO9VlYUtuwhqvKcKHl-nAf-B58kdkj29yZNiHgqspGGdey8yG1rnOxXje3c2budLH90gOw1qP9AoicpqEbq-dLB0gzDemAUDinYmZFxjyGf-LQhZY-lkNV79tBAVLSL3nkmz6ysN5zmNbqDVUBisGN-69wWJyM_5ToKIYk5-Wrge4otK5yzYfoPC9LSDXkXLv2i4_zzCSiAbt44cKArgu_7bcdfEvXRonTRz8ZKpxMoxq-WBW6K-nMz5bbWR60Esz7m24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=Y-EIPrhAOrrlgNiZ7X8luJukKlcxFv7fVLhYcV4Ghi1mU5s42s8OvvDLW4c_tj9Tk24WvobqEmAHuAOqGBaBbZBqMMD41zKUW5AVRb5wRdZKby56sWKrMxDWqIBwYMS6k0Fk1EwfYL_09Fdx-aUOR26PiExAWkLQY7Z3pmtzXo6JU2VHl-0AT8M2NgN3OD_JBDhg_TgOaiAFcD0pTJxboRSF-rqWLWX-WkQVqJTDSPsqzO5rwVGeOgScfNqM55-wEviuxHY3I8S1VP6a06qFMucK-zL4pQZyLEU0MfpWpUnJ5BHF4MI0sGy7WcZ7gFmuat_NyBAJjWfQgu97bkbl6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=E0JeZChsoT9J-jZlUqztweGxfySIm2AJlWHzvE3zr6X8FG5RnK-NuIBT8LYhIhtREFerYuEyZjG1vD65276fCS057y7e9W2KmSMDEXT62r70574E89Ii0_gyXUH7C6gqOEcFjnNOTg0rO2XxHu_LrfPoc8d0JLoKLeixFrQcgjQ7TN53Mnxde_NfXDOdZRfaiDtqEMpLaRpOWGyZHsdpznRF-mbASh32GSKy-fHzSYJRuq-Jxs_L2rl9eMfKrUr19peczuP8Y4hpug7RpoMIituWbguaMaN53TEee8W_uuSA4a_Q9EbMqggAp8o-YBdnEjRflMG1ibMBIL-azYc9Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNl1hpjsh1osc3qEo1IY9vTdgMt1lrsl9k7XNpOGYeYNcE9etLSX4-6FXacAycEooQZ8zjfNwrXwaeFo_H_goln9xD-5_jA5PSBV2-MwRipLB4qzWx0Okz1NjOmp96WgL6XayYIKQuBqRekkf_mL7eaQtiVl7wqjgyqjQ4_BEMBiAwPqKdRKcc86mZpfZHq7PJ_oniNed4KiygC8XH1yzMZsYfxXfSrl-SoWOpeaVdEtT1okbQtgzaYq_BNj4lHpT1-nwGnYIqixBHqpSWNLQ46FrdY2klwqNfLLQIDpLRt0jr3Q7qGpcuvxqYgJxuvhc4elzl6X-Fgf6hH-Z7Bpwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFodfH1BHMEeLUV-gksrkOwWv90cafYgEer2CSI_7_-ESLtNepEXYAi0Bor2TlW1tqeBar5_MWNWf_rRLK4gMGOeYmuEvl1WRQ4uCFVKoL1WcmYDCiK2Y7kHnQI7ZifrOmbPIEKo3j40ltCe8fYbcu0O0h2yfvC6dJ2ePVUXh3XSqOAnBI9qVOAJzdxS49xptvs_N9kBTxPSrPsm1bNvmr3UHolhzOKouIBt8gfbXMj0wIa0p8eYGlyh5o7QbWnp9DuKZA84MsTkTUzR9Moru-_14xh8pLaSFTliWO9Ut8NDVZUqwnPFi3FDMJll1W-eHxRbNg9l3jadud5r5v7arQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHFLEHf8y9mg00my4rHF8Q-JTPMcF6taitL4U3WX5zOOSd8UgsEXP_WyRl4Qb0dKgg0WzhT82NeXrpBYJoOY0R1KtF39Zjvcv2k9p6SujCkpobVa5V343mpGLcxUL8YH5JXY5N9OQ9XnK5dBaGJw_hBQcjFEnBEtCQIsvZAOV_R0xsqJEuN6tPfsAIxSy7e_N0SmIYk92gthex5Ss_CqGkreGlTruuIfQayRuBlUzSCEyJEwJcXcpVaMOeHEZP9M7ntIZT-N5LssSXRsv-dQSiBbNoYRS5LbstwnpElf5ljgsR6-dp5fluLcJOIBND2ujMmEWTDbsyfE1M12SlTH9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS-fH3qzGeFuZItzovKGlFk23q_0vh4wbwAU6oSoGWqg2c1z1J_g5Y6N3hKgfvQlLEqnBBVxHLi5jCR6_vADQGbJLYnrXXXjrca4E1QTVYCWAHm179PBxQNSwfAsX5HuOAxbCRFYeKUaImC_YqE5evDETrmOQInxWvLX2GACHZ3wxzpa0cSG0hl9U7cx47THTgc31m4vkwwEUcKmZts-ET4eF85uwXHh0lhrUaR8bVgAl9ya3kInpbWyRXImJG-Epe33hnMzkDa-E2T7MUMR2sbDNnFMfQPBLoxiYbYiezThlEmIfEuLxPydMLC25mzVKLnt1FjClL0IP3PqiyJ_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=JLALEFAEuJy3pWqRgagiHGzoVUTNJJe4Dq-GCeQg7NwaSHSMj03J9mo1HrrxxXs0kHT1JXfGExh2Rd4ISlafwVqCTfr7TXKtMku3thnlITfDRino0lD9nS8OSAfWO2PvjCWolP9NXy89yG9n1VW_JLr3FPIX0usIG_6wjYCOxcBLKaAhPN_Lpp5TYph4uPD5e-x8ufy0Q2eIEk6_8mTz0Ti_RxWpdAjP47QhR8hg3A0shcSQnjBFws490IWdpciMxTJxbpchu-kkttXn3G12v8od0EeBFhn-BfVHiDnzkNpLhfIR9t_VS3t3zwWbvPSA0bgv14WAW78TJRWhZe3bbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=bjmCyKpod0FvrEZTqNqs7gBTpPlzQ4ACvFsD3gC7e3iIMcAfg4kf96tOf3eDB_oDn3uQYQRPxQ_8c1XiLZ4BeTiH-EQTh3u0qy2W0riBkGOTfGKj8QoEOEZja-OfXg53rZNkhUQlQOp1VjM6SPQKctqsWRZU_lm3x9d0zoKpCTPzyrKNg4b6GQLXI-WEv8iucFPEfqQgvTxNGoXofdfnDtWAiJlnbWcGLFe3DkDbCtqE8yn2w_A8SUUlcWJ5BsvhNr6gQrdYAyn3yRgSc4KPhSLjEQpZcLwq4xzZF6ZvOJtk3KeFRE-np0ERcqIPcRo9i5iupaNH4Mh_63NGW0Tpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=EadIj45nYFyBHcPkfVnQmVwRbROMKHZlNhLTa0r_CFjgnG61Buxz2Otw6bobUhNcX0U94hmF7Lnd-a8V105z-y-wXsac_y_gn7-Jbmkdxg5pIbbnd2C0IBxIbCwQ11u_dX_KQnOAi9uFg8WBqxhgaP5d8bZ16TS5BkoaKVdUpIn2bZ_MpDcxMXTbDt3DAiEXoIp31AdgaKkDklVcjaY25udT8JO5BrDmXTQK3NLU42oTP6FOsrwPv-4A9RrwuLeTQIwLuorBoWSCkDeUV28gH7GWFr4FJzEWn0MVjuMDTOoLjVP8WyKxT75cPmFHGbVGisHt81GVy9FsCGOj2lKHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFm06uSYg6159Puts4R1f_fpEhfqXtoJ7eyjgLVjtnMxjCLgrh9Lb-btuuY3_h-vV6xwg7H75UQSxhg_2dAuKDJbgb_seP1ty53gdBFDuY0mGyWxIxZs8fM0K1XGHSfJmaS5Sja1UimKL-chjGK1RkRXWkx197oI9cAl8xQ5WzG-a27Y-BBcwW7s01gOKlZpRHiJp08NJ1zljPzQ9E21hAag39Y2bjgb65f6VU6XfivzUmA5YyIQEpm781NvGvs3CbBOHOGV_nQcxLd_5dRXqDV0yrFuA6RPWy1Zm-LItURLndxvGmD88GxL09x55nvbD7pXZxljl72xUGtO84A8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=oSmrcDH3bi__OqeZLupTGPKauVojLwNvDZn0_AncEwRo6JSMe5TqDC53UKXvQWc1zHzMWiGLe_0TRQL-0-0GrKELQT71uRTgxFOA42BcH6rBGa-Wx3Khpz31EhWjWYX2UWpMNfmI019aA5rb3VDt69ZPs2hqx_GWqi9-fAd2b_4GreaOiT4E6mq-x4WQ1WNSMi_xNQYE9WIsUe46FRD3RJIHCVfsvlTNVAvyacZHSchnIcXD-kzfSmynuLzEwENgXQ_zarPJKBwMTAzsVNB6JpNy8-l_KNlWOmxHSWVHYiGWQJCU0WaZZiZUN2mjldOAk_dPTYLwHuhvm7qrsV4bLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=BRuj3x6ARAPp7zMP_wB_A2tiW6YjGhacu3xqvC4RHpT3vBChRpXlxD1x8Zub29qPRnynPdDc7a9l6nkqZvz95e4xTaidxRkaAQ2VNkab8ThvVEYJ_ZdPYWR2ObyYP2Ud57H2SUvjNORJuZbJsyS_DNmYaR46DiBIlVMEGBswaxNr20KU7GbTLfRZPb2az0vIwTOLJGUZ6ZpU0ZutICh187e0L0dQwQv4hXmidb4KPII4cmh9qAUc9j72N7jy51c0ysqlMYn48-Zx9foYFRWtuoP8CpEg0lyZSGnhHziUapvSQaPp0x8Xwq79f5LWElnkcgCxtAjMewkHKLtFVSxaAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm2dEeQh4y_skKjM6wcngDG1C3Sx3amBxupjkJggt70mQz3C87wPfFs2uBumnrMEGbRuvXSoN7l_wKJ1PU41F58xvHafyb0PYsPGQPcD1RFcWZBfCOXRw6vRMd8vElH5wVAwVu6ZXHQx32_ALO7IDQEnqDSC2oaX5l7YwgFbBLKhDkOis7vq34m75r-OirT2OXXG_KqQdXTPzRPNiMAkpOKl-U9PR5nWMaXwoCGH2yCsRXslap9HAqDxlFw7Tuv5UEML0MIm1GV18hpgkVRLDmP3Hl1sNCKPe-gYXLMU3y9VBcxKw9skFnOMhX6pf75rbqwn0Lg7ZasgrBYON-WtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=CH7x9TwX3aIKYg8M10Weplll_oP2qMI_f30n8chzeCwlRDMEVtwdiDl0PTk0kGNQB_IijCujLlDt-lCAhHjIEUVtjRCjrjsvz_asOLWnOEA8EUhnr-uiKqBl3finE_VZ4kNxapAt3MMaP48iJn3Qbifgy-wd237_CNPXjhgEM42Mrdc6C-wGB0-l0YhpqqOhh9yy1nTiJdlutoBR_TXNBfu6y26CCPm7Na-VwER1A-e2rn2AZ07GM6yCtYVDjQT8y5kpeZN6SqpBe4Jyp84SAqvVl4nh6tSuL8lc97BAGxcg4vj_TURENcaG6MdNrLil8JK0pU1Flks8PAPHBgV5ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0J4m7ZtyuWxj8PMAdFOSR21Y1e--yjrgtV_VEOMLZ6qxTxYN5MlqAzXoOnbZrtySATY2ekmgbquDGE31pz64zZQ1xH2G-jqptmLaQiQN3PPygLUQok7LD3YcywAtGpw7KYsosoE4CPpu_CCnwtFpWB8AW0Q5WrON4eUlXwCjz-rHdOPI3j5S8F9c3vKESup1wQLxZycCgszD0ACYlB3fmTtAxspMTmYHNZg6Ak52evG6xW9K6XJzN3yl5b_h1uoTqJh4yaukfFNswRKvKcV50dATNvUraOAZ-HCIky6p_MojGgF3EOP2NYtzT300yIqW7se2FYyspVnkjTNFONvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwJmv_LX_PH9Wt5x7I4FtLznHpbeW0mQpU8A-Thzfpwvl4keth9dMp2KGYVg7bffiry4hc_2jKo87G1vCOKts-TOKaa9GoO0VKgpZUUkPDvNB48DTmlcmDuyvtUpGBFhW4shZvkgR0rfaxjQ3V6c9R8P0elnphSLiCKXc3I0xI40JwnUxuOqfmiWRft5g7V0hxEIFdjHEHuwVzrSRyJmaJur8dlKRQxTFoooPWf1dK_PlCpt095GH2N0zHZC_EwvQo8FlFyQsRkbEr8z8cvgsaSJqGz4xshfMIfm2y1wHVG0O0Xro-D8OocGd7pChNWDuwfJLwAQvMwi4V9ZsvCYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=vR5IPMukM5gtvdY78U7RFsyeeMmhBkW7KaMLumD-gxqI1fCuJHpWr7SX_zHMIMI7mdjh8ffcKg_jf53VRlRk_5waV-7eFqxOOQlUmRvGLTsF7Td2GNAFfbBYFTEx8XlqHmMT7miK1D-KSPcj-Ql5S51A_GZEWwfz_Tfi1oHrWP3KMbEEQUNlCp65FTUE6V5kd6s6wCIkxy1K1XaMPN79TKNTFvfAv1jt2JmsfJ4McUa4bIOFhoTOHwdwVunBXhc74wbbpNp_zLp9tF0SlBqkMvw5G2pReQO0-f2ifT8ZNRsV_Gn3MKp34Gad9k8uiT5at4bLtkb1HAAXXyqK6juBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=O4QCZlwpXNBXUd2JP3gWj4stwj-hhQdVK8_llI9vVFen0x7nQrlgGZEXJk-symLbTSEGwOqic1zP3Pt-_ulIZACbKpE43Peq9E64VizSStMFehQEgevzrU2yZJ6lfc53X6Jefp_BACz-z1byjaFF1_2qtmJ8e3jwXzPBDrNtuDMFkmsJhWevUXUVcRcWEC1IL0jiWX0OvSIvEpY3KfvbPpYcWBwCaAQIgTHrDumw-Qo2bpgXIobPgXjttKdglc2p9tz2GEImtRkoldA_781EoSJF3UWAs0NtqxG4Bw6ERg9DuNPQIm9LCGHXQixLn49M2OZ39IggzlhnhCcVROM2xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66827" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N44UMwe8q28-Q-74uWtaP9m5w__GCj3Ww9kHgjiIC3AkfJ7CyxAl4HIRuAnEcRiRUBug1HDGlLLeCzlUlk6AV-PS595ZR-GZWDKzN-NjXwBVl_d4OUO4nDg-2VB2b4324kI0Z9MJpUH_6anTjhEoJMsqJEYIAsPpIZ1Za2jeYih8tJ1DkK5xjpLEV0ZMC1VTfXz_YYU7fDK_YD8f718NDWN3-muN4ZZ3xdXto2fcdiC8LFVkqz_nboxKeX24dp5MowKHIm7mgyzRL9PgFrXFm7Wg4igr7zhjwRNfReqQBUyOS7hFlvO5owzjlkoNxr_BCxfuMDumMlU8imPW6F9F7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66826" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66824">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO9aANO2Rp94H8_pHpOZD1OWzEquun0J1w1KPfUkLywkaOM2ad9Z5BfC-rHcLCwc8kgvNMSGESoraTu6vIyTNZ3uteyA-POYR5EbghfQtD_k1VpgK-AeIngy9U12aRAJzdodlpMSLr7pYdVsLQ9aru9E7CwcIPYtEDawqoFbTNjEMBZJTUU_l_2XjReMGnI6RAmJMHqxpACdwbVdoZObedPN2ypUzV4A0Rq3PLv97ULb3ixi8S4qkE2Z0Yyz2ZfuUiue7Q-bXX1p2Ohb-62gw6JZHF4Rv-C3uqnLiBksZxJiq1kYcuO_g82RHW_Cp7R1v_eRNNXdCbYFqnlGgPZWQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b8ae4df4.mp4?token=fDlCVhdwwJakdI0qt23JHOP17ZKO4_QDgaxWYAKllzSDjUCn4yuAXJWVVBLhWhioqDXVLiZ6MFKi8ONMiIxQV_v8_NwUgHyvBH0uXLlGtAbks_4rroLi3A6KlMDVMyXJBbXbYrLC1-eZR2lH731vbPz9c9Ty5n1wXdoBGQCqFgI0V_3I4fyuAU33ZQONebllJvkHo0ROdV1kjwzS_vs0J2ZxqPtLmTF_DnFw4jz3R0y_LqDLIXo6bNVNoU-8BTn1145vVygZWKfj2tQeZ5U9UQBC78TMamfMZVPA8Yet1pqw-PSZUdQoCxG_k0IH6VPpCwC5Ao4Y64F8KUe8QfK6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فستیوال محرم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66824" target="_blank">📅 19:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66823">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113cb570d9.mp4?token=UsBpEaMyDCTCDtrZDLoHtEuNRKLPnzErlz4oji0z4tPlBb3hYqaPY07VQFWmLiWUzwUCUA-W9AxoX7ZvioHQN8pbiDsiPW78Y_XHt3Lm5QVr3o4t6wMiDR20toPGtF5u1klrCgsstidVXwu5aTtPNXC8bf0wRnfH9fTG_B_EVzI66y9FSKxFBg5e1FXrSwgkY-cMiY87ILRp9En1sAKng4KVuEyPWkrBaX7MY6OvGnTwPmE5hfopB8WxIae2ESsR3JNdbnl7kOJOG1mFU-EdRLs98_Fw67Z5ddyCKDein0oG1m-Z4PTepEVpnSPgg0BvGJLV73x9Wal4X22ySAXpmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قالیباف پاسخ مجری صدا و سیما رو داد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66823" target="_blank">📅 18:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66822">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0453856b46.mp4?token=J7uWg2SH8lrpIpAkMbkoxcD-9GP32YGDHGVBReZ8do1fvg7mZQrlnKYLEs5zeywbZBw4vr-qKQVzGuhW4PViaket8Px8xKHTwJlGZgFJ0w0FMqaipwtbSSRgOrqf5A5hqB0bPu1HFY52GVQNOkcSF8MEMqX-OKlb9Jy0-xIeUIMzZJyJyBqYdJgHxksUFZT_n3Ryi5RFEiXyJu_x1_5ppX_7cQev_U6s7dhYjo_bJKomFFj4CRE9XZAwA29yeTT3-KQjNobpyRBB4-DcoYJOMKAIfhnuOQTuLok9VwylRn0jsMd2Fos1IBFlDyqiZWlghgYiywk2MiXrFZCdkyvtKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
اگر کشتی‌ها در حال حرکت باشند، واکنش ما هم بر همان اساس خواهد بود.
اما اگر کشتی‌ها حرکت نکنند، این نقض توافق محسوب می‌شود و در آن صورت با یک مشکل جدی روبه‌رو خواهیم شد
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66822" target="_blank">📅 17:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66821">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50938460f0.mp4?token=i7qWMzA2gdXFZOJ0RUtdPlmlyvJCaND5_8ZDH0x22fVcr9ijWtRK2LC2UN6YYmeQDrnI-3bbgLzCx1Vk7TJhGlRyorox4rACP3uSokT-wL1L78ytg6LIhkbGWM5dDApbnfMa-s5FrOoKUEm-pd4fcFIvcupaq1EUWFNUtHQ4ZxJLUeYbJn4UP4qvZ0Vu-c6f4aDnqid8ENWmxSNh67jz8O_mKYJnoFVSQtzTwjyJXOozLyM0xv1BX2TDa2uv6Muf2Fy8PR4u7_OgXoVTNoNGQ6Xyjl_mFZrLvhh8iE8mgogDt_WdbfX9wFD4br2Ajv7BWiPr9N0Wb2isJMybHSKpRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
🔴
فرض کنیم که ما کاملاً دیوانه شده‌ایم و عقل‌مان را کاملاً از دست داده‌ایم و تصمیم گرفته‌ایم با ایجاد یک سیستم عوارض یا دریافت هزینه موافقت کنیم.
این قرار است چطور کار کند؟ اصلاً شدنی نیست. چون اگر کسی هزینه را نپردازد، چه اتفاقی می‌افتد؟
فرض کنید یک کشتی بگوید: “من این هزینه را نمی‌پردازم.” این مثل عوارضی یک جاده نیست که بعداً یک قبض جریمه برایش ارسال شود. به آن شلیک می‌کنند.
اگر به یک کشتی شلیک شود یا یک کشتی غرق شود، دیگر هیچ کشتی دیگری حرکت نخواهد کرد.
بنابراین چنین سیستمی نه‌تنها غیرعاقلانه است، بلکه اصلاً نمی‌تواند اتفاق بیفتد.
حتی قابل اجرا هم نیست. پس بهتر است همین حالا این خیال‌پردازی را کنار بگذارید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66821" target="_blank">📅 17:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66820">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ6praqAha_MBkP65yUkrEm0NDEHf-w-hwTOqXynpVQWId-ECFXV0LLaYegWfNVSHUDWkxJRYEHj7N8gFukJ4u2MBFOYhko2b0UZMQaqZi2YlWkjP4vG0ctFbIubsWBHZwX70UglUX-kibrLuh_QK42Q729HP4vKsrrbkRrUpxEa3AcpcJFH4SMxVIKs8LmtgzIcqnrydAlFxL4l5UjqakNWUVdniOYUxdrPlvnruESood_klGSO3Lfw6QnocfOiKQiGsNdLLvfGGfbrMcCp8vW2UAYS-tBp9dh9bYq56pukMeYmeG1HmtRZgDsC3zAdENd1sHjT6nzbWXmQ0N_Cjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
آمریکا به دروغ ادعا می‌کند که دارایی‌های آزاد شده ما، کشاورزی آنها را می‌خرد. جالب است. تنها محصولی که ما برداشت می‌کنیم همان چیزی است که شما کاشتید: دهه‌ها بی‌اعتمادی. این محصول ارگانیک، فراوان و تولید داخل است. اما ظاهراً ایالات متحده فقط سویای تراریخته، وعده‌های عمل نشده و حرف‌های بی‌اساس صادر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66820" target="_blank">📅 17:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66819">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/477cde7837.mp4?token=jh_jiZAGx0grdWvEHb7QUEEUWsl9bEnFUdBZFyv4zkcr23xgXtM3EG3Z-7MRQiCV58gW95GFTBHuj4X7CBCjP92a5RMVwRLGWx-LVIZkTbz7R_EAA-xr_xg_mT1Wt7y3t3tz7mXJKQamo4wMDVrK60BrtaXbmjzuVeywgcqTUhfeBRPuLt57JtunjHMaC4Fb55SIj1SwyepNf8YGolCRIRaycsb_jrHtGrAFoGLPx9R1ySKn0sBSN4UhONyMwOQIaViJs4mCwJm-gNGSNb548KjAlJzMJSOHZfacY0iGbujrD85aOo4IhG_ZyI0hoorXTdhTpvjkw0seSLclOSyDyjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویرانی‌های بر جای مانده از زلزله مهیب ونزوئلا در شهر کاراکاس
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66819" target="_blank">📅 17:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66818">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K30xs3ZTn23nz0dITGwVfHrF8RqJPQiEmvRPou8SMslr9ukPTeWUpsAWuq0_k8VnMdm6PN1E5Hy6LKvy8pORRi2IJIJiqqHDvT9gFWIALQRl4UARH8n4k3KrDsVtF9TdQLyv01QDnZUUNQAyPEm5fNX4BE6jA7TD0BxoQLgHIIpFQ87UfK4_BfkC8lcFpByV7lcWbd5CVMlQOFa0QC25bp2QNGLqFUfx8IK81PfBpS5m-XNWzQoTH2RHAatVAWVQR2gSlzcegOuukbJmVV7zdGfb9dHNcinjfpDO8s2-A8O5P7H7rJ6aF-Hrh3PHQaVnvbhwwUaNTLqvTWrjWhV_vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل قاآنی فرمانده نیروی قدس سپاه پاسداران:
اگر اسرائیل امروز داوطلبانه از جنوب لبنان عقب‌نشینی نکند، فردا مجبور به فرار با تحقیر و شکست خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66818" target="_blank">📅 16:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66817">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4301a5bfb2.mp4?token=cEq7FKT7yvdPFdoL-tuMYmZHGfGBww2bLMCleOH73Bs0aPTG5rPzX8ZjC-Qp0-PMPq98B8N89c7LgDc9gkrK7D3E46QGpmf9_FsWOMGs-7rKr4wxTgMXiin69s1nm2zf6xvLPznVirlrdpbS7TQ_EZ6Y2vpS16YtwkuACPMdDfI9iKxIngdMkbrxJuGEcCIKAh_Hvm-XKjAWJys6BC3i-5cl5bvaQ9JEwntTPLbMZxlHqRSMIH3wOeEw_kbjXZIMdAoj41_EuxhjlWPVQIPM1qORUWU8ayQnebowCTqMLj5EZhPOvnpIDDg6ZPQH47LSIrjk0UOGAOWk971nBWawXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
نیروی دریایی سپاه:
تنها کشتی هایی که از تهران مجوز دریافت کرده اند حق عبور از تنگه هرمز را دارند و با هر شناوری که از این دستور تبعیت نکند برخورد خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66817" target="_blank">📅 16:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66816">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyQWQv9t956qB7_sADt_7LGEO7autf7AcXedklp61k_mNfuTEtXBnVx6ZGwUg84bs6BYuWxYcg9liLj_IAReEOWCOv8buGt4hQtIjr1t9r1U-_d11SzlEtPBrIxN7BJolPSlvkpziY5sqKbO_EV6DgBshg517G2_ooAn0ZL5Yp4O1h9M5oDxyjQu2J2OKi4eu8pyA4gn5Ks56fQTbt2qNopi5jb2tm-sfLWVerq9T0NyYRp8xlNVhtgTN0LijzT7enzhfEbkx2f1mpLjPzhdADDCe2A6I1xwmHtT5hlfo5gFfWCT17PWecsNwMdrAVmLldM3d0_rvmYmkXZJ0NevCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت
ترامپ در تروث سوشال:
«شگفت‌انگیز! سنا رای خود درباره ایران را از ۵۰ در برابر ۴۸ مخالف، به ۵۰ در برابر ۴۷ موافق تغییر داد. رند پال و بیل کسیدی رای خود را تغییر دادند. از جان تون، لیندزی گراهام، برنی مورنو و همه سپاسگزارم. این رای به ایران هشدار می‌دهد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66816" target="_blank">📅 15:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66815">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
خبرگزاری رسمی عمان:
وزیر خارجه عمان اعلام کرد ترتیبات آینده برای تنگه هرمز شامل دریافت عوارض از کشتی‌های عبوری نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66815" target="_blank">📅 14:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66814">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a64b900d33.mp4?token=IwUopvKACKhCiBFn736r3u8zuGJ1ZFX2Yqkpm7GtO4x8A8cWaty8hVMTl1VF7zYo0f2VYCAyySTDs2FVbUoh5Ofmx5T9FbH5C6xxTUzFbMH0j01Tx2H8hAvVgjJRvrs7UZTaFxUB1NuXH4Xns14ncW0VMpFCbKk80k8AU3KpYxqQ-f_RWCfEZ8OTjUM-nv1KWabFNxLls82Zva6D4N3wyNsqCwYIJrFtLdJ-UWaP6RF0QBW8mA9I7vzSHKurtutpvbjZT9tx4_Jvfc0h21tLyIyE6RElzOoSEXgxysTCb-tvxs6GznHQgeFRbqkHE-CDEcpwfPNhu3Nrhynhc3gcIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره اردوغان:
🔴
او دوست من است و از جنگ دور ماند.
می‌دانید، او یکی از اصلی‌ترین گزینه‌ها برای ورود به جنگ با ایران بود.
شاید هم در طرف ایران، چون همان‌طور که می‌دانید، او طرفدار  اسرائیل نیست.
و من از او خواستم که وارد جنگ نشود. او هم وارد نشد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66814" target="_blank">📅 14:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66813">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YL4zRlLMw-NoW7Z_chXkQiHRKXwrDeKkS_95GPUwA3mGEl1IzqFstZUvqMc7AOkI1HMMzqMNJ7AKPUcp616OPeOz5pbqK5IUV_8j0gY66ppBTE3ZxWeJsMxM01aJm5Puhen3sTarpxkxmZsGMFutUoFlc1WmtVDh22i4utoWUOsSUxHGmTtEW7lz5VDygagRhGyiuJZDEsPjWUfc77Vh797ivsTOuTBILfTHFs2c9CweLCIgJg9teKKUvQi5-CxiCc8HJOl__jAl5NS8gy1BDvLPpZi1wlMtUNgdkHTeDkDkvhjFC-UvM2dhbiwFrOSGelf4vcOuzyu5QTsfqWQ1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
🔴
واشینگتن خواهان توافق با رژیم  جمهوری اسلامی است، اما نه به هر قیمتی.  هر توافقی باید واقعی، قابل راستی آزمایی و همراه با پایبندی کامل به تعهدات باشد. اگر رژیم جمهوری اسلامی به جای صدور ایدئولوژی بر رفاه مردم ایران تمرکز کند، آمریکا و شرکایش آماده همکاری خواهند بود، اما انتخاب مسیر کنونی نتیجه مثبتی نخواهد داشت. هیچ توافقی نباید امنیت، ثبات و شکوفایی شرکای آمریکا در منطقه خلیج فارس را تضعیف کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66813" target="_blank">📅 14:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66812">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0835d639a.mp4?token=ckNNQinrkqo1PGRBgC9-avfDg1JAIeU8ldggS51f5Pp1GnS1Gkyr6tC4zBjXTU5ib4COfBWc2mkuYNMmeGN2LXVk1Ow5AoV3tu22IHih0HOt2n-o-L0DGjgLq1Bwns3_wAVl0Pv8VDi3M0IxOjCvS-8a30NTfsR-EX9m28ROtUk2cAzGyHQI1fPy53dJifzTPy_eKT2gMqr4DpHkzpvmbSeP7Pv2vNbxSz3nB2ChAIGHg_cQASZPNRDz1QSkgcVdd5Gqpx3LNOU_YBiDU7gCmi57gJBqe83yQrtPQAchJYRTbg6uL3q-fr2ztMuxNVbLCRWkivL6_-SsmE4RS6VeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حتی در کیس بیماری هم عجیبیم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66812" target="_blank">📅 14:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66811">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6df862a9.mp4?token=eeCri0-svgEwM0NN6QXC_d_31mrMmCE70LDuMWoZnbzlil1Q6_P6WAoXjVbW7sOCD3EQwhOp-97LJwlvL4BZRlYrTDnKNkTR_0tFtPzjw1pEhCBSZJmK4kdHdX1gCZz0smYnPQ3j4xEYWUm5P54yC2lPuHAAPak_Nkcc5xm1THIWuoJ6HdL0K6_5hhi4f-VEv8jHsKvqpyGkDGnxxQMdUoTQZYM7GF4vB3tmfVqRGCRdksOyt8ZDpWDfVPiCvPo2sR6j5sSY3TlDfRdEfoLS2Q9vLM8AKrn65araa6GqJA2Avmg60xfE5qBaJE2OObUakP-1diWpTVAv43TaZjJvpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حدود ۷۰کشتی در ۳۶ساعت گذشته از تنگه هرمز عبور کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66811" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66810">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.2 MB</div>
</div>
<a href="https://t.me/news_hut/66810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
نسخه آپدیت شده اپلیکیشن ملبت
🔶
• لینک سایت مخصوص کاربران خارجیMELBET:
🌐
t.me/ConnectMELBET
🔶
• آدرس سایتMELBET
🌐
bitly.uk/connectmelbet
🟠
نکته: اپلیکیشن بدون فیلترشکن کار میکنه برای ورود به سایت باید سرور فیلترشکنتون رو کشور های اسیایی یا کانادا یا ترکیه تنظیم کنید</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66810" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-WXpQ4AqSuRL296hKpHenFzlX3OvpzYUg3D9sU8A1pRAXN2pQnjyXsUctHMLRd8P2KJFMHWX1b-ZbP-bk4waFk-eMHbh27OW3NF7Ff4WuUTrSswGHfdYPX-x4xU2ENou6mytskF7XX9P-hBR31pXG5Q1T0umnR8FcvOPVrcDE8758MBgPU_grAgEwyCaGo_KOx5z-MrgqFve4df80fm3fP-aubDQeZf0WbkB6ueZhUuEeVS6iLm5djZuErWvGfsRJcjXMWzyG7i5mL60HyNHQtFhWvD-4eNgYhC-UkC4FF8sfchW75uL07w5NP_oR_jr14w1u3BCPZux18sLxSIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
بهترین سایت برای بت زدن سایت MELBET هست که مورد تایید ماست و خودمونم چندین ساله توش بت میزنیم
💸
با اولین واریز اگر با کد هدیه
ml_459049
ثبت نام کنید تا سقف 100 دلار 130% بیشتر شارژ میشید
واستون لینک و اپلیکیشن ملبت رو میزارم که ثبت نام کنید
🌐
https://refpa3665.com/L?tag=d_3312431m_45415c_&site=3312431&ad=45415</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66809" target="_blank">📅 14:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead28978b.mp4?token=FJFeYKtGKZ4Y8j2TpcGsJx1NiADoGTsnENT4-HbLuaVk2E9mOrPhd0FhQnAhBHK10F7kP2UoRyFvHIKl4Xni4wEiN32BS9xm3thgmm3f3OVGyQJwrSMhrSNFxcFA7B3pK7XmzHvI19i2N7oNvnUzvnahLHG9vNsFVfTMH-w4w_puKapoImBO6WYOgzj6ORTfPQGE67KulJBcWyvIOlVlhmw-h5wWvuL-Ku8Us7gFo2UmVKoE9D9yzKKD1tzRwBIU3E8sJGTfa8Uq72OOB1CeljppjA2KRT1xWRqn0UYo9kNB0wl_CQCrvj4cbxPbT5H9d0-HeWGP5C7Wm_vGpaDiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚬
بسیجی‌های صادراتی دیشب تو میشیگان آمریکا نذری بین آمریکایی‌ها پخش کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66808" target="_blank">📅 13:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66807">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba9d2db1fa.mp4?token=uJffux244wgCBrBA9_GEdL4NEQxwajbWUZq0Xh_mTBRuzDBBoRAtxVZPVFR_B4qVXzK8yzJmGkTRgrXToPGlw8nk4XKUyo6yrB67ORoT-ESFqysxs9g_7hpmV5Jtli_CuTy-QgMcy5WEEmw07toa5xYNBHRlR8HYedTEBS8twmMxbpbO7qcYMkd3nNfwSEGR9XlbCeCB3U4DhCReN7x20RV2hchx_g7APUHwWN9TEpNY7UW4iqcI8r4pAuUHsU7Zx3c7qf3gPWL2PIHsG5I-OfPkmSb8upwp7EAYwa88oI8AnVrBPBPN-Ty0ZJo0nuRwg4c8rvcqwtDbaFaCYh1QajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنوز تو این دوره و عصر مدرن یه سری کسخل وجود دارن که با عقاید عصر حجر خودشونو بگا میدن
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66807" target="_blank">📅 13:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66806">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f4c39a8d.mp4?token=jsP-a0FaJrP9Sd081EAtdqLlsJeRQYU0dD-U-pw-on5WFTxj5FWQ6AIO0PVkUyG1b4VbRQH8HKABfpknNbpCLbSH_TSNTdV6ZZJlGKT2IyRYMWzIHlykJSSmmgiBQj-l4FWB8EnELy8YBzomVsNAJso23IrBUrtKZvEc6VV74vlR_C64cgGRtYj6HPi8Me2AfMr44iE_7-OkBM-XOaRzFv2AiMIQhMXHvSXzYLME3jP6lEU5rBs9ceCsrg0OhrbnsEXhwKtO7sg8r1c2iWMi82vEr8MuQg2skFdG5JNcVu_nylJY_iEbw10Zk_3e2-dx-xNbiXgkjfgfqv0b4-lsEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرستو نظام با کلی عمل زیبایی که البته هرچیزی شد بجز زیبا: قلب من با امام حسینه
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66806" target="_blank">📅 12:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66805">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f836563943.mp4?token=JsWy0QugrdKNt77q5OeCKV6Nr8pggJqk13vCZ0pQ__7XD5lzm3nqXh24ImOCPo0Zbxjt9mH0UWfxbEMb6uWkiUypmY8wjvk-u3ooZ7L5YpfQttGp2v7O-WKUHZ8k5pWUrUwnKeEJwfDcjxmYQzCHM6zbERfb0UQ4yUChi9DU7QZ0Ryhshc74Pyw6auMuP59KPhdb8l4dH-gPcej0NDrfT5P97WX7Kz0xmCOi2MQK0qakXUtOiFe7mkCeIqHDNxoVRmq5iVrlvUkyshdSIPhuKhVPaAlUM7YhgeWkLzAZjnvpetQx-Zxslx26orN2bUl06N0Xb6znI74fMTQmjkPJVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از هیئت‌های گناوه بوشهر یه مداح به این شکل از جاویدنام‌های وطن یاد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66805" target="_blank">📅 12:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66804">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f61a8cbb.mp4?token=p-wk4mockM9oIBVQ2N469o6ddg3V_IhvtodgkfpclK_vxlqAtlohZwjo5GXeOAhdnh6U1hC5FuCPdaGvwKJGZnHnuc-iYMFnro6R9o3eE--XNDzzXPxq5WWh-KhF2D7f393vkRDCx8EHaZrezdvHU7L-8QP_r5E0dpUabqx4NmxsSfVjMKpxz8AVduzceMRZis019QknkUfVnimE69Q0mTAGa7fySasWgLUKbIoUFZD4sdonln9lgDEnBEV1LupQJCiZUNabin4rscSX6_d04mEavWkDbzcBkd6Jqc8i2GH2921TXc8AeTbivmh9-aJTCCa8Gg9I3CjaEIazH-uSQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیره چرا شبیه یارو خپله تو آل زبیر نشسته
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66804" target="_blank">📅 11:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66800">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=otfFcKeWFNJhrGNQcMHDQAuHgPPp0S2gIZjPvbDqYeO5Vu6VyrnmVtlmX2DYlSbvNs_UgCfvncMo4xVNb-ftqgvYhInXJrGr0VtvLF5JX2eyfWpQiBY8WL1dKLyLt2thawT6FnkCfRu_GYdnRBkaPOp1bpdZGHXjNl50XVZHUGEVclrfGptYAeSKOGkX5tjSNgCgDX8UCdJ21dd9pATqXpaTvE7MSQqWWllC2OpQOSrEEAvxJNoFDRgFBFib_sezHtDUxhVy2cQ89meGTqGpB41a72nGQNCQA9uZqG2Q7HlqJR0mpkUY0LazcAK-6csbJweL4PuNhOYEob-x9d9xnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80f5246ce8.mp4?token=otfFcKeWFNJhrGNQcMHDQAuHgPPp0S2gIZjPvbDqYeO5Vu6VyrnmVtlmX2DYlSbvNs_UgCfvncMo4xVNb-ftqgvYhInXJrGr0VtvLF5JX2eyfWpQiBY8WL1dKLyLt2thawT6FnkCfRu_GYdnRBkaPOp1bpdZGHXjNl50XVZHUGEVclrfGptYAeSKOGkX5tjSNgCgDX8UCdJ21dd9pATqXpaTvE7MSQqWWllC2OpQOSrEEAvxJNoFDRgFBFib_sezHtDUxhVy2cQ89meGTqGpB41a72nGQNCQA9uZqG2Q7HlqJR0mpkUY0LazcAK-6csbJweL4PuNhOYEob-x9d9xnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تخریب آخرالزمانی در کاراکاس ونزوئلا پس از زلزله7.5 ریشتری
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66800" target="_blank">📅 10:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_gho_jXcixdvCGbmxzK1fjfP4aRMJKVTK5v9kh7PLjIcJNHBnvl5_AUp12_xndNaI3sice9hRMgnLHS-NyWlEziPZsfbi02_5muDiSDywzw_TMOO6Ecrf7TZ_1ytG1QS75ScVpvWTDdLe2Ihd-BGaxj1uY4bgiHADiSBvU5rrMKLJc-ZsJ2UCR3aRDoIzI5KzLH8mOZTQ5-SbnweBkXC4deTcr5GJTOTluIeCSmCI7NbYe7Mc4MtPhIQB21Tni2rA8Un4FrAtvTZeN915WFB4XF9Fm2IpX--QP01s4YNBEr2HMJD2wmIW-vQ6bHWfVKn7WiZotQJMi9xmrbMjrchoRsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3743ac3a0.mp4?token=gm_iqpngBWLI5-TmXMx-BUfPJtkDM_pKsQtS4tqz8eYT-0RDCxp5cd7-2lNrMq8sU3Sj3VfYPi_QY8JLyl7JQuZWP8rU7GQQBrDQ72LgzbtF44L0As2fXeLiszSZhE7kursQNJ1HaV86pwf3emnNKPtGWaeqkLz4XIGjb6gFvNO4slMJahyrKpTsrMAODMF6dkTKiTtygk9-EHOYKDa_LX-HiX2x9KQ_BCDv6WW6Yw38ZIDsn2FQtJulm742X7Z6q669tt3p_l2gnTDbI3RTjzdD6b0VqQr2BS_zAeJTHP9521MxMhPJUxBUJ8UvIp9GaJ_GDvM19kkvF6OzOA_gho_jXcixdvCGbmxzK1fjfP4aRMJKVTK5v9kh7PLjIcJNHBnvl5_AUp12_xndNaI3sice9hRMgnLHS-NyWlEziPZsfbi02_5muDiSDywzw_TMOO6Ecrf7TZ_1ytG1QS75ScVpvWTDdLe2Ihd-BGaxj1uY4bgiHADiSBvU5rrMKLJc-ZsJ2UCR3aRDoIzI5KzLH8mOZTQ5-SbnweBkXC4deTcr5GJTOTluIeCSmCI7NbYe7Mc4MtPhIQB21Tni2rA8Un4FrAtvTZeN915WFB4XF9Fm2IpX--QP01s4YNBEr2HMJD2wmIW-vQ6bHWfVKn7WiZotQJMi9xmrbMjrchoRsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاروان اجنه و فرشتگان:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66799" target="_blank">📅 10:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/638875c442.mp4?token=fgr3rz_CcuNCAU01LKTMvYDyEi6g4J83iNaktC_ej0-mqtznES0U6q5cm0-WiqD3yAYzlzsxamjx4dnVaI0ZxALYE9p8iG6edLDsArplOQPbcYUgCv85IpNt4aJjfTRF-qYTAfNWBc7gVIW84mSs1N5Bq8-rcEVbzeML64fh-7NfngFapK94FxzuXcYOVl7NC3WGkC7_t1Q11gwpF1i_2Fu3BuaKR5mRvv48R9qeCvbNYlYRE91r31c0kn-zo7QyWTEGevHtGyLfbkzbgAi0dXO76U-0rd-Jo5xbje4C8ujxt7wuQ_EigFk0V6gt17TJ0AE8JqUSyzA1I2cInvonNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/638875c442.mp4?token=fgr3rz_CcuNCAU01LKTMvYDyEi6g4J83iNaktC_ej0-mqtznES0U6q5cm0-WiqD3yAYzlzsxamjx4dnVaI0ZxALYE9p8iG6edLDsArplOQPbcYUgCv85IpNt4aJjfTRF-qYTAfNWBc7gVIW84mSs1N5Bq8-rcEVbzeML64fh-7NfngFapK94FxzuXcYOVl7NC3WGkC7_t1Q11gwpF1i_2Fu3BuaKR5mRvv48R9qeCvbNYlYRE91r31c0kn-zo7QyWTEGevHtGyLfbkzbgAi0dXO76U-0rd-Jo5xbje4C8ujxt7wuQ_EigFk0V6gt17TJ0AE8JqUSyzA1I2cInvonNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه سریزد  ، یزد
شاهکاری از معماری باستان
جایی که قرن ها پیش مردم اشیاء ارزشمند خود را در اتاقک‌های امن آن نگهداری می‌کردند
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66798" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh2nlEs4i5VJB0Gl0FDiuCBkjNPWUhy0d_vpbfSSyU0FMTHx__EOzF0FrhEFBf1JqYYwgKdPiwN0b_mhFvqgfdAdG-piMfv_KdNDIGyw3f3icXQ5bpE1PDTBpis0NUF8cknnt2gg40h_Y3NwJXd2YTw6xrDcB5UejGu6Aamn_TBbd2tId2dgsQKKWBO9LaxUGEFC1QvIOhE3W0BOuhQoXzZeK8HX4cJJ4k9j19pxsWiWSIQUh43l2onWXFTjchuUPS5PS2O6_baGFo6qPNOv4svZ28a6kreKiIml3gPvmZfw3zgC4IeyUYt1H-jRonDboR50J2UxsmxkxUZ2HBcTvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
دونالد ترامپ:
دو زلزله بزرگ که اخیراً ونزوئلا را لرزاندند، بسیار عظیم بودند و تعداد زیادی قربانی برجای گذاشتند. ایالات متحده آمریکا آماده ارائه کمک است!
16;من دستور داده‌ام که تمام دستگاه‌های دولتی ما برای اقدام سریع آماده باشند. ما برای حمایت از دوستان جدید و فوق‌العاده‌مان حاضر خواهیم بود. گزارش‌های اولیه امیدوارکننده نیستند!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66797" target="_blank">📅 09:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
از ناوشکن هسته‌ای کره شمالی رونمایی شد
🔴
رسانه‌های دولتی کره شمالی گزارش دادند کیم جونگ اون اعلام کرده است نیروی دریایی این کشور به سلاح هسته‌ای مجهز می‌شود و کشتی چوئه هیون رسماً وارد خدمت شده است.
🔴
این ناوشکن ۵۰۰۰ تنی به سلاح‌های ضد هوایی و ضد کشتی مجهز است و قابلیت حمل موشک‌های کروز و بالستیک با توان حمل کلاهک هسته‌ای را دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66796" target="_blank">📅 09:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66795">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66795" target="_blank">📅 03:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66794">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66794" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66793">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ru3J__s7yjkG3DGVTkxcBtWqEkzlQbffbBYtSMAO32N_NNgjxCvD5jGdRtR4yeka4NwNKFC74VfBkvQdXm1RxQU8GPqAeojtCP3C59wlYfx9xTMjPL4FKF9EAmT5eDPBjx_0en1Yvxi0L3gNkfM6HvEB5KPczt_ifdp6zVwymDx2eeaRkBEQoWFPg5cxSVHc1bZZAHnar6Gfh17WQaMe7VNbdnJVbwayoMPjIAEWTVYp2jpvh1t02-QrAZ5G8LhilB_WIvaSoyezYhOCUkvT5BRp1-i2bdIRVbweNLDOm5WllEQEn3AaJM4-2gdWVwoqp6Om8WTDPe9AbSK6NAzNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66793" target="_blank">📅 02:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66792">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=k7tmFnQ1-nq52Y-ZN-TyKypoKHqyJIYXLqUwhJTc7HDrbFltAvADw0dbdlVhP3ulbVhMYbkhvuLecIvk9LG_wGLZH0LKAK1kMrZt0tixWdxq1lTB0QU881q1B3WBcA8Lutn0xp9Hxi7MhEW1b0elqIpYT0oxkAgpzQFMtVrWzgfkmVvXmf8qBVBoTC-vaaFqnxEEfq704sqGeMS4MWi5VE_yreIWnFSRTrXagCsDdrn4u9n-gEssCcKQsYMZG66LwjFDL0RUEUEfJFJ4EAelhEAnfgrpOJRcZe6EoBeDsCmbd8W3mj0uCtPTt4NDu4EEPsBgRVwc5KEbaDbUO4K9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17bcbdae9.mp4?token=k7tmFnQ1-nq52Y-ZN-TyKypoKHqyJIYXLqUwhJTc7HDrbFltAvADw0dbdlVhP3ulbVhMYbkhvuLecIvk9LG_wGLZH0LKAK1kMrZt0tixWdxq1lTB0QU881q1B3WBcA8Lutn0xp9Hxi7MhEW1b0elqIpYT0oxkAgpzQFMtVrWzgfkmVvXmf8qBVBoTC-vaaFqnxEEfq704sqGeMS4MWi5VE_yreIWnFSRTrXagCsDdrn4u9n-gEssCcKQsYMZG66LwjFDL0RUEUEfJFJ4EAelhEAnfgrpOJRcZe6EoBeDsCmbd8W3mj0uCtPTt4NDu4EEPsBgRVwc5KEbaDbUO4K9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
درست در میانه یکی از مهم‌ترین مسائل، ناگهان خبر فوری منتشر می‌شود: “سنا رأی داده است که می‌خواهد ترامپ جنگ را متوقف کند.”
ایران این را می‌بیند و می‌گوید: این دیگر چیست
؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66792" target="_blank">📅 01:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66791">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=q06dvUA2zd4pn9P6-BgQN0fvOWj5o54KsaZJLlCYTR_AfFOFwqzzXdD1ey475VdrQu7ri01-MvogINZLGawNGOgXLIez5eZQeqV1uV7mIinGbTtUunLk6dRA6p1NpuZNEbSqzP0NWH2Rt1rbt1cFL7zWqaBw7eqUYGrIp31Tb2AogttQ4EF0-NUnimZSZky0SMcGOvd_lD4FAS6XMR9T_KU2PAEwXnmeLFlGQy996EFnIuwQBwO-m3KIxcy9tkHOeMRiL0mX5yLPVjvxhCXxRyUXg5FCUTUd9ZnsK3dJtC4eUyZm0-dcZjmH8te0wb39jHP304G3wlIjM1GRaqx_vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6928b1a5c.mp4?token=q06dvUA2zd4pn9P6-BgQN0fvOWj5o54KsaZJLlCYTR_AfFOFwqzzXdD1ey475VdrQu7ri01-MvogINZLGawNGOgXLIez5eZQeqV1uV7mIinGbTtUunLk6dRA6p1NpuZNEbSqzP0NWH2Rt1rbt1cFL7zWqaBw7eqUYGrIp31Tb2AogttQ4EF0-NUnimZSZky0SMcGOvd_lD4FAS6XMR9T_KU2PAEwXnmeLFlGQy996EFnIuwQBwO-m3KIxcy9tkHOeMRiL0mX5yLPVjvxhCXxRyUXg5FCUTUd9ZnsK3dJtC4eUyZm0-dcZjmH8te0wb39jHP304G3wlIjM1GRaqx_vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره حمله به مدرسه میناب:
«نمی‌دانم که آیا آن‌ها هرگز خواهند توانست این مسئله را حل کنند یا نه.
موشک‌ها از هر طرف در حال پرواز بودند.
کسی گفت که آن موشک متعلق به ما بوده است. شاید بوده باشد، اما من هیچ چیزی ندیده‌ام که مرا به این باور برساند که واقعاً موشک ما بوده است.
موشک‌های فراوان دیگری هم توسط افراد و طرف‌های دیگر شلیک شده بودند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66791" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66790">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66790" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66789">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=TGrmkBE_Lqfe0cHVVYHFuj5fLXxHRqw2XTw_eo6I8yTYHIyFQter2Nm1oKzCGXoSAL9olflEVarnUIMxKz0OMQF9k1jxU9TeqhbxCEVsrG8wtKBF0y-CBUpmrQf61nQOYTTJS2T5pH0_pZLcGsCG9v0r8PxGsQg_jAbghw94S9p5FjnYd3GrMBAMzq1eOkF_Olv7GeUSoDLjLQ60CZG3uitR3v_ensrB55WrZgWUcaEbTCiVtKfATK2ZNFv1eEqmT1FTEJiuVon0qjOqtZctD2IQ-YLfTyObtWVpeQ0Yi7LHEqmCgBuYrqQ_5kyOWMBQUyCs6oSwgioLUOKlFT_xtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fa6495873.mp4?token=TGrmkBE_Lqfe0cHVVYHFuj5fLXxHRqw2XTw_eo6I8yTYHIyFQter2Nm1oKzCGXoSAL9olflEVarnUIMxKz0OMQF9k1jxU9TeqhbxCEVsrG8wtKBF0y-CBUpmrQf61nQOYTTJS2T5pH0_pZLcGsCG9v0r8PxGsQg_jAbghw94S9p5FjnYd3GrMBAMzq1eOkF_Olv7GeUSoDLjLQ60CZG3uitR3v_ensrB55WrZgWUcaEbTCiVtKfATK2ZNFv1eEqmT1FTEJiuVon0qjOqtZctD2IQ-YLfTyObtWVpeQ0Yi7LHEqmCgBuYrqQ_5kyOWMBQUyCs6oSwgioLUOKlFT_xtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم نروژ فقط یک طرح ساده نیست
🇳🇴
...
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66789" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66788">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=SN26ZlM20HQq2q5pqpihchHg3WdRkNTS1Cm9gV7iuftFkTr_vrZGgeHCnd1ouiH07fNIZyo8EZQ0KnrydSopZeswQi4Jvr3stZLPyU3il3omwpa5wbS-hmU3nU72bWMCK64v6VwOlrj9Zwyr5OGr7hFEALxrFQYxEF9BEZhspvgoKidA-r51WnrtHYcq9pbuBOLqTJo3-60qs2XnOpvHbMdfXqusYyV6C7qc8d3LlE29vzs9Fm6PNOonbTIH0mga4OyHCS2brZ-oYYuftgugEnz7YgTsckSnvns7bQg-kg6yBWIFZCsy8vDY13PvoQVGYmq9zDVf9JEkAETnp1X223Fo8DVVYsG5g8xO1n1XNMf--2hmyLklQKMQJdqAwC8ch_WM4EwnIzosBdlS3v8YTOzlSe-PG534U6kJXjLqqfFSNKVPFIsNxKsGHkrcQSJsu97yvcYJON8p2RZiE3ndp7B92cfvX7CGlkHWMRhbHX21kXnC2N61kqhXNNi0omO937jWDfgCd84es3bj5WF8petw3QDcsOpGmuqKLlUmBKgMDJ90EJdDfNbPpWW42FxkPXnJLD17Km950I4FCWWGYuz_V5mHGeJVlPTbcdeR0A7pu6fU9-YNKncEBgX3Gz8tLZrsLyLw55pPznqSZi_E1p5MuT_VPBK4pBwWvCMM9EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6390fb697.mp4?token=SN26ZlM20HQq2q5pqpihchHg3WdRkNTS1Cm9gV7iuftFkTr_vrZGgeHCnd1ouiH07fNIZyo8EZQ0KnrydSopZeswQi4Jvr3stZLPyU3il3omwpa5wbS-hmU3nU72bWMCK64v6VwOlrj9Zwyr5OGr7hFEALxrFQYxEF9BEZhspvgoKidA-r51WnrtHYcq9pbuBOLqTJo3-60qs2XnOpvHbMdfXqusYyV6C7qc8d3LlE29vzs9Fm6PNOonbTIH0mga4OyHCS2brZ-oYYuftgugEnz7YgTsckSnvns7bQg-kg6yBWIFZCsy8vDY13PvoQVGYmq9zDVf9JEkAETnp1X223Fo8DVVYsG5g8xO1n1XNMf--2hmyLklQKMQJdqAwC8ch_WM4EwnIzosBdlS3v8YTOzlSe-PG534U6kJXjLqqfFSNKVPFIsNxKsGHkrcQSJsu97yvcYJON8p2RZiE3ndp7B92cfvX7CGlkHWMRhbHX21kXnC2N61kqhXNNi0omO937jWDfgCd84es3bj5WF8petw3QDcsOpGmuqKLlUmBKgMDJ90EJdDfNbPpWW42FxkPXnJLD17Km950I4FCWWGYuz_V5mHGeJVlPTbcdeR0A7pu6fU9-YNKncEBgX3Gz8tLZrsLyLw55pPznqSZi_E1p5MuT_VPBK4pBwWvCMM9EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی که یه عده از طرفداران حکومت با هوش مصنوعی از «مختارنامه» جدید درست کردن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66788" target="_blank">📅 23:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66787">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlRtBCHtUqeSEXT6Ntl5svNtVmd-6cUVoxDGt7bnAUGYANYDzYfac3hO4BLmNEdceEB9_ZHOmPq_K1NQVP8rDzf6eN0l3K6IqjxU10m0prfrBVXHlrBP8pzvsOSBAQG_yvaN15aT4QADQzrSPU1-81KRt_SwbPl5Nr0U453LXnezy8jM-CIcKy5_iHWG8ue1RmXVS2ZgnnJ56a9zuj75JBz4wtAnMVq3l4ZxRs93pfUh9HcZTPKzx3rDo7bmnhVPlMT4tQZU7VXVwHbgUa6RwroVG1TCQxLrkfYZT6l0ehRlOVsguhgL2DCJnmLsozk-dIDJ7-D4EjDoEKP_IIK8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی وزارت امور خارجه:
اظهارات متناقض آمریکا درباره یادداشت تفاهم برای پایان جنگ به کاهش بی‌اعتمادی ایرانیان کمک نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66787" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66786">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66786" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66785">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BYHMob6285KmAALkmOgPY7bx2V6TUV34JbOX7M9RmgX-r9uQ1TbUiG-KXBGkC_NPgolS3TYVLTw_Oz1pc8vge6WSR-I1Lvmvs6gUqelIDGNaaeUn8mnK7-jJWaaXQgOvpF_c_GfrP1W1TIR_5wHZF8RuLbTCUgHC-egVce940EIJj66pCDwrSgZPjkKgji5S35EsQFFHyF1mSxylpYGGuh2xd2vMEyxUP28wvD5OS0ITQBkRE2hluUCVqjbcOuxyhiYA4NI9FTn45RUZb6aDZGaCISJJErEEKp0Zus_u9LJcB2_nxad32AqdU03aPAxn5zshVT7EP6HT0k9aQbInAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66785" target="_blank">📅 23:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f56950043.mp4?token=t_kKz6eyhYUu465iQJRnxH1jW5gVUPqDls8-SRyQfXId8Qtjl0hUupFlDH6b-RqYWJ0_hoYhLGz88X4EAyKcBuArJTJDBeI3WZMORnSmkBRBiqXNtjJeDfblCiHN-tU5FrabhMuuN5GJJL7NmIYOlzFi7d3vaQzAqys6iQc-nk3moOatMxxODBFNjsm4flvc90PUh0afYkDwMw-LdmtmTAH0eIs2XMxNvWtIwoMyRhUVyeosrkFspwTfNrqteG4a0TXXLLt936SNAmK0GAFTvIaReSY00PLmaYzfyuw3-3dUNky9fGp0zOQhA78C2Z4dpMWrWQHrq85nG0LXURISXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f56950043.mp4?token=t_kKz6eyhYUu465iQJRnxH1jW5gVUPqDls8-SRyQfXId8Qtjl0hUupFlDH6b-RqYWJ0_hoYhLGz88X4EAyKcBuArJTJDBeI3WZMORnSmkBRBiqXNtjJeDfblCiHN-tU5FrabhMuuN5GJJL7NmIYOlzFi7d3vaQzAqys6iQc-nk3moOatMxxODBFNjsm4flvc90PUh0afYkDwMw-LdmtmTAH0eIs2XMxNvWtIwoMyRhUVyeosrkFspwTfNrqteG4a0TXXLLt936SNAmK0GAFTvIaReSY00PLmaYzfyuw3-3dUNky9fGp0zOQhA78C2Z4dpMWrWQHrq85nG0LXURISXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ازای شهادت مقام معظم رهبری چی از آمریکا گرفتید؟
قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66783" target="_blank">📅 23:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66782">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f387d3e0.mp4?token=bIyOd7cMkK7fBGmMCmRS7k7XZYyzSP80BchZAyy79CRdLSJmm3a8mASo_PYLr5WP42uEIZ2TUzO3y5EmWU2oRnYGRb-2ynd_n_bNlXjpRCENOsBVNN5uVoGQMdWVeY6AXcdpfM5kMJa_mJ7lexdumlJwuymWiWXGLM2rThnkU_ZwOcAZrUdA6atYtsDW7BwL0XaWzRm9eOlmhQuACLIrgO522_7PxsqHdYoGpsjWtch8ojJGKJe0QiLiRb5KoFFHfkLzrSRZBSPkhMGnmDKTtyKFR2g135qU-tfit-K2M6ls4XDj4DEE2t2tP1Ej_qgbK9r7kUEW0qDr5Ifd37p8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ایران خیلی خوب رفتار می‌کند. آنها با هر چیزی که من می‌خواهم موافقت می‌کنند و باید هم موافقت کنند.
در غیر این صورت، ما فقط برمی‌گردیم و کاری را که باید انجام دهیم، انجام می‌دهیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66782" target="_blank">📅 22:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98a05f2cc6.mp4?token=map3hdh9bFow40Dk60ix75C8bUe-OdJ9XXiJssKbN1l-zSsjX5V6QfsCz5SCDA0Cx_CbYiNYLpJpQy0pEC-_7VAtOirT05ZBGwkP0sHdVhV-FCXEdSIWkCYUC681rzQPXR6nvkFNEF4jVCJHE-xCZlaThJ-CkkttqKNf9F8AAxXbHeqxw9ch9_qV9pZD5VPI8ATU8efPs_4KKMWXiduoEmWzPzQ5bh5LqhYfNqack-sU4q9U-3SrX7-8CQUkmFKJojrJrmB_zqA6Z122uHLkyXs_KnvseMBLJYInVXs3BsHzK2KEgpjzpol1cY12XQK1kqWZ4jTLuPwosxJx2glcnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«جنگ خیلی خوب پیش می‌رود. همانطور که
می‌دانید، ما با اختلاف زیادی در حال پیروزی هستیم. ایران امتیازات بسیار بزرگی می‌دهد. خواهیم دید چه اتفاقی می‌افتد، اما بسیار، بسیار، بسیار قدرتمند بوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66781" target="_blank">📅 22:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66780">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=JvWAQpH646OZWye1t1RlsV0KzzApE8o3mkYx7SqzyzOvOdNnu8-4zRQ9MoGJZ7NTxzM5toNJ1nWCw0SX5aWGtmGBBtWRw9I7wWNa5aGwEfAmXJwYfsUJoqSgXUeWtFxlRtomjVN5DwDTCdBqSO9J-nDYH2hmO4RQOO0Twex5SWO3WAvcfpbsD_9Vr4L8oJs6X0X80qy5068KPBJeNq6xiu6YR8DJUz2idPwKKlKWpL6Vf_QOlPzdDVw_s5VI1LjOLDjdcRWUNWWDusxaMvS4odG_3qZis74rmaDOVyCdxXOsExwK6CZ-TCJxJA1sE9hyNlDviB_Wu6lc_YgSxyBqDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a25b4d46.mp4?token=JvWAQpH646OZWye1t1RlsV0KzzApE8o3mkYx7SqzyzOvOdNnu8-4zRQ9MoGJZ7NTxzM5toNJ1nWCw0SX5aWGtmGBBtWRw9I7wWNa5aGwEfAmXJwYfsUJoqSgXUeWtFxlRtomjVN5DwDTCdBqSO9J-nDYH2hmO4RQOO0Twex5SWO3WAvcfpbsD_9Vr4L8oJs6X0X80qy5068KPBJeNq6xiu6YR8DJUz2idPwKKlKWpL6Vf_QOlPzdDVw_s5VI1LjOLDjdcRWUNWWDusxaMvS4odG_3qZis74rmaDOVyCdxXOsExwK6CZ-TCJxJA1sE9hyNlDviB_Wu6lc_YgSxyBqDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالناصر همتی:
اگه کیفیت ذرت و گندم آمریکا خوب باشه ازشون میخریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66780" target="_blank">📅 22:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66779">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN7uGYsz7IOQwrIVXwYKFUecHm5DEIYuKVBoexPqm6IZNeYHGRqGNodx25MgAw4xIJEBhLzbQTVB_IS-BE_ZTXnK94ATFIzVDzI2YUilaveRZy33ifUDNcyLgsLS23c591pgZNAAsypSEzS4J3FGDLsh-GSdng9NzGUIxFcJPajNmShk4mFO1FLs-68H9fFFNeIxmoWhiskl1oqdLQvWWB-cN3F1aAg87Vdjl46OtW4Iq97at6HiSwLhsSxYmWLHhzLaIuKpSnmFdHaR7EcHflI9pJCsQFG4XwSDqaxxufIZlguDnM8tm9OT-6grZf5nIjoJ7R7B95f1q1rgAQs1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل به مارکو روبیو:
رژیم جمهوری اسلامی و حامیانش در عمان در تنگه هرمز هزینه دریافت میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66779" target="_blank">📅 20:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=eH--fW3KF-h05KtpkHhhTEXjDwM49s3EZpokFrqMOKiP2MS_h4UHDFt4zwWbu-VZDW0mwydG9gPLjjo48KOg1Pt8rNHIF4cglRx_WKn7u_BrgXjjx3DdhlQ-BNRSER_JcjDJxfWCeFsvWHiafOBgiAB06r6M_6hdYZKCNXMXMR_KrcdRTvcEBSU-o3IZsvvGMBcLEIJ33GxNJJJJ6W4ee6cPpasyfZk9OQIOV_qXNZmVmJhG8KUNGkuCGPqipqYAn8fBKrSj0gLrTeKeYVb4OYG3UgFj0mUVIs5c-wz-WUl4cD_Lv11iblYyn4IYGAVE1Z0Yxm8biW7tlNFLDPbhKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd80a69999.mp4?token=eH--fW3KF-h05KtpkHhhTEXjDwM49s3EZpokFrqMOKiP2MS_h4UHDFt4zwWbu-VZDW0mwydG9gPLjjo48KOg1Pt8rNHIF4cglRx_WKn7u_BrgXjjx3DdhlQ-BNRSER_JcjDJxfWCeFsvWHiafOBgiAB06r6M_6hdYZKCNXMXMR_KrcdRTvcEBSU-o3IZsvvGMBcLEIJ33GxNJJJJ6W4ee6cPpasyfZk9OQIOV_qXNZmVmJhG8KUNGkuCGPqipqYAn8fBKrSj0gLrTeKeYVb4OYG3UgFj0mUVIs5c-wz-WUl4cD_Lv11iblYyn4IYGAVE1Z0Yxm8biW7tlNFLDPbhKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو:
توافقات اخیر با رژیم جمهوری اسلامی بخشی از یک روند مذاکره‌ای و یک اقدام موقت ۶۰ روزه است.واشینگتن انتظار دارد تهران به تعهداتی که در سوئیس پذیرفته پایبند بماند و در غیر این صورت، پرزیدنت ترامپ ابزارها و گزینه‌های مختلفی از جمله بازگرداندن تحریم‌ها را در اختیار خواهد داشت.این تعهدات به صورت روشن و صریح مطرح شده‌اند و ادامه مسیر مذاکرات به میزان پایبندی رژیم جمهوری اسلامی به آن‌ها بستگی دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66778" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66777">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=bB8FI2ztIN6VCJ6BA6tyT2vwKCEkj7F2DECxUsyi_QbaGCNYe5Hf0-8_odcogiw27oOp4vxF3-Tvd31HzZO5YRahD32vlCn_bgNLfBtLbLpzcLvd6N6s167JPw87Ay5jvRk2967QnZE7HG14xa8Tc_Oced5q_BTQ51CeVJYJ4HpC6BXH1iwc07M4xY__lKDdmgT9y2KVpJo0KnXW8piVT46ZYgYsdOcD-J0hSW1KyLINI2cnExOmNsnlsolndQDo7cajFy5In8ofDqJbTRG59gv-eprIgNy9irSXdPJ1FYg92VE1oyTQlbw9Kk2famIfcOHLPN-768higdZHFL99dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ffe99615e.mp4?token=bB8FI2ztIN6VCJ6BA6tyT2vwKCEkj7F2DECxUsyi_QbaGCNYe5Hf0-8_odcogiw27oOp4vxF3-Tvd31HzZO5YRahD32vlCn_bgNLfBtLbLpzcLvd6N6s167JPw87Ay5jvRk2967QnZE7HG14xa8Tc_Oced5q_BTQ51CeVJYJ4HpC6BXH1iwc07M4xY__lKDdmgT9y2KVpJo0KnXW8piVT46ZYgYsdOcD-J0hSW1KyLINI2cnExOmNsnlsolndQDo7cajFy5In8ofDqJbTRG59gv-eprIgNy9irSXdPJ1FYg92VE1oyTQlbw9Kk2famIfcOHLPN-768higdZHFL99dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: برخی از عناصر اطلاعاتی ایالات متحده ارزیابی کرده‌اند که اسرائیل علاقه‌مند به تضعیف تفاهم‌نامه فعلی است.
🔴
روبیو: نمی‌دانم در مورد چه اطلاعاتی صحبت می‌کنید. نمی‌دانم این اطلاعات را از کجا می‌آورید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66777" target="_blank">📅 20:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66776">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=ZBJWKmzAgdItxTjytAxqpicmD4FYcwYacexliQvtDNZwkUf5S5xNeTzDw4gxHz5aeer5TFXGxqBYJlJUEPrssPreMDWozh6qod1k99GAylISGcNUNTLOoE7CGXv1oZhF_euh90mbIeR_D2FnBNL_DnE6M5HDK2ojVPlaA12zV6lcgx5cJcTo-uUYEwTkTzf1GRRglDb8CUja2wYiw8UvtHdh2UUumyNbuyE6_-h3Pd37UpBoAmzNFJR-Pp0G76MXgHtvo41sXnK786eD4IQ4BTAw6ROacXqbHmM3hlnHWr-W6tEJde_QXJIbfhde2NH_86yAdiLdMnqgMsew1MzR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8948b47d.mp4?token=ZBJWKmzAgdItxTjytAxqpicmD4FYcwYacexliQvtDNZwkUf5S5xNeTzDw4gxHz5aeer5TFXGxqBYJlJUEPrssPreMDWozh6qod1k99GAylISGcNUNTLOoE7CGXv1oZhF_euh90mbIeR_D2FnBNL_DnE6M5HDK2ojVPlaA12zV6lcgx5cJcTo-uUYEwTkTzf1GRRglDb8CUja2wYiw8UvtHdh2UUumyNbuyE6_-h3Pd37UpBoAmzNFJR-Pp0G76MXgHtvo41sXnK786eD4IQ4BTAw6ROacXqbHmM3hlnHWr-W6tEJde_QXJIbfhde2NH_86yAdiLdMnqgMsew1MzR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
مارکو روبیو درباره ایران:
وقتی می‌گوییم تنگه‌ها را باز کنید، منظورمان این است که تنگه‌ها را آزاد باز کنید. آنها آبراه‌های بین‌المللی هستند.
هیچ کشوری روی کره زمین از گرفتن عوارض در تنگه‌ها حمایت نمی‌کند. این اتفاق نخواهد افتاد. ترامپ این را به روشنی بیان کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66776" target="_blank">📅 20:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66775">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=bsXQsgDqUk4ALXGOGdvW-3gthCHIe8M3QYimmYoAaNggBjFe2FvgaxU9rzWVBx_4qeHqjKpOcwHG4io_DPlPzzmVw-rbIRnSQ5fZyusJFd7Hd8g6pt31LJfnK7EoL4igBY6FgWRAvZk5eksYvR52ox_cnv1MpeTNmVDJq_e2MdFereOsaqYbsyyCH60zX1_zk4YLUMlbmflxuUZU8revg8IKmpT6tLF7uBporn0zHE5kXhlorhgX4EBxCu2nzUt3RgyT6ToeqmpOPljJStbeNZ_TwFTNHhVLkXWYl3xrR9RD8WMdZ_xTHLNFds53_UI0jw9rlthByM1Svsv-yD48-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bf8d5d6b.mp4?token=bsXQsgDqUk4ALXGOGdvW-3gthCHIe8M3QYimmYoAaNggBjFe2FvgaxU9rzWVBx_4qeHqjKpOcwHG4io_DPlPzzmVw-rbIRnSQ5fZyusJFd7Hd8g6pt31LJfnK7EoL4igBY6FgWRAvZk5eksYvR52ox_cnv1MpeTNmVDJq_e2MdFereOsaqYbsyyCH60zX1_zk4YLUMlbmflxuUZU8revg8IKmpT6tLF7uBporn0zHE5kXhlorhgX4EBxCu2nzUt3RgyT6ToeqmpOPljJStbeNZ_TwFTNHhVLkXWYl3xrR9RD8WMdZ_xTHLNFds53_UI0jw9rlthByM1Svsv-yD48-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
به من گفتند: «وارد رفح نشو.»
می‌دانید چرا این را گفتند؟
چون رئیس‌جمهور ایالات متحده گفته بود ارسال سلاح را متوقف خواهد کرد.
من گفتم: «احترام زیادی برای او قائلم. او در آغاز جنگ کنار ما ایستاد. اما ما چاره‌ای نداریم. وارد رفح خواهیم شد. و اگر لازم باشد، حتی با ناخن‌هایمان هم خواهیم جنگید.»
گاهی باید بدانی چگونه حتی به رئیس‌جمهور ایالات متحده هم «نه» بگویی.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66775" target="_blank">📅 19:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66774">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=FczyP_Xjbn_RBDGxNJlRtcWR2pbPVtI9oPEUcQT7bQ3znz0CIE-c8FwGJcIneNXVBXXOXtcs_smrHB-hPPNxBl-4BYqYKzyKLkGq2kYCXwI5tYVkavQDkmyUFkezFGnzX7JR942Du1LAKrMAXtmm8BmGr3LGZOgnX5FbW_bwKWyRvqIadMHSg4XaLTo5rndhoJhE43_I3-eCGDj0w_bN23w2BrMgSCcNGOCM6pDcQphQpy-x3HdmioVhE_KJZDK6OVhN9x0VbOL86XpWyM2JH-5sW1lHhZhqrVE9AJk_qsZpaaRMacbBEyykV0WwgcTSnCWTWbAwKzfHlBSmQLFiKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7873635e.mp4?token=FczyP_Xjbn_RBDGxNJlRtcWR2pbPVtI9oPEUcQT7bQ3znz0CIE-c8FwGJcIneNXVBXXOXtcs_smrHB-hPPNxBl-4BYqYKzyKLkGq2kYCXwI5tYVkavQDkmyUFkezFGnzX7JR942Du1LAKrMAXtmm8BmGr3LGZOgnX5FbW_bwKWyRvqIadMHSg4XaLTo5rndhoJhE43_I3-eCGDj0w_bN23w2BrMgSCcNGOCM6pDcQphQpy-x3HdmioVhE_KJZDK6OVhN9x0VbOL86XpWyM2JH-5sW1lHhZhqrVE9AJk_qsZpaaRMacbBEyykV0WwgcTSnCWTWbAwKzfHlBSmQLFiKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست وزیر نتانیاهو:
در عملیات غرش شیران بود که من به ترامپ حمله در ایران را اطلاع دادم و هیچ اجازه  گرفتنی در کار نبود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66774" target="_blank">📅 18:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66773">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=XyZFHrFOdLdTjUPfueZxWs2lTiImlWBgyP9rZmj_xrdhtLn6xiAvwV8HjtO8m9kdDOJAXkhcKyJcB5VMIK2SphQjI1s1NdXmzlMFzxFFoXXgd7REtSRZLdD42eSZXElCD6LSogcNVtd7FKIup2EXLFMF7dsFebKB8UfPujKkTpE3qCK6-wp6BRuK7o_DGE9nDuZ1D5RsAUzO6TXbl-C0DxUTrTXgPVNZe8yEQ61AoNmhwVO8HQLPPXKExiCJhyhlSHmqAWrxHEMMtVJUub_8hJgHfiG7S07BytoW6suVjjuI81S9RXMXWsNXlyUTVgje-WlbtXJFxInkVMcuSZYVPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1071e13e2a.mp4?token=XyZFHrFOdLdTjUPfueZxWs2lTiImlWBgyP9rZmj_xrdhtLn6xiAvwV8HjtO8m9kdDOJAXkhcKyJcB5VMIK2SphQjI1s1NdXmzlMFzxFFoXXgd7REtSRZLdD42eSZXElCD6LSogcNVtd7FKIup2EXLFMF7dsFebKB8UfPujKkTpE3qCK6-wp6BRuK7o_DGE9nDuZ1D5RsAUzO6TXbl-C0DxUTrTXgPVNZe8yEQ61AoNmhwVO8HQLPPXKExiCJhyhlSHmqAWrxHEMMtVJUub_8hJgHfiG7S07BytoW6suVjjuI81S9RXMXWsNXlyUTVgje-WlbtXJFxInkVMcuSZYVPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارکو روبیو در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66773" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66772">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66772" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66772" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66771">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=LC9ca2QshFgL4HQ8cfeXLt-CGRvN4zT52dKEAkp29d8oIBl_9Cy2oTl61mc3fWvPg1iefC9vczyaSrGBU0BQqlWciAnszIFPoSHhs9AEIA3KUNFSMi9DARlL2CHcJj5-cd3PKO-ikjDZ47N1ZFgRdQjZimZfCazLIr4hjwiA5G2a-iFO_GHOTA3KUBS_rVCJO7WZpW3aaGlpZTtbuxUJ68W71EjV79-J-lPi9vvS0IR6Z0Yb8vuLtoWesXMAIqka0rleSzfZhT1GPu5snqKls5lUzotIYLWrG9-_c3GefAR1GtTmfwlxqVLEDzjLPsq0rJD0VDda_HkKcexI6AlN6nSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=LC9ca2QshFgL4HQ8cfeXLt-CGRvN4zT52dKEAkp29d8oIBl_9Cy2oTl61mc3fWvPg1iefC9vczyaSrGBU0BQqlWciAnszIFPoSHhs9AEIA3KUNFSMi9DARlL2CHcJj5-cd3PKO-ikjDZ47N1ZFgRdQjZimZfCazLIr4hjwiA5G2a-iFO_GHOTA3KUBS_rVCJO7WZpW3aaGlpZTtbuxUJ68W71EjV79-J-lPi9vvS0IR6Z0Yb8vuLtoWesXMAIqka0rleSzfZhT1GPu5snqKls5lUzotIYLWrG9-_c3GefAR1GtTmfwlxqVLEDzjLPsq0rJD0VDda_HkKcexI6AlN6nSQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66771" target="_blank">📅 18:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66770">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjSbs0Aoe4vPRcdOW8hh24o5y1zpelOogCWCEriuikf3E0VKTH2DUCcdchQ8pqN8CGVp4kRLpmuqTseE71sa6HG7FLbzF9sWh9lBJGIVAGRGPDK3g5i_GdgnAKTX0_FVOTZoT2vRy7BtCk4sG4Su-BMizsMoDLpIRdCsvdZW1pOvmtxsTJPcr9kef7Ol8D5g1bZfcZo12Are73g7IfXMCLdl--aoFXYiPUtA2LK5WsH-T31KVZ8aumwi9IeA90iXRu3SaHTlUas_1jX6ERAjEcAz13tSDpFY-iIJJnTafXgvFPuaLevvEsqk0TJ3v-hL-tcPMvxJAdyoTBp8dHKmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
ایران به آمریکا اطلاع داده که، برخلاف گزارش‌های دردسرساز رسانه‌های فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای و هیچ نوع هزینه دیگری از هیچ کشتی‌ای که از تنگه هرمز عبور می‌کند، توسط ایران درخواست یا دریافت نمی‌شود. اگر این خبر نادرست باشد، مذاکرات فوراً پایان پیدا می‌کند!
همچنین، آمریکا هیچ پولی به ایران نداده و هیچ بخشی از پول‌های ایران را هم آزاد نکرده است. ما بخشی از پول‌های ایران را که کاملاً تحت کنترل خودمان است، برای حمایت از کشاورزان و دامداران آمریکایی آزاد خواهیم کرد تا با آن ذرت، گندم، سویا و محصولات دیگر خریداری شود. ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد را منحصراً از آمریکا برای آن‌ها خریداری خواهیم کرد.
از توجه شما به این موضوع متشکرم!
— دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66770" target="_blank">📅 17:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66769">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=FdiWPQaKCaUJXIYTDPlzxF6sIVXXEPhxH1AJe9SbPz_yc2cMV4Ti6ggOCyQIfCMovZMKWrf2p_-GhfBl2yp6mw-5kK_1BZMPHxrymlb-Sjd-loDAxbIghAIz6qQeYS2YW-8vUztUhb16yjSIIwRRwE4G_cW2rdEH2-pasFJ-zxkHtGVxiPN6o66vRE6mx10KFignVDSX6UWb2HFa42E6AqXoeaaa4MvQdpx6w0goNGfmXGHnOJduQR-O8AyXUahOgrTLSjSaqKRWrH8_87G02gbkX0TOCVSS9o3sLvRs_gnA04P-2BTzDOVX7dlO29aBta7B8F1ukgxQBwbayi2-Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc755f3dc.mp4?token=FdiWPQaKCaUJXIYTDPlzxF6sIVXXEPhxH1AJe9SbPz_yc2cMV4Ti6ggOCyQIfCMovZMKWrf2p_-GhfBl2yp6mw-5kK_1BZMPHxrymlb-Sjd-loDAxbIghAIz6qQeYS2YW-8vUztUhb16yjSIIwRRwE4G_cW2rdEH2-pasFJ-zxkHtGVxiPN6o66vRE6mx10KFignVDSX6UWb2HFa42E6AqXoeaaa4MvQdpx6w0goNGfmXGHnOJduQR-O8AyXUahOgrTLSjSaqKRWrH8_87G02gbkX0TOCVSS9o3sLvRs_gnA04P-2BTzDOVX7dlO29aBta7B8F1ukgxQBwbayi2-Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگه
فکر می‌کنید قراره چیزی کسشر تر از این امروز ببینید عرض کنم که سخت در اشتباهید. فقط کافیه موزیک ویدئو شاهکار صداوسیما برای تیم امیر قلعه‌نویی رو ببینید تا بفهمید با کیا شدم ۹۰ میلیون
😐
😐
😐
😐
علی بیرو تو دروازه یا نیازمند ، کنارش شجاع و کنعانی میشن پدافند
تنگه هرمز ما تو دستای سعیده
شوت‌های قدوس و رامین مثل خیبرشکن، مستقیم به قلب دروازه‌ی دشمن میرن
ترابی دریبل‌زنه، نعمتی هم حامیشه، مثل هایپرسونیک از لای دفاع رد میشه
یه طرف میلاد و ازون طرف جهانبخش، پهباد شاهد رو روی دروازه میکنن پخش
حاج صفی ، حردانی و یوسفی مثل شیرن
توپ‌های علی علیپور از پاتریوت هم در میرن...
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66769" target="_blank">📅 17:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66768">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=ty3qDOEcllSSIQgH4ozZQCBhq_ewSoDWT4jd2ovcQ3HHzMF4Tj4FStdm2qEJu93lbeTNvNHxid6cnu3QHF7Ugt2KroT4xGhY0o-JveLVQFts_z9953UwwkFz_rHB91Fa-4Ql54AqPJrCSOYWIa8HTV2T9VpSI7dyFMAZwZNtnaHaqx7uTz_ZBiy84y1opl-7_rHALZc0wzSvb8kQweldBtL8VwYw9LanatbdDyiu-w3k5kCq05dkXhSh7Nf7MHLSd3xebu857k1XW2rFr2Q6MeMP7uNSIN2bd3PQ3aNtYMDd_XR1jBBWrzB0ZXOpLYRiCW2jdSGxn6y2v_bxddRycJXWb8Nr5OjCoHSGO-zfs2oAIRTPsQjTDYBIlB56oE1C-eUIPN9lRI_X5XDjQrCnw6MZxkzhXJeQ2FZ6EFrxpr16IIt7EsVMo0ZH38Q2bwYP8_eVStZcYqkPDKZtmjUt3UbqYtp7Ayw_ba_AD9UitvarOpfJeJmM9J3kncwL6_BLK-l6u2sa3Z1AEHeT4orf7-8_Fojklj2Uc5ToEKgwN_kFCQFNX5vkXk-KLkkHmgj8hG4_IGt0Sr-beRGY0Futvx6bJtn2AqoVdrR8nYppGKVu-igU6mSDyfaoRxSUxHlt5R_TbDpMb3sdMVmAbJYtoscIYqPJkYy3VpWD9CMTG5c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f90bbfd79.mp4?token=ty3qDOEcllSSIQgH4ozZQCBhq_ewSoDWT4jd2ovcQ3HHzMF4Tj4FStdm2qEJu93lbeTNvNHxid6cnu3QHF7Ugt2KroT4xGhY0o-JveLVQFts_z9953UwwkFz_rHB91Fa-4Ql54AqPJrCSOYWIa8HTV2T9VpSI7dyFMAZwZNtnaHaqx7uTz_ZBiy84y1opl-7_rHALZc0wzSvb8kQweldBtL8VwYw9LanatbdDyiu-w3k5kCq05dkXhSh7Nf7MHLSd3xebu857k1XW2rFr2Q6MeMP7uNSIN2bd3PQ3aNtYMDd_XR1jBBWrzB0ZXOpLYRiCW2jdSGxn6y2v_bxddRycJXWb8Nr5OjCoHSGO-zfs2oAIRTPsQjTDYBIlB56oE1C-eUIPN9lRI_X5XDjQrCnw6MZxkzhXJeQ2FZ6EFrxpr16IIt7EsVMo0ZH38Q2bwYP8_eVStZcYqkPDKZtmjUt3UbqYtp7Ayw_ba_AD9UitvarOpfJeJmM9J3kncwL6_BLK-l6u2sa3Z1AEHeT4orf7-8_Fojklj2Uc5ToEKgwN_kFCQFNX5vkXk-KLkkHmgj8hG4_IGt0Sr-beRGY0Futvx6bJtn2AqoVdrR8nYppGKVu-igU6mSDyfaoRxSUxHlt5R_TbDpMb3sdMVmAbJYtoscIYqPJkYy3VpWD9CMTG5c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
⚠️
پشمام اینو داشته باشید. تو عراق از معاون وزیر نفت سابق این کشور حدود ۸۵ میلیون دلار اسکناس نقد از زیر زمین کشف کردن که دفن شده بوده!! فساد سیستماتیک تو کشورهای اسلامی ماشالا خوب رونق داره
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66768" target="_blank">📅 17:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66765">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c68737622.mp4?token=H7zWbdhI7gh3nUCxVXz3PZXLKPeWZG5GbH3tXSCk_-YpFyxiH2GM70lkkuGkFTvYtiD3jBxjJX7-4z93vgFgoF6ktfTV5q5DSH-8S2HDLQV0yCFSFblFsZ3Z-rYKlhRgqnWdFESfowwO1vMoN-bW-nzpUBjROBhCsU0AsRppRiOIfWwL2A-PTRYqYMCdOnvJP70wiqaQ_e-0SD5H-WFroxjbrGil0htlTmKMH3q2HIkc81YEZuV2Ny27JsYhOH4WeCFoHxWIyZx-KYZsg5X6LgW7VQokuAc7nZsO7vdj-hbe6Pley9Pix07pO8wymu5ncDnjWDuKDGaeX_rn9QxDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c68737622.mp4?token=H7zWbdhI7gh3nUCxVXz3PZXLKPeWZG5GbH3tXSCk_-YpFyxiH2GM70lkkuGkFTvYtiD3jBxjJX7-4z93vgFgoF6ktfTV5q5DSH-8S2HDLQV0yCFSFblFsZ3Z-rYKlhRgqnWdFESfowwO1vMoN-bW-nzpUBjROBhCsU0AsRppRiOIfWwL2A-PTRYqYMCdOnvJP70wiqaQ_e-0SD5H-WFroxjbrGil0htlTmKMH3q2HIkc81YEZuV2Ny27JsYhOH4WeCFoHxWIyZx-KYZsg5X6LgW7VQokuAc7nZsO7vdj-hbe6Pley9Pix07pO8wymu5ncDnjWDuKDGaeX_rn9QxDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
ویدیوهایی که خیلی از دیروز  وایرال شده از کربلا؛
دیروز کاروان شیعه اسماعیلیه که تا امام ششم امام صادق رو قبول دارن، واسه زیارت به کربلا رفته بودن.
از اون طرف کاروان ایرانی ها هرجا اینارو میدیدن واکنش نشون میدادن..
تو یسری جاها هم نزدیک بود دعوا فیزیکی بشه که پلیسِ عراق اجازه نداد...
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66765" target="_blank">📅 16:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66764">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=L7tEoaoTZB5bkYJRd7mcy6YKEOIJZEU8Umsduk0Nqqgm6IX7o3lknjgcRra4Yj25LgCXatzVVv0zBphsUGs1oIjOJg2rmSGDqJ-OX5Q5wR5cLZaU_FKva9PtLciLLWAbVrzKTs87iYNeo4Ij_HXh9CPdbDsSGh-O5-8YGkRCzRJwjGsksGNsvIZ9WGBmhdkVpMJw2hMwQ6iur0rpNVVaz_hypf3ocSfqSf9_1Y5tfsiRrlY3fVqJgLk6ZLlHTrcwfVjk503-9Fp38V7hgcIIeAwVhj-HEh7PrHQt2tSdZgEHKiz27STWEC2Qq3jA8fzrB4852rbsyseDY8SNa6Zkjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbff1343a7.mp4?token=L7tEoaoTZB5bkYJRd7mcy6YKEOIJZEU8Umsduk0Nqqgm6IX7o3lknjgcRra4Yj25LgCXatzVVv0zBphsUGs1oIjOJg2rmSGDqJ-OX5Q5wR5cLZaU_FKva9PtLciLLWAbVrzKTs87iYNeo4Ij_HXh9CPdbDsSGh-O5-8YGkRCzRJwjGsksGNsvIZ9WGBmhdkVpMJw2hMwQ6iur0rpNVVaz_hypf3ocSfqSf9_1Y5tfsiRrlY3fVqJgLk6ZLlHTrcwfVjk503-9Fp38V7hgcIIeAwVhj-HEh7PrHQt2tSdZgEHKiz27STWEC2Qq3jA8fzrB4852rbsyseDY8SNa6Zkjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مترجم: «ما هرگز در مورد توانایی‌ها و تجهیزات هسته‌ای خودمون توافق نمی‌کنیم.»
پزشکیان: نه!! موشکی! موشکی را گفتم…!
مترجم: ببخشید موشکی.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66764" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66763">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=BmYch_ELvKvIgixUT6DeMEiTcqp6yPPUcFcIby_xtTrglx0BDRm8ppFWX6ASbl1Z2sbGvSxoAe66e_eUAnQBCHVmeJxylt1gqVmnatG4ZXRmrLhoX9g-V1BVwMA1cPVlTMiGaqu20aSqGc1FNTuCbAg9dazXHBMxZ9rNgbQVOuXCxWs7uFwQWvVyKeFT-HQ7uGMvLIMwD6mm_wB23b4mum4LbtlXO9rpo2w1Yj3G4AapPJgia0y4jwsdKACpJjbSt3k4pzDU2N9MlZHSCMAq9lVGYtFmQFS_YYNnvU6EdeNRaazWinVqDogL75XC2_s-0kr5bAyvDQbZ8pOgYP_9MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/d59ef82aac.mp4?token=BmYch_ELvKvIgixUT6DeMEiTcqp6yPPUcFcIby_xtTrglx0BDRm8ppFWX6ASbl1Z2sbGvSxoAe66e_eUAnQBCHVmeJxylt1gqVmnatG4ZXRmrLhoX9g-V1BVwMA1cPVlTMiGaqu20aSqGc1FNTuCbAg9dazXHBMxZ9rNgbQVOuXCxWs7uFwQWvVyKeFT-HQ7uGMvLIMwD6mm_wB23b4mum4LbtlXO9rpo2w1Yj3G4AapPJgia0y4jwsdKACpJjbSt3k4pzDU2N9MlZHSCMAq9lVGYtFmQFS_YYNnvU6EdeNRaazWinVqDogL75XC2_s-0kr5bAyvDQbZ8pOgYP_9MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مراد ویسی: با توجه به تضمین آمریکا، که گفته در جریان مذاکرات ۶۰ روزه مقامات رو ترور نمیکنیم، احتمالا تا ده روز آینده از مجتبی رونمایی بشه.
مجتبی قراره احتمال زیاد تو مراسم تشییع باباش شرکت کنه. اگرم پیداش نشد، یه جای کار میلنگه و مجتبی حالا حالاها پیداش نمیشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66763" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66762">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=C6lwoWcWQu9PWJr3fEqJPsQHpnC7SvKB11vxJGt0bGnEqtjJEH0zJ-fHPIFhc0jmOQgw-K0a6piy-lC4CITXukZcYAsFyAzTvhjCQ0rs2F_eSkXjAsOCQr2Yx9ZrHmeXYiHgbnf-9xjjFAZHvnLBDSVTQiiK0BkGm_QKyihXqVeYP-Daszt-jpl8xOUKfYFb_bD9XTptV7dcZUq5Q9gJCQlWiPPOXEh6pEPL9ICv_SiCTcNOmxJajJ1nxraCfaNRv2xR8WfvwlgB7sowkHQWaisZsenzEgYiFSqR_q2MImOISHOiRkn3QQ0nHxwcjo_E9OGNSOHKv5ydkklout59Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65be3ab63.mp4?token=C6lwoWcWQu9PWJr3fEqJPsQHpnC7SvKB11vxJGt0bGnEqtjJEH0zJ-fHPIFhc0jmOQgw-K0a6piy-lC4CITXukZcYAsFyAzTvhjCQ0rs2F_eSkXjAsOCQr2Yx9ZrHmeXYiHgbnf-9xjjFAZHvnLBDSVTQiiK0BkGm_QKyihXqVeYP-Daszt-jpl8xOUKfYFb_bD9XTptV7dcZUq5Q9gJCQlWiPPOXEh6pEPL9ICv_SiCTcNOmxJajJ1nxraCfaNRv2xR8WfvwlgB7sowkHQWaisZsenzEgYiFSqR_q2MImOISHOiRkn3QQ0nHxwcjo_E9OGNSOHKv5ydkklout59Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجری شبکه دو:
کاش قبل از جلسه تفاهم نامه یه سر گلزار شهدای میناب میرفتید.
اگه محصول آمریکایی کیفیتش خوب باشه میخریم یعنی چی؟! یه کم بهتون بربخوره
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66762" target="_blank">📅 15:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66761">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQxL_xqnWUrT3_vc4zvYs9JF-8p-RDDKz20BQeCtdDumWvHqOhBy__2YRCE7y-BzmZV9sE7AE3KDMVScVrVtwXR3zsBupFJyzSF5zJr0VENUHfQ9rTVxqY_s-ICc6viuNK9e5oERo9-wC5U9jM3eILeZ0IjdOlcW3L3TvKMQFlYU-oGNrcIanI-TVd1GhE0re5WNl1pvaZw7QnYVc4xfQt4qgsL3kTGGPEMPpM_JdSTauAdsjUISmSQVRd3j0Ov8mUJoLCEg3l_aXKzTqFztAqUhaUhG4dDFHGTllqiCzWauHUNTFVhALPFrSHw0TTVXlXv3ZI6o4vbc4saAw1FRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله دنیا جهانبخت پاشده رفته کربلا عرض ارادت به امام سوم شیعیان
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66761" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66760">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzfQnIYe32aFOTO4OZFOVvED9bxi3Z6Sc9IYHoLRAldfL_0dzum4qcE2cmyRnZHVPJUN30WUonLsVWOw3Jv5CNYuGWbFdmfIVQtvMm1yzdSQdpvJEJYfQscYWrB22tuzyKa6Vi_f2aNhctrFjHw_rUliOyGFzMvvPp4MciNcQdREtXJ7sL4j6v2e2OiQEZqLY5vcmwkLa8CE0d7jt3NCHAun0xB20YjsgVJ2XqVz_rxp94UoyrK7YmXbWMfyOxV_c42cicz-US2xQy8Thr_OoobPjiTU8ltaYYuuwUlMgeCel9_oWMX6Kb3kuctRfeEn5Ch5IiYh-i1Q_f-MCDTcRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران در آینده‌ی قابل پیش‌بینی به آژانس بین‌المللی انرژی اتمی اجازه‌ی دسترسی به سایت‌های هسته‌ای مورد نظر خود را نخواهد داد. چنین بازدیدهایی مشروط به پیشرفت قابل توجه در مذاکرات است. تبلیغات و تاکتیک‌های فشار بر محاسبات ایران تأثیری نخواهد گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66760" target="_blank">📅 14:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66759">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=aHIBVMQYCIVIbdT9KDHZHVpO0_wju5MCBFRGD5cp4eAvG1q_f8v9a8z7xXx4ARXWAPrRUn4NWail6NnQEXv1f9aMmu1wbZtoAFBLEv6GYMfAMlguAeN_LFSwo-e8_kyH3nWN6L3kBiDuulpB37RBDB4oo4_OCxsbrWfImE_OEfUdy50WXXIy0_-Pv7e5mXFTBvC0vrN4GQqeWpxC30rF_j5SlGn5cEu2VsgQPZsikurzXPnwko1Bk1JY7vdc3W2vjVxhXX9vXriYR9PRfWuHOLsro6DLK85L_Fnw1949CNyI8pOhs2WsUEqV5ZrluAQ5kK2W2I5Dxk8eLmgTDqojjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6644dcda.mp4?token=aHIBVMQYCIVIbdT9KDHZHVpO0_wju5MCBFRGD5cp4eAvG1q_f8v9a8z7xXx4ARXWAPrRUn4NWail6NnQEXv1f9aMmu1wbZtoAFBLEv6GYMfAMlguAeN_LFSwo-e8_kyH3nWN6L3kBiDuulpB37RBDB4oo4_OCxsbrWfImE_OEfUdy50WXXIy0_-Pv7e5mXFTBvC0vrN4GQqeWpxC30rF_j5SlGn5cEu2VsgQPZsikurzXPnwko1Bk1JY7vdc3W2vjVxhXX9vXriYR9PRfWuHOLsro6DLK85L_Fnw1949CNyI8pOhs2WsUEqV5ZrluAQ5kK2W2I5Dxk8eLmgTDqojjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
یادداشت تفاهم اسلام آباد به اعلام شکست آمریکا تبدیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66759" target="_blank">📅 14:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66758">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTw20AbeViuu1eHdwyIXhAS7TG0Zb_QZOO_VP-KRP6SYY0gIUguSxROFlzKvpukBI5hoy1LsDhVb1cZAueVM5aEFM_TJDm0CmygGRwYqA1w-qodytEfZLDVLdc_2meSXzU5UJ-NEUGeiYWRIpy6EkTj5vrXGIdTWXtnr7vs45Fk_gIrh3mqJ__OQkptWvAFQ7axmPOUOUS35nBDhKsERaMSathfo5LEQ86mnw4Z_twGT-4s9yKcldGOMsPORxsRrQoSAPuIHRkZAxImJfmCiygBGSwAJizYX2vNetADxZzvblj2CZouZHMGRzupB2kMwQZXtnii7Hiowe2eG0DlCjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت فست فود برای دو نفر، قیمت سال ۹۶ !
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66758" target="_blank">📅 13:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66757">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=plDx0L4SZkqrLxJmwjQkpCybgC4BETfbOiUEdK6uQd6ZT_rVZyeckywbM8ydWe1MdYSDKUr4U8GKgczLXqEL_guD8C6kODxa0BHY7cVf3VNYxp_8mBSumIvG-m5YJsXnnguTn70irGkP45Xmqs5Qq3VmrfSrIwQsay3wQjm0leI7uLZmEhJEytBehnMmIrmRTclIbVHlBvHPbak7Z7qCbcs_K6-YNbbZ6eQ6E1wbQjmXh0gOdZOP3NE4wPtOzT-NikqM3wd7x1aTMH1CBwzGNL0CGtwiaaO0NWrN5XXGhHy6A8Zj1MGTOf3Ch2JaL69oaChmh_vNihl0sAFYOu1Qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768fbbdd1e.mp4?token=plDx0L4SZkqrLxJmwjQkpCybgC4BETfbOiUEdK6uQd6ZT_rVZyeckywbM8ydWe1MdYSDKUr4U8GKgczLXqEL_guD8C6kODxa0BHY7cVf3VNYxp_8mBSumIvG-m5YJsXnnguTn70irGkP45Xmqs5Qq3VmrfSrIwQsay3wQjm0leI7uLZmEhJEytBehnMmIrmRTclIbVHlBvHPbak7Z7qCbcs_K6-YNbbZ6eQ6E1wbQjmXh0gOdZOP3NE4wPtOzT-NikqM3wd7x1aTMH1CBwzGNL0CGtwiaaO0NWrN5XXGhHy6A8Zj1MGTOf3Ch2JaL69oaChmh_vNihl0sAFYOu1Qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
بلندترین پل جهان که به یک آبشار عظیم تبدیل شده است؛ شاهکار تازه مهندسی چین
تصور کنید روی پلی ایستاده باشید که صدها متر بالاتر از کف دره قرار دارد و در کنار آن، دیواری عظیم از آب از دل کوه به پایین سرازیر می‌شود. این دقیقاً تصویری است که این روزها از پل «هوآجیانگ» در چین توجه کاربران شبکه‌های اجتماعی را به خود جلب کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66757" target="_blank">📅 12:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66756">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=h-OIBTNRWMGddGfWiv2hQqFo7DzWONiy4aSfmNW5WMbYENPQd5JF1PqsCm8xTbN8ICM7F585JWUZmzdxsssnmNy2fpt6GFaYcbETawml4tGd26hxzwiLedvz3iRa1qmazW-1QC2dgJcJuPjowMkb0kLMfs-dAcppwdO9N569sthgAfeA-__EpbCSVQnbvA5e2n7dIviE8co8oLtbyubFN8D1jPWZItWEHJwAKlxC2X-2aUK8PJsjWT791wVhxfQzu2yiA3Z5fgu0teEatAZlPWuBKlbOGrlz9QZu5ltmroBdXWSURs1D0j4OicsLXqBG-2rMxkgK5x4buuls5sxt_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a52e8497.mp4?token=h-OIBTNRWMGddGfWiv2hQqFo7DzWONiy4aSfmNW5WMbYENPQd5JF1PqsCm8xTbN8ICM7F585JWUZmzdxsssnmNy2fpt6GFaYcbETawml4tGd26hxzwiLedvz3iRa1qmazW-1QC2dgJcJuPjowMkb0kLMfs-dAcppwdO9N569sthgAfeA-__EpbCSVQnbvA5e2n7dIviE8co8oLtbyubFN8D1jPWZItWEHJwAKlxC2X-2aUK8PJsjWT791wVhxfQzu2yiA3Z5fgu0teEatAZlPWuBKlbOGrlz9QZu5ltmroBdXWSURs1D0j4OicsLXqBG-2rMxkgK5x4buuls5sxt_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه سرباز روسی که با پهپاد اوکراینی روبه‌رو شده بود، از اپراتور درخواست کرد که اول دوست کنارش رو بزنه تا بتونه سیگارشو قبل مرگ تموم کنه
اپراتور پهپاد درخواستش رو قبول میکنه، اول سرباز دیگه رو میزنه و بعد سربازی که درخواست کرده بود رو میزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66756" target="_blank">📅 12:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66755">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=jdXNidOnQPUQAgPaicw1ywrGP4eT7pQ5KQzkktsWLd5nZ2yL1Wl46B5vVKeqEPXXV0zjLSYQG07LyCPXwuV1_Nxd647SCLFZRtpUnCHI8T0gqFG1AL3865O-X0_wUgTi2K-ZdpnHbFuX_YE4l7Oj9DVfMBxfQP4J7FHj34RVi2at_udf3rDvCe5aP5O6JowFqadlPnDIEQQIfXSMGXgPcoRSRP08CYgZ4xyZHOVBfoaK4EgXcL22HjMDRKnt2sfVY9PWsXdVo9NRQFY0qFp6qMi6DnNCvSo1AVNnm5QILVjO3MDWZtvdS1aDGyowgC9tklFNK3Th7qUvNhnHc5cygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=jdXNidOnQPUQAgPaicw1ywrGP4eT7pQ5KQzkktsWLd5nZ2yL1Wl46B5vVKeqEPXXV0zjLSYQG07LyCPXwuV1_Nxd647SCLFZRtpUnCHI8T0gqFG1AL3865O-X0_wUgTi2K-ZdpnHbFuX_YE4l7Oj9DVfMBxfQP4J7FHj34RVi2at_udf3rDvCe5aP5O6JowFqadlPnDIEQQIfXSMGXgPcoRSRP08CYgZ4xyZHOVBfoaK4EgXcL22HjMDRKnt2sfVY9PWsXdVo9NRQFY0qFp6qMi6DnNCvSo1AVNnm5QILVjO3MDWZtvdS1aDGyowgC9tklFNK3Th7qUvNhnHc5cygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیروز تو دولت اسلامی عراق یه مسئول دولتی حوصلش سر میره و اینجوری با منشی‌ش کارای ناخوشایند اسلام از جمله
لب گرفتن و ساک‌زدن
رو انجام میدن. میگن که این یارو اخراج و بازداشت شده
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66755" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66754">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b320081976.mp4?token=YeKMh6drfNh2FkTDyB4ocyyYCdFoLKpzomxLiod5b8Ni2X_TMnQfbhR2Y24uEvu_iwyci1B5cOKRfAgYT_P2F8D6S4wPszYGGQ-VvfueXZeySBLhfJ9CAmTbVgiI570C3Kb2kjnkOZgrFHQeScQPfPTKPSTFX-4x4pfm_RD-zMim11XssgZdEo3CyE-6OANMh4vonZdRbSGFVUMm7K2TDGi7TlCuf5CP1OMxglawiBcaGiLfXg8dK5A8pMZhEEYES79IrjZmhvBovE4_ZHIse6pHUXl64lK0LvZgC5Hc3gHBiXJXGjFM0QIhEeX1r7j7PVTU3UgWQs8w2H9siIj3Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b320081976.mp4?token=YeKMh6drfNh2FkTDyB4ocyyYCdFoLKpzomxLiod5b8Ni2X_TMnQfbhR2Y24uEvu_iwyci1B5cOKRfAgYT_P2F8D6S4wPszYGGQ-VvfueXZeySBLhfJ9CAmTbVgiI570C3Kb2kjnkOZgrFHQeScQPfPTKPSTFX-4x4pfm_RD-zMim11XssgZdEo3CyE-6OANMh4vonZdRbSGFVUMm7K2TDGi7TlCuf5CP1OMxglawiBcaGiLfXg8dK5A8pMZhEEYES79IrjZmhvBovE4_ZHIse6pHUXl64lK0LvZgC5Hc3gHBiXJXGjFM0QIhEeX1r7j7PVTU3UgWQs8w2H9siIj3Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه ای که مسعود توی مراسم کاشت نهال در پاکستان بیل رو ول نمیداد
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66754" target="_blank">📅 11:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66753">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44438818f9.mp4?token=d1yZe5blTiRbUz-tisrAJU9A7o8byeoZ7fF8olwoBbWjNeryJABO7T4FnADEvXkFlPsZYe48keWHKoGCaiKcpslBnBhgLAZ_Jxrh0btIOgMYu6ARrehU3O_DtvtSkBJ_9DsEaQ4uMVepvAHpfnAcjyMsKcE8vsaTglolZIdqcEi6bOf8JWYmmng5yTfp_PEir4ojMeDL_jeaj6jhPkEaOyB7s2C55U3iWUWo5Ekd0nA8SL_Ach00vMbhFNgCQvl67PGWTXdn-e48D1McGE5dEcneleyU_yeBkswWnFvNYFzZtuliwyjZY1ubxAJh6CvemgZ3vMTA-OmDLfdThJCN1aJMJwd9NPmr6Yn6zN_qNe6ivk9HR82Q2-n50GWxNU1J5GxK56orIVhjbvZ7k7Bt5S0FB41PRB-gx8y_7u-O6K1iM6W44RNrgRgvlPWQR-FR7IgOF-y0Rp60yW2Fnj6FAVvM_yk0ScuJ_ucwam-AU3dHdj5N2s0M7zcOHFcvUmB_cH6O_TOfU4a6p3c75NJgDt2d-U8QdQWalH9ygVLvBnGeCEsDfkkXBwExcEMYyhDL8iUXsct6gcsCo5VeBURaakk0xBTXqt405bGHdNFHrckpzS93T6mS_Z8xXRiGTg_Ciqp2b5s_d3rdhVY1EBDqrVDPcvknGZ61DFYlaF-lHgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44438818f9.mp4?token=d1yZe5blTiRbUz-tisrAJU9A7o8byeoZ7fF8olwoBbWjNeryJABO7T4FnADEvXkFlPsZYe48keWHKoGCaiKcpslBnBhgLAZ_Jxrh0btIOgMYu6ARrehU3O_DtvtSkBJ_9DsEaQ4uMVepvAHpfnAcjyMsKcE8vsaTglolZIdqcEi6bOf8JWYmmng5yTfp_PEir4ojMeDL_jeaj6jhPkEaOyB7s2C55U3iWUWo5Ekd0nA8SL_Ach00vMbhFNgCQvl67PGWTXdn-e48D1McGE5dEcneleyU_yeBkswWnFvNYFzZtuliwyjZY1ubxAJh6CvemgZ3vMTA-OmDLfdThJCN1aJMJwd9NPmr6Yn6zN_qNe6ivk9HR82Q2-n50GWxNU1J5GxK56orIVhjbvZ7k7Bt5S0FB41PRB-gx8y_7u-O6K1iM6W44RNrgRgvlPWQR-FR7IgOF-y0Rp60yW2Fnj6FAVvM_yk0ScuJ_ucwam-AU3dHdj5N2s0M7zcOHFcvUmB_cH6O_TOfU4a6p3c75NJgDt2d-U8QdQWalH9ygVLvBnGeCEsDfkkXBwExcEMYyhDL8iUXsct6gcsCo5VeBURaakk0xBTXqt405bGHdNFHrckpzS93T6mS_Z8xXRiGTg_Ciqp2b5s_d3rdhVY1EBDqrVDPcvknGZ61DFYlaF-lHgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💢
سنای ایالات متحده با رای ۵۰ به ۴۸، قطعنامه‌ای که توسط مجلس نمایندگان تصویب شده بود را برای جلوگیری از اقدام نظامی علیه ایران مگر اینکه رئیس‌جمهور ترامپ ابتدا مجوز کنگره را کسب کند، تصویب کرد.
«همچنان ترامپ میتونه وتو کنه»
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66753" target="_blank">📅 10:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66752">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=TVLMyeDkCVn3RBYTDsiUk3M2M59FaxgIRKPZQUgQvDtIBp8gJsKSH1e_MtU7q3BD4NbHixsMtlrs-W7lRTDcuQe5tDWdO3WL7_LONHwz5D0oJdX1kBnGWQsG-CfZvOUYJFt20FJnGjFbA99orqhR1hCLLSBOV-8p9dpseiR2--tLqRky55ZUq2uIIFGKKsnckiLIX6tE8g7nDawtpCkX1ar84ccGiV5edIARzVxw3gM4dx9gqm0i3k05u-01p5Akteq6yct9NfR9aPlD-NIVVCFIDlL59Xx85y3IrXYH00aKaNQr4KcOSE6bDhGdzVEseWGoDAU4pXT4bRlXAlyu5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea291f4b71.mp4?token=TVLMyeDkCVn3RBYTDsiUk3M2M59FaxgIRKPZQUgQvDtIBp8gJsKSH1e_MtU7q3BD4NbHixsMtlrs-W7lRTDcuQe5tDWdO3WL7_LONHwz5D0oJdX1kBnGWQsG-CfZvOUYJFt20FJnGjFbA99orqhR1hCLLSBOV-8p9dpseiR2--tLqRky55ZUq2uIIFGKKsnckiLIX6tE8g7nDawtpCkX1ar84ccGiV5edIARzVxw3gM4dx9gqm0i3k05u-01p5Akteq6yct9NfR9aPlD-NIVVCFIDlL59Xx85y3IrXYH00aKaNQr4KcOSE6bDhGdzVEseWGoDAU4pXT4bRlXAlyu5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جورجیا ملونی نخست‌وزیر ایتالیا:
نمی‌توان اجازه داد ایران به سلاح‌های هسته‌ای یا کلاهک‌های هسته‌ای دست یابد، به‌ويژه با توجه به اینکه ایران موشک‌های دوربرد دارد و این مسئله را به وضوح نشان داده است.
ملونی تأکید کرد که این موضوع تنها به ایالات متحده یا کشورهای نزدیک به مرزهای ایران یا اسرائیل محدود نمی‌شود، بلکه مسئله‌ای است که نمی‌توانیم آن را اجازه دهیم یا تحمل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66752" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66751">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3361863344.mp4?token=BFOs-mfeur3zoPtBzOFKydG7CJyRxoLjbGc0qcqBndk9pR1hpDkc-v_AWzAsI-sDph_EZnoqPi_f8kCAW-KVcVNWEEKTQEreQuplnJ-JCVBpNCwip1-97HihqDFHQRiutj9R-mSJsbdhrCQqStKBY17Rsqb0r0-RtLbnLoReMqvlD7sQzZKN0vyKbLRY9mB4Pd1Rcxj3BG6UgOC2C76ZV1XyXr7_rKtGQIkWUl2hmZqIVNyszR8g3O3X1Jf0n7ixNE-nkkLLEyUa42JUkB7LkklC-GkLzM1lXNJtDN6Va-uZMw9GNqCAj0Lps6fucuYeLIymb1S8UAzSXB5SXg-9AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3361863344.mp4?token=BFOs-mfeur3zoPtBzOFKydG7CJyRxoLjbGc0qcqBndk9pR1hpDkc-v_AWzAsI-sDph_EZnoqPi_f8kCAW-KVcVNWEEKTQEreQuplnJ-JCVBpNCwip1-97HihqDFHQRiutj9R-mSJsbdhrCQqStKBY17Rsqb0r0-RtLbnLoReMqvlD7sQzZKN0vyKbLRY9mB4Pd1Rcxj3BG6UgOC2C76ZV1XyXr7_rKtGQIkWUl2hmZqIVNyszR8g3O3X1Jf0n7ixNE-nkkLLEyUa42JUkB7LkklC-GkLzM1lXNJtDN6Va-uZMw9GNqCAj0Lps6fucuYeLIymb1S8UAzSXB5SXg-9AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سر دادن شعار «مثل رهبر ما مخالف با تفاهم‌نامه‌ایم»در هیات
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66751" target="_blank">📅 09:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66750">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=e2pwdML4RRxgyVXp2ejKArOMR-Z9GUV7IhMTisg1zIvL9LOHlKkPvPRyWBpvWUvJqDdiJ-HEy0Zozz5iuTS7SRcnUIRlv-XV_6AMsBtjCIw9RnaA7zmfVM7c6nBMN6TubNROOuNhEg5nt79oxU6T3xGFbjxB-X8Klex20vuoe2Maqy_DcKfvzy0p9XQvXFSPBcbLKBJIeUuz4650OexbwEC2uZumdrlNqfZ0z3cI5sh4H9wcLQprXPI5QEaXvCGNpqAg1hWE1OwJ_azsSrnTmmgmyFYPcCrqSRTTnpEawh0aZpY5Nl3egVMB8BKxbw8FJOXYLsvsm3rpgKWdM2Tfvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f22d87ed3.mp4?token=e2pwdML4RRxgyVXp2ejKArOMR-Z9GUV7IhMTisg1zIvL9LOHlKkPvPRyWBpvWUvJqDdiJ-HEy0Zozz5iuTS7SRcnUIRlv-XV_6AMsBtjCIw9RnaA7zmfVM7c6nBMN6TubNROOuNhEg5nt79oxU6T3xGFbjxB-X8Klex20vuoe2Maqy_DcKfvzy0p9XQvXFSPBcbLKBJIeUuz4650OexbwEC2uZumdrlNqfZ0z3cI5sh4H9wcLQprXPI5QEaXvCGNpqAg1hWE1OwJ_azsSrnTmmgmyFYPcCrqSRTTnpEawh0aZpY5Nl3egVMB8BKxbw8FJOXYLsvsm3rpgKWdM2Tfvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از خوشحالی تیم ملی نروژ به سبک وایکینگ ها
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66750" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66749">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/66749" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hSRkQMzUvQGmDYKfixrEiKm9T-wbi-exOPAPnDJ8nze9gBZPJVKl-lgD2VJd8MIqKeXyxve1v4yzM7CPVlC71vIN8xOPRW_QnYzc1cbMqCb-KLLFgBa37s0GNbVsr52TIiBOQmXjktc6dsVUj3jJoxz0eCItnNmV1vUhYY13U35Ayo1CewrvDCIbsfomgbgcp7PSbQ8rAjFn5SwqDtO0FRL6s22sxGEE1vLrGX61Lht9uvW5gjzz2DilFnEJgl4pqEybo3rwyh6VOQHlnRPkE7VIAv1DXQN7lSWXrvT5Z_r2YIv5X7zmdkKxAinPlIOs-_WeRdF7bTSrTZj72Ri43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66748" target="_blank">📅 02:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=uX_iNvxQUKVDlLdY88wgbkX4IUIaclsCcjSYEkF9iQlMqPtXHiGIHNhXOPGKhjatYofl0mKveq1tHlF6sjHDKeYKIpsf5qfTgouyj3TsVK-UyEGxM7tV50vvqHylO5htznawZJLniMR0SF4hII3QZPDw5y692Yk6Jfu4LWw5O4z4swD3aHVtlUJO19RA_EwFVDHBihQYFBreBuTAjTFbu9bxOzJGPJDqnG-4OLKQmbJcxA5jJOrvxvFmS69Zbg0LOHptZnXEG-TATqC_lvmec4pgrsZ_qs2zNTovLuOHFx-XjW9QJ4Q8Ah0c5XpPGEGrDHqVc9VTBm8HzkFPhFa87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89b5dc5b2.mp4?token=uX_iNvxQUKVDlLdY88wgbkX4IUIaclsCcjSYEkF9iQlMqPtXHiGIHNhXOPGKhjatYofl0mKveq1tHlF6sjHDKeYKIpsf5qfTgouyj3TsVK-UyEGxM7tV50vvqHylO5htznawZJLniMR0SF4hII3QZPDw5y692Yk6Jfu4LWw5O4z4swD3aHVtlUJO19RA_EwFVDHBihQYFBreBuTAjTFbu9bxOzJGPJDqnG-4OLKQmbJcxA5jJOrvxvFmS69Zbg0LOHptZnXEG-TATqC_lvmec4pgrsZ_qs2zNTovLuOHFx-XjW9QJ4Q8Ah0c5XpPGEGrDHqVc9VTBm8HzkFPhFa87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«ایران عالی بوده است؛ ایران منطقی رفتار کند و باهوش باشد. در غیر این صورت، مجبور خواهیم شد کار را تمام کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66747" target="_blank">📅 01:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=UUmXTlzIIvSP21B-9CBLzijIqXZLGl4-eR16vYp8wzUHRiSgHTnFzdlUswDMfw4oWD2PxugUvvBLjnjc2TLmS9KRNiRgF2wVn0RUIepL5YuPc5XqVEW1keF_0TWo4ylnkGJIdHHIcyOOxPW7mgNv8Sgx9RLB0-TxsV0waVHa828geboKtLi5foSJQIrPruAWm7OAM4o3c6bgyNDEQnxgpOdMx9pCzUUVZk5_bnZMR5LwBTybUjLoWOpYkn6o8YgJ3UqLDViZnpR3EtwjPmPJv7ZF_CY0uZvAamtKRidHZ-pJoyTstdtR_fSKWjJWUOYUJgamZiZhyP-fDDndIoxBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7d99b64b2.mp4?token=UUmXTlzIIvSP21B-9CBLzijIqXZLGl4-eR16vYp8wzUHRiSgHTnFzdlUswDMfw4oWD2PxugUvvBLjnjc2TLmS9KRNiRgF2wVn0RUIepL5YuPc5XqVEW1keF_0TWo4ylnkGJIdHHIcyOOxPW7mgNv8Sgx9RLB0-TxsV0waVHa828geboKtLi5foSJQIrPruAWm7OAM4o3c6bgyNDEQnxgpOdMx9pCzUUVZk5_bnZMR5LwBTybUjLoWOpYkn6o8YgJ3UqLDViZnpR3EtwjPmPJv7ZF_CY0uZvAamtKRidHZ-pJoyTstdtR_fSKWjJWUOYUJgamZiZhyP-fDDndIoxBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران ایدئولوژی بسیار متفاوتی نسبت به ونزوئلا دارد.
ایدئولوژی مسلمانان تا حدی با ایدئولوژی کاتولیک‌ها متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66746" target="_blank">📅 01:15 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
