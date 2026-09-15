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
<img src="https://cdn4.telesco.pe/file/jnNIBoT0Zvav2-BPdLDskPicgRxBGg7VWJoqBzldU211QotPy8A9gfirYGFhBk2l51Pi6UojckdgLcPTG6Ru1nqPvIL8LlB3fvxj2D62At4rv3LcmA1JqiHa4gAAPRrdYCJ8bpANAuq7SIs0sLq6FzkJbRA5kxv58tblGhXzHBGjKr6P9_fxDyKF59MHVJaUmaTEANgNEkt1LMY7RjAV0HWNkcJaDN4hZkUpTenMEUd0oDfYAIGGQszpXP517msD42nVlFPdAEgbIhh35R8iP3wXiMrclyWPKBnmfggslqXmoAGLqOHqXsAUWTbEpnS-q34s-JpxZHuqkAfSUUUTOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.13M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 15:26:15</div>
<hr>

<div class="tg-post" id="msg-690113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
آمریکا اصابت جنگنده اف-۳۵ خود با «آتش ایران» را تایید کرد
🔹
پنتاگون برای نخستین بار به‌طور رسمی تأیید کرد که یک جنگنده رادارگریز اف-۳۵ این کشور در جریان مأموریت بر فراز ایران، «هدف آتش دشمن» قرار گرفته و آسیب دیده است؛ موضوعی که پیش از این تنها به‌عنوان «فرود اضطراری» یک فروند اف-۳۵ اعلام شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/690113" target="_blank">📅 15:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNvaMx9g7JG5iTbDn6wL9XNYsVdA0ZlVpWVBegMbtGFkozcEBwbDLw_hVo9EQyiTOydJi3QAewGBRQGBXgMPivpcsPrfx4C5EscpJ1sBpNN6wgC9UZ4nVCu5boZh4By64ZExFuJk2kleH5ml-s1hbaHIafAsjxUv0_p2vmsAGpL4bGTFIWX9SKrgxq1Dc4rKXV6f3Nts4mpfFjKn-05ZpLKdF8QxyOJARJuByADfXofX_ay5sx840tmi0NJXMCTy1T6fUJoAjon6Ii2NOlgHGzvHn4kwYo0XxcZuz8rwZyq48MORobJqBah59tzgfaIJ3D69oX6sriNl0k_J-khplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BurpcgSZuMxxK21Q9FSO8ZNyePrd2h7yJTWMZI2VsU58jP5LXCW0jFXBtxeiqs-PqxTskIbpzRndZnLelgJ-xnIGM3DsiU22gelVyj62VlEfzV6N3eaS-s3WsSBHULpsSZK5KUHRx6CEsFk1pvH-iu4i3wFa2AcfwoOSEbh5KWB2QncnluLlJe9hbSEYu5gXwRBM3UCUdpWrOl-h1SRIPifNNUGHAuEk1tnhkvIlyictLRjCqxfD2ljcmqfAag3lxBytoWIJUNa-Fq5pIZFmvDzT9YHulF1r2rtCxgq1-BohaILZ2RRKGqedKyfOpYYt20JOGxJ0pHfqvvHUEekkww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افت تولید ایران‌خودرو و سایپا در ۵ماهه ۱۴۰۵
آمارها از کاهش قابل‌توجه تولید در هر دو خودروساز بزرگ کشور حکایت دارد. تولید ایران‌خودرو با کاهش ۱۸٫۴ درصدی و تولید سایپا با افت ۴۳٫۹ درصدی مواجه شد.
@titretejarat</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/akhbarefori/690111" target="_blank">📅 15:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS6-DWJj_05Nd1BS-ExXbqhKnBRNAEqGxZEOSrYCpHI9H78PDQ_eOmBUJwOY8WZpmnX8W6x-dr_WZ9SdpXvsTGN2s6GbAI8B52rpYVJEC48eu4zUJc8K_Dvtk1RZMsiAtpcocKHhAj4ynfHuPqsq7l0Js1rU2ZgFkOKke-DPg5tLTaB7R_qpEiOPvb4tdp4yUnRIS1HVXUyx0lFwHDslkZGlQioULGHslmJefj0m-kxapM0C1sgKB3ZernyS935rztcSu3Gcl_Bki4ySRrIB9CVIDrKmtNdTzRv6wyNnUZ1ANqQ2LISyBicYRQsWVyiHI52NSYcxJ5icDNDcSYIxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار افت شدید درآمد قطر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/690110" target="_blank">📅 15:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690107">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vw5x07DsFdLZ35dn9Eaf7YdcfsRzt_8LCCfw7yY_BgbD0yrmkoO0jsigd788xZywWXVXdKOJj0zI0wmlJ492Ajx6tH-iHPyjpstF8fNIDspYkZ1YbrlEFQYuHYhnEBeH9z4Lcwiexqqk31RvojkKJH2Hq58TfWEbl7_p-pr7hZCO1eHH3b02fAxZS7z70IwDfqKqqAmpY1OBvzVv_xBYrUiCb0XRNKFGNQruOTXAPTbKzPHWETBDNub--DRoEbXuo4nJ3QWCv4mGIP38XIiCsHUpd8-yr8N1ITj3V9AGUc3YLyVrty4MqwxzIHQcBgrOBUnY9XInI3lHK--WImzEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqNd1l4OUSc-fOuJ-zipnPFwN9D03NikD0KP4xRHCSbbAc1Dc5xwAi_pv5QQMpQoz7fpVQYerjZxM9mJEoL6FO71SFD5wTNbSkGD1O66uRhNK0zASHp-6-KwN1LAHolaxPWRd6XiOYAng433F2t3GGK2SNQYnl2R44aZTAAdS60XV7AsXxQDU2g783I0uUdSAPRAU4F_t3_F02oUo-Os7vRAhKNdbjmHOMCnHRBBCMO3rBDO9CvUz86gpRZnMU9KfFSoDhsl_aXZGAl8VoDDiXeifoXEPlGtiWZCIZjacHWWUvtpPyMiSIHtYmH6MZpUYGXCA2LCjUHNoEInLs5OVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HErwarXiEUlqix-ZoNAaLzBfenhE_joq3NVyTnRywI3FGNL1ZJl51gYb4jcS-R-00x1_XRPaHbtUOU9VaxWItH3LgUpYlLIgZoAzEx2cMFJPCKTq4pk5NjfWje1RikTkJ6mvmJN4mFNiggoamfEf1NcmXeE5N829mLDhbb6UcInl4t2PpYUu2q8bKu0GqWyymTKJsNlg6lSAVqB1eEERGRks8m7tmpgFkKNgpmpFt7jiphi6ZnjedzsT4rB0tUlKXySjWnBKXs8VZ20LF8UHDRYBRealXjRynA0jPkeqhHz_rnHon7UobnYlH3I1z5utqtXi9iP6_UKbQRNUYXigJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هویت خلبان آمریکایی لو رفت
🔹
پنتاگون هویت خلبان اف‌-۱۵ سرنگون‌ شده بر فراز ایران را به دلایل امنیتی مخفی نگه داشت، اما نمایش چهره او در مصاحبه با شبکه سی‌بی‌اس، عملاً شناسایی این نظامی را ممکن کرد؛ اقدامی که کاربران و کارشناسان نظامی آن را یک تناقض و بی‌احتیاطی امنیتی دانسته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/akhbarefori/690107" target="_blank">📅 15:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690106">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
مرکز امنیت دریایی عمان: نفتکش «الگایا» پس از اصابت پرتابه‌ای ناشناس، برای انتقال به یکی از بنادر عمان یدک‌کش شد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/akhbarefori/690106" target="_blank">📅 15:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690105">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKICe744Z__mqe9giNTvUbdXuQwwgyZyhw5bGnOKtumyKr2jtjhAD93-DSaIi--o7GRjN8hTOFE99BP72kgjYdgI8gy9uG8oWvsFP2LXWVtZc3SznZ88LdsXRAXs9TsqBbfl_8AA81sj2htXvMAaqKtsCFDWGqQZ8ikARnzlaxt4LynEA75FHRhcsW5ZkUfCLjc--VN98eeTOrTSnhgkFc4ob_VBjUG45VuAiY8VawYt76kqWBNO9rnDTTjKcwjBKObvZdpEoAKHjvaNr-ufWDk4CUl27DPZTURgKWtKlLeBJRyMeJSS_mjaKxpJdDdQwlBHsBfSZueCb7J83ywiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
🔹
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/690105" target="_blank">📅 15:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690104">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1715812e49.mp4?token=ZYusmByQVbqg3RfL6em1MQ8Fl-ZH-nYxfcwsWdnFZhUHAehSaId27fGqzqlofzMgqxa7inU0bd38DOh8N7XdPzpzzkgkMSXjUjqeCSaYlgyDeUyNG0Uy9c6eY_3bbCUEyPNd8BMIFb-cudJQXn-fjViQ6i9qZu_KqbyNEjOFrncQyN8OzH-MbjtxuJDYQaKePbeBfuBshR8GzG6ykUf-_vb7NTaCZRjFf5c3Bf_dleIxg7hkRoItbxsDBeq_JiSxAUnHBn2a8YfNMelo6X7MiEzxpBBUSHwIU2etsH3RJT7hjbDW5APFRdc8288mqCgMj7mp0sU30LnR9zBkvWZoRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1715812e49.mp4?token=ZYusmByQVbqg3RfL6em1MQ8Fl-ZH-nYxfcwsWdnFZhUHAehSaId27fGqzqlofzMgqxa7inU0bd38DOh8N7XdPzpzzkgkMSXjUjqeCSaYlgyDeUyNG0Uy9c6eY_3bbCUEyPNd8BMIFb-cudJQXn-fjViQ6i9qZu_KqbyNEjOFrncQyN8OzH-MbjtxuJDYQaKePbeBfuBshR8GzG6ykUf-_vb7NTaCZRjFf5c3Bf_dleIxg7hkRoItbxsDBeq_JiSxAUnHBn2a8YfNMelo6X7MiEzxpBBUSHwIU2etsH3RJT7hjbDW5APFRdc8288mqCgMj7mp0sU30LnR9zBkvWZoRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سکسکه فقط یک صدای بامزه نیست؛ یک رفلکس عصبی عجیب‌وغریب است!
😄
#حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/690104" target="_blank">📅 15:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpqNroOLsElhpHhqTLBI9JfRGs10yVddlizMP_8r41Zv3aLUlXDrrrPn18NaFPXsZkUt1ZP_67oEpy8APdCM_qyUcxXz2E-Sb8lusrR6dkiHpo3ckNRUHnfbxBhVFhNjy7q5lBevEQs6gg8pvqw9k4zNUS8MugBGHataB3vUTzlm3HSnL2a_zN-0s0ib7aofqO2TttdoamG2S52sn-1XNGmVMvdb8eiADClLIiXpi0LFfi_qPZeXKJ_p5I729Fz3-_WXYDllSDlvBP5x0oYK5C78SseVpi9yKY9x00_5IyA343jreL-QjrirZEcgznVb5IrDPoWYiGXTAX3xnIw0Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان جذب نیرو در غرب تهران
🔹
فرصت همکاری برای حراست، انتظامات و مهماندار خانم در یکی از بزرگ‌ترین مجموعه‌های غرب تهران. اگر به رفتار حرفه‌ای، ارتباط مؤثر و محیط کاری معتبر علاقه‌مندید، رزومه‌تان را ارسال کنید.
واتساپ: 09309000316
#فرصت_شغلی
#مهماندار
#استخدام
https://jobvision.ir/jobs/1524386/استخدام-میهماندار---خانم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/690103" target="_blank">📅 14:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJp-3mJYTAxiI85MDOEWgMEQcrziZ-DEjBOvXb5x19ZOnLOBe946mLdBYeBmGbyXrCzkKFQ-cDpfepgZ0SZqr49eeKpmDelXX84gpwkNox219prbEXCmLSbG0D6-MH5gAPgL1PJ281n4MQRUHoz_SfXn-YRY97yC0SvUl6Pnfe0679Gsdo1CGSAIiHac3sW3PpJ1NlEjQHa-enXuxM99iHFF2FaX0p_S7TgHpEvqozIBpdEPX_KLec2EBcbP6wE83UI_CdnrCG6kqEKudA1KqzQlt311M6vTy9qu6PbpglAjepD3IobOf5-7HkrUPLZgdOQ0b_A4dmZA8tyIJRxPCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/akhbarefori/690102" target="_blank">📅 14:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690101">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
وال استریت ژورنال: بسته‌شدنِ خط لوله شرقی غربی در عربستان، یکی از خطرناک‌ترین موارد کمبود انرژی در تاریخ را رقم می‌زند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/690101" target="_blank">📅 14:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690100">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqUbhYVe3lFEWiDmSVV2Iubu3rkdq1olgOmzsMPzXe3fYzLCoGjmsRc8IuMeVMwq2zLxvJaQUj8EGLejbJxwNdFZlIxiFQ8U_9cF6FR_t5GOitSCfFQJCj9yGhjYGvvYv2L4HiY3UvZRmr0benCY3bXM3ngbGG1OKtSm0CKicBy4nlIMoW2Ueyu_zzH3BND2CLHXKxt5jCWr7ypzFrbkdjTQ9qmhvEyB7fzaj8f94q6F17Tc7f4uuUGGpt_0EGH_vZUW5ZhGEK0iX9HdqwO2ZPqFTZEjJ2oMVU1enBF-6Rf4OUfzecKF2S_Ah8M2tlxULP1VUxvpdNqcf33suXjf6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترکیب‌های طلایی سبزی‌ها با غذاها و ادویه‌ها؛ این راهنمای کامل رو ببینین
🌱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/690100" target="_blank">📅 14:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690099">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GP39ctjccDi5vvYxe7YDBH6VUvypSux8YJTYiQlOxBGJOB4jifHyJwvud1bgNTWQsWGYy0BKNr-eovh0UN1yqvvRj8qfRqObl1SrpspVeaBxM5BAq2r0XEXRcTLq6UeKCxQRF9P9RJCPIqgnQA7Ge6OFZyJS3PQ7LUkErQbBdr8XLmn9HSoUd6XcTTA21bhrWYnzOlsIMXPer4al9z1tznrkMil1kSX6hQvjs5v4zkAoS56lMHQbU2O-p5R2kZQTkQDz_arCQbNUifJcB7zGK2ni2LdBkjC9AgV8jZ7ALIw3_icM8DxBHPJIDUJiBrONGe4o1cYFAY_g7vSQSX4cvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت دفاع عربستان اعلام کرد در پی حملات هوایی اشتباه نیروهای ائتلاف یمنی(وابسته به عربستان) به مواضع ارتش این کشور چندین جنگجوی وابسته به ارتش سعودی کشته شدند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/690099" target="_blank">📅 14:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690098">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
مرز تجاری چذابه همچنان بسته است
🔹
رئیس انجمن صنفی شرکت‌های حمل‌ونقل بین‌المللی از باز بودن مرزهای مهران، باشماق و خسروی و توقف کامیون‌ها در مرزهای میلک و دوغارون خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/690098" target="_blank">📅 14:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690097">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fd5f89d1.mp4?token=IxI9ScpifkzGPv8dt0SWcFbcW_ORcAwTqjRTQFwbMbSB77f9oI8GeP_C_0APaAtvPXbWnp9LswF_6MTkwnfiOJf7LgscYho31To1B6UfYkZ0Hf5PhoTan9DekBfb6Kda_VYmwhC9stEj-jDOYhZeTgAKbCZc8rHTdi0EJdsM58c1l0Wg_gZ1RIF8nXSj9-lLEJVaz0EranErT6i4s0ejeqGmcbKpXx9YbOk-sB_B1PR62bLxHSdp5Ynq0l8_v_vHPkM9CFzmdx8tONqXiT_CurRY7esnkVRVSjNBY2kOLBPd5il7DNg6fzeBsWdEExJ1pGlBYwSxeMjDbSTYiiL_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fd5f89d1.mp4?token=IxI9ScpifkzGPv8dt0SWcFbcW_ORcAwTqjRTQFwbMbSB77f9oI8GeP_C_0APaAtvPXbWnp9LswF_6MTkwnfiOJf7LgscYho31To1B6UfYkZ0Hf5PhoTan9DekBfb6Kda_VYmwhC9stEj-jDOYhZeTgAKbCZc8rHTdi0EJdsM58c1l0Wg_gZ1RIF8nXSj9-lLEJVaz0EranErT6i4s0ejeqGmcbKpXx9YbOk-sB_B1PR62bLxHSdp5Ynq0l8_v_vHPkM9CFzmdx8tONqXiT_CurRY7esnkVRVSjNBY2kOLBPd5il7DNg6fzeBsWdEExJ1pGlBYwSxeMjDbSTYiiL_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهندسی شگفت‌انگیز در دل یک کاسه باستانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/690097" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مشکل مدارس دولتی چیست؟</h4>
<ul>
<li>✓ کمبود امکانات و تجهیزات آموزشی</li>
<li>✓ تراکم بالای دانش‌آموزان</li>
<li>✓ کیفیت پایین آموزش و روش‌های تدریس</li>
<li>✓ فرسودگی فضای مدرسه</li>
<li>✓ بی‌توجهی به نیازهای روحی دانش‌آموزان</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/690094" target="_blank">📅 14:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690090">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6yaVqMuQ6IZ8_VkZkkCK8-u3PynbR_M3SALvVyzvI0MZ9-uHekb24ZJ3eGcZr3rmYAFUTJgK-nHkunwZcjZSISWvi8mg0sCssBJVXbu0upNJGd4OJ1iZY2sfhBSgCiv-egnIkhmUrc1Fl2VKi_Ri5FR9d9YZvtqR0zVykhg3cpMr6ixfJwqNXzikGEilH1t5L389VrUb_q6UMUzdNCGy1AD7oYUWR8gTjmTMiBt7qW8LxMTvfBYak1kMoGH-95shJSiT1eQG9bKnuoDYNFcMhHM1INrITj5YhCzRTUotDnQJkuVM61ZTcfltHBZCp5nVAtczZvFcM-2n6WxwIXleQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WzIkSyMtTgxBxKxS83H8LtxGIibP-o8WDkmkxaPwWJaIX35d7lnn_wZBbilsiZC-maxz8ESmpgLG8a20UKBP5pUi-G82C2cYY9YZ2b0ClGB2OHC6MVEscuqKGWCT5ryxxiJuG40gXsfAFZx1xZxjoozzholNsCJdlBUeRwivuvKwMLN5wFSpVhWDEpFL8azxNhRf4-fG75pMEBGS0vooRVlctujWqA9fl2quUmWGREZnx7qnPawdGT15wKkZxn8GOXprMulFPXuvI6fHOfxj8vaakIu81RK3z9wj6AqCVD1MoOd6LYH3Plk8ArQG7CVZvd_sGS618LD4nBu5KW6sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_AFfhCvZu-gzzzaO9jrd3eUSjlOd0LScl_RR2c1Nc4yMZDfspP6B6tUosuUnUNc4boOonqotww-fnqY1pI8jBSeWIuFLTpxMzo3-Ni69Q-z_Lm9a9hK6FSDH9qDMoPC-_3sZxDzoa7iblrPsurn8SUcZYfKAFkrnvcNL5FaqzVKapC39JnDfze3tAEBQFpC3vBUEBTlSZbHGTzgZJVIxf4UQYbX8JQ3DO26ZE_ofbcqIz0-tUsD7vBwJXmpCDVwtvCrNB9rVRXgjz2S5pQPyiCdjwjpyL3Fd8MPgNS6J3AHYn9kXYpL_17Zo0k_-ZEoDRw-Z69V5kSD2aombmLqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IRDwknoY4Z3LsPpGAqRRT1TLkv0QIGjT2j2HCjyN6vPpzoRSMLWG2_XP7y3XcrRbOPFq43rDNSl221Ib2A63yTSEPCShHPZXwu74UXZjh0nS-ENqbanzHaQV_YyVwk7nnpohC4TztvBfxb0Oo7POaOojHpu_3rZIBSSjiVhtbfgb7Bf8BSXS4Z38hRDIrZ63KErELBxmm32MKE6wO_yGwaMLZ9pjiFUNdZQiJVK0wJ005J1knxUOSMRNaQcK6VfYHS7oLmeo9COXoHewg2S_bFXOLXAiPp6QwRefjQPVBcvvDhFbEEkMXRDFlCGNhkbnUxKew-SiwJTsaZ1vXp1oyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با این ترفند ساده، دکمه‌های معمولی رو خاص کنین!
🍒
#فوری_استایل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/690090" target="_blank">📅 14:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690089">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بهادری جهرمی، کارشناس مسائل حقوق بین‌الملل: مطابق حقوق بین‌الملل وقتی راس یک کشور مورد هجمه قرار می‌گیرد ما نیز حق داریم اقدام متقابل کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/690089" target="_blank">📅 14:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690088">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDrXvsIi304p1IgSxexN-9UXTaUP3ljC4ELVctBIbIzBKMNOV4_A9fSrL51XWeSAAXjyJXwQuDuSc4H8nvtoyvCthbsp5YALyaW6jHKqP760WHZXZP_Df5PwZiOutlh1qU5GksOHaoD_4JjVu-PqqQBozAt1SfRvqC0fmZoqdstbu-H2OlfqJOR2RhbJUCaskTx188-ImQ_KQGRC0b_j6GaXPw3CxnrfJjXi26oortlHOlYKHJefeMVVFrL8B861tiWl3CxJLab9HeW5abXIkM9hKlOTNy8IQyik0ThUbWzZrkkSWZ_N2Co_9sJ9oegctL3GMf2g6n5DkgtZUTkhjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خلبان آمریکایی: کل امیدم برای بقا این جمله بود: «هرگز اجازه ندهید کمبود انگیزه باعث شود که شما را در تلویزیون ایران ببینند»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/690088" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690086">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
عامل پرتاب کوکتل مولوتوف در میدان پونک دستگیر شد
مرکز اطلاع‌رسانی پلیس تهران:
🔹
فردی که سه کوکتل مولوتوف به سمت شهروندان پرتاب کرده بود، هنگام تلاش برای خروج غیرقانونی از کشور شناسایی و دستگیر شد.
🔹
این فرد در جریان دستگیری با مأموران مقاومت کرد و از ناحیه پا مورد اصابت گلوله قرار گرفت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/690086" target="_blank">📅 13:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690084">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
برخورد سوپر نفتکش «الگایا» با مین‌های دریایی  فرماندهی نیروی دریایی سپاه:
🔹
سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقهء ممنوعه در جنوب تنگه هرمز را داشت،بر اثر برخورد با مین های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/690084" target="_blank">📅 13:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690083">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhIQy5gkMDwqoxs87sj2IMexsvHhWDyzhi5LKEDRMnxqu9RTNKDapNv5BhLdeiUA4bFniMr5nAwYju88D3XOOiSYt1gcj3sljjBBUnf1TAVEmpb5_DuOx1ODgs1U33ucH44J7mmyY6c7RE_aWXbtEr9Ffk0ozTSIyxbDhbRC1k4v64BC3YZ5nJKxOwY12KQz6HpVZDsk9MILJojaV9ey8gVakF7mA3h3QwcAr1_md7E6hsQ0vowA3up85DHJ1Ht5uoiYmgoBpiQFCG0Mn5PYnoZGccP_GaNgAlPXb3HWBxEebkowbC9dXm3niIyTqKsbu_-jfA2oHQb4uunZpIso0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کرایه روزانه یک ابرنفتکش در مسیر خلیج فارس به چین برای نخستین بار در تاریخ به یک میلیون دلار رسیده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/690083" target="_blank">📅 13:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690082">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
استاندار خوزستان: تردد مسافر در شلمچه و چذابه در حال انجام است/ تردد کامیونی از امروز صبح در شلمچه آغاز شده است
🔹
مساله حمل بار و تردد کامیونی از مرز چذابه در حال پیگیری است  #اخبار_خوزستان در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/690082" target="_blank">📅 13:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690079">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IO1m_k5Np6hwRFy6Y-SdBKUF_6ArDGDO8Kyiy6EMK7egXh63nZhwDyXZMd4v1tZq_K3tqjPfiBNp_trjnfDTnYXhgHo4tthVcSdQZJhpe6QX7MXTPP-3ADKd64oAYLk7tPphLJnvaZjyR6xJZXPJGKf69rzw13kaTlthvGvEKFjed-pZb6AvSnox2DfHB-F5F5Wultl128NPVUulRpQk3pOpUDpfFAzX5TdIoLUvvGQuvHu3vbWN8JNJaJPfhCSKyjonzwhapx_ntcwJlxjY9Yx0YSrDiWK4df3wc9Tr4QN-8YuJdEK-PrLMy8i4memVE0H_2SGeYHZKoaeMZQ_PkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSAA653kILdtc2sAozma2QCTtPzo9go1EeHbrVt8ZavFEasvTWdpl4jO2n56RIuTgacPSFG0x_H23sOda-QBnXx86z3ZzlBks1r0dP2Frcuy55SFcghRB6c0AGVSaovV9UJBbPdHP0Sj1hr91M-mb5lEZcu_Uw4s5MqogGI-dfnk4ZLbUbgrNxTAax2nQ4Q8tsASWuF4JXOrO-vUhNUwIcw564xkGozzVZiyfgs2kJBijwwek7IKGVJA8cqdkZg0Udx_Ihgyaj-D_R335vYZ9-5zY_djZvJm5FICba73sBcdYkpAyDaFlWxvaRrmkl2_PFRo1ecHOeUUe2B8SiHKew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
بنز میباخ مجوز ورود به کشور گرفت!
🔹
فهرست جدید برندهای مجاز خودروهای سواری دارای خدمات پس از فروش برای واردات خودرو توسط ایرانیان خارج از کشور به گمرکات اجرایی کشور ابلاغ شد و نام یک برند لوکس دیگر (بنز میباخ )نیز به این فهرست اضافه شده است./ تسنیم
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/690079" target="_blank">📅 13:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690078">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fS7IN2uheyMY53VexHFW12rqQvS7pZ-Z2o-u5-dciqgoH2EJOT6Hd1ZRdpO57VufiopsuECCuf_BFnOkbANH8gefg20HNQZMw3VaOhDkTmbgHQxeLdQSFAi1rR9hNB_-TFTjXQn94f7MQVwsBWO9VGIxob9nJmOMP2p3_HqCN4SRW-IrYm_OTc0UZnT-GnYnm5Ie3vne_B2HvTZ_hGWNhEPydbC8Ogv0Iv9ZUT7DXxWerkkq9SjlgD86-my_4K7_i1e9G1irOzuUgjBVYqdDO09QziF3nvsfa0JGuZ6RAAdLreNKPCEw1c-4pEQ2S4Fydm0ZoVsC60kt8tpFeKjiIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای گروه تروریستی پژاک: ایران یکی از فرماندهان ارشد گروه پژاک را دستگیر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/690078" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690077">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
الجزیره: صدای آژیر خطر در شهر مکه فعال شد/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690077" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690076">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd45dc7b2.mp4?token=KXaccK2gCQ1eEIXxGwY6uTGYhxSXWWgmEPQ0FJMxF4O7DMQoBRMOk7O3Ct173dRDC4dX7ZbeFqhFN62XhriPd8GOho0kU9LVCyCog4YFrhOrSmLvuBlKOkNyOmurqb2fht-F3I86_D9mG1DQusU94otfpGUQyAL9qt6gJqKgG15mE5lOBWxcklnXsVxN1noWE4krzg8s5e9oRP3dKVZ7j2WiQvFKsrhUJRdr03avN-XfI827ybGS3PjFS2EZIRO9AUgaIutZR67z39XNsSqgfdHpCiRkpLaSO1t6rUI3NGG3_u4X0vkooLm_P0Qz-mKmPZV5LWk4Ey-irjoMKfog3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd45dc7b2.mp4?token=KXaccK2gCQ1eEIXxGwY6uTGYhxSXWWgmEPQ0FJMxF4O7DMQoBRMOk7O3Ct173dRDC4dX7ZbeFqhFN62XhriPd8GOho0kU9LVCyCog4YFrhOrSmLvuBlKOkNyOmurqb2fht-F3I86_D9mG1DQusU94otfpGUQyAL9qt6gJqKgG15mE5lOBWxcklnXsVxN1noWE4krzg8s5e9oRP3dKVZ7j2WiQvFKsrhUJRdr03avN-XfI827ybGS3PjFS2EZIRO9AUgaIutZR67z39XNsSqgfdHpCiRkpLaSO1t6rUI3NGG3_u4X0vkooLm_P0Qz-mKmPZV5LWk4Ey-irjoMKfog3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوشی افسانه‌ای Nokia N95 در زمان خود یکی از تکنولوژی‌های پیشرفته محسوب میشد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/690076" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690075">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFQf6oFRn7ZfUzKoqMpLzdXlLwRj_IIOVzCgTimcAi51GFdjEmKz5WEWs_U0moQ0VIhI1KmM_a_RAwj3xz2wsKPxwsgnNFH8zkNFsHfx6Id6lPaJzJ1CjbbjHQRpgQVgt4lPk4SIIQ-CyeRTz6CmHUexrJt8sIi3CdLH6_w5nd6O_JqU3NlLHhi3RT1f3NUVRAGThn0KQyufcbjfE91F9buKAndjg-4qYK7VK0ZS0LkvbK_ny2yrInBpyn-uZIeFJB55q7txfDzA7HL8s3EcdbzPT0LJ76X2iLga6BBcePeT1ZMevKJ07hvqgH0Qw9PxpMNNeGO83RbV6hzdw-go6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
*۹۰ میلیون* نفر جمعیت و فقط *۱۰ میلیون* خط ۹۱۲
💎
📉
بخاطر *محدودیت* عرضه سیمکارت ۹۱۲ و اینکه دیگه قرار نیست هیچوقت تولید بشه و روزانه تقاضای خرید ۹۱۲ رو به *افزایشه*، در نتیجه قیمت اون *همیشه رو به بالاس*
از *پارسال* تا همین *الان* تمامی خطوط ۹۱۲ *حداقل
4️⃣
برابر رشد قیمتی* داشتند و انتظار میره همین اتفاق طی یکسال آینده *تکرار بشه*...
با خرید *قسطی* سیمکارت *۹۱۲* :
✅
سرمایه گذاری *مطمئن* کن
✅
*اعتبارتو* ببر بالا
✅
برای همیشه توی ذهن ها *موندگار* شو
مجموعه رندینو با *شرایط ویژه اقساط* درخدمت شماست
❤️
از بازار ۹۱۲ جا *نمونی* ...
😉
https://t.me/rondino0912</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690075" target="_blank">📅 13:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690074">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
هواپیمای دولتی ایران وارد حریم هوایی عربستان سعودی شد
🔹
گزارش‌ها حاکی از آن است که یک هواپیمای دولتی ایران با شماره EP-IGF وارد حریم هوایی عربستان و وارد ریاض شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/690074" target="_blank">📅 13:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690073">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwSDGbNpHDyP7YNGG7TSp8ifqxvFy0e9cBdGfn71KJTAFn2GrvoMVPcm56j0307hX5ZheNW_SMs8dCWE9C561C2TJVIJQJOOG4ULxyuodzy1sP3ff5pehi17fVwzGWp6N7yZbFedErBrR1vTX5FOA890I0_tLw4ho5-g7zjLoJMK8mhvr5UCcHCrh4_rlkUA41NPw4gxEbHAEK-Bx3-OkMLKLuqQPz00APFGakDWN2qo_UZeNtjaeLb3hK8qMqNuHHUUQCFIZEz68KvR5JDZ3L135FzlQePTCi1Qu2maGAdZA36m8kHbf26LpzcUoH6yuIzs9lMv00Kh90RRsu3n5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بالاتر از مدال | بازیکن استقلال چه کرد که رسول خادم برای او پیام داد؟ | ماجرا چیست؟
🔹
اقدام خیرخواهانه سعید سحرخیزان، بازیکن جوان استقلال، بازتابی فراتر از فضای فوتبال پیدا کرد و این بار رسول خادم، قهرمان سابق کشتی جهان و المپیک، از این حرکت تقدیر کرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245364</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/690073" target="_blank">📅 13:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690072">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXEIFPgbDCP9vb-jJ7X_WMWoosK_0sXkWE0EKZCophiej1A7Cq8wBfzltAnI7h5gv0OAv2SCsEsLVem7EsUxPkvphXfqdI0FUkX96gr0YmsIIgcy-fzHVkHTtAdwkG43JL5LnXovWwsqTupo8qj5l5MkQKUf0NHi6CtFiC7r4ppXv3rPJ_0_zTLHBIAgFHJd2Z6ppz00nBlGJgjamklweUbDurdYGsChitKeIRQF6FY3LckH8V7XKXedX0Or_fsJ0JfF6bbOAsLfheRGEYdvLa4jiqdM3-xZo_Pi5zJwvt2_CGNXoJFcjL1xNbxj2snglkv5J3jgiNf7pUeynvv7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا از دریافت گزارشی درباره اصابت یک پرتابه ناشناس به یک کشتی در تنگه هرمز خبر داد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690072" target="_blank">📅 13:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690071">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTExEjz0ANwnuP7wnWT1Mx-BTewK81YvMoqgwYDXxxNHeYn-XtVqqGx1qCXWBiSCoyfc4X5NCAvEXvYVwUCajTUwiJVeb5hH7zzN6s80yg2ykQYfAwyOUOPIiA6BYsElVimfBK-RxnEkmWEqS6TcU7xtMjn0gpr-G59SKHEDQKUBtObPk0k1GsjfUd6uFEJPDul1-0pzaycTelCCjqeQqqZyWgb3vb4wXzetx_81NmYTQ_yd50Tv4jIU2dQUvnX_IyK8ZmRD-NhdSmjMde5QSK0xkbLa5esSav7q9IQwIuSxMqxjeNuBgsnSbbEO6IxExDd2che227DfsGXm20s-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و ارز امروز ۲۴ شهریور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/690071" target="_blank">📅 12:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690070">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
جنایت جدید عربستان در یمن
🔹
منابع عربی گزارش دادند ساعتی پیش جنگنده های سعودی یک مدرسه در استان تعز یمن را هدف حمله قرار دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/690070" target="_blank">📅 12:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690069">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eiwb72Tw04GBG9nK1AtVfhp2JVwgvtjR_PgKdBrtBGP3Rp203F68d0DAzH2BHd0FtLh9Gng7lpedqF2SDIeqT3EFp_Fsu4TkdmZKoFvS0X4sQ9vfMuQDI7XJTrUQ-STW_y5CSJEBa6Etv2MHrVsKJWgAN9__nq6Vdo-EPXrdG-v5kZx5fddFaEC6vXSNT5sGLkMo1L4J2NTPpeetg7FI-Q2orZLfINtTqw19y28UQyG865DBy7odcvLbE0wXGdD8PVBDC8-J8rSLPGMfavthm3K4DqQJ3ZYtv1bM-D_ePqOITk0OwxneZNESMomCrJxP1QpsG78i3lNWv3Y6AThH6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های عربی: ستون‌های دود در استان زرقای اردن دیده می‌شود
🔹
هنوز منشأ این آتش سوزی مشخص نیست./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/690069" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690068">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‼️
منابع عربی خبر از صدای انفجار در شهر طائف عربستان می‌دهند/ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/690068" target="_blank">📅 12:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690067">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
منابع عربی خبر از صدای انفجار در شهر طائف عربستان می‌دهند
/
خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/690067" target="_blank">📅 12:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
سازمان عملیات تجارت دریایی بریتانیا از دریافت گزارشی درباره اصابت یک پرتابه ناشناس به یک کشتی در تنگه هرمز خبر داد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/690066" target="_blank">📅 12:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGlKpaLjYV1-7j8ZpAOXycunw24rFCid6Hr-uZgOcBk9mHb2ulOb-lXsCxDZDUnJxZ6ae2YhAzdqhBw1zoZMQgSw8xuUOisgzGXtIjCJiAoocIqZNzDHAeX86TQmqt5yKyTzCsEEdUM30a4mqkBnuogZs3_CcL3EMtFA65NRMIaaaF2uB9Ly47cuQ1mUSZupVphE8N8oK4ffdZvClzobvjGNDghxt-nlwPbr3jU2TbO2bB_vLWy-sR7DgxPJJ1VmIwJYQIQLASt0bGHaU9ZBsqtCpTCSqiv3HwjDgaIy0whiZt-J1Nln0T61fKqJREGWuxzV-L7YtuuLm5fjKetH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از شوگر ددی تا موساد؛ حرف‌های جنجالی امیر نوری | پولدارم، می‌خورم و می‌خوابم!
🔹
امیر نوری در گفت‌وگویی تازه با مجید واشقانی، از وضعیت مالی و دلیل ازدواج نکردنش گفت و درباره روابط عاطفی، حواشی «موساد» و فیلترینگ و حضور احتمالی‌اش در جنگ زمینی اظهاراتی خبرساز داشت.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245356</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690065" target="_blank">📅 12:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24e444f512.mp4?token=b6qT9cAEnYw9bCZlGNmtTT3OiGfJXNkImVup995pBWjjtqrd5TrYgdkH1dkJChDBv1i5r2qASZRJDHchzRuEAMX0fX9lp2M10X_DMFAjkcpqCsMKe1eZROTT82UFdXzqVkCZiDcyBwSTrkHxlQOn6BA62WXh0Lqko6zrtX3QqzY-FADk1EqUHcLxiEDoLWOgUQ3TZ4vN_w_G145ANKbNNfJtIOYldFGLipDtk47GMjkZXRdP1CdnhobCs3Cf6raRKhz62meFtaJvP7xjQ_ZLBPvLg2Zm4KkuHb9GnaRlzS3VCZPCSQh-7S9totTCSPUrSSKMfS9rM_s3U4fVxnXnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24e444f512.mp4?token=b6qT9cAEnYw9bCZlGNmtTT3OiGfJXNkImVup995pBWjjtqrd5TrYgdkH1dkJChDBv1i5r2qASZRJDHchzRuEAMX0fX9lp2M10X_DMFAjkcpqCsMKe1eZROTT82UFdXzqVkCZiDcyBwSTrkHxlQOn6BA62WXh0Lqko6zrtX3QqzY-FADk1EqUHcLxiEDoLWOgUQ3TZ4vN_w_G145ANKbNNfJtIOYldFGLipDtk47GMjkZXRdP1CdnhobCs3Cf6raRKhz62meFtaJvP7xjQ_ZLBPvLg2Zm4KkuHb9GnaRlzS3VCZPCSQh-7S9totTCSPUrSSKMfS9rM_s3U4fVxnXnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه سقوط جرثقیل غول‌پیکر در شیلی
🔹
وزش شدید باد و بارش سنگین در شیلی، یک جرثقیل ساختمانی را واژگون کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/690064" target="_blank">📅 12:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690063">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
گزارش خبرفوری از مراسم بدرقه تیم ملی مهارت ایران / کاروان ایران عازم مسابقه جهانی مهارت در شانگهای شد
🔹
چهل و هشتمین دوره مسابقات جهانی مهارت (WorldSkills) از ۳۱ شهریور به میزبانی شانگهای چین کلید می‌خورد؛ آوردگاهی بین‌المللی که حکم المپیک تکنولوژی، تخصص و مهارت‌های فنی را در دنیا دارد.
🔹
امروز ملی‌پوشان تیم مهارت ایران، با انگیزه صید مدال طلا و اثبات شایستگی‌های فنی کشور، بدرقه شدند.
🔹
فاطمه منصوری، سرپرست سازمان آموزش فنی‌وحرفه‌ای کشور، در حاشیه این مراسم در گفتگو با خبرفوری گفت: عدم حضور در تمامی ۶۴ رشته، ریشه در متغیرهای مالی، محدودیت‌های لجستیکی، زیرساخت تجهیزاتی و همچنین چالش‌های تحریمی در برخی حوزه‌های فنی دارد؛ با این وجود، ترکیب اعزامی امسال نسبت به ادوار پیشین به‌مراتب حضور گسترده‌تری محسوب می‌شود.
🔹
بر اساس آزمون‌های سنجش مهارت، میانگین امتیازات ۲۲ ملی‌پوش اعزامی نسبت به دوره قبل جهش معناداری داشته و پیش‌بینی قطعی ما، ارتقای رتبه و رنکینگ جهانی ایران در این تورنمنت معتبر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/690063" target="_blank">📅 12:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690062">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هواپیمای دولتی ایران وارد حریم هوایی عربستان سعودی شد
🔹
گزارش‌ها حاکی از آن است که یک هواپیمای دولتی ایران با شماره EP-IGF وارد حریم هوایی عربستان و وارد ریاض شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/690062" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690061">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJY43X5VtL1UEL7gfN7-oA8CTCXxByLKmYFDssRlAFDo3673_YCTd7kk-hplIc9RYHjssHFJul-3b92WHm4mnfBYeSvHtphKXOyk5FkvD4ojrGD6GXJBmAiLo6bebsQX7boXWHRkxf9F6whhdZWeE-DoZs8ZXTu_0A6iZZt0cURkJQqEGnzdm5E9lE_X0gtsYiS6f6TYfUibBYlOCRHp0xlmKmiS4PwSPI5LmlwdTfzrbcJV5iHr9BKo0841Z7YajdaWhX-IVMX8hSQCz7KK8p-FwixGA1V8w27pnz3d7Z_ameJSqTpxj_7MYtrFJvLeTAPAjLwahAwumb3ZXE7B5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کسری بودجه آمریکا در ۱۱ ماه نخست سال مالی ۲۰۲۶ به ۱.۹۷ تریلیون دلار رسیده است؛ چهارمین کسری بزرگ تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690061" target="_blank">📅 12:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690060">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c85078f1b.mp4?token=W1mySjHNVlbruEmXW6I7K6ardjQ3TkjUvXERkGyp3nmDnZlOhlPDhUTN7nH7kmfVfY4SmE-PlSpgYzhV17o2CKIa5fS_P5umViVYaXMiT9add5WcuiDeyjo10wC_PgJnXFWKo_NgaT0w3KzxkkFXRSz7ER5aiQYy67nv_KpV3PKhGe0cdjgmyauPbBcF_ljOF6QSYDKf1VbQ8PQEClF84xLa9EJ9-7RL3GQ2GtOmf5NdNgUDZ0xaq2-9oZ_M4VlsvlY46oBLcZBp8o_526dQNRJyIC4oqhq1r7WdniGszey3GecLaO-2fIfXYp1x_Rh9fK-7F4mAQgb8OeuUL0qHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c85078f1b.mp4?token=W1mySjHNVlbruEmXW6I7K6ardjQ3TkjUvXERkGyp3nmDnZlOhlPDhUTN7nH7kmfVfY4SmE-PlSpgYzhV17o2CKIa5fS_P5umViVYaXMiT9add5WcuiDeyjo10wC_PgJnXFWKo_NgaT0w3KzxkkFXRSz7ER5aiQYy67nv_KpV3PKhGe0cdjgmyauPbBcF_ljOF6QSYDKf1VbQ8PQEClF84xLa9EJ9-7RL3GQ2GtOmf5NdNgUDZ0xaq2-9oZ_M4VlsvlY46oBLcZBp8o_526dQNRJyIC4oqhq1r7WdniGszey3GecLaO-2fIfXYp1x_Rh9fK-7F4mAQgb8OeuUL0qHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خنثی سازی مین با دست خالی و بدون تجهیزات و دمپاییِ همیشگی، توسط یمنی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/690060" target="_blank">📅 11:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690059">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رویترز: شورای امنیت سازمان ملل امروز سه‌شنبه نشستی درباره وضعیت تنگه باب‌المندب در دریای سرخ برگزار خواهد کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690059" target="_blank">📅 11:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690058">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پکن: عراقچی فردا به چین سفر می‌کند
🔹
سخنگوی وزارت امور خارجه چین امروز اعلام کرد که سید عباس عراقچی، وزیر امور خارجه ایران، ۱۶ سپتامبر (فردا ۲۵ شهریور) به چین سفر خواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/690058" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690057">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6aeoAbmcBQQRukuhdFtXslkd0GxDMskvkAGyXbzLV3--WzGAt6fqgHrvXPhkTvLqCnonBjHGJT4QzUftCNNbs-GSjuF57tL2KE7cu3KEQhYQaLq1Wda3YJwh9g-MhdzJLtHaA77dpuwtpvAxidskEvRCvfCIRA3UGiUPQaiYgdCAtk51wfG4aV0lBFcH6gjbJN8DX3sIIjdcvipVUfDA1F0O1EsEU75y6dgkqdGzxTYQUg2vzCfMKgzi9MYZbobUkCqaEjuTpkath4ynPuEMfDqiO2fM-snLJNJdsrOXpMtx9YCZSAVuDifv6ek1bI6QpG07cXE86Ay6VMEO6vOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحرک هواپیماهای سوخت‌رسان آمریکا بر فراز کشورهای خلیج فارس
🔹
حدود ۵ فروند هواپیمای سوخت‌رسان آمریکایی بر فراز کشورهای حاشیه خلیج فارس در حال فعالیت هستند./ صداوسیما
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/690057" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690056">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49481d0554.mp4?token=ia9YhkkzLzV9LyxRXXcNY69T7J4A-ExC_twfWWYdl9upmkSSycMpRD68ARlUUcJtvMTvxEzCdzUA-Zz3s_8CqhPG_jZbBenuLlGPkbON4y0ZsvtC0FyaqZz2LtDPHo5HSQBYLWjw01g-nvQGP9lOXR8otYVJvUquqRXBMgnJa8ud4BGMAM0qtpnqtijQgkaauYfjuslU-FUG4J3KmFdsAMIfFt7TCLUu2-rWpFaag4f0VdDQ1fmEa2P4HP5b8kHd4gOj2qqyfgJJlsCAZaDRWSk-t_o1dqPGkTWOg3FOaVzQZbEbQrJfxYehM9kx2eoTSiMCAvjvp9hRgjDHUPvuqYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49481d0554.mp4?token=ia9YhkkzLzV9LyxRXXcNY69T7J4A-ExC_twfWWYdl9upmkSSycMpRD68ARlUUcJtvMTvxEzCdzUA-Zz3s_8CqhPG_jZbBenuLlGPkbON4y0ZsvtC0FyaqZz2LtDPHo5HSQBYLWjw01g-nvQGP9lOXR8otYVJvUquqRXBMgnJa8ud4BGMAM0qtpnqtijQgkaauYfjuslU-FUG4J3KmFdsAMIfFt7TCLUu2-rWpFaag4f0VdDQ1fmEa2P4HP5b8kHd4gOj2qqyfgJJlsCAZaDRWSk-t_o1dqPGkTWOg3FOaVzQZbEbQrJfxYehM9kx2eoTSiMCAvjvp9hRgjDHUPvuqYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک درباره هوش مصنوعی: اگر هوش مصنوعی بتواند کنترل سیستم‌های نظامی را به دست بگیرد و، مثلاً، یک سلاح هسته‌ای را پرتاب کند؛ این اتفاق، بد خواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/690056" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690055">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdiweEec5jvXrWEOC_AjIc-fanHBtVXafOh2xCPklipLoGn5tRLi1wyKWKUd-pH7Zy4kuL4BPsIKdgVH-fHIlQS6pzGSN7wGVvR9VZPBVBzPi7-J1Xn672I9Bl0tXHVRIgjagqP5jDcJrJC57mNZ78kc8Q-mAOiLuUu0grU_oo_z1bPLM473FfduuwW9KvPMd6HyVeVYfQ_rxSebIyXA4hOLra7H58E__dbFiKUjXOqLFs0s8Bgk92xWoWoqlxmuLZfKCb0wI5qG3UqnmVDocMXUkyccPdcwYKcVP1RIHtlgW2dFlxVYP2Jv8U4fan70d4pAA1tTYRTRzXCrJVbslg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید هیراد پس از سال‌ها مبارزه با بیماری، صبح امروز درگذشت
🔹
مراسم بدرقه او، جمعه ساعت ۱۱ در قطعه هنرمندان برگزار می‌شود. @AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/690055" target="_blank">📅 11:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690054">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxCo25KUdwNIaNENK80qpwoEcvw5dGNFvhxwQJlJ8-BdUNj-bPyOjUvRk192d6VHC0ub-bS4rBPjF90hssj9g_JCGjTpTaXEGDoRkDoBAACmZYKWl5p44qFdmSZMaRKxDoNI2opSo-20Mpuo5PmSWbUJDWkyY-MtpPfmgT6BxxrZEqfwB3ULpTvjb141ocC4A8b1riYZDzgE2lcLAN5TmbLPcdlS2YpbyoqbqjTOy_7c3Jy6tGp4CZ3cqzwY3odLL9RZO0SuITsxk5oQBekCosqmmeaOE1dgfDtr2Ps-agAHG8UVi4SuXjRVV0ReECtoJxtdjSBcfnX94Tl-YAvKWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک هدیه «رضا جان»
ترکیبی دلنشین از سه یادگار ارزشمند و معنوی که کنار هم، هدیه‌ای شایسته و خوش‌سلیقه می‌سازند. این بسته، انتخابی مناسب برای هدیه دادن در مناسبت‌های خاص و ثبت لحظه‌ای ماندگار از ارادت است.
✨
مشخصات محصول:
▫️
بسته هدیه شمس: ۵۰۰,۰۰۰ تومان
▫️
فرش سقاخانه: ۴۹۶,۰۰۰ تومان
▫️
عطر و نگین: ۶۰۰,۰۰۰ تومان
💰
قیمت اصلی: ۱,۵۹۶,۰۰۰ تومان
🔥
قیمت با تخفیف ویژه: ۱,۲۹۶,۰۰۰ تومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
ثبت سفارش:
@gharar_order
👁
مشاهده محصولات بیشتر:
@ghararshop
ghararshop.com
قرار؛ تجلی هنر و ارادت</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/690054" target="_blank">📅 11:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690053">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e877e5cddc.mp4?token=pntuhnhbE0HBhfmxkBwJHui220TDrjslOTS8Fu90vD4VQgPiXZS-t42DixUfFr_c857YhcZAa-pUlmdXFBWy1CmEqRxe1L8OzF5LHc7t4G0RzQdcUVUQRbWpmyiTA9umm7jje5gXXVT4O_h9cYvpO4SDoPM4IUoPFMNETIrqZZfAs1bJcvC5yIR1qHzpIgT8WQUGDNAvKLF5TxJsj2tIhxYJcdWgUhHisqEKk-iIaC5_I8c8HrfMxSBWFDkmP5R2dVhFLQZtCqIfYWYqIccykDJvSbg12OntPv_GTZmKvs5dBaA0zGYrp-1gIJ8Q5Umo6ZjgwYCDUE5sLBwnRchTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e877e5cddc.mp4?token=pntuhnhbE0HBhfmxkBwJHui220TDrjslOTS8Fu90vD4VQgPiXZS-t42DixUfFr_c857YhcZAa-pUlmdXFBWy1CmEqRxe1L8OzF5LHc7t4G0RzQdcUVUQRbWpmyiTA9umm7jje5gXXVT4O_h9cYvpO4SDoPM4IUoPFMNETIrqZZfAs1bJcvC5yIR1qHzpIgT8WQUGDNAvKLF5TxJsj2tIhxYJcdWgUhHisqEKk-iIaC5_I8c8HrfMxSBWFDkmP5R2dVhFLQZtCqIfYWYqIccykDJvSbg12OntPv_GTZmKvs5dBaA0zGYrp-1gIJ8Q5Umo6ZjgwYCDUE5sLBwnRchTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوری‌ها خواستار سرنگونی حکومت جولانی هستند
پیرمرد سوری:
🔹
لعنت بر جولانی و نیروهای او؛سرنگون باد جولانی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/690053" target="_blank">📅 11:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690052">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
افشاگری وزیر نیروی هوایی آمریکا در خصوص نظامی کردن فضا
🔹
«تروی ماینک» وزیر نیروی هوایی آمریکا فاش کرد که ایالات متحده سلاح‌های کنترل فضایی را در مدار مستقر کرده است .
🔹
ماینک از برنامه‌های ماهواره‌ای نظامی مرتبط با دفاع موشکی و هدف‌گیری دوربرد نیز پرده…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/690052" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690051">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
تصاویر هوایی از محل حمله آمریکا به مراسم عروسی کوهستک استان هرمزگان که برای اولین بار انتشار داده می شود/ مکانی کاملا غیرنظامی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/690051" target="_blank">📅 11:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690049">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c192c460b.mp4?token=k5OVas2uN4JNPvzx_9LCjgAzE045Pm9t-KfZrnP-2BKEmKc9rbvvy8ktvoPpWiGAzlgSqxS1X0u8Biz06aCGpCSGImOwQafMyqhxX0CqnrLA82izhEJq2J5pMqKarFRxIGz7h41Ax3Ry1KuHu5PsYoh_pdhFP0-ldwSK0F7Ux0vIJC15CzjSsc7iXUsl_HAZhDZYreJtjpTQa2ae2xdP0HjI2-vmaGFQPbYMX1aYzWb8wEQeqbhqb1ZWl2xM8Ljrbp6IlNClI3MsRXTmmDgphEfYkvt1ENd2tBrvkqiPmxD5D7TnRPhfU2xFnsWRGSqwophUWItl-jA7Hf-02XkNYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c192c460b.mp4?token=k5OVas2uN4JNPvzx_9LCjgAzE045Pm9t-KfZrnP-2BKEmKc9rbvvy8ktvoPpWiGAzlgSqxS1X0u8Biz06aCGpCSGImOwQafMyqhxX0CqnrLA82izhEJq2J5pMqKarFRxIGz7h41Ax3Ry1KuHu5PsYoh_pdhFP0-ldwSK0F7Ux0vIJC15CzjSsc7iXUsl_HAZhDZYreJtjpTQa2ae2xdP0HjI2-vmaGFQPbYMX1aYzWb8wEQeqbhqb1ZWl2xM8Ljrbp6IlNClI3MsRXTmmDgphEfYkvt1ENd2tBrvkqiPmxD5D7TnRPhfU2xFnsWRGSqwophUWItl-jA7Hf-02XkNYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیگورات چغازنبیل؛ نیایشگاهی که حدود ۳۲۰۰ سال پیش به دستور اونتاش‌گال، پادشاه ایلام باستان، برای ستایش ایزد اینشوشیناک، نگهبان شوش، ساخته شد
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/690049" target="_blank">📅 11:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690048">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
سرپرست سازمان تامین اجتماعی: معوقات اردیبهشت بازنشستگان تا آبان ماه واریز می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/690048" target="_blank">📅 11:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690047">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbfd6eecf.mp4?token=Cw0bqaMAGkNdQemPJ6uYGpkQs-sZmBzptdoy7Ysc9-_OcavU6QcOinBAxhV8J6-s1Ljnyac_h-e7F0OqnJLQNn8GvQaEmrfIuGt5j_rx2tIn4_I9ad0SgTluIZUzmwyUWSIMvQU2c5hMIu9UrFPNVhLOPX0odpyVbHTzG3q-WOgL_8OtJvMiwtu9mLiLAfITN0gsmZa_MUfjqSAfXDLH0rhIYvBjGGSQyn4ZIckuvbVwDWmZf8SEQdEEuW0b35orhh5JicvA1DsfOf7TiIITZwNkP4OWZ-ZT5sNODOCzsEsdE4D4LJcYE4Jf5NW2Uef5e6BsZU6abE0ZlkWihG8DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbfd6eecf.mp4?token=Cw0bqaMAGkNdQemPJ6uYGpkQs-sZmBzptdoy7Ysc9-_OcavU6QcOinBAxhV8J6-s1Ljnyac_h-e7F0OqnJLQNn8GvQaEmrfIuGt5j_rx2tIn4_I9ad0SgTluIZUzmwyUWSIMvQU2c5hMIu9UrFPNVhLOPX0odpyVbHTzG3q-WOgL_8OtJvMiwtu9mLiLAfITN0gsmZa_MUfjqSAfXDLH0rhIYvBjGGSQyn4ZIckuvbVwDWmZf8SEQdEEuW0b35orhh5JicvA1DsfOf7TiIITZwNkP4OWZ-ZT5sNODOCzsEsdE4D4LJcYE4Jf5NW2Uef5e6BsZU6abE0ZlkWihG8DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وال استریت ژورنال: بسته‌شدنِ خط لوله شرقی غربی در عربستان، یکی از خطرناک‌ترین موارد کمبود انرژی در تاریخ را رقم می‌زند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690047" target="_blank">📅 11:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690046">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7XKdmngzCYx1SRo4itPFqVXNSk7h4-zlGpNbJQ1yS68C3nU7iQZZ6vZMi9au9RvW3CV-n_pmcnl3lSHQx_KCDru9tO6jR0NswKG57gEYrwZPixOXX0pt0mpfPWwFFWHFDp5kuKvOZVUAQbouDjtxkyIV1T05T9OU4OupdOVUc9iC6OPpmK0xPoobaPR9wQHTFaKx4Pl79Lx3dzBk3YhvsT4ARamx5Q3WKw9DphdWBfIsc29yhB8HwdTaa1GmfSpjTt9oxUrETh-uxDkzvu5lXA8bIV9LdZO-Bqkv0CQWjlE1rdJt1icqoi_Fo5VEHmQe9jjghn0OZsl-j4dIqg6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعطیلی صرافی CoinEx پس از ۹ سال فعالیت
🔹
در حالی این ادعا درباره تعطیلی CoinEx مطرح شده که این صرافی در ماه‌های اخیر همچنان اطلاعیه‌های رسمی درباره حذف برخی رمزارزها منتشر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/690046" target="_blank">📅 11:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690044">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
محصولات ایران خودرو باز هم گران شد
🔹
هنوز ۳ ماه از افزایش قیمت محصولات ایران خودرو نگذشته که قیمت مصرف‌کننده محصولات این شرکت باز هم افزایش یافت.
🔹
خودروهایی که از تاریخ ۲۲ اردیبهشت ۱۴۰۵ به بعد پذیرش شده‌اند، گران می‌شوند و ایران‌خودرو می‌گوید بدون پرداخت…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/690044" target="_blank">📅 10:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690043">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f85ce82e6f.mp4?token=bkGzmxYaofvRVjG9uu1gAs5F2r03TX7lCkO4nElh7_JvUlFbSfkHE2VrYOnZXDo5VZfIkqpemcUpQ25jjcTXRwlRPgsyf7dyWEqdcyyW74zs-A3Khb_UQklpFnXDutloROzcLF3pJ3PsKfqNKd7uPiy0paTrf0m_eWSB3B37dan0jtULnIHj4O9dvfU4WPw2WHHuWbriAWE6OoF5GqbOki0rxEw3KcS2ux8b3v12KDcQ6yCtAyEfVKCT8dnYE11eIer3BLbZkQKD892JNwNN2k73YyEzAhwUc44hKnHP0yTDdYBI72bYOVYJVOb6K22_qgfJJhWDzP1cuwVaAEYyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f85ce82e6f.mp4?token=bkGzmxYaofvRVjG9uu1gAs5F2r03TX7lCkO4nElh7_JvUlFbSfkHE2VrYOnZXDo5VZfIkqpemcUpQ25jjcTXRwlRPgsyf7dyWEqdcyyW74zs-A3Khb_UQklpFnXDutloROzcLF3pJ3PsKfqNKd7uPiy0paTrf0m_eWSB3B37dan0jtULnIHj4O9dvfU4WPw2WHHuWbriAWE6OoF5GqbOki0rxEw3KcS2ux8b3v12KDcQ6yCtAyEfVKCT8dnYE11eIer3BLbZkQKD892JNwNN2k73YyEzAhwUc44hKnHP0yTDdYBI72bYOVYJVOb6K22_qgfJJhWDzP1cuwVaAEYyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهاجرانی: ان‌شاءالله گواهینامه موتورسیکلت برای زنان صادر می‌شود
🔹
خلأ قانونی و برخی موانع اجرایی در صدور گواهینامه موتورسیکلت برای زنان در حال رفع شدن است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/690043" target="_blank">📅 10:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690042">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک فروند پهپاد پیشرفته MQ1    سپاه:
🔹
بامداد امروز یک فروند پهپاد پیشرفته MQ1 توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان غرب تنگه هرمز رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/690042" target="_blank">📅 10:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690041">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
مهاجرانی: برای معرفی وزرا به مجلس تا ۱۵ مهرماه فرصت داریم؛ از حداکثر زمان قانونی استفاده خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/690041" target="_blank">📅 10:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690036">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5tF244Tz8y6XhI3OMAShWB-jaAAdYoBo7m5aoGoMoDaPzcl4o03Z8yoX1SprM7jWt-H3oT2IaVQM52k7xPe_IqM5bHHRVPDtr00UZqGeR--wYna0-lQf-EtHeuJ6KilT6Fejamcm2w0mrh-9v8btg7OpNLKENj4tWDakwh483sg30cQVnHaoHuwplwVrk-sCm8-eWswvFQF6GZycsdFr9TfyNPL8IloxLzLeQrcVRzaRBfJQAUD2Y2CTbwsPzapOd0-JhZa0HYrOxjgkxzG-IvAcWGvhuSDTikh7fYHyK-dTcTud-mDAQU1MEKNh8Xi6_ayEfgBIsuh6dlAsTE_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzPfbgP12mOhM9vE8yo5wY08FjxKLCNznqKec5MKOAqUqoZfxOZFgYxUeYkn8F4dahiy_WcDvAUUOSOvyXHDS8dBH7jEuJ_LdfMQenqZwaCwkHwm9gbtdSqsffX4Ng1tDR2dmoOxCwNNN8jmRcuFUZWx4L7BqzB32TBm9xfXmcyfIYhJw3JIWFCItFkCyZFFVyNdv4eQkbJa7Jr4Bu3tOOZFl7oYPRRnWmThHbC6PRv9_uIK7lvKFg_hbjvDEYD8AvtXP98H5dqUrUOOdZdJ-jn-x-rg_PtDGANEXB39A4OFVkeBf-bmuqh4Z-mpHWDLhTb4fLolLuYgETRYuyWzPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2c108cfc.mp4?token=J_feGIyDkH3RIK5zLPMgOithF6Dz0bIp0jkVnOVbaMthgTI-s5SgGMbNCYS0mYX0A3feRbp7M_LkqAk0ZNB4gCT_SevDZiVF5byxFxvejfu0-c_6wAi14TWV6BHhw7blA5U7cx4P3PPbthBgrqdoQ7vi9QUuXgvN1qpPodJAebqg6Dfwyty_Rtt0_4X3ZlUdpfU1W4YuU0QajaLzsVdbuvhJql3OHIIGtvJCrTE5KNs7sbECp19Rl0DKW56q37Ik9joDgh5NRcS4ujLUt6psU9D1j7GBzTVfuqj8uX4veZQflp8eRpHtRZ8a4R3g7kBgtTyW2BFxC5jC5h7HIsJCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2c108cfc.mp4?token=J_feGIyDkH3RIK5zLPMgOithF6Dz0bIp0jkVnOVbaMthgTI-s5SgGMbNCYS0mYX0A3feRbp7M_LkqAk0ZNB4gCT_SevDZiVF5byxFxvejfu0-c_6wAi14TWV6BHhw7blA5U7cx4P3PPbthBgrqdoQ7vi9QUuXgvN1qpPodJAebqg6Dfwyty_Rtt0_4X3ZlUdpfU1W4YuU0QajaLzsVdbuvhJql3OHIIGtvJCrTE5KNs7sbECp19Rl0DKW56q37Ik9joDgh5NRcS4ujLUt6psU9D1j7GBzTVfuqj8uX4veZQflp8eRpHtRZ8a4R3g7kBgtTyW2BFxC5jC5h7HIsJCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تمرینات عملیات زمینی نیروهای تیپ ویژه پلیس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/690036" target="_blank">📅 10:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690035">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4DYHN3eILNTGbmzZJG02GhOy_Q8_sdC1cfgVrJaG5aH6hAjDLg0ku-oZbRb_eB-QNNkLu9X8MmJczwn-ktrlnmb4YJ6u0kbp1eWrNG9PCx5EMb1zGCPVhoh_hJpvPXoqmjoyLml0l3L9H_gUHdDf8k3nK12POomyQjDCtkykiQ7EIDUCIiqWBg0Hha6f6f_04y2eSkfgNRxJFOdWW2w4kYHA_5GiNfw-xQUGIPCryKtrqWvgs_xYttLv3QF_nnn2NGOl5E5z-mAWrSdvfKybIi8JRpiDUIEezHEFqm4aIlYP46hZ12Qs50wPTqa6GqHXWnMVLD4g6ZYEEfkF1Idlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توزیع سهمیه‌ای اقلام مصرفی خودرو
قطعات وارداتی شامل:
کیت‌کلاچ، لنت‌ترمز‌،شمع،وایرشمع،تسمه تایم،تسمه دینام و...
مختص خودروهای داخلی
شروع طرح: دوشنبه ۲۳ شهریورماه
ثبت سفارش با محدودیت کد‌ملی
تحویل رایگان از ۱ تا ۳ روز کاری از طریق پست
💳
امکان دریافت اقساطی
🌐
متقاضیان گرامی جهت کسب اطلاعات بیشتر و درخواست اقلام می‌توانند به وب‌سایت ایرانکو مراجعه نمایند:
www.iranko.ir
.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690035" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690034">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfg2LatsfLSmbyABwhsd-lYJSjv5CERN48Il9QPcTV1PgwOpvDHKAFJOuYsaarUYSt2L_17u9WrmgY6pHtkoyXfAwSvBdccwuwBzDeosChdtDkM9_QcjSeF0VkquuOJ7C2FrOe-F8QL8ZQpFuaiFfIZfC7bBHJ5Ba-0c09IkSzX2zmFoGEyRzP3Tz136Hmh6C0Nh92JptMisiH7x4rfGdnRhMnVTYVF9BmlNFmxZIHXyIM97_GRGjRIXVY7m6kghu9eRBRdANkbKRuJpfW2Mz2OUOko-WaYvLVhVqSPoiDpIxQJlhpyqnpn07p8qNiDJn4weetc7lyhbb-EOOUzgFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست راحتی مردانه سوییشرت شلوار مدل EA7
✅
جنس پلی‌استر باکیفیت و سبک
✅
مناسب هوای خنک بهاری
✅
فری‌سایز (مناسب L و XL)
✅
تنخور راحت و خوش‌فرم
🔴
قیمت فقط برای امروز  1,298,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/59419/180124/
مشاهده حراج آخر فصل
https://l.memarket.me/lp/615/180124</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/690034" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690033">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6f2a563a9.mp4?token=QYcAxZL4eXles535b2fE-f71I9WXyahHFcBYf51PGBOck2azFema2IVJGtqMEP0AdZpW_shaIN4w_MMInDNdNQt4cvb7HwVE8yXpHHR56YLAgnRFBSTg3GiXGPUGZ60vWnuXrShupTr8T6nXKFF4uOBggAA_Q0NuAQPlazum5IxtLkVfykhjLhj3XWhnnf3SHrzDFeEPFjWAtvBfyZnvyWnKh-3kp87fEd3OSPaeytY39I7edmG53HvwCvNYoQWJyzfd2CTbezXv41kMEIEujZr4ZEhFdc9S5SE8cwn-_tuUpcwJHgJM5S-2EAT86IOEB0FMAt77Wcp32NGfD7zE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6f2a563a9.mp4?token=QYcAxZL4eXles535b2fE-f71I9WXyahHFcBYf51PGBOck2azFema2IVJGtqMEP0AdZpW_shaIN4w_MMInDNdNQt4cvb7HwVE8yXpHHR56YLAgnRFBSTg3GiXGPUGZ60vWnuXrShupTr8T6nXKFF4uOBggAA_Q0NuAQPlazum5IxtLkVfykhjLhj3XWhnnf3SHrzDFeEPFjWAtvBfyZnvyWnKh-3kp87fEd3OSPaeytY39I7edmG53HvwCvNYoQWJyzfd2CTbezXv41kMEIEujZr4ZEhFdc9S5SE8cwn-_tuUpcwJHgJM5S-2EAT86IOEB0FMAt77Wcp32NGfD7zE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: مصوبۀ حذف سهمیۀ بنزین خودروهای نوشمارۀ بالای یک میلیارد بازنگری می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/690033" target="_blank">📅 10:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690032">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d58d1b1ac.mp4?token=PfSGz7vcjVyqsRBKpIG6SlHjSymWr7HllboolWVUW81W6ueUJhT21giRlVo6__1DLvFrHIH_OMEoEEIMAQ77Z-M_PkAREFmbeVHUFVkSt_aRG9YFSkzz5Yws5scp7c0VJTYzfukg3Pny7BU9xkUzjjNJO6sLf1HCZkR48Yn58-8lPJW-Ktn7prrPPQKxBAMq1MJAtN_rKe8Wr-w7LBbyb0RkVmlyJ53G3Yp6QKaRC5f_kxOwH7LyG1gEopfJ_kRdh3YO9a_1XrTcacQ8igXIlYihS994t96OKqVrE__ah-uxo9xnIbDUbfoz4gSCmZa_zEPI-ltJdgFz1b4Bg7ALqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d58d1b1ac.mp4?token=PfSGz7vcjVyqsRBKpIG6SlHjSymWr7HllboolWVUW81W6ueUJhT21giRlVo6__1DLvFrHIH_OMEoEEIMAQ77Z-M_PkAREFmbeVHUFVkSt_aRG9YFSkzz5Yws5scp7c0VJTYzfukg3Pny7BU9xkUzjjNJO6sLf1HCZkR48Yn58-8lPJW-Ktn7prrPPQKxBAMq1MJAtN_rKe8Wr-w7LBbyb0RkVmlyJ53G3Yp6QKaRC5f_kxOwH7LyG1gEopfJ_kRdh3YO9a_1XrTcacQ8igXIlYihS994t96OKqVrE__ah-uxo9xnIbDUbfoz4gSCmZa_zEPI-ltJdgFz1b4Bg7ALqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حذف سهمیه بنزین خودروهای نوشماره تکذیب شد
🔹
تمام خودروهای سواری شخصی موجود بجز خودروهای دولتی، وارداتی و مناطق آزاد و خودروی دوم به بعد مالکین چند خودرو، مشمول ۶۰ لیتر سهمیه ۱۵۰۰ تومانی و ۵۰ لیتر سهمیه ۳۰۰۰ تومانی می‌شوند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/690032" target="_blank">📅 10:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690031">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff019fd34f.mp4?token=HmxiKjrBq7mVGmrFR8BlLqi_6x8xcYU1X0heuiKOmIQ8mhNFwJwizSd3yqHajfIkLKFEZuU_M_oAVdyU9euhqFY7pQeXDqPtphKLG3MbTdGBey1nXQ_EuSjLYeA50wzCpfEfHHrQSD5470naJNDRslxGasp0Eg7MDWal1bQ_lfIwrJBM4Dxzd2lnnhJdsHkTbB8CxVZUgWvfViMHIVxgKI81HI7M7vF_QYse355J9POhdZ5_ya3uLQi_pXf8hdtBvyzPGMp2_69qw4ypguwPvjrXn-xcstqOTOCdwAfb56SFfVZ5lVRmodP4-2wpCAHDbRe3ar3hU1B1fBNh1GS39g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff019fd34f.mp4?token=HmxiKjrBq7mVGmrFR8BlLqi_6x8xcYU1X0heuiKOmIQ8mhNFwJwizSd3yqHajfIkLKFEZuU_M_oAVdyU9euhqFY7pQeXDqPtphKLG3MbTdGBey1nXQ_EuSjLYeA50wzCpfEfHHrQSD5470naJNDRslxGasp0Eg7MDWal1bQ_lfIwrJBM4Dxzd2lnnhJdsHkTbB8CxVZUgWvfViMHIVxgKI81HI7M7vF_QYse355J9POhdZ5_ya3uLQi_pXf8hdtBvyzPGMp2_69qw4ypguwPvjrXn-xcstqOTOCdwAfb56SFfVZ5lVRmodP4-2wpCAHDbRe3ar3hU1B1fBNh1GS39g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: بانک توسعه نوین (بانک بریکس) با عضویت ایران تاسیس می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/690031" target="_blank">📅 10:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690030">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن ،بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690030" target="_blank">📅 10:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690029">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74e49a562.mp4?token=LXnAFJxYMF2bDXIBfRqJ8j97nzvscWRPhtmeCZBTKqqyZgKA05DP_098BOBBPzphclHtT0Ye6q-j92KqijhOW1NMXJ5d5dbXKD9LFlvBoeYLvPkR8S_EhfwnnsjAFE7565iLkv4Y8jMmFCmCt_R0Old7Invyebe3uixjHRSBS0viCm_jsuTBDwE8YkidvGEivXHVISHyoSaFcVWUxNUbUL-H-FWOI-WvASmBb3PW9-vDQWueJbpwVIHb7AZz46PYOnHk8tkaclxqpjl7ahnPqSmQN1l9J2zYjxeoP9iDt_8vlgO2xqwnGTNkBm6HSNU3_xiHM9-QYpbaglR6rpILYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74e49a562.mp4?token=LXnAFJxYMF2bDXIBfRqJ8j97nzvscWRPhtmeCZBTKqqyZgKA05DP_098BOBBPzphclHtT0Ye6q-j92KqijhOW1NMXJ5d5dbXKD9LFlvBoeYLvPkR8S_EhfwnnsjAFE7565iLkv4Y8jMmFCmCt_R0Old7Invyebe3uixjHRSBS0viCm_jsuTBDwE8YkidvGEivXHVISHyoSaFcVWUxNUbUL-H-FWOI-WvASmBb3PW9-vDQWueJbpwVIHb7AZz46PYOnHk8tkaclxqpjl7ahnPqSmQN1l9J2zYjxeoP9iDt_8vlgO2xqwnGTNkBm6HSNU3_xiHM9-QYpbaglR6rpILYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نمای چینی با قابلیت انعطاف‌پذیری ۳۶۰ درجه
🤖
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/690029" target="_blank">📅 10:13 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690028">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42042ebc48.mp4?token=NsI04tpdu47zTSJ22Y8HQjWN170btw0-xn6tJa93cF9gWklnAKDfvkNaMMybWJj2HOZAUgJJLhHs_FmSEo2wbxinn2oKvZnR__E64MCxZVctRDNrSQWdaft-g4UF1oBXpD81chExsuQeEdGEyGsL5v0KvooNZCES4VPPgIQEFoEFz-nXECvH4DBwWAZndzgrjbfyckMWJq-lmjBjDeH1FhMiTvr8AiIYUkDiFeQjTheohRo6jEq0EbyKGAwwreANs4w1x6nEtE7PiPTmKSwptFaVgUfIqK5mT8_MvNtDiDAaxflTO9KZ5HdisLr3Kn4lwT5LMvBZ7MSF5-wqtpr0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42042ebc48.mp4?token=NsI04tpdu47zTSJ22Y8HQjWN170btw0-xn6tJa93cF9gWklnAKDfvkNaMMybWJj2HOZAUgJJLhHs_FmSEo2wbxinn2oKvZnR__E64MCxZVctRDNrSQWdaft-g4UF1oBXpD81chExsuQeEdGEyGsL5v0KvooNZCES4VPPgIQEFoEFz-nXECvH4DBwWAZndzgrjbfyckMWJq-lmjBjDeH1FhMiTvr8AiIYUkDiFeQjTheohRo6jEq0EbyKGAwwreANs4w1x6nEtE7PiPTmKSwptFaVgUfIqK5mT8_MvNtDiDAaxflTO9KZ5HdisLr3Kn4lwT5LMvBZ7MSF5-wqtpr0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: بانک توسعه نوین (بانک بریکس) با عضویت ایران تاسیس می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/690028" target="_blank">📅 10:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690027">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d65ac8d49.mp4?token=MkTHehwwT8pnKdULVasOORZbdZ4TzvdJus4FgVQoWmPGOchZ_B0UEuADZsvvu1b2HweL9J_Dc06BhFv_guKt_1HNCZ6ojTBppfTBhRQTuGhkqqUJifLn2wEZ8VCFBPZeI6CYN2cq-bBzud1R2ZqRaYMx65oYi74PVEx2FpU7Rju0CBoWIrAXRx_IyTMDW21EiuPSZNaJrUsfxuhRhKhy1H2kBFL63uMjWh6iNO3etHBGrwHhfAyKDiFjfSplplFgAuQBwcwjjtPAP5DAwaUl7DqOq41ClbC_LOHZwmm5CoYiIyMuwWNvaWtxIh07SI7_6vN04pprvcATIbyxjT1HEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d65ac8d49.mp4?token=MkTHehwwT8pnKdULVasOORZbdZ4TzvdJus4FgVQoWmPGOchZ_B0UEuADZsvvu1b2HweL9J_Dc06BhFv_guKt_1HNCZ6ojTBppfTBhRQTuGhkqqUJifLn2wEZ8VCFBPZeI6CYN2cq-bBzud1R2ZqRaYMx65oYi74PVEx2FpU7Rju0CBoWIrAXRx_IyTMDW21EiuPSZNaJrUsfxuhRhKhy1H2kBFL63uMjWh6iNO3etHBGrwHhfAyKDiFjfSplplFgAuQBwcwjjtPAP5DAwaUl7DqOq41ClbC_LOHZwmm5CoYiIyMuwWNvaWtxIh07SI7_6vN04pprvcATIbyxjT1HEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حالا که داره فصل پرتقال میاد، بیا یک پاستیل خوشمزه و ضدسرماخوردگی درست کنیم
🍊
😋
مواد لازم:
🔹
پرتقال: ۲ عدد
🔹
نارنگی: ۲ عدد
🔹
لیموترش: ۱ عدد
🔹
پودر ژلاتین: ۴ قاشق غذاخوری
🔹
پودر زنجبیل: ۱ قاشق چای‌خوری
🔹
عسل: ۱ قاشق چای‌خوری
🔹
آب: یک‌سوم لیوان
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/690027" target="_blank">📅 10:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690026">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
خاطره عجیب ابطحی از رادیو تلویزیون مشهد در سال ۵۸
🔹
در تلفظ عبارت «مُدَّ ظِلُّه العالی» و «قُدِّسَ سِرُّه» مشکل داشتند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/690026" target="_blank">📅 09:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690024">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu7p6fxoqTOkOi0vUl5HnXvj6nxy0hXCD6dM09YydNcsWfdxBOsnikK9IAdI-gU02VepLGsSEPnUH4j8PT_nuSMZ8kW0GFg-5_y_svLSHKbwu3OG6CPZ_G2UynmF2SLwRDL-coc9PM8gkXgRGRkKh2a_hlFfRVMtTxqsMrIFSGbBTWLyUSMj36yTZWTwK7_hXc9f8EwSxmM1cj6wjyw2khCtXall9vy4nrbrQarXJXEMbDXN91kRa-l8doJuzn9PsgOKYHYLWCbYeE-Fo27eNENPR1AG84eXNtAlCK5TGSjgx8DOHOfw3HE2DJ0S6qulYYRAyGDs8F3hMpy80zxhrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
استوری مادر یکی از شهدای مدرسه میناب: الان باید برای آرشا وسیله مدرسه می‌خریدیم ولی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/690024" target="_blank">📅 09:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690023">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
الجزیره: مجلس نمایندگان آمریکا رأی‌گیری در مورد قطعنامه خروج نیروهای آمریکایی از خصومت‌ها با ایران را به تعویق انداخت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/690023" target="_blank">📅 09:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690022">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLxbEcPAqSJ0GvB_ElADv1trwec5L_TqSfpuaTZSld6ph3ggPJ27zP5hID3RnhaXvnXpaFc6crgfYl2Le5ZCEavogP64EltH4vcimn6lumzb83Asfel5W5UHkoCkn9QlZPbt8SZ2AN18fDvpYHfYU_6KAlierGgiikWVFzk6gejq9Wgy1Oz0YnqN-h-WwVmmTHM35m7T9DcCjHfhe36Xb0E_nm2RuZsIlStDtbTp9qc6j-Uher5W3cX-lisYoA3Ibee_wsE0uZQX7iJEsflFzF4o2yGjkvqsT-z9W9lgH7UWJwtKxn8AGNTGESKa-Btyz5GP38d8WRbnMgb8Cgekng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بنز میباخ مجوز ورود به کشور گرفت!
🔹
فهرست جدید برندهای مجاز خودروهای سواری دارای خدمات پس از فروش برای واردات خودرو توسط ایرانیان خارج از کشور به گمرکات اجرایی کشور ابلاغ شد و نام یک برند لوکس دیگر (بنز میباخ )نیز به این فهرست اضافه شده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/690022" target="_blank">📅 09:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690021">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
اقدام تحریک‌آمیز وزیر افراطی صهیونیستی در مقر آنروا: «حالا من جای مدیر نشسته‌ام!»
🔹
ایتمار بن‌گویر، وزیر افراطی امنیت داخلی رژیم صهیونیستی، با یورش به آموزشگاه وابسته به سازمان امدادرسانی آنروا در اردوگاه قلندیا واقع در شمال قدس اشغالی، علیه این نهاد بین‌المللی…</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/690021" target="_blank">📅 09:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690020">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
داستان نبرد امام علی(ع) با جنیان
🔹
حضور زعفر جنی(ظفر جنی) پادشاه جنیان شیعه در واقعه کربلا در لشکر امام حسین(ع) و اجازه ندادن آن حضرت به شرکت جنیان در جنگ.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690020" target="_blank">📅 09:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690019">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
کرونا وارد محدوده هشدار بالا شد؛ آنفلوآنزا B غالب است  وزارت بهداشت :
🔹
میزان موارد مثبت کووید-۱۹ به ۱۱.۷ درصد رسیده و از آستانه هشدار بالا عبور کرده است. همچنین ۶۶.۶ درصد موارد آنفلوآنزا، نوع B گزارش شده و کودکان بیش از یک‌سوم موارد مثبت را تشکیل می‌دهند.…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690019" target="_blank">📅 09:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690018">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmUtcgbB4gXeFh8VTTBLUrCR6s9uZs5KsDQUOSuTBYjQDk8npx4r8EtFhxTMhq9eYgFUaAPDIvTPIg8ohBkABInr5CWqtUsQKxp3Ggan7epom9CKy8yf73QM12H9rco6Y4aoaVJvoRwIoj90qYMp0iamezSU1hCbe2xsqQ9-aasSjf3AHRk0fvEPNfNAXmCel98isLLkc-mQyWyHO6KYMwYqGbU1bdvWLGChiOTha8bJAKnwfX640dGVrxk90J7WbFOzHffJb9rC7LWjRl_7WXvBk8Jez0qO9lhTsyfLrKdivSufVM623hXbiV4jxC_xiQHrb1w0iHNGrC5TUiSWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک پالایشگاه دیگر در روسیه توسط نیروهای اوکراین مورد اصابت حمله پهپادی قرار گرفت
🔹
ساعاتی پیش از این اتفاق ترامپ اعلام کرده بود اوکراین موافقت کرده که به تاسیسات انرژی روسیه حمله نکند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690018" target="_blank">📅 09:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690017">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkZQjSL1gt1xn0Mw9sEXJ44Olmovx5YcUOOkSJgZt7rfugGMU0sWTOTg0xpg3KbsCAoDfkuftFDoWRSUtyhg4xEF5O_c1b7_t7_WKrXSub7X7HoE2tmhzWBtZmyfmhp4-Fewrig8Se2wy3DirMfIbjwR5skxTHaeRuQLlodZnKBnuTlo7ZplwYpZ-l3fLEEYvanhIn4N3Grc1YH6U5Se7aV0ZcqNHVc_uhj4c5axXPx0BA9NHa24bozUr3g91wdo3pmniKqH6Zfyhg6xEV0LWLrFAg3WIkfnF0EZc2uaBlSzF5q7CJ9VO1wMPKdXatCbtmFPFWmy-wY_ZXV80zXu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روند تغییرات مهریه ۱۴ سکه؛ از شهریور ۱۴۰۰ تا شهریور ۱۴۰۵
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/690017" target="_blank">📅 09:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690016">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5524fcfc69.mp4?token=HqMSZSIVfX6suO6zJSf-97JoBwC41q44-sHY-x_E3Mz-bVU4VcAHOgZkOyUiK1uOpi3loTcgLj8wKB89mDvKR18rI6xM95B4WBOMBmta6NshEP6g-YIx0h2SdV-2_p1tNPxGcIwQ1e09HluYawT6cUnBL-OL7W7JapjcFWPIGuRpha62Bd69DIb_JDk14MtFlis8EPPzaatqz3Ks4NnoncNbdd2GV9jhQ2ThS5O6oGOF34MDaNGLZcKeSMEaxcnaWKvBTAHgDgkiVHjWS6yA0JxYBJbmviveXZh0_x_Li6kT-OzSjODjyoXnGBO21z_4QDwi2dbsI3kvUeMP_n0eMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5524fcfc69.mp4?token=HqMSZSIVfX6suO6zJSf-97JoBwC41q44-sHY-x_E3Mz-bVU4VcAHOgZkOyUiK1uOpi3loTcgLj8wKB89mDvKR18rI6xM95B4WBOMBmta6NshEP6g-YIx0h2SdV-2_p1tNPxGcIwQ1e09HluYawT6cUnBL-OL7W7JapjcFWPIGuRpha62Bd69DIb_JDk14MtFlis8EPPzaatqz3Ks4NnoncNbdd2GV9jhQ2ThS5O6oGOF34MDaNGLZcKeSMEaxcnaWKvBTAHgDgkiVHjWS6yA0JxYBJbmviveXZh0_x_Li6kT-OzSjODjyoXnGBO21z_4QDwi2dbsI3kvUeMP_n0eMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از حضور یک ماشین بستنی‌فروشی در جبهه‌های نبرد در یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/690016" target="_blank">📅 09:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690012">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/358c1c02ab.mp4?token=ByltWy0m5IqQQGjO1sV5oxA2vASA3QKT1FA1CH0x7nHYNdRu2doj-U14lU3mTDyBlQdYAqeFFc7LjLS63_vdSnCyJcva8QasugaAd5bEyVR2JX3aVdDXFEZWMn3idL4lPzYsX5onom4AFZBak6XIHEkeqlqw0kJj866n9oCLIncwEJFeQ5y0AXxIzY0C3nbOgMlJ-IKP2DWPr6QAOckdHXLMOaeaC8jq5wlps_vUEQMeVpVS2VhWz1sINrorWk-aPSIVkklDClKZvol8Xs4XNdNYYYSQU7jnuLkaFG4oEDaXraG9ptC3lyV3W5PkuRlEsY5c4nB461dwZ94n1FRzxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/358c1c02ab.mp4?token=ByltWy0m5IqQQGjO1sV5oxA2vASA3QKT1FA1CH0x7nHYNdRu2doj-U14lU3mTDyBlQdYAqeFFc7LjLS63_vdSnCyJcva8QasugaAd5bEyVR2JX3aVdDXFEZWMn3idL4lPzYsX5onom4AFZBak6XIHEkeqlqw0kJj866n9oCLIncwEJFeQ5y0AXxIzY0C3nbOgMlJ-IKP2DWPr6QAOckdHXLMOaeaC8jq5wlps_vUEQMeVpVS2VhWz1sINrorWk-aPSIVkklDClKZvol8Xs4XNdNYYYSQU7jnuLkaFG4oEDaXraG9ptC3lyV3W5PkuRlEsY5c4nB461dwZ94n1FRzxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین اعتراضات گسترده در سوریه پس از سقوط بشار اسد
🔹
افزایش ۴۰ درصدی قیمت گازوئیل و حدود ۲۶ تا ۲۸ درصدی بنزین، موجی از اعتراضات را در چندین منطقه سوریه به‌راه انداخته است.
🔹
معترضان با بستن برخی جاده‌ها و مسیرهای انتقال سوخت، خواستار کاهش قیمت سوخت و هزینه‌های زندگی شده‌اند؛ در برخی تجمع‌ها نیز شعارهایی علیه احمد الشرع سر داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/690012" target="_blank">📅 09:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690011">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
فرمانده هوافضای سپاه در آستانه دویستمین شب بعثت ملت ایران: عظمت و شکوه بعثت در خیابان‌ها را با حفظ انسجام و اتحاد مقدس در همه ساحات حفظ کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/690011" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690010">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
فقط ۶۰ درصد خانوارهای شهری بنزین مصرف می‌کنند
🔹
بررسی سال‌های ۱۳۹۵ تا ۱۴۰۳ سازمان برنامه و بودجه نشان می‌دهد سهم خانوارهای دارای مصرف بنزین در این دوره به‌طور متوسط ۶۰.۱ درصد بوده است.
🔹
یعنی تقریباً ۴۰ درصد خانوارهای شهری هیچ مصرفی از بنزین ثبت نکرده‌اند.
🔹
این سهم از ۵۶.۹ درصد در سال ۱۳۹۵ آغاز شده و در سال‌های مورد بررسی حداکثر به ۶۲.۳ درصد رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/690010" target="_blank">📅 08:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690008">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmHM2GD2ly8kBZ3p5ylg_7WuYq_9m_k8sokFmDEquX9K3V8-BEemFAM0KF6VBOcBrwuaWZFA0nTZ-s7pCzHEpKfu86HWSz4YE6r9sp-qxg7VD729zLWuEklvrv0Ie0viWzQuN4ADAuLH_M84TLOhST37MHCdOH3va8WRKP4kbZG8n_R6pDVm_SUnT40n_xLNAEGsRgO2QgGu_QgMoeyb8ur6xCLDRJuofiw0a7yvfVPguMfaZePWbHVXS9BzAwqQKKe-T4x9w-tZbxTwcU-AFLUcLeD70kWJgmxvAFF4bqdFJRFRYjlqgYASC9_we6lKbIf0Tb8MPXjh80ge9RxwcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BnMzlQoCZW0AOej-356BEt_pf6l3yM1LzZQu6alme39kJ--lcsugCvpOCpfKXdrEqtT9NEDyJmiUQXDvwEsWF4x8Pq7EnIRZ43Lj_6NKo9CDSuvmjtEl-MgXZrKIFvbWtFV_9F2o9q124pM7_klzvchBWFAElNsU4W2jMz7k187p86ZiG27eXC6ovN5V1a9hmnwGOxFZadz3qgxcWLMjv7gCH4Rcw82URTPwL9wN0K4BcvfIYwqbpGSf0Xm7t1krb79BpF0l92G4ow9pf0696vH86gBJKuITfczs-GprIHgJ9rhe-mIhk8dDtzINiL1VUxYvfl8KJVHzPx57a9Pn7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تانکر ترکرز: تنها کسانی که انتقال محموله‌های STS (انتقال از یک شناور به شناور دیگر در دریا) را در تنگه هرمز انجام می‌دهند، خود ایرانی‌ها هستند ...
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/690008" target="_blank">📅 08:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690007">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0ZmaEUTLopJ560zAcAW5AvmpVFHzx1DLSI1VYHoZIZxkQpiAGKAyO8FDOSg7GxS0Dj88bJZcAbPlXi5w1IluidHQ5Y3khQH752-gxWZC_2cUQa6_n_GxudOZdLzL9Q8W8QY_yBaLuIgiySi2EsDLqpn3wSkZhXdM7gAV7-bnRLaAmlTcTOJD0dNsMp_ECJwuAVWPh4zEPsb5AS7rAZZmxmDxGOsCOxlJ0Fi7YLOiHsJYY0maJYTu9kyDkwJva2eOg76k3xcgPtI1Q3uhZDcAh9p4YcbWZTG3uYpmZ4aEsQc-lfqzt3FfKkyZ_5fGOp74fI4hPBZr36JYJ4wSF2Zpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رده‌بندی گرم‌ترین شهرهای جهان
🔹
بر اساس داده‌های سازمان جهانی هواشناسی (WMO)، شهر «قبلی» در تونس با ثبت دمای ۵۵ درجه سانتی‌گراد، گرم‌ترین نقطه جهان به شمار می‌رود
🔹
پس از آن مطربه در کویت با ۵۴ درجه و بصره در عراق با ۵۳.۹ درجه سانتی‌گراد در رتبه‌های بعدی قرار دارند.
🔹
شهر اهواز هم با ثبت دمای ۵۳.۷ درجه سانتی‌گراد  در رتبه چهارم گرم‌ترین شهرهای جهان جای گرفته است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/690007" target="_blank">📅 08:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690006">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEPiJowdkeJsz9FcJ_7VOYSIeGh0PzB9ZTcRcXb7e9qRTjapdYxM0jKT4d1oN4vYt50zWv3CrjmsUzvHpGy884KyLuKwJGC7T7mion7zfQ_ceJ87tBATV_8mabHkPx9x6GY4hw_NZRQyUgArFts0Hjjo-a1MCyoN-VttEQ0piY4qe8lPvaxFuy_zbXgQkxQz11JvlMqRz-59DMPjyDnArfkEakEJ2Z1SUwWfCaj13gdoNMLopStz-fDX9ZqJAuejsAmxIle9zQWgCFFI-6bBzanHjkSglddUkeKqHzSFjqWy5EBnHkOzTXdVdmAPJC3yi70E96s8DpOQCdlPZx5TQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه دروغ‌های ترامپ درباره ایران
🔹
ایران خواهان برقراری توافقی است.ما تصمیم خواهیم گرفت که آیا در مذاکرات شرکت کنیم یا خیر، و این گزینه‌ای است که ما برای آن آماده‌ایم. #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/690006" target="_blank">📅 08:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690004">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
فردا اعتبار کالابرگ کدملی‌های با رقم انتهایی ۳، ۴، ۵ و ۶ شارژ می‌شود
🔹
مبلغ فعلی کالابرگ همچنان یک میلیون تومان به‌ازای هر نفر است و اعتبار شهریور تا پایان مهر قابل استفاده خواهد بود./ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/690004" target="_blank">📅 08:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690003">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/676582eaec.mp4?token=WWPL8AFT_vdpBCV3D65gNIr-ySOS1fOMKLfC1Wt1Bxh0WX2PvYhHSbx4DIXScw2ZfWciYMMCupd1dAMUjBxyOn1xP1cOjUgphn40ZiGzVF9CiMtWGgjtHCFcN_M7pabLgk5G6uzcyfOblXbbwc5mSPoF8UYOFM9bApaRgMSq_keeeNs8XEhJzkzH-TxM7ppAncrcWcEfXSzOKy84P9BVDarFtReEi189H2Q2moCnsg1rPYhO_khM05Cnem3mxohjjdrF_TiNDc7-Rp5XmEaVgthwMIrUt1w4zV_YPAX3AdAEnoPyGwA_podxku_nsakBoYiPn-GTQuKJmr3qvtJCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/676582eaec.mp4?token=WWPL8AFT_vdpBCV3D65gNIr-ySOS1fOMKLfC1Wt1Bxh0WX2PvYhHSbx4DIXScw2ZfWciYMMCupd1dAMUjBxyOn1xP1cOjUgphn40ZiGzVF9CiMtWGgjtHCFcN_M7pabLgk5G6uzcyfOblXbbwc5mSPoF8UYOFM9bApaRgMSq_keeeNs8XEhJzkzH-TxM7ppAncrcWcEfXSzOKy84P9BVDarFtReEi189H2Q2moCnsg1rPYhO_khM05Cnem3mxohjjdrF_TiNDc7-Rp5XmEaVgthwMIrUt1w4zV_YPAX3AdAEnoPyGwA_podxku_nsakBoYiPn-GTQuKJmr3qvtJCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترور عالم اهل سنت در زاهدان
🔹
مولوی یوسف گرگیج، از علمای انقلابی اهل سنت و بلوچ زاهدان، توسط مزدوران صهیونیست مقابل درب منزلش، به شهادت رسید.
🔹
اخبار تکمیلی متعاقبا منتشر خواهد شد.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/690003" target="_blank">📅 08:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690002">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: مخازن سوخت ما در حال انفجار بود و پس از مذاکرات قالیباف بود که تانکرهای سوخت به کشور برگشتند و توانستیم سوخت را در فضایی دیگر ذخیره کنیم/ قالیباف گفت برای حضور در مذاکرات آبروی خود را وسط گذاشته‌ام و آماده شهادت هستم تا این ماجرا حل شود
روح الله لک علی آبادی عضو کمیسیون بهداشت و سخنگوی فراکسیون ورزش مجلس در
#گفتگو
با خبرفوری:
🔹
ورود آقای قالیباف به مذاکره اقدامی هوشمندانه برای جمهوری اسلامی بود که یک ژنرال و سردار را پای میز مذاکره آوردیم که این پیام را به دشمن بدهد که به هیچ عنوان کوتاه نمی آید، اما برایم عجیب است که چرا برخی سیاسیون متوجه این موضوع نیستند.
🔹
قالیباف یک نکته را از روز اول مدنظر قرار داد و آن  اینکه تعهد دشمن باید نقد باشد؛ دقیقا برعکس تمام مذاکراتی که در طول ۲۰۰ سال گذشته داشتیم.
🔹
آنچه در این مذاکرات دریافت کردیم نقد بوده و امروز ۸۰ میلیون بشکه نفت به ارزش ۶ میلیارد دلار فروختیم.
🔹
نزدیک به ۳۰ کشتی حامل کالاهای اساسی را از محاصره خارج کردیم و کالای اساسی وارد کشور شد و تانکرهای سوختی که خارج شده بودند از محاصره عبور کردند.
🔹
ما گاهی جلوتر از فرماندهان نظامی حرکت می‌کنیم؛ شمایی که گوشه ای نشسته آید و فقط شعار می دهید مراقب باشید و ببینید که فرمانده چه می گوید.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/690002" target="_blank">📅 08:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690001">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
کلاهبرداری ۱۷۱ میلیارد تومانی از بانک؛ متهم پیش از فرار دستگیر شد
دادستان تهران:
🔹
یکی از کارکنان حفاظت شبکه‌های بانکی با دسترسی غیرمجاز، ۱۷۱ میلیارد تومان از اموال بانک کلاهبرداری کرده و هنگام تلاش برای خروج از کشور دستگیر شده است. بخش عمده اموال نیز توقیف شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/690001" target="_blank">📅 08:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-690000">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
خبرفوری/
انهدام یک فروند پهپاد پیشرفته MQ1
سپاه:
🔹
بامداد امروز یک فروند پهپاد پیشرفته MQ1 توسط سامانه نوین پدافند پیشرفته هوافضای سپاه و تحت کنترل شبکه یکپارچه پدافند هوایی کشور در آسمان غرب تنگه هرمز رهگیری و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/690000" target="_blank">📅 08:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689999">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUAfFOaRRY-ZYmnOclrQ4YtH75oJ5GmN8TeRdM3FbbxHble4-qLiPeGWAIvgWRgM0hymb_l-VmroBlvt7ck4Rtibf2eAVmo1hV_wiXPxj7o1Us9a86T-hzxqzTOV3WQ4MNlb_FU5lFP4WF85UvLmnjZXc442H9RH49EP0pgpyn41rSIOpYyIeO1aw9HJHu1TLxOVobisaH3ZRGTrKAN4NAB9be0D6VLgxy0484xJ5jy7pj5juw1Ihw7NeFvu3PXrQqrYmLE7AZmhqMF1osHwC55PNaeTLm78OXvf_pk9z-zxcEji9bkIJF-6vq5wOTc7ZV1pf5a7g6eVpdSVN0x2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه دروغ‌های ترامپ درباره ایران
🔹
ایران خواهان برقراری توافقی است.ما تصمیم خواهیم گرفت که آیا در مذاکرات شرکت کنیم یا خیر، و این گزینه‌ای است که ما برای آن آماده‌ایم. #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/689999" target="_blank">📅 08:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689998">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtXPAFKHeuzBwFqDhfOkP7L0BgMj515AJnmtHupx1LnPm5yMw21R5iwGq8QRueQ76FsVKst2yOuKuuo6m-EdP2KRxlQnZixKvjnEs3VY4bCPKOwLI6sRUNh-AB6viMPQpSONGXTnlZZRjwNj6Un-_WIU_MJYRJYL1-frWY5AkZJWs0hW7DZPcCLtdAxAwk5_pU19iq4wBXXk0WMUYy23RIB3HpfP2UXx3MphkCICw8lPoav-kN9C0QuqJAPStMeifkjGrG58BdNe4W46skm6s4Im2RkrfcLryq1K6x6NNsgDV-uM1-NinAhFVm9Ta0HkAOq0xHi5gGMyP8m3xR6pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۴ شهریور ماه
۳ ربیع‌الثانی ‌۱۴۴۸
۱۵ سپتامبر۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/689998" target="_blank">📅 08:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689997">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSeap7KZCsyzwoWHdr5J5H8vgOOuANJpSNrfN0PPYZY66Fb_rJ6C6FdSpiPcZXFJw3GVDTsckDxxr8XwPGPvrhtKZbMkaqUiptunOLhkRgoE7DxDpNPIelK7NG2F0UWEvDspsmShiHGS5oiDODd1zcNbuXdqo7uOkGT6WuCjp2X6MmgqBSQ6FRfvkfhKTc8_PqTHBL7FDK0S7Ms-J8IcZkd32IRBy6wykG_jL9CGJcQVd55FFUNV2YesLBv3_n_4NT4K0ZqFUjecvpDf8oGA9fmrT9Ptc_Nw-XGGr6bt1O233hZpUxq38PwZhVoR_0K7Nhu6mNdbHgZGVhlUZP9h_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۵۰٪ تخفیف برای تبلیغات حرفه‌ای!
یک پکیج، حضور در ۵ پیام‌رسان و دسترسی به بیش از ۲.۴ میلیون مخاطب
🚀
@Titretejarat
📱
روبیکا | ایتا | بله | سروش | تلگرام
اگر می‌خوای کسب‌وکارت بیشتر دیده بشه، این فرصت رو از دست نده
👀
🎁
۵۰٪ تخفیف ویژه برای حمایت از کسب‌وکارها
برای اطلاع از جزئیات و قیمت کلمه‌ی تیتر تجارت رو بفرستید.
@ads_ghimat</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/akhbarefori/689997" target="_blank">📅 00:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689996">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCVsCSDFs6u0baoRIll-GcsPtAbJFL2QDSvIHlvaS0ooM7_f69IfwiGBQD49VZzawXzUia8Zx3HggKXfccdy_sLJXcU51AyqXSB9LwIZeL0CtSW4BD3jKSmYaItR1WmBkNkQJkYRjaFO6F-2qZStdOsNVSOyvKrn_nDRm24tPCGtYznf6lSVj_bQ1YiKqRRLZlcQiHR8bswrrfYP8EbBUhIT-_7KvmdhbMfj_cqmJom6HEJ4Lv4ne_OgQJ_IHcBXSsqc5-_GQTiqCM_iLs4Kg_U9k90MhDNLBWjOLBJD-K6cieu-8K2mfwGC-_IWj_Ftqvevwef1M_KuwJMhA3Tg1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هنوز هوا سرد نشده، ولی وقت خرید کاپشنه!
🧥
کاپشن مردانه
Adidas مشکی | داخل تمام خز
💧
پارچه مموری ضدآب + خز تدی گرم و نرم
✨
کلاه‌دار، جیب‌دار و شیک
💰
الان با تخفیف، به قیمت پارسال!
📌
قبل از شروع فصل سرما بخر، چون وقتی فصلش برسه خبری از این قیمت نیست!
💰
قیمت ویژه تخفیف: فقط 2,380,000 تومان!
👇
خرید:
https://memarket24.ir/product/brief/50703/180124/</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/689996" target="_blank">📅 00:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689995">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1-cd6BHoJ9CnV17zKw8TVM9nwoIOjEIjzPbKrKWAX7KjoYZiolviyOVY38sxRzNrdocssPTe8hWA2SWuoOsRRJDACozEwkxunD6S1wVtL5oM0IS5_ODsJ8ze4kSqZ9mesO7u_OnedokH4to3ffaxAAZiawWIk2tGkmqbo7YTb8j4hplzRd8_gJ9U4pOLKczpTdxuVPOcB_RZeqI_AA2ZGc2YsXaA-KrYS1NFpu_8ti1w0wuk1QtPYr45-F8GDI-WPJrTKUU8VgmiTYsTiPqnMH8rqvydvY2e3ymxswhZE2m3134Qs_9lAxFP_F9u8UOOcfuBcj8ANNH6oVd1YHcQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
730 / نبض لحظه ای بازار طلا
🔥
🎷
آبشده ۷۳۰ با قیمت کف بازار
قیمت رو آنلاین ببین ؛
⚡️
همون لحظه بخر بفروش
📍
پشتوانمون حضور فیزیکی در بازار
💰
قیمت رقابتی
⚡️
معامله لحظه ای
⏰
هر روز ۹:۳۰ تا ۲۲
۷۳۰؛ جایی ک قیمت بازار به معامله
تبدیل میشه.
قیمت ویژه برای همکاران
وارد پلتفرم شو
⬇️
⬇️
⬇️
abshodeh730.ir</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/689995" target="_blank">📅 00:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689994">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mApNZGuDSEDwxh7N3t0Ee3CAoLTTxzt3swSPg75bbFbnHlAYcXviv_ZYOiyeKkgiV760lSr1Pf18En1SI7LcvayYF0XU_k7VexpNbdLb37TPwP3OZookZxdMqJuAdMyYL0NrMxRP6_wUfpq7aC9ELG9qTV_v3nh6-TDYn2PfRPkKqHglyJUQRpptCqlH7SyYuRtkqmJuySrHftN3lWD9ijfC96lHaK0-7DKyYibjI16t4Dduq0s-NELkOBrsFOiev468vkjXlck5m7fG25BR36IxF5DfjYYMJ_Ah2hsf5lh3_oCtmtmSu7ULRighhavBYupJVPQLDh6jUtb7B3kXlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال سیاسی ضدجنگ آمریکایی: ما طبق معمول، همین‌طور برای خودمان پرواز می‌کردیم و با مصونیت از مجازات، مرتکب جنایات جنگی می‌شدیم
؛
تا اینکه ایران از خودش دفاع کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/689994" target="_blank">📅 00:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689993">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بقایی: عدم صدور روادید توسط اتریش نقض صریح تعهدات دولت میزبان است</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/akhbarefori/689993" target="_blank">📅 00:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689991">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
منابع خبری از توقف عملیات پروازی در فرودگاه ملک فهد دمام عربستان خبر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/689991" target="_blank">📅 00:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689990">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_FFg77PInlqfPOpyAenop7fFseiMyFN7bTefdZHCswYb2xqxoEBmH3asF-vcE2emhvCZ8AXYG-dw2B2AQnmCNqazE82-7AwzH-le9AxTIp5byZF7LxoGDQLtyEMSCnaB7igQY5VivIceAlFEFKIJ4kSUKWJSjFz7JuC3XccNDFPaxSDrKdn4Cy-OEr-sShRRIdtZCkaXKN8WdUEL4tZs4AEEzJs3S4Ro_fNcn6oSuh8F7ZmWGLSTem2gV8wphxaMTy8xWcF4faA0RG3jmYWWM-YQ-slPMYoa15QMy0mt7HBGo13eA25YnK2dUxph4NEVwP9uOXI-2-eW2OwoTtnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیگر هیچ‌چیز غیرمحتمل نیست!
🔹
در فرانسه، آلمان، هلند گازوئیل ۳ یورویی دیگر منتفی نیست؛ اما برای آن به یک شوک با خشونتی نادر نیاز است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/689990" target="_blank">📅 00:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-689989">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkuTn73l4spfYH7j0CorR5MFnL_WVORmrFh08-Qhf3uq6ld9kEv2TfmgqqlF36nz2Py7WZ76E-ERgqBEkP-6Q0Ny4lyIRyPe5ZMHlnfr1UnibMhEusB_fJ70KPHNcyb066C4WfJ5lgTYmOXsUBf9A0DL1ayp2c4_XDLSo-XU6s0KYXTtX_0WY4KBLsBpbwUF393M94ZS39kyYT2nNw_YZAgWZumLsq3woyLdQbEs93-22trgyBHTF5_Z5IbvCqwBhsJ4N2AXwbUyj2ha-EE9xnfqJHLFhs5zdLShcam-eIfoIvRRFxgF00AUfuutCT1xA81tvBjzs1Xn0pwfZSAyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت روز با بنزین گران؛ مردم چه چیزی را تغییر دادند؟ | نه صف‌ها خلوت شد، نه خودروها خوابیدند!
🔹
هفت روز از اجرای نرخ سوم بنزین و افزایش قیمت بخشی از سوخت گذشته است؛ اما برخلاف انتظار اولیه، هنوز نشانه‌ای از سقوط شدید مصرف در جایگاه‌های سوخت دیده نمی‌شود.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3245136</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/689989" target="_blank">📅 00:02 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
