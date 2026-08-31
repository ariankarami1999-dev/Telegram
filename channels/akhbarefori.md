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
<img src="https://cdn4.telesco.pe/file/Cum2mwPgF9KxX5VDzk6YfkI2Alko0A0-SwsUJgLx2E6OSplcX2U3lc4rGHNBiYU0Sfje0Ol8C_Vjm2TM-rHX7q9xuI_ANC1AY4jamcjmj3pm84VNicdkAZZSZ2D9DJFRC6nctZyr80BnRCKIM8fHGXEpmdFUkuxYesG9G5YAMOFiuWaOBIrNDCzFhPSSc2c5-v5JB84kG7gMgi11bfbOVFvS7Ml5xNm6ZkA8w_95KkDWfF_CYXrHJrf1Gh95SQtJwWxcKPJxMIB6Sb87nfWkh2dHFn7AlBT_teQ8XW1I-zeYO3hmFLQGrdPGbcaX77EjCETJjZbIX8E-qPXAYz-ABQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-685954">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZGR7easugQNFLzrAa5wR90YbRG-rRE8jZd3wUIi2I8FruoXXLzjVlwb1m80HLK8fjtHTmZvaC5eohCvDLhpnWxpIQvfum-EZdMqqioFKyz4B0dSlHQ-Ov1kjmGNOcaLt8Qb5JBMWRhFXLnP-0159EP9Rz6LlXKb_7I52V1g7ne30lSipbRAOPWEpSqoV5TBGMcH5iiU7KLec0cngBYf5d36gBBOQ3QrSlIWIoZZGeBbZZS8CMhDXQWNGEjvgtArPofhFdjby4GEGT_HIRJdXsRDuBQ976ijnh4PucSUXNkWnLZ5XMDVMUKpMVlMv7jEafHljYN6g517B0TRQbaggQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترمز هرمز
🔹
آتش‌افروزی شب‌گذشته آمریکا در حمله به لارک با واکنش قاطع ایران وارد مرحله جدیدی شد. ترامپ امروز هم با تهدید مجدد، بر سیاست جنگ‌افروزانه‌اش اصرار دارد. این رویکرد، ضرورت استفاده راهبردی از ظرفیت تنگه هرمز را بیش ازپیش نمایان می‌کند. ایران می‌تواند با مدیریت هوشمندانه این آبراه حیاتی، هزینه‌های نظامی و اقتصادی را برای آمریکا به حداکثر برساند و زمینه‌ساز عقب‌نشینی آن شود. تشدید فشار در این نقطه کلیدی، پیام روشنی ارسال خواهد کرد که هرگونه ماجراجویی، پاسخی سخت‌تر و پیچیده‌تر از گذشته به همراه دارد و معادلات واشنگتن را دستخوش تغییر می‌سازد.
🔹
هشتصدوچهل‌وهشتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/akhbarefori/685954" target="_blank">📅 20:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685953">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIy1bLcX3iTHnvkXXqNo8m-mUwMiN3tcXCZDUjnfVg2C7Z39PaM46dhoTyzey0FuDsjokg3IiutcQUPRxOmJqXYttmxIu_sq6XFNchg6jVpZn41nRxhBv_6VySGQXQE6ErKNP3D-UJKKM-0WnYteT2Chd1okfk3DStIg94pAaOD4SI111egjndy17faBQ6Ovv1CzAb5yPuTWbEi_-1Efv5t1yC9517p5lqwtc21Y20vt9txQEJyPT1j-ij8lnJ10XbMek9eNlaXNwsVn8GJjzHNUFhhF1POpmjzi88-jxxBqXos4Vz-dmTvJEaI6uO5t2ddOQ9fn3Lq3ljHIAAiQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین انیمیشن جهان، جام سفالی در ایران متعلق به ۵۰۰۰ سال پیش
🔹
ظرفی که با چرخاندن، قوچی را در حال پرش و خوردن برگ متحرک نشان می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/685953" target="_blank">📅 20:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685952">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ناو آبراهام لینکلن در پاتایا پهلو می‌گیرد
🔹
ناو هواپیمابر یواس‌اس آبراهام لینکلن با ۵ هزار ملوان و تفنگدار دریایی که بیش از ۲۰۰ روز را در دریا سپری کرده‌اند، روز چهارشنبه در پاتایای تایلند پهلو می‌گیرد. مقامات محلی ضمن تشدید برخورد با روسپی‌گری، برای جلوگیری از آسیب‌های اجتماعی ناشی از ورود انبوه نظامیان، گشت‌های پلیس را افزایش داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/akhbarefori/685952" target="_blank">📅 20:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685951">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fad2c3012.mp4?token=FLHiQpTEjmzBdHedyt94S2AtzrAfPe-GJRiLRx3yApdKUI3ke7L-SbntQEf5IKJM0iB_5fFmFfE_5C1q4Sh7AtUxB0lQ5LAo-vAXuRIxLDdgKVhpnn7x_AzarBYRnwvpoE2S3o3IklMlMqAcmQwwLCWKP7ssT-PZxNJyUrSeHkH_wq-rA1XYUMgNRKLGAgkmx11ddrs9K4itq7khAqb-nMJhCRepuz8oL4if52XHa1S52FR32w_S64LzJ-ztPlfanQBXvmXAEpf6dBqUJPVT_GsBw65fN3RKgmy5wiMwjCZRhQeT4JJTQr8OswxFJmjnDkrsCdWiIwm5o96cTqnNFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fad2c3012.mp4?token=FLHiQpTEjmzBdHedyt94S2AtzrAfPe-GJRiLRx3yApdKUI3ke7L-SbntQEf5IKJM0iB_5fFmFfE_5C1q4Sh7AtUxB0lQ5LAo-vAXuRIxLDdgKVhpnn7x_AzarBYRnwvpoE2S3o3IklMlMqAcmQwwLCWKP7ssT-PZxNJyUrSeHkH_wq-rA1XYUMgNRKLGAgkmx11ddrs9K4itq7khAqb-nMJhCRepuz8oL4if52XHa1S52FR32w_S64LzJ-ztPlfanQBXvmXAEpf6dBqUJPVT_GsBw65fN3RKgmy5wiMwjCZRhQeT4JJTQr8OswxFJmjnDkrsCdWiIwm5o96cTqnNFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج هواپیما از باند فرودگاه در برزیل
🔹
یک فروند هواپیمای مدل ایرباس A320 متعلق به شرکت LATAM، پس از فرود در فرودگاه «کاسکاول آدالبرتو مندس دا سیلوا» در برزیل، از باند فرودگاه خارج شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/akhbarefori/685951" target="_blank">📅 20:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685950">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c31c441fa.mp4?token=lTrDH8ir9GdO66X1Ld54KdVQOjnPaoPdmksDoXl6aKPIFO2eWu4g3avY7S1z3SaZkC0vSGnksdDQAeoy6PVflEFr3Xet8qklsr6FxvrMYtqtvl3DYOu5Kns8M8KttgRqwPFBA1fbpBIwIZhfBhN5Kolp7EN00ZOvKYqDBUl2DfDmaSSzPsLOCVZsECKKeWNf44nx6qto2OBZ0wu2Okg-_aayCbyTpB6XTnnPDXBEBGJvelmK46QwONcJkdOOqgEY6sMHg0FhPmmGGUk-quF8tI-xxrR79VdRVnBMtA3Ot72Iq5yo_Tp3KF2btVRordlw5iecEFRERbOt0A7zy4k3jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c31c441fa.mp4?token=lTrDH8ir9GdO66X1Ld54KdVQOjnPaoPdmksDoXl6aKPIFO2eWu4g3avY7S1z3SaZkC0vSGnksdDQAeoy6PVflEFr3Xet8qklsr6FxvrMYtqtvl3DYOu5Kns8M8KttgRqwPFBA1fbpBIwIZhfBhN5Kolp7EN00ZOvKYqDBUl2DfDmaSSzPsLOCVZsECKKeWNf44nx6qto2OBZ0wu2Okg-_aayCbyTpB6XTnnPDXBEBGJvelmK46QwONcJkdOOqgEY6sMHg0FhPmmGGUk-quF8tI-xxrR79VdRVnBMtA3Ot72Iq5yo_Tp3KF2btVRordlw5iecEFRERbOt0A7zy4k3jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تایید اصابت موشک ایرانی به پایگاه موفق سلطی
🔹
تصاویر ماهواره‌ای تایید می‌کند که موشک ایرانی مستقیماً به آشیانه هواپیما در پایگاه موفق سلطی اصابت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/685950" target="_blank">📅 20:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685949">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmLydeQnLmAJLDkwRfQ9NpJ31pKwrPBwfaRPnblRaxqVPkDNYtoh-JY779Ge65kFkweVEiCZv_RrxIy8kis6UaErNfEh5rxkujafiWtUb__bscfO8Q7lVP4o0px6evZlrcl5UqaWUTtDioxx2QRbkwDiPeAWyj4GG95gIeRsKZ39WCVA7DRdx0CO9kqvM_P1zd8fFeBg9ViiA-JQe4WQwbwVnI5TsGCCYSagJUIbnRySXB03cWLvU8uY8Eiyr7tqcBp_UHAz1vutMQ4JRJiwH6A23vDDdnaHHZuzuSTP-DQ1JpY40Tz1nymrTb90WJzznoE5JHdpmwdPVv2RB_B6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلیط و هتل رو از جایی بگیر که بقیه می‌گیرن...
🥇
علی‌بابا، رتبه یک همسفری
✈️
بلیط پروازهای داخلی و خارجی
🏨
هتل‌های سراسر ایران و جهان
🚆
بلیط انواع قطار و اتوبوس
📍
رزرو اقامتگاه‌های سراسر ایران
جستجو و رزرو در علی‌بابا
👇
https://albb.ir/idsDnZ</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/akhbarefori/685949" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685948">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riK3MPTWOwzuIWd9WMTP_cexCN7H67VXL8u7p3eRUfok8SPBZZR_b1nOW_maAYmWfU7P397j1hzKjeTjm57RZlBASgdEDK0XzOGvncyvc0FJdxovqsP-uK-BU-_kMj96_L0CY69OTTXYW-Xi5HusfsXLeVnKWq1pm9MJ-cTs_Tu4Dfdy1FSu0PLU8DcdLbscay7EC5X_zF4Sl6Hp1lYFcQGnOaxPnib9G4jx3KrMnwxPdlXqnsKuqsxG-IuR9_pOdGt4WGbY3TYOEXRKDkOjXQ0b5GiHegv1pr0z1E5z-HPMN4w9uu8MnQrTTeM4E2574K_lCWqyqtXsOWC2yNYlmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
✨
قرعه‌کشی بزرگ ارکیده شاپ در شهریور ماه!
✨
🎁
با خرید از ارکیده شاپ فقط محصولات باکیفیت و اصل برای خونه و مراقبت شخصی‌تون تهیه نمی‌کنید؛ بلکه شانس برنده شدن  ۶ جایزه نفیس و کاربردی رو هم دارید!
😍
🎉
💚
کیفیت بالا | قیمت مناسب | ضمانت اصالت محصول
🎁
۶ جایزه ویژه برای ۶ برنده خوش‌شانس
📲
برای دیدن محصولات و دریافت شانس قرعه کشی  به ارکیده شاپ سر بزنید
😍
https://t.me/Orkide2025
https://t.me/Orkide2025</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/685948" target="_blank">📅 20:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685947">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ccf957497.mp4?token=Gxa8K_QLasPfmySVqQMfYaVk3VlK1MiGs7FuVh1i1D27ssqv5R4eo4f-L7opI1Zq78dQtbJ78PZJtpP4N6_wuSH9T8p-RDI-al3AiqZPrD7Sy_QKKu53yXFMcm5gV7Lu_bhlhuRAAN6_d4HdLL3ipwLohR-t1DLD94ESnlXxg_bkMR0w7Zg9oGNxyYyQQuVvCFRlFixtZXexNKH9JDxCfuaIU2ZKaGfmOtk2u0zl2SVkoPt5lGtzVe77yXSSdPs2tBG5L2TpUL2sbzTiZdAUk31zQ4vYsrlHD6R9sssfxnKpxa1eiIxnEspjxkCUZRfEBN5jGY1pWoGhf0M5LLyfRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ccf957497.mp4?token=Gxa8K_QLasPfmySVqQMfYaVk3VlK1MiGs7FuVh1i1D27ssqv5R4eo4f-L7opI1Zq78dQtbJ78PZJtpP4N6_wuSH9T8p-RDI-al3AiqZPrD7Sy_QKKu53yXFMcm5gV7Lu_bhlhuRAAN6_d4HdLL3ipwLohR-t1DLD94ESnlXxg_bkMR0w7Zg9oGNxyYyQQuVvCFRlFixtZXexNKH9JDxCfuaIU2ZKaGfmOtk2u0zl2SVkoPt5lGtzVe77yXSSdPs2tBG5L2TpUL2sbzTiZdAUk31zQ4vYsrlHD6R9sssfxnKpxa1eiIxnEspjxkCUZRfEBN5jGY1pWoGhf0M5LLyfRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رازِ پلوی مجلسی دمکرده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/685947" target="_blank">📅 20:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685946">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTVyYF7ptexpagItclnEmQDUENFRxI_vMfemozR0hz1L-dx8nOk2aUc_s3-zxOIYgJVQ6-bYw4XrxWjt3ff6B70JQuGXr65EipLHBEF4e3HfExNL3N_W8WJGV7dN-dTtWRu6tET6-GVllmnuJHniGkpwTYWsyll03hD6ljYB9qC1Bo3ya6Mxe5LF80kwn9aAeXZomu-lms4xXKDpx72Bf5Mq76w1V5vKrn8LGR9T1U_sohOTWknw8UczY4sHdLF9Yh-GTPyWsDh9vqtah0LJsfXJ53S9KLAFFnsHiPmj1Fot1V8EkA43loRY8WZ4D8CdWV5D_xzxkdfBsWs2ai9HtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناکارآمدی بیمه؛ مهم‌ترین دلیل کاهش بیمه‌شدگان از دید افکار عمومی
🔸
در این نظرسنجی بیش از ۱۸ هزار نفر شرکت کردند که سهم روبیکا ۵۶، بله ۲۶ و تلگرام ۱۷ درصد بوده است.
🔸
حدود ۵۲ درصد شرکت‌کنندگان ناکارآمد بودن بیمه و ۱۱ درصد عدم تمایل نسل جدید به بیمه را از مهم‌ترین عوامل کاهش تعداد افراد بیمه‌شده می‌دانند.
🔸
کاهش پوشش بیمه‌ای را نمی‌توان صرفاً به بی‌میلی افراد نسبت داد؛ هزینه بیمه، دشواری دسترسی و کارآمدی خدمات در کنار تغییر نگرش نسل جدید، به چالش‌های مهم نظام بیمه تبدیل شده‌اند.
@amarfact</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/685946" target="_blank">📅 20:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685945">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
زلزله‌ای به قدرت حدود ۵ ریشتر هم‌اکنون یاسوج را لرزاند
#اخبارفوری_کهگیلویه‌وبویراحمد
در فضای مجازی
@akhbar_Kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/685945" target="_blank">📅 20:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685944">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
رویترز: میزان صادرات گازوئیل از پالایشگاه جیزان عربستان در ماه آگوست به صفر رسید
🔹
گفتنی است پالایشگاه جیزان در ماه‌های اخیر چندین بار هدف حملات انصارالله یمن قرار گرفته است.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/685944" target="_blank">📅 20:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685943">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
صدور بیانیه مشترک «توافق مکه»
🔹
عربستان سعودی، ترکیه و پاکستان اولین نشست کمیته راهبردی سیاسی و دفاعی مربوط به توافق مکه را در استانبول برگزار و بیانیه مشترکی را صادر کردند.
🔹
در بخشی از این بیانیه مشترک آمده است: برای این منظور، به حمایت از تلاش‌ها برای کاهش تنش و ترویج خویشتنداری به منظور تشویق حل مسالمت‌آمیز بحران‌ها ادامه خواهیم داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/685943" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685942">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50af0cd4c.mp4?token=hFwnhNxLoQS8qG_Mw_52dcBBzn-ThmAcRGjo5dzm1OxsEQjh01mMWqEk4NrfYXPL8fbnVisSj14IzDF35LHDj-75bXLna71UP1-HPIKskgWwx_Y1X6HzqAtojBZIqGgkCvRhKDZfdKxTOhyzXx3vGf7y8_uDNOAhxHVZW_i-0N8Y8dBu88i7_ZpFp6HoNuc87nPNazkaqj6cfoMCgMaP4xX8e9w6dDkwEmD8mW6dEgN6tJpkf77uB8kthHlIhYbafLTvVgtPGgJtOUtwrkkjrnUnQd0L4YiDXkdJNHm56yR9IzcaPi0sVaAo2oB4pWRFLShu8t_nDUX2mjVGJvtwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50af0cd4c.mp4?token=hFwnhNxLoQS8qG_Mw_52dcBBzn-ThmAcRGjo5dzm1OxsEQjh01mMWqEk4NrfYXPL8fbnVisSj14IzDF35LHDj-75bXLna71UP1-HPIKskgWwx_Y1X6HzqAtojBZIqGgkCvRhKDZfdKxTOhyzXx3vGf7y8_uDNOAhxHVZW_i-0N8Y8dBu88i7_ZpFp6HoNuc87nPNazkaqj6cfoMCgMaP4xX8e9w6dDkwEmD8mW6dEgN6tJpkf77uB8kthHlIhYbafLTvVgtPGgJtOUtwrkkjrnUnQd0L4YiDXkdJNHm56yR9IzcaPi0sVaAo2oB4pWRFLShu8t_nDUX2mjVGJvtwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/685942" target="_blank">📅 20:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685941">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انهدام یک فروند پهپاد MQ۹ در شرق تنگه هرمز
🔹
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/685941" target="_blank">📅 20:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685940">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a07bbf2f.mp4?token=NOftnDsvZiDgM5kTue_8ebwEcT1iXkwnbQwlBNKcGau_REqROrM7uir-xCvpCsc57_hDuYEgzPoS-vh0qqiyJbNLgxeh88vBffdm_dqLcFkmww-y8T4YDnZr3CPlIp5v931NhzByYf2cKgU7BuA4P3bfF7Mi5ibO4T9eBxvCDZsu1VRtsB_O-JTOX6fn_6W6NqKt4e3vBf0vQi0FbFNX2BD9FdDUB2jPyopObdvQhVTgGZSbwbBXTLNUMAmBH32aq48da347tLYHcRNuqZNZVRpRrYYDI2M4WhHKlJHl7iaCDDUYmbBcJ0bjWoH6RDOcrLP1Tf3d0cPtyGGNlSqJ4hVg5HVCrXzTRRSV2v7lSvSqVGaHRSfymVs8r_wZLVULU_Er9WGp__KRCkWfyLF9kp9qXkwJH8Q4diHiqQXSdMY0aiZG4XdYLja6Mp6-l39A6nhgA-_33DQ-ikSu2m2dcbnSKYPaC3Aipa74weXvPi-4mTqvLW1s_L60XGc4Zg2AK3Zzuk6GrI96ZlU7z5v7Bt1_K015pimiHvIUf7TSijSYIrJ7fIuCr3XwDu1Hz_lgL_jVcayphiMd-HGnvtnsuP4dpcl0FkFUg9bT78jfa8cyvY2R_cypEziX1SEsHgCD3UCWj4XMcJ8CeXH4HZtdWwrHz1a5sm-Xug0zXV36yW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a07bbf2f.mp4?token=NOftnDsvZiDgM5kTue_8ebwEcT1iXkwnbQwlBNKcGau_REqROrM7uir-xCvpCsc57_hDuYEgzPoS-vh0qqiyJbNLgxeh88vBffdm_dqLcFkmww-y8T4YDnZr3CPlIp5v931NhzByYf2cKgU7BuA4P3bfF7Mi5ibO4T9eBxvCDZsu1VRtsB_O-JTOX6fn_6W6NqKt4e3vBf0vQi0FbFNX2BD9FdDUB2jPyopObdvQhVTgGZSbwbBXTLNUMAmBH32aq48da347tLYHcRNuqZNZVRpRrYYDI2M4WhHKlJHl7iaCDDUYmbBcJ0bjWoH6RDOcrLP1Tf3d0cPtyGGNlSqJ4hVg5HVCrXzTRRSV2v7lSvSqVGaHRSfymVs8r_wZLVULU_Er9WGp__KRCkWfyLF9kp9qXkwJH8Q4diHiqQXSdMY0aiZG4XdYLja6Mp6-l39A6nhgA-_33DQ-ikSu2m2dcbnSKYPaC3Aipa74weXvPi-4mTqvLW1s_L60XGc4Zg2AK3Zzuk6GrI96ZlU7z5v7Bt1_K015pimiHvIUf7TSijSYIrJ7fIuCr3XwDu1Hz_lgL_jVcayphiMd-HGnvtnsuP4dpcl0FkFUg9bT78jfa8cyvY2R_cypEziX1SEsHgCD3UCWj4XMcJ8CeXH4HZtdWwrHz1a5sm-Xug0zXV36yW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لک خودکار روی لباست مونده؟ نگران نباش!
🖊️
👕
#ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/685940" target="_blank">📅 20:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685939">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">#چند_خبر_کوتاه
🔹
پلیس: عامل شهادت ۲ مامور فراجا فروردین ماه در شهرستان سرباز دستگیر شد.
🔹
رئیس‌جمهور روسیه در دیدار با همتای چینی خود از آمادگی مسکو برای لغو دائمی روادید با پکن خبر داد.
🔹
پروازهای بندرعباس - دبی از سر گرفته شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/685939" target="_blank">📅 19:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685938">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGJwyCx0_dKB8LNzc_CJV-lhJN6vkvRxO4jmIRT5la2BS9enPk74ZQzXndGrSnZgl2V3xExu0UXMtBUgrynjQ25h21cfBd2_NGAAcivZ50Ye8pMI-kU9JntlK8uVHl2TQTcrDlUqYWaokwFr6FRsjkyaDQN4zA_6jeRYeC-V298dfrhN7i8dr9bwLSbQWXMXL1AbsnlUmmu9MR3toXoE_OyOf-AA7-FqP1CT5I8ZtYscuXp_0NjTQvZGm5CuPZEHugmxtuAFxeAuaY2aw76mYRbyUGe6rOepBPQuB72lV2p8L7XqJ9w_k_53t-eWA7O9ka5ow6BV90F082m1WlIH7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم با «حمله خیالی» به خارگ شاخ‌وشانه کشید
🔹
ترامپ در تازه‌ترین نمایش توهم‌آمیز خود علیه ایران، ویدئویی ساخته‌ شده با هوش مصنوعی از انفجار و آتش‌سوزی در تأسیسات نفتی جزیره خارگ منتشر کرد و مدعی شد: «جزیره خارگ دارد با خاک یکسان می‌شود!!!» #Devil…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/685938" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685937">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aac975f75.mp4?token=OwMb5HvjLXTlG3tmIRuqwAURC4Dngv1FBgbsGiAilEK1EhmE70edotJgRwZKRKs0E7-erh56pEmHM9QvfhQc0f7sUBI4y7e0qluJYq8KI9ARQwkaaaBv_pP6-E51lhYZYx7XwK9erMGABsxfNIROGlOu5S5XHz5na4Efsqe89wdAMW-H0yx-4WdJv5QOThYTcYnx7iawkd3UiAFJAtRlfmDSoN4T31XZyOkfJ86tTnYiQ-f9CTQwmee4OM2m2ZS3_0d7n3c_VlAu5l_SU49WREQinH4coFCAPpj6RfLyBFF2X4bIZBfBLe-UL5AUPPYmUlb4z_dkUszDt1EWG-I7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aac975f75.mp4?token=OwMb5HvjLXTlG3tmIRuqwAURC4Dngv1FBgbsGiAilEK1EhmE70edotJgRwZKRKs0E7-erh56pEmHM9QvfhQc0f7sUBI4y7e0qluJYq8KI9ARQwkaaaBv_pP6-E51lhYZYx7XwK9erMGABsxfNIROGlOu5S5XHz5na4Efsqe89wdAMW-H0yx-4WdJv5QOThYTcYnx7iawkd3UiAFJAtRlfmDSoN4T31XZyOkfJ86tTnYiQ-f9CTQwmee4OM2m2ZS3_0d7n3c_VlAu5l_SU49WREQinH4coFCAPpj6RfLyBFF2X4bIZBfBLe-UL5AUPPYmUlb4z_dkUszDt1EWG-I7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: دولتمردان آمریکا غیرمنطقی هستند چون بین حرف و عمل آنها تناقض وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/685937" target="_blank">📅 19:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685936">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cb7e782e.mp4?token=MT1VX9iXt1mrEFdqodytuGn-lAJP010Z31_asMPUDqtLeplaMH0RzE0uinhVJaWEkFkqfU-x4dKDUWHGKHJWNDg-wkMIbUBZJzAt8LhTrkAM_33O1FTPfjDDNHbOGnTfgM8E2ZKIgylWJ8kq0GP9C8h6fEctCconh1h6_OA1e-0aMe-yaMA1rYhbVsrD10B9H-ujvbisRvaMqK4DoFhK0aS1QvaRgCbFTmS7BmkZVAgvmwhGS5eQuC_gSLKCVLS9xUQ2sXQqcFwShormBqSsldW08WS3sJLd346yImdKCmv7BzaqMc1cEArsagOKdScUFk-mcupywKfc144JEKm9eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cb7e782e.mp4?token=MT1VX9iXt1mrEFdqodytuGn-lAJP010Z31_asMPUDqtLeplaMH0RzE0uinhVJaWEkFkqfU-x4dKDUWHGKHJWNDg-wkMIbUBZJzAt8LhTrkAM_33O1FTPfjDDNHbOGnTfgM8E2ZKIgylWJ8kq0GP9C8h6fEctCconh1h6_OA1e-0aMe-yaMA1rYhbVsrD10B9H-ujvbisRvaMqK4DoFhK0aS1QvaRgCbFTmS7BmkZVAgvmwhGS5eQuC_gSLKCVLS9xUQ2sXQqcFwShormBqSsldW08WS3sJLd346yImdKCmv7BzaqMc1cEArsagOKdScUFk-mcupywKfc144JEKm9eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه آمریکایی MSNOW: ترامپ از جنگ با ایران سود شخصی و کریپتویی (رمز ارز) می‌برد؛ ارتش خواستار پایان فوری جنگ است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/685936" target="_blank">📅 19:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685935">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438e4aafa5.mp4?token=jJaoxxKWWH6-_eKD9UeU7Azlvg5mY0GHQIIP46J82K88qC8Ap6IDYe1_9lcM5hAdh9tFj_t2uiqgiDu5TPj6tFeolWhdp16_ybJbdWS9VV89rDnnldDaXRouqep83e_MDEIAFzQGR-ilyIVGRZ9dF7XfuLZwVwZOK91YxOlkUWZbj4h1SAi_HiIH2adeFK-cQzCmzFzPOkub4aNCzIjYds-exBfc3M1Mz-5hj9uvdAwcxQjwjG6__daRPHkG2IzGGMjszjvJpF0f2wHvGtIjINrSj-pInHbYrWYO_WVwjBqUe-hkTvc3XACeFSUEKXztdh7QIMeWJktyTq2HnEohW2sbD75rhLPEZshUiyWEV-MkBk36BddoYFJtN-jyDxCVHIzpxnFLQaIdZ_qMMVJwTcuwOyYWHk8aaCI8Mt5Jmf3F4rR70Sf7EbqqcBWUpZ-qeckbnBcVkf7H6Zrm0TQDQqVPFT0F35ygO8jEoqIpDdp7eA8AxLxjSclz407ZkEkhzDkDxzT6rlpdYow97QeAlDgBDe9vSAx776DeqGrxyzdAAU2fzFSXcKn8pcJZEqioYnuXMeB3X7Oku6JH8VstSCTQPfC5lyv_jhNUo2hyDyiKnxVrA-XmF4RVzJOBXA_5X2k8W5TFSOLFGXd_KyqEbEdInoFgDVyO1UrAMcaX7Qs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438e4aafa5.mp4?token=jJaoxxKWWH6-_eKD9UeU7Azlvg5mY0GHQIIP46J82K88qC8Ap6IDYe1_9lcM5hAdh9tFj_t2uiqgiDu5TPj6tFeolWhdp16_ybJbdWS9VV89rDnnldDaXRouqep83e_MDEIAFzQGR-ilyIVGRZ9dF7XfuLZwVwZOK91YxOlkUWZbj4h1SAi_HiIH2adeFK-cQzCmzFzPOkub4aNCzIjYds-exBfc3M1Mz-5hj9uvdAwcxQjwjG6__daRPHkG2IzGGMjszjvJpF0f2wHvGtIjINrSj-pInHbYrWYO_WVwjBqUe-hkTvc3XACeFSUEKXztdh7QIMeWJktyTq2HnEohW2sbD75rhLPEZshUiyWEV-MkBk36BddoYFJtN-jyDxCVHIzpxnFLQaIdZ_qMMVJwTcuwOyYWHk8aaCI8Mt5Jmf3F4rR70Sf7EbqqcBWUpZ-qeckbnBcVkf7H6Zrm0TQDQqVPFT0F35ygO8jEoqIpDdp7eA8AxLxjSclz407ZkEkhzDkDxzT6rlpdYow97QeAlDgBDe9vSAx776DeqGrxyzdAAU2fzFSXcKn8pcJZEqioYnuXMeB3X7Oku6JH8VstSCTQPfC5lyv_jhNUo2hyDyiKnxVrA-XmF4RVzJOBXA_5X2k8W5TFSOLFGXd_KyqEbEdInoFgDVyO1UrAMcaX7Qs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افتتاح و کلنگ‌زنی طرح‌های بنیاد مسکن خراسان رضوی همزمان با هفته دولت در گناباد
🔹
آسفالت ۶۶ هزار مترمربع معابر روستایی
🔹
افتتاح ۴۷۷ واحد نهضت ملی مسکن در گناباد
🔹
بهره‌برداری از ۲۹۸ واحد مسکن روستایی
🔹
آغاز عملیات اجرایی ۲۳۰ واحد مسکونی طرح «خانه امید» در گناباد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/685935" target="_blank">📅 19:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685934">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان/ تعدادی از شهروندان محلی زخمی شدند.
🔹
هندبال نوجوانان ایران چهارم آسیا شد.
🔹
وزیر خارجه ترکیه: نتانیاهو دشمن بشریت شده است.
🔹
قرارداد بنزما با الهلال فسخ شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/685934" target="_blank">📅 19:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685933">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خط تولید پاکت در ۴ دقیقه!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/685933" target="_blank">📅 19:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685932">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
دستگیری یکی از سرکردگان شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی  مرکز اطلاع‌رسانی پلیس:
🔹
شخصی به هویت معلوم «الف .ل» از سرکردگان شبکه تراستی که طی سالیان گذشته مبادرت به دریافت ارز حاصل از صادرات نموده بود.
🔹
بدهی این شخص به شبکه بانکی بالغ بر  ۳۰۰ میلیون…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/685932" target="_blank">📅 19:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685930">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
اضافه شدن ۵۰ لیتر بنزین ۵ تومانی به سهمیه سوخت در ۲ استان
مدیرعامل شرکت ملی پخش فرآورده‌های نفتی ایران:
🔹
با هدف مدیریت مصرف سوخت و جلوگیری از صفهای طولانی در جایگاه‌های سوخت کارت سوخت جایگاه در استانهای کرمان و سیستان و بلوچستان حذف شده است.
🔹
سهمیه اضافه ۵۰ لیتری (۵ هزار تومانی) به کارت‌های سوخت شخصی در این دو استان تخصیص یافته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/685930" target="_blank">📅 19:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685928">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صدور هشدار نارنجی برای خلیج‌فارس؛ ارتفاع موج به ۲۴۰ سانتی‌متر می‌رسد
هواشناسی:
🔹
برای تلاطم شدید خلیج‌فارس در سواحل خوزستان و بوشهر هشدار نارنجی صادر شده است و ارتفاع موج در این مناطق به ۲۴۰ سانتی‌متر می‌رسد.
🔹
در این شرایط احتمال پاره شدن تورهای صیادی و آسیب به قفس‌های پرورش ماهی وجود دارد و فعالان این حوزه باید توصیه‌های ایمنی را جدی بگیرند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685928" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685927">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس پارلمان لبنان: اسرائیل با ویران کردن شهرها، به دنبال محو حافظه تاریخی لبنان است.
🔹
پرواز مستقیم ایران - ویتنام برقرار شد.
🔹
آمار قربانیان سیلاب در نپال به ٩٣٠ جان‌باخته و نزدیک به ۴ هزار مفقود افزایش یافت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/685927" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685923">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YquOBod6zwb1TUQULaShumurgNri5VM33ASaFmyRar0eYp5Z4h0KWbxXze08QF-qXL9bU-fpdxA2Dwd8yk5ch0YSjdLTIeiu2lXFB5zmaAqDHgT1pjnJ5eWgB3gqgT2N83CXfk0OiE1SkE4L-Lju8DOuV5-mR2HNf0B4oh_WMGwB86VfpospTNW3ihBdxNPna08TC3QpGYGP7JNZssa4QPh6b1dFuRW--_O-ZdD7NAOwEpUwlrdGXUF_ZsrwG_DMzs_Gty4xwhIAUx3DWKGCCFXtkhDc90Ax5Z0yVQoB4HyoWOlaTYA1G9At-U_Srlvcp2C9LkkDSKPvCzgRDyDpXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Mm61u5GgOq0r1yb7JJVPKWNz7iiNtr31Y2qyiP3MQrV_ZLtWzXURzYLz0abX7hIqLwnD478w_CXZeikKWzyBTDrVQsJUoFvL02kiZZLmbZLXarGEdTNZxTZQFFsW10s5NpoUAOzHyITBI5cw-tkpC7x3tWEyYmR17phacz8zbDPL7OfPwBpJDuCUAVvmgEBTo7Ufuolh5zjfS4d1OXyRVyXamKB1sAljzMsT2eXpCyKjOcvau1I_pSPfCEctGFTN0vuBSZ6QQSlpBVx7eEmGwYT5QZkRtflvb1EjcyCggM08Tmb5NDtk5Cnh3zzBtfFMiP_P6c_3MxVAaZby10qOkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IaU5IyzOXoasE86i4uYGqJK6BYvN53CCUszpwUc5VHfbLW7FyVv4Be8u7GYApQML-q3-4Va-cFcMcn97NcEf3KW0GyEWgRH5eAs_jm74hsy3emkOGGsCLFeJaCnwkpcEWBoxrWRRLsnsoOeDtN_GNGhxgDEGT8ZyM6UcckV9JJMybp4GkB_B1V1TQ5eqjeuLA_eJMbTmvWPvTkEEGCCkSyWu_mYBUhabNKh0nTsnKFrgiO26N2MmMmb1a4mwhM0mumA8wYEzFU3VkxA-m0sTk7MIfK50LN-eAcggusSfOlIP4QeAF8gpvwdk8RFePOPDIXHaOiKaXCpEwo6MCtGnqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/juqVrTpIB6lhHDMy6gqLGrZ8lOrO9b6kj5wpcVS9qfRf90SpKcHeJwbKsZ0C-MvDMTL_YmjTjRG0nFKAKaPGmVTMNDKK9Cf-h3GlzAC5bVvF8_Ue03an4UnCKFLnN5eeniGrKaHzqZb6YHUaQhS1aEu7G32_J9DX2CWO4HYWT6uxzEITwAF9tP371yoNgiqPemrOk3njOyrs2bE_cF4D6wyJEHStSsIrWb0lNrd4rP--RUjQz5P9tyWiwWOhZzCCu956IEAak9J0ZCixsgzGPz7ULqU7S-YxDMdu-FEZEWdB8vg7VPDMupm1C-OvTu42X2z6sxhYNGuoko5XGeg9Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هر ماده غذایی چه فایده‌ای برای بدن دارد؟ راز خواص خوراکی‌های روزمره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/685923" target="_blank">📅 18:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685922">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBP1dYTT8DbJ-y6BYovG9u1xXMbku0qN3eQVTMP8YwIhBAkGF1DwpDAf__MltS-7QszMf6vAH8ASjKZuZKjDVCEGQ3lZ8GipViaKCn37RcNYBi6BBTjSJmpKSRuGpnOCLolY0HyrP3WUZJ2L4B8fLvAH7W3s8ajl11wj3-AxjOL_CwACB1iG0P7MgvaS4hYd9E7sSx7lEgyFc-pBe6af2407ILwAgp_1cAoxb8FhP-PRc_xF2jAMcSN8ROCaHsrCkD0yVco-Es8Ulo1SvXzNZrYD_GwgVwtqUV9yPiSr38vdLQ07iVj3Fv5F283VfJRWpCGugOUdfzl3HnUHwX6sZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگترین طلبکاران خارجی آمریکا
🔹
این آمار نشان می‌دهد کدام کشورها بیشترین اوراق خزانه‌داری آمریکا را در اختیار دارند؛ یعنی به دولت آمریکا وام داده‌اند و در مقابل، اوراق بدهی آن را نگه می‌دارند.
🔹
ژاپن با حدود ۱.۱۲ تریلیون دلار بزرگ‌ترین دارنده اوراق خزانه آمریکاست و پس از آن بریتانیا با ۹۴۰ میلیارد دلار و چین با ۶۳۳ میلیارد دلار قرار دارند.
🔹
این ارقام لزوماً به معنای مالکیت مستقیم دولت‌ها نیست؛ بخشی از اوراق از طریق مراکز مالی و حساب‌های امانی در کشورهایی مانند بریتانیا و بلژیک نگهداری می‌شود.
@amarfact</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/685922" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685921">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
اجتماع میلیونی یمنی‌ها در جشن میلاد پیامبر (ص) در دوازدهمین سال محاصره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/685921" target="_blank">📅 18:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685920">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG2nVABNeqbdFxOuvyHm9P8w2sfMCGYBjVKhQ8MYbc7tffqJV0HNiF87D_d2L_6JT8jq_kBSLocEy87_LsmSmRIV7e882iyiZ2FU9fSSKSV1i0Q6XWdpjlZFh-ZePl8CxDm0GN7fU-LnLL50NfkWSV5farNXNlS8DlQKbnqpVO_GuuZteO_0wypqXJgejT7x5DEiBs59XU7UtRjALsVWu59Bd2DTv_RVArp2I95ingF5cTMVYD8I8XLj_g-lNQ0u7cM4yPqbF8m07eVpwKYuVzaHtQagiyWVart0XSP_5c71srZl9aUZk4MgN4WMMyDFaD8dLBP23Mv53zrRGr23SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیونل مسی از بازی‌های ملی خداحافظی کرد
🔹
لیونل مسی با انتشار پستی از فوتبال ملی از تیم ملی آرژانتین خداحافظی کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/685920" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685919">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjvEYwX9b4r1iwiPmJjGUvVDxK84_BMC5Ldky9bac89hK5V4CW_n4yq94zNSilgK2ciXuOiSUwon_3a6OmmnTMc8o4yXrUgE_BeYcgPW2sbB0Y3johWS--bOn8ZThwcSXXIXCh_DignamkFNMYx7wayaN8-OWD-kTEnLf9LO4eunt60pOYUUMV2vaI4lpPi_sL1jQjSyn4HI522kXYgPqC5Y0Wk9r6eS3TEWcAJaVqMdjotezejNVg3jVYIB9hEYmAy_VE5DS5IZZeoppTSw6HwrgdRgb7XeC004tOlHxNdIAoQIzCuK0b8A_Hws1eMd02zzm2kZersjxzJCqQs97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرحله دوم مزایده ماشین آلات توسط شرکت آب و نیرو
🔹
شرکت توسعه منابع آب و نیروی ایران قصد دارد ۲۰ دستگاه ماشین‌آلات سنگین و راهسازی خود (شامل بولدوزر، غلتک و زنجیر چرخ لودر) را از طریق مزایده عمومی به فروش رساند.
🔹
مهلت دریافت اسناد:
۱۴۰۵/۰۶/۱۶
🔹
اطلاعات تکمیلی در سامانه ستاد به آدرس
www.setadiran.ir
بارگذاری شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/685919" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685918">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سردار نقدی: ترامپ تصمیماتش را بر اساس منافع شخصی شرکت‌ها و مؤسساتش می‌گیرد
🔹
ترامپ سرعت جنگ را به گونه‌ای تنظیم می‌کند که در بازار سهام سود کند یا به اطرافیان خود اجازه دهد از نفت منافعی کسب کنند.
🔹
اگر آمریکایی‌ها بخواهند تصمیم عاقلانه‌ای بگیرند که به سود منافعشان باشد، جنگ دیگری را علیه ما آغاز نخواهند کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/685918" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685917">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f40036eff0.mp4?token=Eau8af1kbCwMCL0t9aVznWP_P2HrULFPLr0qcaMY6Ig4uYqF1RmMh1STXgp_SBwdzIXWFvTodfcrAC-vkNWOdxgvgMwkz6IV4yBwOzIMYMlqHkbuNbmj05YYMGcAOeWDM4aWJy-kZSq5QaqxgP-acig5ycytpHzRCEqPBdsFXFKTkHjySVV_xctRenOBIhFp9pBqZgu48r7Ls_faV17SB8b_mVnBCgKyGTrjXWkpCHexR-n49HOgo5zbimxUWu2D5CBr28z2GimZm6WJ2f4JQXDPnhmW3kZ8d7NB2SAyZsXm9J9kA932Z20--HXX_9ds5_6Kjn7DXyKnHxvAQlq7VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f40036eff0.mp4?token=Eau8af1kbCwMCL0t9aVznWP_P2HrULFPLr0qcaMY6Ig4uYqF1RmMh1STXgp_SBwdzIXWFvTodfcrAC-vkNWOdxgvgMwkz6IV4yBwOzIMYMlqHkbuNbmj05YYMGcAOeWDM4aWJy-kZSq5QaqxgP-acig5ycytpHzRCEqPBdsFXFKTkHjySVV_xctRenOBIhFp9pBqZgu48r7Ls_faV17SB8b_mVnBCgKyGTrjXWkpCHexR-n49HOgo5zbimxUWu2D5CBr28z2GimZm6WJ2f4JQXDPnhmW3kZ8d7NB2SAyZsXm9J9kA932Z20--HXX_9ds5_6Kjn7DXyKnHxvAQlq7VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژه کاروان ایران در افتتاحیه ششمین دوره بازی‌های جهانی عشایری قرقیزستان در حضور رئیس جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/685917" target="_blank">📅 18:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685916">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
چرا ذهنمان خاطرات تلخ را بیشتر تکرار می‌کند؟
🔹
یک روانشناس با اشاره به پدیده «سوگیری منفی‌نگری» گفت: مغز انسان نسبت به محرک‌های منفی، تهدیدآمیز و هیجان‌انگیز حساسیت بیشتری دارد.
🔹
خاطراتی که با هیجانات شدید و احساس ناتمام همراه هستند، بیشتر در ذهن فعال می‌مانند و تکرار می‌شوند./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/685916" target="_blank">📅 18:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685913">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfqNLv4tHFO8xRf3tlLl4lQKiiwZno6cGRie8uN1tUmhTIoqxeLTyKn-eh24CKOMCbaMts1_pjfYOv3NmjWn01xBDzg1lqUZZ5GEm9xK-p3IZfNpYWTglN0g_QSdbnL-tdUAXxbYSCUcntKfM60YO58JSXEnuMXW3txR2GDCepdg2CCgT4ymwAhdJib9uwUw8vCNd3LIPLvOVb7KRGmMRAEjqpTqg5rMPMDgPYrOZfb3NAlewwcF2_1U38oeVjm6N2COQfnMP_BLI1oQX3bfzsM_cjVVRCsbFYyuHlez6qPZ-X0A7NFOXEuqBXZeBDjx1yAzHrA1etwZ-qX-_xz6dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtDWNSnB7I3XL9rhvwNEJSaE3omiW7JW4oum3vK6yAVcvOLV97nqvfKYQnhAHJREmYc8mlX5EJv2XZiIpEcwQdmAbci_UtzbFMwaIO0rMCIAB04JIUzbo3pKJ1oiDSYwgos31caw9ll9szNtfBnwjBBJb0TTo4iW5ps8KMFTuEjmdpm0ptCQOuQtxGaNkwUAgItMJSn8kUSfxMeL7tQPgX9N0_sU8zEKZtlNgLFMWaD7AyGOCC7Z1enFWBKrbWPESn-26EsezyzeUIRgtBnFp2bRchTct7xiklchcgcXyLPzTYKnYAKFiRXG_xNUG_fLJCz7NKz7NEFqDyjKyAYDmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صابون قهوه؛ یک ایده خوش‌عطر برای راه‌اندازی کسب‌وکار خانگی
🔹
این بار در #چرخ_زندگی سراغ یک ایده خلاقانه و کاربردی برای کسب درآمد در خانه رفتیم؛ ساخت صابون قهوه.
🔹
با مواد اولیه و ابزارهای ساده می‌توان صابون‌های دست‌ساز با ظاهر و رایحه متفاوت تولید کرد و…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/685913" target="_blank">📅 18:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685912">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5esAsfBkCCd7mb4eptt6iC0N_mu24mGU97EBdmkI7sltfSal7CzbAxdrjSGnP83ZSCp4pSobxhnSWoe8Gs8jel2BXyjEycF29ZnGNQSbiTax57Cpd_kJ_29B_3AQVCz05WG2mth97ESkkPGmUxQevQ_X8cdQI9kuINlx0xVDQA3-vy5KpOT8nutsArz5Zv7xVfWrCKJRK7w8xMHaoLUwrnzHcVIDuMFsQNj7r7YgZAK_GzIU8rIvw1cEqgdZ-lG4imTSgAvY5rOIR6DMMjwXnQIjtx2SNAIsLNRdWxjHsn_8LqD0_ITtNrdOQGddcYA0MMzi20_bbsg-xMrcJAqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزافه‌گویی وزیر خزانه داری آمریکا: آمریکا به اعمال فشار اقتصادی بر ایران ادامه خواهد داد   گنده‌گویی وزیر خزانه‌داری امریکا:
🔹
کارزار فشار اقتصادی علیه ایران می‌تواند هفته‌ها یا حتی ماه‌ها طول بکشد.
🔹
ماموریت فشارهای جدید اقتصادی علیه ایران فروپاشی اقتصاد…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/685912" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685911">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-04FPGeACLj9vf1H36uIY38Fd0izqzOzQxNnzFqG2xP_h0Rju6Pt_mL8N69Mo-jf-6kxv7rIaT1WnLOed3B7I8pFKK3NHPcKsiOy95y1eNdA1SM0IOwCB2cMmS3RoYGS_4nYlhFHgzs59U0-Z0Y1Pc_MX1GVaqwAX2TB6Y84BQ07vHK_LNA94WQ9RxUCZjJownzngy4qso6GDq9VuamboGo4nkaTOC5ZqGZJ_zHwQHrci03Hpe68_0p11LnvuxRyQwFXMHbTwnHP9Rp7P4HvPKTRXg-n3MDaDfTEqAJge7UJwi21EVPr_UPbIkkRDBDwUAZYjmffAmirKC8FGcbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان با الهام علی‌اف رئیس‌جمهور آذربایجان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/685911" target="_blank">📅 18:13 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685910">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll3hNuJcDWE7oyuJneN40iJWnug24RA2f_EFbTKEr7_5moq5QSLKZe4K8luUH7AHdT5fQc-Z_evsKWl_0nfl7tBHUXZTOJbSWED_mjPWKnUl1g1ntEGwPsPlcWShW3ydSPsP-bnUlIkFk-HakpnwYCLaT7ja8kpvPkg7I5NkwWCzVvay9a8TLDJ6s9dN101MCq3dxeFHgYrcFro7ahaAl5BMv8j7r3izjtKMRyzZEf_x5gXmATY_REGWCMsOfaLm9Gw92ywm8F7pV3ezuNjyRHZTTUCVk09X_oi0FssreO-KlrKUQZJdup20kMokWCxd6nOCBYLGPLEhnhbrrouFWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفیر آمریکا در سرزمین‌های اشغالی: آیفون ۱۷ با تراشه‌های اسرائیلی وارد بازار می‌شود
مایک هاکابی:
🔹
‌این تراشه ها مرور وب، دوربين، بلوتوث وای فای و عمر باتری را کنترل خواهند کرد. اگر آیفون دارید میتوانید از اسرائیل تشکر کنید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/685910" target="_blank">📅 18:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685909">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_POf3vlOHGCkGCaIXnjbk9tNd5zR50LyRqwxPQ1V4VOuXtvNZU8OMrC6OK_9lkIUnkB6XCvxzxKWv7mcB9Z7zUkICd83qdCvl47ZhrTOl06BJEuC_rq-nYX23x_Y-wURiFPDjC1GuVsOotFBBuxMGmpQpHlD0m3Gv2DzHMmclN82XsSwdi1xL1IGNYFX2HGbdeckS8FmBIX_9DDG2UkV3xg26mNsaPYGMpK2bHL5Fi2H98u0wHtdE2LaA0YsTegCA_ukjTjzMOpRY4flm_zvGi2zusul_NmmNP6R3xbAm9JpYn5tTgB6aazmetUPpQ8PxGC71F3W0_6q4XiMOYFBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬜️
الگوی بی‌نظیر
#بيمه_البرز
برای «ایران هرچه قوی‌تر»
⚙️
هدایت سرمایه‌های خٌرد مردمی به قلب
#تولید_ملی
در حالی که وزیر امور اقتصادی و دارایی اخیراً بر حرکت همه‌جانبه سازمان‌های تابعه در مسیر *ایران هرچه قوی‌تر* تاکید کرده است، شرکت بیمه البرز از حدود ٣ ماه گذشته حرکت عملیاتی خود را در این مسیر راهبردی آغاز کرده و توانسته است پیشتازی خود را در صنعت بیمه به اثبات برساند.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5094</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/685909" target="_blank">📅 18:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685908">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e9f28917.mp4?token=UXQ4YbGG_Dm-QuWWwJcxXw5mrKtgl2ROTi1rbE16jiz4lX89U1MdNGWunL_bJ8u6agI5dC2OGXN_hNpPgi3Q7CPyPa_HQF8qtsh_3G3WDAqADj1PurvMlXUQtk9B1Mpi_1NwksbHcthrE3ToR-NwnGMtH_s1FzTsl9RcRlibWsJU3T0ynh4OvUYaz2hOTta6amQ51fmptMQ5eW8Xp4Mzyp_FDQZZ2gGKtUmt81ST2T9L9m1H2kVLFk3-4xegXBfBibpsnno2_gmlDE2KWGuGRLvLdPpD2wLk0wEwncco1P4xjTA55MJ_oxjzNPECJ6x5VjVpkAQVBGJEPJIOe9cA6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e9f28917.mp4?token=UXQ4YbGG_Dm-QuWWwJcxXw5mrKtgl2ROTi1rbE16jiz4lX89U1MdNGWunL_bJ8u6agI5dC2OGXN_hNpPgi3Q7CPyPa_HQF8qtsh_3G3WDAqADj1PurvMlXUQtk9B1Mpi_1NwksbHcthrE3ToR-NwnGMtH_s1FzTsl9RcRlibWsJU3T0ynh4OvUYaz2hOTta6amQ51fmptMQ5eW8Xp4Mzyp_FDQZZ2gGKtUmt81ST2T9L9m1H2kVLFk3-4xegXBfBibpsnno2_gmlDE2KWGuGRLvLdPpD2wLk0wEwncco1P4xjTA55MJ_oxjzNPECJ6x5VjVpkAQVBGJEPJIOe9cA6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این تکنیک‌ها گام‌به‌گام و خیلی راحت فیلم‌ و سریال انگلیسی رو‌ بدون زیرنویس ببینین تا زبان‌تون تقویت بشه #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/685908" target="_blank">📅 18:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685907">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
حملهٔ آمریکا به لارک ۲ شهید برجای گذاشت  فرمانداری قشم:
🔹
درپی حملهٔ دیشب آمریکا به جزیرهٔ لارک علی فیاضی و حمید عوض‌زاده به‌شهادت رسیدند و چند نفر دیگر نیز مجروح شدند.  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/akhbarefori/685907" target="_blank">📅 18:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685906">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1RCLARrXxNCfa83O2tpo6fgjxbLkag_X3oeqcFD-IvAx4hAmHOSAVhl5ojAOP9SbkqmBq_iq5gi08tx25-yrxLQTboWmYUtxqSBqHotYjdV2Axo-jozhptimHXHMaY4lUePVY8EMBnUcOfED1zS0HZfZe1TR6Y0Ebx2S6ys7BF7XG2G_qniGQGXij0hHHRkajvLcwHu7sdCmhNjmrGK9qVGeH356c-b-bbuZ9gCD1Ix9otdQc5rGDntxvJDYlnBbkuNYZfnLEt7JQuL9DGgecP6EP6ijxFNfjq4Vhou_FRvlGhKH-bLtrAFus8Gpo1xrqet5oO9Fg5CVFBPEg7BnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان با الهام علی‌اف رئیس‌جمهور آذربایجان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685906" target="_blank">📅 17:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685905">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQBntPStCER1aYzQ-tC98cRH11QZlK0S2BvMtwXMj2tNp8CtIJgCsLdXEZeTAvfivcnQNULTu44iBFvlA1RrJ5NVwFV-fnpYQ5ibUr7G1m023KK_8ITG0BE4Qb29v6LugLxn9UzOfOGVRimY0AoRAus-dDUrTusb2svv4UJPtGoNLgAhastaLKze35uHrqyVZSV_IBfGkg2HEaPgchYuhcFetkxhSQufFx1Prvubko-xYlYbpZpBVMyS8-kzT5Ry7FtQhE9DltaK_MgmgTG1GX6GqHt62HEPmDVtGVJEvBkeDLy-FwmAZap_UKo0V8IS1AeUuSbr-NaCit43GR616Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اینستاگرام حساب‌های هوش مصنوعی جعل‌کننده انسان را جریمه می‌کند
🔹
اینستاگرام حساب‌هایی را که با هوش مصنوعی هویت انسانی جعل می‌کنند جریمه خواهد کرد.
🔹
پست‌های متخلفان از ریلز و اکسپلور حذف می‌شوند و دیده‌شدنشان فقط به دنبال‌کنندگان فعلی محدود می‌ماند. برچسب جدیدی هم جایگزین می‌شود تا ماهیت مصنوعی این پروفایل‌ها شفاف‌تر اعلام شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685905" target="_blank">📅 17:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سردار نقدی: بیش از ۹۰ درصد ذخایر موشکی ایران دست‌نخورده باقی مانده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/685904" target="_blank">📅 17:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMf4F6t1WwHyF3yXpcEUYsoRiAleKTyvbAFPLlbwXrvkVew5A1YO7thcRORM09jDev5zpWosjMciewoiVr7m4uzQb7-_iWw5UQcxl2nsLpiEtr2YLqykZbVIixm-lT-T937dYc4f4ayh5zrEajTbAI5K5AORYZX2wxma1qbwbCfuK7o6oKTkmQTrPEo52gssCAF65TgQrDdg218OfnmvWI81QdVSajrnHArf-v2CYGITlZZRMosjrU-BtZK4dF2ctJE4dlaBl9gQhQtKeQe8yjqx3grgdvjQ-7XhL5gsQUt5BkR1U0AD6nrK4T5ObeNl2xHcjgqyKXmyHGG94fpn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتباط زنده با جزیره لارک تا ساعاتی دیگر؛ دیشب در حمله آمریکا چه گذشت؟
🔹
امروز ساعت ۱۸:۱۵ از شبکه سه ببینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/685903" target="_blank">📅 17:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685902">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
هشدار پلیس فتا به کاربران آیفون
🔹
پلیس فتا اعلام کرد کلاهبرداران با ارسال لینک‌های جعلی مشابه سایت اپل، اپل‌آیدی و رمز عبور کاربران را سرقت می‌کنند.
🔹
اپل هرگز از طریق پیامک یا شماره‌های ناشناس لینک ورود ارسال نمی‌کند و کاربران باید فقط به دامنه‌های رسمی اعتماد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/685902" target="_blank">📅 17:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685901">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1xEPnBgaQUqVAaXPwIHzi9n_1IFGxeR0ivzbE4MQkNQI476X3ylCaIEZN4giOirdaU5ze11ggbeWWk7eRCw4C3CAZG3sJwKEVcW9nnA8EayyoDC4-sJfWMl4rw63aZG07Bg_LvBFPKwJW6t4ZoMPitf4a6Uel1u5wG8oPlW4Ra-INI6wgGrGaJi6aUdIRwxvWXPUPmeoGJXTrOUQFpm8ULX0EIkVtaSqc3UJR_U0o31X6n8NBN2D_PEwOH8tT6ZREvTP9whLjikAxOUZCibkza2wSAMHbzmwmSWBNScCxFYGJWIPJPcpFqiAAtolVoXBLkVpjNduGkOyoItKr9Wow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در کشور ژاپن میزان تولید و فروش «پوشک بزرگسالان» نسبت به خردسالان پیشی گرفته است
🔹
علت: سالمندی جمعیت و کاهش شدید نرخ تولد…
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/685901" target="_blank">📅 17:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685900">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofruogWi5TYnzPK_W4Q0ALtRgjeGdqaTwWUl2vMBMzseEZ5Rpwrqt0zi26eBd-ZT3J8_FTMYK_UZmCcfd6V6bYtj7ZtkZ2QMkjz9HTqbtq82kQLJFEM-lhxkTpv9tC4D7sfbHx6sdBeoYD7yN74rXz8N_KpzINzTXlPtL2t0uHl0l86Hbt-h38EOjR8D4Ar81MhRlu_DyloO4qDMGN_0fjKg6RYfSneVaGrp1Q_Vb8gZOYF4LYL2g29Y0jjpZ2mjSwpdtml7ruoZcD-Dvi6h4PT5t-isTKoWVmBGFKjICNG5LfXO9RxQD8Sc527w-EL7pxT6uU2-Ofz_SRXeU60OMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: ترامپ در ایران تحقیر شد؛ جنگ، ضعف آمریکا را مقابل چین و روسیه آشکار کرد
🔹
ایندیپندنت در تحلیلی با تیتر «دونالد ترامپ در ایران تحقیر شده و نشان داده آمریکا چگونه جنگ بعدی خود را خواهد باخت» نوشت: جنگ شش‌ماهه ایران، ذخایر مهم تسلیحاتی آمریکا را به‌شدت کاهش داده و متحدان این کشور در اروپا و آسیا را نسبت به توان واشنگتن برای دفاع از آنها نگران کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/685900" target="_blank">📅 17:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685891">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKCmfJJrruUnFc-dFnuu-NDrzXkLDB8-clN7FGL9W3QAbPHB503ecaGDiN3Qhs6xGPYhyCXzA21G0WgSjnbx4Sy8yxZG0D1-VBlBMjebNc8BzWlqnaklBl6-lEcRdtiO9PhUU12x3kXtaQ5pABoCOgP0aUDhtSQlyzaWWJKanUZl5XODF-_IzgFOI0DYJ2Xjsb-UnKGFwfxgOO-ahiPJ4VxSYYilF5GgGmhy7YVleVAeABIWPW6W484FSxvjjgPY-fBwaVf5670yKxnfh3oZJ-52RrLUiaahrvAYKeaF2EkAgyjTR17adBkGXsgy1aiw3uQaLyCDLAktrYwXlriSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/peoqcXrGW019CZre2HJW-6YL8GaC3N1f_jeMc56mn8m7Whzw9S6zxWWtlFusZDFlBpgnVIO7qfJzN3REzRwvWQBG9VirTyzHmtV3FvidKsGr83376F6d4l_O2fGKA-iF2OcHX2l2RifNSGe4Dxo-3-s8gc3lR1LNFS2jL8y8Mw74l4JXdBHZU9imPhiYtWaA2uam7qxXXEs0Q36jhGH49yNZdfQbqClgx1gkHaW4kcpZuUudlo70QzFSi418O76TPYYwZSHJc5RuLa66ClzdeYWopp2EttTekwWnye4169a-4rX37HjI3iexpuQ-NsupdvR9agqjc6cQb8eEeUuC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mAdyQGfX1RtsxChxxNyGP5amhX4Tl_exxrnJ5idsvBQZM9xFcZ4q0FWrbLsngXeC0Rh6Hjx3Mbiug5zDHsrDz0TJIHk49qHgI8eY6ZcXrEdG_QYigvgv23OGDMg0X-cCi3_f1YsHR13BKywWBDMADSJfFn2T9xJgHBkFuTymKGu88rux2vCCNoM1bqN3Vpy3dx0y3VSkbUpyhJLT0rC9_gTiUbQTrYl1ku2Jgkjk7nZaKfw8AspzygJqcUXNddYO7V-4nkk2_cu7yopDS6RNR4j9RXftQXUd7F4D1jOzZhes-ptE0vlJ0Jv8fNvaMti0Hi2JdceEvUHujifK6ZLyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BXum_LOxEc2KOGccy-qPWSdizdDPc0iM8RJ_30yO8zXDlo04AU_7GFTcllf0COUpm7vTzP4Q7do6Xk0uehOZdeR8sN7soqLwDTS4vcPG8hSJ45e3Rgrbi46Tre3Xa9gZ46B-QaijEpQISte_VsOxNU4GZR2529gT1qbvoN-Pdu8fQsmOjKKEGFDyand-y9SpwqaaZJM9gPA1DbG8gZxz66iaL84NVz17bdQwcomBboxIBZdSO9f1EFd39-F5E6uQuxCZwG0Vnpxe5XWHKRUioHnEDogUKwQrARCzDBjBJKfazGJGdofx6owJKbBJUSSVWPClx01Q4Xg69OmPRPc3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ux74JjUC-hDWm-yGSXgx-VdVbEmSnB3FxqzKdwa1NHBFVPk8ivSGIrE7JjPmsBWrJvAoH7g9P8lAUU9oo2JhqG0tMuCLT5-kDsBezuqpznLH2mWLBf4BoSJNP3uxf66EFxdOT9Q1Dhldu_zAiJE03k69kNnXKWvxtl8rc5v1GIE8p-4_M8Rb_8vZoB9ponPis3HWRNOIduM34pAP3kruiV3fG7LWFFobI-2EXL7R5WK2iOTYjparv38prmDzAlB4LbGZenzKXBl6J9eW2JgrTvgDJz-Tg6mKFLJleTSkVBYdjhWOhxtlYQgYM0KUqqV-gOoKpTqLb0kQqkIxz6WQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tBkJRUnybvP4pXOQZEUZJXss__GdP0ugIzaeqs_QPK03L_MSAzZU3pqMF7Yufyj78YveyGGJB7QZDJUqix8W2wclndfGK7BooK971bh_Pt7SgW0YPpAsVf5Aaob8mqcIrcCs4rDu9B4yv12cAHVA2WifC2IncjhSTu3xHg7dUSAF6xq8hB6qteZuZiVfqZ4M7wEILLsQi5cwnrGXOEfi5QYx_HyW8ZyKKe2T1NGcnDIwnyIpSoLByfTDz0SFe3iSY9dq7d854Xx5-WrCKw_nYnWZJo0whrW94xk7OJ09adQhHFk-Z--TZWn-SF6JHZWR-I1LBLs8kwhh-HOTOMhj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3FNDSw06V3FkiY9ks9vjwPOY-yH_tj4B4gqIklPuz0C46ySJDYP5ccMpRRyRxJKJ484yVNBcUDj7B8G_cI8kQoZ1o3uj4jHOF6CKwohIp0MG7hfHVRUkxD2ASc0kfKxBvY9edR0_8nXeMjj2KhtDZQJhsROWJMWFAiIWgTCWMcSAs8Yp9nQJs34VBAVPorPY0kRRkmEZQGfrfYwo1sfhTk6fwabeCIoIsGREdNP1GxNhpbWZf0sNTPLFOeSBaF8lDK2CcsCPtM0Xq8Z7cK9NVvIkZo52nAt-GBvOVTOodc84AIwqNjJ1GmYYEvFhheZ_YLricY3ae62g67D6sr3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRU9KcywSc0DmMNISCBlVfl1t0scOB_GLHKDOEZPbfHVv3fGYhyuwYfe0WYlestSR20vin9_4LwFuQIUON4C66OttsZyGo4JpKCqLaTpBlLDD4HaZx5oJYIEqpvUp_3_EBcJPkWKk7-JiU7mDom0oUdGrcaKsQ4QAr9tFHqSFlnuevtSkuX9IRE1ocKFh18EXeVfzTTBQrhnPoisMLZdwGpZhAhz49YOW44vkEiaYWkUxBTOsQJSBtByh6U-KCbkAV3EHzyS0owxmp31GLfcHGchItHscQ0nlzjH2UH4yaW3Q2w5KRmmDsr_6ILvxpzOpsrkGCc-muhbx2uzfjz-cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqWu9_-Qn8y0ripvCaDNJGuK4Q9-Gq4XDw-dm0CRfLkdXj2wFImGhuiP8NwePPBUiQO6z22wm-HCDQTvcUC4BGIDRDzXL19K5T5SupOLopd0iQpy8DtZ6AlitL8EjZ8eOC82sn6QWOh3G8dxQIopTJaOm3pLdn-R01uhm0wGNXG-it-ZEqgXTFexcCZCIAbVySWxlWhXeVo4ZcgkHJjzghihmr4qRInqOmRpV0aoCDwYyiCPiWCoN3gYClZjsTRYvmj0WXnM-37gpbEa2O2544vNgtLGU5NZnXWQ4vR128WiSk2DholToB34JNOM5UoK0c6GOAJKNLSX_Q8KcY-wRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت مهرِ جاری
💫
✨
مهری که از دل‌ها آغاز می‌شود، وقتی به دست مردم می‌رسد، معنای دیگری پیدا می‌کند.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های حائز صلاحیت، این مهر را جاری نگه می‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/685891" target="_blank">📅 17:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685890">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0XAp5u4VoyU8cBAcS_8c-PonnllAtpQSBJoZL3hrVTPNsU0q4HQHKgKsFzfb27nop-94RuFzK41BNDuEbFC6ayOyoZgtesK22c_vE_gPlUhNK_Bhc71qu0Qw0fTNw6c1RKP1Vf5TKQK8e6IHf8L181-2g_4JRTRVCibvqQSb8e-UbsGBDBZbMtGIu_7BWNLHlLNIliOcq_uo2NX27409Y0_z9Eo8ezsSnxmxO-2l1fg9WDI7yonkTeELXVN5KbmFptVIya-uZYwtjNHMDvbi-L1070GFf7y2zwvvzm0EE5yZSCNViSlV_Gf2z0yg5CUN7efn4CvFrkR7XKRiKpLmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست آمریکا از کشتی‌ها: با هماهنگی ایران از هرمز رد نشوید
🔹
آمریکا هشدار داد پرداخت عوارض یا دریافت خدمات از ایران برای عبور از تنگه هرمز می‌تواند به تحریم منجر شود.
🔹
واشنگتن از کشتی‌ها خواست پیش از عبور، ارتباط با ایران و هزینه‌های احتمالی را بررسی کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/685890" target="_blank">📅 17:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685889">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ترامپ قمارباز در گفت‌وگو با فاکس‌نیوز اعلام کرد که امشب آمریکا به حملات شب گذشته ایران به اردن پاسخ خواهد داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/685889" target="_blank">📅 17:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685888">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
گزافه‌گویی وزیر خزانه داری آمریکا: آمریکا به اعمال فشار اقتصادی بر ایران ادامه خواهد داد
گنده‌گویی وزیر خزانه‌داری امریکا:
🔹
کارزار فشار اقتصادی علیه ایران می‌تواند هفته‌ها یا حتی ماه‌ها طول بکشد.
🔹
ماموریت فشارهای جدید اقتصادی علیه ایران فروپاشی اقتصاد ایران نیست، بلکه بر سر عقل آوردن دولت ایران است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685888" target="_blank">📅 17:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685887">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس سازمان ثبت احوال کشور: کارت‌های ملی هوشمند تا پایان امسال اعتبار دارند
🔹
معاون اقتصادی وزیر خارجه: تحریم‌های جدید آمریکا بی‌اثر است
🔹
عراق با ادامه حضور نیروهای آمریکایی پس از ۳۰ سپتامبر مخالفت کرد.
🔹
خشم ترامپ از کره‌جنوبی: احمق نیستیم که کمکتان کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/685887" target="_blank">📅 17:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685886">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKpaU5_J8dptA8Q3V6TztmniehGRLabrnga6kJ3SFeth5lM2wQde4ZLQ76ER0bjSD9vVKO9ep8c0xZQg_EhMDE4RqMM97y204-8IIAPtvvsb230uHdd3NxGQC7D5EvVgmDDjU58OGHrjCibQCtWzFYgtWBeFDZQ6_VCnZIfhn3VCh7snvu8sW-IvXvUaP0PiOH4yqebMhqHoA4uFuHRyx1ursyUywv_9gwiUkxUvfyvBmh4So-m3H0niXJfYFOcM5GmgP6L0a8cSFGxjwE1soJb30zKzQuu7RI6HY7XugEmfyb7-RM9g76zeVEe-H97L_MuvPCMZche2B5oe038fxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»
🔹
جهش سبز شاخص‌های کلان بانک کشاورزی در آیینه آمار
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/685886" target="_blank">📅 17:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685885">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
وزارت خارجه: ۱۰ صیاد ایرانی گمشده در امارات هستند/ ۳ صیاد دیگر همچنان مفقود هستند
🔹
از اواخر مرداد، مفقودی ۱۳ صیاد در آب‌های بندرلنگه اعلام شد که احتمال می‌رفت وارد آب‌های همسایه شده باشند.
🔹
امروز امارات به سفارت ایران اطلاع داد که ۱۰ نفر از این صیادان در این کشور هستند و می‌توانند خارج شوند.
🔹
۳ صیاد دیگر همچنان مفقود هستند و اطلاعی از وضعیت آن‌ها در دست نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/685885" target="_blank">📅 17:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685884">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75bde4d2ea.mp4?token=NYVTcTnMOU2Nshj9Arsjaj5hhogG4bCiNw_HwUfJEu93ue8XorD6L1nmGNIvrCoEs9bPAroel9lJ8sCZ5bMpINsY3ho3vuLmBHtmYF0RWbIyz2b0XgjUR-8bZbjOI9tOLfp4j67igJiTEOkyArJlCt6dLK3UaeiriC6dpu6JZjuETLBHyO_D2t3wDDK6ZjPNnnG7TcK8vCAS_ps7HO37KZ8-KXtzEvuLw8BUgphLgWiKYfrBO3OUlaoYYI4w6ZnfsUdSRvplQVftBRow6lsKN7u_fSxYg4d_V_1DFMuwqcIx6_7eTue0LThe8HQRsvksWVCmls3Ai3OuwwOlVHRDcU3ZpG5vF-DjDuJtpazTzStnPikaXr2FxWA8ChKILBXp_CqQjsAE_wVUNQEgPRMJ2O2w06uOWJtbIJ7v7XqkA1RX9ilk7A0V9OI5oBdZ1tJ6_kzJrQK0lGn7MH6zDXHZUKK7rWkASXZITXQdOfnBA9BkuC7kVKoS9OLseU-8gAkQEL8GEtU7wLd0P30HrG9-pDrjq3SltCnHz0tXIlLKFe6-4x6Ub1S_0agt5PjV-U-Z0W0l8h5pK5I9CvEp7OW8xhM9yjAo3QdUtCNxztjW_-Oz8ZjYaeAaZkfpicNS1G54_USBqq4zH7EzlftVkYocAejDBY5cl_rZcBEW9Qo-EBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75bde4d2ea.mp4?token=NYVTcTnMOU2Nshj9Arsjaj5hhogG4bCiNw_HwUfJEu93ue8XorD6L1nmGNIvrCoEs9bPAroel9lJ8sCZ5bMpINsY3ho3vuLmBHtmYF0RWbIyz2b0XgjUR-8bZbjOI9tOLfp4j67igJiTEOkyArJlCt6dLK3UaeiriC6dpu6JZjuETLBHyO_D2t3wDDK6ZjPNnnG7TcK8vCAS_ps7HO37KZ8-KXtzEvuLw8BUgphLgWiKYfrBO3OUlaoYYI4w6ZnfsUdSRvplQVftBRow6lsKN7u_fSxYg4d_V_1DFMuwqcIx6_7eTue0LThe8HQRsvksWVCmls3Ai3OuwwOlVHRDcU3ZpG5vF-DjDuJtpazTzStnPikaXr2FxWA8ChKILBXp_CqQjsAE_wVUNQEgPRMJ2O2w06uOWJtbIJ7v7XqkA1RX9ilk7A0V9OI5oBdZ1tJ6_kzJrQK0lGn7MH6zDXHZUKK7rWkASXZITXQdOfnBA9BkuC7kVKoS9OLseU-8gAkQEL8GEtU7wLd0P30HrG9-pDrjq3SltCnHz0tXIlLKFe6-4x6Ub1S_0agt5PjV-U-Z0W0l8h5pK5I9CvEp7OW8xhM9yjAo3QdUtCNxztjW_-Oz8ZjYaeAaZkfpicNS1G54_USBqq4zH7EzlftVkYocAejDBY5cl_rZcBEW9Qo-EBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران پنهان کسب‌وکارهای کوچک و خانگی؛ ایران باید روی تحول دیجیتال سرمایه‌گذاری کند
/تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/685884" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685883">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_4nMQoVBfkwtwJFPRExtpuQTFKZMLb5QF3WVL0LarVWs1LYNWnE7UGwrToKp2_QzTzU9AyNewfRFplawo8vC7ls04UjIWKqY3cPFN1JkPeXY81hMhL3dt9yYN_1FM1ZPKpIdIR0ZIX9IXc1j5M_8670okiJPi597m50XNmnq9Z1ZD4fYW-NHqWxfBd5vVFFP3Ml0HQosN7cqRhlZ8CXy5UoUiRXKOhteAclHPbhzRMo5w8xZe2PaSo7hKYhALiLCSZudKXjjxY3ttatuVnNZvAUsRVegVuw1WRtUFgrt64q5SaaTc6BAMn0ppuw5IjrQPuH8qCbbSQfpKrkoX2NRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانه سوخت‌های فسیلی چه سهمی از اقتصاد کشورهای منتخب دارد؟
🔸
بررسی آمارهای جهانی نشان می‌دهد ایران معادل ۳۶ درصد از تولید ناخالص داخلی (GDP) خود را به یارانه سوخت‌های فسیلی اختصاص می‌دهد.
🔸
این شاخص نشان می‌دهد ارزش یارانه‌های سوخت‌های فسیلی در مقایسه با اندازه اقتصاد چقدر است و هرچه این نسبت بالاتر باشد، یارانه سوخت در اقتصاد کشور سهم بزرگ‌تری دارد.
🔸
این میزان در ترکمنستان ۳۲ درصد و در لیبی ۲۸ درصد است؛ به این معنا که ارزش یارانه‌های سوخت فسیلی در این کشورها بخش قابل‌توجهی از اندازه اقتصادشان را تشکیل می‌دهد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/685883" target="_blank">📅 16:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685882">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15cd15b2ba.mp4?token=SRVWqW-IRsHj14rcgwU4g_UVckUi568KAlL5h8u6cHXhn0BWr1UdN0TtfmKpHog20TRgn6dqQm41e1IbGgmHrO5_O0kv9MS_9gVHeJgDtWnvwyigqxKTkO8_tH16I27ZyNC7EtN0UpbKT7ra9RseRPwkscq8dDgy58iyNWyAUhEgm2DxKpk_cjwPTUty9xojfbtEsA6h89AEkUx43m74PjXB4uioJK97PneU6jFjHEXJldiV3U7YOXgZPuDmQKfxCMndJilcKdKvD2dVS_F0-lO1LAWzV6170UPCJWC0afSpc19jD8a9KTSgwiiEF0hO6-8IgaXvh2Odxd1qr90Dvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15cd15b2ba.mp4?token=SRVWqW-IRsHj14rcgwU4g_UVckUi568KAlL5h8u6cHXhn0BWr1UdN0TtfmKpHog20TRgn6dqQm41e1IbGgmHrO5_O0kv9MS_9gVHeJgDtWnvwyigqxKTkO8_tH16I27ZyNC7EtN0UpbKT7ra9RseRPwkscq8dDgy58iyNWyAUhEgm2DxKpk_cjwPTUty9xojfbtEsA6h89AEkUx43m74PjXB4uioJK97PneU6jFjHEXJldiV3U7YOXgZPuDmQKfxCMndJilcKdKvD2dVS_F0-lO1LAWzV6170UPCJWC0afSpc19jD8a9KTSgwiiEF0hO6-8IgaXvh2Odxd1qr90Dvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش یکی از فرماندهان نیروی دریایی سپاه مستقر در تنگه هرمز به گستاخی آمریکایی‌ها: قول شرف میدهیم تا مجوز مردم و امام خامنه‌ای صادر نشود، اجازه نمی‌دهیم حتی یک قطره نفت از تنگه هرمز عبور کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/685882" target="_blank">📅 16:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685881">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
پشت پرده موج تخریب سایپا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/685881" target="_blank">📅 16:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685875">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWjkXEsed8M4DRsQkk5JwJ7vWrNqTsh_LFGQLnuNG35gtIbeUOaMOW_q-IivZuSF-g4KSHwiz85MsHjlLw9uuNrpWs9Bgs1dz5rrWMIdHnG0bvm5Ut32Ox82NSOWzDNu7qcyiQaryy08u7k9X937d_HEsBbWvvPkN8WgsyfuUAee2TdbJRFKUtasZU8dLCkLhP2wY9KC-req_SIHjMzvOIW6RPKkUtcc2_uVQmQfE9OeipEHqM520-owIcJt0Q-xdO5fa4TYcDVe5brPxUwMmOZsZe7cEw-n5qk8OL2VbgdC9h3In8NyY4hmcV3v9tOJLFY_SYmjWY3Uk0VDQiX6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C809cgC0BPCwSE52I6z7mtc_BWrrmXl66KzoPm_R5PiCpvqQlClwKGlleUOznUYtpxGxSxdmhOoTMHORYus-FHUSuGUpAnBy7TZlL-TAmsMZHiG1Qncz-kIRgQpMbANW9zKr2xaAH3NdJ-Xh9DNkGcdhxofa24S_a9SptBHWqaIeS5BVeGrceg1nsvtxVc6By-7dkYN0h7QGB7qDKP9Ma7g-NgsvqovjHS5YB75O_6F4mB1VJFgyHoeEKnaUx9GOK1LWxvyinFyZEBvQbBqNVTDk2amyK7E95OpBWMkcOJjQO1VK1c57XBKd_BR5Wjib2W2tDYQB8gbxGEzfe0ikfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SrbIfM6cgpy2Kme6sLAyPP1M8NIvGYfzezUKPA1QEBBGI-Q0lNIaIhslGwYh4Dgg6IxmA7xvCypz1HXduPSzkALY69u7r8I0MhEapg_pQ9FGc1isgl5rGzv3s3LGbH4Pobm1NZSLjq9_EXKmtqsAhDRlQqB50_YbVRIUbFNu2JgpXAmJZ-IvJcFeBjZ6hbLbTV34Vc24G2otJjO3MK-lnu4hAg4zjx4jswfi16cUHphZlj1E26LY1DxH4LCkQBTsMg9w4IL6WYJKKIAcvxzAEZR_wRwFc1QnrgTtKYprZ7dzbSyD_HiHNaKLTSWQ4Q_ZB6w992nIoAyd3LZyZyo8Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bn9JT4CwMxdRnyiQlOK1CJR5bVeSOmmB2_GduvlvTeioKMNhx9uyV0fNljjdL7aM0HEyo18BVAw8oMGr5RakAhBYZ4uWuesZEy5Z0dqi8ThkaqI9jQnpRSJRt03Vj0shC_ERtfbKNf1VAy1p6_EP5Glvi8rzkFEmLkkIr-OIzqiuxcB6oRrg_dEKSjJPSU4eQnaoXrcsrvrxrQfEUektCduqv6HSzCj9DuRFUV2ulBEJxYl_w2fdxMNRHhuSlS-qZXw03lsKLqF3Ohd5x_bow0pRqdT1b4a-MmYZgpFNkfts1x_7zeXLmvtT4DKrIA2_tcciWHyulqQEZEAMZPpXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i64s0XXuAUYwKIe1jXb7m9PMPEC35hdcK8c15JXVW5PUnotpuGXilPQAPmYCUe_jXBupNVJjJWBKflQUDdbJM_VT_uAv05MCqnLnvtzM3oSF6J2UPdcY7KZOq53GmMUvUHylm496AN0GwYzKmp7HH-r6JWvHu1FO3zJDO9rEu0ACvZ4IbBmERkixZxAsgzeD_v89LlrsNgbtxyl-4YJqr99KUgVSaVUodJf6RBLqQ-wG90B5DuZ-dGHMSE1vqYKW2FGxPoBSulHZbBUt1EY_DpG-fI45LDwFff3H-YQbhvnzRMFuJtx9X-HgIiSUx0hyhXhVq8WXj9TiLH4BMHqSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qoS_Vvs47ed56wdDVduig8ha3XdOYDlHsQVrwvDs0-svpvWInyF7oZjuPJyTb8Qg2q3ySofc9wy7qEVZ7a2bkz8eclwT0ywUDzaLA2zFAnB62dq6ZNn4DmaX-_Mq3kc6CwRC-6MmRmcDjt04ytf6_4VRSiPsa-wyUYES1yxwKInlmnlVR2-nBDVETcxzCgP-AsSvGNX45NqKJLJVI67whOisug6q0mBmKaTN7VcB0-G1gco4vMt7JAu_qIYFxacQtuioQDCkcEFpRq_Z6s0zmgfPK5csGZ8YnrITvoFwimfBI2DFAzFHmqymlNIx3xC9EANCJDqQUgSJdsfidB-oiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پس‌انداز فقط پول کنار گذاشتن نیست؛ مهمه بدونیم پولمون رو کجا نگه داریم که هم در دسترس باشه، هم ارزشش حفظ بشه #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/685875" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685874">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f35961b50.mp4?token=h7VSKDT17E7Enox_PGKSQZDiK20uQ53nnmwPsBjt_fyNHXKjVcsfgAOcTpp-P-Wbz0nMjQD51ZMIjQl7IftAr14zjXFfQZLVudNnjITopIFhIprA5gidgL9QK2tJsALt10evCiGoW-r9vIjvndRP29Px7xlj5sFvgoqUK3akwvH2v7lr3dNdkQCKXlHbqei403jH1z3uX1Y6sR77yuqCNsHTnAspbnH-UKe_3KFhlnLWTQFRrxHKXnw0WQlyNwYN_Tj0mK-zLJMSwEfeMOAGZqxQDLMzJpqLgNDicokytd_RKIIzVgxDyhSr38ZrZ7lAaf-u8tCzVgPjqXLOgKaXvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f35961b50.mp4?token=h7VSKDT17E7Enox_PGKSQZDiK20uQ53nnmwPsBjt_fyNHXKjVcsfgAOcTpp-P-Wbz0nMjQD51ZMIjQl7IftAr14zjXFfQZLVudNnjITopIFhIprA5gidgL9QK2tJsALt10evCiGoW-r9vIjvndRP29Px7xlj5sFvgoqUK3akwvH2v7lr3dNdkQCKXlHbqei403jH1z3uX1Y6sR77yuqCNsHTnAspbnH-UKe_3KFhlnLWTQFRrxHKXnw0WQlyNwYN_Tj0mK-zLJMSwEfeMOAGZqxQDLMzJpqLgNDicokytd_RKIIzVgxDyhSr38ZrZ7lAaf-u8tCzVgPjqXLOgKaXvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شپشک برنج با برنج چه می‌کند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/685874" target="_blank">📅 16:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685873">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDRToj6DE6JR7GOJ5qFEmWtIpGKFdl31i099i3oIynFrRTraawB8eZe8j2-TI0WlGTPTLtSuWYbkvT0BTTPLmXdlN2aEu4Hpx0dv3qDPTuTRHpox39m1088QSoRU3EzSgf6EEnAD3f3-FJjSDaqKLSFTm5-FS2sCBDwF3umxI7uhmvH89Z4KfR2RbTCWMMVJyf2IjstId1v2yLaMsWUiQdIl8CThTS5n80Dky7U_Jg7be6Q8ROQlIIE08jxBS9QWb8Q1VWD8Vyq5ffH4zquG-uz9bHkQ4iLRj5kGV3Xlb8j8I9LmdOFBv95ynktPyTfSuIPAWddu2BQCZ2IlLh7C6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تانکر ترکرز: تنها کسانی که انتقال محموله‌های STS (انتقال از یک شناور به شناور دیگر در دریا) را در تنگه هرمز انجام می‌دهند، خود ایرانی‌ها هستند ...
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/685873" target="_blank">📅 16:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685872">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/217ca78a6f.mp4?token=kTZ3gu9cD6CAD1xNS2HVsbEfGYcm335yC8eZHJNK86MkPYQ1PD0SzAjuDjD8hMRe086oxcXUdACQbK-kbcBPoP6QDpLa5rGFCo3NlvUBEAZTN8VDWFlhMzLrfni4fup8C_6phN4HlWVITBMTn7avmQ9d0_yHh415a3sUwVl2haXVgKq-xG8IRHKyDzfmPTLUt2U6HXntl4zzAoaEL7zZvBGF92rnyEbJmj5BuCkYzgAvPNkuL0RV2NQNx2rTsKPnsxiPnq8NxGriI62yb5MCu1xsmbICM36z0BQ0OiYKullgvZNoPkOwwK3yMKEdgS2CiIQhn_2fME-LUZTj5N4VdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/217ca78a6f.mp4?token=kTZ3gu9cD6CAD1xNS2HVsbEfGYcm335yC8eZHJNK86MkPYQ1PD0SzAjuDjD8hMRe086oxcXUdACQbK-kbcBPoP6QDpLa5rGFCo3NlvUBEAZTN8VDWFlhMzLrfni4fup8C_6phN4HlWVITBMTn7avmQ9d0_yHh415a3sUwVl2haXVgKq-xG8IRHKyDzfmPTLUt2U6HXntl4zzAoaEL7zZvBGF92rnyEbJmj5BuCkYzgAvPNkuL0RV2NQNx2rTsKPnsxiPnq8NxGriI62yb5MCu1xsmbICM36z0BQ0OiYKullgvZNoPkOwwK3yMKEdgS2CiIQhn_2fME-LUZTj5N4VdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ قمارباز در گفت‌وگو با فاکس‌نیوز اعلام کرد که امشب آمریکا به حملات شب گذشته ایران به اردن پاسخ خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/685872" target="_blank">📅 16:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685871">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_BubDr2amBs8XN3iG2Cy0rAiknYtc213WbYlLIDHJvvPBaA7aGdaB053sqCPMNI37jZpmZ6uLZPgtQafX1nl_sizLGR8mNZf1IRljc61Ns-bGZV59qcNWW3dF-tOISJltYzEkgiRfsUsuiipDy2LOHK0fiLVKqAkz5-JRnPGGIJYLXcqYlTM2b8H8DCGditWkBwww_SzidE24wDkxD5lA6EAHYFoalGp22VPr1dg26FLJsvKbdO3NVT7SfbBkzyIvNcHwLBpLq2dVuODdLG1-MXS47CvBEFO6DHjmG8E--iUk1S1A5WGEIm4sT0r8-kF6F6W7NVHmUbR10oyRmNfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در آیین امضای توافق‌نامه بازسازی پالایشگاه پنجم پارس جنوبی (فازهای ۹ و ۱۰) مطرح شد
🔴
مدیرعامل بانک شهر: حمایت از بازسازی پروژه های صنعت نفت و گاز را مصداق جهاد اقتصادی می دانیم
⬅️
توافق‌نامه طرح بازسازی پالایشگاه پنجم پارس جنوبی (فازهای 9 و 10) میدان مشترک پارس جنوبی میان شرکت نفت و گاز پارس و کنسرسیومی به رهبری بانک شهر با هدف تسریع در بازسازی و بازگرداندن ظرفیت‌های تولیدی این پالایشگاه به چرخه تولید به امضا رسید.
⬅️
به گزارش روابط عمومی بانک شهر، دکتر سیدمحمدمهدی احمدی، مدیرعامل بانک شهر، در این مراسم با تبریک سالروز ولادت حضرت محمد(ص) و امام جعفر صادق(ع)، با اشاره به نقش بانک شهر در این پروژه ملی اظهار کرد: برای این بانک فرصت مناسبی است که در همکاری با شرکت نفت و گاز پارس، در به سرانجام رسیدن یکی از پروژه‌های مهم ملی کشور نقش‌آفرینی می‌کند.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/akhbarefori/685871" target="_blank">📅 16:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685870">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdQ_wTc88kFqDBJTLoGtkJpJLIODQyFydA7g4qxWAX0gYZp6ZPx2-v_8vvm4JvlKh3e6uuFr7KZCvtlXC-YkHMOaW1_55mdRepXVXxewXqbrVGRHYkAg0QqoTAombjl-_vc3xH64RlYYxrU1EtAoC4M7-B5uxKQznRjzEONYerpuAgVJ2Y5-j33-FReXXZ-3kmwq_7WBNhwIHYHm84JAyrteD9vUnttaV7z8rAAPK_gjEqLsqJiLj1BleLjuMPbsFUuXsw9HxLPKIbE8KtPDTPvBPEG2Vh7oHYUpGezi5DXFF6eDjJT8GNyb2o90RpV9Fq7d9lVoQMKzRb7b2omeOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری یاسمین‌ پهلوی برای ایران
🔹
‌یاسمین پهلوی استوری گذاشته: ژاپن دو بار بمب اتم خورد، پیشرفته و مدرن شد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685870" target="_blank">📅 16:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685869">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3kIbApP5IDtUfEUktvmA0YgtZSknZD-MRFDv9_YdBXIPj07K68JEmG86fpJkiPcSbsOCVyVsNXp92ATsIYxn0674R9J3ezGQy2UVBhywxkQLXEBGM43N-9518JQbj5EBczReUT4iBp3BkEfnCPGNpV4DNINQEXOfDDvYSzNErBpp2w9LJwkY3wDTSmG-EkUz6abtUqPfn0Mbsdb150gLotzW6NmIJARpBj2dF7y9w0HLCV6eTtTeGFCmawsDEwwdzJJH7GVTRFFtGEVl8GBcO105WqyqBEe0LP4Xc4OU25iFkEDzkfqqNvWNuFKTmrCZSmiHw-sA41PRKbEx_SFiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعرفه واردات خودرو در سال ۱۴۰۵ چقدر است؟
🔹
تعرفه خودروهای واردای تا پایان سال ۱۴۰۵ تغییری برای واردکننده های داخلی نخواهد کرد ؛ اعلام تعرفه های گمرکی برای واردات خودروهای خارجی توسط ایرانیان مقیم خارج از ایران از پایه ۱۰۰ درصد شروع میشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/685869" target="_blank">📅 16:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685868">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هی ترامپ منتظریم! ما جدی هستیم!
در پاسخ به یاوه گویی دیشب ترامپ:
🔹
واقعه طبس و دشت مهیار اینبار در خارک تکرار می‌شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/685868" target="_blank">📅 16:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685867">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دانشگاه هرمزگان: کلاس‌های دانشجویان در هرمزگان مجازی شد
🔹
وزارت صمت تعرفه یکسان ۱۰۰ درصدی برای واردات خودرو را تکذیب کرد.
🔹
جاده چالوس از ساعت ۱۶ امروز یکطرفه می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/685867" target="_blank">📅 15:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685866">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
وزیر نیرو: پایان قطعی برق از هفته آینده
🔹
در صورت سپری شدن بی‌حادثه این هفته، از هفته آینده ناترازی برق در بخش خانگی و صنعتی نخواهیم داشت.
🔹
شرط تراز بودن، مصرف درست و پرهیز از اسراف است؛ نه مصرف بی‌محدودیت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/685866" target="_blank">📅 15:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685865">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOPqY3rKIZeH9wXplC5V6hbIX3PjfOFPeB2qOIzlrCnNQVx3QMN0FAvz_t-K5SKnJeJEDdHTVWuecq1SjwbkEe-bWCX2KyOaSB-CmLZZtahEpBqLrwfOI7jcZ_2366cGrnKGHOgDJCwErsUEeKgKnqWqWgXWFpXE5r9dXQDZF9_iJd87qfrI7LWOKiPtqQX_yE_vSCVan7Jmu0mfia3hcPGC2C2zT0W1d2U8zrv4sgRF8uPSVMETsIcBKxSkhawm4-C_D25ZzZPQ9lbR0DGpSIHc7w2NUfi-nn-gnIBPktoIk60hZHSA4sQ_Vh5_jbd-zGjIUq26avq9VZ_EkMp_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش همیشگی ترامپ به شکست‌های میدانی؛ ایران مرده است
توییت جدید ترامپ:
🔹
ایران به طور رسمی یک کشور شکست‌خورده است. این کشور مرده است! آنها نیروی دریایی ندارند، نیروی هوایی ندارند، ارز ندارند، به سربازان و پلیس خود حقوق نمی‌دهد.
🔹
تنها چیزی که آنها دارند، اخبار دروغ از ایالات متحده و تمایل به کشتن معترضان خود دارند که اکنون بیش از ۱۰۰۰۰۰ نفر کشته شده‌اند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/685865" target="_blank">📅 15:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685864">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06872d2119.mp4?token=o8Pmx3GHAcTYqdGSUV9-S0iXLlcfCksR4PjG-dAcWjFZA0OHgZCK0V9K5RASeeUpGb6YTNMNiwJoBB252sQ8bFBnx4BlPMXJOgHpwvgmqZfp0EF19Xa4k60jaxl_1tuilLmP9gyXIist_QZxJFwk7-IJxzpdrYoOz9xkYbNn3b2GvweTh7MeuO_SAUINXkLiYkkwU1cJDs3Bn_IuaT0WH9Fiq-l3lUerC0hngi3PYtdpgH-h3oh4_y_4c81wOq9qSRtQP-eS4mqY6j7sjN-3a9F44ZT1hfMfN3duh_7XviTiOQCd_MDy9eW7YJoJGYFWEWugsGTA-nZkb7_BEz9VAjguyNjivHkEdWNYPCyAli9K2M3czdKMYCZeVsaB3W8vvqYmhQdi_XwULyzkjIVoyLYO2hnPMJskr0OH1sT2n38derH_r2z9N9ZTAlNXWWni_YGBKlGsjs6mj2JpQRqnIUvja3BVEpNxJYmbZQPxb0YqG5A13kvGXWou-c1VIs3R-HInxgDyYr1Dh6dC_4rnkU-J2DJk_dXRZTZy74toB9LNde1981ArcCv_24fE9lrxALZsGtEbmbyav0Qkr37hAR9tcVWGYED5sbiAp0qvhB8o0QoV9E_JVVT2JivUOs5wLSRzk1vx6YtdzMLvtRdk4nb-O0HD4uz4_kbuWTqA6S0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06872d2119.mp4?token=o8Pmx3GHAcTYqdGSUV9-S0iXLlcfCksR4PjG-dAcWjFZA0OHgZCK0V9K5RASeeUpGb6YTNMNiwJoBB252sQ8bFBnx4BlPMXJOgHpwvgmqZfp0EF19Xa4k60jaxl_1tuilLmP9gyXIist_QZxJFwk7-IJxzpdrYoOz9xkYbNn3b2GvweTh7MeuO_SAUINXkLiYkkwU1cJDs3Bn_IuaT0WH9Fiq-l3lUerC0hngi3PYtdpgH-h3oh4_y_4c81wOq9qSRtQP-eS4mqY6j7sjN-3a9F44ZT1hfMfN3duh_7XviTiOQCd_MDy9eW7YJoJGYFWEWugsGTA-nZkb7_BEz9VAjguyNjivHkEdWNYPCyAli9K2M3czdKMYCZeVsaB3W8vvqYmhQdi_XwULyzkjIVoyLYO2hnPMJskr0OH1sT2n38derH_r2z9N9ZTAlNXWWni_YGBKlGsjs6mj2JpQRqnIUvja3BVEpNxJYmbZQPxb0YqG5A13kvGXWou-c1VIs3R-HInxgDyYr1Dh6dC_4rnkU-J2DJk_dXRZTZy74toB9LNde1981ArcCv_24fE9lrxALZsGtEbmbyav0Qkr37hAR9tcVWGYED5sbiAp0qvhB8o0QoV9E_JVVT2JivUOs5wLSRzk1vx6YtdzMLvtRdk4nb-O0HD4uz4_kbuWTqA6S0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب‌هایی از حضور مهمانان، مدیران و فعالان حوزه رسانه و فناوری در غرفه خبرفوری؛ جایی برای دیدار، گفت‌وگو و مرور تازه‌ترین تحولات دنیای رسانه و فناوری در بیست‌ونهمین نمایشگاه الکامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/685864" target="_blank">📅 15:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685862">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcTeG21STxZKoo4bKNae8VUDdUcHIKfvA1okRmqn0v4aEXcPROOb4OiE-EqmR3aKRxlwHZmj-JXoFV4kHj7KWriFxM7HD_xpqh78IeMcI2bRkd0l-a5bTGfzJ7r4NM7p-RYjFEowVqtwHCZGahKVMoMdhrVGB6c1UvqzVKZlC86RnmB3KUxQKpbz1UcP3AfLGIg5G4919zIT0RtldEGwsWgGEHO8Rvu8VJjLSavPheArt4v2PqPtJo9QtGyrfPnDRPPpEhSYxq5FtS4xZvdxnZh5oYECkgWIb5XYJSVAXJBSdALwbGydBxWi7VVcbSktF9waN5O8lN1ugUElF7IE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرسرتیپ الهامی: ایران پیروز قاطع نبرد با آمریکاست
فرمانده قرارگاه مشترک پدافند هوایی خاتم الانبیا (ص) کشور و نیروی پدافند هوایی ارتش:
🔹
تجربیات ارزشمندی از دفاع مقدس (مراحل دوم و سوم) در زمینه‌های تاکتیک، تولید تجهیزات، پدافند غیرعامل، ارتباطات، اطلاعات، سایبر و علوم نوین به‌دست آمده.
🔹
دشمنان اگر خطایی کنند، حتماً پوزشان به خاک مالیده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/685862" target="_blank">📅 15:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd54215130.mov?token=vXYjE8fLZ10VuDe5FC1JvafL6gylxIvWbl5TX13jKWSN3TVwgtuKIPVjLpe_pALDXPx0PS1itHwxUbQ5LH8QSBERw-06f98DRdc1IDccckMugQ2mN0XsIfqo2SDHl-T93_OZSR3j0L6oi6HbnfxoYjjvc_PSuoyNEHets9UKPi9Vm68ioIvtRSHQjc0dRWnsNr-CkKhGGZnCxjLkBnyl9wroQPcV1P6mVyZlJFMjcD89_HBHZ5WzV8RTPSI53YtXwV3giGQMTyCA_vZ9M81Bjs62FlYVCr69UQvMEMQm9sVskiyaHIIBd6cM-vASAmM5LQVuatoFgBD_segaFkPiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd54215130.mov?token=vXYjE8fLZ10VuDe5FC1JvafL6gylxIvWbl5TX13jKWSN3TVwgtuKIPVjLpe_pALDXPx0PS1itHwxUbQ5LH8QSBERw-06f98DRdc1IDccckMugQ2mN0XsIfqo2SDHl-T93_OZSR3j0L6oi6HbnfxoYjjvc_PSuoyNEHets9UKPi9Vm68ioIvtRSHQjc0dRWnsNr-CkKhGGZnCxjLkBnyl9wroQPcV1P6mVyZlJFMjcD89_HBHZ5WzV8RTPSI53YtXwV3giGQMTyCA_vZ9M81Bjs62FlYVCr69UQvMEMQm9sVskiyaHIIBd6cM-vASAmM5LQVuatoFgBD_segaFkPiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیدار نخست وزیر پاکستان و پزشکیان در حاشیه اجلاس سران سازمان همکاری شانگهای
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/685860" target="_blank">📅 15:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBHz9aAx4h5udTrSqCqP3bouoEnHeDgNtcivJew6lHfwdl7_jokoVfrq936flQ_5RE8zZ1CFr5SIhFnpsHsJr052IBDu_wtpTevUlK7_fwJQxZ2j2p2TpM2mvAJVhZFYx_vWFl5sKFjc49B_kZ3R5KLmDSVRGzL9Vcyi_TRaUxBqIfQjMzT51IKiBzKeOoXY7KRAknmQ_5c4Q2-RcF7Zflw_ov7uqYrN4nhDmx0Yb4soRoHp_6YOqoI25QUFGDSZjmpLkzOvVTKG_0N2LaZPvbYzglT1x-IEpoCZWDibL7L5R_8xaElCcc2ewJmdx67QOWIKaJlQI8mpP3vDq09JEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرنگار صداوسیما: حمله به لارک در ۲ نوبت نزدیک به هم صورت گرفته است
🔹
حدود ۴۰ دقیقه پیش صداهایی در سیریک شنیده شده که مربوط به دفاع ما از مسیر ایرانی بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/685859" target="_blank">📅 15:17 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی به رویترز: نیروهای ما در حملات شبانه خود جزیره خارک ایران را هدف قرار ندادند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/685858" target="_blank">📅 15:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685857">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoqCpXTxXViEehrpvONpNFZbHVD9qlV9ysOKAl4KeMB_voqINa6GbjtsyLiI1Wg9LJ5f-wHcTqFqucEJ8jBFhuWctIyj5XEugAlS3NsKwf4IisQyEt7anEVcfa_CfNjVvwtf7Y6St6cjyVZPH-QhXuvcaxTASo0u1L7kaVRiFZbEiVoGGA6zzNRJjWWRmdmyHMEJh3C_rawObdy0rzp259cUXolZzJGcBvbQY43hoK5ohmcTckw-T0JDmz2nGIvif31Xs33tC81_D7aTwkcBiVL4cisMocUoukXE5Imq9iET0A2eqxujz5_Ev67tnIxj_mpUNfeiN1u1EFqAVUf0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در صدر بزرگ‌ترین حامیان مالی و نظامی اوکراین
🔸
آمریکا با اختصاص ۱۳۳.۳ میلیارد یورو، در صدر بزرگ‌ترین حامیان اوکراین قرار دارد و بیشتر کمک خود را در بخش نظامی انجام داده است؛ پس از آن، اتحادیه اروپا با ۱۱۰ میلیارد یورو در رتبه دوم جای گرفته است.
🔸
در میان سایر کشورها نیز آلمان با ۳۵.۴ میلیارد یورو و بریتانیا با ۲۶ میلیارد یورو بیشترین حجم کمک را به اوکراین ارسال کرده‌اند که بیشتر آن نیز نظامی بوده است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/685857" target="_blank">📅 15:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd472da21.mp4?token=RfchNf-zpz2qO3Uc-swo84Fgc00BkIIFUjtACCY2xANlb4D3whV-sYkEtB4W6mZkGT4Lt6F4kMQ5iUpgpLqYJ2qpwvakvfZUHTLN-SzZfVHMtzHXPpDwhPeDIDByRKitGSH-VAcjKeeG6HEWL2gBrwyqIjfbvx18b0AKcPqZJHSbJRr23X2akEyLllapSNxLWjL--f13luwPS_stEVIRwdoSkvvn3VAIPn2qynBp4B02-YtYjOECnMyYUu9JUwcBUYVbw9ZseJ1ZXI7xM5WcaCCMey0RYA77SkjvVjObDnJSnVb3UQ6mTMVlrf6ZDUKUJxFurR2QDCPHib8hR4M_HAmX-ewhERnqUcMUR2icm5yFuDQnARKpcRH6pz_0fUrPMcnLLPkNBpdg60kXwP-xzsqIDTzxlfw3dBMSU7xq43FkKNdTJ1UF9zAaz9Liju7gUsZXiMI8gjwJG3NF1u8TIyAOKrz71ds2jDP7c8KOekqpRTgcQxLgwCYAsNsiJqkhZxJzka-lGnoQ4s1MODn1yaQpoinG5H_85FxRBvQuclJ00V1cuWp3FIPlcb7yA4CPig7x70qOsgZNBZ2SzAgxDbimCnWT_208rBn5j7M9zyYV4VxUneA5qNNb66D3WPQpx6lbgcZEus3fZBwHO7AyT6a6L00xyB5GtpGyh4kgM90" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd472da21.mp4?token=RfchNf-zpz2qO3Uc-swo84Fgc00BkIIFUjtACCY2xANlb4D3whV-sYkEtB4W6mZkGT4Lt6F4kMQ5iUpgpLqYJ2qpwvakvfZUHTLN-SzZfVHMtzHXPpDwhPeDIDByRKitGSH-VAcjKeeG6HEWL2gBrwyqIjfbvx18b0AKcPqZJHSbJRr23X2akEyLllapSNxLWjL--f13luwPS_stEVIRwdoSkvvn3VAIPn2qynBp4B02-YtYjOECnMyYUu9JUwcBUYVbw9ZseJ1ZXI7xM5WcaCCMey0RYA77SkjvVjObDnJSnVb3UQ6mTMVlrf6ZDUKUJxFurR2QDCPHib8hR4M_HAmX-ewhERnqUcMUR2icm5yFuDQnARKpcRH6pz_0fUrPMcnLLPkNBpdg60kXwP-xzsqIDTzxlfw3dBMSU7xq43FkKNdTJ1UF9zAaz9Liju7gUsZXiMI8gjwJG3NF1u8TIyAOKrz71ds2jDP7c8KOekqpRTgcQxLgwCYAsNsiJqkhZxJzka-lGnoQ4s1MODn1yaQpoinG5H_85FxRBvQuclJ00V1cuWp3FIPlcb7yA4CPig7x70qOsgZNBZ2SzAgxDbimCnWT_208rBn5j7M9zyYV4VxUneA5qNNb66D3WPQpx6lbgcZEus3fZBwHO7AyT6a6L00xyB5GtpGyh4kgM90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان لو رفتن آرشیو قبل از انقلاب صداوسیما و سردرآوردن فیلم‌ها از شبکه ضدانقلاب من‌و‌تو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/685856" target="_blank">📅 15:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685854">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58aa20e786.mp4?token=Q8fXbIheXq0Lqc0J47tp2CSYGFumDkQylhUMcJ9poCeBt-L9LxY7714Ge85lgjK9Ofnuwv2pBkQb0HrMnC65KwoEv-bTIp1k_Ofxll2Y0SybyJwadCxE6kf2Mz4wIiWk6LSeE5gUzWwZHfvziQbpJ_OfNu8V0-KAoaW1bB9EQuF3i6HvvEi2DUwF413be8iIyD-cEfLiVzzbZJZzyCKsmOejl5qEyKLa04z_iKzMDaQWmsmGj7c7HASHwxgJbahEstddwYl8XJLisV8j4jcRk5w_6S9M_cB_reI8fF6rndeByT3TU971pYEHuT0sG8Y4cwFOtp9u0qxuk9xS1_sn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58aa20e786.mp4?token=Q8fXbIheXq0Lqc0J47tp2CSYGFumDkQylhUMcJ9poCeBt-L9LxY7714Ge85lgjK9Ofnuwv2pBkQb0HrMnC65KwoEv-bTIp1k_Ofxll2Y0SybyJwadCxE6kf2Mz4wIiWk6LSeE5gUzWwZHfvziQbpJ_OfNu8V0-KAoaW1bB9EQuF3i6HvvEi2DUwF413be8iIyD-cEfLiVzzbZJZzyCKsmOejl5qEyKLa04z_iKzMDaQWmsmGj7c7HASHwxgJbahEstddwYl8XJLisV8j4jcRk5w_6S9M_cB_reI8fF6rndeByT3TU971pYEHuT0sG8Y4cwFOtp9u0qxuk9xS1_sn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حواست هست عدد روی لاستیک ماشین، یعنی چی
🤔
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/685854" target="_blank">📅 15:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685853">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی فیلیمو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ea3sLVXyFQbtOjZfoyJSFLXa9-n48JsbKxEBq1BApiXOMVn4nqw6sfe-u4zDd7ewxd9vu5WxwYC_YlWwPiB2DXAD4ytSVpa_eAmKOSj-r9udpLRT936KNQuaSwCDLtSeQvbY23yP9hYLJ8-OSlJGudw9t0KkRGdqmo4ADB-7izboa8ZthWxXBvtoPhOIjhnBdghOrO6wNaCspkyHWRCIQxvxOr5WhefIja3HFFchw_wgaXyptszN8JYNLWjiCXvT6GlqHRI7GjQOsnQxMpIXGr-qMqvBkN1JT3t9NN3fv-OYjtA9FcLRD96ilEn0NLmNtxLMefsmKcRO3q43ku1SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ۱۰ دقیقه تماشای
#شفرونی
سفر استانبول ببر
✈️
👨🏻‍🍳
با
👩‍🍳
👩‍🍳
دور ایران می‌گردیم و با
#فیلیمو
قراره سفر استانبول یا باتومی بریم
📺
⭕️
فقط تا ۲۰ شهریور فرصت داری یکی از  برنده‌های ۱۰ سفر استانبول و ۱۰ سفر باتومی باشی؛ اونم با یک همسفر پایه و ۵۰۰ دلار هزینه‌ی سفر
💸
🎥
r.filimo.com/Tchefroni3
@filimo</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685853" target="_blank">📅 15:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTdMqjR77kuvV8IBXbiCjFlBm_Xlpn1iNCsHRD4mJfxpsNd7yJxZBwY-TIg50wUkG85H33XsDo8H7lvDppNN1-3Rmtc20KNCUPRT345D7bxczvwLV4EjBb5X3yaSwMiVDLOED1FSELiVLL-YVGtkmsX9IJnQbDpJTcut2Y4gSxRgYg3cNKJdDj0eP3BzLtW1uXrJMrbMFskmqnacoXFb5ujC_CRWackrMAWv4oTrbj5VsV0QMsFR9fH6PwlVLBAyPHtsNywV7FyKN7QbgtI0JsGkf2NF2JrU11D1-TzuIBr9Eai-X1RY15DxM7e4giD1LVJy2Bl9bhC5EOMGy0MucA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«به اعتبار تارا» کمپینی برای زندگی
🔹
تبلیغات محیطی کمپین جدید تارا با عنوان «به اعتبار تارا» در ده استان کشور اکران شد. این اکران، نخستین فاز از برنامه ارتباطی تارا برای معرفی کاربردهای خدمات اعتباری در موقعیت‌های مختلف زندگی است.
🔹
تارا در کمپین جدید خود با عنوان «به اعتبار تارا»، تلاش کرده مفهوم اعتبار را از یک ابزار صرفاً مالی به بخشی از تجربه روزمره خرید تبدیل کند؛ تجربه‌ای که می‌تواند قدرت انتخاب و قدرت خرید افراد را افزایش دهد.
🔹
این کمپین با نمایش موقعیت‌های ملموس زندگی، از پوشاک و خریدهای روزمره تا کافه، رستوران، خدمات و سفر، بر این پیام تأکید دارد که اعتبار می‌تواند در موقعیت‌های مختلف همراه مصرف‌کننده باشد.
🔹
تارا امروز با بیش از ۱۱ میلیون کاربر و بیش از ۲۳ هزار فروشگاه و پذیرنده آنلاین و حضوری، خدمات اعتباری تا سقف ۵۰ میلیون تومان ارائه می‌کند. فاز نخست «به اعتبار تارا» در ده استان آغاز شده و در ادامه با تبلیغات دیجیتال و ویدئویی توسعه پیدا خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/685852" target="_blank">📅 14:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685850">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c0670b65.mp4?token=uVlnIVDxBgv6ADFgRNkh8qsMYohsJ3KyTSaxkCVULds5G_Q9TijxBh6xPBXvHApP8mgQd8RWobkY05S-kmNwnGszMbisVd0uoeeKnsOgyi0I_zKtvakFdmtHCTogBbdcUjFH-aSRTyTazGZ47UBu-r8FdCbPN4urS3w5F-EamiNNN1_P0oz70kEvUJB3KOV6qdou3dWLiWKvKLI-AssQWaF7HJ6SkNs9bkTX2sQWvPETToFMgKiQSGFAKBa7oI06Xq5PY-nyFvDVkle-7O_MAKFC7AMtK-vvnLwh8QP7FubxJsbF-wCEuOc-nbmhRu3-75BwH63OWVh_MoNl7Mk4sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c0670b65.mp4?token=uVlnIVDxBgv6ADFgRNkh8qsMYohsJ3KyTSaxkCVULds5G_Q9TijxBh6xPBXvHApP8mgQd8RWobkY05S-kmNwnGszMbisVd0uoeeKnsOgyi0I_zKtvakFdmtHCTogBbdcUjFH-aSRTyTazGZ47UBu-r8FdCbPN4urS3w5F-EamiNNN1_P0oz70kEvUJB3KOV6qdou3dWLiWKvKLI-AssQWaF7HJ6SkNs9bkTX2sQWvPETToFMgKiQSGFAKBa7oI06Xq5PY-nyFvDVkle-7O_MAKFC7AMtK-vvnLwh8QP7FubxJsbF-wCEuOc-nbmhRu3-75BwH63OWVh_MoNl7Mk4sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمید رسایی، نماینده مجلس: هم‌راستایی من و اسرائیل مثل داستان دویدن یوسف و زلیخا به سمت در است
🔹
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685850" target="_blank">📅 14:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b283d953.mp4?token=gHaa-BkhcOJLI0_Z8qK5f2_I5yJkAo-MaId_pPL-zPoGKyVpjc0dagPgLf9jWXo7hP0TXJI9uVVkqoaCAY1mxnFWCIqavCSSeAY5JVoM4b-62yupGHrtQFHwOCyzwwy7rI6wxO0UyaL5Tdhz0vRgGC3XSIhyo_XWzsAp0woaWHWR0ExwGvHnNU5GHfDrSDH-pAHWPjdlwtKUesuH_mnwVYUdfbBf57ixYL-CwfiMMvo3zpZDn5YbC85m4apJFJxNPCDZtbejB7SDGZenztpwgGbppUH8cKlxRYktvjHEPYmnKm23VwDEhZkJ01CS183ooULwUvSW8c9n2ujB2ahh-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b283d953.mp4?token=gHaa-BkhcOJLI0_Z8qK5f2_I5yJkAo-MaId_pPL-zPoGKyVpjc0dagPgLf9jWXo7hP0TXJI9uVVkqoaCAY1mxnFWCIqavCSSeAY5JVoM4b-62yupGHrtQFHwOCyzwwy7rI6wxO0UyaL5Tdhz0vRgGC3XSIhyo_XWzsAp0woaWHWR0ExwGvHnNU5GHfDrSDH-pAHWPjdlwtKUesuH_mnwVYUdfbBf57ixYL-CwfiMMvo3zpZDn5YbC85m4apJFJxNPCDZtbejB7SDGZenztpwgGbppUH8cKlxRYktvjHEPYmnKm23VwDEhZkJ01CS183ooULwUvSW8c9n2ujB2ahh-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف عجیب در اتوبان ارتش، تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/685849" target="_blank">📅 14:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685845">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رئیس
قوه قضائیه: بخواهند دوباره در داخل آشوب راه بیندازند پاسخ ما از همه دوره‌‍‌های گذشته قاطع‌تر خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685845" target="_blank">📅 14:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685843">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IzgZl5gfe9-KLHAInwPM6Vu8h3mD6ETocyTNuRkwFJoySyHl-osd5OvnorJdp5MrWpKJHrg_NrFnPmQ5MBSh_nSDG_IlnHe8wqufXlvQN-61L9ikeCuDiEGlByASBMgzeG4W2gzH6xCZGnDL1_7oz_wDocJwmojGOPNpAU6cmleBbJQNz-LXWeZ51_dD8mW-AQIoYtZP3_NZodc10xcB6hzxahEHK-o4ERDlmypZBIf6kwoVrYz5FqHOdHjGORA6FhCw1yzhDjZ88icrH9aOFNNDFRmKNVcaGfrK5PGoxaO_aRgS2vTfLYfMMnFilullOf_41qhVAkC7ZL9_zzlTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IzgZl5gfe9-KLHAInwPM6Vu8h3mD6ETocyTNuRkwFJoySyHl-osd5OvnorJdp5MrWpKJHrg_NrFnPmQ5MBSh_nSDG_IlnHe8wqufXlvQN-61L9ikeCuDiEGlByASBMgzeG4W2gzH6xCZGnDL1_7oz_wDocJwmojGOPNpAU6cmleBbJQNz-LXWeZ51_dD8mW-AQIoYtZP3_NZodc10xcB6hzxahEHK-o4ERDlmypZBIf6kwoVrYz5FqHOdHjGORA6FhCw1yzhDjZ88icrH9aOFNNDFRmKNVcaGfrK5PGoxaO_aRgS2vTfLYfMMnFilullOf_41qhVAkC7ZL9_zzlTsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فاصله ۱۳ تا ۷۸ درصدی قیمت خودرو از کارخانه تا بازار آزاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/685843" target="_blank">📅 14:28 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685842">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkStXGDKGpa7o4Ko5D6kRXMBh2fmyv8HKDDwAp1lFRyaFXwAw15b30it1Ph6kOd7bi6_R88ZwageOdxRu4l3GSX_tfMOa7zlRb9fUcqgWzKoKaQ6zDWhbleJIqIqGRcwRlZz_45azS7zT_C9wBDfmp_FGmA-NDy2JweWwQDUdJZgj0y66LTBADk2rBVdNwLuP6ssRvPN8htHJFlqdMBKQHwwms3TLYdD3iszPBEndpnJeNS-dt7yh8QmR7OUkOYU2cCihSSxLnSTIzhP1SZkuGsNSi-BFw4MkNN_49LlHHiqY0klu5nGZhcsRXgZKL2DLnm7SE2XQKLOknXfyj9-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پتروشیمی دهلران روی ریل جهش/ از الفین تا اوره و آمونیاک
حمزه کریمی، مدیرعامل پتروشیمی دهلران، از صدور مجوز طرح اوره و آمونیاک این مجتمع خبر داد و گفت:
🔹
پتروشیمی دهلران با ۵۵ درصد پیشرفت فیزیکی، پس از رفع موانع خوراک، منابع مالی و LC و با سفارش‌گذاری تجهیزات اصلی، وارد مرحله شتاب اجرایی شده و در صورت تأمین منابع، تا ۳۰ ماه آینده به بهره‌برداری می‌رسد. این مجوز، گام مهمی برای تکمیل زنجیره ارزش و تبدیل دهلران به قطب‌پتروشیمی غرب کشور است.
🔹
کریمی تأکید کرد: با رفع چالش ها، تمدید تسهیلات ارزی و ورود جدی سهامدار به تأمین منابع، پروژه‌ الفین و واحدهای پلیمری که روزگاری با موانع متعدد مواجه بود، امروز با قدرت در مسیر اجرا قرار گرفته است. اوره و آمونیاک، توسعه سبد محصولات و تکمیل زنجیره ارزش، افق جدیدی برای اشتغال، تولید، ارزآوری و خلق ارزش برای مردم منطقه و سهامداران صندوق نفت ایجاد خواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/685842" target="_blank">📅 14:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685841">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfcc66647a.mp4?token=u8T468Ll4WTO-l341NYdduaRca-kChmJ386H2PuKD40oJtrMUeSJi96SNF0NSU_yUqoXpwjj_yT_LuPs9s5tD2eI7r6QP85NGwrRL_hwAW6KPmSyV5rl0ButTUbF9eXrmsbtSh3N3jtx5PmrVWzrLtIfRnOmWL5XBV1cUYbrYBkmdG4HZ7U-RoXpYpNE1IJrTSn4wL8T0GWqatiFe9sDBQsDd7brL5_vyWtWGfsJ3bN4uF5oAsi1BtajM1V-NjdlD_XPafsn10rSUsBg88SETz9DTzQxmRyHw3msoJVF_2VrAO6Lx5RntmdU12N4S9JnO_f_LDs_LZXZ5lrkwweFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfcc66647a.mp4?token=u8T468Ll4WTO-l341NYdduaRca-kChmJ386H2PuKD40oJtrMUeSJi96SNF0NSU_yUqoXpwjj_yT_LuPs9s5tD2eI7r6QP85NGwrRL_hwAW6KPmSyV5rl0ButTUbF9eXrmsbtSh3N3jtx5PmrVWzrLtIfRnOmWL5XBV1cUYbrYBkmdG4HZ7U-RoXpYpNE1IJrTSn4wL8T0GWqatiFe9sDBQsDd7brL5_vyWtWGfsJ3bN4uF5oAsi1BtajM1V-NjdlD_XPafsn10rSUsBg88SETz9DTzQxmRyHw3msoJVF_2VrAO6Lx5RntmdU12N4S9JnO_f_LDs_LZXZ5lrkwweFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگین‌کمان ۳۶۰ درجه‌ای خیره‌کننده در کنار بلندترین پل جهان در چین ظاهر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/685841" target="_blank">📅 14:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685840">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
وزیر کار: امشب معوقات بازنشستگان واریز می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/685840" target="_blank">📅 14:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udiSFoDumhGYtUORL6iHbbaqqLP0Kvpbe7e12o8BJvKiGmWy1UA8jzig1nD7X_KKfT1PCDwQMsC1H7mAhYxwI-WxypPxy_rHh0mlXWyEspGxnCltC-6MQ7lCrHg_56ssbC0ao1HBiPj3sGwpqT_cROmaCzQGl35-jIWk1q8JtACyLlOgTRQArxrlQblHCb_Ciqtbmd0Csa6bxdsQCrTdffxHiW2Q6jH3f-OuS_PzRDdgw6uS3VU_8DBeT_cWefiriPspY8nyo4jgHbgIMdaK_sfYQYun2g_TWM39F_tTAOxSl4W9P4ZINhZTDtV03qMPGyRepwdfW5Aq9bly3i3sjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m83KfHSfLBfYqArnqn5QjVFiogPDxpttGaYkz_X-0nZ71TN4pZUTKvS9_6TnYJp_4kD-N-vd-i7KsZSS50lJdYWKg7vORIb1MmYkcKHeJ9ShLnauo1tuTM5n2-1GiaI6cYiZg1AVbUCV1uRgueNsQiAMEIgoiz_CgTK-_fZceA3Wfc-EYQF3SWCeAhq5H9rrdG-7Q105Ih7yup7RYd2dbMWuDkM0lnPOyIaNHPH3aEoPyqAVMNch0Rcb5lnT_dEkKTjdIIS2v9VCHEFuIpcyaaVA2ikJc5_AHrhBqhY18Sr1G2aGjFAlw5E2QEvhoXlqG12Mwr5GqZVcDBBD1FZcQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DK6PgDO5H4u2YZwR0qut_7rFsnfCii35gCqYB9KaYRDlmsyeMLU--Ie1Ct5SMp1Hc9v6QqFp6caCM7ezdgXViIO-ajk3CJ-M53lCkIwNWULfUoCtXrdOoPXSeO7L9_xKOknVCNW6_tIw3ezTp3DACH-XXqQVrDGxLmGZJK-6uURxbuf3rTUBtwVWi6AjASQ7R-JAEL-QvOO2-rVkIcmyXNFpLcvWGkMEtf82MYpp6z_Eeo69kpD9bUd0n5haBBZ0GlO2zp0sG8zD5Hr1BiVtYWIU5O_I1HVhgSv6E92xofLqk06UDMyNJcj3iZHzyB13Q8mdnvdnCMqPMRVXF6Fr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPM_zzKTGOAWVs_K9YstzCm7ZR1KlEpt38dMc5su8wjqZw2IOXSrJhr5IjjF71vpETBnrS6SWtEck5NcB45F4y7QQUFhz6Ma-P9DGc8GLoJx45-5i1QUCaKBuP9AUWs6278Ss-q--hw8Rg1pykW1b8w-8V5PRPEehh3pM6D9aBSQEMjXeOQtBpoj294WLVL6xYsCQKq20wwctCYDlrWgp7Eno9ZS3mrHjppnEpy2M_cjy_27qoEQENmOSNFeAkncTCS19AGp2SDe6XAh5VBb_YiAKrbvFlwResxOWF7CKjdMCD1aWhDtRYueJoCITaoGrJMjv-Fo7fJIliZ8p0zBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUoS9ZaV2mgb507WK-jh8o3Y6BPKQGHSFvyVRQAadRXKG9siH3pDEJNOgt84erRDmoUNSDFZHFmmRviOTPToMTEuFLl3NP5I2WiZVjyVR7wRVkp1K48NCWK2gRiUlueB-6ncEAWSG2lPL_I5OsSNJTxol2AwaSeLsP2zN7lAyVSf1goauALDqjfgPZUdNGl1sme4O1U4ASSi_msWfCYFhU5Rqq0O6l2VAlbxIyYEjSCqj11LWYn7w96BYrAFxMSDJxM2olc36rIqCkG7ncjF6QcYZOEJycQkIbROEliURE3o23V30qQH2HbErWsXpYbUMKVWAYHppC3S9M2k_f_Row.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این ترکیب رنگ‌های ترند تابستان، شهر رو زیباتر کنید
🏖️
#فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/685835" target="_blank">📅 13:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DilesQDA5edGaDm1xDlB16fau18CAxy3KDbGV5R4iR7LuJDjKRMKfVUvmOy7PUpfE68xNtVtKzt4_CDdWIJBnIveIP25vnTlnLTzuC2n_TH54h40jKjfU35Tf5D-FTbomwkd5mCXoZD0g_6pYoHNJ78YejGhMhn_R_KwzrV1nvN5iIqpz8_E4SRvomEWmH3us6u65L6zjIel8rgvKqwWPnUw6tLdC_mDVFiNpJ20odHoBO0mg07jav32715G_TuzmxCprUR2ZwXBosEd2aJYeUmdMpcoDRQi9lu0nQwv3VPCisjyHztIsW4img1SiCOn6cfeAWkZBeJilFgkXUD6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره‌برداری از ۲۵۶ طرح تولیدی با حمایت بانک صنعت و معدن در دولت چهاردهم
🔹
بانک صنعت و معدن در دولت چهاردهم با هدف حمایت از تولید، توسعه زیرساخت‌های اقتصادی و تأمین مالی طرح‌های اشتغال‌زا، زمینه بهره‌برداری از ۲۵۶ طرح تولیدی را فراهم کرده است.
🔹
اجرای این طرح‌ها با حمایت مالی بانک، زمینه ایجاد و تثبیت اشتغال برای ۱۰ هزار و ۱۲۸ نفر را فراهم کرده است.
🔹
برای اجرای این طرح‌ها، ۶۴ هزار و ۶۵۴ میلیارد ریال تسهیلات ریالی و ۵۷۰ میلیون یورو تسهیلات ارزی از سوی بانک صنعت و معدن پرداخت شده است.
🔹
بخش قابل توجهی از طرح‌های به بهره‌برداری رسیده در حوزه‌های نیروگاهی، زیربنایی، صنایع شیمیایی و صنایع ساختمانی قرار دارند.
🔹
بهره‌برداری از این طرح‌ها، گامی در مسیر افزایش ظرفیت تولید، توسعه زیرساخت‌ها، ایجاد اشتغال و تقویت بخش واقعی اقتصاد کشور به شمار می‌رود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/685834" target="_blank">📅 13:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
آمریکا برای حضور هیات ایرانی در مجمع عمومی سازمان ملل شروطی گذاشته که مسموع و قانونی نیست
موسوی، معاون تشریفات و سرپرست معاونت سیاسی دفتر رئیس‌جمهور:
🔹
یکی از مشکلاتی که با ایالات متحده داریم، سوء استفاده از موقعیت میزبانی مقر سازمان ملل متحد است.
🔹
طبق موازین و حقوق بین‌الملل، آنها موظف هستند که تسهیلاتی برای حضور اعضای سازمان‌های بین‌المللی فراهم کنند، نه سفر دوجانبه است و نه ارتباطی به آنان دارند اما متاسفانه از موقعیت میزبانی خود سوءاستفاده می‌کنند.
🔹
اخیرا شاهد بودیم که شروطی گذاشته‌اند که به هیچ وجه مسموع و قانونی نیست و بدعت‌گذاری جدیدی است.
🔹
در حال جمعبندی هستیم که آیا شرکت کنیم یا نه، و اگر شرکت کنیم در چه سطحی و با چه تعدادی باشد.
🔹
در حال بررسی هستیم، تضییقاتی که دارند فعلاً در حد حرف است، اگه قرار باشد اجرایی شود، احتمالا باید تجدیدنظر کرد./ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/685833" target="_blank">📅 13:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSFs3qR0TdeOmEduUcp04WUIUt4Xa3bKXHCswN4RWx5PRCKWybP-O-VhN3clc5MfKcDoaK4wGM6efckYUzrK5polUuupfpZTF4hajwuWaXJjNR8_fydU8znMj8hMiQ2Piq_CUfxU8N3lUfVK2qYL5bnCYKPVtfeF3NvZSR549c739taNI7qfyVFd2jicez605CBDgtLpSmQ0S7RgQs9SbnK3ksH-1cX6nGL8a-JQfffjxQRm4z1m0bcKiYc-PMc0hgDKFpbjtAPCXpPeyBtM0FDn_RiNRg6AlM4vuNzVezHmuf9VHbyeAdUTeogUpNuUVWiV3mRnpbkFnJzS6xS9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان با نخست‌وزیر هند
🔹
در این دیدار، طرفین ضمن بررسی آخرین وضعیت روابط دوجانبه، بر ضرورت تقویت و گسترش همکاری‌های مشترک میان ایران و هند در حوزه‌های مورد علاقه دو کشور تأکید کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/685832" target="_blank">📅 13:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a7e418b8.mp4?token=Zr7vOIRCv9SsI8TFp_Ov3712W1RTtiQ5J48awJhZfteWZZ_45RZ_96sgmL7CQcV39pkbic7wrH-rnzI349AjpEzVvbEDVDr83tYmitHxduOr7GtAM3mm2OUwKZuMHrhej7ADuFpoHcaN7PwBpdygho5PjW_wtZVZ5HM66OqtAW5SqyQQX4C5sFyl4ZIniEUfIk2eDUdL-F9MZECjq6xxlY19-FvPWMxtGHDztqT-ZFAeSLrKRzK1M7tGKIMwTE3axRCV0nCvAGRkyv0Uq-nr6hmCFMNXkWn4LwRD9bns7qxNw8qKbzPcL1IWYE3QdMK5mz3VFZ19zguUZ4KzBFLV4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a7e418b8.mp4?token=Zr7vOIRCv9SsI8TFp_Ov3712W1RTtiQ5J48awJhZfteWZZ_45RZ_96sgmL7CQcV39pkbic7wrH-rnzI349AjpEzVvbEDVDr83tYmitHxduOr7GtAM3mm2OUwKZuMHrhej7ADuFpoHcaN7PwBpdygho5PjW_wtZVZ5HM66OqtAW5SqyQQX4C5sFyl4ZIniEUfIk2eDUdL-F9MZECjq6xxlY19-FvPWMxtGHDztqT-ZFAeSLrKRzK1M7tGKIMwTE3axRCV0nCvAGRkyv0Uq-nr6hmCFMNXkWn4LwRD9bns7qxNw8qKbzPcL1IWYE3QdMK5mz3VFZ19zguUZ4KzBFLV4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ساده‌ترین ترفند برای تمیز کردن و احیای اتوی سوخته!
🔥
👕
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/685831" target="_blank">📅 13:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685821">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkgqp0meFSgYR95vfRT2xakG4rHJ0RyYaSXjD32eAB19x2rqRcdyj0zf8X_fPec7epWcCcFnhjEYtz5NTRfLIJEWhlMW2aP0Z09QgoHaZxgxaGq6NkMkAKbrvavyMk4u2K-UKzCLn_DT5df_JK9UNGFkJbVeCGqhLqJp_zpk8Vv4iZeEdc9n4UP-2sXdX7b_vkoSErWW5gfBm-oZAkTH4BVhC4SSxgh96YX8XTra5SE5TdwACBNHmg2g2BnB7xGiAqGMfVfeUS8TyBu1rcXRriqzVrYgJApF0vHiHUhMqeaAf008h52OW6fn4uXPVeNi0iaOxpxrrl7NyicpBgyRUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qMxsQOLvs4QRppA9g59hZiw5CwWEM5-y8Dhd6d_YFXdkTGpgJfgdrQdNhfgYeQx17hTXOv928ygUHU9UHbaD-saSVmMTN1_HspWd7dROgjiELpFBIxLLHju9lDw7qOWojo0k4IazK0klTbXRTEMEfN0n2l8bXACiTwTt0bIyobmJlszQdNhDD_jLUsPNW7e_esUvcTNn3GKbsMTeAs9ApCHnIum8BG3ivanHgO4ntXKQJ29qqNCe1mxdRmfHnokh0iuDzsr7uwV9cFbn8Yu6xtUBiz09kxAZtddff9OMcX2Y74U-KsM6yhMLztsYlExfQRUVdyzwpH-D71onPe72zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rZh55c199TrNJvXfy3FVdP9_A0N5sMlKp8r_pQKJDo7Tfr6kqbT0567yH5nfBiJCgBeowsxEOedzGOf5hnk_8kSLOGTc5bsIvaF5-e7NkW5WS_JFMx1agKEHZKmnk5msG9I6Whr7BOunT3yfcjFjwQYjRrqR-g7OWrOMq7pgltnRrhDvuuNij249YU4F8HpKPgQ7bsU1-DTSpyitnMFtZLL2v20frPEywWitrkhp6L1pz7aZ9SWyCRtBGwK9sssTrAgjBLgSsJahieYHsAij_BxhHjLxeZ8Q-5sUaOSWy5f2K-zx75sEvIltXkBFmoDea-RFd7IQtfCflkoa6YfI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNqc6PPBMto6QYMeEdOXiTW0Nm7j3v264BdMiAl-krS4OCMR_ni-Y0r-f_SeOHVCSJp7_I2SmKbqpBqEXNbWrr9z0G0zD_hFeFbP-NXVBKLsWdN4ZVXVPMc50-LnLkbWOFBsN9AukIkIi_ZB6qMEoPL93_jR_vfKS1XPOLmGOmUCw1jwyVWgJ2MNq2hgFPsLOhkggJ142a__5N7qc5_mOc-JiuEhXpIpJqbMqu65vQndYbfVI9X_0j-fA5wezISLmqXLE6QKfGbqrY-QgF7MgA5Yg592ut36Aag3Ay8u27rf-wnnEaTvU0ei9xRV8NWkgaVTtUWenZ8lNWxIdQcntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q4TkncSekNY88lUgvRTZaHwITRQoklbD6BsY6AtOzTEYJ5hGhkN2NcCVU3tyy6iiieb5nu5f28AKhv7j_RCEcJmm-b7FkNaZIPSlgFjbtqPEOy0K8bHX4a_b1q44tq3m-2bsU0TSBIp_b22oatUvshWyKR-5DXL2Pc15-s7Jv1s_E6UJviGJWqVJkNp12-aIgCbKJq10J-KnxlQxx-vlslzjBBLINkaOAq96hjoPVx4pwlJIZ528j9hy8ycVPcTExx0vzkqf2TnrlEzNvaiFlkCV-f7YRwHC4WidtqPsIJ9NPoeynA0gtlN1j4-DeZLpVkYBVCWfb51TJ60oAGk73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FitS67fZBvrxd_5g6HvneymEkF7QuchE6yyZXnUDI_eMADQKWLQS0xtPcd0wbMAaYQzeowX1pkHXpuidH-dl4xziZT09AZsssrpj4amTWGsTG2qfGP0AO5TNAna3nLjgC-RQQiTtbWI3eI-ZyW0clzWvtvfOTsuAoha-tq-PyJmPAQLCDzPdLrABnLqaxjhC3GtN35sdUEMtvGnD-jXMhonvFhhT0upRAlEFbv8arl4kzRn-0wk10D2tIk34wmQWm5oFEsjSE7R23k3MjH3zTPhQSMGy7XSZs1-fLDdK4nR_OLtPEjpQjXXXwAKu2AP2NZLrstaumHPi_ggQVNn4iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JMm95JmBg5l9L5wiZGZf4VPzOMQBuW2aviv58ux8G-mleLppXmt9rTfkcPC3THaZMNP4djChsIJbgzBJEUUHG1wH8azYAwKv84iHG6iBW9pmShDfo_oUw150vZSXzKjRKH1udrFWX2z_DmQGx--2honZiG345fzUZdr3OHZSni37uYNqYNm1cgG46l8S23VHT93pq_krIVXvWSrSeKEledQYWjpqitElqEwrBplNnOKjBfovRuQLJ-TE-h1o-v5b2Nq_zfng-JQHk9wMHMJIy52tnhgJ9YTzgAeouKJxrPtHCyC-qGOSFyPovkPsCpN5Vo5f0Bb15qae6bdAVHDeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1qhAcnwj1VgrliY8oPCj8AG_GmOJiDV7dufvgHWXC8SLAb3GGZsPQjS1GVZyG71BWGlx7b6R_uzJVPy98LCjJz8wFd_qyfJwyUGIkd6r6-BbVrbCY6cIDkVARdmkrbY31ZXyfr_FUTaJRhstWO_1zifhmOkUdbjvq3I3f3OD_55XwqZ0A3qV0tfrSNvb9wQhSZxpq6yZe5OKbdIheXWvsPpMvTsJONPA_HjCgs7nV-aUahRdmOrp9wdRL2INXElX5lnbYwH6C2LWcoBd4RpJyZmUMl0l4Mg00mK4FVWg_QX1C2DA9tkuoqt_Oj1Ql1CProRmHo8BPnuyVPoWkva6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a72y9Qg5ysfXbskazGfhVtwsuS6G77QZAOqy5NNhQEMicrFuqSjnWWGfR5g8OJqPD9hgcxdxCsDLpGYzaGphiBg_DdIUY9cWEqRWTXxpk1IpN3rcBd0yCnXwROOY8qeRsD4uiel6L8HGWR8lzGVPThvsKzxF_Hr4wGX2I60SZSBb-nRtdomxfhJORK0cK8nMfHqDaps4WdGuo5dmJbt1THrF_YC3NXGbaj5Au3BitTw4G3hi14KqU-E6YDDb1Y1k3dUqIJFWNGZ7u4_u-do5NxOlmDL7D48P6oPkRizKuV9jQGP4Zu6DozaTNeQXL-BUUvbfg4jVMLgR9f_wlLUrVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSaa6xBx9CIq-EIhAD-xZkGL9H_RArUWb07G_KVwLbMpMR6e9mjZ82JKsCwviKbDro2ihYU9R0ksn7PLcjXTbs0PS7DZ0R6GCbcfn-WwGTC7lrNvGCT9iiLYYvxZuYQg14j-oV4OKZUcFWK_JUYqxdWsiUVLrirsGL0-fAaFnuJyARWWvsKTxk31UMQCcIkArAW0HqZb1SFVID51rXMb-nNdJ3G-67Ov1oWuUqTi7K8nwoUSEzXSesXP49u4S_ShVXgeW5xBS1NyUPfapyET_rlIeOLYIaIDZsLA_demi8osz--idaWhPH7zXZamWN-T4lH-1jVz8LLDnzAcznHxbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
استقبال از غرفه خبرفوری در نخستین روز الکامپ ۲۹؛ شروعی پرانرژی و متفاوت برای حضور در بیست‌ونهمین نمایشگاه الکامپ
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/685821" target="_blank">📅 13:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685820">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
هزینه معاینه فنی در سال ۱۴۰۵ اعلام شد
🔹
خودروهای سبک تا ۱۴۰۰ کیلوگرم: ۴۹۶ هزار تومان؛ رده برتر: ۵۱۵ هزار تومان.
🔹
خودروهای بالای ۱۴۰۰ کیلوگرم: ۵۵۶ هزار تومان؛ رده برتر: ۵۸۶ هزار تومان.
🔹
موتورسیکلت: ۶۳ هزار تومان.
🔹
آزمون مجدد تا ۱۵ روز پس از مردودی برای خودروهای سبک ۵۵ هزار تومان و برای موتورسیکلت رایگان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/685820" target="_blank">📅 13:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685819">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a206d8bf.mp4?token=nes_k0NZV4EvAol0YfZxj_URAz5nxE1Ur_RDvo363uv5cyfWeEuJCXqUaro9LSM09ZopfSRNDhkTRQfLViVLMgTs7rYOBiIGnXiDhM50BreYTuu8-ahbfircqJ_EXtdd0kK8zDjz9xHjUNf2r8IVX_DCelPDXNw1pfMUMvy3vcXtOzsD_c1KRJQER4srDccWd8brZ9w3XjOuPNcMSs7WhqpVjYIkIaOhLVQbcZzWbu5MRVqtpzlrIIRNOODxcXPVhFsp65L63w5t6jepHfJXvzVO3taMs1myqxjqbZHJWP_E32KU3J67aZ41jz4mfknal87Y8jXx8OS1Jj0RI-sIFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a206d8bf.mp4?token=nes_k0NZV4EvAol0YfZxj_URAz5nxE1Ur_RDvo363uv5cyfWeEuJCXqUaro9LSM09ZopfSRNDhkTRQfLViVLMgTs7rYOBiIGnXiDhM50BreYTuu8-ahbfircqJ_EXtdd0kK8zDjz9xHjUNf2r8IVX_DCelPDXNw1pfMUMvy3vcXtOzsD_c1KRJQER4srDccWd8brZ9w3XjOuPNcMSs7WhqpVjYIkIaOhLVQbcZzWbu5MRVqtpzlrIIRNOODxcXPVhFsp65L63w5t6jepHfJXvzVO3taMs1myqxjqbZHJWP_E32KU3J67aZ41jz4mfknal87Y8jXx8OS1Jj0RI-sIFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فندک هوشمند زیپو با نمایشگر لمسی!
🔹
این فندک علاوه بر روشن‌کردن آتش، امکان نمایش اعلان‌های گوشی و کنترل موسیقی را هم فراهم می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/685819" target="_blank">📅 13:19 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
یک منبع نظامی: ادعای آمریکا درباره حمله برای جلوگیری از مین‌ریزی ایران خیالبافی است
یک منبع نظامی:
🔹
اینکه آمریکایی‌ها گفته‌اند که "با حمله شب گذشته می‌خواستند مانع مین‌ریزی ایران در تنگه هرمز شوند و در این  کار هم موفق بوده‌اند"، خیالبافی و داستان‌پردازی است و درگیری دیشب ارتباطی با مین‌ریزی نداشته است.
🔹
آمریکایی‌ها از یک سو می‌گویند که همه‌ی مین‌ها را خنثی کرده‌اند و از طرف دیگر مدعی شدند که دیشب مانع مین‌ریزی‌  جدید شده‌اند؛ حال سوال این است که پس نفتکش‌های متخلفی که به مین‌ها برخورد می‌کنند دقیقاً چطور تنبیه می‌شوند؟!
🔹
آمریکایی‌ها شب گذشته بنا داشتند که از تنبیه شناورهای متخلف توسط ایران ممانعت به عمل آورند امّا هم در این کار ناکام ماندند و شناورهای متخلف تنبیه شدند و هم پایگاه‌هایشان در منطقه مورد اصابت پرتابه‌های ایران قرار گرفت./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/685817" target="_blank">📅 13:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bfef1058f.mp4?token=uXYCBQPnQmR075O6wqwG867CrHrjc81qcuNv8IdXjmMiKLTeMffeXf6lY6gYQWD6ZGEOmz8q-pO6vu6fqPBB6tklzGgsyJG0pM1JKwuFtsP8-BHbXS-wfC_Nnt6P8jmfm0cTGTzGvDMh5DaZvo-2JadhnhpQ6h-0USPU8F4hj0Bi-M1DDD-k84g9DsgVJhevPMblgoOp4fFUAYloDu3ASHYCG_n1tszEdtA-UaklBEuYbfjWx-pzTF5NqfGWk39OXisa8vzVqAqjVUHiw-9Sb6bVlFbR0TMjpP103muGPpMwtImQ2_uB2QHqi0-fF1WwhtHBSAQnoz8WP8W1r0K1Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bfef1058f.mp4?token=uXYCBQPnQmR075O6wqwG867CrHrjc81qcuNv8IdXjmMiKLTeMffeXf6lY6gYQWD6ZGEOmz8q-pO6vu6fqPBB6tklzGgsyJG0pM1JKwuFtsP8-BHbXS-wfC_Nnt6P8jmfm0cTGTzGvDMh5DaZvo-2JadhnhpQ6h-0USPU8F4hj0Bi-M1DDD-k84g9DsgVJhevPMblgoOp4fFUAYloDu3ASHYCG_n1tszEdtA-UaklBEuYbfjWx-pzTF5NqfGWk39OXisa8vzVqAqjVUHiw-9Sb6bVlFbR0TMjpP103muGPpMwtImQ2_uB2QHqi0-fF1WwhtHBSAQnoz8WP8W1r0K1Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پچ‌پچ موز؛ یک ایده شکلاتی جذاب برای درآمدزایی در خانه
🔹
در #چرخ_زندگی سراغ ایده‌هایی می‌رویم که با سرمایه اولیه قابل‌ مدیریت، امکان تبدیل‌شدن به یک کسب‌وکار خانگی را دارند.
🔹
این بار یک ایده متفاوت و خوشمزه را ببینید؛ ترکیب موز و شکلات که با آماده‌سازی ساده…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/685816" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBFSO6FmAMF-1unjycnLAunl9ZrZllhDbyY2tErlTUSS75HuULudR_OwrIPUCKpqjgnhbcyEnIuJ_ZDxQX4r2xziJVJXstA6ctt-PGleOlKiUQNfA77vVtTdDYfeeGlW_VSiQM5nIthDBV59X5OmiLFdIYO0_lkNIsRixFtMGvt1LHRnHWrGCgyC3eH9QFzQkjohW3peUOdGd5kRHSAKOggGZigTQQQHKMldoqhhwfzE8QO9etHemClVURA1A8oLJZWimsx24Bb_ZUHnLGuBUfGtRNK8mTnlhL2pGCDdcK827CLG29gIEPEkfhOB9SvC0n3mIB4UVk-gZhtpeNFKrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۹ شهریور ۱۴۰۵؛ ساعت ۱۲:۵۰
🔹
امروز دلار آزاد با ورود به کانال ۲۰۸ هزار تومان، بار دیگر رکوردشکنی کرد.
🔹
با وجود رشد نرخ ارز، طلای ۱۸ عیار بدون تغییر محسوس در محدوده ۲۱ میلیون و ۸۰۰ تا ۲۱ میلیون و ۹۰۰ هزار تومان معامله شد./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/685815" target="_blank">📅 13:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685813">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
قطعی برق مناطق گرمسیر در همین هفته به پایان می‌رسد/ ۴۰ درصد از فیدرهای حساس در تهران هستند
سرپرست معاونت برق و انرژی وزارت نیرو در حاشیه نمایشگاه الکامپ در پاسخ به سوال خبرنگار خبرفوری:
🔹
اولویت فعلی دولت، تأمین برق صنایع است؛ به همین دلیل محدودیت‌های بخش خانگی کمی طولانی‌تر از پیش‌بینی‌ها ادامه یافت، اما امیدواریم ظرف یک تا دو هفته آینده، محدودیت‌ها به‌طور کامل برطرف شود.
🔹
در مورد تفاوت تهران با سایر مناطق، باید گفت حدود ۴۰ درصد از فیدرهای برق در تهران به مراکز درمانی و امنیتی متصل هستند و قطع آن‌ها امکان‌پذیر نیست؛ اما سایر بخش‌های تهران نیز مشمول محدودیت‌ها می‌شوند.
🔹
ما برای مناطق گرمسیر، تخفیف ۵۰ درصدی در خاموشی لحاظ کرده‌ایم؛ یعنی میزان قطع برق در مناطق گرمسیر نسبت به مناطق عادی (مثل نیمه شمالی) نصف است.
🔹
هدف اصلی و اولویت اول وزارت نیرو در همین هفته، رفع محدودیت برق در مناطق گرمسیر جنوبی کشور است و طی هفته آینده نیز انتظار می‌رود وضعیت در کل کشور به حالت عادی بازگردد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/685813" target="_blank">📅 12:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685811">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6-d11tu9yz4g2uGMqlH4iThLcJfs04SGZ9_bhqPKJPur7NMl4cTlffPj9TM-U2qRJ4gjzt_ni7B9ltMrlBMqBEBYFAImshPJDcFBDwfZdMJHvrG5jRLDU57MN2SW5YMzFyj0DqtFEpuig8IL11js-6Qm-v9aNH_KiRMOVSPJo4gyJ1y6GgcLu3Lmox4JEh-bxO1zg73ezv5hifJla2bjNuwVG5BalpkPZuru-xmsXqc9if8zqNuUpz10rJK7NlpHe9Yva09ZX4M7sXeqtC6oPr3F7tjloGYSTwrgComWno7z5Opn4PGcLuy5c68iM-viBiSufb2PSKzF0852OYBHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8Le_dUb2BnsJ-J-1Xm3FEgTwel6qODLetjgpQs9wAoapw6i_d_KPd5EsjNfC2pqI0y1iQb2okqR58hKBI_KAkHPAJYTudX4AwkV_sRqg2q3MZuyydNwSDbfEebdQ5fMonUJ_raatJ1JDM3vKDBOGr4aklBr07bUIj4-W8rhf9SOBtu8hUB75ihTtbZPuhjY5VbdHp-RbVLlDbrGd6rItX8DhsN_rcyQu3VXNyin1-TLP6ZXGkc5YbisP8SuYCJHa74mYVCzuTntMYPr8hfRxNWH4ozRTgNkFuEKce3nvfyMBj4-YFeIzMmAs1B3lqLE0V2pNSg6qSG5Vx9BeFlx7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سرو هزارساله هرزویل؛ تکه‌ای زنده از تاریخ گیلان
🌲
❤️
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/685811" target="_blank">📅 12:51 · 09 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
