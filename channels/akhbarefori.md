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
<img src="https://cdn4.telesco.pe/file/XGPjN6iDDvlF36BxpIbKJCAM1I_B4lkDcU8sD0Rxpo6ta4_3BU8iZQegmZvgsTK0EVBP2Gt6dgD4ouxlRPrZugqZNsluAVjbaPorTawDZpPGT43efdiQLXGnrCTMm9V9hoXkruQY0_3UUWXjgz3cmm67fGIKyjKnHreVVx3XfPnc4-hQGYS_IttutZ2A3Q6w6kx-LxV05vg42CaHhdsdpVL1Ok2MluVEFwDCa-wMJufGXSBWi4qTPWy4e5rFYRh6HkUlyFXBKeBb92c9TQbSTUcxnqbzdHi6QczU21GZ2CwSqYjhfyW1SJP3yPje1FhBmyDOUqd7dSwBHCV58jV7FQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 23:33:16</div>
<hr>

<div class="tg-post" id="msg-657498">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awu2XhKzGatyO-80MW9KXmOmZWhQHPiS4DM4vWpE5DHzgAX0ln_jsu3FZC06YspKqlSeU_Suv6MPBqDhcGz0PDxbXm7dkhvrSuwj90pzE5PzfQcmzxrGlhQC3RVBwTpAsFNHFinyqAe7bHR3AUQ32FlmDiLIiliLNN7XIHQ2Lg8WoWuWjyP6_C8JnCqhXR93SitKw5r57fYKjezXBrILFKCnu9wSx06VjnfaLfiZfuoRW18yme7ahGASZo_sIbvGFxY-U8zJlmvKSs_86dwVMIimLR6retaMsmS9fHQjA3S7Q4bRfdRUvp19cXknp4ZJivMwcYm2G22Te4tJbrDsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه قیمت نفت برنت و میزان عبور و مرور از تنگه هرمز
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/657498" target="_blank">📅 23:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657497">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
یک مقام آمریکایی به آکسیوس: نتانیاهو برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/657497" target="_blank">📅 23:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657495">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxIaYzg_8J8P4d0Dd2flcirAzDPOgMy7KpeulQ4nV48YmjUj2MclrjB2lxVR4gjoo5PjnnYy9MTPG0iz7FnFqAZPlZOt9oI6nMZC4wV5nVjgBXPxXhknBL5wnxG-gh3g2-9BiShWMv9eozwhmOe8myVmjzu-VnS8vNBop4qGDpnzmzKWhTtBvvCpQONKTEre-ar5rgZlhHeCtbA1EZR0BLHWgF8pJsdfvoL9-E9MQc0HGIn--FJxZ7tqZmDkBzDWcaudrOC63sofGP1cErBhz-H_Cu8mWNGum9hSGssnqUAA0UIJ6VrWLEqK_OhrZ9C-RLZq1Vy9UB7jGDiuaXhrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقایسه عبور نفتکش‌ها از تنگه هرمز در سال‌های مختلف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/657495" target="_blank">📅 23:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657494">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام نظامی اسرائیلی مدعی شد: نتانیاهو به ترامپ اطمینان داد که هرگونه توافقی به قیمت از دست دادن حق حمله به حزب‌الله تمام نخواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/akhbarefori/657494" target="_blank">📅 23:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657493">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad56aba44c.mp4?token=MTTRqp2RrV9P-f2FpywSU3RhNH7NUOasVYhSMFkPfdzzwDPtMZAyaso33bPmgqVrTU6J1Se2DSEzLqU1Dff-N6t3KZluGJzlAhjNeXKb48b2JtytQtGZ-lK2jjgjX-iAKxfEQkKr1TaM97OFDDvzyq3_o_mcQkjgJMUoWeXpfgjI1u2m0ZimxopJk7IzMCxFNIcxYnxxftNtN71syQ11skChbzAP7PqoxjwjOqhxZJpgpYyrBggO0E3JbneESwz08WHtvjv9wGcNXm4XlbryiMvfqLBQHI_qyhWdVtL-NAu4aXDoh4H3r9FyFLkJD36qzLyBcPlEKkiXct7QDDdeXpIRzAE2zQ5o939LEyYf6i79drA-Go55cQIfjIokHhZlFv4i9_h1WTD9ruCDibHxcJ8ifja5seyURF9KkvSI9x7xS5AHxGUyZ8bbfQuw2CE7Jntq8_1TEJNWM6Ko1q9LUeF8_LR9orlKk_ghXFcDucTj2AJJBC-c2Rgse-7dQFS7r_-8R1OWx59LQwRJoc-P2kXQnsOd4HgUoRZQe_W2twWTqRVo1v72t1u0_HakXWtLEQnTYaYO9I-Aw3slZUt6Cg6hXmXWvloeAEYwQweGdXOGwsQ9WrzQj8BYTcibjGrPEl9GiplYFoiJgprgqLYofyWf321OIgrmJWezuRkNaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad56aba44c.mp4?token=MTTRqp2RrV9P-f2FpywSU3RhNH7NUOasVYhSMFkPfdzzwDPtMZAyaso33bPmgqVrTU6J1Se2DSEzLqU1Dff-N6t3KZluGJzlAhjNeXKb48b2JtytQtGZ-lK2jjgjX-iAKxfEQkKr1TaM97OFDDvzyq3_o_mcQkjgJMUoWeXpfgjI1u2m0ZimxopJk7IzMCxFNIcxYnxxftNtN71syQ11skChbzAP7PqoxjwjOqhxZJpgpYyrBggO0E3JbneESwz08WHtvjv9wGcNXm4XlbryiMvfqLBQHI_qyhWdVtL-NAu4aXDoh4H3r9FyFLkJD36qzLyBcPlEKkiXct7QDDdeXpIRzAE2zQ5o939LEyYf6i79drA-Go55cQIfjIokHhZlFv4i9_h1WTD9ruCDibHxcJ8ifja5seyURF9KkvSI9x7xS5AHxGUyZ8bbfQuw2CE7Jntq8_1TEJNWM6Ko1q9LUeF8_LR9orlKk_ghXFcDucTj2AJJBC-c2Rgse-7dQFS7r_-8R1OWx59LQwRJoc-P2kXQnsOd4HgUoRZQe_W2twWTqRVo1v72t1u0_HakXWtLEQnTYaYO9I-Aw3slZUt6Cg6hXmXWvloeAEYwQweGdXOGwsQ9WrzQj8BYTcibjGrPEl9GiplYFoiJgprgqLYofyWf321OIgrmJWezuRkNaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واقعیتی پنهان مانده؛ پاکستان دارد از جنگ ایران سود می‌برد؟
🔹
پاکستان این‌ روزها همه‌ هم و غم خود را برای توافق تهران و واشینگتن گذاشته.
🔹
حالا سوال اینجاست، چرا؟ چی چیزی پشت‌پرده این تصمیم است؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/657493" target="_blank">📅 23:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657492">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
آذربایجان حمله اسرائیل از خاک خود را به ایران تکذیب کرد
🔹
باکو گزارش‌های اخیر مبنی بر اینکه اسرائیل واحدهای نظامی و اطلاعاتی نخبه را در آذربایجان به عنوان بخشی از شبکه‌ای از سایت‌های مخفی برای تسهیل عملیات علیه ایران مستقر کرده است را رد کرد.
🔹
رسانه مدیالاین نوشت که باکو این ادعا را «کاملاً بی‌اساس» خوانده و گفته است که هرگز اجازه نداده است از خاکش برای عملیات نظامی، فعالیت‌های اطلاعاتی یا اهداف خصمانه علیه کشور دیگری استفاده شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/657492" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657491">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: اسرائیل خیلی دیر ما را از حملات به ایران مطلع کرد، اما من در نهایت توانستم دامنه آنها را محدود کنم
🔹
کشورهایی که با من تماس گرفتند بسیار نگران بودند و از توافقی که با ایران در حال مذاکره هستیم حمایت می‌کنند.
🔹
ایران می‌خواهد به توافق برسد و این اتفاق می‌تواند به زودی رخ دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/657491" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657490">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53478ab0e9.mp4?token=CzwmgyD63fs7GBreiYIoL643_dl2GBuyt5-3YticvRFOBas068DwpK0kzWxFyPF98ZikFCSYsCEtP1AO3bFPj6KDLavanzOxyyqqhcRYDfyM5c70LhqnLSokWmS01ZyNpSlVPZIawYV3D_K3UoTygCruKHcVq8nDqwhJAyw3ou4eLOb-QoLUOGu-OkrqxrPBUboi_3zVqQWRe-poMsK1ic5_-dUcZXvaUnG642rnxVPs63WYwr06PB9AgYB0w8luRQFYKvnUkkv9PPJogDzVg1GBv5ObWmINoII2u6rVtCZb3Nitm7TXMRYskt0uPbeJRPSbTzbYyhEZPyy445Jhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53478ab0e9.mp4?token=CzwmgyD63fs7GBreiYIoL643_dl2GBuyt5-3YticvRFOBas068DwpK0kzWxFyPF98ZikFCSYsCEtP1AO3bFPj6KDLavanzOxyyqqhcRYDfyM5c70LhqnLSokWmS01ZyNpSlVPZIawYV3D_K3UoTygCruKHcVq8nDqwhJAyw3ou4eLOb-QoLUOGu-OkrqxrPBUboi_3zVqQWRe-poMsK1ic5_-dUcZXvaUnG642rnxVPs63WYwr06PB9AgYB0w8luRQFYKvnUkkv9PPJogDzVg1GBv5ObWmINoII2u6rVtCZb3Nitm7TXMRYskt0uPbeJRPSbTzbYyhEZPyy445Jhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بسکتبالیست زن آمریکایی اسـتقلال، مسلمان شد و در ایران ازدواج کرد!
🔹
"شیا رائل ویتست" بازیکن آمریکایی تیم بسکتبال زنان استقلال اعلام کرد مسلمان شده و با تصویربردار مسابقات ورزشی ازدواج کرد.
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/657490" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657489">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms0FGx4cwjGD2mdW3yMyF-ZGf9UVNjCIiQehnyAyxVZE2ExMOiSI2OIXQOXDLe04dw44Grygg4DBR81VBekhOPWHD-lK7srVQTNkbg1-d-MHpgPR2cXrS_bThX3EKIR5vnrD4ELhv9ci0xnM4iOtDZIFwE3FaM_IcEFCNq_ScRoyMrzHYHJZrAY73KEWydjIyHdI4kUISDVr0t4XB4xFf6_9E0lQaeXI8NbplOkEaOGXUBZCa9VoZwUbripaY2CaK3mFfCGQn_gznjtfFJjK2r86UPITJhkDH6qB_FdN8XUX3uIlf12kO9cbzRDwTDH1BNLl0bKBJVj4I0IPfdTuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جام‌جهانی فوتبال همیشه سیاسی بوده است | از موسولینی تا ترامپ؛ هفت نمونه از سیاست‌بازی‌های یک جام
🔹
جام جهانی فوتبال هرگز رویدادی صرفا ورزشی نبوده و در طول تاریخ همواره به ابزاری برای نمایش قدرت سیاسی، تبلیغات دولتی و ساخت تصویر بین‌المللی کشورها تبدیل شده است.
گزارش خبرفوری را اینجا بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3221464</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/657489" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657488">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070d993c60.mp4?token=gP03gm-kv--piXNYkCcxSVC8VRvi8zrsHCVGjskwkOlN9S155fHh2uz7mTdo1k20ttRI4M1yD03Qsc95DzlyuuhQo166IxIgVoADNaacfLmtdKn9jn6eaaUjWVVBrYaJwbrHpg4SAvFJ8YUsb7WN2t_sSNMXsh0npnbSFZvkZC1rgkikDQk4BClWr13dLTVxFv3QRM9TuwUujP8QDsiDs5WO919BfEFSCYIhLf1lUHEMmJMBXSBZub-5VLoXHFEVq8a3Tir-UvjiyGyPXc0vRcdLgPZHlHTfXxdCv69orWK7owbNRMCaEZa4PHy4aWOmaSU7HBcvIZpl8RPhFRPq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070d993c60.mp4?token=gP03gm-kv--piXNYkCcxSVC8VRvi8zrsHCVGjskwkOlN9S155fHh2uz7mTdo1k20ttRI4M1yD03Qsc95DzlyuuhQo166IxIgVoADNaacfLmtdKn9jn6eaaUjWVVBrYaJwbrHpg4SAvFJ8YUsb7WN2t_sSNMXsh0npnbSFZvkZC1rgkikDQk4BClWr13dLTVxFv3QRM9TuwUujP8QDsiDs5WO919BfEFSCYIhLf1lUHEMmJMBXSBZub-5VLoXHFEVq8a3Tir-UvjiyGyPXc0vRcdLgPZHlHTfXxdCv69orWK7owbNRMCaEZa4PHy4aWOmaSU7HBcvIZpl8RPhFRPq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افزایش تلفات زلزله فیلیپین به ۳۲ کشته و بیش از ۲۰۰ زخمی
🔹
عملیات جستجو و نجات همچنان ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/657488" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657487">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارشناس اصولگرا: آمریکا قطعا وارد جنگ با ایران می‌شود!
ابوالقاسم رئوفیان، فعال سیاسی اصولگرا در
#گفتگو
با خبرفوری:
🔹
آمریکا قطعا وارد جنگ با ایران می‌شود و بارها آمریکا ثابت کرده که از جنگ با ایران خارج نمی‌شود و از دوره قاجار و پهلوی آمریکا به دنبال جنگ با ایران بود.
🔹
از صحبت‌های ترامپ می‌شود استنباط کرد که آمریکا شکست خورده و شروع کننده این جنگ آمریکا است و به دنبال تنظیم سیاسی غرب آسیا به نفع اسرائیل است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/657487" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657486">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اروپا تحریم‌های جدیدی علیه ایران اعمال می‌کند
🔹
اتحادیه اروپا در اقدامی خصمانه علیه جمهوری اسلامی ایران، برای  نخستین بار با ادعای نقض آزادی ناوبری دریایی، تحریم‌هایی علیه ایران اعمال خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/657486" target="_blank">📅 22:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657485">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebda6e9ef5.mp4?token=XVu_wVG4QlKATQTKOGu2yV2v7hNW5uRRWnmdj08g9dCJRwg6M6iOHb78O8iKAFHNOBBm2LoSei7O8HYb2y5_U9PLsSVGsXcSJteX4fv0WaHHfeoY-vH4PcUIxAmUFdtCmynRP8zb8Y2rwyISq8yFCm5tJW_z07eBS6VbxjXnv5rVlHdkHTPznOo3f9z8-H8VinmfWnXjNrJGZjWGtZIi4Lr_aPwwnJDglu23mSrfgK13PSHpVF1FM-eJr4ucL4cudGRJCsPPhrEtAiuJx4sn-68zzeIEEg_6N8O1oKtxmhm-_qaMQ1kVg1MYIOGvVM-1IZ3gML2mAMm3iQHJFFUesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebda6e9ef5.mp4?token=XVu_wVG4QlKATQTKOGu2yV2v7hNW5uRRWnmdj08g9dCJRwg6M6iOHb78O8iKAFHNOBBm2LoSei7O8HYb2y5_U9PLsSVGsXcSJteX4fv0WaHHfeoY-vH4PcUIxAmUFdtCmynRP8zb8Y2rwyISq8yFCm5tJW_z07eBS6VbxjXnv5rVlHdkHTPznOo3f9z8-H8VinmfWnXjNrJGZjWGtZIi4Lr_aPwwnJDglu23mSrfgK13PSHpVF1FM-eJr4ucL4cudGRJCsPPhrEtAiuJx4sn-68zzeIEEg_6N8O1oKtxmhm-_qaMQ1kVg1MYIOGvVM-1IZ3gML2mAMm3iQHJFFUesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
ادعای شهربانو منصوریان با انتشار تصویر دست زخمی خواهرش: رئیس فدراسیون ووشو با چاقو به الهه حمله کرده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/657485" target="_blank">📅 22:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cIY-qH31K0g9gjKP6iHzhm9ZPDw6VZ4FrEzsCFkV6xzINihRwKjVBuJNzB4jbct-BnrejiCoWQ76BmCIwkdBYRX-jHlglhpj2HKFPr6AbvlsCH4RwNGyzS_So35AbFfeyX9K8lX-wWMqOQ9ERgM7Nm3GL6rrz8vroDtgpOXEpICSvpUNbWJHHB972HAMerELyQ9UzcIoMYd-WgfyKV4OiryUzYbh4ZFLwBEmBtAi--qd4o1ON18hjE6ycfGlGkb2nq0xMzgfaVaIVAqXEpCLNlyUGx9no_1JWLPp1EoNL2NfErOhc0a_h_unxLxt2L8loNoeOL_ty-BzVnjddFEROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DQDZa5uTUwxu0yp2y00-p3bNfC-IjQzaQ7y7SrxSGmm7lBZyevLblyJ7alS_K7AzSY_CMXzU8LND_esgEo2FYivICO-CPpNyZ3-7oMaQC-NkDvpgDp7iPyC83lnVVVsGF0hQDTjwSU5OjIqflv92EzvlCUl7SJTZDvo1P-ygpUW9oeRei5killF5lByns2gYG13zvOv6B7p_37hMhL82lSSQS9buZM5UKul5R3dssRuUlrbHZWhOm0gVXXA71lYhOznTn8cKUxqgeyDvIwmLMihKsvTwwtw447mtd0689-8K2xD4UUH6gz0aXosjNkJw7Dx9kMHtnV-Vloms3SYZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n-8URXAEgBtg8MZFEfsCY6cy6EE7GDR_afSZEsb4ezu6T8SFiE3VMouxwmnJZcpmDMi0jUC6VGAeRL-aE-_5xo5FhGFKR4H6wPCQcwQkfxkPiHnPm5XfQHq5x4MUaOYdp_oiOT5yujHc_bMA6s5pgsLzThPpFGIrupcPQHXOpzeE1LuGsVWIDKIL2XMrH3Z0LqEJ6dhNVHzooR_4W-CkZm-b8IiNddVPzqKNSEPi8uLMe5zEdk9E5qP2e1R7nNFg9fxgBet_i3MaOftUmgzZ8HWfG6MVaUWz1nboP7QvpTbZJeo2UKw2q9YzfP7SGMefOVY90D63p_ZsTPeOR-pJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9kAIu8vM-gjF9Isi5QJz-rX62YilW7cBimq-qTvJ_fH9dVSPC4l4IF5g778EBoGWag_lK1_yEgBS8mhKy-AWZvquRxOqTIybP2VfcMUFZAXUmTECfMuAMLqREdD5XRsnhMuFVdagtQgZTRx8jYpxuxqtv1a6-tj5w29aMmsm5w3zxx2AQrpcw8JOFvik4Kh67btfnRZun-PixBGjdLw_NMIvTRHYucTsoMT2ZThGm6dUm7GvA5EaQa1TGzhY3v7xXqpx3b2hOILshGGuIqOxu6nz2iBBz6tlkuydg9Bejx4SibCTNubdYiPOV-ajmnOK_E31DQPcTodeB5VPuK8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oq5gM7Nkz_irj28vwkLU_x2olkebXCO-WFU7yuiZvJCAzGSvYxNW6lBDnJYTRfeDD0TVGvldTlVTJ64u4236vEOKASQ0-DEINbGHNxZ1kEoinJ7TfByXwnAm3SQNjyF-Nf7drPtwE0jHUlSPH9YgHvoYPJOqlNgnnViV72Na4Teh7SgKpWxxV-r0l_UuoMjpC4ZpiQTa5teoRrQLp4lfps8SvhUZzea_QPOgVAO54ge-rL3qv8NewZXFh-nlWnIVFa2CcqLKgGdL8rRjoXg1GefF9-P3CIXLiQzsR6xvbnopqDM90hmxjZqpJvr-IZN0lu8eh6rguCLZfogFN6nCvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWOx716R9_K2bfPkKC6MLSC79aGdnBhPSgZszphA--OsR4Aaq9MI1hXd4D3I6OXD3bwdzMLR-EiIALtPkcXznCwGns8c1Lb7ayH4Zd-MpiJ7013HpesQGHpQmKuQvEyC2InZ626Y0uDmPazOFVXc8SE3zAcPyfBkq6aeQsgk93cJMfegetxw_CMb_TzOgyw0n16ysmLbLFlDsfGyTndnhzaU65xsi9PUlymLa6GJCK0uOw6Pov5qVYbRaoewDe8GDlZWmCRHHSHJRX--Io5LL6-d448SMZwi7x2FUCpnKjb9_32x-gOiGwu25Oi_uD_ac1Y1ROPfBnXOYyrkYVe4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r2d8W9i7QK8QCrcrVhqqcR6Qzq-9_mUJqBeXnxh0VWqNTMBe7R7n0OPkgJPw8BNoc7XGGrGVa8_bJsiM1f73hG4FtSHu2KbAH4ehamLNt8-7ci0gROlwcM2yVBfjg_5BSl7_XPGB2EMTW_x_ckB1wO0f0CuCxQOVi9oLN_wTQscUs6xkRzkAwApvWk--C3Ov3zDqCUtOYAgtCR1aw-tPMyWAeJ5VmBULu3UlMac8QsH2PxDqRaGtulMgwcfKKxKELTi29iL6YYn_GZvsM_vOdCZAPQkj-SYb98G9zZ90Ho75qZGprJNJutpI8_31I-ENDM4qXkhnvc4Sof0L26TcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSJ1ltNWaqhhFKqrVu7QqgenycXRXj2nnKxUGvICeiG8EI6neyyTIxziA_EN4kaLG5XbjzBexfp7Oie22ibObsIaEItNdijT0DbPo8WE8s1k9oU_hhF5Wl6cvGQ9rj-w7YkvyvfqILeAK_Q9eH4jB72tG_XvQnAAKxH_FwmaSqM86IntjdecVRZkHTH3_7Lcqx6JLmzLNqYvvcenXki2O3z1fhN1DxpJpOjJkvx1XsJUnMFG8vnKWP0SGhSEe4YCbjTQQmAa20HqcYWRBESjRd7__wkXcVPs0OJWESfTp5imL001EpjZAUmQkmopx1X6tyPd-uVcbojAjsNWleuoLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت برکتِ همدلی
💫
هر روز، به پشتوانه
#همدلی
و همراهی شما مردم عزیز،
#هیات_قرار
با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی میان خانواده‌های حائز صلاحیت، گامی در مسیر حمایت از خانواده‌های ایرانی برمی‌دارد.
ادامه این مسیر خیر، حاصل اعتماد و حضور ارزشمند شماست
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/657477" target="_blank">📅 22:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657475">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14432d14e4.mp4?token=LsTALVonqhD7PjBA9l64WQq2eaYOP64VTOStYCN_K20i7boQwQB76aT-9CvNGHRkNiH2GTgsdqDTVITCyJku9IUzgvUbl27iOmmhIE621EFTs5X7qAifZ6y-zimtVcMkTWYZCQlK3ObeH3my4JbCoJSEh3iqFmiooP6H6v0QKa4Z3G5-WTZ9iPqXIJyDrh4GamrUxpi6Z1PMg8fzVy9KwCQ2ULdguB5fEDZ22CGcZUorCpUs0BUwL0yC3-mq11sl3KNIoYLY6qobFP-UA__oVBFrBYDKFaQz1VBEp8hcIUJzd-7KV5AWN4-VMHzyye0Okd9xGDB9ODJRGU89gbTM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14432d14e4.mp4?token=LsTALVonqhD7PjBA9l64WQq2eaYOP64VTOStYCN_K20i7boQwQB76aT-9CvNGHRkNiH2GTgsdqDTVITCyJku9IUzgvUbl27iOmmhIE621EFTs5X7qAifZ6y-zimtVcMkTWYZCQlK3ObeH3my4JbCoJSEh3iqFmiooP6H6v0QKa4Z3G5-WTZ9iPqXIJyDrh4GamrUxpi6Z1PMg8fzVy9KwCQ2ULdguB5fEDZ22CGcZUorCpUs0BUwL0yC3-mq11sl3KNIoYLY6qobFP-UA__oVBFrBYDKFaQz1VBEp8hcIUJzd-7KV5AWN4-VMHzyye0Okd9xGDB9ODJRGU89gbTM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله به مقر گروهک های تروریستی در اربیل عراق
🔹
منابع خبری از حمله موشکی و پهپادی به مقر گروهک‌های تروریستی تجزیه طلب وابسته به آمریکا در اربیل عراق خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/657475" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657474">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
حمله به مقر گروهک های تروریستی در اربیل عراق
🔹
منابع خبری از حمله موشکی و پهپادی به مقر گروهک‌های تروریستی تجزیه طلب وابسته به آمریکا در اربیل عراق خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/657474" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657473">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
رئیس‌جمهور لبنان تاکید کرد که کشورش به‌دنبال روابطی خوب با جمهوری اسلامی ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/akhbarefori/657473" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657469">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدیدرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_e20kZc7TYICOBGY3ELjetnYiZEQvFFS16R3dShhLQm9BsO2VjXk-dYVFHotiMSITTL20JLujERQXA20Z_I5MDXpfSus5Vn3TvsQGrkPIwxSMgJuBvVS1nnr6mDN1eKU0OHlhbw0GSLMJuM-s_Q8lREF7sE31nTge5i-Pv3jIz46GNz9xRzhN6UPeLAfKffLF-1QA9NdOe2Hjdi4iH6K0EZ_R6Zpg1pxDVzmiD-jKE_S7ZPCcJyBmwtMZXFxKCxegFxrs6O_GBCOQHwiZofra0EKVdFhYTIENUs8ZWX3Qygvrzlfv1vn6h9wmqaFKA7QuyacIpAHpY2LBsuQjWH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q8LbOMrvblhkYSAx9--1iSzcyTnP_sLxjpRuLPy7nADNb9YKAJnWeDJvyiuo0zIPQxBwVsqKSOAYnFEc45fogukBBLOUeUgwJwdOFfjWBNQ8TJZy8m8wE460eZaM6Lb3FmwO_8staaTtveF75jprPTWmPEPccgjgb9cRNCmpdBasma0lN8ay0q7RlLniOkokSbPh71pakMVOw08T6roxmyb0Xt4OMieLaTq-HHyMIJtM3O6z1s-cd6Ht1oaI7hgsPbxEFI-oxx2ZW_T1F4kerUS7yuicezFnpLQ4p2gMZ6sB_N6YllICkW0M9cdcAf3IW_DZYwFhYK044V88STMxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYIc2X-EZtHkjlVQbLpOh1S_3mQGPBoyKAkIV7jXZXVMu4ICral59rYBnMv00Ux5YAju7u4qZcBX9aZxNop9jDfHJGTD8yCqQ9usEZB9-isj8QkMtoLLwQO05poGtlEpxoM9JWT9eHgMufidZqxX8rGLWgTbZ1g2jdc-B_kAnooFlc7m8NUJMol98rfrQcC7JYIUpKylPWRHkZytEUZP6oxVJpPc0xsNz4Q4ZaTaKnpQFd_P14cjr7jvR4hjJ9df1KUAk9akfQe7sKCvtIkujpSMuqnPV586daIjc7_tFamy3LzZve61E35_6PY9kxH9ejplHb8NOTTqLIM3cH0trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvKf9u40RU0_DkqAE4CNqOFAUctd3awch7K4tmaqutZVpeZEQ53AteJISQuUbc00ct7tQMMpXPYfPUbI2smKSbUrr2vRa6kAxSqhwWIzvZeLQunWsXuCOl3Pf-du30P6PR1INuTLQCjH-3t7yXK4zAzAg2NjRlSh1GhNLJ8TXNomIiUhszv4SY33cbRKtOVxFrAl3kwB_eK6OavMnrNvcVIJsIprPoFZc7j8KZF4t-kUVZJVm3rWAT7jjQTfVHbEUmtkPK__XQbXvPO3j3zRtLKGDSgOxeN-1kIuTn0OXXaEzDxUFk9DRN-gtTng8Ie9nHM549se65gXulT0y5WypA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
جریان معاند و بهره‌گیری از تصاویر و ویدئوهای جعلی یا قدیمی برای دستاوردسازی از حملات رژیم صهیونیستی
🔸
آنچه در وقایع امروز مشاهده شد، استفاده گسترده محور رسانه‌ای دشمن از تصاویر و ویدئوهای جعلی یا قدیمی با عناوین مختلف بود؛ اقدامی که با هدف بزرگ‌نمایی و دستاوردسازی رسانه‌ای از حملات خود صورت گرفت.
🔹
بررسی‌ها نشان می‌دهد هر چهار تصویر و ویدئویی که امروز به‌طور گسترده بازنشر شده‌اند، متعلق به وقایع گذشته بوده و ارتباطی با رخدادهای جاری ندارند.
🔸
در چنین شرایطی، خودداری از بازنشر این محتواها و قطع زنجیره انتشار آن‌ها، مهم‌ترین اقدام در مقابله با عملیات رسانه‌ای دشمن است.
🔹
شبکه مقابله با روایات و اخبار جعلی «دیدرس» از مخاطبان خود درخواست می‌کند در صورت مواجهه با محتواهای مشکوک به جعل، قدیمی بودن، دستکاری یا هرگونه ابهام درباره اصالت و ماهیت محتوا، آن را برای بررسی به شناسه
@Didras_FactCheck
ارسال کنند تا توسط کارشناسان مورد ارزیابی و راستی‌آزمایی قرار گیرد.
🔻
شبکه مقابله با روایات و اخبار جعلی
✅
دیدرس |
@Didras_ir</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/657469" target="_blank">📅 22:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657468">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiJgU9K8muavS22MQ3JHZ1qYx2GSCsAGBDmpjNX_fi60H0zQSh8pnZ4Ky74tjlPJEN8eYo5303n0XnyKE9oEq2Mz9eFSfLBU1WvuZRohlibmhnGsAl-zisJ7ls3nAUWilWpQr2yLQKIzoXoe8h9uBJq7PqMeYWJjFL8zwlPTrTsLYFlnumSNeLQw2jnSTbhe7pJne_JXRzL8BNdxknWZTW4IHKMKOi73iouX47Vl79-Bvg27-gXbE14GglODXtHxiS25CZLVOPvXFGoDDsSg_N1TCuj7JRHNAgBM3PKROQo4lfFQAB4XEJkdnMo_oClxz37eGIhw-WDLxEnqWXigBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیف تهدیدآمیز رسانه امنیتی جریان از ۱۹ مکانی که ترامپ رفت‌و‌آمد زیادی در آنجا دارد؛ از پنت هاوس ترامپ در منهتن و عمارت آبلمارله در ویرجینیا تا باشگاه گلف ترامپ در واشینگتن و قصر هفت چشمه در نیویورک
#WillPayThePrice
‎
#هزینه_خواهید_داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/657468" target="_blank">📅 22:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657467">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqh2kBB1fVubLR4yE8gpKgbOuoXkBKZMpapbkz2NCi9CTikgws2liJ_-C0OOvR7HKO4sJd916u4YTh0tGAo44Z_x3lrfD_jUZNmpe1BiYxRaEjLh7pddP7VmJchBneP37Smv0fQhyz1tCJT-RnR5EPoipaZKg96iiMhsaWOL3OSSpb86FPbIKZq2WIQJs1NBH-akopiiaXTj0eiakGOoJoJFnTe7I3725bzTMgXaH2GADxW2CpEt9xFSgde8HQpeSrlrIxnSou6IW4uPHyWa1THQsPqg66RXaULSwtnTN0pGBbqec0uFDhzVT-1FbxQVnaPyrH7u223tLkcInfpelQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خرید قسطی با دیجی‌پی
همین الان بدون ضامن، تا ۴۰ میلیون اعتبار بگیر و هرچی می‌خوای از دیجی‌کالا و هزاران فروشگاه دیگه خرید کن
👇
👇
دریافت اعتبار فوری</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/657467" target="_blank">📅 22:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657465">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c4f9536f3.mp4?token=vuLNkjzS2HtcO92oYmlpzrcCGqPnoh0cBAXg2ZDbO2p5_WXFotnvvZN-CkLkL26cElj7vBuv4d8BaquspxV3qWyPji6LK_vdmCfYzi54CGXe8CX8xdUFEqZokae3IX9udFQlYJPW9OFFmtOPb6Y9Dfv_FJKH0WUniumX9O2q1VS4EtEzlN0DpFesi1Vx9xQXczq7mpMUmUyiKPdA55iW2wH0ETtzPoL-lmF6nB4vyGT6Fvjew1B12O_oLGUZ7ijcgXtsoQwgjjZ5WdvmpjiuvdKU5orifS96v767Xz3Nn75ouAiABf7mbsh-0ob2lTWp4J-oHQuycqtP7_p4gFPJDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c4f9536f3.mp4?token=vuLNkjzS2HtcO92oYmlpzrcCGqPnoh0cBAXg2ZDbO2p5_WXFotnvvZN-CkLkL26cElj7vBuv4d8BaquspxV3qWyPji6LK_vdmCfYzi54CGXe8CX8xdUFEqZokae3IX9udFQlYJPW9OFFmtOPb6Y9Dfv_FJKH0WUniumX9O2q1VS4EtEzlN0DpFesi1Vx9xQXczq7mpMUmUyiKPdA55iW2wH0ETtzPoL-lmF6nB4vyGT6Fvjew1B12O_oLGUZ7ijcgXtsoQwgjjZ5WdvmpjiuvdKU5orifS96v767Xz3Nn75ouAiABf7mbsh-0ob2lTWp4J-oHQuycqtP7_p4gFPJDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی بزرگ در برموندزی در لندن؛ اعزام ۱٠٠ آتش‌نشان برای مهار آتش
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/657465" target="_blank">📅 22:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657464">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV0EGu98bRtmEjXAMkwhFmLg0aeel2_HARVM2wIWKwEyFGOcSYCs_XXeW01649Wwcl_bvNBJqYk0atfGA4iu29q3ZfsC8a2IYOsJbE1XSEm62jatL3b7OlqOofm7_2kQ-edstuISazJTzphdXbSe3WH-4tKadeLJLiCM73M1GiKBIx-2ntCjy0IoakOiny-6uUVOvBlyUviLysT6_QkKXt41FsO9V1lQSFFzcCsYwnPnpiQgOvAexiWHi86AlpevTTo1Zr9BqcSBDqH04H9ruDyR6LqQlYg0Ja_yJMYq4f7bXs3XhZeSSruY4O_VS9Vg8WdTo3sOxzioo_iFpm4Ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستاوردهای عملیات شب گذشته ایران برای دفاع از لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/657464" target="_blank">📅 22:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657463">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
وزیر خارجه فرانسه خواستار توافق بر سر هرمز شد
🔹
وزیر خارجه فرانسه به العربیه گفت که از ایران و آمریکا می‌خواهد توافق بر سر تنگه هرمز را تسریع کنند./فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/657463" target="_blank">📅 22:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657462">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAyafH7BndEIv7rg8h8ufs0Ny-E2q5SK1Oltup6IHVntOZWG445UZ0gZ6BHSdj6DTybz6ybn_shZphKE6Zzd6k7dfzDq_q8jqrcT855SXD4fjrtvn1pVe3ZjY0rvC5nRCeP9dzVVNPBcHTrEFICTD8mBJwERmpt96fDr9FMn0V689xPUbKib5MBTJlz8bG-YO8JxEU-83_gmBXFUOcRaVCaZzl4tBYvQi8Me5A_Toz5cCnLh3mZMnqiPmyd0qThDOmNPKdSWqU2NRTVYfWY5vK-xThORVc8uowOeMtFthgkIkuALWA7GLK2bLE4xisGntSrGkn4GpmziCuF4h4G1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهرمان ⁧جام جهانی⁩ ۲۰۲۶ کیه؟
🔹
‏اگر جواب رو می‌دونید، وقتشه که در لیگ پیش‌بینی جام جهانی «همراه من» ثبتش کنید!
🔹
‏پیش‌بینی‌ها از امروز، ۱۹ خرداد شروع می‌شه. رقابتی که فقط به شانس نیست، به تحلیل و شناخت فوتبال هم بستگی داره
🔹
‏اولین پیش‌بینی شما چیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/657462" target="_blank">📅 22:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657461">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD79GEh7JT-Cjviow_GYDAGn7-Kagf8e2iMgRgdhIkU_UT0C4STvp3As5JYRiR-CcXOuwTF3i9jQuB3SZIawHVd9SpyUno4CvVqXFKYO4mAIB-TJ6iqoIH7wQ1lXqqVFxB0GWmqLKAKxQrBQQYKXy27-gdyz9RFKGgJ5QKzXBjidcStzGTzF0-dHJX9T1YFqa53IZMH8DjkrM68mKpoGJ7VMc_CI-I5xrWt_oDHIMn48e3B02SNdwnbtT3v42ir6NbZ-6PUeOytGWD7YTiIRx_JZwFu7NcZvKMFLQcyK58BG9-H49cE0l1FK-_EvaPYwaphmrzvKoidtv9g9r9WFFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
To be continued...
🔹
نبرد ۱۵ ساعته میان ایران و اسرائیل که در واکنش به نقض آتش‌بس توسط رژیم صهیونیستی در لبنان رخ داد، به پایان رسید. قرارگاه خاتم‌الانبیا این خبر را تأیید کرده، اما تأکید دارد که این پایان ماجرا نیست. بیش از سه ماه از شهادت رهبر معظم انقلاب می‌گذرد و ملت ایران در انتظار خونخواهی قائد امت هستند. این نبرد تا زمانی ادامه خواهد یافت که قاتلان و جنایتکاران به سزای اعمال خود برسند و تقاص پس بدهند. وعده الهی تحقق می‌یابد و روزهای سختی در انتظار جنایتکاران است.
#WillPayThePrice
‎
#هزینه_خواهید_داد
🔹
هفتصدوشصت‌ونهمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/657461" target="_blank">📅 22:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657460">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24a75b678.mp4?token=njoqxvGSQFuFqT4AP2TxgaQOw0swNU-t8vLNUdKVLkfv3A4aw9m-4w0YVIPmlgekdYcRmWoDukUOB3x7ZsosiUDm9mxQnEtDIGgZGrx-qfdrzz3R13WNi1DrKNp2_QX8TTQmZwVGgZTSNQF8lNJq-EIIlJDfmv05P0-kj4mZHd6xgsxk8mlH7g9ReJr4vGhm4zNSLHh0VcJDGr8EdY1VNv-AsrsnjbLt6X0cqtH5jTRByzzacXV58Gfm3tc7WtD4RLdgAMJn1IQCPfX1Dg6rBHd-0NHSbyCMmuaR3Qq1c-nYpoQhVN6Xzo6za_qXh87PuEhLwDy45HMPHoSRbEVyoaAQCCQRihpwd4HWCE-kY9Mn5nmGMJBac6NjaOu1lswHc3mxPv9mwhLSN5CMO6DhDSxhGDbs136k-ITd97f_gwnFsmaXztN2d7HVRuC_dkyXrs9KoQmd57DUK2-QQQQa11J_w8P9kjjpGMKAaLBiT-tTFQmfxQZFHsE64byDrpD9oIwedjlHvTtmpOp8GAM68rNycJPhm3JJvvEnQyqLTbJRUL-AG5zzlMmH3kGVkjw_4pAvTLNq36CR07jKbqMSN7KaVliOxjx5h1rKKrnemXXYDVaHUxIMr3HzEBqSTIzRfV0bFYZmwDFd8kEfubc3-uRz-VlHGMWN55uvDPxrAVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24a75b678.mp4?token=njoqxvGSQFuFqT4AP2TxgaQOw0swNU-t8vLNUdKVLkfv3A4aw9m-4w0YVIPmlgekdYcRmWoDukUOB3x7ZsosiUDm9mxQnEtDIGgZGrx-qfdrzz3R13WNi1DrKNp2_QX8TTQmZwVGgZTSNQF8lNJq-EIIlJDfmv05P0-kj4mZHd6xgsxk8mlH7g9ReJr4vGhm4zNSLHh0VcJDGr8EdY1VNv-AsrsnjbLt6X0cqtH5jTRByzzacXV58Gfm3tc7WtD4RLdgAMJn1IQCPfX1Dg6rBHd-0NHSbyCMmuaR3Qq1c-nYpoQhVN6Xzo6za_qXh87PuEhLwDy45HMPHoSRbEVyoaAQCCQRihpwd4HWCE-kY9Mn5nmGMJBac6NjaOu1lswHc3mxPv9mwhLSN5CMO6DhDSxhGDbs136k-ITd97f_gwnFsmaXztN2d7HVRuC_dkyXrs9KoQmd57DUK2-QQQQa11J_w8P9kjjpGMKAaLBiT-tTFQmfxQZFHsE64byDrpD9oIwedjlHvTtmpOp8GAM68rNycJPhm3JJvvEnQyqLTbJRUL-AG5zzlMmH3kGVkjw_4pAvTLNq36CR07jKbqMSN7KaVliOxjx5h1rKKrnemXXYDVaHUxIMr3HzEBqSTIzRfV0bFYZmwDFd8kEfubc3-uRz-VlHGMWN55uvDPxrAVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی عجیب است که افرادی در کشور از مذاکره دفاع می‌کنند در حالی که رئیس هیئت مذاکره‌کننده ایران می‌گوید دشمن به مذاکره اعتقاد ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/657460" target="_blank">📅 22:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657459">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrVmVMEXkkzIYzafGoXKRuLIQ1cW0JY4t8H1gpdIRUivk-AwscPx8_OmAiA5X-vSgkOonyPn8hCSXfFvPSebuA0qwFmKTaS4CCa0iyaemXNukWvzR9gTredE8vUCsy1pk7NHXjBna6Aif09kIMP4odAdgsgZR_Go918P4in4b95n1B-25q7AmJRVo7hnquiMYCWhL-nUDhvnWf39kCwkxg3ZnqNuV09ay3oqDoQ-k_mxVleG8lD0cXEO-wHB5qLDmlFWsCF-Cl7fMUFqwjrxhj459Ci20jFYIs6ozQfzGg3jj0s7YboqFEdFz9l1YCrLT3fa0P8HQrsmC0kPFqya0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عارف: دشمن ناچار به التماس مجدد برای آتش‌بس شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/657459" target="_blank">📅 21:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657458">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
استان یزد فردا تعطیل شد
مدیرکل مدیریت بحران یزد:
🔹
باتوجه‌ به مصوبات کارگروه مدیریت شرایط اضطرار، غلظت بالای گردوغبار و افزایش شدید آلودگی هوا کلیه ادارات و بانک‌های استان یزد فردا تعطیل است./فارس
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/657458" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657457">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ee952df8.mp4?token=hURMeDJG1Bd0MWKRyBrkLNMUj5n_c4teK64dNjwcFR_JjeI-1dumBBCTBX4xlQmpCCn88rgFXWuPxF6ifcHXtFjCaSalohVrb5jMDjX37kZxrGkVMIkUhAcTHgdmxxxpyktV0VV1WVYaWaBc0xG5Rt41fg_mUsgae7wpEEwIvXIhuWMRkzk-qj62vyaMWf1afXRm9YY6npFnr4PP1whhrj45P0FkzL9d1_N0cRTEEI3R8LLttBSBJfmi0Jhm5ON3xsmhT6p6ETxu1eDT1s7PRgssJ-y6_aZEiW0TCbK_XuKSEXh1xlhKa-wZ7fsH12_EBtUl5lFgcqY1Jc6ZBRoAMV9bTfkMFkxiFwdOy-lYiZwzGD3Xg0cD5DI1TeBdia7YesAlNpnSg4aACjfnWOCkNi5n5KGxPntTE08betmX0tDOwj9D2V1wgKzOeER44gHBWUqhLwkaGcOxC-HoeKioN6tApxNzGzkFVo5abyKtCLenrwaYk2SiuFYRfGuWhB9ox7KSq21Oy8CsiDD6oPZsWxVlVNoP_1Ln8JkSdWq_vCFsKwRREEgZr2xXiHVpK1GwqMU6lnNPbFh1zP9wuyba3vm0A7wtKkxCsnLXM9--i0qERVze7hxt6R8i_ku0kOlucHUekUfgO6dlPmEqDWrTdqPLeMStWZ_-fZ5aB8Ja-fo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ee952df8.mp4?token=hURMeDJG1Bd0MWKRyBrkLNMUj5n_c4teK64dNjwcFR_JjeI-1dumBBCTBX4xlQmpCCn88rgFXWuPxF6ifcHXtFjCaSalohVrb5jMDjX37kZxrGkVMIkUhAcTHgdmxxxpyktV0VV1WVYaWaBc0xG5Rt41fg_mUsgae7wpEEwIvXIhuWMRkzk-qj62vyaMWf1afXRm9YY6npFnr4PP1whhrj45P0FkzL9d1_N0cRTEEI3R8LLttBSBJfmi0Jhm5ON3xsmhT6p6ETxu1eDT1s7PRgssJ-y6_aZEiW0TCbK_XuKSEXh1xlhKa-wZ7fsH12_EBtUl5lFgcqY1Jc6ZBRoAMV9bTfkMFkxiFwdOy-lYiZwzGD3Xg0cD5DI1TeBdia7YesAlNpnSg4aACjfnWOCkNi5n5KGxPntTE08betmX0tDOwj9D2V1wgKzOeER44gHBWUqhLwkaGcOxC-HoeKioN6tApxNzGzkFVo5abyKtCLenrwaYk2SiuFYRfGuWhB9ox7KSq21Oy8CsiDD6oPZsWxVlVNoP_1Ln8JkSdWq_vCFsKwRREEgZr2xXiHVpK1GwqMU6lnNPbFh1zP9wuyba3vm0A7wtKkxCsnLXM9--i0qERVze7hxt6R8i_ku0kOlucHUekUfgO6dlPmEqDWrTdqPLeMStWZ_-fZ5aB8Ja-fo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ فردی شیاد، بزدل، خودشیفته و کلاهبردار است!
🔹
بازیگر آمریکایی: "کسی که در نیویورک بزرگ شده باشد، از همان روز اول می‌دانست که ترامپ یک شیاد کلاهبردار، یک خودشیفته و یک سایکوپات است"
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/657457" target="_blank">📅 21:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657456">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNGjPET2fMz1WrPysGiVAvxPWbTzrIP7N_aXgbuZAVGX-sLI5NfEo_Bens_sGTo4PqPm36RXNDL_yqhqa8Ahv-DVR_Cikxpt9gJq82NQAJlf49QWbL54sfXu9d6iUrUUeBP6of-HdNlAC1YTHnJTlBD_getOY--F000WzNOSRoVPQO-FAH22ivFHPJ4WjssKfLkNfCu5rEUYNHk99Qnxjqa02HAHiIT5eYSgLTZHwoWBxGDiy_kDNu_z3M9XMdlOlENi_SsvWu9i1cz-ZMBRUFL7J92aI5ogpSKoIJeoVPyQSxTkmaOio1bTPKB-_GYnMyAoRz_zunu-EAsrCxsujQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: از تنگه هرمز تا باب المندب و از خلیج فارس تا دریای سرخ کمربند امنیتی جدید مقاومت خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/657456" target="_blank">📅 21:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657455">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
سن ازدواج ایرانی‌ها چقدر است؟/ تهران رکورددار بالاترین سن ازدواج در کشور
رئیس مرکز جوانی جمعیت وزارت بهداشت:
🔹
میانگین کشوری سن ازدواج مردان و زنان به ترتیب (۳۰ تا ۳۲) و (۲۶ تا ۲۷) سال است.
🔹
البته برخی استان‌ها مانند سیستان‌ و بلوچستان میانگین بسیار کمتری نسبت به متوسط کشوری دارند، در حالی که اعداد و ارقام در شهر تهران به ۳۲ تا ۳۳ سال می‌رسد. /ایسنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/657455" target="_blank">📅 21:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657454">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc5bb308b.mp4?token=tqQCMXKRQVbeiwSjbsciwBUrqngQu1haQAyaDhGkols8G09BhKnQks4FzISO_mdApe7WhCjnuuP6LqUmVb2pSHYu3ypyww5jL4yaLe8Zk1JQpKe9ioMVJCeVzs-C8RQwA0KK4rT8cK9y5QFr3x7P4Fj1LmPUe9R9rykfzVmb08jKlYPGeuYscwyqueXGEzvc-TxjTT7QL_xezsHkr5fztOARJq_sFJtBdmVBtJDsNkBGCkGL9aA0YcKYTbu0D2siQIOb1p2BiUSr05V6zT0eUjK-cXrVk1SW3_U1ycT39y8tCvhbDKnVzmYYxnX97jVcEEtdNOK3g7H7h9dokpUarw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc5bb308b.mp4?token=tqQCMXKRQVbeiwSjbsciwBUrqngQu1haQAyaDhGkols8G09BhKnQks4FzISO_mdApe7WhCjnuuP6LqUmVb2pSHYu3ypyww5jL4yaLe8Zk1JQpKe9ioMVJCeVzs-C8RQwA0KK4rT8cK9y5QFr3x7P4Fj1LmPUe9R9rykfzVmb08jKlYPGeuYscwyqueXGEzvc-TxjTT7QL_xezsHkr5fztOARJq_sFJtBdmVBtJDsNkBGCkGL9aA0YcKYTbu0D2siQIOb1p2BiUSr05V6zT0eUjK-cXrVk1SW3_U1ycT39y8tCvhbDKnVzmYYxnX97jVcEEtdNOK3g7H7h9dokpUarw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژنرال چهار ستاره بازنشسته ارتش آمریکا: خود ترامپ یکی از بزرگترین مشکلات امنیت ملی آمریکاست
🔹
مجری: ژنرال، آیا در یک جنگ مشترک، این طبیعی است که رهبران متحد تا این حد علناً نشان دهند که با هم هم‌نظر نیستند، آن‌طور که ترامپ و نتانیاهو در هفته‌های اخیر بوده‌اند؟
🔹
ژنرال مک‌کافری: نه ... واقعاً نمی‌توانم تصور کنم وزارت خارجه و رهبری ارشد نیروهای مسلح ایالات متحده با توجه به حملات علنی آقای ترامپ علیه اسرائیل یعنی تحقیر نتانیاهو چه فکری می‌کنند.
🔹
او از شعار «تسلیم بی‌قید و شرط» و اینکه «من به انتخاب رهبر بعدی ایران کمک خواهم کرد» خیلی فاصله گرفته، اما همچنان به‌طور علنی در حال زیر سؤال بردن و تضعیف مذاکره‌کنندگان خودش است. بنابراین، به‌نظر من یکی از بزرگ‌ترین مشکلات امنیت ملی در حال حاضر، خود رئیس‌جمهور ایالات متحده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/657454" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657453">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6e58ae01.mp4?token=f1kwU9r4KEXgHeVCLBmdKUBbkd_r_0QyUNwQlNGLCZVutGofW-2i1fXMwvd30umuzJCVAHYkBF687hy8_9wrEPezYKoTfb3PT4KFTFrS2XdW2_FzFvw8eoZhw7IWWWrekJwq0881TA9SsotMQQ11I6DUQmtC2A7sFPAD-oLX5fFBns4gRESVhj7eO6x6DMye_H_vKplkW4heC7ulewSF1QtrH_SWLnmJuv_E-pbXxMwMUSPCkFAYrpLhsIwKT6hvZw7wAK1SPwTn1AhhNinNGg1e4QgZJQAr7lSzcojs3BLre9uJXZCsykwDTD5iqUf-v-kyHqebIuIHs1Rqwf9-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6e58ae01.mp4?token=f1kwU9r4KEXgHeVCLBmdKUBbkd_r_0QyUNwQlNGLCZVutGofW-2i1fXMwvd30umuzJCVAHYkBF687hy8_9wrEPezYKoTfb3PT4KFTFrS2XdW2_FzFvw8eoZhw7IWWWrekJwq0881TA9SsotMQQ11I6DUQmtC2A7sFPAD-oLX5fFBns4gRESVhj7eO6x6DMye_H_vKplkW4heC7ulewSF1QtrH_SWLnmJuv_E-pbXxMwMUSPCkFAYrpLhsIwKT6hvZw7wAK1SPwTn1AhhNinNGg1e4QgZJQAr7lSzcojs3BLre9uJXZCsykwDTD5iqUf-v-kyHqebIuIHs1Rqwf9-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: هر کسی که در کشور بین آمریکا و اسرائیل تفکیک ایجاد کند، یا ساده‌لوح است یا خیانتکار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/657453" target="_blank">📅 21:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657452">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
قالیباف: ما در مقابل دشمنان ایران، ۴ میدان مبارزه داریم
🔹
۱. میدان مبارزه نظامی
🔹
۲. میدان مبارزه دیپلماسی
🔹
۳. میدان حضور مقاومت مردم
🔹
۴. میدان خدمت
🔹
سه میدان اولی، پشتیبانی می‌کند چهارمین میدان را.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/657452" target="_blank">📅 21:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657451">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
قالیباف: به فرموده رهبر انقلاب، راه مقابله با نقشه دشمن، ایستادگی، روشن بینی، انسجام، اعتماد متقابل و هم صدایی نکردن با دشمن است/ برخی به اسم تبعیت از رهبری در حال عمل کردن خلاف خط مشی ایشان هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/657451" target="_blank">📅 21:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657450">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
تداوم حملات هوایی رژیم صهیونیستی به جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی در جدیدترین تجاوز خود، مناطقی از جنوب لبنان را هدف قرار دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/657450" target="_blank">📅 21:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657449">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFXWj1whcovCwKOw_XvVWNSnQ6CiJ80pvBwLAwkSR7TsEAwhojcycfqezmervgtr3cHZPr6Hj6-27IOdIBiSavpbC9XZ4igL0t9CwMfj6RLAiByiOxxXVu2ubHh2iaJ9wHO1HAUyxsDtpDieiWUibly0Yay7qvf9ZmixHriSAes3dDlV4HOLjElLtSHhfna1BL08AhuwarCnafw__bMY4EhgWcB4tDgn1tnEcO-zx5EwFLB1buXMUWvGXMievt7uN1tieOnQ_F9wDWFEREumk7T8bXZm3Hu4Evwlxbm6m3p8UKLqh4guvR02K1yXX6szeMR9jPzSKBluJ3ZkVGWBkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
جام جهانی ۲۰۲۶ از همین حالا در «همراه من» شروع شده!
برو توی اپلیکیشن
«همراه من»
، بازی‌ها رو پیش‌بینی کن و جوایز هیجان انگیز ببر
🤩
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک  PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
3 کمک هزینه سفر به عتبات عالیات در هر بازی تیم ملی
پیش‌بینی از تو، جوایز میلیاردی از همراه اول!
🔗
https://www.mci.ir/-9VEQ3HH</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/657449" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657448">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تهدید شبکه‌ای، پاسخ شبکه‌ای می‌خواهد
تحلیلی کوتاه بر اقدام نظامی ایران در ۲۴ ساعت گذشته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/657448" target="_blank">📅 21:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657447">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
لغو پروازهای «ایر فرانس» به اسرائیل
🔹
در پی تداوم تنش‌ها، شرکت هواپیمایی «ایر فرانس» نیز به جمع شرکت‌هایی پیوست که پروازهای خود به مقصد سرزمین‌های اشغالی را به حالت تعلیق درآورده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/657447" target="_blank">📅 21:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657446">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WzDP2IH1-Vkbd23Al153-qlKqt9qUZ7DwLy_5PT8xxZEGJBKPcb-3Wb7BynpGMs5qlP57NNgrin-J1EJLShr9aUJ3rlDOXj8x3bBJoVdGeLU_Jy20IKo4jwrEW7XuFJrOOrQr7JfycI5uPDGaVi2igsPwKOd-6asf0KB4NFUa6BKnAfnKgSt0kWiRe79G5Fi0JEIC4JQtlJm6hV2mRnnaZbvsEj-RVHkcYKkK4SsNXK5kF_NWJIotSKgKLYK3aBXkpvVstGZJg4xKGVqdpZqRqF6uKsKFcegYXsXeUuepJpttk9rhwE-u1Kw8itZe5T-AiuoEmnzJO5TseV3zXmy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
المانیتور: آمریکا شب گذشته در رهگیری موشک‌های ایران به اسرائیل کمک کرد
المانیتور:
🔹
یک مقام آمریکایی تأیید کرد که واحدهای نظامی ایالات متحده در منطقه، برای مقابله با رگبار موشک‌های بالستیک ایران که به سمت اسرائیل شلیک شده بود، موشک‌های رهگیر پرتاب کرده‌اند.
🔹
این اقدام در چارچوب «دفاع از خود» صورت گرفته و ارتش آمریکا در حال ارزیابی میزان موفقیت این عملیات در سرنگونی موشک‌های ورودی است. هم‌اکنون صدها نیروی نظامی آمریکایی در اسرائیل مستقر هستند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/657446" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657445">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قالیباف: صحبت‌های رئیس‌جمهور آمریکا دربارهٔ یادداشت تفاهم، مخالف بخش‌های توافق شده بود که نشان داد آن‌ها نه دنبال آتش‌بس هستند و نه دنبال گفت‌وگو
🔹
باید برای دفاع از حقوق ملت ایران پاسخ قاطع می‌دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/657445" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657444">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌
♦️
قالیباف: هدف مذاکرات پایان جنگ و ایجاد امنیت پایدار است، نه عادی‌سازی با آمریکا
🔹
به مردم عزیز اطمینان می دهم که با قدرت از حقوق مردم ایران دفاع می کنیم.
🔹
‌ما نه می‌خواهیم با وادادگی پیش برویم و نه با شعارزدگی بلکه باید با اقتدار و عقلانیت ایرانی به‌دنبال…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/657444" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657443">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود
🔹
نه دیپلماسی مانع عملیات نظامی است، نه عملیات مانع دیپلماسی
🔹
میدان نظامی، میدان دیپلماسی، میدان حضور مردم و میدان خدمت به مردم تار و پود یک پیکره واحد هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657443" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657442">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
قالیباف: نقض آتش‌بس و محاصرهٔ دریایی، علت تنش‌های اخیر بود
🔹
نه دیپلماسی مانع عملیات نظامی است، نه عملیات مانع دیپلماسی
🔹
میدان نظامی، میدان دیپلماسی، میدان حضور مردم و میدان خدمت به مردم تار و پود یک پیکره واحد هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/657442" target="_blank">📅 20:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657441">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
بحرین عزاداری برای آیت‌الله خامنه‌ای را ممنوع کرد
ادعای المانیتور:
🔹
بحرین اعلام کرد که عزاداری برای آیت‌الله علی خامنه‌ای، رهبر فقید ایران، در مراسم عاشورای این ماه ممنوع است./خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/657441" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657440">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
ادعای ترامپ: به نتانیاهو گفتم برابر ایران تنها هستی  سگ زرد:
🔹
به نتانیاهو گفتم بسیار مراقب رفتارهایت باش، چرا که ممکن است خیلی زود خودت را برابر ایران تنها ببینی. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/657440" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657439">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
خضریان، عضو کمیسیون امنیت ملی مجلس: جمهوری اسلامی دیگر نقض آتش‌بس در لبنان و جنوب ایران را تحمل نخواهد کرد/ موشک‌های ایرانی به اهدافی اصابت کردند که بتوانند به حزب‌الله در جنگ کمک کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/657439" target="_blank">📅 20:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657438">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ادعای ترامپ: به نتانیاهو گفتم برابر ایران تنها هستی
سگ زرد:
🔹
به نتانیاهو گفتم بسیار مراقب رفتارهایت باش، چرا که ممکن است خیلی زود خودت را برابر ایران تنها ببینی.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/657438" target="_blank">📅 20:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657437">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
قاضی‌زاده هاشمی: اگر لبنان سقوط کند، ایران در امان نخواهد ماند
سید امیرحسین قاضی‌زاده هاشمی، در
#گفتگو
با خبرفوری:
🔹
باید دید چرا آمریکا برای اسرائیل می‌جنگد، به همان دلیل ایران برای لبنان می‌جنگد چرا که اگر لبنان سقوط کند، ایرانی هم باقی نخواهد ماند. لبنان باید بداند حرف‌های مزخرفی که رئیس‌جمهور و دولتمردانش می‌زنند، اشتباه است و متاسفانه این خود فروخته‌‌ها در همه کشورها هستند.
🔹
لبنانی‌ها هم باید بدانند که اگر ایرانی نباشد، لبنانی قبل از او نخواهد بود. تا زمانی که یک سرباز اسرائیلی در جنوب لبنان مستقر است، این نبرد نباید پایان یابد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/657437" target="_blank">📅 20:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657436">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ec30c567.mp4?token=rR7e5Hx6RbQhijo8gqnntmeXoOgU3jdsyAlQ12JOihj-Tq2yzd2bjsJiWi5-ZL9GFF1PYtGNpmobt5QH2wCR66mORjCp4pdLE8AKa6kTtfvejnn0s9dtDrJxQt179d9tYLISfpv5C-ix4uZO7fCGr1jDriP8sZVocvxQb0QW4xLE-ScFgzKJmFEynsJZToKyhUjcv8u3Cbr2fX3qjMlg-6ODMcZy4Idf4cpiFt907dkQD1ksQz4biBZzir-EBi9orMxnilpUEDdySZf6knnQsJu2bcdzxK3TUHHTBHe-At0TX9aQ2QmAirXpYwMFgDJHC3g59P1fPLrSisRnbl0SEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ec30c567.mp4?token=rR7e5Hx6RbQhijo8gqnntmeXoOgU3jdsyAlQ12JOihj-Tq2yzd2bjsJiWi5-ZL9GFF1PYtGNpmobt5QH2wCR66mORjCp4pdLE8AKa6kTtfvejnn0s9dtDrJxQt179d9tYLISfpv5C-ix4uZO7fCGr1jDriP8sZVocvxQb0QW4xLE-ScFgzKJmFEynsJZToKyhUjcv8u3Cbr2fX3qjMlg-6ODMcZy4Idf4cpiFt907dkQD1ksQz4biBZzir-EBi9orMxnilpUEDdySZf6knnQsJu2bcdzxK3TUHHTBHe-At0TX9aQ2QmAirXpYwMFgDJHC3g59P1fPLrSisRnbl0SEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحنه‌های آخر الزمانی از زلزله‌های فیلیپین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/657436" target="_blank">📅 20:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657435">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
برخی کاربران مدعی شده‌اند که دارایی‌شان در چند صرافی رمزارز خارجی، به بهانه تحریم و بدون هشدار قبلی مسدود شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/657435" target="_blank">📅 20:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657434">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cd07775b9.mp4?token=U81fcqM4EaKTsshJievKknUC9W2bqeyCDs2obl0BRgyp6htYn-PCXGbLTl2VOWtNKUQXAthNhrHOfSkwEgCF8umHXanAPkR5_L1f0hSv8BGENnzvT5Rk-FEQY9oQXotwCFCATCkhuwpBNyUGcV8wezIDy1hh9gk0_xn03Cu02ID6aOn0vBoyQa72PCvCvttrUoGLO2nbdmRm2mMp0DU1w98tFqUbHIOWScvxwFG-DgjCPb7W4GVFd2OT-7SBnyJwcyFVVPJH7VwgmmHDbYnw5qdEPu4avqRi53-TDK422NYU2Pch18jBhLpByrufqwb1J6mXOAL9C-GxjIY72JC4dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cd07775b9.mp4?token=U81fcqM4EaKTsshJievKknUC9W2bqeyCDs2obl0BRgyp6htYn-PCXGbLTl2VOWtNKUQXAthNhrHOfSkwEgCF8umHXanAPkR5_L1f0hSv8BGENnzvT5Rk-FEQY9oQXotwCFCATCkhuwpBNyUGcV8wezIDy1hh9gk0_xn03Cu02ID6aOn0vBoyQa72PCvCvttrUoGLO2nbdmRm2mMp0DU1w98tFqUbHIOWScvxwFG-DgjCPb7W4GVFd2OT-7SBnyJwcyFVVPJH7VwgmmHDbYnw5qdEPu4avqRi53-TDK422NYU2Pch18jBhLpByrufqwb1J6mXOAL9C-GxjIY72JC4dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار تحقیرآمیز آمریکایی‌ها با اعضای تیم ملی فوتبال سنگال
🔹
انتشار تصاویر و گزارش‌ها از لحظه ورود اعضای تیم ملی فوتبال سنگال به خاک آمریکا و برخورد نامناسب و تحقیرآمیز مقامات آمریکایی با آنان، موجی از واکنش‌ها و انتقادات را به همراه داشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/657434" target="_blank">📅 20:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657433">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a531b5b25.mp4?token=EVGbUTYAiaxrCkjRADVWaZqbUlcftrJRVeFoB0zKGWBu7SyjXaq7SxRmDIuQUDBkrYCjaO_kEq6WWXkSDdiocAjQ6jeIyyq8Jg4gad_3vQ3yY4z7p61SBmyBtJZ4aLiCDJabTitF8LSvqIKKlB5CPfSluVAKBj9uVZoCF5imQ4I7fNXgLQhm2eGcyhSWaUbui0n_obxrGE10NikW9FxsLH-1JcLU0hHKLo4jWxHKVOEw3iyEvg7RMwN0jIJK8pb3e3qZmNSIDSLvZxA1WDrPMeBQGAhkrY8cVe9sW68JsK9H_qkflG1xGBdGcbSiwR1qy75cYaKDAa8RisTeJ64jzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a531b5b25.mp4?token=EVGbUTYAiaxrCkjRADVWaZqbUlcftrJRVeFoB0zKGWBu7SyjXaq7SxRmDIuQUDBkrYCjaO_kEq6WWXkSDdiocAjQ6jeIyyq8Jg4gad_3vQ3yY4z7p61SBmyBtJZ4aLiCDJabTitF8LSvqIKKlB5CPfSluVAKBj9uVZoCF5imQ4I7fNXgLQhm2eGcyhSWaUbui0n_obxrGE10NikW9FxsLH-1JcLU0hHKLo4jWxHKVOEw3iyEvg7RMwN0jIJK8pb3e3qZmNSIDSLvZxA1WDrPMeBQGAhkrY8cVe9sW68JsK9H_qkflG1xGBdGcbSiwR1qy75cYaKDAa8RisTeJ64jzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتقاد ممدانی از نحوه میزبانی دولت تروریستی آمریکا  در جام جهانی
🔹
زهران ممدانی، شهردار نیویورک را به دلیل نحوه مدیریت جام جهانی، محدودیت‌های سفر و رد درخواست‌های ویزا برای تیم‌ها و دیگران مورد انتقاد قرار داد.
🔹
جام جهانی قرار است جشنی برای کل جهان باشد، در حالی که خلاف این را در این رویداد ورزشی شاهد هستیم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/657433" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657431">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29a218a22.mp4?token=DGcM24EYPcf6cMLkGAWyZoLFBdxNyH6GKQYZcFl7hitEZg7pBIX4FV5IT3iVAB-_N5UgGsmwUQlrrXs2B9pj_ILByycps0T61T0Vt9SAZnrcGKKDYlxUxkOWwkBpQ0bBqHO-oSpy3wMD7SspDvXTVr4ry3NKWJUZ4ob6QNRALVBEp2_X-HlVs70rC2ZRzYyg25FeCRXflYYOf2sHMrrR0ce8duwTKio5JHw-WpBGGinPLCERpOYzjktD__YUowqpwWuWwl4JsFa8hoiWnchR2L4wCK7FerP4qfuW_0ESbekZ0Nrmsc_HgVfWj5NiIc36OEueWiTIej1FC38UcqTANLyed1nwxt0b_1dPdsFS8WeS7CsNr1bVY9pz6X1vslFcMoyJQIVUb2Q5MeG5Qy9lVBh7foCaicEU1vdvZFBB5Pr2TI1ebraTP6iTvRdaaIqOEkSgFk1W8wYXaMWE8SYDSFPdDIQCmvWtkBKSbpoU8DG7FduGx3OSPl6-OGZdcw0zTkFeMIeyyNe9g5MFgOdQCuEabNEVJK7WTyNkvcsyLrIHjU384Y1J8-e7B8_4jw-62kacWxSWyYDJRagrQuZynfIJWgLRV7sjKk1VKNMaiE_lrtXDY97mllaJtuSDhNlKpI4Xl8dkQIlt6LF2s8nh7jrUEuzgic3x_IXXHECNyCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29a218a22.mp4?token=DGcM24EYPcf6cMLkGAWyZoLFBdxNyH6GKQYZcFl7hitEZg7pBIX4FV5IT3iVAB-_N5UgGsmwUQlrrXs2B9pj_ILByycps0T61T0Vt9SAZnrcGKKDYlxUxkOWwkBpQ0bBqHO-oSpy3wMD7SspDvXTVr4ry3NKWJUZ4ob6QNRALVBEp2_X-HlVs70rC2ZRzYyg25FeCRXflYYOf2sHMrrR0ce8duwTKio5JHw-WpBGGinPLCERpOYzjktD__YUowqpwWuWwl4JsFa8hoiWnchR2L4wCK7FerP4qfuW_0ESbekZ0Nrmsc_HgVfWj5NiIc36OEueWiTIej1FC38UcqTANLyed1nwxt0b_1dPdsFS8WeS7CsNr1bVY9pz6X1vslFcMoyJQIVUb2Q5MeG5Qy9lVBh7foCaicEU1vdvZFBB5Pr2TI1ebraTP6iTvRdaaIqOEkSgFk1W8wYXaMWE8SYDSFPdDIQCmvWtkBKSbpoU8DG7FduGx3OSPl6-OGZdcw0zTkFeMIeyyNe9g5MFgOdQCuEabNEVJK7WTyNkvcsyLrIHjU384Y1J8-e7B8_4jw-62kacWxSWyYDJRagrQuZynfIJWgLRV7sjKk1VKNMaiE_lrtXDY97mllaJtuSDhNlKpI4Xl8dkQIlt6LF2s8nh7jrUEuzgic3x_IXXHECNyCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحلیل‌گر اسرائیلی در واکنش به ادعای دروغ ترامپ: هیچ عملیات نظامی توسط اسرائیل بدون کسب تاییدیه رسمی از آمریکا انجام نمی‌شود. ایران آمریکایی‌ها و اسرائیلی‌ها را جبهه‌ای واحد می‌بیند و اهداف آمریکایی را نیز هدف قرار می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/657431" target="_blank">📅 20:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657430">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعای عجیب سرافراز: یک سال است که جلسات شورای فضای مجازی برگزار نشده!
محمد سرافراز، عضو شورای فضای مجازی در
#گفتگو
با خبرفوری:
🔹
شورای عالی فضای مجازی هیچ‌گاه در مورد قطع کردن اینترنت مصوبه‌ای نداشته و در ضمن حدود یکسال هم هست که جلسه این شورا تشکیل نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/657430" target="_blank">📅 20:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657429">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
سنتکام: یک نفتکش مرتبط با ایران را متوقف کردیم
اطلاعیه فرماندهی مرکزی ایالات متحده:
🔹
نیروهای آمریکایی در ۸ ژوئن یک نفتکش خالی را در خلیج عمان، پس از آنکه این کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، محاصره مداوم علیه ایران را نقض کرد، از کار انداختند.
🔹
جنگنده اف-۱۸ پس از آنکه خدمه یک نفتکش از دستورالعمل‌ها پیروی نکردند، مهماتی را شلیک کرد که به موتورهای آن آسیب رساند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/657429" target="_blank">📅 20:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657428">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/52f18c222e.mp4?token=owb61rxqLZRDuK76kE1DV9js7mqGslj-GElu69xerMVFa46yGIoU9luu3KiQoHNps7wkLufwcG37rFwxI7-J4LCNF3H61iAW0oCqhf8Ys7Cc17ihy5jAXsh_YyOnQxJ0Pugon8uj7YSgrVhEKsOPpGCevKJQ4-DvlwudNc_BeaZ4QgpNUqqzXFGa-oObvHVHTcAhl7mAPAoDmKOosRNctDOr_vMCJF4K_AOuRQlKv6L8j-juETtkolNAiAwQYcBkOaLmuyBVfWcyf51Y0cYZQeRjbXg83Qwh-VY507AJrMnOl-Jd9JBQEMzoYVqLxMU_x6kpt6mCu9BJOGpae7E4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/52f18c222e.mp4?token=owb61rxqLZRDuK76kE1DV9js7mqGslj-GElu69xerMVFa46yGIoU9luu3KiQoHNps7wkLufwcG37rFwxI7-J4LCNF3H61iAW0oCqhf8Ys7Cc17ihy5jAXsh_YyOnQxJ0Pugon8uj7YSgrVhEKsOPpGCevKJQ4-DvlwudNc_BeaZ4QgpNUqqzXFGa-oObvHVHTcAhl7mAPAoDmKOosRNctDOr_vMCJF4K_AOuRQlKv6L8j-juETtkolNAiAwQYcBkOaLmuyBVfWcyf51Y0cYZQeRjbXg83Qwh-VY507AJrMnOl-Jd9JBQEMzoYVqLxMU_x6kpt6mCu9BJOGpae7E4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروسی در پاسخ به سوالی درباره ۱۷ حمله به تاسیسات ایران: من در این باره چیزی برای گفتن ندارم/ نماینده ایران حق دارد اعتراض کند اما من با آن‌ها موافق نیستم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657428" target="_blank">📅 19:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657427">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بازگشت فضای هوایی کشور به شرایط عادی
«شیرودی» رییس سازمان هواپیمایی:
🔹
پیرو اعلام مراجع ذی‌ربط مبنی بر پایان عملیات نظامی و با عنایت به هماهنگی‌های انجام‌شده، فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام) صادره، از سر گرفته خواهد شد.
🔹
با فراهم شدن شرایط ایمن و انجام هماهنگی‌های لازم با نهادهای ذی‌ربط، محدودیت‌های پروازی رفع شده و فعالیت‌های هوانوردی کشور طبق برنامه در حال بازگشت به روال عادی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/657427" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657426">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/859333bc25.mp4?token=SdMvGwU9D5WUE0fySOZmXtDnnNSnu1orZ-Myw8fLvxupx-sDGZzebS_D-HppIenP1oHAa5RxpDXf1vK_I0Aco1aHqMEOp6lgVDHgLTLtckd3Wfi8QmFhGCK8je7yuEbSYJl0e-jJraYTqmWqM5pZ5XhHFl-ZJN2fqg_bJ0DvjCrZi5aBix68yddxBhAhm9ClEOTIOZmGZHKatrEwcZqMwIKB3RokWWGGFFB8XIEVsGr1IglrTRAJZaXAdrm2nMKo_FRFmotplTTL_mXB5SARj5Ak7qoTi62ywVhmzR7F6FKDlR1vIrd0P25TSihkcv2n707fbXm0-MnWAn6f88QFFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/859333bc25.mp4?token=SdMvGwU9D5WUE0fySOZmXtDnnNSnu1orZ-Myw8fLvxupx-sDGZzebS_D-HppIenP1oHAa5RxpDXf1vK_I0Aco1aHqMEOp6lgVDHgLTLtckd3Wfi8QmFhGCK8je7yuEbSYJl0e-jJraYTqmWqM5pZ5XhHFl-ZJN2fqg_bJ0DvjCrZi5aBix68yddxBhAhm9ClEOTIOZmGZHKatrEwcZqMwIKB3RokWWGGFFB8XIEVsGr1IglrTRAJZaXAdrm2nMKo_FRFmotplTTL_mXB5SARj5Ak7qoTi62ywVhmzR7F6FKDlR1vIrd0P25TSihkcv2n707fbXm0-MnWAn6f88QFFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوانین جدید فیفا در جام‌جهانی ۲۰۲۶
🔹
فیفا به جهت افزایش سرعت و جذابیت بازی برای تماشاگران تغییرات جدیدی را برای مسابقات جام جهانی ۲۰۲۶ اعمال خواهد کرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/657426" target="_blank">📅 19:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBAQcCen9-kd7hqcIbpvF0JMtjxjBkStlqGdcyLM09X8L7DN3xmrq4NkCWDw7CYvrBS8uTJwGFMb5nDbL8ufD-F6m32EddRvCpLR7Hnmi9aAUcdWGCfyZw6AbiYX6rMYXm-3CnQsBKQ7Gp0TGmS1h6qSGlWZmNjUO-QHWm5AW0wuzqGelPyvVEpqTJWqNjpAdxd8YPYzQ11u62HgOph6WqKoMwbQS_TK7hlCvxd17cjG6Xwv3rs_muIiXjUTUs2XhqlyRJyemsEOxA80yt3K1JfcX9vBcXtGJSxd73LI1Ja6MYj0PTImHo9ZMeS9mKnAqTM0mVxSTTq4MRYf-f2y_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روسیه برای شهروندان خود در اسرائیل هشدار صادر کرد
🔹
سفارت در اطلاعیه‌ای که روز دوشنبه منتشر شد، اعلام کرد که روس‌هایی که در حال حاضر در اسرائیل هستند باید احتیاط کنند و از دستورالعمل‌های مقامات محلی پیروی کنند.
🔹
این سفارتخانه اعلام کرد که هیچ گزارشی مبنی بر زخمی شدن روس‌ها در نتیجه حملات موشکی ایران دریافت نکرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/657422" target="_blank">📅 19:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9efaf273c.mp4?token=pNaBiSDdISm95jEndk2pFKYDjraN76BWBD49P3QFgytVyWijlQq8QtysjbDuWtOKVMBLxJMgOwET28v4j7Oecwp4sJoapZ7ydh4Kby2JMHrLfDyU7BztIBJkWBup0Zo7mzKFQhs-_3RoFW0WFnfABjc3P4UulaGogizh_AR07QgqEKVl1FBdgRaSsqplbog01ig4ytkXpTTezCfxecmNgbYNFw6on2-2MZA-1-GGo-ZPyTVY9K5Oiw1EK2PAOdzHpmZrfr7VFOrP7WKUibep3ffPNZdjE-ocDw6yGgKAsv9BsxC0zCAdUa_75afmupVnS31sXSJ7l9n-KojrqxwdUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9efaf273c.mp4?token=pNaBiSDdISm95jEndk2pFKYDjraN76BWBD49P3QFgytVyWijlQq8QtysjbDuWtOKVMBLxJMgOwET28v4j7Oecwp4sJoapZ7ydh4Kby2JMHrLfDyU7BztIBJkWBup0Zo7mzKFQhs-_3RoFW0WFnfABjc3P4UulaGogizh_AR07QgqEKVl1FBdgRaSsqplbog01ig4ytkXpTTezCfxecmNgbYNFw6on2-2MZA-1-GGo-ZPyTVY9K5Oiw1EK2PAOdzHpmZrfr7VFOrP7WKUibep3ffPNZdjE-ocDw6yGgKAsv9BsxC0zCAdUa_75afmupVnS31sXSJ7l9n-KojrqxwdUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوم‌کشی؛ نخستین مستند جنایت آمریکا و اسرائیل علیه محیط زیست ایران
اولین مستند تصویری ایران درباره «بوم‌کشی» (Ecocide) ساخته شد. این فیلم به سفارش اداره کل محیط زیست شهرداری تهران، آثار مخرب حملات آمریکا و رژیم صهیونیستی بر منابع آب، خاک، تنوع زیستی و سلامت مردم را بررسی می‌کند.
از آلودگی تأسیسات انرژی تا تخریب جزیره شیدور، این مستند جنایت جنگ علیه محیط زیست را روایت می‌کند.  «بوم‌کشی» از شبکه‌های صداوسیما پخش می‌شود.
https://www.aparat.com/v/vheh27v</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657420" target="_blank">📅 19:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای نتانیاهو: اسرائیل فعلاً از حمله به ایران خودداری می‌کند #Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657419" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntntr-K_fZ4LvrLyKmPCfFwnRSn4iqNXxbbbzAjgyHHruqpflcGZbi34HVolqSiCiTYI_e8rNgZ06gX2GMn3Rh9plpg1bzQ7P-tF4-QUe2TSxlMeghU8K8V1DEYchrX1veMT-z7m3xqwzXMatksOqEja31wQ3HDCzpUWItrkC4nAXgp5sg-uXPC-CcFVKoUK--hCtCbXE6kRxINuYArjvQn4TB1R4NcbRVK9uKsf6Zwb3n1pLUHTWhqrbVugNc4aXw76l6crv5yLVUxTyt7xxFu7q92M8R_dc4zcUhnkxQJqQrsBRqN2wFp8jjgjBlmbTfEo-HTLCs3gxo9D1HszSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب‌آبادی: ایران عضو کنوانسیون حقوق دریاها نیست
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/657418" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
نتانیاهو: ماموریت ما با حزب‌الله هنوز تمام نشده است  ادعای نخست وزیر رژیم صهیونیستی:
🔹
یک سال پیش ما یک حمله تاریخی علیه اراده ایران برای نابودی ما با بمب هسته‌ای آغاز کردیم.
🔹
ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند و ما آن را نخواهیم…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/657417" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7918af41cc.mp4?token=Ann4wINXlZIvXz5OaVvSUXSt_u1IiF8Zz2d2JDM5ZWhXZiS2unn4l7RNesQe-HNCZnGRKV7sg0wVBIiBZyA4UFHhL6LUNH4ng4NYY5rDxWk27YtT-IsJK8oeBHUchcGJ_RH3uD54PGe_Crb_JI3SZN4w9VE09DrBImWw_N_U4vCjPr1bH-DCzNaUHm6nWvS5B-LAo28XmQM60WoxF0OYdXiW1Vi0qJGwvnNXwXYPahgTnRo1JR7nMbebloeKqumycHsXinJIHy_M8xSu0OW5goGO_ILbS555ZdERwmXnce1Yh78ibQFz8EYtH55X-YLs1WYJjzJqau7Sc-kOBmOE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7918af41cc.mp4?token=Ann4wINXlZIvXz5OaVvSUXSt_u1IiF8Zz2d2JDM5ZWhXZiS2unn4l7RNesQe-HNCZnGRKV7sg0wVBIiBZyA4UFHhL6LUNH4ng4NYY5rDxWk27YtT-IsJK8oeBHUchcGJ_RH3uD54PGe_Crb_JI3SZN4w9VE09DrBImWw_N_U4vCjPr1bH-DCzNaUHm6nWvS5B-LAo28XmQM60WoxF0OYdXiW1Vi0qJGwvnNXwXYPahgTnRo1JR7nMbebloeKqumycHsXinJIHy_M8xSu0OW5goGO_ILbS555ZdERwmXnce1Yh78ibQFz8EYtH55X-YLs1WYJjzJqau7Sc-kOBmOE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: ماموریت ما با حزب‌الله هنوز تمام نشده است
ادعای نخست وزیر رژیم صهیونیستی:
🔹
یک سال پیش ما یک حمله تاریخی علیه اراده ایران برای نابودی ما با بمب هسته‌ای آغاز کردیم.
🔹
ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند و ما آن را نخواهیم پذیرفت. من متعهد می‌شوم که ایران سلاح هسته‌ای نخواهد داشت.
🔹
رژیم ایران پس از پاسخ ما، از حمله به ما منصرف شد. اگر رژیم ایران همان اشتباه را تکرار کند، ما با قدرت پاسخ خواهیم داد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657416" target="_blank">📅 18:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657413">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVv622Jp5dWmnTEX1q7nH39-EMsPVbemNyvtgNVhch71RfVcLzrsCZWOCdfoToXWxQlnJNqES7sScQvxWWTUmZ9uVnxXJ37mfN8Q2Do_oesw3_FMZir3AsDG5XFP1T3MiR9RqmV2RlA9FR0G3d76HoPfqFz9IMZ8gw9hllZjdYVkRBpIJS67SgyyI2cng7qMz5fGJC-Tkw8UDHvkYNFD688P-AlNnCX_FXtJa1WUz01XvEHriXTlFLA1D36TxJ3NOmKJXzynk5aVe39BpqIChuD_dCyfnI6yfy8XRfF2X47YLZsPwDcDNChhl4r3Lw0suoXrP74D8o4YPeR45tWIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/657413" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657411">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تداوم تجاوزات رژیم صهیونیستی به جنوب لبنان
🔹
جنگنده‌های رژیم صهیونیستی دقایقی پیش شهرک «دیر قانون رأس‌العین» در منطقه صور واقع در جنوب لبنان را هدف حمله هوایی قرار دادند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/657411" target="_blank">📅 18:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657410">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
نتانیاهو تا دقایقی دیگر بیانیه مهمی صادر می‌کند
🔹
دفتر نخست‌وزیر اسرائیل اعلام کرد بنیامین نتانیاهو ساعت ۱۸:۱۵ به وقت محلی برای مردم و رسانه‌ها سخنرانی خواهد کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/657410" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp2fAkFb6YcrvKV3wwSAbknpdJ1oyLl6ppzg8hd8pnH5Jwx-5Pep9Pv11T7O9X2KVfZab7Uj49njxacjFNTbRuGZKRyyMyFZOKSYvkXo4pOJMrL2tISpVgKLMrWpB5kf7nfiro7GDhf7D_u71hNmixBfv582PAwDJGXWO5iH5q4sREJGtKBZYFZXXXfGjWp5hFeTxyh2h809pWAzjUw7oXkDdpL7LE-FCjAbVj5RzQLY1ttgHg29umaMQenf8QTzr-3nPtDTdIBt_RFjrfrfncbHBDNM-M9w2aloZUqNBzqgej8X0HyDJiQqGC-gXF1wu-tw_3D4hdtzJe2bEK-3tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف، رئیس مجلس:‏ معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم
🔹
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657407" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
گزارش‌ها از وقوع حادثه در سواحل عمان
🔹
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از بروز یک حادثه امنیتی جدید در آب‌های نزدیک به عمان خبر داد.
🔹
این نهاد دریایی اعلام کرد حادثه‌ای در فاصله ۲۸ کیلومتری شمال‌شرقی «جزیره مصیره» در کشور عمان رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657406" target="_blank">📅 18:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
تصاویری از حملات موشکی یمن به اهداف مهم در «یافا» اشغالی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/657405" target="_blank">📅 18:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hh2SRunJLjcdHP1g9Fe72glomLkqjxwDFl_KjicHuz1m3DbtMbEEWCw_nY0J3g-rMn-2MXWKaQPi80jis50W7dTjcJAWw59jCC3B3FaydUC2rcWspRHG_mTPIqUvMpIdCMTfgOBaSXIEc11I96-2MoZ9wkAQ6gAjJjeVWduS4ih54WdAy5CM_TJ13UzLIKJ-GcF-45uJdfBbm6ltQi97hTbhnfFdA4Q0Rn2p8lfHJEKpjC4rp9ZwaFV5XrWSTgqmBrhQLJr_OgBROIydqxLzeXRbVN2bjH9tsgtA_Gub6QWwcPhhu2Q-V4k1GvPRhn_0Cuagpe1JYLo11KQ2xN587Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیر شورای عالی امنیت ملی: اگر ائتلاف شیطانی صهیونی آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657404" target="_blank">📅 17:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
الجزیره: هم‌اکنون باز هم نقض آتش بس و حمله هوایی اسرائیل به شهر صور در جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/657401" target="_blank">📅 17:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOLwGEjRqftAJm1gRmij11twsOzpZ9cgFaw6w7taGFSvB5A48zD-2UeNYGEKYDb2daxxDTTgt_HpFQohv0aWbkjoFiPDvbgq4HR7SQMnUbCQMdS44UzsmuyMXsP2_vc8oFZlR2Mg3HUVXEzM5R5sbxlPhU4sjAY_sflws1qvF1_9kwIgFvuSt4ZFYaqHYwPZ2HN8oUG-sirNuzGDFcx0xN0BREyIfaC4k_KW7_1icipClZtfANQvFZVH2kN_YguzVPRChMDnJGf8WbekIFdXsttCsDrt65b48dlstv6-3nZlgm8JLbFQIJGFL2QW9Hdis1hpSc6bK3CP7ozoFFgdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اختلاف واشنگتن و لندن بر سر سرنوشت جزایر دیاگو گارسیا
رویترز به نقل از تلگراف:
🔹
کاخ سفید در حال بررسی طرحی برای خرید جزایر چاگوس از موریس و کنترل پایگاه راهبردی «دیگو گارسیا» است.
🔹
این طرح در پی اختلاف نظر با دولت بریتانیا مطرح شده؛ زیرا واشنگتن با برنامه لندن برای واگذاری حاکمیت این مجمع‌الجزایر به موریس مخالف است و موقعیت این پایگاه را برای امنیت ملی آمریکا حیاتی می‌داند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/657400" target="_blank">📅 17:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657398">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ایران از هفته پیش گفته بود پاسخ می‌دهد
ناصر ایمانی، کارشناس مسائل بین‌الملل در
#گفتگو
با خبرفوری:
🔹
ایران از هفته پیش اعلام کرده بود که اگر لبنان مورد حمله قرار بگیرد، پاسخ خواهد داد و این از نظر ایران نقض آتش‌بس است.
🔹
آتش‌بس که برقرار شد شامل لبنان هم می‌شد اما متاسفانه نه‌تنها صهیونیست‌ها اجرا نکردند بلکه آمدند بخش‌هایی از جنوب لبنان را اشغال و بخش‌هایی را تخریب و کشتار کردند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/657398" target="_blank">📅 17:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657396">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCzERuyVCZNJKTRl1bh99L70TJ70g3Cio-xeJXbrvQ8adBMXv6fwFlCrYm5Lfb0zu61_AXwoLV9rwaUs1QDFoFZ0kO0C-SuR64n6gPqGXTl4NJhhpWK3BVBromr_hQl3Y8BkPRuu-7YlYtjQ2dbDQmEL-cTppwXv3eTmgaSYMl2gbAZHmjNAlE6Y8tirF5pIrrt6Kam8qb02QLZIdkuBRX_MhiBNdLn9L-wjIU2hVsprq-LzfT-qgjkPvEMXH70GwyZ44hbPXNHpruWVMI7B9b9o3ksvRpOwmf9mAcQBSTKz79xchQxuhuNBzFK4X6WNNRzsyHO5WnMLI5Ldjhr9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران معادلات منطقه را جابه‌جا کرد | حمله ایران به اسرائیل؛ آیا قواعد بازدارندگی در خاورمیانه تغییر کرد؟
🔹
درگیری دیروز و امروز میان ایران و اسرائیل می‌تواند یکی از مهم‌ترین تحولات ژئوپلیتیکی سال‌های اخیر در خاورمیانه باشد؛ تحولی که پیامدهای آن احتمالا به‌مرور زمان آشکارتر خواهد شد.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221488</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657396" target="_blank">📅 17:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزارت دفاع عربستان سعودی: آنچه درباره هدف قرار گرفتن پایگاه الأمير سلطان در الخرج منتشر شده است، «صحیح نیست»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/657394" target="_blank">📅 17:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657393">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AueKdaCqRGSJP34W-LavWxrqmWMTO50cgX0SVmVcjOC5Ax03sUgya6j2ebAb6NZKG-uxVlm6W0-M3WQDgISnbPlqxKfd58sTCDi6dAWj57RHl-QZgSTU6jN4CUhP-Yr9GNziqycKDNG_k3rxn02AErrdBDw3_7jBmrNlwTSLQh4fwGAuSnliJm-5RxpLFNG7zg_BT8XENgEKjFHjDt9fJi3XOfSdWcT6X8Cqm8W2dLhmXD80FjJK_ZjmoUGml2ewvWuE1kTJuRpZULVUKHaLyhSbKH29LgX2_rfPuq9DFjrQ4SH6GrPf803DLhhv2JIPQ2M_Dw3PLWkuQSfvTmEYYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657393" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/077152c1ab.mp4?token=DgyFP8qUTYfmfyi2kPjf60qZDGCeSuB3HBf500dHe2cZKuqdYuLBW-ReWMRdrguhTEMGhJTdsfgV9b733DTWvmWdj9JgpqWZSfz-e559WKx545uEU25ckPfETPAWjEqmiMpeUrZDwfmYZjowmpWwWS76NZS7XEvHo7ZYePBF9qma2XqGOWkS1OnN19pvKBiW6TXMhiIVnjsfcfLMCTXIZ4JAAMF-sj1XLgcEFJoSG0l9Q0EAxa86DphMhR6GDKxcqrL-ML7978JsFphGYNMe2ZqEucv7O3BtX60_gTUfPl-Ci5uOAPUXrE4PuJS_NeuLU2-KTcEXCaG0wQwkqxyAsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/077152c1ab.mp4?token=DgyFP8qUTYfmfyi2kPjf60qZDGCeSuB3HBf500dHe2cZKuqdYuLBW-ReWMRdrguhTEMGhJTdsfgV9b733DTWvmWdj9JgpqWZSfz-e559WKx545uEU25ckPfETPAWjEqmiMpeUrZDwfmYZjowmpWwWS76NZS7XEvHo7ZYePBF9qma2XqGOWkS1OnN19pvKBiW6TXMhiIVnjsfcfLMCTXIZ4JAAMF-sj1XLgcEFJoSG0l9Q0EAxa86DphMhR6GDKxcqrL-ML7978JsFphGYNMe2ZqEucv7O3BtX60_gTUfPl-Ci5uOAPUXrE4PuJS_NeuLU2-KTcEXCaG0wQwkqxyAsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسن رضایی: تنگه هرمز مال ایران و کشور عمان هست، به هیچ قدرتی اجازه دخالت نمی‌دهیم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/657390" target="_blank">📅 16:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: بند ارجاع ایران به شورای امنیت از قطعنامه آمریکا حذف شد
لارنس نورمن، خبرنگار وال‌استریت‌ژورنال:
🔹
پیش‌نویس قطعنامه آمریکا در نشست شورای حکام آژانس پس از اصلاح، به قطعنامه مشترک آمریکا و سه کشور اروپایی تبدیل شده است.
🔹
در قالب یک مصالحه، بند مربوط به ارجاع فوری پرونده ایران به شورای امنیت سازمان ملل از متن پیش‌نویس حذف شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/657389" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5a518dd2.mp4?token=Na46LzKAqCZ64qxrLEvQNSADrNEaLvs7y9s6YZSUHqWq90JMjrnapSAaIvgdWrZKb7Oa_cNIfgjR7mWnAc2_hoaM4kOLUfp6bIn1XoOiEbCcoM-weyVpPMmeCLrPq4Ma4y5y8l8PpOf-JGBAMTlxeAn0iwBB2ycpOdBJa6BRqpF3kPN4S5tiGd20YRAgPBfU0CzkxuIAUuwNBIbm6D7tcESnob5zXnRa6bcPWxgJ3gODXE6Kfp7OJH9t9QZMG0XZtGAYBa_RsmDtiApyptKzzzoakKYG06CHw3AHDnAEZvdxMRbmdyYLZFc2dcGsY6mBRx-tt1S016G0gSQbqmiveiIAFWwlb-lkuYgNR3j_AmJ0lh-8Izisph_gTnxlQAHQaJrmSxSyLWXgpfHqLcVTgQfto1tyAj9o3z96NedfPBvi011o-uPOYRlTetf_GcUmJVDJdRE9LgrwkBnh2xs4ST82zKYlNLMdtJJlEwhKsDSlTXqSWPchxWIj8GK-DpngQ9x5LLjkQiM6DLDNCFlNSdbBQu5-wXwWVm5xlti7SUF5cnzpPEm4B-9QwVc126eU4sYmyX5iJOuEuf115gEv-LRVGwDqDaUv83u6nY9vd7cvfDTMGAUUM05m_sP7G7kGsd5_wmElRGfRZUHKmpBB8dotlucHdHP8gohkYZxUs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5a518dd2.mp4?token=Na46LzKAqCZ64qxrLEvQNSADrNEaLvs7y9s6YZSUHqWq90JMjrnapSAaIvgdWrZKb7Oa_cNIfgjR7mWnAc2_hoaM4kOLUfp6bIn1XoOiEbCcoM-weyVpPMmeCLrPq4Ma4y5y8l8PpOf-JGBAMTlxeAn0iwBB2ycpOdBJa6BRqpF3kPN4S5tiGd20YRAgPBfU0CzkxuIAUuwNBIbm6D7tcESnob5zXnRa6bcPWxgJ3gODXE6Kfp7OJH9t9QZMG0XZtGAYBa_RsmDtiApyptKzzzoakKYG06CHw3AHDnAEZvdxMRbmdyYLZFc2dcGsY6mBRx-tt1S016G0gSQbqmiveiIAFWwlb-lkuYgNR3j_AmJ0lh-8Izisph_gTnxlQAHQaJrmSxSyLWXgpfHqLcVTgQfto1tyAj9o3z96NedfPBvi011o-uPOYRlTetf_GcUmJVDJdRE9LgrwkBnh2xs4ST82zKYlNLMdtJJlEwhKsDSlTXqSWPchxWIj8GK-DpngQ9x5LLjkQiM6DLDNCFlNSdbBQu5-wXwWVm5xlti7SUF5cnzpPEm4B-9QwVc126eU4sYmyX5iJOuEuf115gEv-LRVGwDqDaUv83u6nY9vd7cvfDTMGAUUM05m_sP7G7kGsd5_wmElRGfRZUHKmpBB8dotlucHdHP8gohkYZxUs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از صد شب شما مردم بگویید...
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657388" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657385">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df2aa9553.mp4?token=sUW6an4XM1v5qWHoHEHEsYgLpMoPxjMqnPeTIVMVETZdG1d87oHjhOH07pU7-WnF5XYWpm7yhxe9fFTInP_XNdd2RL5r-x8KyWEa5Cg8VrOZiGn647sdxIEhGZ_wjxO9A8P65Fbdy7ImN9J9s_3X5z0jyGsEclkFj-y4pT4__oeER_w0pKOMS7rcUYTqb8BaoQ8_QjIjQtjh3A0u1E-d5lWlKORJspeSceZu88F_ODf4KJJEjBP-AeU1BoojkOMxjhRU_8u4Z6VPSGOfXbQl1rVnNTzgAQQep1VStfXb2v_X23fd2ER4fBh4Z1nLOSAEHnSQLy1On9Qr3H9_19GJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df2aa9553.mp4?token=sUW6an4XM1v5qWHoHEHEsYgLpMoPxjMqnPeTIVMVETZdG1d87oHjhOH07pU7-WnF5XYWpm7yhxe9fFTInP_XNdd2RL5r-x8KyWEa5Cg8VrOZiGn647sdxIEhGZ_wjxO9A8P65Fbdy7ImN9J9s_3X5z0jyGsEclkFj-y4pT4__oeER_w0pKOMS7rcUYTqb8BaoQ8_QjIjQtjh3A0u1E-d5lWlKORJspeSceZu88F_ODf4KJJEjBP-AeU1BoojkOMxjhRU_8u4Z6VPSGOfXbQl1rVnNTzgAQQep1VStfXb2v_X23fd2ER4fBh4Z1nLOSAEHnSQLy1On9Qr3H9_19GJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تشکر شهروندان لبنانی از ایران پس از حمله شب گذشته
🔹
پس از حمله ایران در پاسخ به نقض آتش‌بس و حمله به ضاحیه جنوبی بیروت، برخی شهروندان لبنان با انتشار تصاویر موشک‌های ایرانی از ایران تشکر کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/657385" target="_blank">📅 16:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657384">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
اعلام جزئیات مراسم وداع و تشییع پیکر رهبر شهید انقلاب اسلامی
معاون امنیتی انتظامی استانداری خراسان رضوی:
🔹
برنامه تشییع و وداع با پیکر مطهر رهبر شهید از تهران آغاز خواهد شد. پس از ۳ روز وداع و یک روز تشییع پیکر مطهر در تهران، یک روز تشییع در قم انجام می‌شود و پس از آن نیز یک روز تشییع در مشهد انجام می‌شود.
🔹
بر اساس مصوبه ملی، هر گونه اطلاع‌رسانی درباره زمان و جزئیات دقیق مراسم تشییع توسط دفتر حفظ و نشر آثار رهبر شهید انقلاب اسلامی اعلام خواهد شد.
🔹
تدفین پیکر مطهر در مشهد صورت می‌گیرد. البته مراسم تشییع و تدفین، همزمان صورت نمی‌گیرد. پس از برگزاری مراسم تشییع، مراسم تدفین در حرم مطهررضوی در شرایط مناسب صورت خواهد گرفت./ اخبار مشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/657384" target="_blank">📅 16:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657383">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
🔹
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/657383" target="_blank">📅 16:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی توقف تجاوزات به ایران شد
یک مقام ارشد اسرائیلی مدعی شد:
🔹
عملیات تجاوزکارانه علیه ایران به دستور «دونالد ترامپ» متوقف شده است اما این رژیم همچنان به تشدید حملات در لبنان ادامه خواهد داد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/657381" target="_blank">📅 16:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J5toxzW-uqlpQA16xgNNWdTx2g1jgCKAw_2o5sKvZw1S0l9g8M4CaS78cxZn5TYHrPzHFfHC_gNWtDr_pgZYmuscYaDwUbDxay-w-yukJ1gEZy5QkSyynxzXHtnTHcvxwqjjaZKV4R2IOWGXXbNzdf2VgDyXEcWzl1ge90IEOFgmYmHvyoVO2wl0GiOpXy1rc4Hwm2EuSPswAlZ-Ep5jPWJnluzTMDUkQzQlUqeTOuudFrT9pCUt5uHTMuXuQ0_7FJQ-0HjbmHTTXpjYGanekKtBx2NrG1gJvY2d1_8BxzRRZRvmkf7ajIhDFeMiWwClWpwmbZxeAh8S8W7DDJA_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKZBdJB6v_eKzNtypyzjyEn2Tr13fX8EYmSu8BbkjK2BjmmPsPEqfnYpCyV6Dj1LykoRc1-0udscQD_lQE1RzzcS9LdNK7FpAd58v6Td99gM9OimREdZJeguaoscN_wdaBxjBdBLIlgDqJAj9TYAz8olAVE7PT0gRrr5XV7yJ6VenGvt9ceosGFUrUQ9jtTfWw7K9wHSSkz19gGFj9oGnzb5jH5B0HCQCnTSkZVFITcS2EaBe0lqiGRVv--4aq-GddCpNM1dupoYWTx08FF2OZ2IWMU7622JVFBo200RfjBxR0HVdJHNZgfJK7EU9_8QywilPiAQt_wxqH21IRIQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lm97MXqGqa-NQ2puNTDPDPMF_Co5Z1pzvrNeKtpHS_2CirIFC0lEHngMfuXijO_ruiJmXOZ6DL2vNj5UuQFu03urTbvhIJFnuXymrcnFst8RCf5dotosVy3QZUgT81EbBVMGkd7P-WUde1XRaenULKM6ETow8TjHqOh8jXgz_hgZH8ObDlv3hnGD2eVI4nby9-02yYz2rOewcU0i8UF7mJ65mXVHgKlMOSIr8B1yXa9Rpmc68aWywvI01LZYMtzH_DzHep_T5IAUL03NEvsZ1ULefNj5bp4fAC5YL63UrMaPqEudPo78Lz3ZGKXnlvt-8GYeAX0yzRQqhISQZauHUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هشدار درباره مارهای سمی در کمپ تیم سوئیس پیش از جام جهانی ۲۰۲۶
🔹
فدراسیون فوتبال سوئیس با نصب تابلوهای هشدار «منطقه مارهای سمی» در اطراف کمپ تمرینی خود در کالیفرنیا، به بازیکنان و اعضای تیم درباره حضور مارهای جرس هشدار داد.
🔹
این کمپ در منطقه کارمل ولی سن‌دیگو، زیستگاه طبیعی این مارها قرار دارد و از اعضای تیم خواسته شده برای جلوگیری از هرگونه حادثه از ورود به مناطق طبیعی اطراف کمپ خودداری کنند.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/657377" target="_blank">📅 15:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657373">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYJr5bAaaeWhwGJE8VNqNrkqRUYu_UBFjQGrAeZoM7F0hBy_0bq5vowOsoeyz5vRjUkAveB3Acmz21DWzmK1LmgirB1nGE44WAlZbyuJ-u1o67wswT8rmT1exq6eGsl7CW5t-EscS8Wzb_QLTbhSN3Zs6U_6vQ_HPkcTCjZs7cZWPaOGpPMxbHEOAde6E0PKibK5sq9VarDeyAOEu3GREJZMCn0is_jHhYGcx1UsIBwisigEphdJwtXtANiPUokQWJF3_Wm-Ctl-eY3Xx8raSvtv1NSBbKi0NS7AQUN6hcvqDTiDE0R5cp4h2JSITZJALi6-F--viudn_gqU4_Pftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم اسرائیل به منطقه مسکونی در صور لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/657373" target="_blank">📅 15:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657372">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgxIIB7h9ah9UrN8RKng9zLOjBaXKnoyYEmprr6mgD7Junx_XueQv5SoqUrwEbbr3xqSUYSjPVlutaY9gSadJ11l1gDsG3kUSA8qq_hVOprIB8vWbIrjyNTZcRZQncIQXJqCSiTX2REBRILfhr01-hvIUKuLANQzS1Vgbns_5ObMiuhAbzOJ9bGCz7fzFjZqX_S_syZJ63vvzdJwU2PeTtGsg8AbWVV1-_m1_BjeYhRMm_UhBx2ixopMwzbrsGJmoG6Q6zeC8yohQ0E4e2wAnybAJcB8tCtUdroGXIII1phk2tSOlnzinrZP23nAE0_dRBc7EjHQ7Cjne42TKNxJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله هوایی رژیم اسرائیل به منطقه مسکونی در صور لبنان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657372" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657370">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqMmsOjRudaViTuHN5XqN5bn6LS1uzJ-1XeTjUCjDaUqiGqZKrUmmoFqFtggwIN7uMeZ-op-Xd2lBdlhhIFy49517VI2y4xGoGuMhyOVA1jLwW3lDYZ4qbFCMbL0U14zXurwzgmUSTLaUhSj8qMbDYHqN3Qz4nnAC1Isp12fWExLxaA_hC-uqdM1_Avte6YXoM_1WLNeGp-XsLIQcF4jN76LlpZ-pwI1RQGfYRDvtva51Xtm8MWgbPwLDdWjTnQA8fFJXx6bZkh_WX5eTEE9MOD0N5rBUKnyFuN70pCNTU2_nnasNOWYwemxSQU3gI8VGmndgxAVZuTklGUwL_Y66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تعرض یک ملی‌پوش ایرانی به دختر ۱۴ ساله در ترکیه
دیلی‌میل:
🔹
یک فوتبالیست ملی‌پوش ایرانی در جریان اقامت تیم در هتلی پنج‌ستاره در ترکیه، با اتهامی جدی از سوی خانواده یک دختر ۱۴ ساله بریتانیایی روبه‌رو شده است.
🔹
پدر این دختر مدعی است بازیکن مذکور پس از گرفتن عکس، از طریق تلفن همراه دخترش برای خود پیام فرستاده و سپس پیشنهاد رفتار نامناسب داده است.
🔹
به گفته او، خانواده موضوع را از مراجع قانونی پیگیری می‌کنند و مدعی‌اند پیش‌تر نیز شکایت مشابهی درباره یک دختر ۱۵ ساله مطرح شده است؛ گفته می‌شود مسئولان هتل همکاری لازم برای ارائه تصاویر دوربین‌ها را انجام نداده‌اند./ رکنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657370" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657369">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0270d3c6ba.mp4?token=G7jHfF6kX6MjWIzE59OuMkwSaZxMuaxrIt8oEo9QhoiyGyt8tR9l0VBX2zz6A4G2VU9DjG3excXqt3oChyuv-JLbIPqqPTR4ucfeS3sMUqB3F1VrRtBFqRl4-HVWVPj5zZwHVzMU4uyZHsFHlqB2xQ747_-aQootrsXtTmybPyiYEa_Q8LOeg-YN2Dcby0sydYYfN5F-beZThv776uePjiEfF1IY7qmxzQ6dU7O_27C5JWz9Kw0ckAq4fr1OkFSh-MKA7G-oN37JPnQUWXgYM2imZr_M9YytoFYVUwBF0dHR3dsS3qvUrebPrvZXZ5qh6cPgk4lpvlMfLOZFDX21wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0270d3c6ba.mp4?token=G7jHfF6kX6MjWIzE59OuMkwSaZxMuaxrIt8oEo9QhoiyGyt8tR9l0VBX2zz6A4G2VU9DjG3excXqt3oChyuv-JLbIPqqPTR4ucfeS3sMUqB3F1VrRtBFqRl4-HVWVPj5zZwHVzMU4uyZHsFHlqB2xQ747_-aQootrsXtTmybPyiYEa_Q8LOeg-YN2Dcby0sydYYfN5F-beZThv776uePjiEfF1IY7qmxzQ6dU7O_27C5JWz9Kw0ckAq4fr1OkFSh-MKA7G-oN37JPnQUWXgYM2imZr_M9YytoFYVUwBF0dHR3dsS3qvUrebPrvZXZ5qh6cPgk4lpvlMfLOZFDX21wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های عراقی خبر از حمله پهپادی به پایگاه‌های تجزیه طلب‌ها در کردستان عراق دادند/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657369" target="_blank">📅 15:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657368">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📷
ادعای شهربانو منصوریان با انتشار تصویر دست زخمی خواهرش: رئیس فدراسیون ووشو با چاقو به الهه حمله کرده!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/657368" target="_blank">📅 15:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657366">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3lUChKlGg3UspVdjZVp23GNfvfcsM6vVQxMGQ2glYTMZ5aoSO_dLrkvCFqiLFl2_sHyhihpRGz6R3F4ZjEPCrwMl6H8rgiX-QzVow6K87plkhH7JsxdSE5D_bHMs-Jwpu0_fWNtcKBcuqDU2CDZFKLAp3HvfGGBQi1EoEW--avUQ3DjIAQFgvqeUiO2pKy6QmX9qa-UYSCuIutrzhkpHWs7o51tRvop08L-lk8xbguXAtsE3Nc-rGwVAz7nv1jmUlQ7Bo2rlRzm_hMqm0FLA61aTw0d6NE2YNPyU0K1esp272nc8V-noa2qBsLBRZNtB-82dX16eJTYFNVjfaZO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دیپلماسی و دفاع دو بال قدرت ملی‌اند؛ نه میدان را ترک کرده‌ایم و نه میز مذاکره‌را
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657366" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657365">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSMwFhwhmfJV5SfUlPJqIOdXgntr-mcuqFjizr7k1iQdd1w4uXTZ13C_aqL8XK74DNyjKQVj1Abh6EWWHCdBhh97yzijpWU2YNz2uyDYbFQWRrVpkhQYshQeaOJ7oaw8SSxFEn52lfzTvWBmxDeLgzFvE7sJuSWg98rvRPZemJHQWSXHCnoDEgj0h2Uw3UepB3PoBJRIYT-TOIuScm4ShAGWEj3B_Kfk5THNQMaxz0fFI0br0OKwEUk1xpweD6rffwj5LZl5fvm5tOpl3k0cAnK4BQ8ra5ee3MkFHPdZcV0b23InxtpDoXJP2F4ncgVUMYatksSl1Z2khHoBqRQ5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هواپیمای اماراتی در مهر‌آباد فرود آمد
🔹
داده‌های ناوبری پروازها، تردد یک فروند هواپیما از مبدا امارات به مقصد تهران را در آسمان ایران رصد کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/657365" target="_blank">📅 15:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657363">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
عراق آسمان خود را به روی پروازها بازگشایی کرد
سازمان هوانوردی غیرنظامی عراق:
🔹
حریم هوایی این کشور برای پروازهای ورودی و خروجی در همه فرودگاه‌های عراق دوباره بازگشایی شده و پروازها از سر گرفته شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/657363" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657362">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2att15hk28xM6ppf6r8lMe5FeEvnxtYZNad3LD08n8h_Guirbu5i9mBWpHqUkGw0SYM9x2ZEzVcMNBlPMJK-_pJ124nlnrraWkBfDTX4r2pztAKmN3HOjoLGKBBxHkgI6hcaIllss0HJFrtO7Wrdfzsqc7Ie7NVZtWwtmrq-jyFBJ6LGry7f_y7_Ecv9WmNFQMzSV_kODNGHmCJ-X-Iydl-vxR2XCFjyGlLIxsQATRp7JfgOx2eo9GMjUOiElAedTm1709Pi0ZdR5cDd-hRy-E8uOTzqTSbT6yZB-B20n8wNKKensW2nCPjjtuyDbDJ4WKpksYKuDreIJnhTmH-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به ۹۴.۷۴ دلار کاهش یافت
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/657362" target="_blank">📅 15:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657361">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/657361" target="_blank">📅 15:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657359">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3jhc7uOWB2T90HTnCcev0Mb5WNU7oiX2Ghg1gFeLEgk2BJRDkz1cwwz3b_7QXna6paId_Bn4B-P3RTUMHSrcPkr9LnI56EQ2CVmslE_XK7bM4XrmO2VKUZfYjnRQJFZMipfqN_vtGU9t4300fgfmCrabzBo77pMGebk4qo-LsXhGNb7Z1Kz4tauMhoKbLwJ23SzVtdDMk5g5KG7HfzcOcrqJxNRcMG5OhhK6MjyKTXv8_vU4qCrZ1O-4sjf8tAM3bkAVvVyb0PfuLj8Vj-_nxpKbYm1CBtBz5M6b1e6ZT1Z2WKWMi6la9KGwC6oF2BsEUtmQx9ujBpXZBZg_wiG2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فدراسیون فوتبال
🔹
۳ روز مانده تا شروع جام‌جهانی ۲۰۲۶
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/657359" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657358">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
اسرائیل هیوم به نقل از منابع ادعا کرد: رژیم صهیونیستی و آمریکا پیامی را به ایران مبنی بر این امر انتقال داده‌اند که اگر ایران مجدداً حمله نکند، حملات بیشتری علیه ایران صورت نخواهد گرفت
/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/657358" target="_blank">📅 14:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657357">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خبرفوری
pinned «
♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/657357" target="_blank">📅 14:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-657356">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص):
در پی تجاوزات و شرارت‌های رژیم سفاک صهیونیستی در جنوب لبنان و منطقه ضاحیه که با حمایت آمریکای جنایتکار صورت گرفت، نیروهای مسلح مقتدر جمهوری اسلامی ایران در راستای حمایت از مردم مظلوم لبنان، پاسخی دردناک به این رژیم دادند.
🔹
پاسخی که رژیم جعلی صهیونیستی و حامیان آن باید از آن درس عبرت گرفته باشند.
🔹
بر این اساس، توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما تاکید می‌شود که در صورت تداوم تجاوزات و شرارت‌ها، از جمله در جنوب لبنان، اقدامات بسیار شدیدتر و کوبنده‌تر از قبل در راه خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/akhbarefori/657356" target="_blank">📅 14:40 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
