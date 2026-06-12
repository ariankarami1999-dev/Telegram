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
<img src="https://cdn5.telesco.pe/file/Cma3ZbAAk513kQ8tQvaGzZrD5R_o1snNfZmEamQr3sXUGZ2vLuDMoE8xUp7II6gDfjdlvOp5k5nJkKImFx_vOR8OcEsxKYL1Pe4x123V3KKawuueCwfwLBJ3yicHXLqQLpn7Yv5mZvxL4coOTxBnzX1SBzNVMmKujf7Wcoud4Iqwbbo_Dh0p7CaJUnrMhBMrAuL1_4aAKUVvTExF_YEgjhcbN_n_GAj73bM751lMxTifE6mf0lITj9BjM2gjzpQ8aURY3SS-WY46UNRACeM8OqK9Fgoeqr1HgpI1XPBFji3mZnn1EzcPM0qIhMw6MjXpqDR3SCndDVbsFHSWhOZ2Aw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 451K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-22 22:28:47</div>
<hr>

<div class="tg-post" id="msg-92395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAFo-gXBgfQk0dQPdC6R_i9FBdx3R1VNzuPGCOPourtOk8iWJi2rSbI_znbDB5M4MI-8_o1MrDv8Zf7-kMdD9UDA_QMzbv3bH-DbECaVgTvh8ybPRXpB9-ZTejduHbVeN-XdRpZHxikOcnc-ch2UdtWK5JpvAld2R16iHkYDII1M_qL3qdqzAb9m16tVFSu60s4PDIesaagVuT55sP2YkSjCANv1ojYgya4yB2fhDxbi6CE4tn1Biv9a_lYdFm7DIpxBVVYZKDNZgqmVdiK7QapsE8gIm2yM9SEJAYDAI25iNCMyfCI2UsDLAWF8x9ea1wBwlYVFAPFWuQz0tq-p9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فورییی خبرگزاری نزدیک به آرسنال:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به بارکولا علاقه دارد و میخواهد جذبش کند!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/92395" target="_blank">📅 22:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=H5E6tywjqT18jaQf00fGsDNM3P-4m3mSjn9URUfWZa8BxwDviqKQ0M1j1kXCss5aaWKtewb0yrv2vAxFs7P71_-K-ow2BKDGRKA6i922MOu_M-FxaJmo0mCkI5TovaGiww82H3CnNzbTRXGHKEYx6gjFkkEryVt4bXMnEQSXw6fNzEP_CC3pwoHg3WesJT1iPl7GPek2Owl-iinc5fLGEx3Ahbxfq9MDRSaJN0_lMJv7Il0NlRjnQ-KjR0nkxBfWfsQb8cDkMz2f12fyAVGY4hbPFgCkITi3MogwrAqVR_UCiDgm90qNtn2PVxCpK90RrOihClTro_EtqAMjmOlT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318d7b2c2.mp4?token=H5E6tywjqT18jaQf00fGsDNM3P-4m3mSjn9URUfWZa8BxwDviqKQ0M1j1kXCss5aaWKtewb0yrv2vAxFs7P71_-K-ow2BKDGRKA6i922MOu_M-FxaJmo0mCkI5TovaGiww82H3CnNzbTRXGHKEYx6gjFkkEryVt4bXMnEQSXw6fNzEP_CC3pwoHg3WesJT1iPl7GPek2Owl-iinc5fLGEx3Ahbxfq9MDRSaJN0_lMJv7Il0NlRjnQ-KjR0nkxBfWfsQb8cDkMz2f12fyAVGY4hbPFgCkITi3MogwrAqVR_UCiDgm90qNtn2PVxCpK90RrOihClTro_EtqAMjmOlT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
افشاگری جنجالی عادل فردوسی‌پور:
فدراسیون بعد از اتفاقاتی که افتاد تصمیم گرفت سردار آزمون رو به جام‌جهانی ببره اما فهمیدند که گاف دادند و اسم او را در لیست ۵۵ نفره نداده‌اند
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/92394" target="_blank">📅 22:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92393">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=bq9DRd8hxrmCozQ2YNbRHt540dvqqlSmrzXKRIe91vNrG5MdYIDgfXo6dVeYtwoQw7awYkX8WDGVHIMtxnXDNlyBoSLr2OOspD0pJ0CEYUg0PZ2Z93KM6eq0gi9zCUCx3CqAXbc4Kd89C-ptu6RRXFL4V2_3kJt8gFOFerU8i9CjUWgsA3qW8r9HaPJsGoSLRa5KXbv6tzD0Lg_CQLHn5meRf7gmvYFww6e_6bd3HmSGdyj9WqwoYQl1So4Bw0ZSmbdSdPordXgixSnqXJgmpyhhzwwqN3RhP1JBREfaw89nPhdQFwAmtk7CK5AnjPFpHHCnIBYVI965Rm6TMfTtpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6825a80c.mp4?token=bq9DRd8hxrmCozQ2YNbRHt540dvqqlSmrzXKRIe91vNrG5MdYIDgfXo6dVeYtwoQw7awYkX8WDGVHIMtxnXDNlyBoSLr2OOspD0pJ0CEYUg0PZ2Z93KM6eq0gi9zCUCx3CqAXbc4Kd89C-ptu6RRXFL4V2_3kJt8gFOFerU8i9CjUWgsA3qW8r9HaPJsGoSLRa5KXbv6tzD0Lg_CQLHn5meRf7gmvYFww6e_6bd3HmSGdyj9WqwoYQl1So4Bw0ZSmbdSdPordXgixSnqXJgmpyhhzwwqN3RhP1JBREfaw89nPhdQFwAmtk7CK5AnjPFpHHCnIBYVI965Rm6TMfTtpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روش جدید لب گیری در سریال های خانگی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92393" target="_blank">📅 21:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92390">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stXHlOYRrn1FVgYoXBplEioQGFavSljKp0FC26Zvm_5b5-fVr4_MRn7vthxGJKX92k-0WqXuUWmn6Gu-WnbbbbSnbGIsebwYYhDKISol1ZNmMG4mUAMfGTy4GWqvSrAncuc-4vopR1Cl9f7Hm7PlxIcptIa65vWPB84hFEJFAbTMca664aSdQtoL5V0Yd_G_eNVljVUZS-uRMjMs4sHqk0lJ4gU03THPwqSUdbWCvMVba9hBVq1GI38i8ScgEJsWLNzOGe4AWl3feP5sANHDCxJkAmAAIfkpbKPoGHRKrQt6lIxck_GT2co45ZLLtDog0AH1G4Gz_YzN3vvSqlXDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ljA32dl31ptuXl4uif3XkXZo4mfVasZVu0BC_gEm659Kzk0pOzHW4mC3VDjoYE90k2IHjbrrMObTER27ovRME6c-EaKLWygY3wHMFGMNN08GHULp6Aicard9uzf-Ugb4-LTQWueb9I_sPc4hua2F97wSG6DP3_ojUqUlhDyogtxM9-cVfT9acdbKuTHzwDESHnieQJNs50DfkORIXSOc_jeKa9Ya2mW-6vCNvQD_lD0HHEtgFlbZVBiUGfu9afvcEBwRonnKcWIfGb7h0_NqnJiT0hRDzAuT9MXLADIDuPTaedl8tK_Lgu6mRrz1MLZOq1WfgZMrGaw7uH4JZ0C4xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KrTECSa6uZUAijXe2HANFSOeW77_bibVTsfQU7fDFDQvpU05uo4gYF5qyaGxJu3Zo8KhXn99amqdaAHnUsTndN0HB5mwbgQjwfecUyHHM-MOHIA0AM4BL1LN_M-lPj7xVhJNPhZHOxIU8fOKdj5ayN2IhQqt6lwlh4Caxs4t338g-epiR7tr80mzfqJ9wVSc42ZCdHhZASOThzse9J1G6RenrLHwsNRRQcMKH-YGuQ4vZ38LFH_T2lnkvtC5vjPCF_-fntjWMSoC2mhu84DHHYeL1ku2K6sq1rJffLHGc9W9VonZ58HBc4SP_SOojtuNx3U-Hd0vPYT2FJ5Aetod5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
فتو‌شوت‌های لئو مسی با کیت آرژانتین برای آخرین جام‌جهانی کریرش؛ البته که قطعا به جذابیت ژنرال قلعه‌نویی نمیرسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92390" target="_blank">📅 21:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92389">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b3801082.mp4?token=jz3RITrqN9422Pc-D_qjPGocTTaDPzFEOjrUwcLGKYf5k2grPyHxWoAuSplkbMXj85uMHq47GnfX92msbk2YB3T9i8TnAzr4e5h3CjNEzDheLKIEwY_mmI7b74HI6y9pOWjK8WpO4GgV_ct4OrNxUMpeM2sE7qjkmPSfkyvQgxMLV3c0vgjH_53vFMfyOfMQukggc3VydsLjqOBCpVZKPOS0XrYQ1oMax7daO4qAbQHZLu4pp5x9OW_bY5oAfC2RiUoOyslo1MX-a9MyObbxFGjC8dgB-DQR4CKOeXfExS83u9kcifQvLfVNXQEfQDf32FzIg4tCZTlhc9OuP3_dng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b3801082.mp4?token=jz3RITrqN9422Pc-D_qjPGocTTaDPzFEOjrUwcLGKYf5k2grPyHxWoAuSplkbMXj85uMHq47GnfX92msbk2YB3T9i8TnAzr4e5h3CjNEzDheLKIEwY_mmI7b74HI6y9pOWjK8WpO4GgV_ct4OrNxUMpeM2sE7qjkmPSfkyvQgxMLV3c0vgjH_53vFMfyOfMQukggc3VydsLjqOBCpVZKPOS0XrYQ1oMax7daO4qAbQHZLu4pp5x9OW_bY5oAfC2RiUoOyslo1MX-a9MyObbxFGjC8dgB-DQR4CKOeXfExS83u9kcifQvLfVNXQEfQDf32FzIg4tCZTlhc9OuP3_dng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گوشه‌ای از مراسم افتتاحیه جام جهانی تو کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92389" target="_blank">📅 21:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92387">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqNGr-DCuxv4CTDcmIktEUI4HNwd16bIBWd2W-niL8WtOyoVIYM9-3ZW9b1ZuZD0aqYetwaNnWfXvvsbuH-blKrfmMFgD8x2eacTMDj506Wq9_yJWB_1n6r7mLltCRBbAAB0x9VqA0mOQ78zsTjvf1ZURyyIhXjxzA45ielaC4-MWfQaYB9y4KUQrBbcyZ8-xX4tlx9225Kvugbq6A1q-_h7xeJY4WnAIOkBUvWlQp9maY80giRY7zKITmQALT9mQZziIyS73REP8QlrTSGeSYxRKF0oZpGNR8waKO1mDx6oRmmFETqpiCzw-kpkl_B4LhVI2-xEIY8Ir_9BVBCErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qusQOTYDh5gVGp3Oer-dHPIpSU0BVbu1Cob-uqlkv3O5FUEf8j_uNZKl47X7STAhtjaBxDnQlYBDn-CCOg8ZA5s5tWvAK-ScwBB5vflur4GZ7u82EbOvjfcNgWZY_DZVBBb7xrUt2Ou3FPsjxTo5_rgcsi-uufn1uZ7wWjyyfYLpWTgYQ6dU8PCK6qtfIpEycDQnTnH2Q2CwDbaGrwiIEQQWx58SoU47jwYbt3DHeDfG1IM7xgB7MP4OAh0Qt5zaitV34y34XfLs2ZsXO5wLl6cN_H37m7MCAApKqDGYEGVT3I3SvTZ1D7qNEglagXBsHKKYbYNoP6Qs7xdcBiS78g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر شاهکاری (رامین رضاییان) یه کپی بی ارزش هم داره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92387" target="_blank">📅 21:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92386">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffaacc1d36.mp4?token=vU88kCLcnZ9QJ0vVOjD3WBfnGRUPAGJ4iUqDNUIUAAvEUx4aK4W6yiQ22tI3Cix3-4Ah_iBeiM7rsDqb5N02mlkh0O5HGA1h-Bs6TJ0aa0XlBzFNMwowDy2MaVV-zbc5NhvME17ui0-4nj8w2_rbVsB2C0mHf8q0n1X9QCB-vlUtBtVn3srugIUes8ocYklE5RkqM62QQC_O61Ig4-ORkRiN_0e9auKlQu3q9k-o0TGw7et44Y8eYsme13QK6azSpNl4LcjXbpm9Zv0mVP3bkJnXsqKRiZkpzenjo7G8P2rs55BMwEShq0t0lJzEPEZ5Lyum4iCRQuUCBDcOi_90tQ60OvSaui56SQKClHzFZUwImvRDOaQqHQSh2As44R1fGGuva0iVFwUyd5EcqEUBHfriRWI1BFE7wANHA0yZzNSJf0J3XYJX1wORNEqNLuu8TSgpDOOD6v-DIomXU_yyZYfE2ZYRzf_yrJ1GsyQgx_0aAuHluPIhjEyNv66up4CS--hwLL3HkICYz_r7lKCXcoQgngkq_AZXaYkmCPogyHO3fM1vRt74Lu5_DHGYhPbI_32yAh7sONdtWfcLvSgLxFWcsIJDksC-XLmaT8UyMxqNS3WJcPpl66uRcGH0WNshGaTd5OYZnXTb3H4d_-iE1r72QjX0uhcEM4ru5zWqQGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffaacc1d36.mp4?token=vU88kCLcnZ9QJ0vVOjD3WBfnGRUPAGJ4iUqDNUIUAAvEUx4aK4W6yiQ22tI3Cix3-4Ah_iBeiM7rsDqb5N02mlkh0O5HGA1h-Bs6TJ0aa0XlBzFNMwowDy2MaVV-zbc5NhvME17ui0-4nj8w2_rbVsB2C0mHf8q0n1X9QCB-vlUtBtVn3srugIUes8ocYklE5RkqM62QQC_O61Ig4-ORkRiN_0e9auKlQu3q9k-o0TGw7et44Y8eYsme13QK6azSpNl4LcjXbpm9Zv0mVP3bkJnXsqKRiZkpzenjo7G8P2rs55BMwEShq0t0lJzEPEZ5Lyum4iCRQuUCBDcOi_90tQ60OvSaui56SQKClHzFZUwImvRDOaQqHQSh2As44R1fGGuva0iVFwUyd5EcqEUBHfriRWI1BFE7wANHA0yZzNSJf0J3XYJX1wORNEqNLuu8TSgpDOOD6v-DIomXU_yyZYfE2ZYRzf_yrJ1GsyQgx_0aAuHluPIhjEyNv66up4CS--hwLL3HkICYz_r7lKCXcoQgngkq_AZXaYkmCPogyHO3fM1vRt74Lu5_DHGYhPbI_32yAh7sONdtWfcLvSgLxFWcsIJDksC-XLmaT8UyMxqNS3WJcPpl66uRcGH0WNshGaTd5OYZnXTb3H4d_-iE1r72QjX0uhcEM4ru5zWqQGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بازی کاناداییا در مراسم افتتاحیه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92386" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNlZGgt42W8t_9KYjBbJL4VBR4v626N5jPKQWleb3FtevUYdf1Sa2hx0N6HdKZ-CgDGjo8exjts466874SJkBLvoTfxt1uAmeRAgdYYqgllcRFBMz03W6lQi8oHzoIVwEmm85xlcWp_fEGDE6X_7MhXzSbsd4tmsLmSdXPG96Dd74_VsthWQq7S-ZHR3oRWcwRLJdFhDuBSMtByAwG_E5BW5XOk--VnIagT2KmCGUFhR819fPff4VS0mJQFQoBUeQOQ4ysR5q1saCtJ5y2dd-SzUMfwCCS2y28-tAd_SHT5u47YTI8awTZO7AvL4ZzloFbqB9ynvOHHGBaN0ga_efQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdE-kzrJWn593yrTxNecBKU4P2PQkt3vTNklX-OV-inUFC0hbGsOHV-5tbmak4jOSwhHS2_fOk3FXuq54pvlN-WtOYXVaUtrGiObc_L-D072iWFWwLBkf9EC5wwSjCYzZ75V7SjSqZi27lKrsRLm8hGFAtnSqctoWfl2AXLzZd7P9n0uBNuuqiKV-doLJ_mZMJCF1c4yejXEAZ-CAEwT2pImQ5pRnfMaxjSNcEDAXLlyi4IMlQSa0vgtK9FO4tQf_ivPQny6NKw3mLd1SKYF87Hiqcg20T1lfgv2lEQW6Oe-pvAlWJ-pUjPcAeOiQoDmrKf8-1OgSgMGLLQ8b9vw6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇨🇦
🇧🇦
هفته‌ اول‌ مرحله‌ گروهی‌ جام‌ جهانی | ترکیب
کانادا و بوسنی؛ ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92384" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز هفتگی پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92383" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ym39Hqo9Ys2lNIyOrOH4N2dZV5BUxNiMfQMwp55_8HoJUUP_SoEw2jNKdXA_fwH1rN7Vnb-yetFb1fewYpmzs4iLgdLMxPJHsgTpx1CakIWSiVpuo133d1bVDE1bzsY-T5c-tvfJKYurTiPs03Ce_QsPPvd-jPSTLzWj2X3Mqb7ws2-porQuNnD6g8mJQIctMdVoiTGEJoeN63bZ-tx4fXHphJf6BYXf_WHhePpgVAWzClt7M8yG4L5YpXnTfs4u4MRMXScEmCjna0IUDDC6qTyg2OxKiMdsQAyCSyemRV7j_sJLr6iluKu4oGSrvhu366Pgem4-D-1291fylwfHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
رایگان پیشبینی کن؛ جایزه ببر
🍸
درسته! کاملاً رایگان می‌تونید برنده بشید؛ فقط با پیش‌بینی بازی‌های فوتبال، بصورت کاملاااااا رایگان میتونید برنده جوایز ما باشید
💸
جوایز
هفتگی
پیشبینی رایگان
🥇
نفر اول ۱۵ میلیون
🥈
نفر دوم ۱۰ میلیون
🥉
نفر سوم ۵ میلیون
🛫
نفر چهارم تا هشتم ۲ میلیون میلیون
📈
۵ نفر از اعضا به قید قرعه ۲ میلیون
🏆
فقط پیش‌بینی کن و برنده شو
👇
➡️
@PishWin_Bot
➡️
@PishWin_Bot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/92382" target="_blank">📅 21:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0q-2SMZJ_Bsdou2bcBuIjmlQSf8fhyeO6w_dv6I1hstEAEJmdMRNv5Mf04qFMUTr6CT5V2qjxgHYFQksih0A8OyRDa_mm3WKSheZfam7WZQdSqpCe-PSH4yMdj_40Dca_L7nPMnhqZ6Xns9S9mwIF0lqkgOw90XIjzuFMMFQl6ZBl_-nfN21uOpdfqD3hAgXXUe_TxQcuqO5T_C6OtXEpN-w3vTdx8fs4rpX1MSz3e4EfeTfsPwSEmCxFrchqnRcGwp70wy_6CsmhDUs7WVobah3bu8_8BtRXMKGD8q0U8or2DetJNvLF-U989kqKPXeIzEx2-RX4Iau0nC7VSYpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
فلورنتینو پرز می‌خواهد مودریچ پس از بازنشستگی، زمانی که تصمیم به پایان دادن به دوران حرفه‌ای خود می‌گیرد، نقشی در باشگاه داشته باشد.
این تصمیم در داخل باشگاه قبلاً گرفته شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/92381" target="_blank">📅 21:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5fvaJgIMFdwTxNdpOoLVnDnP8IAxhpIpQVGWOWhQ4UOd-obxZkU_jdTJSGeHjEqckyc8lHmeye1btkpy81Cv7uZcS41_N6JvztFAvGgOG1GOjsQRGMf6334SfzNgooJ5seRhXZE0nvozOvk0oRsEaJpws7zI-ooL_ruWGaLh81apA4VJ6JdocMSswOql4EDTexYvVVjLeS2pDWFNUv3aTDrFUQhnQhcLtrOQYWBpxkhSc8t-wi6EsRl6fFBx0mPy8spwVLcLVTL2SaSIK01No_nwO8Rbe_f1HAAuvPddVK6hVhru03i_0ER35meDhZydeJr2M-WLJsa-uq1eJozqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیانی اینفانتینو:
هر وقت جام جهانی 64 تیمی شد ایتالیا هم صعود میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92380" target="_blank">📅 20:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RX6dCrAsojB_zviDVXUk1StDDvfDnmQtbftmXPNcDB_RUr4c-HpsBe2s0vyjTQzYZWM0exsP3E4KEqi_OuO-k_WQ8a3dRWzPXWuQEugOZhx5xRMzb2tHkG73a8xaX4mXuFDO2lkdf14JClPJqm3o9EFen3sBE2gwTN9Z8b8y1Z7DIsaKGwf1mAk4NgyMh9-cStlmqq2nzXXBOhYfpya9gb7FTrmCB_wQzA1K_wn6rMOzZBUlA5NdyvydFOFhflwrHp1vxbTdTCh4o3Z39JQn0te5iWvzXV4JSswV2wcA4Roob3hWuheO8vhiYgqGhyY6uxun_tkGo_jg8q7ItTF5Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تلگراف:
منچستر یونایتد نگران احتمال اقدام رئال مادرید برای جذب ماتئوس فرناندز است، در حالی که مربی جدید، ژوزه مورینیو، به او علاقه‌مند است. با این حال، منچستر یونایتد در حال حاضر نزدیک‌ترین تیم به نهایی کردن این قرارداد است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92379" target="_blank">📅 20:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f444195b78.mp4?token=cRnnJsh5nPBquZimtMck9kzLYFxn5zJIPoA-apR2IXKARlb43ipTwyLmO7hX4viTZu0AgW3jTR7Hv6S3SPB6qHloOfAv-QIkn8VvMu8M1pJBsgdpWkmpuZPqi-6TT1Mgczk6TX5oAZmq5peqmTUBKcNfDNvsHFE5RWjNSbb3DDPAf6uF8Sf5k_ajaGSIpI_QJl1GU6306VmlGKDR-mgR7IztrVoIdtCZK98ywUQi2o5rBifnb1SjZHNi_1kKpNCEzL9NDDajPsC88zDfwELeJ3yqe795kkb7HDuZk9wZ-58JEnxxL09kKBC7arrCxsC8TR8skeXJzSEAubU0cPPvV0V_DjlrYhW46rQP3U0m2doHasiS8Qpa6Kq0Xr8yYQb5QmD294_cKWuUFmb8N12T7pQSxDbzjKIdWYdECv3sslukm310ZkpOtX5_dMgUswvV6pg06Yzk0_x1l4KM2Bh40akme-rWkpdiBzh2EBKT-FrKd2Taw40wM-_uNsep2_VsD_ZKHWd7z7joyPebajHfTevGJ4svkXgVZQAGhecHl2RU16RGjjS25zxUUZMs2NoxwXST9SYerBb8mSC4E8v6PKUkozuw3i5T47BXB_o5RPnbwWijt-ltIrZzDbOvBjjytJttb5ARK08HYr8ajXgK_S-bQvuY3FsqdK19y0r1SWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f444195b78.mp4?token=cRnnJsh5nPBquZimtMck9kzLYFxn5zJIPoA-apR2IXKARlb43ipTwyLmO7hX4viTZu0AgW3jTR7Hv6S3SPB6qHloOfAv-QIkn8VvMu8M1pJBsgdpWkmpuZPqi-6TT1Mgczk6TX5oAZmq5peqmTUBKcNfDNvsHFE5RWjNSbb3DDPAf6uF8Sf5k_ajaGSIpI_QJl1GU6306VmlGKDR-mgR7IztrVoIdtCZK98ywUQi2o5rBifnb1SjZHNi_1kKpNCEzL9NDDajPsC88zDfwELeJ3yqe795kkb7HDuZk9wZ-58JEnxxL09kKBC7arrCxsC8TR8skeXJzSEAubU0cPPvV0V_DjlrYhW46rQP3U0m2doHasiS8Qpa6Kq0Xr8yYQb5QmD294_cKWuUFmb8N12T7pQSxDbzjKIdWYdECv3sslukm310ZkpOtX5_dMgUswvV6pg06Yzk0_x1l4KM2Bh40akme-rWkpdiBzh2EBKT-FrKd2Taw40wM-_uNsep2_VsD_ZKHWd7z7joyPebajHfTevGJ4svkXgVZQAGhecHl2RU16RGjjS25zxUUZMs2NoxwXST9SYerBb8mSC4E8v6PKUkozuw3i5T47BXB_o5RPnbwWijt-ltIrZzDbOvBjjytJttb5ARK08HYr8ajXgK_S-bQvuY3FsqdK19y0r1SWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از خواهران منصوریان به کسی که واسه سوپرایز تولدش هم اومده بود رحم نکرد و کتکش زد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92377" target="_blank">📅 20:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJdPAiBN5eranipxVIyUEUpekEdV5EY4WWwq6j5L7VD6-HX6ee49gl7wtrFbkqJmxt_ZjtkmOeWn050LgxonmdU2XDPU3TYMUVjH8a9be7KstnFgEiBih6OqB7CMxM1uXWM4vFktJLC4J4XoTfgv6v2iZ7fUwc1pQ1iC0wv0SYMDZGFkDM0bl8hd3tv9VW9Zsr7xudQ2js-DPMn86_67RvJEAYq-YVFj5WW4W9D9_YCFWBNCs-51nCNuS4mezRSwFqbjWJgkY8am9vlOQilzzsFcIPu7nlABotc2TiQW8d9dmFUDaemZ3f3BaJvt6tgj67uo-yn9bVT2hOl-IoVgbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
از حضور هواداران سنگال جلوگیری شد و به آنها ویزای ورود به آمریکا داده نشد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92376" target="_blank">📅 20:41 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1HZ4ZJq14NOqrGzy_OpwhS-BHirhnt8EwEJUftYijAvTr96WS315TLB8OnqQUSaS4XiJWxI5ZkIEYhzZXa-y49rPuiAXjA5EsGipDdKulj7ha6qaWn2ciAiL4Ec4zUw7jNQN6I0WAelMWa-uylaXNZjHgQU3xw6OPqHFG64ljpHxUla8O8CHw0Zbh14ir08vLQy6KA1LiGA9hv-Yf8UKR7nnZPiEDjbZtqbdaMFJiuI7XNxHm-HB1miPKafAuObOOcClMp2oxOmQUfwErRG4v9t1O3cGFgwqAk903eJ8GopOM249Xidm9hKgR3lqQcoBAQE_6Dlitj8Zf5GjH30Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
بن جیکوبز:
اتلتیکو قراره مذاکراتش برای جذب کوکوریا از چلسی رو در چند روز آینده استارت بزنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92375" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92372">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jAar6psInMFU1lyX9H85cbMuySpNTy3-VwaJPQxLG-Thhqa7Z-AHHHWBsrDWypXvhBtK-g_sziiCBN6u2w2Ycik-dLsr-NqHS6QjfLU6HWCVH44wRHl6eyIdJHQ3ASPf5jSwpaa2auBSb0D3TgNMeHtIrE948y53imD48qXFB_c6IwgJIBvfiVV2P80tl1zLP910ZBdDutLdoDxt_CI1Bta9Pg5P_jzZG-APthHr0h8FS4zT-CXnU71_rcMdxbvpgQ6P1aA_j8y9JvwHCD8UJeHUg7ll0jdAhzEXifIvO3JOBU58AOS0EJGb0RsXUMFQKUatydZ5AW_6sEIjFekvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iJyuH0iu4Y_AtuS1LV-3jE21sJ15cPEwx3f1dDfr4dr_FJwbrO2k1Xdd_j0VhpSrCJAyILxASTHM-gTJhyWD3bELTeJcPc-9ONlpJ5CaPZLBW2E6GlmEA550HjEbMV3EKYcnu4QmfPxiOqYZv0eCsFCIRZj_KVXkTzbPYiVW3XcEmTaZtiQSbz0xMU9075nzI31usEf2BFnv7-G8w5f0B9OZirqEKchryRSXiueGzGmZBO2fPmp4dVCkou-H1AuwF31rfgV48sImWwJ_SlyEJ5Fy6s_49YV4ixaIwu-H7KBsPx-SJnogNMc7xh_ClkfY3g5DqaNor8p308VJKD9XZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYfsH-lt82RQeWTDv9co74GvnupXw1PwRjF25PPTTEteUdWXH3EHy-av90T-ofccN9kIfyPn3104wb_mqxrYndB7DanjQ6hv2zu1-7MTzIMTV48sak9F18gh-R52gEBCH51R0JiUvafryVFI2DYWzW1nW8qysMV8YhmDdB9ClgwJvXfTHw1bxVNcsJcSF92OXbXKklu1ZAs5AHJj0cK-hc5b-oc1CizxFkvFxHi5HzcDbuD2_O4nnwKlKk3U2RhQ_Vh083y7-6CqTNBimPFQsjoXn_bynwce0NCYZ9_b0TnncIns36QwTG1e0aYcodttg2dtrMn6QAhCqG2eq-c8iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکنید آقا
😂
😂
😂
(بازیگرای سریال دبویز هستند)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92372" target="_blank">📅 20:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92371">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P523nYxNTVgS1rvRy7NSVbGFGixoo2BzmuN1JyoPr_uBuw8zkLNHdDZws4QlaBQagsOJpIS7qhJxMs_CbPW332O5MnFM4YAcdzAnn8uLCQZS9HdwTp8qqgFcKUu8qXKEwkla-6M3fZvHlK0Ve8_eWbfaj02RR5hYiVKYRyCLq3DfnzxoKpT2aOjRQBfIfdEkFtDliNBJ3jD17GsYfz4vOqVkXfVh0bo-Sz3AX-it23ukEWw99jlr4HY1lfiFQaD6XNMFBp0KzYadg5ukC8GFTVeAHcI1NPecPKrIAkgKNTdHzVYem3CbvE8uObU_kJ-s4z0hjF8g4Cf9zpVqwE5Ffg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توماس پارتی به دلیل اتهامات تجاوز جنسی از ورود به کانادا منع شد.
او بازی افتتاحیه تیمش مقابل پاناما در تورنتو را از دست خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92371" target="_blank">📅 20:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92367">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l09KV92UfzRvHppUIPP4jSLk-AxS9g-vjXIRf7scdKYOrtK93uljAY4NYLB9lTu0jafA6emI6Lgo9oNCLCSMZNE-N8iV7ui827LfKEyetcBaqQMULGW-PjOPwxV8gD5Kc9GUS5ZbXBvYX-GpAOtOp2_o707Et6H43lFd5s_hjNMLWcQ3wUB7FYSt1A2JblNcdp5fzviGw_nZqd-Da7SP7SFayQmpyKw2HhqCExXcjsjywdnIXC1cOCvEYp61LS9gxMb5bESn8qZnfKGrepgem16b9g15zYSQuvYpjjsWtQTF01c-kiiMAWWZ2HQHxJcp1zHwK8cpqWNXZV4mv-LBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇦
🇧🇦
وضعیت ورزشگاه محل برگزاری دیدار کانادا و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/92367" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92366">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGlCaWcnKomknogDZomMMqcWO5aPI10Sh8KgZmGrlPMNZjblYphDGCAUTl5z1xL12II5z72hDRcoN_PKOeJLzdUoK-daskK1QNcuHT6Eb2oDt1QoEG5kzv_JgyYMW9-dg7tJivn4WO_PRpgXgf9f0yexW9S10TePZQ6Vr_Y-t2uR6frBHGMHh0YDdI4VIQ2t1HpuWCxOKdFocCvD0Sm48XTyPJ4hY2n_fcbp9Qp0lscv65YltBYLXjHiR3xSw-dEbxR7aGUGMoZdbtOqTgFhby2jrm_yUtO-3TFTq16In_QyBOfKnnZgHx8XdMYQBnyunyyHTaiHZz-h6pxzrcd95Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
خولیان کوئینونس:
برای من گل زدن توی لیگ عربستان سخت از گل زدن توی جام جهانیه.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92366" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92365">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92365" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/92365" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92364">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_lBWoHkjfV7-3TIoEYGbF75Dcl06LEQxlTqFXZhFtBo6gWoHUwiIzXXKjFwTXyZUotAxK6dz5-Gpsgr7pQsOlCVD72xBUquLPJnIs6EDrs-XDmM5nBrsS2E85tRoEck4uzA1AjPSBWOTDUecD_nLhmk6N0rCx0d7Fn8F2iniNoHtrAzdk855rti2y8uCLmnYh4jThzuGMt40tZbmk7PMWPYljPUd1Dg4WOaNR-goKEcneWxbKbRDP2HgqjC3vNo3QOTqsxGPsScg1Z_wLbZP9mL3BjLwXklinVW5wGPsQYPrrYgXZ_HC4QyvSj-3VgkqbDCecn1sWxyrpiFGUAQDw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/92364" target="_blank">📅 20:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92363">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhCNc7_LAvOKBl3_QqOhY3nZr_GMvfOGOOEpRJmEzGrXE_RX4nPIwVTqHWHkM_L8-flD1pTiWvpz6TMTjYwSRmiQHbcqByt-93jploubmKeo8OVV4bFvqlH7x7PhN8yL2MzA4cAugP39RckdIsDmbPHAEafH5egG3oHlnGLA6MaF1zmDjXKQklQKZ8GljtFDddRlG3AFqrPZBvL7XhYmTQhaKZs35b32Xp-xiyD_ptJm6tWC5Ac5Ti2l-lGJJ-hOYNrd9fSyh_n3Q0bYQahbNkcu2SOv-C6sK26PIA9zfuN9htTGecUYxUs5vGiVgN-ydNgfwLQlr7QC6qhytOtRig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سیرو لوپز (خبرنگار نزدیک به باشگاه رئال مادرید
:
🔹
یوونتوس ادواردو کاماوینگا را در اولویت‌های نقل و انتقالات تابستانی خود قرار داده است.
🔹
اسپالتی شدیدا به کاماوینگا علاقه‌مند است و برای پروژه‌اش حساب ویژه ای روی کاماوینگا باز کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/92363" target="_blank">📅 20:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92362">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPQjrq4yO4P9WcijHPlwTGYCAzHAQHcej4AAU-F6iK7YBedVtgioIewprS75v-NOZ38coZH8YqafUKzttz2WbhSd27JW1TO3RuLLL1Vy30yswJlt1lzChgLyVcgY67UR5KGjNqZOyldFtq5fxUQgKZAfXH0s5-os_q4QHQ5AjgD2bGHOTdGf37WmCy-lINsT6-P4RYC1dRyD3AJ2NH79LdDFaMI49vYpVKA37NcEuH_Ys2n7R2iflJ3JZNE92oDpqHyzvl3jUtE6Mw7UL9Ak1Hb-REVxWBxv60JBJZLSVwzecL5C1R74HSnC05Rc25UsSirGKsGKcL_lkvjhJ-oubQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
عکس رسمی تیم‌ملی کرواسی برای جام‌جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/92362" target="_blank">📅 20:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92361">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇨🇦
هوادارای کانادا کمتر از 3 ساعت مونده به بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92361" target="_blank">📅 20:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92360">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-jdPk0ux-azu7-mDKSqRAlr94e-7eT7qCQ_R2yHpe530ra73cedCLcCUvWcYqJGUVpt-1i8gy3EO7MsYSvtiGZyw9HszUZkuWJgmYMy-WSSSVjbX8UlNuGsuGCNa7KMaql-C76s2ch9IulSBxLpNT6GVWw8b67dqyi-mWHpzYC91i67lEqnilkWI1r9S0gf2IxYD8mU-o9ixSbZL9SooLWuOrLCWNz466YwRpPgBlYq30ZXQpNerOBYF70E2zrnv_xJlzORjsnm0ZsrSX3GFplspOEiq9sTes52hjgEpsjbOF7q4-I1fhcfPLBbtMt9gCUJIq9-aQCjRvf33n_MXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
رودری: اگر ازم بخوان توپ‌طلایی که گرفتم رو‌ تقدیم کنم و در ازاش جام‌جهانی قهرمان بشم، قطعا اینکار انجام میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92360" target="_blank">📅 20:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92359">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28c3684885.mp4?token=VsPTB_15PMDPHymFvz94S_pQpONB328ZbYHo2egSMmGC6sbco5tqGgENSqatKNeo6BKF_ZElcOp5f9kaIhKTOHSO2GAdC5vfRVnINcRWrfkEVJy0ElhhbXcc3gNizxUzPHpU6cj_K1MT_Zd_H_anQKvfVCSTw6UfQWejrasmBaIceygt95c46YS-RHnfAi2HRki3uyi143KSqhkWt43JH78uZUw2PmhWbUGas2XrpzKXy4JlafvpndjVa-xo7Fs83GAfc6_UlBm2lrHw7q-Ozb040Lv7MTIYQrYgy6LoIu1TUY-j5_bkXB-olCqvvU9Wzb8qnGC0mNOOylQdgK4R5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28c3684885.mp4?token=VsPTB_15PMDPHymFvz94S_pQpONB328ZbYHo2egSMmGC6sbco5tqGgENSqatKNeo6BKF_ZElcOp5f9kaIhKTOHSO2GAdC5vfRVnINcRWrfkEVJy0ElhhbXcc3gNizxUzPHpU6cj_K1MT_Zd_H_anQKvfVCSTw6UfQWejrasmBaIceygt95c46YS-RHnfAi2HRki3uyi143KSqhkWt43JH78uZUw2PmhWbUGas2XrpzKXy4JlafvpndjVa-xo7Fs83GAfc6_UlBm2lrHw7q-Ozb040Lv7MTIYQrYgy6LoIu1TUY-j5_bkXB-olCqvvU9Wzb8qnGC0mNOOylQdgK4R5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
پلیس در حال بازرسی بدنی هواداران حاضر در جام جهانی:
آخرش فقط
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/92359" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92358">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ لیست اولیه بازیکنان مدنظر اعضای‌کمیته‌فنی تیم استقلال که به علی تاجرنیا سپرده‌شده‌که بلافاصله بعد از باز شدن پنجره‌آبی‌ها درهفته آینده برای‌جذبشون اقدام کنند.
🔵
پست گلر: محمد خلیفه یا علیرضا بیرانوند.
🔵
پست دفاع وسط: مجید حسینی یا…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92358" target="_blank">📅 19:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92357">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf073331.mp4?token=vcBWUB176BFZ-B0Y5kW9-3x9mhZ5H31KPZ1TlzyT889dKFH8MiVCaQPIlxiBnnx9uPN8KLkYh-RVIjq3lKcC5Pk7hx3xhqJmhEsRGcUUPU7Z5bDdHZ8bbJPnaes4d4NQvvdaezLrwYJs6Gwmq6H0vB0jX7mucwluAiN7uedLy0h3fprrMwPlOxKP9cfnm-2EZLfNJEuqVAyMfbLFkM5MvNeUMeCl1fXqaPUrMfHfXl3sTsujsnvCnc5380DErlNecZ3WYM1lTus8ygECeyw1AgNBL66qqouqcM_x0qKMiHnT949N_EhvwhhKYv_ltaoZo3DVU4GMkSoO-wm6K7g02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf073331.mp4?token=vcBWUB176BFZ-B0Y5kW9-3x9mhZ5H31KPZ1TlzyT889dKFH8MiVCaQPIlxiBnnx9uPN8KLkYh-RVIjq3lKcC5Pk7hx3xhqJmhEsRGcUUPU7Z5bDdHZ8bbJPnaes4d4NQvvdaezLrwYJs6Gwmq6H0vB0jX7mucwluAiN7uedLy0h3fprrMwPlOxKP9cfnm-2EZLfNJEuqVAyMfbLFkM5MvNeUMeCl1fXqaPUrMfHfXl3sTsujsnvCnc5380DErlNecZ3WYM1lTus8ygECeyw1AgNBL66qqouqcM_x0qKMiHnT949N_EhvwhhKYv_ltaoZo3DVU4GMkSoO-wm6K7g02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
احساساتی‌شدن عوامل‌برگزاری افتتاحیه جام‌جهانی حین برگزاری مراسم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/92357" target="_blank">📅 19:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92356">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMrNnbKZMI9u99jT_S9euT6hv7o6ix_xr1HKE7ZsLgsTtufPaMArI5ZjdoUxbwtYY35DgWtf7vB7m9M070Q3dBq3bpUAtm35NgVZIBpKO5rV0pLvy5mnBNmXF3ezH4A9HRehyCbPD34XKNRyfwnOg5S6lN1yzxp8dF8ZulnLARiO2LR2Su4e48ylvT5BYycxNC41iMXZHINAZOoVPgrqKWXp9kWq448TKFBucavMorHttiHRVh0UyW-e8WshFhRemC1T2VgmIbuQkDoUFjtBG_SGqko9HaAA-huzRhN3aTi_BbMgWgxQ5E2a-bd2UB9rRxb5wrTesm785Kb5NZKeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رسانه‌های خارجی از تصویر قلعه‌نویی که منتشر شده شاکی هستن. این رسانه‌ها نوشتن که سرمربی تیم‌ملی جمهوری اسلامی برای نشون دادن دارایی‌های گرون قیمت خودش که همون ساعت رولکس رو دستش هست، تصویر رسمی جام‌جهانی رو خراب و زشت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/92356" target="_blank">📅 19:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92354">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwagenvWi0h-iAHOdQygs5egoalmkc1DoDVrWk5xiXAjYVRFwp2uIZEQ9thgYVRYJjRhsBb5ItwgYnO6zHweRz4Tt1PETsHe5So8FFBz_NziQ59AAGV7OTzyABnz6PWpWAzyhzEgkdJJQZABkzKuT1wLE7v41SlFC5q05ZZcZvDzX8-hcffkr8VihQTfgbFTOP8ldo4rQY6GsGaMzvP43MQI8t5lXGSdjTBZweXk9X-4jIr-dQMZKcDwqy7K_kiUUYZAItxv_lc0Pdcg-BCmsAf4dMeAcjRxHD9xfVPCmj-dsHchxaaVjNBsFAg-cxtd7ovzS2STc4jt47wJq_y8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فووووووری
🔴
🏆
هکرهای مرتبط با جمهوری اسلامی، مسابقات جام جهانی ۲۰۲۶ را تهدید کردند.
🔴
🇺🇸
گروه حنظله ادعا کرد که پهپادهای متعلق به دفتر تحقیقات فدرال آمریکا (FBI) را هک کرده و تهدید به هدف قرار دادن رویدادهای جام جهانی ۲۰۲۶ کرده است.
🔴
❗️
این گروه تصاویری و ویدئوهایی منتشر کرد که ادعا می‌کرد از پهپادهای هک شده است، اما نهادهای تخصصی در صحت این ادعاها تردید کردند.
❌
🇺🇸
در مقابل، مقامات آمریکایی پرواز پهپادها را بر فراز استادیوم‌های جام جهانی و مناطق اطراف آن ممنوع کردند و همچنین جایزه‌ای تا ۱۰ میلیون دلار برای اطلاعاتی که به شناسایی اعضای این گروه کمک کند، تعیین کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92354" target="_blank">📅 19:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92353">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#فوووووری: باشگاه بارسلونا قصد داره به اتهام افترا از فلورنتینو پرز شکایت کنه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/92353" target="_blank">📅 19:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92351">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxaQN5J-wFNqtB08Tt99mmVEFrIoaffZJSVHQEmAPHXs0NdBj9MntEuwYXGzn68j9gPXLUmWPS5LOx4it85CjLYjKDPg7_rM9MjBRC7OIiGSQ0oGey9MutvTjZemUcGRnk6D8Z_7u5n6j6FltQgi7AHP8-O7IpBhyhfFdFdb96RV6K_LpVF-6002WtHTmlHWP16CHKHjXSFA7BC2lvpmiC00Yof5uLnD-vwLqoZVHngtX4OMjz5ogRDsg9yGWgen7MxA6WqzNMvkr_CvcojVGDrXUkmPt2zhAlZ-cXtEe3k5H1ZVcIULs-nOI0TdsDzAE9RFSzN06BVOsodeYrd1mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
#
فوووووری
: باشگاه بارسلونا قصد داره به اتهام افترا از فلورنتینو پرز شکایت کنه
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92351" target="_blank">📅 19:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92350">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY0g4p_E4wIRZolI7UlgLVIGMBxhirAR1Efb_TStUqjBYdB_IPiYJAgSNKZxHvjo_g5Qvz4XXT36EK7EBQy-e5f9Z7qqsUL4F6is_iq67Ya4FEY0uB4sCDExHUohub7P_dpCQ2oAcPNdB0HyiB04GFllemL3LSozEVfKWE1YXnjteeg_xllOFz6SoXmS1RP4sZkBhrvOP5nbEQOOO3qO-MAUNjlADwvvvOeXHL2Md5BHm5avAKR8udSon5tbGY1PKu0Oxu9iQbTEST-kGh8bcX55Dr6gX7DLDTXmLyvTWu2SVxDMZ_4X0bCSup_zW064ptQ0n2E-Fn3--ksDJS0NNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
موندو دیپورتیوو |
لامین یامال دوست دارد در دیدار اسپانیا مقابل کیپ‌ورد از ابتدا در ترکیب اصلی باشد و این موضوع را به کادرفنی هم منتقل کرد، اما لوئیس دلا فوئنته با این درخواست مخالفت کرد و از او خواست آرامش خود را حفظ کند و به تصمیمات کادرفنی احترام بگذارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92350" target="_blank">📅 19:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veOveq49CaqGYwLmFi2YQSlYlGTSbH5FP0bWFrZHO5VerKbILuHhNSHqxF0iA01y77Ix9MCi4Eq1wQcjfEuEFuRHgLSEpr_B5ghe_uBqkp3Ei4Bu1LZJEuj4-dHW4fPW1hCPg6GmyjsiGbjAZSPLNT0kgXQkhuMhj61FRYjKYbsmeeXeoBeTjkhwEGIrXUV5S-iR16q_buQ4JFAavkgZBaSQetFr8m6lIekQ64F1MNVzOkmSp5I_ufg8YYMf4flkiLRh7GnyfMTt58py_RS02EjNqsPDjKL7cQavXMf78cATaVZPQolCZ5coyhMxda7My-oPfeFGJJGErQZe4N7_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hl5V0yC01JwlQWygZXpU7SbzSenGABu01fpY8-GuCq4SFebH_sIDDRK2Xf-KpmLXgyv9cD50ql0JetiG7xHjC3oI0cGvDSxV3Iy0QtTpCbmQ0JeYjnTqvkooGWWplFFIAzp9I5hXGSDN9wzJ7kUCUybWDKIM2cmZn2iZUF3nvUaR4L3UcTXtqpIsPcNmkC73KDWIBr9EZ3D5qXkBG5YIafWdWQYx2vGNoWcBCZI2vCX5d6p1cOQ8Kr5kkq1syxoUr54ttPnVjuyYSvnbvENkrEyeM3AMBoFi3E3PPUI7MRmyqw5mHbxT8Ad5YtSQ_2LK2u8-5x-MI-iRyR5PtbTN-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏باز خداروشکر Puma کاندوم نمیسازه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/92348" target="_blank">📅 19:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92347">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtQcwyj6loASsWj9JMKqxYjWL3rqM8EYUqvt_L_Kmo9WlKnH9C87YAINWsYQUm02KI9Fg20veugRvG7yTp9epvQCIG2Dw5X6BRQkQK8e5WxAbMN1poCHKQwYXinfU49JhxSv79VXruuzlBoaSgE7xPHlY28EOBh6FyGZaHx7shDVxQ4rI6V1wuX3ZUungSMI-PacP4LowzSwkbGYltEdjs7RhBbX9dgrdADscVacdCQdx_jyIlrN_yqExflm0blgrFe3NtnQ5qRVac1Sb0eoGgxI8McQkDJxSvGtdk0I1WP7UE9nvPMreyxigdWcl-7VbtCG44AAR0ObhbUvPuEvCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فورییییی از عراقچی: توافق اسلام‌آباد تا حالا هیچ‌وقت این‌قدر به نهایی شدن نزدیک نشده بود!
در ادامه ترامپ هم توییت عراقچی رو‌ بازنشر داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92347" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZW2Ifq3qFoTUs7uhoOo3vZho4CQtDGZowcNF2UKrjrF61GKOWki3b8beFQDrE0iXHodZNgizzXn4iFMATU09coYG-ge2y0aTrgO4_Rvk9495nyQD4nGKyGrqX0Z6wohLlKeUSDrYy7hF19HYq9B_UK6mAYqExK34rXEd9wA9eHs6kTtybnauC1LtHJOAWLOax3fFlyp5LORzkEQRV0HfiIs-BVpJ7ZYmqkzCo9OpRbat2wFHbCXWOk4ArZRxXeLgwYfdl7T5PWO_uGNqP6lA02EzrOdBLHSTVDIBgSnV9wK6Y6-jY6qA5aZJvLQ7b_toWgCDm7FZbmRnwgF_BgXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QuegYvIYJIf8GV4WDGlif3gkAjGarTsdQrDOsD1Pb50zU0UVw1qAELOAtLTAty45ADe3AIQzI-XtYjiosugt1_VpFddSxgQhLo2XKVKVQ1lEM_6xC5a2svjwS9fRC01J43Jepti-T_6KWE1g2m0ZAOojngO2YtKL1-YPLF-o_4JIWC5LQQ6RCLD-tPcV_XOzCTB56GwmZ9L0Uo0GS6qJz3ALZbl54PgmKDNsL2IvXOozoO7joqVmj9ZyybCNB0VAzoM8OCD-YyQjiGUqjBzyLxFwdzkBYc7qeKZK-VqHvyl54eMukGIso2va51N4ab8vlObHEg9HXK_rzBfV8iEwkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🔥
بازی فردای آمریکا تو ورزشگاه سوفای مقابل پاراگوئه‌ست. بیشترین هزینه برای ساخت یه استادیوم تو جهان برای این ورزشگاه انجام شده، با مبلغ تقریبی 5/5 میلیارد پوند. استادیوم سوفای متعلق به استن کرونکه، مالک آرسنال قهرمان لیگ برتر انگلیسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/92345" target="_blank">📅 19:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92344">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🙂
🇲🇽
🇿🇦
داور بازی دیشب افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/92344" target="_blank">📅 19:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92343">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0u1KmQrirsZS7Ou_hsFZlBUQT_zaTKWj_Ut8H7MxTaKMZp5Hz7BR4T3aYZtmUuY5JYe9-1PRjzAdq-GXXZ52gAkPf1dQNtpNriTAF1M-VYa4m4X-c_W0zTH1tvck8Y18gTzjAPN4GdXhzi6gvMmNmuloMBjXFYEStHeu5XyLbl2L28rH38fHLEWBJ3GtrOGlPoxHX_v215qAAFefz1DorhtrPa1x7B24I0iwnUepBy-FWJdJwE5jZ_e2qGMQbKFonQ9j5JGrJLTZp9r1yiQ9Nc_zlvfC_JC53GNCXphA_tOUg-gDl5jdt5DfeMIBSMV45C1r9jIiYt0j8FuXq9q4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاکا:
🔴
اگر بدترین قراردادهای رئال مادرید را جستجو کنید، من ابتدا در کنار هازارد ظاهر می‌شوم.
🔴
تجربه من در رئال مادرید کاملاً کامل بود. من از میلان آمدم و در اوج آمادگی بودم، و اگر اکنون به بدترین قراردادهای رئال مادرید نگاه کنیم، من در صدر هستم در کنار هازارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/92343" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92342">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=FLGJIx5erGcBZ8dpd0Qpoo9p0gBXwD2MtredUrGD-OqAVSyTY1YR9Uk01Ks4CVTpfL3y4uIj7w8zSyhSvszcqCjGfBIo8O2AETHCThRmpnmtkLOykkoxhyfUGA0dxYcrZ0P4xiAt37Jx71axvpITDfkvI5bxZv0jyuBfhpan6im1bTmC1GyYQ5V2J9Felr2L2dwCO0s2oCG_tklIvQr43ojiIEgoMvo52JigLHwyAsxah_VQ70KAUIzYqoa4Fo-QKJ9MwcuNomXdl71DusbQCo7gKXcABjXJ5e6_Qnul6FiIN0-JlJNlESHN493AEY4vKFoVw_IiQbU1HFrQGcX5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/460611eb6b.mp4?token=FLGJIx5erGcBZ8dpd0Qpoo9p0gBXwD2MtredUrGD-OqAVSyTY1YR9Uk01Ks4CVTpfL3y4uIj7w8zSyhSvszcqCjGfBIo8O2AETHCThRmpnmtkLOykkoxhyfUGA0dxYcrZ0P4xiAt37Jx71axvpITDfkvI5bxZv0jyuBfhpan6im1bTmC1GyYQ5V2J9Felr2L2dwCO0s2oCG_tklIvQr43ojiIEgoMvo52JigLHwyAsxah_VQ70KAUIzYqoa4Fo-QKJ9MwcuNomXdl71DusbQCo7gKXcABjXJ5e6_Qnul6FiIN0-JlJNlESHN493AEY4vKFoVw_IiQbU1HFrQGcX5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
فوری/ "
یک کیلو طلا
"، جایزه باورنکردنی برنامه جدید ابوطالب.
استودیو "
پامپ
"، این بار ترمز بریده و با ابوطالب برنامه جیمی جام رو ساخته.
🚀
🚀
🚀
جالب اینجاست همه میتونن، با روزی چند تا کیلک ساده، بدون قرعه کشی از این یک کیلو طلا سهم ببرن.
🔸
بزن رو لینک که زمان خیلی مهمه تا بقیه سهمو نبردن. ...
👇
👇
👇
👇
-
لینک شرکت در مسابقه ۱ کیلو طلا
-
حتما بدون فیلترشکن وارد شوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92342" target="_blank">📅 18:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92341">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64c13f2711.mp4?token=ir0NPEftxSuN94o9njQMle8XjoIhIpRkLcyrBIFhOU7Iu2Hylxsv0-JPVevpIlk8_BQGAUlWddigsu6vPv3olRn7iqmTHVgTZQ9Hmlgq7vKD74BeKpjHCEF2rtNYoweiqHNoSzgAck0wTd-90yLBu71C5JR7l5oVXMAo1xq1B3EI5JJiD0vbZg-p6TvBB9RRDXhhk8YYcsM8vDb6-V__lwD95N6V99oQupJGSiaHx_1BqNRmNHNdHQZm9qMJP2ktqvUfjNyrtUx7TMDRaK0x6c6ngpPFAgp5rPJ81uTEfjOnMFaIijXLXZxUTjcpE5f4xK-UO2mWL90YNM_5FywgmhtP-OGecTUIVoixWv2rKuThM4eBBBsC4uHGbChkPcDKEAR9izA3T9eS1pY4Mfs8Fjwn6ZjTS6ZyWhSEfP7SLKPeqhuH2aPz-H1B6UwCnvmLrBKtDrFByA5NnazvleEpbzPt72DZmqlp1j1vSZONkTtFzw6YAYzp2NysQtybrpDwnaiDvgeocMW1bdwZUWT-e6ndr4dgT2QRfhhiM3iRjrnqj0AAk9ItcbLh_FqyRMvqXqgLkkGos1w3FsUGB-4IsNRN8DRXg5JwmAJwhbP3ENbsm6rHbhJVdN6Vh_uXdmuR8V7NbPYT_POxZcq7RieNvlGJGqs-S7fxnLmGqGNprA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64c13f2711.mp4?token=ir0NPEftxSuN94o9njQMle8XjoIhIpRkLcyrBIFhOU7Iu2Hylxsv0-JPVevpIlk8_BQGAUlWddigsu6vPv3olRn7iqmTHVgTZQ9Hmlgq7vKD74BeKpjHCEF2rtNYoweiqHNoSzgAck0wTd-90yLBu71C5JR7l5oVXMAo1xq1B3EI5JJiD0vbZg-p6TvBB9RRDXhhk8YYcsM8vDb6-V__lwD95N6V99oQupJGSiaHx_1BqNRmNHNdHQZm9qMJP2ktqvUfjNyrtUx7TMDRaK0x6c6ngpPFAgp5rPJ81uTEfjOnMFaIijXLXZxUTjcpE5f4xK-UO2mWL90YNM_5FywgmhtP-OGecTUIVoixWv2rKuThM4eBBBsC4uHGbChkPcDKEAR9izA3T9eS1pY4Mfs8Fjwn6ZjTS6ZyWhSEfP7SLKPeqhuH2aPz-H1B6UwCnvmLrBKtDrFByA5NnazvleEpbzPt72DZmqlp1j1vSZONkTtFzw6YAYzp2NysQtybrpDwnaiDvgeocMW1bdwZUWT-e6ndr4dgT2QRfhhiM3iRjrnqj0AAk9ItcbLh_FqyRMvqXqgLkkGos1w3FsUGB-4IsNRN8DRXg5JwmAJwhbP3ENbsm6rHbhJVdN6Vh_uXdmuR8V7NbPYT_POxZcq7RieNvlGJGqs-S7fxnLmGqGNprA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
برخی از گل‌های لحظه‌پایانی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92341" target="_blank">📅 18:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92340">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Xh9mWwK1yRQVi3uic_k3fOOeADYPzboOIlATBSSzm81uf1VtCPwhdKNkfRbHtOrt1AMkgcIwyXuNeefIu6AHQRiVPj9UkwaPgWmGEaJtjOCVEg1ks-s8mR09Z4N6vltHBmmMEM85idC2iqpUEOdKwIBo-K_EsMHQ4KlooISgiXM5aGbz2o8uSE5nb-rUK1FaYgMIk7H0UCofIarssqL22S77VEpWwavDkKThXXCXWb0KOqDG5Ca0OvWe-Um1lylqI2ErUVWYfqvCdtaXGF2mKWdiAPrDe5_2A2Q_V0-q1M5GLU0lNm0U3xviZ5FBku0Ufqz8cTZLbCKMbFChgMLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو پلیس پروئی دیشب طی یه عملیات غافلگیر کننده با لباس عروسکای جام جهانی یک قاچاقچی مواد مخدر رو حین افتتاحیه جام جهانی دستگیر کردن.
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/92340" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92339">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mX6ihPbRMSdYeSPda0w47GCgrLS0IXEvmY0wA_wgivAVO-EkrFr_xYQannc-tIGDFfPjDrCr1Qwl_EaPm0GM0STZ_d3VlxaR2O3LzKVLOMbfxXYAq8iiU8w10JIOyzl1aanxpjcSjrtfrE8NFzvqhlRJeiUa1-Tu7dqb75gGZQIYEP0vHATjk6utKvY9rSbOO0qUIcNeCPcKg5PI4OPoG_is1cN1efF4U4WFfJ-3VDL9crYuLYAzF24Upk09Nxd9e5kQFl5-4yzIUywhE3E8qsDTUkOgwMRmpXgyO6B-P1s7XBS-DJTrIGcFf6j0GrSjtv8oOS4XGB_85oIqPH3a2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رسانه‌های خارجی از تصویر قلعه‌نویی که منتشر شده شاکی هستن. این رسانه‌ها نوشتن که سرمربی تیم‌ملی جمهوری اسلامی برای نشون دادن دارایی‌های گرون قیمت خودش که همون ساعت رولکس رو دستش هست، تصویر رسمی جام‌جهانی رو خراب و زشت کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92339" target="_blank">📅 18:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92338">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPK_0oUSeDQJq0o_S9Ily50JURGgqKRTtNFsuqZxe7UAs7_L2LZU6lkZz8gTthVE8_oPka8-omETksMlgwk5HqfacxI3bmMBHcZZFbNdi7FFRPOxxfGW-07auO5NXWmFvaQSuDFHTGlhpD3XI1Bo9ciD2QdZiVdJIyxgyMZTEmwRb1L3BDnxBUauN4F2m4sLIsdoVQSNrNdDIgnGE_U1HQuLUfBDUIYKD7lYSt8gilPzBNVBqG6tx0G-Zosm9nsj3kiaMMLNcVzCo4ErBo71PRQJbl6UPbMsAxZuPAb6C_O0oDh8SvrCy_VWAdY6ZTYQEIrC5Qv-0HXLCJk2eLf4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏆
تو کل مسابقات جام‌جهانی گذشته، ۴ کارت قرمز رد و بدل شد اما در بازی افتتاحیه امسال با سه کارت قرمز داده شده ظاهرا قراره مسابقات‌ خشنی رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92338" target="_blank">📅 18:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92337">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGy8rjZSIynDsbLrAzmwrCUJMwJCiD7llifki968qhaKESOOgnxGnPObfRQwSeTJtEg9tK-xpLW_IBBo9Ob-InwIFPm__2Ma0PPv4fafAy9mqW0bREm809jlkqaM0yGtXpiG4VUwlbyP5cYd4oGXpQPthjRxcBGKwOnqMYG5rbd8w-1uNgbWCMKseu4dfQ5r9G2CeeY0rmbRkkO3RKIF18eYQylBE1YEDGDY4D5gYJJKKODcWnA7lHRPlg5WwRS5ZcyGV1PHJfQGNJ50fVi-SpUMn70AGlZJ-fMOS5xjJ7vSE7luBQaXp2FD8ecVQuvvbPMRyFm5tO_sSAjyITYqSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
🏅
🏅
🏅
درآمد تیم های ایرانی از جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92337" target="_blank">📅 18:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92336">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8vfuVkNLAOqFPzCpIblFC_fp_WJ5g9NjV-oda5OcpEtZm9Hb04At9QmLhckvgyaenvJX-lgk0tJjOZfzfdnZI0AY4W9-uRUH3pDtOc8n8DA2D3kJXYMRxeWRrZ6i7g3YOihwLmviKiXM2g8ewZJOxhU1K_uZc--mWgFUDWukmYcMcVH5xcb8iBemol62jVIy-LBx5Sfy1Em9W6q2SZQ1nF3BIAhN8Hpn0eQazThJZZwVhEIdb_AiEYF0_NMLStZptMg6kYU1ng91STdE74xcqLXwnbWQoT1hDsv8XAXirjANGJaqEoV6XdSTBXBTW6bglgyZS3op94K-1GZ5kTz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
سوفیان آمرابات:
رویای ما قهرمانی در جام جهانیه، اگه با تمام وجودت بازی کنی و همه چیزت رو در میدان بذاری، همه چیز ممکن میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92336" target="_blank">📅 18:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92335">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0993fc7eca.mp4?token=HHdBvRmtRMb38xsqvFUdC_2ilF-OVrt3WbqyfUSHds7jRLjdMCAKNNMGiIjeC86cT6OqBt7zMM-lYZyE9q6M8eon571pQxhFsIVB-owuFUPUkkwe5yl5F6PARSIiRtsJAawSBwB0vIG6dNaZDLCwpQ-oulJKYGF4akRq5BMaRARrbwdZ0fswVUgmFVonk3AuKmmJkWhQKXU8nKlkPakgRPMtlWN-5Tz2cagGcTtkG7VBc3Ir8793hmYoewm3P6cE2YeWgRTP0pT5cFw567Fi99jClU_Ay5fF0zqsGUN-z2hdaMq8rFQzlm9k60Pk2f_6fnDxQmCiSDILSSWx_QqG_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0993fc7eca.mp4?token=HHdBvRmtRMb38xsqvFUdC_2ilF-OVrt3WbqyfUSHds7jRLjdMCAKNNMGiIjeC86cT6OqBt7zMM-lYZyE9q6M8eon571pQxhFsIVB-owuFUPUkkwe5yl5F6PARSIiRtsJAawSBwB0vIG6dNaZDLCwpQ-oulJKYGF4akRq5BMaRARrbwdZ0fswVUgmFVonk3AuKmmJkWhQKXU8nKlkPakgRPMtlWN-5Tz2cagGcTtkG7VBc3Ir8793hmYoewm3P6cE2YeWgRTP0pT5cFw567Fi99jClU_Ay5fF0zqsGUN-z2hdaMq8rFQzlm9k60Pk2f_6fnDxQmCiSDILSSWx_QqG_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهرا سامی، مجری شبکه عراقی برنامه جام جهانی هستن
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92335" target="_blank">📅 18:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92334">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/051f0d1e00.mp4?token=XVv6nLmB8i4WeV73P4aK6KWZ1f9mlGwMJx9hKlWlhqnvSF9lFkx0fUKtNFYiDjVOk7kd4N7EVmmjfATj27HknPN9KLBVVsBsvXhcXp3ecZOgCJPtyvb9oIK8sncAOKWLi6L6za944w5jfnM_BgKM64w_o1Xlugfkn97jlYiC0HWOas7AYmadOvWsZ9lVt83oIJwCVWfelwwv6N5x-L0L_iUJD-56Mp7GyQhcaW3uKZsWm6CYDabiVBixGqIwLgs59k17eMPia4foV-Vov5A3Q_v5tffXoS_9lmcs17HnTlSvIuH5o7lWD2OithCCWeskzHqcDV4QX7tF5NKjmVevZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/051f0d1e00.mp4?token=XVv6nLmB8i4WeV73P4aK6KWZ1f9mlGwMJx9hKlWlhqnvSF9lFkx0fUKtNFYiDjVOk7kd4N7EVmmjfATj27HknPN9KLBVVsBsvXhcXp3ecZOgCJPtyvb9oIK8sncAOKWLi6L6za944w5jfnM_BgKM64w_o1Xlugfkn97jlYiC0HWOas7AYmadOvWsZ9lVt83oIJwCVWfelwwv6N5x-L0L_iUJD-56Mp7GyQhcaW3uKZsWm6CYDabiVBixGqIwLgs59k17eMPia4foV-Vov5A3Q_v5tffXoS_9lmcs17HnTlSvIuH5o7lWD2OithCCWeskzHqcDV4QX7tF5NKjmVevZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکالمه اسپانیایی جواد نکونام با پائولو دیبالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92334" target="_blank">📅 17:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92333">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5718ad0590.mp4?token=HKb0AkgEeMm-ldWyUaS-XsmcLiJKswoOAOGoku09Xu-pq4k8NYksF4M1UCR_Z2Bod-8GN6UVfmcHrzOBWAqhAx2UBrVaWLzzvR058dvY9nFkb3C6Bug6I6jy_vKaQWD1larEVQMcT3xbG4neDXs7kXwvBmx3NTWYNZ28gOshUUYeqowfz3Wmi394OVtUpHmAOuWYodEKI9UPE_nD7nfECxVtIa_PEnyZwoWlkuN6c1fOAzrJXOhBBnBnQJv1I7G9ROgAUgN-AiGjL8ZUUX6FXrqTOWJkOzcwo5HYIz-eItJ_M4vLnvnAvgpcb_PNHGnsTBmHOVDKQSnbN2BZ-CzJMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5718ad0590.mp4?token=HKb0AkgEeMm-ldWyUaS-XsmcLiJKswoOAOGoku09Xu-pq4k8NYksF4M1UCR_Z2Bod-8GN6UVfmcHrzOBWAqhAx2UBrVaWLzzvR058dvY9nFkb3C6Bug6I6jy_vKaQWD1larEVQMcT3xbG4neDXs7kXwvBmx3NTWYNZ28gOshUUYeqowfz3Wmi394OVtUpHmAOuWYodEKI9UPE_nD7nfECxVtIa_PEnyZwoWlkuN6c1fOAzrJXOhBBnBnQJv1I7G9ROgAUgN-AiGjL8ZUUX6FXrqTOWJkOzcwo5HYIz-eItJ_M4vLnvnAvgpcb_PNHGnsTBmHOVDKQSnbN2BZ-CzJMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عیش‌و‌نوش کره‌ای ها و مکزیکی‌ها در‌ روز گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92333" target="_blank">📅 17:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92332">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2cc8b70f.mp4?token=tytsjvX1s9rtxddWfsrdKEIebZyKYyo5PUKSRNHSv2QAe_2T5aOLhKRNKYaMyej0JL0XTBbxQl01sj4eA4v2B0XqN6Isc9hixsTGVOuioWF1UMoPn8y4L3_MKWgYOrISUlf3UwtRWfJseFM4SFtyl_L5djWbq_4kY1izkVwI2BxoL-SFWtJ_ptiIIt33I-6djWvMiYJ_-GQxoQAtCBUHlTvI0BHXAupPqf9xPabW5Ijrq4ZtA9N6s3h-FE3LpTo34ZK3NbovH63xPJ4lm3X3kPPTKuHYREl3uyvYZ8oaMtOmwRTsoS9lupD9U6cbFtYNLG9u7B0RhzVNDcMaUdQRCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2cc8b70f.mp4?token=tytsjvX1s9rtxddWfsrdKEIebZyKYyo5PUKSRNHSv2QAe_2T5aOLhKRNKYaMyej0JL0XTBbxQl01sj4eA4v2B0XqN6Isc9hixsTGVOuioWF1UMoPn8y4L3_MKWgYOrISUlf3UwtRWfJseFM4SFtyl_L5djWbq_4kY1izkVwI2BxoL-SFWtJ_ptiIIt33I-6djWvMiYJ_-GQxoQAtCBUHlTvI0BHXAupPqf9xPabW5Ijrq4ZtA9N6s3h-FE3LpTo34ZK3NbovH63xPJ4lm3X3kPPTKuHYREl3uyvYZ8oaMtOmwRTsoS9lupD9U6cbFtYNLG9u7B0RhzVNDcMaUdQRCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری نیکو ویلیامز از خروپف یامال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92332" target="_blank">📅 17:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92331">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=KlTMlJO123ru_1xpzsvoG6gwN39qu9KkfJlyxifWZuHVntKgb1dtOJoj2cFmcZAW60UZTxkhBSN8TFdqoxtzdAa2LTWd1EUyYWQdp2RMmhM1R_6qtghTGWwYEYD3m8x7KdNuhRIXuWcdmEIDFejCJfuazSU1h1tGxv-8IAUSOEnh6kPUBo_g2u6IxDqrRPRKzk0FZPdRuSjEIPWnKYUx2MGaU4nz5WHJUG4v74ceV6Uww9IPX83FI7O_DfZ2n23qe1Qps04XMsFMSCIMz3SBTsGqWDKGcsXiNZPeqGfxvHkjDXuSaZ1i3ny_cHQzg6zA0HjElHSkjmU3HcQQ0lj8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbae198e1.mp4?token=KlTMlJO123ru_1xpzsvoG6gwN39qu9KkfJlyxifWZuHVntKgb1dtOJoj2cFmcZAW60UZTxkhBSN8TFdqoxtzdAa2LTWd1EUyYWQdp2RMmhM1R_6qtghTGWwYEYD3m8x7KdNuhRIXuWcdmEIDFejCJfuazSU1h1tGxv-8IAUSOEnh6kPUBo_g2u6IxDqrRPRKzk0FZPdRuSjEIPWnKYUx2MGaU4nz5WHJUG4v74ceV6Uww9IPX83FI7O_DfZ2n23qe1Qps04XMsFMSCIMz3SBTsGqWDKGcsXiNZPeqGfxvHkjDXuSaZ1i3ny_cHQzg6zA0HjElHSkjmU3HcQQ0lj8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
🟡
اون چیزایی که ج.ا برای رسانه‌های فیک‌نیوز درز داده، هیچ ربطی به مفادی که به‌صورت مکتوب روی اون توافق شده نداره. حرف‌هایی که زدن، از جمله اون بیانیه ضعیف و رقت‌انگیزشون درباره توافق، هیچ ارتباطی با واقعیت نداره.
🟡
واقعاً آدم‌های بی‌شرفی برای مذاکره…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/92331" target="_blank">📅 17:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92330">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
فووووری از رویترز: توافق بین ایران و آمریکا توسط جی‌دی ونس و قالیباف امضا می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/92330" target="_blank">📅 17:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92329">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4e50671e6.mp4?token=g3Zdp3gyZNeH-G7dMtCnMjX2F6JnlyIj03XnUTyQv3GqOM5fkxz094yMS-G-ofJQSEPpD7e_oW8SbFI_1vs7atXqFOIToXhQgTIuqeDMB-ouAy2N-15dsaVP7fH9E6MxmU87UKAT3-JJQyTUHtkWO46169lhV4T74E9k-pxD5mYYRaF_iKYnT7VzvRc3sgm5hs8eS3RRPBkLcl1hpiQBxKL6gQ2aMQrBu45DJKGauppKFdV7s60DcVLdBBZhKFZ20pCqcv7b14Fx8hWC-vtVT8I5Mcw6GsnlgvTzBexNAS0IglwxSSyRmqhwPzxMHu_AlSk-3ANGBM-lVqi-wc04Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4e50671e6.mp4?token=g3Zdp3gyZNeH-G7dMtCnMjX2F6JnlyIj03XnUTyQv3GqOM5fkxz094yMS-G-ofJQSEPpD7e_oW8SbFI_1vs7atXqFOIToXhQgTIuqeDMB-ouAy2N-15dsaVP7fH9E6MxmU87UKAT3-JJQyTUHtkWO46169lhV4T74E9k-pxD5mYYRaF_iKYnT7VzvRc3sgm5hs8eS3RRPBkLcl1hpiQBxKL6gQ2aMQrBu45DJKGauppKFdV7s60DcVLdBBZhKFZ20pCqcv7b14Fx8hWC-vtVT8I5Mcw6GsnlgvTzBexNAS0IglwxSSyRmqhwPzxMHu_AlSk-3ANGBM-lVqi-wc04Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
ورزش‌در خانه پارت‌ششم؛ برای دوستان گشادتون که‌ورزش نمیکنن حتما بفرستید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92329" target="_blank">📅 17:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92328">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e115a319.mp4?token=KreWh4GPhtky6Z0ZEMFMQkOf-IrZdL-X2zYxX6E1XOCwozTNlYk3icTb-VCw70ARp8NaTEwdu6_8YPsxShaR4R_cYTQPvZL9NmKkC68UMjcSqxBEdGVQDtFfL4NNZMsX-kIWcztPM2CgrlYnuRYMYOYU5wn53fBRylDup4L8o8mvYtBrUiW7g5wdYBwu3d22w9UZvc2WSwSFpRahxdRrVo1yHrHvwyY-dNE0rMdgzwtkMOU6jh0geUmGdwiGr81BGaftArn33EVcM62m9WE7s2YTkG3qqEmX-6clJwbbP5FfkkvYmPsXA7AJiRsnEPcsdnAss157HS5hi91Cp5D4kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e115a319.mp4?token=KreWh4GPhtky6Z0ZEMFMQkOf-IrZdL-X2zYxX6E1XOCwozTNlYk3icTb-VCw70ARp8NaTEwdu6_8YPsxShaR4R_cYTQPvZL9NmKkC68UMjcSqxBEdGVQDtFfL4NNZMsX-kIWcztPM2CgrlYnuRYMYOYU5wn53fBRylDup4L8o8mvYtBrUiW7g5wdYBwu3d22w9UZvc2WSwSFpRahxdRrVo1yHrHvwyY-dNE0rMdgzwtkMOU6jh0geUmGdwiGr81BGaftArn33EVcM62m9WE7s2YTkG3qqEmX-6clJwbbP5FfkkvYmPsXA7AJiRsnEPcsdnAss157HS5hi91Cp5D4kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناموسا اگه اون ۲۰۶ نمی‌دیدم فکر میکردم خارجین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/92328" target="_blank">📅 17:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92327">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAvFhPdzXMWx1rBkaB2SnEwdYd3uRzOfwNgspO_ErU70I12SaZxCN34YLCOolZ2vNB2xHJUb69C_1DZZk07lN7R-m9KIVqTVgaJOqze2nnF_E4_B8RsRprb17RAQzqO9MNzQk-pgdXsKaim2_E9TPmf4e1vBLq6KgLvjbtlhyHh5ngnCXrr8tWo36235ChRCqL3FqeZFLd7zlQzAGVvgy7rQzZG1Ol67A_1_7TsD2nu7CnUbGYvdAlrZWeAdeIFL0G1_mfpXhLI2EIQCXlc3AXsq_t5X9ord0DPFTwzAF83EExzYHaf3Rx0QZ5Y8O1Rs56W4RCKy6q1iyBG1Ys3F2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏆
با اعلام فیفا ادهم‌المخادمه داور اردنی بازی اسپانیا و کیپ‌ورد را سوت خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/92327" target="_blank">📅 16:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92326">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-IyGWxfd5GDApySd45_WDndGwFMWFFDZ9nnBi1E6KXP9A9cJsj6CTdIfRXOwxhpPT8JE9b-4JHWS6CWvBA1IieDAGAS651dVg4g7QOlu8B-Bb4nhkETpKfOWK7-Xk1sSR89FgfRTqQWP-bRHTMATjkvy7oX4sqSQSXVUfUBbOn5CRmyWjSrOIUSwLeBOyBpD5Fz2vGm9FgjSdDooQThQS7vXrSjnnkZDQk2S0aQn0N9C3PPb6SJY4x-TdAMS6Umye5YAB8xDvDtb4FwDQTogZS27VpEFTp-l2BH3IeqFBPGwZ93AMwEU059oBXTR1h1nHkC5kwTTjTbC7oojBUsgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇧🇷
#فووووری
؛ رسانه‌های برزیلی: وضعیت جسمانی نیمار خوب نیست و احتمالا سه دیدار مرحله گروهی رو از دست میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/92326" target="_blank">📅 16:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92325">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFcK4WI3uoZq-OpWUHwqn9thS67JKz44lbeGPH1HC3jnnZu58LuhycaP4xV1Vy07qymyOrMfsxla4ZamXnSFfEuzPWZHKAnoIORQozn_5YZQUJt8W3-OGO2q5SFKf7hjDUKcYwq6AsRNnq1Xn4dcBJruGwnNRV373hxqr8vJgt1-J7HKnZR9REvv33Kv_ptLeaNyd7BfH-_lp6l9nKYQDZU40xJ7Pw5BJducuv0d3OkN0-G084Ud0STFVMvdOH-0_oBlhSUMRyGiGdQGsqzIkfupuekgZL4L4HeeT_ZEQ7wOUSmaDTvmFqI69VSTRGDaN8iTFgRYYwvM2T9fRKYgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
🇳🇿
سزار راموس مکزیکی داور بازی تیم فوتبال قلعه‌نویی و نیوزیلند شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/92325" target="_blank">📅 16:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92324">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOGbO_zbpmvFBqhsZI3fgpio6_L3N-aEjDlXEp7dRbP0u64Kvx2dPiYwRukxGtYxGEeG8R7pn74we9kbZxv5Pt2bYlHBgmUGJz84QoMB1uSqpj0m1LGUcHbNFp-FgUP_cbHDjFsy9d9LEbMtXjoelhenXWA6mqueQvV6evjpy8N5IGJqYoBylcK7ZVk7UJk0uJDpmumIFchDSQiqtX_wVMJAu37HnxReEe1JYUNRJ95cTEWug-FZvjHgcmxpdpLLDphgEbf7m_97WjAWb3SuVk6JVWBCm4JpaokKDUjMGVmyiKrGZ_dCf06mZkY_lKZ8n1BbCiuFUKrxXzTZcwhQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فووووری از رویترز: توافق بین ایران و آمریکا توسط جی‌دی ونس و قالیباف امضا می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/92324" target="_blank">📅 16:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92323">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf8fe0259.mp4?token=LfZpD1abBuX237kQskDOS3auCmCNSdQxbhNOhsnDyNtC3rCHv7hpG9jFtK_ehxCaoMTHOd6Su724PRcsQ-_Vxe3Nj2tMrovsOjaJuUj1-6Sg6j1yjw_GABOK876H9L_FX3078aB8sWbr98F9AJFwulWP8yFEF1dOb7q-JYEkAK5hklo4dQDiMT6HDn83BP96GTamA0uPojzfi3FmYIzeE2P8wHqo6LG5thQfCRQTZNZxIMgoULDQJqyqbBBrLf02JO7pyOcBAN3YKRxi_SKvLFbBIv5rACRdxa5p4xhY64NRohm0puCBCGo5ryPYli2mJIm-uMX05ZcWUaqaNAqI9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf8fe0259.mp4?token=LfZpD1abBuX237kQskDOS3auCmCNSdQxbhNOhsnDyNtC3rCHv7hpG9jFtK_ehxCaoMTHOd6Su724PRcsQ-_Vxe3Nj2tMrovsOjaJuUj1-6Sg6j1yjw_GABOK876H9L_FX3078aB8sWbr98F9AJFwulWP8yFEF1dOb7q-JYEkAK5hklo4dQDiMT6HDn83BP96GTamA0uPojzfi3FmYIzeE2P8wHqo6LG5thQfCRQTZNZxIMgoULDQJqyqbBBrLf02JO7pyOcBAN3YKRxi_SKvLFbBIv5rACRdxa5p4xhY64NRohm0puCBCGo5ryPYli2mJIm-uMX05ZcWUaqaNAqI9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
عشق‌وحال‌ این‌روزهای هالند‌ در آمریکا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92323" target="_blank">📅 16:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92322">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz8FSzZNvQ8wn8HK8oSLzn8e77AyRJ4MTBHmUVllgGZMigSTn-Jo2uQtLVovxTWpGEmX7ZhZCy-lhQsvkR7L-DFKdvMZJePS__NDlQDJmBepKklLBI42d6ry36fz_GaJMSqamagj5-qehG1B_uBjSGlXgLc9KzptA4OqJXRUREKWKe3zWvHJgR3AWiwOenwOKxJdtl1GBZUzUWxvFB5pF6U6z09GreN3UOV5NlENDnyRwXHzhzwDJrYS0OmpaJjcv789sBp7BaiqG-gqpQqxzF5xxsszg-CevKDseCJKcFFNVnnxHHz6gUb-YvEo6d8KLdL9iGVImfLNrmM7MqZi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
عثمان دمبله درباره انتقادها از امباپه در اسپانیا:
آنها با او بسیار ناعادلانه رفتار کرده‌اند، مردم نباید اینقدر سخت‌گیر باشند.
ما کمی بیش از حد به انتقاد از او اهمیت می‌دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/92322" target="_blank">📅 16:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92321">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWrJPSJPuHlEUn_ZVZ-ZEjLewvpeCXO3gUkbXIt8j7zt9i52odOM_J59BOQuLzSd-8taRhQByAyBavCSSlKAO55pNn8He6nB4pW4_e1ldAGSLEEs0caSGK6L4gbF9yRVFvOE3SYyB6TXYBqOjlJpQJOMUuJAgsWzSikrRj8kKuDRQl4302G34bT6eTUcarOfm4EmMSmINblyy0HD2RQisf1SPydzQ5a_wHNhBnPrayNEe9jY-bcveqqhkNC4FXD5edd7DQAhfM2Mkv5wuCe4ICxih6VwnUCnu8LaByYQIO0nGUy7M0RH5I-yR6G6a_DebUInxTpB_bt_UAwHTz5kwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
گاوی:
اگه با اسپانیا قهرمان جام‌ جهانی بشم موهامو صورتی میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92321" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92320">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEmBWvUpiMzpU67WPxVVmElQ9RZf98wCCmQf8RA7NjtdtFuDaWIodSE7KgB4mAYLjg1H1bmF3GtBXIrhYP0dSG7easQ_bAaoSWP7Q9ahs5SResF0E3wf4yy_MEuvHIjirQdP-xo6nN8KBdBpT2ZsP2nHipo1uuRvTx_llu_VWH6Qtq4c_8ZPVIZ-gxHQsILXW-g7pj2u2zMLV8L2EOF9rOHQyPzBBJCNbhvWdg5jMMI1LS4DseFZMBpsq88pV6StvT-ELpGdxO0jKAKhPI88IVR2mPV1XKFaSrI709YjPE6PtZyyf6zG38gAqavgUNIjYWJiU2LdlChjKNWlMMnvZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
این مارکوس پترسن نروژی است - او در پست دفاع راست برای باشگاه سری آ تورینو بازی می‌کند.
🏆
✔️
او در هامرفست نروژ به دنیا آمده است، که به این معنی است که او بازیکنی است که در جام‌جهانی از نظر جغرافیایی در شمالی‌ترین نقطه کره زمین به دنیا آمده است. هامرفست یکی از شمالی‌ترین شهرهای جهان است - این منطقه به خاطر موارد زیر مشهور است:
❤️
خورشید نیمه‌شب: از ماه مه تا ژوئیه، خورشید هرگز غروب نمی‌کند و نور ۲۴ ساعته تابیده می‌شود.
🌏
شب قطبی: از نوامبر تا ژانویه، خورشید طلوع نمی‌کند و دوره‌ای طولانی از تاریکی ایجاد می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92320" target="_blank">📅 16:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92319">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beSCwC_7osx_ntEW5rdQKAEyTWv-o0fqybn_858c2StkS0qTn7vZYqKqSEVxfEkGQEbWzgeZwWtUUnVJH-XmUlRtn_hbse3dNyTu5EPQ5hXvVVEeAimlHkOr40r9Cv_D2fIDV_tTBjJpD9V47O9lws3dEpSxm-WQBMgDau7b6DYIe08N2sRPZglFYqzbmIyMLFielZlNVu7xI1vmjeKSb8VVqw5X-AO4DswsTi-0p5gBxM6JCMFLR8Dl5BT45jfZqBbflieZlZluI_G2khyYtpaHSUkvr3OhRmNTitibqOA2S4Ue2Cwr5E54I7Q7HirHqRgyl8SuXS7cmBz6GMoIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گویا برنان جانسون هافبک کریستال پالاس، با لیلی فیلیپسِ پورن‌استار که رکورد سکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/92319" target="_blank">📅 15:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92318">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a9fa2e76.mp4?token=u5AjDtZHg3d2jeyF1MK7JPrSjkkZkEGZmxF4KMowzgNQFogj0N_pWHCAm1XaKeeQSgRKd1PMzaIwQ4z0h1r43ymVbjq92v9uYcmo73zFG-dRbnYnlwqcixga6gZrIJNAnRRvDQEm2VewbCY1cswWR86PrR-JpD-AMJ6Z697uP0jNFmMEn-QnoEVqle6LsD42ydrBXkU_GokoZ4_Z0RjaZYeeeORacYkvRGi_FqdAnKK1U7MOUumpyHi81di9yZdegJDTCNqtOfVi_6j8Wa_Aasr1zMEN-6bdISbHTbeEgXx-W3Ts1e8HkC4o4YnnX2u7q-m3KqBPH0RMy7EfaoULAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a9fa2e76.mp4?token=u5AjDtZHg3d2jeyF1MK7JPrSjkkZkEGZmxF4KMowzgNQFogj0N_pWHCAm1XaKeeQSgRKd1PMzaIwQ4z0h1r43ymVbjq92v9uYcmo73zFG-dRbnYnlwqcixga6gZrIJNAnRRvDQEm2VewbCY1cswWR86PrR-JpD-AMJ6Z697uP0jNFmMEn-QnoEVqle6LsD42ydrBXkU_GokoZ4_Z0RjaZYeeeORacYkvRGi_FqdAnKK1U7MOUumpyHi81di9yZdegJDTCNqtOfVi_6j8Wa_Aasr1zMEN-6bdISbHTbeEgXx-W3Ts1e8HkC4o4YnnX2u7q-m3KqBPH0RMy7EfaoULAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سی ان ان یک مونتاژی ساخته از صحبت های ترامپ که 39 بار گفته به توافق با ایران نزدیکیم
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/92318" target="_blank">📅 15:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92317">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnPYh2MDyiysTzUe9IlaYD7RcXeH7pe3i6ubNpW0kjc8edAXT7adls6gbJzIwbQrZQ-xOlC4Gz6l7RpNMnTd6zAP3_2Il9wDVZ2j2reZ_y0dwygZWM74sln1r9Wl9ia0fnnwExD-uhE7GUhqWF4R1tPVZgoBOrH0P6kjsBdWoQqvT96A4AizsdXc_fmQU7YkP6-XPt9Vj8ssuQGr1FhrT4SD3NDzFG5dQEHNJ-Pn4IREvHYQmG-DEaKig7GQl_TstbxofXSwQoLIQiJKNhbzuu8FGqr093Ua9Bs85PDZREDZ1b5F30PxKhOUQldp2mMFzOgNpFbiOmpChp0VbgYv8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه حس و حالی داری؟
🗣
کریستیانو رونالدو:
مثل همیشه احساس خوبی دارم، با شادی فراوان. میدونیم که این یک تورنمنت بسیار خاصه و با امید فراوان وارد این مسابقات میشیم. از نظر جسمی من خوبم و هیچ مشکلی ندارم. قهرمانی؟ ما یک نسل بسیار خوب داریم، اما عوامل دیگری وجود داره که کنترلشون دست ما نیست. من معتقدم این نسل شادی‌های زیادی خواهد آورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/92317" target="_blank">📅 15:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92316">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eds2ZaVs7-gKhplTw0rxZYQDG3siA1TYktEKtA-WjyARd_Gw0vu-sYxVyf8IcMZlaBlp3TihbbgRw6cZh-8PUXO52xG7JDS-NfyBDQsEBHrfuceuK_JWOBgFlT1VC61N6INL2JFbmfCxgjA0J0ELSdQ7m4iGuIZgq8o2TnfPINYwKHtM3zoYxq2jUN-ZHE5vC7-_NaFMIH3IzBvMWpdWq8g1wcQHaM4onCQR7B8phsE3f6Nx92Yp1_vrN5oATfPy1NwWkk4Ml_A1IsC9FRsqhGuOW90YqiS-kNrFjOBLPCitfKWUPz4Y4j7txrZum5bojFvDhnn3lZQeis0JYjzGrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
هواداران جذاب کره‌جنوبی در بازی‌دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/92316" target="_blank">📅 15:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92315">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PByGHXsZCFo9oPKOGzYEzY0PX00Tv_VDf_lhYWlN_gJLbr8irJoHToTpH-gYut8oSNm697VkL2LqWl_ibswdd7StlOotKXGBfbxbca-s-9BjMVCCZ7wUjFvcxUuna3fykrvfNTni3z8oF73X4MFP8H8znNUKw0n6rAsHrSXNrAlHU3kCRpvszBnTN3hKQ3AwoFRwoz6mTaEv_k7XMqSF-lbjO6dwj1rem8CxNkmTrMEPLCmlaW-xJqLOHuAoXgsUFZSZBnB9w1oWNvNPJlyup0nrHrMnBbkg_jG68bZYgjXMB3jr6kgllg9TtnkGJVOne_38qahYbRBXT_fuEQfJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🏆
بهترین بازیکن دیدار افتتاحیه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92315" target="_blank">📅 15:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92314">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3CTaaW2cMKv1qX0sjZkNZ5o1fn6uo1w8XV_MZgn2Hr3GwVn3oCrscTGwoSCaVGBH1-TefqbpO8QByfj353FJ1HIYtyUG2jJ4nRoIPmeyjh66ED_JMgpdvVC0M-HVKorf38bQmtdiGJdVm33WUstUyVsOj1AWbD0i1KSpnG57fOK8Lb8gNvjPsREGDwgAEtdfGSl7UfGj5IvKMKvaQi0UWgHwOuEO9PS-CMl4wwtRAF2IdF-bbU1iS6QdfNwAzLgLdyGANKQjGQWTzzkARLKdIdjPcvk03Kok32Rni2U5vmsqvUJgS7qRYCLUAJf-fgbgcyaUqqyZ2YxpgjxpdHmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فوری - موندو:
عملکرد وینیسیوس در جام جهانی تعیین‌کننده ادامه حضورش در رئال مادرید یا خروجش خواهد بود!
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92314" target="_blank">📅 15:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92312">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6EbNR0dN9kQbvQdFKxp3UkZhZNk11mE8pYKKyCKLGx59i7JPTS9fwLx_NNGlRZ-ccYTibZCipzSw_L7F9VIjXpL7fmjIELe2UR_RztQJcXHu0KESfyK5TahGGXZstbbYlMDZrgB9ev1mG-nCC6kfSKaBGfwHRWE_pNOP7eGJHnyn1qiZjHslKdAMwfXhFEXmtHGVQIP_ngeaJ1rZ2pine7G48BdBZRlNrG0cidjfXhO5NUbDXIcCei1v3Wnmn8rmwuPApcEzoHQyLK1HFz9b0Zd0XUq8aGAdKq0h1QTZWeNleV1WJcWJgBKcjiMWHly1NFcLhS6A7CafKFClFFeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z6YMubJ-UPHAX1W_lfjQwnNqfTUYv3OPlPo3UUvciqR5L1Mnrr4J_mk2EOpIRGTn1SuCIzoHr_rwIPIOKfcKtpzr4Yi2f8Efe5GsRNm0tYonftkVmnbElOS0iADFILWbsIJFAwJJP7o74LBM5B3xInJjzyvqEcRAjkU0LwyUupcLfJBolj6aLix68INDXuONuDwiMUTcIIuB3jastfaFuCEMhm7NMtGSRdrC-Z_Fv9BeUaHOE7_2aEp-8YARKYwHrssIJ9LFNynU01vsRmvcACE9dNj1t-3ck9SX6l1cbQqg5bLZF0gRhy23FNB6dMc5vKmsM1i7J8daYWCSmrPsCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بروبچ تیم ملی کنگو هم با این استایل خاص‌ وارد آمریکا شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/92312" target="_blank">📅 15:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92311">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsElo8xikfL8-4lEOxO8O-oSU-75aNSjvzcajVWs5C61M7d4nZHfeEQ98-Ne-bmslxhCGut396W2Xi28H2AyE9Fc4JLhSe2shs4_j7H4Wl4u8nMw_X2K6rugJ1LXFeqNsEAm131PH6wbEUrWo3Auwz7QmbgxqLTF-U1s4p47kECqlIekWAeDczEz00L47UclDlSve_vdmqmUq-m9OAjMBAnNbDkulTtAsxnA0OmkmgiPZ_kEh6rsPD0ozrFRIU2c0r5HEG6TZCagGR47RlnKwf7XaruIaUS80mQdbBmub5UYQ2mM9HJTNrQCt_sfok-eni2DS_iT-AvNnMT7aFqfGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل اجازه داده که پارتنرای بازیکنان انگلیس وارد اردوی آماده‌سازی انگلیس برای جام جهانی در هتل لوکس وست پالم بیچ، فلوریدا بشن.
🔹
دوست‌دختر جود بِلینگام، آشِلین کاسترو اولین کسی بود که از این فرصت استفاده کرد. او چهار ساعت با ماشین از تمپا سفر کرد تا به دیت با بلینگهام برسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/92311" target="_blank">📅 15:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92310">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5515e03704.mp4?token=WqiYPT_E8-Crrw-IHSgxXmekece7S87eUABsMhzEdEoV9HzyNaoccDeSV8vERgRc2Ei3bJf_MbgXKrxRtai2HIEzcUL5rlpOsKH-TUDAFDjPOw8Ba855XtkCi1deoINRv0vgN2MK7WuYwNPusN8i8PeO4HOd24MxodiP5O1zBUnTmwcY05TcTgrkvXU4SfNKrYjUDlihMij0bvqq3U5O5rZlKSjdOIMI4Fof4xXpfcG2gv68fPqvlgG8WE0a0SZKZjUTHyyb-eHnPIsC3zxLViSHIOcJCcbRtGse6gmTUWHqKdBNtyi0GvUNJqdmZ7mhFrG7GrD6bqyp5UjkT02ZxmQCN2sk5de-URsKek-9Yrg7W-GMw4NPwTFdmSWhGlzj17UrZ-zzyGN9Ow0SCkdq-DOTLLk64-3Axt0uBpxLEx1v06xRz3plPPMwHEVYv-96xEw3lZJuwbvCNyoMKTwcuemRmyihyxVOxyma2GuvHFswTow15z18WNf2iXzuciyjDSI5KOA0p6YSuILLrrfDizuhLvS69oY7pCSUGxIBgvrLd-lP-JiyffAyWeNWnjzYnGI4bR776r1HH5TCcFGfB18ryOBnMmYorABLlskDWpSGPMUhoCT7lyNdEX5Us5Crb8H4CgKiKKPhzGiKK1k7Z4G6mZpyECD0nGxQ77vJ5mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5515e03704.mp4?token=WqiYPT_E8-Crrw-IHSgxXmekece7S87eUABsMhzEdEoV9HzyNaoccDeSV8vERgRc2Ei3bJf_MbgXKrxRtai2HIEzcUL5rlpOsKH-TUDAFDjPOw8Ba855XtkCi1deoINRv0vgN2MK7WuYwNPusN8i8PeO4HOd24MxodiP5O1zBUnTmwcY05TcTgrkvXU4SfNKrYjUDlihMij0bvqq3U5O5rZlKSjdOIMI4Fof4xXpfcG2gv68fPqvlgG8WE0a0SZKZjUTHyyb-eHnPIsC3zxLViSHIOcJCcbRtGse6gmTUWHqKdBNtyi0GvUNJqdmZ7mhFrG7GrD6bqyp5UjkT02ZxmQCN2sk5de-URsKek-9Yrg7W-GMw4NPwTFdmSWhGlzj17UrZ-zzyGN9Ow0SCkdq-DOTLLk64-3Axt0uBpxLEx1v06xRz3plPPMwHEVYv-96xEw3lZJuwbvCNyoMKTwcuemRmyihyxVOxyma2GuvHFswTow15z18WNf2iXzuciyjDSI5KOA0p6YSuILLrrfDizuhLvS69oY7pCSUGxIBgvrLd-lP-JiyffAyWeNWnjzYnGI4bR776r1HH5TCcFGfB18ryOBnMmYorABLlskDWpSGPMUhoCT7lyNdEX5Us5Crb8H4CgKiKKPhzGiKK1k7Z4G6mZpyECD0nGxQ77vJ5mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇰🇷
🇲🇽
دیشب قبل بازی کره‌جنوبی، یه هوادار مرد این کشور از یه خانوم مکزیکی درخواست لباس میکنه و بدین‌شکل وسط خیابون لباسارو میکنن و عوض میکنن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/92310" target="_blank">📅 15:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92308">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kenv9zNPq1XsnJsNWW1q8RzNNOed91Ju6vH6HTTc_xlWtRrKQxczMPP14oxGRsT2JS3LCXxWE6dKCL8cSo8qfmA2SQ0_EfaV1n0840y_D6QSOOzbEsXTSZUCdl9lx2VCP7DwBeYnDF4fCeFMEY2T-Anox0vcTdzsILhEW_Gg1QmOo-RXykjw0yopEcqdEYQn-ES0PmNU9nsbGQysXmKg4q0R6LEwMsEU5LlvO_D4xqArzI0XDdX3j0VYgaaY7HVJZAvu-xZ1XE9-E-OK52LT-3eMqGktFzHDyubBLt4hydW2Y_xaHfkH00xk3QdG-iBuMjsYC9iivblr1owFV9rt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GForV6TSrrtqq-pojTeDT-Q3a3m8exFUjzDH7VlBJj06GxvJ1LwuhSPIByYaeuYCzIV44qYeoJCPRKYDMCn97J3kfw8FCbcp5uaNhpkKmCJIOfos3s1n0Fe5pYjl4VsXN22IKMGjIvM-rMptMsj144ToOSQpkRQ3_C4NTLSVk0LMGHjqL3qsgwqruPI1-T8IEDWV5lx7KTD9fdPBXJ_4-kQBoADdC4pRJbmlzlOrG3ivxldedUnuE-pv1U0PCu9uAFsFy-F-9CtOTCohdwjERfER291v_7Tl3tKQElEhEd8IdeDYOv1Wj0iI70klhB9VQbLwAqDUb82swlxEDnOwdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این جام جهانی هم قراره زیبایی‌های زیادی ببینیم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/92308" target="_blank">📅 14:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92307">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0d71bdc80.mp4?token=bQeqmVjTRk3NqnVKk_SVdI1WT_A2mkhC1G7WBHCn_5OD7lwtaQIosftitlHSsfNzy6p0TPav4HORoXQFx1EuwN2oNQ716CnDflE57PbCTg98X7IVVnbJyZbSCPNHQB5KfMTjlul2YpuG_LjmXOWUCqtiJZ7xUF_Q5hfcqaxhW9ZNJAzpj8pU19rUcgfDM-HYlkGCkUTEG0o-tmWI6JY98XzLU9qvvQH9k3NuXEpzyd2cRZLaC8y92Yw8zfC9vpaoIxweCAdrDYp-myP6TN2nR7HjMKKxJZE4AOgx_sY2EFgLaMBlNbJvAiRvjWMnJArNaQvjuXu9TBCh-mte4K7nBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0d71bdc80.mp4?token=bQeqmVjTRk3NqnVKk_SVdI1WT_A2mkhC1G7WBHCn_5OD7lwtaQIosftitlHSsfNzy6p0TPav4HORoXQFx1EuwN2oNQ716CnDflE57PbCTg98X7IVVnbJyZbSCPNHQB5KfMTjlul2YpuG_LjmXOWUCqtiJZ7xUF_Q5hfcqaxhW9ZNJAzpj8pU19rUcgfDM-HYlkGCkUTEG0o-tmWI6JY98XzLU9qvvQH9k3NuXEpzyd2cRZLaC8y92Yw8zfC9vpaoIxweCAdrDYp-myP6TN2nR7HjMKKxJZE4AOgx_sY2EFgLaMBlNbJvAiRvjWMnJArNaQvjuXu9TBCh-mte4K7nBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
صحبت‌های بامزه دیبالا درباره مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/92307" target="_blank">📅 14:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92306">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/em1dIZctmEcOS5u2tqVkU15csq50Xdlq0ct8f6L5RmcanHBSoSjzgsIWQFyFNAx7zVWhQYANsydhdERXSeSzKWkl0C7NEssFAUXgFBwm5kTQ5cB2XFVBS9TXs0ob0hTz8TZc9P2yAHb4cK6NR4gAiVn-DuxQ8nKim3ilFfuyO1ZyxO-cDjEXO90spyRZ1dwzQ1PiKVov2VzA4Px1_DTP5dfzEkcg3sbPoDyTmuWouCjaenK7nPEsiOpbCRUDnT6sZWCK5klade4eD78hQfZvrkQeP8S7CXHZh9fuCuXfc_hbDDQKR6MzY56Xzc2wLYrJ2psLhwgVC2s3piTs-s7RUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار معروف کرواسی اعلام کرد به زودی با استایل جدید تو این جام جهانی هم میبینیدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/92306" target="_blank">📅 14:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92305">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_8EiGzWUt_ooy4lnCEHLNHrZqecA1_XyyYFMIwqCgWO0zg76SmdjkbuQL8K-t7a11Y-Tkv6WyB_PLTwxFcft_G9KHBU2riJGQBhRO5Is0iYTsQT1YNB4eyJdBRLdow9MLULro23yzXqZkRKRmMSQqF2cu7wv4czroYjlVn8-zZEvq5ADUtXGO_FfakQxiUK86K4JNCD9Nbh3OfDWO7ytvugeFbLlLxi28__ocNH1OKn9zdWjnJnFKM-nOM_yTtjdT7JwvBOiv_LxHJkvCcJboUGlRO3wTcBeWzmZHfvgMNHPYXVIVGYOmReC-P8jJD54x4nt_ToCezFz-aZyiLPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🇯🇵
🏆
اولیویا، یک طوطی پیشگو در پارک حیوانات ناسو در ژاپن، سه پیروزی برای ژاپن در مرحله گروهی جام جهانی پیش‌بینی کرد.
😁
این رویداد توجه بسیاری از بازدیدکنندگان را جلب کرد که برای دیدن پیش‌بینی‌های این پرنده مشهور به پارک آمدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/92305" target="_blank">📅 14:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92304">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
فوووووری؛ سخنگوی وزارت خارجه: متن توافق‌نامه ایران و آمریکا تقریباً نهایی شده و منتظر تایید نهایی نهادهای تصمیم‌گیر هستیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/92304" target="_blank">📅 14:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92303">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhjDZyU40-m2qn3wddHZ8AfHFaSj54pr5WxLjOzr0hgrPRsYoT0tVjdP-h1yMAmsdrJmsQZ3yyokKZ2dGDcuz6KbyLkPyuoxNsbNIgPkXMh9Zeg-FyQTfedFEOPyAcLqYKDA42tg19UKIH_aWmJDapHCX8mRRPZPMJcTcHnuHbCHpQrORv6OSGhlANvWUBaVd6lsXZeY0zkXMSt9wzl4q0u_o6dviMfi03DCWchynHcoQYRQjZvdnj4km1MPmIv9JbsmNLIDios8e46u2LYUB5UX_j0JijMwB5HHVfKDgzNjcFpGUtlihoVbSuXZH8wSC6NOUdTW5kAz_JmgD-bAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
🇫🇷
عثمان دمبله:
مسی حتی در سن ۳۸ سالگی هم متوقف کردنش سخته و با تمام اطمینان میگم، لیونل مسی میتونه دوباره جام جهانی رو فتح کنه
🔥
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/92303" target="_blank">📅 14:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92302">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
👀
🏆
رسانه‌های جهان مدعی شدند که دیشب تو مراسم افتتاحیه جام‌جهانی اصلا شکیرا نخونده و بدلش بوده که اومده رو استیج.
❌
این ویدیو هم تحلیلی هست و حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/92302" target="_blank">📅 14:03 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92301">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNh4fxX1oJtoXFRLtfRJLWWSeXKyVAoUqy4CL_BQmHwZfwOpJ99BZ6qfDV3jNJvsDzTMecWjksrRSjSCNuuYlKyho-3rTTJZZhKpV8HFMKFOi1lrmMBI2RLzF8jlYu6ucmOvgs4zt8B3z-71g7blcWNuGAHFaS41FWrdfrhlVZ_9lA6EA1OCgadquyLGd4kWscJRfdo-uPtXaCduR2pgx8PG97PtUR2NdqUwNxwYij8J6KIiDHWl5V5se9UJFZ1LUC4ouT-spjrjNpqruq_LO4bdWsAMnpLgYU9G7if_v9tL2MzVBeFMF_GTmA9beoBtBlOS0a3aEuQzmD5lfzl-PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🎙
🇪🇸
اشلوتلبرگ مدافع تیم‌ملی آلمان و تیم فوتبال دورتمند: رئال‌مادرید؟ بله خب یه سری موارد هست اما باید بگم توجه من تماما برای جام‌جهانی هست و سایر موارد به وقتش رخ میده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/Futball180TV/92301" target="_blank">📅 13:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92300">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOJx-JFnGohka4f28XsL5ybhv4IpsU0xoLL7LNuC_XvNMY-0rezWzXzFlBvN478Gyl19_0WbQCUPnV8NUlKvItdzQsRSAl3fcM9-sNGWifmKTDJJfZ_rFM4Vlkv4DcoH7D_gtkC9aaPrm_adzRVXH6Ff5miiZiu0YICxlJE6zIo-r2eOR0pXqw-EpdAI9zZcMpO5ql82E-bBukpV_5jyIsn1a3MOs-qlArn48_sBhzB4iW-tfwqUFlus99j845BsGvwNF09N9Hvui0QcZQmlx6tOXyEVMDhJLx1cOuLrc0lMifCBw34DW95u8JVz40M4rsYtwHSrNdNfjTNxk-kEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/Futball180TV/92300" target="_blank">📅 13:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92299">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMgbKmE4CgtIEoaF2RfS1PkmyLeZC5bsnoNU6UPdTDBVvFq6J7wYQwyZQOG7onW7Ga6MfTm-2ogvV-OvC6cyu1h-5FN_snrtZo6_eqOzLpVVksbaMKcUmoDzkWSp94y6jDTB9AjdW0Xdxkv6-Dx_mlrEDdT7l3zE3qIHhEr8tfHfcI2P1N4-pZHCB9LDgC0TPr0L_7wjuM9WCEmC6_lqslWrG6jT6NZcCBpdTVePf9JehhME6B5VFrqWjLF5-Fw-ivJD-zTghEBGvW04nc36g8WFu9YhGx7p_cBz7tPfDPzqMSBnN76C8JX2ludWkUIJ0g3E0kLu-9vORRjdceSGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
🇲🇽
🇿🇦
یورگن‌کلوپ راجب افتتاحیه جام‌جهانی: عن‌ترین بازی که میشد دید رو به نمایش گذاشتن‌. هر دو تیم فاجعه بودن و حیف وقتی که برا این بازی گذاشتم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/92299" target="_blank">📅 13:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92298">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9vfgOSuX2R0RbXv52SxR7ZP60OMxa6WF7Hgu92jfqcyUIeV4Oi8Sufyf6ax7qXTCj1XVvGsIPqdG1hE825VIClZXSSp-dxBT2WSejkOzbMY4Lz--TkMfxlzOGyEt1MKh4VgMebiriZzC2DbLkVe1Q7XvUqh1k6SaIxhfkmm386QQGLKR54eVBksDKC5o6Gy8KQVII63j8ZF6DzGUivMVkXhlIomGRFGMB095eudDdYzWKL8GVyd_iX-fP8yk8ZhL7QWSn_sVCbsobtc93NWQ6Bwa-VtsynyqfhX6_cW2O5zj2Dut1IxJU3-bJRg-DpquuAAwZOejvcLFK7WJQ0XJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
‌دومین جام اروپایی پاریسن ژرمن توی موزه این باشگاه قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/92298" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92297">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILjvP5lNbODd08FCQlPD1gmUyClZcWdNu-Zsqh6Wt2dAIiDU31bPszy85lw9L_ln1XJWCWYmOExTEp-4GUDYbsUDZUcdGQsa59ZQ5SB-BZkHRa59sAub_2lomuXo29NfU6OfWocI0CpOk8comTh7VY6xMXbH2e2zUQkMLxm17qhCERQ7BfQXGT7miR_poWeEfN-zSykYvSNRQqQLmup3TrMeaJfpv0QHddVwFfvGVxuRmGuuTguOHGMCoO4D9ioQtXxbqFv5AHqY0SEOvck08wk9_t1lR3UMtD7w3AfxagAWeC0owd-cyn-o_UiH0gkg3PzJZ7f_6rl7noMj5llFmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏آیا هنوز هم باخت در فینال قطر تو رو آزار میده؟
‏
🗣
دمبله:
نه، اما بدون شک ناامیدی بزرگی بود، با این حال، چهار سال از آن زمان گذشته، ‏خیلی چیزها در تیم ملی فرانسه تغییر کرده و فکر می‌کنم همین موضوع تا حدی درباره تیم ملی آرژانتین هم صدق میکنه. ‏البته آنچه اتفاق افتاد هنوز در ذهن ما حضور دارد، اما به ما انگیزه اضافی می‌دهد تا در این جام جهانی عملکرد بهتری ارائه دهیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/92297" target="_blank">📅 13:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92296">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5acf7f96.mp4?token=IhBnURwbyC0fxZbwjDC3pk-cXFTjjeJ4SB5JXfjSeRgKQhRFyL9ZLNMqjI5Vtfvs5sLD3MpqxMX3rTSdunHn6uw5AFM9M5asZ2CXN97cjTMXEsvYxRXjnvu8DMatSAvgRFo_cpS_A0JHZLRjdC9FyRRFjaXhF-147WIEZBQgbfTQn8yUv3LCYitQdjEL77KZ8BnIjSVk5Hca4-kr2tc_fwVdQTx0-jWBjn-M3KnwzPPhhv6xkR5LWGaj7sSv-peZHHEViEOrJEWT7fWCGrgYfsmlri41eDgyT8a7MIAtf3MDoYve0RLl0DfiMlz7q6s4OoEyAZT1NJL8HRjgO3c1qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5acf7f96.mp4?token=IhBnURwbyC0fxZbwjDC3pk-cXFTjjeJ4SB5JXfjSeRgKQhRFyL9ZLNMqjI5Vtfvs5sLD3MpqxMX3rTSdunHn6uw5AFM9M5asZ2CXN97cjTMXEsvYxRXjnvu8DMatSAvgRFo_cpS_A0JHZLRjdC9FyRRFjaXhF-147WIEZBQgbfTQn8yUv3LCYitQdjEL77KZ8BnIjSVk5Hca4-kr2tc_fwVdQTx0-jWBjn-M3KnwzPPhhv6xkR5LWGaj7sSv-peZHHEViEOrJEWT7fWCGrgYfsmlri41eDgyT8a7MIAtf3MDoYve0RLl0DfiMlz7q6s4OoEyAZT1NJL8HRjgO3c1qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🏆
🇰🇷
کره جنوبی هم‌ اولین بازیش رو برد تا هیونگ‌‌ میونگ-بو یه نفس راحت هم بکشه. این مدافع اسطوره‌ای در جام جهانی ۲۰۱۴ هم سرمربی تیم بود ولی حتی یک بازی رو هم نبرد، رنک فیفای کره رو به ۶۹ رسوند و خیلی زود اخراج شد. حالا با کلی حاشیه برگشته و فعلا تو اولین قدم چک رو ۲-۱ برد تا قدم بزرگی به سمت صعود از گروه برداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/Futball180TV/92296" target="_blank">📅 13:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92295">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duLz5Ci_jwuzEImadMyBUPzdUJlbS08IgIX2FQw09mZ9yCv03vShNn6QVKeX0ayarWRZdn3olMYMe83ee58xPoIE5Zwzc-DuC6wX5At-IUa2n96BPCt-vbA_175IPHMCASlxCFfFp58WlAM9vSm_EsyGh6Ps53Xie2iuJxT-QjNbarGzMN3Y85-dWjtzLk8M-x-Y06L1bOTt3l1tDpiDWtmFFbLhze_1P5vbBjRcw1a8ehGjjgokwx6emntHiTK8VnuoY_dIMsc861CMjWmUo0JFGykTBgyRXaJZdrqbrttnfYp0kX3J5Yb6UATEZrUywNtwRsPse0s_Y3cn-8mfUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توخل اجازه داد همسر و پارتنر های بازیکن های‌ انگلیس تو هتل کنارشون باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/Futball180TV/92295" target="_blank">📅 13:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92294">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5962002c79.mp4?token=WH_XvowpNR4orYBsldH1Z7uHaDkzKNvQaHRZsHGo-bY5qnCiQis9sqGdJscwscrgGrubjrcrqVYi_Lf3WDnf2dbShDNNddqCIC66UUFnZE6wTDc9Y9bfOss4Y4zOv79kjHeVHBe7JBoHy4WjulJfSOr-MRyblam76qCc5dqgEqbazivWqIo8vjYZusa2YAXCMjukQqQ6YDR4JffYNbF-uF8DTnpyEPNiS8uXbv6jnIC-iBfMacZGmMzpYfDLvrqz_Dmzdx3ymSo2j5RRdUnDBgOthUWHGqArdEXqOpEDSuM5Z6CST549iGUU4zy52CXFH0O1vSLH3HOgIOmFHcNFrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5962002c79.mp4?token=WH_XvowpNR4orYBsldH1Z7uHaDkzKNvQaHRZsHGo-bY5qnCiQis9sqGdJscwscrgGrubjrcrqVYi_Lf3WDnf2dbShDNNddqCIC66UUFnZE6wTDc9Y9bfOss4Y4zOv79kjHeVHBe7JBoHy4WjulJfSOr-MRyblam76qCc5dqgEqbazivWqIo8vjYZusa2YAXCMjukQqQ6YDR4JffYNbF-uF8DTnpyEPNiS8uXbv6jnIC-iBfMacZGmMzpYfDLvrqz_Dmzdx3ymSo2j5RRdUnDBgOthUWHGqArdEXqOpEDSuM5Z6CST549iGUU4zy52CXFH0O1vSLH3HOgIOmFHcNFrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خبرنگار کره‌ای در حین مصاحبه دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/Futball180TV/92294" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92293">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92293" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/92293" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92292">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=KWFaZT-hcRaEUlXXtyOqd0Xe6xgDgYAj2O7xOH3Ci_bAijMweHZ5ylcC6iK7R24B_AYYnsJX6n3BkhwS57xO-bkIgCQcLOf-MzGC5tzVI4dTISGoCc4yakmJF2Z_S-90d1Fo4Mv0dNH7K0kj2CHueoaH8m8NlCFiaBTG1EAn1mzVfsBOf-Bxr-CmsXG6esg0oSAmQRe6smlPZKMDHv8gW9jPfPXOxRsMDVNmrQh2oKP7vL6_30gmNdSg1eXTWlDSwXBHdSE9nzyFfkAIpy88kvsRXOKG_x1ZdhuHgeLCdDaAwQBJduLz2Fr3ehlSg_-yezj5J70ZLxN6bPkMgCK37KFNbtaIAxEzuKTVe1N5tk0m1-zbFRwzP88nlmeQxV2x8jBhzg6F32FjVeTv62mZw09urT3EwD5Zq5LxZWJiX7Tg4B92i8lnDZ9ixH5GoIAOm6EUs2BpFCnX5q1GJJ_JAG9ms65SyWeSxTc4cbQ8EOPTE47Q4_JLf4Pm0q8iFra2C2xuGFEHiDylmL3bsidoDSmgdIWVVqJRW1BfuF31dDKIhGcCaVMSX4e5YdbgRs8flO_fJ6NyBLlVTW4tEE7QDBUvlnYbczclRbK3C7SYrLYfJSoh9UAkW1AFcFQeHw2k9sSAccDmfh82FTsgtjsTK0bo1paQSh86Jox0A3955pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=KWFaZT-hcRaEUlXXtyOqd0Xe6xgDgYAj2O7xOH3Ci_bAijMweHZ5ylcC6iK7R24B_AYYnsJX6n3BkhwS57xO-bkIgCQcLOf-MzGC5tzVI4dTISGoCc4yakmJF2Z_S-90d1Fo4Mv0dNH7K0kj2CHueoaH8m8NlCFiaBTG1EAn1mzVfsBOf-Bxr-CmsXG6esg0oSAmQRe6smlPZKMDHv8gW9jPfPXOxRsMDVNmrQh2oKP7vL6_30gmNdSg1eXTWlDSwXBHdSE9nzyFfkAIpy88kvsRXOKG_x1ZdhuHgeLCdDaAwQBJduLz2Fr3ehlSg_-yezj5J70ZLxN6bPkMgCK37KFNbtaIAxEzuKTVe1N5tk0m1-zbFRwzP88nlmeQxV2x8jBhzg6F32FjVeTv62mZw09urT3EwD5Zq5LxZWJiX7Tg4B92i8lnDZ9ixH5GoIAOm6EUs2BpFCnX5q1GJJ_JAG9ms65SyWeSxTc4cbQ8EOPTE47Q4_JLf4Pm0q8iFra2C2xuGFEHiDylmL3bsidoDSmgdIWVVqJRW1BfuF31dDKIhGcCaVMSX4e5YdbgRs8flO_fJ6NyBLlVTW4tEE7QDBUvlnYbczclRbK3C7SYrLYfJSoh9UAkW1AFcFQeHw2k9sSAccDmfh82FTsgtjsTK0bo1paQSh86Jox0A3955pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/92292" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92291">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cy3lY_X92S2mdNWG_Zn0kwIK5_3sCaLfVdEw7jlXrWvJBF5hLOEpLIq7X2CG7gCKRrtp-uYzzXx6pDkngrMRyfxZsW4-8kMJNHMJvbM90ro6XssANPBJvddJwAT9Q4sYJOjYwOoMYLTWHpMKGFG79ggdSLuWGCvZ0VamlFRG3AY2m59FHSemiZNbcq5ke1ln5U3Szx62OuUH9aMgwvbb2H6-jyXuED673XHN9Vd2r0V7vKnwNAeWTBzdxsllq6O87JrkCgGxe8Q-4jvow1LonOPoNSCYNjpcOZFYFQSDKYq8CLGlAZj_ZVINyIgm4r0K4ghGQIRXOS409H6QyhSFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کیلیان امباپه در جام‌جهانی
:
14 بازی
12گل زده
3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/92291" target="_blank">📅 12:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92290">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c18ef9a2.mp4?token=Cfa8bCpL8YjcjWAJULuld-PNQG4pmK_5lTesaDKPJN2wLKjPtyhRfgfi9Fv4NytF5HE-IGTSHHA_67uTgT1dflFnh9y3WSiyNVQ4ZVFQhFTvlTGgCZNGRb8ad108z_76w-h-11VQ-edig3uczWFGXAGX43g8haVHeOtqEYhS9MtDKNNAiRKe2Tr2ZnKgzkBsEVt4rPIHz5iInfLpqxyl88XJUakrNjgtXhL81TAVSlsOCKgX9VLjJfNBOJs0gv41s48JX5YFs99-r9ASkUnOwUdTsEM0-6LPZfJdbMEJLRqrtFBVl9k9R67qQQUhmH-xm3p_hvdpnPG58TMSqLbdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c18ef9a2.mp4?token=Cfa8bCpL8YjcjWAJULuld-PNQG4pmK_5lTesaDKPJN2wLKjPtyhRfgfi9Fv4NytF5HE-IGTSHHA_67uTgT1dflFnh9y3WSiyNVQ4ZVFQhFTvlTGgCZNGRb8ad108z_76w-h-11VQ-edig3uczWFGXAGX43g8haVHeOtqEYhS9MtDKNNAiRKe2Tr2ZnKgzkBsEVt4rPIHz5iInfLpqxyl88XJUakrNjgtXhL81TAVSlsOCKgX9VLjJfNBOJs0gv41s48JX5YFs99-r9ASkUnOwUdTsEM0-6LPZfJdbMEJLRqrtFBVl9k9R67qQQUhmH-xm3p_hvdpnPG58TMSqLbdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب بعد بازی افتتاحیه جام جهانی، یه ویژه برنامه تو کشور آفریقای جنوبی برگزار شد که کارشناس‌هاشون در واکنش به بازی ضعیف تیم‌ملی کشورشون سکوت کردن و چیزی نگفتن؛ خوراکِ میمه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/92290" target="_blank">📅 12:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92289">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4813f4b6ed.mp4?token=uYXYN97XXa-uxEvmqMiQ2nFnoSIY4D-TiZ4y8wIGTLRgGu9csFDcS2qN0JG_qyyAnAHlm2xAktPww0ZTHL0yXQMqJrhia_vu19dvaGmIa4LLcB0pyoQBJhJ1kEd6o3O4A-Lt6KmLRst2HGzTmgYrhXh5rFu7Fq3Dntc0mitdxZ9rDxGZb0XFv9IpuX-dWVpBJNDYeJU-kXH7xGWa0BMr8pD2c6nrQwZK9_KAIf-NZE_ab7EFs4tjgGzCfeWxcgcvGsylExxNxcQmMnWS5bx255MiNWUXeY3FM3PqNyivi8kWaPtlEnXcOlCLjwxS-k6suK3K7tBgzFhEv_lxhUxr947H6hL0eRklEk9WPwIZaQw7Wdae-Tiu8xgBqlBK2C5weXQNY2s3FaO4MPH4rkN8W7Wgg9FzZ1MZ_O4-wLKPYGXYx1mN_Ca5Qg0s88ljIhWNDDlylikp1Z1SfXjIsD5RmjriISoVD0fQhHwxSAXUN1vR1UeD2LOr2YxxAObE5PHDtENnlIfvbNBzFQfLDsayqg0VdrkYVWuY4nFxeJ0ouj2BjkmO3jj25Og6BIJ9azT_OFrExYCuM7_vWhDhz1wm9ZPf3LL9XIlUDobiZTbqTUj1enimQdDEL7rqJwKtlofEyyMiAMcxivCedPLQaKZZ-sRNImOoCIXttybw64dYec8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4813f4b6ed.mp4?token=uYXYN97XXa-uxEvmqMiQ2nFnoSIY4D-TiZ4y8wIGTLRgGu9csFDcS2qN0JG_qyyAnAHlm2xAktPww0ZTHL0yXQMqJrhia_vu19dvaGmIa4LLcB0pyoQBJhJ1kEd6o3O4A-Lt6KmLRst2HGzTmgYrhXh5rFu7Fq3Dntc0mitdxZ9rDxGZb0XFv9IpuX-dWVpBJNDYeJU-kXH7xGWa0BMr8pD2c6nrQwZK9_KAIf-NZE_ab7EFs4tjgGzCfeWxcgcvGsylExxNxcQmMnWS5bx255MiNWUXeY3FM3PqNyivi8kWaPtlEnXcOlCLjwxS-k6suK3K7tBgzFhEv_lxhUxr947H6hL0eRklEk9WPwIZaQw7Wdae-Tiu8xgBqlBK2C5weXQNY2s3FaO4MPH4rkN8W7Wgg9FzZ1MZ_O4-wLKPYGXYx1mN_Ca5Qg0s88ljIhWNDDlylikp1Z1SfXjIsD5RmjriISoVD0fQhHwxSAXUN1vR1UeD2LOr2YxxAObE5PHDtENnlIfvbNBzFQfLDsayqg0VdrkYVWuY4nFxeJ0ouj2BjkmO3jj25Og6BIJ9azT_OFrExYCuM7_vWhDhz1wm9ZPf3LL9XIlUDobiZTbqTUj1enimQdDEL7rqJwKtlofEyyMiAMcxivCedPLQaKZZ-sRNImOoCIXttybw64dYec8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای بازداشت شیث رضایی از زبان نیکبخت واحدی بدلیل شوخی خرکی وحشتناک حین پرواز!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/92289" target="_blank">📅 12:40 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92288">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOfL_J0pLWcvJapAdvuK9oIG4ljBb3QrsrSfDuzqVO7G8SsthYNPvvft1wRjHBGNGBCt70_qGM62woKyepgIfS4otIIheszJj5awto26Ln5r69BcSiMERbyIClgH_fXRW6DU3jNc5pXkgfCHBf1X0CCPHIz9KE6UzPNlJj-zrPyX3525AYLrF-s5Xa-mWRN7m5RClxi9P6ka419pjGTfinwtMvH5I5yz5a06O_0L9d8uDa2uWGkq-pmm8QAwoyc7AimYUY-xnaBUchd_qPzihQXJXuZUpG8pkBW2Cg7kBE4FixVr_XEyNv0q4_KMmJXwmP0PHU5YpjY26hSvCnI5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یواخیم لو:
- من طرفدار این نسخه از جام جهانی نیستم. همیشه گفته‌ام که فکر می‌کنم سیستم ۳۲ تیمی خوب بود.»
- با تمام احترامی که برای کشورهای کوچک که گاهی اوقات می‌خواهند در جام جهانی شرکت کنند قائل هستم، اما به نظر من کمی زیاده‌روی است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/92288" target="_blank">📅 12:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92287">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urBiWR07LzoAQWiXnI58rcTzRFB6W0OPdLFnk4NWxGpqPGfryRGHNVmxyDjwUQZGHKPEoHuUNyiu_FuOP-9o2S3wuPM1Jpjim8krkrvTXdlgzF8gJErYsaLyOXsjWiTFi5PB8p2X9B2xr2jDpqNHFzMIfRJHGUbwYkogr0axh8h19muyNzPMGQZKOndB9Y81o7LBa8fJPWTQV7h3dULsjAel4FvhtZbDomm83VlezsZ3IGbfwBmD3VZJKExImDh_-ku0UJd4UNQP0B00i0s-Egu5VgxGM2JXZ3suvKtV3ZYhCACLscEQzN8rJH8mTNDsfbQLJf5mINAT8Q5OlWNx1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پیش‌بینی‌های استیون جرارد برای جام جهانی ۲۰۲۶:
⚽️
آقای گل جام جهانی؟ «آلوارز»
🧤
دستکش طلایی؟ «مارتینز»
🎖
بهترین بازیکن مسابقات؟ «مسی»
🏅
بهترین بازیکن جوان؟ «یامال»
⚽️
تیمی که همه را شگفت‌زده خواهد کرد؟ «اروگوئه»
🏆
قهرمان جام جهانی؟ «فرانسه»
🥇
چه کسی توپ طلایی را خواهد برد؟ «هری کین، امیدوارم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/92287" target="_blank">📅 12:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92286">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MunCw85mvj3TV1Sl8nSdpBLcw13FzH6DwpqUyMGdDOG3fjs1m7lMWqu5MD-eDx9C7x73mft2rdII8yfAxTV4iJzABm7MsoBDhrdZ45kY8g0FLCDfBOt8PSZanBCmi65oDMGEAnIrsogOawZ-53-Lt-f9dTpQBjVRMBXPmATKWg7lBLf6geV6Hm9kccxJSvMfa3q88NKoZltJwwvgW8wYaY2LOiPp34d-6raD4GIlxCahGLKU7TFye98FP5wooCou-p5rU3644EBK0nF0q0Bz4DIVcTHppop1b0carjec3uwYGFDx3ZGTIBhsZLYbVErvQOzjHuoNI7-CBGHMogPQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووووری
پس از موفقیت مراسم افتتاحیه جام جهانی ۲۰۲۶، فیفا در حال بررسی تکرار همین ایده در تمامی مسابقات آینده جام‌جهانی است!!!
برنامه احتمالی فیفا شامل برگزاری مراسم افتتاحیه‌ای به مدت ۹۰ دقیقه با حضور تعدادی از هنرمندان و نمایش سرگرم‌کننده پیش از شروع بازی‌ها است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/92286" target="_blank">📅 12:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92285">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTs-a-f0h08MXD4zOD4q40g_LqXZDe958RKo55wzyqmmN12vtfkj_s1t2qBoy8aJF-tBLyCWK4Kk-1DTu1qRf5u09UdWaJr_1EKcO9iV_5Ik1_L9ubwASpXAm_X0fC9TnVheJhak0rh9CjXmCPbL_nUcR3-YLVNrXNWHddAyf0Qcu624lzxlKWuWdyGBAaPL8Vbv1TqmU3WilhagJmFPfwVs3gWM7YxMBb_LVDSN8d_MumvQdJIUp42PvL6-D9U_VPYZ2sOv_GUAdkrTkB8q6BVTZS_f_nZPQWg2kw1nt75UBy1AcItrfuW7TlIP-17niIAbOHItNSiiKTJ4nAVY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
عثمان دمبله [
🇫🇷
]:
‏«من از کودکی ارتباط قوی با باشگاه بارسلونا داشتم اما با توجه به آنچه در چند سال گذشته تجربه کرده‌ام، فکر می‌کنم تصمیم درستی برای ترک آن گرفته‌ام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/92285" target="_blank">📅 12:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40bfdb027a.mp4?token=eA3ZdvNVGrxNVkJa-kckTet-j1sXFcOWvcVxLCOHv-8qsC5K7n-4Nk9voqeYsRZW2qM1WTcTwbOMYiBujU9XQEACjuUXiMjIyhpdyG9QgTjZsb5W9ACXEN-4sJq3JVQz9Vj31xee-tO-2sJBHhqMM_LtU0aUMZTCjdxgvJplQJtihMNAjGLlonkbM2zU_1nLhXqay2xblVaPWsMXyHdCrHM-AbidRD6gPUVsmhuis09h3B6cjIoCYbFiy2JVJyWYKc-EQZ5oOCg7ZQVhg7elDqsr1s8kj0lP3vqLA--GwehirXvBQmip2To8rEZ8oVRYsi7e3Uk5JMIAKpgkKsTClQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40bfdb027a.mp4?token=eA3ZdvNVGrxNVkJa-kckTet-j1sXFcOWvcVxLCOHv-8qsC5K7n-4Nk9voqeYsRZW2qM1WTcTwbOMYiBujU9XQEACjuUXiMjIyhpdyG9QgTjZsb5W9ACXEN-4sJq3JVQz9Vj31xee-tO-2sJBHhqMM_LtU0aUMZTCjdxgvJplQJtihMNAjGLlonkbM2zU_1nLhXqay2xblVaPWsMXyHdCrHM-AbidRD6gPUVsmhuis09h3B6cjIoCYbFiy2JVJyWYKc-EQZ5oOCg7ZQVhg7elDqsr1s8kj0lP3vqLA--GwehirXvBQmip2To8rEZ8oVRYsi7e3Uk5JMIAKpgkKsTClQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇨🇿
🇰🇷
هایلایت بازی جمهوری‌چک و کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/92284" target="_blank">📅 12:06 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92283">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ae4e3b947.mp4?token=ht1rSlLSctYNuYculsJGJHLd8ZR8gHKfQoYK_PKzf8_3xwg42L3bp4I_qMsVCtY2fbUKgDV5KKA6L1Lps5LsQEkmCd4t20vx1iXb6X0dlfRP6hfuWf6uXUCCZTB_Vh9QDHWdVIfGWaDriDjPzCG0n8tbfVdSFOYR9Z7GLjctypU46rklZ1nkkDGVMILpwNOA4ykKEDNTHNDp4wKnnACZMx-rCp0zdsriERVOM8lPt3c9JdVTgoTTKCtLs17lwukCnPVZY2y5NUYJgdbp4wkVdNZNxReJDPBQcdCKYSWZyPc6qJ_QCyeN9zY8bCUVJTW9bf0Ma-RqINx71FqFoojvjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ae4e3b947.mp4?token=ht1rSlLSctYNuYculsJGJHLd8ZR8gHKfQoYK_PKzf8_3xwg42L3bp4I_qMsVCtY2fbUKgDV5KKA6L1Lps5LsQEkmCd4t20vx1iXb6X0dlfRP6hfuWf6uXUCCZTB_Vh9QDHWdVIfGWaDriDjPzCG0n8tbfVdSFOYR9Z7GLjctypU46rklZ1nkkDGVMILpwNOA4ykKEDNTHNDp4wKnnACZMx-rCp0zdsriERVOM8lPt3c9JdVTgoTTKCtLs17lwukCnPVZY2y5NUYJgdbp4wkVdNZNxReJDPBQcdCKYSWZyPc6qJ_QCyeN9zY8bCUVJTW9bf0Ma-RqINx71FqFoojvjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
زمین‌خوردن عجیب فرد حمل‌کننده پرچم آفریقای جنوبی در مراسم‌افتتاحیه دیشب
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/92283" target="_blank">📅 11:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxfOsQ0fehSwu8Hv9GQIKKTpKev3xSdXIuakTPs5iu0TNO-wj7A9Gpwsyy6vhE5h25T-KBr7xO_tEqidoxflUs4RxL6IYWKIYJUEAaJYUojJ9Na212Z103YBJvA2BHQLgLPtb6fYw510SmY8KUHrDlfahovtB2dbdfjPy-ERrVzlZ_QAsWzWN9ywNIfXw5EvpoCHfozhM5SWkqvX5TFOI3LbZE-nFdUIz-s3ACyTw9xMWiuaI9obzMt5VewiifWU2QuwkhpVFmW2GQ-WoGZNmgJBStBLKBrar5hecarys-KBQq0sOptat91GZ8RtItRB5kEh2Iu3li-9CgB3DqZONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
فدراسیون‌فوتبال نروژ: بدلیل اینکه ممکنه شرایط غذایی آمریکا به بازیکنان ما سازگار نباشه، با خودمون
۳۰۰ کیلو ماهی، ۶۰۰۰ پرتقال، ۱۱۶ کیلو پنیر و همچنین سه تا از بهترین سرآشپزهای کشور
رو‌ برای تامین غذای اعضای تیم به ایالات متحده برده‌ایم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/92281" target="_blank">📅 11:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhoK4kKNciPGfmU71aEo1CH9uiXrT8mxFSNcMNH9ukKa0zzKk0_uLWvenoXvjotz8mgmfSXZoXWzntioxyBgcCoX18_4IVuKzFLxNKeRaofC285IQ9FVly31QZTjHHZraK2IHW4hcHk0Q-bXIZnMb_rIIQPiIEI4eO6KsWHHoL2yHn2JW6fHjRja5foBNQDUA2Vd9PHawIXhOfTBYKxkVZXYuPPPyMvVX_hDGs6X40CjpVi_BeFXMkypHoxrG94VhoZjI4PCuZ4ObtMSPDwNntkAKzF1DgGoig9NuazbrPVXU-pIsPt2dcjcfY5W9yjhgp8LHtDMvUiOMdEmK1Zqwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🎙
🇪🇸
کوکوریا مدافع‌تیم‌ملی اسپانیا: اگه قهرمان جام‌جهانی بشیم، عکس دلافوئنته سرمربی تیم رو روی بدنم تتو میکنم
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/92280" target="_blank">📅 11:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39aa059d6.mp4?token=U5MVvNxc5Mdq1q4XbgzpRBtC0FbgLcpnXmTSUmb4Yon6HUeifvr0V0ORRpSVCUuh2HyfLaY4bj7gmJOmUVDX1j2A8CT06kr8wU3I3lpb8kkTNFTu7ymhiUVFaqpoHnfvdVQX-4qPewQT-pJXRae5xlqYrRVUGZNrN2uAR4FQ4pz7e8jNhqrR20DAdZYrEGsBRFKPQnMBuGCNvzbGl6lqK7FZ6yzkIyRqU7mLib8dcr5keF7PS5G9jDCpkUk1hcZndKdU4QhNLDfIrkTTRiulFVwW6hgMUmzfXfo7mhWYcZJ0MWL7qNZHgx1UAF15C-uJO8Cr7PTA270EBt6j9dwpGkeloB-GuyJiAZYgX5ka7lldtPtFp-90Ox54x3CslvCQtGXwgPRVrz1Gj8uVYgxEJdmdQ8Vvw3zwnrrBp_Pk4gtCGU_F7z1X8PUSLUIW3sjcZM-GwT4oug__AfxFFoq6H4JZYJSe49Ot5-F4ne_o2400xZL3CbgfffXXUtH5JfJVxFr91m4qbfQ695p8Q7NNKB4z_qQDwUJA4Cr1_GZr6PumsWiyikiPd5fQq4Vov4NvDND3lI8Eitl1GMtslhTZlYpeMmVdh74r_ytd7XJ17wCKFYJVjz57TDDuHIFo3tslgZzLsN-59w3cxJuhYzrbnyLj2pDqLRv6temWkpRxOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39aa059d6.mp4?token=U5MVvNxc5Mdq1q4XbgzpRBtC0FbgLcpnXmTSUmb4Yon6HUeifvr0V0ORRpSVCUuh2HyfLaY4bj7gmJOmUVDX1j2A8CT06kr8wU3I3lpb8kkTNFTu7ymhiUVFaqpoHnfvdVQX-4qPewQT-pJXRae5xlqYrRVUGZNrN2uAR4FQ4pz7e8jNhqrR20DAdZYrEGsBRFKPQnMBuGCNvzbGl6lqK7FZ6yzkIyRqU7mLib8dcr5keF7PS5G9jDCpkUk1hcZndKdU4QhNLDfIrkTTRiulFVwW6hgMUmzfXfo7mhWYcZJ0MWL7qNZHgx1UAF15C-uJO8Cr7PTA270EBt6j9dwpGkeloB-GuyJiAZYgX5ka7lldtPtFp-90Ox54x3CslvCQtGXwgPRVrz1Gj8uVYgxEJdmdQ8Vvw3zwnrrBp_Pk4gtCGU_F7z1X8PUSLUIW3sjcZM-GwT4oug__AfxFFoq6H4JZYJSe49Ot5-F4ne_o2400xZL3CbgfffXXUtH5JfJVxFr91m4qbfQ695p8Q7NNKB4z_qQDwUJA4Cr1_GZr6PumsWiyikiPd5fQq4Vov4NvDND3lI8Eitl1GMtslhTZlYpeMmVdh74r_ytd7XJ17wCKFYJVjz57TDDuHIFo3tslgZzLsN-59w3cxJuhYzrbnyLj2pDqLRv6temWkpRxOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🙂
💥
نظرات فوق‌العاده هوادار معروف پرسپولیس نسبت به بازیکنان تیم‌ملی قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/92279" target="_blank">📅 11:20 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
