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
<img src="https://cdn4.telesco.pe/file/afKLmoGvCp62j475DquBz5TFPkWJ3Ds62RT2JbG7yiCwIjyBGedNI4i2lh1-Ne5nNUvDYXHaUgFrCg-LE11o6X4hSzA32PABk9XG16L_UK0NlXWv7z2WniEpZqGUUv4is-EOfchDBmt46PgpBNXknUmNeyRhv_tNGQiwq3i1jlSVl8f0uAqjogfzje299xUj7Yk7YVOg1EpiENK_fEeQUOjUhnyl3oFscU41Nbe1jQzqlty4tBj_CTKKuaSEyX7YpPBKTljDf4IeCY8CnDTEtxS52sSjNl-bfQfc-2SniAnY2SRzjlnNe9hpy1WwBaSJTm00daFGuqEm7eSO3K-exA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 112K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-71289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
دقایقی قبل صدای سه انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/71289" target="_blank">📅 17:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=kyUxWn3bu9zBfQymDU3PrSHCLluMSRtSaE6dwbsCq18ZZZRQRstKzGbHpIazYFTaCJBi0hKaSEJVqTJkGdpnXZBg6oJcZ1iBMra_usGTLfYtlRYz9rekZl0pyuNwIozHYk1KhPXvoZkxXCyCImnR-5-FrnOvt6KXIgFtjPMFqZI07O2ASytiZsKlLabcIKyu21wHC0KELC-AZuxRoIvHX4yTKVxZ9iFQ1TlLdnpjzxFnoeFJJmspsJYuOSVqDo0wzLv1Gv5oMXR_PECnXrSpzcvsVO-C4u0a3hfFqAnXDyQvjb3ous0oWaqfkF0wsAbbqDsaY64f9YN_JwMDyT5sxXu7sJaOkZQJUZNBRDUBAL7DHLXq1MBB-pqClmNygPF4zkHqS6f6YAMJzt2AkV3Mel79OpnpdaDL8ejlpMfQ8rLJyHCdaRWUKcbWf4-j-IHw-xcA6T3rC0LCNZPsp3pUYgM1pDRSfpSiknfmfDCZISAYOn3mVCC14A_VBrq9WoLk7eordrRkZ4WRlsSuoHmcdxJlM2G75rr1-g5Koi7TAlkAbbbJuN29vGSFrWa_gSPtVmvz_MQxThVSu9uX4vNSkIV0msYhBHMRv3rnY9Lt1n9FSSQtvQjTyfaZLMWf9_f3qQEyj2sbIOXgC7CFrOVZ5F3cPJ1jKYb7tfUo3o9bNAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b881718fc3.mp4?token=kyUxWn3bu9zBfQymDU3PrSHCLluMSRtSaE6dwbsCq18ZZZRQRstKzGbHpIazYFTaCJBi0hKaSEJVqTJkGdpnXZBg6oJcZ1iBMra_usGTLfYtlRYz9rekZl0pyuNwIozHYk1KhPXvoZkxXCyCImnR-5-FrnOvt6KXIgFtjPMFqZI07O2ASytiZsKlLabcIKyu21wHC0KELC-AZuxRoIvHX4yTKVxZ9iFQ1TlLdnpjzxFnoeFJJmspsJYuOSVqDo0wzLv1Gv5oMXR_PECnXrSpzcvsVO-C4u0a3hfFqAnXDyQvjb3ous0oWaqfkF0wsAbbqDsaY64f9YN_JwMDyT5sxXu7sJaOkZQJUZNBRDUBAL7DHLXq1MBB-pqClmNygPF4zkHqS6f6YAMJzt2AkV3Mel79OpnpdaDL8ejlpMfQ8rLJyHCdaRWUKcbWf4-j-IHw-xcA6T3rC0LCNZPsp3pUYgM1pDRSfpSiknfmfDCZISAYOn3mVCC14A_VBrq9WoLk7eordrRkZ4WRlsSuoHmcdxJlM2G75rr1-g5Koi7TAlkAbbbJuN29vGSFrWa_gSPtVmvz_MQxThVSu9uX4vNSkIV0msYhBHMRv3rnY9Lt1n9FSSQtvQjTyfaZLMWf9_f3qQEyj2sbIOXgC7CFrOVZ5F3cPJ1jKYb7tfUo3o9bNAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇬🇧
⭕️
#فوری
؛اد میلیبند، وزیر امور خارجه بریتانیا:
ایران هرگز نباید به سلاح هسته‌ای دست یابد؛
از این رو، ما نیز در این هفته همگام با متحدانمان اقدام به ارجاع پرونده ایران به شورای امنیت سازمان ملل متحد به دلیل نقض تعهدات هسته‌ای‌اش می‌کنیم.
همچنین امروز می‌توانم اعلام کنم که ما در هماهنگی با اتحادیه اروپا و ایالات متحده، تحریم‌های اقتصادی عمده‌ای را علیه ایران مجدداً اعمال خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/news_hut/71288" target="_blank">📅 17:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71283">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/645274372a.mp4?token=aziZXFAFk0i3BVOjJwagPK5YEhmsTngTwQyE0bRQ9tSQfQT0iD83psfs8Mt2sMYnZrWKjigYhahEMlJmJb57ptSWc5CuoQ1zcBYdykoCegSiSGaGPbXegHCk6U32_2zMPF_wKc6pJv1YBa464BWZbFKY1k18Xc_K9PRb_aURKpUbxMEaL0DxGdMyX2uVW3qqgqSJmdzsV2vmDZUfWe6lWTzO2DU6WHEYTBJ3Zls9SvOZBvm0xv_-0n1rqwqt0e3OWk5Peb57vxt8szZBg644Wv12HOaJn7pVN53N-B9L6fybalQpi2fZQyItxsQ9JHDyasdbpdejib4WhDRz3YBCrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/645274372a.mp4?token=aziZXFAFk0i3BVOjJwagPK5YEhmsTngTwQyE0bRQ9tSQfQT0iD83psfs8Mt2sMYnZrWKjigYhahEMlJmJb57ptSWc5CuoQ1zcBYdykoCegSiSGaGPbXegHCk6U32_2zMPF_wKc6pJv1YBa464BWZbFKY1k18Xc_K9PRb_aURKpUbxMEaL0DxGdMyX2uVW3qqgqSJmdzsV2vmDZUfWe6lWTzO2DU6WHEYTBJ3Zls9SvOZBvm0xv_-0n1rqwqt0e3OWk5Peb57vxt8szZBg644Wv12HOaJn7pVN53N-B9L6fybalQpi2fZQyItxsQ9JHDyasdbpdejib4WhDRz3YBCrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
نیروهای «شورای رهبری ریاست‌جمهوری» (PLC) تحت حمایت عربستان سعودی به همراه جنگجویان قبایلی، شهر «الیتمه» در استان الجوف را از کنترل حوثی‌ها (انصارالله) بازپس گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/news_hut/71283" target="_blank">📅 16:47 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71282">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⏺
فارس:
یک پهپاد MQ-1 بر فراز منطقه راهبردی تنگه هرمز با هوشیاری نیروهای پدافند هوایی جنوب شرق ارتش جمهوری اسلامی ایران شناسایی شد و هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/news_hut/71282" target="_blank">📅 16:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71281">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de453ade.mp4?token=FXCpnKYIbrKul9FGj6_IekpP-3dfZUbqCznzWYHIbRMWALVHVjlw9V5A_jBIhYEUanaeVjKXrUtKExUuWRku5f9fXPYocKXziSEMCrxvdFSIHArq1eUeNzBCH1_bHeXGfktLfH85jVjen8MjBbZpUnW6t0-AZWDD8a2S2Zwpd5P2iy8YCg8aJ_7-XNSY-2mws9ugS4yiQJ7NT9r6sqvsh34E5rvNgSblPKNFHS4GS4GVdLqwv3QiELnqyDnkx_9YoYzTrCt7-SFTSLDKsLcPZS5vZEHy5EgZjHk7DcrAD_5HFvhXxEmE82a5BMsH_bVgusB00Qsju-SKcCvsF6gJSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de453ade.mp4?token=FXCpnKYIbrKul9FGj6_IekpP-3dfZUbqCznzWYHIbRMWALVHVjlw9V5A_jBIhYEUanaeVjKXrUtKExUuWRku5f9fXPYocKXziSEMCrxvdFSIHArq1eUeNzBCH1_bHeXGfktLfH85jVjen8MjBbZpUnW6t0-AZWDD8a2S2Zwpd5P2iy8YCg8aJ_7-XNSY-2mws9ugS4yiQJ7NT9r6sqvsh34E5rvNgSblPKNFHS4GS4GVdLqwv3QiELnqyDnkx_9YoYzTrCt7-SFTSLDKsLcPZS5vZEHy5EgZjHk7DcrAD_5HFvhXxEmE82a5BMsH_bVgusB00Qsju-SKcCvsF6gJSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنازه و تابوت ترامپ و نتانیاهو زیر پای طرفداران حکومت برای بار هزارم له شد
@News_Hut</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/news_hut/71281" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71280">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=MoGnbcCf3nUZH0-LF5L2ZVJetYMwTxuMW3ywZFj1ebQ0X3vOLiXfOGDm__C_CYK16y9Wx87nLZyWUJG0Kku84BXMHQ8UAfigUKmJL5I7FHwGUo8KsVo0hZuozxUQHtRQLaTMil1gGAuDgsVtwCHs16SFNDOsDtYsURB8IsKy59EANv5Mz9xsbC-abVTT4tqdXCjWX9gmwMAWvghR8sRX2hUp0T9XIA4RcubCCxmvwGAuqKxm_UAXlgQ5UTHAJMsnJOfQUEErkXNBb5UGa7Rn9G-FaiGs4fGuJxvhKXEgJ6ZQcca371mlDk5qNLCh8AcqghgugJ7sGZpPFUH8O4wt_TaMN8v2tZNj_KBQzBMwb0K58dGnCLFnSb3e6gNMe6yeKLwL8kojJchlUcFz0uiBuoeAVy-rOLvqjRUv1ACHnFMUgxa80UOoGemhhjY373PGVuw8HL39wkRy4LVmmdbk7lFxAh6Aenm4_hQanl7dLoIaFTq1j4i6MFqgq3jQyDHdDkbDbi0Qd-fxoTCLhMur6poO0rghoCg3X4DyMqjafEpLOTcR8ANQStiT_ic0cVbHoVRy7GARs6umedWa7jsj3mb8aMyuvQIORrcEPfo0WLV6inILuoLM1kXF6xdGGD97VQSrFf6kLYH9PuwLKm2ueEyLSM3WHuC3eqDJyxV-Jc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a724fc44e.mp4?token=MoGnbcCf3nUZH0-LF5L2ZVJetYMwTxuMW3ywZFj1ebQ0X3vOLiXfOGDm__C_CYK16y9Wx87nLZyWUJG0Kku84BXMHQ8UAfigUKmJL5I7FHwGUo8KsVo0hZuozxUQHtRQLaTMil1gGAuDgsVtwCHs16SFNDOsDtYsURB8IsKy59EANv5Mz9xsbC-abVTT4tqdXCjWX9gmwMAWvghR8sRX2hUp0T9XIA4RcubCCxmvwGAuqKxm_UAXlgQ5UTHAJMsnJOfQUEErkXNBb5UGa7Rn9G-FaiGs4fGuJxvhKXEgJ6ZQcca371mlDk5qNLCh8AcqghgugJ7sGZpPFUH8O4wt_TaMN8v2tZNj_KBQzBMwb0K58dGnCLFnSb3e6gNMe6yeKLwL8kojJchlUcFz0uiBuoeAVy-rOLvqjRUv1ACHnFMUgxa80UOoGemhhjY373PGVuw8HL39wkRy4LVmmdbk7lFxAh6Aenm4_hQanl7dLoIaFTq1j4i6MFqgq3jQyDHdDkbDbi0Qd-fxoTCLhMur6poO0rghoCg3X4DyMqjafEpLOTcR8ANQStiT_ic0cVbHoVRy7GARs6umedWa7jsj3mb8aMyuvQIORrcEPfo0WLV6inILuoLM1kXF6xdGGD97VQSrFf6kLYH9PuwLKm2ueEyLSM3WHuC3eqDJyxV-Jc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چنتا دختر با کیسه زباله خودشونو شبیه لاکپشت های نینجا میکنن میرن تو خیابون...
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/71280" target="_blank">📅 16:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71279">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=rpco5qFqlW1O2EjGXOKTdS1ccOksD7nCJ9SyZDu_F3LDRII__6lKzK7z_Y_J0WH_lchqVsEiYHBhKr0F5pWiJsWlFA0OHE0az0eq_9WsnGE11OT2_Gqk9XCq3r6Wby22uV5OyqdArEHyhBDtTUTHZgzo44NufQCect0wrgtm_ThZ0QUQr0FwXOGS19tJNo_T85VJVdLSlzNKAiWIWX2Iu00LNG9u_qeBJdNtKP-m18CsDLI0qDfxLzhx5Kmur2nehCLJL4NUdk6vMsy22W71HtjBtY_iMPGOmC31uEp38MwCzwhW5QjznG97XFAkj0GrW4f6kFKZJE-ZD1_MihcT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2ae4bae8.mp4?token=rpco5qFqlW1O2EjGXOKTdS1ccOksD7nCJ9SyZDu_F3LDRII__6lKzK7z_Y_J0WH_lchqVsEiYHBhKr0F5pWiJsWlFA0OHE0az0eq_9WsnGE11OT2_Gqk9XCq3r6Wby22uV5OyqdArEHyhBDtTUTHZgzo44NufQCect0wrgtm_ThZ0QUQr0FwXOGS19tJNo_T85VJVdLSlzNKAiWIWX2Iu00LNG9u_qeBJdNtKP-m18CsDLI0qDfxLzhx5Kmur2nehCLJL4NUdk6vMsy22W71HtjBtY_iMPGOmC31uEp38MwCzwhW5QjznG97XFAkj0GrW4f6kFKZJE-ZD1_MihcT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
آتش‌سوزی در تاسیسات آرامکو عربستان سعودی در پی حملات حوثی های یمن
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71279" target="_blank">📅 15:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71278">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=Hb40ISf88lZOzLtN-9JPRGzOj16AZO-PjeQhH7LGi2nZx0LZJ15IST5sSnPC0YVGWqxgKv2j6ljVH0l7j2fwdtcXZ3h5NLCGgfT2rJyKOS-BhbSViRyE9eiso2c9daDuKhTxYsExY2aJ0egE6kSqsTbZEOxMZ1NaNbPfNrnQj9s9KOBGTy4YIlQrtRjUlsFXtn44EyiWTlEoApWYocJcSW6LnrYLPjpeRAm8lFzrBNlgklIU5rfhff4IJWY-4zp-oUPmGQZABlWzls4mkSY8lUnkFazpWJkO6pu6EN8BL9z5a5P6PnJZ2XxN-r1i1aS8QYIUOoDuEJF-DoF7PvBA3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef148c5074.mp4?token=Hb40ISf88lZOzLtN-9JPRGzOj16AZO-PjeQhH7LGi2nZx0LZJ15IST5sSnPC0YVGWqxgKv2j6ljVH0l7j2fwdtcXZ3h5NLCGgfT2rJyKOS-BhbSViRyE9eiso2c9daDuKhTxYsExY2aJ0egE6kSqsTbZEOxMZ1NaNbPfNrnQj9s9KOBGTy4YIlQrtRjUlsFXtn44EyiWTlEoApWYocJcSW6LnrYLPjpeRAm8lFzrBNlgklIU5rfhff4IJWY-4zp-oUPmGQZABlWzls4mkSY8lUnkFazpWJkO6pu6EN8BL9z5a5P6PnJZ2XxN-r1i1aS8QYIUOoDuEJF-DoF7PvBA3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در سمنان برای دومین شب پیاپی میان مردم و دانشجویان عراقی وابسته به حشدالشعبی درگیری شد.
این درگیری روبه‌روی خوابگاه عراقی‌ها در باغ‌فردوس اتفاق افتاد.
ماجرا مربوط به متلک‌پرانی و مزاحمت آنها برای زنان و دختران است که بارها اتفاق افتاده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71278" target="_blank">📅 15:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71277">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FBMVO__gqV6r19mj_4svdlJiwjNnmmDD8CCdHjICh33Mu7sWLorEm1LxvkEmbB2aIcof5TM-Y5pL-CXZdT4OoAJV1sPsWViwiQSXYI1fjiu80Grbv1A0H5Yw6D5Bkb-l138vkOC_tO6etIv3xNUo-fPyruSYOXFEGr19cW_a-5Z8meWIylpJMsMPBI3Kb_FYkpEmxWfKETPxneY42SSBe8sXdg0WdDh3sjH77cDSQdd89I80RK5m7W9QTvvROPeh4yO7fO-lJixk8TMqdZPPegXfNV_-DSAOPBU13yosZN4L6iv6P6jG14sZoilAQWnmVgWisyfvvtXHNg9U12AP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
امروز ۱۷ شهریور، تولد مجتبی خامنه‌ایه و ۵۷ ساله شد.
اگه زنده ای شمع هارو فوت کن
.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71277" target="_blank">📅 14:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71276">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=BKKkosu6eQtuBHbwdIARIlZyfRRhHO3CFPbUZoVw8FT8U94d-zOblR18x85W7-lkebt73A5JJ99YH3-zP-8WgfYpeSsYIDbV2Ivu8xoMkT3o-hWkrDjAkDuTmAyul9YHo33Awyv5WM8UuGIdaE09sac01T16NswmIMwaTNvtAiftHIQkSJw8VSIUVAllDbz8TQAUCrIzdG1WSZqc73d64oY78VRSx5RldInGTiFf8C0pr3ZMtFgwtXUit7__C0py6qd8I09gwPxqKpYElZEbQYUx2abKwwWeO9ksXOL7Ks1OBiUrlD_adkV3wF__JhFXlADt0lYCTSNF9AtEOaUBWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed3b8e81d9.mp4?token=BKKkosu6eQtuBHbwdIARIlZyfRRhHO3CFPbUZoVw8FT8U94d-zOblR18x85W7-lkebt73A5JJ99YH3-zP-8WgfYpeSsYIDbV2Ivu8xoMkT3o-hWkrDjAkDuTmAyul9YHo33Awyv5WM8UuGIdaE09sac01T16NswmIMwaTNvtAiftHIQkSJw8VSIUVAllDbz8TQAUCrIzdG1WSZqc73d64oY78VRSx5RldInGTiFf8C0pr3ZMtFgwtXUit7__C0py6qd8I09gwPxqKpYElZEbQYUx2abKwwWeO9ksXOL7Ks1OBiUrlD_adkV3wF__JhFXlADt0lYCTSNF9AtEOaUBWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
شب گذشته در سمنان، به افزایش قیمت بنزین اعتراض شد.
این اعتراض در پی تصمیم جمهوری اسلامی برای دو برابر کردن قیمت بنزین خارج از سهمیه یارانه‌ای از روز سه‌شنبه صورت گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/71276" target="_blank">📅 13:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71275">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo1PZwMl6sciPATxoUl-K73zx6kzp1tWgKJRlCoCIGc2fv7kxeJQIAx3fOUd5FjQwHjKpwqEjc1LCoVzX6ZnjOVbfPYcnIYlq1gpTwNSk-KNK4Rf2wxcXw9Y4YQbF3gGEBZ93WDXiPnBFj08Uo9RU36CfEn8fyDOhKPndelKDOx-iLy76z8gM64Wp0W2vaBqpv8CZR8s0j46mt_YN7EQ7GulOsz-cuYGXooa9Awz9Op9p_YVigFEBsg3dCfMIrnPGmFywQfpw8pPFcknxk2vG7S0acsx5itqpS1W9nnFvdhG_MIrHKwHS3U3M8J8pKFq7DbJieysMVKbLf3CghVYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود پزشکیان:
جمهوری اسلامی ایران همواره با جنگ مخالف بوده و حفظ منافع مردم و امنیت منطقه را در پرهیز از آتش افروزی دانسته است.
اما چنانکه تا امروز در برابر تجاوز، دلیرانه به دفاع برخاسته است این مقاومت را تا پشیمانی کامل متجاوزان با قوت ادامه خواهد داد و پاسدار حقوق ملت بزرگ ایران خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71275" target="_blank">📅 13:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LbhQKvLJt4bUL2hV_qdnlYTMPBqbs6jOYsfVlf3yO4LiDk0-3knNMYhaMvH9zuKcsm_HQ1FkFCNc3Ksmu8I-9EV0pJ6bR1ih56z1kdqQNW8cfSRQJkpR8nSgBn0fNR51BH8WbFoYRueVuLwoPI_tkeMIDx2pv9WFp5U7NemKaWutIk2SRG1WJzx_RQzW5slsfVRrR-sn5PrGRJAs4E0WE17wj_u_3nMq8Kv-RpiwFZ7XDF8jSnUecjLDBNP6X0jgCCI7fqTlBdcxJrjbWboX83c35Ghu3eeXt8huBTxdvI7gJ5ayz2av9oLw8tFdob-PISAkGYReAHQWvsfpBfyyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8833895957.mp4?token=Cwqq6tYAGGludgiFuzKZWM02pNhmkNyvEe0YY6BGloxWmaiELuxsGEsHVM-kt4FULghQsitc2y6ByEbItvLRcJKSrC-7nkgTm4_9IgpmxJhKiCCYx25HWKdsMNrhHhhMr4LiQ8SWir22Jp0QcEl5eN_psufU3QF3Weeef9P-fF4dBMfnZVkwmzBIF7hjH2Rbsq3hs2PImik5Zn4d0YrZsQK1QOnqeIJmKlY8VYULNkfUjoKWXyVDd4G3RV2qk_rcl4Siy4MfYOdSyG98p3Ch-8nVlXX5BQd8lLHjYdPRiu8KYpHDfk2LHDc9jt1rDIDFSkcRRDYtSrR5-xUOEfqp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8833895957.mp4?token=Cwqq6tYAGGludgiFuzKZWM02pNhmkNyvEe0YY6BGloxWmaiELuxsGEsHVM-kt4FULghQsitc2y6ByEbItvLRcJKSrC-7nkgTm4_9IgpmxJhKiCCYx25HWKdsMNrhHhhMr4LiQ8SWir22Jp0QcEl5eN_psufU3QF3Weeef9P-fF4dBMfnZVkwmzBIF7hjH2Rbsq3hs2PImik5Zn4d0YrZsQK1QOnqeIJmKlY8VYULNkfUjoKWXyVDd4G3RV2qk_rcl4Siy4MfYOdSyG98p3Ch-8nVlXX5BQd8lLHjYdPRiu8KYpHDfk2LHDc9jt1rDIDFSkcRRDYtSrR5-xUOEfqp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌧
بارش شدید باران دیشب در رشت که منجر به وقوع سیل شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71272" target="_blank">📅 12:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bpx8DXPSQWHpgP-SRMh9Rj6wc5foCq5yT6x4uYrSVnIuOvYFsqoUAc020kF_26iWckTFK_Wxl1BCrO7Xo3KsloRDZHWPFV1ucEbFtq4cduLZF12Pk7zYWNSbL0spb3KEqhV2dJEDO-fN3y8KgQh8uNPN1WToAYtu0L0Pa3aQ7L650r-P7UsqNa-8Mq5UzLopEMhcBJexyuLVh9JJb6iKVKJWmIjilI16NHCZOyQydpHpHCCbASsUXaWm5jbta81k2VoW7wJXIhullC-cIe1UjJF-zS0z__EChOh8J3pZqFpybKOqdAiHMUo7nXFVfhfdnCUbBbYhSRxxGbt9etx5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=r-lRlHreGCYQasMQjkcgsrRNENaiGw5LDdwW8zBY_RMLVyU34UoweBUK9gfyBuAvIopyIf48zkax2MXwR4RQvs8VuqeDvhDbU5rx337LFVw98Okal0RxIxVyxmQ2N8HtY3w9sGPVspbpXHJFmuifmSt-opZwNnUlI-nR9xqIfurpZpbpxqjd2JUtqkR-sCgSryhySBBPr9R6455cCpf9kAy_P8Kk_9a6ufRhXcwiIolRoWOzrZerqqs4J5fkfvL9rXYkmo52wtQIao8Eg8TYOCIl5dSfPd-4jd-nKe0dTirInTbjLTjb5JZhqSIDZ8QQ2-7QE1kuocA9CvyDn40wwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bd51248f.mp4?token=r-lRlHreGCYQasMQjkcgsrRNENaiGw5LDdwW8zBY_RMLVyU34UoweBUK9gfyBuAvIopyIf48zkax2MXwR4RQvs8VuqeDvhDbU5rx337LFVw98Okal0RxIxVyxmQ2N8HtY3w9sGPVspbpXHJFmuifmSt-opZwNnUlI-nR9xqIfurpZpbpxqjd2JUtqkR-sCgSryhySBBPr9R6455cCpf9kAy_P8Kk_9a6ufRhXcwiIolRoWOzrZerqqs4J5fkfvL9rXYkmo52wtQIao8Eg8TYOCIl5dSfPd-4jd-nKe0dTirInTbjLTjb5JZhqSIDZ8QQ2-7QE1kuocA9CvyDn40wwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپاد اوکراینی به یک ساختمان مسکونی در پرم، روسیه، تقریباً در ۱۶۰۰ کیلومتری قلمرو تحت کنترل اوکراین برخورد کرد و یک نفر را کشت و چهار نفر را زخمی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/71270" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71269">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71269" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzwhRA9rA8lO50hRbQmjsWpG0kQdHlr42tUi9JbKbM1eRVmu4xnD4dLv0XllumgfK65MwjgIX7tUmjuXJjBM_qtcFWUtfisfaqhb3VUeuLsko02oNyXNDzbqAJTl7-zMYsB-5JQZzgmEppJmcaBmMz3JQeF9imwsPuobnZsYrUETFJfwSfNB8RJ1FV7BrKGKjFWE-kysEtQikFHFm4GYYjiiHE62apvb9re0t-I-TX0Am2nwUug6SK26892q4meby3xsPFAvqd5OfXcNjZG7w0f_j4bAPz2EMq512NuHo7dS1OTyRSZIqodyt5tnFONC1V2rjGonrhC8-gu9O-rFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شبِ بزرگ فوتبال اروپا فرا رسید!
⚽️
رئال مادرید
🆚
اینتر
⚽️
🎯
این نبرد حساس
چمپیونزلیگ
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📊
نگاهی به آمار ۲ تیم در ۵ تقابل اخیر:
⚽️
رئال مادرید: ۵ بازی ۵ برد و ۱۱ گل زده
⚽️
اینتر: ۵ بازی ۵ شکست و ۲ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/71268" target="_blank">📅 12:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=htCAcAera6tCxLv7SMi3KoSbB8HIscP7NZb0TDVRULP_Qh4CqXWrMRCokV4uHLDomGIi3GvO2yCH0C36u33nFNIuU4YQ9bam-C5nhttivrmRgK1TmMfKmvmnpybdlZb8dpGWNr-0UZFD61FVSQGqcC720l19CWblQ9-ERiWiS37asBQfgnJOC8uMckft5FolQPABKxSkZqdKfU2l4WWeXAp38k8wLeDR6xadRVUSHdUsjh1SZN42fDp3KSX7POlBwKvXtSsh_UVTclyaXowQAzx5CtQSD_Srdk-DtZVpZSGCy_cQ1Cx_G_ROJpoHDAl8YfTh8HNuuIjI14AMm6qT0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/193f66d1ff.mp4?token=htCAcAera6tCxLv7SMi3KoSbB8HIscP7NZb0TDVRULP_Qh4CqXWrMRCokV4uHLDomGIi3GvO2yCH0C36u33nFNIuU4YQ9bam-C5nhttivrmRgK1TmMfKmvmnpybdlZb8dpGWNr-0UZFD61FVSQGqcC720l19CWblQ9-ERiWiS37asBQfgnJOC8uMckft5FolQPABKxSkZqdKfU2l4WWeXAp38k8wLeDR6xadRVUSHdUsjh1SZN42fDp3KSX7POlBwKvXtSsh_UVTclyaXowQAzx5CtQSD_Srdk-DtZVpZSGCy_cQ1Cx_G_ROJpoHDAl8YfTh8HNuuIjI14AMm6qT0DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
حساب کاخ سفید در پلتفرم ایکس:
در روشن‌ترین روز و تاریک‌ترین شب، هیچ شرارتی از نگاه من در امان نخواهد ماند.
آن‌هایی که قدرت شر را می‌پرستند
از توان من برحذر باشند..نور فانوس سبز!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/71267" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71265">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=lLcPkYsv1O0bPiprKpFDcLJUUF37BpDzC6Rd26QnJ94T-gekCKRylVWo5nJYwhaeXy9MdppyxjzM0Ua5ts8KvOFob6yxZdIIRgqM_81o3hNZkQ1MfdGEz6NkgTL1CkbjWWTe1O1XioWSw3oWypmVl2UgCF9jgISm9HXlq0EFplSctYw9_2B7iGo1WQxnbicA9ONlF0oXIpQg34x12RxXOfm1KUxRtyFcdi1Cm1unrl_iw8k2Uxt6iWIraNfyjUmlILBEDKA56Eu1rGPYDffQaK-usflMcbC2vTM9S3DMKqmplgJCaYcvt5W9bOCNRLhm81XT6fJZ_MrT4YKLxQPtQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658f8cd399.mp4?token=lLcPkYsv1O0bPiprKpFDcLJUUF37BpDzC6Rd26QnJ94T-gekCKRylVWo5nJYwhaeXy9MdppyxjzM0Ua5ts8KvOFob6yxZdIIRgqM_81o3hNZkQ1MfdGEz6NkgTL1CkbjWWTe1O1XioWSw3oWypmVl2UgCF9jgISm9HXlq0EFplSctYw9_2B7iGo1WQxnbicA9ONlF0oXIpQg34x12RxXOfm1KUxRtyFcdi1Cm1unrl_iw8k2Uxt6iWIraNfyjUmlILBEDKA56Eu1rGPYDffQaK-usflMcbC2vTM9S3DMKqmplgJCaYcvt5W9bOCNRLhm81XT6fJZ_MrT4YKLxQPtQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یکی‌ از مراسم های تولد در بالاشهر تهران
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71265" target="_blank">📅 11:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71264">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=O8Hq1R1vYSaZpSYOe986qrMlAZIPeW6NDzgTLQlLifhhOWLvApbcTBa3p95f7xngtwba9mMPrVhce-l2_WEfh2r2bU2FivJKnay4hKJp2WxnvPJeLf1fGl_Y9GKAfc2TFpfDugl4rMt2sqg2ax4Ocatz9wMyC1GxhFVP2OQARVhmthhphBfAiW3ibIfmTLqfxrqw1XcFoWu_9MSS9AWXkY_X7IwaAddYA0jGWAyBsZkdWm59vUw_kFO-dH7tapOdU3blUOZcsKp6jmfH5PV7cd7FlUtlZZJhHtu-BMFeMRHOSaGxkY2Kmg5H3zk9kuDQX9W_LSvplGcpX6v_dB6LkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0de73320.mp4?token=O8Hq1R1vYSaZpSYOe986qrMlAZIPeW6NDzgTLQlLifhhOWLvApbcTBa3p95f7xngtwba9mMPrVhce-l2_WEfh2r2bU2FivJKnay4hKJp2WxnvPJeLf1fGl_Y9GKAfc2TFpfDugl4rMt2sqg2ax4Ocatz9wMyC1GxhFVP2OQARVhmthhphBfAiW3ibIfmTLqfxrqw1XcFoWu_9MSS9AWXkY_X7IwaAddYA0jGWAyBsZkdWm59vUw_kFO-dH7tapOdU3blUOZcsKp6jmfH5PV7cd7FlUtlZZJhHtu-BMFeMRHOSaGxkY2Kmg5H3zk9kuDQX9W_LSvplGcpX6v_dB6LkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یک پهپاد اوکراینی در طول شب، بمب‌افکن تاکتیکی سو-۲۴ روسیه را در پایگاه هوایی ساکی در کریمه با موفقیت هدف قرار داد
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71264" target="_blank">📅 11:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71263">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=vRGvnHENY1KuFwpc-6s9WT6QovUNvG5fd1HqSeAt1-egLaUYjWTJ4jpCkrMyi2wB3Ne6YensTS5I04f9yNzaA4_JYtiwfE1W6Yh6ajYD5C1QSjuGk1AdtYchkG0Wi9bpnsuZszNOZMoMVzXx_cVpF2iHIx1lpNeB42zfWXrGuh1LOzvimVBpWVK0tODYmUmKg5bXzg1MihZ8p3e_vcoIHqs7ueQtocOR45MhcZ4ak_n-fXa8FlOMeDNvM006sgAIjGHbSTDq2SAAXThYVIipD-3P-C-1iJRR2_-oKsioq22cCJ7u-2T_4n8-mBkaFdpKVwNkhcI81lUbmJ9zjIhxgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/233fc1eb07.mp4?token=vRGvnHENY1KuFwpc-6s9WT6QovUNvG5fd1HqSeAt1-egLaUYjWTJ4jpCkrMyi2wB3Ne6YensTS5I04f9yNzaA4_JYtiwfE1W6Yh6ajYD5C1QSjuGk1AdtYchkG0Wi9bpnsuZszNOZMoMVzXx_cVpF2iHIx1lpNeB42zfWXrGuh1LOzvimVBpWVK0tODYmUmKg5bXzg1MihZ8p3e_vcoIHqs7ueQtocOR45MhcZ4ak_n-fXa8FlOMeDNvM006sgAIjGHbSTDq2SAAXThYVIipD-3P-C-1iJRR2_-oKsioq22cCJ7u-2T_4n8-mBkaFdpKVwNkhcI81lUbmJ9zjIhxgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تهران، بیت رهبری، ۹اسفند ساعت ۹:۴۰دقیقه صبح
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71263" target="_blank">📅 10:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71262">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=tmXAti8-G9Q-vPZjvrauGG9mXf4xc71SnR4S1XCABYVe4IQYqTh7AIlDxoIUnIEKS5OWJVoUSobkL_2ommE9L2y-QPVuzpy-QDQrrF_d3saeFB6hR9bJdZKFYIhZVWHga_wM3I2crDm_9Xjz68L-FuduhMUX9GOrnFNnXoSIIIaj9B9Yccw5storvuVUJetM_oHK-vATrH5R314PUu_8LyM91LqVa1GPPZ8Dv7YIUzfdNQJIKGof8huWwEMiulDLm3_O4cb8WoZ8h3EE6GnMsd_JmMFx2bl1Dix9YAf4kltQkRp6NfjM6Ksjwh5igimwsXG70rp7wvyaP64aE-luxXtzEjD18e8dUP1MYYWXwDAEerQBobJc-vUM5pEbW9UKwqtC75Y_28CJXhWBJ2MwTf9rAjW4YrIvj5m4UfA6Py20ps0vxuuSadngsGAFtD8Q8JvGsaO6C35IxkSqNgk3O4Fe4D_kOoNnhSxCrROnakx5h1qCJ1EIZBPAZ5Lg8QKrIFgr4Bpp27A8aGMz4hY05udCVqRse0PiwBwMBXVKaP7J9GUZX_aOMkwniGp-jVVg6Izw2-8eQJ0FFyE1_45NMt-4bRA3UBANV-i2qWzqj05MrdvTM00XnRRE14v4Gy2IVGaYs1LCpVqK9JtGPBzSNWh222DOgy89Sf5sJ40HLBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221662e8f.mp4?token=tmXAti8-G9Q-vPZjvrauGG9mXf4xc71SnR4S1XCABYVe4IQYqTh7AIlDxoIUnIEKS5OWJVoUSobkL_2ommE9L2y-QPVuzpy-QDQrrF_d3saeFB6hR9bJdZKFYIhZVWHga_wM3I2crDm_9Xjz68L-FuduhMUX9GOrnFNnXoSIIIaj9B9Yccw5storvuVUJetM_oHK-vATrH5R314PUu_8LyM91LqVa1GPPZ8Dv7YIUzfdNQJIKGof8huWwEMiulDLm3_O4cb8WoZ8h3EE6GnMsd_JmMFx2bl1Dix9YAf4kltQkRp6NfjM6Ksjwh5igimwsXG70rp7wvyaP64aE-luxXtzEjD18e8dUP1MYYWXwDAEerQBobJc-vUM5pEbW9UKwqtC75Y_28CJXhWBJ2MwTf9rAjW4YrIvj5m4UfA6Py20ps0vxuuSadngsGAFtD8Q8JvGsaO6C35IxkSqNgk3O4Fe4D_kOoNnhSxCrROnakx5h1qCJ1EIZBPAZ5Lg8QKrIFgr4Bpp27A8aGMz4hY05udCVqRse0PiwBwMBXVKaP7J9GUZX_aOMkwniGp-jVVg6Izw2-8eQJ0FFyE1_45NMt-4bRA3UBANV-i2qWzqj05MrdvTM00XnRRE14v4Gy2IVGaYs1LCpVqK9JtGPBzSNWh222DOgy89Sf5sJ40HLBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🔞
وایرال شده از رقص و شادی سربازان ناو آبراهام لینکلن توی کلوب شبانه توی پاتایا تایلند
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71262" target="_blank">📅 10:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71261">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b860e39243.mp4?token=J5tNOuVnGxwQHRKuFpIIJOgGfsKWQuiVAYEigOpZAPWgMPV6jMW3gOvNXuCcIMs9-S7DkBVXRCR-ImF9EzAlX6JblsgWO7bmxAQzJDWiVl-Z-E0IRo3nnaSWnXdGOY83zh8vp3E1J-Qfhmt1BNTeCm6ITE01YALTM68AfwQow_EpKlkjSOGl7q-M4XGrZd19yySP15amaGRuAxr_sB1Cg3-w_hlmZmUrXAbCs1pRtdECc5rOh6YRmajv2Vqs2_959_5UXhO1kNQqct4Jw_m7D61CD1f3pqr4yjpyvoB0LsN_pqm7A9nsdfgSLqxbS5S2hEJFst-GCS3ZgYzo4L6yig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم ترسناک منتشر شده از یه بیمارستان روان‌پزشکی و رفتار یه بیمار ساعت ۳ صبح بخاطر مصرف مواد مخدر شیشه، گل و...
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71261" target="_blank">📅 09:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84f97591b9.mp4?token=v4b8DFla_VEBAs96aO67SimiJoX0dAV1Kmm1xdBH6O3VRKiVNIwOHi4HPOtPuWk9WowWlSuF1vo-mSTWfNGpuFN57JHD-l1rUR7W_Mch_Ch2ZSzpfQdLrUZpsX9ivcBnNJBJwnk8XU6dvcnz1MxUYHmHhAgz58yZ7WmlfGK8PfbORVVcw5ybZodpOSDUdtq_S6Fgje6ThKTWgmVPKQSZNLYl_C652jzVim0HfL258EVe_SfMQqb4vxdtLNzIujKspN_7dglvvOVuTC8XXBVusz1Yz9x9GlgdQlrj19snEc-xK-_5HW_5vT6z_5wp_dGJCUd0OlQNYZwkphYMydPo4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
⭕️
گزارش‌هایی از تماس‌های ناشناس با ساکنان جنوب ایران؛
درخواست برای خودداری از حمایت از سپاه در درگیری‌های احتمالی آینده
بر اساس گزارش‌های منتشرشده، اخیرا تماس‌هایی از مبدأ نامشخص با شماری از ساکنان بومی جنوب ایران برقرار شده و از آنان خواسته شده در صورت وقوع درگیری‌های آینده از سپاه پاسداران حمایت نکنند.
گفته می‌شود این تماس‌ها با کد کشوری سوریه برقرار شده‌اند، اما هویت و وابستگی تماس‌گیرندگان تاکنون مشخص نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71260" target="_blank">📅 09:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71259" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71259" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gERIJoMigZZIAwkv5NfrfWaGAbf5PobOxHFcJkvOobIadaPXWiNhiI6zPfDIeACEVBxYDedbGNdR1_DP-NsV3f9DZwv3qiuAz08__SayShjtbeZZ8jkryM7F0n4PbCRT7etK4pd2myles9ZtPzt_gZ-MntT6_UDPtV4sLUmjZ2l2Fe0QGVLWQiYVypnCN5c-7p-OeVfdupNZHRcPbLQL-Z-0K8RT76TZLAAx0yA1_eAqo-FpjXqSnOA7lE4IijFet_NFSUBqM8KB8vedTNZC2uG7f4NJPO-Lsmd9vEt13dMjK-5_xz5kLc3MAilGKSRTYDsKW4v70svEH0-OErHfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان
US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71258" target="_blank">📅 01:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
⭕️
از دقایقی قبل نرخ سوم بنزین به 10هزار تومان افزایش یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71257" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56a780504.mp4?token=K5xURIU2WntE77DkC2w_7ZHHKuTYJzt9N9FHkxn9XkdjRd1GkG3aj832bIwhu9ADAIJ0EKD_QPvdV8SU1-pL1DDTnhMMtw-IftUqoVG1kLsjddr4IPRrD5RN2mLTE4DGOQhwWmBCUtiWMzdiSLi6_Z84k7Mc-kROtVnapxB67l2jtJuix-o0oJGt065A8jzUH84qJLcibNcoV4sAD3X0pGDPv_dEMAeF5fdOEZPxZJxEg77lfBkJvicKCIkhza5-E9j6ONJIy6KJzRaEJ8H7TqcDyLUdAL5GU_g5zmwISXVTRn01k6S64GI5rHh91lYnRePjKiygmSCiE9HrFA2V9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56a780504.mp4?token=K5xURIU2WntE77DkC2w_7ZHHKuTYJzt9N9FHkxn9XkdjRd1GkG3aj832bIwhu9ADAIJ0EKD_QPvdV8SU1-pL1DDTnhMMtw-IftUqoVG1kLsjddr4IPRrD5RN2mLTE4DGOQhwWmBCUtiWMzdiSLi6_Z84k7Mc-kROtVnapxB67l2jtJuix-o0oJGt065A8jzUH84qJLcibNcoV4sAD3X0pGDPv_dEMAeF5fdOEZPxZJxEg77lfBkJvicKCIkhza5-E9j6ONJIy6KJzRaEJ8H7TqcDyLUdAL5GU_g5zmwISXVTRn01k6S64GI5rHh91lYnRePjKiygmSCiE9HrFA2V9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
عادی‌سازی سقوط تپه علی‌الطاهر توسط طرفداران قالیباف
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71256" target="_blank">📅 23:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23e98b62df.mp4?token=Ci3TjndQERCcSAq3WvCxvLiYu3i7AERhqMSjNRk8uuFgaoq1PlnMdNUa7JdaIKJ0k7lsyxrXo1K7tuxKCW_isjx3OIcfLtaEwtHCbBK8A4BDjljl9SNfSieG1pM_eihVLzGBZe1UJsaH-tGA6KGL3qwe38eNlk5yxnKIoyseqd_Il27PS0vOg2NAieLd9-D6N8jc5dZR6k3J1KY_bBh9M9RH3MefJKm0ECATjIgYagk1bm6HypfHHsOfsQGFLr-w627ukqnd7Fgawpe_nKPqjprgBZVXL-JvFgAnFpJGc_Nc3tJjiEmlwsO4F1GZro2Jbj5ytFBlYg_7-G1Zyjj8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یادی کنیم از اوستاااااد خانعلی‌زاده که در دوره جنگ 12 روزه معتقد بود جنگنده های اسرائیلی هرگز وارد آسمان تهران نمیشن چون باید چندصد کیلومتر داخل ایران بیان و برن و این کار ممکن نیست  و اینا همه شایعات مجازی هست!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/71255" target="_blank">📅 22:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚫
فوتبال مملکت هم اوضاع جالبی داره.  خداداد عزیزی امشب کلش فوق‌العاده کیری شده و اینجوری خواهر و مادر امید عالیشاه رو به فوش کشیده
😳
😳
😳
😳
😳
@News_Hut – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/71254" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⭕️
دقایقی پیش صدای چندین انفجار از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/71253" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ead429175.mp4?token=ZY_4KyZeJd2CqLV_2mRTLS1RmBZu_1BAVwVhpxtpZROZvCg2gedcNsSi9Wu3EakHOqkdGzTIiteoFSO8GnvOvyMZnvFqLDkW_EeNeypBc_AK2nrEx8v79GaZYzfDxcQZPqSQL-qV66JEk7vVVzgSNKmLbKbe6W_Fqo0lt1n_BhbLMXemHR_zyE9De-aXs7AC19gnLOEbmwcQq0o9PQ8kZtJ8jEbdtrRUv7Su8Izlug2UDjDFFf0gs5_dXpDJtdIt8_98GPSuFt0yGJmlY8sOffhDC9P8i5sFI0wd5cvoBPgG0yFlYUlnFaephTkPfXppJCy8W0YhlywMsUMq6l4TeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ead429175.mp4?token=ZY_4KyZeJd2CqLV_2mRTLS1RmBZu_1BAVwVhpxtpZROZvCg2gedcNsSi9Wu3EakHOqkdGzTIiteoFSO8GnvOvyMZnvFqLDkW_EeNeypBc_AK2nrEx8v79GaZYzfDxcQZPqSQL-qV66JEk7vVVzgSNKmLbKbe6W_Fqo0lt1n_BhbLMXemHR_zyE9De-aXs7AC19gnLOEbmwcQq0o9PQ8kZtJ8jEbdtrRUv7Su8Izlug2UDjDFFf0gs5_dXpDJtdIt8_98GPSuFt0yGJmlY8sOffhDC9P8i5sFI0wd5cvoBPgG0yFlYUlnFaephTkPfXppJCy8W0YhlywMsUMq6l4TeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
دیشب خبرنگار لبنانی داشت توی نبطیه گزارش تهیه میکرد که همون لحظه به شکل پشم‌ریزونی اسرائیل حمله کرد به اونجا و همچی قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/71252" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=bBVtJ8bEXkuPhXUjYMiRqVseOGyWRUhUw65aZPH1Yo0UIBfEP2DYMMmBLnxJWRl0rUOA5YF29IB03fteRLmzHLlICfHeXhOVYujq3wK1Ynoq6q1_hoq26_dmh7iYklnq3VPfT3NM5MUztzzBqI5TRfupedqtFLVmFxRjWll7B1x2IphV9baI53y3d6B7aLAHz2eeoASCzG72CpaM_fDfWg3kER-g2m9SB5xaPhAn5kA_xgTyU93PK6Deo9QE0HCR0qCmXowAFGbFAA1NM0td97wYPVnuoVdJGRlt9SPowvwXWx9T_s5kDB2TZ0yZogOENirpMGHd1J93lJ1R9KKxl4t7Q6zBummsLK2uWG-ItvC2c2emhcdK_tjFX-8A2uSFp62bTsVufnGXhlisDel_LYW5RKWYdQzOy_ZETqBW6ftxxGR1DbOXNXaV7kZvXdGiTzR5nzx2N98vi0FjxRo8qAyV-OGyehvOFpBdNS3H33lIUWCUf6X2ZkaUDyhToEibDby1iy4jZO5phodU2-d9RVUrq_sL-b2YYfH-lY6bpQW8Q4ffGniBJod1pHzWrKBGhHzFc4O8bWjLt5bqlQWDEZpUpAvOaRk2RUoySaC0737Y-9DlN-m2blwvrgKA0Q8SP1bvq-9tj4Mt1itGVPxxfgzyhQuEOTe2kCqebn1qpWI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a7bd5cfa8.mp4?token=bBVtJ8bEXkuPhXUjYMiRqVseOGyWRUhUw65aZPH1Yo0UIBfEP2DYMMmBLnxJWRl0rUOA5YF29IB03fteRLmzHLlICfHeXhOVYujq3wK1Ynoq6q1_hoq26_dmh7iYklnq3VPfT3NM5MUztzzBqI5TRfupedqtFLVmFxRjWll7B1x2IphV9baI53y3d6B7aLAHz2eeoASCzG72CpaM_fDfWg3kER-g2m9SB5xaPhAn5kA_xgTyU93PK6Deo9QE0HCR0qCmXowAFGbFAA1NM0td97wYPVnuoVdJGRlt9SPowvwXWx9T_s5kDB2TZ0yZogOENirpMGHd1J93lJ1R9KKxl4t7Q6zBummsLK2uWG-ItvC2c2emhcdK_tjFX-8A2uSFp62bTsVufnGXhlisDel_LYW5RKWYdQzOy_ZETqBW6ftxxGR1DbOXNXaV7kZvXdGiTzR5nzx2N98vi0FjxRo8qAyV-OGyehvOFpBdNS3H33lIUWCUf6X2ZkaUDyhToEibDby1iy4jZO5phodU2-d9RVUrq_sL-b2YYfH-lY6bpQW8Q4ffGniBJod1pHzWrKBGhHzFc4O8bWjLt5bqlQWDEZpUpAvOaRk2RUoySaC0737Y-9DlN-m2blwvrgKA0Q8SP1bvq-9tj4Mt1itGVPxxfgzyhQuEOTe2kCqebn1qpWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمودی بعد مصرف یک بَست:
موشک رستاخیز ایران می‌تواند در لحظه اصابت ۸۰ کیلومتر مربع را نابود کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/71251" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzbmiHtx71GwRXmYq3IHO-q0t6rNmfQjD40qnZNwzmq_BbRgyp1QUCYgl-Fz_NUWuy0O_UiuaPdyLhXSiOQ7YCxf7-46DY_l49oo2uff7Xr0rB8_iw-sOat0Oy6sF59CaYYnN2nEHNh0Gm346ZaIvQotJiwnQc1C-SoDHtOYmLTcmaj6q4iX1W3awuBfLHq75OGkgmsGpvGO1bla9PB5iBNLAMmdKYx3W4uZHPj3HVKOBSRDpOh_mBnoHv8bozQuDhzV6uzGVJu5SU0mkyHhwul0RG8So9XP0fMh3RiDP_cOtx7pZpFK5ZtiL5tOB5umCr4IB7WjQGbDPHQxGm0ScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
🇺🇸
ترامپ بازنشر کرد:
سیاستمداران ارشد ایران خواستار پایان دادن به جنگ هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71250" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=MxM5xhCxa73BFoyCGacti4FvEtM4RY6M-XT2lyWExfDPXwkWP7ogxUOnOPAemIFNAlHa8N3VtV_IEKWctYs3Xr7eBzToHfKh47-XMEphjGAG6flkY8S3EOyt2To7NcBV173G2HPoNWzutTig5pHgXMvQO-O-htk4xCpUlmMZupM0D7rvnFULidbstbrRg0IM-v-z-ET99XqPAO9iXaiB5sG3ouVW2IY8Xw1hz3-p09xZbcvnyVdI48mKOP7haY-2cFnn08Nq_5LH9zWLq0SR3bneVNpAZxQEdOPR8xy5Ayq1ZVPx0Wfa_AoGqC3MhKapx8uImC8vtHJBODabzio2SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/807f8a83aa.mp4?token=MxM5xhCxa73BFoyCGacti4FvEtM4RY6M-XT2lyWExfDPXwkWP7ogxUOnOPAemIFNAlHa8N3VtV_IEKWctYs3Xr7eBzToHfKh47-XMEphjGAG6flkY8S3EOyt2To7NcBV173G2HPoNWzutTig5pHgXMvQO-O-htk4xCpUlmMZupM0D7rvnFULidbstbrRg0IM-v-z-ET99XqPAO9iXaiB5sG3ouVW2IY8Xw1hz3-p09xZbcvnyVdI48mKOP7haY-2cFnn08Nq_5LH9zWLq0SR3bneVNpAZxQEdOPR8xy5Ayq1ZVPx0Wfa_AoGqC3MhKapx8uImC8vtHJBODabzio2SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
به تازگی یه چیزی مُد شده به اسم «جوجه پارتی» ، تو این پارتی، پسرا رفیقای دوس دخترشون رو به همراه رفیق سینگلشون به این پارتی میارن، تا برای همدیگه جوجه بکشن و از سینگلی در بیان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71249" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIeK2l-k6grZkmqW8A1nYomf4_zWSicPRPL8smnLnoUC65-2EXvEG9dxlKc04AO4hhVA8tSoIUZG96eq3ngbS0i6rkQT4og5yzl6Jas6I85vyKPERVdWwS8JCs7gYZeMfQIYt7rBQ5zopt4a47kqdM5JjzMoviK127X-2kF5nDMQcloJMy2FPgr5PDaKjdk536KdkBGoESSEWC8oy0TFYAQSvRUNF0OUJuQHbLUMuc2sMDWSkCUndm1UhC8sSxbjgGpEaM41E5dOWmUF0ZLqPYAfucn5gjk_BG7YzxZHI_B1Qbk9lYHTtLb8sWCcjkDY2nRYwjsMekGVisWhiZVMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه موضوعی هست که فکر می‌کنم تقریباً همه ما به‌نوعی باهاش درگیریم؛ هزینه و شرایط بنزین.
شاید خیلی‌هامون هر روز درباره‌ش صحبت کنیم، غر بزنیم یا فقط سعی کنیم با شرایط جدید کنار بیایم، ولی در نهایت چیزی تغییر نمی‌کنه مگر اینکه صدای تعداد زیادی از مردم شنیده بشه.
برای همین این کارزار راه افتاده تا نظر و درخواست مردم درباره این موضوع جمع‌آوری بشه.
من خودم اینو امضا کردم و فکر می‌کنم اگر شما هم با موضوعش موافقید، چند دقیقه وقت بذارید و امضاش کنید. حتی اگر فکر می‌کنید یک امضا تأثیری نداره، همین امضاها وقتی تعدادشون زیاد بشه می‌تونن نشون بدن که این موضوع برای تعداد زیادی از مردم مهمه.
اگر دوست داشتید، لینک کارزار رو برای چند نفر دیگه هم بفرستید. شاید همین کار ساده باعث بشه افراد بیشتری از وجودش باخبر بشن.
🔗
https://www.karzar.net/346254</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71248" target="_blank">📅 19:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71247" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71247" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9O_z4L2kLBpxHvcnS4uXdONI7YaDYJYeu6cjjJCRl8pRCFPsSYfRqk-V8plpgMHnLFHUjmOWtPOpsdHGxPU1ZSFPxuckLnxNfbGQ_mJDPOVAHDyy6Pk3yr-E2q-uRaM6SCQVJ272k5F-fAdQzPek-O39uspOMuJkQylEkM4vrCaMWH8D7coGbUhrtD3As7D3TiD0g8nlVVkHi270bmdnL6eZDD0KlcjRjPcw2QkdcfpBPtWy77j3esCdynMcqTcpzfwCxZNcbiwReqOe0FgnR9MMoJ_w3yVo2S3Bne_MATQh3XhBxsWDZEl5tcA9_Ff3En5xVzqQXYUtcv0MdQI9A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71246" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
🇱🇧
🇱🇧
این ویدیو رونمایی شهر موشکی عماد است که مو به مو طبق شهرهای موشکی و پهپادی سپاه پاسداران ساخته شده؛
دو سال پیش حزب‌الله لبنان از این شهر موشکی زیر کوه‌های علی الطاهر رونمایی کرد.
جمهوری اسلامی بیشتر از خود حزب‌الله لبنان خرکیف شده بود؛
از برنامه ثریا تا اخبار سراسری صداوسیما تماماً افتتاح شهر موشکی عماد با ۴۸ کیلومتر تونل بود که مدعی بودند ساختش چندین سال طول کشیده و اکنون تسخیرناپذیر و نفوذناپذیرترین دژ عالم است.
این شهر پس از سه ماه محاصره توسط ارتش اسرائیل سه شب پیش در سکوت خبری تمام رسانه‌های جمهوری اسلامی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71245" target="_blank">📅 19:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c892ca398.mp4?token=BkVvp0DMCbonYMbCXQEdB3JFc7lFvjEMi54HCXya7b4hFFufmiUf0HX6VEnvn8h6FH5Ox0UYbh93PEcPBhkBEYPJNrYo0VZkCHT3w7FYKTFR0yI1p9I0K-L_pNy3EGCn8w80k61R7R8QpnxzySuGO1jph6Mb1fZYay_9xY_i8pq9Jz6BQHQ6gK0bhJTLtq3kpCqXEF0l-S5BSmTpIFornnnwhHBbHGFsdIYlUCuHMz8cX5Y6whYXCrd-IjCgTQEYzjpFPLpXhx7UVSiOiigqhqy8bcqNigt4dUOJa2vPvCyOrx6UkbjzlPerthtwD3QvsA-kgd_1wS4bfpGMwUP72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از لحظه فاجعه انفجار تانکر حمل سوخت در سنندج که باعث مرگ 11 نفر شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71244" target="_blank">📅 18:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=UZWZfnWpEnTT_cXfxiTF0pnjmJA-YMPrzSBiNxz2wyy6TAUh8RB1_-2Emc6Hsu9TpA4lykad7NPzG8bC2cew_bLs4MYlToMeGcmVHHXHDAebzEpbg4a7fbgHU6uYpnvojcQ59hNS06qx_O3vn6lJZnJY0JtoGP1cgCGQxQdfPk4Z8y5u2c68FNl9ReXsXbaJk1t29NA20z6WE5ja2vdDWSfUuO97_a-LpQJzzvRaEuFax962bZf6jAyHTrcTIKxZmsW8x_n8C50wrRG5XZDxVfm8KUnSuBGRC_AmdY8yu6JpN_mC4c6bZ1yqS4oOputIVniaQY0gtwYuRiPFjTfI6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08df0f1761.mp4?token=UZWZfnWpEnTT_cXfxiTF0pnjmJA-YMPrzSBiNxz2wyy6TAUh8RB1_-2Emc6Hsu9TpA4lykad7NPzG8bC2cew_bLs4MYlToMeGcmVHHXHDAebzEpbg4a7fbgHU6uYpnvojcQ59hNS06qx_O3vn6lJZnJY0JtoGP1cgCGQxQdfPk4Z8y5u2c68FNl9ReXsXbaJk1t29NA20z6WE5ja2vdDWSfUuO97_a-LpQJzzvRaEuFax962bZf6jAyHTrcTIKxZmsW8x_n8C50wrRG5XZDxVfm8KUnSuBGRC_AmdY8yu6JpN_mC4c6bZ1yqS4oOputIVniaQY0gtwYuRiPFjTfI6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
طبق قانون، استیکر و گیف خنده داری که از رفیقت میسازی جرمه...
و میتونه ازتون شکایت کنه و تا 1 سال حبس و 5 تا 33 میلیون جریمه نقدی داره.
اینکه شوخی بوده هم هیچ تاثیری تو مجازاتش نداره
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/71243" target="_blank">📅 17:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff06303045.mp4?token=IXbMVb-e_ySJ6nnmWblJsR-M7RYyiBKj-HRsq54a0PWJirRZNr2mBDA3RLtp5P4Mzapmn8ArjnsPHzGf63XWm5tkgkCyWrYUXtItDu7HsGJ_v0rBtTPeXrqIkN1xpIypTegVx4VHG5N_jWVzOSdY8Fh676jXKUa2wnvVpcTNtX38LPiPR5Fc2ISbGjp1vUbUT74lgGwCCOlTTMhriNi-gz0_kzhfHpNevu9Zqe1EduRVyxgKFI5ItBHjHl8EhnujKw9uS2SUwrqJT1eZC7rW7iwi_JPXpU38oujdzlUtzPBiY3mq-qUBrXLFEqHm3NRNyuNKFfGBY_sBKr8BPyHyAWrAmy4YYwk9C3qLdUJrX7Ug0gwL9uZiYG1k63-QtN_KoxOeeimr5vFddKsBMvLitQuv5zS9tWJEW7H6dAzfC3T-AVXx_UxZUGWz5WYLydjD4sZqthseCyl9SSaS4_50RuCcmvZ6xoLij-YpWemlavQs5RnMsjTHHn2m94sAaiX--jk0lhJR4sQyZg7DHNAQyGwCkkLBRJKQV0wpaRSNyRfn4hmgqT-z66HT4gnJP-iHfS-XS1vWxLWIDMh0yK7H17jYD8_ji5I2YlCH00rddrwCFTWGS9io8tPkZW1V22ElBYtz9zBbSeQG1-AV_Vwywb6X3QTBUqnOXDrnbd3lXd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff06303045.mp4?token=IXbMVb-e_ySJ6nnmWblJsR-M7RYyiBKj-HRsq54a0PWJirRZNr2mBDA3RLtp5P4Mzapmn8ArjnsPHzGf63XWm5tkgkCyWrYUXtItDu7HsGJ_v0rBtTPeXrqIkN1xpIypTegVx4VHG5N_jWVzOSdY8Fh676jXKUa2wnvVpcTNtX38LPiPR5Fc2ISbGjp1vUbUT74lgGwCCOlTTMhriNi-gz0_kzhfHpNevu9Zqe1EduRVyxgKFI5ItBHjHl8EhnujKw9uS2SUwrqJT1eZC7rW7iwi_JPXpU38oujdzlUtzPBiY3mq-qUBrXLFEqHm3NRNyuNKFfGBY_sBKr8BPyHyAWrAmy4YYwk9C3qLdUJrX7Ug0gwL9uZiYG1k63-QtN_KoxOeeimr5vFddKsBMvLitQuv5zS9tWJEW7H6dAzfC3T-AVXx_UxZUGWz5WYLydjD4sZqthseCyl9SSaS4_50RuCcmvZ6xoLij-YpWemlavQs5RnMsjTHHn2m94sAaiX--jk0lhJR4sQyZg7DHNAQyGwCkkLBRJKQV0wpaRSNyRfn4hmgqT-z66HT4gnJP-iHfS-XS1vWxLWIDMh0yK7H17jYD8_ji5I2YlCH00rddrwCFTWGS9io8tPkZW1V22ElBYtz9zBbSeQG1-AV_Vwywb6X3QTBUqnOXDrnbd3lXd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
🇰🇵
روسیه و کره شمالی یک پل جدید را در امتداد رودخانه تومن افتتاح کردند. این پل دو کشور را به هم متصل می‌کند و با گسترش همکاری‌های نظامی و اقتصادی این دو کشور، اهمیت این اتصال نیز افزایش یافته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71242" target="_blank">📅 17:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=LBcEXrAYSM4qpW8KR-PSSjqzu88UEJNBfK09THCD0O2U4FyLV_Et23WXUhyL0ltu5Ab6Z0JTfXEOEp4NJk9ZomHL4rfmPTvlhZiiGC6MverLXgDUI9F_fY5eNMsIN2yCwiy0fw9A2GfUKvueNN8i4gMdGZfarjvNqBQ7fQ6Y1yxYldakFy1b9YZ-rRQWWfg_RYO3X26l0VnAUpVELfvQ76ojo6hXx0ve5n3lD6OUEt64OjVDSjjmz_wCxNSo8Q6ksBu--tX8CzI0RRgC8gxmJfq76ZC6vzV5KlBaM9eo5k6N4atDsSIdSngMCKaQ6LbNP9WR9_FjmszFkx2zE77v7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8cf25fef.mp4?token=LBcEXrAYSM4qpW8KR-PSSjqzu88UEJNBfK09THCD0O2U4FyLV_Et23WXUhyL0ltu5Ab6Z0JTfXEOEp4NJk9ZomHL4rfmPTvlhZiiGC6MverLXgDUI9F_fY5eNMsIN2yCwiy0fw9A2GfUKvueNN8i4gMdGZfarjvNqBQ7fQ6Y1yxYldakFy1b9YZ-rRQWWfg_RYO3X26l0VnAUpVELfvQ76ojo6hXx0ve5n3lD6OUEt64OjVDSjjmz_wCxNSo8Q6ksBu--tX8CzI0RRgC8gxmJfq76ZC6vzV5KlBaM9eo5k6N4atDsSIdSngMCKaQ6LbNP9WR9_FjmszFkx2zE77v7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
معاون وزارت ارتباطات :
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی باید ادامه داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71241" target="_blank">📅 16:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=Da25xBE0bz5xty66C_tR3nZyxXX-cY2AgslOZjtFO_nNgCMgYnC9axzIQk-yuQ2sfHfhpvMwLYAqarCE_C9V6MgDKBtcOMmbqAukLhTWmbr32eRZZ28zSmgbBv9gWcfNGLkCOiXrNc1DLgQbJXokT2L5t_hz9CZbhxX9F4bLAyRAfof1O-7Y8v6rYu1VnVcpgH7nwRGw3QU9L7snZ-577y_nVzSh_b19OGm0mDFYoK_wyqmGOQC1rNy2uZSU5kNDZf4qgM3g2RTbA1ncABeR_nBBh_CgSogfziJEI21qWxebL7Ra1NgjdyyYGTMhOjZJVDjdb7MTaa6nvbzip7mDJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6ea773c3.mp4?token=Da25xBE0bz5xty66C_tR3nZyxXX-cY2AgslOZjtFO_nNgCMgYnC9axzIQk-yuQ2sfHfhpvMwLYAqarCE_C9V6MgDKBtcOMmbqAukLhTWmbr32eRZZ28zSmgbBv9gWcfNGLkCOiXrNc1DLgQbJXokT2L5t_hz9CZbhxX9F4bLAyRAfof1O-7Y8v6rYu1VnVcpgH7nwRGw3QU9L7snZ-577y_nVzSh_b19OGm0mDFYoK_wyqmGOQC1rNy2uZSU5kNDZf4qgM3g2RTbA1ncABeR_nBBh_CgSogfziJEI21qWxebL7Ra1NgjdyyYGTMhOjZJVDjdb7MTaa6nvbzip7mDJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آخوند قاسمیان:
برادران یوسف 11/11 وحدت کردن یوسف رو انداختن تو چاه، این که وحدت نیست، وحدت باید حول محور رهبری باشه..
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71240" target="_blank">📅 16:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/98f065761f.mp4?token=HkwT6C7NyljcWv1EcCIffUEWxBcjmI5wPAndBhUyjq0a47vf44VJpgBvP6QMjxIHPNL8UzkjjIWhYJttXQMsRQ9C1-BfPVc9N0zdL_ULHolU8yFhdLXTv9Pz4S7R6dp80bltCOSk_YCgfO17H5bMuMN8WscF6-3s35jxLFPHiw5VWlAzTX4ReZT4Ncp1Q_rnF0spfTA43zwzbELMbEBFsKV_GSW47wFu_TZRk8DSSjO4J6foGlsnxd4hzYcRRaTvx6rEG2qPAwV4S59_VcD7FsqhZiZ12B1_J9qoQ0IFn4DOXVMO91PjHyqQ2WfaEEn_jXhylb6ayYWZg-Is4Fz81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/98f065761f.mp4?token=HkwT6C7NyljcWv1EcCIffUEWxBcjmI5wPAndBhUyjq0a47vf44VJpgBvP6QMjxIHPNL8UzkjjIWhYJttXQMsRQ9C1-BfPVc9N0zdL_ULHolU8yFhdLXTv9Pz4S7R6dp80bltCOSk_YCgfO17H5bMuMN8WscF6-3s35jxLFPHiw5VWlAzTX4ReZT4Ncp1Q_rnF0spfTA43zwzbELMbEBFsKV_GSW47wFu_TZRk8DSSjO4J6foGlsnxd4hzYcRRaTvx6rEG2qPAwV4S59_VcD7FsqhZiZ12B1_J9qoQ0IFn4DOXVMO91PjHyqQ2WfaEEn_jXhylb6ayYWZg-Is4Fz81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایشون رو آورده بودن موقع زایمان پیش زنش باشه و بهش روحیه بده، آخرش دکترا مجبور شدن خودشو درمان کنن
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71239" target="_blank">📅 15:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f53489458.mp4?token=C-Os1Fucot9lwwh55Xh_8V_jT6jArs-LF1-B8GL9vBY89tU8ajdIRj3EOZMi9Vt0QrqRm7kxkN2Zrl1j4OEbbTlN0rEsxZupU9BdmhliFiyLNMM5G5i406Y6te_e-j6uQYCN_ueoEzteUKoQcU-Pvi3yiyP2e9mAAMwo9c2jGKrizDYx3yW1bLtmi8fOdVuARjMUKnk_IISG2G0whzvCVyJmGGShHwYoWo92hGOm7f6LBnwQaogvVl-b0JI8h0sufarCEw9GHLLNINjU4rk0sIT8orVDlyT8iF5zFJa-f_lX6QTDJtj1bNLiUVxk9jnavqvKkop18KgySLxgPvlLTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f53489458.mp4?token=C-Os1Fucot9lwwh55Xh_8V_jT6jArs-LF1-B8GL9vBY89tU8ajdIRj3EOZMi9Vt0QrqRm7kxkN2Zrl1j4OEbbTlN0rEsxZupU9BdmhliFiyLNMM5G5i406Y6te_e-j6uQYCN_ueoEzteUKoQcU-Pvi3yiyP2e9mAAMwo9c2jGKrizDYx3yW1bLtmi8fOdVuARjMUKnk_IISG2G0whzvCVyJmGGShHwYoWo92hGOm7f6LBnwQaogvVl-b0JI8h0sufarCEw9GHLLNINjU4rk0sIT8orVDlyT8iF5zFJa-f_lX6QTDJtj1bNLiUVxk9jnavqvKkop18KgySLxgPvlLTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ویدیو وایرال شده از یکی از معلم‌های مملکت :
اگه مدارس امسال مجازی بشه، از گوشیِ شخصی‌ام نمی‌تونم استفاده کنم.
چون پارسال 4 تومن گذاشتم رو حقوقِ 14 تومنیم و این گوشیِ 18 میلیونی رو خریدم.
امسال همین گوشی 70 میلیون تومن شده!
حقوق من چقدر شده بعد ده سال تدریس؟ 20 میلیون تومن...
اگه این گوشی من خراب بشه، دیگه نمی‌تونم گوشی بخرم.
آموزش و پرورش باید به فکر تهیه وسایل آموزشی (گوشی و لپ‌تاب) واسه معلم‌ها باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71238" target="_blank">📅 15:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
این خانم ادعا می‌کنه که در جزیره اپستین بوده؛
صداوسیما هم صحبتاش رو پخش کرده.
ادعا کرده که به کل جزیره تجاوز کردن و شرایط بدی بوده.
بعد میگه خداروشکر فقط خودم مصون موندم و بهم تجاوز نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71237" target="_blank">📅 14:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c603211e44.mp4?token=b8Hgiu4mZ5mkhryI6QLCrJmGyfyjV4Qr8bW38Gke9y8I2rqf2oFA2_ZQ61sXBUSSZhZgm6maTwfe_aIL-NbL5dwguCg2lLYVNMixfghvoIEu7sO36PXMJZbhW1EoRoXmY4qw0bg0lI7yVYN4KsTHyp2oNhFr3BAQhFp4GvL3gmB3FAJcq0zVZuox5wiZElZA9xERLMga73rmNxvyWT2exVdxGcZ-sY-0sKfRolbYExFkgkieiRNT8UXg3KVS6U1oGT4Z-sV2i91FRTkK_YK_TWODhB6fpNAZ-Y3GSCQKtV3iPdZSOOg5SdyJJqgqWE5xexUHgktbtae52Elp25i_Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c603211e44.mp4?token=b8Hgiu4mZ5mkhryI6QLCrJmGyfyjV4Qr8bW38Gke9y8I2rqf2oFA2_ZQ61sXBUSSZhZgm6maTwfe_aIL-NbL5dwguCg2lLYVNMixfghvoIEu7sO36PXMJZbhW1EoRoXmY4qw0bg0lI7yVYN4KsTHyp2oNhFr3BAQhFp4GvL3gmB3FAJcq0zVZuox5wiZElZA9xERLMga73rmNxvyWT2exVdxGcZ-sY-0sKfRolbYExFkgkieiRNT8UXg3KVS6U1oGT4Z-sV2i91FRTkK_YK_TWODhB6fpNAZ-Y3GSCQKtV3iPdZSOOg5SdyJJqgqWE5xexUHgktbtae52Elp25i_Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی
:
چهل‌هشت ساعت پیش اولین موشک ناوشکن خودمون رو بالای سر یه ناو آمریکا تست کردیم
واقعاً یک جهنمی به وجود اومد.
🎙
مجری:
موشک بالستیک؟
🇮🇷
محسن رضایی:
موشک خاص حالاااا. موشک خاص
😟
ناوها فرار کردن.
حادثه آنقدر بزرگی هست که سنتکام هم نتونسته نفی بکنه. اعتراف کرده به این
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71236" target="_blank">📅 13:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhrHH3l7fcD1Omz1CSxbXKJiDscGAaczEQH2xTi6tTUGhVx50EPG_SCTK-s3ubDAX-Bxvs9hSo1r88zVH6iynZXfR-zNrZ8r8jZrg5bYj8edJ2LRuAPlcUHdeDXfOuFljjVrYtP6nhwaQDLWO1nMiZ27Zk9E3pI4B-4Pozk7hZPxJetpeOcVH2OomBkgCxOtNAC8zvCBWMqSZXeXhzKZ20LXm20WSYs1GqG2VFAyrguHjrvfQQAFncyAwQyda0KzXRej-2_HADGY27dRsV_vamJVy7RXTDrye6YwuXkh2o7ZvvqmowTQfOEGBBzKbgVsVd52TD5Trk3OnEQFXPb4YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
⭕️
🇺🇸
👀
افزایش شمار هواپیماهای سوخت‌رسان آمریکا در شبکه مرتبط با عملیات ایران
بر اساس نقشه OSINT منتشرشده توسط DefenceGeek در ۷ سپتامبر ۲۰۲۶، مجموعاً ۱۹۵ فروند هواپیمای سوخت‌رسان KC-135 و KC-46 در شبکه مورد بررسی این نقشه ثبت شده‌اند.
⭕️
جزئیات این آمار:
۱۶۶ فروند KC-135
۲۹ فروند KC-46
مجموع: ۱۹۵ فروند
این نقشه پایگاه‌ها و نقاط مورد استفاده برای مأموریت‌های تانکر در مناطق تحت پوشش CENTCOM و EUCOM را نشان می‌دهد و علاوه بر پایگاه‌های فعلی، برخی پایگاه‌های مورد استفاده قبلی و مسیرهای ترانزیتی را نیز دربر می‌گیرد.
در نسخه فعلی، تعداد KC-135 نسبت به آپدیت قبلی(3 اوت۲۰۲۶ منتشر شده) ۷ فروند و تعداد KC-46 ۲ فروند افزایش نشان داده شده است؛ بنابراین مجموع ثبت‌شده ۹ فروند افزایش داشته است.
منابع مستقل نیز در سال ۲۰۲۶ از به‌کارگیری گسترده تانکرهای KC-135 و KC-46 برای عملیات مرتبط با ایران گزارش داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71235" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71234">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcNl2TeYbMlAQ9ZBRVdX-1xIUC8ueMaFLtbl5VH02OUeuGIHwvpAZKQg-U5WZJnDlMYdlazUaFUM2NsRstQny2LG6nxAtm_r3N80mFGE3AQPdlQ8yWAirnsApR9PX3w-0xcGStwBIiLdr09QIFEEDjoajf5_HrY9xZwzve7V0Yrov9fwLc-s4IDFhkxB9WXvckbyUhsyvt0eNG2oeU8x0VM3dDFp6MBM1NxNSAtmHmQi-lqjSvrf8AR1jGkJBGRZIIFmyxaX197pn-Uwxoo91qAJjUQBKQwvYP-W_JRJa-_5CJykpmRO0kfBJKWgDf0tEIh3IRT-IOm8Nv74XCPZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
موضوع ساده است: زنجیره تولید نفت و گاز در اینجا گسترده، در دسترس و آسیب‌پذیر است.
شرکت‌های نفت و گاز آمریکایی که در این آب‌ها و تأسیسات حضور دارند نیز در معرض همین آسیب‌پذیری قرار دارند.
به دارایی‌های ما حمله کنید، ضربه خواهید خورد. ما پیش‌تر این را ثابت کرده‌ایم؛ از پایگاه‌هایی بپرسید که دیگر کارایی ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71234" target="_blank">📅 12:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=os3evVwDLce1NAmmFjOXZrTCIHL5xENM-9QBCVyKqUXnI8CCT3yneponu-8aWDSMNS5IwaqnzbrBRDYAsn1GVLXvb8p8KKhiSV5zpDBEaXAv1NOVHySWTtVIpa-BfpVTzUcq6E1mbCyRyONaA9t5LQqZ0aaWnOMcJXPzd6y7pcoGBpzPRoPHkFLv1XX9JyeQkuvMxTWc8bgZmbnDr-e7wbT5RpPpUYj6-v0B-Zws1rIiBqJkMqYXp85hy_wsvVApFU2ysbkVjsuPHXXWSFeyRb1Unk4Ka6Etug_GlPn5JTgLjVMVrh5pgmBLfXYByv_H9w2YjSBcm_8Ylu1bFONgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9570398f5.mp4?token=os3evVwDLce1NAmmFjOXZrTCIHL5xENM-9QBCVyKqUXnI8CCT3yneponu-8aWDSMNS5IwaqnzbrBRDYAsn1GVLXvb8p8KKhiSV5zpDBEaXAv1NOVHySWTtVIpa-BfpVTzUcq6E1mbCyRyONaA9t5LQqZ0aaWnOMcJXPzd6y7pcoGBpzPRoPHkFLv1XX9JyeQkuvMxTWc8bgZmbnDr-e7wbT5RpPpUYj6-v0B-Zws1rIiBqJkMqYXp85hy_wsvVApFU2ysbkVjsuPHXXWSFeyRb1Unk4Ka6Etug_GlPn5JTgLjVMVrh5pgmBLfXYByv_H9w2YjSBcm_8Ylu1bFONgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بمباران آخرالزمانی پادگان فتح خوش‌نام کرج توسط جنگنده های اسرائیلی در جنگ ۴۰روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71233" target="_blank">📅 12:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71232" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71232" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trJQG18bgGVWn4KqabQ29BrdZKUDpEMIchAzMeXkw9Gsaz-uVH6vrTXocs0oo6BdUrY6tJm6sVlJjVveuOejKI0gsR79ZrISxtTOw7nyabjQkIkyTd40RCXsOSyE8teB_0gFFQp-RNgql2Pm5RVDcJmBHP5sJsKzl00mCHj0WxjgmThZBjsgVdXazH-5rLnHaNbJMuzxjaWaR-t5AKc2SjDe9KIyaqPPyOzBiBIhlhAYCjFR3ufW4o79kb_Hcc7ZIIJu0Y9RHeBF4OkcEcREDjxKU0Wz0Yn-Tje4VNE_2rtTgFrhlPoy8ovmXYXf3jzmeYxIROLWa1O_d72_3Nq1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
ذوب‌آهن
🆚
پرسپولیس
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی
به آمار ۲ تیم در در این فصل
ذوب‌آهن: ۵ بازی ۱ برد, ۳ تساوی، ۱ شکست
پرسپولیس: ۵ بازی ۳ برد، ۱ تساوی، ۱ شکست
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71231" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6953e87af5.mp4?token=BQw6z_Lt1KeVb3w0iJQiYu8Tvq3G3LWJuI19bd9B7FMIaTsYK6EWnzF3n91w0vy5HDf6FYO3_bsGUA2Edeni5acWdFU3ZeRYWLcHJW3Sw9ZO6HaJsbzqELlsdIU82LsYasnHAXSXH3Qjgsqg9gsjMzqvyOMi89yzWvpUCvbYZftioGKOUvpd5e26p_yVI28ERAxEbXbNaJlRZ4eT5aLKoLI6RAeH_x7lgtWLijUJIjbYbTvzF6gGRovMFyusl53HW2BpH0KgSFGQD3PGz3ZaSRyf9iAvk83rREzzGFBLDiX82B6BbOPlxGET7zIydnySOZ7DciGUzbW_LAycfByFCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇶
#فوری
؛ بیش از ۱۵۰ ایرانی به دانشجویان عراقی در سمنان حمله کردند.
🎙
به نوشته خبرنگار بغداد الیوم در سمنان:
گروهی که این رسانه تعدادشان را بیش از ۱۵۰ نفر اعلام کرده، به محل اسکان دانشجویان عراقی در دانشگاه سمنان حمله کرده‌اند.
گزارش ادعا می‌کند پلیس پس از اطلاع از حادثه به دانشگاه رسیده، اما هیچ‌یک از مهاجمان را بازداشت نکرده و صرفاً تلاش کرده درگیری را متوقف کند.
طبق این گزارش، مهاجمان وارد محوطه محل اقامت دانشجویان شده و تعدادی از دانشجویان را به‌شدت مورد ضرب‌وشتم قرار داده‌اند و در نتیجه، شماری از آنها زخمی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71228" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=LNA-OPv4Jjlmt-pJQ8WS7JJSFDYYMmzHP1TfLDFE7Mb8qvOoMrJ-a7HULwY8BucZBg8izM8ipTb5clkA6YE2sT_Ht7pUt4a3smOZuh7zpotocGEhLqlcnsCpKnxpCvD5vUuk65I3W8whU4DgWdSkJAv3Cw4Snd6tl10Xgxy-KA1xBcILbftlxJObNIR3THi1ahLCaC6nZsV91iiDaXCd0XyPgY0_ukEVVY3UTY6dCVzubX_7DGHiUpaiH5hSS_Nkkc4FrDTPg1NnJbax7iuKMXht9sZooZkxNaqCLVtpFjCz8wvE5zgipJMxoiSZKqDmqOeARRgxZg0Xc0smxlPclA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6387c174d3.mp4?token=LNA-OPv4Jjlmt-pJQ8WS7JJSFDYYMmzHP1TfLDFE7Mb8qvOoMrJ-a7HULwY8BucZBg8izM8ipTb5clkA6YE2sT_Ht7pUt4a3smOZuh7zpotocGEhLqlcnsCpKnxpCvD5vUuk65I3W8whU4DgWdSkJAv3Cw4Snd6tl10Xgxy-KA1xBcILbftlxJObNIR3THi1ahLCaC6nZsV91iiDaXCd0XyPgY0_ukEVVY3UTY6dCVzubX_7DGHiUpaiH5hSS_Nkkc4FrDTPg1NnJbax7iuKMXht9sZooZkxNaqCLVtpFjCz8wvE5zgipJMxoiSZKqDmqOeARRgxZg0Xc0smxlPclA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از روز انتخابات دانش‌آموزان پایه هفتم آمریکا که این پسره ادای ترامپ درمیاره و مثل ترامپ وعده میده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71227" target="_blank">📅 11:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb757b4cf.mp4?token=RWmiCUuhcwuuttPcwrtygoGKeNt2LADXxuMKakSU-_CrHQoBU8YEAnSK6Htcg3XVeWbgZOCQdvdVkOtj_jRP6nTgiYZj1Qvb3OnnV5hvBGud_PAISP6Y1ASpH_NQTJK71xyf1FkDXqO8Kp4gfhJtQo5DUI_jfy-8phB41y6ALZMN7LPuKkStVJxjkW1iU4wRXNj7CwtIK5Mx7GZkJlfkPujpD7-Q8yk0HV_KSM6CNxHiOD_35FUbL52X9nBGkjX83Fl1nyMSq17wu1JPCT2VbEpzYVPejgx7VQrjeiPLM7YY_K6j09sltXOJhaZmOldHo-XuGrhXzMGjS59RUKxc74mCnqzdFwsyGxzwbohcryx3vbtsPLVM8UG5ZtpNdIPL3b7Acdn530RqBKwyibUw7q_ag-A5r4u-mbhuV83ZipdklVBhqmPwI7a53Tmr-1IF09ejcJfaycNRS9pAws1R0VEQco6KTod_s-wm7PFUmMnf6OR1IuMP6Kb0VSGw8mvz4W_IqDtbYJ8-klK3BB45Hgh-LnOATCA-QHjkt6Szh8IP5cBohH_ijykfntmOqRUATbwHfeflJiN0l1EpwWF9Jo9M5e9md_VFNh4YEliGsdKk8xyCLG-Ss21rTqrLkRm0LWO9DYHLcBbhNwdwZ00xgumxQ-8zp5dMYDImCxA4n6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرفداران حکومت یه بازی ساختن که برگرفته از بازی مافیاست و فقط نام نقش ها فرق میکنه.
در این دور از بازیا ترامپ برنده میشه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71226" target="_blank">📅 11:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=Y0bx93zd70U0rezGE7Rp8Hof5-L6dLCf2Jufz9QyamnVYkoyHQT89_Kkj4DzLZ6RSNTknLp9NLww7XFhmiwRJPXCYju_K2iWuBvcfDD5c7ewGA7cTjTljqYOfmFDpBmj_xyDaBvlXxezCGEjjoX9kjnVVd9LDeWfzMPo6iZEXdIuCsyEJDK6DtL019IzV2fR1bxrFOU4vUglFsLHxciUKPOQifV_7Pn6yMlYtCbB3ZvXv-3cfya2rfikTCNU3upS0JhFkmjMXKWoK-T471Lk8Ndk_rQ4vuzG34cR_lNDuaa_yfeRojkyHYvQlrk1Lw6slZkEguiMJBLF_ErYtCmujw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc54f259a.mp4?token=Y0bx93zd70U0rezGE7Rp8Hof5-L6dLCf2Jufz9QyamnVYkoyHQT89_Kkj4DzLZ6RSNTknLp9NLww7XFhmiwRJPXCYju_K2iWuBvcfDD5c7ewGA7cTjTljqYOfmFDpBmj_xyDaBvlXxezCGEjjoX9kjnVVd9LDeWfzMPo6iZEXdIuCsyEJDK6DtL019IzV2fR1bxrFOU4vUglFsLHxciUKPOQifV_7Pn6yMlYtCbB3ZvXv-3cfya2rfikTCNU3upS0JhFkmjMXKWoK-T471Lk8Ndk_rQ4vuzG34cR_lNDuaa_yfeRojkyHYvQlrk1Lw6slZkEguiMJBLF_ErYtCmujw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ادعای عجیب یه آفریقاییِ سیاه‌پوستِ ساکن ایران:
خیلی از کاکولدها به پیجم دایرکت میدن و اصرار میکنن که بیا وارد رابطه‌مون بشو و با زنم بخواب!
حتی یکی‌شون می‌گفت هرچقدر پول بخوای بهت میدیم تو فقط بیا..
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71225" target="_blank">📅 10:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjmDuOqrxz7GKRLKLUTxQunYyPyBsCdvlQOU8DqpJ_EKQ-9uL3aDhXDvvi77ejFubFIFQpOzhk5R6sWRTxupnL94EosMnRAU9CuylT88PLeR-dXdti7boZ3jWhBsoiARnBP9m50MVkD04MrwefUcPMF0P5uSzUq2vTJzCfJyoUs2-ka5-0c6QeP4Z5b8IZhVQHlBCjJHTBqXZ7CAgagtj-k0v3BEpJAf8saHMgym9xuvjLVJeRIj9F4c3dWWWtktfVWDaDAEmDo8KWugTWBod775bNp9Cuj7Z075B7Hntrg6zkn3tkX7cimzMXCH_UApNWQbPzaBBbfF1EnSk4sIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
شاهزاده رضا پهلوی:
هم‌میهنان،
جمهوری اسلامی بار دیگر با افزایش قیمت بنزین، هزینه بی‌کفایتی، فساد و جنگ‌افروزی خود را بر دوش مردم ایران گذاشت.
همان‌گونه که در پیام ۳۱ مرداد گفتم، گران کردن سوخت در شرایطی که مردم زیر فشار سنگین اقتصادی قرار دارند، اقدامی ظالمانه و خیانت به ملت ایران است.
به رژیم ضحاکی و رهبر مفقودش می‌گویم: فقر و فشار اقتصادی که بر مردم ایران تحمیل کرده‌اید، نتیجه مستقیم سیاست‌های ویرانگر شماست. منابع کشور متعلق به مردم ایران است؛ نه برای پر کردن جیب مافیاها و نه برای تأمین مالی تروریسم و جنگ‌افروزی. اموال غارت‌شده ملت را بازگردانید و حمایت از تروریست‌ها را قطع کنید.
گمان نکنید با کشتار ده‌ها هزار میهن‌پرست توانسته‌اید اراده ملت را درهم بشکنید. آتش خشم و اعتراض مردم خاموش نشده است. ملتی که برای آزادی، رفاه و آینده‌ای بهتر ایستاده است، در برابر سرکوب، فساد، بی‌کفایتی و تحمیل فقر سکوت نخواهد کرد.
پاینده ایران،
رضا پهلوی
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71224" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJkSsTHNCl2zSeo51qABuqqRBECuQiMFFzy69QVOxURMnB4tYE5DogdDR_IZSn9lZIAFuQXZ6fa16yipKRAcjsRw-OglfHkGPbZg5WfIAVxmsjTGc6DMWAhcCZ41-SUQOngTayGCyz_a_3X0lPahn_vNuHz4-y-JBj1orHzVrwCIe-UZF_vtAaWtNTWGP9EurRLkO4-mjLgw4q5QR0zxiO5fk1kku4cpSlxjbm380f6J0RM-BsiDjy7LffqPKXW7uJya74LYzVglIlW1-PSf1CXJXUmNf1hmoz-9bES1Ov3cZAU1MsyXT6IDJSecxQeDOfLY0p3KFX-WLG4k_DqMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71223" target="_blank">📅 09:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=MS4S2YFmlFsR5SFoZBBEWyOIRwOO5_0jy0AY1qYohE2sJ2ZoVNGEHmxIJM6FsCHWj6PDkVO9k0fSnXpNxCE3kicaEkZHXgYKIINUl6XnK5mRXtVLFrexhJVDlpyvo2aCXLEpt4c2P-sfcaoa_1rB_I7IZ6gGvNMzCIkY7I9eJPpoNx4xAyk_pZM0Cea_DYO4wRTZC4F9ZORQjNVRWg73XPj-c08gsYjCHnzLajUvAocjQzwx_qUMw1-cflSwRazumVRhkUAS20BVNyywwZ45ZEK9Rv_RJMJwXzTxVpAWBmzpXCYsIa1G_E90J02UvlZvrGpEfyH2Qyjg0izDNI3ylA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924d85f6dc.mp4?token=MS4S2YFmlFsR5SFoZBBEWyOIRwOO5_0jy0AY1qYohE2sJ2ZoVNGEHmxIJM6FsCHWj6PDkVO9k0fSnXpNxCE3kicaEkZHXgYKIINUl6XnK5mRXtVLFrexhJVDlpyvo2aCXLEpt4c2P-sfcaoa_1rB_I7IZ6gGvNMzCIkY7I9eJPpoNx4xAyk_pZM0Cea_DYO4wRTZC4F9ZORQjNVRWg73XPj-c08gsYjCHnzLajUvAocjQzwx_qUMw1-cflSwRazumVRhkUAS20BVNyywwZ45ZEK9Rv_RJMJwXzTxVpAWBmzpXCYsIa1G_E90J02UvlZvrGpEfyH2Qyjg0izDNI3ylA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک سرهنگ ارتش :
از فرمانده‌ی کل ارتش ایران تقاضا دارم، یه قایق پر از بمب با جلیقه انتحاری در اختیار من قرار دهد تا خودم را به ناو آمریکایی بزنم و منفجرشان کنم
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71222" target="_blank">📅 09:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71221">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=VHhODgeA8YwVnU6rfw3kcAbaj_nMSs1cpx7aeTthMDUnXgWvRkAXkk15PUYGSkEbU1KcH_5FnlguaPky7YLuZcGcjYYqQimgmVvYh1slOAgbP8gpdZgB0cN-D_i6OujyktLlEbYMTLIECskilZ6uJ9qiwK4qBcLwD9DN3lc5QZlrEaX0xUQtORNVwPbwiveIa4z7XlQrHskAFt54t4iRB70lLGGo_b-yaUD06UXnRmhwa9OOMBQzIpWIh364So_q1-c_QkXrHEw1w-Hhln5n9wYqvAYIdOtKQ1xifp1n-7tqZa2md_XrAMym2qYirlZDdiQTA3ZOZ9t79_OD0mHIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26767c2cac.mp4?token=VHhODgeA8YwVnU6rfw3kcAbaj_nMSs1cpx7aeTthMDUnXgWvRkAXkk15PUYGSkEbU1KcH_5FnlguaPky7YLuZcGcjYYqQimgmVvYh1slOAgbP8gpdZgB0cN-D_i6OujyktLlEbYMTLIECskilZ6uJ9qiwK4qBcLwD9DN3lc5QZlrEaX0xUQtORNVwPbwiveIa4z7XlQrHskAFt54t4iRB70lLGGo_b-yaUD06UXnRmhwa9OOMBQzIpWIh364So_q1-c_QkXrHEw1w-Hhln5n9wYqvAYIdOtKQ1xifp1n-7tqZa2md_XrAMym2qYirlZDdiQTA3ZOZ9t79_OD0mHIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان زمان انتخابات:
خیلی‌ها میگن من اگه رئیس‌جمهور بشم میخوام بنزین رو گرون کنم، ولی من بارها گفتم بنزین رو گرون نخواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71221" target="_blank">📅 09:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71220">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71220" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71220" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71219">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxKNxbGF-BrrjCl9dsY_K_54Z-DGn6kvjNt57XIHMnfIrOh7a7fC73dvSLZ5Vi3hY1RB9bcDuFFDxWT_hdlgnml5KIWnhBEIAWXUtq9RM4x2-404r9iHxxl34UBjvkeUo5i7fE_4elxSbvEfqPI0tKorcrPM8B59SEJQ0EFGAAkEtGyFyhLrW9X8ZxoU9IBJ_FOCz1CbNttA0SRM7QjcTYqLH3B8s4-Xe6NUfUMRWcWuwIJz5of6snaS4w-YLmWXpYulKHTP4jvk8Uj0UBbGBEuD2hkG93UrM5u1d_95FwnIYcW5yg9XsoGOA5Lho8qvt7RBKLbVxZY2ABO-2aOs_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71219" target="_blank">📅 00:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATzKpHmo1sCK48UvnAUk9KaRmEWt4g3ftyJwOwS6FvohGlFu8a5YNUOKAFOkIJbmiZeB2CxzKtc5YbM1X2GIn26TuY7VZLTVfVZtte_STs6AlaSfrG7gCvMW-OoedmqRqFmM0cMprDREKJQYd0DczR4ciGzDl6UFUk7sZKdHszoXvTL6Cqv4BYJDEmSwpN9RdQ8dxzl-m4KsBFrur58hhX1vprS74hWKDVqqP1O1BQU3uGruJq3KTdPMKKFFcN0RL9rkAC6C7rFs_T2fU-grcSo0zxzq6fTryqfIVUEJm-JWVILCeePc7JzBtiStctIbnxHiyiRwUorY1AJzgF_mkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U893axIWP5iNOQAZ4UzbX0orfcI_6N5GX2CueM50QuyCWJja1_xYsZrdFrJXLpTduHNRW62vbawxKQm4yxxjAJ4saa5wXsFy56ghV58Qo0Z9Ipv530ApPCo6WLnaRMnKNHMgB0uNTRS_59eKCYtmAuBgm9lTAAUqWcYctImljSKYY8EQbScCNmDFOTIxT_ZPxdjRHKLnPcK-e9VEsjeiZwxwVb-l96mqPBHvGSyJ7QPUyHvDghr_kBssLrLX3h7nZ9zj0rMgLIKrdZlrhDx1kSF47fd8S22KMWt0Uq6wF_kJlij-hTNOvrKEP0lRlbmryYHWj_AoIwFXmdrsrhWWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y90BVVq_6xqygw7qHuc_3Dix48H1KrcdNMtcLAijzsEFnVTjpMzperPZINmOOGx0wPnv4jhF_JU2rwPQrAGgew_G-6YFdVM-zCoE7T4rtWFtJ2YnTRM81km82L1dtWQYNCqITBpaN7NHRUBcJT85v4ZzVlbZtNstUOyofSnE-3lXQVbh2gkaJS5WjheEYffcPXE8NjPgam8AgaIYBDDhw6ijFTM71cYvLGlfiK36decN0vhZdRI-hzNcvZ15ahcw6BWj1LLs1AzgADJt-yCyFs2d2Ql13dXAC4MAVj6UUGo4ntvFxa4orw6TI8gjMtSZSn4rRw4-LXl6ArhEPKsaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9UqixpRmiMulphvtb0Mu0JCXgtFoYBGih7tpWp8sBA0JZ3qFkoxp2zcX9L-UREt0YSuUy5pWTXYh5JC1fPoSYmjwuX0bB50jca062QwU2mHqQ1fG9Y8iPAXKGJrGkvy4ZGx3_r-z-loAtMBMKG-kRhePOn8XQUlQqrX8aC_ge5hzgS7Gb0RO_AKgRC0h5J1AMlzTBnKozkuHDpMDmF01-yWs3Rr5yYKUC0wQMnMb6xQMCXvEOXhGyFoTX7grhgWje2yO-vdjkjX8v1bHbISmKkt74kvyPnyS2tbUVRojqcvBSROGjBYCg-8W35O8iadC5VwyyYGIBjITDZglBT7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGdcnAMOQtxaxxILuV2JCsSYr1q5azDvN4CbcpxmVG6tTRQunX_wqpXD55-h_GEcZlh5_C0fQHL305_cMWVFBRD9gE8bcUoJBwYSpl5IXXkWXLfl10wdHiyAZbfsCRLeNySCLXElgUFOgr2gquOa8MP2uUQKlf-9FBh8KtBadZYZB2Piz8wXolHJ0A98UWJAVVquFeyDAVbQgfYmR8H8i9jXc0yx4dZDx4hnXTepxBIwEHkE4MKVsqB4Kypl788ZKjX3plj4kS35oeZ-uhtd5QhSN2klBv5j27we76v_Yf0hrCBJMzU6DlBRTdBwAkDawKKXJ_Yd_P0Kk1LL8Wk0LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ:
۱_ایران کشوری در حال فروپاشی‌ست.
۲_خداحافظ جزیره خارک.
۳_ارزش پول ایران از بین رفته است.
۴_صادرات نفت ایران به شدت در حال سقوط است.
۵_ حجم‌های نفت هرمز به سطح قبلی بازگشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71214" target="_blank">📅 00:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71210">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlJodFilTtsht0UdrsgXpZ9MldCYUn06AxWCkJ6R9iZN0pPRl6E-Jwf9iu8-tN3f1TzsbfhHdOBZDXs_mMYTn8dS8nrQzwytSyDQx6OIYJKWGbJBdpomECibbE8hH8lDU3554kr7H7vhJLAPJZg05C3tvgWcoszkXby7pbGb3WAlIyGPZoS3q2LZgU7OSTsp1FRS8P9MaQSt-gDL4Q3VcomZLG-VSKWdJl2rQAWcK729rCsEVLZvZP27lt_yA7gdKyvG3CIO9_DG5tZ97gYWBwqDQrVKOyZ49SWl5xsV9P5XW8nwc9SGLP0YdMzhQ-My76G2-K9-O-ZBU_3Vs2MxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fKvBhlPHK-RX1Yd2t40vUKiMOR1WyTnbbi25dM5iNSU8Gc1fGCXdqFl0rXbF3dAKiMkRV2TCS9aHfyP9CM7YhFhrxLx-IR08amUUerJB_g0Nvk_FHNZ47YVfNs2roY4eTwHsfJu-Q1VD6ebMiNOOgSyL86srl6fGaE3f3PSzDQ6AGUR6fGMbudRg9wy4txbxBdmPJQ9s1-mUIDt12YFw01Y_nerqdVCKS8gs4oHRRSGoi7SRp2t5QYUKamNLqCpqh26E1-nX3dhq51kzPfKXNeT-aOBONVdqwhdk5sGT2YQkWGdZvh9S8GEfiJEpOASITTHkx2DswIeuFyctNr0vyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ در تروث سوشال منتشر کرده
😟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71210" target="_blank">📅 00:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71209">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=CjETC9lWpmSM5rV_U3IodbORoZV50qws7kjbEd2LVIZyiUx3NBwNc8YESJhyoIbIQ0QiW8rXSbbhqDGgdKnFKdesrhJpDtTDEr-x2-FGFSB2jbEL9oVw2Xr6-uLTZ8EwxGjRZM4dQ7coFtw4K3Jego09Oqj9n0A8d1aaOLu0ORkaJU_tsm1C8hsKnhEOtoZwiOzI9M_gWn_dWp3MaaV39XkAA2cwqaNZKvPiDfmsxo9KvcflgIuOqo6GoVS4n2RvzzG6LEZ-3DJr8MuyCWIbI2PparD4c3Z87sV-8NdP1pctuQk9kP0bcNXqMzLyMUbAftB8NID8ZIyYhxVoQTiijQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca8942d62.mp4?token=CjETC9lWpmSM5rV_U3IodbORoZV50qws7kjbEd2LVIZyiUx3NBwNc8YESJhyoIbIQ0QiW8rXSbbhqDGgdKnFKdesrhJpDtTDEr-x2-FGFSB2jbEL9oVw2Xr6-uLTZ8EwxGjRZM4dQ7coFtw4K3Jego09Oqj9n0A8d1aaOLu0ORkaJU_tsm1C8hsKnhEOtoZwiOzI9M_gWn_dWp3MaaV39XkAA2cwqaNZKvPiDfmsxo9KvcflgIuOqo6GoVS4n2RvzzG6LEZ-3DJr8MuyCWIbI2PparD4c3Z87sV-8NdP1pctuQk9kP0bcNXqMzLyMUbAftB8NID8ZIyYhxVoQTiijQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دو عدد سیب زمینی 100 هزار تومان؛ اینکه قیمت یه دونه سیب زمینی بزرگ‌ به ۵۰ هزار تومن رسیده‌؛ یعنی فاجعه اقتصادی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71209" target="_blank">📅 23:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71208">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=lGu-5mLlLmSEa32_-RxCk5DAgAHWhVtkZwk1PNspTzmNwNrF1T5GJ62bdFdF3axvfO2kO7JOsu9crQ8fBvkf7Qj0AjgVo8dt2AcRZ23ILV56GQnL77B0oOFQSRuaGDgdS3dI5s81LGwmqV2yUmjk3iJP9V8VNCB17STxz9QrceUhjmjCPthIsItYWmwpOVpp7LcCMOT1HtbkxKqB3N8wu51zz33eVUwP1dX2qDMyATNG2dgoc8QtzfhY1BfeDtqorV8c_reJOdih7krTN6QCSSsBB-P8wWlQpXDplNcY1zS0ekiRghCUsJQx6Mh0_SQnERdzieI0B5CPHbYFIeHyQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a65cbcd011.mp4?token=lGu-5mLlLmSEa32_-RxCk5DAgAHWhVtkZwk1PNspTzmNwNrF1T5GJ62bdFdF3axvfO2kO7JOsu9crQ8fBvkf7Qj0AjgVo8dt2AcRZ23ILV56GQnL77B0oOFQSRuaGDgdS3dI5s81LGwmqV2yUmjk3iJP9V8VNCB17STxz9QrceUhjmjCPthIsItYWmwpOVpp7LcCMOT1HtbkxKqB3N8wu51zz33eVUwP1dX2qDMyATNG2dgoc8QtzfhY1BfeDtqorV8c_reJOdih7krTN6QCSSsBB-P8wWlQpXDplNcY1zS0ekiRghCUsJQx6Mh0_SQnERdzieI0B5CPHbYFIeHyQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سعید لیلاز، اقتصاددان و کارشناس اقتصادی:
«کشور با تذبذب و دودلی، مس‌مس کردن و فس‌فس کردن  اداره نمی‌شود و حکومت باید تصمیم‌های قاطع بگیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71208" target="_blank">📅 22:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71207">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnTXi25td1cw0p9WM4fPbdIE3SGYdxw94lUfgshJNYBy5CLV8c6yZEenRCD_UcpgccSz97VsNw4aWINmS9OvlWeDI7oLkG_ofm30OPlBIQOIAiAnclGhqg5E6bFHXYkDsheUhMM-TRHu8fH2-jseH4AXmZkLvfED3NG7O6UweU0mjoW-SO4xE3p88ae7bYgblrWL2s2nOPnMZh-shi4yeubT30anYhPZqWEJ3MXIml7Zoft9EiJrBUf6qKCF_bPjfHphCPZm0Vs4hIwCPvyohlhDb9gfr_kyd_9ESuIHFy_q4ZoPuQo2SnIZ5gkYV_bFlFkVuYWUXUwj1b8u5WqZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث که اومده کلشو جای نقشه ایران گذاشته
😟
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71207" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71206">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=CZHinBPwDtHGb5oANIAwS0vmf50DhP7KqLgQ13-oF1fVestIExFsaFWZ5fgIWugy0hxGkraUzf-bsdYeSX2rDNTc1j4bdrLd8Ejip-foYnx9sXsKM9oF30VUNR3wBpviyq3cdsSED-3sVt78wLOpWapbILWN0s_PXkALih45AEaKusC-QxEmagtvai3U20_HVnEtDPvdkeZ_2nt9fQ4WGu0DvDRqL4WZtuiYl2ol9HIbbemPRWBN_OwWbRYbwJqM4LSomwUFlPjFeymFDhRDHzZiONiQQBFu3RaqDNwDIhMsIh2r_cMJplCCOQGosWez35NVEv5BQInEsCLVyA9SvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6400639d7.mp4?token=CZHinBPwDtHGb5oANIAwS0vmf50DhP7KqLgQ13-oF1fVestIExFsaFWZ5fgIWugy0hxGkraUzf-bsdYeSX2rDNTc1j4bdrLd8Ejip-foYnx9sXsKM9oF30VUNR3wBpviyq3cdsSED-3sVt78wLOpWapbILWN0s_PXkALih45AEaKusC-QxEmagtvai3U20_HVnEtDPvdkeZ_2nt9fQ4WGu0DvDRqL4WZtuiYl2ol9HIbbemPRWBN_OwWbRYbwJqM4LSomwUFlPjFeymFDhRDHzZiONiQQBFu3RaqDNwDIhMsIh2r_cMJplCCOQGosWez35NVEv5BQInEsCLVyA9SvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
مجری لبنانی:
مجتبی خامنه‌ای، رهبر عالی و ولی‌فقیه، اگر به بیروت بیاید باید بداند که هویت ما عربی است، نه فارسی.
بگذارید این را به روشنی دریابد: اینجا بیروت است، نه تهران؛
اینجا پایتختی عربی و آزاد است و هرگز به پایتختی فارسی بدل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71206" target="_blank">📅 21:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71205">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
⭕️
#فوری
؛ نرخ سوم بنزین تغییر کرد
سخنگوی دولت: نرخ کارت جایگاه سوخت از بامداد سه‌شنبه به ۱۰ هزار تومان افزایش خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/71205" target="_blank">📅 21:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oCU-kDMGVNquCe1HUaoxycQXNWYUw9sScCVuqdS8-0rApJn2aDA6JpLTrb4x3rIHK_aClN2mCuZM88_4BeXEUj7sgTNvBykJN4jSvzU8Ap5T4AnMRzMfv1FNvBW6raM9ErI6dfLevmrb2BCdwX89RkuoOVBslgLflvhnd65xRhUrigzLEG44hoabCd9Tpj3Q2XAUOtkhyD_ZCiw51FQtrTG65g96MfjR4W521cjlYEmb_5_v_rna5YdjQFjxih9wcHDtKpRiyaokfjKfM3f4k0F5I9uzkRQvcL4bC3juZVnrcFAxerj5pDSoaRNZJ8qIS7v655lGg0szVGnSUpOnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gomWnydVJf5uA-QC67JPDb8zyZHoFT3LZpllj7iMZMbcDJfeiZbKMf7rMupKDLGw5eHcXElU0QU4ffQWO05hQ9BKvJ7uRkQ0cya1DmdnIBUu14zpOWT3pHrbDlSFmhaxpOl4OTgHfL2tVBzh8aR_TgcbExXvcK9atWTvlFBG36yEqMo5zpnPjy02dEv4Kq1HjMKYODmb-S4cCK03NBMUkOvHpi6tqVzGJGg_HMIOT9kUWC0qsQMjk7JX35FeqaXSJ1dpSWrnzfZTmgUVZ26zV7HiBCg5CEVekdpfuufeE1NjBgmIkT1UKLaOl34zXvNxsSkLqalgxpqxrg0MG1F49Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=dMCkOcMXYxz7LdULna-Du24MJOBaFhnZiR8cIkIRWyDkwGityplKQnWDZs-VN-1p9vA07ndKJunol1bjIgbHYisdyTGXCwHKX5fOeC80WdZN86LrrDWX_ibeafbboRUYJPgXDIFM46rgf2K-Mcjf6hB7S2mQtVl2ZT_ydB3KzlOA3lAkX40sVIGJWM2BHid-lTeL9bTLLn8zyHm3h30mU3oYHnHjUhXYQ6HqzN8DtQQuvu7srT4YvivuAUIxprLp2aOj2zPGQdXEbak7kKsoffTjlqSg-6Y6U_80f1mAYtVT5DNHElOHAZXqyz906lMMmm1VLGHbWzSH3tBKJkxJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98460c35d8.mp4?token=dMCkOcMXYxz7LdULna-Du24MJOBaFhnZiR8cIkIRWyDkwGityplKQnWDZs-VN-1p9vA07ndKJunol1bjIgbHYisdyTGXCwHKX5fOeC80WdZN86LrrDWX_ibeafbboRUYJPgXDIFM46rgf2K-Mcjf6hB7S2mQtVl2ZT_ydB3KzlOA3lAkX40sVIGJWM2BHid-lTeL9bTLLn8zyHm3h30mU3oYHnHjUhXYQ6HqzN8DtQQuvu7srT4YvivuAUIxprLp2aOj2zPGQdXEbak7kKsoffTjlqSg-6Y6U_80f1mAYtVT5DNHElOHAZXqyz906lMMmm1VLGHbWzSH3tBKJkxJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
حملات شبانه جنگنده های اسرائیلی به ارتفاعات علی الطاهر و نبطیه الفوقا در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71201" target="_blank">📅 20:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71200">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a237cee509.mp4?token=gUvd-e7NRfQblGg23gQIecGyYGU4gXy3dn_O7j0RD_1cMTZcHGwtQkbkP-okQRDAwgp0wu0fP0su0JVPiPNXfxjWQgEibsLPDk8V74-PFTN382K0OnyviLid2xU6bk4d_PlatbV5iWlitEf31tftwbZfvWXSGtakCXzuurF70TRHwfjD6t6y-EToOUplKzIgQ5lhhb7kbJ9EaBIDnXLtZVxMuTjlW0tctL8Gibxk9CJx1pbHVo63cy-qG-XSGQLokYaeweDwNQPwgBxBIUzvP97HZZbOJdjfjJ1EhS-RX9KzwZIi7RQWGyZ7byL8Kk-P8kc42hbRW0ZD09tm_ZIWWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a237cee509.mp4?token=gUvd-e7NRfQblGg23gQIecGyYGU4gXy3dn_O7j0RD_1cMTZcHGwtQkbkP-okQRDAwgp0wu0fP0su0JVPiPNXfxjWQgEibsLPDk8V74-PFTN382K0OnyviLid2xU6bk4d_PlatbV5iWlitEf31tftwbZfvWXSGtakCXzuurF70TRHwfjD6t6y-EToOUplKzIgQ5lhhb7kbJ9EaBIDnXLtZVxMuTjlW0tctL8Gibxk9CJx1pbHVo63cy-qG-XSGQLokYaeweDwNQPwgBxBIUzvP97HZZbOJdjfjJ1EhS-RX9KzwZIi7RQWGyZ7byL8Kk-P8kc42hbRW0ZD09tm_ZIWWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زاکانی:از وصیت‌نامه علی خامنه‌ای خبری نیست، احتمالا در بمباران از بین رفته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71200" target="_blank">📅 20:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71199">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90305378ee.mp4?token=p-g05i3Tch5EjJZaApj4QJhxwlUsrwzDsoD-EUEKXOuyaRApvf1NL0vaxGM_teEOOcT90zMyl4hkFg5tQQZfjbzM8QxasE2MRYXZWX_FanUFgdEzEMISWSzsBOaDV02kMdG08m7FO1rBsaIxZmDPOT7soXbJE6etDdtXwxzcmeYCN8C7Wsuwk4e5RSdHSx6Dqw3XvCRz35UvgFIaMoJTmQKADhC1Mb61F8b4Z0-VlZ-p8E-oS5c7O7tt-QQvVNrYlSB3lTShLyEZUhIu2VpCY4t7aCjd5xYN85A9GIBa5XxDHZAAejKfieU7w5AuWe4YssmLk5NlJhq4-udWLp4TMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90305378ee.mp4?token=p-g05i3Tch5EjJZaApj4QJhxwlUsrwzDsoD-EUEKXOuyaRApvf1NL0vaxGM_teEOOcT90zMyl4hkFg5tQQZfjbzM8QxasE2MRYXZWX_FanUFgdEzEMISWSzsBOaDV02kMdG08m7FO1rBsaIxZmDPOT7soXbJE6etDdtXwxzcmeYCN8C7Wsuwk4e5RSdHSx6Dqw3XvCRz35UvgFIaMoJTmQKADhC1Mb61F8b4Z0-VlZ-p8E-oS5c7O7tt-QQvVNrYlSB3lTShLyEZUhIu2VpCY4t7aCjd5xYN85A9GIBa5XxDHZAAejKfieU7w5AuWe4YssmLk5NlJhq4-udWLp4TMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇵🇰
بلاتکلیفی بیش از یک‌هفته‌ای صدها راننده ترانزیت ایرانی در نقطه صفر مرزی پاکستان
این سنگین‌سواران ١۴ شهریور در ویدیویی گفتند که بی آب، غذا و امکانات بهداشتی به حال خود رها شده‌اند. با اتمام سوخت یخچال‌ها، بارهای فاسدشدنی در آستانه نابودی است و گمرک هیچ‌یک از دو کشور پاسخگو نیست
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/71199" target="_blank">📅 19:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71198">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بیناموسا مگه نگفتین از امروز برق نمی‌ره؟ رفت که
#hjAly‌</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71198" target="_blank">📅 19:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=pDwsjx6wIc3IgHVB9IW4ZQ40bLc3Uh9URnEq4wDlxFGDs6JNrVCPngt3sqP9kln0qHUn9FCVXMdAxfz4toLVjOKcJwcxe1KXcG4GWsGGeFSj9ogguwhYKFeMgYdpK3iFmG85-ONgeQ7QxiVrIcXbiMoQl3oeejdMy587iQJdU60r9mEXMeGQ6MxLInIjxFqztajTNzbMgNxxLy8QG5vFsMr6JbxOxTRSUfDIqJfBQ1Y7s5t5zjJ249z8P0N9uSm2vlPtyj2ImfaqzRLkRFY-de0Bi2nyz5ZX2wEFVA0fJ9YR-bk2GLI-tMNvuAOGrjRetDFwzC2lz3wbFAFpBIxWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd3aa09393.mp4?token=pDwsjx6wIc3IgHVB9IW4ZQ40bLc3Uh9URnEq4wDlxFGDs6JNrVCPngt3sqP9kln0qHUn9FCVXMdAxfz4toLVjOKcJwcxe1KXcG4GWsGGeFSj9ogguwhYKFeMgYdpK3iFmG85-ONgeQ7QxiVrIcXbiMoQl3oeejdMy587iQJdU60r9mEXMeGQ6MxLInIjxFqztajTNzbMgNxxLy8QG5vFsMr6JbxOxTRSUfDIqJfBQ1Y7s5t5zjJ249z8P0N9uSm2vlPtyj2ImfaqzRLkRFY-de0Bi2nyz5ZX2wEFVA0fJ9YR-bk2GLI-tMNvuAOGrjRetDFwzC2lz3wbFAFpBIxWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
پایان این رژیم در ایران نزدیک است.
این رژیم ضعیف است، برای بقای خود می‌جنگد، متزلزل شده است و هنوز مأموریتی ناتمام باقی مانده که ما مصمم به انجام آن هستیم.
این امر در نهایت چهره خاورمیانه و مسیر تاریخ را تغییر خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71197" target="_blank">📅 19:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIIShPkuajGGUxhYSJeakDv_gvORs4rObsjS1QxGVb5SvLD5IXjtn379CPMryH2tUurin03GNwkHjbkaTAW2-ZmChuoIZlVpB5zpqTvy40QXazeDLuiDiLgozwm2VO86YCGs1NWc5lSFPWaSYePZ1u9w8elrK-EIw2ssSHrRZYwgpk6UQqmC-R6NwMQaMDSfAF8LTNeHidVppQV4M_e3mICeYz5x9oW60H21WliF3wEuir8MuvhUmsWPhxsW-coDMSbqrxrEifIUKYGjclz2vljXyEbFHj53YcV9-q80WTFu9QksZEVZ4Ea7nOfQpeAioZPkH8oDoqCsi41bskSxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیس قالیباف به بسنت:
چرخ‌ها آماده. گرم کردن قبل از پرتاب:
دیزل ATH: فروش فوری
بزرگترین طلبکار شما: موفق باشید با Yentervention++
80میلیارد دلار کاهش می‌دهد: نام نروژ را به Americaway تغییر دهید
استخدام کم: بدهی به خدمات با DO[Israel's]W، طبق گفته عروسک‌گردان‌های شما
اوه. طرح نقطه‌ای فدرال رزرو قرمز چشمک می‌زند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71196" target="_blank">📅 18:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BROPiN9PsRGNJEFux7DIKOW66Mb8ISbecuhRKt-azuvTkw-NsPTQAL59B3H1h0hzOTcFZ8bAvuqCpcmkaP0sylOxIQssrg25aRLv1VTDE6bQd3VET0ApvPzuxnhwBJFMkM8ZdYzUDle023Z4jZK-VL9GGcRjdCVMOubYJEMMuqOB6hcQb3RZGLbFSUcnEBsCNaEia590_Rn0q5i12_TZGx0wXMEDyT2Wi-q335BW-OLgnvAYw83u7EDHmGLvid4EvLgcvizfhm-1rZE4nUFtz9aSL_vyn07rY5UPu2eBjrN1R5zVKa6sPDJXgwYLpcFXx3yi4bKy5Q-ZDS6fG1O33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
گویا املاکی موهاشو رنگ کرده
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/71195" target="_blank">📅 18:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71193">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNjdLHBlwUJ_7kAgb1f3hBKrUALB3JYfXmNrKYaWBQ9VIHf6wh8rU9Y_OV7rQbBK1NPPyp6v-4nikNqH6eCICEZk28oJtet1zEIBJqfB0WrDWX0C-_huvR854UvICEzdvDiWfYiAoqgZ5l4k0xfdyRic4cVaY_Onml7V-ZNEjz9ToXSw0BlJHyubdPy66F39bKE8GkrZFdd6GMLBAII2Gr5LZVJzd_Vqk1nA87PZ5lPOhjVJEaVjOocdH2A_i15hHCe0T-86LpeH10QgbhL1EaHbXS9KcODSaZbSoY-1CNtc1x4HARRz1CHgdHu1cIrjk-D3A2ihjImK7nj9whHfKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=kbkAeSt0-tNjkGo5EjRIAQ_GFAdIatJCPidWjzCsP3802pmJhVdo4slH6aTT01Y9Jde4Z4lEFCU39ViOkRrnjKBWvm0L35pTdEVia-IiEtCkVoEbG5G7h-uK3yRIOan5Jtvmbeiwan8PY9963pcNlK4NzWYUi2WyiO6KPpSy6h0ZJeB-Pcef6IOH3vf8CGct_HqPqsDsTHS19ctCqHwnJKxXn0m6UghnR2TRAj3JCUOo8nyR8W3sKOqm-taczYSII8oe8qO5gA6pi-s0X7L03uz5HKsbuGutpjG6MruKoB8ImcnVIq1r2HYc4_Ce1lT2eycB_EU6OaBzNy_zU2OHog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385d0bbd1a.mp4?token=kbkAeSt0-tNjkGo5EjRIAQ_GFAdIatJCPidWjzCsP3802pmJhVdo4slH6aTT01Y9Jde4Z4lEFCU39ViOkRrnjKBWvm0L35pTdEVia-IiEtCkVoEbG5G7h-uK3yRIOan5Jtvmbeiwan8PY9963pcNlK4NzWYUi2WyiO6KPpSy6h0ZJeB-Pcef6IOH3vf8CGct_HqPqsDsTHS19ctCqHwnJKxXn0m6UghnR2TRAj3JCUOo8nyR8W3sKOqm-taczYSII8oe8qO5gA6pi-s0X7L03uz5HKsbuGutpjG6MruKoB8ImcnVIq1r2HYc4_Ce1lT2eycB_EU6OaBzNy_zU2OHog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
تو همه جای جهان هوش مصنوعی داره جای آدما رو میگیره ولی تو ایران برعکسه
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71193" target="_blank">📅 18:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71192">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=OVrQKDDVn-Ki2eE3EEeDBdnl9Av6ptk1eWRv5gGsj0M-XwZK5OQfl5BfuSOg4AoHQ-v_N3adH1cJbkHJ4T1jL3X97WIHe1fmkvaikZGG-eKOfMRxcO8WjbBem7f8GGPgZnFlN00yLXkAWGS943k61d-rhhDdCppl7zyBxD33iIxb3sfjiWQJhdKbQRsm7OR8Sx5vgliSDWeW5DEOt05nn0i-ICPtpt2dA5n9SfQdbjZ0x4lFsOYw_4ANB_NjnFCw4PfQcsr-4L5MRxQ7-w8Xped4H2zsJmL1Wspq0mZhlpwDp7812lqamvxBgnKfYiIUS6iZTLeGJ01qPiOsGTILNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa47cd6f21.mp4?token=OVrQKDDVn-Ki2eE3EEeDBdnl9Av6ptk1eWRv5gGsj0M-XwZK5OQfl5BfuSOg4AoHQ-v_N3adH1cJbkHJ4T1jL3X97WIHe1fmkvaikZGG-eKOfMRxcO8WjbBem7f8GGPgZnFlN00yLXkAWGS943k61d-rhhDdCppl7zyBxD33iIxb3sfjiWQJhdKbQRsm7OR8Sx5vgliSDWeW5DEOt05nn0i-ICPtpt2dA5n9SfQdbjZ0x4lFsOYw_4ANB_NjnFCw4PfQcsr-4L5MRxQ7-w8Xped4H2zsJmL1Wspq0mZhlpwDp7812lqamvxBgnKfYiIUS6iZTLeGJ01qPiOsGTILNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دعوای دو تا ترنس تو پارک لاله تهران!
فقط آخرش
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71192" target="_blank">📅 17:34 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71191">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=Dr4bxDSF4A0Shf5PECBdUjzv1Lta4gakXzSIF2LtLESn960N59bwRYfzg4P436k8jYkQl1kiWOy5RYrxg4Ib4B9FyCPZhNbLHKW9nnFvz2LhV1v7a4Zey6JxNNSaUSZmsNa_yEBL3W3jnDgzyWFZsoolZWBREtmQkiPC9XoXhEZIsopqTVPwEhol9Y2cllfy5QQf_yjKK6zeH3G2rKR6EiKV4A33V3AZuTNn0hnue0sAudLJfx_PeTTj4HWb4CsEnHa_uOoq7uAhxmYDqm9df1iV-24uzvITFHCp6Cp27rE2e1LQvuRdfAWUC06-4eJ0KDQQUTFUO8PH2n3X3UBJ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=Dr4bxDSF4A0Shf5PECBdUjzv1Lta4gakXzSIF2LtLESn960N59bwRYfzg4P436k8jYkQl1kiWOy5RYrxg4Ib4B9FyCPZhNbLHKW9nnFvz2LhV1v7a4Zey6JxNNSaUSZmsNa_yEBL3W3jnDgzyWFZsoolZWBREtmQkiPC9XoXhEZIsopqTVPwEhol9Y2cllfy5QQf_yjKK6zeH3G2rKR6EiKV4A33V3AZuTNn0hnue0sAudLJfx_PeTTj4HWb4CsEnHa_uOoq7uAhxmYDqm9df1iV-24uzvITFHCp6Cp27rE2e1LQvuRdfAWUC06-4eJ0KDQQUTFUO8PH2n3X3UBJ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71191" target="_blank">📅 17:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71190">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/45226525f2.mp4?token=drwFA8Ocj2gEJCJkylfr7TEFqQgLYhCYzmuPAbyYVzCsgIBEj4wrNSGHSHSwlM1ZfVHdnrYF9gMELyi1ZuU8VPdzAtRJ5hGPnQqxWIowHl4l1YwZpAQreG6bd1Y8cJJLecPD7ohl9MlKAsbcFPccs6qFR1OCCuZV2V_CuvJK-TC46GkM7mSS7GKuwWpBK5bUoYimPKOOgNBAKth8siyZrObOM--6-0oXQGdctYF0BqoQRtRpmlhorah5eodr6KhNW0GK-pw0SgGyJV9re7ICA_hrnDzhRCatSG31H6eBng6KORT3ii2K_AQ_-5GRy-cRF5i25dfpMyiu5M5YEqRbYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/45226525f2.mp4?token=drwFA8Ocj2gEJCJkylfr7TEFqQgLYhCYzmuPAbyYVzCsgIBEj4wrNSGHSHSwlM1ZfVHdnrYF9gMELyi1ZuU8VPdzAtRJ5hGPnQqxWIowHl4l1YwZpAQreG6bd1Y8cJJLecPD7ohl9MlKAsbcFPccs6qFR1OCCuZV2V_CuvJK-TC46GkM7mSS7GKuwWpBK5bUoYimPKOOgNBAKth8siyZrObOM--6-0oXQGdctYF0BqoQRtRpmlhorah5eodr6KhNW0GK-pw0SgGyJV9re7ICA_hrnDzhRCatSG31H6eBng6KORT3ii2K_AQ_-5GRy-cRF5i25dfpMyiu5M5YEqRbYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
راننده ای که چند شب پیش در مشهد طرفداران حکومت رو زیر گرفت:
عمدی نبود تعادل نداشتم به یکی برخورد کردم تشنج کردم جای ترمز گاز دادم و یهویی زیر گرفتم
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71190" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71189">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71189" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71189" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71188">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNF7jx352bc8CTCVCydvSAad11W8mVbAaeG0kUnNnT0PtW9scAQ4tAYS_oMei_TSs-W9hARnWPx5y5Sm7Mael78hteVHM9bxBo3EnlpO72oOMpHsdH3eAINef9xVOZZPhDjL-mj2NHTLMeEUg68RsNUIJg9n04wqro91ezdOhSfokAWCiFv99Hue1rXDFb-k84E9Z0k3exvsyFZH3LS6iKWr6Vx-zMtz94SCd4eUpvO8Scfrx6XFNS0PmsPw1izERz6-OV7kpXVZpMe2_0s6mhyCTTHg7kBsaQu0j_arqbEGDcTxBQAgjcMVJZ8Z6NMDzM7P1Wrt4bot-WkVODsM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
چلسی
🆚
آرسنال
⚽️
را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم:
چلسی: ۲ بازی ۲ برد و ۷ گل زده
آرسنال: ۲ بازی ۲ برد و ۴ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71188" target="_blank">📅 16:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71187">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YoZVT0O3Ecqa3sFaG0ldSX42zJp-21INFypc0BU2ZOhUWQCVL7axKTA5UY9vC7dMIz0Taxw5lKh3s_q8vKC9ewXW6WnJ4IuFGRjIGWIRnshqymCY7Osky1TZBawFnVw0z5qp5dmsThAu0JNduEkCxNtuWbikCSyawKEZH7ZADy7vXc7-3-UVCuJ8g0tGAOU-61LJ9CH3DVFVy3UBu61ifpG6-A7r1xD1h29WFS7pd-SaP6hA4tQW1q7cOGgk02XUVDW19okblNO8Wc7jG5f8VL30K7LSVQA8OFr5x2TX1wPbyb6o4iYXvn94RSfTmVtZHvJWON0DbIy8a0PV-lFwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇰
🇵🇰
پارلمان پاکستان برای نخستین بار در تاریخ این کشور، فرماندهی قانونی هر سه شاخه نیروهای مسلح — شامل نیروی زمینی، نیروی دریایی و نیروی هوایی — را به «عاصم منیر»، فرمانده ارتش، واگذار کرده است.
او می‌تواند بدون نیاز به تصویب کابینه، کارکنان این نیروها را بازنشسته یا اخراج کند و یا در خدمت نگه دارد.
دوره پنج‌ساله مسئولیت او دست‌کم تا سال ۲۰۳۰ ادامه خواهد داشت.
او با دریافت درجه «فیلد مارشال»، این درجه و مصونیت قانونی را مادام‌العمر حفظ خواهد کرد و برکناری‌اش مستلزم کسب رأی دو‌سوم نمایندگان پارلمان است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71187" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71186">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22246726de.mp4?token=v_pGHtX7OX5v9jh-Wdlw88FFC32RaW8TPdjD7jHDfdtE1-BVYd4lhbRAFPugLGY5yz5LMYJ8pQSqJH5Pw1Lc9lpmL8L7elQqOIx9XstahVEsbCq-XRQpS_14z5xn3fZwUcqISK18v6JZTBRxN7j7f03Yrb7vUPXCRH5eVm8bcFabzRpqp4ZzYwRoDoIZg-q07Zs3vy0Pc-A-yMRIIuKOJJQo3hzeurLNEcmeu3nDiz2XEyJXifCf3ITKzxzCSUM09vY5udUH05DraakO-g7DNCvlO5bSu63GA09wlujOYs4ToB9tucBeqci59l1xzvXmSE_BeerXvmHSfR6kl2AFag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22246726de.mp4?token=v_pGHtX7OX5v9jh-Wdlw88FFC32RaW8TPdjD7jHDfdtE1-BVYd4lhbRAFPugLGY5yz5LMYJ8pQSqJH5Pw1Lc9lpmL8L7elQqOIx9XstahVEsbCq-XRQpS_14z5xn3fZwUcqISK18v6JZTBRxN7j7f03Yrb7vUPXCRH5eVm8bcFabzRpqp4ZzYwRoDoIZg-q07Zs3vy0Pc-A-yMRIIuKOJJQo3hzeurLNEcmeu3nDiz2XEyJXifCf3ITKzxzCSUM09vY5udUH05DraakO-g7DNCvlO5bSu63GA09wlujOYs4ToB9tucBeqci59l1xzvXmSE_BeerXvmHSfR6kl2AFag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلم وایرال شده از ی دختر ایرانی که با یه پسر مکزیکی با هم وارد رابطه میشن و بعد از ۴ سال بالاخره به هم میرسن و باهم ازدواج میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71186" target="_blank">📅 16:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71185">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTOzBiqrVE_ukNwGT30vz_zZpYH-fW42MgMyUXAqWlQOlbdutxVhQG6hWG2-iQGmVnqK86FDPejj57sMREe9yIkiUuhCWZuKJfcTdO4XfAfvkegXkcx5sXO2ouJHbhyv2lyRZl9uPKCd634dhgBKNFHyApyrQlxktDQcfGaBsnxPl9QF6Dw-6qlGNMLFvczZN8DUn3Aq_an5bDSSDjrXNG03UIwwA1A5wSpIL_Dy7dAUzFIN7yXDMtHbhEtL-EzEwaLYXnKSWG191CO7yfO-l-tk75u5_YNOLw8xznQzdXebDx_ZW_RP55VLGIWI3lJr_FLug9XwM43anEWKu1Q3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیده شده در تجمعات شبانه:
قالیباف
:
علی الاصول یادت رفت
علی الطاهر هوا رفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71185" target="_blank">📅 15:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71184">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=cyxRG2a9Fdye_Oxqt5UzQsuySjoHzKdUWqUjjS0f61oMBaG39Fdnvgyq_SYlFvJQEN8uddXyOx7LtaFsPonN7dfiBmGPaiJCpEzcqE9QlxJ-AYElw2J-Axorzfkvl07cK_TWMqmmXzmNh0F3MmeIq1D6Clw6MsRU1fGqQuoVFS9iwbORl2YaB-oTX2jLWiq9wSaUCjzkQA1mwdYu9ACWuEBYg4YzXnAEGzHdxE9YHQdQtimUOrtIQ16AOy4nEullt3Mj8sSRFMemx9HSSwp8dvWy-uflRQ3AWzPEB6Aw64mzRhSrtZoraEliTvttivtrLGegO6GG1oeBfeUCdw4KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/64baa312ad.mp4?token=cyxRG2a9Fdye_Oxqt5UzQsuySjoHzKdUWqUjjS0f61oMBaG39Fdnvgyq_SYlFvJQEN8uddXyOx7LtaFsPonN7dfiBmGPaiJCpEzcqE9QlxJ-AYElw2J-Axorzfkvl07cK_TWMqmmXzmNh0F3MmeIq1D6Clw6MsRU1fGqQuoVFS9iwbORl2YaB-oTX2jLWiq9wSaUCjzkQA1mwdYu9ACWuEBYg4YzXnAEGzHdxE9YHQdQtimUOrtIQ16AOy4nEullt3Mj8sSRFMemx9HSSwp8dvWy-uflRQ3AWzPEB6Aw64mzRhSrtZoraEliTvttivtrLGegO6GG1oeBfeUCdw4KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو درباره یکی از جنبه‌های سختی مرد بودن در حال وایرال شدنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71184" target="_blank">📅 15:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71183">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=T_caYHE9CGW90V97V5yl-kTQYxznZFras0EdBFuKiI508V6Bno0pQSWfmFzYlN_tZh5fe-DvqkzOnEE2dySW4JnNFonqycwkDSYgY5Fbr-zQrXm9PtAx8nWv1DeqalLQKAMf1AotdoOO_5Y9U7q_eRVZ3oFkJ1DRSW1qJduHBuI1yHwL6lhxMzq5tWU20JaA89Ur6rD2lKF-Of0IfdD88vADAm8X8tTYZzViieAHo3e5_lwISeLSgxT0r13z_rOSD1SGkCHRtpTPGA1xgzg_3ia0EPqCDNtFJL1-6Yj3cLh1V3UIBbBy2DyCx6gMft8ZqpPO36Sr6r66vDwCZd-swYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c325a7591.mp4?token=T_caYHE9CGW90V97V5yl-kTQYxznZFras0EdBFuKiI508V6Bno0pQSWfmFzYlN_tZh5fe-DvqkzOnEE2dySW4JnNFonqycwkDSYgY5Fbr-zQrXm9PtAx8nWv1DeqalLQKAMf1AotdoOO_5Y9U7q_eRVZ3oFkJ1DRSW1qJduHBuI1yHwL6lhxMzq5tWU20JaA89Ur6rD2lKF-Of0IfdD88vADAm8X8tTYZzViieAHo3e5_lwISeLSgxT0r13z_rOSD1SGkCHRtpTPGA1xgzg_3ia0EPqCDNtFJL1-6Yj3cLh1V3UIBbBy2DyCx6gMft8ZqpPO36Sr6r66vDwCZd-swYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مراد ویسی درباره مسعود پزشکیان:
حساب اینو نکنید این متخصص قلبه. از نظر سواد اجتماعی یه آدم به شدت پرتیه پزشکیان.
گفته کارمند‌های دولتو داریم صحبت می‌کنیم در سراسر شهرها، نیان تو شهرها. مثلاً اگر کارمند بانک‌اند اولین بانکی که اونجا هستن برن تو بانک بشینن کار کنن. اگر کارمند تامین اجتماعی‌اند اولین شعبه تامین اجتماعی که هست برن اونجا کار کنن
😟
گفته دو میلیون خودرو میاد کارمند ما اگر یه میلیون از این کارمندها رو بگیم روزانه نیان سر کار تعطیل کنیم اداره رو یا بگیم اولین اداره‌ای که می‌بینن برن اونجا بشینن کار کنن.
گفته یه میلیون خودرو هرکدوم روزی بیست لیتر مصرف می‌کنن یه میلیون ضربدر بیست لیتر می‌شه بیست میلیون لیتر مسئله بنزین حل می‌شه
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/71183" target="_blank">📅 14:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71181">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=XS7qPBOEvmrHywsmCn98TtHDqzmMX59JtwoojvHefg9i0lg7XnzawIddVk2e9_qXq05agbYGivpH0togJCWEPhhY7WBcButqtuRv0h9PEjVh75_7nCGx1BiFhnWhhN7Wtsuau2EKA06vnLp2HALkQGK0E1YGxA6UbmxaRCF4w8EozZoHVYy27Nzn_O4QN5jkLKh7us6tTnm45-b42yeWBeQkfL8RQu4TXZ_4r8EQrZhayTlvnAo1lZFs_Dc0QHi4653Z0xVqDMJ-XNx2S7jFwCjEJCKSFQ5VGrvezEGQyig9nhqaIYUL238N-_l5MyvGImHhYsPBvlx_HfAxuvspOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c318eb355.mp4?token=XS7qPBOEvmrHywsmCn98TtHDqzmMX59JtwoojvHefg9i0lg7XnzawIddVk2e9_qXq05agbYGivpH0togJCWEPhhY7WBcButqtuRv0h9PEjVh75_7nCGx1BiFhnWhhN7Wtsuau2EKA06vnLp2HALkQGK0E1YGxA6UbmxaRCF4w8EozZoHVYy27Nzn_O4QN5jkLKh7us6tTnm45-b42yeWBeQkfL8RQu4TXZ_4r8EQrZhayTlvnAo1lZFs_Dc0QHi4653Z0xVqDMJ-XNx2S7jFwCjEJCKSFQ5VGrvezEGQyig9nhqaIYUL238N-_l5MyvGImHhYsPBvlx_HfAxuvspOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
〰️
ناو هواپیمابر «یو‌اس‌اس آبراهام لینکلن» (CVN-72) اسکله C-0 در بندر «لائم چابانگ» واقع در استان چونبوری تایلند را ترک کرد و مسیر خود را در عرض اقیانوس آرام به سوی پایگاه اصلی‌اش در سن‌دیگو در پیش گرفت.
خروج این ناو در صبح روز ۶ سپتامبر، به توقفِ حدوداً چهارروزه‌ای که از ۲ سپتامبر آغاز شده بود پایان داد و مرحله بعدیِ مسیر بازگشت آن به ایالات متحده را رقم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71181" target="_blank">📅 13:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71180">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003437fd92.mp4?token=e5zgWc4Lr9Y1rWWvZkeU0iC6KCdsfRQQZGZrIj1grFMRicoR5w1RFhO5T-Jyphe5v_fBQSX559r7-Yx99FKc7MAu0_8lWc_EbPfTeTYzf5AXRg2_4Bl82gVyU3_YENjqJfCEiBpsrI3DEsQAowqrDwm-DnxFv6AiaJLvSPVOchk3ULZejOFClq0RbNc-TM0NttEzPo2IZe_5LjWRjJQjd_mZIDcmi1LQOohGu2b6UcjYb4a2nhEsViQMfxP5cGV5i8KtFcRPDulN2sMcvbDVQvPAwa-CBJaiZlSaww3RqPrQAe1UrUI_Duq7AVXpzeVPIDnM9cccNfbmCuonHJylMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003437fd92.mp4?token=e5zgWc4Lr9Y1rWWvZkeU0iC6KCdsfRQQZGZrIj1grFMRicoR5w1RFhO5T-Jyphe5v_fBQSX559r7-Yx99FKc7MAu0_8lWc_EbPfTeTYzf5AXRg2_4Bl82gVyU3_YENjqJfCEiBpsrI3DEsQAowqrDwm-DnxFv6AiaJLvSPVOchk3ULZejOFClq0RbNc-TM0NttEzPo2IZe_5LjWRjJQjd_mZIDcmi1LQOohGu2b6UcjYb4a2nhEsViQMfxP5cGV5i8KtFcRPDulN2sMcvbDVQvPAwa-CBJaiZlSaww3RqPrQAe1UrUI_Duq7AVXpzeVPIDnM9cccNfbmCuonHJylMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
توی ایتا و روبیکا، ناو جرالد فورد رو بمبارون و غرق کردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71180" target="_blank">📅 13:53 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71179">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71179" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71179" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71178">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0O6C-OVssVJRZyK6pm0JY4HNDesm6q3DzfGqTZ0UGbsEfCdLCAov5PXH_A86prs9wQdaTIW25Nbd7Z2Jp9adaQfmZ8a5xRxo6x8p9mHj42cII7pt5-sfEr7abe6WI-cHRp2Wffoy3PC6cuca2GREafXMRVd98uWQgFINjPIk5TObJovnXf1KDXYlZm2kYzZMXpG52sX9HIKLV8Is9znLN9miUUMCV4tWNsGGQN5exEqEbaT2OnBGaSsW1NRTcPmeUzp7cz1gfYAoVcs1L57OEFEy2-IN6wRUq-fV0guX9HjSrun1PGQg6fnmJRNZYg0fR59k5xgKIV8oYjgsoZRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید
.
اورتون
🆚
منچستریونایتد
آرسنال
🆚
چلسی
آلومینیوم
🆚
استقلال
والنسیا
🆚
بارسلونا
یوونتوس
🆚
میلان
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز و برداشت آسان و امن
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71178" target="_blank">📅 13:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71177">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=vgQ-AMx1HeGXKtY8lZCZOH-JeB3dtInjKqJuOuigYih3LEINAdVB7E_Hd8_m0it0Lao6BKjsjokXNMxBwO_aeUSpT-FE5DaiFW9i1JH3s-c9Etqi1dcTG8W5DDcFpJ4mxEbnI7FwBVj8RRN0mneornjBcCDml8FsoLuZvBI-_ofoCAGs3gv4SnElGi4221eCZluyvUjVn288A-_2Jfn0opRd2khi-LVqQpI_WTYO_8qzmOTeo5p-VXcWUbs07sRsYdUQ7GVYfE3YqBtHcacy997M4Lhuk0xBsm0mNzxH2xuqKPdIn-jtc7MkTb0epQigjIiXb2NlcJAaQOQJU0hqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3c6743716.mp4?token=vgQ-AMx1HeGXKtY8lZCZOH-JeB3dtInjKqJuOuigYih3LEINAdVB7E_Hd8_m0it0Lao6BKjsjokXNMxBwO_aeUSpT-FE5DaiFW9i1JH3s-c9Etqi1dcTG8W5DDcFpJ4mxEbnI7FwBVj8RRN0mneornjBcCDml8FsoLuZvBI-_ofoCAGs3gv4SnElGi4221eCZluyvUjVn288A-_2Jfn0opRd2khi-LVqQpI_WTYO_8qzmOTeo5p-VXcWUbs07sRsYdUQ7GVYfE3YqBtHcacy997M4Lhuk0xBsm0mNzxH2xuqKPdIn-jtc7MkTb0epQigjIiXb2NlcJAaQOQJU0hqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
سنتکام ویدئو غرق شدن نفتکش ایرانی در دریای عمان را منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71177" target="_blank">📅 13:12 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71176">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⏺
🇮🇷
قالیباف:
آمریکایی‌ها باید دریافته باشند که دوران «پاسخ‌های متناسب» به سر آمده است.
حملات ما به پایگاه‌های متجاوزان تنها یک آغاز بود.
قواعد بازی تغییر کرده است.
از این پس، هرگونه تجاوز به منافع ایران، پاسخی سریع‌تر، سنگین‌تر و دردناک‌تر در پی خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71176" target="_blank">📅 12:44 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71175">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=UJ0faXITYKsUp1nAnElXkiwXJbtOW1HX2xwCuah5O9_hV1STMNtAly64pM0gF9ZTDTr3zkX1Moct5tjSEsF_ODOlV9G5buQsPGkLJ1d0NumyEXxfcLQIAFUdi-ZqRq6gOhERMmsxUogwTJGOSX_tIKm4DBpQcQ-zRcvv6D1gaZbxY20FG6219JZHfAXFOcFE0PoivWNTNKaJAhHi9UcTfY0ZnZh3DWeUY8ETZR07mXS5aAjq8Z7SljDvcMlTFEkpY6XC6WCaX4DxfWNQs9sDfWxPRgrWK9MVZ2ZJtT4aC46aYvMQr-R56NChp8Y4zlno4XwokQojxyw7z6bbJFU4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d5a31326.mp4?token=UJ0faXITYKsUp1nAnElXkiwXJbtOW1HX2xwCuah5O9_hV1STMNtAly64pM0gF9ZTDTr3zkX1Moct5tjSEsF_ODOlV9G5buQsPGkLJ1d0NumyEXxfcLQIAFUdi-ZqRq6gOhERMmsxUogwTJGOSX_tIKm4DBpQcQ-zRcvv6D1gaZbxY20FG6219JZHfAXFOcFE0PoivWNTNKaJAhHi9UcTfY0ZnZh3DWeUY8ETZR07mXS5aAjq8Z7SljDvcMlTFEkpY6XC6WCaX4DxfWNQs9sDfWxPRgrWK9MVZ2ZJtT4aC46aYvMQr-R56NChp8Y4zlno4XwokQojxyw7z6bbJFU4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:بستن تنگه هرمز به ضرر ایران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71175" target="_blank">📅 12:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71174">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=KScWe7b1j610xVMRM2BEP4XhXaguYBju4HRNEey2EM8Q6VjE9nCIMoxwURZZBL45l9fTWeRVM5AJvaHc7NR4HYcpMZ8MpBXJtpZLGYf0aZ-luI1srKoq0hQoAQ_NbMofe8N8C873lRZxfdYLRqQjZjYzOh48htNBlbCR8eI_f58hcLovbujs0LYxE3-KPfkFlAUG2Va8atubb1VCz19f4PAHaUkCLJLTY0OJWfs5zMCUx4Lp4HzoEk8DmcHls5RVGkLsm5x8uLmD_3MClp9-3WcVf0gTD6pEUN3CpRbVPpdFRVntNBIy2V_7MhaKYAdqb-brLx0R6k4wh2-ZzoX86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8313313bb.mp4?token=KScWe7b1j610xVMRM2BEP4XhXaguYBju4HRNEey2EM8Q6VjE9nCIMoxwURZZBL45l9fTWeRVM5AJvaHc7NR4HYcpMZ8MpBXJtpZLGYf0aZ-luI1srKoq0hQoAQ_NbMofe8N8C873lRZxfdYLRqQjZjYzOh48htNBlbCR8eI_f58hcLovbujs0LYxE3-KPfkFlAUG2Va8atubb1VCz19f4PAHaUkCLJLTY0OJWfs5zMCUx4Lp4HzoEk8DmcHls5RVGkLsm5x8uLmD_3MClp9-3WcVf0gTD6pEUN3CpRbVPpdFRVntNBIy2V_7MhaKYAdqb-brLx0R6k4wh2-ZzoX86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">〰️
ویدیویی که در توییتر فارسی به شدت در حال وایرال شدنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71174" target="_blank">📅 11:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71173">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=M5raIbcFz_wVryHT0v9r81Urw6ZJYMbw23Ltmspk9Oeu2iMs58l5A10KCsimhZvKogrXzovWwmSRY8fXlS0njXGBusx6kKboElBsNpmTgMFIm4QYPNgCxaG8ymyAfN1aK4rn7zkSB3BD7nykQgWw0hCkWc68-kdWD7mU_VYHY80pdwJv5bOpzSSJnXqElPLn3RptvGhHLmj6fgEVnX_NLU_knHBwkVCN4EpO8ce07noTWraIPSxY_WBU5nYOxC1q793Npt9TgnlnNE24UIgnte-cnS_R0fZ6oAotTKcgkhZyiWPS_8elOYFcCqXw_3rmWW3PCrL5-6dHMn0J-DXOVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8295abc0.mp4?token=M5raIbcFz_wVryHT0v9r81Urw6ZJYMbw23Ltmspk9Oeu2iMs58l5A10KCsimhZvKogrXzovWwmSRY8fXlS0njXGBusx6kKboElBsNpmTgMFIm4QYPNgCxaG8ymyAfN1aK4rn7zkSB3BD7nykQgWw0hCkWc68-kdWD7mU_VYHY80pdwJv5bOpzSSJnXqElPLn3RptvGhHLmj6fgEVnX_NLU_knHBwkVCN4EpO8ce07noTWraIPSxY_WBU5nYOxC1q793Npt9TgnlnNE24UIgnte-cnS_R0fZ6oAotTKcgkhZyiWPS_8elOYFcCqXw_3rmWW3PCrL5-6dHMn0J-DXOVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به گفته آقای دکتر اگه می‌خوای سرطان پروستات نگیری، باید ماهی ۲۱ بار سکس کنی...!
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71173" target="_blank">📅 11:02 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71172">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b321711db4.mp4?token=MaqxaMdEWSwusIUotY35V1Z7nulgntkKAjH-4p37YAAXtASZXzkdWd4H_v8YJULz_g23sH8KA90dv2yOc32BcO_rGEnXRkWvLkoQNEwtBAfX4aqUQi0_seB4YlNKsHqeNzkHF1L0t4pgfsbLd8AUapahdCzCTW5AqMO1dUmyZfUod6dYoKt7C6tqEIOMFxYS2GLnvz-vLEq9sCYvow0w5grGIH3MP_E_7rSEd3DltXegdHeSKL2BlJI-DOetCkfzQsU-1mTRoxRhprMMqENLl12tmIz8puscY0f1bQPY3uFppl4ECna60tFw0qZIrtkDa4gHndqPku9OMbcJY_BIqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b321711db4.mp4?token=MaqxaMdEWSwusIUotY35V1Z7nulgntkKAjH-4p37YAAXtASZXzkdWd4H_v8YJULz_g23sH8KA90dv2yOc32BcO_rGEnXRkWvLkoQNEwtBAfX4aqUQi0_seB4YlNKsHqeNzkHF1L0t4pgfsbLd8AUapahdCzCTW5AqMO1dUmyZfUod6dYoKt7C6tqEIOMFxYS2GLnvz-vLEq9sCYvow0w5grGIH3MP_E_7rSEd3DltXegdHeSKL2BlJI-DOetCkfzQsU-1mTRoxRhprMMqENLl12tmIz8puscY0f1bQPY3uFppl4ECna60tFw0qZIrtkDa4gHndqPku9OMbcJY_BIqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇹🇷
این پسر بچه ارومیه ای که چند وقت پیش با ویدیوش که در حال آهنگ خوندن بود توی اینستاگرام به شدت وایرال شد حالا یه کمپانی بزرگ از ترکیه اومده و باهاش قرارداد همکاری بسته؛
فعلا این قرارداد واسه اجرای کنسرت های مختلف تو ترکیه‌ست
رئیس کمپانی میگه که این تازه اول راهه و قراره بزودی تو سراسر جهان کنسرت برگزار کنیم...
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71172" target="_blank">📅 10:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e529d142.mp4?token=vZDg3Zjpb1WOORWjYGQwi9tib1WIAieNtFYRZPx7Pz559pJT-LDWlGcCUanEq12ku4o4XmegSMfavW9Ai6NuVnB7HElZSFihf7RH-KvuH4G4rNGV8xJm09Zy_17jiYMOczuKqOY1Ksd1kDwg64QlvY-DeYwEpUzKAo3Era98g_W6cB67lrAGGunoa02-gg9wUVTNUe8UWSS4BRTCidXBW0e0f5sQYEs99tCNuUuWdRZ-IJ3o3zgniqJjEaulcza-a_Q4mFBhesR7qbp14cBr1IZT5Na8kaeueZycBFdy3zdUyRkrz4WOogUy1pIEEaJbwdB4TAbJ_yT9TULEQ-CUaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e529d142.mp4?token=vZDg3Zjpb1WOORWjYGQwi9tib1WIAieNtFYRZPx7Pz559pJT-LDWlGcCUanEq12ku4o4XmegSMfavW9Ai6NuVnB7HElZSFihf7RH-KvuH4G4rNGV8xJm09Zy_17jiYMOczuKqOY1Ksd1kDwg64QlvY-DeYwEpUzKAo3Era98g_W6cB67lrAGGunoa02-gg9wUVTNUe8UWSS4BRTCidXBW0e0f5sQYEs99tCNuUuWdRZ-IJ3o3zgniqJjEaulcza-a_Q4mFBhesR7qbp14cBr1IZT5Na8kaeueZycBFdy3zdUyRkrz4WOogUy1pIEEaJbwdB4TAbJ_yT9TULEQ-CUaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇱🇧
خبرنگار جمهوری اسلامی در لبنان:
اعضای سپاه پاسداران در تپه‌های علی‌الطاهر، به دلیل محاصره اسرائیل، در شرایط عاشورایی قرار دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/71171" target="_blank">📅 10:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a662811c73.mp4?token=RNY6UAUbJ6Bg-mZPBoxcVT67JQ_YWpU93lKGHu4ukw60BzfNf1U7n_-FLnJyZhnD6N81KHZKB9s-g4oTnPMbhi4k8fcFvOn3ydYtYxPDilY5szC4-EvG_nxx3k0O6LW_kKp2CHQ7FGsiZPj2SqgFEv_6IzwB-q-vBbAWJPpj7mK42y4VCZIUsv8GjtXn7PaaKZ34y-YkDH6RwzE6ELCGtfsHA3K1z6VeEQ-5BAWV_m3C85Etsae0ERblLO4nlM8ih8k2NLzJBDmMjH4SSX9c2l-smYQNr5EvgGzUIA75TNgcfrzrwmr__RjIWfE4Ns4Lx4BL5QN0U-VnOK86rj3yQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a662811c73.mp4?token=RNY6UAUbJ6Bg-mZPBoxcVT67JQ_YWpU93lKGHu4ukw60BzfNf1U7n_-FLnJyZhnD6N81KHZKB9s-g4oTnPMbhi4k8fcFvOn3ydYtYxPDilY5szC4-EvG_nxx3k0O6LW_kKp2CHQ7FGsiZPj2SqgFEv_6IzwB-q-vBbAWJPpj7mK42y4VCZIUsv8GjtXn7PaaKZ34y-YkDH6RwzE6ELCGtfsHA3K1z6VeEQ-5BAWV_m3C85Etsae0ERblLO4nlM8ih8k2NLzJBDmMjH4SSX9c2l-smYQNr5EvgGzUIA75TNgcfrzrwmr__RjIWfE4Ns4Lx4BL5QN0U-VnOK86rj3yQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شاهین نجفی:
هرکسی رضا پهلوی رو مورد انتقادهای عجیب غریب قرار میده و میزنتش یه سرش وصل میشه به جمهوری اسلامی
اینا جوگیر شدن چهارتا شعار دادن و حرف زدن بعد دیدن اینجا خبری از سهم دهی به کسی نیست مسیرشون رو عوض کردن
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71170" target="_blank">📅 09:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71169">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=rXKRDbwdH3N5G2MHoqAhrbr7k0_caM0ElwktjhC6T4TuQhC2e0_LW72nrBcYs4etaAPbBVNsqVLfUJI73uLcH2sbC5U_Q2c4tMqSuXBe-HF9ofOOsFtJGb24l_6LR_P0_AdECNAJCNNmeMu9Urkm4XDKCOFPdYx0FlAxNE_IG1GLsUMPoRfQzGvQy3He49TIqitCuUb51mQP0iaUd-NQ6EfwSr1-V4Db5wuMMSzFR180ayRGf_nDAdjOlcW2Uv1fwXZFUXzlaU-4YinDiyhZKzcSYkmTjF70V_hx0Qmn3tD7oUCa3OvLE4QXKmjJQR65JeNo05mHE2gcwA9rgn0sMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d150aea8.mp4?token=rXKRDbwdH3N5G2MHoqAhrbr7k0_caM0ElwktjhC6T4TuQhC2e0_LW72nrBcYs4etaAPbBVNsqVLfUJI73uLcH2sbC5U_Q2c4tMqSuXBe-HF9ofOOsFtJGb24l_6LR_P0_AdECNAJCNNmeMu9Urkm4XDKCOFPdYx0FlAxNE_IG1GLsUMPoRfQzGvQy3He49TIqitCuUb51mQP0iaUd-NQ6EfwSr1-V4Db5wuMMSzFR180ayRGf_nDAdjOlcW2Uv1fwXZFUXzlaU-4YinDiyhZKzcSYkmTjF70V_hx0Qmn3tD7oUCa3OvLE4QXKmjJQR65JeNo05mHE2gcwA9rgn0sMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما آمار رسمی کشته شدگان اسرائیل تو سه روز اول جنگ رو منتشر کرد:
۶عدد ژنرال ارشد اسرائیلی
۳۲ نفر مامور موساد و ۷۸ نفر مامور شین بت
یازده دانشمند هسته‌ای
۱۹۸ نفر افسر نیروی هوایی
۴۶۲ سرباز و ۴۲۳ نیروی ذخیره ارتش اسرائیل کشته شدند
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/71169" target="_blank">📅 09:01 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🇺🇸
🇮🇷
سپاه پاسداران انقلاب اسلامی ساعاتی قبل در بیانیه ای مدعی حمله به یک ناو هواپیمابر و یک ناوشکن آمریکایی شد و اعلام کرد که پس از این حمله اونا خسارت دیدن، ترسیدن و از منطقه فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71168" target="_blank">📅 08:02 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
