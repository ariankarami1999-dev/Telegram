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
<img src="https://cdn4.telesco.pe/file/fFAGFRpolZR1WQSVV6IGYMwwxEaRKNgBS_lFnekThVtFj_Gbzrcl1seWFVQ4jvUu9IIyFnfpFmHVCEvUCVaIG7bk1_GpdEDkXhejmfUYGQMAJYbuncPHYDpZDFSok-35VQuDfC5yIqOwiJd82WvllL8w891hOv-n3-IymlAY9C3qDiVzQwQOJGDrsf2RGzjSkom5j6uKMDOcpgfQOQ6GIRPmPdCc99tXbmAOhV4UiUox_E8cJT6XGRdAejG0FU2ECDaI3NwGv1zeRwBcfYfru5JAg2txRzcaprPlMRRRumWOOoqJPQGP36LTvlxqOQ7uBnMdNebh1AS9qb5_9st_Tg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.17M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-24 18:41:23</div>
<hr>

<div class="tg-post" id="msg-681455">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 13 · <a href="https://t.me/akhbarefori/681455" target="_blank">📅 18:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681454">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19612db87.mp4?token=FIUvy51RbNPwemuFtk5t-XJp3977moitVDT9eLQ-PZN3qZ4bjzk_My_SXTkWtakUfCnjiIDx3mh7cihVAQZYA3YAZ_i4Z08xoISNjRBOjFk-YoW9lE9Et77v8mNuQ2Gkl5qd4TXVQdGX-Ksv8IfEUrH-DzG4iktH0-n2V6fyk2jYJwXnQnx5nQyWwdYZKc-efg3ynPKYAwnguRb2A9mE5uwLXthjOlAQZKScne1OQrt0eOxnSoZqSEGk5O32OiO3FH8hjpXSBg7YRSK4kRMXvlLK6yrMo4Y2-Rfo5HoB-TuPytRJIFMdZB3GL-S2-4o_n7r7mqMEcbmNNUNhwnLW7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19612db87.mp4?token=FIUvy51RbNPwemuFtk5t-XJp3977moitVDT9eLQ-PZN3qZ4bjzk_My_SXTkWtakUfCnjiIDx3mh7cihVAQZYA3YAZ_i4Z08xoISNjRBOjFk-YoW9lE9Et77v8mNuQ2Gkl5qd4TXVQdGX-Ksv8IfEUrH-DzG4iktH0-n2V6fyk2jYJwXnQnx5nQyWwdYZKc-efg3ynPKYAwnguRb2A9mE5uwLXthjOlAQZKScne1OQrt0eOxnSoZqSEGk5O32OiO3FH8hjpXSBg7YRSK4kRMXvlLK6yrMo4Y2-Rfo5HoB-TuPytRJIFMdZB3GL-S2-4o_n7r7mqMEcbmNNUNhwnLW7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور شبانۀ پلنگ نر در منطقۀ شکارممنوع کوه سفید دماوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/akhbarefori/681454" target="_blank">📅 18:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681453">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استانداری تهران: منتظر اعلام رسمی پایان جنگ از سوی شورای عالی امنیت ملی هستیم تا فرآیند دو ماهه انتخابات شورا‌ها آغاز شود.
🔹
مورفی، سناتور آمریکایی: جنگ با ایران از اول قابل پیروزی نبود، ترامپ فاجعه آفرید.
🔹
اردوغان: بسته بودن تنگه هرمز به نفع هیچکس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/akhbarefori/681453" target="_blank">📅 18:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYte3zEUdyRmgHRTQo0AIAUbv7PmYOEOxOgNbYIqx6OztmtOrvpmydyMDjMHnrzfZN_EwTAt236h_Zpcq_vme6V8mBL1z9dRXBpmq0hQLqe7KMW87dUmyxaXb4gMMv7ICe_SLewMKSSQqDsbU78Oz68GBqvmsWM_8U6JqierkI733Utsj8_AVbjDFtyoKrmuc5Iqe1aAhwVGf7LQVLZVO7FeumnzOEpeonrEPkWCCx4PkUbVAp8kB7br9PFeltoRT6jLNuPlNLSc_hl6MX3v-ohwOcEtty9f48LlX0ULeR-Gmfy7juvOBc8Mpxq5QLWwQ4wgJUFzncMRxcj7OxcG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJtWWUuQg1Ikh3mtIRTVI9Qg4k8cEoR46vMHxTSsJMaQ4xkZNSZcCHZsa0XuQxjo3MC-nlCMC--fuRvJs44AiJT-Js7D2jMaiBXPFtgmggC4caMkIywN2wbPO0lMIYsK7ABX-LF0xntooVMNDsJCZyrxvBD-pPGXXEoxUlA2_wYaCExoGu2m2j5MJjxhs6GHqD_m6ZU0XvRe4UmCQxKjnSSjqWo7HtcWtf-AIHWuJwcxQQ913WiM4zM10UL8Czj5pNxJX2Ehp8xJ5WOMaW56lSlB3vSpaOG_XHRcSHrU8t70-QAfkL6mrD8a4xGAL2NN9lwXogKc2ll1AFVCmTDGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SahPDlO33Uu6co0Gx4nWWcA7SAYM4BDJHwaP08tSUlC-jA3IuSy-UQkVhUTwbXFXpsGkeZRU0LurWZ5RoWI5rD95XcifDAlhQZ6lM1AKvRJCruGjn-EPYQFMENRmE3VdEc3kt84zP4S6MsmdNLyolJmfXZWBdqfbMB-Q_nqDfKcMnmK7d6j3lu0Ndwz32kbPBbMaHGULvAE6inPmlsdIAtXzmDcDjIUG1JGvehd1cbfk_san21_FOUZs-F4EM80pI5IydsvdwCGXI135KqCBElj7U0CWeqs_Wz8gOnz3DtQhfTfVeK1_wNCMExQSXC_NDnLfstW2yazo_8wWUA1Q0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IM4z83PmkIgghFa1CKXCZPTFGHHtqQ0ZB59TQrq0RsmmAia_FtqavJGbA9DY3qG-Zo53QmCNbAZSvkB-EWVqV7-Oa2ixhR0aKgoK7saafQuk1jyYBFhYWGmkk3dWADWb1z8Yd7HmEOKwzcL2URMX0OTbQTKopYvVgFzxFho8fxJs1nn1sLQhSwzxWO5KdDYZu4IOoNDSIQxXbq3eflGRbbkjpbJPZNoaRWTSuWRw4949KQe-syCUvF8zkW40veAnHdkoHN-QFOLLJwHn0nhTqGXiZL6EOZ7HG1hPBXaxPnje_Ca4e1eh9ZfUCsNkQaR1dYDjKWUyf499tmjNsmDQdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qEZq5fVbMdKZ6Wmv8XspxJRAhln5yzU6UBXsWLZO2TyDUxn_6yS02_n1ej-Q-xSSGc-9cuDmTz7Avmwn-SfnDYHbgbv1aWgy71tTzapRiaEqYSRQZtDOUc5GypkvJbq8E1m97xfuQrDGrkZmvsWt0EVz6Ipk6rKbihWvs__vD1wrpmXir_cNU-XiBX0TFBzbQORup7HmUJjsZ5864Xb2vZ716WLeL91QL6BkmAdnoGpW14_A2Gx6ebNXhrCBiM88qwonmObjzCcWnCnkmipiPNlMr_8CQsgnpJgCFt8fPzewWRsSgcJ9gWTVQkOrZ773fJ23HE5HjCZaXKB1EptnBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر متفاوت رویترز از خورشیدگرفتگی در اروپا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/akhbarefori/681448" target="_blank">📅 18:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFziUu_Nqv4uIE19d7zhV5gRMXw-imzUoYlymPv1nVU9_1x8saEa4-UFxDUZpgBfUvrPGQnCvX7f-eNr0mfLyEEc2WHgGdOWlFyzcA4Me_gAI9md3in-xk0cVT1jC6yI5dllGX4uEHaXjt-4uRkLQkz4svCCuGSGBNbPH8BB3hRZj5NQ4GjUjwKhuEO4EsVOV6PwrfGhQXYDsclb9aEojd9THECdjQqr5LNkJd32C4MUXLIvEjS4EAvMwHyZGhCfsKJNPOM4w83pDfut4Wb8zD0LClI-PxgnI29P8OWmicmTey9J4WOlLNP_lAmXm_66ZjLobDfs3oFj2hX_80Wqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برگزاری جلسه سران قوا به میزبانی رئیس‌جمهور
🔹
در این نشست سران قوا ضمن بررسی آخرین مسائل و موضوعات روز کشور، درباره مهم‌ترین مسائل و اولویت‌های جاری در حوزه‌های مختلف بحث و تبادل نظر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/681447" target="_blank">📅 18:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681446">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
گاردین: انتقال مخفیانه ترامپ نشان‌دهنده نگرانی جدی واشنگتن از تهدید ادعایی ایران است
🔹
گاردین گزارش داد مقام‌های آمریکایی در اقدامی کم‌سابقه، ترامپ را در جریان سفر به ترکیه به‌طور مخفیانه از هواپیمای ریاست‌جمهوری خارج و با یک خودروی خدماتی منتقل کردند؛ اقدامی که به نوشته این رسانه، شدت نگرانی واشنگتن از تهدیدهای منتسب به ایران را نشان می‌دهد. با این حال، گاردین یادآور شده که مقام‌های آمریکایی تاکنون از کشف حمله‌ای در خاک آمریکا که مستقیماً به نهادهای امنیتی ایران مرتبط باشد، خبر نداده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/akhbarefori/681446" target="_blank">📅 18:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681445">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC02MBL9zlkh6fWZj6TnUYfI8mdKPKhuFiZ0facf03wUReJIpC12pAAZuXJCkWTt3gWfsI71pd5ss8JulSNB41-PIDC2Yl-gAJ9fPdxYbCrRn0ShY4Yk-MvJmBEGVzL_GVSRUmbAoabnSbSgce9tMyS1bd9yb0fiM0AyQnoMO_LIhiKY0gsLKRVDwyN54ClrKNu7-CqurchmVxY8DxLEBEWXYeTVNjCgbK4SLrGLTOh7KUlkkSDsYM9FZQXOmpaOswe38HHKxw53Sn-i-Ako5_m8JNOE-F4H4ax9dx_6gCVZn7Hz_Yfjipg53chTWOcES84yRYGLuiKmSBYYn19Iqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روندا؛ نگین درخشان اسپانیا که جسورانه بر لبه‌ یک دره ۱۲۰ متری ایستاده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/681445" target="_blank">📅 18:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681444">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDeg6GGuEuXhpX_E-jkosvYlfjYzz8U_ID30aFjyeB-065LxXc8D-vvOyjZWOqCj1pW75Rx0mlne7nNrU1Ska--8wOFs_wMxGKzquhfPzxZdq7ma2MWUwV05NafvMDuVtyBmdjVcgVrC78T9t25EwSxe5U-X823kPXO0LvLkqh47SIOJRIBdR_qDp5oGp69RUVvSKAKGr3_FOzG9hXlqbsAQZH4TU5sza2PMZf7OVp9_Z00OKzemXgVMikkb8pDV2Gqv3D8kibs5kfQQQ8ANspksuLmlXnHfePaAgSKi5ePU3h0y0mjOPz0EvBvemOWjDnVW3e6N3XgmolNaQ9E0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دانشمندی که نامش با جبر، الگوریتم و پیشرفت علم درآمیخته است؛ خوارزمی
🔹
محمد بن موسی خوارزمی، از بزرگ‌ترین دانشمندان ایرانی، تنها یک ریاضی‌دان نبود؛ او از چهره‌های تأثیرگذار در ریاضیات، نجوم و جغرافیا بود. آثار خوارزمی نقش مهمی در گسترش علم جبر داشت و واژه…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/akhbarefori/681444" target="_blank">📅 18:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6tQEtSk_8bhXPRjC1WksVHYeuHrfgQsipA9HjjKwyvQR0yvR1XY7SLC7ZkEBkcfp7cZND8oL245fVy_yjWxnZASKO9z6BzZf-4kS-W8Jd47H6lvSI8ja9OVZ9MYqBg8erW-W5i9dlG72Yaicz7hWwYXbxhMEW6Xmnw22Kw8BjIVHTf_sy5_-CIlV5nzcW9al4jmabl79it8OV6FnitwyAMG8OWTZf8SGGaUJKA_GCGFaRyyXVrRrepySYCXLxl0x1nCx33mK0DLyzBV5nYhD6VD5oXC5AP5kg7sV_fuchT1m69NQJDB6YwapV98RVJReOT7RhJ38q0q7-CAIeYBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-SsE3EK_frSKLgopMG2VdZ4Rq76IZzF0ed0RQHdBJx-0ChOt6Ch2FuvSfkpqQNOAIJZ0BLPgdhMvYlQ6zJlAsUfYXtMK6hci_1wIMLkLnjKLGAHmOIhRb1cVQEo756DARp3274n_-2_BqDRdVQ-lx4cQOosqTlpavvfGI27O9ERHs1IPdsndSruGiNcV2XSh5fQUn8HA6pKbaamNlLWeNnz7By9G6zw7g58q_Fb2CVeG9h-HhC6ct1UT62zCY49mhfAP6UbLAXqcEHUCodJNaJ25xSDmqJLDZXiHFdZovyeJPnHO_4cSch289mtQ1Sv9O9wYLJtpN8JibFPZF5CMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
آدیداس و دیزنی کتونی راپونزل طراحی کردند؛ سه‌خط‌ها پرنسسی شدند!
👟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/akhbarefori/681442" target="_blank">📅 18:01 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
بوی تعفن راز جنایتی را فاش کرد
بازپرس ویژه قتل شعبه یک دادسرای امور جنایی تهران:
🔹
مدتی پیش بوی تعفن در یک مجتمع مسکونی در محله نواب ، راز قتل زنی ۳۸ ساله را پس از چند ماه فاش کرد؛ جسد این زن داخل پتو پیچیده شده بود و آثار ضربات چاقو و خفگی روی آن مشاهده شد.
🔹
قاتل پس از شناسایی توسط پلیس آگاهی دستگیر و به قتل اعتراف کرد.
🔹
قاتل ۴۰ ساله:باهم زندگی می‌کردیم‌. بیماری اعصاب و روان داشت و چندبار خودم و خانواده‌ام‌ را تهدید کرده بود؛ عصبانی شدم و خفه‌اش کردم؛ جنازه را لای پتو پیچیدم و تا صبح کنارش ماندم.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/681441" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoyHmQ9DHh-aTQZAUnhTuU7YcWHxik4PSLGHmnTqkNOCpc3MIfydrJ86QKyF7ptQ-XcF_XVFblONC-F6eA9uMraXedkcOYgJvUE5N9EdDY47LGRBGK7L1puRSfvdsuMcsp8XmXQNKG-ycBpsBLsJIeS9JJMNODqSNtwoi_7-EvKevzIGXBpq36cCyRUwbl4nxUAwXzQ9Y7H16XV1RopxbIbCo1jWnINeAt60N6fci9hY1f6TPogEXLUNQFZFlgh_W6VsMMTDbemhFyo8eUNgNTb3N6gHILl5Uz5lt-O8oz69-id0jJHpGapsvARAy8YbPscStWx42LN0NJms_ho0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قطر خطر کرد
🔹
ستاد کل نیروهای مسلح امروز اعلام کرد که ۳ خلبان ایرانی پس از سقوط سوخو-۲۴ در حملات اسفندماه، ۶ ماه است در اسارت نیروهای قطری هستند و اجازه تماس با خانواده را ندارند. اعلام این خبر با واکنش‌های تند و تیزی همراه بوده است. مسئولان ایرانی باید با لحنی صریح و قاطع، خواستار آزادی فوری این افراد و فراهم‌شدن امکان تماس آنان با خانواده‌ها و نمایندگان ایران شوند. دوحه باید بداند که ادامه بازداشت بدون توضیح روشن و دسترسی قانونی، تبعات جدی سیاسی و دیپلماتیک برای روابط دو کشور خواهد داشت. قطر نباید جایگاه خود را به‌عنوان میانجی منطقه‌ای با چنین رفتاری خدشه‌دار کند. اکنون زمان اقدام است؛ خلبانان ایرانی باید فوراً آزاد شوند، در غیر این صورت ایران حق خود را برای اتخاذ اقدامات متناسب و قانونی محفوظ بداند.
🔹
هشتصدوسی‌‌وچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681440" target="_blank">📅 17:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09430cfdc.mp4?token=C8kZYnsF_S-spDD_vd53-5OAfHexYO5X3NRyq35UEbgugVnvJ_rNnoBgj7c_d1nYZKdewe3-TcdQaJTiykrinvJVL0zvKpmmtY-4o8Xw9gN30yCbxU3JceYYhpr5KZmtjS_48oqqox6m1HOp2EFdei9tCkdVdQBrCOk_WDbs9BkdNs6NObEMJHeNZoiSzuGQOQ8cL-OIvNuCsMnB-Fa4mHOmHK5o3HPDaJZcQsdCMBml0GtsW_Kn04MsaLu-_lFxNuk2WebqmJ5l1tkgCqb6oh62EYzw81vOUO_orsCNnB3xqu0BfV2WekScunaSrBG-uJa1RlRKXAmtHAXBgI-1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09430cfdc.mp4?token=C8kZYnsF_S-spDD_vd53-5OAfHexYO5X3NRyq35UEbgugVnvJ_rNnoBgj7c_d1nYZKdewe3-TcdQaJTiykrinvJVL0zvKpmmtY-4o8Xw9gN30yCbxU3JceYYhpr5KZmtjS_48oqqox6m1HOp2EFdei9tCkdVdQBrCOk_WDbs9BkdNs6NObEMJHeNZoiSzuGQOQ8cL-OIvNuCsMnB-Fa4mHOmHK5o3HPDaJZcQsdCMBml0GtsW_Kn04MsaLu-_lFxNuk2WebqmJ5l1tkgCqb6oh62EYzw81vOUO_orsCNnB3xqu0BfV2WekScunaSrBG-uJa1RlRKXAmtHAXBgI-1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو تله مالی پنهان که هر روز تو رو فقیر تر میکنه! #چرخ_زندگی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/681439" target="_blank">📅 17:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
اسکن مغزی؛ سگ‌ها احساسات چهره انسان را تشخیص می‌دهند
🦮
🔹
پژوهشگران دانشگاه وین دریافتند مغز سگ‌ها می‌تواند احساسات مختلف چهره انسان، از جمله ترس، خشم و غم را از یکدیگر تشخیص دهد؛ چهره‌های شاد نیز مرکز پاداش مغز سگ‌ها را فعال می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/681438" target="_blank">📅 17:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
آمریکا هزینه جنگ را از طریق متحدان عربی خود جبران می‌کند
جلالی‌زاده، فعال سیاسی اصلاح‌طلب:
🔹
ایران بیشترین آسیب را از چرخه جنگ، آتش‌بس و مذاکره دیده است. صادرات و واردات ایران دچار آسیب شده و آمریکا به هر صورت با هم‌پیمانی با کشورهای عربی، زیان خود را جبران می‌کند.
🔹
مسئولان کشور برای پایان دادن به این زیان، باید اهرم مذاکره را جدی بگیرند./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/681437" target="_blank">📅 17:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIvSF91aoxRvFSI2W30AfieA1oin4sQgGtQdQ4UOhorJMcPUW6owQh8FXEYQDsnkAAPQTszO-R6B9i1KQ5OdXlrN60QmUzRzmfMNJMmYkv_69XM4PCqimu0K_zBKrsj5gtMVuAAJ9yDyhEkDQlaiDodJUhnkhM5y357OAWb7FAObsJ9ufRuize4YS3uFilUUoZItborX8sf1Ul-Sy_1ekHPABJJlkP1t4m3SwDdgbaySwaYPSAfZOOu6zdj1xhoDEV6rphfHnDL2KwBjklTOazlgp_NePuDWopOF9-SvdfcH4CiIvJk-_OsBJ7URxleLml22_tozjzAzoMmLcV-FxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست اینستاگرام نوید محمدزاده با لباسی با طرح پرچم فلسطین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/681436" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c55eef2cd.mp4?token=oQudpL3LORKYmgeXuUDfAi1xoig9Oib-31kMcwwvYNjw76O1PL0jCFPOyBqX_taze2QyjPkhEadkEjwMdIOY8Bj7eY3rzQbPbFXw4rZcL6Y_jeCGmImI8w4rYcBcy2gWqlfrowyxVhCT9DVo1QBulN_ALlPR_UINzfdju2qB7Xg-oG7w6TW-R0keWqfitugGA53X6MKig9OhX2fIfnubl53k0JCcULT1VgDy1BIARa-apHwVHWPnaL2--jRPo2W8u3hwZGYLIAGf_TjNHtF9RJU2ERIImNiRk5ge7UVS_NIiFfj4FAhv9Ka6xtezJ_KMaAEGtyecXILTV2L4r_JRcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c55eef2cd.mp4?token=oQudpL3LORKYmgeXuUDfAi1xoig9Oib-31kMcwwvYNjw76O1PL0jCFPOyBqX_taze2QyjPkhEadkEjwMdIOY8Bj7eY3rzQbPbFXw4rZcL6Y_jeCGmImI8w4rYcBcy2gWqlfrowyxVhCT9DVo1QBulN_ALlPR_UINzfdju2qB7Xg-oG7w6TW-R0keWqfitugGA53X6MKig9OhX2fIfnubl53k0JCcULT1VgDy1BIARa-apHwVHWPnaL2--jRPo2W8u3hwZGYLIAGf_TjNHtF9RJU2ERIImNiRk5ge7UVS_NIiFfj4FAhv9Ka6xtezJ_KMaAEGtyecXILTV2L4r_JRcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوکراین مدعی حمله به رقیب روسی استارلینک
🔹
کی‌یف مدعی شد موشک‌های «فلامینگو» یک مرکز موشکی روسیه مرتبط با شبکه اینترنت ماهواره‌ای رقیب استارلینک را هدف قرار داده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681435" target="_blank">📅 17:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراقچی: مانعی برای صدور روادید اتباع افغانستان نداریم
.
🔹
حزب الله لبنان: تداوم جنایات دشمن اسرائیلی بی پاسخ نخواهد ماند.
🔹
به دلیل اعتصاب کارکنان ایزی‌جت، صد‌ها پرواز در فرانسه در آخر هفته لغو شده است.
🔹
پیش فروش بلیت‌ قطارهای مسافری شهریور از دوشنبه آغاز می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681434" target="_blank">📅 17:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deedd68fa3.mp4?token=VQbsrc9_rhixmir8KDEblXLFIXFJG09PUVg8pFsmXD5kbKFhtEvSGDKWlbBj7OHVXJMOtoDw-4lp0eLD9JTPCyLESh_22qBom4VKpG-soSAiYqaGh9TxlkrTIjjMCHOI9Z646vGiBnUMMPqC00UCBtdbeFQcMeV4g0uvgZf2TALLyzQjirVG9T1LDhKH3iJPelsqAsfSZ4esHS0-pyTfwTRGmNlieVVTphzeO7p7Ewuy9dzPMPTxbq9jvc0i8MIlOfTsIrD3zGXi1TiJIV7_yCy6DudXr2OL1qXmrqGwKuqErGQ2TQxNklMeKk6fUEGK5JCx3Ke7_1SD5KFFVNoYYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deedd68fa3.mp4?token=VQbsrc9_rhixmir8KDEblXLFIXFJG09PUVg8pFsmXD5kbKFhtEvSGDKWlbBj7OHVXJMOtoDw-4lp0eLD9JTPCyLESh_22qBom4VKpG-soSAiYqaGh9TxlkrTIjjMCHOI9Z646vGiBnUMMPqC00UCBtdbeFQcMeV4g0uvgZf2TALLyzQjirVG9T1LDhKH3iJPelsqAsfSZ4esHS0-pyTfwTRGmNlieVVTphzeO7p7Ewuy9dzPMPTxbq9jvc0i8MIlOfTsIrD3zGXi1TiJIV7_yCy6DudXr2OL1qXmrqGwKuqErGQ2TQxNklMeKk6fUEGK5JCx3Ke7_1SD5KFFVNoYYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قرار نیست هر چیزی که در اینستاگرام ترند شد، تبدیل بشه به معیار زیبایی ما!
🔹
این روزها بعضی دخترها از سن خیلی کم سراغ عمل‌های زیبایی میرن؛ چون مدام با صورت‌های فیلترشده و استانداردهای غیرواقعی مقایسه می‌شن.
🔹
شاید بد نباشه گاهی به جای پرسیدن «چی رو توی صورتم…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/681433" target="_blank">📅 17:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمشاور سرمایه‌گذاری ترنج</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEyOXclgbvIKqU47mcNnAZp0rnrPLSYgJtkftL0K0gaeVTZPcODnCaz3IeDpDbb2XnIOkF6_wsSnMR8DIve_AAYdH9l23KhAvyA9yADeITrgtS0kjydKfDeJnnAUQGBA2OiueLQeOOm--AHvBBBhycSe-HXwR0VLkwUR21BZtCQzll7LRNg-cyuf9HySmTGGWKhh-Ji9FaK5VcBfUuQ7HvZCxGXUtGuWt3zD9EgLkYhb7U7UM_h-bixVr2-yUuIqqytvaUdKiXdjobta1kh8OZGqw230aY52NQ9UmAb5jyj_0VwDIwspQ91mz8fH-T3s_UFbJqNv9TIlTqOfaHberw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترنج ۱۰۰ همتی شد...
🟢
دارایی تحت مدیریت ترنج از مرز ۱۰۰ هزار میلیارد تومان عبور کرد. نقطه‌ای مهم در مسیری که با اعتماد آغاز شده و با مسئولیت ادامه پیدا می‌کند.
🟢
برای ما، بزرگ‌تر شدن یعنی مسئولیت بیشتر؛ برای تصمیم‌های دقیق‌تر، مدیریت حرفه‌ای‌تر و خلق ارزش پایدارتر.
🔵
ترنج؛ ۱۰۰ همت اعتماد
▫️
@ToranjCapital</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/681432" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU64dRK9SnBqLXsnRsmjzvASJdzUEFUEz_CC0kUKSxts3oJ6v0IznC3UhzIEI-qdd8J1Xp8Ko6gGMxXKBT9hkXn-HNMSIxisa7bv9s9auHyMLA1CC6bJBgI5XCwuq3SxpoQjmvI7ZyAzsg2MOakxhTnCXoTn8IYwxvnPfJkhAsvaP68eaCBC96fKElc_-t-3J51J8aOntBFXMZVbxSn8hmcBHh8At0L2EaW_mEMAlryiUhY6PKzrEGci1oq21cSZwbuV0q1M7ebSKr40i9INzWfajeJswuXopdy4qN_Y3tvzGcSnAA4CgpU5grKby3N3U2XNMUChHi8NhRxgoDmZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدت دریافت بیمه بیکاری بر اساس سابقه و تأهل
🔹
به افرادی که ۶ تا ۲۴ ماه سابقه پرداخت بیمه دارند، در صورت مجرد بودن ۶ ماه و در صورت متأهل بودن ۱۲ ماه بیمه بیکاری تعلق می‌گیرد.
🔹
همچنین برای افراد با سابقه بیش از ۲۴۱ ماه، این مدت ۳۶ ماه برای مجردین و ۵۰ ماه برای متأهلین در نظر گرفته شده است.
@amarfact</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681431" target="_blank">📅 17:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca86c810ab.mp4?token=hz3T8vmkQOFIkD-G_mImgOuS7pXmSHoUmIHIMMoC8Z4OARMcPpqMum0th2Yx4pVuZ9Vlk0gMZbRYO3IgDajl-CNH3pX15gGTwjtKarfYbcz1PPaaOcUP8C2YTtQoozTVTl8LTy9-X8bj4ZbICapdct_UAdtEjaklTda_zi98wkOdtq-NR3MtbPkUcxjT9ZgY0M2iMKUf8IkTgHaJYHFZbp366mt8pVvs6K0DIZjzi97yNKAU2O27nSzu-ktNVK1JyKVgMaDkJJLXcj1yYePIaVW_ytBDNZk_aQ1j5492SBoBt70FmhPzPmmG_aOMu3eCmbYI6BTxyfyejCGe61KGSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca86c810ab.mp4?token=hz3T8vmkQOFIkD-G_mImgOuS7pXmSHoUmIHIMMoC8Z4OARMcPpqMum0th2Yx4pVuZ9Vlk0gMZbRYO3IgDajl-CNH3pX15gGTwjtKarfYbcz1PPaaOcUP8C2YTtQoozTVTl8LTy9-X8bj4ZbICapdct_UAdtEjaklTda_zi98wkOdtq-NR3MtbPkUcxjT9ZgY0M2iMKUf8IkTgHaJYHFZbp366mt8pVvs6K0DIZjzi97yNKAU2O27nSzu-ktNVK1JyKVgMaDkJJLXcj1yYePIaVW_ytBDNZk_aQ1j5492SBoBt70FmhPzPmmG_aOMu3eCmbYI6BTxyfyejCGe61KGSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نادر سلیمانی: رضا عطاران در دوران ممنوع‌الکاری پفک می‌فروخت و در سیرک کار می‌کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681430" target="_blank">📅 17:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تداوم حملات رژیم سعودی به مناطق مرزی صعده در یمن
🔹
رسانه‌های یمنی از تداوم حملات توپخانه‌ای و راکتی رژیم سعودی به منطقه بنی صیاح و روستاهای اطراف شهرک «رازح» در شهر مرزی صعده در یمن خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/681429" target="_blank">📅 16:58 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46402bb50.mp4?token=DgFs5Esnd6hUIgJEuUNu4MTBTOuu8YD9jBg4LD1LCn_8t-LxXW4353Qycg-kezpnAdDhhax-cY_ee8K_R0baXlbI6LplhOySfdlpTUWl6g0uZU-HQyOv3MmDm6gD5UmrwrPu1nl0RgBdJ_oPE6GZ8a_62ednuCWkanChY4Q-922VVIPjM4dP8W8D7wFl-dArF2-ZHTgahhsoTqdbkCUvYmNUxHVj2elg0gQccBUqlbl8KrqaGTL9-nE3VDZQvT9T1aS-Fm1T0xqhGDVkqaQD0nkRibv1et3MRBeVgzSlKloVQdZ_wY9himduzpsN2tdGzrEQpHttXaI9_WEegnoAfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46402bb50.mp4?token=DgFs5Esnd6hUIgJEuUNu4MTBTOuu8YD9jBg4LD1LCn_8t-LxXW4353Qycg-kezpnAdDhhax-cY_ee8K_R0baXlbI6LplhOySfdlpTUWl6g0uZU-HQyOv3MmDm6gD5UmrwrPu1nl0RgBdJ_oPE6GZ8a_62ednuCWkanChY4Q-922VVIPjM4dP8W8D7wFl-dArF2-ZHTgahhsoTqdbkCUvYmNUxHVj2elg0gQccBUqlbl8KrqaGTL9-nE3VDZQvT9T1aS-Fm1T0xqhGDVkqaQD0nkRibv1et3MRBeVgzSlKloVQdZ_wY9himduzpsN2tdGzrEQpHttXaI9_WEegnoAfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنجاقک؛ خلبان ماهر طبیعت با قابلیت پرواز به عقب
🔹
سنجاقک‌ها می‌توانند هر چهار بال خود را به‌صورت جداگانه کنترل کنند؛ قابلیتی که به آن‌ها امکان می‌دهد درجا معلق بمانند، ناگهان تغییر جهت دهند و حتی به عقب پرواز کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681428" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ذخایر جهانی نفت تا چه مدت می‌توانند جنگ طولانی ایران را تحمل کنند؟
نیوز دات کام استرالیا:
🔹
اختلال در عرضه نفت ناشی از جنگ، حدود
۲.۶ میلیارد بشکه
از عرضه جهانی را از بین برده و نگرانی‌ها درباره دوام ذخایر اضطراری را افزایش داده است.
🔹
برآوردها نشان می‌دهد ذخایر دولتی کشورهای عضو آژانس بین‌المللی انرژی، با کسری فعلی عرضه، حدود
۱۸۰ روز
دوام می‌آورد؛ در حالی که بخشی از ذخایر راهبردی آمریکا نیز به‌دلیل مشکلات زیرساختی قابل استفاده فوری نیست.
🔹
این وضعیت نشان می‌دهد طولانی شدن درگیری با ایران می‌تواند فشار قابل‌توجهی بر بازار جهانی انرژی و توان کشورهای غربی برای جبران کمبود نفت وارد کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/681427" target="_blank">📅 16:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
بقایی: توافق بر سر نقشه تردد کشتیرانی در تنگه هرمز حاصل شده است  سخنگوی وزارت امور خارجه:
🔹
با وجود کارشکنی‌های آمریکا، گفت‌و‌گو‌های ایران و عمان روندی رو به جلو و مثبتی داشته و توافق بر سر نقشه تردد کشتیرانی حاصل شده است.
🔹
این اقدام حاصل یک همکاری جمعی…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/681426" target="_blank">📅 16:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/230c5d55ac.mp4?token=U78a7eua9QU2BMANPK57Aw5zhzZgOGqSyQPHAHbWjh8x7hyLQClAL6bUmn-b2nZKmqK_lSvY93ttrKbUtqTCPpsrZKSlYJ8oONBz8V3taA3kWLzuZbUVBVLRBRIywK6TG1JpY-VSR6pitZ4BXCZ8e7ZcvgUMkOcbliv-QjAOdYqpIZ1RkpKOCp6pjB2mWIve3JgoFNEH3AA6rU0dKSgPDUZJw2wZCugh1hoh2ifBbhtW22FCyAZ0NNWWcovvA5we6kyEtQNNIge7TPHAf1pF_9xE-6DcvkKS2MVqWq9r5Mh1V1vBELysk7LsiAzmjF-EkknoLvZqGRLGSM2T-o1-OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/230c5d55ac.mp4?token=U78a7eua9QU2BMANPK57Aw5zhzZgOGqSyQPHAHbWjh8x7hyLQClAL6bUmn-b2nZKmqK_lSvY93ttrKbUtqTCPpsrZKSlYJ8oONBz8V3taA3kWLzuZbUVBVLRBRIywK6TG1JpY-VSR6pitZ4BXCZ8e7ZcvgUMkOcbliv-QjAOdYqpIZ1RkpKOCp6pjB2mWIve3JgoFNEH3AA6rU0dKSgPDUZJw2wZCugh1hoh2ifBbhtW22FCyAZ0NNWWcovvA5we6kyEtQNNIge7TPHAf1pF_9xE-6DcvkKS2MVqWq9r5Mh1V1vBELysk7LsiAzmjF-EkknoLvZqGRLGSM2T-o1-OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز از دید شاهد
👀
🔹
انهدام یک ایستگاه توزیع گاز در منطقه چرنیهیف اوکراین توسط پهپادهای انتحاری گران (نسخه روسی پهپادهای انتحاری شاهد۱۳۶).
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/681425" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد! #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681424" target="_blank">📅 16:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpmZfHKOxXfmZPWwut5AEP7hMMaVwHbvePazPf9uMqTxdI5fqlw0O_7GUeAYHi_GhNwhOivr-o1e-aY77J5fvF9zA5xgZ9S9viJUwMO6BnNErf3iwrZW72CLvAMKAkpZ2AqWxeII6kzoxOPrl10GcAZh7NDbqk995hjTSwUxTL87oQ-0RhAFGDtO0Lc-AnKLqJhk28vdq-3O32m_hGIWQDgwytcqs54fseEM3_eSCT4sCHK5vYlMVxlJzUymt04Bsxo-eUwAAAsyoeLrqCWf91A5UcSpMIlJAnsrLNFY2_AQ_CS10gruBdZWn0VQgj1xp0DzuIB13gCRSNPf5UPz4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست اینستاگرامی رونالدو برای ازدواجش
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/681423" target="_blank">📅 16:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpzK9rPl3SMwGIbuNi31drlJwFNPTtosJ4zsBUJa2PxX0NbzB-stX27ZSQUNbAvgVxy3_Fh5jUYgfN_09oAfETVdPeWsEatpnjinQ6SvThXAbG2vq0DmUB-tp19G0QIHC9fdxTHK37OFQ4dFUCWTW32JJBdToyN3xFFGzUnTDpWvqj6r2-9UCYRnIeaIMjv8-fTMWb7SyHf2kWfHzT5K8It7jpWfdXw12lHr4sdOBHM2HBRiwixxMNbN84tmu27-1p_tzY-Kf74zCEZ6ieT6FWtULBUWQnTL8ZtZyE_KHzlGe7OPRoc-mRQeOLwdgNGGQlwOmjsZ95ClpxQKZcLTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آسوشیتدپرس: تلاش آمریکا برای ورود اتریش و یونان به پرونده ایران
آسوشیتدپرس:
🔹
با متوقف شدن روند مذاکرات میان ایران و آمریکا، دولت ایالات متحده تلاش‌های دیپلماتیک خود را گسترش داده و از ظرفیت کشورهایی مانند اتریش و یونان برای کاهش تنش‌ها و بازگرداندن طرفین به میز مذاکره استفاده می‌کند.
🔹
رایزنی‌های اخیر مقام‌های آمریکایی با وزرای خارجه اتریش و یونان و تماس‌های بعدی این دو کشور با وزیر خارجه ایران، می‌تواند نشانه‌ای از تلاش تازه برای شکستن بن‌بست دیپلماتیک باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/681422" target="_blank">📅 16:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بقایی: توافق بر سر نقشه تردد کشتیرانی در تنگه هرمز حاصل شده است
سخنگوی وزارت امور خارجه:
🔹
با وجود کارشکنی‌های آمریکا، گفت‌و‌گو‌های ایران و عمان روندی رو به جلو و مثبتی داشته و توافق بر سر نقشه تردد کشتیرانی حاصل شده است.
🔹
این اقدام حاصل یک همکاری جمعی بین‌دستگاهی با محوریت وزارت امور خارجه و مشارکت فعال بخش‌های دفاعی، امنیتی و زیست‌محیطی کشور بوده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681421" target="_blank">📅 16:18 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کشتی سعودی مسیر خود را از باب‌المندب تغییر داده‌اند
شرکت ویندوارد:
🔹
پس از تصمیم یمن به محاصره دریایی کشتیرانی عربستان در دریای سرخ، ۱۲ نفتکش و کشتی باری فله‌ای با پرچم این کشور، به دلیل ترس از حمله، مسیر خود را تغییر داده و از عبور از مسیر تنگه باب‌المندب اجتناب کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681420" target="_blank">📅 16:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHZJ6i9dwWekuwE8VNavc2INKZ7GZv5q7r2w8bSf4jX-ZttOFRw2DYCObJ2LLgMv5V5wSDUgVhbPKm-Vih87AC0iq0jvd6wtKANIAqbR5qVkPasVsUYTAoXQq-BYUvWWoAIxX4hArFNAfmy00TGc9nI-iMryiDYdrVFyLCmEdvXmHdNBEvyrwSwfry6RZho8Cjt492zuIqYym-txzHDWQeEK7szOaFQ5l10jjP-HW_5C-9aYnOppA-a6gp98sCpZXY0uqXa4C-4BEdGL-aoNyqsMMfhS7jRrG22h3gMgUDMCl8V-NXsFu8RutjLIiauYHt6ywNW40_6PlY5QP4vpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در اسپانیا به نزدیکی خانه‌ها رسید
🔹
آتش‌سوزی گسترده در اسپانیا به‌سرعت در حال گسترش است و شعله‌های آن به مناطق مسکونی نزدیک شده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/681419" target="_blank">📅 16:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
گرانی وانت کار دست مردم داد/ اجاره پراید وانت برای کار، ماهی ۳۴ میلیون ناقابل!
🔹
در حالی که قیمت پراید وانت در بازار به بیش از ۱ میلیارد تومان رسیده حالا شاهد ایجاد یک بازار عجیب و جدید هستیم. حالا بسیاری از افراد توان خرید وانت ندارند و به سراغ اجاره وانت برای کسب و کار خود می‌روند.
🔹
به عنوان مثال در یک آگهی پراید وانت به صورت ماهانه به مبلغ ۳۴ میلیون تومان اجاره داده می‌شود. البته نکته مهم دیگر اینجاست که معمولا در آگهی‌ها ذکر می‌شود که باید مبلغ اجاره به مدت ۳ ماه واریز شود./ خودرویک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681418" target="_blank">📅 16:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23620ece1e.mp4?token=I8fE2LPyVUX7oUlyZp5jQLXWtNyqCY9c6i5IjoHvhlwLx4kZScaaeZh16RYhXf2BU8lufSRlZk5BwASzc117H8Mv0yyf0_CQjWTJsEfp_5HYhIEwyXLM0jHQMpWKhjD7A2YG3CtWYCsB-ogdN1jlXE1jxWCOUgmBgC9D0UUrevWB-uahR3FctH4eQYg57gQvORpODEK0LKlQF2Yne-52rVykFtbm8-W5JYE4Scs3o1yXoSOJ7Annrcusy1bu-hg9XcLZ-ksGHhpKvGYhnU7ZsQY7DEV36dghAQpfT73-j6CyIE7P33USXP-a4zldMY-a-8R6T-q0J0bCp7wkZ1xXwb7dGC5v1cwjLrWEeyeooWCEbwRRPi11NznCUB0bZFOnbf7w7_Z_XI-P9s_wUOg8nYU4n7_yyX6upfT_L9HWMWQB1352faRDyFGPIvaAnolJjepp3j-KUex4SmmYHiCfZKtP3egKIZ9Oa6X5Ix7eb0XOhQv0kOtcRi36CCmJX92GqLddKw7shWPx5Kdg1VlhUpH54sUtBHfGwUnL0AKcQT9MI9DMFQt7mGh7virNH9teol_zczZHwoPemeZYMpQt_8Pj_f7gtx-jERzaNBbHYgNxJf67GDTo3WXk2JkG-lDitc4jDgn1MWA7UPO5rdE4ba7bfN4aWfIkN6whmGBEMI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23620ece1e.mp4?token=I8fE2LPyVUX7oUlyZp5jQLXWtNyqCY9c6i5IjoHvhlwLx4kZScaaeZh16RYhXf2BU8lufSRlZk5BwASzc117H8Mv0yyf0_CQjWTJsEfp_5HYhIEwyXLM0jHQMpWKhjD7A2YG3CtWYCsB-ogdN1jlXE1jxWCOUgmBgC9D0UUrevWB-uahR3FctH4eQYg57gQvORpODEK0LKlQF2Yne-52rVykFtbm8-W5JYE4Scs3o1yXoSOJ7Annrcusy1bu-hg9XcLZ-ksGHhpKvGYhnU7ZsQY7DEV36dghAQpfT73-j6CyIE7P33USXP-a4zldMY-a-8R6T-q0J0bCp7wkZ1xXwb7dGC5v1cwjLrWEeyeooWCEbwRRPi11NznCUB0bZFOnbf7w7_Z_XI-P9s_wUOg8nYU4n7_yyX6upfT_L9HWMWQB1352faRDyFGPIvaAnolJjepp3j-KUex4SmmYHiCfZKtP3egKIZ9Oa6X5Ix7eb0XOhQv0kOtcRi36CCmJX92GqLddKw7shWPx5Kdg1VlhUpH54sUtBHfGwUnL0AKcQT9MI9DMFQt7mGh7virNH9teol_zczZHwoPemeZYMpQt_8Pj_f7gtx-jERzaNBbHYgNxJf67GDTo3WXk2JkG-lDitc4jDgn1MWA7UPO5rdE4ba7bfN4aWfIkN6whmGBEMI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی می‌گن سکه حباب داره، دقیقا یعنی چی؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681417" target="_blank">📅 16:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
محکومیت پرسپولیس در پرونده بازیکن سابق
🔹
با اعلام فدراسیون فوتبال، در پرونده شکایت سینا اسدبیگی بازیکن اسبق پرسپولیس، این باشگاه به پرداخت مبلغ ۱۴ میلیارد ریال بابت اصل خواسته و مبلغ ۵۳۹ میلیون ریال بابت هزینه دادرسی در حق خواهان محکوم شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681416" target="_blank">📅 15:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عراقچی: با عمان بر سر نقشه مسیرهای عبور از تنگه هرمز توافق داریم
🔹
مترو و اتوبوس در تهران، تا پایان جنگ رایگان خواهد بود.
🔹
حملات توپخانه‌ای رژیم صهیونیستی به جنوب لبنان
🔹
وزرات جهاد کشاورزی: مطالبات واردکنندگان کالاهای اساسی پرداخت می‌شود
🔹
نخست‌وزیر لبنان: شهروندان اهداف نظامی نیستند/ اسرائیل تنش را متوقف کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/681415" target="_blank">📅 15:48 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
هندوستان‌تایمز: ایران با وجود حملات گسترده اسرائیل، توان موشکی خود را با سرعت احیا می‌کند
🔹
این رسانه گزارش داد با وجود خسارات گسترده ناشی از حملات اسرائیل، ایران در حال بازسازی تأسیسات آسیب‌دیده، احیای ظرفیت تولید و تقویت دوباره زرادخانه موشکی خود است. سرعت این بازسازی نگرانی‌هایی در اسرائیل و میان برخی مقام‌های غربی ایجاد کرده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/681414" target="_blank">📅 15:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681411">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRVzZrXkuAXW3-SS5RDnDBvm9MUCTnKVPhzeD4thJ7VenMvAVWtLXQoyBQoVqfg2ohX5eMJuCQUwhb3ffNUHB7g8w1TpyGjkH5J9v7kGTnCPbEjuLOhuvt1r08PsdpbTaTgHL1hEFkUXtYRO9yA2uFTcIxdNXEMlbNWibgWWG5DSbmLTxHlgAyZ6NoItRbPtwtgAgJ2xGtJCW7jIBmexeCaXQX4aGir2tkmXWdUexdupKjkVSawXFn-4KKxZ-fUmJtau-EPcXsIkUcXtgQiQZq90nmR2kjX3EfHKM13hw4iwM_9dgPwb_VyQc82qhkwT5QzcTUeGSZLjgz6lGTsD5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j9lxh9l_W1q1Oqee3C141VQbN3USv0EOm_-ua2Uz7tnyXjcYKYO3vizJDcrLS0fTe2I4qswjh_K7kbwo0D8qC_hmXubIDZnJK-64zv-TS8byyeoR0Ja1gbRggs7msravCf9Tr9N0oduX1y6roIBICUfwx-A-VTAj2RETbNMjcRBcsFSOBGHQM4HU9abpOqv-2JNh89aW2VagjALOVUCjK3c4UIpdVrg0aGjCwJb6mqENknMjh4GFc6N0rID5Kl9fkph1XbXNvfE60CmvDmYlg8fmMT-qMW5kCDtV9YK5osbFczbbqvaT47ICp_z1tLfSlOetv_fvB-7m5KdhDDjvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX2NrY0XaAgVHJy4tsRK7yIUXJMqWzUfyP6qwZ9ZZFjwT5kWfZQGQHHGUznhpb7ueOgK4qty_0sQAPk0XbFfxCsj776Ceun5BbSncIFo7Guqxa3bfa89c2uD_QHsj9fTYZsTq_ilKZjnAQ-mqeBqXWgU7P03cRiAjLx07dK1LT3e6FZ3RcYdG_UxsEzi57YYR5BbLcS5sQudjmzcEzyIL3wOziYeTsPen0GClQYBUlQlQeDHzBH47lGtbygGu0a4TlP-MfVLGmGfs6mBMJ0r1mCl8bUhOGf6wrg2IDkl0NydDfXAFGH7tPB4LVBcfTazi2YmssSiCIMwumYZs81Ddw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
همه باهم برای ایران
🔹
آینده فرزندانمان در گرو صرفه‌جویی امروز ماست. با مدیریت مصرف آب هنگام شستشوی ظروف، حافظ این سرمایه ملی باشیم.
🔸
الوفوری را دنبال کنید
👇
#همه_باهم_برای_ایران
@Alo_fori</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/681411" target="_blank">📅 15:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681410">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
هشدار سازمان سازمان بازرسی به بانک‌ها: وضعیت پرداخت وام‌های ازدواج و فرزندآوری قابل قبول نیست
رئیس سازمان بازرسی کل کشور:
🔹
۶۱۴ هزار متقاضی در صف وام ازدواج و ۵۱۵ هزار متقاضی در صف وام فرزندآوری هستند؛ این وضعیت غیرقابل پذیرش است.
🔹
هرچند مبلغ این تسهیلات شاید بسیار بالا نباشد، اما برای جوانانی که در آغاز زندگی هستند، کمکی حیاتی محسوب می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/681410" target="_blank">📅 15:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681409">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa3785379.mp4?token=hrW4qSo8p_BdJvHamkTI_zC0IPXWs2fsOzkEMu_IR6no6458U4ESiph-ZFe6fI_o0gbOL2GpRJ4qoEXLoPXHje3pq7-OJneSR9iu3eCZs_1p_wrMeX0SrCsFLg__T-BDuWrzfSjNKyyHKpEnQd7C4r6wnVdmQhPAnX2ExYIbBE_nF_me_LJkKY5PyOvkcKOMFwuptuvmrllN99KWRYGYZBjJajhjP4_HR_sEF55KewOT2SA2YJuqAv9FbhnviEV3hd0KSwKA7lCUTHGdxkcxQ26OFIcoco0eNz3cgJy4SKqk20dpeE8lP3t7fIGcEKqoVAhc8umozhoK3mbWI4h6yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa3785379.mp4?token=hrW4qSo8p_BdJvHamkTI_zC0IPXWs2fsOzkEMu_IR6no6458U4ESiph-ZFe6fI_o0gbOL2GpRJ4qoEXLoPXHje3pq7-OJneSR9iu3eCZs_1p_wrMeX0SrCsFLg__T-BDuWrzfSjNKyyHKpEnQd7C4r6wnVdmQhPAnX2ExYIbBE_nF_me_LJkKY5PyOvkcKOMFwuptuvmrllN99KWRYGYZBjJajhjP4_HR_sEF55KewOT2SA2YJuqAv9FbhnviEV3hd0KSwKA7lCUTHGdxkcxQ26OFIcoco0eNz3cgJy4SKqk20dpeE8lP3t7fIGcEKqoVAhc8umozhoK3mbWI4h6yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قابی دیدنی از مادر و جوجه‌های جغد خاکستری بزرگ؛ بلندترین پرندگان شب در نیمکره شمالی
🦉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/681409" target="_blank">📅 15:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681408">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMwrEJnSS_DNsJFk9WkqldWGSkIqdTcDNznMOVIpygkYHPUhLKIK-1xJ_hJTYMxU9K5M8FvOQOMH0Y0RO8A7wSSK6Q3_CmVCXHRLYdR_DgrwWW49idWq1FQnZuRxzx-BleUSsth5_sfd9VuFYLW5Q6wgLnMm_W8OCKEOo11RONDW9kvNm6QRh8SCkDQT3oS0ozetZN5vxcdMicaIIqNddO6W_RGsSuuawCJ4xwv3V8WL9dovuSVN5TLcrf74z8H1VYxKYH2aCE2At7C7DEAoiLPbDcN6M00ew-W2T7i0G1zYtiy3dJMr4i11hMpUOr_8RCb4ISQYgOWSSXx3e1Vs7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران»/۸
🔹
ثبت رکورد ۷۲۶ همت تامین مالی در سه سال توسط بانک کشاورزی
🔻
حجم تسهیلات پرداختی بانک کشاورزی با شیبی صعودی از ۱۸۸ هزار میلیارد تومان در سال ۱۴۰۱  به ۲۷۷ هزار میلیارد تومان در سال ۱۴۰۴ افزایش یافته به طوری که از سال ۱۴۰۲ تا ۱۴۰۴ با رشد متوسط سالانه ۳۰ همت، جمعا ۷۲۶ همت تسهیلات پرداخت شده است.
🔻
رشد مبلغ تسهیلات پرداختی هم زمان با رشد تعداد تسهیلات، موجب شده تا متوسط مبلغ هر فقره تسهیلات نیز به طور میانگین سالانه ۳۵ درصد رشد کند.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681408" target="_blank">📅 15:26 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681407">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ساحل شیب‌دراز قشم از آلودگی نفتی پاکسازی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/681407" target="_blank">📅 15:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681406">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مشاور سازمان سنجش: به همراه داشتن موبایل یا سایر دستگا‌ه‌های حافظه‌دار حتی اگر خاموش باشد منجر به محرومیت از آزمون می‌شود/ تخلفِ سازمان‌یافته تا ۱۰ سال محرومیت به همراه دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/681406" target="_blank">📅 15:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681405">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuBb1rB4lU0GF6VReKSnEO99JffTC9LIFg4l3PG7EyX17jbWFmUXsCUEs2bgHGjsbgnhvjMk4UbpUAy1I88LLabQT0dOunno68NMpA09MAXw-8QTi9NF11RERO9Pg9pGNKvNl4eCw5FEa6JU-Xa_JdbFLrCCDq514yKyq7kXSIkmfo6xW4YwItkQRQ_8QjtUHCOmVZhR57dmmUbuVhUh2sF4MwYQv0w_253W06FUCWG1nD_O4qexLE6AHBZljHB_CbEieA6iuo4Q3f3B_S_iiQV79J3LnLTpi94hu16wBPMakD1SuqknrCTy0SUpmA2f8btnfy7Ozhrpc7G524iB8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون هماهنگ‌کننده نیروی هوایی ارتش: چهار خلبان پایگاه شهید دوران، مأموریت بمباران پایگاه العدید را انجام دادند، اما سرنوشت سه خلبان هنوز در ابهام است
🔹
تاکنون به جز تحویل پیکر مطهر شهید مجید کاظمی، خبر دقیق دیگری درباره سرنوشت سه خلبان حاضر در این عملیات…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/681405" target="_blank">📅 14:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681404">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سازمان لیگ: استقلال باید میزبان دربی را اعلام کند
🔹
درباره اعلام مشهد، تبریز و یا اصفهان به عنوان گزینه‌های سازمان لیگ برای برگزاری دربی پایتخت که در هفته پنجم انجام می‌شود، باشگاه استقلال تصمیم‌گیرنده است و باید هرچه سریع‌تر گزینه خود را به ما معرفی کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681404" target="_blank">📅 14:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681403">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
موشکباران مواضع مزدوران عربستان در استان لحج یمن
🔹
نیروهای مسلح یمن، مواضع و تجمعات شبه نظامیان طرفدار عربستان سعودی در استان لحج یمن را هدف قرار  دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/681403" target="_blank">📅 14:46 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681402">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c91565062.mp4?token=aISubj6YBbbU-R75xoFXnhnLPQeD6PbmnfHDopiZHsld3TDE_uck51QYd-88YXVJWOgJRC_0Sy7FcMELBUJMEkdtqjdiogQb7sOyMh7iDcxbovFqBxOcqrDG3z4dnNPp3_GSCJL4sjzBjZywWSZjo88qoZ7Xyfc8aXziVDDbUH6LIRwIQ-4071vKpOyNLMXZyfceYnSSf6iu7kkfsWLMAZ6v9weE47Ha8n63ADOhsnUfMITo7EpKKWO4AGrgeaEBox9e3JB4HJ4zwcPvFmxCD9VTxWyA_dLiQ9GJY9yhmbiTTAt3OGfPgMwJ7t7KMizkUu2DH-GEpgkyuq-KdqPvfhz5J4YrZAsIoHxWi8arnOehPbdo1MIyf0aa5kbk5GI9gb7J6th9Nv8Lmbd040Z9tziLZz0Jo4xiYnEignHssTFxmJWNrs5BpDntldHLm-xknG4T1YAbH7yuknPwKK1yw2CxBIrUSkrekc-HEpvZDxY8cuhMmChEBNM5zuxbqe6xdLtUqdJxOS5FBDlpoM_11iVMvv8TwFcxisZXjQk238-E1k2qfzUvyBACFSHe715ceE8suJEWyGTnrkdjQ9vawTNJ-fqCMhXcjCRcrkZlU9Nc-CM14WZIguQxkReFaDNxp8edWA-2Zu1NNwoJK6tvoZNBWpcQxI5NIHokgVmRcVc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c91565062.mp4?token=aISubj6YBbbU-R75xoFXnhnLPQeD6PbmnfHDopiZHsld3TDE_uck51QYd-88YXVJWOgJRC_0Sy7FcMELBUJMEkdtqjdiogQb7sOyMh7iDcxbovFqBxOcqrDG3z4dnNPp3_GSCJL4sjzBjZywWSZjo88qoZ7Xyfc8aXziVDDbUH6LIRwIQ-4071vKpOyNLMXZyfceYnSSf6iu7kkfsWLMAZ6v9weE47Ha8n63ADOhsnUfMITo7EpKKWO4AGrgeaEBox9e3JB4HJ4zwcPvFmxCD9VTxWyA_dLiQ9GJY9yhmbiTTAt3OGfPgMwJ7t7KMizkUu2DH-GEpgkyuq-KdqPvfhz5J4YrZAsIoHxWi8arnOehPbdo1MIyf0aa5kbk5GI9gb7J6th9Nv8Lmbd040Z9tziLZz0Jo4xiYnEignHssTFxmJWNrs5BpDntldHLm-xknG4T1YAbH7yuknPwKK1yw2CxBIrUSkrekc-HEpvZDxY8cuhMmChEBNM5zuxbqe6xdLtUqdJxOS5FBDlpoM_11iVMvv8TwFcxisZXjQk238-E1k2qfzUvyBACFSHe715ceE8suJEWyGTnrkdjQ9vawTNJ-fqCMhXcjCRcrkZlU9Nc-CM14WZIguQxkReFaDNxp8edWA-2Zu1NNwoJK6tvoZNBWpcQxI5NIHokgVmRcVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنگ کیسه صفرا؛ مهمان خاموشی که می‌تواند بدن را به دردسر بیندازد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/681402" target="_blank">📅 14:42 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681401">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تیزر قسمت سی‌ویکم از فصل پنجم
🔹
در این قسمت تجربه‌ نزدیک به مرگ آقای سیدهادی سجادی که در اثر تصادف شدید، هنگام جدایی روح از جسم، شیطان برای انکار خداوند توسط روح تلاش می‌کند و روح حسرت اینکه چرا در دنیا به دانسته‌های دینی عمل نکرده را می‌خورد و شاهد قطعه قطعه شدن آسمان و نفرین شدن توسط فرشتگان در هنگام دروغ گفتن به مادر شده و ۳ سیلی به خاطر ۳ دسته از گناهان به ایشان زده می‌شود و گرسنگی طاقت فرسایی که توسط تکه کوچکی از نان و پنیر دختر ۳ ساله از بین رفته و با شنا کردن در رودخانه و گفتن اذان فرصت دوباره زندگی به ایشان داده می‌شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: سیدهادی سجادی بلالمی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/681401" target="_blank">📅 14:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681400">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
امارات: یک کشتی ما هنگام عبور از تنگۀ هرمز هدف قرار گرفت
🔹
منابع خبری اماراتی به نقل از شرکت ادنوک این کشور، از هدف قرار گرفتن یک کشتی در تنگۀ هرمز خبر دادند.
🔹
سازمان عملیات دریایی انگلیس روز جمعه از دریافت گزارش‌هایی دربارۀ حادثۀ امنیتی برای یک نفتکش در…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/681400" target="_blank">📅 14:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681399">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون بنادر هرمزگان: بخش عمده آلودگی نفتی سواحل قشم مهار شد.
🔹
پلیس‌راه مازندران: مسیر جنوب به شمال کندوان مسدود شد
🔹
بلومبرگ: ترامپ فعلاً گزینه نظامی علیه کوبا را کنار گذاشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681399" target="_blank">📅 14:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681398">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrQQ46OwJ-_OuqdLp13P3eQUXP2TNgjESoDr2ukZEYHPchUpTAPdu7TRK-GKjwoyonUlA4UwkpG8TuZRmRXDelzbvI-7Y0SLkE_PM7kMx0y05i3wMt3cr-85VQY3aUVRvPRV5r5wra2IEmhIEvTAL1jkLCBHcOTB8kl-EwwpKy9gDHM17PjGg62u4huQg1_RRPLRWVFFKWLZPSCkozTL7qE4F6OcNADATqwCW0GMFOBqVo5oqzAor5B3kquef-ZPAj4JfT2JNCw8VclaYVLihUtBv-A68eR1MwjOkCI1MA9Dsgzh1vbjcNwZ8vNJn11Pav4S-IkxGkpeGWthTi2IUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش بیش از ۸۴ درصدی عبور کشتی‌ها از تنگه هرمز
🔸
پیش از آغاز جنگ رمضان، روزانه حدود ۱۳۰ کشتی از تنگه هرمز عبور می‌کردند که این رقم پس از جنگ به حدود ۲۰ کشتی در روز کاهش یافته است.
🔸
از آغاز جنگ تاکنون، حدود ۴۰ درصد از کل عبور کشتی‌ها از مسیر تحت کنترل ایران انجام شده است.
@amarfact</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681398" target="_blank">📅 14:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681396">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXRmKFdvr7m7G8db6gWlgyuSZs_X07eRUu9J429IPDU24cxnbmT-_MHf1q-i1sp-uHn1Sj3WeizknFo9LV8Ke3zeoJh4XluDp6XnxJKRK7xBhvnCxoEeZXdqDwcV12yrzasOb0wRzshLp0b3G7cs2L2F2ndjzwhD3XncDxv0R32yqlOBJPcmLE38NhWFPKeBPidf4FNIUktMzen7jCUF0vQHATIa3EVyeD8CsTxRQ14M2l7k6gDHq7nlTSSOFD0yFw3w0nkQjv4EIQgdPeTtvBKhku8vIZRagZBTySmZkF0g2GS48_MwkvkRS4MH5LRaKR4BSKH_zeW2s0zQqUSxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ متوهم مدعی شد: به زودی تنگه هرمز را قلمرو آمریکا اعلام خواهم کرد! #Devil
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/681396" target="_blank">📅 14:23 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681395">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730d812ca9.mp4?token=NtLEq3twk29qMaFsR4ciEWmxKBdrKQfzmjXQR-fZpCdrCowt8VRiPQ53rHkZlJzVZ0fwzgwNpB1QB6dy2x-kx4x1b-36HaI3hHm23pVW-1OWL6S0GtAcht6DrJ9TDEafvljGtUiKOHXDwGJlPA38qWH9AZfOW2FHqRrMSi9eSGyKTq4iateHlGCLyIt67PHJ04Xx-Z8VUOtpt1ljmDvHIAyCRMcC4uzHNYb8Pw8hVE6lZ159nNCUL6_zPVPTgzlLumrjI_CKlfzMOqRu8wa8AYyTc66qdwO9axt78ZOkybnq5-0fv2HB6Uvtfel4ZmIkZdR6YMidCGyJuVQbUVXRohV2UA4Iw6lKCTMoClNbpGCG3bln7omAKUa1cQROlntCvhD7Y8ZSXzUBTPQKLQha1azcwo2XqqgMRd_APMWaK55ePMXM-KRqMMfmY9jQ3ql8B7BGs5L4Mc1g8kRwF-Rilfx2DBrKbrDdn16HfK0g289uGWjOGSGITcjzKi9tuAeVShbYU2tSYM6D8knRTbE4MmyNTaVmglDQH87Hp_PoHp4d5LXeEO8ZJY7ifWaIUPDc3YCGhw4t5BceBgfaH1FwF_qufPRv5VA2p_ydb0GhQtz6lDXs6KEtaCq7PXWVQgyinAZY64NVDYnr2bv1pxycBhOljueEz9n4RaOjLydwidk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730d812ca9.mp4?token=NtLEq3twk29qMaFsR4ciEWmxKBdrKQfzmjXQR-fZpCdrCowt8VRiPQ53rHkZlJzVZ0fwzgwNpB1QB6dy2x-kx4x1b-36HaI3hHm23pVW-1OWL6S0GtAcht6DrJ9TDEafvljGtUiKOHXDwGJlPA38qWH9AZfOW2FHqRrMSi9eSGyKTq4iateHlGCLyIt67PHJ04Xx-Z8VUOtpt1ljmDvHIAyCRMcC4uzHNYb8Pw8hVE6lZ159nNCUL6_zPVPTgzlLumrjI_CKlfzMOqRu8wa8AYyTc66qdwO9axt78ZOkybnq5-0fv2HB6Uvtfel4ZmIkZdR6YMidCGyJuVQbUVXRohV2UA4Iw6lKCTMoClNbpGCG3bln7omAKUa1cQROlntCvhD7Y8ZSXzUBTPQKLQha1azcwo2XqqgMRd_APMWaK55ePMXM-KRqMMfmY9jQ3ql8B7BGs5L4Mc1g8kRwF-Rilfx2DBrKbrDdn16HfK0g289uGWjOGSGITcjzKi9tuAeVShbYU2tSYM6D8knRTbE4MmyNTaVmglDQH87Hp_PoHp4d5LXeEO8ZJY7ifWaIUPDc3YCGhw4t5BceBgfaH1FwF_qufPRv5VA2p_ydb0GhQtz6lDXs6KEtaCq7PXWVQgyinAZY64NVDYnr2bv1pxycBhOljueEz9n4RaOjLydwidk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویری تازه از جواد عزتی؛ این بار با روایت هوش مصنوعی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681395" target="_blank">📅 14:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681394">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پلیس خبر داد: دستگیری دو زن در پرونده سرقت مسلحانه شهرک غرب
پلیس تهران:
🔹
دو خواهر برای ملاقات با دوست هم‌باشگاهی خود به شهرک غرب مراجعه کردند که ناگهان زنی نقاب‌دار با تهدید سلاح، طلاجات و دو دستگاه آیفون آنان را سرقت کرد.
🔹
دوست شاکیان با سارق هماهنگ بوده و انگیزه خود را انتقام‌گیری شخصی عنوان کرده است.
🔹
هر دو متهم برای سیر مراحل قانونی به مرجع قضایی معرفی شدند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/681394" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681393">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLIgqx2pDN0TzxITp1fIIdzvVs5BrJWHGlfHVCGo24n-OkT18vNzK_V8SHm4jChOb9qZ_QCUo39ng6E14VVf_K9QRmlbDeIzuvkp2vTWkOemFZBnupaZKlUQ-7gPRPF6-0a7QAlci5rm3M7QCln4sdBFywCTZN0bdD8dqZYp5yKpQsq6JrlnBVGgl1zP1Qz0WY_lYG6xSvQbx6mGzpgU9HXh86d3OJ5WalC8E9f-ZzFsMB2s8-uBxKuNDsyTUNghFOw5q0yYQ_zCz_7LKg6tpuutmszZpufCZZTOvDp09h2fklESJWI2lCxbDx2D7aJqZ5jL20-Lrh6aFXlqXdn7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در لهستان: جنگ چهل روزه رمضان، افسانه شکست ناپذیری و غیرقابل دسترس بودن تجهیزات نظامی پیشرفته آمریکا را در هم شکست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/681393" target="_blank">📅 14:15 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681392">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5332f54efc.mp4?token=TvBkI-R1ZDoEacfT8sFRvG7UJsqTXBvgDfNjGz6GGQx1mO042XilKOszMeHsGfxiChZ3LHbMFkAnbe3CC0YrmAG8-CJDqt45LbPKRM15k4SidVAPpYujtAhyvtT4hSPp63GWLBcLp3uJDK4tUpRvKqV88xeZ2el7t-eWO-bk5mglLhv1FGGC4wn0VNZPhdFU6zcgxPI-Exs3LsZkWH6qShvmhbRwtFv8T1Vwbdksz9drahhU1BZYOSnJRFnrkXV1jR_MyZ7muNHAdeNg49D1qagbWttgHSf5-avOPgs2gHKP3z6WHGvgsaGMPCY7uG55IWC9a6Oex6R2hn3pFLP9Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5332f54efc.mp4?token=TvBkI-R1ZDoEacfT8sFRvG7UJsqTXBvgDfNjGz6GGQx1mO042XilKOszMeHsGfxiChZ3LHbMFkAnbe3CC0YrmAG8-CJDqt45LbPKRM15k4SidVAPpYujtAhyvtT4hSPp63GWLBcLp3uJDK4tUpRvKqV88xeZ2el7t-eWO-bk5mglLhv1FGGC4wn0VNZPhdFU6zcgxPI-Exs3LsZkWH6qShvmhbRwtFv8T1Vwbdksz9drahhU1BZYOSnJRFnrkXV1jR_MyZ7muNHAdeNg49D1qagbWttgHSf5-avOPgs2gHKP3z6WHGvgsaGMPCY7uG55IWC9a6Oex6R2hn3pFLP9Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر کتونی مناسب چه مدل شلواریه؟ #فوری_استایل
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/681392" target="_blank">📅 14:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681391">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
جزئیات استخدام نیرو‌های شرکتی اعلام شد/ قرارداد مستقیم فعلاً منتفی است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/681391" target="_blank">📅 14:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681390">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB2iCsRFDbzgOcqDdAyJ23eWQknYVF9APkZv7nsaigVRXhWgYL7IPORXE_-83Rc0wfiAEA0FdnIn9yNigVbqphklGGm5K5NIXpcZweMHdYP1hjhFTVH2sszxiYcEjATj5bf-jRozKa1SALsxbVwKxQ1EHBInReYoAsOwV1R8WR8ZLlXC3eMq9jGFYxzogLBCX_7XBQtcDjG688IYJYexpMhI30souRE4eHeOaXzBzMQDtrFe6yAZFJl3nm2ICt3nuVMRGXUd91RLw3TDbOuyIkzmtkGv8fKVNi0a1IMEwEybo6oZov1YInk2EXPt6avC5J1gumx3856Nvfcuqcw0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روح‌الله حجازی: سطح هوشیاری رابعه مدنی ارتقا پیدا کرده
🔹
حجازی کارگردان سینما درباره عیادتش از رابعه مدنی، بازیگر سینما و تئاتر که به تازگی از بیمارستان مرخص شده، گفت: سطح هوشیاری ایشان  به‌مراتب ارتقا پیدا کرده و خوشبختانه حال خانم مدنی نسبت به قبل بهتر…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681390" target="_blank">📅 14:05 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681389">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
کارت ورود به جلسه کنکور سراسری ۱۴۰۵ از ۲۶ مرداد توزیع می‌شود
🔹
کارت‌های شرکت در آزمون کنکور سراسری ۱۴۰۵ به همراه راهنمای شرکت در آزمون از روز دوشنبه ۲۶ مرداد تا روز چهار‌شنبه ۲۸ مرداد از طریق سایت سنجش آموزش کشور منتشر می‌شود.
🔹
آزمون اختصاصی گروه آزمایشی علوم تجربی صبح روز پنجشنبه و گروه‌های آزمایشی هنر و زبان‌های خارجی بعدازظهر روز پنجشنبه ۲۹ مرداد و آزمون گروه‌های آزمایشی علوم ریاضی و فنی و علوم انسانی صبح روز جمعه ۳۰ مرداد ماه در ۴۱۵ شهرستان سراسر کشور برگزار خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681389" target="_blank">📅 13:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cc-98bf4GdUEg9kxIlxEttlDbdf7TcStk2l_vIEWItpUNyZyicwAOy9lIDUCzc8uXQAysGBYSYpcnQlP8ud3h3PeWSUXbhOrNjurc6u1fzQRVCq1TnyuC7DrWXYS4SvpjatqqyMCBCtr7Ihjs8ov2I4mQoClik--I2MVnTB9I20ZeADSAOTp77rrBSQCpfHHG4qB7SwUqGEyH2oxQCxrCt--OfXoWMgVEIh47RMorrFNQrSNAenmtvOdyLAE_SKv4lfbFIVVJJeB61kBqSr7T-yI5jeyhcrp_HB4vmxxPjaRJRu8c0mPtlDSuDo7oUO3MCi-AEI8CCrVS5CjhKiFMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از رهبر عزیز انقلاب اسلامی
در جبهه‌های جنگ در سنین نوجوانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681388" target="_blank">📅 13:50 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
موشکباران مواضع مزدوران عربستان در استان لحج یمن
🔹
نیروهای مسلح یمن، مواضع و تجمعات شبه نظامیان طرفدار عربستان سعودی در استان لحج یمن را هدف قرار  دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681387" target="_blank">📅 13:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یک تروریست تکفیری در الانبار عراق دستگیر شد.
🔹
نخست وزیر لبنان: حملات اسرائیل، ثبات در جنوب لبنان را تضعیف می‌کند.
🔹
کره جنوبی خواستار پایان رسمی جنگ با کره شمالی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/681386" target="_blank">📅 13:44 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681385">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
آتش‌سوزی گسترده در اسپانیا به نزدیکی خانه‌ها رسید
🔹
آتش‌سوزی گسترده در اسپانیا به‌سرعت در حال گسترش است و شعله‌های آن به مناطق مسکونی نزدیک شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/681385" target="_blank">📅 13:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3185ce41e.mp4?token=XAVG5lu_eGIeok3N6uSRm-IQsIecZRnNXRoYbNxEjvrMOpm2wqYtQT6Lmf3Y6Dn3l_vMvo0SBZiHLuxEOvyi7LnIkrVXeUEBluZJ1dKackB-fIxmHsepPlgSNWArw0wRnCl3i0KnEZSRILuxILni3ebXUB2SSishDcSfTtS29Xs3HTOtrMSqz0qJEsLh8yBqt1NXsugDUlS4Q6S5xXhYGCZVfDOUiUh-vO1uZvvNX8p7BqiU13QUP9CzC7ohEWgokDLLsYBzhju8fpr8UEFQZGaTbB5bbNCXHjACjc8R_ktOBICDCLP11LOe_ysgf7txIZlHq_PBOxj60YkN0UdhEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3185ce41e.mp4?token=XAVG5lu_eGIeok3N6uSRm-IQsIecZRnNXRoYbNxEjvrMOpm2wqYtQT6Lmf3Y6Dn3l_vMvo0SBZiHLuxEOvyi7LnIkrVXeUEBluZJ1dKackB-fIxmHsepPlgSNWArw0wRnCl3i0KnEZSRILuxILni3ebXUB2SSishDcSfTtS29Xs3HTOtrMSqz0qJEsLh8yBqt1NXsugDUlS4Q6S5xXhYGCZVfDOUiUh-vO1uZvvNX8p7BqiU13QUP9CzC7ohEWgokDLLsYBzhju8fpr8UEFQZGaTbB5bbNCXHjACjc8R_ktOBICDCLP11LOe_ysgf7txIZlHq_PBOxj60YkN0UdhEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه آزمایش اجتماعی که نشون میده ما مردم ایران از کارکردهای مثبت بازنشر در شبکه‌های اجتماعی غافل هستیم...
@Tv_Fori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681384" target="_blank">📅 13:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681382">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36015263c5.mp4?token=VtLGV8sbHIIVubeDmkw782hqOQmwWr6NAcnXr4acaMp8zzvV_YWoFelR7J1YcHenMuzRU3AIKwpb4znhRahQ5BunzaRo7_1UgrwVYdGmovl63MdeiCYIlmXV2iDoUlqbv9E0IzYLd9lQS9h-EsT9Yu4fVi8N5KT3mKFGdJoaddkiBjBycM7AAPE8mUbXKJXTRugUIWEhRfpzWAD6Hyo11ot9ZWl1QYRP3GnHilH-9gpdW-TqL0NR1tmfQO1zbxGUB90tooZBneb8iqD377Wb1ENPjDjvdTBugdc0IBxvbuZi8YC56aFS84hgQcub-KtxHDwRIpYOjTBZaaCvx8n58w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36015263c5.mp4?token=VtLGV8sbHIIVubeDmkw782hqOQmwWr6NAcnXr4acaMp8zzvV_YWoFelR7J1YcHenMuzRU3AIKwpb4znhRahQ5BunzaRo7_1UgrwVYdGmovl63MdeiCYIlmXV2iDoUlqbv9E0IzYLd9lQS9h-EsT9Yu4fVi8N5KT3mKFGdJoaddkiBjBycM7AAPE8mUbXKJXTRugUIWEhRfpzWAD6Hyo11ot9ZWl1QYRP3GnHilH-9gpdW-TqL0NR1tmfQO1zbxGUB90tooZBneb8iqD377Wb1ENPjDjvdTBugdc0IBxvbuZi8YC56aFS84hgQcub-KtxHDwRIpYOjTBZaaCvx8n58w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باران مرگبار در ژاپن
🔹
باران شدید در استان چیبا ضمن گرفتن جان حداقل ۸ ژاپنی، سبب آبگرفتگی جاده‌ها و قطع برق گسترده شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/681382" target="_blank">📅 13:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681381">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06827928b3.mp4?token=kv4Kp1Ea_dfn4JwSO70O1pLaGpPi7WUXvXhSJxtO2_HSnpnvB7lfQpEljuUWlJja5yiU1Aw_USLW-_sAFCf16uTY6Zq_WumnNWGxadBMhWac_nTxbWdx8HT2da-bbJc8xrl7bCjHgLZjZxSMZ5dY82h3cFGiS3ghC-LyTgbs3L9svJAtaEv0dvkVPteiYwbHpE1UGG173rY9jgPXCJ3hinuEsYI1QUCX7fIt3WGPlnWsh9Kwm3_sX9XXmO2Ad34FNTzjHZDafTvbU35RzKUy0Kb6UHps47U_28VqlspDJfKx_KPkr_X-UzIYkEj1YEUE1VAbkiWE03jepwawMJJpJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06827928b3.mp4?token=kv4Kp1Ea_dfn4JwSO70O1pLaGpPi7WUXvXhSJxtO2_HSnpnvB7lfQpEljuUWlJja5yiU1Aw_USLW-_sAFCf16uTY6Zq_WumnNWGxadBMhWac_nTxbWdx8HT2da-bbJc8xrl7bCjHgLZjZxSMZ5dY82h3cFGiS3ghC-LyTgbs3L9svJAtaEv0dvkVPteiYwbHpE1UGG173rY9jgPXCJ3hinuEsYI1QUCX7fIt3WGPlnWsh9Kwm3_sX9XXmO2Ad34FNTzjHZDafTvbU35RzKUy0Kb6UHps47U_28VqlspDJfKx_KPkr_X-UzIYkEj1YEUE1VAbkiWE03jepwawMJJpJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروپف بامزهٔ یک مرغ مگس‌خوار!
🔹
این پرنده در بیداری فوق‌العاده پرشتاب است، اما هنگام خواب برای صرفه‌جویی در انرژی وارد حالت «تورپور» می‌شود؛ یعنی بدنش به حالت کم‌مصرف می‌رود!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/681381" target="_blank">📅 13:22 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681380">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ثبت‌نام ۵ آزمون علوم پزشکی تا ۲۵ مرداد تمدید شد.
🔹
دو شهید و ۹ زخمی در پی تجاوز صهیونیست‌ها به دیرالزهرانی در جنوب لبنان
🔹
آمار تلفات زلزله شدید اندونزی به ۳۸ تن رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/681380" target="_blank">📅 13:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681379">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رسید جعلی، پول واقعی را از دست فروشنده خارج می‌کند
🔹
رئیس اداره اجتماعی پلیس آگاهی فراجا با هشدار نسبت به کلاهبرداری با استفاده از رسیدهای بانکی جعلی گفت: شهروندان و به‌ویژه فروشندگان کالا نباید صرفاً به تصویر رسید یا پیامک واریز وجه اعتماد کنند و تحویل کالا را تنها پس از اطمینان از واریز قطعی وجه انجام دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/681379" target="_blank">📅 13:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681378">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
رئیس دانشگاه تهران: کسانی که در سطح دانشگاه هنجارشکنی کردند، احضار شدند و شورای انضباطی به پروندهٔ آن‌ها رسیدگی کرد
🔹
به‌طور خاص ۲ نفر را داشتیم که متأسفانه در اقدامی بسیار زشت و هنجارشکن به پرچم مقدس جمهوری اسلامی اهانت کردند؛ با این افراد مدت‌ها پیش برخورد شد و حکم اخراج آن‌ها صادر شد که اکنون در مرحلهٔ تجدیدنظرخواهی هستند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/681378" target="_blank">📅 12:56 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681377">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ercEHOBeGiE9DtOQBMRZG256NEDJxG2vxKJG7OqNn1VHH0OhgqnNItghB-Q4ZGlmLCuD61Onyt1pJz_g5NNNn9seGCyX9jSrzOTQenRdzVZunip2Duk4frmUBSGS6nMXlfVml4ww9trZGcIHXxImdqBh3WN-ZT-_6qQQgz8ojnrcrnA5oDgBgBiKNpvH6ZLLXMIa_rYP6KGYsfDFiV-EnU4ZyQMmi0DYiu9qqdr93ELO6H3RH2jmm6xu1F_TAeEwxFb08XvlT9VpuIAEKC0pEwlQM_S4OA-SuG20n8iyC6oSVSR7lDZF1DNYhWDBJ7aYkxI2bvBqmuo1U6mgXX2BKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فوک‌های خزری یکی پس از دیگری تلف می‌شوند! تلفات به ۲۵ قلاده رسید
محیط زیست مازندران:
🔹
لاشه دو قلاده فوک خزری در سواحل بهشهر (میانکاله) و محمودآباد کشف شد که با احتساب ‌تلفات ثبت شده در سواحل استان از ابتدای سال جاری تاکنون، ۲۵  قلاده فوک تلف شده است.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/681377" target="_blank">📅 12:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681375">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e032fd3c33.mp4?token=p4masViTHgN68_uq6-ikbh7B2VgNrAq13R9HrAktqToMXDE64Y51yNB0JikVNvEnlgNwWimKvXWAD-FUX_ndeDFmqVLx5gjxGRygHJS8Q2y648RJpOhRfy4vcQwz_1ybfex3KPtfquMm-TOZMWTtsvDELJ_gFRVB99h8P0qiuKG-7u3ZaUYGbzrDj0M4yJq1FiB4cqfANzsh4WenGv85PV1yGSkTqNvuRGQbEhsrHv9j12tuwUtEy9vgcEuk5MAzfU9Opby3nnWxpe2lj3QXaF2YWbxnahrIHO-EsKwOEO1MsaTM_U-Y6vP2zPp4WQzr8JthSW5X3894c2rqi46K8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e032fd3c33.mp4?token=p4masViTHgN68_uq6-ikbh7B2VgNrAq13R9HrAktqToMXDE64Y51yNB0JikVNvEnlgNwWimKvXWAD-FUX_ndeDFmqVLx5gjxGRygHJS8Q2y648RJpOhRfy4vcQwz_1ybfex3KPtfquMm-TOZMWTtsvDELJ_gFRVB99h8P0qiuKG-7u3ZaUYGbzrDj0M4yJq1FiB4cqfANzsh4WenGv85PV1yGSkTqNvuRGQbEhsrHv9j12tuwUtEy9vgcEuk5MAzfU9Opby3nnWxpe2lj3QXaF2YWbxnahrIHO-EsKwOEO1MsaTM_U-Y6vP2zPp4WQzr8JthSW5X3894c2rqi46K8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترفند هوشمندانه معلم برای وارد کردن دانش‌آموز خجالتی به جمع
🔹
معلم به دانش‌آموز خجالتی گفت: «اگه کاغذ سفید رو انتخاب کنی، به کل کلاس نمره ۱۰۰ می‌دم!» اما بچه‌ها نمی‌دونستند هر دو کاغذ سفید بودن!
🔹
همین ترفند باعث شد اون پسر بیشتر وارد جمع بشه و بچه‌ها دوستش داشته باشند.
گاهی یک معلم می‌تونه زندگی یک دانش‌آموز رو تغییر بده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681375" target="_blank">📅 12:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681374">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94ecc8f64.mp4?token=Ptv1XfKXKOzOn5LjW0DcUuBmKPdvd24rodIFwVIaOR94EeKDh-t_2p_u-w32u03MdMoJvkQclEQ70nCC0WvuCc22YLWkcclBhydhan4xhCBocXKZjnVVu9JeCDtzX_eDy6Qhq2rVLPCHMori5QGHAl7-pXi0n1naMIutR3aAFzTVR5u0xQ3uGhCLU43Q1BNQITByqDP5q2EC4oTewKuFg18UV1WaC6ZbsDhjYBO-JoA1pW_rXzbg154GM0X9AX3qZAPQYD0-oc1kOYxCvh45I2iDEfZMOeN9WS2u1XH17c42Rc48lGvtUhs04-KpM13PDbyA3Ufuu9s9P91bqtp4gYcdOW1cgV2qgbADSz5H0hOpGKr5USe2dMCmq5WXD4mOiYL_cjiDqECL5Rte8bKal5KhrOjs1IuwAm7f7H1kQxHN5D8l3HBuTsFOAOorWLM2dEQs4H7Lw-uIv0makwgPGFJDHispAjh-3HT39bhjeaWBZA7ZoUwUIPGJOFDOZ-NUvlCGU-FbG0WKhG84APjzGWQHIINfvUZvWhH40_BQng4QVGN79MCfUslQEMDWqi9Y9HcmG6rb7DaJpPfF5QoFfFCIq9ZNdTLNUaKsMyOlD2I7oLDjrovU4csgfSgou7yshULbDWjC8dFfuy6AEA1dYqMTEc76ni9NTtZU9TPZ-AM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94ecc8f64.mp4?token=Ptv1XfKXKOzOn5LjW0DcUuBmKPdvd24rodIFwVIaOR94EeKDh-t_2p_u-w32u03MdMoJvkQclEQ70nCC0WvuCc22YLWkcclBhydhan4xhCBocXKZjnVVu9JeCDtzX_eDy6Qhq2rVLPCHMori5QGHAl7-pXi0n1naMIutR3aAFzTVR5u0xQ3uGhCLU43Q1BNQITByqDP5q2EC4oTewKuFg18UV1WaC6ZbsDhjYBO-JoA1pW_rXzbg154GM0X9AX3qZAPQYD0-oc1kOYxCvh45I2iDEfZMOeN9WS2u1XH17c42Rc48lGvtUhs04-KpM13PDbyA3Ufuu9s9P91bqtp4gYcdOW1cgV2qgbADSz5H0hOpGKr5USe2dMCmq5WXD4mOiYL_cjiDqECL5Rte8bKal5KhrOjs1IuwAm7f7H1kQxHN5D8l3HBuTsFOAOorWLM2dEQs4H7Lw-uIv0makwgPGFJDHispAjh-3HT39bhjeaWBZA7ZoUwUIPGJOFDOZ-NUvlCGU-FbG0WKhG84APjzGWQHIINfvUZvWhH40_BQng4QVGN79MCfUslQEMDWqi9Y9HcmG6rb7DaJpPfF5QoFfFCIq9ZNdTLNUaKsMyOlD2I7oLDjrovU4csgfSgou7yshULbDWjC8dFfuy6AEA1dYqMTEc76ni9NTtZU9TPZ-AM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جزئیات استخدام نیرو‌های شرکتی اعلام شد/ قرارداد مستقیم فعلاً منتفی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681374" target="_blank">📅 12:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681373">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cg_32phAewMklXaeFUZLLrwF5DfqG8EkVc_2bQAd2Nlzlk_0M1aagZtAilM2L8YiDBTTlkWlq0RLMC_jfhx1q4RWnCEY_MKCgXF19UBMfH6-961Wl91RCFdLKiLiJvjcL1rYf1zcTfp6ypO-4DK8oxybK8yVYQ9FkiScpMAqQ-Q1lnU1gq1WyytWTQRxaRhE0FmIoXKvaMwCfsL9XneJM4xdGECTlfX8RLQ9NN6kvY8lP-_BYlJrXpDuDGiB5TFdwaAKMzrL9rFoq662Qs2WOxWJlLuZdcIzoXmxCPspwv6ZY2V7abMVOJKjUzzq7jntwjowWFd-ZC4ThkUT693U0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بورس
| رشد ۱۳۱ واحدی شاخص بورس
🔹
شاخص کل بورس با رشد ۱۳۱ واحدی در پایان معاملات امروز به ۵ میلیون و ۷۳۶ هزار واحد رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681373" target="_blank">📅 12:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681372">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
کپلر: جمعه هیچ محمولهٔ نفتی از تنگهٔ هرمز جابه‌جا نشد
.
🔹
نایب‌رئیس مجلس: ۴۰۰ هزار معلم حقوق ۱۶ تا ۱۸ میلیونی می‌گیرند.
🔹
سخنگوی دولت: جنایت جنگی مدرسه میناب از یاد ایرانیان پاک نمی‌شود.
🔹
از ساعت ۱۲ امروز تردد تمامی وسایل نقلیه از سمت تهران به شمال(جنوب به شمال) در این ۲ محور ممنوع شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/681372" target="_blank">📅 12:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681371">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a639a2889b.mp4?token=voek7Rwg7ZrxYEz6oYe0Xd2UEBRGhnEkcw0aqLCxvQ6sOGguxopVdZWR0zD1-6SevHm2gSdcZReKhrJEjVprjQVI_Stes-jVBXBIbjU5BoeihVNiPLDXYERhIuxGc0TUUSV5wxys0ne2I97k2z43SZBoMsnkX6DDpOOAdMjwpoxEY3sE4xFEOPX9nEOKmRxUeOdWtjOO73D3AAvClNIbOpXYrbaq_cJ5aHxze_ZcWn65g1ZkLhtlWrn1S_mBBLiWFyZp7Xgd4gRr4tJEuAKxq7ESxi6H7vC0fEB1owASNKEKaYf4bfPVNMiOhzUVW1r7poZ1vXJeHHxU-XJbwJ2law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a639a2889b.mp4?token=voek7Rwg7ZrxYEz6oYe0Xd2UEBRGhnEkcw0aqLCxvQ6sOGguxopVdZWR0zD1-6SevHm2gSdcZReKhrJEjVprjQVI_Stes-jVBXBIbjU5BoeihVNiPLDXYERhIuxGc0TUUSV5wxys0ne2I97k2z43SZBoMsnkX6DDpOOAdMjwpoxEY3sE4xFEOPX9nEOKmRxUeOdWtjOO73D3AAvClNIbOpXYrbaq_cJ5aHxze_ZcWn65g1ZkLhtlWrn1S_mBBLiWFyZp7Xgd4gRr4tJEuAKxq7ESxi6H7vC0fEB1owASNKEKaYf4bfPVNMiOhzUVW1r7poZ1vXJeHHxU-XJbwJ2law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر عزت جهان طلبی، قوی شو/ پیام رهبر شهید به روایت رئیس بانک مرکزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/681371" target="_blank">📅 12:33 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLA7bB7MlzIIh1AVrObuitkdoPvrYcFhqgUO9hN54qImboqbnd-XtmErJxoY9ON7sglDgZDNU0VlBGyltYjJ-nq8JaEbRfk0e3r-rqixj57d2_c388QIcEFwJflsU6M8ZLz9TkH0-APKDoMCQnqzLTtn9YW4JtPlMh2OZzbVEfhpUWIusRahkcVuy8pBAD97lNR5GMl9hkw2IRczYvY1detXg6_BUI_BhltBZzH5LGscHbvcBWH56s3D4mOMAa2al7bLhPyHNGb16oBbXUqhnV8s7zaTMt0ANXTgv5d9tMlTMpEO0RjoWpZWgcK1viq0UbVOS2xO32pA5_5hUT-gqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه جدید کارواش خودرو در ۱۴۰۵ / روشویی تا ۶۰۰ هزار تومان رسید
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681369" target="_blank">📅 12:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8eaa4b02.mp4?token=oGrMg8Hx5wAV2mJ0q7uqClznUGfOsIYPKsz2qywiwpvbwEa5DqbLE6d9lfuUvdXtDQBfIRotXXX5wFDVv1Oq6iva1PVgLlK4P1-NnDCKrM6raCUWpwNC-xgwhZewx7VaIYZLEC_jZ_hL4zf-k_Uzi3EslfBihS5Opr9gYxufLA36l7V0FiQm3kgeAcpTk2gzu7Ijqz56ECby8yRB84Dt5V1_BcoQwKw8J5Gq8k9fC0v1UzxhUb5Wlm2NmYNU2eFjdo8eaXBN6X6aZG6iE60HIhY0p-K2t0ceGJDYtWCd2c45jCERxbUUqRfhdIeuofKPXVbt3H5ZaTLp34yzazKDvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8eaa4b02.mp4?token=oGrMg8Hx5wAV2mJ0q7uqClznUGfOsIYPKsz2qywiwpvbwEa5DqbLE6d9lfuUvdXtDQBfIRotXXX5wFDVv1Oq6iva1PVgLlK4P1-NnDCKrM6raCUWpwNC-xgwhZewx7VaIYZLEC_jZ_hL4zf-k_Uzi3EslfBihS5Opr9gYxufLA36l7V0FiQm3kgeAcpTk2gzu7Ijqz56ECby8yRB84Dt5V1_BcoQwKw8J5Gq8k9fC0v1UzxhUb5Wlm2NmYNU2eFjdo8eaXBN6X6aZG6iE60HIhY0p-K2t0ceGJDYtWCd2c45jCERxbUUqRfhdIeuofKPXVbt3H5ZaTLp34yzazKDvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی احساسی از واکنش یک فُکِ مادر به زنده ماندن فرزندش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/681368" target="_blank">📅 12:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
تابستان هم حریف قیمت تخم مرغ نشد
🔹
گزارش‌های میدانی نشان می‌دهد با وجود فصل گرما و کاهش تقاضا برای تخم مرغ، هر شانه تخم‌مرغ در مغازه‌های سطح شهر ۵۹۰ هزار تومان و در وانتی‌های کنار خیابان ۵۰۰ هزار تومان فروخته ‌می‌شود.
🔹
این درحالی‌ست که قیمت تخم مرغ ۲ هفتهٔ پیش تا ۴۵۰ هزار تومان در هر شانه پایین آمده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/681367" target="_blank">📅 12:11 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqWIH6wEfQa26ukm8nFGou8ohUn-82mnCmqqwLzdVNZQnhafbyCD6M6L3fu_Jcnj3SfUcYOe1Xk5zAs3dZuTeCVgZbR0h-TDZo7EvIKcRPaSUYf6VWz4wPldSrviofuAzuIkz6oDLrosh-jF_kbWBBPreyH2r2Iqgf9epjm4T8W-tVKYYwiUCFZRzUck45yfryg_WZXDY1QYdkFaSx09bxp0EX5Eafq7Y0KR5us9EkmT8lzR32_Kz-5GkxPVg2mzLc1xt597BSWMgNXX4y5Wv5WfGglvagUXuIV6UCXpx8t_0ACIX_nk0AhH9GbgIeoIsEFQP8bEynbt80Ddn6UHTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر روز ناسا؛ برساوشی‌های درخشان از سوئد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/681366" target="_blank">📅 12:10 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKn9nTTdVgJD7W1RcwGBVYIDdJJ2G7zZncKQ9oF8oQa4Z0MpHJkIwbWkWHR3C9tPUiQDVS0npYpw1A51ORHR2BF1FCMLKmmF-ePY4fmwex4yK6GkztEvR9ARW7yaR1Sir5j2wqKo5SB9ZCZzSCjkoqMz0ecak1PkbfAzPOoRR-RrIKjUn63ePht4yuQwoV3lMPkm_FcTnqe0E1RgcA1s02nA6vXXpFXC4PllfL4CP_bREkSiqF_aMdrwjN7UuSUdpIYoadmOh8xjnQQLgJk5jPvRseVD4ATNwKWpYq2CbjZhfsBOk2-NyYq6bghTeKY-v86j_601XfXPTehIoA-klg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اثر مسروقه «پیکاسو» کشف شد
🔹
یک چاپ اثر «پیکاسو» که در سال ۲۰۱۸ از یک گالری هنری واقع در ایالات متحده به سرقت رفته بود، حین تمیزکاری یک آپارتمان پیدا شد./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/681365" target="_blank">📅 12:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38e1d5d72d.mp4?token=Ei-wZDTDaMJthJRN1lqlIESDlpMvofE1_g9xhYdAgvDpHGwlhS2AwkAl99p02269kcBicCLczJC2k4X8QVw-BP_xBZUyv7Y3-R-bVBac0MftqpXG1kuBuQ5RGaak8glJOjDrToe_7xsn8fyZXgTfKNu9xtOgK0DcBdMHKUU-iaryBGkfQ6t0eVSGR1XLBte6q-RZxIjCFEr7FWM1t0PyWu0PQNzfqmsjqMFghvhFbxEs2l_sVjwDjSoKIhR66ha9bfXJh_enUhwO7ff48tjYbfZ6dX9kwNBqDK4NnCAXha2hieMej8KTn9iR1KXOC31jASvXEK7yk81T7eccBhLvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38e1d5d72d.mp4?token=Ei-wZDTDaMJthJRN1lqlIESDlpMvofE1_g9xhYdAgvDpHGwlhS2AwkAl99p02269kcBicCLczJC2k4X8QVw-BP_xBZUyv7Y3-R-bVBac0MftqpXG1kuBuQ5RGaak8glJOjDrToe_7xsn8fyZXgTfKNu9xtOgK0DcBdMHKUU-iaryBGkfQ6t0eVSGR1XLBte6q-RZxIjCFEr7FWM1t0PyWu0PQNzfqmsjqMFghvhFbxEs2l_sVjwDjSoKIhR66ha9bfXJh_enUhwO7ff48tjYbfZ6dX9kwNBqDK4NnCAXha2hieMej8KTn9iR1KXOC31jASvXEK7yk81T7eccBhLvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک تکنیک سریع و کارآمد برای کاهش نشخوار فکری #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/681364" target="_blank">📅 12:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681362">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMT_qwycx5s0XSFvch3xy8vcWVKlons7Vqrr6mDW9xY10BwVal_kf_dpKr-TWZwwR6ifGCDXd05tPkRo-_uMOo_dVB9LB2tA0wCnyQK7f7VJo-5gy2lYLO9LPdeXfinOuvd9U-fYIGj6lf6dRfDlhOLBzhOAXdTpcTE3eRhm9S6qrYB0GnT-v7b5awj6_ZmIVo3ZinXbfVSkSY3rn9rIQwbrMS8OzVA5nMrSVKDgI0hkDvEM067M8xslj-bF67rGQiZGOjAtP0-RLsixd5kI3F4JqJJPTIS_pYQomu7QHTXqy3Bvv7ppjXDqncx45WDi8m_0XU53Xyi2xqu--JY5Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ اتحادیه طلا حوالی ۱۹,۲۰۰ تومان معامله میشود
@Titretejarat</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/681362" target="_blank">📅 11:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681359">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c47a7fe1.mp4?token=pBufGs4_3hrXeqoReazsPUnIQ1n2MQhDj9VLbFeHebmMSq31utlwAkZnqXHdmzJvXzF0rLk8ZIloCbYqrRog0BOJ6pVKG5-Vyu0dLhwT-C--mr50YohqsOAevB9apA47-gL588-JrI_Xl38hLpNfYrEgDjBK8kT-MEpWDqYGynvJRFYE_lo3n4xo4NC-fn-Aw29VXDaeGMEdOXxRuD5GCVKGrensj2OasQstfWzerT3oXtf3CZtdf7uhA2TBvP0m18PBr4Q8C0cUKG2-JOXNiYu-mnrhtTsBGvmmvfC6wvByG2OPwqMXMxdUcPEcqXPLmEyIlddlvJ8cx4k_YlKlqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c47a7fe1.mp4?token=pBufGs4_3hrXeqoReazsPUnIQ1n2MQhDj9VLbFeHebmMSq31utlwAkZnqXHdmzJvXzF0rLk8ZIloCbYqrRog0BOJ6pVKG5-Vyu0dLhwT-C--mr50YohqsOAevB9apA47-gL588-JrI_Xl38hLpNfYrEgDjBK8kT-MEpWDqYGynvJRFYE_lo3n4xo4NC-fn-Aw29VXDaeGMEdOXxRuD5GCVKGrensj2OasQstfWzerT3oXtf3CZtdf7uhA2TBvP0m18PBr4Q8C0cUKG2-JOXNiYu-mnrhtTsBGvmmvfC6wvByG2OPwqMXMxdUcPEcqXPLmEyIlddlvJ8cx4k_YlKlqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در ژاپن موزه‌ای از علوم فضایی وجود دارد که به شما اجازه می‌دهد تجربه کنید اگر روی سیارات دیگر بودید، چه حسی داشتید!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/681359" target="_blank">📅 11:51 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681356">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJaXkiUt92Ck4nklearC-5OiaSAQPXyShEw8N2kWVRDWfChEUbZK1Lj9ym7u2xt8pii8JhoR63gsZx2dADAz6fD9u6I-n1W--DneCAb2CTGJVH2ZIHWpm641ThGNGt99PQyn_qI6Ma154Uo3DjfawIm-8eCM0FE7Q23ln2C0GAyEBPKMhnD5ojPp9fkCnJxg9ZX_7BuwDB-5PcExatZ0f0tUvsJ1yo6jCD0TqCJIbYFrikMuGCBV8xHkwim8DlZzeSjbmD5cM6MKUr16bEG6tHazyzrx90ln5iTb4jJjud1rHNuP1vLXRSwPm1NgfV6rhlkVGnuYdal21cUKsZU6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iEblpK9m11qILRQQnIvTucf_xHJhD86fe3rCFJhaLBO5roneIJJGeiLb8zXMPDj_bbzmj3iA1b5bP1-g7c26fEb-0cWOi_wGEY5ft_4XwYZveK-rloxZ7unDIVLL4-Fm8FtLpNFUlIxB6BS3BeUSw7Cz0F7QUJnlz4_dcH195N7yeUuACKn4kqzFRzIMtjXgCrqACu2RQc_NhFFk2p4jjiTPbLZQS4bvCHzpWaVShfaajsRkbUqNFaFIbLZCVsNbSJHFdsaR8gToEYeYiM7XNJqV1ae8cdYCpvoUnMcoiRMBxi5mJwibUAL-GY8rlqaj99bUen5tDhGgMbIlR5LKtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuycZJePUwX4-ZBChZxbq6bn76vJ_6Za7SJcvLXB8MEdGkcRvV4PPUPNMOFrM6Kihb3KYGx8ROcRV1fS3Vu_s1JO3g50rXylcWmlykH7eiUhPpo2egTQsnXtrVW15XSIAddn_RVyqwZiThzGkRY6-GG0Hhj3JEGuCVW_h4Y_zkIj3AVUb42dADXmQYhrym7d4_8UoyKZBDxbr9REGUo53-xWT7hRLV1mtihH_NezrV6eMag8t9GQGYZ9C8pYXFF5YZHoWLk2Tk4Ka2NqMxfhjl8VVb2W40xWfYVsL5JR0IUDNnx_EdmKyusc93HNYzbbIDSW_HN1EozJIhyRs-Kt5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نرخ جدید کارمزد خدمات بانکی الکترونیکی ابلاغ شد
🔹
بانک مرکزی با بازنگری در نرخ کارمزد خدمات الکترونیک، سقف هزینه‌های بانکی را با هدف متناسب‌سازی با بهای تمام‌شده خدمات ابلاغ کرد.
🔹
در این مصوبه، ضمن تعیین نرخ‌های جدید برای تراکنش‌ها و صدور کارت، با رویکردی حمایتی، خدمات بانکی برای مددجویان کمیته امداد و سازمان بهزیستی تا ۱۰۰ درصد رایگان شد.
🔹
هرگونه دریافت وجه مازاد بر این بخشنامه تخلف است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/681356" target="_blank">📅 11:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681352">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ساعت کاری ادارات دولتی از ۱۵ شهریور تغییر می‌کند
سازمان اداری و استخدامی کشور:
🔹
بر اساس اعلام وزارت نیرو تا ۱۵ شهریور امسال ساعت کاری ادارات از ۷ صبح تا ۱۳ بعدازظهر تعیین شده است و بعد از آن در صورت درخواست دستگاه‌ها، تغییر ساعت اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/681352" target="_blank">📅 11:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681350">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
چرا ستادکل نیروهای مسلح و قرارگاه مرکزی خاتم‌الانبیا با هم ادغام شدند؟
روزنامه اعتماد:
🔹
قرارگاه مرکزی خاتم‌الانبیا طی بیش از چهار دهه گذشته، مسئولیت فرماندهی و هماهنگی عملیات مشترک میان نیروهای مسلح را برعهده داشته و ستادکل نیز به عنوان عالی‌ترین نهاد ستادی، مسئولیت سیاست‌گذاری، برنامه‌ریزی و هماهنگی کلان را دنبال کرده است. اکنون قرار گرفتن این دو ظرفیت در یک ساختار واحد می‌تواند نشانه‌ای از تغییر در معماری فرماندهی نیروهای مسلح باشد؛ تغییری که تجربه جنگ‌های اخیر، افزایش سرعت تحولات میدان و پیچیده‌تر شدن شکل تهدیدات، ضرورت آن را بیش از گذشته برجسته کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/681350" target="_blank">📅 11:38 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681349">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dR1o7uRboNoGlnOkdN2HJQDHS6owiScxNBajlYb0MWRZUe85NsOpDOvcvWQ7HHmZwXYCX_d2fK_Wgm3JQBa5I1ilfvwEouObWZNNEUdi4-HmEVMjWU_CCAb6jRrIERhE8db27ipocDfBXZGgiwkkaMpIp_2Hxk-I4NGzHRrQ7is_ze_LOY_BcQJcbdLJJpiKGWU29ayx4rCvyCPDTOdIeMxa2UL2tXHDWydaYZAW3HpLEPVtMMQp2c7usxG-HCCZZWZAJHkMb3N3OGWUV42qmMdjwr7x6fr-ylYB7dP5x1WEQqQAmqdqI0b_QFaZlMk8nL8m3f4a63G0YBHGGMQhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
همراهان گرامی؛ اگر با کمترین بودجه کسب‌وکاری در منزل راه‌اندازی کرده‌اید، روایتگر مسیر خود باشید.
🔸
عکس کسب‌وکارتان را برای ما ارسال کنید و در چند خط، تجربه شروع و نتیجه‌اش را برایمان بنویسید.
🔸
روایت شما می‌تواند چراغ راه کسانی باشد که می‌خواهند از صفر شروع کنند
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/681349" target="_blank">📅 11:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آغاز فعالیت مرکز درخواست ویزای ژاپن در تهران
🔹
سفارت ژاپن در تهران اعلام کرد مرکز درخواست روادید ژاپن (JVAC) با مدیریت VFS Global از یکشنبه ۱۶ آگوست ۲۰۲۶ فعالیت خود را آغاز می‌کند.
🔹
از این تاریخ، درخواست‌های عادی و دریافت گذرنامه عمدتاً از طریق این مرکز انجام خواهد شد. برای مراجعه نیازی به تعیین وقت قبلی نیست و متقاضیان می‌توانند با مدارک کامل، در ساعات پذیرش مراجعه کنند.
🔹
آدرس:
تهران، میدان هروی، خیابان موسوی (گلستان ۵)، هروی سنتر، طبقه پنجم
🔹
مسئول JVAC دریافت و بررسی اولیه مدارک، ارسال پرونده به سفارت، دریافت هزینه ویزا و بازگرداندن گذرنامه است؛ اما
تصمیم نهایی درباره صدور یا عدم صدور ویزا همچنان بر عهده سفارت ژاپن خواهد بود.
🔹
سفارت همچنین هشدار داده است استفاده از خدمات JVAC یا پرداخت هزینه آن، هیچ تضمینی برای صدور ویزا یا تسریع روند بررسی ایجاد نمی‌کند و متقاضیان نباید به افراد یا واسطه‌هایی که وعده تضمین یا تسهیل صدور ویزا می‌دهند، اعتماد کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681347" target="_blank">📅 11:34 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681344">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
دعوت طالبان از آمریکا برای بازگشت به افغانستان با پول نه با سلاح
🔹
پنج سال پس از بیرون راندن آمریکا از افغانستان، طالبان از واشنگتن دعوت کرده تا با دیپلمات‌ها و پول نقد، اما بدون نیروی نظامی، به این کشور بازگردد؛ وزیر خارجه افغانستان از آمریکا خواست سفارت خود را بازگشایی و در این کشور سرمایه‌گذاری کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/681344" target="_blank">📅 11:20 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681343">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDjT9f9BM--hnyKdJpUx8jRw0JoOMcaLDM1LpYHjohBV6aF17oF_TwIZEXtY6wrx216h8Dwm9-2OKUwFcl0hKiNj6TzW71lEnUC2-NKxsSn442y14VcPjr1j5-4t1-_RvQ_-PEg_oaq3AIlpmLd2mnocg22mRsRWGLEMv9WumQnmnIQDSgx0AOdwKOk7MFxUVIZ04E0IuTXat7Afl_wdS0peEVCFBFcIAnXaFTtBYnvpBpRSXdi72p0mUUtuiHSeq2ta9DVMKilcwUthFfGHU5LYZKrBc_YOkSqqAmmainNs_kHZKr2UlPm5JbPb1PKHsUhZwNUQoA6kp-wt5VqXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هلیا و ۵ توله‌اش چه خبر؟
🔹
«هلیا»، یوزپلنگ ماده توران، پس از ماه‌ها جابه‌جایی به همراه پنج توله‌اش در محدوده توران و میاندشت، حالا وارد مرحله تازه‌ای شده است؛ آنطور که معاون محیط‌زیست طبیعی و تنوع‌زیستی سازمان حفاظت محیط‌زیست گفته، دو توله از مادر جدا شده و مستقل شده‌اند و هلیا همچنان با سه توله دیگر در این محدوده در رفت‌وآمد است./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/681343" target="_blank">📅 11:19 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681342">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61f8e5d284.mp4?token=AGi3GOVzLVS2mog3YeNXw9SdxbGw1kowl6PndabEEuXXF2q0jUFFWMe6IWv4m_KRryfdV0HXpG-Z_9QICFUS2gC_OeC8LO6geGZW6hCA6efDhnfe6rE2J9EwUvC_skdITVZr6mMm-bF16mUaXNmfy8MzH4PANGE3_z7HaIsGc_4rdNH0yrohMq7m-_MVIj2j6J3qVpPD9-1QPxtYoAVKnKi9bSiN5oohcIedj2kzPYVzs2j3r1i-MCvcF6XlvuZcyAGTcjdqRbffdeA2Vn4TQ1VmtHzLpAOVveNZX4qW4HgZk6b2eJ52POwwapA6lMvbkdHuea1XsT64uikog2qeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61f8e5d284.mp4?token=AGi3GOVzLVS2mog3YeNXw9SdxbGw1kowl6PndabEEuXXF2q0jUFFWMe6IWv4m_KRryfdV0HXpG-Z_9QICFUS2gC_OeC8LO6geGZW6hCA6efDhnfe6rE2J9EwUvC_skdITVZr6mMm-bF16mUaXNmfy8MzH4PANGE3_z7HaIsGc_4rdNH0yrohMq7m-_MVIj2j6J3qVpPD9-1QPxtYoAVKnKi9bSiN5oohcIedj2kzPYVzs2j3r1i-MCvcF6XlvuZcyAGTcjdqRbffdeA2Vn4TQ1VmtHzLpAOVveNZX4qW4HgZk6b2eJ52POwwapA6lMvbkdHuea1XsT64uikog2qeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی یک بوئینگ ۷۴۷ با سرعت ۹۰۰ کیلومتر بر ساعت از کنار هواپیمای شما عبور می‌کند
✈️
🔹
جالب اینکه با وجود سرعت سرسام‌آور هر دو هواپیما، به‌دلیل حرکت نسبی، هواپیمای مقابل از پنجره تقریباً آرام و شناور به نظر می‌رسد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/681342" target="_blank">📅 11:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681341">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سقف انتقال وجه بانکی برای حساب‌های تجاری اعلام شد
🔹
بانک مرکزی در اطلاعیه‌ای سقف برخی تراکنش‌های بانکی را برای دارندگان حساب‌های تجاری اعلام کرد؛ بر این اساس، انتقال وجه حضوری از حساب تجاری بدون ارائه اسناد تا سقف دو میلیارد تومان امکان‌پذیر است و سقف انتقال وجه غیرحضوری و خرید کارتی نیز برای این حساب‌ها تعیین شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/681341" target="_blank">📅 11:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681334">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZcC7uF0OTF6vtuoTouAFgO99jD0ypM27jOZ0zEGxdPjBprkJbuS7JJutvqNGysEDzN1RVMpKKoHt9mxm7JyPH5DTpcpjcWaS4ngYp32eL0DdbLCkzAOur6T3107-G6kmFIUxHZJ4gU-5oT8qgR1PsTbRs8wIdWWaUMmcDRBHvyDk-MOg5WlZiONa3i3urJ0Ute7ZfbN90WaLSsHQQTpk74rZr_J19e_ZN6WO8j7mTd-8glY6Gq8PSkFmRkYiUs67WQxTdPKjqULbwT55yNRS40lEFkQXYPNYs0fwJ6mhjlS_NKyEnD-yfUlahmX9OP2-Eydaj4sntJPphs8_BVwAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f7dVV_KZwsmFZebBt_OsuhBI_Qd_OnL3xGArwUqcbn8O6i6CAcZ2R-czXdbYT5hwIbsLc7fhab2cNazDnAIb_E0TmhMrs9E9-t3m8gbxdWM-MLT3Voi_Jn_8T8vFIPo1hLVbzWOnLcG72Vzec08oGFMjiqPTkJEgazGWUQWTjNz7NBs1yl32idJueq_eu2rH-oxOqTPHfvvSRd2yt0Zl4qsaarTLE7zUp7K13weUj6TfxO1hQYgrOMfw1NHzFJn8HvMMQzuuCvq9EjwM0D7x3HSUo8sZPf3UJ78KusTDqNB9t12tuTCLdV8J_HipzRBvbjWsywkhThulyWP9vjO_ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQIvmZgd-BT-jxU-Jgpbx7NStsnQj5hI2bDAvqM4nXo1nv8OoWgNvaOeeSjWuJK0NAkQT1o0uLv7Mrr_IexDnRTAd9TWFsKsgTFnUqFj9Ks7qCBMhe7GV4WYk1GerqBBf3eOhP5T58j0fWUpMxrjCqBD6kVTEUZB_e-fkcmnhbhaVvPDkhlVat9nzYWYRrwEKiY-oHeAn085NBPajjHoADv-Ibv5iwQjWH58RdtZHrjqahVY4w8UFM5538AO8_bT2EBaCvIncGJ5lKlQ-DDqKQ2BBVJqzF8KRO5ruN7dxAaI5Hx_4JHeLT4tJYg4JQW9XSsfRkxexOhPAqBLXfe6RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GD-w2vzJQW5nXKFOk9NW0wQVLGrbo3HOj6zn99n6jq2EHkjdmeSPN8lqJv4WOFn8qamerzXQLBUD7CNv6Ts4tcCoTm8i8-LmwqwqyMKeJgt8tUZLJ_kaA0dfKGFfHK502tx9AHRwByHAb3VYM-3NRnWn0sxnnPMVLipxFoBYAioCT9rKI8ONBHsbOO3T45YDTdMbzGuP1YFCFWkhCUgTcKq_cMKndbjLv6MvcUMkeqOJnk7uYNhxJOjOBF5fMrkQi14_qUuSqs9a9fRsc22ZauwvaSQN3MO5eiN1GyNvT1ybnd5MjkHr3eM8orav22a9c0lcxQ8LyWMOatk6xxaGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k3f6s-CGOeZgPz9pSoGOH5qgoflmgzeNEmjbhmbprN7m6dVjp121pJ6Xg6UtJN4F0V8cAzhCIVX8QJ1wcVbhgpFjTPVBsbs0zOqDFr2ejXsf0GEcY-iruDa3M6vhCiSfuWNdZTYJfM8rkpYtmCJ-MLPXPQsq_x1imL3Iq0Dj0bGUlFrghlrbV67pogMKWyDcJ9z_4l43ZQsqZvOHOurLTGq1lZtYAOEG1rhlHoj9ROMtX3sC8Fd0rLivpIrXIDt5E41ALm9V0IDRZPTZnvQcp28rlpHvrLSZIe_hc5LupcGrWZcZQ8WL49Mle6zeH1j5CjbduNZjqJ4SQvSUEMzbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTd1w1FaVfwLx3rs546EXNuUuF__4lpCGE_QfBaUKezlCVmwKHOz-OminyAuvc3Tb7LlkyKccv-sw21LZzM7R1hjjLRmMMkPA9jb6lDKb8gBgivwB0CF5m6c0NbOOVH6bp8VAk-X5lFb1ynHYF0K4wQ0sALjwwjroisQBRxKtOycRyVkclLXkZ3PyQX54itOwNnWyxBxJHB0u6A8tu6usgSvXvALr-WyjDJU0CLkGJKDblq3DyUyH7HrcfcEwMEzeal1dp3K9-iZe3vWGITygNDf9YtYGICshtjSWr-_LnKXiys_rTe5qbiW6A6NIVqqp0o1u2G4YBAQ-wHuHxj6qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AVcP5nXkny5pVqFwqAdkvqDXMuju9Nu19FFp0v-p598UpqIY-c7V_zo1FPe5RP5Z7NQewzOZpi61pqjanRAH4UmTAsjPfRdyNXQgkyrnkVrm0rJdjZCBd1NX0bRLC9EoYEq48Vy1UAIlrlv5CJTTO65kvPFbptAVtx4oFWR2qubjtyukXOMqGC5WaejoIgxC_t8lAot-3mGS58jwdV4QbPzi7Fs54y3vj1Ld7FKWV9_le1C4L7JVpm8JDAYQAsv_nxTZKmCpknKLXfzXcva0aiV1ToyK2iy8fvZAUogEp6MwwGDGj3GGixwV-1DI3awbQeUK5CXGbI63pPgUr6FlOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شناخت رنگ‌ها با الهام از گل‌های طبیعی
🔹
در این مجموعه، طیف‌های مختلف رنگ‌ها با استفاده از گل‌های طبیعی نمایش داده شده تا تفاوت تناژها و ترکیب رنگ‌ها راحت‌تر قابل تشخیص باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681334" target="_blank">📅 11:02 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681326">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SR8AvE6TZA6pn20stcGTND5S24UJyAdNmhqDLh340vXwBIs4QkZ3Npq18saocyKGIUCJV-hkYsUfWJsEM7rB0C6C6rx0sBBwYzRGelM66txWp4Je1UlaHvwFIIIkg1jiIV9PozYKmgBlL95aiNYavYtFdSbHuRTPH07tWHuWoXRT45mKc8gv6Htx76YI_khzzSppHyG4X-Kb6PYR_enp2-mS6jfX3z_FCTGYm8cO9wJ5_a0vbY5bIvy6LB0VwLmThK_zBi4LrY63cpY65pftDagoeDqO0Qc_pKMnoJk0GYJz7quSkMeGNcjXuuG4rwTpT7x358g4XKzdM4KFdmvk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایرانی‌ها جزو ۱۰ کشور پرکار جهان
🔹
مقایسه آمارهای سال ۲۰۲۴ نشان می‌دهد ایرانی‌ها به طور متوسط هفته‌ای ۴۶.۳ ساعت کار می‌کنند؛ رقمی که ایران را در میان ۱۷۰ کشور جهان در رتبه دهم قرار داده و افسانه کم‌کاری ایرانی‌ها را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/681326" target="_blank">📅 10:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681325">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2576faf18.mp4?token=fnTpceOCLSMt1kPLDFxGgO3yETXcTpMZNtnCUFuE4SdYv-lwPH4RzM_D9d61ASpT6ArhJa-l3C_DEYt2S1UK8gRZF5XMVvo4v7c7VvUng4PS8Xb2E_-nRPc6DK96m1y3sTnX8N_WOU26vuyqhlcTgrTuTMRH3Xz-TJbDe0ncdNO4vTCtYge-2_g6ntzV7ToSa_n7a2zynl07GEIRSZjBGCEeDlCa4fdsgMM_diRXxhs6TugGgfnWrUe9JAeOrCC8I7UcYcy9wttLWrqMMOlmr71T5-7hIEmsSPnKX7lBlMfdBwzHJblxD0lktt7F0LZ6p2g4foi8OvaypH-pmdbghg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2576faf18.mp4?token=fnTpceOCLSMt1kPLDFxGgO3yETXcTpMZNtnCUFuE4SdYv-lwPH4RzM_D9d61ASpT6ArhJa-l3C_DEYt2S1UK8gRZF5XMVvo4v7c7VvUng4PS8Xb2E_-nRPc6DK96m1y3sTnX8N_WOU26vuyqhlcTgrTuTMRH3Xz-TJbDe0ncdNO4vTCtYge-2_g6ntzV7ToSa_n7a2zynl07GEIRSZjBGCEeDlCa4fdsgMM_diRXxhs6TugGgfnWrUe9JAeOrCC8I7UcYcy9wttLWrqMMOlmr71T5-7hIEmsSPnKX7lBlMfdBwzHJblxD0lktt7F0LZ6p2g4foi8OvaypH-pmdbghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری که می‌بینید از دوربینِ لباس پلیس ثبت شده؛ سریع‌ترین عملیات نجات گروگان‌ در تاریخ!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/681325" target="_blank">📅 10:49 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1490ef01bf.mp4?token=TQVy1CHEDoaggdgTzP78jMnssG7XzQ0RRmGOCXhZUre4iPEGhIvAwiWydtyu4hRK36vmRikexb0SPV8fVrb1DSJ8O4f6xurpQzHd15uPnz2HVtVCNLWYba1sSpjd3iKQW_ZJU7ften0h-cgmcWpaf4PyrqhQvA-wE9eyDyrthe3ZkeQX14BAAfTsN_S8PW8quCjdBeZ1eqfmwuy6DInaTmqOk7cWbYoBizuCLWr17311zVxtLUGZCctJIqZrNYlecaQaKIJcibHrh3i-GyFnX52MYJWPGVYp9ymEI-YoiIHuXae8kKGxZYW8cEEEdQ99Kfq84ne_pR7-gvnkPfKWgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1490ef01bf.mp4?token=TQVy1CHEDoaggdgTzP78jMnssG7XzQ0RRmGOCXhZUre4iPEGhIvAwiWydtyu4hRK36vmRikexb0SPV8fVrb1DSJ8O4f6xurpQzHd15uPnz2HVtVCNLWYba1sSpjd3iKQW_ZJU7ften0h-cgmcWpaf4PyrqhQvA-wE9eyDyrthe3ZkeQX14BAAfTsN_S8PW8quCjdBeZ1eqfmwuy6DInaTmqOk7cWbYoBizuCLWr17311zVxtLUGZCctJIqZrNYlecaQaKIJcibHrh3i-GyFnX52MYJWPGVYp9ymEI-YoiIHuXae8kKGxZYW8cEEEdQ99Kfq84ne_pR7-gvnkPfKWgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
قطعی برق؟ تاریکی دیگه دردسر نیست!
🔦
چراغ شارژی خورشیدی تاشو با طراحی کاربردی، مناسب برای خانه، سفر، کمپینگ و مواقع اضطراری.
✨
ویژگی‌ها:
✅
شارژ با نور خورشید و USB
✅
طراحی تاشو و کم‌جا
✅
نوردهی قوی
✅
مناسب برای قطعی برق، خودرو، ویلا و طبیعت‌گردی
🔥
قیمت قبلی: 1,598,000 تومان
❌
💰
قیمت ویژه: 1,098,000 تومان
✅
⏳
این تخفیف برای مدت محدود فعال است.
🛒
برای مشاهده مشخصات و ثبت سفارش، روی لینک زیر کلیک کنید:
👇
👇
👇
https://memarket24.ir/product/brief/47540/180124/</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/681321" target="_blank">📅 10:32 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52aac7c16.mp4?token=dfuhlz3c0nGgH624BEL1z01alGsknDFdGt9dfMTzEmdt_lIvwIu6pt_-C_86GBZrEd7HWMvIrMSyFZKsgH3M0GGhfo_pkJwreYcTc2ZVRmzAFdl05-BqaDCIIW_G8HTI4r-Z8G63l3--Yr6Je88xGe6Nca0wxVZlof7TXeye2C1EPj0eWBRFPuF-BM77R8idft9x4FEXiKZZYtcm_WTpWtznY3Ofa76_BHLVlMpOvsQN4gaiiozPUw0ZcuFlOoOC1EsyxMw9_-zwaBa15HELBCp0HuePmIfZ06gqKdj_uI59Gln-OWUbNeD-xyvQ5RgEy2p1OC9NjuCuR-tQsHsfFCdH6uEA_57H-HAc_jVFZUZeW1sTRU_4154j2T199ACgTAMq68mDvUKbAO7WA8FfD5rqze0-_rUbkfi8Eukx9BrE2v7ojqywtdoXL9VHYzedM1cUyTFazySuzCn5CK-2R83IOw5j3elrVIONGE1IHpQ2SNw-GJWfTFEOyghJKwQj70TdMiM_vJVgnIBZHf6oRhj73f-fzTnxmaseAKniCRGKRgv5vHdns4l5yyz1t5o6W00Vp8a7eZmoZMhXGt0PlV089HfN5Ru673MzP5dK6UbJSEQNi4M0FLkIPgQ8ESpJklF6WOhItHD4ZmsDACu7mLLEMSpv9tpUBeDAaULL6lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52aac7c16.mp4?token=dfuhlz3c0nGgH624BEL1z01alGsknDFdGt9dfMTzEmdt_lIvwIu6pt_-C_86GBZrEd7HWMvIrMSyFZKsgH3M0GGhfo_pkJwreYcTc2ZVRmzAFdl05-BqaDCIIW_G8HTI4r-Z8G63l3--Yr6Je88xGe6Nca0wxVZlof7TXeye2C1EPj0eWBRFPuF-BM77R8idft9x4FEXiKZZYtcm_WTpWtznY3Ofa76_BHLVlMpOvsQN4gaiiozPUw0ZcuFlOoOC1EsyxMw9_-zwaBa15HELBCp0HuePmIfZ06gqKdj_uI59Gln-OWUbNeD-xyvQ5RgEy2p1OC9NjuCuR-tQsHsfFCdH6uEA_57H-HAc_jVFZUZeW1sTRU_4154j2T199ACgTAMq68mDvUKbAO7WA8FfD5rqze0-_rUbkfi8Eukx9BrE2v7ojqywtdoXL9VHYzedM1cUyTFazySuzCn5CK-2R83IOw5j3elrVIONGE1IHpQ2SNw-GJWfTFEOyghJKwQj70TdMiM_vJVgnIBZHf6oRhj73f-fzTnxmaseAKniCRGKRgv5vHdns4l5yyz1t5o6W00Vp8a7eZmoZMhXGt0PlV089HfN5Ru673MzP5dK6UbJSEQNi4M0FLkIPgQ8ESpJklF6WOhItHD4ZmsDACu7mLLEMSpv9tpUBeDAaULL6lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش تند آماندا رز، نویسنده استرالیایی به توصیف «دیکتاتوری» برای نظام ایران: دیکتاتور کسی است که ۱۶۰ کودک را به کام مرگ می‌فرستد
!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681320" target="_blank">📅 10:28 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681319">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09a61bf62.mp4?token=CCy5AGRx4sS1ZN_eIQpfKZtSecp7F68vX4lVLWkBHRsoM7g9GQi3c9BWiUsD1EHVwaudJDZD4ie6ZwwwauwcQOfvM9ZhrAgaMuf_U2KMveN0b2_BwDZvUl2i2WatslANvjKki4AD7KTGT47F7WFezagebSENun3myjPe70VCWWEuquzl7hyyjC34jJpzOSsllZFARHoiTEtbt6HiACcUuhu2YcvBX8Ax-hoEfJh_R05UxQMj9E5IGEwumXcvGShfTwuY_4VBdXZNhDhkFwukc5c2ixarc-0uHJHTJ1jAm9NvEk5rWzEOtgH62dU_l3j9blc7aTknx_juB1TnuixaCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09a61bf62.mp4?token=CCy5AGRx4sS1ZN_eIQpfKZtSecp7F68vX4lVLWkBHRsoM7g9GQi3c9BWiUsD1EHVwaudJDZD4ie6ZwwwauwcQOfvM9ZhrAgaMuf_U2KMveN0b2_BwDZvUl2i2WatslANvjKki4AD7KTGT47F7WFezagebSENun3myjPe70VCWWEuquzl7hyyjC34jJpzOSsllZFARHoiTEtbt6HiACcUuhu2YcvBX8Ax-hoEfJh_R05UxQMj9E5IGEwumXcvGShfTwuY_4VBdXZNhDhkFwukc5c2ixarc-0uHJHTJ1jAm9NvEk5rWzEOtgH62dU_l3j9blc7aTknx_juB1TnuixaCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی عجیب از یک دندانپزشک با کلکسیون ۲۰۰۰ دندانی در شبکه‌های اجتماعی
🔹
این فرد طی ۸ سال فعالیت حرفه‌ای، نزدیک به ۲۰۰۰ دندان کشیده‌شده را جمع‌آوری کرده است که هر بار دندان‌ها را شسته و آنها را سرجایشان می‌گذارد؛ رفتاری که ظاهراً برایش لذت‌بخش است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/681319" target="_blank">📅 10:27 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8789f7e651.mp4?token=J_biXwAlhBO0Fg_xl2CwTCgoJUmC68QkmGCGFYItGvKKX7k00TlJciIoNWOOUCdy-cj5xBFBQRG4whe8oSjCd0dLsLCudjhLLqYkmQ-bO7hZliHJnwtZlFpMRI1hF3TPDfyWsFDoeO9_oMjk_3OIj5yfi08P67MD9CboOcGgbT2pazfSv-Qp5waX7ekfABIYmd9PqT-cnw8t0x_0PlPXmASIWLY0RPWulUIc4F6wKbOyeLaZPXBGHfvN7WKXls-HtloF2snEGJDeoEPnS78a_ddL_iCwI2YAZDhtwH0OjJBflM-gZESVGoKopy3XewgEXq9l23R8KoIHNBvTRVezbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8789f7e651.mp4?token=J_biXwAlhBO0Fg_xl2CwTCgoJUmC68QkmGCGFYItGvKKX7k00TlJciIoNWOOUCdy-cj5xBFBQRG4whe8oSjCd0dLsLCudjhLLqYkmQ-bO7hZliHJnwtZlFpMRI1hF3TPDfyWsFDoeO9_oMjk_3OIj5yfi08P67MD9CboOcGgbT2pazfSv-Qp5waX7ekfABIYmd9PqT-cnw8t0x_0PlPXmASIWLY0RPWulUIc4F6wKbOyeLaZPXBGHfvN7WKXls-HtloF2snEGJDeoEPnS78a_ddL_iCwI2YAZDhtwH0OjJBflM-gZESVGoKopy3XewgEXq9l23R8KoIHNBvTRVezbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: در آخرین حمله به ضاحیه مذاکرات را متوقف کردم
رئیس مجلس:
🔹
در آخرین حمله‌ای که به ضاحیه شد، مذاکرات را متوقف کردم و اعلام کردم امشب رژیم را خواهیم زد و اگر رژیم پاسخ دهد، کل منطقه را می‌زنیم. نتیجه این شد که همان شب محاصره را برداشتند؛ در حالی که قرار بود طبق تفاهم، ۳۰ روزه باز شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/681316" target="_blank">📅 10:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
پیامدهای مصرف «گل»؛ از اختلال حافظه تا وابستگی شدید
وزارت بهداشت
:
🔹
مصرف گل نه تنها از منظر علمی اعتیادزا قلمداد می‌شود، بلکه می‌تواند آسیب‌های جدی برای تمرکز و حافظه مصرف‌کنندگان به ارمغان بیاورد.
🔹
مصرف موادمخدر می‌تواند از نظر فکری و جسمی وابستگی ایجاد کند؛ به نحوی که وابستگی آزاردهنده‌ای به مصرف یک ماده مخدر پیدا کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/681315" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
