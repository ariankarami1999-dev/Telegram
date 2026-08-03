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
<img src="https://cdn5.telesco.pe/file/brtrORJalMfrrebJiXj9ESFbviE5gYZKclHTVBpmy43AiV9Jmr7f1TTryIeA8SacmQH9mowl3zJgWnC3E2tcWWRPjcqfUrJGijb2KBJ7eclEbviVvwY__SonjrrPX7Zvdea-z3asA6ki4wqF7txg_X2W2YWD91JZjozBRlRsqlGZ_Ytb_RmTLS0WcHMid36Puyh7G6Nirv1UWeyeLuUEgN5-d9GaQKgkv1qxDbmJupJGzxHJ3qkmuOpffG0hUnhXQ2ImcPgITbZFacSMxwFs5XrLHI_2ITbmMEwL7HGRBCg70NI1FsWKf1fIKStz28qOKYIVUUsDutT_Esr43fsWiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 499K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 20:14:56</div>
<hr>

<div class="tg-post" id="msg-102628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owx5XO6NMefhBIwQT-6zEs4rLexupecnmfet_0JqDODeyGwu_n-zZnEiWgTeYg5Z8FXCK1gKvE6mJbQatc0OtHi4CqJH_Tvk1nc49h_OPNL3xpwDpK8mAvN7PbGA2zXmNQcGcs6tVCP7y7Z_RHs9lOscypbcYhzizgtGSz_QT47DbRdtz548brvqfvrNOS72D9WRRwgGk3AS0HJilJE0iL0qMPI_WtbjIT_J-i3j8eLV5MnsbnRaQxd3vGIIRr-zBcYiAnEkYu2LQ1INeRGe_FYxrkz71r5Ljy2bBC-zKPBcjpWWM0PvGHCdwqDEhryH_OmBBWdkbecOVyUr54FBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
فران تورس:
در حال حاضر با بارسا قرارداد دارم ولی تو دنیای فوتبال شما هیچوقت نمیدونید چه اتفاقی قراره رخ بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/102628" target="_blank">📅 19:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590393501c.mp4?token=O8-GA1En4CCXxcxPsYa6OU9jwNXZ3yEpLuE-lvl2hcMjXmG_QqKiKhSVJyQspJtkaXpibNJV8y0fYdRI3ziVRUPmvMPAPjX5SZfBwfLoXyovfeIpAYRIGuheMsQu9E9r-3PT2OVfPoQLobJg4k9uouERaI0ovIHYJDqouzrRPy540KnwfyV7j_1IU-OdhYAAAWxG7vaxOrxeNSvcgOdHfSR_ph1Hhv5ucD0LEet3w3FO3Kaj4sg-XHVWCpG3F41WVhuvjTUsIrjyYJfVK6gRrm3yJpf2E7mDx8tmGAiHh5SiYncIIxCL5MyuIfjxfeBcCFCX4MWuzUp5jIKjMB-qag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلیچ: علی دایی مردمی هست، من مردمی نیستم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/102627" target="_blank">📅 19:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/pXyRH4BvmWjGQB_0vBf3MFFW9OJo4AVDnG0UgRZDjkicT2de07iSyh2Npec8j-DW9-xdv-WvwlFajkgKgprOAhqlIogOhQgUbKmAlqtFyC6SK4XRE_vpr7IlVHb8my5tl9Wkqdrad77Jz488EgLF_MU2d_PZRK8GkDga5z0SfY3Wo721oQ5MDu1PY7GfEgGCosSO99kO3nWBMXjD3QOzVqCISGPH-0DVVHX2f3tUQbutZWFZa4nfVQNwAzhtsXJAzdAe1Ex3ycZP1abvMIuFtWPqlteIJriiwwWBCw_bghrUISDfk_IYGIeoaYlKoIKb6kb44kW623LOvehA3iWC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
باشگاه لایپزیگ اعلام کرد که پیتر گولاشی، یکی از اسطوره‌های این تیم، به ویارئال پیوست.
این دروازه‌بان در 11 فصل با لایپزیگ حضور داشت:
- 362 بازی
- 117 مسابقه کلین‌شیت
• در سال 2016 با این تیم به بوندسلیگا صعود کرد.
• 2 بار قهرمان جام حذفی آلمان شد.
• 1 بار قهرمان سوپرجام آلمان شد.
• 3 بار بهترین دروازه‌بان بوندسلیگا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/Futball180TV/102626" target="_blank">📅 19:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQcQLUGi-Sr88dgpO_s0h2dNKiVzoM-SFk0tcZ8wqnup8yBYjlrMb89N5DMtlA6-5UVLVS31Tzz3yqfQpsNPTZ7N_S4i1psIlfTYeaVJx7PRWcs1nYpETrn92NVBb0_6yrrLDwNswSOGnZykAJlESpr59yiuH4druKRpQXm2m2Y-LxMNdCJOQTeqM8nWdWiCUOx8ww_2h-724GPh5T-5Su3vqjWhkY163KAKG6opujPqDdoGOe2ID-hEBE_uK2srS1JEP8x8-bmxXlfuoXeD-3vx8k_ZNM2tQsvYCBesRwq5CPY35ocnDdP4TQloGVMzVOGFXg6hN5M-8ygw7VPzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رونمایی رسمی چلسی از جردن هندرسون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/102625" target="_blank">📅 19:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102624">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCAz7t4jTYD4buu1vpnvFphl5OYcOzqjZPgvcDFQoO7AZAn_mYSuSRnXJW40c8v9usD05q8C3ufdbZBkZDsjAnnG0WV0IDE1UCb-NzaeVPwUKUdFWCSNNMNnQeus2z_zkzz1LkLzBzgVjNEfFTBi_D4n8luokoxcMempvTrwnnbcFSIlKD3zc-DLGFvH6egYEkbCCy-Eu8Z7gR6T5d4zzzmbKx85SOzYDBDvLq-jfSr7OK-ePMBg_W5AVdMDGzCRGHOpZthcpdmc3FTDgy91HudEX-ddWhvI0ql3MMIfx8hYrdlY-Hzfzd-SImwEc0PIZq4UYpzsbnCCiiZtzt9UKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیاس یایسله به کمپ نیوکاسل رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/Futball180TV/102624" target="_blank">📅 18:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16357a3407.mp4?token=C37C8vCJSzt90cIP71pcsU8ap444z_GWXgCMftYz2XTVLXxk1bYHhypayyyeizrLJk6vuXcZge2IVumuB3TmnUuXIQUCYRNfY1aVBAwoTjlmIvSP4FQAycu9TYC0pkJKt9A3yh0klt4VzsQl_nNo6_wRcRGLKcOfi9M5LI3bYAj0XSHWKUBYJlyC5qIyw2mEDJo2MkREI-UIzpZrqm5KZJdhCuF_-r6odzq1vCwCLxLR6AyCYQW3OQxE7J6SOGyCWP3UeCoSdxWbr8eDGSbZeUdIWMerMuhtJAOMxguJdOhsQ2VAOlQN1RVRUJbhpYVA4Wtw-javw0xTAPbcgbSwRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا فوتبال ایران بهمون یه ممد مایلی دیگه بدهکاره.
😂
یادش بخیر...
واقعا فاز عجیبی داشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/102623" target="_blank">📅 18:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ویدیویی از شعرخوانی یک جوان بلوچ در باب جنگ که حسابی در ایران ترکونده
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/102622" target="_blank">📅 18:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIEA_HyimysYkoN1OPqa-ySsQ4dkk5VklLOUKLtpc1QzG7BmSHptD5U19EcQOu1s6SjdZvyyZQWS1HWYBaOtG1xSIebTkOZnEFVXVro8oB4mHuu8xtgLWBA-IHkWcYg26OOWvb9Ar3zIK9auFYwAaP2I2psR2BrwSRYiJ8kccWVL1OKzL0UvI9I2LW0d1A85ctSWkU1GiO9RYuPNzEsyc-awAS3hya-DES8mwUbxx_XFBlL0OKoKtr5LUOzgJ4gNMr7e0MaUAFX2Gwi27ygNoB7fJjg5EaZQJ2yvh_beT32qtV_3CmwtgZIUB4yv7CnOVQLPItLU1w9-EltcVauYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مسابقات سوپر جام در ماه آگوست، پیش از آغاز فصل جدید لیگ‌های اروپایی:
🔥
🏆
• سوپر جام اروپا:
• [
⚽️
] پاریس‌سن ژرمن
🆚
استون ویلا [
⚽️
]
🏆
• جام خیریه انگلیس:
• [
⚽️
] آرسنال
🆚
منچستر سیتی [
⚽️
]
🏆
• سوپر جام فرانسه:
• [
⚽️
] پاریس‌سن ژرمن
🆚
لانس [
⚽️
]
🏆
• سوپر جام آلمان:
[
⚽️
] بایرن مونیخ
🆚
دورتموند [
⚽️
]
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102621" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102620">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwJueIpBSmSfl8eoUsIt-zRLfMN4oB8zQuiWMP43Zl2nJYPtRQ6Uq6p810_sF7X3Nrt1GuYB4GwCPLpV9WQtJNQf3R2E5jOZKGWq5mOvJaQJnPghuTmG4M9ix3RzbE86ewLtPtAqo9CVYt_BFH-ctDXgNC-3GdkGQSokDKDQiM21IQoMKkl8yPdeTH852GmO5NRd3gaLdrOmY4BcH58JwnwH0RA4K-eIydwUx0dHRC8YgfApXnO6LZ9ylELxWlXu45xEWk0okOUx_cgrBuFYp4-SammqTjC8AAq6M_4jLX9-0VL_OjTJQcDuaW41f2kTiSzMFb1kYbEjq4iY76ullA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
#فوووووری
از رومانو: چالوباه از چلسی به کومو با مبلغ ۳۰ میلیون یورو
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/102620" target="_blank">📅 17:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102619">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnyKCdiK8cxNLPDT-sk67osyULAR2zL9x8tMjkF0zGr8wuScyby8nG-0-SrZ2V2lUZwPn6mj3lRtJgrCiC1_nFZfi-K58kunEaDJG5ierYotCfOQuoXy06Vos-PtOJ488RAmMklU3S2qVJt_Gz99j2Tzg0637UgCRvWlV_2kAgKs_UM4ufDoWSSeTSCJI-R2eg-eVL8QuzIvK-eMNNiKZQlB2C0THI09aWd66a69WMVwOoCv6ZF7Uc1oq1-OSu2YpGKOJVbIIxDnfTe3qWDkCHhLmAg_nAEHokzuL0rl2znD_r-gcxZFQYGJvRcLMnBPraKQ1-_5K8U22npKoKbfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پوچتینو تا پایان سال 2030 با تیم ملی آمریکا تمدید کرد و به کار خودش ادامه میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102619" target="_blank">📅 16:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102618">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سیوهای تاریخی گلر‌ها در دهه اخیر؛ پشماممم حقیقتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/102618" target="_blank">📅 16:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102617">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpkR0Ki79ECeVNClilmNuAe_9pBUNs23aF-nB-tSyGtkVU2Rg-FdMEcAI0ALm2UJ8VpcmrSXa5bHJS6_tbqMtGPkkEM5V9tjxg1mGv1TvYuctK_cJvoT9rRWKjuc37yjVh2XbGKXF8zpKh-P7S_EUCJEXaizgEGTQWzU9by86fTfzwQHfSLMUa6-HWraS6TdUS-XgqGD0dqwG2LQHB7cEjsPNT-qTenT04xvEViwZ0x43jaze6HsYt1JD8U5QVBWZmvSaIlUO7K_EMvbz3PF-Ym7BCDZ7GGGC_GUgO-_w4OSe5dBL4iJogotK8qwBd-n-AwaR0oCq6raoqNZycRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیماریا:
بنظرم مسی تا هر وقت بخواد میتونه فوتبال بازی کنه، اون تو 39 سالگی نشون داد یکی از بهترین هاست و هیچ محدودیتی براش وجود نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/102617" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102616">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=XaZULmbhbImWWilLQlnwTOfHhGLYbhGvhtf23Voo7SveRT41nyJysIVQCHGcE4-Rty1NddSOkzZD4T8r9jzMCo0UAwzbOEChUU7Pte7R1liVF3DeEzJS2xiiIDQUpWpDamrws5kLPnmzEHlX56TyVxs9cVXH6hf8Y9j61sXsSq8yFNeqc70XsZXCGXQHUlLHHipEkmz8hPFBPR7A2kaTA05ERLFyuMtculP_b2vc2Ah04Ek6TDAuvg90k1dGAleXaZDbb07FvfrRZzQ3cshzFaS6-eAh4um9rUhsxaZeUgJn5kDMXUMxmJnFJ1oswwh_9GbYKmfbg-3hd9i7Nuj0tzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
بعد اینکه رونالدو و جورجینا با هم ازدواج کردن، ملت شروع کردن به ساخت مراسم عروسی با هوش مصنوعی ؛ از حق نگذریم این یکی خوب درومده
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102616" target="_blank">📅 15:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102615">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c41942b27.mp4?token=HKaz-xVcsiNA1qgdEIN2B4lSucl65cySxJIKoXGI_1GQ0eNZ0zwwqG7HPtM5ESK2rqnjKIOtXkshlLf4G4yCOL-NtN3_RC68Yj2TXWtI2vT-XgaMSHkCsUetinnW7HxplnCEILUPOsmn8WsrRsyrln6nZtdxc8UiJS_UdMypMb64Cm5t2MZN9VkIXZFYP2WnlVAH8_5nkaZVyKi9oo2gjarD0qmO6B5qAHolVC_hAyoMPrL9HfYk0jtKgeImgOlf_fxZBUBjhfyrL0Pi3M70yBSHTDyEdU_EvQxweyREvbkA6lmVM6dDp2GujP-m55g1N6O7BFrz9PCvzYny970v3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
یه قانون خیلی جالب فیزیکی تو فوتبال هست به اسم «اثر مگنوس»!
وقتی بازیکن به توپ چرخشی میزنه (مثلاً یه ضربه کات‌دار)، توپ تو هوا یه مسیر منحنی رو طی می‌کنه.
ماجرا از این قراره که چرخش توپ باعث می‌شه هوا دورش نامتقارن حرکت کنه. یه طرف توپ، هوا سریع‌تر می‌ره و فشار کمتر می‌شه، سمت دیگه هوا کندتره و فشار بیشتره. نتیجه؟ توپ به سمت فشار کمتر منحرف می‌شه و اون حرکت پیچ‌دار قشنگ رو می‌بینیم!
برای همینه که تو ضربات آزاد خوش‌گل (مثل شوتای دیوید بکام یا روبرتو کارلوس) توپ یه دفعه زاویه می‌گیره و دروازه‌بان رو غافلگیر می‌کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102615" target="_blank">📅 15:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102614">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b784bfd43.mp4?token=hGjwSewrH7HE22swz3UxZfiIJ2zNdgUUWtNZnzvt8K9wZstglTFln8HLbT3t5z_y1L8tUI3F8KrstTL2WkvTO036pAKlJuzRX2J9cUvvpyodSekzlLTpymXcaA9h6RBr1zqURq9UdBdK7f8wCM9Nayg1GT_hVAmPiEfCIglg4W6eL6E7ar-xNF1srDTYsCJLAJi2pdgc12svvCnOEaGt5V4MWIO-OswxVOUGbZC0FJFqTCBFpzNZIr7toiBDf1oeSV2W7_i-wqyn4Pcz9_fmbX4GZSaFqrppjJKWsHRYmdPaAyPB8P-Z_95rI6MD_jfENPA5P4lK9eO_01kmjMPLiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خولیان آلوارز همچنان در رویای بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102614" target="_blank">📅 15:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102613">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElJJIJaPra8QlTovgUAtvbG7eAnZvDwLenwfwSTihsP7PgOm4lLQ7S_aqTnHO25JIQWRRtw8Is0a8KlYPisYsiod-OzbzE90aWcU6v8aSHUG6tTFCMbE0qoiKJczkh3Uhtmcb-Ci5t2N6fDQK-7qc3L697LS9j9QUiYNPHiRiPUnuhfwKMOiTUGyjjaoQ-IPYHC85Y8F43Mkkn-PzNgstRKANsJTtaN0tVidMLyzWJk2NwidjMDcq2HpRJ3pfojxicUn9vpf523vxRd_Vrsav4TazvIOcwetFpgdCpzUBU0blzeVi7CQimb5cOhTuZOAhG8PHDbLbPOo6tMaJMzKIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
استقبال هوادارای کولو کولو از ووزینیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102613" target="_blank">📅 14:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102612">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP5xTQOq8oF_zPg0NSJ8spYtig1t3DDRAkIozDgcNRN7sF5cMf7QjEQcs-flZ1CKlcv3uZJVAcxQTZvMLeS1ov8kBRG0nXLZek0a3adT1bUHXJdUObWtB-cWg3DrYiTqdAHRMlOUIk8Ue_dj97cP34xisjQPYGuub3K50hr6eIl6oUe39pcfFUzPNkwvv6kev5nVOtRGqr9QhBcjpcCO9dO5_6pL3jrjhNHCGQRJDFvxtXX5PGcC8WJrSLtOCx8UcMnWt6-v0bo_aFkHV2KkiT4B9mecOTUSVOxL4CCfNAwgd9KvvRfZ1ulDdUEvK_nbLEzCgxlKMS7ve-gwTAJ-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔵
مودریک رسید به هنگ کنگ تا تو تمرینات چلسی برای فصل جدید شرکت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102612" target="_blank">📅 14:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S2wwmUjIWLWRsqbJlCQVNJyzRo5WfK7yIOPLQoKOYRjR-VDZRYXWftL2APTK6IclJFibmlP1HVDGO4m2bpPqYP_yqwnD6NLBwQ0Ak2x6QqKc1tjBpsPig1wmJKp1hnYHFgKHsvazFcYHVVdfoZkP6c85CXjjV9XnFxZzxIt1gfVDrcw2O_KxURgsT6usI4v0LmFNn6UFe1vAM1qi2OGXkK4xcrV6Ye4oq1f4Jce_4Gh9BTch7WDCQbSRlvocqEYB8JMOARNIqSFZSw8tn7JXLbf3MwNXFVkQHmw7QDWy0WNxA_hVZfch5vGzKGyeWIm7Jmuc5w7veaFseOzr3HVISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bidWYN-6zHdaT6ZPr88FheyDZpRkdvIwOoTuIl467SfZgXqANhXmEtMgL_e_qmiM6vCphsOZNz-ZEo340i_gJ5e9iVU07xqimMvQ8tJfvvHMC2NsfxBAU8utSvekurgTqEVbG-NGGH9XYPlsapTKugbo6CPqSDxUUlQHGx8YVOdltFZHsX3fgHryfZWcWbTR6HnB651w8vJTQG4Pxb8Tr59KsbvbmiHfe2_SlCfT77QmYTIF0kZuulmhQcNog__QoDVLI4-UZq6QadGs0jMvPHTf5rIUNIibL0Fc5kd7RXX5b6WJFZRDkZivw2nWjDjf-8WLMt9979fXz4Hkpwk2DA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینا کامنتای زیر پست بنز و پورشه نیست؛ کامنتا برای خرید پلی استیشنه‌
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102610" target="_blank">📅 13:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e039d9b9.mp4?token=GuEnYHifRb5wcFd-BcnliVf3JPBB5lnwyNo_RRl55Q0x-EQBSX6RO4MVoh-6GlS5E2aZOkOfnxr8lMMwsdusx4h8oARq4zsHar0qH-Rq0Gi3LjdbWmrID7vfRZVzSEyjPNCBGHBax5zUHTkw5YwKWkEj3GtQclQsophZL5D32PMq7qm-KcEkaTxWN61f5jRTVykgEOQ4FKHskuWOi1QRZF8r0YE2nFvsax1ShST0GWarH2Xy3YMmkclUDOt5peUhZ2liTkB0WfRLQGyk8P52KIKKupp3E7Hgb6Cccx9aUvAL94y1zX2dulouW1KnDZXqEt0e9IbnjX3FHNLe4U-jGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد ریدمان دومفریس در بازی اول با رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102609" target="_blank">📅 13:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce2j_5JLWu3ShREelKFxbUNpSKUPq7ksT2BSTLeQFP7Xnw1sn_U6R_Ig52OE6gx2uTTfdRjl5F70GVbuTQ7He-4Nzh_43iGpiMZKj7aXKyq_IQj-BRaNeDCMo-UmQ0H2uL6J04YzAWvFK-hif3rO0KZmGP8TTfe1w5f4P2oXTCLqNHWd2fCoAFaiZZsSs78HaR_C9NGIpeA2hlGqb29-nfdD_UUnWtD8RRk5gMDUNQVUVlbjgEaMeL7-ViEDWNJHnIAKflE7PhgiITqQDoOg_k9wQsUNYaLo-T86eIrIGDwPaC5fAKI04ze_tiT9PEag1HOZUg3EwhKmiaFDEZx6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس بعد از کلی خوشگذرونی تو تستهای پزشکی رئال شرکت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102608" target="_blank">📅 12:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d0946d726.mp4?token=vdl-ce1XioHuhrcyOALzs1E5SzEKs_THDFw76ak-sqkKF1VkHEUXUfn-A3aU_cpBKkB9vbj8z5jvyaZQ_Z7lOlU_H9jztJumSemR_Zqk6DZyscoOX79p75USxk-BRoyr2FgfoknKQ0NgqQFnn2W4foxPHX9WmJoEhF6t6VJpmEwBex92x3xYmcqcPBNF0QmcsHzOWHVAzJRXBUasgUARHk43RuaLi8ay7lYeqMAqanD76IJTNnwLzCM5c8DisSMT350R-JOfDuKZijWq6Tr3boi26KRyOdkLZdgdMSLzcXHNq7LXERp0V3voLHQkMkAsSMMZoMkbD1rilWyIC18fzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
انتقادات شدید و عجیب وحید قلیچ: چرا تارتار منو دستیار خودش نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102607" target="_blank">📅 12:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t30fls_VuilR6tSDXxrcEZhtFqqztCGRfLraT8m7ZP3y9F4wsG84_s0h0oqQXbsWgIV9m2FW2JYou26ODDJlOHAtMJ7HjpRSUAaUEojWjke_n57LBS4UzZoCaoiWDrkxoheqcNoTR9qd7IXKtXMecnxnaSTGPiN5zHGmroJ0osANIY7pZLPeG6TwF8_WgNpJ9GCUY0nvyoj_EArXIZAm9ABuYy45UhB4IvCtGpP8ZPwJeh5KhyQiw0d5GwGFncqqGWwydNe5Xs1Y8DMXUNBwp8fGC-kHU0hv_56ILIeUjbjNupRQd7H86dXKmXwFOTpwR8hJdTWnU60v8XXSDpwUfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⭕️
باشگاه‌استقلال اعلام کرد که فیفا در نامه‌ای تاکید کرده که یاسر‌آسانی فسخ قرارداد خود را در پرتال فیفا ثبت‌نکرده و این بازیکن مشکلی برای همراهی استقلال در فصل‌جدید ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102606" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19edf655f0.mp4?token=GgUqwCR20Wx1f4-O_Q0hlu0tMU8Aj0bBDlR1ByCDcDn6_oCvl-6SGTHHjo37U9BP2Qwh1YxsYJir8Jj12DN9agc3ciY0B6i8yjOyz3mUdvZbVOisMvwmonjG9TqczkGBn09meuAu9SzOMRKUpE7cWBKQhdh04gjE7W8fF6Y4AOTPQbRHQuDKDQno7MR0Zp1LHLLFBB_QVhh-qOGixsP_3Putw5J_y1UT2BYyiBszuBWZOCpcKsv2URBhA9dYeIq4kTCbrWuo7RjGFTl_J8hkmkoH0oGZaWQE0g9052hDIUo6Nk74rbdSqY0qnHqAKYQB6HrjVBvsrB43D92UlCLc8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
این عالیه از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102605" target="_blank">📅 12:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743e4b909e.mp4?token=uI6zhD4RwIgKwGmLnGuWjavMj888Sg-lV4q5pStv-AwNJfQrp9dv9Z16JgKm0n-iQv-hYinq8Q4paY4Cbcw-ec06jTGGJO2Dd9I-9b08fEdwyWnOCRdbe3NjUTSpa7Sm0RDiV4MnEcizux7xDGic1kTaLRd9aavGzL1Z4GnO43PJ3mq5I_seCeXSvFxzI7fLD5GjoqVcZxWurP529Mmn3vK5u4VijXBGd_STWC4dzeFfJSyXryueaBV8XW8cUwn2_aeuaD9NixCJVybgaM_aD1ms01sj_rjAT6PzehigJPcg0MFjC65OfcuXijzVrymHJtVNc3aVP3v7z0nEEw5qYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
مورینیو رئال امسال رو نجات خواهد داد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102604" target="_blank">📅 12:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjul3lpHp3q7ENDfyKmZ9RrIwFbbTur56-t1N3olLUO9EhaNJCcoehTtJbjBr8czMXgj1qVa9Yvt0jAwHYlfF_OPlLaIE2N3viOWLbQHBf_i8ftdcPTSHLGqjFcKx1r32qLc7Gl3hwGDf060fUFe9T7iWzvJ1EKNSDwvjDrtKiWkvZrB-27MJCbuRtJXpLa6_s-TBLXlMGYylrJfUX8apAZgcvOKzXxHXHiL0C3h8Qu0Vm6obG9StaS4hLAElthIYyHu-6GL3aISzomcgSOTZ3KDJ0UFPLSfoA-Y00P62Vx6qDFYrrbjmRmopjD5ZSXCUWl5duo12scqQuFTm-M3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معجزه فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102603" target="_blank">📅 11:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OUFBCnDvcbB91E7_KyoHpUsZQrVfXsMiIv8ucHrts4Cv_yb8V3Ll5LjdhVj6t1bhbrTuvRUfyCJdhyRJrt48JEKhwLMG9JYAEmR9vkXfkkxjeU1C_2Lp6zWlptbY6tPeg87VSKCPVAajfCfQquoDUsXIU9hyBiuH9KAYYDekf3ohB9FZihlBR0opuIUHJYvLtnzT1vhgjANj9C9LpqNTD43juxzLh72t1yb7rR8obVtGixUshS1Lzfe3cTruUD_dPlR7aDC4ySkBowv2l9_H7hvpX5uI3I_hSmeb4mHfghFzomzVUswjDsLrdEfAQCimYucABbXZXoopBs8FipoPiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PBZqillcVD2_apzjoS3sxrYxxM5Ol0rGWdn-oS25qFsEM6tHTXXGbmcfa49jwYBe9fk8_m5RooMXkNAj-DDXivLu9NUvTDmX4D4TezlHgSDmnKLL_xRPJSHMYCGl37tjpBRx8ZpRDtKsKLal_XdWDni0VFBKvPVtPaxWJVQUO6tzoL2qf7nlmngLqqx9BLxFwamrw9YK89u-fsHrlRqMQzqxBKV_CrDyEg051_YDQdDAtDYpV_5gMmyi5thBBUSmu2x9oGAhLIRIzTm3rp8iPPUvAL3Jws5vPnk7k_X7v963k1CxVelRb_9nJD0IR0hA49OalXZumDkyPDH31j4LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5GPY5T7G4CTRsrUQlWEvL11gURgwoyhZ0qFAHDt0299BJ3tcipUz2_GrRe0m7fa6ZUDwE5wdqT-hlT7YQf3P1ks4DGW49MPvWsD8rfJGEVJJbhGcqMjOU89HQWWj_9IYnDDiYR3fAfwZwh1ymR98RBrx2T1rhg1qIYy23IDKajGzS4507KjBwVJz8OTnI243eb1FAr98xc8oqCPDQa6ycfTXezjEBY1WobHNYmiOwCYbDBNPf4NV0RWCmAY3FjgnZdp_gJ8j9MlKCK0JCuwAmW1iKwiImDdXOKTAi224-dWDjXV__IYp01FL08UMcIOqr0xo3ZFbL4MQftoQzagXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⚽️
کیت
‌سوم فصل‌آینده آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102600" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU-OzwQ05mh0nQ-PjOfV-RUyKwLPgsUzFzl6AjF8bZXhgcNfEC-e_gv6A-peld5WUgbmT59QzIErut_NK5YAQIGDjWklwi0oeLciFug3JRRbZ7w4bsTcHw0biW3KwtoqWoSaY---Lz3wa2VMAqzsB1jxf_9KAsFY3qT1qsHN_oQXhLXmnlt9drvYlYRJvqeBuYkyE65bfsLFe6OQEhiZHfR_i2pZ4bC2b5JJZRMoidI3FXUcNXc_OIfN0hngIOgGaMLO7USFfRPptVgSRrOJMCOQdvsW4f_Hhubf0L58gNBMMdTcvOV2nrtjvLDpFp033l9eI2yvnP27we3p7vCzbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی منچسترسیتی از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/102599" target="_blank">📅 11:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvoWGrKpkTncmSmE4W5sgwMFwKGWiTvZR74HxxgMJdeUFSwSt5KdsJjoZ-vybcB0gX7pnaF7_JsP4TsCYaJcevCJ5AvqPR5x547u8EtWLXTgnoDra9uc68ILi5zBSKkJNbM3NEkZRZK9YaKyfa4RyWMmKQZCBYGUKf2rsl9wUWRjNYF5IcmbmWUe4zPzBjdFYd9H4Om87QpSbwduqPLM35rkJf-gWre2btEfmdy3CXkGhQ321qB35sfOtQ4Fj1JNwqn0FsVjhLgg86mXfVeLqDl2wotSqbInAbgMd2fWtQlXihAw4qXtWXeMML5gw8Ca8A3pUGZ_qzvdnZBmhGzjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
لاپورتا از جذب گوردون و آدیمی کاملا راضیه و اگه آلوارزو جذب نکنن، عجله ای برای خرید نداره و ممکنه بازیکنی نخره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102598" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17336a98ad.mp4?token=t_I2C_1Cp41Z2678KnYgNh2TVyQvYVxiQtzM-7wVc7vvTxJvjBEvHjqaVuHnRSsf-xawXYJdSnrDizedaqn9cPjjRIbKIjdPl7ojMqLxw3tHt_dd-LwEDZBn33SCbH-uerp18vcWP-thYJpBFujx9LZBjy0g3xVeY3IiWL0B47AWUHwaYqykv_jV0wxTb3AH10QLFs-gEbJX-06W2Yi-Fo75Ml2-9_Vbv_4PmzLyBGrlO1t8OB8pTakD2uknakD6VaVyxo9a7fIbRrQX6ir7_GlPPCcEuPjD-rqRzS07BswV6EVk7lom3Cs8M4uJhEKKm5mlDzdP3ne2zHmG2eJLBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از رالی‌های جذاب و تاریخی در مسابقات امسال لیگ‌ملت‌های والیبال ببینیم
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102597" target="_blank">📅 10:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068f09e4c8.mp4?token=jiYOU4kXD6-UWFxsETHqLfhFIbcsGkmkqoD2PYYXImH5VXvdM-GWeVIfcdEFVlPZenTesrJoxgNjMohqquRLqsXVDvDPeC_wpBy8zT4sXc3zG_iDp_YDNdkPl_DjNqxkkpF4GSsuX_VmdJskRuVZ9NM3rS-F8HLLq_xHx8X1RmCXT5TheU7R_iTZ-KDVdf0WMNJx0pcyIdauNrSBKOHKsRyXLPeG6EGaTib8u19sGn-76mTuWv4E2be4iMUhAFLpWbzqHXQq0KEW0t0-ymm_LSMN09NAD4LwYoQNHNlWandp4eOMuIEfK1aFmqlWDQhm1K958yxDm2jXw6oWMLsJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌بهانه مراسم عروسی اسطوره رونالدو
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102596" target="_blank">📅 09:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba13eb170.mp4?token=GW-BFi8DOKvNefRn98KSW00f_hm_Oj61HaTp3V77YuEPXWMEEdDEWM_ikW9BjwxW2ZRtEZ5jPp8EYpZDbEey9LfJSh64Qxm0kK8PLcfAG3aUNMNt2qX6U64mQVYNhu6LBd32YnbIJyyGKg9wn-KwtZQ8dp6QHRcvzFP8m9CIPL4fMxGqCBbfXpmAPMqskh2EW74PUvQpbaTXT-wAQp4eJoyiRPJtkY08CSIFIHV4IERmfA9yuH_lZydmkvw3adYR5LwlaW3b_SZSURJJmgkz4cT1N1mlMa829XR0Vwrl_CbU4tNnSIfmX2Yk-9kcFy3eUkzWqf5L6LVSrn8Sy3RZaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیزا بنظرم از معدود بازیکن‌های این نسل نه‌ چندان درخشان ایتالیا بود که توان رد کردن یک در برابر یک رو خیلی خوب داشت و حتی به جرات میشه گفت قهرمانی آتزوری در یورو ۲۰۲۰ هم بیشتر بخاطر عملکرد درخشان اون تو خط حمله آتزوری بود تا چیزهای دیگه!
خلاصه که واقعاً حیف شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102595" target="_blank">📅 09:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0e99f007.mp4?token=cbh7TF3L_o0pTChaCcPMikMv3nt0YaIU2TE-waY3WLfPjECLB1zqUjwfz1aFKRFRNz_Dem9JPLkdxnOb4PETqEvg459sOEdsccMK6u39zukv_TB2ucMIW-VngWSpuL0uksjSWEP4W_5so8MrWeSHHLRrk1DCjmTc7x43BmtNBdnYyolYIqWN-ploQ3m_RrELfXHiD2SRFunDagYwUfDNqpWKq1ZRtI8B5fhsMse0LUv0J_8oeS95fXsFj6AOIgLDTvAgBUV0aZ-WOyx6_vSL0Be_dEOxVd2bWiblYikqOa2qIqHQ8A6khuZ9Ct_qYGQ4Np4nVUEYJRtDJwjO2wwUaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
👍
نوستالژی از رقابت مردان آهنین سال ۱۳۹۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102594" target="_blank">📅 09:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aciY3P9YX3YhtWuL15LXx4HG_txeo3NEBb5fH9fPd8X85RMPOAhVwl9iNFk80kDbQbWQgANE7LXeDzpGokZfr2PKAcsS8IVilN2jdc8tj4KPrRPg9NuCm99LtLCvS6tYZf-BE5cevsmu9eUCDfeyFZxbrkIfSmGt4_EbuEFwAJcapVoR68rd1FmhwdQfdKVWb9TbBIAvYg4HL8PKZGuxFtUqaoN99CaN3xyNxZXvF9kIe8YFDzM5m4gJG00fjMECVL2-Undtgr1sFVOHJt3r1_pV8gnR0qyNuOrbgryp1vbRlgLUG_XAYuB53yqDTibO5WMJirW1N_HeChSDqrJ7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏آمار تولد در سال ۱۴۰۴ با ثبت ۸۹۲ هزار تولد
به کمترین مقدار در ۷۰ سال اخیر رسید
، ۱۰ درصد کمتر از پارسالی که توش رکورد جدید کاهش ثبت شده بود، ازدواج هم به نسبت سال ۱۴۰۱ حدود ۳۰٪ کاهش داشته، به نظر خرد جمعی ایرانیان داره تصمیم درستی تو این اقلیم و شرایط میگیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102593" target="_blank">📅 03:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE3ou-csGdduQBcPL3w1dVjemzPn2as8NdND-0mJfm0k0zyEkgOuJeYqLowVZjjYk6pQsdZNeU6JJytnmym0urI6c7_FjAqLxzW4OV_98nIXR3Jb5x6XQZ9MSMmy7VKFRzCccmYoKghLCTULxePCJtMy7jgzgVLEcYnmtT6qk7xa7kWjR85ZX3JdF_0-TDDnVs48HOQ0ockObe6S_CYL9jRtzAJsHBfhz28wVFMoZXdqQy3hdq9qKLScwI_PRgslAVtuuMkRUxGYQQSKrwokmewQjbAqzG9y0wsHfgPIjqLKijeeJbq_AtlxNfJAbcYvdoRtdq50_pK2QjQX0oG5ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
نشریه SER: باشگاه بارسلونا پیگیر جذب رودری ستاره منچسترسیتی شده و اگر این بازیکن تمایل نشون بده، اولین پیشنهاد رسمی قراره بزودی ارسال بشه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102592" target="_blank">📅 02:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
▶️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی لیورپول 2-4 لیدز یونایتد با گزارش هوتن خداپرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102591" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش جنجالی پرسپولیسی میشود؟؟؟ خرید جدید پرسپولیس درحال نهایی شدن Tic Tac
⌛️
⌛️
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102590" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwrjqzJZLvYeQPrWUrGgVxTc0Q2d8OepgLor2EB05Co-f_AOG9uunLGwD_EKqUXuLIhfDRhFx7HsmHVJ5JivS9qdJ0lQBbVMoOhCvQLCJF17n9AFCpOZJwUoQDAnMnfApfn1OsnwLLbFB0xpsydGEK-HM0GGSotcTxHoXNyLPa0WcLnymWb4ZhemZIcyW_d3LyrJym4uQdms4Oy5gqraQ3eQUCGc-8RtKUfqvfHu8BYV2M_kOLR7NeJs3cIYvY_Qz-FqpL9MQi6Qi0lSfjG7pN5DbbC-yUBSlDioexWekoR30clhH1Aju2S0D31Bp96ih4lK6BpUUzeF1SCObHNGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
۹ سال پیش در چنین روزی؛
🔼
💸
گران‌ترین خرید تاریخ نقل و انتقالات رقم خورد!
👀
🇫🇷
نیمار با مبلغ خیره‌کننده ۲۲۲ میلیون یورو
از بارسلونا به پاری‌سن‌ژرمن پیوست
؛ انتقالی که تا به الان گران‌ترین خرید تاریخ فوتبال به شمار می‌رود!
📈
عملکرد ستاره برزیلی در پاری‌سن‌ژرمن:
۱۷۳ بازی
🎁
۱۱۸ گل
🅰️
۷۰ پاس گل
🏆
۱۳ جام قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102589" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f59637d24e.mp4?token=k4R7Jr-st9emW40808OjDdpS_R3Ivj9Zs88-Hs61UUGy1uKVsgXHx3FITjBQ9xJFODooWWovOJmn0iTFINK3CXda1Wejzj0WQX8CP41UX4QCTLF8LQ3pmHXjFA8gissGR645JKqF9cQKpPHZ_mdMfe3BxKlPl2x4X9hcFkg5OCvtm7MP47Q1Pe_u4_sniVGWoKhkaCx7-7WDios5pAaYrZmYTFH4E4LXW_aZXzHESjRZh_bubPu9HjNiqgPEsnHouCAzfrTDGY9Fx5M9pgWNYFs3OOh8sELYhVYkEXkxkJ-bOmz1wvD64YrZTD9uOpsVyFpvCaYu4Eti9Xbqfu2vRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای انجام شود که بزرگ‌ترین حمله از زمان جنگ جهانی دوم بود.
این حمله برای آن‌ها فاجعه‌بار می‌شد و به همین دلیل نمی‌خواستند ما آن را انجام دهیم.صادقانه بگویم، عربستان سعودی هم چنین حمله‌ای را نمی‌خواست؛ زیرا معتقد بود توافق بسیار نزدیک است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102588" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=anYqJss3L2WxGraCp9nnGqEEl7PmCmW--iwGbIK9ehzbMyJzx54mUzIigvLXa73idwiya0U0rOUpOo1iz82XndA5tWdi0YhseejWJsHyoQarmC5eUF5af2xUoddzIVCXMla13kPY00AbcgLRiJZMSYVs-jqpmVD81QUnt6MPmhZwv5BHqCzQh44ZNPc4sPicis8inFSHNfvhBxkfkHzykCB2yAhaHHMMH3hohTEJ8yMSNldHWyto4gPoDQjqOgT_NEQmPgfeNoUIZq4OkF0JQODB9SZM6GU77VNLiITESe-qms4IhstAU4kvzUOP0LNu9s-F4hhU27YLPofhVp2mUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed5f1be34.mp4?token=anYqJss3L2WxGraCp9nnGqEEl7PmCmW--iwGbIK9ehzbMyJzx54mUzIigvLXa73idwiya0U0rOUpOo1iz82XndA5tWdi0YhseejWJsHyoQarmC5eUF5af2xUoddzIVCXMla13kPY00AbcgLRiJZMSYVs-jqpmVD81QUnt6MPmhZwv5BHqCzQh44ZNPc4sPicis8inFSHNfvhBxkfkHzykCB2yAhaHHMMH3hohTEJ8yMSNldHWyto4gPoDQjqOgT_NEQmPgfeNoUIZq4OkF0JQODB9SZM6GU77VNLiITESe-qms4IhstAU4kvzUOP0LNu9s-F4hhU27YLPofhVp2mUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌خوشکل لیورپول در بازی امشب با لیدز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102587" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102586">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYXtpba2KkxikPtdEz0Ter_Yn6VWGcM-qi8CjsnaWxarygj2oKqxY-4RCUYc6OWP3cuIornOn0tn6ErWAE_GmKvx0b1gFZ51DlvjuTo4gaYR835HzhlgWuL80KkUvrKCnP304DJPDIaXzU-QAyOqkUumtw7A8JRYSJ_tOzN6m64mwwmMzAx1IrccJguNYHtt4--ZBfjgMkbEbWJ56i7-Y46jDZziWpi3Iv1RNjb3P-z6ZKd3xweuft92ZlBhxuStnOg2CUKOUawfZBI9uGArlbQ12NSy3Zefe4PuQIWggPIkz3zXnA_oqPXwWu5rz3aYNrbdCTJ_JZoL937vuB70NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است بزودی مذاکرات نهایی باشگاه پرسپولیس با باشگاه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102586" target="_blank">📅 01:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102585">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVCjjeZBVab2kyP64HkAT4NtpAzCtOQZRhQdwmRuBblmBW7JGA2k65cytalJ3agQlb8eqsgznvecP0grpcUXeSEkILn8-d90MQchgLCDJnTRM9y_6zW3gguPm9wLEslwk0eJlYpIjVgdxqpkcMUXOz9bxfXKqcvjW_ZBN8c4RNm2FII56B0V9ubo7ik5wTZ1LQvWLNQIgNWetVx864gJ87hqPc7SbfF2wkUJgWMjQJFyZFD0AJz4VUAjh8xqbk0oqRTCzMBhNjpnR5e-vM1SPmTGzIwOcb2sEckU8vEH3Sr0QyqeS_vqkvkg4AyQn1HUncfUJ2nVAqEre2VZESHe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خط حمله احتمالی پاریس برای فصل بعد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102585" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102584">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=ESLYzEJiXCoCIZJVstHJrysBAo6YFef-qm9nn1cVqDr4JLwMezgR13O5eXH05H2yCE_OtkiBcP9ujqVV5UL6Irh4GWfsZ3s4IO12F8e12U5DXBio-c7UNcND_tEzRJ9bAusfrPDZiWOX84W8VNUjnTORAFBo8a8oGpFVbLq6V_LS97TTcSLmzjsFfSPclmWnKZztFnHv8GjoU3mK6CgBVGfFrqR3l7Uzw_DIZDmHrkZko8eyBKWn1z3hVhXAUd_jvckS8hONBrO9RMs6YXCWDgkrHQ3o67QTDu_tzbuHX4yonOpoN_jElBSOI_qnNut5lxtY47qAI5hH_TELc1dehGx5a6b5XeKkwWyinTZvXZBVKiIWP2qAyN5Y_iMs7QYWW3uvVir2GuszxsaLGpMeuYQczrMIerv3aEDfNd6BosTZcH_EJrqEZ3nkDooYVT7HfzVOj8z57pQ7CtmegDpITPw3Q2LFI1uXPSQF2jt6ufU5ac_Joo7UNUoSfELj1pM1cyk17A3ayDm3rIEeNTAKU_7cxozYtlGQo9SmDh9ihIjFsRslXVgt31rN4uIa0V-PBRSwFU51GJzLv-huakpywy643IhUfDhhoQ_Df9GHwE3N23B6J30FCw_jSuUKje0La5coM1i78oag_a0hk1x5PqTgtmwfq_clB6CEUZmzsO8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26376bfb69.mp4?token=ESLYzEJiXCoCIZJVstHJrysBAo6YFef-qm9nn1cVqDr4JLwMezgR13O5eXH05H2yCE_OtkiBcP9ujqVV5UL6Irh4GWfsZ3s4IO12F8e12U5DXBio-c7UNcND_tEzRJ9bAusfrPDZiWOX84W8VNUjnTORAFBo8a8oGpFVbLq6V_LS97TTcSLmzjsFfSPclmWnKZztFnHv8GjoU3mK6CgBVGfFrqR3l7Uzw_DIZDmHrkZko8eyBKWn1z3hVhXAUd_jvckS8hONBrO9RMs6YXCWDgkrHQ3o67QTDu_tzbuHX4yonOpoN_jElBSOI_qnNut5lxtY47qAI5hH_TELc1dehGx5a6b5XeKkwWyinTZvXZBVKiIWP2qAyN5Y_iMs7QYWW3uvVir2GuszxsaLGpMeuYQczrMIerv3aEDfNd6BosTZcH_EJrqEZ3nkDooYVT7HfzVOj8z57pQ7CtmegDpITPw3Q2LFI1uXPSQF2jt6ufU5ac_Joo7UNUoSfELj1pM1cyk17A3ayDm3rIEeNTAKU_7cxozYtlGQo9SmDh9ihIjFsRslXVgt31rN4uIa0V-PBRSwFU51GJzLv-huakpywy643IhUfDhhoQ_Df9GHwE3N23B6J30FCw_jSuUKje0La5coM1i78oag_a0hk1x5PqTgtmwfq_clB6CEUZmzsO8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف داشت از ماشین فیلم میگرفت که عجب ماشینیه یهو میبینه راننده بارکولاست
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102584" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102583">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78a83fcdd5.mp4?token=OP3QQTbz4fGCV0U8z76hpIOsMKsx99wD2XIY6jaE7TDKOZ_8Lf6TWE0DfkOr9WsPz1tJUrDvOw4YjdhijOQHYYbRMwWhwSjRKWAmy5yUphbkbVClhWw-t2InZuXCJ0VwxTa2eUuj7egpuRv4nNC9wE8PiPIMTJybNCYVoNWo7OQ9SHKBotpCWjElXsMD3MWaB1iSnU4zyk9TPnOM7LLLQsaAkpgiqFggsa_YwK4ugxMqI8jr2xlT4R2WrckNX4x4JoAazXO60PmbE0AyETsonKCmPzmpTsMPFvXOl067iFxZx1R0rkMWIY1p3LPaHbml7uRYn7svq9rfaWEnhYy0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت زیدان و بکام در برابر استرس و فشار بازی‌های بزرگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102583" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102582">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qo_Qd49uLvTQ69HyTq9XAnqb9qK9eH1OmUHhoglYMU1m53XEMwnBChqsZW81XYFs-IB2USgezFVUIqf1V49olLJ8l9FVYYQhIbPygz0oCJdrXJVNbpgyeRk_kepVNZxeb0D9cEIltHthnP8qKGglIJVZIQs78PBBt9LAa_b_fo6gCat1oR442eUft46hy6ejfZpPOpV8sZ3lERzbFzHpv91d_aKOief9vIYvQz7QrdEGk4pmO_kiwaXP7uK-MTx0zQ1u5Jy6OqGJPMDsH0IRLQYEiXrd9YYYqrQXupf1xiNiqYqnT8F4DJz2N0FEI85LOrh_WO-_bAKnd6qkOzssUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
یوفا داره اینفانتینو رو تهدید به شکایت میکنه، یه نامه مستقیم بهش نوشتن و اونو متهم به فروش و نابود کردن فوتبال کردن. اوضاع برای اینفانتینو داره بد پیش میره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102582" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102581">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n87o6nCVhGtkwltGMh4Nsd6eC9vVx3m_wj2uW-mYkVyLGPmSzEttQoflF_OKFrGMHcygAAGK_4R0ZmGBOX0VMW8q_QkwFKYBNdGTjjJRSussiUcBKPyLlHkqckvIvuGpiUipP2JTp5NNDZKzFTslVYvtgFjyYZfSJzL59FChpaEj0XTmFS7mHLiTz6ZxjuqgaMEAXGDp97kR_sglAikz9ADBH3AiKcfaExojnRurgwtK86_VokoSsLbqQQNfHT5-R_Pa2GdUUAgjJ6h6go0vDMPbatYPrs4qP7m8wrWiXUvtjvXPTIuktSx9NZpjbnSNzxQFY7U4xo6Wma5AD_LykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
هکتور فورت و دوست دخترش:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102581" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102580">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsJY7DmlZrVWgcCc36Wr1700qIQDod6evO_YlADCr3ubBe0ggikUEJp628MjeprEE7kKMi1pDmpA44fwGf1vETjUt0uwaj3QQYE-7AwfiiOU46Ckv5r3KHlSWDZsWPIvox3j5qRunj4Un9gFt9YDO82GFtwhBWK-ftlezefBag_nZO2BJm3G724Tmjsrw-VGzbIdrcsWzHogVtYlc0arZGtuOMJF_TZhLeQt-sz_LZMvuGQ_Q7efunUJdScf6NoCpQ1Y6z30JPMwjrl13CirTJIL50SidqToCBs72XlhBQA63X3QDcJ3qH_HwIf_s-sr5qXI-6vL6Y1-9WGc-bgg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ژابی آلونسو:
از رئال مادرید یه زخم روی من موند، ولی الان خوب شده. وقتی به گذشته نگاه می‌کنم، هم نکات مثبت رو با خودم برمی‌دارم و هم چیزهایی که جواب نداد. خیلی از خودم انتقاد کردم و به این فکر کردم که چه کارهایی رو می‌تونستم بهتر انجام بدم، چون همه‌چیز اون‌طور که انتظار داشتم پیش نرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102580" target="_blank">📅 22:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102579">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ofCNhZ1eXlL7KTd0qoSpbRP16wSf9NTFvZa3r1yaLxObgyMuG1DyAPqzV4cVrdkT3pshFu13rlScWl7IsakMSeEZhLOnCYRs1ucpAaabNPYuG7P7cQbV3N7XataSg64968U4W8CSIpqfT-VBIxDHaLu4pxWVrxTUWYjvG-JxLHJ-UiWYyUUQ7M4i1oRV_fcrKXzHolJ0666WGa1Y6gXLAdl8Tg73S9_jp40jxO_wffbm4EATV_YiX6mLEfWn5ejynv9YvdLydl6QHRfHRTsXW8EEze_d-PKlSlEF9j9E7fAy9I0k4tm9a82b9_g7tjwhbysa8fr2pKxYfnSb57rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرناندو پولو:
هانسی فلیک میخواهد فران تورس در بارسلونا بماند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102579" target="_blank">📅 22:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102578">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCKq874gjv-o5-Jz7jGzEsf9Jp-rrAZg2d5Va3Gh7dvdaw8eTxlO5RxRXSzD2QrRzUlgnDoAq6GwtCRHR8uaJkPxfJiafOxuRmDKGJafPYozcXTRiH_HUdjU5K2WXrvFU3ZNezgemUBZ1aoGB4-KdzS04UQQwhr4iuY-bUmOh7J8gddmIHCRwNCxXsLFJlXc52BhpWAIIFZQJhGLdLIlauaHClTDxIqyX_6PAiD07Y3cbutEuFPKVxspjK1iw3KXXbf5m2K27u43ccnPp6wSa7KsuaJWh8CZ2L3GvQan-gbaRVCKsZDXvmxnAX2byEudQX5sBC5onfCpR2lFbZE98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه‌هایی که از سال 2020 تاکنون بیشترین هزینه رو برای قراردادها داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102578" target="_blank">📅 22:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102577">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNd2CdItzmWQo6TQnbKw9Brd0z29wFc-gAxOfjlDA_wsojPV0bd3tKTi5q3XreUmdeUIGMoenMYyFskj1wihTGD0hgPMlfA9PXv3eDhWHvjpRDn1Rw5S3MND4iaD9Fq5ddGWWtVQ1fF5KZyTbx62VvUmzOUkUTOceTyB3ADP_z5CP-kooq3Lz57mVK90XCluycu4P8XEnQxjbDPITS1m_Xxa92glNOvnUENhg_OzpTnF8qyFHs1XgrGnXQGVsb6vBVePUtKWBZ4h-jb5N0GL8eWfXwM9ljakaoAhmb6WG1-NiLOoYuHm8tqWEl3_g1pIlOkBhrrEgtQ2fCJ-HzXn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هندوانه جایزه بهترین بازیکن زمین تو روسیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102577" target="_blank">📅 22:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102576">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
تمامممممم شد
🔵
here we go
🔵
💣
Coming soon
👀</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102576" target="_blank">📅 22:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102575">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnj4lb_zL-xAEuFrZIfUe6_fEK6Kr4vh99cMIZAtI0KuvFWsRp2Z4Xlld1i1Bq0H8ItlHviSQrkU5Jb-BzPydoNE64Po7mAp04lN6lecGfDFFS09CC4tDsK7Mm_poW5-XHTvJpXO1un97MAMYT_U3V5GFgIHhzSX76fKjbcm3CbGhmMMquyPII4RTSsaleeYaM_HTgl6V3LYuPs6a7h2jdzOnrJbU8QmgC1EkEbEV-apt74ne9ycjIilln_lPxmOwpTx0is73rqboNagw6wTNp_tOXWoKUVJDMVmFtM_2GbvJh03ygTgJ93JlegRqvdbn0uMZIy6CsLtE1kMgL0MqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">براهیم دیاز عروسی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102575" target="_blank">📅 21:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102574">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238d22991b.mp4?token=gEJcZ35HKdBl4XRErWp08Lb2q0z2tSHoMgnZOBTyikvZrp3D9CIp4r8VFfK6Z9vT-Bk4780wl7do8Wn8vvlT9oA5YfM2M8Str3BvUKIpzUu_O-L86_DAjDro4jk-nekiAhdBy27HeLj1ZqVgnF_3AuRPPbkmHqmHG54l_NrvmcQcTBny5Wu4Wcdy8ZdkTYnyetmIGFewvebjArfXoq3-8QuynZ9n3e9PgggW-g7c4vGVDJqAxvyyx2_QYWlr7Zb2wYJqXKY6JYBI5jaEqgeHl022DcVOdh08gMZFiqatDxRsPaNsbwEZMYnB-4xC2Ww3NEm0GVBpFPh1_nSW2l6Zsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238d22991b.mp4?token=gEJcZ35HKdBl4XRErWp08Lb2q0z2tSHoMgnZOBTyikvZrp3D9CIp4r8VFfK6Z9vT-Bk4780wl7do8Wn8vvlT9oA5YfM2M8Str3BvUKIpzUu_O-L86_DAjDro4jk-nekiAhdBy27HeLj1ZqVgnF_3AuRPPbkmHqmHG54l_NrvmcQcTBny5Wu4Wcdy8ZdkTYnyetmIGFewvebjArfXoq3-8QuynZ9n3e9PgggW-g7c4vGVDJqAxvyyx2_QYWlr7Zb2wYJqXKY6JYBI5jaEqgeHl022DcVOdh08gMZFiqatDxRsPaNsbwEZMYnB-4xC2Ww3NEm0GVBpFPh1_nSW2l6Zsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی ساده و بدون حاشیه رودری، بدون فضای مجازی
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102574" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102573">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=YsmL2TgeQSgneUrF1CHSUtNVefYTf1oMgPhZNvpZt8JCKeWgPeu2xDk3-SE5d-XkR8PeX70uiEkKt3b06Kuie78qnZK-DGAw9c062-ZYplc78Yz-aLyd9J06t5oJOGbqDBKvDs1t0aZy-6qYipu-t-E29cufROutA19VMj7y5Vd8va8l_vCN0hA_sa4eJZKcw0nEX59sIk51oF3Jz_Q9xJLRZCplhftiQtueZ00Li7lE0BdgOP4nzanAjxI7DBw0KeXTW-eE4HsXDhdusSSFbHJbhgY7Sm7y1JHYYU8FH49U5DwxdmOA5QzapMJpaaxbx2IVNo_L2NUjZtaSrzY2lEWl0zjC0NfJQ2etKuzSIaFT6ZcdyAtOV13GXo9a8ApkK7E6vQgjvhotb2rLRo5X5qYm45MKVjtYrIQVH3fF_X4a3o9OwzU-G4IltbGM0rACO7giUKSG1wQqJdONYpMa4S5kkGGQdRgtYoU7v_aBz17DutMouGV52nfKs0NqTWOae1MKWjaRrQbLBJSvASik3TIuHzdK3yep6Y4PvTgKupmY764JjFL2wxCroKpsbNWplaPrB-IpJSaWgJLcAp44FcLSM8SIFtPw1VMNKqy3J-0zasAhctyNuFtgAWDk3pflpfjbZftv4udCu0OgSLATJRhVBnLN7CnKV6ubUAbXYe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f9b5ccb92.mp4?token=YsmL2TgeQSgneUrF1CHSUtNVefYTf1oMgPhZNvpZt8JCKeWgPeu2xDk3-SE5d-XkR8PeX70uiEkKt3b06Kuie78qnZK-DGAw9c062-ZYplc78Yz-aLyd9J06t5oJOGbqDBKvDs1t0aZy-6qYipu-t-E29cufROutA19VMj7y5Vd8va8l_vCN0hA_sa4eJZKcw0nEX59sIk51oF3Jz_Q9xJLRZCplhftiQtueZ00Li7lE0BdgOP4nzanAjxI7DBw0KeXTW-eE4HsXDhdusSSFbHJbhgY7Sm7y1JHYYU8FH49U5DwxdmOA5QzapMJpaaxbx2IVNo_L2NUjZtaSrzY2lEWl0zjC0NfJQ2etKuzSIaFT6ZcdyAtOV13GXo9a8ApkK7E6vQgjvhotb2rLRo5X5qYm45MKVjtYrIQVH3fF_X4a3o9OwzU-G4IltbGM0rACO7giUKSG1wQqJdONYpMa4S5kkGGQdRgtYoU7v_aBz17DutMouGV52nfKs0NqTWOae1MKWjaRrQbLBJSvASik3TIuHzdK3yep6Y4PvTgKupmY764JjFL2wxCroKpsbNWplaPrB-IpJSaWgJLcAp44FcLSM8SIFtPw1VMNKqy3J-0zasAhctyNuFtgAWDk3pflpfjbZftv4udCu0OgSLATJRhVBnLN7CnKV6ubUAbXYe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخر و عاقبت جوگیر شدن مهاجم حین خوشحالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102573" target="_blank">📅 21:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzIUI8wOvHwDAh-7eHa0Cw_qhed5_PnygBGyHlnwvRjuGQkOC-jtre-kJrDa6RUNgxuYy2DwWkpavY4MoOI4Cv6V8kURrQnuT8Fqr1BPwykZ_Nayyhnhfy2nyTvkGS2QSosHeA-MxI0K6qTbO4CfEhKH-_JKhy3xHHW0z3vNic24tmkU4EMjgVf-pwc5_KIBvwDCuAln89_AlA-8naVBVQHKBxYozogdHbND3VH2E2hmCkx23f2JxQsn0NS4tg0SzK5RwEnbj8UsSMfeNerLy2YMvrYEuF3Igk6iDXbMm9XXbAGNpmRMtH947b0bnNw5jPDfztXbzpdNPk4irV8pFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuH7kZqIo1KPVOKHCVJPbJrNzCiYbxfita9GVSnduXxjTzfi3AKR7QVqD2nd-eWJoNt7Kj_9PkQGXGn8UWeBozdYrnWboh3KRhAYx0KeZEtwFxuqq5M4jdgdPw2qB_T6l7o0U62X0tB8Jgw2fvxLiTlnGlrBI6tIUutdS2_iTbtp6rXArN_o3g-VJdo8kd6NFGJtBPwvzFJNFiou2cFRZ2_md5Uv7DzxLn74LMM7neTNxC9K9pAzd-TYLne0ZX0EjrkVdnU3VhR6E-E9IDaDHVv_A96DjcXfrIwlg3Kik3F141o20II0OP4z49ogoj43VGhubaaRIrXgQM0cjUA70A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید وینیسیوس
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102571" target="_blank">📅 20:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102570">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hnx2SgIXYn6APQ3enDrs56kf8KTZn8jyaoN3F37tHzh-7i4ViCcyUjIhP3NUONmw6hLawRq1WRLfQKCQVQsw3f5ypFOnRoWrl11b12c1A-FOiKPlmsx1vA396jUayxN-ZqYcWEooCTAVNmcR3Ch_1KxhhDAO7aGverODdRs5EuQ78PxjfPDkTlc6nrHHKmwNc_hTcQOhxVlOjCfSI8bBHEK_pPCwSDFpAMwStbCoDfH8E8lUXU7CVoAKLL4ASbn9YDQtVXk9U2LYJCP8fh3pnMRnpUPkNEOn__zrW_b1wl07Bu5pTXY8k7iQ_CO2q0Lhy70E64t5cne0BmRq_HkedQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
موندو:
اینترمیامی بدنبال جذب دیبروینه‌ست، بکهام میخواد اونو کنار مسی قرار بده، کوین خودش هم بدش نمیاد بره اینترمیامی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102570" target="_blank">📅 19:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102569">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQTAEkM7vGuGlnGEdzcF4NInpVdkCBg-XXYvOvXJC332UIVdvlW0htN8YCQz6Ap5-IQJs6vYjdq2nJeXOF1zkKsXqXpdmug9C9XFb3X1eSKKVnzvuSVIn3hPhLjKV-re6kmZ4jzwc_aVw9B0MLiAgmcpitySwVjn7Ro_xWmnP8CQGKOlTK43EMO6T2M38CuwM6aQtKizh_Djk6m5Itlvt-LJrs2dcXp4E39_g4SJinJE1XDocXJKjtCzWj2OooAsyIzQ-KsmcehNVC1f_06x4K02tcSvhY80krbAsUeBgfXw238HOi6SDytdxdGFmt6njhkLrygbro9RDCv4u5jfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب پرسپولیس برابر ارزروم اسپور در آخرین دیدار دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102569" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102566">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Q7lkR_vpBFRuGp-FBDxPi2JUvalSQUtR_72ZyY7DEWXAmRGN8Sb_jMJDtJ2lg2MdK_qdnsFif8DyQ9qDOHCYC5H0GsdULXnEVRnRTv11dpy-wN9ug7XZo-c8aS5ni7HLRxb-cqzW3W9E51P0WbfUyVx_9YO3-otNeaXOWW1TQR35fMl0Hc06R2FHbs76OxvKtb0ctPTUDqMJzqVP_KMrIo60hWrpRsT7pBD_3tcUY1YuGzdn5-WG0jj1p2fS98Jp9qf_Mnbrlhzxm2G-00tttpA6W4-E6lrJMo6Zgakb49-6oHA-qGi9e6y5Y6ceplJ83EuOUAA1bWa49eSDwknmqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=Q7lkR_vpBFRuGp-FBDxPi2JUvalSQUtR_72ZyY7DEWXAmRGN8Sb_jMJDtJ2lg2MdK_qdnsFif8DyQ9qDOHCYC5H0GsdULXnEVRnRTv11dpy-wN9ug7XZo-c8aS5ni7HLRxb-cqzW3W9E51P0WbfUyVx_9YO3-otNeaXOWW1TQR35fMl0Hc06R2FHbs76OxvKtb0ctPTUDqMJzqVP_KMrIo60hWrpRsT7pBD_3tcUY1YuGzdn5-WG0jj1p2fS98Jp9qf_Mnbrlhzxm2G-00tttpA6W4-E6lrJMo6Zgakb49-6oHA-qGi9e6y5Y6ceplJ83EuOUAA1bWa49eSDwknmqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
این بلاگر دختر که خیلی ماجراش تو اینستاگرام وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های مستهجن
🔞
منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102566" target="_blank">📅 18:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102565">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=fKIdxlQ7hgwQ3YuKIwDXWIXbJKgJGD1CgU9OzaJs2NmtH4qWfTuiV1xmq4d2YFyJgitN1gqHAtsCEwFRXtTsmfVaLFoD4wlXLjTwO4-vhZRoGqKhxqg_3BZb-KnT_IKkK_7hrDU9Kd_n8Jl0OKDVMoYmy7yIK7PfqrrwDPXLshmjPh-btmrwJs58KH5IcUVlwQz7vG6Bq0UDEH4rLZ8dn-D3kwk0zt-cnB86httg0w_UCR2Or7-ZA4SoPlvvwaS3ntHDhRaTvhdoaRIdO7AA7qDejHynbH0qrUc7grRoXcHnE368_iinwfJ_l3S0fsxLQ8VcBtAHDeUFmfxCe7Aqvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7692adf8.mp4?token=fKIdxlQ7hgwQ3YuKIwDXWIXbJKgJGD1CgU9OzaJs2NmtH4qWfTuiV1xmq4d2YFyJgitN1gqHAtsCEwFRXtTsmfVaLFoD4wlXLjTwO4-vhZRoGqKhxqg_3BZb-KnT_IKkK_7hrDU9Kd_n8Jl0OKDVMoYmy7yIK7PfqrrwDPXLshmjPh-btmrwJs58KH5IcUVlwQz7vG6Bq0UDEH4rLZ8dn-D3kwk0zt-cnB86httg0w_UCR2Or7-ZA4SoPlvvwaS3ntHDhRaTvhdoaRIdO7AA7qDejHynbH0qrUc7grRoXcHnE368_iinwfJ_l3S0fsxLQ8VcBtAHDeUFmfxCe7Aqvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
تفاوت تمرینات بارسلونا و رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102565" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102564">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3-zkkGBaNjmKOEBlt_Is1jrC-3aKT7h52Qp6Y3h05oxOF8gt88hIgrz__nTduPyoW2YKH2p3A7DIAGVoQ6i9CBmWmjhEREoI0uEy6NFujQnMUiRaqqgL-YvGk9E2lBj5aYEXG0b5Yrz10R3ydCozPHm158QtedQ7qL8zs2_uLXAsQM4_du7cGOH0FoBq6ZuDQA1gQ9gZoXg7kwZkYr5XJR37qeamYDGYzh-UDby8SxGB69SvcMZQ-Os_yRtTldseW0TmZq43DUBJGRUy7cLqCCMwv_tsnybmkimfiiyV5veVA_9Ec6Gc6cGjbG8vlWRmJmbWlRGWzMD22l2q1ewFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
✍️
رسمی؛ کولو موانی با قراردادی ۵ ساله به یوونتوس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102564" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102563">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRXjIZLOsXEzux37j41HGcVrYqgj60JTq4wWcqUcY8pn-SzmwG9_Cln_Bab2W2xJoXTxnED8yZuuPMlVm4rz4taavWut-1JcVADc04IgiTW7n7aPG02Js5Tm2VI5rEyyPQwwbrPNusIOnzpL5sPTOQrP_wo_RDrR52wnfMDBlu8S_teL76pikrk5IJ5v6leNlFvFDPFVkCTlviAJfwIEjBDUYYNzMTfHjsCRES1X0nr8h-zHT6PCwrrejLAOPlPbc4VtoOgBj5G1dH8F-VA6xDQ8GIhRf6RZNgJAOqBuXD6vOzGWTDV_x6SSNwGtlTbsYJi0kP6J4bw8JQWgKLiQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
سال 2019 اینقدر اومدن کریستانته برای رمیا بی اهمیت بود که اینجوری در نهایت لاشی بازی معرفیش کردن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102563" target="_blank">📅 17:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102562">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYZCnCOUxD771-6j4m4wwvPq2AfRSNuF_yXh7HeFaFvI59XA9XuYeeYH3f2e-Yng4v5Qu4b7NAYMjmEuApaMoTXgHjWWhbErJZOeo7E9jOrg1Yq5xP5XAOhyRKAX5-UxAMvbF-ZHdXdGietod-4yCbDBP9S3KXyXVzJ3gGZxbnBb__bdmA1wF_FRX5u2tTvEvrxfZwO8wXY_Zvoa9OdmYoo36tNr06sdcXH3MPsPJCvHJuB8oY3-J2s8U3qhOqKSvqAKH1Ci9GrGG34IIyHI60AWQL2bCgVljKI9qV-UQLu0fsM4sVyQFT1TLI0uUK-Es2AnQz6lO1x4_2nV3iONRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
لواندوفسکی با دبل دیشبش به 720 گل زده تو دوران فوتبالیش رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102562" target="_blank">📅 17:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102561">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quZT2WHWpcT1uHxuVgN12DGZPQPiQpT8iKe7kObNsiAlp4-kB7X26JRXiUt53MNXLw87CXd5TjEBz9mhMXMQZS7hc6aKQHl9Veyw5OE1cFqHOVdxAXMnrgvlu-FAy0kZl2LDtuJSezA9UAUINcqRmV415KwgeCTqJXvPLmWAKb5NENO-9C9NZ3XmOVPdasPPCitHt17vDB-yPXeIBBNzBUodjUHfEE4DMvX9BFstTxxlbxrXvS7M4TYX7Hd6TUa0Ledpbi9gAAw7cFhMf-A9mmfclHPy141gAOvnYT08lir5Vyp0ETyTEJko3sICk3RdPGeovX3WEv9VXmPNANjEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات نیکو ویلیامز.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102561" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102560">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=HxXaF1bKJaCcyDZs5uA9WfJN5_BvKIvhPrHX5L69-RRXJhPC4bdTDvqgrGyy6up74S87EcRKMtzPy5g5wpfOlS0F2HYnjEJhi_RrZv1ilNs2Ec-cxHckwd6avn54z0HOZ5E7l0J8bqkbQcQdlDQFHT21SX-qhomE9nrWtJPgAtjHDLzrMeTtx0uc6wCKKeevsO6mpBD3fkBIB35gyejkWsq6nRwpbyix2f0271clnX_F7ncTge5NUQJsNmy0eC04VMcTMEj8GmMY_2cBtIKUsyV2dIbQ0vs9KPUtNMl5C2Sr3lDwS1OSqEkLtbwdImbr-NtcEH_C_9GSukHGyN1fhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e41261d41.mp4?token=HxXaF1bKJaCcyDZs5uA9WfJN5_BvKIvhPrHX5L69-RRXJhPC4bdTDvqgrGyy6up74S87EcRKMtzPy5g5wpfOlS0F2HYnjEJhi_RrZv1ilNs2Ec-cxHckwd6avn54z0HOZ5E7l0J8bqkbQcQdlDQFHT21SX-qhomE9nrWtJPgAtjHDLzrMeTtx0uc6wCKKeevsO6mpBD3fkBIB35gyejkWsq6nRwpbyix2f0271clnX_F7ncTge5NUQJsNmy0eC04VMcTMEj8GmMY_2cBtIKUsyV2dIbQ0vs9KPUtNMl5C2Sr3lDwS1OSqEkLtbwdImbr-NtcEH_C_9GSukHGyN1fhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تجربه پوچتینو از کار با مسی در پاریسن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102560" target="_blank">📅 16:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102559">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
خوزه فیلیکس دیاز:
امروز، وینیسیوس به رئال مادرید بازمی‌گردد. او ابتدا با مورینیو و سپس با مدیریت باشگاه دیدار خواهد کرد. فردا، تمرینات را از سر خواهد گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102559" target="_blank">📅 15:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102558">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCLYjQMWgo7kd-H2e1CMovP2oqt0EyjK9fjUBwJr-hxP5R4ab0yRiiy1EC_H-Q-ILDirqy4tYQ3711Xo98g16e00jNeI-pbUnLfMMU3o37TTrkNd2C6i6-JmxJZR73koAzFVXDUTwSE1W4tTRrP3hl5zg-5NQhn2KJzD15Qc4wjodBcDJKbcd8DRHM_iuInpHgzudbK3Z8ZmyN421Ahw8qhiS2yjT9lcwoJfNs9pGifKU8Ttd82X4LaOgmW1WXl_MXBlUWt9xAdzB-Rq1-ewesjJxKX4smoEEzNdhCyJre12OvcN5OsO9dIJ_NIH1COVaYFoVCzVbCgwtvo47LPxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
اکیپ: کوارتسلخیا باید گزینه اصلی توپ طلا،باشه
🔺
مهم‌ترین برگ برنده کواراتخسلیا در رقابت برای توپ طلا، عملکرد فوق‌العاده او در فصل 2025 است. کوارتسخلیا با ثبت 10 گل و 6 پاس گل در لیگ قهرمانان اروپا، عنوان بهترین بازیکن این رقابت‌ها را به دست آورد و نقش تعیین‌کننده‌ای در موفقیت تیمش ایفا کرد
🔺
از سوی دیگر، در شرایطی که هیچ بازیکنی در جام جهانی نتوانسته برتری قاطع و بی‌چون‌ و چرا نسبت به سایر رقبا نشان دهد، شانس کواراتخسلیا بیش از گذشته افزایش یافته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102558" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102557">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=YqG6K4r5VU7YaAgweLCm8oyPAz4UkPmB4cHUErOpp1U-Klk5-OxL2f3k46B88MTB4bAdf3J9ZviMwaRZuF91b4IkFCXTnggoTzDBjpYyPzILRaDD58NCwBsmeqQj9gvBv3ZnPn_Zw56dtPQFeePtiru6ZbDY0VfHMb5UfX7CgnkQhaq4oPmHDXYXWCDjMlCvBBtgnrjnFgqzw1zTFAJ_77HADYI6LUPOgZtsbw4cinut6wzrjtNQZGbAaebGR1ZW5QUFjeP4WuHNNpXZjIn2wG2WlJRwNf48G_cy3rW3FwpQsA4vG-2b90skWnYhJf4gItSk7YducESvDv-6qaRu4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371fc4291c.mp4?token=YqG6K4r5VU7YaAgweLCm8oyPAz4UkPmB4cHUErOpp1U-Klk5-OxL2f3k46B88MTB4bAdf3J9ZviMwaRZuF91b4IkFCXTnggoTzDBjpYyPzILRaDD58NCwBsmeqQj9gvBv3ZnPn_Zw56dtPQFeePtiru6ZbDY0VfHMb5UfX7CgnkQhaq4oPmHDXYXWCDjMlCvBBtgnrjnFgqzw1zTFAJ_77HADYI6LUPOgZtsbw4cinut6wzrjtNQZGbAaebGR1ZW5QUFjeP4WuHNNpXZjIn2wG2WlJRwNf48G_cy3rW3FwpQsA4vG-2b90skWnYhJf4gItSk7YducESvDv-6qaRu4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚌
از پیاده‌روی اربعین برگشتی و رسیدی مرز؟ قبل از رفتن سمت اتوبوس‌ها، این تیزر کوتاه را ببین
🔹
در شلوغی پایانه‌ها، فقط کافی است تابلوها و مسیرهای تعیین‌شده را دنبال کنی تا سریع‌تر به اتوبوس شهر خودت برسی.
🔹
این تیزر، مسیر درست بازگشت از مرز را به تو نشان می‌دهد تا سفرت آرام‌تر و منظم‌تر ادامه پیدا کند.
🔹
چشم‌به‌راهیم؛ به سلامت برگردی
#چشم_به_راهیم
#اربعین_۱۴۰۵
#سفر_با_برنامه
#بازگشت_زائران
#مرز_مهران
#حمل_و_نقل_عمومی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102557" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102556">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkKpVr4toQSYyTRkR_fErirVe6_gWNr0Mi1co-laXece74F-XxRufJx667vSe3eZ2cufeKxsNpJ0ndPpAQl_x0Fw_DmLJdKSCCxQQI88fK-q55EhzEHxS9wsyLLxh3skG582S5e4-DsMoTx-OrAjEsgyIP069b3vjYfmYskeL_zo1qLw9cRUp1ZI4BxR5qDBJu61LSyzc-k40QuTUb0uZRhHAt-nYSA0dnOUXgkLDgAwuPfgRR0zH7cw91eXcKDyos6Jo6LOHK-a77ddMHMYGFVtYChcTrZCMwEtnvbbHQJGmMS1ToajKaP5BbEBqjM4HVM4LifgoHoqLgCsYeHPLems" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed4912fbf7.mp4?token=ngZplXunJSoE5Dg8Zza_o-ETisTUaXDiK6W4IzTUURw_nx4_vJ6S0u1bSdit2rH-Mvfjif_xZ1G0FDa20iLiuAc_GqrydsCcXrP-CggC1LFflPz3S0ZBEH-oOCNMtQUy-9yeQUTD6cvny219L-e9PG8L7I2xiQBnuRheMKmfGvzt5TDffyr66eqDSwo3WXrPpfxag8cz9M_ic9V1vno7CI9GtozO-SUBqfCaO0k3_e6_jKNDjnpGhA1POquVf8uSFSOGyod_vU7MZ6_m6bxxn3gPs_FfaNKRhPzDp8BRYqk8m-0QXEYwVvdUXId2kCiHxPAIo7g19JWD4Ldxgz9UkKpVr4toQSYyTRkR_fErirVe6_gWNr0Mi1co-laXece74F-XxRufJx667vSe3eZ2cufeKxsNpJ0ndPpAQl_x0Fw_DmLJdKSCCxQQI88fK-q55EhzEHxS9wsyLLxh3skG582S5e4-DsMoTx-OrAjEsgyIP069b3vjYfmYskeL_zo1qLw9cRUp1ZI4BxR5qDBJu61LSyzc-k40QuTUb0uZRhHAt-nYSA0dnOUXgkLDgAwuPfgRR0zH7cw91eXcKDyos6Jo6LOHK-a77ddMHMYGFVtYChcTrZCMwEtnvbbHQJGmMS1ToajKaP5BbEBqjM4HVM4LifgoHoqLgCsYeHPLems" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
چند سولو گل تاریخی و جذاب ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102556" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102555">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1Uk_9QAJCvEfxYP-tz5zeKY8mQjDyPLxaMIdnDUGBgijO1NbYcoyrjO99myY4AJqfs0GWWaVIJdct39qJSIt0FLCVBdIwoya-wDEK30xpplNWJgxpVTrBxHFLWG2ReWAlurP-sMD-xaFAAHDzOEg1Gv2W3_TX9r8WINvmaDcExzp5Au88NwZsJTCDtagv5B3TThqXyx8C5oGOzPkffLl7-Qhv3J3bTqVMuiAoo7jKH_vVpJkF7ieSX_lVTHpnPM9RrR5fIb-y1Gofx2zCwuprvAfXifznOu7aVsT1z1fY04OTZ64cpLwA64CELUGASCBWUuuF9bPkH_2TOcEohEDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو:
مودریک امروز به اردوی چلسی در هنگ کنگ اضافه میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102555" target="_blank">📅 14:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102554">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5jk1VGjaUCpPQR3ZeX8Bg7acDdzEGjNW5DJjf62SHskb-5veHV11n3zjrtNONcImqcMKbsxXWTDTd0_4V1DOGz_D2Ux9m5QGHimfKNkwxgPKzQmJRMyQoNHPXYIskMBTiX-A89O6R3VlPu-v3e234amCB01IC2P0aDoj29IjPGDROfeCs3LWFoZiTMcy4WYpcpuUNHHmo4sthP_x8KDaf1EJlNbW3a9Y-aYqaslGTIaga6lTwK6xFndmX-yNJwRczAyICH3wH4KKgOtzjxsiaNoeOWYbV1HNMy1AKmzqo82MOcUPAU1AyixAw0q1XSth0Mo6ULVlNen_3NjEBgmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
اکرم کونور
:
🇹🇷
گالاتاسرای قیمت اوسیمن را مشخص کرده است؛ هر تیمی که خواهان جذب او باشد، باید ۶۵ میلیون یورو پرداخت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102554" target="_blank">📅 13:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlN6huIYASGj7Smf6hc7LaKzIhd8BHp8hjZAdfEf998LD7722uul7HLztEYVNHQv25eJm8eVydG-PCnLXr3Z-eJiEP0uytSKPbgD7LMISO7ZW0WB822SH0oB0Rm5aeMT_R6Vz5wl_7bxU-ljiuOjd4Gzu5VhdUEsKzxn1f6jasicdY0b6nUKOYr_-z0vbCAjAvIdPzRZDMqt-pZ8Kp0EQc6Oar-XupmOjQVh7pM0JX7DNk0pcWN5IH07RYhmDoeuTr2ULCTR7KjD4fCQphLiKd0IPdSZDQydXBSAtT_8GilvLxcB3x0F9vG-7Mvni_KTh9918wd71eWZwAGpzkqGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
مارکا:
اندریک قصد داره تو رئال مادرید بمونه و خودشو به مورینیو ثابت کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102553" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPY0GGNxxrX92Cnb28VwsSgMNeh1gdCQBvrDrQ6RcnZRf_MOheYF4rZ7u5MDkds2W4q-HswBUMDTiHRvKjLsHProRjuzicz_eS2uRVI-cyidIhAqcMbHgjb1GxZR2CdCP36gq1P-zVNe2E81GCFzWMxTgznow26q74rMWkvXA-47UWtp7bKsnI1qJw4bFoTOjrFLckpyswboNFgTqsK6J4bjxTgAVH2Ip45zTA1gKlx00iErQCNFWJhKdh28t6xl_86EhILHHFL0fymByX3u5mFmsRa_iuiCAvSXKZQ-IEjR1ac8NmACUuRik5bxt-fpnjmuyJ8Cb75xCn45yWnL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
مصطفی‌متدین از مدیران صنعتی هلدینگ پتروشیمی خلیج‌فارس در آستانه مدیرعاملی استقلال قرار دارد. این شخص پیش از این مدیریت سازمان توسعه هلدینگ‌خلیج‌فارس یا به اصطلاح شرکت "پیدمکو" را برعهده داشته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102552" target="_blank">📅 12:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMOn14awAl5Ultt_8pQdIdjkVEm7d8c5nRye5cSa6zhBhLbC848XBBomiRgEQjnFKW3hoxJcWhPbd-EeyrY0XDMpQfgH3OXDI2k0zKGhdkWt2GP61F6CB3vQF2Xh69S-JZa7qSY6Xt1hRIL-vfqXGnvUb9_0QdY518OanIOvtA3P4OdNLaTg1dBGo_qBqWEqVowoAiTRTn1B35KK-2QMHOkIaWsS2IqrXKImoaamXk6I-_jlSUYjmSUBsIJlQ2icEZunj0ebXE-swLz1hbptMEj4t_hP0QEEZvxRDLX96AYWbsEkq3ZsH8iTH6Qr_pxlxmepGc2Y0O8x2zdWwryajQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبرنگاران ترکیه‌ای: باشگاه تاتنهام با رقم ۵۵ میلیون یورو بدنبال جذب اوسیمن ستاره آفریقایی تیم گالاتاسرای است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102551" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoiQO89JwFFW4Ebko1wAuKxt_ELgw8EIO-hI1OPP076KNZu1doWS3LR7tctgtV8DwKUOVTow99epr_-XRctz3mkn5i5CET3rvarRH8hbV-ghq-YRi9LXhAu7xw3CmQGHxkDI7ppFvP-2t8fjo4l7ZjymOc7cXUR5TVJZmVMeSRh3shZGB8EXPwaCMbTpGzag9wxkfIhLlfvjUUWsK-UZcN59YHFDn9b-D_9Xn4Omt5RHjwYVsaSNIdsdoseQr_YMUCi6RLCfUWkXf5YC2mPlRcyUMFW1Z_YKYUF10ElogE5UkBtkD_Z5k-69CVj3bFb5nc6nxO3d_yP6pBQ5Dgqd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تصویری از مهران مدیری در سریال جدید مرد سه هزار چهره در نقش «مسعود شصتچی»
+سریال تا چند هفته آینده از شبکه سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102550" target="_blank">📅 12:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102549">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=VwXy0lYupCBbO0_8G8Pil1m2Bshb8N5WtBvnkndAxYxuSRakk5Tc_74S5Vc_O2YsWda341Qg1YkaF0wPwOXTtvhobYPf9FB19_aNxw7j3JAO0d9uEaZdu1RvR-fkmg2ffZnC6DzNkrr4aQxpvzKRc_ayIi6h15r_Fn8GDJxI9qDXVwifABLDz3bASeFxLgXaGkjcE5F5Ltyx64YBYItCvPPTKPT4_YP2jUskM1mPPGWpOtW4W30D0I5FtqEXR6PyE6QCr10MX0PirNYY8Ko4af3f2yUhiV95VIIe58Qs8_olh_i3ojBnGs4j3qGtvwbvgrqj0eB9o0VvTmVDivJQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a514ca93e0.mp4?token=VwXy0lYupCBbO0_8G8Pil1m2Bshb8N5WtBvnkndAxYxuSRakk5Tc_74S5Vc_O2YsWda341Qg1YkaF0wPwOXTtvhobYPf9FB19_aNxw7j3JAO0d9uEaZdu1RvR-fkmg2ffZnC6DzNkrr4aQxpvzKRc_ayIi6h15r_Fn8GDJxI9qDXVwifABLDz3bASeFxLgXaGkjcE5F5Ltyx64YBYItCvPPTKPT4_YP2jUskM1mPPGWpOtW4W30D0I5FtqEXR6PyE6QCr10MX0PirNYY8Ko4af3f2yUhiV95VIIe58Qs8_olh_i3ojBnGs4j3qGtvwbvgrqj0eB9o0VvTmVDivJQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سورپرایز شدن مورینیو از عملکرد خیره کننده و درخشان کاماوینگا.
😢
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102549" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102548">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=nFSweD3sFkAswfowla0BDAjJ_NF-ont5XkdB9NDP247cUMAH7XDuGGUid6_B3hETGDJ-re0liKTiU3em6fLh8coxbSfhjXEdyIK_B9K2c2wd3GHJWds9gQM0I_zWHy4Dc4xpBTBpQhsinNvgB25Jdk9-awyE8Ywoc9WlJb6DsR9-40l8vvzhHevr0oN1pSJAfXcduYmGP7-LmkScxWLBUz9TNbat-G74gXzP3cdJWYRUu0NDXu9Amgw3gZ-EiuH6ZvivcIuNR7GbqAhWFjRNJJK4xydabu7f6X8vcxSm_r7ds-bLpnGazKjdULWnSild4T14PM8ygHlvxHeiqLH8XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8a29e5339.mp4?token=nFSweD3sFkAswfowla0BDAjJ_NF-ont5XkdB9NDP247cUMAH7XDuGGUid6_B3hETGDJ-re0liKTiU3em6fLh8coxbSfhjXEdyIK_B9K2c2wd3GHJWds9gQM0I_zWHy4Dc4xpBTBpQhsinNvgB25Jdk9-awyE8Ywoc9WlJb6DsR9-40l8vvzhHevr0oN1pSJAfXcduYmGP7-LmkScxWLBUz9TNbat-G74gXzP3cdJWYRUu0NDXu9Amgw3gZ-EiuH6ZvivcIuNR7GbqAhWFjRNJJK4xydabu7f6X8vcxSm_r7ds-bLpnGazKjdULWnSild4T14PM8ygHlvxHeiqLH8XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
عملکرد ضعیف کریم‌آدیمی در اولین بازی بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102548" target="_blank">📅 12:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102547">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=MqjP001SryEJ3C69tSxDSb4tt3HsIf8ZQiom7u3RUCCHOQ_-Cv8n4lllCNs1M76aGf65fGCUX2Dsto3GwrzCF4KH5XYxBbq4YSfdECGqX3XAuhIANRbeSg8pNjdFKiXih3ahIbzBSOj94ilNIGP5PvpVCqRC4T4Zz7x0dvBNmAQo-04a5iAoNO1v_YyPQ_vT-TLhua8q9ia5MW-fCVE4ad39VQc5bwiBE2p5Xs2kk-YchIIMiMOnGArUAvODhtsdM0NSvvU8xOxQn6nrRSRBYYn1nzAsM7xdgePJJcSirl4wQXIa8o_waHPzFq2mkvpGBdLblacomiix-E7Lm4Xw5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233ef33c09.mp4?token=MqjP001SryEJ3C69tSxDSb4tt3HsIf8ZQiom7u3RUCCHOQ_-Cv8n4lllCNs1M76aGf65fGCUX2Dsto3GwrzCF4KH5XYxBbq4YSfdECGqX3XAuhIANRbeSg8pNjdFKiXih3ahIbzBSOj94ilNIGP5PvpVCqRC4T4Zz7x0dvBNmAQo-04a5iAoNO1v_YyPQ_vT-TLhua8q9ia5MW-fCVE4ad39VQc5bwiBE2p5Xs2kk-YchIIMiMOnGArUAvODhtsdM0NSvvU8xOxQn6nrRSRBYYn1nzAsM7xdgePJJcSirl4wQXIa8o_waHPzFq2mkvpGBdLblacomiix-E7Lm4Xw5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زندگی‌ برادر زمانی که لوگوی این لیگ‌ها عوض نشده بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102547" target="_blank">📅 11:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102546">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=pmvqTR6j3izjDfamwXuAWl6B9FYoebCw3CXpZhZK3oq1IGPSKtOtzjGJeCHAui8_uUvMTIvSS0RHPDZmeXo2LjBx8183nChlRLbM0kVKdH2Vyim5g1jdbMVgyN_nZl8TjOA89cHlS0yF_5DIdSBkKHsZqr3lMadayVrzRqQvMeED1mXhVkN4L8jU5Pf-Zf-f4mnEzBKYPr90FayCx_mN6feuBx7kFl2o755qUCqJRG95cUAXoqyUCZqgYa1aP9Vg3lrUHwURzQNfI_7ejuyIwbMjC4DpWcmK_jpLEmb7eoRpsF_pu6_p_wuOcacf7jjD-zwr2GYuqPa5-hs-mjRo_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2090c572a4.mp4?token=pmvqTR6j3izjDfamwXuAWl6B9FYoebCw3CXpZhZK3oq1IGPSKtOtzjGJeCHAui8_uUvMTIvSS0RHPDZmeXo2LjBx8183nChlRLbM0kVKdH2Vyim5g1jdbMVgyN_nZl8TjOA89cHlS0yF_5DIdSBkKHsZqr3lMadayVrzRqQvMeED1mXhVkN4L8jU5Pf-Zf-f4mnEzBKYPr90FayCx_mN6feuBx7kFl2o755qUCqJRG95cUAXoqyUCZqgYa1aP9Vg3lrUHwURzQNfI_7ejuyIwbMjC4DpWcmK_jpLEmb7eoRpsF_pu6_p_wuOcacf7jjD-zwr2GYuqPa5-hs-mjRo_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تمرینات سخت و نفس‌گیر بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102546" target="_blank">📅 10:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102545">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=BjW4xcSgH790KHOtfc4tfzAejeycNMNGI9g0OUPVFOErWuT_rRLPiv170Fy57I70UJLFBGGNV7enNCxEYlvTUFk6xb7Rv8R54ftycNyWwsGvkkLdhZrxZ9Mx6qgub3Z5qUG6I464PcOWx-t2vDmZYL4I2GP6F-bcVAqTH5IOSXkcxnegOzNJrY7eOUWO8S2H6t4u27S0vZkDVe1qhnYa-Ri82PVk7HUCp0TwN0f6QqLXCGk5w-dtFYX3BULTxMlZjSLwWtqxzqpq_b4VrgiXYhqoEyW0C_CLaCzPfwqOhSWffk7Vy1U2EdrOqgoOmBKCyxVGcYctDmZN8qHzS5G9gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f010d3bc34.mp4?token=BjW4xcSgH790KHOtfc4tfzAejeycNMNGI9g0OUPVFOErWuT_rRLPiv170Fy57I70UJLFBGGNV7enNCxEYlvTUFk6xb7Rv8R54ftycNyWwsGvkkLdhZrxZ9Mx6qgub3Z5qUG6I464PcOWx-t2vDmZYL4I2GP6F-bcVAqTH5IOSXkcxnegOzNJrY7eOUWO8S2H6t4u27S0vZkDVe1qhnYa-Ri82PVk7HUCp0TwN0f6QqLXCGk5w-dtFYX3BULTxMlZjSLwWtqxzqpq_b4VrgiXYhqoEyW0C_CLaCzPfwqOhSWffk7Vy1U2EdrOqgoOmBKCyxVGcYctDmZN8qHzS5G9gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لواندوفسکی هم در آمریکا پاش به گلزنی‌باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102545" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102544">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=vE6BpOhbcDcUlowSnKGpy-9vA3hwDQzj_Oa0pF1v1TUfB-5sDNtsp5RINE-ZUdeq6wEOlDsd7jcLGXz6YbYhpB4-vgYcKlSNpyU9lZfWF1JR-fhu4cpAU5R2EdeNrM4LhDcOXnUYlLTH_SJ6YLFmm8tZ6UuZjzHztPqwbKbpkxM1PMkIXCgbcckEnPQvty-jDm5jH_L8AYsdXeTx-W3AOsqD3drCQkVbwlSoh-A5LVrNj_0m9vKBm2c4sGg_pIKSx-Hxhx5p0_JGIZx7lps8cwgISIyrNz45WPlvuxDZRNqvE0VppFFQK5eOldNhMIyn3lALLQ3odhpuS6bdASURrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a652d9a082.mp4?token=vE6BpOhbcDcUlowSnKGpy-9vA3hwDQzj_Oa0pF1v1TUfB-5sDNtsp5RINE-ZUdeq6wEOlDsd7jcLGXz6YbYhpB4-vgYcKlSNpyU9lZfWF1JR-fhu4cpAU5R2EdeNrM4LhDcOXnUYlLTH_SJ6YLFmm8tZ6UuZjzHztPqwbKbpkxM1PMkIXCgbcckEnPQvty-jDm5jH_L8AYsdXeTx-W3AOsqD3drCQkVbwlSoh-A5LVrNj_0m9vKBm2c4sGg_pIKSx-Hxhx5p0_JGIZx7lps8cwgISIyrNz45WPlvuxDZRNqvE0VppFFQK5eOldNhMIyn3lALLQ3odhpuS6bdASURrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
گل‌زیبای لوئیز سوارز در بازی اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102544" target="_blank">📅 09:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102543">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=l5lJrV9nO11g77Ojz8O9ZwX6CbwM2a5cuLfc2xuEomRkrZfRi625nnKXp3pmZBkxVbHHO77RBPtlsC4hXMR5DPC2aS-l6NOIIHoAV4OsjBQvF7fC_QvCubOANrItkUYs-FJOo6ToucQZRx2x0PX09CFsnDqDfyFgE-tFKKl6sOgtxdUa__Sb3sQ6sRwkViuKXur69IVLkGrytrZq6NDHE7IgW3Jgdcw_mUyBJkpQ9WZtuOPBYcUVnmExhh3zuAfguiue0zdeqjQerKSmM8nBZabtd5V6h7owZGWDLfhvLGHK0nSFxCd0diNGCwA8ngDh6IAXGhIJRuil17uFUe2dug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ebf3b2b10.mp4?token=l5lJrV9nO11g77Ojz8O9ZwX6CbwM2a5cuLfc2xuEomRkrZfRi625nnKXp3pmZBkxVbHHO77RBPtlsC4hXMR5DPC2aS-l6NOIIHoAV4OsjBQvF7fC_QvCubOANrItkUYs-FJOo6ToucQZRx2x0PX09CFsnDqDfyFgE-tFKKl6sOgtxdUa__Sb3sQ6sRwkViuKXur69IVLkGrytrZq6NDHE7IgW3Jgdcw_mUyBJkpQ9WZtuOPBYcUVnmExhh3zuAfguiue0zdeqjQerKSmM8nBZabtd5V6h7owZGWDLfhvLGHK0nSFxCd0diNGCwA8ngDh6IAXGhIJRuil17uFUe2dug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
استاد کاسمیرو دیشب گل‌کاشت و تو بازی اینترمیامی موفق به ثبت گل‌بخودی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/102543" target="_blank">📅 09:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102542">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/im-NedTrCEHYl6aAOOTGVfwN1rxy6pOf-4ogj3wqG3TBag1iqppGYYmQd-UfjZrGWv7C9q8g-2TRVmZQZ74Q0VkDXYvtav1hX1OZVjzFaEZKGII1jRGjoKKojJAlgD8ZNljh4iImiyofNLsSu1TIgPgMpTBp9HUmKdS15c5hB43DADu_fm_dPSGVdbQefdLqQqN1y0XIvOM5wRgxzh-BCJ3CE6piNoQu8ujPtj6seF1RGM6DkJUYr7aOswaQimGUpL4LbOg2XvBr8DSzJ3lZ2_0mYuHN1wE_wQI6a9QNtw2wifToq8_dWODt1bEK2Q7Yj4VqR_kxE6DMbBEVaua_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
لیونل‌مسی دیشب برای اینترمیامی در روزی که تیمش به تساوی رسید، حدود ۴۰ دقیقه بازی کرد که موفق به ثبت گلزنی نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102542" target="_blank">📅 09:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102541">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=RpqydwcXgrqSR4v9lzKc-cjr34R_KJWXNl5mJiuBkNPWyMUXqUsPChjFWHW9YqPks0FuaheDd36ZbN3OCec5FZAEPJqacRQkzPrMzQ7DNobgZJ3eXR5SPz1Hc3fyN8DxK3wa5LR-ebB9Tg2oNch0ZfTZhTaHYuit6jlW-5GW34_nH3XdiYxDgGvyjKDa1izXSAqQphl3u3QOW9DySMq4BviCs9P12P7h34SfrMMpg7CxP9GyT85nQSkwHrY9dC7gFhl9bPhGF8WoZuX1mXmRNt-pfIscxx3TZFWwhJNPAFz1VH-kai5FzvM-9PAaCvg2Vud3ySItP5LokWcX4epiew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f4f92fcd.mp4?token=RpqydwcXgrqSR4v9lzKc-cjr34R_KJWXNl5mJiuBkNPWyMUXqUsPChjFWHW9YqPks0FuaheDd36ZbN3OCec5FZAEPJqacRQkzPrMzQ7DNobgZJ3eXR5SPz1Hc3fyN8DxK3wa5LR-ebB9Tg2oNch0ZfTZhTaHYuit6jlW-5GW34_nH3XdiYxDgGvyjKDa1izXSAqQphl3u3QOW9DySMq4BviCs9P12P7h34SfrMMpg7CxP9GyT85nQSkwHrY9dC7gFhl9bPhGF8WoZuX1mXmRNt-pfIscxx3TZFWwhJNPAFz1VH-kai5FzvM-9PAaCvg2Vud3ySItP5LokWcX4epiew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادی کنیم از این تعویض کارلتو که خودشم پشماش ریخت و خندش گرفت؛ بازیکن ۱۸ ساله ۱۸ ثانیه بعد از ورود
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102541" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102540">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYflTjRDIf57azZ6O3BB0O6DwVPAdm9BdbzHhxH27sJfYOm6gF9Vx1z8jsJzOufsRi7ZqNHG-grmBNlZYO5R5CkyNocm9sm1F8GegQP2AQlNLIJLBGsb87md-bBPRYdmGjmHQi56JaYNqEUiO0_cfT_wctCdl26hx_y8STb4j3NKllvQDwUb3w_VTN54qo1rL7I2995o-SWOhHNUIp_uMGiqMIXQJq30h3MF3Rbm_5dDpL3FqNFgy5AdZkHZ2Z9H5YTmpAtMebdN95BPslaJW3_j5cZFY65Ogk-pH_GklMrfcwC-b83E0Cu-TC97Cr2beDppDpuDEo6EkfyYaCQUWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
تیم پورتو پرتغال برای بار ۲۵‌ام قهرمان سوپرکاپ فوتبال این کشور شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/102540" target="_blank">📅 01:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102539">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=GR7qdetDDqzA5EyKrm8-T9aI3JbVsSQE0-Yrn8cu0QFQyYW-1zA1hEWAS0ksa83RfVmsdkQC0euSZIR0zDZNojR-VDHBV16ACWuQ-QcSyoyC7jBfvgaVVEFnk5p61KIm2i3PMy_BFZLazsSs9YPEQXi9CYZSMWGpGU6A7jZMRW_-k_6qwjfoNvMJrD4ilHDadKkuHEmHKRV2Ti3vVc6gmSoag5XO9KJQeWju92p80tjQx8X5XYha4IJ58s3bRugHG9U-6Ar96Kozx21P38TnXWIXEpFwIoKtKeqyHnKZaNmkvPvU0odGZ-R98MBr_mtRJovohI9QXFZAK7UeD7MpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27f4c2f037.mp4?token=GR7qdetDDqzA5EyKrm8-T9aI3JbVsSQE0-Yrn8cu0QFQyYW-1zA1hEWAS0ksa83RfVmsdkQC0euSZIR0zDZNojR-VDHBV16ACWuQ-QcSyoyC7jBfvgaVVEFnk5p61KIm2i3PMy_BFZLazsSs9YPEQXi9CYZSMWGpGU6A7jZMRW_-k_6qwjfoNvMJrD4ilHDadKkuHEmHKRV2Ti3vVc6gmSoag5XO9KJQeWju92p80tjQx8X5XYha4IJ58s3bRugHG9U-6Ar96Kozx21P38TnXWIXEpFwIoKtKeqyHnKZaNmkvPvU0odGZ-R98MBr_mtRJovohI9QXFZAK7UeD7MpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح برگزاری فینال مسابقات زارم کلایه استان گیلان رو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/102539" target="_blank">📅 00:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102538">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqKTGktOJCFf-UJyWgKXflunUre5gIN0Wqrt5eM5G13yeve3DD2DuKhgT69jblOwOYIyAmY-EDsgZKW2AeHLsI0ioZMDTle3yerhvPvOE7RiuieyYoT1aNwINl4OHvI87N1XPb4fNtasi4-86jqQlAIfGBNXIzEr3RiM85qBASEQyaA7sT9zuO828c84-EX8NWu8589Ejmduf2Ixh7SAoblf_FBdUx99ZgVdgCPWGiGv6sj58NUTDFyutbyKipjNctu27YOQ9wbe6M6ureJfB3zME8bkBPF760wd4V9o3DR0VxzXNS7LmrL0UddNtkbiSzNik1yiUCSEAIQL-syXf72Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93530c3ba8.mp4?token=P_wd8NUSf94dEYxIvCH6OEai1J7J_EUSOiNsm_KNvMUlWTrg32R0BOiJdZd-ksgs7u7Z9z45GR3cTWCTk1x-UpFo9tIjW7EAAyEGYnctobZG6cIXju4x9q12te4WqPafk5h1uDZUJ724FLUh7G9ufyEdnxULbaoWOJCbKywUvCTUmjoWMTfdsgZ5YTuZ0TPN25iyurQk2pamuMNQWeHurTiM2IKlQl2hm7UTg69qGRHVuE6zwe4AfLmTxsNZ2UVQ_Pw2WnwUUf-gooNP54kdopoZ2H8gmPDEk4Y8h4mqZ09KzyfjScjsmrVqCW7dB792GkjXYxV_mzXfIMF3msCAqKTGktOJCFf-UJyWgKXflunUre5gIN0Wqrt5eM5G13yeve3DD2DuKhgT69jblOwOYIyAmY-EDsgZKW2AeHLsI0ioZMDTle3yerhvPvOE7RiuieyYoT1aNwINl4OHvI87N1XPb4fNtasi4-86jqQlAIfGBNXIzEr3RiM85qBASEQyaA7sT9zuO828c84-EX8NWu8589Ejmduf2Ixh7SAoblf_FBdUx99ZgVdgCPWGiGv6sj58NUTDFyutbyKipjNctu27YOQ9wbe6M6ureJfB3zME8bkBPF760wd4V9o3DR0VxzXNS7LmrL0UddNtkbiSzNik1yiUCSEAIQL-syXf72Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت‌های جنجالی قالیباف درباره لحظات حساس اولین‌روز جنگ با آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/102538" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102537">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی #فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102537" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102536">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G7BHNopVThcWOoE0OeqJym24PjRmaM29Y86IDDB5wXBDoxkAnuPfCkYB1FmGwCFG91jnnP0lJKtzLuoK-Fne3-SlMXfvbdYSuM3Zi01oKfxb9QuyTDvaVBFP4s7Ih4IstefWYgXqKknaFZAnMFZlRR7Fa7z_ovRFhmxMY1YIycVtePC76BfGaFtqB6Q7ernv5NWe2-43ZcYpLZUrcY1eVeNDafiEAoNqYbOe8eSaDpx60vtCKmz_hHfrdbi0Nfvo8msE14l9Cpjo39R5s7V9wnoYE7pT3Njphos4h6OdFJ4KfSrNIClTBZ9b4eQL42lfSJW8G02SVB1eeKDJVOK1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#اختصاصی
#فووووووری
❌
بمب پرسپولیس در استانه انفجار، اگه بشه چییی میشه عجببب بمبی بشه تو تاریخ ایران
‼️
‼️
‼️
https://t.me/+W21WaISjE0U4M2Nh</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102536" target="_blank">📅 00:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102535">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=BAUk_wl6MzHAOE_Fodv4ODUai7tBSHIve0_4bFLx7sb11991w2YdiLM1fT2uMSryUspGKuQAdka5MWKvFqpjfK4eq3L_UJCk7zHJyGt2nR_6qZCbDyr2AaokLfSXX5FB1Wohp5YYIFMggw--JdO1qeupwTnF2Gp_kSj6JkwyqjTMk39I-ynQ2iVJwmbvutZRmC24WGAebDoMZUwFz_1n5wjyaftShgO4Som0xgQR9tNBT5C367ETQ3FNRcdI38iFHUxiz11luvnlFM3fSn3ZQKMB4aJwdBzuvO7iBFuvpq2LXcGxbyT6i75qxcV4yF4ofJ9yFKbsTA8rh8A5C55xUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15b1aab08.mp4?token=BAUk_wl6MzHAOE_Fodv4ODUai7tBSHIve0_4bFLx7sb11991w2YdiLM1fT2uMSryUspGKuQAdka5MWKvFqpjfK4eq3L_UJCk7zHJyGt2nR_6qZCbDyr2AaokLfSXX5FB1Wohp5YYIFMggw--JdO1qeupwTnF2Gp_kSj6JkwyqjTMk39I-ynQ2iVJwmbvutZRmC24WGAebDoMZUwFz_1n5wjyaftShgO4Som0xgQR9tNBT5C367ETQ3FNRcdI38iFHUxiz11luvnlFM3fSn3ZQKMB4aJwdBzuvO7iBFuvpq2LXcGxbyT6i75qxcV4yF4ofJ9yFKbsTA8rh8A5C55xUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاخدااااا از این سوپر پاس کاماوینگا به توپ جمع کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/102535" target="_blank">📅 00:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102531">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXi-w-JddEGuPKTzQP_1THHk5ukBE8-MZCJSaVeaNxIzv7YIbvxIPq1vu_Thd2xZfeiTWtM0cocUYX6D9gYq3vG8VOZOW0Y4Q7AkenoniuWO6sx1vz77LG2TC-dTlJtwJ4vgLzxpPJ8_ZT9iDFAhGsYGPYb2VGrOwH8Fl6ubecV4Xzdg8ABfL08qOgr1QoXCc4znMavRL-4t43gR-tTwaL86IyreVuVrka_hp70wva4cp-ZmnVw__U0gWs_BC3rmkvTwZ5JQZndvGu1oJd7wSmSZt9R1NqHOYMsdMPTq71MTSjFa_Qew2SbAUUWxMWeO81ABfV3cXH2_eq198pY_lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H21WVUC4QjPsmuT4KI9N7FXSVHbG8A9rpv8iWBe71x81Ao7ChR6PrIsc6W_LGCkjAJBP9aOAh4xua51EpvqT2jTncxu33Wz5wi29tzjN_TqICdUqNA2vnl5ze-AAXMymokVNmqHYViWXiHl2Bxu1VH_TgH1jCCD6l5rMbHdDtM-TBX99VQP0ktIet8BCQbyNEk0S_36PNbKImZM_XkGkOBdfaxdDzIlGIQM-ZMmA8UBSGrn4JvoNVGT8JQXa3It1DVsO4Grerjy2tESlqCZXx2_SZJkWVe0XokmO6w7ukGrYKcoELYFGoqulswoA4NxuawnYxPiyF_Q98hjnS-18lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HoC83WbwtjorMJYhhoThszNWz-eGJZJyrlnYQ9gbNPKhK2oH6F_18uGhXeEagj-oXe6dD6nzc64U0bdoM84vrdEUwf03LkP7Q3kPrSE3M7zjR2EtexA2FUf1m8Z1JZIjtykUxvVbSx27G5jTzeVuYR8eIxPrt1eH2ubsW5yVwt69jShcnnvCb_yGau_Sn-92RSwLLRbjRQz0unWcHHEgxRy9fcY62Ve_YWQ0sLsoDDRTVgpubhR0UMMi4Xe16K98JFMsPKtwNBuKTONoX_wnbzCAT7IOg1wUCtbthi86Ji3CM3_F8p07_JEMXtTDZ5FtuU9rXQDnw-Av1c3rbrdETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DnNuyHBXRBDRG1ITMFXWNqkqcUO5UOAk2waN5-LzRAvoFlKcnvzKxej9WgrZBGZLGSCjeNEpfdA3b7RObl0jfn7ZTtj7spIJ1WuOfEh_oJQJyZKU5640bKdMzDdiBINxcwn5BvPdoZAB57vgibM-mY5SpQGBuICX02DPk5k8tb11ZXvFVJIiJGcwylRzIc7Tvk1pK1dCBgVlVBvey83QGxCjmNBcsJiZgzvhI9km0FdBNab18JJMdfO2N1LiCyUGTVbVvh6GhWyvqwSXRNRJEU_DTNMB1M6FDyYc_vPHlbRYoLVyt83ZCL66kysJnbh2G9aHi_9tfwtgXPY0Kk_bKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
عشق و حال وینی و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102531" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102530">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZUxVJHFf51cPVFRm82A4VuSLoifopvWlOkitUsYX2Ua_70Krw3VmrRslhctA69DGeYf5B26Tg0jRYQ3ocm5ctCDBAB8RtLBTIDhHknzW2adgKzD7OjeP8FkKt25CIlF1pSMMGQfPE-Mg4ehuPpnHrIabY8ngfmeRvHL3_0b_SU4SbQx9s1B69GZ72YRiO5JkDuNK43V-cz3_5gAAN2K6APUzj8YeTyPxXNIHij1hT9krMhKDYhcC-h7iQQEmhlDkA3mFzYclSMGCfoEjDcYrRx9S-xzxKQCcL2MACqMtAiNdDfSZuxmdS9OKmYkneORdhrRnQkxOAu6VUgE-NG8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
مورینیو بعد از مساوی امروز.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102530" target="_blank">📅 23:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102529">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRXJ738a12SExS01x0pPycmA217fr1aXXwlRpCHoPr7OqNHCkprXKhaxbAkjzVNbn82AhKhit408FAdlTblDZzO4QLgj3E2uBG45tJBBBqKW5iZeLOfAtU01GQftcXtTGr0KQTF_AC4H6WVnyZiC60IlH49mVdRmNmr5hUxydqUWw6cctgbdaXaFzCnUVmBOnc4Z9b8YYEwSnBWo0XCZISs1rkSyvFtD5j1CzhvqIJkaIivy2TAQVTjp_Lj8jNqy6N-SHd3FW3wqh0Fv3eRCqIpILRSboZ_bzns_2WPqhWDR25JO86U8f6p2C-cvROW4QWlMbR8XEdhKCOdZtGph1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تیمایی که ولبک در اون بازی کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/102529" target="_blank">📅 22:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102528">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaNH7tzLMzo7C7HHUbrLb4ixBxjbxoNGfu4uO1jOdA2pp3jtP00GeqMFTUaDtexlVFPSE8tirK7tani1hnb0Tq-wCl8leEHydaXcwPxlf6t0-tXz5elYvWrqZE9tQWrWwCUndu8txcNNPUKP5RRpTenN00qQ1kTAeBXTr9FukTRmyVVmN2G3mo7XyK1pz4sr6CBQfW9PoRGov_w1OLlASdZo0Ro3q8g8VgwWo0wJct0X7lYH9eYAPReTp6CrzOCTVVB5hgshYBQbr57sYUTZb58rKWgm5gDt69Kl-wLVoAJcBpT3xxAcizUa9RxtAoUNzt97VLJeJgbgmNsBVqE0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال هم تو بازی دوستانه از فیورنتینا کامبک خورد و بازی مساوی تموم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102528" target="_blank">📅 21:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102527">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2kTcGrgmI1vP4xlwFFSUwmy_zHYPpGJjb8emuMJlXrxCnnMvYt7UgbgyO8cj_Dwj2rTsgABXJ3F0Y6wJsfGw-2LW_Icr3aLu3Bhd1UeEK92sft1NoKspXLhlNM5GdHRMtil8eih3IAy2_awfvu92z_qcPfSdSbaM1SAbLBlNLptH1g2wkEbtw009jgNfhBAijdMISdIr2XmDwUZN_BTMsnm7PXRvbxk2aVqJjfBk3msIoOfikNjsKcY4-_ovFMGX9iJf1Z-MLGMgyiCHXw0hQ13Tu0BUUvCXzNI1dMtiNbg_-xdqeNSmaG7s3pWBDDdyFAU8l69sYj64gLQ-E0U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کارلوس اسپی:
🔺
پنجشنبه: بستن قرارداد.
🔺
جمعه: اولین تمرین.
🔺
شنبه: اولین حضور در بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102527" target="_blank">📅 21:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102526">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP4RqaRqoxbgdDO3wWv9tPeNmDzdJoZKOlMSrJa8-va0sOcmXzQkDG_LWFtPlMAaRPUfEJ9nuIx-GiR0TKl242FIDqc2PX8Dc0lAdGZjkv4RCLqSdSpBbujXB7SWnaM_I7vGeF5mXCdJ_1fFM1s31OiVQJre0Zb71m1waU53ONMtTVjLZ3RRsOZYQsyEi3JUdpEdpaNCdyHfVLZF5DfI2FEig5KTgYUnvyCSxCTxGs2WbHHRMOuwbXnhwmbpu5GVA6_YEVycuFmrgipNT5AetuNxBs0lSV9BBOwOfImNmXMfMRsvh7QF_rOKBNGDTMMbH_QCKeCn4a_VyB7zmXx8Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی‌دوستانه|ترکیب آرسنال مقابل ژیرونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/102526" target="_blank">📅 20:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102525">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uztapziCdETfWdPg0t1LZk-XPYR5C7NwPT3-j5VYbDetBepRqEHTEqPvx8sE0qFHrof-6CkikIjtvGGvPg3yMNGc3ImXVWWnlCeNUBayl7m-4jQ-UsyoGDzG8YHoIPAschAjXgncBEKFu0GmUbBS_j1G24oA_U2JRxwVFuoLlc9PXIxC_67SX-YmDs-w6FH5pYFb4wqPzu0c1mwPcW2ydGAGs5LysRkBD5PYPYH8ErZhNwwlSSzuAdEX-9DuZHo5Y3dd30on1TG62r2ap_X_9I-DXVZ5zLFuqyU85J3SM4t-6D0D6VNDQKzB_KltPLeYM6vKfaEGd6y7smbFXKSIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامبد جوان با زنش چیکار میکنه اینجوری شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/102525" target="_blank">📅 20:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102524">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltt4m3bTrCfk2SRq2kP8Xvg4A2qzNbKyIBRlGBpFZ3tL_A-iLszvH7GjXL0Q5xk5W6cB7jSKT3-4bQwaimP3Hl65Wk6uf2Fxd51il2nBgqbGeweSfPyClY9rfmJd7X7QkmS0byH7T8JzqHb5yhy1LjePE0euouvlhV9iQDrll69z8WlqZnJQKIu4OAqULtcMvDvdaOZGbg_d9IzG9Rkn00mHyTp4j2U9Yqo_Ii7vReuoAORhvy_xX4EY93Wl2iBM4rt1NJ0OQP46Afrb-wEM5H65HorxIRM-zgZM0avUNRGlfYHr-o2CcMfqQv2QbZiVHm3eWt_9yBQZemJp-HAPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دنی ولبک رسما به چلسی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102524" target="_blank">📅 19:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102523">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx62OfdDdTf9NBA61mVtwIf36HTgsJ2kRwvtVPzgIs7fzmMrs3gRovpUxYbBaKK_esksUihvoe4o46HIZIK_I06aIOLbV1SeBzeSPH0C8EOjDPz0DQJ-kPmUecsQl6oYu80Q4Xpbg5bUtBsQYxl79Bbf2B4e35CRNUjxTCAnPtOJaJMNdR27EsU5zJ6JanEjB5PXyR85-mWWyjiNxvurs9eEeLpS80kWBn0gu1N26zXOqb-mtXjTnwcDQoxDsEKTi2cJM9aAjsFd8Gju2eB-G7drIrfe4peoZYfCKTQBbMCIz5SD6RnGSCOIkcOGYNezZ3J9dSLGYcctA_Wo0cuBXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جاکوبز:
جایگاه اینفانتینو در فیفا بشدت در خطره و احتمالش زیاده که برکنار بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102523" target="_blank">📅 19:37 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102522">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nb7aZOdcR6XQP8Lbuv9T1GS2gDtXwLmLEkxRGGUIlVtBNMvXxcSvski4YFVla26HFbBp1HE4E2vK89MEn_W4FFwXwIsL6qFNSqnNbctjtGb7Sh5RMDpje6YSAq8wtYf7gCrXimlTWc1kkBEa3wQ0xROiI_NWTnL21JiCh99gqe-gascombif1WdMlZ1v7YZy9x9hBcajpmCMUEWLZGZM0hOaILO6YbFhugrDMQAo7v8p7PWFrmez8awU0CDOH6_MTbzgfFBzPnQZyjl1E374Zuu_KkQjLHv6j9p5umgdRR5aIxv_pApwHZYaQ5rPg4EATNDf8Ca9oTa099_hjyXQFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
🔺
انتقال های رئال مادرید به آرسنال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/102522" target="_blank">📅 18:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102521">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Na3Dm_CIyUEUJZKfJAnum7zsa-ELx9Z-yygzSxM4gp94TdSnfj8cE4NPSarIU4C-nZNc7uzt7VLzxdylOJmFWBhjgoz4rwI1wLjDldfr6Zc3hSWSkCf--BLETlm_LlFIDDlgo2X6cpuYrj5mqruWxHEW7kTPKvP1V9hLnmxZVNTjX6wLT_7k1YSPmejjf7dON9qJw98Mr6tosxhv8lYCdAYEq22WabOOD-J95Gho-YvMTAWwyxvGQMZMJ-o6kzPU4rgBUCzR_pP-nu8YOKbuI3PbphUqEt6G-0pbnMJ0SuGamCF9Dg-JjMe7x2gvy7jRjsmK9wdIThG9ynRs0jSy_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مقابل فیورنتینا در بازی دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/102521" target="_blank">📅 18:17 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102520">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9FAb_y_CGRS4-zIiRLP2lzmTnbgktHBe1Ee7jH1jAOsO_V0rhonNhW7-Wi6tz99hzIiHM_ssQ3Tv6O5qg3pPZ0chtphN04EETHDfA1rlZ89DdfJLI4uU4jfOWxwywn6tVLkYcrtXRAxqWEYpP1NArnCQNe3jiLl7h2gtqRgtiCqobnUhX8iCEP3Jo6Cbl_PFNHYLVra0-R7GPP0a87ZO9I_QpaD8OxMqcUUI2h7IwjAIds3bERk-7ulgtW4lG12EPevZVImukXqYABynw5q8Zv1uvUN8vvHBPvkRCVpS0D1KHOUexLyhf84pjpCXmJAFLgnajXbr2bre7C31iXqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوکاسل رسما لخت شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/102520" target="_blank">📅 17:51 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
