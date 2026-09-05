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
<img src="https://cdn5.telesco.pe/file/Yk_aN2BNTEALTKKu37m1Dux5Gr5Ra3gqdJEQykIzYOz144QoJ2mgzOpSz_fAWDYG83CgDl2FX4JoMlG04Em4uWZGS_Up70pBlqmgTDZzROhnSmqjQ4wRdxjA0C916tKckkdQNes02XAoDy_WmQ0PgDYX0DpoBsSxNc5TZZXdc1Cc4XEGNXZ6F2NpZ5W2BejUkGf1NRG1siFnrkq74Ecz7GYCtldYMqnWEcHC3ZsGLkomT234wkjo7OOarFvMVxb5R-yPoLtx4JNwHlOsUYhYJEj9pPq5Bo2c7R27up7sTzPVVpI2tQoAVm7lorlbGPe3qsHexM1QGe866DPeliOUJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 426K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 01:59:55</div>
<hr>

<div class="tg-post" id="msg-105655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105655" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/Futball180TV/105655" target="_blank">📅 01:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aetgjCKioELIT5HUX-_tVa0nJe78bJdErJL70U2acV3-F03GZttP9xFAqIW-WL4kIodLwBwttB0vSHsiZudJJx0BwqTLS2hTTl_-ZfogkNSj7XlTcg4ZD35DvfEeVFeIxF-SOv2niA2TN3kNYYT1N_lfoLZli5MBM3453bu5FxGFp1BnggXVnTKrLkgvOHkLP5QB79mRtaULwIK1fqU7HIk0olU_Ce-tyJv4ssyIHM-3LpJ7ziA66cuRsI6wxNKLgr3Ch-NgvRvyqd4DKP_t0Vmm5wnXUWzBrW0oTKu12irM7gMz-2rEiQ_dJdr03m323KICSpBp058iyaAquU39DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
تنیس US Open داغ‌تر از همیشه دنبال میشه!
🦖
مسابقات جذاب
US Open
رو در
TrexBet
پیش‌بینی کنید، هیجان رقابت‌ها رو بیشتر کنید و برای جوایز جذاب وارد رقابت بشید!
🦖
فرصت هیجان
US Open
رو از دست ندید!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/Futball180TV/105654" target="_blank">📅 01:35 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/105653" target="_blank">📅 01:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dff4d583.mp4?token=NgJrn0cPcwkVU0GkzDG4IctAEu83OYlR3ECqC2Kd5GCAqHYGMgrBE760qLokqpcCauwZcG1DOsUEyte5fewEM-xi8xJbMhocuWNOPaKgdBPrkvTxPeMG8_GsYGMgNiZ9_0c-2valf_QZKB4GsJkleHnbTsC4GlaKvbKWwxohSeAbAzx7mmtLsRnyD2muTCfHoXYvg0Sw-6cYj-9ewh-RAESe2xS35xK-ogrw5sZZRMJmE0BqvgcdHue3_7sMpOelf1slDYb7t5rgd_Mnr02UQHOkZ9SfSmcJsGyG7EOgGuAO9PvD-IJO_wLRoaYVTBiPemDjhbBJw3UkdqUDvYnUkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dff4d583.mp4?token=NgJrn0cPcwkVU0GkzDG4IctAEu83OYlR3ECqC2Kd5GCAqHYGMgrBE760qLokqpcCauwZcG1DOsUEyte5fewEM-xi8xJbMhocuWNOPaKgdBPrkvTxPeMG8_GsYGMgNiZ9_0c-2valf_QZKB4GsJkleHnbTsC4GlaKvbKWwxohSeAbAzx7mmtLsRnyD2muTCfHoXYvg0Sw-6cYj-9ewh-RAESe2xS35xK-ogrw5sZZRMJmE0BqvgcdHue3_7sMpOelf1slDYb7t5rgd_Mnr02UQHOkZ9SfSmcJsGyG7EOgGuAO9PvD-IJO_wLRoaYVTBiPemDjhbBJw3UkdqUDvYnUkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚫
اوه‌اوه لحظه‌ای که خداداد عزیزی به داور بازی میگه کصکش
😕
😕
😕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/Futball180TV/105652" target="_blank">📅 01:07 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b7a4758e.mp4?token=sEqYq9QvYEUN1j0QP12BMRGv9XObYgHEVLvwP23ZCX0b1tyEoPlRNtCBk4IEhjZLsizaWIknPZgYDuNK4yYX3PV2CfcmFCUAwRcpgXCr3LVYFrwzsnyOce88G7JrvDD1KRV0OizwTJkEa0HnOhcyvgoLYL28c3anFYKHvb6OCQ7dYeuGODmTRvb7MpztM1alxpcCpFuh3P9mnhz9S4aU9V5hv0v76Cu7ORZyxdOSFAeZFB-_cINLMylo6wcGnlIjo8zok8-BHtl0hGvNtPxVrWJH-JE50SHCWfzmQeSndlrPy4fb3G6sE9vzhx8V_yG3xO9DeADX03xdoLPW1TkkgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b7a4758e.mp4?token=sEqYq9QvYEUN1j0QP12BMRGv9XObYgHEVLvwP23ZCX0b1tyEoPlRNtCBk4IEhjZLsizaWIknPZgYDuNK4yYX3PV2CfcmFCUAwRcpgXCr3LVYFrwzsnyOce88G7JrvDD1KRV0OizwTJkEa0HnOhcyvgoLYL28c3anFYKHvb6OCQ7dYeuGODmTRvb7MpztM1alxpcCpFuh3P9mnhz9S4aU9V5hv0v76Cu7ORZyxdOSFAeZFB-_cINLMylo6wcGnlIjo8zok8-BHtl0hGvNtPxVrWJH-JE50SHCWfzmQeSndlrPy4fb3G6sE9vzhx8V_yG3xO9DeADX03xdoLPW1TkkgoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
🇮🇷
واکنش محمدرضا تقیون، مدیر روابط‌عمومی هیأت فوتبال تبریز، به ادعای گل‌گهری‌ها: فحاشی صورت نگرفت، مدرک دارید رو کنید
!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/105651" target="_blank">📅 00:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105649">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=tdNFjb31zLaB01VrOuxuXkbcmYK4BhxCo8iJHEUzguLpSp_81HqExWm9mXTA3nXVONvJLUSg8ErHMiagqBe-VTNSPrPAqL6TQdvasnmVQro5-1cpl4hKrvBIEifDlxKgAj5r9sAgq7S0Bs87lq8gaxEDP3_Cg47JKCHUuSBcxlhmpZjMjaCrtfktTL8YVdX-WBzIGxWGR3cNz6iOtEcxf84DhOKCouKqkOPshlXdrdiSzlvwEPzRRXiezxavaOz32aJjBIhQ8YtkBnHRUzIrehb1jfZfoVQPpT6FlQ9S0QhEl0Ee8T6f6rqwsjIUf-lpfPJvmszZGXpTzSKJnMt9KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e65ac9cd.mp4?token=tdNFjb31zLaB01VrOuxuXkbcmYK4BhxCo8iJHEUzguLpSp_81HqExWm9mXTA3nXVONvJLUSg8ErHMiagqBe-VTNSPrPAqL6TQdvasnmVQro5-1cpl4hKrvBIEifDlxKgAj5r9sAgq7S0Bs87lq8gaxEDP3_Cg47JKCHUuSBcxlhmpZjMjaCrtfktTL8YVdX-WBzIGxWGR3cNz6iOtEcxf84DhOKCouKqkOPshlXdrdiSzlvwEPzRRXiezxavaOz32aJjBIhQ8YtkBnHRUzIrehb1jfZfoVQPpT6FlQ9S0QhEl0Ee8T6f6rqwsjIUf-lpfPJvmszZGXpTzSKJnMt9KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🔞
⭕️
⭕️
⭕️
⭕️
‼️
‼️
‼️
‼️
🇮🇷
🇮🇷
صدای منتسب به فحاشی زشت و زننده و ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105649" target="_blank">📅 00:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105648">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArWr--WdKHkE2sD2RVrrWjDYgR-FTt_YQRVRno6wMDDEJuzHuuT3uOUAJFkuu5L4PX0DOo1FBYQDCBq99urZPD3cODju5hkA2EVXXJfQMNj-UVhPu2RAu3TOfrDHI7ttLPS4zSZEx5zU5gSm8CtbeRTKu4GCU__Y5WaN74YEsicHkzphYcqVL_0m-0g0tE2zo-xTOO04mbgclrMX_byKXzXIONcdrooB3H_rDWB82FmUBB8EY6iRcw5WtQX-izATPMCBAE7Y53EWZnrUoViTk21gsGitv4wQOlP9BP_Fi3PXNhF54cRmTf0KopYSkHEXdr669Yq__Z5o1dofU-9GQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
💥
اوبامیانگ در این فصل از لالیگا:
📊
👀
4 بازی
؛
4 گل و 2 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105648" target="_blank">📅 00:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105647">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0972e47983.mp4?token=ut6ZAj-47c5LHUZ4fw9RLIpeVmwRT9HoNtehvwNh_FQb5buO0BG5n3y3qks_Mzp7TVpMcQbuuCzgXKD6-lAp_BYDDxcXs1xdUoptmISLIaGuFMF0-0htOt2g83Fj0l_SVWYjg9T5SYxYdFA0WOcow-0EemCXOSIGThFhsyi7kKN2PjKt1eEoZbO1f35aKcvMzxy9Ec6zRuFWJVE9N7N6qgi-zJJXZ8FVq5bCkz0t2lQjfEZMmzOJaKlkD6nGzj-GK9N7uhYNaRkCV125gJDLmm8ajcealObaswAf0S-Dt6Z4jhGwtoc16hkgGedJCcIjVPGuV3j92wdulkytT1ZQX6V9I5Ykg4p6FLLQcUPVeGYqFgEr_kL7qSQwf9JUe31W5m5IQi27qT3ITM48VlaK9bGdhn_75lECaPoMBMnkrzu2jgkLskTi2etEnbtQJz9btR3hEPOE0qf_71pPnw9MReghDTtgVu5U0xb_bes83DHe-24WdXdCJ48dLgL6t4h4MFys834tP1DNf1ID2LPQS5Ukw6KB0ikL7pXt97eie_4JsVgQLt8rbQ1DmaXZL7omEC2uH5XE4huY7GhQ4jv1A9PRwM232Z3tzEAhLy8DnVMJ0s0qRn2WzubS1eBqeV0UQV8NBUwInruxQI1TgHqjY-MDlkXZdZq1VUFi-6Bpghg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0972e47983.mp4?token=ut6ZAj-47c5LHUZ4fw9RLIpeVmwRT9HoNtehvwNh_FQb5buO0BG5n3y3qks_Mzp7TVpMcQbuuCzgXKD6-lAp_BYDDxcXs1xdUoptmISLIaGuFMF0-0htOt2g83Fj0l_SVWYjg9T5SYxYdFA0WOcow-0EemCXOSIGThFhsyi7kKN2PjKt1eEoZbO1f35aKcvMzxy9Ec6zRuFWJVE9N7N6qgi-zJJXZ8FVq5bCkz0t2lQjfEZMmzOJaKlkD6nGzj-GK9N7uhYNaRkCV125gJDLmm8ajcealObaswAf0S-Dt6Z4jhGwtoc16hkgGedJCcIjVPGuV3j92wdulkytT1ZQX6V9I5Ykg4p6FLLQcUPVeGYqFgEr_kL7qSQwf9JUe31W5m5IQi27qT3ITM48VlaK9bGdhn_75lECaPoMBMnkrzu2jgkLskTi2etEnbtQJz9btR3hEPOE0qf_71pPnw9MReghDTtgVu5U0xb_bes83DHe-24WdXdCJ48dLgL6t4h4MFys834tP1DNf1ID2LPQS5Ukw6KB0ikL7pXt97eie_4JsVgQLt8rbQ1DmaXZL7omEC2uH5XE4huY7GhQ4jv1A9PRwM232Z3tzEAhLy8DnVMJ0s0qRn2WzubS1eBqeV0UQV8NBUwInruxQI1TgHqjY-MDlkXZdZq1VUFi-6Bpghg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
🇮🇹
کامبک جنون‌آمیز رم مقابل آتالانتا
🇮🇹
آاس‌رم
😀
-
😃
آتالانتا
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105647" target="_blank">📅 00:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105646">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed90248c0.mp4?token=txVB9sAZFZGZiMDswJVd0DWVHKoLRoUSNR-bu89yLRbpLxPh6icz0EQHDuc7hI9AiW57JgOGwh44ZyBFqe6N5hWotlXxTY0OplLA2F9aquPqZUoJ3tFuhtmQ4-bKKTzdVLl9Zt1zHP8K95SKqXg3n0ki7ZNDBnvNBIitWpUq4CgcfQUTz6SilA2Xkie6hd6feZILoI9swz4FsoZKOaPLiY7tAeho9_Xjvk53vTt35Dvx5MoVeiCxmHY55xhE0DlwcpVmXV9jcCKWi3DvjwzA7wj_4SfPxvb8CFDACKyToP_IFCAQUodZUyXn4JyEJC8G74XHWKuxL8zU90XYJQ1CWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رونالدو از پشت چسبیده به دفاع حریف تا تاکتیکی که مربیشون داده رو ببینه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/105646" target="_blank">📅 23:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105645">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea5a0900.mp4?token=JhG3o9yQgoG6h9lKuMdQfrL7JtlFd0z4dLgspCz9vA8ShMsC-hOpfvERmdJi4eikw65pI5XG-xl0350Wbqcrk_Wg3JHvYKtSrd0Ds5yU6A3mPKYCHCPpb7yrBrEY4kLZt0xTZRjTYZZnUHvxnU93YIYR_K_-iuXgWGzdVorgvMO8u38W6SC02nI3umQL337Lb9NYPCFK3r-Lk4r44UXHQwFJxRObaY0eb3_EwXhjhAvTQWq0Vs8udRSVBVzmlXcZwFwinW-qT8Y8OzOcvrNr5skEeWctmUp8j-YbHcPtTSJDdqYJuaC1_CgD-6ufnB89Zm8Rk3vezUxepPpxedCEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه گل گهر با انتشار‌ این ویدیو نوشت: دو صحنه مشابه با دو برخورد متفاوت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105645" target="_blank">📅 23:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105644">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5829c411.mp4?token=Xs0dJDYbiUvwGzza1ts1WrAKsOWsAjvl2B9rKeNepzQzxIfAvcHdFzNI5b_fbytVlf0Lb2hzpRh7xenEpTsUoB3U9oM8cxLGU277wf-eqIwpi7qFJ9IuCzDe8OXNVqHgG2azW6H_VXrGCzsqZ4bgP-4_GS7n3f_7V_Z4pMiGBXwY1kb-N0UtdPnEaQe2Z4t8AOlSEEiKGu705wiAmRDVdQcfZ4dQRoUNUSmHICZytFsjUukHfZ5ASIJ73pgO89inp7wzN-fl8VZZ4bu74iaYlJB4P59LZigPEJ40lBFCOmVaRcpImgnHOX41LJkK2fHAC3VP_mZIzraCod3dllkIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
باشگاه تراکتور با انتشار این ویدیو نوشت:
خطای شدید امید عالیشاه روی پای امیرحسین حسین‌زاده در شرایطی رخ داد که بازیکن گل‌گهر پیش از این یک کارت زرد دریافت کرده بود و با توجه به شدت خطا، می‌بایست با دریافت کارت زرد دوم از زمین مسابقه اخراج می‌شد؛ اما متأسفانه داور از این صحنه نیز به‌سادگی عبور کرد.
در ادامه، خداداد عزیزی، مدیر تیم تراکتور، که نسبت به این تصمیم داوری معترض بود، با تصمیم داور از کنار زمین اخراج شد؛ اتفاقی که در نوع خود قابل تأمل است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105644" target="_blank">📅 23:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105643">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fedf27ce.mp4?token=FOwwa3_xkHFW3gMI50CakMQjbl06Pa44J6sLt5UhJaOVuQCReTmPrn2wFq4DojKY9Hr4tSusyVF_44kwgvktK1U_b793F24AQrwwRIWTaXyUy7-KZOr28lQsgBXobpdeNwg6Fm8fmIk4WFCNz9_ZNcEa5v7r2SbjkmNKrS7ILqnd9g0Qqgh4ODS8p7QXzASHrMi0EH-C-lYyOQX0wT_mjHpRC4GfGYLBWLjI_11N6fYUhAItac6LitQOgIJoMsnaiAuWGn1KhKSdvEKHo49vY74LSpG4MlxSzC6tYUEQB4XRWAKQZ1oN7dPKL9R_ouw7SZb8kdAjvZySHJkAPlGJOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
مهار شوت سنگین رونالدو توسط رایکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105643" target="_blank">📅 22:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105642">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/267551e507.mp4?token=Z5w_psgeo2Y06nuyFXU-Osz3MCugmvT2Hy1STBvXNeLqZnShdQIw7nMRo-DzflTwMfkR50Crx2HMICujCTRBjSWN8MKKC1D4jDNiLWRkK06f979IQWaK4zwS2Dtu_ffP5X7_kYpd8jV4hpF8QcM2qUBxgO764cG4dBqe5mszGEpZj6IpYdiNVVDqHSeOM_MqRSQvpRfr3yMHHfUES00EwLcHphs6I-BIClA0Rx_XGN2cfbr3aK74FcsxqTO89se82KsVJYMqxecHviXZ_OSbD2_Rm6yflBfafYxMfo8EamVRncA8w_-Ifx13RbmFLB2DIwBqC2SSgJZY_ZJBnq3iYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🐐
به پرواز درآمدن کریستیانو رونالدو برای انجام حرکت آکروباتیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105642" target="_blank">📅 22:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105641">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62cb090160.mp4?token=NmmRaz5IJT3f_CcvieqGDqlHmQwT98II1HQINfHesgHVr91YItCTuszf4VSQKjpkbSXQyMhiGOrdard5krJClVNjp1eMJ7Cwoa_yqAUjdieWJdMM59oACYc0-7Q0u4FTTUg7u4vnVFlqnEY7XVO6Uiez-ngoqEBuRGIW52JlUygKyEonLl8ddcjojNqtpnm00WHbW5cIEp6ZwHW9slxJQDIwqjfxXy_e1rkVc79yr4lW-3MMP4gX6j9K-RZQYbSiAnahyLq9Wt4NsRZkJ0u1ykTIoHtmtm8p_2zsnwyK_lJMjfuLsxXGQ1ej2e9jy5sty56ykyn0hOFCJL7Q5QG_CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
حمله شدید امید عالیشاه به خداداد عزیزی: خدا را شکر سابقه ملی ندارم. من نون بازومو می‌خورم
🔵
بزرگتر از شما هم نمی‌تونه اونجوری صحبت کنه. داور سر تیم را برید، گل تراکتور قطعا خطا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105641" target="_blank">📅 22:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fes7krtB-XoqFR7HVJaeSGqYmgqumnHDDLqfrsGDcBFVXApxOQlxtmqjk9Emg09VyJCrfr-aly4_tqvm7ntpLA0wQ9P787grF3OhFTRt0a9qKpuEwyGB6zyvyufmA6WnVpLfCXL_jsEkcByjCiB-xPS60pJRWEzgQNFBq09_6hGqmrjlX5TE16TTKtLN4KvUinjr_yPY5-pxtjwxltVzAkLUUsa1yh8eBwh9BA4-tARr846TKFxlkgmTEmPC0gn3C-C0T_4Nk8ZUbO5G89IjpJ0GlNyQIHm8aTGw9A3V6M7aBMeASEriCmgXPYk2BmnUCDuR3Tl3ifDsUJxDY5T6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🚑
محمد عمری بازیکن پرسپولیس بدلیل کشیدگی رباط زانو حداقل یکماه غایب است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105640" target="_blank">📅 21:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5384812d.mp4?token=AsWSuOb5N-5wGZ1CKiBvvI21wd3klBWxQgoL5jOZ_gTS1l78DC0Ca71HK0cjC6DoFHmD1pORtS-GEmLgjcjvQScJ0nM1tUe3N_rV6oJpdxKbSA0FAjtyVgiM9kA6lgSuk6l4-TJr2-bX1GDbqEy5IOApOLRifImEgDo2ULqrRehrQIQ3Hf-FFHziXtpL0XI0Mt0bfjGJS9mG4zg0aeQQUT0dJt9pL91MU0FaNkiWA8pHZ11wlLbCIFeTVMxLgZH_y7CesJROwbWc2snXOY7Fv4YDXrxrbm3celrI3TuM4-d-rWC6-ytQUHYRJfwZUafmiMWtP8haQ7PcSz41LIbKEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت‌کریمی، مدیر عامل تراکتور: از آقای تاج درخواست داریم ستادی که علیه داوری بازی‌های تراکتور تشکیل شده است را پیگیری کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105639" target="_blank">📅 21:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkWFOPnxA2EC4r2PupsxxqySXxLLJsWYC-2kY0YEKxzih3c4yeAocwKsOFCAbmSjd04vGLZBA_MXRx-EN5Lz_zUVLae3NpNo5DXWKaURIz27mTeBBHqitfWzUIsGiCVPCDdL-Y38vnE_nD2zt98v8VF8fkXnbIwil7Dpm8YOY-b16AU8-osoGfYgeToyav82f8IE1OzYBtg9QIkuPjaOs0rWVd90AUDVGNsyg1ZJnKLM3udcCc75ZDoyYBtjm3JjrByuQ_u_yJ95NWswZQMBAEhgZ-OCyx5fSX0ZMlSVyT_trqmtSWK9LhIFvk3l00uRK5r2iWTLU942zUMHsmMyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105638" target="_blank">📅 21:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f75618ba1.mp4?token=OdwD3UxE6j1N8IMeRFCiZOORAvB63AyG8QUzYrDllYYSAeMZFNbbB2ogx28cKNZKvhUwA38CYNis5uiTKrUvmoQfeiuv0ZRGbTrZ3l7a5oXtQwFpYGm1cqw7T_1Nffuk5COUYcgLfJP0ltWDybfc7O2Xdr0pEd1PkGwc5u_mptbPJ24cE_K5ozOvQs-7-_6NOFLxNQ3_eDgaxTfQ4eLiDAhFKzVFUw0PmaMz0VdwQaR_iR1puIDVmtwQaOwGIXh8tecX3cO0rBRzYOZhx3O7eaY3zBqJEh6tnlF4psSND_YlFstAyNgR5JI7MiPeL2ckCfNT176cIqbD0cywegzB-HGRIRf-GXYbejhsXElhBiH_UnkMYcidryV4-j-p4PB8WJwDEqLmaeM5sJzoZnztt4KaeMpstIfGt77W9xqVv86TTfVfZhtjB4zlWhQxqX5Onx6UfBql_zTDUA8pASyNHHT_KGzi6JYMbaTbmySWlxP0pWbk0uFm9s684CXqlD1y2M4Y1y2Ei_d2vHRq1Mmz19Oh8DkGV-1lVNSYpM9sGNApnEneq1rKgNkPqcaSX9ZJZQMrQ5BE5Gj_rq5bVYxMJBXdab3gPN2M8WG6hIJVB71GHX5uSs8HYAMTMl099V8xEFL7ZTp4OCsy_xPR4hsN5lFtPB2-biT5ZcJh0JSB59Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇹
گل‌سوم اینتر به ناپولی توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105637" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8ffHm8eDwE6KH3blBsKX6sXDpea1fdp3EaTVLyxvXWso2n3O26mZC6LzpxwJRuxhsiYAfPC_fpOYC4rgL_pfa8QPz6RNu4D3oUQeB8XfrEm7aqhUDnGJy5DoJNaKXtJES2BVu89nK6oEFusCOKTCB9kJA8yOzgmh1AHqOy6ahUn5mSZubyywKJaXLfT3tp2ryFqrYOkgtJkh8MYi7m_WEfuj5dgNHe3AiR30BwvWxLshg8qljsG4gCybD0s2km1LgIKqpJyJOKIomYz_O9rJ6ToTaEOmQwmlfNyCF4deewDv7rtVvE1Nnqx5fNCkRaf8PkYVe9_OZdjlicGn_vSeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105636" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3686a0d49d.mp4?token=CJZkTe1TSuJ91GVq5DWKe9v6QLpIokW7x1HX0e7itQj0KpKWq-i33jJHX6DGe8zd0JAZWA022h6gWiTu1zeo-2LDES3bbYiAFv-y6ZM0Tdg1m_vI-EDkXoUPnTsTarhPN8uwsGOLF6AsGiLEi7K5Dv4R_Nh8XwXEc31_bR_mBbfjmLTKjZ9ud-YqsJu1KCUBGL1nmVbGw1NkDa8Xra_4r6WhuSrMCneelQNxm7mksPCRQm9QKcU8cOFtNUpwbDCI9fGj01wJsQI_D9IBdPCxY9i76p6L2XZpBrJp0iq3CuDQEpxZAPsdvZqVAKqRNJ-IE8xuD7jydZq_-XelvcpUXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇮🇹
گل‌تساوی اینتر به ناپولی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105635" target="_blank">📅 21:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گلگلگلگگلگاگ سوم اینتر به ناپولی
😐
😐
🔥</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105634" target="_blank">📅 21:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56515cdfb8.mp4?token=TgzuauekKI3PsKUTFH_hQJbMoUpJn-ad4B3KXPKEDsnaee5ofUGZbl20-C9JVxI8LNREe6MI506-cOy3x86Wz-88AROXeJTkq-Uha2spiBbXqLCl2gJdJbiTJxxQ4DdBmqn5GK_h87UF2c_K3dyfEPMCXmbFkgRiCRO8aVBrPVQ54lluxde0TTtld7HNe18uymvUHxQYWtNH__EzUJWd8SqJlg8ccnDVkm7eStFK7KijtstGYdVRDbfNSr1vnYH_-N_Zr12H4uMVeDbQlp10I5DF8Kv9gsWw9e7peP8zKnOanPYbPchYi8-MKKYwMeBZvEK1A8T_eKN0kzOh6J6MBREKpa4UKtfCrTR1qUoTEEgV9wm3N3D7_3MLHtXNl9ck5vYLZkjpMeSQpplZ4IVOSg8jbfvIrA5n07J7DJMtZuggo_xvN0IpTM7xW09pJhegAFm9QZfoxlcj1PUtpHpg8DIZXxUA4mDDsOxvVjwSQpVS9-y8pVMAB7J2HTGSR0fnLz9I1435FxD60wPugW1Ru8Nn2I3OZivM2Mq6Nb69Iglr4OCh_TFIdYrgKI6DXkYUzHDS9NuNOIvxb2ypFnm98vn1nvP1Mh0dsVOXDU4eIp5Vu5ujcx4-mZq2anwXVoNjM7o-MUrEE8uYEAgHg2ZjAkjSFh4BladG4Top7mOmVLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
‼️
صحبت‌های جنجالی علیه عالیشاه؛
خداداد عزیزی: او اصلا در حد من نیست
🔴
بیاید بگوید کجا بازی کرده است؟!
🔴
اگر یک بازی ملی داشت بیاد صحبت کنیم
🔴
این همه مربی آمدند رفتند هیچکس تو را نخواست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105633" target="_blank">📅 21:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8b13cd017.mp4?token=ZkkWZO6RDaGIW4nE6eDFWyTMScz-I4VqkkpFu1egxw7I9mku4yIx1EGXhPs00K-O9RJU0jfkLAonSq-_185BVDa4twedgNpbImJz62EifBwy5-dYn2shz8KN3JH3hR-Ugow7AEflOj6iDUyGKNafhQG9uXHVFSeLs2H4RRrIcW5nVt5rbeJX11NHbEvQUYC5IO09XHUwufG7E1TapW5AJdbaRFhkwmbmd76YWp1K0cFvj2HUdebdale7UychUzztKVVllH-GUSnRSDSwfhijTMe2_TaiXhalkCtc4t-LPphkXX0TNFLsy8emnVFHNNGauYVROuwOA0thhlUHet2TFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول اینتر به میلان توسط لائوتارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105632" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f3a740412.mp4?token=D4NbPjUW6PZfk3H2ZIfcvDvMgN-W_x2piRAkiqXyuHHUiRLsL-Z7sWMr4qTYFxCb2zTaQzaW8bA3I6RPOVEPe7egEuKZCP2ux7ASSim2yoH-DgAxEoSW5y8w2NGtEJFR-ScWgCa8Mj_J9kuKq54goaUq-FqEhDBWXUMHxcKCKUv0BU2fzYiCNFgFix2defuz5BM9F9GiBHa2tldkMw26fnU8lvjJ3WrGCZCpYhyM18otgVfpYVy9wQhXyx6ne9AzvPbngIyLWBmVA_xFPfHsaq4qMaOYQvKyLNb2zcIR7_jtb4M4u0_Uer80a4MYY9WxBlQpZBWYVRsEEgpxQRjyOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌دوم ناپولی به اینتر توسط هویلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105631" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3255aa137.mp4?token=nljlfyfE_QE_lI9k-UH4JssAXt_47x-hEIi5Av39pKtbsk4sld5dIqEyjVywwMZi9hGhfwhFrnmbxjygxrbVF5KxaMIMhcQ-jWgpDSN31DuQcAVEHUantr5Qxy9JcGhIt9K9XVnA5Y8wv8-Mg6R3Q0WGcJ8npJYrWAKvsuDx1wv49pDP9WZuQ7idj9GOamKskcdt8RXgs39FZji9-cwZwVl4_0r3yGfekpddNxOSQO9Dms430wut7QWAc06vBybVupUDnZwd_kXBjaupoPqdXGxIQ8h1g4caa14eTrbZscq3VPF_nr1Jf2Fxromq05WOe7gBd7H2d8TzSgh-iI-6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
گل‌اول ناپولی به اینتر توسط متئو پولیتانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105630" target="_blank">📅 20:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbX4gQce3Ygf9gSnZkOcQfrmQF3Pb_n9EywhZYDfcPcM96zf2-TFdVFYHvAPHc4HlLacal-kOhNEnILR5sWi3UEKFXaodHCmoZyYxII54kY_DpI2MZsjVZGlJZlv3_gsDOci_VtiqSZSwciKhjfjpApCosi54IBxH6O9Hyax4YgDAouY3tYf3JEpKR__eXjnCBejkOjX4zi05XHDvRCH8r8qFCJaN-szMfz2EjSCpBPjCLWH8PZXxKU6GoRju9-Q3EXXQ-LUhDctzR6ddclhGe8vNwko_EVWgkJBPU7n8bhdOj75yVQCGdXN-S-EPxN77InFoJkMILdI8rnWFvg-ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105629" target="_blank">📅 20:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eaffb64a.mp4?token=qCGEhisukerYOVmqFr9HIwu-nBBJj0FUI7xnG6tk-Ii0gBv13Fi6vpjGF86aeswMGUt_ociRIFNmvAJmq_rzbPX6W2SzC6qwXwifpLGQdVoaBfIewoY-67IsnqAoTSmXk1bK-FGRLj65pdVuAI8wsntQnp0p9X9WVm6coOLuB1wzRJPflh_AgaKp0_BroMclAd2Mhz5sp7CMlwxDA0KQ2wFbXTASdbJHq8OublvUL38OzV9yTleOyC-Dms1thngVq5lV_Zz0iBS7X0aAz7Urdk3whk262hreqbUGuXKiqAMPNULZyETs8OP15lJVhvlxbRVHP9v-IQe4vURyi-pF60bsFCc3sZPRMTXs-ySgdA9xRoumea5mPTCTBukQ7MwWgrRhveDl6vTuRB38kpMDl3HBGiXulFMBGIHowQzz4lbnnHJ31pfgNJyzbxVjkfk7L-6hrdljtb8DqhGYc0hDUlLIVlpxXI5Oenthy3EpMsriyyqnlHCuejBGrvZYKFKKZ-GX9zglB_xv1Y3v7UrPva2KGYOqkSEB_0WPPN-nMuqMt-X59Del8fhI178dzBHXhytjUyE4QkgLK9xAC4ZdhljaTcQ9ZNo5oNtUBl37C3g2mNcbZ7RKNdpWx2Gvkd4xNWqShOiznPKEGvYe0SYATJctoNxHVl4boVo6mcGVTKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
🇮🇷
سهراب
بختیاری‌زاده با کنایه به صالح حردانی: کاپیتان دوم ما باید یادش باشد که زمانی ناصر حجازی، پورحیدری، شاهین بیانی و زرینچه کاپیتان استقلال بوده‌اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105628" target="_blank">📅 20:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105627" target="_blank">📅 20:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
⭕️
⭕️
🇮🇷
سهراب بختیاری‌زاده: تا زمان حضورم در باشگاه استقلال، صالح‌حردانی جایی در تیم و تمرینات ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105626" target="_blank">📅 20:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEfWKDZtZfw3ZlDM9zwIAOr51YNLDYvyD1b4WBvCoD_m4pA5_R_05XNJ4RcLh6pQoRIbvraOifzWZjw6oRtH8zhCJBwchMg8EHEWcXLEQBD76dD8RCUxEMBpRjQyyG8_VijR7SfqAfwilI4CNQWCDmurc5R4E6_pABWL9Fjmy7cLmcjuU3Kracuf0Qj89yw1hQukWk5aBedpXso_9WtMVyOLRT3fz0S3t8xiRYyD0SpTje-hEgxbjwwUYm5spcVYyWd-3BhpIUA3OyhVky1o2Q965mIzuO9FZ70r7pvXt7KS5t9ezkp5gSVnGqV1PJPSDkL63oQpCvM5v6a1UzrrOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
ترکیب النصر مقابل الاتحاد با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105625" target="_blank">📅 20:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105624">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QoW86EBi1OjI2oq8P3Gi5aHU7zaBiCeNhn5-2Ks0A79JVidnz0O-dFEhLihHg2mv09-trur3FG6eGIKx_jjnLI5b-g-lfKhDdiY3X8yQ1XuSCj-ciZVKWwkPGzZSGj3oeWpD4WKyWgllDLAm2ahI-aXnBP-RRoNDQiHdg4msgDRlPc5rwFyfO_fTwqUx0G0IcII4wJKotv8EGMwCkMhd3qMFRDE9AUw7DeFCtS3EWX8eMJSVJOAOONWYoHB_tYBwry-S1h9f1QTTTFTVf438G2DSplQNf75_UiAm-djNaCJaez4UBO129HkKqvvLnbQvTmTh8zVABB4QVqrGd1l_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌ششم لیگ‌برتر؛ پنجمین برد نکونام اینبار مقابل همبازی سابقش رحمتی؛ تراکتور با تک‌گل جنجالی امیرحسین حسین‌زاده در اوج باقی‌ماند!
🇮🇷
تراکتور
😃
-
😏
گل‌گهر سیرجان
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105624" target="_blank">📅 20:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYet1nlpnfQDAPZHM5ciMCFs0crLSqnpSS31lozMjIrw9O7Bl5UL5ekTiRK7ZGLz5U7soquM8xR4US5hyvJiBavZdUj5BAfBLwQbnBA0k8j_Tr8pAciRlgFCTarxtAVaf4Jy5oqrwFfU6c9MUJWo0ir22b3WqY7z-Y3STRQeMnouADuaz86dK7A8WkIEbf8zO2cwUdALPWmkOrEp18p9aq92qLplnybP7ECNEQ0hu3BEXb4DQwdeIKlJYvyrltDxzJUG9wM71_m9xFgQ_teSLfFHX8JZvPGHuE3XLQNkQM_sW4S515O8KE9CnZm7R6cuNV6lupPyf955iXit9Z44ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105623" target="_blank">📅 20:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgECjQm_s5crvmw2WJwTITd4cuCv0DzKrXRxihGYbr81zI8Nu5P6V-hrwlzF9cHHA0c7lKAYeey94zBWkpBX6OAMDWyeSeTTZ9TymArD6deCB_7Xj-5VXjPNZQE2YhwBK_CflOfS-D5xtaZgWPTw3yt0ce2xrA_G8NMWNIiIyWBJzmSrNNm50rAMh6eelq5gPNa6dVKaKMcuAfdG4ZMSD7IbZzGFCgnTlb6-qmYQNw1d-2_ce2RUsIRy_f7t-llo59bJzVa3HeKH4smqe6jGEaHeR7eCiUvxVTofmUnNxnJCJTH02tZWxchB71hM9iVGRv1yowPcvjYm-DrH8GxOWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پایان بازی؛
🇪🇸
بیلبائو
😆
-
😏
اتلتیکو مادرید
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105622" target="_blank">📅 19:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKZfJVbEcBtnjtDoWQhlbPv0Gn1KjDXkt1zFZ8aHBixia9fmf1VZYfVHAD4iH0f1DxWTM7Yjbk0DBXBvlSVq0qtIRTRWwPQeAQHTl1kYhqztRi9i1BfCyxT9wJmskz6HDbw8LoED4RDUKDVPwhkeyoLLeBg4h9AVv4EsiOp21MpBkGAb8lqqDX3dUiW9fkAmIQUsCiJakJ_9XKfROcWenU3-ifrnbYUtlwbvPz9VubK8FcpD3XrYJouO3aTiIH5soMTksnAZfkfgxhPk_nM37aRvO9KRoZRDcZBxAWCS5xXa5Bd8u60_2HC15yS2pbLxqa0D9dW97L-9vksgHZADnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105621" target="_blank">📅 19:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🇪🇸
🇪🇸
🇪🇸
گلگلگلگگلگلگلگل سوم بیلبائو به اتلتیکومادرید حقیرزاده</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105620" target="_blank">📅 19:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a3e6c77.mp4?token=JIFhASOmQR0UDu0wwXZEZ33UpfWc5It4vZZt41grb8I32wIZHgaT8RoK-Vu3Iu_yMXizTT8-fHmLGu0Cd2FPbEHtNyA6eIvqxdYUeJr5zFpwpZJ4GMJjPZg4OwVDskBBR6Te0FqWMCRbkjdzdK__UhVKkeUj6RevsIhyocHos9YRxEygBXeqjkK-DFHLrxKsvDKViFfHj8QCvB6oipgqsEgNxrP4beun-ItsxoN_VPPCkbkauh6s2FqpL0WHg4wt0AVUcmTYdLK8bFXeJwNHItsKypHOrTdoU6RhXMyz46J6Z5s-TelUJDQGqilJl-fqmZ5M-bV3s_F_24ZjDihBCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اعتراضات شدید خداداد عزیزی به داور بازی؛ واقعا بعضی وقتا کسخل میشه الکی کارت میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105619" target="_blank">📅 19:38 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🟥
خبر کوتاه بود و تکراری؛ خداداد عزیزی در بازی امشب تراکتور هم کارت قرمز گرفت و اخراج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105618" target="_blank">📅 19:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQsM-d_Q5P0cd0ihPl_Xl-JuEoO8Do-8irmOwnaVLGyl91kMbjfWOFvD8B4fyrDN3wd3upOO7PngEaJTfzPBDayJPJ4dwhwfuLV2iVWdKtqX3Ejw0fh8T_thoWhA8HpZDuyorSw0Q4YR-5E0TPRO0FaLbXP0N_o9QnoaoJ2CtO5tTvlYV4HRiAiImdNL36PeLTv1vtN1AtwM5xekhOXsNNHuAR4dMh8HB-RMS8NBFcydgnTrTvwwNk6cvhNhlWd8xe2ZP9mNqMaq1DPcc2wJV8BB8AWBUGli3s8Bch6RXeJUr9jznHMeFVXl5NgmHNzj7mx1he-HrL4__KW-P7hicw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تاتنهام برای سومین هفته متوالی در لیگ برتر، بدون پیروزی و بدون گل باقی ماند!
😵‍💫
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 3-0 مقابل برنتفورد.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
شکست 2-0 مقابل نیوکاسل.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
تساوی 0-0 مقابل ناتینگهام.
💸
باشگاه بیش از 300 میلیون پوند هزینه کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105617" target="_blank">📅 19:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
‼️
🇮🇷
🎙
صالح‌حردانی: مشکل خاصی میان من و آقا سهراب وجود نداره و‌ بزودی شرایط به روال قبل برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105616" target="_blank">📅 19:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105615" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhvY6r3v6B-OcfC3h3YfJvFSiK8yet22CYBABCpG5jwbysBf8XZ6oGglCrmypRihQY6PjJN3MRmJT1n_FmoPB0bHw6_TlXlGDKZIb9hP8XEHT04hEP903hj14-qfHNQ18ozEF8_P3HRJRnl7TcX3A7ssaJJTYaTExSWy5pcsEIaKjzPIpys_Tc7JW6piJ74h6S7_7RpN8X_51iTEVv3X6MS981XG3BGW8tzL_HMQ8Lkh4dXFSO495XSTEpL9bGPhsihVPnzTmC4P0SMb7rBc2H1uthaGSRXmaXRUnr_4KnBxPIy-drHVw18466bH0AKuT-CtKfLXwlp57Z2u4TjgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105614" target="_blank">📅 19:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8baa9605b.mp4?token=FxENXGmuD50N_ogIT5ZbqhSMIr83Y7ii6dt-rD1OlWFUr3e6bOxELE2vD0X34K6rAJJUelE2WBF_PJ2hgtSGpFCJiWLnJUj5lwdIt0rUByeix3FLxMUY2BUcF_BhuaKSuTyJkeECyOJ_fuh-A9MuuX1-T8swl35A1wQtBMp3l86xFRU-kC4InvHWV07C_ywkHsGP6O-ZfXQ2k0e6GbRaqRhYCA5yqFZqV-J7F0Lk3OpsInzRUzHbxghm3YslWPw-vR34k96PVTKaEITWFm9gDtMmbe8kbeZDoAdaXpsBkhnP9EEwycPXF44dPDk-D0elg-2HnO9UPMjV2M1MW-05Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
عصبانیت فوق‌العاده شدید مهدی‌رحمتی از داوری بازی تیمش مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105613" target="_blank">📅 19:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Im0APaUhlFgjwTWL9l7UjhZ8CfYrHTBEhFZZa1gJF1FuegPz0M_rI9sPnujvl0BiAXery7hFMO-9Q3jVYrktn798bKOo_rfw3NhENK-44_njXgBriKs37Snz_O4SLQD3aWTwc707UpPrudbfNZhVu4rR4nw7hZs3Rcv1rrMvC1kDI2IZuhedFNwiVDymgkbJySCOb_ozcJ5hcCrnfraJbVt5WAvVo6CqA8rqYA1PbneIuK9I3bbKfSvIISCb99g6F0JwSe6MElvMLFivTar7U59UWO_AT9j_J9QKhlWxGtO7oIpQMYhI4n1vF6ZVXksH_q5qR6TgnUjcY5iQ5UZicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب بایرن‌مونیخ مقابل شالکه؛ ساعت ۲۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105612" target="_blank">📅 19:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cf5064174.mp4?token=Y2PoLTojF5T6yx-ec33f-yyis_MU6PK4pD8vmbDwFJVgQoObqlVXgF_ueaSdhuOWVEANsSOwkZQcG4bvjPP6v1NrIuY80HswEtieOeHt713bXVQ07Uwf8GxbwNFuwMdWrMF5GwNwM4PAZVhvG1nozKwjL1l3gVPr9ZtO_zuzU46f0SBG0vGoX2aIOTLKskAuB_miIBFcRCHwLmTSfFgEMhikDp_xii1RuSIlpiMqikQmTlfMbyAf5Eh5ek7ktu3MF2-LJ5aW97_xKxzP2LWNTvqWsH-SXVmlWzGXa41qnchDGxFvwW6o3jr2S0rppPIPQORmu8KKyHdx5S6bbVMk07mUlQOlkicSYYZ1fiQXuxfMxB8X7YBYYMG0WENOEnomkMd7rw4aEI5WHJ2t4W7pfo6kqzgXy0KS4uQGIG5d0iPDnBoOKxTowm3PSd0v4DRyQAFWk3S9JS9wZNTWm2nQDWeoGXwDzgjg1u8NA2_HjRDOroXIL_e_9JxApmEanOLXLCxNaPrNBYrPkh869nXQOKIZIOnM4BzC3FtozHEThiKQFIbdVl32eKBKs1cW-gqoHzugpHJi3EgnhLDg3jcDYx1w2FDndo3rb3KEayaGkVYnkkjxqrDfC7h06n15mvtj-12lVmY089i0W0tNqTd2jqMuo1KJGZpkItxC5qDm1rI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌دوم بیلبائو به اتلتیکومادرید توسط ناوارو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105611" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d7c282d728.mp4?token=UQuD5rQedljy2-qJj_imBZPCQhY96T31Pjc_KK7_IB9XnTwvvR73M3aZhfwRuS-fGzGFej5Hyq1BYyd_QZ1DuqIPP6yV3zjjLWA9S_CtSH0I85MUTqInw3fPjX_AME08ZKdUYxyyzOFdMDXTaEKiZEXGHUJ4VggQ7TTeDxe8-ANLMDjNbMakgTiYNlNiZUenHlXIM9wvbfY-9lwu1XI0jIt-N2R1297lnIrEudG8L-t0zxkpFHdon9S8TG4csoU5mQXB2FV593WQT2ctpPV3Is6WDvauN6-K-Dt2dIduM2YXhau9D5i0k2FuNKXBtJFwXCnqRfthvRHFZ-ewP3D7szVljGH_wNgWonv09z9ZIpeLbXPIihYZHF-Ku5adWmWvdIb4ykfKk6bBvjn5OJQnuN4T_3lKsC980CehuR_Bx9oDjBxS6I395bvmIjuLzEKrvwb3lvaF3ohbHhn6h_DExERV2F7XKqXh4yOSrls5L0lBvRrLmOpJiLxczH8Ivfd5OHZwE3fdI1cWPsKTHml8oDME3hu-N2xBhq7PnHxfl1zNysvwHlPqRPD0WI0J6JysbcmuZv5BIJFnQafhzNqpNms7vLatzqTBgPVOY9hVVcjMsPA7slLxkQKmUX4Wkd6KX8aIbz3yoAn6egVNH7KdwMSmoLJCltdR3JfvtcNRBbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول بیلبائو به اتلتیکومادرید توسط ویلیامز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105610" target="_blank">📅 19:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105609" target="_blank">📅 19:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9c8ab04f1.mp4?token=XxD3yu5H4ieLGPJECP2rZPAASvMovCAFnIrogF-UvInoLQumKEo9VEQwNfVNOJ1uXgSH-i7nmZWaMGn1BMlz-0ug-1Egbv2PKDRP83RDYTR1bAllQO-Dpl125q5GaH8fjqVrSsuhAxpkQenrkP5vJux9rB9JgLY1ehAP7u2vjfgyEGoKQJWC3wHT_R97X9c99qZtEptFuBnjNFWFVJ6c6Z1z6hMJbRSW4tr8vHPvkOGlRwQqNoJeocAYYZx9Jw0u7IOP2bSJbJImGIpchPJB6Orb8vNUo8H6oOM5e2FybK_drkVuPpj2diJ4GjGsMs8GA6tEbbR0MUtgJ0w6riQleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به گل گهر توسط امیرحسین حسین زاده
روی پاس‌گل بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105608" target="_blank">📅 19:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تراکتور زدددددددد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/105607" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105606" target="_blank">📅 18:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ بالاخره اتلتیکومادرید خورددددد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105605" target="_blank">📅 18:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91e2fe36a.mp4?token=e7WTuTvqN2UkWm1ThPIlwZ0Xlm7dDQZlWwoYnatFC5vajrQ0JeZ0QmgZZneqz9XSrt9iE9DdaKrkChioQewJte8lsm08o5T3jT1f2-xh0T9v2BUqRMbXu8-teXbRzz-Yg8DZVyiLF6WZUOv_t27xIwNPZfMnUZi-bUj_Ie0-zw8jgonbu3myG8-yiwD2x1GatATQhZ3G78PJipIacxUYEU8JaZQz-c7xEhjZqBbH-9HnjhibaV8HoPIyvcwa7t8UVoRe7F8oLrS6NsxGpl7bSZ_vW22WjPCIvxcTIkS4oXRevj7J_k-P33MgxPVEvSHPTbqmlW893rEp0qYaEp5vtEFC1K_oSik-LYZKUWZUJ2rOKEJrh1JIHdKhJtSUlHQWeCYBcgvlFz6_wO9iFX1mLHP9hZM1qfgWoYNFNUUJDkbrcv2uHUpkxebk6qrKTjFH62yEBF2NAyCnnf_XuBrT44SRCyRjk-A-k6mQ02wQfN1pJfIB0ykiW6GLuxYPa4KT9KjM5WTH8vZL_i6NCVURjqE0nt82yJqk0G8HNXeRfNk9X4QZ-Up0y_L7N4FfXB0aGFv2VeMJc8kKWOsGf2yARihWqt6YRSY4vc_l47IzDcF0sbBcl6bHHB2ptKhtifRQ5tmID33pzNAg_AdueXF4ZYjVF4uoL77Q0jhJzE04kBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
تمجید لوکا مودریچ از کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105604" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/105603" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUilMYaeh-pu55GzFoOeduLSsnKIrtaPWdP18BGOzUAsquv3Nzl26Z0urNmcCwE7Eu5mcljcSnQVpHOB5oDDQrj0xTJw8NuKACVN_lRlwYXg9YPacFJ-4nBD6U15TpljPI-VFO2ZP112eY5Rx58M328MBXGBwPLddW3n66tibM2TX1ae-kYbKpKu12CMvFHdge7NWQcYK2ObMIx9xZ3YuW54Vsq4AVz5hTrF7gxBL9ON1lCQ5wZxiwsyqyL4S7IvIYWmXZPgcHmjbm__nQ0v4prFFUaGnfafUKcMzzVSfeeEavLSrbF501rGhwFW4dLseemz5eF-qq9PfTz1WK3IvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب اینتر
🆚
ناپولی را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار دو تیم:
اینتر: ۲ بازی ۲ برد و کسب و ۵ گل زده
ناپولی: ۲ بازی ۱ برد و ۱ شکست و ۳ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105602" target="_blank">📅 18:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=KZwHtDDLADV_bdC76V65W1HHJsOvsIpv7sBbUyNUA3Ds0Q5M7kbKcpFh2u2onJ0ZNLstefM2HUVcDeBP7d9nmUcqIsRWa2m30MQFFxA9BugBVgjNKclcjusYDBtuX3vDEXHKhrI99SHmfFC7XreWS-pqewrCf59i8MY4o2cuIBep3tQbln9xgZRmu-iFQ9M78qCXv4ydmBCD7MzZf04vw_6dzPXvISf0YJJvyq34crrdoW7rI86GGsdm-DTD8rLVZNS2kW6qGkRQAJqfC6WWhFMHW3-cosWBo7GwWpG-ALg1fFdrPIsKQRf9v-qk9EO4E10gErocINr4n99PMYwRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcfbb8df7d.mp4?token=KZwHtDDLADV_bdC76V65W1HHJsOvsIpv7sBbUyNUA3Ds0Q5M7kbKcpFh2u2onJ0ZNLstefM2HUVcDeBP7d9nmUcqIsRWa2m30MQFFxA9BugBVgjNKclcjusYDBtuX3vDEXHKhrI99SHmfFC7XreWS-pqewrCf59i8MY4o2cuIBep3tQbln9xgZRmu-iFQ9M78qCXv4ydmBCD7MzZf04vw_6dzPXvISf0YJJvyq34crrdoW7rI86GGsdm-DTD8rLVZNS2kW6qGkRQAJqfC6WWhFMHW3-cosWBo7GwWpG-ALg1fFdrPIsKQRf9v-qk9EO4E10gErocINr4n99PMYwRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فحاشی هواداران تراکتور به امید عالیشاه در بازی مقابل گل‌گهر سیرجان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/105601" target="_blank">📅 18:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOuhUrCj9iZ2gjmo7rrZxxdVMm5nGlQIyva5k2fOzrivb6RaOgg1uFYocAjc_Hg97wU4LzCxqI3ZruQnVV6jkQXmXJ2ZGDR1HZ4d-KvrZrC0Y5dNirdXmodacHX1NtdJHi9ICojAToiuUelIeTf2klz7iHRAM73UXZgcN7G5VsTuKB-WmiXocyvXEvQQ9-Osi9xF5VtrARu8NABEYcDetHH2ba8HCI7QUEFLmMdYudblxiD94mrsJweAl3lnoK_oDTbuVljMakvKwMyEfJy0iT5gFzxn2fzH9JwI7izF153uubKVxGuK-E7Gs_4TKDw5IzqVcLGqSdmzSqViIADZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🤯
🔵
هالند مقابل تمام تیم‌هایی که در لیگ انگلیس با آن‌ها بازی کرده، گلزنی کرده است، به جز یک تیم، یعنی ساندرلند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/105600" target="_blank">📅 18:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeDjBKTaLxH9AwOf2aEHgPFiAF3JTSwdheAyJWd2KTcmMknOaQCRJSgOOoBJuvb1A1bcOLlJzeDXXWbM1z729rg5j8W_ix1_xdhM_64jZdKg8N51A7-gWGEJnFc3V4KcY-TG_0TKU3OcEhaPykAHFuU-y0YenEZyPWAU8ysRGGD4eu0cDY8pjQ23R-jEBnv6DlzeF2A4vG7tPVqxqiJnVGu9FiDMVUDQTVOo3ri-ROiKtbcBBlhAb_V5cVJMpI18X2ECYKfujFypfEpeeVfouL6q7fGieUG95RMcQcL_7eHkDjY0-hcWJH54lcj0ZQuTSfgqGsFH7BH5OjhWUkS3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
ترکیب اصلی اینتر مقابل ناپولی؛ ۱۹:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105599" target="_blank">📅 18:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvNfsFGk1VeOsneTnnA8O3lQdTLY0pDEy17K4LSl9JjBBAMyccMSfd7c_daBKfXQuYO_VXV6caC9hpYTK5Yxfh109dvQMKUDRm3ybV60dxvBWncjnqPxk57AnrpCCpydJY5kuv-i6pu4HySDSTSLmD_84_l-Ikb8Z19a4oBzDdysGnCkOFUth0EMdEGdoNs8Zp2bkogMbCWSIRl1O7KG9ltHjN5j7cMh1kRE-KM7hBxu3mUnqJeimk4HTXmtnoUWw9svklhbNRGP0cZS3kSPfy2mcItTc32TRy9bj_vS1cZHBJlOZXjcWBGFKjlQPQBidaF0UlHsXPgKwowZ0JoiEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خولیان آلوارز امروز هم نیمکت‌نشین اتلتیکو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105598" target="_blank">📅 18:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=JtqB4C8nV_SLPMNAMYlldBcfOPzaG1HgJIFVGU5xOrmDj4fnRQn5cAWV6ZmsYumnk_-HDHH7WUR8D11790zdh6zA5FrPBSbObJjAZ-KjpRoqXWhPXsJr6zja49cIb3WhshmJ5GjlqonbncX_aKJg_ngeqFmKQPkZK9yl_QQSgWGDNMFGB_fz5coFa2-hDsScfofY4eMO9CD4IxrCsIXNWDHkLLgo2bQdveDHFd--3g5KbpXp3RW-b0kktTK7He8f_623mUjfovCcFfMC960ZP7xECqxHlR8PX6kEg3cRWZVssy9bI35dl0_7OkHZl-B64qWy4M6wmWIs5gS0sOQ9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ffcdccef6.mp4?token=JtqB4C8nV_SLPMNAMYlldBcfOPzaG1HgJIFVGU5xOrmDj4fnRQn5cAWV6ZmsYumnk_-HDHH7WUR8D11790zdh6zA5FrPBSbObJjAZ-KjpRoqXWhPXsJr6zja49cIb3WhshmJ5GjlqonbncX_aKJg_ngeqFmKQPkZK9yl_QQSgWGDNMFGB_fz5coFa2-hDsScfofY4eMO9CD4IxrCsIXNWDHkLLgo2bQdveDHFd--3g5KbpXp3RW-b0kktTK7He8f_623mUjfovCcFfMC960ZP7xECqxHlR8PX6kEg3cRWZVssy9bI35dl0_7OkHZl-B64qWy4M6wmWIs5gS0sOQ9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل‌اول سیتیزن‌ها به کاونتری‌سیتی توسط هالند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105597" target="_blank">📅 18:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
🎙
🇮🇷
حمله رسول‌خطیبی به هواداران شیرازی: لابد پارسال فجرسپاسی قهرمان شده و من بی‌خبرم‌. یا من فوتبال نمی‌فهمم یا این چند نفر هوادار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105596" target="_blank">📅 17:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🇺🇸
سنتکام این ویدیو رو‌ منتشر کرد و گفت امروز سه نفتکش ایرانی رو با موشک‌‌ هدف قرار دادیم
نفتکش "دانی" را در نزدیکی جزیره خارک و نفتکش "استارک 1" را در نزدیکی جاسک به طور دائم از کار انداخت و نفتکش "کایلو" را در خلیج عمان به طور کامل نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105595" target="_blank">📅 17:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇨🇳
🏀
ژانگ زییو، ستاره‌ی 19 ساله و قدبلند (2.23 متر) از چین
🥶
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/105594" target="_blank">📅 17:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105593" target="_blank">📅 17:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWfCwkiNddk1zXLlRtZY6MzltLofp6HQAAA74a2p_XklPCpQzU5rXWrIX4CGkN3L6aH0vZUoEwqMgnkuEqDhLumGpA6uoTUSQX97AseQPOe9TOQYlnzvErSZ3BLd3prdObfWQHbPrrfXfawaZPJQRqKu7jRIo8aRp0ZIhoE4dTX85ou1C5bWciiSfiKRIkGw9IbJrrUbePSfdJkzuViziY8c0qtz6UwFHgNsCG_TG3beUJ3uWJ0amIMS1LGFwhsyIYvhaL9UtxsEEPNJ-oTeA0phL_5NMj6HuVeRuoe0iv1cYBIjRnwDJBG4hvvkbh2SHH3wEQwzvZG_7KDW7oAcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
لیگ برتر ایران؛ ترکیب تراکتور مقابل گل‌گهر
تراکتور- گل‌گهر (١٨:١۵)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105592" target="_blank">📅 17:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=BfsosQeY-dBl6OICbysP4dTAWDSjPCzAO9_IjgdETA3EEKJgF3pBQw7R299uZhU-OZt-Qm6UPMpV6USJwTuYsmxlOXRnwQ-KZ1xQDQHERqGf1t0x_hVTeZI3UOBXgiyTD8vGgkpXPO2cGL-rxDCmeANyzA0eTo7gnYajHmQSw7aa2dJLwwH_FmamluEFck6FMAEPCXRSgs-T5vO8W2GwmT-99XMdwe0jc0t5E7OyreYSArL-cUD8JEL437EIaUTRi-aD-MFjNRlJXLQITjhD3TsjLxT1wT5Sf8I2mshVsR0IDujfqmYVQE9CirrLRdj7UHDYifvy5u9u43X7lynrLoc72Lp4v0lS6kRIq0toWTIafrmMihKSujkXb6UQ081wfNv26OIvZhy_Go6X1wHojnB7jT-j6vEmieE9ML4ysp0lJLZEQoExCL48zvxBF9Igd8EzqSWWlqFh16wIMYRc9E0PL_wsVXZ4JY5iqTEsozsCwXfbE96_IVnd66FB8pM7YCgge0GC1FJkhqmGfg5PDUgYoaKUD2Gc1VBQiylCCxBGgxPxVhIs-eOOPn6OMklnhhg9ty4cnZPePh8g1rp5GRtRuK9yxTElVOTaaT-6Jqt_TWs7eTT-53YSCcQYuqut6bYyMmVXnbjsyztjGCgjDmfRzJm9YXN3432apg8w08U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3805b0d1.mp4?token=BfsosQeY-dBl6OICbysP4dTAWDSjPCzAO9_IjgdETA3EEKJgF3pBQw7R299uZhU-OZt-Qm6UPMpV6USJwTuYsmxlOXRnwQ-KZ1xQDQHERqGf1t0x_hVTeZI3UOBXgiyTD8vGgkpXPO2cGL-rxDCmeANyzA0eTo7gnYajHmQSw7aa2dJLwwH_FmamluEFck6FMAEPCXRSgs-T5vO8W2GwmT-99XMdwe0jc0t5E7OyreYSArL-cUD8JEL437EIaUTRi-aD-MFjNRlJXLQITjhD3TsjLxT1wT5Sf8I2mshVsR0IDujfqmYVQE9CirrLRdj7UHDYifvy5u9u43X7lynrLoc72Lp4v0lS6kRIq0toWTIafrmMihKSujkXb6UQ081wfNv26OIvZhy_Go6X1wHojnB7jT-j6vEmieE9ML4ysp0lJLZEQoExCL48zvxBF9Igd8EzqSWWlqFh16wIMYRc9E0PL_wsVXZ4JY5iqTEsozsCwXfbE96_IVnd66FB8pM7YCgge0GC1FJkhqmGfg5PDUgYoaKUD2Gc1VBQiylCCxBGgxPxVhIs-eOOPn6OMklnhhg9ty4cnZPePh8g1rp5GRtRuK9yxTElVOTaaT-6Jqt_TWs7eTT-53YSCcQYuqut6bYyMmVXnbjsyztjGCgjDmfRzJm9YXN3432apg8w08U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
لحظاتی از مسابقه طناب‌کشی تیم ایران در بازی‌های جهانی عشایری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105591" target="_blank">📅 16:55 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20fca94904.mp4?token=F8heJyvld863DHh9qEad2PIG1NpXp3_yTSkE1qx6iCn6cHhhSu5vrf3oHRiLGQ2hEDcdnCFMKDjfy8h2A1IGB2pecO72WQucp7KbClamb9OjtuQ0wVIwLN7fvitiTVWJgHDPZOVXG7Bta-7cHN6dPZldTdtluNEkysJYwlL5lyUzXxeSDU7xZZrYIa8yN-WwQeW3OroIV3tXjXfqNfRkOrGvKHlB1k9qntr65V0mfEvov3njXRhZiNo0PB-N0CdJws4u5R-MyOM78e2UWRY60366DZbA_DUODhn6PC2QS0r84pfYeb2vcrHn3KM3VBD5uTJ7D9H9yeeONo5VJe6mFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20fca94904.mp4?token=F8heJyvld863DHh9qEad2PIG1NpXp3_yTSkE1qx6iCn6cHhhSu5vrf3oHRiLGQ2hEDcdnCFMKDjfy8h2A1IGB2pecO72WQucp7KbClamb9OjtuQ0wVIwLN7fvitiTVWJgHDPZOVXG7Bta-7cHN6dPZldTdtluNEkysJYwlL5lyUzXxeSDU7xZZrYIa8yN-WwQeW3OroIV3tXjXfqNfRkOrGvKHlB1k9qntr65V0mfEvov3njXRhZiNo0PB-N0CdJws4u5R-MyOM78e2UWRY60366DZbA_DUODhn6PC2QS0r84pfYeb2vcrHn3KM3VBD5uTJ7D9H9yeeONo5VJe6mFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
هوادارای بارسا جلو کمپ تمرینی این تیم منتظر حضور رافینیا بودن. حالا رافینیایی که جلوشون دراومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/105590" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmDgMiU9jDNvo1pCTQQIxw6-dwI6Xjo3e30ePY9GzfP5Ugy8LbBcohDvHM2LG83AWzmqv1tUcdTosxQZ0dnOHhEfUKTHb2jhq-J90Trjkawh02Ku0FS8NWS8CZhn1MWdG4AfzjoPMZqybg1N3GtQGePTla6ZF-WONaDHINY2DtcsdpI63wzaKOHxsfup4fPJo0RUu0XC0HcQauRPbqDcvKf29MzwZ_nQgG59dFSUsKuKyQRqPwcG7pQNSpi-DcHkpNEcRbtE6XdYMfetT6dNyGeGPjOu62GOfozcErC8xM8Z6Py4jZPYY79xad6Pzt3nxAxwY29xmeIAJWoUNTh9pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شانس برنده شدن باهاته!
🎁
تا ۲۰ شهریور
با خرید هر بیمه‌ای از اسنپ‌بیمه در
قرعه‌کشی موتور یاماها، آیفون 17 و PS5
شرکت می‌کنی
🤩
چرا با اسنپ‌بیمه بیمه بگیرم؟
✅
با پرداخت قسطی هم می‌تونی تخفیف بگیری
✅
برای هر سوال یا مشکلی، پشتیبانی ۲۴ساعته داری
✅
و در قرعه‌کشی
موتور یاماها، iphone 17 و PS5
شرکت می‌کنی
این فرصت رو از دست نده؛ چون با اسنپ‌بیمه شانس باهاته
💙
وارد لینک زیر شو و جایزه ببر:
👇
👇
👇
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth
https://l.snpy.ir/ixsth</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105589" target="_blank">📅 16:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
‼️
🎙
مُچ گیری عادل فردوسی‌پور از محمود فکری: کُل دنیا دیدند دارم به صورتم گِل می‌مالم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105588" target="_blank">📅 16:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkYUou5dywXpT6w3DGzI9HVVMldZ76HwFkwdgLUILd8_wF3b2-HZ1LDvbeY7EnmFjglrO6XamcyzJFvJBCnOlFpY4hQQ_IQ9iLOM1_SaVjBbjjcLvYj37CKigk_X2SlF5qSTq55jL5mXODNMS5Ded7NQQ_LxdTDdAdqMWzHUovxFv4RYxF4qyx1BYMpx3uyzv47qMp90042EAG3VM2QKbYs0HnCzzLiTzlrZS2xWQQ3XW7cbuiasOQWGL4p-PnoCM9qqKeitCmR61bhG9MfI5W6JA3u3rHm7e-BG3oXOagiruH0paKOMSR8ehK6vx33twQ6opjB-IZaTDWVN6-6Jtlt0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29285b8410.mp4?token=IZGXPQ1KF3hBGTmGPpU5oo143t6kVMT4cgel7gt-saTlzVn0bBR1D7cn8RPqQY4XP5n6d87cByXIqFchhmNE95mEkQJN2TstkqMuCLGlSlLcbJI-jZW2pMcPtoPs3AipHARYIPjunH-UN_JISXNpsYrTRoDJN_pw5OpyWPZ1a66udJ12_zj9wKkGh5oKqx9nYeoFeUsrlWHqyBYEaRK0Dhb3xRD-G3nkTV2SQTSsBxCwBIQhQlKxscAscTlxyavbK-RCN3D5_UyMk7GB0UUpDoaWu_4tlobnTvB4MTDKVVdXZomODSiRWGuaIpzlKCcrWCwM39bn_1Rv2UTex9qGkYUou5dywXpT6w3DGzI9HVVMldZ76HwFkwdgLUILd8_wF3b2-HZ1LDvbeY7EnmFjglrO6XamcyzJFvJBCnOlFpY4hQQ_IQ9iLOM1_SaVjBbjjcLvYj37CKigk_X2SlF5qSTq55jL5mXODNMS5Ded7NQQ_LxdTDdAdqMWzHUovxFv4RYxF4qyx1BYMpx3uyzv47qMp90042EAG3VM2QKbYs0HnCzzLiTzlrZS2xWQQ3XW7cbuiasOQWGL4p-PnoCM9qqKeitCmR61bhG9MfI5W6JA3u3rHm7e-BG3oXOagiruH0paKOMSR8ehK6vx33twQ6opjB-IZaTDWVN6-6Jtlt0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
خاطرات شنیدنی ستاره سابق آبی‌ها از دربی شش هیچ؛ قراب: همایون بهزادی زبیاترین گلهای تاریخ را به تاج زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105587" target="_blank">📅 15:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=IZmY_lGtm_I6jlmMpLYqORlWhfWa3SR3F5C-i-v5vp3Z5NbQLkK888LT1jwuwDsUobERqNbRJb8EXyDJbB_mH9QMpKTpnPa_JKzAC64DTltxDBsyYM5wOUY6DLOFnL6e_Tpie5s2uIiliFYqeFopEPpfFZEYKXYz2vvzlw3NAKzPauesIM2eT2hBv5wkPLCjD4NTcCCwpX_4MluUpBsbQ_91xqgjNrmwE6eT3KWjE6iStbMxIAYUycTwnWDPUTyieln8WWUjqU2Rofup8uPie1vLtICbqZXVpmpEToGd7kMpaDyet5yzGk1KCudsoHL4y1kB4DRpOUkqTle32YUSkDFCWWEWdExsFynYM-DxxaIqeB2_DToAi1xjaKxkIbDoX5l4yGwxZkA00q11G6k3A7iYzK3ZXULCbr0euzDs6c5rFbxJGfWSynNPS1qbSa8k7vMzDwi4p-L9IMFdKor9DhwAeVqEwaplvJumtI6j49XblVqlZLfnm4tFtnqBa-6ofBoYZ8f2l-_s5StbUpINEcS4MLCw6joJ4ZQCe-eO9ChGdvc6MBebnppSKSO6jXZHBabPZ05Bzc9RUvnVtYQSu99dXHFjqdhmOJhOmkMpQb0puOrb5pxtlmZOEYrOHyEwtHVpRFO-6oVF5AZVGHuzJ-EstDiCDiHWcK6W6MnJ0aY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59ae44943.mp4?token=IZmY_lGtm_I6jlmMpLYqORlWhfWa3SR3F5C-i-v5vp3Z5NbQLkK888LT1jwuwDsUobERqNbRJb8EXyDJbB_mH9QMpKTpnPa_JKzAC64DTltxDBsyYM5wOUY6DLOFnL6e_Tpie5s2uIiliFYqeFopEPpfFZEYKXYz2vvzlw3NAKzPauesIM2eT2hBv5wkPLCjD4NTcCCwpX_4MluUpBsbQ_91xqgjNrmwE6eT3KWjE6iStbMxIAYUycTwnWDPUTyieln8WWUjqU2Rofup8uPie1vLtICbqZXVpmpEToGd7kMpaDyet5yzGk1KCudsoHL4y1kB4DRpOUkqTle32YUSkDFCWWEWdExsFynYM-DxxaIqeB2_DToAi1xjaKxkIbDoX5l4yGwxZkA00q11G6k3A7iYzK3ZXULCbr0euzDs6c5rFbxJGfWSynNPS1qbSa8k7vMzDwi4p-L9IMFdKor9DhwAeVqEwaplvJumtI6j49XblVqlZLfnm4tFtnqBa-6ofBoYZ8f2l-_s5StbUpINEcS4MLCw6joJ4ZQCe-eO9ChGdvc6MBebnppSKSO6jXZHBabPZ05Bzc9RUvnVtYQSu99dXHFjqdhmOJhOmkMpQb0puOrb5pxtlmZOEYrOHyEwtHVpRFO-6oVF5AZVGHuzJ-EstDiCDiHWcK6W6MnJ0aY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پریمیرلیگ هنوز شروع نشده، جنجال‌های داوریش شروع شده!
⁣
🎙
📹
مایک دین، داور بازنشسته پریمیرلیگ، توی مصاحبه با پادکست جیمی واردی اعتراف کرده که زمان داوریش بعضی وقت‌ها برای خودش چالش می‌ذاشته؛ مثلاً ببینه چقدر می‌تونه بدون سوت زدن بازی رو ادامه بده یا چقدر می‌تونه توی دایره وسط زمین بمونه و ازش خارج نشه!⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105586" target="_blank">📅 15:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rLuvCXgb5px8VqxP0tR5o2yQIr1Ntlnv-3PhiHuTuMBzGbDD4RkbXgBqU9gFhrn4YgT8hdMeymv3izuWUGVB-7pAjszePxlOxFt4fl7fipcVoVlgqua2i0yEjEE_qr2ZfBJybmw6E4I-mfG39BIZoWpfgaRLqnTgXg3aYF1rxfzYqcqebyY_cbfS4vv2yQxraG9R1alvcs1YLbpmHrJu5Z8Oiz5LeqJ_UVihnccVyu0IT8DS4Z4_6_dD8AH_bV95TTAQKAXJVQKIjACBvQ7sQIG5ObCG4Fg12nDHeSXFfMaFZ8RCskood5Pfq7FG4ErsxN1J4agCBHOVMebC5PlZwlo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rLuvCXgb5px8VqxP0tR5o2yQIr1Ntlnv-3PhiHuTuMBzGbDD4RkbXgBqU9gFhrn4YgT8hdMeymv3izuWUGVB-7pAjszePxlOxFt4fl7fipcVoVlgqua2i0yEjEE_qr2ZfBJybmw6E4I-mfG39BIZoWpfgaRLqnTgXg3aYF1rxfzYqcqebyY_cbfS4vv2yQxraG9R1alvcs1YLbpmHrJu5Z8Oiz5LeqJ_UVihnccVyu0IT8DS4Z4_6_dD8AH_bV95TTAQKAXJVQKIjACBvQ7sQIG5ObCG4Fg12nDHeSXFfMaFZ8RCskood5Pfq7FG4ErsxN1J4agCBHOVMebC5PlZwlo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOVkJ8g8HhUFyRxoRGptb1Z2Gm_g3D5SLWRWRiom-papcaUyHCA8lxHsVQh4FY3O4LhTDorgnpcAyG_ZVwjzZM2iTH3QhPdDWjG24m3vj9DKykjv_oI7mXQEkU7T7TdqsnCuEqyULTJcOmYgq61_9GEbl3pI6Y5atLrTXsOKrgqlCu3PKIUwndQicDPx9nuHBQi_382ho1FRZj7R5gBj3QG0_cNKeKFvuksoc_ynwMg5lyJa9QkDqOIXhleIInAxIuSHmdxRkjJubX8TLTCZFZkRCf-uXUTAQV_jNyjW2GRWg10hpKItw17Nuuj0PfC4U8F1ksSEJn4Sd1mGis1Spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=oRNs2_8FVVSsTponoYxwiFuZ4-uJyCr9yJ7FyiU4jONilePX-EczUqCmVw8-pYhMRkqsK4pRoxDoq6gDuCfftx8Iz02hAB0StttKVHGEYrZVIZEDnrfwFMOd2wb4y0Hw9r5Ee6oCxVwQSGcgup0igurv8_Za1Q2TsIUv7l1R_dpTfbogC47v7wWIXlg_U5iT_nm1e_afPnGMggZffy_G3PN129lxjHgdQBikAyDYBIxkYbHI91TGVgnFL1kjy9yM1Y_pwveJaVjJYXN00FkJSx0Ed6WbJqhkTaMJj3tPbxbNE8nvZ0muUOBVuNYXl0ZsW5pMdRQ_9PPzqVT5j9ZkoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=oRNs2_8FVVSsTponoYxwiFuZ4-uJyCr9yJ7FyiU4jONilePX-EczUqCmVw8-pYhMRkqsK4pRoxDoq6gDuCfftx8Iz02hAB0StttKVHGEYrZVIZEDnrfwFMOd2wb4y0Hw9r5Ee6oCxVwQSGcgup0igurv8_Za1Q2TsIUv7l1R_dpTfbogC47v7wWIXlg_U5iT_nm1e_afPnGMggZffy_G3PN129lxjHgdQBikAyDYBIxkYbHI91TGVgnFL1kjy9yM1Y_pwveJaVjJYXN00FkJSx0Ed6WbJqhkTaMJj3tPbxbNE8nvZ0muUOBVuNYXl0ZsW5pMdRQ_9PPzqVT5j9ZkoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
آیا پنالتی امباپه باید تکرار میشد؟⁣
📹
تحلیل صحنه پنالتی توسط روزنامه مارکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105583" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PnIrf9icKz955TsYuNiz1cX_unNTDUosFyThx904Xxx6e-VcqL0loOIsT0sPMsZ1tWZvwU5LzHJov0fvuI7RT03RSnbNWFwXUYcppmE_4NKcCCavo9AIBj0p48QAokyZjsJLk8fqDMNu2fPq-aCCwdZeoknPHShOGh_wVRYj1PYs9bPR71S8YxBNbJuvzNGo9uBgUg_WaULlUfgukrXr278WYeojXdUo5CbOpHeBfBMb9hBBbpKDru6PNuocBzvIazQHGhx8vQ-mK-mIeCn6QMylG9uxAsVn3hO0NTXKpFw17Qqz0mft9zaJaKhwNBgZ-Z6q0cWxppm3eoxFlf4XtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PnIrf9icKz955TsYuNiz1cX_unNTDUosFyThx904Xxx6e-VcqL0loOIsT0sPMsZ1tWZvwU5LzHJov0fvuI7RT03RSnbNWFwXUYcppmE_4NKcCCavo9AIBj0p48QAokyZjsJLk8fqDMNu2fPq-aCCwdZeoknPHShOGh_wVRYj1PYs9bPR71S8YxBNbJuvzNGo9uBgUg_WaULlUfgukrXr278WYeojXdUo5CbOpHeBfBMb9hBBbpKDru6PNuocBzvIazQHGhx8vQ-mK-mIeCn6QMylG9uxAsVn3hO0NTXKpFw17Qqz0mft9zaJaKhwNBgZ-Z6q0cWxppm3eoxFlf4XtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
وضعیت دیشب فوتبالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105582" target="_blank">📅 13:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU1hTulGWTFfKcn6yMX3_GiSAckZfGmQlucrIMuU8ckENwp-awtx6Idq8bTdL4zgoHjcglY7ZtxWDHpcvGVvu5rzIFqWf9kA93aaK7PBwMW5YiaZ6e1ASP6J9QjImjocHxbMzK0twRlASdiw-nrKwVNAo_97estdiWAP_bdj0mYtdCWf2jjnr7isK9NgUQSQMHZyoBDR56x8dlfSfJC_1iI-IyQaDlPfhWUxMA3i7LmhT6i0O_67mxhU5ZViPf2LEz7Dj-G9cY8JkfZ4Z4PlB50V4mUpiED36tsd73NjpYT7b60t2GRg6Rxcmh1sz_k_F3hhJpXIoF8b5ps0p6L9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
20 تیم برتر جهان، رتبه‌بندی شده بر اساس ارزش‌های بازار، طبق داده‌های سایت ترانسفرمارکت
💸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105581" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105580" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105579" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
‼️
🇮🇷
سهراب بختیاری‌زاده درخواست برخی از پیشکسوتان و بازیکنان استقلال برای بخشیدن صالح‌حردانی را رد کرد و نام این بازیکن را برای بازی فردا مقابل آلومینیوم اراک خط زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105578" target="_blank">📅 12:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/105577" target="_blank">📅 12:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🇪🇸
لامین‌یامال در آخرین تمرین بارسا پیش از بازی با والنسیا بدلایل نامشخص غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105576" target="_blank">📅 11:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrehOSHXRm0rXnDIPY2AAVJdspAmeWekOO4BDfbhxVhwD1zk4ZuyJGp96WlfMmGa7S4f1I7yeKk3eIr5NU7AJSbhLJ1EDpmT0vQhlFOXsSFIg8KdTl-vtjqJWjN65EmG67qbi2qwp4qFk8FhZKepPavs2JNoZzVGDMN8Q5QGGLOnQw9kWGpX6G0hMCdzO6s38T13ksxtZlWOVhh5AcopC3LOtHFt3A-HIDnNp0pQSpbG1qfe0-oE068keh-kZRUxbsvsYEkrI055G-nlDq3lgzLDrierpGEdJZVMtkN2Rk_6Rp-V8vbl-agANBdpn_Nz3N8li_y1IFCy1cYX2WynXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج رئال‌مادرید در ورزشگاه بتیس از سال ۲۰۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105575" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
زوج فوق‌العاده پشم‌ریزون ازه و اولیسه در تیم کریستال‌پالاس دو سال پیش رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105574" target="_blank">📅 11:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105573" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkZWU_QNCD33cyP0w6NcpHrxfo2qZsnYSysN88hlfM4DE7TyD1y1gtOkIiKcIelbNhQUf9ngqcFhvqFLeBG0ZBd_SFjaUdNUfzHaTfActEhH9QLtqQ3NoSWW1wbS3YfWLpSEd2xo0BcJElQHE74cKrrLXURQcFbNHDpW4X9WSrVwQ54tGpnmptW696VAg-X4hzFt5img95CUON9lT3lr3Qkppz4AiR7TTSu-6m6OLoD06_eRgQOCPcVo2Txe_GsuuZeQwEBwVWibH6sg309PFeamFlVhK7t7yb2mvX2cFNSDm0wsKswp2vGcVobNNs_7tmW9Ovq5pscWXaGanKIdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105572" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=QEb2bJAw1ai3Rg0r6ePB1RBR1IjjhgG2VyZ0Ew3XBrDTuZ1nv-PH0euUNqwjCRXyJC5YUBaqSwbgTCu48Yd9JLNA1tA6aGL0wGREh8Ou6OqTNe-pEd_5Pd9JrkJaVjX4-m3bg-AfX3psBGCcNDrP2_Lpx4u5Qj-F462w3dOUA6XMejEGgBEeytB0xcX9pr-EF6zP34oWn4d-h0_GgI0fOpxqpIsJ_wprr8i_VLCRxhRISfbKxadyisabrYwRyRTbVQK6pa39L51_SsNWaE5MHujDujyrqDhZLFpNnLZAUF0pj-AB8HOKJAKKWFPsvv2CgvzOVYOQBEoi2wyz9DzkHnlEFBuPU6iqc6riV6w6NJyfc22m8SwFZwlsktfbduj0BxZMs6a4yiEsY8aRMoRZZf9EXzNfkhVbMK2CiGWKIkAa_wKkSCUqvfUlSGPiE3eV-yuYDsTp0n7RT37fRd3Vlbo_Xwdx2n0hjHlkJJ14KOpxt517cK84_9huxs9syGwGgEGJiY2w0K2gsW6gsqB-LRezPAEQM644FvSGMneSJ4qeEGYobDcW0ELH5a3_oaQf2bQb-wvlm_oaL6ynDD3yA4zd6n8J10bAfTOHo_kbeeezpd4GwjoxeA8n5-y0QE63WhWuNV5ITJ7Q0fvHsfCcbTYBFuSbY6jcfznO7CITpJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=QEb2bJAw1ai3Rg0r6ePB1RBR1IjjhgG2VyZ0Ew3XBrDTuZ1nv-PH0euUNqwjCRXyJC5YUBaqSwbgTCu48Yd9JLNA1tA6aGL0wGREh8Ou6OqTNe-pEd_5Pd9JrkJaVjX4-m3bg-AfX3psBGCcNDrP2_Lpx4u5Qj-F462w3dOUA6XMejEGgBEeytB0xcX9pr-EF6zP34oWn4d-h0_GgI0fOpxqpIsJ_wprr8i_VLCRxhRISfbKxadyisabrYwRyRTbVQK6pa39L51_SsNWaE5MHujDujyrqDhZLFpNnLZAUF0pj-AB8HOKJAKKWFPsvv2CgvzOVYOQBEoi2wyz9DzkHnlEFBuPU6iqc6riV6w6NJyfc22m8SwFZwlsktfbduj0BxZMs6a4yiEsY8aRMoRZZf9EXzNfkhVbMK2CiGWKIkAa_wKkSCUqvfUlSGPiE3eV-yuYDsTp0n7RT37fRd3Vlbo_Xwdx2n0hjHlkJJ14KOpxt517cK84_9huxs9syGwGgEGJiY2w0K2gsW6gsqB-LRezPAEQM644FvSGMneSJ4qeEGYobDcW0ELH5a3_oaQf2bQb-wvlm_oaL6ynDD3yA4zd6n8J10bAfTOHo_kbeeezpd4GwjoxeA8n5-y0QE63WhWuNV5ITJ7Q0fvHsfCcbTYBFuSbY6jcfznO7CITpJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
واکنش مورینیو‌‌ و نیمکت‌نشینان رئال‌مادرید به پنالتی که امباپه از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105571" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
✅
🇮🇷
صالح‌حردانی که دیشب یک استوری در حمایت از سهراب بختیاری‌زاده گذاشته بود، استوری خود را حذف کرده! با این حال سرپرست آبی‌ها به حردانی اطمینان داده که تنها با یک عذرخواهی ساده می‌تواند به تمرینات تیمش برگردد که تا این لحظه این اتفاقی از سوی حردانی رخ نداده…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105570" target="_blank">📅 10:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=dMfZnMgZwl3FI0pFkp4umJJ9_lE1XwkWiuMc96JdpBMNc1yPVkzUoiMu_RzBFuPg29Jev3b-CYv7yjbsJFIddLpWxml476YZ9D4ls-LiJbjnfEDZLcm4a5ixefemZG-7UoSRrmjYuL2qObgJYTmcSDXYeuiavQSfqPZG-EyDMh8KrsC8c3kkbAd3f4bfkTMzl8NP1zGa9ZZTGWOa2hceW6mf5-dVrU428-XkPCaZUNjVnT2Bo5CAhOJXowphpTdF6wScQwN1fRPjyHFplXrAy5zAU7GJn2auFZh41zt8grBDQ_EkYElNeVCSR7g_2EZk8mDKm4FYn5VAhrz8f2Fe0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=dMfZnMgZwl3FI0pFkp4umJJ9_lE1XwkWiuMc96JdpBMNc1yPVkzUoiMu_RzBFuPg29Jev3b-CYv7yjbsJFIddLpWxml476YZ9D4ls-LiJbjnfEDZLcm4a5ixefemZG-7UoSRrmjYuL2qObgJYTmcSDXYeuiavQSfqPZG-EyDMh8KrsC8c3kkbAd3f4bfkTMzl8NP1zGa9ZZTGWOa2hceW6mf5-dVrU428-XkPCaZUNjVnT2Bo5CAhOJXowphpTdF6wScQwN1fRPjyHFplXrAy5zAU7GJn2auFZh41zt8grBDQ_EkYElNeVCSR7g_2EZk8mDKm4FYn5VAhrz8f2Fe0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
اولین شکست فصل رئال در خانه بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105569" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQXZLKOozhID2sbLhADObvbb9RbgrZD2abGubfLPichqQUVvE6jWCKiuTzbIMkEC0EaTxXujMHA5m4NugSEZc8VKFEyF1nwnpLkJNqg0KAnx82Ne_nAUOn5YP-i7daV0InKvbyKlZLO0n-ON7a_H9T4mzrQI3gVtWdSpj2uQOLgnfHGnrNI8nhyKFu564btBDI-kL4YXsXXRf593EntdK_Qqv4ykyg-6QZRzGTMGTQkWL08iSctJKZlokB6A55jYWZ03Na7xKUhvU0PXYckUe_MsiXi1kcYK1z8vihqNcgmiR6ql6-v1_hbfX_HkefRDf0M8B-9nHRMC8vhU5tHYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇫🇷
لوئیز انریکه درباره نتایج ضعیف تیمش: اگر دوست‌داشتید میتونیم روی قهرمان این‌فصل فرانسه شرط‌ ببندیم هرچند که من شرطی که خواهم بست رو لو نمیدم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105568" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=Qnb289lJilqNXfxTHv0TyiBQyo6PGfdgYSEk7a5MlTtfZRw-EdLgyFtk4YzKfUPZixzhVAujWWURv5PNLknwpRCFgpfdfxo5VO-g99fqeiCrh3axN68wXzOJVjK_NOY6Rg63uenmo8Iwctg6x261aobAMPlXuUi9UFaspPONj-cstE8rRBYCEpRzXS0LP9HnipmbPgzXxQ9no4yb_W_q_bTy3_PsoXXLAp1TkzFg2f30CqV60TGh0pE9YF4KklsBoisiqGTZNIduAFSo0F4P-nIIF_9oVGn9cKpSwmLoskL4cT-YkAZnqXfJx5t3yaULEoc63VaWLG_DyDV4DWDTrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=Qnb289lJilqNXfxTHv0TyiBQyo6PGfdgYSEk7a5MlTtfZRw-EdLgyFtk4YzKfUPZixzhVAujWWURv5PNLknwpRCFgpfdfxo5VO-g99fqeiCrh3axN68wXzOJVjK_NOY6Rg63uenmo8Iwctg6x261aobAMPlXuUi9UFaspPONj-cstE8rRBYCEpRzXS0LP9HnipmbPgzXxQ9no4yb_W_q_bTy3_PsoXXLAp1TkzFg2f30CqV60TGh0pE9YF4KklsBoisiqGTZNIduAFSo0F4P-nIIF_9oVGn9cKpSwmLoskL4cT-YkAZnqXfJx5t3yaULEoc63VaWLG_DyDV4DWDTrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
به‌نظر شما دلیل فحاشی به شجاع خلیل‌زاده در ورزشگاه عادل فردوسی‌پور است یا رفتارهای او در داخل زمین؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105567" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=uj_moYmBuaaHtS7ZOfPr3nzgMlSbQX6dy-lHViJw2RQ5UaxGSnLOpY6hRphuAbCcyZ_gCbp-qyt1Jsz_3EFcQ_kW37tAQSf2N6dY-o4qu-r12P_x33ub8tgJod6HH5YosnX0shiX7d_c64wWiweuW1HQOPsB1zaRVXGpQE5ZyY7M27ALe6QNDLr9h1NEnK3LUW90cAeybO_K7cbH429J2Ru-d5KtYFzm_IUzPhbyBwYpmny0VN9teBqXr7gZQQGVsdM6cI2D18mqFeXxhZlUpVPF5ue3iPMiNEQxEHt3QzDzEyWQh3wKaWnXhUStOdKwhRhQpfs7SPLAfLXpdqVV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=uj_moYmBuaaHtS7ZOfPr3nzgMlSbQX6dy-lHViJw2RQ5UaxGSnLOpY6hRphuAbCcyZ_gCbp-qyt1Jsz_3EFcQ_kW37tAQSf2N6dY-o4qu-r12P_x33ub8tgJod6HH5YosnX0shiX7d_c64wWiweuW1HQOPsB1zaRVXGpQE5ZyY7M27ALe6QNDLr9h1NEnK3LUW90cAeybO_K7cbH429J2Ru-d5KtYFzm_IUzPhbyBwYpmny0VN9teBqXr7gZQQGVsdM6cI2D18mqFeXxhZlUpVPF5ue3iPMiNEQxEHt3QzDzEyWQh3wKaWnXhUStOdKwhRhQpfs7SPLAfLXpdqVV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‌مخ زنی به سبک مهران مدیری در سریال جدید مرد سه‌هزار چهره: فقط اونجاش که میگه برای من منگنه بشید
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105566" target="_blank">📅 09:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=Z5S0jUwVJLyOMUxuZuAGQ64ooOauBDpywLWNeWBYtlg9wiIY5TAYHSoNG9nFEW6y0f_cKCg90qfb29KLztONxiPY22PFkzjOpo-3PcSehti6Z9uctecw4HHoMVXKLa5gWAWM-Aw2P20HC9oCAkJTdujLicXXEiXP7DO95s1D-P7ABY2xHCLdMSYjgs4ZBryzZEEiZUUI39uol4IMVoBwjKYuEg0IbksAg_j3ZmBNaEk83H3u9zHhgEVwD1jrDPEgRpExV_zrEd24UUuckUhvVIP21gYPgtwqznkNsIpWHZlwHd53LtjLDBPPgNFNqVHG_R2TOzPyke_JLOasScfEJ7CA8rfItWVWS_GkUuuuj5AYLpgzdz45MQ1pZwg589nF-cTbpBSxYd7diqRutkcsq7GVqrDRcWZMwXhM5v9SvSbsL6p10LzM4ewZhbt_sOXuaMxsq3E2bWMoCQhyqCUoWYz62xjMcynFgSU6Sy52tpmBUeFd47SkIBuCQ6mhOwlcjVJV0xtF1lpZ2PZ80bftJOPavYSUe876vPAVislDKolk0ZnHUie4XdzqYfIWSxDvrtGe9EJyMMMZzthXk_-wAtqGk5oihdOtNc12EkRbASx_eKJBXL8vvYl7HweA-Vxb1IUDyxzG6CzNdNivdBRuaMN-6pkbyggigcyeld28KdU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=Z5S0jUwVJLyOMUxuZuAGQ64ooOauBDpywLWNeWBYtlg9wiIY5TAYHSoNG9nFEW6y0f_cKCg90qfb29KLztONxiPY22PFkzjOpo-3PcSehti6Z9uctecw4HHoMVXKLa5gWAWM-Aw2P20HC9oCAkJTdujLicXXEiXP7DO95s1D-P7ABY2xHCLdMSYjgs4ZBryzZEEiZUUI39uol4IMVoBwjKYuEg0IbksAg_j3ZmBNaEk83H3u9zHhgEVwD1jrDPEgRpExV_zrEd24UUuckUhvVIP21gYPgtwqznkNsIpWHZlwHd53LtjLDBPPgNFNqVHG_R2TOzPyke_JLOasScfEJ7CA8rfItWVWS_GkUuuuj5AYLpgzdz45MQ1pZwg589nF-cTbpBSxYd7diqRutkcsq7GVqrDRcWZMwXhM5v9SvSbsL6p10LzM4ewZhbt_sOXuaMxsq3E2bWMoCQhyqCUoWYz62xjMcynFgSU6Sy52tpmBUeFd47SkIBuCQ6mhOwlcjVJV0xtF1lpZ2PZ80bftJOPavYSUe876vPAVislDKolk0ZnHUie4XdzqYfIWSxDvrtGe9EJyMMMZzthXk_-wAtqGk5oihdOtNc12EkRbASx_eKJBXL8vvYl7HweA-Vxb1IUDyxzG6CzNdNivdBRuaMN-6pkbyggigcyeld28KdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
باشگاه نوریچ سیتی هر سال نشست خبری ویژه‌ای با عنوان "نشست خبری با قناری‌های نوجوان" برای هوادارای نوجوانش برگزار می‌کنه تا بتونن مستقیماً سؤالاتشون رو از سرمربی تیم بپرسن. امسال هم این برنامه برگزار شد و البته با یه اتفاق ویژه همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105565" target="_blank">📅 09:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=CRZI3B4xq-G09zyD9793L1_ucH0GUEPCWPu2bcrsab__pnVSpj68lCtE0XKj_dDnHB2-CwKIomMA4QZ3FXZOj2cLZbjrvrGd7b7L1OdC-Nm76aPIbExgcz7GTnDwnmrVMTRXNal4ofDBYoxRoJuBaXmSpO4mzLWFrGM60mEK_t55jdeK_I3EyT9jv3zWDaYudypqa_8c2FJw8rSK4_nz5f4hxKtxwfLxdc6fY3FuPUH1D3iCbGt_HxTiYLw_v4ZidgKrXesgoAMfNpdta1EztUj5C1bgBg9cngIPqxjK4b9gEHupv2ItbMT_en4Flsj1pcvB7njmrkNrrWrh33qkgRBS8Gj-6EUrkSYOM5aVvGXsGS6k3ZfKmt3MqoMtbUyU_Xh0Fy3dRGiKnqKi4-V0Ec2wmeCW3-OHBbtXfmP42I8Lg-6jnUk0X27iS9EPurQE89GGI-kOVpjDrljpznArGnomGVbysmUH6K3Oh0KHPnqqECUAOzbMZ820Scq0JpROTK90qLeKBSo1-dmJWPvvU_8bnK6r-9fIIKzr_cviCFkC3axaH_vRUomLFsg7qUQH-2oXHCdNWcn6xqqEHlwSi-g5qx7y2l2HyAmGFlUk8oMfMF4oujeY21kL2JG6aF6lUeC5X8Ee9UwRYiUbV0SYvuQd3fn8w1DrvC0uLrE12ME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=CRZI3B4xq-G09zyD9793L1_ucH0GUEPCWPu2bcrsab__pnVSpj68lCtE0XKj_dDnHB2-CwKIomMA4QZ3FXZOj2cLZbjrvrGd7b7L1OdC-Nm76aPIbExgcz7GTnDwnmrVMTRXNal4ofDBYoxRoJuBaXmSpO4mzLWFrGM60mEK_t55jdeK_I3EyT9jv3zWDaYudypqa_8c2FJw8rSK4_nz5f4hxKtxwfLxdc6fY3FuPUH1D3iCbGt_HxTiYLw_v4ZidgKrXesgoAMfNpdta1EztUj5C1bgBg9cngIPqxjK4b9gEHupv2ItbMT_en4Flsj1pcvB7njmrkNrrWrh33qkgRBS8Gj-6EUrkSYOM5aVvGXsGS6k3ZfKmt3MqoMtbUyU_Xh0Fy3dRGiKnqKi4-V0Ec2wmeCW3-OHBbtXfmP42I8Lg-6jnUk0X27iS9EPurQE89GGI-kOVpjDrljpznArGnomGVbysmUH6K3Oh0KHPnqqECUAOzbMZ820Scq0JpROTK90qLeKBSo1-dmJWPvvU_8bnK6r-9fIIKzr_cviCFkC3axaH_vRUomLFsg7qUQH-2oXHCdNWcn6xqqEHlwSi-g5qx7y2l2HyAmGFlUk8oMfMF4oujeY21kL2JG6aF6lUeC5X8Ee9UwRYiUbV0SYvuQd3fn8w1DrvC0uLrE12ME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: مردم فکر می‌کردند این آخرین جام‌جهانی ما باشد. میخواهیم در جام‌جهانی بعدی هم باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105564" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=HyPkFoOLkS1Xco2EJ7HAJ21JLaxmnXi2_UAEOqN3zLtQeu-Oz3W7uh5dsfGdTzfDMPot4Ar3vDZ2jlTlYC-MnaUvlOuGiI8rVUcw6QPAA_MC36pP8ugY1c6J4qxogY-XCkxSq2isk90kN2dPHq2f2K3TBGsuO6ubdZLpNCEmvu7Ksbryrb_KYlCzFgGPnxnlAxWshhOW3shGLlFl-nnCB509eh62vSD1KSOLo3tpEgmHXHEWYageMLC_Y8ShgtOcVpDNVW0xt7cYZ3zvFgEcudsbPEw09sfSkVGpQeGAZ9Fq9IFNMfoY65H24Wgbfu_IkRgRH0Vc-c8RyBMBsJiRdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=HyPkFoOLkS1Xco2EJ7HAJ21JLaxmnXi2_UAEOqN3zLtQeu-Oz3W7uh5dsfGdTzfDMPot4Ar3vDZ2jlTlYC-MnaUvlOuGiI8rVUcw6QPAA_MC36pP8ugY1c6J4qxogY-XCkxSq2isk90kN2dPHq2f2K3TBGsuO6ubdZLpNCEmvu7Ksbryrb_KYlCzFgGPnxnlAxWshhOW3shGLlFl-nnCB509eh62vSD1KSOLo3tpEgmHXHEWYageMLC_Y8ShgtOcVpDNVW0xt7cYZ3zvFgEcudsbPEw09sfSkVGpQeGAZ9Fq9IFNMfoY65H24Wgbfu_IkRgRH0Vc-c8RyBMBsJiRdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🔥
جورجینا همسر CR7 با لباسی از برند گوچی در هشتاد و سومین دوره جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105563" target="_blank">📅 08:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoKer5EZhekg8pN12V9x-Pl_-MoU0O2xoaYYb0S3kbalXckAqon2ZDwvNW0jTyTQite0nbCYkbs4W7Rr-vXseqPD7RXggzvDoG47xIDV34Bf-M8TTYy26I1LcQVdQXsOKz3P-Di8kpEUpZy2uLfCuZhPFrCsT9kioFIvztGK8FWR5RG2jNK2SikQfFY8m_T33zmN0ztb2fPYx_73hvZrdIhVMxfwbPaV8EAtWZ37uhe6Fl1E3WSASTZolyGxd9eCXCQSchIfzmJ1B-yLuoj9WibTfc83R9A_QRSnu86MI_27K4eCWfM6hID1MoizQJCc2QotKCbrawhSqQV6PC_h2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=WFWl3-VpiGK10HLwheaWhBzXiFzoZTFO7upg0ufYCdzXYlGBDUYQGPYlOp5Hh9UwIkp51To2yRC2oU7c0FJu6SYHh2SnBjr4UyRfGi5cxAP8zb4KJat4EXNBIkhFNo6TRSAa6cW9H24wzNxLX7URiAbUZ35a43xlAHMdvrjziLC02aN1bYpgMWPk8fwChxtlAOvLvvPzKfbCwoFQ3WDeSOOouNQybMgELT5ByDUHFov8kuLXEweLKfA9Wa2OnMLRkT1mwJNrxHlUUYGrmDhDztU3xYpljq2NqmxPF2v5Sc35fE8jYaFyi5HDPGPstSyvCZx1KlQ_qf7GTQx-zrAo_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=WFWl3-VpiGK10HLwheaWhBzXiFzoZTFO7upg0ufYCdzXYlGBDUYQGPYlOp5Hh9UwIkp51To2yRC2oU7c0FJu6SYHh2SnBjr4UyRfGi5cxAP8zb4KJat4EXNBIkhFNo6TRSAa6cW9H24wzNxLX7URiAbUZ35a43xlAHMdvrjziLC02aN1bYpgMWPk8fwChxtlAOvLvvPzKfbCwoFQ3WDeSOOouNQybMgELT5ByDUHFov8kuLXEweLKfA9Wa2OnMLRkT1mwJNrxHlUUYGrmDhDztU3xYpljq2NqmxPF2v5Sc35fE8jYaFyi5HDPGPstSyvCZx1KlQ_qf7GTQx-zrAo_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6OBxuRS-80IGh701ONUVZnoRbBbTAPowuU_COzID255MHlyVSnfjL7NopQack6aWQoOe6XRXqhMjh_nKGbNA5mzqbkoK4yIWj0i4jBXgnd65XAmmK3X_9KvZJc6UPfOQWrrUgpeUlLyQFK1PK-ZFtiPNQ9qkNApw7fpO1fbKtqBIiZPBnjVyEZvC2HEHd-yV9I1ZDT3amGTR5StzVQb9kk5s7UFeJI1E13dBy8KUBOUBNYeB9iCpeB0hoMplt8y8UsiqIJfPRGfPVXME5HRhyjHYRUYTxiCaXHX3WY6h_2sEpf4DWMAOSokLYeFO7zEZRhkcVum3WuDkW0v8j818Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgY559qeKJ4-30cVEztJc_yIorlB2ANTkGSWqd-DnCV5gP8k_Zl5D4DZ2RtK_W9n8sdSLJ0QHUtq3Q8fNU8WkNfIK6QAv77RzLOQfGVd71qdObMtanwOdEKtxIAE8kJtYW9c8HLDH8AkO0zCj36FFRMeR_7jnbrhJGB8YibFtjkZ5cxIuL7oMcSFEpbrfFVJKqYqVVleyyL5BT4WxsIfl-kg7JakIOOb7M5B3NxSDU_1PULLO1XeXbmQVKJnvwqrnrvOd1PPwTClUQF7-6bJvx2ncUTl0jcus-p5CG8gHScJ1m5rAb9b_IJryRvon-JoARD9ljVtMnEzf7D0OTWEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl1kwDy6HosB3hpaxbFpZsQX0KRly3U-JTicQDbKqLP8KjE-C-qrbOoACQnE6LrIawbcwKU0tWxPum2PMmRwtioCo5HrjDO1Is4bSlHm3EEVUt4ieIzjtr0wTyFIfN7G6-t7gTRKe9Fgf-hKURYeSufs83v2i2b7vsYXAd_KO1RZlk7y0Xi9-pXgGNhTlVUdDaQe6wkUg9DO1bi4ABNCRwv7GUZmEVRU3l-VAuhXwQArhxtI83aITJFRLKgNYpNwZYvcwV7Zr5REJZyGPYTsIPp_kx0w7DjCvm3AzAGrzSpMvRPgsC-1xv-LDWH1w7xatHw2KNL4b5IyyOCHFm8Rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBNygaPO0XO81nFjojUrVgpqyiwDP6s_ZVAQUjj05lvSOhDeVfps2qo4eEzHRRlzIiBPj3rts0nObCdxc-UEhVCafWALU08iTQyFU3l7QJjvdOCPvN2_RuwZ7wkHkgJ9UUElMnqSJxeMo0znEZyITd-vtez0GN8t0vl18FMQb2GhT-Nk3uDyJPNqi0FtWIqi63hwn3kCjP7Z8gd3ri_bkcso7qMy3v66dbX6RtfMuiXwtydnGBBhpyORc0GDplgF8gjv6vquRR-YOhS01LQbBwvcG68rdzQVo-lLzY3VNcz-vThIs1xa8VqAypdrBxbI3xwi2vSsMS_biz0TvRXd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
