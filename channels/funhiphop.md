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
<img src="https://cdn4.telesco.pe/file/ewYgmAiQoAO5tSPyrplbGDmnZHEGcTR4rkQuFLk2VoUXlgE6QR2eX9XHvfYnmc9Oe-dlUeH8dSpOqG2zXTwe-I_RMP8XuhVmfvYlKuqBTNIO3giwjWBHl7Epon21MHTARkjQoJEqsH7Fc5xpkzIWfdunvrej0dlO_TAY06DWr1G0XTxb3deXuq7vXv-XWUsifIXP4F24QwnkzSp5-Avk78DQAYxIz0WUSOaLLAHpLWQxe1lwwt75Qo3xBK_rYEm38qO18yOouMkHBTkCjs6rYg-nAI2CEToyZkicc88DJEsGmG_FZuKFNznpPnmpem-reFkUzvTo_hYJdrZZY_GsFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 255K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 00:41:31</div>
<hr>

<div class="tg-post" id="msg-83912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سازمان مللو عصبی کردید وایسید الان میاد نگران میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/83912" target="_blank">📅 00:23 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">من به شخصه اروپا رو به خویشتن داری و کاهش تنش ها دعوت میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/funhiphop/83911" target="_blank">📅 00:19 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مادر روسیه گاییده شع دلم خنک شه</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/83910" target="_blank">📅 00:16 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/funhiphop/83909" target="_blank">📅 00:14 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روسیه به لتونی که عضو ناتوعه حمله کرد</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/83907" target="_blank">📅 00:12 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83906">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جنگ جهانی سوم استارت خورد</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/83906" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83905">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بچه ها تبریک</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/funhiphop/83905" target="_blank">📅 00:11 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نخست وزیر عراق اعلام کرد همه گروه‌های مسلح عراق سه ماه فرصت دارن که خلع سلاح بشن و اسلحه هاشون رو به دولت تحویل بدن و اگه ندن باهاشون برخورد میشه و مجرم شناخته میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/funhiphop/83904" target="_blank">📅 00:08 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqy2WRxMuTpksf3L6lvailBYnNAphk4Ucoq2ziRFa_NmyxB8xwciN5x26D-8GvK2M_vaQ5qqcpaDDQUMPSds0004BjR5xohWqVwnpqXzakYgotzur3WBmC60_L5haKiVDz5FJfPIuSScjT3DlgCTQNT8Cn--FVgofRZfFHiijjKueLgDjkXQCuz4hObwmGdOAPu6A1g8kpQ3ovYsgfg69AzVKreKPruiCPyau7FHRWi-Qw27hlb4V5WtUIHsNaPiQkimFIXhl5WusrB9mozQDtTE8Yp2jkEuE7rU-86I71prAYtPZbpwkfAzZeUphN8jhGn2NSIXlTcX9eXHylEVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح حرفه ای بودن نیرو ها رو میتونید از کلت توی جا خشابی تشخیص بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/83903" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuTXl4x9_TuN-2P-biDyuTgTLxUeXIt0zOeaOni60xwGNTcfmyKZ3xJ7f65DfZuYCwzcfwN-7zDL8DdJQrlAdkWrhKiq7fFm_0rL__1w2BKm4b364SyNAqIvr4KdF4_DOFerXp88Hai5edcGI8watx9HUiScOBcYa8kTQxQpF5NQx4bKEwSsYgg1etxiyRlZItnH1LdDXsDIsm7Ov1B5--pz0KInm1okv3sg9HTyCN83zVEH0dRmC5BdFVI5n1XJaF_RL28bn-ngkz31hQ1LZbB1n7b-674RSQrLqE0OA0JvY_oYZhSLyuV_VMD_yXmUkdCLSPx3LSnHjYNt4Q-cIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حیف نمیتونم به جیک پاول فحش بدم اونوقت بسنت چنلمونو تحریم میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83902" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=p01dz6TKszaTAG4lz6edTkwZOYB0oLXZLztDW6t5SbXeNCYEoxLXWb_nR_5gj1Qn2vKmeY76pOs0evcDWYDPI0YZ2WoQRWdSMmp354MrWwf9Q_gsoUlRk5k6lxq3pgfA3U1K9o7iyMmjQ45FHp8TWhyi-rXMh5OU2SPq24N3gHjgw3LySYJe3DebqgDVV22AmQ0cNPC-8j8GFEZxEGe3kyhsJZ76vPv9g6pYTs9k9llaKnLUivnKtDDucGp6U0kEXIGyKlx8-tsBFSpLGeQGHLrHBi-UBIK5OSg4l1vThywjG7MaMWNKq-ULynbhAOUUnKXe1rSCRt9NEdMIp-Vfers9cqVJL5sAxEWOiOMxAUrVSe84MHzTjUR-56xaBqPVb5M0u2Vcu19NoEEZYXFP9zvtmTcHQ9xkoQWz1ZrE4Y2zo58ZYHJQW8oMRfdRvRolPAC4Kop2399563Kbi_sGOerF-gNWIkbHvyY_uCNM4QfzwreuGX90scX54N08wtbwmBlWhMTV4QxoQlJyZkBzkyUTWpH_tKBKhLqxJMp0A2FW-5fRx3_Jny1003tAhBY66sTGcdIlA7lp82qXHIh1UYY752eVT2-hdK6TipxoIjKl01Ht1tZMlHI_g0ToN8z-4H2Z_zevDuyc1TrWmH1-AxafOiJa1yIMMBbsIBIJVY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01a45378ad.mp4?token=p01dz6TKszaTAG4lz6edTkwZOYB0oLXZLztDW6t5SbXeNCYEoxLXWb_nR_5gj1Qn2vKmeY76pOs0evcDWYDPI0YZ2WoQRWdSMmp354MrWwf9Q_gsoUlRk5k6lxq3pgfA3U1K9o7iyMmjQ45FHp8TWhyi-rXMh5OU2SPq24N3gHjgw3LySYJe3DebqgDVV22AmQ0cNPC-8j8GFEZxEGe3kyhsJZ76vPv9g6pYTs9k9llaKnLUivnKtDDucGp6U0kEXIGyKlx8-tsBFSpLGeQGHLrHBi-UBIK5OSg4l1vThywjG7MaMWNKq-ULynbhAOUUnKXe1rSCRt9NEdMIp-Vfers9cqVJL5sAxEWOiOMxAUrVSe84MHzTjUR-56xaBqPVb5M0u2Vcu19NoEEZYXFP9zvtmTcHQ9xkoQWz1ZrE4Y2zo58ZYHJQW8oMRfdRvRolPAC4Kop2399563Kbi_sGOerF-gNWIkbHvyY_uCNM4QfzwreuGX90scX54N08wtbwmBlWhMTV4QxoQlJyZkBzkyUTWpH_tKBKhLqxJMp0A2FW-5fRx3_Jny1003tAhBY66sTGcdIlA7lp82qXHIh1UYY752eVT2-hdK6TipxoIjKl01Ht1tZMlHI_g0ToN8z-4H2Z_zevDuyc1TrWmH1-AxafOiJa1yIMMBbsIBIJVY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار رو به جلو
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83901" target="_blank">📅 22:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TP8NN1i_ftEpmF3PvNIQvwvU7q5TVi6kDv0D54-Bv5OgLXl_N9DpPLOwh3ie08Wdlgj0fNP0nVmAlWF7smegFaM9kkT_wO9gxxYjzif7MHZ0IdxNJAzuOLyWErIU37UFqMncXGfxFMwTUGR7FZ5-pc5cSDopWAvuedg7xZBUm3e8qdWLf1wsdZONoFiPpmt6R9eTfg_wV6R2Fy51cwXRUPtdDJJ1k2u74iknRGUTBmCN5KB9lbuvTjfKG-qgjt87eUZAuvLraEwxdDet1zQUCQrXecRiS3zm80iyZkOFvD8uhWgh_yULR888f1-PnaIbh92ujQbktv-KbblBqCOKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی چیه این؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83900" target="_blank">📅 22:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: کسایی که میگفتن "۱۲ سال دیگه بخاطر گرمایش جهانی میمیریم" الان میگن "هوش قراره مارو به کشتن بده"، در کل به این کصشرا گوش نکنید، هوش مصنوعی خیلی ام چیز خوبیه و قرار نیست بشریت رو به گا بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83899" target="_blank">📅 21:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به قول امیر پارسا و ناگهان تیرام میس میره</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83898" target="_blank">📅 19:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83897">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=al6EzquoUQ279w3qIH1DL1g75XlEP8D3SdMLfzVszBHpEYA-44PwV-L4HEDrS2uIf2qBuauQMH6D6nJy0Y4sJXalm3wIeKf8245JbNxTqMZQMu6e_SVY5IIzPidWjia8p8fKSg1RMC5yXWVRelZLOQjpq3DE1lYpRzV3uVCVyfuOQnreoyXN6Mjq2Eh27g0Wr6H93LXkUV-dyS6LHb7m0GRvar68gX_HgFcY5FnwIwK1cLX5xDomARJuLWQsbp0_BG3cml8jCLIH1NPER6pvRx7-eFokAmvVoOGy6gCigwT8CI6rkE_V_sfnZO1xXSWm-x4Y8QqH-f0-qMvsw33Y_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e9a89e6.mp4?token=al6EzquoUQ279w3qIH1DL1g75XlEP8D3SdMLfzVszBHpEYA-44PwV-L4HEDrS2uIf2qBuauQMH6D6nJy0Y4sJXalm3wIeKf8245JbNxTqMZQMu6e_SVY5IIzPidWjia8p8fKSg1RMC5yXWVRelZLOQjpq3DE1lYpRzV3uVCVyfuOQnreoyXN6Mjq2Eh27g0Wr6H93LXkUV-dyS6LHb7m0GRvar68gX_HgFcY5FnwIwK1cLX5xDomARJuLWQsbp0_BG3cml8jCLIH1NPER6pvRx7-eFokAmvVoOGy6gCigwT8CI6rkE_V_sfnZO1xXSWm-x4Y8QqH-f0-qMvsw33Y_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حس میکنم بعد قطع شدن ویدیو کامران و هومن به شاهین نجفی پیشنهاد تریسام دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83897" target="_blank">📅 19:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=vdtxgid5dGdicuMq0ZukppvcmheM2Q6H9wMQGgW5lCjYKP0EkZZs8kwGYZqfZ1Xm3dVnwgKHSFJyuOTCwBEfcrJVyld4XVOEgO653AOR1Mi2j5mVnX0OSms730vEGlovIlPrEu8GV9Nyf2mu_FLxShKSRAbO0QYSR09ldjK_PfWtO11OmhL71D6ydHru-fLnxynjkQD86UpZEdZavAok2zhX08IHrM7QBi123eCCrzUgJDrgrRDJUT3paVPyT0ML6K6w6rC8NGl83o5oFw0h4vZcjRuwbsb4Knp57-EeeKPv4X5HDE71yFo0fUXkbnhA6wsc182gKU7XgA2vTTSlLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f095302c4.mp4?token=vdtxgid5dGdicuMq0ZukppvcmheM2Q6H9wMQGgW5lCjYKP0EkZZs8kwGYZqfZ1Xm3dVnwgKHSFJyuOTCwBEfcrJVyld4XVOEgO653AOR1Mi2j5mVnX0OSms730vEGlovIlPrEu8GV9Nyf2mu_FLxShKSRAbO0QYSR09ldjK_PfWtO11OmhL71D6ydHru-fLnxynjkQD86UpZEdZavAok2zhX08IHrM7QBi123eCCrzUgJDrgrRDJUT3paVPyT0ML6K6w6rC8NGl83o5oFw0h4vZcjRuwbsb4Knp57-EeeKPv4X5HDE71yFo0fUXkbnhA6wsc182gKU7XgA2vTTSlLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود بین دخترای دبستانی:
میدونید من اسمم رئیس جمهوره؟!
دخترا: ببببلهههه
مسعود: میدونید پدرم کارمند بوده؟!
دخترا: ببببلهههه
مسعود: آفرین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83896" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یکبار امتحان کافیست
👆
👾
🙂‍↔️</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83895" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83894">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjYcs53ihT6A17Ys2IfSCXQBXNcB_W1JnjoCQVrg5RGUpf3Jegm1fG5iVAICQ3leNdq27jx1VRd_x2s4M8UJVwKtiwRK8dunK9jGuScAgptI4lSKx3-3uS24RxI9iU54RSXbUAEUAqPfThWxRlqYvPydA4LgfXKiSWsAnT9COqgN3d0ulaV260RkxFgHpidRaS7YEepLkyr2fPG0MggWj0LMIxhxrO_xktKtlpbsifBKGWqel4JkHxG1gtneHhgxam4gQ55qWVDNm_ApTqSj6GcvtoqT_Y2qffUn0Fx_B_wGRZtOmumhf7Krbrm87GNRbGzdxkD2E-tylsglNVrbhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g30
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83894" target="_blank">📅 18:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsWts4CoH99AFD9uWHFyVNtFooNFmejJ6Ukl639tv1AsYeDwSHr6HqUPlmHimN_hVZpFgAu7FFsaJaeGygDOHzTx9ABw66AhvldwwECvrcI5KaoY9S0Z8AcR10e7k0act2BrgavXv8PvHRNG-d5hhyyl0X77E7dL3n2upByUnBd59rAXcqh6TA9jueFcEc8yK_EQWl6SgjdXp-Y-_XjS3JISf31c3GFXvXfPzHZwZEiUic01xYhbYLsrrALRWR34ofAwnuthlFeqFplxsazT1WZjjybsvBLnu8poQpqrJNyrrAoK0_-yE7r1_JbO2PwBe1x5BCRzjkq6S1_rohLtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83893" target="_blank">📅 18:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-KHRpa-Es1Cjpy9kEWxrDUPiGe7OB4GsA6JhbjNuLeS5jENqTHF7cQl1KpfBZ0UpfaakgjB3bc6iioPTBX0S63tlqAb9b29V9DRxqyQWGDgOTa4mEr9I2FZisG_Y9BLJG5zbKCdwzQy5Sg-s_HWqEe2mnT_WPtNOzPmrlxQ5-H6F1Jcf_ST1_eJLbMGHu2a-B0bZi9s6EqAa7WrYndnMl_iAnv2DNpAWLkuwa1pYLJdhloOoD93yldU0kGlLIKERWWXIEyART716-LY3_HNjGUh5R_XcSs9WC0tSBpTz5_0BaRh36mOSXTMx4JSGgygTAEfG215VTX8P2w4SeEXdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=XzjcrdRNnnMDzamT8sIE5c5Klv2hfVuNHqpcXzprwSk6jUhL5ylkHdczAQC6Bal1fUzftN22fo0BKMdDsQvWs8PK-tHE_7G4wvWEuxhpM76ZZMLwRycgCaWbM4mMVzJngEKSitco5ZoqTL4Bz2DaQv1stexzAHzav3SSHC-nsC0NRzdJMf75U54oxWDPlHsTY6Wf2NoHOMszIZTTQJJI1Dq0F2pL77YexSRCocnmY-Rofz0WfIC_V7kHrhZ0d6W_udIrhZIser-iepJ8xFFYgO0Vibmf25m4s0ij5fm1Dp56BhQPF3bfby-LH2GdRZkTNVReHn9vjOu3tfGR9MgImQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dceae7f4a.mp4?token=XzjcrdRNnnMDzamT8sIE5c5Klv2hfVuNHqpcXzprwSk6jUhL5ylkHdczAQC6Bal1fUzftN22fo0BKMdDsQvWs8PK-tHE_7G4wvWEuxhpM76ZZMLwRycgCaWbM4mMVzJngEKSitco5ZoqTL4Bz2DaQv1stexzAHzav3SSHC-nsC0NRzdJMf75U54oxWDPlHsTY6Wf2NoHOMszIZTTQJJI1Dq0F2pL77YexSRCocnmY-Rofz0WfIC_V7kHrhZ0d6W_udIrhZIser-iepJ8xFFYgO0Vibmf25m4s0ij5fm1Dp56BhQPF3bfby-LH2GdRZkTNVReHn9vjOu3tfGR9MgImQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشکان کاگان یه ویدیو از حضور ابوطالب و رپ کردنش تو استودیوی کاگان منتشر کرده که به شدت طبیعی به نظر می‌رسه ولی خود ابوطالب اصرار داره که هوش مصنوعیه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83891" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">منابع داخلی میگن مجتبی خامنه‌ای اجازه دیدار پزشکیان با دونالد ترامپ رو صادر نکرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83890" target="_blank">📅 17:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueQFbDjgogxWg09k3D5D0UII6C2ut0WML2vgrAo4SEm-138g-2vTtVkRujnnAt8goYW-L8pQOoQZBDsiz7XNO_6mpjgewVBpSFTRgAnL--0hKUZYoCK_qzLZ7rMPRmNCfciEc3fFPmPwPI3Gai3j-ZSYMqEeVfmJjiwmaYTJ8IpM34s6ECKiy6JhL8H1O5XxZSwHLvUJ_CUF_Tj5avXzx3q7PEZn48ybYlOMVPmQbh17htvLcUyGZREoo7eudqpR3c6On3uqgqf2rJ1iqZGMQh46__WuJF2NHyhkOBlh-5C9eWlABOwqHi3658Ty-HMvUB4jVlMO5b7yqUAWoGgHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر کپشن دیگه‌ای این زیر بنویسم میان منو می‌برن پس سلام
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83889" target="_blank">📅 17:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3lTQpLDqc0Eam5ax6SCDbhcherIbKwmxp3eovPtk8NS2Rtueo4G8WBCziiQmpKseywhuVRekj7rDmzqAQdlAFuStTSsWxvbEp4xuuPn0wDkCrmQRxycwvjisbUDk0DBu-XmqV6YisJmR6bVd1QvX8hCHnfPhmgXcVIxtWQyzwiKawNqpJ_tHnKNPggKSOtJcBJVPwJ4LwlLBpqq_RNvur-pYPj5fJCcNm2sp1HtCxJvo50nOgcSlhz-BRpahb3PUR4YMFHHePNv1GpOQzgNgyKRu467m4gqPXPJS9S3zGOFj7EbfILBLjWTJYA2IkXJRTtJrivJ3kt_pqdb8l-kdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی بازیکن فلیک بود میرفت نیمکت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83888" target="_blank">📅 16:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufMj7lqGjEperX56N5diEcG5YpXQjYzImCM3Td-D8ABEm9vNT1Z68IcL2vXJLK7rIgTq88WVqRBqcivUQr1Ole2_DwkdwgnLML72t-jT1QL-gyX0G1U7mnZ3LHTEYBR-U0SQ2lVyOCuREasUlivYin3oZu4ifl5PLSJld2QzC6J6PkBaiHLdpharasfQJ4G0nVNNgENTXQLk5dTCn8R_VovOYSdKcnaL7PiHETsk40sXm25lYNjuNnEDus4AoNbm0SWUwj04UE50Z5Z9Z9wwwqXMJATZbJ7FMoVC4ffMdDjx4aKXxZtEaTbKrcXl5g72cI6_4IwB9b1htPvalK_2GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83887" target="_blank">📅 16:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=TpI_28mh2HT823Cnvu_kb5C_LlEjy1rbWIqg6Xq2m2KfF4zwTzmSxFSVPsnF7OWjenDVXvJCqFv_vqm2-UQssWiUYvzHkLrYGSKHd6Q2LJqtCxF9LWYDnbbs68FN4d82UuDi4P154LjrZ9LhbMcifoyEBMDQGKOTjWYXndKOS-PXdODd4RNcJAXeQOFyDyWHVba2QGcLJbm3_fFZSPEoi35ARQoNSYsHyeyjBMSke0Iu189WT93lGDiVze9v2d3KmNfl7Nhh4zZMNqVo5xEyLdfMhCaAArGQq2ACOtwfe8bXwqf25u_AhJd1waGHVZPT6XfK8Br_gVVcII2vSUCG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b416ce1a.mp4?token=TpI_28mh2HT823Cnvu_kb5C_LlEjy1rbWIqg6Xq2m2KfF4zwTzmSxFSVPsnF7OWjenDVXvJCqFv_vqm2-UQssWiUYvzHkLrYGSKHd6Q2LJqtCxF9LWYDnbbs68FN4d82UuDi4P154LjrZ9LhbMcifoyEBMDQGKOTjWYXndKOS-PXdODd4RNcJAXeQOFyDyWHVba2QGcLJbm3_fFZSPEoi35ARQoNSYsHyeyjBMSke0Iu189WT93lGDiVze9v2d3KmNfl7Nhh4zZMNqVo5xEyLdfMhCaAArGQq2ACOtwfe8bXwqf25u_AhJd1waGHVZPT6XfK8Br_gVVcII2vSUCG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی سطح طنز مرجع تقلید هامون»»»»»»»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83886" target="_blank">📅 15:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آقا کامران یک نسل چهار</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83885" target="_blank">📅 15:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آقا شما بد جلویید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83884" target="_blank">📅 15:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJRRdqLUe49XPhmLPrE0ph9WF4nvhF7Gw4ZcR0e7oKI1v5QvGuEzj2f5tDl0yg9fCyhzB_phhK-xw0dbH529DRjmfW4zwFCQKUOZiL-MmgLiMBs3Gby-gOIU31jAynuQw0cspyzT9QdI3hhoFGTQmAf5HTdTV9JBDtoNVPCL0Y1rBo5Tv8iPx7ikO0472YYeLCJ3rgwhWMVn3ZGI8L0Y8yLDqkva-4l8YH_1sQjxsBQk0_LLZ2mpPtSFBHmBYdM8FLzMj2JB32a_j0qnGPaissZsIg10NegDLM3GvENNON2UCLdRv4xXneDbQhYsAxmtm2pMAz2P3KveNpJTAJXoMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا شما بد جلویید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83883" target="_blank">📅 15:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یا یه رفیق دیگش سرطان افتاده بود تو خیابونا تهران میگفت چرسی پیدات کنم زنتو میگام</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83882" target="_blank">📅 14:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83881" target="_blank">📅 14:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فمنیست ها دهن آرتا رو گاییدن آرتا مجبور شد ریلز دیساشو از اینستا پاک کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83880" target="_blank">📅 14:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیرانوند گفته چون تتو دارم مشکل اعصاب روان دارم، پس معافم کنید از سربازی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83879" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خیلی وقت پیش ی پیشگو گفته بود ی یوفو میاد و نیمار رو از زمین بازی میبره، احتمالا همونان فقط تو ترافیک گیر کرده بودن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/83878" target="_blank">📅 13:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhtW1MDQvlV66iqkQJP40YZ43VRhUjnbR2zG-dUi7SOVK2x_VMyTFknMMD4tToD93wGuCUEQSBNiMoU_tgSG5Ghmti0Efu9c-2zHK26qh-079KinyczbQkksN5IWr-otEQObN-kujejvMuw-hdT1W0j6dbJhzhT35srmdaCBKcjkQpHKphd6cKgHNZmnN1QSo4Ge33hwLrKkloAVVD9dxGlc_nuXTP08-g3u4-HEJgEWLkpMonhFWhEd12EZ_EH5tUZMK1wSa9w90E9jHTu7uui_GrZPTjdFj5RnYLnjhpeh3q5_MIb1PQFOWSB92n16CWQThlEeWCRs00ZyQFhZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادرا یوفو رو هم گردن گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83877" target="_blank">📅 12:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=eCnO0hYgdPZ1I-7pnpo3qmpg6GUk35hTfD5QyD4VF8QcOQgfsKp3BWA-0Ptsw_3NWxlatGmTPUt8zLmLDKnUIZjXOImMsqcpNNSv9kUq3RZ9vU9tR1TAPetbwP_vvTh1GIngHwLP9AHkEgMSFVv_knXfy4OC2ymF4wlWwTtxWwWpO8Ui08RYQ6ZXtvBu7KLIYMYFj0G77NyyEa3jMqIHvXzhDJq5MR0pX2tZOWfniYmF_4BBL59slgxjn5sV6OB7lbgNefwvm_lXb3o2SA6ooqwt8mi_5zSHTDRHhvc9_g0K8sxXDykmzShrhpaG6wyryZpGmIjIdWAfxbL2KbyqzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a7a08089.mp4?token=eCnO0hYgdPZ1I-7pnpo3qmpg6GUk35hTfD5QyD4VF8QcOQgfsKp3BWA-0Ptsw_3NWxlatGmTPUt8zLmLDKnUIZjXOImMsqcpNNSv9kUq3RZ9vU9tR1TAPetbwP_vvTh1GIngHwLP9AHkEgMSFVv_knXfy4OC2ymF4wlWwTtxWwWpO8Ui08RYQ6ZXtvBu7KLIYMYFj0G77NyyEa3jMqIHvXzhDJq5MR0pX2tZOWfniYmF_4BBL59slgxjn5sV6OB7lbgNefwvm_lXb3o2SA6ooqwt8mi_5zSHTDRHhvc9_g0K8sxXDykmzShrhpaG6wyryZpGmIjIdWAfxbL2KbyqzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83876" target="_blank">📅 12:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WhH6HVhJWmMgCVE3r60KyRYq8-sb4ONSPSWJOGEylncZyYrRfcsCE2IMYy40_Z9Brwly2LKNByWlWDmVRmqptCyncqKm3cF1RZ69EeNMRwwzreCFX30uYcEOX7AZibsH52iLvMbDdNK-P77eTWzZlo9vSaT11mfV4EppFqLGwuIdgSBfE8NMwtyUEHeOxM4jkOmaZGosVbA7rtqCU9t5G8a-eftp1tc6IsQhKrAYop12C4mTkm5TGAOHTgnCo49KMTkFjuH5poI_Y3bj1Ecl5SKSXbPSRwxl4pbMo9KzMLn13Bg62kFDdO-dQ5kqv3hb3j4Xhw3usbZa2DN5JnRTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینجوری حساب نیست اگه میخوای علاقتو بهش نشون بدی یه کار دیگه ازش لیک کن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83875" target="_blank">📅 11:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=iO42olTK1ghmWEufAKdJ5G9B9dfJhj7Fk1YxLG8zh76Lidq9W2-GWblc9m8bkw8sm_1CPv-J6IhuQm0mUpAqKzPLNOME6r7xGmJKiXneHcNSWW3l3unB6d3M9oB3KqmwYjGL-tJFHuT4zEH2oaxYMHogmUuo74NCLWZKgtW9S_YJCtAGqCif5XkBXntd_I13L1Yh3aQj0Y7r1ozs3kZZL43pKYtK1wNQ3PXJYkIM_jESaOLMsY32sD8BtCWaAUP7LzWam7D-TG3onT9RQC_IE2d11VP0aUe9bxkgtewkm8MwHTmSbELmWhosx9Dugb8jGYogWVltmemmnEM5is1KcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c48db08f07.mp4?token=iO42olTK1ghmWEufAKdJ5G9B9dfJhj7Fk1YxLG8zh76Lidq9W2-GWblc9m8bkw8sm_1CPv-J6IhuQm0mUpAqKzPLNOME6r7xGmJKiXneHcNSWW3l3unB6d3M9oB3KqmwYjGL-tJFHuT4zEH2oaxYMHogmUuo74NCLWZKgtW9S_YJCtAGqCif5XkBXntd_I13L1Yh3aQj0Y7r1ozs3kZZL43pKYtK1wNQ3PXJYkIM_jESaOLMsY32sD8BtCWaAUP7LzWam7D-TG3onT9RQC_IE2d11VP0aUe9bxkgtewkm8MwHTmSbELmWhosx9Dugb8jGYogWVltmemmnEM5is1KcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83874" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83873" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9b9R8YT84vZmuAftZUpPejTQj1nNSobYITrZgDWhg7j_dFIxgsa5SjPBUuoS0A2MyAPkxPyTF398xD4OzD9NmNyqNqZIyx76cnL8RyKiL0OvO0Co9flN9jL-bKetkxuE64NfExs6z-qbC8HagEplj7-unvo8VzJF5V_NaLsXpjeKHDqV8UTbZ_l7WXyjGnS_v-Aododpa_J4XNqU-dn291VGEqStnbFvT87J3dff_-kjGoO2kpzOnDGnts0YhP_7fmH19RmYFi1YAptWLLGPMPdZQPVbjGtMpFtCDRbQDmcmVFKC9vJSV0VNjdKgDktS3lvBV_cgfVQDHqpJLgItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بلژیک - جمهوری چک
⏰
ساعت ۱۷:۳۰
🌎
📲
اسلوونی - صربستان
😀
ساعت ۲۲:۳۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R30
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83872" target="_blank">📅 11:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgNhSrLnI4zzQm6kJjwLA7rc_ErUj3bzFONxe4TdF2DMkm5L6FM42PXEhatJQt_Br4Od-4kayyDxmL_eI1cvoWbDny6cn0nOUdtuZVJvlPDNqXWpoHpLOp49fktX2S92isvlDXqRJSnNCzE8Dfirp3CA19gnmP9V4Gx6zr5pofjD_zsg7syT8ENyQkUt0SJV3vQvSdvQvVGmBnvLNhqt0BXiVNOlWc183SSoZ7POJVpbmlGCti5usfrF-I7e8FiyIh76BF0QhLnbpWTMmKHFniFETLxUNa7nRPATagrywDvoI6Htv8ZXKilRbjlPbhttzUxz1d14umwsXV-8_cJFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممم عجب شب عجیبیه، دیده شده در آسمان تبریز.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83871" target="_blank">📅 02:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og98ENghO_iXKX0zox6pEKhZxnD6n1S3hRQDG8m_7EwdeElzFS1KZ6PVe2WV3cqsvQeG_vA_nt9lkTJScJOLzdddTzxLNed2arRljzNPcaT6hnkDOTwhjiHBAjDnyn4cM1fbVkGbmAG95ODjj5qKwTiDUYdbXErUF8qmJ4ZvEVMR8eC-lW-JPh87feQBz4HJgumYQs6kwI6gqGvrRy2c283SQGZxcDdrYovp16Dfdfz_PaIFCKFjPtc0MzJZRSkFKxaq32Mdm2_QvsvryZB26vuz2mYKGkspcG73dBIancTZIG8oXa-mz44Q4uGYF8DJjGVyTbSP0WZAVIAX5E841w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83870" target="_blank">📅 02:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83869" target="_blank">📅 01:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83867" target="_blank">📅 01:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/83866" target="_blank">📅 01:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شاید یادتون نیاد ولی خیلی سال پیش ی بنده خدایی با فوتوشاپ ی ویدیو درست کرده بود که از آسمون بادمجون میبارید و تا مدت ها مردم فکر میکردن واقعا تهران بارون بادمجون اومده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/83865" target="_blank">📅 01:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ببینیم مرحله بعدی دایناسورا میان یا نه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83864" target="_blank">📅 01:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=Zv3RLRpDTN5dTSAiXBMtgzGJ3pLhwUyjWreDIqcn-oLWX813feOVFgv9d1Ii1quIfASm177NFvbR5ZXqGBaYCqB53X7yn3XJE8ISkEh0nLW2GQ-hoVlJLK5vkdxh3k_L7QLvFv5GNjRzFrhoXxcJFjkMsR3csx_GVGGkmYLasPQN5Qo8oV5ly9cXQSLVydlmfQ-SxvPA5eSKBGwql_Qv-20wDAL4LDIz74RMznf01Z9O7328tmxNvn9YJmei9j1YTc9K_Ip3d8qIZfK-e6KVwrv3TnQCVqIWQJ8iP_pTMZI0mU8T3MrQYPQiMYsIRht_Vy3WHY2nwrZYusk1eNfhpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b69b54bb2.mp4?token=Zv3RLRpDTN5dTSAiXBMtgzGJ3pLhwUyjWreDIqcn-oLWX813feOVFgv9d1Ii1quIfASm177NFvbR5ZXqGBaYCqB53X7yn3XJE8ISkEh0nLW2GQ-hoVlJLK5vkdxh3k_L7QLvFv5GNjRzFrhoXxcJFjkMsR3csx_GVGGkmYLasPQN5Qo8oV5ly9cXQSLVydlmfQ-SxvPA5eSKBGwql_Qv-20wDAL4LDIz74RMznf01Z9O7328tmxNvn9YJmei9j1YTc9K_Ip3d8qIZfK-e6KVwrv3TnQCVqIWQJ8iP_pTMZI0mU8T3MrQYPQiMYsIRht_Vy3WHY2nwrZYusk1eNfhpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد  @FuunHipHop | FaRib‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/83863" target="_blank">📅 01:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان تبریک میگم مرحله جدید آنلاک شد
@FuunHipHop
| FaRib‌</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/83862" target="_blank">📅 01:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شبیری زنجانی مرد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83861" target="_blank">📅 01:05 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4-w9j0lFj55aukUbt4a4TF8OpbN-quBlWWFbxWuKJSxG5M4BzLLF8LHVnNzbC6suDcKeK-1JRUNOU3Itt8HarwpY1Frccj2HIb4fEmFH__NA8KOYJfMk7D1x7UsbJOeIWNApkni4c1NifaxoRKoZChsUbwSIQiMx6R2c5NSMfe8QN7sGDcHAodRMmH6AtO66vyYYnCZ9ZgCGrgLTNZ4Gg2anIlNOZdThXtlHfOeJXjEgL9wMh6pZo6CL1WnDBVWfDFkiP7sVBMAZdHfhu_Slr8DAypI3kjzLOO9OuGflMXEIElxg4TQ0_YyBBMk1nLujjbjPNL1mOfrSKMdmKcXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبیری زنجانی مرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/83860" target="_blank">📅 01:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BQeUFcRqjDY_NYLtFK6Uk1zb4-qPd8io7PBWDzQdMf8skdn9DNcjfoDI-wE0UJRxwUtmzDBVjl4GclAdK-welu3tK1d702-uEwvozAqph-VFJdW2oeESSsfL2fqSGwL3sGN674gF6vnYEHc30O78M3Hc8qu6XAEAPv6YH6UdzMVLS0nscSQ1q6Fw8oGYVIo8CWoJqD0H2F2ij8y8VSFE01bOTBj6YOCB5AwZ3HIDjlclLcSS9vJRUvszjtSM-7QKq4uu6FBpgTf3BydyFSerjyEa9gXiX6sHPh6mj6ZNiUiaJR3uErne9slATQhtYdLGCwsf9_kFSFr9oSnWB4XVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C5UQGYXp3VRMtdI_YU3_daWVr98tv0xPbYnvYZF1HtRtlGDSzXIjYY-5cvuz-EtZRRa6OfZm-oGcpef81qvwMBY_7Ws5udB7HP9cAGQ51b_ZEEC5NrEhkaIzH1tzuSeQGCr5-SMInL2Y5PqOYS_2yPOsw5iSPIlYmD7FMBYZy-_oSJiUK7P9nMXAEdhN6AxFMkcfII18mqWHdozu6MbDAa3zqIkdJOtNrmC1PlvoxqSM-DkLmivpQ7d9I-w3p3cRQxE-xhxiOpsa1ufLJ8cFuVckRZZ-OIqZz4YMFNvSoKG8dp8fAfulpB7ZlO9a-NDOOa3OwNPrasTKzGI7ThyHRg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">چقدر زود پروژه حکومت لو رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83858" target="_blank">📅 00:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0053OAnsAazcZPy3PycjWy7jQdP4VIMs5fStRpbFWZDPL6AzOICRsZwrZRCzew8G0yc47xz_ozTTRBUhSEIjT8gnjKMlpb0q5FIMkjMrA3-EQ-pwTpdW2rJ0_VUP6PRTcMEAgL7T4iRChaYAofTGJcO7pLQEGZ3tmn6IseEUVoMbQpkuxSJ9eFPull7Lf-6Kak0kAka23c4yNiHy1mfiDD-d7RBxJVR6AnERBxVn6LYxMpdJMOgBmF4mrLi3BhAXciH7LwbZMnj6FicsRJXD4gJydhf15aozTp2TKiLYhtGbWmZ2nhqIQUihSC8T4JTMgIwWpeYZu4P_-ZBYfRKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلطان امیر تتلو را آزاد کنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83857" target="_blank">📅 00:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">همون منبع
کیری
به طرز چشمگیری موثقم گفته که صدا پدافند میاد و جنگنده های جمهوری اسلامی دارن بر فراز تهران گشت میزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83856" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">طبق منبعی
کیری
به طرز چشمگیری موثق بزودی جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/83855" target="_blank">📅 23:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdfYMwWnHQ_O54NvxvOPRyFLKfPLcZPZP4vMeE9_ZqeC4blfYymjGhT61ewxfNBknlIY7NwLrHbeRHDm6RuQaatLknncmRAEkCVqke6ZkUL0KtDjY7bdaaGqWmPZgP4KfIYhMsaiM2ypFrT48e314g9PllQqZvubPeWuZvmJL7AJoPdOcKuQIEyUQw4gb_e3YrM57ZTPYN6dCNETPNZvWEs3MZhMFZo0H5lRg3NjtOkuWRhHQich6bOzTtzmZbx77jUiLMElduMvSbIRGnrzGesMHLZyBQjLE0k3PObPm1-BO9Hg7UWhH6GxfdVuU0HHbbcCun01nAmnS4dydFSuLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اونایی که براشون سوال شده امیرمحمد بزرگ شه چه شکلی میشه داداششو ببینن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/funhiphop/83854" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">به امباپه اعتماد کنید، الان میزنه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83853" target="_blank">📅 19:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بمب خندست این مورینیو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83852" target="_blank">📅 19:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">این کورتوا چرا نمیمیره</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83850" target="_blank">📅 19:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئال باز پیشرفت کرده پارسال همین موقعا ۵ تا خوردن از اتلتیکو، ولی امسال فقط ۲ تا خوردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83849" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یاسر آسانی > وینیسیوس
عارف اغاسی > هویسن</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83848" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سر رئالو بریدن</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83846" target="_blank">📅 19:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بابا دربیارید شماره 4 رئالو از تن این بچه کونی
حداقل خطا میکنی مردونه خطا کن</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83845" target="_blank">📅 19:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دوتا کارت قرمز مستقیم داور تا الان نداد به بازیکنا اتلتیکو</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83844" target="_blank">📅 18:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVYUTTiAMt1xV6GSdPfx2M-Gzf9H4Z2gzPRjEUoGUbTsA7Tn7uDvf8A9tYOXRu1mQVor05X84Gz0T6gDk5WOMEHzb_URbKxq63Lx-sWwrMrtObSmBOHnsuhvBZkDGBsiusA99Yy0oJGGZSlWDw0NXsuqIgmF-AQOlb9egikwHWZYoCCAeMKJ9yjkrjmaFVMd_ZU84PL4PGbpluwUxaEe9FU-YQJAoapRX0lisHPIy-p3u6n84uGvYOLVKTC07eO5-4UvwEwxxFac5hlV0pgCd8lYj6LmZcXAlycNjy9KFKBi9JErrmxtPg9qrs9T5YPuycd5A6ShZnDoEtYchjnUJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید با دایرکت دادن دونیتش کنید میخواد پول دکیو جور کنه پس بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83843" target="_blank">📅 17:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lcrtu-3PdhhLSg80kLiunBxi9YehOcuiRfV_esVFM48RCrHHNtFx2wHy_AUD0j5FZEkT_bupZqCDku9icOnmwi4bS7G7sysZLMjn7AUQ7U_05Yl77hDz7WhXClSzGqIc3U045f7xemUDnMOiiCOfn1MPig0p7zj5zADka07IRw3g4ekqCAoBab5D4pvoUzbucSA3DMsLmOnShV_1KqCpzae0pwW0PaCs1pvW3nwjVgVoKpWJwPGPZQP94sYriGnarK9eHLlYNs7n7bCMkkNaj3BmUKHRUih4Q9xnwVXwoDvV89YleBVjO1Yb7OUl4JPpRKeOgaNnWtjQill95WLN4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت دربی مادرید الماس مادرید رو ببینیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83842" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLBCMVSx63F24yoMOMB4vIJs4goyqle1buiMF0e6YriMQZnEM6LDceXoDdmKIoAeXHyoSgBYzFtoxRZ9mKZQptEZkOwR74gKIwTOQgmdIklQi6Zs798Z61-hDeak7VgTWN3XAFg567pOUXN6sxsaihp5phzJcRXoIOgdxyNL1nbcVdMksu093cAHxlX8na1lfSwWQqq3PnqWJX_XS-0HfVvqjvMkKAktxrU6NzKVFaau7XaU9j_8414PTT6lHm2zz_7JKgLKJX59T6NWFTU85WtoVAO3JUX4f4hUeCADqpdZd6vS3t66Jz3vpeO6f9Iv7EAK6divSLHm41iZxB1HtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👁
سود روزانه میخوای؟بیا بری بت
💝
0️⃣
2️⃣
🔤
سود برد برای اولین واریز روزانه
👀
😎
کافیست با مبلغ دلخواه حساب خود را شارژ کرده و برگه شرطبندی سود برد را فعال نمایید
🥹
💵
10%
شارژ بیشتر برای شارژ با روش کریپتو
🙌
‼️
برای اطلاعات بیشتر به صفحه بونوس‌های سایت بری بت مراجعه نمایید.
😀
🤖
ادرس سایت:
🅰
g29
👍
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106
📨
کانال تلگرام :
👍
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83841" target="_blank">📅 17:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a15289855.mp4?token=vioXAddP6QRo764-VrJkr_XiDW6nIrWeTPYq42TKPllwgtOg8xsR2NcF2FxC2ynORWvSGIakmCAF53_fZM9rBFZA-EUJupXc0NJNS1Bsz2fet_HJbYfZPtUggXjedzRlMxeRb4po2lbFz2rPUKV97yCtuetUEJWbCzy2gwbwuIgPHJx2Xf9lthamKsuEAW84sVP9zVhE1lQAngn4w50Ep5AXRggvr6CTiD1zIQMyOd18oO9_D7oebOti4ZQBhg2CPCiFI7EcuhKWWsoE3_9NxIjTDFQ6l_FC_T2BVIkyCQDNMVO0Sa-P3_6ZTtuJgOqwcrPd_GNBr1VXqp73PB2m6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a15289855.mp4?token=vioXAddP6QRo764-VrJkr_XiDW6nIrWeTPYq42TKPllwgtOg8xsR2NcF2FxC2ynORWvSGIakmCAF53_fZM9rBFZA-EUJupXc0NJNS1Bsz2fet_HJbYfZPtUggXjedzRlMxeRb4po2lbFz2rPUKV97yCtuetUEJWbCzy2gwbwuIgPHJx2Xf9lthamKsuEAW84sVP9zVhE1lQAngn4w50Ep5AXRggvr6CTiD1zIQMyOd18oO9_D7oebOti4ZQBhg2CPCiFI7EcuhKWWsoE3_9NxIjTDFQ6l_FC_T2BVIkyCQDNMVO0Sa-P3_6ZTtuJgOqwcrPd_GNBr1VXqp73PB2m6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83837" target="_blank">📅 16:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">جنگ کنسله
صداسیما اعلام کرده حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83836" target="_blank">📅 16:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83835" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=Vc3_fBvXwGhjPHQOodeqIyMG-xBap-4NXAk-JBWRa4hm56r3IDZ1R3JfmyBsq2vxrfNw7ICmZfayiplYPSXjgdlZdIXuJAAJKF2ecDaT5ixnT2ZmyuovrikFg8oDUTRNS29W9aRDH9LvXD-4eq0vmi_PawWjt5ov9loOKjShNxVUzkcyR7tKh0j0exFkAvaJ2DDnZJUfMEw2KV4PDR9PV2qmAYV6Zt8gw8XSjHCMCbW7Ig0HUHQ1ulkxpzbwad3DF8Tn9IXI7WsClqfRef7YW9ZkSHIs8n5E0HPPzvxRNuy3Eoklt4NsDV9ZqSNnjwnksxF78adX6jNvGoewUZL5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cbbae1cf6.mp4?token=Vc3_fBvXwGhjPHQOodeqIyMG-xBap-4NXAk-JBWRa4hm56r3IDZ1R3JfmyBsq2vxrfNw7ICmZfayiplYPSXjgdlZdIXuJAAJKF2ecDaT5ixnT2ZmyuovrikFg8oDUTRNS29W9aRDH9LvXD-4eq0vmi_PawWjt5ov9loOKjShNxVUzkcyR7tKh0j0exFkAvaJ2DDnZJUfMEw2KV4PDR9PV2qmAYV6Zt8gw8XSjHCMCbW7Ig0HUHQ1ulkxpzbwad3DF8Tn9IXI7WsClqfRef7YW9ZkSHIs8n5E0HPPzvxRNuy3Eoklt4NsDV9ZqSNnjwnksxF78adX6jNvGoewUZL5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب «محسن نامجو» که به تازگی برگشته ایران، شروع کرد وسط خیابون با صدای بلند آواز خوندن که یه هموطن با دو کلمه «کیر، خفه‌شو» دهنشو بست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83834" target="_blank">📅 15:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امشب یا یمن کونش پارس یا ما، همه شواهد نشون از عملیات آمریکا تو خاورمیانه میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83833" target="_blank">📅 14:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83832">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قرارگاه خاتم: آمریکا میخواد با چراغ سبز کشورهای حاشیه خلیج فارس بهمون حمله کنه، بزنید همرو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83832" target="_blank">📅 14:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83831">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83831" target="_blank">📅 14:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83830">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=hgMpQbPPFsUCodQM2M4tJJwBDRBEHDPqsW9JsObl8NDidYYjHmEwniNTxad07hrbTLSJKbYJfjS9ayC_cBMENFwzpI17EZ4llXu-sL9B3DAGeCNWoHpyPJtVqWAHyRK1FMOpr6asIQdVikPF5VozolKWrsgP2jYEubfuY8AMoOJJIb4AAEEXZ8Z_1MYM_3R0cbkv_zaSRb4lDdn7feswyF1ICMsH4fYg5qOgQTJqoGOLCV4V1LOY1K9ubIomB6fjyG4YgfZ_3ZhEFCJ1eOUvNVmkV2xJfHkRWiTrWIirwyLHUZfSLvM0UsLnKaMaSHWTqOi7AxtHdHW0eczGVctd6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3daed41be3.mp4?token=hgMpQbPPFsUCodQM2M4tJJwBDRBEHDPqsW9JsObl8NDidYYjHmEwniNTxad07hrbTLSJKbYJfjS9ayC_cBMENFwzpI17EZ4llXu-sL9B3DAGeCNWoHpyPJtVqWAHyRK1FMOpr6asIQdVikPF5VozolKWrsgP2jYEubfuY8AMoOJJIb4AAEEXZ8Z_1MYM_3R0cbkv_zaSRb4lDdn7feswyF1ICMsH4fYg5qOgQTJqoGOLCV4V1LOY1K9ubIomB6fjyG4YgfZ_3ZhEFCJ1eOUvNVmkV2xJfHkRWiTrWIirwyLHUZfSLvM0UsLnKaMaSHWTqOi7AxtHdHW0eczGVctd6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدونم دلتون برا جاستینا تنگ شده بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83830" target="_blank">📅 14:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83829">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=McLYefi97al8oyrGZ45wBpr3igYHxS68JSwtJD3aaSuRMDhzRMQZcixEfn5JEXHlB5JNbT4-6g6ez4lwVlDeQdnndqeNpwQ1h1F9rU-yhDYsQwFwIamsneV8s6PqOG6deu5O4tZSYZXYD4fJK6xPiWe8foFlIR51ppWPmJhf4YaY_bvCuXt5m2rE9R7KbYa-mUA0Kstrn-xItsX9SzKOHo_p7zJnnIp1aA_CK5-uyyaTjYD77lAmJnjf2HfZvHB6g9tWg0g9L9ghPkpbYusDVLQ8EFLzwejjKTgrgpk1NfdWnqdNHWUPnWN58bU0AnkZIp8vN0RyN102xhTb719OLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a2f841f0.mp4?token=McLYefi97al8oyrGZ45wBpr3igYHxS68JSwtJD3aaSuRMDhzRMQZcixEfn5JEXHlB5JNbT4-6g6ez4lwVlDeQdnndqeNpwQ1h1F9rU-yhDYsQwFwIamsneV8s6PqOG6deu5O4tZSYZXYD4fJK6xPiWe8foFlIR51ppWPmJhf4YaY_bvCuXt5m2rE9R7KbYa-mUA0Kstrn-xItsX9SzKOHo_p7zJnnIp1aA_CK5-uyyaTjYD77lAmJnjf2HfZvHB6g9tWg0g9L9ghPkpbYusDVLQ8EFLzwejjKTgrgpk1NfdWnqdNHWUPnWN58bU0AnkZIp8vN0RyN102xhTb719OLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیام اضطراری خیلی کوتاه ۱۷ کاراکتری (EAM) ساعاتی پیش روی شبکه HFGCS آمریکا پخش شد. آخرین بار بعد از شروع جنگ با ایران همچین چیز مشابهی شنیده شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83829" target="_blank">📅 13:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83827">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=mp-6sJxahY5iriCJfQ5PaVuyOfe8PAIQcr-3mC4gKUD21odsDdXxVZNWG9W1clh-9PIFXOXeKNsFVR9mCj3D79Ns4BoT61R-mPSyZEXKTa70W1dM1bTvi0I6Mn9GE6ATe7qjn_8hfKuduXEbhbrfIBBLk5j3OTtVz0gzhJj951RNEU_Fh-OolV2Gh35ov_T5DASayox8T4BBsq44v1lFGGDE3WUvG_qay1cIRMGNomGNYbgE8aFS0l5NLxeZiDjDvt3yoyxHGYpQNueltsW1ADZRfJjLIysCLzPXa1BYgAr0rjkBLMBb1P2aE0Wns23OGhsm-iVKSswaxgL2c1kjow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/defb7ab2c6.mp4?token=mp-6sJxahY5iriCJfQ5PaVuyOfe8PAIQcr-3mC4gKUD21odsDdXxVZNWG9W1clh-9PIFXOXeKNsFVR9mCj3D79Ns4BoT61R-mPSyZEXKTa70W1dM1bTvi0I6Mn9GE6ATe7qjn_8hfKuduXEbhbrfIBBLk5j3OTtVz0gzhJj951RNEU_Fh-OolV2Gh35ov_T5DASayox8T4BBsq44v1lFGGDE3WUvG_qay1cIRMGNomGNYbgE8aFS0l5NLxeZiDjDvt3yoyxHGYpQNueltsW1ADZRfJjLIysCLzPXa1BYgAr0rjkBLMBb1P2aE0Wns23OGhsm-iVKSswaxgL2c1kjow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طناز بعد جدایی از شاهین افسرده شده و هر روز داره با آهنگای غمگین ویدیو میگیره و گریه میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83827" target="_blank">📅 12:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83826">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=f-SQ355lG4S4J_5ZLCb7dS5wvgl_dgoNRSKz3zoYZfrFxKSZeQ-KYTKMYdcO-kCPimT9j_VfLoytnRr_VafKeuotSeUJoWta-N7y7tkEKHETrMGplGPx6jnRqcuMB6YZZfyVLOcWeiBW13A-mjturdpgy0ygqdyGctUbHROSFl9poKGfhRhhdJ8nBctLSJUk_V0w8W_kXQdqk9EaMRjxoExAGn0dGvSpyTBHjVwsSQMEmND6mN9hicMXNv4UbaI6JuthLL4OITkRiUXGcyvoEBcOrmTkK25LRHtf-piyz9ifVoTDhzCgzl0uGPdi8d07zFHY69WO3YYixPKcdRnn8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/334f5e7f1b.mp4?token=f-SQ355lG4S4J_5ZLCb7dS5wvgl_dgoNRSKz3zoYZfrFxKSZeQ-KYTKMYdcO-kCPimT9j_VfLoytnRr_VafKeuotSeUJoWta-N7y7tkEKHETrMGplGPx6jnRqcuMB6YZZfyVLOcWeiBW13A-mjturdpgy0ygqdyGctUbHROSFl9poKGfhRhhdJ8nBctLSJUk_V0w8W_kXQdqk9EaMRjxoExAGn0dGvSpyTBHjVwsSQMEmND6mN9hicMXNv4UbaI6JuthLL4OITkRiUXGcyvoEBcOrmTkK25LRHtf-piyz9ifVoTDhzCgzl0uGPdi8d07zFHY69WO3YYixPKcdRnn8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83826" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83825">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWUYFK7qzMWfsqfDP07A2NBJDpX4TkVwVZXIswB950XfqJXwlvyhExOt7zwaefIwwS8o5x7acvmLathQDYGhgsCxuehi-82S0M3gdFLkwhGfeNiQJuO4mFHvEIHKVkH56i-629bKDMP7oDr97iIiebnpDIt561h_HlQGmRoVTL6Z1oMO-HmDKZMuE6keq7qwdSmSEP3Fh1CX--pJRjtdnyNitlgXq6d3-07yjzLwPxH0EGTjh3XSxqsKsDwfyN7XtW6FPQvDqgRF3pHgUeZK_uRujJhlElkNUQ7HBlgbsljrcElZhdD2g2Uj7ona_L_Ml1uG8cKDMAgz0yDI9AVOUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
بورنموث - لیورپول
⏰
ساعت ۱۶:۳۰
🌎
📲
آث میلان - لچه
😀
ساعت ۲۲:۱۵
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R29
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://whejkfjiwe.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83825" target="_blank">📅 12:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83824">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/83824" target="_blank">📅 11:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83823">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام فریب خوبی داداش چخبر کیش صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/83823" target="_blank">📅 11:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83822">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ایرانی هرجا که هستی یک قدم از Ai فاصله بگیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/83822" target="_blank">📅 11:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83821">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صرافی او ام پی فینکس بالای ۳ ماهه پول مردمو به بهانه های مختلف بلوکه کرده و نمیده، همه مدیراش هم داخل ایرانن، حتما باید فرار کنن که براشون پرونده سازی و پیگیری بشه؟ حالا اگه فعالیت سیاسی داشتن زیر یه هفته بازداشت میشدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/83821" target="_blank">📅 10:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83820">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxf9hWCa5z0--hvo4osHyw-QK6HciZkK-jgOpR1Ljy06RFZH7gApA6L9FXGyF1jzTJsmm61J-sLNb0Px0TYgoTxrLenctRyz_aa9WdLblydhR2U5AesrMW4oC_wl4glNELygRjaadxF1bso7l-QGk2F2pDD8SxXMvgLAHEWanf7g1uH6f4K7ExuB_ZIrVIQYTKIAY-6Y6JTfa47MiXjMp_OzVmlr7uvCMd4xs41KYiJkpfF_mqeyD94abza5JsMAWuDpPbqTnSpmuu3is7IX2ukGsoxJ0c_28YtfGET6r1_bH0-WE-HXj9RlPX1ptpwMdbnWUld9p6vTrTHxIm9jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلوت کنید این‌بار واقعا تعویقه
تمام برنامه‌های عمومی‌ای که ترامپ برای امروز داشت (از جمله سخنرانی‌هاش) به صورت ناگهانی و یکجا لغو شدند.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/funhiphop/83820" target="_blank">📅 05:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83818">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlRO0Iloq0GpYklRc3LgaXXByK8wi2Z31neJQLQWhgzTHJqHoiRLmDr9ndom3-vviSvNuqUK94b3AhEDdxE2WJBOIQ3UL3RGZ2Au7wxnWc6aXZfD9E1GUsgh3st33sE2YFX4-luRzMVO61iMxaHBvgLL2TpgUMwPcGBdeMdPZdKpFfW6suEna7BOflWbzbmAGNpdRq_l8uYRTO-K8rIcyoeNvHkWiwrX_5tfQuf_usWbObsLVrGLIYfgiQXiqSDPx16yqR1bUC64CGMcsGhUczM9s1VfbTKvniZpXtenvZLGyaATFdyR4puup9UHccLKAgCxKMBFnwAHAlOnlWb4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/83818" target="_blank">📅 02:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83817">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پیتزا فروشای اطراف پنتاگون سکته لاپایی زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/83817" target="_blank">📅 02:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83812">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حاجی میگن ترامپ یهویی برگشت کاخ سفید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/83812" target="_blank">📅 02:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83811">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/funhiphop/83811" target="_blank">📅 01:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83810">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی. تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل،…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83810" target="_blank">📅 01:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83809">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ایشالا که هسته‌ای نباشه حداقل
🙏
از یک ساعت پیش، سفارت آمریکا تو کشور‌های مختلف خاورمیانه شروع کرده به هشدار فوری دادن به شهروندان آمریکایی برا احتیاط و آماده بودن برا اتفاقات غیرمنتظره و بسته شدن حریم هوایی.
تا الان این هشدارها توسط سفارت‌های آمریکا در اسرائیل، فلسطین، اردن، قطر، عمان، کویت، عراق، عربستان و سفارت مجازی آمریکا در ایران به صورت جداگانه و فوری صادر شدن.
یه هشدار کلی هم وزارت خارجه آمریکا برا کل شهروندان خاورمیانه صادر کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/83809" target="_blank">📅 01:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83808">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKOQnOTcGGWLUB3TJMjbUMdz3TtkNcFuLb0FOim1ntG7yzkG5l70rb-hw5tQ4rqp9jSFVF-eaV_iUOEk26J8eC4PqsDaAWZus4M1wNrhPz-bJOuiwBQqIOsEzSA79hfMdrbj-RdbcBXLo0bklt142I3oesUuHASZh6wvSjXTtcjtri8q5tfHu9-pp8ineCR5EWAUKHknWM5s39sFvWZWy1norAJdKMrUqbtpkL7WS0xYZDbVf_8hN7bKj1oB3dYqQZ2NLkuFlt8OJJfiFQXJXgjkSM26vzH0puXChyBpdI7koORv801csKN-h5gdtZeDPeQxoP4HMfaczxScfFz35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر نمیدونید باید بگم سازنده جنگنده A-10، یعنی شرکت فیرچایلد ریپابلیک(FairchilDRepublic) یه زمان لوازم خونگی هم میساخته مثل ماشین ظرفشویی.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83808" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83805">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🎓
آکادمی فتحی  انتخاب رشته تخصصی کنکور ۱۴۰۵  با ۱۶ سال سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما  مشاوره در ۳ جلسه: ① بررسی رتبه و شناخت علایق ② بررسی رشته‌ها و شرایط قبولی ③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/83805" target="_blank">📅 00:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83804">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilV1ooxMfqhKIHkfHCyFGBo6qRwn5sQG-0QrC08oamrn7nlADW__GqKbVcsnvzFK88A_ZFvTrKp7aK7x_TmSBfaEUrVZsMIorPWpkaFYIaZEzYtru7F6aTCTNh-uo_4N7aGXfRa4C6yKTiW9ShaSlv26Jk1zPul_StI8lYv3RMxgdJuy4Ke859gTfB8f1z8Cs3VIxJbkDFMyrRJwEGe6BxH40kZ49zzMxgS5epMEAUqdk0cgzkTrHI1hkrqr-Mu6q_hOSn4iYPXu_Z6JxStIP-zcLQxervKYO8tNGRnxerS-1-_yQhJnFj7VyVuApxe8M4WovgvSwW5c-Q67fkMm_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
آکادمی فتحی
انتخاب رشته تخصصی کنکور ۱۴۰۵
با
۱۶ سال
سابقه تخصصی در انتخاب رشته
✨
انتخاب رشته متناسب با رتبه، علایق و شرایط شما
مشاوره در ۳ جلسه:
① بررسی رتبه و شناخت علایق
② بررسی رشته‌ها و شرایط قبولی
③ نهایی‌سازی و اولویت‌بندی انتخاب‌ها
🔹
مشاوره حضوری و آنلاین
«انتخاب رشته آگاهانه، شروع یک مسیر تازه»
https://t.me/+XFqj-oe9FrdmYzBk</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/83804" target="_blank">📅 00:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83802">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، یعنی چی کلا ۳ گل با یه نیمه اول سخت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83802" target="_blank">📅 00:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83800">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/83800" target="_blank">📅 00:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83797">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه زن دومم داشته انگار پوتک که اسمش دُرسا عه و فرار کرده</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/83797" target="_blank">📅 00:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83796">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/83796" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83795">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آرتا ویس یکی به نام نوید رو تو دیس پخش کرد که کون پوتک گذاشته و داره تعریف میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/83795" target="_blank">📅 00:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83794">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جواب آرتا به دول سه سانتی گفتن پوتک: لابد آمار غلط داده دخترت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/83794" target="_blank">📅 00:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83793">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دیس ترک جدید آرتا به پوتک به نام زن جنده منتشر شد  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/83793" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83792">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کیر تو آرتا داداشم رافینیا چه هتریکی کرد</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/83792" target="_blank">📅 00:04 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
