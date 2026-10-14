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
<img src="https://cdn4.telesco.pe/file/Ppy3EHLeWhiRw0rxmolyCmCjQ8N-XykUMzUd-YWpq1hWFjvhnzKgoUEyT87hPRAKIN4cEe3_c_P0yiGdLCo6BCObs-xiI9xpHwB_FU8-z2cHb9VLWEJTHnndvED2aS3BbXwDMJy-SOr53xmW_oDzl5l7vhw3uN0IaQFnxMKcrWLNs2jNzUDQJZKqE5BBRWYrZWD1jA42HU4NRM2T_XaqB_APMoHG7LKuAKixq5BC8rYJ60HlE7dfX72t1Uc0RiMpnpQ3kk7u0_7xhFiwN7XpVHqudriRde93O5Sjph_qzr0JO9lYlUuZwJXwZ9crREuSHNq8R7HREQnsy_fn6J9Kvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-152695">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
طبق گزارش ها برای چهارمین روز متوالی، جنگنده های اسرائیلی پروازهای تمرینی را روی آسمان سوریه و عراق آغاز کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/152695" target="_blank">📅 21:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152694">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: دو هفته آینده بسیار حساس است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/alonews/152694" target="_blank">📅 21:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152693">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhXnAJsVKejPR_uNVAl5q4aRmlgGgxWd8dFj45YmidYXRgBqd2qcn7e7SyaXF-g2BosE5xLcwVzvN_MzFeEqb9WZvY5NJQqJGgTCFVlOAIKVCQjGi0w9uuHPJsmyVPf2CeVMI35Up6xwi0hmWQStfVOnh_6aoVIu6dDWFOnkq7re5qZV9mXW-KTqBz5pID4BUo2e68UkPD6BgPexhRqKcAANSzdJt99gEgEg97NUMAB6bQKu9bI9-V83QY7q9z6bXCBBphVgOJLN8K8PliKiaWBkju1R2w4yjsPZwsEwtbARSXKNCEekgkxnYLw9dNQDis6mbGqfI7znv6--83xw2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک اکانت اینستاگرامی، کد مخفی عکس خاتمی را رمزگشایی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/152693" target="_blank">📅 21:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152692">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWlzm5xYc7c5Lduu8ob0PdfxbMQiPAhJnc5CXz3850y5bVrHIqu_urRcBbWfkvbluT8Cc5EpHgLZK5aCvLCjO0asJxuj8b_l_N1DTqNpQL6Vtv0xrBf14Jo6I3hBHAj1Cr2PHmRfbSkhE8f-aqlp_7gNWkYY_kKbN6MqnZJ5UGJSPBI_AANeEsoR2MRl1LHrO1QZSj_L4YJoeY9rAXEzIZ3xgDLT-dLK9Mt0VnLkOTu9fyfpdU0qv4edVtJ3vPC9ZTmrdlAP4fE82gkR58dteAzMEF_JfadkMeA-iPLViGeB_0TeZtAJqGXoMhipkFf_50jwX32ZyGlmunVhuALfSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: بیایید «درصدها رو بازی کنیم». منظورم شانس نیست، بلکه درصد رشد‌هاست.
🔴
راستی، «دو هفته دیگه هیچی ندارن»، «سه روز دیگه چاه‌ها منفجر می‌شن» و «روز پیروزی اقتصادی» هم گذشت.
🔴
زمان نسبیه؛ معلوم می‌شه ممکنه اصلاً مهم هم نباشه. جایزه نوبل فیزیک کاربردی برای وزارت خزانه‌داری؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/152692" target="_blank">📅 21:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152691">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
قالیباف: هم می‌جنگیم و هم مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/152691" target="_blank">📅 21:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152690">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
زلنسکی: ترامپ به ما خیانت کرد. او در طرف اشتباه تاریخ قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/152690" target="_blank">📅 20:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152689">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10c7c9b362.mp4?token=vqXNpbHBP6IURQfufY16QRNDWybFVARluUroe0MgsyATTdY__gd-KbBuuUOa_iqYf1oegGeWS1Zt-25EwBkNfbhCYl9ApzUEV0b22sS-mkjpQcBPnoJM3New5IaCUbfskqpKDBvrMYAvIUpGXhndr-IsuHFLFurE1jW1OsZ3topHk5R8zw2sptDkWCkTLPodFSyJ4oMfSXwbkZqfaCYKbE1wxevmFR3hQyBu7Xw2WAc4nZDn7MZyFxn63pdUJuW5pEhDDcHE2nFsDsyQ5ljiCwmPL0fau1XwjrJ2bZnyXg4J8CtvFanAhmbRoQMOIpfWNEABUeeTPHKZfSz8eIfnYTdN-Gyfw6yJVBFXrDHwY_ScfqbAlC7DhBl6_yX2hzx8ClYUbUk1gI0AtMgiUkqm7ghCmPJn1OxuxvcF505P1ZUR2o8mHYKiiL993yMG44W1jeIBdHxDh1NjyAWWM1BOKfMnxsk-rYabmxl5vWVeN_N9mxj1bDIsB4RDX3PWz15i2Lvrp8VJgXTaJ3iNCYcUd4gKLDOk8xAQhHEKJ8_QS_zcf0eKo4X-pg4wiXKvpqlFmgov6gpB-hj_AzV9LoJ8GNo02LDy_15MdeERZLXXRIHn0gBKytwbKkmLrG3d-uJIiKfLYcfDt1u7IsLWh3s_xnDiCUDLdD_atBiUbMMCMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10c7c9b362.mp4?token=vqXNpbHBP6IURQfufY16QRNDWybFVARluUroe0MgsyATTdY__gd-KbBuuUOa_iqYf1oegGeWS1Zt-25EwBkNfbhCYl9ApzUEV0b22sS-mkjpQcBPnoJM3New5IaCUbfskqpKDBvrMYAvIUpGXhndr-IsuHFLFurE1jW1OsZ3topHk5R8zw2sptDkWCkTLPodFSyJ4oMfSXwbkZqfaCYKbE1wxevmFR3hQyBu7Xw2WAc4nZDn7MZyFxn63pdUJuW5pEhDDcHE2nFsDsyQ5ljiCwmPL0fau1XwjrJ2bZnyXg4J8CtvFanAhmbRoQMOIpfWNEABUeeTPHKZfSz8eIfnYTdN-Gyfw6yJVBFXrDHwY_ScfqbAlC7DhBl6_yX2hzx8ClYUbUk1gI0AtMgiUkqm7ghCmPJn1OxuxvcF505P1ZUR2o8mHYKiiL993yMG44W1jeIBdHxDh1NjyAWWM1BOKfMnxsk-rYabmxl5vWVeN_N9mxj1bDIsB4RDX3PWz15i2Lvrp8VJgXTaJ3iNCYcUd4gKLDOk8xAQhHEKJ8_QS_zcf0eKo4X-pg4wiXKvpqlFmgov6gpB-hj_AzV9LoJ8GNo02LDy_15MdeERZLXXRIHn0gBKytwbKkmLrG3d-uJIiKfLYcfDt1u7IsLWh3s_xnDiCUDLdD_atBiUbMMCMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت ترابری هوایی نظامی آمریکا در دو هفته گذشته بیش از ۸۰ درصد افزایش یافته
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152689" target="_blank">📅 20:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152688">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22ce76e630.mp4?token=AbgSOn6mO6FamgwJeODLwQV0QlqDYvUKkCTughwkbLMPALZml3Du1DhP8k-ODRALc7NtF7HD5nJkrOeWpXGy075XWHAwWWG7mzAk48KcFmCQaNyv2G8oUVEqeMp3if9bOC-WKCiFv_amf2ai62OL59OlOxXSm0VYMi7e4Dr-9SIkEplDSLGQgJ7YcaT6unZ7y_4XvIkkS1EEbgL8KxmZmzUZsoR7HcPJB_IjraAz4HbGQyd3zgvaJNBDsDIGoxkh3nBuSNUKfrvGNwUiiLTIvEGIAY7jylLfNEX3Xu-bvJ6-XsTj-cblyE7HxeSjczBWd21Ccwh9NM-UY67VdByuGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22ce76e630.mp4?token=AbgSOn6mO6FamgwJeODLwQV0QlqDYvUKkCTughwkbLMPALZml3Du1DhP8k-ODRALc7NtF7HD5nJkrOeWpXGy075XWHAwWWG7mzAk48KcFmCQaNyv2G8oUVEqeMp3if9bOC-WKCiFv_amf2ai62OL59OlOxXSm0VYMi7e4Dr-9SIkEplDSLGQgJ7YcaT6unZ7y_4XvIkkS1EEbgL8KxmZmzUZsoR7HcPJB_IjraAz4HbGQyd3zgvaJNBDsDIGoxkh3nBuSNUKfrvGNwUiiLTIvEGIAY7jylLfNEX3Xu-bvJ6-XsTj-cblyE7HxeSjczBWd21Ccwh9NM-UY67VdByuGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی: ما نمی‌توانیم پدر آمریکا را دربیاوریم!
🔴
هر روز کارشناس بیاورید و بگویند ما داریم پدر آمریکا را درمی‌آوریم؛ اما واقعیت این است که ما نمی‌توانیم چنین کاری بکنیم.
🔴
درست است که به آمریکا آسیب زده‌ایم، اما باید دید دقیقاً چه میزان خسارت به آن‌ها وارد شده است
🔴
آسیب‌هایی که ما به آمریکا وارد کرده‌ایم، با خسارت‌هایی که کشور و مردم خودمان متحمل شده‌اند، قابل مقایسه نیست.
🔴
اساساً توان و ظرفیت ما با آمریکا قابل مقایسه نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152688" target="_blank">📅 20:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152687">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff57fce1b.mp4?token=fOFZJQ58hZa8yd6RFjYzoxEITEjUqR29H7YJmiP97CaVWuWiYOjDV-MOJSW3ovj7uJVXk-rf9RYotBMlan7Yk3aGQP9hK7KByIWfy1nfDl8UzCtGvdosR-iQ0GyARuZa1f-9SZ63U967UkeqAn2Kxahp_8jPYgMEW4lKfkQGwLRWJRUrYfTzw6-0Owb9FxxH3k-aTutT8swXMqONdfZz2tQhaebHJ498sJ6dVzEuEHJQOo3xixPDJsxJy1Y3J4AmDZHF-9bGnpU1maUi1jPpo6nXI3g4JPJKa-kaC907rV3y3CsMZLa4HjisRV7e2DPUelOK5aN0-6QrC4Tu58tfPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff57fce1b.mp4?token=fOFZJQ58hZa8yd6RFjYzoxEITEjUqR29H7YJmiP97CaVWuWiYOjDV-MOJSW3ovj7uJVXk-rf9RYotBMlan7Yk3aGQP9hK7KByIWfy1nfDl8UzCtGvdosR-iQ0GyARuZa1f-9SZ63U967UkeqAn2Kxahp_8jPYgMEW4lKfkQGwLRWJRUrYfTzw6-0Owb9FxxH3k-aTutT8swXMqONdfZz2tQhaebHJ498sJ6dVzEuEHJQOo3xixPDJsxJy1Y3J4AmDZHF-9bGnpU1maUi1jPpo6nXI3g4JPJKa-kaC907rV3y3CsMZLa4HjisRV7e2DPUelOK5aN0-6QrC4Tu58tfPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی:
سلاح هسته‌ای بازدارنده نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/152687" target="_blank">📅 20:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152685">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd776cbdcb.mp4?token=ABofCD_yISVdJRdZ1cuyNoDhg2Wgw1PCvqJn2Gl4XujzaTTVjFFgB-0sbiBSm8k9_ViPer4Od2FyPCFi_2i2sItlEwMBeU-qmzuQSv2scwmUAUtmPT33QXWCCilAIrWM_M7Ezd4SnL-BBX7OZILndkNGLb_KFtUzIMy6g69OfgiQXNnXo73PJNtCkVB1lF5QYW-n6IwQ3wn0aPSrYQJG2o_BBHxoNDXy9jpY3AEh8B5AzwCwFO_CjctmuEQA9uYRFwRMLwW6_yNlkXP_B13Qs-rqEGjGus15VNkUzO1HUWpxo_VHmB7uzWZVaLE5N7ruZx7D0oVEGLRDnM2WmqriCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd776cbdcb.mp4?token=ABofCD_yISVdJRdZ1cuyNoDhg2Wgw1PCvqJn2Gl4XujzaTTVjFFgB-0sbiBSm8k9_ViPer4Od2FyPCFi_2i2sItlEwMBeU-qmzuQSv2scwmUAUtmPT33QXWCCilAIrWM_M7Ezd4SnL-BBX7OZILndkNGLb_KFtUzIMy6g69OfgiQXNnXo73PJNtCkVB1lF5QYW-n6IwQ3wn0aPSrYQJG2o_BBHxoNDXy9jpY3AEh8B5AzwCwFO_CjctmuEQA9uYRFwRMLwW6_yNlkXP_B13Qs-rqEGjGus15VNkUzO1HUWpxo_VHmB7uzWZVaLE5N7ruZx7D0oVEGLRDnM2WmqriCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی: زدن سه نفتکش بعد از توافق نامه اسلام آباد بهانه آمریکا برای از نقض تفاهمنامه بود همه دنیا تعجب کردند که آمریکا چگونه زیر بار این تفاهنامه رفته است
🔴
اما پزشکیان گفته من نمیدانم چه کسی کشتی‌ها را زده. هنوز هم رسمی ندیده‌ایم نهادی گردن بگیرد. اگر این سه کشتی زده نمی‌شد ایران دست برتر را داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/152685" target="_blank">📅 20:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152684">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhBHeg6tGo3wUHoT1JC1rbIvdQDW0UWtMh-XpbtoLug9tLV16v5dOnvQTmc6OEAXmKjseK6yzru0egPS1UMZ5a1ifKsGMb1nwGVvnIOplyo7_IQ4fbcc0-jk-wDGEOoo-EgwVQNeOJBd5C2R-BHIUm-Ro-fi5eYXZY57Tr6QQXTNs3esdQf2FUxtcYlf6WNfwpUPQfbsOzMBCFtUVRQOXFi8pHWbj_1VE8Sm3e8S27w4sdX_ZiSxZ3yHfg4Woe_-paK-2KDXbJ1FsdoiBSnuhbp7miropZ7tsN-8PVvm1SnsLrobCiN3QWdm_ZELUq6b_MfWh7dTQkGaN6C_Q4W7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کرباسچی:
باید قبول کنیم حریف ایالات متحده نمیشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152684" target="_blank">📅 20:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152683">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کرباسچی: باید هرچه سریعتر جنگ خاتمه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/152683" target="_blank">📅 20:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152682">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
کرباسچی: باید هرچه سریعتر جنگ خاتمه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/152682" target="_blank">📅 20:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152681">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9180b0e9.mp4?token=gx5KMg1huI6lMvAevAZzbtj34qmOfs_DB78nBKlTeuPQtngALj4DEpxoJw0jY0qRQhW05BwaAYcP23jVOW2PAY9fSp1xiM6fmjlRkWCw9kwpXiZYPGGjlUYm_HRiU5EMAmFKfbsCn6G19Vo5HdcqGDLdEKMnw6x8d6sVRTJt4l2rr0ntXpa9S5a0TrAM3lmKn4PA909DTApSiVmTsVWs49jZEKRdIyOuKAh6VvFn4iPhGZGiBxIgyKIpRUVWPEkEie4u07110_WHl66r-wSrp6zPVQ6jsO08Ts3_SnWkAzORJnjbeuwrkj5eU6HUt639jh59clCIGKIwO_Xu6o6dRqYhuwuK9hHK-CMQibDlenqcEcuXEUpUCzT7uJJqvtok3AwVZK9Et2ysKbQttps226UpUkaAL-oss2kq7SV1uJhquClUPfBKfMqXRubdKTFKLhcOYs0DORBsJTSQeSO4TQbzYMyxk6kR3MJkZzMwvdxC4pGDg-VkoJhfcpkN2mEqF57G3_TNL2MbArwS-A0bX8MA4pPZ3dtXmUyidMijsepCeNO_UyLljgD58LvuuQIUcJLYzcy2URE0pBLFbpC6CVpxJWPUqwgwArePwq99GU01OsR4PIAasjlMxv6l7L-SNvW-_HYbcvoY25k6bS__rmlx4mBBVHyr6DqnblLyZmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9180b0e9.mp4?token=gx5KMg1huI6lMvAevAZzbtj34qmOfs_DB78nBKlTeuPQtngALj4DEpxoJw0jY0qRQhW05BwaAYcP23jVOW2PAY9fSp1xiM6fmjlRkWCw9kwpXiZYPGGjlUYm_HRiU5EMAmFKfbsCn6G19Vo5HdcqGDLdEKMnw6x8d6sVRTJt4l2rr0ntXpa9S5a0TrAM3lmKn4PA909DTApSiVmTsVWs49jZEKRdIyOuKAh6VvFn4iPhGZGiBxIgyKIpRUVWPEkEie4u07110_WHl66r-wSrp6zPVQ6jsO08Ts3_SnWkAzORJnjbeuwrkj5eU6HUt639jh59clCIGKIwO_Xu6o6dRqYhuwuK9hHK-CMQibDlenqcEcuXEUpUCzT7uJJqvtok3AwVZK9Et2ysKbQttps226UpUkaAL-oss2kq7SV1uJhquClUPfBKfMqXRubdKTFKLhcOYs0DORBsJTSQeSO4TQbzYMyxk6kR3MJkZzMwvdxC4pGDg-VkoJhfcpkN2mEqF57G3_TNL2MbArwS-A0bX8MA4pPZ3dtXmUyidMijsepCeNO_UyLljgD58LvuuQIUcJLYzcy2URE0pBLFbpC6CVpxJWPUqwgwArePwq99GU01OsR4PIAasjlMxv6l7L-SNvW-_HYbcvoY25k6bS__rmlx4mBBVHyr6DqnblLyZmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کرباسچی: باید هرچه سریعتر جنگ خاتمه یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152681" target="_blank">📅 20:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فرود اضطراری پرواز تهران-استانبول در تبریز
🔴
پرواز شماره ۹۷۰۰ ایران‌ایرتور با ۱۱۶ مسافر که از تهران عازم استانبول بود، به‌دلیل نقص فنی ساعت ۱۸ امروز در فرودگاه تبریز فرود اضطراری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/152680" target="_blank">📅 20:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152679">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
رهبر کره شمالی خودکشی کردن رو ممنوع کرده و گفته هرکی خودکشی کنه و زنده بمونه، خودمون اعدامش می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/152679" target="_blank">📅 19:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152678">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d51b184a4.mp4?token=snPcPxvSAuwpEUqYW4WOy3y470QNzKm6gDcwfG1tlZXZmtv6MWmPJ4jTEysQNhEyvsVXfBb05bEq7FFN3oStWzJc7yPlCKxfPrNQNYLWxV_YfU5KrtWL0GsYOhNXPUru-sJcuKQ__d8mPylTIEz-nnKYv7s1XCRHP7n2h2dxfD1tNrxlrS7Zdl2qMHzsXkWx5ytb5Z6A0k9qgnuZQwirLykiHs0dbdb3ZM031EKOjfgeGzmxGm93lVpqjts80SR9yHiJeVcLBdif9fxA9OQVvwpcZEcnUM0M5JhUWiCXhALPaaJPscBtKWjZCIkeaqMtKy1GJMNDWzx7yiQvYu7bLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d51b184a4.mp4?token=snPcPxvSAuwpEUqYW4WOy3y470QNzKm6gDcwfG1tlZXZmtv6MWmPJ4jTEysQNhEyvsVXfBb05bEq7FFN3oStWzJc7yPlCKxfPrNQNYLWxV_YfU5KrtWL0GsYOhNXPUru-sJcuKQ__d8mPylTIEz-nnKYv7s1XCRHP7n2h2dxfD1tNrxlrS7Zdl2qMHzsXkWx5ytb5Z6A0k9qgnuZQwirLykiHs0dbdb3ZM031EKOjfgeGzmxGm93lVpqjts80SR9yHiJeVcLBdif9fxA9OQVvwpcZEcnUM0M5JhUWiCXhALPaaJPscBtKWjZCIkeaqMtKy1GJMNDWzx7yiQvYu7bLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سینه‌زنی بیکارها با شعار:
🔴
«ظریف آمریکایی مایه نمگ مایی، فریدون نفوذی مفسد انگلیسی»
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/152678" target="_blank">📅 19:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152677">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">dbbet.apk</div>
  <div class="tg-doc-extra">45.9 MB</div>
</div>
<a href="https://t.me/alonews/152677" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#دیبی_بت
😃
😉
🥲
🥲
🥇
اپلیکیشن رسمی دیبی بت
😉
با اپلیکیشن اندروید Dbbet بدون نیاز به فیلترشکن شرطبندی کنید
✅
#Dbbet
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
*️⃣
🎁
تا سقف 100 یورو بونوس‌ با
کد هدیه
2️⃣
🔤
2️⃣
🔤
یا همون
(
2K2K
)
👑
آدرس سایت :
👑
https://DbBet.club
☑️
کانال تلگرام
🛡
@dbbetif</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/152677" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152676">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfNteqNTVU-TnywnDQ9joI-UZ30ztA3q23_mG7rniZjcKmUgwfEkSL9Sba9ZUlrhr6-RGJ8xdTISO4VHh1rJKxhwsGrJ0YNQJKok6LhJ8tZmcsZVOI89Xt1A-VjtVoGV__0UAwI4jVm9NFjEu_b1z7ucu_IhDLO7FHP5col4RejlGP6jmmHGWooeprWrVp5aQ6XrCqe1nvXjRT6jSV6UovMXKsseoMhS7P07FZSNIjUiALfZtScc7BaSxyiHbkSkgFzTB-Xd6T9Y5QvVtwRRIj7YItO3x_P9if9v3EYalnOc_8v_uGpgpDeLHljdLs50ij7MaBM5uHh8jW6YeUGfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
واقعا چرا دیبی بت انقدر در بین ایرانی ها محبوب شد
⁉️
➕
دیبی بت اولین سایت پیش‌بینی فوتبال ، که تمام ارزهای دیجیتال رو برای شارژ حساب پوشش میده
💳
درگاه کارت به کارت امن ریالی برای کاربران ایرانی
😉
اینجا با خیال راحت شرطبندی کن و درآمد دلاری کسب کن
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
😊
https://Dbbet.com</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/152676" target="_blank">📅 19:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152675">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwiQBxGQiLhrA1NWIitQkRBQrSxqpDw3U46M5o2eGU0wxnPyYiXXkYseLNdflUGFgjmA426d4PJvl4eufOm-CjD5-CagB9Qsl2rnvotqGqT2S7hVyfbBpBWEvBCb_iQhxi5885yXoBjSio0o8C9InUG7V2jR3rsOrRTIHOC46lXD6lv55qNOgGCT8x6qs5aUUHC44VKt7rtuRFQ7y_YQ_1lSIQ1EpzPrelipR2BTWW6okQWwqAb8rdYlsE7vNYs4yLagUPZ3dFHyTRYzhUkMCCSryhFlpPNl-m3xBtoG9oYzbdIMpyOSSTP6JwOz9O2GCyPCZu1_ZU_cpxwnQxczew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار الهام علی‌اف رئیس‌جمهور آذربایجان با رئیس‌جمهور اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/152675" target="_blank">📅 19:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152674">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش شلیک موشک از قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/152674" target="_blank">📅 19:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152673">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
اسرائیل ۱۲ بالگرد پیشرفته آپاچی از آمریکا می‌خرد
🔴
اسرائیل و آمریکا، قرارداد نظامی جدیدی را برای تقویت ناوگان هوایی ارتش اسرائیل نهایی کردند.
🔴
کابینه اسرائیل پس از چندین بار تعویق به دلیل چالش‌های بودجه‌ای، خرید ۱۲ فروند هلیکوپتر آپاچی پیشرفته مدل E ساخت شرکت بوئینگ را به تصویب رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/152673" target="_blank">📅 19:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=a0aoQ5Gx1TRVHL3hXrVhAjPr4s0ap-rfpkKnAzusCDawcNbt8aFAjCa2bIZkQQfQYC_twFJEPv9ZdMQspy8Z1oJ8TDJ2HF3BUyJCbz0R_Dq4Q9FHhqhdtJsKWboJB4VoJ6rFY4ZfGmV6Mo84QQ8x1epRiHZwtmnyoUWGMU-IS5bgUBt_p0tpTsBz26vzdwJRC2arVQMtxDZ6wO57Apt9w6R00VXFRdR-7Y_VRzNZ8xYnLHK6026zouZzfuxvwN1TcKuYbmLlAQn6Y_atb193yZKfZaB4psD2YC13WeUiVt_x428IN-qxPgI_PxJH70a49yhVISZ_JMvwNPDOXxdYkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac361504bf.mp4?token=a0aoQ5Gx1TRVHL3hXrVhAjPr4s0ap-rfpkKnAzusCDawcNbt8aFAjCa2bIZkQQfQYC_twFJEPv9ZdMQspy8Z1oJ8TDJ2HF3BUyJCbz0R_Dq4Q9FHhqhdtJsKWboJB4VoJ6rFY4ZfGmV6Mo84QQ8x1epRiHZwtmnyoUWGMU-IS5bgUBt_p0tpTsBz26vzdwJRC2arVQMtxDZ6wO57Apt9w6R00VXFRdR-7Y_VRzNZ8xYnLHK6026zouZzfuxvwN1TcKuYbmLlAQn6Y_atb193yZKfZaB4psD2YC13WeUiVt_x428IN-qxPgI_PxJH70a49yhVISZ_JMvwNPDOXxdYkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سعید لیلاز: پیام آمریکا به ایران قبل از جنگ ۴۰ روزه: کنترل نفت ایران را به ما بدهید تا به شما حمله نکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152672" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ایرنا : خطر خاموشی در زمستان جدی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152671" target="_blank">📅 19:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نام برج میلاد تهران تغییر کرد
🔴
بر اساس حکم صادرشده از سوی علیرضا زاکانی، برج میلاد تهران به شرکت گردشگری و تفریحی میلاد تهران تغییر نام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152670" target="_blank">📅 19:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz3agRBAnDV0ujAkiUyg4ikqgTArNKNhc4UgcUM7wE_92tzlcO8oXT8ceiXGn1a0h2EBmhau4shChE67chE5CJLU9aD6-UAGy3_S964jYmwt6P1W1CYVL_CTfIYAmgAaTKQLyCGaNXqpkc3I1elnFlMf4BjCZU5OzcD8x_0HhfUE83pE36yuCWK-9yeIhRd9p7lYMHS5mKEe2ZUX95uE3YpuQLldC8rU2Axp4ZfaPmyNGYBbIt0FbyRl78aH4VPpxHIoR6LAnPJZhq5j6sbLz4kDa3guQS7yHJLCoStbs1o_H7EZnFace6mfxBd7bxklQPrlnWnlGhz5Y7xAoyURFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش آمریکا در حال انتقال تجهیزات نظامی از قبرس به امارات است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152669" target="_blank">📅 18:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: در حال حاضر، کنترل تنگه هرمز را به طور کامل در دست داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152668" target="_blank">📅 18:49 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سازمان دریانوردی سنگاپور: دو کشتی‌ کانتینری طی دو روز گذشته هنگام عبور از تنگه هرمز، مورد اصابت پرتابه‌های ناشناس قرار گرفتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152667" target="_blank">📅 18:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152666">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzsTzkxCtjt2OVvsqwTuYvUn7pK6xTI30d2t2bBFnx49xsMxPh5h1v_Rwb87Tg9-FQ5mdnDRHYv6h0l0LUMzeqv2ExRnyCFMJH44Cx0VdeFjJ4XHxEgA7kLF9p3EsL7-OoW7zOlxQW8naJgQnJ40RvSG74uGOag3-GIRgrv8Okus6dVf8jODKCgvt_w5aYN-OX3XSsILOQkwAE3GrcgwC1P8xj0AwiRozI4B2MpcO4VEOwIedN8DHVu82qpW3JIoyJsrguT2k3Qxz28uU-FExhwll7cV4hknm46wfBLDJWqYDKpAnF4vHw7nSZ-9Gfk_n9YYJYOfMMtJvDCPUeAZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم آمریکا در سپتامبر به بالاترین حد خود در سال رسید: ۳.۷ درصد !
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/152666" target="_blank">📅 18:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152665">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87f461be38.mp4?token=fAMZtiXRnFWqSnz6kBTGgX-YRCUu-X5hHyed4QuNoB3QgIHkjem55MeaTdQ4nYu8-wEwclbMbezgJjfI3bjcwk0FBAwftK5rG_uaTrZKvn6j6ciGHeq79jDhoTaAyOcUAyf1e0fUj2ak1sCFF9_-U0VupyrUyETG4kFGT12o3jw0tCi2DM_oKfvLAIqhBYtrdjyEdspxkrD2yADH5Zt7TPvaawnMTrdIwDDl4LNjE-DNBmWi6UWhMXBAih5NBT2dxb6NgY3LtIbSLaKtu8gmBEMX_xbv_Msa5Bfn1Zgm_r_mv7jIXmUfsxIOi4mCA2-q_MhlQ68MI8yA0g7-Q8DlAIACyxdP50UZdQqQuskSsJL2ohwA2DAJwkQNHvXyZ7xF8hZYE1uZigNvw6bQ5cQClY5QEHg8T-co4RA5ksIfYun4gEmrjyUTJmmmjA7Fc3wbnlCjn_9vr_lqKVn5jyEGo_nQ91FGOAjdTVxQIwsH8hF0eUi4f12ETMt3RnOymy36oOeiet9xrcvC1rRatn2tFMDQ-FR5na2PS_9lDa5_Eq-peB2hNK36SndjTTgAJqrbRCQqaez0gA-ECSY6hstq2abqG2yQFBwCMcEwjA68pAwuB7EKwrsY2n4dseSqChYwSqnWCk-KEFbdp5Ow45NapgOkEXZWWzakZn6o3e8Aamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87f461be38.mp4?token=fAMZtiXRnFWqSnz6kBTGgX-YRCUu-X5hHyed4QuNoB3QgIHkjem55MeaTdQ4nYu8-wEwclbMbezgJjfI3bjcwk0FBAwftK5rG_uaTrZKvn6j6ciGHeq79jDhoTaAyOcUAyf1e0fUj2ak1sCFF9_-U0VupyrUyETG4kFGT12o3jw0tCi2DM_oKfvLAIqhBYtrdjyEdspxkrD2yADH5Zt7TPvaawnMTrdIwDDl4LNjE-DNBmWi6UWhMXBAih5NBT2dxb6NgY3LtIbSLaKtu8gmBEMX_xbv_Msa5Bfn1Zgm_r_mv7jIXmUfsxIOi4mCA2-q_MhlQ68MI8yA0g7-Q8DlAIACyxdP50UZdQqQuskSsJL2ohwA2DAJwkQNHvXyZ7xF8hZYE1uZigNvw6bQ5cQClY5QEHg8T-co4RA5ksIfYun4gEmrjyUTJmmmjA7Fc3wbnlCjn_9vr_lqKVn5jyEGo_nQ91FGOAjdTVxQIwsH8hF0eUi4f12ETMt3RnOymy36oOeiet9xrcvC1rRatn2tFMDQ-FR5na2PS_9lDa5_Eq-peB2hNK36SndjTTgAJqrbRCQqaez0gA-ECSY6hstq2abqG2yQFBwCMcEwjA68pAwuB7EKwrsY2n4dseSqChYwSqnWCk-KEFbdp5Ow45NapgOkEXZWWzakZn6o3e8Aamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد انتحاری اوکراینی، یک هلیکوپتر روسی مدل Mi-28NM را در حین پرواز، در منطقه‌ای از خط مقدم مورد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152665" target="_blank">📅 18:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152664">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
معاون وزیر امور خارجه روسیه:
مسکو آماده است در صورت لزوم تمام اورانیوم غنی شده ایران را به خاک خود منتقل کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152664" target="_blank">📅 18:13 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
به گزارش والا نیوز، رئیس ستاد ارتش اسرائیل گفت: ارتش اسرائیل در وضعیت آمادگی بالایی برای انتقال به عملیات تهاجمی در مقیاس بزرگ قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152663" target="_blank">📅 17:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152662">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayKrDdE7gAOFH9wKemjOxxsVsfN5P91lntFg8ZieHqU6qJVTw7S-nOR-7ZmOH6UJps1Rw5XoV6cv-MDq54G7xu2xRkCgVdSqRapcVAMJfxZ6ZbURv-y6_R_SfmsOgRVBIsUs_lAUDyp7lGNAUqJVgHiYVmIoyXiT0BIt6l5SR5rkB51PVeJIWkTAzpY6LxQWSj4I97YdRys-Z6XfwUrQqSAi4edFrFeMuKt5nlhzK949E5YGXgsIkMYl1d3urtuPRLP99EutQGvihOoeZb3KVh14fa_BCOz1nBOrTNq6RnwqWREbdRo-glMF-yBa_aBujdN0XVqe4tS1tkWzb47yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالیه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/152662" target="_blank">📅 17:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152661">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4UqvrhIIokARl_w2LJPhw-2-SWtIwmUqX-zaJsAMk_zGEX71Ed9d6tlowfFZoPyLpqH_oA_zydjtc_g3fV_LSakl3nbp7TKt-92aeS8VYn4eeTd_JKTj78-HE-U5Tnb-mMT6OBCO0bI6YERgrFrfVs_SnpcsHsDyIH0kR2fYt4PkfQ3SjpLbkUE_FMmZ23ryJKrVwXoM5_wwF9vHlxW38qcCAcGuRbqCV5lXZbCxc5uBQPb1AeMhq7t1DYKKEKiBD-EgCAlcyjbKfDTDlglb5pqqIkgP7cz12VY8n__9e54b-xvnbPLgfgM9sML-ni-jv4UmurZRj_oA69e6f-tnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قائم‌پناه،معاون پزشکیان: هیچ مذاکره‌ای بدون تصمیم شعام و تایید رهبری شکل نمی‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/152661" target="_blank">📅 17:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152660">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
جزئیات جدید از نحوه بمب‌گذاری پیجرها از زبان سفیر ایران در لبنان
🔴
یک لایه مواد منفجره نازک ۲ در ۴ سانت در لایه‌های باتری پیجر جاساز شده بود؛
🔴
حزب الله از قبل از انفجار؛ به پیجرها شک کرده بود
🔴
حزب‌الله به پیجرها شک کرده بود و یک اسکنر کشف مواد منفجره از ایران به سمت لبنان می‌رفت که با موشک زدند.
🔴
یکی از کارشناسانی که قرار بود پیجرها را بررسی کند؛ قبل از انفجار پیجرها ترور شد!
🔴
جاسازی پیجرها در آستانه لو رفتن بود که انفجار را عملیاتی کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152660" target="_blank">📅 17:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152659">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
جماران:
احتمال گران شدن ۴۰ درصدی اینترنت از امشب
🔴
بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152659" target="_blank">📅 17:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152657">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDMRPijx-iFDByp16LTIKsuxQDkraLZnB5-WIWSrZpjrd_Yu-kg6ZhtZcGtR4m4lpT0BmI36nswQVcTWod8Oe18XEq1opQlmEcC2M5Mgcs8QifsbygV5FQEWWNZPA-dtI1ox1GDqgtDxlm48nIscrxNCavBDlRE-3sLUPISYSBoB4YAYTpV9yUpw5rohEUCcr9zS7U3jET_NqKuwcLuOnduYx582zIc1WRwrorVAfDahoczedPPdYXVra0jxsdkIFKBcMrARdlSF5NQsW5uLpA-kmPlactx8y1eTswgKvYF2mPZkh2u1Ur3XXmU4TrP6llIEjAES8h0gYRrrAtS18A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8sr42Nhhxh--Pt2EYC1yrLA6tCYSGuXgI0yWpPA1D21oIgfh3VjI7lk2YdAoJlNcsnxjN-RgMvfOMBRmAQlwMs5l_U3_mSnaH5c7MOkteeuI3saVnf0D1NvOTyWgrMcgu88X2DY0EVFTzyCYUg7aPZrLtJ2OJwxlUPkQsdj3WW1_2smf5fKoPI8iftwGw3yPTs1UO_JhlpJqlAh0bP7dWik02CaYfW9UenIgxGPSTUuK87tDD-81lsgDgdmVJxRTZjrL41P9GNvL2D9oJ2scdCsx4JyT6jwt_mZsDTWd_xwciU2b8r4hG19r7Sl5YyJkQ1D7RQ9J0E4infdI4nsoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای آثار غرق شدن کشتی باری «GFS Pride» در تنگه هرمز را نشان می‌دهند که هدف حمله سپاه پاسداران قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/152657" target="_blank">📅 16:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152656">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
بیانیه دولت عراق: زیدی، حمله به فرودگاه بین‌المللی خالد در رياض و هرگونه حمله به غیرنظامیان و تاسیسات مدنی را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152656" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152654">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sngx_hlYQqCJjzE7JN9gMwlR7_yQERX5-MTeX-DsshwCe1c_Z8SHPAXHVXIem5xwh58o6ecsSTjRIi_sb4lpCjJmcZRctbvc7AXmoZcjAIhDAoSMQgNVF5l1STuViaH_abX1M2IkN8n0oJaRVeSUF9meyQ4FeKXkWcaOAOtyQciS_GEkpXG9toXFNlWPUBUaD9lWlRf0RGEGxjoscFYlVTfyE_uj9zL5Bz6ay_hSEnSVW7Tm-B0w92C-oVVylwfHWFy7Fij8bHHmgsn1U4nEd5EZRUN93FsQHsoYxYr0U0rzoSN3rijxQU0ORFmvIOMuuCKucqW1kfulIxgtkvr8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrTf_f9pg3WsxxJ6Ju99GbbaE_PlCcGIBKV1MC61uJXg9mvplJcov-KB7uaf2oWNRR73nid7Fv1EWXafUjPqoxqVQM6fHauBYt1o8a77NN0Mcqw8BZLOUIuR2OihfOiZvdkdG42ZcEFnnRnzmAzduDNFE2YIgcEGGRJ-LnqhY1pETLl7VMQ9nU0ae4VniRvSXt_khzZADIg7mPNIptIG0wbXbT83nNFywOGKHsXOcxH91389K2rL3i29yYy5mCS7B8k2y_QIWac42J46T4r_ohnxyk11TwXRbNnCYxXNeWt-DokvK4GHc619LriGDEasZs5Fop_ny8DYF1cLJaCubQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر بسیار عجیب خبرگزاری مهر و ایرنا از ناو هواپیمابری که درحال قاچاق خودرو به داخل کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152654" target="_blank">📅 16:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152653">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
زلنسکی: روسیه شب گذشته با ۳۹ موشک بالستیک و بیش از ۱۲۰ پهپاد تهاجمی، به طور مشخص زیرساخت‌های انرژی ما را که شامل آتش‌بس می‌شد، هدف قرار داد
🔴
مسکو اظهارات ترامپ را قدرتمند و بازدارنده نمی‌داند
🔴
از رئیس‌جمهور آمریکا می‌خواهیم تحریم‌های شدیدی علیه روسیه اعمال کند
🔴
هیچ کشوری در جهان نباید در برابر بازیگری دیوانه مانند روسیه، تنها گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152653" target="_blank">📅 16:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152652">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4482fcb60.mp4?token=JD70Bo_s_a8yI9eNdw5U1_j6S7ptop-em21tHiUMR3_7kL03-Z11ZBEhjwP5eIzyK3bTC2gh-7DKz56GYSvuXX3Guikg-H1ZhFaVuXWh24SCyA--sAyHeY6_lcXuwvqXs6u-1-wDPl7-BYHpL7mhaV2YN1rmWJnOkGDzwOOScz0yypQU3dbGLoWT0EY2ltJJO00PLxyR4mrqJ3AguyIHDMjeXbFVGLQ0Q7C5nD17A2muyP5WMXi5EOe-8w69TB7TTdofFqZbQNkfkii-GGqx3rY1EtHl-aAcjjRmlDGwF21AuekDVdPPacJz1jk-ALOgJTikEttTtFfljwewayJV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4482fcb60.mp4?token=JD70Bo_s_a8yI9eNdw5U1_j6S7ptop-em21tHiUMR3_7kL03-Z11ZBEhjwP5eIzyK3bTC2gh-7DKz56GYSvuXX3Guikg-H1ZhFaVuXWh24SCyA--sAyHeY6_lcXuwvqXs6u-1-wDPl7-BYHpL7mhaV2YN1rmWJnOkGDzwOOScz0yypQU3dbGLoWT0EY2ltJJO00PLxyR4mrqJ3AguyIHDMjeXbFVGLQ0Q7C5nD17A2muyP5WMXi5EOe-8w69TB7TTdofFqZbQNkfkii-GGqx3rY1EtHl-aAcjjRmlDGwF21AuekDVdPPacJz1jk-ALOgJTikEttTtFfljwewayJV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شاید بتوانیم یک کشور فلسطینی در اوگاندا تشکیل دهیم. آیا این می‌تواند راه‌حلی برای تمام این مشکلات باشد؟
🔴
نتانیاهو با خنده: «پیشنهاد شما به‌طور جدی بررسی خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152652" target="_blank">📅 16:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152651">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=e23E2kZVJBmRBEtFYhfI1z-FZ9YfmPPIm8_Uwe-Cb6tNbBIAVj9xu5rbrx1g05BspkCp7lgTJ6a_cNPKp7bfD6QQni2FyYEl5xXp1b1USNnIN-hZx246smHganGAnYCIwnolKYSpcREt2m4yvYUybgoFXTXiBbL9IHkIIinxz4WJ1gpsDEL3WqcGIIMILqsP6BZx1hB4ZdhlwKGk08UPW0N36ylUKXlgescRY82-VOYuZ3FWdoFfZRi0lUEMvuh0_FGbcB5zbRbPI8J6jelllLf_5k-W34t8PJHwQpsaTN-406Qz-UWntnwrdeNpql9sENmz5-f__MATZhYahLsNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=e23E2kZVJBmRBEtFYhfI1z-FZ9YfmPPIm8_Uwe-Cb6tNbBIAVj9xu5rbrx1g05BspkCp7lgTJ6a_cNPKp7bfD6QQni2FyYEl5xXp1b1USNnIN-hZx246smHganGAnYCIwnolKYSpcREt2m4yvYUybgoFXTXiBbL9IHkIIinxz4WJ1gpsDEL3WqcGIIMILqsP6BZx1hB4ZdhlwKGk08UPW0N36ylUKXlgescRY82-VOYuZ3FWdoFfZRi0lUEMvuh0_FGbcB5zbRbPI8J6jelllLf_5k-W34t8PJHwQpsaTN-406Qz-UWntnwrdeNpql9sENmz5-f__MATZhYahLsNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152651" target="_blank">📅 16:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152650">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIJL8kBsUIiZdN7zEmeVc_n4DhzaVQvq0H013pqI_GxFjKw1vNNhnbIJgAr3TeE7NEtjZ4URzeTQfpy5P7KEtEV2hVtXgUANAbF-F5PINkQhXkY3rLZ64_fGdllxrXGo5mCBKMps1KEyo8JJMWFtiqMaIJZana3DwVpZdQKBbfF9GLTz9wmocbp-kCW1_NyXc0kF2y2m_7UtHnYR99BueM41wGhJxFOBCGhDUmV8E56PSUag7SgElGYP_k53quVZhvwy_3wHT_Gy0zuo_rv_nLV42xT8EPLuyPjC_5aW2iNIXjde2M_V_r8D9PaYfOYiTdzPSGFm_cThEUYj8ol1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اکتشاف گسترده نفت، گاز و مواد معدنی در گرینلند آغاز می‌شود
🔴
دونالد ترامپ در شبکه تروث سوشال نوشت: «اکتشاف گسترده نفت، گاز و مواد معدنی قرار است در گرینلند زیبای ما آغاز شود!
🔴
کارشناسانی می‌گویند ذخایر نفتی که به‌راحتی قابل استخراج‌اند، از ذخایر تقریباً هر منطقه دیگری در جهان بیشتر است.
مهم‌تر از آن، گرینلند از نظر امنیتی و دفاعی، هم برای آمریکا و هم برای اروپا، موقعیتی بی‌نظیر دارد
🔴
هر حمله احتمالی آینده به آمریکا باید از مسیر گرینلند عبور کند؛ جایی که سامانه‌های دفاعی ما می‌توانند پهپادها، موشک‌ها و حتی سلاح‌هایی را که هنوز اختراع نشده‌اند، رهگیری و منهدم کنند.
🔴
گرینلند از نظر زمان هشدار، موقعیت جغرافیایی و میدان دید، شرایطی فراهم می‌کند که در هیچ جای دیگری از جهان وجود ندارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152650" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152649">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
خبرنگار الجزیره گزارش داد که نیروهای ارتش اسرائیل در حال پیشروی در غرب روستای صیدا در منطقه جولان در حومه قنیطره در جنوب غربی سوریه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/152649" target="_blank">📅 16:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152648">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بر اساس ردیابی اطلاعاتی منبع باز، بیش از 19 میلیون بشکه نفت خام روز دوشنبه تحت اسکورت ایالات متحده از تنگه هرمز عبور کرد. حملات ایران به کشتیرانی در طول روز ادامه داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152648" target="_blank">📅 15:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152647">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rkyv7d1_nG4gm-I6hNflq8_obhZcNaAFa0zS9fmrhnEIsq4Q59m3qtNWOmLkqIlc6mmhzXztueJsPM2AlCAazHZTuV_t10BZbaX-_hcB9HcRXXR4S8e9ZEi-jut-NzqASZvuJtZCbk9BKpNprbREivGnZJCswNTfB7bqNUANEYTF8dwhuaTxfBvvu2qp539_DRDlxLw7BDYq_dTtIU0ixNFXFNwD0bBDP3RTZgkVz5fRi6msVRZjeBqeIwr1HIuZQcgEMIL8nzUewWx5rh6Lbb1TxMB6ZTcZm_WFmj7wCrL9IrcTMQUwGqN2UL06TjgMefhtIJi5jUCOGblLkNTCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rkyv7d1_nG4gm-I6hNflq8_obhZcNaAFa0zS9fmrhnEIsq4Q59m3qtNWOmLkqIlc6mmhzXztueJsPM2AlCAazHZTuV_t10BZbaX-_hcB9HcRXXR4S8e9ZEi-jut-NzqASZvuJtZCbk9BKpNprbREivGnZJCswNTfB7bqNUANEYTF8dwhuaTxfBvvu2qp539_DRDlxLw7BDYq_dTtIU0ixNFXFNwD0bBDP3RTZgkVz5fRi6msVRZjeBqeIwr1HIuZQcgEMIL8nzUewWx5rh6Lbb1TxMB6ZTcZm_WFmj7wCrL9IrcTMQUwGqN2UL06TjgMefhtIJi5jUCOGblLkNTCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای مشاهده‌شده در نظرآباد آموزشی بود
🔴
درپی مشاهدهٔ یک هواپیما در آسمان نظرآباد البرز، مشخص شد این پرنده از نوع آموزشی فوق‌سبک و متعلق به فرودگاه پیام کرج بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152647" target="_blank">📅 15:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152646">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مرشایمر، نظریه‌پرداز روابط بین‌الملل:
این احتمال وجود دارد که عربستان و امارات، آمریکا را برای حمله به ایران تشویق کرده باشند؛ زیرا تصور می‌کردند می‌توان ضربه‌ای «ناک‌اوت‌کننده» به تهران وارد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152646" target="_blank">📅 15:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152645">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac89bffc3.mp4?token=XQN8WMkNtkNmTuXVkzY4ePPjX7eX98H_Li8Evi-021t6PpocnRW5fYjJ_pg6W0NnvK8wedxVy_YDKWTobbIxD6ZKrNt6fmLLuVHZU-XYixOO6A2U99Ge__rUwcQLT6r6SaPDoch_iK1MMWMSPIgMOK7aYRgsYpeNihGSN0f9h4KmbvIh4R8zYgUE0OGDpvs4wcJIDLEMRj_TgL8roxDdpX5CwejjNxaRATiHfbaUUnA6Sy13y-8ubjmxLbKB-jum48GTCc5my1WjBNaUKLGjURFQUKnY7GvngZeDMp8N9r-1fIL_Cm4aVnjjCo-L3CxHJTS7cpnrHsKrHRTd3XxEJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac89bffc3.mp4?token=XQN8WMkNtkNmTuXVkzY4ePPjX7eX98H_Li8Evi-021t6PpocnRW5fYjJ_pg6W0NnvK8wedxVy_YDKWTobbIxD6ZKrNt6fmLLuVHZU-XYixOO6A2U99Ge__rUwcQLT6r6SaPDoch_iK1MMWMSPIgMOK7aYRgsYpeNihGSN0f9h4KmbvIh4R8zYgUE0OGDpvs4wcJIDLEMRj_TgL8roxDdpX5CwejjNxaRATiHfbaUUnA6Sy13y-8ubjmxLbKB-jum48GTCc5my1WjBNaUKLGjURFQUKnY7GvngZeDMp8N9r-1fIL_Cm4aVnjjCo-L3CxHJTS7cpnrHsKrHRTd3XxEJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وای‌نت: انفجار و آتش‌سوزی در کارخانه اینتل در جنوب اسرائیل
🔴
در پی انفجار و آتش‌سوزی در کارخانه اینتل در جنوب اسرائیل، سه نفر زخمی شدند.
🔴
همچنین گزارش‌هایی درباره نشت مواد خطرناک منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152645" target="_blank">📅 15:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152644">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGPMSVeRC_2ZWTeB20A3W9_WbCavcU1ytvxR4fMSYHujQhJSncVZYhkyZ3Z0Zfa9Y1KHv6AmKJkMqKbGow1VpstDHPo3nPAfwMez4O9Y14nkwzs0VdQCVPzWNgblqjjm7XDW2ajt6Kyv7Ia-aixDET2ThtNUtvajclmRULDB0YWW8qfUpk3ZdyUDYDRw8aBDSeFazxbdcM8D6blQTFAJwJvukz0yJjv7lvK8T1LvxbiMLnSYAY9ja4Kw-JRZxovp4DK_h92qpN9Fz_rEHdmegGXyo1ZwLBpytP9VcJUIolBC-aJrHKhyqvapA3OXKSchTTh3zS87VDHc0ypzkZZ-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۳ هواپیمای ترابری نظامی آمریکایی، بریتانیایی و ایتالیایی به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/152644" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152643">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL0AXsby4XFvtpqe0HauIVITekOwApxEDxyj23FyeLz7Goe0riRYr7elg8TjbITEp_ZffmCq7iHRL_MveCCc9cr3FCopldI8jHdhT_7f_S2zUWUFWhLNK7Awr5BjkRQlGRGMxApyJoSO__x879xfviU-1G9WTs6za9FGjLb7gBYJzVYVyA-jUECudt7oUCy0xUEpUcH9CwIEym1ADuJhxO1U8RFstKT3RjLBCEt-j3AnNYD2HS9kNuInj8QDmvSOCZn3EnZxDuMQW2VnPxb3eXsioyigNNhR22bYIv6rLNUxqbdYukD2flXrSJya6J_8UDiJ6bUUG1fxv2WytsHlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/152643" target="_blank">📅 15:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152641">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VznUNT8PU-mQxHpOh_KhyRNC7m7qGgSLyndV5YDJtQkGreCtdfI2Z5Rr1RlyVIFM1X7MxnDSqeVE9YvJmPV8bUeUxcSHTLz_iSBzOWaedYVMwkef3gp3iqMfNp4WqZVCbk-3ANbcJHOmnjQqsZB4EDCntQuQR9ydptDtEq9oW43FQDYPBN7khZG5duXZ62VSaCCMVzqmUIXLv5qsmxmT6i0R0Xx8yvZwffkd34QosqpMNwqwtscijmtw-n7fWjv9XQcLu0IoukmKcUAIYjqaxyHCaW5UwTBnwD6l_oC5Qq0FGWnpHEZHBXyg9me2H4F3tcTZPpfbYUvsAk53coV13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGqAxShGndIsKyn-k8thWhhJaxzWrh5wvGYSyQbbBdBvTz-jnSJ5CaduMOvUl5pFSEr6TPAwt-dKn0Ex5xOqk1Fnrs-gp002LyH_KySn9TZJV2uNou9S17Kw48ekGixzUFlrPoJ9xLNKRcTRdk1ohJiz8w5KEzcdMWKzG-zXZ5YkS_79vCPfmH_XaK242SJIpT3mqa0RIcAitZRwWfS_EPW8Hj5yKTIUutZhRlvaTHvjrns_AQYh9GkKJ5x4jOI-ob6IVqQJ_4knDIF2Puw9WlQdW-I9_75P0-FEmItg5hDwtoaAnMzEo8kUr8hjeb-lOYmgbFlxkM8QwKPe6oYqAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از لحظهٔ برخورد کشتی کانتینربر با مین در مسیر تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152641" target="_blank">📅 15:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152640">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ترامپ در حال بررسی قطع اشتراک‌گذاری اطلاعات اطلاعاتی با اوکراین است.
🔴
یک مقام دولت آمریکا به رسانه سمافور گفت: «ترامپ واقعاً عصبانی است؛ ممکن است دستور این کار را صادر کند.»
🔴
این موضوع در کاخ سفید در حال بررسی است، اما جان رتکلیف، رئیس سیا، با آن مخالفت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152640" target="_blank">📅 15:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152639">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل : اگر حزب‌الله به ایران در حمله به اسرائیل بپیوندد، ضربه سختی دریافت خواهد کرد و زمین‌های بیشتری را در جنوب لبنان، به ویژه در مناطق النبطیه و لیطانی، از دست خواهد داد.
🔴
این مناطق به بخش پایدار امنیتی اسرائیل تبدیل خواهند شد. به ارتش اسرائیل دستور داده شده است تا برای یک عملیات زمینی آماده‌سازی شود
🔴
همچنین، محله الضاحیه در بیروت تخلیه خواهد شد و زیرساخت‌های آن تخریب خواهد شد. بیش از یک میلیون نفر از شیعیان به آوارگان داخلی در لبنان تبدیل خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/152639" target="_blank">📅 14:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152637">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCR0nmBNpH9WrCPlrcnhmC6hXB9jOTOXKfbJSBVzT5vdZDs5jpw2PY22uSk0q4jNMGPC9tRuE7iw3L3S_t9bf5gZx8bMRuYndZ0u3LXnpnEGMgc4u4KK3dFAppSPW2GdR_XUPttka7r3Fu3dockyxGj5KGPtNXZavccrxr7TifR9s73vGyUZqfTkK8k6ewuxXJsM6RUHiBZNB5yx7x75C6_BZ5dXGZCwAgQy7wj5IGX_ZXSmvFRT6nooTSEh0-C025ZkqPC7meSjmsi5siY2qW2qy1x4gjqL0IMX6G85_aGQZJ2d7tjBbaog_jUoI4HDpH_KMkNoncqwudCVjQ5aow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgHGu5aS_agIrtuY2EAXIuvp-_C8pnmjJ5oY84GzfjKdGGhQ1Et-AJcXnxBcOeouz83J4GzEOeJ46NtiO3GneqMXR0EzrSokiL2J5TtZYBC7wk6SfSkotLnqvzcU1qvKzfqdByJuYZ52AAItk7mz7_erPUHTBBPpdSRNePm_fdQ3Mp1gMfzDj48Xm9idon9Z4SVrhCT_Ly5qSzJgS9-8BhpGhD1tl8LMNiG9ThaT-N5NUeYvu9ZkqUxrC-btp5CgImY08PRN5rQLYCVyqqjnymhEbZtEfr-jv4vD25aQ4GA9aB3X6UjZPMp_jnJ46vlm7QUDyHZotBf4t0XV61Zngw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی فلاخن داوود در شمال اسرائیل مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/152637" target="_blank">📅 14:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152636">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز: مقر شرکت آرامکو در ظهران در حمله روز گذشته خسارات شدیدی دید و آتش به چندین طبقه سرایت کرد. به کارکنان دستور داده شد از خانه کار کنند و پس از این حمله، بخشی از فعالیت‌های شرکت به دفاتر آن در خارج از کشور منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152636" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152635">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
هاشمی، وزیر ارتباطات: در شورای‌عالی فضای مجازی مصوبه‌ای ۳۲ بندی را برای رفع فیلتر سکوها تصویب کرده‌ایم که باید اجرای آن پیگیری شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152635" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152634">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
آمیخای اشتاین، خبرنگار i24NEWS :  نتانیاهو، اعلام کرد که در مقطع کنونی و در آستانه انتخابات، با انجام حمله پیش‌دستانه علیه ایران مخالف است
🔴
نتانیاهو گفت: «از نظر من، اکنون زمان مناسبی برای ما نیست. من در تمام طول زندگی‌ام، همواره ملاحظات امنیتی را بالاتر از هر چیز دیگری قرار داده‌ام.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152634" target="_blank">📅 14:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152633">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی انگلیس: یک فروند کشتی کانتینربرهنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/152633" target="_blank">📅 14:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152632">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
ممکن است ۱۰۰ هکتار زمین را برای دو یا پنج سال در اختیار افغانستان قرار دهیم تا کالاهای خود را از طریق ایران ترانزیت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152632" target="_blank">📅 14:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152631">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نتانیاهو: نیروهای نیابتی ایران قصد دارند در روزهای آینده به اسرائیل حمله کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/152631" target="_blank">📅 14:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152630">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQMUu9wQJSpvkkt25Tvro-R4yJp7iiAG6O3iJ-FdKeNGjknVS0OI8mmUb1adrilmVzdsqaDLOENaG4G3l3z8MwhFKsILatFUhWDowpwi-hok6EkNGD952J8oTqMgKPET-txAnjhQUPda2J1BGloPKD33A7ZeUQWM3tEN8upGN1FZFEGjelK66eItZG0o9myMpXzbz7as5-2BnJ3T9R5vtzig1g9MZMD-kEFwYcZpgvfsj4ChkJPEQ0DIEvjqao8msySZqgBGDhud674XX5GQ0W3wDkFqL_104abUqbku2anuK1SdXFqCpvOnDCqiHBCUqalRntEmZoToCzhE_r2Zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله خاتمی: مسئله فلسطین به ما مربوط نیست و خودشون باید مشکلشون حل کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152630" target="_blank">📅 13:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152629">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0ZMCWT966E9epN-WWMDfPa41tt6Xiy_eK4Q2pdF56ayZRkoSoha-LVjjhQB4FQdGJG2XRBeSgxElc2dres9R4tiW4TteEEEMrXuwUO31MneNzEdQpHWlGGxZIZc7oj0b_CzLaTpI03l4cUM4uUlxvLJtnVY2i-kYQB8WCUd3KJZmMg3LUfdJN3yZFBTuqHMpSgaD4AmLwaIRlB_HWPheJu3OZQyhxUan2zVb5n2YRmHXP7ujVE5O-zL896maVLwjPBMaeKSfgDeKaw46lsXKp2RKl8YFL-qtjJlGX5a5eHzfD4BaNEoLBJM6oaFn-GnppXnJvykGfAFiJHzKP8_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعات شبانه برای رسایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152629" target="_blank">📅 13:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152628">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duA-X9L63n9w-DNYLzDO3xm66SQcJh6mFhYGfsPX4TDIYmea2hmYKjHYfqrqGNAO_9P7mJbxU9rQJBj-qQ2hlzrgcdKH5z_HAxQKiPfLrk5QCI1y0YRzmavBP5ngzzSFKkW33ZaALMDbMFiTput4FYZam-E6H973RLzWwcctorWcQ0bIfzlodmcw8hAbzc8N7C_92mVOCwKkYuEy6VMFQcOkXd3aVfcbCe038YzkR4Nl1YYVq8aDtWe8ZGIig2IOmWEW5-dUzSTMvi9GzFlMicoYJul_bXbosTYUsYiEdz6z5J2zD6d5pRHFDfuyx4fYDjuD06eW6_xuz3xYRZm1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر عراق وارد ریاض شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152628" target="_blank">📅 13:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152627">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
برخی رسانه‌ها از شنیده شدن صدای انفجار در استان سلیمانیه در شمال عراق خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152627" target="_blank">📅 13:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152626">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت خارجه روسیه: تاکنون هیچ درخواستی برای میانجیگری جهت حل و فصل مناقشه میان عربستان سعودی و حوثی‌ها دریافت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152626" target="_blank">📅 13:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152625">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فایننشال تایمز: محدودیت استارلینک عملیات اوکراین در خط مقدم را مختل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152625" target="_blank">📅 13:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152624">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سخنگوی سپاه: ایران آماده است تا به هرگونه تجاوز مجدد، با قدرتی بیش از هر زمان دیگری پاسخ دهد و این‌بار، پیامدهای آن برای آمریکا بسیار دردناک‌تر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/152624" target="_blank">📅 13:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مسئول بسیج خواهران شهرستان مهرستان در حمله مسلحانه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152623" target="_blank">📅 13:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152622">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PKrolojmBac4UPPfcX4K5J9WicOisgxGjRD0kl_ozUNzM79tvlrZt3S5Hz3HSCFn0zxxVi1jbLIf3_q4Afuu0h0y7cgJIknzNUYYdf-cNItREpzK1D-PoLTmJA-sZEJbLFh5DaetYqlvZeP_JyvLXaBTSt2Haz_D_ysHvJxr0uJp-f12TW-XtiJjTiIE95wR2AdOYiC5h-1AqvScubVtUONQbDFqzTXG-FiBTfikHSIKovo2wtIvw5I1hzxBechGggAfu7eAFtMPeCTIRxqxDIMlSAvfsVxhnMs5hrG3dMrWNCE7fHWS6Hzq9wnGtsiuCJHHKwcSM8nsBEfhm1dZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه اعلام کرد یک کشتی باری متخلف با ۲۵۰۰ کانتینر هنگام عبور  تنگه به مین برخورد کرده و در جنوب تنگه هرمز غرق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152622" target="_blank">📅 13:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152621">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPG3B4hkMcoR1fh-KWDeuIJQFAcztRenhdxxWC24O3C3FdnX-iWNR4hgXevEJ5W0ry2Mfv7gWdWbXBXZ2UJeqEQrsA2RKK_LjkWPPB2OpJTn5mbWL6I8j8X1hCBbml8FKql2wNVY19pZQjFAo6Zjg0nvvII-hAfwzt2S-qG7hebkg4lPVbYrR_GUBcp-8sx4kea-dzUdDp4JAd5Tc1-kHVDEgjF0ZlcUp5m3czreh3njhEpiW9_euH7VbQb3Mn4jvwkaP2nBFaCH-7Ix47J602hWb86HAO_ulvD4FadQ2XIe3uxsttNPYXnnVbl6frRySh2uUZe2K8JKv1d62cDS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت عجیب کارخانه برای ارزان‌ترین خودرو؛ پراید وانت یک میلیارد و دویست میلیون تومان!
🔴
قیمت جدید سایپا ۱۵۱ بادلاین پاششی با احتساب هزینه های جانبی ویژه مهر ماه  به شرح زیر است:
🔴
پراید وانت با کفی پاششی:  میلیارد تومان
🔴
قیمت قبل: ۹۴۷ میلیون تومان
🔴
میزان افزایش قیمت: ۲۶۵ میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/152621" target="_blank">📅 12:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152620">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
خبرگزاری مهر : ترور یکی از مسئولان بسیج وابسته به سپاه در سیستان و بلوچستان‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/152620" target="_blank">📅 12:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152619">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
هشدار امیر قطر به شهروندان این کشور: باید برای بدترین سناریوهای ممکن آماده باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152619" target="_blank">📅 12:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152617">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
هیمتی:  فروپاشی اقتصاد ایران توهمی بیش نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/152617" target="_blank">📅 12:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152616">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر خارجه پاکستان در دیدار با همتای عمانی: خواهان حمل و نقل آزادانه در تنگه هرمز و باب‌المندب هستیم
🔴
به نقش آفرینی برای کمک به صلح در منطقه ادامه می‌دهیم
🔴
لزوم خویشتن‌داری همه طرف‌ها در منطقه و بازگشت به دیپلماسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/152616" target="_blank">📅 12:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152615">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از داده‌های کشتیرانی و منابع: کشتی‌ها در تنگه هرمز با شدیدترین حملات از زمان آغاز جنگ روبه‌رو شده‌اند؛ وضعیتی که مالکان را به تجدیدنظر برای حمل محموله‌ها واداشته
🔴
ممکن است ایران در حال توسعه توانمندی‌های موشکی ضد کشتی خود باشد
🔴
در دو هفته، ۲۴ کشتی هدف حملات ایران قرار گرفتند
🔴
صادرات نفت از تنگه به شدت کاهش یافته
🔴
برخی کشتی‌ها به سمت بنادر آمریکا در خلیج مکزیک حرکت کرده‌اند تا در منطقه‌ای امن‌تر محموله بارگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/152615" target="_blank">📅 12:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152614">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnPTljafarhfDGVhqtahL1klZTIdyCzAz_qMtoyov0dG962V0LRWYH2UHObzjv_sfcumYf4hYwtanz5E_tZCUoYm-sws4k5zj3OVFOzmv_Yz8msCfZoyt-4Js2j-kYh8IYSNK2dEa1HdEnBI59cgNKDytA5oQDsqPudL7HBinjjWpICreyeArMyCN1hsJF3ChKlxuapkLmFwZHFvGtiDzZpxy03kPvjz1UEgjx2axYG4Z0cDb_DrJgaX60Bg3h4noWJpPBYsSx0E1qhUaT5v3d-qot8AAX2WMUjQum11oEmRblSn1Xt5Cw3RZcTlwqkGEfEiVy6RnfkgHlaSZRBLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاله نرگس، مجری برنامه کودک: میدونی چرا به ما میگن ارزشی؟
🔴
چون ما با ارزشیم و مخالفانمون بی ارزش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/152614" target="_blank">📅 12:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152613">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
بدر البوسعیدی، وزیر خارجه عمان، اعلام کرد نهایی شدن توافق با تهران درباره تنگه هرمز به نتایج مذاکرات آمریکا و ایران بستگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152613" target="_blank">📅 11:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152612">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRk3-9cv2EnfIb7xrV_JFnWbgDJORYjV9dV4qexInrIsoIhBXxNtdGQdz6bZSxqy2AJo7njwQrFOvuCN1lUifHKCXWqsI5PMABdgoJGoYJzzU54NUx1esbT4G7JshShXgfod38BklyRIbpwvkAbSqSX3bzXq7jcui7doFqxwUWqU4wffrBou9Bs37TMyOeAmJJvY7F3V4D2m0XNz_Jclpt_0Nr9byC_0sqEtq9B-SrBCHIp8ztLAx4sKLZnveJy_UapIFqI1WaogZAerqiVTP6DuoN-12YJFYy1DNpLDczhP59_zYAjThkWusN2ncMvzZ_rGnLFNNB8e4Y12FnVDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: باید مشکلمون با آمریکا حل بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152612" target="_blank">📅 11:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152611">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
آماده‌باش اسرائیل برای احتمال حمله غافلگیرانه تهران
🔴
رسانه‌های اسرائیلی فاش کردند که در پی افزایش نگرانی‌ها از تجدید تقابل نظامی احتمالی با ایران و احتمال اقدام پیش‌دستانه تهران برای غافلگیری تل‌آویو و وارد کردن ضربه نخست، سطح آماده‌باش در بدنه امنیتی اسرائیل به بالاترین حد خود رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/152611" target="_blank">📅 11:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152608">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihY6z1iir3Xi4_ZA_kPXSrNPjChZQ5M8B8UHtEe7BR9p7PzNdmtGh9BJdDTfTPvO_Y9FgqlZQVVTP3usWReVrNdUg7w6pSSfP7YemPf4MGzm1Kh7bojUAa0hAmwiuhN69lQA6K9jYjFr9e8F30-EQVOPi7IlK_k87TR2IcYIZJKBWDdv0hQCTrhl2rJqWORJYIZ2uGQMf_C-CVsQHBX9vvkuzPg7mysI_dHxDVV95LX4Vmrn5i44niieIJwM0heKlZj3mhm2SrHDRbmy4m85v2jl23c0eOFGuVYTQoLrX5haQKexikvjxtsHs76SWG7wwoQ9x6JFmCQuAGWx3Bp8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPmRQTu-Z6KxV98w9P4PhFVKo9IAnNW1bDrRD4tt8caFB_j5B58KZB9q0f2t5tFubHlx5H8_xhclBzT1kN7m4mWkks95_NJH_lRITeI8oURiARGeJB-OftD8GUhiqaWjIBZgajsEFFXXAiaXkkCDy-fqgjNu7M8WoFrGo8T59q2B86Mk0C5RhcJdNJJ2__oEdi5jjhLpwIkG6HYJppkjyGaRS_XYmUj4x03gCb3cAsLL2Dn8eWXEVC09iFhGeXIDr4RyET5LMV48gNENGlecz13579muhNBOuJrfRTKPhmu2uv1hnWezR91ZKdPZgn-_xfgMCtm7EiRWmD7PZmXXXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=nP8CP0wVNK8HjbHucBYrLfW60TYy1f1q95nT0H4G7HVu3R76sfkkU5OpvHPO-3A-6inlaiLZqrWwSK8xBXs6tN4dvKbeG2BNt4lNC73cEr9sERKJMc7oEVHPxYj5JvnJC_7jEdKGf3b8LZKa4tighAdrexHP_1aUoUrzs_errkDxyRZTZxD6NeMyHK3C2dYGQhk_QQAXveZDcSXrvjPqYoi511RYIOzLGokaJhJtqmutWldBzrJ-8RkI_DqPN4Mk4sdkczgfuRzSvCOzj_-1XIIDacilR6Z3ANFWYrNyiJeZ_jSLNMjikUSyeSiQOwE4j_McfTnCAb8R2hNwAIJ16A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=nP8CP0wVNK8HjbHucBYrLfW60TYy1f1q95nT0H4G7HVu3R76sfkkU5OpvHPO-3A-6inlaiLZqrWwSK8xBXs6tN4dvKbeG2BNt4lNC73cEr9sERKJMc7oEVHPxYj5JvnJC_7jEdKGf3b8LZKa4tighAdrexHP_1aUoUrzs_errkDxyRZTZxD6NeMyHK3C2dYGQhk_QQAXveZDcSXrvjPqYoi511RYIOzLGokaJhJtqmutWldBzrJ-8RkI_DqPN4Mk4sdkczgfuRzSvCOzj_-1XIIDacilR6Z3ANFWYrNyiJeZ_jSLNMjikUSyeSiQOwE4j_McfTnCAb8R2hNwAIJ16A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی کانتینری هدف قرارگرفته در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152608" target="_blank">📅 11:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152604">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
واتیکان : پاپ لئو چهاردهم به سرطان ریه مبتلا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152604" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e813e99f5.mp4?token=UZiiakJ4HHQhJRreJ84-YiK430mXlRXt_HGrJvjtC96UD9bY6AlXq9rp2bvshTarliBzYmMmObINXOE5sEVTyfcCp-fY9ej5BnKUxzmTITB6DZEeKzcaAvO45gCX-stB7wsZIriUxDGdJ7QAtrPfbIkoDf7QQDG40H8SEHbyzj97m5WSorJCKpNTa7nVh9vmr2Nfe1KPOEhI8jsmq26hokqgflWUjZUMMG4wcQNHi5dkSSe5sSZX5liSsbt-kXRdekj9-zIrCJnuzT-kII303xyUbX8CmdfN6PT7K5b8_qTwTDHqNI3HfzoVx2wmSkc52zVPZb-cMeG5nfDQV7cCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e813e99f5.mp4?token=UZiiakJ4HHQhJRreJ84-YiK430mXlRXt_HGrJvjtC96UD9bY6AlXq9rp2bvshTarliBzYmMmObINXOE5sEVTyfcCp-fY9ej5BnKUxzmTITB6DZEeKzcaAvO45gCX-stB7wsZIriUxDGdJ7QAtrPfbIkoDf7QQDG40H8SEHbyzj97m5WSorJCKpNTa7nVh9vmr2Nfe1KPOEhI8jsmq26hokqgflWUjZUMMG4wcQNHi5dkSSe5sSZX5liSsbt-kXRdekj9-zIrCJnuzT-kII303xyUbX8CmdfN6PT7K5b8_qTwTDHqNI3HfzoVx2wmSkc52zVPZb-cMeG5nfDQV7cCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم دود برخاسته از تاسیسات آرامکو در شهر جبیل در شرق عربستان طی حمله حوثی های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152603" target="_blank">📅 11:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
استانداری هرمزگان: تاکنون موردی از فوت سرنشینان لنج صیادی که صبح امروز مورد حملهٔ پهپاد ناشناس قرار گرفت، گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152602" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152601">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
هر لحظه احتمال جنگ و قطعی اینترنت هست
🔼
اگه میخوای همیشه وصل باشی میتونی از بات زیر یه سرویس تهیه کنی
👇
@VOXNET_BOT
@VOXNET_BOT
مورد اعتماد
✔️</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152601" target="_blank">📅 11:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152600">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2a0bfc52.mp4?token=bOdOhzY-jph3iCcEI9fU_optqxCO3dQEptcft7uUAWD4blK27cqpei7APoFUHoEho3q4qzGhlGbaLvmoknknK9qcVn5Cub9CuBUi7IEjXijEKYqRWkSNnRjZIkk4aLdf5DEXrgfxyFabGa9osbPcZrbdA61uoo0NW8mUy-Se_77gj9K9QhWA96uzKYT6RMoTy4gym1ziWK2ScRYsMavZdLPpnGKGwVBWncEIodTvApMCqu2DodJQAr9TAIOzpY3K83-di7D8MwjNf2KpQbsdw60haLmpHwuodZVo7IGxiq_ti2YPZZ3Ti-2Sk5JlkdnIK7S50u6MIKNR2jRpjhkdNJ5kJpA7_UqNHGBga74SSzpbMh_xsDgA7SrsAPfTvDQK2Fiy6gr4j6CTvTGixyX5k8VAdGV6XNlmZ37q2Jlro_sV1Kj-WiKcQk9U2-SE5YDO4OFTAIAM5K5_Z86LK7TCw7FmMzFx4xOqHjwyr3FUQwZ5nSAxSKaWRe42H3TRvZGBjlvOEwqMH39Yx82RwOrOQ3oty8_oU2-RpwCdz0if7cJy0d-C5C-26M5ypJvrOrnD64rRwIcnTd4SZHaJlnBdBiFr-2uYiyAXqvX61G_ZsRS2LHYgpxJrMatUXYvPucS44Hd4mQdW3T1LGwdnZyFUoKH7sm-dIET_UmeMGdkorc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2a0bfc52.mp4?token=bOdOhzY-jph3iCcEI9fU_optqxCO3dQEptcft7uUAWD4blK27cqpei7APoFUHoEho3q4qzGhlGbaLvmoknknK9qcVn5Cub9CuBUi7IEjXijEKYqRWkSNnRjZIkk4aLdf5DEXrgfxyFabGa9osbPcZrbdA61uoo0NW8mUy-Se_77gj9K9QhWA96uzKYT6RMoTy4gym1ziWK2ScRYsMavZdLPpnGKGwVBWncEIodTvApMCqu2DodJQAr9TAIOzpY3K83-di7D8MwjNf2KpQbsdw60haLmpHwuodZVo7IGxiq_ti2YPZZ3Ti-2Sk5JlkdnIK7S50u6MIKNR2jRpjhkdNJ5kJpA7_UqNHGBga74SSzpbMh_xsDgA7SrsAPfTvDQK2Fiy6gr4j6CTvTGixyX5k8VAdGV6XNlmZ37q2Jlro_sV1Kj-WiKcQk9U2-SE5YDO4OFTAIAM5K5_Z86LK7TCw7FmMzFx4xOqHjwyr3FUQwZ5nSAxSKaWRe42H3TRvZGBjlvOEwqMH39Yx82RwOrOQ3oty8_oU2-RpwCdz0if7cJy0d-C5C-26M5ypJvrOrnD64rRwIcnTd4SZHaJlnBdBiFr-2uYiyAXqvX61G_ZsRS2LHYgpxJrMatUXYvPucS44Hd4mQdW3T1LGwdnZyFUoKH7sm-dIET_UmeMGdkorc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خاتمی: مسئله فلسطین رو خود فلسطینی‌ها باید حل کنن و ما نباید به جای اونا دخالت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/152600" target="_blank">📅 11:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152599">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ترامپ ویدیوی سه‌هفته پیش رو بازنشر کرد: «مردم بزرگ و سربلند ایران، لحظه آزادی شما فرارسیده است».
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152599" target="_blank">📅 11:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152598">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام اسرائیلی: نتانیاهو گفته ترامپ بحث درباره احتمال حمله به ایران پیش از انتخابات را مطرح کرده، نه او
🔴
بر اساس این روایت، ترامپ از نتانیاهو پرسیده «آیا اسرائیل در این حمله مشارکت خواهد کرد یا خیر؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152598" target="_blank">📅 10:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152597">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭕️
فوری/صابرین :حمله آمریکا علیه قایق‌های ماهیگیری ایرانی در نزدیکی سیریک، در جنوب ایران.
🌎
@ForioNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/152597" target="_blank">📅 10:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152596">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نتانیاهو: ما اسرائیل را به قدرتمندترین قدرت در خاورمیانه و یکی از قدرتمندترین قدرت‌های جهان تبدیل کرده‌ایم
🔴
آنچه در کرانه باختری رخ داده یک معجزه است. یک معجزه.
🔴
آنچه قرار بود به یک دولت فلسطینی تبدیل شود، امروز به آن تبدیل نخواهد شد.
🔴
این اتفاق نخواهد…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/152596" target="_blank">📅 10:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152595">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روسیه شب گذشته و ۲۴ ساعت بعد از اعلام آتش بس ترامپ با موشک‌های بالستیک به تأسیسات انرژی CHPP-4 در کی‌یف، پایتخت اوکراین، حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152595" target="_blank">📅 10:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152594">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
نتانیاهو: ما اسرائیل را به قدرتمندترین قدرت در خاورمیانه و یکی از قدرتمندترین قدرت‌های جهان تبدیل کرده‌ایم
🔴
آنچه در کرانه باختری رخ داده یک معجزه است. یک معجزه.
🔴
آنچه قرار بود به یک دولت فلسطینی تبدیل شود، امروز به آن تبدیل نخواهد شد.
🔴
این اتفاق نخواهد افتاد زیرا ما اجازه نخواهیم داد.
🔴
تقریباً هیچ کشوری در خاورمیانه وجود ندارد که از ما کمک نخواهد.
🔴
و شما را شگفت‌زده می‌کنم: تقریباً هیچ کشور غربی وجود ندارد که از ما کمک نخواهد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/152594" target="_blank">📅 10:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152593">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55840225a.mp4?token=T72kYAdjvjdDC4NpCVEynzUDYfjlEoZ-UMb1zICeRB3LCQcpB-RKCQyvpQdVXhGhZwRaJcqxqFFZi5jJyDO20tsdlYZ605ydEsHLpLKcTUNrQAtYCMKtukAUxlnZVvz01Jo9VteNtqpNynukVojx7bRRWHLxKnXpQldutNygeLTg4nKbbn08h9J5zKTWsIKyY2Sjb8fvP56YgaxOkRTfGq4rttXIF_Wfx8Z9cHmpESjDshDSVZwzZOB4TXPsdid9ZYI31r3EuZ1NA1dt6JQTH4OG9rjbmEKXzpZzmyv8sIikiQ0yHpDxAgIpV0q13kkzJIR6UCCQ76erzVNWyOiCKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55840225a.mp4?token=T72kYAdjvjdDC4NpCVEynzUDYfjlEoZ-UMb1zICeRB3LCQcpB-RKCQyvpQdVXhGhZwRaJcqxqFFZi5jJyDO20tsdlYZ605ydEsHLpLKcTUNrQAtYCMKtukAUxlnZVvz01Jo9VteNtqpNynukVojx7bRRWHLxKnXpQldutNygeLTg4nKbbn08h9J5zKTWsIKyY2Sjb8fvP56YgaxOkRTfGq4rttXIF_Wfx8Z9cHmpESjDshDSVZwzZOB4TXPsdid9ZYI31r3EuZ1NA1dt6JQTH4OG9rjbmEKXzpZzmyv8sIikiQ0yHpDxAgIpV0q13kkzJIR6UCCQ76erzVNWyOiCKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش ترامپ به اعتراض حین سخنرانی اش: اوه به نظر می‌رسه با یک بچهٔ لوس طرفیم! نیروهای انتظامی حسابی حالش رو جا آوردند؛حالا باید با گریه به خونه برگرده و بره پیش پدر و مادرش که به من رای دادن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152593" target="_blank">📅 10:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152591">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf60973ff7.mp4?token=qLhIiyZVJH1ybd4DG54WgN6N-mstEs5jftHE0PYSc1EyMmAIBc0MTsAVaOCz03TyAlm4w4yb3qaJpRz0yxIrPxmu5Y1_kGtHoNC52DGW8r3N0Wx5EhDrKvRsaXE7slVS52kPlJtZF4MIxhpfmUrPaHWw7sUzd1Mb7hwbXfU-xKGm9ZiHIt6Oalxm1d3DqmMggZCY2TtTI8DY8Olbh2nLAb0CeHpe1H8idl6TvC86LvWuB22RMLOSA_tSxcAhMSTS5MMSM7UYdMqP7QmEDEdSFn71pj6iAqh31QEFN1AhTbApqToruEo-wTsVBYHSzu8G5dIyXE6Jwj7ZeKEzBBTV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf60973ff7.mp4?token=qLhIiyZVJH1ybd4DG54WgN6N-mstEs5jftHE0PYSc1EyMmAIBc0MTsAVaOCz03TyAlm4w4yb3qaJpRz0yxIrPxmu5Y1_kGtHoNC52DGW8r3N0Wx5EhDrKvRsaXE7slVS52kPlJtZF4MIxhpfmUrPaHWw7sUzd1Mb7hwbXfU-xKGm9ZiHIt6Oalxm1d3DqmMggZCY2TtTI8DY8Olbh2nLAb0CeHpe1H8idl6TvC86LvWuB22RMLOSA_tSxcAhMSTS5MMSM7UYdMqP7QmEDEdSFn71pj6iAqh31QEFN1AhTbApqToruEo-wTsVBYHSzu8G5dIyXE6Jwj7ZeKEzBBTV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️️️
👈
اعلام وضعیت قرمز در شیلی به دلیل طوفان و رعد و برق
🔴
طوفانی همراه با تگرگ و بادهای شدید، برق نزدیک ۴۰ هزار نفر را در استان سانتیاگو شیلی قطع کرد.
🔴
سازمان هواشناسی شیلی به دلیل این طوفان و رعد و برق شدید، وضعیت قرمز اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152591" target="_blank">📅 10:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152590">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
هم اکنون هدف قرار گرفتن یک پالایشگاه نفت متعلق به شرکت آرامکو در شهر جده عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152590" target="_blank">📅 10:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152589">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=Vi8q74PNUMhF1eWspBfSdyyMhltidei4hCrK65vkxnhENba__HDBtkWTLkUfXSYFubaSZf8w6W-9YoHZRrDSEtZFNYhqLo8L8z1rs_ysG_zK348LREkoUBVYwWutUg1wIdn_GXqp-C9OywAYCfwBlgVsa0az7meI2qhzKND-Q26J5JArhf4E4qs3EQTO-ZuJjavdBPJqZGl9JjKVyG2YgNfgQf5a1XMIYZ5wTwAxLEZOevTKkyHXZT3gGVgi1ZuFLZ3-9oK5Q-tSfUznrpfhRvm4nGvUh_IbuqkDxpRAiVWjKK-TS_Vs2BW-nK7wNYv6uBdpamHolqgdn1oV3LU1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=Vi8q74PNUMhF1eWspBfSdyyMhltidei4hCrK65vkxnhENba__HDBtkWTLkUfXSYFubaSZf8w6W-9YoHZRrDSEtZFNYhqLo8L8z1rs_ysG_zK348LREkoUBVYwWutUg1wIdn_GXqp-C9OywAYCfwBlgVsa0az7meI2qhzKND-Q26J5JArhf4E4qs3EQTO-ZuJjavdBPJqZGl9JjKVyG2YgNfgQf5a1XMIYZ5wTwAxLEZOevTKkyHXZT3gGVgi1ZuFLZ3-9oK5Q-tSfUznrpfhRvm4nGvUh_IbuqkDxpRAiVWjKK-TS_Vs2BW-nK7wNYv6uBdpamHolqgdn1oV3LU1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو نخست‌وزیر اسرائیل: حالا، این یک رژیم دیوانه‌وار جمهوری اسلامی است. تا زمانی که بر سرپا بماند، تلاش خواهد کرد تا بازسازی شود.
🔴
تلاش خواهد کرد برنامه هسته‌ای خود را دوباره احیا کند. تلاش خواهد کرد تا دوباره ما را ویران کند، حزب‌الله را بازسازی کند و حماس را بازسازی کند.
🔴
برای ویرانی این کل دستگاه، ما باید این رژیم را سرنگون کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/152589" target="_blank">📅 10:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152588">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قتل خونین کارمند فروشگاه هفت در تهران؛ خواستگار جواب رد را تاب نیاورد!
🔴
دختر جوانی که کارمند فروشگاه زنجیره‌ای هفت در محله دولت‌آباد تهران بود، مقابل دوربین‌های مداربسته یک بانک با ضربات چاقو به قتل رسید.
🔴
بررسی دوربین‌ها نشان داد خواستگار سابق دختر پس از مشاجره، با وارد کردن چند ضربه چاقو او را به قتل رسانده و فرار کرده است.
🔴
متهم که چندین بار با جواب منفی دختر روبه‌رو شده بود، پس از فرار به چابهار توسط کارآگاهان پلیس آگاهی دستگیر شد و به قتل اعتراف کرد.
🔴
تحقیقات درباره انگیزه دقیق این جنایت ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/152588" target="_blank">📅 09:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152587">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
هم اکنون هدف قرار گرفتن یک پالایشگاه نفت متعلق به شرکت آرامکو در شهر جده عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152587" target="_blank">📅 09:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152586">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وال استریت ژورنال: انصارالله با استفاده از قطعات وارداتی از چین، در حال ساخت موشک‌های بالستیک میان‌برد پیشرفته است
🔴
این گروه قطعات تخصصی جهت ساخت نسخه‌ای از موشک ایرانی «خیبرشکن» را وارد کرده
🔴
شرکت‌های چینی به بزرگ‌ترین منبع تأمین محموله‌های رهگیری‌ شده‌ برای انصارالله تبدیل شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/152586" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152585">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
عربستان: زخمی شدن ۴ نفر در ریاض بر اثر بقایای موشک‌های رهگیری شده توسط پدافند هوایی
🔴
خسارات مادی جزئی به ۱۵ خانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152585" target="_blank">📅 09:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152584">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b835bc2e1c.mp4?token=ChMgYMRSFVBRiLKVwk3bVgLoD2R7NJVNU1QWv1vBsn6VEUfN7xmVJykUzojGojZeNQ8c027uBW7fOzUPdT3xUE0_3GdB4U6jkq_rE3Qr9I1Qf9lSYus7-BrC341Bz27kv-D-0tHVJZHif7dzaZOGTyz5UebWL86ANGMp4q3WTSYHqnXU2GyVlpXfUrP3T51lZdvgSH56I74ES0XQfxtoUGTNB07EaPx84x5L71tsFW5Ti1WnOnaybNDrJLyGWcrMbaustNv16XfdX8iX33dvPtp3P-oWaYl4tIf4RliePXtOvKsZ_d5POwKZJj-ITG1WyGOOh87YKPp2aw5J6z3ZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b835bc2e1c.mp4?token=ChMgYMRSFVBRiLKVwk3bVgLoD2R7NJVNU1QWv1vBsn6VEUfN7xmVJykUzojGojZeNQ8c027uBW7fOzUPdT3xUE0_3GdB4U6jkq_rE3Qr9I1Qf9lSYus7-BrC341Bz27kv-D-0tHVJZHif7dzaZOGTyz5UebWL86ANGMp4q3WTSYHqnXU2GyVlpXfUrP3T51lZdvgSH56I74ES0XQfxtoUGTNB07EaPx84x5L71tsFW5Ti1WnOnaybNDrJLyGWcrMbaustNv16XfdX8iX33dvPtp3P-oWaYl4tIf4RliePXtOvKsZ_d5POwKZJj-ITG1WyGOOh87YKPp2aw5J6z3ZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل ناگهانی در منطقه گورخا، نپال، خانه‌ها و پل‌ها را با خود برده است
🔴
پنج نفر مفقود شده‌اند، در حالی که صدها نفر به سلامت نجات یافته‌اند. عملیات نجات و بشردوستانه ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/152584" target="_blank">📅 09:28 · 22 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
