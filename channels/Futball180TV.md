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
<img src="https://cdn5.telesco.pe/file/tS9HPWfA7Ikzxf5PPvdCp6RYUyh-gAGuq4iTc_HDSOV-avpnosRA_giQAEOYq-be6o-S8oSfEz2-AnAk8cMIDWP0Y1CvqmHm0ogUDBCWdGpHIuTY-241vwuJSu_EREUL_7PIobSvLgj0ECr0ZrKkbnNGx8T2ofthoZAOl8NzxIqvZNQVh6_aWjbo8pwRVVYgSkTnU-ZiOwilyyzkB84YskQKVzaRTULg9qzN9X8wvNOxqPGuKKgqz-Jcso5CLFaer5xaij9GBKTOR039lJfOwYZEggPYkN9QuJWIK_fkleogQ3ICjLkrdT0EBHrJPZhS94OntIRiAjqS0J7TYe2BzQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 434K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 20:38:04</div>
<hr>

<div class="tg-post" id="msg-105202">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
اعلام جزئیات بلیت‌فروشی دربی ۱۰۷
🇮🇷
🇮🇷
بلیت‌فروشی دربی از امشب آغاز می‌شود و سهمیه هواداران استقلال و پرسپولیس ۵۰-۵۰ خواهد بود.
🎟️
ظرفیت در نظر گرفته‌شده برای هواداران: ۳۵ هزار نفر. سامانه بلیت‌فروشی که فروش از شب شروع میشه:   https://ticket.sepahansc.com…</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/Futball180TV/105202" target="_blank">📅 20:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105201">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb_uhU_VOcPrEPaF_M21xM6GU57f2SlIO1YHxaw9JFIG1kUo34-Fx-G0i_psWf1WELad70nZojHHHH76Md75QEHEbChEGBLIiHpiWks0O1r3U7e0FsSACx4C-DD7L6O82O58nLvF16mzTE5EndB4OASfhuwbKx0vksLye4aGy0SRQML2DlbvGM2D8txzwxMQNTjnlF1lqEJvfRQiT3GxYMBI1FTrVVa4nFoGKROR1lzQKGbZqtfXWUkeWilpeUTtyqp01cS1PdsY9OYxrtgrHIm0AYL_tvVdxCGaBY2jVZ_58pgVqepXEamJ5KHiQ1JHOrH-_2aB_jzZqOV8StMVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
در نشست امروز کمیته داوران، موعود بنیادی‌فر نظر منتخب اعضای این کمیته بدلیل تجربه بالاتر نسبت به کوپال‌ناظمی بوده و قرار شده قضاوت بازی روز چهارشنبه که حواشی بسیاری خواهد داشت، به بنیادی‌فر واگذار شود تا بازی به درستی مدیریت شود. هنوز تیم داوری رسما…</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/Futball180TV/105201" target="_blank">📅 20:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mp6bamTBshMfv8Ogl3NmuSVKeta8iJ2q0QW97Ek9GVEXDFarBfwGJ2gRSaSrTqBIGRalmWKTJQZfMa_e7HRQv-2OtIljoxS6BkgUTmvu3Du60E2OgAv50y59LdgZhyPYxqzNx1AeNHDW7HHBaU0YV5xAOl4rtNRyD9mfoTxA1P1AsjQSpvGiowyms8AwQlKStwtdU873cYJ27oP_z6nF8rYvhroEyUn1RN2vv6tvT_QM24ukPgEyWoYL-Sq87_ZmOSpwHuxw8O01yrchahqzNtL52fx90R0lajND9qa2QibyNDM8qGsXGqp8MUetDxsJaEIhG4bbZwGpCEcQ1WaQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😃
قدرت دوس‌دختر در بازی دیشب رئال‌مادرید:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/105200" target="_blank">📅 20:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=sYCsRb3IibVrnLlYff3AuDQ2BFazbPK26xl4sPZPI9rNZXSNFpSQNhbnTwU1XClznnv64KQhIzXFvaEuzC4JDHyILhL6TOzvn9_70omZqmkW0nhvTzGN_qNuX-Aw-K1fe89iQXi0befJGEZInWZClN3gsqW0G-H0u_MtNeFEigFrkb5LvL5WVjRpdh03W9qUCFgwvIMdZ1H5atmhQpC_f-AdCr1LbMz9a5-Pxer_0frgvgs2t__NwGdKqeO4KGa13pKkp1oKpXacEPf-8PPdxBEe0AYFP8UULqufX39U8wzoD2q6kB8Qn2VzcUzxR-Z9dnyO8XPKZye1RxtZy6vVpItLSXfjQ4CVSuS4UnIcNWBigXE0W4dT96Aw_C_oaf9T9a53KxEhsl46tz1cd-QRmhREsYVxU4AQpHia_dBTrhzDCak7cyxgy-oV2BHXzLNdejcklf4Qqg6YBQYtTrAEKZbwAOga00IyPVQEV7IzcOzhJr9Z-8_TVG8Uq_AFFv1E-bAIWK8Fk9qSf4rSGK8lPm5YZBobT3PGdOZAGOJxg7fwSlxH9RMhT40ZzjvXIUlY1iCop9g963MhDtZ3NXOMkljaC51xQL4vSF4LO_FycTze5op5Fa5BQsc6Rqb2kLooiXFDa_b3ZLKaPoxGP5VXUd1Fee0J7MBqqt9N1dGjGE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cb7444c7.mp4?token=sYCsRb3IibVrnLlYff3AuDQ2BFazbPK26xl4sPZPI9rNZXSNFpSQNhbnTwU1XClznnv64KQhIzXFvaEuzC4JDHyILhL6TOzvn9_70omZqmkW0nhvTzGN_qNuX-Aw-K1fe89iQXi0befJGEZInWZClN3gsqW0G-H0u_MtNeFEigFrkb5LvL5WVjRpdh03W9qUCFgwvIMdZ1H5atmhQpC_f-AdCr1LbMz9a5-Pxer_0frgvgs2t__NwGdKqeO4KGa13pKkp1oKpXacEPf-8PPdxBEe0AYFP8UULqufX39U8wzoD2q6kB8Qn2VzcUzxR-Z9dnyO8XPKZye1RxtZy6vVpItLSXfjQ4CVSuS4UnIcNWBigXE0W4dT96Aw_C_oaf9T9a53KxEhsl46tz1cd-QRmhREsYVxU4AQpHia_dBTrhzDCak7cyxgy-oV2BHXzLNdejcklf4Qqg6YBQYtTrAEKZbwAOga00IyPVQEV7IzcOzhJr9Z-8_TVG8Uq_AFFv1E-bAIWK8Fk9qSf4rSGK8lPm5YZBobT3PGdOZAGOJxg7fwSlxH9RMhT40ZzjvXIUlY1iCop9g963MhDtZ3NXOMkljaC51xQL4vSF4LO_FycTze5op5Fa5BQsc6Rqb2kLooiXFDa_b3ZLKaPoxGP5VXUd1Fee0J7MBqqt9N1dGjGE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخرین وضعیت زنده‌یاد ورزشگاه آزادی تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/105199" target="_blank">📅 20:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105198">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT8FCKAtjCEUHmSwbn9NhxwPgL6CpMHAfMwXv1HfppZtxncMveJzkJAbsOaO35eWG-VoUGax7Gp53Qcd0vOQexyxUfjPUSyra0t6h9n5apDvGnOnjgrqEdb2QtYZNniBDgZRGxGxPd2oofvO5u9_GEWiLUrb9hXgpi_5ZGA_2obeSgsLgrRtUHC9hQ_RUoqWTk-b3mIJHV2Z2pRgWJMSrAsf51kK8AS7d3HzZthf4x0Z0oG1BP_H1c9FmtWco5nH33XDcNoIWVLReMXbKKbVfHFHCMxp9VCMODNHreZJNUOex3nCKVcyM0fwB_hb7jXEq5m97ibyCHADcXlr2QvSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
آنتونیو آدان: به باشگاه استقلال گفتم که نه پول فصل قبلمو میخوام و نه دیگه حاضرم به کشور جنگی ایران برگردم. قرار نیست به استقلال برگردم بخاطر همین طلبمو بخشیدم چون وضعیت ایران خوب نبود و مشکلات این کشور رو درک کردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/105198" target="_blank">📅 19:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4Q7XUgDD1tIBW61wCvVgQXyhb-AeF8m-ysenfu7m_AZVAWQSEIfcCt0t1Zu7uYJVlsSu6-HmuolIyf-qMjhCH7UFRctDIz0XtidCIlrY0pzp37I7i5iR89OFvhYaiyoLrmwxH_UguSXuHAmoE8GM1RKZODumeBU9A3q0sGDzyg2zbPxO5OtKvKNUesPYS87q7WCiKtvIQWtvMuQcwbIloyLdLYjpLi4_G9lhs43f2eVegLhn2PooQ-jjy6K2GExdUicIfrPtbidVR0-J9NqWkEwgo7qriOVeQb16fOx7wR2E4htJ2Yc5eEHFjgz7wnb_gjeLaL0Ga1iLrwGJjDHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نامزدهای نهایی جایزه توپ‌طلا روز ۸ سپتامبر رسما معرفی خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/105197" target="_blank">📅 19:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO28TqHKnkWmcsoBb71h-pv8FLSRA-S9vjPP1F6_4PEQ7TfHS2tcst2mD6Nh0KSOcY8tvxsW_sWdMmVePvot1KyEre0uoV1NNngBLU0Ie_kQHeJrD7SdSvGMKnHuGvlco5DriNWCaU80euqeTaq4pPUhhmZosxL_dFOd_pAUMGPaDdo7vnoTemDxSwc2v6Fy-O1t1w4lpDJVOBcuI8MPjupmAo05NAPIaU0H1Mb1joDehpB_j3bzB0CBs8V2XRZFSIxbVhDRHSXU34N-lw265xzpJ0U2fWVHXLyrJPMCqbNP16PcOFnSotHs41B_aOrkgL3fmgrD3fJ9p77bUa9aLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
🇮🇷
🇮🇷
دربی با نصف ظرفیت نقش جهان؛ این اسمش مدیریت کردن فوتبال و مردم نیست
❌
ظرفیت ورزشگاه نقش‌جهان برای دربی از ۷۰ هزار نفر به ۳۵ هزار نفر کاهش پیدا کرده؛ یعنی عملاً نیمی از سکوها خالی می‌ماند.
✔️
در دنیا برای حضور بیشتر هواداران راهکار می‌سازند؛ اینجا اما یا تماشاگر حذف می‌شود یا بخشی از ورزشگاه را خالی نگه می‌دارند و اسمش را «مدیریت» می‌گذارند.
❗️
مدیریت واقعی یعنی فراهم‌کردن حضور بیشتر و ایمن‌تر هواداران، نه ساده‌ترین راه یعنی بستن سکوها.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/105196" target="_blank">📅 19:39 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F26bMN4vM9Wkf6jfnaUKoD7Ea6fGIPckrAtkc0jwixes1iEzoBZN-1MY056wuHsgw6w1idA9FDncy0yeUTZxS5GStUTQ3lIxmgc6adjUqLy8BGBkmTyIWDp9nKAfd2NtzgHVgHzKdLwoRrNcudekrcxEFgSQUgDuJZmeIkw59x5DC2KEovQuGntyoHziMNxbY4PSZN-W_pwwwLp15ldc0j3YBWjbo7IeC400qzNOlgZeoTOJ_TfHCdFm8xYb-pCSLkAmq2ub_mahHQtporydYBTdCOgDGbjk4S3usQYW4AD3Qqzp0q38RWX-bMIoc4A1cJQFqev5LtzHnc6v1WNL9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اورنشتین و رومانو: لیورپول پیشنهاد ۷۵ میلیون پوندی سیتی برای جذب گاکپو رو رد کرد و این بازیکن در آنفیلد موندگار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/105195" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105193">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=lxtZk0GF4qPKREzywQ8g8zBavwlG4QiQB7xcUWG5BYYmgVss9N3CtCMvsK3TixyIln5XDBsMfIGh3efAZnm1AiP0sjeXYL07ZaB2yH07zP8xwl6kEdNyn-TGBuK89CVBOE49nWVJNdZjr3-FmG0zbM5KkjMrAC7J5K5Tv0-7ROjwSZjJAVt2vU8SyWEdBqrVfSclG_OXASHcziwCjxDPQ6UowUDhIjqwUI_NiDmGKkCYb8GR2gn4NjE0qJau1LEncxpMugJtAhrycU4-5BoBbTrKsW955ttgl6JoTN7WvNXtUqI9bzU2VIO0kPRa1l6PbfUTFPTiW-eP2GhCx2EoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddcd857187.mp4?token=lxtZk0GF4qPKREzywQ8g8zBavwlG4QiQB7xcUWG5BYYmgVss9N3CtCMvsK3TixyIln5XDBsMfIGh3efAZnm1AiP0sjeXYL07ZaB2yH07zP8xwl6kEdNyn-TGBuK89CVBOE49nWVJNdZjr3-FmG0zbM5KkjMrAC7J5K5Tv0-7ROjwSZjJAVt2vU8SyWEdBqrVfSclG_OXASHcziwCjxDPQ6UowUDhIjqwUI_NiDmGKkCYb8GR2gn4NjE0qJau1LEncxpMugJtAhrycU4-5BoBbTrKsW955ttgl6JoTN7WvNXtUqI9bzU2VIO0kPRa1l6PbfUTFPTiW-eP2GhCx2EoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
💋
با این ویدیو فوق‌العاده و غم‌انگیز رسانه 433 میتونیم ساعت‌ها گریه کنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/105193" target="_blank">📅 19:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105192">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
▶️
🇦🇷
ویدیو جدید اسطوره لیونل‌مسی از دوران حضور درخشانش در تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/Futball180TV/105192" target="_blank">📅 18:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105191">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyppWmtdkiLx9HLNywUiGOku87O2_k2Z_ncNfxO-38HhG0KypKqssu8Es4tqZiPqF1F6bohgiGGbo2umVHB_lvHn3mRzpkP2m9km_Kh4ZMCnB1IcsSRZUy94MBBvlpFKblgeO6FXE71FVo5yhPJnpDDgsKopwOdC1SyhbYlr_VZaf3mD9oYlUxd-kn9X0119e7xq-UNvCL445tZtXkk9GRyUb-FicT1nU8tnbUeydHPb4qwHcZlWxL0lysz5fNUHF7YumZRjPqPuDLcOVwXo-ZKBSTq3GfnS-Z1-b252GXNb3ptGtFB19_29YJkLa0Msftxsdugp5vppq6ttydw6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🐐
عملکرد اسطوره لیونل‌مسی بهترین بازیکن تاریخ در تیم‌ملی آرژانتین:
🏆
1 قهرمانی جام جهانی
🏆
2 قهرمانی کوپا آمریکا
🏆
1 قهرمانی فینالیسیما
🏆
1 مدال طلا المپیک
🏆
1 قهرمانی جام جهانی زیر 20 سال
❤️‍🩹
207 مسابقه؛ 125 گل؛ 68 پاس گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/105191" target="_blank">📅 18:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105190">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COv2PZvXM-RiMoePOqEciAY09prIy1SNQd6NBmKobPtR8W1ojbm9eNgljDAzYXrNDkxoDnJEJylgz60PoTT-R5M5EFVKwI8BhiR3rNd04gC1KYgbLZkwFmtEAsm0zAoAfFm81cQXcClacWc8KEQu59TzTmFdrn67FK9LWYj8XTJrUZpS78O94psgaiMkgbYRdvk6OH8sTp-AwaQ3C6EgXHvNRwdnS9dSyqX0P4wojPBuR21dsPv1iSd5h_nFyvlPNvpdWPCtx3Cupg0oBk6QPhZA6huX-MVTPVNI9GFmqr79aT-3fYzEFj6G49BPtRjkAeuD4feCMvrbnflpw8DZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🐐
📱
پست اینستاگرامی اسطوره لیونل‌مسی و اعلام خداحافظی از مسابقات‌ملی:
🔻
دوست دارم، و دوست خواهم داشت، و همیشه عاشق این هستم که بخشی از تیم ملی باشم. تمام تلاشم را کردم و دیگر چیزی برای ارائه ندارم.
🔻
همچنین، بازیکنان جوان فوق‌العاده‌ای هستند که در حال ظهور…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/105190" target="_blank">📅 18:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105189">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ejWp-PtiWxy5Fb7oE8TvvcPG3_mWdmYy9aUa92OtBiwNkZmqa4K3phODIb9-FZ40twPzKjYEF7M6NVSX4UMFq0tFCqTseqI_S3bI7Fk5xIVitFiMHdd_OIs3nnQmC8D_JuG5WK7BMyjTkInpdN88e5T06zlUmgchQKnQc6u8UU_S0M2eF97Paqh46HuAYG8qynoRoM5aPf8VFOhsYmojpshx11QpXISGC_sN1IGG4P-CIZUs7CmI1PGpC7OXirJCDjut7MMSqz-ZQY4mu6fa0t0CY_J_RdBh1NxQ7x3ITsI3nnLbyq-hwo1s36TcVCXjHmd7ejFHtegg-kPumXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری #رسمیییییی؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/105189" target="_blank">📅 18:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6TvdTBrbYtLeuihgIq5LYtVh0d_xtgVajuxPzbLLT3ykql4COstB_D2_Qle975EIZnx2jXKlThShHLYiT7eipiLdsMdxp8HOgkjb4T4M0VNW2TxgYyH3u0ZXQfve-PStIAQ-RfZ_uO8LbkeeTDfDbrWVlkym60bVx0aKTknBL1Uhs2MMK9OIj3Sblfs2Oo7E8iMLvHHNYO-lxbfkE08Vo35iRJiSv6Fi6Xpq1srvfqiHzT9fCqW7dSTMkKnb23NipHDl35ByEy00ZUExEF7WG6ZR-RIwKhO0k18IytqkMLScTIsPbVVQ2liUOKa91eT70wVvwOenahwGEsm4sfNPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇦🇷
❌
#فوووووری
#رسمیییییی
؛ لیونل‌مسی از تیم‌ملی آرژانتین خداحافظی کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/105188" target="_blank">📅 18:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdbv8IDz3PLuA6-YGJjbuER1tyl0tfXLi6lYnqFAGwOmyj5kQvziq5Crn-3FF4NpAMxRXPIdv7F7xvYF8-C0bf4e558MVgZbRNrqYQnQAPoybAM0p73PzWKJaIDfa-BP0mIMha23Od26Qxezmdbavc2lg1VDuloDkomhybn6PUX1Ovu-wReUQhFTMordtrPH2-XctkjL6MZi2gubdnwyDIbjfrHcseVYu2gg54XtPxMW09PPQi0wS-Yu61pHgdTQe1zhS0LSlPtMlrG1mROr4MKlllhF21HiNRvg7uuaIEQbSOBuMqyIx96DX6Q_NVUe0Kt3SV2CHeMs6Gmkcn1O3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
مقایسه عملکرد مسی و رونالدو در میامی و النصر؛ کدومشون بهتر بودن با ریکشن بگید
لیونل‌مسی
🔥
کریس‌رونالدو
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/Futball180TV/105187" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAuxXtY7c6Dp1BPol-ST0JPRQBxdzIrfpHOdlnrWGokfmZ2Q4RJRtLcmj_oevA7wo9ypUWAtfNJaSXB1nSal88jfIxuwxJoCaIIm9E8SkU8Bh8G1UQRJs33CooVCxO2M5I5MolbnDoQOushR7TZrCMBmbkQRJnG39QsIiIsaVlJnkNT7rInx_MK3JlQeos0AO6RBeWTZRuShaXAhCQPlErPMj1_V-qt9BFcOejgG9Hn8Qvt5ZPD3--sc0Fd33I9azXcvXjZW25CqlO8I86onRJYagviXgc-_TjEusLwrKa8hGHGkC7razi42xKcMJIaJHxPnCmbYWlZAy8h-inAIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/Futball180TV/105186" target="_blank">📅 18:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=lTTj4b5pzba0vXwNOobCxdRQj10Gk1OfdPbxlMMCgPWdbwByespv7S1K1j7Rr4AMq6SxYf3rxBxbbJxJWJ2xrkNDQnRzDIqk4k6QPzzJgDKz0L8XsAw__Pr5FFTAISLJrz3siE_rGLp4HnoJgBhHpQzlRV5xKk8j8zx2Xmoe0SrESV_6C4niM9mqEyhCAte0Kc2qkvL9TlKDT7WPzuvnpCvWiQp1QHkI5UcAR28XSpgUQ_Y9vE9eikpzwffxYNzmhJNvbvCJdFJE_sh2DEEBE1SRgijsROZ-yqoBpmoVv56qy_EuJZ5M8Qf1RKb7qB9E6ZmCJdSpZ_yS16egLABsvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f80bffe56.mp4?token=lTTj4b5pzba0vXwNOobCxdRQj10Gk1OfdPbxlMMCgPWdbwByespv7S1K1j7Rr4AMq6SxYf3rxBxbbJxJWJ2xrkNDQnRzDIqk4k6QPzzJgDKz0L8XsAw__Pr5FFTAISLJrz3siE_rGLp4HnoJgBhHpQzlRV5xKk8j8zx2Xmoe0SrESV_6C4niM9mqEyhCAte0Kc2qkvL9TlKDT7WPzuvnpCvWiQp1QHkI5UcAR28XSpgUQ_Y9vE9eikpzwffxYNzmhJNvbvCJdFJE_sh2DEEBE1SRgijsROZ-yqoBpmoVv56qy_EuJZ5M8Qf1RKb7qB9E6ZmCJdSpZ_yS16egLABsvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
استادیومی که تاجیکستان در کمتر از دو سال ساخته؛ امام‌علی رحمان چه رئیس جمهور شاهکاری براش این کشور آریایی و متمدن هست واقعا
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/Futball180TV/105185" target="_blank">📅 18:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-dHGPTnZDSmh4h8vFIrfcIqxiN_72p1DJqtU2qLe9k-sTuyr0BQjVCzn2U7x5RAcuv2-vDYJarlgxKajlidiH6VQR_b_aT-mkfVIdiTs3juW1lLgFFV_I9ILpACkNEuH0eOf7HXI_DIgQBidYZM1Ar4AVJfhZNaLsqAcAza1QNHGb52OujByPJxZYEA2feI99Mc0L9gZjYC9YGmf8V-_DTztlXodeFLDDypn2W7iQIJ23bXGzpjNHRDfw8d0JxhzmWF1iednBcwn3MzoDWENJ-_jxD2PgTZ02exmjQZly9-hZ_Ue1WjfVnDZlq4z1LdsDDAAaIL6qn8Lw-y2oKebA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: بارسلونا هرگز از تلاش برای جذب آلوارز دست برنمیداره. اگر در ژانویه موفق به جذبش نشن، در تابستان ۲۰۲۷ تمام تلاششون رو انجام میدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/105184" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/105183" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/putqCnGYOnltcKMuK1Yy0m-P5y4XZKvj0kEboTtM4FJw09VZkQeDie0fMVlKBiZab6n97NKRSPNerieNx3k2kVmHIWbTNzuGfgspCbTugJJcPgpFUhBfzwez5K2iXdGR55ttU7hqthhJDf8XWI3PBSGmmaiCLPyFT6_8OBlsWPsZsHYA7fyoM8OZRjk_TepkoT0YEMQkFTLJZliwJeC1qcUfBUuWLwS_hxcHevqc4XlIbJ2eRtdqppGbTxaOXzMZ8r-knqhK5o9eTDrN71t7xgb7AsLNEbGDYiCKTvLtVbhChq4__dDhdF5YBhjfMpeVLIgxV6KHApOxnBimL-Y92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/Futball180TV/105182" target="_blank">📅 18:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njndECYtzTQZYKJniJPYVzVsTtRNvQUIr6dzuz4SDR0Vhwg0UY-V8MBn3AX8hLAm9gq94wYRquBTsL6GAv0I4seYL-cgZspzleHCRW7vb8CTrNRu0lULTTGq3TL-2tdD7BGTuZISjsBdOyq0X9H5ZSK3yW_E_DCqR253PNjOWvUEs3tXHov6gzawMzcukBvmBTiPIz_agIP-vLhte0voGzE8c-AlOHM4TfPqy8MlSESF9QnPi0-7hddltM8Iwda6_t5g3GTfX4H1WJNlJxfKh5h1NJFyB32zVvj-Db8EG1e0XiLE5xwwf2jJwChrLdHLtLkA1Cc12URKg7U-7dQ1hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇸🇦
وضعیت خوب نیوکاسل پس از جذب یایسله سرمربی الاهلی عربستان؛ در مقابل الاهلی حسابی فصل رو به ریدمان شروع کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/105181" target="_blank">📅 17:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⭕️
⭕️
با توجه به نزدیکی به دربی پایتخت و بازدهی فوق‌العاده تبلیغات تا پایان هفته، اگر تمایل به همکاری و انجام تبلیغات مدنظر خود داشته باشید، با ×
تخفیف ویژه
× در مجموعه تبلیغاتی تیوا با بیش از ۱۵ کانال مختلف ورزشی و غیر ورزشی در خدمت شما عزیزان هستیم
برای هماهنگی و‌ کسب اطلاعات بیشتر به آیدی زیر پیام دهید. سپاسگزاریم
❤️
@Tiivaadss</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/105180" target="_blank">📅 17:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMoWmGs1Iy2owGPX362Hixd_gINSxy77oJrxg_C8f5AV0TLtupwIOTD0P3fRRyhiZ7cl7kDfGgKy6Svl0Pz8KSQM2bz9bfwE1fT1TYNJ1unrES9WgwtSoMRE1kDvN1O9XrOAJpAd5yvpCcjEaM16tcKCPf8L57I5jc66aUtA18gEEGR-O_JEqfwfOLkZSqLEHDXWn8h5gpTQTnh1a84VhGtPwFTEp2EV4NlL6e_SxB9IvW8Fj41A9LVOr8KuAh0i28JDFbEhpD9hk3Vh1ozY3ZqnjHmVUrTTzB_dNlumD4fnuSf-R3QBErzlwLs4RoQ34iQ__-kodMO-dQS76Ow74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
🗞
#فوووووری رومانو: کریم‌بنزما از الهلال عربستان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/105179" target="_blank">📅 17:43 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105177">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oTlIn3DgaFarDb272nXbWeyzHiist5g6zSpZJWGzhPgvcGQMfkkxThyu6LUktudCykf70U6RmYve-GVPmM4UoCN6V-GBjUdkYOtU1zhTiZpsG-SL0Qedu7jaPeyv1WjhInqJHHZGblN5YhJrspZUCWY0uxkOEjdLYauzUOIAmBi8xnXq5bMb62XGc4-YBuTIgdd38cs75R6Yx00LYUoXPPK3DTvhRgmAX7MlVejzbQsuT4HaS6OLTFG71WZmLEz4q6oRY5Sa1Z4eVxq3jCtV2xi70m1YL-ZTOpiXLiGvJSktVlJ6-hDbSpc8J_ee-G4OSCHxbXN352qj0otfkd-3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RInj94KQ2zac7L-vDvhUqZky7YLpCjLc-568aXo3iU8p2LpzNGYD-Hl_SkogN7WPZqHgnaoltmf-GA_0kZH2VMBKVjpxMUa9Z87GSkgSVVH6JQUr4ezhUUpEm2Xapc6Lea1iYlF2A2bE0HD1BVUHOj3fPgQyAF1fzx3bIaI9ZW_gdTXBCMeaUIvQllqt1zdtkaGOEkyNllBD1ieQk-NfL0kGxnpumken2hgU4ZGc_I3hbDGMStOlxJXWHoJDwAxEikR0mQVKxpor7A3hJUhyc1FOugBLOMMBPlvTovoRNmbPOIIu_jokAavmEZLcv9BIpJjYoXINBCW2qwjXhyTNzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇺
اوا موراتی، مجری ایتالیایی چمپیونزلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105177" target="_blank">📅 17:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105176">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ ابوالفضل جلالی بدلیل مصدومیت از ناحیه کشاله‌ران دو دیدار آینده پرسپولیس مقابل تراکتور و ملوان رو از دست داده و وضعیت نامشخصی برای دربی داره. پزشکان حداقل ۱۴ روز استراحت رو برای این بازیکن در نظر گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/105176" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105175">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/105175" target="_blank">📅 16:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105174">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=TQj_SrbLYtpGoI0XqF2Y2WMfS4Zep14mO6nBtGSkVREmJ4dKOHZmIb2UbDrRuY1gPgqJp1DvoAMWp0ciH4E1bhd1yt74D9awB5KmYftoeimMoFioc6TilCMbbkYvvCiTzbdLnuXx-u8oErUJOVg37jMbkbqc4rmTcPTw_npjwjN87hs3TliAzf_1cuB7_AUhcdiAX7c8W0GTgTFEaUsOkhOv9XzEofkweZXqKruypYV_sWBxLpm_KvTadwgZ7_rzCgtBRuxMU9Pl0kYIiPxyrpz66DZDCKrF8KiOj837ci4i9OSVcP3HhLZeOXk60om7jH0iQM9WQrwWC70Cige-EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15501a2dd1.mp4?token=TQj_SrbLYtpGoI0XqF2Y2WMfS4Zep14mO6nBtGSkVREmJ4dKOHZmIb2UbDrRuY1gPgqJp1DvoAMWp0ciH4E1bhd1yt74D9awB5KmYftoeimMoFioc6TilCMbbkYvvCiTzbdLnuXx-u8oErUJOVg37jMbkbqc4rmTcPTw_npjwjN87hs3TliAzf_1cuB7_AUhcdiAX7c8W0GTgTFEaUsOkhOv9XzEofkweZXqKruypYV_sWBxLpm_KvTadwgZ7_rzCgtBRuxMU9Pl0kYIiPxyrpz66DZDCKrF8KiOj837ci4i9OSVcP3HhLZeOXk60om7jH0iQM9WQrwWC70Cige-EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
وقتی صحبت‌از دربی میشه؛ خاطره ورزشگاه آزادی با جمعیت ۱۰۰ هزار نفری و صدای عادل فردوسی‌پور زنده میشه؛ چه دورانی بود واقعا!
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105174" target="_blank">📅 16:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105173">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">▶️
🤯
برخی از سوپرگل‌های چیپ از راه‌دور ببینیم؛ حقیقتا گل توتی به اینتر یه چیز دیگه‌بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105173" target="_blank">📅 16:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105172">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHi52h-XHZKBcHhgc9DB127_zdldo3gAQLN8YYQ-x25Kz-dpOvuSFLK15W9bv4RhQcuEKAS7VVPGJJKZ9YdyCGOiemhYi6_hrWIQGZcOvtybNasj1wDK8_eztQdCvp99FmJrOmJ5Pazxkzs4vfil6pB9ezFazTb1lBQfoa0FxwscQ7N2Gb8t9bKynf0gLwjZdV7u8cVC68W7nRCUXe-J-j8Hk-j79F1s5bzYkXcQmZVXKQ99Gg4CLZ85OtHj6KJKDc3NbhBOEX7XgpHxmudPYsOuHim0UKQmalNljMk1QsqjnfsPpMW9QOEq4gAaIYRQdRFYv0VdFc1u9PCx5O0UaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
عملکرد اسطوره رونالدو‌ در ۲۵ سال حضورش در لیگ‌های مختلف فوتبال اروپا و آسیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105172" target="_blank">📅 15:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105171">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zsw73-iSqcb2H2-pB34wgGBtpNjrJpp3KJDeJUWLnCnzGvUSGmQdvEZI9ri70o0mbgRhHM7zNAuGI4SUtkv-m185SJf8jadq1bpHXa7xXR8kehQ-NCK0BVM5rugBFbDqSDiHUhVyZZyZQJp63iUV7-Ry8piUWC1cFqSd8qLL-0KDIQUARuKfJ6iDjM6AoC3KZKIt2snYA55t2edPyOy1AUZiJ5H3n1hHyTCVsqH7BpwOBxrf-OTBvJYvVeocLfRNcUHn0ypFOCeqHDMvwXPBH83Ryu-4tfUwM2NXjqU0FzMaQx1mBa7HK2S6Gjo3RzL1Jzwd08e4mFSA179VsFW00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😢
⚠️
دختره ول‌کن رامین‌رضاییان نیست و یه ویدیو پر کرده حسابی ریده به سرتاپای اسطوره اخلاق و مردم‌دار نسل فوتبال فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/105171" target="_blank">📅 15:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105170">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkgjAt9rUuArWABttUEqwOuhxAC4Au83N4a77TFTDwT8G5Ks6jTjl6-BxRHo1xQJa8EpjmDgQl41PT9iVCqM8c838bpAMEGK4He5N2XFxHy1rNvVTE8RJiF-UPezY_1pPrW5T_qBGIFDza4-SmSnzEpnp-I8tt7uJo9Vi8-O1aICBVxqJdqthbEVZvwNdw-NWd-w2u1vwVEEbzwihZGDSnZPNSI0hyUUjRCSTRKDYoFCE9p34TC34NB7FB6jpnOMq5fUTGGnUAEUlI-JR9AlOS3tGaMVfE7RXRnvRUmPhztFZpMuoe5pgImfAQ3ET_GVKcMA0z8g8JoJtAiNmpXg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😱
❤️
💵
با رسیدن قیمت دلار به 210 هزار تومن ارزش حقوق یک نیروی ساده در ایران به
75 دلار
رسید. حقوقی که
یک ماه
باید با اون زندگی کنه! معادل یک
دیسک بازی کنسول
که در کشور های دیگر کودکان با پول تو جیبی می‌خرند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105170" target="_blank">📅 15:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105169">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKchE_54XCgYnsAlbVezdnG_Bt_Xf_orguVBm0P7EaGojFNwaMxvHiXhhSk3E22MwUSMCpldZ6I5VxV-Czr0V9LzVnPAJ0kj7lZaePVlYoraqkwzyntdwYzcsmDuhw1CUC5zQyqy5P4utemhMiR3ppD0s8xGdZZaiJaBjX2GrbgIqJRBJ1BhWrxcIWyya5KhTclsib38stNQOUKrxzc10WwyZRe2UUse4ReGQ43119xDllAMDxUjyDdFB-09uI9NmGPkD80fvDiwRqdkVika36HrDjZuRNMx1O0f6rLvmGkq8b0IoXHJal83GzcvMmjVfPpL1JouqaPpTqacheeLCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسا برای بازی امشب مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/105169" target="_blank">📅 15:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105168">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a916d757.mp4?token=BRazWrUyy9aw7Uh51E8Sa1QhiQzIw3E8pemKD4qK_Hf2dnGZI0A9Zp23qkKPJ7j68048G_5vsUM2ZZg_UptjvnplXADcbgfBFZYQdbhfquyMtemBTajn3_reIcLwMCJDJEJ98vHeFdyO6nVwbOnWEKgWGd0ORmrfIS1yKzbPy19GpMgcnLSaC2tliGU5DiBWxc9JRyCH82YBOxvS0-1BsyVa3FgQZH3W8YjRQi30cBsJ6Icj9bjhbyTXXm_x8ySxkPZAtkql4sv4b6Ob8uyIIHv4kyWMEF_g3pAUnd9de1H9y5zF_wP34zSKLxELmQ31lIKVctyP4TLPScOJaxUP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a916d757.mp4?token=BRazWrUyy9aw7Uh51E8Sa1QhiQzIw3E8pemKD4qK_Hf2dnGZI0A9Zp23qkKPJ7j68048G_5vsUM2ZZg_UptjvnplXADcbgfBFZYQdbhfquyMtemBTajn3_reIcLwMCJDJEJ98vHeFdyO6nVwbOnWEKgWGd0ORmrfIS1yKzbPy19GpMgcnLSaC2tliGU5DiBWxc9JRyCH82YBOxvS0-1BsyVa3FgQZH3W8YjRQi30cBsJ6Icj9bjhbyTXXm_x8ySxkPZAtkql4sv4b6Ob8uyIIHv4kyWMEF_g3pAUnd9de1H9y5zF_wP34zSKLxELmQ31lIKVctyP4TLPScOJaxUP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی دو سال پیش این ویدیو از نامجو رو دیدم که میخواد کوکو رو تو ماهیتابه برگردونه، شما اگه این ویدیو رو میدیدی از هیچ کار این ادم تعجب نمیکردی دیگه حالا فکر کنید همین آدم بعد کلی فوش دادن به جمهوری اسلامی دوباره برگشته مملکت تازه ازش استقبال کردن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105168" target="_blank">📅 14:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105167">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=gxtd8ceWRSr0tX0DfSnkzG2at1Jl47JL1tGnLLZPlHVtswTGRfmW_BfeBA5z_dbhDZWu4JqeLeQ2x4aDyxOLveyZtUY7T0jHlvWlfYQvaaTtk8490DpIaYJrD_p_5ggCn6kjuw7yacuWbw74Jd66DIrP2jSWyLQgdOEECJro2SHD4krrMNawOYb3_eDlueIp5oaqP4gtSvdlbwyQ-OA-ldsm7ae1u8EksAf4ImxpZPZjt4lZeYOT9h5UlxE2AI3DKKFqi2x2__FQZShjlJxMGKhq2dt3MK69Da3Kv4ysbF7Uj3S0DjXTrSeqizhM718qg3jPS6dXXRdTKzG4fLh7_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fea9db172.mp4?token=gxtd8ceWRSr0tX0DfSnkzG2at1Jl47JL1tGnLLZPlHVtswTGRfmW_BfeBA5z_dbhDZWu4JqeLeQ2x4aDyxOLveyZtUY7T0jHlvWlfYQvaaTtk8490DpIaYJrD_p_5ggCn6kjuw7yacuWbw74Jd66DIrP2jSWyLQgdOEECJro2SHD4krrMNawOYb3_eDlueIp5oaqP4gtSvdlbwyQ-OA-ldsm7ae1u8EksAf4ImxpZPZjt4lZeYOT9h5UlxE2AI3DKKFqi2x2__FQZShjlJxMGKhq2dt3MK69Da3Kv4ysbF7Uj3S0DjXTrSeqizhM718qg3jPS6dXXRdTKzG4fLh7_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
🇮🇷
هواداران خانم خوزستانی در بازی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105167" target="_blank">📅 14:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105166">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=tjhqXuGvYm0TdjGCl3QGvrZeFBr2TpdoYyLpYPFPzwBwuFtA737qG4kC2s6VZPmvfKLag8amaQMfTkmdXhzLr09ooiBN9oFufC8DSHA2Ca_3jwtmwRlJWPM0qpNV1Fkw4vrf7kzNUOBLqHI_m_ZDppy9R-tMICwrSUh4BxPTItp22yhzGmj8VA0c4xsA-_7Yp3evNwHrQcitD8KiH390bAVLZCoR87nZRoSFriLtLUUeoMYC4IYH95vd9Gwpzw_qDNThyOhoesvpVrBX3aV_aZS0i4YWFr-b24Vqox7kfTQo0vR_Jr-s1B2inahZeBkwzqiGzvVR7DXqmen0pIzGPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c2e01cdc.mp4?token=tjhqXuGvYm0TdjGCl3QGvrZeFBr2TpdoYyLpYPFPzwBwuFtA737qG4kC2s6VZPmvfKLag8amaQMfTkmdXhzLr09ooiBN9oFufC8DSHA2Ca_3jwtmwRlJWPM0qpNV1Fkw4vrf7kzNUOBLqHI_m_ZDppy9R-tMICwrSUh4BxPTItp22yhzGmj8VA0c4xsA-_7Yp3evNwHrQcitD8KiH390bAVLZCoR87nZRoSFriLtLUUeoMYC4IYH95vd9Gwpzw_qDNThyOhoesvpVrBX3aV_aZS0i4YWFr-b24Vqox7kfTQo0vR_Jr-s1B2inahZeBkwzqiGzvVR7DXqmen0pIzGPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها‌ ایرانی که میتونیم بگیم خوشبخت شده همین همسر جان‌سینا بزرگوار هست. چه عشق و حالی میکنه ناموسا
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105166" target="_blank">📅 14:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105165">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b552c4303b.mp4?token=bfKEbaB6IJYqX74U07lrHBIFnGOV2faCLEr3oruzX2-63sclvgAWrkMclKJsGsFy8JDoRz4YKYxIuZx66BB7Li6scBfyzBKF3fqsTYymRHqFUAinzaPMUK2gAGxYFowEO1Tswuk9_AO3nvV2r5_fqPdzxiorckpsFsF__YpZ9oZhhZu6cBOQ9wL0l0n1F11uCbu0l-ZRATGQHNmvCA2aTbYVq_sPkqmM2bMS1EsA8BmA8OUPSwh78GvFse7J5H08mkEAOccB8lb2oV69re6fIW_OehtddRPFcqAEc5s8Zm4StnhB9s9mPa5J-g0w-66olCBccB4xZ2YckUBATE7Ea5iBFA_R2rFhePKNhWZHnkiWqLDXLlWVgx3fWh8bBHHeEvYcZZbqa2KMdF3XdfJRi9IibYyf6UbUsxOkjfU8kRTQxLMxcQxiqL8MqyytxpiYqDMt7zpvT_kuVqQ8ZAZVF_840JqvmkwAp0dfTb2uIrqsPid9udmXe5I7Wv3j9R1VERjS8MzeXtTsdcClierVQ1YZy0g7wBfPwLq6P3E97fV0XZO5def3rdD13IB8gGCMi3a5Zd-PVfkZRoyz_mOHFucL6NHWEc-ptY7LX7MIc-aRyqpY5MoyznGhAddSP1p8L2Pn4C79x-4fKwf7SdhmQL_yRvPQQDlOUyNcHYlqJok" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b552c4303b.mp4?token=bfKEbaB6IJYqX74U07lrHBIFnGOV2faCLEr3oruzX2-63sclvgAWrkMclKJsGsFy8JDoRz4YKYxIuZx66BB7Li6scBfyzBKF3fqsTYymRHqFUAinzaPMUK2gAGxYFowEO1Tswuk9_AO3nvV2r5_fqPdzxiorckpsFsF__YpZ9oZhhZu6cBOQ9wL0l0n1F11uCbu0l-ZRATGQHNmvCA2aTbYVq_sPkqmM2bMS1EsA8BmA8OUPSwh78GvFse7J5H08mkEAOccB8lb2oV69re6fIW_OehtddRPFcqAEc5s8Zm4StnhB9s9mPa5J-g0w-66olCBccB4xZ2YckUBATE7Ea5iBFA_R2rFhePKNhWZHnkiWqLDXLlWVgx3fWh8bBHHeEvYcZZbqa2KMdF3XdfJRi9IibYyf6UbUsxOkjfU8kRTQxLMxcQxiqL8MqyytxpiYqDMt7zpvT_kuVqQ8ZAZVF_840JqvmkwAp0dfTb2uIrqsPid9udmXe5I7Wv3j9R1VERjS8MzeXtTsdcClierVQ1YZy0g7wBfPwLq6P3E97fV0XZO5def3rdD13IB8gGCMi3a5Zd-PVfkZRoyz_mOHFucL6NHWEc-ptY7LX7MIc-aRyqpY5MoyznGhAddSP1p8L2Pn4C79x-4fKwf7SdhmQL_yRvPQQDlOUyNcHYlqJok" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره فوتبالی هلیا امامی از شبِ‌معجز‌ه‌بارسلونا در نیوکمپ: پاریسن ژرمن که گل ششم رو خورد، دور و بریام در ورزشگاه غش کردند! جو فوق العاده‌ای بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105165" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105164">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
✅
🇮🇷
🇮🇷
موعود بنیادی‌فر شانس دوم قضاوت در دربی روز چهارشنبه معرفی شده و‌ قرار است ظرف ۲۴ ساعت آینده تیم‌داوری بازی حساس استقلال و پرسپولیس مشخص شود. همچنان کوپال‌ناظمی بیشترین شانس را دارد و کمیته داوران تقریبا روی این گزینه به جمع‌بندی رسیده مگراینکه امروز…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105164" target="_blank">📅 13:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105163">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38c6e037e9.mp4?token=vGI4aH7DPci5t2EGyQyZ7EKc50COxHiE_NSFEWso8WZ0QrUU5vMXjffRjzTttT18mLQUOKar-rHLHJ9AE6NyX-ETDBEBFkJg5yO8JSwO0wQi4mriSunA54OC-F-lg0lTy2VaQNMwyanPgPa1b8evkrfbrgVLj43OJw0QazOf60j4C8j7hAKwFSb8wlwCUZyoJ8wJgnAoSpzd2Jq30aONWXp0x12znuZaJE9781KmN0-_rAXp3Db48uVmdmWeujhkQdnswVDP8uvl4tPgBpl-0hU4yAT5CMawc3bvsuFVyj5IjPnZFQla4f3FSemu-0J8kPbsX_2aE3ylbIeDcCMkF5vj0gqmsACEkuaM2cIHBFMflJNJBnTqS5MaxtqYp9-w6QKo7YsX8NT4tT8AOdZyEyMqEgAm25a6ZTYtSLhlZmMKK_n5PpyMF-gnAd_TuaU1nZhFYWG_yGqZEowdeU29K1UqZPv_7lzZIdio7THFA-9pE-ipvFRR-LIcKBk_OkffFNil3OjqNMl2iBLnSstPsRc1Mra1xm_gWu3t0CeUdlGnEmjnQN-gbUPnUUh9QOSqNBba43dEeZD7pWiOv1vbZ0M7dMuXXHwKHKaXh7Ys9QGsAQRE1H2NOCBe0cRYoS7vf7iWKxjHXb1_mwt1JLgddlXUnAQ14LoTgG4rP7srXo0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38c6e037e9.mp4?token=vGI4aH7DPci5t2EGyQyZ7EKc50COxHiE_NSFEWso8WZ0QrUU5vMXjffRjzTttT18mLQUOKar-rHLHJ9AE6NyX-ETDBEBFkJg5yO8JSwO0wQi4mriSunA54OC-F-lg0lTy2VaQNMwyanPgPa1b8evkrfbrgVLj43OJw0QazOf60j4C8j7hAKwFSb8wlwCUZyoJ8wJgnAoSpzd2Jq30aONWXp0x12znuZaJE9781KmN0-_rAXp3Db48uVmdmWeujhkQdnswVDP8uvl4tPgBpl-0hU4yAT5CMawc3bvsuFVyj5IjPnZFQla4f3FSemu-0J8kPbsX_2aE3ylbIeDcCMkF5vj0gqmsACEkuaM2cIHBFMflJNJBnTqS5MaxtqYp9-w6QKo7YsX8NT4tT8AOdZyEyMqEgAm25a6ZTYtSLhlZmMKK_n5PpyMF-gnAd_TuaU1nZhFYWG_yGqZEowdeU29K1UqZPv_7lzZIdio7THFA-9pE-ipvFRR-LIcKBk_OkffFNil3OjqNMl2iBLnSstPsRc1Mra1xm_gWu3t0CeUdlGnEmjnQN-gbUPnUUh9QOSqNBba43dEeZD7pWiOv1vbZ0M7dMuXXHwKHKaXh7Ys9QGsAQRE1H2NOCBe0cRYoS7vf7iWKxjHXb1_mwt1JLgddlXUnAQ14LoTgG4rP7srXo0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
‼️
⚠️
محسن نامجو، مرداد نود و هشت:
کوروش ایرانی نبود. حافظ ایرانی نبود. ایران یه مفهوم جدیده مال صد سال قبله. گذشته‌گراها شاملو رو نمی‌شناسن عاشق فردوسی‌ان، می‌گن به فردوسی دست نزن. می‌گن گذشته‌مون بزرگه. گذشته ما کجاش بزرگه؟ یه شهر مثل پراگ داریم؟ ریشه‌ای وجود نداره. ما چیزی از خودمون نداریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/105163" target="_blank">📅 13:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105162">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabb21609a.mp4?token=ilnbgG73xP8Vt0NUH_dCrZHW62zNVhYU7dmlzPE1wsYR17X0MuXXm5b0LSzFIlNV3EI8lMeFc7QxaRmm3VbnYW2DcGLql3N_LvBYAmbx1g3BVntPaBKw9kQMtNbM2ofmPONeWZGuy8I71uFNxhWw6NRzDFg4f0_CeA3pEP5KuSjhCkAQ6s9ieLNYeYC5kG1PDeG8htNGV0PgSBPx53-vWbooVVb-5Eq7Q4GPIPmBqQdt0YNRrpStKV0Wbs7ifcRpQK_LTO3585fhRlnPoeSUC0WqtOx0ov4zdqOVumOAmUe57ByIJ2WPxPMdBsxLq0Ur39LOP4HcQHxSy5uY9xp5uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabb21609a.mp4?token=ilnbgG73xP8Vt0NUH_dCrZHW62zNVhYU7dmlzPE1wsYR17X0MuXXm5b0LSzFIlNV3EI8lMeFc7QxaRmm3VbnYW2DcGLql3N_LvBYAmbx1g3BVntPaBKw9kQMtNbM2ofmPONeWZGuy8I71uFNxhWw6NRzDFg4f0_CeA3pEP5KuSjhCkAQ6s9ieLNYeYC5kG1PDeG8htNGV0PgSBPx53-vWbooVVb-5Eq7Q4GPIPmBqQdt0YNRrpStKV0Wbs7ifcRpQK_LTO3585fhRlnPoeSUC0WqtOx0ov4zdqOVumOAmUe57ByIJ2WPxPMdBsxLq0Ur39LOP4HcQHxSy5uY9xp5uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
رحمان و رحیم سریال پایتخت: یه بار کار از دستمون در رفت جفتمون عاشق یه دختر شدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105162" target="_blank">📅 12:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105161">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j87VDv2PKSHVFqTDhVrsvD8hxEGXYhIl_IEtm5mwmIiYMmF9TtMPupRBkf5969jShxi6JpS2QmWRSsD61jn34IsVNzqGGUhk1CHmIlVWGA2XNUjs5lYyzSZc8q4Q-BNkfeQkyRWR1f5PSddkw-mzlq5t52Ceg4s_6bE9xcL2-sfsW0eNsrCcIZNq3uh5AXLXwK5eP3oXvXpob1lK8MsIuPOOqgHYMU3v72_8aqoxbq-ZhWwJQYmKB6L88jlGjPkd1eW4M8LoGWUAR-z2fdMaZxHN0Ci5xr8HeVbfCuKIdZdLoiDo07Lf4UoWqABECjk5PKkPUcAJCaitvqsAcILn9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
رومانو: میکاییل بازا مدافع ۱۹ ساله هامبورگ با عقد قراردادی به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105161" target="_blank">📅 12:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAUB3QHSSibNkurfWKE7-FoJ4aHzph_GtQ52_yT8BVbzcb8fVxQim7QZEg1TJlHDCWzdSx6BzsdT1v-zMr8mKwOrOjZU7JC0Q6ptHdoAWix8_l5gT-oeS1n7lNN8pkodksHId5yOv9K6kQraAyk_f_PBFVuRwSBVb_TTbnW6VlB6jFViurpe2foHVix4nxRt8oOQX4YOa33O2bmpU2ZalmJRgnxou4p0i3A75PtZ9utwgGNG_N748ecAxbfZ-V9xkfTkOlNR0Sprs-fCSdyuL88X1nmDnjp40tekInHcWRypmpRWZJ9dUWc6YKnseDWH8lD7e9lBFsvp_i1uPBhN-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جونیور بازیکن ۲۰ ساله برایتون بعد اینکه دیروز مقابل چلسی بازی کرد و بخاطر چهره‌اش و کچلی در این‌ سن و سال مورد حمله قرار گرفته بود، یه عکس از کودکی خودش منتشر کرد تا به شایعات پایان بده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105160" target="_blank">📅 12:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105158">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m_JbjPGR37CVZesET09vul3e8Nkdvj2FmZA3qyNHL_ozqg0gOm910V40l4EtXd57b6iFeBu_wE-LTIiO493TEOfxqWBdEdAnSRXmn5YUpNjIFhQ0Ne_p_-1sZDNTD5V1--3t08z-hIkdkwKU5j9GNJNrOFUHKapTlLzjFQRX2_S5x_OyRBkp-6Io9aSC6wUlmPGnf48JKZSaJG6UZCi0YAVsj3Ft8ql3QdXj8U-VmjwN7GYjXevL1Bm_j8iL-AMRRxxdi4D_g5zYycF6z562xXCflSKxTWQhMV_yduFfF6jgwEyfyGvvQrQA0ss8qYvK1dK1iKYteljo8IXci39D1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpG9KbSazuUirlq-mkSGhqyvVRbcjyR6Kn8dYxNqUJoKSErcPmH0OI-Y4N-nYYumX8XeBwH6aR66Ph2DBBMItJgBEVUGSCxu3rT59EEHsMlObQVTFSeQXstMYEcaX1T9ziDJSL75abynoCcXX_Q2W5HnS5fzZ5xiRHVTJjSEq11Gs7zaC6pNjT1NF99dDTK8TGieguxS09ai6gLMofaP9uPuGTp-UWVyJ_BwYwLFOrQfyuevnnL0cREonwqhqNWTX2PwIRSBB4RydUFUb7PlD_pot2Z4ywDQqUqZPdInmcBTWrxsB2AoANYVQQEHy4H7CN3V7cjcNYC2RLJz0HGodw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
مریم‌یکتایی گلر جدید تیم‌بانوان استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105158" target="_blank">📅 12:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105157">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
⚠️
درگیری فوق‌کیری و خشن در لیگ‌چهار برزیل؛ پشمام ببینین چجوری همو میزنن
😐
😐
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105157" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105156" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105156" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105155">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thqKRFZngJt_1hVdfktLVc7Q4G6xrKpf5mEp5YdwYrQs-DH-Lu_sFVK7wZj117XewmmfY5rI3dHg9_TTo32hC49ppjnv8zCe2Fy7hHcbS2xZdCgxrgZifmtNaQZPx2stE9nTQbjxMf2e8S37g9Z87JJ8SklKnJGrfHdPoyFfv68aFRarP6wpE4oZdI_VsB7uf3l3zrSL1dDx9fYL9oGLckZG2oF11wlCmTnvDY1cgCH_1wU3PYFpYLTDAgNn_cq5ApRtW7ke-MPaZHFnKEevLzC9NbXtp6puf9DPCf4zyFl-YjSofJsLKkbo4huozSnCCGhVPO6JN9N9jPfIa6wM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
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
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105155" target="_blank">📅 12:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105154">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b53bca956.mp4?token=ZEefMp6X2K4JltfaspC6EUH3QJMaqFDtq45l1BqDQH-0isDeNGCvcGMi2V8Nlf0U77EVv2_32UEpoBASohpVnar2COgaBxPYasUXp-Y-iCGcMSczin4g1dZFXBXyoluQAXmCNF8ylt7SFDn52SxNr1_Cj9H7gsYt_UUdO-hLEJ-lidYZ6DtAb1wU3aZhHbxU1-qJd0m_iHwea9AaVSc3zex75EnO654VB2IHoqCPMf26YTLrFpTMsnBHcx2z-L_fs_pCatmW2HYI_CsfRt7UwTKlkpL2eQPn3Y_RV97c9pON1xyQAalbfaBucWUvsP813RFLZkBEHx_NEUxYVvd4F3Jovx1CSxPl8SspyJO5XK-eXoCPXL3-cE5-gZvO3c6fPrpDeklXKaTlq_QoftzKe7yESHIViweMDqt31A4qvIVEigEwP0SMn2qBhne5b2jxbRKCJyvSGvDZEtosXcfn4EST4w3hLfevP2mPadgJljYxwv01GBrqR3WjD9eia2TLjhh5z7PS0NFJvioJXclkiSlD7stkbTdfb1y88gnDCSyTceLw69lzRa6KITpsJZgEssZjMPp2zKi4tyx0W5b4UtRTNrudY4vdu6l4w4QcGwhmCGvGcni0VoMkyzwcUkB9Dz2MBPWWBzr9DSD2GieTKJJvelt39amdc3WuAiHGxBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b53bca956.mp4?token=ZEefMp6X2K4JltfaspC6EUH3QJMaqFDtq45l1BqDQH-0isDeNGCvcGMi2V8Nlf0U77EVv2_32UEpoBASohpVnar2COgaBxPYasUXp-Y-iCGcMSczin4g1dZFXBXyoluQAXmCNF8ylt7SFDn52SxNr1_Cj9H7gsYt_UUdO-hLEJ-lidYZ6DtAb1wU3aZhHbxU1-qJd0m_iHwea9AaVSc3zex75EnO654VB2IHoqCPMf26YTLrFpTMsnBHcx2z-L_fs_pCatmW2HYI_CsfRt7UwTKlkpL2eQPn3Y_RV97c9pON1xyQAalbfaBucWUvsP813RFLZkBEHx_NEUxYVvd4F3Jovx1CSxPl8SspyJO5XK-eXoCPXL3-cE5-gZvO3c6fPrpDeklXKaTlq_QoftzKe7yESHIViweMDqt31A4qvIVEigEwP0SMn2qBhne5b2jxbRKCJyvSGvDZEtosXcfn4EST4w3hLfevP2mPadgJljYxwv01GBrqR3WjD9eia2TLjhh5z7PS0NFJvioJXclkiSlD7stkbTdfb1y88gnDCSyTceLw69lzRa6KITpsJZgEssZjMPp2zKi4tyx0W5b4UtRTNrudY4vdu6l4w4QcGwhmCGvGcni0VoMkyzwcUkB9Dz2MBPWWBzr9DSD2GieTKJJvelt39amdc3WuAiHGxBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
پشت‌پرده درگیری اخیر هواداران چادرملو اردکان با شجاع خلیل‌زاده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105154" target="_blank">📅 11:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105153">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🤯
🔥
رقص‌پاهای نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105153" target="_blank">📅 11:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105152">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ba1ea291.mp4?token=sq98eTEhm8IdRG4yFlV54RKhrDIijygi5_btUnzs5w2WYD1TbmIXGMBh1t9ZbtV6t04Phl1v81KYeRWb_Dm4RbSKZcsXJYBBD6ioHlhp4lz7tiNcyMPz2dUvV9ysCHApzt2Pa12sS59epG5ypfPDDfXyc0iZcz0cuYDRZXfFI7tPBCvqC1rD2ajF6O7RK7JX9NT8iIdGdFG7hBtvsrUoDJce9bX3Cy8509KiQIsca8dUZbxfPAFIOnTMWgf1LDc2-INTefoOEpjk9RdKo6WW-q8pLFOTDko8dkpMt2nXDV47l-wQqjIdb-P6-SmFKCUzwP1a6YIt6kkK7VlHf8n4og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ba1ea291.mp4?token=sq98eTEhm8IdRG4yFlV54RKhrDIijygi5_btUnzs5w2WYD1TbmIXGMBh1t9ZbtV6t04Phl1v81KYeRWb_Dm4RbSKZcsXJYBBD6ioHlhp4lz7tiNcyMPz2dUvV9ysCHApzt2Pa12sS59epG5ypfPDDfXyc0iZcz0cuYDRZXfFI7tPBCvqC1rD2ajF6O7RK7JX9NT8iIdGdFG7hBtvsrUoDJce9bX3Cy8509KiQIsca8dUZbxfPAFIOnTMWgf1LDc2-INTefoOEpjk9RdKo6WW-q8pLFOTDko8dkpMt2nXDV47l-wQqjIdb-P6-SmFKCUzwP1a6YIt6kkK7VlHf8n4og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
خبرنگار: سرمربی مالاگا بعد از بازی گفته که داوری تأثیری روی نتیجه بازی نداشته، اما این حس رو می‌داده که اگه بازیکنای رئال مادرید رو فوت کنیم، خطا می‌گیره؛ در حالی که بازیکنای ما باید خونریزی می‌کردن تا خطا بگیره. نظرت در مورد صحبتاش چیه؟⁣
⁣
❌
🇪🇸
ژوزه مورینیو: ارزش اظهارنظر نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105152" target="_blank">📅 11:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105151">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyWYL-nGBy452i1SjAOAuuvaII8EkmFi1lTcxpU6FyX52z1_M1eOijNZqAPArZ45C3zGsT7tJsc4EzURm3PHHtbhLLjnlJGIcfqnSzECv5QOJnBr1BfRvrWkgU3Y_GWJNCy2HKv-y6K7X7eNEDg_mI2xaCt3T3FKSLiKCO4VLEecsXl27S2v31VNgAl-8JmSQ_ZUZ5412g9QULYdFzLR6hNymafJL9LZ5InSNy6CY_x6fAj7oqaheEqBwj0GREmYlQABj7aVrg8TndYjCuEKfY2B_Da3txrsVM4gSsp_kgy7nmSv8B0PV0zONyRf2TLf057iBCe9rpxjxThkq6X5EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
بلیت‌فروشی دربی پایتخت تا ساعاتی دیگر از طریق سایت فعال خواهد شد. ظرفیت این مسابقه به شکل برابر تقسیم شده است. ۲۹ هزار بلیت برای آقایان و ۶ هزار بلیت برای بانوان به فروش خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105151" target="_blank">📅 10:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105150">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqkCiaCrUXPTxQ9tg7RXdPkeGnpE0VJVLXcRSHiEKuX8N-Q0dPLZ56QVZtGuxRVFOg7L5qX5PxINrZHV6RLoB3tdfFkMejra2WkpZf1yS7qybMz_qxm9nC7NbPpeGF007kUnSxa49X-QP-BxkmUIKswj6_FMzCBxdwnixYgiw4MfysC3W3bxBVcRO9V4h2SRxG5Iy6-VLHKx18A0ZB-QIjL2iLceDQzKFC-km90Y6p9NIbhJWF5fTc4klU9ZBB30NLDdYS4w5wYEPO8NmTW69NwTczEP4cRs4Kj3ct8890FOuG-MUkWwM7Knys7Jh7jLEIre-Zh3WfsSG0Xs4jrOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚪️
پس از اتفاقات جنجالی اخیر تورنمنت سه‌جانبه، هدایت ممبینی از دبیرکلی فدراسیون اخراج و حامد مومنی موقتا جانشین وی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105150" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105149">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚑
❌
🇮🇷
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/105149" target="_blank">📅 10:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQHXqy5I-Ltb8650yy0zI0gygiAZcWRf62yL39uMk3MtBB5Mv6A7h3iTnthfbAt1kGmWzegOHbjIVavpZW4bL2RIjPQHv5f2zBZBk5XuoC3zKAaVMo2QQmfVO-pKjd0wIAgcbOSt0p1KYT0U8AQhmAMhGnbUEM9ldcFeE6hbt_Tk_YweegYc1ysBEgIMc_qQTSyK6Sia6_ucOo_j3XhTyoHASrIXdaSQBwFwiFQFG5rZfwdB7ZcVB2fhfw3Ajq_EmbWzuScdV9oRR4Bp_k4vyFEIW0aLDTco4iXHhrH1Sscymco9zvZWxFrS090QM0V5HSAjcWWSV2UNFBk6igCpIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🇮🇷
آمار فوق‌العاده تراکتور در تاریخ لیگ‌برتر؛ تنها تیمی که ۴ بازی ابتدایی با کلین‌شیت برده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105148" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚽️
🔥
یه فرصت خاص و دوست‌داشتنی برای فوتبالی‌ها!
کارت‌های حساب پس‌انداز وینگر بانک اقتصادنوین، این بار با ۴ طرح جدید و جذاب
👇
⚡️
مسی | رونالدو | امباپه | یامال
و یه خبر هیجان‌انگیزتر!
🤩
💳
این کارت‌ها تنها و تنها در نمایشگاه الکامپ امسال در دسترس شما هستن.
📅
۹ تا ۱۲ شهریور
📍
محل دائمی نمایشگاه‌های بین‌المللی تهران
🏢
سالن ۷، غرفه ۲۸ | غرفه بانک اقتصادنوین
🌐
https://enbank.ir/fa/page/101088.html</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105147" target="_blank">📅 10:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b7206c7d.mp4?token=RPIJ3YmQjIjpJYhtfAlqFoyfbitEh_mJWBEu4ikOZCcFATha1vi0IAQQ5953D2genHYGReO1XVuff4nvDbfJdnYCgUazO5yGv5Fjq4Mx-B8zJ5Uv5gH95CRWI6K-cxmMQkJFEIl-MC5iW9soA1Hyy_R1GpLcqi6QBPONs6wq-A_fPM5ASHaZcOVf8AVMTcR16fvX9LPsaED5M0suKh69_w_MRAcTEgZj4phQKIg0eUoPPFrvUwG2d1wFyUEqYnJm7cQw9x9o5ZYlraZ25pv7chWQoFpKfUb4EWn6pjch_OsQPC_PyoiDBFTUNfhUtVeoAXChS_7V8CzTpFECPMGAMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b7206c7d.mp4?token=RPIJ3YmQjIjpJYhtfAlqFoyfbitEh_mJWBEu4ikOZCcFATha1vi0IAQQ5953D2genHYGReO1XVuff4nvDbfJdnYCgUazO5yGv5Fjq4Mx-B8zJ5Uv5gH95CRWI6K-cxmMQkJFEIl-MC5iW9soA1Hyy_R1GpLcqi6QBPONs6wq-A_fPM5ASHaZcOVf8AVMTcR16fvX9LPsaED5M0suKh69_w_MRAcTEgZj4phQKIg0eUoPPFrvUwG2d1wFyUEqYnJm7cQw9x9o5ZYlraZ25pv7chWQoFpKfUb4EWn6pjch_OsQPC_PyoiDBFTUNfhUtVeoAXChS_7V8CzTpFECPMGAMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
حسرت ششمین قهرمانی اروپا از ۱۰ سال گذشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105146" target="_blank">📅 09:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/793fcfe694.mp4?token=sny8sJsFFECw9RqhaNwWQmulGKUyRM4AaQ00Y_QgjRAujibApmWZJmkJXOYORWIQoMgvWYnx78LYtGGfszCtWxrvGPCG3qYjp1AiOE0Wt4eFioHo-nem6jfzzCl0StRlgUjUJi1Ok-dRuMa3zV3qWdWhLLp6y3GtljamLOSP_c_PkBq8MXnYqtQyDoPzBWHN0Xhck4m0FfJVXUxQh7OWbT0RcgWAlMqnbWLizvcqyWg0nkQO-mcOsnKGTDtnTCSwAkiWu_kDLLNS6ggBCLhg59B_YyJlHMS_jiXCnJzxBsWz8lsVrq0m7Sxl9uhxgZQTGp8fmTfYjHJtsw0o-gpj7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/793fcfe694.mp4?token=sny8sJsFFECw9RqhaNwWQmulGKUyRM4AaQ00Y_QgjRAujibApmWZJmkJXOYORWIQoMgvWYnx78LYtGGfszCtWxrvGPCG3qYjp1AiOE0Wt4eFioHo-nem6jfzzCl0StRlgUjUJi1Ok-dRuMa3zV3qWdWhLLp6y3GtljamLOSP_c_PkBq8MXnYqtQyDoPzBWHN0Xhck4m0FfJVXUxQh7OWbT0RcgWAlMqnbWLizvcqyWg0nkQO-mcOsnKGTDtnTCSwAkiWu_kDLLNS6ggBCLhg59B_YyJlHMS_jiXCnJzxBsWz8lsVrq0m7Sxl9uhxgZQTGp8fmTfYjHJtsw0o-gpj7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧊
✅
این‌ویدیو بسیار کاربردی برای دوستانی که عاشق‌ درست کردن معمای روبیک‌هستن ولی کار باهاش بلد نیستن. بفرستید واسه رفقاتون عشق کنن
😁
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105145" target="_blank">📅 09:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7e507ebd.mp4?token=YLWw7zyljCN-VCj1hDdlRoVLXtJ8oQvYFYYC4rIwvAk4njvPkZYRdSMxo2cG-YabY3ezAVtH-E59IBPDZPNqblebwYSW8xfeYC-6-_6h5Rn6QUlAnUeAmSYRWTtBPLLDpHpmBBHaj37ACJopzNrnaen_1O3A5K8LDMz0qD_2pMJsljEpB7TcPU88hCC3hIv1CkpOcArNC3QzNWR-qfjn13UJNLS8Be-oVxcaN8AtCBLCZzf1hwcC058Vw8a4_M2mEQlFENruM7z2wsUTXWwmyoefNgiOszGvHDmqujCC-sTmaJtEPGhqFEPo_p_6KRmy9Q4d5TwZAxNsJQyj-xmqkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7e507ebd.mp4?token=YLWw7zyljCN-VCj1hDdlRoVLXtJ8oQvYFYYC4rIwvAk4njvPkZYRdSMxo2cG-YabY3ezAVtH-E59IBPDZPNqblebwYSW8xfeYC-6-_6h5Rn6QUlAnUeAmSYRWTtBPLLDpHpmBBHaj37ACJopzNrnaen_1O3A5K8LDMz0qD_2pMJsljEpB7TcPU88hCC3hIv1CkpOcArNC3QzNWR-qfjn13UJNLS8Be-oVxcaN8AtCBLCZzf1hwcC058Vw8a4_M2mEQlFENruM7z2wsUTXWwmyoefNgiOszGvHDmqujCC-sTmaJtEPGhqFEPo_p_6KRmy9Q4d5TwZAxNsJQyj-xmqkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
رسول مجیدی مجری شبکه‌ورزش: خداداد عزیزی رو آنتن غیر قابل کنترله..!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105144" target="_blank">📅 09:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105143">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105143" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105143" target="_blank">📅 02:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105142">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL7npcIdHeMNUVXtp7_UF-Nhll8iccDlTx4SllqHUBAW_-JHDwBWJwZFwmQvko-NGQYMiWREtCDNijHwUp1KZyVJpShbSWaeuOTm818OBejkFn9BGY8UH8p1TtkzRc9yDGaFNA0rUqelao1SOG0AusWd9JFo-2CyjDOOQycXuA7nArpvcsxsobli-Lb9qBvc29STjlmReNXwzxEynRmenF2J6bmJB-K4mvNJL_eJNqUCVGd_ULsRgGx5qqRhJXUxXs_cajg8DGpvvWyiguNx0JH87Ui_NZ3avnqWetLIqpyUoOfKxnKhYFvyzCXeBJ5VELEfdKciKZ1CZ4fee4qCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105142" target="_blank">📅 02:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105141">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105141" target="_blank">📅 02:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105140">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=IdpIzAy1axxLB8je6DeTml7Jgp4dKVM8azrobjN1kyyQX2mSaVPULaoEPGafY1HCOgSG92iEXZGvgFiS0pzjFVeLF5X0WuOWgoTtIkJE9D4iQNNEWF5hmJZMigKsDogqFMgBXtgriz62U6dV3oJ4c9mPS3Q8YVr1-gRAGsVyOE5nRgPu5QmqdhbtQyHML_Z_p0_0ul2NDzaM4Zz6kFiK8Q4xvNKnFDtSHE6ZbY_F0TjoxuOfqM_Rm-8vjLi-eo1M_Ri9DCARd1112UqXM1WOv4R-jEJCE7axMQySB__lmKIKRVnvqK6yWF5dTAS5n4aU4cLyrsZzJCkV-nRlo9-1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2d04d67d.mp4?token=IdpIzAy1axxLB8je6DeTml7Jgp4dKVM8azrobjN1kyyQX2mSaVPULaoEPGafY1HCOgSG92iEXZGvgFiS0pzjFVeLF5X0WuOWgoTtIkJE9D4iQNNEWF5hmJZMigKsDogqFMgBXtgriz62U6dV3oJ4c9mPS3Q8YVr1-gRAGsVyOE5nRgPu5QmqdhbtQyHML_Z_p0_0ul2NDzaM4Zz6kFiK8Q4xvNKnFDtSHE6ZbY_F0TjoxuOfqM_Rm-8vjLi-eo1M_Ri9DCARd1112UqXM1WOv4R-jEJCE7axMQySB__lmKIKRVnvqK6yWF5dTAS5n4aU4cLyrsZzJCkV-nRlo9-1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
پایگاه العدید قطر مورد هجوم موشک‌های سپاه قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/105140" target="_blank">📅 01:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105139">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19f322eb80.mp4?token=rI9oPBo8hGufH6WBKIVRgfO_8DUuAEtfy4ZhFMKaOlp7RgxVX5n72MVbeDdtA8QW7ie-B4fqe0ThlnfjavMrZVgUdo-HArWmwdgMQmaaFeEOna7izcOPaltjx34nCQJ91QR1CaCspN6wLX8Ur_YqQwrY95TeXQVcbOXk7iA-DepwE2uMBF8XmgFbDi2BF4YbXJ1N3yyZjJI7GdDlKu3MBK_aEq5gXYxOmGDDwBKT1YnWUh3GxQxZCFjwpW-7FDXpUV3NUUosqP-vYi_y4fEL0dLs-74a96l1u6F_54j4WOtV5Yc1aw7FNP8ixKGi-adfRRw_xnkh8PrNNc8DH8ErOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19f322eb80.mp4?token=rI9oPBo8hGufH6WBKIVRgfO_8DUuAEtfy4ZhFMKaOlp7RgxVX5n72MVbeDdtA8QW7ie-B4fqe0ThlnfjavMrZVgUdo-HArWmwdgMQmaaFeEOna7izcOPaltjx34nCQJ91QR1CaCspN6wLX8Ur_YqQwrY95TeXQVcbOXk7iA-DepwE2uMBF8XmgFbDi2BF4YbXJ1N3yyZjJI7GdDlKu3MBK_aEq5gXYxOmGDDwBKT1YnWUh3GxQxZCFjwpW-7FDXpUV3NUUosqP-vYi_y4fEL0dLs-74a96l1u6F_54j4WOtV5Yc1aw7FNP8ixKGi-adfRRw_xnkh8PrNNc8DH8ErOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اولین تصاویر منتسب به شلیک موشک از ایران به سوی کشورهای منطقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105139" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105138">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
فرودگاه مهرآباد تهران مطابق روال گذشته به فعالیت‌ش ادامه خواهد داد و اخبار تعطیلی فرودگاه تکذیب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/105138" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105136">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=suuGw-T3tV5Pf38mEQ_6EIi9yVIl7gY0TwVinIpCZC5u_wo6fhn91ky61-CxnKP_PhcslWg0AX2nZrBPKX0mxhHLjjoc-v25n_4Krqt_62EseMZJLg1LrP44J0sOn0h5PXbE49aBepWOpiA4cpKAGP7KjuMr8VPOp89jf5vWoJtIZwuOVT9Fz58arphTArD7zGF8Gdm7iLlIT-gcjLknN69inZrTO0Pq19BUGco-3eL163u2oJ2H5KIgCeBfaPxnRHSO6hT60_HrjY8QakUYGk2fiakmDq2f-STSGtnEyTMAhSMd1qz4JIF9ZFe4IgwF6U1D-nb0wGu_N4c-Kv1vuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=suuGw-T3tV5Pf38mEQ_6EIi9yVIl7gY0TwVinIpCZC5u_wo6fhn91ky61-CxnKP_PhcslWg0AX2nZrBPKX0mxhHLjjoc-v25n_4Krqt_62EseMZJLg1LrP44J0sOn0h5PXbE49aBepWOpiA4cpKAGP7KjuMr8VPOp89jf5vWoJtIZwuOVT9Fz58arphTArD7zGF8Gdm7iLlIT-gcjLknN69inZrTO0Pq19BUGco-3eL163u2oJ2H5KIgCeBfaPxnRHSO6hT60_HrjY8QakUYGk2fiakmDq2f-STSGtnEyTMAhSMd1qz4JIF9ZFe4IgwF6U1D-nb0wGu_N4c-Kv1vuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
اولین تصاویر منتسب به شلیک موشک از ایران به سوی کشورهای منطقه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/105136" target="_blank">📅 01:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105135">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
شلیک‌اولین موج موشکی از نواحی مرکزی ایران به سمت اهداف آمریکا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105135" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105134">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jJrYOeXXm494IAGg7fcvnnzL4Ls5I0120xXq-nukmvNZ7GRVTdGjqQEOwoLSALAj330Mfx1gbFf4JebYPSeD-At3X5LkaOm7nBrCMuwJ1mhM2jRd9zuUMbzsrIXn814lfsMr03fOJ0fJwngSoqiV98EbH6s0u83mKHtHdbM5oI8JkvIj2aQXhqA1XxxDEJ2HP9ZVDWu5IjJSF_UCMCH3N436-v-04EAezIP22vP6bvNHh2Lf2IYhbpLV_xq-0llpwDg96ZByOA857R1AD8fhVCa-Sj9eJewBIOYKHrueBmjeOomgDJhxUEbOmfu2xDb42r9zFKWBjuuG4bpAn7K9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇫🇷
جدول لوشامپیونه تا پایان هفته‌دوم مسابقات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105134" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105133">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370a134319.mp4?token=FbODYZdl-wzoSMRWsoYL-Y06C2TGAn5euSY3U61gWii3esEKVi94Qdr3XKnJTOTQ7FBAqZtaesHxJcdwDEEpfK81d5jJrWO5-it3LAPJVc_Gtyv2f1qRsCF3FkuzgZQ5LQIIsWQROLlpn7UHfs_AFROSu7nXI-602mlcZTKmeurTSLmjJ0yKRb1FjZStN11TrvHUnAZUlHiCu1lCswsqIeluDbO2N-KmYFg3vXCOPb0ZRj4PrGVGzuvhiKjCOInIG6a42SJ422E6IFkONpejB98LlR2TnvSZmna4GsKGBkkRyhAU4SA4sOTtIWIwtWlrKLfIRWc_kj8LT8aXO6jleQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370a134319.mp4?token=FbODYZdl-wzoSMRWsoYL-Y06C2TGAn5euSY3U61gWii3esEKVi94Qdr3XKnJTOTQ7FBAqZtaesHxJcdwDEEpfK81d5jJrWO5-it3LAPJVc_Gtyv2f1qRsCF3FkuzgZQ5LQIIsWQROLlpn7UHfs_AFROSu7nXI-602mlcZTKmeurTSLmjJ0yKRb1FjZStN11TrvHUnAZUlHiCu1lCswsqIeluDbO2N-KmYFg3vXCOPb0ZRj4PrGVGzuvhiKjCOInIG6a42SJ422E6IFkONpejB98LlR2TnvSZmna4GsKGBkkRyhAU4SA4sOTtIWIwtWlrKLfIRWc_kj8LT8aXO6jleQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇱
نتانیاهو:
ایران در تلاش است تا برنامه هسته‌ای خود را از سر بگیرد، و مادامی که در این سمت باشم، مانع از این کار خواهم شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/105133" target="_blank">📅 00:36 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105132">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
در پی حمله ارتش آمریکا به جزیره لارک، شماری از افراد سپاهی کشته شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/105132" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105131">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
در پی حمله ارتش آمریکا به جزیره لارک، شماری از افراد سپاهی کشته
شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/105131" target="_blank">📅 22:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105130">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbWi4zknP3dKCk6JKvc0jHyZUoiOLjNQWr5pdZTTPhQyQZ1taoO26CFgl5JAk5snm0SRxuE2HWZItVcXdSbGj2mso8wbOWykuQXyr9qKBNCH3nAyvF7QfIwCNnKnOr1Ziuq9Gzb14JmP_bXi9Tm4CdOXu0CA97goXdhi_MIBXATpuf-MRVQ0EbIfcjgnScFX_jgFJV7MGuFyBhqEovsZ6yi01iPhCZHgHbUmCgfJ65hkJjNaOtLLcjBwtkdv3ZlVXNpA3iW_NZsvaknxlOsldBmgwxfsq_zqY8XfLO5eWVBnhD5Felj5kpH_nJUok1nWeDGRS21wmdMgQYXs884y0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180؛ کوپال‌ناظمی از سوی کمیته داوران شانس اصلی قضاوت در دربی روز چهارشنبه معرفی شده و قرار است تا روز دوشنبه تصمیم‌گیری نهایی صورت بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/105130" target="_blank">📅 22:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105129">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/105129" target="_blank">📅 22:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105128">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c996886b7e.mp4?token=e2MiAB886WR9YV-upN2Zkv9NhqS9RxRe6mVkq-YqpqUdQp8_Ss7j8US342jLZfQ54PS0JjrJaFJCidL7GkRl9GfXu6Oz4izvCMPzJ0ozFbB6PC-wlLg5ZWlAn62StyZDUUIQA2O1owHoASpkIv_jDjWsNIjZFggsHp6ZxDheAHe2-BnAF6I4hd2YtIVwSHdke2UDIeVeaHxO_M_JLGTZ-gsPxLEoJFrQH4u3Nppa9k-Ub7mSs7D_0ym6RCWE2QAYr0Caqu8ifUCuiuY0ejhRZhll-zSBEINaC89KVPyjn0s64HTFLkEym_JF5VdUkPU0bmaWYVqON3Gj5wIXsTvnng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c996886b7e.mp4?token=e2MiAB886WR9YV-upN2Zkv9NhqS9RxRe6mVkq-YqpqUdQp8_Ss7j8US342jLZfQ54PS0JjrJaFJCidL7GkRl9GfXu6Oz4izvCMPzJ0ozFbB6PC-wlLg5ZWlAn62StyZDUUIQA2O1owHoASpkIv_jDjWsNIjZFggsHp6ZxDheAHe2-BnAF6I4hd2YtIVwSHdke2UDIeVeaHxO_M_JLGTZ-gsPxLEoJFrQH4u3Nppa9k-Ub7mSs7D_0ym6RCWE2QAYr0Caqu8ifUCuiuY0ejhRZhll-zSBEINaC89KVPyjn0s64HTFLkEym_JF5VdUkPU0bmaWYVqON3Gj5wIXsTvnng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه نیکبخت واحدی به رامین رضاییان
📝
نیکبخت واحدی: من نه در کوچه و خیابان می دوم ولی سیکس پک دارم! (شوخی) اسم نبرید آقا از کسی، من نیکبختم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/105128" target="_blank">📅 22:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105127">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d54666045.mp4?token=rjgdgOBGrrcDq9Rn5tjn3Ru0GH4WpfinC8gHGr7fwqGyGH8V3fY87jv_oMWkrvt61z6GBSRx-Em9BZUEeSZSz7UVs-ewZc0PM8XS2mls6vL6LIxf76_daANofG1i4OoAYIN9l1oFJphjKfj_2bYwOVJYTvb37CRmaALy1X38PqocbWTT8C58-Y7iniUXtCImTHYiQfn4rNIZU6_sk2dFx38a-tkBEvPpaokVzz6ViyO6a3u4Qcqr9x1Os-YzoeTZERS-8uiGFzksjRyimh-lIhf6xZEbwvKSNhb82Ae3uL2LTW7sm2PzvE5RgIYtJWlamM0JNzqkearjH0qHQbvQwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d54666045.mp4?token=rjgdgOBGrrcDq9Rn5tjn3Ru0GH4WpfinC8gHGr7fwqGyGH8V3fY87jv_oMWkrvt61z6GBSRx-Em9BZUEeSZSz7UVs-ewZc0PM8XS2mls6vL6LIxf76_daANofG1i4OoAYIN9l1oFJphjKfj_2bYwOVJYTvb37CRmaALy1X38PqocbWTT8C58-Y7iniUXtCImTHYiQfn4rNIZU6_sk2dFx38a-tkBEvPpaokVzz6ViyO6a3u4Qcqr9x1Os-YzoeTZERS-8uiGFzksjRyimh-lIhf6xZEbwvKSNhb82Ae3uL2LTW7sm2PzvE5RgIYtJWlamM0JNzqkearjH0qHQbvQwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
😳
کسخل‌کردن مهدی‌طارمی توسط بازیکن شباب‌الاهلی در بازی اخیر الوصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/105127" target="_blank">📅 21:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105126">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxAyKjhUM4G15gia2EFm9cUoynpO5GF2S5mtYR2fOnl4Igk9emYWJLpzGE0LWgAN5aHWJ0ejEhbPTUtYhVzpCsn0vK-0hAtJWYhYFFkaPBGTexEfzjApkhcvx4baqkAe48XgUbBSD0QfT1WsTspapPLmmFdiH-3wsOod6C2NXUDfu4N9A675TSfetodnoiFRBa7olGA-t0VGr-8EWA49zbhLytlkcRrMJ8rfFqOhMpYjtI-o-vYltQBt7oGiS7GxOXIm-joJrKLu7p2u22v4T1P_SgwLHKE_-GZbNeHfccEYc2TqIl3jiqERG004lury3L5nQoLypIIaf9GonQSlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105126" target="_blank">📅 20:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105125">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">منچستر سه تا به ایپسویچ زده برونو فرناندز دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/105125" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105124">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گگگل چهارم رئال‌مادرید توسط آردا گولر</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105124" target="_blank">📅 20:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105123">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">منچستر سه تا به ایپسویچ زده
برونو فرناندز دبل کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/105123" target="_blank">📅 20:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105122">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🔵
❌
کریم‌بنزما فرانسوی بزودی باشگاه الهلال عربستان را ترک خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105122" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105121">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=vCNyR7wB1nC5d6MrYGLbVHEl23hMHouwODT7STssx0-WEq9DDBhh4hU7DdYFAu-sUycwho0eEhMHcg6D_Xa52Nt00YP1_Na49uO2sEGRMlscq-LgRFbX4Br5JxjBGlbqHb6TyeOviJC_BN-0_Vkf1sMfRntgrOgaMqpg2E0pyjW7W48rHsu-w1kpUyFZ-GjUQVPLAF8mjxVtkaOwf5kBApFEP48pfp9Nx_CBa-o2wj3hEwB_XY0VBodot-R6j7UJjWSHqRhR8a5CagTnXm6T2W3ZVd2caqutqk6bukG-4QrN520o7ER4AUihdzUzMkFbhWn_wj_Th_gcBx0OA9A2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26beec0b11.mp4?token=vCNyR7wB1nC5d6MrYGLbVHEl23hMHouwODT7STssx0-WEq9DDBhh4hU7DdYFAu-sUycwho0eEhMHcg6D_Xa52Nt00YP1_Na49uO2sEGRMlscq-LgRFbX4Br5JxjBGlbqHb6TyeOviJC_BN-0_Vkf1sMfRntgrOgaMqpg2E0pyjW7W48rHsu-w1kpUyFZ-GjUQVPLAF8mjxVtkaOwf5kBApFEP48pfp9Nx_CBa-o2wj3hEwB_XY0VBodot-R6j7UJjWSHqRhR8a5CagTnXm6T2W3ZVd2caqutqk6bukG-4QrN520o7ER4AUihdzUzMkFbhWn_wj_Th_gcBx0OA9A2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇦🇪
فرشید باقری: بعد از باخت ۶-١ استقلال به العین منصوریان در آسانسور بلند بلند می‌خندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105121" target="_blank">📅 19:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105119">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105119" target="_blank">📅 19:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105118">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=YQR5wsGO-DA6Dex_LqmjRvRwlEmooNuPAKh-kA85f1PZweyaPykAfu1Fws7uckSzvlatBER0LKY8HVhih5mMBWnWNZT_crrhOBJvW-0PKtU3Qkih_8mvqGzRPECb6moYP8iJWKnlKKRajGaSw6RNg-_xWZDxkZhXGVfw2rIdHNFw6bs0LszyhlegyUcWmdiqNQDFIoD5B1kvuvLPIM5Wv7dg8S_QwIMunSuBVVgJMemunIGj5hHMW0FYJj5MI1NOKjmiBLSJfTH8Or1WfznLlG30g3UyGhyDVyxV5NtyIdyvgneRwp5_M39h2dN0F6Bz9XWZ-MgJ1fFe400XXoZJRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50c131dd4b.mp4?token=YQR5wsGO-DA6Dex_LqmjRvRwlEmooNuPAKh-kA85f1PZweyaPykAfu1Fws7uckSzvlatBER0LKY8HVhih5mMBWnWNZT_crrhOBJvW-0PKtU3Qkih_8mvqGzRPECb6moYP8iJWKnlKKRajGaSw6RNg-_xWZDxkZhXGVfw2rIdHNFw6bs0LszyhlegyUcWmdiqNQDFIoD5B1kvuvLPIM5Wv7dg8S_QwIMunSuBVVgJMemunIGj5hHMW0FYJj5MI1NOKjmiBLSJfTH8Or1WfznLlG30g3UyGhyDVyxV5NtyIdyvgneRwp5_M39h2dN0F6Bz9XWZ-MgJ1fFe400XXoZJRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بیچاره اسطوره فرگوسن با این وضعیت میاد اولدترافورد بازی تیم‌فلک‌زده کریک رو ببینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105118" target="_blank">📅 19:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105117">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یونایتد ذلیل مرده دوباره گل خورد
😐
😂</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105117" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105116">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
حمیدرضا گرشاسبی مدیرعامل فولاد علیه استقلال: شروع‌کننده اتفاقات بازی، هواداران استقلال تهران بودند که پرچم فولاد را آتش زدند هواداران ما بعد از ورود هواداران استقلال وارد ورزشگاه شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105116" target="_blank">📅 19:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105114">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8oAEza6Y7DjEnr77ZDKcZMMxjpJngxl7-RgOAH__aX7P-F58n7lH9RbT13jpIB0X2HbNeQYQlUPUY3MJTSC2yAdYPA6fzlguYTB6h3O2I7izsjLUFVnakXf3PBp5DgmLZYHIniffucJn_4EJJtG5nPVpf08vLB0GxQpfc7WmvTE6U8KMXdKQC3_f6Pd5WFXYaZ3Q8gQ8q9zqq8s27DBt8DyBEnuMjUWyEV4cgFTJVG3iqhPADwfuuz-8tAH6X4Lf91a22SY9aA4VX3_dCBOdSmR6kKFoQztQmO6qdPi_RLHUPtYaMABwxeQ5p9h_-YvVoYqg_iw5PEhAcJLdOQnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
استر اکسپوزیتو دوست دختر امباپه تو ورزشگاهه و داره بازی رئال مادرید رو می‌بینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105114" target="_blank">📅 19:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105112">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😆
-
😏
مالاگا  دقیقه ۳۰</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105112" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105111">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امباپه سومیییییییی زدددددددد
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105111" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105110">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105110" target="_blank">📅 19:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105108">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😀
-
😏
مالاگا  دقیقه ۲۵</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105108" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105107">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دبلللللللل بلینگهاممممممم
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105107" target="_blank">📅 18:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105106">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105106" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105105">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTmsHU-O_wIE8EtnYtob2UykC3Ttc5xG9FxPxsc1b6c0RM3OVEimuOKQjoS6e_mvxg_WOT4b94BdSfXvi11JYsL9ogaqX4HVSHltM9F1O5psgywSaSfZf2bjLoOuIeCimO0cTAL_rtDZ34ER93Zs6IrDSKqb-U0USd-kgp5Ed2jN__n685YYtquMxAC_Yxh3AlqAFkFM_1yQTskEvdUN9e3SI8d6TKUbLaSSp5fSxPWKayOx2XBYgRn482rvKJk_g_uzpQcUosUsuC1kk-1iaVpVhYSlFYV0PbXbaK_2LWvMoGjYauzs8JZsSjgfAOBMRCzTIkKlCQo71nSg_BXPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
‼️
تایید خبر اختصاصی فوتبال180
🔻
در اتفاقی عجیب و کم‌سابقه، از بین نفرات دعوت شده به تیم‌ملی امید تنها سهیل صحرایی از گل‌گهر و مسعود محبی از خیبر خرم‌آباد خود را به کادرفنی تیم‌امید معرفی کرده و سایر نفرات از حضور در اردو سرباز زده‌اند! قرار است عبدی فردا…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105105" target="_blank">📅 18:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105104">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔥
🔥
🔥
رئال‌مادرید
😃
-
😏
مالاگا  دقیقه ۱۹</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105104" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105103">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بلینگهاااامممممممممم
🔥
🔥
🔥
🔥
🇪🇸</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105103" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105102">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گلگگلگلگگلگگلگلگاگاگگاگاگاگاگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105102" target="_blank">📅 18:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105101">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw4wZU611lIu8NKNAoFskAe7zbYjUjLWz3bkPWuh7D9KVv1FMUAEQRJVJUJ94v80kZ1mEOSRNObNWsPH710LGbKOZ-SBSN9d0k_wQWuaVfKxYkH7-RUiQZSl_LEbCWnaKX8qNS7VmdrXltoiPEbEhLZ7SoNE1ER5M2nvGMfzOaVZXsZhoXRvpXyyD7mBIeD6SpoDKQcBVB-_rV-Pe-__sF-RwOHOG_vk4eHOcOMy1-Me5BzF26uWu_LOdyhzo6HZ7dCsmGOwRLFN4GRznpLBwSwdFVjKyxLVmTH-I6y81mFJkoNo5LlfldKHPX588lZwJtwKVwYZZERzDU75wjzU2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
مقایسه خط حمله الهلال و‌ النصر عربستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105101" target="_blank">📅 18:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105100">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl4C4rqbzpIQgraUPxSEMffBv5tK_KalGPRiQ3e-KnJFN5lOgnY0nsUWS0_XkBgrpMPJddcllZfO5Gi4g_IfATPPHR_oe6PXjzLzEBChQNQx-HRgL-mCdCFEztpO78X9x6QLwEPLXjf-L1EIhhrNGIvlzT0zUmph_Ny5GNrTvxf0NXk1_543ChcZVnZtYu-xxRIKKXDHHT1B9m5ouJxfZX-p59VRTDyjqRSqEQN_w_cn-mh5Ld2QVCU6hlnA4qkM5j7b_F-jkAhgjLysYnt12A6MfR-eN1KFUDQFoJIKCSNIXfLAQBAXTnikrr3kfWIsCXg6slHs31E_cvSGVHj7Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔵
#فوووووری؛ گابریل مارتینلی از آرسنال به الهلال عربستان؛ HERE WE GO
💸
مبلغ 65 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/105100" target="_blank">📅 18:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105099">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایت بازی پرگل و دیدنی چلسی 4-3 برایتون با گزارش شایان آقایی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/105099" target="_blank">📅 18:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105098">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAiwXrpe9OH34tYlDuUR9-Pem_kObPUHx4Jpdc7mkMBEDZXGIafbP7x7lBTxfNGVsw2mhB58HR6kZ5MQyQsqCt-tKypCo4k0VU_LXb0WtViazjxVg7kfIAaXSHccpqIvhSBKGSpuynhf_V4ILjmbRQyPQPSjMnc-9ZlkafJV50x_WS41S9jCV6CL4qQ6YMgctB_Sas6RxruxikTppxQED4YNYIMKfvJ-aXPTk0yw8Gz0iR5VAykOepXVpUU1btrwxSDihfUYyQuf8VgrPjz8r8JZJvHPsX2CxL1W9AUaUvJOdhl_sz-3HKSacLGwwkw-dl09-GiP35Ls7zJe-UWNMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم پریمیرلیگ؛ پیروزی سخت شیرین در روز رونمایی از مارتینز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
😀
-
😆
برایتون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105098" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105097">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZNgxMpt9z3hRaUqg-jjkQASswuOjFMaOrXhMC8YgVIl2xoFjL3flSYvwlVlkuARPqpxigRNO4JdgMPIC-tAcSrB8uGDgKdnXn-iH1TYE4NIiLXbh2-fmtSRfkBXJaPNkc8QLQFNfHARW-DJyCihwgRrMUPiX4aEUVmijwP6xwJdoREO1rAI36MSzAwHCT-iNRY0Day7blzxVFADkP2I1DslkGqghMQ5NZOqk7fzR9BUgvq0jAVjzXOFZqt3_kSdmX6YpUkZH8x5bmJACgeXrl5j7TESPWARfalI7143lwd0QiRP_aTL6-PCvpNha-jqVdoAdn4KNTgkySAdB5m2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/105097" target="_blank">📅 18:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105096">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixDv54ElXNEXkeggr2qpN8NLc7uCcxk14aN87ndkmQoqKYvFy-O12O_TEZ5RjKGKPcU_7Wbjo746_jXCE_7jFAr-cEabRNUenX9NUcUqcdDdB5CP-39tYNq6S6FoV-6QPtTAExkGvvkcHX7NuYnYXRlSe3GNTxXADkylsQmclh6r5Ndrq8aIgNjCPySTGtU0m08SlCo1pEi_TsKL9TmTAIyChbPkBKZ-HBnjA_UoRLcMouqBgXSXOr7i3VeHPAOCiO0nrXDrtw8egqn12QZc9mJ8k3jkdsQub7Pmu10GS4FyhBQzDfOQocg1j4EhM4AGgCz54A4LkfxIQsMVWDWoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هفته‌دوم‌پریمیرلیگ؛ ترکیب منچستریونایتد مقابل ایپسویچ؛ ساعت 19
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105096" target="_blank">📅 18:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105095">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9709b25451.mp4?token=VJ9a6obi1v_O1mmmSO-cECaXOMFFjWIAH7k-eL5xZUubqpcnXMiDJuC_SHK7SGON0WHOZ5TaFbVLQPaYlnNpPvmHXbWxRR2S2_VUJYCVcW6-elcGLYAEn5_LTWEW2lEJQyjjORG7OJPlK9f8lD_9IvDmsOSXqsXLjEN-zFUVYuB5Gebf-z5EghV0MFqgS72a4lQRgkdgIgq4hCrhUKPo3JhEzKd7neQQr5M1UgjrjepXBht0I2PMtpTGYsQGbdukcR0Z_Ln9mOZx5QT923WGjLBzebWW2ywSh0QNIPDUVcUhZqji0rUmj15r02FPYm86AqW_34gKhSek05oQTHKUMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9709b25451.mp4?token=VJ9a6obi1v_O1mmmSO-cECaXOMFFjWIAH7k-eL5xZUubqpcnXMiDJuC_SHK7SGON0WHOZ5TaFbVLQPaYlnNpPvmHXbWxRR2S2_VUJYCVcW6-elcGLYAEn5_LTWEW2lEJQyjjORG7OJPlK9f8lD_9IvDmsOSXqsXLjEN-zFUVYuB5Gebf-z5EghV0MFqgS72a4lQRgkdgIgq4hCrhUKPo3JhEzKd7neQQr5M1UgjrjepXBht0I2PMtpTGYsQGbdukcR0Z_Ln9mOZx5QT923WGjLBzebWW2ywSh0QNIPDUVcUhZqji0rUmj15r02FPYm86AqW_34gKhSek05oQTHKUMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
فوتبال خیابانی روی زمین چمن؛ هنر این روزهای تیوی‌بیفوما در ترکیب پرسپولیس
‌
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/105095" target="_blank">📅 17:45 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
