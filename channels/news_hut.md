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
<img src="https://cdn4.telesco.pe/file/Wb5vikQKjnR3R064ZObBTHz1gJJuCo74W78UKpOhVvFS2Map67uxXatO8taB6JER1dNWDdtX0pdhMfysmMZxqgirDg0QiTRwZ67CR8ZHsW_VI-92p5iIsCCAFjG0B6jxrbmA0IVR3STpyV-PDjwTSMvhL2uBUwlv2KoilXLF-LfhntpGDwhks-qwkVJ2OIFOqneekX8pII0Q-D1-C0vPozQxFBzvhKZaI-BC6SqcIZijzwedTv3AwRKEatLyjBaJ1sGn3FQ-bzNd_bghF1vbMkHbnUIPbw1paApMmKXdpQsUJ7rJlDcD2N9ZWLnkW1yh-jUA-oXT2tZSVNLX1Q1OSQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 127K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 20:18:18</div>
<hr>

<div class="tg-post" id="msg-69907">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf8b7227.mp4?token=GDAb3PLrKQW5fhvI-pEU-NyOTkmpnSSoDgVQg1y-TLTw0ZRo3MTsV8QU0gSbsLjpVLPJ9Dxoa-pLs5FVgfpDzSPtdBzkbIHs1Y0TS7UXYBW-Q2lJ58a9wqvTBVByd_K2RtJAgJfjCkclEupTK_qAj1XzVLa1K2kK9CBo6D7Ri8Y1vEXYZMsuPmYmaANi79KFOwtnRph_tTECIRdmCZ6eh3gO9PnP2YFZWC9adb9v6ds48RUtBGrah3Y1dBNmehmr1LHR8FNj5HuKTsXRU_DNVT5A-X_GOBKl1euuEMKssrVnr6ws-dcChlm4_jm9N5yzZO_qv4iD0BPYBku688Pnkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
رامین رضاییان:ما خودمون از عمد به بلژیک گل نزدیم و تیم بلژیکو نبردیم.
🔴
چرا؟دلیلش:
جلوی بلژیک شما دیدید مهدی طارمی یکاری کرد تیمه ده نفره بشه.
مهدی بخاطر تیم به بلژیک گل نزد.
من باهاش صحبت کردم داداش چرا نزدی گفت داداش اگه گلو میزدیم فشار وحشتناک میاورن و جبران میکردن، حقم داشت مهدی
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/news_hut/69907" target="_blank">📅 20:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69906">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇮🇷
فیلد مارشال محسن رضایی دبیر عالی شورای امنیت ملی:
آمریکا باید جنگ رو پایان بده و خسارات رو بپردازه.
به هیچ وجه کوتاه نخواهیم آمد.
تمامی جنگ ها باید در کل جبهه مقاومت پایان یابد چون شرط اصلیه.
شروط دیگر را نیز از طریق میانجی ها گفتیم به اونا ک باید بهش عمل بکنن.
توافق با عمان ربطی به باز شدن تنگه هرمز نداره.
پول های بلوکه شده باید آزاد بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/news_hut/69906" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69905">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی We pari همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر…</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/news_hut/69905" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69904">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si5K2npmDngoSkXO-2TisKJqVVaT4L5pFjMwbVHLj8V3xqVYCOMMHfTvgih9AA61O0LaVHJIj2JImoBE4XKuRzqeU7T0RozD_sIPCiim9duSG9ICESNIIx7tCDQlibe3ze6dtS2RzneRNId6ZMxxGAUGNJeitxv5HyWvr8wDLdn3lqFSwqPi0_LVDwK6KEY8CZ63OeogCKwbipCHFg6_I4swszxGX-IZdKAqqu18ovOB9VvzfU3zGS37m7emwAsU-Z1_o7e4TlxI9xsCbV-wgV_7a3uSl186JE1a7ZQmK8MF_XNkVaHzh4l9nVdKwlokVfWww0tKm-5hTzwhK3Qz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
واریز اول و هر شنبه 2 برابر شارژ میشین
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
💖
فعالیت بدون تخلف در کشورهای مختلف دنیا
💖
بازگشت بخشی از باخت به صورت هفتگی
💖
اسپانسر سوپر  لیگ ترکیه
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
https://t.me/+fxq9NcirUag3N2Zk</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/news_hut/69904" target="_blank">📅 20:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69903">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e58dcb779.mp4?token=lBV4ToCv3YuwX4SYEqBs8ci3i00nrf4N28m1W5VKRrl9W8kvtCwG7-P5FjmEwmWybXgeWe0zX3xAxZ69RR3bvgja2kG7aoo10R3tx_LXft_4DYA0zT8vtWrQbvaVO9qC9ZJ3RpquQJ-AdpBNgwRVysUrQnEwKUtayVKPlccFcftMCa4-o2Xy3UX97C6ZBwYrMJkzwmvbKLmEZ0LbtNwNqwDkCxfgutpLeivFFFQzpvVNY1ewY3oFiQSGAqNT4BdHSYXbqpjb09TEkzPdyFDLgKa-RuIu-cobGPPS6Tgu5tFmrtBSa5z5TIp4ODZjvodadUP_q1-vx4I_P09qhY_aFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
روایت تلخ یه فرد نابینا:
اینکه من نابینام به عقیده پدرم کارمایی هست که دارم بخاطر کاراهای اون پس میدم.
پدرم وقتی جوون بود نابیناهارو مسخره میکرد و بهشون میخندید.
مثلا پدرم بهشون میگفت بیاید جلو بیاید جلو و وقتی میومدن میفتادن تو چاه و پدرم مثل خر بهشون میخندید.
پدرم بهم گفت من این کارارو وقتی جوون بودم انجام میدادم.بعدا وقتی تو دنیا اومدی دیدم نابینا شدی و این دلیلش کارمایی هست که من باید پس بدم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/news_hut/69903" target="_blank">📅 19:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69902">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfb370d6c1.mp4?token=HzYiZY1sqVLIqKjNol8p-jllT7FckJ2lHwXEzmWLcHOLRSOeDaOuczem-opuAtPZ8TDrlBtRgXSW4JOMEDQIez7_a-rIvTaGOo4iuHGsyvRK0Zx9RVzga0dqV2djTaahIRiwSGaZ9YULIgiZCLQ1q_2zxilmTaXiVw0yQj4jD5PaeYX-olWAOXxuLA8D7muVNA6uDBXO1XLcUP3vcfS5TmayBD1ZTXxu0E-nYjxJffXI0j8w8ccFKNnvbSYsNm3me7JFljLQW4fNDLe-PezoViahTyJefPi4FoDxQiwnNXESpqsRz16MM_UMb7ojFaoQAfw7qUAqlxONBJdsPVtA9RNkYmjqyb-EhsrsO5rGUz1hunQ2lSC5JoYMJa9BSvDqRfFmaYV7A-Zm8Mf4FkDJalojnpzJyvR-SHxgGy6HI0S_sKNJYf_Y7MVIynFE8aTe8r3pyZzvdq1v7XuvUpWqQKt9HlU3oKNHU3aKAXUJ3Eho2pfmsmFF6katENitvj2x0NJPMtcEskLzjBFbWNPQvrK5Xpg9_SbOalpUMzQFnhV7rQFkHe9wRkKBw5VPPunrO-JtfenjFTPKX1pwtaq595fnr0OdfQHzmuL6xEfAWW7P0Qrw22nCYm5T-WYD8RkENOv9d-IACPVBTiWslbnWzpwQBKqAKe7R11CNMieIopk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از لحظه حمله آمریکا به پل B1 کرج:
@News_Hut</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/news_hut/69902" target="_blank">📅 19:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69901">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:از شیوه مذاکراتی ایران ناامیدیم.
ایرانی‌ها بازی فریبکارانه‌ای با ما در پیش گرفته‌اند: در اتاق‌های مذاکره موافقت می‌کنند، اما در رسانه‌ها [توافق‌ها را] رد می‌کنند.
ما از هیچ کمبودی در ذخایر موشکی رنج نمی‌بریم.
ما می‌توانیم با نیرویی عظیم به ایران ضربه بزنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/news_hut/69901" target="_blank">📅 18:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69900">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24b53c400c.mp4?token=C5K5dCv8f60ZvPFjTEKnqEsQvziVup1Qdfxq672zG64rnkyLzNVOdMTo9Kn52Ba4AMPckLFFywANo9s6XdbVX11EVgbka0hsG_AWk2mscR1XeK2Hsin2acR9hLdeFS3W5Tzwwu_QeK1FrzUrNosMa4ubBNVIPu_6vYYvH42Cbsoai-AJLDbIhIs5nJGfsht_7I7aSTjVBPUzd3nN_vr-HNEqx5J8uAsaVwUABOJQxiS1y_jpKYbdQsoGwTjbLDQ7eTkRgiG4BN5VVRO85B-bCwmQr5JkHX72PHE1Op_opIbPwopnZ56VrhzxRCKqiq4SgveppQWlD__cuznUL2zAUwvBACeV9sDa4RBP0WxaMpWi4HGvTyywcKcGlUxMfA_lXtGFXpLMUXIwNtexJ659jpFSXD4aN7qUW6nQSHFbOUSESiJH_79__fzBaIOw_vQEVdKwwiVJQjigQf2BdbB8ee4hic7GR6fq4Y2um7-f22v-avIjg1MdL0dxe8sm-N-iiqerwqlFvJNR84wjVThBp8zAxOdy58Qox5KTbFFpkdXnotnFKXuFj0jDtYf-POD1x-LBTSz5n2xt3pLkULV3qHELdEM6VN8tDfOfHW0_hmiMucT0gRLHSYOjdh8Y9hxwbb4701RAjVuhlxFwfLGC16ry2D8VntHD0xMRZTgtGLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رونمایی صداوسیما از «قوی‌ترین سیستم جاسوسی جهان»
تماس با پذیرش هتل عمان برای جاسوسی:
@News_Hut</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/news_hut/69900" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736f2f73f3.mp4?token=Fr18eSrt-8ecWO6VQxJWKwEIW8jy13hyTLRHl-e-BMq3rtIrWI47dfo77R77VWYAgTyCsIozQe1Ml260dBQlPPMGLQpAOR7DOX2lEINpk9jiY9-9fw4qdEqvGtPJkUyPFW_fkJylAq4fG4qYIgHQ5anWHrCga5kyBfrNLw3voQYk4KPannwJD1xpnepGBnYauyUS0p-T_oZ6WSi3MtdB76fgdTD_93Y5m7WV2wkWbwd7HEx19CHim9UbLPQEc3hIdUgmDfVtRlW-NohU3rEMjTpnQh01UcWqHVercnIZ3V4DmxjmqPWBXsQweU7ta3BDOPQIE7vjlGhSBa40CU6eyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
مشاور قالیباف، مجید شاکری:
هیچ کس نمی‌تواند با ترامپ به توافقی برسد.
این تیم فعلی با هیچ کس به توافقی نرسیده است.
او هم با ما به توافقی نخواهد رسید.
همه فقط در تلاش هستند تا "تحمل کنند و صبر کنند" تا پایان این دوره.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69899" target="_blank">📅 18:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c85bc1feb.mp4?token=dzUEO3U2pBpEr0vlRc_K1HKdatV-CorGbQzeyoVbr8RilpPXaPXnGW_mbkv79tmQsoryjs5S80u5xgCh0NVcQ69rt8HQXLBF-0WEsAY8mMFWqEsuZwvDSDkrCytXbWtp4GcTUncathZb5ijOq7WME75S2unX-HCrgAsApYTXDVd-OTuMU5ZiypHTEouqTrXi8YJL4ZvstabeBCX3vSreS4YncEfazekfkYigLL9MWi4SZ_jlUwC-ZETcO-Dun5Bnesau45aLPr_lLym8Q0vEgMtTIZyQOBEUmPLGYiBh7UTiwOuvWIATcrUybNfSkKjOPd1bx5NaFiexp123quREvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
نیروهای روسی تلاش کردند تا یک گروه بزرگ از خودروهای سبک را در یک نقطه تجمع، تقریباً 20 کیلومتر پشت خط مقدم در منطقه دونتسک، مستقر کنند.
همانطور که در اینجا مشاهده می‌شود، پهپادهای تهاجمی کوچک اوکراینی این گروه را مورد حمله قرار دادند و ضربات متعددی به آن وارد کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/69898" target="_blank">📅 18:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c9ff38ed.mp4?token=lPu7GUcIFMWRpxRITLehSIKfW6ksi7l0QCk9d3x7ywLp0HZyZtvDyZGLSV_UOzIBoLSOvfwmpoTx0Jw7iCzmYw64IPAow1F8zAwt3_c6yQc25uAMrH5BIJF6ES2d03DOrlvhrmO1fXO-mWXW7JEaOte71uCxV7AEJBlKVQT-j3Y3gBrD6IIyay8J43LhI2chfAW7AWRsJk6p2qFmVKzggv1jEwtNWa5wwYPH7STU5RKRUjhkbk2LTr4AJrAJQMaZqpI1hE2FgJ7O0FuTZNIIlZ8cjN1NdXrSvgDlnONWvpk9ovk4fs1UPhxtSTL7U0rYLC61OGO1lKSpTB23ofjPow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سامانه‌های پدافند هوایی «اونجر» (Avenger) و رادارهای «سنتینل» (Sentinel) ارتش ایالات متحده در نزدیکی محل بازی گلف ترامپ مستقر شدند تا پوشش حفاظتی کوتاه‌بردی در برابر پهپادها، هواپیماها و موشک‌های کروز فراهم کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/69895" target="_blank">📅 17:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69894">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01f4acff5e.mp4?token=gA7iENkfM9tF17WNCrCsyZeITH1stldmNNt1cZv_Uwn_2iB--LfLSqOteNaOdUAuNgawKAGZGcO16qQ42zTXeiB4thzMCOPMhIOcZIuhBM0hSGIJoEmFm30a0wnQUyTUFE_1uVl-uJg5gC-KZgJUVdM_d239PRgf_Smq_c-wrhpMuRWV_Na14LLzopySK6VYkiBD4oazCZMXcnGUTtY0gdoiFC6xv4N-Z6gdNwfEaoxcDfXGRFEHtiaVgL1Q_lzyF16NxqbE7TNC8kg93nyvhqq5qOrjKirQY1dn4k7mm8iQn7EL6v142dvEvuIQq1yOMz6n2mN8jiy0AE7v38XT9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیشب توی تهران، یه نفر با یه دست رانندگی میکرد و با یه دست فیلم سوپر میدید
😐
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/69894" target="_blank">📅 17:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69893">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDNB0EVzqzqMfUgalQ6xd2FlmnlFxdRgd2zmUovzqh8VwvDwOORoxM9PEsN5V_bpgnk1Hp1G5j8wNdGkYqf1NL9oxaejEqYFmZg4WJee2Yc-FB11V139fqA5uMg4yO-VtQ_pFWPPk3uwKFwYhHnjf6YBpgdFu7noyC8hy9MCvNZg8FMJuVAj0EXYb3M7WgBlEEdHASPG_8rCbrh4OHhW01yyGRFtWv7guKdQFKCFcSnOeiT4vbkImNFEV0bxChZVtpjKZzGceTq0e24orGjWhQ7QrAgZpqz8pcxZWYEUYlV7jTBB2S6trNN_6ah5CWvswCvI8P9aArg2uTVDKdUaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال:نیروهای آمریکایی بامداد سه‌شنبه به سوی شناوری با پرچم پاناما آتش گشودند؛ این اقدام پس از آن صورت گرفت که شناور مذکور ظاهراً تلاش کرد محاصره دریایی بنادر ایران توسط آمریکا را بشکند.
پس از آنکه خدمه این شناور هشدارهای مکرر نیروهای مسئولِ اعمالِ محاصره را نادیده گرفتند، یک بالگرد نظامی آمریکایی سکان کشتی را هدف قرار داد.
خدمه شناور در حال تلاش برای انتقال به یک کشتی غیرنظامی دیگر مشاهده شدند.
در نهایت گزارش شد که هر ۱۷ خدمه کشتی در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/69893" target="_blank">📅 16:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69892">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VooULoBmfIZORG4nwH6kqwAV7BMpjyAI0FcqeClRoYU3MiUmAjTUnP09jcPlzty2bS2-axH09yTOiAgdMY2VqzJszCKfblukEIaFu33wYQu9b27BwdNNp4isiwCUrpm6xzXhcrfQ65znwd44QjMPAk0lTChhZLqLYCTG3iGai5B5HQZI-20bD-_-YNWS6M1s0tuwjlKE9ANKA0bYwLDec7TPfnfPjbmfYZ49chCkFlHwjhoZ6WqjGXfXPq5Rx13KOYWhpCfUojtxZ7IQY9b3uJ1VgA2-bzwKjP9v4JGZSPM0WAZK-_jGllB3qc_eglqv8DR9lwZUa_zwzA3aKqzNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📚
#فوری
؛ زمان برگزاری کنکور مشخص شد!
صبح پنجشنبه ۲۹ مرداد : کنکور تجربی
عصر پنجشنبه ۲۹ مرداد : کنکور زبان و هنر
صبح جمعه ۳۰ مرداد : کنکور ریاضی و انسانی
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/69892" target="_blank">📅 16:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69891">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=MBjmGItyz1jseoM0JhB4XAZRi-QZqc4p4Z0kAZCT8o2vdQ6cq8VV_STxKeltI9SdMuI9yAFhEHbud3YZmdADpbpvavH0MpY3LZmFGkCJDE68adw-8DWwzUNQaL0xS2NwYHHjHeAEWGT4KVQUgfC7E4NWyWxUE-bfpnyWJSmUKXjE5FOsHLWvZzRktCW5DMEsRXQDKX1fHb4yw1yB1iVn_HTNnUaJCe39hjHazo61_cCcbWdqMIdWq5HYG7SxlMlCphGpSkRTaB8yXHf3azp9alUxLt-Apr0Jd1iqhNdbZK4eoNuB33koF8keVkUGGU8Ktu0bL2AIuubF7_mmgQuZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62f8b2cd3c.mp4?token=MBjmGItyz1jseoM0JhB4XAZRi-QZqc4p4Z0kAZCT8o2vdQ6cq8VV_STxKeltI9SdMuI9yAFhEHbud3YZmdADpbpvavH0MpY3LZmFGkCJDE68adw-8DWwzUNQaL0xS2NwYHHjHeAEWGT4KVQUgfC7E4NWyWxUE-bfpnyWJSmUKXjE5FOsHLWvZzRktCW5DMEsRXQDKX1fHb4yw1yB1iVn_HTNnUaJCe39hjHazo61_cCcbWdqMIdWq5HYG7SxlMlCphGpSkRTaB8yXHf3azp9alUxLt-Apr0Jd1iqhNdbZK4eoNuB33koF8keVkUGGU8Ktu0bL2AIuubF7_mmgQuZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یه آخوند توی برنامه زنده داشت به اجرا نشدن قانون حجاب اعتراض میکرد و میگفت ملت بالای ۴هزار تا پیام دادن برام؛
بعدش گفت بزارید یکیشو رندوم براتون بخونم:
چیزی که خوند
😔
:
«آقای پفیوز احمق بیشعور حرف دهنتو بفهم»
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69891" target="_blank">📅 16:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69888">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=p-VomaNDYZlvT2IYbbEW1cDa7JefcGz3HvPO5tHsIm6GT-ljFJQvKit8NJWtY4qBeRq3I9QiNQfnBdChIQo5-R6SS6i0IPgFuZs_oB3_8sDJsOGGh4pzLAtzWo5pYu7koEPTPE_SmYuD4TPFIAOUZ1QmbC-CaD6dMMx9Elvga4MxiikJcEKdfwEqJdtBJHEew17n9gVRSM1upZ0QeeYiqpGar6cb7E1exZX7iygbyKdij-4TdVdR2OD0XcNrTx8SWZA1tvAcsezV0N-lRnlsZnSIyXQxJN9e5efI5TTXWZh5FpJSZJTG-bGU5-U9_xu5uP0AJZPl-nBu13ddcFyxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698b90aa95.mp4?token=p-VomaNDYZlvT2IYbbEW1cDa7JefcGz3HvPO5tHsIm6GT-ljFJQvKit8NJWtY4qBeRq3I9QiNQfnBdChIQo5-R6SS6i0IPgFuZs_oB3_8sDJsOGGh4pzLAtzWo5pYu7koEPTPE_SmYuD4TPFIAOUZ1QmbC-CaD6dMMx9Elvga4MxiikJcEKdfwEqJdtBJHEew17n9gVRSM1upZ0QeeYiqpGar6cb7E1exZX7iygbyKdij-4TdVdR2OD0XcNrTx8SWZA1tvAcsezV0N-lRnlsZnSIyXQxJN9e5efI5TTXWZh5FpJSZJTG-bGU5-U9_xu5uP0AJZPl-nBu13ddcFyxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترلان پروانه توی آخرین مصاحبه‌ش گفته رابطه‌ش با شروین حاجی‌پور یه اعتماد اشتباه بوده و این رابطه تموم شده.
بعد از این مصاحبه هم شروین یه موزیک منتشر کرده که خیلی‌ها معتقدن حال‌وهوای بعد از جدایی رو داره.
جالب اینجاست که اوایل رابطه‌شون شروین توی یکی از موزیک‌هاش گفته بود قراره تا به دنیا اومدن نوه‌هاشون کنار هم بمونن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/69888" target="_blank">📅 15:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69887">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=C8moe2I4UqswvFSUvAHcxLZ6lw2_LZx1X3K9-jdyFTnX6-lhsEZ3MW_800dA2f0wKiG9k6MCXnUMM5jwOV-Mk91TQACOLI7gAUNURHuWUOsfSQfxzaW_SQMxx6gGrmlJhmJfXP8CEUNN8EPCOzmgIuKU3c1aSgH7alLkI7M2ie8GxVX_lW9zibOGRVd2OTWmMF-HIYOtyBL2bMiyyrJFX6Wxawx5axF-4J5orRiDj5-ndS-BjlYF8cLajDq68dxqf7OaOTmmW9g-S5dFcO1rukWIOeGXCIe0rwnMqLUR792SqQFsfgjO4rRK2z0ZZlaT2Ex8kb0XFB4gHX-g6kMlyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e9aa8412.mp4?token=C8moe2I4UqswvFSUvAHcxLZ6lw2_LZx1X3K9-jdyFTnX6-lhsEZ3MW_800dA2f0wKiG9k6MCXnUMM5jwOV-Mk91TQACOLI7gAUNURHuWUOsfSQfxzaW_SQMxx6gGrmlJhmJfXP8CEUNN8EPCOzmgIuKU3c1aSgH7alLkI7M2ie8GxVX_lW9zibOGRVd2OTWmMF-HIYOtyBL2bMiyyrJFX6Wxawx5axF-4J5orRiDj5-ndS-BjlYF8cLajDq68dxqf7OaOTmmW9g-S5dFcO1rukWIOeGXCIe0rwnMqLUR792SqQFsfgjO4rRK2z0ZZlaT2Ex8kb0XFB4gHX-g6kMlyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود هواپیمای F-18 بر روی ناو هواپیمابر در هوای بارانی.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69887" target="_blank">📅 15:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=n03_xE3asT670BsnXZghShswKCySLZsIh2pyLJ_IZPZ4mZ2TAwGrXJINGMc4RnIWdTZMoSHRUN_2NiY38XxaRr-gUGpfIOhByA-a6PSeaU7sZFoFVC9BtCs7GMoBgeM0pX38VfXoqADvnODNusIx2Xl2yw8bw2NfBUYDqlP-mbe6rfTCTkbAz3GU84eSr-VAxsQdgKt81y84s3IRWUQbQs-TO_HwdjAJEhaJbdIRxHuCZGphvhk3ejtQjWGOi9IcLoZNrL5cNPrZmfFJ4n4cmwLQdTuBhVXqeSjenOS0hN8eYY-JSuM8O05cVJpJ1kfNNzqf0GwEvS4pFTnQmRcYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=n03_xE3asT670BsnXZghShswKCySLZsIh2pyLJ_IZPZ4mZ2TAwGrXJINGMc4RnIWdTZMoSHRUN_2NiY38XxaRr-gUGpfIOhByA-a6PSeaU7sZFoFVC9BtCs7GMoBgeM0pX38VfXoqADvnODNusIx2Xl2yw8bw2NfBUYDqlP-mbe6rfTCTkbAz3GU84eSr-VAxsQdgKt81y84s3IRWUQbQs-TO_HwdjAJEhaJbdIRxHuCZGphvhk3ejtQjWGOi9IcLoZNrL5cNPrZmfFJ4n4cmwLQdTuBhVXqeSjenOS0hN8eYY-JSuM8O05cVJpJ1kfNNzqf0GwEvS4pFTnQmRcYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbTS8WBs5qKhTj6UpCLJj008xm8WI7bwPPnFmR-NEJEzIhhcFH2Kg_UFC35DoOjEyytYl2FQwV2hh0bVUBzod55TapzYYIicQD0SOBaHeGiUVLu2VzXkveZBzz6bzFAEYbne3zZyiXPTyqmnoUmabruH_4AUd8nUml2wm0-XVJjGnUKIep0jzcXJeGSmzt_rfNZT8nwAK_bJOTSZg2zkaMVoaQqy6zCP2XW9mPj71VVazeiPG9eyyHLAB1I5Ay0JX8IL8rHcEzhD-PmFQBAZtNHjfaN10JsaJPWcFfgGsT1mYW5tHP8jaXEL3BXhy3n2ojoE6oINRmodl4zzch-kpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=QDmc7BEKxzZFjGS-X5YRclZjIeQmXpJW07WH4dqEbAg9bg20ORRIVxQ377F_MYBH2LlcdmD6zaHlYLvh6HAFJoJJUas6w_oIP7XobMRaEJ_pZ_ijkMTu5mnmJUkVJuSUjSeuWkPnDzJ2P8d98AM_o5YgRr-AhM8ASziP7bfQJAoRxFdEe26BSc3LkLycuyGUA2C7NziozW4I8cOPSgk3a_rqZ8KdM0lUdU_t9Xi0Wv7KLcezMp0-UZxa7shXCnNhLWoGg1NCEzEDF_3gRQ0wxbBuWWgrDHysmXtDtz6brtgOOHfCwaTKySDuA3a49g5q39_HENw48M1fdI_ZR9Vz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=QDmc7BEKxzZFjGS-X5YRclZjIeQmXpJW07WH4dqEbAg9bg20ORRIVxQ377F_MYBH2LlcdmD6zaHlYLvh6HAFJoJJUas6w_oIP7XobMRaEJ_pZ_ijkMTu5mnmJUkVJuSUjSeuWkPnDzJ2P8d98AM_o5YgRr-AhM8ASziP7bfQJAoRxFdEe26BSc3LkLycuyGUA2C7NziozW4I8cOPSgk3a_rqZ8KdM0lUdU_t9Xi0Wv7KLcezMp0-UZxa7shXCnNhLWoGg1NCEzEDF_3gRQ0wxbBuWWgrDHysmXtDtz6brtgOOHfCwaTKySDuA3a49g5q39_HENw48M1fdI_ZR9Vz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=mWnf5cZEcjEeGDq8z9C5OUtsbhgryxre5E95SQN4wlO43Mlvi3n4daDVV0uNm7zt8jCNqBnwCSoTdWbgaorSwNbzHPCOnruPkT58DMuEJjl7vHyOeUbdNl2u4PrUCdGLGNbNXmyAaV4fMHmDQdExNsBIyubUZ09dhoo9dB1xakQhG75Sie9JeHidX2tE9LVvqh9y8-O9BuYuyR7EzX5BlYOwK6BkyLDNNrKcsHGt5TewcC6YmpVSXVONNvq7cssvVkYuc2jSDILkZlf5vcXDJwnImUVq_6azcMXhHx2IY8rb0_pHy8Vb_7uq8nGd9NwFCd7Nyimf663XybTV8oYPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=mWnf5cZEcjEeGDq8z9C5OUtsbhgryxre5E95SQN4wlO43Mlvi3n4daDVV0uNm7zt8jCNqBnwCSoTdWbgaorSwNbzHPCOnruPkT58DMuEJjl7vHyOeUbdNl2u4PrUCdGLGNbNXmyAaV4fMHmDQdExNsBIyubUZ09dhoo9dB1xakQhG75Sie9JeHidX2tE9LVvqh9y8-O9BuYuyR7EzX5BlYOwK6BkyLDNNrKcsHGt5TewcC6YmpVSXVONNvq7cssvVkYuc2jSDILkZlf5vcXDJwnImUVq_6azcMXhHx2IY8rb0_pHy8Vb_7uq8nGd9NwFCd7Nyimf663XybTV8oYPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=setARej3TUu-2HFoVM9bQr96Y3nCyQgNPKBEeNv4fPUfBRCvV_FkcvkcjowkcbTQbpUzNxPYqE_V2zsdQraGh62bCYxMUvWgpW1Piy5MXtTAlpA6JHPd7VReNSXGgDW4eIyDRxKlqXzDUDvulePQJBZlnHLbMO_iU2QFNY_IOfUFThDyfLfdZ2i__n43wi0txuey5w8iMdrzUNPDw7uHg_F1emq2GeGrg6H7umVOIfIMg9piGX1aCRVXBxPR0MsGRo0vuTbt7am0BgKQ71BXeBKIZKL-xgqKFUEYMZ5As-OEcEwPjSRJu8UC91Pvx4T0_M2eNmKj2zZ1pgSt6R3PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=setARej3TUu-2HFoVM9bQr96Y3nCyQgNPKBEeNv4fPUfBRCvV_FkcvkcjowkcbTQbpUzNxPYqE_V2zsdQraGh62bCYxMUvWgpW1Piy5MXtTAlpA6JHPd7VReNSXGgDW4eIyDRxKlqXzDUDvulePQJBZlnHLbMO_iU2QFNY_IOfUFThDyfLfdZ2i__n43wi0txuey5w8iMdrzUNPDw7uHg_F1emq2GeGrg6H7umVOIfIMg9piGX1aCRVXBxPR0MsGRo0vuTbt7am0BgKQ71BXeBKIZKL-xgqKFUEYMZ5As-OEcEwPjSRJu8UC91Pvx4T0_M2eNmKj2zZ1pgSt6R3PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dRI5baYmi4hbWk_YlgNVc73JlbamEyfzRmRDtsrzUjRpJc60nkccZaPiwjKD-m04Ab2cY5_cP2FuMdvzJYkSiDgAR7Omstg6_oHQJfOD_iHvX_Qj3Bkhg_GMxfHcqndWbHqKcSlnE5XdHtyXNhKPv33jxL1qSlwoWsDhKVA0O_ENivcSG17WfoH2e-3fQj2GxTZpSf1XyD_FOX6qs4MjFg_XIi-T-3jRoCwMo8fafiim7WdLhQJhR86oAT65PkjTLlSR0ubvKhjjRuIwqrz1PUtTqUpyIxFqHxZcVsDLDK534gq11MQrQMbgF-G9ivM87YEPeq7EKDR_ZnwhmLY14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dRI5baYmi4hbWk_YlgNVc73JlbamEyfzRmRDtsrzUjRpJc60nkccZaPiwjKD-m04Ab2cY5_cP2FuMdvzJYkSiDgAR7Omstg6_oHQJfOD_iHvX_Qj3Bkhg_GMxfHcqndWbHqKcSlnE5XdHtyXNhKPv33jxL1qSlwoWsDhKVA0O_ENivcSG17WfoH2e-3fQj2GxTZpSf1XyD_FOX6qs4MjFg_XIi-T-3jRoCwMo8fafiim7WdLhQJhR86oAT65PkjTLlSR0ubvKhjjRuIwqrz1PUtTqUpyIxFqHxZcVsDLDK534gq11MQrQMbgF-G9ivM87YEPeq7EKDR_ZnwhmLY14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCL5pMj5gRmRht7322033OL9hKO1-HB7_FUuWqlTAWmsQ9wo80tVVXnDMc0MyyuUcA0SvzjMXm2r1cIp6xuB5J8-l5Q5Dp23hps7N45DuVpog46vMIo3Itt1RO1D_Umsj8-RB5Y1bbWMO6TljXTMEQde-J5DIjCfu6gNJEFAMZBXtPW3GJnNhk59jaFvYj_6wGLX__41F1xWRNdltU0NE5yvtRg-HvKRylxvUWqMRZqocM4zuGOAVrbcGWt-GAhmCyASxBOuqKllp7IcSZOS6IbK5wu-8aGiGUpPKOygequn9i5rbKvcyv8ZJ5pXNnIjexfilMnu0atC_yOtWKILJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=lAnIi6utS7j7Ke_TxJ5VQ4bTYNg9--354N1HBVq0BhJ2gfOfdZH8X4fjg9JMNHbX9r_V0HRD7DD1uDS_aMWQLe_0ftjzMqrGuP8tXrcAEMeQ9Do1A-Q8zaaaycKCQOQUDXqn3LGYu3mD9vYIRbLk4wDK-DNG4H13MBVWux-hBgzO9r4uK-wJjN-W0cgObqONk6lCD6qOwfmnug-s8Nn2ScTZHBsgeOxkIkRy4dW1N6UmsGE188Niu2WlLQLyGmFeP1AZAHGNFDWu3BbkMxFqYPbB7NNpNlfbVL95YH_ZI61YYgzCX_47YMgL34mdBbCFimljEowaDVVORNKK_6QbIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=lAnIi6utS7j7Ke_TxJ5VQ4bTYNg9--354N1HBVq0BhJ2gfOfdZH8X4fjg9JMNHbX9r_V0HRD7DD1uDS_aMWQLe_0ftjzMqrGuP8tXrcAEMeQ9Do1A-Q8zaaaycKCQOQUDXqn3LGYu3mD9vYIRbLk4wDK-DNG4H13MBVWux-hBgzO9r4uK-wJjN-W0cgObqONk6lCD6qOwfmnug-s8Nn2ScTZHBsgeOxkIkRy4dW1N6UmsGE188Niu2WlLQLyGmFeP1AZAHGNFDWu3BbkMxFqYPbB7NNpNlfbVL95YH_ZI61YYgzCX_47YMgL34mdBbCFimljEowaDVVORNKK_6QbIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=iI91T19qeTaQy0blK40at6aNN9sWsvXzDqImLb1k5PRv48ClVakbIS28L-wiXkFjwKtEhxrPgWdrgFg7Fdads6DWVuvweUVIVWjdsnyl40YFzrNNtluAWoD4umytzNeOmkcV0tGH1jV5U5_dfuPUnHQ6x919RwSZVBBlzzLBDMib1XiLgdDtgHwbXqWbYo1sKHl532B3lkO3p4BKL9HKRSo_HCP6O-m1AxTxUCN_y-pm52SSFcqeBZnzzl-z2Aou0RBDgYxGSQM9vm4Fhr96CKY1Ky5TMMr6Y4QuNaN4BKZ5oBcVZY9BdwHiuap63pt_xjnLbywqw7eiblHnYu1whA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=iI91T19qeTaQy0blK40at6aNN9sWsvXzDqImLb1k5PRv48ClVakbIS28L-wiXkFjwKtEhxrPgWdrgFg7Fdads6DWVuvweUVIVWjdsnyl40YFzrNNtluAWoD4umytzNeOmkcV0tGH1jV5U5_dfuPUnHQ6x919RwSZVBBlzzLBDMib1XiLgdDtgHwbXqWbYo1sKHl532B3lkO3p4BKL9HKRSo_HCP6O-m1AxTxUCN_y-pm52SSFcqeBZnzzl-z2Aou0RBDgYxGSQM9vm4Fhr96CKY1Ky5TMMr6Y4QuNaN4BKZ5oBcVZY9BdwHiuap63pt_xjnLbywqw7eiblHnYu1whA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=kwbcItVEe6WsZZzF5O5trVUT6LMDUkhU7_NeVqBKK65b4WedGCnpK62KLxUuSUGdXyFU3mE0x4ALQUP6kDnp7HVEaetn3GPH7W61yvgEYs3LpCCfSbAzlYIomHojfyUald0hrc5AgVPg1kNCWyeo7ItpR11_RHEqOaLaR2wLyH3Bu69hqL6kuJsUn0gsWA2lYsZRj8TN9PzkrPp3W0VPBq4yEttPOZxV_CN4tbNLlQcJUlZ4mk9ThwPgv0Hu-XKZ2UqJLh3dS7PxWY3YA8BNTcEBFR-z9jmXmzD0UIfrEXxGHKuoNfnXvjLyVnwkBxZg8PP2h68E2LYlupZk-B7anQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=kwbcItVEe6WsZZzF5O5trVUT6LMDUkhU7_NeVqBKK65b4WedGCnpK62KLxUuSUGdXyFU3mE0x4ALQUP6kDnp7HVEaetn3GPH7W61yvgEYs3LpCCfSbAzlYIomHojfyUald0hrc5AgVPg1kNCWyeo7ItpR11_RHEqOaLaR2wLyH3Bu69hqL6kuJsUn0gsWA2lYsZRj8TN9PzkrPp3W0VPBq4yEttPOZxV_CN4tbNLlQcJUlZ4mk9ThwPgv0Hu-XKZ2UqJLh3dS7PxWY3YA8BNTcEBFR-z9jmXmzD0UIfrEXxGHKuoNfnXvjLyVnwkBxZg8PP2h68E2LYlupZk-B7anQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=ao13aT2K1HMF16Jxny5pvd5p_9s6GT-N1z1A8IC0bg5pgeMBFIC9bypgJt_e-sncuTMk_MbCqQ1quoA1otXrn1UU2Z-a21BDq2eipmUnhDctBUK6LpRKjZMu_WdUkK82vsVLVyov8exRQWgvQa5Us69PlnaAWgp5KkeLq7YQrnfNZ_xXmYdGU30NZKvyaB9PJJg8xzUBJ8yvsScKK3STd7Xksf9m6fyP7qCqY5XOgQGdpLxnJCBJpbXVjYdwHIS2B_oWtW4OnRRTTZCES_TvqKPaZ79POribqt6btpNraZGh5Qoj9fQd-DsaLOgmfeQqNbgfeEhXW-2pLFJJSws8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=ao13aT2K1HMF16Jxny5pvd5p_9s6GT-N1z1A8IC0bg5pgeMBFIC9bypgJt_e-sncuTMk_MbCqQ1quoA1otXrn1UU2Z-a21BDq2eipmUnhDctBUK6LpRKjZMu_WdUkK82vsVLVyov8exRQWgvQa5Us69PlnaAWgp5KkeLq7YQrnfNZ_xXmYdGU30NZKvyaB9PJJg8xzUBJ8yvsScKK3STd7Xksf9m6fyP7qCqY5XOgQGdpLxnJCBJpbXVjYdwHIS2B_oWtW4OnRRTTZCES_TvqKPaZ79POribqt6btpNraZGh5Qoj9fQd-DsaLOgmfeQqNbgfeEhXW-2pLFJJSws8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYUI2pJ4mSEIyM84cxFfSXNmZaKxrrykAy0wpMPDhBYxz4HDLdoqs5BhRdDdtpcuiNjiWYnlIkm3EJ9sKm32xgv4TJFwcoSoO3s6Ud-ohLi1OEGRN2z4RhjZ-jgdeu8D7rZFTwz8oTPdZsnOLbPGBCQehkLnAEmKP1PGMLGW5PAEZTopYMxNoEwZS4xahUkvt3V8Yp2WwGkhEcLwBtZtIFKcsu6Rt1onmkvz7ABjs7QQzWNDEeXYDBSpRNfEzck9HIQ8ekl1pFVV3WQzQgBDNLqGwvwNQt9ZSllZVjoE5oZW_eYvAC28jeYcFcyk8ebAlSKxnxPaUEwaL_OPjAZOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=O6PrhSFKJXpIxBPO7WbkNnmsq6F2JVI6CXEptV1ttkXggMaqwLy8zJp95g7kQMwEzispqcdrwYqj-1WkZjLkEnP8Uh2TN7lSu96_4IlnkjBUEl9shWUHGGAaaWlwE4e1D6EnrXrfF5UutGAwQcCYU6tFgT7x-aSF2diYkA_QxPDwtV-rxErfReTV51J1TQq-PTRJZ3f_EkJGY6Jo4O7Mwi07hw-n9cwup4krNvJRVnrcGwrWJSsiIXM551uEt53SdPjYCiPH1bA93VJcJt4kjacQ_7avhE5GOYkGTX1C5KD4ktNhrHvtVog-ZOQJ1HbeJhBorJpz71FXVsR6sFtjdLNjcGI-hjCUe6qdmwls9xBKImNPgC7rC-xutfviDfYyKLiSusTe4suc7JY9-s1F3ByTH0SndSe5RY6WNe3uHtuWRwWc6Gsc2cXVxcqQtVVPwxjg2v29B6_O_6gk3jvN6pvUmdKqXMbEiKy2vDdsz3QIr_tbTcEC5_oqb2_0Kb52ZNLflyWCEej2uKIlDNi_P4rcNNc9RE_Ow6vfhaI5I-OgPZ0ImuwxOWzj0S6Qe0BNxw6A_PKcnA8CaJ267lV4-8Rc2n2kWKOFxfl64UwFetaUUUJh8WabdUr_FooZwyckVpfg4VYyW95b2V7jYJOxDEvfqhcL8NwtoZqg5IF07n0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=O6PrhSFKJXpIxBPO7WbkNnmsq6F2JVI6CXEptV1ttkXggMaqwLy8zJp95g7kQMwEzispqcdrwYqj-1WkZjLkEnP8Uh2TN7lSu96_4IlnkjBUEl9shWUHGGAaaWlwE4e1D6EnrXrfF5UutGAwQcCYU6tFgT7x-aSF2diYkA_QxPDwtV-rxErfReTV51J1TQq-PTRJZ3f_EkJGY6Jo4O7Mwi07hw-n9cwup4krNvJRVnrcGwrWJSsiIXM551uEt53SdPjYCiPH1bA93VJcJt4kjacQ_7avhE5GOYkGTX1C5KD4ktNhrHvtVog-ZOQJ1HbeJhBorJpz71FXVsR6sFtjdLNjcGI-hjCUe6qdmwls9xBKImNPgC7rC-xutfviDfYyKLiSusTe4suc7JY9-s1F3ByTH0SndSe5RY6WNe3uHtuWRwWc6Gsc2cXVxcqQtVVPwxjg2v29B6_O_6gk3jvN6pvUmdKqXMbEiKy2vDdsz3QIr_tbTcEC5_oqb2_0Kb52ZNLflyWCEej2uKIlDNi_P4rcNNc9RE_Ow6vfhaI5I-OgPZ0ImuwxOWzj0S6Qe0BNxw6A_PKcnA8CaJ267lV4-8Rc2n2kWKOFxfl64UwFetaUUUJh8WabdUr_FooZwyckVpfg4VYyW95b2V7jYJOxDEvfqhcL8NwtoZqg5IF07n0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=jkOvZs-u6hU3SxYJQNPbzwFY_RJ4r12vXtFoMUFsg13eicYElQSjOsLk_k0Gc2_jUitTooI0CCbqF7DyzVeU-Oki6LgHtdFQ5HmF8ufShErvJS9OZUYysXjKCmuDRXHnZAuEANxOG1mcoDbR0_V5xuuoK6Th423BWjKA7q-jOm3QzxB1C9PagoVHfbC7NP4qwv6p42rVd-mnWUhPpeE3Xl1h37xr9rnthRyJNj8dKMbijMMac5fXvITOWLAtUA_H-F_q95-uVzDHtME2XiflOBFyYidO90XkS5ZMgzq0JAeZTIOAWInQz9v10vJIltlbTzOeilmDLoBrlF113nAgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=jkOvZs-u6hU3SxYJQNPbzwFY_RJ4r12vXtFoMUFsg13eicYElQSjOsLk_k0Gc2_jUitTooI0CCbqF7DyzVeU-Oki6LgHtdFQ5HmF8ufShErvJS9OZUYysXjKCmuDRXHnZAuEANxOG1mcoDbR0_V5xuuoK6Th423BWjKA7q-jOm3QzxB1C9PagoVHfbC7NP4qwv6p42rVd-mnWUhPpeE3Xl1h37xr9rnthRyJNj8dKMbijMMac5fXvITOWLAtUA_H-F_q95-uVzDHtME2XiflOBFyYidO90XkS5ZMgzq0JAeZTIOAWInQz9v10vJIltlbTzOeilmDLoBrlF113nAgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=b34SIecnCfHFOZWSKejpzpxNg0OXxWEbQvcKcK4Hn0hbi5L0SzGk8jVOqx_JGoxYJeGZQREfe99utHBFJc8E8SHLpuWUD5-1b5hFg3Qc2o-P2nFZEZk8UJbtpxA5jiYm_xKq0wRQeOgCk7J9P1qz-2m14TdzjiD0QejqQilel5de7Lmb4O6zsckwgoC7HescuAnHKz1ysWFV9JVTigG4oFs9EyYSUMBulQP9kqHwlaKbA-1JywPHSlFcmz2a0gp5LL8IqkT1BPObu1zsjMbj-abfGwgh1gCjohbR1Qd_vqNz3TpfO4XGT4lJu1HlsT3GYb2YyqjdTgA6DGsEl36CJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=b34SIecnCfHFOZWSKejpzpxNg0OXxWEbQvcKcK4Hn0hbi5L0SzGk8jVOqx_JGoxYJeGZQREfe99utHBFJc8E8SHLpuWUD5-1b5hFg3Qc2o-P2nFZEZk8UJbtpxA5jiYm_xKq0wRQeOgCk7J9P1qz-2m14TdzjiD0QejqQilel5de7Lmb4O6zsckwgoC7HescuAnHKz1ysWFV9JVTigG4oFs9EyYSUMBulQP9kqHwlaKbA-1JywPHSlFcmz2a0gp5LL8IqkT1BPObu1zsjMbj-abfGwgh1gCjohbR1Qd_vqNz3TpfO4XGT4lJu1HlsT3GYb2YyqjdTgA6DGsEl36CJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=mGN4rgbKKvwWfUgr9jG-aBEcW8fkdsgcQMf2ss5IHQa0aQ9buUVWrHfZTahKJLx3fJcPpGuasIB5suPuYRpr_IUzf9P4qAu5qOp6S3rxOgP8h9nKSh7KwEH5QQyW4JkP2ezekV5hApVTr-w9PBJtFoJ03pMwVgNb3fNuf-tsZfzQtP2CXCT-NyBu-O101sTQWTo43y_JnAXFBQ8ZB26EAWUt84YBahojZzj6Tk-pMKd9YKUDmvBWue_ziECnKdhfRxxudOsshxu6urTUR5RUxtfaptbTGvp2RtfqnGIgRQcM68TN_YMm22iYndVqQBSLGdWnoeYRwNYvLSEuqNR8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=mGN4rgbKKvwWfUgr9jG-aBEcW8fkdsgcQMf2ss5IHQa0aQ9buUVWrHfZTahKJLx3fJcPpGuasIB5suPuYRpr_IUzf9P4qAu5qOp6S3rxOgP8h9nKSh7KwEH5QQyW4JkP2ezekV5hApVTr-w9PBJtFoJ03pMwVgNb3fNuf-tsZfzQtP2CXCT-NyBu-O101sTQWTo43y_JnAXFBQ8ZB26EAWUt84YBahojZzj6Tk-pMKd9YKUDmvBWue_ziECnKdhfRxxudOsshxu6urTUR5RUxtfaptbTGvp2RtfqnGIgRQcM68TN_YMm22iYndVqQBSLGdWnoeYRwNYvLSEuqNR8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=W4iw4kISa7IIZ07wHeRuOsb6oe8xEz8-AY1pDM2m95gfHYzlRmNaH47Ekq9XTZCkVTh-XvDYFnY0c1cpBh-SuD2-RTeOz2lJ7eSp3ZE4EBoWg_Ln3HLHqB13Y7qvQYid8eM6plvxrbA2qGCEOfWNBeMXkGnrkuAE4oQjEo8Tv5laYH8zKcdSKB5I9aBxptAWiclx9-lHcUYKhum-0j5a3OMhgbPILkEfU64A29DHg14hAg6tO7dvTTetdB1IKU0X6OoyRYz-ZiLflbFV1RytAYV7Z0og60g6UF9htYijU29RCvL3WLSzVUXSSVKBv8BEsHsS3fqti573YIqSB74siA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=W4iw4kISa7IIZ07wHeRuOsb6oe8xEz8-AY1pDM2m95gfHYzlRmNaH47Ekq9XTZCkVTh-XvDYFnY0c1cpBh-SuD2-RTeOz2lJ7eSp3ZE4EBoWg_Ln3HLHqB13Y7qvQYid8eM6plvxrbA2qGCEOfWNBeMXkGnrkuAE4oQjEo8Tv5laYH8zKcdSKB5I9aBxptAWiclx9-lHcUYKhum-0j5a3OMhgbPILkEfU64A29DHg14hAg6tO7dvTTetdB1IKU0X6OoyRYz-ZiLflbFV1RytAYV7Z0og60g6UF9htYijU29RCvL3WLSzVUXSSVKBv8BEsHsS3fqti573YIqSB74siA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=tH2PFWVmoeUp1XQrbhKv3pe3rLSe_cpg3vgBARwIuuKJC4SIF1p4qxMn_JnvnrH-Q2J1oggAmE9ZqiJLgn828O-vmFiVqLtkmnF-Jp-rkz0oMyS1rbG_acofXdaShGlh7VxCTYq4BTcwOXdQsYs_jlV0-Zfi82f0raxBQsJNW26In_12TD5FtAlK_tWhXfxChad0STMgoWc3spk6NR4cPeNyPe-tAjfjRiAWhPYbPQgsJxj8KfPYsT_c5FKPhquEAMm54DchQ40Eoey9YCK9UtTDOka68HA71qwnCzvdxtva2UGw5kCvN__5cEtq0BSylokZXoipk7zpwHzno-XOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=tH2PFWVmoeUp1XQrbhKv3pe3rLSe_cpg3vgBARwIuuKJC4SIF1p4qxMn_JnvnrH-Q2J1oggAmE9ZqiJLgn828O-vmFiVqLtkmnF-Jp-rkz0oMyS1rbG_acofXdaShGlh7VxCTYq4BTcwOXdQsYs_jlV0-Zfi82f0raxBQsJNW26In_12TD5FtAlK_tWhXfxChad0STMgoWc3spk6NR4cPeNyPe-tAjfjRiAWhPYbPQgsJxj8KfPYsT_c5FKPhquEAMm54DchQ40Eoey9YCK9UtTDOka68HA71qwnCzvdxtva2UGw5kCvN__5cEtq0BSylokZXoipk7zpwHzno-XOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGK9KsCn-BfdCUhqmf0qluLV1nWj0ogpIQRWaOhfq6R47uPBdo3l8QXeNF1fpZSDNZY8pEuxoJRfXERIzelSBm_yuqGKBtagDh6ylKDvqlHYncjg3gOW4wvADun3FvQHGpM-JWRVuQXAKdHYOIyxbP3tdAozQ-fTQkXTrVNwxKE4xaKjzRji0Eg3w0XJYljDYqUZBtyA13wmq7FhkSEvdj5nIbNLHTk0vs7y4OJRJeYtTmu4uH8R8BAITyYfzXNc6_nozzp7650HayCFhxmWWuRZL-JiYcu_sURaiyuBvIFPMypUNwIS2qvrOuhLpLuBJnGVHyP-zZ6yj4kdLUdgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Gh1D3Awa34H_3Sh9QspAP4-ayqgXbk00ZwwUE2JlBRUMoQYtJhxeQaujaYO0tmK-kHUpK9at7UkbTOplFnpxonCm2grViA5QD6DnZ2ZjfdPyVEF6__RKaCg9jLHTp7QOJcrRMzOtEyTuzBelCJjOdRnoQHoDrpo5HzcxnhPoDBfW0m99zwMlKzf2pGk6IBhupMdehPTSowJPE5s7ySNXJOpHQ3e-ehzW-GKA3PkOetKIEXTfZzhvJBH40-jyqUPX3-jSx8eFiE01tvhGrpm1Yn7GKPsRPyW0gcG5pzRZYCf59ALUt0HnrZ-IAFdACFqIuccpfJvYttrEPp_CsJOW3WjNPSgiUKMOkBzAcv_YbOeP93xG_8zZUYGxYWCLHTBv6Tm_8F-HKBcjcHTtZ06wpdWUSqOTzlrEMcsf1OJUWK4WpqwnS0nNDxoWFMMINaphi3ZD5sbPvVRrLzRWYzp9XRlP92ILVtHWftGFBoZAbfJH0uuTICqgQmrO1Asnz34xoK9dFoYWzer0tIfaKdNZEZFTUywZbJShg4PvkswV1FRcawunILMJvc4WdMeWqGgeRmDjWJ28SLHU-nQBe1haDg0ooldnhO1QV8kIEpK4HAgcNrYO6ccZGfXb084RClA8r4gc0ekEkWcMPsg80wrzwleQJTjEsB1GJ7dU6hROskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Gh1D3Awa34H_3Sh9QspAP4-ayqgXbk00ZwwUE2JlBRUMoQYtJhxeQaujaYO0tmK-kHUpK9at7UkbTOplFnpxonCm2grViA5QD6DnZ2ZjfdPyVEF6__RKaCg9jLHTp7QOJcrRMzOtEyTuzBelCJjOdRnoQHoDrpo5HzcxnhPoDBfW0m99zwMlKzf2pGk6IBhupMdehPTSowJPE5s7ySNXJOpHQ3e-ehzW-GKA3PkOetKIEXTfZzhvJBH40-jyqUPX3-jSx8eFiE01tvhGrpm1Yn7GKPsRPyW0gcG5pzRZYCf59ALUt0HnrZ-IAFdACFqIuccpfJvYttrEPp_CsJOW3WjNPSgiUKMOkBzAcv_YbOeP93xG_8zZUYGxYWCLHTBv6Tm_8F-HKBcjcHTtZ06wpdWUSqOTzlrEMcsf1OJUWK4WpqwnS0nNDxoWFMMINaphi3ZD5sbPvVRrLzRWYzp9XRlP92ILVtHWftGFBoZAbfJH0uuTICqgQmrO1Asnz34xoK9dFoYWzer0tIfaKdNZEZFTUywZbJShg4PvkswV1FRcawunILMJvc4WdMeWqGgeRmDjWJ28SLHU-nQBe1haDg0ooldnhO1QV8kIEpK4HAgcNrYO6ccZGfXb084RClA8r4gc0ekEkWcMPsg80wrzwleQJTjEsB1GJ7dU6hROskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCryMxwQ7tObpVshmg39x4z9f_b1cC0oX_V7vZB5iEF1ZWcDnDG9IWCGs_agJHVd6ojkd4D9KMcjpuqYEogtvkiWM_QsvexZyPWge0hfd8GSEXtZuwoTHQiwuEKdDqxrBSAximumQdNMy1gaKPwwni2rbdp_kNjg5efEg8CguOjFvOs9Cl8LV0-VZR_k18HAYLAjf9vJd6IHAJuWaIpr8BFtscjL2nwlZO8vd7kl1UBVFkqUwv6eHpOW7x18U9QmvvXQgpBITtZ89tgcKQHxefcPtv-jG-Xtoz05X9qp4LcjpLL02_p3dwX-wzzE5K47zHZxE6HC9JAaCiCTwmz8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_JYhXfPuBkzoQWceLlhmbY2O_I8RUv0NVd-QxM8gt3_QF5ulEtnDfCqRHvku_-bCvp-Hol_MX3r0yLyoTvSi2TyYFvpYQFDyIVkwR6lQTA4gSkTOXVsPOn2-_F28fSFu-w2WiYyPM9wl5zSFc04Ncak-SLh64SSEmEcRCMwACd1RgTc-lV6BRi5Kc3kv9Dn4eMa6dkzLNTqNZMeXigtdKund0_XIeISGzmhLq2HBdGnfvBmM5zgFdnNBoxQh0Oa3ui079N9cbZ49KW37BSrLDxe634-ZJvcsv3jAidXethqrm6kCuofUqMfZA5Gp5N4KLYkRo5WYERtSESana0gbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=It_13FwSqKyrHTo8uYbUc-TJVtr1yp2lFI4OLUGFvLTpKktNLQ9G5e0CDwHEQAIegBaffYF1dYmzEHFuGna8LmrtM5m-k19JvfUxup1p8GTR7q6UuvJNpJYEdOjQa25SQxlK7yQpckWEMbhhME06GAi6yOKXbLeVC12VDSN38XymjkQuOEQjohJYEKupcYyL0RDlNb41HRWprohyRMA3l62ApE2ipHTQrG12NgrTn0FQVEZRG6m6jOisGa2I6BvDw3CEqCk97VAjZwbz25rHzhrXCwRbgyVvPrHCZSmPsg_rl4-lj9keUZcP72cc8hoptqYVXu6SV6iSaP-pi8kvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=It_13FwSqKyrHTo8uYbUc-TJVtr1yp2lFI4OLUGFvLTpKktNLQ9G5e0CDwHEQAIegBaffYF1dYmzEHFuGna8LmrtM5m-k19JvfUxup1p8GTR7q6UuvJNpJYEdOjQa25SQxlK7yQpckWEMbhhME06GAi6yOKXbLeVC12VDSN38XymjkQuOEQjohJYEKupcYyL0RDlNb41HRWprohyRMA3l62ApE2ipHTQrG12NgrTn0FQVEZRG6m6jOisGa2I6BvDw3CEqCk97VAjZwbz25rHzhrXCwRbgyVvPrHCZSmPsg_rl4-lj9keUZcP72cc8hoptqYVXu6SV6iSaP-pi8kvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAW4iPz5OkVvZ_gvKw49nOYBQBsRRj_CmKTLn_noftg9cUzcaD89fuCA4Vo9zKaGFMjngkV42xghC78D3cZZgKPe-sswesMILHe5cEFp6rimNkr-yPm1NTuh_atQ6cMEMqlk3yurA2RmZOHZpNyrEIXpZcisXWX9DhtPc4yoDhs647ydD2Nykg1jfFKFit3gQjMlIjRafM_YpAYt2xgFz_-rdiJgA3H3H7-vi-M71eyIGOve41Rnz8x62hDXgEZ0xAHVf-KKKvzROukR6-6t6YZ9Alyym18H4jJg3yKAnuOoSjMFmAUXZ9HHxaUD6BS3RUK7z4ZRumdq-C9yzU31Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=rG7Ct1GHVEvnSzTfUyL9B8nnEREn-fyqckn_lnI_8rlaiIJELqJWEo6Ut9SKEDW2S_1AqtBcH10WhuG0WrV9R9JP9YYIgBwpBh0gHmuYTIA-xkyRQGofvAL9gx0obEgY_QzxV2q7XnV1Bd3iVaBFRFt_MM1PdY_7wJcL_cLLNfZwt_rjpQ88QDBWq8JL57nzVzNaRlorq4ZNA_lE_N0LQ9GzayPB9-lW7nP0JgnFWnYXLYkMZJQw5gFbWykeR43-njWZ6MJiOW7VfvFd5uwEZDT_e3aiFJ6odygaziW-wW2p-FN28xLkUXJuynOlk0n_S1PF26oE2Tyl3h3GzVKe6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=rG7Ct1GHVEvnSzTfUyL9B8nnEREn-fyqckn_lnI_8rlaiIJELqJWEo6Ut9SKEDW2S_1AqtBcH10WhuG0WrV9R9JP9YYIgBwpBh0gHmuYTIA-xkyRQGofvAL9gx0obEgY_QzxV2q7XnV1Bd3iVaBFRFt_MM1PdY_7wJcL_cLLNfZwt_rjpQ88QDBWq8JL57nzVzNaRlorq4ZNA_lE_N0LQ9GzayPB9-lW7nP0JgnFWnYXLYkMZJQw5gFbWykeR43-njWZ6MJiOW7VfvFd5uwEZDT_e3aiFJ6odygaziW-wW2p-FN28xLkUXJuynOlk0n_S1PF26oE2Tyl3h3GzVKe6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=ftkS-Jw3Mze2P3QCxz0ULZHU2xzh7CiCrO1PdwaqYHZv_2DMpFGWHxe45RgSAMTreINafYgoUAzrEs5mjFOY5Nv9GyKnQLT68EhR1G4GVwo-GRGqW9DmeS1TwAf2eGt2css0r-6XVPtFB8hCUagCy5Vnmy_cr_8xdputLCqgyb1YzpovMkg_bzjK61EfeGW-MVXiDN_G5NzHprCyvRmjSxwOW9pruHyS7kwdTAEFCEsdEYA12vvtWh_U8RAbk7-cyvCzQki8AdVchYFjUBP5kGEKQ1S_xO1G_O4Agqk4jLL17e6uw0Z5yqrBqelvNt5NjHYL3quHIGZ_eDcuw4Pu3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=ftkS-Jw3Mze2P3QCxz0ULZHU2xzh7CiCrO1PdwaqYHZv_2DMpFGWHxe45RgSAMTreINafYgoUAzrEs5mjFOY5Nv9GyKnQLT68EhR1G4GVwo-GRGqW9DmeS1TwAf2eGt2css0r-6XVPtFB8hCUagCy5Vnmy_cr_8xdputLCqgyb1YzpovMkg_bzjK61EfeGW-MVXiDN_G5NzHprCyvRmjSxwOW9pruHyS7kwdTAEFCEsdEYA12vvtWh_U8RAbk7-cyvCzQki8AdVchYFjUBP5kGEKQ1S_xO1G_O4Agqk4jLL17e6uw0Z5yqrBqelvNt5NjHYL3quHIGZ_eDcuw4Pu3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=JqtXJe5J5rctee-lDU1uIn17pAPS6ZmTZ-dZsffUpAD0eFqwWoq2vSNryui8_j2E2Rc479aY3962hKBCHFQkmEKJ7SsABHdXf9Vp-9-wpUEGGbgPLorzRUeLWsGyXqwLNdAxWCB-m2_8oD042K08Xpr6MXZAHVMzT0YdJMozeIPG6nJ43gO1z-6IWeweFDvpqLLh0D40NnrQrVhtXFl0AU8JpyDuO7bVbVeeWvKoXbKQjloJjVwOhxl3wbii61XqINn79trokk-0Si_IcmkNAX7VkRq8ok6UAmtQx-X49kYazsXu7Au6zPEdwK1TBd6mCREMy--D3YAuAM5pLuF-kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=JqtXJe5J5rctee-lDU1uIn17pAPS6ZmTZ-dZsffUpAD0eFqwWoq2vSNryui8_j2E2Rc479aY3962hKBCHFQkmEKJ7SsABHdXf9Vp-9-wpUEGGbgPLorzRUeLWsGyXqwLNdAxWCB-m2_8oD042K08Xpr6MXZAHVMzT0YdJMozeIPG6nJ43gO1z-6IWeweFDvpqLLh0D40NnrQrVhtXFl0AU8JpyDuO7bVbVeeWvKoXbKQjloJjVwOhxl3wbii61XqINn79trokk-0Si_IcmkNAX7VkRq8ok6UAmtQx-X49kYazsXu7Au6zPEdwK1TBd6mCREMy--D3YAuAM5pLuF-kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=kke_YsYQ3hmJpx_EUfyBazUDNqUsQWtC7A1MVlZxTTfGgCLZMxf008GCf7SSJCperflz4uFWEa3RIpraxFt8lNEqCCu4cAuZVoW6d_ZwbnQ9hAQa5tK8rMncBYex3vX62XXzpLClVujBkIq1gNSKM1BxaNEtMydYCcptVue6gWj8rkZ7rvBpcqEKq6wCTQK7SfEE9cyHDcTjdEdqiK5xZSqlLEqNScAkYwSN6iqE7ED8dQVLhyLXlhtBSVrsbBSvet9Gv7W4ge7mutVcWwuygDyG7uW-oLJKopHWVQ4QDx8T_EenTviTyJJGbVr0x2AL-vD2rzatBhJDxx5VPimJJj35FEJ9NSNocPyqCohsIS9z3JYhPPDZ9zkfMDdy7MjgQxn3Ag_IeIqfpF6-Pqr1rmVtmiMnM3brn__mAp0WIxmmAc4tiE0h6eoZ6GbKAVmqwOXFQWHo7_q_yNsBZPTO4pojvb9x0RlZGrSFyEekjt7rtcdnncTtDsUDE6wquwqfuGff2KcJDp5yPcWG3cqOMrkpXAXibQVNWUaOWUDXdBZxR4NHBds4ZJFORPj2CpXJX6gzr16VqFQjcVOvjnRDmPkRSWZqD7mLSiz2qQcs6IqCxaJIH62p0iZj1hS-JhxD6VKyWyokKKsO5Wr_oWZuPcO_VU3PlaB2shCfo277-Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=kke_YsYQ3hmJpx_EUfyBazUDNqUsQWtC7A1MVlZxTTfGgCLZMxf008GCf7SSJCperflz4uFWEa3RIpraxFt8lNEqCCu4cAuZVoW6d_ZwbnQ9hAQa5tK8rMncBYex3vX62XXzpLClVujBkIq1gNSKM1BxaNEtMydYCcptVue6gWj8rkZ7rvBpcqEKq6wCTQK7SfEE9cyHDcTjdEdqiK5xZSqlLEqNScAkYwSN6iqE7ED8dQVLhyLXlhtBSVrsbBSvet9Gv7W4ge7mutVcWwuygDyG7uW-oLJKopHWVQ4QDx8T_EenTviTyJJGbVr0x2AL-vD2rzatBhJDxx5VPimJJj35FEJ9NSNocPyqCohsIS9z3JYhPPDZ9zkfMDdy7MjgQxn3Ag_IeIqfpF6-Pqr1rmVtmiMnM3brn__mAp0WIxmmAc4tiE0h6eoZ6GbKAVmqwOXFQWHo7_q_yNsBZPTO4pojvb9x0RlZGrSFyEekjt7rtcdnncTtDsUDE6wquwqfuGff2KcJDp5yPcWG3cqOMrkpXAXibQVNWUaOWUDXdBZxR4NHBds4ZJFORPj2CpXJX6gzr16VqFQjcVOvjnRDmPkRSWZqD7mLSiz2qQcs6IqCxaJIH62p0iZj1hS-JhxD6VKyWyokKKsO5Wr_oWZuPcO_VU3PlaB2shCfo277-Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=KnUvsHsx1j4p52TOcjZ7WE6W81c1u7suQHaimkSisk3Z5Rj_gX2nFJ_2tJd5oM5-80-Ez5ub9iIfGMoY2iAye6-8g572LYjENnknsLx7ElVTSt-ZrmNroyebr6Tx0UzHOcN0h_LpjZx_VhustaDb8lu80dDE2tJnZTs2FW24fJRYYpjYqYdDk94jD1WH7FeodScMKP9BfO2SgEXIV_SxzPUW08gEbzjdQKme40B1PDdJGQKEabJn3JvlIm6uIJsGZ-6PPFWKl23IAGFWWOI7zRId8Ykn8cZyaapmxU4BXBsvKE-0uZEaEkBeLo8D52r3Kt7pm_ug201dFWZky_waozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=KnUvsHsx1j4p52TOcjZ7WE6W81c1u7suQHaimkSisk3Z5Rj_gX2nFJ_2tJd5oM5-80-Ez5ub9iIfGMoY2iAye6-8g572LYjENnknsLx7ElVTSt-ZrmNroyebr6Tx0UzHOcN0h_LpjZx_VhustaDb8lu80dDE2tJnZTs2FW24fJRYYpjYqYdDk94jD1WH7FeodScMKP9BfO2SgEXIV_SxzPUW08gEbzjdQKme40B1PDdJGQKEabJn3JvlIm6uIJsGZ-6PPFWKl23IAGFWWOI7zRId8Ykn8cZyaapmxU4BXBsvKE-0uZEaEkBeLo8D52r3Kt7pm_ug201dFWZky_waozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iM269DDE1iXDU01yLNxYs2SZZHrwM3Dw1Q9BCC-ahf040ON3ASgDhxM5_wTzacq9EMPH2OoKP54Yy8PHAVFbnrxbyWqJ7NdO44d9G0zSQFCSZIIxuS5oxwcqsE5RdciJx3k2HiK39goK18uI9C2jQ0dsuEqpfzCJz7YSXgMEeyt9jamkGb_FcDFZJENkdMpW-4wUrmFS-U85iHYHTtlceOlN-sdlvHKAh2kLBMZ-Y3VM92Xr2q457MGn79N7gawXJLKMsKqG-bnBJw4NWxzWlCtzndn3Qwmvf52OOl7TKEbN-w-V5omHp5eXNACjCFqDv50w6LyhT3GVXcRomSV4Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUYsgp7OQ-SBU-xbhAkv1HzVZ4RKd_lpJpgr6zhJzHRVwzISdpOF6UPpQ0dV2FqqNa6iQiPqwcfdgfSjIP8gdijMiRNJjKfrXDvi6QWt3_TKNwb1Rs2-NASNfx8FwODC-S5x2tS1F9HoZzzKCKlRbnrQ5g5Rs7vM6G3JpaYnDOuZzF-6xOhB9s7T-HINGwDarh1ISufR6P9hinK0jnjK2HfOwCgPcM7pFYuUf4bwdZWbT2huLD1vhhkf1iZtDWkfbA6Re-kXPCYcdhn39T8OziBiVU0MYfPO_CxtsL4yKYFLdtzej_8aTQA84gK06NEE5ByConMNzGcZ6xPlWLNI0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=bY_I45_3kvcW3Y_bjHyf13eeChim9xpxokGOAip9-7TMPY77o7aBMMqLH6DeMhIq_YDkbzOSXqT2lCgKFMyTQVOr7XSQGFwM_3OCD7Hxkfi8e_n5U52kezWJXOsdri5IaCVQtx0AbsyQj2y49XKTSJ1_H3J5yLRcCZMD7OpVxeP59YXSF7DE0kG01yxYDwrbi-12MP22IIH81Iq_rl98sDE8rzVq9ramAPyhRsNeuO01j8UYWf0Jhe8o8VZ1U5yPtxqcglnPlq1M3bi3wG3RLU5e0CuoaXrvrDlA46DrVfANZ7MXMhyeEothJNvoJZ11W6Vg6I2Kfi5Vd615tqLjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=bY_I45_3kvcW3Y_bjHyf13eeChim9xpxokGOAip9-7TMPY77o7aBMMqLH6DeMhIq_YDkbzOSXqT2lCgKFMyTQVOr7XSQGFwM_3OCD7Hxkfi8e_n5U52kezWJXOsdri5IaCVQtx0AbsyQj2y49XKTSJ1_H3J5yLRcCZMD7OpVxeP59YXSF7DE0kG01yxYDwrbi-12MP22IIH81Iq_rl98sDE8rzVq9ramAPyhRsNeuO01j8UYWf0Jhe8o8VZ1U5yPtxqcglnPlq1M3bi3wG3RLU5e0CuoaXrvrDlA46DrVfANZ7MXMhyeEothJNvoJZ11W6Vg6I2Kfi5Vd615tqLjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=tr7my-_XCeqCDW6GFM9Z5s6ImAa6UJ3p8eMwGK8y6B6ckP5QzpJl-P--5UuuHPHt4KRZCx0DUKVMZzwjxmMKGbwDaHmEhs6JsyUWR_UvRP4Xa1EKZ9JcaDmwGa0B3d7qMhb3jq7Aj-Uv8eCyDAuCJfGCODXQAaAM0M4-42eZLk00rGknR_EbcWli6pG_sHCpq3-G119EEIZEpkkZVtaIpFpURQSe42-QEtVr10Hm7OitkrQsGGntWvI0Be2NjV3MWEMgfPigHWStKYoAY7uDV9-bIuyvw__cDwBf-zXSBTmLGs2RWCXwLd8551hInTsIAVJlbRfufxjmQS2fs8radw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=tr7my-_XCeqCDW6GFM9Z5s6ImAa6UJ3p8eMwGK8y6B6ckP5QzpJl-P--5UuuHPHt4KRZCx0DUKVMZzwjxmMKGbwDaHmEhs6JsyUWR_UvRP4Xa1EKZ9JcaDmwGa0B3d7qMhb3jq7Aj-Uv8eCyDAuCJfGCODXQAaAM0M4-42eZLk00rGknR_EbcWli6pG_sHCpq3-G119EEIZEpkkZVtaIpFpURQSe42-QEtVr10Hm7OitkrQsGGntWvI0Be2NjV3MWEMgfPigHWStKYoAY7uDV9-bIuyvw__cDwBf-zXSBTmLGs2RWCXwLd8551hInTsIAVJlbRfufxjmQS2fs8radw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr7lFUWdxmQmfiUh0dyFkwE9scOU7dxW6LF62Jz-oqazQb88ib1l9Y5a7s9ot6v6cDjbB3C3FStDYUmnoaP_Nyi1RxGZGWC_JoiEgJtqJTCByz8EINqHNP5y_Bfbw1VEoagTdkgx3ppFmSCx7VF7VSG_BPC2FQaRivtRGckZHlgGOUZHgd-MMhsehNjdMSdHdD7jzFmrv58b4vmcFzhUlZA-glf7OGrqtu3uw6rw7HQVfza2fl4HeM-mw-hPaT9MVCe_gdxFREWAoqs09y6n9vqhJOKFmXonzFJaPZTifczkJn4Hy0MiNZam3ivevOqgWvgRHfRdyb3EdN3M7WCgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=vqpSglZIiNtU8hFc0cssXpAC1tU9UB-66g_nACGRX1XvQsh2pc-H2DN8ZxjoNygHhbTWAjTytNV1qVp_ngjz7SGINrCdcuz7cww2arzqDuJGAgu0Vter2QWiugcHh2s_TXygr58mtNKNcm8DvQyE942XJX_tpJEspPNgjub-ccL55bQPQq6dCFPd3oSHfN2qFwu8tv742MGDZKguetAYR7ghjiOxmLKk3q0Ohnlz59GOCjJHLFuh6vzfb0KqDeyyhQgChAKmZiJ8CgwKDctlpiArpt4KwejMdoBIpCgWoRxIL6AXwodX99wTeQQSWozAn2nm8wObID_BN3Fpt99dSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=vqpSglZIiNtU8hFc0cssXpAC1tU9UB-66g_nACGRX1XvQsh2pc-H2DN8ZxjoNygHhbTWAjTytNV1qVp_ngjz7SGINrCdcuz7cww2arzqDuJGAgu0Vter2QWiugcHh2s_TXygr58mtNKNcm8DvQyE942XJX_tpJEspPNgjub-ccL55bQPQq6dCFPd3oSHfN2qFwu8tv742MGDZKguetAYR7ghjiOxmLKk3q0Ohnlz59GOCjJHLFuh6vzfb0KqDeyyhQgChAKmZiJ8CgwKDctlpiArpt4KwejMdoBIpCgWoRxIL6AXwodX99wTeQQSWozAn2nm8wObID_BN3Fpt99dSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=iyhyfrfAYhjsw4JfTZWfwR8ZPezT2-kmj-VE3LDJZ3ZY65hbyNugH9VbmRw1NWPs5ZwCVk_Prb0O1OwQ7e2o8k26hlUkvldybmZM2txyTwktVZem-mQZkWJI_YjwC1F7-YaeinIzpbch0g81a1-u7nJ0mqYCw8Kk89uzUwi1g4q9PhawlMaSu-7oiSgmvTCMcRmcHykCmSUC1RMQERehSqLhgVowY9ieW_ymgQBOw0pxlL8pC9gRQVgfBXAnSJdGxkVWsTc-uCTaafNvpfrzmMDqk1Tx5yO_hpGf3IkHHNW-cxdpLTtDn45BA2Co76K8tQQ-D2iYJmvX8vosW27cNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=iyhyfrfAYhjsw4JfTZWfwR8ZPezT2-kmj-VE3LDJZ3ZY65hbyNugH9VbmRw1NWPs5ZwCVk_Prb0O1OwQ7e2o8k26hlUkvldybmZM2txyTwktVZem-mQZkWJI_YjwC1F7-YaeinIzpbch0g81a1-u7nJ0mqYCw8Kk89uzUwi1g4q9PhawlMaSu-7oiSgmvTCMcRmcHykCmSUC1RMQERehSqLhgVowY9ieW_ymgQBOw0pxlL8pC9gRQVgfBXAnSJdGxkVWsTc-uCTaafNvpfrzmMDqk1Tx5yO_hpGf3IkHHNW-cxdpLTtDn45BA2Co76K8tQQ-D2iYJmvX8vosW27cNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=mH6wzoQLqyO3H2yZqeDY7IEySk-dEf5eow7Xm04Ha2ev7ENjmuMB20FRa06HDBeZGedZ0yGbrLmPZwqs8WdHO3K4xJddT8UqLWLMJYieAOEQ9O_ojZLZsK3a0l1r4PQIz4TsJMcITpLe1M8DHwcLg7oPKenSlB7a7nEDEw_D8Lbkrd8EFbHabmes-kJIdXV44mCvZH7FBlpUapbwlYqthSRDvXavh36-jNRu3-4SvbJnIKlNFW05LDNnYOBFQBjIVV0lwdCi6cg4aXWDIRDLjE4I7mUGwg1CdfZwbZ_XPz2aoG5t3KIZQ-ajKAZW8bE14-VI-xdrHUip8FYgk-IfRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=mH6wzoQLqyO3H2yZqeDY7IEySk-dEf5eow7Xm04Ha2ev7ENjmuMB20FRa06HDBeZGedZ0yGbrLmPZwqs8WdHO3K4xJddT8UqLWLMJYieAOEQ9O_ojZLZsK3a0l1r4PQIz4TsJMcITpLe1M8DHwcLg7oPKenSlB7a7nEDEw_D8Lbkrd8EFbHabmes-kJIdXV44mCvZH7FBlpUapbwlYqthSRDvXavh36-jNRu3-4SvbJnIKlNFW05LDNnYOBFQBjIVV0lwdCi6cg4aXWDIRDLjE4I7mUGwg1CdfZwbZ_XPz2aoG5t3KIZQ-ajKAZW8bE14-VI-xdrHUip8FYgk-IfRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=OcguwEt13kKmmO8C_jcXEHSAzW0BpGfSSS9PB-E6wx4s0ZkKa2Qoh8i5F9Hn1A0zW5SdEKbsUptXjEW0BdARFfok4dKVQfs1nR6tz-1cm3nUc4Xw6tbTrvz-XsF50A3nU_bZMwXcZ-61JDxU1xNJmU8Q26u5nSaeLSvMnKOk_gihzLC_UGV57o5VFz8Z1SeYtyLsFyHZxGcvbpw2ReaGOqqLMlSkKywq_UZNBvmzT_RtSjkQ1pG3AcNa82rDEWTkjf0B09WH7SksTVbLA9guWfK7bFvLIw-0CHIEheDMlnrlG1CZX6z4dL2OM0AsFllTVC7dtNqvVUCGE_YE0sILQl3RGfXDFkxgF3kCFJL3ACNxEV5_k6VVah8Us0VfWG5wFfB7ZrA--usNpVLvFoHd7f3XSlV0wpoWNuEuXLwev1LFj_6dO-dBoHySK8uLzTPqQcNszd9WWA0wEMQ2Kgrfl47pHb1J4PIAxqiFEWJlEqJqdumpb7pEWlfSyRwfPWiwREAUuf8gwoRNei4c8IcVu3z2tt9yCXJzGFIN1L4OH5iWbJ7D4uoYeVl-JUVuDjxPgJP11QDomklv2P8pBG9n93OhtfB9AwSTpFd0ZZoHvEqvm6TBpoPvZMvzz5B9Oi-VfkmA5GYyW7qUMB6aHdIu8IVlc2-N6-5jNIG5sDH37Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=OcguwEt13kKmmO8C_jcXEHSAzW0BpGfSSS9PB-E6wx4s0ZkKa2Qoh8i5F9Hn1A0zW5SdEKbsUptXjEW0BdARFfok4dKVQfs1nR6tz-1cm3nUc4Xw6tbTrvz-XsF50A3nU_bZMwXcZ-61JDxU1xNJmU8Q26u5nSaeLSvMnKOk_gihzLC_UGV57o5VFz8Z1SeYtyLsFyHZxGcvbpw2ReaGOqqLMlSkKywq_UZNBvmzT_RtSjkQ1pG3AcNa82rDEWTkjf0B09WH7SksTVbLA9guWfK7bFvLIw-0CHIEheDMlnrlG1CZX6z4dL2OM0AsFllTVC7dtNqvVUCGE_YE0sILQl3RGfXDFkxgF3kCFJL3ACNxEV5_k6VVah8Us0VfWG5wFfB7ZrA--usNpVLvFoHd7f3XSlV0wpoWNuEuXLwev1LFj_6dO-dBoHySK8uLzTPqQcNszd9WWA0wEMQ2Kgrfl47pHb1J4PIAxqiFEWJlEqJqdumpb7pEWlfSyRwfPWiwREAUuf8gwoRNei4c8IcVu3z2tt9yCXJzGFIN1L4OH5iWbJ7D4uoYeVl-JUVuDjxPgJP11QDomklv2P8pBG9n93OhtfB9AwSTpFd0ZZoHvEqvm6TBpoPvZMvzz5B9Oi-VfkmA5GYyW7qUMB6aHdIu8IVlc2-N6-5jNIG5sDH37Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=rcOdFFIdLKyIhoQ8HYCLpzjuBLuSApOhuruQZZgXeCAE50SKwu3F8Z-3Qnl8xaNWFquLz6JDi0TEZZNDIr_zWf1u0NLsqFRbI2mbJe9kMhMWSYH3g8SYrtKkfPCyxc5npqTAteX9DAqJRpfsiwWEsa3Z9Jl5SXh_OguVm-TbhvwRwU2HJVO8zLB3MPcBdiNO1A9yPGOODzxKgHygBG4CJlgNKApTyUDPhCgpTNGyEedIlRdNh-aF1-QlxNwpNpDJconh86L8cSjcBpmuB-7Kek-uxPcHe2KdAgN4u3TuvSGxhFZUgTyAgM1cvnEPKZBVj9ZfmzDkD9BVrB_5KejnFw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=rcOdFFIdLKyIhoQ8HYCLpzjuBLuSApOhuruQZZgXeCAE50SKwu3F8Z-3Qnl8xaNWFquLz6JDi0TEZZNDIr_zWf1u0NLsqFRbI2mbJe9kMhMWSYH3g8SYrtKkfPCyxc5npqTAteX9DAqJRpfsiwWEsa3Z9Jl5SXh_OguVm-TbhvwRwU2HJVO8zLB3MPcBdiNO1A9yPGOODzxKgHygBG4CJlgNKApTyUDPhCgpTNGyEedIlRdNh-aF1-QlxNwpNpDJconh86L8cSjcBpmuB-7Kek-uxPcHe2KdAgN4u3TuvSGxhFZUgTyAgM1cvnEPKZBVj9ZfmzDkD9BVrB_5KejnFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=ZDQkrX3kCuab9MUk3F4ApaZLC7_m_epPXzewRd8YdNSmYtt1ZxgW3YEMhghfc56FQQkzU-EE5Nh1elb9iFgsei9J7Nszqyfu9bptG6kBm4bvOy3ILsOlMS6loGJJ-baLkk3bXV98usECsWfhG2UJg5jIL7qpL8hHudGLBTxCM5LAjOTYlwlReZEDmGsZJKCrjLj2k8MzGv2L29dkXlbL3ij8nGYPLz7Bu_5Of6LRxrY5CbcWVQ88_B0laKNaFPPp97a94dQj10o1ZBtz2hv91MvAnpczfAjP5XO_ddXGKKfcIwurAVTx2jIUjwtqKPceA5taiP1HrnejqgPorWjpoDPNw0xxOytqiYMcDw_TyhFjLe8-hAHu7dk1HoFBfGq6s1ymM8t-GhkyaeuCUBLvEZwUSrMK-cm0M_7emAT5UoY7T1nzM5ce5yiXR94zq95hfCAIMQOS32eIXYFTml6YBMlAmqVFAO1HLo676f4FqqIcFFrp_xlDkv1czdpYGoPbsXzXB9M7_XFXC6bakS2MKST3kWLZMZG1SnN_G09v4sGAhtX-P3xTXEMslRXDKTeQEeL93ttfqOZX9bQtgdac49KR1tLCCgPcNLuvmxy_VmxtlXZ-0yOBeubB6kisNDA60a3GkldC9OqAh8YBfSPVARG0dnxDVFCnyvJlkiPxaVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=ZDQkrX3kCuab9MUk3F4ApaZLC7_m_epPXzewRd8YdNSmYtt1ZxgW3YEMhghfc56FQQkzU-EE5Nh1elb9iFgsei9J7Nszqyfu9bptG6kBm4bvOy3ILsOlMS6loGJJ-baLkk3bXV98usECsWfhG2UJg5jIL7qpL8hHudGLBTxCM5LAjOTYlwlReZEDmGsZJKCrjLj2k8MzGv2L29dkXlbL3ij8nGYPLz7Bu_5Of6LRxrY5CbcWVQ88_B0laKNaFPPp97a94dQj10o1ZBtz2hv91MvAnpczfAjP5XO_ddXGKKfcIwurAVTx2jIUjwtqKPceA5taiP1HrnejqgPorWjpoDPNw0xxOytqiYMcDw_TyhFjLe8-hAHu7dk1HoFBfGq6s1ymM8t-GhkyaeuCUBLvEZwUSrMK-cm0M_7emAT5UoY7T1nzM5ce5yiXR94zq95hfCAIMQOS32eIXYFTml6YBMlAmqVFAO1HLo676f4FqqIcFFrp_xlDkv1czdpYGoPbsXzXB9M7_XFXC6bakS2MKST3kWLZMZG1SnN_G09v4sGAhtX-P3xTXEMslRXDKTeQEeL93ttfqOZX9bQtgdac49KR1tLCCgPcNLuvmxy_VmxtlXZ-0yOBeubB6kisNDA60a3GkldC9OqAh8YBfSPVARG0dnxDVFCnyvJlkiPxaVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=J85hOGq5bpjFBYyZWd0-UVey7f5Ak3GSly-0OUzBnI9Q4N8YWi823c2WyfLWpc96t11H7hn5kyNXZb1FJv_5QbjSLpEW6bga2gHidrh6wIi2ZWatKrWEJSykVVHkM9_L810ks5j-NXU63S5x7U7vEH3BeiwFCC8aDg58kOvM3MnYun1RZNnxTdI-WMllN77XHHu3WMDp9XbFCT8X9iVr8bR4M8c4PTxpIJq1feJJtqpVtDibDJvucRuJxQUr4xaqbT2AbeOPmhP5bs1uPQHYEdqai_bVydtmTaSggkzhU3YwMU8o3nLjWrnuRuc8AheyPFyBy4wHJRFvG8WuFxoHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=J85hOGq5bpjFBYyZWd0-UVey7f5Ak3GSly-0OUzBnI9Q4N8YWi823c2WyfLWpc96t11H7hn5kyNXZb1FJv_5QbjSLpEW6bga2gHidrh6wIi2ZWatKrWEJSykVVHkM9_L810ks5j-NXU63S5x7U7vEH3BeiwFCC8aDg58kOvM3MnYun1RZNnxTdI-WMllN77XHHu3WMDp9XbFCT8X9iVr8bR4M8c4PTxpIJq1feJJtqpVtDibDJvucRuJxQUr4xaqbT2AbeOPmhP5bs1uPQHYEdqai_bVydtmTaSggkzhU3YwMU8o3nLjWrnuRuc8AheyPFyBy4wHJRFvG8WuFxoHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9HO8gqJTZFkel5TqQcpo3IKx_75ZH9Lx38tprqNJC9FVjHBpYyBB3QIDAk2Q_rTOrVFH8Od05uY-5Mz1-SDFqLhVAwmHleB2ZgIDv6G40xP0aSIZyqyK4l-UTvtZC-pIBNnOzqcMEE8TmEO0EzTicZHUTLxNMYluTbeKFf_RsjiONxwh6hovkP3DbJzwPidbkql6eFFWF2J-cBz7uD_ANpzMoYZ8LYyhNtlGe1YkAoOFFr_7vJQniGsw0u-fYmd277CLUeLpnWmQEKA-drQInzyOkGOyhTRM52WINkwK2CKfhf8TlKKqjHu1HrekyGLdOpLh3DEY9Rl15OgsX9E0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=BLabfG2BTMKyDh_Sq_aUd2A13hnkMYvT2zeJVjpyC7gN6H9W15Rml2OWtucrByxOSVF7dYqTWgZI6VTuXkvhbuvnCvmoPi5ti3kKmdPakTaTUY0j5Q7Bgfp3Yt-vsb-zro4zUeg7xCOgHUMe5k5ZZcdH5-JtQ5mSA8RZLAoY_9RqqzFvFm4TH-kwsNNv4LMjVNLx6_-s-KkJCYMYEYvl0D8W-WxEXP1OxKFFlz2DnCtGuwK2L3yDRNTHm0pIhMfCp1DQF3NcPcapQGKeq2JBWNo091KEa0e5rDr0WGcVrqyuqjp3QKeDx79sP0Q2hzConNNf6gARFSaw12qdw05uzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=BLabfG2BTMKyDh_Sq_aUd2A13hnkMYvT2zeJVjpyC7gN6H9W15Rml2OWtucrByxOSVF7dYqTWgZI6VTuXkvhbuvnCvmoPi5ti3kKmdPakTaTUY0j5Q7Bgfp3Yt-vsb-zro4zUeg7xCOgHUMe5k5ZZcdH5-JtQ5mSA8RZLAoY_9RqqzFvFm4TH-kwsNNv4LMjVNLx6_-s-KkJCYMYEYvl0D8W-WxEXP1OxKFFlz2DnCtGuwK2L3yDRNTHm0pIhMfCp1DQF3NcPcapQGKeq2JBWNo091KEa0e5rDr0WGcVrqyuqjp3QKeDx79sP0Q2hzConNNf6gARFSaw12qdw05uzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=YBJq5lqregy6cXMucmGiCIzciQlNeKlBYjz_BWbu7Dm0-2tiJsnZlGYR6qcL6ZnMzt-FgvH05WxjmxGFRsffb0Cxc-nOtlvzUFDgBJpkLhRzRRFp0BncrwiP44b5QDu-ffyCNUHA6Mf05cAOcTo3FaJv9dvMLhI0I8i8t2OKwJXRK431ZK5Vhefk6EpJXA308kIntjSZrNinByzuziwWkkHUCzXFWVWP0zVhoY-xf_7ADSHWH_CpLEBZRWbPXDEQiGZ6xNaKQoWcn3EKULzGkxy1nOfbfdKUzYkinkr2Bl0yYPcwOBAsJ66iVmOF-joKjCmoYisDsxRw6v8fgrAixQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=YBJq5lqregy6cXMucmGiCIzciQlNeKlBYjz_BWbu7Dm0-2tiJsnZlGYR6qcL6ZnMzt-FgvH05WxjmxGFRsffb0Cxc-nOtlvzUFDgBJpkLhRzRRFp0BncrwiP44b5QDu-ffyCNUHA6Mf05cAOcTo3FaJv9dvMLhI0I8i8t2OKwJXRK431ZK5Vhefk6EpJXA308kIntjSZrNinByzuziwWkkHUCzXFWVWP0zVhoY-xf_7ADSHWH_CpLEBZRWbPXDEQiGZ6xNaKQoWcn3EKULzGkxy1nOfbfdKUzYkinkr2Bl0yYPcwOBAsJ66iVmOF-joKjCmoYisDsxRw6v8fgrAixQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=cMDl0woi4wpiKiQshFe0_1Ja74oD9ZmiHQUwsLr8itDVIUuTmZ2wfxDjZieEXq679w5O6FQQ5FpyZ7KmoXLAOZygy3d4LkuXuEdL2Bj8tVajJ0XN-ghaeU10zRMCnX1-KNZh0RlI8kzg5IGrtgJ2l2ep-4LcH5aL1SauzaunqAKOUVBL0rcTtkprX368TXwp8FHdw2ECwS_G2JdyoScCC6-1BL96Q1pcqO2Ob5ihnyYiUbHKcGAkJABH5oDbi-bOdz9qoAUf5Cs9yCb4k1_0LX9dgzCgoHUTXGRMEeML063bNHezxSugjGBckdPadUYHozZR9l-61-e6VEa96lpI1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=cMDl0woi4wpiKiQshFe0_1Ja74oD9ZmiHQUwsLr8itDVIUuTmZ2wfxDjZieEXq679w5O6FQQ5FpyZ7KmoXLAOZygy3d4LkuXuEdL2Bj8tVajJ0XN-ghaeU10zRMCnX1-KNZh0RlI8kzg5IGrtgJ2l2ep-4LcH5aL1SauzaunqAKOUVBL0rcTtkprX368TXwp8FHdw2ECwS_G2JdyoScCC6-1BL96Q1pcqO2Ob5ihnyYiUbHKcGAkJABH5oDbi-bOdz9qoAUf5Cs9yCb4k1_0LX9dgzCgoHUTXGRMEeML063bNHezxSugjGBckdPadUYHozZR9l-61-e6VEa96lpI1oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgHNKXMZXt2N18JywSC8W9AJSckNmyHcXboZuKhljzkvVdAJFTVxNhShcv79x3yTp-K64glvMBSSRTSoCEy20vNz4OGtMxueHCAhP0Sl2L4pU3nSoORkKgPn8wguCrHcBnEksZ4m6PLts9dGuVGxoJo9K-kXlWZySvt1nZjw-47Tt1IEsk08nrHBA6OEVfradHsY5XArxkxGdakAyHhZwpBfxxd69kVI61hhzmpL1bwJtu9TSWp4lZ4Y_BXmhDBnjLMd4lhe5GhWCfSy9E5GJ6Iro3lbghavq7cLZ_fnE_IYihCI5JAUZQpFbl31m_yJnLxDO3yh6a8QoQqYCmdCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=KXOxCDNWLD4E-jlXuxJdr1ETBOIAuh_bXMX7n9oMMa2MXNOudkgHQaUc41ByxgyCdaYOhAm-QKILRmbJ65kSQwlnduo0OG57xPgy6FW_K8OqUYgfBSJDRSw57Y6X5Vxe6g_JOqcBAXQTwgbyitl9SL1qZRDZftp-_jxXiBbbjEySJgRHmoFjWdMp6-WshFJBqTQ18BfS81QgBV1a6C17HpiWHvrMYUiP9ERAzCaI2N4NtkkLyLMtxISQX7Krj9RWfKE2MgxkxhLFSmfRYHpcFtJpdvRmBt1IpAg2ZBVS2XQPJZyt5GTqdEhUVfmGGNEtC0FreK1wgx6qT0Guykqg_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=KXOxCDNWLD4E-jlXuxJdr1ETBOIAuh_bXMX7n9oMMa2MXNOudkgHQaUc41ByxgyCdaYOhAm-QKILRmbJ65kSQwlnduo0OG57xPgy6FW_K8OqUYgfBSJDRSw57Y6X5Vxe6g_JOqcBAXQTwgbyitl9SL1qZRDZftp-_jxXiBbbjEySJgRHmoFjWdMp6-WshFJBqTQ18BfS81QgBV1a6C17HpiWHvrMYUiP9ERAzCaI2N4NtkkLyLMtxISQX7Krj9RWfKE2MgxkxhLFSmfRYHpcFtJpdvRmBt1IpAg2ZBVS2XQPJZyt5GTqdEhUVfmGGNEtC0FreK1wgx6qT0Guykqg_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BS5fcpmPKpTqg-ElIK9I-GI6uLjylhkQGNRq9ZBE9oz8HZYT-xWnPZFmXsKY_A4F_0L0Hq-KBeEUY5iWXVJ4ZxgHjybrk8dm_er1-6Q0ncwI_L9M0cHf_YfYH0tORpSbgBvHhLyZj1uoVFxYc_b5Bf4eWtS_pjvv2OPiyQEqKLNNpya31-y_LqlK8R8fg6ioDk5HmVKl6ChNRs_6Zu8cJhDkUnsvxU_BG1O-m3VMSUb1ji5XHbKuxSy0R3STWoGCCfV1DcoHzkSXftGT0AtCBr31oMfy3Y0VENoKPvf9nLVZnOytCQCemsoiI2oQl3BLNw1i-T4vNpBX015jRrgL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=YvsDYbDPSD8PGjT_eZ4YcYiu82D46jPssbiOhw5NZwggB56bSVtZjTKs7dBiLo0eXWKa1w6BHAegTljPYZUQq7AbHf47oWr5uA0DKF7BmRaMXSPCQSomdT_Y3EequfMGUS5G1O0JONAOy_V5kvWrxP5rSVVxsZwiHJWespsroR1LsJSO_5awDw-7s7EROffhfY1BDF-zRMEMC1lamJOk9Hp6ZMsv3huVZQx9M6whoXF643870-cg0xjlV6rGpmDgfmrHEtx5KF6ZXkckMdCR-Y9AF-WUe8ylY6NPfTAc4IAuEOKAJO3iRRYdty3ZSvizDRs0vQEKqv_gOn7kMug0ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=YvsDYbDPSD8PGjT_eZ4YcYiu82D46jPssbiOhw5NZwggB56bSVtZjTKs7dBiLo0eXWKa1w6BHAegTljPYZUQq7AbHf47oWr5uA0DKF7BmRaMXSPCQSomdT_Y3EequfMGUS5G1O0JONAOy_V5kvWrxP5rSVVxsZwiHJWespsroR1LsJSO_5awDw-7s7EROffhfY1BDF-zRMEMC1lamJOk9Hp6ZMsv3huVZQx9M6whoXF643870-cg0xjlV6rGpmDgfmrHEtx5KF6ZXkckMdCR-Y9AF-WUe8ylY6NPfTAc4IAuEOKAJO3iRRYdty3ZSvizDRs0vQEKqv_gOn7kMug0ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=Gd8wYdVlTuCLyM8j2YTgwljC9S41zc9-bfSnFLuWr2Rkcvu_F98fZb5QTfH9snpY3qffesStj1H_y7ovQc-qyuiNgxy74HD0_qL9ULGGQByIv1FXmNz0FaXaYZVQWh1vQhIiGmeKFcX-cMNNCaE9VndrYt-1AiEql6UGVs8L_3ORJyYt3onMAn3_Kyq-EZC5LVEM-EY9nzpXaiMb7pGyHFMDMQU535MMu0Ygn78ha6aT6oXIIHQCRQLvHtkxyKTYfp3Rnq4QPNcY8A15EUayLbuRNF2B7_MFLPX2XPl9qxMlyR9XsmF75ae3n9V9k8GBGi0PWAp9gZyi6tL9zdnWLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=Gd8wYdVlTuCLyM8j2YTgwljC9S41zc9-bfSnFLuWr2Rkcvu_F98fZb5QTfH9snpY3qffesStj1H_y7ovQc-qyuiNgxy74HD0_qL9ULGGQByIv1FXmNz0FaXaYZVQWh1vQhIiGmeKFcX-cMNNCaE9VndrYt-1AiEql6UGVs8L_3ORJyYt3onMAn3_Kyq-EZC5LVEM-EY9nzpXaiMb7pGyHFMDMQU535MMu0Ygn78ha6aT6oXIIHQCRQLvHtkxyKTYfp3Rnq4QPNcY8A15EUayLbuRNF2B7_MFLPX2XPl9qxMlyR9XsmF75ae3n9V9k8GBGi0PWAp9gZyi6tL9zdnWLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=EZUJi7rtzA-lOvlVTSu5_OTUV5vAqruxiQ0_4cBSOreQp4Ee7wfaY6i0Jfg0uy9tCWDtxzZkXSYnpWhpXRaeQ5WFryp3d13wcQadWlHezcUBCutk7MJAPN6vqqIKTxN9ndVCE2VlupFG7xV9dsYx-FtmvKrJVYx3XW7dm7z5MIK4d0eaAb75mncsiIwb0RIWl9zk1Ezxz450E2Mu1FaHRrlt16TuPBSBVboATHTINS4whoBNX_qBpB0uuNwlB_MAVK1qWlsHUUnn65pnCVy34y_XA9wtzjij18FKysk_whJq9NLJkvvsiSETOKFvz4MbwkFK-LzqLgQqacQDXxbYv6j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=EZUJi7rtzA-lOvlVTSu5_OTUV5vAqruxiQ0_4cBSOreQp4Ee7wfaY6i0Jfg0uy9tCWDtxzZkXSYnpWhpXRaeQ5WFryp3d13wcQadWlHezcUBCutk7MJAPN6vqqIKTxN9ndVCE2VlupFG7xV9dsYx-FtmvKrJVYx3XW7dm7z5MIK4d0eaAb75mncsiIwb0RIWl9zk1Ezxz450E2Mu1FaHRrlt16TuPBSBVboATHTINS4whoBNX_qBpB0uuNwlB_MAVK1qWlsHUUnn65pnCVy34y_XA9wtzjij18FKysk_whJq9NLJkvvsiSETOKFvz4MbwkFK-LzqLgQqacQDXxbYv6j6zAcEe33LzLUVTb0v-JSH2t6UP7BjbIAai7K90UDrDboJReOHgCGTVNVAfVxVCdY6vgV88B5eL8yrXl2Xz_Rfni6_D10CXCxsa2Ea9fKXy81-NcgXl-h2GXFGOqOFxBTUIUciOxbVDpq8xmHCoqFFXSrI-_XvY1OEFDJOYpJoqcqrDd1dDuMmJQSXkB69nnldT0c2lzaxO8My3_jvO2VvQ7jo-NQOkS2_9ISABRKyxe_WXf4JLDOxGf07_Go3rH0LQRfD96-WjPAT6lyi1kUEsO7isV5S32wLcBNFPcEHMo5rHFeA89CptoL0eS6A7tpJIrJNVZSqlq4SVJ-l99g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=iMTckGkntDIL4NIS-Na2lCkq16MhazJPmkc3Sc8eQqCcar51QSTddZsLOW5ZzXyriosn2MGe2Fv7mucBAEmnKwbV4-YmAidQa-fVjVqtZu5v9BPrfa_c2LhkgP9Ik-OPVHwaKZdcLcE1-R_vA4aj18lpcSUF5Sq-P9adppkDOOSU62O2dj7ZxgaoyBw9LfQKjTjGb9r6zcwgp557VvCCjYCWuR3M2Y1-MEMOuBO9NBw7hlHjIpX-M3TIIsHRFApIFWil4FuraAqEDji-8uO7LGheRrsb0WpIbJ73vqNuShdnnqCLEhGejfbaPDPfXv3pe9s0Q-pPy7H7X-6j_I6HzA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=iMTckGkntDIL4NIS-Na2lCkq16MhazJPmkc3Sc8eQqCcar51QSTddZsLOW5ZzXyriosn2MGe2Fv7mucBAEmnKwbV4-YmAidQa-fVjVqtZu5v9BPrfa_c2LhkgP9Ik-OPVHwaKZdcLcE1-R_vA4aj18lpcSUF5Sq-P9adppkDOOSU62O2dj7ZxgaoyBw9LfQKjTjGb9r6zcwgp557VvCCjYCWuR3M2Y1-MEMOuBO9NBw7hlHjIpX-M3TIIsHRFApIFWil4FuraAqEDji-8uO7LGheRrsb0WpIbJ73vqNuShdnnqCLEhGejfbaPDPfXv3pe9s0Q-pPy7H7X-6j_I6HzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIUF65BYMJy0OZb9LILb-EmJgE5ZAqZIKfnRS5a5YsTluHWaFKIgiYMtTqZc9S7IQo1Oe2SACdpLIXsxtF384kB2b5t_ArUDiLuKFu65XF0x9gbysYImDW8puOcYGuga6e3AinWGx9av4Zvwx2pX4Dwiis1CJrpSnM8i4D-5-iV61gV2mzyNXysqQ1fq8FNGoozQiZjHIqiCkuWyRhcVDwQyNow8WEVITRjjWGcHydKdJWpGc66C_JPozp9JjWKYJxO1K18pjiFgh9wgqlGZ92dL-WzeAYTYMdYPL7MhLpw16CtCy9s8ZJz2lyb7seO5TncihxrXw5WDuPdRTCYSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNH7yk9ZuL2t7-Z8nIoHkmTnN3XxWfqQyvvORg8t4mK_PLiXC4n2T6G8Cf_mUudGj56oJ7ijlvP-qK4_zrgJsBPoy64SZFSbakTBhI7z406Gca8k5sakL9Flbxh2AeWXwMkX1u-8Dow5UHL-Xew5QmyJzds2zZ9yF3qplWgAtrhgw_gob0UJMkiEW-eQ-39OgZbi5aizjQRPUXJA529Pz0b2bVxXx2tj1tmE-Jikc3_ORm31KwD61w9T47EjbKKxn5Nw083NHvm-JYnvFRYG6in2xcfqvBTEeNHzuRxdtoOVKwwbQrPQibCug6Jo2yZQXNQ5m3l2RHOD6c2U9ZjJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=LwsHsa6-yEBlo4jnVibD7zJODXmzLBbo2zEVMQRr884cJUjrujWe47RN1pGEtfGAIuL7L0zIyiuskyVT6LY1OlIATMjvv_0F-thhB0Y8-XWMKs7qSwX4FmoNIIWPWo7EmXaXp3nzPNlIMgEPM0Z4iqWlgBtH43070_saTpzDLQKIdmwjVD_qsHXB3ZTH60flpQWGsk6kwEjcUgS4DsehkB079oCGO_MSuSnBh_N002i3b6wDhMIsV36w7U_h8XAVJ9FRzYfpTcJ6tt7fN1BttNGeYCQGu9RauG2dklTk8ZS5PpIKXRv-oiLoXtZkPTofftQxTrv5blynP6wVJNeSXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=LwsHsa6-yEBlo4jnVibD7zJODXmzLBbo2zEVMQRr884cJUjrujWe47RN1pGEtfGAIuL7L0zIyiuskyVT6LY1OlIATMjvv_0F-thhB0Y8-XWMKs7qSwX4FmoNIIWPWo7EmXaXp3nzPNlIMgEPM0Z4iqWlgBtH43070_saTpzDLQKIdmwjVD_qsHXB3ZTH60flpQWGsk6kwEjcUgS4DsehkB079oCGO_MSuSnBh_N002i3b6wDhMIsV36w7U_h8XAVJ9FRzYfpTcJ6tt7fN1BttNGeYCQGu9RauG2dklTk8ZS5PpIKXRv-oiLoXtZkPTofftQxTrv5blynP6wVJNeSXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gEhDxmhhDLJ2rg5O0cO4oEmzNyS_iyAmorzpfTu-TBN_nGOmT0ZxyMP_xjnMcY1wVvKhf9a-aHIWrC2L0tIVpQQyLqCd2khqaG5i_xzhm3GNWhGmjeoz6bcPCfdgcFGNRST1KuHxKZkoOkdsnXQ8v3hJ-k73uw7LaAUIBtgeWT2mVTqXn9Y8-L8gUJMUvu6KJVxl_f3JbBIzvwwkR5hlh3RiiLZwPcq12IrUn47TW72927wicu3zK76qgjOTU7cNyrP6_l9Uu6g411Z7GpuLewt4pbxpWJKxG0h2M557aK-AZo449k6bzJODKcnqldP1lyhyqnkKrKoFxraZjmc4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jcNw9BNXUTfOT0Q_TBDnS-0q3rjiPdFRWS0wfzxMFFvJo5xwpJ7nd1YKnQbV8_dCPCchAbfLm0SfE_djXpFPX6EwSk6n77V9IVBzQX7Ii0K0mGHWazk4qZu-ZZnvZu8jnjb00CvBdjSpEZn21XckX0hxzxz7rHtbHm5UHBHvtoFKvZjxl-P053ND_Wcj-AV39yBzWEGswSSNIIB2tYscOoLhb2OuTOfc3cGzl8eZCEGTwOc4imfcB6XLZSn36Os3pXJDkNr-CZrtEw5ocYLvaKSKguKo2IEKLZ_ZChYtW2EIIinwrUVscAciTeQQOjwiahfaIA-UJrAsXJKlUdYEKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/syXMvlOtYnMQ_lHBKq2jpRJ_MFCdisYa6LqATqXsDW0u1x5OxLzCZIk7L5A6pA7GljoOSjeNte7SQ5tDdf6_AxYnu1GzUxoak37Wzs2-JxcT955P771kqxnTfJL2Bku7gzdRm0GfDH65xDayrxPmdbtAg0oglpgpfdyrGbyRGTNAadw4x4PJ3kKI0Iv-h0kK3rgId7ixoWp40Q2H_kiHKBD6zNjTQD2HTjSqaMDZjOMrZpEui7tEnM3OC1Db3DTYHb3Yb5ZPeB0NND_dNv286yUoJj6IwwRA4A8EQukl4za_F6N3BbtjzbzApYHicJK31W4u-zDhGL5CH9KWmymMyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=BovWgWOIwfRnJex3k-lfW9DB3nz5vKPGAlre0lqHYfNBhtiJQZbMWdke12IhoqVlC-7x0Cs-vjooD7BZzSwU129A_H00yHcLLGN4SYwf-FZ4uHv_3Q9uc5pePvet2IhBJXAestopydP4aflV_r5Y7sLOUDqDrJDp7DZq8v53xtLOFT264E_vogbBYJecTeKsf4kPTKegb2yw3zRh76_D6aX7h59yobxQR6r5jCymZazC0SD-efXO268CMvj8irGWHykKFuS1teT9BKtwT5CYGndQby81Iu_py52R1COSpvmlkpcm1_6fFGm6UcAnNfQRphlDNPMEUsAaLRdtrD78bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=BovWgWOIwfRnJex3k-lfW9DB3nz5vKPGAlre0lqHYfNBhtiJQZbMWdke12IhoqVlC-7x0Cs-vjooD7BZzSwU129A_H00yHcLLGN4SYwf-FZ4uHv_3Q9uc5pePvet2IhBJXAestopydP4aflV_r5Y7sLOUDqDrJDp7DZq8v53xtLOFT264E_vogbBYJecTeKsf4kPTKegb2yw3zRh76_D6aX7h59yobxQR6r5jCymZazC0SD-efXO268CMvj8irGWHykKFuS1teT9BKtwT5CYGndQby81Iu_py52R1COSpvmlkpcm1_6fFGm6UcAnNfQRphlDNPMEUsAaLRdtrD78bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7bh0ucQFLP78w3fJ-CjOih7Vg_On-wd1jMOVwhGzY8n_mRMyKoda64di28TBKlH9Lo0Na_F0fT8R8B2B8TRFOuF8EFQVvJ7fAp5tyy7wsPQSfDNp6Aqvfsm1Zgo0sTU3rsIOjukbT9AoNljyTK4z2MIGlAZCUYv4e9GIwI8NmEK7YzibQ065tXmHIdCtq4E2BxwkfWPG_BDaT4Avds7Ee6e-iG4ZUcz4qLYgWOSTP1d3dHOy4woDZvPGJ76eCHMIVqxM3AwN4G5uX1ZIVPr5mIBldAUYQRQIs0HJ-WuL9dSFyztvg0cE8husiowSjKo75jXnr7kYham1mdEWkYkig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=FkE5Nqv4qG88HWemPWVVBAuyBjU4Rt3ex9GhbzDpdEJVXYLeZ6I0cwwCGVdaJZ-ezYa65H9gFPQlt_S92j2JthqskN6VW7V5NpiKY-VlsTXxSkUkfLCRU81fcXMDi0XPlS46XUxUZUH--SSx04ecge0eHeaiVCv3aS6R293ufUqMhhxXE7ia0BuKB1qpn0l3ipGykWvL6D5kTX9Z_BtrnY3bKmv57j8y_HVciJwkeNQhkqoI-pZ410D2r-aIQ1QwU3kunl5f2VQWGDBwegnReY9aosq_razcXhYSDmHlT4Uo8S6mlLD5q9octWuhKRpLslmy25Ep8iN6ZVsGLlYXTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=FkE5Nqv4qG88HWemPWVVBAuyBjU4Rt3ex9GhbzDpdEJVXYLeZ6I0cwwCGVdaJZ-ezYa65H9gFPQlt_S92j2JthqskN6VW7V5NpiKY-VlsTXxSkUkfLCRU81fcXMDi0XPlS46XUxUZUH--SSx04ecge0eHeaiVCv3aS6R293ufUqMhhxXE7ia0BuKB1qpn0l3ipGykWvL6D5kTX9Z_BtrnY3bKmv57j8y_HVciJwkeNQhkqoI-pZ410D2r-aIQ1QwU3kunl5f2VQWGDBwegnReY9aosq_razcXhYSDmHlT4Uo8S6mlLD5q9octWuhKRpLslmy25Ep8iN6ZVsGLlYXTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=dPhXUUPzt2vp4mdr19tcnZaHrUdRcU9jrB9jJEU4XCg0OH6-E7eHwiIzyIBlvOe0_S3kZzt-u7k0t4pJMntAllfOHrSPkykquSJl81QmyqL9Hwe8UglXERix7LBaUdzHVQmxW5JrP-QCLGhN__WyDhKgImjyI4w3RUXtpFVAQPIJD_MJyZT5lzOhwtOGaO36mEs36G4fYfbUyULfvxZOO5Vr4bRMM8OZyoPgfKkuXRVkPdG3plmR3mak9hYYnVvmFzTW9Oh5jacKmMwuqW4MutML6DYKEKWa0Oo5d-LBbgwN42-cLcIEuZrWJXz08U8m69SGrlblS64c1IINz5vIPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=dPhXUUPzt2vp4mdr19tcnZaHrUdRcU9jrB9jJEU4XCg0OH6-E7eHwiIzyIBlvOe0_S3kZzt-u7k0t4pJMntAllfOHrSPkykquSJl81QmyqL9Hwe8UglXERix7LBaUdzHVQmxW5JrP-QCLGhN__WyDhKgImjyI4w3RUXtpFVAQPIJD_MJyZT5lzOhwtOGaO36mEs36G4fYfbUyULfvxZOO5Vr4bRMM8OZyoPgfKkuXRVkPdG3plmR3mak9hYYnVvmFzTW9Oh5jacKmMwuqW4MutML6DYKEKWa0Oo5d-LBbgwN42-cLcIEuZrWJXz08U8m69SGrlblS64c1IINz5vIPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KG1XGzKKjiAj3cTzQGo6Bp5w7vbLb3JxRis07Hh4XuWRZtGuCilJMwqIm03VaOdhMx9ZGuMq8uSPKk9SXnerDrPtJUn40T6VtlYZCLfPX1pHPhvNrVHY6-9_5qxNH7_ZWX2PSp1L4ikXxNI8fI7TBa9pWwPoZgFKmI81JTv-BReSETvHRf4vnwGUUGfHbSkbB9A5WNZ8-70mI8Y1A_PSvrBpAHoPm_HslL9DNhHlW-wppTiuvDky30P2zyDCGYUjfpEA_hlqtwFTHGooX95Jsvp_nd_768xOQm2F3wK6WhxH1F-bjx07XkQClD4dl3gQctiQRrUHb1TIO2KVnOALOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=pJS7UqFrgtAtknVA9CF49C87NvmTFfO9st1ZqB1ZkQUG38xmpyeDSZV9OkzTP0jGFIdBCzPoYdTTZVcPr6uqKgxn-xZTM4-GEmdbIOxbLlCLouEVshFRoTQymYeGLGJvBpFvi9Ztj-yRvR6FbBtBFukVct5R2ht5s0x3RXmfaOafDNKG-tekQwfljLa6uMacwcvwnymsheV5m9byfJQrd8jz6aCFLeH1N52DfRHVm2iK32yTp-RIGi_1l-eHhE9dBvJ_gCITAa_LjeL9yuhob5Q_HzaRFwTAFamOhiCyUPVYmp9ZzndFYVPx5m98XFxpLDRspXCD9Mh9NG0OsTeb8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=pJS7UqFrgtAtknVA9CF49C87NvmTFfO9st1ZqB1ZkQUG38xmpyeDSZV9OkzTP0jGFIdBCzPoYdTTZVcPr6uqKgxn-xZTM4-GEmdbIOxbLlCLouEVshFRoTQymYeGLGJvBpFvi9Ztj-yRvR6FbBtBFukVct5R2ht5s0x3RXmfaOafDNKG-tekQwfljLa6uMacwcvwnymsheV5m9byfJQrd8jz6aCFLeH1N52DfRHVm2iK32yTp-RIGi_1l-eHhE9dBvJ_gCITAa_LjeL9yuhob5Q_HzaRFwTAFamOhiCyUPVYmp9ZzndFYVPx5m98XFxpLDRspXCD9Mh9NG0OsTeb8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL7fTG5PFpaJCmVANz8Q_wN7bIMpZbrYNDuBWNiYcoMIxZEELfPYj_hz7uyKq9ZKY8IdAvieGdwJKfhVSWrpiRNQ3zvigz7Qyy2-_i2bCbDownpzi1RwmHLsHzIxbBAAct8tA1mgTbwctRskF7iM58TB3D9KWp8KDHKiILKEgEkC4RGNWEnh5J1xje0CLFOnRpxZIjTKOPIZuhAYLK2Npt-w9dMUYoX9txeG1-L7QKFYOXXS2dirjgCHkmR0kDhl3juj1R_A7RIrVoWWaJaaUFEN-YmA6p8Pc3ESOKK_NbtUO5zFXUwt-LiPN3ryxYSXdV47kAFMO1AVwYnQ66ucle_o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJL7fTG5PFpaJCmVANz8Q_wN7bIMpZbrYNDuBWNiYcoMIxZEELfPYj_hz7uyKq9ZKY8IdAvieGdwJKfhVSWrpiRNQ3zvigz7Qyy2-_i2bCbDownpzi1RwmHLsHzIxbBAAct8tA1mgTbwctRskF7iM58TB3D9KWp8KDHKiILKEgEkC4RGNWEnh5J1xje0CLFOnRpxZIjTKOPIZuhAYLK2Npt-w9dMUYoX9txeG1-L7QKFYOXXS2dirjgCHkmR0kDhl3juj1R_A7RIrVoWWaJaaUFEN-YmA6p8Pc3ESOKK_NbtUO5zFXUwt-LiPN3ryxYSXdV47kAFMO1AVwYnQ66ucle_o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=kiNnbgR7Alx9-M5IXxzW38v2MNbbTIXB6TKnI-roY4Jo2Zz8T7QhZWpPl47p8aw8howqGmGv1crybHs9e-w2gzbWMdI-8b98yF_1-ucsqhblsM9OKa24UEarLpwmdSBHNbjQnX5j9-mSEMBfYLT3DRzFwAVQ9a8za5lYTusG5AYARPRdhC-NnZv8hGCwufKidKk-PefAsMnPmXmrniNrQ2HEnmoxPdbvN_X7K1YFRdNyJjWkQUcL19S11es9t81sawOvTm8-hgXKnT9PY8NmrrlENQ8I1aOQ24Svw6CMHpvTMkvpcSzS-Kx_pzDmuyNWbDL_ALtdUK7pfk4nZt3nww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=kiNnbgR7Alx9-M5IXxzW38v2MNbbTIXB6TKnI-roY4Jo2Zz8T7QhZWpPl47p8aw8howqGmGv1crybHs9e-w2gzbWMdI-8b98yF_1-ucsqhblsM9OKa24UEarLpwmdSBHNbjQnX5j9-mSEMBfYLT3DRzFwAVQ9a8za5lYTusG5AYARPRdhC-NnZv8hGCwufKidKk-PefAsMnPmXmrniNrQ2HEnmoxPdbvN_X7K1YFRdNyJjWkQUcL19S11es9t81sawOvTm8-hgXKnT9PY8NmrrlENQ8I1aOQ24Svw6CMHpvTMkvpcSzS-Kx_pzDmuyNWbDL_ALtdUK7pfk4nZt3nww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=As1Je6XdYG3yhpCtPFk5fBs4lZzZ_GMsoYrzls0BQA27cRRlHuVzkHhCE9geM07CHA9jcM89keTQ2thSpHNk41Z2RGSWpBoPgq2TJVfrDCHsscHwGLwK25Ju64liHfSULccXURcSItDyHjsZ4bsuRlfE3d9TIQv1xVpB3HOLnNJ8oie2LlBPEN1tcbm79-0V5eqamJd_KZtWuucK0jQeFMOCrfondN31SNtUYkf67iptjpVnoMkvu7dO0i867s8JBM1GnyXUErBkw5sEm79ozVdCiczYnSH7A1JfYtmr7GpqhNBm8IiUOYLJf7NrIihyGThykbEJKHNFE-3JY1NP8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=As1Je6XdYG3yhpCtPFk5fBs4lZzZ_GMsoYrzls0BQA27cRRlHuVzkHhCE9geM07CHA9jcM89keTQ2thSpHNk41Z2RGSWpBoPgq2TJVfrDCHsscHwGLwK25Ju64liHfSULccXURcSItDyHjsZ4bsuRlfE3d9TIQv1xVpB3HOLnNJ8oie2LlBPEN1tcbm79-0V5eqamJd_KZtWuucK0jQeFMOCrfondN31SNtUYkf67iptjpVnoMkvu7dO0i867s8JBM1GnyXUErBkw5sEm79ozVdCiczYnSH7A1JfYtmr7GpqhNBm8IiUOYLJf7NrIihyGThykbEJKHNFE-3JY1NP8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
