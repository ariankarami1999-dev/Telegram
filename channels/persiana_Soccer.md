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
<img src="https://cdn4.telesco.pe/file/V2VEBOYmAQ_uahw2NGUfcn2pZG1_y4Axe8PquWEChYFVJCI160dbLBZNujF4GGUGWj1UrwElqOubUygrg0O0KtMcRQk_bmCthTAuZR6pdY4ivLVJk8uX0LiIf0j0jrR9zcB909O3y35zLN548jcKsaqDJmiFuZlb_MtgkoFuU32BhTVw3s_XoRVFrb0nor81IQwKXu1msiqFJBnd1l1t9D_a1uhE_yFz72KYdPpUBZ7Gd6G98qQOkIN__0AjbxC2yQI4UqjkDAdI8W6gbf-zdskWEqUft7SUTuTmXCH0Ih0PSbJ9lFi9OAUyPzP_ro2VJfNdJUf2ydTBe7sJS77Fug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 493K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=YuB5JUQz6x-qG82yPZHDTLSrAAr-fyY_h0EtDvHcRFlXlgvBR0BKqMankLtCRwfX6OiCtv3DCnyCVajqUnWkDjFA-9WzEug1H1C08ifggcOpHK1z7XFp9plW99SOLrRpcM_H0St7DVBVXBvpq_VHkUbjyMbxaFc4LimeE3Vp1ugEXh2nY6Lih3sMdb-ngkp5FF0p8jGmAjeUPoQe89-YOCMvc0nUiWWxViilIHEZjG0iAmSMfhGLScPNx3ZDFLi8l9dPw6PU-y3_Dac2gJGa0sc2qsGaBWATqHDnDM3dFm2B5AG-OnZZMJbkey4t_BRzMecTbZMfAQ5Ke-muA0Hb4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=YuB5JUQz6x-qG82yPZHDTLSrAAr-fyY_h0EtDvHcRFlXlgvBR0BKqMankLtCRwfX6OiCtv3DCnyCVajqUnWkDjFA-9WzEug1H1C08ifggcOpHK1z7XFp9plW99SOLrRpcM_H0St7DVBVXBvpq_VHkUbjyMbxaFc4LimeE3Vp1ugEXh2nY6Lih3sMdb-ngkp5FF0p8jGmAjeUPoQe89-YOCMvc0nUiWWxViilIHEZjG0iAmSMfhGLScPNx3ZDFLi8l9dPw6PU-y3_Dac2gJGa0sc2qsGaBWATqHDnDM3dFm2B5AG-OnZZMJbkey4t_BRzMecTbZMfAQ5Ke-muA0Hb4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=tOafOF6dbB5tK8txlbG3f5nH5HfSb6cVtM4oGKG5p67A3W5-Rk37-busiVMJBRxBkghm8G4f3tdoHPGzCLwust6DX3ikyRVIEUpCj9WkytxXe5VNywDCQvstEzcS785BUM5yaDb-745ZEteChxZlGPmXAEDPghODEuoxuI3peHcOCsXs4k6uipKgSXJKxuduPmWPOVAbDqd6VZtXxHhk0S-Xd9v0EkMCcR0TgWsSao8Owl6ofXPhe3OAqAfD3GWE93qBCdh1QPrEBBXV8tZiZPm-kdd3GBX0yPbyCKI5UNGNCO_pmzjc3Sx7oNbyVWLz04sVqFLpgW08sGPKuw0gCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=tOafOF6dbB5tK8txlbG3f5nH5HfSb6cVtM4oGKG5p67A3W5-Rk37-busiVMJBRxBkghm8G4f3tdoHPGzCLwust6DX3ikyRVIEUpCj9WkytxXe5VNywDCQvstEzcS785BUM5yaDb-745ZEteChxZlGPmXAEDPghODEuoxuI3peHcOCsXs4k6uipKgSXJKxuduPmWPOVAbDqd6VZtXxHhk0S-Xd9v0EkMCcR0TgWsSao8Owl6ofXPhe3OAqAfD3GWE93qBCdh1QPrEBBXV8tZiZPm-kdd3GBX0yPbyCKI5UNGNCO_pmzjc3Sx7oNbyVWLz04sVqFLpgW08sGPKuw0gCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=m48dDSEpiFWaJ0xgzOrEXZ5QKiFaOhRs2CxLwOOQ1NPEeRzxeY9Amx8e4HkaZz_pxtMfABI82QwelS5wYVIFSM8r1_aiV1hdwg5zzNAuOiilsFTeiYA4T0Jb3h4nLqgPM2OgIxBTF4dqftyi5DDqJmAJnf_B5chPSoXiuIeub898sPlHqPH9YMZVbiDM-nh3RrUISJEnwbbdomuIvHFkGhW9xlU34ZJkVS5BjFzF35syOpeHtb6fBamqHHP1yFDt3vibn7qtjd2mWj-CrysX8Y2u9RP3gdsLIt1gyy27nADHACffbhVYTUK2ZsCVdU5Y3K0gSlb663EL5p91Uj6LGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=m48dDSEpiFWaJ0xgzOrEXZ5QKiFaOhRs2CxLwOOQ1NPEeRzxeY9Amx8e4HkaZz_pxtMfABI82QwelS5wYVIFSM8r1_aiV1hdwg5zzNAuOiilsFTeiYA4T0Jb3h4nLqgPM2OgIxBTF4dqftyi5DDqJmAJnf_B5chPSoXiuIeub898sPlHqPH9YMZVbiDM-nh3RrUISJEnwbbdomuIvHFkGhW9xlU34ZJkVS5BjFzF35syOpeHtb6fBamqHHP1yFDt3vibn7qtjd2mWj-CrysX8Y2u9RP3gdsLIt1gyy27nADHACffbhVYTUK2ZsCVdU5Y3K0gSlb663EL5p91Uj6LGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9dDE1B2rVO1bZa6IrS3kievp_5oFltY98jBhZyGR2fqgyzpUkRMUNeszQt2uvDXGcG6UckLg0sNfO1RbM3Tvpfzh_xbln3ecSAa5Z0F7ODYFDA53Tke9RN4ZdIc-EBhZkNzholOaphYLFn_ZBa_ESXuW-xE2sOtfcTU0BShc5P4b1KdANQyLMiN2zJTe_DIucsY2PYFG5UKrofxfxAJ9JYE8OCp--ws4x-9I6fCFAKyzCwu6OXs53sF7XJeay4iADtPjYxv98hhofOiDLT3Xjf27VcnSMimQUhOVN_2FcOXRakLb6rzRUErOqGujUOkTeVOlu4h5FS89R_bUiZ21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=Qgad1eh7zqkc1fBXVcLVK0957wPt0YnA2UeKWXHT2pJrnS8eq1Yr21YUKcfUItlcToOTY4nHOjHhmzWzerySVh47wtPkYv8k1R06XWoKX5aYIJ4jUM6sKRtjlu1UIurqe-hqEUsVAcaUdugams-NVZ1g-XDKtdtrQ_lEvo_vR1uW9nG6sKwF7-zQMUmHh-sY9UF8YREZtK2gnPPUBtTa4604rAFTR4JDG28URyXL2cVNEa9qIwzzr4_KllsBEvmNNvYrEvWetgX5ssN2e3cDwouXc79hB_Ho7Dzd_RiWcqBLrLH0RtSFkVNyI5d4rET_Fp7nN2jhFXo5eBWOhpB7Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=Qgad1eh7zqkc1fBXVcLVK0957wPt0YnA2UeKWXHT2pJrnS8eq1Yr21YUKcfUItlcToOTY4nHOjHhmzWzerySVh47wtPkYv8k1R06XWoKX5aYIJ4jUM6sKRtjlu1UIurqe-hqEUsVAcaUdugams-NVZ1g-XDKtdtrQ_lEvo_vR1uW9nG6sKwF7-zQMUmHh-sY9UF8YREZtK2gnPPUBtTa4604rAFTR4JDG28URyXL2cVNEa9qIwzzr4_KllsBEvmNNvYrEvWetgX5ssN2e3cDwouXc79hB_Ho7Dzd_RiWcqBLrLH0RtSFkVNyI5d4rET_Fp7nN2jhFXo5eBWOhpB7Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=p_E8xjUzQ54gOkY8phu7OKaICEA2vj4fw-LeHUBf8slTLWOOrY6Dg3UU42FVyl7khrJ9Y6_8PRbNR7cwc8QyXxt7sdGQ3PO7Zy_27lP7PshIAPx_YpdqLCFqcD6uM6pRZSwkoUw18QRviewynP1mVvDiLhB4wvEaRYt3BnEsW-5DBoZDYlWMuEJP4wfssoWSznezyMoMJER2u0eBcPhQ6xPw2dVdk17Cg2Gf9uGiK35UhwTGzgLauu_eEHuz4Gp5-qTuZKeOz4I1qfI1-UassoW_W4r-cVSBCeQZYrRga0f-CQtcQFH9mkxm7QNs43MdNFXecgGrsQQo-HkTNVg8Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=p_E8xjUzQ54gOkY8phu7OKaICEA2vj4fw-LeHUBf8slTLWOOrY6Dg3UU42FVyl7khrJ9Y6_8PRbNR7cwc8QyXxt7sdGQ3PO7Zy_27lP7PshIAPx_YpdqLCFqcD6uM6pRZSwkoUw18QRviewynP1mVvDiLhB4wvEaRYt3BnEsW-5DBoZDYlWMuEJP4wfssoWSznezyMoMJER2u0eBcPhQ6xPw2dVdk17Cg2Gf9uGiK35UhwTGzgLauu_eEHuz4Gp5-qTuZKeOz4I1qfI1-UassoW_W4r-cVSBCeQZYrRga0f-CQtcQFH9mkxm7QNs43MdNFXecgGrsQQo-HkTNVg8Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=mqo9Etn2SXc4WCbm1KKU7zPvg-II0kiXY0l27D8E8vzAfrCTKlue6qBS4Hapcye9o34s2OSMmbNfE-PWULOBL9iHhdnrppuF1WIY9rEUx3XA0ZlE02RlZyAxbcITzFh4_8xrnkXIMaYkNEGGWyNm8stH7qxYLDpC54xHTvvae4Yq9-lUdTHzEf4GvXmjKdKdcS7zigi8oIJXFmSUyAFBdbn3cNlUwA7ajGEDtwKJsXz3Uu-BCFEODlPB5yYDd8wH6CL5LDjXie57lq7oeK1qC1pPgFDNbtkATo49SsDcSFcVxBBrvrEvVNRNoH7egYnPSKBrowXVpR8xDDId2Djamg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=mqo9Etn2SXc4WCbm1KKU7zPvg-II0kiXY0l27D8E8vzAfrCTKlue6qBS4Hapcye9o34s2OSMmbNfE-PWULOBL9iHhdnrppuF1WIY9rEUx3XA0ZlE02RlZyAxbcITzFh4_8xrnkXIMaYkNEGGWyNm8stH7qxYLDpC54xHTvvae4Yq9-lUdTHzEf4GvXmjKdKdcS7zigi8oIJXFmSUyAFBdbn3cNlUwA7ajGEDtwKJsXz3Uu-BCFEODlPB5yYDd8wH6CL5LDjXie57lq7oeK1qC1pPgFDNbtkATo49SsDcSFcVxBBrvrEvVNRNoH7egYnPSKBrowXVpR8xDDId2Djamg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZqESWV_Hi0wuiBUHgnzRhoyRvEE-c1AtjVP1uohrFFWZomT1mPhxADCQ0hOPqahkGa_GCmf54vNzuG9yeYysoUYdd27rW-imvPtsl76duE8Y6wW6utIXLmgGediRYTNL8yHd3bj23Tw6eUPboVI9ckOHRkSmnHx94FIm7k2wrZx76MLvc40ENQwCN4ct2GuNFfCYy49vdnJdpNDL1FbDlrJc3xqzmtr1G7fRZk3kX6OksIs7sN7bgji19XzCm6QHuycgkcmxYlGo7C0rdxcS1CR12c32_lHMbgfF2fnFhMrbQ0EomLRHgOwWAqHBxxdVnIwhdTidN8Bu6v_kvGltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwiMchr5iqOGJC6rXabIGekTYS1Y-PmOPdwd4CT1qAS0jS7Ap4_pJDpgaiBJ5_UwzegAmFI6TM9euxVVJStvHDU-CVo4AwurqfJJI1StYis7XqmqNT8Zv5qNoP76ovk9kfJRd_GHSQGALZxdjTmHEi0GObWMDhua4rAT07OC0OCE6P3_CUvQsA26rN1HT0R_Lf8g5fNaC8SYUo_1XdHNEeY7jMetChPIjBDUtvbDBJPYdTIg9TVVWAKZ0svLk_vuH2kv9cgt1fE_9XIha7pavA6dImcPcToE10EtW-4l7HRR-Wib8doZK7fEQb0KBYLAW0mSi05M8u9VU6jMvCy-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCD2z-YRTN07x0EtV70aZZSLim9nu4HpzuqlN-ocKxgpgKUcspIC6WKFUujMTvJW52l1VECDCMpRR_ph8QhcmFHdq4jFytqXjRWbgx_zwiXeCJ3B4ehQQ759DPJgS49-JSWQOK1bBJxBZgU8HbJhjmoriv4_9Em9OcFDY74pY5aQ6XOHLA_Sk8O2RDjQtyXU6zykVXPxm_q5QETv2BFqRSf-pdM6Gufzk4T2joLT9nkSK9AHnFDU3V9h561b0NdZLi7oL-POINn6_6zdOtpsA1h8pFtNfdsMQyFARh1UiJp623k0uEAmoJTK4M-4PRLfdAsKMxxBD4MwSB_k8Zw6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdmUNmi3SOVvyJCQAFrjWnkL3bBzlndMBP2aasCbVouxCIAdvUNUhSqaPejx0ipFHrYNsZqs-8kT0QieitmmE_8vJnhIyvJP2cI8a-cY665qLz0TmXONNAxxY70_EvO_UxSmFL7xXC3IDqlM4pFFOGE2I-O-FQ_04tDi8Qca18BtzKnspG-RzG8xhciLww4K5Mziz_e4DwIRQT7p_c_Eaa5celye-d4-ITb7lF7wsVM0Z7Qkk3fsI1AJj4Q9Vo2zB8erpKI0THiXZ03WhJbxmMOdlCxT7dOuK_OsVPh_G1kkywg1Mz_8vB2JkAKP6bRDVTxl5QeOTkbZiY6q2Y8XDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kz2XJADiZamrBXZXygFRFZW3Sneje89fMwsXzHRWO6CSrp_yo18HuKGoGfP7lnuBlv_p1twrTHFIihpuAhUkzAqf-ZdkYZKXPFljf6LTrppHpdnma6XvNFpdY3AabT2hmOSnSciQP8-mwHOklCSrR74ceu_cLHSVKz60lc3zuCX48gqbeUH8dZi8e_1LU8yK3OZdFQcGFv06kUp-t4MZe26mO9HZ1bQrRpSi7sfT3385KGHT4jmYf22K3STuwD59Y5QI66JIFKo-KQ7NHvwphyN2IWLNFHuQggwsU1BPUPLgVG9KbrF_HhWxDrwWSjv3Js6dd7HpfvcwnGZ88bn9kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxtBX9qdVHgUHdM5Gs2CTX8j1S3q1M2DvhVGbFTjP91OFP8ICTNhw7-bdZch70ayu4IXcSWgIOKXNaETNjR2jB3Dq3MuokW1-jNptESDFH8Et7Wvfz2CfcNxGdve_19-oBue4I9u5n9DTk5kTWGbdgEcOrqthoEBw-TFk2BjtnmfkpXxS5UbVLqsrYbEOUxts1wPSS6ArJ75wM8J5EtGqQKNPXijFYcT3LFhwGOrmQN3ExpVOr9kyJT0rACdPrEu7Vi0FGqD83OdfHxxU-DetZqErWq8UWj40NNI5cCBPfCpN_jI_hOeKGB4ntihGKrot1VCSpi9gcj7SvnPwoxTJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31247">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبر داری فقط همین امروز می‌تونی از اسنپ، طلا و نقره رو بدون کارمزد بخری؟!
🤩
کافیه وارد سوپراپلیکیشن اسنپ بشی و از بخش سرمایه‌گذاری، اسنپ‌سرمایه رو انتخاب کنی. حالا می‌تونی به‌صورت آنلاین طلا و نقره بخری و دارایی‌ ت رو مدیریت کنی.
پشتوانه خریدت هم اعتبار اسنپه و هر وقت که بخوای، می‌تونی به‌سادگی طلا و نقره‌ت رو بفروشی.
همین حالا با اسنپ‌سرمایه، بدون کارمزد خرید کن!
خرید از اسنپ‌سرمایه
خرید از اسنپ‌سرمایه
خرید از اسنپ‌سرمایه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/31247" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua81F3pAUaTxx0fUspuPbpMTgJqg9jaVZhggh8HW5xVOfM0rZBLIwa0SPNxMCFkwTvkIb_ntBdBMekm7-IpEs-oTjbmvlBiZbMv0UGgfNe-6qptl7uIDGCFz5pns3OF-OlWgSoDiS96oLnBDzNr-P0dg4zUGUvtKPqWqD52m_bzqfP0hXO7e8Papc290QDmridy7KigsfCRtxMWF-w8S3tm35SFmVEnlXKG_z8xC1Vmj1eKUkEZXpTKgJcZNcyz4EpuGmC7F0H7M5EJVwfWJO2WrPB8x7KkAAzdIYD6LIkiQ4plI7vSQ5xCUGwL53yzc3vzt3fnkFF2fY9uh60B1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=Sbok8w-UPc6tBibjpEcP16mLETFG93rBW0GlO-OpmM_U7cgRIEtFUVzx4Gz6-m8eDmezsAkoi3b_Uj2Y8OFyx_X2rBJ4Qx-8zXwCkU9w0fJvZ1LgY3B-qHEqTMmR8tN4a3RH5ryD2UT-Sp1gU6HQHhvliFyD9onDOtJQddKuI1J2Tr7qDcPfBwfc-bUGhaQOLw0iP8I1LdsqmJ6giJBzlDsyRM2fYvLwkM1ix4K1O6aLwCfaxTkR5zHD1q4ToaZHgo-OWqgH8jX8c2tsePtp_2NDYz_wKW5a3UYZ2cStRs94GM5M8_yQgpJ--Yxgx2ZxCPs80gNoXbY6SpJ1BVSOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=Sbok8w-UPc6tBibjpEcP16mLETFG93rBW0GlO-OpmM_U7cgRIEtFUVzx4Gz6-m8eDmezsAkoi3b_Uj2Y8OFyx_X2rBJ4Qx-8zXwCkU9w0fJvZ1LgY3B-qHEqTMmR8tN4a3RH5ryD2UT-Sp1gU6HQHhvliFyD9onDOtJQddKuI1J2Tr7qDcPfBwfc-bUGhaQOLw0iP8I1LdsqmJ6giJBzlDsyRM2fYvLwkM1ix4K1O6aLwCfaxTkR5zHD1q4ToaZHgo-OWqgH8jX8c2tsePtp_2NDYz_wKW5a3UYZ2cStRs94GM5M8_yQgpJ--Yxgx2ZxCPs80gNoXbY6SpJ1BVSOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmL3ZTriGrG2BxUws5mavVEhqJvEIilybxi9jkXpHmXbywZAgiEHTQlMxlJiadaOxvfOxIY46RVXtt5jeykR2SiSN3C6JSxZyx0F4Dh038mp9PaN0tbQVMvjYO2JJIhQ5swtGO_9_4fJxa2s6xhDSlyaTgG1znMUgAsSlelGLtEcTrHkNpgiS6Y4XTlEbFmZUMj0BKnnHUeTaMTcLSx5yNQFUVkPpeyPuPPP_f_PbvE7vX08R6DFmLPLG3uotdraL-Q_3fZO7T5YTyeUBLemq9w_z8URScEh_T9W24gP10PdTEfbyX0bUh1xvopSQ498JtRNDw4ZI_Roi1rxIrjJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=OmZ2O1Ir3oJCXswCKUUQ_7zhgzFSLjlVH--0xs__cfj6yWrg9qPE9CChab1mcwznuyaQ29CMCiK2Qq0GKhD1BxkptagC8YzyVxNmzKJBHZlTqymVt9-p-EIbp0AJOyQYMJtRLqRssLgu36f_IGT1gdd_Jcdxqi37fdSLNQEcKH2LvX6JltFcqLVAP3-LYoDSx3mlb7z2oJSx6wIUH_vcEyCpx03X-Axia4wdSmhKUfGCx37VxeR5UORpKdT-bTDX7qQZJLs2IBeGYx1xF2H_PONkS7z6vfy73GJUZX_o3TEFkXKbSrDy-H_QgEaC1_94rdVNJhNVfGQtEnQ0kBc06A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=OmZ2O1Ir3oJCXswCKUUQ_7zhgzFSLjlVH--0xs__cfj6yWrg9qPE9CChab1mcwznuyaQ29CMCiK2Qq0GKhD1BxkptagC8YzyVxNmzKJBHZlTqymVt9-p-EIbp0AJOyQYMJtRLqRssLgu36f_IGT1gdd_Jcdxqi37fdSLNQEcKH2LvX6JltFcqLVAP3-LYoDSx3mlb7z2oJSx6wIUH_vcEyCpx03X-Axia4wdSmhKUfGCx37VxeR5UORpKdT-bTDX7qQZJLs2IBeGYx1xF2H_PONkS7z6vfy73GJUZX_o3TEFkXKbSrDy-H_QgEaC1_94rdVNJhNVfGQtEnQ0kBc06A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvpKGGSygx-9gnWozYN5ofvJ9Zzyp6ZAyGnjUl4skOJKfgyLQpNpTH98dLcNZ6QmITy1pT-RdT9AemhFVOI-Nav3iHJkPvZG04xMliTspya1cmr-qgJhMN_s9sDPs6ApNK_ZSJypum_gbtT_t-fC-nzMldNZfoStrf4a7WyjN0psbRsxkXVcwI-VmX4dK10wMydbyNuzjZrU7MzIrMGx75Mh3MBqrKVIB6ZSE4mE2NvDR5tz6e0hoSAEDrt2T0vBAJt9jQMkInqZ3vBmlh2lbRGeOy8-CRZsGG_NbJZ1iEcQZDidl2bnAtf1mrAmill64DBbCkKkyk88kVfOCDDC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6dwuByrKuakR7zTMFGVPTX37qYL2V2BXx18UM17VyC-vcJpLkWyhdMz4xBvHP2m3gpN4J731guM4rWs_aAkgaeeSU7X8qqV48fynsPI8Jd5qfYVfIH_PArCXh6fREW4O0eT8A2kxDpoa5i1--zy-W-cWPLlDTJIQ0Nx2pYVHbey88z7UVdsLaW54hkolto6S8hgkAnvlsN2PyC32Q1Y-89sjsEQh542HdoLmxugvwd_It7xs3s5snkKfz4e0QvrOE8I8wmi0t7mVgTluX3KPjdTm7u2L0wMGVLoqC70vC0HAlik954lN_FafM14I731yFxbDANyqL6sn71slXGm4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy6KwTXSvHj2t36buV04p1ZugdSZmrEdnnD3fVypUiaFtFbVAttfJB--FbI66M-MCS6CBfujIqI9-z1PUwqUoJmMQ_kOG4Aq59SRnxmcT54_bKx9vIVwsGlTTHzpY2fbzxSIGnJF28vRB0V6D0gG47lxwRchuk9DWUrpym5XjeTFRzIWf7CQRKItBc9bKIo089qp7rXNtHHb_YYM4b8uZ3a7FkKTsoSCqEnDTPIvv6k3BUXg3dLIDYDy0xFkUHSW9RwbZEiOtwlcinXZ-jdatHJn3_wBVqgbGnXPKhcHfL7UIggfXfNw4UNnvrXE5aKiKGmm155AOLfAQR0WSkX5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-Vwcx2ATMc_828-bhr1Th1CLDTpV6O-JrU2YZReFu8QXta-KsVS_UVW8075IFNDEL0h5RfUFsLliytgIi48WnJ8bqKi6FA0srG2eDiz1UXOO7UUFjrYD-HpX4duv0Fuf6YioySaEw-e-bZsjFjFKnt6gTj_e9oYAI-hk3nnl__vEA0R-R_0UiZL7GW0bZvvITxqbZx6QvwN7YQctRF3OkVdcAdk6wuS0KnK2rVdixNyxZmNmmtMwD0rS7KbHaCfOutMjroLFYg70H2Q9u1ttTDRJlrYxHZOChrOFb01rCZ0DttNQ77knQnKWAlrzpm2tlfP05M1W_H_B0vv2nm0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vkgJXeWbiZTYe23U217h9lbY0xm9KsZppGp8zPLvn7MaD-MeLNHE_9yu1UPlQ6so4UqiYD0nCWDsPoDGyPxWS40ts8-zalrXrJ6pLdeMMToUQpevLmb0AIJocmJHzq5wUaBGbad2b_zAWSfRFuht20Yj3JbEySyCipUBIYfDVkP4CdDHw_eVmlIEd92NiQoPSItwAync0jHIju2XOlIzZFm3UgTUG2zN_CekQqUriYUHQAFSAo-RhSHkE5HQx2EObWvO3qCapYQC1pIQMDWSfL_2m1HxN2lFW7CPK8g7HUr9VWNBVEhKNNiMkLODwbl4AZ50LB_mIhDMYf-6Dt4xKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsbmz186mqZaBQK4gzXUX6oyzPKCBbMUmKJNYnM5UTvkomMUTH9icFnqQ4gnR8dvf7SpcPNduiFdCruyfFM9VRs1XXt60C37US0Hef1l9ZqZbVUeM1T5A_mPjypGPhBHuWvIiCVWCNbEDLG4m-tIdPCNGCzxECqy7zBmWeEH_mns7t_QNQrS5O8iCOfptLx4h2BgHP6KnlIW_GbZeqQRYvgG73ooQFAiY0t_O95i-lOwTWq3fopRTuv9w86k-o8VqMpzo9X0WnOTJhTMPJPb3yp1b33mH3cAvILz_t1M9MVzivZIsuib_ungyPuRZtzLo2GNuXP3A6pkW_Vqd_f72Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1sNDwAD3zQve35udSJQydO8f17W0CZDCQnavwD-XJlgwTpIQxxCkQlnMIioXafNM-m3_WrslCbtvC3ljMMT8k0ip_bwh8oQEkuxv_eXJj9kKJ_r2eMcxvgSG8G-7TY9ECwZQoHbJ_kCCbvG40ejX6f4_39Hky49RsO_QnBpekzI9aSUyEhq0ZPPfg1bzDA94YoWidKVmAbSYarRlyBSxNqOxQ93VxZXhnOKsTs-GgkWt2bRz0_0w8WuLKrsqNnWUS4fEvEbx7d0TlfSsFj7BTUHe746oYu-cN-3dRdChBHFodnBBS7zLmJZLn-AdXpONlksbOuKx8_HlbzIGx5fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuVhOHozvo4vlrV7FvM4_sqVD70LUTEdYS2cjoCk8-BTxcN3qBkRej9Z_FMKLS6m_MBlObpGyS8NjctfUKIb7vDY6pYPfiPJPsC38jhcKqCIkXHgNfPyRDKbsAt1owkILawkPu7CYEKCTbC2Y2aTTOi2GgI1Bc-zaNdWVK45FpRXmyJOnGdmH_ExNBA0KHOPdxkKC-3cqoelyKo5A9Ie0SJn-iOigX7K2H5gjUVaXFDfpsYOYS89V_9XQNLxlucMNgzhZPARVSxLA7Euqnhar51paOS_aKrO9gf9E4Z7M54ue-VUXspvMn2O2iVkoP6z7XMiefU7Gn830AzjRieuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZeFKTI9KLu5mi99KnOof30mJA0WH2Ssu3c8GllqnpDP65p46N7UdEJX7xXkJl3sz0BUllKUi3fq76G-0W6A0kJZzjl5f_yjEinYc9i8Wae5iIcdqQ_O01cbz6kPkF3vpJAbcn8F44UCSaxQ3AQx0A6Eep-3CHQlksQGj5cVrbzJm1uJIXsZYCL4GFKn8cQ4iDzEFJ8tzWpqZTwtPH27i48xcKlsP9ftEyBBekwdRnRpI7OAhQk6t678zViOJS7JqOD53Iq4Ed-8TGyRfqjbvbZJ2e7214XthGz0p-xUHdla1NPRtahioDb6oD4XGavvEu4G1CmvA5G1VtGGwjvKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جاییکه پیش‌بینی فقط حدس نیست، شروعِ برد های واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌ن
ام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری مثل قهرمان‌ها
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع و بی‌دردسر
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته، همیشه پشتتیم.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!
🅰
r17
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/31232" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG9bZn1saMpVmshqEtSDou6cU41eF51-vM9mDfVa1CfRIpoq5E1EDTwPa8_FEmzWrveMPY7ejNs46hZp_or3yWjJjIlztVJC5zODot3V9-b6wPLvHQtcVEKAODIUNws58pCewn_oYtK0X11niAKYRNACUKxWlZqx24UhNWwrhME6uHOR26McRDe1kNQlLfP9O3Y0KrTY1ZCZlgtkUtExKMv-rFPL0Co4cvO47mzDQxpnmVHJ9kG7qPwqaN8lHdMi5zxNY6RJIiu2Zg0V94WfCCqvA-dWwY4dofzT-m75xyVyGWkuYxTCe0Pbw1yejWUaOSALTwbZRjOalgHmlZ06CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPfcN95V7ywktdTHs7jAKChuuzSLGXn87C_EB0af_IlbcdxODr-cuNHMQ5mjm7uUqbM8K1F3eA7vu3TV5srSeE13gFZZKCsZ5GJm9XSTxVeNZdhC2-1uUfZc28rIPXnvJ68798MzjQdTLeCzPdOX6AqLIZaM4QOrypbzsVcJxQj21xHosmlc11o2lIgfdifxvBEtVICORm5jiltvn_udm-q2-zWDAXBv7zFZSZOnWn8_9piI5ZMCxHAFhAsqhy13OJHDvcPMnpWlUOD9juqpngf0zv1oK6oRJwTyLbwNBeRGBqaH4n8IyoS7ZEapF_fxTV1Np2TNJXrn0v_k-5lK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31230" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=AIt0rDGH9L8ymTb9Gw1mS7thFJnx7GljU5Iy3_8nTI5POD-cV3JF6rbgOGsWNK6YeDBTwUGE5ul1hRcHwKuJdii-0cIC6jNt7ORoUDWeTp0zOud2x1TfkGk78yhR4RNdqlPHbJsOOsfknZ-ohvLyGlZ3k6d8sn9l1zQKZxncAz1XygnNQma-0I6IZMd7sHNvUtGC-GuBiNQS7PGkgk_BPRyYM_90IuDJDbT8_kAePNILf7wbxIA0TIDnfS7d4IiRq_DYueA55-YlkdUn66o5J27t0Cmb0U--towxIq1zF2qgTEohp7WtVscDDt64VOF-hLN_V0Na-wKgDXdyROKPfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=AIt0rDGH9L8ymTb9Gw1mS7thFJnx7GljU5Iy3_8nTI5POD-cV3JF6rbgOGsWNK6YeDBTwUGE5ul1hRcHwKuJdii-0cIC6jNt7ORoUDWeTp0zOud2x1TfkGk78yhR4RNdqlPHbJsOOsfknZ-ohvLyGlZ3k6d8sn9l1zQKZxncAz1XygnNQma-0I6IZMd7sHNvUtGC-GuBiNQS7PGkgk_BPRyYM_90IuDJDbT8_kAePNILf7wbxIA0TIDnfS7d4IiRq_DYueA55-YlkdUn66o5J27t0Cmb0U--towxIq1zF2qgTEohp7WtVscDDt64VOF-hLN_V0Na-wKgDXdyROKPfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو: نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/31229" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31227">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBJG8VoGWtRArqggSkZ45sWqDP0LO4eKoLHVy7DqfUk1_hsnxOm7-qjY3zRg5-HFMxc0ONhFhA-1edP9oFnhmDNUAkpKU2O-DY0sux8e8z6yJjYSH0T7tW_V-Vl70_B8z3EeqRFKg994c_flr5j6XO_KiZWvisO-zZUxL3Q17U_lbdL0KzxSZXnjOLgto_pDdI2zi2KC3Z7VAqGxp9yjAgDJxukE0-9CnE-bbVs-cT1Tr0bZrs7GmsOCirnfRvLQ3y8JzVAyNr8rZGHssWKCaIsMkrJ0WZYMnnGlV9JT1hcKQsXocEQZicR4PRjtjHpmDthRgUnYRMFihltZPSA04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31227" target="_blank">📅 10:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31226">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgk7WrcmWjIinNKvNskTMy9Xmob4VleIPjgglD2fWxeq1s6KC4zCuDqIBhzk1PmxJ5WAz4SecVP__lWKeslxzk0kyOmMkJPlqBCwobfoKxK25zwMMPR86DLdeLftGdA1QoZD-Zrg9tt7lJBeAa-KcQVJLHaNvoS2CkNKn5NeU_mBUXSsueQSH3GY8YuTaqJj1gyPIT-2Gawwd1GaY5aJYVYB4JpbAy8MT1WWRSYdFh2lw21S5THN_oRIcATZRFh3DTEk4QbyEEJ3mubUCGF0vKNPa9psjxrfeLWipqh2m30SZhDDNSNb1oa4mdeVckdURhtOKVPUHANa-NgQg1uvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31226" target="_blank">📅 08:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31225">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcjesIShIhK8sdUCqphQuahEAbbPeNOikPurddx8cLM4cBiqWs919PVPmoUP9ntjMF7asA04xXxE_V2SGf0HKMcEgZU5Yjpvpj1Hsz9W8aUwTxTvGr8DWtQ6OvWkrSQ4g4gYhJGlQNZfD7pJNJ-zzkFY8TF0FelFFm6P9rjFFifrs9nAkUiy7lYig1-x1kupLLWJ3J79QPwcWL5B07chjODu--esxgMWGDQD4gFqc_SJci-aKJg4CWG9u2awATtvnhn5jtdnCW4MJwYFlsEQ_jzkS4SmfSV1weD8wDte3SgGkcDR_nfCOBoesP_Cx9OuHR5VO3P-B3Eqhk6ipmrRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از تساوی‌در نبرد استقلال و تراکتور تا آتش‌بازی سپاهان با درخشش حاج‌صفی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31225" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om6yiWgUfibJjwO_CEdCpLhq-_FNWEyN9679eby9waMcFmuLPtLsgTsGLdIpRJBeSgb0JofNLgiMR5X_Y6qjmf-izX-sMemkcITpvig-jLEcbCHDN_xqKU3c0WOjs5ZCp_W2wE-W8OnzeD7Va2Mf5a6c0sp0OGxDPE7GgEccOYgbVXswx4RYODDlXN7if3ZOh4oO8-U6Aw5pFWt3j-kG9ApjLb2exQH52NkL4-6wJ3YDNXjCvfB-bmexDt4NI6JoEp6OxJrpidKC2UzjLlYfMhuKIT5hRA9-qnvkX8XSFWaj2taA5yDoepSBn9edMMcMK8bYVYLl5P_Li8wZ4wvNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=XUxRbu2kZMmQzcUB1HregAIlKJWfRqPjlzI2e151DpPsPll0C1dCiHIqYX2w41NmGvlZ6fkCce9REKKo3jQDHLYxgdgWy4_15gErG0e7Xy3O4hVC1gfe-phfX8uIVgQgolOkP8MacgNoQ0Tipp7KKPRs2qndGBDO22L7SasRQOawm4kJmkTpTZydh3IzEB3UWkEZuRRPxlhh166nNgXTDO3cwNL_fXD3cWJoLfIjMZDV4aDEEhX27oLQR8VbD2RDac66dJ49pjRkxgPPNVDl6ezAUJJZDum94ofXEi9m5NhmHDgilWn1IZWOSYRnXD5z875cO2kN-pqmZVtIX-X80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=XUxRbu2kZMmQzcUB1HregAIlKJWfRqPjlzI2e151DpPsPll0C1dCiHIqYX2w41NmGvlZ6fkCce9REKKo3jQDHLYxgdgWy4_15gErG0e7Xy3O4hVC1gfe-phfX8uIVgQgolOkP8MacgNoQ0Tipp7KKPRs2qndGBDO22L7SasRQOawm4kJmkTpTZydh3IzEB3UWkEZuRRPxlhh166nNgXTDO3cwNL_fXD3cWJoLfIjMZDV4aDEEhX27oLQR8VbD2RDac66dJ49pjRkxgPPNVDl6ezAUJJZDum94ofXEi9m5NhmHDgilWn1IZWOSYRnXD5z875cO2kN-pqmZVtIX-X80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocpucCHuXrFJ0yG6G9cA5E-sc3vEnp0i9zHwLb1opxyNNiYZIiOh2cloHzaz0z4ZXbOeaCUZcAxk2dKfBbqS4KVXbP51OS4qG935HivY87_-RWt3cvVi8cDij41BaWvhuWa8W7AOFLzzOKpVvThssVOE7Y1WROdtY1NKy-6lAhCJSjlZLJdoQBYVh5eVIHCxFUD1za1g1bxYmhgqFDeNsjcJBkQ7WJ7mF_G8Xyt06dc5sYkuPIkBhV2xpA4j-wa988lwE2H5Z6qmoxMBnyxTvniYAbES6x69rdufzSFSJ6Y5_xTTxQl--0eUWcXoIw3SUM6CWpluXVBV5K3zVa8klQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qq6o5HdEQrkY-GMSG1t4cyoy2upQcdFXaAis5jtr3PqLmclzsNbR7ARIo_xtthNBSY91k1alta-IV0_imO0fHTpz0j7ISkZou4QksIsiMYlyl6WxTetBJs0U4nU7fsPtl4t3XaIWDJhGi3EpyLdN_3wsAbZ3mSHi6DIR5xgvB-r24bh5LtAUhO3rCow6nDXxcJg-XYwrkuQ_j5SWwVvfGej1gBxGKBMLP8j9Vcjl6R5x6iD9amm6SvOrSXohjYinrmiuSGmIp3ITOetH1odK44mAFqdShLEA8EdBk8VOxiJjcIaW1D_SkeqT8jXK_Oy3It8N9mkzeWaZbjHWIUMOCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_EgsKk_5PKAcgAfyakOJDWbkC7ldgHDr5BsYH9RQyfAFWYGrFyW-jSa2-KiQ0PneSq-tB0BMLRRa2yI46XYe0pJsTdheFIfLzQnxUnGo5ibGEkCCWW47b5L_F4GidFv3793f3vcYGrMbM6eEp-R-dKnuIZ0cE6EXjOasHQQ9CV30eUKjorbpraijZyL6LdxeR8Mr8A8BnRowTlZSA3fVoNs6aqxiZ0Qd0Hl2ufu8E4cTNtN8OvRYLeoWb11MZW_AAZ6Ex1fKzXkLfubjp8-wNLAoOg5Ui_fmVdxlp-QcLAnfZ-vUH3ByXREzUwMfvSzUreca1lHc74vIFhDBYZvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=L6ABSrcjym64gq6C23YDkof1ZNzhrcAOxljPrBKeiXgYUG_CkFj80Z2nm7gj7qqbXxVBWQ4T0ljxQCs8NtfX8nMTqArTKZhep6nHSIilxpjy2_feqa1QAOZ2fG6kJvsMpkPxPBmGJ-DGVF_C9dwnkT4FM_AxurPhXZSwj8V6JUY4Hrl_Bxy_JilGqAIi-dLB4aWt-y6vNSUYJQDuNBYck-hgwhRixHzuwJ6t3o19Tv1PKx8sX80jfP_f4jUMGpqKNfjb08cbQMWNuuVYHc99Hh3Am0u2DohUo0CB2rv2RG4QGtDUikkwNZ_dCRNPwSxtYN1C0xaa-dEwpEeUIl3FUrNEcWEQH26b-LvOprG7DeRhXePhIBo_T8FdkV76vm72pKvQ49UVqBWCfvTu50AuwUWwu51m7EaiAzaG71VhHDwwDa9LXYRcZURXha-XHFn0TVufeVYN049dRFJJFi71RpgEi1dDaT9dGdvhAs9-bfaUsZvTp82VzRL48PL6mAVvht8ceDsCgesdQoM_mI3dXDO0O0Qp_EmGRVPLMx_v7gerNIT49Ei2TAUJJ7CrIgvNYIq400jSUfcdGfVSJ19l2xRHroB-bx-inSKQTQHa0nZ1-vRn6gSyCMjb78wqMe6U6nR4pHcc1Zx_T4RRfbzoSvEgXekAr1XmwU4oQ-wjio0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=L6ABSrcjym64gq6C23YDkof1ZNzhrcAOxljPrBKeiXgYUG_CkFj80Z2nm7gj7qqbXxVBWQ4T0ljxQCs8NtfX8nMTqArTKZhep6nHSIilxpjy2_feqa1QAOZ2fG6kJvsMpkPxPBmGJ-DGVF_C9dwnkT4FM_AxurPhXZSwj8V6JUY4Hrl_Bxy_JilGqAIi-dLB4aWt-y6vNSUYJQDuNBYck-hgwhRixHzuwJ6t3o19Tv1PKx8sX80jfP_f4jUMGpqKNfjb08cbQMWNuuVYHc99Hh3Am0u2DohUo0CB2rv2RG4QGtDUikkwNZ_dCRNPwSxtYN1C0xaa-dEwpEeUIl3FUrNEcWEQH26b-LvOprG7DeRhXePhIBo_T8FdkV76vm72pKvQ49UVqBWCfvTu50AuwUWwu51m7EaiAzaG71VhHDwwDa9LXYRcZURXha-XHFn0TVufeVYN049dRFJJFi71RpgEi1dDaT9dGdvhAs9-bfaUsZvTp82VzRL48PL6mAVvht8ceDsCgesdQoM_mI3dXDO0O0Qp_EmGRVPLMx_v7gerNIT49Ei2TAUJJ7CrIgvNYIq400jSUfcdGfVSJ19l2xRHroB-bx-inSKQTQHa0nZ1-vRn6gSyCMjb78wqMe6U6nR4pHcc1Zx_T4RRfbzoSvEgXekAr1XmwU4oQ-wjio0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe2dSzLOn-RIOyMfhtjFTB8BH3o7hT76plWQV_nBMni7IPFpOUh9lJwk2zt4DdWAQ-H7xVcBnzv4CiaahczRjjcRVpElZ3hXVJKHhB31mOjr4acIjFLqAIoEJnM9N5puttEk0kmhBtXZPG6N5UEsID1BJRwO24NPOItvSnk49qbLrx4XgLhN3AwoKYICPFfWKkaRd37Js6cKaohzqff4yBtVevo5_qAsjmBr7Pl6QPYjOEB9VL5Nn0k_ue6_qJo0OMAt3fFV_7E_W36a-BPoDmLGmifLPnU3vnzeGEYDkVtIwqJjYajbsUyCmOPwBedTkLxf1lbiMbACXOFjqTdV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctNdIKfpu4XXM4ktvV0dBTkBftc27eTgNCnBlv9J7kJOPEEHxLMldCYYgzTRMLVKHlScruvY9Qaz-dexSwvvKFmTEkwyXBEX7E4hrZdXYFE16ZJF2T6ODg9KmtEk3O4A-Tbc9XiTqcuQDhg5bMMe1D4i_Q8Slizs4xGvy9dc4pcbjRkr2n_l9gd0B9O7y65ScUumK5bV-NIwpoM7TcfW6jOlXaIrH2L7r64BMwXf5GsvNmltrbpqECO-bOpmwSZc2FMmNH2vkoRsoEglVuVISWyWHmhw2xp5DzZShuLOQWzYv5X9zPodA2uZsq-4l4Xug_PzDx-SHonzC4cSrLjGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31214">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwZxj410pRyjryjYsJ-VCzsYBeUABRZUI4z4aIgSza-NfzovhjLEv2C-IfsQBza_e4sKBnyPDAWv-DoufhRAqCiZECmuyd_Bl5Rb4yvDoTVZNHlHJpshdU1W9O2OpfXIZYmCZAzc0oHo62hQriQHV_uewtXGectNBym3PaUZ5WXWWcS82e1sPVDovpp12BrzJviNk3iHtUyWTh3WFgDq3GuBzlzJ15FdAdZuPNDUJadIGOhpv52oClD2OZIDNvQqsxSqMVj3h0CjPB2Dcd71QHv_gQYqOYQsYFYcKSJRcTiidjSqtY_yq8TPbk2_czZGZEpF2H50NYDf2YLpxxAJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31214" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31213">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=q1OF9uDhs84YZttjF3J6mFk2tmqGCNEvGcpXKnutKPsnOLTpfGy2ioDELab4exynsbGUueGEzLOXn4xS9ft7_lk6FfWgf3tFssQRxteOJQNnyo3rOi7nLi66yE-GV8efPgUOP7VXz9q8YnjAMZhs9T0UJ8aBpIfnBQoEl-_hspI26XTPlJ-zujiMgP4KftSTqWjTnThk5n3oqu_UL4O2CoOmWL6kffiSA0GtSrfnMm1s2rF9jSr_qs70h_cDrMWk7RPXKxll2bSrnL9z5mQr9hXG4we5RJrjjqQIQG4m1uoO7T-Qf7fj-U6L8NrmMiFjtSHeyZbt3QvFKrcdDB_QUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=q1OF9uDhs84YZttjF3J6mFk2tmqGCNEvGcpXKnutKPsnOLTpfGy2ioDELab4exynsbGUueGEzLOXn4xS9ft7_lk6FfWgf3tFssQRxteOJQNnyo3rOi7nLi66yE-GV8efPgUOP7VXz9q8YnjAMZhs9T0UJ8aBpIfnBQoEl-_hspI26XTPlJ-zujiMgP4KftSTqWjTnThk5n3oqu_UL4O2CoOmWL6kffiSA0GtSrfnMm1s2rF9jSr_qs70h_cDrMWk7RPXKxll2bSrnL9z5mQr9hXG4we5RJrjjqQIQG4m1uoO7T-Qf7fj-U6L8NrmMiFjtSHeyZbt3QvFKrcdDB_QUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31213" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31212">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzUIoWDMQfmPVJONJM_H0n5wMGAV2xWeo3kAEoM1iCmucc_r0WqPc_4daPvIX_4GIy88mo3TR-98ChAHGrFHNiRi2JuDVBppJMjW3l9ebMA6Vq2xwOxG3DY504eBp390O-NWoY14tiKFG6xOFOzplel7P4hS3eho1ycgkBvRcI5BXkKBTM-bTQTpLEY6rtzYg8SH1lB1v2eD3GiycuE-bTeLVt-v0u5IYT-Vhu7-YkHFhpV2fx9DO_Z9gDG5P-H6r6rml7Mc2ZXRsLH2TuqwBR0S7OuDHXbh9s-LFn9rMt_DH-VkqM--ZeTMMK5voWznrjf_cx0VqotOsSeS9GFQqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش‌ علیرضا بیرانوند به احتمال حضورش در استقلال: استقلال تیم بزرگیه. من یک تصمیمی گرفته ام و 100 درصد روی تصمیم هم هستم. من نیم فصل سرباز هستم و بعد از نیم فصل بازیکن آزاد هستم و تصمیمی خواهم گرفت که به آینده ام کمک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31212" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31211">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31211" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6Wt1w2vkSv1vw5ejjpmuf0_SwyM9GhwIGUrCK-zlndSJ6FrP9Md6TQSlBakvdufwa-U0BdpSIddKrHtDbjJyrc0Z4DFN83rJqVPD0OFmuc3Yj1QHVpImPjJCjJxw5UflZBygcLxlTn8vUx4HVsyBwXLNUwSqyEEzbgmK02Whb_U9tTCsXBYVwz6-K5ySK-AdHbokXODDerfFEMFxidVqA3mKb7Rr7NTNolnKtwctlL8_XW7Au0sJEVTO72XsK8AxktGvL4dl5eWitCTehNM0iApH-fuqhaz57EYGHPC4zLec00PpCq0Cwv7qZqSyrKhKwDHzW_VlDzBWGh03EO3ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rmh-WwvKPTpLvYXX1Wvj3t7_-owGf1UzAkLGWrV3BWC8S2NY65rZftw_ALeBk3aMKa5ap2HTA5WGkb-wGAdPzH0EnH9VCG7Ad9sSIsZcqiZaxVWpqf0WxlNx4e0HjP_Y2ck36qEvnjn0ArRvYNwSGG4KHFbfkTeZep1flcLeNq5vzQ-puJa-5HLXLO_8aOBjJecik1eDenTEFsVZ1gCBQJkKVhe2KkN4-F6TehGDJDhQlsLGTcm7ETAKn-ho1WBvIcrmFdZ9XYrjVgHQVwf3vk4tqbl7zdBoqay6fiEgg4lGDCTQ0mLG1dkjByJCmalbHMpyzzY4-VesGZB44wuG8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
گل پنجم و ششم سپاهان اصفهان به فجرسپاسی توسط مهدی لیموچی و آریا شفیع دوست؛ هر دو گل خوشکل و تماشایی زده شد جفتشون رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31209" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=MnCshtO16y-NY9tfFXND0PoV6v1tOYTX7GzAi3QVbVJ39OwRCpPXloucUa7EWKTvLyIBKIUih7NVY2suUNiz_tRXgSksqlazuGjl3NAUQ7izOa3dEqJXJ9AeRbykJLNDMJLbR_1MnbHna3_V36Zk90ipdUotTBpymKIth4eM-UvNclX_RU0r157wB8fajVSQUxWCdIGm_5a-wcSGGTSrx4yOg5xlvcGG80dZPlKOibuMRGHJsOeSM95Efi6abgbUdMuhRfYQmIvQc0fv7xiJJ_yVyYfwxs2xXkZ4IwoFS8OvZ4bWsh5oESP0uk0KSal6cgdjzQ6NX0XCB5RR83ozYA3xd1l531yTxWzZCosr1KXKpzdOORWsntJQrpxiy7h5DtiMFBIj4XLJWKLSWji5q8BPt1ntAFvRIP3LNj6uNzI7LIjRTHDCaSSpBs-bVf0M7HwDJlXUNwUHeBg9R0NVziDenk-FxLHU-OO-nrj2bKTKECkKGbgLcF8FFVl77MJvVUMVmKgORoaRahyijsdg4U3Vuz9mvLOrCjmdykYqNN-5UIbCj8fSBgrOHAnjOVIbFxnjkOyzddiDeMqstjF5UUxJBAHoTBzdtEoDDFrJMNUDzipfHLUNoC2145XBUkmyWCZNM3pu6iy_bPxdzfB7CNefpIw35IR0Yz7G4xdKG9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=MnCshtO16y-NY9tfFXND0PoV6v1tOYTX7GzAi3QVbVJ39OwRCpPXloucUa7EWKTvLyIBKIUih7NVY2suUNiz_tRXgSksqlazuGjl3NAUQ7izOa3dEqJXJ9AeRbykJLNDMJLbR_1MnbHna3_V36Zk90ipdUotTBpymKIth4eM-UvNclX_RU0r157wB8fajVSQUxWCdIGm_5a-wcSGGTSrx4yOg5xlvcGG80dZPlKOibuMRGHJsOeSM95Efi6abgbUdMuhRfYQmIvQc0fv7xiJJ_yVyYfwxs2xXkZ4IwoFS8OvZ4bWsh5oESP0uk0KSal6cgdjzQ6NX0XCB5RR83ozYA3xd1l531yTxWzZCosr1KXKpzdOORWsntJQrpxiy7h5DtiMFBIj4XLJWKLSWji5q8BPt1ntAFvRIP3LNj6uNzI7LIjRTHDCaSSpBs-bVf0M7HwDJlXUNwUHeBg9R0NVziDenk-FxLHU-OO-nrj2bKTKECkKGbgLcF8FFVl77MJvVUMVmKgORoaRahyijsdg4U3Vuz9mvLOrCjmdykYqNN-5UIbCj8fSBgrOHAnjOVIbFxnjkOyzddiDeMqstjF5UUxJBAHoTBzdtEoDDFrJMNUDzipfHLUNoC2145XBUkmyWCZNM3pu6iy_bPxdzfB7CNefpIw35IR0Yz7G4xdKG9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31208" target="_blank">📅 20:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=TXvG_9vs8QQkgrKoZGkT56TECJ3idHnRgOME4Q3Vf0WdGGwBWHe-_PiOMNcAAJU39S9Rh4oTMatoMNx-KppsUFzFbml4lZvIItppoEsOX4Zx5O6OyO4cAy-QYYNl-IASZzvgUe8rKwp6qoAZxkRZINsp0p6BFqZlXjhFhPCvJON_0m53a9DnfYLjW2RkPvnYiUSiSWyDsJZyL-_PFMTmtkS_s43TZUEKWcePIafc8btwGK7Ur3S3wlenGzDLvGPVUSowIOcHLqhzfVhnpL_l_aJDIyW1_kmxOLCc-vmcdIfTpHdtNuJd32bSt2_p8O7B2Aq12pB6hSNlxSYSMDR70A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=TXvG_9vs8QQkgrKoZGkT56TECJ3idHnRgOME4Q3Vf0WdGGwBWHe-_PiOMNcAAJU39S9Rh4oTMatoMNx-KppsUFzFbml4lZvIItppoEsOX4Zx5O6OyO4cAy-QYYNl-IASZzvgUe8rKwp6qoAZxkRZINsp0p6BFqZlXjhFhPCvJON_0m53a9DnfYLjW2RkPvnYiUSiSWyDsJZyL-_PFMTmtkS_s43TZUEKWcePIafc8btwGK7Ur3S3wlenGzDLvGPVUSowIOcHLqhzfVhnpL_l_aJDIyW1_kmxOLCc-vmcdIfTpHdtNuJd32bSt2_p8O7B2Aq12pB6hSNlxSYSMDR70A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31207" target="_blank">📅 20:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVsT1m2PHovBl7TvbMf3e1lc4E4J3mzAvAg3u6XnBzK7G6zAtvTaQXfWNX-TSuz1hUVXzi2QvP_D207NV6s0QghVU9unHBNbb_0rNEqQuyOby3-Gw0-vSAvZkh0VYJIcXX1HnB1I3OZorTirkvMOYavXskcsVbI0anXreIY3QnFYbkIKGMHQc1mk514xfiMOj4MNVnYLG1AZycD4sBaMe0lIcKMraK01o2FYX_pyMWO_G3xwKr4JTp1nfrcsbsWgn9BDU0WvHZ0FKuK5NQIt1C7Y7PBIpqmLgdkNUP88J2xDmfsvXWQz1A4mrLQe38u5D6SllfeHtOwPQCSpXBPnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دونالدترامپ رسمااعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31206" target="_blank">📅 20:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=QPVBFaOMPNQyOMIVMYpMHAq_w_YptGpHC9RcXWnxjqL8dpd5OnlUU5gjNFdY5lA1ksvQyIugy56qqH69Hz6Y7zEcZb9_fUCfsLz_qVucFjnMydwctQslrLKXt58G05UEPl0-1e2MbYxU1o3ixlb67Krrc7mEY6I9XCTdNs-jBJVy8tkDIB01vpA-tYzkhPKGFXhvC7-7w8lwgC3OcUvDtdAXeNJIjIr7aT6o60JYVxtfyox7BTif72-g1lRX03YJ8Kosr2qUJhFRYea4BjKgYJhrLlSE3gjqAgQPPKg98PTLqjPZwu1Vo5F8Z6djFfz1Fi56PYW7BGOOGmY1XrcVHjp26OhSaPbltsuESForrLubvvRz-T50mnRMmFO9t1oNIAvXLNn9v3LThD5a3UMQFYuyUlQ-PjuCfsHLRXoc7FISXgRCuLTwh5Y6W6lFPUo3lKH4Bt9Wko4vo56IK2B38J4jxFz1cEqKY66RHa-9wKzqdEHBF0T13w3t7x3bs-6EESpceG5bJ_ULP_GY8OjR_O4Qd63zPj1ivigat00ajXFSqB4Xmm0hC82H8Q2KQuH2QtlYHkkF1_RomFIyha3debt21u3w368dUd0jpTNfQRpWTgUC3GMrGRdQ4MLYiM9CWgJwWMZ62IkYNyhNeQhLJPqPX7ajWM8fgS1CQOUsCIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=QPVBFaOMPNQyOMIVMYpMHAq_w_YptGpHC9RcXWnxjqL8dpd5OnlUU5gjNFdY5lA1ksvQyIugy56qqH69Hz6Y7zEcZb9_fUCfsLz_qVucFjnMydwctQslrLKXt58G05UEPl0-1e2MbYxU1o3ixlb67Krrc7mEY6I9XCTdNs-jBJVy8tkDIB01vpA-tYzkhPKGFXhvC7-7w8lwgC3OcUvDtdAXeNJIjIr7aT6o60JYVxtfyox7BTif72-g1lRX03YJ8Kosr2qUJhFRYea4BjKgYJhrLlSE3gjqAgQPPKg98PTLqjPZwu1Vo5F8Z6djFfz1Fi56PYW7BGOOGmY1XrcVHjp26OhSaPbltsuESForrLubvvRz-T50mnRMmFO9t1oNIAvXLNn9v3LThD5a3UMQFYuyUlQ-PjuCfsHLRXoc7FISXgRCuLTwh5Y6W6lFPUo3lKH4Bt9Wko4vo56IK2B38J4jxFz1cEqKY66RHa-9wKzqdEHBF0T13w3t7x3bs-6EESpceG5bJ_ULP_GY8OjR_O4Qd63zPj1ivigat00ajXFSqB4Xmm0hC82H8Q2KQuH2QtlYHkkF1_RomFIyha3debt21u3w368dUd0jpTNfQRpWTgUC3GMrGRdQ4MLYiM9CWgJwWMZ62IkYNyhNeQhLJPqPX7ajWM8fgS1CQOUsCIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
یادگار رستمی ستاره 21 ساله فجرسپاسی به این شکل از پشت محوطه جریمه روی یک شوت تماشایی دروازه سید حسین حسینی و سپاهان رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31205" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=i-FYmxKvb0I8I2lq6O1Bqz79T-bP8S0571AUio-LUmffmJlBl4M7ZYX_B6-51tN7Y9tPUONHFHdvW6ooD23_AcqReClCnunsRR7aUuacsBgpxDqIhh3SxmWlUiaYzJP8EzWkVJ2v2uipUfbz1KlVgyi3MLqfQEgfNsDWV7T6wXn9sG0QQMyFGXmkbe-zgAn8w4CZV2LZ7k1lRP6gLtEcrrege0MssgfSi-ypq_fK2m3WfKr3ES5K1qaTfPJhpnI5nb4Qsiym-NR1IpuvpcLYDMH_HrmukxWLzop2HuDySmoB2KzNTw_60xCCg6m2sirXH6xzPpjY7VXLkm0CbBZxUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=i-FYmxKvb0I8I2lq6O1Bqz79T-bP8S0571AUio-LUmffmJlBl4M7ZYX_B6-51tN7Y9tPUONHFHdvW6ooD23_AcqReClCnunsRR7aUuacsBgpxDqIhh3SxmWlUiaYzJP8EzWkVJ2v2uipUfbz1KlVgyi3MLqfQEgfNsDWV7T6wXn9sG0QQMyFGXmkbe-zgAn8w4CZV2LZ7k1lRP6gLtEcrrege0MssgfSi-ypq_fK2m3WfKr3ES5K1qaTfPJhpnI5nb4Qsiym-NR1IpuvpcLYDMH_HrmukxWLzop2HuDySmoB2KzNTw_60xCCg6m2sirXH6xzPpjY7VXLkm0CbBZxUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at32JDGUQTUSmbRbhI2Yie4pNGfWWgqD7FmuXVmQBq3_Bm3gzo1U3JEBhlTqk2Trb8o4dLcgC8oqig1fCzGJ5jIUvl3g3qMasVpNVy2buwRArCew5P9NhhfsA4eTOPE3KcULu1f4hFaJ2iPMz5C42qP5m2ht1bRZ6Nv14zXmuiKaAJjJeYUFMTsbyOmH-SIgqvXcJGIoI99D_1GpiWJBF3qeE-QyUhfNnxjaYHJbHAH6vyllTv0ZpTKLssFSJka7j35Tfaq7lz0Q7gEmhu3NgO_CjWcaWNNRld3T-1Ugsv0NRYLJOmq_COuBP5Dq3emMWdxdEK20xz2-KD0IgY-dow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O1JtRW4YF0GAWNe4ehgEnT6gCZnOxk1Gcm6uzgx4mUAzV52Cd6bN05ZjnXEFsFkLeN-o97Dp7-B8Owg0fKJY_DyUFlLccxcXpsHvK9wHBXjXppwka9e1zVq6guGszVV_90NH9DGAd0h6p79WrD2klrU83rRQ5HBpSIon7A38ZyK3Ey004bNSxl0lGu3O_k-l9vTYUon5fvvRM1z44R7kUpU78sx_NYeeN7NSPNd_8BKNrOqmhi2c5APvpgbNYoMUkvyOUAokcfMGjSqrEnnY0X1SKBvgF4CWC_su5X8jRZhyeI5Lu-YnCi2zndHE5UDGsmgvP8SrRZYXJKuk_xKOO04HPuwY4iX1XEreIJiKJUpBfg1dZ7nEdozdaesBMt5fI3_ieCsff91JhzuYY1xXctddmwBN2VRAYVY0tR_petuEnibe68xho4Q41C9LviI4lVja92DgvjK6ZEaA3eAjQLyprNMQjPFouJJAGnD1rSaoaE6-GQT-S_AW4lFtBy9R3AbW4Gwn0foWEM9JnWNAToV9UCXlNSnR2rhamD6gqw1ZFQtnu8a_yvLKfmZr7hA4gXFZUZlo-ypdAdz23iXu5la3ijMWxYOudinuGppMhCWlrwqoYYZVSAGPuQn-eOg9_YRL0Btqgh1FthmKZDYOauHHZYB50VVjfyk6NMc8Cr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O1JtRW4YF0GAWNe4ehgEnT6gCZnOxk1Gcm6uzgx4mUAzV52Cd6bN05ZjnXEFsFkLeN-o97Dp7-B8Owg0fKJY_DyUFlLccxcXpsHvK9wHBXjXppwka9e1zVq6guGszVV_90NH9DGAd0h6p79WrD2klrU83rRQ5HBpSIon7A38ZyK3Ey004bNSxl0lGu3O_k-l9vTYUon5fvvRM1z44R7kUpU78sx_NYeeN7NSPNd_8BKNrOqmhi2c5APvpgbNYoMUkvyOUAokcfMGjSqrEnnY0X1SKBvgF4CWC_su5X8jRZhyeI5Lu-YnCi2zndHE5UDGsmgvP8SrRZYXJKuk_xKOO04HPuwY4iX1XEreIJiKJUpBfg1dZ7nEdozdaesBMt5fI3_ieCsff91JhzuYY1xXctddmwBN2VRAYVY0tR_petuEnibe68xho4Q41C9LviI4lVja92DgvjK6ZEaA3eAjQLyprNMQjPFouJJAGnD1rSaoaE6-GQT-S_AW4lFtBy9R3AbW4Gwn0foWEM9JnWNAToV9UCXlNSnR2rhamD6gqw1ZFQtnu8a_yvLKfmZr7hA4gXFZUZlo-ypdAdz23iXu5la3ijMWxYOudinuGppMhCWlrwqoYYZVSAGPuQn-eOg9_YRL0Btqgh1FthmKZDYOauHHZYB50VVjfyk6NMc8Cr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=TxCaTVCtXTJslzEJRiLLEqKSWlf0jFF8ziCjKIG9goQZonNUMYDinFfwZJLnYf3KSxhJ6ttja2HqnySh-Xxk0k67UFbvKk9_eQjRXEqS9sbVYcTNlYZM9Ie-54t3pt4VI3YhJXXaLQcZojI_dwT3d6UQ6hCEkX2Oaur41cMptZvHo3axNCciHfaXUPBwNujeEolpsEa94N80hgWoBZEIo3MWFU-KNfbSX_xon0W8nPwHOMUPusaD04VdbmJEL1VABBQ60s73DVLG0CYByI0Ts1iyc9dN11Gg151sga_eGblGZj__0SZCMuPc3ePPpSJNlNDYAhttGCg4jK2h4X7bsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=TxCaTVCtXTJslzEJRiLLEqKSWlf0jFF8ziCjKIG9goQZonNUMYDinFfwZJLnYf3KSxhJ6ttja2HqnySh-Xxk0k67UFbvKk9_eQjRXEqS9sbVYcTNlYZM9Ie-54t3pt4VI3YhJXXaLQcZojI_dwT3d6UQ6hCEkX2Oaur41cMptZvHo3axNCciHfaXUPBwNujeEolpsEa94N80hgWoBZEIo3MWFU-KNfbSX_xon0W8nPwHOMUPusaD04VdbmJEL1VABBQ60s73DVLG0CYByI0Ts1iyc9dN11Gg151sga_eGblGZj__0SZCMuPc3ePPpSJNlNDYAhttGCg4jK2h4X7bsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seq0kjY0pwXelOVe1FU0idN_W_-jQnkpz1oqxCY4ANuvPQwbZONH6gbZ-uMV3XEG6_E3VITaeQkkPIdUQ0bL8lm0hTfu0u1-NElCCffdZOr0VrRKVuMRgqFQz2E2ZJL5qjDkjPo-SwNUf_8ERnHuiu4iqTUAzNrXqlFolJRXRjUcMus569UVxzMBP3DJKXYLWwtPP9EtYTWOa6_gLP2h5F7sV4DNsqLDe4_SvVaV1q5mO-tHiLpRdGwcGEkeDSg4FFvRAOwJGQInKaQ00e_ijmJxtfuzvdTCyzgDO7LzhxTtAkysjxikvEJU7UYdCDDor-KqvaC_1x5iXclusWpqAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=eDz-6CHio0Q9PqIxyT41R4etkFUIC0jn7nESDXhg-PEabMtonxsQatJw9fkEUcK5_Sq5uBbw3aQ7CAJ17et8IeDc8DnJWf_4TdbytAEO49aeK0lqHOte26oVfit2B371dbmV8K53I_D6JoSg293UU62V4oBBllMpymXTKbtS7RFXAkXRcjQTzlUzqGzEVDAWOz1j5J-IqEbB2UOcmhtEfHEMI-nrNY--rs84QhqqJFSBAC5-sphwnZEVLZcgRdgeT6FjfLXJTBkHkW1yboXc9L0sCgZTnl0MCenVAdPgMaIXk9buFFZ14ZSaM0GQB8uPtfN2JWEGwa4uUwHmULsg-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=eDz-6CHio0Q9PqIxyT41R4etkFUIC0jn7nESDXhg-PEabMtonxsQatJw9fkEUcK5_Sq5uBbw3aQ7CAJ17et8IeDc8DnJWf_4TdbytAEO49aeK0lqHOte26oVfit2B371dbmV8K53I_D6JoSg293UU62V4oBBllMpymXTKbtS7RFXAkXRcjQTzlUzqGzEVDAWOz1j5J-IqEbB2UOcmhtEfHEMI-nrNY--rs84QhqqJFSBAC5-sphwnZEVLZcgRdgeT6FjfLXJTBkHkW1yboXc9L0sCgZTnl0MCenVAdPgMaIXk9buFFZ14ZSaM0GQB8uPtfN2JWEGwa4uUwHmULsg-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول تراکتور به استقلال توسط هلیلیوویچ در دقیقه 68 که VAR هند بازیکنان تراکتور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31198" target="_blank">📅 18:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=sbjipnfx2Neai-ChwuzMi23RiupNHVJ8MDkG990RRJ7JqPRfk9Mi97U6YdRrloGUcAgLmQmuzjaJoxeY2HCllsF585hj79nlBmQqFtihfExVXi-riIE_1-tmqX_fVwFhWhEJjjzDAGHdkMz0HzJ81F6OiMM17uOnop60QRxHZy1CQHggdq8MO3XcZ-pBXHubuTdhTZFM69pL2ahfmQ9P7fppjkRQMeTBTc0SxbFX6XPBgnEua8ofYJ8Q0EAqdZaErJe_mDWXndo8CpZ7zWxSIG1RmVM_kDxoj1ilXwjGmx2Mq-AzhZcofplkfYfDAQcQfblaS_qQ-oJOTPyKAROm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=sbjipnfx2Neai-ChwuzMi23RiupNHVJ8MDkG990RRJ7JqPRfk9Mi97U6YdRrloGUcAgLmQmuzjaJoxeY2HCllsF585hj79nlBmQqFtihfExVXi-riIE_1-tmqX_fVwFhWhEJjjzDAGHdkMz0HzJ81F6OiMM17uOnop60QRxHZy1CQHggdq8MO3XcZ-pBXHubuTdhTZFM69pL2ahfmQ9P7fppjkRQMeTBTc0SxbFX6XPBgnEua8ofYJ8Q0EAqdZaErJe_mDWXndo8CpZ7zWxSIG1RmVM_kDxoj1ilXwjGmx2Mq-AzhZcofplkfYfDAQcQfblaS_qQ-oJOTPyKAROm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31197" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31196">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdRUN69FEE0RmrgnHC47rpRIxfL7YQ_Zm2YsTyksBkj2g_NQ_RXrkdZQNyRj2wpWTgq-GoE0BE4HcYK_YEpecqw_EKUxBg-V-nVB9UB4Pp2X-16OE6Ho16Kc8pn3o7OoWkGWF18c5sFWJ5404k1Z5gtjYXQVhYpaubfND7h1AWUbvvn8vPDc_x5bODsct5FOIQVGTw0BnCudykcQHwrcAX7Dr7-ME7Vd6wWxuO-grOkEt1WAfqwC7U99IhvwWS9XpOvAtOwFIyvHqI4noyvUlu0ml_fsoctWbLMKVyvOO2k908I6KZntX_UiQHPGKCkrbg3gTcbC6vg4Fsem1nGWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31196" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31195">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moeO1RMZWbZdBMMow7Y9mFERonqa5O2URR77KfLEras-5FeYRv_biu6NYitjNPrwFOTwSVUkiyCvsyRiPHoERCwL6GB5qv1Lakc1yCrERdkXjVeLqXHZaRrJkZKMk-WY137M58dIEt0MT6Uyc5D8aiSESVzF5NPxUApMVnIPWp_BRKNoiNanw8MtrYvD_GpKiXOGW3SzWb0cEYoanvx8Csqr2CudYKTFyce84pVnF5mAjAJM6WOKVkVeAINHPxLwptoVz583degJvYAvHzZ7SZJ-3-i2dKGp9iOz0dYUD0Ms-3z-UbrtFKXdT3DZA74XFFrCJXrOzKGXS4mBvq3sSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31195" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZrgoYKIb4KgHFZuaanskOcMW2tVX6NETB6Q35k7arPoP66tGEX0mE_VdJM6cmF42sDHJTFXoIwoH7-qcgFjaeg3X5Ddv2aGNxjhfwmlhizthlxpCwGpxmiG5p3UNH1FoG4RE-26aTMlK2KDgEwI443l1_ElYv-X3wba8bxt-pLp0b5ZsjpXhxMpz-Q_ZBrKCJCjJziEzZALNv6gb84idmxlCChOF_OgZveVqydJ9i7dsyzwjZMsH4FDhgr0YpMP1uMH5AWs-FHysuDzTZSRAdKd9ikthfnU67LPrbab9BCx84QsKXp_vnvzNSURvGGQxRYyz9C1AXoY1tew9J6Jxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lsqkCyrPk_KnIkOnkHAbG87SRs6QbWebkIA_5di0CwjyO0C3WRvHw-ToOP7dK4lFILJ_zwZ6q9Bdb7gOcW7_pRB8evKwqBo4v9gVYTNM5jf_MiWv0gMhyUl1bWo01kmDJqaVv9dwl-BP89Wmu-aqGV2NhdwXRzIcZmoSdeMmKJgQFAYW9e4J0PZKFDHIPx_ojZGpemS4baF4Mz7tsNW2ROHqlsWyjPHI00PA6BjlHUONorTd2jPCBFsiW6kqn3nht-MTK-a6er6NNBirkhfiq_glhpM1QN8mThpGBOV5ghEssuV5-F4cK93LYNHLwo1Fj5_EmqTzT4yFMoZKa5kzag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سوفی رین اینفلونسر مجازی مدعی شده که لامین یامال ستاره جوان و پدیده بارسا اشتراک 12 ماهه اونلی فنز اون رو خریداری کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31193" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b022014318.mp4?token=XBISmk_RO8JFnjJoKY_kdVOIqx1YuJDC29yMutkvzy3lZr3nkrcg1JiWJ4bLfBQfFkVlTR65dDO4xzIshL1HpdeYoJLclQvcOlIrFhAc3OOHvknPjRkkRtWIc0-vea2x6LJvECsaAiDYfTZlMBOAVeVGizGMGgfzncNuoahNc7oyDTDodHyVXVsnS1VDYbKZZfa4f8-la6J7DysboG3Uf2NcFuU4NoE9sDvHmoO_Oeis68nsP4JpZELt_hB2XQ9N_2MoYzLnA3-vjSPEe_kL6G2Knhf7c0avEgLO5gMub8PN8KCubaTC-_VQ7U6SW3ClPYic_zXakdR4E4L7Dfecog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b022014318.mp4?token=XBISmk_RO8JFnjJoKY_kdVOIqx1YuJDC29yMutkvzy3lZr3nkrcg1JiWJ4bLfBQfFkVlTR65dDO4xzIshL1HpdeYoJLclQvcOlIrFhAc3OOHvknPjRkkRtWIc0-vea2x6LJvECsaAiDYfTZlMBOAVeVGizGMGgfzncNuoahNc7oyDTDodHyVXVsnS1VDYbKZZfa4f8-la6J7DysboG3Uf2NcFuU4NoE9sDvHmoO_Oeis68nsP4JpZELt_hB2XQ9N_2MoYzLnA3-vjSPEe_kL6G2Knhf7c0avEgLO5gMub8PN8KCubaTC-_VQ7U6SW3ClPYic_zXakdR4E4L7Dfecog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31192" target="_blank">📅 17:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ9Xpqkd51WfMhZ5LBEiE4aecL49Q_WojYYwPjx-qwmoJrPxd5DtH8SqvkjONplyhtzjuLpBgsueRb3wgVEuElYEeUU71GSPZGVGtBW4FyLRvZQSO3S9SwJdCYTpsGo2COSJhBRd2Mzp5mE6EAxqgxLCPgQZmvRytVb-_G4ngqKxOvawgMDCWSDxSuXmf59XMUosvvuQwJsuq8iSpKVLf_DCtpagUGR0prd-QybugvL2XWRCH4erckJnEOUTkR6kygeojmvDh9ZjpUs-QBwoMFDvTtC0OPUnRZwZJsnfHaEd7YkUjMfZkeUCAsXgvBPNqzRCgyjAlXBo53_eg_DKZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
باخداحافظی پدرو از دنیای‌فوتبال؛ از ترکیب استثنایی بارسلونا در فصل 2011 تنها لیونل مسی باقی مونده و همه خداحافظی کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31191" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=gdYT-uVpPnNVTqGIHbZI95jWbwnc_A7sQGhocFzWLQz13046JH_8ofnkJxzGxFfa-c67jecURUvOVZEAAHDmmKzjtBH8Ooz7Kv7wz2zNmJPS1Nr8PpbTuPAUkop068Ve2Oi4ITER1B7_O3Od5T6XczVpgYg6x2y2wmusjh1sckhd24wWX5DAbxjqdsuhDVKB8WnCcMSNJJIds0IFAGYuTKF5U9CWEBaM3O4n-hqJmRgqVr3tbzyFoTsG1Xe49R0DXQXJz4tir5Z5QxTt-9WXhGOQ16Ky0RlKz5-UvgeYOL9VJdmB9I1UiTKjZ05-1s1WI_W2yL1t6yt7Y7avXkxrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=gdYT-uVpPnNVTqGIHbZI95jWbwnc_A7sQGhocFzWLQz13046JH_8ofnkJxzGxFfa-c67jecURUvOVZEAAHDmmKzjtBH8Ooz7Kv7wz2zNmJPS1Nr8PpbTuPAUkop068Ve2Oi4ITER1B7_O3Od5T6XczVpgYg6x2y2wmusjh1sckhd24wWX5DAbxjqdsuhDVKB8WnCcMSNJJIds0IFAGYuTKF5U9CWEBaM3O4n-hqJmRgqVr3tbzyFoTsG1Xe49R0DXQXJz4tir5Z5QxTt-9WXhGOQ16Ky0RlKz5-UvgeYOL9VJdmB9I1UiTKjZ05-1s1WI_W2yL1t6yt7Y7avXkxrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امروز مقابل تراکتور در هفته هشتم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31190" target="_blank">📅 17:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04026264da.mp4?token=LMFK57Pz19DtbuVc9ROzNr9C8yUcQ29EOiJ0w7BgAaIMV4H82Ek9mCWdFGCunTFsfQE9KOqbn87vD9O0fhh70Ab9148YiexaUqp21r6SpDSsJS8b1OYvjZGxMVOwQsXJD6zWauo2lBh9Ky3Qv4UDTLmw7U80W1XKbjg7NcKgyb7LdoPnJHgIa_aR2jUJOIgr25bBO0qCjzFE4nrdz4JU35g9vANae8rcrO7ptvVWhhILNjpF1I3j1KuiVCKgTiyxelyXsEA8KEouWitd22Y41IR515cebsoejudZtZv-EHQe8Avcx7R60SaIO2LZHnVe1CRj7agePXNI3txR_wgC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04026264da.mp4?token=LMFK57Pz19DtbuVc9ROzNr9C8yUcQ29EOiJ0w7BgAaIMV4H82Ek9mCWdFGCunTFsfQE9KOqbn87vD9O0fhh70Ab9148YiexaUqp21r6SpDSsJS8b1OYvjZGxMVOwQsXJD6zWauo2lBh9Ky3Qv4UDTLmw7U80W1XKbjg7NcKgyb7LdoPnJHgIa_aR2jUJOIgr25bBO0qCjzFE4nrdz4JU35g9vANae8rcrO7ptvVWhhILNjpF1I3j1KuiVCKgTiyxelyXsEA8KEouWitd22Y41IR515cebsoejudZtZv-EHQe8Avcx7R60SaIO2LZHnVe1CRj7agePXNI3txR_wgC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر…</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31189" target="_blank">📅 16:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdCfOQv84dGtmrOzNZHNUQW_eyZ1rImFokYoLSHpNdLCFrmqbKuFRu7EGqpCiGqz0eVhy9eovCze4n_1UFVvM0Ok_XYWIOoPmbJ_j5UF3mCDrEYXOvVrESSeJ9Ta5EopgkCe3DkX0hobQzvl9oate4gYZZatx8R8BEGqo9GYAZbTHpgL9tLtm5J0yanyzhYdoIeVndc-LzhxfGL-XprofZMN3IFrFZnQW9rWda9kPurQbIhxpAflhfFhodVkdPzcMx_JKZW6lRfswohGTnh-bnU7V308CdkQui54YpZEJKPBUiC_wVngRgpp4TD6qq1Fs9gZpTGXETyoxcJX5ns3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌پشم‌ریزون‌وجنجالی‌فوتبال در دیواندره؛
دو مربی به اسم‌میثم و ادیب 5 سال توی تیم فوتبال ستارگان دیواندره‌بودن‌که توی این پنج سال به بیشتر از 50 کودک تجاوز کردند! به کودک ها وعده میدادن که اگه باهامون رابطه جنسی برقرار کنی توی ترکیب اصلی میزاریمت و میفرستیمت تیم های خفن تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31188" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIoJDzil2z-XGk9sTQ84rurcoodPe7VfCZUsa_LtDHxhhcUHLqvFJVGeKEurRcETSCxBqqE48s74BxXCr2EaIcgI0reSWAKCUyTsfetZYFXgxSeQgESKL1LUHxJ-7QRlhD0zRaqPtMQPstgF5odM95OStlO2f5D575lh0pT9QLZ0h4EkDLEStr9vToc-573FTh0dcANbB7RQqVQfLl6tMNOXpIAUYlhR02Qgs0qD_PRJ-bhZjq_00TdUGa5DObxb5L5jNpDdVMSoaoWut4vZIP32F6rlEsyNSwu_qI1eDrCLBjzVrSmoji7e-pzcuJdbV6DAKirLbpnS8StWArS3kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب‌استقلال برای دیدار حساس امروز مقابل تراکتور؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31187" target="_blank">📅 16:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRhTqCze1M2_HAwjlHUGQ9ioMTKPg4veT9ZPnGvqJncTkikW_e0sZrrWG_TOz9hzR2gRWug2T6PV1sTy0quCTTpmh8ctJUs1-EzSjkI4YSokZMWRGOqA1sejrHuLAIWblrpj-FrJCNp9M0pjgkIprq9dG1PKhED0AiGPR3i34G8fKmAdsoB565A6VPh3oSy4vAPz_Lv-T0-YZ15lYWIJS5YkK6FJGwO0wIXY_I-zi4MnaaH4KuFgi81jSlcF8Q-bppZELcrZ_JRo80AmQXdSxpS0VEntbVOjTaY39qyCM25HeWt8bhq-IMNJcFgbs_rFfMfz0sSFhNPFoLP4FBAZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب تراکتور برای دیدار حساس امروز مقابل استقلال؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31186" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdVohlO6arF3MHBjg9VTa52wUtZ8AgkTTBXnLQx5U-QR4n1BIgVAFmsLiqqQQieXgWBs5Drup2i7MlL0ISUKghaZxQovn_sGVHgsfkKNcHSsi-T29-dM6vmSNbfC8BninwdQo7kRok9ZcZMJSmV96c1kG3e825XiVb9RNDoQHua-SZPlFHxElHVyPz4bxviBehZITADkrc5Rt66L4_3RtVs8iM6TGL9ErgllJzDt78ZTM-NU0hWA65ANDBLO6A_OOFDn1e0lGtU7U0Ctjuhcv1rv7gyrKwY4BbAYWFKuuO0Z2wHmAD75uZw0Q6e9Z3qio_sChqY7Mz8aZIDLZrdm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31184">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rpxHus7hIxvMYT2MSEzjzgVby1YcHg8KGkY_eFu7a8TOev2qMwRdqkZzZZv7V4zWtTYW6Fz5vKZdQYRUINMNkXAM0d-ARRSzgi3nMkWp0TBBaA0aOkyOOOMFAXJOoWY7vWln3WCMJ46VJQnXlQmv9FPbmXH6tKqdHGndZNSLgZZujqfnzHnANyz8T6hm0YZsYtAfXObB1aBQ0pdxHXZ-lM8pQYl057cPV2qI8ngrQtqdIXufzsv2XvmeaI6YO-zViEJ6iINE3EDo_NMp6ltUUQS4Jv67t2c86KEoZyh0cqRKrvpHxAjP2YymM4Cl7WwxNcFQrOqU6g6VHSNKKaxH2c_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9307641030.mp4?token=Vest8un-mPwYs4dNykVPoRlY98rE1gUxepxftXQ8SFBvIjyON8m0b_9_ecyF6h_GJXkNFmfXyXD6IrP-b9Zj8e6KAYBNKQhOMehUTxeKuBkaijiWUT8Pn75zE10k4f2VlOZIeFdy3k9oro5YdFRcFjtYy-xSa1UR_NsjnrVCuYVzVpV4V8oxnPotHseGfS8njdRC4hViAij1GzzlZs1w9CJUx136DwU8Zz7NdrmNBzJAM1meOR4DZjOrp9nKNMZH3GV3HRxS8zbp_kG27NIAXrHINWnm62PL_KGwMh_jGaLpsWJlrj5JqbanB5RZMZmzVei4kjEOEGyW7DTFN5_rpxHus7hIxvMYT2MSEzjzgVby1YcHg8KGkY_eFu7a8TOev2qMwRdqkZzZZv7V4zWtTYW6Fz5vKZdQYRUINMNkXAM0d-ARRSzgi3nMkWp0TBBaA0aOkyOOOMFAXJOoWY7vWln3WCMJ46VJQnXlQmv9FPbmXH6tKqdHGndZNSLgZZujqfnzHnANyz8T6hm0YZsYtAfXObB1aBQ0pdxHXZ-lM8pQYl057cPV2qI8ngrQtqdIXufzsv2XvmeaI6YO-zViEJ6iINE3EDo_NMp6ltUUQS4Jv67t2c86KEoZyh0cqRKrvpHxAjP2YymM4Cl7WwxNcFQrOqU6g6VHSNKKaxH2c_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افسانه‌یاواقعیت؟ بعداز ۳۰ روز در قبر چه اتفاقی می‌افتد؟ روندجسد انسان‌ها بعداز مرگ به این شکله.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31184" target="_blank">📅 15:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31183">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEdqCD97qB4ujVYLoj7l4VaSKo_aDT6HPDNMBhAXirNrydns9l4tSA6amoBMzAHVhP5-Z6Vresw1RELQRn5h5lMJLOqXeYdUaBSYxPZ80CkRaZVN6bjQ5Jj5XiZ0o6MFyaU1VWoxyQo-avl2NicuYkNjzvKaaCAxDZ-5khzKjg0RC-EH0AZUXhJchS_GJ2ygEVzKvQYdj2ocpfYcyEFAsaDNucUEXVibWsVbJeZqjomyjLC6yy0t9ygs9yPHMpEN_VkuKzl-J1JbDG-HlIh2itMYfyoGVo6NpeIizlduATUIfIQ5PxdWL1x_XTsLD-KAlQ_wDTMD6gcymiTqf_yrUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌امتیازکسب‌شده در تاریخ 5 لیگ معتبر اروپایی در یک فصل؛ یوونتوس در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31183" target="_blank">📅 15:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31182">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=Lub_AK6wYvRmHGpAaVbj6KON-5UQImKMnvu9ZjErB-Yjrt0418V0a53-i6DUJZPedZxmfCFEANgm9MZmyWlXh6GbbctalENFp4EAZlP6U7Fk8JlVsIjKBM-R_xEG3rPR8w2c21kbLB6GYrSk6ae3VSuvZnr_gnBJ4fHx4wVq2LtVsXi4Xar2FeDK711cGFWHYtOvRinVQofmqVP5I3VO0Vrz9nOAGMYYanfrFsnFOBzWJJpa8CcvYHXvI9CcUt8o47HCV0pBFMYXlcroyrMSJIeOk0LKh2OSYlM5H6ae6Nkopriytz_UKDjJfAZSJczQFyww7H369iJ1kiikatILwqKodKEuPOM2V7TvqkeNehSYG4EC0pr4_yyPm1H43ZS3scNlw3NSGKqsHuyqHfoYjGhgubQ6eKhLGOd8TT90frYqeYrGuR_FOgDz318OFeK2wNM0j4riK8-Da6xKHT-7VzuM0V5JR-dOIWA9Nks4JwgfKQJ36UrNw4jemtunTlj6xuny9IUM2ej903gsnRxupUN2enWcE1RfQUIkO8QfthBMYe-fP0K7GvuJySrJS_zqZ9DaknIKb1fkzILYu08xwTddlJyq1s4qUBvYx4WUaK9JB1nxZjRPGYO2ey4wv22EhAn_-uoTtf-YFAa_Eg0FlCpXbljo-0fjgBI_ddIdMpo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=Lub_AK6wYvRmHGpAaVbj6KON-5UQImKMnvu9ZjErB-Yjrt0418V0a53-i6DUJZPedZxmfCFEANgm9MZmyWlXh6GbbctalENFp4EAZlP6U7Fk8JlVsIjKBM-R_xEG3rPR8w2c21kbLB6GYrSk6ae3VSuvZnr_gnBJ4fHx4wVq2LtVsXi4Xar2FeDK711cGFWHYtOvRinVQofmqVP5I3VO0Vrz9nOAGMYYanfrFsnFOBzWJJpa8CcvYHXvI9CcUt8o47HCV0pBFMYXlcroyrMSJIeOk0LKh2OSYlM5H6ae6Nkopriytz_UKDjJfAZSJczQFyww7H369iJ1kiikatILwqKodKEuPOM2V7TvqkeNehSYG4EC0pr4_yyPm1H43ZS3scNlw3NSGKqsHuyqHfoYjGhgubQ6eKhLGOd8TT90frYqeYrGuR_FOgDz318OFeK2wNM0j4riK8-Da6xKHT-7VzuM0V5JR-dOIWA9Nks4JwgfKQJ36UrNw4jemtunTlj6xuny9IUM2ej903gsnRxupUN2enWcE1RfQUIkO8QfthBMYe-fP0K7GvuJySrJS_zqZ9DaknIKb1fkzILYu08xwTddlJyq1s4qUBvYx4WUaK9JB1nxZjRPGYO2ey4wv22EhAn_-uoTtf-YFAa_Eg0FlCpXbljo-0fjgBI_ddIdMpo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زرگری حرف زدن جالب و عجیب و غریب ساینا کریمی ملی پوش تکواندوی ایران که در مسابقات آسیایی ناگویا مدال ارزشمند برنز کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31181">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-COKro4VqdWHsdj7NlgMbdKVIrjdzDEbHGgoVXzyYuwYpWjAEcLgmC6uQRJaygzDYFeNB8KZal0joDCrwdJiPbR-Wt-6_LM_eF4cM2e3hrd3tXma174Bn3avQlt8DzZSa8fKdVisL0FXOicaWC6IS1fOAKi53KiVI-_ODmTLGjv5LNwduUZEyZsmOSyskHsxCyBP9OTt8ur8QroZM0vc9KklnvJ9qjB3Bbdje3eM98_sfwIQAQFgrqStW32nPBBEkmalVBS0gNvJY85-kvzskmYeReXe2QKzeuwHrdzMxMMVIdjf0-o2azxUkqEQ9DkQ5QYXY7_ibkKjA2Noiy2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31181" target="_blank">📅 14:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31180">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoPeijO93_9VQNGz1gW5G93eUR4H5xj6ISyTyR7w9dB2aZ9pFRQX7-YxAGVmUnQXwOdXCWVTCX9m1J5I5_AjTWRRbwmszb5ClkxulxCjRWQXIpvq9MWHjjp4b7V8nx5fLlveZvVDDxriF2uYIg6kjdtY5P0hOOqanFnzwzRL5F4SEcgmPi2YYOHkW5aN3UT4-JKrQdggv6ABJjEf7i3Cf4RR8dkpA7iMdSNDmuzKh_OD-YUtE9JXdN54CHQYWlQuTrQJONNAAt1jseGPC_A2LIgFrka_ZkESH7hqoANsU9r-AUBx4Sm7Np0UBuxTszaMi9BNXf6_NXdr6NfDqt-DDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31180" target="_blank">📅 14:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31179">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfpOCT6Tl5l8tQ8GEBc2U-41PhKSK78qOgRWLnLXnR9dVzLb2KUk5lxpM5285O0tAbhULm8gsRVu3tT9HwkJtg5SqdDa51DOlbXV-KjoZnmMyzXfJPSzNjxu0FuMpewsC1SkW2-044q4bGAPVquQCV7yPhS9Is3b_WUUQ2Z7_vEIWrT38s2GO_yrtjTTrWFzZKQn3JN6iV_Fuy__LM_8xQXoBU20-pdBnnBAtGo9z1GoncY8JxLdDOcaRChjWXdy9Fq7yrUZpm0motQthiVtB_y6q1DwwcWw7chVrhgAzkdz_gUNN1UTPk87C51PESuAqLFJ5ccgU-jxsh_YfV3G8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیب تیم منتخب دو قاره اروپا و آمریکای جنوبی درقرن‌بیست‌یکم از نگاه هوش مصنوعی بنظرتون اگه باهم بازی کنه کدومشون میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31179" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31177">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u19Cv-1AzOL-rgfyG7JnPJnj3rikUYdXqYM-2Vervdg16zfb_bj80RywzSLVqiJwZPxOFxwTznKTRWKYsh-IDHYX_DwVedN5UZIGYRMY06f-YiGIGc4P_e3jvSMIrnLTf9P8h19naQMbPkHWQszze3NtUbAWn_Z2ASE0Q9whHzHJ9BGJUQZhe0RR5rMi6sLuD5gmxcvXQ9elNmZIvGMlhIIwfhbCqqmv9snrgcj9MR9SnJIroayz3NoPcRRuMO6yqYz_OAy3TIoUtALov4Wou5wn_TeahznlxKV5YyZqggWCoiaQmY0PrdanuhiXBg86Vk-N8PUPd3Lvmwz27JfMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WSVK43aD5PJ7AioOMBbOcQfgBUztHkZulKZ54vQMW7i89ZIQCwbpxdm8i5XjHr09Ql06f2aoQCwhDQHZoDVRVD6ALzn464iqQz36jHyhfYL4gEZTuEUtrtK-2u0DWQpdIyXdCSXifN9mqmt90VYvqrrvEn4vOTLWTwZiEHIuspSjMgVa-f0IZYmvei6N1DAU1whKMKKW2j4761sXvRU-e-g0IAP_UqcYJQ-C0I0JRxomYkvDyEBQnUMKu1UJSTKEnnG18da-XIH_fHo-eOlh2_upGcP0gP9H-DqAMv3RV_pHdYCz5kN4qADr0W2vsY5qO36BCcAzE_OPCUh8yQZHWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج‌بازیکن‌برتر قرن‌بیست‌ویکم از نگاه هوش مصنوعی در دو قاره آمریکای جنوبی و آفریقا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31177" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31176">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yru4opVs75636m06872IEH4PZs2e4pKiGcMrP00EOqMbtWChsX_CzKquuwYSkV9zOO5CtZA9wOJwXM949fDOhcjEQs-uaDKnBAxc9D2B3QjJj6aEb1SvZxNvaIiOd7u-XxrsA3qB1udp5GwfJcAsDb1raLR9vsVUMqe0AFsJu6c9d6GIbdTF7oZALnrujUhe5ICpP1S5KPSwVHcJmtSbtMyTQDR5C5sFwwYnwLnX2TWfs0LDRlj0yk9pXpntG4jiEAOHudbxs-UqBqust50iNlJwWRpi76T7QyZIiWhcC2H6f_xBCiCBvXZ2me_iI_ZeKM3bqix3vD8VUfTRouBhMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31176" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31174">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCogmnJvDBshTW8p5jPFXtVvoLurKQXjGPfVLia8rILo-PRDr_ILb43-ZEW8YHRCi6wq1Z9VQ2A9uhAU5l-sRny_9TegMlXxsp_99yign10G_UtpDLYoce9Dt3DhqaNAN7JcnS-q0SIDPSXeu0j5UAElpYEgrPZjMU1bDSes48bTCg3LERVSPS7EfReOhCVsve_QE1ZVqwncDI_7uFkg44U7tzoKiRMPobWEwFwWXCds1NfnOUj6o2HcpegR0attKA1uKVS2_mdZNj8aYE2VRn5RBxcD_jaigR7tvYko0pHhZVLgT5Z2qwK7HVhfLnZh2gocc1dX263Il_XFzHbnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد پرتغال، هلند، کرواسی، ایتالیا، فرانسه و المان در فیفادی مهر ماه با کادر فنی جدیدشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31174" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31173">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=dUHz9cCyfTt5k_LR0IcM6iz2IsBRGRjYbpPyHqaC-O9h-OsSLsTI1HbGzcOJcX11GIltxlYQ06NtSZOSIneLqvt2HiOt3MeI_yfJ3ulOmgrggG_1GCIoI8DenZq2apgJVMd7JyBNJGx_SkN_Rt7oE7Wvyr73rWg0uDTMlF5q31IUVjashshZGGXy_ZLhykh1mlMUj9LdVRAMx7fYIize8UpYS1rkEYsOMr_6I6MGlsC-X_iAgMWeWYjSrMGhO3LcqbzgAOpymBXKBMvynD7ns94lD7kYmT2QOoSdvvbWGM7ap1cn4qD3Bl9LS8VFybBwkKhqI_VitJWJZcUPFqpzR0_zmBbs_4IHkqVg2qlIBXm6IPkafcW97oPlgWMVh2qOllPe2I9gIFtKPsoM28me6cpT0B2ZT_7UYzs-EV0TIXQWMowGlG6M9UiIAVVEDiZooltPQLn8ytdmm0Di-zlo8Bxah_AtRpT4p9BRMYlzrcSdOEm2knHCuLOc2USyCkmImseqG8pE0UGY5ipNR96R80dtvnUMEKkjrDxb3SAubTM_Jo6wnX-hMYu1t1CiPUiucAcKljwY_g7HaXUOZqex36OXilMIab3ixwqeho1-iGR3nXINodDO8S_GW4uUAAkq-l-UyVx0UY_11f11v8DmFJzSEe8QIiQU9pm6TnnoKRY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=dUHz9cCyfTt5k_LR0IcM6iz2IsBRGRjYbpPyHqaC-O9h-OsSLsTI1HbGzcOJcX11GIltxlYQ06NtSZOSIneLqvt2HiOt3MeI_yfJ3ulOmgrggG_1GCIoI8DenZq2apgJVMd7JyBNJGx_SkN_Rt7oE7Wvyr73rWg0uDTMlF5q31IUVjashshZGGXy_ZLhykh1mlMUj9LdVRAMx7fYIize8UpYS1rkEYsOMr_6I6MGlsC-X_iAgMWeWYjSrMGhO3LcqbzgAOpymBXKBMvynD7ns94lD7kYmT2QOoSdvvbWGM7ap1cn4qD3Bl9LS8VFybBwkKhqI_VitJWJZcUPFqpzR0_zmBbs_4IHkqVg2qlIBXm6IPkafcW97oPlgWMVh2qOllPe2I9gIFtKPsoM28me6cpT0B2ZT_7UYzs-EV0TIXQWMowGlG6M9UiIAVVEDiZooltPQLn8ytdmm0Di-zlo8Bxah_AtRpT4p9BRMYlzrcSdOEm2knHCuLOc2USyCkmImseqG8pE0UGY5ipNR96R80dtvnUMEKkjrDxb3SAubTM_Jo6wnX-hMYu1t1CiPUiucAcKljwY_g7HaXUOZqex36OXilMIab3ixwqeho1-iGR3nXINodDO8S_GW4uUAAkq-l-UyVx0UY_11f11v8DmFJzSEe8QIiQU9pm6TnnoKRY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31173" target="_blank">📅 12:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31172">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZzm-_BRAJEHZ_j8-LuAiw3Lp4_eLRT6c-Dld5eMyOw3crhGaGqyEvPsj5-bIIakSXVr9M8D2DmcAYGjcwwDKcGw1CGpQENHShXjmTjk_WwW_WXmmlx4SOcs-599CBjzMuexBe2TYaCNDKd1RaPvGzPQjqxoqmAvRcNyk11ihjA3mZchHG9maHmdFojJyzcdbH61QZEdZ_S4iDiWb4l0DuT2pQV62_jwlbTpOFwIwOYr3UNSt9toyOWuj0RxXD7rApRbqY1gDUZOC1sjN6wdQFtBOiQoBB8KbTYNz-BJ_m3dOpZyANU35ynQpHx-DYG3ksodF4nBd2Ad_HJXpC-hcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31172" target="_blank">📅 12:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31171">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMNI9SabqYxhgcsEeWaIy5Y9YL0onVX6WEl6dluz-SGVZiXAFVBYHiVb5cOKsjx6vIDA48qxZhR6rahIqP9t4jZteaTvgm7Vfv_D_Smz74qKdoG3hEfvnHlz7ynlQ8bKTvSBrQ5THC3_YwcJOgt-RiQWW4cXgMo3Nng35bO8EQYbhUqIEJTjoZpbZ2mZbNveVYZpCmeGedJKaV0ABdjGWP-ASR3ufCvTtT0gwFObGJLEbc-pNs0_nE-E6rvP9a9UOZb0bKEsFp03pP1cR4B1CSBck4n-PBEuk1NtDea516FEhzAj2UT8Zqb2bRwvMINtNHIqCOGNDxoS9qhdq9fqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:
«من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود. اما می‌دانم که به‌هر شکلی در مراسم افتتاح حضور خواهم داشت؛ چه جسمم آنجا باشد، چه روحم بعد از مرگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31171" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31170">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmPKwcpaohcs9Da4nYF9qq6DKOo6Dc4ske0CMHnt1nydXFYKTL2nA_rN-O7bxPqNqeARgq4U2en-x7ySWgF6FMd6cOxNbTQTGgbkDKVhUNMpPzCyAJUw-GwnhmLsHtuwDdJMKazZUYvg2ICZ0L9-76TinlNiadceX1GiPnaOIGWqd-HY5daNntRgvEF5nq66bOmO_USw5OsF6qJpXJepXbwPqEVpj-B_deR37oOujlYYo0LvkUTGiuFXSbDFaBggCN35Tn5ynjwPvq5S812GBJbcyZY6wsdRrfhsneb_sk4mZ90wNrcXNPaLjMfDsj-OJn1wRJ7gPum2_-cWmeMj9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31170" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31169">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpUaK6r6O7ar4hhJJIeKwu31refJ1OwmpXGvl1Cm2yTf6NbFTJpm1pYS3mwrbFBy3COKBhJnm6Z_jXqwkiOrDcJqn_Z9KSkx2182TieZen6uxtTQU9mITmwCFR8lyWKqCThxUBSUdMd4wMF5IT9mBX8vL9GjiFBd2zkViJYyhAOnyLQIPx_hddoOcpNN94WGixizaTPc-UM6Qk4azKwLNctnebMX5-gmTQJ13qPHZ1riidDogMwi-JBDtVC747FUFckyCU9z1XyltLneHtoN5jUXUP_xmF4pAbIl3N8TEC_JGbelMZ9133laF0uxA3XQK2g9R2KxBHAGYo3c6nZV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل تراکتور در هفته هشتم لیگ: حبیب فرعباسی، صالح حردانی، سامان‌فلاح،عارف آقاسی، رستم آشورماتف، حسین گودرزی، امیرمحمد رزاقی نیا، روزبه چشمی، اسماعیل قلی‌زاده، یاسر آسانی، سعید سحرخیزان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31169" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31168">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=Ug7Q4GuE4LuUman37rVDxlr9KVtk-4bM75LxLnDXBHZQJP8mSE77PsxTHUv01d4nzpxVxcjNxBxAX3eixzAeTlzX3ODFp852Lw9ZK4NnhZeea9PkGGSCMjUExouv4-ksGgmSU1xxqyThkLZLmHZ1aNzk86cbXPSP2oWT355XkyH6DrXtRbSMeOApB01JsRSOw6UViwSoNs45HfvuiamlNi3x12Zk-pNYP99VMIJd4drN_2W1id-RQraqQu60WLtBCOclyhMeLy3KhGed0SD_ee0R7QTJ7BCIzlyTUAN9fgjle-Q0WIRT6k0bXkm6Pviz0IPHyQLY74wHaQmRLwEbfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=Ug7Q4GuE4LuUman37rVDxlr9KVtk-4bM75LxLnDXBHZQJP8mSE77PsxTHUv01d4nzpxVxcjNxBxAX3eixzAeTlzX3ODFp852Lw9ZK4NnhZeea9PkGGSCMjUExouv4-ksGgmSU1xxqyThkLZLmHZ1aNzk86cbXPSP2oWT355XkyH6DrXtRbSMeOApB01JsRSOw6UViwSoNs45HfvuiamlNi3x12Zk-pNYP99VMIJd4drN_2W1id-RQraqQu60WLtBCOclyhMeLy3KhGed0SD_ee0R7QTJ7BCIzlyTUAN9fgjle-Q0WIRT6k0bXkm6Pviz0IPHyQLY74wHaQmRLwEbfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استایل‌جان‌سینا و همسرایرانی‌اش دراکران «مچ‌ باکس»؛ جان‌سینا و همسرش شهرزاد شریعت‌ زاده در اکران فیلم«مچ‌باکس»محصول اپل تی‌وی درکنار هم ظاهر شدند و توجه رسانه‌ها را به خود جلب کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31168" target="_blank">📅 09:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31167">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=NoZZb8TV4zEur6MV8SoM256EkiMpvWyjkYEz96Lpbkf1itvqXGEXOuDVQg7ZMuOM0FpnWPSLQE0OqEzuAd-ESLy8sOin7YFmLxKVOOaBVHjBnS9DS48VhMHIX8RMe9fSFzeFRXfL_p0geseRkBEp1SS6bITyWqzq05pI_QBUfH9e-fZ43hcgpgrGEnBPMHfUb0M09NiaeontC3soPNnYmSkrwQ6jZ6PT3FPwsD99fxzeCz-fT-sIvGfxf2jhndIFrIZxTBeqPZfMs-1W01JAbFDcNwlwzuY_DlcZVpsj6bTnPqPEWyxVUUFO2kCjkGHMEfuL55sWrz7mD9yuIyG3Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=NoZZb8TV4zEur6MV8SoM256EkiMpvWyjkYEz96Lpbkf1itvqXGEXOuDVQg7ZMuOM0FpnWPSLQE0OqEzuAd-ESLy8sOin7YFmLxKVOOaBVHjBnS9DS48VhMHIX8RMe9fSFzeFRXfL_p0geseRkBEp1SS6bITyWqzq05pI_QBUfH9e-fZ43hcgpgrGEnBPMHfUb0M09NiaeontC3soPNnYmSkrwQ6jZ6PT3FPwsD99fxzeCz-fT-sIvGfxf2jhndIFrIZxTBeqPZfMs-1W01JAbFDcNwlwzuY_DlcZVpsj6bTnPqPEWyxVUUFO2kCjkGHMEfuL55sWrz7mD9yuIyG3Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31167" target="_blank">📅 09:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31166">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=JYek0otn5UBbde3OXoenJwMi2ffE4sXndI96sv32bJ0pUZKQLGGO36t0Y1ZxQRU5moR0e3ZzKrQOq91E-hDgkdzQscDO_3155ZzRTKFSCblUVw5LxEEmXeogcxlfG8YLYuEJBc37BwWWerlqfU2yQvNL-VHdfo118WkVqBGtN9YDQdySnWZ-N39HQmrvuu9vPmv6XqiYqI5VS5mx5uMD2CsEMuGuyjwdLtE_ypzY6FTPo_7Y0gXyZA_KQ6gFq0x5c8C-C3xWuVAlf9I6-N3EWd1Zq54unjl26Imdqs72essCbOF-6NQYgRK11YvAuCsIZK5Dv-yeISVXuOXs09jD2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=JYek0otn5UBbde3OXoenJwMi2ffE4sXndI96sv32bJ0pUZKQLGGO36t0Y1ZxQRU5moR0e3ZzKrQOq91E-hDgkdzQscDO_3155ZzRTKFSCblUVw5LxEEmXeogcxlfG8YLYuEJBc37BwWWerlqfU2yQvNL-VHdfo118WkVqBGtN9YDQdySnWZ-N39HQmrvuu9vPmv6XqiYqI5VS5mx5uMD2CsEMuGuyjwdLtE_ypzY6FTPo_7Y0gXyZA_KQ6gFq0x5c8C-C3xWuVAlf9I6-N3EWd1Zq54unjl26Imdqs72essCbOF-6NQYgRK11YvAuCsIZK5Dv-yeISVXuOXs09jD2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31166" target="_blank">📅 00:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31163">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iv7eXoJN2UYqokh3Fr5i5UxXlN4nDuGCB7MSPujq_uES_Q4USWn5AbNFFr7DyiO5k53QO8vihIuFUsb5tPUyg3G4wZazylMmnl_6oQjngJtRbqmPeii9aJiMjFdTA8Zq9Z7YLNWIWUv7xgB7eSDZ3BMBjeN8ifFlqHg0Xe1Z5Dn34MmevswT07kJU-9Ov0nzrz8RwE8-wtUZRv1Y6L59VKtEs6up5XUptpXfA5fNSfSxPMI8z4zCO48yC2-1ZsstD577xC4w7YulnTqU9dAj0jx2EtAiJrDlluXitDnNEh5VdeDtf3OmkHe0R7rdstpTobhTuc1QvsxXKayApYbS6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ بازگشت فوتبال باشگاهی با تقابل حساس استقلال vs تراکتور در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31163" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31162">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI-sIjSWoxioDsFM2lrxn78q1f1_ioF1cUzVQAyEPOsD4RIGUuxSuEh4CNKNwMpfUwil_1xPmYR9KJTzPCHNzDx0q78xXkIDDPTEzTtv6aQC0LvWOoWAUQLwNmpMYhEHfwLVd9WH8-fg5FAXQYN8v2Pa1f6T-HLiDf_mUO4gEcSl_fHy1wn5KATInwqKReNLEHesL4g9V7EDME5VKwwbL4ZudV6uGSLkWiGlQ78n-xFGA38qTOpmNz32uDGLWUxg3akOaJFSaPtiTJEoI1pY8jM8F2nKVX-vIyV4-VXcDTp5HNR34w9-Dn7ofjNllYGcQV3SIgQBDhNL3TrImZqJRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ لست دنس مسی با پیراهن تیم آرژانتین با تاثیر روی هر 3 گل در جدال با بنین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31162" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31161">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMnXj4gDUupYWFeKtoHBTTc9fg1Q-pN-ZuPQskOIH5OBR0ixZyvrM9OGOuMkVJs93QSWsEdYmZEl06aDIMWifBlau4qLAclhaT_LCxgEo24ma1_DCzYC7dHfKT85rDF5W5oZExNdZMurWXNezzs69n0bX-o-pSXRFEz4WSg2e6Zk55y3FL38qCrcapQrE5mn8HMRAIOZavZodlongIaA7Ej3nNZn5gWCQD3K4SDVB_A4O32VkXhVd1X-lkiSzNTsFUQGmQBzlKpFd-yOabD68ofqnUCwAY78S65SIaZy5KrWxaK7EoLDW4Myp-duGsrdU5ajcBvEQMVi02Fr96FlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31161" target="_blank">📅 23:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31160">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_4IWeliW_GqoGssWLifBsMVwKc0WWVzh7bXjB91nKof-5IPVwD8ur30TjRiv1owzb4h3YJcLoD11ddmsKeWpQ6YZHgjbo_KFfxOFodgVpmlDotTOh2FKsFPZlLwyIdlSYWsLwlbvjezHSl34OSC-CVViYA3mXqqBbvIn-6-gioYSpOQMaoXueWyfRLGKRVH5yTz9WlvG_VjtaYpXQ-2Sp7VQxKcNd5DHR4FLNRSsAkmnO7Tb-6R26XYHN64_35TbFWm0edbyxcSkoCky8vkZ5GLO7GiyauiUqbdXw6kK1jSbvFJ90dMf3GOrTycZzFgQDkOPiUWVrfyyJbTG4PcfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه استقلال به جمع مشتریان مبین دهقان هافبک‌دفاعی 21 ساله تیم الوحده اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/31160" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31159">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=RXQEq6x84aG8LFk1wYFmhG70cYqs_0hBCbQwu9s8vOXcXHiGwjUhBjO-dCWIZQh237ikHgp544PdaTmiIQSQZxCo5D8UWw4YE6UGLaHGax4TI2o-iXRKhCUlD1t5Yyd9alnkGy7aJAeZ6CkPAY3gjc-tBBy43JdCrW4TID7aEMdmvPX3xaxjPiBUqcLcdN70lXztExAfeNC2hRhGLd1Lcayy0h-52S8-EAiihLnK1y4ZAuVOgoixAUDBBRaDPU3dhbsspmBGT4hjKh6hCd4ucHbGX8I3NNvOjHo5rLxxK1t-Z7f8x2Ygh1KyGJtqcuQR2m8gXGAa9RsE-rE9K4eS1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=RXQEq6x84aG8LFk1wYFmhG70cYqs_0hBCbQwu9s8vOXcXHiGwjUhBjO-dCWIZQh237ikHgp544PdaTmiIQSQZxCo5D8UWw4YE6UGLaHGax4TI2o-iXRKhCUlD1t5Yyd9alnkGy7aJAeZ6CkPAY3gjc-tBBy43JdCrW4TID7aEMdmvPX3xaxjPiBUqcLcdN70lXztExAfeNC2hRhGLd1Lcayy0h-52S8-EAiihLnK1y4ZAuVOgoixAUDBBRaDPU3dhbsspmBGT4hjKh6hCd4ucHbGX8I3NNvOjHo5rLxxK1t-Z7f8x2Ygh1KyGJtqcuQR2m8gXGAa9RsE-rE9K4eS1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو زیرپست‌لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشههه موندگار می‌مونه. بابت تمام کارهایی که باتیم‌ملی‌آرژانتین انجام دادی نهایت احترام رو برات قائلم. یه بغل گرم رفیق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31159" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31158">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFXkU06l5Z6NjKhP_e2aCggTI-7wGG0T5ey_HoXl-R7ij_fUjIWfFT8GoRm4yZrKbFVbfR51KKxbpx8AWHoi3wXIBAmrKuaDj5E6iSeMnNHveupq6gUENzKVpbXesVnaWtsVqaY4mAqLcMjt68Sw1Pw7BvYzxIDYN7HLF9hmKO07Xee28q876XiAwb0yrF0p-YxZgcff2Q-tk-pSqxohoFBTIcWxyNnn2X4MApZkasUEu6m25npE8QJAZlUNotXlauHw47LhkmHzbNan1P3OrLajKaIRYhYyU0bvSdYEURsOwy-SEEmmEgtw6oUkL9arrw5s8Td0HE9iFyvRAesMuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان
؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک ۲۳ ام جهان سقوط کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31158" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31157">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uX49ZJkt4JCn-P2MpvzpkYnBjP9xpgSHJ6uxpmKSkEwJuWQ1ufketyVKY0AkU4Cj5fm7tOF-YtCCQnDdd9BJKbrQfHZ2ha8I1zqbLacyWD5Q16ctSSX18xvijn3iK19mVh-0TPBRZhJiuV4dbSIkCHl-3WI8kyVDPcYbcEV5lMNhHk3CXshm3PtA7QWC2x6qCqbcmopNmprTMg5t6cxVl42IRO1iufl3pzY4f6u6odBBOzHIBZk-wOAicCyruKeSVXBZgVKEI83SqzNJc0jTQVmG8-VEIBOGhNggKwQYD8Y4yRcs8JbkfhFd3uBTXFNwFp_NKZB9wXnMHXdjRcec-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان: لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/31157" target="_blank">📅 21:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31156">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBA2udAPe0jT9ePrFnc660ldA297jieq3bclwwgQS4YcRbK3J_71hEC6g6eD6vadRinPsy2FRHSoCSpLIQXRDpB-8BWUkzF6QpSvpUCgJfSWB8EGWAok5EyogdrhJDzyS4HbRZS87pMl-_58Nyf4ckQEm_8n_fTDwfarMB_qyZPK2Bi80Lsnq5x1zI7SWDIH2MPcnPYF7ehryJuDhEQ0zNC8Bytv_6Kk0xX15gs_OfAgIqTDJawTUPiCazG5UPWVB3D23wywT42OiE1VT8wSH0e9xKPT8pnbkfGLZdji3OkIO_ySRLk4NoQfx7cNOjkdOLxMGGVU_7rSqwTRBRTMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31156" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31155">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_XwlOyMb-IMgWFue_TSF8LkGZin_iCcSKLszJ1Wzp4Gu92zrrKwCbGhh9S5VhQaUNKVyFPRcWjCKAM9eavR52FLCxyI-B2T64hWgLOreyWctc0kx1MSO0DnOPZQNxKKMScpd7H4_JKVP5HBmRjD2NWP6I2Y4BbcTuMuoeREqdwByHYHEl9WQl4ZPkSKsREDOtWGGKWOmnsSjHy2IbxfcpGUiUE7uZelJeUyuFavmvyCtN_QKXQq8vr6nouUeU1EjblM6a5Z6JDfB5nrwxGwOxTg9jAwxTgRYT5_W-gD6NUXtBov6O58uao_5PRKCemO9jYxakN83gP6Bx13ivpyig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان:
لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/31155" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31154">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
هوادار تیم‌ملی جمهوری دومینیکن در پایان بازی دیشب‌این‌تیم از ماریانو دیاز خواست‌که بوسش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31154" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4uG9fAC-QsgVAOU4SDP8Z89X9FwsF_hsmbkBz7LHii3s9L0V9CxZE1_XKtMzg72QOWnMx202DmidktbnFtnWAd9Zf8Izan5dRBo6cK4KQfc-uxpSUtFJVRIBkLKuN47D6CcfU4zqFQ-IsQQYVAMr_Ld7IfOIi65CMU9WleFPR6v2DcFSXikwRmFGgiNsOC2edQ9aJZVSu-cxozvtJ8-7RPK4jrSRUq7s0H3ifZecNFKEfcsUTHReMXEZNxwMUD-Re8QYx_m6A0INvqgCa8aOa03Jhx-OgisY8B_dDNevpnfC9BYMSY2_GgFux-82HNrdASdbWlrb__LKMThZxC3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=bc-3YBajyNZZWpiaBHyyZbE7fkaRbaR9iT2KlVao9xTq-nloKMVxVCUoT_Mg9c7R7VCsLPtZN5EbretRiOS0hFBPslDgXZ6_mXsf5p5f-O3A39VGXujRV1bBnzPVLKuldHb2350z1E_DtdXTPpNoH1Ys62g3ctWnndto3o8lwVXpgEhnmzqMfl0jIHWXqCZXv1-TGB1b6IqMDrSr5ZqwGnfhqOfRztZqpxS5nhvx7lf-3Xab8HCM0uMKMaiE0s_HyxJSETjxDoCtuHEboM_MvX7umOrIXwHTnVcuFc0qG4IBlJitPeMRKRjUNlpYTkPQEEA-f08VdANC_M_I1Ho9MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=bc-3YBajyNZZWpiaBHyyZbE7fkaRbaR9iT2KlVao9xTq-nloKMVxVCUoT_Mg9c7R7VCsLPtZN5EbretRiOS0hFBPslDgXZ6_mXsf5p5f-O3A39VGXujRV1bBnzPVLKuldHb2350z1E_DtdXTPpNoH1Ys62g3ctWnndto3o8lwVXpgEhnmzqMfl0jIHWXqCZXv1-TGB1b6IqMDrSr5ZqwGnfhqOfRztZqpxS5nhvx7lf-3Xab8HCM0uMKMaiE0s_HyxJSETjxDoCtuHEboM_MvX7umOrIXwHTnVcuFc0qG4IBlJitPeMRKRjUNlpYTkPQEEA-f08VdANC_M_I1Ho9MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qt2VPw1eMQ_3PNEiqfbSPtwEzzNpNPyFrWKIdOK-xQWtK_n1YtT3BZP4bs_AwgLeaNngXkmUh7aOCUrjEI_CZ6EUwDGMyAY0I1Rbcao17tng3TG0sNHHrF5d_4hf9fuArOvctO61RglAOzEa54uNj2JlK17mf55XHP4KBLoD-2c5a1iUJjvBhZu-1KaYanI9Cx6joroTgJzpcusy6w-B2cJxQzSwhGndR49Y45shHhMQ95_nqUq-PC_zz_rZfc17B2PFOy30RSaIb6f4UIN_UXtHvpT0TNtSDrbu9jLDGG3C42tpyMhhHc6Uh7kbQb-rVMqL2wJa3b1-PdPjGeKCBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
