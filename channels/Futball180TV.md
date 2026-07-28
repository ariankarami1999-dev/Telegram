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
<img src="https://cdn5.telesco.pe/file/E8_LYLo-hCQryOrexXvw3KDvoPxcmP3YV9muPtyQ3U0fJywo3m848TXcePVBZUoZa3GSQeF9NbqOxV79NawiaoFphVQ26FdmVky-SrhnMi5-29KgDtf_rv3Okqk5qclU0sk67pc-5QQl-9mEVEHgweL91BFcqx-vDsEdHCTISe7LbYRfhUDjv0aUuCoFzdRDo3U0vxz6UIfqFfEXdhsbaiEvum07yVhpza0HARGh_JA3iCxutFjMw8_umTT3DvizO69MuHvyCKRg4UL9BO3MuhU3Gq7QUlJ-aCOxhPaRCHSutPoqyQfeGQFNn-qXwB9T222Yz71ohE8DtvGCsMunrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 518K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 21:37:21</div>
<hr>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz3UNkk3rz3N7CX950Q8bMXqxAR4pG_gzCFE-VxvD6_hSCE0YH5wT8YAReyMxRL07E8Ww87JX5mwfLFxak5ZIM-XgEwNCaRBx5oS9GkHcEghX_lchZdwYHLi3UPOYsIjwslHrGuLxlhdJrWJHVWt5DB8Rh5EwoPiTy_y4xTD4O26SfBApuRhbaFWYHYRvfauMkEYTfgftb3XqzQwCXXAprfdR2qTlE6_z1e_h-KVxQMHv1MGw46rViFcPlor_Te1JyysFcfA-dzxuCiXCtCtmmbk3DUS_oKlRM44cBDC0Ei_9nEDgTIEw0KbEWwJ0fWt0aOLi-Y1RM-QsvZwwq5ZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 615 · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpUkYef_MGxgaW0vmYUzYAe12hmhvL7Eq_8fyUGZOPTxsjTOMSU02bBk0EBrD0YF8fD0Y_YILrlKbFQY9XbULVYMF3jqRgbysgFHuEj-vSYNBHZ_CCli2Jh0lAO7OD-VpeDeCcqv0r_wSdqFdrFpn7merKtRfcNnWfcOTe9-8_R7S7HpVy9j0I_bb5bvTXcvCnW2kreKH4DhXME1Sejka2qdW__OWEeB_dc5pQZvap06M15OMDRcVohaVmV8BAYHEmGKzRYojB_z4JwyLRJ_2yKO2Zc5wclle633OoEYC0g9HUQGHcr-fUSLS2jc1kgYb96jSkO1pUiWxg02izk1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV6Z9umMzgfyuqDN4cBvHkMNNRt01EegHzbI_uQVioQTjPzA9IJA9AXmmPobZtWKHV2_ml3sdCgmJeMVnEU_inAD6xyPAPUgaybQnV3E6dBtd_VfyniPYN7PtD5Z73A7t0KcDNjcRg71MGIXK91JSVTfOh2hkxwTmQ6iYr8zDDu6-BAwysgibHiUtYMg8G4zcg2gY42-_2dy2s9Xn1bcFvlmrND8BtSs2DeZmi8pX8uBeMvLVqkxBAfgcHPSep3Bar3SSfZJ4_rTvt5EyX8QSG9TbZ38KuMUmRqEct1Q0aXo_psFN8iKV9xb0ztCwUBhIb97DuXDzYv4aFnE381GAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aItq0w75KW08n0o3wFN25_1ka7ok2gxEEjYJOODNZQimCaiClK0upD4vTqiPYiuwB1aFI65qVvnD_LUyizwY71GRIQpu-iTWqFqrk8Jcrf_d0vEWGjDHDWsOIMPAdKLPdMl3dw1ZjtnKLY4yQ4OK0_MbATZvtkzeaYyiFNsD9hbSW5GIC2giqRpcBsPAuTHsvudlbGWGIB2trKH70qXjQELwRQNYVaBFmM6BIAF8Qpxu74_-UO0_XshIhNvX1KiK7Bzw7GbyE0vnh5mwg19s6vnIuLCgUKbzYrU1vNTnvO3qXGykW6t_S3QdRmrpm0ZSWfMhiLF0IgQlWzZKTwfIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=PD3ZQEMpVenL4UsDHdxIC98sbahZCiAMHoDzavtkluxpNej9NLs7q0DlTpq7TPAgW1vBufwjdYnZ5cEW-oqv5nXdiMU0UeglmoYuyvc0-nvmu2uF6hZd7359p17ejRwkUzQQ9T4Cs1nPfxcxJGR79qAGKCJENEPzdyYs19zs4ZncTizOc56BQ7S3J_G2_2AQqVVMimMXqFkbZ1avsghQMK3OAHaKksVGGbzAY0OpYYINfP1tmS540x5IJ9DCEwXxI7kP_b4zMZxPawJTfGUVKE3j2jfBbQ8--aDgpL1RRBO38Jp95KcXQmbT7ohNk1BBN_kL8AVVJz_tlCIii85tOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=PD3ZQEMpVenL4UsDHdxIC98sbahZCiAMHoDzavtkluxpNej9NLs7q0DlTpq7TPAgW1vBufwjdYnZ5cEW-oqv5nXdiMU0UeglmoYuyvc0-nvmu2uF6hZd7359p17ejRwkUzQQ9T4Cs1nPfxcxJGR79qAGKCJENEPzdyYs19zs4ZncTizOc56BQ7S3J_G2_2AQqVVMimMXqFkbZ1avsghQMK3OAHaKksVGGbzAY0OpYYINfP1tmS540x5IJ9DCEwXxI7kP_b4zMZxPawJTfGUVKE3j2jfBbQ8--aDgpL1RRBO38Jp95KcXQmbT7ohNk1BBN_kL8AVVJz_tlCIii85tOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcRobxhuJr7Icc_Z5uXZM1Oi2JZZppFGG3PhP3Au0VmKGNUYA9fhalR_p27pg6RU7GlF3s4yB9Ix_1fV1zjW3QjuounzVCd0cOZS-emrwlPkIyzaMRAu7dn9NuRU6bhYON2rQ-SlCflDzAo6oddNJTEfOTsV-Vlq_udVbCH_F6vQ_MT1JWzVHw4b3zVXsvEFAFw6xY4cgCstutUNVGObE7hY_merN195ovqqrJ2QWWfL4a7DuxrfqVuucP8vhdx1j8W_T49Ad1jip7VWRxVkiUvo6TzxknWitEMlDJJrivqceTHk84t_Az2LVoK6Hbgyz_dKhn9xHTzASrvmFqOshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rrKcRZvlMATc9gx3uXanPggC8oPdY46-1Qr0KfNpvmEgGrLgKtAe6IPuSV9BoS3ezqkUk4S0ffpXX6WDhljwl9UTz4-GGLaz4h_VoRoPynEZn1R4u1GhSs_wqFZcO59LCGr2_w-hvD6UyoS0f193ZqzK_jrUQtQjYidgYwxjeNTwtFSxDHCsb-BweQ5r4GNOkWdkAAd-QJ6Nfny8oZ5JkoAXOg2LZYvOLgRHIIUdvOew-iOzT6wFEzCZYGk6FO576NGRm9u_RBRsk9f7m_vHKBlw2morLNUDgKW-GfRMjuyVhuG6NDKxy1Irj5q4yDqH5Y_kh3hQ0Esp6VXqq1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsk-WUsHWM7uLk0Naao3XQ5hUPDUmdwlEAjwc-zsgCZlaa5j1ieXRa4L0EbQwpU3txcbK7zBIE53-BrJIOr4WYDmAynkA1VYGKkLpKrpxHVCq_8nasLziWmjB1q2Irzuce_Q32Sh7Wivo39KwZI-TZibt9LEEdwyiHjZMnxaOrdkHTI2ioA5Jr6LygN12jXzftZ3igpk74h1kVTiHLgfKUl_-N_FTDBgEpxd0Un1v3KVgrL-h5Fzl9xEJDqt4k2VXL9S825OBWMrdWRI98-1ztxQmI4BqgbxGUaQOAtKcf8xaEsvtIx2yB5iKng5A2VqQQ2WDwKjUnS990TJFSGZxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of6oXoNr81IHWMPOOk7-70LS-eI4LNQX2Q9muAsMbxFQ_aChvp9_WKgJDM4zzhzyhD2ZH_bGI8iVI50SQ1OFnBOwoVD285kP1q4-PDqd1wCEX0JS_xtqXB-dTEBaC2ax7f2ypSWb6O0y3lAz83ghRbNbvlrp7UdO45-UoasISwg4ZbNochJ3IouSIZFxihGNGH5LlKOc81BuA4t5HfmX-bBH-AsP2HSDFbqfDPnsjKaBAtqYq0EXqs0V_O0O0ynxmuDekJ0xyxZsqKJV0Sd-HtU7flkFC7wxPoh-GYLZXG_f4kI4001FBvP_Y5r6vKOJsF9HWJf_swh2o8SqJKENhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMGBECrsWuYesRGX3JKZh_Ky2M60XGhCl9KBP4U3Lmdml-UHKxe4azKG704Afwr0bHMQ8gQUOHvkoIbIkZqLnhEGWOrBC_5DfNMSot0KH87oSo2b2ZQ9bzRRf6fZuA9YF8C_SgQJqYdtW1fr5H2aWp42jNrYbgrIpBLCwgDbuncYrIjiu58WMwGYOBrRJ4Gm-n-TuLcKvIR7aL_28h5Y5P0wU4SJISmFwRZdbdSUgCucaL9VE5uPRVFCiIk6ux6D0bb4KyH9rNY3ppqQDMF0tjce5IWh006WyfjRUgT63t-ThdEMl87sI0LIRzsiBtS_qj-ZCFzpgJFgsMTNa7zUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl4Xejz0tKUkZ1XxAHcL_so9UL94fECmrr-irsJBzmLU_tFFJTgDEsXhDyxyScs86QqWhkZNvQ9dmLjyNc2QkgZtMLkkq3ujsxVKD0O_B0aaqQAp2YsWXGdTsb2AgUGFWRBv1kIsTQnjgVOW-0t-a3QrsnLWZxnSNhpnSY7LQbzgcmiry1qAAAN9YSVO9GyQzoqAH07n_FpXWDJXy8v0VQgyUzOVE1WmtD2Of5TnSzHgP7gne4NFqiJFViEeSCqXcAXGXDgiqgQbNEmC2MPlQSBB60rZ-jBQet3DJxLhYw4XLNhDkXHWqoSP3U6Tnu8J3nUb-oPPcTQ1549dYkEmPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QitpTL6fOT5Hf_RaRhedpE8Mpu66Z6xFBS834CXbwW7YrZwzJu5Kijt_kiZ3Ndp3RJqHiJyzFSHmyjYXGx6M-dOySpyfxxBQB_U470YUgrjK5Bnc_auptC9RoFov25Ok_TiUFbxkvSRVPHSw7i-ZugtDCsFl1H7vjK3xbqncpq3TDn1TQ9AagW78hEFOaTsCmdqRGtqEfdZvTXZKorGIjyVAsPvwayoZguULvOKFqc0yAFHdQml6w9KuR9ys4NYcEXswGWWp3WJbw6g4mhlwIkJ1WAPYjvgBjMMAUm3e3DpZJiS_1gBlXE-yOFYiprIZhDD-HNLorWD2xmI7vJJ46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoj9O8u2w1hi1S9tQztRtwls3r-Stm04PBqjsKwg6HP07zJcRC2L_IAgRHRIwFBg3KvMfXRym0-MSzUhG2P7SdOFpvDE5s4TnMgONX1PjFHopNEPn3E4DW3sO8HKnIuY_GBSMoPE7u3OGxT0dm80xTAQOj5ynkQKN6BbvCTyg4lzmbqmxEULmEEIg0iOc5AWCjIfQQvmgPhJKX4-BSddT2sKvJgHT3QfVkXNcIAZE4wHzrS3NpDjW-WtaGWC_IhPDNVAIWUE16GsHtZqRb0x3yoAccrixXQzeYqUbp2QkxuxJGcU_ITenpMlD2_EyHQFtvEKSM7T2ThKWUKhZ1I0Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjb6-pnzDmprmuJk3LPiBPFtcL2cPuZU9SV5FkcUCfUfkMdOZ4zwgO5mL4fCkg67G3evqQdiCaCS9c7MEGzSOoHq5M8k5g2R8jCgMX-XHOG5ELhbkM2oj-wfBwntKToZIGkMPkaMeLFS9DwybAowiSBOu02CW86Fi8UvDQPK1fZcawtQOr7YwAjWSkuZFzIzeC9hx1hqXapSJeVJUY6tcw0Xop_h84JpWn6Oh4OQjbgdYC9ZW_85trPMt95sRb8-afWRYnxHAtYSBGZnpGu2lsbavCxB6PqWflzlWk1bLhu8MkwkrPKFtT20yTrQfm_Aln3gdQT-9WJ6Bwt7OMqhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoBhxsxdKHAONZ3jtq_svla7rdRx1cSitgfTM4bXNxgaAX4LRw8A4VKYqAvIbH-HDcMrYUUmP_Qqh8LN5ZwPqO286BlyNgHOqj95M09AOG7lhP9JOnsvB5GPa62vN_fltwWJ-pFM1gnRxaggija6Ob0G-Ph9dIe5_ukw9fp-MaCTNyTAPczOy-rbCMW0qs-9gapCc7nWCeztL5spSudHxYm_8M4mTnKxSA0IC9m0LzNZ1HuEcVpYyfWdMjYoweNHm9ZjCPYeqbDzIY5HFaGyCDyx7twAeO592RKxwDFtFhL4IM6taQJ5fS4Ve4BSuuX5-tFVezVJ79StsF1hriFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVNKw5JVl66Szvb2AkjuukNI7zu_4_qDBxj6SEPkFRl-ecUQKSqIA09x7kh0t_5m0CUbTqWT8moSgjREbKKlGRdr3uqZwATffMISpJXunUjaNSGC1aQTjZuHgb_qZlP3kL5Isfn7bMytT0AaR8g4JWIlvalyrtq1znXVgeNnjVcYm8phHU2y75gdrsk7wHsqwp2U_gb5jfh4L6qjOX93Qsb6FpfvqL-UMLoVtES4e9JIKx2hfNV6z-AsbMXVZ3B97jamQBDGicJgXGnsWnMjTe0E2r4P0b--QGXd143fD0dJzO-gC-oAer_x_O8NapB6NbhefS_lF0yv2S69ZgVYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq0iXaaicdVpXAmuSld-PH3gH3h0pTysAdTFHR49jFwKC12aMFqcTRiw4QRx-CZqfvaA4e_1yVK9YJTnTbwujJyWWmMTxDS163rPcbFUvMWksQ2NQiWnjPlWQ1rD6ew2G3wpGuOdyHeBLdeDgAwdIJFeN8sMnRVGWrdzvybHN8MQaCdSJLhZ2cQMumeavPjg-97LI3nEtp7u04LsFZSD_U8Tb240-6ERuLUX3eWjr1AJ0WybnPHJ5gvVOxb9yh1ExdJeNN4YHMQZmIwd0twoRqlw1PhLIdrVyqhCcUMiF-R0gDQxVj0qTfnnrAe3Pyg2aLveumUsfOa4ki8I1Otjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD5ka-4F9pbmf4NfyxziuDhsldzHyeHdzv4vuzChAInisz0dTBMIwJ5ehhtSk8uIxVj48f8XhjlCO8GGTIONfADkmbWeYq2Jbc4goxc7uHdAQ3SnJozbPQTb3pX6UkqQGNacKYDPzhRYO2rKHvZKEzTz0nAE9uy7V3y0M-2Udd1nmUJ99aaPd8IUZzX27GoiSGE-pafIZcaE14CctrFJ1bVtq1vC1-8mXx9gnsA_Ih9Q9DF9ih6DZFa6TqAKP7z-621HHEfYhj2cR5aN7EGMNZyopzsrFomoOGmKalw7g95r6O5Ydn0jrcsjOoTTEE-iolNRfsyiaS3t_k4EI-ZpGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WagISHqPqPD3xBhl3TjGbm53-h9acJ32rLFhXFHNSa328c3whBqZ2GnSaq7Rnzcne7Sa8vkl9ZgCeuokY7OWXxZj5Z1EwtU-ldNhQCxrJ_v_XvCfetbVntQfSyG4i6Xzo4b5Ut5N0PeXPU3FcMwmGuIABHSpAavpU0O6phUfk5g1Ro4iOIuSsWE-Wx80GZF94U3cR1U2tf4tIeZ30ktJMuuzDsnR1HkknEfcd3oydi7pKTEeHyWLbVaRLEy4onMa_pgpvCy4M1fV-MSw7hXjqxtQrDZ0-EHGlXW0uQVPJgFKPCovxsO3OaQegsAvamVOpBHza8FLG1SF_aVFLRIv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUWs9Nk5owdIrCrRQuWmnSqt0efzUkXknR19OwbCAAx3eDXWoaQGEnILkloYi0bvYjzhTE2lFPwJTcK-Avwy63vuuqv0O86wzomgsgGJp-MLmboV8H2dq67cIfWCne4_i0dYclgr0gqjJc20rV7SOEj5h-PZ_--mzUIDLr5f6d0utUarSw5bkC2UN_n1VMevNGadKwp5k2ghjqMBZoxDfzEOOofwuSMoLZ7s6OcIknlviENMTw9OuLLeDQmH0FkDBS7ON27kmdAUImz74icU_KzVwOZLvlqmgVUFcvGkl5qsp_5nUoQSo01tVMLYHJWsXUxrwXzBsWtuXZwzhtxgxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHsLAxrHn5An38Oe4DaOZVDrDjmBhPa_2_9wTtQwi4dvSHxQYjiRaZyJB0WRFb8aDTOZ82ayLKxd0lsqU3-E5izDYXo6gXhEQgHc1PVGjOz5lp6EWWqTMFbNZbA2dhkcP6_fgvMLX_f_jNGH8RGphL8MlJf7H487Biwotyjc0qr0ouZ5ZJ83dze2tDyD6pIK9vxkpti7HTit7DC3njIxmYAZmcQa5emHuzZ4MUq5r4x4URKbIy0Lg0-Ju_SOMWhQ8w4aBUrSQjSGGgTSSjpjVxBLkQydGCdCK2FzXk0v_NxfxaidGC9vPHi9k5mahPxLR_HYnVM-PuwaVCs9bkOMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpC2eyjADYddrM7ryjTL_td8U-X2R3McUhiQXIBqwcdjaz1H_P7mvQCnaBKG3n8vzixOOl2jqKrPMnOhtqcrLoGyS0mVn8-BIMBqAYYVHUDQLVkYsiBqgEQeVKUXXN09lU6tmCC3SpfvtqtvLki56qrXXJAgTjsjMr1iamLOtbbULVp2vQvxcyDMw9SXge5Hj2sl1rQeRUv8zm5i5iXrjRR65dg_7EKOLZpr48HqjJZmE3h57vrfTuBdolb1jCbaXQEje8D_dbgfPN7AivMJrgikNtp6dXfn7CTQPosJSXqNnlH9UpQ2nu7jSjC6KmmRolHI2K7VPwaHEhLZ7irdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=b-OGPmdXa6EiC0afWLDWDW9Og1dCmfXH_drXImH728wTuDmI3QjMpT_JidIX9lOqMVz4-WAdq06Sc3gKqHrqJ1CEwbOsN0ZmQXUIxiRkOdTtv-KmxO_6K_Ydtm5v5OlgWvRVXdKhvkeOa6NR6zhOhqv4jKqyszu8xykKx5bucy99NUf96-lrOzo2nFlRBFzK3mN8NzYoww6M43LWAU3yPOK6GttiHOeNw6UcBPat7Z-mtax7DSHQPfwH_Ejjee8bKQrpiNfp1ddJUIkW0S8ILJSi0KcgCG-9G-TDGBpm3rV7qbGo8c731lkmZoBgLfZkO4TGFP-HF_ifHl5cCKko_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=b-OGPmdXa6EiC0afWLDWDW9Og1dCmfXH_drXImH728wTuDmI3QjMpT_JidIX9lOqMVz4-WAdq06Sc3gKqHrqJ1CEwbOsN0ZmQXUIxiRkOdTtv-KmxO_6K_Ydtm5v5OlgWvRVXdKhvkeOa6NR6zhOhqv4jKqyszu8xykKx5bucy99NUf96-lrOzo2nFlRBFzK3mN8NzYoww6M43LWAU3yPOK6GttiHOeNw6UcBPat7Z-mtax7DSHQPfwH_Ejjee8bKQrpiNfp1ddJUIkW0S8ILJSi0KcgCG-9G-TDGBpm3rV7qbGo8c731lkmZoBgLfZkO4TGFP-HF_ifHl5cCKko_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1fS1xCR_YJ9UFU7wPfs1xnOMVecnspqQlyzr3cs6mt_d1NZvyJ2XUFsAphBGjBTaiuChRIHpUEsZJEwaAz5yUZUuT_NdVke_ca0DgWJKOs5fBdwVdVao3sepivrPDkYTIhrUQtrU_42AtLrf8jPGczX1xKqK1LbzWcpNM3CYJfX0i_7I9key2KK4i7w11AWX4wr7ipjOkUsw0OGkg6fDpwn596M_upXTGyVWK3fbSqmNSmBt5_IMgdzUluL49IS2kZtL9WKME1rwDaPGE6xRb_KvXL5UrRsNHSCpuUCWAPDLripHnr1bif_1UOu-Jv6TegW8_dz8HlyROXe-Uq-2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU2-1a-R8cqcPEhwV61oF2qGUABxFyydT2q4v6fZdDaGNhCfeLutYUBObv3p10R6iWSsxG0c1WjQ5qv-jPAzaAGaZS2W0Inn7e0aXKNyDGShp8MKPg3BSP6CC4WA75Ht2TfCW5k6HIURdnfciPeP4SgaWNdoy8VD3HCRdc-BEE0qXUoY-A3wY8-sBuH2730DL4faO28fr_wt3Jcf4VJK8TvJiWgSbIRTEd3h8pjNs3FMAMSnnJJbNI8Sm9nEN6tJoLKGYBxj3snCbcyCTtvQ9xfF0zDL6nPcHUYzwg4tnI4GHqS_spuJCJ1ZS5ES428aoKtQqU-S8Y600pj-NDvrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGsPgyqHnLFWazj9zv052A9MJ9Xb-Ir2TzNv70gZh35XDmk6dijyt79cvNrQJ6z9TlsU1-PhWH3VWtnBXBzaHkMm6y71c6bCz7_bXH-v5AM1Dwd5mlFDXtKkLHVnnLjgHaYWTUeKRSQUe_ADeBPn2FbJuVXbiqCBy4R5f_InXJnhrKs2hDtt7FL59DsnvChn2ttBrCJdwOTgk1foKOU7fZ7BrKHIBwXx8T_cVl1dgb17F1DOJNOjhBuTpW58XJPZDTkbP0YpsjOkYRUawBdYnHc-Mjuo7ygizztRE3_fPOeDNtuNvCpr0Xq6QIAbrppWt-kpJ1Z760Lf9EE-AuavHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmqxlNjXBV4Tr6MK3eHO70EUSAi8HxmRXmnLTwzZhDk9hGA-ZG6CwB-MLYKnjTbfAFHHRAySeFgb7XoUZTt7znGz8WfIwkCw8wNRbHEhH9cdRB1WrfXA9aDLsvDr0PNAKfBR4nfQNlE4I8Wbk61_7ZiUhHwlP7XBQRX1D8MP3W7RHIs-ZDp7MF8VzUcEx1bcwv9gyYpAz9ETzohLBVcYSvR3d6_bwnC7DEmqnnj0_3TBXVAkbAII3F6ftkTEQagtD_2NDAa_Ifi_qd8pS3sWSfPeDLjSxTUQ6PAoOqjXgRS0v0Igg-Yw3Hi3Zv4bKTnFo18Ulwl6YEyHrOZMFZozfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Goecwu0hlDcrj-YqMm7foMrBjZvT4AOXFryFHRWEjY2eA_8OGIl3pjn0faKK_oxfaGG384ZNbYTtGEYv-yUj9SXKnk8cYPj1BZ-AKKwWw8fnwOR1AykfR9tRai6BoDVL25gdyJUDpQjm7h6oZlJgu1oYNEpwEzA2rzs4L_MbOAFvMXSW3eOy_8RrQPXb_PJD33Ntg0ZzmVSISxsLOiW-YiE9wNk-9XZkv0mfg-Hk--PFCY4lqrV2UsQGTCiCT4-MsPZ5lcNaadygLlrSaf8JBmiOCb_vDHrs8K2jLbDnX8g051J12VKciU-DOPop1Z-vevZSyfxm-GhHOO5p29iJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=Faj8QW0Iv48e1bdEzLfMr9HTjPbVz_IgXTR0k3KdfP3HNvipB5HpXhhehJwgy0Gg_iqQ45_KDnkdmnB_AlKYeftJBUKFG7s34DejVVT8UM1tMzvIKhk8ZK8wldFKaT2sD4b2__1EoWx8ryUk7F2ziTvjlbTGyBmUhGnB9hwOSAT0uwwAJm2XpGZyrTy8NJlyJ4BZpaaEsPbU-DXmFYth2NvmfASgdEccJGEJghl8EYtErYsgUhe62IC-2_4knG0JO-7Q-3I8QlCRhbWfnsOpVLt3MxVT0e7aPmo0iQAXyJuJy7FpElGEyDsorgbGm67Gjf4WzVx0QWdrmCTc4PXYTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=Faj8QW0Iv48e1bdEzLfMr9HTjPbVz_IgXTR0k3KdfP3HNvipB5HpXhhehJwgy0Gg_iqQ45_KDnkdmnB_AlKYeftJBUKFG7s34DejVVT8UM1tMzvIKhk8ZK8wldFKaT2sD4b2__1EoWx8ryUk7F2ziTvjlbTGyBmUhGnB9hwOSAT0uwwAJm2XpGZyrTy8NJlyJ4BZpaaEsPbU-DXmFYth2NvmfASgdEccJGEJghl8EYtErYsgUhe62IC-2_4knG0JO-7Q-3I8QlCRhbWfnsOpVLt3MxVT0e7aPmo0iQAXyJuJy7FpElGEyDsorgbGm67Gjf4WzVx0QWdrmCTc4PXYTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1wE1Maz7UBIekJvvVx58wRomRCCRBWrc6cMXNhT--dzCQhhKbXC-9J9YI5UfceFmImX7hRYRw0d1JQHCV8OTejZtRd2YAsVlbG2IGvEqunNvgA0GPwXE_IxavBWCEczekhnBLaACpmlj4Iy72QcY6bQd8Ojh8av0zlVTXhUfADdcJgzl87jrdAiBMJV9kfxtlF4QK0LmqwL8eZZfZNcI-z3s3n6yZwufWMmN3N_qci5jgc-w3bAJrcdcXEcOX4vJxWnn-j6ln5BVFh3GtMlKNuyMzIH44-Ki6i6Mq0x8uddpmOEFfHhLHWT11yPacQCUtRNF3VE6V9dLjmsb34SfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MG7W8NyBbJd_Swzn0v0jq4uOLV1lxF_39FoyonvWUjvbnlSV_CsisTm4cWlY_y2AMzLbWYCKgM4Ihj-P-i4XYdEMTDNIWmLFb4yU53If7_xmzges9Yej9WnFZoj9mNRjEk3pFLbqUIDkiaYxQ8cSHCt2_aW1E8VRGhk6ykqUwicw5giRFTyCYC-4bXkOOyYTWm7jp0Pq7O4at-q31vdpzX0uM96Bxoo_Ci80uNAc0e3QvGPwlYsvGbL8eCznB-hy83XQ0KwV4WNNO-uJ_ZwPmXgjCNDPqap2K2BVLO5RoTVaCTvPg2o04_1m5NSzgirTGjV3wtP3ohyE1y8HnG5jPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=koeX8bq5hEdLDglk9zvnOVbNy5X3gj7Ma51W6BTzsod0RQJMJ3Z3lL4jCYzim4NNw7ehd0UqUTv-cgTwFxwMgejbFoViyNUHinGYmOdy_RTsvl4ScfsmiQoNcpBlYcWBhqicsWmvZX71SXIRyBJpyehHyZDy_SMhtOKs8RVAA3Y6-L5V-W_l1HxuoDhMJo76ud6Umy1rcm6KDtSXzyv9agc3oBrkhVTgLrBsGoKP6HhluUA83dJZ1-f1DU9kFrjPg_VxM05p9oaArnVsTln182G_1LR7HVi4xeeByagdgBX_VM02071q9InmTPKcnZVsMPn_H5s7PCqkLjCcYh_SMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=koeX8bq5hEdLDglk9zvnOVbNy5X3gj7Ma51W6BTzsod0RQJMJ3Z3lL4jCYzim4NNw7ehd0UqUTv-cgTwFxwMgejbFoViyNUHinGYmOdy_RTsvl4ScfsmiQoNcpBlYcWBhqicsWmvZX71SXIRyBJpyehHyZDy_SMhtOKs8RVAA3Y6-L5V-W_l1HxuoDhMJo76ud6Umy1rcm6KDtSXzyv9agc3oBrkhVTgLrBsGoKP6HhluUA83dJZ1-f1DU9kFrjPg_VxM05p9oaArnVsTln182G_1LR7HVi4xeeByagdgBX_VM02071q9InmTPKcnZVsMPn_H5s7PCqkLjCcYh_SMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=XSutlN2LMt9WSYCjrJ2-fg5eM8uyby8Q25c0xgbuVds9yXm2DjgNo_xzgfI2gEGip-5nZ-DvwlU9wEUW9FLTSwQ1HS4CFuTTjXDp2uiKGe7r0U4qz8G3Lv8AaZZmyr9fRC0tpnQDbh2hGpR_CqV95nLkH8bl1zDgATRSeDaLSq5TMwU7gXb8BeM8Ui7NcciEMG80KgeVBr5PVGHnNJ38Avjh5uOeUthbrVf67BGRIa1HmNhLQFtHr1L1ZwZsbhxa571qGF_m0eLszX8E0EUQb61EHjD2mkruThqDcNNamF8VUWz7wHUBJxapEY46ZpND39zYrcBkKVyM4kjCPMbowA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfBgxnBuEnK1aFhxzYI1ydQGfF6b5KpzFtpsqUXy99ecr651qbHYvvWpBJfghX42SGgzTKhJA02n88LIqttLWfYJI7eo4v8mWgTIu6X4D5La4sWT9c6UBLZGOAwDUF67TZGMNdBcJ92CXnc1Higrxdezz8pNwbi4rc-v3s2BKaJIdyAI7S6Nj-sr3yX9lfLBnwY5fqUGSKVHVy41qtSqpgXkh6w5ZHCXKyekCvYl2y6P04bq8jF14XjlBtmGDzcVSkqT3VJC7PQ4_xXC4rk7JC-C6dqNjcGmBA6YOr8EhHdti3GS-WhWqzTFEpf5n7tt_KiSOT-GnX7QM1HjpVP-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOsPkChsUeRCu01aoiCtAWvm5doPpnhoScF8EigadQHHG3hRX4FpEqbtBJnhz6Hm0jKihnC6NDWIBPy3_qZb2w-rQOQVJUuukQOudCICuhTbPXrf9EDytEdPsC3tit-_jmTUB25NIvOJuv1BOV72HtUX8EKVbRYpcVk5Yy-7CWwgpAAKMvWw_jbrSpmwVjC7ytmTz_gk4IHlQXvYBPqcud99smLPGn7MkZ9ZaLTYduqd8biQeac0uvXDwu3Zvb0yjuDS7BHU0sYBRGXOQ7_r9h_R2L5OVT51rarNQZxRgPe0az2xflZkLd-ylgN2z1edeCdFvqa4Gy4rpN65kQQF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVoIofhK-aXnxWKvYDk-7j4sr4Buqi8g25osgx_BSBvcQ6j2IWS69cmhqDxUN0uCyBpdT91yhHkGOWFVliS6LT9edajnaSA8Zn7eAr-BWDE7JDyYMaxMHuBepc1q9e9Doo4k7TzH8p8WkPqcKgoBjZ4_G_x4kW7EkWVkygPTxD3qC_oKzYfhyJZYa21jAagyKV1HPMJVwBaPvkjhYpHbFrC3fKRIV9ZbKtzH1ZTSPsfggGsCdIssLnWMhWgZXSgWGM38DBPAErvBzcHyGjkfHYkYOghqepX3lZDIxk7eJrUkovsuSqfWFSkl9PGUmBFtjny4KJMLqUopdquY7eIPyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKPgOiakNKl53N_qnR4PubCQ0NNZfoGA2v0SFO7aQIwGCd0YPgI6DNTzke_pvg3HWnuX0SKz6O1nqjNtwoOJQ351uWanMcqQ3hYGWDjH1Xc-YYQjqPqNPbM4AveJgB42NhAOFjS8-DfSpSADOk47N2_fPulN2W-aWWhP0sv23RPt6h236jVTOyDdDV-peK1nATxE5Kt07DRoN8IM17dpTAi_zl1fwQaLy9QMSLwWPPgfISP6m-8021_iwmY7iLR0LKEHEJeV7ZGBZuDDIS9BNL_PX7WHv8SQ3cMWYjyYE-0MnqtDp64htpfmDZCFYEtC27no4_tna985woq9lIWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbGYpkD1jDEFQrZgnMmyLjxGDYmuF13BxasyhjYiQbMMvqQic-HYG-G6A9hrH3Xh77_crjvsNHJhe0Y2IHc-cilYwqZxaLoiIFmY_JMDAEsFzu7y4zVlzMdtqCjQbgrisoZaBUFvV3MUoB3fyF8repY8HgLoYfp9splQrl3NQo4525V8i7_n_zqq4BEr_EmdcWka5hahPswmXjGW13Bxi8_kBymtVsu749uswA7ooTqrMSjL3sb5hkMNZJma0nKH89mAFteEeCKPxBo65ydKIr8CXdGaK-OEIgy9dmtxIeD9-uqV4NpSL36E-3iUQCP2pxWQuE7EnheINW6o6MrunQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=YVWni33M-WNfTQHdgixQEEghi26eiRGIwVI54je-OwT4CDeu3TnVx6uQZNUQqogEB_QN6N3SWNXS5sHiTcuyBygbYEpECm4qcK5TMAQpJ47VvxvBbiXmJdTL-nVvUYgBnEB6Pnzk7mPTOwI3m3Idg59gPXUTmNa1b4oxkQxdZslEchcBet3ajoV7WP9LwVt43IZaeAQIePpzLU_B6BanO62yPyFKns9aBvAhepr8JUJ326u56wTtfCsIy8PUoGnF6X3S1KvhWQF3J8YQ-CNDqJ1NqN1i6n2V8VLV5KBQ4I3si4HUhYdejcDR6nm6IXeTSzP1oubBdhDbaTwfQyv3Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=N0XBRLfmZfI8Bbrfxc92G2F6xMNRdqBZLkOXBIMeLH3msz26E9csj2X68gVb8j2eVB6juofaMB842YhT-SxRHTKrthq69USXVCb79-FoN3D3PuGqObTJvFFND3zAyfhWrXYlhp8GAiL1QAU0R2vRN6663MYTI1dHu_e4tHVGzXfZIKjlnUUDKSG49AAdfToH_NPCI7DL88n4fyNwYnwXMEGU6bkeZqv3vsCJ1LC7UeOcvcFFryKika-tCbuq-3LVbZpDHyhgQOiTpQSoMZsl79yk0ic5pfiponUR_u3WqQwZMm_3WLIFC-EJNUCPnmfhztdFpbuPw544Z32lINGnEIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rZySUpoedLvmValKfuRzVO4_ywSpLcv1IxkIU7w_llg-lYT6zveoEe5kKzE8b231KRSxTl9cQX6Fyd7RAsrx8nhl8xRsfpPj2PaTqF1Z0HNj8QRyxcvvT4WaWWwJm1LtshCMzApAaNTRWdGS0CaQlCIi2nm5kM7mBq6py4B-lMZxquuHcfDpKxZSni3ROBI_WbfTcfCwdJGmw3Yj7_eUc8ZAj9O9FNXakwu4cnPslYXJW04ulorb4QWP15A6Q4EKViv3ldtiLHQ3zcRWPFekxZ-nnLdaWOCYfr_sm8gsCW-q6nhaRIYGK7Kfc4IdkCpRRUYfaCN43GFiiNpt18G1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iLiA7rKCKMSyb88wfeHFDBDLu0NvWpAG8WAGyYLr333ZzlvZ2efoHZhc8VUDi_bbiaNdj-CQarCbvCW-A-9T6seGWy3g5Twwnsy0ul-ANtgRQ9nJ1uvr8m0nirMn2W03kn7tT6NNZwoo08AxoLWnX4DP2n65sUBhCBIL_LU0KuxnRJCL91sFzbnLss2PMiewLvTkmCISEY0kKNHFA6Apc3YVUKic8-gsUlQGsUYGXeM0e_xNe0WISrfZ1CiUIDfm5sWYqe5Kjzo_bJ2F3Nu7tVoE11crd5lG4XO0U9DNPqRsmbMlF2enRKQfeyxHW4SVtJBfKAQAJ5WPz_ZNgWpacg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_egji9M3qztq35_bVM7_ldChygf20QG-StAkTrTSKS5mHUB1z1kqE5uW_yHcXlpsQYlo-N36mN9eHyjwtcmUc_yxmRZKhRGd494aCMDSPmjkeJTfeQa5s22D2ouaOQaFuZD7pneA7kKnCez4u_yKU6FtL0laFOs8uRpPTmBYuSUM0axx6nBwCTT0t3OwK0qvFqxXAtBTjhQP010-cFeVCZg7bmf5dSu7QPLNNfiluqpNtLcsNEnSkjaHO97GvxvncBEZgpMdhj_lTSwG9iSFfPiYEn0NXvdT2iPtBWY_aGrCb52UrmZzA4NCyba3PemXDBv6a3SL8GPZ0HN7_Eo5bIo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=Rpq06E-dnaF5Os_670zH6ivdVpY4kveHT7icSqpnU-sEgEVcO34Du_lxRWdQ2gzbmiL8Y4Aq9i_d9v9wuk8ngzaoRbEWsrUf84Y5l9Ur4J3PETCk9WVN0FWozZ2NMZNWS0_D7arGo_XYuYjUkxMU981Lakn-zll0Lrk1RkCek2BLIc0TzndGqDqfEIw96tvu2EecpJF2eaRBeSh6sBgZUvIJRh2lEjGOQzvIWagxIG9iNrX3Poq07PZcxNxv6iBSBxnfl8hrj8K6ZcqwRrl38a6KqrHQPTbYu1R3vV8zWB6S-pjnIaC3dTU_rhy1AtI2zUuxT8a6mm2GkNQfK5c5v37gTD_TyVHZBsanewtTgGTfkCNc4UQ8_RXCoofWmGaRD06S8e6hOE5NMTvgajK4XtsHB1qV0Btb95SL-FzvR-jNywHZU7Iw01b-x56fkDEbs0EpfS7pEFJb2jo5POZS9oBn5oUmdBqPw5FwefaLld4BOYqihZ_FXq1aIjtdBverDxjyb9sqThprlZWMIWYOE6NuYdBu9-1SV-52yRWZUHx4a5q_zVQuUvf-RDPDnkTgGp_3Uwi8aa9EqdE9d0Y7MZyfNDVFFWgG0SoqevciEgXChL4BG9zDyVxKGmvWPEvlQPCiGGXsdJuiMI22XIlYUqrK3ZEn2muL2Jp9KX3N9Z0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVf77KjXtwBH9q6JF5AsNT90x9Prs4Nes91JWtfpTKE8kd76X4c9ya00aVopC-1Ya_4uLExJnG_dQGze2ga_8fXQ2n9FmWiGyBhCTa6phJEJ1eP8KNCSLesHBUzlXsn7oCvXoE9c9PmcE-EqmYxN7F5NhO-SoOZWaZ4WEQeQiGSt4SIg9E53nQzlqpO6wVuVBK51hmRkRlAokCKUquodhNGnRvegGUyTixZCtSuM3QBzcVvAWMT4p5mlRR-L5Hi0GpcMqJjN8HETchmCi5u-61M4BlDtZMgTlT48fkVRtvkMl2LftBgkW-Qa2WLLZ4PRLat5t9Hh0h07f0squgKvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKPGpCIyeI0o5nrw2pQ1OKWnUUBgAAv0PpOoLcbR_U0k_IBHzyBQWemXH5wm3BMZGDCE1CuN3QL-4Vj1dDlCMGEd9KKjZsZvIUg-eQ3uW-aqNpgaJ6cu7fEHm2cu8CDvb9KqfTtweSkyzknS6iuStj4RwMKN6rmPV2hPfmtkNkAQRNEboZgEWyDsNGk960jaSXIlsKkwbQ9u1SibmPYX868k_zy_5eEDmLJ2mVT4nErcqd2_Lecb9qpc4e8oKPoqKQrGQ_OOs0s6iGK3Koq4Q7QJi6y4S1SQ-UDSTTX_MXDWMDnv54zNChGrPbSEsea3MbwzIMnjqyYn0pKPxzubcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=ZI0jhzCxfye7AKF8zcVgoqEbfGSTNisUxQerRi1jIWC4u_IsVGQO_DAfEPSMVrMQvD-70uCExwFM7S4FQi9ax__to90pWVnPyh7M9wD-stb8032QTF1LyxWLTJJPpW9k-1goImJUILFlhfsFct0LQ-_Sl5gkcgp3b0TR2YiDVSjQO2E2Tga1V8SBo3WEB95H7yDBY3PSUa9TSZUsIZXKSLA_azZISy9FIIF59kdu6KyawEDOPF_qZm7cmHNmHvSuHsYJ6DkxKR-TQRmh_W5uVKUu9pWeSOSFc2ZEvb9dC_CkxQdi-aaogeoNeLqrX-FyDK_QK_Q_jucthF_R4-JGmLeQh6J9Q6mzQNptqYL7tskSdlwNNokx5KEzo-V3kRTnIITXoFBEkHpPK1lmSUFRKxGbsgWb11JeHkuN_WObFLVfiXhnsjLKVRbGoBABDzzzOf6jmwLQlxFdEOs3QGijP5r3M26fkaEg9ivJZGxp7DFn5LqYwdRRqriV4LJUZ5C0bULwGu4XeGOtdKQuLqsbhZ_kyWrdpyuFxoaUbC3gtxQG23htifrgWRAGLk8zkzyu_PHBQOqycSxESSFpVD3l_fHRCyJ9EZgDtDtiy7GFGAb3HNts_W9UPDwleFFd4MGI2MsT4VllLWSgHWCl1JbRXjEesR_Kxiq-XNVvYD1l7qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxX90uO7T6MshIvu7FOR3gU-ovvc0yVVPM32mteDbyVundhx44bvYPchc5PCZ9yEm-sjn0IVEsPVOabRfCnaqGsSNNJVNSNrUoyiijWyn_QqIYPM1V3s_HxcvivH4avCkZLcedJ8u0-RrZpVOH_XqssHBDXOrl0ZGA4XPf-lYTDqyq9VFEnBAZQL8xJDY8DZ-gWbQTm2vtx9wsphjgJaoeTib4Z891QODX3FybZ4bpTS67iWFaxOiDPHBQOug9jR0KY9eabC_0FK-EIU9BP-FlcZsGNPvASxr056xh7nfISccQz6AMuwt_ywrd3zl6KS94TTFqt0jpBXMxaotcK81A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=Th0LdFgnXKGiTfZZAd45W2uQHt49Z7J5X06GU9vaGM3mfmaPYb08NbuEpCC5fC0bQdojW-kHsqYN5ZaUrGy-w4VGmrmupfQ2TBZus-T9SQcLzkdhoMjBx_VZWSjwFV_EViDdnVcwDFInUaBkyY8-ellfoU4HSKnW1lxtIVuZ5ia-WbMuRfDs2o1iV66qklpsbwHtf4LRxiIYbEOK9gCCO__MA4BhJ5hmyIKZu5aIqS9VRPUXglrF7YcbkosgrJEt5KhnDvPNg5Xc_Mb7j5B1hfMOAlWC-03mxz3i2_ZyiOfRgulJaTM2IbuSBI4xQm2oye4XjF_2gA2Nyjw2FcYxPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-X8xnqfWVgskM_qz3Y2Aa8OBr8WvYO08UIh3iSXXufuZUOui9wB0Ug2bkiehnMcorCEaP8oAzolDJ0pF9iS_m2-HJaT3sSmeefKtsfIpqg77dXFkw60aajQLxV7lS3NXQkPJTPuiLACzW7cHMcxzdBXEuKzY1BUWB0vZm1JBtXNHjMNc2ugXEWCQZPxQVv4OltlGGscGNKpc29VuzntQ6AQOJuzXknxq9gZ3MwOEvcdbs-fwPJeLbn30sDWwhuzYyLiaB-GPjAez9ZsWeGTmwnaddNs7czckZyakBUdhl2_JwaHIxhT34D91VW7AeZZSteS8YJKgbr6LkxKOtGbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKGmlC5OyxO4AcjgRs_1YZ376tJwB8okr8aqyE5Qa33nOGBPTt0iyl5a8UjfDCDyoS4vJdDAq0WloGKjut3NSctXAncXOfsVpaDtgEXSy8gwgKqzXChYd6r5TkrrMlUAaNOCbtPHwZj29L67ors--6ACZh60kMETMMPpRJceT6Niu_CuVFWouWrzFQGQLqr66sXTk4Vwx9yD4gIHSNGEdEp7IhI668Vp9l3nPiQB2QiQqg74avcSeGMKPL96Gcwp800fRbgJ54sWsfGw4KHzaSIgku4rHgy6XEMzK0_pKqk23JAz1n7iM1r2uyW6VQm4gPb5DHn8vITxQX8Dm2JHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Gdv_on4BwfjkDyOCX6iu2J-1NbwwFOIf6SzEi4n6KotQlDG5mR4ZWxWjCkEkzx-F45Zac2hrbHJ3-3JgtG3dTxXv4DsoFv3gFoUMiorpjWV-rRj9qQ1ZpCfM2BNyW46ui1deOvTXKJipJmxBrzdCISN28oxoRuscLAh2_5B74qv9DbiYGlicztYKsCHmmRzqWkYPCtoXd1VECMFCuRmC5KU0UIaTK5l6lNr8kMDF0AwKvQyTHeZsF-6RozKuCFy5fD07-_q3j5WwXaebyfreHzlKZZQs-j2gRF6NAwVN34TJx548K0gVEwyD-15674MDoQXY--zFYpUY71hrOIoUqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=Gdv_on4BwfjkDyOCX6iu2J-1NbwwFOIf6SzEi4n6KotQlDG5mR4ZWxWjCkEkzx-F45Zac2hrbHJ3-3JgtG3dTxXv4DsoFv3gFoUMiorpjWV-rRj9qQ1ZpCfM2BNyW46ui1deOvTXKJipJmxBrzdCISN28oxoRuscLAh2_5B74qv9DbiYGlicztYKsCHmmRzqWkYPCtoXd1VECMFCuRmC5KU0UIaTK5l6lNr8kMDF0AwKvQyTHeZsF-6RozKuCFy5fD07-_q3j5WwXaebyfreHzlKZZQs-j2gRF6NAwVN34TJx548K0gVEwyD-15674MDoQXY--zFYpUY71hrOIoUqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=SdWvA61uL1Y7RjQlh0afYB_2qaRA272hvurrPaaDxRK74f7d9bYqWJ00v17qvjFgJVSLJrD0Ojj3HlVCxrl4IHYvAPsMz-pa6KBrbVmlSucsoSi8XJnYbE9mJKM3_ZyaOQhFUi2cBIE90XDdPClEf8t_0NpkCNhpEO0CqOwXAC4Z3EeCnfEzbn5rSTqgN9EETqTKUXTa-BDTZzYeHaLE60QVnkC6JiGeC5p6Iy89K8wKv6AYREscU8xE697JLL2EmD00SA6GY3JlVOqXtYVOP1jsnkeqF6oyUIwK62552MSVk9s0RQPj008Ll85R5PyfVzXzc2lr4iQ0nz9CffK7eQUj-CQEDzfXkMbQXc5jFcsEmLdsOyZCWnaQ36r4x8aMBZSSuk6lSGN_JjdsRZHsYb_ZplAUG1YB3O3vwHVbP6fIVSpxjULwp9AMpoKP0I8gZZPq_RO9qKUSyOWksTHQrD9jnnugtmfhGWmT4k36YpbNLjy-XcfldfRibPASsV-pvYVZ9iVdztsyjJGh3Dy6EnUq8NaGjd6-oGbd7PKxu6RGSl6LHoCJYge_Zqn7TWq0qQYKfyQmDOf78lNKICYKUGfteRQvXVVGsiwLj-2AGq1lXZCH4cf47KtLn-YyKd-Zo6pLWGPjOLtPeZhSiSrr0Xuc8Bxm1pZR5FPSMvY0VUc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=SdWvA61uL1Y7RjQlh0afYB_2qaRA272hvurrPaaDxRK74f7d9bYqWJ00v17qvjFgJVSLJrD0Ojj3HlVCxrl4IHYvAPsMz-pa6KBrbVmlSucsoSi8XJnYbE9mJKM3_ZyaOQhFUi2cBIE90XDdPClEf8t_0NpkCNhpEO0CqOwXAC4Z3EeCnfEzbn5rSTqgN9EETqTKUXTa-BDTZzYeHaLE60QVnkC6JiGeC5p6Iy89K8wKv6AYREscU8xE697JLL2EmD00SA6GY3JlVOqXtYVOP1jsnkeqF6oyUIwK62552MSVk9s0RQPj008Ll85R5PyfVzXzc2lr4iQ0nz9CffK7eQUj-CQEDzfXkMbQXc5jFcsEmLdsOyZCWnaQ36r4x8aMBZSSuk6lSGN_JjdsRZHsYb_ZplAUG1YB3O3vwHVbP6fIVSpxjULwp9AMpoKP0I8gZZPq_RO9qKUSyOWksTHQrD9jnnugtmfhGWmT4k36YpbNLjy-XcfldfRibPASsV-pvYVZ9iVdztsyjJGh3Dy6EnUq8NaGjd6-oGbd7PKxu6RGSl6LHoCJYge_Zqn7TWq0qQYKfyQmDOf78lNKICYKUGfteRQvXVVGsiwLj-2AGq1lXZCH4cf47KtLn-YyKd-Zo6pLWGPjOLtPeZhSiSrr0Xuc8Bxm1pZR5FPSMvY0VUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=c4VVrHHgmkCWPOzJbeu8QZsAjcIzLD_nVobjRvBM_eIRWQrCehZgyxZ9CZ1mmcX7edNLDSwvM3u6wTaZLXSVFr0wHYvKXbmnLlKHCOifMih3SBhubQUCJVY-nIG4SeXcfRahAaaevdlf5INX-3Dhe8UPns_YQlvGkFEDmk-N16rEq5_w3VrZEI_tFfxY3NFFpW2zNkc3YHlXoka2zEiaXwJ6l-Cm8j5rCQn6XIYAosoK252CQBTrFST4uDDHZQbGAEkLmnx98V2RCwKGApXrQxpjhsgmG7z8YMLKwdL93RLmWJqG2WfVPUj3_NVe-MVw93lIHvuo6TXcy-9tF9d6kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=c4VVrHHgmkCWPOzJbeu8QZsAjcIzLD_nVobjRvBM_eIRWQrCehZgyxZ9CZ1mmcX7edNLDSwvM3u6wTaZLXSVFr0wHYvKXbmnLlKHCOifMih3SBhubQUCJVY-nIG4SeXcfRahAaaevdlf5INX-3Dhe8UPns_YQlvGkFEDmk-N16rEq5_w3VrZEI_tFfxY3NFFpW2zNkc3YHlXoka2zEiaXwJ6l-Cm8j5rCQn6XIYAosoK252CQBTrFST4uDDHZQbGAEkLmnx98V2RCwKGApXrQxpjhsgmG7z8YMLKwdL93RLmWJqG2WfVPUj3_NVe-MVw93lIHvuo6TXcy-9tF9d6kDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=ZylOSgjn0aIxcQwhyexdrBtXWQH2nSwsD1CrLj-WuuCUOJFcousFMvyjmuXxZNsr_dyk9KlOXLJWbkXSnge8tRe4LNSqvkPxnj7XLLGCvF3Go42J_zx8UryEWlMzKxvohH2w1Um3XlbP6Vrq1bSZ9k-FRoUDVih3ACMLiUPXUQjg6HeZIInFHzIihxP4FqWsnqawe70vwWwCdNW43IFAFJ_JfIpB3aZ0S-OOtCvgglpF_jc_7S1gm-jOXRxc8YCB0VDSAgFCEeprnI21cRrAWxb6mP2ydKOlQ7MQun2R7FkFUSDJM1B9euASFmuL361UiDavPb6Bcy918VytrNEjEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=ZylOSgjn0aIxcQwhyexdrBtXWQH2nSwsD1CrLj-WuuCUOJFcousFMvyjmuXxZNsr_dyk9KlOXLJWbkXSnge8tRe4LNSqvkPxnj7XLLGCvF3Go42J_zx8UryEWlMzKxvohH2w1Um3XlbP6Vrq1bSZ9k-FRoUDVih3ACMLiUPXUQjg6HeZIInFHzIihxP4FqWsnqawe70vwWwCdNW43IFAFJ_JfIpB3aZ0S-OOtCvgglpF_jc_7S1gm-jOXRxc8YCB0VDSAgFCEeprnI21cRrAWxb6mP2ydKOlQ7MQun2R7FkFUSDJM1B9euASFmuL361UiDavPb6Bcy918VytrNEjEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxwfF9iKLu19DPX4G_Z7PBZe1sNB_PEqLYlY7tZVHgwj13WOwy5m3qvOZXVz4PlAhEvKOl_cGC20FUVeLG0RZEzRRBoP0Qdi8dHMNQgKymT26weiuSDm6inu8CMj-TLqRdXMu4i9lkPt8BK4SFgr6AZOnhdTyoAJzMrAD3ARTUvEmYh1YXZoi7alBuqbDWYgqz4O9e7S3ACci6TqezsKcx_axZt1dd6yMpmlP0DgJBA5UTgIuu_M3pIvVLOCgRrT4OXcLgRWBXAtui-IHTcM7sdphM-rB0rlREVQ1G9oqnlQkE1uyby3c9LSoB_gS2dvbRPuSGRJITgzgUbII9u-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102118">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=NvhC6PwTv5rR6CP1tXZyDSMkSJKvBYxG39zLxJ3TBVpQA2FOZ5xNyXw3xJk2ZhKwTkRcNJc2H_J9iMCv5xZmEu8PjTk9IX5QwNJbZNu7TcHXGeTPNrjEMnbuDMkK5H7KbLhUHUYHYxr9fGxTnDtYLxTayIBZEzgoDDQMTsN42qbdMXNWHhRjSN7gLiGvmRcn4qQ4CicPhXfEe1tROI2Po1E4rLDJakIKyEwN-vUEUnQjy_Gsxlv3WPPauxl5UGiBMQUAQNQp4U2hQE2oQYPlh05ITs-Ed4kwBXrqc6VVPSfhkQXGuDATHFnjRlQ-1PnY701_ahW-U3OWJhW4J6ay-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2348e726.mp4?token=NvhC6PwTv5rR6CP1tXZyDSMkSJKvBYxG39zLxJ3TBVpQA2FOZ5xNyXw3xJk2ZhKwTkRcNJc2H_J9iMCv5xZmEu8PjTk9IX5QwNJbZNu7TcHXGeTPNrjEMnbuDMkK5H7KbLhUHUYHYxr9fGxTnDtYLxTayIBZEzgoDDQMTsN42qbdMXNWHhRjSN7gLiGvmRcn4qQ4CicPhXfEe1tROI2Po1E4rLDJakIKyEwN-vUEUnQjy_Gsxlv3WPPauxl5UGiBMQUAQNQp4U2hQE2oQYPlh05ITs-Ed4kwBXrqc6VVPSfhkQXGuDATHFnjRlQ-1PnY701_ahW-U3OWJhW4J6ay-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یادی‌کنیم از تقابل نوستالژی نیمار و ریورپلاته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102118" target="_blank">📅 10:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102117">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=VBxjel_UU0Lc8pELGlBSIX4vgDVhBKCVPma93eJEhxZjgIyP6wVe1hQI1XpbZ3ghtOR9i92eziJPrQxH0pXSDZ5tl4-74fv5nvbfrRqb4sfMpPREZv0cEr3eLBI8oDIYmFgUa-SISG_kRGaLs-2O8xXTNesSD367mS_tCm5bzhBS7dx9Ta9Nt2RESCQdWXeShupkEM0dBAqbz_lYf9Abi8bnaRy7o2mepFbnaqkroLd2NCefp-3zG9mTF4BkZtFWHxwtBHerNtr-24Y7xY3KGR_HKodHhOES-cqBEuNm5h0Lxkp74EKZxL5ETQLJeooQkBRflzBgI6Jqm_u1zLgWQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3115e0e757.mp4?token=VBxjel_UU0Lc8pELGlBSIX4vgDVhBKCVPma93eJEhxZjgIyP6wVe1hQI1XpbZ3ghtOR9i92eziJPrQxH0pXSDZ5tl4-74fv5nvbfrRqb4sfMpPREZv0cEr3eLBI8oDIYmFgUa-SISG_kRGaLs-2O8xXTNesSD367mS_tCm5bzhBS7dx9Ta9Nt2RESCQdWXeShupkEM0dBAqbz_lYf9Abi8bnaRy7o2mepFbnaqkroLd2NCefp-3zG9mTF4BkZtFWHxwtBHerNtr-24Y7xY3KGR_HKodHhOES-cqBEuNm5h0Lxkp74EKZxL5ETQLJeooQkBRflzBgI6Jqm_u1zLgWQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
▶️
این فیلم مربوط به سال ۱۸۹۴ هست و رنگی و اصلاح شده. حتما ببینید واقعا جالبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102117" target="_blank">📅 09:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102116">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=ub2aR8veb1KkxJRO0omNy8sOdOqfYZ7BpDYrNYZQ7YZmdypEgBNC_tfVtNYLNq2h8CnS8i_5xZp9fHZ1w3MiUpA85b51K2yg-4KShi7k6f2S_4R4LCioi4qOjwXgw55WBA2laEe78aJR74Qq2ssxcioMCKH5A74YS3xTlu5UA1_yn5rDomDAeUgWQOs6Mt4qaBXvudTRCML3ZWOaWSFDfNDlpDzdx-pXWURw8i92EwenOVgEpoAgFlDubR6bOMA1--IEWUojQtndy9UbAIvSok1rsa_eM7WGtK2MFZzM1sipa-2wmVGa_YciIP8Y5zqHgoi1B2dzW7F0ZXSULQo5IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dd0bc973.mp4?token=ub2aR8veb1KkxJRO0omNy8sOdOqfYZ7BpDYrNYZQ7YZmdypEgBNC_tfVtNYLNq2h8CnS8i_5xZp9fHZ1w3MiUpA85b51K2yg-4KShi7k6f2S_4R4LCioi4qOjwXgw55WBA2laEe78aJR74Qq2ssxcioMCKH5A74YS3xTlu5UA1_yn5rDomDAeUgWQOs6Mt4qaBXvudTRCML3ZWOaWSFDfNDlpDzdx-pXWURw8i92EwenOVgEpoAgFlDubR6bOMA1--IEWUojQtndy9UbAIvSok1rsa_eM7WGtK2MFZzM1sipa-2wmVGa_YciIP8Y5zqHgoi1B2dzW7F0ZXSULQo5IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ذهنیت برنده بودنه که آدم رو به همه چی میرسونه
🔥
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102116" target="_blank">📅 09:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102115">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=insi5LiffC7aO7sA8Re6wvhToVl_2IykwCnCVKjhNXnszxOQzXe6h2p2eQCFvJ4j44STU9ZpFQ7dv3yqYmaVptN72-d-Sy9j0G7ZxtLrY9UDwDVAOcwpUaSa4cJtOwwe2q1t7v1Fap1RZ-iuH2DyEze0cvmDOgTSDT5SVf1BzTGNiJX9tbRdMFfTmcdzmaKAkwDw8IpYiCyUP6PVjdqwCfdtGiYLCI1zSGaKdlE6Q7usqq3QTf9MoZQpQEm983IRHM0DBZvEMOphkFCbmvLw7ZbhDm1usnf5d8fbjkv9KE43BLZk-F0dBfUZJ5mUGvOAeDB8C_0LdsoWXE9vQDRJ_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffacd8024c.mp4?token=insi5LiffC7aO7sA8Re6wvhToVl_2IykwCnCVKjhNXnszxOQzXe6h2p2eQCFvJ4j44STU9ZpFQ7dv3yqYmaVptN72-d-Sy9j0G7ZxtLrY9UDwDVAOcwpUaSa4cJtOwwe2q1t7v1Fap1RZ-iuH2DyEze0cvmDOgTSDT5SVf1BzTGNiJX9tbRdMFfTmcdzmaKAkwDw8IpYiCyUP6PVjdqwCfdtGiYLCI1zSGaKdlE6Q7usqq3QTf9MoZQpQEm983IRHM0DBZvEMOphkFCbmvLw7ZbhDm1usnf5d8fbjkv9KE43BLZk-F0dBfUZJ5mUGvOAeDB8C_0LdsoWXE9vQDRJ_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مایلی کهن و پروین و کفاشیان در خنده‌بازار
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102115" target="_blank">📅 09:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=izO8o-hgEc5votof2I7ZNs_Fi4QbE0Jfq_RkAfsAXhhasRaZHAOiUTB0poBsGwF50KIfB_T4WOVHO0C61VaLjx31CWK8xI57LF0o1DqVgU2pgeUCQ99k5RMLPKrp2GiK-XLZsApfszQeg0DG_y21l-WacM6qywLfNJAmyDbE7S_Hfdl0_alWNfsTh7qqlUiYkI1tzk3T82dxHObSHIglTck9hRw_Zf9eojzZCGQHi6XzLf8Td3ZOnaL4sJsn_T76hpNVJkDy4nuJrDu2fsWtgi2FdZOWMfDZQx19C0A3lUKpLJN3rmm4892_tysZatE_FKMpV9QrRbZgjc-vUheG1oGFC63V0XQeEumuLxzTDnymG8ycQqNW6GkSs_2GY7a47mWMVuxrf9Robt4V37TGpBZ_oM1DHUTuCBRn_kCWKgGQjyleRESnsDbozv7FMjSXDbe2qlGwvPq1OBu2w2UlqaVfC4Mkym_52jMYD3A7R9rmHJEA9vWQcM0xYy83gNvi08VOgkAxnmpFa9XIgr_UrvH0F_nfe255Zr6jpdpSLi5bAZopE_Y4QL2AdZkTn6Zzx9KjnFzfFFfK2yUYURefwMapusaRxSMLd_kNkynT-mXBP97towAfkTh4xskd-h8NgeZbO0pU0LvLhzt8T_qGYGs_8w9jTyR3mOV-cv5ltXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e0420a2b.mp4?token=izO8o-hgEc5votof2I7ZNs_Fi4QbE0Jfq_RkAfsAXhhasRaZHAOiUTB0poBsGwF50KIfB_T4WOVHO0C61VaLjx31CWK8xI57LF0o1DqVgU2pgeUCQ99k5RMLPKrp2GiK-XLZsApfszQeg0DG_y21l-WacM6qywLfNJAmyDbE7S_Hfdl0_alWNfsTh7qqlUiYkI1tzk3T82dxHObSHIglTck9hRw_Zf9eojzZCGQHi6XzLf8Td3ZOnaL4sJsn_T76hpNVJkDy4nuJrDu2fsWtgi2FdZOWMfDZQx19C0A3lUKpLJN3rmm4892_tysZatE_FKMpV9QrRbZgjc-vUheG1oGFC63V0XQeEumuLxzTDnymG8ycQqNW6GkSs_2GY7a47mWMVuxrf9Robt4V37TGpBZ_oM1DHUTuCBRn_kCWKgGQjyleRESnsDbozv7FMjSXDbe2qlGwvPq1OBu2w2UlqaVfC4Mkym_52jMYD3A7R9rmHJEA9vWQcM0xYy83gNvi08VOgkAxnmpFa9XIgr_UrvH0F_nfe255Zr6jpdpSLi5bAZopE_Y4QL2AdZkTn6Zzx9KjnFzfFFfK2yUYURefwMapusaRxSMLd_kNkynT-mXBP97towAfkTh4xskd-h8NgeZbO0pU0LvLhzt8T_qGYGs_8w9jTyR3mOV-cv5ltXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
ویدئویی که صداوسیما جمهوری اسلامی تحت عنوان مستند شوک از پرونده خیابون علیخانی منتشر کرده که ساعاتی‌پیش به سبب اون سه جوون مملکت اعدام شدن!!
+ اتهام‌هایی که به این جوون‌ها زده شده:
- بستن مامورها با طناب به تابلو
- سنگ زدن به مامورها
- آتیش زدن مامورها با بنزین
- روی زمین کشیدن مامورها
-  تیکه تیکه کردن مامورها با چاقو
- فرستادن فیلم از اون لحظه به رسانه‌های معاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102114" target="_blank">📅 08:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508992e992.mp4?token=eX1zVJn-z5CvsdmemePey2_kt9HZpudi615t40OmF2nqF54HHbTbs6H30zQdjKx-OyajaIE1Cxm6VYjaf_VLNxc4Pub6-PON2dI3sdoHDjI5IFMAon3cwOJ1ENbIHYPsVZ_d6Ly3qXEYMdZDSxBS0KODgbkYNc5rZLyHPXeO6_h-BLAxC0KUgVd3KnzmSGP6KBeNxhRzQN7c8cDaPl-VNwHoxhe-PjJt3HhScO2EJlKWITtuPb3L6GuShIVZmeP6BNERoVN6NjZLLQ3AoXQdVSia62cy4vP9XVivW_oGyDDtgHV6UVG31vtH8lMCSJTQRRJuWNRH3KU8oq6oOhB67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508992e992.mp4?token=eX1zVJn-z5CvsdmemePey2_kt9HZpudi615t40OmF2nqF54HHbTbs6H30zQdjKx-OyajaIE1Cxm6VYjaf_VLNxc4Pub6-PON2dI3sdoHDjI5IFMAon3cwOJ1ENbIHYPsVZ_d6Ly3qXEYMdZDSxBS0KODgbkYNc5rZLyHPXeO6_h-BLAxC0KUgVd3KnzmSGP6KBeNxhRzQN7c8cDaPl-VNwHoxhe-PjJt3HhScO2EJlKWITtuPb3L6GuShIVZmeP6BNERoVN6NjZLLQ3AoXQdVSia62cy4vP9XVivW_oGyDDtgHV6UVG31vtH8lMCSJTQRRJuWNRH3KU8oq6oOhB67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپیده دمید، اما روشنی نیاورد؛ گویی خودِ آسمان هم داغدار بود.. صبح آمد، اما هیچ‌کس از آمدنش شاد نشد؛ انگار خودِ سحر هم به سوگ نشسته بود.. ای صبحِ غم، مخند که امشب هزار شمع، در ماتمِ عزیزانِ خود اشکبار شدند...
⚽️
@Futball180TV
| Quf</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102113" target="_blank">📅 06:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3lUvHNfpkVVYhefJI5EDOo4T0ThiQ2n-yAyIlRAZZo4KGgTNPY9NJXceFHcvjKIPnizUhRubB1PUjRP84YbWTjURF0U65UzFmngGksrZ24bLbLf2x0oDT4xH48lo0ylhlYfQkOX2zt4ppARe3o3EgR_TnnHGshMWq5Y-IXkFvQZsc7-4CctwC6JDZaVWtmEwuVai4BJ4CKZXcbGazDEFgTGxEyxs2yOnkId2IDrwIoKkDf3CM8Xd2c4J-zuZDCElrj_H9KoCBuI7CG7odcHuLFGYW749ZTsjEiu5CwI8pYmp277mJFct5DoC1Y8rz6iFFJdiLortpVI3r0umD2z7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوووووری
از رومانو: پرز مجوز مذاکره و عقد قرارداد با رودری رو تا امروز صادر نکرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102112" target="_blank">📅 02:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkN10hv8tVVVkeMt99QE37VxGDxzL0wXuN9o_-Je8l6wXp4pBcV-Oo_Lv2srfogyFy4U4uXiIkcsKZpIdlZfyZ3Hdnowdf9-u1PR9sHHlsotFSLhYCHcKpNjAr3gcdJs5s_6-rNvaVwmDnzm99rS3LQ_-PC12KjwzGmjZV4PejWz08CMbactyecaUAnae8WL14yYA_ghOUQ9QGs_gBA0GlTNwHnrfyq1e60A6O57tjYAbV5ePI-JofTK74S7646n8Wp_IdLJC36hxfIGLsb8a3lwrZ_VNfKQ_bV71og6cYvZp_LOCm7YdOMNV9Xe7pE61Pm37MN-gffht44UKm1aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇹
افشاگری پائولو مالدینی از وضعیت وخیم فوتبال ایتالیا و دلایل استعفایش:
یکی از بزرگترین اشتباهاتم این بود که اصلاً این سمت را قبول کردم. سطح فوتبال ایتالیا به این حد سقوط کرده است، و دلیل آن فدراسیون است!
وقتی منصوب شدیم، فهرستی از سه نامزد برای تصدی سمت سرمربی تیم‌ملی تهیه کردیم. پپ گواردیولا بدون شک گزینه اول ما بود، در حالی که آندره‌آ پی‌رلو گزینه سوم ما بود.
ما مذاکرات خوبی با پپ داشتیم و به توافقی با او رسیدیم. با این حال، وقتی به فدراسیون اطلاع دادیم که به توافق رسیده‌ایم، به ما گفتند که نمی‌توانند هزینه دستمزد او را بپردازند و گفتند که باید گزینه‌ای ارزان‌تر پیدا کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/102111" target="_blank">📅 01:59 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=H_wOmFj--zCLztf2-hxdoom36d3MOrhFE-sHlo-MMP5sJqAFi_ZFw-68G4XXzyqqxi70Mj6q3tWCz_f74jbz8eQmqmsOO-cCTXlDt7pCmJlIjJIufdUDjv9MtRhcCCtzE9IpZBrh1fzKoFYb26LYVGTBBuFuKooWind72ZCXayIi8HiKUrem1xmEHsKa9LrLGchliv8hFmd46wi0OzZ5l5AeT1kL2QM2io1dfItJcoGGH44ND5hgARdOy9M9jD8OrJ64RALop-B1oyyLYT6nfpuNl5TFhPBAEV4ZVZCIZJhbc2WxOWLki3_yKA_QY5iNUzls694QeIXmkYz3VscQ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c83412a5e5.mp4?token=H_wOmFj--zCLztf2-hxdoom36d3MOrhFE-sHlo-MMP5sJqAFi_ZFw-68G4XXzyqqxi70Mj6q3tWCz_f74jbz8eQmqmsOO-cCTXlDt7pCmJlIjJIufdUDjv9MtRhcCCtzE9IpZBrh1fzKoFYb26LYVGTBBuFuKooWind72ZCXayIi8HiKUrem1xmEHsKa9LrLGchliv8hFmd46wi0OzZ5l5AeT1kL2QM2io1dfItJcoGGH44ND5hgARdOy9M9jD8OrJ64RALop-B1oyyLYT6nfpuNl5TFhPBAEV4ZVZCIZJhbc2WxOWLki3_yKA_QY5iNUzls694QeIXmkYz3VscQ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✨
روزی روزگاری ایوان زایتسف بزرگ و افسانه ای در خط سرویس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/102110" target="_blank">📅 01:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOy0eznOA8_0gIWvERINRbqmsPqLRuf4ABvAs90r3ROIe57RDt4q8h994PFoeUYdavxevG9MlDkASksDjxRtjTskIhn1ZRwJMuyDNtzQOPojng1NjmHf5oJYw3Ut5qDdx_VodjU9Mltb7MioFWpbHit_zr-OT2t54mM67qSpP_XKRN753odRt-_5Rqkfhje6_0FCXUP46g858FXPk0CfNr44_MYtgKwW3iEcdqhm_d6cn_MHN1-Wysk_GwaK6XhoK1sW0rIs5x8ij9jiAN7Rgler3pAzCln1Nf5asTz9xzbwgtU-OtI9HycZnHoYErcwDy_-hfYiynZStxyMei6d-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
‼️
لیست گران‌قیمت‌ترین نقل‌وانتقالات تاریخ که ۵ موردش مربوط به امسال هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/102109" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102108">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6Pf7RqTDgBou2TG2bE0ZNGuWuMABZrBHyELw2RVTeo5e2sDdZTMMx4OYggTHMGzgA3dK4f9UzuGNN3FmQsy_vcvqOYrWFz5iUjr2R0rQwnFwbZ4gkyD_1wpo3XQPenO1fTs1bvAdeC0J9ildW1W6Cd7nIwjdrdPTDBHoBpp8q8OSze9zfuUUtfkn5Y4EIpdwN6CZX4aMqfHScLnVcwxiK1iREoGKAJJiSmE4zumEzUv4a4nw359YzO4KByGAy33cfw2PAP9spZijrlW3Mv6P-NGsMXmxuvYg7h5-GGhWyLWUL5m2ej0GobiiQIfeif0u4PmO-H3R9Er7y6VQwOCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پینی زهاوی ایجنت لواندوفسکی:
لوا برای اینکه بتونه برای بارسا بازی کنه قید 200 میلیون یورو رو زد، اون پیشنهاد سالانه 100 میلیون یورویی از عربستان داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102108" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102107">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=JmQVm31Mn6nNGGASoVcxjRhtLdy6w8G2zd0zQVJPxvMYy9EMKPybxQd8FFDcxd0406tkCp_qya0yKLJHOCVYSXfSkxkkec92aTA-ndga5iEoITJCSL99oOeNj6trQk7Cy3RhLTWe0T4IIQiOZ7Oek5hGKfgMO7WAvHfVvSDHKstNfRguupfQWAzzJr_373ubvN-kdYBSIykTPopM53KPeONeGbe7xWvhwNSClHLkJBc-4a9TulkrL7or7LNtx-uC2wwoEBjJafMXEL3kqAOLWCL72K83TekmkOg_7l43N4AXScu_7EZPKYpqdPQ3LAVb8BNkSlhyMDhX6s5Uf8W5sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102107" target="_blank">📅 01:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102106">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW8q_NQ2FijcnMZi9VdoYkPF9YKVWXrQAHTz78doHnzKgTEvcoVy9BoCe8jySjeGoJPf-ncGlrdiFIqX_QrSvcRaxsNZMzGh6Sufb71kY70N0jMny9iHmU-OxYJhBEZWFsDSRM91DY4p6wybskJMJtP1iitdUhsO-7d4oL6zKZYGk6N4fr_axV-E8GbGH-PBp6p8nVY1MNr-Fsj_pkzlRxiyMZKFozd01ZBG_H6fwL4mUn5DdHfDZOB4dtIjGrExJem9n3SdD4zYxXunYBZg9dFpQSjv5HbS9Y3CvjuEJwugw-A7c1hGoVJzTfOtzknsoxGXRJkSAtQWPV4yOqTkag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🤍
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فلوریان‌پلتنبرگ: رئال‌مادرید از علاقه آرسنال به وینیسیوس مطلع شده و اولین پیشنهاد رسمی خودش برای تمدید قرارداد رو تقدیم ستاره برزیلی خودش کرده. از طرفی آرسنال هم آماده ارائه اولین پیشنهاد خودش به رئال برای جذب وینیسیوس هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102106" target="_blank">📅 00:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102105">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_OOZe1Q3wG2Ua-LpsjsxoTY0enACajvSWYdpYBZj3DoCqqb6JEQWFcJsUm3ItQJGhhDINAcFiv2yDmUUV5kxP47gYIGC2NgpR6d-faEf6QZ5SDMR248zQDR9CHgYz4cjH7gQrgijH7eA6tju0CwgbCpucYSnz5JE-57D9qgbID7BXfGONuOWK42gABZulJV9vpH4CWCFjZZOSxdquFp1CFIyHhphmhOMhlQzQytiW5XgVOVI1FuCiPN_6D8Znq7wHElVe2mxIUx6RFE-nmnfO9CSIVifz8Zg1MePWtFAB1WiHG42XXLvwQt4F5DxvcIPRIkLMnARXFA8fxnrYvY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: باشگاه چلسی موفق به توافق شخصی با جردن هندرسون و دنی‌ولبک شده و بزودی باید شاهد عقد قرارداد با این دو بازیکن باتجربه باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102105" target="_blank">📅 00:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102104">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezzibQZw6rA-zq3stQfIiJpCd5rw7NEhVEyuclqNfSPFvaWPlJYj0UclNRyGFRwhlt1mWrJMI54hNa25SLvRY-B_SKg-HZPLIj02hHdQw6hT9HNk29Baf5Y3egAroYI9a9VQFJnTxS7nP4aJQeFaOw0FZdFucLiEz5khzMzd9lo8oeYihL4G5Rmvs08KQUpTorZDVh9-sGFCNQlPYpRQlNpaqF91TXHRofEjKW7TaE4H0juVmEfjZHXL9850-eVW-B_T-Z8zIrilA_6Y90ZQ86FmE1N6U7IophCNHKYgFwfRV-chvy9yz3_wIR3NtqU3n0EhMRyXuikgAz6qwhE3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇩🇪
فلوریان پلتنبرگ: هیچ توافقی تا این لحظه بین رئال‌مادرید و لایپزیگ درباره دیومانده صورت نگرفته اما مذاکرات به صورت فشرده از فردا ادامه پیدا میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102104" target="_blank">📅 00:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102103">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vrcky55GDmGywv7N6X7Hskn5-c1xfM6MKzdFglGPGO4eWP5k3WLJjLN5eZwm6HmU8nn7U6vBAQELPRwThnaY3czXc6vYmSYYOgU2-oOqIb6S4nEcNyutljm8hlnwIxTYdF8HezxBxFdGbnwvM1D3RQGmzRSSInoZu9HAqZ-bGXJNkpoAcwTb--6oYePyILwVJ0ugsmbiax3Dr3pkU7YbxYkk2J2E1D__A-jhlMKhxL0cLLtv77hn6WJqhUgACxm0fRqZELmq6mXbJTsbe4mJMw8Z_SihTIQSQSrBrih6ebcRkd6Rti-87vjfXc1i6QqDNfgWWHZw1yAzfgY8s5Ecrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
مارکا: مورینیو درحال تلاش برای قانع کردن گونزالو گارسیا برای موندن در رئاله. مورینیو به این بازیکن قول داده که با وجود امباپه،‌ دقایق بازی مناسبی بهش میرسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102103" target="_blank">📅 00:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102102">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fH7oJrZjjxNWV5liQzuxQRB-UJVOQZLwPwdMJmFCiaIsvo-oyulLic0pocRD7bpK8sJnZSQgFCTzSWyvHZjNXYE_1bmIvl-x9CpW2mY3xRtceIb5onOZ5WCxKig2BCiRuLovzwx7T2K8kahvjIh1rFyVrWxWLdhkayyh5rfZIkxjs5GrFvRgpQ3Ag0of9uSlYNMQzDZF5pL-9rFrE5CO7Pwltd_zGYdL07fVIlshnfghE32qqPOemt2RqEZw3_53mxuKK5nJWp_GqHeQqMG-cY_QwsTq1HQtqdLUyEmDHeaibySynCqCB3lSEZL4byu3FTdUpy5jESx4AOB2W-sUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
لباس سوم فصل‌آینده رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102102" target="_blank">📅 00:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102101">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=JFsr2aNDW5w1fWFYzEn3xvipzVqcZcpJvWY39MrK700_CwST0Qpe_K_X8_KvIKHcAktXAhY7CWli1VGggZUA_YPGYhIyrcWYduMyAJPUiqlCZ51FTG3fWoqGt3E-ymzdeNFq4GcAg0xutMWoCxS3Ac7_PP60GuDulh2H5DZejHSeI87wMRres8-J-LeQ0MZdEW425K67vyF7gLfbFWTtpHwKzJmiEZKGAb3odRt2jdL_-EWKYi-ADH2Z76MvxLaUqfOBb8WQaDGYWBmTzqhFpEQi1QN-JcKKomyjLeqyWYxrYeJkvD8LIoQHjRwhFpxu3sEW2EBrcTjlegY2yd1rsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52dfeed19b.mp4?token=JFsr2aNDW5w1fWFYzEn3xvipzVqcZcpJvWY39MrK700_CwST0Qpe_K_X8_KvIKHcAktXAhY7CWli1VGggZUA_YPGYhIyrcWYduMyAJPUiqlCZ51FTG3fWoqGt3E-ymzdeNFq4GcAg0xutMWoCxS3Ac7_PP60GuDulh2H5DZejHSeI87wMRres8-J-LeQ0MZdEW425K67vyF7gLfbFWTtpHwKzJmiEZKGAb3odRt2jdL_-EWKYi-ADH2Z76MvxLaUqfOBb8WQaDGYWBmTzqhFpEQi1QN-JcKKomyjLeqyWYxrYeJkvD8LIoQHjRwhFpxu3sEW2EBrcTjlegY2yd1rsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو تموم فینال هایی که بود
میرفت تو نسخه (پرایم) خودش
و تو اون نسخه دو تا وینسیوس و یامال رو میخورد.
شاید یکی از دلایل نتیجه نگرفتن آرژانتین مقابل اسپانیا هم نبود آنخل دیماریا بود..
🥃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102101" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102100">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=Wf4s1ZS-XlOxiU7RZ1Gg-frpsP7WeoJh37YfXCaJE5tk7QrMbyMVFIJCpsqb4UuuZhDhfVdp5yZytGatvfB64jWlnSi8TQWc8y1qfOVNZbBCqQhFonLWPN3jTNIsIaWz-0IqXLo8Im7-SSGqgSwMwN2BFVToPRwOGdDPwN5JsFD0Sa51ZmbXUR1NbpABUaCs0l0SvQo0W5EWV8jMgcsmm4ZgqwvHMaErxB2Zs7lk1HqJP_HTGsqpyF_RjeuoMnaP2I-q8FMNVLhwMrY0PPO_XOk4lM3iRfSPEtpDgTl6AvSXC0eamyDIRBjMqTqwspkZrS9DduqXS_xo1C_fLKmtQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f39b79d0a.mp4?token=Wf4s1ZS-XlOxiU7RZ1Gg-frpsP7WeoJh37YfXCaJE5tk7QrMbyMVFIJCpsqb4UuuZhDhfVdp5yZytGatvfB64jWlnSi8TQWc8y1qfOVNZbBCqQhFonLWPN3jTNIsIaWz-0IqXLo8Im7-SSGqgSwMwN2BFVToPRwOGdDPwN5JsFD0Sa51ZmbXUR1NbpABUaCs0l0SvQo0W5EWV8jMgcsmm4ZgqwvHMaErxB2Zs7lk1HqJP_HTGsqpyF_RjeuoMnaP2I-q8FMNVLhwMrY0PPO_XOk4lM3iRfSPEtpDgTl6AvSXC0eamyDIRBjMqTqwspkZrS9DduqXS_xo1C_fLKmtQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل سیدنی لوپز به آرژانتین به عنوان بهترین گل جام جهانی انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102100" target="_blank">📅 23:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102099">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFAU3HkUqEevbpwkOwE0CPhMAYAaqMC7E35-M11k_NDsHXa5O0lWUHaFyEtkiMjEvt8JkJveKl3Ei0yNgrhUZyF7CyuV6JbpL9jjudn_MtEBuJkLy2EpFQYu02P2MdSAR3CQZs20zmn1en2_zlXiazzjJ7_qkwXEyOS2L2RsQ-7aw7Fvlk7U3Lb0sX9aBj6KFwfY-ctkWHtuU_5QvzoNydNKnz22AMTFVFKcIb5WFBTmENjtsDHYfqQx3-ILRDWoayyq8pgpKIwwfC25hJ0OBEonPKZSFX2ygGuvVqObGVBpnYHCXYNaoNtMFAmi336FF18RS_A2j1gkyoijMtY0PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رومانو:
جان استونز به اینترمیلان
HERE WE Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102099" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102098">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tEe__o0oDhBJllqFy09bmkZABH8-XksAYjtoR__0wnNVIyLTYo5tZXr_XjodxBzRN3TgTN-z5UCdV0TwMoKDX68cpi5JoUEB_7jQpHB4zB9A54tNyR0tKxOQnj04hmyFO0tyl4ctRrOyo8kJkZWaMl3m6NgPjarpdt6AXI5N7CSXrxj_F2khu3QD1l2UxiCkn_YmUs3u2MNnquS6qn3Oa8sdqBHmLOyODPPEAiaejWbGs2P8Z7ZVm2_40MI0pPlmQAdJxGoz5xvrrzjvu1ApRdksiYVYXDjPIVRcGeBuN_PmsRA7XL73TlXJVTP4oQg1kz2B2pGTikLm0H8M1iU2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندریک و خانومی و بچه‌شون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102098" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102097">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLaC-Y1FeJ8z4SZRAmAkfpd2emOTSqqzFWFzoWjXpM0c-bF0-wyDWn6GZJ7KucXRdBXojL5HjRF-s6nFfpjXzRGKSGhOkb7fgH3YGRuWQ4C-EieI74Q9COvzdBhbBcYeTpR283KK0U9fTvrwaW4MztqwFWABzruJkdpniTP8SBLT9iLG2aKiMF9eMorD6_E6BEQOkL1SCt_XhE0Zyo8Hng5cNxHYEiEvyp0u2N1oxkrO8-82Y2G2Fx-ny7-Jrbo97BILOxrgTpqZJVCXUsX_OPkAKjoMmG4NogwPy_zkbxmP_TVu54mPL2wYWcb0pqND4K6nx8TQ8iNIyFg42QYdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فابریزیو رومانو:
جیمز ترافورد از منچسترسیتی به لیدز یونایتد پیوست. جقی 3 بار ادیت زد تا تونست درست بنویسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102097" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102096">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biXt5webrI9CPnfrL6RVw_lJdukwJYL_Wkoz9N7iLgxngJTaUOycr_hMZMYG8MPavKYJQSQysLM2PL99jX5sIRcAfMiEY8SrQ98PRedYBaeocz09X8S6SkOmfXlV-Fy9QWCqGUnFvaOF7nZ8nuWNA8dl9sIS0Ezauc_EjeV1NPntLy05x_Alld37dHc3GTo0RzolLUMUcL5yPmqFXMMxzbsZQYbOtW2HTVP03_49YqA31hbnb5LVkSZNh9z1Xjlk1isz1k1ozS3Xeu8sPvuKKmv_8T5Em0B8BBkxOBXhOSmpXex8IC2eDeQgpht0vpRmNqzHw4OmyknirlptrC_Rxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
تیم منتخب بازیکنان آزاد در تابستان 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102096" target="_blank">📅 22:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102095">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🔵
متئو مورتو: جان استونز در آستانه پیوستن به اینترمیلان است. دو باشگاه در حال نهایی کردن جزئیات این انتقال هستند تا آن را به طور رسمی اعلام کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102095" target="_blank">📅 21:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102094">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gApmiF8XNjpjhdMe6m_aWHfYnGDdb92QR_YEeF5t9q-xz_VbcPfTQIBSIzmyyMWUcXb1LWXYL3A6vUM7fPQeV5Iuvmj3IvGJhrq9dE7p3w9iM3IfvNtocmHtp5pVgT_HqQr7NwL9Wt0nWcdY0qXdDSWJN45MAGrIMTIRc1QjJKroUSG-OU2wcEvONSM22TE5FqCeUck75eH8ovZ_TY6JqUQUHwM_mojQYi1nsODg9eOrejA280HoZqKp-fTW6qCD6hDjlVm_dt5XroHDWsiCeNHK91ElmTdfQ2iAEvAnM40wSMBqOLXzO0wivBkvFPRAya-MI72aVCTJ1C1t7gDsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فلوریان پلتنبرگ:
لیورپول گفتگوهایی را با مدیر برنامه‌های برادلی بارکولا و باشگاه پاری سن ژرمن آغاز کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102094" target="_blank">📅 21:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102093">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxG3n7rLjJXITesMiSfPfWHfuFKn0fCqNHUp8X4S7of6QNKl9tpqxTqJU6BtxIfAoKoKOTcTJujC0iVhqG_URskGOGB0DWMHqsusb_PDNvBUWthoY0z8IdNomjJl8frThInUulLT_w3VvHMl5MHfHb5N8fe-vGyEQWNDHaMd8nveUaJDN7DrbxJQqQRxQ3RWelNTgjmIdeVgQ7WB8EFoF2leyC8T9DICze8h7s34daXr7J8_5EJC0c5TUeSQvp0uTalUnW22Lo5P9iEHy0GVoPm9Oay5hEdaTvqA6_tyR5A7Aa2Zq6b_eRipGbBVHbrQQJrMuAhP02bt4VEzDafQ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو: چلسی قصد داره جردن هندرسون 36 ساله رو به صورت آزاد جذب کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102093" target="_blank">📅 20:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEkRJJfhZ-ldklxLyZYXgnlwUCHkqJmDXKHcBcga1O3L1rgzY5XG7viv_fVg0E8SiVsRM3YyBNFqxVsfqYyliRrauO_U0Q59I2PuIz_qrfA_HWkJcffguoyXS3xPvQyH8LV3IpvVmvVqK0WYz00hLqsK-Urov_KwUivAQ9XcOxUJvbdW1MSwCpEmXXaJdSayLUkNlWPZEsqgfyeT396J3KUr9iQcmMM9Q0193vXlI8Gxnyzd-5TIIqnLT6NXquHuubBE8UwQ0RO3TWDx0O_3Z-KJdcQoXLgz6src8dG61_rKFULCD8Y060GNJ42-YhwesrtZxc7TcBqXw1sVL1eZug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇮🇹
فابریزیو رومانو: پائولو مالدینی و لئوناردو از سمت‌های خود به عنوان مدیر فنی و مشاور در فدراسیون فوتبال ایتالیا استعفا دادند.
❌
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102091" target="_blank">📅 20:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102087">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrofzIhm6wR7-I1UOU29Slihz7tImdkK36xbSQUr2Pf-QZYKoLUHLh3L4w4ZIM3KJAJ4PkyHHMNFLarwXzCZljItRiwTO8jJLx0hGNDJBdKSd1qTnytS6CWLSa49jzaPqJIPh65gjtKIBaicU1Ao2bC35vknDQaUeGvI5B5jd6HqIDrMImJFe-6IpkSfyJXYj3AlBEgT-7HImExImTjVz-qwighRkAcOY2O5NI_ZuwFBTvo62Z16FtjtsocYwN_95I4XUFOEa2dETfFnNpjaoy6pB5xIOZ6AoI5PpCyyZ811p1nssA7BVp2V5jOJvtFk4rIcOveLtXVzH4s5GTQxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVwUPspxD5KITNHcQxxNBWoS-jlRrpUkn4oQ9bnSdrknkbtgQYwPp7P3dccYlp0ymcjwe3HFiBdtowaayqWInsz16fCHflE3xrt0CDh0CRb0HNk7_BvNNyPT12NLkOTYwjGYBwTl8g5EbRZO557LOh_R0oxc25i-t6TJM0MxluBOGBjWi1Qjit0-EKsobYVzaav4yDzf2PUWbYJVnRKN7s7OFO-h98MPdrEwrOKMJ4J_cSIcPI0cYZp3Bet9U89RN2tXgflHZVQobSYBy9LegZCpiS34HkCfCn5-tvwQrE5fZUWQMJitIKJiToOlFXWbjf0DUb9SEx-OeZ4JaRBncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jKRr3FYbbIKrUDtFG5JI9VYoDbCv_7uwZpZQNWjuyM4WipG6kBt9k4ZKLBWKi_NMCzmG8gcSjKZHMSQxNbLLx-9NXj_HmEUjrbxG4J75dV7NJ4XBAUsodsY_SvHze51QofaGeOrjVFNaSlh09loybswFvTTuUZbj9nZPwywulnVEQ4iLj-S3RVcPX2KiOjvqQY6u6BdweQDAAW2kHFA55fVI-MY5Y49Tm4F40r7Dr7UEcqPrOB2EBUkMxpLP7TQDUcZG-iM04as0kubtl1_6WV0K_tEgTYEwZIT1gEoOV6zg35JeuL5L9-WbLd5Y6iR-LLR0TVGR4M59D3Qpktqwzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adXsgi-4ZhZxO_ZcoJ7TOGQWz0NJyLGRdcpg9GKQ3M3JUL0u8ev92nALBpu3ES9qcECzd4hAoIPbZgbeP6tN-83ZofoG7p-cM1cwAIQAW-kI3-f865bQfZyX0vc_DVCK0l0QkgQVIgXX9bNVr62w-7djuIfaB_MLPNX6TaMm4jCXc2gbCw99oQ-mEZdYalBHiVVxID8y3CIs0ltKPsDB3x8Jdm2qusGvoUZcJ6qn0c55L0w12H2mmwTZ_XOcu09kZUeIl62p3EFQ9Fguvo5ZWLjgLoJiCy_WV6jPqTFeOI_gcJpFTzzyTFJyHLdcj2vwt758p8TBXfrW1c4p6RV20Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عشق و‌ حال وینیسیوس تو‌ جامائیکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102087" target="_blank">📅 20:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102086">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIhmo9U1ixEUncomYo1xMQFZ9dpZ_-9SqUzgSNKa5pukClKEW5b2k--rbMdgMGcXOvVCwowtyu8EjEw_iAn1oc8K26Y4bp30qC6cYNYwat8lZVb8oadY8A6A_acPG7bW6dQR019wGYxXkN-7nNu6Ab-z-Dccp1UmX4L3oBpB_MYQ5q_cNRhvDqPOos0IUikZwgKC1HUGoqYYTl5g_QmQKTuTyyeik5or1BUjvMAGQXxYm8-mrj_U0kgOAEBa49Ft0VqimfUQix55VRbMJmbXG-XFfzqI16pVBJfhr2rA-g_By9JA81MzW9gUoDABqcctSyykk8seHPtBp_8nruMXPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
گلوبو برزیل:
سانتوس قصدی برای تمدید قرارداد با نیمار نداره و این بازیکن در دسامبر جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102086" target="_blank">📅 20:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102084">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVhx8SLmYg_pqT_wnBK0ppg_GBH1-dMEuat1A02TKd73UnRcFgANt4cxGu0tHx4PITlYSLWAPV0U57_s3pH2c--zTFW1kKqs8DYuXZYO_dzuaO2MNgIEAiiZN-z7TL1N0zSIAOgziKMcdINfae7WY9NVJ1bgcMzEgCyxEmIokDVuOZVvcD-dsHDY5PyRh7RrQ_CYDopuMKRdNT47gm6dc0Zn9xxBqj_Qom-jOKYh5GArEwIvuzVMQTAAGnZLPkJEf2rmWDwyzXJvwnI7KAuLDYpz3sMQdLXYwCssxEsKnz_yjcC_MnfITs0r9iAZ8wjTgqfoHeEKEnNmvs67rhhp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZXMnvNQny9OZOUpIjsRcemtZgZxIZWR9UsHzshMNsBzPSRcntTi-60VKJmdAs23_hRcxEuhH2owUCz-Uc13KXDZOBkBUbt0x0NYiOiRzhJw6-1gS5ZDXR61BpsHI3szlfekaJv4Mzcgi1pIY1pa7oXFlooOzDKTe6Xkyq78ZoskAFwprDoq8A2mpRn4T8kXdEg8PXa9-3sY9hU9vuGoqP4wCW5_P5sxNM0g5FCgvvO43rFvkAl11HivMhnEVYtQeP1JQ7-TZ5ftJiVxJRsGQZLtKJugyvp-L4dneHn-VQC8KIpm6XpF1lIETiChXyG-H_8jiAbmXlueEJM8H6DCNkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی درباره شایعه معروف طلاقش گفت:
اینکه همه اموالم به اسم مادرم بود، هیچ ربطی به ازدواجم نداشت. از ۱۸ سالگی که فوتبالیست شدم، مادرم همیشه مسئول مدیریت پول‌ها و دارایی‌هایم بوده، چون کاملاً به او اعتماد داشتم. حتی الان هم قبل از هر خرید یا تصمیم مالی مهم با او مشورت می‌کنم و این روند از همان اول همین‌طور بوده، نه اینکه بعد از ازدواج یا برای فرار از تقسیم اموال اتفاق افتاده باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102084" target="_blank">📅 20:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102083">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2Aa3_3r8uy2X-yPRKraYnaAp-aGxj4EHrKH1ktuBP1M3gR_0N9TqlFKnwiQ9DwDeggbCVGCmVF3GGhikCDZquJ_lJlNjLziqZmBxgd1pWwcV3R-LDGaOebl-9S39pPjt-yW8BQ3R1GdjYbojn4TfnoCf0HWs5hrnj8vRQ-tGC_7Uhz1ezRmj-vrChc0KZw410t4cu4snyiEZ3lrU13GulAmjVM9-1pujQ6CGLZgdyrjKBL69y3FSKqPrWISjdoxpwngQXE_KISQ-FiPxkuGDF0O65rxxlAcPyZGuYNiFXMRcDIaxY7Gk2UdBeQlct8JV3HjKRHsnDq67KLl48ywlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⚽️
امار سه فصل اخیر جونیور کروپی که ظاهرا گزینه دوم بارسلونا در پست مهاجمه
جونیور کروپی ۲۰ ساله متولد فرانسه ، پا راست . پست اصلی پشت مهاجم ، مهاجم نوک هم میتونه بازی کنه.
💸
ارزش ترنسفرمارکت ۵۰ میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102083" target="_blank">📅 19:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102082">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhu85DW8GgNx91ap8ruH6qlmIIYQvcLXXPkf6Oq70jTbL4JTZDH-9GLP1H2hKZ8WpU2n_fOot9yiuDjd-i-4y6LIqkXPe-AYJ2goxmGabbrJFEW7vDavcKcwMn5pHSdNmcvJB1ATBWDv0hPXI3zJ_z1nGgDBIl2xoVnwbePybGm3q71ldb_8-8LmPfhgkTV14WEwMv59cSYQFAF---xlQnyfA5L_MZo21M8ynR0KYvkjEdJ3_hwlAu9ib-UUd0255AzZq67VM3SmaJ7hNHAitmCVXiHepZ71q-4gLcnrv0vN4g8esVqCw1p3AG_4Ci7JNTN--WX5dK4XqHdnztZydA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدرتمندترین باشگاه های جهان از نگاه اوپتا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102082" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102081">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=rhph1sbamYzGg7GQUKpzHvY2MpJeSYhmS6WLY0tri13w1Z1NXRHmT3PcFzi2gkYRM9LuAxC0ITYd2fdRr-VQQu_YjbJ62pJiame_gTeQgt95qbu1WdzlS2KLr-edYPT11rnkKWsMAOBHoZZpx0aZ-1VnUYUHhtbzLAqGmA-cSBf52kI7VVl77hKSvMS0kBcLQ-QflPA_uHENt5K5lyRDxL03qugo9Vumc2nYKpdwpA3cP2razE75e6ukCWppRGGXpf7hLAJWx-O3JvM1ZCZl2ceFbUEgZGAlha6oNuZSvNoIsOUzqayuXNgnfdAx_TYKPDVLlUfGUVDd0mtBaeCXjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e948c535d5.mp4?token=rhph1sbamYzGg7GQUKpzHvY2MpJeSYhmS6WLY0tri13w1Z1NXRHmT3PcFzi2gkYRM9LuAxC0ITYd2fdRr-VQQu_YjbJ62pJiame_gTeQgt95qbu1WdzlS2KLr-edYPT11rnkKWsMAOBHoZZpx0aZ-1VnUYUHhtbzLAqGmA-cSBf52kI7VVl77hKSvMS0kBcLQ-QflPA_uHENt5K5lyRDxL03qugo9Vumc2nYKpdwpA3cP2razE75e6ukCWppRGGXpf7hLAJWx-O3JvM1ZCZl2ceFbUEgZGAlha6oNuZSvNoIsOUzqayuXNgnfdAx_TYKPDVLlUfGUVDd0mtBaeCXjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان کریر سرمربیگری دلافوئنته
از اخراج تو تیم دسته سومی‌ تا قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102081" target="_blank">📅 19:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102080">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
فوری ترامپ: به درخواست واسطه‌ها ما در حال انجام مذاکرات فشرده‌ای هستیم. اگر این مذاکرات موفقیت‌آمیز نباشند، به اقدامات نظامی قوی بازخواهیم گشت. ایران فرصت کمی برای توافق دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102080" target="_blank">📅 18:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102079">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeUIUuW2UhGqKQOjn9mBMQVNavjQxbx58Ku9rVN0nvvh1TDkehdGfHqS0YSOlwbH8S37B_qLOJYYq8q_YhEqQ276PEyDgWIdUiWL8y-CWAGGKaXzmO0jJlpQQAr_V2qTtT4SCrioNzltxfREN8OwjVa3LgRbAvWhxYhDqsiIlEzGmazzWyLctdnrMmX2aVkis1WKhr4PkKr8X-uANvWAc_qRogcIWDVMLgf6TaD2S2nKrbXdFsMvjRcsnGMqsJqo-d7ahAxVFMAjX19B3bc4PUcG-5FZgwZdyzr1QK5OhpUaBtKEmhSiN_68XnXLYZLAb0LBJd1pOBKsEdaGOJcIaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
👀
چند ماه پیش الچیرینگیتو توییت زده بود بارسا به بازیکن های بالا نیاز داره، و حالا همه این بازیکنا رفتن رئال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102079" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102078">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp8y8A2SYBjbgInwF-JF8p57Skj_BOCAA_2whV5b_10-c9uGjTxyDf3hez_wbPcTEPgsdpYeWoR3zvErulZnEgTHLegdbBKSi_bPm4ZddQYDfy4ssq4KP_8JBrjXccoz0EQ1z0fMM_TO7EUoUKvHDwbadmRZJ27awI9CI-f2dqJnWY84yZDQhO3BSQFhq6ET80yJzeTryBVB9BBxCuXqAuHNNpwXUwFpTE1v4EDmgy3OvTsL2gyyosOTWMeRzdV6GthbyeyPlJwf0rUyi3oPc_crnDynylwuMA59GxLqdJ3ojO_bmEqZOyhvHHveu5Gf_HJtLfEMSgwLhbrvcKlOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
امباپه:
ازم میپرسن ممکنه یه روز سرمربی شم؟ نه فکر نکنم، من تو تجارت مهارت بالایی دارم و میخوام که تاجر بشم البته بچه‌های تیم میگن تو میتونی برای ریاست جمهوری کاندید بشی ولی باید بهش فکر کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102078" target="_blank">📅 18:13 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
