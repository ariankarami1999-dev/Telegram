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
<img src="https://cdn1.telesco.pe/file/jhALuPeBAmSaRj9yrKs4fg3BBItuHOGwaCWF7No3lMH7uQDXqYDXbwNJBOfkQ95TW3NB6ChdSMRRaMfAzk9OUYNOZeZdIrLV42yPzTyrYdCIeLpit_rex87y4g_eqneW2XAymGBKczCqBnuhHj7d5_ALKea_DUbMZPch_QasQYQqU0vE9hsOQ6qEm27TSEI4aeiGVeMSnlllJPpRmDnur4WuiJS4CnRrbNh_9x9k46H-QK4oKeZ6iaKLFFDrK66FvoB73tMb717Wh2i8egh9Zipu8l5ryh3Wa-2Iplm8nGFWDvjfg_feZvvOD0Yi_iy1KXO-AvEul3Eb3iXfKg9aKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 02:17:45</div>
<hr>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">هوش مصنوعی و برنامه نویسی | آینده این شغل
لایو هستیم روی کیک:
🟩
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/MatinSenPaii/4999" target="_blank">📅 21:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/MatinSenPaii/4998" target="_blank">📅 20:45 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بچه‌ها شرمنده می‌کنید با استار هایی که میزنید. ممنونم
❤️</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/4997" target="_blank">📅 20:44 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeUFe4TQD0eygR3s99bO3Xt6vFp_YAdxCAAvHWijhuq1DYFbkHsojnVzir344r_G6TEhoPL2K_WMf56CLrIuYuOh2nckKpg8b7wti6XdiW-X90KuFgSpT6s4GR-1t4GyT1bGqzFy46p6yTg12_syvRP3ERBGneCZABtQjV_co1KVJLXyE2d-fv3hjjHtBKASuq7HMCoKya_b8IzDkZSb7azqZuHmVW7iXilFjPlOaQmGcgNOM1OAQXZdeBud2zh2tKwJF4c2macBmfOptcRQodOVOteViNGpJijItahxSD0_-r8z3j1nlixlitMKJ2g8UKdvWDNegxqvLVYYod0Itw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نصب هرمس وب یوآی با یک کلیک
متین سنپای
بهم گفت که Hermes WebUi نصبش سخته و بهتره با یک کلیک بشه نصبش کرد برای همین روی پروژه اصلی PR زدم که اگر تایید بشه از این به بعد میتونید راحت این پنل رو نصب کنید و ازش استفاده کنید.
لینک PR:
https://github.com/nesquena/hermes-webui/pull/7152
میتونید روش ری اکت بدید شاید تاثیری داشته باشه.
اگر هم تایید نکردن مهم نیست
یک پروژه جدید روی گیت هاب خودم اوردم بالا
لینک پروژه:
https://github.com/nesquena/hermes-webui
میتونید به هرمس بدید و بگید براتون نصبش کنه
خیلی ساده همون پروژه اصلی رو میاد براتون نصب میکنه
حس می‌کنم شدم هوش طبیعی متین سنپای که پول توکنش رو نمیده
😂</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/4996" target="_blank">📅 20:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MUQKK02yHWAua74BMobGmyZZfA8TFxWufvOJx48Vgzypn1uJ93USWbXVzn6KhAkSJ5wF0AxSwV9dmVsmKLhzlsPcvG7GHPIVtp0CpUKzlzsNM4w37uZIdOGz69wyQmQXXt0PFcaNBxxU8E5kHUDpnXB4XhvqNe1iK5UtwHw-RrUe9ZR63DvqvpjLSRlcGltEVy1JmiXUYaflNpvp4UscD17-T2VQGgntDe2iG6IQpA_6wdzTUUTf1c5p4SmjSqsV9PtNhXq57uBwG9_dxO8G7gRxop2nwyV6UTmPyctH8GrByqLknzQqA4VkWe_r8Hfdrfhi3fdxCsrsZ22nY1hYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PCYBSuCfI5alel9UHMEuI4zKdyvWFrjlQAKn61G30PGh2pZL4lAFRlcrWqIpigOOFwNACbiOWKPLb4RMXKZd7i7SGzE97vWYjJ2cTjfOj713biNrsL_F2GdSNT-KxAUuduahGvjCwCZ5YTQO5guhP8abH1lSaPpNHi8oal7Zv_CFft-Jy-GVQqJkhTCvSeouf-6E1eyh1J1hu80XPzG9c3GF_MuGMpd3wVb1CiJ-OQ_V5-Cjupk16eRJgviSKxuLQlEqkoAnTyojGLdu5DeS1uPfM6h2nbZJKHkp_z5UwvSP0TGcgsZIDD-PqFPwlV568LEtaqPy1b1bXioKg1hr6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/MatinSenPaii/4994" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jRFj0GAkGamMYpIZ9XKGSZDl_vxsUlTRXnBGEH06K5X4jqtAYpZKEyFzQc1KnTFKWqA-rVpd0598WA2ILecXdEoaVpOaHpmp_N6a6-PRAzgRuCnCZw3ocwIBpbCSKFfWNP6nOFnou-LMXZ681Sjn7QvSYMVHEY16BKIfYNn-RjQrQjQT2AB1d9gnqCImfxb7hM8UYLiy3CbyDW10epFi1Bq0klNiRGlwekc7g522NsNFIqejaUo7mPUT4vecQKJPUnjy08A1BNDlcK5I5HNHietT4VxPoFplcIZxLA7FZvPgtuk5vEdvti-3H7R4EBY4vOwBSHKhqCLHYdpuIY-N5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرویس استریم شخصی هم نوشتم واسه خودم که با نت داخلی بیام روی Kick
(تانل rathole
😂
)
هاهاها
به من خندیدین؟
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/4993" target="_blank">📅 08:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HOALewAFSlM7MBYJk1c2woz_EXO6ddOFPcIIJI4UcSeoT3SEGDc-snx7TunVKEGjD4xsi1qQ1XN6HdpgnrHi5pKUZoIleKNO4u1ZHTdLWdPQp83oWumjL9EYm89ET4nzZL27VKqzDkIZ7WHj6y7gM8hKkhsS9sm_pZ9mJg2S-0EVQj29_o8QUrHBic_UxL9A-NOJPVzGQ2A_ld_tNxjvYUv0OCfy9PM1pb0H3GPtgN0vxGg_IVwulba1atsorNr7iLbVk2yv2LKpd4rVtWfl06s0GF-SLL3t6wREapO4-KthIP4AXx_fv08_bdiCYD1YZdVx8m2qJ1Ovk6z1PzCa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربه من از 5 روز کار با OpenCode Go
https://x.com/MatinSenPai/status/2089928470801318139?s=20</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4992" target="_blank">📅 07:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T0NHe9ZuHqN0GXnX5B3wBqXEiFoxaLpD0NkCcoSv-HEffUoDLC292aFsJ1P85axmpIRapAvIv4u61SDHiEPeO2Ee_fzSB1YALq32_XlreKTM8-bTYaCZEl-T91LNaccFEtF1ngTG_PI-SmOCN3VH0jxXxXpyrUtsyT6KrhG3khDxrIjaBvGUhonPNIXn32faWrEEeA3OTb-vTgw9BttJfvVn1L0DpYDagORdqzMoHhKP5S0XpoQDiKK2GvAtz5DdsSTEvfB_RSrcVKJYiiXmQSCFNmLrrOloRpDdsXS0eYJVNfvs-A1rwz0gPc-o7lccZZTzX0XCvFly54M_hoU17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پنل BPB + متد پترنیها + Chain Proxy داره بهم سرعت آپلود خوبی روی آیپی ثابت میده</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4991" target="_blank">📅 23:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">لینک داشبورد کلودفلر:
dash.cloudflare.com
لینک ویزارد تحت وب BPB جهت راه‌اندازی:
https://wizard.bpb-panel.workers.dev/</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4990" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lUBgtt-7a49xBRb2g8XRA5QoNiLMdATZ8yy5CutvlBUoD6cHCPrOiS8gLS-GbUB3RHzt7teyJBpzpkxW_RshsoCC3va9wnaYncTGr-9xo-lXDLYp7rybrkbKX1SgFyYSt48zB86aLtIh8qURz4wBDXtY1FAmRJMKjLrXxsjgGYELYAXw98R0if1rTiUWR9pQRzRyedaPpCaqNLCzngOzcPMF1jDT2AaBGAivlapnveZIuZ_6S2x5mjP5XgZJO7tjFp-rTnGPwLpRRmcB8XlY_Fefh1Enoq7A4biyj_l--ZnCI_uD2ACgJpcvJqjVRyvBso7p402thJqaxe_8Vb6N5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
ساخت VPN رایگان بدون سرور با پنل BPB! ورژن 5
🌊
⚡️
لینک‌های استفاده شده توی ویدئو:
https://t.me/MatinSenPaii/4990
⭐️
توی این ویدئو بهتون یاد میدم که:
1- چطوری با پنل BPB برای خودتون VPN رایگان بسازید
2- روی گوشی و سیستم چطوری ستاپش کنید
3- و برای خودتون و خانوادتون، از یه VPN امن استفاده کنید
ویدئوی آموزش تنظیمات:
https://youtu.be/7G9Fjhe_NxM
ویدئوی بالا بردن سرعت آپلود:
https://youtu.be/dQKfkXnThCE
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4989" target="_blank">📅 20:46 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ویدئوی BPB دیرتر میرسه و می‌تونید اداره برق رو سرزنش کنید
😭
😭</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/4988" target="_blank">📅 19:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cXG7mCS4LzTVA91aPiQ2ttWbi7I1KMMsleGvm6hrUf3_UYThnN7CuGUbyMmBthkCcjeYNZDcWZrewRzjvhG_ociaDGlqG0TQtiZIR1dNkPmPdlw6o5bm0Ms7pijENXZzn_we9yUwvDabveWEwigW2ocUHC30gyFI5chrVPoYDjs-aQmg9nFPiowhpWiM2gJ9gSxoQmqebgTWlITjy34ZJMaiPVND1S4vz18A49z6RnGNGbRi0nVQt5l5RqVN024Any0Ib7e5XNrlGHhuYYKzD2x4bLYo3oQwBtABdJepkKIrElhgS95pP69F2T8cyjnQgbxqBPkHriKuneV0cV-1Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteVPN دسکتاپ هم سرعتش عالیه. تازه با ساب خودش هم دارم یوتوب می‌بینم</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4987" target="_blank">📅 13:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.5.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4982" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">WhiteVPN V1.5.0</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/4982" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgkLtl6QUnO07MJqkswAUlg5yAC4AFdVsWtPtCYWacINXz7d_cYpc7DdNcNDdLKLtFD5dE_iAxvF0A5wAocXdsz5k7mJFMtXHy-hDiVn7gNWVYE6ZggtLEL-yW-tn9zo55uTiqH4qb8ry-dVzwFkoERWEx2RxGweInaHZzlc9kN54z72qq44bVS3ZCNnArw_YKsho2njct12PKn5-gwSJCviUjbLfARw6tKnmhZk6jMsBh-Q6-nrRUlyfu_eGQ8Gs--QIfYVMTySB9bw2vAbH2nyOhCM7CxWMM7wPzdXu7ViDut_jbdzfVWCdz1j7zs9-xhH50yt_RxEmGuxRx9oFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN v1.5.0
توی این نسخه سعی کردیم پیدا کردن یک اتصال خوب و سریع خیلی راحت‌تر بشه. اول همهٔ اتصال‌ها بررسی می‌شن و بعد، اگر دوست داشته باشید، می‌تونید سرعت هرکدوم رو جداگانه تست کنید.
حالا می‌تونید زمان، تعداد و حجم تست‌ها رو هم خودتون تنظیم کنید تا هم کمتر منتظر بمونید و هم مصرف اینترنت دست خودتون باشه. ظاهر و بخش‌های مختلف برنامه هم مرتب‌تر شدن تا انتخاب اتصال، عوض کردن سابسکریپشن و پیدا کردن تنظیمات راحت‌تر باشه.
⚡️
تست اتصال‌ها سریع‌تر، دقیق‌تر و مطمئن‌تر شده.
⚡️
برای گرفتن نتیجهٔ بهتر، تست تأخیر حالا از سرویس پایدار گوگل استفاده می‌کنه.
⚡️
تعداد اتصال‌های هم‌زمان، زمان انتظار و حجم تست سرعت قابل تنظیمه.
⚡️
تست سرعت دیگه خودکار انجام نمی‌شه و فقط برای اتصال‌هایی که خودتون بخواید اجرا می‌شه.
⚡️
تست تأخیر و سرعت از هم جدا شدن تا خطا و تداخل کمتری پیش بیاد.
⚡️
می‌تونید چند کشور و چند نوع اتصال رو هم‌زمان برای تست انتخاب کنید.
⚡️
انتخاب و مدیریت سابسکریپشن‌ها راحت‌تر شده و از صفحهٔ اصلی هم قابل تغییره.
⚡️
صفحهٔ تنظیمات، تونل تفکیکی، اطلاعات اتصال و چیدمان فارسی مرتب‌تر و ساده‌تر شده.
دانلود آخرین نسخه از گیت‌هاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/MatinSenPaii/4981" target="_blank">📅 13:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امروز ویدئوی پنل BPB جدید رو داریم</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4980" target="_blank">📅 12:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zovsa_jXwMRBXVqSntC6sq-p0FgsYXKRT6P0BzMSY_DpMIgnQfO_U4bU9HrBhDMXS34Jw91iq54-F6oQj4DLFzXnqA_paY8wp5q9dBIrekuyZdIts7bDF1Y5e9dywjZeTQLz9LTSE6wYJLJZfLhqrvyFDjyjMuZN2LZSGAYgMSy9alEOrXEUuUPEhUFulg9mX9a1mCqlmlAigN_BCrrNAr7g3qQVQ2cjZMeShgZZyC0PGH4ibBrv3NL2apk_AWlpRsnPM2jmyYykn6arB-ZzlRxlt9wl7wTLQKCp-qabX3xnarRJMcutEwLNX3y7gxZjgcciPUJ6rVopFXB5hrjyTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمتون گرم بچه‌ها
مرسی از همه‌ی کسایی که اومدید
شبتون کانفیگی
😂</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4979" target="_blank">📅 01:36 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بفرمایید لایو
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/4978" target="_blank">📅 01:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اگر دوست دارید استریم‌ها رو دنبال کنید، جوین بشید:
https://t.me/matinsdungeon
امشب یه لایو کوچیک خواهیم داشت که کمی گپ بزنیم و صحبت کنیم راجب اینکه قراره چیکارا بکنیم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/4977" target="_blank">📅 23:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DfuX-kIolrDDGbM_csCCbWK3nFq7mL0NaCRzUGFrgUilGrl1DExR7YxKZeuqXFEtR-8nQPOxDtJRD-xGyLs1kaVyS3Is1YGfDMSf1uzeXoZLx3d4p11vGao3K598k3jraWkkoSpjQaTLdel0U5KF-A1gjnWzzxwFgTFcir2JHbG9DLclL4jW6LrpXMV0IboCfpCrFG170_DlToeSZ1kmG43GWm_vf9jKaZ5J2jGtyReBqdOjkW6CZqvwND9eFlINAvuh9hIEQkUQx0mMdZNPVeuK600zYYEkptcFFDaXD3uzaAih3dviawLcABafuZZCM6Lx7tuWmruwyR_WYw68JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ریپو رو یکی از بچه‌ها واسم فرستاد که دوستش نوشتتش و جالب و کاربردیه، برای گرفتن کانفیگ رایگان
فرقش با بقیه ریپوهای «کانفیگ رایگان» اینه که فقط کانفیگ جمع نمی‌کنه. کانفیگ‌ها وارد یه
pipeline چندمرحله‌ای
می‌شن:
1- اول duplicateها حذف می‌شن و ساختار و endpoint هر کانفیگ چک می‌شه
🧹
2- بعد اتصال TCP سرورها تست می‌شه (سرورهای بی‌راه حذف می‌شن)
🔴
3- در نهایت هر کانفیگ با یه درخواست HTTP واقعی از طریق خود proxy توی
۳ دور مستقل
تست می‌شه
✅
یعنی چیزی که توی خروجی
verified
می‌بینید، ۳ بار واقعا کار کرده. نه فقط روی کاغذ.
🛡
اعداد و ارقامِ آخرین اجرا ( که خودم از روی index.json چک کردم):
- تغذیه از
۲۱ منبع
(۱۶ تاشون الان live هستن)
-
۱۰٬۵۵۲ کانفیگ یکتای
جمع‌آوری شده
-
۲٬۳۶۲ تا
هر ۳ دور تست رو رد کردن و وارد لیست verified شدن
- خروجی‌های
verified
،
fast
،
secure
و
top100
(۱۰۰ تا از سریع‌ترین‌ها)
- خروجی برای
V2Ray/Xray، Clash و sing-box
— اپ‌هایی مثل v2rayNG، Hiddify، NekoBox، Clash Meta پشتیبانی می‌شن
- کل سیستم هر
۱۵ دقیقه
خودکار آپدیت می‌شه
- فیلتر
secure
شامل forward secrecy هم هست و لینک‌های بدون اعتبارسنجی گواهی رو رد می‌کنه
🔐
لینک پروژه:
https://github.com/0xRadikal/Free-v2ray-Configs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/4976" target="_blank">📅 23:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C0S_gGOZWM1vSE6-ekoL6e1nFPZbEU4hTzZZOi13BQiYTQqQuPzYP8D5qvhxAXsjrmRCYwgBdFVK2g6zwiUHrcpgBpGaNL3BduT2s9q25hQCnnoxbJqlxnBOKVLQ7jI1QomuZYTPunpq1PTnxsdPgsyNRIciHWpjAGjkPF3fpJBuH1lqTxxudUxmrNbakvE3B4XDccOwUG9LI08gyVenL8aC5n6GFSMXADra5JbkpE0ZYpi9LUXXH_2rfNH0knyoZIdw6_RqamUQa_ANlhJ7TV-2ocXAWSs-kgCmzV3CgI-u_OKGDma_530UTy46QR02V969OPn-IFy0Pq6W4MAG1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته‌ای که من فراموش کرده بودم توی ویدئو بگم، این بودش که برای حل مشکل آپلود حتما باید Fingerprint رو روی Unsafe بذارید
عذرخواهی می‌کنم از همه بابت بی‌دقتیم
❤️</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4975" target="_blank">📅 17:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IjwUiLtxT4m2o057qrOZr3JC4mxI7GRDCaePdySEs-kRMaYGiqySaqjaiifXWZKadD_pNJkHesj5floeuEAZXd5vjfFrJR4AQ1c5S3RDfKpMOa05YCRO4GHMbAdtHiwsX3L6mScQB1uhHZ_uZa8kxtMr8Kp5WauhrRGD2iDgThZgYjPQ_Wxf3G0IbwLlkvtBeet09zfTASu6O6stSwyTVFXeC-Ogn3nTujX41XhwYxYR2EiwG1e6ttpScUNujiwn4wlKflqgLBr1foJLrcr0m4pvv8mlxoKb2rKDRnQBmQHUWq7sWd5QRlZgho-peHIFcTTiSzrUEuqnWuVFuGm81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب به سلامتی تا ما ویدئو رو ساختیم رفع فیلتر شد Worker اما هنوزم ویدئو رو می‌تونید ببینید سر سرعت آپلود خدایی که این متد پترنیها میده
🥰
که وقتی ویس می‌دید دو ساعت صبر نکنید آپلود شه
و متاسفانه ممکنه بعدا دوباره بزنن ورکر رو فیلتر کنن</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4974" target="_blank">📅 11:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فایل و نکات مربوط به ویندوز:
https://t.me/patt_channel_x/101
مطالب اندروید:
https://t.me/patt_channel_x/91
اسکنر من:
https://github.com/MatinSenPai/SenPaiScanner
آخرین نسخه V2rayN دسکتاپ:
https://github.com/2dust/v2rayN/releases/tag/7.24.4
اپ PattNG ویژه اندروید:
https://github.com/patterniha/PattNG/releases</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/MatinSenPaii/4973" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bJXT2mwYCupwVfXfrt5hQA_AvnOJFDKU0Hm6vjQzS-UcvkqOuI3mFq2Gjvq7GYms4K8DSXstrZd4d0LVdH12NEiUyKtFOGyv48LurAra0G6dx8fitPl40SbyokJVUScMKoib12Z2h59ZQzY7mjf0Wk-b3udH_27dIQG5-5vIBVNmn8GooA_mg5k4ivC9bGnJ5xggLxkq0TO84ytwzWAEKGFKgbHDHmgLVGwHrC4GPrcbgabQ7DwBMBA9zKCUbjY_2BpglPUgomrm5MO3Ko-BwVby-p8806klPo2AI5B8K1DK0RcbB5kHBIW4n2yjr1DNOFLh3KE_E0c_vwCjZtImnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
رفع فیلتر کانفیگ های کلودفلر + حل سرعت آپلود
⚡️
لینک‌های مورد نیاز:
https://t.me/MatinSenPaii/4973
⭐️
توی این ویدئو بهتون اینها رو یاد میدم:
1- آموزش دور زدن فیلترینگ
Workers‌.dev
با متد پترنیها
2- از بین بردن کامل مشکل سرعت آپلود روی کانفیگ‌های کلودفلر
3- استفاده درست از اسکنر من توی این شرایط
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4972" target="_blank">📅 03:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4971">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ویدئوی رفع مشکل آپلود کانفیگ‌های کلودفلر و دور زدن فیلترینگ
Workers.dev
در حال ادیت توسط ادیتور عزیزه و به محض اینکه تموم بشه، آپلود می‌کنم واستون</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4971" target="_blank">📅 23:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FCEeuoVXXqeFfZDHudB9Nn0blyAe1uWXN8eytkt5VAhr1g-O_Py0y2aaxJ0rfQEnikVJ7tI_d1JKogWpsAmCUOcKAR3V7nluU0fWX38fKWC3piTZ_XOakdxN3QE-kZjkQVX1VVVtaIggOknGt-LVU2FDELxlFZq3CTCdM6TzdbOUYMBPFbWQcOPp_ngJl3-KW8_vaKeMm-Yq8-CPYMqYPRf2YIHVEkMDkOBoFf9m8SKZJAM3RrTRVW7ovZF6b9W3PbzS9WKMUfYsc-cpMhMSPVaXqAvH1rzPsrj1yVDfhrwPwT1w8XKHO_JJmrl9U1Mt3IC_qLaDZOgYfzoPuM-2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزهای باحالی قراره داشته باشیم به زودی
🔫
از
🟩
می‌تونید فالو کنید اگه دوست داشتید:
https://kick.com/matinsenpai</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4970" target="_blank">📅 19:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">با این آموزش، نه تنها محدودیت سرعت آپلودی دیگه وجود نداره، پلکه پایداری خیلی خیلی بیشتره روی همراه اول هم هستم</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/4969" target="_blank">📅 15:25 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WXVq3Ulybj1KSRD7ucjsD7ffpuILRT4aIy10y1WdxzHB94LcrgDqj5ZbD0DohGXREqIQdipgU1rnkoPPobx1lA-Gv6y_fydRIBBPII92OXrfcj_OZfaXpjCj19zLoL9xvHUJKinE4qyhrPqlm7JgpWsL4TjlgDOgGA1B4h4XQCoWE9hzFa6rsnLStm2vz3jk7posrGKw32LGnd8qcROdDc9C1kxPNZ6hSv8kXmVjlg5fAQYRPJxnyD2ghnspBbYKUI3jp6aaRsvGFZdZ8nqA4Ti2EJoAJqOzoiKBcTuWH-sPukpYsjW5dAxnlKGTAe66zpc2tRZfVDMpzDBwSuVzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4968" target="_blank">📅 15:10 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eYbw0ia-PRIzyVT7A0c8cHPGoWgxLVvz1sUfS9b7xwh3a1IkN8TsgMvxjBcED9_YKxzC9U-lgw9hi-E1e7uDmMbj5fS5VCPwPGmN2RAoGduvvr9AGN3l40NR0wY8mKhjhKTKcs8rH0sKUxVAtHakCP0RnWMGlX9onwuab1aw4WK4AXiqlulrY01291pMeMLwxxmvFkJ2f7d6t0pmVtohKfsDAtCWYKVgLd3daW2m_m3EOQujvLICIfeDJa30dLwgJ8dG0zPrTRsn-ouTBoUhYam2SPl70FefrxVza-htHAtuN4AA1yUMhDwgnubJp5g50_wZFXfRrsDkPL9yr5JbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4967" target="_blank">📅 07:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:  Android: https://t.me/patt_channel_x/91?single  Windows: https://t.me/patt_channel_x/101?single  Android/Windows/Mac/iOS/Linux: Use Xray-core…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4966" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">آموزش fragment+fingerprint برای رفع فیلتر دامنه و رفع محدودیت آپلود بر روی کلودفلر (ورکر/cdn) حتی روی نت‌های محدود:
Android
:
https://t.me/patt_channel_x/91?single
Windows
:
https://t.me/patt_channel_x/101?single
Android/Windows/Mac/iOS/Linux
: Use Xray-core custom-json-config and change/add --> address, finalMask, fingerprint, cipherSuites</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/4965" target="_blank">📅 05:14 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/4964" target="_blank">📅 00:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گویا روی سامانتل و رایتل و نت مخابرات و خیلی از اینترنت‌های خونگی هنوز فیلتر نشده Workers و بیشترین اختلال، طبق معمول روی همراه اول، ایرانسل و شاتل هست</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4963" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تمام #نکات واسه مشکل فیلتر شدن worker رو داخل این پست میگم:</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/4962" target="_blank">📅 22:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:  1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴): https://github.com/2dust/v2rayNG/releases/tag/2.3.4 یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید برای آیفون هم Sterisand آخرین…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4961" target="_blank">📅 22:08 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DMy1Oct8XARqvMsCYp9MqsoWntwbZhO3nFZ4-c-GeztQVpZXSVXNAZdC2fTR5Ry2hQb7fg3XmmUQB8wn9J-NH1mydNH1ps0Hpsvt8sVudzwmsoWle_wg7joITcSL68DS3Ht94-mUqu9DsDWpeRDb_FuaKT26tYOg63eLNvz3J5Awe0bt3cs6AKK1oBBj-hDcuTfp9LMAzlL6b9NPjmOIGnZQ23x0z5xGLBQSFd984cOWt21xmS5NcFAT9NAMSP50ypbKzS78M6zQNJofdJKQ6iblhI6V5qA1Ah6VpKR4Ve7rOGVh480TjWh_PEoe2bY1EpejaoTCO_S4QHAlFx0S-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حل مشکل اتصال به کانفیگ‌های BPB و تمام پنل‌های Worker کلودفلر:
1- آخرین نسخه‌ی Pre-Release نرم‌افزار V2rayNG رو نصب کنید(۲.۳.۴):
https://github.com/2dust/v2rayNG/releases/tag/2.3.4
یا V2rayN نسخه‌ی 7.24.7 رو از گیتهاب بگیرید
برای آیفون هم Sterisand آخرین نسخه کار می‌کنه
2-
این پروژه
از دوست عزیزمون Hidden-Node با الهام گرفتن از نکته‌ای که Patterniha
اینجا
گفته بود، نوشته شده و اوپن سورسه و کانفیگتون هم جایی ذخیره نمیشه:
http://hidden-node.github.io/proxy-builder
3- وارد سایت بالا که شدید، روی بخش Fragment + Fingerprint کلیک کنید
4- کانفیگتون رو کپی، و اینجا Paste کنید
5- پایین، روی Enhance بزنید و بعدش کانفیگ جدید رو کپی و توی
v2rayNG  2.3.4
v2rayN   7.24.7
برای آیفون هم Sterisand نسخه آخر
پیست کنید و به راحتی کار می‌کنه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/MatinSenPaii/4960" target="_blank">📅 21:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/id2kgvi5_2kO-v00lZwM6ZM9HXCJtwKf_tOQqcympeL1RCVFPX8Tlw5Sr_RKdrrU1mwJOmw7Jn8nlsNAS4fGXkbe6A_UaQ1vjMynWBmWuciMqJFaBtJVFBNk3gA-BIgbUm37lyYPUu0ZT2IB1mSl21fm8SxGMFDvys25-GkE2TBDh_m76hAwezZcLD2bMoPLFCLRyE6r7scW1hhG5NdtNWixaiMjrRByVMs36B4cP5DalMRNwiRjCIfBk40CTVXPbY-ASI8LFTzChPt7cPO1wmtoAC-IYxX2KeU11v2x1s2wlNRCmAn86Yzccu-enLMPL2OpfFblopwwSdMVRkcpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست پترن عیان شد
پنل ما جوان شد
مشکل رو حل کردم با کمک Hidden-Node عزیز. الان آموزششو می‌ذارم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4959" target="_blank">📅 21:39 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbZYFVd91Pt6Y9aONgawtCVMqy9_UVFJlMMLG7ABPPdsBvEu69gH8WQ7_tWuyF9u4bvMnMzqEEWFp6Xz_49S4Ap-LebzaAePTElK8PcWSVEzJQmZ5FGNPTc6Y7FkqDaG_oeAAaYPvXRuPYTwzFHX11wCQrMR-2IFCkB3zfU5rE5edJJWtT--xkmjl1T_5CPOSBNXfCP0uP_OsVOBNhpupzoeAgHyKLQ20teHuv5ORsuThoE2HMpVSzKxL9PmC_YGUrc2ano5KkqwIchyJcTAHhRoDaM4D9IZu8tXsnShP5ZEuzDFoCCu1jgfq2zXwdb_ATDFKYXuVx0612Tx5JvzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
چطوری فیلتر شدن BPB و Workers رو دور بزنید؟
میتونید با رفتن به منو تنطیمات، فعال کردن گزینه Amnezia Noise فیلترینگ ورکر رو دور بزنید و به کانفیگ های ساب BPB Warp Pro وصل بشید.
این مشابه گزینه فرگمنت هست برای Warp pro و Wireguard داخل اپ WhiteVPN</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/4958" target="_blank">📅 20:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=VYRXWhjcX2kn85O_ZQ_iz2bcKGMpHYOg4gvi-en6iw6azvb25xlHJzKDgIK-JxOpE-lj74CoBrTf34SwUwJp2bnVvUf6Eube_NReApk_s09HgVT9O9Fbs0OUJQzrBaDoIXm79TaO5Yt_RZpbEJUTH9QvK_Th5b_a6ujQY1fije2ZNw-c-_BDbaQhfZtG8FZt4jzqDuvFvkQnwswFWf8D0VE41aLWoNzXt2e-sFx7dzNdHUA14REnnZQn-gTEiLdAqusmu_3Le7MWnMnxXiLcCxrRj_oVfAh0vrTSVIPRSYqjsb4nep8KAEC4QGmKJ67UnpvMcQfq_cW__NM_6kwQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dc224c1a1.mp4?token=VYRXWhjcX2kn85O_ZQ_iz2bcKGMpHYOg4gvi-en6iw6azvb25xlHJzKDgIK-JxOpE-lj74CoBrTf34SwUwJp2bnVvUf6Eube_NReApk_s09HgVT9O9Fbs0OUJQzrBaDoIXm79TaO5Yt_RZpbEJUTH9QvK_Th5b_a6ujQY1fije2ZNw-c-_BDbaQhfZtG8FZt4jzqDuvFvkQnwswFWf8D0VE41aLWoNzXt2e-sFx7dzNdHUA14REnnZQn-gTEiLdAqusmu_3Le7MWnMnxXiLcCxrRj_oVfAh0vrTSVIPRSYqjsb4nep8KAEC4QGmKJ67UnpvMcQfq_cW__NM_6kwQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
دوستانی که فقط با فشار دادن دکمه کانکت براتون وصل نمیشه یا سرعت کمی دارید، از این روش میتونید تست سرعت بگیرید و بهترین کانفیگ بسته به اینترنت خودتون وصل بشید.
توجه کنید، هر تست سرعت ۱مگابایت از حجم شما استفاده خواهد کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/4957" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.7 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4952" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/4952" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcHjGKWrGOtINiNxqTCjM3mnksxyBEFvVMMczayqOAkdd0nS2GGSE2jr4xQG6EGnEuKIOmU_I4xdaMB-_iykNE0YlJ8jScsZ9xUFYNWocJlOOVN7DbTJsiXxt9rbAJe6NMSemJ53xzuzDXDgEAGm_cw0EOct2OD45uBcEnA2BH1e9jUr9Y-j-2KttfN1aVWhBLZbAO_gFNd2aEfdm0bXr2S_fFebY9Zc5700UbR2Xp7eXsGroJYUqqqRyvl9ig8e0vuEjkv80f6DlhP16p9L2g7FUpEly1nmaBq8evS_eu8gDjfe6CmLi-5xeyIVcb-k78Qgkj400VJ9Sa7B6zZTQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
انتشار نسخه WhiteVPN 1.4.0
• ظاهر جدید و مدرن اپ
• بهبود اتصال بعد از قطع شدن
• حل مشکل VPN Mode & Proxy Mode
• بهبود تست اتصال. حالا میتونید کشور رو فیلتر کنید و بعد تست کنید. تست هم به دو مرحه real delay و تست سرعت  تقسیم شده.
🌎
دانلود آخرین نسخه از گیتهاب
https://github.com/WhiteDNS/WhiteVPN/releases/latest</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/4951" target="_blank">📅 20:35 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اپ Defyx وصله
متد Aether هم وصله
کانفیگای رایگان MahsaNG هم وصله
کانفیگای مستقیم هم وصلن
پیشنهاد می‌کنم پول به فیلترشکن ندید. defyx و mahsa رو هم از گوگل پلی می‌تونید بگیرید</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/4950" target="_blank">📅 18:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xl1tSDl_gdUypLgKZmZqg7ndXVN12CapfeufsQ7Dcxlncv_b0SeFwej1YwE-I5src79KOyDtfAtPeNDqy8REuMeCflDx02M1yUoek_9HK7iy3VZ8qQlU_OyKp91veqEFdSm5JHVY6XupVZZQ6SXhyeNq9idrgbWT84c6UAjHxup_QiNEJsO5d_sIB8ac0C2igt2Ij9kchXVHBXjZHEl3kus6C-7evtRPtpUOtUwfsmyAm6kUPYV1XAaLcW8Fee8A6qK3KMA9JVqwDuFrSK_ExZoZ1QdpAHb-LH8E4PXUjCMlTf4n8QdKHtzOcQOxczgPJr_tclnW3InAooA3tUgOqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4949" target="_blank">📅 17:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پروتکل MASQUE از Aether-GUI متصله. از اینجا می‌تونید آموزش اندروید و دسکتاپش رو ببینید:
https://youtu.be/2h6qlA1pJFw</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4948" target="_blank">📅 17:52 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/4947" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">https://www.youtube.com/watch?v=EZ4q5V6fZh4</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4946" target="_blank">📅 17:30 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">من خودم به لپ تاپم دسترسی ندارم الان. اما Sni Spoof باید جوابگو باشه قاعدتا. اما اون متد تغییر دامین رو هم الان چک کردم و بستن</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/4945" target="_blank">📅 17:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WKAk7xsZXZVU4QnJsnBamIlqySn4axsofLr0jd7QczvB0wlIzN-RNZ3rlBzXS9LPShpS7ha9pMfCMp0SLSWIdCehFaNraW9H3uTU66K5VQojoPS_iA0bYpHIsXyMVhm7xf0L-r5zBe_mLrMnIDJOnz1xIar3YlPCwpp-GjrYZGKMt4uoEfwYYplfqHOueCL8pIP5zeF2KO4vrvKWunykCVx1LhsgVBJ1kC7wQ_P_MDVmNtOPpZZNSO3w1zeyeqGKu3yvFQJU2siixhP7h1hRsVI4cbsPWcCkDTSdIlCn1eNlRIjfBoullRW4quPuv_9_97e4X8MUGbFKUAbmaXz1Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W64G_kqIC6bhkhOl8cLzIWeziUwLvOSSsCJa5U2XHCorPxBYyZKxXjlg0-cLu3SSopj5zkCGpnNFnl6CQPEK9I_dMwnOgXUOvmVYc_U_Y3McaHnbgp_MgZ9qlcwNIlop9ps8GwZE-BfEsMShc0Vdoo1uOZDMLHk79hRfie4KyAq1ZF_FfsfolyeL-8cwTm8W70ypWRnHjFBYm0YE4l15stnTU1xTgmB-3kejJUVqf1yA8BwLqzS16ahNj4fhKMssQ28Fp9enHFQxQ1pYK8ROFHHoD2EdARVKez16xTzyhSguJHntyqZixhlBcMpTlnR3SUQ7y64TLCQmknlrwP-hRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد فکر کنم که ساب‌دامین‌های *.Workers.dev فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4943" target="_blank">📅 17:21 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از صبح داشتم پیاماشو میگرفتم. الان برای خودم و دوستام هم قطع شد
فکر کنم که ساب‌دامین‌های *.
Workers.dev
فیلتر شده باز. بررسی می‌کنم</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4942" target="_blank">📅 17:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-poll">
<h4>📊 کانفیگای کلودفلر شما هم قطع شده؟ (چه Worker چه Pages و هر پنلی)</h4>
<ul>
<li>✓ آره❌</li>
<li>✓ نه. وصله✅</li>
<li>✓ نداشتم. دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/4941" target="_blank">📅 17:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">برای نجات یوتوب فارسی و درصد تشخیص ویورها، برنامه‌هایی داریم. و طبق تست‌های کاملی که دیشب گرفتم، خبرای خوبی دارم واستون و توی یکی دو روز آینده می‌بینید دوستای خوبم</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4939" target="_blank">📅 11:59 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mnYXEWE0CqclzKTTxO8XtBD5MYcKBDcU_KtnTB5gtTsQS_zRF4eXKlkKJ5luVPLky8_5RAYa2zNpfKaxrjk6f_JjCrmZ8foVpUb9L2pxpxGHmima1lA1a5HQtNV21yr6KABohMwN1PeEu7scf62m1pDX4tz21zjpkJ7lkAg05rj2n0dZi1JAkAHhexTBM5dJqv26Uxef692ObYJZkvBcwG6kQcEVsKyJi2HDyY6NR901aO9uXKfSQzpNv28jTvcq4ULiczHQ1hCF8ssB13UDYnKZ_XRsi2oawtEY3BwuQjrjUhQc8dDJ_XI6nn2xMr2cyw23_I2PEzC396HiQRzZvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/4938" target="_blank">📅 23:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jj44XCTLBYoYqWsNJ8TDFibOLYnrZWWDBlq4gqA2DnaOZ5OGSWVGi4WcMS-Njok-pZOxj4_3bJjW92aB9KIszmvnCw8E68Wg_ayo6ZtZMa1JKKzjIGtJxOB8gKwIHleA47MDj7fy7I3q6w5WqWG9a2Ynax2wnOlIHf0ki_xUDQY6sGElSBMypzGHYVNn6rqE66-D3d9BFDVx3p1prGbuzzOtYjTeYo0SJtvPzdyx7nCH6tYTzrwIIxYb0cTknYl6rTrFgayPoH9ZryJ1PhxVTVHpHt9wPgC57llY3tQanQJSuKA6OS_OZKv7D7HBMTrl7P23HVxqVOlyQxPGAKBzvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/4937" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به همین راحتی.
تموم شد و رفت</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/4936" target="_blank">📅 21:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4935">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YK_7ctoIiEiXUe2Y1tqOLLdcWuF2P_DvU1vNBOdP39Zqso8N-S02Kb3XZq7qqnIVkwbSC0ho6NnJCrwOgXRN15ysGfvIoVZnMlALjFFmoTGaLtpCFCnz01bqTKHjusVJqmfF5w0_PpZVUAVbZQnrrF-f4R2VG0o7JEXrfYhDOU3eN8MOvLZ_rD7hcl3Xf0fI5zX576sZLUhXv0UCXVg6QGC0THWW3eoFOdz_Bpu5jT6Y0YPgT9ns-0sGdp81Sxub6mjpVDGFGpR5qWr3dX_b5y48l9APH60DcGQEQgWJcmVa1EpFkECIOdwerP1RhF-oBwzMxiX_qU0R2ij7rAT2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط عادی :
•
دانلود آخرین ورژن WhiteVPN اندروید
•   دانلود آخرین ورژن WhiteVPN دستکتاپ
شرایط قطعی اینترنت :
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین ورژن WhiteDNS اندروید
•
دانلود آخرین نسخه CoreForge برای آیفون
@whitedns</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4935" target="_blank">📅 21:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4934">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h-hZNoXOvcWiDEaGsYYEnnB8VpF94M7DU1rzH_LUB-WtEJkuNoG-ZfJ-RgeChHg0Gr409gvMjD_mXYuwSa5b86Sy4yRzB9t8bOp7oCqQI_I0D2e-74RY2VOUVkyoW3Hhg38FF8i2TeQ8lLTiRk1zrv3E_s-853_Dhok-4jCidOZwT6WY4CHo7M9wGVNaneWmDlr_kJvK-3rQA0lKeS9IbXPFr8FSW5lFwN5A4ckfRollboB5cY6RYrAFxloM0TuZlk1B7iiy_C2TOB6Vwg28v7vCErhgOvr8LH0QklqcVc1xaVdwpsrBq_flzs-ciCCgoSpQWIWFeoy6m-M7CGbhUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/4934" target="_blank">📅 21:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OfBf9_sOuHgfcqtFRZantS-v9ha-M1wxfoybeCqyippu-lss4R5KNSNU6rEt219FmUWZg8w9R7QLXPPJEAxy1on0B2nFJgdfZmQs2kPBS6M5m3ZGHQ8kBwekvvruHjHlAAVWTVNxtWZqEVTUJQI0HGG7bX-uvAHbj7S5Vay_Rs8O6l0Wbs49_cav9CqwUA0_dQ5400E7LReg1F1SBtOoZzv7XEVjJWOgfPqatXXQ6Yo3c7E556nhWHr1o9b_glkS5KteHACisINtycvQzodR38S7JTElfWPcGlrQ820CcbBjz7BxSFluqo_1ODR6RURXFWZaxv2qwndhWvqVdOkvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود. باحالترین قابلیتش اینه که میشه Mode شخصی ساخت. و از معایبش…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/4933" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4932">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Td8HF4N6i5OisdLiulDNR_UqNDxPqZ_kOVlNQwDRnBteomA1Nk_G66rG9oO_FlGOgDxeBTlEtMtmFbIj8KSpBS0Rz5vUimufQEIEXxelfkndvnPuwfj0TTLRfoICeBwFSjJe1k2-iQ0caGozD33ulfaB7WTpp-bgpZ2-xhTMA1ShVaAPPE32nQd_fo-S9dvDzeHd5RroB0AWr7QgbtfbpPhQBX7ehtHbKWXlcIamNNbKPxL3ywWuN5oxDrljJGZnIiykKBwsmCyDBkIno_1icwdvnh-5hE3gMQ9wl4FxhYuemMzVx7SNVx3Peah2Q63k79ZMYHnMgao09RHOIYAJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپ سیک هارنس رو دارم تست می‌کنم، خیلی باحاله
محیط UI اش سبکه، و کاربرا هم توی ردیت خیلی گفتن که Caching اش عالیه. یه بنده خدایی قسم میخورد 4 ساعت باهاش کار کردم با deepseek pro فقط 60 سنت مصرف شده بود.
باحالترین قابلیتش اینه که میشه Mode شخصی ساخت.
و از معایبش هم که بگم، درسته UI سبکه اما کاربر عادی ممکنه یه کم گیج بشه
و همینطور فعلا توی فاز تست هستش
و ساب ایجنت‌هاش هم مشکل دارن
پیشنهاد می‌کنم ستاپ فعلیتون رو ول نکنید بچسبید بهش، صرفا در حد تست
مدل سفارشی هم که می‌تونید اد کنید طبیعتا. من الان OpenCode Go اضافه کردم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/4932" target="_blank">📅 20:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PII_y8FKQfJjVBkG4gWDYSynNozw_--hljLiit1K1iZlqNHG8qFuBTa05wg_4a8xC5kMNK8-OWYB73_ii_RJB6aNff7-9GEtzmhkW9F07jnleYp0uP5NjEk41ZkdTlC9CesUtMTGJOOA2lpLOauHMwnDmv3XoEILMNQzYqXZiu6g2x49eGE_4EZ23nqHEbz_Nv2MuzHA1K1w0fXC5xMC4W3d4GlyRYMorqX1MH0VXAMuHLIjELL0WLG-STGpGkRCfqIsL_mZrUy-xN2iithK7DujL34msIDwCLdFkny-JIBkdf851o28TN4kk3sJkIeDEIx95lyfVhXvaLyV3WVt4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عالی بود
😂
😭
اینو چرا پوش کردین مسلمونا</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4931" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔺
ابزار کدنویسی متن‌باز DeepSeek Harness برای رقابت با Claude Code معرفی شد</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4930" target="_blank">📅 18:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4929">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaO0TK5aTW7iEPCDwwAo8dTs8gKot3NRd8jN956A1JbFW2PYyusxNSKcv9u-uf4gNR4tG5MsQ2c1Iq32nTd2DnsQMsAqxBCAR2uniheDwjg-0erANN8Zz7GAc06jvW4AE2wud_dPawEqdpYnx_p-e6DJ9koE5ycxM__uglQlFBWkoX3e7ggq0wooNgcx46xzs6zheDITSzX8JedfettJgb1iPKn8qgeNpUX9qGVd5tcRiYP0ly2MbG3I8tV2upf3BpfcOxl4X-NIvVWxRZ8LyH7lC3A3sxJkMqAUOfOsQAJ1O3tR1IP0MaecAKZm0Bq2oY68xy5oFAA0ydca9jiQYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه قابلیت خفن برای هرمس ایجنت معرفی شده به اسم Bot Mode
به جای اینکه هر بار سشن جدید باز کنی، می‌تونی چند تا بات جداگانه بسازی.
هر بات پروفایل، عکس، توضیح و کار مخصوص خودش رو داره و حتی می‌تونه با بقیه بات‌هات حرف بزنه و همکاری کنه.
https://github.com/NousResearch/Hermes-Bot-Mode
@RepoFA</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4929" target="_blank">📅 18:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جالبه که من دقیقا سر Kimi3 هم همین مشکل رو داشتم توی کلاد کد.
الان توی OpenCode + DeepSeek V4 pro این مشکل رو دارم
سر دیپ سیک فلش هم داشتمش اینو توی کلاد کد</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/4928" target="_blank">📅 12:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/runLk8rOH5BqSh9ko6vUn5OzkQ27O6Ls7wtyHGFI-Ty0S4IJEhOlKWaSHLYRU-ZG-YfnfU2h_vm7WgU8UoVaFVO1MyGua6olaMTLRsw0S7-JEqcUScpMU3FqPfrljyVy5LS9ljKJnxP2NjtNM3hB6hqrviXZ5Dg53H7DgcwwMu1z-LuNQbSebjBxraBc3-E447eEaBG_V_pR1c9Z6KfRCnoyImUnttlHWx_SMcAD8y2ujUaglomZIGYMcWmekv8yghFC0-2J1r5zRwnbFO8wiSVvXbp5Va8VNFobT3ROBXV8koUswUTRNijxCv8OBD_se5slHuyKSd-bJcziGXnAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا عوض کردن VPN فقط باعث میشه که از اول شروع کنه به Think و من اشتباه می‌کردم</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4927" target="_blank">📅 12:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4924" target="_blank">📅 12:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4923">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vit8BLhPIeWxUUzbJrgih2eX1j4mji5iUVTxyzQHNAz8TLVe2NXyLkiUpvoU9fVuCZ_iVGh8tezcUu0454eqZFyMXQ_bFvGPL8zQP8NDMaPW7drmM1Gh4itQQV4tIJr64Dt7Vo-iMqWk2dCMQjMDYRzvlKjKtPhzCYffGoo45-oTT7gATkdN61Nz2DMgENdRWvrPbuWmyGWHvaL4_Sg_kQhrNa7SFM0dysF2Zmot2_uRgfkyiL5K92rkxucyzc9bdCmete4SL-AjvfeE3xfAxRddiSECmQn1VMIp5gRlGV2zBrrZW6L1njgIKgx0KEae1iEOsdFAKLrMZR4J3viMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان OpenCode Go خریدم باهاش، پلن 5 دلاریش رو
تجربه‌ام رو ازش باهاتون در میون می‌ذارم حتما</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4923" target="_blank">📅 10:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e9lnJgC2J8UT6aLwDYIPmfiXBgVN12wIcdtBRpa_9MM1A3lWb8wb-CWjGcH9PJQxZUCGZNXg2usJnb4HSn3hx7_6DSSf3-3sAqE9DQ0fAVmSikcta0vTb-gq0KE1bH5Ive_ApPH8pUQvDAzMJ1_vVJm7Un4PTOtf9Z9e6q7EWSo3RHhboEDjTk_D72X0KGdcmNwLiLAE0zG_PEaGGNgW3VK7IYlZ8i3CvfXgXJns0s7iEt9oRuIGEFAfq_bauvF6TrOlsYbb3CX2SyRbaVJdIJVzMoQuqgRbqsCb-KriOg4BMVDw0_KfBMTb9agEFQ9w_0Z-04FmN4rA5lIWE6k0Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از پلن فری هرمس که گرفتم</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/MatinSenPaii/4922" target="_blank">📅 20:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AsWXHYmVrvoMU6W-Gwss6dvbXFY2PT0sKYapRrrobS23cnOzNvepJpivpQWCOkiYFEFfuXaA1ilsRbUVwA9Te71FyaJyjqGWiZvnLDTi42LDogWNDADlEYcYMaWGY-JPswSsAS50A4__khAQltZxzQkaszBfYb60FCP-BHgdEOy75KcLrfL-sYBgO4hC9v1T2PimyqGFBPM1o-vkcrxlRZt4281VnlrPl8MaTP6G6r05hhWjBfSqxpfdTy6a-tyC7dFSj39xCCu7Sl3RESxeqjU13wPKMJx5xmu22AjzalIdaIkV4dfaL0GP6-nBP9kWAiVXsPFwpBUTJ3ewkAX5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/4921" target="_blank">📅 20:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگر روی 9Router+Antigravity به ارور 403 می‌خورید، یه بار اکانت رو حذف و دوباره اد کنید درست میشه</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4920" target="_blank">📅 20:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4919" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUN4pyue_DLrYY0_s6pT6bm4Vc79nSMjB-x0kihbFA0LKgr26vsOzEuyN6t3NoYc-4qeAWtVN7vo-UfDjT8hlZ0b3F9O32C7CWoQH7f5IL0ueNTWfA9HX3ZwhSwgG02KjVhqpk2EQnuMCsZqxGvFtX8pTD6uzjxGWWtwGBsVyIe78_nes83S8uzV1Rl_IYXiqU6DiaWdJeCtRUxTt7wHPRkWJQUoVhzSUADBHHHFllhJoiH5cehXnYoGMGjK4TkSLY5O-mtu25we9p6589NSGpNvS8LGG36CJSKjIZZKDhHUfubEHTMK8T-elJ0PfqlkasVIhQTZmBVoFnI6NDiMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4918" target="_blank">📅 19:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nJJsDOxWXAx8qmqv2wgpX--JDg7xozT2oB-nJfVlY5W8x46RuLJyD2YYEW2DandL49PYtSZo8fHUUxAIWnYHSZ8m4Hz9FnjT_-i_54fqPAS5vuZv93Fg6Bd1lkzGfQru4ahMQFQl99H71Caavcu2FreiS6_WCD0ubsCPP2uIOK56AHjvaJcycuRTnNCFklZSwd_RqJtCTxLl-r0RKH2huWc8sg1pP3e0JRKtH8tVAXGEZ3kzsAxUDuddoK28Jb_EOISilWjpyb7YmRGXwFJPMeHNV9QD9SRMXeJeU27drzOK9498NEIYvUyc7LrFMOZ3-piyFx1QxI5xZrRMthC2Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NOPT29p7Uv9Kz9ncY6MiuGubx-E6uXJmTR1Jgk3lNbQygBc_4h3lQQXgzzdcXzohkPdy_xSL11qprDGWjTmfklU15xbMvuB0ByHD3LZS1kbxOcPRKZQLDHM4xC8xIUECxeOYQX3EXzr7gT07Vin7eUhNYnjIdX44cMUpFnXT_PnxWipTwwYi6UGOkwF4f72EWZwllPa6iGmeRnWgBrDPPlgI833nK8HCxSvx5U7yJ9eU7z37B7XaFnBtK35FOgQxn9o5LCVPp43_uljb5_adTZAhC9w-lWh-0Q_kNqEiR4cjKQFFpNyUFW3sb-YPwndES-LjUXMksr9tQ-6bGfSWwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dYKjcitXXvU7lM-IZh9yHXeFX74YUO5SHzfYk4Sz8r7i-rs4PGHNXFRFVTnj6zmebDy1krzooEkK4RjOLnTUrdZodvMT9U6WtkX8Shu5WkiZUfA3H_WxB1iIpr6KfAHkdhyljwd9ZGzCy9W1EIMLCbEFhwmlC0nMXG4qv1KFmenZxdF9rE3LXiiu_QoSJ7mZ4O1JcUqg8t984cqUgbV1s8vEmeWXJCPKjTS48zm2ks0iSXRsKWOL5OswRORYVwxdeSiCvHpUBbflS8hFQ1DRrNjYcBLYv4Qq4V5-An2pxa9oZV5Ciyu3boGXXmPkmU_0RlSHMJEfjSZhxmQpRbNVBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی
خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید:
https://app.mpay.cards?startapp=ref_PzwXZ8
(لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید)
1- بعد از اینکه وارد وبسایت شدید، Next بزنید تا با تصویر  اول رو به رو بشید
2- روی Apply بزنید
3- با ایمیلتون لاگین کنید. دقت کنید که تمام هویت کارت‌های اعتباری شما روی این ایمیل هستش
4- بعد از اینکه وارد شدید، با کریپتو 5 دلار پرداخت می‌کنید و کارت برای شما فعال میشه. از USDC و تتر و... هم پشتیبانی می‌کنه. برای آموزش پرداختش با نوبیتکس و...، می‌تونید یوتوب رو بگردید. من خودم با Trust Wallet زدم USDC و مشکلی نبود.
5- تبریک می‌گم، شما Visa card دارید به اسم خودتون!
مزایا:
- می‌تونید توی تمام سایت‌هایی که نیاز به کارت دارن و رایگان، اعتبار خوبی میدن، ثبت نام کنید(من توی Nous Research پلن free رو فعال کردم)
- می‌تونید برای OpenCode و سرویس‌های بین‌المللی، با شارژ کردنش پرداخت داشته باشید(کلاد رو هنوز امتحان نکردم)
- و تمام چیزهایی که سالها از ما گرفته شده و ازش محروم بودیم.
- ایرانیکارت و سایت‌های مشابه، با مبلغ‌های فضایی و میلیونی فعال می‌کنن همین رو. و به نظرم 5 دلار، منصفانه‌ست
معایب:
- برای واریز به حساب، باید اول 25 دلار شارژ کنید اکانت رو و بعدش می‌تونید به کارت منتقل کنید. تنها محدودیتی که بهش خوردم همین بود
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4915" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mNl5rNrrVHyHhEDQgoAnWic9wsvaHFQC-19o7StPGD3pvRHK7L5B2xadIdWb41PWZAB7cWkf3sHBdBK9v_gObyC0PUdhN0bHdEtIPHmQGII5wQKmyndHkiPIySdeHEJZrIDjCqeqxLJFknw0vWMSebhMrYBgAd_j89S_KjbaAMtXaejd92xvp3hV8zREOVcfE6RLO4-s1gs6ulQQ4VefG0ofx5LpZi_vMw_8QjpcmYwCx8zyvwBLCAsouk_CWsDKUFl9gH2DiLFXG9jP7_FU0Z43dlxa-OdpsFL1Vf6gL8wh7z-by6OOWONMBSNi0wob6HawL_LOc6oY1WojqlWjlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.  از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/4914" target="_blank">📅 19:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">همینطور روش رفع تحریم آنتی گرویتی هم چون یه کار کرک ماننده، باید همینجا آموزش بدم و اصلا نمیشه یوتوب گذاشت:) چنل سر دو دقیقه استرایک میگیره</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/4913" target="_blank">📅 19:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بچه‌ها من تونستم با همون ویزا کارتی که گرفتم، پلن رایگان Nous Research رو فعال کنم و مدلهای خوبی هم داره روش مثل همین Hy3 کاملا رایگان.
از اونجایی که یوتوب به شدت گیر میده سر همچین موضوعاتی و چون داریم تحریم پرداخت بین‌المللی رو دور میزنیم، اینجا آموزشش میدم به صورت متنی</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/4912" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این دسته‌بندی جدید کاناله، با ادیتور جدید عزیزمون محمد.
پلی‌لیستِ "قصه‌های مدرن"
قراره چیزای باحالی با همدیگه بخونیم و یاد بگیریم
🤝</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4911" target="_blank">📅 18:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kgxjguut2KQkTABXJL3Tr93FvjGSys-5M6Pomog2uRBu7KZVaqAzgsStyozOqEpMJXkoRgsrB_fbFtWCkLr16R8ZATOVNuKsPmClUOd8-L6kBIlocLYhR9__Qc_dME1O0EKOVjDLYun_zrIHVRf3vf0HY6YGzX-4A-LG6Q3M9SgiV4zboSHwmC6dLbBD_hSetB4w28OSDtdZQW2a16vQTfFj6dSQERDZFQ4YtkOxv5MzOoD9ooPwJ5C1Y0y4o31q6qfyOlIGsJ4xZ5XX3hq6XdJIxsRc80oTvzYuBk4dbFB0ImSE5INK2KNP4w1gEM0yo4FIJ1JIXyXT9c-Qfg1hAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
قصه بارکد، خطوط سیاه و سفیدی که دنیا رو عوض کردن
هر بار که کانفیگ V2ray اسکن می‌کنید یا یه چیزی می‌خرید، دارید یکی از هوشمندانه‌ترین اختراعات قرن بیستم رو استفاده می‌کنید. اما داستان اختراع بارکد اصلاً شبیه چیزی نیست که فکرش رو می‌کنید؛ نه آزمایشگاهی، نه تیم مهندسی‌ای، فقط یه دانشجوی بی‌قرار و چندتا خط روی شن‌های ساحل!
توی این ویدئو با هم می‌ریم سراغ:
➖
اینکه بارکد اولش دایره‌ای بود
😂
و اینکه چرا تا دهه ۷۰ روی زمین موند؟
➖
لحظه‌ی اسکن شدن اولین بارکد دنیا روی یه بسته آدامس
➖
بارکد دقیقاً چطور اطلاعات رو مخفی می‌کنه
➖
چرا و چطور QR کد به‌عنوان نسخه‌ی پیشرفته‌تر بارکد متولد شد
📹
تماشا در یوتوب:
https://youtu.be/PAHA55mHLWs</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4910" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">و اینکه مدل رایگان Hy3 خیلی از Nemotron3 ultra قوی‌تره. از اون استفاده کنید</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4909" target="_blank">📅 14:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AodRDXZUM_03z4FFB5N7GEDQCgHbXkjHgQgLQE_7gc9b5XA0p4zgT9G_ZtISFToL2CRjrZ-KVxIFcgCVxPTQWi_D6WPfYqIiQCIWxMCYYvhNkxjocgqCwSKe71Tx3wRqHKUZb0TOiYDHuD0Hp2yAWrEDH4OJX2PZzokvXf49liD8E_rPOinDf3cptoolhqyxnjqY3rpV0fNzLuWg61aZ1X39FOUUSr5ydC5SHjF_7LJuyledRVV5eqgidngDR0c43ABBdUrr-r18S0VeFZCiPFMP8Wce1T3kFrq6yqCTSm9iu3D9UQ5zFTWHN8BvpcAo2dgS6pMOsrsYA6a-YaKYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا به آیپی‌های کلودفلر حساس شده کانفیگ‌های کلودفلر رو با آیپی‌های دیگه chain proxy کنید باید درست بشه</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/4908" target="_blank">📅 14:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده و فقط روی خود OpenCode در دسترسه واسه‌ی خودم احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4907" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیپ سیک و میمو کلا روی 9Router+Opencode به مشکل خورده
و فقط روی خود OpenCode در دسترسه واسه‌ی خودم
احتمالا کلا محدود کردن دسترسی از api های غیررسمی رو</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4906" target="_blank">📅 23:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">حالا که شماره مجازی و کارت گرفتیم، هرچی سایت api رایگان میده باید شماره چینی تایید کنی و پیامک بیاد برات
😑</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/MatinSenPaii/4905" target="_blank">📅 22:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4904">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/MatinSenPaii/4904" target="_blank">📅 20:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4903">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FS5juWOTGWNzXO0DjW8gKoDABiSDUBm9aO0LsEO-aqsqaXJNm4R_tmrAkA1QDT_KQJ-Rosdh6NAE99Cv-Q6Fk9Tkcq-Ry78hzbX2Yyk6hooVIcV5Nryj2DjWXo7X_MhVgbbMOw7cfBl_eX-A3FPGPm3HxO5la8JoRT-r78YMTuPzoINRrPhIqtX4I39GiODn5ptwbTWPyHkJqwh2Acg0c44GVVcVAmggOrFB7Ft9Q8OjRZBaXS7QBJ39v0wSkl5t0zPfy0VhfUwHvQEmiBcfxBXkIMsnhIFmCPE1DzwT7yvzfIQzEhwyfOKQwKb5O3OdI23Iv72Uxe7AKeV3_SeALw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب گویا DeepSeek-V4-Pro-0813 هم اومد بیرون. با قیمت باورنکردنی In / Out: $0.435 / $0.87per 1M</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4903" target="_blank">📅 20:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4902">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه مقاله از 404media نشون میده یه شرکت پزشکی که ادعا می‌کرد تحقیقات و peer review‌شون 100% توسط انسان نوشته شده و ابدا AI نیست، در واقع کلا از AI استفاده کرده. طنز تلخ روزگار ما
😂
https://www.404media.co/company-offering-100-human-written-never-ai-peer-review-is-entirely-ai/</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/MatinSenPaii/4902" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4901">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XmwuSfvCXkfW_v2xqNFC4wiOQ_SijpLBxBoVco2w70hWcg9apmMVZbHRkcaIKFyeFJ78fCu4vPfcSDu5k5n2wHUCsr_F8bL0Mn0b7uIdRWDMJPTJP8SEgcaTaTOe0I_c-RKYppzohD4h5X-ExaFGsZLaFw5EqaqWvnYkvlz4kfH2qtKzirEcfsZtKokkwx_cm-0FgDprU4NPP7j7FdDAjfXneo1SE1q7euRcyU3WVA7VtNl8iqMEz0VKGW7ulDl22gvB1ERFYHc6ky7MH1yqRHHh0yM0snj-__QpPHMP1ZG3NUe3neFmqOZ9q4FXrjjNvAl_LpI_6IMb7zg3nKwTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها اینا تروله دیگه ایشالا؟</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/MatinSenPaii/4901" target="_blank">📅 00:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4900">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گویا ChatGPT قراره تبلیغات داشته باشه داخلش
😂
تا بتونه دسترسی رایگان همه رو حفظ کنه:
https://openai.com/index/testing-ads-in-chatgpt
اتفاقا به نظرم خبر خوبیه. کمپانیا می‌خوان ضرردهیشونو جبران کنن و طبیعتا بهتر از گرون شدن اشتراک یا محدود شدن دسترسیه
اتفاقا با این روش، شاید بتونن مانوردهی بیشتری روی دسترسی رایگان به مدل‌های جدید داشته باشن(مثل رایگان شدن GPT Luna)</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4900" target="_blank">📅 22:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4899">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">از این به بعد، همراه هر شمع لیرا یک تگ بذر هم براتون می‌فرستیم؛ تگی که با کمی رسیدگی می‌تونه به یک گیاه زنده تبدیل بشه
💚</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/MatinSenPaii/4899" target="_blank">📅 17:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4898">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRick Sanchez🤍ریک سانچز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOvSGoPFrfJ9xeIxDZbZKIQ1Te65HWmLlMMZNBI49J_EeK8BfDJP4BNBMG7n9AjSmLVhtDNYA9mEQ8zP3sNCmzsZhUw1lVAFZHUftjajDDhZ15QV3eg-s5Ud_UeBWRVo2ExWcHgn5BixSUaY_ZrlmD4jjRaOj0agZaInTxufofvfG4jm9BXxviRctSqPSt-1w1f9-KYUole3xRFkMIWITEk621a__vyOaftmPQ4GKqgTBTbc8CvrylLw-QoerD8tA2QAuvvnQCusfH2hwqH_Gl05MD5TQaIYJV9QTupq_EC7hQfTSNH_NtaRaU4RoJLNcWjsg8otKehIHCMPeFoGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون حرکتی که برای کلاد زده بودم رو برای آنتی‌گرویتی گوگل هم زدم
از لینک زیر می‌تونید استفاده کنید ازش
[راست چین شده و استفاده از فونت وزیرمتن به یاد صابر راستی کردار
🕊️
🤍
]
https://m4tinbeigi-official.github.io/Antigravity-RTL/</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/MatinSenPaii/4898" target="_blank">📅 13:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4897">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4897" target="_blank">📅 01:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وضعیت اینترنت به شدت بده اینجا
جالبه از 4 تا سرویس دهنده، 2 تاش افتضاح شده، 2 تای دیگه کلا فقط داخلیه</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/MatinSenPaii/4896" target="_blank">📅 01:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4895">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">مهم
⚠️
WhiteVpn Desktop
دوستانی که میپرسند اگر ما کانفیگ های ساب خود whitedns را تست میگیریم و بهترین را پیدا میکنیم . چطور ذخیره کنیم که همیشه داشته باشیم . ؟
شما با این روشی که من توی ویدیو نشون میدم میتونید راحت این کارو بکنید. , و همیشه اون کانفیگ را دارید
یادتون باشه که توی subscription باید حتما manual را انتخاب کنید تا ببینید
🔥
@whitedns</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/MatinSenPaii/4895" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4894">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Building_Applications_with_AI_Agents_Designing_and_Michael_Albada.pdf</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/4894" target="_blank">📅 00:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4892">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شاید بپرسید پس چه کاری؟
حالا برنامه‌نویسی آره یا نه؟
باید بگم که نمی‌دونم حقیقتا. تخصصش رو ندارم واقعا که بتونم تحلیل کنم
و به نظرم باید ببینیم AI به کجا میرسه
اما یادگیری رو متوقف نکنید حداقل. به قول جادی، یه چیزی یاد بگیرید(هرچند جادی میگه ai، استخدام برنامه‌نویس‌های تازه کار رو replace نمیکنه که به شدت مخالفم در حال حاضر. به نظرم تا حد زیادی نیروی برنامه‌نویسی کم شده و فقط متخصص‌ها یا کسایی که واقعا علاقه دارن یا ایده‌های طلایی داشتن باقی موندن. حیطه‌ی برنامه‌نویسی هم مهمه)
اما خب حواستون به حرف‌های غیرمنطقی و امیدهای واهی هم باشه.
و سعی کنید خودتون تصمیم بگیرید. و توصیه می‌کنم حتما علاوه بر مهارت‌های نرم‌افزاری و پشت سیستمی، یکی دوتا مهارت فیزیکی بیرون از خونه هم یاد بگیرید
❤️
نه تنها وضعیت دنیا معلوم نیست، بلکه وضعیت ایران صد پله بدتر معلوم نیست</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/MatinSenPaii/4892" target="_blank">📅 23:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4891">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XvlLNGygyA3j7xMaZ-PwXAvh8WiAqkgHM0Yd81YM0jEJRkZ0leHSIF0-78qrO4yBbtVS50BGzzJiKg7v_t86anoUIwNfBEVM7zkooj279_h4-yB3u16j218shBZ6TWijmSoyktw_Pki50E6XJKv7Cs_X7VKljlBNUePJ1bvfVdMn9q8s3QI9LA1vGsg_HSTNEcl-cbkGmq8Mc_V2PNEoMaJUsY56juaPz3OsVaOh9miCkMuufMBQwsAz36zFBJJtwUBL0nGICDDw37PI65fsdJyM3--xuxaLlL1-aV401B6WagZN4xtfYedVyWrjFrT1vJezaHakFTBetdSl92CTmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">21 سال تجربه توی گرافیک دیزاین، UI/UX و Product Design دارم، الان هم که چند سالیه با AI سر و کله می‌زنم.
از زیر پله تا شرکت‌های اروپایی و امریکایی رزومه دارم.
سن‌ام هم دور از این 35 نیست.
بدترین زمان برای ورود به UI/UX عه، قبل AI شانس زیادی نداشتید، الان که اصلا شانسی ندارید!
✍️
Diego JR</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4891" target="_blank">📅 23:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4890">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X_CGJQ_w2JuhOpzg6KB-4CBag63sMQlek8-PDbouizlPfj0LrdYZtWpMx6Jj7r-1EomfgdwlhzeUdf-nClk5IgL6EXld7BwFFdh0jK7qZxhMclPS6uTYCrrpQdP857jGDCONPzr84L-W4lHFhFJxNpizC6Oz2uA4QbUZoQfP8JWVuBADuI2Suyk6mVGZtlY0DpSHNelgml8l7YoSgOPvV8HXJiTlsAvv5tSFb7TxgFHKNbcVcpj3jP2JeO6IkEZpnaSWfUCbhM2mk4-fL88O2zBReGGFjNYYJJ_kROaUJNN_lEZfjrRIqa6ovFz6O_Pq27DlTP07X2kwvqt5h5ujMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز نشستم با Hermes و WinDirStats سیستم رو یه کم پاکسازی کردم</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/4890" target="_blank">📅 20:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4889">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کاملا موافقم و به نظرم هیچکسی "عقب" نیست
با کلا یکی دو هفته می‌تونید به ایجنت‌های جدید و api هایی که هست و... مسلط بشید اصلا نیاز به تلاش خاصی نداره</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/MatinSenPaii/4889" target="_blank">📅 17:29 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4888">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-text">به نظر من کسایی که هنوز نرفتن سمت هوش مصنوعی آنچنان ضرری نکردن، چون الان استاندارد خاصی نداریم هر شرکتی چهار تا Agent برای خودش راه انداخته و داره باهاش پروژه هاشو جلو می‌بره ابزار های هوش مصنوعی یه دو سه سال دیگه پخته می‌شن و شرکتا یه همگرایی به سمت یه استانداردی می‌کنن اون موقع دیگه یادگیری هوش مصنوعی اجباری می‌شه، ولی اگه هنوزم کسی نرفته باشه سمتش با یکی دو هفته شایدم کمتر بتونه تمام ابزار های ترند (نه استاندارد چون چیزی هنوز استاندارد نشده) رو یاد بگیره
عجیبی ماجرا اینجاست یهویی یه ابزاری چیزی میاد توی یه ماه 50 هزار تا ستاره گیتهاب می‌گیره بعدش فراموش می‌شه و یه چیز جدید تر می‌اد!
@Linuxor</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/4888" target="_blank">📅 17:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4887">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نمی‌دونم واقعا یه سریا، کی می‌خوان بزرگ بشن
کی می‌خوان به بلوغ برسن</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/4887" target="_blank">📅 16:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4886">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">«الو بابا این پسره منو اذیت کرد بگو سایتشو بزنن فیلتر کنن.»
خیلی سایتای فیلم و سریال و انیمه و... همینه وضعیتشون.
تازه من دورادور در ارتباط بودم در جریان یه بخش کوچیکیش هستم فقط</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/4886" target="_blank">📅 16:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4885">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">با ابلاغ مصوبه جدید هیئت دولت، مسدودسازی و اعمال محدودیت برای پلتفرم‌های آنلاین از سوی دستگاه‌های اجرایی ممنوع شد. از این پس، تعلیق فعالیت سکوهای مجازی تنها با تأیید رئیس‌جمهور امکان‌پذیر است و مسئولانی که خارج از این چارچوب عمل کنند، ملزم به جبران خسارت‌های مالی وارده خواهند بود.</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/4885" target="_blank">📅 16:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4884">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ABcIVH-x09W9WEUqXyyNlFPfmNdAM5WWTfCMy1n_JxOb3W2aWMzcBymRdn03zGthB5s2uKrN1ICo67VJoGs1-kDR3PAUH4oSjAPLJZDdjxRrKUPbYVs8kQPu7_RHFjIUTTjNTljgflp19NhzU6K3CnwbFJ5xB9TuJpZDf6JfjxXHSiE1c29D8E1fa-CdWL20-ngonteMrjY4kVvWnaRUelgxWMEqkyRVklTzGqxd1cckMJ04KzEuXLRAP1518oDOnlrQ6STeLzO-_LSfYZJKp5RxXp99pSTPrxHfWO_LPqnk25P3iUl1D1FgXDZkZinOIuV_9VvYksEpeWCG0ZyHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Free Movie هم بامزست. دو نفر می‌تونن با همدیگه، رایگان فیلم و سریال ببینن
https://freemovieir.github.io
هر فیلم و سریالی بخواید، لینک مستقیم دانلودش رو می‌زنید اینجا  و Room میسازید و می‌بینید.
در واقع استریم نمیشه. Time Code کنترل میشه و چیز باحالیه</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4884" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
