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
<img src="https://cdn4.telesco.pe/file/e5yBaKnljrCZL8f-XmngXq-2B2E1Q0NSSzMSzE5PcZ8g1-NzrM1iZ3Y96Yt1J3sek7RqP1Vkw-ssWEioNf54qZ1zg17LrPuUz0R4NwCGduwQV3Ex-_IrpZE5Rw-83-Mt-zKp1iFM4VDdtWkbcWsOpOKOvZQgse7NURtVyPr_Vt9pweyTqO6dl3QYiPJhoQexCfTjMwcKkIaNPEWDD-WkhVA-axK1c4p95axa2MWypfRCVc_efsuCKJ22dvvj6VtpfywzR7Cr96YWMxzXmlJMzwCPntGV5fmr_rOHTnlqzMEnaozpICU_aiPoVw0l-zUCJJBh89_Ptb3mRGZXSx4GQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.03M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 02:04:20</div>
<hr>

<div class="tg-post" id="msg-691579">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA_8VfFWL29LP7aIsZzqOP5aqkUjQvgnLBpDU7zi6Lp5YySP9YF20VntqIwZYJHzsdMBBbZrmzp7qodfx1Nc0b9fwTATA820nATfrbhoyz8uje_MLWRtXxasoShfy3J0Fwp7PiH5DZcx_Ce2wVlt6lnqRjef_CVYO2j2Q4kpMltGmxjUNynjJ3RbybRqIbYR3g20xsvv4XRurytiYuLhzlgfgJW9glZqbhGtSl2737zIM8D2v8-iMnvkheAT1CCtj5DS9ZrHanVDwJXDwE70Jhtth5KvIHiXLPkbJJ-AyX54Y-oJAmP-jeiwvXP2_3FR_j_eMAibILPdCLV5j5fuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥾
نیم‌بوت مشکی مردانه مدل Sorush | شیک و کاربردی
مشکیِ همیشه‌ست، مناسب استایل روزمره و رسمی
👌
✨
رویه چرم مصنوعی
✨
زیره PU سبک و مقاوم
✨
کفی پرسی و دوردوزی‌شده
📏
سایزبندی: ۴۰ تا ۴۴
🖤
رنگ: مشکی
🔴
قیمت: ۱,۸۵۸,۰۰۰ تومان
✅
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/63746/180124/</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/691579" target="_blank">📅 00:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691576">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6c245cce.mp4?token=XNgNWqUK8lVV0ezNnbQxvsd1huPF_1j9rMbpAuYueuoGNxDc0_NkVyl17Od3nvyvICfqP1as9TOhmO5OUWtSqt9CwtQIW_2lfN9d8_WF8lidI2X7s-idHpPUVXkY-Q-oc9ZaaMKSkBn1ugH0gWG1jXQg4uncQD73R9GG-wbnWSTa9s_gUw6VwApQ1spEYbwL1y41Q2K7EyIuNpPS3_8i6PBMrJDFEg_QeArHl3qvZw5cS_rhCEX_nu7hQyS4cEDNSFfmUdaeBfEqB-HoGT7OvHrcMGXwnJHM4IGYZfN9ofMZZcG-ZBb-imzmlYlusTVO5og1O-yEZu8Gxj5skE3qEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6c245cce.mp4?token=XNgNWqUK8lVV0ezNnbQxvsd1huPF_1j9rMbpAuYueuoGNxDc0_NkVyl17Od3nvyvICfqP1as9TOhmO5OUWtSqt9CwtQIW_2lfN9d8_WF8lidI2X7s-idHpPUVXkY-Q-oc9ZaaMKSkBn1ugH0gWG1jXQg4uncQD73R9GG-wbnWSTa9s_gUw6VwApQ1spEYbwL1y41Q2K7EyIuNpPS3_8i6PBMrJDFEg_QeArHl3qvZw5cS_rhCEX_nu7hQyS4cEDNSFfmUdaeBfEqB-HoGT7OvHrcMGXwnJHM4IGYZfN9ofMZZcG-ZBb-imzmlYlusTVO5og1O-yEZu8Gxj5skE3qEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برندگان مسابقه عکاسی میکروسکوپی نیکون ۲۰۲۶ معرفی شدند
🔬
🔹
رتبه نخست مسابقه «جهان کوچک نیکون» به ویدیویی از تپش مژک‌های ریوی یک کودک مبتلا به بیماری تنفسی نادر رسید؛ دیگر آثار برتر نیز تصاویری از لارو عروس دریایی، کرم لوله‌ای، تقسیم سلولی و حرکت میتوکندری‌ها را به نمایش گذاشتند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/691576" target="_blank">📅 00:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7ieKk6qDO_IV9E3QM5QQ5Vy-L2bNR0ub5J3455LPQbuxa9amzzceQmFgpNlP5UsN6VQgxVYt0FIJN064BsNQNKoxSWoXDjmsLoGk6Y-WMUT_NXimrxWuR9UWtugiOJHqhnAiKKt8tDWYEZJdndZh_nmAC4GK5H7PFIZCmXwTw5qpDfo3_hZXMamrsDK-vScgeCZr8MaVLDzD2f2vtBC8pD-ZOUhLI7YaB0lO6nYGx1Dzn9b2WYLbgvNP4xEn9DiSqa8_o0qzyxO_QnusoVAmLWFhWGMDoA6FZofZavUnyfltFsDocHNXYZMQaT-TFnH-orTB4SaX8ax_-ZbNeUBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8kOhv3LtihkvshZ9maRMSOXybh4Vvw3cANjGXw9G1ggg4kJTyus5xxAIPT1qtibYbuRMJNcTTvMDm97C3-MTjxsZIlZiWwQiZR2yhqxt7K88hlrDuA_yOPxhifsxbFjoXxehT3gBgv612Enpk9FD603Dmx8oxwGiGEGqmAxtLloO3xK_5f_UB5cMqIFJRSzKozHZdavyqNua-5ZWQGVuKpiG3M5AwjbCuLFeTJwgxVUP_bYvSoQbwKj2V_hbwMZb0VkDDb59LH14GbTdFvCpGNK8n7PO5xcDzyxQBJHaz1Yi451vZq9WFrPxFVO-kdcFHg98e35p_39vu0Gk1s-_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PtekfxAVAEPo98PZiO1RzaJQwcPOflmD3Rly-EHPGfPcMKANiVsmGz8TV-36lnEnlwi93eimwVFqG4i7xy6sLwEcsvo5as6BE2Zy4RmR9yrOpHvGCaK9l1d-KgMUctBng3FTJ09m4RCEHLtCk4axo43SLAKWYfJhGixUgOBLb2V_pcpXFx-p23o3WgRF-oBsMUGBaHosFXbzrVWE-tiSx_hS1y72PJ1DlC8TRYXpuoNacBUqtnpLJceKtra2oC6xPNpk3NGxwXmJz895VQKimrSERKm0q3t_esGSdGkBfhZHnW12I8RjW7FUAwcDsthZ7xyuua4zJvigWDRKfVppDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4_fnlutyXN4wI9dZFgkb6jHRV4VLuNISaAFuy8g2TiR8OuXxmT6B6A3Q1nrI_cnhQGbZZW7NsEm9OWGWe6OAaAy-0GZpBaLNKsYitUQKQCi-crry1hX-rQL9Ycj-DahyPKu_5jxBip2S0yjHmiRqSQvDKCvcprzZhsfgDIH9270wyMnrUrOnbIpl765IxYpH6WK8fmnnAPsEQNcind5rHgQ-3KXlXVRoA0EsoQacM7brhEtZOzeI4rmiYNe4SDrl-tCpfmkrywgFwg8D_2wNqOxV-WFKrj0WItEoTVtX8Bp3AhacwgK_2cTG15dlgiwDU88DC5Th7iCcPlqEkA20g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
خبرفوری/ انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز   روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفته اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش در منطقه جنوب شرق کشور، تحت شبکه یکپارچه پدافند هوایی کشور،…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/691572" target="_blank">📅 00:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرگزاری خبرآنلاین</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2064b90d.mp4?token=qmIcTAj_Cy2L7_M4cCUyjai5XkXyAhTZyuiQ400VB7MiuKYSFIwdzRZ3lEaAWSauFcc8dbjKqliZk8KvhQPfsFWHe8wNu-uJ2js7tlFBRGb_TuPL1ydPTX8WYI9OHJfuhM5Q39YeIZ97wTDunnOOeWyVxpLw_dheQf8Y1P9z2M-C9zL7ZC_frkqgp26DsODXjTwg_eBizxudXnsT2k0Mz8A1aHCAXtwNIELNrV4rHAeb2it81V3jGUC-mWVmY-pVVN6D58dPwsHJLnjf1UE3NHwb4jd1wzkKFAfZYASZXFKkq0noquQwQNZhMtTyoOUC2gAqqHCRgjL1tvJzH2UAGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2064b90d.mp4?token=qmIcTAj_Cy2L7_M4cCUyjai5XkXyAhTZyuiQ400VB7MiuKYSFIwdzRZ3lEaAWSauFcc8dbjKqliZk8KvhQPfsFWHe8wNu-uJ2js7tlFBRGb_TuPL1ydPTX8WYI9OHJfuhM5Q39YeIZ97wTDunnOOeWyVxpLw_dheQf8Y1P9z2M-C9zL7ZC_frkqgp26DsODXjTwg_eBizxudXnsT2k0Mz8A1aHCAXtwNIELNrV4rHAeb2it81V3jGUC-mWVmY-pVVN6D58dPwsHJLnjf1UE3NHwb4jd1wzkKFAfZYASZXFKkq0noquQwQNZhMtTyoOUC2gAqqHCRgjL1tvJzH2UAGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
رئیس صداوسیما از همکاری قوه قضائیه برای محکومیت یک پلتفرم خصوصی تشکر کرد!/ حکم علیه آپارات بی‌نظیر بود
پیمان جبلی در دیدار معاون قوه قضائیه:
▫️
با همکاری قابل تحسین بخش‌های مختلف قوه قضائیه توانستیم حکم قطعی محکومیت آپارات را بگیریم که حکمی بی نظیر و قابل استناد در مجامع بین المللی است که برای احیای حقوق بیت المال صادر شده است.
درباره این حکم بخوانید:
⬅️
رای علیه آپارات مبتنی بر مسیر درست حقوقی صادر نشده!
⬅️
صداوسیما می‌خواهد رقبای دیجیتال را حذف کند/ امروز آپارات، فردا کی؟
⬅️
انتقاد قاضی دیوان عدالت اداری به حکم دادگاه علیه آپارات
⬅️
بزرگترین ناقض کپی‌رایت، شاکی کپی‌رایت شده!
⬅️
صداوسیما به‌جای رقابت، رقیب را حذف می‌کند
@KhabarOnline_ir
|
khabaronline.ir</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/691571" target="_blank">📅 00:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvCp-UXKgApCoQw5yMe7KgpiFAkimEhvqvHE9lzshPgFI9hZ-IK1ke4nBBbbXEEe_RXXj6VqcXcXEXgEOsgZq_g6lP7JUqQN5fHbZ10Zh5RD3QQqNAaGmxTtonspqQ0J1bHAT1XD_mgQgg8FAi-hEaAeImdVKlHEabTZje-ZgHac9LGiwTdVf2oOoi76mhn7bkkqN5dON5_Fi4vCsO_1uRJP6rFsPrBMkyCS3T7Tmy0OMs1kT3Vs3CLVDmXe7ZSPlx7WXpb6J_KeBfxGUOHp0QZY6EOkReNknf2RSbVdfBKDw5CfIPC6D-OYa6EL5AR6RAMmiP2zEAwn2DoA7P7UAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/akhbarefori/691570" target="_blank">📅 00:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/addd96b83e.mp4?token=eG1db3-YLu_7W3nbvC0DclEvSPGgoEO_rE0bZ2mZRztfl9BESgTWu5jq8QZZjdp0LRWR7c9iC09siFFuN_bGQe6YSkfcs2AVBm-4HjPKmz_G4nyMI0LSr_i4JHe9VTVhY4jL6iKvQUbSNJTAO08Mjg81jqWP7YaUBSzVGyyxFA309L3BNCDSXk8ddnu0gkNIs5DzudIMlKDdt6b9YTmpJg5sE7xNbEMuBpCkHWivUIqNmeHMypxrO9Y4tmwPEGLialkNQkImUaLFOQj-ZbOLQabogc8L-2yv2vn44Vgrro6vkMJVoxnpsG7AFzS_qK-WIOsO0m9NvwDR-5TMAgvmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/addd96b83e.mp4?token=eG1db3-YLu_7W3nbvC0DclEvSPGgoEO_rE0bZ2mZRztfl9BESgTWu5jq8QZZjdp0LRWR7c9iC09siFFuN_bGQe6YSkfcs2AVBm-4HjPKmz_G4nyMI0LSr_i4JHe9VTVhY4jL6iKvQUbSNJTAO08Mjg81jqWP7YaUBSzVGyyxFA309L3BNCDSXk8ddnu0gkNIs5DzudIMlKDdt6b9YTmpJg5sE7xNbEMuBpCkHWivUIqNmeHMypxrO9Y4tmwPEGLialkNQkImUaLFOQj-ZbOLQabogc8L-2yv2vn44Vgrro6vkMJVoxnpsG7AFzS_qK-WIOsO0m9NvwDR-5TMAgvmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعترافات بهداشتی که هر کسی باید از آن‌ها اطلاع داشته باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/691569" target="_blank">📅 23:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پلمب مرکز زبان وابسته به سفارت فرانسه در تهران  قوه قضاییه:
🔹
مرکز زبان وابسته به سفارت فرانسه در تهران به دلیل فعالیت بدون مجوزهای لازم و پس از چند اخطار قبلی، با دستور قضایی پلمب شده است.
🔹
اتهاماتی درباره استفاده از آموزش زبان در پروژه‌های مرتبط با امنیت…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/691568" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5344568a53.mp4?token=JjwPxqkl59rCXV05Q8izyLD2sM9JFPVhxd7lDfeRN67_34QaeEBTnHfW3W6RMt84YH9qYi_U82l4IRp3i7pd677bITOl4A0_Tgqj1fgIkNuhIGpTzGjNzoFiVXiSzb3wD8p75bgFw0OQ6-CtLUf6X2HKr3lPWjOVXrIy6PQT1OyesXWz1uVIPDL8mXjz_DidG6aYMYb5bZZdBWXaUgT0oK7fdH_keQKaJlz6rjb0I-ivKlsGvEZuf-e8RiSUmop9QgUib1HjBjV8FqpY-nuda4IdcedqhkNPaw9c4_DpfeDVRe5jzQ1zFIKhVm9z1oMONP8FdpezBaz9CZuFr6dJ4WlzIsdHWyXXUJpePjAE4snVWnIubVRZS0pHrZU7t1rjf2g1EovXeXbugPymw416AvZ7QN4kaqw08RrmMaOvkCKeGnuuN_lo9jNGsScBOWJepA6J8L5Fnj9uJq8qSWCfFzqS4KbPlLp_UKmXWZ8yLY7r2Rssdy73iChShXf_oem15zMH5SEVMg_5gd9wEZT6s3_12ZHCuwCR7NTBNFr3gQ6UJ8F7dJ93xR2-7nDxp9wI6Ouiwp6Hw419dmU5VLzM9S8niQtQvOBR0z7vcyAz8LhcBynbV943a1Xw7ossPZ_pxvBxwI9MvOdYNnecgGke3OZtaO7AVrksax1NUNCccSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5344568a53.mp4?token=JjwPxqkl59rCXV05Q8izyLD2sM9JFPVhxd7lDfeRN67_34QaeEBTnHfW3W6RMt84YH9qYi_U82l4IRp3i7pd677bITOl4A0_Tgqj1fgIkNuhIGpTzGjNzoFiVXiSzb3wD8p75bgFw0OQ6-CtLUf6X2HKr3lPWjOVXrIy6PQT1OyesXWz1uVIPDL8mXjz_DidG6aYMYb5bZZdBWXaUgT0oK7fdH_keQKaJlz6rjb0I-ivKlsGvEZuf-e8RiSUmop9QgUib1HjBjV8FqpY-nuda4IdcedqhkNPaw9c4_DpfeDVRe5jzQ1zFIKhVm9z1oMONP8FdpezBaz9CZuFr6dJ4WlzIsdHWyXXUJpePjAE4snVWnIubVRZS0pHrZU7t1rjf2g1EovXeXbugPymw416AvZ7QN4kaqw08RrmMaOvkCKeGnuuN_lo9jNGsScBOWJepA6J8L5Fnj9uJq8qSWCfFzqS4KbPlLp_UKmXWZ8yLY7r2Rssdy73iChShXf_oem15zMH5SEVMg_5gd9wEZT6s3_12ZHCuwCR7NTBNFr3gQ6UJ8F7dJ93xR2-7nDxp9wI6Ouiwp6Hw419dmU5VLzM9S8niQtQvOBR0z7vcyAz8LhcBynbV943a1Xw7ossPZ_pxvBxwI9MvOdYNnecgGke3OZtaO7AVrksax1NUNCccSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قزوین؛ میزبان یک پروژه راهبردی ملی
🔹
طرح دانش‌بنیان احداث کارخانه ۷۵ هزار تنی آب اکسیژنه با پیشرفت ۵۰ درصدی و بیش از ۶۰ میلیون دلار سرمایه‌گذاری بخش خصوصی در قزوین در حال اجراست.
🔹
با تکمیل این پروژه، قزوین میزبان بزرگ‌ترین ظرفیت تولید آب اکسیژنه کشور خواهد شد؛ طرحی با ظرفیت اشتغال بیش از ۲ هزار نفر که گامی مهم در کاهش واردات و توسعه صادرات است.
🔹
حمایت از تکمیل این پروژه، یعنی حمایت از سرمایه‌گذاری، اشتغال و توسعه صنعتی قزوین؛ یک ظرفیت استانی با اثرگذاری ملی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/691567" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyiDAQ7kIgj2x9j1EdgyE3k-15OWZtC-c0zDoqZNo1PogKGD4jQ74ZwRjET4g-zPJGXc_KV4-wghTMj1Lc0PM2H19kELF2QHYT8_70vNua_tcGqKU1IK4nLhhHchd1ggBmP4UI9ozQyjXQDo1ws5n_aorz0kWrBxRkfsRigpiWPOlKiLIKzB76_Dyu58RYFy99EreBSsaB83iKfdxkS3uYofLgxVni7Bu5J-sT_o_CibVH9qfGs4f3gnUUjfauwg1-vGuGq06uDbeIwucV79vSQjSRfxLoLVNz05OgyBKCJxRpjZjQOHgRJdyxIZKpxfOcUP_idx51Fblg06Eh8agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
احمد ایراندوست (بازیگر) از بازگشت شادمهر عقیلی به ایران در آبان امسال خبر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/691566" target="_blank">📅 23:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067fa96a68.mp4?token=dCR0gkqHz1Nule7zxoRm3yzQ11sMBL6pXjPqG6dxvN41MoW9cOucik9_jrYK2U4ha3amSFMkjlNm7dOnhSn28wApnd6kTHUEGAZ_ZNpEZjTTlHXMAV0GlqtEdcf5aSjnAF9RhNCOZAexgcNIG0HPp0o5S3XCq6nQw3mDdjmLbmpI83gcWm2Bec0p8MtMGnVL6KoLg0lQFuG-SG9TgdRVg_LjUZlJzfOZ89vEhWdciNwSX1w8vtpUpQVoMtq1A_Pylc92q98H1xemqlr0L46TeAsefr5JDCt_Cdyzes1E6HhQy_UdlBtw4e4nMuY8Nx8Wmagonxp7TvOb1Pq67ZJBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067fa96a68.mp4?token=dCR0gkqHz1Nule7zxoRm3yzQ11sMBL6pXjPqG6dxvN41MoW9cOucik9_jrYK2U4ha3amSFMkjlNm7dOnhSn28wApnd6kTHUEGAZ_ZNpEZjTTlHXMAV0GlqtEdcf5aSjnAF9RhNCOZAexgcNIG0HPp0o5S3XCq6nQw3mDdjmLbmpI83gcWm2Bec0p8MtMGnVL6KoLg0lQFuG-SG9TgdRVg_LjUZlJzfOZ89vEhWdciNwSX1w8vtpUpQVoMtq1A_Pylc92q98H1xemqlr0L46TeAsefr5JDCt_Cdyzes1E6HhQy_UdlBtw4e4nMuY8Nx8Wmagonxp7TvOb1Pq67ZJBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: آقای قالیباف تمایل به پذیرش مسئولیت مذاکره نداشت اما با اصرار پزشکیان قبول کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/691565" target="_blank">📅 23:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای علی قلهکی فعال رسانه: آمریکا اصرار دارد ایران باید تا ۴۵ روز آینده وارد مذاکره شده و همه موارد از جمله هسته‌ای را توافق کرده و امضا کند؛ تنها امتیازاتی که آمریکا می‌خواهد بدهد «رفع محاصره» و «آغاز نکردن جنگ جدید با خسارات زیرساختی بالا» است. باید دید ایران از مواضع خود عقب‌نشینی می‌کند یا نه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/691564" target="_blank">📅 23:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
آمریکا رسماً از شورای حقوق بشر سازمان ملل خارج شد
🔹
وزارت خارجه آمریکا این شورا را متهم کرده که به ترویج آنچه «ادبیات ضد آمریکایی» خوانده می‌شود، می‌پردازد و در برابر رژیم‌هایی که به سرکوب مردم متهم هستند، رویکردی مماشات‌گرانه دارد.
🔹
این تصمیم آمریکا یک…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/691563" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
آکسیوس به نقل از یک منبع آگاه: ترامپ در گفت‌وگوی تلفنی امروز بارها از زلنسکی خواسته که حمله به پالایشگاه‌های نفت روسیه را متوقف کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/691562" target="_blank">📅 23:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0717956bcd.mp4?token=qFCDjufvaB84ISxE7Nh1weWGERC5zFmQKVOxf0mCyxFT-gQvDYuQrGutMnE-9qKw4wVQ-4mWmobeXLYdGvLtEzmsNy6cF4BskWCb2JbtG4jq8d7epD0Njyr2stRpEmUTVS6Ht0BF8cA8MttAkeljiRkbULVQSMMWxyReAhuu1xboiMJDuDCa5hkeIbDKCu_zgk3yfTfHLudGuYgo2QjSEY5XSTMIpTA9uFLD_1Po1aK3iFhg0sQprjbd6T7JMbvO_VWoikAALQwBopckryVqQwSp8g3Ptz-E3JSt6ypzp0i8OL2JzQaETHpKZCNm320LP-KPuyjlILZ8XM5iNOWq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0717956bcd.mp4?token=qFCDjufvaB84ISxE7Nh1weWGERC5zFmQKVOxf0mCyxFT-gQvDYuQrGutMnE-9qKw4wVQ-4mWmobeXLYdGvLtEzmsNy6cF4BskWCb2JbtG4jq8d7epD0Njyr2stRpEmUTVS6Ht0BF8cA8MttAkeljiRkbULVQSMMWxyReAhuu1xboiMJDuDCa5hkeIbDKCu_zgk3yfTfHLudGuYgo2QjSEY5XSTMIpTA9uFLD_1Po1aK3iFhg0sQprjbd6T7JMbvO_VWoikAALQwBopckryVqQwSp8g3Ptz-E3JSt6ypzp0i8OL2JzQaETHpKZCNm320LP-KPuyjlILZ8XM5iNOWq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انتشار اولین تصاویر از اتوبوس‌های آسیب‌دیده حمل و نقل عمومی در حمله نظامی آمریکا به کشتی ایرانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/691561" target="_blank">📅 23:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
کاظمی: هیچ مدیری در هنگام ثبت‌نام حق دریافت پول از اولیا را ندارد  وزیر آموزش و پرورش:
🔹
در یک پروسه ۷ ساله  تمام کتاب‌های درسی را تغییر می‌دهیم/ نظام آموزشی را مهارت محور خواهیم کرد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/691560" target="_blank">📅 23:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPi-vH7AIc_bo_xUiTzTQMs5T_YvVMlXK0Q_hQYy-xzDWGTiDjSvm5J5EUcym3EgjCE1N7RvMRkGYuZF4anbJqZgomAB4bXxBUrS-6N-NYd7AOtrjVMfQ5cKdY4E43fHM3rR8urZKYIHoiZ-mlstEHZkw5ELF7Frqhg-KfD1Bt7HTTJzcg4hQZ6_o8oKMYdWRqXEPh1DfIBhrXQE6k9gIjru_7UwpcECuPFPpBG405LSuOcom9Z2h8A7xgsQIYBaK8tdvBYGZoULXMoCpQdhbfHnvGBLi8b-yoC-mBpImrPEs70kHDh5O7uZOal0vV57GL0_4s4lR384NaFIR9sfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۴۵ هزار مترمربع درخواست مشارکت در هشتمین نمایشگاه صادراتی ایران
هشتمین نمایشگاه توانمندی‌های صادراتی ایران  با استقبال شرکت‌ها وارد مرحله اجرایی شد.
این رویداد با مجوز سازمان توسعه تجارت ایران،
۶ تا ۱۰ آذر ۱۴۰۵
در نمایشگاه بین‌المللی تهران و به همت شرکت نبراس برگزار می‌شود.
فرآیند جانمایی شرکت‌ها و طراحی فضاهای تخصصی در حوزه‌هایی همچون نفت و گاز، فولاد و معدن، صنایع غذایی، انرژی، خودرو و تجهیزات صنعتی در حال انجام است.
تمرکز نمایشگاه بر
توسعه صادرات، مذاکرات B2B و شناسایی بازارهای هدف
است و دعوت از
بیش از ۱۵۰۰ تاجر و هیأت تجاری خارجی
نیز آغاز شده است
جام دهند .
جهت کسب اطلاعات بیشتر و ثبت نام با ستاد برگزاری نمایشگاه در ارتباط باشید
02192002799
09127989492
https://iranexportfair.com/</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/691559" target="_blank">📅 23:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLqMxxXara4d-rjfOLy54rkDMmFH3IwJzoV9rDrs9b6t024u6kR76Y__X4LYdfg32OflaTDMXaXliehccNIj_m2ybZNz37IxRTXaJqTrs-X6oMfQV_ZcRUtG_QJ-htZnP2nAmQB8NIRtLyy-IR9hFZNij9k0OiGn6cUWms2tKCfydmmp3CIQvKqWtWnA2YInifMQEpqMKPGV8Tk2GW9Euuc9NKJIW5ezGjr6s98xfGNMWosY1vfKEnoBLtJkKAwIQAnivJiwF50OjsYMgHKep3wzRjq085tUAl3kn10Flz7JqjdAhDmQJL79f2q0zTkfSArkQZhP52CXZ1XYLbTdUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
هیتر برقی ریموت‌دار ۸۰۰ وات HANDY HEATER
کوچک، کم‌جا و مناسب گرم‌کردن اتاق‌های کوچک، محل کار، آشپزخانه و سرویس بهداشتی.
✅
توان ۸۰۰ وات توربو
✅
تنظیم دما از ۱۵ تا ۳۲ درجه
✅
ریموت کنترل + صفحه‌نمایش دیجیتال
✅
تایمر و خاموشی خودکار
✅
دو حالت سرعت فن
✅
قابلیت نصب روی دیوار
✅
ابعاد ۱۳×۱۳ سانتی‌متر
🔴
قیمت: ۲,۲۵۰,۰۰۰ تومان
✅
پرداخت درب منزل
🔄
ضمانت تعویض ۳ روزه کالا
خرید تلفنی
👇
https://memarket24.ir/product/fast/52904/180124/</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/691558" target="_blank">📅 23:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af25ea306.mp4?token=n_ovuZRvDfYqdyS81b4_svoXLes0mIlaBxAZMHIwnmHdLt7PeQqHfW_bz_DqPtxuVr7iIZaoxWM-pklWi20KHFRaVn5XsGgYEa8CjnZkN8WdwZM4SI-2s5T4BXbYgnb4-jd2s2iRPd8RZoz4zWWCZ_WvKLsiNx3WmlajknHQSqzLtuQjY-m_5Hs9Or7wcnGqkpi-FAvy0vaEFG2vUMA1d7mm1jDxEXDuMpc4bcquIStz50dL4l6miXYSzBC0FD-fcaZStJsa-mePrmrJqCUU7bBxfkc4Iz-UdDFrZy5IKCuIHpHqoKvfyEzwMc4_tee7MDFcAwxGcobOE6pANh2qZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af25ea306.mp4?token=n_ovuZRvDfYqdyS81b4_svoXLes0mIlaBxAZMHIwnmHdLt7PeQqHfW_bz_DqPtxuVr7iIZaoxWM-pklWi20KHFRaVn5XsGgYEa8CjnZkN8WdwZM4SI-2s5T4BXbYgnb4-jd2s2iRPd8RZoz4zWWCZ_WvKLsiNx3WmlajknHQSqzLtuQjY-m_5Hs9Or7wcnGqkpi-FAvy0vaEFG2vUMA1d7mm1jDxEXDuMpc4bcquIStz50dL4l6miXYSzBC0FD-fcaZStJsa-mePrmrJqCUU7bBxfkc4Iz-UdDFrZy5IKCuIHpHqoKvfyEzwMc4_tee7MDFcAwxGcobOE6pANh2qZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ذهن پیش از آنکه فرصت درآمدزایی را ببیند، آن را از بین می‌برد؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/691557" target="_blank">📅 23:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691554">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه اول</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/691554" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌ گذر از دجال
جلسه‌ اول:
تفسیر دعای عهد
🔹
دجال با فریب‌های بزرگ، پیشگویی‌های دقیق ظاهر می‌شود به گونه‌ای که حتی ممکن است مؤمنان باسابقه نیز به او بگروند.
🔹
راهکار اساسی برای مصونیت از فتنه‌های آخرالزمان، قرار گرفتن در دژ محکم بیعت با امام زمان (عج) است.
🔹
طبق دستور امام صادق(ع)، مداومت بر قرائت دعای عهد در چهل صبح، انسان را از یاران امام عصر قرار می‌دهد.
🔹
پیش از هر درخواستی از خداوند، یادآوری عظمت و صفات الهی ذهن را به مرحله‌ی پذیرش و گشایش می‌رساند.
🔹
در دعای عهد، عهد سه‌گانه‌، عهد(پیمان قلبی)، عقد(گره رسمی و محکم) و بیعت(تعهد عملی به امام زمان که بر گردن انسان است)، هر صبح تجدید می‌شود تا راه نفوذ دجال بسته شود.
🔹
دعای عهد یک قرارداد، پیمان و بیعت رسمی و دوطرفه با حضرت صاحب‌الزمان (عج) در عصر آخرالزمان است که به مؤمن کمک می‌کند تا سبک زندگی و مسیر سیر و سلوک خود را با جبهه حق تنظیم کند.
🔹
ناباوران ظهور را دور می‌بینند اما مؤمنان باید همواره آن را بسیار نزدیک حس کنند واین احساس نزدیکی، ایمان ایشان را تقویت کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/691554" target="_blank">📅 23:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شایعه خبر لغو پروازهای ایران و عراق از روز سه‌شنبه تکذیب شد
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری:
🔹
تاکنون هیچ اعلام رسمی از سوی دولت عراق، وزارت حمل‌ونقل یا مراجع هوانوردی این کشور درباره توقف کامل پروازهای میان ایران و عراق منتشر نشده است./ مهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/691553" target="_blank">📅 23:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: مدارس قطعاً حضوری خواهد بود؛ استانداران در شرایط خاص می‌توانند به‌صورت نقطه‌ای درباره نحوه فعالیت مدارس تصمیم‌گیری کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/691552" target="_blank">📅 22:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691551">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e18c13209d.mp4?token=KKhmRLNQzFrgQv96rG1dlY6dpVeb_Z_VEDilNGtG3zer-y3MWR0Sa7gv2aVGSQ2Wtn40tzMjuVlOJ6wl2lzqJ9VKFMP2PJem30Mh4vbEUaLUuDvcNuWkW_2SP_4eKnz3O-Kacw78AEDwU7z8yhIB1AMWDn2UXUOUin9BLw55eTPZc-bJcBFK08L-hRsjWEOyQRPKn0TVaw9KXWVUI-ns6d_bZh9zC7DNg2gCQuM56w6s3q1d2IGaU57Jpu5yziD8miMI9zJwcERs4nnDbsm_gs3NvfnbYxZOO9fCTey2QsLCKTG2BMQ40aYMxs-o5t-bzoyMLBVH999hyvACbbHPgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e18c13209d.mp4?token=KKhmRLNQzFrgQv96rG1dlY6dpVeb_Z_VEDilNGtG3zer-y3MWR0Sa7gv2aVGSQ2Wtn40tzMjuVlOJ6wl2lzqJ9VKFMP2PJem30Mh4vbEUaLUuDvcNuWkW_2SP_4eKnz3O-Kacw78AEDwU7z8yhIB1AMWDn2UXUOUin9BLw55eTPZc-bJcBFK08L-hRsjWEOyQRPKn0TVaw9KXWVUI-ns6d_bZh9zC7DNg2gCQuM56w6s3q1d2IGaU57Jpu5yziD8miMI9zJwcERs4nnDbsm_gs3NvfnbYxZOO9fCTey2QsLCKTG2BMQ40aYMxs-o5t-bzoyMLBVH999hyvACbbHPgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر چیزی که می‌بینید، واقعی نیست؛ هوش مصنوعی آن‌قدر پیشرفت کرده که تشخیص واقعیت از فیک سخت شده. حواستون باشه گول نخورید!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/691551" target="_blank">📅 22:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691550">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-4dpGwUUbOxC34-kl0pXF9BUoVhmAr_RSIaP3l32upMtUr0asEm1ie2YO72vtE5BCSc5bSdrt3UWnpouZN0iGaHI301sT4Ov70EDE_AEduj5OvW3JG7DyEbXvGiOadoFrDohmq_lzN8a3dutb9dPjoaEErvSo8vxaEX2UfUypkpvnDy6BWeijOrkZod29oZkA5CJxPdV-4ALIEjpi_bONYrVhDo1xBwUvvjbg-xYcXYViks6lWa7u5c3az8k_W3HI0E2whhUzUbhtFDy9xFLQnOMNpBDH06n3uEmVFHex7ztkd2fM7I_3ox_MWIX0P_q3Qfu_eaxFUIsjHChOFgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پل بیات؛ نمادی از اراده‌ و عزم متخصصان ایرانی
‌
🔹
وقتی دشمن پل بیات در آزادراه تبریز - زنجان را هدف قرار داد، گمان می‌کرد شریان حیاتی این منطقه را قطع کرده است؛ غافل از آن‌که راهداری، با بن‌بست بیگانه است.
‌
🔹
امروز، با گذشت کمتر از پنج ماه این سازه به همت غیرتمندانه‌ مهندسان ایرانی و راهداران خستگی‌ناپذیر، دوباره زیر بارِ ترافیک رفته است، تا نمادی از رویش «امید» در دل بحران باشد.
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/691550" target="_blank">📅 22:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691549">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_aVg28SC6drVm588A_60d0itJ5ZoALkiI7PqDsi_K_R66-PZMODGWeC_stpXFK2-i_IiCWAaJ0mk81naPJ-JMeanWIxJieEEqOGv48pT0LAh19ppSDXBk3tO11Q17hMu2FmFETTwAjJJBdwS3XVJKRBmwdApk_b6-Ch60eEJsQFqdwlGK0dw3h9qV-q20o3SsqedSuBfInf8wd21PZoQViL1lEL8LLAB5uf_WCYYGxlhmsp08EaDouEFUJTXxQ-clg93lFmqPg-GRzaSiOrD4J3GBAjUYzrw2LRhmK-7w2mCt3ShaVSX4lhTqe7jAobum9g8VRwY_RuE8yuLnHl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مدل‌های ماهواره‌ای از ورود موج گرما در ده روز آینده به کشور خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/691549" target="_blank">📅 22:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691548">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEN7PNN6IE8QppOQNS0Ot55xZC8UgGcb-q763bkp1g2MtEANdKphB5_La4CxTb_-KqG3Q4WrN3qrFl0VPTaF-WOJyPkYd80_tc0YbP1hDRnCeUt28wCzfObqWnZGVjWXdGlt6z0Ef7Jq1chc6KrvQUgVV9TY9k_1z05IJjXA_3XKjVuXi0XqOilPba6PVq20JcH1qE2ZPCj5zvMWNiYjOn4TqGDT0sMgPGkgZ4S8ySt386jPa-uGpJnll4bTk1pCF7jAeqZSZefgR-bJCcTgyMGEZHAtOA4rvD6XJSaTEYDW8qCsmzTrwVMy7UjhC3B0yGq7xU4a_HAK3tW1gP32YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور سفر پزشکیان و سخنرانی او در سازمان ملل می‌تواند تاثیر عمیق‌تری بر روند تحولات جنگ داشته باشد؟ پاسخ در نوع صحبت‌ها و پیوست رسانه‌ای است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/691548" target="_blank">📅 22:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691547">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مدرن‌ترین خوابگاه دانشجویی دخترانه کشور با حضور تولیت آستان قدس رضوی افتتاح شد
🔹
سرای نجمه خاتون (س)، مدرن‌ترین خوابگاه دانشجویی کشور، در دانشگاه علوم پزشکی مشهد با تأمین مالی یک هزار و ۷۸۰ میلیارد ریال، از محل نذورات مردمی احداث شد و با حضور تولیت آستان قدس رضوی به بهره‌برداری رسید.
این خوابگاه دانشجویی به مساحت ۱.۸ هکتار و مجموع زیربنای بیش از ۸۲۶۱ متر شامل ۱۰۶ واحد اقامتی ویژه ۴۲۴ دانشجوی علوم پزشکی در محل این دانشگاه، به بهره‌برداری رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/691547" target="_blank">📅 22:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691546">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
وزیر آموزش‌وپرورش: مدارس قطعاً حضوری خواهد بود؛ استانداران در شرایط خاص می‌توانند به‌صورت نقطه‌ای درباره نحوه فعالیت مدارس تصمیم‌گیری کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/691546" target="_blank">📅 22:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691545">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc6967506.mp4?token=LQaRlJtx79InEekYLbLxNyzuloZhbknSeWsjw5xT4CPhzOdL8BfuKQZHWIYmGbqP9lrFPhWBBHPW5f84uZ4TgJ5hA43LE88BIX7_XLdl3_ft699FqDE9rWL-SkPq5iXIeo5KLTN5TzsEa8RCsCA9BKOGfSNPg92tqBR-9zZR-P3NvSCJREx7_EXSVqGtGgfKlsb7HppEpN1LWPAJKCxEtZRL0ijilqmXihwxJGB2cl0GFyjbibn45wRV80gz3td7uvv3G8aeCd3PW1PAvLkzOvQMz4xIxKF9BEGrtVX85nRqhlfFEWWPmlNfv6L6bWSSI0JdRSa-Z5nKUDUtvM2tEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc6967506.mp4?token=LQaRlJtx79InEekYLbLxNyzuloZhbknSeWsjw5xT4CPhzOdL8BfuKQZHWIYmGbqP9lrFPhWBBHPW5f84uZ4TgJ5hA43LE88BIX7_XLdl3_ft699FqDE9rWL-SkPq5iXIeo5KLTN5TzsEa8RCsCA9BKOGfSNPg92tqBR-9zZR-P3NvSCJREx7_EXSVqGtGgfKlsb7HppEpN1LWPAJKCxEtZRL0ijilqmXihwxJGB2cl0GFyjbibn45wRV80gz3td7uvv3G8aeCd3PW1PAvLkzOvQMz4xIxKF9BEGrtVX85nRqhlfFEWWPmlNfv6L6bWSSI0JdRSa-Z5nKUDUtvM2tEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرید گردنبند طلا ۴۷۰ میلیونی برای پت خونگی!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691545" target="_blank">📅 22:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691542">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
،
شنود
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/691542" target="_blank">📅 22:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691541">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jo_jsihNDsWBBcyzOQ9b7eetO8rijgh2nSxyqZuxTRnzQZS-zv17dfFreFR8Orxsm3v95-lbWh1wwH2Lnh6O0-ENWhHvoUTLxVF-ZsKYHoFTNwy5gnt2GKKPv4KD0w5U7meEAdRFWHuWMrFjDcJZVaUJ2LUWr_Ks0sanULOqFtT22WeI52yfQKe9dXU1IJtCC78pzx7ed8VikxCt5W_x3F_rHv7iRkmCYyJKzUwVcj9Bi_GxxC6D8cW_IlquAXNHaoqlKnaKv2PQYGGfnb2mK99JO2iKoJaXYcRHaup3sewXKiN5K4V4J7ag2h7-y4yY4f370cIPylczMvgsxQLy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خانه‌ای با معماری جالب و عجیب در سانفرانسیسکو، کالیفرنیا
🏠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/691541" target="_blank">📅 22:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691540">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8LOnS39Iu0R-ALjfHeI9kwocPlTyfiBQ_6haq-BjsfYZ7R0gvA8bxuaChD5UxOY6qwbsLoeVGcvrlWGCaFSv1u0F8xjHk5xtMSHEP5Yro9XT_hc5t5ESa3xnsqQyBfF0TONexZ8-dyRErgp8sNc2e7V6cHh8CScvE4XowKMuhCU-kt6IoRZOMWlauoHeB4MVU6OF3mEm_nQm2xT6kds3BX6stqO9LMzr_qA9E5pANhlKp2GWSFRhjrKIJ8GltmvIiUSxN4DWMDUiAj7irj72fk9Yo60dw7TfjSfoxUjRypyByVdlY6xEnY4lTmLmieeK1mfZ8wKZsbzjuZNJRSWrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنگ‌تمام صندوق سرمایه گذاری زیست فناوری برای دانش‌بنیان‌ها/ روایتی از همراهی تا اوج
صندوق حمایت از سرمایه گذاری زیست فناوری ، وابسته به معاونت علمی، فناوری و اقتصاد دانش‌بنیان ریاست‌جمهوری، با ارائه کامل‌ترین زنجیره خدمات مالی و اعتباری از سرمایه‌گذاری خطرپذیر و اعطای تسهیلات تا صدور ضمانت‌نامه به پناهگاهی مطمئن برای شرکت‌های فناور تبدیل شده است.
رسالت بی‌بدیل این صندوق در ایثار مالی و حمایت خالصانه تجلی یافته است؛ مجموعه‌ای که با پذیرش ریسک طرح‌های نوآورانه، شرکت‌ها را به مرحله سوددهی و تجاری‌سازی می‌رساند و سپس بدون چشم‌داشت، سهم‌خواهی یا طلب سود، کنار می‌کشد تا تمامی دستاوردها و منافع تجاری در اختیار خود فناوران قرار گیرد.
🌐
درگاه ارتباطی:
www.biotechfund.ir</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/691540" target="_blank">📅 22:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691539">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPdQ3TotKqJSBOOiFbZ0cRU9wjojvtQLb4Mza5OGsV6cHtO7smPKBXYfANBrnL-Xtp1dUPL_8Aam7X3XbH-VlvslVQFbncXepRumdjE-hZGNDVzpLKjNrnfLQ8MbW2WmuW9Q_gKPpDvFfR47XnFDrTHSbmiQWhVaonuijQHLYymPP0AE4VeiI4J2DHOSVDFDWKzZLDhEuJxI7VKFqSy1OG0dOaihfvqwoyxV_8aexFG7uU7CFr9NA8drfKw1EVozUAaVWK2UekxOOLOr73oPtY3x5q8dWSP-_zxQYL2PM2C4JAPyfglShg380CNtNpbW5QsQLyOVhXUHZkAFMl3vGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بیمه تکمیلی رو قسطی می‌خواهی؟ بازارش داره!
سلامتی خانواده خط قرمز همه‌مونه، اما هزینه‌های درمانیِ پیش‌بینی‌نشده همیشه آدم رو نگران می‌کنه…
خیلی‌ها فکر می‌کنن خرید بیمه تکمیلی یعنی
پرداخت یکجای هزینه‌ سنگین
؛ اما من رفتم تو سایت
بیمه‌بازار
:
✅
شرایط شرکت‌های مختلف رو
مقایسه
کردم
✅
به راحتی، حق بیمه رو
قسطی
پرداخت کردم
✅
و یک
سپر امن
برای هزینه‌های درمانی خانواده درست کردم
👈
برای مقایسه و خرید قسطی بیمه تکمیلی کلیک کنید
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/691539" target="_blank">📅 22:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691536">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
برخی منابع خبری غیررسمی با استناد به داده‌های فلایت‌رادار ادعا می‌کنند عباس عراقچی به قطر رفته است/انتخاب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/691536" target="_blank">📅 21:36 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691535">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: آمریکا اعلام کرده خواهان توافق است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/691535" target="_blank">📅 21:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691534">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd23357f53.mp4?token=eN7c-mC-FYsC-RBPFwng3_edl1vjFRUIbNakKyY7_kPEoWcIFQoIoavYqssQXQ9yMsHcau9Xz1LERmEClEqsckLXsmziqoIp68U5XV-W6siP2nNin9rJy1m6yaPVA8ZrVuopLvSje9BcyBi9SoI3ZHLXFBNi-uHpMKHBQ5lnLT3BSB1XOC4OO5sA3T2TOEAqr6LmpEWFqDiyfQYGpfjZybRSyStQQqAYaG8Kg1sqnCamqVGDrRmLpVjVLGfsc0RLdmjsxOzhjM1TqfbdKWgkNe-zntcdFmp-ssGREQuwG0lkiJprTXWkmMjoaSBLoEArTAzhgp6dqQGCuXuxw-nS3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd23357f53.mp4?token=eN7c-mC-FYsC-RBPFwng3_edl1vjFRUIbNakKyY7_kPEoWcIFQoIoavYqssQXQ9yMsHcau9Xz1LERmEClEqsckLXsmziqoIp68U5XV-W6siP2nNin9rJy1m6yaPVA8ZrVuopLvSje9BcyBi9SoI3ZHLXFBNi-uHpMKHBQ5lnLT3BSB1XOC4OO5sA3T2TOEAqr6LmpEWFqDiyfQYGpfjZybRSyStQQqAYaG8Kg1sqnCamqVGDrRmLpVjVLGfsc0RLdmjsxOzhjM1TqfbdKWgkNe-zntcdFmp-ssGREQuwG0lkiJprTXWkmMjoaSBLoEArTAzhgp6dqQGCuXuxw-nS3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاموفیلیا یکی از این علائم را دارد؟
/
پیش از مصرف کود یا سم، ابتدا علت را شناسایی کنید
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/691534" target="_blank">📅 21:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691533">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وزیر اقتصاد
:
ارائه کالابرگ با مبالغ جدید از ۱۵ مهر
آغاز میشود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/691533" target="_blank">📅 21:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691532">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYpG9Inhwe2N7jEbRra8atV0SymriqZfdE4xb5Tc45MKWyNb-ag0S5UTjFsYESb5DoizasfbT2-7q48RNj_R7SonzzGqBTgoTbknLQJxcpRoJ98GzBKpsSrJ9ZNF8LD5k6HyXpRM3No-BzMffD2t6DOODFTPPXqmrgxHNZV3umJMB_0LmhJchLatId_uMJ6tnDsQ9IDtO4eJZgzvSzjWp953F8WCCK4aqoTbYmox1H4CZvbDzAb-hgevdklhhLIuKXIC-va6Xu2k-kHapw4mHoufcIFMRpUhg6qSYct3nC8vvXiZMP_F_e7a8EgLJ3ujNNiGz1K9b_7ERZaTVB6jTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: آمریکا برخلاف ظاهرش آسیب‌پذیر و در معرض خطر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/691532" target="_blank">📅 21:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691531">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6d8yYvScGBt-0B_2MZ0H2EE1llKDCAiYacHYy7brLkDHfFtGc7Uk9Fpvn1pEXyHean_warY5UErlfzoMV_OE1wHf18zkluxGhF04R_EogY5BOGqjZ31rpYpFECfccdVrkKeXGZz84RyrGG06zlxnOp2psN8CsoxPmawud5gytTYM7VW9uMfK7DQ0J-DGDew7OKIBywl3ZaAiAjF9QMFMKCjm49F9jGx2GR_jy3-3fhYfdvCEnnQfIeWOG7wSg5BV5ao7WSowKlAvoeXnOBHALeJvyYJSesuGBU6WH-nT1rF279Y2C5iZKAr1oM2pBgmJpWrLXjvFJYevO1t76VyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با این ۵۰ دستور آماده، سریع‌تر ایده‌هات رو از چت‌جی‌پی‌تی بگیر #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/691531" target="_blank">📅 21:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691530">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9d1966b37.mp4?token=pn7kYybYepCeu0AsJyVOKQACnvgixP4I-RJB56CE8I3gC79D82B7xcH17IyajAK59qbZC42nlmP5Gqc3xQrMqbCM3822azDctruvBodYf4RMiOqP0WTLNbBmCzeuk_4Xxah3W7-K8jnmTlbW6ahk6vn1LdToBP6JshSG2fwhqeRoRaxnv8gwQ8WpGaDy6rSD1BP6YnYzdITNTgxv5W96JkaJtj78YHNz_ToHpE3fTwS9tKa-3PHKNT-RWeaC4l1oDyzi4R2r2zOM64ECWfLWjvPE8t_WCnC7SC12XCH2uDUds9sbs_GtJyINBt41N2m0rhzw0qd9e0PPiSB0Cz8_Zw8WfMo5oQkRA4o8Hx5YIEIFJTvgLhSB3kxOv-LUzUBEel_0NT7wa8h6nhGX7oZSR7Z6PwVElXq1aSAkTO0y97Ez9_4shlXZjje_2dT9x8KqkomoUyXH5iOppCCRGvLa6sO3FEp353M6r_EFEA2y8gPdAZZiwnwKVHW0QksDqnv-dGjfBl8JcAePvMjWbDiKaAfDzBtVItcnlUxm_I-9UzwehI-l-_c7cM5OMaPtqDMKXoz247paeFA24NsGn-LTHim71jvkJLFq369hDEF5rgRmAaGH4cR1urCYOFrMFp7_L3sSWm6hE22IYOuQ760SWlnttZu-5dGjflc1EnzB9c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9d1966b37.mp4?token=pn7kYybYepCeu0AsJyVOKQACnvgixP4I-RJB56CE8I3gC79D82B7xcH17IyajAK59qbZC42nlmP5Gqc3xQrMqbCM3822azDctruvBodYf4RMiOqP0WTLNbBmCzeuk_4Xxah3W7-K8jnmTlbW6ahk6vn1LdToBP6JshSG2fwhqeRoRaxnv8gwQ8WpGaDy6rSD1BP6YnYzdITNTgxv5W96JkaJtj78YHNz_ToHpE3fTwS9tKa-3PHKNT-RWeaC4l1oDyzi4R2r2zOM64ECWfLWjvPE8t_WCnC7SC12XCH2uDUds9sbs_GtJyINBt41N2m0rhzw0qd9e0PPiSB0Cz8_Zw8WfMo5oQkRA4o8Hx5YIEIFJTvgLhSB3kxOv-LUzUBEel_0NT7wa8h6nhGX7oZSR7Z6PwVElXq1aSAkTO0y97Ez9_4shlXZjje_2dT9x8KqkomoUyXH5iOppCCRGvLa6sO3FEp353M6r_EFEA2y8gPdAZZiwnwKVHW0QksDqnv-dGjfBl8JcAePvMjWbDiKaAfDzBtVItcnlUxm_I-9UzwehI-l-_c7cM5OMaPtqDMKXoz247paeFA24NsGn-LTHim71jvkJLFq369hDEF5rgRmAaGH4cR1urCYOFrMFp7_L3sSWm6hE22IYOuQ760SWlnttZu-5dGjflc1EnzB9c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁨ بیمه زندگی و سرمایه گذاری پروژه محور
یک‌ سرمایه گذاری کاملاً امن،
با ۴۰ درصد نرخ سود در سررسید
به پشتوانه و تضمین
#بیمه_البرز
معاف از مالیات  همراه با ارائه پوشش بیمه عمر
#بيمه_البرز_توانگر_و_ماندگار
#بالاترین_ظرفیت_مجاز_نگهداری_ریسک
⁩</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/691530" target="_blank">📅 21:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691529">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761a1bd315.mp4?token=nSa4aSVZZl8Yla7oBBvYJfGsefh3R7FE4bTX-qEZjm49QvG_uxh26SHwutD5LDlZ7G5w79TIyaCZ8vyairskpnKT91X5RXLf8Fnt5GnZNOxYLNUsNnUyqk7e6olpsXjMcTNXnepm2fkynZhWefuf2P0Jo-CvIoXq8QSoHpeJ1bpATqXInHvuat0cUp9pT7-CyjOrepEdHxR-u1FbGO0STxMHhuEe5R1wMDjaDUfFZl3ZT8iOHwbVRoWZzqcl7HTqYSR6tKcyzURTjZwfaco44HfJYRd-6xkJgNGpOFTB6hbpV_AGpHiQDwyUAhlQDP7qMdYX4vZEiXLpXeNkKgxSIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761a1bd315.mp4?token=nSa4aSVZZl8Yla7oBBvYJfGsefh3R7FE4bTX-qEZjm49QvG_uxh26SHwutD5LDlZ7G5w79TIyaCZ8vyairskpnKT91X5RXLf8Fnt5GnZNOxYLNUsNnUyqk7e6olpsXjMcTNXnepm2fkynZhWefuf2P0Jo-CvIoXq8QSoHpeJ1bpATqXInHvuat0cUp9pT7-CyjOrepEdHxR-u1FbGO0STxMHhuEe5R1wMDjaDUfFZl3ZT8iOHwbVRoWZzqcl7HTqYSR6tKcyzURTjZwfaco44HfJYRd-6xkJgNGpOFTB6hbpV_AGpHiQDwyUAhlQDP7qMdYX4vZEiXLpXeNkKgxSIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژه مادران و کودکان در رزمایش جانفدا به یاد شهدای میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/691529" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691528">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
رئیس شورای عالی سیاسی یمن: اعلام می‌کنم که نیروهای دشمن سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند
/
باب‌المندب به‌جز سعودی برای همه امن است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/691528" target="_blank">📅 20:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691527">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3423be4c7.mp4?token=ozj2xC2NwdSaMmGC-xklx3ZlF0rbgMvo_n6CmYI3ll1H2vRVBBlYUaRc1LDSo-2vwER5wRnCR0osX606X6nKztXDZP2yqD8snRVCAc7xPjyk89ElMMI1cGt0BlZ8sgdB0mAV4lJtojLzkXtLeamPg-2D72RFnLiEg3z81Dmg_T3kw2MRZvd2dpGqKONZpoTb6bN4oQcSGCAf-Vhrf2Z2DCSDsMBpf27DyqMxOD6LUJkRq-xCUYjN9kITFsr-OShP22TkMLHkLBycHUDMoDhYeG5o4Cf3bDlLSDUtJG97YVrG01Lr330F3Hgte50LtwkgvmvZ9utjSsmEMxNsrQoG5wWpiu5qyVa8gZVav5NfrWpMiwGYQb9ynRthxBiHNXj5mZXUoD-dqtBQKbce385sn4I6Gee7DaRrMO9jpt_FQeDeqAKdlsgnMcCueEC08oYUSMGGKqc5hvdg2W9APN8w3qIJvZZPK1fA8IYExUobHpWMfiOcdANqg6aJf0vGBGgdYWOBH0VEHa3p_hrv8TLEvzU065pD8Tz0MRolGt1vpXHHpK_GhPgOkXytjLIu9xwOXfEv47WCuh2Ma6R1_4Dc96BwR53_PTCHL5wIBV8pq-pTxHuIWVjkZvNnUnh41dpnvJFE7KP66P03IxlN5Ls0VDUsmZNG2vF7mnIUiK1WpDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3423be4c7.mp4?token=ozj2xC2NwdSaMmGC-xklx3ZlF0rbgMvo_n6CmYI3ll1H2vRVBBlYUaRc1LDSo-2vwER5wRnCR0osX606X6nKztXDZP2yqD8snRVCAc7xPjyk89ElMMI1cGt0BlZ8sgdB0mAV4lJtojLzkXtLeamPg-2D72RFnLiEg3z81Dmg_T3kw2MRZvd2dpGqKONZpoTb6bN4oQcSGCAf-Vhrf2Z2DCSDsMBpf27DyqMxOD6LUJkRq-xCUYjN9kITFsr-OShP22TkMLHkLBycHUDMoDhYeG5o4Cf3bDlLSDUtJG97YVrG01Lr330F3Hgte50LtwkgvmvZ9utjSsmEMxNsrQoG5wWpiu5qyVa8gZVav5NfrWpMiwGYQb9ynRthxBiHNXj5mZXUoD-dqtBQKbce385sn4I6Gee7DaRrMO9jpt_FQeDeqAKdlsgnMcCueEC08oYUSMGGKqc5hvdg2W9APN8w3qIJvZZPK1fA8IYExUobHpWMfiOcdANqg6aJf0vGBGgdYWOBH0VEHa3p_hrv8TLEvzU065pD8Tz0MRolGt1vpXHHpK_GhPgOkXytjLIu9xwOXfEv47WCuh2Ma6R1_4Dc96BwR53_PTCHL5wIBV8pq-pTxHuIWVjkZvNnUnh41dpnvJFE7KP66P03IxlN5Ls0VDUsmZNG2vF7mnIUiK1WpDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گیاه‌ها پژمرده می‌شن؟ با چند نکته ساده، گیاه آپارتمانی‌ات رو شاداب و سرحال نگه دار!
🪴
#ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/691527" target="_blank">📅 20:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691526">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرفوری
pinned «
‼️
خبرفوری/ انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز   روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفته اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش در منطقه جنوب شرق کشور، تحت شبکه یکپارچه پدافند هوایی کشور،…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/691526" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691525">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8Pn3mV005tFg97z5svSxN62oXEaqurHhXUCBiDtNgpaNy41s9MX-v62A1Qyt2K8QBW-IwrgxqboNU9c33HBOlCAQMu-ii74jwN86r2HwL1SkgF4J_wYQijv_SDyH2pmgzPQxDwPqIjrsxjdc0b-f6nuOiGMGOmrOHIj_ra1hOE5L4J_0mUVs6Z5e3XsP9F14l1iuos9_73M-jtRSDt4l2AilcPxNIFg9DdiqmfkvnVV5Ujrw-POYF7z7wlpfWr9p7KuZ8ENetElJM-TdSukqoblmtm2V6AIvo-JiVK1-BLqp6TO7aNeqEp706WDgS0zePe1JwRHGFmbHoHRjBjDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینها صندل‌های ۳۰۰۰ ساله توت‌عنخ‌آمون یازدهمین فرعون مصر هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/691525" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691524">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
خبرفوری/
انهدام یک فروند پهپاد شناسایی پیشرفته اوربیتر بر فراز تنگه هرمز
روابط عمومی ارتش:
🔹
ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفته اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش در منطقه جنوب شرق کشور، تحت شبکه یکپارچه پدافند هوایی کشور، بر فراز تنگه هرمز مورد اصابت قرار گرفت و منهدم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/691524" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691523">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd208e723.mp4?token=YNQZu4XKAtbW9lqgVDBc-StOtsyVZ-KW9UF3rmB7Y8oPOq1hiKxT21sLqCEFB1b04pCO-PQI_EfbuwZ8blDwbGp9OJb5kk_faX2PTbOWCuyOhDQ-ulR88IM8kpW7Fy4aAOVC-CaVIOi9yi14QG2pZOrg-vdGxuTdeRQVT2Lc2rrJ3ELy3gVjtf-yAowbH8N639oGuKcZYfjJluDwerCfbw1Jm_-KmwvcNLdmc2EvFJCWcvsh1nLOU2QMPu6fwWHRHUnXP8qiqmkKhYIU2wGErMIQHmT53swrK6SrjNro0bq32QioOEGfrdwgQ083u3sb0I9Oa2wirkJXH_iKDXgDEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd208e723.mp4?token=YNQZu4XKAtbW9lqgVDBc-StOtsyVZ-KW9UF3rmB7Y8oPOq1hiKxT21sLqCEFB1b04pCO-PQI_EfbuwZ8blDwbGp9OJb5kk_faX2PTbOWCuyOhDQ-ulR88IM8kpW7Fy4aAOVC-CaVIOi9yi14QG2pZOrg-vdGxuTdeRQVT2Lc2rrJ3ELy3gVjtf-yAowbH8N639oGuKcZYfjJluDwerCfbw1Jm_-KmwvcNLdmc2EvFJCWcvsh1nLOU2QMPu6fwWHRHUnXP8qiqmkKhYIU2wGErMIQHmT53swrK6SrjNro0bq32QioOEGfrdwgQ083u3sb0I9Oa2wirkJXH_iKDXgDEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش اقتدار موشکی ایران در رزمایش جانفدا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/691523" target="_blank">📅 20:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd51ad34a3.mp4?token=nIUbDJkraOcFPEIG89jZghUr0iBYlFNYKbUIn1n5zNL-FIQ5rd0HDkMQ-j8HT2BoBkaXoHJ_2PuKxCl_tx0GAG4ZNhX-eCPRmAsvyuRlickFGagww-GMHqfVb5YvCM2VVDivoQb4RKErg5NBcTA2bfeqzpnt9kn-OhcfcLezHFWRyWbAQE940OUN2Yloj7Ok0qbRYktODlyig7xKXogEEtxjogvcZhH2tNrjmN4HUdZbGviOIiccm4hfV7MHEOd4KJmq9bNqe3278s4yI7owsen3Gm-vjuA2RDKQ1bCxrHPFCaxaB35C6UuPgP6GuXpBKB5KzCfQHiMIVQr25e6RWSKPrZcCPnk6IFjf1Irsh7ey2I7YsyDrw6N8c-yNnwCPw6qvegUWdgyWJZIms6yusnXV7g2Bu0EJJembo3c74uy4w6HJzxlA9FTFIdstbForL9BnMyWFTM4xaguCR7b2KJKyYUjT-uC-x7qvnhc2C7pLpfgN0jdv8sS3CG19wPwK4WcMLRNVOv7yR8NqPoK4FfPMdvwPLaH9MWsk_LPmFGJtt2pfE82a6IXYm8-xrUqSC8Fm8p7e9AzIcYMz3tUiFSCo609FemkDf6Kf88SvtkG_-uzRqupULOmk_ccz25KJx4MgaAPdDNz4NMwOv5TbYO9_fmqFOYI7uzF4EKaNgtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd51ad34a3.mp4?token=nIUbDJkraOcFPEIG89jZghUr0iBYlFNYKbUIn1n5zNL-FIQ5rd0HDkMQ-j8HT2BoBkaXoHJ_2PuKxCl_tx0GAG4ZNhX-eCPRmAsvyuRlickFGagww-GMHqfVb5YvCM2VVDivoQb4RKErg5NBcTA2bfeqzpnt9kn-OhcfcLezHFWRyWbAQE940OUN2Yloj7Ok0qbRYktODlyig7xKXogEEtxjogvcZhH2tNrjmN4HUdZbGviOIiccm4hfV7MHEOd4KJmq9bNqe3278s4yI7owsen3Gm-vjuA2RDKQ1bCxrHPFCaxaB35C6UuPgP6GuXpBKB5KzCfQHiMIVQr25e6RWSKPrZcCPnk6IFjf1Irsh7ey2I7YsyDrw6N8c-yNnwCPw6qvegUWdgyWJZIms6yusnXV7g2Bu0EJJembo3c74uy4w6HJzxlA9FTFIdstbForL9BnMyWFTM4xaguCR7b2KJKyYUjT-uC-x7qvnhc2C7pLpfgN0jdv8sS3CG19wPwK4WcMLRNVOv7yR8NqPoK4FfPMdvwPLaH9MWsk_LPmFGJtt2pfE82a6IXYm8-xrUqSC8Fm8p7e9AzIcYMz3tUiFSCo609FemkDf6Kf88SvtkG_-uzRqupULOmk_ccz25KJx4MgaAPdDNz4NMwOv5TbYO9_fmqFOYI7uzF4EKaNgtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیکانی که به مهدکودک می‌رفت!
🦩
🔹
«کاتّا کون» پلیکان ژاپنی بود که از سال ۱۹۸۹ به مهدکودک می‌رفت و با بچه‌ها وقت می‌گذراند. او در سال ۲۰۰۸ درگذشت و داستانش بعدها به ساخت مجسمه و یک مستند درباره ۲۷۰ روز رفت‌وآمدش به مهدکودک منجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/691521" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691520">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q03mb_i0Ff-VcTJ39Qk0N9Nailj1uyHvSb0fWbR-YQc1O_w9w8KiJ-xvChTdHeFBGxHoMUc4JAG4BdObJ-UasCgJdKsvyjqUk7gQzG6Jhn6qlTH__KgHXIqoMh9uz5GdQk4nEr5rSuNVcAJG_1VfQLPc9jY0HQgVT9gkfAtryyuJXN0sIqEAlHsrN7O04BtyE8uryZ8w_xofgFqWihii_oCxVC2ruHrYGwLcyXjzDlSuuFwBo0Ddg6-ZUvX6l-9_eYaWn-ZdsNwr9OrDSDclorN0msMa25FvYRf1GDqpqoaU7cPZCQBI2edEPJiS7hixa94w2X31_Ye0Cxitl0mfkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارو، درمان و خانواده‌ها | تحریم صنعت هوایی ایران چه تاثیری بر زندگی مردم گذاشته است؟ | آیا آسمان ایران بسته می‌شود؟
🔹
تحریم صنعت هوانوردی ایران وارد مرحله تازه‌ای شده است؛ مرحله‌ای که آثار آن فقط متوجه شرکت‌های هواپیمایی و زنجیره تأمین این صنعت نیست و می‌تواند مستقیما به زندگی روزمره مسافران ایرانی سرایت کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246674</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/691520" target="_blank">📅 20:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlcFfwyfLTVdlTHDgH7ABkSZw2SKiDACX0rnNALdWFGog0teQRdkXmnKn4gHVaXs2B-u7yq2JDqLQ1vKMfCFzCGYTJD2GnR3QPjpTcZOVXc8RErY48MjqmQFmH3fBkJYs-iFGp2IejZzcfSL7yW_913TPbPyaQZxKpJ9bP87gFE6tibSAQMtkMfdBcTftYZybD8LuuTuwz2E0-C5tIPp8JMsImjNpYjEeosvoIy-zkoI5DlWF5mb93wDSCshxekw8vW75TWNS82OKLVxncZ6Bi-TnQ97CBc5C9XmAnn5mlk4rpZ1QRzlpfK9baTBjdy6FGv06eXOJ--fbI2lWkQehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ تصویری منتشر کرد که سی‌ان‌ان، ام‌اس‌ان‌بی‌سی و پولیتیکو را به شکل کیسه‌های زباله در بیرون کاخ سفید نشان می‌دهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691519" target="_blank">📅 20:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
پزشکیان: ما از هرگونه مذاکره‌ای که به امنیت و صلح پایدار منجر شود استقبال می‌کنیم/ الجزیره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/691518" target="_blank">📅 20:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">16-2 Ane Manaee (1404-02-01)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/691517" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه شانزدهم؛ بخش دوم
حجت‌الاسلام امینی‌خواه:
🔹
نقد و تبیین مشاهدات شخصی از انحطاط، حس‌گرایی و نادیده‌گرفتن عقل و حق در جامعه [00:06]
🔹
مرگ؛ معیار تمایز حق‌گرا از حس‌گراست. اولی مشتاق وصال حق…دومی هراس‌زده از مفارقت حس [07:33]
🔹
سیر حرکت حق‌گرا؛ از تعبد تا اتصال به حق، و توقف حس‌گرا در غرایز و توهمات [17:53]
🔹
حق‌گرایی یعنی؛ تبعیت از قرآن و دوری از تناقض‌های رفتاری و نفاق، بدون توجه به پسند یا نپسند مردم [23:43]
🔹
«قاعده تضاد ناپذیری حق»، تقابل میان اهل حق، نتیجه اشتباهات و جهل است نه تناقض در ذات حقیقت. [27:52]
🔹
ایمان به قرآن تنها راه رهایی از سوگیری‌های شخصی و تناقضات رفتاری [30:38]
🔹
بهبود حال و هوای روحانی، محصول رهایی از حس‌گرایی‌ست، اما تشتّت و گرفتاری نتیجه دلبستگی به دنیای مادی [36:49]
🔹
تأثیرات متضاد قُرب و بُعد به عالم نور و وحدت و عالم ظلمات و کثرت [40:10]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/691517" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
آمریکا به‌دلیل شرایط امنیتی، تردد کارکنانش در عربستان را محدود کرد سفر به «طائف» و «ینبع» نیازمند مجوز ویژه است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/691516" target="_blank">📅 20:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd9cab305.mp4?token=HwkFqoQboL2wkGB8TGbtu6YTliF8m0zrunjP3PWgNE6jhlQw_tTXPdbnY3MK6_EbzxtjAZRW3qLQD1ZeGts_-XA3tFpZHvDN14GEBPh6TXCMx3kOjD2jAYypG9oerlhPU8EIv2dv6nxtXaTbiBn6QuqTMvJvkSRFaMd1DLEpwJdpEHxObn_CuCiUQPXCE4lIWphrH2V4Z-CgCwFShK76Ia-9ejbC2uTmtj1Rr5U5-gq-65CEt6BLrWSZHhaWkFVqv4R2h3MBfvbo7bjHgcWFdjOmnv_2XVm_tOWtsksRiF5BfBk6PecVCGXvSobhnjYwLrUA8KIFwTWgV0eSNNizMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd9cab305.mp4?token=HwkFqoQboL2wkGB8TGbtu6YTliF8m0zrunjP3PWgNE6jhlQw_tTXPdbnY3MK6_EbzxtjAZRW3qLQD1ZeGts_-XA3tFpZHvDN14GEBPh6TXCMx3kOjD2jAYypG9oerlhPU8EIv2dv6nxtXaTbiBn6QuqTMvJvkSRFaMd1DLEpwJdpEHxObn_CuCiUQPXCE4lIWphrH2V4Z-CgCwFShK76Ia-9ejbC2uTmtj1Rr5U5-gq-65CEt6BLrWSZHhaWkFVqv4R2h3MBfvbo7bjHgcWFdjOmnv_2XVm_tOWtsksRiF5BfBk6PecVCGXvSobhnjYwLrUA8KIFwTWgV0eSNNizMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیگار کشیدن چه تأثیری بر بدن شما می‌گذارد؟
🚬
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/691515" target="_blank">📅 20:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
پزشکیان به نیویورک می‌رود
🔹
بر اساس برنامه فعلی، مسعود پزشکیان برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر می‌کند و ضمن سخنرانی، با برخی سران کشورها دیدار و رایزنی خواهد داشت. یک هیئت بلندپایه نیز او را همراهی می‌کند./ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/691514" target="_blank">📅 19:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd823234ef.mp4?token=Rgu2sOFn8A67kndPtyYp21VVIK27YnB7lWuu8CdoDZYz4kxt8YhIrS9wZnsuN432RpmBUvxz14h4dr0dIsFkPW0IgUlaigjXD1HhxB2_B_b8p3jWNLYhaesYRghlrZ0AT_vSy-Iuw5WeyINqGiArYiBr8dFXG6lTg6gNpnwdZ0l7Uw9unnW7kFfDvt1-BnwTPbPDFAPRZV1xmJZe4Zxy9acb8mexlDUKo9iIf_UmDkZ40g5607bj0Sp6kqhjfi9dQnCwlxEZ8SQDqnfbdp_3xf79EHOSXS6e2Eac8AfeolvJE8flrw6eISwHGaQu8yaePUIjniR50BxIabwUjxfYpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd823234ef.mp4?token=Rgu2sOFn8A67kndPtyYp21VVIK27YnB7lWuu8CdoDZYz4kxt8YhIrS9wZnsuN432RpmBUvxz14h4dr0dIsFkPW0IgUlaigjXD1HhxB2_B_b8p3jWNLYhaesYRghlrZ0AT_vSy-Iuw5WeyINqGiArYiBr8dFXG6lTg6gNpnwdZ0l7Uw9unnW7kFfDvt1-BnwTPbPDFAPRZV1xmJZe4Zxy9acb8mexlDUKo9iIf_UmDkZ40g5607bj0Sp6kqhjfi9dQnCwlxEZ8SQDqnfbdp_3xf79EHOSXS6e2Eac8AfeolvJE8flrw6eISwHGaQu8yaePUIjniR50BxIabwUjxfYpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متفکر آزاد؛ نماینده مجلس شورای اسلامی: جان‌فدایان ملت ایران؛ ظرفیتی که دشمن را غرق می‌کند
🔹
جان‌فدایان این کشور به گروه، گرایش یا قشر خاصی تعلق ندارند؛ آن‌ها و هرکه دلش برای این کشور می‌تپد ملت ایرانند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/691513" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
قیمت زعفران از کیلویی ۳۰۰ میلیون تومان عبور کرد/ ایرنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/691512" target="_blank">📅 19:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k72DOG3jSb8brOjCZYarMMhsxdmJIBhVJ-5y7bl7AEFVptKciqO7_64bwEa-Gkdky3p8ZgwSPTIZBTwx-5_eCAewur3hxanU1XA4mv_nMx9bgnY68HlMK_DeMzOz21RAPPEcqvZVCPVD-OdCnWHyXVACSZwG-RtU2JuoCTEEbClP7txbCmMkE33SKXTxeJEQcWPBhfF90_0gUcjBKii8wzm_R8xn3jXp1DEETbQyXYTqrK3X366t7u8VQujj4Z3bqWyhZe8nFgnY-vljzyveIxR_Fq2tmAIpXaafzq2V13kA2qcJo3GFV7uU1_LTVgrN2UJrZck1UbH9aqxSwRjakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با پایان تابستان، موج گرما بازمی‌گردد؛ تقویت پرفشار جنب‌حاره‌ای موجب افزایش دمای ایران تا بالاتر از نرمال طی هفته آینده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/691511" target="_blank">📅 19:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4472dofrvTUr6jOr5FAVqinK1bNc_bzbcViSR5W3gF_jb_ySosfkQfKgREZ4BnYEFxHHxfSw3lh7ocziEs9cvXnxTEU0hc5qsxy4R4q3Rm6DFjutOKEhptFmuDe3dBr-ktL8tHD2kMQ1G_7puPDctv6RxAUNSDqKFqQRAoXXw6Yxv4IE35U8XR7yvM3585EhspH0nppOJed4v9I-U6YNVngA0mhx3p3AUP48TWxGhvT0mVHHUp0JfsC94XASiwBUxxxSJ98p1l_b8MqDAZYxL0D2i0VsuU6EAnSE3FqzwIr8PNbz796m2c81sADhVTOPoGF4aAv1TkPsqeh4mtjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخی منابع خبری غیررسمی با استناد به داده‌های فلایت‌رادار ادعا می‌کنند عباس عراقچی به قطر رفته است/انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/691510" target="_blank">📅 19:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691508">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbqnBV1txgjbT3yGCSivJCKnz1serMOF5uBBv-_GuD7Us10WVwfNhtoseIB5luTs0HiSdWnHyA12xgbyYS6e5qd-N7cHj85FFScBaX8ROv17ROV1tNU3q2S3JYtDlcv4uaB8Bm3x-7fm5PPMqSIf_hp0PERamnLVkKOPlMNnrMK4-_iNP5K_Z8PEt0_b8HMEgQSSGdTAnMl6jNvOuLG8WCVyqe6m7wJw-RoWxotNk6JNFQfQvUGFTZuU0phf4MlVzs8WGMYbc_uQPxbs2SYv04PYVBeU45Oc3kzqq5G-_XAID3bePqAZ4WCeK0xCUIXQtC_TJmkbs2kvzJXCt9qu2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آشنایی با انواع دهنده و گیرنده‌های گروه خونی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/691508" target="_blank">📅 19:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691507">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW4WyvxelqEh-hEpHC36MZvUB774kV90tfeAtH78q3BIsh6Z8RIdAHouFyzAS0gER186qow4Xr-t-S8xGS8q_af7U1cZGnozueARSgYJrhX_q2qJlBCp-cfpNH-TBG5bfhEgkQ2onWJWC5C0eolyKh40HxN9XBP5oKTJFi9AoLDmGaNMdRdcV62NA2zDqlf7iXkJC5JINvLbJJgvqlIyczMluS3du_qMcR1cxQWse7OF16wxg_ObCnlqh-ozPOuLsmAe5nfQK7i16dVHQBU8A5ui5ui1KWXelaJmiyalX7XHGPGz3VGTvcqtLcMwQVIfYLwFqFQ1clHec2qHxnjB9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ راهکار مجاهد برای تبدیل ظرفیت «جانفدا» به نیرویی برای حل مسائل کشور
🔹
مهدی مجاهد، معاون پیگیری‌های ویژه دفتر رئیس‌جمهور شهید: حضور مردم در تجمعات شبانه و همراهی با پویش‌هایی مانند «جانفدا»، نشان‌دهنده یک سرمایه اجتماعی ارزشمند و آمادگی ملت برای فداکاری و مشارکت است.
🔹
این ظرفیت اگر به‌ درستی سازمان‌دهی و هدایت شود، می‌تواند از یک موج احساسی به یک نهاد پایدار مردمی برای حل مسئله تبدیل شود.
🔹
محله‌محور کردن، ساماندهی داوطلبان تخصصی، پیوند با تولید و اشتغال، استفاده از ظرفیت مردم در بحران‌ها و ایجاد سازوکار شفاف برای ارائه بازخورد پنج راهکاری است که این ظرفیت را ظرفیتی برای حل مشکلات کشور تبدیل می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/akhbarefori/691507" target="_blank">📅 19:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691506">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCpp-KE0XvabeddA-ozVDwGZwmnk9mcg3uy3ZhtJ9qzeLkotKyk6LAork47wxU6nRbz9B6NUQhQr7fO7rDoZEjp68ujLAB0uQktnrkkAq0_-Q0Ln-sYB4e5imzJ2kNatMbvQvQD8bPiT0YZnywyAVFeqDI2r5WfluBRc_wWsRtYwuvgUUYlzCBrfFXh4YMN5RVsdffElg1WCKtNLBZpBywlLbp_-_DssfjIiAsJWodtATA0WxXs1uEDB9K81r0uD12rFWRhHyuvRwSRsXuPa-siZwwceShjFIJWH3OJPaufOzrwk1XaFF5coRQKFkzS8m0IJVfYhkzXPKHUwcUJcLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایلان ماسک مجوز بین‌المللی اتصال مستقیم گوشی به ماهواره را گرفت
🔹
کمیسیون ارتباطات فدرال آمریکا مجوز بین‌المللی Section 214 را به SpaceX داد تا Starlink Mobile بتواند خدمات ارتباطی بین‌المللی ارائه کند؛ مجوزی که مسیر توسعه اتصال مستقیم گوشی‌های معمولی به ماهواره‌های استارلینک را خارج از آمریکا هموار می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/691506" target="_blank">📅 19:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691505">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im58CDRT3lntAyPRjKdwCq1ZU21XhUyxQTofJ5i8cyeCiIF4xgPYeo6QVy9tVtYb_0gogKOPb1z7EEJ07yZ-p6I33GVK6SKegq3DP2_5gqX0J8Mhgy8SrZPGEEtMB0rCFtwGFp9bLA0nslg4pF7GigqmOvY8kfkT-0frE-MeYpCxu03TCuAebgHX9amC_BzXAVOxbYThj4kWcSiTSO4DvmL_rVByGhI1JDj9n0OmGU58-SP7RZ-6dqboTxEyNXYs8XoKUYSEH2fXExQ_-0ks85g29L-Kwz3gPpiqUj5K1ndCbZz8CDju_p_5kDRZ6N7KUUsneTfpU--pqsphZhIrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران در لبنان به نقل از رئیس‌مجلس: تنگه هرمز تا تحقق شروط ایران باز نمی‌شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/691505" target="_blank">📅 19:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVCnpihh8lI48aicdSZmK-zme2dS0-yx6ZhEQsA-c8xyMBYKr2XXyavz2mj0NB1PvII-1yQDwFMq09l77ey2-ErqluCNg0acqazM76aNzzQiCRIiT9CXaJ1C-L2ZcJEJezin5FD0NLqiDPiTfwD2YqPIeU8Q31LUrgUUYMSIOTWUPONYUvHWdWlP3P2HisvF9cqOJUhKcgRgRZHqmAhOEpfdNHo2Y8LFdL7QuqLLTFxZEtOf_X9L0y_BhA9IrSiLEjtfjJ9adCO6tfIOHxZ9brWvx1mTp7v41MG5LIhhQG7RnvzbFmROlcKVUbALXbk-dWbCYOMc0W7C1PvRG3x56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین یکی از بزرگ‌ترین موج‌های پهپادی خود را به سمت مسکو پرتاب کرد
🔹
روسیه ادعا می‌کند بیش از ۱۶۰۰ پهپاد سرنگون شده است، از جمله ۴۵۰ فروند که به سمت مسکو هدف‌گیری شده بودند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/691504" target="_blank">📅 19:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fa58cfcca.mp4?token=k2osmf3lEO75VZOtpbwRZxdsuycxxPJQmmTDLO79uW_yj1Z2KXdtx1upz4QDaehR9cr_XmDaDamrhH38dr3lUtXhcqP0vqDSi0Po6q7DEQojQQu-I6pk1WoQOc6p8dXXsRUIG67JLFaV2cbIF13m5eXuPaJgeqLtx6g_DZNyv8EMdbJDVMBKa_hPgQfw4SxigAfKl3BZMerp_tQY2S5mYPjbvIaXtioJxQOEWYx1z2n5Ak4hayL3A0DlhRFhXYEhFOdZYY_Bz33Immui4AE_XrXfpWLhTsUGJ5DwQKEbgfyq4SZmuW3M0Fu4MspGEqvuTG3oYmtl84fmDH415Alz0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fa58cfcca.mp4?token=k2osmf3lEO75VZOtpbwRZxdsuycxxPJQmmTDLO79uW_yj1Z2KXdtx1upz4QDaehR9cr_XmDaDamrhH38dr3lUtXhcqP0vqDSi0Po6q7DEQojQQu-I6pk1WoQOc6p8dXXsRUIG67JLFaV2cbIF13m5eXuPaJgeqLtx6g_DZNyv8EMdbJDVMBKa_hPgQfw4SxigAfKl3BZMerp_tQY2S5mYPjbvIaXtioJxQOEWYx1z2n5Ak4hayL3A0DlhRFhXYEhFOdZYY_Bz33Immui4AE_XrXfpWLhTsUGJ5DwQKEbgfyq4SZmuW3M0Fu4MspGEqvuTG3oYmtl84fmDH415Alz0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی ماندارین انگار مستقیماً از یک نقاشی سوررئال یا دنیای فانتزی بیرون آمده! این ماهی یکی از خیره‌کننده‌ترین موجودات اقیانوس آرام است
🐠
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/691503" target="_blank">📅 19:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzF4rwLjKdcJseAvKVO0Wt4oQvW7dhugOND1J4u5AT-g-7x3-28187DaIcxbYXH3w2EdN6VefLTkWJz2FZzSQV27QbIsFOm8cuTq6NPCszMpKVbNckXQJfDiCsidJuJRGQmtL_bJsqI6P1PJ8rI9MTVluL4J2BIcF5-ChpqrVWLpx26EUvTAbUJDxEnyvZPWk1whYz2lS3tJoc5-_98k4uTWlgajAY7OLp2PkKmh12uxCic_Hfiq_ux2-8U_e9ric1FgmxpymRJCp_hpCD7IovhwvchUtmVmwyJpx_VZMDaR0AIfwzceMG431xqSwTln5CU52AY5lwFt1Q9d5GMFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تا ۵۰٪ تخفیف روی تمام محصولات چرم رجحان
اگر به‌دنبال
چرم طبیعی، طراحی شیک و خرید مطمئن
هستید
مجموعه
چرم طبیعی رجحان
آماده‌ست تا انتخاب متفاوتی برای شما باشد.
👜
کیف |
👞
کفش |
🧥
پالتو |
🧤
دستکش |
✨
اکسسوری زنانه و مردانه
🔱
چرم ۱۰۰٪ طبیعی
✅
ضمانت اصالت کالا
🔄
امکان تعویض و مرجوعی
🚚
ارسال سریع و مطمئن
💳
خرید اقساطی تمامی محصولات
با امکان پرداخت از طریق:
🔸
اسنپ‌پی
🔸
دیجی‌پی
📍
خرید حضوری:
مشهد، برج آلتون، طبقه همکف، پلاک ۶
🛍
برای مشاهده محصولات و ثبت سفارش، وارد سایت شوید:
www.rojhanleather.com</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/691502" target="_blank">📅 19:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
رشد ۴ برابری قیمت موبایل در یک سال
🔹
افزایش قیمت تلفن همراه در یک سال گذشته، بازار موبایل را تحت تأثیر نوسانات نرخ ارز، افزایش هزینه‌های واردات و محدودیت‌های عرضه قرار داده است.
🔹
به‌طوری که قیمت برخی مدل‌های پرمخاطب طی یک سال دو تا چهار برابر شده و دسترسی…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691500" target="_blank">📅 18:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691497">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25c3c8eeb5.mp4?token=XXMIJt27x8SoEU9-_USech_sXjrAmeoTJ568Nn6qwSg3aRJ9NFuEDeYYQTrnn2sxiJwwGY6z018m0qATpsnAPT-yyFkZqKowpNhRvaisnWXqOzOCKtJQP6hYYR9fYcpEdE_2Zo8wG-QmrJ8H6l6r7tJZEkVbbbNrrk7emvSEwbMO4S7U9Prh5hpodw6AKjDmLdF3mRuuCzgMiWqsAvDSRnxbdioA0dcPIQYqSzxKI4LO8TwLW3Aga2IoxyMTvFwMt4dm777FNJFBsDc1MZKnPlDSYA6gH-Pm6LcQn4McdKA6Y7YRoMR2WRAVCWDKmVeYwKXhWeV9lfyBnwF-xKVvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25c3c8eeb5.mp4?token=XXMIJt27x8SoEU9-_USech_sXjrAmeoTJ568Nn6qwSg3aRJ9NFuEDeYYQTrnn2sxiJwwGY6z018m0qATpsnAPT-yyFkZqKowpNhRvaisnWXqOzOCKtJQP6hYYR9fYcpEdE_2Zo8wG-QmrJ8H6l6r7tJZEkVbbbNrrk7emvSEwbMO4S7U9Prh5hpodw6AKjDmLdF3mRuuCzgMiWqsAvDSRnxbdioA0dcPIQYqSzxKI4LO8TwLW3Aga2IoxyMTvFwMt4dm777FNJFBsDc1MZKnPlDSYA6gH-Pm6LcQn4McdKA6Y7YRoMR2WRAVCWDKmVeYwKXhWeV9lfyBnwF-xKVvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلایه شهروندان از وضعیت نابسامان آسفالت خیابان تمدن
🔹
باسلام، فیلم مربوط به مرکز استان  می‌باشد، خیابان تمدن، بین تمدن ۴ و ۵ غربی. سالهاست این خیابان پر از چاله و چوله هستش ولی از سال گذشته تا حالا این قسمت بوسیله ماشینهای سنگین انبوه‌ساز کنار پارک تمدن بطور کلی خراب شده و روزانه ده ها میلیون خسارت به مردم وارد میکند.
(حسین نظری)
🔹
استان لرستان، شهرستان خرم‌آباد
🔸
ما در  الو فوری همراه و صدای شما هستیم؛ چالش‌ها و مشکلات محله‌تان را با ما در میان بگذارید
👇
#صدای_شهر
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/691497" target="_blank">📅 18:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691495">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdkT_HLFC4RhzLdEdoZEF4owC5O5Ckk7FdaTeOKmSlfEkP8bhhcB63p3AI0fxaHSedsXOPicD0RwTaIMz2-lYfcDXPdL5ASnWr55zkETwWpN8O7W3A5BCZY_mksbmM1YEf6aGW_uWJ1Qv42FbgGthqif5OsdMgC9ZW-6lJTfWJfYDWwlpdZZLHfS8VVQEytwDQLaRSNpfAfx9lM-9diaX2OsVPdCeEORJSFtvklwrm9q4sta0hZ7Vy0rUSzfH0-GsIX6yOxfjJeSj7YZzmvvzgX_qtrZhjd1ampFEJS05VK8ufAj1hbAtX1_KcpeZNGAqgB9RvxXDW_xNF53Amjew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توزیع ۲۵۰ هزار بسته نوشت‌افزار ایرانی برای دانش‌آموزان مناطق کم‌برخوردار توسط ستاد اجرایی
🔹
سید پرویز فتاح مدیرعامل بنیاد برکت ستاد اجرایی فرمان امام در آستانه آغاز سال تحصیلی جدید، از توزیع ۲۵۰ هزار بسته نوشت‌افزار و ۱۰ هزار بسته معلمانه با هدف حمایت از دانش‌آموزان و معلمان مناطق کم‌برخوردار و کمک به تأمین بخشی از نیازهای آموزشی جامعه خبر داد:
🔹
۶۰ درصد بسته‌های نوشت‌افزار ویژه دانش‌آموزان مقطع ابتدایی و ۴۰ درصد مقطع متوسطه
🔹
توزیع ۱۰ هزار بسته معلمانه شامل ابزارهای آموزشی و کمک آموزشی برای معلمان روستایی و عشایر به ارزش هر بسته ۲۵ میلیون ریال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/691495" target="_blank">📅 18:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45feae1ad.mp4?token=a1N20_xqWpCEQ_lIGEU4uvvPAGH5wvxuvZ1ThVgs2Cmv1HUftacW1oGy-S3aDwE6vJ3iwmusz9sSyV1biIx4gO5iGP6HcAHxxGElAILgv1VXr0YLHAD7tFPA1XH3kyWeHC67KM156LDPVGINtJNvIK0ZbvJO1xm7lB3BJklA-Ssw9IXq7u1Q4krk2oxa2tGQXBjrp7aJeb4HGh3wkgIzKEE1a2DAZTLAPVzdcjTZSa9GnFMAFZuhuyN4dyHbnmhuAfpY0OEwizYXCSnzFVja0vrNNkNbR0ZY1STMfhzKvsZ4Mpcujip4zpgHuAaPKo9GuQe7jzew1mDYIk9yl7y9_Y7WbwWPn2OFC6IvZwSpTuJVTirDWeZnLI1xpdXrCmaYbuRYWpAayDnYKzMEJ6AqbLe2qxG_NanFIDBi8Q4szDsjp7-vj6t7lp3loRDGHzOMhWW6h58kiWA9nGPYujEx1KCr3swIzQS9XlKhOPpsFCMd7VL5qDezFmuGg1j-szg6V4EONuwnkiyIi2F_CoWtoWGrm7rgJqTpisDR4SYa0fn5DeTmfkS5W7XuhMcMnFgx2yzzCUDavll6s0TCIYPTTS303uL-hbT2CBBWIrOaiQKZY55MaDLRbjXcGQSRg9nuX_2TNoEPyYKml0dOVPsGr7sMr58b_97dQk-h1wD8kAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45feae1ad.mp4?token=a1N20_xqWpCEQ_lIGEU4uvvPAGH5wvxuvZ1ThVgs2Cmv1HUftacW1oGy-S3aDwE6vJ3iwmusz9sSyV1biIx4gO5iGP6HcAHxxGElAILgv1VXr0YLHAD7tFPA1XH3kyWeHC67KM156LDPVGINtJNvIK0ZbvJO1xm7lB3BJklA-Ssw9IXq7u1Q4krk2oxa2tGQXBjrp7aJeb4HGh3wkgIzKEE1a2DAZTLAPVzdcjTZSa9GnFMAFZuhuyN4dyHbnmhuAfpY0OEwizYXCSnzFVja0vrNNkNbR0ZY1STMfhzKvsZ4Mpcujip4zpgHuAaPKo9GuQe7jzew1mDYIk9yl7y9_Y7WbwWPn2OFC6IvZwSpTuJVTirDWeZnLI1xpdXrCmaYbuRYWpAayDnYKzMEJ6AqbLe2qxG_NanFIDBi8Q4szDsjp7-vj6t7lp3loRDGHzOMhWW6h58kiWA9nGPYujEx1KCr3swIzQS9XlKhOPpsFCMd7VL5qDezFmuGg1j-szg6V4EONuwnkiyIi2F_CoWtoWGrm7rgJqTpisDR4SYa0fn5DeTmfkS5W7XuhMcMnFgx2yzzCUDavll6s0TCIYPTTS303uL-hbT2CBBWIrOaiQKZY55MaDLRbjXcGQSRg9nuX_2TNoEPyYKml0dOVPsGr7sMr58b_97dQk-h1wD8kAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر آخرالزمانی از پالایشگاه مسکو پس از حملات پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/691493" target="_blank">📅 18:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqnYVecb4XTMlKFmZ-lthnjuVG2CLEPfVaM6LwdfYGo5nhgSDQcqJ63t-jynAb6q_eovyxbgxzpQYJCt7WyAaqstatmXbJmHDFqS3bcDWbyuCST5FK9msZj3lmGZJeDJnwqoaV4Xl8l2gEYmQa2SZcuQWznPaGf7M9LzyMZNhbu6UhSmkNHbXwt581WZT_dA_g9oONDFPKqK1NF6Z9yPUGMGhTigHDjT8JhsbQh6cVfCeMVadacgKrEt-CCH5g3NE9hr30dNj2mieLKUc8T_dclUUgddOcj6phjERnZkWVK3XOn7ipansl-_hAdZgc-bLF8mUackCdyS_-BoN_825Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاسخ‌ بدون‌ درنگ
🔹
آمریکا هم‌زمان با افزایش تحرکات نظامی در منطقه، برای کشورهای منطقه و شهروندان خود هشدار امنیتی صادر کرده و نسبت به احتمال تشدید ناگهانی تنش، لغو پروازها و بسته‌شدن حریم هوایی هشدار داده است؛ در همین حال، قرارگاه مرکزی خاتم‌الانبیا اعلام کرده است آمریکا و اسرائیل با چراغ سبز برخی کشورهای منطقه و پس از برگزاری نشستی مشترک در یکی از کشورهای اروپایی، درصدد ازسرگیری اقدامات علیه ایران هستند. قرارگاه خاتم هشدار داده است هرگونه اقدام جدید آمریکا علیه ایران با حملات مستمر به مراکز استقراری و منافع این کشور در منطقه پاسخ داده خواهد شد و کشورهای همراه نیز نباید انتظار خویشتنداری نیروهای مسلح ایران را داشته باشند.
🔹
هشتصدوشصت‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/691492" target="_blank">📅 18:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
پایگاه خبری اماراتی العین مدعی شد ایران کمتر از ۱۰ روز پس از کنترل سواحل غربی یمن توسط حوثی‌ها، برای گسترش نفوذ خود در این منطقه راهبردی وارد عمل شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/691491" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljuoQMkqdi1hjRYA_fMmMHF4_HPGqWZbU5F-sIvj7d1DioOjt1kzUjzqI3a-eo3Tba4f1ipz5xxrQYzzJALFI3gW1xK6mjTqKq50aitHd8AU3W5YJe-o0NvkqA5r_5fqFIw16l7RGf456jNG0Wo8Vva92kqnyduKb6q4ft-ibEgSMof_ttM-nyJXe-8at42nrkJbnTJmz7Yhu8BlusFwWr-giq0szgfk_-QNljhWMxBLu-mAAEET4qdnshDa51ECJ-taOLty2BsqOzHCC3PE4cebSgxQEud1Eonlg_U-4tHQi8G-waEdGESvnz7KzrTguSI_bn-9MfN1b_rBhzqReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کابوس آمریکا در جنگ زمینی با ایران/ این توپخانه‌ها می‌توانند آمریکا را حین ورود به ساحل نابود کنند
🔹
اگر تهاجم زمینی رخ دهد، توپخانه ایران می‌تواند در جزایر نزدیک ساحل، تنگه هرمز و مناطق کوهستانی غرب، تلفات سنگینی به نیروهای آمریکایی وارد کند. فجر-۵، فاتح-۳۶۰، رعد-۲ و ام۴۶ مهم‌ترین گزینه‌های ایران در این سناریو هستند.
گزارش تحلیلی خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246661</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/691489" target="_blank">📅 18:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجاباما تور</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWRBk5b7Nw5hcwY2oy_0lzSEljZMUzgWBXM-cYiPo3tuvABATQd1KJeYH-ACf4pBe8HEeiLHAJ8T8ZaZl29TOXZ7lebuDhu3-70k9ASyiioFgoZkKOJm1xN8IAVydldfE_FFpFgWBx8a6DthT43vWQJfxAzY4-UPfXLrBwMAsJ8ymOx3DMdX35Ig05ZwSkU6A8iG4S7i-0jYel9cdo3YY6G5gZ_ebzTAicHnDgNjOHE-gB5aGxT9k2anfZoKwUv1U2XHH_1b_kJdueqbZVaryr1QhvvsAME8hwc0GgeOFyGljSuVrRce3AqGByH2xIwkX709bCyyHfv79Oig8Ny2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ۱۰ میلیون تومان اعتبار دیجی‌پی بگیر و
هزینه سفرت رو در ۴ قسط پرداخت کن!
تور موردعلاقه‌ت رو پیدا کن
:
🌤
از یک‌روزه تا چندروزه
💰
از ۵۰۰ هزار تومن تا ۵۰ میلیون تومن
🏕
از سفرهای آفرودی تا جنگل‌گردی
🎁
تا ۱۰ میلیون تومان اعتبار دیجی‌پی
✅
پرداخت هزینه تور در ۴ قسط، بدون هزینه اضافه
📞
برای انتخاب تور و راهنمایی رزرو:
02149275111
🌍
جاباما تور
@jabama_tours</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/691488" target="_blank">📅 18:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
الزام درج نام کامل «خلیج فارس» در اسناد و مذاکرات
سخنگوی کمیسیون امنیت ملی مجلس:
🔹
طبق طرح جدید، استفاده از عنوان کامل «خلیج فارس» در مذاکرات، معاهدات، توافقات، اسناد و مکالمات مرتبط با شناورها و ناوگان‌ها الزامی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/691487" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f78b96a18a.mp4?token=lSEJVdK_yqHY4xRgzHvXT4c3YnusZDgfF5nSMejMdfKJw0aBFM_ZnKavWWZFccOwosTr5H0JqFABjm4dACe6Uch0DF-NVqG4LxE7oEeV-PhQWJQP6lKF0XoE_hAuokVTgQAIJGMuwXAT3WWo5WENMWNYMlmYcrkAAUffhy18OLJhAE1P7zSCXpWQA3-ImRn-sir1fsHHJRaF7NDNnvmvKucMvOWhPOjjGrT3rWCXSKnNHeagS-xxZtbQJV4pX-vaJuq5isgwLVbpPReYLbcZll1LAoiQNDLHU2vjFIpZLJ9tw-XE6EiZXgnRBIE3R5qSjwuemNkXKS1IUK3_xvenqH742IqOQCA3OtNqjECwG5ydWQFEjWbSk6-HRmcPI3JQdmg07ARpfbnmtILhKDzcGAMUBItPifs1z7Gj69OVhPh-NbmkFWrDcpN0TZ4t_ARI-7wcZmGYvpByhuMTCUL-l0y_Bh0xW_uaSPW-EJKYuPW0OtFJCVzNtChmT-aCUQ0Q7D7qNuSWvieCI3buTZHvvwhrD7DD2eH_mcoZncnQd6bR1q_aFnZFH0Lg9SGtRtveSWKGznt1L1tEKvICa4dX5c2_IYHl8cotXBs84op0ksxVbLVjb6XhqW_BcanPpVBEu7vjA8LkkkfguzJusxOR7QYyFbcBvzWrbtn6JUrfW0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f78b96a18a.mp4?token=lSEJVdK_yqHY4xRgzHvXT4c3YnusZDgfF5nSMejMdfKJw0aBFM_ZnKavWWZFccOwosTr5H0JqFABjm4dACe6Uch0DF-NVqG4LxE7oEeV-PhQWJQP6lKF0XoE_hAuokVTgQAIJGMuwXAT3WWo5WENMWNYMlmYcrkAAUffhy18OLJhAE1P7zSCXpWQA3-ImRn-sir1fsHHJRaF7NDNnvmvKucMvOWhPOjjGrT3rWCXSKnNHeagS-xxZtbQJV4pX-vaJuq5isgwLVbpPReYLbcZll1LAoiQNDLHU2vjFIpZLJ9tw-XE6EiZXgnRBIE3R5qSjwuemNkXKS1IUK3_xvenqH742IqOQCA3OtNqjECwG5ydWQFEjWbSk6-HRmcPI3JQdmg07ARpfbnmtILhKDzcGAMUBItPifs1z7Gj69OVhPh-NbmkFWrDcpN0TZ4t_ARI-7wcZmGYvpByhuMTCUL-l0y_Bh0xW_uaSPW-EJKYuPW0OtFJCVzNtChmT-aCUQ0Q7D7qNuSWvieCI3buTZHvvwhrD7DD2eH_mcoZncnQd6bR1q_aFnZFH0Lg9SGtRtveSWKGznt1L1tEKvICa4dX5c2_IYHl8cotXBs84op0ksxVbLVjb6XhqW_BcanPpVBEu7vjA8LkkkfguzJusxOR7QYyFbcBvzWrbtn6JUrfW0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت یک پزشک از ماجرای بارداری دختر ۱۳ ساله
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/691486" target="_blank">📅 17:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691485">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خط لوله ها هم نتوانستند هرمز را دور بزنند
🔹
قرار بود با خط لوله‌ها، هرمز از معادله حذف شود؛ اما اعداد چیز دیگری می‌گویند. مسیرهای جایگزین هنوز فاصله زیادی با ظرفیت هرمز دارند.
🔹
جزئیات را در این ویدئو ببینید
@Tv_Fori</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/691485" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691484">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
منابع خبری عربی از شنیده شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/691484" target="_blank">📅 17:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691483">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be98fe0e5a.mp4?token=BjJvEDmNyDk-s2x1OhHXt4PlzYw9QedAWz0MFHt_Kr5ykNfjt1BcpIrIKSwjZ5ED2Of3PkHmwkJIWzFpTpE77smk-7gNgNKVQPsauiMVo668th1DoloMPWMdHB_uDBhzZ7_e4h6wBjE6wJwYELIXtOrIzB9G3s3vSsI0xOV6WZ-i3rT_3s9jqo0WT8LIZtR_MOPDpjayFosRcuAu9CkLF6rZbkVON1rvpaPr7ihkXpqSmuFFZES0PGxOpecO9bWCEYLD_F4CCm6_aqgapuRYhpPykz9oBjD_0Ee-OEaKBWlUnFgDhr8sENMEBaDW-FzCXPFkaxCg5A35XH-dadvlzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be98fe0e5a.mp4?token=BjJvEDmNyDk-s2x1OhHXt4PlzYw9QedAWz0MFHt_Kr5ykNfjt1BcpIrIKSwjZ5ED2Of3PkHmwkJIWzFpTpE77smk-7gNgNKVQPsauiMVo668th1DoloMPWMdHB_uDBhzZ7_e4h6wBjE6wJwYELIXtOrIzB9G3s3vSsI0xOV6WZ-i3rT_3s9jqo0WT8LIZtR_MOPDpjayFosRcuAu9CkLF6rZbkVON1rvpaPr7ihkXpqSmuFFZES0PGxOpecO9bWCEYLD_F4CCm6_aqgapuRYhpPykz9oBjD_0Ee-OEaKBWlUnFgDhr8sENMEBaDW-FzCXPFkaxCg5A35XH-dadvlzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منابع خبری عربی از شنیده شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/691483" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691482">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzg80iKT5hZ_wptmkRpGoJtLVZTuQ3Co1mNs2cmVhpxcXLlDb36DgfEkFqLae_cuPsw1hRDCRtJEDxvILOn8Feh0xClL_9DOjnD-dhZ3ohGqEV6tURUPT9q4oTzzcTj9PfAKN7ytKK8hrx7UxEvflNsK7pfyAivNDpq_02drt8JgH5pogs-ksYhpu11omB1Oc8tSBFiEcbvY2yyWXz7RabyIFaOU9sMiJCV8W-VPqcEpKOYsgAHGa-ypZxVrA7qwxHVOLFbCenFKiizvRfA3hEW9_XE8QeC2OYwPIEPODBoz1y5uo0fwVJTf83xj4rJ_sj6373fBu1UbhKrfv5BA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بهانه جدید افزایش قیمت خودرو؛ مابه‌التفاوت گواهی اسقاط چیست؟
🔹
قیمت پایه هر گواهی اسقاط خودروهای سواری از ۳۵ به ۶۰ میلیون تومان افزایش یافته و خودروسازان نیز طبق ضوابط جدید باید به‌جای یک گواهی، ۱.۵ تا ۲ گواهی برای هر خودرو تأمین کنند؛ موضوعی که هزینه خودروهای صفر را افزایش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/akhbarefori/691482" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691481">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6aa19afc6.mp4?token=f59hDdjAOHfFt8oAtPmaChF70UNigFyRrbwqd1HC5Ku603rcVOZDHN1NC3tmfkjn8U-g67B0bLi6npGkhDdWCb3a1a-Oc591NvqdvrxTUYdH3G3szURImi7KYbmAGGBZROD-A9AIUUp8a6KQp0kUrVLv6SNux6HgY9sb90wAFh8WHXL4y0hCC1fxL61f5IfYPkbJOdezkzPTwjrIGftOJfwsi-qFRZoism-xsAQ77iA23qLjESSb_tdpzqqq9vr2Gw0tbMf-5smoLBGj5YIWLGljsaxJPwlbqS6RqI3gOqqE78-MhDJjWoQ45x1M98WPerhamVrf8iTvLutPz-52YRIdwUe8fybkp-AgzWhNiP6DC_lObb8xYi1-fJWfkrfXaAT_FK-kGvYBm6NW6b0ykf9iKlgbgtQEmQuMKGiK-BEQX4Uc3_R7kG_OilzOHVMQGcEyEX4ecCQdDDydIUpYaKq9tmCff9BGCMPouSsfWv8mLrTgPknGRYeedrLHVhROEWOLqrgimNABQRS4-CzkC5OvfqppacgOxF9JK0zgzV3Mqyby0M7KVw0q6d_Zf14YnbCOolnZh4cAydcdDAFvwrfpJPW8fpL3dAG4GDGnS29Vyhn4p5sK5CPZzzmaAlN7JlIZFasN7HGWq4y7oYKLM_cAHlACg7TJO9kMevbUvTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6aa19afc6.mp4?token=f59hDdjAOHfFt8oAtPmaChF70UNigFyRrbwqd1HC5Ku603rcVOZDHN1NC3tmfkjn8U-g67B0bLi6npGkhDdWCb3a1a-Oc591NvqdvrxTUYdH3G3szURImi7KYbmAGGBZROD-A9AIUUp8a6KQp0kUrVLv6SNux6HgY9sb90wAFh8WHXL4y0hCC1fxL61f5IfYPkbJOdezkzPTwjrIGftOJfwsi-qFRZoism-xsAQ77iA23qLjESSb_tdpzqqq9vr2Gw0tbMf-5smoLBGj5YIWLGljsaxJPwlbqS6RqI3gOqqE78-MhDJjWoQ45x1M98WPerhamVrf8iTvLutPz-52YRIdwUe8fybkp-AgzWhNiP6DC_lObb8xYi1-fJWfkrfXaAT_FK-kGvYBm6NW6b0ykf9iKlgbgtQEmQuMKGiK-BEQX4Uc3_R7kG_OilzOHVMQGcEyEX4ecCQdDDydIUpYaKq9tmCff9BGCMPouSsfWv8mLrTgPknGRYeedrLHVhROEWOLqrgimNABQRS4-CzkC5OvfqppacgOxF9JK0zgzV3Mqyby0M7KVw0q6d_Zf14YnbCOolnZh4cAydcdDAFvwrfpJPW8fpL3dAG4GDGnS29Vyhn4p5sK5CPZzzmaAlN7JlIZFasN7HGWq4y7oYKLM_cAHlACg7TJO9kMevbUvTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تراژدی تلخ گردشگری ایران؛ جذابیت در بین برترین‌ها، درآمد تهِ جدول!
محمد درویش، کنشگر محیط‌زیست:
🔹
ایران از نظر جذابیت‌های طبیعی جزو ۵ کشور اول و از نظر جذابیت‌های تاریخی و فرهنگی جزو ۱۰ کشور نخست دنیاست، اما در کسب درآمد از این حوزه‌ها حتی در میان ۱۵۰ کشور اول هم قرار ندارد./ تلویزیون اینترنتی مدار
گفت‌وگوی کامل در یوتیوب
👇
https://youtu.be/uH-2rlDLEnw
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/691481" target="_blank">📅 17:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691480">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de4dd6b96.mp4?token=kUwMqMH_fNrQAcrJtrA7aaOYtD9deBVzu1_WnXXPZeucTKnACc85AylqFbsmxlWoSHHqLunnRRC07ZnCHsgEUX1ukJ0n57_5an_ofA90XQBwFbvM-zfg82ATbaGmzC5IRBA14Euqc55KwcgaB4zGClG3NgoB2j6F9_NN_UkKrRTx3qZhny-6QP34oMZYVWezCNOnWFjLvDMxmEpeJIbi_mTWEQ9PjzanCS9NqEPsKKIeByTazFha1qKkQIavb57RrWpDr5tpTI5PzIkPXSsh3zDygvBUdqMZwznw5JWTDtfUUW2S9I36WK22ATm7iW3n2NBuOmy9Xnq4FmTY9YrRkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de4dd6b96.mp4?token=kUwMqMH_fNrQAcrJtrA7aaOYtD9deBVzu1_WnXXPZeucTKnACc85AylqFbsmxlWoSHHqLunnRRC07ZnCHsgEUX1ukJ0n57_5an_ofA90XQBwFbvM-zfg82ATbaGmzC5IRBA14Euqc55KwcgaB4zGClG3NgoB2j6F9_NN_UkKrRTx3qZhny-6QP34oMZYVWezCNOnWFjLvDMxmEpeJIbi_mTWEQ9PjzanCS9NqEPsKKIeByTazFha1qKkQIavb57RrWpDr5tpTI5PzIkPXSsh3zDygvBUdqMZwznw5JWTDtfUUW2S9I36WK22ATm7iW3n2NBuOmy9Xnq4FmTY9YrRkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زیر گرفته شدن فوتبالیست انگلیسی توسط خودروی چمن در طول مسابقه‌ در تایلند
😳
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/691480" target="_blank">📅 17:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691478">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e978e35310.mp4?token=i3CH_Dti88NoeqvAFMeAue_X9dvYZwFehjifc81FOJZIlMlMUDVHIqft1UD00GStWbgTSoSibJYHhd9OriSbPz3FsE3YUNALeXiqJJ7nGTdO9sCfouu7rauraKBnG2VA9aZf1F2I3nqkqeCgrV_bAOCz4kfaY9hRZSRAqZxAYcrv2YeMj4_BAx4A78fqsIK-TMvItWTAFcKDewYZpAhbYL-fJIb7AmRCe-pBNeIYR2Yh0chL8FA1DeUjlBigF_HR4Ts6oBgWe_UqMQIeumDlrmKGup5bkaEOyxOSsSvqAqRxIAKdYZkXLXbHsu30Stwu_FADhaIRbaPTzRF3ei0Hqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e978e35310.mp4?token=i3CH_Dti88NoeqvAFMeAue_X9dvYZwFehjifc81FOJZIlMlMUDVHIqft1UD00GStWbgTSoSibJYHhd9OriSbPz3FsE3YUNALeXiqJJ7nGTdO9sCfouu7rauraKBnG2VA9aZf1F2I3nqkqeCgrV_bAOCz4kfaY9hRZSRAqZxAYcrv2YeMj4_BAx4A78fqsIK-TMvItWTAFcKDewYZpAhbYL-fJIb7AmRCe-pBNeIYR2Yh0chL8FA1DeUjlBigF_HR4Ts6oBgWe_UqMQIeumDlrmKGup5bkaEOyxOSsSvqAqRxIAKdYZkXLXbHsu30Stwu_FADhaIRbaPTzRF3ei0Hqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی ترامپ قمارباز: گزینه‌های روی میز فعلی، محو ایران، فروپاشی اقتصادی آن یا دستیابی به توافق است
🔹
سوال من این است که چه زمانی و آیا کل ایران را منفجر خواهم کرد یا خیر، و بهتر است خودشان درست رفتار کنند. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/691478" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691477">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتامین مالی جمعی رضوی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLP5X1TPHzql_1GWfb4VIsz-QkFpwVl2DxSr0xEJOdro4fde54PJ_ZIRrlc2pC7S9zQVrum_qz_JBYkWRfyARV92AiJyDs7PzCWvC0gPcO-p_3zrMbGcEogZ0uCjLl4WTBmWC6kPwcnAwZr0mCUBqnL8e9LVBAmWRrD3tzcHtPeeVAf0pnkItwpq8fTYn1zYVopzY9HNSFu5WKMA8OGujrEqvUQr0BCpfsFEjMmuT0QTB1dPildfqc4EI_fQxObw8LzbpP25YlQZCvdSk8gzne1NrT8YYs2gEXSCKrMFS7eEY_ZZ994E6aAwcvDaT4d9dn2IUI-MP_SBYTuR0FoSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
همراهان عزیز سکوی رضوی،
فرصت سرمایه‌گذاری در طرح ارائه خدمات آموزشی تخصصی زبان های خارجه آغاز شد!
✅
سودپیش‌بینی شده:
۴۶ درصد یکساله
(پرداخت ۳ ماهه)
✅
دارای
ضمانت تعهد پرداخت
بانک ایران زمین
✅
شرکت تعاونی راشد جوان مبتکر
🌟
سودمندانه اعتماد کنید…
کسب اطلاعات بیشتر و سرمایه‌گذاری:
تلفن تماس:
05191008000
سکوی تامین مالی جمعی رضوی
cfrazavi.ir
آدرس ما در فضای مجازی:
تلگرام
بله</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/691477" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برنامه‌های «شفرونی» و «روشن» با دستور قضایی رفع توقیف شدند
🔹️
پس از اعلام جرم ساترا علیه برنامه «شفرونی۲ » در ۲۱ شهریور ماه و دستور دادستانی مبنی بر توقف پخش، امروز حکم رفع توقیف این برنامه صادر و «شفرونی» می‌تواند از همین هفته پخش خود را از سر بگیرد.
🔹
ساترا در شکایت خود به دادسرای فرهنگ و رسانه، انتشار بدون مجوز و محتوای غیراخلاقی و خلاف عفت عمومی را عامل درخواست توقیف برنامه عنوان کرده بود که با حضور تهیه‌کننده برنامه در دادسرا و ارائه توضیحات و مستندات و انجام برخی مراحل قانونی، دستور رفع توقیف «شفرونی» صادر و به پلتفرم پخش‌کننده و ساترا ابلاغ شد.
🔹️
همچنین برنامه «روشن» نیز با استناد به قانون مطبوعات و آیین‌نامه‌های اجرایی آن مشمول موارد ادعایی در شکایت ساترا نشد و دستور تداوم پخش آن نیز صادر شد.
Asriran.com
@MyAsriran</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/691476" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ادعای ترامپ: احتمالاً آماده دیدار با مسعود پزشکیان، رئیس‌جمهور ایران، در حاشیه مجمع عمومی سازمان ملل موافق خواهم بود #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/691475" target="_blank">📅 17:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1e18660f7.mp4?token=g-xBROToyQTZMq4E-CldrkKzagPl8doHc_DMSKnQrVuPNNu8yAOdCck-DLF_oxw1Zf_o6cPiSQ8UpC6TAuXyLC5-542kiwxoFQcuf2cck_hE7aBEmtsX8F7vx65iV1Cz1GgN0s7v20t23rdqvhBr28lOfUnAB5C1nGFfGMkxk7jNNiQedjGUdtsXD9V5R5C6OvYIVzw1zIr_cz81kskLlce4RvPsnQ9U_e7RjawP49AqHp2oP78A23cQrHN-yKOCuQ7azHTENRkjH-P4SR82BSv8q8Jp9FQQm_Io62U5YEcEnZsyZDzE4ZRHlK2DO7C1xKkaX3JftUB31LYib9zg4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1e18660f7.mp4?token=g-xBROToyQTZMq4E-CldrkKzagPl8doHc_DMSKnQrVuPNNu8yAOdCck-DLF_oxw1Zf_o6cPiSQ8UpC6TAuXyLC5-542kiwxoFQcuf2cck_hE7aBEmtsX8F7vx65iV1Cz1GgN0s7v20t23rdqvhBr28lOfUnAB5C1nGFfGMkxk7jNNiQedjGUdtsXD9V5R5C6OvYIVzw1zIr_cz81kskLlce4RvPsnQ9U_e7RjawP49AqHp2oP78A23cQrHN-yKOCuQ7azHTENRkjH-P4SR82BSv8q8Jp9FQQm_Io62U5YEcEnZsyZDzE4ZRHlK2DO7C1xKkaX3JftUB31LYib9zg4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ممکن است به زودی اتفاق  بزرگی در مورد ایران اتفاق بیافتد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/691474" target="_blank">📅 17:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای ترامپ: ممکن است به زودی اتفاق  بزرگی در مورد ایران اتفاق بیافتد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/691473" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=ZhsLP5_dF3bWS02JSppbLT3nKiHlQ8Ynm7SE8zlYCglOQh6zyEH8TBks-ri3GFG-bH0MnYe0gbatXoPpZD1eVdczS6bhVHq_2AiMv-lg5YMg4aeBYVcij5n0DdDWPRe7Y7qdF53ZYGTGd27Z0KCV0oF75m1u8HRwPhCVnzkyJDUt9F0bjragaJYnoe8JyqQ3St0GypbdsT2toX3bPimy-iQZ-83hYf3rMR0aySBRSDOQ6_7PNO2FgTcR5qrvG7k2okmmg59bI3G3TfABXmc7wo8Ef4-LqZSEIwZ5PtU-WzUyn1Bm0PIv1oacQJhcsltxNDmkP2guBkIFPCSDOs0fwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=ZhsLP5_dF3bWS02JSppbLT3nKiHlQ8Ynm7SE8zlYCglOQh6zyEH8TBks-ri3GFG-bH0MnYe0gbatXoPpZD1eVdczS6bhVHq_2AiMv-lg5YMg4aeBYVcij5n0DdDWPRe7Y7qdF53ZYGTGd27Z0KCV0oF75m1u8HRwPhCVnzkyJDUt9F0bjragaJYnoe8JyqQ3St0GypbdsT2toX3bPimy-iQZ-83hYf3rMR0aySBRSDOQ6_7PNO2FgTcR5qrvG7k2okmmg59bI3G3TfABXmc7wo8Ef4-LqZSEIwZ5PtU-WzUyn1Bm0PIv1oacQJhcsltxNDmkP2guBkIFPCSDOs0fwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نویسندۀ آمریکایی: ما از منطقۀ غرب آسیا بیرون رانده شده‌ایم؛ به این معنا که پایگاه‌های ما دیگر کارایی ندارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/691472" target="_blank">📅 17:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80061ce38a.mp4?token=TqaR2EADI0qW1KLgdAFvQT81OAjy4QgjVnHQ47Ay0Ck8tRnbdEp_iFYFgZ85sqmhItKRnqADToGW9Fs8rs3U4GKutWoiFcWF7DJUuIVvLrhN0_ohiSaqfbbVpnpnSBtY7RxuOZusRgLKExIEkG2gXkE-vT_gjrBOKfmdXwtg_aJ7AJYAaC-vv7-biPV9Q-hbg-isV_uMMbFFUEdtClRJ4aO49jm5hH-0vwUQN_5SbDcTNJVWl0nmxncs8-iw3qx_BhIR-51asUgSjm98ZVpyYxSEQv0LFlgC0AyXDd11EcLHbcxuhhN-eqmP6KUQ8x_2OeaEvCm8XtZtfFGt-M8PUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80061ce38a.mp4?token=TqaR2EADI0qW1KLgdAFvQT81OAjy4QgjVnHQ47Ay0Ck8tRnbdEp_iFYFgZ85sqmhItKRnqADToGW9Fs8rs3U4GKutWoiFcWF7DJUuIVvLrhN0_ohiSaqfbbVpnpnSBtY7RxuOZusRgLKExIEkG2gXkE-vT_gjrBOKfmdXwtg_aJ7AJYAaC-vv7-biPV9Q-hbg-isV_uMMbFFUEdtClRJ4aO49jm5hH-0vwUQN_5SbDcTNJVWl0nmxncs8-iw3qx_BhIR-51asUgSjm98ZVpyYxSEQv0LFlgC0AyXDd11EcLHbcxuhhN-eqmP6KUQ8x_2OeaEvCm8XtZtfFGt-M8PUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسن روزی‌طلب، معاون سابق صداوسیما: ادعا شد در حوادث ۱۸ دی صداوسیمای شهر کیش سقوط کرد و تسخیر شد/ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/691471" target="_blank">📅 17:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
صحبت‌های تلخ محمود بصیری پس از مدت‌ها؛ تلویزیون بیننده ندارد، من برای کی بازی کنم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/akhbarefori/691470" target="_blank">📅 16:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691468">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d52c097554.mp4?token=lAHh4ZsVK4AgSZpZw-Ef2p4muBr6nsmhuTFlIdfT8ClmTLIU6lCmDXP7GxzisgE1CZ0NAe7aNNbMWk5ebgWZKV3dEu3Q38hnfxozgBGkZWR1_IJrizS8fR9_qSjymL_mov8gzLzLHZfkdNGc_nE_IQ_BxxePGlLDFsFOR5EI4RooUf9BIwcrHnVw7zLvnSrPArRGz-puu6AJLDUIC3l9w_77ZSIK4_j-xOwlU6GIr3cwl1TF-V0vJ2jF2ap4tmWvOCOMc1YoIQ7zypEZIbTUBNNExfwp8ncQAehi622nQG4KbSCZNMTYOAtljMqjgyVHrE_e4dUmCxrcU56Dx9N3cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d52c097554.mp4?token=lAHh4ZsVK4AgSZpZw-Ef2p4muBr6nsmhuTFlIdfT8ClmTLIU6lCmDXP7GxzisgE1CZ0NAe7aNNbMWk5ebgWZKV3dEu3Q38hnfxozgBGkZWR1_IJrizS8fR9_qSjymL_mov8gzLzLHZfkdNGc_nE_IQ_BxxePGlLDFsFOR5EI4RooUf9BIwcrHnVw7zLvnSrPArRGz-puu6AJLDUIC3l9w_77ZSIK4_j-xOwlU6GIr3cwl1TF-V0vJ2jF2ap4tmWvOCOMc1YoIQ7zypEZIbTUBNNExfwp8ncQAehi622nQG4KbSCZNMTYOAtljMqjgyVHrE_e4dUmCxrcU56Dx9N3cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
منوی سه‌بعدی؛ ایده‌ای متفاوت برای سایت رستوران
🍔
🔹
می‌توان به‌جای منوی معمولی، هر آیتم غذایی را به یک صحنه سه‌بعدی و تعاملی تبدیل کرد؛ ایده‌ای جذاب برای منوی رستوران، معرفی محصول و کمپین‌های برند.
🔹
این مدل اجرا برای Restaurant Menu / Product Showcase / Brand Campaign واقعاً جذابه چون خود طراحی چاپی رو تبدیل می‌کنه به بخشی از تجربه کاربری .
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/akhbarefori/691468" target="_blank">📅 16:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691467">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt9KQpMX7NL6Xdyx3RzM379RbhFta4HodB_D0cSDq9023AZ1wEVvMs6wuPuWmzXkgTNhN7seljxEwTdyDgwhjyhbQJ_llLb-pH1uHBrL5hjnE2BC8Q0Vi2hdIG8KUzZAThMFD-1cxkylDJT-U7SYinJbnZ24EMHMA6aUwWz5JsTXBCPnBP8tatgUiNNipSTlbog3bp4rzIOmg2c2y4kQqCmDz72qhASRQGuVE241xThK7tyE_NDfLaNZh2XyAid5BG0PiJxob58BxUB1lUPPPfEvlyZ6c_sy3-cYHgCB9JqFFKl0t6db0NAgvLdIyhQlnFoUb13coaEuEQORcFHudg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کارخانه‌ها روشن، بازار خاموش | لوازم خانگی؛ صنعتی که نباید قربانی واردات شود
🔹
صنعت لوازم خانگی ایران در سال‌های اخیر یکی از معدود بخش‌هایی بوده که توانسته از دل محدودیت‌های اقتصادی و تحریم، مسیر تازه‌ای برای توسعه پیدا کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3246628</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/691467" target="_blank">📅 16:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e6167b311.mp4?token=J6Qv6hGv3fR9GBeINpkby0p2vgCwbxiyJS1qEJubC_T2n9fYqFkQjai6fQ7U2Gqjw_xOYRKVstkLas5-cYpmmYSQVpQMGufF8UPzh6AbnDotN0x2keEydhb3Ja1azvRKKu90UlBCqyIzWAwpDsvufEwqG3h9iXU18A9Cvl5jB5lybXV7snL3APxTVSCXayjotfIEFeeBHYPqreypuJH6Pc3kgXGsLVyGzRT7H91FCN_9XxF4To74zTaHS0jq59mcdycgoCRB6tLXp_FJqPfpu5lEvEmOlUfTM5-MvHc4ZSrUy38g0Jd6UNPMhDk2EYFpOV3eA47ZetKxc-CxZeXylQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e6167b311.mp4?token=J6Qv6hGv3fR9GBeINpkby0p2vgCwbxiyJS1qEJubC_T2n9fYqFkQjai6fQ7U2Gqjw_xOYRKVstkLas5-cYpmmYSQVpQMGufF8UPzh6AbnDotN0x2keEydhb3Ja1azvRKKu90UlBCqyIzWAwpDsvufEwqG3h9iXU18A9Cvl5jB5lybXV7snL3APxTVSCXayjotfIEFeeBHYPqreypuJH6Pc3kgXGsLVyGzRT7H91FCN_9XxF4To74zTaHS0jq59mcdycgoCRB6tLXp_FJqPfpu5lEvEmOlUfTM5-MvHc4ZSrUy38g0Jd6UNPMhDk2EYFpOV3eA47ZetKxc-CxZeXylQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی عجیب از آواز خواندن آقای دکتر در اتاق عمل!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/691465" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f97800973.mp4?token=Sb4wOCdyPUgMNinQTuaCc295j4SkB1M1TqA1G0jDOVlsd85B_YpW-Yub6WZEbQx_NBA798cX1KnjTWZWOr-reg6x6SqrRTZLL5vrDBd2uMUz2pJpRotHHMW7xbE8AVoRgnUDnFP_TrQHu6zPix1kY34h_yK9575bD2TkHqr2d3Q5aNwWcVGdwesOjVCBnoQfCALn6A5n8MhPlhL6Qannx3WhPglAqIFwj4PszbtsTqI-9zx-4YmdYfZbeD5aLCDLR8d9Vh4YyPzX6QdGTOwFwjiAomz75MaqBytbWr_4O6KfuENIorFbSAiOHMp6pJMSwOhRsHSky0lgTINjnBHqQidtDkmCNIJz9w3lnFmdff8R_1vOGsY3d3KcflzcRCk4CKpzixUF4YEVkb2IUVVM5uGIM8ayQ-qIpaHHVqO9MgR9OIOXvavnsUVClVDeWxkyLR6V8Jc2ep0F7xRRH4PTdyekXQ4yGrfDn0qm-VoywkbfCM9XawPt6TLJ-0IUcBY7dUYRSiCGdvo9gMxKFpUOgIG2rH0XQqPiljev9IKyp_tograe9lqU0dX3ID6gr7Qczb-6uUErh0LTFP6jThUcWtBCWgFSyYMNEUykVrBIH-19veMsBqkhwGYdvmdLwwUZyTX_8oRaoCQKxF3EGo8Q2geFzAqoxpNwZPB82BF_SJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f97800973.mp4?token=Sb4wOCdyPUgMNinQTuaCc295j4SkB1M1TqA1G0jDOVlsd85B_YpW-Yub6WZEbQx_NBA798cX1KnjTWZWOr-reg6x6SqrRTZLL5vrDBd2uMUz2pJpRotHHMW7xbE8AVoRgnUDnFP_TrQHu6zPix1kY34h_yK9575bD2TkHqr2d3Q5aNwWcVGdwesOjVCBnoQfCALn6A5n8MhPlhL6Qannx3WhPglAqIFwj4PszbtsTqI-9zx-4YmdYfZbeD5aLCDLR8d9Vh4YyPzX6QdGTOwFwjiAomz75MaqBytbWr_4O6KfuENIorFbSAiOHMp6pJMSwOhRsHSky0lgTINjnBHqQidtDkmCNIJz9w3lnFmdff8R_1vOGsY3d3KcflzcRCk4CKpzixUF4YEVkb2IUVVM5uGIM8ayQ-qIpaHHVqO9MgR9OIOXvavnsUVClVDeWxkyLR6V8Jc2ep0F7xRRH4PTdyekXQ4yGrfDn0qm-VoywkbfCM9XawPt6TLJ-0IUcBY7dUYRSiCGdvo9gMxKFpUOgIG2rH0XQqPiljev9IKyp_tograe9lqU0dX3ID6gr7Qczb-6uUErh0LTFP6jThUcWtBCWgFSyYMNEUykVrBIH-19veMsBqkhwGYdvmdLwwUZyTX_8oRaoCQKxF3EGo8Q2geFzAqoxpNwZPB82BF_SJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرتاب کفش به تصاویر ترامپ و نتانیاهو در کره جنوبی
🔹
حامیان فلسطین در سئول در اقدامی نمادین، کفش‌هایی را به سوی تصاویر ترامپ و نتانیاهو پرتاب کردند و اعتراض خود را به جنایات این دو نشان دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/akhbarefori/691464" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
پنجشنبه‌ها در استان قم تعطیل نیست
معاون توسعه مدیریت و منابع استانداری قم:
🔹
خبر منتشرشده درباره تعطیلی پنجشنبه‌های دستگاه‌های اجرایی استان تا پایان سال صحت ندارد.
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/691463" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f20de068bb.mp4?token=d1JX22ZM0bO7adilZhZQilYMS_Y5usmTl8y6tEiR55l04FPCt2b4Lvj7yuE3-NWVutEJJNAzXdnsOnYExGE9hgU8Ewz2qBKYaZ70xCauJ2lvaqkaetyTtG92COvR4Vkmdo7KQCP2lA0Mnw3WS7JD_6J0tj89zNAJgXPLfDXzaCdPB4ou4iu9ZC0rF3LEocxKvaW7q0I8XNTBC_WEidouwky-Hfxz3uQ9lOk1DPh9PU_df3G_925w35dpq6I1N81t2zjCVy5JgSNy8Se7b4wAs6f6vlhzdx1XYWKZYEe48p85k-S1M41Tmwh1NRd4jfkR8-QXZiu1hVZUbx1CJc7gHjfT0SevryPmMUwNPNzdxNUI0lFxP-pr7W7J6qvFKviCfb9AOVikC_8EF8DLs4Lj4mdacMcWQV5cZvboGE2nj8gkAxuBtUdh_U9O2YEF_gWJ1m9HwsI4gOpaLB1U5dHbg4wk64I8k6FYXtlYj_THtSVDxJ-zHTotOnL_0Udk2rEfaRci-gdSDKMpDIWCF8QaT7CGhkvetvzcb_NyHRg1BNv6F31tWp6e-lKxW-krjIMytAwauQMKCzZeGYWPbKTbdLIr7Hx5tQrk8krP7ozZnj7GrAp_STmW4wjgG62vbCCary4jVYD67-rxGiv8sTH8VK-PL8-jHCXNXtfe0Z6gqcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f20de068bb.mp4?token=d1JX22ZM0bO7adilZhZQilYMS_Y5usmTl8y6tEiR55l04FPCt2b4Lvj7yuE3-NWVutEJJNAzXdnsOnYExGE9hgU8Ewz2qBKYaZ70xCauJ2lvaqkaetyTtG92COvR4Vkmdo7KQCP2lA0Mnw3WS7JD_6J0tj89zNAJgXPLfDXzaCdPB4ou4iu9ZC0rF3LEocxKvaW7q0I8XNTBC_WEidouwky-Hfxz3uQ9lOk1DPh9PU_df3G_925w35dpq6I1N81t2zjCVy5JgSNy8Se7b4wAs6f6vlhzdx1XYWKZYEe48p85k-S1M41Tmwh1NRd4jfkR8-QXZiu1hVZUbx1CJc7gHjfT0SevryPmMUwNPNzdxNUI0lFxP-pr7W7J6qvFKviCfb9AOVikC_8EF8DLs4Lj4mdacMcWQV5cZvboGE2nj8gkAxuBtUdh_U9O2YEF_gWJ1m9HwsI4gOpaLB1U5dHbg4wk64I8k6FYXtlYj_THtSVDxJ-zHTotOnL_0Udk2rEfaRci-gdSDKMpDIWCF8QaT7CGhkvetvzcb_NyHRg1BNv6F31tWp6e-lKxW-krjIMytAwauQMKCzZeGYWPbKTbdLIr7Hx5tQrk8krP7ozZnj7GrAp_STmW4wjgG62vbCCary4jVYD67-rxGiv8sTH8VK-PL8-jHCXNXtfe0Z6gqcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلایه شهروندان نطنزی از تأخیر در رسیدن آمبولانس/پاسخ بحث‌برانگیز اپراتور ۱۱۵/تأسیسات هسته‌ای نطنز در نزدیکی این شهر قرار دارد!
🔹
تأخیر بیش از ۳۰ دقیقه‌ای در رسیدن آمبولانس به محل یک حادثه در شهرستان نطنز، موجب نگرانی و اعتراض مردم شده است.
🔹
بر اساس ویدیوی منتشرشده از سوی یکی از شهروندان در تماس با سامانه ۱۱۵، پاسخگو اعلام کرده که آمبولانس در مأموریتی در سرآسیاب است. شهروند معترض نیز نسبت به وضعیت امدادرسانی و تأخیر پیش‌آمده اعتراض کرده که بنا بر این روایت، اپراتور در پاسخ گفته است:
«بدبخت اورژانس! اشتباه می‌کنند خدمات رایگان به مردم می‌دهند»
و سپس تماس قطع شده است.
🔹
در ادامه این روایت آمده است که با ۱۱۲ هلال‌احمر نیز تماس گرفته شده، اما اعلام شده امکان اعزام نیرو وجود ندارد.
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/akhbarefori/691462" target="_blank">📅 16:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb09df83f7.mp4?token=tvi9CQZhSfbVzBINlHDnyJUF4H5d6mWRI2pxZwsKuXA4wEjkIcA6Mtk-SkuGeX3FrDfqgdat5HdFRaezwp4vXf8T8HnjRj-cvgblS-HR2D35ydZ5L-1P4HogaVECBB0KIgS5lv4v-VngY7kO3krGbefQhq3dpYpmOWDAtB8L_hMAN8_aNPXDQs2qFv6LNYCx2TBYFr4-rnt1IIDFVQrz7HFQn-sjnrSu97TG1zl0EYTlc7oP1-L5NIxrrflLjZ1XEdmbuH0HxfJSLpB2d-qYtZCmOxBNEIZrDj7WIQvnYmMnIznIvoavnSZtANFK12U8IHrkLQVKFP5SPtVK8NTtgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb09df83f7.mp4?token=tvi9CQZhSfbVzBINlHDnyJUF4H5d6mWRI2pxZwsKuXA4wEjkIcA6Mtk-SkuGeX3FrDfqgdat5HdFRaezwp4vXf8T8HnjRj-cvgblS-HR2D35ydZ5L-1P4HogaVECBB0KIgS5lv4v-VngY7kO3krGbefQhq3dpYpmOWDAtB8L_hMAN8_aNPXDQs2qFv6LNYCx2TBYFr4-rnt1IIDFVQrz7HFQn-sjnrSu97TG1zl0EYTlc7oP1-L5NIxrrflLjZ1XEdmbuH0HxfJSLpB2d-qYtZCmOxBNEIZrDj7WIQvnYmMnIznIvoavnSZtANFK12U8IHrkLQVKFP5SPtVK8NTtgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا حباب صندوق های اهرمی در بورس منفی است؟
@Titretejarat</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/691461" target="_blank">📅 16:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691459">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
انتقال جنسی، شایع‌ترین راه انتقال HIV در سال‌های اخیر
رئیس مرکز مدیریت بیماری‌های واگیر وزارت بهداشت در
#گفتگو
با خبرفوری:
🔹
انتقال جنسی در سال‌های اخیر به شایع‌ترین راه انتقال HIV تبدیل شده است. او همچنین اعلام کرد وزارت بهداشت آمار بیماری‌های مقاربتی در میان دانش‌آموزان را در اختیار ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/akhbarefori/691459" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691458">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
فرانسه: دو دیپلمات ایران طی روزهای آینده اخراج می‌شوند
🔹
وزیر امور خارجه فرانسه در پیامی در شبکه ایکس ضمن حمایت از اغتشاشات دی‌ماه نوشت که قصد اخراج دو دیپلمات ایرانی را دارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/691458" target="_blank">📅 15:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-691457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
شمارش معکوس تا انتخابات آمریکا و اسرائیل
🔹
انتخابات میان‌دوره‌ای آمریکا ۳ نوامبر ۲۰۲۶ برگزار می‌شود؛ از امروز ۴۴ روز باقی مانده است.
🔹
انتخابات رژیم صهیونسیتی نیز برای ۲۷ اکتبر ۲۰۲۶ تعیین شده و ۳۷ روز تا برگزاری آن باقی مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/691457" target="_blank">📅 15:55 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
