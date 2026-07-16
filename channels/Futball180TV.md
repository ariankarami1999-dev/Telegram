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
<img src="https://cdn5.telesco.pe/file/i5kruk9pXJTOKeHAEy3brOdrH8Ko6UcvZYbY0nh2Xe4PZM17ji6NGz-NGR16jvEwAF2qFqK9fxkuYy7gFHjlN23TPdwdXckqFB-kMsl4yIZqlzuo1tn32cApPLsUK4jyCMM96UxQycpHOtmV0CI0EWHIo6ksNrfL7jrqLWgaFvuSTx0O8vqOka9bw4hB58HIKsknftNO3ph-T-rtDPzvoouKgi4gAlEoouX61kmXm-K07uZy6YBXK2CG-gKRdgOjzrMbm9Gp3J3Az1wXvafUkoUouBpJk8yaAv4U-K8N-jVy_lwD7A20K5ppOsjkX1uM-62FzTR3sPDp7i0A9VAp2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 569K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 21:14:03</div>
<hr>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChVirtynu9SG24l__Ou31zwn9rKO6wmb2LEEYZzW15glAvOS-d7gl3Cs0nMRqWou84-U6uHhMpUaxBtHaepKJOljoLkaeg_Cj0D616fR7m83jPg5mD10MgtQgyxvLWDJ2P8i5si0iyjppMtP_IGzVsEpQw5yhOhCM8TwUy16gKyt0eM10Ej91QP6c_abLYuDqwys1hI0FjLSDI5kOWhISOF8kztBPNlXg2Sd6j6LTtCeTNoziKNKLsANAUPvfWxjPXZa-Vgt6_7pxn2HcDWQBfM0hXtFv8lbF-77aTzkTVx_DxT0fst-WRMYevvcUKVfmwvoUBLaQnr_7ENLmooTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKsxqecPzWq0ff2ISlxm217bMDD-N1Stu7KHDK1Ibd10PQMExUbj6opnP5CR0RNrrKxPRg3ffRhy7XVPhW4tlqCk-wqkXc0DuoJXh5hAxa5prufg11ScX59DxLUIwoOQtKH5E8KZ7AECPqL8z0vgDU4YSWi0FlLFjZBhJ5H5jPbCGsHf2KNT5x8Mzr5V_Wz-NQrDolwVN_tHZpuHfPYzT2SD1c9WjZHEAWInmPf68ECLrTsGxg3NKq4kuD3fmHxay4AeBrnXqAQYO7B2iE6Xr2rubFtlgzyQcfnBT3pEemdA-RdEptkteDQXIiMQ13H8xdEPN-hrGcH3aLbliadz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6JDy3hkKY_gwM3i0OYMLca4mHZabkJJLcTNsCEzyyxyZwHXwEbAea3fZeymR40TN_Ov7mfzZxAAaFkkUp-I9vFayLLMqngBRN2gHrwM8zpo5cjehjSpaJGCDtqUTqtJRSRCPM4yYC98dm3o6gBk1dt1CZLjJ1Yx4KimNmo-0wDX_NqIzqchgZ0CQo7pM1ZF4-a84vDdzGtHcDNQSJniETUJeWJqOhHmipe-GA-hEbZV8IYAHKm2kwayHCvaKXOiDRCifDZJl0-sFJE5e9TK3OgywkMXmh3zjAY4_cb9wGAaaplb8iCWuBJzpm4ursNHJPswDMxoF5Le1UuTaUvmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=pd3PeXtxeIF7g2Xaul2SfGynMMFuWx-t9OQf36PwmzW287PGZ8ktS35oFf4KR_klOSLVtmUIB_9A5U-tCWbGhjplPmCtORi53FZktUiHPRAsG2KeMV6g8s00E8tYZJuoGnw-m-q5t3zUGTN9UVsPCTDKaWRn7tQi70ZIackf_HVzhoo4g8-R0S7Ipcacf7a6iyZIzZwLQlhvaj-NPbhwFAhZV6XCESb84EDiPFq77gSCCR6zniWxttakADxh70LpzaQsEeGMlgoz-w1FIW7tXSnU9sHePgbbPgB08Ohiowi0GeieKHiCJRi_kjnKHC6vu8Z-9kC_tSvsYAvaEjqiJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=pd3PeXtxeIF7g2Xaul2SfGynMMFuWx-t9OQf36PwmzW287PGZ8ktS35oFf4KR_klOSLVtmUIB_9A5U-tCWbGhjplPmCtORi53FZktUiHPRAsG2KeMV6g8s00E8tYZJuoGnw-m-q5t3zUGTN9UVsPCTDKaWRn7tQi70ZIackf_HVzhoo4g8-R0S7Ipcacf7a6iyZIzZwLQlhvaj-NPbhwFAhZV6XCESb84EDiPFq77gSCCR6zniWxttakADxh70LpzaQsEeGMlgoz-w1FIW7tXSnU9sHePgbbPgB08Ohiowi0GeieKHiCJRi_kjnKHC6vu8Z-9kC_tSvsYAvaEjqiJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFQjvSx_g1kJY5aSN5MLaeHM1SvxQL7Ztwg8LLqvdMJ--hSwL4VC11kaXWrkyQHpJyOYH27nOKVfEPieaRv1FDydqqPK42qHm8sKgvRFn0X2UI8Qjr1qzaoFeUIIlzU8PNswI-S_Ho69E_Pwuflr8k6Tz-uIXkfiI1T6ijb9YK5Rq0NZsK808X5i0R9XJ4CqXGpZ76CeLzVXEsniHihBFNK5IR9kCwC9z_thrTlB7c-JW2CXjDZkV_VyJjnFqW4KHtf4Rg0-UxNPs0XY0BZibzkYMqKEgdDadMxNGAkpI8lu7MbsKRMCHvHNLObx7smbduOzb2-3ExCpaDiBSkCvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zetqpj2MR3DFGKyQ_rhFtzPdwvWiIs2B8e_FGOBCcZdK8qOH7BeoAarjjQk8qWCOKj2ROEix5SUxwHcSZFnQY_tiKnGxz7SYrDfWpNgbc-_nkxuh29gt_q4CziAWiiBkePDPyOzJuuhXicAxgUC4JgOR7ni0f-taUL-rJNYMxKl5qHKycWv5Ng9hF4ztmaeEcIX8FBY7lcuouOJjixh58eI47_0xSaSZy1fIZxe6RU9REWD6Svj3inSGGneXiiPYfp3K8C5uZBFjjaKeg-Lkvw-bFefy96q9jwZOA4aEAiuCsK9dGCrzAJhpJkPs79XPokWFFc0Fs3lorox8-HUjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=D64OC4vwH0sevomgTLlRf6y2Bi8QTrzMEzosdNdDOe3kwp3v1FJzX6ogCJnSIVSQuYXWDraQT7zbCiAmoH8V1UMMJrg2Hnvqs1n4ickiqeQ6FylqFB7NAv69_-jveOXRjGMe4DWtR_NnhRIijLIcb1_nBid1JR_10s8zumGJzmjRz-DmF-r33YjNELq1qcMUdntigz0YeOe5eXldEmCcTI-CiG_Gzhen2DvMkZxTlFzQLe6USmYqQzSIe8sxzPZERL1kfS1oxX3eZ09hCX-f5SGq6c16Yl1Kb1Uj11mb9Srz0bLrqJO47eO-AsMN0bY6d4y0LxhU1kke9zdV0acmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=D64OC4vwH0sevomgTLlRf6y2Bi8QTrzMEzosdNdDOe3kwp3v1FJzX6ogCJnSIVSQuYXWDraQT7zbCiAmoH8V1UMMJrg2Hnvqs1n4ickiqeQ6FylqFB7NAv69_-jveOXRjGMe4DWtR_NnhRIijLIcb1_nBid1JR_10s8zumGJzmjRz-DmF-r33YjNELq1qcMUdntigz0YeOe5eXldEmCcTI-CiG_Gzhen2DvMkZxTlFzQLe6USmYqQzSIe8sxzPZERL1kfS1oxX3eZ09hCX-f5SGq6c16Yl1Kb1Uj11mb9Srz0bLrqJO47eO-AsMN0bY6d4y0LxhU1kke9zdV0acmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGA6hZxMJ4gCXPIX2Dw1YD1cxz2BauKCxbAM13joTc-ghNzNP-5nEYDVIXjH5XDq7Sq16rZwra4jtuvWuZQ2xrnjl4AKJ83uvBZm7xRkx1gWbO5FwVVECgETpQ9eeDAZ9EoOhbvdvswN0_5MWhowfJseyuLOGKh9vCzyrLDskD0HUrHh6w9KEvPOFSS-kdh_TADhTLReacJKwpOppDDZMeGC4tkybuGJax7H8qyHnLow4r3NUnmYWNU4hlMxGifR7RT9ZwfGJtHhYWEHc2XxcHdgmr4StvkY4yJjCzw97I-pwCOwWCma8ri3-XcwGLENOeQsnbd-OMDYMMaiHUVZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2tZE_riwWByK8TkFDsLh5cEj1j83F86eJHwg01kla4BlGucp8JECexYkoYGOK6uoW1OT6RiZUDJ7wEfRKYA-TLVzWC5nNqwoSyzOvgoY_MuGNB3p_PqYs5PRCk1pxbFw59c5MjZvAsFZ8ICuR_O2HJbYnX45Z3rH_ybmzqxqDr0v8kmPL-J_LUIqc17C9AlnqQMTuhAZleC1ldC0h-v4Mi-7tmUKHuzUBiKtCqTmwuuMDQvFModH0wJTtT8QojpaNO2zxR0NSHcAUSHzX8gaSa9eYStXFknWU_07wm8Ol-Ap3nwLBQg1yMUO1QUgUeDFfqhq_QWthjASSW1mcFaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtXtGya4m1eMWt0GAKhKJYQIqtTjJCdnjmuF9PAXDaXqQ_HIenKJz0RhQXBkaamdZlVIAVyI5vCHf54pZBKt9dXjq0DX27FcsSiVjJvnPFp0mHgxTnkM9jq-fx8EXAZizSYefPoar278oBxd_k-xPyJiz3yNH_MrRvYkiBSgIHYUDEGAethYv-ChfiyWc7V2ohBFy1xMYWg9J4K-pqumKZSOI4g8jham-OLXOZ5nL6y5CUDbwf68EHL09lQXs8YfXfaAXQIJqPULtoevafEP2ISScOvNoNJxIbuIyO2pKFlu_-BnaVbk1GLn2Gdse3tx5n90eVD2yL3O6_AzTZUkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tikfnqILYDG7_iRclgxXy_MEk2HHsyxpH-XVNPnO_l2Ui074tG0sq_o3yc5X3WCFLE0vitIW1s4uXxrnhnwm3JNJMzVNMglxKfg55MOfU7VV2rUXBS9PfXodY-hvXgXCk9RxjDvIajwTiecHHZfnJhZGSao_BklEbR4oYWgGQyteilWuqxuxhwCAnvw2nJl3jTOjJDKNBcigUS4DwfjOZiKKjFew1n4Vqu51C1fbPkCo0iRG8bOfk0301I6TjCm8BgANvK-DrA-Zik8JHkAt6iBTUtohGOIogWYlLTUfjoZuhDIsBPNvOqZyWB-2iBiNovi0TIe9FpWQHiXXc_hqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcY61zCUdEp_9q9CrvIjhIsvEpNq30XUNdII92UOTnJG7iXmOQG2Pf4935clwtbvkxGyx0utwTUwpf6I5xTUFxJQZVtzZOZ2o8-tlzluogdgET1pCn6QH8orw1KRR3QfW4Yhf3L5NMoz3vPNW-Nvpe-730voD-xDtKp2F-0CEAHEoKjnDIHvrgPINDPbH8vWKQ9cJllmawoEdfSurDgv0DOYgUDwXWrV8p9A0KXmW79k0TLKvtfpa1ptJCSq0WsBMLJLl6hUW0tq_qRbZywCBijTFoWg_O6qaTjXoTkFo7PnwMEr7pp3JXS4NqGT_cn4bu9iUDk5pePhwZKLlS16Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfxpm_m-gN3F4BXnqx4gyR1r92cZqKIeH154NwPBJcCquIUfBbKAdwd5VWeWnjep_sTQjbWxxcBKtLNKm3o1yz7iSmQ-n9cCxa1p6mU7d0ug_6IBrCahw4QgVkgGG7wAPdnIr8kFMzPSekrluXWzzNufLQ4_kwFQCP3LUapM7PtyBxebaoEaY7jElmcQPkWIkbkJ09PhhDxZRxi5yji_OAhS01CYcKkILmUSUxGW92XMGjDeonZxX84TTh06uC7XzYFBXjQ152owmqsNZRwSCD6geDNpc2JLYqeCQAyxJZPcZrKIH1hHMd3Ks-Ub6Qz-gN5UEW6Hm0NKd8GVxAs45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhpMX2EmACN7MZ_wcp72EkPM2Hlz6lWjg3VS7xYGxnn4W_qXiDU23jHXMBN60VExTOIeBvpcURe6IbeAgSazTLeNrq2gEM-IrQ-PUFBwRnIo47aLdp70D5vukHahRitOHGzECOqZQDbVfqAlUmvpx9z485a_qQ6ZegTfOpFeKMMroXjLsFOmRaSHck8JGClSxYdBL_K3PNU27pTBvdhzGZKBaOqPRTH1pyI5l93xQovqIJfB05ogSeL5gQyH5YddVakpigLs_0tM-UtiTATbOC1co7t3d9pM9ZEe256vZneoerAuADg67TM89I0pRB4ODJIeryruUSyFVIZOtfb2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6P8D88h1e_ywTuh4UbXQl0IfKxaOV3ICgNj9HZMNa6vUrtLgEvcWrA-4XKjikI95cSbIOI3UxhEo130W9H7sCxIHj1sS0nkabkVPi-XLWDYx4gwxLt6I0H_phj0YYP1w9mdgYgdy00oUeMbBg4Th1Gf6LvyQGciFGdEm1YIuFf1UcdBulm1GcMHEzv1X08i6epvFD8i7oOfIQnr0Edjony9FrCacSx0F9vMeEyKqupitevpO3xQMk_2JIjfhoFucUpiSJiqCveP4xFM5YM4TBuG5hahgVx2OGBl2SVcNRM859sg3d-0iKhXGSFWIaAL0PRMBuU65LZKgIoihoyMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100510">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=eAwhfAIvS0kOZhJSW4A7Kz8ndrhv0jDTY4OeK1NuZvSKlNMd85_3I4i9Ir8M8kSnJJvxL-AOE3Qcy7HcLp4ft5aG8WgzIRz6cTfAwTrbon4hLp83nIGQGz4waFzAg0OePy9qp9Y2fdydPcGIiRZel3rfIM_11Fu3b0LeSVeDq3mtO5CJLxI60bhLHj8GqZHWVcfb_vGAL-zziDLTsJ6z_mDC8ARr2A19omwKlysoDVtwndrhYjX7YS2EFVBSftB_zRR6ps2t0fGGNFUYt0_K3NVAEtgK-Kh9aEnb2iAtKT_t3GzJthem1UG-_yjH9NzzJ4EQMa5GTx53cxYWkkA31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=eAwhfAIvS0kOZhJSW4A7Kz8ndrhv0jDTY4OeK1NuZvSKlNMd85_3I4i9Ir8M8kSnJJvxL-AOE3Qcy7HcLp4ft5aG8WgzIRz6cTfAwTrbon4hLp83nIGQGz4waFzAg0OePy9qp9Y2fdydPcGIiRZel3rfIM_11Fu3b0LeSVeDq3mtO5CJLxI60bhLHj8GqZHWVcfb_vGAL-zziDLTsJ6z_mDC8ARr2A19omwKlysoDVtwndrhYjX7YS2EFVBSftB_zRR6ps2t0fGGNFUYt0_K3NVAEtgK-Kh9aEnb2iAtKT_t3GzJthem1UG-_yjH9NzzJ4EQMa5GTx53cxYWkkA31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از کجا به کجا رسیدیم واقعا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100510" target="_blank">📅 18:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=NZQXG2ZHOal4_d3CkUfrSzUVIAbiqxjVhjNebSKd0VDy9pmLWisvaLrCkd3nmZKpA2Dcnp2GX-2hxKP5Iey1VueuotBjGirfeLeh1xLUJ3y18RLDfm5UlurHIXgJchdneecsABCbhtJdslpUhOQ7EgxZN9OupIeySgtocsGV3uVlpzUqE-0r4sWqrXvNDzx-RDWckPiwHQJyXc4vkLudX69Fr_AYhZAEHE6nPOw4drFRIsYCEQ_KekBpI4M3TS0gux0v2aXvGsgwSVyYpJQ3ktDV7_umfqyDPFDKg14Pyk_cnPwry7gVX5rS7Husk_a_KuW89bIiDIn1vOJF20u5mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=NZQXG2ZHOal4_d3CkUfrSzUVIAbiqxjVhjNebSKd0VDy9pmLWisvaLrCkd3nmZKpA2Dcnp2GX-2hxKP5Iey1VueuotBjGirfeLeh1xLUJ3y18RLDfm5UlurHIXgJchdneecsABCbhtJdslpUhOQ7EgxZN9OupIeySgtocsGV3uVlpzUqE-0r4sWqrXvNDzx-RDWckPiwHQJyXc4vkLudX69Fr_AYhZAEHE6nPOw4drFRIsYCEQ_KekBpI4M3TS0gux0v2aXvGsgwSVyYpJQ3ktDV7_umfqyDPFDKg14Pyk_cnPwry7gVX5rS7Husk_a_KuW89bIiDIn1vOJF20u5mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66BdoEzW2YZ8RXjTCZ1O8LIhTJ9cPlqcvIN49gv8ldUBDhWA4ZMe71jvzEBj3GJuBnZ-6W1dsrjFofNFvOsTgBW4a6vzCAfkkU0N5TKjbpbDjWeUJCq5lEw7zRhgyBsIr9qrqEFDwfWMNrasPat4AhpRm_ZO077Sfw-NuBgnc0FVxeJ17QzwxjNcD-m-VPMQzS6XNUkZVWbvj0fEtMc59_JSJBXId1bE_sRLaBpkNsk6i8V0qB5iQ2__XXQ_AnbQWxF5A5OtaVO9Dl5TkauTgA84GtXZGC968V4yfXAKhkI6Mi5-0GVfihxxjQNr-sZkwppIr0BPgQcjPbC_hhjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlPUFoZLOGzXhPfEgL911uGYR2kTNrz72fM2LrXh1HjUuwYawbya9Zy3cwu3TqU4yQyw1hrrD_Vb6fIYhy0NgQSo92nw5G3tOImIVKzgTL1q8d9YibYKZ7iyd1VVrkN-FEquz9KHcLBhhFCLFwWajM2vIRCRMEfFB3H8Z3rfYZ_yVHwlxbvf2ypDWD-E2jqr9FBTW6auJcQKGGqLPep1mpQoUq35Qv6bMJuHP4IDkiAb-zqJCnYRb3pIm3TStVE5NBng40ATBrMtTL4Qh8fWIngqcroZdAY0P3F9N7jg974sCkcoPU1IcdutWk4MQPuD50L_kk683B-3lr8DvpfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLgHvIcjW3v5cxBrPfeOEQbc1MubyAHwBEH0h3-eEbdBkbBiLjMnZK9uh3aLTB4EneklySr7DQRXll9lo9m30Fjb2Dkqo_3nVwu-oZ-ArAlzZKWHJzZ8qAmwlCty9UmE3Gpi5wkUow-Pbm8uOqE4Sq_pYBd4Q3Yjvo-Cli_68CjOQ166rgz6Dm4gpyR8nXta_iZz94upXci4A4pewMxg30_lX3N11P4fzpVOKWkolZjNz4kzipL3pdcU5y8QjMiSvaLOf-A2oqEFgr9Fm2Bb2Ane2ws9WkSbX6kYdxQZzkMzRB6kebP0zpEuxAAgvzZTEZZtr7WeIbLtGoshrwAz-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvD1o_L6-OC_3pt6tiNxH32dSMxcW83AjIz9HFTn1qeu1bxq6B3qDxy_4pa2WQ2-GlaYtrWhCMF47Xn_7ZklF4OAIXIt8rCA1Xb7DcGlIoHobzrGTpP546ufW9Q2TUoKz9hMogq23I4UxwrXX7PNBBkzd9dWqf-XZDr43e1lLbmre45fAD3JEfkxA-Gx5wsHUDjXKgQvM12ZsZ8B9sKnaTKhQYnGgSrbCeMaamuW43an8l3yfTtGUDynDidX0Y5-s0ELsVnIAYEe1bC5asW7tbciavaq1-OeZBrOIqVQk5XB37UEgSCQcBaPRaGGGCfu-RxQOR2jfQQk7yXN8mZzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxErwStoKTi15Z9NPKM96b8ln3BuOsTtnyIQiK1MEuMGVPcpaLT4lAE0gM0AewfVhdda7-wUCpesGI_z_T1havWwoUbiSXh4ZJD_5a3fCmvD_VOycP5HPyxhRsgHTJlQbHF_nWt8yzw71HcgJIe9yZpb5x54X2b-f4uh8EQLuU_NCTtodVjBihjfB6cbcShOUsaP-_WlxKMJfPuyHTSXYmarozgh7I98vOl6qcTLxf_WdBu88cemokmdmEXsPR9pMZn-fWVMZJPTv0ssAJ8R3y_JF22T0DWJeGs8aPMaDYTJgIaE96KfwIMpsgykJvc3fDhT5b0fSAgtUr0hpeNE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N92zQns_P9Ro-c8n1xGcyRTq7k6Eb6uxJ7jb9vdhnSaT8RrlgCAiFS36u0K3y1fkysM-evd5pj3MOGamQBZsP76g0AHdv3KP9laorkQ-HZZLLad-97O05RLl3dlZ0RseN72nEMHi0iCOxG9HE2TQte93FYYR2fSkllK96CYyaXXoQ2K3fBgd31ayntmwZs31fAEB3ojQA5g3tfUquFnW0M1YW3UJ1-ks8gFNUBvUTPUlS6H9GGVc8VHkjP5A6QvYE_uxI7Unpt167u5rqje3p8ylPDK6xwRlWa7-rVOU_qJSbdPY0RFLVNgsAn2ot_iJVVAc1PHzaNBYB4EPG4hTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd1G_fIKc3AuegYTEV5r8-mWnNaXj7LF459qAWhs4Gf28UVTpjwMM3FjFNeN51CjTv_INvYJ1dDy2qmi1D8C_QCrxZziPdBSJarxhLwMdMzAJMom42rxKWRnzDM63RUauuZhpq5ENc7oonyKNsURU0tv_z49fp11sPqEC-KWZx0xsa02xnp7uYAthHJ9C4FXYB2OoKL_UbCPkEpA0uReqZbqAgiw8rveDRN65WS3z60B0mTPRFzCA_Rm8GEuzKh3a1MDrisu_zrWtx5sgHn4Kb2eXG3cNM7bS_XiGVMegNSzFbMQe_GxiIkEsdIaxUtbngvTUL_kXL-xW1SSSPW0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZdyhRScUn2A513_RPvtabk8iZmhrNZJJwOjrfu5r4qhJ3eZhZh7bP9tNYQF5sDBstCiDcN_1aN4Ho3CddsOi1vo_3ZNCuE1c55YWzlb1XRLbLHJMPxZ7e2amdLkNwgTpI5TUqxrPAiRWIis2P9q4AZv_q7N4XTkFArZstx6h8yodhnyj6pjbnkAoFy0NzhOOtbaKXviuFS10E5hRWUenwwaZi3iupICNavDcxaDx7mSxiVIRZXcKuIMqHevRcqk0mOZbKW8YyUw7nYlOxVuRBw13OxtamgbxxVRRc0CohqihkB867IUnm6yRm0lCVGkFxOxaHgqa8R_MeJOo_ldZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYN5nsVCu8LBNJCHW5FzG-8cXpIVWAJEHtX20C7uGm3XsAqTodJiCkdzDqS3clvo7OQKqfMPGSblskCZ5xNyKgbygPlClEztDlNG39dndHLNPzDmaOO3X5f_mtRBAAB8ImyrNlgnXpBagU2ayVXhqKLs0VDleTH7hPl0qZFcFLmzHv435MS-xNbWaAf5RziRk8VUhZZLfWXeca9V3Yhw_BCXHRUOVSQRnjwtPYmfvHM-p9ya8JLtLKSlnYRrw21L6MhOMw0Pflh3e9Pta-P1UV31T3lzK4F_6_liDlVtdMUOZnykYaSg9A-PnPLQ8xPSiwU5eZ0OkQpIl6D-QQBPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏆
مالکیت توپ دو تیم آرژانتین و انگلیس بعد گلی که گوردون زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100489" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100488">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/100488" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100487">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100487" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100486">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لیونل‌مسی به فینال جام‌جهانی بازگشته‌است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100486" target="_blank">📅 15:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100485">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مردم لندن درحال تماشای حذف انگلیس از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/100485" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100484">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
جمعیت پشم‌ریزون در بوئنوس آیرس آرژانتین هنگام صعود این کشور به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/100484" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فریادهای رومرو بر سر بلینگهام بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنچه در بازی دیشب اتفاق افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-I5MCyBozQRxvYuknNE-ct5ewx027CXlmiyiNvclzLco43GyAa2LvJZKPeAygOG4Y4OaeaJfmxcwUFoBADEHTVjlIijp5DqWLj5dLr7JzSJMfYk8Cuu6hVQyZiYTXmAJdRSQY-u1c2_YwS5aWB6HZqxWmLSMZaRUPhC-UJT_svUePUf8Jb-QUG1wIqVHXueVfLvsEOZbti8oMEvfBFvqXau9iB4WF3DiP2xMgi3PZ6Fw3i0n6uUwfioqkUkH-kgx7N9zV-F-pLDPt5rwt8wWkUYD7Y5tqq4SURu0TmE_sRhuPPgsbIVDrEhIpiuT7vMKfL6vqhRWdRDRE2mw3OZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100480">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇦🇷
سوپرگل انزو فرناندز مقابل انگلیس از از نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100480" target="_blank">📅 13:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100479">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=t_IMJlK5t6ZGQi9n7drXvYdURA4MgcAO4Kif7T4DR2Wi8AIVE7ad_P-vvEVYy3uViFGmIkDwzzJUALoDq0aBSgrMnX2l4Fg0kh-1tt2XhttdwiniaNivlYyJCs3G3xNR_ek0adKGXCuc-1jfxIvAzW22iUJXIv-sS5Ydpg4l5j2St9QvgQizWpmlYoxFlvja7ir9FtJNoWDpFkot4pTE-kAXkiLiLm90ahN7EDO2OMpdwHA8Uj1XfibZLowOLrq1enCaDCXF8kY-40PWcAwH1ejdtsm2_UIASnXczHFXYVKSZeNbs9P0MMKB3YVtTw_w89BU1I4vmpT2_ze_MF-N6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=t_IMJlK5t6ZGQi9n7drXvYdURA4MgcAO4Kif7T4DR2Wi8AIVE7ad_P-vvEVYy3uViFGmIkDwzzJUALoDq0aBSgrMnX2l4Fg0kh-1tt2XhttdwiniaNivlYyJCs3G3xNR_ek0adKGXCuc-1jfxIvAzW22iUJXIv-sS5Ydpg4l5j2St9QvgQizWpmlYoxFlvja7ir9FtJNoWDpFkot4pTE-kAXkiLiLm90ahN7EDO2OMpdwHA8Uj1XfibZLowOLrq1enCaDCXF8kY-40PWcAwH1ejdtsm2_UIASnXczHFXYVKSZeNbs9P0MMKB3YVtTw_w89BU1I4vmpT2_ze_MF-N6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب تیم‌ملی آرژانتین
🔥
👀
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100479" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100478">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کریستین رومرو: امیدوارم وقتی بازنشسته میشوم مثل گری نویل احمق نباشم و از بازیکنان انتقاد نکنم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/100478" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100477">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U54Dih8fr03Yj8tRyiczh56x1n9Uw4jfhCch4JjFZrnAR8lBD4FWEMUqyvAkHHcWxJybbGA5ncBXfLkubF6gn9jSuOdmtFvX3j3JVTufQKkduo-GDSFoLILBcuYaCQMpbZPhwBBZRvPC74g2UzF46_MqXjkTsIQj7vcytl5L2jr6nLeR9_lrN8KLdDPC2N_4FJtWsnRu3EavuM7kx7H-798Fd_0KHlQlYf7DdTo0Ke6-ShMXfYpbgNGqNNt6odB25GyZWXVdEVXss3mAVeyJTPEb8Sfn_NcyHhJWY9Cy0QH8q9GL1QO7YsF7vtIPYPrUe7StMDVXSxY9fqHS7hxteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دو سال پیش در چنین روزی کیلیان امباپه به عنوان بازیکن جدید رئال مادرید معرفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100477" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100476">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3896b54423.mp4?token=Hcb9kKkZagFJ0mHmFumVztLPuuWp5fvtdm_XZ2MQEixvJ1K50xba6_DksP5meKacNIkQMFuSxUyRE-4OqeR5BBl7bxFCMXuGA6shkvNEe2aCtrN5TtQiHHGROLjBH5_7oPsq3Td0Qz4LGDVhS2Bx3v5gOPx4L7DD0sVtSeCfi1HnJ-EVesnV6CgMi8rshtlo8R2WMpAfOhjon3zdo0XjqctvJz4U72-DTf-s5xX6BWTB4HZSd1s4jr_6-LH0U5nozns1TK5avMySX8RlyeFJPFCsL8S2jtEjuVrZZAhfcSbD0A160Bkyz-Zpew3cRLjV1BZSWBu7xzfmiPifU4rn3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3896b54423.mp4?token=Hcb9kKkZagFJ0mHmFumVztLPuuWp5fvtdm_XZ2MQEixvJ1K50xba6_DksP5meKacNIkQMFuSxUyRE-4OqeR5BBl7bxFCMXuGA6shkvNEe2aCtrN5TtQiHHGROLjBH5_7oPsq3Td0Qz4LGDVhS2Bx3v5gOPx4L7DD0sVtSeCfi1HnJ-EVesnV6CgMi8rshtlo8R2WMpAfOhjon3zdo0XjqctvJz4U72-DTf-s5xX6BWTB4HZSd1s4jr_6-LH0U5nozns1TK5avMySX8RlyeFJPFCsL8S2jtEjuVrZZAhfcSbD0A160Bkyz-Zpew3cRLjV1BZSWBu7xzfmiPifU4rn3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
توصیف عادل فردوسی‌پور از کامبک آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/100476" target="_blank">📅 13:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100475">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876233c65c.mp4?token=ZK34Dfx2U9QKLolPyJ6107n1WrTxHDJsOQW_pe9aJdssUR0C9StrSncCeZeM_8W64A5RMHFXGreOpl2WG891Q1c-F6pu0sec9o3xWpIpEtS9mx9zdC0I34p_Mr9qD8KmgLrGZFf1pcap5eJBPJVDGJIPip-MHu6EciH0qZmGTcmY4DIzplT0Lj7Aj2j2Bt0FMmhSxeIT_y80i4u1LGWU_dfNu9kyHL8oLPxWG1Z87ojojzHX4pBZHjc0epLD1oYM3CvGoT0q1L-xXTxgRVDOWTLm9kBnkTi0Svt5Q-2xkXx-WRNIM464pW8FP9DWvr-DQPaKLUZfB_uyWUcCC4axsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876233c65c.mp4?token=ZK34Dfx2U9QKLolPyJ6107n1WrTxHDJsOQW_pe9aJdssUR0C9StrSncCeZeM_8W64A5RMHFXGreOpl2WG891Q1c-F6pu0sec9o3xWpIpEtS9mx9zdC0I34p_Mr9qD8KmgLrGZFf1pcap5eJBPJVDGJIPip-MHu6EciH0qZmGTcmY4DIzplT0Lj7Aj2j2Bt0FMmhSxeIT_y80i4u1LGWU_dfNu9kyHL8oLPxWG1Z87ojojzHX4pBZHjc0epLD1oYM3CvGoT0q1L-xXTxgRVDOWTLm9kBnkTi0Svt5Q-2xkXx-WRNIM464pW8FP9DWvr-DQPaKLUZfB_uyWUcCC4axsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
گل‌دوم آرژانتینی‌ها از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100475" target="_blank">📅 12:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100474">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=XsYICfvdLvb8HE_8peHGArurZsUZzKou-VtJPj0d0TWq1xyPk2lmh95BiOgI3Cfthc-5lqH-C79oWSFIu5nHuG51-n5gReEfYgmb4f_0hyAO8FM-aKvmoyOSaGXvV10rlhPO563hevqTv535KkxiiVE12qkXNbKqVyosecwkBlsIHq0IrxRvuYYD-Vf3RUDo4q-nzRvqffgDs0CCN8vI7zc_g1JRWTkTk7IoQpjV4KLxS7oNKkmMtkNpNORmXZl_pNj65tQlw6rckBr5LAFEyFgNDO-t-yZR2WMyJBLw_J4pzslQikUSp47EkSNmo8y18rgqI2qw0yqKofAjjbrskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=XsYICfvdLvb8HE_8peHGArurZsUZzKou-VtJPj0d0TWq1xyPk2lmh95BiOgI3Cfthc-5lqH-C79oWSFIu5nHuG51-n5gReEfYgmb4f_0hyAO8FM-aKvmoyOSaGXvV10rlhPO563hevqTv535KkxiiVE12qkXNbKqVyosecwkBlsIHq0IrxRvuYYD-Vf3RUDo4q-nzRvqffgDs0CCN8vI7zc_g1JRWTkTk7IoQpjV4KLxS7oNKkmMtkNpNORmXZl_pNj65tQlw6rckBr5LAFEyFgNDO-t-yZR2WMyJBLw_J4pzslQikUSp47EkSNmo8y18rgqI2qw0yqKofAjjbrskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
پست جالب باشگاه اینتر برای لائوتارو
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100474" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100473">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M63EL4ssOxM9XwjFfl3wP4V76LNz9EaQV901tuyVeQWEBW-Vj2UCxsCBXfWVeSkJQWrzs8chFurhRQi9bvykMGRRB54M7HFLGKn2q03xipP7bQOqc1FYaSzuzCppAl2U3MQq2Y820VDGTlTEoTGPH14lsHun_VeXfP_iqUjtE9XuKOnMbxQ5q10TScUSJYi3bIYRlR1uGsPWKzKrT11D0QYIj3mFopPCgH4r1BBu0FAMWikfkN8RQsOwldmZFXY_7_xNvUhWwjqliZh1u8vjqCwtK5c5OO4fRmP59XsC1WaETcI8M_xSNsiOGuMkT3bZSFj0iY3x0QGDp-0_77MENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب نیمه‌نهایی جام‌جهانی؛ خط دفاع کاملا اسپانیایی و حمله آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/100473" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4QbAhNQTNzD4BYDpcS9K9BF7hOwVdOoMDsZ7iUJRAg-G7mUjdQRVR96X8DQD-yFAwc_Ntqt2nqWqjIfeDwJa7U8iJmakal8Eb3C5JqXj5O-fZWgTeXQPGlEhFeLm4ghqwoyFUqaySfKZdM_Pzlj9eciJupOLCIUC8qUahUof55tNlrFu1yvcpN22TKb9GklF6jAS7BukPg6wPHD56Cl3bv3m3xiknnSozwvtCqIcKBwaYjvDM7GlF8RoBLxWC6lRc4qg0tV--Qg3b-_Pti3DuAyz7dtckVziKmXOP73CktxzPW0RaLIxEjU0LN7QFB4AFOETyywzQPpeQd0wnUczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nYaIKm8E5-Gj4vgEw1bX46IZTA5GoHpd24Vi2f4fjC0X_qxHA4yTKFrVh3VXE0mfcOnnDJTGhZgtf_j8fPSmuUuf9PTm69SWhBEsTNH28Obb1j2i-gcsuvtd61kjx1OE3l6SMg1mBU_WrXxxstRxP5bmxq4ITa_Ctiw8_zfqk1RjP1nwY-5Iz_9E-N4KUTG0orVTw04wrQcywoQ-TD6U32JpDObbv-2beOda4M8Uh0U56Cqd9f8XJ7mFS_cT0gTR6mXxLlxY4wRI7WQ21Xto8NIII8fN1VB-f4G28AUnvESNua0alXV0kIfs1LCZtLfX2bT27VXNcUUKSuxGMK4gaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUt3LGRUuEUK_jsg-33v8CRFUTUA68HGFLLFBZOT4q0Qh5pej5iTS6co8p4LzAWjXDv6A8MwwJ1XIHZ9wOLGMN_hB2Y1dbhVKu_8olt_bmUoxla5Gj0ZIXNYCLCMP7bplKgX5ztHHXYd9QdQHATdtphWpUMNgDE23TtNynAk7SfuTSDPydzie7LBuX7LUh6JGcGepO0o0Fn0bGk6jcBGwisdrnS30DiOyAwp2gFzPjCDyQzcfsSSDciErQQd14mP53PwUr1teYqunA30HJcXi6CH8Hui9CnB9hwZbv9gkm8C0sU1lKnu0EJt7Rm2q6a71izwk43DtSUetwXyHETtEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
📊
مقایسه قدی سه‌بازیکن مدافع انگلیس در دقایق پایانی بازی‌دیشب با لائوتارو مارتینز که نشون میده قد دراز همیشه ملاک موفقیت در نبرد هوایی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100470" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100465">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DoIZj75agkj7Ap5qJp2Og7DShaYMODqTUsDfHbaYIJnQEqhbjGpaR-4kIwA-lMGOtTKiblvOkNw8opPKp0Y2cZjCL7GSL1I4jfyTn0qW9HfH2FdsLsfF-FPihPHD2l5bDTzAoOA5dtQ6ADNpi-ACT0r3Od3du2Rv5OHS4ClO66xCzBcT8o3fvY1a-9LonDPFnQ2aRDMoLmCOcMvUc1iafFzLr1ugDEEApkEWMcgK-dvVZMlKAmRiGkUmiTIijn0rPR6e0NOs7v_12OIn--xXv4gmjyxFXrdgDzpPaNlPOO3xlz5fLmFWWP8iiAmUMtofbnqfsPYx24VZSRePIvFqUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uG4M42J0R5rE1GTnW935sHW1OGlutr27R96V4G0z8v8MYdxWwUDv_POdnqIhaDIGrVsg568fMr1yhipoOkWrpdMrsIxotJg8stfqP4cqcRhMyrak_uDzXEJNxa5zX7XGGTKJvO2SXg5Hbhv6GODMFll4djt5hBWhwbjihC9e7Fya79Hpdsjn8n0c8TZs6xE5t06Qoan3ljtntP0qTaZU_AByn79uMMVQXn1iMKYv__WnM9-2MVU5O6R1VbS8fyhZ1h8fuzHLYOWmJDzuA2Djjcyg37OEEgb3nXzNQA2-TSv3jb4001SxkH9rZxhhIehsBAceLrIvnk13YJ3kpsFBQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aTUkSiKxfLI58-m3FjL5XdoB-gbPnztuSprG9OxoVoA2w9_PdDa1v_GZqd4uZCv8NBjwBLgcWKwKGDzfJOl_PR1sL85_CRjNcchyz0Mbe6E_5sLbptrHx7kVE-Soa-nOAmMPBM1Sp3ogpLPcF6U3kf0_EM0CgB8q8lB-gC3M08ZWHF0Q5AdRdYSizbn6yedFMCAf35g4cjFMkBrg38j_GMINrGLtAYvaRlz-IwMf-r6w6eu1rFt52oVejH83cLOccaebEwJQQRb5CxS85SmmmL1NMs_I7TDSvGpAsF-1lMqCWbY9skcrGzgBcgINyjXLjrG6H9LCwDRu7vCdhTnlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHXczvbUgH3i35Qy8PN9dpgoHEfFrontLjefBYxKfM2bsRDifpI0rUZRv6WA_3QzqqZkzS7h-pBCKG4c2secwuebmUgxF9Erx9c7W_QH1Cyvzxp5zYuJZArq--X-9is-wDd8TlY-VKRGwUPZpQnXeE_Yuvy8XS7Ckg3-I748Ye3Gd47SXP5lcmvMr9vdysaR1lO6LGIlpPh5e3L-S83JTwEAPyQEV1wSSMkkPWAvKqQJG95IxM_D09gudTbZ9e9RKSqdsHs5gbiBSCIbZRBplhmN3MDNYMhRdUGECbDKWX15Imo3GAa1EfCkQDpfe9JEtJSvMNXW3IaVL2HKuNBwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwDOoZ2voVeg_hT8hFx5qqN0gcWD-eaGyHWcZ-3XMmCHY1Gd2g0ka1mj-DJtWh0bUgqZW76wI6JsTiRyKuf3bpL0Aah8QCOSG5tHL0FCFDYxBxXaWaUirtlx0koA3Uez4Vni9Wpt7Vyb4SHc7Vf4m-di54d6jxYfntaR8_OriMs82boYScqhh2l6a8x0qlu_IcyiEhxDsPRKKO7YG82QB0dXkBAi28kbMe2b4Ps02FP7Izrwrvy4k6GGDj9QJC95E_l4CR_IM0fnIDSzWhwVOUEd0t1dpCdwOie8qCbU6ddehn9djiX59S0jA5QO3QWaoeBsJJPrsmobWZI9BuWpLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🙂
اگه یه روزی بعد دیدن این عکسا میگفتیم مسی قراره با همین بچهاا فینال جام‌جهانی بازی کنه بهمون میگفتن کسخل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100465" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100464">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=ECkfQd84b7Qy4tTTYb2UQH9FKXPg3Pk2zLi71KCuUZxGUOQ3Mi6Obi-R0GGv0QlmVgFNbBzDpxlMSGeVLMJjOdCzhzifVy4DtdQaasIWEBaBzR77aLcjgX43a9pxNtN1J5AqkOppX9-lPbuUjFEbUmeGwZ3WycOGEozUeMMBGYRGaq05zackAYt5aatvmIm8A1MQinE2r15zZkUpZ0X7epLIfPHI8yC-gYFniIDRCdeNl05dzTcC2G3C9pA8goy-nZ-UAUXha4aZ-g59Ix9PhQzu62y3GsYFmjwjY14it2BcOMsGIeElbE0XdrLLEfvQtURtHwXwyCltoQ-VUd-NmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=ECkfQd84b7Qy4tTTYb2UQH9FKXPg3Pk2zLi71KCuUZxGUOQ3Mi6Obi-R0GGv0QlmVgFNbBzDpxlMSGeVLMJjOdCzhzifVy4DtdQaasIWEBaBzR77aLcjgX43a9pxNtN1J5AqkOppX9-lPbuUjFEbUmeGwZ3WycOGEozUeMMBGYRGaq05zackAYt5aatvmIm8A1MQinE2r15zZkUpZ0X7epLIfPHI8yC-gYFniIDRCdeNl05dzTcC2G3C9pA8goy-nZ-UAUXha4aZ-g59Ix9PhQzu62y3GsYFmjwjY14it2BcOMsGIeElbE0XdrLLEfvQtURtHwXwyCltoQ-VUd-NmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه‌های فیروز کریمی به قلعه‌نویی: تا الان سه تا تیم تو جام‌جهانی نباختن که دوتاشون فینالیست شدن و یکیش ایران بود. این برای ما افتخار بزرگیه و باید جشن بگیریم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100464" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100463">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=NYTMbZoa6l5sf0P3FGpajUqFSTfOqe-vzbuuumVWY-FaIy5pv_B4HXq3msaTHDgK4JoogBFvOAyfsISevZ5Y4Q3qSlF65-GD-0vVLLcE_CNu3d4fPuAsK2wVWeaPUXq0taE9Pc4V3jsHD6h8kSEcIBlPkNqF8bL4ZbT2T7XTgH0DlGdHftbuhQZ7esPE2qHeafPa_8T2veAujKI8pDVon-vYJz9hnz2RCo2IvysjYxpJrUkUpcQy0Q-ywMtlFe9dwdZDm6OgYsCyjryTrzZynIlHoKH76mBJVVTaYTaeOcFDhJL0pvR7C1ER62iBWgDZu4hdyaVHNZB4TmeAXUo5jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=NYTMbZoa6l5sf0P3FGpajUqFSTfOqe-vzbuuumVWY-FaIy5pv_B4HXq3msaTHDgK4JoogBFvOAyfsISevZ5Y4Q3qSlF65-GD-0vVLLcE_CNu3d4fPuAsK2wVWeaPUXq0taE9Pc4V3jsHD6h8kSEcIBlPkNqF8bL4ZbT2T7XTgH0DlGdHftbuhQZ7esPE2qHeafPa_8T2veAujKI8pDVon-vYJz9hnz2RCo2IvysjYxpJrUkUpcQy0Q-ywMtlFe9dwdZDm6OgYsCyjryTrzZynIlHoKH76mBJVVTaYTaeOcFDhJL0pvR7C1ER62iBWgDZu4hdyaVHNZB4TmeAXUo5jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
😍
بغض و اشک‌های جولیانو سیمئونه‌ وقتی دیشب راجب لیونل‌مسی صحبت می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100463" target="_blank">📅 11:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100462">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=nYvlNq8nyNmcxS8DdLAlow2-FrjCA2iVjbbCwTh0rndo4Epuel3_v3pZpxEhDV9NBc9K5HDCR_-DhFJxdBY9GOMOZ9KYoGrOoTWaPWuX8hUzHiX25B9PBSK-2c59LeHhGRcTtLyUdDGeoHloern08Eo1eIOMoEuGYFhHnDwnwyyV3OzjKyUFQgiIyAUnabO31TTOvGyqEmVz148O_QdlbQJCKisMvLYChR4OicibfMVTlvpzLrhDC4y21bdWZPYY6iKMC3rZ4fYNFffKo4yJkF8U2Jd97PJAoPgTVH5jVFOrF2y_L9myzECBADQmWa53JV8sdiDwoRxYQueEzFP3PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=nYvlNq8nyNmcxS8DdLAlow2-FrjCA2iVjbbCwTh0rndo4Epuel3_v3pZpxEhDV9NBc9K5HDCR_-DhFJxdBY9GOMOZ9KYoGrOoTWaPWuX8hUzHiX25B9PBSK-2c59LeHhGRcTtLyUdDGeoHloern08Eo1eIOMoEuGYFhHnDwnwyyV3OzjKyUFQgiIyAUnabO31TTOvGyqEmVz148O_QdlbQJCKisMvLYChR4OicibfMVTlvpzLrhDC4y21bdWZPYY6iKMC3rZ4fYNFffKo4yJkF8U2Jd97PJAoPgTVH5jVFOrF2y_L9myzECBADQmWa53JV8sdiDwoRxYQueEzFP3PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
لیونل اسکالونی در تمجید از مسی: "اون دیگه چیکار باید می‌کرد تا ثابت کنه بهترین فوتبالیست تاریخه؟ واقعاً دیگه هیچ شک و تردیدی وجود نداره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100462" target="_blank">📅 11:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100461">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=PevvDllHXZS6JuJglpCgveEaNltgFN_SAP9Rdk63Rdee4gn5qO9Fkr1qAYtwxrLMbKQfFruuHY5lXAHU2Tflu8aRlpBcZKr4Lr1xskVIveRjArF-9Dvvqb1nFJ1u5bLFA_vMKzhFxgLy7JgREN8J6y8qZ7ITiF5ZqOQXLzIyblgwgz61R41NVaohJE7ZyXsWuEkbBnxwO7HeUQiRqsxLbkwhFOgch8YP8XQOpJKlIoc7WsvpZkERGliU3wh2i_z28FEa_fkmPw572soeePnWinNI8Z0Z8xBU6b2YohKgrFhbLe10oPfYm2HsYXSltzGJbPC22KjtObkOFK4Hsa8YRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=PevvDllHXZS6JuJglpCgveEaNltgFN_SAP9Rdk63Rdee4gn5qO9Fkr1qAYtwxrLMbKQfFruuHY5lXAHU2Tflu8aRlpBcZKr4Lr1xskVIveRjArF-9Dvvqb1nFJ1u5bLFA_vMKzhFxgLy7JgREN8J6y8qZ7ITiF5ZqOQXLzIyblgwgz61R41NVaohJE7ZyXsWuEkbBnxwO7HeUQiRqsxLbkwhFOgch8YP8XQOpJKlIoc7WsvpZkERGliU3wh2i_z28FEa_fkmPw572soeePnWinNI8Z0Z8xBU6b2YohKgrFhbLe10oPfYm2HsYXSltzGJbPC22KjtObkOFK4Hsa8YRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
بطری تقلب پیکفورد که دیشب دست بازیکنای آرژانتین افتاد و حسابی سوژه خنده شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100461" target="_blank">📅 11:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100460">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔥
🇦🇷
جو فوق‌العاده رختکن آرژانتین که نشون میده با نهایت اتحاد و شایستگی فینالیست شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100460" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100459">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
⚠️
زد و خورد طرفداران انگلیس و آرژانتین بعد از بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/100459" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100458">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=Xu0VSQ1vjVoSF8Gn0TRu21c99oOxLj3ShohHTAxSPDd4mGX-FkfTKJA4vnsCHV5w-W9RMopC-Pc13pSyl2Cn9ZCuUnOzGAWJheb3V5g-8nK5P4ik5surmKoCTD6FS4hndFMmfDz6cFp7PYNNQcZJNUQezDmtgpYRmnp1HObthbqnburJcEIIu0ANHlAQ6Nbfft_D3N_TwSZdkeRxsAh_z68xqOPMV1q4I3FYoMl5WEscRBAQurEllxyrY-FLUSeDTgK72BJGpAiuzErnJNvGI2LUuQS0i8Uhx82dxK37jQqQPc8mj7iPWa80Lu3yYq4z14uH6_aR7y0NzofeQtnmLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=Xu0VSQ1vjVoSF8Gn0TRu21c99oOxLj3ShohHTAxSPDd4mGX-FkfTKJA4vnsCHV5w-W9RMopC-Pc13pSyl2Cn9ZCuUnOzGAWJheb3V5g-8nK5P4ik5surmKoCTD6FS4hndFMmfDz6cFp7PYNNQcZJNUQezDmtgpYRmnp1HObthbqnburJcEIIu0ANHlAQ6Nbfft_D3N_TwSZdkeRxsAh_z68xqOPMV1q4I3FYoMl5WEscRBAQurEllxyrY-FLUSeDTgK72BJGpAiuzErnJNvGI2LUuQS0i8Uhx82dxK37jQqQPc8mj7iPWa80Lu3yYq4z14uH6_aR7y0NzofeQtnmLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
۲۰ سال و ۶ جام‌جهانی و افتخارآفرینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100458" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100457">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=JU5HpWqSQG3RQkXU30anpv4GTUWn06Wn7ZIm9-1RsWEQAy6yucnoE0K7zrighfAuYngO1xw_qCeA1AoaVOscMRJaRqtYs9n7DIHQY9V37Ko-whaoXeL_FBAU63NepL5Sn6re51vX0Md2q_4AyV7CooGwHwHRO0b7u_NunxJ_A13XsiKGlwLLidVqGaROkhinIUR98woVDIXijfWZsWHL7gy5S9i_ccO9cv2ryQoPq8D834_dfx13HipXrleyaakjnDmXrxjXMCa73dsf-3hyaRFgNsDVQocmZDY60WrMayse4w8XAGzumuQDLPbkILL2cyFQ5Yh4Tn-9GcJxuEI1oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=JU5HpWqSQG3RQkXU30anpv4GTUWn06Wn7ZIm9-1RsWEQAy6yucnoE0K7zrighfAuYngO1xw_qCeA1AoaVOscMRJaRqtYs9n7DIHQY9V37Ko-whaoXeL_FBAU63NepL5Sn6re51vX0Md2q_4AyV7CooGwHwHRO0b7u_NunxJ_A13XsiKGlwLLidVqGaROkhinIUR98woVDIXijfWZsWHL7gy5S9i_ccO9cv2ryQoPq8D834_dfx13HipXrleyaakjnDmXrxjXMCa73dsf-3hyaRFgNsDVQocmZDY60WrMayse4w8XAGzumuQDLPbkILL2cyFQ5Yh4Tn-9GcJxuEI1oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
پشمام از مردم آرژانتین بعد گل لائوتارو
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/100457" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100456">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-Rub5fXMu3AirHI99xH2XAa9kKnS63X8G6fCxr2ILuDfxv-tOe5dgWXe-gX0YIkyaFKU0DN2o6OIBWlVUdwy_XZgHJXtWk9mbVJViISrjd5yrdZ9-U6CWjRuSkmM0KhxpjuF0ZlBkNjX-iXjezI9G9PP33E4qB_od5ah3qrf0683djttqtI1Jwoup6mHkrMPv8yK1dDzUztsBRM-Bw3JCPfJMRtryNYqS6TENCIaHPHHdJsWXsXMnu9ZoKEgqygXAfiDb2tc8xxYwMM2bRTPhmNtWeFgZueARVzY5GuezSRo308q13yu5kJvzNfVYkXq8U0hczjQnhmZ-pcKBazEh7y38" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-Rub5fXMu3AirHI99xH2XAa9kKnS63X8G6fCxr2ILuDfxv-tOe5dgWXe-gX0YIkyaFKU0DN2o6OIBWlVUdwy_XZgHJXtWk9mbVJViISrjd5yrdZ9-U6CWjRuSkmM0KhxpjuF0ZlBkNjX-iXjezI9G9PP33E4qB_od5ah3qrf0683djttqtI1Jwoup6mHkrMPv8yK1dDzUztsBRM-Bw3JCPfJMRtryNYqS6TENCIaHPHHdJsWXsXMnu9ZoKEgqygXAfiDb2tc8xxYwMM2bRTPhmNtWeFgZueARVzY5GuezSRo308q13yu5kJvzNfVYkXq8U0hczjQnhmZ-pcKBazEh7y38" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کون پاره لب خندون مثل اسپید کسخل
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/100456" target="_blank">📅 09:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100455">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbdUNMG8A44NjycQ1217wv3Fd8bEoSknZdxABs2xBRRvuswtEM7w9mst2Ggfy2b4fldvLLvf1H-Rum-H3OE_EsumYb1ruiA0oaSy2CZ4gXUCOMJDpEAnCcFd9Rh6woXQOav_bjoX3abAQ9xwn8St5mWrd1RnlY-b4AwwhycNbNvULk-xyHKXnYD-zscVFhhLRaSTqZw6p9HP-uSK84NQI6WhVZjr5MsWlwpVNxoNbfMGaezNdfZD2RgxfxeyrZyAvt30EEjMD9UuHfnwiLG53p-JgvPf_dBunXDZSWd58xaedFFimXekVgUUQWBmEQXs3JdqUQz-KkUSSJsWrXrrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جود بِلینگهام: "برای من، بازی کردن در برابر لئو مسی فوق‌العاده است. عملکردی که او در جام جهانی ارائه می‌دهد، شگفت‌انگیز است. برای او در فینال آرزوی موفقیت دارم."
🤝
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/100455" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100454">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=HJS7szEi1VwXKAFxHiJ_AS2umZ2lS0RbZmI7aXIvKWUeTURppB1SPfZY1WaeTV34E11gtIfBfdUF5DVOpnn6TLf7RB_zBVQvEwZImN2Iv2R-0Gu07Dfee8Kdq6e_iRZVmOljChxb9XQluGpSs0nB1oIb-7PRToeZ77oAdAOlAdg2PfFLX6jgRvYCkY0miKYeSHbuR7zAWPEt26753OJgbJ_mcZ29fgBWWLkwJiDXXh6k_TkIEPNkEOTgegX9VnGE9PiPWe5qBAp8INqPwqzmkXrQzBV2A6E4AywJYi5pqxCIs-1Ayq8nl3T_VcGZkRie_7NMaab1RtfYbOFGJtX9JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=HJS7szEi1VwXKAFxHiJ_AS2umZ2lS0RbZmI7aXIvKWUeTURppB1SPfZY1WaeTV34E11gtIfBfdUF5DVOpnn6TLf7RB_zBVQvEwZImN2Iv2R-0Gu07Dfee8Kdq6e_iRZVmOljChxb9XQluGpSs0nB1oIb-7PRToeZ77oAdAOlAdg2PfFLX6jgRvYCkY0miKYeSHbuR7zAWPEt26753OJgbJ_mcZ29fgBWWLkwJiDXXh6k_TkIEPNkEOTgegX9VnGE9PiPWe5qBAp8INqPwqzmkXrQzBV2A6E4AywJYi5pqxCIs-1Ayq8nl3T_VcGZkRie_7NMaab1RtfYbOFGJtX9JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی خودمونیم بدل هالند خیلی خوشکله
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/100454" target="_blank">📅 09:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100453">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpDjc5fcHl9LAoS6DVtaVU1K2uL4KBw0G8mnu2Ihl4PGtxGDDaEPp0gvPrHQxRu3P339OGV9EEqhdSxO3xIwHSN0XJZf8QwwSqoebfs_N0hAVMoFbZCD4D-JQLjG7HME8ZmFuWZKVstBdJieK9Do4evlZ46v6rebwrDLZashSRX4jY_tsORkKzd7nQw-GQ5T3hxb6L-IepDqn6te1A4r-UjeK5pwX2qlbxer_09YP8-R7hnTKGqvdt5meiwh1wNwJh67i7Glu670jODDnFmnCIi_9M7LPN-9YrE2gLdwBqrgOfe8Ji6vCb7x32TInI2Me-ChHwKJsILlJoA-vBvqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
| تعداد دریبل موفق بازیکنان آرژانتین (به جز مسی) + بازیکنان انگلیس در طول کل مسابقه: ۱۰ دریبل موفق
🥂
مسی ۳۹ ساله: ۱۰ دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100453" target="_blank">📅 06:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100452">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pea_U9C02Rc3k2ssk5GF7jwkcKV84cHyW9jGZPLeFPzLr0u5iwVinrd5l9pflTR-VEuRwqKo4xL0PMQfCbBC-vBVfpDLYUSgN-FnsNTbXOie7ilpfdU7ZgNsFJsT1ocVtrWz3CNN5stt2l8pIXpWzqOpT5gu8GcXEGSZfcbhqxkqKCWuFL_5_RrQZ_GdZRKLSAPbff7IU4IwYYLmx8HduEg59hEZFV5gwaH-rMmxvx6t3DjB4hcf9UuJI1lTw5-oIkNlo9HQP5tjbmbTTNeEVjBUN7e--sKwcfjy2oyEfoX3tDibiZt4HmSWwKsaOB058tYDvpV8Od4Kfs35e1XG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
لیونل مسی :
🔺
من خیلی از بازیکنان اسپانیا رو می‌شناسم. خیلی از اونا در بارسلونا بازی می‌کنند، تیمی که من عاشق آن هستم و هنوز هم اخبارشو دنبال می‌کنم. این مسابقه بین ما و اونا بسیار نزدیک خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/100452" target="_blank">📅 05:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100451">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=LE8zg1S1D0aKUpeyIuHJi5gsg--MHO7Zu9NyQ1ZPEUpC8VeXM5K4INiXIT0bsaE5lXBEH4rjNrsBIKSobE-00h1exlCmEcXiGL_L2Nr6w9Z71ex05nXmv5ANCmmdDWlZkjRHbl7O_r8woJHBRJxiihl3jw1n95X-qD6pNJvykFG_F_E9p3RN4Hj_0WDY67eSCDiaASmeMr_NNumbi9NZXWFfrilJJWDnZfQgO499jrvN3qMW5sWujXWSscAC3EHQfhDcEMpkHzElulVL6v3sE71CcViuqh-ylikuQ26ls1ybHYi2_1duhjWHsA31kJXSpLVeBVJBxOSxA8s-22n5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=LE8zg1S1D0aKUpeyIuHJi5gsg--MHO7Zu9NyQ1ZPEUpC8VeXM5K4INiXIT0bsaE5lXBEH4rjNrsBIKSobE-00h1exlCmEcXiGL_L2Nr6w9Z71ex05nXmv5ANCmmdDWlZkjRHbl7O_r8woJHBRJxiihl3jw1n95X-qD6pNJvykFG_F_E9p3RN4Hj_0WDY67eSCDiaASmeMr_NNumbi9NZXWFfrilJJWDnZfQgO499jrvN3qMW5sWujXWSscAC3EHQfhDcEMpkHzElulVL6v3sE71CcViuqh-ylikuQ26ls1ybHYi2_1duhjWHsA31kJXSpLVeBVJBxOSxA8s-22n5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی 2026: اسپانیا-آرژانتین.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/100451" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100450">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIw7eWaX2rKz6N2jmitwzHk66gooX81MAMvuyqNUZ0i1hiw0SfAmAOlkMVucj9Eqk7asrPngG0lxPt0dEy09VC16pl6hM1phq_d8Pgw_QbU7VnvQS6EThK0sbLW5awXCayic4-qtEvkeoRLBFJHLs7QJ4MOJVdcLqv8Tl7eG3xqCwvFkSSKGJ6BfGQEeVW9Yuvnhx6osGVXoRngXpRzPdNYG_vuQH6GH_7XtkqoA7Ar9GFM352o_L7W0F3zUP77ueTqzvNiqGWs7_2JYUc02nkVuQSLlnsvOPpD_tt3kXIiixKbT5r_PmCod2lXTmrFw6mIbfcGshMqw9jnqvxODIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/100450" target="_blank">📅 03:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100448">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBHdCTxt7iPPerjcokaw2D-kmPM-9da6sCaFhCBegRDmVqC1u3QZdXMBlizjuVxcQRChuHLVhtIFOCb62MGt9usA0vGqMxQbthPD4ztopXfI9zm9QvSM7rz86ntyGaSSkRedCtl4YQOW1ISP96x-2arNVGAg3HWR1fGrLTjCbfI_-E96AAcf3Lk8TgcKwZrOUVTWKgG7tk5nQoldid__yZFQ6iN4HUNcnxr1PAn5AMtudnNd3giKSGm9pqj5gjr53R5NY2yx2YT3HUQXw8umJrAOx9KyE8hGjByzYwaAijFOp0jlwkhxNs6n-eDRGO1UzpypF1GV0rAXuv4G5QuHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا ممکن است تیم ملی آرژانتین را پس از برافراشتن بنری با عنوان جزایر مالویناس (فالکلند) متعلق به آرژانتین است جریمه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100448" target="_blank">📅 02:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100447">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=lUakfvGurSAyhwMMz27EI9A2Ly5bTWv_Ftf94T-evLx7RDBL3DZAOBftHejJ4EtdbWr4I5A0bcFSWx-hfBdDgFanp3_vWxeir9eZpH6a7yZY3yQxeRqwZzNSz4C0paKweEccW8Sxo2vetpqVgjLQrVbP9AlpkPiceK5YOgLtuLpF2m51OPjde0VdOO9Oh9MNLT1ZaE7fB0vyPnGKuaPalUcYTGqO-LhJ9G5tdJnj3CHRnIuKcIJaa2O_JNm0rztAsBOICvHZH4bZ97exdQnNNYXYtwzY7tS6c_6QJJeAuO6fzLRWxknQS0wazTQakPlVd3mnLEpT_Xe2sLfPljAhdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=lUakfvGurSAyhwMMz27EI9A2Ly5bTWv_Ftf94T-evLx7RDBL3DZAOBftHejJ4EtdbWr4I5A0bcFSWx-hfBdDgFanp3_vWxeir9eZpH6a7yZY3yQxeRqwZzNSz4C0paKweEccW8Sxo2vetpqVgjLQrVbP9AlpkPiceK5YOgLtuLpF2m51OPjde0VdOO9Oh9MNLT1ZaE7fB0vyPnGKuaPalUcYTGqO-LhJ9G5tdJnj3CHRnIuKcIJaa2O_JNm0rztAsBOICvHZH4bZ97exdQnNNYXYtwzY7tS6c_6QJJeAuO6fzLRWxknQS0wazTQakPlVd3mnLEpT_Xe2sLfPljAhdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری اکت توخل و اسکالونی بعد از گل دوم آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/100447" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100446">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=Lep5CPsk8ads2mpZj5ch9bCT4sDq-ZObHK-Iarlve-R4WJoLBWfzV52P-7ynnepqmDwq4T4R0-XWwWroOj2b51GjS2bS0gOQzzgFLfHEmTLhtdWheghkU849I9wLC7L0RMomm8NuEAvNxj7r_FxQXO_8gkvawYfIIPKO3RH6_rQvO8fymwQaLtYrGeEERVUze7czfaxQKB9h67Bv-8pe788VLigQZUIOLJHN4LCtgCLVLhmpzDm6UuOEwL1kd-WXJhdgHQixmKazcMaiFFApRzuqzC3Ad5f7uAvVnQOP0kEfudJcAPx_6vx51C-SwYUtz2nk4niATNI7965nOaVqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=Lep5CPsk8ads2mpZj5ch9bCT4sDq-ZObHK-Iarlve-R4WJoLBWfzV52P-7ynnepqmDwq4T4R0-XWwWroOj2b51GjS2bS0gOQzzgFLfHEmTLhtdWheghkU849I9wLC7L0RMomm8NuEAvNxj7r_FxQXO_8gkvawYfIIPKO3RH6_rQvO8fymwQaLtYrGeEERVUze7czfaxQKB9h67Bv-8pe788VLigQZUIOLJHN4LCtgCLVLhmpzDm6UuOEwL1kd-WXJhdgHQixmKazcMaiFFApRzuqzC3Ad5f7uAvVnQOP0kEfudJcAPx_6vx51C-SwYUtz2nk4niATNI7965nOaVqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل کل مسی و بلینگهام
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100446" target="_blank">📅 02:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100445">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNgiiYjU-2crFa1bBQzM4TMhadbApNBiFWCaMnqkAe6A-K-IwcQG0LGlzNQAcoC1NR6PKPGydU9mr-r_HcXEzUUUPh95-O-m5eXGlDD1fbgb08FTD7txBtUwELQohTB445x2yXsuG3f2dguoZWY1yuGokZqY5WeaNyzVGxCKMqcd_Zh0pcn6nBzz7yEJo7OeQ1MbrKViQWc1Ty-_9C9CmiQntDszUqYTTioL-4RH19IYYoWV8LJ7todbAv9OxnWP4ttTG7JqQXO_vAlHqSg_fUpUNH6jPjpM2VR-pBRv8biB3UcBdQS2urpQpcfknVIF4BfKe_QhFpv90bzkPHI9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لائوتارو پس از به ثمر رساندن گل، نام مسی را که روی پیراهن او نوشته شده بود، بوسید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/100445" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100444">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAQjCXzDwRbRok0ZBRXQ9PkkQ2ECjg5REjuKMl1cNv_FfvnwJOPFLMAlMvXVP2F8z7kFjZXlTZ_7IEsdTeB8WVxOvkJx4u6cDAGzUQ9kk1RLnCYH_Oe15_mmE1vC8uLRi9pHIbYwCAMw2FOifhRd3HcOoIJ9n5xxXYXZHGCNB7BK4kJxL08-FcS_9AihinuozqhfyE_7qgU2-i41ezV02G5MP5FfCNxJt97Ip2Y_tOVoUKRUA0b4C-cDMsDl8blNUQ6BFH-Hms3aaNXk_iAorO1xP617pthlxmr5ot3Ovvxca2GHZefySl056Id86ZqDqHbPpsjkwjvVba6kgeGGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی:
این جام جهانی دیوانه کننده است و رسیدن دوباره به فینال باورنکردنی است. من به آرژانتینی ها در قطر گفتم: خوش بگذرانید، این تیم هرگز ناامید نمی شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/100444" target="_blank">📅 02:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100441">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zd2Bd_PY1fmCDY5afwXA6Yi4iIbBXdUVlMApdmNod_GPIOgLNMRef99so0xatbg1_lkeoSUPc8bsWDn82CBpjxBrScqV_dv-aU8rhkvql4C0pEJ8bGymknMaX_o6dXfpumlCr717PrSfu28iv4U9ZYJugAfYV7VEQd9EL5L7_Wu2ldthhFzqaqOe8w5-VwX_LawlILsknjJ-W8QN96mJBw76k2aqMn3d0HJuJqsO4OtvK1Z9Otcomaua3-CnM00Dk1sdE16k8OAMBc_4Xx3sbCYvJiUB-mNAIIdoCP_Y_nJuMSf8-GR87uzosH1OHAOmHB4geVQ4jYIQlpJVYHoqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/od7Hh8qMbrF1ySkMzMeWT8JQLHn_WcOnxKCjNDMMZFMeWcpNYHHIsKWK4e6e5SNYAVSaSvVk3gNRsVtNAJAJSJiKPnC_3a7H97gLqMuiLSZf8s7mS9F4RuiCp1_eMDu3gtIBvlFrGEy_fDN8G99ZtDEFow8TEO-IJjkmDAktthYkvnGwzDU69i9MYUCHTpkhgdgw7Pnnbk3okQ3H8pXZmwI3HhaQtWi83K03BoCtFhuy-peNzIThgvFC3lo-YJ8szUR94PnIS9jKVjjjO2b8A4xUBN-WgXeJaFOJx9o4CH6iFwvVSCf1-QfIEQVpphDhBGW-w3KwOCSs6GuDfPjcvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mJac5v8rGox5M5zRD6xopbvP9duObm8bde3Z0UvYWssmdn-CLQN-CcbsTZLN0eCnPvyZCOqYemW26sMTDkDguetVHh-8pu-U776Gyj86aZ9b2Q3nFY2SWVhrOAvocbhCmxfFRxqgxmt-69owUof9qdCTJ9JBkPg0Lk0k06u7fQAEf9QKnmo2GLSy1Hsc8YOdUsniLBoSCn0C1ExK531_a-xR4u8RiFDND07VTKmjPulxL7AIcGVupbcfsuBXhyFscnJ22E5Lc95W_jmcrk5GbtKhiYY4xjFnprBaS1chunCQbFH7xuSMZzTdyAKgGdNnGVeMZbW9xBv3Lx33aqWTYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
🐐
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/100441" target="_blank">📅 02:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100440">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia0NECdAomjnF5ia7ct1Q4MBq6wjAL8sYW5-chSUKjx8du6dJoL6HPrsV9oBMAFqfIOymEVWXGkd4WISFAgYBoLWcx6Z3nM8HJzAV3_0kB4QpJ1l4I0PVYyp_W9Qps-dp2E_MDZlBy7EBecmSdWzDbyvM9085ZRa08_tnmOlgt-C7p7bau8XwUGkLmb4F_TVoxzOQtZtZ_UCI2abKk1gretciAaI1lZurVJPFHpi0cvsY71ocCkUe9ymAgf3V6oGMYyxLQQjyECeoxM7nUan1G6QiS_lpnuj47BKhjfV2VtyiM0QpNBH4AvUgo9IXKWq-HahAkeVSaqze5a4_ZrQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
اسطوره لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100440" target="_blank">📅 02:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100439">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135c24c050.mp4?token=pfpT7JDogVBqynjjzBDwYhWk0hejRLaLWtYbpYks4rsKItMKZepoUqjREvONufKLJevK_4JUJzqF6RIBrB9nuwec95-SpRt68fDYkxNklTAsqY6ujtri1D6Q4GKKGFK2wqtdXu66zw2EMbYt-x8hgDrr5Wzw0kVPcWGYd-YkQ6cTr887VEvrKi09YZ74H7SQVV9Xg1TdEMjbjYRFqhskmZw4Glx_eDvI-i0-Q06TU6Og1uMlhNKrUx1NMLEM6KQ-Cz11EURypgzXjsooonTsdA0L8f5_62uVuOUP39R6w-4KsRa5agw4OKl-xPwG0HLOgIufpOAl3krISg4Xe9LGHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135c24c050.mp4?token=pfpT7JDogVBqynjjzBDwYhWk0hejRLaLWtYbpYks4rsKItMKZepoUqjREvONufKLJevK_4JUJzqF6RIBrB9nuwec95-SpRt68fDYkxNklTAsqY6ujtri1D6Q4GKKGFK2wqtdXu66zw2EMbYt-x8hgDrr5Wzw0kVPcWGYd-YkQ6cTr887VEvrKi09YZ74H7SQVV9Xg1TdEMjbjYRFqhskmZw4Glx_eDvI-i0-Q06TU6Og1uMlhNKrUx1NMLEM6KQ-Cz11EURypgzXjsooonTsdA0L8f5_62uVuOUP39R6w-4KsRa5agw4OKl-xPwG0HLOgIufpOAl3krISg4Xe9LGHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
شادی آرژانتینی‌ها با رهبری لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100439" target="_blank">📅 02:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100438">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiC_jVbNGR2y0DuyWNb4X3dBP1P8ZgM8_BLuxa_NaVUEbN7dPGjQq6V9SZv7MVjAX3GfCDvSAjGer1pwuyMGCWbWQ8hly6o4Pt1ftJHs05uaLUL1fJrBw7J8wDdY-p3bMEWJ0MmV4nmPkefqGCuJjDO6X0FDG91QShn_uM5dodMJ9WkIPYiU7uS7kQF8ShEOiuKFWGEdJqjoXpZ7FsUlhP_9U1_gmM4mO1aMKCtTN6LXzJ5LcNIq6eokT6VsNdUtw8QgPEwpc6qrsqmfrC5eiv-2h4yi71lavNvQyxbQzL2p6kSiKKUjdA1pJ5AoHQVUd55gAKEu9EWLbwxgwo1qJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیونل مسی و کافو تنها بازیکنانی هستند که در سه فینال جام جهانی شرکت کرده اند.
کافو: 1994، 1998 و 2002
مسی: 2014 ، 2022 و 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100438" target="_blank">📅 02:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100437">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=dfMFVXrl0oKdjMGdAEfMEU-dSQ7M_SZB2KnC3gtGcD5FKVefSqWJ9t7D7TT0VYj0Ti3PWKhDQNdJo6v7T71KAJQ5s2wje1Q6KLUU9gRNcG3C417G1e5vAc4KqajKaHTJPPvCNGx8suZ5kBB1r7KJ25AII7JbgkpY4Se5uIOd_InJBRQpx2pSSYoKplRZf9xcr9fLPxFjjLbAERPxSW-7CWkwutYx6p8moQOB7szPrE-NCRURfcpQNHevYMXnDFUv5j9Wd7nvajzSp_IZgF0v44baz07T4-zCv0O67AFe89qkbtwvHIq0PteqxRCKEbOiMbuUf2YbC9FNN4lIE3eReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e27d580c5.mp4?token=dfMFVXrl0oKdjMGdAEfMEU-dSQ7M_SZB2KnC3gtGcD5FKVefSqWJ9t7D7TT0VYj0Ti3PWKhDQNdJo6v7T71KAJQ5s2wje1Q6KLUU9gRNcG3C417G1e5vAc4KqajKaHTJPPvCNGx8suZ5kBB1r7KJ25AII7JbgkpY4Se5uIOd_InJBRQpx2pSSYoKplRZf9xcr9fLPxFjjLbAERPxSW-7CWkwutYx6p8moQOB7szPrE-NCRURfcpQNHevYMXnDFUv5j9Wd7nvajzSp_IZgF0v44baz07T4-zCv0O67AFe89qkbtwvHIq0PteqxRCKEbOiMbuUf2YbC9FNN4lIE3eReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
حرکت زشت و عجیب بلینگهام بعد بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/100437" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100436">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🎙
اسکالونی:
ما برای پیروزی به فینال می رویم و برای قهرمانی در جام جهانی تلاش خواهیم کرد.
هیچ کلمه ای برای توصیف بازیکنانم پیدا نمیکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100436" target="_blank">📅 01:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100435">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=vzEXMSqscfqbXrZ5Y2AMJbn9qOIqzBTm-7wfjVowChEaoJOKszLWbZkFME00b75XA8xvzr1TkjTHxEsNslNIAaFmENWWNVouLUoeuG2clwV31-iyupoTZotptcnyu_995Zd_8CFsHVNbDy4kgnp5FI5P9lpobS_wDohVlSN-zD1ArlNirRIGKWHB3eYT9r7h5cXjglJ6bE9BMcbuHx9dZ_3pT64E3H5iDrFra3XlHprUaTrnxFYrhd_mOM-mraIoRNP8842M7AF-YkeOGAdNYrBYpwUStxo2ZQGQyDsNLHNZ0vxkJNSWYAiJln-vRc3nHUWsx4A2RM3RVU_-XcqNPIs7npIzBrVYKg4T2605wiN5m4CVMlJQew3_Ocsf_yHWyR154yrtXHc7l1V5VXFdKwcNXl6l_SqBVOCICrKTvRGic0TeSpE9NWTT3S88sj1EILmpvALaGPnzYTCxjEVYYADNUuumHEEgw-o1ZIooMQTSuuVNSflvUjwTA4Mp6Wq689Lx33U-CZbK4yepDNUvaCO7UuXuZ66e74i4eWGuHD_BR1-qpB4RRVXEcTfFV9BLznQHbitKTAkE_4rxelGXAH_ynE4lZfXbYmd2ZBarExt6dV6bjMdwBA0ZRctUVaV4AJ_azM3LSc362hPc9Kddimzh19Z_gQtVAcQ1PLGhrm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9481ccab4.mp4?token=vzEXMSqscfqbXrZ5Y2AMJbn9qOIqzBTm-7wfjVowChEaoJOKszLWbZkFME00b75XA8xvzr1TkjTHxEsNslNIAaFmENWWNVouLUoeuG2clwV31-iyupoTZotptcnyu_995Zd_8CFsHVNbDy4kgnp5FI5P9lpobS_wDohVlSN-zD1ArlNirRIGKWHB3eYT9r7h5cXjglJ6bE9BMcbuHx9dZ_3pT64E3H5iDrFra3XlHprUaTrnxFYrhd_mOM-mraIoRNP8842M7AF-YkeOGAdNYrBYpwUStxo2ZQGQyDsNLHNZ0vxkJNSWYAiJln-vRc3nHUWsx4A2RM3RVU_-XcqNPIs7npIzBrVYKg4T2605wiN5m4CVMlJQew3_Ocsf_yHWyR154yrtXHc7l1V5VXFdKwcNXl6l_SqBVOCICrKTvRGic0TeSpE9NWTT3S88sj1EILmpvALaGPnzYTCxjEVYYADNUuumHEEgw-o1ZIooMQTSuuVNSflvUjwTA4Mp6Wq689Lx33U-CZbK4yepDNUvaCO7UuXuZ66e74i4eWGuHD_BR1-qpB4RRVXEcTfFV9BLznQHbitKTAkE_4rxelGXAH_ynE4lZfXbYmd2ZBarExt6dV6bjMdwBA0ZRctUVaV4AJ_azM3LSc362hPc9Kddimzh19Z_gQtVAcQ1PLGhrm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇦🇷
🤯
کسخل شدن گزارشگر آرژانتینی پس از گل لائوتارو مارتینز به انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/100435" target="_blank">📅 01:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100434">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PozGwsmkKtnJvqdilGKw2cYcDxSJl6JkxdlODWwLGEk97uM58bYKmIhtNgSHj30gppSmmPQLraFYyBy9vx76OGDnlvxaD3RkvVbt2_Pvv9DFlcFwAl9nN8LLIbh3_oJfrJ3fa_vCw3hRElDA-xUY8qwE1lA7zWCIcmvg5Skx8GJU02emZ8l1J37Sztq_S6CBecjDbNWzqU5dE_N_9btH6SAgA65vW52CwjEVKeVbN-x3J29dXosdoLOUwDM0eBNhkIBbNlhcQHkE0TxyVWBTPzfWvKC1U_ZLFGYL7OntHAcHu06EeOd38EHpM3n8SCa3DRyf_19OO2C80dKWogj5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ‌هالند بعد برد آرژانتین
😂
😂
🔥
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/100434" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100433">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp6GebD4xwsxamVxA3DdLW1fK3DZUsF22sVjRyjYG8xJEh04aIaUsZf5YFFhhDLx46JknKHcpW-MLTSMYrupFLScStbvu5nAyEFsI_s9-aqdCnWXGGox8cjuD4YUmUv6El5xOpuTt2WN1Bb4RVZVcMswFsg5Qct7JnZUp7dz90gVWZWn6h96L1XYfAiVAHLtGx6W8dCnwBdtYFHooS-aXoHVgVuWmhrMyrVYTzhazZ6xeb00fGxbXUaC_2PjkFv6X4UqxhLpcjyCzeYe6stOejQxcyQPO-cs_zJb0fbsF-s5LjkuYLD4E3y03H-YM_8zx_q6muouFA17aoyJ4zVg-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🎙
خایه‌مالی سنگین گوردون برای بارساییا
:
سال‌هاست که شاهد تأثیرگذاری لئو مسی برای بارسلونا هستم و امروز متوجه شدم که او حتی از آنچه فکر می‌کردم هم بهتر است. از حذف ناامید هستم، اما می‌دانم که حداقل جام جهانی را کسی خواهد برد که دیوانه‌وار بارسلونا را دوست دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/100433" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100432">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=JosP5Sxdw3LPokbaVsF1cTh9qgOooGIj6lZrU4suv6lYa0oocKpUkZNqxRDVXQYW9ZnwAvr0WUh3d5liZI9vncb1nnXzG2jbz7OPgkrAVfV6RcV7pJQhHtyDpO-md-8GOsdPjytOB9O1vfBAvbyIYhmUWkWD_R6deIshl1Mi4mevfkU_Nu7J4BuuoPKQPXn-fmeiT0isjuwAJuDxNw2dj5PK27m95edmS9Gs2UESNP3iqoMWZcQ2L8EducgslnHGEp0lsDW3Pddb25fMbespEoIJjgKr01Fk-tYnNyHSnVURU6gsqGlEh7XRwIf8cFSADfkl3NIF7od7C-hr2ADWaR6f8uUdnlY4rg9sdAahCbe0hRMKFYO3C0X3Wl3y2OGtxHjqOrbG9JBWLlhQRAY3-7qzqCe-GltI3h4OhePxeWXL47a9F0quT-Kvs0gLnaAjyx4DBsoLR_4MtIrU0nLHqutosWXcIqT2tyIphlgQa-lzrvvDaDOzosnENwqXw-PHSjkPAi1c-AD4MgDvTtN9Fk0exTmzu7hGSaZSpomC2HCKRtvWzE5-lstYIuH0OwSihBs49FQCHD4uHDpcQMIbYu0qyrwqbYZw8VytmoP_32FIXy7h1kqNv18QmAbTO0rmT6KZilh8bVok5-5ZGxMy38jqwIoIwLNdz4yGz9I6roQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f031b79a3.mp4?token=JosP5Sxdw3LPokbaVsF1cTh9qgOooGIj6lZrU4suv6lYa0oocKpUkZNqxRDVXQYW9ZnwAvr0WUh3d5liZI9vncb1nnXzG2jbz7OPgkrAVfV6RcV7pJQhHtyDpO-md-8GOsdPjytOB9O1vfBAvbyIYhmUWkWD_R6deIshl1Mi4mevfkU_Nu7J4BuuoPKQPXn-fmeiT0isjuwAJuDxNw2dj5PK27m95edmS9Gs2UESNP3iqoMWZcQ2L8EducgslnHGEp0lsDW3Pddb25fMbespEoIJjgKr01Fk-tYnNyHSnVURU6gsqGlEh7XRwIf8cFSADfkl3NIF7od7C-hr2ADWaR6f8uUdnlY4rg9sdAahCbe0hRMKFYO3C0X3Wl3y2OGtxHjqOrbG9JBWLlhQRAY3-7qzqCe-GltI3h4OhePxeWXL47a9F0quT-Kvs0gLnaAjyx4DBsoLR_4MtIrU0nLHqutosWXcIqT2tyIphlgQa-lzrvvDaDOzosnENwqXw-PHSjkPAi1c-AD4MgDvTtN9Fk0exTmzu7hGSaZSpomC2HCKRtvWzE5-lstYIuH0OwSihBs49FQCHD4uHDpcQMIbYu0qyrwqbYZw8VytmoP_32FIXy7h1kqNv18QmAbTO0rmT6KZilh8bVok5-5ZGxMy38jqwIoIwLNdz4yGz9I6roQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جو فوق‌العاده رختکن آرژانتین
🔥
🔥
🔥
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100432" target="_blank">📅 01:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100430">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRB6qAraOTLD3s0vGBjOQDkthkOFu4etWODUQ4ln0QTrkotbUJc2OfF8KIiahivc4PDCjhQYiJmdwX6RivkGmFupdM4DAHt1ST3P8eK5vWrqrRca4iT29JMlg1s79RhPloHDgq_7LfQNe3SHAS5O8U5lIcrP_O748aLyLprBwiy7BI10a7KS_1Q6IpAldy9VP98aEb3FSZxpXhFGcUiuespfGiTPDKWmT2RMofbQTTIBKLttGxgmd-KegrwI8-aecBEW6uXcdx931MuNDt1n0bkEPBWlM11ChSYkgXwVpeJyOYMKt7XU-2TwGj36RPFuNyerrZWFApZ2CIY-wOaIAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙
هری کین: مسی یکی از بهترین بازیکنان جهان است. ما سعی کردیم تا حد ممکن جلوی او را بگیریم، اما وقتی توپ به او می‌رسد، حس می‌کنید که انگار دوباره به زندگی برمی‌گردد.
😮‍💨
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100430" target="_blank">📅 01:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100429">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-bfPf6cOYMFQDsiu1JH6wJbSuxbsi640YwWUIR7GIhXZ4-t6albyLMEOcNGfvLK9LJaLapRisrYINJyLHMNaPCclC6mibaM8P65SOyi_Njfwh2MC_Dp0zLWCDwGoqF5QsFK2DA2IN6tyS_mu1BSYEqdrKjE7EQyKxRl85PsZ7wKcKPihR7QjMxcNMJeIcV1ioFDQBZS0PgJfYcZDZpw_kwq0tKFZxa2HZloLYX1fhyKQmfZy4qKNPWocQvxWXKJ9_3F54wR5b593hh60oElRKeOe9BbCNrFwAiElub-kjDiWwUnnjug-j9M38DbYbf0VAiL5ee-yF59qy51tmMHdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇦🇷
طبق آمار اپتا، احتمال پیروزی آرژانتین قبل از گل انزو فرناندز، 1.3 درصد بود.
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100429" target="_blank">📅 01:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100428">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_tte_7PR3rc5DjApFqE2NTVzF3el2EZrVJXVH6q77EAoxisNtNS6XCYW2DKAgB0OI5bYOJBGsOnfxnkPSET0GZXL32w25tCDQGbaWGE9D5NDOjuHYOpkRiefcVGJ4bfs3n3Ra1aoUb2vUmqDMC2vqW0YkMV7SCZwd8IIa3Y9EMcN9qS629PinkXTYHuTXcLMjFL7kkjW3dA7uXK_ebGhNPD3IZDCjYxumLKW8P0PNFQL_vO0hGmcPX-T_4hk8Zfzt_vus21D6WMnXUv62mSkClT9XIuC6IAwjtL2L2MIWufTEHyq3AeEXQ1P4OQHcC3At3pDyuch8vUE2fxeBALTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
😐
🤯
کاربری ۵ سال پیش پیش‌بینی کرده فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا سه بر دو به سود آلبی‌سلسته تمام می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/100428" target="_blank">📅 01:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100427">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSDZFVTo9R0pE9xX2YwJ00H0gGaDXOcpuCq_KGTxEXnGU1_7CR55z28h-R_mxjIMMiNt7Lv3v0xhthnyhHRzOM0iyVEw4vvTRPJ5Op6-dnRSeQDfb5yc5ZgK7bUg09DjVfSqkAR3HxcdPN7nx1s4SuLTR2V7VZA8cQcNbuRDJU4B-TU538ZObkv99rNMuR8LTFA4eEp0HFvr1h5UXXfhwAElFRcMVAod3bUQbV-ghDA3FuI91pCscgGZYabVoCgFE98j42HnZi-KIJqTfSt-Fxp_o64-szBuBcWUR9N_mjbLl3FfApgyhl2roEiQAjQ9yym-DqLlIr8hleetcUXajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏆
MOTM
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/100427" target="_blank">📅 01:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100426">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOvF7owS4Er1R6GtDNVvaqdiyYynx_rvJzeV17Aoya6kEykaqOTCL5UN_mTRXtpb6pG9nQd2xQEZVc_Nuz1c2OseMLs0vWtkdIOfTZnqflBJOsA3OXgjVpwwVTZlw5agGBxAb5X2YycXkhHczCkHkoLerKkixjoFPUmcMXSLWqLIixUnKEQyVhetgs1P3kb6IzCkP8IL9TzF_mPUjtHi5cD9O1Fj9_Uj510E25PeY0ngn4NS1WjT4TTqoaKpwjXZngFkd-hVbjmXqfCQYuR2b6537GjShwZkWnt34CeTH3yhL4_DnCGLs_KX7lBDtBBX9vVDWBKmHfE0M12llLbbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری کین:
قلبم خیلی شکسته. تیم بعد از اینکه جلو افتاد، خیلی عقب‌نشینی کرد. نباید اینکارو میکردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/100426" target="_blank">📅 01:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100425">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwFg9EuMNRFI-CE0BviUjUt28DXweHUGJAxcpWXsaPYJ4cTHgL8mNY521_UQ-eebFI9Wxba-H_bauL5TpNJtAZ0jbnDjCtr2ar2cvz6GTnKIJYpiqmxhybI2wyAT-zVO3t-doK-yHXFz8FFiO-blfWS6x0yZlvB7-aZMQfkp1wQ-90bwJmXmBlKFTr7zP3hTLSzi9ltIUqUIyXwbLGqnPqu6g62k0X2kLVWkfRYnmetgbKCQwzEO7VypIpxB0L7tkXYu3zP6zvH0jYauBgR545isf6Gn2G6nv0uhtcAG52D6zK6bqLRf_S3DIBKuE3uIel2fbmmdNcgiP8ChKT6rlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: قبل از بازی به صراحت گفتم که لیونل‌مسی یک قاتل بی‌نظیر در زمین است و از او باید بترسیم. او در این سن توانایی خود را به نحو احسن ارائه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/100425" target="_blank">📅 01:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100424">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py05XPPaNEDEO2LznfKa17-Enkquk7LsIx6ywP5HqwDxz_yLKHD9zmEFynrKPK8YJPe1ESl9wG5hHfB2rfCYnlrF-2iovkSfi2bfvBa7mGwW85gbSwIN7lDyKrCA8fK3XYPI5wbf6yNiafmGvKyMyhOtpoweonSKedsd6s-0-yToIkAJ-oEaKeFcEY-iSAtYDLCictkR2TeltS1z6R1DbMqTHXnYjjPY8OWVO9zMB4t2JoPy6OaVwi8ew7yuSzHQstPLt6p2PulaCsgc9mprQ58LKH2YQDGUV_GEp4gjfD51Z1X2QbMe6s5KU187hPvY6U2t5vaTOBQWQES5CF_mJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
اسطوره، مسی، تا به امروز، بیشترین تعداد دریبل موفق را در جام جهانی داشته است: 24 دریبل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/100424" target="_blank">📅 01:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100423">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pw1cak9xsWK87Wu0MKVIgoYN7brOSNrl3-rbHAi9mbsBwDYvqBdPDzBujzddTNHfAVBfxts4ZeUXlZ8vUj-OaHu4VX6_l3GH3oQpOduZpENKyw4Xn0Kw73cA2wJyqQO3p_uAhEtJM-Tk45RSIaj4WkQjtVAWTlScx0RThDWRrJGOv5s7BfBBKGmfaGVGRGZSef_tni-INxAfPwRJe-BV2CSDQ-0K8e9fBAIC0e59gfh5t5i6hh_cYUX--zwYmTyOQWr3swBSwi-p1VMVURg0CLJSKyOnybToLwA_gf6ST-sHG_Irbhki3PJqPl24ch9fjUFpgxHFxogPQHAco2huMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل: شدیدا ناراحتم. نمیدونم چی بگم. بازی ضعیفی بعد گل اول ارائه دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/100423" target="_blank">📅 01:12 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
