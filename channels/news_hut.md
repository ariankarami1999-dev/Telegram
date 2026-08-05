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
<img src="https://cdn4.telesco.pe/file/IAp0lxosLpzmXajifemzV0lrtYevhYkhQGChPvGRd57HMR6sMQyEfKw3DXyE_S3eZGf0Va4qqSIMv7NP-K8-C3ow_sT935BmghzcPtOE55Z3s4SOcXu7P7n1KufUFDmso8R3xzeWRIMcrqcRpAogN96pIKtsuKjPNtk47E45V1xMJz1uaS6BOUacuqHHSBeBRk1JjtC0HE2tcC7epAZGccZm86GOB-D1YMgnrIQdtjBNefKpek94QydNrHhYxhfu5jnGkGUYud-AIqdJ7zv6bjO2a4BJmesqIleKW24frv_jl8vD7-XK3ZdAzon2yb3Eh4wZfl3mTtmfLUdw1jPJKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 135K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 05:21:00</div>
<hr>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=agHeGS9OsGj0xZkKIJT1scMTMy2EyarruO8HtvTra_m5gGz8R-ezq7okB9iFt_Ne3ASGO9AuBdxq9MM-m0RFFeyyk1DWpJi9_WHjOUe3_LYGQ2c-nXWxRjnYG3VtdTwfEHNVwAMyHwko6ozS6aZcctmJaS5BN9Qe7UTroAhW3MjGnE5uNGdOnrJ6PW9epXsj_zwBygct4aAn3TAB3KD5uZKk4g7BauibZ4PnIlUsbl5c8hnIyJDDAkGGviZbHsAvcYLottEqMC9G4aHpg1QzFeT9ThFE6EhNdzFuQyo837fBWnrCCiT049-XX91gmR2TcfhayS7dJ760GGV9azKg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8GjKeDsmjXIxxnFEomLQ-5ykilfp_a4WJNOuAWdP4ngAIGHJEa0qn9za8M7x84s7oL2IlSu7tBjrrpDRPc_smDrH3TrezIqKVeX53XNdz3c05f14jfzDxxTfc73WJwBgXTFimdqZ0PlTi39if4ml8ed2PAFMcYhl4QeP33wAoxbSNkfIINRdsGaSHRv43Lzp6UwAFd4h2ELbfvScTj7pEe-k8VzaLQw7Q3sD6038gaQcyY5l9-IIMgIiDXmkddy9mYswHIGvk-QHBXxIG3lBG55YDXpKAlcrGPU8hWE38EX4cUtrnD1t10ELk1po6-3pkfIoBWeHAbnzA_1tZQ7dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjhTbHSzWrpmmcqdvLYpogz5smzlz4xVlqJArkjTZPcDxOk0AGcVth3XAUyPA_M94LfNyPLNZHG17AqZrJwW0gVWyZesVHOeoeIVjpK1mzgrcjm2fGN02eQ2-WyVSNy1lZY_0ZDsGrzMdQ9q1ZwZNq3hoaaBx3EgcuV_HZ1jTs-uvbunrsTv4PD44sXKOmmgYTGYhr7OghcHFehqGjulNt8rRJNJFdZRsr4TiI0BFinwaHGr3TSncbf-G1qZPTv7z0z_LlrmYcnck8ZFosvZjEdKWwV53D2euDaZxS09pZoE0sCemtNi9oGZywXtFLCHhvKQ-g5bKElrnHwrtxJPYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSpbY4Bn7879deH84mNvbQG6eEY5xp8YLtbpWlTY_Y7i0cNlWwI0EgFY3lpPilI4TvtI1lG_zpIQOZfcl5Rg3iPuiGDHYUkJUZp02BJ1d81gCMUhhNmOFz5PO_aLy3_89wgxnnQFHe8FSjLjuXUD94qPcWGFOOeECLwlgtcCYsMaSRpsYH8VnPVR5iJZ4zk45vTD8xaEzRQ9lF49xb9GjEZ2j7GV9Yzl8XqvL1volnmbTLdiDJP6fmn2b4vfRzW097i75HRR87LCo-QeTTfeogAsgEq3kG-tQZGVaXHNY2dxhcu24vfWFoITJsQPBflWrGhzs2FLYl56z4Hp7mF3_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RI9qXqxAS-W5IjzCRJbc0VhJf0UkgZUBJFu_6KyEF93fBFENUWLTI2MfpMBom6UBOmkK8ZMYzGYjfl9H3hIwltjIftU7NxhPvqbbCSctnyUHvBsZawSEKOA4xOHp5MmgxSab01T1_cnkPm9Fi3X8qC5G6OjQnlnVN9GPY97dOm6MJnZX2iEFRoW0k6AmPFMfNh_lJXmD7rWweKfP2BabbUngtA-WeVjxkuuX_6ftpiM7H6ZcLTNqQio3JOVGeDUvNcsVNFuUUSzYg9rk8f9aruKdJu3SnZ6831cErQjxT__lp18asxCZPTQwrxJ_12l3Mr-csTWTTkeWdoSM6E9u5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=bShf72abCQ-80qSUO8L1lesfjTCtcXbmyrDs5jm44qxVQuHBBIWpPWobSB4eui4RzFKIh4P-XzeIv_RC6XtxAf0aWQRgPX8XHkJLzq2OCuQ4fB1gEWyhb04Wh1N1nLxY9-65PVNeTBXXmljd4KiVLGeZwYa4KXdLOmcOIozBBC22lVC_zIg0EZi8PE8WKgmBVm-8k4R0qBKYtXqXPyPf4phRWqYeFwavuEUfDKgsU75v6j5jN1pz1A84SRRPbQ3D0Q2VSYblWzD-7Ra7LRBgYiyHxdZrsPEiL1GnwnD9t59XFyPp-7W7oP9F_dCZppW67tMohygvP8j0CmVrfCs5LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=bShf72abCQ-80qSUO8L1lesfjTCtcXbmyrDs5jm44qxVQuHBBIWpPWobSB4eui4RzFKIh4P-XzeIv_RC6XtxAf0aWQRgPX8XHkJLzq2OCuQ4fB1gEWyhb04Wh1N1nLxY9-65PVNeTBXXmljd4KiVLGeZwYa4KXdLOmcOIozBBC22lVC_zIg0EZi8PE8WKgmBVm-8k4R0qBKYtXqXPyPf4phRWqYeFwavuEUfDKgsU75v6j5jN1pz1A84SRRPbQ3D0Q2VSYblWzD-7Ra7LRBgYiyHxdZrsPEiL1GnwnD9t59XFyPp-7W7oP9F_dCZppW67tMohygvP8j0CmVrfCs5LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwegdNTHBifrCNGBYkygHXxegJAtLzJ0gy0XVuQg9cqbu5Tb_JUR4qnuDx9M0nPGgkQW20_Dtc7YJ8SvQuFKuQhiDddKBIAYvvAj4-1VcShCCowlGtSuPxOvGrv43LHOLCk1sKpS0hsx1oPPT-iKCSCwQ9DQrIESA-gfgeIKSil8ttHge-mvj1ZgtyBTVOQWrWtfILl7Y9OToksYePyK0Y4Y_z4CtCRHYSAVuugll1RWITzgvNMVTyQQW7Co0A_GklGMMrLrNqanr_fLnqGwGhUzeSa-I70N75xumWrpIUW4hVCZO2k7exzxFrHawFsXiM6UPeerLnzn-D0zH78lPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dsXqzc_gyOCgJKc1Kf82sYbrc_w9_R4OYrhQuVkjNaeUgBiZPo4opi39iv6DYq-9NKLfhUj8aqFCHrS0O5MP9C_WqQymDLGOpcHrnpm5D9TJtkactTkyNg9vZhZUdDQ9weJFITUECBcnhWM312BYB_6CI4ADWTcmsT9D_ZvEyIhN_DCaEO6aUsVr7TRUxbidRRxRoSsLqjPQIITQGHZ9KlTtUJiYZfCL3Dc2ktxEPuxmGjQpjXqYThBECss9HNjWkqUbzLRAl-JpkkUNnHfVjGP--YI3gv2zfwN4K_yRd0EnyEmmdsTQLxum0-l2mPhyqPgXRkd5Q_kL-SKjpX7-gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss1U0eLkkYpYFcaB3jVgAyy9kSfanJXMlr11tvU73he2HPTVWAErIm6bqfl4vUY-Fpjz-nDZSR2cJijemDDF6zAHk4_2hjQTZjkZd5RyFZolWfMx5SF06Spr8BZ_mlpQguH6lupN_97jGu3QIgEniX5es6c_qfhxO2iFcUsJ9SvWyHLUEEh4kN4cX55IT62ViX_zM2KtOPo4-9HUrFbFLbfCXfYcsEJOFWG7dHrO7OZ9zH1nKhrwxW7_vGqq0QMaruqpWVat-r-L-a14QzbpBzxygMwWig9vpogLV54Ha5JHq2Fp9v9GskNOfb78nyjRBiEO1TGkB162b6qd7wRwxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=N-Mu9d6LT9QQTLL9sJIqy1DVvF12d6O4A-S2Evd3qLwz-aZ92pgUA0W_gfeb0ErnmfFV-s1XGp06gjxgEMVbnLhr-NRSxO9jwfG6u008bnm7DhpfIoSBlycMko4u-DLo-wYTQDliULI2cCjfwqEWpfYhd8OELtiyZ5Rz0uyR3t0eUgiuho3FfgHCSkDSaO5yKQORElvzVwlE3e7diA0NJunx78OoErWRf-jUtgD2Bb6HqiUCz7KrP_uaWCDdYsPENr6YBo3qI7VZX4M5vLrFDgFtULIWW2LhyQ8anmQJqg6EFJztjhzIcb68oGRjrJ9HGsm4Cv1hIY6WGmq34bhhgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=N-Mu9d6LT9QQTLL9sJIqy1DVvF12d6O4A-S2Evd3qLwz-aZ92pgUA0W_gfeb0ErnmfFV-s1XGp06gjxgEMVbnLhr-NRSxO9jwfG6u008bnm7DhpfIoSBlycMko4u-DLo-wYTQDliULI2cCjfwqEWpfYhd8OELtiyZ5Rz0uyR3t0eUgiuho3FfgHCSkDSaO5yKQORElvzVwlE3e7diA0NJunx78OoErWRf-jUtgD2Bb6HqiUCz7KrP_uaWCDdYsPENr6YBo3qI7VZX4M5vLrFDgFtULIWW2LhyQ8anmQJqg6EFJztjhzIcb68oGRjrJ9HGsm4Cv1hIY6WGmq34bhhgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2gUsnoScekGBuB3xIyEGWpyXxTuJ3vrMza0p6ZNWbYTd8nYEdtYoVZq4Za6EaoKelFKI7xErkfUeBc7wYr3Xd-rO57hRviIDB-OVx4JVhhpPhp5-ZC0DGGBnOpQ59raprYEzqUGF9PGQysYq7JIcCvFxPnwAPSpGTlNeZHbeFTJDW0Ur2BTETECB_CA0lke89TN6lSK0boi6XeJmkZEeyTt_AOaJBRWIHELCsyN9RYy_k2YSXAEkBv__se80dCmOL1O2jnoHZA185Eft69x24JHKUtqTJYsEQEg3HpI9iCVwgGyENWooQj1Jahh9p_Q06dUHajpKBI5Wrqgj79kfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFovRvHGf1_DVMMjc8glAv_NEbhYR-RiDjY3GIkTeLRiq4ae4pruGKchs0fZfp6RThQLOqnptRW97U5ckxXK-zTC3iMf0QB1IVXCdhli5XYHrNAUu2YFUn-t1eSgVyp4h-Kyd3ATb0TZ4ZVAI5lr_IfuK0b56XONZhNIBQlVKP17ONZyOkcdElFgLXUcPpmiiadPUHAv2TzxOtwOtxnzZXopZY4xVyUTYnogPo2nCp6jfN-q2KYbQUvBZ6OfVgpDbuT1d9128s3R0SmTvsjw0EPqgue8islgSotS4iTT3O5cOF9c8uAotsyJuXpboyborIKAl9irqTIewz6zRaFfTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHI8E_TBOW4RfK1tKAkRfJ-OUcVQA0Qcbr_49SxpYKjc1XzJ7xIxPNa8Rm5e9kPyxt9cwJlImMbHfu72BfMRbl4S0y-EFZ52AdrxksMk8uZAFn-QGRlyQeVgtfcov3_dtbZXak06BzkxkfiiWnvNKO5NJ_LMs09I5zMOs3lizdVI-3-eZ05HiKrStxQD4WSRkM2ckrYcVLW3odCAN_tj-26I479Rain2ZjDKn9TfHbG0uNDqp2EUm9z2QUJfjXU_laEs49yzrZuhmH6EUsicd4XJ3lMsMIXosMjMavnrWHEPN4eC5u591VWS7ltfn5JYdvhCiidmU3o13dZ5fIHKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=mG4diN1xeKWo1dnWhBe_ZkquCn_BiYiiMep_cXNY53DFXpMqPOxyLFn0CFkNKRi5QP-0HnLq4ZB1H_wb1PCZQbQIOt86q3GqTkE62UVJFtrZO4D7gBVT7WrKc17S-uDOwZIgf20xx73722vkJ83v30pKt9ANHLYwfrBcQTCDcChPZZ6vpEqx_wezZ8lxJYBH83RfkDfiC3EGHYt6TiHqor69PgUAD4ZoRKfLvWOdaUhTaRc2766afzmcs5okdHbCteAdW9dic0FGq5WvFUF9nBypyx6h-2FPe3HtWCO_ZolmyEhkC1hDK4WY7mSZDZmWZ-EQZAhSx9Rgke9QRaJ3tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=mG4diN1xeKWo1dnWhBe_ZkquCn_BiYiiMep_cXNY53DFXpMqPOxyLFn0CFkNKRi5QP-0HnLq4ZB1H_wb1PCZQbQIOt86q3GqTkE62UVJFtrZO4D7gBVT7WrKc17S-uDOwZIgf20xx73722vkJ83v30pKt9ANHLYwfrBcQTCDcChPZZ6vpEqx_wezZ8lxJYBH83RfkDfiC3EGHYt6TiHqor69PgUAD4ZoRKfLvWOdaUhTaRc2766afzmcs5okdHbCteAdW9dic0FGq5WvFUF9nBypyx6h-2FPe3HtWCO_ZolmyEhkC1hDK4WY7mSZDZmWZ-EQZAhSx9Rgke9QRaJ3tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=f-FXlXdJHTfLPe5DZ4R3dnI_LZbRW62GxCKQk8Qz4oTW5TVGeZwjuv3rstgZWBG8EarK8NDtaPQETSaM9C7lKK2Pz8GWk59p1NK7H9KRrkDOcPsEt93dsalz7ssDYvIfXCnXZgDKCtVyr-r-BrfV9BhuSFctOBFdgX73xSL-5uk_YajCvCoFSxtsnKEBCDHH3vLeWkKRHxjwhIwsWNafae_Rq40-tzPcp6uXBBIwvH5Bw4xyYiK33A9VYC9-yLEgA8bBRbdInQxkatRicl1ZKQekfb80_mZQ1AQABlCHJv43m-49HJ5Nu49Gu1XGrT3YgrLYm9DoHr1QiqxNyZuO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=f-FXlXdJHTfLPe5DZ4R3dnI_LZbRW62GxCKQk8Qz4oTW5TVGeZwjuv3rstgZWBG8EarK8NDtaPQETSaM9C7lKK2Pz8GWk59p1NK7H9KRrkDOcPsEt93dsalz7ssDYvIfXCnXZgDKCtVyr-r-BrfV9BhuSFctOBFdgX73xSL-5uk_YajCvCoFSxtsnKEBCDHH3vLeWkKRHxjwhIwsWNafae_Rq40-tzPcp6uXBBIwvH5Bw4xyYiK33A9VYC9-yLEgA8bBRbdInQxkatRicl1ZKQekfb80_mZQ1AQABlCHJv43m-49HJ5Nu49Gu1XGrT3YgrLYm9DoHr1QiqxNyZuO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=YOQQ6dilprqXodFAGKIyuzDOwBOIhN4s79Y547pYekt160QvcAs7ZsG0k5hYO12eCnqFuqRfW5pQ95K_DKB4SeC0EB8GCHFz8GbSsqsatg3vhVB0Umri7o6f2armRpRfS4SnltP_1ynoF8JT2S_0-Lqmsee9kpBITAXJQyCg4RfMGDx8Q9QyAikQzFBHrLkZzJrFbbTtF0yYVwsZIoyMYfnGIX8BuFnJWNAhWfBgmnWp1nF6GUChyhwq1O2_dv5gPEOUxq8btmSK4XcMeaSVabsGb_ikICl8sqTFrzJcvluFNmZZBhlnIB0mYPDwC6tE_6_4D2IZ-5PQEJSVUvNqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=YOQQ6dilprqXodFAGKIyuzDOwBOIhN4s79Y547pYekt160QvcAs7ZsG0k5hYO12eCnqFuqRfW5pQ95K_DKB4SeC0EB8GCHFz8GbSsqsatg3vhVB0Umri7o6f2armRpRfS4SnltP_1ynoF8JT2S_0-Lqmsee9kpBITAXJQyCg4RfMGDx8Q9QyAikQzFBHrLkZzJrFbbTtF0yYVwsZIoyMYfnGIX8BuFnJWNAhWfBgmnWp1nF6GUChyhwq1O2_dv5gPEOUxq8btmSK4XcMeaSVabsGb_ikICl8sqTFrzJcvluFNmZZBhlnIB0mYPDwC6tE_6_4D2IZ-5PQEJSVUvNqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnlMqZPkEipH3Ei7Pc_877aGmlHUxULYW0M7gKf2jeiefnzpg5T-tXh-cdSW5eeWLXwDadP-Qcg-_3Y5t-zt7-GkXVo6J9DoaWA_k4KzKYQvFaxck4awA3ZRGtKP2zxBKYyA64JJ_-LXePiBUR1dfvo4Nrd15bW-bfcX4GPvxRYBVVBa61U1TjSNwjPrroOVdAP2OEMABvpHx7ldciHS1SldLNHDRKyhngw2lUy2tyO2qLKxlNnn4qUmC83MNHGMDhtHNJtpB69j0pp5cwR46hylSmj5kl4Bzg39VOULxTxzNQkFAFgtFq640mVtfvJ8LdXyDoLjcw8vaP97tuP9rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMCFvIWC304sDYiVUeiAqqu48vTkkpWPWybnFg45im3YiYGirkW7yIkQudnqzBtZu-ewqqOklUdst3ogmMX5pyHIzQTPr250AfCh1xh4_a0YAlegKuZaPW7R7Ccyw33HfBd2RdpK4U90M6wrQn3w958VSL2JxLE_kBNpPYSor2idmCXaS_LFAmuC1lwvDsN5K5W4aMwoffFyiA-OI1fSlU3CdJyT1gxY6G_B86ATI22z3wMK-LQV1S7FPFA63_LpiuZyQ7pLxE3euXY-EugW_LLOShxGvxcC4mBL1g86KE76pwF-wrlog1aN7JtyqZ9-bu4DMy24gWYDWMXV3Yo1rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=gVx5h7RhHn-5E15B8-Tbxjyyt-ceLzQErJqMc2wQA3BdjVA-_USs2pnPv1LNdrSH9osDcucIx305Nm1kQjltkg2U_GHJYSa-pEC2VduUN2EqaO3GgBAdEeze8cbNXZtcwyTW40xzA_G8YfXJIjIt7UYAFNAPqYn5DiRgi3IqPu-sDNFqBvkvU8Hr6setSLVcngk17wMhI6bF2wwOgauuTVh8kzGRTw6FN6rWsF7dQbgmfVN64xkmhcYGCtoBpWyeDgjBmzTkIL_9WU3nqMy9vLWEOESA6CldTRbVXAaML5r02FtK5n80BqLiQsrs9Y-Ket1jtfZKPJVeuYIfzRAgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=gVx5h7RhHn-5E15B8-Tbxjyyt-ceLzQErJqMc2wQA3BdjVA-_USs2pnPv1LNdrSH9osDcucIx305Nm1kQjltkg2U_GHJYSa-pEC2VduUN2EqaO3GgBAdEeze8cbNXZtcwyTW40xzA_G8YfXJIjIt7UYAFNAPqYn5DiRgi3IqPu-sDNFqBvkvU8Hr6setSLVcngk17wMhI6bF2wwOgauuTVh8kzGRTw6FN6rWsF7dQbgmfVN64xkmhcYGCtoBpWyeDgjBmzTkIL_9WU3nqMy9vLWEOESA6CldTRbVXAaML5r02FtK5n80BqLiQsrs9Y-Ket1jtfZKPJVeuYIfzRAgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBtL55xc8gGSLjref35PbQYBcVOJFFsX6tVUG7sZDRSySaFHLVSLDSaDdWdWMEEgBeXNqTVni4rZZC7Q7l5PVBuObFnj6SoPVB30J7pT_rI_OrrpbuTghNDlWC-tWbl5rQFWD8YLCfz_gHGZkubpwWa6k4Kq-LvDee4peLczt0QlW_uo2g4u1NZttKM6aT9OGtA8r2zKH3Jr9VK5iq1MsBGWixvB7jGwMl2uE3gxwB685XlCH52pz6Om9Pt-mNl5krcSBR9yLtafyd2nrgdJ5Z0nbr_hG7mQWmv_m-XcNzH3iMeG6LFT3zNLZPCl7s9lERJ7xpsgxkCGBqM9twl1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=OYY5hZPC7CRhvbvi8xLgevsUlc1YsfJ109kd86y7uApFHD3lWfkAHO1t-A7NUOhwxZK95rmm7NDsuXeUdhGsquON6GeI1REtaIOUaaG67V6fZMOwl6ukl9Auqs6a_HU0db-osGm3fbkinpoUcfhCRz7ugkCoNScsm_Mh8S8vwSsgclLrgTzicvF0Li1oY9a98Fih_pOjPAWIN-xpeKv6vYP9ehSBWLNJVCCnIKYZbE1dqexRntbcISa3G_YQEm0NnAuvM6tmvXEX1721QwmvBP3vUCe5iSyYjxE43yfXCy3wUoqpn6iywMxdy5Y65ITevHwkN97E0qmguH7TdwxTvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=OYY5hZPC7CRhvbvi8xLgevsUlc1YsfJ109kd86y7uApFHD3lWfkAHO1t-A7NUOhwxZK95rmm7NDsuXeUdhGsquON6GeI1REtaIOUaaG67V6fZMOwl6ukl9Auqs6a_HU0db-osGm3fbkinpoUcfhCRz7ugkCoNScsm_Mh8S8vwSsgclLrgTzicvF0Li1oY9a98Fih_pOjPAWIN-xpeKv6vYP9ehSBWLNJVCCnIKYZbE1dqexRntbcISa3G_YQEm0NnAuvM6tmvXEX1721QwmvBP3vUCe5iSyYjxE43yfXCy3wUoqpn6iywMxdy5Y65ITevHwkN97E0qmguH7TdwxTvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFTmJ08cQESAdPQK3DEgcoVqofsdFZZVOtvaeMdDieHscxsB6ViB93xDryqWlyF73occC6aJGqZn6K7AqwLE0RqtPKHiee8a1CUNT65xF5tDq8WONz4rPVQNfZpGAWbcc5Wm1Ij_SYvkSv-Ud1tNva2po6bhi69bncKqxVN8ldUJl5qJI29QmJxyi7NAd6vA46T7CifTOqam6S7ydHrl8CSlAj6XNaBhOfBOsVXNo1E2j8vhRGLXDvn1I8U6PaSmV6Sr6lmZoywdhgNa2QFXOvgKA7ePn00okyV2gm_dlpXJ0EOl1Z_suB6N3d7iNF-3kGB0AGmO3w8JH0IT0HATuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=udYjkV5Q73nj2KLGQkgW5rKbuOfTEUojatsUKgNDDUH92ow0ekeyFdZZaYd4t1Au86sCjaM4pLVbuYPCKmiX72B769ICS9RO9h9sCdsAA4yxrSxxuIrEIShAf3FnZimlBLJLEr1c2nKDscBjE0wrS6ko-aPOQmmhSCtznb5FjtLEuuYBvvpLI3pBi7v5NH2Uzd2UkQlt4IG-PiQs-Ae5HF3nrUIVh7yial8Qfd-Wto4yYHzAB1PzOSdI6vI1UoEwa3nN6R5yHE5dGMNSLxUOCbme9pL6bUocrzV7GAQwFlZFAEdAeuSo4BHXQwQh-NSEyTfmmT0rV-9YgJqsX0lBTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=udYjkV5Q73nj2KLGQkgW5rKbuOfTEUojatsUKgNDDUH92ow0ekeyFdZZaYd4t1Au86sCjaM4pLVbuYPCKmiX72B769ICS9RO9h9sCdsAA4yxrSxxuIrEIShAf3FnZimlBLJLEr1c2nKDscBjE0wrS6ko-aPOQmmhSCtznb5FjtLEuuYBvvpLI3pBi7v5NH2Uzd2UkQlt4IG-PiQs-Ae5HF3nrUIVh7yial8Qfd-Wto4yYHzAB1PzOSdI6vI1UoEwa3nN6R5yHE5dGMNSLxUOCbme9pL6bUocrzV7GAQwFlZFAEdAeuSo4BHXQwQh-NSEyTfmmT0rV-9YgJqsX0lBTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj4oWJGfuT3lgY1BMLeyLdpNMPs5QMtrXd4uBoPBhfwGjCBjSvnkG55J3aAmxl5RRsp5LNeIHDvn_xliiC2DxmeTcTdhKlnllQ-3myQ1fPkhGEm2sSUMe-9yDn2s7hsxlDpzxGo2arzcCCOaQQisZIjL5W_JmAiZ5ALJ6pRbReOdGUmsbcCGkfFcJ8U7xdrM36D5gOahXXxhTjo41xRE_8rsUMcwzG-OZhF-5UR6sp4BWQ7shCwHtR1ZYiJ4dcmk4UE4pH_viYuGXm6HTcA9qYmg-csagYen7TTBQC-kUz4_CpCSd1MFobLqGH93jf_lzdG8Mk2pvEvenitPJbbErg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=JpSG7mXjcGPV-kL5ijjm7Kvk4SBl0egzQx4zFsO6QqpO9Jnda8ydHlvZXC6BnVpwDu2qVlyZpsPxmkkrgs0gWtdxDLeDcNndcUth9T1lAChW8ts8LolIFPrxRHnIodSXhcZYVMZmEUvzIzvS_ED6wXU2hsHrHPEU3cO6mW1pA0pLQqi2CY5Qrpbqlh3HsEdDKbCBRwzKnLuawOjL1PnM-TuT_eJXTqCKEqyOruRR2H3mEF5eCiAzqwuCYz57msE5hd6vQnpvNxd-WtuJe4R-eZUbmJLi_kZ6jcAi0oN-TLNnzsewqv0H9aV3OrRAxPNCWrqVvT-GS1Anb9sVnbLZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=JpSG7mXjcGPV-kL5ijjm7Kvk4SBl0egzQx4zFsO6QqpO9Jnda8ydHlvZXC6BnVpwDu2qVlyZpsPxmkkrgs0gWtdxDLeDcNndcUth9T1lAChW8ts8LolIFPrxRHnIodSXhcZYVMZmEUvzIzvS_ED6wXU2hsHrHPEU3cO6mW1pA0pLQqi2CY5Qrpbqlh3HsEdDKbCBRwzKnLuawOjL1PnM-TuT_eJXTqCKEqyOruRR2H3mEF5eCiAzqwuCYz57msE5hd6vQnpvNxd-WtuJe4R-eZUbmJLi_kZ6jcAi0oN-TLNnzsewqv0H9aV3OrRAxPNCWrqVvT-GS1Anb9sVnbLZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=ZGGgM-bfV7htQPE3RC4nuhPHIEVDepCabgepZp5RYX07Y90mfwzunpuhR2mxE-t4I5XL0drbPMXAYPScPxDbbeicu51F4GSqn6Wzb6QiehgAYyNVO2mv8qfBXm6ZI7_FxvUtdgTS11gQuG2bDrhapnk_WW-E3rAr5iboAIWMEQaVSXVs9vZQWcM2QeYjT5fVW1q7dzMyzFnh88GPulRUw-plBle3n7PE7z4Iauie_jG2XKmDrGJi6zbjKSkbfXW4X7dXmh2-0YOvHomWteD8FZF1pA1DOo_YcRgbvWZXSxWcorB7j2TYBdkSoBhwPCgEUWiY2mwkvUXIbYKbq-gdqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=ZGGgM-bfV7htQPE3RC4nuhPHIEVDepCabgepZp5RYX07Y90mfwzunpuhR2mxE-t4I5XL0drbPMXAYPScPxDbbeicu51F4GSqn6Wzb6QiehgAYyNVO2mv8qfBXm6ZI7_FxvUtdgTS11gQuG2bDrhapnk_WW-E3rAr5iboAIWMEQaVSXVs9vZQWcM2QeYjT5fVW1q7dzMyzFnh88GPulRUw-plBle3n7PE7z4Iauie_jG2XKmDrGJi6zbjKSkbfXW4X7dXmh2-0YOvHomWteD8FZF1pA1DOo_YcRgbvWZXSxWcorB7j2TYBdkSoBhwPCgEUWiY2mwkvUXIbYKbq-gdqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=E6LKi0P4ARTO9yLJ1OK_G5190KvNfS6Kb5fRp56Fg6AWNpounoTvlDd67Vwf_cQqLRLPwCk0lULquxg6XrwKec1kAZPUMkdZDF0Pwrw_gTgJSlws1F3mYZoMD4iOIDEhoTgR8S8AIeVFs3ILJct4XOvmUdMn93bGC8HshK1r6YAWMeodM29OegnQnO0COVBQut0O54TZiUQ7BhNQedpyTk9Dd7hv-wT7InbaTm06AukKNaCVwczHyjFYQNbx-MavHQXgXicUlu4bOaiOvMYT-dH1zSDcm5xuMgR4HB_T54nT4Eex5ZWa1dhbf_nC7auSohSUoGBj76dWuWE_leIBoLNxFjeTX0C1tbLnrdSFINayZ_ZZtb_95QG1_M1qOg-w60eisyV6mhV3v3C-YQJvl1KS1bctFzTCRlYi7IJKVmuaENoWjj6Zuyec5__VxC5m3m8p-ZxGuNFsaa3lrYQPyWRtG3pqwsRoBFqnces_7QzyLYTyw1iSO8tDU0527qUxB3EX3iAIZoFqI36bT-_Zz1YCywmrYgy2f2_xVYHnHk3UNrkH-xsR54wf29CrhEiRcEEAqEoIdvUm1-p9x0mb0GS0slxIdEsWRGXy_lMJ27JuIJiYrfFkbsbCMzSlq37b2AqIf5kN62pLdKfrURB4hnihJ_76UZ7Evw5gLI-fV7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=e2DZR1gISX9m_ZUjeH7sz3ugPakAYt-vdsNrws2x0dNiKy9pORgKyxS39FPfrbqj3WMQa41sMsujtdeLfvlcAy_L_lMr8z3FVIdHCzdJBq5iBs0meAwlUpeoXrjvLYX0ZEDWrVFNJrYJBCUFNszEnCBRfqg0xAIps2f02Glg9btGJgxgrZub-WXFI7BbF9H_hL9sNZlOSBZn25Frb_IawuSBoczcZxkAfBizR3NL9sKQuKOmlQz7EGuUKSCFBd7Mx6CBTIwXE_FdDhHnruDST23WAaaOuffcPIcsO6kTsZFXacJiaXdtjTHlVR6whHzxFhi3vXSji71WwLXmAhs5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=LHH6ynFz_ilf12iVJya2kV8dwPjiR9GgKyCUspzU0A_PQr7Q62xSwxo-u3mURa-on_91k1R1GsB3fRJyC1VYysoJFRXQfDLHHtlMwev7GQ-9XvGuWyWV2wziI7Qp1gMDdCOVqxO9hA9eL2NWMiHk82kqYrIFP-G7zm98XzS5YixufwxiqMuhlRwZKzXigJ8hGbOCO1JPyQMmbDJv4zibpmrUCduDxj5iru73ulHZaaRPzR1D0brVAMmJ6jGv9YaN2xWxXYKFiODtVd6iK-az9AiHJQwIgJjjESl4aoPTXD8mtWmZGh1FTIKx7R0RJ1dESk4qxCKO4X8uOA1IeSDU_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqaPPRCVQtksZkDyjCQdbkCJ15gKpF5yC7JuQjgCy20Z8hwHPnSpMkBNzfHhzwc0RTb8DPRb1kpy3IZaQ9BfmvHhqjr9QLIJYJv3Y_lRO1pwd22OznSjO021CvnNPg4Xu0TNRzIH22oJAF2PzqJPXtSMCJkNIsXUUdEKgaQYazrEvNhXro97TzpdBL9WEMnfP6EegScJOXJL501FnGY7ZiSyYhtBrcRVeVizcJAcGrU6p7Bh7Tmifkb2vypPb9FZuk2XOsueZTNYD2DzVv1HKPFXns0-MOfqrCZQUiqHes_IE7BGszhn5ogdEYntnqqFzGR82jYwOt5oAxKMKXDVmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tx4R1crOPZpPcax6y651h4HF-OkIr-G4U6GP4UfJJ9Y3Cu31wNxcQnDZrFOzS3SkWQc0Ii_A-N6w17yH24jDcST0TNGSWPpr-ozFofy6OmM-9nXZNurJ9GFG_n-gTHBiGyPNxebpp6CX6toog-T17uJ6S7L22GEs7xD6kkLeUs9zc_hXcVyiHIw56d6-dXQJOHUFNuZ_zkiKAmcWy6is9TLXpIgWDvngXLunE6cHq8U52M9aF1E7h4BA7yfjgchbfxkoR_2b_bR2COymOkocqRzcXPSNIoWxiEDoMV0p-F799yl0-Yv7v0OeJkl6bTpXLWS9d9R5e3iRGEVLgiG9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=rG04TriBqzoKWTf3jQieAQwSnnfSBVC5y9AAMt0dxWAHYzkNplfylTMM1YdmDgGZu0Af3ry7jPkQLczXOgF4RVeTKaEMXLMSSI-_SNMp7_0_MPhVrpimSbo_ogOX0JNn7bIFudeHWZN62zAcqqZ0AbkqKzxC-8UPLISTKM4x1sdY1c4GUdRxRFOs6xgSSE3RT3hVnXMg_BDWD6POwLSJDxWN76roZib_j8CjiLiZHqy8pPWz2MfT-QLkUfUnyPZ90tz0VptaLYmylEA52Xom47hM374ETVh-DpQpAFnp8FiwTYGhyYNGjqNr0vvTdQZu0gO22dXJgwjTxQp8bzzsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl8WHFTvVx4Eq-b4xPo4gP-Fq43BksQkXGG8f7HogJwe6QG590uFVGeY-i_NIwkaI0hofHVgpWH0e2BZ0qOIhz1ZsjCHBKz4lrd5wEdvoflIALUy7lWw84ntFbZj9D-5ROFOthq5cwfNDuVoDcyBOiYaaif2EGGU-xQU6rckUGNz6OE9Wyb5SPUkhI5f4_Ur5RXAkcQ8jSHD7IcGYNeiBP8zi_kD-YoVVUQPfz8nLSrGUhLfwOk0mPz2DpDxaWMUzZqHISKjr1bXqCiEtdOOpTPfaiwJohG8UyX_JPejJ6UTBgYxDtnaibqm9M-xK9Fc37qJXF_0MqMB0dv-dcebUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gktjGordFIZ5dvmU07AIK9ChqdNnShWeeCd1PGWhVFCll6UppKkSKHnYJ2ZcMHxRdgEZMy-11gwmMT6bVNFDhwZju7fD7fsdXCLGlJlQitpgEqkz4WBEe_k0Qp9Wyg2n2ud1zvG7-yTlDkV1VacxBmTTSwm5F3GXsb4vJe5ghtGg3vyIYHpbqv-dG5Wxr4KrZyTOAcjglOixUbpF7MCyR07YKVQJQUH3Rrazl8RN6F2XPFwI_MJXyRExWSNYgpT0gpb4oVAclHxw0Ayhwerr0sbapnA6BmZvbCqsRryjhA4A3Zhs5o3TLIHXc2a30gpiXvp_m-q0bV9Ycpeg4K3fNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EGL2snDC_8SKE0fdV77Ze6wGuWxn5Ni6q_MrC3sRgNg6-mz4VKgeBXEBd20fSx9A2GL_mNbRugI7sENiQbdq1BPFeiavBf49XrldyyqusHZc0r7os1nVl8-rozfI72DISf-UmY9sjB8Nq1RZI-ipwRYyHY7htZvTKHp-xfjLMHOVbXw42XUN3lvjSQmLDYXeP3sjKhoti-5SeEZ132P6r0dZ-ofefXVInWG7x7wlb9D8aEFdX0CGCriYZHXtSspnWanK1pEE6ETQUy1sgMAJNfaIN3CEv38eM9zJ3ls1gRyDagwdgVaDlGg5CV0f7ZW32-j1cN_XYt92DhNzNc43Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQC3VmP_LD8GZU_c2Ev4f5IUTzmYvdzDD_2cCRtax_75hQ9rXjre3oLvikaOR0xy95LXm3IOlWs449-S9JYEZd7KlKsKbDh1oJHpkt0lNWfNcphPPBnkYkfhea57Uc4NnfrbX1YW4GU0iDdkvAWhJfGCPBPYTs9GuLfWnFrIpRfbJGqIl3Tc96NYE22ZObyw_hfbZZ08nZfu0OXbe6v87jNbSlkzhraXv3fwF2hrO2jj2-1wIZpsuw3lPgEdkHXHuzw2x6kMOkPKM69RM6aAp0cMqRcLl7qA3AuVQ--tKdE336mQAvNivXJoKwSf_Svlel7jN0bCoO1fg2pyae2ZNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDwVJDVbQkug5AXhm392jWwZ4hFVDBA3DRVPbuTyjtHhc11_cV5RfrBxAea5mTJHVcEjc6J0rHS1bPkgjiDHN0UaJ5dlcHICsOYH4l2o_BFnxqRaaXMiS0xR24zVTPrTF7WxTvhfLppUjh9K_K_ESMItItkN2aEDkmZUX1VzIK8CrWPuPdhyWjH_E2SqA0fpA-aQhbL-J5pqaEj7veO9tobdSKb2ALVRPhURiEB3ZGj2qzsPi1KUhZLToFuc950eDCnP-_FqG4QMltXazrbXypXOhGgmPtoC_yaEJowc2Wok7JonsfiHMBslbQgb098QYED_B5664gatYgFw__vZXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=JMBpXedzT1Raum6ralaBlWjodaKRZ72eJKJxNcm7VNb1eDuBE4LXb2wXmdYnQnei_m9wIdqyakygIiyGLChUpUEUdoOMR8WXveXbyHmFVcci0J8orFds1iXNC8A5dZi-98W71TVkPH_Ts20FvNaykm5hfXjM01DAGbNnMuZXFqFr6tS0JX6BpWso8x_8eAhHQLU447qTijN7_joX2TY9W4kZ7xgYIySHMIMaOZ-5uUpeVqtg-bgUeA6a2BjTW0aecyJNpMOR6Gf0Z3SEvJ3bSKCRfzsGob9UnRPtEzAw8lrPka-dr0sStnhO8vWfse7EDrMg7guWvt0vI5CUmBYlzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=JMBpXedzT1Raum6ralaBlWjodaKRZ72eJKJxNcm7VNb1eDuBE4LXb2wXmdYnQnei_m9wIdqyakygIiyGLChUpUEUdoOMR8WXveXbyHmFVcci0J8orFds1iXNC8A5dZi-98W71TVkPH_Ts20FvNaykm5hfXjM01DAGbNnMuZXFqFr6tS0JX6BpWso8x_8eAhHQLU447qTijN7_joX2TY9W4kZ7xgYIySHMIMaOZ-5uUpeVqtg-bgUeA6a2BjTW0aecyJNpMOR6Gf0Z3SEvJ3bSKCRfzsGob9UnRPtEzAw8lrPka-dr0sStnhO8vWfse7EDrMg7guWvt0vI5CUmBYlzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=h8uy6xEJH-Ob0Hy50DAi8mtUe8NIVzol2MvVWjgDzq_YqV_TAqFZMG_sHprR6USObBgorCdGghg04BV1jnn5idySHZRRpa6Tnqz6u2UXzJpM7eNe58lCsHtkiYcCJ3YKW0PZtA4uW1OE1bpcw7-cGK000jVLjRFrNEL4CSBXAdPSw4rqVHMDSARQ0H3RJZcHomKdIGKa0IF4OLdAmEcP60LAOh4iCW-pQDOBE9DtI90mkTfm8ub97HncWTJYhq7O4LrIZrt7F6IKfoQf9njJnbUPtkEi4WaPcUoXcz0xuiPKx6yOLbOd9EtjLc18B-u_rTSha-ccWNua1wodh3gpVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=h8uy6xEJH-Ob0Hy50DAi8mtUe8NIVzol2MvVWjgDzq_YqV_TAqFZMG_sHprR6USObBgorCdGghg04BV1jnn5idySHZRRpa6Tnqz6u2UXzJpM7eNe58lCsHtkiYcCJ3YKW0PZtA4uW1OE1bpcw7-cGK000jVLjRFrNEL4CSBXAdPSw4rqVHMDSARQ0H3RJZcHomKdIGKa0IF4OLdAmEcP60LAOh4iCW-pQDOBE9DtI90mkTfm8ub97HncWTJYhq7O4LrIZrt7F6IKfoQf9njJnbUPtkEi4WaPcUoXcz0xuiPKx6yOLbOd9EtjLc18B-u_rTSha-ccWNua1wodh3gpVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=OTTXMsf3uEHnFtUURRrdf5TB2gBwn09ygNyJvd_yRn3cVQa1JywlVIeifp8N6giQWHYcGn_hLZFUQaYsmFqTPXWqfJARKBBFZbTvf8UsZr8EVHnGIICqHrbCHrRnX3omMjK6C35OlkVCjwUERFBGKRM-IxKdJ4RUzeVFDRARJQaX7AcQ7SUZ3Zsjj2aLMIHNag6aZzyT74NWdYCzG6noO3JcS0ZHywud4_8FGCo-wayAd2_xbdu2-kwTpc_M5GV9YrTwjpNxdt4wa5GV8eNm8UDG-u2SerOrr9LQwDGsN82xElXkwLA-8-9oD7LSl6KjhQxETx_hiG5jpz4YQ46Bwyt9VNb_pyZu2AqERJeuCjfKkCn1UGUn2YawyuTdHr-pgUqAewGg4TqZwOQ9rnN0FQTCNN5kX-1c4046LlFMTpDP0O5kAKEQ5Tf8fqgZu7QMZ9cXGIEDVZvufLTdzIwfzlklfuPLjTukm1ZSP766-aBUoLqOXnHd7eebz5haYDx75LeAZ6bu4tewtQz4wUkphwufH0Pg1aOPDJ8IHH-CeeXYOvsSoaUnyRPcswjE_9vNrK7GnZEHaDVH7unmg0u7vwp3FEacEA4HAh3D5Pv-kF-eSWK-88AR3f8kJsIe01KWuBwmQKwwW27iVVBNYfJqVHUWiPzbwyi_fItTSQtZS4M" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=OTTXMsf3uEHnFtUURRrdf5TB2gBwn09ygNyJvd_yRn3cVQa1JywlVIeifp8N6giQWHYcGn_hLZFUQaYsmFqTPXWqfJARKBBFZbTvf8UsZr8EVHnGIICqHrbCHrRnX3omMjK6C35OlkVCjwUERFBGKRM-IxKdJ4RUzeVFDRARJQaX7AcQ7SUZ3Zsjj2aLMIHNag6aZzyT74NWdYCzG6noO3JcS0ZHywud4_8FGCo-wayAd2_xbdu2-kwTpc_M5GV9YrTwjpNxdt4wa5GV8eNm8UDG-u2SerOrr9LQwDGsN82xElXkwLA-8-9oD7LSl6KjhQxETx_hiG5jpz4YQ46Bwyt9VNb_pyZu2AqERJeuCjfKkCn1UGUn2YawyuTdHr-pgUqAewGg4TqZwOQ9rnN0FQTCNN5kX-1c4046LlFMTpDP0O5kAKEQ5Tf8fqgZu7QMZ9cXGIEDVZvufLTdzIwfzlklfuPLjTukm1ZSP766-aBUoLqOXnHd7eebz5haYDx75LeAZ6bu4tewtQz4wUkphwufH0Pg1aOPDJ8IHH-CeeXYOvsSoaUnyRPcswjE_9vNrK7GnZEHaDVH7unmg0u7vwp3FEacEA4HAh3D5Pv-kF-eSWK-88AR3f8kJsIe01KWuBwmQKwwW27iVVBNYfJqVHUWiPzbwyi_fItTSQtZS4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=vcTrgnrJxQv9m8CrPWE5k7Uq_-aBUn8lcFBl7qvcM69kBchXNNFwS4i-Eicf5h6Q6e3jIsIqzj-ENRP9NlXJElWMpKPAiBOdngZ6jayGEU0ds8q7iJF7umtjA2ixXI4l45d7Dbv_F9--Jm0rKVQR5wBOrtrSdlclybboo4xBF3zO6ljdUvEn3G_PzapJk6rbUz2w7GKLwDBE9m4l4tToF7zYyGjuKkvIX18gcZ8ciTVf5jcm1KfQs2wrpUCVGq0TOFnEPB6mqj1Vup4r98gzcP3jxPuKf5Daie9vkxS_N6LIHckYsT5EfQDOzCeNoVlVn0UOvrekDuHJ9zyFrGpsL6S9N3DRy-DYbi4fKBMO-8DMxnkZ6Uyy0eiWXgzX2vRh9clI4q3b4OoVoVDWS1L8P6wtzRGv7gK_wXa6P8d6hUCstMdODuCTacKq17pSZAx_r_CG4DdWtG3YHuKhzg2rgELMG6vlKVGFbQA8l3l7H0sLcwztBsiVk07YKvwp0Ts3_uQCFrd2YDh1guS5Bu37XjoQdvS0iTBTwoY2cuWjduqjiRXOmDs-GF5SKHJeX24R10PfRbc3rD9nDFniz8hZ-c5V5pi3qybmJrSLWC0ss5flznzBGHHhvxOWsaP2oTE7RQDqrZxsu79kl7hyFPgFI-7iOL1aRpxEjAeq1JZa8v0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=vcTrgnrJxQv9m8CrPWE5k7Uq_-aBUn8lcFBl7qvcM69kBchXNNFwS4i-Eicf5h6Q6e3jIsIqzj-ENRP9NlXJElWMpKPAiBOdngZ6jayGEU0ds8q7iJF7umtjA2ixXI4l45d7Dbv_F9--Jm0rKVQR5wBOrtrSdlclybboo4xBF3zO6ljdUvEn3G_PzapJk6rbUz2w7GKLwDBE9m4l4tToF7zYyGjuKkvIX18gcZ8ciTVf5jcm1KfQs2wrpUCVGq0TOFnEPB6mqj1Vup4r98gzcP3jxPuKf5Daie9vkxS_N6LIHckYsT5EfQDOzCeNoVlVn0UOvrekDuHJ9zyFrGpsL6S9N3DRy-DYbi4fKBMO-8DMxnkZ6Uyy0eiWXgzX2vRh9clI4q3b4OoVoVDWS1L8P6wtzRGv7gK_wXa6P8d6hUCstMdODuCTacKq17pSZAx_r_CG4DdWtG3YHuKhzg2rgELMG6vlKVGFbQA8l3l7H0sLcwztBsiVk07YKvwp0Ts3_uQCFrd2YDh1guS5Bu37XjoQdvS0iTBTwoY2cuWjduqjiRXOmDs-GF5SKHJeX24R10PfRbc3rD9nDFniz8hZ-c5V5pi3qybmJrSLWC0ss5flznzBGHHhvxOWsaP2oTE7RQDqrZxsu79kl7hyFPgFI-7iOL1aRpxEjAeq1JZa8v0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=Zht7nMWVOrxGzI_JcoVG9q8tWjpp15TEzjjSVYwQ5agz--kbZ-Ir-MaC3o7tZfroRa-uEycxOGuGTrhZ_-4yr38txVyEGdpITkEgybk38s1jR3P8zkV0L-_VpncqYueswP5KJZmyVqVf_6QTZo3KUvZWv_aOgB9wsPmB8iBPeV5t7Yrk0-ZWhGIC7lmdEOsaMA8iShbZZuSzWqS6wuywBOdPrEH-_SaSCK7oI7F_BuEpcMjhSYIqej8ToYGVVi3xc_Zkkeebse37KfkednoM-9vLR5osHv6tNO6ab6eAvi9H2tuJLBfSySt92Pd2IM0vNbj29_73rh1-4xC1Vi8Iiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=Zht7nMWVOrxGzI_JcoVG9q8tWjpp15TEzjjSVYwQ5agz--kbZ-Ir-MaC3o7tZfroRa-uEycxOGuGTrhZ_-4yr38txVyEGdpITkEgybk38s1jR3P8zkV0L-_VpncqYueswP5KJZmyVqVf_6QTZo3KUvZWv_aOgB9wsPmB8iBPeV5t7Yrk0-ZWhGIC7lmdEOsaMA8iShbZZuSzWqS6wuywBOdPrEH-_SaSCK7oI7F_BuEpcMjhSYIqej8ToYGVVi3xc_Zkkeebse37KfkednoM-9vLR5osHv6tNO6ab6eAvi9H2tuJLBfSySt92Pd2IM0vNbj29_73rh1-4xC1Vi8Iiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9_j9HNOv_c-qy5kZVOi2aFwjPLf6sr1p6aJ66cptG0R-feUjjomprXas2neXLOhAxHtohdtbM_JFouVRiUpZtRq2jVXqY-6q6Lnkl7MCGL4kVghQrun5edlGK13lzE90y6rE0XfVHanNTY5qSMEDysY7iIl6ZthkbRfIBy7JZwb2sCjLPcdBbfwVzFqMCE0OIDGZJ1tLTZ5lfltvXMcaTNiNt9rr6zcDEmC3K7cTqj70-IONhAh36iGGRKCrXxYoCkOtZMdRfcYK3ex_tNN6wXMhkPDBHjk377Bb9cLSiHA4Gs1bIhikE191QBtW5SCUPXLts8BDsBbeuAF761jrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=shqtu0cW4IfL4baiyRtwnrlIn3YeHctYIyjE80Ach1GQKo0mmPZYBGrdJ3wRq70-nG7JpyKmzsCS-_cz7uOd2JCX3Hj-7XI9RpHwRqMZHN_Y81CP_CfJBHSIwsE-IDxhiqDjOZTBiDVHJ1yhbR_E1GvhocmdvK0M0mK4Br5MHU64U_2uQHSvoSkVDBwkmnvxjPS_10Xw7GFkV535lG9_0tTxY8GHEzhhLvRVdcSTl3ypExCcB6vagSmUyJAJIX3pf4m1MZSKvxgI-QN97RKyBjhAk3vvp_Vaq0myZRWHxGdFmoHdOUlLI-Z8SHI7QAs7fmUnsBkrhXsFYdyB5wcI7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=shqtu0cW4IfL4baiyRtwnrlIn3YeHctYIyjE80Ach1GQKo0mmPZYBGrdJ3wRq70-nG7JpyKmzsCS-_cz7uOd2JCX3Hj-7XI9RpHwRqMZHN_Y81CP_CfJBHSIwsE-IDxhiqDjOZTBiDVHJ1yhbR_E1GvhocmdvK0M0mK4Br5MHU64U_2uQHSvoSkVDBwkmnvxjPS_10Xw7GFkV535lG9_0tTxY8GHEzhhLvRVdcSTl3ypExCcB6vagSmUyJAJIX3pf4m1MZSKvxgI-QN97RKyBjhAk3vvp_Vaq0myZRWHxGdFmoHdOUlLI-Z8SHI7QAs7fmUnsBkrhXsFYdyB5wcI7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ8DrSgWnEBnY3kKvdWksKOSFKCJpYoY0fc2S64E12XKgc00MXZZtNjZqcIzsdeLDShmKPnGHq2Qh-JPRrbUMnLVGlmV2dddz3AgDIEm7FsKbpJrGU8Scb_FOIxl2IVLUFYd9tRIES-fqRN8rhD6dRsEjy5Jeeh76omBYDRCWs476iJLu8tEilZS7muleXh4gDXUYUqPGsDPhWL3wwiZj002XPt8cHLE07BiCnMhHYHDXKRU1wE_vPzT7aOiC5aDXUuKqXh2rMVL-ISjkvrze40VdiFwC7XJ70tRxXIp9fTculaKILYeI3muP73M5Y1sRbOHbLhccpADFvfphsuPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=jXUF6AW_Tim2kVDP41_W8ldoZzOo5YvYlmeT9pP4L_cNP-IAAx6nr5MCIVCcJqnf6-e7M3kJvQy32NeYdCKuG6iaRhVvy3Cc5QtoN8QweXWWVYQH5yrbcHwfK1dE8gO4JyXeNVLoZPGUxvTbhJbYHoqknE25mciUvbX0I64-4YKm5LalJophBUjkq3a0wQ-0UG3YkBYFqgPsxXfyjF7jogcs2FVFNZ5n9n-x3u7RTnnKIJBfRcSgoB6GE8JZe4dh2wUcXvaCKMUqCGJ6Fg5lNGxQP9Wj2pnmXETljBeVvS5rm8rR5uLJ5KqhTEU2yOSQOPoS6C72wUkVmBi-5dXcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=jXUF6AW_Tim2kVDP41_W8ldoZzOo5YvYlmeT9pP4L_cNP-IAAx6nr5MCIVCcJqnf6-e7M3kJvQy32NeYdCKuG6iaRhVvy3Cc5QtoN8QweXWWVYQH5yrbcHwfK1dE8gO4JyXeNVLoZPGUxvTbhJbYHoqknE25mciUvbX0I64-4YKm5LalJophBUjkq3a0wQ-0UG3YkBYFqgPsxXfyjF7jogcs2FVFNZ5n9n-x3u7RTnnKIJBfRcSgoB6GE8JZe4dh2wUcXvaCKMUqCGJ6Fg5lNGxQP9Wj2pnmXETljBeVvS5rm8rR5uLJ5KqhTEU2yOSQOPoS6C72wUkVmBi-5dXcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=P2CHM4ja_hb22cG85x0hwWDEyoBo-s6ST6p8Mx3yXJG7dnHGZlGpKMd2Rb7N_HmHpGFw5vnODiTyB4qk89IuyseKhsa9S4xjR6mecYhtEduNFUiP-gOm-ATra2EbblPSpAbR6xsrg3Q04Qm-ANdmn2Qb5xo3TB6Z0dIWXZj74eUMpRXvwr4RclYiNGiKrkcvZ0Ms3k_Y1mq_oK5CvTA6wdr__MP3ehCnq3qWEMneT5yMmcuUhIFzfy2yAp0CqUTcwIanCeO63YDzzQ7xMvS9XVmWqXXsCjmPH8E8zckxJXRQcpWspyc44JXmsdQa3aMsGVT3bQvuff-ADh2dotozIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=P2CHM4ja_hb22cG85x0hwWDEyoBo-s6ST6p8Mx3yXJG7dnHGZlGpKMd2Rb7N_HmHpGFw5vnODiTyB4qk89IuyseKhsa9S4xjR6mecYhtEduNFUiP-gOm-ATra2EbblPSpAbR6xsrg3Q04Qm-ANdmn2Qb5xo3TB6Z0dIWXZj74eUMpRXvwr4RclYiNGiKrkcvZ0Ms3k_Y1mq_oK5CvTA6wdr__MP3ehCnq3qWEMneT5yMmcuUhIFzfy2yAp0CqUTcwIanCeO63YDzzQ7xMvS9XVmWqXXsCjmPH8E8zckxJXRQcpWspyc44JXmsdQa3aMsGVT3bQvuff-ADh2dotozIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eV5JtZjiiMtt5kskBEd8rkU-Lse2f9pAwW1zYfwrBxkdOZWDBHRApHxNerhIfNePmL29CzlsAAGcr837yCSWHzunuAL5IgcY2NzmRYEZGud4lloePcDVf2WUxduv-gMLk8LTnPlCfAeRk_qosNXtgPmZedSfvd-SUuoEOc0ztHxGsYMx-zQMfFYc3jAqBWURbASwvuPzWNWY5TB79n3HUryV1zgiJRkgcxitF9ux-MMlwb67F2tS0F_Igb1-pzXwjmS0pKL6XeZzN0dlBnpXxZvMWiolJ7SI6OQLsR6_fdYaG3WQU70rvcluxYLI0DfgDZsWEft38pbEjG_W36p-9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oJ90ojCvOsf7qQF5LTxzs0cMqxyZNqqmB-JFS8KTpIh8L7qwg0YrAeUh61qZMEV8AlmW2Ct1oSWYJCUkGY-Uo72yG37uEFji683niZVCpd1lRuMSviW3Xw3LD5srKRX8aTrl-CgbH4Sl3fXN4VCJa3GbV5HnodslMxFnhGt3fQEGFlJCyOHrN_4IAJwuC0a6rGpnj-t2-mkPRVkEq-Y2-nXJ233YY_FFcCBoPu5Mwa4cEKy1Z3JUc9wc3OfyBFZYvyKg4DexjSBuxuhjubqPHFJ9eJdbtr3vgLFUPmMTtw9aeBiC4kD7HzW1H9L7XVJalhAP138gPxK8ceHHSgacGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=oJ90ojCvOsf7qQF5LTxzs0cMqxyZNqqmB-JFS8KTpIh8L7qwg0YrAeUh61qZMEV8AlmW2Ct1oSWYJCUkGY-Uo72yG37uEFji683niZVCpd1lRuMSviW3Xw3LD5srKRX8aTrl-CgbH4Sl3fXN4VCJa3GbV5HnodslMxFnhGt3fQEGFlJCyOHrN_4IAJwuC0a6rGpnj-t2-mkPRVkEq-Y2-nXJ233YY_FFcCBoPu5Mwa4cEKy1Z3JUc9wc3OfyBFZYvyKg4DexjSBuxuhjubqPHFJ9eJdbtr3vgLFUPmMTtw9aeBiC4kD7HzW1H9L7XVJalhAP138gPxK8ceHHSgacGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=THAXCHX8Ss5qcXWHEISn-VR0LtW6Gh_NhHtEs-qtYY3XOXTNddBCf0FwGAG4uIXEIU0EwtpQlGdla4Ky5KWloQwtE0BTLDEG5WlfsZEoq4S0Xvc3eeXwD2e3BoRYU0P3uRqYLcFNuDNbXG4q9H7G54JMr9PPLAfryC2prYC64q7o8mC3N5j8N3N00UZ3eEMbKhVmjDKxpO-QQke8zsgUlg8QWS9jI7SNQUA6ucX_mkZiOxzzPwvyUCx3dPCXEG2q5exRYYYHGJKzR_lp-4g74SxgTBEFF0_E4V23_UkB9qDsA7oZ_Jekmhrki-3n-bqS26HS1nC65TkghIaN8ETQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=THAXCHX8Ss5qcXWHEISn-VR0LtW6Gh_NhHtEs-qtYY3XOXTNddBCf0FwGAG4uIXEIU0EwtpQlGdla4Ky5KWloQwtE0BTLDEG5WlfsZEoq4S0Xvc3eeXwD2e3BoRYU0P3uRqYLcFNuDNbXG4q9H7G54JMr9PPLAfryC2prYC64q7o8mC3N5j8N3N00UZ3eEMbKhVmjDKxpO-QQke8zsgUlg8QWS9jI7SNQUA6ucX_mkZiOxzzPwvyUCx3dPCXEG2q5exRYYYHGJKzR_lp-4g74SxgTBEFF0_E4V23_UkB9qDsA7oZ_Jekmhrki-3n-bqS26HS1nC65TkghIaN8ETQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9Pl4aYF7ll96BbtIZ9g9CxfchwNsMF35BhJvB_aXoc9dtdOX_H1RWzFDnw7_1a7mDOJWry6UdiPEo8pu0m6NYZA9ku6TlqzFeOzi68voweCUucARuJR409-c1GwiXsVrFjqt0bHIb5omEaENofAdQ19iQjIVLHTGSIXwkaINgEjYKigQ1KdRIU3AIUU9lP-aea6rb46AhMLxshP4HNmxTxzf-F7G5wyVg0KTVE1IL2_-FFF9690Jrb7EU8JK_g-uG2WyxvhNyyDrAB3C5neDzM3VBJr0ijMiNUS9mAfanf1gu9d9nlKr95TocfIxZW7R_oh4X7UYdkv0zpb4Xqq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7ddVY7ZJdLy8RcgZlFpRtWDrmAd7cnsQdQqL0YNkaI1mkOI1B6FOYls0gluCL4prOWooWO6rQxeo6doeEMetYqKRY3N58JWxvnCjZeOlBzoTKfjo9QlfniyYS2yQcDQ8PYnCdzMpthmDLSRmJBstPS4lEFgUI7sMA3xngSZFgxm80ajRtXtc1MIFjQiD8EKpay01KW873lVdSVXlETE09S2nKBu_vG8oYjYyXYVhv-ilkqC-3JmrukMPQ3xPYSljMZoAOxrM6gMzbx95Vbra98yKQmGQh77Ifxkdhl8Jku1pcVqwbWQZ7VeSDGNYjGr7MQcOD_ayDZi-2ZwQ5xcWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyNIA0BfKZJVCHdaTPfESDXW3JQHco-xSE31c208dfpDFH-mpusZB1WwrabQH7fF3toJDN5CAONWjgrNcfPKlmvhttqaUI6-iKXJlPJlV26Lk4OWIvp6zyUbeC7RPAPILIMgWmxOx6e5r77gYwHIktvzzsXa1QEXnBdQ3NNdaQ9cAQyyHQZypfE_FZBDgqtEHNCtJGWCX8QrqSfX1GWayhbriUb7bzBwqHd4ec-FGaazSyFFaRlfcAfAENqTrF2gmDFy95ft7latYBdsPj86vFi86DFkefUqmwVzqUI7X_8OlUS-RuiJ48EBe9GD0K8_nWD1VXHL_m2iSNZLUWKnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4O2mw44KvKrr9y3FKZhD0YzN8dogNJhMAZNpp7IjFB3bUpgkzrs6da3PWvnlhr62Adwk4Uq_k79y6lYjF0lDXrsWJbKQxCeSLloSIO5xv8pyRJyJa5SNFN1IOFL-HtvaJ9eNJK14xVc_oEuKLuE2S5wZ-mGjXThqsVqYKxOSneATMndqHgk6hvPm12rmhmq9KhQ4JAwZOEuN1GNh0I_KBRi_Yo9X5yPcLDJXKwMDr61jcHmBPFvk26pFfRt9nJ6o4cmelG7XuzHLCMo4h1ysCvVVn2SX7Rwd8MFjxXNAO5WnttG_0LPpmM3BhGnbbiBHkSo6uhd6pli2mUiqW5fpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=pjPEOrC-E20Hbxh2SzQS3qs5MOCXdVMdIDYawUg97VpoipWXbQiaTnjsU0swd_AKMERvi7ZD19MABKh9p7d_ejbrlNKYvHrJ3XuiA3aJ47E7-782AfdnEs4bTiCsxbyHtrLT9HZucVA-D5gCtzLvD0SqxmnVdkU-rxEBheCy43jlLFkrp6hlg0CiRlxOx7CJOSrM7SpGFtLsP3yGZdDY5O9jN4julF0-VeNKEa9YUudbyTFz8VrXLgP7IivJwhQnOitB9bbnn3QE7r_VvOJszkgL5ehSWb_h_U9x920SiErm4XbjNVAOpLRxVPx0eqZPXMXLNmL3Gj1B5XLH0ApuVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=pjPEOrC-E20Hbxh2SzQS3qs5MOCXdVMdIDYawUg97VpoipWXbQiaTnjsU0swd_AKMERvi7ZD19MABKh9p7d_ejbrlNKYvHrJ3XuiA3aJ47E7-782AfdnEs4bTiCsxbyHtrLT9HZucVA-D5gCtzLvD0SqxmnVdkU-rxEBheCy43jlLFkrp6hlg0CiRlxOx7CJOSrM7SpGFtLsP3yGZdDY5O9jN4julF0-VeNKEa9YUudbyTFz8VrXLgP7IivJwhQnOitB9bbnn3QE7r_VvOJszkgL5ehSWb_h_U9x920SiErm4XbjNVAOpLRxVPx0eqZPXMXLNmL3Gj1B5XLH0ApuVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=Bb0pzqg7jaNU7qcokUNSUwUx0NU8h7DN6UXkchcbCDnW_g3cMgSdRhCwVhDdsi5spzB5lXE4Cx-VC14JjZAcHSo942cj0NQM4yZnMV0Ux2f4j4YJj88fPPBfPIpX0G_GAI9mEMqzTUzGrkVJh8ubKMzA9qZFqYIrdCLsI1ezyPqjCReBOSnd9OMMYHJAZ8aHivRWEtv6BiRNCWOI-3Y0mFi3BxS-jaaM3w6yZnR3J5Di7MI4LNqmT4WMp5yySB9SHpYui5BHsdYpPywvMKqLxA75AYY0YH6NxGtU5wsf6PazN5w5DszzvS5BbiWNYn4xLAGOyAYSUHWKsPXQYnBcBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=Bb0pzqg7jaNU7qcokUNSUwUx0NU8h7DN6UXkchcbCDnW_g3cMgSdRhCwVhDdsi5spzB5lXE4Cx-VC14JjZAcHSo942cj0NQM4yZnMV0Ux2f4j4YJj88fPPBfPIpX0G_GAI9mEMqzTUzGrkVJh8ubKMzA9qZFqYIrdCLsI1ezyPqjCReBOSnd9OMMYHJAZ8aHivRWEtv6BiRNCWOI-3Y0mFi3BxS-jaaM3w6yZnR3J5Di7MI4LNqmT4WMp5yySB9SHpYui5BHsdYpPywvMKqLxA75AYY0YH6NxGtU5wsf6PazN5w5DszzvS5BbiWNYn4xLAGOyAYSUHWKsPXQYnBcBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=HCnbcJ4uqycU6o9YEzz4_LKqyqNvE7ggyeVNaLxZtqyPaXX6wKnpW0p6pgXR98-9ABkwajRGgBO1RbcwK4DMF7mbwnOs0Y8rdfG0wPrHdJkbPrrrNzcp0yfAH-So52OhyD-FOlqmnAzGkzO-k4SJYLE82-WeuoSsrdb0IRx4zoiccDnB-afeIk6vGnImHsX7drY7LLUTBQIo8WPyQlnyPZRWlcdm43e3lOta6XHGuyo_7YOdtFEt-PaI8RFY7YHIIw_L1d4MuSFcPC3n5JZUiYj5_9vr-QtWZdukXTVEzv-0JgGqx_VjmU-wpq7-CUcHXWun83gFaXi0JTQhYxRmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=HCnbcJ4uqycU6o9YEzz4_LKqyqNvE7ggyeVNaLxZtqyPaXX6wKnpW0p6pgXR98-9ABkwajRGgBO1RbcwK4DMF7mbwnOs0Y8rdfG0wPrHdJkbPrrrNzcp0yfAH-So52OhyD-FOlqmnAzGkzO-k4SJYLE82-WeuoSsrdb0IRx4zoiccDnB-afeIk6vGnImHsX7drY7LLUTBQIo8WPyQlnyPZRWlcdm43e3lOta6XHGuyo_7YOdtFEt-PaI8RFY7YHIIw_L1d4MuSFcPC3n5JZUiYj5_9vr-QtWZdukXTVEzv-0JgGqx_VjmU-wpq7-CUcHXWun83gFaXi0JTQhYxRmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T7jFCGxqemU30TfobPChWCA27Dw_C3fFrOQo47J2U6XszILtLbPC9F0T-Ro-c98P6oS7j8rz2S1_9XYP3i86UHC1vH7jIkrGs1goztiX02EdBFrP9CLHksQtABFnAGo3RQfOph8AvMTHQ7ZiDRCP88YDUjIkcJGU1YH8sU_gr8Y5o1FT3KEkvGkm_RHjPtP7ftV6wjmkZEl1J3fcMA1vjyhIFiEKGGphmGjTW9bw15ppMm9rVL5fmTPi77uFwlRFePiMEoz0Z-LKDlhUAGJgmRvr4qf6dDdDEDL1-oEC8_8_LCWaEDh6izsdkEWJzQf3zo5H0kqQhNMU10A6a7mH7dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T7jFCGxqemU30TfobPChWCA27Dw_C3fFrOQo47J2U6XszILtLbPC9F0T-Ro-c98P6oS7j8rz2S1_9XYP3i86UHC1vH7jIkrGs1goztiX02EdBFrP9CLHksQtABFnAGo3RQfOph8AvMTHQ7ZiDRCP88YDUjIkcJGU1YH8sU_gr8Y5o1FT3KEkvGkm_RHjPtP7ftV6wjmkZEl1J3fcMA1vjyhIFiEKGGphmGjTW9bw15ppMm9rVL5fmTPi77uFwlRFePiMEoz0Z-LKDlhUAGJgmRvr4qf6dDdDEDL1-oEC8_8_LCWaEDh6izsdkEWJzQf3zo5H0kqQhNMU10A6a7mH7dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=WG0L5My4d2aiYQIj7ZOZicyJEKzbQu8SsHcuDx_7fY3e10YQ7onLHCbKLK-6ZwZvwZsQojTf3wizwi6KjozrEUVePxCA0GS6eDkk-braZz35ToMZ3frW3pccYxWhsN6Cv7-QRaoiCdE6Ha2m5LZZnIqXMsOze53E8n_weTHFAcpvraVH72RodzO00RByn9f66Fk5ugK0vSwzFS8bgtEqXH7haJCUWGxkJrPvcTMrppY3kzvdmWpZZmD9rRjOpSRyBMNFAnwhd98JDoxaa03Hay-DpFIJQGWICt697IruJQciwRDlvhlEq-aMeKtCj6xQ8NpX7r55zYT5nneersfIODsInEvhVDMlGI2bUI5YUaTtxrIXLy43V89OzuBF0-ZG_6zcFUHCbbjnzGUH81GT25eQ2j0WUELNodBnTE-SHlXAf2vPkWv5r5y1S_N6E-i9AbbWnqqQkMkil8zJi_ehmYRJaMJsPkUtFoU9XTRy-YBBCdX_A48G0toxdMO00XCJ8k-tUG4yHg0V5I11_kxEkRWaZIPVUEP57GZVV-Wr9FpZDOjeGePJfZ4xjjmKz3kPn4MiHQnK6FdvXTxdj5CJ0M8T_SNRxmZea6IIKQ7BQuPp1pJBl55n7ShChZPJwhyR1h-ei5FrAFfIPfRd7EVKouLLqfuQEVtUJp4MXWeoo0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=WG0L5My4d2aiYQIj7ZOZicyJEKzbQu8SsHcuDx_7fY3e10YQ7onLHCbKLK-6ZwZvwZsQojTf3wizwi6KjozrEUVePxCA0GS6eDkk-braZz35ToMZ3frW3pccYxWhsN6Cv7-QRaoiCdE6Ha2m5LZZnIqXMsOze53E8n_weTHFAcpvraVH72RodzO00RByn9f66Fk5ugK0vSwzFS8bgtEqXH7haJCUWGxkJrPvcTMrppY3kzvdmWpZZmD9rRjOpSRyBMNFAnwhd98JDoxaa03Hay-DpFIJQGWICt697IruJQciwRDlvhlEq-aMeKtCj6xQ8NpX7r55zYT5nneersfIODsInEvhVDMlGI2bUI5YUaTtxrIXLy43V89OzuBF0-ZG_6zcFUHCbbjnzGUH81GT25eQ2j0WUELNodBnTE-SHlXAf2vPkWv5r5y1S_N6E-i9AbbWnqqQkMkil8zJi_ehmYRJaMJsPkUtFoU9XTRy-YBBCdX_A48G0toxdMO00XCJ8k-tUG4yHg0V5I11_kxEkRWaZIPVUEP57GZVV-Wr9FpZDOjeGePJfZ4xjjmKz3kPn4MiHQnK6FdvXTxdj5CJ0M8T_SNRxmZea6IIKQ7BQuPp1pJBl55n7ShChZPJwhyR1h-ei5FrAFfIPfRd7EVKouLLqfuQEVtUJp4MXWeoo0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=D-QKgXCx6H4YhVzq9E0eddyVIO8mEAbPVFiFHNmVlOsfp_8_96g7bTvw-4Jefwx-3Nv_0cJCfrdqhSGtvir0NWGMBEkVGcr5R0zVpYtfuVYxcniGLJ2fOrAJijxh5UAHA3jfHk8RyYurTyPcwztPb0Z57PU_Cw8HF-if84ldFV_TFdPVQ8WpBQKL0hLPdNd1WgBA9YTY0Oq-JQpy_ZC1WNUdONB0ZcAv3zHfawE9F944_2PTQ8sgzBpXYGjmnBCT57LwUIGomLlxPOM0fW1n9L_-JVUAZu6wOiogWOdmuDpp729vu9fB8-DguFwZ8rPpY7APLmLyddDKtdezBTgO3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=D-QKgXCx6H4YhVzq9E0eddyVIO8mEAbPVFiFHNmVlOsfp_8_96g7bTvw-4Jefwx-3Nv_0cJCfrdqhSGtvir0NWGMBEkVGcr5R0zVpYtfuVYxcniGLJ2fOrAJijxh5UAHA3jfHk8RyYurTyPcwztPb0Z57PU_Cw8HF-if84ldFV_TFdPVQ8WpBQKL0hLPdNd1WgBA9YTY0Oq-JQpy_ZC1WNUdONB0ZcAv3zHfawE9F944_2PTQ8sgzBpXYGjmnBCT57LwUIGomLlxPOM0fW1n9L_-JVUAZu6wOiogWOdmuDpp729vu9fB8-DguFwZ8rPpY7APLmLyddDKtdezBTgO3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=rkOxUNGnL8vu9YLjKhVUYox69wlKMSYz02Z7mnPEQHzL0zB_yUdCRZP_ikkU1Z82jW_ETIuD52uqoULYMtXz-IPbAnr5R7C2GMnDCZNAywVxiKhk10nJzLyjA2Mxd_j4pMLRqlCeVsBczMWyAWj7yBAGZewWweXvJf33C3IameeQ94aX0fJvVqzsGvEIvwXY2mFxffQDeEr8h85H_4t_mbzAeGspYo2w1AaQ9BwTwd8VGT5KxQDaS2-EH3Mv6E-NJfJjQ4GnC7jh1EWX5S4lwutwBbllvSj2iODjT1RlVsQ325TynRDAzIgPee9zHdgCkaoFKEr1GibHb97eC_Sxaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=rkOxUNGnL8vu9YLjKhVUYox69wlKMSYz02Z7mnPEQHzL0zB_yUdCRZP_ikkU1Z82jW_ETIuD52uqoULYMtXz-IPbAnr5R7C2GMnDCZNAywVxiKhk10nJzLyjA2Mxd_j4pMLRqlCeVsBczMWyAWj7yBAGZewWweXvJf33C3IameeQ94aX0fJvVqzsGvEIvwXY2mFxffQDeEr8h85H_4t_mbzAeGspYo2w1AaQ9BwTwd8VGT5KxQDaS2-EH3Mv6E-NJfJjQ4GnC7jh1EWX5S4lwutwBbllvSj2iODjT1RlVsQ325TynRDAzIgPee9zHdgCkaoFKEr1GibHb97eC_Sxaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=P1PJtyTdFw5xc3eIybZUGB6CkgLtpggIbvto9saB6VS9rD0jYQl9IyoQW3C08Rh73omwXBG1qKi5-hwQIdfpobDq_r3cPPJXe-OimKOCfCoYvsxVCrTWoZHzycwDIF6kZU7AMnoDweZ6VCfd8Egibusk12NGE7VeoeamIuKz5JVgRQamTSGPDqblw0bkcP16ICg1sr-Q6FeOn33xnuQape1_s86W_r1mnsMXkblM6y41l91qtNdu-6Gg6nkS4b9KQA4uGwjvhZWCXcphaGljqJe69x2Vxvbv6c3igOemPyRg5gCDOzOO1OP4-bDpFDLe7xjlU8IKsaPSilc5Q7_jak4sSGH8McI5N-EHojh77MQgqKsvDtjdEjvqot6uoBfphUp81nOxiB_1lPtkGY32fKLjKhduYeAbPWtzXXbEv-UVCn9Yzee5IEdbrd5J2VUhdLZTpvFMEfnQS6pw8Py5LrDs8-RpmXXCGxEBuqzwwPDwZ70OApUDFkHEe0vle1J_LS-LN-xlakYnPP1xT6bodW3yprJ3Bp_xeCqI4e3N_mYF_PlacjF8JKlgClN13ThOkfeEifi3EskA2a0XjtHZ6KzlPUmfvlrC4622uGNf3RfyILE_GsmqftXlgrzwCm6oYpK1zcaOXy0oMZXRIuxcNIoPnnD8Hz1F44omAyrUWFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=P1PJtyTdFw5xc3eIybZUGB6CkgLtpggIbvto9saB6VS9rD0jYQl9IyoQW3C08Rh73omwXBG1qKi5-hwQIdfpobDq_r3cPPJXe-OimKOCfCoYvsxVCrTWoZHzycwDIF6kZU7AMnoDweZ6VCfd8Egibusk12NGE7VeoeamIuKz5JVgRQamTSGPDqblw0bkcP16ICg1sr-Q6FeOn33xnuQape1_s86W_r1mnsMXkblM6y41l91qtNdu-6Gg6nkS4b9KQA4uGwjvhZWCXcphaGljqJe69x2Vxvbv6c3igOemPyRg5gCDOzOO1OP4-bDpFDLe7xjlU8IKsaPSilc5Q7_jak4sSGH8McI5N-EHojh77MQgqKsvDtjdEjvqot6uoBfphUp81nOxiB_1lPtkGY32fKLjKhduYeAbPWtzXXbEv-UVCn9Yzee5IEdbrd5J2VUhdLZTpvFMEfnQS6pw8Py5LrDs8-RpmXXCGxEBuqzwwPDwZ70OApUDFkHEe0vle1J_LS-LN-xlakYnPP1xT6bodW3yprJ3Bp_xeCqI4e3N_mYF_PlacjF8JKlgClN13ThOkfeEifi3EskA2a0XjtHZ6KzlPUmfvlrC4622uGNf3RfyILE_GsmqftXlgrzwCm6oYpK1zcaOXy0oMZXRIuxcNIoPnnD8Hz1F44omAyrUWFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=mi1MNuECv7ll4BCdTe6NwhcIZysIKtI9VHRD5_t11r9zKmj5hhWpMm8GZImv73bh8NcFSjElU1dl0cqdyHLFWi16bbQAYqxj1jq8AtZyMm0tmzA4wGl6oRX0A3ZixhbdA_d6aW_g4wlR9FzdTV0lxBGTx0p5eliiCdMVbroBaRPURXeQSsoafrrNtDXdjkHc9roAIo1EHnmFgquaBTxNSaipUkn2EXdqYnFRxeYl90yDyb34VSS1qD3fQuKX5Uuz1ieO_ylVVpIS63Sy-IIMzmGlQbYV1gCkQ5TRQgSgpfQjT0I503ZcnqocPBGtVjdhnbl5vFjjwaFcPn2LD7hJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=mi1MNuECv7ll4BCdTe6NwhcIZysIKtI9VHRD5_t11r9zKmj5hhWpMm8GZImv73bh8NcFSjElU1dl0cqdyHLFWi16bbQAYqxj1jq8AtZyMm0tmzA4wGl6oRX0A3ZixhbdA_d6aW_g4wlR9FzdTV0lxBGTx0p5eliiCdMVbroBaRPURXeQSsoafrrNtDXdjkHc9roAIo1EHnmFgquaBTxNSaipUkn2EXdqYnFRxeYl90yDyb34VSS1qD3fQuKX5Uuz1ieO_ylVVpIS63Sy-IIMzmGlQbYV1gCkQ5TRQgSgpfQjT0I503ZcnqocPBGtVjdhnbl5vFjjwaFcPn2LD7hJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=XwrWaEC6WUNpkyZmCJumiSkyZIK5RupR_cHUMzBh8dMzi-V2fW2nW3iVAtOTzTWgRC3FiGT9unIUB-Qhq6yB35Ef9AP5wSPcrav6YfkOid1GtPaMvccIB_Hw6rcfzy5Qm95tuXbwyFipxrqe7QW5evxUNbT1l72la3lwcvuzqPVug0zBEhkA1_0cvHcrjh3pAqm1h5U1OeYCTi62a1sLJ4Rqy0VehasOmP-G1nnFgwWp6jN6m1PJARETP2hyMarCleNCuHzaLWsZo7__qN5_AeDKbAnIcT1L8P2rNHtl020h2APi2ny3ImTmIRKR12dQrzbOXKk4jiw7_VOhyGEXvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=XwrWaEC6WUNpkyZmCJumiSkyZIK5RupR_cHUMzBh8dMzi-V2fW2nW3iVAtOTzTWgRC3FiGT9unIUB-Qhq6yB35Ef9AP5wSPcrav6YfkOid1GtPaMvccIB_Hw6rcfzy5Qm95tuXbwyFipxrqe7QW5evxUNbT1l72la3lwcvuzqPVug0zBEhkA1_0cvHcrjh3pAqm1h5U1OeYCTi62a1sLJ4Rqy0VehasOmP-G1nnFgwWp6jN6m1PJARETP2hyMarCleNCuHzaLWsZo7__qN5_AeDKbAnIcT1L8P2rNHtl020h2APi2ny3ImTmIRKR12dQrzbOXKk4jiw7_VOhyGEXvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ3VBqkIq5qdka4pcMchzrYlxtXhnILYwjpWJvQyOa787m5Q5qtz9psAo-9p9BM6R94Oz_jjUqkaVSlww5BrN_igF7JMOVt64l2vVPYN5Y1qLnkuIBMbBhSLkNZQSPrAn4UAsjjF7jcJ5j44PsHAZnFxwHI_hp2XUPYiF9X70iO0u3FKQESF9gOOLY41hg1l4cNA8cqNdCpwSP5OJZMVbRFNOS6oAGPeOfUm88LpF3393OWaEDsDcg_Cj-RoEqr1u1THmJg0l64rtNnEzLwFVOqNkzD0vAXoWclw_D0JlxA1U6D1I0NKyDKD7Ipe1GUZTr1J2DhVK8S2Mw771EI8VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS-kmQuFiRUrnDNjtqp6e8e7qqvg3Sf_pyaPIrz09eRGBZ8-lgSExFH1eYR9XPD3WwHDVblml5gqOuNbArgoDq6odsSA9jvSd8YwbnxN7sx44ENwJd3VE1NoUlkgAYOLDuWJlhF6iX4W72B7KCViPHWrQDTE8ircFGr5oCfuADACk__IQbOLAJNZpsNZaQYUZvR5L3OFwhNLSmFHlkSYflr8OUN3VvzKMmfelvw4D3gmfjzoyr6SFzk4s7qPnFyjHTN6XppfKDy9zE72tYaJafxjHPx2g0zwiDBWo2mXBbLug2CJgOiWb19t_55N8v5cLXBNz7mLhJjEnXao7N3iWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=F7XMAxtcsvVNPLoAiGtOgFEVNLa4YzwT1C80TNr0heQdgVRDvlx_AIinMtqj_bK6pkI0wcZgrKW6zt5RSy3ajzS2yZX_toLCt5vddZQ158e5rVxZf_TXqQToHeucE52Ea-M6tqywERXWyKnyDuu5b6Xko8BmIUPmNmnT5mTYNvZhvwSg2btyPvVh8gzt9jMP1bA3xJPFcgF013AfNq_T9Q9jY9zNkY4jwyJohiU15FMoFqIHz-wgnphXoG0TAKZnqRK_fWqSDXRThm6YOJYLQJ2ckx36yqulYcyTPXJpLPAozV9KUOOEI0v4TipLyrHjLeWJ-6kTaeiven_JZApYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=F7XMAxtcsvVNPLoAiGtOgFEVNLa4YzwT1C80TNr0heQdgVRDvlx_AIinMtqj_bK6pkI0wcZgrKW6zt5RSy3ajzS2yZX_toLCt5vddZQ158e5rVxZf_TXqQToHeucE52Ea-M6tqywERXWyKnyDuu5b6Xko8BmIUPmNmnT5mTYNvZhvwSg2btyPvVh8gzt9jMP1bA3xJPFcgF013AfNq_T9Q9jY9zNkY4jwyJohiU15FMoFqIHz-wgnphXoG0TAKZnqRK_fWqSDXRThm6YOJYLQJ2ckx36yqulYcyTPXJpLPAozV9KUOOEI0v4TipLyrHjLeWJ-6kTaeiven_JZApYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=bvU0-aN88IwZdBVKsiZVnblpBX4PI-6SLyAYXsKLZBw87AJBXecuYggd4Nty64KqY_TMWFcFVTgUFdEUVNfI9q15fzNP5YeVNV8DKn2o1SznQqU0JhoG7pFJJbbdGBjcWD4Z4KA9WUQ6EfdD-0shhMaj3E1nIfzDOzFv0krNq8QB8cunAuKRVB5zUlutE4onDfyfJ3LPMo4qa38d88kCdo8lISqmKIg4W0r3WagOiBQ8U3YYPcryX7v9pPp9N7MUF9NvpwJbeZBg0HPjoJsVB2yq_qdTRQ_jAhn9Ee7uB3ZCMjSa45S9j3V9fd4iYVElWiuUkxAgd5iu9rKFSGfPKpm4e39RBPaTv-NazpWzDXX9M3GCx--31vKrQ8aOxJ630MfhYriF3ez6ZuVfTje0auMfprjSTcapaknpsambVAON-GTew-Cw1A6PI5D01OaAQhvKEC1RjCzH8smFjfLddCUzS-IUyIGz16OOh_Oi1XEdikpN4hfDmdBg3OxpVvGWrvPOKdexiX0Np6ZxZ_hQPKHbch-0sL2I_Gxr0-HBu0F045recur5XB8zpwVxgxVCpExijijRi-KRtei4kBT2oZergSNFPK--Myp0h3ps3ZBiGCui35whHGldmHbpMuC7HFOXXg7BKmKAVmSvhR-1xySHXiwxmuKPCPy9I2SlAWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=bvU0-aN88IwZdBVKsiZVnblpBX4PI-6SLyAYXsKLZBw87AJBXecuYggd4Nty64KqY_TMWFcFVTgUFdEUVNfI9q15fzNP5YeVNV8DKn2o1SznQqU0JhoG7pFJJbbdGBjcWD4Z4KA9WUQ6EfdD-0shhMaj3E1nIfzDOzFv0krNq8QB8cunAuKRVB5zUlutE4onDfyfJ3LPMo4qa38d88kCdo8lISqmKIg4W0r3WagOiBQ8U3YYPcryX7v9pPp9N7MUF9NvpwJbeZBg0HPjoJsVB2yq_qdTRQ_jAhn9Ee7uB3ZCMjSa45S9j3V9fd4iYVElWiuUkxAgd5iu9rKFSGfPKpm4e39RBPaTv-NazpWzDXX9M3GCx--31vKrQ8aOxJ630MfhYriF3ez6ZuVfTje0auMfprjSTcapaknpsambVAON-GTew-Cw1A6PI5D01OaAQhvKEC1RjCzH8smFjfLddCUzS-IUyIGz16OOh_Oi1XEdikpN4hfDmdBg3OxpVvGWrvPOKdexiX0Np6ZxZ_hQPKHbch-0sL2I_Gxr0-HBu0F045recur5XB8zpwVxgxVCpExijijRi-KRtei4kBT2oZergSNFPK--Myp0h3ps3ZBiGCui35whHGldmHbpMuC7HFOXXg7BKmKAVmSvhR-1xySHXiwxmuKPCPy9I2SlAWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=hT9sFG4hrCXoZyxTF8uWXwRfJxBGTHIJPZ3BqEMmY7TXLBLJkwchH0bQKagaZpziKc0nXxsxAnWMy9X7t3pIdCmpz1UFPa47eh5yNWhgyOT-8x-ZKB7muZSAxRPZ6WkY8LP-QmPS5tDcIHgBerd52n3mHV_XVCjkMNAP1apfaz0Ya3ft37XAijEbYYHVF9cO1JVdEdXTPDD8YgOsuaM-AZv_IiWLUjpW2Mehgldid0rOM0bPMl6L9-60vYkZsJN4DhJ006fM1tp4wgWqXXBguSUtybdHAxOqQQOvJ1mHN0dAzsuCpiFTwsPL7skPhivjAnwafSW2qMPxRPFvTYX3aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=hT9sFG4hrCXoZyxTF8uWXwRfJxBGTHIJPZ3BqEMmY7TXLBLJkwchH0bQKagaZpziKc0nXxsxAnWMy9X7t3pIdCmpz1UFPa47eh5yNWhgyOT-8x-ZKB7muZSAxRPZ6WkY8LP-QmPS5tDcIHgBerd52n3mHV_XVCjkMNAP1apfaz0Ya3ft37XAijEbYYHVF9cO1JVdEdXTPDD8YgOsuaM-AZv_IiWLUjpW2Mehgldid0rOM0bPMl6L9-60vYkZsJN4DhJ006fM1tp4wgWqXXBguSUtybdHAxOqQQOvJ1mHN0dAzsuCpiFTwsPL7skPhivjAnwafSW2qMPxRPFvTYX3aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=A92NsxEydaa0MU48CmvYtetSgPA0FRS9k9TI7UAxyeah1oPWKDXoOGXpNaimWNRDK45lHPGj-b4A39RSVsiNe5PdUli5dy-OoZGEm4mB9mR8HAuk1UYo8LxNi94hbfQHR2AuX5XIFhBBIJ492K-phumtIcClGPNoSRCCltQHiqI7XO0PJ82CueWWMqfH-0iCps7uq0l0xBbTX3T68x2VI5Wd4WRyliM9U0enbwqomhRZ_som0QNOoPlpQ8RYc2DtA-iHWJ4XBfg4HTIWpUnSJoEnLusIgP2t3_nKZEyPGQmBAM2xPGFNBGMTi2zjmSTq2wSZp_ePpk8jy8X1zNFDLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=A92NsxEydaa0MU48CmvYtetSgPA0FRS9k9TI7UAxyeah1oPWKDXoOGXpNaimWNRDK45lHPGj-b4A39RSVsiNe5PdUli5dy-OoZGEm4mB9mR8HAuk1UYo8LxNi94hbfQHR2AuX5XIFhBBIJ492K-phumtIcClGPNoSRCCltQHiqI7XO0PJ82CueWWMqfH-0iCps7uq0l0xBbTX3T68x2VI5Wd4WRyliM9U0enbwqomhRZ_som0QNOoPlpQ8RYc2DtA-iHWJ4XBfg4HTIWpUnSJoEnLusIgP2t3_nKZEyPGQmBAM2xPGFNBGMTi2zjmSTq2wSZp_ePpk8jy8X1zNFDLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=NOsAFR7iNA-hc7F-kpCOH6gBNksQVDDaYRgoIZI3VWz0DhTM0Gpd3Z1BabOtGwiztdvE_YNFQruukM2pOomXyCgPqnamDwxgEcZcrC6DUJwPUd161etblzrFh6h-_kSLlHUGEp_WE9rs1hM4FJnaZHhKtByl8y4lBbX3O43o6Fw87WrVBsYyx7xdQwim2MOL9AaLDVJI4FPkX_UisAP_520FmgMJnX0r7cAq85eTihBv1HJQIAMz3Ji6_vCH3iuAyfFwiTJzkmOYN1tmMaYvWA5cQ669ePEfUzXMYmS_WOb4_lLprOyRCDQ4Y8-oPSxcZc22Rgrz-Ajfm3mDsTLWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=NOsAFR7iNA-hc7F-kpCOH6gBNksQVDDaYRgoIZI3VWz0DhTM0Gpd3Z1BabOtGwiztdvE_YNFQruukM2pOomXyCgPqnamDwxgEcZcrC6DUJwPUd161etblzrFh6h-_kSLlHUGEp_WE9rs1hM4FJnaZHhKtByl8y4lBbX3O43o6Fw87WrVBsYyx7xdQwim2MOL9AaLDVJI4FPkX_UisAP_520FmgMJnX0r7cAq85eTihBv1HJQIAMz3Ji6_vCH3iuAyfFwiTJzkmOYN1tmMaYvWA5cQ669ePEfUzXMYmS_WOb4_lLprOyRCDQ4Y8-oPSxcZc22Rgrz-Ajfm3mDsTLWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=Ai3JsqciSWfM0JKaj5tHIdlY0evTlgChzU29aYfWh4VwyknGWu3zNLH7C7QZKFRzbpc8Z5d9P31jYydggHV7V9f-D7Vb1THewP-UAyGY68vvJpdEFdIZwv7d68fcr0RzHL-GEDrMKV2bGlQhR5iTNSmss1tHN1zHoDJPYfD9No7mRfkKOM6Np4KM_tJMe1-ehYEKsVV1q3gJF77nXNAJmNzz7To4slvCOE2-2bpbCpsFDNER1Kp3RTS4F25aqdGi005y5XgU17tvQ83hpl5LfWEGVujyM5gAit0J9YBORbT-l3ON8Stdy39Y-7JU7HyX8xmWB5zrL3Ly-AbozwNvYSamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=Ai3JsqciSWfM0JKaj5tHIdlY0evTlgChzU29aYfWh4VwyknGWu3zNLH7C7QZKFRzbpc8Z5d9P31jYydggHV7V9f-D7Vb1THewP-UAyGY68vvJpdEFdIZwv7d68fcr0RzHL-GEDrMKV2bGlQhR5iTNSmss1tHN1zHoDJPYfD9No7mRfkKOM6Np4KM_tJMe1-ehYEKsVV1q3gJF77nXNAJmNzz7To4slvCOE2-2bpbCpsFDNER1Kp3RTS4F25aqdGi005y5XgU17tvQ83hpl5LfWEGVujyM5gAit0J9YBORbT-l3ON8Stdy39Y-7JU7HyX8xmWB5zrL3Ly-AbozwNvYSamQj4itgTFyZNHdjbAGPbeXe_1ReA-rYlZReXBzA8CVr47g7k7zHyRGladRkTkvhOK4FArT3pP20IrJrQyhuBcMD1dCTpbfIXvk972SG0yF3qthCjrUiSF-8KCUG_xpNBO4aMPlk3MxOh931nuQnhlv1DgjwuDABwOgdZKe3jrLCm_xg2RfyamjzwpORE2hHxyIbLouQ5vYbr4BhBrPWUuEdMCV2rfL8m_HPIQ-iJ40AOW6zd7fuEavZzQ4l4iboMiXTVvz9YVlgzmd-0iURpiyzwvhhj6DqiP9uxyU8DajDhIl_srmy0V9mcy_vetSmrhNq6kzYdzdXsYcLkjKHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHeBXYM69I0h-3UVXnhH5jV7QojiLXtABB9DnTZCRAaXrAqDFk9xblXbcewGftk5yFg8OyjaClOSfq1BYUhHnbkAnlfIZbo6_9jpc4ixrRqgXy5H3fj1F8LWs40ltLx3wvsZqMsukevYC0U7tsr5GLwQnfX_K4GtBuTBLmtkaXqfBuO96tV3OmSJakMf-3UAE1xewRPQE_4lYc-DunXiePzIhJtjppcUHlFAyJW7dId2fitruR6UMNzRvgowJo_tSAvex1zzbmzG21jWf5MSjbqN7jUbpnWj-yJoBQ5xKc8EolchkLelkHNg5hy3nuxruwcUd8H2_F59duCjRFCyxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIqRH1fE4wOz-3qnHIEFrXX5pNHmxmYfLDTkY_zq0biTS3BE5TcjRbTWwyA1FWmFeKyc2tuHmb3Qk5WxQNEHdVFSzZpkiPgGU0U0NShi39JyD3_ZxFChc2iTBvj0xF8zpVX4_o6jQZvcx55vhB3cAZEGpFrni_V1UKocPPDh9lYS_pxmm-YA9FQ8QwauGSXLj_aq6f3cpqbRlEeGAsvuFrCjc-vzyUGDI5UId3BtwBRYHUO9n_d-YLBALpnyia25EMliiR_xoCwcM6Hg0k16yWT7_dyXyiwFk75WECbQjITdmPdRck6-ReqUhOGyZXozFdceRdb749jqI4FQVks9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=u1tut6-6jYOEcHY0cJwniZp9dw3tK22MJadFNssMkRtX0fvGeujZNYfKDkdLcXsi20YFzinXbGHReKRe_XFK3O7DkZZp9tdeB38MtV6bm7q-K-2eLuovtlUwf8w4xwMFE6Ja5Gt5lqaU7Ss5m8Js0gaRx5EM9mNTM1KLs0k58dIQ2C3IXH3BpDDIXb8lyitmslty9rq9echtZ7wOh2BwozXh5KCs8K1VCxEH7AegLfL7ds7yaIxgRgJj9tTOkrEEFSAfoslBwciqMZpfJ_yN0QB-ZecTVVH4kYWEURtCNmEIibFHCT_wfhnephY5Ada9j-cT_EXKQgR2XzaklH7-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=u1tut6-6jYOEcHY0cJwniZp9dw3tK22MJadFNssMkRtX0fvGeujZNYfKDkdLcXsi20YFzinXbGHReKRe_XFK3O7DkZZp9tdeB38MtV6bm7q-K-2eLuovtlUwf8w4xwMFE6Ja5Gt5lqaU7Ss5m8Js0gaRx5EM9mNTM1KLs0k58dIQ2C3IXH3BpDDIXb8lyitmslty9rq9echtZ7wOh2BwozXh5KCs8K1VCxEH7AegLfL7ds7yaIxgRgJj9tTOkrEEFSAfoslBwciqMZpfJ_yN0QB-ZecTVVH4kYWEURtCNmEIibFHCT_wfhnephY5Ada9j-cT_EXKQgR2XzaklH7-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=YGgw-N8vN7NbS46vJEHTaEzMnBJNhGhrtqzNaJJsplQakswwNsDcimjTZTjFfN6S7uYDYV0RGjn2KIou-y_2WOBp5axYYdX7M_67nxKCefZjt29J7LiEP0s1LVjYpvwevN3ILi7Pz2TjHNdpcyQNgFpOLcVQKNU2kQjVplUaLa52HAIlg8TOVhAqQpYZtkkX2dQy5hdMdAPg7PEN2STVJIoZOg0NygBUzzs9yu46RNH6hhCSYg7jXm4NEZ8iBqSZMtmpnqMVyHa4Jw7lYOcaHKIBU7E851BLn9T3g4_g9mtDP_qwjPNpE4N8o9Wo1DjLasei9inLYDYXQkVc1-2f-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=YGgw-N8vN7NbS46vJEHTaEzMnBJNhGhrtqzNaJJsplQakswwNsDcimjTZTjFfN6S7uYDYV0RGjn2KIou-y_2WOBp5axYYdX7M_67nxKCefZjt29J7LiEP0s1LVjYpvwevN3ILi7Pz2TjHNdpcyQNgFpOLcVQKNU2kQjVplUaLa52HAIlg8TOVhAqQpYZtkkX2dQy5hdMdAPg7PEN2STVJIoZOg0NygBUzzs9yu46RNH6hhCSYg7jXm4NEZ8iBqSZMtmpnqMVyHa4Jw7lYOcaHKIBU7E851BLn9T3g4_g9mtDP_qwjPNpE4N8o9Wo1DjLasei9inLYDYXQkVc1-2f-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=HtKY_SSZA-nJLkdYQU62oeiBPkKuyHB_JDcYmAFZGfQsu8Nw6fpR6gq_g5NcRYIxUXBe7W4otecJ1fX5iYV3xMrpY3NFXA8M8sw9wRjUFmen77zdEWQtZkHS-pHlsCHYCUJJwhJTUuUK4ldxfNqsxMCdA9WYfiyKxxPM-RdmmIiZM22xEiL5tFFHIa_FLetn6BDJ8tdEfg0VIyI4Gt5WO__gO77A8A7UYMhnfiNi7od4E0s-d7yP8XApYqrQddDN7-MJXoihNhh4ZWY-JQpcf7p5ALEy0W3MXCypsSH7chKGOxSthyuIC9pfd1ud4_UQJYb5QhpDcoOynuposqea0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=HtKY_SSZA-nJLkdYQU62oeiBPkKuyHB_JDcYmAFZGfQsu8Nw6fpR6gq_g5NcRYIxUXBe7W4otecJ1fX5iYV3xMrpY3NFXA8M8sw9wRjUFmen77zdEWQtZkHS-pHlsCHYCUJJwhJTUuUK4ldxfNqsxMCdA9WYfiyKxxPM-RdmmIiZM22xEiL5tFFHIa_FLetn6BDJ8tdEfg0VIyI4Gt5WO__gO77A8A7UYMhnfiNi7od4E0s-d7yP8XApYqrQddDN7-MJXoihNhh4ZWY-JQpcf7p5ALEy0W3MXCypsSH7chKGOxSthyuIC9pfd1ud4_UQJYb5QhpDcoOynuposqea0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=t3buDM0YzUQZ9mxGHSNHe3jX1U-UG7KJtODzftusWj9PBRNnR98Kq7vRH4UxNEaox6ivaSvtrNOuyV68n_a_TKAhAowqv4N_RrXDLswP4KGqVsT91_v-LbSupfUGKvsjojjtQHK7C7Ug1Lf84EkP1xiwC7VWM-Y-bRCOEmzy8ALkBg4Vx8Gj28wic0d4Lj3hZaf4Z_AHkyNbzURFmkcxA-U_XawcbxH4j5XSuXaNbDGuHxJTvvznaihqKjixmuC4HlsnGDgzw3Ha64zDOMAXj0Xyub5DQID3VhZJF0BzpKG5ENW1wo2d1zBU9xTRGWbK8URcQFnf3aS3jtb3eDXGqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=t3buDM0YzUQZ9mxGHSNHe3jX1U-UG7KJtODzftusWj9PBRNnR98Kq7vRH4UxNEaox6ivaSvtrNOuyV68n_a_TKAhAowqv4N_RrXDLswP4KGqVsT91_v-LbSupfUGKvsjojjtQHK7C7Ug1Lf84EkP1xiwC7VWM-Y-bRCOEmzy8ALkBg4Vx8Gj28wic0d4Lj3hZaf4Z_AHkyNbzURFmkcxA-U_XawcbxH4j5XSuXaNbDGuHxJTvvznaihqKjixmuC4HlsnGDgzw3Ha64zDOMAXj0Xyub5DQID3VhZJF0BzpKG5ENW1wo2d1zBU9xTRGWbK8URcQFnf3aS3jtb3eDXGqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=aouKHGGTRp_5MjRgawb5zy0RRE8DNdAOXiwIxnLP-Eyi_S_GiINogrxZ0baW86ja3k2Z3MGYl9_5JhO68z6lDp5i9MVTZIOKK54gHZMGs2TCitJANoxp21Y2S4Mo1TEOJnFA7O9aA7FicQUVRWqzUe4YjSEzFFeFK8tD9y8bYKydq2ZWf58-35I5VSGx-YTLBHuu0DstbqyVXmU5thjFi2kpYtLCMgwimF69Y_UN_t3uvsA7EQvxr_A8vy7wpxnz5N_wuIfALatm9pfdr_s7LN8kut4A3Lfwkp3iPDrjWWN4brMgJIHztl215VU-36ahe8aJNtlmpvAKz5DCSSf6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=aouKHGGTRp_5MjRgawb5zy0RRE8DNdAOXiwIxnLP-Eyi_S_GiINogrxZ0baW86ja3k2Z3MGYl9_5JhO68z6lDp5i9MVTZIOKK54gHZMGs2TCitJANoxp21Y2S4Mo1TEOJnFA7O9aA7FicQUVRWqzUe4YjSEzFFeFK8tD9y8bYKydq2ZWf58-35I5VSGx-YTLBHuu0DstbqyVXmU5thjFi2kpYtLCMgwimF69Y_UN_t3uvsA7EQvxr_A8vy7wpxnz5N_wuIfALatm9pfdr_s7LN8kut4A3Lfwkp3iPDrjWWN4brMgJIHztl215VU-36ahe8aJNtlmpvAKz5DCSSf6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKW_3A21U6d2HuBkJDJhBhCn6d37gK165qc_J_TR0yHvd4KvtnNl5oI4rx_o5DapdIb0XsTg6iQMJdDAfcm21r6IC_x2Fp6MXCCQXpoBILmsNJsiB6sikjmIHVorRNMPRnGKQE89KZAGn-hNr1-mUYiAlWPeId1PWASuBuJaNPwaTXQSjlbSyylYx_RTVUvY34WmQlm18QGNT6qud6MSJNMBzcVPghEcePNazSelgpPFtS6-m68TRyhoIoA8pCMhMwJ6gl9wvZsePtsBNBLM5HiBRcfxLbiE7-_wIyyAiYWhJdkZbc7XhoXaQVYMdcEkjXl9301nzeAHYZMSsIz9jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=Eo7JKnuFAMfIxLBKO1jLXyyPccbdC-4HAmIY7weMSAzBUoeajoQZSOwJUgoJYZwqLmDYdi_3mHtp8YfVTD9KIClaChL6d2T7k8BoMaDLmks4X2s6Pgwixc57F1kA_xpie6dWqtNC2HiFS9E4yosV7U4F0r4lzwoDJmhUaRu45iuJCZ9mwKMUyKzjiSs49jdNUQPKVYAppabVx1aDGzWRPiJ4LXlZGLODjQSAT-natW8IcK0RogZKn48OSoMWvoOP2ln7HEqOsJY4WnNYCNsxBRT2whK8DO8v76eTghbuTAZgqqa9rAkp6ykPRRm3_Ef80eC-RXQ-ABT2syyZVo2ApQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=Eo7JKnuFAMfIxLBKO1jLXyyPccbdC-4HAmIY7weMSAzBUoeajoQZSOwJUgoJYZwqLmDYdi_3mHtp8YfVTD9KIClaChL6d2T7k8BoMaDLmks4X2s6Pgwixc57F1kA_xpie6dWqtNC2HiFS9E4yosV7U4F0r4lzwoDJmhUaRu45iuJCZ9mwKMUyKzjiSs49jdNUQPKVYAppabVx1aDGzWRPiJ4LXlZGLODjQSAT-natW8IcK0RogZKn48OSoMWvoOP2ln7HEqOsJY4WnNYCNsxBRT2whK8DO8v76eTghbuTAZgqqa9rAkp6ykPRRm3_Ef80eC-RXQ-ABT2syyZVo2ApQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2O_pZ0kwDhlnov11cv0LgzWjFJtj-wM0-D7qq5S_G3EeLzB8MdHqssDFit5sZdHtIU5N3Q4kJvANnTj2MR32Ololm6dQ8JZ59VejngUyEgm7r8aGwwmegGP5UDqBEriM0Woc7AMBjCbyX6GF57NLOavM-LK5B9yA6PiDN8nlBUqFQU8Um_HMucWHmZQJST7hRAozCtP_mhV3Z5-VdhfmNPKo-6mW9rBJak0745wBE9BGPtJY_ssyBYAKNY-89xeF5iZzGtFnVKC8WZWmyA_b1fgZsYQUAK07N4vuniVlEQF1hbOi5grX-FfPLmRYU9iTJB91PxIILbSD1BItw3Ylg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=HstWj4APLE6TsCiXhq-vx9QCgMCo1go23DEQ36xXjEmQsFw5lUHVDD_0ALQRRggGCO2kx-dSgzeuCOTeIdb6gihfEIb1EyjbSWRtMpGjnDLg68Q6datlyTPO9yGZsH3Wb4-BiyjpQFN180EnFVTjZjvN6gfZ_HHaJDyslq3IwBQUWCaguJZjVI-tXOnFexXRiDxKd48Qh9zuOlu0bMJ6WP1n-kytbPslSzzBu5rAArISgk6EjZBlA4vvwYlvkcMiLqfbhaeVjj95tUdjc6H9Pq8k2vas_3w__9-W_d9SR_PbZfcNwCms371m8Pw7VH7MAQAIOaxBkZkEEX4DMvL5cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=HstWj4APLE6TsCiXhq-vx9QCgMCo1go23DEQ36xXjEmQsFw5lUHVDD_0ALQRRggGCO2kx-dSgzeuCOTeIdb6gihfEIb1EyjbSWRtMpGjnDLg68Q6datlyTPO9yGZsH3Wb4-BiyjpQFN180EnFVTjZjvN6gfZ_HHaJDyslq3IwBQUWCaguJZjVI-tXOnFexXRiDxKd48Qh9zuOlu0bMJ6WP1n-kytbPslSzzBu5rAArISgk6EjZBlA4vvwYlvkcMiLqfbhaeVjj95tUdjc6H9Pq8k2vas_3w__9-W_d9SR_PbZfcNwCms371m8Pw7VH7MAQAIOaxBkZkEEX4DMvL5cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=X2fkOIOyA2BqHYP1MUCwVqD3X6SprHFHlGcEJe_M0XrEqRtbOsYnqvRAvnLvISVSsJwWzs-64Ho3t6R3qmijgXecHWWcZkAE7taK5WPRjd7vljyPcJ-UQcWe_ycKFyebbHy1uBE8qu0XLiNTUhPbv06wacZrbZ9sVTjooky2SSI1xfrQQvWjqNE3z0h-KqKNEPoHGIWyJAx0xXXimkmK2Ewzt-27MfIDAbh6Dk5FfFRCKr9Sw0ISI_uQwrfWONXUWaNDR6diMKbTKzgY1mcRyw9_ZPnvIc_Upz_2F3B9OcaykZmyyd9sNBzf8aI7_zyNlmQwG6_RmGwF5Ps53AByWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=X2fkOIOyA2BqHYP1MUCwVqD3X6SprHFHlGcEJe_M0XrEqRtbOsYnqvRAvnLvISVSsJwWzs-64Ho3t6R3qmijgXecHWWcZkAE7taK5WPRjd7vljyPcJ-UQcWe_ycKFyebbHy1uBE8qu0XLiNTUhPbv06wacZrbZ9sVTjooky2SSI1xfrQQvWjqNE3z0h-KqKNEPoHGIWyJAx0xXXimkmK2Ewzt-27MfIDAbh6Dk5FfFRCKr9Sw0ISI_uQwrfWONXUWaNDR6diMKbTKzgY1mcRyw9_ZPnvIc_Upz_2F3B9OcaykZmyyd9sNBzf8aI7_zyNlmQwG6_RmGwF5Ps53AByWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=Um6moJbZkUmOu6aWocqVrXBYNOE3G_XkiKLOQH3bJOre209_-X6POKSSGEH1uGzD7jjhUEEuaa3L7N--sQXYNXsKZuH3267z_BQonsIymkyopQQgLyTN5iOErUC4DhYmiM53IrXPNq9aG62EwIR0wifETmtPr0MlRQh07op1l9LgfdXQzfXcOHIkJ1jzXyWdJeEueq7OvcQxYFmxSfad8j1HtpsneA2rO7WydvhvWtPs9CQlxAuewMUHMvQhdK3WrzKOJ8PmcDV_UQ6jdN4SsGff_YJPXahAP3aIAqvG2fItce_n2NIHMFUW0fX-thpbpbr4jlqOEUi5T-cC3LPy8zKDKwJyBrDlPpRhQVXPPAb29K7NRs_MMnCRgspWRZ8kmjgTK8ySDFa2BGptOBIn-yfAaumvgLxoLlJ2XLaOfBQjLResd9CPS_ebM4buy7aiiZ7zKgDxMLroW-KQ8AXXYbMx34SzIIZaPQlTEel3EUwAjyXREij2iC6FJkBPgIDvlpkQcSbBqMf64v3BD_yIQUAMu_QaI4hUthjX_B7R3aZKmbP0N4QtDJmP1_Yr2i-b2DrtoutV5__DBMj30fndTXTj16qM97pW4c-gh5Xamw7hT79EkTm78UQ7kkpuSKhIMMFYJrD4NVcIKSH-4YyzoyeotvjipA0gsIF0kdQqjb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=Um6moJbZkUmOu6aWocqVrXBYNOE3G_XkiKLOQH3bJOre209_-X6POKSSGEH1uGzD7jjhUEEuaa3L7N--sQXYNXsKZuH3267z_BQonsIymkyopQQgLyTN5iOErUC4DhYmiM53IrXPNq9aG62EwIR0wifETmtPr0MlRQh07op1l9LgfdXQzfXcOHIkJ1jzXyWdJeEueq7OvcQxYFmxSfad8j1HtpsneA2rO7WydvhvWtPs9CQlxAuewMUHMvQhdK3WrzKOJ8PmcDV_UQ6jdN4SsGff_YJPXahAP3aIAqvG2fItce_n2NIHMFUW0fX-thpbpbr4jlqOEUi5T-cC3LPy8zKDKwJyBrDlPpRhQVXPPAb29K7NRs_MMnCRgspWRZ8kmjgTK8ySDFa2BGptOBIn-yfAaumvgLxoLlJ2XLaOfBQjLResd9CPS_ebM4buy7aiiZ7zKgDxMLroW-KQ8AXXYbMx34SzIIZaPQlTEel3EUwAjyXREij2iC6FJkBPgIDvlpkQcSbBqMf64v3BD_yIQUAMu_QaI4hUthjX_B7R3aZKmbP0N4QtDJmP1_Yr2i-b2DrtoutV5__DBMj30fndTXTj16qM97pW4c-gh5Xamw7hT79EkTm78UQ7kkpuSKhIMMFYJrD4NVcIKSH-4YyzoyeotvjipA0gsIF0kdQqjb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=Ot-HW5OCm5nb6Obf8jLbeKSKN9qt2RdY99Wx4bpSHuMB1-iKsIStiRFBWivD8u3ND8USoRhDQo5dede2yc-MH3vPsm1sT35JZtXa1eIHgzPVE7NV6RVr-t3TqCchYZcg2t8wXZAzKSwaLKX5Qbfx-7w6unzMkur4gWYREiA3-p_QIVn2qhd7c7gz5tmfiUhhxWJVuMntOh7BnXzSB0psibZNZOyCnLHV6z-T-Ss-F0RG75EDR93lrUdMX6DBxAg26nBi1YNnkjcn-s2x9UC63tiCvcVyK6UKIQ4V5RJrx3mSP1kSvH_aeOH9wUTbJuj6dcKV4MRfKCEHxqakI8Jc4r2-_lCf5JM61L8hKMJjGJeHOiCC6xjPmUNLkxDbdFoJSaOkvXLFaB2Gu1qE_3iihffxaQM0uZJAQusYbkzMINWyY1RlvIwnYq5MdQxWL_EMbHiNxkL0AnaSDqt7TTF7CsCVk85HVPBOe4OrAwS35jqIL5rtbC7JKCgcmQ4kqvM308jJtLzZguZHvCTeSgaysCdF9rrOnQrF58Or3z3kHcW77DtpSOq4yyMm2ON_pbIyDlN2Gw1AE-y9nXfd1kKmIPwySZdsdM8etUqF0AAcJDvXTKaO3yj6IDz1wKLXlzp5OMYYx5cTfC_K6pEAsfCrjlR9a3JtjAdXybdDCii9KME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=Ot-HW5OCm5nb6Obf8jLbeKSKN9qt2RdY99Wx4bpSHuMB1-iKsIStiRFBWivD8u3ND8USoRhDQo5dede2yc-MH3vPsm1sT35JZtXa1eIHgzPVE7NV6RVr-t3TqCchYZcg2t8wXZAzKSwaLKX5Qbfx-7w6unzMkur4gWYREiA3-p_QIVn2qhd7c7gz5tmfiUhhxWJVuMntOh7BnXzSB0psibZNZOyCnLHV6z-T-Ss-F0RG75EDR93lrUdMX6DBxAg26nBi1YNnkjcn-s2x9UC63tiCvcVyK6UKIQ4V5RJrx3mSP1kSvH_aeOH9wUTbJuj6dcKV4MRfKCEHxqakI8Jc4r2-_lCf5JM61L8hKMJjGJeHOiCC6xjPmUNLkxDbdFoJSaOkvXLFaB2Gu1qE_3iihffxaQM0uZJAQusYbkzMINWyY1RlvIwnYq5MdQxWL_EMbHiNxkL0AnaSDqt7TTF7CsCVk85HVPBOe4OrAwS35jqIL5rtbC7JKCgcmQ4kqvM308jJtLzZguZHvCTeSgaysCdF9rrOnQrF58Or3z3kHcW77DtpSOq4yyMm2ON_pbIyDlN2Gw1AE-y9nXfd1kKmIPwySZdsdM8etUqF0AAcJDvXTKaO3yj6IDz1wKLXlzp5OMYYx5cTfC_K6pEAsfCrjlR9a3JtjAdXybdDCii9KME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu03Y1y6DKPQldOVZGdgiiTRuOsdV1dZQHsC7vpLwgGGuFORUZg2-FLzBB3nPrxM_ePZiXT0XP_QJkvnjpiOhs_2Kkp3Xx3fZoE34P2OXyUBA4ZN4XJCKepKOoufBcbJbQeSSUCWPd4tcm0wNVtx8bsnf8OGg-sOpLTHi8HNInVj6aq4jExGq2vRfphualz1zF-bKAvtOhTvRemheHeONMHKpukcckzmtMLkYcmykZ5ycMcbCTffWmOP3uFe0y-jSPw7eLinaiciPcnrAxnvQr4NnU22si02c8zBK6d5OH5jC3yXtK0JcbfwBkVchCnL-rdKjeQkSQW6bvRzcHE49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VZIF0J7C-LlQGFz2r-nrJ_0fmBVusM3jhjMwuBh4rF2x3iq6-pNWUWCux7MdFlpFs38zHTHOG9t2csPuLzgytGfzYo0Uq1S4el3IVlN_zbWjdgksCGR_-ts65MxQ3GH8KOAgTs1iMzx6FDeV99tSErR3BWZOF9d0XumihF6OhKKVWGkbSy63D5tlsegyvcTkbg2mwjdLt_M93FN0FrRn4au8Pa1XyNh1RMzqZU6p-43T6AMsRDaowr2SKfhahjNEbuJ44mgOKGNbjAtLnIxskty6FRWnKNiG7fqNLNODHgzW0si0StQ2cSxRP67AhKFunGc9hxTTXEsJzMikz0FsRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW9klWJTB8u5LamDK-3zkWsEUkln-3ogrOr2FyVupmYk4eu13uyfc3wjmEKdk2JYCVA47c0k0KJT5W7qfxlXtRhA-khLIgFiE9R_4Nf-2E6bLrTUXS_mIUQTDTfnyluVGi3-q-YswDqeZ8we-t4Tafb3-6OH4-C6895P9vwpHqo8gXBZMn9t_abqLLQCKSrL-2eBRsnEsVv7RhxgfKcWFgfiqxnk2ZOVV2CL7C6ICa4tfeiF5A-fGIqE89NCBQ92iaY9QRegCp52RcXTIPRvHNIq9S6WRh2kw4SWtgBZCu2k31-eeiiODQgTUI9M8ZRqPk4hujMTTWGM_4EEF-avEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=M_GSQmpG64TFbTSit4B1WRBeZTdgxI5YXGu1Milts92r7vQtVTfej8MhaWOIMmz8wyG03Omyt0M0DR4WjpPVnbYzqDIZMLTb3fVGlFQlH64Z2a6HCPm22NoU5RFwC88UMCT6-rcD3U6lK3BPRT6sKxcz8FCGbU1JWHk_m0t21xy1LBu5_ZNoYWjO2jo0hfDG7mmfWSHB1vGJm1ad0YG5rVOSHbJCq0ii19thZBLJj15VMj4G_DEwRXFbc6MpzdVPXjY5ip2bCVNLGHU9qalYMo7TUdeT9G3lHhCTyPjvVYtIIORarOi9UYTdafKB_IvvTeVNAMPLlmkuRlPcgT9hbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=M_GSQmpG64TFbTSit4B1WRBeZTdgxI5YXGu1Milts92r7vQtVTfej8MhaWOIMmz8wyG03Omyt0M0DR4WjpPVnbYzqDIZMLTb3fVGlFQlH64Z2a6HCPm22NoU5RFwC88UMCT6-rcD3U6lK3BPRT6sKxcz8FCGbU1JWHk_m0t21xy1LBu5_ZNoYWjO2jo0hfDG7mmfWSHB1vGJm1ad0YG5rVOSHbJCq0ii19thZBLJj15VMj4G_DEwRXFbc6MpzdVPXjY5ip2bCVNLGHU9qalYMo7TUdeT9G3lHhCTyPjvVYtIIORarOi9UYTdafKB_IvvTeVNAMPLlmkuRlPcgT9hbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=FHgesSTjHfTW5PHtj94j2v5XZFBSE6yXaFy3isdUsETetRBgoahBUs_hiW5Zac_VL7GEwo97By6dAizkEN9fpGAbWWuiyeV7ENYCDTdY8lNzqfrmD-t3bcJDPH3TjCG-SOsUuqA_QPab6Xb6thdODwKjHNEwZdhzUkZwNb2xYhogTpOGtpfqVAkaV3t__rGMximXosXMm7jZbiMSTJ5AVCuKu8kVNYWA09XNmsxHjvkvCNAnE7UqA9gswSrbZeILWfkB3kyPhNroqV1F_mmx0fBQtFQ-D45XtpKBNy2FFPkf474Ks9l7_agu3RC7Q95ExidRpAAT5B7DEegMCRacAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=FHgesSTjHfTW5PHtj94j2v5XZFBSE6yXaFy3isdUsETetRBgoahBUs_hiW5Zac_VL7GEwo97By6dAizkEN9fpGAbWWuiyeV7ENYCDTdY8lNzqfrmD-t3bcJDPH3TjCG-SOsUuqA_QPab6Xb6thdODwKjHNEwZdhzUkZwNb2xYhogTpOGtpfqVAkaV3t__rGMximXosXMm7jZbiMSTJ5AVCuKu8kVNYWA09XNmsxHjvkvCNAnE7UqA9gswSrbZeILWfkB3kyPhNroqV1F_mmx0fBQtFQ-D45XtpKBNy2FFPkf474Ks9l7_agu3RC7Q95ExidRpAAT5B7DEegMCRacAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=uzrEDzVM8IDu1wFIUgVJw991DZLluWD_pfIP33RUdwS2LcrQGVj9cUTdHW6qr4zUBrnnHNYTJhc2_4scJa43oPKinz4qbds4MEzv93nLbxKkjYZ3i1ho0uivjijXoAe_SV8u5g082Fa1smH-UVrjEWihPPFG3pmgBEDFI0dlUC0-hhVBEOaDRM4QB48xFBjNBadnnMcGq0M94GAsti1eSp7oc1hq_8UwbRyW0SWkvy91Ydrc46yOneBKmxEHH7wlD71bpzSRqsoLUWhbAcjfwZwli3uRawWuXbvlEPzEYw4IqswwJF94USpo0mbfRrAQ4LtUb8mUEnwlkKL4bayHaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=uzrEDzVM8IDu1wFIUgVJw991DZLluWD_pfIP33RUdwS2LcrQGVj9cUTdHW6qr4zUBrnnHNYTJhc2_4scJa43oPKinz4qbds4MEzv93nLbxKkjYZ3i1ho0uivjijXoAe_SV8u5g082Fa1smH-UVrjEWihPPFG3pmgBEDFI0dlUC0-hhVBEOaDRM4QB48xFBjNBadnnMcGq0M94GAsti1eSp7oc1hq_8UwbRyW0SWkvy91Ydrc46yOneBKmxEHH7wlD71bpzSRqsoLUWhbAcjfwZwli3uRawWuXbvlEPzEYw4IqswwJF94USpo0mbfRrAQ4LtUb8mUEnwlkKL4bayHaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=VzhbDhOZbvX7b8zvrYNIlVzxAp3NyOqrGqCo8IG4brLPOp0jlQ8oZX4QJFZ6-7LPqNlZYdmnBxsHM_mxXAjvOHBYwBLUZorAHHcjuPmGvyzDKzz_E79Kqy08Mre_cNOUg1D8aHQMfIoWvrcOWNlBkvER426jMdqJAGqIYxcmWXY0uznu1cbv35-5Wmk79JGTxROokerD6fHpvOBPZA1M1_7JDPqLogUxV9jsu0nXvVuBPDrXbG3ILPUNyHC5uWIUhn4FD6Jf8ZaPOu2O7iQrqNwE0M-82AWT4gqdVXYeRdhLIC1xTYi_AlOtKvCUVJAmeRNC13qvrv47brrKRNq9Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=VzhbDhOZbvX7b8zvrYNIlVzxAp3NyOqrGqCo8IG4brLPOp0jlQ8oZX4QJFZ6-7LPqNlZYdmnBxsHM_mxXAjvOHBYwBLUZorAHHcjuPmGvyzDKzz_E79Kqy08Mre_cNOUg1D8aHQMfIoWvrcOWNlBkvER426jMdqJAGqIYxcmWXY0uznu1cbv35-5Wmk79JGTxROokerD6fHpvOBPZA1M1_7JDPqLogUxV9jsu0nXvVuBPDrXbG3ILPUNyHC5uWIUhn4FD6Jf8ZaPOu2O7iQrqNwE0M-82AWT4gqdVXYeRdhLIC1xTYi_AlOtKvCUVJAmeRNC13qvrv47brrKRNq9Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=t9wzSNHyaJObafBUapeGb5Oylr7Zoy4-xIbC_xLLEpiGJEKDChh1cAmmoT-68lFKae4ZfIV_bIibqkxJDfRRiSH2aW5RsbPndbSIebEc7p0pfLJegleWq8NIdd51wnYDIVEsvQzeKewxKx4OhrtsKrlngu0HZBlNtegzkyb_tKmHhmNiLMMHixtTDh3EU6jgbjsFWMPiUgcoHvpk4kMxrQP6IvTg0_blqtWtgeqjoim4xt51Ej-OEMqF-mzufhoGJAf_OUc2g-83kaJ9V6c2F3f98XnRI5FDt_V0ZHFcPkde_YLkgBgjLzA2mAqdmbrkYd8ooVBNk4w-QX7ZoTqQng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=t9wzSNHyaJObafBUapeGb5Oylr7Zoy4-xIbC_xLLEpiGJEKDChh1cAmmoT-68lFKae4ZfIV_bIibqkxJDfRRiSH2aW5RsbPndbSIebEc7p0pfLJegleWq8NIdd51wnYDIVEsvQzeKewxKx4OhrtsKrlngu0HZBlNtegzkyb_tKmHhmNiLMMHixtTDh3EU6jgbjsFWMPiUgcoHvpk4kMxrQP6IvTg0_blqtWtgeqjoim4xt51Ej-OEMqF-mzufhoGJAf_OUc2g-83kaJ9V6c2F3f98XnRI5FDt_V0ZHFcPkde_YLkgBgjLzA2mAqdmbrkYd8ooVBNk4w-QX7ZoTqQng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=AyjUuFWTQN_8MRo_TfJQl6HwlWPf0_9QV0v2dnqAp-qETd8lLyoON2kBRQSOdZ6I5JW4upyh-d_RjhauOJtULEUjBBB0n0fd3PiPYJ5O8DX5Gbxh-S_VXer6h29rlcBRggby6lomV6fTFljxrexoTb2msx1RirBDY7d-fwLji17GeOSQyFxe1nkZj-uHqdyvlPbQcqS6r59HIeJzBWydRVrWETfd5bAi2I52QVcVaeV3tDrrc9iQUHh3XIiiNPUV5Q03QE_rpo0KJz4KGl4yJx7KCQ5PiAnXKIDZERw73df2Zh4KQIKoQbJ68NtKeNIWsZSnCNxLEie3REWOwPMB0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=AyjUuFWTQN_8MRo_TfJQl6HwlWPf0_9QV0v2dnqAp-qETd8lLyoON2kBRQSOdZ6I5JW4upyh-d_RjhauOJtULEUjBBB0n0fd3PiPYJ5O8DX5Gbxh-S_VXer6h29rlcBRggby6lomV6fTFljxrexoTb2msx1RirBDY7d-fwLji17GeOSQyFxe1nkZj-uHqdyvlPbQcqS6r59HIeJzBWydRVrWETfd5bAi2I52QVcVaeV3tDrrc9iQUHh3XIiiNPUV5Q03QE_rpo0KJz4KGl4yJx7KCQ5PiAnXKIDZERw73df2Zh4KQIKoQbJ68NtKeNIWsZSnCNxLEie3REWOwPMB0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=Zl2tEPEjMtbNK8soxCSmhI13X5UAzKoXPOOzL27f-dsVXeQbkFtrpD3pA3Cm7a0YoTpuVW1grdycGw4ooGrcnXIqzNIAyEsJl78JzmRregJrSomf6-WF_o7vAFnavhTd9iJMu_Tf-UoKGKuu2l9lgCWAIapZm_WyylXBAuDw2-GWgRjNsSwlC0Ujp87nwJt-DIrYxTsJCVSQ_pP_-30y8s3iZtTh0Fv0bH5B6ZfhaeVAx0pRCz5HZB4KjcEVclZztKx9P_tNYW8WbHSH4OzOmypLkO2NERmjJbU-Y8cEiSQk5VM6usV1Vgf5PwRGP_ZsVvefn1B0i90NNLhWFJCidw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=Zl2tEPEjMtbNK8soxCSmhI13X5UAzKoXPOOzL27f-dsVXeQbkFtrpD3pA3Cm7a0YoTpuVW1grdycGw4ooGrcnXIqzNIAyEsJl78JzmRregJrSomf6-WF_o7vAFnavhTd9iJMu_Tf-UoKGKuu2l9lgCWAIapZm_WyylXBAuDw2-GWgRjNsSwlC0Ujp87nwJt-DIrYxTsJCVSQ_pP_-30y8s3iZtTh0Fv0bH5B6ZfhaeVAx0pRCz5HZB4KjcEVclZztKx9P_tNYW8WbHSH4OzOmypLkO2NERmjJbU-Y8cEiSQk5VM6usV1Vgf5PwRGP_ZsVvefn1B0i90NNLhWFJCidw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=A1kJ-Zw2pIDf1jdSUU_rwqKLqR9ByCGJzMjhgv1vFIIkZI0WoNMUC3RTGblaw8sAc_MuihtaRVfhn0cgGLEvF6KuNlknCEG40MzuZ6tZZoWgC84hb9Tes7SBTF769kAD2FeZrO0hskfyEBrQkHRZmltGF8uLLWNhvbw3az3LVPm8Q5x5LjBZc44qjxWPX135Scd2ncux-CrwojrXK3twDqVon5Ixtyfmt711J3TvCb03LN7L_bQnZePPf9sPB8vj3SaC8phKUlYHVU1j-LiFvwmXeKooMsJrHACGZfTkQV4iz90v0-3cIFPLtKg93wtOsueKfuHc96RMlxbvX-WldA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=A1kJ-Zw2pIDf1jdSUU_rwqKLqR9ByCGJzMjhgv1vFIIkZI0WoNMUC3RTGblaw8sAc_MuihtaRVfhn0cgGLEvF6KuNlknCEG40MzuZ6tZZoWgC84hb9Tes7SBTF769kAD2FeZrO0hskfyEBrQkHRZmltGF8uLLWNhvbw3az3LVPm8Q5x5LjBZc44qjxWPX135Scd2ncux-CrwojrXK3twDqVon5Ixtyfmt711J3TvCb03LN7L_bQnZePPf9sPB8vj3SaC8phKUlYHVU1j-LiFvwmXeKooMsJrHACGZfTkQV4iz90v0-3cIFPLtKg93wtOsueKfuHc96RMlxbvX-WldA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjJMyNWdn_fRhbZutftv2Zql4L75n7eKZ65S8fSLcGqvklCQ5ZcvJgyu4cmrVmBia_sxKK0ov-n8yu_n_pS8sKv3hKi8emFPxgoCGbaQaFrAGYFIIAba8Ho6woVb8SztmViTeAp8237O0DXithzmktfqxGEqHae6GReRYJejyx29R004Hm43_n_8TwjyOsVNqQ7v0wD_p3k23bVxYctyUfEKIOtt7NHk1x9X2gMYdzzpW3Dzs-Q-rId6LeRMWK3lAMacgsyDRgqwde0Ia4MFIS5FM8AYb98R7gpfpw0fMVmUodv4JZqX27b-UklXIGhbpIk0lzQF4aDR6LtJGkzAZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
