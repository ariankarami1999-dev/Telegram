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
<img src="https://cdn4.telesco.pe/file/Urx7n8UWhVMfZoJwOgc_v5teOhSn6CsOE07iV0gXBPUDTHYLWJX_ZUetCqltDU9VgrEBrtWu5SRfoGNVqGZfRnrZ5iBLLIcjPmYNPamFCu9XtnM2XgqokC1luBD-ya4atwGc9Hv1_QOFn-NB0lsRrzGVadVlErQmMwPPMGWNICHbkpfq_bgAz0p5_r6tBXfdz5qC6jvK-_Uiqve79MdiO7_LI3AESVvMqfqFYr-xUk5cx8YoPQRKd9N8ZLS3BzWIl2Y82kd1lsRzFnfZK5WW_0dS__mPLR5aRXdzaCqdOSamGfrt47UMjunl501yYriktjtC7rjqcxh9MtB7sISsrA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 586K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOZiKJnovxWfeqhV8WMUPUW3y6hvF4ov5_fpX-vBsoqkcJe1d95w9AbLTmJLCg5c3sLoByAIvBXzYW7z7RO6VGXk3_-Rc8DiPcmdmTVfri-cV4k1CdRLkwtbJkM1wRU-WEkTDrn6CqqpE5OfHZnT_ikbS6igwIwdlohmD4H1awm28HgFHpw7DiHpwBuZB5P9OZebB-3oywxH2fCHhdWCBzOFmfVrQsPXWNUQE7NmXojblxvYBaOOBubXV-nPn9ekJ8J8ZtDdzgpOcA87KVn3JTtw_RwTS3NxICdr45GxKOUVGP0ihLuRGi0kta0FH5qqhT2elZBG1ENrp6pk76NNZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jX1bmDak7KBbDC-pWi7072iOwHXYlDHRU3IwmhaWweC26s7c25cZgjva-rEIRw2puIRyi9Oa5jXVrD2a14wGkefq0h91HAsDbxquSZLIDq9j9O1y4SmMkbNIr1AJ0h6ON7tn0W08jDrR-1xnPZWbJzj0FNoxlYLUOQXRyQzyq_KTSadjMoI1gyooCsjyNhplzGRGnA652sLoKfncbVsC8IGnCSIAoXyTLxzYnvrNSvC-cbdJj24AZ48dw2ZQfeo24iAU1-P4hRYVWkVLYm4j6akCuZPb8OaN9dvx0ZCTPsX9oGgZTeDKi6sumQZ6bdw33PUGtjzDRSkqDGBd8TiytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zg1TfS2_X37UlrwQoOyEXG5Lz6t0Mo2u-kIDPztvgxoyX3i2cs5Vf9svM-AFpCUPr0-iPjRNuNo5yzxtCTzH3c5oY2eA8SIanAauV35be0f8A-Snv5U_BUttMieecC5s2dC4DoD9Fm0Jwze-l6p5YzGtT6V2H10vTxpQf1VMIpQYiOOFw6XTL2sLV6oU3XBDbHYxpvIYVBzuM63yuLHArgmsyffTzEThhRlnX1ZPqnDeN80JStXMCSF1sXlU55U5U3bzV3lqIR5PZpxiV_ZkOUiV00MCiHZELfs5cQrs4DwbiRQ2eU2ZfSosN2mkKU_Ak42J_dNkylpwuUBtFX1jDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTKQAEesqIrI-QSv93cNyh-pFn8sLYbkhJ8T9c-HmjihNWCQK5tzT8gb5oKmBe5BQPu8bAL0H3u1K75RWvkFF_ynw6pv9IDxm3rgMkTBEjl_pOHKWEmLwXwEKBzOxuEGisXwyx7QdlrPeBWJ7OA1CPuGoKswn4hM-TrbgmxDCAFQEe42_VfyL36Q-1-3UMZqrA8rbbG6YDODzyYLGKVaoJSqvSxI9iZbOLFhwaW2uKM0PeMmLJGvSFozkiBpAvfoC0lcw4jcStsfF7ISnbtCqL4TVh7fSzfN4v6__SoFFzPyt9zpunCUf-gUfFXHO8LtuKbv4Gw8mUArIgjU52YRq0Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTKQAEesqIrI-QSv93cNyh-pFn8sLYbkhJ8T9c-HmjihNWCQK5tzT8gb5oKmBe5BQPu8bAL0H3u1K75RWvkFF_ynw6pv9IDxm3rgMkTBEjl_pOHKWEmLwXwEKBzOxuEGisXwyx7QdlrPeBWJ7OA1CPuGoKswn4hM-TrbgmxDCAFQEe42_VfyL36Q-1-3UMZqrA8rbbG6YDODzyYLGKVaoJSqvSxI9iZbOLFhwaW2uKM0PeMmLJGvSFozkiBpAvfoC0lcw4jcStsfF7ISnbtCqL4TVh7fSzfN4v6__SoFFzPyt9zpunCUf-gUfFXHO8LtuKbv4Gw8mUArIgjU52YRq0Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29232">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e15DdND2eGL7Lk_VkwazpS81x6dtWIFHwwTEwumyHMm_RAZAqf-Ah3lW5r0rIdqohZ0XL9QBTU2iizjCC1BuEpY1wm73vDnbcZynn3OmS1CphxdoiZ9EM9lZhe3cpWEsYTeh0q_oQhH2GF27V_LExiVr2l_nC3YKZ2kxnBZhR7JQAC_XJzskuz_UU4q02H7mM5BLi6XB-4C7ZKCoQOJXajwyCK1wUzhxP530v6355IJHnFToGmwggB5jO82VmTivmPWyUnWErUuFf83piMjZpNxzf_Ue_xhYjpCH6QQL1g29-tvD46tBx5YqZmyJCc-rcx1kY7U0NBEFDLTr6PwrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
پرسپولیس
🆚
ذوب آهن
🟢
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/29232" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3RTz5WxX5zol0P34WZ-pH2QtrUVyZfv0XQIT9HH1CUh9nrQjSdvl1oCS_KAE4pmy3lp_BnAh2c2gdFaYp9VF7pwV3goA9dzofKMS4ZmxqGl1VTzO0S_IsCZ0iOyVXNxvK_I7YwixvpQfXS6rxKhy8yqrCXUjWBeSd5o_SpRLgDVbVZ125QjGW-KCYz5qwE7Kjnl0KcjoL5wS2dzGn7WrAbitLELC4B9AQlyM3T1v-YzIJqx5PUMR3t6OGFk1f5Fx2DB5lIMqUB1HQDkNCk_OcWGf3Kto_eVhXlBuWxl9Ka_Dg93boXmlAZHKPpOwkn7BCgPfIrp4aoehUpXdimcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSxpTk3c-tXQ5GkeE4nswxIYNXrD8-wjzV0ny67pnUgyVINWsmaPJn-L8IpJEvdbcHxYPaupdLzRp7BKtIl8ouMJDVxN6zax6CqNy-WuaKVll_pqVTVi1rkARqgr-tdvh-bpehSS8OehEAZTmqemYcYkPi6zJbYa7yy1wliwZwRxwh4wV3I0AnpTsvje9gpAUXnowbDph7dNseZ9ikSIXK8MXULy6J626nSkDyGawViwz2H3iPA6LLcIPEXguv3Tz1755WMOvI7JF9y69QDQqVMuC_nGaI1trvz3NtmRNXzsmgTOEZjV3UTKxIby11MpqXd0ojAsAiPWFLvCh_5dzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LysngS0pVBxwzDapt0kkJNnpFtJqF7wk8KWpvTT4rzUvEut8FNRcMX78dY_8VbymclS1vWoGoFL7FtXyKV5hbYTqVvfUVnXzSR7kvMHPYpVwqznCdyGT1dTg3pTLvn8UNwTEhGt4WB4kBt_Wjr48dyhUCSbbnCRBX2ONXHqP5gOGO7ED759tirpeD8J7iUc5bCvSLGPkb45veMHgfj8Y41BUip1I_yibXLXdjsAu1xzwNKniuzOnuc3py4LwvT21l8wF0RnspeGy1NNpbBEvTAW3dkGJsnh_VRgARe8T4qvLSMqM8E51h6NlAXQVmhm37qPDxRuDIHkRuQTlifQ94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/29229" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29228">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LN7HTglgwp1zqS0Mrb7VFbyEtF3n6jpEP5QN1MrJN7HaKYsO6aK4_xvBbyCeOchPy0mcj-AJeUO0ZCJATvRKumMlMnOwYGeUuo02tbExSdHJBxAXD87KLvXn1t1wb2s29OUqq9qNlaR2s9fKnX2o-ksNZ4OwpzTDmiHNHyL7Br4ieMFTuQAD42tuUkP4-KSItF095ENi09GiYOa_kbH7iNqDm_G-45qLR2-xVv46aINDhhnttfIZqI_CHlvUB5py1-Y7kP6rMns0DovB_Mruc1urFS1q7OINt5k8wEHVZmHZpTAZp4q8yUbqU3R-RoshqJAuGT2n5T-IcYB5p_t_vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
آخرین برد ذوب‌آهن‌مقابل‌پرسپولیس به هفته ۲۸ لیگ ۱۹ برمی‌گردد و این تیم در ۱۹ بازی قبلی خود با سرخپوشان تنها ۲ بار پیروز شده. از آخرین پیروزی عبدالله ویسی برابر پرسپولیس هم ۱۱ سال می‌گذرد و این سرمربی با ۱۱شکست‌مقابل‌پرسپولیس در لیگ برتر از هیچ تیمی به این…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/29228" target="_blank">📅 12:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/29226" target="_blank">📅 11:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNkHjwA_RQY3_3vRdsgNIMwQ2SJywpwoSzbKwUFkyKpFiobA2y1Vy6plnKo7I2ASA-AmrSZ4i_wFVFW-9dB3GxHWiN7xYqD-1lkI4Hv3WhHUOy4q5g9qGB52vGyB3Ue34SIsRTCxb9Z_0l5cUbK-5CBFPySSsxwOQWfXwdpIQM6HLB2jIeEoGtbnycxRbrfJkLRGlP-_lOZBX5PFpxDIshsoxWiJIrQBtJA6xy3jnzM3DYgsjjvCgk_cg0AvQ_3H1kwZM_fwJnYGq8dItcIHNoocOeempvB7a9aIxGvDtCaCF_mthFaKEnG5YsSn4iWW1fEVI_C_Bu5yTxxuux51tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خب‌رسمی‌شد؛ ازساعت 12 فرداشب به بعد بنزین لیتری 10 هزار تومان به مردم فروخته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/29225" target="_blank">📅 11:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvAHNna7DDgzKI_xsan7UvYn9SJ6ywgjz4uV-16hKXtaoQHlGPH4k6NQz4NtIlpomgyIi1PqmZI1deN4q73mZA0D8FYFAAnQ-ISER_JB_iEcPPbZBRSwsGtGbbedul5nn5Eb9vD6KLuJVxgbXyvkXNAaaZ9UzBFpt1HyjXqgdcPv-xIX3FMbIv1zMxI-Wlgm3w-7Y6Pi0xPt84fOUGJqmI8eF7s5MSXgyr8FhkKQXVYiW6df3UWsGVaAKcftkuZkDLDLeobE2-o4KhmmUJ5ISk5errFX15MsN7wzcno0XRrNgbLSc9vbX2fDNRY_Ng3WaPgr2AaWuw2Ixyn_P2ZmCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌بازیکنان‌حال‌حاضر فوتبال جهان بر اساس جدیدترین‌آپدیت سایت ترانسفر مارکت. لامین یامال و ارلینگ هالند همچنان با ارزشمندترینند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/29224" target="_blank">📅 11:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axyBqgkdrHKZj-DIH76jkrPoiHJxoLlhUTTO_nrJx2QikC59hfLQ6JnNlRTsL8iKWILUojHwQogy-Yx2JxxFIqcOQq2va8AsHM8QGuLLzE-57Gh3aMLeK507Dip5hgMHRpjEXYineXIqNaJ4JOKldRHdH1-uQR_6kThbFvCJ_3fK1qrVuSnadQCOF7Z8yeS41GwkUu2Q4O7CUagNLpz9ErRul4a9GEpQOOHgD0QTsXnb4grTMyyogMxwpn9zKHox5Bc60M_s77Ao9Myzmk6cONNb8OvP8JjWAM8snhBwrXVK3yaA401kxRcL5EqwIDgbQs3NlbpDeBtsXl5HkdXfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اردوی تیم‌ملی امید به دلیل کمبود بازیکن لغو شد و شهرآبادی، لطیفی‌فر و ایری سه بازیکن پرسپولیس، محبی بازیکن خیبر و صحرایی بازیکن گل گهر که تنها نفرات حاضر در اردو بودند به تیم‌های خود بازگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/29223" target="_blank">📅 10:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpa3xc_Csht9mJk8VBt4xQG7xJ88PwFHVGMGXRgbq3pOeUJXd74Sj1CeSjgUP5e7RNzgFC9w96erD1gGCrAD9bGvwMoBfLeGkODmlwqs3Q-9weufG6Yv8cfKgCxSYCQG3iPLqLU-BouhWYCBnTLV7nTmquaVN6Fr7gq1oYyEU3XNQBCa3J48S5wnTxe6EXXFSyonusHF4PCDEnlTAf-9CWQFg-5ozuT4lguq583BlnojCBZbfLk1ZwWZbCSSTfH2PVdS1Kv39zsHYNGUoM5cN5Eqf0gLa6kDvC1R8fYAHkxbcv6r9OG16wUTF-kL7m8XPFj5wFQpCbVY20EsMeqtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/29222" target="_blank">📅 10:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ac1rlSb2LbTgLIMwQqJFUYp1_u11puGbA285tqegTFjCNJjFDH19_TpViZd_Fu-OvjtvVOlEsJr31l_wX2RSDNmU8brVv-pqGjNaqKgvacyczDwD8wElVle0EyDme5iBbRFamNkmA-JIJ9Yq2a5XI8KpJbkQVz2uGvdZ8NZrEeoqLXNDvwoe4U3GxEPNFn3SfvQdkFjViyVqY2AjI_gsGwmNNpxjdrOIRZVof60ZDsvBTaWgM2XQUnNEVu6wxgbrLlLf9spV5b93WzcCLlE5wuiCB6tUd2NjVVLzrIqLvbZi57tPTmGk8_DCNdWftmXcSCKvGtyza8s65xPTrhR8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29221" target="_blank">📅 00:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEbvW5Tg3RL08lI3JILcxY8fHMIlYEmGe8_WN_XG0_scekRyZiWcX2yru5r2ruuv5i2fUBzr85varHstG-pW5-qkd7ARhCWMdsm5_Ok8VM0Qwn0PvlIW74WT2uBMNFwAffs1BG7Uums21QNPYreN_Q_BVvdd0EO1ThZ63JnGwbLkR_VlsOnyyvhZs_8QSigVaeohLpZZqtlZ_RyH9Fd7B-yEXKZZNGHB3ui9_xoglxx1MZcWYE1jrZurVEGKE5l2Jn4pZhjpv5OeaFW1b4tdGH9xTBWZPDIByzYQFkivANOVhpEgZTyZBlP1XNks3HG_y7NkUIGH0wZarqtiZgieag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛مصاف‌شاگردان‌مهدی تارتار با گاندوها برای باقی‌ماندن در کورس صدرنشینی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29220" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpIumgk_lEkRYF4n1ggV8sF_CwwXfD5F8sVBk-lHQivaUxNn0KjWFMzRlaRU68kpR-aJ_kmCQP82Qp6lSmGqakPdBUag_1aNeT9SGM6oBZRczmOs476F9wLD5LKsYCesazrYDVH8B10O1qIyuRGERCQRkRA7AeNFlFIM3o7VYbQqJTXIbfFNW8MDDYtncsHBarKFjmA9W1ayiQB10sANoh0NeJdlV3rSZA094JyqH08kIk0nKTZidZnMgGNTXZ7xel-QtYwuA0bXcORyB6sOopOGGEVhYEEzXvWdRYs-kNFDwWTK1MSMjOoDYY_mUIhu23nELnvJ99DVGQ3RIINcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
توقف‌آبی‌ها درشب درخشان خلیفه و شکست‌ناپذیری‌ادامه‌دار آرسنال دردربی‌لندن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29219" target="_blank">📅 00:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6Sc4Rij1Uqus6FFxOV9wqNdJ9MGvrxPqLrnjsLoK_xYWQyenQY-hXPbcTSvotYAli8dlyGCF6B1pr2hMG2qfid-9ZjgjeYhlAr4yGr_Bm_zDoJys51rjFrteZG0CBKLsYKSCPllW0ygnKhg5J9Y1uGWt16gU_CYNPw2rherDALdkuNCh1xVnPfZ-m-ZFRxeb8R_jnK6D1GYjZNwxyvP9yrep1dhF7p0-YKAt6mK3C8BJFi5JGKCI_AsC3twwJEvdSN8-m_WX-R6WD4wiy5PDeNum5Z82IWUZgv_tamWgwZjWKi8TD3pp6x_zoiBId0hypdwO9LCd2Oe6jNFBOonyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
بعداز نمایش نچندان دلچسب در بازی اول؛ محمد صلاح ستاره‌مصری‌ترابزون‌اسپور شب گذشته دوگل‌خوشکل‌برای‌این تیم زد و سه امتیاز رو گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29218" target="_blank">📅 00:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMsnzL6C5nTyQZECobDyQaGbVo1KgamWeu0T3DMj46DpgzHNimpXiqFpAmOtTrKU4_MW7T2ZuuhsoYU1s8SbrpivHZj6R1n5xmKru9IK1fD8-8Tep2tTi79Tx_blA-QFpr0xcE_NhXez3CHIUzf85qPskBznwWdqcob3GT8ei9YoxbcWnMvtFx7et-1mQBBi8hlfyPipEvObfMLPnwwuA-o8KJCHBldHpIIbPoJa37G5ODWXIwRdPbFbymI1DfPtHaoz1DDar0wsG5Vo1Tbd2UbuEY5TsAGlmiOuwnnNu_Qv5H4uCmMX8md8tIno9441Tec-TRzI2vO0TFUvLM33hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌‌سوم سری‌آ
؛ شاگردان آموریم در واپسین دقایق بازی گل‌مساوی رو از بیانکونری خوردند و سه امتیاز شیرین بازی رو با یک امتیاز عوض کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29217" target="_blank">📅 00:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGlBVEpb-ll8KApmJ6B9oUqURvTXxCB60U1zDW3NouoLkW8E6rRglyUvpGX2cc9V9TI6fYuauwzXhKcDHb3a7PYWjQVz--2No2P1do0X9DIEBloCRpQKwMa7HqAKlkQ66s8dbSfDnS_UAYBGfRPk_INABoBULYcJL-ylqwZMwGV7Bcarci-nIjXOmiZqHQrUOTgpm2dxlsOKjQkHb_OFrOLpHL2DEzIcF1CLnsJ4PXfJ0cRFtcKVPzKaQjajTcIFKr6DwlLsTxg3qTL_i3_6U0kIfiXuftvkLgo2M8quUjowgyGz28Cl6JX4biXoKqOwhi81LUdAC8Po0u3TY0dhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسابقات لالیگا برای بارسلونا به یه جلسه تمرینی شده! ۱۷ گلزده در ۴ بازی‌واقعیه پلی استیشن نیست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29216" target="_blank">📅 23:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=jWsvmu-rxZGgsKOJ1gDxjA8OunaF04pGjuTuimM30WCDpwx5lSOp0PYOleQk2p3lFtfvMdmI7M2f4adMEhS-D3MlLRq8j6ra8SSfHCMj5CIjW5N2nZ77aO2plLKj5DjJNns8u5tXeJ_i8PujhsxkfdrGh7zHslQOda3sCw_2evRiIoQHHCOSZYxCCbofnjTUWVACcVMviRjWpQJQ4At6etmRFJeMy2pQHh9DmS_6C1PnEolf-m1e2bU6TfQoTAYuc6XIrtHjzcNn1Xjmlb6Buiwax9qsCsBHPBYFDk5reolTEG6mH3UztY7oNAsC-vkvKjaFmpDLJ4JEKIQrZQhq2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac032e583c.mp4?token=jWsvmu-rxZGgsKOJ1gDxjA8OunaF04pGjuTuimM30WCDpwx5lSOp0PYOleQk2p3lFtfvMdmI7M2f4adMEhS-D3MlLRq8j6ra8SSfHCMj5CIjW5N2nZ77aO2plLKj5DjJNns8u5tXeJ_i8PujhsxkfdrGh7zHslQOda3sCw_2evRiIoQHHCOSZYxCCbofnjTUWVACcVMviRjWpQJQ4At6etmRFJeMy2pQHh9DmS_6C1PnEolf-m1e2bU6TfQoTAYuc6XIrtHjzcNn1Xjmlb6Buiwax9qsCsBHPBYFDk5reolTEG6mH3UztY7oNAsC-vkvKjaFmpDLJ4JEKIQrZQhq2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علی آقا دایی هم عصبی کردین؛ واکنش اسطوره فوتبال ایران درباره درگیری خداداد و امید عالیشاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29215" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdJHn7v0jodbQeBCSkOPCydd_zoWLVMvcjv1nehojkjATdSnrdtQgyDSDXsQZGB7D7YX-O90ZsNb3BWiN1vjkONI3GXrgVkcFlqliZVCbdEGSR3g34gd9LRs8mToJOsr22tQ6zRERZcXuGzawO5V-971s4scoqVGsKkkj8mEe34G1tGzMSQ6pP7-InrfQdCBxRO6feWAhuaVlmE2F3IZMT998uHZ9JZINkxiY8jUMSw9zsh8uD7suj0AwPHk0YXV3AIlPbiHa4tjK_Tkxy6bzZOlScWQUpp5P7_izf-PttYobCEsZHfrObnrhjmKa-vI1Cpd5NHg8-pLCfH0-A8oJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیروزقربانی‌سرمربی‌آلومینیوم: کاری به توافقات بین دو باشگاه ندارم و اجازه نمیدم خلیفه و گودرزی دوتا از بهترین‌های لیگ نیم‌فصل از تیم ما جدا بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29214" target="_blank">📅 23:19 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4nZeoNcjIsnfTx3STBsD95e0FVoZSxznc9HNkTIjrCjHju0Sff2yrQ6jToHwcSvXrobxNdrcwEIRMiA0cLI_bFBj7LtaTE31YEmlfiJ6zxBypj9iRY-Z0oXQ72TEa11sWhWQrc5G3MHP8GBgpr6pEZROrRbVigGG9IbMhQmKrPX24sNroDBcNRkq1ufM8L8cMw3xpsGYl8c06-0G7G4Ec8izSMje5Xgvf7WbMKnNpS6s1y11Qq4M2Bp42B4d7mx4WLsGWRPy0cMJS8nDWQP0t5-Gb3rjmy_8LJN-7__LaqstWJU6doU34CK6YGiV9e2P-V1UgxjB4YIKo7f0UKvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29213" target="_blank">📅 23:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=MUq5q0XeHF-hWXm_v5RzeFpg9M9PymIa7C53f3mHQPAuKxOFlwkzvUdCQMyq39kmL5kaXhpCczm2QK1jOsuWHEGG5HqoAN9FYiUdIT1LqEicpVu8kgiG7Ci_TpweL3CbA5yC0OXZySSy74WuKW6mNMXKDmajKCaLsZuI4JpQdd3SisMWt8QJlPP76pFDWWfQgXJ58q271Fo_R_nOgbAQI-xojFAVuWMDV9VPDsc2MH43JxhEcYJ_D0pAGKBy8XSkKXj3_ScLP3H0wkIbY9TLP5t1J5J8SdNpkeOxlq2A3FAK7uDd51OdQ78eZ3GQzlh3RMoGMw7kgNRNGLwGmH3D2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c32a03f776.mp4?token=MUq5q0XeHF-hWXm_v5RzeFpg9M9PymIa7C53f3mHQPAuKxOFlwkzvUdCQMyq39kmL5kaXhpCczm2QK1jOsuWHEGG5HqoAN9FYiUdIT1LqEicpVu8kgiG7Ci_TpweL3CbA5yC0OXZySSy74WuKW6mNMXKDmajKCaLsZuI4JpQdd3SisMWt8QJlPP76pFDWWfQgXJ58q271Fo_R_nOgbAQI-xojFAVuWMDV9VPDsc2MH43JxhEcYJ_D0pAGKBy8XSkKXj3_ScLP3H0wkIbY9TLP5t1J5J8SdNpkeOxlq2A3FAK7uDd51OdQ78eZ3GQzlh3RMoGMw7kgNRNGLwGmH3D2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی‌لیگ‌برتر درپایان دیدارهای امروز؛ سپاهان با همون تک گل لیموچی سه امتیاز خانگی تقابل با آبی‌های خوزستانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29212" target="_blank">📅 22:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6Le4QOBeAoi6qXy4ZYg30NpkoebFuJ8Lt1Ocx3olaFQjegyjY7sTF5sSa_JEEyCpvlLXISxqYHvG1wi-pCmjvCHP3GFPpby-QboT_fhweQvvEQSdaMV1mCe-1LVmE0CCyzKJr12SPy3-cfoyAT-o1f6UbW2QHD-Ew6xlKiNt8fWIoIXqTkfEY5b-Ye_Fn3pdi_yWOBZsbiPR8YvooH6Xk1ug1pM_1X3tq_--4LN4mqXL6x0KjQ4nnr-nC0BfgECsGN8i28qihZ6_jK1Mw3fW_IZZCWYRgAcKq7HjwTTM_EYZ_hPzBAl8Dp85Dyc1TM1JszrlTDmbj0wxwA2BjXOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29211" target="_blank">📅 22:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uv94aotyjbQ6hsDuasZx8r4Yb2vH0kA04ioO__cjngrZ1tpTdEg4BlRC3hSGZmLLm5h0ixDvAlIlmFPEKu-ieE4AABORk-YYj30XzHtd7EzaCRd2x3LDguzTJAegwJhq2LL46DyixAZEJYYTqq-AGhE4nT2GrrCbaXY-tNz58TpfgJcqXWGvVBs7m3fyWRreWi8ih9K4Tc5bRTcqgUsPhM3RmeIZg3n7tm2xwqHH-eVpovqVBlSqtjHVOa99E9g38vcTwwrmpR3N_vIVC4bedrL9DSvjyQ0CNqcGZmeRlY9wrNdCTwUJmwhBgmY3-xn3PNgDy_qrco_oerQAgM11xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29209" target="_blank">📅 21:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=qM6frFOb-iQDEDJ8LTOgwAXHzvEQcSBGf8SD3GUy6mOAu3JwBXZp5ZAL5UHqBTu4DoLHoO6HJ4L0tlPGxNesWfALRTp5I_fsVo0IjwA7B9KqIqVda2gYPAZRDJHxa_hRtxJBZCSYodUnuWo1q1R1raEPWlRkCAaVx-7zx9cdHy7dBUO2m5IBuqmXa-NNTzN2RvhJR68A7gHXaNsH2JPfDDDNOSmXGtUbIFUaX85Ik1vOPyUXVnzgYkJ65kINz_NeBEkx0IA60hZ69nJmbsEgABkFuV0paPeRg4Te0469lpwRJkO8qH73X1qEa0tXXJD-4Wrasc4PvjvnqQjFwLM4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664fdddf46.mp4?token=qM6frFOb-iQDEDJ8LTOgwAXHzvEQcSBGf8SD3GUy6mOAu3JwBXZp5ZAL5UHqBTu4DoLHoO6HJ4L0tlPGxNesWfALRTp5I_fsVo0IjwA7B9KqIqVda2gYPAZRDJHxa_hRtxJBZCSYodUnuWo1q1R1raEPWlRkCAaVx-7zx9cdHy7dBUO2m5IBuqmXa-NNTzN2RvhJR68A7gHXaNsH2JPfDDDNOSmXGtUbIFUaX85Ik1vOPyUXVnzgYkJ65kINz_NeBEkx0IA60hZ69nJmbsEgABkFuV0paPeRg4Te0469lpwRJkO8qH73X1qEa0tXXJD-4Wrasc4PvjvnqQjFwLM4H4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
موقعیت‌های‌دیدار امشب آلومینیوم
🆚
استقلال؛ محمد خلیفه با نمره 7.7 بهترین بازیکن زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29208" target="_blank">📅 21:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJYRclT4Ihpb4kExX_APCwU9-1X3ddqoNS66GT5u_beXPXbXKDqVNqAZyw3mvkKjMXh8CB1dGyCHa-RkvGQ1lyBpjsL-wbd4aur7BzWT0O4u0t7LA_-gl-OoOTg1jkL3PwYOLvSAolcXanijHTGmIZI4k0laiLydO_QR2imLcW99nEzoVhykmSx_BYhePL75tc_IWXbVgkKS3JHNbxWlouH1gJmxvGSjiY2jX-P754GTLXcoj4HR6oXLo7oK6JIavxQqwXauetiFzDuJ4cwcgdFgngnBCIF2ycRKRSvugZJO9zFnuVFFpyjLh8QpeRQndgIEMY8CLa7tO_I0kInnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29207" target="_blank">📅 21:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti9XhBBtqTdfQpiS2FE3voEtGi1Ky0QZAYsj4Qxtj45aIvvLM7APATXts27zxzSByTXVeeLdDl-fIkG-3UwhIa07_keBmHhfaNTOPePXgZfpOWSCLgpk0KzAMbDptwRfcA0YS6Ur9Nn2MLlxl5ru5QY77Uy-BL3Jl063CB1u08d7WgHJG5yoAA1gQhkmLj__miuCmzhUc3AmPRUD4v1xEogezWUhqPm647YBbJSxWNT115mWii2Z4Osb5ipKS93oUD2_X-djElhSWZKPOpeOG58NnLof0_23umekef0zLutylvjmNtXQ6bLJ2-p9tAoszaqvviQjLJnOrAlhCOJPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری جدید یاسر آسانی که نشون میده عزیز گانیف ستاره تیم‌ملی‌ازبکستان هم‌اکنون در تهران به سر میبره و به احتمال فراوان تا پایان این هفته تیم جدیدش رو انتخاب خواهد کرد. اگه استقلال پیش پرداختی رو بهش بده 2.5 ساله آبی‌پوش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29206" target="_blank">📅 21:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfe4jVAtvYIXOT5Z9Pl4rJWKwCb_TKog5OXs42msnwv6QtoCnJNArWqsGRmHSTl16LlMWHG4bm0iqdgMRq8VhrHo06C0qX29zf5wipkwwoZnTPdz-UHe3vGgu2b48yj2Ec0zgy5LYO--VfoXu3rLJbRssYZyinMYVfepzoZrFIiuKadpFhtMLMOv4by-JXm8x9AHJ620FbFteOK2AiUWRklxwcsV_2B5p_P4DY28FJAvTiKVYAxHG93usH_XU_HC6Fst_pi3ugdjQqyx51bVLwvHnToQDGT5s9Akn2L6xwTtgA5ygFhVMWGjUH7tYi_K-vIYCPzaMODjoNSvHUquew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ توقف شاگردان سهراب بختیاری‌زاده دراراک مقابل یاران پیروز قربانی در روز درخشان محمد خلیفه دروازه‌بان جوان ایرالکویی‌ها.
🟢
آلومینیوم اراک
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29205" target="_blank">📅 21:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWyq9MKLOmDjOYAWwJkpTfpSY0AHP72fHaa9dsz8rFyvvad7WNHNJPS1G1fxV6Xk4KU3R5s6ulaMWbcs096vVaw6RTvvS-2v6c7dQRFRJUvHE8dES6MYnDOJ4BbxwsmAz-TiJ_GQet8uvYK-_wTdsxItsOkap6-nM-q7EnJl27qYDPNhsoc2hUOChXatjJY0i1py7S1nPNmNokz2AXKws4-NoVbKEGIe-PeIKM7HsQLMtnJHuISy3a9Le60FaEgMqaOrxBF1XNtnPQwjm0Tz4svBbqksSuZAelLSgnlbdXEw21G3yLpGJXBllpguk2RQc2PXNBNb998tOd4l73Chbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛ شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29204" target="_blank">📅 21:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/banVahDOnWQElsi9p4pViX_nh7efNeHLtnjbUuCpmrBRu6jOtQlyECxtG7Pbo-blHn2tMaVzpzkY47d0KASF4Ki1zUYmb2EEKSyB3n01dTaUZ2C3omcufhGF4rbVf6XkwTxm4q6n6YjcdgwB7Lx98FGXkQ5agUOSs-793AdMosMBClHdh7oukx4CYATXoYNsRUTnfOJLCyzrhc5VC3zN5yX48U55hG-TwCltI2-N9bra5zb9eWweow6qJJRVHlTo6srxCpQHTE374D9cirFDDHFybkH9V9RZk18Qih4380G8Zq_JY2ppS-RVj5UgabTzCP0N0Vz-SCf8rF6IACmgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دبل‌سیودیدنی محمدخلیفه دروازه‌بان استقلال که قرضی در الومینیوم بازی میکنه مقابل حملات آبی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29203" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKKKWshUYrqXNzanSd1a3Y84LX3f-kkyFhoCSmcBoxSQJ-YlkR_hf_oV9HBORitNnGAU1mXMx36hgKwJ2QiHCjVtqXOClFc-K6v4_efHvB6csqTB4GuOYzMbBoILhM93SzyEfHF_6SISIgPoRWPDJFwztpX25KrT7PPXEXW1KkGkOKqgI2NXJurb0kjgeGQsecq64SmqQbj6paH2bX-c4KKwZoI-7CECZSf1n0ydpv6bcf6T8AnJ0rrvWk7TP7J26B78qjcZKnMJaOcxgEr7wqgPdhGsbmHXT-zpX3ORgrqnBHKf0I0rCX_xEJhjztufpurFB-0kUnsdQOxJDwbtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخی‌از خبرنگاران نزدیک به دولت مدعی شده‌اند که از امشب بنزین لیتری 10 هزار تومان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29202" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJdNy2hQyEUaIwTSIYxa5tix1uJOu3HKS35MB2Wd-AZMENAUQmMF_4_5ynjQ-vB_RnbJoU8na_jzcvtfXh154oiD6EY5SS_KAB4sIaGXPCxPg-cVWueCIeHLAsWi6WgCN5PnHH6NU3GMdTCdAfSDN1_xHlgkv-rje2fiAaWOQD1W4o3aYtVMKEFP1x9NtwsvIMKfAuENY6w6GbVCCeJzzk_hN0G_XwEnn0H4S6fmtK-6a_IvuQtGlvXAeF0xJrwmTJ2_OG6Ghwlj7CNnAPnBOj0y0habsRyy9sZEx-NiTe271ggHRQ28IoRclOWD9hlpPCqHpT5R6KaYrO2ZH4GBZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
هفته سوم سری آ ایتالیا
🇮🇹
یوونتوس
🆚
میلان
🇮🇹
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/29201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=YzrtuNuj6HtzNNRaCl4dIK11bB8SG9cHe15Ly-ZSxF-QWF1YMuLgDUmhWfcnNXBnUwoJgwyer0k8tW_U7XTAaBV0gxc4t1L_NoxkFpnP56vTIQYP5yA6YDLG140JSKlwqL_2_7s-fnU3cDtooV4B0zrO_eSezPK1c6hocoYZb2i1lBjEV4sXAPFMQRlK-Hp4HApRIw_IQBv1A5y9GV5Bku1wUKZgi0hJtliGjt-eXYwvZidR9JqAnAA9lkK2kvrp9z5TrZAP_mk3qQzOwWlF0fWcZvpyJlJOlImL-YvkGaUWQDhpkQZSLBBj6O7GJwBx2k9xeMFFIe4QNQD8jKbvD5k3txnAZoD5P6nY9EgFIkrCuVV4vVVrmD8y_Q0gRx4Kria8GiebCxV0UQkeCyZtvuBgWMztkV0GKGzopAvF_W0iJhTyoQSm-dteeo_zZOhZ0uA0xeH60QOfOTiDQgK-br0-YGjyyb1-VdJLNX7rox1on3e9DhLrl21-Q8XPLP0HKXNHM_7-j3FlyeDwnr38CMi_5yh_mrcrT0bSh2ac8cJcmictyWbDYo_0zO9wRLZGMzBVI6ls_4nXTHmPjl3xE7vS2aC65XBfAKhB2NYKjJlkRgBlMbaGVQ71R_QUXgMXzUMbTRgetfWKTYW1u9hTuzCOivM4HKHVW15kz85tHNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30be494cb.mp4?token=YzrtuNuj6HtzNNRaCl4dIK11bB8SG9cHe15Ly-ZSxF-QWF1YMuLgDUmhWfcnNXBnUwoJgwyer0k8tW_U7XTAaBV0gxc4t1L_NoxkFpnP56vTIQYP5yA6YDLG140JSKlwqL_2_7s-fnU3cDtooV4B0zrO_eSezPK1c6hocoYZb2i1lBjEV4sXAPFMQRlK-Hp4HApRIw_IQBv1A5y9GV5Bku1wUKZgi0hJtliGjt-eXYwvZidR9JqAnAA9lkK2kvrp9z5TrZAP_mk3qQzOwWlF0fWcZvpyJlJOlImL-YvkGaUWQDhpkQZSLBBj6O7GJwBx2k9xeMFFIe4QNQD8jKbvD5k3txnAZoD5P6nY9EgFIkrCuVV4vVVrmD8y_Q0gRx4Kria8GiebCxV0UQkeCyZtvuBgWMztkV0GKGzopAvF_W0iJhTyoQSm-dteeo_zZOhZ0uA0xeH60QOfOTiDQgK-br0-YGjyyb1-VdJLNX7rox1on3e9DhLrl21-Q8XPLP0HKXNHM_7-j3FlyeDwnr38CMi_5yh_mrcrT0bSh2ac8cJcmictyWbDYo_0zO9wRLZGMzBVI6ls_4nXTHmPjl3xE7vS2aC65XBfAKhB2NYKjJlkRgBlMbaGVQ71R_QUXgMXzUMbTRgetfWKTYW1u9hTuzCOivM4HKHVW15kz85tHNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
درهفته چهارم لالیگا؛ شاگردان هانسی فلیک در در دیداری خارج‌از خانه آتش بازی به پا کردند و با نتیجه پرگل پنج بر صفر والنسیا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29200" target="_blank">📅 20:29 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e23364253.mp4?token=VVUhno29i5B5tYXw5DwL9IgE752At8OHUuI5hgQue3DsrvcjVDEmXnn7mxJit7fmRWYsV7JBuxMmOE5Oc5eY1QiG60yi-x1pfOQmPSq1URo6l5MA8FVNyaY5NkIrEHkvHlDGzoKvNJYXqZKxNUwceF2UNdsyXmUFm5j23M_mJswBBzc4KQqL8aNmwDSotQKlbwAtUty3HL3fAfNuxuCP5YhcS-RMeJbMOd5RKZR569HfT7UnQLPJsrOQx1RxLokIdGV4LQohj-FHOlbGken2OVy8lIXVM9kc3FofGx-CMQs78anKDu9v3aeUGuE1WFuGhtPVTLZDrdlXDzK6XGqwQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e23364253.mp4?token=VVUhno29i5B5tYXw5DwL9IgE752At8OHUuI5hgQue3DsrvcjVDEmXnn7mxJit7fmRWYsV7JBuxMmOE5Oc5eY1QiG60yi-x1pfOQmPSq1URo6l5MA8FVNyaY5NkIrEHkvHlDGzoKvNJYXqZKxNUwceF2UNdsyXmUFm5j23M_mJswBBzc4KQqL8aNmwDSotQKlbwAtUty3HL3fAfNuxuCP5YhcS-RMeJbMOd5RKZR569HfT7UnQLPJsrOQx1RxLokIdGV4LQohj-FHOlbGken2OVy8lIXVM9kc3FofGx-CMQs78anKDu9v3aeUGuE1WFuGhtPVTLZDrdlXDzK6XGqwQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لیگ برتر؛ کسری فیکس شد؛ ترکیب سپاهان برای دیدار مقابل استقلال خوزستان؛ ساعت 19 از شبکه استانی اصفهان پخش زنده خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29199" target="_blank">📅 20:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND8dnzAYjfyPlyJ6SLtTNZ7yrDY4o452aGV0tTSyzTtvzuQVPA8Jp8ypKQh8x__694e5n_a7fTjF5-_4kWaAHsaxOUO-RpWolK7Sm911SSjvkvNyrNempugolWoKWyouXWyGgxi5OxVr4AmAAKjY24Vf92bkVoPqlM-Objn-vBf3j_0qo74Rgz4NkuDM9qPpddD0C-7hLOY5h3KhcXh1x--owq9XnnYdeTzmJyHiMTdPw2tUBwCIK4BjeXo1BbDAcAg-RNrdbw5YC3EzPY9xuphF0lZQruLTEOoaSFw8Qo-mLdhoHXnPK6p6ISe9Ae2qRwRrNOrcGv0D7r1wHm2fIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی پرشیانا از سیرجان؛
مدیریت باشگاه گل‌گهر به سید مهدی رحمتی اولتیماتوم نهایی خودراداده‌اند و درصورت شکست دربازی هفته آینده با شمس‌آذر از هدایت سیرجانی‌ها برکنار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29198" target="_blank">📅 20:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doZ_B-23Fx_BTMIbwuzygiKUXUgVhigeJpl2h5-9WXKsJJdBJAxNFJ-0B3Q1v1EBrBKeyTtq--iGFqdsVDddKz72kTA3tbOYSzNA7dGKSn1zvavhYt99CVbpiAYR20Czv2vPRx5PLz7TfKLBRGTHKI_z78xpmY_vtwk8YmoNXjhlkLNv-71oDWocKFSEqv1xing9s9EyqKMl37hbRAvlU-i1exZiatWup2c_P_MRT3DdjBwXzgFzdtXjxjUrDPhUxyrI3CFJ5GsR5pzH-bj0ryeXRRW0FW8q0GqJNA0fLmOU1bdvG_f5ECWB5sm1Y7MWYJ4uTKfH25oPm0BVIzoOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|شماتیک ترکیب بارسلونا برای دیدار امروزمقابل والنسیا؛ ساعت 17:45 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29197" target="_blank">📅 19:48 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=u5eo-C8jgumGKhjwwBu1jkmIPqy5K-uCuPvAG8Iz4MLETCEFVn_p_7Y3lYrhXkVF-5Td313_ISP1G7UFWLGE_TM4fx9oDvcYAadFdNmYwCRnB89G4WMbAiaF3zAoychreuojqRG-IFd_uTuwMjHaZwkJ_hzjTOGjmDOz1rQ8FqmVzqcy4gDfxIWJQWQhANpVygV4G1f98vj_b9wj7Pq2GmZv1-EIswzmXNfTp1wXJ4dV_vn6tW1NkgX1xSWuvPb1PoT5aXJZhA2XhF7ydeXqQPEXa3gpgdd8ud4Oj599kPWJGyLEdEmNmoqEWNcoEnjSWDNlYEGSlIhbCHLamReHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de348f7d17.mp4?token=u5eo-C8jgumGKhjwwBu1jkmIPqy5K-uCuPvAG8Iz4MLETCEFVn_p_7Y3lYrhXkVF-5Td313_ISP1G7UFWLGE_TM4fx9oDvcYAadFdNmYwCRnB89G4WMbAiaF3zAoychreuojqRG-IFd_uTuwMjHaZwkJ_hzjTOGjmDOz1rQ8FqmVzqcy4gDfxIWJQWQhANpVygV4G1f98vj_b9wj7Pq2GmZv1-EIswzmXNfTp1wXJ4dV_vn6tW1NkgX1xSWuvPb1PoT5aXJZhA2XhF7ydeXqQPEXa3gpgdd8ud4Oj599kPWJGyLEdEmNmoqEWNcoEnjSWDNlYEGSlIhbCHLamReHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت تیم آلومینیوم به پیروز قربانی سرمربی آلومینیوم اراک اعلام کرده دربازی فردا با استقلال از محمد خلیفه و بهرام‌گودرزی استفاده نکند که قربانی اعلام‌ کرده که محمد خلیفه و گودرزی از بهترین‌های این فصل تیمش بوده و نمیتونه اونارو کنار بزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29196" target="_blank">📅 19:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjtUs1X8HFE9PFsy-OvAFhpq_UXY90Yt_udHBentPsud5WzpOm-YmxxgItfiYDIsXsDhKJf_YahMM-wQyV46-whO3MB5epoiSXnteVF9zYJ-eh4ZufljkLz2qLlNRwoU5gLdFv9FRwykeledGdxE2HfarOgE4D5hR1kgr2fMz8e4HC8p7i3eYYaKOGfHyESwBKrtObYn7oXJbpZT6u-svGuRQn5_NPmxdkem9iAPt3K-Ikia1_c3Dq1kalZhaZhbordTvNy9biowaMvIvq9zRIDIHKSGhXvJjt0WCQsr7j4TiBujzi_a0bqYM-t9ZH5IstDs3S3o3nzPkuYvZEtt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
تاریخچه تقابل‌های دو تیم پرسپولیس و ذوب آهن به مناسبت بازی فردا: 77 مسابقه، 35 برد برای پرسپولیس، 16 برد ذوب آهن، 26 بازی مساوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29195" target="_blank">📅 19:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29194">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAMbgMGsMIywnX3QpYBZZtOcMe5hHLKeHUZ1v22w7-o2r2NblNfJ2nYBvaEuf6SZLKK17m2T1bZZcWlv3UUAmWwG7kgomlF6muxS1a-Lq_0J0W46Yh1oXlefP_sWJPTxr5w1B6oX1Rk3yW8qdM_v3np3W17zkb7p_WsmcVdu1kf7si13wAOnEQCUrkxNAEV8EQO0Skmnu9q3CM5BT8ccudvGA4a_DUTEJuLJNJRCFzmj0xA8KiYPxJ_uU-0P5RBuVv0LZgPnb2HFLnX52C85XlXQdjdyDe-hiC3JIvQGPBh2SFWhWm7A8AB7CJTlEw_alzu7doQo-sCbgHoMXfkaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛ ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29194" target="_blank">📅 18:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29193">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🟣
درهفته‌سوم لیگ‌جزیره؛
شیاطین سرخ در حالی تا دقیقه 96 دو بر یک از اورتون جلو بودند روی یک غفلت گل مساوی رو خوردند بازی دو بر دو به پایان رسید. گل‌های دیدنی این مسابقه جذاب رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29193" target="_blank">📅 18:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29192">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmXvzuPPub9EtO0pd8cRzBrXRsd7KLeMqiyxWvJacYzGFwFf2BfhtxiO-17B7aj9vWO0SATMvawi3fOGMeIT2Ya60NBbV3QyuBeT5EbUuzI7YO0F6DZA5Zh9O1A03YzN2uhNT494wOvEBS9hFh64jRklXgyN5ljME24_OmOMx6iO7KbtcO93sQEJr5Y5RiEX7Mq7nKrw6ZmFYc1V_eypFogkFnXclFCDkErkip0bv5dnE62ooApQMbsMSPyu8qpf2OTGVB0yd5F88ftfLyPVGFQUMEge3Sx2hnjDrBCFjh6m-P4Q_lTy3gsncyzBadkUKmcAOtrAdBYxZd3dWtHRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29192" target="_blank">📅 18:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tj2-mx061mHzTWSXNwGhUtQE4NDF9T_tJOmuz5wgXD2Np0MNR19j3UDT_8ZzMlIhsBM-oneRgu1qlANSn0bDkfwyMFcFNQkTG48p07JHck939LIoHpSobxi-b1k7gJwVZmMbDmPPpL3-IOJRyABbFY82aOCZZKBZ3dacgRjgt0IHGWnu2OW2TAY_EYTu5IPW5I_9O7XE8ZbN-KFNtuReC90pNg2et1HbbPomWUAXkv9hxPOmXuPvq2gc9kq3OtAXqAbMqFYlL40S6rcqiYa7M6AlL-fA7ncwYXWndAFDW-J3zESM8vwBB5f4aHSjRdkWfhlWTMUVOQVZ4XtGSzoGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9R4lXO4q1W1qqy7R85EOSflJrf8VjnC6h2EpsvaG4Cpdg4mqsKAlyD3PXAGlSL158cbGY4SB5TbYtNrjNpAER-obLhTAv8ubuaQovXjLJeCuWS3YxLLM8bGJ5d3UnACoAUkd_joPL4-mC4sdr9D6U1e7Qb0F2DJMUlQ15ZkVNfAN2uKvgoOIMSXKWdAnGsfEb2lhq1r01XP5LiukfNkhCI9wkWYt1_pBVTZKz24siWywB6tIlHMBd2GtDVvbwK6n1h1isvux9r5baHxFPRXiGRC-Zx3V_Qed0dj4U5SFkPTdlBLUu1FIEl6D4muXr2d4_RzbiSePjxzOwuJJ2prUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
هفته سوم لیگ جزیره؛
شماتیک ترکیب دو تیم آرسنال
🆚
چلسی؛ساعت19:00در تاریخچه تقابل‌های دوتیم‌چلسی 66 بار برده، آرسنال 87 تقابل رو برد و 62 مسابقه هم مساوی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29190" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5vTASmmoThJxph8gwhPOxVoHRscUnRkas0ExKPdHgTP9j4h3ecmnlleNaSgCGnXHb6JbtTW4xzfcOpYDiCFfJ35v5n8uC1CYx4RpfkU5AYWRtsYaKYrO2BQ27_CqVYlTReFeMVDJ2d1m7aMuq093xzxsgR5HmaIxfGRs6ptkq80b5qYkSfWsf8eMVYzl9Kg9dE4JiQD9jnkWs4zHbDLgvi9LJecxgo6rLV_g3yFQRItLKe885RJbzx-Ulb64OkyzK5DwnHjiK9wcer8t3eeI6WsuW-5Q98XWRZQZeIrmdMkGrGDIfunW2wVuiY6IXSwxG_ax0U1HjInd5Dq34hcAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🇦🇷
رئیس‌باشگاه‌اتحادعربستان:
سال2023 قبل از پیوستن لیونل‌مسی‌به اینترمیامی ما پیشنهادی دو ساله به‌ارزش 1.4 بیلیون دلار به‌اوپیشنهاد دادیم که اعلام‌کردبخاطر آرامش خانواده‌اش قصد داره ادامه فوتبالش رو در آمریکا پیش ببره و پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29189" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29188">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE-wbtyXc3C7fidKTwsq7deLyPOBLPL3mK0r3ZtTeTl3q54h_zdxN7Q1Yr3U_RHbV_fQI8_tY1rfA6b_W-3P31O4clQhSv2v7wIsMIXA1w0KoRjKcPKYzKVXKAvk-bDTIJ4whsj1pZyILn82K0SZspKDu_jA8LcRKTgYhxRJaXWl-RM8T8kUt--aJv28MTXwtt-goibmNxlXasDVGcvDkX3donnwaotgEdNHmViW_PflyoH0LmcCsFSkJ6H3_F6s3A4j2x81Hr2fQGZX1KOVshvG96SgL7WbIiLCdt5Yv0HK5gGDLsj4LiMvLmxJf7b2Pej1lHqWmlJ1IVevdS0Gsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه‌های اجتماعی هم ۴قسطه شدن!
بااسنپ‌پی می‌تونی از بین بیشتر از ۴هزار فروشگاه در شبکه‌های اجتماعی‌مثل‌اینستاگرام، بله‌وتلگرام در ۴قسط و بدون‌کارمزدخریدکنی تا دیگه با درگاه امن پرداخت اسنپ‌پی، خیالت از خریدت راحت باشه.
لیست فروشگاه‌ طرف قرارداد رو از لینک زیر ببین:
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco
https://l.snpy.ir/gskco</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29188" target="_blank">📅 18:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29187">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icEbwdh8GG5VzVtkN0lOoMm6cRJk_bFffiBYKKOnIYykbxTC-0ogrlySBMJXR8nX_hH8IP3FkohgryRB0t8ObkGeC7-ta0o3qdJETzUdvAOoCq1-8uPbQhtDnNHJdsEiijQuHK6YQieBAgt6QCeOpsL1bSNBvcdNr0hrxfVjKX_9iOge-LRQln0KqdFbD9djgFiYURUKbC6b9Hx6qS7sNLWIrWt2HrFnlcK5m1P3UqATOBKNwurEFNsEMV07_urTYl8vRaJrqXLikW-xLlbgCfmuqO-ruXZ-yxU7QHSRp9ncx4dlNu2wh6H3XmVEkwzuQwAGD2Do_IoyQHOGEsUINw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29187" target="_blank">📅 17:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29185">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qw0vjKmMYHkLzMnOnpkRxorMOzZoCBeLuPnrM4f_8VPY8zddey9SJ2H0nz42NEJ-XHl6Lnw0Z4kXYG_T5GMh_4ba29hHE2A2MCmPhdxz0GQaROQieO6QsoD1C_T4_iyLmoGlj2KsoahoICU0-iMmEA7BJ8XUI5OK5nurRRHi0CftZ3cPb2wsCAnMsA1Uj-pfjuSI3qiSXlNoJaMzfN-5R9t5tTemcQ_g62-rmEOc8kk-cW3RpY08xTha0GhO8OeIXNcS2sNsoCWWnfRDkfkIt9nBqGoH5NUfc72Q1KRsTKyjCpQcIb_XyM91Bmh2IVHt2dmJiqzCDAVPgJcAvNHe_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFalxynOo7WjWVTdUNVxSZ8NcukTF304oKDnCFj_3xzegiToq19xcCfRCWA8gR3iZdZcq_8IZrza0PpI4_x_M4_dwFqRBtkDsjRZDg9W6AiVA0YUXHdh9L-M3yW5VBVUkobrw4ufTBZ3TJKc_UBox6GpSECnDZjSPR1PGYiZyvrp0R-LJxwnAgp1x-E0J88jpxZ8260SER2cg1i5ecF-N6775mJpLywgocbHkYq4zBH6rETT5HeMFPrswAEsgDfI70H3xmYolkhmgUy8vitFpygyE_pJVwl_TROsaXiGSRISILz2KnMGHp53Rs0F5V2h8_k01q3JMGdpQSTskbLzFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌برتر؛
ترکیب دو تیم آلومینیوم اراک
🆚
استقلال؛ ساعت 19:00 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29185" target="_blank">📅 17:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29184">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkPooC3hXNF-a1RCx9UQAMN7TiSOQRL9eC6gAWl2mEpiYZSqOXcq5KDwbvqHhf90WT4XebgnmfIv-r2H7mds8VyJR1Ch-KfXwNG885Jww9QnX_kaVOhKVaWLNZlWJVBT8M21w2Ope6QINtUsnVnpGyRPxD634w8ROWr8IENdekXrpIpNBipArJ5Zte8Tg48FMfd-f8-UwlTdQoXhzTgz8MKm1dSBLHTqGqBdRs-w7eHUCbVWLicXsVrsghKr4CtjSBj_NPAoybPBPkjZgD_EUiEpDjZmXsN1uT4BqqDlXjbiHMx7k_37AujaztvaCwGC8n3JEh1LdnMLb2A6N7JzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باورش‌سخته‌ولی توسال ۲۰۰۲ تیم پیکان یه اردوی ۱۰ روزه توی انگلیس برگزار می‌کنه و اونجا یه بازی با من‌ سیتی انجام میده. بازیم یک یک مساوی می‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29184" target="_blank">📅 17:21 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29183">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=tqbPHoHTsXfcXXCR7BSQ1nNsAF_yIjgb2eaV_dG6-7qSC6H3YkR8x-eR-nro4Xa4I32Q3i43DGKtdLaCIdtwaK_hRaJeE-KlBGXsDrsegZYlIgOngN0QR8L3LYzPwatdWxIl2KL2RqFcv3Ww5Mo5OCYK_zlzpYyY4nIzWl9HLWyVOo-5ZkLLgzSVca0UEubFsapZfsKpZRax3__XKS2OQ_Q8V7SUcdo1jv0ajieVjfBi_5PXmy_Cjob7yvihBxPtJvO0VUKfGSEWeFFBSsy3NBgqN17iaYtYNHWlv1dqcTPWICc7kTVBS988w6-agMx32LkPY4KcKfcpW_KJgPJs2ajDJqf5HoMtPCrRk06OGBR-wrfce9u37WCg90lHBRvZGHhOROZh8Yw7fzEwFqMyL8Qav3JtbR9zRgX7R2Zll9yGB_SiDdLfO073Lmpm7Y0GM6EThLNvDH45Kd_ZqntU0eCEBTcopoKTGipFrHCI1RbBfJrqP7ZtbyUFHItuFb-wyGp9spghts_yYOhHq6zimnaBZ7BaaM7S0ysP3xz4flTRnlnXIcDJ_A8VHFWEn8TsKR_qrulPIu_aOLlxaheoRoWsmcIm7osHDDRcsuh3Mb-g5jOlLwNS4_culmhHIBsxGREIZhgqGJ3YFFjHwdPuOT6qCmN7hZAGZvlt8Oc6IDY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b4709ec.mp4?token=tqbPHoHTsXfcXXCR7BSQ1nNsAF_yIjgb2eaV_dG6-7qSC6H3YkR8x-eR-nro4Xa4I32Q3i43DGKtdLaCIdtwaK_hRaJeE-KlBGXsDrsegZYlIgOngN0QR8L3LYzPwatdWxIl2KL2RqFcv3Ww5Mo5OCYK_zlzpYyY4nIzWl9HLWyVOo-5ZkLLgzSVca0UEubFsapZfsKpZRax3__XKS2OQ_Q8V7SUcdo1jv0ajieVjfBi_5PXmy_Cjob7yvihBxPtJvO0VUKfGSEWeFFBSsy3NBgqN17iaYtYNHWlv1dqcTPWICc7kTVBS988w6-agMx32LkPY4KcKfcpW_KJgPJs2ajDJqf5HoMtPCrRk06OGBR-wrfce9u37WCg90lHBRvZGHhOROZh8Yw7fzEwFqMyL8Qav3JtbR9zRgX7R2Zll9yGB_SiDdLfO073Lmpm7Y0GM6EThLNvDH45Kd_ZqntU0eCEBTcopoKTGipFrHCI1RbBfJrqP7ZtbyUFHItuFb-wyGp9spghts_yYOhHq6zimnaBZ7BaaM7S0ysP3xz4flTRnlnXIcDJ_A8VHFWEn8TsKR_qrulPIu_aOLlxaheoRoWsmcIm7osHDDRcsuh3Mb-g5jOlLwNS4_culmhHIBsxGREIZhgqGJ3YFFjHwdPuOT6qCmN7hZAGZvlt8Oc6IDY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛
به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29183" target="_blank">📅 17:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29182">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=EirKy9Kzj6OnilRdb3WcpF7oE5_PSWnvyfk85aVCZBpKliMRMj-tu4BReclT_V-kOLix60lS6IxYqQLRPkVmjxRUBmLXjcgLS6gEHiH-dvQMQuDJrtFFNbV86L6qSdzWCwLLOKDCo5036IS4RY8ukl8x_P5LmJuJLgzCCgVcQQrVXtMEqhz5HDLxzeTRLZWf6_vdBsOs4JxMsAl4sQ1I_HCMxst3p2HsHBZAwhh6m6CRDqNPcu7EMkvcASQj6mI0UP60y50hs8mSWanAn7c5rJ-VejHP2KeoBpweoViSGHO1vWU7Eh6jx9HL5Ub2CF0wQXt-T9l4TP4A0uiwWGNgQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8cb4f04a7.mp4?token=EirKy9Kzj6OnilRdb3WcpF7oE5_PSWnvyfk85aVCZBpKliMRMj-tu4BReclT_V-kOLix60lS6IxYqQLRPkVmjxRUBmLXjcgLS6gEHiH-dvQMQuDJrtFFNbV86L6qSdzWCwLLOKDCo5036IS4RY8ukl8x_P5LmJuJLgzCCgVcQQrVXtMEqhz5HDLxzeTRLZWf6_vdBsOs4JxMsAl4sQ1I_HCMxst3p2HsHBZAwhh6m6CRDqNPcu7EMkvcASQj6mI0UP60y50hs8mSWanAn7c5rJ-VejHP2KeoBpweoViSGHO1vWU7Eh6jx9HL5Ub2CF0wQXt-T9l4TP4A0uiwWGNgQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عمرمفیدقطعات‌مهم خودرو؛ این پست رو ذخیره کنید و برای دوستانتون هم بفرستید بکارشون میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29182" target="_blank">📅 16:45 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29181">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TlZC9msglm5e8sMJ1WNAewoBSjW8UR0ZckJEbUiyDnJ4Nf0A033Q95tTOZ6rs9psGL1a1D7zndhk2B_DKn_ZsHb7NErvlM0nHFYHnur-g7TXesDc5OGGWz1Wtf0eo6hg3sR-qS2QH1mzhKZxjLDH-0xABumQG71Eiw8Jg2olBHlkQdbi0h6ejkA4k6YgYZaeMz_SV3Rhy0UKo1vfRF1Mj4ACrpY59YMgN6Ch-vHb1luEDfDDjb8dHAbqYCYJckuCgg6lbbEg6aOiPJBKJ7OV5tXjZlCxcH01o6v_DY-r20TlymbkGHW_-YAfdt8E5YZwmu_LbucfEIrjpxwyA3bwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29181" target="_blank">📅 16:36 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29180">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUSFWvfWvUCdhfrEHDzv_UJv9K0y9W4GHOYWqfP31oipEdV7ioGQVdlmnrbPX4JETZntOUGdyBbY6ZSe3lNpRrhH4VoNVOga1E0GcmVkA9270CWhRoq8b15yufBYYmUDscFinfjbpftDjBIAIK1CV9xeLQrM-4MvTkD-aE6Hddc3IahCvn14s1whL3B5WKkmUYlEVzrrWXp5UDJL1NLmexeqw7SZnjVjByHMqotWIkxOmbERgNoBwf9gdUi2GZsicTZhPcQuJatlsUQX4W5uI86waNPQg6TssZHe37tlPhBn0DE3g0pD-_Gn5pG7uflZvd86lQjahQOQ4C-sJB9OnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29180" target="_blank">📅 16:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29179">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8GzZSaKU_1P8K3aTOrLT8KsFRr6ZpnWoV_rAgis4EovLLk8q-Rc-yF8gEdCN1MULdK19x7tjTxJGGcli9alwtpIGswn8XsJNOHNZ1hua94lDKgF3m__SfduwUJgRt9k9lV4R0yNjIj5VDvdSgWPuAS_jP2CzY1vQ1klBFsd4mAX1tqsa6x9hGnAbtpmCoU2tvrBhkXmK1wtiNtHWEOPa-corQVAN97YuzXPNAUtKE9l17J2yK4JScxpMHE3ZQEyQlMZYKDE6T_ajfEYxKSjPR7wS9NEHbov_ByWNHeSSkFifhQcv5H5Irrjn-fPWb6a76QXrk5Uovpb8hIZ_59sGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29179" target="_blank">📅 16:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29178">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=BctmgSWHu7KW20HDXnqvzKhOERr8WPL-CP2AsVKb8hAO7Ud7HUoDpMuSfAy9BHu3cIdN7FAcoqciVcoH7PKzhBhrKrtaaQ3IRKsj7szeCtdOOfspmj78cpU58BIZVWwqofdrzTduD1gRsBpDnUnGpK2QoVqJuWhDwshAJTi5JZ7Ki-jyh0aKS8OC0Cu7CLqiPMgUM8HtsBiyLL9MPctduA6rMN0_2vGm52NxmEFOHgzpcV6sROeyXQKIqvHGjnudEPmoeeq9E-by6ip2umpEacBfUk8Wc4WoAMxu7NNteSrBu8O6OpmZXea-G904oiC_XymlmX2IIai6pqOrWeLkNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e34dae2233.mp4?token=BctmgSWHu7KW20HDXnqvzKhOERr8WPL-CP2AsVKb8hAO7Ud7HUoDpMuSfAy9BHu3cIdN7FAcoqciVcoH7PKzhBhrKrtaaQ3IRKsj7szeCtdOOfspmj78cpU58BIZVWwqofdrzTduD1gRsBpDnUnGpK2QoVqJuWhDwshAJTi5JZ7Ki-jyh0aKS8OC0Cu7CLqiPMgUM8HtsBiyLL9MPctduA6rMN0_2vGm52NxmEFOHgzpcV6sROeyXQKIqvHGjnudEPmoeeq9E-by6ip2umpEacBfUk8Wc4WoAMxu7NNteSrBu8O6OpmZXea-G904oiC_XymlmX2IIai6pqOrWeLkNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس‌جدیدخدادادعزیزی: بله امید عالیشاه به من فحش ناموسی داد منم به بدترین شکل ممکن جوابش رو دادم‌. من‌ خیلی باید بیغیرت باشم که طرف پاشده اومده تبریز به من فحش ناموس میده و من جوابش رو ندم. بله من صدتا فحش به امید عالیشاه دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29178" target="_blank">📅 15:43 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=JVtxXecbQxPmqfnxGc-m2GvIxQiu6baZqxl_XYLVa8MiTByci651ToZpLlgo71GaU_8X5LiYdmTnzqPOabNad1UGJunFDNbtoAG_lg1HXZYFwfeIqhFtH4UPOeygoW4u1nTO4VRL9Dg9AipjIjlrWDY4HPux2QSsc_MGSgqaP9c0ZZf3egKFdF4V_DDiObHLbTWP2i5roP_6xRWGChasHkAmOqX0mx8WlCvfXNdqSSob8esmp5t7lRncX_ncUzYwjtSO9JP_rL5hGYys0u2FdHlVF3QBW2bFvfp69NovV6ZeYn2-tsOntozs1rDbvPFt-DarPa1z97elbgdzq2ykHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8508e1019.mp4?token=JVtxXecbQxPmqfnxGc-m2GvIxQiu6baZqxl_XYLVa8MiTByci651ToZpLlgo71GaU_8X5LiYdmTnzqPOabNad1UGJunFDNbtoAG_lg1HXZYFwfeIqhFtH4UPOeygoW4u1nTO4VRL9Dg9AipjIjlrWDY4HPux2QSsc_MGSgqaP9c0ZZf3egKFdF4V_DDiObHLbTWP2i5roP_6xRWGChasHkAmOqX0mx8WlCvfXNdqSSob8esmp5t7lRncX_ncUzYwjtSO9JP_rL5hGYys0u2FdHlVF3QBW2bFvfp69NovV6ZeYn2-tsOntozs1rDbvPFt-DarPa1z97elbgdzq2ykHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روزی‌روزگاری‌ادن‌هازارد فوق‌ستاره‌تیم‌ملی بلژیک و باشگاه چلسی درمستطیل‌سبز؛ کاش هیچوقت اون انتقال انجام نمیشد. هم رئالی‌ها پولشون رو به چوخ دادند هم ادن هازارد اون بازیکن سابق دیگه نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29177" target="_blank">📅 15:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0sMaqI69A83EorAqrWjJLWqGj7XvaxOkRU1vkLpna3zJ4rVS7boRu9iMnjnMtAaStcgYEWNgGUFGBhs5_Ct_mJpHdgHDGtJunDeX9nhGw4P1OcsqcB4js4R1Myzz-uZOsbSSvM8TPLfR_vi8to_Y282mNCt7ZhRgJvaBC36kH566wrgThrfidA8_pOzy6F4xJXLthq5Hic48Qx6XhyC2dfTD128mM_sjRum2cwPJNK2sQOZ39X3Ad7WdAXRRrpplsrPAX1_YmFwQ4NwBXG4EHtNg3GHTjEkytQnMPf4IDy9xrQcLzYf7v9fR7OV_OIkVrLT9ZM3R2H0wcoZij52tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛
ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29176" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29175">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=jOT4DlLLnM6oZ4t9pqFvacISHon_vUZfN0M8MWS_dHDaxVBObGKkFo5OdVVxBPvHtyIO0nWCJUqJ0eeJ1-UUQBsksFavdInXElLGlTkrArQauBTSvnro9--ULvsJ_v2oO6jcsrVUp-nPH0poYAnd7cUnxdNBTNQ_hSwlQRI_Uo1bFsy_-VckfFtkJ38UED_xm9cd6FJndccPxbtax3WRvVa64hAoUNzVy1MjBjodrd7-ugZJqtapBxvHLiWT3PmgQ9lLK4iN0AvxQSz4W2F21tMFiO3bo4ZXJtqFeD6XYaNIV-4z7dwZ8D3RAurlHI62Zt5mrYbgHKIqpT1oNALtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f7513b2bd.mp4?token=jOT4DlLLnM6oZ4t9pqFvacISHon_vUZfN0M8MWS_dHDaxVBObGKkFo5OdVVxBPvHtyIO0nWCJUqJ0eeJ1-UUQBsksFavdInXElLGlTkrArQauBTSvnro9--ULvsJ_v2oO6jcsrVUp-nPH0poYAnd7cUnxdNBTNQ_hSwlQRI_Uo1bFsy_-VckfFtkJ38UED_xm9cd6FJndccPxbtax3WRvVa64hAoUNzVy1MjBjodrd7-ugZJqtapBxvHLiWT3PmgQ9lLK4iN0AvxQSz4W2F21tMFiO3bo4ZXJtqFeD6XYaNIV-4z7dwZ8D3RAurlHI62Zt5mrYbgHKIqpT1oNALtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇳🇴
صحبت‌های‌جالب ارلینگ هالند درپایان دیدار روزگذشته‌مقابل‌کاونتری درباره کوتاه کردن موهاش‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29175" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29174">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsgyK5MHKJXtx1zN2FPeM3EF4uOYlrROXAFm-HYMkpZi72oUkOZzIw1j_25QrJM92Swdn3WXBjRnWOVQ_VpCBs8xXTpAbfn6liDsENlHvIvD3kNCuJbjWMF107sSXE53vm-0U4MYZ-rTyY_UjUkr1bKF0SLQzjI4DAgi0WInevbgeHGj4G0zdyylYKQom_LPVjxnRfzIY0v_aOF3zWPNR6PZxkW5_8tuS4vYQmd8mLWJS17NgFshC8nbmo_4KEsr3Qp8ej09cLNw_4WFGk4__8ye8VURVTHeZ8NZhzpbPO29-fO9Yt9hYE9NA-GADtz5L4_-XJa_maUeuNOPH2jilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🟢
آلومینیوم
🆚
استقلال
🔵
⏰
ساعت ۱۹:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29174" target="_blank">📅 15:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=ZWslrLbl-BQrdJVAdorrZ4WciI9I20jXOsc1jFKLePGHRfvu-G1Y_VJNREjlDle02R9BumkvvjPldXOLOFqtpn_LOlZzTEmMat7xLjavxOVEWlBOSCl3V6VaUGWXYgfJDpMrLwZheMl70X9ReXg_DPeUoM8a2oXYspsRljBeUj47g7IFplr5HvmH6s5kdwdmJ9wGLv-u0-hBqZqBhaCfxOLgTiAHlQaWAkLJMUSaS5JCAxbKipzew6AGuaInO-iB25-qkqzG02IpHQ9TAKSipnjDdjnPQrJOyekr_ceol_1QgfUUZxvhuwqLsUpVEpCYyfNYds0knREYmL1UzO7AwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac4ec6833.mp4?token=ZWslrLbl-BQrdJVAdorrZ4WciI9I20jXOsc1jFKLePGHRfvu-G1Y_VJNREjlDle02R9BumkvvjPldXOLOFqtpn_LOlZzTEmMat7xLjavxOVEWlBOSCl3V6VaUGWXYgfJDpMrLwZheMl70X9ReXg_DPeUoM8a2oXYspsRljBeUj47g7IFplr5HvmH6s5kdwdmJ9wGLv-u0-hBqZqBhaCfxOLgTiAHlQaWAkLJMUSaS5JCAxbKipzew6AGuaInO-iB25-qkqzG02IpHQ9TAKSipnjDdjnPQrJOyekr_ceol_1QgfUUZxvhuwqLsUpVEpCYyfNYds0knREYmL1UzO7AwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
گل‌های‌دیدار جذاب و دیدنی امشب دو تیم اینتر میلان
🆚
ناپولی درهفته‌سوم سری‌آ؛ برد جنون آمیز افعی‌ها در جوزپه‌مه آتزا در دقیقه نود مسابقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29172" target="_blank">📅 14:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4hqmqbx6RorJBkMEU95cau19Ax_0fWFZnSP30y1RQoWWKSrww38wmDxyW5Zj7XK-ejSSvr9LJuNHYJKwWeju09Pz8kf-WFi-uaUChqnqdSxesXBeJCTVimjFBTchJ3vtU_W2pNwOMA6MLZRfPvTKV6-_-oNsAu6Ekr_Ab30A8w2S4D_ZMc2CwjJn3tEaficVCEAraC38G-u-DeYP4Kq2QHC_F7o0Jtqd2KiJlOTBv9FVCkBwpONgpCXgNTXD4NgZEwdoE9_GwoFl9VFAnVTZmzYG8jhL7BtFc5JYg3p0jGF81j-ac9ox9Qkb2F050pjzcLu0wG5nOSRZKNc-2-dKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29171" target="_blank">📅 14:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5IImDs30XycMBOnNZKnUzukbR6ekeyFLxRRA7cKO4aaxeVvri5FWxj9zusEu_A0-Sv7VXWmoUMIF8E2qZ1TVh40oLfaANpXq40mwZjnZ2hm0LM3YzqjC2ElbsqbBKwD9vzwjsl0CWtDYMnznAAmrGYW0fbC6E8b6KtA3Zs7VyuoZ-TCYOxCbInpTy_D11vgmP5VQ6N9berNJnSzWmsU6bSu-T8xXNDtMWu-Ydd_gbItjBwBb-zIvMW8RZPvFS4qhmBQu_Rr3MeaPaazdEUpK0OJSXl0a183lLXZnVXX3mnPSmQZaWwvWy2XjBt3yCYPemsie2R4dG0hM3sKZInB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29170" target="_blank">📅 13:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0jN9R94qRkFS8HCz0fsYqNJ5xoK0jMauLYBQITZwwlX8fPDlvuTKjhJLb3EOZlTCJBFqn_xi7zsDC36P2cxzu-As_Jwdk_oU0Fokadf1TWQUmQ9fnWGI1rZs8-QKU2TuBPZtpIZv9C3NjdZ2ZIu2cXT1lMNMSvGPMMO0bErPK_Dac5brbJuzVuy_ZtTSpn-3m1O6F1hAKqT82SfN_wijbX5xGH7vLVsrj-zizCwF6oJ_Oe_kiukj1uIv43p6itKAtHww_DymS4vRbmmnxc2L8FDvUfOUQq0L0VrJqGTu_YdDAU7P0FGOQtomE16qvdQbgbCiVDZXATUjZo3w8MC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29169" target="_blank">📅 13:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVYmQBr8zcnqaG1VIr9YlCL-1X8T-UvNLxPWaNUlTC4zDpkYowC77UsLjM8FMdVumUujOQe0Nm1i5oBuqc7xansbD4KKPVS1unVAgdueEujUnzp_jfkYxRQ1aVcyruYAZcgwjbamDGs-yeyUievLzEUjvPNHbQLD6dZsclGiNnyprEqo64zdo7fcNH3ibkGf3DC5gAEES14RvX4OEiYZ_da_POH4mb332kD7tEPYEaGSQsncD2C9wOSFEtcozHQ3q-vFxBXqYM7muwTSJWhlYUKbmSARyqUUSl5Dmoe1tS_I4tLwLZXvk-_fIrQbyeE2H7QhENafp_cIRibay07bGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29168" target="_blank">📅 13:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29166">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmMbLzOkLJc_7WR9FiwnrMQbLfl3QN6wMFgbSdc5FFAdhauowQzTZ_IFVRmODeZkQUFOFH6HaUxBCQ1qaYj5_KEJpPuv2ym5SLa8mIrPh8gNYPf-s91IyBEQVFLu1tcSS9pk13Sybp1elBrDo-tJhaV73K7dja1U_hNTtNElIoBn3HYujnM603L-IIr_J1tnA7gkNC50iTmePwhrJAW91OuYpa50hWrTZLhv-USSEmGt9UPtpLZzp51YRVGP8MiJg53-2S9qrUu3W8AYUvlrjQ93dnrhgcKCQmQ6FAtjlRmjGMVYpp0J-boSFT7ZkOmo83jBMY7z91N4PhinXqBIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29166" target="_blank">📅 12:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29165">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzmbD71SZsQLZ0KG2cOYPZDfeeABi_YYpe_YcrQYGANrfwsbW2ghiiXBk7TKJBeyjTPYCDqSY7uawOB4nB1xHD1it9fWlnnuPwIRg2HWNT98c1V7tg5gQm1Q3RDKZhIKYPx-a0P2jT8XC9INW63MVrGBNEVhGMZ2N5X1j3E6f-k_FVOeX_yxGgrP7B79s8zn6gwynFwGQD3s4pEaIHZtjzpz6ZKB8kIKBQSz2G2PXZcP-kXsueqNn0Z_YU-BP1R4nt6XHONcBjS6Th-4IRzGLzwoxLG74gq-t82HoQe_m8mMytQfurBvov0BRtQ4DviG-NV6ABFqFS7td1UX_AnUOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/29165" target="_blank">📅 12:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZnhJIPvVo0denRURicJ3-RTTteienb5SOH2recyW-RXDT0A9U11WtPIvJZasmejjiaUxlpj6l3zZaeMBvlB79sLuaitMsTPiozdWjv-h0r8ThjAIODAgPp-R_BV0ZDD7L8QOed3a0oJTlUi2oTufromq0pG8eUhVeaSC5NAY8_IbRfXXC_CNbPzafvESeVCQZSqJB6rgpNytLOLAaES8ntIXUF1K3dsCfWRAhiU-IOOaOQ1szS7dx-Wvr5xkwO-Ejs2Cb_o8SW0SgMehQVY6g6f-GI-SuPsAobcSKyIN1XtecEDUx6bnraHq_JUTFfH-BUyrWYaVYYP3OEfNsTJvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/siHwcJEG8IMeYCc8FPOocrNmYnUnIURXpPPSJGNwIUUYjzY_QFmdzxc3T2dP3ijOux2v4lSTRNgZIBxz63Q_OykFCb49_bgaLMtB69HyLGPTyhROOOcQZSSRJVGzkS_GJ9FIsqWuTe7IW_ipvkK10ytRpzEFK18nt7EarSpH_rKaTwqxetMzy4dJRwaLIu2J7eQvmM-mCADSFq4cmbcXQPTA-DqW7wyjwwKLFJEiiDq92xcw9WFQ4v1jwb2eYZM-CWGicf3S9VSNAHSATNVHE_EZrYJ_B9GgOpz0SnHAN3ygLD2_iHmE4A6HarP7gF-_Cj0QsUnLAO7Dp7OkBa0riA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
همسرگابریل‌مارتینلی‌سوژه‌عکاسای عربستانی در جریان بازی این هفته الهلال در لیگ برتر که از گابریل مارتینلی ستاره جدید خود رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29163" target="_blank">📅 11:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amIz-qEwMQWQm2eksu1ZHBdXsSGQsG2Me6WiRNyHS_TH7dgNO9rA_O0aGRVgsvdNG7Br3t-LnohzdUy_qbfSEOPadbupgjeit3WA6es90EhSM0-W7dkRJ_7IqUZPzh3iWhZvQRu1TZfg7G1o1HRN0d-30u3EpdiXC1sqEjwGEHBvQKPTvhddVegSLQ5o_ekc4sR31UdmW2j4lsjHFUPorS2GmCcNwSGJWhFOBzHppU0_Fh2HYuFYl4xYT-RVfpn43ewPFH1L63LMdAGBWVmXouf0G_-qDKqndVanuAmWdjElf03euLVuL6xNbW9uQDQ53j5ao87CHNspd-1std1SYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت‌دردناک و تلخ ایوب الکعبی مهاجم 33 ساله المپیاکوس پس‌از برخورد با دروازه‌بان حریف در بازی شب گذشته تیمش در سوپرلیگ یونان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29162" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇪🇬
10 گل‌تماشایی و فوق‌العاده محمد صلاح ستاره مصری سابق لیورپول در دوران حضور در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29161" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29159" target="_blank">📅 10:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29158">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=uxhIA8lp6xXXRkLCzidu86AZymTdxRrD2L9A-D3optDSz65COwY4bKSMFkiSPSHLwTXFCm9nr5CQR5ojNs-LISagw6i0IR6HUVkRFpNsbh-nYfgGBHas6-83UHlDQznFKjgX4W7K7qjwa1g1yfkTFQEpqTFBSN3qBWb56Zlh0IfsttCN2I6deHtoPsauzRb43AvIYman52gy-SLugtKFQzux_PUwBk0AC-8viGEMx49pUAo4Qdb909qOcxSxf_jHba5YbYBrVaaXhh1coGRpvD8aJOKqPq_oWIWk1YjcCozulyv88biCWLsU0xyv3LEqT9ktDodbOigim7rjJB-jmqSH7k3wX0Gt-tzV_M8Ro8k0LZs1bU7bVZFinQvbY2Yq8ThDyGTau92-BPcXFrlaQb_tZ7ifYn-M3mjaa1SmLxKW2t6DOu-dsCCscebKfME9MV-DLrMEHYC77vN1QGVWMeX9m5hFDuTXJLZrEOGsPVPWNn4tuumo_iDRC4skV8-IQEzdxmO-yNJovXWdoSPMz25pzIxJVHVsr0faGXQXOLiELBzO2vBy28CTJ1lAgbDglC1fLJoAlWn6wERQ307mhDtXFYnO8raiZDWYARmkYv-F_mRniHinVUyBwaXoutHxFWvHUUo2WhT0wx9ANbojILQhJD96un_E6L6yKuVbYZM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64b0fb55b.mp4?token=uxhIA8lp6xXXRkLCzidu86AZymTdxRrD2L9A-D3optDSz65COwY4bKSMFkiSPSHLwTXFCm9nr5CQR5ojNs-LISagw6i0IR6HUVkRFpNsbh-nYfgGBHas6-83UHlDQznFKjgX4W7K7qjwa1g1yfkTFQEpqTFBSN3qBWb56Zlh0IfsttCN2I6deHtoPsauzRb43AvIYman52gy-SLugtKFQzux_PUwBk0AC-8viGEMx49pUAo4Qdb909qOcxSxf_jHba5YbYBrVaaXhh1coGRpvD8aJOKqPq_oWIWk1YjcCozulyv88biCWLsU0xyv3LEqT9ktDodbOigim7rjJB-jmqSH7k3wX0Gt-tzV_M8Ro8k0LZs1bU7bVZFinQvbY2Yq8ThDyGTau92-BPcXFrlaQb_tZ7ifYn-M3mjaa1SmLxKW2t6DOu-dsCCscebKfME9MV-DLrMEHYC77vN1QGVWMeX9m5hFDuTXJLZrEOGsPVPWNn4tuumo_iDRC4skV8-IQEzdxmO-yNJovXWdoSPMz25pzIxJVHVsr0faGXQXOLiELBzO2vBy28CTJ1lAgbDglC1fLJoAlWn6wERQ307mhDtXFYnO8raiZDWYARmkYv-F_mRniHinVUyBwaXoutHxFWvHUUo2WhT0wx9ANbojILQhJD96un_E6L6yKuVbYZM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29158" target="_blank">📅 10:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29157">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw5jLI4_REW25pav8ohlc65JuF6otXi-HjjM081XrJM53uCzcM15Nl4XIixDWR_IU1q7cJiFrK8iAKSX0J38sQRUjUWexCyXbEz9Btpmz18xh5cv7KfqFv0nJnMlLkHd7BdUnyffHgumodDzAmsnshMPAUI5YSI-2y1g3zk7eAqmq1Q8dmKtSI6JCvac-0HcfUbojkwhAB8AN-XMm0ODYWKZH0KO06ubvvY9QX_3LMqTOd4s8epYWdOLE0d84ytK5eWPUxvwL2RU72-g_b7h-XHqHVVzgp0Knn5fNYcR3bV9SyikHn7Wi-ceg-9VwHzJ60ylME8C-4z38pl8UeWLvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29157" target="_blank">📅 10:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29156">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kl1uteqV8Uyv-XSKbZvNTVK8Lr0qnMKa0by3k1-_n4h7cPCCbsbIt-qgfeP8Oszt7Y5C4ffb-dxbTL1YbaIq4zxxlETJE-3C3Yod1sfMdp06dvnz6fQ0NGEmREh_bpYin3gQhb3wB-6fgyEuUE8XLxvI6yhNeKJpy-CSZ53obg78LvzlFgbdLa9GBLxUafuRzkRhCYhNiJ-waa3PFBIXwOWbsJZTSUzlPx0dE0PjgdVNo-TnA8gBfS4En8s2sanQ-PEhFK52eWYsxIBCEVZv7erv0Z7lRQe22g0l9eL1BAZwC9-goKGAXLoSPrShD755ZOCL0h_Klkr9bj2csbzm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29156" target="_blank">📅 10:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29155">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🟣
🇦🇷
در شب گلزنی کاسمیرو و لوئیز سوارز برای اینترمیامی؛ این آتلانتایونایتد در لیگ MLS دو بر دو متوقف شد. لیونل‌مسی فوق‌ستاره میامی 422 امین پاس گل کل دوران حرفه‌ای خود را به ثبت رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29155" target="_blank">📅 09:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29154">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awUa8uiY3Fwa30f8r_XFFD986Pq1kfB85FmUyz3eQAsZ-5rfVXf6g4pU7mL0ufGxnCwByxegNU3T174b6g2YhVHnHMgqN5p0hFUTiw54Jkf2toVhifLfGl_0I1D5dpLDWLCNBV5s6aBnLFb-sCORFBH7ojwBpmNK12UNFbohJIZFInQc-QBexFZbGr2-EPXV-Fh0_eJBB2I3vU85_vMxt8iM_o4dze74Sy-lxvI5K4HFxY1ueEhDp8YamFjKTFDrRS0n7qWeaNnzd-QUr4hfwhvkxAyNMxO5FAgvHHuPrDLQmKQqUN_hmLq6qeHlCczbyQ34PmNwfv0TrU2JTO1rFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار امشب مقابل آلومینیوم اراک در هفته ششم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29154" target="_blank">📅 09:50 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29153">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/29153" target="_blank">📅 02:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=bjXLTOKbbMK5Z_Ycja3DkJ_icIDK_OnxFMGIPeGhjxttffIRnh4HoVbOhYDidXJ5rlc34EYa8kZlS8lPFMjj3okkRmtSxfgVtrqa3p43cTzUn8mjNKQPI2kVYzDqoZjNcUHnr9-r8-zQpPIFHi4G-SZckEU8OF41meZjPAD7vgj-piEiaqUp7TvK0szBFfdGRffNzUs8GyLJSWM8oo2LEQHDTN5OWANuWNyt2a8i3Wu6D3OjfOAQiIJfxCsYp0S7i_U1fAHm-bUXzTaIRrNQp4QCV4lXjGSfvq-tzCVBgHX_Ks5t414mCNiV2NbqjMUf3_W8oZ_Mp28WF5zlw2iMyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=bjXLTOKbbMK5Z_Ycja3DkJ_icIDK_OnxFMGIPeGhjxttffIRnh4HoVbOhYDidXJ5rlc34EYa8kZlS8lPFMjj3okkRmtSxfgVtrqa3p43cTzUn8mjNKQPI2kVYzDqoZjNcUHnr9-r8-zQpPIFHi4G-SZckEU8OF41meZjPAD7vgj-piEiaqUp7TvK0szBFfdGRffNzUs8GyLJSWM8oo2LEQHDTN5OWANuWNyt2a8i3Wu6D3OjfOAQiIJfxCsYp0S7i_U1fAHm-bUXzTaIRrNQp4QCV4lXjGSfvq-tzCVBgHX_Ks5t414mCNiV2NbqjMUf3_W8oZ_Mp28WF5zlw2iMyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E20GrsbMHL7i5JsJWcEYCsAu5H0dbQ-u_kuvsQGBumJHNH4ivbYE0Z9bDa0GW0VzYBalfHuXNJ4tONi4IpDAxPhr2s_c3wG-eu1lCi6jfyyvWTcX0rc1meMTXQe7Zc5uJm003s9SK-r3nUIX3WmQbsjTijqYLWimvHrS4gOBaODIK2x0XdIKc7Yff-_lQqFRCycPe00P-79SD-nKaH_Yt0u30el4EiuKeSnf7dK6-jGmnpniTPQuClDLGtolxb7agQpz2_DFRRl2qYEfe7eeGom60kkX2fM2637ekueTH1AnZQkvOLM6hEkm1fSEc5qtpLkeIQ8wp2e1ePCBknUdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va6g9YHgdadE8vMVLs3thKu8av-NiiJ-dH7jYlAmPVi5yblrurzxnZBfKW_EDa43QGZguBr04ZHC5xmUMk-yXbIf0wln7iGmhFgZI5WPprasH_NYrdhp49fBoRcNYw4tTizMhP2hcbCArl2HwjW32VmwUOvg0sPpoB8wGvno3vBF4gu9WEWm12sbo3G4pm_S0SXIZFhJtJdkWkh6mkS1MkmkIBChyINtysRHlGNP5JWo7MXpJBfpd5uRPO6HTZiR3zsCHV5R9etNZ9L3L64_2QFgnU289nDI5re7lkvhhvZOZqzEq_Ykl7ZfxP5j1STGXS-PZqf8orjm9mjVuvo5uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMg9B5vxPQGSoJAXmWu_o6HmI_XrEzQZgpa4n6rkbU4D8FdIXuXSpHMSNTJzJkCAjneZkVFIVssaMIsAr30ZwnPzhg2xey6hfvxE2idwSkK7GSPNtxkF5-idEj_w8CGyP-rh7rKb3IwB1yrrouHMxk2xNJ0jGoXTwueWqJAbW3SHe47ldETUShMtYtSkW5y3d1-RVHH9XGWXRpXhv9pH_CVnfeokTBDfIsIwB8W1hHPoAyF9BCCwPyIXeTpXWKRdRM5gsg_AIinythTa-1fI23MwL1_JNv1R4WYtG25Vf1d9m7poULjrd5tuiXXMdjgVH8Ydk3UVGFuEnp4t7i4k6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=Aex_vVPfnGQqkGhgDiNQ5-_hugEKnjp-K64Ul4JAi7mE1YhsCuMkiH_rB58wK9duAYkmzni1DBD-T9iiBTKuVKs-j9P6_xhuLE37FIPfnfel7NlFnorhiXYKxwkhGMRN1_1YPDIcSzUeNfX4KCHwyFjVm3SvaV5PhJtIp58gLyJ8MN6Z-i68QbHJtXq8ZiKl65NzKpMnC3a_pqeROsFAD8wI2L3wQABhG0yISJNpBuhtDmYd06e68ggwO7vfSsYvRFHaLOXtArHeSlf-c3oypuXR9XXKmg4A636P2_9uRjGlyy_ALPeC1SGBU1N0qNwOWhoj4cAWDjiseap_LdxLsaun7NLDVqRrS7Gr4gEaGwunI1O9yO9Q9DIHVi2MYvfKEY_C8dHFgilGCrccXLKCw_eM4vTu710wl-3a0D0Hr7M-oNxC4ADob7FTnq1vZAICOaxlJIwR4YJGB8xuCVR7XSdu01jdq6ISDvn0xN-SB41UMfiH5TIbsUgNQUJAWC0Ova2bqcFnMxWrR51KLbjyhRub3fiOBD9BcnhAb81Fv9zIxq93VwMypfyPBOcUVDzfCma3j__CqtJYhJQHCytRQshw-R0rOr_P4MSGJUAx38_FlWbp70z5RbMMQL9NxrtNOHqOVqDkT2mT_u_vm-hi_V9Rvczik2_XiuUOh7oghwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=Aex_vVPfnGQqkGhgDiNQ5-_hugEKnjp-K64Ul4JAi7mE1YhsCuMkiH_rB58wK9duAYkmzni1DBD-T9iiBTKuVKs-j9P6_xhuLE37FIPfnfel7NlFnorhiXYKxwkhGMRN1_1YPDIcSzUeNfX4KCHwyFjVm3SvaV5PhJtIp58gLyJ8MN6Z-i68QbHJtXq8ZiKl65NzKpMnC3a_pqeROsFAD8wI2L3wQABhG0yISJNpBuhtDmYd06e68ggwO7vfSsYvRFHaLOXtArHeSlf-c3oypuXR9XXKmg4A636P2_9uRjGlyy_ALPeC1SGBU1N0qNwOWhoj4cAWDjiseap_LdxLsaun7NLDVqRrS7Gr4gEaGwunI1O9yO9Q9DIHVi2MYvfKEY_C8dHFgilGCrccXLKCw_eM4vTu710wl-3a0D0Hr7M-oNxC4ADob7FTnq1vZAICOaxlJIwR4YJGB8xuCVR7XSdu01jdq6ISDvn0xN-SB41UMfiH5TIbsUgNQUJAWC0Ova2bqcFnMxWrR51KLbjyhRub3fiOBD9BcnhAb81Fv9zIxq93VwMypfyPBOcUVDzfCma3j__CqtJYhJQHCytRQshw-R0rOr_P4MSGJUAx38_FlWbp70z5RbMMQL9NxrtNOHqOVqDkT2mT_u_vm-hi_V9Rvczik2_XiuUOh7oghwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhZ5NNVfJq0StwP-bDTFEzupVb9ePXXwkLvplSsNaVb0hFYdmIfuOea1_13hVvCacxjnf1FcFwTjCrM0c29tNV2rZOZZumOUKo3lsJOen39bi34KtCwnVHyZLDw__uzBIeA8-0o1ifG1oEmWe2QaN2FD9DEg_Pqw4-RfM0b8xeSXed1cH_PycHXilfUaBXXNY3x7Hrq5z6EB7iqyq-BrALt6hbaE4KzC20xUTM6l67GrVn95uVv9n-DoBbo2jcFBbeUEz0CsqqHW-Iyh2xaYgJaH_bQyXQULXdv709hd4Ar65V52tn8OeOwiP_3v_uvlmAi9LNMl1xqf5pcHSczEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzy8Smd_DJrrZfn0ESRLQrsfFzzTMC3-V0mnjfxBugHZ0coAtagqMvy7u1WamG7EJvaaCzJKjCSsFPbCIld-bPBvTqaGDjRR0D4bsyyQkqg-SkuclOB56HFU1AQlkns1u0pfeAuUOpZyN0c-7n8zeZbkNaf0_8PHEswnb0JJJWlm2VAZ0F_ZdDIhUmkjLN8BKzFA1TvoEFaSEXoazhnVJlQ8F7TYLdAFNvBNwtzLK5NErn2lB9lStqEXp44jhyKqRWyI_UNVtOcdq1ZkccKYxmcllHSQIHDS2Dc6ERXA4_zS1wtfajeQkR-BZvzr5_oY-3uv9XFCB9GczgsorKb6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=VO9SJBj6eUZLn3o7VDj1FRREhOq1PNURztCOJpo-mMCbbVwFeZHxiCd9Ieozx8PNpRMZdrk0tZjFtSh-d_5mGG1mda-7aqLjQVF5_AncNEoYmV7gakG88AfxeogeiOQ4zYuUM15cvsBD2KBir5mVZ9Cu7H-a0SUhenO74Sm5yeUst9RKnm-UBGVpTqmJuY9iHhRIDCBpy8RqmCDVAMlOsRNOb_0wMUpp9EoM8QbJo3mdkF_r1AKfv6z0k04ZRQfWLwQPDu7KsFMaxNLGH-i-uc_yWvs4_SLGRw35FQoVXf09JbuTvZP8EnUoiKFH2E_H9oGj7aGLVYY6gRHMONnrnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=VO9SJBj6eUZLn3o7VDj1FRREhOq1PNURztCOJpo-mMCbbVwFeZHxiCd9Ieozx8PNpRMZdrk0tZjFtSh-d_5mGG1mda-7aqLjQVF5_AncNEoYmV7gakG88AfxeogeiOQ4zYuUM15cvsBD2KBir5mVZ9Cu7H-a0SUhenO74Sm5yeUst9RKnm-UBGVpTqmJuY9iHhRIDCBpy8RqmCDVAMlOsRNOb_0wMUpp9EoM8QbJo3mdkF_r1AKfv6z0k04ZRQfWLwQPDu7KsFMaxNLGH-i-uc_yWvs4_SLGRw35FQoVXf09JbuTvZP8EnUoiKFH2E_H9oGj7aGLVYY6gRHMONnrnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aR5wWYZnsChDaFKm8wtQIIJWg_RltqE_xDt5e4kKU_z8jEn3mJuRzO755V31ow4SjsoxZURT3hjbWPuT7tkNmv00kdjHoxgCanCjTEaT71Bj8NoHPnzjlb05UbHn9ftlgc2jXOjRxoHF-DrKwyg30xVqOex40Ukly5Rsv6xOvq5chmsoLqUzwTHpqZlc5BPAAriY1Yu0wXweJNGuJUcmGHwoztfbF4fLc5e-S_AarJHIiftO0s3AGbgwxQbBNQCogGxiQrwXW12jrAiP4oNSMtAwNNRtF3ezqW6wOi8Eyugxa-wKkqrHZN7-efmpiG2DQsAQ7lT-i1N_XJvqYIe6xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXb2_pbDhqqSp6jUnsink-BTHaqIerjhEk6wlO1UNAIcC5XvaH7PM8H5C418ExleCopy1CP0AG1xUBzv8WgH3v3eDAyqclMVyakZSTJzfBUvQtTuPcZ7Sbk-NqZwPjK7hyvc-50ZBB6qRq7lumYJ_MWnu577tqbEF1B1GM7_UuTTSjIGeToFvbfxDNw4V2BBegcr6CbW6OtP4punCWrbKJ2VJc2vLL51ZZRQWdLZSfOyuKQIFDOyYIuQmnVRSj-Yz-6Wghu8ViEVJi4XMTC2O0_0OemiOz8vPfu47ZoLF3Q9s3fEfDw-CjWq-zcWxY5FJ62_jJsyaaYav5wVm1ppkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc4oQwU7rMAZWP3YKV92h9Ie14UFKcIxkXcEyLqyEZKyOADTxBI2BA6KKDDyPBWO1WRfh_gmQiJSAj1AX8-TmpPJuuAkHjM09JXhdGWD2ku9T9atZ5GxOGO0AUhyYa81v9tp3U83MSYMMQ5zyBYRWygNzTyzBer20B1nWU0SD3fSwnDETaYsIPQBvYsL6exSdHnZeKW5h4hiv6f51X0j43aeZLo9LCPZ5h4zasNF3y4wj0DSWjn-FXSEzooRnnZtFwfzm0XL0ypz3koziXw9k7696I8fKSKYez6M7qVhaL9r7w7KDlVH1KHPYuKVbHXgjqmUusjFApJkjTY49R-qTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtnMRdPHhWTKUbWQmaKX3wMdR_KNWRcUiDXrWVy3Z6N0rXAszJTvv4W5DsoDnb8DZd6TeM2rHa-QWXfZDLkmu7ShUbVfrJJ8ZkMuN9NMqEJ6pnMQE5DtUo4sszRbcKk24vE_UBIn8-NWKu42wwBQIDlqN_3zpW-55FpD1rkNgVXoeLVVa8qM5KYqA8cP9GNK5EN3iwj_Aoj3Kd41gfhwXIgjWMpnW860huk2NypulmhpBkHxYcRdZYMbpzXq_awepH3fgxcvjdXRr9_WKcBQD4X8gIpPWg-FGeCnb66SbjT51v688W7rrZOZ_fr_fEYSeYQ20zSoV5U8QVrcbwNFjopE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtnMRdPHhWTKUbWQmaKX3wMdR_KNWRcUiDXrWVy3Z6N0rXAszJTvv4W5DsoDnb8DZd6TeM2rHa-QWXfZDLkmu7ShUbVfrJJ8ZkMuN9NMqEJ6pnMQE5DtUo4sszRbcKk24vE_UBIn8-NWKu42wwBQIDlqN_3zpW-55FpD1rkNgVXoeLVVa8qM5KYqA8cP9GNK5EN3iwj_Aoj3Kd41gfhwXIgjWMpnW860huk2NypulmhpBkHxYcRdZYMbpzXq_awepH3fgxcvjdXRr9_WKcBQD4X8gIpPWg-FGeCnb66SbjT51v688W7rrZOZ_fr_fEYSeYQ20zSoV5U8QVrcbwNFjopE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJQpdoSl9Io9nAShYmijkvtShwcSpXhDToRniUw24WQnQTb4Sf8HRF-YLZ9NT1bWUphw1m8cenoh1Bt3LStPb_4AOxn7tWeyi1Vow1fhYiBpiCqWPksP-ZtxolDzySae8GTBOSjZDZCcLwdUYZGb5hAmQjGQEYSdMbhg6zlHsIeTHPHt72A3jpVGFP6PXzSkDK6pGLffu3zVb6__PPFiLDOEd0a1atAuqecpQ4gY-WiGCJW0KJbF0LtRXNh3SF0p6_y4_OQdScPax1qVLISUjWjrmFzNpEG-oFbHWrrpyIOnXy49TZXD_P8o7kGZE5SKoPzBEVH_RpVCM02Hyf6LEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uck2RuM6mcXL4Fy_w7oIBb_cTdydloCjJISxpZ4CtgH6hRZA4ZmrjfqEshvC95ClKlpM19H6G-d-1Gy0azUDMSax_Sd7hgAYdI0bgVpUCqxoVnpTsg07DuzRGufTAmaP1l6oEWQXOG2wiAPKVm_kOMWo_Aix8xEbPjfbS4c04VwoY2QnZJ__dNymIVD70hdrcfekd0213y7WQiU57PcnLBOD_quRD9g5YAjLpKSkLM8CoYCgWSAX4zW2hwxdsliRQxkB25Yls8MywzMLkoMRpg-SFN5hdwgiwm5QuQ_rqdsruhIB2F1Sn-x7PI9BG0JoghfzCXnRAD92afVmCzoGzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dOco8wxTFDz3TfYsWmeTF5N9QYtVuBVSBm1wWokRJ_ka0pWXl7y5YWdgAHLsN0_QiJX7dhO1HOy1T6obKAEdcfxTesq_KMYWN9b8LejlsQKWgnj-wPuxSi7NUdJ7zj88LpfOe75rTqDshovl6iH_NC5A-Em_C1BHn1uJ0JxywdKY6OlJTJbPSsLtuvJ5daspNdRz7T3gj6RrQw5_F7WNTtj6LRylFy66Vl61BV7ItvjZDutqRwzWYlLqrKGmqoi5lwtCnPme3ecyT2Era8ynF8xqMJTBLqWE6IJB3qScyaC3nCq8iLsknC7p5esseKSD80C51DellHRJQQK0uAa6Sg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZrRvrrefXiTyGDMKnJYS2m6KCBuLeQKAOBoaauUlAbNIm4BZxy0rCKpzrNxFUhyDZUaVCrcbmbkQiqFhE9BbtF-ZwwKuh7lOqKsSGzV-mF3udqLcKGzDlFRckJn0CvBgEbGwEOYkhjGMtRFHN5pLiAG5avaR4cCBA372KMjklmys2ytpH5FwZTiZPyiVeLF3eLaZ2kO0TtC5Jmfapz3C2UiU8cgYu2n8j6QNlBOgCw1ADRD_rhtrc06zp12QhS90bpY780-g33--cw49KlSazljG5gdG8TmMT-biMgZjHjFxdWAR-lDqCh0lwl4cGaVC5taknXryw7avP0NJzgiu-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rk3c8kWNf_n_y1XKhxiPPbq0CiF19WUH82VuTbSpH7TbcW7KxGcL9mZD1Kgxu_nW8TZHHFxXuN2moTkTqEsZjfKaaGT95C1PKyyhoySiPtfcg9-HjowiWCCj-zVKpn6dKuSlIeEC1YZs3eNbktKVXhIkuPB-VyLXPa9saytmz7TMzD6vnQMgWAeHl6LZ4ufhZTbFXjBrkGzHCQ9Wpl_j4-BIn-TfaTNx1nFeiz1yuOThmGwlUzvnYw1LcT5Our5glECHSFmfQygtyKGVSJR3aq9ht_zoFpM9zJ-6jCY57XhHD5fiFh1iP0Hzf1EMob4rd0wcRMkoZLTO-Hg9FmweFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=evIZNkOtAWzMgDZfBaiHyJDEQ3vxyxgNml9_WkqfVtHuSLZiQZKuWwEr1aUHaEFwFnk7aZcWHaKJyMMDdT9ZLQOZB3Cmg4DrQZVzLhf0MOqngXhcn6iP8vdTITXXqTNQphmU889C_G4-mmmNY62LkBz3ft0Gb8qccNrNx1KXVqHNdzSWroNvALoO8R-Co57W3OlDOeSuA5DZXuTxPOuXqJC7K2SChfjz4mJBh04urvXOUdtu-BnviVLVQhFEVa8mPwTnjAHeTmZVgZnRuP94uSWf-tk0eq9xImZ7ybLr6E9C8nRCQVINFWMIpimQOdyBN3YzR85-a-oRwGkckJgiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=evIZNkOtAWzMgDZfBaiHyJDEQ3vxyxgNml9_WkqfVtHuSLZiQZKuWwEr1aUHaEFwFnk7aZcWHaKJyMMDdT9ZLQOZB3Cmg4DrQZVzLhf0MOqngXhcn6iP8vdTITXXqTNQphmU889C_G4-mmmNY62LkBz3ft0Gb8qccNrNx1KXVqHNdzSWroNvALoO8R-Co57W3OlDOeSuA5DZXuTxPOuXqJC7K2SChfjz4mJBh04urvXOUdtu-BnviVLVQhFEVa8mPwTnjAHeTmZVgZnRuP94uSWf-tk0eq9xImZ7ybLr6E9C8nRCQVINFWMIpimQOdyBN3YzR85-a-oRwGkckJgiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDfSTcXNyzkWLg67t2I0dOBGmOTeSGwYAivhrvNQhqQNRr1MDaBZ1URXhAMTasy3xcs4d0uPOSkbkY48NnZ_7fJxrAnoe7jd5RAsenKnAKyJ3K7jG_iWyxXQZRekkCN6ABPJm3e_5VCipvi9gQqL_urVr4Gm6VS7qrR8z_7jg89Wy5dvyxvioOCNcdmC-D2UBw1y6cz2dbD6T8s9uOQiMLipkot8yCdfNAew7_E4LQFlZSoozO7AFIhWCg7lfO8VhB7YOVsFUrCjhq531RahTJnm-PNE3_6QclI8O3lJ2R_g-8LfpQbffWSAsLg_PXXU6gYiCgJDL_GxnhNYTq-keQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfnY-2uRBnn1e93zT65_2yTJ3mw7u6oHa06hB77DqnqKVd4bmIiZl0l9KOr1DD7FJmu-Vy_X4kQQnWxT9ZFQxyLPTki0kGLTak37VlKsCkqumtgPPMhFWQEYvgSQ-NIeCtrKl8Zh_-k52KAmnkZxS2Xre-K4aTBl_zLhy2bsLhOHb_geZrKxrAi79vcPt6TnCYQBLTwlBSO8eAuVLVXNuFGQLr8pW6Xm0AkF48KKOZ_wtAaTuAioGuNo1KkoaWfK4stvjkfPsijlWdoBhLMnByf6wx8HyM_-Nn0LiiGCq2ay81MtRFYro7KSl5d_TgNKjPmnFCFkMNVf5MGaFwk7OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=GNGf9smU7fZnBlsQt986Gv8kFyOiQ9LqM6AS_EpwSXuml53PUimKyQ52Mhy4F0IhpI0i4Ipa7u0FrDbHHeBjM2UtuuTGKwtMkkyTcJzNL8UXAEjsnb2ZkERbQzwj1Kn-t9w8XYFlIzFN1rEiSqOh7z3DbrQsZVwS01DLTc6su23Ubwzpx9o-qzttTuzaWFpg7n338YHmWX7mMqRGSBg4WwhFATrKHv2JwkS8npcqLohRZq7mNck8rj_cMhJFG3kj_hg4gDXhQLeCkhkpQbCdXixeAjV5Kq9yjTlvyyk1y2XrZVJrQpekwVuUzUzeMEAa5GkSr4-NhrbL1fnhVPJ6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=GNGf9smU7fZnBlsQt986Gv8kFyOiQ9LqM6AS_EpwSXuml53PUimKyQ52Mhy4F0IhpI0i4Ipa7u0FrDbHHeBjM2UtuuTGKwtMkkyTcJzNL8UXAEjsnb2ZkERbQzwj1Kn-t9w8XYFlIzFN1rEiSqOh7z3DbrQsZVwS01DLTc6su23Ubwzpx9o-qzttTuzaWFpg7n338YHmWX7mMqRGSBg4WwhFATrKHv2JwkS8npcqLohRZq7mNck8rj_cMhJFG3kj_hg4gDXhQLeCkhkpQbCdXixeAjV5Kq9yjTlvyyk1y2XrZVJrQpekwVuUzUzeMEAa5GkSr4-NhrbL1fnhVPJ6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3h5XGNGObxJBff9y853MMsd07xuawtZ-sp5N29JOqMXzZSmwXCVScLsDwnMdC5NGy7y07q5pGmwhIKFsAEIISEquUnivNvTHTfoUiOU_ypjZwfUdb2M8wZz-i9qsrixiflNFQyvDr4Ny5VpRM3Lb4hF8UFoGqnPYhZ4oW_omkzyNDHa-ss93uWXrigvFSqKpCss-S8Apn4c2828CinY59jhJ7blZbYjyudnzsuwg1bIF_8J9Gnqhq8-aS1w60H-VGp-1vmcUIlgZitYM_XPfQ1o4660wtGLwB2WaTGVdsr0xJjcQkGzONiIyEgrzRlWrS-BrUM4tbYOgJMQwhPpHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4--XgfKPiOe2iTWXvosXVdJvUwkZQGqFPxWUzEFzdKuS3UJlifcMDVqBUgD-MifeDrfFQb6SFOSga4y-o5gr6UA8OI4vs6Go5srg7SfUKdQXIhKL3qLqtFa2vid7W1o5Y4P4mLZxiKmVEHr9QcAFK8ALSh42N68-8oPv6zXhMC4WEZZ-zU2luVUPi8uC3tZx3c_25_bMI0lx0RgsdH0stKKpoQ7GvbjWEFf24osns7X3SKB649WMWpJA-1vRtIJRnbKsf2u8pEYJMC0Cw1Mci0r9MDG8EJmugyOk5FZPUVt2s_P3XIJ3xh28mLFDJSfzvhu3UwW8BfuqiDNWqTpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK8Ce1zTraYqPaSXb7hdqcR9R1Is2NvVVZeT-MXTiO4MTEbL82Q4hp5Lu_RlukgKjSv7uwBtC4PCYle_JbOpua31Fv6I-Y2qjBQqXVrbTr_W7hAwnyiCJ20rPHaAoSuwrqJHmn8W8YTH7yA0TNx9ixm-pTZNyKv178nkD-mupfATcyyV8CMArnX-xUI5SmOqp7ON9bRVqNj3A_0isyyLQcBAHComxyCprrakIdffQCsyKfXTrUFI3rnFwnbuDS8EjCwh1n1uG2kCvrXRYgzB5Dw_WDd49hYpTOjiknHpS9OoX2SBYFan8XAXUZJiefQN2ypcZ86xd_iDOsKjwgOUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
