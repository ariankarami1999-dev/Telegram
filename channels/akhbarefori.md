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
<img src="https://cdn4.telesco.pe/file/R0QujRp0kFMGFtf6GFXynj4rVje2RDKrKsBeb3RNzUpdc3X2eJ98d2R991Ej8CwSnFNxcTHIkRoao110YM8KpDwMsdSbQ50buVGrNVxD5-hn44FWYbOrcA0yKc2Ggo_YU1RYjzJo8TG3j1C9FbnXG_2nKZFR-kJm6gk-JxQO0HuhCTR29-3V7RDsfdRqnZZ3xdIxL5T2ziIcQRcRjd9N6LhBknGb1B0Ux-BJ-93N28C-HpF6jN-a259ATY9yZhzh1IlF_Gg70nMRru1zCHv_C9SvwahXvUM3IFeFHS4V9nx7q3vCVsOw7Uo384ZLFktqSslbpccLKgixcSS7IrUsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 02:32:20</div>
<hr>

<div class="tg-post" id="msg-662110">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_cK3UdpRsF_FkLPJF9lTEUUXFSuYxPwTgbHjmTNZnOzBQccbspo649_DzLCKzxwnIZb3gRvzWeGuyYQmSramHh6ZbMeT_PFVMOrIbtPN6KbEOMSMnXFL0jRZMluukjRwymJthVsTUZLyGWx3UdvDHkqX_3fiNqlFhH2V20K3PjYPvFzjlq-MWh9930xYDvd3Dp3GbwlgmB6pf9X1J3Qktp7Ozh1gOIdU96auLkYYLM22-dU_GvhGInaqjQNJQP6j1foWDO6n1pSX9t8BfRp5jsBQ_RwBhTeIQN8jm0HijINzrGfkNgJCIdI_0yeh-REkBoLqNOhdtIXV4KzKbo9_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">《اقامت۲۴؛ باتجربه در سفر 》
✈️
🏖
تجربه‌ای از دل سال‌ها همراهی
بیش از 20 سال تجربه
بیش از یک میلیون نظر مسافران
و پشتیبانی ۲۴ ساعته
پشتوانه سفرهای شماست
رزرو آنلاین هتل، تور و پرواز
همین حالا مقصدت رو انتخاب کن:
www.eghamat24.com
www.eghamat24.com</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/akhbarefori/662110" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662109">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFs8CFUG6UwNtH47Yj82vRyYEEgSE3Di_R3gSggJdoHZzu2NifpU6uSahbVjRr4HHlEwoIL8K1T_feIEFBBOx3ZGwu3im0yaUGMto13kZZWcO7nrgScZ4PaVqLulRNK6wwlc8jVyU5PI1yTlbefD49KGMH7dW4DNc6AcWEP4XrWXoDWVMfNbRJxIofFqNzbUqJSQ6F_JhbRTyHeZMki1ed9E9uy6udAbsSXEBGmK7RrFQDcfMWOwNpBQpXBPZoUnW2nw4QbPLh9g7UVi2KaLx3Rb1Nl4x2rQvx7Xem5HmSW7mVCy0LGHiNY--a2aNpvpkxhNEL4nRXRtOJ94qLbSow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر لگویی از علیرضا بیرانوند با اشاره به بسته بودن تنگه هرمز
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/akhbarefori/662109" target="_blank">📅 01:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2srdAa-patAG5NoTMWFVX_bCTH0ifg2CrHuqqAhvJbi_kgjpfO0GxJSMxEpzKEKCO8QwZ3nDLv2Vg_MLK9IOGCUCd9Zwvf0gy2PoWdQGlH9xnVQioVwDxWBnHI-jh-gJy28YP0DfMMoWPUZLxD2lxDRhnv4wMCnk1O54fYAxRkJ8PzV4DF2oPVr64eoHTNx-shr3CRQIpcApb1v8Whu0_b-G1ovZcp0dpxOc-yBvwobi1qxKjcg_H-O5sFU11Bi3c3WDjEw6Kq0nVucc57MGA47f91pr6PlEvcmHqzL5pZNyQ-DPF1VKATgyAufqWvgK0s8L5oIg2W6FjMo8WcV-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«تاد هیکی»، فعال حقوق بشر ایرلندی:
مقاومت این تیم ایران، نماد مقاومت یک ملت است
🔹
با این ورزشکاران توسط سیاستمداران شرم‌آور واشنگتن مثل مجرمان رفتار می‌شود، اما با این حال چه در زمین و چه بیرون از آن، دوشادوش بهترین‌های جهان رقابت می‌کنند.
🔹
هرچه بیشتر [بخواهند] آنها را پایین بکشند، ایران بالاتر می‌رود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/akhbarefori/662107" target="_blank">📅 01:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeJOZtyk8OgoI0fuo15g13eSu6YrUVK1xUp3Kh1V69m-Jbs-XhQZXiXbIRp5BqqNALNCsfAx5Y5vWszL22874v3B0wUT08wBNvlWTHYCj1bBq_iYtMQyHwbeJxVZa2n-GZa3pXnn8WxZLV3IXP8_2s9NheLhutKyJmi6tYqgPj12VrViXNayh8BC6-f_ZtET4mMFRJw7hx7-AKbWImW0VyqYjkv8SLp5SKPumfd5UeM1G0im2C9asLdww05TmQiLJZTgzqD4pGNsb-XyEtpv7AWaiQ5oaUrv7Ws6RgxCX2E7OxHnYLvDpe0mAc1QjRMo-DLb-7K_H1VkazWa9LQhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ در پستی در تروث سوشال به گزارش نیویورک‌تایمز واکنش نشان داد و نوشت: «بعد از حدود ۴ ماه جنگ، چیزهای زیادی تغییر کرده است؛ از تضعیف توان نظامی و اقتصادی ایران تا باز ماندن تنگه هرمز و رشد بازارهای آمریکا.»
🔹
ترامپ همچنین نیویورک‌تایمز را به «تحریف واقعیت‌ها» متهم کرد.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/662106" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feOc5mW_OVXMTM5dkOuHObZkU9kHINq_dtcopFkaNGBr11rfY7dRDJ_Af5LbJ9zxebdVHHKOXEtDORMIZR59_AdTbOldqq2sFGyY5szpnQcb3s1g-znBlPiiOBuJedRUAMnoAfiu-eL1CwlZn72iXu5gFdsLAWOSU_aHQqv97lHpKDWYH3X9ueSyWNW_5EDQCceq9EfGAFjtga9CR9QRw6-VIX9Lm33xAI2-tJ-s6DlOXR9ffZOMNJGmqALp0BOV3aA-BfPZ1AXGThn-UtsQjm4ZnYN4HkL1Dxs2OFad7XBPhHL-YIxCnxrrMMHmstx3gl0yIW2p4eLTKUcJ_9aTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محسن رضایی: ایالات متحده بر اساس تفاهم با جمهوری اسلامی ایران، مسئول تجاوزات و اقدامات تنش‌زای رژیم صهیونیستی در لبنان است و باید پاسخگو باشد. در صورت تهدید علیه ایران، آمریکایی‌ها را پاسخگو می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/662105" target="_blank">📅 01:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662104">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrbMlbOft2n5hv219ISgLtLnV3SC25KmmR6oIgD3iRjtRhbYIwh6dVbXOo9nuDF0nN5xU0aaWVJUuniGKrUFirZ7dVIrdFKBdrPfTtGBo-nTXv9GY2RAi2bhOoVS9sW0pAgVVcWVHO1jpP7SmGbgn0a5YChEX4LEGE4jP5YrVrp3X-5Jzg1B3Y4iKidjozrlS6cqfKOfV3UAg5rN16049yIVXimOXKEU4W9ab7vO3r75MkVduItAlsOLhukq2_fSrBVwD9DeOWS315hjEcyfIP3mu-8UdiRkLuJl79V-v6VC4ZGaksgJH7w8I7qcWJHNpLkciBZIH-vDpaVfCr9b3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ما اینگونه از سرزمین‌مان محافظت می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/662104" target="_blank">📅 01:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662103">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhOEZEntHNzoFjZc_pq9wTHD39zeBRlIEd2rG6P382NuGfeagxVyJhX5uIk3iAy55-P8rtPad9rLK9rayvEwMum3a1Hyr1ZNBghpL3-7HaDvWVZzY-QcNWpkcX-oGj_NCnm2Pu2C2gUkwxIE3ocVhFSCJhXSMrEhp5XVYzeZdp5VWegZHFUbsz4CZwfrFXKMC0QfC30oSeLHWv4bZCc6AGCg2IRP4ITZywNeAEl9VADSj4j2oKPQ2XVGeDrsDLaxty4x7gW3bJkICVINcqIEfGFVLkQ4oOUBt8JhlroZXXaZDp2vZNTzFv-GohMVeAG3e6ImO4Fc9wcQexZY5BwWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استوری قایدی در واکنش به بازی فوق‌العاده بیرانوند
در بازی امشب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/662103" target="_blank">📅 01:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662102">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxcbspyvB9-Gz8y5AIjo-p4FleWCGVREIoEpOKQwpJXktDkUukN_JWMRz7RbWhp4H9-B6eyRZoI87uf-8S2kP7P318kC6F-j6tkHLcAD7qdO0HrmWCMNz2v8hMQ5cDu6WeNc54M163GPMTQkBJR1fLVuQMUcehxs4Bk9p2rcHgpiJk24AQatkzslUampcxct1xgvtC_WStMlOsfcubLuIyri-I7EFoJG7_32xzO4--ohkoizOzr0dMioNRp99tr0ZEjC2RhDr0R2_CZx3wwy-SOF5siu7IReDtXqtVzeSTJ9s8y_vCG-8sib5NfJfAY7wIZLNNH7iKWgawfW_uGW1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران چقدر شانس صعود به مرحله حذفی دارد؟
🔹
طبق صد هزار مدل شبیه‌سازی شده در معادلات جام جهانی، نتیجه برابر مصر:
🔹
در صورت برد: ۱۰۰٪ صعود
🔹
در صورت تساوی: ۹۴,۸٪ صعود
🔹
در صورت شکست: ۴,۶۶٪ صعود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/662102" target="_blank">📅 01:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662101">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
جدیدترین اخبار از مذاکرات در ژنو
/
مذاکرات چهار جانبه همچنان تعلیق است
یک منبع آگاه:
🔹
مذاکرات ایران و آمریکا در قالب چهارجانبه، حدود ساعت ۱۵ شروع شد و بعد از حدود یکساعت و نیم، برای یک وقفه نیم ساعته جهت مشورت میان هیات‌ها تعلیق شد.
🔹
اما به دلیل اظهارات تهدید آمیز و موهن ترامپ، هیات ایرانی حاضر به بازگشت به مذاکرات در قالب چهارجانبه نشد.
🔹
با وجود این، تلاش قطر و پاکستان ادامه یافت و تبادل پیام از طریق میانجی‌ها انجام شد.
🔹
تلاش میانجی‌ها همچنان ادامه دارد اما تا این لحظه به نتیجه نهایی نرسیده است. در جریان نشست چهارجانبه، هیات ایرانی صریحاً نسبت به نقض تعهدات خصوصا بند یک یادداشت تفاهم اعتراض کرد.
🔹
هیات ایرانی همچنین خواستار تسریع در ایفای تعهدات آمریکا در رابطه با آزادسازی داراییهای بلوکه شده ایران و صدور اسقاطیه‌های صدور نفت ایران شد.
🔹
در رابطه با موضوع هسته‌ای، هیات ایرانی تاکید کرد که شروع مذاکرات درباره هسته‌ای منوط به اجرای تعهدات آمریکا طبق بندهای ۱، ۴، ۱۰ و ۱۱ است./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/662101" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662100">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_bOe_A5Bum-XIhGJzEW8XJfC8YjD2THtivYQzasgfITZZkNtn-0uEfzAvXZfQ6I1A7VI1FdpDMipAwG3WAdWII58zFGcM9N2aflOZKrVGw1pyP5dMY7jDDf48Be0WVHUUcd7dpVS4YYE26CEUKrZdwSKj7uZ3TjLqUyo7rNeWN7NnOgRkqeGdQoz-jRlm9jid_xu0g-hjypdUJQxT8fm09t5oIa0Av3spz2II7GlKdOsdPzZ_F7UveUvwSZ_tqHcKM250poNDNCAQUraDRyLtOHdxg0NUIQVb37Oqnd07Kut2iR9RMBW3x-HfWWyg34Sqix2GjRi-yXgDknaT6uUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مقاومت در لس‌آنجلس
🔹
تیم ملی فوتبال ایران در دومین دیدار خود در رقابت‌های جام‌جهانی مقابل تیم پرقدرت بلژیک در لس‌آنجلس با یک بازی کاملا منطقی و دفاعی منظم و تاکتیکی به تساوی رسید و امیدها حالا برای صعود به مرحله بعد بیشتر از قبل شد.
🔹
هفتصدوهشتادودومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/662100" target="_blank">📅 01:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662099">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bdb7bca2.mp4?token=bIEPgi1gdXhWJ3THml2CWhg9KxA-MjYzPRczSvlvI53oLkNdkb9VY6l7RYFzt07frvUlEBFkLzK2TebcnQBmLGJ7_UajdUgpKuXtodN-Id1JJ-px5KXIFwYf-EED484nrdVd_e8ECJ79eKJemTHWZEOBqBmIym0DbdcVFaPDM0XmNmHzfkxm5mfns28CclPwkiStZFhIfdGx9GgByARXsim6H2cjicFwcJgFah-pBf5Do6FqQk5lYbeSbWrTH1JLbSdPBs9Bdxi3u4su6fMAdhLjiG50esebGNQycFt7P_b1TGcRaSSyjeGbdIi0s8pudLuGQOIJMLt1gXWnZn7lzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bdb7bca2.mp4?token=bIEPgi1gdXhWJ3THml2CWhg9KxA-MjYzPRczSvlvI53oLkNdkb9VY6l7RYFzt07frvUlEBFkLzK2TebcnQBmLGJ7_UajdUgpKuXtodN-Id1JJ-px5KXIFwYf-EED484nrdVd_e8ECJ79eKJemTHWZEOBqBmIym0DbdcVFaPDM0XmNmHzfkxm5mfns28CclPwkiStZFhIfdGx9GgByARXsim6H2cjicFwcJgFah-pBf5Do6FqQk5lYbeSbWrTH1JLbSdPBs9Bdxi3u4su6fMAdhLjiG50esebGNQycFt7P_b1TGcRaSSyjeGbdIi0s8pudLuGQOIJMLt1gXWnZn7lzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیندسی گراهام خطاب به مردم لبنان: کمک در راه است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/662099" target="_blank">📅 01:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662098">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/662098" target="_blank">📅 01:08 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662097">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01037f4a6e.mp4?token=ub0bGaYi0JPnjBjibO-hKsG7WbQGKBl2ZP7VN__MvTbpA1nKnRguQYY0p1n5BNY8_y2TyfK15uMUB7qb0zzAQeSzzYZsC5d1Xpqds1lYlGoVQJ5rNX1c9nt1Ht3r7Aq_cA9nVg0cajDTagtWSWiVwDr4wDZSh4VZ0LhYGxxT4ntc-c8Sa-wTLC6QH76geIYbuBsszChilCzHe4P9F8v-bqF_atkgby4aa_RqE6Lm4pGN8vclZqHbWuST3ucgIIqYPFICdOzl_UfJ88SPxILUL9HHPw8lu9hM82AZdRP8ppq9a35Wu66Bb8BLWb97uvDrah6EAcy2YRG3mICQNMxI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01037f4a6e.mp4?token=ub0bGaYi0JPnjBjibO-hKsG7WbQGKBl2ZP7VN__MvTbpA1nKnRguQYY0p1n5BNY8_y2TyfK15uMUB7qb0zzAQeSzzYZsC5d1Xpqds1lYlGoVQJ5rNX1c9nt1Ht3r7Aq_cA9nVg0cajDTagtWSWiVwDr4wDZSh4VZ0LhYGxxT4ntc-c8Sa-wTLC6QH76geIYbuBsszChilCzHe4P9F8v-bqF_atkgby4aa_RqE6Lm4pGN8vclZqHbWuST3ucgIIqYPFICdOzl_UfJ88SPxILUL9HHPw8lu9hM82AZdRP8ppq9a35Wu66Bb8BLWb97uvDrah6EAcy2YRG3mICQNMxI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمجید لوکاکو از عملکرد خیره کننده بیرانوند: او هر توپی که به سمت دروازه آمد را مهار کرد
🔹
بیرانوند هر توپی که بین تیرک‌ها می‌آمد را مهار کرد و همه آن‌ها را دفع کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/662097" target="_blank">📅 01:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwvjcGqbdSYLz3ineNXm6b15raBZ1HSRtxCjOC9D6oss_h6bwHn7R1vj3wfAUH2QxO79w50ZTuUy2rkyx22atCjhy5xRbdIvW6hx2IS8uXO-r28B9ctkEp3Uj0CcaxBC1Tpi-MLgDVzNGblI0vGvGoudlcd7XbK9cwI_bCTAWfHp3m4imG3IUjzq1jLncim4ECcfBipafv0hFhaT-1x0gztVaT6rQxGa9oL7AThc5zN7gXYEGisGgncMXq4kEs25KN-e7jXr233fUlWikZYx-mbwjeJN-0yu13nzwlSUoGDxfO6LhR7DW9EcZ6Kp45_NnMicskyl8MOYtxRO1rIqdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خاک پاک وطن! خیالت تخت
نسل آرش هنوز پا بر جاست...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662096" target="_blank">📅 01:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
لحظه انفجار در راس لفان قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/662095" target="_blank">📅 01:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzxPhs29-KA_yjkOMWI0N5rsnSQeeDL70ynYjkhhRHCfAC9xVe1K__HL4lvZRYK_8eVgDBmEGi3KZ2MIgg9dxOhFIQOAdGBy3yGRRpzEF7Kg6Z7ggKuFt50psbRtcTF1AYY-BJyLFOByavIphLAgjWVAf1kU-c_03vE9GDCVaGdaCM-51U-lhQsztgjg2hCwmN730Z246KXRIodVn7rwVC92Sh-v65FV2GBW4CPjXpgx8EhZpT20nvPSQg0KxJF0PBzYDsE3K0tTGhdkrKm49ihcTlQbBlywjUG_-PzNn6nB0CWwMbphvxdJx2tcGmOGJHToArBeMP6RPTN861ba5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست پیج معروف ۴۳۳ از عملکرد فوق العاده بیرانوند در بازی مقابل بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/662093" target="_blank">📅 00:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-Zo4yhYQFa5uZQlZ13EmplLNmvzi7rTq05Mxa-us8YZoIhGAlANZmp24ju8w-Z-RdeKzmeYBFcpZ9A77ohGK6GhHdSfcQp3Ag8dn6P90GABPJZBjWi9TUJgAyWaHHu74-8EnA0NPZTmNBDsjIla-ZJI0aN8JbWDLfbpXall_6H002sG34QsRhNb4vQGueg0QKAvbsq0ImRMk4tXv9JqXwmdT1U3Or659nSZdMDRWxQEyLVrVKsPLEgOocKxbZoiTQLwGAVMd8Gmhvw-VrNxyQ97qu-MPg_dMLWEFnMKWFyxdWpgfnzpnDfOVjnTu2sU4BCKPoinFelIFFQBgzv3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سردار آزمون به تساوی ایران و بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/662092" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FH3Jp17SxHzqELUJTuZ1aZ02sPCDLDj7qk2R-pelex6w0DhAg_qQt_xvPPWcFxCR2iaAu6cXbdxfCs499w0Wg6TSKiI-vPB6N0BvCCSCYTdvrI3UPIVgyEjECEvap1yVoKBN3mYLfDh7CIJpfp19ASUh1vkyGZFqqB1IKvNjc-RaLOGKk0Gb-5_9Onurv8XVSCt-sreYJBRnTnCs4VEdxU_x82BucWKrYwbrBrAhWxIpmZso5IIfxMAfBKJarXnQjW5uKQGe5EuTUIm3-yK9fvjBI40ATVdRcfSpIpTE2JwbN27UCLR0-6vvtqpFX1YDwnmsLiBKEm-c709WcxJrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست پیج میلیونی و معروف ترول فوتبال: تنگه‌ی هرمز بسته شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/662091" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662090">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lg3h0WbvkeEcIct7Ywq4d1wefy32Fc55UT__hCJ3F6dAC0iifsetXJI62POg580rlhlnXICmaPSO4EQ4m_YMab_s_mL6wn-THip4gyrJkTHa8-9_2oXt-QyGG3C1YuD2kGfLyUfBDF91x1cBp7UAh-Q3z3iWapIud30BzPK0yICdGVJ34OrSnOvE_MwyT4R5P0NH7vYQiI1tQP35kB8tsgPHf4hu8e6X1rwTxtYiXTIJhkMgVBW715mmbEUskBSgnUw-LOe9b4LhvUx-cLRPN0s0xetFAQQ88kjuyR2vTK5zEUUy8XUzEE08zzuXH9s-nyARLF-t8B04r3alY1Jv2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
علیرضا بیرانوند و جایزه بهترین بازیکن زمین
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/662090" target="_blank">📅 00:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662089">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b771a66ca.mp4?token=I1vZgkCQ1FeXO5tEPUq0js6p-psz0-S2RFekLnqBA0_TZfSnX_UTX7PJhEVvt8ohVcrBWq9HyXYzVAHkCoO1Y2cisX1Zrkkn9VVjdhetdrHqmCM8VJMZ56FCzI4CTUxB14ToNLY3P1KmrOX3ahaCkygUM5O2BT5Pv1P111V57GLqCKMfVVodQfH8FEXUBl7LRbQSMdKJi2BmUUJj9YA7K7QV1tXnF-SI4qYP7POhe7aH8-wrCdk-IreIVeEyJUOSz5N4naAB_nRB1dAxWgNM-OfTZOFTbx7PqbvDPuY1fKr5saOIVzOdwR8Tc3YPUCckOvepm1jMyGXDsD59LmQifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b771a66ca.mp4?token=I1vZgkCQ1FeXO5tEPUq0js6p-psz0-S2RFekLnqBA0_TZfSnX_UTX7PJhEVvt8ohVcrBWq9HyXYzVAHkCoO1Y2cisX1Zrkkn9VVjdhetdrHqmCM8VJMZ56FCzI4CTUxB14ToNLY3P1KmrOX3ahaCkygUM5O2BT5Pv1P111V57GLqCKMfVVodQfH8FEXUBl7LRbQSMdKJi2BmUUJj9YA7K7QV1tXnF-SI4qYP7POhe7aH8-wrCdk-IreIVeEyJUOSz5N4naAB_nRB1dAxWgNM-OfTZOFTbx7PqbvDPuY1fKr5saOIVzOdwR8Tc3YPUCckOvepm1jMyGXDsD59LmQifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیرانوند: اگر دقت می‌کردیم می‌توانستیم بازی را ببریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/662089" target="_blank">📅 00:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662088">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
کماندوهای آمریکایی در دانشگاه‌های کشور پیاده شدند!
«وحید جلیلی»، قائم مقام صداوسیما در امور فرهنگی:
🔹
واقعیت این است که آمریکا کماندوهایش را در همین دانشگاه‌ها پیاده کرده است. آن هم کسانی که همین امروز حقوق‌بگیر دانشگاه‌های جمهوری اسلامی هستند!
🔹
در منطق این آقایان، اگر می‌خواهی ببینی کسی خوب درس خوانده یا نه، معیارش این است که آیا تسلیم آمریکا هستی یا خیر. اینها گزاره‌هایی است که با همین صراحت و وقاحت، امروزه دارند در دانشگاه‌های کشور ترو‌یج می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/662088" target="_blank">📅 00:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvXEBrYmxQLQ31uRgijw0QZ9-7BHq7HMGASjZWBtNHB3H4ZtyWC6fSb-MdZ7z-e5nfOTS6p5H_9CXqQ9RevhxC-WmRb4n8FWEK6q-CJtZB_x8_Tu9Fh5f3b53EBDwitBOqM0WFcVOGqOjMYFCbQzGkI5rMeklQilpergs1M5jHljSpZ7kKt4jnuZIcAwTyNqqCcaq5AIX02hmvUz3FHw5RzBSafbByOJNmZtlY-QAbdt5uYieicQug4SnxkmqYTx0Lae9mEoqi-nNc6rOaQ_K64oNzLUyzoIGrGq5FBCeFWwJTm3T3fWvnH31LGrqxFfaDJnlQMmLsiRmc00tu857A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۷۳ درصد اسرائیلی‌ها ادعای نتانیاهو درباره ایران را دروغ می‌دانند
🔹
نتایج یک نظرسنجی نشان می‌دهد که حدود ۷۳ درصد از اسرائیلی‌ها، ادعاهای نتانیاهو نخست وزیر این رژیم مبنی بر کسب دستاوردهای «بزرگ» در جنگ علیه ایران را باور ندارند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/662086" target="_blank">📅 00:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
خبرگزاری دولت: ایران همچنان در محل مذاکرات سوئیس حضور دارد و رایزنی‌ها میان طرف‌ها و میانجی‌های پاکستانی و قطری ادامه دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/662085" target="_blank">📅 00:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662084">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
قلعه‌نویی: از تعویض های خودم راضی نبودم، حتی شانس آوردیم بعد از ۱۰ نفره شدن بازی را نباختیم
🔹
فوتبال همین است، مثل بازی قبل تعویض‌ها جواب می‌دهد ولی آنهایی که در این بازی وارد زمین شدند توقع ما را برآورده نکردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/662084" target="_blank">📅 00:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662083">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0cYe82tL22oNqHsTj9--ofPtx5j86xLtGZ3tf-RrI_dDAYrGYcHDESJSlMRzXirWRGUDQx9Nim-_2bWzhlBHDnYSvlA3ut5XuS5MgDYTq2Yed_gZNNGuxJ744d89EfGoifQghX8qMZJWrpzbvvzA_E2RoDTzEFIGuBa57p-IEh0DRhhYEM7CQ4oOb7aBUl2IuK2T2zQpmKzeS5bZOSaRmCTqlMskxr6ATbUSpvNNw6H5NcY50NEjgtD6WNFI8dIQfauas7i3y1wbISGPLMILk07w6eopdjtmCFRiyfEmGGgghcC1jDhMgQ7o8Ehtsz8B2WJ9uoBJ0tZDtNTCEgOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی بلژیک برای دومین بار در تاریخ خودش نتونست در دو بازی اولش در جام جهانی حتی یک گل توسط بازیکنانش به ثمر برسونه؛ اتفاقی که آخرین بار در سال ۱۹۳٠ رخ داده بود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/662083" target="_blank">📅 00:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662082">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLDlwdsKanP-ZtVSMGjJw62BfpmPdUmeoReR82ny8NWLvqFWIhRaLTOe9g6cDs5efxUhVFd5o-N7Wmm_cHMnNQDQS5AAg8ofRC-8z_6ekvvCWSWaKLPQs6mkM8Eg9768KruLvWHofss-PlfQ13j_j9txoWJNQ5kRkvpT1n7FCrPKFKRtfyUbdq2iojeqytwoRW77Tk1cIu7XmT0qRMWwmaxd_sJVYStJsziDY0vyrDXS-C98Kce7RWLW9nqMhCGKOtq5Dp8SOB9gaMvem0zdcjVILIj6m5AvQVFXHnix4angpbCUv6UIznbBxNGpy5eYDaAWKOOII7D8FC-ibWrUrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمرات بازیکنان ایران و بلژیک پس از پایان بازی از نگاه هواسکورد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/662082" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662081">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9657e5566.mp4?token=vxvg8oPqLdp0olBisZqPYYCzB4KNguR6fZN2c8fWBnmeWLJAbPHww48D8RLOW2RO2cznnRF8uPOnkNfkm0vCllBV3oqTYdxbdRB1mRiFzb3-fDAKi9297Fsrv9pdk3NDC97InZuNj3X3-gKHtmKrRqDk9dZqX8QXreujZMa2aKtq9_Ph5w_kuHCtUDhBE-pIfgG4fwpwMX_hY7Ey0LuxD6BzYXA387yteUKqIKzWi1CVm7DcEPvxtzz-hqItBRy-OOgf4PFR3-9hJXpD-O-vnJN04Nctw72EYysGX2buCKxqZ3Dh9taGg9GHhDw7yy1ZHUnGqywQD4KCK47BJFE8pRl3ZrqvoLXMd2oN4vH6TlPtqMEW3V6cldE6dULimN20NDo69WpiHy5OCAR9tU8jmi0oz7bNmgK-o29fZY2E5ojYX7vFEGpY_4K32wCKaCaRMky3w6Fn6EPGutDrmp3L-0OlMXEVvBpaRw-TeteWD3EeXaqwTSBGk3BmC2UxVi8acciCuS_sJyXgc8Nw8NeRaZADppZiX8gCZh1bgIoSPuB9Hbjm2TctFcWi4VJOCv0wBQ3wlyCg0SMz0zFzPnv4ff9fJrMrgplTOQ44Dx1VexCDQU1TXTSwQkWkDLKCBtGejSYUVxqSvCfqsMudn154wI_A6bmlP-xq7I_ARHFpjdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9657e5566.mp4?token=vxvg8oPqLdp0olBisZqPYYCzB4KNguR6fZN2c8fWBnmeWLJAbPHww48D8RLOW2RO2cznnRF8uPOnkNfkm0vCllBV3oqTYdxbdRB1mRiFzb3-fDAKi9297Fsrv9pdk3NDC97InZuNj3X3-gKHtmKrRqDk9dZqX8QXreujZMa2aKtq9_Ph5w_kuHCtUDhBE-pIfgG4fwpwMX_hY7Ey0LuxD6BzYXA387yteUKqIKzWi1CVm7DcEPvxtzz-hqItBRy-OOgf4PFR3-9hJXpD-O-vnJN04Nctw72EYysGX2buCKxqZ3Dh9taGg9GHhDw7yy1ZHUnGqywQD4KCK47BJFE8pRl3ZrqvoLXMd2oN4vH6TlPtqMEW3V6cldE6dULimN20NDo69WpiHy5OCAR9tU8jmi0oz7bNmgK-o29fZY2E5ojYX7vFEGpY_4K32wCKaCaRMky3w6Fn6EPGutDrmp3L-0OlMXEVvBpaRw-TeteWD3EeXaqwTSBGk3BmC2UxVi8acciCuS_sJyXgc8Nw8NeRaZADppZiX8gCZh1bgIoSPuB9Hbjm2TctFcWi4VJOCv0wBQ3wlyCg0SMz0zFzPnv4ff9fJrMrgplTOQ44Dx1VexCDQU1TXTSwQkWkDLKCBtGejSYUVxqSvCfqsMudn154wI_A6bmlP-xq7I_ARHFpjdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای تماشاگران بعد از بازی و تشکر ملی‌پوشان از آن‌ها
/خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/662081" target="_blank">📅 00:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662079">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6051968a50.mp4?token=N2v3K--9RBYWdwn7DRgGnCbMEeLc9lODqjCh2qsSL2J3vmgFPi1eD4AfZ2dnMgDWZzu8-Ny7SDah0PI1WhhQDu5V5Uhxm8QmWU0vW9Amuolnkm-kGTkmjKEVJu1Td0cUxxLm2XnUY8EcqETucGbBM8MqWye4YNdOmYZml3dwC0FjFzCwoeKDcj_9U6wVebtAfyeeWrgffJDXItQwsIJaup5EkLaRx8iUiEIQ6XucEFPayWnibCyBtcx93wY8gX6kIi4HzejS4U5C6N5SFTUTHsdqHRlUCP7OKBV5ezmqKq5i1lj6huaokUf1mCnRLgFKXSz3zaEQHk_j6Ms-T3ptEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6051968a50.mp4?token=N2v3K--9RBYWdwn7DRgGnCbMEeLc9lODqjCh2qsSL2J3vmgFPi1eD4AfZ2dnMgDWZzu8-Ny7SDah0PI1WhhQDu5V5Uhxm8QmWU0vW9Amuolnkm-kGTkmjKEVJu1Td0cUxxLm2XnUY8EcqETucGbBM8MqWye4YNdOmYZml3dwC0FjFzCwoeKDcj_9U6wVebtAfyeeWrgffJDXItQwsIJaup5EkLaRx8iUiEIQ6XucEFPayWnibCyBtcx93wY8gX6kIi4HzejS4U5C6N5SFTUTHsdqHRlUCP7OKBV5ezmqKq5i1lj6huaokUf1mCnRLgFKXSz3zaEQHk_j6Ms-T3ptEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماکان نبودی ببینی ما با بلژیک تیم دهم جهان مساوی کردیم. ماکان نبودی ببینی ما خیلی خوب بازی کردیم. همه کار کردن ما ببازیم ولی نباختیم
کاش بودی ماکان...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/662079" target="_blank">📅 00:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662078">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ff0f76ee0.mp4?token=ga6turcPhaktxjbk6wWVl9S9qBLAQGOmH3fLgdom0ZkJRqaEKzGhXKvM7RKDjM4yxEEThTkldIefhdMq42QWdTv-vS_8rzJ9RRCrwVKUba784cp_Tv9ufGmcPiURB4QO3M0yLiF9IFrfsLumhC9Aj0HMq7aVIoE1VkAmpYQ2empJw3R5NGkx-aZcccmMB5ELbokfguE6SPJEzAuR2dPbCQW57ONOcWntP2bhUtXWu18E85T7jIDn-kiC321U9sFP_jf_o_hMYm9s2v7IrlyVOTsAVPpES3oNBLPEQOFmXjNqx1yjkpk-Yvo5zS2OpZhyanCA_fEl-ceXh2-Wb5EbtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ff0f76ee0.mp4?token=ga6turcPhaktxjbk6wWVl9S9qBLAQGOmH3fLgdom0ZkJRqaEKzGhXKvM7RKDjM4yxEEThTkldIefhdMq42QWdTv-vS_8rzJ9RRCrwVKUba784cp_Tv9ufGmcPiURB4QO3M0yLiF9IFrfsLumhC9Aj0HMq7aVIoE1VkAmpYQ2empJw3R5NGkx-aZcccmMB5ELbokfguE6SPJEzAuR2dPbCQW57ONOcWntP2bhUtXWu18E85T7jIDn-kiC321U9sFP_jf_o_hMYm9s2v7IrlyVOTsAVPpES3oNBLPEQOFmXjNqx1yjkpk-Yvo5zS2OpZhyanCA_fEl-ceXh2-Wb5EbtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاربران فضای مجازی این ویدیو را با کپشن «عادی‌ترین واکنش بیرانوند در بازی امشب» منتشر می‌کنند!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/662078" target="_blank">📅 00:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662077">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW_lhgWhFCzotEE8cetvDQm49tM1OMEVFh_HO_FX0ek15dSlXfx3P-hmI9eRGDeg5RULXQ9-71NSB9r1CS8ZLDjt4zS64FVL5YHcSMAmHANwi4oVyl60LATHxIZaUwcX1eptsschsSjpXbmh2Dp6DTBnwj2hZSVhW_mia2BOkUeCXzlIGLfrsKfo1KNJjQgwgIU-KjGWYjV0L-MQJSXwwk17VeG2aYJN_-SxKFD3-d1Ssm2fGKEbgI73yywcUFzWDleLrM8QrcLUGmpptRi61eb8FpTsUymq8YqmNsAu_61Fj9Y-xX1YEBHb0krwdiAtKTiU-NmedS8M6Q0h1BUrcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا بیرانوند با عملکرد بی نظیری که داشت بهترین بازیکن زمین شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/662077" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662076">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOHusbyLZ-ozJKBKQbgyM1ajOiGmBhImobrG7IN_6xhr_GwN80tcJVe-aC0JdqoG8bSsvwlfFl7QCgP8ngwr9a4NvwBRU7flk6J5qqi8fTOZ7enMGZNqSw1EQWeC4L3UfAAGGyAUsEeHAg5v50QSu4_u96lNhRB7-gTogUwmdcpqMYamhnds5Gu-TkiGJ6N-Dwi5Bc11abRmf811rh8yz6-Cu1hvXxPjey6W0l-kSFzorxpGIxIj9m58KmkyIkpWE63xYBOvqNYZcYRQW458A4PBNwMeun4Do77UByuy4eZqdvDwZskFGOV9C_VLcrjgEFOsivc1GyyiDH7UuUBpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایران صدر نشین گروه G
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/662076" target="_blank">📅 00:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662075">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfyLpLR2FxQT1zKlwKsl1GAKvGbFky5JW8gZpuCuoxJ5hkTKwA72SanzsDiKojfC6aqkqEyjCOlpYvlo6wh22X98uPpDHKzr-clPpfYPD89Tv09wPiqK9K8ymt7VFLfRT_mBnf2K2LdQM72u00TmnPadIl8U0obAaOqHOSi1x0smh4TDh-9rTs8PLRT9DtZTyadTmsteHwkQa53Hr_EDy-3OnY2-lIKgKqwJUhmvQpd7lGsyKBhsBnY2wShaEX91Neo8-LHHcR-ggyixGqewzVtLLIUSYPNal9ze-JIBKxyLwFjzGpBTzmJfjTJgCIqBTfxIjvvH38sHLHW1HK-PTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا بیرانوند با عملکرد بی نظیری که داشت بهترین بازیکن زمین شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/662075" target="_blank">📅 00:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662074">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlNa06W0rGiB5giNqXcfW9Cn9iz4TYthi6d1klrRQsP74t27AT7UZovwSZOtRZAdFGMXcUpn85QNGbKVHoWeSRvP9y8Vf1rHr-Xhvy-mwrnjAIIZvwVjNRu1tpGZFMTxhjXYcVT9SDoESvtHpN0VCS5BwoA-p2H3M4C0I1Y1G40DMFIdBA5cyxDL6wOzKsR2KzB-5yeKpkwnB5b0IQhuh6ELsnl4YENJ8IE2Vb5970wykBNYQk_vWO3gDwfSIondaTpKtN8hoHA4Xl2Y9FszI6kzeYxmz9u7TXA2nHLPqg3bufFS4e4QSgp86czfEFiOAWzF6D8RbNRhce6231Niyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران از بلژیک امتیاز گرفت
🔹
تیم ملی ایران در دومین دیدار از جام جهانی ۲۰۲۶ مقابل تیم ملی بلژیک به تساوی بدون گل رسید.
🔹
تیم ملی ایران با این تساوی ۲ امتیازی شد تا همچنان شانس صعود به مرحله حذفی را داشته باشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/662074" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662073">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایران ۰_۰ بلژیک</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/662073" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662072">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">تمام</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/662072" target="_blank">📅 00:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662071">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک دقیقه تا پایان</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/662071" target="_blank">📅 00:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662070">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سرعت بازی به شدت بالا رفته در دقایق پایانی</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/662070" target="_blank">📅 00:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662069">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">۵ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/662069" target="_blank">📅 00:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662068">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پایان ۹۰ دقیقه</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/662068" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662067">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
دیپلمات آمریکایی: هر چهار طرف از روند مذاکرات راضی هستند
رسانه آمریکایی-صهیونیستی آکسیوس به نقل از یک دیپلمات آمریکایی
مدعی شد:
🔹
مذاکرات با ایران صبح یکشنبه آغاز شد و تقریباً بدون وقفه در قالب‌های مختلف ادامه یافت.
🔹
یکی از موضوعات اصلی بحث، سازوکارهای جلوگیری از اصطکاک و اجرای آتش‌بس در لبنان است.
🔹
ما درباره تنگه هرمز و اظهارات اخیر تهران در مورد احتمال بسته شدن آن با ایران و میانجیگران گفت‌وگو کردیم.
🔹
ما به روشنی گفته‌ایم که می‌خواهیم از باز ماندن کامل تنگه هرمز اطمینان حاصل کنیم.
🔹
ما در موضوع تنگه هرمز پیشرفت خوبی داشته‌ایم.
🔹
ما در مذاکرات روز یکشنبه درباره همه عناصر توافق هسته‌ای بحث کردیم.
🔹
ما مذاکرات مفیدی در مورد سازوکارهای اجرای مفاد یادداشت تفاهم با ایران داشتیم.
🔹
ما در مورد طرحی برای ادامه مذاکرات در سطح رهبری ارشد و تیم‌های فنی بحث کردیم.
🔹
میانجیگران پاکستانی و قطری به هر دو طرف کمک می‌کنند تا بر اختلافات و مشکلات غلبه کنند.
🔹
هر چهار طرف از روند مذاکرات راضی هستند.
🔹
ما احساس می‌کنیم که دور اول مذاکرات، زمینه لازم را برای اعتمادسازی در مرحله بعدی فراهم می‌کند.
🔹
انتظار می‌رود مذاکرات سیاسی سطح بالا روز دوشنبه پایان یابد.
🔹
مذاکرات بین تیم‌های فنی ادامه خواهد یافت و آنها احتمالاً برای ادامه کار خود در سوئیس باقی خواهند ماند./جماران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/662067" target="_blank">📅 00:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662066">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چه می‌کنه این علیرضا بیرانوند
بهترین زمین بوده با اختلاف</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/662066" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662065">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcjTTv3Fa_4tAAgZjnwOlWPuo1Mz8hXDuq6zFS2TMl1NQSf9KEZ_46I0eAC4Ief1LZF2UHVe9Ec04riplKGtFLyNg1yAui7IcgjicZx-nUPyXnq6QbpoYOaGL6AhQGWFh2qIKcX-plj4B6G0909yBGoxdamhw9Guj5Ba8wup3sI9-NWu2CFsTjrM_HVAeYwerUUUSmv22FkvmHkjAxqIjC8dmwv_5PynI9P88enCm4JGzTIMSkCH8av8tjCmCGfuLOLAKY9e6j-n_3hG779wTKi-N2v9jxRjW8N-QO4fSvNmpJpUlbvclkeJuWWU63RaCUk8Vw42GAZqPEvpXxKZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تقابل در توافق
🔹
مذاکرات ایران و آمریکا امروز در ژنو سوئیس با میانجی‌گری قطر و پاکستان برگزار شد. بر اساس گزارش‌های منتشرشده، بخش عمده گفت‌وگوها بر موضوع نقض تعهدات توسط امریکا در پی حمله اسرائیل به لبنان معطوف شد. تهدیدات ترامپ همزمان با این مذاکرات اما با واکنش قاطع هیئت ایرانی مواجه شد و فضای مذاکرات را تحت تأثیر قرار داد. در نتیجه، گفت‌وگوها به شکل مستقیم ادامه نیافت و تبادل مواضع و پیام‌ها از طریق میانجی‌ها دنبال شد تا به طرف آمریکایی ثابت شود که ایران زیر فشار مذاکره نمی‌کند.
🔹
هفتصدوهشتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/662065" target="_blank">📅 00:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662064">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd336ae7ba.mp4?token=ZGeklZZTRPIhowcWnZ_-Iw0-fB5xJy9Rmxc0RB2BjR80SYhMoJCmkGug9LRdfRB6AbkZlRs8cQsUpP4eFAWL9ikWaP0yEfq9oxZ7WZXwVscgdk6riCI9IVSjORPcAkmMS-u74_QL4_bIjtdICVvCiJuDxiVXDEdLS-cR9VdgE0SWk4zlui-8b_7L2uXEUlkNS015nc_zMrIKBSuwiwNOQ7gi_rc7lhgE-hegHUMIy5apPD7CW9s-RvGvup6nxP63x3e7b8OjJFt8czAACxsMTye7PBpimYNrpH57Hlaa5OV-rDqueOjIG0tvm9Usgc_DVaO4QQx8X-cQlbw2kOZgVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd336ae7ba.mp4?token=ZGeklZZTRPIhowcWnZ_-Iw0-fB5xJy9Rmxc0RB2BjR80SYhMoJCmkGug9LRdfRB6AbkZlRs8cQsUpP4eFAWL9ikWaP0yEfq9oxZ7WZXwVscgdk6riCI9IVSjORPcAkmMS-u74_QL4_bIjtdICVvCiJuDxiVXDEdLS-cR9VdgE0SWk4zlui-8b_7L2uXEUlkNS015nc_zMrIKBSuwiwNOQ7gi_rc7lhgE-hegHUMIy5apPD7CW9s-RvGvup6nxP63x3e7b8OjJFt8czAACxsMTye7PBpimYNrpH57Hlaa5OV-rDqueOjIG0tvm9Usgc_DVaO4QQx8X-cQlbw2kOZgVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش تک نفره جلوی بلژیکی‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/662064" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662063">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/272dc78b3b.mp4?token=jtcB5q7Pbhf22NP3DoQqvnnsbfASmnJJGebwk84O9gVkc7jF0CIdTxQEeE6QaR3IZ6K1U61H167JXmKVuAFuIx011C_-NEli1foUMf-nFIwLkL21BjB6HHE7sYmO0k4niVjen6k9hNsAvXlz10O1l_Vq_uvxI9yWKBs0mo6AUwVrY3F84ku7OSShSHr1GQnofD00QZ1ytrqDXlAfveT5hRJnWBSSSsWaknOCeasekfU0576xNFB3ovXEN1eLVQ6tCSVZSu2YzoICxqvQmaWlIy9PE7djBqjS-VcefmarU_ysPVWNJHpQpRSapmhkA4uaLZs5YxJ542u4Gpy_tIFqtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/272dc78b3b.mp4?token=jtcB5q7Pbhf22NP3DoQqvnnsbfASmnJJGebwk84O9gVkc7jF0CIdTxQEeE6QaR3IZ6K1U61H167JXmKVuAFuIx011C_-NEli1foUMf-nFIwLkL21BjB6HHE7sYmO0k4niVjen6k9hNsAvXlz10O1l_Vq_uvxI9yWKBs0mo6AUwVrY3F84ku7OSShSHr1GQnofD00QZ1ytrqDXlAfveT5hRJnWBSSSsWaknOCeasekfU0576xNFB3ovXEN1eLVQ6tCSVZSu2YzoICxqvQmaWlIy9PE7djBqjS-VcefmarU_ysPVWNJHpQpRSapmhkA4uaLZs5YxJ542u4Gpy_tIFqtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و بازم علیرضا بیرانوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/662063" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662062">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حسین زاده به جای عزت‌اللهی</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/662062" target="_blank">📅 00:20 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662061">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1I_KTfAZX94rd_iVKBaBE3h8a8LPbQblLo14Rn1K3of7X41kfvF8HyNmX5ne1OKky5TfrCcSfORyeC8_G4b1LKZaHqwud4LOILNbzz561hxxCQf1rrsHjw588oXnWRjy1s7ywrgvP9cIuXEDUeXxPD51WNRj5jwETJB4cbisovrV7AnbfZvaNZwFvTVWdJ5RbKaAuQEcUuicE_U45r71cfPR1fu75ru-xp8zRjBajffz_QIvmVqJoCrlFdRcKJPHe5l7Uod-KGcNESycklgsObAA8dfkkqf-DQVi200TH0BCpz84HOMXED4djvdMDZSFgQmHcKDICEY0ZqXGmsRJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمجید رسانه تاچ‌لاین انگلیس از دروازه‌بان تیم ملی ایران: بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/662061" target="_blank">📅 00:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662057">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbna88WARwlWd8r-5n3vu6qPsPksZoMak8Ocgvko0Jh00ANA29xBAaIMbl2CkAEz6SfP46XzoCksIqPOAAmAQXjLGMNbaLjj_xwowzVz4_IR2AZlypJ9sskznPgEe6cIWkX98uKvy2_ozgUWu89cS8Y5jPG-vqDW2cCV_1QO332pIo5RouAIoFEN_AhuPuSoL6YIRRkGM0Dj4Q6hX5X8g8KUm7SKB_fArLYpVAgcqG1aEekFATSyT0QKOygnnkYrJ813zOiOQeWN9tPGfUx2S23EMHU4KaH4hPpwRS3TdjncEIWVRGi0rzb42uSezbkdW69rPoVNZRCluJTSsgSQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1M7GKaZz1s87ROZtm6dYSVR0Vje9j2s_6bYVheuuTclxV-7Du65dRj9xopT9Pg3jFCN1-OGdTHgtTzl1RE61U1mzdhmK7wP3QMJzf6a2sgxNLZaStnOsnNhyWjyDT_Tea2jhLV20QVZ0Yl1cl-T4K0d_PcaBfx35GJCoJgSIisz-rsF7nCLaQJLp_8mnxAgjI1j5ysp4R6nsOk_1lUxQ7nmhvXMdeIQFp3DAeLuMVoxZDWw-GtuFPD0dN56QPM4yOKwG-E8Zo5MbIyF93lM3PkA8j9ASo850BRukOyExL2cVNc2qmpAMS6C1z0y4UdvimEvRnmyNKPMML7zPh17nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_A2X7NclBDD6tejv_hRqQduTQZZp1d1QHZNfPYf761fZJbWtbMjQL1M3GDcDs95Th89Fb50OMvR-BUTvDO21JJQp26RtMFnkcUFIPrX7eKGTgHKOX72AXLbTPP_CW3T2NGvT1w2ZciQRySIXJsjkJd4JOSdbM9Co5u4Mo1VLoiwV-3E70l3xznVHcLL2RpSLCUijtA_LbJ_CuR5q7BYhiD7okGqHnYYKCMT24wtukYBt4hmFAY4Bueo07v5QBVDhQny6e7IulGPcAzYjQHWeBcJVvh9mSwaE90W3v16HZeOP6P2vAWN16hQEhWpUNVYOMBszVtEW0V0pDoDRxahzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boAUvqPWmTarIqvzpQB3KombPkEMfzGnQd7d2uL46wwUpKrq5paFTEWBhvDwsvEV6cCBaE2TtSWFgJ_0zzqYHiGNrCUtvr1Wr7IadKCnEcZU-jtQJiuCkU9Yh8OU3mpt2pQi94w5XMhXzgyZYoGzHx2enPL_82VkBrbAUr4UX2YEd_v-T-PaUSRQ0z5Np8_lUk0jmdKr12ufL2u8lxiRjxF4vgwZUG01q7o1RKhHEfgLbtz9U8gWXWmcuzhGsuxNkwEm2Hsu-X4_mmHrXDk9atOAK0NSJg0zkmrS2yAb1tM3E3-nZSG7Hz_qwmqeYR2gLr6pqnV6ZJITGGQwopXInQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
قاب ماندگار فوتبال ایران؛
واکنش بیلچرریپورت به سوپرسیو بیرانوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/662057" target="_blank">📅 00:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662056">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403ef823ee.mp4?token=jfu61GzRKVqZyIb_8gA48idfLTKTHkOKK-PSjd-gcUatU_TATJ5NvrsDZbQvoDqk7lEta04upouHRCWqMlJ7tq-msXlx1b42MQNohJRxliobjIEo-5UrnNVVw_vkJd82Eanef9YLxXfiMK-NmYFu2JYjH1Z1gPbuKbunMO5Czgf5aKDqaICytNJLbGIIIpluzO70zm6SoEzXu6zuqcEEeplnUaUZrmLboJ--eyvfJR9XR96d7G-cPE6MssxGGi87aepg5xrErehCzDvh3pCM5156zBRHHbp3YIbkIaiQ9bkWkcn9gzhWszIUKyV1EraucFTuJ0k4ho8dcgSszVALFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403ef823ee.mp4?token=jfu61GzRKVqZyIb_8gA48idfLTKTHkOKK-PSjd-gcUatU_TATJ5NvrsDZbQvoDqk7lEta04upouHRCWqMlJ7tq-msXlx1b42MQNohJRxliobjIEo-5UrnNVVw_vkJd82Eanef9YLxXfiMK-NmYFu2JYjH1Z1gPbuKbunMO5Czgf5aKDqaICytNJLbGIIIpluzO70zm6SoEzXu6zuqcEEeplnUaUZrmLboJ--eyvfJR9XR96d7G-cPE6MssxGGi87aepg5xrErehCzDvh3pCM5156zBRHHbp3YIbkIaiQ9bkWkcn9gzhWszIUKyV1EraucFTuJ0k4ho8dcgSszVALFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیو کورتوا مانع گلزنی ایران شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/662056" target="_blank">📅 00:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662055">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">۱۰ دقیقه تا پایان ۹۰ دقیقه</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/662055" target="_blank">📅 00:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662054">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aszrXOHDKd0btO0XJ5NGxlQQYplE4MgmD_yoc531sn86eR86CN-7Hru5OQJTQquMHG_8rB54d_hA99UbOH2GCM3VtqgJbVOCXFIpLag6rrMPCIBUFcvF1jYJM_sFaWtBO6ZCODlqbeSImddNhFFyxPnOd3N-xmlL4KAIPZ-J51IGNftAIOZAVr3woNBOrdb2soh5GQEGAnkhKyMWGebvDtmad-zt57lNWuIcocAvN5uIT0we46Zg6gzsFlDegUmaP5VarcjmUUdrb-xnOjGqTiZpy__wk1PZN370v0Uqjn-3z4YxEfn9MNj5gqXNxP4QNU8dsLNSjn4NOi22y_mRlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا اینجای کار، بیرانوند بهترین بازیکن زمینه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/662054" target="_blank">📅 00:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662053">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnSK4iqCLpubFmByoIiiZ4mMt2HD7rDsGMVKXtKkHTqj0wqOhWmXpj9NXodfx00GmwyFHTpuS7h39HVZI5AIFaXpC8u_t8SvP76h1aSjnZMzfOMrv_Uyi2pE71L8_clKRmOU8pC22oZ3DERP0h8rzY-t8_d5TOpz2-HkA8JNdGhE1NmDxC9Ion6bwBcU8xcEooqJ6VzVBCz002Jw8XrL5UIH_WTDOIQ4s_rGlhkkFkSTP18i8mtJjw69TrnsNoyW_x-RbVKfhU8y8ilY8PkZyjlYIIWG_xC-s6YjDws1h1fQnQw1KlvJxbJqs2nxBcg-wtoQ3eZHzMzK5pdN4ghe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازتاب سوپرسیو محشر بیرانوند در رسانه‌های معتبر ورزشی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/662053" target="_blank">📅 00:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662052">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
نبیه بری: عقب‌نشینی اسرائیل اولویت ملی است/ اسرائیل مسئول نقض آتش‌بس است
رئیس پارلمان لبنان:
🔹
حزب‌الله به آتش‌بس پایبند است و این اسرائیل است که آن را نقض می‌کند.
🔹
پایداری این آتش‌بس به پایبندی اسرائیل و در مقابل، تعهد حزب‌الله بستگی دارد؛ چرا که مذاکره تحت فشار و تهدید آتش ممکن نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/662052" target="_blank">📅 00:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662051">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bfe3e593b.mp4?token=I1AcXWi-J3leYvKkucByl2vu1BKX5-G9csWoBdRhgGzajwqxC7T9tO9Ls9aqASZKVesRvT-ksVx7O5VdORES0tqYDNycHGzjPwh5xyAU1_JEz1N8C4aONHtxvR6UU0MAcUsNUhaVimvSFd-db9h4DxNOiHAjsMnLkDxbOV2l4oeNYiJJwsHe7tXKfzYpkwnBLhagiDFh33ufkZj7zzORwKMeObrpriN4sQ3VpgqkSQz_-6VtFiRSwokqduYLmMmY9UlC_799NKnXb9aZacl_2CNrdDZCWJhSJIYhPFo7ZuM3kO6N7vNn1m8vuEd2z0En84hZaZF9MLOmrzuCG74_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bfe3e593b.mp4?token=I1AcXWi-J3leYvKkucByl2vu1BKX5-G9csWoBdRhgGzajwqxC7T9tO9Ls9aqASZKVesRvT-ksVx7O5VdORES0tqYDNycHGzjPwh5xyAU1_JEz1N8C4aONHtxvR6UU0MAcUsNUhaVimvSFd-db9h4DxNOiHAjsMnLkDxbOV2l4oeNYiJJwsHe7tXKfzYpkwnBLhagiDFh33ufkZj7zzORwKMeObrpriN4sQ3VpgqkSQz_-6VtFiRSwokqduYLmMmY9UlC_799NKnXb9aZacl_2CNrdDZCWJhSJIYhPFo7ZuM3kO6N7vNn1m8vuEd2z0En84hZaZF9MLOmrzuCG74_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش ها حاکی از آن است که انفجار در صنایع گاز در قطر رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/662051" target="_blank">📅 00:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662050">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک دیپلمات آمریکایی: گفتگوهای تیم‌های فنی ادامه خواهد یافت و احتمالاً برای پیگیری فعالیت‌های خود در سوئیس باقی خواهند ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/662050" target="_blank">📅 00:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662049">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
نتانیاهو: به من گفتند وارد رفح نشو، شدم؛ گفتند به حزب‌الله حمله نکن، ما به حزب‌الله حمله کردیم، گفتند با ایران مقابله نکن، ما با ایران مقابله کردیم. من نماینده منافع اسرائیل هستم، نه آمریکا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/662049" target="_blank">📅 00:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662048">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1461007c.mp4?token=TT34IYVWcx-ifm3UDZeBtJa3GV_7xwi1Cq343vUgn3L1OaLnONSvsULqqIJU6lEG5jHaLOMY15BtbOg4Hors5dRBQ_uudX4DtA5yKIcneudM5pcAIeaIno1uoHzu11R-jLNy5SxcWsImIAxVr2vnJ8lBI3jBayHO5B1jV7-vswYPLsVIEj17aOrtDlsV6zf2V_U9nq8zWMinEkv7TWKKusH13aXhCtZ6aRduamEqXvgd3dUhTExu3tCxTwBgzfbdOomtTEsLRz69jRelYXLn3lys18M0Prd8Uq_rXA61_59TIXGS8nQDBzz2LMOJ2ineqdgzkdeoSyF_LtZzXmh2qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1461007c.mp4?token=TT34IYVWcx-ifm3UDZeBtJa3GV_7xwi1Cq343vUgn3L1OaLnONSvsULqqIJU6lEG5jHaLOMY15BtbOg4Hors5dRBQ_uudX4DtA5yKIcneudM5pcAIeaIno1uoHzu11R-jLNy5SxcWsImIAxVr2vnJ8lBI3jBayHO5B1jV7-vswYPLsVIEj17aOrtDlsV6zf2V_U9nq8zWMinEkv7TWKKusH13aXhCtZ6aRduamEqXvgd3dUhTExu3tCxTwBgzfbdOomtTEsLRz69jRelYXLn3lys18M0Prd8Uq_rXA61_59TIXGS8nQDBzz2LMOJ2ineqdgzkdeoSyF_LtZzXmh2qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرصت‌طلبی طارمی، اخراج انگوی و ۱۰ نفره شدن بلژیک
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/662048" target="_blank">📅 00:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662046">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کارت قرمز برای بلژیک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/662046" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662045">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
الحدث به نقل از منابع آگاه: بیانیه مشترک آمریکا، قطر، پاکستان و ایران درباره مذاکرات تا دقایقی دیگر منتشر خواهد شد. / انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/662045" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662044">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترابی و میلاد محمدی به جای محبی و حاج صفی به بازی اومدن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/662044" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662043">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eb93eef74.mp4?token=ivv_5UIXMAx1BEd1-607QZhL9VwIkEz_Bu6DiQfdjYvhIK98J5rJ5MaDUca3rX5NB8g_IB2o1Fgqtew_FqTwqcubcTUU4hAWPYzrybAF2-xQATBx4HKq-QS3ERrIGJJYSTPED39pBERlxtfErNaRVmdRAz2aJ08cTwJESkRCTimCWcisolT2AUktj-Lf3QFbeMkt1uxxe82JpgiXGyfl-NE8j43mV6-MGOUjPTPCMBeb032inc_3oTh34MxcQ6916cc31ikI-9XcMkY41tkfv6VvsxJEuG9n32-eEfRvcg29VHl2pLN4HcqS3GeER0Znv1UQnZlJFbDR_ZM1WliKaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eb93eef74.mp4?token=ivv_5UIXMAx1BEd1-607QZhL9VwIkEz_Bu6DiQfdjYvhIK98J5rJ5MaDUca3rX5NB8g_IB2o1Fgqtew_FqTwqcubcTUU4hAWPYzrybAF2-xQATBx4HKq-QS3ERrIGJJYSTPED39pBERlxtfErNaRVmdRAz2aJ08cTwJESkRCTimCWcisolT2AUktj-Lf3QFbeMkt1uxxe82JpgiXGyfl-NE8j43mV6-MGOUjPTPCMBeb032inc_3oTh34MxcQ6916cc31ikI-9XcMkY41tkfv6VvsxJEuG9n32-eEfRvcg29VHl2pLN4HcqS3GeER0Znv1UQnZlJFbDR_ZM1WliKaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باز هم دفع خوب بیرانوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/662043" target="_blank">📅 00:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662042">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfjA8v3DqR72e1O9NstlX3ex7zgkb4S2rNRi9qtNDZaa59XzPK0VXXDqgy-b_lixIYQY_J6wL_0vOcra4JbLQwgtHCM1ybdcTNa7NXXPABvb-YECbHVCb8Qn5ClxoIi31t_R6mvgD_HWVuy6xw4h0o8oFAeVV27nookvD3TR1DB1BrYRf8ChuVVwoItTmFbhadnEpsXIpcoh12JbetzA9EJHgYW2FD4pyzzH4oOwe1u5J72SfFg74dAxEH2AskoCgd00hd-JqPxX0QbrhiSJYVz3xrnImZJNlDKxHaQfHa_n5h9xXNvxb5VOKqKePHcMfSy9DFGX7zd0vr7MBX6FNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/662042" target="_blank">📅 00:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-662041">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">در این دقایق حملات بلژیک بیشتر و خطرناک تر داره میشه</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/662041" target="_blank">📅 23:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662040">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91379043.mp4?token=BxSt7p4RUnyN9tI1Y_oqBaYDUE6R6LHF4PpiuRDY1i0cKESxAQS5LUuFK2H4gUOlOG6SBTPeSB8Lh77hJmqXG1VIn2FI9fr-xxaph6nHX6c7565I7iZ0SfuN5HqG7pCHUG9jtIPYXGri8f-9D644AxuUDOOQyK0Oke08e05hWKVEz2z8C6YS4ErIGmAl_mbLbdB4NionLgzrOsApY4KRuXBxy2LOq3MHy1zVPtwNOrlSaobToHN4SFSYhpHNud8cJdva0RyxQRu1oM47IVs8Uc1JMehyczicTrlxGCJxQ9zf1R48sPgCoZFwvpwCB_Df7kcEfHe0m-1C6Wcy9hcIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91379043.mp4?token=BxSt7p4RUnyN9tI1Y_oqBaYDUE6R6LHF4PpiuRDY1i0cKESxAQS5LUuFK2H4gUOlOG6SBTPeSB8Lh77hJmqXG1VIn2FI9fr-xxaph6nHX6c7565I7iZ0SfuN5HqG7pCHUG9jtIPYXGri8f-9D644AxuUDOOQyK0Oke08e05hWKVEz2z8C6YS4ErIGmAl_mbLbdB4NionLgzrOsApY4KRuXBxy2LOq3MHy1zVPtwNOrlSaobToHN4SFSYhpHNud8cJdva0RyxQRu1oM47IVs8Uc1JMehyczicTrlxGCJxQ9zf1R48sPgCoZFwvpwCB_Df7kcEfHe0m-1C6Wcy9hcIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موقعیت خطرناک و صد درصد گلزنی در دهانه دروازه ایران با واکنش بیرانوند و مدافع جلوی خط دروازه مهار شد
🔹
گراد؛ انتخاب نسلِ شیک پوش
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/662040" target="_blank">📅 23:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662039">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">چه توپی میگیره علی بیرانوند</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/662039" target="_blank">📅 23:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662038">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866239d8d.mp4?token=PCxxoqrvYXY25HF7QOK7Wq36cSp1vJulZGsvvdSpdEi9fZuzDM1qpiBnDv-g5VDrKMGZF-X5fkB-temtxTSTdMyZ_sJv6pS4YiA2uv4Oxjva0JmYkhlVUkSxRPZc0kv1yPUpthcmFRurVjfLopjCY0bea25zjWC2ojYD4niZ78OCO7NsR9OEbZgdaYnI6ZFCvgf5ruxKdkUQkjplmDIftc42aodraEunHrXtflLt4pCCgpIYfr4QahEFaL3FXC3GQ_GtDwRKUNSkee8DiXjLylG5aehgARKo2oiaRYGFWxyiWS5MWOLRszhLX846U07brj4x7A1nJBfxwW14sG7_YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866239d8d.mp4?token=PCxxoqrvYXY25HF7QOK7Wq36cSp1vJulZGsvvdSpdEi9fZuzDM1qpiBnDv-g5VDrKMGZF-X5fkB-temtxTSTdMyZ_sJv6pS4YiA2uv4Oxjva0JmYkhlVUkSxRPZc0kv1yPUpthcmFRurVjfLopjCY0bea25zjWC2ojYD4niZ78OCO7NsR9OEbZgdaYnI6ZFCvgf5ruxKdkUQkjplmDIftc42aodraEunHrXtflLt4pCCgpIYfr4QahEFaL3FXC3GQ_GtDwRKUNSkee8DiXjLylG5aehgARKo2oiaRYGFWxyiWS5MWOLRszhLX846U07brj4x7A1nJBfxwW14sG7_YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کورتوا مانع فروپاشی دروازه بلژیک شد
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/662038" target="_blank">📅 23:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662037">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXUj6qKpv7FG45OYSpBCCXWzwA449wQSjU_FkTz0ZeR262b_7COtX6IPVU_DyM8wJew9z_-MYS9jsxLzxMd9K3aOj_exXJSLifqy7euobM_qgOwAt1dh9hw4XSHdjIsgzYRLJz7uKMWl3WNPVzhuiyUi5eZ_TZS_np7bJSeNWDKBGNv5itd7bDq2vSVxvxOCfttpxH0TjyQaOd0lXK7335eTh6RlbH_VkXtSUA6-cNffGhRh-c2OEuNn2zyQ0k55Kg-nq9FW-OOs4Dp9JiJG3pJgm7Zew9Qj-CBP0QADDvSXK956Js_yjb6MMHumw76ZbQ9UWd6kjnilwDvsBe1qTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرچم زیبای یا حسین در ورزشگاه سوفای لس‌آنجلس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/662037" target="_blank">📅 23:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662036">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چه فرصتی برامون از دست رفت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/662036" target="_blank">📅 23:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662034">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoQ8gqiWCf8GOD5iZiGo1rCdjerwcUJErJKw2ISHclnDIOGlb_z_3gmRQBpQ2xbORfk0SGAlizCiAiD5c8bGMrbfN-D9Xke7_CL37-D4gV0ub-27_nFdW39qbS3vy6WqiR9itttuY6kG3hRVrhfYFXs4K2JHILwivcM8xxXhBrRqpg58IRPLQmSEVtydXoqxoC9LQnTiotguklSMSHv-lng_2CA-qb0-iptKUGXNVW1Kphi0IQC5_DIPGcUgf7KpORoptx-ar2ZoqmEHcYsWd6vFJ-x8sN1OPNNEezcTT0E52OCCYeZc63vS40MoB6EDoFqrDP6YEaW1J9oi9G0iig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنعانی به طارمی میگه چقدر توی آفساید بوده
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662034" target="_blank">📅 23:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662029">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBpuD7vI9kMQXhtYbFSR95TbnZio7nY6eeuHE5M6jhOdw2FpM-YYuWkokumylay4RPrxXXuq9E4VbtiRgQ2HEkosIAbfiz9a3-lF78rCqw9lI2JsYhzmZ4NSD_WkdadZhhJD3C_mQKA9Yabs7vUQP9Z4uCX-2FA2HDJUi0FdXgAedPNq8791yrF2IfiZOj0xhB5dzPM6lsui3TKaD7ie283S__rFHMwkCPM5yNaYsUHRiBI7mKp8B3ca9fKBjUPlslX4CVWRdmXgALr8dRar-WyQEKqyKbbcRHBP4L1jVgGou6Dmw5qFwyBBVl5_UOt94ZdeNrBXwjE7nkM9tG0dxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTfRj636HwvNkFnhkMvv_UDOiU6aTN7ukzHG4uIrXAnTK0en5ctIcSXuIvplmEF3wkwX4uBCeak6DG9w5p7gJts7ZONtQAPkxMuNOktQzG8SH0qdlbUd8hYeEDmxoeiyK8mf3HQ-P41QL1QM4x-zQEmkW4Euvgq7Z9qQDMVkQ3QkoHLDFFDpvPKQ7pjbqFcQDIl4SbczT8x90xYvNNm_Y1r9ffYPu76rLeUNuSv7AJcK6xXuwcvB2f61fw2eKAM44L_E-I9nNUfxfzIMVz8iJSns4ztjg7r0kO9Z3sNTlpSttXVe3RRTEmT-dkl2NXvwjvP1Um0V13h17JYCfnC7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JP9mPzfoRD2Vrg2Kk7UD9T-sXXkR8-1XR9pdeeIB4JZsbIOx04pxeVOovo3dZt8qZB8pg5sGYVC2Gt_wGsDd1KSrBcSNVL74WsZxReKrhWi403WIdkwXpt-hoMmf4Jnso_bA_7S6TJnxAcipDuIEINFGzFXwUjMwBKc619efM0o-aeVmDyg4VOK-_hpUN9r7epwCi5eh-WtNbDHIn_JEmHSEOdPSAmuYFGFyh8TiyR6L6__6MYI3IZfjtjk3RmJsU80uQT0fSf4XaMYNXRxqyt1MyTIrfYyDFES0ZKQ1fTIRcYhZPiRhLpmHRJ251JfR1ULewQCnD8I1Mwv8ZpEfnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW-p9kzrZQhc7GRnVR5bjNbgyeoUfeDgcza4coz3kAzAS5s3Vnx0v7Z6sqYXpebM6EwB_yaSo2W5B42_KP8vfAheIr2VRlNN5kzqX2NIkIloprGjgg6939RBVS-JIqjaGqlA2FVwKGDqjjNDFwGEpevhvDMtL0IowMWJrpC8CXTNJnqh6_QlcPmRF9rH8JCsj7W1SSfsi5nH3SQVodcHKfFgyAFTGdfOfGBPLw6BYpX7cgQX6Dgmi4lINb_-7rryZSvCuilf9oFUR5vXQNyq_G5V0qM7T1tjlSuF3d8So1RKEGmeffrzUP-k10ZWjYw0q-YRzhnhXO9OL9JqLJBhUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khIqEsnOj-nLH_4-7smlpT-5MybYt8xqdvn8Nn-QyUFl_fcqGKUHSF9hUMmMZ5F3bDGqSUIFzHwGlo-8fU7vF1mTQEB_K6pn8S5M25TFiW_rWcWP0vFcDbMjStsnpiELLxG5o1AtDDTnhE3Lp2tp7bPYC73G5r2z36HzVeC0oF95_RNSo5w24cNvCfqWV32nmi0BYpd3D4NltcSCW1mZBz8yxLXxl3-daYW8mULrVbeHidADNbctCyHAYh2GQcTMtP8rLKGAwrsLtCK70MPVMlsF576dRHmXaCpcyZMuczeD1ePBd3bf6E1TzSAPShj7cMDkk8Jxb12OQi4nz3odSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همبستگی و هویت ایرانی در قاب ورزشگاه
/ خبرفوری
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/662029" target="_blank">📅 23:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662028">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
مذاکرات ایران و آمریکا متوقف شد/ رایزنی پشت پرده ادامه دارد
👇
khabarfoori.com/fa/tiny/news-3224774
🔹
ترامپ تیم ایرانی حاضر در مذاکرات را تهدید کرد
👇
khabarfoori.com/fa/tiny/news-3224806
🔹
پسر اسطوره فوتبال درگذشت | ستاره فوتبال دلشکسته و سیاه‌پوش
👇
khabarfoori.com/fa/tiny/news-3224779
🔹
واکنش تند محسن تنابنده به دعوای پزشکیان و مداح معروف
👇
khabarfoori.com/fa/tiny/news-3224743
🔹
مدودف می‌گوید روسیه دیگر به قواعد جنگی پایبند نیست | جنگ هسته‌ای در راه است؟
👇
khabarfoori.com/fa/tiny/news-3224713
🔹
ویدئوهای جذاب ما را در وبسایت خبرفوری کلیک کنید
🔹
http://aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/662028" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662027">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNDkDpcf8kli1Omd7DmFsnx8hfiaiwNWtJ9v8HIDuR6tON8MX6-1LBD_0_2NNtq-EUQ-pHzqfzS3gQLETL0jZlBqTualnauaKb577SiucPAvoyteTbqlmmZkCc2Rui-CaCJZIr6SApe2baOwgf6xailYLimuRJbNEsJZ8yW79lQlpS1g7NPm5c9ZaGm9mLrqhvF1AAj1wOjFIEgQw9Y-1OySVAJK_dxZQk6s77ijvojlhyjyHoWQGtYjFst9nnVT_FUH6f_pN2qryCpu8V39EPq-L_DU6_apOiRrU5U8_hOw8iD0Up8g4nGWQXRDlRiy4_IiEJ0u6xYuRIEzpZ3Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سنگین و پشیمان‌کننده‌ای به هرگونه نقض مفاد تفاهم خواهیم داشت
🔹
سرپرست وزارت دفاع ایران در گفت‌وگو با وزیر دفاع پاکستان از حمایت و همبستگی این کشور قدردانی کرد و پاکستان را از کشورهای دوست و تأثیرگذار منطقه دانست و گفت: نیروهای مسلح ایران با وجود امضای تفاهم‌نامه، در صورت نقض تعهدات از سوی طرف مقابل، واکنشی «سنگین و پشیمان‌کننده» نشان خواهند داد.
🔹
همچنین ایران آمادگی خود را برای رایزنی درباره تشکیل «کمربند امنیتی جهان اسلام» با مشارکت کشورهای منطقه اعلام می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/662027" target="_blank">📅 23:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662026">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4380672321.mp4?token=NkBbbL4KtER8MfufGsTxweWd3Fd8-HuWLoLIXqHVJkrP80Mthyhsi46cive5F_zrSe7Fe0PE2MdFneBIeWD5XlZd4C6off_kP0VRKb6g4hlD6VonmEsPJbjFKjYeRatIOoAnT9MMnubbHN0Gy2y-kOxYQllytbPN7RY1Fe8wf38KwKCZXHq4PsnH7fgnflg1ZMsMZp6S-OEfKxbk8xk6map6-Ojz_uUyF6exf0OqWfCcOo5ms5hsw-uiI2UzC5NWQe6HtLRKHqlOQDCaFhn5TuTZ-npMFtySEPD3Qfo28SNuIf4l8Sy6VUPPk7wgdpSnmILjBQj-tUQAEEuK8RLtsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4380672321.mp4?token=NkBbbL4KtER8MfufGsTxweWd3Fd8-HuWLoLIXqHVJkrP80Mthyhsi46cive5F_zrSe7Fe0PE2MdFneBIeWD5XlZd4C6off_kP0VRKb6g4hlD6VonmEsPJbjFKjYeRatIOoAnT9MMnubbHN0Gy2y-kOxYQllytbPN7RY1Fe8wf38KwKCZXHq4PsnH7fgnflg1ZMsMZp6S-OEfKxbk8xk6map6-Ojz_uUyF6exf0OqWfCcOo5ms5hsw-uiI2UzC5NWQe6HtLRKHqlOQDCaFhn5TuTZ-npMFtySEPD3Qfo28SNuIf4l8Sy6VUPPk7wgdpSnmILjBQj-tUQAEEuK8RLtsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرصت خوب جهانبخش در آغاز نیمه دوم
بلژیک ۰-۰ ایران
⏱️
دقیقه ۴۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/662026" target="_blank">📅 23:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662025">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a882f72f.mp4?token=qtrCRBQCVvWi5lFPLKa72y18mAmuCUZsfArLjfoNgfajsG2c5of0wjI7vJ9hZaTuEx3VPeEH6c9b5V1RK69QEL1syImJ4oLO_x4mGkhnIAoYLBPSJI4lDAOykpd8Ugj3WuyzmgHjsE1Sws26YvRe0WeoUCvnJlRt7anvmN6aDGwWUjOvmNaOs34iufckVijzwzNg5QYGevE7bzexwZ46mvhtQaczrvVw2szCG24c-YYk5PCsgScMJ41X_oxCGb6r1MiMVWMEfrYxPGrbbCRElQgwH6PbcLZxOgMWXAP8K4jYfAwkTfE44OSFJuvRypTDaz_oigC5RGjFsyuxfKy_eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a882f72f.mp4?token=qtrCRBQCVvWi5lFPLKa72y18mAmuCUZsfArLjfoNgfajsG2c5of0wjI7vJ9hZaTuEx3VPeEH6c9b5V1RK69QEL1syImJ4oLO_x4mGkhnIAoYLBPSJI4lDAOykpd8Ugj3WuyzmgHjsE1Sws26YvRe0WeoUCvnJlRt7anvmN6aDGwWUjOvmNaOs34iufckVijzwzNg5QYGevE7bzexwZ46mvhtQaczrvVw2szCG24c-YYk5PCsgScMJ41X_oxCGb6r1MiMVWMEfrYxPGrbbCRElQgwH6PbcLZxOgMWXAP8K4jYfAwkTfE44OSFJuvRypTDaz_oigC5RGjFsyuxfKy_eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در لس‌آنجلس فقط یک صدا شنیده می‌شود؛ ایران...
🇮🇷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/662025" target="_blank">📅 23:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662024">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
گل طارمی به بلژیک آفساید شد #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/662024" target="_blank">📅 23:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662023">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c97315ec1.mp4?token=ii1j_Kee1YqvRZTEsRzVAGsIDsvPTWqswTS-NDKF_2W_q3iD5UHCgjAGKX-UPn-e6a9ZqmAk8KFzqMUirNgFHKT3ANhOPL54tr9TxiLAp2KATQkIKubzS7piwxwF5QUFGSZEnmLTdqxlTlrXFH8icf7xOb7NLVx2KlDJpdz12zzJ2AxAV_a3XoSKsSJnO3rKUfengnkd54Q1jyf_zwxFHD8wYmsSdDWFz6M01C7rzqHanIAt6uP25LUIbmq_zRPuNoFbqt8FWquGYRl8BghFXEIpFNioa_7Mo4ZG3dYGt6YzHHQhXO8cG7Z5ZqXDOSVEte8nwApOKwXR7LFaSBud0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c97315ec1.mp4?token=ii1j_Kee1YqvRZTEsRzVAGsIDsvPTWqswTS-NDKF_2W_q3iD5UHCgjAGKX-UPn-e6a9ZqmAk8KFzqMUirNgFHKT3ANhOPL54tr9TxiLAp2KATQkIKubzS7piwxwF5QUFGSZEnmLTdqxlTlrXFH8icf7xOb7NLVx2KlDJpdz12zzJ2AxAV_a3XoSKsSJnO3rKUfengnkd54Q1jyf_zwxFHD8wYmsSdDWFz6M01C7rzqHanIAt6uP25LUIbmq_zRPuNoFbqt8FWquGYRl8BghFXEIpFNioa_7Mo4ZG3dYGt6YzHHQhXO8cG7Z5ZqXDOSVEte8nwApOKwXR7LFaSBud0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس ضایع شد
🔹
تلاش‌های نافرجام عاصم منیر برای متقاعد کردن عراقچی برای برخورد با ونس!/عراقچی بی‌توجه صحنه را ترک کرد
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/662023" target="_blank">📅 23:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662022">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
پیش‌ثبت‌نام حج ۱۴۰۶ از دهه سوم تیر آغاز می‌شود
سازمان حج:
🔹
پیش‌ثبت‌نام حج تمتع ۱۴۰۶ دهه سوم تیر آغاز شده و همزمان این سازمان پیگیر تثبیت نرخ ارز زائرانی است که برای حج ۱۴۰۵ ثبت‌نام کرده بودند اما فرصت تشرف را از دست دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/662022" target="_blank">📅 23:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662021">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آغاز نیمه دوم  به امید موفقیت تیم ملی ایران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/662021" target="_blank">📅 23:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662020">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isUVH2EM4ah0F_lar69YX9x0rcE5Iv9TP_Fi7oubiK92PI9YkjN8tuCv6PST58hfnFT_E4YZ5WEWoYuCyiDMuPLARpfjXDO6EetP6FRPISpIbH-DnM0RzY-VXCJlGrZNfQHfaRMSSYAy2mccVFgKOSU4aDixmHbPdzCYfqeuEk4YjfEe8IQBrW0dE9rk1jtIa5oAdufOovCICS8rvj1UizqSIZJiUNThJaqYh1alMy6gVDPzSLc2CPoscTEY7b-SNZ4Dqahy1Wk6Ge6NLD1yPwHc599b9XKJcGRQMrm6HGSovfVfpdjPu3TZSrq3ZXMJobtWPShdzA7fdOGpgr5MXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نیمه دوم
به امید موفقیت تیم ملی ایران</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/662020" target="_blank">📅 23:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662019">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P08bo5VDyfEfRV2GLTQfLFHFbRPz8rbUalNkxtuxGHuB_LT1M4-JiitmJ-894rf5VYmofOP3SFjMFjI_h-XDz7O43hoUWWjEezbjVI5k7vDQKWw3qwPHZy4HwYy1lLvjeb4yKY35pj-i6APEBFlCcsTC8QufabL4-zDXZ9S5DKsoYWfxmhKxnfaMVS2CD8vbYMzuK-kI7lhDLYlN8roGZP_NW1abQiVZBCOanif77fax_se5J42601ewuMc9n1G2s_GyOeY_5PLXnEuwXyxzbclR0vmnBbVF_a6MqqDUGUs-x8QEfLamGzR8zEXhoNiuYy1B6szg5hJr5tQviMi34Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت جدول گروه G
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/662019" target="_blank">📅 23:40 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662015">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-LO-SIisnO-XUPWvskFG2Zo-gw9VqgRyghn3Ai2TZCNAOtWI6BKxGGThV1GYOdXRSq_hZGRZOj_xMM3dMmwUetFkLF5KQYEZWocE9p_gDL6PdnaGxTX_di3XGr0UcVO_nLTm_uOiVigkfKdY-ZZw63v8tuRzNNcGbkop9VxNLx1N_sKhaQcXa6ngrhR024Bh1NUI_z-iah9Szn9qN14hjoh-SZBz8Hybx8O3FJ5eq_miIGq8GiBBnr_MvUOWf22hsUOzE7NXni6tTOQUBhHash2SHhKiw_qqYsaTZn25POt8QvUNKntC8TIEngoaWxo0B-BLaaduvo1To7vOKCetw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZodD5m33SKivKbqZ9hn22mKOp6XMGhW3TmENopgPAJi69agOSlk1PPOtTq7LT47qEkaqOptbQMJ1C9e8dc5nRNIgjajRARCFvkOmFq9Kuq95J6kp9UQqjw2eJGwvaQw3tB6fzoTfHWZ1QBvO9ymixY2wU2CQigM8fJZf-os_m-pKkjy6o3KoZh2HULZTO5zNY123iSlJ2QVW5_ac1aADgV--_wjHkv4nRIn3jPEmeosWzhMWiGFbmGP8_IoyCpaN2JCGWkuKq8COa3M7mV5Elq0lU3w9IbRz4KXD9nnBhfjWYwp9rPPxDXR2dvT0HRlBCALtarmWAp-9bN5F781Hag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EcTTTvVPoSaaiOTVv50Vadl24tQAgNOWqm6Wo01NLJAt8Yvqjp5JO6dlPxrC-T45vWUDD-LOetq7quZP79YLqMx-K2-Py-G94-01bKkcs4VGhwL5dPqeDKm0wkBADqw2P6SPnX56geE8VrhVEWgNmyI0T71jNKW12PvzlQodSA6FKDtFMoVhFSEiI0GFLsqou-8wTi0SJsst1aLqfTZvpdUNhCm4RT9n_88_zR8jmkQzC9S6ctRGmchYaY54jzg1ZZ4DKz4AEgdqAqxSmhwgB7tEoZFzUxCJqTpatGL3x_sPCMjkzvc5aDqhaMQDhjUy1pJQjtxPOQTrZT7eK9Z4fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nJs4zULr0D52W9ysTLM_ws8QC08Zset6GU9A_maD6qOoGywRCwjdCjmeSodaaeitcTZeobqA_4DoT0UKopudkZI9-P8sBkXMzHffxxNCFf5dMRIemjj1UEe0bVK7NoFGYX3TW7Mmz_Jm1JnbKUYnFJKd7TAPI8-IISAIMTuTrrFrh5Bp6mOXTtXZ7371jupK6hotSrSAdyY27tAt17hBpJRJNL_7b0cw3L_cV7OwgWP-OYvEO4dVg0ViJoiCVaQ3bwneRz2IvpC1fMtVp1ihPuQbllKIitz9yi-XgD77IMJCpvHQ7kpt-tv3EZx3hn7iKEwXFXDXRGDQjXn8XXYSEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
از میناب تا جام جهانی؛ حضور کودکان میناب روی سکوهای جام جهانی
/ خبرفوری
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/662015" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662014">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867650d109.mp4?token=lDvEhCl17lCewsm8Q3KiaqGcM4dJSKR4_cqHev-jA9B7vT2V_z69aBRzqiCMz_LaEvCxpB5d30SIEy3va5BlqppGLrBc6RZgXyxQls1TORrRwtmsN_GjC4RTaMdBX_6OG_vWTBdLHVBaS-ixIOHXPgTzsQKReyoiXlo7SGSMR8rjkt4PN-KGsQBETdIHgcqECdrMFdpKnjMMnIYCIDG7WCy3eJgGcy3Ku4Xy99mPu7hBcl1cZ80-YC72-lSXCWpxPmVVayFBRpBrAXtWbp3ifnaMyiJ6-d_Un62AS5CVUSix2p0dPHVtvxtF757o6IxzS7hhiivehNsieeqqMSA1JzyulNwFtJgwuV_caJFYeGtVJjWa7argt2DjYPzWTr6b0gX5Rd_LxcMSRU1XNOT78egj17rrJHSLhH7nMpllg-fNZkNE-7Bt6_NA8t3O9o0qocT_YRPSzDcJz-AXXBlt87GEX646E7DtGtLcmZlnpTSs3tttrGUQ6Egl7lXXiY7Nef8D5WHOV3DrlzEYniuHpRsoHmt9mg1y6omnkvCy_eWBHCYekxVfXYXe_smt4_uwQlG5qowzrwm_HrsT36zrpxzYWgM86RltqIP7EMuPlk7W1mCs-wztcDOmi_s1wZ0bg4BowID8cpGtOhTWIWXqYxsiYWHRuNtZLFwXMmHrq3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867650d109.mp4?token=lDvEhCl17lCewsm8Q3KiaqGcM4dJSKR4_cqHev-jA9B7vT2V_z69aBRzqiCMz_LaEvCxpB5d30SIEy3va5BlqppGLrBc6RZgXyxQls1TORrRwtmsN_GjC4RTaMdBX_6OG_vWTBdLHVBaS-ixIOHXPgTzsQKReyoiXlo7SGSMR8rjkt4PN-KGsQBETdIHgcqECdrMFdpKnjMMnIYCIDG7WCy3eJgGcy3Ku4Xy99mPu7hBcl1cZ80-YC72-lSXCWpxPmVVayFBRpBrAXtWbp3ifnaMyiJ6-d_Un62AS5CVUSix2p0dPHVtvxtF757o6IxzS7hhiivehNsieeqqMSA1JzyulNwFtJgwuV_caJFYeGtVJjWa7argt2DjYPzWTr6b0gX5Rd_LxcMSRU1XNOT78egj17rrJHSLhH7nMpllg-fNZkNE-7Bt6_NA8t3O9o0qocT_YRPSzDcJz-AXXBlt87GEX646E7DtGtLcmZlnpTSs3tttrGUQ6Egl7lXXiY7Nef8D5WHOV3DrlzEYniuHpRsoHmt9mg1y6omnkvCy_eWBHCYekxVfXYXe_smt4_uwQlG5qowzrwm_HrsT36zrpxzYWgM86RltqIP7EMuPlk7W1mCs-wztcDOmi_s1wZ0bg4BowID8cpGtOhTWIWXqYxsiYWHRuNtZLFwXMmHrq3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرس تی وی: هیئت ایرانی پس از پایان یافتن مذاکرات چهارجانبه، محل مذاکرات را ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/akhbarefori/662014" target="_blank">📅 23:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662013">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0addaa1aa.mp4?token=AmoD_mc-Zd6_p9EIeJAWQ4_LDW59Qjn--x_Uk0Bpj6a9c9Nl6EfLoW6xrE8P1hE_Re2u81ZghSyE2erz6mhsAVvg4b37lf3I7bZBBiId7D2ykXFq5IomWaSt6mnDHXZ4ShjpE5eZRcJpOUYJzYX2tSIz0arDda0PwfjdBPTsv686gOpS6WkBr5qYFg1dFOtYeTIgB4tWSXB2ldxPXtmA6jqd-TudsfkIxRF1gosUmeC9X4hMox8EXwJRAD3pGg5zLYyJOJnJOwzbp1UWJjoUqmRH34Kuv3Yfq9-JSoiNmOjgLE0JtDODOscI27BtwhWMzEA_MO4WKxBv5mkfR_xKMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0addaa1aa.mp4?token=AmoD_mc-Zd6_p9EIeJAWQ4_LDW59Qjn--x_Uk0Bpj6a9c9Nl6EfLoW6xrE8P1hE_Re2u81ZghSyE2erz6mhsAVvg4b37lf3I7bZBBiId7D2ykXFq5IomWaSt6mnDHXZ4ShjpE5eZRcJpOUYJzYX2tSIz0arDda0PwfjdBPTsv686gOpS6WkBr5qYFg1dFOtYeTIgB4tWSXB2ldxPXtmA6jqd-TudsfkIxRF1gosUmeC9X4hMox8EXwJRAD3pGg5zLYyJOJnJOwzbp1UWJjoUqmRH34Kuv3Yfq9-JSoiNmOjgLE0JtDODOscI27BtwhWMzEA_MO4WKxBv5mkfR_xKMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای کافه‌های تهران در حمایت از تیم ملی!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/662013" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662012">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است
🔹
این دور متفاوت از دوره‌های گذشته است و برای اطلاع از وضعیت مذاکرات و نتایجی که تا الان به دست آمده باید منتظر اظهار…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/662012" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662011">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smaC3JTDcCN72OCRXbEtotryTQSJeot4Sq7CPvRjjP6aZn7lzMi8LszTrBpc1lCXoroMGSIz9ttZTrxA1e4Mxn6zPNl0_NydlBYw_RNLapp2wUzLHIeFBHlG2tU-jDhtik6Hx5zQ3KwrEwX0kJ7WUhKzaQnrCEJPvPQ39O6CuyQn1wa96kJ9cjfO5ljAedjJoOtOSxj42iRvhjz1ELsDL_6Y0CEZjfISd7ZTGahIGG9aXq8_QGBPJ0GiyIuaXktJhmCPK2kdBtVSqFNZ7WwJF5npe8SM9E5hJe9wq2dOSdq_i71h2jvYUSdi8wqa33FYQdjHKbuRSNvRIfa86pek3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام سردار قاآنی خطاب به سربازان تروریست ارتش رژیم صهیونیستی
فرمانده نیروی قدس سپاه:
🔹
سربازان متجاوز و تروریست صهیونیست ، کمتر از ۴ روز ۱۰۰ نفر تلفات دادید!!!، اگر با پای خود از جنوب لبنان خارج نشوید، حماسه سال ۲۰۰۰ بار دیگر تکرار خواهد شد؛ همان سالی که با خفت و خواری از این سرزمین فرار کردید.
🔹
امروز نیز اگر بر تجاوز و اشغالگری اصرار ورزید، با ذلت و شکست با لگد بیرون  رانده خواهید شد.
خود دانید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/662011" target="_blank">📅 23:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662010">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
رایزنی وزیران خارجه اردن و الجزایر درباره توقف تنش در غرب آسیا
🔹
بر اساس بیانیه وزارت خارجه اردن، دو طرف به بررسی تلاش‌های منطقه‌ای و بین المللی برای توقف تنش در خاورمیانه و تضمین آرامش اوضاع فراگیر از طریق حل دلایل اصلی تنش پرداختند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/662010" target="_blank">📅 23:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662009">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
خبرنگار صداوسیما: هنوز نمی‌توان گفت که مذاکرات به پایان رسیده است یا خیر اما از شواهد به نظر می‌رسد هیئت ایرانی در آستانه بازگشت به کشور است
🔹
این دور متفاوت از دوره‌های گذشته است و برای اطلاع از وضعیت مذاکرات و نتایجی که تا الان به دست آمده باید منتظر اظهار نظر رسمی اعضای تیم مذاکراتی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/662009" target="_blank">📅 23:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662008">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGn6asOspZ8Kacs-6PK6XQbPuXa0v7eBQYbJlkwRJHqFkCgX7qPH8OnqXmL1qFkPrnKR4PKhBnjtVa32xtgfqjZmLhHIIWKC3N9IArM-vNy3cAH4-uOFTcnSSk_L9vtvZsxYHvRLdOOsPU5jTlB7O7CWm35By5tiWFTMA2cvYENfBB8tN1_cIfkBtOf7c9icIbzNjWcPqjH_ve4OUMCmc-4UVEJf8-NFa5-BF95u6nZJQADdG8qgyRuRZ8cThAibI5RdGeI5FIPJkc02WR-8Hqh1qSJbGXtDCT2IfWyuloMOkY5N2aM0jxIplSdl5FDNkNXe8MCBNSAoYJr4K7bpKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انفجار در یکی از کارخانه‌های رأس لفان قطر رخ داد
🔹
وزارت کشور قطر اعلام کرد این انفجار در داخل یکی از کارخانه‌های منطقه رأس لفان رخ داده است.
🔹
مقام‌های قطری تأکید کردند در این حادثه هیچ‌گونه تلفات انسانی گزارش نشده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/662008" target="_blank">📅 23:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662007">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiadNTPltC2esIg3By0ERUZoNkCF696CfXpXvNSn6EMKbTLVXJZ9Q78aw_qtRIMc2r8wJnVSUe0wR9CIJ2Fkn0xLjp71Te8d8NLTiTU-NDuTvProOl4C9u6fX9BpS4n3T1mikxDSW5MPuvWmeuGQBVypI8KDJA7by88oBtt8JJFXJSaolW9wO4i4pjbduD0KnmDQZBVV5ZWTh_1HDm4HEVjTOVuJGwdt13Z-YUS_XMIy0zveAtSh4Dj9dLolNJOlkCPpQWC1UukMtgXkoAH3YH8jlwDL5Xw3YpMrc2Q3i4XfcgzSZoloGK5H-rRxs1ZpQS4j-F1-zVtUQZZyM1HQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حملات دو تیم تو نیمه اول
🔹
قرمز واسه بلژیک
🔹
سفید واسه ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/662007" target="_blank">📅 23:28 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662006">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8TS9uS-G4YKEAhbfOGCFR7gjHHzmpwvyc17giJ6VDanZs7RdDvApNhULmRamOL0GA9_E7aloLcZUB8DL2sHqJQKGb6u66V9FxY3F1q9623atq8XCsK1JHW2luPwbRWlB7RRf1C1ResCUzP3bCeiYPFsTKYwv8nCt6r0R2E3_0orp-sGuk6-FdfypyYIvlITOPf6fjf8bdLX87NCSrfVp6GMZSW50mHXB2eU7Qh6O9x7Zaf6Ez3fD6S3o3_64NYFdKM1X_HaizDzGbBqqL1yGQ7_O-jLA_10EwR5tnZpyJXe3XOT49VeW-xcr7RbJujn0_zAmUgp89G8WQ-uxPsfVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمار بازی ایران و بلژیک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/662006" target="_blank">📅 23:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662005">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">📷
‏انفجار قطر
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/662005" target="_blank">📅 23:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662004">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HT3c6MUnEDYojXvgX1oC84LS10npLng4I02azNTy00YtvLgQ1wdoS4KTnHwokWdzMvERD6AP8gPEOw73plCc25wuI-7Hq-qpTfmMl0dwpIRVmqlwG_y5FmJXNRNcNfna9zwcDx2LD7RFO-97BPP5FWEEeesHzr6aYvq9HpeKqonsjMMhNHdgbf28Opt_0O-lsU1lROiAIg--EY9UewQGw4_rHtUXVTbjFj-9cqBo1F5ynVy4JXmGsK1t-kNpZpU6EuXqEg_k1BT9VrxpgZ5v4DHjXaPIb1DV40ys8acMNNCJAswcZJ3mWQTTE7Gb9ak6tZIF5_1Gf4fHYv_qowKlrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز از شنیده شدن صدای انفجار شدید در دوحه خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/662004" target="_blank">📅 23:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662003">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پایان نیمه نخست با نتیجه تساوی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/662003" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662002">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
وزیر امنیت ملی اسرائیل: با ایرانی‌ها، هیچ فایده‌ای برای سازش و امضای توافقنامه وجود ندارد
بن گویر:
🔹
ایرانی‌ها باید بمباران شوند، و سپس دوباره بمباران شوند و سپس دوباره بمباران شونددر مورد حزب‌الله هم همینطور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/662002" target="_blank">📅 23:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662001">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رویترز از شنیده شدن صدای انفجار شدید در دوحه خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/662001" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-662000">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
المیادین: تهدیدات ترامپ بر فضای مذاکرات تأثیر گذاشته و آن‌ را پیچیده‌تر کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/662000" target="_blank">📅 23:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661999">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c65abc230f.mp4?token=gaRKUMZ2zVGF3ACC7XTuebVBOz-RgKK-gAgBjGJNBfLUeH5kUgFxZ2LYpr1UHJtnDJZDE1bzXtkrkw0VFM5Arml5i-jmvDxQXSIb2f84-FtbA673D55X4gSpABZEwRq4B6_F0k8BU6ylbVO8TuOGlg71Zv63s84gQSNOl68z5bZcymJfwArjsKP24AIh_4VYeMPT7SLKJrUoUqPDjYrWAFAxmQ_OkH3x9COaD0YmrZu-hjIZYF3lKWTpTMn7FU5l3lUkH93lAZA7R4ZnZQ2Zuha7IyGrRBaFvlRUQFz0oeff03cbLEiCdVXenw7AtGRaMcdpZ9Qb-eFXIQQLfzV_FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c65abc230f.mp4?token=gaRKUMZ2zVGF3ACC7XTuebVBOz-RgKK-gAgBjGJNBfLUeH5kUgFxZ2LYpr1UHJtnDJZDE1bzXtkrkw0VFM5Arml5i-jmvDxQXSIb2f84-FtbA673D55X4gSpABZEwRq4B6_F0k8BU6ylbVO8TuOGlg71Zv63s84gQSNOl68z5bZcymJfwArjsKP24AIh_4VYeMPT7SLKJrUoUqPDjYrWAFAxmQ_OkH3x9COaD0YmrZu-hjIZYF3lKWTpTMn7FU5l3lUkH93lAZA7R4ZnZQ2Zuha7IyGrRBaFvlRUQFz0oeff03cbLEiCdVXenw7AtGRaMcdpZ9Qb-eFXIQQLfzV_FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داور به‌خاطر تعلل بلژیکی‌ها پرتاب را از آن‌ها گرفت و به ایران داد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/661999" target="_blank">📅 23:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58838dde80.mp4?token=LYDLp7YC3JyXnXl0Y0Vdf7sf853WHtQbZewhnOu_mHRktITZRZT6CvTdvp6k-uczh8oV9nexU1jbNDN4Dknw_0wiw9tA7QUdhUgSknL0tFJ7fgntDbd7BXwDFmzOINkEQpiLmWDDntuv8bkG_lYd_LUEmrAzjRZ8mvcGEhzi6GaEF2GTNe1YtjeGu5ZkfUAZLTD7U6TlUvcFW59HGOPU6lkNkGUsQ57rAuwAdaEsQdrRrgrmXiT9dUFt-VRVUhTxbf6I0d2cTCzH8HqP4q6uhKPKlVNRKVSvZXtCuKoX_-Zq8Enr_XPnteD3zsmElih8U_WCWjszNxgU8JVncfLNuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58838dde80.mp4?token=LYDLp7YC3JyXnXl0Y0Vdf7sf853WHtQbZewhnOu_mHRktITZRZT6CvTdvp6k-uczh8oV9nexU1jbNDN4Dknw_0wiw9tA7QUdhUgSknL0tFJ7fgntDbd7BXwDFmzOINkEQpiLmWDDntuv8bkG_lYd_LUEmrAzjRZ8mvcGEhzi6GaEF2GTNe1YtjeGu5ZkfUAZLTD7U6TlUvcFW59HGOPU6lkNkGUsQ57rAuwAdaEsQdrRrgrmXiT9dUFt-VRVUhTxbf6I0d2cTCzH8HqP4q6uhKPKlVNRKVSvZXtCuKoX_-Zq8Enr_XPnteD3zsmElih8U_WCWjszNxgU8JVncfLNuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موقعیت خطرناک روی دروازه ایران رو بیرانوند گرفت
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/661998" target="_blank">📅 23:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661997">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dcb564df.mp4?token=LAnGV_kKSMWgsC6Ygd6vEv6Y1oKe18FhaGCCE_9WL7pC_v2bPgpWUJek0li2BBl42QjE6D_YkL8ToDZkPtveOe3CeoNp2CbFq9Aa_3PZ4AtTE-Q0dN2F0yl2oG-05SCWnkWj7QmjnbaQl_8YUbZwsg4qvToA_iwz7zT9rcp2Q9cVmRUX9JVPgMwlKi1q3500gSrzrFoxSNHJdchykE1ELHMTscPIdYyG1KQfnr6b5k80mHaBC1DHekqZGe6SDdmFQQHw-ZvY7sK_n-9yRq8aYoeij-IunCY2YgEVMUClylPhqm0FaFuNq76HzdT3700IRi4OBJgQRx8PH0llSnEHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dcb564df.mp4?token=LAnGV_kKSMWgsC6Ygd6vEv6Y1oKe18FhaGCCE_9WL7pC_v2bPgpWUJek0li2BBl42QjE6D_YkL8ToDZkPtveOe3CeoNp2CbFq9Aa_3PZ4AtTE-Q0dN2F0yl2oG-05SCWnkWj7QmjnbaQl_8YUbZwsg4qvToA_iwz7zT9rcp2Q9cVmRUX9JVPgMwlKi1q3500gSrzrFoxSNHJdchykE1ELHMTscPIdYyG1KQfnr6b5k80mHaBC1DHekqZGe6SDdmFQQHw-ZvY7sK_n-9yRq8aYoeij-IunCY2YgEVMUClylPhqm0FaFuNq76HzdT3700IRi4OBJgQRx8PH0llSnEHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی مهدوی‌کیا و جرج وه‌آ در ورزشگاه دیدار ایران و بلژیک
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/661997" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661996">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در حلب
🔹
منابع سوری از شنیده شدن صدای انفجار در شهر حلب واقع در شمال سوریه خبر دادند.
🔹
هنوز گزارشی درباره علت وقوع این انفجار منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/661996" target="_blank">📅 23:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-661995">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a51af7066.mp4?token=WirRNQLR1XQg6HdgRfWeEBJ2IGlzI72GwUJQU4QYmfFnnuBCLeP0ChFsIK-pDWH_Bz1W4Gd1512PUfUVMspy1C0OBcmxOzSe65Orx4g2llFS2x7Lw7-uu1NhQXjepWbCzQugyctn_e_bhPRhGpOjOIZC5sKG634T0DSulAq_g455aysBBUI323O2G6AukFjZX-4EIvFLkMgklLMc694HTGhq3ZAIz0rVR8gRXF9UToyXu2VIt2tQm-ZjJfPgxzIRSb_5Vuw6sxUBrXsQ3QaG1-F-LLwgMtkNurXtKS0OCU-MY8w230IR-z_e_s0ooQUr44cCrkN9IBEE2cAaEpaVxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a51af7066.mp4?token=WirRNQLR1XQg6HdgRfWeEBJ2IGlzI72GwUJQU4QYmfFnnuBCLeP0ChFsIK-pDWH_Bz1W4Gd1512PUfUVMspy1C0OBcmxOzSe65Orx4g2llFS2x7Lw7-uu1NhQXjepWbCzQugyctn_e_bhPRhGpOjOIZC5sKG634T0DSulAq_g455aysBBUI323O2G6AukFjZX-4EIvFLkMgklLMc694HTGhq3ZAIz0rVR8gRXF9UToyXu2VIt2tQm-ZjJfPgxzIRSb_5Vuw6sxUBrXsQ3QaG1-F-LLwgMtkNurXtKS0OCU-MY8w230IR-z_e_s0ooQUr44cCrkN9IBEE2cAaEpaVxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ضربه ایستگاهی دی بروینه با هوشیاری مدافعان ایران دفع شد
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/661995" target="_blank">📅 23:12 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
