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
<img src="https://cdn5.telesco.pe/file/vB9xIVf5gQy9DFHWlrxQGSLgXICoMtY-_OIHsdOUuKFBkZi5FEvDYR_uAaOyk2-9oAknWfvh5H2js8m8Nh0g48IY078UpPx7wLJKm34v0ZFz5CEUxbeB33Vqfi7A0xso5oh0gjN3myLD4VCJsfaIc1BsTjkZWDC8d5TjcA71SeMjAjH_7u4Eeyu3-we2ZxMKA18GkrWrTfTKqZ36nGuScbyC1iZhseEu4zkB7j82Bkmp2jpwz0Nkiy9m1UOwi8A7WN_CyadCNp9a85ziJ37L8x4RacNhdY_2QLyoNTa-KyKbPtPOg5beXGs6DYxk8uWjLyG9OgLBL3ENtcD8JMlvqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 609K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 08:59:38</div>
<hr>

<div class="tg-post" id="msg-99144">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
به نقل از آکسیوس:
مقامات آمریکایی خود را برای یک جنگ چند روزه یا چند هفته‌ای با ایران در تنگه هرمز آماده می کنند که بزودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/99144" target="_blank">📅 09:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99143">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox08oR1_FcrKXDD-NP-PwE65dbQ2_uITGVj6y4M6WOkBEgKzudZQNjIS4Rkj-U2QZozZaIu-2eUDIOR_WwDotDruH923TZi6ayS7fQIWEew_VXo3P9v-8Q4UM69czouOPFQtL2K6x5JNhxmBwgzK_nrC8cG5GJz0kl0BfiN1RGhfXesDE3557NQxXQyb-AMdsoCSJdDDiwI2C1CCXrbTUdiOY6QTpRa5mS6-lZErGWw6OC6p1JtOMK_I-10ytRypCNj2CESAaNkyPmbSg-Jy0X1wmJQl6PvGI41_a0kMMGaQGl1-WEQecDxCq6LbgNlxhVhx3QJOHjcGEKhumL-BQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
در اقدامی عجیب و برگ‌ریزون؛ دولت مصر ورود لیونل مسی و خانواده‌اش رو به خاک این کشور ممنوع اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/Futball180TV/99143" target="_blank">📅 08:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99142">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
بیانیه سپاه:
زیرساخت‌ها و تأسیسات مهم پایگاه‌های عریفجان و علی‌السالم در کویت و پایگاه‌های الجفیر و شیخ عیسی در بحرین را هدف قرار دادیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/Futball180TV/99142" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99141">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSIF0GBAJ8EDBNmVZjhkDlCFiusMpWUBk5WILJj8ipd303cmtUBtyzaqscKF3L-bP7F78KHi5_MDwrnVgrCxh9owObhsPvcZjkxkoDlzM4saji4P6G2R1GoBQ9ADf_0eoQY10kzPSAy2flEYTWy5X8ZLvwgeLTwU8CwskS748E3uwMETlzUXsu126XqJenm1EkPIvM4zfr0FYCuqSqaUIiucBtdjJcXEiW_a8Gtso7wvyFxDZFZhf9hURmQhUltAmnWJgEDeUtPoSmuDlVjaHtDdkUFULN3gaJoa8C4CZAfuzuKZAas8w0ABVDCMnVpoMKc_8jPyBMHwRTX2fOXxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
🔻
دوست دختر جدید لاپورتا
: «من بخاطر لبخند لاپورتا عاشق او شدم و نمی‌دانستم که او رئیس باشگاه بارسلونا است.»
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/99141" target="_blank">📅 03:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99140">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eR0LMA5IwQ-VgELPkYZd8IwsdcKsN29uuD-0Pbxd6yCs667ATltIsfuE9IeiPAtlRZAn3o9-4MkffkuWgf9ZEMXERp0vshM3gRfdFXMXUiDggwEoIsGUuVWvmSdU73O949H7qYRayJFBMnYI0pSc6uao_-hT2BsnydVBoMmdnYEGFDH580t2aTCEZo3xurVVQ2fq_TAw4BNrB8wNsl-fhDXJpsfkNVwyZpkDtrw98DYht7mm2_Kf7teLaVihhaoa9_LPe_Ovgl6GzXzQ2q3lxxXgeO29myHLapzPuI6YUKLVE_E_hhnj6emGOr7ofwiLLPU6OuH8W6QjU2r8iWCjzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d7f4ff5.mp4?token=eR0LMA5IwQ-VgELPkYZd8IwsdcKsN29uuD-0Pbxd6yCs667ATltIsfuE9IeiPAtlRZAn3o9-4MkffkuWgf9ZEMXERp0vshM3gRfdFXMXUiDggwEoIsGUuVWvmSdU73O949H7qYRayJFBMnYI0pSc6uao_-hT2BsnydVBoMmdnYEGFDH580t2aTCEZo3xurVVQ2fq_TAw4BNrB8wNsl-fhDXJpsfkNVwyZpkDtrw98DYht7mm2_Kf7teLaVihhaoa9_LPe_Ovgl6GzXzQ2q3lxxXgeO29myHLapzPuI6YUKLVE_E_hhnj6emGOr7ofwiLLPU6OuH8W6QjU2r8iWCjzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
تعجب مهران مدیری از درآمد علیرضا فغانی وقتی در ایران بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/99140" target="_blank">📅 02:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99139">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aC-FfBGGuNwWHQ5Vplgb3vAzBrXGhGB3_4Wa559YiAXn08LxeAsDmdnyjRo5TKXa66Ino_ZXG4XTOh9uLv9jg105W-b3-sGFyOPzOhvzd4XixsnXVCMEWAEaCHQWA-jEUrVhTgYwy1776LAZ-CW3r8QybXqnXG6ydXv8WIfXZPLfyjrnq3rTGtxYE85LB8bbM04kTZ0Ik4DlqlMFWg23Sq7UOLFREkEjESGk3V_ZMleP0yWrpevY43FVefGaC55k3Orbs7Amj595MAPORqjHdcQ7S4wX1parW3RM2mwqmJoRPhe7_wyNU9kwDM-lmRLqJN79e5xaYhImkkbsmVoOsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99139" target="_blank">📅 02:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99138">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bv0X3x9lqCuQYFPJe02fVxAjIA6xgkl5HLgmudPfVF5F0H2Zh9OBonlj8BKeMBBDMaImSu7zzKHLt8D8w1MPnTA1yNxBkYGuOdDDdz5sAX2J56ltzH-qgIQ6DGERRjvyHPpc5d7ykUayMZoU-HrmsO1xuUjujpzPCOw1eOVVUzorOpc7CVBUuQlP0tqIW7XJlpcPbne6VX0Iak-5hARPfYaMUoDxj1JxyE0ZZh14A52aC2nuwZEdf8imHb21vNq5ayJpXFKyWu5F5mzOhm5QJFXAzMwBUFcC5Tq13nrSXcfmC5YQPl6QnI4JmgTlgvQcX5H20YV-JWFwIQxmJ29B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تفکیک 3 هزار گل جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/99138" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99137">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/99137" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99136">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LgRzkMunuWmUhth9s7DSa90NbKD7PdrJnyyspnYjhdb4xLNxFGS9e3GaGAk1eDtqORnvT7mfngVjAo4d6vbxqUQLUu5EleLV0Yk2e6ofIFavrt6D-onQyOmXt0pX0N7nAL-yveJftvzVaq2zAw1dGefG-4JS0n5R2wID3fKwdqxZj96h4Ei7lqT3MPfALW-xd7ynSM1P5VOfyELS_mdKJyHW_4iTpKrTrI5GSdIBLzo4NBKvk-fCKZAMCvTIFa7DZ_Yj7iUChl1m0-2UTj_mf7UHW5mN6rHSS-vYeBnV0xieh60OZSWq8FQiahMEu7F7CaFijT6FPNyNjtQRmiXSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/99136" target="_blank">📅 02:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
رسانه های برزیلی:
ممکن است نیمار در روزهای آینده از فوتبال خداحافظی کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/99135" target="_blank">📅 02:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYeictgruHL5fOmHNhgEe7qXSmiN2J3_G7um6Z-ehw7KAG8IqGlHC1qdXKG3PgVxPyy0l0BJSbV14HUBjCFWf1QQ3ngkWoSZg05zn-715VRONNumD_7RYoFnrFhEcQMEUmbOWnwnGgaZeQACACaJM-TXWUbyeaa16srIad4mEs-paUGpTnHMFv_dCN_19mJclreBKNMIu-ox2rZQSCgOIppxCPuuU9FbHNoaBfgDRDXSJcLvHX4GBqZovnCm5G6tyCmHF77TKBkkZCDfiTOiS5wCpso1OEIe9lR2pLEk8cC_Fx0gD9oT0Xvzq2d_Le79c7iDTqHPlJw95qjGjVxxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو:
بارسلونا به جذب کریم آدیمی نزدیک شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/99134" target="_blank">📅 01:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8ZNe7bL8bQ8IDiLUNSWpIZQLbhLNIgAwp0ikgCiecHBOeKy8AqN2_weviK8o2w9AmeyyIE0qY1zKxdzqSvbN9X2Ss601Jvfzx5wmYE-LApXV-Pega1MC9KoTPe03UHECn210GxCZAYqUlW6pYrwAjCmjmIorHWGmvPITXHXEOZWG1d5ec2UCWDFZDNDIP7LUGnYlZx3yJmx3ZXAqgg6a7hCguOV5ymtT9VX9fE8wPXqPVZDgF4IV23A6KQy6gHLN2lmGLfqnI41fbEkUnqQX9KX3SUfru-60yYth9H3EVonGcgM5jtDSSXSFNzcsJCKpBX5UJQbxuk4tDE1CIc2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نقاطی که امشب مورد حملات آمریکا قرار گرفتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/99133" target="_blank">📅 01:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
حملات امشب آمریکا رسما به پایان رسید و تا ساعاتی دیگر حملات سپاه به مواضع آمریکا آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/99132" target="_blank">📅 01:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpuWvVLTgQvr-tiZqqWexIUdXfJc6b6JSn0XTTGp9ATm4MkHEEOsMhhfoSqsOrgI877M5oI2Ykxi4S2GTuRPKBijU7Q7QVWcyR3l3GO9PYrf80MRSz0YtImb5SN0-CDxzDNZRwdmio3d7bThQGx8c7BRrVOLTU-47S0ckoUsYYREvcZNBaUpUVVnWB0QpHV0YE7iFrPHXMZ5NzhV35rLRVQyqBrs6joJx1R0qvvCngtLO5DVknuQmXZ8elzhDiG4dbDcRDKbN1aPRiDLYdLGNzBQcJDBDtR-IGlSnBoX_cadHoH0xhL0X3WFw6uJl6pkvAGDhlkOl-1XFbAMyrLIfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زیدان:
لیونل مسی بار دیگر ثابت کرد که بازیکن سیاره دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99131" target="_blank">📅 01:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99129">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JE8X5QZqoHJsNBr8W5qlEPVSAPlyTrEjTf2j6YY-tMqhy8lXhl-XjWZ1HVUS53J8PCjJQoqMGDVRSKwpDJag4xUOOLoEEnmfOfU4AYWr_jg53t7sba8eGzJ01LwQVIi7YoR8QK2z8vsoKECkkY5wE7yh_f3VLFOt15N8tKXjz4J0s___uM20-U22TYaws2WPthkgS9XnUhaxl-9cG_hgQqpEsZVDolPM-kupigON2XArYFbOIUkELkBZcSN83AgyUqXnJNA9Bx6224MzgPA6FLtTHx_TVD4r5HwbnFGMpDF0kEswKw1bbRQT3hbKdGuvGnCp0EsoYtZ4qWuseeaM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: این اقدام، تلافی بمباران کشتی‌ها توسط ایران در دیروز است. اگر این اتفاق دوباره تکرار شود، اوضاع بسیار وخیم‌تر خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/99129" target="_blank">📅 01:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99128">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
#فوووووری
؛ شنیده شدن صدای انفجار در مناطقی از کنگان استان بوشهر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99128" target="_blank">📅 00:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99127">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8JM8jFJcSFPOeop5pAYPfByXpI0HdPAAx7yquGVQSC32VLqGm2jPhjWryssPrwt66npyhPl9Yk40TVzNLhpulK7B4--fndpJts3yUt7ecTo3sfCIvQR0GOQQqpdNhiSTB0lvGEyJUPwDGJLsm7xgMZlL7vIXF1stDIPm_GTU8Pq41B4XAmN4ALmSZDKIvMOCkjJjio66mAuXEWL7kqcWwzOKpqTcXbnHhq3dhVjDhnnnTxnH0E59k1rnCQkOqupJuHz9JTKRMN6GU9qWjJv-A6pxyVOUEzqsPtF9eq944WFBdX2Y86F8emaTGFXxPUtGZksMEG09xA0xXeHhLlVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
محسن رضایی: دشمن متجاوز و هم دستانش به شدت تنبیه خواهند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99127" target="_blank">📅 00:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99126">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
یک‌پهپاد آمریکا در جنوب ایران هدف قرار گرفت و سرنگون شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99126" target="_blank">📅 00:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99125">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
فارس: دقایقی پیش مردم در چغادک استان بوشهر ۳ انفجار نسبتا شدید را حس کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99125" target="_blank">📅 00:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99124">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgZ2KrkxEbzgYhTV6HU5phssQH_NTVVsN19uEbOAsTVPUF-jw2gYxBmAU6olTso7crBhs5qKHwG3MWcnC81I45N53ZaUbQP11NXRAflf2XHPhxXyeBGAukxY08iru41pGKlqhj9hs8u9Y0jo3owBtaqTc1VDBDFAzI2ZIoaXQ-1I1HRhBKCkFButHCQfgF0RD-BWLIn_yMHSmbxcxH_jcslHObzJ9q0NnhqdtLS82Ze9QpBEHxJzk9R4bBFbkBchJon8rnVf-qZpLtqfhE5vZxDuCRV2HVbkeT1rR5MnqNQFsiE9z2XPka0_7SXBuaQ8pL4IjywAV3nT635a9zFLaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
پست جدید کریستیانو رونالدو:
‏"پرتغال، همیشه و برای همیشه."
🇵🇹
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99124" target="_blank">📅 00:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99123">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
مقامات ایرانی: تاسیسات‌نفتی در حملات امشب هیچگونه آسیبی ندیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99123" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99122">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
انفجار های مهیب مجدداً در بوشهر رخ داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99122" target="_blank">📅 00:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99121">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ انفجارهای شدید در جاسک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/99121" target="_blank">📅 00:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99120">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوووووری
؛ اسرائیل هشدار شلیک موشک از سوی ایران و حزب‌الله را به شهروندان خود اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/99120" target="_blank">📅 00:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99119">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از یک مقام آمریکایی: حملاتی که امشب انجام شد، گسترده‌تر از حملات روزهای گذشته بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/99119" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99118">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
#فوووووری
؛ شنیده شدن صدای دو انفجار در جزیره ابوموسی/صداوسیما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/99118" target="_blank">📅 00:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99117">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrkzHn6VOkdGxqkcYbgznv1IvbX5OvhpIdQ1BM5s88j_c1ZRZO4OPqXN7ONMLa8Iy8iNd-hLvfJqA9aNimx4eO_hEwxrfP75E4D_6MxRBH6nfDTyU_9Nt8_ZPHb-ssrb5FGy1FNsKcPzu27VklMUC0LU94kyN3HRj3EwgJPNp4nbFmo806a940MYu9OzJENCRkowecEThGgfuZiz1WbmK7a_h84c6CiUOXM4j4YH9cWtypqYdkbc2x9tjztOBElGT6cXHYRsk1YWg2HQrEQET8SapKpmXZ_LYmCnRPiL_abVfswCSUSu7NAtF1gUtvspKQvsZ9krRAIBXWnFTfwOpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
تصویری منتسب به شهر بوشهر
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/99117" target="_blank">📅 00:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99116">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
کمیسیون امنیت ملی مجلس: بزودی پاسخ قاطع رزمندگان اسلام در سطوح بسیار خاص و ویژه انجام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/99116" target="_blank">📅 00:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99115">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
منابع داخلی: قرار است نیروهای مسلح ایران به زودی حمله‌ای گسترده به پایگاه‌های نظامی آمریکا در منطقه انجام دهند..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/99115" target="_blank">📅 00:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99114">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a36705c.mp4?token=K4sX6oRSf4HkuFbXgfH_KZwsBhYrQolA0rm8DobpVrWEHWWV7DDsg_RSxqdkkYKBcNl0Q2d4Q-XyNMfFIIMyOllAmMuNMjzk_zA2-QklCMxtUrbRxORqKfzQpnT4u6ZimZaPO9meT0ucgl-EFOlM6q0hdWF30hcWYApG1tJuLrIqlQkbfyXa-sBN-9leJ8c4wTxGTmqqaK84YPKDExuAvu6hgmnh8hPJq3HRMhppkF8Y0oW8uwmbGDCfq3AiWfaAVP5k1u02K8L5c2UP0gryZF72IvJ2PhNGoOfN7FyNR92jN1Kcn_YeNc4IIImQgaGPa7qkYMKHE1P012g2vuJFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a36705c.mp4?token=K4sX6oRSf4HkuFbXgfH_KZwsBhYrQolA0rm8DobpVrWEHWWV7DDsg_RSxqdkkYKBcNl0Q2d4Q-XyNMfFIIMyOllAmMuNMjzk_zA2-QklCMxtUrbRxORqKfzQpnT4u6ZimZaPO9meT0ucgl-EFOlM6q0hdWF30hcWYApG1tJuLrIqlQkbfyXa-sBN-9leJ8c4wTxGTmqqaK84YPKDExuAvu6hgmnh8hPJq3HRMhppkF8Y0oW8uwmbGDCfq3AiWfaAVP5k1u02K8L5c2UP0gryZF72IvJ2PhNGoOfN7FyNR92jN1Kcn_YeNc4IIImQgaGPa7qkYMKHE1P012g2vuJFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ ویدیو منتسب به حملات امشب آمریکا و انفجارات شدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/99114" target="_blank">📅 00:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99113">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووری
؛ پدافند اصفهان فعال شده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99113" target="_blank">📅 00:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99112">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به نیروگاه برق پایگاه نداسا در چابهار   @News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99112" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99111">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d737LQMqkuSq1f_AD-cpFSQIT4VXmEpIuiZUDXVFsV9WAQpox74tVXmaJ-jsvk-jVPfqERCxm2xgq2blsxG6CTudnWijveeHeYt06BkWKRN_PS_o3OuOtxIrbkh9Qbd890ny9bib2bjRigW5Kgt_O_O4m-jaDiZkgabQObyE014JBD3DSN9TNzuG9BBbP06XG6hESBWWJzTIf2SmO5BNdSklVDU-tBmMLhuOIxORqQIRBlMePNzIfKq4Z7KeVv5E4faP6F6lh8zGxKhnt35uHrvT1HhYcBVmgplCkGz0cX-qAVYWi_uO9Xf35gU6P1WLGFLDZGlMycqOgMAc71BUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
چوامنی تا سال 2031 با رئال مادرید تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/99111" target="_blank">📅 00:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99110">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=U9qGlkUNErkflWcWOJu9FeCkyf2AZloiPaWpq3aPxyzaBwt_nBh0fWIJcV6U5iS_G0TScY4CCvDpHNFSBUsdmDCrJVnikxHdioRYXfQES400M-z0uIrOIzZ0ZQx_GCArEJGKWybWjdw6J2wei5_Dc8nzn6xrluJVdSKniJ9l7ky9_Cp-zLSPKmtDT18R6bXDTBBgnTO91R7mLzmCEbySLEFXKybPAPsjtt7cP5zbX4jg5vaAOEnatdGHOP5ST5QpNdDDMVgyTEh3ZWztYWicRI1hayyZNcw1p4ys92BnJlL5Cwps5tPFBBh0r41JU3ij-UHRRKH8tBh2YkmKlhW7jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82d743a24e.mp4?token=U9qGlkUNErkflWcWOJu9FeCkyf2AZloiPaWpq3aPxyzaBwt_nBh0fWIJcV6U5iS_G0TScY4CCvDpHNFSBUsdmDCrJVnikxHdioRYXfQES400M-z0uIrOIzZ0ZQx_GCArEJGKWybWjdw6J2wei5_Dc8nzn6xrluJVdSKniJ9l7ky9_Cp-zLSPKmtDT18R6bXDTBBgnTO91R7mLzmCEbySLEFXKybPAPsjtt7cP5zbX4jg5vaAOEnatdGHOP5ST5QpNdDDMVgyTEh3ZWztYWicRI1hayyZNcw1p4ys92BnJlL5Cwps5tPFBBh0r41JU3ij-UHRRKH8tBh2YkmKlhW7jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات متعدد به جنوب از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/Futball180TV/99110" target="_blank">📅 00:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99109">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=JAt63_Y_63XderMzyd8UrYJompoL7rLOQg8OcpKVn02TfChpLBSfDEZUUgL1Oqm33KeLUi6Pm22Tg8GHAU0EFQ2s6gXH4_NoV9d-V2zqP6NSDNGhLmHowixXYNXzKOkPe2Zdfn5UkC112ZqFfwljVOAuociSV4NlehEoya_HDyWRxm0u3r5OC5Y0PNlhgADMZD3If5N7tOR0revszkNd5GdmbVzNbeTkJclUAm_dOOtiH1z7ayPbzQARceqetXdsTFirU3AwcOTy-hdQEbBrzB0Cf-tALlL96mhVi6L5is56HtKWY9J2ya6RgMrIKunen_1U7kYHL8qABUdlK9lToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf4c74933.mp4?token=JAt63_Y_63XderMzyd8UrYJompoL7rLOQg8OcpKVn02TfChpLBSfDEZUUgL1Oqm33KeLUi6Pm22Tg8GHAU0EFQ2s6gXH4_NoV9d-V2zqP6NSDNGhLmHowixXYNXzKOkPe2Zdfn5UkC112ZqFfwljVOAuociSV4NlehEoya_HDyWRxm0u3r5OC5Y0PNlhgADMZD3If5N7tOR0revszkNd5GdmbVzNbeTkJclUAm_dOOtiH1z7ayPbzQARceqetXdsTFirU3AwcOTy-hdQEbBrzB0Cf-tALlL96mhVi6L5is56HtKWY9J2ya6RgMrIKunen_1U7kYHL8qABUdlK9lToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نیروگاه اتمی بوشهر هدف قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/99109" target="_blank">📅 00:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99108">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99108" target="_blank">📅 00:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99107">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ایرنا: در پی حملات امشب برق بعضی مناطق چابهار قطع شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/99107" target="_blank">📅 00:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99106">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
بیانیه سنتکام؛ فرماندهی مرکزی ایالات متحده:
‼️
به دستور فرمانده کل نیروهای مسلح، نیروهای فرماندهی مرکزی ایالات متحده، حملات بیشتری را علیه ایران آغاز کرده‌اند تا توانایی این کشور در تهدید آزادی کشتیرانی در تنگه هرمز را بیشتر تضعیف کنند. ایالات متحده، ایران را مسئول اقدامات تجاوزکارانه اخیر و غیرموجه علیه کشتی‌های تجاری و خدمه غیرنظامی که به صورت آزادانه در یک آبراه بین‌المللی حیاتی تردد می‌کنند، می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99106" target="_blank">📅 23:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99105">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=CMMZVnzsxdSiasvuRrboSMsp6qyH5sBehUp2tlZ7cBCmmdwOVYEuIbdbK71G-PQcjuh2XWPHMuZuFt06_FoFQgDGgFL10bs0dTmxLKmDb1ux7WlTwIPQBJaETnSUP8bxzxuveA1zmMI4-fdEWXS8ovKNWX3bW5plMnrBiCW80Ld0GQFvgjurSoI6eW9KJE3v-QEjccpbS2Uk4z7sycD25KLFaHQS-QNLT8kTPpLT-Bs5yFDssstjxv_1jw9xhZ1ndMzp95-pb07omrp0938DwklD8so_SyBdyEP8tJFvIaW4ZJ95GKG5A8x0ujCgwVOXzYgTtcwbyo_iHoSLzIeOuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1d5e85683.mp4?token=CMMZVnzsxdSiasvuRrboSMsp6qyH5sBehUp2tlZ7cBCmmdwOVYEuIbdbK71G-PQcjuh2XWPHMuZuFt06_FoFQgDGgFL10bs0dTmxLKmDb1ux7WlTwIPQBJaETnSUP8bxzxuveA1zmMI4-fdEWXS8ovKNWX3bW5plMnrBiCW80Ld0GQFvgjurSoI6eW9KJE3v-QEjccpbS2Uk4z7sycD25KLFaHQS-QNLT8kTPpLT-Bs5yFDssstjxv_1jw9xhZ1ndMzp95-pb07omrp0938DwklD8so_SyBdyEP8tJFvIaW4ZJ95GKG5A8x0ujCgwVOXzYgTtcwbyo_iHoSLzIeOuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سنگین آمریکا به پایگاه سپاه در چابهار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99105" target="_blank">📅 23:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99104">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/99104" target="_blank">📅 23:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99103">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
موج جدید حملات آمریکا به جنوب کشور آغاز شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/99103" target="_blank">📅 23:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99102">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpCzMdVA8EWB7663braKpcGaaP7naQott8BR3qhTJJeifh8tDkQl3HwAnmvoEry3BhTWaGFe_Q-cRArEIcDPPg2KEl-8eOGpDhgji0xzmfIIE5tx9j_13GEeC-me0f_RQFJqwDDIuNU_ftGRaJV1ImLgKJIH_gkobOxoC1o0EhJXkA0i3KpcB9rpqrFkdj12DDbuWWhIowXcoUQqPl6-t1_nFHL9dWuyzm9elC5MnolksemwoARQBo663Uy-8bZGobB73A0FC4Fpv22Tiy9KG8Or-PKvuAZabgQPSD2q9qcxd2LwnGSD9rNhhDc2mRjR9maB5Br-VF7TmQvryq3KkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنژ پوستکوغلو:
چه سال اول، چه دوم یا سوم باشد، تمریناتم را تا قهرمانی ادامه خواهم داد.
میخواهم امسال با باشگاه النصر بهترین باشم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/99102" target="_blank">📅 23:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99101">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=F5fCSNXtIobIEajYWUhHDbSLjbJG9WMMOeGvBRN5VwsvS6WqwYVYC1a2E7yHD5wR83JqZrYswisCtS_tXjWVnMLh_Dl-_xQCoz_aTI1H4HmZ5ZtMrCo-aoKGXTFuEiitI3JC2iZF8lMoK_JP-wlp4T07IDKv3lR4CsZ0g5rOKxOdvN3CvNjLNT83oOzeidvOzN1o7Ln1Rl7Ct3m9zL56hVMp8u9fep6zGFuJBsSPzd1VmKTb_DqOK62cNUdAqaKAqeQ9vLiwtE39XxgJXWWN95NQujz3057v-tNwCJ-xH5vjra8_LstbESPvIV8enwjzbCUcIj2t1MyssC34makVLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2cb709e88.mp4?token=F5fCSNXtIobIEajYWUhHDbSLjbJG9WMMOeGvBRN5VwsvS6WqwYVYC1a2E7yHD5wR83JqZrYswisCtS_tXjWVnMLh_Dl-_xQCoz_aTI1H4HmZ5ZtMrCo-aoKGXTFuEiitI3JC2iZF8lMoK_JP-wlp4T07IDKv3lR4CsZ0g5rOKxOdvN3CvNjLNT83oOzeidvOzN1o7Ln1Rl7Ct3m9zL56hVMp8u9fep6zGFuJBsSPzd1VmKTb_DqOK62cNUdAqaKAqeQ9vLiwtE39XxgJXWWN95NQujz3057v-tNwCJ-xH5vjra8_LstbESPvIV8enwjzbCUcIj2t1MyssC34makVLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی شده که برنده توپ طلا اینقدر با ما احساس راحتی میکنه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99101" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99100">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha18OWZH0F8yp2DxtYrAZGWy4-E4O5SnHUKFhyEG5gCEz073b1YSoDkkEDFo8FcBS9IqU4fUxmzxGWcO400Ka8JvC7we-l8WfKheDMFCT8NzmVDltRnSRiYSu-_YWWJ3bBO952ZJ_HwiGuuo-qX9YDQM-0RZgEwBDnXmlcHJhy_m0MD1fudpAMJOBVuLYJ4DCQUtWP6PBvxnyONc8fhlmxgqKc9PJiksQQLMQhn9AwqghuQq2TP9t7vBQJbu4Z4njIU590Qjkt8_9qqtoxBKWDAhVBkYXBmeWW70RD2287NpAfGlUpT7PWd4LhUUuBaXNbeN-FboQaaR86X_yReMAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جاستین بیبر بین دو نیمه فینال جام جهانی قراره اجرا داشته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99100" target="_blank">📅 23:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99099">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJK1Pr-ICisDBdRRhIUsFtAfxgUjmRtwUXAgRZltQKZN0MIoiqzZtX1h6naU3ewhGk8Q5uCL0eBpST2SEHch15PiRAff-NnCYYAiQMyuBqgdd2DRrJuqLO0XCzGmYvSJkMp0bcHbsAP0HZuuqBOeTTcDabpX1Eg-9Cw4OU6xZKrtAsKWQdn1MaA-YNdFK6eVdZeq1EB7DaAIDrBuEAdlOdpdQBHWG882RzIfo185ah4t6sc6rtrYyUMu3OHw-MziFxjGkzaZ4KdendtMvabeqvPryF57BZeYO4F8FLVixXL0zV8VYgKwCgkN4r1onR0pwDPvNj9C24WvQRlwnXmBUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رافا مارکز به عنوان سرمربی مکزیک به جای خاویر آگیره انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99099" target="_blank">📅 22:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99098">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR9wKhU33jrldD37F6BDpL253LMeG-1kP-xbw0Db3fQqXMKOON2fbDN7lPgwIEaWuB2hyTT365zBEXyEk8v0j0gX18-qOcVd1kG7xMWp1QwcE22nrD3lq8LzcsOjyuPd8QwiqlhHfGfJ_yD-qrVq7AYkwPERZ0Uwse8DLjcvk5KYQhzSIofT1iDxRIyKTHih_YIkzg60X812S4-iS3aNPEj7vntr_qSwoyOlEHPYaNBvgFv8eeP01kHjZqM1JioVSazkr4kM67fQk_Ne-NPQ21339FKLJQmbqcwQmtK4vd5c_0B8rLPzU5ctL9hcjMD4ORCXcP1SdUGXYuQ-4heaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلسته آماریا بار دیگر به کیلیان امباپه حمله کرد :
"این حروم‌زاده فرانسوی نیست."
سلام و احوالپرسی یک رسم همیشگیه؛ صبح بخیر، عصر بخیر... این یه سنت پاراگوئه‌یه. چیزی که ما رو عصبانی کرد این بود که وقتی اورلاندو گیل این پسر جوون، با نهایت احترام و فروتنی دستش رو برای دست دادن به سمت امباپه دراز کرد این حروم‌زاده نه‌تنها دستش رو رد کرد، بلکه سرش داد هم کشید.
این رفتار، رفتار یک فرانسوی نیست؛ یک فرانسوی واقعی هیچ‌وقت همچین کاری نمی‌کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99098" target="_blank">📅 22:52 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99097">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9AZ0DN9DiLa71yoM-Ewo24UtuCu1q2N6KyqAx5Ee73gX6ALLxduta2q7BY75p3TKgMk5p13dlvK0bIsd8Agp-iJDH88eYUkwDv4TO7DMNiUSeLVhLvqxY7ca-T8_HaOTnJNmOB2snJgD3hPwFg0YlLdzbAvLB5ntCF1HdLf41NHB9IhfTWMBKC7LOWb0peYlnjZovq458_i3LGY3Dsqrmxtx4IM3Yhq2MlMMtv5Fw5F0yWXpir9I_00Kida43AB2zvrn6_FZQvQBF9BB5lATml1Nwo88Tsb9WGCkZWbxTVom_HMnL2unY1BdkqMeKPNDDBHhbz2lJVlCy_orrXplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در چنین روزی در سال 1990، آلمان با بردن آرژانتین برای سومین بار در تاریخ خودش، قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99097" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99096">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC-AB-nCn4cn6WJF90GoV-AI6_r1vW_PmU54PZ4p4Fj8ROmA0lzN4bU9zD4wFMTqLvqhH1PKnRKY3sSaYJchzkQTKj5OI2JTfNnsXSkhiyHCDAEXe4tOyaAP6-W5Z2UaLdlDpfLHzm6dLs8Tlm_fhSMzXMpeQLxUx7Zl8NLGD4V4GNBWNMHjEVYxC6y77_Laa6zXViBRiG2_g-fymImKM06RYs60qTRhX6o_Eq2sm4aeJHWVYDB20wxD1H83mN7NEwfPoGYbA4N3uZNAiQIC5Z9Oop3lzJqQCzdKDAFWGMW8p7TW_D10gna0OoeNfTh5vun_qWyx8uk71DWOq3VX7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
شانس بردن ۱۱ جایزه ۴۵میلیون تومانی داری
فکر می‌کنی از بقیه سریع‌تری؟
😉
⚽️
وارد این چالش شو و
کارت فوتبالی اختصاصی
خودتو بساز
⏳
فقط ۴۵ ثانیه
وقت داری؛ سریع جواب بده، امتیاز بگیر
و ببین
سرعتت شبیه کدوم فوتبالیت و ماشینه
👇
👈
شروع بازی
👉</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99096" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99095">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3rOQ15k849MsC7Rrj-c_eX4ozKcR_TYKGw8u3H-_bCzl20PA5X60i38qNkAXXlf3-rH1Pv4Rg_H2vpPb084ZptCu8x1vyJjTH78qH3oSPzH-nyhB675du040dRAfwych6hyEZrTfxnHm_UBf3qfnuTv65o53bAuxzogceID7ZkMrI37Io2_iM3sLgV7GhYDXsZol1GXh10bfukqFr0hJojkQ5CRGgjnQ2gvWctPbeUBbgp5lS0nPh66CaytB7-EbM-dzCUmWqWgx2tBxtwS7TCp7gdm6_uVNNyXYb5QNrVCJQVLC1IVHzZqVeQ4-tiHjZWcpKhWoKd8wvJH5xJpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
فران گارسیا رسما به رئال بتیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99095" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99094">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM1O-QVvQi05CbzgmESoH8gwJj53Mmt8kFx4BXBwVUgSZjjwuNESjRrHa0-n-ApNHc7Iif0gIpv-QkQVNrqPlW4IzByjLE-f-iSjxDbSkWuQ1qgplAAwK3Y7pZvcC6WuWk_GrYKa_AWqRbZJanPHDHJwxERIC7BIkl0oi-X4wML9SBcPhmD2OllkISePLyzAXk4PzqndjXpOlQ_AhytLsDfTPftz4eFw77YNLeI1ZPMJjGCiXq0-shzNW18rjjErXByngoj-x7frAy2SsXSLbibNDUzBPigLwbh5QOIyXfXnuj6wX65SHo9N1N2nFjkhP12LgxCnBsM5NkxbDsLZpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار یونایتد رو که یادتون نرفته؟ هنوزم بعد 634 روز منتظره تا من‌یونایتد، 5 تا برد متوالی بدست بیاره تا کله رو بتراشه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/99094" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99093">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjgXXmKjU7xZR8aaFiemerb5q8VUijI1yMUW6R4JptsETGEsICAhSHIT0GYh2wT2Pr03Xq0P71029ZazSwhr5Ewlcgwm91g8WXD2kPuQucsMGNHAdFTW0FwiEPvv4xQmtXmZQaSOLqPHEaz9mlsmoyLZp33K9gKAoMoxTr4dCQS8n_n8boMv4p6OGf7LlAcXI-ZXiztdO-pkNPAxIf82r-N6yEJGot_gGgmxUoPP6gqRBZn0z-5CiDJUlSDlqsIgZEfUujmWb6NjsmNma-VH8pg_EiYEiI-rV56jAqiwmCVLho7Wry6Fy3_-2DRK_07qDFBCEqCWloZ_a9XmwHm1zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ژرژ ژسوس رسما سرمربی تیم پرتغال شد.
🔻
ژرژ ژسوس رهبری پروژه لیگ ملت‌ها، یورو ۲۰۲۸ و جام جهانی بعدی را بر عهده خواهد داشت. او این فصل به همراه کریستیانو رونالدو در النصر قهرمان لیگ برتر عربستان شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99093" target="_blank">📅 21:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99088">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vQ6_2wITOtD5uEt8btS1H5P_h5kNojA2Yf5lSuzyw8aQpc3QQcL-2SG3i8D6M1bwHLR541vp7SKa4pP9TWVftzyNY-jZjgrjnLInMb-5RN8tuu3Qk714MDotQjvkWBn99vl7tNpmp9JUI8sqzFn20hnq_aXBebri3PDjJX8SYHLml766h6mjkzpPPdB87vaU6k_bYkVmndhpXryENsSlnakviyEg2QGSnbteLNzmkPOYEcYwJcDYwhPt5mVQKQn_bVzhoItaD6ur_T0vUaLR9wzq_qgCnCO3LUsIhkRFPsvMNQF5jBJVWu-4JnZ3ywA0pzijA9jXsMojn-7-TVSWsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GMvmTHhfDAn9pAAP4HNtrgw2tuTXKZI4xlYvi27x_HMhnDI41mDlJToXWUGuUyC_VcZa2PxjV-pnmghYAaJOOmidRNIu0JVr5G4cPl9eZ9p-73HNBiFtOfxXZi10FbwEz_HbHb8CNmUSBAZihm3aXjLAM6fBxE9l1Sq9jDD7_azBZL9Q7zY6loFJ92FBcK1KnNHaW_T4AiznZRGdslHSqgSO669hXZYXuZUudFVD3p6bb5hoz3HcINDe9s-7x9pYv-khrzwzyC9x-3kZXMNO3Mtqlk-OOGt6C0_shdQTFri_puFdoSU3dhSpf6g_ItIpdU0nKpRsOGOnE1zII_peqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwqGaAW2GuUvYN0qL3PileiUvmr5Yok-RfwoeZScwxjZ-9r12k5JUV_LArojUYiUDesfV_kR0zn8WjtcVPrFw1MJGZVyNsXg7KCxO3BdSTHSM1hxcLmXM3ShTwEIE_fDLgzGCkF_1gRhZ9_LXLjDpkgHHGowE5z6xbf6up2y5NpDha3rMxzyN3f0MTaycElix-YN9JGwVhBCiTMSCXG4AlxieED2XHPCP9KSP0jOWCZPgf4oZ20K4r12hefoNA_35TKTKE8Ug20Rv24o9eOOqwHXj3mpAkv0u0w-1pBq0BeGLNMp8q4xz5Qqcfp-DPb2OLuyiRoZlntW1Qe8bxGr2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aY4aSTqdd4BQZuj7m_4PCQul8aZpCTB83G34QZuqwv8yyo0qDJjGF31KYhf6se095-G-tUbtjE93dnK-yunuBwSaQzlQ52OqTDXsZOc8H24TZgjrYQWWvu9CsK1ZJwl9iHDRIbUQesb6vg7LcnaWzsbRV6-YxlU5JyatYPvDZchUcbspPmGanVnZFIloDH87iEi6IMlS-yh5x76UGmUXmkJKdSB1404urtsemRvBzPTqVtMxutpyl8AqNb1C25kQfIZJL7r8gtU2xz-Q0DSUj2ZcxrpKWVjJRt0zmgcPVgAL9g46V5LwPZ3LkCUVgyB_M97Y9oAGGYmR8mVuBxlZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JbsH8kRslZINs7GwdLOvk0ltrD5igrWFjNOHhi_KmpohCLJu3Piu9tFSj_471zMiye1ogzzEWoeCUAIrmR-JWPLDNr4WpZBqpwE8qHsUGaUz3aVl3TfclBB_3wCMX0IcBTJO-Yi01IvlueBzxGf8HuMpagKUowQGx_b8x2md11VEXata9UXGE2ZWzsQ9awFf7TWO4SSl1rgg9KXd5qplpsgAnxy6XKA9opxO-KzRXKL0CiFu_f0_nv5eQ_AfzcF7pxSWOAaMJCDknJPfkv9a60Ft7OHf0McQiQ1HUhgKwGQQ13vIt-GnAI8LFegUE5UdKLP6qe0viztO8X0_chKXAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
والپیپر آوردم براتون :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99088" target="_blank">📅 21:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99087">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hi6XOfMSpSEOf-dLyU-H49j1iKPKqQbDi_CeFTib1ay-7wwSC8c7OtEFTulWUCO2z3VamTteJRDMnM3kyON6xfPUjE1sURzFjYt9KCdDvBhl7tmADiOOWrnMg0nUmMiBpjVvCZNABJtS8XReKxdEhX_P1FDBGxo4_Bc7NmIs0UhnJ7sU-Z5gRBw2OF1IWiwH0YN-3dKBJ5_aETYlNN1hWVriP1kqD8FKmw7iIaYCrSG3F7CMqB_Cesq2JvQtjYpgX0-Hbglo0QJ6fRmFUQlnNIZA9ehlq81-xAiVrwa84DJjOsi9OIjmj_yvXIn_PjwnKflLtgfeQ4jBjjqmJHi7BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوووووری
؛ رسانه‌ UOL برزیل: نیمار احتمال بسیار زیاد بزودی از فوتبال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99087" target="_blank">📅 21:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99086">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVzKqkBaeFq2IrHDUtuPjmgRBAuQURTLEOl_yLyHyMtZKo1stgEZHNQjT-FaIcJa6rs0L6XSKp4lqNMSZ-aLFTe6fY-i00ZhCLw5JibkQrM43nxGv7nSOgjI2kXV3b7_3Qpe3c8sGAiPZJ6K2ZKTIeTD6DCA8R1PNwhZFsIjUurmLLXfnXbUAMhRUe6AwU1aEi2VXqVtMj744hIveUVIQv5JWkkdJhBYvbMiUT0L2maUf2hIwYW-SjLemJplA2fGWJuv6CDz0_uPPA96zFTGDCUDBRwKVkZFc3QEC6muI_ivvJnm4njFXozhs2i0wzA5YovyHgs-7-2_j-Knd13Kmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین میتونه بدون بازی با حتی یک تیم از ۱۰ تیم برتر رنکینگ فیفا به نیمه‌نهایی جام جهانی برسه
‼️
🔺
علاوه بر اون اگه آرژانتین سوئیس رو شکست بده و نروژ هم انگلیس رو شکست بده، آرژانتین میتونه با شکست دادن نروژ در نیمه‌نهایی بدون اینکه با ۱۰ تیم برتر رنکینگ فیفا بازی کنه به فینال جام جهانی برسه.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99086" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99085">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHmHV7-kU1kNu5hbKMi4x3o5jlktVnW9gI87VzsUQFlTlQ3jhy12OspJUAbOt96U3aTL5b1ZWlEKEprHNxOoksVvbZJygsdQ0uadYYNDy9MB1y2lvADQE7hv1wpzaq4sh9QvPsTW8NeVYQn8OQ03pA6_E2zNpmU7uhry18O887KyWwx8FYv5EV_L8G-6lhcoX55tKueZnWWjs9gpk1Kyd5dnJNm38GDBOdkywXy2tL2qLtFyejybnkXUqcGTsU27vs0-4uREVp83-rARWAYTq3zFKB1_vaiMnRLpUClHJhkCrUR_6X_C2py9ubrooY6jT6sNhR-e3ij2Pe3dXymDRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
؛ فنرباغچه ترکیه با مارسی به توافق نهایی برای جذب گرینوود رسید تا این بازیکن را از تیم اتلتیکومادرید هایجک کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/99085" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99084">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPDW1IY7t8utwIZhlUIfDq8ogLWxj64wBYKhQPB1Rwe-QJOTjk-RbUap9Sug1UuHZ3CtaLGChGXmGlymnoBvl0urBw9TJxfmuGWuG-NVqONET1jfXlw0qnlrNFtVddfKFuiqo0nG_oqiQdvVKUwCX7D11l93wiGRPmpkEbvH7JhXMe-s7kqSig_mP7Fb6nOkP88kw0y2c9dEJ1SX1fscLmnSpXqEb2aGhBVOgSKF00ypJYJ-10CYtdfHwncx2TR2wgsgOfGp7fSG5S0NllrCEeX8oEx66FQDDm3SYSO-BinS9Ens4F0SJ2lJiwYqkFQmSTZTyiSHlyA9MXac5qqAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی خودت را ثبت کن!
🇲🇦
مراکش
🆚
🇫🇷
فرانسه
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇲🇦
مراکش یا
🇫🇷
فرانسه؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/99084" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99083">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbZMr77hb3GwLXRSzukjzrFG6BhFJeTiWQCsZkchourcLBOV9bWZdRnOHL0KRlIL-_EWYWKUR8NiccuABrAPUC41_XHnP3GDNRC3EUSldm8S0dWz9wWBWKtnfIphPuwVuF9vJoLj9j5ejXsNwbLGepgXjrb5WFnuiHcXa6NUZMkmNhtudZ-gdow8VoIjGmlKXargy3NkJMR9c62dD6sYHVXtIFvXRLUdeT3SY2QZb_u71A3UzFw6B65bsA-WUucEoDBXHbN-_ZMcXNqOs15K0PRrEoS4kxY41cxDtXnvV-FO4mKd3CfZ8Ce8mJ_-tcy7YSJeP6SKn2uA43uruWfSkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁳󠁣󠁴󠁿
#فوری
؛ روبرتو مارتینز سرمربی اخراجی پرتغال گزینه اصلی هدایت تیم‌ملی اسکاتلند است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/99083" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99082">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkp00vgFLT6P7IEpBAapOT0TrKrdtsJvM6nYWTWhv5DVJV7OTjnY8p-RPGg_7ut-wQEH1HLW7FBFS4T5l8_vHZ3HMAb98Op8444W4xO4IU_0Mxy6Mngt6UZe9_1U9DMqVLDmm_RXSS7cYAZzaf_fTEVI7n9HWrav3DD0ltaJqlAyTB4jcBmtCly2UnWGbmVuM63QBqFrC6_-hAtu9IYy4wfZ-ZOnC4PnwhAyi9EKWp9bMHagvjKrgSvGHqEJFsEvmYcOx39r2Ic7SmCsHh7fpxwPuHwhpJLb9BllGcyimzIKOzOHrQoqliC9gvFzR-1aGjQrXZ1syeQaGqvwwhxCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
الکساندر نوبل دروازه‌بان بایرن‌مونیخ با عقد قراردادی به بشیکتاش ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99082" target="_blank">📅 20:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99081">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoAQkzsOZdJc2HHQHROtH-BMeA8qJ5M8qCXQOKxYKcMYKGPdGUdd4EvNHV1v4zo9KV1NhCxVgBX9tkMaMXNZ3bQwq1uqMHXddAfN7udqV399K0z1vuCln8vZhQ-qsKUyNikKcOvKjdERrHqf0wn9npGBa0rMcOETqnG4Xc_I-yj6RfVGY2HO3G51Hz10N_PS_roInOABVYPyhs50fj3kfEU4ftvt7VOkmJnb4ZngA6aww3vX2mahy0zR9rwyMOjfriTHwLt2RW7wFIcxvfDRnQfkyeYYa6caSoB6BMY8Af_ircYsGIlu110CuKERwn1dZLkN8dUANEKaKjsFbVIwtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی به رودری اعلام کرده که ستون اصلی تیم در فصول آینده است و هیچ قصدی برای فروش ستاره خود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99081" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99080">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ ادعای برخی رسانه‌های انگلیسی: رافائل لیائو برای پیوستن به تاتنهام به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/99080" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99079">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdAMdK2V42I0c2qXxflbD5m0TPMt3VIrwpDZxGF6mSBkv8ymPYojSwqKgJV-795YKVABDu-3-xjtozHVLchB9TTVwKodkYiJH67gBtijMv25AvWztaTRZPt1y2iM53aB9jABkgLh_U_APzS9jTEopKU0H2zkmUqJfcXYi47DEUBEEzT34eY_o2iZnp4BqZmbL1DNGcklU3SM4XEN2Ejk9BgZstFvin2yFU8wfiecjH-oxTR4aVL6MfIWvMiWO6TBw7wF-8n_abYV1GOS0RQXUdcp3QCo38qV5KSRD0Z3jy9LtvvWRwDdTHKxSaO2p2F7o_FbyToU2T3XYEsoVJ988A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
برونو گیمارش از تمایل خود برای انتقال به آرسنال به مدیران نیوکاسل گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/99079" target="_blank">📅 20:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99078">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18362372c.mp4?token=DECLg5rKH8H5bwt29bccRkOvkowb-rL6p9FkBSC1rFFqVjTfeuV6xcEQXVNH-p-2lJVd0fh3HmtUd6XQheZ0squ1L3nGSuRgP8JxDlkVBA6flN8vEpffOwYlUVgSxRHqW6evw-Lo3UkEzVsJln4XvVDbsAWqpo2DRbg3jwwvasrtnxPxTgC4FWMdDjxT8-u2ZX2kylBRhmxC3taD91T4FHb_bG3JPWNzZ-OEZUk8BVGULKpKmrP-J1S52yhY7HuNmL80pC-jYO23Wyhhp3Lyanzj1HQDb3YhtTVpWqBF7RH5NPPTdIYvWT_A6164X8Ni_tg-6q6jQrmEesiOqTmAQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18362372c.mp4?token=DECLg5rKH8H5bwt29bccRkOvkowb-rL6p9FkBSC1rFFqVjTfeuV6xcEQXVNH-p-2lJVd0fh3HmtUd6XQheZ0squ1L3nGSuRgP8JxDlkVBA6flN8vEpffOwYlUVgSxRHqW6evw-Lo3UkEzVsJln4XvVDbsAWqpo2DRbg3jwwvasrtnxPxTgC4FWMdDjxT8-u2ZX2kylBRhmxC3taD91T4FHb_bG3JPWNzZ-OEZUk8BVGULKpKmrP-J1S52yhY7HuNmL80pC-jYO23Wyhhp3Lyanzj1HQDb3YhtTVpWqBF7RH5NPPTdIYvWT_A6164X8Ni_tg-6q6jQrmEesiOqTmAQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این چه سمی بود خدایا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/99078" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99077">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vct9NEMwEA-mr4vHhDzBK8LDAB9ZVo8Em7P1gbJ8kOCu7DLsTZvQL75RpDbWasdkze-LqN2AhaHBiRhfBz1z8_YszAmKv4S9_pNI4RbOKwQwPq7IZCfHEurMpwVWQ5w8F9y_IuUzgmXUo9zOhBsu76s0okLJP-3e8HS2CVWV06hM7x6-3pTkAs-8AVvK7zuUKhuMvlkVnFURZrdz796OZz3KPvx36UtSAY9LYzhFLrc84onJuTTS9eCYC8LMC5CPcyclEzZ15p2XagcKALx_YIHIXHD9tebj3wNLv6AuiKeHa-ogsdzGMe9cNweyZn8EFEtuMf2n2pysPjZ8A4pIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🗞
روزنامه رکورد پرتغال
: ژرژ ژسوس در تماس با CR7 اعلام کرده که مایل است به حضور این بازیکن در تیم‌ملی پرتغال ادامه دهد مگر اینکه خود این بازیکن تصمیم دیگری برای آینده‌اش بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/99077" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99076">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgEStz8ShP1CVV2z7YdjiBImXWy8YKQZUeiBlWHkToFprKQVW0sOjOkA1R4sHNlwKPLo4JMFKm2lkYT6oorB0IxymWZMx56udbxMM3FdC-zelCqm5WNXlNoO8DBcPZ2T5O-EZ2WHkBFTqmkPaedecVCFTed_iz-BCFRebgXd7mLoNG05Jztfd2N42Vt9VGrYNTQENA606sXNvqTcbaKKlOcNUat-U6BUqC0LF2HOZ23jJQ1LVWEFmBisEv9o7uX_u8YUsl4yzDgGLG0JtgHD-md4z1_qT-U35BcCCfp4rvkGT9EmVfGse4Xu4c8v63z3QF28AvK1tGIgAUC62pUd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گلهای دقیقه اخری جام جهانی تا این لحظه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99076" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99075">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_xnqUVhcsE5bjHOKMlipf624rdmN7jiQfYVgTKv0iIwM60TyB2quINjVKRjcrCPH3YDuFG8RLmRZ6zQxwAITFu9Gb_LSAqGJWTyHSlroWT06ZHxpnfsULqVcCAopyU4v3UMboLbc6TAtyvEw4_9JofVrIDZtqZZweDfVrrUO8k0wZd8dO_uvUTGmeI5Xm0s7sKe1OJsFFj8z6VdBZtAWW3dWD0BKxEj4wvTYaNR5WRat2LwBF5Xq72gPPijapz-pU7Xhgd6Mnv8AMZxDr8YuvneoZqo_tEWr5Dk-ExKkPfmBxO8dfhLLFL1sl2EOjgCBhdb3jO_aC_WeTy44P8CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: موضع اتلتیکو مادرید هیچ تغییری نکرده.
❌
❗️
اتلتیکو قصد ندارد به جولیان آلوارز اجازه دهد به باشگاه رویایی‌اش منتقل شود. این موضوع چند هفته پیش به خود آلوارز اطلاع داده شده بود. اتلتیکو تاکید دارد که تغییر موضع در این پرونده غیرممکن است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99075" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99074">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/99074" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99073">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhKranrZGamx-8lUI3tauHwzpGqnYx94B-M9f1o7eRnkYNq330LN0SpjTuwFocG6Cr_s1LYKT35hzt29MZ2t_SjrFnVTQJcVZUv4YBRKqwarEJ0Q_sCMKSTSSl8aT6jdjEjvD0qFICCCou3TuhrJY3DW84cXvvJieSfTTeGziGVyaR0vt6r1l2fRv2n1tNC-ZqxgfoNn-PHZhmODRtThQXjqTFNnYGgEjj8SYSMgSApZk9P12lFhMomfI82BVdmdc76I5WLOvSGzlSKi7zuT1MuNgcazyplBGMLMjfpJBksPNQ-YzxERgmPgQhfICFeLSRWkWZg1N47KVUMGh0g5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99073" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99072">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=Wji1A8AlgVxEGbw5mPKQQNvyG77KdfEA4WQq_Y4izRX4a3LCpR2UMcIUtiWa0aGK4bFthhngQc7xL30eLJuhez-UrZB_FHQH-K4ipZm55LAAWZHjrHdfxyWIT4u4AClFrI4p4wGfVzHpzSxp6wQSw4WcpOWlzA3COlJHHU98tHffepenOg_fzS82pcUwQSJdPtoTWnJkGT55iG1g0PIqf8LgIpppi2XEuqM-WFU1KbzpdikuhnS-J9D-kYFu73G-nUKAXsWal6-tczMbUtOiTVXeu4QF3G8yZxbvZS331mbWSz_NAbta8_Zcsm5gttAFHbAomgg30pCchyjvzw60TRw3cqlZ3dVWpnRbdkcOHq3LDt6USUpqq-4-_JJSWIcqpq3YZwPpviwbpNny3CCRtzJLMSBZ-uHxW8xyc33oRXWhA0huJUn-hdCET9tur19XjVm2HMgk4G4DkqY3JY2PPtRPvVOmY6peucfNypna84KH4jpPfGoBnvB1PoalK0W29-YD775fBd5c8jxJe5p3Das3-R_hK2MI1gD8QeW8zJcqj5kLt1JymeKEzPm8H1GxeL9s1GOHEI2GEGYA5U5JIYPuNcihc-G0FDLqYW7rrYnUWf3WlHX6eaBFllCbPBBcLz-5X30vEfMGpLDoaK5Xx2VK_KlkR2FbYzrv_IkAgmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=Wji1A8AlgVxEGbw5mPKQQNvyG77KdfEA4WQq_Y4izRX4a3LCpR2UMcIUtiWa0aGK4bFthhngQc7xL30eLJuhez-UrZB_FHQH-K4ipZm55LAAWZHjrHdfxyWIT4u4AClFrI4p4wGfVzHpzSxp6wQSw4WcpOWlzA3COlJHHU98tHffepenOg_fzS82pcUwQSJdPtoTWnJkGT55iG1g0PIqf8LgIpppi2XEuqM-WFU1KbzpdikuhnS-J9D-kYFu73G-nUKAXsWal6-tczMbUtOiTVXeu4QF3G8yZxbvZS331mbWSz_NAbta8_Zcsm5gttAFHbAomgg30pCchyjvzw60TRw3cqlZ3dVWpnRbdkcOHq3LDt6USUpqq-4-_JJSWIcqpq3YZwPpviwbpNny3CCRtzJLMSBZ-uHxW8xyc33oRXWhA0huJUn-hdCET9tur19XjVm2HMgk4G4DkqY3JY2PPtRPvVOmY6peucfNypna84KH4jpPfGoBnvB1PoalK0W29-YD775fBd5c8jxJe5p3Das3-R_hK2MI1gD8QeW8zJcqj5kLt1JymeKEzPm8H1GxeL9s1GOHEI2GEGYA5U5JIYPuNcihc-G0FDLqYW7rrYnUWf3WlHX6eaBFllCbPBBcLz-5X30vEfMGpLDoaK5Xx2VK_KlkR2FbYzrv_IkAgmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
تاریخچه تعداد یازده بازیکن در فوتبال از کجا شکل گرفته؟ ویدیو جالبیه ببینید حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/99072" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99071">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/99071" target="_blank">📅 19:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99070">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GliPMwPIwI_UpPks6jO1HcrRd9K1SczHI0U7Oo2zNtbcqsWRVlBDlQL49l6sngahihK4eCtOXvNxogMbKapoDHM6T3RWMaR4Y3WYWk1NgQc7Get8Q1aHh6_92itpOLvN29kn_mgpjje6CHOtlAMbJgPeAkGwHMeyNb_IjDw1AEfISYyZz1etqNcCJJCA4zBYRprQeuks8NGKRw67E3_1uENdZKvuNEqR075i2jy0OLgi-H4tQPbk5AlhRyiNnlin7VKsV8j_5Sc-Ex8HbG5AgxFtNfWdRGvz0ZZnLdMAqqT4on1PpaUtamU8rN-MMnC45zlYh6VFDg9RWAlp61ghyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/99070" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99066">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EOEWQ2letpvYYbFYGKlOBiPWivsDNElHlRATgVkAh5k66sXmKWfO7mAdYM45CUHeAvGhndlxDpF3L0Jvs_H5yXF3OQRSdzVl4IKm94jKTQufzEKjtFpoYTEVbWR303j8oVVw6mMM33zYW_MGs9aj23Lh8QvEe_U7YykjmJb0Op06c1AnMt4MvgVpG1u7t8ULH60i3xFcs8NPVuEWsOU2ywsQ8-Y7Uniuqvge18yktFEarKFJ-IQd2Y5ceEyeReNMjqs9vnDzNCZ_BltZNcLLXdaoN_wdlegDe0M6hTsd6cYTHJRTkvEc_mTSCoZ9wQLR3kBzh3P6ImMrabpR5r0c2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d7jd857yteLjbT7TRK00_XvPQEvT7Q_7CgOSEZgEzJ__QniDqSjq-TOtAas--u_UzKldbwVTSP-ZKQzgfdHLdkFxD3q57-SfSAbaaTWSD-3q5Orn7f899V_Ln3ulhiDy2yEjAgtmxbGQjHhlxB1fv7IQrdMTmIAUsn6Sk8n0i9S_RzGmw34-ueZAKg-irbNixmHwlbW9uDkdzBa3mPHy8z6JlEMw9V01IxcWz3gDHaZejU3SiTILSpkHIdI3E5O3nNSRxMwtHmgtbkInFO-8I5rPLGIs9luQ7Bpgc54U-sp3yQ5mWTmVWoUhXcdTASSAsrXV5u4P0kxD_apJWKn21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TB17DbsxAftrKNUuDR_eMsp_WjoqnaqfAhYA3Wu9q5yfm7jhTSG_HPaEdiqFjm4xxAqakXoS3ZNPEkdhDye86d9avdcRh444t49BaO82WURZFb92vuj55Uv2F-m6UOIa3mHzBCQPC84gSTglnF0kENSOoK5NnbioZVioRdT9MMuNcetrhqij0wvY2ku4wUKc0czepfiUutxvPPEpWI8BmeF331JwZpNc_298zjgAQkolgX7MtF9k_OO3fSh67GAlc3PWDwAruiEOX0-knPLQA3IqrO7zonAebfRzp0IXrXz6vg5uoetzYDoIJ9GLPLq43LdLuehHMv1l6MMdvNdnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDna1_D9kvsKGdpPAIJQg0qrdVGcQd0bEqZlUE3zovbGPNSnnDsPQuk6aiUizSdtugHAs_8qBNMQ-lybVPl6prZoYtzYPYXoi8n1zanKAn7xlUmNw3NxBs9PxpUETuKXd_hD6HEDixfC5YJXl5DFx4ZVIPzD2xl58d1JBtiF6tMMqot4EyhQeNIJEQiAm4k__3fAytvHG9O99Tg6INEeEtAYqo5k-xLntYcp53Qx41q5sxHxByFXaW0b7PR-_C8tPR4vPdJLMZXzGuOPUjVe5Ucf371INXVrSGY2bE4FJm7rChdku1VO1t-HiQNwFm8KpTn9JZLnQ_lw84KsW5jPnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇪
همسر جذاب کوین‌دیبروینه در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99066" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uqNta-4FWlecEYNnf4R3QN1XtQLohM75Bf4b3a4vTQY4SpLVd1vDsccHAqvKUd4MDEELefiG7ESwEP2hEGlJZNprAEugCVQXPuLvLz7dWGPeqyRMAaqOtfUS5BPOeeXtdxx6CvClnAtunhL3PDvRYolSNRJCXD8rKPJyFvBdOz3jE83R133A3_OdluIS9e5WkTXTJQlzb1ZOzIL3pAOS5bWpCtL3Q7kS1GQAQP_06RirE4kJNby1zHIGktVENDktFIGDH1UGEkzAP2yl15onoDMtAMiIN9LlLlSQa6dzbjhGzXe4K5YTvyGvJZLL9pAqi7BwWWAwF159BLXNl3TXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/plY-J9VCH1f6fc0YLPqJk_5cEym1UJoTP1A7nQgP-zWhcPI_1ENFMjtzLQI6SE8tt8tjNBC5S5hsDoi7_QygE8pj5M26_PVHZ4RffP1Dn9gv4mM1sCGEJ3x1_ieh_j4nJsuU0F8kSw7JO357Z_5sZtoIeh0A-DTlz9npBfskrNWl7Z1hnLF5rreWIu64842nwj2UFulrSdGZGOossdRwlnVg9pK_h3p3nms0NCPs6RW0X8LnptvbCfEazbNRKqtn7VbUP0oBd2PQqNscUkMZXTqLPqWFrczYMHNvNKX6Ni-IDk3CyZcFUTAs0aJfsFuJWWq57-u57km9ZsCRMRKIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUW46JwcMoPaDLBK-_tItU4fNpOBd0paVz7n92JWjCOK_wp6vxYusb3v_StQ38lzBGiZnWsPrczz1ckaw2FHzDEl3xtZiBKIWcxkBIDKLdlU4bwDT6GGNUoHbBJPrNTuqKaNyDeJ1fg4LhQqzHliwgzxj276_2qQIvWDNi95yO9pnLnGRJbfgdSqA7A2aXp91sdbkXYpgvmcc-nlBB8c2r88rG1e_bluYlDbTk27HZIEdE8ObHIx7rR1RqNzh3hLdE00bBzOIbPnO_EB0wv08L7cFRLx91R5EHxtN4P077uOU1z9n1J1xjpSTy5l57-WDVji56WX1tKjOcMnJ7wIfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسپانیا قهرمان جام‌جهانی بشه چه چیزاییو قراره تجربه کنیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99063" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=rLdf5g17TOnOe3OQb0bf-Y6E9TqEi_TirU1rMLbUr20ol2_UtQyGoNYi_RYpRRZrOk-ZlvT7JN8DZTM7qDxocjwpWPSYhsuMcvA7-NmZC5yCvALGs4ONUu-rUkyOiqA7h94Uqi1ptUcFcLEVvIIJvd0BgUMLLDEzpPZLmkHVVe-VjeCxl_INgBcqA4PdiMlUKN61JUDWV6QCx5-PPqSCBbyzSwlZWNXujvKioZ1zQk5QNei7zlOx8jNBmIfEb4XEOltPqD-vTph09pKKB8tx5oGscx1AvUBkOboCu1dM7Wznz6LfQGt9EJnNKewzqwLsSPw6P0f69UzfzCK4q4f1-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=rLdf5g17TOnOe3OQb0bf-Y6E9TqEi_TirU1rMLbUr20ol2_UtQyGoNYi_RYpRRZrOk-ZlvT7JN8DZTM7qDxocjwpWPSYhsuMcvA7-NmZC5yCvALGs4ONUu-rUkyOiqA7h94Uqi1ptUcFcLEVvIIJvd0BgUMLLDEzpPZLmkHVVe-VjeCxl_INgBcqA4PdiMlUKN61JUDWV6QCx5-PPqSCBbyzSwlZWNXujvKioZ1zQk5QNei7zlOx8jNBmIfEb4XEOltPqD-vTph09pKKB8tx5oGscx1AvUBkOboCu1dM7Wznz6LfQGt9EJnNKewzqwLsSPw6P0f69UzfzCK4q4f1-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
صحبت‌های جالب علیرضا فغانی درباره چگونگی آشنایی و ازدواج با همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/99062" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99057">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22194ef951.mp4?token=jAmzImPHrucujKwzkdb_p-SLk0N6SDZHeSlNksA-PuftGIc0SpCx77SOPAV2a4pQBwLrZV20UH55YFQMnVC8WWx_loVFtYZ56V4wWvJVumWGql3_s10N-CcGivb8o0Wyk76XjINI3Tw_noLokqcbYzCsfLU3J0B8eGpyqqD8Y6umfQkD7uimuUEORmusZ3sjbTwhYtflEFL08h-2yBTZoj8A5sYkcFf_9NnZHM5eBTfOgOtlHTusGEzYFSDag88MJgbd2HeQR4plSzfQZhnv9i_LDA5-iwa63YGBxNzUTx66_mlZ3yMr2zBcs5avNZFhvxX_-hsZiVPWFB6y3erkw40wN6hO-Ps3XHrK5IZcTwP5fu1QPLrP4CjQtmc032xINgYTMvk0whpTls8MYB_e8XWy88P3Ri_Z4SBToXaGK9dDcr6mo9_OitbBMpGr-FGekbzBaG051jfn2rKnyZiUFAietCbgkcGn3CmV3ot4yqOIFpfFYLFHPkLdfCorgVf9MVAMt2WneX11sEnDLKdpMeXf5U3s_GsKuODw3BcJHUu7cxVO7D6DRx1xj9VOHRDVrw1NXkQ8b0n2Y_2eqKPavzd4PB6udfGAEWV1c8MNRTE5iyoXkP_sDr-sjDjuDacAph1e-j3BQBhNyKQ1voqBD6bb_3s-owC00ZG2Q7t5bUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22194ef951.mp4?token=jAmzImPHrucujKwzkdb_p-SLk0N6SDZHeSlNksA-PuftGIc0SpCx77SOPAV2a4pQBwLrZV20UH55YFQMnVC8WWx_loVFtYZ56V4wWvJVumWGql3_s10N-CcGivb8o0Wyk76XjINI3Tw_noLokqcbYzCsfLU3J0B8eGpyqqD8Y6umfQkD7uimuUEORmusZ3sjbTwhYtflEFL08h-2yBTZoj8A5sYkcFf_9NnZHM5eBTfOgOtlHTusGEzYFSDag88MJgbd2HeQR4plSzfQZhnv9i_LDA5-iwa63YGBxNzUTx66_mlZ3yMr2zBcs5avNZFhvxX_-hsZiVPWFB6y3erkw40wN6hO-Ps3XHrK5IZcTwP5fu1QPLrP4CjQtmc032xINgYTMvk0whpTls8MYB_e8XWy88P3Ri_Z4SBToXaGK9dDcr6mo9_OitbBMpGr-FGekbzBaG051jfn2rKnyZiUFAietCbgkcGn3CmV3ot4yqOIFpfFYLFHPkLdfCorgVf9MVAMt2WneX11sEnDLKdpMeXf5U3s_GsKuODw3BcJHUu7cxVO7D6DRx1xj9VOHRDVrw1NXkQ8b0n2Y_2eqKPavzd4PB6udfGAEWV1c8MNRTE5iyoXkP_sDr-sjDjuDacAph1e-j3BQBhNyKQ1voqBD6bb_3s-owC00ZG2Q7t5bUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فشاری‌شدن بازیکنان مصر از تکنیک لائوتارو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/99057" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99056">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssNSpMMd-wUcb0wzdbBwBx566soBKCv9v-lh-rowBbvfpXaczKhocHmBXAOBktbP9UQG6ujKXJcNh-MAP-lmPgC2DUfqiN1DokGv1ASQZDujn2Xy7PkBbNLNXsGU2H81CO0pN2WkkNjLbMlI1PiVcTlVwFPwe6IdSyhTWhp_fGqpf_k6vyzSTeah-6FdjfNqkSNPjKzA4v5B6C8G6O8lmFzoPFA04JYEDR9B_NtFq1QrvX6BjN_P550gncqVcZyvGXwdCFZ0F10KhxVh__jdS6AgYLwy8NPumNHbatEOjMQzwLdx2oeoTx5bQGQkiris3Jqhfy873r926wbwYuQRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJ6Otdkqck8Jhzwa0lEG05Hkd3kOn3e2HJPxVco2UoCunOSursiHOSidrga88aPLRyGPdHvqeUPZWZLofniW8Bowrucje2q8m-NU88vLj5x9imFgJzfvoETTfIypffqQnkSjzlWNMwQH5zmcfv1rcBvEZJQ3tS3qGYDPJRv-HVaP7FelWuCpTUrE2BfULoexSC-LU4ALan2D0fj8YAlLDxfZpfnhy-HiY9nB9GLFFtuR-QklheZmdychCyDF0jbXwuQyGrs1bgrvMSsQDlWXdA17C57HmX-_NVMIdxjYWnwI0AipkQGvaVTs_ZCYQgPIonNlRFN9Mi_ODcHgpg0itg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK_PKFqszNZbzPwEIGqJXl3WpY6T5inxrwhh7UmpJqcZb_LznUAquvIxxh9FXJXj-7zNUFFiFvgyhh6IvpLWoUzeQm-FFEJMxrXFK71Hppu1UgwARgMpAVDQuMXyn56_YojiBlLGRaaIEi-ZjltNr0M9mvQ1XJXSHIelaYcbjRx2INA_DSi_WRTNi0Ny4Ot-klubBCxfp7aQa--w8sUWcZB09KPSUeEFRs2ZllCX_hxMptRv3cyzYcJXwBiPZ8iiH3lNk9T9Du1RI7TIgVCJBtjtjFSaN9FAFxyaC3IzfPTmStaI6suPYpff53xPHRHcakMWGgSBUviDO32WmwkM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4MqTqO8m7d_6XQtSxZZxQMaRQbriOTamniHhNxp72xlKtoqS6TLIq7jg7TsiS9bXukfV0fmGLamTUxiCetyJMvSmXJFXIcq457L-C8JdotXyssExvEPvrjfL8gh7vfyHLasyt-2MWBRD8nuJaVffEAamrdg3_Jxm0Ap0yFG9CCNw8krFvMmuv2IwHhqeGNTgaTlj3zQaXipmEH81-9-fJ0ZTd6zaViT71YaTiRiExbZL4aTLChQbydio_9pzlzq5wkR8hZwJBEwDoOzjxHeZmRISJf6x7Zx5g_NLzlP3skouQ_RvTl-hj_v2Kfl421zUlQ6cs4Dhd0qO6I-zdoQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eS1gmnVlomWmtIv7kufD7I1WkJG_lqS74J6ur4nkaaLdiqRRdTJSTlbDSQ9_kuul6BY6SdKdeu85hyR2Wg9P1Izj5rwb6WbfzZZAXNZICMpBlkDMvnOCqomCTRDMxT2PRmsB-j0VrgXoBXG77Iod06ZPQnZ0fM6y6iZYkBFSR9x515ohxIAse2-p8zvaW78bdlXrHSalOZByhFkDtu1r6DhikYeeCqb1Z2PecPoIJ-iIZWiHT_F-LwzKq-xciwF3cvR8Gc6mtw6gbq-7TyYwnGXZwLsZ1sP88hEmUEPk3zti8uVVGWL6eJjyJA_v1PUosz55KbsxjYdnaGWq7oS9-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
همسر باردار فابیان‌رویز ستاره اسپانیا در محل برگزاری بازی با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99056" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99055">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEUrc066-Eo12vl1AhE22PocgKm3SK-ylYVxBscLtQg5qztOP8V09aWZFMwJ2bZzKVC6haKjT0tQN9ISjxf84CjwvVVYiD10FJ1wkUegLQD6XknM4XEcBJotewcvGeM8I_GmDxbkEodZJ1y1p1bHlIeVfv_LOAQuSvqrKupgaN05PbsfB-c9nRF3TvEt4Zo6jMenqwXM4UHDaewt18DiTgZ2Ne0EJ7IR9S-1Ei56UnBrzMlNWQPJsYrvP5rXXhC1BdnIwoAvlnYvXrZfhAIuL0lOBC0Z_4Y8Ek5jG6UZv2qMtfAI_h2MGLDolAoDaPwYafXaFWL9YsoaSR2BLEmwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رامون آلواز:
اورلین شوامنی با اطمینان 100 درصدی در فصل آینده در رئال مادرید باقی خواهد ماند و از این تیم جدا نخواهد شد. او به منچستریونایتد نخواهد پیوست، این موضوع به پایان رسیده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/99055" target="_blank">📅 18:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99054">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnLN_m5Dj7BlZM_mJVJ838qcfZYaPvyfWW-EnuEx96oR1BluIyopHllvahMyikBa_hdzK9sVT1DOwYxI38ooX-zUWsIw4UwS_o8dak3hdXu1urlFRqQw-JEp-9K3TSB-LJThnrHVg0kZ1QTP5DmrqYkwszLltEPyaUvaZ-fN-yoyRxXqYQ2XGxGgTphj0jQ2sclWjUTxqi_kev3eZpU8U2VUar1G6wc0dOX3kqPdHU6lLiJMFv6vcvLq9YIxF0rWdr54INBpU_CK7sbVnVOIck6eqmutK50yDR97U-okU-ZSV9usj-hXxKaK-GXR5Ilqrq_6JCavfSxA_6Ev-hcNrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🎙️
دشان در مورد انتخاب داور آرژانتینی بازی فرداشب با مراکش
:
"انتخاباتی وجود دارد و ما باید با آن کنار بیاییم. من به داوران اعتماد دارم. امیدوارم داور ما به اندازه آقای لیتکسر در بازی آرژانتین و مصر، کارآمد باشد. رقیب ما مراکش است، نه داور."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/99054" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAzDEjB8UXEWFA0-CxspRTAU421VILVL8TnCuROVhBsiwCl0pavNHC_PlPhGVfE7ZR8iNiB_Qalo3TIyzseD9cWvE-P7lMc-W6tnSq2QQVTkiErKt39CrWfzQz31hIR45DvSO_bpWmH9eKG-Or5IYZ7y0mTeDMVnhqOwIedblwxUcwU1UXOCAgCtsLEbhQtuFkvvY0bajjuwEu2C2QmUJZU1aZiwcuAiZ0saw9UyetsFbMEBhQGxIsM0z3nyuOfb2BBEEj3rhHb4KgjgbHFRmOQcqvFZb-A8dOT7g5ywKqtOnvrhemPAvD6uli8kMGH4sjS2v9uUyqJIs8A4DXQEFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عملکرد لیونل‌مسی در ۹ بازی اخیر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/99053" target="_blank">📅 18:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gc8zbhr75rNRpjjoHPSOjC8bvf23jX043yTcjD4NTAYqPdLJBznckCZqZGRpS1eg9GdYGwWqIb3LlYBJIkp1c6MhLJaYylj2JBgmfD2EmY_ilZ55-3_zBh-wiu3TVsCPNebI-lgBbFdn5Bx_G_QVEusB9APehlUHIY-akwR0I1vESAHI44xBkYrDHJ8Wjb1fO-jkrWnV_k_Df8rRmAO-yXpZNBU_oxZ4rJiP-D6mpyAsPGsV-O7LKimiw2R2hL3v11o3e-BnKE-UtFBfTC7idUh0k8ym4-IDDpBcd6StJA571rPkS1nvalYHTb-3jjVALfZZJGVn2InzkgvOnUpmKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇬
ابراهیم حسن مربی تیم‌ملی مصر: هدف فیفا برنده شدن توپ‌طلا توسط لیونل‌مسی است درحالی که همگان می‌دانند لیگ‌آمریکا را نهایتا ۳ نفر تماشا کنند و اصلا سطح فنی خوبی ندارد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99052" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=dnrTAX4BNrfEN0UvF86O9EdP1GFCYp6ct0HEXnlO9Iv1nOcvGgXuDIQur6XQRX7R-PZrf2BT2_lvKfXdXYUhizHjp74Z2pwaOrzlpLeeARFQj1JqYT3iv8pEOWdTuv9P9bEKg5FE4gqFDeqDPtgs9XrjaQ35O5A_eyyb5l4TE03Z0Ch4uHDQnLKbxOu3zv-P1mQtXqTmTRtYSIRQJSl1LHqBbVBgAjvIH-5jjHM0T8DoOWqQkjrDYXGEdVfRnyC1-EuO60DWJvjcUE6U_MI5b8MKRHS9Fj8YzVMDYYlIM-dTOW8eg9RBfQNWZjGR_M_S1P6gybTATA2ofrzcJK_auA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=dnrTAX4BNrfEN0UvF86O9EdP1GFCYp6ct0HEXnlO9Iv1nOcvGgXuDIQur6XQRX7R-PZrf2BT2_lvKfXdXYUhizHjp74Z2pwaOrzlpLeeARFQj1JqYT3iv8pEOWdTuv9P9bEKg5FE4gqFDeqDPtgs9XrjaQ35O5A_eyyb5l4TE03Z0Ch4uHDQnLKbxOu3zv-P1mQtXqTmTRtYSIRQJSl1LHqBbVBgAjvIH-5jjHM0T8DoOWqQkjrDYXGEdVfRnyC1-EuO60DWJvjcUE6U_MI5b8MKRHS9Fj8YzVMDYYlIM-dTOW8eg9RBfQNWZjGR_M_S1P6gybTATA2ofrzcJK_auA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇦🇷
صدای وحشتناک شادی مردم در خیابونای شهر بوئنوس‌آیرس آرژانتین بعد گلزنی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99051" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=Kn_1dG7dz6lG24VfPdRLSKiP5KYi_-g7-3A4rnjsMXBSp0DcG9cbaNKhEQIN7awInoea_x5oeM8v7ibs5GO65VfEo1Eh47Lu5NDajZaYABSqSpURXxbTlDzKd-lLUCF5dDORc4vr14vLkJPj2RdZITZdEao8h9tE2ftglcmzYk1xlj2B8lIec_avgHW3DG36HMSEapKn8w-jeSnEfAvJiQV630I0FOE_x7h7ACXuW3DAioyjxBBc-Ugud0OE8cttmshOVM9-8SMiirIciWuuo6874Xc97_THNyZemRR-HzcASMyI8U43nQduhCFC5vSr86Qq6kSuJGb4A6EtftFekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=Kn_1dG7dz6lG24VfPdRLSKiP5KYi_-g7-3A4rnjsMXBSp0DcG9cbaNKhEQIN7awInoea_x5oeM8v7ibs5GO65VfEo1Eh47Lu5NDajZaYABSqSpURXxbTlDzKd-lLUCF5dDORc4vr14vLkJPj2RdZITZdEao8h9tE2ftglcmzYk1xlj2B8lIec_avgHW3DG36HMSEapKn8w-jeSnEfAvJiQV630I0FOE_x7h7ACXuW3DAioyjxBBc-Ugud0OE8cttmshOVM9-8SMiirIciWuuo6874Xc97_THNyZemRR-HzcASMyI8U43nQduhCFC5vSr86Qq6kSuJGb4A6EtftFekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم‌ لائوتارو و همسرش بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99050" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: پیت‌ هگست از ایده ترور مقامات ایرانی در مراسم تشییع علی خامنه‌ای استقبال کرد. ممکن است دستور یک حمله تمام عیار به ایران صادر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/Futball180TV/99049" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4vwd-JNylWDoCRRMtxN-vDddEDp_xKpdjcj7wsaJL4lWa7gGOyBQaSSkHCX5Mh8RZyg9SGCSYWJ-6s9gKaplucPEhsbJB39bsO1zMekrcTCESGRMFo1pvF4HLPQsGa_8QEpEG2Kg_v0Fml3cE3nCXIE_fV_kyvnit7UAI8f1-jFdX4B89qdsm42_W-oMma1ZlPij54wCmMmgJI7FKMBoBGcBQMJZP1Pzshg7Ww-4_qTnDPzMTmqW1nV56bEPg3mUql-BT_T49fYsh9towef5V5e30OBGPqiNf-Gj304IPQIP1oASh9oV1SoWGaq3DSCBxCgFI7wrzANbrJKQOSM6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4vwd-JNylWDoCRRMtxN-vDddEDp_xKpdjcj7wsaJL4lWa7gGOyBQaSSkHCX5Mh8RZyg9SGCSYWJ-6s9gKaplucPEhsbJB39bsO1zMekrcTCESGRMFo1pvF4HLPQsGa_8QEpEG2Kg_v0Fml3cE3nCXIE_fV_kyvnit7UAI8f1-jFdX4B89qdsm42_W-oMma1ZlPij54wCmMmgJI7FKMBoBGcBQMJZP1Pzshg7Ww-4_qTnDPzMTmqW1nV56bEPg3mUql-BT_T49fYsh9towef5V5e30OBGPqiNf-Gj304IPQIP1oASh9oV1SoWGaq3DSCBxCgFI7wrzANbrJKQOSM6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی از نیمکت مصر در صحنه دریافت گل‌سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99048" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
آنالیز‌ گل‌سوم آرژانتین مقابل مصر؛ چه ضد حمله وحشیانه‌ای زدن و انزو چه کاری کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99047" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99045">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lI-ffsU2Qd08OsXYBG9sjxCCvlkP6IKlwJE8tj-ruBL9Zy5C_PK2CuRagwfoxJmTjfW-gwzTEE61hIHPksbbwh1G6FaUYckkE0ioot8AmiMj8iD1bqlDtqhrFXq7dxb_4nqBoUw9Fn4TAoBuoNZ-LZmQ-3Lr81nafK1VAHMnssfR52CsxWaJ6YiQFL1l9Cq3UA2b-yJCA5Nasx5H9kq52RzQAFWGnqYaenrCeJW28VVQgOLbubXNAq3hmTebQziRh0DQDhBdaW2A0nQJ-GseVVqIIA83_McMmB4UhfscmDRYa2Mj5NGcuCDRG4dh4L79x1h_UplG5nXFo-4AajGenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0clupOW7AwHKyPsQm_UuxqkOaj9FzqDvBriMmkrZwY00OJ1G88fzHMu3M8IuaLObWZNFUXNBaTNczV4uW2t9mzyOLb0Ei4KEX5abl4pmzzDHo8NI7bDZXjscdZengJZeOm_7TleBOadpHrX6RiEVBDtJET4WLNd2WkPWzIuGrmO1Rwv6NbRw-pwap-ofurcLGUraPbTi7lrqxFcKVwRQ_nBFOrx_aCNZh_6Hqe0fKRqUMw_z9B4I3GtJeDQIKSY2LtuN7vSX-KntpUoCexdp-j-untzABkEQmhEK403PI6L5a1faC2rfGIJheqY_-DuLrS7-OTLLpA_zSWuhZjFZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بازدید روبن‌ آموریم از موزه افتخارات میلان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/99045" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99044">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔥
🇦🇷
هیجان بالای گزارشگر تلویزیون آرژانتین در صحنه گلزنی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/99044" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99043">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWNUK6Hi9swDs3W8wZTg8pGa_2S3V0CzOpv7T65fULFmqbhDdHb20GGBaXz_BjCnI4K0GYAux4RcbdsycSesC42dbh-1MI1ebY5e-xcvrdautXXJ1Vfv2yLlmJrhTp0g9y2rIkQH_DC9HW3Fig56agKUBSIgm9IFm-ul7M1B1AS28BAHm3rxAYZc2gzpguSDfqGgMrs6jNaJvPvvSX1xBzR3yfLHfXj9IB9amE5GuLsn6YaXwg5KrbxovSx3FgvNzPCFdnYCDqiqgTtyhV65I7ZkK0DzIjDbwRniRbBy_bTvbNcBooVEV9AvFivz0-r5SZGs8n59Z4BvMaF6ixNYcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🇪🇬
تصویری جنجالی از داور بازی دیشب مصر و آرژانتین در ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99043" target="_blank">📅 16:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99042">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=c1ai11YJH9QHFBHckhTIsSLgnDZdbP10S3Mc3gERPc1HyEFviURAucCWKDhFBDDf4Wwoi5sCbPd9k0U5Je89LCYIl4Gt-osW1yyNpr1lyS5HZ1_PHVMLGedh69KCjoIU7WEYPPyv2VWypv501zQ6MTsc3wnnMQmF7kawIfsmfWnoum_4hcsPasE9gF6EtPGOsShmue3zIaCPB3X9sjhjwGdtMqtXvdMRpAL9a_1u4a350n7n_bP_lHObRiIOrXd-gshQek247tZedVVFu3kTChyIbw52aIBt4NYvaCz4GQjCN64UHh9kXzJS1_yycolEeXw-Yp2kjRiqAhybAM_I1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=c1ai11YJH9QHFBHckhTIsSLgnDZdbP10S3Mc3gERPc1HyEFviURAucCWKDhFBDDf4Wwoi5sCbPd9k0U5Je89LCYIl4Gt-osW1yyNpr1lyS5HZ1_PHVMLGedh69KCjoIU7WEYPPyv2VWypv501zQ6MTsc3wnnMQmF7kawIfsmfWnoum_4hcsPasE9gF6EtPGOsShmue3zIaCPB3X9sjhjwGdtMqtXvdMRpAL9a_1u4a350n7n_bP_lHObRiIOrXd-gshQek247tZedVVFu3kTChyIbw52aIBt4NYvaCz4GQjCN64UHh9kXzJS1_yycolEeXw-Yp2kjRiqAhybAM_I1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🇪🇬
تصور اشتباه مصری‌ها از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99042" target="_blank">📅 15:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99041">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=DzKI14w7IKZxQe-FG1YUwRHUCKpGcmOIXAk73s67SM20VQ0XOaW8jBzLYe56xEZ6hy1_epphF6jrYzOiDPeKz-iiCamJgJv7sD5KuHIKpx9SgeAoIGsEZ5C1Ml7hjhU4un-c88vJVpO9f-AwQ5_xviH7j6eYV1tf6k5v6H43iE1mJrQqQ_13YNP-Ztxmrs4Ym_NoZ9LVoihNeIz7KO-8GzBgLe15VlZUA-GWl6dKUQ-qlV1Lu2TVTQApGh0XR7SuY4x3KwneqCB1LgsW6hvVIJZ4nOBwI6sCiielzCGhF-Z7gi-I_di5MZfwmAn1tKM37BI8kB3YyMmTD2-miOwlhIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=DzKI14w7IKZxQe-FG1YUwRHUCKpGcmOIXAk73s67SM20VQ0XOaW8jBzLYe56xEZ6hy1_epphF6jrYzOiDPeKz-iiCamJgJv7sD5KuHIKpx9SgeAoIGsEZ5C1Ml7hjhU4un-c88vJVpO9f-AwQ5_xviH7j6eYV1tf6k5v6H43iE1mJrQqQ_13YNP-Ztxmrs4Ym_NoZ9LVoihNeIz7KO-8GzBgLe15VlZUA-GWl6dKUQ-qlV1Lu2TVTQApGh0XR7SuY4x3KwneqCB1LgsW6hvVIJZ4nOBwI6sCiielzCGhF-Z7gi-I_di5MZfwmAn1tKM37BI8kB3YyMmTD2-miOwlhIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسخل‌بودن که شاخ و دم نداره
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/99041" target="_blank">📅 15:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99040">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=G2SfwAHYTFAMyqnAoh12vxEuizAn4CFt9tectAxH8i9V0T0FUiqANZ6yUDK8t_856BJLy70kqanXLzYky2zyhk1lZNN-JbKQMsyTv36t1AxbV_nLoFwYA0ujG-F7ngjpVqwK5X38hlmBNjil81ccOsy26dntnvBmbKgacY93bZunEc_94-2-sz1b1-KWh7GZK89syaVZaj4zSOlc7etSxx9ldzQbKPTZamW8D5a4bOACvx8vJn83hqa0vqcMo0aAhIl76Jowt-jqxe2X-j1aQso60gE-5j0x_WVx6qV40KTSUWg033kQtWZ4143n67gYbxRn_D22JzDIruAuO6ou3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=G2SfwAHYTFAMyqnAoh12vxEuizAn4CFt9tectAxH8i9V0T0FUiqANZ6yUDK8t_856BJLy70kqanXLzYky2zyhk1lZNN-JbKQMsyTv36t1AxbV_nLoFwYA0ujG-F7ngjpVqwK5X38hlmBNjil81ccOsy26dntnvBmbKgacY93bZunEc_94-2-sz1b1-KWh7GZK89syaVZaj4zSOlc7etSxx9ldzQbKPTZamW8D5a4bOACvx8vJn83hqa0vqcMo0aAhIl76Jowt-jqxe2X-j1aQso60gE-5j0x_WVx6qV40KTSUWg033kQtWZ4143n67gYbxRn_D22JzDIruAuO6ou3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
ارزش دانلود 1000000000000
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99040" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99039">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp5AyFZkrpe6IwoTsiQQdap9i2t9AHoSrCXWw3h4PlKZqfFek2qbbBymIGYZ_IFya-jkrdp3Df3TWJGiXcPIW-tVAtGsxobkLlLXEv-HykqZhF3wkUsKv_wu43M3sAlfO5vHnjbK8ztXYsOT3xHensDVAzJO__Yej86kSdjmlzZD875RnnhpjLLM-KklVOS2c-9TQIDNHhb7xKFS8km2RsdAAEwpAC1SClgXk-Mc4WnNtFSSpEfZxIHA4nx3Ds4DRo8C30GP6TY37qKJrfmLcvKlH2IDAlfUFYIPnSFXo5hWfOsqGbqNszKNEWi2pmaGlaY95AyQ42ZDjT9nMpW_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین پاس گل تا اینجای‌ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/99039" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99038">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=NRBGqDreKHNwGqX_lh17YbGJhqLIPiZAMLQ10okRjnyKHrfu9QsEVtL5Csdh6u1vZ2POzSbInyNGbcHOib0cxFQ_-uUl2IU6vZ23wFwfBues9ruMEaSK9a-leHPgX6t4zkR_6EOGrOPljj99_KhLCR4mltAAlmxBOA2rCVM9chCjIuUbgkzbatf67oCqbbMyNOo2de0wHcw75mcGVOtTDAjtqKpW5Hd0xEKCnbT45tAk5XxI4BPZOCHJyxtVh3_qPnFDuM_V-g-vQjUZAMvgMn4yeuojnQ1rWS7HSsuIIGmtNZHSXyFETnu5XnNlPI_Oy7BVps3nk69ETOBgn0vg1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=NRBGqDreKHNwGqX_lh17YbGJhqLIPiZAMLQ10okRjnyKHrfu9QsEVtL5Csdh6u1vZ2POzSbInyNGbcHOib0cxFQ_-uUl2IU6vZ23wFwfBues9ruMEaSK9a-leHPgX6t4zkR_6EOGrOPljj99_KhLCR4mltAAlmxBOA2rCVM9chCjIuUbgkzbatf67oCqbbMyNOo2de0wHcw75mcGVOtTDAjtqKpW5Hd0xEKCnbT45tAk5XxI4BPZOCHJyxtVh3_qPnFDuM_V-g-vQjUZAMvgMn4yeuojnQ1rWS7HSsuIIGmtNZHSXyFETnu5XnNlPI_Oy7BVps3nk69ETOBgn0vg1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدرو پورو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99038" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99037">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99037" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/99037" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99036">
<div class="tg-post-header">📌 پیام #7</div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99036" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99035">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👀
نظر دخترای آمریکایی راجب بازیکنان منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/99035" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVX7-DY_x7XgZp-qAIeZMfM7HIIuVmCwF9jAlenmjKtsoRYGJ6GIsEZZSL8oKxaDBiIAwwpVsKmbnvp3C9450Odm1H2mOGkXukypndFCFOmgMsgumfFmHVMh0uPDuAQXtGB4l0A360-9FzskQYHV6CdmLUNyuwsV8HKLaPRkxs6Q4ZgW3FE-JaffWRacc6H-EjjilbBXz0dS7akzxRENg4M8fbrK9m6csOeO1WApsTjYaWW_fhP-aoF0Y3mq20YRukwppOft9a5XsUr3_HrasGhPRNXunWsKgW_5ikv2hp32tFHxew1-3wj827DcPcuxPIuOpUEJFNltKfcryyatrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
تیم ملی کرواسی از جدایی زلاتکو دالیچ سرمربی این تیم پس از 9 سال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99034" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=JpMYfdxZXPaf3-_RO8OAMfdPRManjWSDbL9YrBXaqkstuTxnldROmVxvHFIGtI5dZKnG2InUxbEO5crQchphgMLZMPsCV7KEQTdSAe9BKOdFP2NIkI8to24qDRAXWKoV9MMVRyLO4zeDhaQapvAZ04V4PIpeyYDJ8MoAhu81zDZo13WLM6RfR9r2tmD_zeuwdV9ZEnWRWpZeZAOQHCmfDfN0WLsJY-iGb8sjjIzNiIKM3saEL7uFP333q_GOW5utTvt3jQ3vABHhd5dsEIxoMIibxzsIEOxLnrTU2KhwCVFZjkqeWpwG58DoYuWwTB6oUQV3F76x7__XnygFe_9Uaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=JpMYfdxZXPaf3-_RO8OAMfdPRManjWSDbL9YrBXaqkstuTxnldROmVxvHFIGtI5dZKnG2InUxbEO5crQchphgMLZMPsCV7KEQTdSAe9BKOdFP2NIkI8to24qDRAXWKoV9MMVRyLO4zeDhaQapvAZ04V4PIpeyYDJ8MoAhu81zDZo13WLM6RfR9r2tmD_zeuwdV9ZEnWRWpZeZAOQHCmfDfN0WLsJY-iGb8sjjIzNiIKM3saEL7uFP333q_GOW5utTvt3jQ3vABHhd5dsEIxoMIibxzsIEOxLnrTU2KhwCVFZjkqeWpwG58DoYuWwTB6oUQV3F76x7__XnygFe_9Uaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تمجید لائوتارو مارتینز و خولیان آلوارز از مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99033" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYSQa2yTbE28DHEqFPHvLoMo5NwPeE4PFiHrJnsW57jHctS0OXxSjTXQ8YEsY_0CthFZOJkMcHn_UtccMlfHcAMjFFqvBgtJ2iK1QAfxR9_GavOFSPI-DznLWG2nnr08erk04vg1Bt4xTW2pa6KsrbVC5BSakGoG2iDpKg4auedU7MEPaTmYhqVS0jogHk-dzxqgH4o_wQNRRfaKjE9Cl2KNDARIre5zX5x6VUTIyeMzkE0Wuv07FU5OHG2xg-OKiwvcN-qwg7t0Fb7nzbSMdtgFe7NcY7tljgcVQHUWMyExCl9fP5opVKJ9xShorun6vaNYwA8FndUfX-A01v7QlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وضعیت قلبی برخی از طرفداران فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99032" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=lSfd6mWHqlJpFLAhu7eJ0827ZTB3qK4fO-IgQCzEUaYVFeQ8CtrCfHlxFatdzGIWuod2p2FDLw9xykl13XlqtRcaGDSf819endQIUW96jZbHMtCAHY9ztKTLX0yaCOGqPq_J7SQvaxBaB1Ld_L9VzbxTgkoX5C3NsZDPBOb9v3hic4O8ZRaookduhn2YFt9bCdPpg8v2DsvMzG5qBKhGaPlwf3Q2mSRVg6r2SG8-0oGoBPR2XAOJP-HuDfYZ-jbU_2J6S5WGZVo-XN_tCn-1WVxBOHP6qTE8Qiyw12wiZSg5YnDOUUQZN6ncLdM98H178JY1xSOTph5fx0uPH4RGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=lSfd6mWHqlJpFLAhu7eJ0827ZTB3qK4fO-IgQCzEUaYVFeQ8CtrCfHlxFatdzGIWuod2p2FDLw9xykl13XlqtRcaGDSf819endQIUW96jZbHMtCAHY9ztKTLX0yaCOGqPq_J7SQvaxBaB1Ld_L9VzbxTgkoX5C3NsZDPBOb9v3hic4O8ZRaookduhn2YFt9bCdPpg8v2DsvMzG5qBKhGaPlwf3Q2mSRVg6r2SG8-0oGoBPR2XAOJP-HuDfYZ-jbU_2J6S5WGZVo-XN_tCn-1WVxBOHP6qTE8Qiyw12wiZSg5YnDOUUQZN6ncLdM98H178JY1xSOTph5fx0uPH4RGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ ابوالفضل جلالی بعد از مذاکره با مدیران پرسپولیس، بدون صحبت با خبرنگاران، محل جلسه را ترک کرد. گفته می‌شود کار او با پرسپولیس را باید تمام‌شده دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/99031" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD7K19YRl_by4DNOTIf2I4WpBpD7k4yzrXHlWhTy3UTIb_APTkoupDdT7UEQq4LrQzB4E3C3cyKabD2kkCtSHycNTPJRm-vgh_v5Xu4_Lyquh-OfH_10ukhTbNI0vcEDhh_42lTm1h3EAAqgXqN_wZlZkxpOIRZwwnexzXX9APYHPBU9JWZmVjfdDHt6qJdysjcSNh-75yv5cqPhBxtB-GmE2FCoRxXN_mXDPz8qWSl_EclO9ZWW_UznCY4ylbywkKOuPJy0nw43w80c-sCdeak5_aE1NKczeTpADHYe8mihRynoqKCDBOZnBsGlQXsKKKlx4U-o0tKJKJ-raxI2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇦🇷
#فوووووری
؛ بدلیل توهین‌های نژادپرستانه هواداران آرژانتین به اسپید، فیفا قصد داره فدراسیون فوتبال این کشور رو جریمه سنگینی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/99030" target="_blank">📅 13:48 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
