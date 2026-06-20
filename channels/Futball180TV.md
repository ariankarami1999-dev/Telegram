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
<img src="https://cdn5.telesco.pe/file/b286uuEr2HykUh3sspM44DvyTD6wkTz7WRqs9UvE78b9WurSwgm2DRO_5fI-NKln9enchnkccnOAmFsZZt4lHg6nb98uWwQgxuXKb0SjOhC5rZLZlVGqNWbifBg7cW-uMLeDF6CIEDIfkOYWmuHit4T8oWfvpkYfTgae3HO4sRoxxclLNdzpGJdy0yCxIMKPyOGlhRashMCR5_gnVkSIb2xC3o9KpJDMOWbg_e0ytexBJhgpltLF2O1WtaRNLuYDK7Pi0TdelIK-PIksolR3HsD2jfiAcV8wnqNKaFE70XP0JulAf2bEbbi40z6ozSOh_8_yBi9hAD6gAJ_AmUCArg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 682K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 00:17:24</div>
<hr>

<div class="tg-post" id="msg-94778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آلمان گل زد بازم خطا اعلام شد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/94778" target="_blank">📅 00:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c338e8257.mp4?token=ZOii1FBbnH_cS8Ihu_b63xm0WK4ERMfpZsCoFEc2cD-e6D-20MXEYlPWF3R5zYEMIi3h5Lo8vxAOM6rZbCFQbisgwBJCOXSt3NXqmccW0toRbbVK9F-sqGTjziEtIW9mDa6KHeundWLauk4JxoxZf1Cwq9QufvbSCgWivzC2gKmdwjZ82G1FbYDjexnFS0NujZJQ42I5J7A_72VA4x4aK4c0vG6ZIZEzQVRdAGxmxLGSJeN7vwKvptgFPoMvVNPUy5WR7dl_bBo-d80bwLPo1LGPjmQyXCTmv5IYo1Axu2hfnhZ4PvNXTanSxP4BP66LeThVzcMfwc1x0ZoGZ-0YcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c338e8257.mp4?token=ZOii1FBbnH_cS8Ihu_b63xm0WK4ERMfpZsCoFEc2cD-e6D-20MXEYlPWF3R5zYEMIi3h5Lo8vxAOM6rZbCFQbisgwBJCOXSt3NXqmccW0toRbbVK9F-sqGTjziEtIW9mDa6KHeundWLauk4JxoxZf1Cwq9QufvbSCgWivzC2gKmdwjZ82G1FbYDjexnFS0NujZJQ42I5J7A_72VA4x4aK4c0vG6ZIZEzQVRdAGxmxLGSJeN7vwKvptgFPoMvVNPUy5WR7dl_bBo-d80bwLPo1LGPjmQyXCTmv5IYo1Axu2hfnhZ4PvNXTanSxP4BP66LeThVzcMfwc1x0ZoGZ-0YcIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول ساحل عاج به آلمان توسط فرانک کسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/94777" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ساحل عاج گل زدددد</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/94776" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پشمام</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/94775" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgwdUXZaRBiUxKYpM62cNLWeONVqdycVoDK_LCoVye8RzYQSCEZ8ZJXWk1vhnfhuW4903EE3LcsDxEb-2MeztU-rjT0nN4g_1K78gB8n5kyY1haqKlFV_0_oEZx3ySeMO24taLdm7YiAeUjVwPz_zFdA5LWPzxM89fWMw4_YGwZY_gzxCj7MTBtgPTaRwWFEb3pMqikzLDcgWpXqjdSbtU8X4eNITC9Hs9Z06TaXOtTirX_SexRefgTuTZPUqMviJwWjRBYNnWZqTTtkiLzJuaWD9M9LdqqBOmUGNMGHLlemZ4kDwZFOiSD0JVGhiAYTR4DJMylvomyQ8C9NjgUxVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/94774" target="_blank">📅 23:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آلمانننننن زددددد ولی رد شددد</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/94772" target="_blank">📅 23:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آلمانننننن زددددد ولی رد شددد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94771" target="_blank">📅 23:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گلگلگگلگاگ</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/94770" target="_blank">📅 23:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نزدیک بود موسیالا بزنه</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94769" target="_blank">📅 23:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد  به سرعت آنتن رو ازش گرفتن  صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94768" target="_blank">📅 23:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کم کم بریم سراغ بازی حساس امشببب</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94767" target="_blank">📅 23:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9ZSd_qBbiVek8Z4N37JX6GZbUoNvnMuFNs1D8GqRDbVKct6HEqhOJ67VhTMHxLDG03EfBRChGdpIe9dwcCO80EZlNyDxjiPvd6r9i9OdjJ_JZ4GLb7AizWYOXV1J2gdojAMjIcN0iLqjZUtevj9-7OEl5ZtNRrDxt53J9o3s6o8ZwW3O8esbz3hR_Kb2mNPstsAwG3sjWNxkzi2TOr9YMZJIz-3w6jrhlXmbgYaAzeAj-HpmFWuWJ7nlzrXv8oDprVsZ3EYGrEoqoYL7k55s9tkN2_kGUYE0g60rBnpm-QxS_R2L5tCCsXidIvvnLAXDStYrqKFqR7zZCldKhZ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
تا این لحظه ۱۰۱ گل در جام جهانی ۲۰۲۶ به ثمر رسیده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94766" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH77s31UmZ7mi4HPAneOfBSuNzgQs8tTOTym4EU1m_HnyRIC8cmJuscyKON56sz8D-4-W0z0_FRb7E4hwCqeGZUAr6T6BOPIuGkWt9tSGW7tjht99DosBHQxMf4KhUPEEG2TxPQ4M1Uryt5nNSXo5Ujq9gUrufFMAu-XpjCnYLrelWLkFwIPg3WOfkcCBxlqyQpV4zMdvxbnQb7uEaPxWzlagirHxs1JR1ZG7sKHBaD-aq35MZs3lePF36fUFVNgH66aHSdwJ9wGVncBsg6t9LoQunHBj3mLgyiyCZXf_0PHhobQR1OuE6HTV29_uWy5YEylLMVF-rmFTZF6m_rGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94765" target="_blank">📅 23:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAZeGBkRNSIDtB27mpasjU3SC7-RZR14SZhF-pH2XEJgMTYygJOHJM0EPzV34GB4eDsVAfH8Ek0TeZImnnY473irY0C17aXae_VCXUjtUkNB_c5XW5hjuADWV2cGiJPGLEP_Su9ZNBDMeyXLEjPR56sAOpbaTNV2nuhnz8eIG_TxiLt19m-iICCPP4O3WEI-ulirg6SVXNHrqJ415-AqA7UAi5ocizrUxDQljBmkpRo3KxTYII15WGKGitPgStDP81dtKk4r-BDalyFvMo15ZIA_N4OQYNRGueU-xwNLwDv0K3vx9bToDb90gEDk_z1-ABlcd9bxzm8MzBWwZNO1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین مشارکت در گل‌های جام جهانی 2026 تا اینجای مسابقات:
🥶
4 مشارکت گل —
🇸🇪
الکساندر ایساک
⚽️
3 مشارکت گل —
🇦🇷
لیونل مسی
⚽️
3 مشارکت گل —
🇨🇦
جاناتان دیوید
⚽️
3 مشارکت گل —
🇩🇪
اونداف
⚽️
3 مشارکت گل —
🇧🇷
وینیسیوس جونیور
⚽️
3 مشارکت گل —
🇳🇱
کودی خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94764" target="_blank">📅 23:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حمله تند اسطوره فوتبال هلند به رونالدو: او فقط برای نشان دادن خودش عطش دارد و همین موضوع بازی تیم پرتغال را خراب کرده است/ در دو سال گذشته، پرتغال بدون رونالدو بهتر بازی کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94763" target="_blank">📅 23:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6zN-HVrXMvNhwDEKqJvwWLphNoxFKgI8plexOwhdjjgxWw1AAZjTkJiBLzf8nztdyulgEGvT03tUFJ0EtEbLFn2pc19X5d_21kXyrzYSKINkLnfxmvEya-SLhxB_OFcgtphDJiZmFVXXiS7uae3fnr4H40w2B1C_bW0y9vbhYCDZ-WlIhSLGitfDFrN2wAn3re1ythDOfUFGsuV1-6lXm2tZWvi3WV8GuJXS62De3EpcIWQhyt2cjT97VkMCHrwSsjRFft9sDaKPGWfiX-YbwrmIV4j3Ta9NL_SYkTc8aUkjo8kdQ6x1aZfWKgV8eEtVp8Y_fcq0T0hikMVPS3Mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مانوئل نویر با پشت سر گذاشتن هوگو لوریس به دروازه بانی با بیشترین حضور در تاریخ جام جهانی تبدیل شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/94762" target="_blank">📅 22:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94760">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z7d1NqAIYlHLHyrE4CdhYsr1RV_Zee0xdH91VyiB4KBMqIWBDQRFc6H_auSS_RLnmCzhZkt1EtdOrKn0ugKQ0SvdWxWg-BMhQ7yeKZASZf5hpGoOxmf7nbi3h4q1l-4kEPK0vSwG_kbtoPgZrfSiMROztmF67WbQCG9L81ADC2_NK-RMwXtkfSxyw9cYqK2lKQeN3rls26LoekJ6Kx3u3Q-pwGBPzuvpY3ojJHADzj3-Z0rPt8NMnyKyAKXWlRMy-TkiK5TChRZaVfFC5jFlVbmWatVLUY_e1JEJEtV3d4oAGTqrbyrdTqEGKPlUyIAPGUBSfQ8MXlQkpJuohEIhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0iwzXYI_DqDSm7ihVL0l3YmdLIbsszCaxPOxaE-zyXSNbvNO87U2aB_tJS88-ze5qKFSlWhBEGR0bkqT_IVutXxD2sCo91OOTZ4HsO27vjwGgA4i-uBEmKWAproq-OxGpk0R8FN0r1h61QHCizi8mXIIYrHqEUggyLuJRilJGDbpVp5wpI3LtV9fTVG8SRqVvy-hTqA0dwSdsBqdO81pljzPCCwHbnJfz6QlCwV-1GzO9Jepspump9Q5RCBSarF8fyggZ6knI382fMWjD9DAz-enZHoRcRIAPYhPEenU9o75WDOhEshppFPgrD2in7KNP3XwOeLqxJiDdUw5-wE-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇳🇱
کودی خاکپو با گل دومش مقابل سوئد، از آریان روبن عبور کرد و حالا تعداد گل‌های بیشتری نسبت به اسطوره هلند در تورنمنت‌های بزرگ ملی به نام خودش ثبت کرده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94760" target="_blank">📅 22:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94759">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spzpX3CBFSr258iP5JcBlNHtwOz7Irq_Jl1oQw0Ittyx2_qDPfOMEtmkAzb_CPoZm-OLSxYMmvOHoYt7KqXC0IgYuy6tE2y9DmFpyM0Flt8mnDDUxN5oJYZmL1g7sGjBkJYewJJ-rDd6jsdAYtn8k7Glpfbm819LgXcbcwtgx81cnVowgH0K4k0Lq-5DbGJCDVtnIaVo1_0RBWy0TTyRJyE6S7x9R773L2rQgzoWMs8-3XBOEtiYq44-VmFkMpP_mRlmPiMl8YdH9lA85dafCaOtxKkRQxuC1JNanAsZ7iwcTKINC1q-tkNz72pYlFAxBRbjVnXcEHTJxISN-2AI9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر دی یونگ با پسرش تو تماشاچیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/94759" target="_blank">📅 22:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94758">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAJXDcGXcGb8fyGp0q2CuIbtSLpdq2nTgAjqp1tbLmuB8KFAoOFWJxBqVwxkNfMXnZ4bmnJAOXR226LGttw_x3EkahJI2O54hOHedb_0tt2q5dsmSmHXmivJeQmKOYm9_f9Vdy-DJsRsYUbns3-earLwDr0_f_wqko88yzSQCktod8OXuQ7bRn03Fi79HDIKDbtTGXWUV9YYUtjt4oFNl5s9CCrcmqZmlisu4fNV1lbe9XPvuR1JS2PZ_d2l9zK3UMpOJdu1Wde8sLS23o3AyjsU-690pVmMfRg91klUxVHnxzErdp_kfqf0obvyCUsAKA-ZbAdv1TlauEpxwBWPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
با یه عکس فوتبال رو نشون بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94758" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94757">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef53d28320.mp4?token=f8V0Skdj12MPomQLs4oAZtZ49hJaottpro9w1iMWVLRFIH5ejrZsAmZniDpz9oyDsp80AkeShi8gNRfsST2TN267u-FwwnWZ5cs3ZfGnpeE4L0or-wsHLPC-GdCQt55p6E1Wr2OYFHkEJ-aq3orebIyIcjzN1w9LhI9wi4EiHhsjNgah6NCar34aDOo6wo34oN_9jz5xNC78gb6XKBGL5kT-Jn6vUdgR_hwjUrVixcPoX62eGFX6nBvesIFxMqsxD99RUBKv1-vpRbGW6mV9-JfAV1rpBjVT66vBA9FOlPqwH93I_yYE8Y0WMYR-Qpx6t5ajlhnHzdbQK4Td_v3rAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
نبویان نماینده مجلس و عضو تیم مذاکره‌کننده داشت یه نامه محرمانه از مجتبی خامنه‌ای میخوند که در اون به صورت محکمی خلاف مذاکرات صحبت میشد
به سرعت آنتن رو ازش گرفتن
صداوسیما بیانیه داد گفت نبویان ناقص و بصورت گزینشی داشته نقل میکرده و ما قضایی پیگیری میکنیم
مدیر کل شبکه خبر هم مجبور به استعفا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94757" target="_blank">📅 22:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94756">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLX03-eD1gJw5Gs8daAC9DPALIPPv3D2x0dsLFNXonoCBi91vLgxxTLbkipOAPlqV8LEYRKnxMw3gYuryDaDEIeNNEYLLiYZ0YQEpg8ax84lDo5yiWUAN6H1eCol0N5nyOnv5sM-gPdSok_6_GMbQJ4F-qg0N2TsqwbScNfVRTJ3tAV7HIWJEAf3e6lsXsgrpC-Be48Gpmui-Gsr3V1FiIdE0Mt7PZGPBq-cXe2FfpYHBgt5OZRtTQ1aFaMmwgGLDPHRlAuGWpZJdwfYOcUO6SyGUVJlp_cQzTTozR4D2G-N6VKzyI6VwwyorGE3wp7TqGYOG4dfBJ5MrwmeK3GJcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
کاگپو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94756" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94755">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فرانک دی بوئر، اسطوره فوتبال هلند: عملکرد رامین رضاییان در ۳۶ سالگی باورنکردنی است/ اولویت ایران باید نباختن در مقابل بلژیک باشد و همه انرژی خود را برای بازی مقابل مصر صرف کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/94755" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94754">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Akq5T12SVHxHSbJSnjIcmVqJV6SlNVFVSHeW6EknyV2km3h3kVdN1jFrIXQFQjJTEZ4Os12OLSxxfPOYF9AzMkK6ATlWM_eHyrE4EnXzYhSW2uI2WL6cn1ro-ZELUhZ5rXCmQs8ogYjJdjRk0MdBLMWHoXSHTwQypL_cSweRb84q9DHKTcA0yVUfL3dPgkXCSOldOOEQSWjaCgewNCdlYcoN5S6yOiXouwul5mlcHHJZkiyS1Ocvsc6myhm8Si8ncj1RqO7Lz181TfSlyyygYZSMR2pB29Aoa9s82RzD-F2e63btVp3H-7FXCSgbb0ZRCsD5BbU8wA5RrM3vZbRQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش قدرت هلند؛ سوئد قربانی شب درخشان نارنجی‌ها.
🇳🇱
هلند
😄
-
😃
سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94754" target="_blank">📅 22:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94753">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9ef7ea27fa.mp4?token=DZ1xeNDbwluFOjpO_pU66SI1v0QnyYO7KNz9Wx8g6COjuggHnqBVWly9u0MYzbetYlCwlVvrtQ3kDI8jyR1yY0bMXVhbpEmiRV5_1Qr78tMYRRIP29dvUPfkKBqQo32abY2LjKVw7mGs_nvhniKhcM8GkoyJqfr5B8DCYsZEx8GM8Bv3Koe03J2iK2u00vocD_BxBZI1_zxsm9Engq4QkI0HT_HkBvTjQ2zBIpFKSu_hFZWG6oq17z7EQjWpFlwjNKcy57MF730V_uim_kxd760I61-B7Kit3mQDLZke6l5sGe6IQz0HGSP__FkBZrBjoQyAQ5mQjkvQKE24S31ojA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل پنجم هلند به سوئد توسط سامروویل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94753" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94752">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گلللللللللللل پنجمیییی هلند</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94752" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhFUOb87k-KN2PYsEOjPNHRE4Qr9plzvZDERMisW__H8tIBazq3hQylmjPqu0aYQnYHUwvJd9ThPvpfibsgZ1We5KxaHI0pLIvNdP-nfFi0WGzGYO9HmIFXZqRWUu62aEjF8F9-hS-xgQltOMmLeWIaaRu5kxhN7bgf0hOr9aZKBeKFCplB9pVdC_HWoB2CoZwHq0dMA5qJK2e9JL--LspxxMjikYq1zlZ2aEmbUASG-nHIdTY9r7h6hoccFlM_nJPftEiBJr1Z6DOfeT03xhJKfnKoQMFjMhHWvj3kYb7DB9eK11v6uxS_LRbU5-KHpsGBnq4cgTDJODYKeovvOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHToEGBS-fExwp3oBEO552RqZTwIysFjcIEKJwxCc28FK6yi5SHfG4s_G_dqrOq2QxHXFZ-8UmLaZOn-1bf6Mhu3djU-1EK--MeRI21hBYsRGKZm9s6iPfis02zCLLpplFyX9-4hG9gthId2EtJTDnW19AlLNX_MSmQX6RebHlF-ZGP7H4CVeT1O6B3v2fjzAWJAq6EQzCzajnKhYULghkqrvTZ5xRzI2I5bKQCgaM67kE6sXMApwmPZROkENH75ry55mEp7-HWzqJMmPN0nQq1ULkZR6FbWq9laSZQw4LIISEjWOEXp24HGjW5521sofoauMJORgUhDcQ70Y4rTqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇩🇪
ترکیب آلمان و ساحل عاج، ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94750" target="_blank">📅 22:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAxi3LGazbi5DbSqjLuzThDgpMl6Ps9VvVkr34Zc2CJ-fleuw4QJhiJ9U0RQ6WShfn4hp0tydzMdS7LH5-Ca3Vi9w808gqhuaWTvoiGERC_wq8ATKw_wbFj-BIFx6q6peTp4Tvm5NvKznpTorKQRGrKtyGs_H86Fa2Mh5LwQ5Koqr05apYr5Svwo2MhDIOdK6aip6g-fVaXT9i8fljtDwIRhS2oKLH9hQqYgVf9pZjBo5-rQX4CMZIfx1R2VO-8jAt84N8sOZwO2bnm28V2xtc4bEMlP_Oram4A7fMZOYZUIaR1aWpa2PRy5ZxclCwFKoFuCExPeUbGwaivtz-GpmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتتاح تونل ویکی فن دوین توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94749" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این دخترای سوئدی چقدر خوشگلن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94748" target="_blank">📅 22:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">چه لایی خوشگلی انداخت الانگا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94747" target="_blank">📅 21:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9b4fed19a2.mp4?token=ayGSLr-UsyhNloYkRp1MTNt_SPr2zXEcCVF8I6fuk8Z1BHDHKyxK-EOwSySr4V-oa8Ft3j7EbNEuC2-tYVpkwfEg6E5W08ACjItKe5EUmGdhxJjYAFFKvTut4tqVIQpFHaL4KC-uByAWkWCmL2O-IKOVd4ni3D39zpRJgdYbYANU-FnMc_BHZpChagpJ01gYVFpg1O_lJ2ala36AJ_t4dVoLaWaRNAfDr7_K-0ZQEgbRWc1CpVlpYC8yDmLd2S0sxlDsnTYVCUvCP9tX2YC_RnILu5Ut9Vb8MzPRk18ZzsR2da18xRkWLbVT4HDXxAJ3tmz7EuC7UsUTvOxwJ4Ol3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇪
گل اول سوئد به هلند توسط الانگا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94746" target="_blank">📅 21:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلللللللللللل سوئددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94745" target="_blank">📅 21:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b48414ae5d.mp4?token=smOMszu-oean8pmRCKFqLMA9DOpe5T76PqVrS_xYvLtg7nVd15_FPALbB6mzsZXlV-VB4-L9HGpLinPFN91ChCvDt3506GFceIxRHtA4nIb8cK6_qNKRrD4X14Og5iiNsrnOKhEXmSLkMY8d7T-QD8Q3beKrrFHM9TTfWn2iOdQx5jk_eNAnGjsEj-JX0g36doRRIQaWCfSF0GOwQOVtYdVAe8Vb6TUh4xGfxXQYuTpGHmpEmcnpBJIEIZkstCu8gyB_Nc1uUbZ968LOMeS7WRif3QwJwGrMlPpOFVuW9hpEI4IAqjtl86-87zheEI30C8StDqu8zNDqtNdfvtLqXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b48414ae5d.mp4?token=smOMszu-oean8pmRCKFqLMA9DOpe5T76PqVrS_xYvLtg7nVd15_FPALbB6mzsZXlV-VB4-L9HGpLinPFN91ChCvDt3506GFceIxRHtA4nIb8cK6_qNKRrD4X14Og5iiNsrnOKhEXmSLkMY8d7T-QD8Q3beKrrFHM9TTfWn2iOdQx5jk_eNAnGjsEj-JX0g36doRRIQaWCfSF0GOwQOVtYdVAe8Vb6TUh4xGfxXQYuTpGHmpEmcnpBJIEIZkstCu8gyB_Nc1uUbZ968LOMeS7WRif3QwJwGrMlPpOFVuW9hpEI4IAqjtl86-87zheEI30C8StDqu8zNDqtNdfvtLqXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل چهارم هلند به سوئد با دبل خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94744" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">چه تیمیه این هلللللللللند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94743" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلللللللللللل چهارم هلند بازم خاکپو</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94742" target="_blank">📅 21:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/81850e4c97.mp4?token=qlR-QTxWGg3f87X6d8IbvmPOUQWuwDrZXxBsu7X7PJtvSLU6YISPQosH2x1n9fach2rGUQV2n0ZhiRKttDADuVrfs_gY2QFrcuqznB5nm6a1RHSVy6bRz-PRJNVKp7UnPZqZ-i-c0kvQkhvf8ZdC4uSbUzm0EUBqGvprR056hkmUDDFxfE92VBGg64_lQGeFCdN9K7YA78X4-k3wFC00vfdMSbYTwi530TfeHGI3xWhjdQWf3OswQie1pzQ70IqyJwQuZ_R_3Y0RD9VCNFZXydBaTjVVhqYyRNJBCHXQgSPE0XMjKDhYfDZBw92UYaxPNZnnQaz7oPnd_5Lxb9svAHmZEZWLlRNP7gWctXnA1ThXiqYmG_mFWsk6ISJanmDYdL3iMN_snOUqP1yUasm8_yov1UkH8Plk3sDsxSBSpuWYEYPQo-Wejt_sZA-WlFpodtvUgiG40EO9Pt01UL440SQLFSw_QCXNNf8bh335Ic_J1J2KC8CjBoQJqTak3nqjxsV7O0WPbE-zmalziYG3we-S9qLHHsaelKuMZr2N6x1WLleH0dhVgXgLrKsXBo11SwBhEDAGB8qnw_2tVm4I_m7J5s4HA0GlosXzlBuVOcw0FdQBsCs6NCMw5dEpt9KmpDEDRMYEquIgKQA0fQMLb84mMGS2enGL9pzgtVeoFNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/81850e4c97.mp4?token=qlR-QTxWGg3f87X6d8IbvmPOUQWuwDrZXxBsu7X7PJtvSLU6YISPQosH2x1n9fach2rGUQV2n0ZhiRKttDADuVrfs_gY2QFrcuqznB5nm6a1RHSVy6bRz-PRJNVKp7UnPZqZ-i-c0kvQkhvf8ZdC4uSbUzm0EUBqGvprR056hkmUDDFxfE92VBGg64_lQGeFCdN9K7YA78X4-k3wFC00vfdMSbYTwi530TfeHGI3xWhjdQWf3OswQie1pzQ70IqyJwQuZ_R_3Y0RD9VCNFZXydBaTjVVhqYyRNJBCHXQgSPE0XMjKDhYfDZBw92UYaxPNZnnQaz7oPnd_5Lxb9svAHmZEZWLlRNP7gWctXnA1ThXiqYmG_mFWsk6ISJanmDYdL3iMN_snOUqP1yUasm8_yov1UkH8Plk3sDsxSBSpuWYEYPQo-Wejt_sZA-WlFpodtvUgiG40EO9Pt01UL440SQLFSw_QCXNNf8bh335Ic_J1J2KC8CjBoQJqTak3nqjxsV7O0WPbE-zmalziYG3we-S9qLHHsaelKuMZr2N6x1WLleH0dhVgXgLrKsXBo11SwBhEDAGB8qnw_2tVm4I_m7J5s4HA0GlosXzlBuVOcw0FdQBsCs6NCMw5dEpt9KmpDEDRMYEquIgKQA0fQMLb84mMGS2enGL9pzgtVeoFNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل سوم هلند به سوئد توسط خاکپو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94741" target="_blank">📅 21:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلللللللللللل سومممممم هلند خاکپو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94740" target="_blank">📅 21:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWiUUhoH-4xVP2iVc-xYwKRWG6SNN9GPVyOUWYS40sW7UT1igZyLG0sBixf-ihWp9Zv0aV37QyKzL8RWJAZTCKDZKKrIhL878QV7NonvdKCYharBuYheWKgWkiZ5lGXzCaFziIGomVo3rb5emYagnviM-jD0DrO3MlEn8lH2085e8MgY6_3ImT8qKXquy8aJwRZ56AHRitJeonNkBwUPgDsMqyLFDESdkw3aQiSWELLDEzk9SKPaHP36z_eQRMtOd1A15a7b0SdrYEtwUTMnqAyyZbrZfd51IsQlgU7W7xDD2gR3SgFURYRA3EDis4JLprLp7wjoRzPVzjF-2WVNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇪
#
فووووری
؛ جرمی‌دوکو ستاره تیم‌ملی بلژیک دیدار مقابل ایران را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94739" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/94738" target="_blank">📅 21:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOFwvts6oZ28hOQrztvMPOWZ4eZm4liS3yiG94UfLQ7ZZlBdVQAGLAaIqMiMjCBbymqkctpnoZtg9x9zZQhD5ONd5AV22z_lohA1v__FuHCcYU3Ozp24KaxN0zbj0FHeFD7tcS3znk_YkV_sd3zv1ELwZCX_A5wKfnOKr--1zFB6_2bEsLqGXdN2F1ecbP2W9BVJT5W50YvUjOxFHX9rt93gmn2frVhMK_3JPc8IGb68YOgs0mjqy8702U3pQWgaCkai13tbL0Qu3qM1xu8vmlcTidQe3Oxzdz5RteW3bBZgXJsiaNkI8L1Bl1R4QFrO9toSPUlou0zFN0DC7x8eCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
‏
📊
بروبی مهاجم هلند در نیمه اول مقابل سوئد:
‏- ۲ شوت به سمت دروازه
🎯
‏- ۲ گل
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94737" target="_blank">📅 21:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZb-icbeZpN4oVBIcgsrkJkgre2_c2MY5QTPVF22mlaEpZAs7NdsF6fOhU3I6NWn9g-0-BG-DwxB55cBoe8-ZSOkjY-gvuM3AJK8WHldK47-LhJZ4vZX7yev5S0J98u5Rq7QSN6ro29GBr06Jk-JVpP7VkwftyM1I5oGTK6HUh-Vyk_CY1qn-qM8pi2KHXJza3jOO7lB3jUC_N2b38QvhCnzhKYXZAsIpQ7eqwXP3Uf__9IC7yZ8cldeVJZne2aUn68r_svg-R1Vyz948ypPorWsfJRkNiqrvYtSE8TDhF0xRg8K8rOKn3YESIOWakgfFktIX_Y92XNCEdXJLgMS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇸🇪
آمار نیمه اول بازی دو تیم هلند-سوئد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94736" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIpqx6JgC7eAvmSrOGj5hZAW9zhiX9Ol5YhGdZN4d1yvBIwRL3knb5PVH-ls_2VhSd2vA5rTc-Tw-Xg-7XtsOcNbZ9pc9Kvw_0Zk3u4g0uHt0h9_ruKIvMZfB4LdYGFYQBEa8wBI2ikNYCbHsTQeGbxvoj-DFQkPVW3Pda-PXdgYkLi7iXW__J0S5k-iaQD5g7FkLpOCiKGFndG_vMosu422iwZCHLKoezxwqqhd_p-H_-jYTtFCPPe9Fmlrjw4nEQJzg8QWABSKX-7__cdGKYToe2l4GYkgMdDHUsqKAY5TY4q2pHZnz47VyDs9gwyJvHnZcTNti0LEol6ya6zdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔺
رومانو:
انتقال انزو فرناندز به رئال مادرید با سرعتی مشابه داستان مارک کوکوریا در حال پیشرفت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94735" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پایان نیمه اول؛
🇳🇱
هلند 2 - 0 سوئد
🇸🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94734" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گلر هلند چه سوپره</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94733" target="_blank">📅 21:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94732" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">البته رد شدددددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94731" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سوئدددددد یکی زددددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94730" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گلگلگاگگاگا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94729" target="_blank">📅 21:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94728">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY44kEbFaZw8bl_EP7oOvlBuylWk9y7LW_q33iKXw848Pdvb7wgNiYGrXv7sbtGc_U8xLWIibLst76URi5vrdCG851yQFt2_VD2e-uOHGCHNQ_QLTmr9h3v626BuDxj66fEGz9yNHueKwpyJOPryi0j-T6-tEShc101MH9fPrbj_ztWaGlf0XdCPY-odKLu-dzDET1WfgWAsyFFjN_n_fVKaj2LXej4igWxqZgJQvevKaIebdEMglKgt87Wg4WWVT9VxO_X3kT702fxE_eeuIvk9cqynDhbdE9n73ZB4mrtT5fhj2giVA84M1j6M69rfEXB3FPas2ZJDegKeBsoslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب شاهکاریه این
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94728" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94727">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">رفقا سلام و درود
اگه محبت کنید حدود چهار دقیقه زمان بذارید این چند سوال ساده پایان‌نامه رو پر کنید کمک بزرگیه.
شرط خاصی نداره. ایرانی باشید کافیه
💙
یک دنیا ممنون
https://survey.porsline.ir/s/ngmblc2l</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94727" target="_blank">📅 21:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94726">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">واااااای چیوووو از دست داد سوئدددد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94726" target="_blank">📅 20:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94725">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=mZ7EMG_0AvuK6YPcW_GuhxMlMtS1TsiC16uJHpH0AD7qkA7O6SJS3DojYqbTBwDqEypHnNWoYg-AHjh0YlgM0gkCWw6bwNJZrwccOfxOHdAfY6rKAr321tLaeo-xVGZiVyOmRH5lbq3lEvK44fVmfTrkQJBglJ33IrVLRQOTKJJ0A2_WWWu4GCyXb8XnF6cv_ngTJLaT6or0UcYeKQ_LUwWG34mFCvJOhP-p7SVE4AFEgbsajbAWlvcxRUoeNDufoyKBieuqywQFDzXkRHfbzraWLUBFJnvgANV079R_sSpP5UTfGvIFVav3TYbXXszCDttStneCgS9R9MWgS7QwIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc96d2cae0.mp4?token=mZ7EMG_0AvuK6YPcW_GuhxMlMtS1TsiC16uJHpH0AD7qkA7O6SJS3DojYqbTBwDqEypHnNWoYg-AHjh0YlgM0gkCWw6bwNJZrwccOfxOHdAfY6rKAr321tLaeo-xVGZiVyOmRH5lbq3lEvK44fVmfTrkQJBglJ33IrVLRQOTKJJ0A2_WWWu4GCyXb8XnF6cv_ngTJLaT6or0UcYeKQ_LUwWG34mFCvJOhP-p7SVE4AFEgbsajbAWlvcxRUoeNDufoyKBieuqywQFDzXkRHfbzraWLUBFJnvgANV079R_sSpP5UTfGvIFVav3TYbXXszCDttStneCgS9R9MWgS7QwIYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل دوم هلند به سوئد با دبل بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94725" target="_blank">📅 20:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94724">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">عجب بازی ای شده
🔥
🔥</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94724" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94723">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دبل برووووووووبی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94723" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94722">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گلللللللللللل دوم هلند</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94722" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94721">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b1bcc530.mp4?token=opSbVRD87l77ZPHDC2vOZXCkXPC3Liw_isD_usBuzsfm24jzvowikrzLMuxzTELcAvAr3Z8BEsKPZoO831X3dW3RlzTkQC854x4onzFk3WnJOKSg04p-RX1QaEktWOWzHhNmTCG70_h-3b0p_OdYashYkatC9z9-7mMMQfmjy4BtjKlf64TqAVvfJPP45hUgFKVEFrq09QdY144kWcIqk-lkK54CbJRNjI2UYlYPjXYJNaUys_mWMh-t0JKQbqxuGsyDX3tIo37CgNTR373vfBQBAFbMH9X2cup-apaWYkeRquAjkagMtEoNNGLOXlP-0FPUcxQ1lEaEAN7MxRqhj2inGVnidxnLhookNe3Bm8vbYY1ymBFJaBbq4mf8_qXNfcN_9RS-UJnGgFy-09V53J8wqwD9uNVePOFDwiGHdqJifztRthRcWShSW2k59wNk9W7dQ5f-RP4XzzvUWwgVXpGV6dYPJLifGiGI-4nL7OBXE3-06w8k39Fxx7NnrbVdNf7U-rVYRgzXJwr2yJCmYdLFasF_c_CsrWZpIocqIgbiB8gpewuZTOCIofSyJQN_fCsBMftTzqhLGTC81fs4UP0W7wsRB22qROZBb9JOE22c3s2PZsUJHfcEg0DrL67mHwsG30aRoeYtvI5YDm_BTy4zI7WcvXFmUL3Wm7cuheQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b1bcc530.mp4?token=opSbVRD87l77ZPHDC2vOZXCkXPC3Liw_isD_usBuzsfm24jzvowikrzLMuxzTELcAvAr3Z8BEsKPZoO831X3dW3RlzTkQC854x4onzFk3WnJOKSg04p-RX1QaEktWOWzHhNmTCG70_h-3b0p_OdYashYkatC9z9-7mMMQfmjy4BtjKlf64TqAVvfJPP45hUgFKVEFrq09QdY144kWcIqk-lkK54CbJRNjI2UYlYPjXYJNaUys_mWMh-t0JKQbqxuGsyDX3tIo37CgNTR373vfBQBAFbMH9X2cup-apaWYkeRquAjkagMtEoNNGLOXlP-0FPUcxQ1lEaEAN7MxRqhj2inGVnidxnLhookNe3Bm8vbYY1ymBFJaBbq4mf8_qXNfcN_9RS-UJnGgFy-09V53J8wqwD9uNVePOFDwiGHdqJifztRthRcWShSW2k59wNk9W7dQ5f-RP4XzzvUWwgVXpGV6dYPJLifGiGI-4nL7OBXE3-06w8k39Fxx7NnrbVdNf7U-rVYRgzXJwr2yJCmYdLFasF_c_CsrWZpIocqIgbiB8gpewuZTOCIofSyJQN_fCsBMftTzqhLGTC81fs4UP0W7wsRB22qROZBb9JOE22c3s2PZsUJHfcEg0DrL67mHwsG30aRoeYtvI5YDm_BTy4zI7WcvXFmUL3Wm7cuheQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
گل اول هلند به سوئد توسط برابی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94721" target="_blank">📅 20:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94720">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چه موقعیتی داشت سوئد
بازی جذاب شروع شدههه</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94720" target="_blank">📅 20:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94719">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">برابی با پاس گل خاکپوررررر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94719" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94718">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گللللللل هلنددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94718" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94717">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آغاز بازی هلند و سوئد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94717" target="_blank">📅 20:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94716">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b62de811.mp4?token=GNEti6SVHAef94iyRiB5ExGtPbyyfCN6a364b83fPnCo0gFw2JES2nJBtqA0zDTqVXuwJQtYau_K8ozXbBBuy4zULxo0yLjif16L_tttn3xvjX9WfbqRtiju7cmgsgHkeWgiZemedN8TCf8ka8fiLF7CZh6fJHiE0U7yF_wp8caA95e0sK79EPvfVJplXueFstft3PL_qzIeUcew2n9IuBXjhHECrwAldAb9pxj-9dm6LPkL49lLwqEIn2Y-P-bXGCuUDs7bh-ZaEhAUu3ME_v1ySKeuNY5525gCQGa9pujRcSdSfRi0LoZWG0Q4m0z2sVyymoZGAK25K_XtTunidA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b62de811.mp4?token=GNEti6SVHAef94iyRiB5ExGtPbyyfCN6a364b83fPnCo0gFw2JES2nJBtqA0zDTqVXuwJQtYau_K8ozXbBBuy4zULxo0yLjif16L_tttn3xvjX9WfbqRtiju7cmgsgHkeWgiZemedN8TCf8ka8fiLF7CZh6fJHiE0U7yF_wp8caA95e0sK79EPvfVJplXueFstft3PL_qzIeUcew2n9IuBXjhHECrwAldAb9pxj-9dm6LPkL49lLwqEIn2Y-P-bXGCuUDs7bh-ZaEhAUu3ME_v1ySKeuNY5525gCQGa9pujRcSdSfRi0LoZWG0Q4m0z2sVyymoZGAK25K_XtTunidA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان بازی دیشب آمریکا و استرالیا داور بازی دچار گرفتگی عضلانی شد. حالا با چه ترفندی به مسابقه برگشته باشه خوبه؟؟؟
آفرین
آب خیارشور...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94716" target="_blank">📅 20:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94715">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy_Xg4ahjD7sKBqWO28KE2UMObo9DxbI9sYvGSFISpaBrsypGpcZawuiRBBHXncCqbwTL0B3Nh7aVUnDlHzCdgC2O4vA0QxUQTWsBxwOJsuOWijVBw--eOyRb60OnwiCcft9Hxkao7dfgwKRNxGd8hZH9lb7NJID4lh7ZxVYZgF6gUwatkmJXHO71i0iSNvHjI3IJYKbhtXNthE6DjpFLyQxJQdVocmUrEeic0DB4Mc-ueiZs9JV0FoPb7s9HYLVOQKhZRW3oLzRklN0v15EuMxlDvuJRIEw_C4RDMiMFaODbu8HCt1P23Vf_vzRva7xMwPZBwHacRf1SeJ8X5OQRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایجک‌از آرسنال و رئال‌مادرید؟
🔴
شنیده می‌شود باشگاه تاتنهام با وستهام برای جذب متئوس فرناندز به توافق نهایی رسیده و طی روزهای آینده رسما اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94715" target="_blank">📅 20:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2b5xJSA5gkoJeggtLt4ONHOI0PuMgiOQVkw3qnIrO0KAaLSK_aji4g4hD02fQXttdXPnUP9ZkwhBxieFF7bsNUQSurLiY3hqrFsb9S-2P2D_nKnsSDfxyxxMcfavboSKPM5KMlc6SkVTe7g_E_c8wmctzbSFig_35eiQ92On7D9_IBZVgluVJf0JFBBBwXCiciqHhtRir6MGRZrUN9e2gnMl-lNwOUUhb5OfO4_-7HmMCxwnCDjgnx6RYpaMK3p6rKDdqPE7yXw9ucV-L15p9tz_HIFWNc1T4tp1aOCrnmTRpoSiPpqKTUhrODKRw-42aRhuqKeJ8ryMdQMRe54lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OLQ-shqA0Dk2DPkqXzsrf0Qo1rlqHIfWNrBPKbCjfAbBKPaidx_ogUXUr_3-kpDV9_L03I-LV9fjH83ZVgMVK6b6rupTdrO1v328xkfdLnakLgZnvCOEpqzxiMiHX12sYgV8q5VM6E1c1rp2cCat_Ajrjb7RqAtg19GPdu1mS5uPhljeHY05jhTN4jRhbvlW2xH1UZYciIs9Tkix998tkaTAwgsDec4MNJOxItmt55zRCTizPopjMz68u_ypToXW_EV9Fuw3C4YI5qIIv6s223HEd4Z9MNI1e31kD08K0r23JuC7a-W7TEYX5nhXk9qk-WwkXInI3iY45vArxwapuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هوادارای کریس به پیج مرحوم دیگو ژوتا هم حمله کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/94713" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/94712" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94711">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-yWqqXyTjVpl6cWRyY-SluWLwisvRelHifUUPf3IDewhxzTYPfkE4_6JuS1HnWzmmdE6mxIQpP_vGrCfUubNtymGzC09jfhe-ptNE2i1lp_E-AmbehJk_1l_dSIRYRiCiSNmlHDNwY6DD4USK1B1Eor7jEdTZGsjc1XF3F9D0FKuS48AsDNOorpPXoRvaOmn8DhWkS6RC_SlX9KksKAb6OOqpOlbMwnnWsHUiqMxzotx9G_MkXo_MWWKuQ0-H6BRpDZlFqncu_qCoOb2LokEH7CRgOzVyle0KQE94trqaHeFGOPtZQD1lKcDGm4tcd4ZhbSK6jYSFb9CWFOZBQeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94711" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXfDlLe93VZqerqgIBT1xNpHonawONt4LH4vxErLzCGDyMbQJ0IY3REElNjg7jZLxR_wUF1c0KvNyaECTLxEijsadr7N3DTuUyyrbCacSyoJ2-XCn_fmO7_PCoaS8QRNqYk1MuW8W7tpoYzklUgvoipK_4RKdpBxVdbnPIvvHRPYmWh8OBsx49-dA8Sf4NDI0DZYE2IQ1OIvKdIH6ch5LSMrrrJwLbmuBaaxN65wUS5xaPmwfDAykuJL1fZMC5EYMzj8OUa6ewKFbu9LHpC9nc4SL3Kdfjty783lxw_GOczSZHJ1U6XPr8nPXVuAQKbbPKqxaNYRYhpIQwlS7SNJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فووووووری
؛ بیانیه رئال‌مادرید: تا این لحظه هیچ پیشنهادی برای مایکل اولیسه ارائه نکرده‌ایم و قصد وسوسه کردن این بازیکن را نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94708" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94702">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aaff8cc8f.mp4?token=Y46e4seUxzrNxBwnFXpqn2O3JBS_zOtOUA_c7RXMyFV37HL9lqzS9dwpgMMZ_z6OEbQMXI5BMZQyoMYTHRPtHGy5Kcyn3oVbYor1m-faPHKA2ibWNOq3yQ7_eCBdnrS63AA-9MjaHrU0Ygt4GtaS_XZ49_U7F9sx1tDMgss8WCwl0OZ0pZ2TSqJkRNNoMZfSX6xkhDGqNlEPuYkZSRWEecro_wcE5yPxXsRiSwmZiZrIOrN6TDYf72--ySzWXHjoKIYxHwaZJfKBLgOh2cFGW9uGYmjZvxbrQ20S846KBpHk0TnoyrPwjasApbcWTPKiTymNdqC92osWQVsf7vd9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aaff8cc8f.mp4?token=Y46e4seUxzrNxBwnFXpqn2O3JBS_zOtOUA_c7RXMyFV37HL9lqzS9dwpgMMZ_z6OEbQMXI5BMZQyoMYTHRPtHGy5Kcyn3oVbYor1m-faPHKA2ibWNOq3yQ7_eCBdnrS63AA-9MjaHrU0Ygt4GtaS_XZ49_U7F9sx1tDMgss8WCwl0OZ0pZ2TSqJkRNNoMZfSX6xkhDGqNlEPuYkZSRWEecro_wcE5yPxXsRiSwmZiZrIOrN6TDYf72--ySzWXHjoKIYxHwaZJfKBLgOh2cFGW9uGYmjZvxbrQ20S846KBpHk0TnoyrPwjasApbcWTPKiTymNdqC92osWQVsf7vd9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت اسم ژول‌کونده و امیرمهدی ژوله
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94702" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94701">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad258d1fb.mp4?token=ZNhw-YcQRODdEa7zG4pm_n-XJcoah1ykJrYAlMgaEtS3AJWDOsNkwprUFDjdqcbCjupI2RVDI4L4yXmQlG7Kr4Y_Hv2hP5wvCMuyENEcZpLC32Niyc8FQRaypiL2kNDXGxwGca6u6yIUsoBKWcOo1uYOl3KsEHsc5lTDE_bo7ydLTeY54zuLh2S3dEt8b9OGY0M9yRrWVtTxOhLEfvqTFG2ihN1_f_IpQhT1ILDp-ylLf5cS5u3CUli3MERXKv1MNhfeL2KXr1k0PhHzaBymagPRnhvx3Vi9zUFumwP61m9I_3b_lGX__DrPJMoF0CkVzxvF5PVah0WeY4TTss8s1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad258d1fb.mp4?token=ZNhw-YcQRODdEa7zG4pm_n-XJcoah1ykJrYAlMgaEtS3AJWDOsNkwprUFDjdqcbCjupI2RVDI4L4yXmQlG7Kr4Y_Hv2hP5wvCMuyENEcZpLC32Niyc8FQRaypiL2kNDXGxwGca6u6yIUsoBKWcOo1uYOl3KsEHsc5lTDE_bo7ydLTeY54zuLh2S3dEt8b9OGY0M9yRrWVtTxOhLEfvqTFG2ihN1_f_IpQhT1ILDp-ylLf5cS5u3CUli3MERXKv1MNhfeL2KXr1k0PhHzaBymagPRnhvx3Vi9zUFumwP61m9I_3b_lGX__DrPJMoF0CkVzxvF5PVah0WeY4TTss8s1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
صحبت‌های هروه‌رنار در رختکن تونس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94701" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94698">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM05B8QocGXAyRug3I3V8ujcPDmvS_shUkA__HHbXo_vfvMCAqZnEKmDOXO_GApgKXGk9YI3ac-L6Lo1Ravcd3CrA8xxbGyB5j9MgiifYepqUJK6NLq0KW13s8_Zmv5xvZx_VhWfZkiiUmWIUpwkZ1HJLmGOlmYvZ1R1Gpi5TM_9Vr8o7GcEmaxs9GNhZlHvbqZJkkI9VjAWbq-M4ppCM3mg7KbjJutUJb9NHTz6n0ElKAZG2aQB2vrXFUFnx0xtLOaF7JWqnwBc54q6Ont0HudOPV4hPCFAw3Nji24W2QaOrER3m-lyzY-7rpXAV-UYnZuUVKbJEXG7FCB8YCG4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇪
🆚
🇳🇱
🗓️
۳۰ خرداد
⏰
۲۰:۳۰
سوئد
🆚
هلند
📌
نبرد دو قدرت فوتبال اروپا برای صدرنشینی گروه
؛
جایی که هر دو تیم می‌دانند نتیجه این مسابقه می‌تواند مسیر صعود و حتی جایگاه نهایی آن‌ها در جدول را مشخص کند.
⚽
🔥
هلند، یکی از مدعیان سنتی فوتبال اروپا که پس از توقف غیرمنتظره مقابل ژاپن در هفته نخست، حالا برای جبران امتیازات از دست رفته و بازگشت به کورس صدرنشینی به میدان می‌آید در مقابل سوئد، تیمی که با پیروزی پرگل برابر تونس شروعی مقتدرانه در جام جهانی داشت و اکنون می‌داند با عبور از هلند، صعودش به مرحله بعد را تا حد زیادی تضمین خواهد کرد.
🚀
⚡️
آیا هلند می‌تواند پس از لغزش هفته نخست، قدرت واقعی خود را نشان دهد؟
یا سوئد با عبور از یکی از مدعیان گروه، یک گام بزرگ به سوی مرحله حذفی برمی‌دارد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94698" target="_blank">📅 19:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i-xlXL83r-7af7uPBn4DqcmjaPqvykzijzfOApmQzwCNmQptS7Y-Shf56hpUUOtFy1g5ZPytkwlU1YfjROXR044-CmlIv2xhO2EoWo-EQncYNUpSumDNFBmudzElsuWVKG0vg6FWsFdjDRDfOolgF3cdOJ_7rw6lnBk9FmQN9eC5ZQMM8oW13mHzUz_qaxtYHF6qvg7u0zVY5UagpNpQGLmHZrGNUX6U2vf7CaSiAeFbPVPcfrjFPEGOVKMupBW_K7GkF802HCUoGO3cEPkaWd5EZ2KyfY4mE_xD7_9AYBV1MFHOhrSTfWOh1_IHLtxsoxxGUYO_D7lkRhzUCvzvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_HJa69P3Vvb09N0_2egJEbJxdnUIjEJi4A9wfOR_9kcaqscsS4PVTKdrBmutzZNltbRkaWW09GbaqRWMMrExigMCTrr1vryDPOiiEm29Uubk4GBgbWV31ZamTK7qhMYdzOIcG2O4KvlqTfMIPp_PmCBxqn5r2QRb26Iaqvsz4SXjJDygDTlDcFCkf3VKP2BSR6CKDRNfvshafiC6mLG4NPaxf5x10rmmE6hdVVHpVEBj5RTw0njuaSgpwajydbRpX15MoOMCBGHrWld6omLbNe1NyzT3rUvpSxAyG-4WU52frACyh_83YwI6MYWmSSFEGwen5t5WsoEhk_Eb1R7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cDO6B5F2UYE5Mrffq1R24Zm0kFQ3XsmEkAqiINK7aW4xNMdxUEpbUiK7We1sBjmfohs3roM_sy4EWbiVHrp2mxBplnAzmUaSG7HK5WV3jliiZAquBvGZrFZqAkWBfnM8KRI2t6qoD_ZURHMB9sRrR1UVMc-Vy02QLc0yzMfkNXuGiuqIvUX_muw4EJNDwKVUPRfeMHbWdX_iVDhzav2_p6S_fSlkTVqphYYHomFnlW65AzNZN2mKx2_MlcPjOvgdAbgXfYSRS_0yPLp0LLmp2TUs6CXx8qPJia7mvUmoVNJadPMaIjRo3azHF8zHZtAqyLRT77uxav-b95_imLcrbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EA5OzsTNn1jZ81Y9qJ0Nc0te88yfG2J4TfRc2DKtoNHExChD4WGUjnKDFanHcJrDIDvK2k39xrKfIK_m9h9HYrAWBZuhsX4Nlff1sk2soFIJC_zCi0IUHMeaxkJGCp1bv4dMsfVlT1E-dgci8r75Nfc2BKvn49EqB3Qksk-pliyN1EsCuECrmA1_94cY1jfgj5jhdOwtQ851ZSNX-7k5YGqRLIoIICORsyUl-JAic_VPxuhh7GbOWnvb5PGwNT_IYneGF93obPj-4oyBowzowgjhkoMtT58jvYZkXgMFDosVq3VvRYTdsG2JLsSMnoeTajYvO3PZBgAhVrwoY0TNDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم ملی چند ستاره فوتبال در یک جهان موازی
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94694" target="_blank">📅 19:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3gYpO7AUJceEyfngHIf7hXoTufg0262cWz6SP8g1apjSquNmsTWi8u1lGK1FLwpXKzJBPl-vyZ_98Nll2kuddKRKpQbOfW-6z1TeYCkVGBimEaSsjZHF28XXpNMEoCoZlLzOdwG_IalIIJPwIcERPwUA9o_VRIHrf2lMFImNpDjwCbQfZ9atBBA8cQ9tyLzFTw4_qEHUEd56NBqHISnLximadT8umEGK5fsmu9XMD9vzXZZ9VH7grVIgLOX529F5D4CKt2IYVK80cbx8ST4gbqEtCUxGg4CQYkEKNsW_MLv5wRBRqeeLEaUPTkDzmEnRy4TSD-EBWrPil4Sm-Tblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب اصلی هلند مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/94693" target="_blank">📅 19:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XB89v4wYqT5AqmscS_phrwy6iCQvlAeiYEe0VxFzuVufMvIHovnyMABTeRNtwRZibhnHnJf30D38Brcf0bJ8h6OnkYy_c2fJaf-RQ4H7un2HyPHezUf7Z5f5PQw7Rj7ODG0p-OlmeuJVQpvFaRT_2x8k5RZVCLDGc3bgF0lHosew4SZnNZ9BHOLNerdMit8lG9VXkYNCsBzUJfu5NJyIJ8wxMReJH1twAVzCLD0K3QSMaUys4_0r5KaCa6yR-2YhYTkgTNVH6ti4NfhnNZ1lxgTkZZzvkUtC9wTiepxX7zWc1eFzDAVUUhPiKWw7SpOhLL0AF2nIne1OyJo4WMJdMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
ترکیب اصلی هلند مقابل سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94692" target="_blank">📅 19:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFLZyPBWKWg0ZkS6FaOVZKkLrJO0OTZDUwgGFaTErh1GKLgWtxhoEGBV_pzz-Hk7qBBsXW6vnvw_EjqCmZzWiznV0WVK2Iso5texhU_pCVQcepSQy8yJJvQUUStgAU1lFftkKUsaXIyRePguAaz1m_r651i9fmA47pCTlI97a4wgqVH7kmDwLyBLdM7s_i2ZxZb0YOA8JqwjhRyugpRnBeXuQO6Q5dbKBbc32eFyjOKVj1gFVum09nrQ9AeF91WNS_elTV7CismtYcDNlpXLeXmwhChC7YNEqUvJy8eu9-4oATYb0K8B2CuQ6kBtOwC0AsCXhEDEyovuw4e6UQMMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
هوادارای هلند قبل از دیدار با سوئد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94691" target="_blank">📅 19:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUjwao8NLM1jD007uUazFwxaxm1shsiIHUBj0To8yCxXXewuRPItc2GjUufd5cyDlQpEfy9LYW2WnmO6uzoxjNAvzKDWQ2G-7g2h48TCbLdFGRpxY7luruOXD9T_TaRwdkcSODKzLzToEPMK5lGi1sLpqrlIFQM0P3GnZwR3eio6nWDec0p2uIEaakvcEHgv03GIuaN5pmp8-jZY0ni2xMMmUTj9-HFuxszm-MappcuJ-BgJRIt0okN88fbUQHd-bfVY5JlmliF48W7SlQEHVNpGmrSUVkVUZwNSS7Xg4hhL_HvAQlIbMazcghlAVQBT0L_GPdzdcol9HyIyW5-30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در فینال با چه کسی روبرو خواهید شد؟
🎙
نیمار:
اسپانیا.
🇪🇸
🇧🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94690" target="_blank">📅 18:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTkpsHglxMHWjtN23qWIbIxOPEYxuEFn_YWkv9MuxW0p-i6nYVVKl4oiHe6QtFMIyyEtScSboozRUUu7nrdHa5BA0D5k1yerO7hbigRC5Gty5dj-PJW6dlSNaHLfvXCY77QPMehRrqIutZNC-Ye8E-JWXR-AYkGnFl2BB5H3zWl8TqXMLuJmhZizFbuDZuxJtdza68jNGDaf1mockZxZCkc3q0tT-dM4YeT7K47SI5q5krsUgoi4YB3ruTh-dexGMYNc1TSXsgHBpzQmp6myB1ZYWTx6_1gF3etILrQkWqhH7olubLJ_axGBn0xO5alMYY7OKObkRRGGfUW6T7Jmvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی یک درصد هم نیازی به تست DNA نیست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94689" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Alx-jbeiR2xz3jv9or-uW2XYXeLZcJ0q8SXrVFXSeubYOgBYZU3aZJwFt-oAXrwHNeWeye80OV3X85HIIC2WavYNigFo6iNLq4l75WRqS0yA_dWLUEAv45_ZmpHPzUvSqOhl5VkfeL4oYjfYwI6ivWTLj47da964Zqdf5Q5Q-nOdNKipOB48OAvYi3OqQAXUDiASzA40iAFVRDJZ0XHeplXe_YotrpzQiskC1KbrRdeWv-4-Thk5BJ31qzfCA8hehpYig6Tl3SwHPNUjmu_TlAKiryr9v9twII1K8cXhLuPiGmvTFfNa0zuVdkFeHRCUl1n7F6s0J-EUoUX5quUh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🇺🇿
هوادار جذاب ازبکستانی حاضر در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94688" target="_blank">📅 18:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGGH88M7PPEeXklbTPAN9ZRBjaffH4RgsdnngbpaDXkVQRHZZcODmC5pziOT8zY5UT32_WrZLNnWsH38vJsvl-kjEMQHzPfSRcL2u_-PhiIaSmxmJwxiSMOcx9F0XYCrhgeYizCRY3gXVOgPzTD-hPYRAAxK43jG-cQWzSeaT7KCLhmFxKWmFTt2eK0JGAjsbvqKLahPRCY7QYHx6Z8mN8Ka1yMmWQxjMgyc7Id_-GKufNa1ViqLur6N8wHaG39u-VPKTiazZ15jh03aeQqBynXIAl-m5sSk5nzJs1UMmiVVH_4oDYdoyYPVnaPL-5rXYN-5FFGHrYhgHmXU7HLBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇳
🇯🇵
دیدار تونس و ژاپن هزارمین بازی در تاریخ جام جهانی خواهد بود و داور مسابقه پیراهن ویژه ای به این مناسبت بر تن خواهد کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/94687" target="_blank">📅 18:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Y3kBse1koZKA2sYteeeCptveR-i2JY_deXHvsWgHkMXLtJYLls19MwYHLqID1cahIoxh3n_pDbz8ANAUtiLAZ4zn24_f2Il2d0FTGxgUJNTyD9N_FrqexQJN2YMu37IwLtN6jqCq2AzC-PNpJecua7c4-5J-AaxCcTg8x1bnGC0dKtynmIr57_RAdNTWcAPRVthxqaWpQblbegWLMvNGvOA9e0KM-Yte7JEarf42WhIxHgp9A--nFtqB0ccH9tvUMkIQdEsc-s9J01HITfm-nSO2XI18tcszm0aRABdKjzkYlmuKIkBGe1U8f2OxoMGPZcSn2_TCP7Y8FEqJMsKF03MXtobwTAIuhqCSiXL8owI9N4DLxjtj1NfeHpSN8Oq_Lq2Qw8ac4PobBMun6NX54UD5RWT-wdZRQuUOnT8BuDdoSHe1EryiZ0EDJj8V57e_dfpnXnaMCKI91LRf33s9yiwzDuRBB43A3G80SP_yNPMQoMmch23qn_JePLatun68-_eO_agc9MlPsSi2MX03dq07TC8r_jbF0Q0ni9uXHnPhGtxQA45RfPm4rSNJxg2eCn4HrlLfCyUqDhuJKAL5oNCL-DkjY6W3ab4XYpcZaMENWaFME92OmOUXoDLqmvmP9Z1Sd-HViGeu5hMr1jvgi7yGrNFDkkRSX_FHfBjx-cI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f6fcf9f4.mp4?token=Y3kBse1koZKA2sYteeeCptveR-i2JY_deXHvsWgHkMXLtJYLls19MwYHLqID1cahIoxh3n_pDbz8ANAUtiLAZ4zn24_f2Il2d0FTGxgUJNTyD9N_FrqexQJN2YMu37IwLtN6jqCq2AzC-PNpJecua7c4-5J-AaxCcTg8x1bnGC0dKtynmIr57_RAdNTWcAPRVthxqaWpQblbegWLMvNGvOA9e0KM-Yte7JEarf42WhIxHgp9A--nFtqB0ccH9tvUMkIQdEsc-s9J01HITfm-nSO2XI18tcszm0aRABdKjzkYlmuKIkBGe1U8f2OxoMGPZcSn2_TCP7Y8FEqJMsKF03MXtobwTAIuhqCSiXL8owI9N4DLxjtj1NfeHpSN8Oq_Lq2Qw8ac4PobBMun6NX54UD5RWT-wdZRQuUOnT8BuDdoSHe1EryiZ0EDJj8V57e_dfpnXnaMCKI91LRf33s9yiwzDuRBB43A3G80SP_yNPMQoMmch23qn_JePLatun68-_eO_agc9MlPsSi2MX03dq07TC8r_jbF0Q0ni9uXHnPhGtxQA45RfPm4rSNJxg2eCn4HrlLfCyUqDhuJKAL5oNCL-DkjY6W3ab4XYpcZaMENWaFME92OmOUXoDLqmvmP9Z1Sd-HViGeu5hMr1jvgi7yGrNFDkkRSX_FHfBjx-cI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇺🇸
آمریکایی جماعت اینجوری لب‌ساحل کنار زیدش بازی فوتبال کشورشو میبینه
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94686" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94684" target="_blank">📅 17:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=is4-QOJfeFw1Vr_ftMAl2QM32_qp4r949JA7-xiHG8piYOs3p3FqLIZc6mrb19RbE_fF1x8zswj5NOPwu0XvSygmq0yVCk1qYgMQzPOahn77kr8YqrKJt1rGaBuajHm2pks84MJTurey9vifl-zx-VY9VAxxfvsSVtaTxVVR043esfgP8_89Q3zbeavhsoB741X3BoqAP_8a5Gh9klWiCBMPDV0J1qoCmIYdhpSaf1fOkL7-T2Mfhw-SaQPIwHBaFSc7cAXA4BHHGg2DUCiPdIUBBtbkjklJdy7Nq5xEMry0550_NkAHMaXLLwX_ePYu5OSziYKdvMykpK9JMrsLrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c3e66478.mp4?token=is4-QOJfeFw1Vr_ftMAl2QM32_qp4r949JA7-xiHG8piYOs3p3FqLIZc6mrb19RbE_fF1x8zswj5NOPwu0XvSygmq0yVCk1qYgMQzPOahn77kr8YqrKJt1rGaBuajHm2pks84MJTurey9vifl-zx-VY9VAxxfvsSVtaTxVVR043esfgP8_89Q3zbeavhsoB741X3BoqAP_8a5Gh9klWiCBMPDV0J1qoCmIYdhpSaf1fOkL7-T2Mfhw-SaQPIwHBaFSc7cAXA4BHHGg2DUCiPdIUBBtbkjklJdy7Nq5xEMry0550_NkAHMaXLLwX_ePYu5OSziYKdvMykpK9JMrsLrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آلمان عزیز امشب بازی داره
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/94683" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=UM_UxkO_HX5t4YJuyB00-0UDJmTUVAVbKULaFcCN1CSC3G8fKoqGAzltms8mL_Y2EzuMeLht4cDQAApdNHJ_WvM5iTBQ8WRtadRyjZj-JFw3n0kt33TJFjfpiOpiqKsZ7mOSItOsnHezNe6kjkxCLJ8-eQLW23vdi06VBihhCC7_Xqr7w6aD1-WuwZ7X_6Fu337hZFkB-ifyl1lj7mexhPzaIts0PRcs1W6wOKqokMoMs1J7I0OikTnxRo2X5Ls4TOr3BgbHIiiGLmoFWN1vqIUmtQ-sZMyhM9jmSh9QxJ4rpn_l8G825sSkXue86CiQih0YIJwMTtBbbaeFx-5Ztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea2896bfd.mp4?token=UM_UxkO_HX5t4YJuyB00-0UDJmTUVAVbKULaFcCN1CSC3G8fKoqGAzltms8mL_Y2EzuMeLht4cDQAApdNHJ_WvM5iTBQ8WRtadRyjZj-JFw3n0kt33TJFjfpiOpiqKsZ7mOSItOsnHezNe6kjkxCLJ8-eQLW23vdi06VBihhCC7_Xqr7w6aD1-WuwZ7X_6Fu337hZFkB-ifyl1lj7mexhPzaIts0PRcs1W6wOKqokMoMs1J7I0OikTnxRo2X5Ls4TOr3BgbHIiiGLmoFWN1vqIUmtQ-sZMyhM9jmSh9QxJ4rpn_l8G825sSkXue86CiQih0YIJwMTtBbbaeFx-5Ztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابوطالب‌خطاب به رونالدو: داداش مگه ۲ سالته
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94682" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=stzS0-fPMIa38EjN0Vl-8zsNheGv1XX4zugRwfPAVp_8WO0l-sawZBrIvBjqnF6aIMVb8wODnnwjSq97AUmjc1zOmb4pl8gstdwIUpcR3wQ6cJYkmfQ5MT5vsM5GH6oQ9W8t8htKPvEOWl-gYlPyrlXVZYUfdzKQtiE7x3K3DwrvSGrwATLlKZB_0Eb883B8Sf5GReVHIseDWN4NqXdidMug1sNl5nSXIHJyDW0lRpIyezP8xSwOU5lNwEEz6UkCixw_u_WEiMSdNO0F2b7DLytvWDn4wnTMLyAuiTi_te7b7TnxuD8cQiUrnu6ntFCY6XM0in6qCpt4OTvEcQdKcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d0e5cc13.mp4?token=stzS0-fPMIa38EjN0Vl-8zsNheGv1XX4zugRwfPAVp_8WO0l-sawZBrIvBjqnF6aIMVb8wODnnwjSq97AUmjc1zOmb4pl8gstdwIUpcR3wQ6cJYkmfQ5MT5vsM5GH6oQ9W8t8htKPvEOWl-gYlPyrlXVZYUfdzKQtiE7x3K3DwrvSGrwATLlKZB_0Eb883B8Sf5GReVHIseDWN4NqXdidMug1sNl5nSXIHJyDW0lRpIyezP8xSwOU5lNwEEz6UkCixw_u_WEiMSdNO0F2b7DLytvWDn4wnTMLyAuiTi_te7b7TnxuD8cQiUrnu6ntFCY6XM0in6qCpt4OTvEcQdKcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشیا رو ببین نعمت خدا رو چجوری حیف و میل میکنن
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94681" target="_blank">📅 17:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-2kWj2EzgYeQdTdxIN1mSVtc7uAWt7oNY6jWq51aUx05dud5Zprf8CRmcvbZN8NE_1IItNJsduhxNswbeKHQaGp1mXxI9e8p7JwmKwSNOUBTPFe1UjP2C5vQ5c9iGgW5ARmR4bxijwCI33f-K-n5WMdPC2LbuQtSOyyrEaAC5hhqtmTeYIMAA9TT5UL4bkLoFK4-MIyhdEkfJdQ7H2paS0kAZ3Pj7gbB_tfcwUonCS80Bv8vjP1sqN22M_ny9IvAVtOeotTbD17pVogwT-zZLEmzEgxytkd4X-za6Ggej3xImjJu-WlD9bNCclGUSGSJ12Iaovq0uFZqNFwkWEnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا:
بنجامین ششکو گزینه جایگزین بارسلونا در صورت شکست در پروژه آلوارز در تابستان امسال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/94680" target="_blank">📅 17:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=I__rJntdHS_nYnsGTZkkDN5UnXE2CFca3hRUS5I8-KOvnvY-HuHPRXrj5aOB5_lW3TN3dbm2_wH9cjUw4TzvmqOYnri0zjNXpxXbfO53SmR2XQy5Muw57GD_M244TRjpd1hYRj9f7WVRryVArTLeaPbOQ-J7ZtUjJ_P8zQo6labt-tO_AZjM5UrCwIWs6pb2ZogTN8NFvkiQ7IvV8vU-2ATAV8CWOHlmuTvY20nebhSTSzt_C-ZnCc7dF7aUnbITyuTeqr-gbHA_lnIph9SGIur2EOypOlpRr2EAUXikG0FDbyYDHRjDGjmrPE8GvNiDgTbFJMaRATwvYLbW-9hrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a1e82acc.mp4?token=I__rJntdHS_nYnsGTZkkDN5UnXE2CFca3hRUS5I8-KOvnvY-HuHPRXrj5aOB5_lW3TN3dbm2_wH9cjUw4TzvmqOYnri0zjNXpxXbfO53SmR2XQy5Muw57GD_M244TRjpd1hYRj9f7WVRryVArTLeaPbOQ-J7ZtUjJ_P8zQo6labt-tO_AZjM5UrCwIWs6pb2ZogTN8NFvkiQ7IvV8vU-2ATAV8CWOHlmuTvY20nebhSTSzt_C-ZnCc7dF7aUnbITyuTeqr-gbHA_lnIph9SGIur2EOypOlpRr2EAUXikG0FDbyYDHRjDGjmrPE8GvNiDgTbFJMaRATwvYLbW-9hrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🏆
واکنش تونی کروس به حواشی خطای مسی مقابل الجزایر:
"این احتمال وجود داره که اگه یه بازیکن دیگه تو همین موقعیت بود، کارت قرمز می‌گرفت... یعنی دقیقاً تو همین شرایط. حالا بذار یه چیزی بگم که شاید خیلی‌ها ازم شاکی بشن هرچند فکر کنم همین الانشم شاکی‌ان! ولی به نظر من مشکلی نداره..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/94679" target="_blank">📅 17:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=q1n7SEIn33RDMKZ-3ErSimTi3MthAcjx_mUzq-7CiFHF2J0XutmJCKbnnuYR3mKiBOjpK6_UcbC78T81JmEbKxrY-hTHopO7bOeoALIjhHKU1C1pZQJVoXxGgjbfk17v2EgBhujQun5MyU_Mc8FMosBRHSPnErrBbHLn4-jRpGejr_wfrMhA3FRLPN5d6Ou4Uv69Y2yALToxF7ia0OjFJ_Dz0w3mmucYwqhpFUTMIXNoAfqW-SX-oMMnRnQgx2mb50UU5qFSN1nw_6lvWuz162kRAL3X9EYt7BOY9uXZmAI4VnICGt9solrAtGAa9ODX2hOfW25eD4isUL3LI0Bpag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ba1b9f67.mp4?token=q1n7SEIn33RDMKZ-3ErSimTi3MthAcjx_mUzq-7CiFHF2J0XutmJCKbnnuYR3mKiBOjpK6_UcbC78T81JmEbKxrY-hTHopO7bOeoALIjhHKU1C1pZQJVoXxGgjbfk17v2EgBhujQun5MyU_Mc8FMosBRHSPnErrBbHLn4-jRpGejr_wfrMhA3FRLPN5d6Ou4Uv69Y2yALToxF7ia0OjFJ_Dz0w3mmucYwqhpFUTMIXNoAfqW-SX-oMMnRnQgx2mb50UU5qFSN1nw_6lvWuz162kRAL3X9EYt7BOY9uXZmAI4VnICGt9solrAtGAa9ODX2hOfW25eD4isUL3LI0Bpag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
روایت عجیب یک هوادار فوتبال از رفتار زشت مدیران دزد ایران‌خودرو بعد جام‌جهانی روسیه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94678" target="_blank">📅 17:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94674">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tygfdDxz6J1GYUtXzMw9IrFbAZDyt8XlvP9shI-KJfdkOamXSMYcPzKTnXFZEg25hPuII1jaSHB1MlbaAUPx1M9W-5QADp2-sMhhrS1AFz4p3VeMMpQKGxmXGrtQl6tKSIwP9G989Up_zHBn3eLCa2clA0fPgilJtXIdMcx6_rF4X3WGr2ENrl-I1U-CVucwEKLvgX6B2-KutrjO-x79tmZ2A9-H_3MdbklMYtfVwPa20-96wevNc2H30bCnEhctmsJCXsOmlLW7BQ4Aquax7packdOOl3zd9l6EUNwXB8xHDtSwnTGIeFSoqf_u0W5lLPqGWlKFvje06RYVuuzR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0X6hnHxh37AsSRVSyPsyFvyz6dHgMXrBZUzOd5mSL7JbAXiH9cxADK2zy0508yCh2kG2NZNDD-9bLeeBexUJ80Wu6xhO29nSkFtjr2YLkzsh03rn4i8PNbYDjy0YPN_UIGeZxCV2gEcfcPT-MHkXvg212kpDkLceZDl1K4nw6_IdWc9CszXtoKM5ffrZ60_MEhEKQ1iWFI2EFCz3hZ3GDQVR3WsIb5yhry5bDwd3GZzflRkX6JjumhsevVAPhUdROvuJiqL1FnNEWPvFlOJjxaITTBuuKlhqjAioLyUEHu_bdY0wM39QW-c_TCcEmir2MtW9EovIXC7sapX-tx21w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCUEYZo479fjwdJbR-xNAfEdAP4LYp3GANdxbV-rWqmPpdbrwPLumEEVfAyFHJIrn555UJrPbRSrHqML3NfhMTrIrVAF-N0jTzBJV7rfBRuoy0zKyR6bKdI6HFFdhX2hhl74aQbsfxfOWQrHG547JPaUnERZyLTw5VSRGMFuBh9IuoJGtrcOT6rJAOsKfjwx7YAqm_yEnvunhYOgs3P8UNNLVfh-JbdsI_f630hZlo3tSpCjLOxPHxSIwKWw6Usjx3QGy4Eb26CaSKW7yr4ZtTVgaxdkCCX7PbPXft5vQazngTo7GDRg1n598zPhocWzKUtElgijQrjgcxl0dmtIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5Cp6jFrdX6Qku6px4Fbb6ItHuj-fMpr6QCpSYSAZnc99PEAK5rlhwuWZr-uB9cHsRDB-P32C6oaX23s5GzuZxrRXKsnFs6kZ6wkSYs6-nr-uiuSgdb1GYyDgyNa2swcb0CSb1uC3BIIUAIzVO-RXeaA1XCsyYX1of9SmHztl--N7iwosdKDjJ4xTkD_yd_9fvYutYW9KPDVsHX0gcUzoBM1uktpixCZPTO_AFReTIdREpD-ICNpUWnpq4C83vsT4Lzw86WgX7Rg5tBcStQENJHBlvfKQMCyqJIy4pt1ANzq0d3QNnGPTkacnT41_kWvz-8pWKtGLDBdAklTt_ZoCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌐
اولین پست‌های لیونل مسی تو اینستاگرام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94674" target="_blank">📅 16:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94673">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
فوووووری؛ طبق اعلام قرارگاه مرکزی خاتم‌الانبیا با توجه به حملات اسرائیل به لبنان، تنگه هرمز بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94673" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94672">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=TCzRR1C0300eXpQKojrjGaULrJpZsbgR1tq_LzvBR54UcC_brFiPWCEoacJMLWNnlsph18mjG_gWD2OZinlRan9cjJM_Znz5z_WzRWa-Xgop_5dJlA0YXLrAzdBSnd9cieIf_w88KrAK9VkqRFVBk05R3SQohwxr66-dqaFCaqoX7PtgRKeAbhpHmuBGkiqGN4CSegm7nX-9--hNal8S6t9uUr2rBxn8icuw_mFy-vxmG6ZodYt7jw746m6ODizUxdzQgS3nWxx65uQY48LnDAA73wkH5hLXZ1Txzscx28qBLb2EeqysDoZ_Dbbb-bM3uC31rLYHXAqOH2rgaoyIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69f2f6a0fd.mp4?token=TCzRR1C0300eXpQKojrjGaULrJpZsbgR1tq_LzvBR54UcC_brFiPWCEoacJMLWNnlsph18mjG_gWD2OZinlRan9cjJM_Znz5z_WzRWa-Xgop_5dJlA0YXLrAzdBSnd9cieIf_w88KrAK9VkqRFVBk05R3SQohwxr66-dqaFCaqoX7PtgRKeAbhpHmuBGkiqGN4CSegm7nX-9--hNal8S6t9uUr2rBxn8icuw_mFy-vxmG6ZodYt7jw746m6ODizUxdzQgS3nWxx65uQY48LnDAA73wkH5hLXZ1Txzscx28qBLb2EeqysDoZ_Dbbb-bM3uC31rLYHXAqOH2rgaoyIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇺🇸
ذوق‌زدگی این‌بانوی آمریکایی وقتی کراششو دیشب وسط بازی دید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/94672" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94671">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKQomSAnNmXTA-Hl8I4kBk0aSlEgdMkJfhTUHEkFqR5vsGbzVS8Yl___YnC-KUogWj4f6efvbo0V6rNx1_VQ9bqD-3WUYN5PRoydzs3-agQ7szUtaso_00go18gwPTlYnSqzTPtEeqgwzNrEAswfV266e8zakPc-kaq2hEHYNua93AEZHEpxg3UcwbFkvHFcy3udqsEr0uhuy73Tofh80f-5K37qV_re0ENOelQnkJRdXtN2vCkiDZitLEjRz1ihC_ObG5UgvraPe1WkhEP4fy-Cf4K8sK9bWCC7eFd4Wh4H1YgJKeHorEfdgP1dN-KVAdFbdciBcRxYhu4vOjng6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کول‌پالمر و زیدی تو تعطیلات؛ ایشون پیشاپیش توپ طلا رو برده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94671" target="_blank">📅 16:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94670">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=SXIhUdmwsOY2L9iEAabUI2FGTbrSkRXNQIJAwreBULTgL-lgZa7_t-zwLpGL0dBeZ97riOHzWcq57HoJoymBCio0iatUt6EM7Bk1ijIaEAuxoZE4MUKTrdWzfLkqi2FRtNpijqMUgDbjI1OCdnjzkEnGWG7zjGbVTYC0lnp4SNSqZMl-auC8_RHvyrL9MuYDlk-_XTe1n_M1Gj2_v7qoYtZNWGZPzQX8Gh6BWhREj9gAOTBmZTbWPzjxcRw6Ye0i62jmXx7ucAChLpMLBo1JIMc6M-z3ngy-hWO2JePgczE-9V8-Q3WCdvq45ewWJ2GnV_VE_Ij5XVC1-8rPPviWuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b719b1cac.mp4?token=SXIhUdmwsOY2L9iEAabUI2FGTbrSkRXNQIJAwreBULTgL-lgZa7_t-zwLpGL0dBeZ97riOHzWcq57HoJoymBCio0iatUt6EM7Bk1ijIaEAuxoZE4MUKTrdWzfLkqi2FRtNpijqMUgDbjI1OCdnjzkEnGWG7zjGbVTYC0lnp4SNSqZMl-auC8_RHvyrL9MuYDlk-_XTe1n_M1Gj2_v7qoYtZNWGZPzQX8Gh6BWhREj9gAOTBmZTbWPzjxcRw6Ye0i62jmXx7ucAChLpMLBo1JIMc6M-z3ngy-hWO2JePgczE-9V8-Q3WCdvq45ewWJ2GnV_VE_Ij5XVC1-8rPPviWuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
سوسن پرور تو برنامه قیاسی: ژیمناستیک خوبه چون میخوابی پاهاتو میدی بالا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/94670" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94669">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👀
🇨🇦
🏆
در و دافای ایرانی مقیم کانادا که شدیدا از موفقیت این کشور در جام‌جهانی خوشحالن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94669" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94668">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=HE06-r2nSH0TCu8Kms9zFGCuzu_XVqpA_QtrVQZWaKlbGvyKE65HU7wdnIOJ1Tbj2K-lrHmuWT3FOFMElYzobBKBZfxpHd4kXheMrIzHyxNQiWlLSkDbwxIICkfusynTlpD1UBh3TqzuUClSLRxOFWTRTrEJjq4kMDSulM0J5ZZZ9yOp4Y_2_ekwpkXp0VDm68VTs5g_00qrD4PpkiHxHIQT0JwjA0KRhCCKcq5jxSS0G9A8w8_xo6Jo9sVYeiAq3-Kop4NN9OlH5bivOlJc4X2PuwRz6z7eZmtj_aQzKvg3hx6AaFdiaUBCSnCi5XtfLZizQijAhty3z53rlcsFTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cd9b0ec79.mp4?token=HE06-r2nSH0TCu8Kms9zFGCuzu_XVqpA_QtrVQZWaKlbGvyKE65HU7wdnIOJ1Tbj2K-lrHmuWT3FOFMElYzobBKBZfxpHd4kXheMrIzHyxNQiWlLSkDbwxIICkfusynTlpD1UBh3TqzuUClSLRxOFWTRTrEJjq4kMDSulM0J5ZZZ9yOp4Y_2_ekwpkXp0VDm68VTs5g_00qrD4PpkiHxHIQT0JwjA0KRhCCKcq5jxSS0G9A8w8_xo6Jo9sVYeiAq3-Kop4NN9OlH5bivOlJc4X2PuwRz6z7eZmtj_aQzKvg3hx6AaFdiaUBCSnCi5XtfLZizQijAhty3z53rlcsFTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
بازیکنان آلمان قبل بازی امشب مقابل ساحل‌عاج این شکلی تو فرودگاه تفتیش بدنی شدن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/94668" target="_blank">📅 16:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94667">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa21338643.mp4?token=dykcHQ_rUkwaS7L7NnpSk47uboEXSGuzHo15hfmZJsc9LUKmlspvX2yEc5WOQ-boB_AKr4iKmalRCKw1bKkt8PlPa2txLGZM7NDrqMbbB0cjrsQSCr4-X2fyBdAxqjZuAasA-Rq8RbSEdK15OflXbpILSYAT2QjGwmXPLrq7t38Aod0IVvm-iZJ7wJZdALzO8FpRc2Nf4pCFASvSFbrIDEtj45W2FuRNvS408HSQjE4IFDF0f_oPU2tpmD4Z2ggXsRaP8j3kRVr9I0l2zzNzWqyLoWWDsRjnn6eLvL-MsXcVT8ge6yaUz04rAE3-NHD0Y9iw4BVBe5kgwZvUVWJjtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa21338643.mp4?token=dykcHQ_rUkwaS7L7NnpSk47uboEXSGuzHo15hfmZJsc9LUKmlspvX2yEc5WOQ-boB_AKr4iKmalRCKw1bKkt8PlPa2txLGZM7NDrqMbbB0cjrsQSCr4-X2fyBdAxqjZuAasA-Rq8RbSEdK15OflXbpILSYAT2QjGwmXPLrq7t38Aod0IVvm-iZJ7wJZdALzO8FpRc2Nf4pCFASvSFbrIDEtj45W2FuRNvS408HSQjE4IFDF0f_oPU2tpmD4Z2ggXsRaP8j3kRVr9I0l2zzNzWqyLoWWDsRjnn6eLvL-MsXcVT8ge6yaUz04rAE3-NHD0Y9iw4BVBe5kgwZvUVWJjtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
وضعیت عراق حریف بعدی فرانسه بعد شکست سنگین قطر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/94667" target="_blank">📅 15:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94666">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBm8sf7brLl57qjzvc37800PKW3K_D7MJNUVx1nDaOm1yVClNB1b948c2mBTwagmJWYYf_tPLgHJrbRfVH_MgN5NDFNsKVdvZ5YqGxThiBH5KahFawuWgyQHZhAAxnup_36_M2VH5kGBNQYP7PgEuKBDh9rRENJj7rD87pF6XPnQlcpQ6WkWix-nvuBe_je59bqw1hZPOVKgF-jerlkrm8amFAGw9a-xAiqRxOy_qztji2BVg0fzEVrpksdPs3MAl6AG0owQ7kpfsZSOcgQwykJxzRBBasguJSyVVPliPIeOHyS-tE_USFod5bb6Yv9ZFWAZj0EfWFim0P7QThdF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
پر هزینه‌ترین میزبانی‌های تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94666" target="_blank">📅 15:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94665">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvSvxHyMADWq5kTynIw_D4t5bZWbufiELK-1uzQHytjePtxCIsDvZ0mrVTfyOlpwLsNNaLXxxM9bo4i2-LggR4THeBXHwtjFdURNyt098j4hhaRhR6Gy7-uZ3N_Zb6iBjCazW3uSfAhm4QD9nYl21A6RPxQDDYZTsZbjc1o2cD2cK9ia-DDsxK06uDJZrAbAdgjRfnhNdZV96HZlseHXJY6ChDwJyDBqxwn9MCM94vAE4LGSdoIeAa-OTD6u_Arhz1ptFUHrpcHQp8ELeorx8o3y4r1Pg7reh0v03vb9nRoITAi6ysBcRdeGssFqArMsdyOiepj51EIblSEYgZ4zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🟣
رومانو: کاسمیرو به اینترمیامی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94665" target="_blank">📅 15:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94664">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGYsaNtQOhe92gSBAKChUUIRH9eFeQe13MDbHggzzxrRi6kD78WtGGkZx21seKH-XG3jfk2V15DmYpwiuW4XuwhVrZFLyDg0eO9as9O024u3uLuSUc0BW9zuQPLe5jG1ewAE4m1tUfNe2Jb_q2ll2FQ7sWu2hrTxK22p-fNBDB6ImU2zIiyxWYMtMpXoQqTLoQzdgKjiq-Gj-5OoSg7vy-eZK7DLnErTdo-0z7XYzxDdtEYLp4svnOhSSa5eMzgmJVk_pa-7CfE7ry9PAfjzaWgykqVOBWi_hECUrZgaaec7meP4LodCPa-bjCnTsl6cVKxaOT8cRu-rwd5dmR61-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توی فیلادلفیا مجسمه راکی به مجسمه بدشانسی معروفه، هوادارای برزیل هم به این شکل رفتن کیت آرژانتین تنش کردن تا آرژانتین بدشانسی بیاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/94664" target="_blank">📅 14:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94663">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=h5ayBSxzAdTdtAn_h8ljvmEl0Jspu8RGqE9n1XFIIR_qWuV0a1bJBVdikGt89n-JGgTjqHuWyrEYMu_m2oZSJqjshpFGrwgov1xqAEVhZV8aEQWMGd6lMu-SsMtJWMiqk9e1nmceXEmyLXAWpQ5iCqvYFDiyqUk0qP7IevlWlvQTPsTcnJwVEhehtrL-5X_HS49igkECjfwNStItUSZqtSzVmaLYweOhnkUUX449O5A5VxpNBVx2pNPqhCqGp1_kWOqfDiFHp4OVHTFolfSj8BDLG2Rz2kR1P23zojz_ewi7m4qtsUcKF-GE7UUneIHp-fOB395Y_sbh1oTHdswQxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d39566eee1.mp4?token=h5ayBSxzAdTdtAn_h8ljvmEl0Jspu8RGqE9n1XFIIR_qWuV0a1bJBVdikGt89n-JGgTjqHuWyrEYMu_m2oZSJqjshpFGrwgov1xqAEVhZV8aEQWMGd6lMu-SsMtJWMiqk9e1nmceXEmyLXAWpQ5iCqvYFDiyqUk0qP7IevlWlvQTPsTcnJwVEhehtrL-5X_HS49igkECjfwNStItUSZqtSzVmaLYweOhnkUUX449O5A5VxpNBVx2pNPqhCqGp1_kWOqfDiFHp4OVHTFolfSj8BDLG2Rz2kR1P23zojz_ewi7m4qtsUcKF-GE7UUneIHp-fOB395Y_sbh1oTHdswQxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
فلسفه کولینگ‌بریک جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94663" target="_blank">📅 14:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94662">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/94662" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94662" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94661">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu6Os9kfrHTldoDxHNYc81P2EeW0CfWAa8aeTOLp_SRjuVneUuHcRzwEZ5Y9qdabnXMMfWad5FJwGgB15njJgh23jMJG5Ng12NftK7_XnCzW3wG1_CgGLODCc0i8Cfj_yh72D4FXdAQazNeWQo6kPfa-iXHEYYQXfHmwyiE7S0-hZiIO_Hvs5uo9mdfgrFBJb9wrhf4ii4nggJXkur__PuSmVldUJ4A-upVyPqHdz5eJ8g5nq5bvK302xeWQCDfseWV_RZ_hkxmFrDQlQgaEppM1yFCuyiDhScmpu2rPWT7m8qmCMhG3Kpg8161SMS5CfY9popV3ApJrQcB1N7BbWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94661" target="_blank">📅 14:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94660">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplslz7wVgMxAs9QfamWboG5TSqTVEt08tYOo9rmTRFQlGoU6CnNqLFQm_YACoR1FPY3s0my8I1rXFTfLWGwEJ-eI0OuJzR1ZTV2Al3tQWmFWXAZ2_zhIgpZ58v1MoM9D4QFez3gsLAKVh6OsydEomO_WZosf7pbDP7lcgo8YU8jEJdPL6RrtfowLBQyOsXePgwftdAjpXBfVMymy0_GOfBFUgubEAHT8AABZK3sCSLbg_gRHvCYHT8QHXs7p36_PiT0u9OEhKb1R_AtMpMzHwPa6HgDy9rTcNLl_jc7YU-G0JhpBdYebS5iud_EOS9qJVLha_ydpApvOfW53YogU7SUU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b0353a5.mp4?token=EnyC_5kIAR48d39GLXEpjXu57RNQVZcOGPVbpNpDRaV4x9pYSfxnYeuO4ZlyAYX-Z0bzG4zCCTE3DmiCr-dI990Y2Dwppk1QYe5TLVsFEif7JUrGIa5wGvcXY9K2gTm2sHEOEcIRPzP58nAtmeaoPF3h1Da_pk8GhR6GWFCVSeQ3m-p9j2EQN9loiEfNukXmsqVp8d_AAMhqV8YE8Vrlzl84-v6-oPd16e8SbNU-5e3g1afpKZt_DqeyilAKdf9gHvj7KqlYGkUmwDmuOAFuoEFDLjjv90xO9LbKMWL8ICj84k_iwsT1RSBmqwFAvROYN2-5OGyDDCoIsLjXjnplslz7wVgMxAs9QfamWboG5TSqTVEt08tYOo9rmTRFQlGoU6CnNqLFQm_YACoR1FPY3s0my8I1rXFTfLWGwEJ-eI0OuJzR1ZTV2Al3tQWmFWXAZ2_zhIgpZ58v1MoM9D4QFez3gsLAKVh6OsydEomO_WZosf7pbDP7lcgo8YU8jEJdPL6RrtfowLBQyOsXePgwftdAjpXBfVMymy0_GOfBFUgubEAHT8AABZK3sCSLbg_gRHvCYHT8QHXs7p36_PiT0u9OEhKb1R_AtMpMzHwPa6HgDy9rTcNLl_jc7YU-G0JhpBdYebS5iud_EOS9qJVLha_ydpApvOfW53YogU7SUU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⚠️
انتقادات شدید مجتبی‌پوربخش از مسؤلان فدراسیون بابت تغییر کمپ تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94660" target="_blank">📅 14:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94659">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=JYZoKwYI_yv3XKbiWj-e4TdADlhxoy2oDIIWL8Bz9dKbm6rTBfvNo4740ayJrQjSdt_Yo3VCKA9icLt-rho4o2hdmptT2B7pFGggeApveN7vOxaQzC2bqsk9dTqC2RZXfSl0kUENglvsKKgnwfGv58O4MM83zDV6oi6dHYQz_Ltihd52H_vkvHN-un_8PTe2AjKV31lyQb7cs2Y8RZVYPzav7uEMZrPu1Fp0ajZRQXCCQaA6N5sOuLlPgbczhNpw2BDj2OLNt5clZIRfU3SVbpFfSsO65WH6UXeXEeQwEVk1YzL_Uz2XIv62P8OsztaEU9YnXiy1hbpphH_RYariUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07af1e396e.mp4?token=JYZoKwYI_yv3XKbiWj-e4TdADlhxoy2oDIIWL8Bz9dKbm6rTBfvNo4740ayJrQjSdt_Yo3VCKA9icLt-rho4o2hdmptT2B7pFGggeApveN7vOxaQzC2bqsk9dTqC2RZXfSl0kUENglvsKKgnwfGv58O4MM83zDV6oi6dHYQz_Ltihd52H_vkvHN-un_8PTe2AjKV31lyQb7cs2Y8RZVYPzav7uEMZrPu1Fp0ajZRQXCCQaA6N5sOuLlPgbczhNpw2BDj2OLNt5clZIRfU3SVbpFfSsO65WH6UXeXEeQwEVk1YzL_Uz2XIv62P8OsztaEU9YnXiy1hbpphH_RYariUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روزا در خیابان های مکزیک چه میگذرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/94659" target="_blank">📅 14:25 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
