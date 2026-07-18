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
<img src="https://cdn5.telesco.pe/file/LJ5LzHDk-F89vV2ZrM8FrPBTz9I-WH3D28j78MFidbk1xrygZzcTtVO34i5TUqPWhaQY7s1joMUN2X3VEcwzp-aRCMLjhN9r20xsDX-Ilxe7XmxWUSmcXV5XMZXnus4AIBT_nswhmW9ZjijtXULLMzLXVL5sC4RzRGDxVI-aAkqPX8N8x9S3mxF-TuCVTPanZOuBOzQaX4EvFoRI3kHUl0U1iYmBRs0Czo74N2bTAGXsLUqS0q0FcSz_8TmzXQ-WMFqWt1dXEAKD_8Rc7yoOdaVLmvkHSIDrEyrDLs9RehCKnn7VkD1pLI6zMHRkajb83GF6_SeT1GhtnWvHssI9eQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 560K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 22:20:19</div>
<hr>

<div class="tg-post" id="msg-100800">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
فابریزیو رومانو :
🇪🇸
اتلتیکو می‌گوید که به‌طورکلی نمی‌خواهد خولیان آلوارز را بفروشد، اما در صورت قطع رابطه بین آنها، که در مقطعی تصمیم به فروش او در ماه آگست بگیرند، آرسنال هنوز هم می‌تواند به او علاقه‌مند باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/Futball180TV/100800" target="_blank">📅 22:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100799">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🏆
بهترین عملکرد تهاجمی در جام جهانی 2026:  ‏
🇫🇷
کیلیان امباپه — 8.93  ‏
🪄
خلاق‌ترین بازیکن در جام جهانی 2026:  ‏
🇦🇷
لیونل مسی — 8.41  ‏
🛡️
بهترین عملکرد دفاعی در جام جهانی 2026:  ‏
🇪🇸
رودری — 8.03  ‏[کنفرانس فدراسیون جهانی فوتبال (فیفا) در زمینه مطالعات فنی]
⚽️
…</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/Futball180TV/100799" target="_blank">📅 22:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100798">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-8gUoiRrMGYtZ90j0NxP6KriUnLKxmDYZ_iAo6NcGMwf4QfnGEv5eXurdcjTLEHkO1erZAgF6-NU-OFFoYFEjlJLLBuMj08izJNbdpeHHNVrru3yK4oON1sErdxmZV7nHfjJA3PXnw9xpIoSwenQ7MuuVL6sK83tRIfRgO3xvWa3ZqPaMVi54_qTj_rEuuVuW5lAvuF_QyryCoxY5Ay83yqShYju_eiZTKyYQfb8W61Noy__7C3-TqSkwPYHgwtR5gtX1aghsOPOynBhNT-3x34aCxTh3EZFFcILypBm2S0zSI_veNcmBms4ihIJo5ufyQoiTY7QUPJ78FmOFCt-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بهترین عملکرد تهاجمی در جام جهانی 2026:
‏
🇫🇷
کیلیان امباپه — 8.93
‏
🪄
خلاق‌ترین بازیکن در جام جهانی 2026:
‏
🇦🇷
لیونل مسی — 8.41
‏
🛡️
بهترین عملکرد دفاعی در جام جهانی 2026:
‏
🇪🇸
رودری — 8.03
‏[کنفرانس فدراسیون جهانی فوتبال (فیفا) در زمینه مطالعات فنی]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/Futball180TV/100798" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100797">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzPUj5ZdwxvK2s8r7IDpCTZWNtBOHWxNGs1DfWLhldBg8oL3p5tzoZTTqtNIPyoAoZkhtQPGQzB6RJxmGrY87gzORrxAoRWXS6bJjovGrW6LD7mMFrwpCR5nGv3V2B6FM3AAgba6UxEBqqlOcTksM2Gp5LhooMHIfSFsPRUTztni3dUd7-w_inhHo_aXug6fPzryAYEBy6BHnRw-InhgLmgw_32qWjgDgBCGJCGEp2Q753QkDIePZGpUBh0VTtsAXVjnu8pXgrXsosgVGsE2mFymJzD2Q0sRTlwgXliCS7wX481P9mTWKDffZGmA8VA-zvbKChUidgQGSgQjO6k53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندین کشور تمایل دارند میزبان دوره بعدی سوپرجام اسپانیا باشند:
🇪🇬
‏
مصر
🇨🇳
‏ چین
🇺🇸
‏ ایالات متحده
🇲🇽
‏ مکزیک
‏تاکنون هیچ تصمیمی به طور قطعی اتخاذ نشده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/100797" target="_blank">📅 22:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100796">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPgbSo3BsLYlHxlmMQZ4zJ1q1gBPdVJsQ0X240bfk5SZlY3u9SdpyStdrqdNfeSJw9V0UhO6ZkXNS9BUAyNA4Pi0wOhDNbm2J_Gkp_d-zNvDFPZPPG21uCfuaclYqY5PKvYUiVl-jdMTtBoJuDUmQJreStxrRaPC68BAbdFuUg5nATY-GQmJY_9AnsHDDD83DbG5C1JKwtY6ALCj0Ewpo64aLouWV-0BTLmq6YaN3xlOemtqlomsq_UnnRplomPDlJMgyza4pVBBj8EQF1Uzlh9mP77HOG2Zz8OpqQHMU5gbvx-zXiyA8F6NqEGh5oxPjf7TeEs352TQb9oHiGQWHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خیابان‌های نیویورک، یک روز قبل از فینال جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/Futball180TV/100796" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100795">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVmk-vVW_LwemtQOI5bPTttiinBUvN84Ecx-TPFNPXvyzjpvK4ZvNrM0FwAzTF4gnIcYgumxZj1TLXkXu7yvUg49xsLZC0eaBJSENEfi3mUg2-pwl_SGtPxqoBVx4nx_S87GtGeNtUHrxr7R5U8hYITWniMpduWKbvosCDNYMSUApoyPiComemxa3sKWQhTEfdnZ5ec8A16Ksc8NZF85chX3pT-V2e4yW1E8HXUm-gSjiCvmtCJe39Cc1pJZ5UTmPTHnS_FuXuwnPA-kr8pJZKeD7NYa4IVl4vzipo6V04PrpYwxW8_X5RooDu0I0Qou2hZEvBKHcNmGjOCqQQZKSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
مورگان راجرز، چهارمین گران‌ترین انتقال تاریخ فوتبال شد:
• نیمار — 222 میلیون یورو
• کیلیان امباپه — 180 میلیون یورو
• الکساندر ایزاک — 150 میلیون یورو
• مورگان روجرز — 137 میلیون یورو
🆕
• الیوت اندرسون — 135 میلیون یورو
• فیلیپه کوتینیو — 135 میلیون یورو
• عثمان دمبله — 135 میلیون یورو
• جود بِلینگهام — 128 میلیون یورو
• انزو فرناندز — 121 میلیون یورو
• ادن هازارد — 120.8 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/Futball180TV/100795" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100794">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDicZdjH952xuR88zRnCbEbDNIW7duCcF_-foa1fkTOC6RQRGi7IBYfqPQI9NCQxO4AoUoLQgKALU3YJx-RzjtKLFbM3286wJZgTMP0Jctxrv9U2LJJtoKf6TlcAsRurkF-o9qyS_ivBacRK5-Ebir95wXWy37mlqpIcUFKq6ilD26Ueh6wg3EM8qWhpdiLSFLydvJmQ6Cv29dSwxG_SMxcvBsie9KJDIjzERD5QhlmVAom-H30YD4_M-Z0U5L76FDQiYLEDwL5Hlk1J_b4jN88KDHM9JkJ6sQfv3Y-5qhGQggiDTp6S3tHnnX-Xhd8cDmUaAo_w85BXM7NbDG_CPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا و بانو تو تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/100794" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100793">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6aXVSiaPe_62B7sRhFPMFRUkYd8RppNBWg7sEC1DTR-g1g6108IA3FTK4t7pvkFeB079jwQGP0L4tGI5_5t8OzxYexsTOM8UCmfACFliLxw534r3NkNbLBy6oyBz8V0WVut2SwljjTGqSjeA5RNKy20h37xMxiUnVWvMLp2kFrBNlxPdtdV-TnI64ly1wyqUo372mn8xVpO_RYiG9Tp47G9yyGpDbnfJtWKAgo1KVjJMNAJzPMFzxj-CG9TVkN4QeeN6QeXZ86sE15pF3KJyKaXXUH8dtRhmF4GNehXGxesDrnI7FU3Y1iTwjndtPUYIVHYx4ImFoLfa8wopikLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین یا اسپانیا؟
🏆
تنها با پیش‌بینی قهرمان جام جهانی، وارد قرعه‌کشی جایزه
۵۰ میلیون تومانی
طلاسی شوید.
از طریق لینک زیر پیش‌بینی خود را ثبت کنید.
👇
https://talasea.ir/sh/uoa</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/100793" target="_blank">📅 21:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXWR_MJ9lufgfIslvcH0Y_Cd8ZckqmOPMKb75UO2S0r_66fAs-tFzySN8XcOukfGJxXd37SVg0F-sKgzMUo8esDdeyV0hWwLLLNH0C-79lcnfx45zE2QdKySg4b3uic5J3rPfxukfa8KSA6y7Wi2TakpR-MPvSA4hp6B5Gfyd_F9eNgpOWA7VzaS9MK4IJiSHFC117B-E8HwQcpAL8jjXeTEDUZPxMrPjelZ7Sz7wrZX9gWwQmGq0ZntOTPn61uuvMGPqY83AqQL1x0VDWsIfJalryKu1SF4XrI7ERUEA4eKMWSiWuo8V-rAM1TQaLw3rDG5bfkfK2B7ubnXqGqMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8Wj9FbwriEuqvAlmm4OOxjBiAgn1JGg8ZXYyVJYiAYhPHqinZoh_4Fdk8AXr5ndvgU5o-_xzixcq_4lQ-1Sn8TklCtp_KPaFuSoAfMbbpI0yNT9nhXMMeRyiuxm-rY1IF5EkjccRuIBsWccIamFhYsTGsfTamcUzM2_eW0YfBz06TxJxQy5hqiDBjchXMI9LwO7k-Y1DOpb70ayjdyOBhvlAyosHWasysyzAMqx_GH22d1bHK-piEQOBLVWaaNKvUQeEaxGtAn8ehdfYBmUKSmVkj3LjxeuAIS8PPwKRgSMaeZ-Wmx1G-rV-k7YuIk41-YCC_avTb061wsavfJdBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKkBK9Y938Ird09Hv1Vl-TOJgZk0TMojfkPalIVA4wAKBuo42B5FL8yfFC8EBnv2jm5_dSl3KycJuXn-qQE3YsPuEBi2G-cuiy1rtTdLTMTH9r8YV6wLJ0ellVf8MkB9mwFTbNa8oKkeuolZb1gf4PWNScylK_AtYPwIwN5Jwxo4GBuwYh0dNDGy54FPd8YGqQzZxQeywZDZnzydBKUr6HtlPevp4P3F8FeiZCMuAkKtmFZPYRwi4imNnk3sYHigvM9XPZpLBm_flGS5M2ulMCTWLPR5LpNPMDfnodFUnKm0XfhuPapO_RBG8Tu4i-NfQVtzTHgiMaDuc9G8CdxKEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
اسطوره مسی شاد و خندان تو تمرینات آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/Futball180TV/100789" target="_blank">📅 21:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0efe47006.mp4?token=qR8pvmTPX4RjrWe5Xg-iS91ih64dIsl4RmdyJIBnwh66a6Sn7GV3EhkBauNpG6fEB48OAtVh3AB-p8ThBnX1dzAfv21qm-0_ZT0gBQ3HffU9kteHpIDozuWDKR1Eel_xwy2d4qbnhXkTOwPjUtNmeuZSP4CKe17nGoqTXsmHqp7CibBrqYmhIpXq-xCs9FeULDh9mctOHK4eYBLiZC39iGvpHyAV6z3F__ocYdEQhBVbt6romPjWP2lY0iSLj3kRsXzDpt_U66QdpSqp9fTjK7d6MyO2OOgkzlywaT3mpWQpOMwMM09dYGlq69uRbEIYmcaywPY_FMg-9N9pqyg0ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0efe47006.mp4?token=qR8pvmTPX4RjrWe5Xg-iS91ih64dIsl4RmdyJIBnwh66a6Sn7GV3EhkBauNpG6fEB48OAtVh3AB-p8ThBnX1dzAfv21qm-0_ZT0gBQ3HffU9kteHpIDozuWDKR1Eel_xwy2d4qbnhXkTOwPjUtNmeuZSP4CKe17nGoqTXsmHqp7CibBrqYmhIpXq-xCs9FeULDh9mctOHK4eYBLiZC39iGvpHyAV6z3F__ocYdEQhBVbt6romPjWP2lY0iSLj3kRsXzDpt_U66QdpSqp9fTjK7d6MyO2OOgkzlywaT3mpWQpOMwMM09dYGlq69uRbEIYmcaywPY_FMg-9N9pqyg0ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درحالیکه بچه سوسولای بقیه کشورا تمریناشونو برا آب و هوا کنسل میکنن، بروبچ آرژانتین تو این هوام بیخیال تمرین کنار لئو مسی نمیشن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/Futball180TV/100788" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lk2RNeqiAYn0ByA-L5xvmCqrxC1YzEoVUOSdPibVbDvBXe3-QE2atkTLNnJnXVNkM9Vx4c9TOuVWGNWKA5RzHFDAD-bs8mkxZrDPDNNx8wNFjB7E3ujGuBE6BqhNM7mke1E-OOA6t5ceQwMU-bnIkUC197SAS77i9k7NgKVckfQzPTOPKhLdBCj3EOt1KOIcxFLukfNJ2rbL0kt_dGbLyJepcqlgV5m0XzgH26VariS60SG370n6EZAbws4Nkeg9rSz3Q4pQhtYeUJnKlZAVARCP_0VZBA4PV_cJDQX56FcWZ6wzfZ4mpG48rC6GZ--wmJmpUYN9Bc0UU-p_cwbDLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت برای هر برنده!
🎁
🇫🇷
فرانسه
🆚
🇬🇧
انگلیس
🔥
دیدار رده‌بندی جام جهانی ۲۰۲۶
🏆
نتیجه را درست پیش‌بینی کن؛
۵۰۰ دلار جایزه
بین تمام برندگان تقسیم می‌شود و
هر برنده ۱ گیگ اینترنت یک‌ماهه
نیز دریافت می‌کند.
⏳
فقط تا قبل از شروع مسابقه فرصت ثبت پیش‌بینی داری!
👇
همین حالا وارد بات شو و پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p9_r4EF37DCE
جایزه نقدی مطابق قوانین سایت به‌صورت
FreeBet
پرداخت می‌شود.</div>
<div class="tg-footer">👁️ 1.23K · <a href="https://t.me/Futball180TV/100787" target="_blank">📅 21:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEtu7jvWwNOPajKsVy2tC40rAsWciKle3647taYHpACwWdqPJQE_SlnzUaBPR5IfBYGFGnxMFXh98kpUOfzlAzfk3pCA3Hg7KL3TajUrg1PBN28Em8Kw_ZIbBVXWDXtC4ysh1UhKgyDG0EcVrqkNYDq6IY-D1UaAXdFOiOYV_55eYp9pGd5074ex-a4FU-kJbL-t_q__CzPj54wn2ImwMlpc59qx5w4o7et3wUqNnq2A_sxuIK3Z2Oc4-frknV7SdVnCxY4L2rc0Vc-rHSc-jzA-LBET-xCGl0UTHzG9g_Zmv0rHrE4ErJhKMVVklnSupNRacE2aCF6L_e1bpWRJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو هم تایید کرد.
🇮🇹
✅
HERE WE GO
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/100786" target="_blank">📅 21:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhbE6quFOQN-iB249fIJEpDR-HAHr3faFUwYKmhgdzoNKpDs7vRqu1xa7_LtFjRzQl218IG5UQ9Lh3p92dTvposLxvfcjrv17hyUcaS-1Yi2KiVeM2oGcG3U-Gl1sEXUKXTImbgw2HOebSV-rxYTJmh2yJzEHSMls6HeYxylNc2wDwaLsz3r-_u6dnjAIA1IwwMO84E_tcpAz7sopDwHLOsDXRjqKu3GBycbVxW-L5DKGQWpQn5UDhi1hkL0bfT2yo_U6CwcEaC6Ua9zz3AYU9862INw3T2NYLVLS6XrEk9-pUSLFavACyD5XIOjVT-UfWGi51hQwd5IGDQb4TrkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤯
#فوووووری از دیوید اورنشتین: چلسی برای جذب مورگان راجرز ستاره استون‌ویلا با رقم ۱۱۶ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/100785" target="_blank">📅 21:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdTPYys2wJJCvbZ4UQbX72OgtzQ0Da8MdPZEVVWTobFiVR_KIf3x1NKZITAOB6FD5Cc5_vcsclmhdB1bNXicfzv3NepkvIetylobZnN3YMcaJMAykOMcdQRYijCeOpbYz2M1e3Ky5hBonGmogkiYF7uv9jKDf72txPSSDYfA9LCO2g6uulqTxUBfwjEOEfP04EsXs_HuWuudrPeSVdKLkBAtgVQT-xBo7B3ncApSauNdc4PJKnO-Y0mECPzc5pRrB7Z9YOLeWiB9u_IzuzgiOJ772GnsaaR5qWVI63t-UTP1gWW8OEUoUfiZGp8SC28sHdh84j6IS0aSjULH8g134g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
انتخاب بهترین بازیکن جام‌جهانی توسط ژاوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/100784" target="_blank">📅 21:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤯
#فوووووری از دیوید اورنشتین: چلسی برای جذب مورگان راجرز ستاره استون‌ویلا با رقم ۱۱۶ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/100783" target="_blank">📅 21:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-y-l5PQjtrgdrAtPuCr3qInM-B1S4mOG4XYhkhPb9MLjMtDLG20HcgHWHDju-8OF0Hy9XDYVKqp4J0KAjQVJyONr4vceZS5nD1sKLHQE_8MBQ31lIGWwjT27WjVD8VJXpEqznU2_tf4MkfJ5grLGggx3ExBal3iREj-vyHPHMM9AeqUc5-DsQEi4OxCMVxaR7W-o_D-4pGmMeOI9VJsbySGMImYfHrmfBEVOLULAi7pIF6WMzlIstO7API_xu50DK6xahXQtlQ_z-6-b5JmfdRu-7v8IbGvoflbyy2HLX3TV2FarpqRs764SKh1AAx3x_buVjyaN43kcz3XnqY5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤯
#فوووووری
از دیوید اورنشتین: چلسی برای جذب مورگان راجرز ستاره استون‌ویلا با رقم ۱۱۶ میلیون پوند به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/100782" target="_blank">📅 21:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100780">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTm261HGQAoawmWwNdB24aAQYLR9JIpMeTapJ6ZfOoGD_rsd6LK93crC6EZza7FK1coIPciAy9z8HN9IuhVNzM-VlwzdOW8FbEuWU-bTdSQoU9OH1X5NfWGYGhLtFrJrYBbHUwvopXH4fZFVMXZbmCe6Bfc0NZ52GkiYddHOUa8ma9z_gxiNmwjrWwpiDfVSMNdDJS8qO4vvl7jv6Yaofk8y8_HDfVvs3tC26-mQQxML23ZGL19Ny-MgGzKiHIeQR8_NFEinv58E9Cj4uBBnyb9zJgnp6bu-UNHoYyLsgyfZtrqcNF9nMSbbz4LEY-w0F2mw4t-hMItmuUnlDwL7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔥
نوشته پشت کیت دوم میلان: «بعد از استانبول، همیشه آتن وجود داره!"
🔻
این شعار به دو فینال لیگ قهرمانان بین میلان و لیورپول اشاره داره که اولی رو در سال ۲۰۰۵ میلان در استانبول با نتیجه سه بر صفر جلو بود، اما در نهایت شکست خورد و تبدیل به تاریک ترین شب تاریخ میلان شد.
🔻
درست دو سال بعد، میلان در فینالی که در آتن برگزار میشد دوباره حریف لیورپول شد و این بار با نتیجه دو بر یک پیروز شد و انتقام گرفت. نماد زیبایی برای بازگشت از ناامیدی و شکست
🖤
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100780" target="_blank">📅 21:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100779">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🔝
با اعلام سنتکام، دو سرباز آمریکایی در حمله ایران به اردن کشته شدند و یک سرباز نیز مفقود شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100779" target="_blank">📅 20:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlwRoIOLeYgVZUU4YEazo2JfdIMiWIv4dxvuMRuShxmwX1kNFlrMVgEuPaWRwzjDiZYtXxGYiLDC7jlY1fSS8GzgYyxkI3rGsLq3iU5f3IOC9aCnRWS0dr3v-H47J8RKepgLz--vPFhg6zQpUHOaxmxSoCKtpFlD3s458fPa49dqimNKtlOBgE-Xxh5fVgWW7tpEuh5VfITqlJ-QN5bV4bGIa4YPuQ0qWx0iwpxbrA5wa2jIKmlMiFEcqZckD_CcLBiIcILCssoxfj6srYswCRXjqqXsI7I6yx4ZDK7vFuJXNGbexQIX3GnM7w2ROqN68xRV4-_0AbJUddHzyfaM8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔝
با اعلام سنتکام، دو سرباز آمریکایی در حمله ایران به اردن کشته شدند و یک سرباز نیز مفقود شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100778" target="_blank">📅 20:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOyugXVUVwKbjZhRBO8b85H846VMfm2sY5yTtzT6COXzd0PKTLAnhmDazbJegUvz0Ew7tsKRNr0JQghJxb2tl3KnQGKLsynkgaMpS5stCqynj6FeTEOsUP-MjmRlBwkhQt3tHUQ14Ks-Q0PhiZN1klCAFOpsY3EUGKrdMpGWhHDRURz9W75W_ZAe4TJq1ntgCY9gffev3OllCxI9_yl6-Tg2466X3nRgojDLY_T3dQShbrmFyCUfrm8eSjhP1CBBTqJRc6ltqn3LIAdvO0IjlT_AgnPYxW8Rcf78aHMufxcGUHIfuDxYJWkRdeVzmmeqGAfYoQXrjVXWdhay_1ZkoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
|| در تاریخ جام جهانی، سه بازی در مرحله یک‌چهارم نهایی با نتیجه (3-1) به پایان رسیده‌:
• 1938 —
🇮🇹
ایتالیا با نتیجه [3-1] مقابل فرانسه پیروز شد.
🔺
در همان دوره، ایتالیا برای دومین بار متوالی قهرمان شد.
• 1962 —
🇧🇷
برزیل با نتیجه [3-1] مقابل انگلیس پیروز شد.
🔹
در همان دوره، برزیل برای دومین بار متوالی قهرمان جام‌جهانی شد.
• 2026 —
🇦🇷
آرژانتین با نتیجه [3-1] مقابل سوئیس پیروز شد.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100777" target="_blank">📅 20:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100775">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utPtGfRJrzsg_OCakKb3461O8PxSWftERkqXSHJbrN0F4rifW125gqZccgjaZs8fYbXa96mlK8wVkRdezHH0j_U_wn3W89_jLX6SRrScB_wafG2I7YAu1iHJ01OQdLyV5gABWYsRikcTysGqr5SyY9lv3IGY40AtmQUiTktMaRcGT1I-IrBgOpPN0Zm5GjSKvJUzMKi1kTVYjczMmoP-_nCZ-6H1W60wxWzRVaij5VaJXrwl7QW1jWq4HrD4RmVBS_N0SLrne51WO7eSCnOj1ZToiAdmL7mmri8JA8hY1dDCndZpNe7Xrphwj28trGmKHamjS63MGreHDSgGGP1Kbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🎙
دمبله: "صادقانه بگویم، دیدن تیم‌هایی مثل آرژانتین که به فینال می‌رسند، در حالی که باید در مرحله یک‌هشتم یا یک‌چهارم نهایی حذف می‌شدند، ناراحت‌کننده است. آن‌ها با تصمیمات داوران به فینال رسیدند، در حالی که تیم‌هایی مثل فرانسه که بسیار بهتر از آرژانتین هستند، حتی به فینال هم نرسیده‌اند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100775" target="_blank">📅 20:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100774">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktfA3gxT8PbeRp_q3Rc4vvfMe6AoLOWmoCzsb3OGlBVC1oTrFhqNOdFHG7H0dYf45ERlbccmBQjpFZbu8cWuuljt-RqAvXH8Jxb8_BV6O8eQX3Ybg_MbPi3Bw5dGgRoxfE-kRCsqOTtEQFqYmgkRYJDfLqiWOLZ6q3hDJ2TboDcmjfyKf8T-Pt5A7kCoC6lgyneRBj_iLJOZdjNQDkmwl-Gh85q8c1qkCoyndA9hIsnYTmhwLOl0tx3sryanCEOWzTP0YcvkkCHsAarNdwfzmoLOq7dKuuuNtYaNsROBYu7KkwpLi2NuMUz7etkpxhbnU5q0wpky6H8NDXmKV5LgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچستریونایتد مقابل رکسهام در اولین بازی پیش‌فصل شياطين‌سرخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100774" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100770">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9XppHfVa1UfZ4Gwlq8PMDUJat_9EMxtdM-uOp6OFQDbejz3vegf5vr02s8Pdbq13xWLirtuwiB8zwpQAxVjr25szhn0B9Z5z8Xk4PLYU_D2X8IP6IayCBvcUH0dmN3BiuvjEkfBcyHVNXfAxmroB47M9oM2VS9sptzl-okflta5UkinlV6u7lDhjl65YQdA--DvUBMhCHY2jbC75xaq8BzNWrpY3iTu6OgI719Xp6ENx2Ni-DLBd1CSdhWmofyZ87XD0ncrPd79McBufFNN1IEBbiEzxo9vXKozar6OozP-4OUlhvHmTGZnhWSSBXjPUzxT_jQAT7JdJOTfiZFEKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smDcpSiSYq5prCq1XSWf-IF6neG8yShYMajWZskQqz5TDt_D3xBQDpLoBsGnrcAcqUhOdKxbn-ZRPoQYOP6wZ4OmGD9pIm6bMiLtno9I40XhguGh2QxIvTGCKhJ4z8-F5P1ko_v7kghh1W7DjvWXPRhIlRLBbENAkbeSKQsiQK6_KV8rmS3-0n9xKTq8XExycKR4lL35qP7V92ipPIEQVZSlKSsONQLxl0WEBBOCDkOcmQpnbZ1mA6VX5t4JypzyHvb23sA9IJe6J0Hn7lNu0fm4F_1cdunzAVTyKIbNfSNnUmTjIaN1Q4i8-jWP9ttWLJFDR8xSrYOYrgUqyJUkXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vTmgsbmVUrl8PcwW69PcWhO51YQwmqPdCOlGL0XeOjOWoWAoJo1yE0eQYFrVFE352QTOSdLewwzlfjEx54yfBxbwftigNdgvfS1Qx4L9PJ9xLbRSK9Hgim2heqiXWz32ST88_OL2fVOy6z92tvK-r-0QXgBD6e2_dQ8MiOd7sK0bADlzcZ_2xum9xtMW9b-N4Em9K0RAvUOUhYYvn8bWi1bECBBy7LD1uW6RfxyW3S6K_ypSew2Udr5Gqg6JwvHQLjoV5ZiDucTqQ3k3_Jg2oXKguVImjoN1hV6j4-BYSEX3BXvGZJlbLSnRU8WEf5CFvJPgDeKx9gfy7TRlDHUcgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I13pJeeP6HYF8xhdh3Gdk71zZbRiOIXTatl1le1HBsUqlvHCZq0suEP44gnsIk2p7TSIHSltznSfGHqZJkHX1ev9sVeH55hYfgiIRga9pt3FE6KNl_2QO0HcdaEZnHK0zHz7ZCE1wwAQ-ctVw9D4dr9rpAHB-XYf8VWOjN535BOv8e6B3yXSPrCUJJI2PAFU4ucEK2NX05kxEOyHYGwU1lZEsUgD6Owb7sxSp83agcje3TRAiHwjvqLz9XHPmktRA-pBwORxchvzbP8nUlau4vr1wwJeX-wcueLz_R7_WZFeYb6yHjgH055Isbge0vlEdpw9f2JNFWlMD7c2jr8xWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
🇦🇷
تصاویری از اسطوره لیونل‌مسی در آخرین تمرین امروز تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100770" target="_blank">📅 20:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A86rOd1uZxGJOfJ0oHd7npssVWsfQnceXb55oy8YmeqA1RrDB9L9u6mRA27IhYvNJUb9XHks_u0eOBLAzYNC0NzMxtjPRxREsrBBB3-Qy14TNTAcgRSROXR6-JHcNLBAriB2oMdAeFLV6ilhbn4JE1aULnoLPtd0IuVG4KZlGacAWVoL6lEBKwwIz-drOsRJt36I5Z00xO5L6FsXyorbrfoGG5xJmMzzUIic5GTr4tjfMrqvwTx7VuvnMTcho8YInNJhmSkP40shMDWePTy7Ef94aCLwPc_S2jxF8dMqkqb_9JqqNiJP3lsL5oTdpwZgFp6iQQVRksD-NdYDIMNSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/io_CI3YnafVXFQKYDMg9OkZBjTFeayIx7twqPXat0BFWkaXKVwsXMAIJYdSU6lqgfj7d0wlCghjZoyGy9XTJWV9-6MusGlNN8uXNve56B24J5dC47k7fxU8HmtiDXjXBAXxchFMsCq40X2YClFtcJ5n23j5oAS75Kc-rdn5EKL0hdxsHF81Cq7rsEYvXIsG5XhzqL19hBmjFWiCHe6yfEOc3yo3Q5eGUMTgzLcDEFK8uYxW4bWGFt-qTqTjVKHz85L9-5_YxfQ9NQV8esUiLpfS0O8pEHO9M8ZfC7PcU5-3bZBjSNzoKhtIXgQDL7kSswS-yPg3NgmvIA-BvhgoCtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
برخلاف پروتکل‌های فیفا، آرژانتین تصمیم گرفت که در شرایط بد جوی نیویورک به تمرینش ادامه بده و با آمادگی به فینال بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/100768" target="_blank">📅 20:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871184ae5c.mp4?token=Ml5QMnG2xcfYrk6t_91GXS1bKlw2PrKA1HRGDFPj-Y69QF2Kd_LEUcJvdCneCoh60x7YvK5SaZAhfT9_9d-uXyz0PYdYGYhmp2VMS36epQJoj1xnl6Ua6uCld8RKtta1L5pVVj-suEXeDZtfrRmSzcqNFeSQ3hzEC4zGAVcq8SK4MVVGxvH38gFRULfTi3a0F6PcFkMFoqUuG33uT9HLYio_aQs-7sS0qRjNnwpURVmevPsYz8B0zBAALtZQOj8k-jSW3uSc9cxiJDdyf2dkxXg6IlEpgtgkztIKI7KBb4TZWCeC6IRYwwUIeWEWbuVP2TkLJScpcvOxm2yU9WiuPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871184ae5c.mp4?token=Ml5QMnG2xcfYrk6t_91GXS1bKlw2PrKA1HRGDFPj-Y69QF2Kd_LEUcJvdCneCoh60x7YvK5SaZAhfT9_9d-uXyz0PYdYGYhmp2VMS36epQJoj1xnl6Ua6uCld8RKtta1L5pVVj-suEXeDZtfrRmSzcqNFeSQ3hzEC4zGAVcq8SK4MVVGxvH38gFRULfTi3a0F6PcFkMFoqUuG33uT9HLYio_aQs-7sS0qRjNnwpURVmevPsYz8B0zBAALtZQOj8k-jSW3uSc9cxiJDdyf2dkxXg6IlEpgtgkztIKI7KBb4TZWCeC6IRYwwUIeWEWbuVP2TkLJScpcvOxm2yU9WiuPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
این دلیلیه که مسی تو این جام جهانی انقدر آماده اس. به گفته خودش یکسال قبل از جام جهانی برنامه منظمی داشته و صبح و عصر تمرین داشته و سخت کار میکرده، دور از چشم رسانه ها. واسه همینم وقتی هری کین با مسی برخورد کرد نقش بر زمین ش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100767" target="_blank">📅 19:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNaPHfHpjg4vQAqsqz6TkdXkQsZ1NmslYqJA62c-gTkGZJCT2VTPMLG59E7Bn8y3FzQSCxL-by5-qv1YeTWnQS8h4cWkUFfhIZMug8cUiYyVlZmwJ8mZO-7qxBcSOHgle9dLAi3az49cu04xG0Fl0gxak9xlD3xQF5M7FHOtNhlYxeWtvj8B8WLgvXKNlTz2gnk0BoGSseFRg4lDEBcIKUBVzVjYz-JUzcygJAr1VzS9JDDKgxWQ_NIwjsM6XeIOYy_UmnL85getNksvSwD8cick4U1i_NN9RkMXujpzU-5MXUC29dtIsNf6mg-bN9lijrxLA6iNgmPfTRl_WGhbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
#فوووووری
؛ آخرین تمرین تیم‌ملی اسپانیا پیش از بازی فرداشب مقابل آرژانتین بخاطر شرایط نامساعد جوی لغو شد!! ظاهرا تمرین آلبی‌سلسته هم در آستانه لغو قرار گرفته!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100766" target="_blank">📅 19:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiZsuc3yQtMotYQvwY4Aa6gIgO1rjVia2L-xW63ZAHNYAI_IoA6-a0zmO7n1bIr4d1amp8UHRyLIZXB82Ehm-S4pfkmUgj0PKi2kfqzAAn11uFEQhFQINSKRrH9p2Sf5GvkN7__5O7dZvgi6YtJ01PjCtBO7BEpmML6J8Cyfxh6LKJR-iNjfthSQh-OnDOIZZE8V9fBKXHi4ZqD0jPPJG7Wm9x1yL-X-yo6mOIj3W2_4kD_vjfzd5eyHiGD4-PCDnCf8qNdKcSWmpdc4cH5Lj9l1ftBHdSllyjJK-dJYzC_tgsffkeZQVBxiTivrdMgc7mLoZe3RdAwhnYn7hv1n8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
🏆
دوتا از رفقای ناب سعید عزت‌اللهی تو باشگاه ردینگ انگلیس قراره امشب و فرداشب تو رده‌بندی و فینال جام‌جهانی بازی میکنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100765" target="_blank">📅 19:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6fa8f4aa0.mp4?token=mtX-AcenUpzwLE65W81patCUJeQ0gkr_c-_gMyyVpv8sUu74QaQAaTR1y0KN5cAFDDJ7hDLbJOqtXrPDtei1V1ixAj01NKzIFaPHo6DL6Lv621KtDRrw5QOZ01tAzw7jRyqYi5i0vMhAueF_xJLkjhkBz6rQZlqUzL2aEP5K17ieoanZlqM1meFFSGrg_C2W9AxNrY43c0fuQskVODWb7Znkj4zBEVulRDcCPuw4nbJolv-_9tODlz06DV6e43KmKrk8itM_zzLP3QGLpd9EegRWUTVGsU39pmn33wiBgw-Ae9VgL64PmrU33vO8xxyHDomDdpx3fG2MOw2ZC0BkVHIZ3RP8NnW2yhQAfjwV_j4DInwMbVyulv2Tx53UkYbAzPodT7E6ZDoz1_ya_QWsPZhqbCP4S3kJnHFa2vXeQzO8cKMkmSqVrwwat9_arsjQLwn7QzgAKfqzz7NicZW9LeKZQCHJPYaXKisXCvZUBvmNx89XOnQKPtv_o91ttAy2nOzNynJmhQ1ydIsJbcFnmLYvvBBNlHs9KFltCUAQaaw5VGGzD89-69T6XOSmFfBHAJe01H5mCiBTJOt_UNLlCv4Jq00FLVb-jExzjq6L-Yy_a8lBiV9dDK_8T-4d66ONPnYXK-xozQDgsQozzMe7rVEEsyRiLBiEnQh2yPv12ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6fa8f4aa0.mp4?token=mtX-AcenUpzwLE65W81patCUJeQ0gkr_c-_gMyyVpv8sUu74QaQAaTR1y0KN5cAFDDJ7hDLbJOqtXrPDtei1V1ixAj01NKzIFaPHo6DL6Lv621KtDRrw5QOZ01tAzw7jRyqYi5i0vMhAueF_xJLkjhkBz6rQZlqUzL2aEP5K17ieoanZlqM1meFFSGrg_C2W9AxNrY43c0fuQskVODWb7Znkj4zBEVulRDcCPuw4nbJolv-_9tODlz06DV6e43KmKrk8itM_zzLP3QGLpd9EegRWUTVGsU39pmn33wiBgw-Ae9VgL64PmrU33vO8xxyHDomDdpx3fG2MOw2ZC0BkVHIZ3RP8NnW2yhQAfjwV_j4DInwMbVyulv2Tx53UkYbAzPodT7E6ZDoz1_ya_QWsPZhqbCP4S3kJnHFa2vXeQzO8cKMkmSqVrwwat9_arsjQLwn7QzgAKfqzz7NicZW9LeKZQCHJPYaXKisXCvZUBvmNx89XOnQKPtv_o91ttAy2nOzNynJmhQ1ydIsJbcFnmLYvvBBNlHs9KFltCUAQaaw5VGGzD89-69T6XOSmFfBHAJe01H5mCiBTJOt_UNLlCv4Jq00FLVb-jExzjq6L-Yy_a8lBiV9dDK_8T-4d66ONPnYXK-xozQDgsQozzMe7rVEEsyRiLBiEnQh2yPv12ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
تیزر جذاب الهلال عربستان برای معرفی کیت‌اول خود در فصل‌آینده مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100764" target="_blank">📅 19:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OT2qJq9IrTDCvbgrWHzLwvkaS-TkQTHQ-XuOPh5uTPCeCZv_6XdPzraQoGa1AKxJRXwu6m7YISBJIGq5DxbrnqDzVWHMnctA6qtOFVlGes3PyUP-17o024bSeBHXFtKv9nQRdja8iigvq4JYzco3KZgJjDvwFUrM-Ur6iGoWnc0cbLXuJfkORf0KMhQZyW4V0dKYCbEg3HOYDVixoGmFafLGibnQk4_jzfROurPGLXQkw4dYiFmhdr3VgdmBSAbO8MMwZ7doOdCoFUTljLVCu2LH1wBuik6CNeyhDJPoac1nEiN0-jqhloPSQx3oqmBSqIms5way-1BVlhrj0asBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔵
کیت‌جدید فصل‌آینده الهلال عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100763" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3cj8w8qDpvY8HfINKFkrWkruqSJA5UKSDdmfeQpoKXfRsOQTDB5JzyT81A9HAhftQpOYcSW253KDqilM_JqvN2090Y9zu3NPS7aWqmvVQBmiljDQTpPyB2nc0W1OIIfmNHpJiGVVhMkyGwJSk70SaY7PDIXRfqv8pjenbQtCSraWcDvCVMutJ0TPZLitDiGa_eBrQLb8AQXN5qQlfq1cV123R8de9nom6ddqu-UManGJ95u6auEz2ZrRddrrxdJAdYtwFjVAmR4QaB5XroSpMF0l9-R_FptL__N0XaLezTsllGhumTZm-nMegllQk_r7TdsVYwKzmG7IOKrNBKjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
جوایز فردی مسابقات جام‌جهانی که فرداشب به بازیکنان در ۴ بخش اهدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100762" target="_blank">📅 19:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778c75cfe0.mp4?token=EP1XhvMyqd97Y60ouzcZzpQwGeZzmlz1pTb8nxAviSmpVRiLucMJMm9gVeACsgi84z_z13nZCItvW-8-ZMgzv9vq3MM5yHIbr5kgT4RCSpV08LOXwuxZmMsJLDdg3XWk8ZO1Au0iqs7wCwXDuADXU1vtNvu080iHoHmMEXjcowX5_0Qefhe5s5AG0zhxwq6BYsa3yHhP0AKxmXykPMwXQb_z3UvOdou5Kx5nCxoQa-gUheKr6AeCgszA1sxKbEJ29tdQORv3MdUMBpYwEwVPFHERUkbqo5Ko2wiQlwD31UIPi7H0hImO5H27zgoDiG7fkk0IgHyjkUyUwD5FO82FNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778c75cfe0.mp4?token=EP1XhvMyqd97Y60ouzcZzpQwGeZzmlz1pTb8nxAviSmpVRiLucMJMm9gVeACsgi84z_z13nZCItvW-8-ZMgzv9vq3MM5yHIbr5kgT4RCSpV08LOXwuxZmMsJLDdg3XWk8ZO1Au0iqs7wCwXDuADXU1vtNvu080iHoHmMEXjcowX5_0Qefhe5s5AG0zhxwq6BYsa3yHhP0AKxmXykPMwXQb_z3UvOdou5Kx5nCxoQa-gUheKr6AeCgszA1sxKbEJ29tdQORv3MdUMBpYwEwVPFHERUkbqo5Ko2wiQlwD31UIPi7H0hImO5H27zgoDiG7fkk0IgHyjkUyUwD5FO82FNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟢
تیزر جذاب باشگاه الاهلی برای رونمایی از ستاره جدیدش فرانسیسکو ترینکائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/100761" target="_blank">📅 18:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCA08WF3CQaAAePUDc56cOIBwHQljvi-1lmKzmp5h3_bNHmaoefstE1qoJpRw0pEp-8cPQQDBONKWvvER7x6woOLSIyPsUSI3SIpkc75cJFnMr8KfQsamchIqbSWzpDekN2cEHs-rmru5Ct6OaWbLafyxbZZKUpIbS2-85RD8tJ3jRDaCdZk4KD3JEZx2_LUtzwJclW1z-qgvLe-LGJ4QhWS2oXpaSBSn9f5UFHYX_U7u5699kTwFcNA1HLarLSr1qSeebPk9yXI9Uit8xoFKFwE_ByzVfWYgbChYea4GVmIh1y4f970xetONOJ8NSGcYAsWygFRxcd2HrO-RiggYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
#فوووووری؛ باشگاه الاهلی عربستان با ترینکائو بازیکن سابق بارسلونا به توافق نهایی رسید و رقم ۵۰ میلیون یورو به اسپورتینگ لیسبون پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/100760" target="_blank">📅 18:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJGfkUu35HqfCvuYSb5h38UFU4QwXTxT4L3WkmIjF1qL2A60ohaL8Pzbqycw5qhDpA68DmWVbDEguPR6TNH4gfUE6Wn9vkcNoAc_WIQAye8KfHy6UHXuXia69Tb0_yC6PwY7UBrS8rnL8j532__Ll79ZRSLf-DDFiGqT58JG4U7euKLPRcZOk6qhi9WYO5oPj0jHTWOD5GMs57_VXntNW2PdgcvuqOnktKyXMIWpwwlo3Owl6jNm1XBf5FNO-KIEWp3lUf2bCpKSV6Pn0-rePKMHFe308vnz37_flZZ7_H_XRinuAA5cqu0Uu93YMlZZ4n9b39ooxydp64jgZBM1zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
نوادگان یوهان‌کرایوف در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100759" target="_blank">📅 18:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLsV7r-TN1XINgBOL5Q6OiMxxq1Ob9k4v9zP4cTIWnMVDJ7vHBVf64pcWPfDHYeycjY7D6zsM-53jggCoAFoTofbqGHw4rjPIC1xVTFt7OYZrzzOfpjdY2q61Jitp3Vm43svejUb6AXVZSxxxmQ4r6jHw3oHDmkPF8Ur--FqjK7SErMa5X6NnVyMf3iNuUCjdna0R7DVw_uxIUND5yaX8tMzRdXJmZdio3RyozhQxQYSOBlau1Hz7hsgwPf5GJEQHOB8Bjhv6g5xKbIN9NRfCw0O94dBRALYR_45TkNavlaaQ682XzFR9KtQEfUwKQvHN5H-TDC8oxv2xeJwy33x_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ترکیب دورتموند در اولین بازی پیش‌فصل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100758" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jV4YByk4rlQZSO7_Una20MJcr6AjdTGOItOy95ZU2KFdzdoNdw6TsS6w8Bz1o3x3-ntyPrVcX76KXLh6n0nMlHzMAZgSu8j42wjfm-SXRPIN2da54v7blNtAGH_y_R8xBM7oNIeNzlArFLD6C8uPVXZkJG2c5fGj_G_Hw0u3MQK2wU8S4_Ic5yU-ixegBzND4KAB1XJJI-gPoAqGih8MKkvjfkKXJAiboaf3kwzzpYXyBxG7m2bVLbiWxO_pAmTR7LrriZE-FhCC4Tm9agpJCNIotWnQ593QfFxu21O_JXexujCegLdee56NAQSqdrncBrZv2untgCDG6JhPyW5K1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب احتمالی رئال مادرید در فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/100757" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100756" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=Q7djhk_Gw2KKkAWeR27uWaivVRk8tvUdoFO3WUgbyKWSOtl_ul2RPn7eNcwBEbjxSTbO91B1d7smN1sKTSS5YchiDcTziR5O8Vp0nSlurmB5WJsu9i9JksoDh_CDGpkN8zh4lugrl4fnlzPdUfPtp3f17f3vnJ5d4JLyBlr1uBG8FlOtyYHwpKolD5wLyAf-QG3Q1nE2Eiz2Yf6JFG5P06mLpj76pEuoIe_6NYZlAwGn1O_70knP6NZXBlEYdErglsCcGV7URQBKacttNv8HhMuMg6uXu9sIDcEbHeUE-O5jCbPAuLE1ZMnEJMpFmSsOgOGVFl14sxvGC2Lp9pdrpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=Q7djhk_Gw2KKkAWeR27uWaivVRk8tvUdoFO3WUgbyKWSOtl_ul2RPn7eNcwBEbjxSTbO91B1d7smN1sKTSS5YchiDcTziR5O8Vp0nSlurmB5WJsu9i9JksoDh_CDGpkN8zh4lugrl4fnlzPdUfPtp3f17f3vnJ5d4JLyBlr1uBG8FlOtyYHwpKolD5wLyAf-QG3Q1nE2Eiz2Yf6JFG5P06mLpj76pEuoIe_6NYZlAwGn1O_70knP6NZXBlEYdErglsCcGV7URQBKacttNv8HhMuMg6uXu9sIDcEbHeUE-O5jCbPAuLE1ZMnEJMpFmSsOgOGVFl14sxvGC2Lp9pdrpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100755" target="_blank">📅 18:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fanhDA7-nG8YXlalKEYZgrjEKTrGeVUm6jeMvCUHXYAhvBJDpY7KipS4w7-q5vCwnN2IGqqIev1zj5G1Hx75EftIEs3hkOeVo3ru8rHPNvzhfHCI3gRl_mBzReaIEmu63fjtn2_oPRxFDb2XS40NrlrTXhWKPc6yoLxv7yy6YKMFP1-U1viwPDgB6sELw32S6f5BEFjSkzGqaAjv_z-k2Ox4a6hfmB7HHNTWPlceLL72s6FIF8XXaldbtoxvksNGNedcLxeeUGOoullgwmaSbY91293MxVSHvp_32wHhQg79o_O3q_3ICf0luOISmX6FH33eO5_s9d6rnbD-JE1Pig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فکت
؛ از سال 1986، قهرمان دوره قبلی جام‌جهانی اگر به فینال صعود کرده باشد، همیشه در بازی نهایی شکست می‌خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100754" target="_blank">📅 18:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqDXUchLyPmM0pF49QO6BG1Y0kc8BuH1T0zmEg7PBCY3rruQrj6qEUb1TlaUQVHM1mLXveGyjhiz0GKUBbzk5pJrvLO2NB2O9P8VLVBV5OL6gEeX-010wKh3BHXiPbzdQ8bZNJ7W1TnmeFNt3IESFl-eE9uIzQjuJHe3MlHFyuofZ7ObISk7zgjGv5dlLk9LvJlKi4RRjEDxRhvbRjEysOxvLznkk-uld8xVBZokM2x922rDiHXPLGWH7Ddqu2X3ouPhQZ4CnJnN0qwK7KH5PzJB12egGSdeSbpNTaMM9TR4H6eG8zkMmva0pVUWNBAeaFS0W7Kawb7gTKqeUJSs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش جوایز در «جام همراه من»
واریز ۲۶ میلیارد تومان تا پایان یک‌چهارم نهایی
🔹
پویش پیش‌بینی جام «همراه من» فراتر از یک سرگرمی، یک جریان پرجایزه است. براساس جدیدترین آمار، تا پایان مرحله یک‌چهارم نهایی، بیش از ۲۶ میلیارد تومان جایزه نقدی به حساب کاربران و برندگان خوش‌شانس واریز شده است.
🔹
در این میان جزییات پرداختی‌ها جالب است؛ میانگین جایزه برای هر پیش‌بینی دقیق حدود ۳۸ هزار تومان بوده است.
🔹
البته موارد خاص هم در این لیگ پیش‌بینی کم نبوده است؛ بالاترین جایزه برای یک پیش‌بینی دقیق به رقم ۸۵۷ هزار تومان رسیده که عدد قابل توجهی به حساب می‌آید.
🔹
این پایان ماجرا نیست و طبق اعلام برگزارکنندگان، ۴ میلیارد تومان جایزه دیگر هم تا فینال در انتظار پیش‌بینی‌های درست
جام همراه من
خواهد بود.
🔹
با داغ‌تر شدن تنور بازی‌های آخر، رقابت برای کسب سهم از این جوایز میلیاردی، وارد مرحله جدیدی خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100753" target="_blank">📅 18:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D8FjAXviWtUBbYf7fMtKRVpjLudQhk7MbVYyRc74vFgDvCN48lMIa0D140nsZWfOJ1_t9wY6rF6B00g0tufnh8-W4hXrxtGhRW7Ob8SvC9dW4UKpUj7uSMbZCav1NDrfGpt74yqVjYiESVzB4e9rwEwH59dNEJHOTAnc5va8JYkioXdVm5-PAHobhp0pKgFnC-y1sBJlcLamYa3G4uOfnP3sIVrvE2DOBGBb9DkmCaT4SxLAVmIwal5IRSqPKgg42FC9IUrhWsQi6KZGDTxrVc7NkcluHmW5lKZKkbvTZ6FqfgYNUqbkOB6YQokQfhR1W_Zl96qSYt-W3Ft_IDurmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🔥
🇦🇷
استوک‌های مخصوص اسطوره برای فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100752" target="_blank">📅 17:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVu7FV3I0ZDUbKf9zqHjHhgaLzMkml-FJrvEl7iDv4hzgCZumUVY-bvCpa8pe5RT__b6Gh916kkPTM7Cp0yUg0hEJZEKay4BOWwbL2SUf0r8JN3PUjRNQeDFkfFvTAWG1AqWFVGxWO0ySLQL4SH78EotK3Fi_EplfTmF-MQlD2f_Xbvr8JX7E21a20maeq8G43Gdq8QMBACroZGjMZGlnqghivcrVYKcAGtIRew_fk8N9qiz9wvRjZ1tUgqD761EsHlWkzEpgXx-ENjNQqrLLF6FLyNKFogyH1iqhSXPksU04fq-V86WXjLMXmAaV1u_IlpqRhdF6mC7rULlNGQykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مسی از نظر آماری بر تمام بازیکنان اسپانیا برتری دارد، به جز یک درصد بسیار کوچک در دریبل زدن، که در این زمینه لامین یامال از او جلوتر است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100751" target="_blank">📅 17:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj_jvljXqt5EOnDDDhh9RNuKz7jToseO2DYZGLk3BPrxeex235hLR-6SH27ttdAT3FKO_UW6cOrinHn1b8ZDGn-ZzMwusBNtJaQPAGIRQID3QWe6mF4skw4v7VcaWHTHAMhbFqcCsWaKXTYDAGTdDlybzxrjTgpx6fydgdkiF8GIzpxjcySSLwLTG-Zj7lepk1aK1hF-Y165Ae4zWI-j1Ns_IL8ocT36uIiutZNezhawgyWj_BaUeNxyMq2DL0VTPzq9kYq7c3FldF_Kdt5wyAXUlnsO5RH79QgD691X7WiW7GD5ngkYzkilziLOjxlW_BvwXZpAQeLb58BaoED_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارسلو:
من اسپانیا حمایت می‌کنم تا قهرمان جام جهانی شود، چون آنجا زندگی می‌کنم و برزیل دیگر در جام جهانی نیست. فرزندان من در اسپانیا به دنیا آمدند و من 20 سال است که آنجا زندگی می‌کنم. علاوه بر این، پسرم در تیم ملی اسپانیا بازی می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/100750" target="_blank">📅 17:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WX0-HW6FhUM2RcDjazy6eIiEXF7NjFleSPOez5hko8hxbyjwS-PgDZ_3hC7ekXHfOViAUU2t5mexKhmaEnC9iLuc-y0zd6pZUhgNGOPtn0uUzW8-XXHyyLxDDOuNG6dWu12a_BYVbsJfzLjCg8g0ooS8ZUjy933BdA7YwNk0e9KRsyQgl6lWzJnd7nmrEX4RGnd9v_v97Fx-4LLmHMiw3A06daSQiNM1vJGXTJC9Q70lVOMBBTkavaj6C8qd_SSwVji6lSeZXAXYjw58rDrZovPvhz_QyFztVv0z5y-Q9U25NUyCfv82uIZG0sAEQIIdwTwA9GLzTNT5r3rdgLx58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منچستریونایتد مقابل رکسهام در اولین بازی پیش‌فصل شياطين‌سرخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100749" target="_blank">📅 17:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaDkDE9dUp1u5_WqtAUcvATw1nHteWgrZZFHtfcFUWT7-fLboaR5ikeOmy48ABObPF7ntIQj02R5HbbyXw9GFfYEibvswGQF8Z2aABH3PbbYfmEnxmd7xMkAk17VefqMi6wLqk3eQvTcTRHVBHzhCMV2rTbG8I5--YPuZJJFeIFcgeIuNS5IvYvmODcrW9AJyglmzpf9jG1pl8UX493kEyC8uWfW3MzxhFWBHgLEjXfLfRQbXVWnpMv_Wq13-vWQW5ywvf1SyCNzJR-v7HWJUFmWS-Cy4LcxTkpLIDtnPi7Q1_oSK-3qlIyMvAMPV4ryfKYeRt4ZxooAEUu223DI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_فوتبال‌180 #فوری
🔴
🔵
برخلاف اخبار منتشر شده در دقایق اخیر، باشگاه پرسپولیس تا این لحظه هیچ مذاکره‌‌ای با کوشکی و اسلامی دو بازیکن استقلال انجام نداده و این اخبار برای بازارگرمی و مختل شدن روند تمدید قرارداد این نفرات است. گفتنی‌ست که آبی‌پوشان…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100748" target="_blank">📅 17:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2480fbbbb.mp4?token=MRwg1v1vQO5YkeB5izGiO0I69xP6YUH2XLIW2bbVCSSyAsUKSWq1nALxUIrJl8hqLY0611wGpax5oj7hcFXFzFmYPEFlBE8X6lyt9dGBVxHVuFXeblFqSxY29FoQpuXZwWQqmLTbUcO5596eCpDCWbUDWxPQ8glP78j3BZOdEt9fCI807mTMOutRpH0LUhdEcEM-LF8wmYxDCSVUrgQz94TSN6qMvSvDkmpVcXlPB8Jq8jN8gW0irStg8q_nMUAf9S2knzqWcGKV165JZBXYxvskcmlSEHznpyJjDb_J3_ONW-Qio1VgGFrFRex0dY3XpnUewBv-tEaFmG3QlgICJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
انزو فرناندز که حسابی هواداران آرژانتین رو مجذوب خودش کرده
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100747" target="_blank">📅 17:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100746">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=CI8Lcq12DyGkwkazArXbqLSwrsTj9Z7DJwJ5XPXg_rgbeMEdfnQ40b9I5s4OGrFpaO8ZHKcQAxuVpw2PJ8mqGYQ-VU6B6N5rcvSWHB63kaUPQ1DoJC3t65-iCAngsZ3CDKpI5bJCzi0Aifb2OD3gIp9CAnrS2EfuQXa1auGHOU7w24JV6d9fo4R-IkHmdRknQ963vZqNqakGYEVRJAoBaFd2N8HxsyIHa24sCQ1a-DQWYjqTqHoxfgACwi43anmBFPZrGO-XcL78sehNczwgQw64uPFDX6Kauue38AmoSKG-nrEWL0d_Ps3VcTBXCcJl3VxvMZapDjvFrvm_WzEYuZTnQGsfF3diCRRT5X931mxWzbcUABZDdl8n6Z_SRoiQkMaOywkfOwkvTSd-iO0oEE1RXroqIBrN3gzvFbYzNvsaWTnrDf3O0XLrYSut6u6ndpXhdzsW24b_BjNRpaRNg0BHffQAz-NKas5Wd5teYrr8uZT5jG679xuvgSNxKkvkZMcC4dxW-RMEeO3fVmt3i27x_G2wr_3BW-cLdIq83kF-6zCX-dx1PaafnNaewljKrIJlv2d6Boy_CaHyZOiVwssMnem3XaI0hIQtbyeDlOhtSK1OjJQaPssVp7HWwbyW4E4B7fQvRdKy4km__GiZ5q27AhDSv6hDZB9H8bP8Kik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc579a6c5c.mp4?token=CI8Lcq12DyGkwkazArXbqLSwrsTj9Z7DJwJ5XPXg_rgbeMEdfnQ40b9I5s4OGrFpaO8ZHKcQAxuVpw2PJ8mqGYQ-VU6B6N5rcvSWHB63kaUPQ1DoJC3t65-iCAngsZ3CDKpI5bJCzi0Aifb2OD3gIp9CAnrS2EfuQXa1auGHOU7w24JV6d9fo4R-IkHmdRknQ963vZqNqakGYEVRJAoBaFd2N8HxsyIHa24sCQ1a-DQWYjqTqHoxfgACwi43anmBFPZrGO-XcL78sehNczwgQw64uPFDX6Kauue38AmoSKG-nrEWL0d_Ps3VcTBXCcJl3VxvMZapDjvFrvm_WzEYuZTnQGsfF3diCRRT5X931mxWzbcUABZDdl8n6Z_SRoiQkMaOywkfOwkvTSd-iO0oEE1RXroqIBrN3gzvFbYzNvsaWTnrDf3O0XLrYSut6u6ndpXhdzsW24b_BjNRpaRNg0BHffQAz-NKas5Wd5teYrr8uZT5jG679xuvgSNxKkvkZMcC4dxW-RMEeO3fVmt3i27x_G2wr_3BW-cLdIq83kF-6zCX-dx1PaafnNaewljKrIJlv2d6Boy_CaHyZOiVwssMnem3XaI0hIQtbyeDlOhtSK1OjJQaPssVp7HWwbyW4E4B7fQvRdKy4km__GiZ5q27AhDSv6hDZB9H8bP8Kik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
علیرضا فغانی: اگر ایران مانده بودم، صدبار خداحافظی می‌کردم
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100746" target="_blank">📅 16:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e993550cde.mp4?token=I6V7MdgF5oSAkQDx8AjQSJp5iltqtfF7ZPbQqrwX14TgDgi5LMsdyHUWj-bs94qkIsbbercO8Glmv7QwfUfZj-SiyEe-n9nPO_akqMFufWVq4190BEQKNVU7ne8RS7lVib0jU6jbCtnH5pSJm-K24ktO5l5vfRcGRK5CGATDVqEBbffenda0YXVOC1EiNcQ0YlXwMI2qhJaZskQsYLUfhOnHmbn_UEHexCeovR4B1CEspnYEIANRs-5NqWRa4O87UEdJI2Uht-A547j4iXcONs8-rAgYe6zPxyuXIy8-cAt4gimgH9li8zCV5vmvaZTLz0P_PJAjtHrcLHKca_x7BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e993550cde.mp4?token=I6V7MdgF5oSAkQDx8AjQSJp5iltqtfF7ZPbQqrwX14TgDgi5LMsdyHUWj-bs94qkIsbbercO8Glmv7QwfUfZj-SiyEe-n9nPO_akqMFufWVq4190BEQKNVU7ne8RS7lVib0jU6jbCtnH5pSJm-K24ktO5l5vfRcGRK5CGATDVqEBbffenda0YXVOC1EiNcQ0YlXwMI2qhJaZskQsYLUfhOnHmbn_UEHexCeovR4B1CEspnYEIANRs-5NqWRa4O87UEdJI2Uht-A547j4iXcONs8-rAgYe6zPxyuXIy8-cAt4gimgH9li8zCV5vmvaZTLz0P_PJAjtHrcLHKca_x7BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
خاطره‌جالب سرمربی تیم‌ملی اسپانیا از تقابل با مسی زمانی که سرمربی سویا بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100745" target="_blank">📅 16:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d4aefcaa3.mp4?token=e5mQ_0SXv6pLRMxVRy1BbCCYJRr0WgpajNSVzQs0xhz71_Lpomkm3A-tYdwNQ7a6LIZqmxlNoA1Qsz7CgjRm4qYWXdqpMAtEPce-_KBVYRQlvmSJ7ZZva7uaYCpmSbqhcJjHqD27d5jRreLNXKdf0ZD5Poy-oO7b5ZhNeY3DCXZkk7RhymOkpkUudHP2EE-5npu6G-LVHdK0sqGnTgPCz8N7dEs8-Qesi7DoR4ZGgWEUh3w_ZLSTK2mnX3lc6ZJiPV3erkfuFQW6kat0skIrxyJcVcnZtiGS3DPz3-yhogAq571Rf-0rAND0pDW8fuwOEtOKU5Yn74ipugg0Dya3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
هواداران اسپانیا در آستانه بازی فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100744" target="_blank">📅 16:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=a9yQxRbGVM8TbRh39_r8e7gX03xo5ocO-n6ViCQWL8kLR9-aB7Kew_QYFgZlVAsetN3yNg_Sd_SRPToUxVNlRlKhfPeg_UIIGx7zbbczPfa1IABNS2KKuP0FVxNB6rDkDmPwy6X2Aubt1bx3s_Th7vCaaWi1Hp01O3R9o4l1bkBRGTlrkI7icI42oznwpVw00zfhFc_LDvRVuAgtbsp5d2R084UMrQihpRN3_fz66PH3OXe4W8JuaxdiFGEaS45xddbvxpeedDc95K3WdyHcO0l2kAG6NflIxZrFZKkhFYqtE0Po0IjCnFrC5GibOYDUaAJxV7WEug6dGlh-PRjbFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34b9470b1.mp4?token=a9yQxRbGVM8TbRh39_r8e7gX03xo5ocO-n6ViCQWL8kLR9-aB7Kew_QYFgZlVAsetN3yNg_Sd_SRPToUxVNlRlKhfPeg_UIIGx7zbbczPfa1IABNS2KKuP0FVxNB6rDkDmPwy6X2Aubt1bx3s_Th7vCaaWi1Hp01O3R9o4l1bkBRGTlrkI7icI42oznwpVw00zfhFc_LDvRVuAgtbsp5d2R084UMrQihpRN3_fz66PH3OXe4W8JuaxdiFGEaS45xddbvxpeedDc95K3WdyHcO0l2kAG6NflIxZrFZKkhFYqtE0Po0IjCnFrC5GibOYDUaAJxV7WEug6dGlh-PRjbFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
صحبت‌های پیمان‌یوسفی درباره چرایی عدم‌ گزارش بازی‌های جام‌جهانی از صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100743" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94776f3b42.mp4?token=bc-VVU_8o19laN29ll8NbfLXDWhvM-AxgAY3teuN2vQ8rG6LkCTeRnTP7FbXH76KDIFaZ_NBDww9_3RBYg7AJvLJDxQQ-zHK-AzSGb-UwcZVZyyVlpZ7ULmM66y_KjeYWNUsYTw2z_D_ihyDuW96lvXxEcHJ2txgZaCZdlFe8hVs4lxEPtVgBD7tE57yfClswrOLYU4nxs905E8N0uyYtIgyCVQCHJe3JLqTmyTAN9Ax6KgziK203vlvHzGhydsR-iAcvQBx5JKSBNqhPo-OqA6ND2toJDdeysJZsoavN_-YbeHj0RPNTQnwWgkxiHstbmOT4PNozSVNU991i9dLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
انتظارم از بازی امشب فرانسه و انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/100742" target="_blank">📅 15:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJuE4lErvwBka7qS79oWXgyEPavJSW9MhDCxm7MLNm_o-JisLwuK4ehdGj8gF3SL4kevCQfJsyhGVrV5D5-Y6HQVi5eqaSCiVFcJGv6tVbWSpK7FHeWtjZiJBi52DgaIfqHXtygplqBjMvnjhlvLwyo5XN2OT6lpVm7OgMFmtRF-aH2tglPKT8a0iXfM3kYzLK-VU33kFrJoD4q7196FPWzFk3Wf1GOvB7LIdyyjGE__gskS34FQdnTyhrxGW9avegMCyvfl1uAMp5jMLSTQqRqGbGKR-ZBy_kB6BoJrtAt5zySE8C_WCwkeDvjA7Ld_w-9GqPJPWwPJbPuuIMmsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری روزبه سینکی که بیرانوند و نابود کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100741" target="_blank">📅 15:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtKWfEvde-ay8D8S0flZ0jHHC6Gdor3OFWw78UKtWSL1HmsnMRH4FEZL3Z736ueE4-jWOaQrSqrgq-kKRCt63GRcyN68DazzL2BJYr_JB9vYSUZkyJME4oR5wPM4lMGFigXanBBzn5HRg1O54UjJonOQCUETHEok3yFE1f-T-ZlOxiCr-WKjTbaHbooTf4MX3oToomkVxUiiZOrXOErrBlKabC-EJ6AAzd7IHIe8sRLy6eDBzVapsfR_27oHEkgSjKpYg7DhcuKm9IQCzzk927925adyQV4am9E3_u1yFQCELHkk2yhqpyrXrvzNdKSiU-Jj-tF1slTxjGWSY1ePFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 روز تا مراسم توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100740" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🧾
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با کد پریمیوم ووچر
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
25% پیشبینی رایگان برای واریزی‌های یوتوپیا
🎁
با واریز کریپتو، سقف برداشت خود را به سطح جدیدی ببرید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100739" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=bCwte3RW8Uo-9jVld1DYu-BOege90u7GhrA-Ts47U9LZSfGvx-1_mLpSqD2ztKvfTvQXUs0YIF571peo-eBUwvaB1UwFQMsC5zx1DjeAKfA5TXprh26oTLloUtK0gbsTKNcvH5eSk3dlZjYOMXJfY8ArAGnguT8T_kuUGIUUv2SPFKC1ocWmGql6LkFagBtQV4I_dnKAkhD0ElXPiMwqy4kQrMJvujgV0wnZ7md52CW224XAw9QG5__qdqFsTqdqf7Gmr6kNl8FUs1w4khKlw09yoF9sZZqIpqvsJ1yfIuwyRRfdEk5P1wySDuu5b5QUgZmc6vzNn4bwQKgJV0ENQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4918cf32ee.mp4?token=bCwte3RW8Uo-9jVld1DYu-BOege90u7GhrA-Ts47U9LZSfGvx-1_mLpSqD2ztKvfTvQXUs0YIF571peo-eBUwvaB1UwFQMsC5zx1DjeAKfA5TXprh26oTLloUtK0gbsTKNcvH5eSk3dlZjYOMXJfY8ArAGnguT8T_kuUGIUUv2SPFKC1ocWmGql6LkFagBtQV4I_dnKAkhD0ElXPiMwqy4kQrMJvujgV0wnZ7md52CW224XAw9QG5__qdqFsTqdqf7Gmr6kNl8FUs1w4khKlw09yoF9sZZqIpqvsJ1yfIuwyRRfdEk5P1wySDuu5b5QUgZmc6vzNn4bwQKgJV0ENQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام‌ جهانی 2026
⚽️
فرانسه
🇫🇷
-
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
⏰
شروع بازی ساعت 00:30
✔️
امکان ثبت پیشبینی با مبلغ نامحدود
🫰
محاسبه نرخ دلار با قیمت 2.000.000 ریال
⭐️
فرصت استثناییی چالش‌های پیشبینی فوتبالی سایت یک توتو، با جایزه 500 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/100738" target="_blank">📅 15:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9511ead233.mp4?token=RXpHaeMMPCifXHLGPKhT1Cciwgc11H3okY0ynGCgBmwNq-bejDmXWRimFIcIitGh2J-PQj8ZztAs27KzsVNdNK5HG3-AZW-isUQYvPq_DTGHcQGOTcCSiJay24bjnK6594XD5WD988F7sORbFwmFPvjzkhuZNkSMaqdlzYAgE1TayEJ5-P2wvdd3O2E9S-D8EdI9dMoJ_3uqH5UoCRu3OXVDTZED8FjJhtZ2Y55_7QbWPJMDxsDrVITH9-M-MX5_1G7Xy097FMW8eeLaI2WF_d2T9-Mb1OyMIk3LSlfeF4zCL3GfCbZXMoQJ4U3z7HG5BhetT7eBGIsPgIRA7tvaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9511ead233.mp4?token=RXpHaeMMPCifXHLGPKhT1Cciwgc11H3okY0ynGCgBmwNq-bejDmXWRimFIcIitGh2J-PQj8ZztAs27KzsVNdNK5HG3-AZW-isUQYvPq_DTGHcQGOTcCSiJay24bjnK6594XD5WD988F7sORbFwmFPvjzkhuZNkSMaqdlzYAgE1TayEJ5-P2wvdd3O2E9S-D8EdI9dMoJ_3uqH5UoCRu3OXVDTZED8FjJhtZ2Y55_7QbWPJMDxsDrVITH9-M-MX5_1G7Xy097FMW8eeLaI2WF_d2T9-Mb1OyMIk3LSlfeF4zCL3GfCbZXMoQJ4U3z7HG5BhetT7eBGIsPgIRA7tvaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پپ گواردیولا:
جام‌ها خوشحالم نمیکنند، تجارب انسانی آن دوران که در بارسلونا، بایرن مونیخ و منچسترسیتی کسب کردم، حس خاص بودن به من میدهد.⁣ در حال حاضر هر روز صبح از خودم میپرسم: آیا دلم برای مربیگری تنگ شده؟ و جوابم منفی است.⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100737" target="_blank">📅 15:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=j3WPh8QH6eRdJUSBGMEmli_1_arlRhTihvd4aPwo2UD54InNR-mKoVdTaS4BYPCM3bwtZQk4vqyXDg8mt2lVTzZ9S0bTpMZPymGD77J4-AmLetoww-sFpxyCpfAXrUu6ETlAvFjazAosLs7uE5FLlFwnjGfuQdtqP9G9xFjyvZ6mcXQFYwb85UM2wiOhJgL_Sua8EKjALE-9BMsoOYej0PtyZODVcDxsQM7mQbW_IrrO8e45ZAwKt4ARS63g8WG3xcIGXQHVbpySkHrZXGwdCJZmY9ry6ZD5mdTu1vSq2AWgfnrT1noO32WdM-4g0BFOSZYQpVhgH20VhKkn0FkUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0b7dbaff.mp4?token=j3WPh8QH6eRdJUSBGMEmli_1_arlRhTihvd4aPwo2UD54InNR-mKoVdTaS4BYPCM3bwtZQk4vqyXDg8mt2lVTzZ9S0bTpMZPymGD77J4-AmLetoww-sFpxyCpfAXrUu6ETlAvFjazAosLs7uE5FLlFwnjGfuQdtqP9G9xFjyvZ6mcXQFYwb85UM2wiOhJgL_Sua8EKjALE-9BMsoOYej0PtyZODVcDxsQM7mQbW_IrrO8e45ZAwKt4ARS63g8WG3xcIGXQHVbpySkHrZXGwdCJZmY9ry6ZD5mdTu1vSq2AWgfnrT1noO32WdM-4g0BFOSZYQpVhgH20VhKkn0FkUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فقط یک نفره هنوز داره به تنهایی میدرخشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/100736" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4652c3d86d.mp4?token=AN-8rxOKwBrfzJ5XK2STAVuyu4Du4zHhaRz9eidKVlB397A91oLXz_MjYkKqNWMmvU3V02-9FxOM06zndBhtxWSbSC8z7__onjQt737ZDLJUN8yCVXEeXSrUnBiRBb8UPGHo3WahZoTn6oJVlaGwxipPzHsEpV8aDChuP3W3BcALw75WNaqYVWI2TLdbC2kO6uyTf8j2hl1wG9Wr_6st4bPQ7lvLsWpSwhIuIx2ax6K3IOKHqB43sZDMyH7fyMf6dYI50yNOWf7HWHFBuSxsVwi5-iNjKcc5hGjYL4sDyHKlBgi9bQ2TXdFe_V3GQG7oBDemghou8Tn56gq4ipBlJjIIqqEy74lAbFJtlrK9FYJtyI6i7TkpfhRLjwttcEoC1cdwFHDN8ZegCB6JBB-ynjXYEoz4F9Tf4DPvQVGSak9uAreMGzq6fruUwsq1rDGRybp7DRt4v3hf8VEAtmBhtJDipmb49OUe4b818Pk-GRm7CAn-tI9KnxId8-yLNQSbBN-iZrlg0CyYsoSuvidg4UHgEAjKiHO6PLuwA7iP41dqXXKJUTzXyx1uNk8QhRSZJRs0JGcljLScRSqcgeSNIb7u0ChPAetn24C2E7LB8h2K4cmiLEl5vhVM0ha-3sK9tSrmiYpV5vPjSEfp0KL5433A8-EmlRLfnd87WQw1MXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
صحبت‌های میلاد‌کرمی از کارهای عجیبش در صخره‌نوردی که میگه هیچ‌ترسی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100735" target="_blank">📅 14:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=OKCQA1oJanT3uPh7mTcXqbhq1J0wc-Vr3p94EBfOZr_WusEo-53LOIy14NCT28Mx7DBWTxOBvtWw21M4fQvxuUxDMYfvg3DPFmK2jS-nDRv-IN0oW6qu5XzApx7BnDxIWwglN5FLpqBJVxTPwYpRUlTbcPjIDT8rF-svG2SgzpStIUDMfDTxIqUC2aNyqioGA0REVLCx31PkATRMo3DIAmWirAbSmbX5_ql3PZSMHIJE-t-hSlnWga5heFA5iDVxMqeD9ksqy4M3UgQKv2dJcdW-EojLtVxrhBiyTKdZaujozGlctcshjFElexnFhnK0Hl0Jl3FlY0-_-yAZ3etP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf5731dc1.mp4?token=OKCQA1oJanT3uPh7mTcXqbhq1J0wc-Vr3p94EBfOZr_WusEo-53LOIy14NCT28Mx7DBWTxOBvtWw21M4fQvxuUxDMYfvg3DPFmK2jS-nDRv-IN0oW6qu5XzApx7BnDxIWwglN5FLpqBJVxTPwYpRUlTbcPjIDT8rF-svG2SgzpStIUDMfDTxIqUC2aNyqioGA0REVLCx31PkATRMo3DIAmWirAbSmbX5_ql3PZSMHIJE-t-hSlnWga5heFA5iDVxMqeD9ksqy4M3UgQKv2dJcdW-EojLtVxrhBiyTKdZaujozGlctcshjFElexnFhnK0Hl0Jl3FlY0-_-yAZ3etP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب، قلب ایرانه
❤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100734" target="_blank">📅 14:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80daff883c.mp4?token=G3NAvRRgs9rWHX3XbJKl2TMgftitm9BY13YosZo2lmxdqZQ-ciHZIckWY873fw2KjfiuDCKEfsUxhwg7JMO3xI381fcXd4_rRujLqwPA34-llT_ryYmHsCcHxC8phODZWJijfuhfwqTDzXg8jTc27LgA_Po80kSMvkFv2-Hz60Ch6-ZJ1r2EmVH11YNdVms07_ENP89mStuMlqEwCqTm4puhidtjYZpGiMigYBhKf17vB0F4tIuI_Osr_V7yiWwKpnX7IsykkFV5j6O40LUBb3D21V73OBgPwBqWADqlaq2GdIe4ala890NB0Jt568v-CPmbU_vtzsxVhf8x3nRq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نکونام حرف دل میلیون ها ایرانی رو زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100733" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f306dcec7a.mp4?token=PMIC_VludABHU6_BdeUPF6UgcKGlxlGysVxXd07QCRXYhcDD_crminismRA0NqVCWf_A5c20W58znqifk0dTCqEaHhyl31GQMCMhyg-26CpaousIHpq-PCnEdSfnNX-zIAWC8Qh0vhZh0IB5LGcHT2eS7UHlruWG2oPeg5zC_h9jU80MwcyoHZyBRWAhJHsuL1zg0pLWVzdJSLz2GSH3BRTW1i05v7TROagNP3l9zXtsvJNoA9SysrQevDzROBXmnh2WuSNYbbuDNsk9bwTCdTbj-SxY3ulJEjguoBs-921ki37LeFMLFT4d-X5yEfqGtL_3SGaQvaHKrn3-8calySY3vBj9-Ys9JodsSBWqLxrY9KN7QKxCIEhjp6u3JKTSeh-54JeIRvtzOYwKpzL51K49r8WPsMJ_VKrzjZZN5yjhs_WkdN14DtntOlr1Yj-fieDPXhutuMktNivIug7_Jaj-t1NffNTF2jpwHVzqaX6EJp0bfoSGryffS1Frf2qKKxPfvGlvz8Lxn15Jfaiw2xekS-OJFcI9_1MkDgnMvjZJkqfOcLI9UQiATRAKe1n7EwZmEtK-L4dg5JVKGk1sjj6v8EcMll8wMf42Ynv4kasYDV737WTkWzfpIGKJYeu8txbEK2IDZtAsUecwQdGvj2zzeAYr7HbOf2NcocsBg-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های تند پایان رافت پیشکسوت پرسپولیس علیه علیرضا بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100732" target="_blank">📅 14:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=cKVgnYyktirG7oskayB93BAnZ3r-0VvsF5wsMBAG8WWI3YVD-m-YJz8v1Y2GD1xBbAJia-PQsSKhpQD6Z1esPgIdukzHGkOW33rqVav2mrdUs6rS_B6s3k42-wMjIRPc5AX9Cr_thA2v9xKhv7UCT1la-mItThiP6Uap9YBsOc4zVvdWIu8-jIYqTQuQZwlun9jSJV266TxLNFsEmY8Pa1vJXpEpqh3nVyQBHr4UCZQV2AvI0nufUoI0Tyy_4wbCMYFbkPQise-YEYjzZ73ryOllcIzGDJaVd_zTTX-C7v10QbFvnLNoPsN3pdsncyvUSfEJEBht4RHC-Bf4LXqxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa83d99e99.mp4?token=cKVgnYyktirG7oskayB93BAnZ3r-0VvsF5wsMBAG8WWI3YVD-m-YJz8v1Y2GD1xBbAJia-PQsSKhpQD6Z1esPgIdukzHGkOW33rqVav2mrdUs6rS_B6s3k42-wMjIRPc5AX9Cr_thA2v9xKhv7UCT1la-mItThiP6Uap9YBsOc4zVvdWIu8-jIYqTQuQZwlun9jSJV266TxLNFsEmY8Pa1vJXpEpqh3nVyQBHr4UCZQV2AvI0nufUoI0Tyy_4wbCMYFbkPQise-YEYjzZ73ryOllcIzGDJaVd_zTTX-C7v10QbFvnLNoPsN3pdsncyvUSfEJEBht4RHC-Bf4LXqxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسکالونی درباره مهار یامال: بهتره توی رختکن حبسش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100731" target="_blank">📅 13:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=SECiJBREK9B8RoLWgFTVGSqjNJIEZNLigV1MVQeWozSXeN9oQx1fZL9indROEcR4LBajB7g5G6yWQ6RzXpycSuveJ_4Vta8HvVzEXe6tv4ChLBcmVmiAy8MK1Qn0fByCFh4siKma6r3nNMmnGnFh2jP65BMLDyx5i7BPNjmVRyFDHAF4thuypqBqoa1UaYRJLrSkf7BlnBo4DQk1C66VLyf167NbhxS_w591dTBOzCiWOTld0gv9uM-adOOUXZb71STOFLiGA6recoh3o2LRhzlc50oV0PQyPhNeNyIMNDs25v6v9JHEDSjruVjbjYsufLacrkwkWh2YjDVu8MFTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64bba4d4c.mp4?token=SECiJBREK9B8RoLWgFTVGSqjNJIEZNLigV1MVQeWozSXeN9oQx1fZL9indROEcR4LBajB7g5G6yWQ6RzXpycSuveJ_4Vta8HvVzEXe6tv4ChLBcmVmiAy8MK1Qn0fByCFh4siKma6r3nNMmnGnFh2jP65BMLDyx5i7BPNjmVRyFDHAF4thuypqBqoa1UaYRJLrSkf7BlnBo4DQk1C66VLyf167NbhxS_w591dTBOzCiWOTld0gv9uM-adOOUXZb71STOFLiGA6recoh3o2LRhzlc50oV0PQyPhNeNyIMNDs25v6v9JHEDSjruVjbjYsufLacrkwkWh2YjDVu8MFTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
استادیوم‌های جام‌جهانی یکی پس از دیگری درحال کندن زمین چمن‌شان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100730" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_r0AtnwUSXcQ5E422YydksIEmMA8qlNzaQUOte9e7H6iZt_NKg-VCjt2a2k7a6z3F_QdriwfwND4tlJKYN67WekFwGrIIa2RpmIy6gnhnJeuzLHvlml3EaaHKy5SXqKL4yE05Q6Z5zmNp5mJcPHfwIai5aIkMnEQMiMPOi_Pa2qQX2TXQ2_PClfMRw42eNP9IbOTvikz6DqALDdJd7HXT7UAFVZsdviI_w8e9xkJi8mwEV3jD8kWNtJ7l7Nm20CdPZZAhllhXOpYHf0UkVwemeioJqDuVG0XZ7q8n6i9S2tGlQVKmd0n_fi6snuSmsrc4PD2-SoLzNM7beIKUoPuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
طرفدارای گلزار کم بود بلینگهام هم اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/100729" target="_blank">📅 13:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=etJ1X-69yr3WE6sJwZax8wQWvEDGeM5oZLmnHcf8e7xPkb0hha5nN54i4VZhjfp9Pz3aj3Tp0qRIx_jNiWQe66_mGCE8WElK110KnAXqTytohORkTkm5EOGsjZAkVyqOhJ10r1jasPNIviIJ0fEbRkYWetH7d02--oNyetjoPMgUzYUqZ8zmJUY71kM4TMM8fU3zx3jXnd3N2rQ8sX8WL3OSthgouRf_pKQFk8IMa7jON8BCrNRg9pfp2TADP_LGCtFHglDuuEXyHih-o3lCMiA3LevCbgadDOhjbO9WOMYr7nDzQf_zWe1W3pCCiaNIi3LPi1cbIWHo1_kgqSrmmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6593b1cf82.mp4?token=etJ1X-69yr3WE6sJwZax8wQWvEDGeM5oZLmnHcf8e7xPkb0hha5nN54i4VZhjfp9Pz3aj3Tp0qRIx_jNiWQe66_mGCE8WElK110KnAXqTytohORkTkm5EOGsjZAkVyqOhJ10r1jasPNIviIJ0fEbRkYWetH7d02--oNyetjoPMgUzYUqZ8zmJUY71kM4TMM8fU3zx3jXnd3N2rQ8sX8WL3OSthgouRf_pKQFk8IMa7jON8BCrNRg9pfp2TADP_LGCtFHglDuuEXyHih-o3lCMiA3LevCbgadDOhjbO9WOMYr7nDzQf_zWe1W3pCCiaNIi3LPi1cbIWHo1_kgqSrmmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🎙
جان تری: "برای من که اصلاً هیچ‌وقت بحثی وجود نداشته؛ من هنوزم معتقدم مسی بهتره، فارغ از هر نتیجه‌ای که تو فینال جام جهانی رقم بخوره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100728" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=lZM66hKKaR8BvHYrpFfDpJ9rbcj1EgEidJrhP4OyKucbV7Hev4X5BCBVXj5l0nqhBzupCQzeboALzFaFVBqOg7EOkMrnlP8tCg92WCaVoHiffu-ARkvTZ9pw9NBpc-i8jE_9MJ9fAVPgyhAixryIMnGqX1EWRD9rsaH7q4d4-6iRk1tVaJly9v8TdemHhSTrUyjF2wibm3dUjb1ZGIj2OFg8QyQF6N_RMIH5sTWGD3zqczkHrerSH5MQVSnh34XtRuvJJFd-aazSOrBaHZcSjgIKYPbrGokqBAVk0k9Xa8ssnkoxyolZEwvRAFF5Ian9aAlwbkuUKYpBSvYWP7l5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdd66519b.mp4?token=lZM66hKKaR8BvHYrpFfDpJ9rbcj1EgEidJrhP4OyKucbV7Hev4X5BCBVXj5l0nqhBzupCQzeboALzFaFVBqOg7EOkMrnlP8tCg92WCaVoHiffu-ARkvTZ9pw9NBpc-i8jE_9MJ9fAVPgyhAixryIMnGqX1EWRD9rsaH7q4d4-6iRk1tVaJly9v8TdemHhSTrUyjF2wibm3dUjb1ZGIj2OFg8QyQF6N_RMIH5sTWGD3zqczkHrerSH5MQVSnh34XtRuvJJFd-aazSOrBaHZcSjgIKYPbrGokqBAVk0k9Xa8ssnkoxyolZEwvRAFF5Ian9aAlwbkuUKYpBSvYWP7l5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
هواداران جذاب اسپانیا در آستانه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100727" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVGinc5dm49l9YEd0OUVutMV41Z_A7Efy8LcwOzfRGegimR7wlGcJqn5jUL-c0zXNN_OjKP8RpJJ5DHONUEdKmarm8_PKDliiJuzZ1p9-WGrIp03aynDtm3qe4dZ2WmM6E3P7nSHl49HcYKITuJOUv6QNCQXrcjlwJT8e34xpjG1iluv21rqhZCvHp5Si102jygY_mjGsJrF1-GH1Fcx0YhPaSl8gjyuiuykx7J2JAnpStGaxW0DIwTsNoKRzBtNRygMnhM7WtYcYe4XbbIj5m3Q7WauYRGhVS0QvNE0h1GfQ5lvWvRYx5kAIY8gAqsAQ8Azg-k9GmPr87Z_r1ON-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
رئال‌مادرید قهرمان جام‌جهانی نمی‌شود؛ در صورتی که کوکوریا با اسپانیا فرداشب به مقام قهرمانی برسد، نام این بازیکن در فهرست چلسی ثبت‌خواهد شد چون در فصل‌گذشته برای تیم‌لندنی به میدان رفته و جزو تیم چلسی به حساب خواهد آمد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100726" target="_blank">📅 12:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32d7d110aa.mp4?token=Y3rnh7L5r2QE8yNVpFe10feNsXA_N5zof2_c4msqmvHI3F96allrOrXT3jm50XuAnRD4KouP4DUrsWHgxQ59RT2uqa5k9mbPoWjxxYL22XV3F0w9UWhxLRo6teZWSfAYOfwvrw6WECR63w_y4Gy6isnjUfAJ2JXjih8hZ6b1cWDJHCx8xOpgAoTdcgPsxknRx-MM4g0_Ikpx1rEZX2TGST_VdoZQhfhFb7kIw6cyf8osXBr0cNeEkzaUsQfRT1kLDsuv30ORgSYUeRIk7RqHENG75WWbIsYz8r2xFGZWHULDHRmadszj1olAqwbdzRZH1Xb9d757QK-rYpClHbN_qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خاطره سوپرخنده‌دار علیرضا فغانی از پیروز قربانی؛ بهش کارت زرد دادم؛ داد می‌زد، می‌دونی من کی‌ام؟ من کاپیتان استقلال پیروز قربانی‌ام
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100725" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=iSZW9t8kqrG2iCsPAFtTd_wJ2J-8rd_Cq0btSrTRr8QEoKKKVkdtB5H-8rMbbooDtxTLiN_bymHSn_Rafkv7-fWj_4egS8ds02nCLmolnhzUA_pW88Jp8MVF8KcmPwBkUosSxv86eZYNL2r69WKExhDAsq18e_YaRam_42AYKIUKi_sfbDqhh8H9IlyAkBMHIm7-mjvwyBsn_fjqLjn44uCc_LizMp1uKRJpxbc0qdOD59nzMOaSOFOuKRwm4hCsPNAeGS_U8eA78CkRvUWpEnMMwMKPqJX2uqqGrNVL93fGrc-rfnpQoC7eCMAFMKWQLUo5XyrJ7qN5gX50lvroIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050e680fa7.mp4?token=iSZW9t8kqrG2iCsPAFtTd_wJ2J-8rd_Cq0btSrTRr8QEoKKKVkdtB5H-8rMbbooDtxTLiN_bymHSn_Rafkv7-fWj_4egS8ds02nCLmolnhzUA_pW88Jp8MVF8KcmPwBkUosSxv86eZYNL2r69WKExhDAsq18e_YaRam_42AYKIUKi_sfbDqhh8H9IlyAkBMHIm7-mjvwyBsn_fjqLjn44uCc_LizMp1uKRJpxbc0qdOD59nzMOaSOFOuKRwm4hCsPNAeGS_U8eA78CkRvUWpEnMMwMKPqJX2uqqGrNVL93fGrc-rfnpQoC7eCMAFMKWQLUo5XyrJ7qN5gX50lvroIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👍
لیونل‌مسی تو مراسم‌ شروع بازی با اسپانیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100724" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38913219e4.mp4?token=itmZy-ftl9R-qz3cJy0p004eMYFKm620Dlx1vQGWMCwv_T1XiEOUAJwBc9Rip9HWAmr6FxXkSK_XfOIXWLNDBNID9mW5E6dCTZcezwF8_11QvcbnZoDZsbhYoGthqXEfmf-0CB0jsnpFzSKRDYi4CCwgOyZr4PplqqTOPvlDFhKot5QoC36n57zXvpSUYGXMay1SJXEVbpvCl_nvWII3gcP6u0I-0srSB-ce7abx_m7oD6HBBYPHIOSX7vMKPbNtAzCXqvd5HENYQhtPc6Do2ckVTgHv8jSRef-f7xTzr3yWYKsU3z_yBO_md7YWmbA8oHaLAdfthw8E4aC9JFRH0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38913219e4.mp4?token=itmZy-ftl9R-qz3cJy0p004eMYFKm620Dlx1vQGWMCwv_T1XiEOUAJwBc9Rip9HWAmr6FxXkSK_XfOIXWLNDBNID9mW5E6dCTZcezwF8_11QvcbnZoDZsbhYoGthqXEfmf-0CB0jsnpFzSKRDYi4CCwgOyZr4PplqqTOPvlDFhKot5QoC36n57zXvpSUYGXMay1SJXEVbpvCl_nvWII3gcP6u0I-0srSB-ce7abx_m7oD6HBBYPHIOSX7vMKPbNtAzCXqvd5HENYQhtPc6Do2ckVTgHv8jSRef-f7xTzr3yWYKsU3z_yBO_md7YWmbA8oHaLAdfthw8E4aC9JFRH0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
زندگیت مثل گیم شده، مرحله به مرحله داری پیش میری. الان به فینال رسیدی. آخرش چی میشه؟⁣
مسی: من این گیم رو جام‌جهانی قبلی تموم کردم!
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100723" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100722">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e94327741.mp4?token=J7H9dGBGuiPWQelyJ___t1tk4Pc3_iVcM0Qw1_EoxJk1KLDOoFOeXKRRv-a3A7HEKn0zh3bsCbNBjC3ntWIPMRGTo6KcprHpDtqNvFID-EHtrWScRqlW8LRE6l-KsdzXWJOIhre98eshkjJUnQLBA0jhaxcde8bGYgKx362oBxvZeFez4fUR8qCkKdS6KyK86NmX25rnL1c3iVN-NQ6OivW-0XiFT1LHyIPFS39-TFTRtoNq1kisezywHTJk4Uy_-_JiGi_kghKHIlgHdqbMOqKfVXIn7hTEhkDgoA265k2NN6QobNX-538nbFXXS0IJFJzmSMYyAEOyX1nBrHYM9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e94327741.mp4?token=J7H9dGBGuiPWQelyJ___t1tk4Pc3_iVcM0Qw1_EoxJk1KLDOoFOeXKRRv-a3A7HEKn0zh3bsCbNBjC3ntWIPMRGTo6KcprHpDtqNvFID-EHtrWScRqlW8LRE6l-KsdzXWJOIhre98eshkjJUnQLBA0jhaxcde8bGYgKx362oBxvZeFez4fUR8qCkKdS6KyK86NmX25rnL1c3iVN-NQ6OivW-0XiFT1LHyIPFS39-TFTRtoNq1kisezywHTJk4Uy_-_JiGi_kghKHIlgHdqbMOqKfVXIn7hTEhkDgoA265k2NN6QobNX-538nbFXXS0IJFJzmSMYyAEOyX1nBrHYM9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌جالب از لیونل‌مسی در بازی با انگلیس :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100722" target="_blank">📅 12:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100721">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXBiZPZj7MmHEhhZ238xYOSbZl3TlQVZOH_kvyR3RnsvJEZ8_V3Jo_yMqUdrweWABYxw245lf9tBZpugqWcyxL-YmLsTMwMO5xl1zNPNePf_n5HBeTl38YSUU88nmzt4tQrLtKnMAb4BzgndK4u5BP6lDaRyxKaOjZLDRRmZj0k8DZbfRZ3Y0AgMGuBdn_gsspl5S9gmv_HQV4BeBwGSPiMHTPBvfkMPFxoVlWqEEg98SPf4H0zSMLoYqz8Xk1jROQSYEB6gM2oL759He8ETW0hXICmAhpgNVKMAcgzAcFSP2RbfV_DBR16QBOTnepfGYF03cD0tBT0XpAmNCn9zwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇪🇸
نمایش هوایی جذاب در نیویورک پیش از بازی حساس فرداشب فینال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100721" target="_blank">📅 11:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100720">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBBEQZp4aIS-gEHbiO8pN2PW-xwV8mk5K-ubSmLnRFxL3sTAWvxUhhK3L7H_hAEbZMxOP-UOU5ZR-MjPa0a6F7qKqbzUmYXIovVwruKqK23wLghQSQQ84B5O1fOqsfSMdtuxF5WSJwJeP_mSff6xBXwzw6W6x0EDc0d4SDMYzAUhk-4yc6srMx-bm0LmrPJvb6JpLMkAyWX1GIX6Vg3zT6JqoYYiVha9mUjSre1EsW7arfW8LHB6Z8BWRXw3ZHPLho_TqsNy7MWZARisp6UeehTBVqf7MU2z6cK5MTNQNqWnWcf7vFYZ0ZiRy-BwrY-XHk29EoEseZB8shWXwfnyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید نحس
😂
😂
تیمای بازنده عملا قربانی اسپید شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100720" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100719">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474e4374db.mp4?token=epDP56XhXbtuAr6xz1Rj7IqmN88YVH2_V3pPoh-PiElB4HygMcXGYNbDCklD3uDZnr2kjX0t9mfxCGRdh2jin5_kqtmy6szcW6slpmET6M2n-xM5UDdOWw2AtFpbopQcg0nV4PRADJRJlHXXeZyqof2tYpcubdB13jPEvNTPWAAOqqzgTNaigwnCx-0jazoWKwGc6o2_Ckb9dc4Fe9xmjSnImMYaVzyALW5RR8Xu3u44AVyR7rrBGF9oohfj47pgeMSnzdq1JoPsWWypRO8pkasSRV6qrN8s256vCjAoevvxtPxH7UJz5SakbiIo_V6VljFQGvB25i25cfTCMeNscw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474e4374db.mp4?token=epDP56XhXbtuAr6xz1Rj7IqmN88YVH2_V3pPoh-PiElB4HygMcXGYNbDCklD3uDZnr2kjX0t9mfxCGRdh2jin5_kqtmy6szcW6slpmET6M2n-xM5UDdOWw2AtFpbopQcg0nV4PRADJRJlHXXeZyqof2tYpcubdB13jPEvNTPWAAOqqzgTNaigwnCx-0jazoWKwGc6o2_Ckb9dc4Fe9xmjSnImMYaVzyALW5RR8Xu3u44AVyR7rrBGF9oohfj47pgeMSnzdq1JoPsWWypRO8pkasSRV6qrN8s256vCjAoevvxtPxH7UJz5SakbiIo_V6VljFQGvB25i25cfTCMeNscw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سوپرگل میثم‌تیموری بازیکن نفت‌آبادان در لیگ‌یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100719" target="_blank">📅 11:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100718">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFDLClpjoUji69yLD9IoNMiX0kG0MjuppXeXsrv0vNLgJWoT6Ee3ov-Y0SuAljoiC3L-9Q0sndi8ZltPDaXM8N9ITH3mYrifoxNy6IahHKwo4c0fybQ1tX0MKi7hAXEoIioyrtj-nLnxlcD5RrN_8jXOaRy4uT8wmZpf64tPTsbmuL80HgexgjuRz--_NZVG1vw-LX2vJx-TJfgWcgAWvcSLBaseYE-UUx-6waAPL_toIi7us54eXDIaXrPZMYjO-HaGyfQDH9GqdwtJLDkXrLGjQlFHdg5MWeQcrZpdcBXtfbKGTOX2Yugb4doxzjZYAWI0J11okEKh3zmX_UgNRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوووووری
از نشریه بیلد آلمان: اولیسه در تمرینات فرانسه به بازیکنان کشورش گفته که فصل‌آینده قصد داره راهی رئال‌مادرید بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100718" target="_blank">📅 11:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100717">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=XXPD9AYJQcaSx6zAhqvn6gGSZnE4slI1pB_SpCINhvHP25nGd-D1jmTRh2kV-B9AFwJGbyyDQ_TE5o8VQZYjMziBjlsyIuepxYCJ_Az-rPDKyt9GAQiDN7ko1d4I9yynh0QOboYnLpVVPjK9WXxPz94pHD78OUdKeD7N0K_rp7-Pu7laCJ8FXboScdfPK_gkUuKkK-rWh3JOf63hDa6W43VBydYJtubOwfhDqL2QCRjRtXc5i-VoR5yq9QmTjFe6CILt-YvJjnPzVS_Qs9gECQIcl1MBW-X4vq7QKJKO9I5lNbt7hGITrdNEA9NKmhfqKZFwd4CIBZDN9yTYPK1kf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c0ee7122.mp4?token=XXPD9AYJQcaSx6zAhqvn6gGSZnE4slI1pB_SpCINhvHP25nGd-D1jmTRh2kV-B9AFwJGbyyDQ_TE5o8VQZYjMziBjlsyIuepxYCJ_Az-rPDKyt9GAQiDN7ko1d4I9yynh0QOboYnLpVVPjK9WXxPz94pHD78OUdKeD7N0K_rp7-Pu7laCJ8FXboScdfPK_gkUuKkK-rWh3JOf63hDa6W43VBydYJtubOwfhDqL2QCRjRtXc5i-VoR5yq9QmTjFe6CILt-YvJjnPzVS_Qs9gECQIcl1MBW-X4vq7QKJKO9I5lNbt7hGITrdNEA9NKmhfqKZFwd4CIBZDN9yTYPK1kf4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇵🇹
علاقه شدید پوریا پورسرخ به کریستیانو رونالدو و عصبانیت او از تیم ملی پرتغال بخاطر ندانستن قدر این اسطوره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100717" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100716">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ebbda285.mp4?token=sUT5MGR-tYxm3x52H2Wpk5UvY2cgGF50dgvyp6iyvumLWl86vaQgEgT3chq_b2WT54opTY1alsJYxiW89KpHnGi3FsM1C3UprCCMtMWPyDh_R_tsPpmltojjh3D_J6KRMWDN3D-VW41_teO-UJimMnI_IgQ8NMUbijyBCuWlp-ZtIqXYbR5kGVp7_Z4vPh0944I0cUM8Gn7Fo7tLVnBmDqluUxcbA2t5IswkG8FqZfSRfpezSBpwzAvmF9nb7pXIJhPxtpr3olZahebgIOKVc1_OU5GL0uI7IwF7f3IO3hBgDqA9L-pyI-B5fdNBAwXMB9fSQdXZycR8XUue0I3oqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
🏆
کوکوریا در انتظار تقابل با لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/100716" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100715">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3GoyR8P6lAGWkxU5K1FoVQP8oJpG4r53GoP5bLkYuldy1RUUlYz1JM8U2scCiot5Fv6qXi3yGbrRyduR7YENNlSvJ_DoiKba8CnC6VN4UuKNMkPRBLtDgCB64fz87qhnhzLZBJZ1CQYL4caSsyL-R3oD20Jod6tg-ToR8j3V5M63hIMU1LiOq0VROVi-5j1HCVfunA6Tik19gUiV3JbolrVM4ZUnfspo_sBOGbLcm1miFOzsS4PG9garFcwxzhlC4mudnkVM8idWIoW85vWlP8Ax4wLdR2iOlkpU_VLE3CZkfLow_xRpEsiQM4S9_93DPafaF--gzd8Mx4o-xLKWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جان‌دوران انگلیسی از ژانویه ۲۰۱۵ تا به امروز در ۵ باشگاه مختلف بازی کرده
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/100715" target="_blank">📅 10:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100714">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=jenRR6XxTCSIfhRbYHexVqnVArJ21LlklDQ8cjTzkD8IGL73jwhwJJ7ytpv_gbOc8FneF0uwUMhskkmeLEq_DZpK4hYT1NWQyuby04BlINOmZ5oCiWe_P0ht6BzBcEAud4Wrvih0rOuq3CVDS6tsAjK5Y_lyq5qwwf_s0LjAY0zO4xBMS3ACkSw1pyY90qRAhuG2fqSu40-6il9ENmEbrYXExbkbtieNfoa3RgLOnwyPDW3L7T5baU6ZninqUa3W6YMF51nxs0seEn9V-hssWWZJNBvACTOPMWkvozaUQQGvV7tZkg8qtur2FUjdTzPThGwABPqbrcC3gmCmZtVM6l55OCV2HS5ird87-C0flwUY7JSCQ_EMwzbbnsqjmeScbyx-1SX6-chKtqGu0PjeenZaabSRoysuG3hSSw_B8H3aKSQpKuLo0zDZzOc1kXvwUkjTE_johE4tb2nDPZlPBYxGrzqo5xx9SeCQu2GFN-dyk4VhDgmYe5zF5VIgt2-L948-9Ou5lGj8FxrGXWs_lLtzFQQ_8tSgUnh6YRxzNN-KYD5WApNP_4OSUFJIxEk6BWp8FvuyhGi33KCJ_CAFLnE6bPVm8Dea21V2tUxTYPiuz98pmwK66a0YwkmLlCElZuRwZgnLnbJrZQYqsJHfH9-5ooBKvrhttsUzXTyOQ7Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638800ce9d.mp4?token=jenRR6XxTCSIfhRbYHexVqnVArJ21LlklDQ8cjTzkD8IGL73jwhwJJ7ytpv_gbOc8FneF0uwUMhskkmeLEq_DZpK4hYT1NWQyuby04BlINOmZ5oCiWe_P0ht6BzBcEAud4Wrvih0rOuq3CVDS6tsAjK5Y_lyq5qwwf_s0LjAY0zO4xBMS3ACkSw1pyY90qRAhuG2fqSu40-6il9ENmEbrYXExbkbtieNfoa3RgLOnwyPDW3L7T5baU6ZninqUa3W6YMF51nxs0seEn9V-hssWWZJNBvACTOPMWkvozaUQQGvV7tZkg8qtur2FUjdTzPThGwABPqbrcC3gmCmZtVM6l55OCV2HS5ird87-C0flwUY7JSCQ_EMwzbbnsqjmeScbyx-1SX6-chKtqGu0PjeenZaabSRoysuG3hSSw_B8H3aKSQpKuLo0zDZzOc1kXvwUkjTE_johE4tb2nDPZlPBYxGrzqo5xx9SeCQu2GFN-dyk4VhDgmYe5zF5VIgt2-L948-9Ou5lGj8FxrGXWs_lLtzFQQ_8tSgUnh6YRxzNN-KYD5WApNP_4OSUFJIxEk6BWp8FvuyhGi33KCJ_CAFLnE6bPVm8Dea21V2tUxTYPiuz98pmwK66a0YwkmLlCElZuRwZgnLnbJrZQYqsJHfH9-5ooBKvrhttsUzXTyOQ7Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
آخرین وضعیت پل‌‌ها و تونل‌های هدف قرار گرفته شب گذشته در استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100714" target="_blank">📅 10:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100713">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91953d632.mp4?token=Upxe01j-C2CClkZyPUPN9gKztpwEgGhCMv3MTB9b2WUquIwJq48XXfcX42C5ZDVlLBy2rr3A3hou-Pptk1n11y7RWvm2HJhGx7FUzAWZry5mnIGmcLHfN6aYBZVCsZwooISjEQsGJd1G21n_3VL35TwyNOqi4bG-HkKKcF0LkQ5Mv9SudDeZBPt9mkP89oewC-Ooehq0qeifH1OKqDpuLCbKX77Jl47TxT1lhOIyfSMQq11fcnho0uPZUePlNov-jQth6KmKPDiEXjknFJkxB9srkI2ttpjhsBJsDxfZmu_olhEL2MqGWwUUcJcF8P4pN8Esl2z43Y2NyEoLNeEq1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یامال رفته داداششو برده آرایشگاه قبل فینال موهاشو رنگ زده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100713" target="_blank">📅 09:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100712">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=rQfioK2AZNzzBafL9tmSt-hI6LZVbxRfm98vtttIvBtxhR75GH6f6xTc7NwWY5j1pJ7HvR-PemvulZywa08xe3Xyw7ZASj4ltJkU_Sk34HS--0hMldtGogWlWNylhFGPNfbF_74pBW3Jv316q5BfLW_CGaPy6yoRFaygTOhPqN0SrqKptMvBaNJ5SUBemBQRqDxvDLQXQPzjQXaIuj3qu333IYZ4acXPo3wDvlfK5LPd0Xt3yYTmnzPx42W1A05OqFMy12CqzpgDhW0neNEgrew_yXGmKXZJdLnkvzzhzcmsB0hHTuVJCBCPxzAs3kObCcaWw9blQfUGgC3iw2NecA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2382f600b.mp4?token=rQfioK2AZNzzBafL9tmSt-hI6LZVbxRfm98vtttIvBtxhR75GH6f6xTc7NwWY5j1pJ7HvR-PemvulZywa08xe3Xyw7ZASj4ltJkU_Sk34HS--0hMldtGogWlWNylhFGPNfbF_74pBW3Jv316q5BfLW_CGaPy6yoRFaygTOhPqN0SrqKptMvBaNJ5SUBemBQRqDxvDLQXQPzjQXaIuj3qu333IYZ4acXPo3wDvlfK5LPd0Xt3yYTmnzPx42W1A05OqFMy12CqzpgDhW0neNEgrew_yXGmKXZJdLnkvzzhzcmsB0hHTuVJCBCPxzAs3kObCcaWw9blQfUGgC3iw2NecA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚫
افشای مکالمه مسی و بازیکنان آرژانتین بعد از پیدا کردن بطری آب پیکفورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/100712" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100711">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dccbf84030.mp4?token=HTrFe0JFtLPpVojc0LSInKGDM3aQ-Dgo7yiwvm5gePm_pMubeQLy15LVWvRRttccS5jjkIreAuGEnvDLG56ZMV8DnZxJ45auInLrWnZvvc1cP5bFlUgnHCGwdLQTUtCyorC-WnBQNtHYlqM__UMiDezy6iCecF4_lYSnbviFuLMjpzHIAKMMlihE89qGnEPBgytEgZNmI4O-yxdMeg7ptA5YK7DBR7oN2TLwcuPtQUBx2snrDjuD3plPg1ib2EZXwUR_I58bkwW8xfHorOHLsKGmj6QopBuijjtlIaESqY0sbYNbL9ri5YniWAGsObxlnbL0ZpCZQw_CYobwlC1X0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😐
صحبت‌های عجیب وحید قلیچ کم‌عقل علیه عادل و کریم‌باقری و سلطان علی‌آقا دایی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/100711" target="_blank">📅 09:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100710">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrZfVWpAp2RqbMyRAq7olAZfT8OANzXol_8WZsUDcNsRKgDJk3nNvpM1836_UcgzXXCKaJP2R6ptNrlSt4MNpVaAZZtgxXMEUzgnQuBtOAaQG4OihHmR6lWV1ScXUvRmnZbOogRwUTavqFD5QNYyUzV7k0Ziqmux3ZVHeHWSoA6d6Vpwn2HuLkSyyNxyLN_Oi68Pkax6p_6WIHYjYJCAw6tryBCkhxvvHSqIeFbGVFIM6k_-LEgAIXDqT6Z_tnpHYKRtIaYogWMabQmBVfLxm3zT7BNUTOijGPzjeJNpW7dyQXsHJF_TnnCBs0cMqKpq_NW4UUySQZuS1yEqteJqcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⚠️
وینچیچ اسلوونیایی در جام‌جهانی فقط یکبار برای آرژانتین اونم سال ۲۰۲۲ سوت زده که تیم اسکالونی مقابل عربستان شکست خورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100710" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100709">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnmwHvnpohJVVqL87NrZeaLN9jCEAU3TG-9XcohHQOieMaL6My-K4FlIosuqIPihsaqLxOjioSxKaBlSY0788bojHbFMj7wGBbEshJ9myD2sXhifZDVSqgQgM18RxbK63pKD-rkC4IfexnP9e4g3ksEmYmkqOQnN7A20uOY3sW2VJ_vZaKEpeFHHbVUvXEll-XiqeeDE2xUGLxmA76-_92NLBsNSWqHwKMCBQxEL-IoWdDLSWBbEiSxVpHrspJZNjC3TzqbXS15JmnLVuZC_zdA16idlCrM9WtUlf1KKVh2MJrm9n3HvH8RhmCOYwYnqlLp5_Z67DE75qHStI7JCGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
⚡
تو این مراسم همچین قابیم خلق شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/100709" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100708">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=cq8ONKrcytmMSEhcdAL52Q0jvu_o1h5hjDM4MNY0yDEnasQXMqdWPKMLwp9JndJNgs9BtNkTw_fc66F-yWjhFczMi2y6YzK7vAdsUR01ArjsJ58Wuj8wNbbr9HwJyoYQmdbV7ltqjqA6Qmd7RjnvP-qscZJEnYY-Egwa2lZvnOVXxZSQOqPPY9KjW--5cziZldvWrmYMjq3gbEteNcFTcVefNP5aTbhaUErCbb3okA_dk8RbkfQihZLDUtxVNCM1wOHXtNlMDad_Skp8iqFIj1sinCfVLXwlQGXKF1ZtYVIsCDT-xO_1utDR80kvLLDd8wvp7OAzRFQpiMP3YhgAxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136aac8a04.mp4?token=cq8ONKrcytmMSEhcdAL52Q0jvu_o1h5hjDM4MNY0yDEnasQXMqdWPKMLwp9JndJNgs9BtNkTw_fc66F-yWjhFczMi2y6YzK7vAdsUR01ArjsJ58Wuj8wNbbr9HwJyoYQmdbV7ltqjqA6Qmd7RjnvP-qscZJEnYY-Egwa2lZvnOVXxZSQOqPPY9KjW--5cziZldvWrmYMjq3gbEteNcFTcVefNP5aTbhaUErCbb3okA_dk8RbkfQihZLDUtxVNCM1wOHXtNlMDad_Skp8iqFIj1sinCfVLXwlQGXKF1ZtYVIsCDT-xO_1utDR80kvLLDd8wvp7OAzRFQpiMP3YhgAxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادل فردوسی پور بی خیال آناهیتا درگاهی نمیشه
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100708" target="_blank">📅 06:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100707">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htk9Ew4rmr4lN92Z1zvJcMg2WHcPuXzIm83Oh5uCdv3wxglgH3jnA0zNMMkyJLE4-OEbhs7ULxTVzuatxZiN1VBQGaxwMlbGzXfOiHA6mEJoRgdClGBErQhXS-YWmaNbglrtcGMkyAm7L6G7isckFdSWAuFsVt8eI98BOJAzYvk8MP3ttOY8vvD5JQiQJbMDF-PBa_PMdU9jU41WRnTSPc-yhYNfGaBxhKytW57yF22wIKtxXzD1nPjmiIrori20SiHXydsUbDGRJpbHue3RQ14y90xgwhlgF5qnp9_gboAaGnQohhqs1hTOenamRUHkwLwHj7kOScttipi1E7B5FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👍
لیونل مسی: از بچگی یاد گرفتم و فهمیدم که آدم بیشتر از اون چیزی که می‌بره، می‌بازه و فکر می‌کنم همینم بهم کمک کرد تا چه به عنوان یه آدم و چه به عنوان یه بازیکن بزرگ بشم و جا بیفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100707" target="_blank">📅 02:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100706">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdiJk6manYethXKxADFM4MbPpjheKQTNrH171chwR7MO4d_U82pQbNmvxAcS5iA6PMXbDZZeXNAkJC7WYHFbxhhuhNdc6_Mmjl3JCvThTd2fBs-yj8jchLEq26VrAVQMCyWJFlf8S4u2WNbeBY9w76oBwos79wwk2waIjhgHWUQKwrlELbx0yEcu7YbZnEEy8vH-KalKT2HsEpaD95ThQvIsWZ-nmDEurzORDEZx3S22Aar252SculPwP3hVcmWgC668P2OgE5wCkyGmrbB2CL3HDMAzhhcWXVnO1fuJlr90ttxFzwOMkkH57Nw-TpO-zOjAhQJOl62T1aFs8XV6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🎙
اسطوره لیونل‌مسی: بدون‌شک لامین‌یامال یکی از بهترین بازیکنان فعلی دنیا است. برای او آرزوی موفقیت دارم زیرا باعث پیشرفت بارسلونا نیز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100706" target="_blank">📅 02:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100705">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:  ‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100705" target="_blank">📅 02:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100701">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGax634jMFrlLcWF1-H7mklNVBW2XTkZC4fdao6PjqpcDcmuf991toUlXJtkPcTnQ0iudQIblHErgacED8rXp2Grqy9K83nsS3MTnJsM0Ny47qx8Vis4eB-S1dUb_dcAtRlEblmh0yJt3O8Of5UNDbtHbhakpr8np7yRtw1ZqWWEJalKY4m8x9_wFfB5Z519J2FrsnnG1ezNVbh43AIYdwXpGjiq5xjyPedwiykFid7q-_YsyX4gdORuNf7_LMPDU1ZDZUV0-1xbYHdIVNJeY-lDx4kzt0cPjIUMXhgD3qB5qad1DPnRdam7vE19E8nf7XPV00TNonupV7hYWIvHXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWNwek2Q_iEIlSSsPY6syj30gNyKzGbgCLKGaxzBBOhOp5zE1YEY5Z5R9P6z4x99qqfZv9b9i5L94jKd-WCesJtO6dlObJ7JDxj2DoaPY4lqa2WqSVjhOjySwQ7n_-yREIdOkW-knhdx-cD0shWBBA5EZezISXw8d198WStd5rEAZ4_3SloNcw_BzwNrHFQ_2gyfNNwniDSqOCJgQpa4Qa5nFhUUdRS0kdxHBslgv74OKW9_N2rPdOZnLdp1p9OEkshEOU3vQo8-B8AcPxvSuQr_b1ADb-jSIaWRUcS38Pz-drYHR6dEb56JnxSHX5Av-7hiVso_1LeUuNISmiyrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbLgfYPObGE8JyC2nAzEVklJCOMyTc0BdCx-_rJGbXVulSGowAPxCX_nOgZMQckT78n8GdQDflg3od2DjiZM4nefw8RUPa4Lah5OeytJ08UeI3xdKUg_ZYIBAnq4NLc028LfqaY0zkWsOMyPoa7u2DyDBj_ifYBGLtzgQiy_-3fAeq3E0WZz6j-I-NpJ2gSryqsst1avMvYB8UaE-K7CaC55WiF-_m8ZatAKIKYJRsBFIjun-TMSwJqL6icSL6V4RbsWlqKZ6-XCZ8PSTqDwPKFkK4kPywVOeCcrK7XiSmWVnGTOYKqvo84TGEsVtBd3IIImKecXNMrv9KT4JHa1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJCcX2dKE07iOT2Fx_13Vb15fMdkd4_Xs2trbCh_XwMzkF4nX7K-mg0WrN4aEsSqcsvj_2KWCsTTxf48sYzsZGM8UmwdSP0QApmeZiggPC9IdjBMrWDb-_tOPzQN03c40cYudJu73MlyjPhVBk1aI8C84iL6gPiMpe4REAjJmXW9JFv7cPeW88jH1L3HIQ1RPTbdWc5XqBJzqqVDwFt3fMwYu8hfHTRj05DtYCrMUs2gmIXOxxWS-uI27MucEJR3bRP_8lqmXJe7C8kfkYYzrd52viNHzc7chyDY72uRwe1wK86rxrZ6lcQA8p_Ijfw767w4cgxq-5ccHHi2Y4zMsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇺🇸
📸
|
تصاویری از مراسم استقبال اعضای فیفا از دونالد ترامپ در نیویورک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/100701" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlLhXB87IiCyZzPKXkK8lJUmqkEFcnxKAShsqlV-JAOiAzPf0AyXJ1tCukm1WqyxWerXoCaYxDaIS1_o9__q2O7-KtJR_q27BxmFW5xUOVWoXZUx0jCBTzFBmpavO-SnGN59Z5vKebOS4wxPBHIal-373fDMDftybjvVuFX_2WmUvzpNdeLkLy73tOyCR0cSeV8Sr-eXBW7e1sSKRBOdCyg34JFBC0AWxBog34skhXl5xsREczmneYR5Q9N071aFADVuRmnKiElXmN6bqR1xdBygoOsJ6qn6jOLL_vW_WjvlvIwJLxzhvAthyNMeWpteD0KLRaYg0HvM6Z1vZYrksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/100700" target="_blank">📅 02:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFsF13XywCEF0Zcu3z8eArxmxiM_zrhsgvmSEuhLKy8nzlY0WXNIZ80VPOpNXCBTgOeDI3kFVK3XPswNytVeL6jfLqUERZcqU38TgI6v4rpwPlRHxU_JhrMuNuvepsUXxQCl_h_6FYne2pmOdtoX0JgDbRhHlN6fwS9MQJ7huEiv5Uqg5LVvvHo-A5JvxPC7gOqm443CwYpSau4hUa-WEvQf0_l0prJ9SFzfb5TX4FFYh_Cu6ODvbB3FbHc1rcOO8mL9f2Ad5nnEkNWMinxuGys47yqxb48jFfye9DfdISv0njOsqQN1uCKLfNjYTr4V1eJn3c4758Q-d0KymMqtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇦🇷
اسطوره مسی:
‏"ما اشتیاق زیادی به بازی کردن و لذت بردن از آن داریم، انگار که به جایی بازگشته‌ایم که از آنجا شروع کردیم، زمانی که کودک بودیم. حریف هم بازی می‌کند و نمی‌توان همیشه برنده شد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/100699" target="_blank">📅 02:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100698">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHu3REwLH9AeziF_FE_FKGyMrv3XrY3_sipEUHp3Y4goeqXDvGvmMyRc_SyQkbxWHRFieYQVEEEEsHusdVCYJQTLigmPuWhqHc1zdWYVOveZVzlc31-W5otEEgSjSWgkVCoFxauJossIvNalw68ZiI7Q76LbAjvAPARVZ99RRJSCVPiWm0zC4HAoMk-XFAP6npXA5VnljSqu5z769DTzDKz-amc0xWinlg7MTapexp7XPmKVRzK7V_Pc3XYuBHQgf3nIGxg7mUwkz_6b3qvFdkI91Q5vOBDhpLOa4wijZdYo5-4Te2N94OC8LTXE5xS6RPiOTQrYC9xqGXf_tbIviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
اینفانتینو: بنظرم جام‌جهانی ۲۰۲۶ بهترین دوره در تاریخ مسابقات فوتبال بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/100698" target="_blank">📅 02:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100697">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
چند مسیر اصلی در استان هرمزگان بدلیل حملات و بمباران‌های دقایقی‌پیش مسدود شد
❌
پل محور رفت در مسیر سه‌راهی میناب به سمت رودان، پس از دوراهی سرز
❌
پل «شور»
❌
تونل شهید میرزایی در محور بندرعباس ـ حاجی‌آباد در هر دو مسیر رفت و برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/100697" target="_blank">📅 02:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100696">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJ3qH9Y64WtMWcv40Y7pApWuSJWV8EZKCkwBf_V0BBqCF8zeAwlikAJkPVLTqLqJm9EmkMMGUyLIIGI-TmxMo71hOrbeCq1JpZUg9X-1TUoGN16kt58NcJdK6xL_Bj0FB156A2jdOCY3DdKzBQjnAZmY6sKRbVZkPqKseYYPRYHLmjCTvmqlgZXQBz5gipPVGbA0jnYo0hdUXhSZHan-n9aAJDe6noDbtAKn1PHFTm8OIsedQVv85g9pNhyfjodEY2MKqLUqOslxZFmydPaKVfaGIsoRQNPwgyn1H14jFL6SvG2FItuUYhoWzqMFYLXERSvtIACQbmtear6rWUW6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
🇺🇸
ترامپ: دموکرات‌های احمق در انتخابات تقلب کردن اما من در نهایت برنده شدم و میزبانی جام‌جهانی و‌ المپیک رو برای کشور گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/100696" target="_blank">📅 01:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100695">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🏆
🇺🇸
ترامپ
: امیدوارم یه روزی برسه میزبان مشترک جام‌جهانی آمریکا و چین باشه. چون فکر می‌کنم بازیکنا از مسافت پروازی که طی میکنن کونشون پاره میشه و جذابه برام
😂
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/100695" target="_blank">📅 01:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100694">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=ECjTk1UvwhJLckv_nSrQLZrQW7fcs2EmfEYlIu1kGG_Sd3Ng2FU7L06W4Kbb0SPcLtn3hvsXek1he97Pf8L4IMZDYlvl3Ir4p2nMw-bXyKZHXatGfylEwf0ogU-Ck55d7buUePmcWckx92Fxh7NNUZF-iIgeOeFjGKRYBK12S58DZyBAx2xSBsT7wCRxl5vfFL_hCekIWRwiYSZhIUzhk642ZTtfHONkd6szw1yyjkTTrlY3VKJAvK2pM_rupcVO3kMkv67aeNiNWh15uuZKXmYu06hpDzFQo02wF4EypOwSP2URFmcqhOMQfKtBfLMOpDEVNEju3L8REEVJ-f22s4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900b057c2e.mp4?token=ECjTk1UvwhJLckv_nSrQLZrQW7fcs2EmfEYlIu1kGG_Sd3Ng2FU7L06W4Kbb0SPcLtn3hvsXek1he97Pf8L4IMZDYlvl3Ir4p2nMw-bXyKZHXatGfylEwf0ogU-Ck55d7buUePmcWckx92Fxh7NNUZF-iIgeOeFjGKRYBK12S58DZyBAx2xSBsT7wCRxl5vfFL_hCekIWRwiYSZhIUzhk642ZTtfHONkd6szw1yyjkTTrlY3VKJAvK2pM_rupcVO3kMkv67aeNiNWh15uuZKXmYu06hpDzFQo02wF4EypOwSP2URFmcqhOMQfKtBfLMOpDEVNEju3L8REEVJ-f22s4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترامپ: هری کین بازیکن فوق‌العاده‌ای است، اما شاید در پست اشتباهی بازی کرده است
به نظر من، شاید آن‌ها (اشاره به تیم ملی انگلیس یا بایرن مونیخ) اشتباهی مرتکب شدند وقتی او را به عنوان یک بازیکن دفاعی انتخاب کردند. آن‌ها بهترین بازیکن خود را گرفتند و او را در خط دفاع قرار دادند. این موضوع کمی غیرمعمول بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/100694" target="_blank">📅 01:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100693">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=KUnvePZLhRgAEkZQuQHlwNY8mMT-KxHbZMD3gz1pMlaI2nRF_rg1H5E7qxyJCQuML9W3tUlbQgc_3AmRvNXO2AZQQ1eBTcTTRBRehoeICeJhXlIgUJP3c4J11yKc1HarDUvTuUNPkL7rv9KudYknJTK2Vi0_u1nwlojlFDmy6lKcekaV1qd97gEKFrKWuw1aUhHRwEwjYGpvJFH6Ocg7h9bylt5wwBXDvdq9G01jcu83Hi4OjoulV0O-PFbUxikEfMEaDPpb4gkmanReHzdl5nQdWaWUxJO0pYUjZ92-OS_Ce0vYHYBxoRmPzgRmcEUeZd8CgsKEFsfAXKITg_LLZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16c25f51.mp4?token=KUnvePZLhRgAEkZQuQHlwNY8mMT-KxHbZMD3gz1pMlaI2nRF_rg1H5E7qxyJCQuML9W3tUlbQgc_3AmRvNXO2AZQQ1eBTcTTRBRehoeICeJhXlIgUJP3c4J11yKc1HarDUvTuUNPkL7rv9KudYknJTK2Vi0_u1nwlojlFDmy6lKcekaV1qd97gEKFrKWuw1aUhHRwEwjYGpvJFH6Ocg7h9bylt5wwBXDvdq9G01jcu83Hi4OjoulV0O-PFbUxikEfMEaDPpb4gkmanReHzdl5nQdWaWUxJO0pYUjZ92-OS_Ce0vYHYBxoRmPzgRmcEUeZd8CgsKEFsfAXKITg_LLZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
ترامپ
: من فکر می‌کردم که ما کشوری علاقه‌مند به فوتبال نیستیم. اما مشخص شد که ما یک کشور علاقه‌مند به فوتبال هستیم، و من فکر می‌کنم که این وضعیت همچنان ادامه خواهد داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/100693" target="_blank">📅 01:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100692">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=UU5Bpo2gIdYYBrFoyWK062f_W_RS7FhLEAk-g0V6d46xnEn4_pzoH-bF65ylxfcgXBqlqBVwcRQzH7MwcTY3SjhUuI4uo0AmB6RwkIHl_pIk5L5fR8yAW8mumiNu9KJytcXOP-oKBcWI-gK8la_mpRA01D0Edi9qbhC-tbosEPGItKP4fBPsRDDuO_75ZmSdoFBeUXZX4Ijty-j12mvtYy7XVH0qFugPOboRNSX240Fbb0UlpdDtSINEEk6gUyosl0MDlA6XjlvdAVkpSLohTy8PFgKLMaz1Art-WnL73zfZiFE5qbB7peEq8AVTYD80a-S5jrJjEUSrDAZeUKIa6VbZXLr2o9T4m0n1aNfKk9YMGghlAJhHfJdLktkQo8QO2Ln67RIy3hVoz0FWGuo-6HesNEdCNMEJEK_bDppPKPM9Hri2_yNUE_moGTolhC6emS7-nL68Op6LVoLj6IR2m9f8VaaLBMEb8YG-cSkfyp1Hq9bWJeBYkhQwGFskhGJnmP6Nnhdv5TnUD7Ni9hItKwH2qJtGbhSAK2sY04m_dXJ4Ox_EOO38qrMtOJBL39EetqJ8lemLSQ8GK8yixOih4-YktQsz7qiSIDzAnS22HPENezN5VlmdJjPoxM2vA35yKXg207JEAw67irntEWj_vx8tgwZmdkUOjChefPzlcOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d154c16b.mp4?token=UU5Bpo2gIdYYBrFoyWK062f_W_RS7FhLEAk-g0V6d46xnEn4_pzoH-bF65ylxfcgXBqlqBVwcRQzH7MwcTY3SjhUuI4uo0AmB6RwkIHl_pIk5L5fR8yAW8mumiNu9KJytcXOP-oKBcWI-gK8la_mpRA01D0Edi9qbhC-tbosEPGItKP4fBPsRDDuO_75ZmSdoFBeUXZX4Ijty-j12mvtYy7XVH0qFugPOboRNSX240Fbb0UlpdDtSINEEk6gUyosl0MDlA6XjlvdAVkpSLohTy8PFgKLMaz1Art-WnL73zfZiFE5qbB7peEq8AVTYD80a-S5jrJjEUSrDAZeUKIa6VbZXLr2o9T4m0n1aNfKk9YMGghlAJhHfJdLktkQo8QO2Ln67RIy3hVoz0FWGuo-6HesNEdCNMEJEK_bDppPKPM9Hri2_yNUE_moGTolhC6emS7-nL68Op6LVoLj6IR2m9f8VaaLBMEb8YG-cSkfyp1Hq9bWJeBYkhQwGFskhGJnmP6Nnhdv5TnUD7Ni9hItKwH2qJtGbhSAK2sY04m_dXJ4Ox_EOO38qrMtOJBL39EetqJ8lemLSQ8GK8yixOih4-YktQsz7qiSIDzAnS22HPENezN5VlmdJjPoxM2vA35yKXg207JEAw67irntEWj_vx8tgwZmdkUOjChefPzlcOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇦🇷
ترامپ درباره مسی:
مسی به خوبی تحت مراقبت بود، و ناگهان او در سمت راست ایستاده بود در حالی که بازیکن بزرگ که او را تحت مراقبت قرار داده بود فقط آنجا ایستاده بود. مسی شوت زد، و آن پایان بازی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100692" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100691">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=Cu8UDe0RuOEmB1Z346Ocqnd3Js9z_EZDQOMCrNCA6Cjr14RNg68fPSzexK0UgKzqzDqKPe71qA8j1mtZ2PMypSaeB64yXE8NxsDXNp7UjNPFPRQIh0DTk3bKB-GdJfkW4G3Vc8La4_8u6V5fQ9v47gzmutl864oT6CLmN2GsyfQ4D5bYOaZ3sWRHHxaqBYe-K3OThN4WuvKf9K4ARXo5Nm9da3EMIBIjY55UgWoUgPuB33Lp9ZyoRlOaisi-WywD1m0Nf4yddCag_XjGGnjjGrIuCO8acT44JNJxQCn-u3jheJ7bdQMqrnP2t99w_APssM3r6QauIF8f4fkvPoUqKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f23fa81d.mp4?token=Cu8UDe0RuOEmB1Z346Ocqnd3Js9z_EZDQOMCrNCA6Cjr14RNg68fPSzexK0UgKzqzDqKPe71qA8j1mtZ2PMypSaeB64yXE8NxsDXNp7UjNPFPRQIh0DTk3bKB-GdJfkW4G3Vc8La4_8u6V5fQ9v47gzmutl864oT6CLmN2GsyfQ4D5bYOaZ3sWRHHxaqBYe-K3OThN4WuvKf9K4ARXo5Nm9da3EMIBIjY55UgWoUgPuB33Lp9ZyoRlOaisi-WywD1m0Nf4yddCag_XjGGnjjGrIuCO8acT44JNJxQCn-u3jheJ7bdQMqrnP2t99w_APssM3r6QauIF8f4fkvPoUqKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
🇵🇹
ترامپ درباره رونالدو: من رونالدو را شناختم، و او مرد بزرگی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/100691" target="_blank">📅 01:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100690">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqSmZRbOTGR5tpCFKRak-Wg0Se0Y2YRdwS7X9MHOwu4bIqdeX4C9JS3TFL8mnfJdnUvuOgKi2XGqY27KHpQpE-ONxDdPbc6CMSXru_K_jE-24mrfalbDA4mXgVYwEhVuTXZVPFpKtKUtWPXvo2PlPFJSeWHMIKGkbG07EOC9bFV8JJd3iwCIYwtNxT1yTHE3_ylgqpUGL_yRPEJnF1NHb7sczQiVTOT9c5UHvSHQglmwXO_4LzOGt60m6NLJNosr7fvwba_jugK-1XPT2y9w6SDBwIpB4SEPPYoD_fgueO2-CY7qj7ExjxzelyJzJOeCHwSscLrYW3aCZdTioPlKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوه اوه ترامپ و اینفانتینو نشست خبری گذاشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/100690" target="_blank">📅 01:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100689">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7JtrYDMgo6t_D9aIJsEOTVO82Z3RjqYdLaSjzZj6jENMdyaugVPeeKFZNPsomsEOtu3pPtnQfCBty0EWldkenDztI6kwsO_XvS2v4z777SSNqvaK-mFonZc_hncc3R4hOHWSDeKY9dvNlhTHdOcRzeM7bvm3dkiloeUjfHrCfhMrznZYIs4mQqlJzs_VRpdrVIt3NIEpDmxVp0k8EtYO8lZQgHaq-xEPRH915a4oQ4lHSqmJRP4wCew6oTKT-aGXhPJlUu9jl8-zD2RE1y5qfDkoY3ZOgpJtwGMw3uaRKH4616gRLUe2xfNRKAVqzJ4ixoDWBFTrzDF1WbMFO47Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🔥
رودری کاپیتان تیم‌ملی اسپانیا: لیونل‌مسی بهترین بازیکن تاریخ فوتبال است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100689" target="_blank">📅 01:10 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
