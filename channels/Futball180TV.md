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
<img src="https://cdn5.telesco.pe/file/CH1tcVEJret5meoBP-vGYlqORPKg7tV7eRGo4e48DFhlV0SOS_OnuaK7y2Ji0TzslvxCtA3Z8mJodGOXqxai-QQhqhq64yDrvvZ2-BdMZKaieE4xDT1-fc67mOiEIdV_D5EH3ngQoaZJVGJ2xb178UfSmNLGRoS57E7nkF_gu_fXLWQOdDrASiiieC6wSZsNlSMxMqfoC8zNSR2fz-EkO5C25D1UeCWwI-sG0X71vUCgFDCkTc07C9MYKF2KGgFtywwZLzrrZCxNNbxStRMHeJAZro_MqhFrsifixFO09fAcSUnsnB39xPdooZzbXcblnLD1-A5WfCYb826UTzyVBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 245K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 19:37:35</div>
<hr>

<div class="tg-post" id="msg-91336">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa8f6077e.mp4?token=Q07-QwJ4YBVQ4SEAKUNn-x_DjFOIyFoc5fwjWoArP3bHsEBsacE7If0mCC1xolSDPbkqKPL5t8ytTKh6bxQWJrYEIY4liGb_ZZED-Kvjcp0wwncDBIip9LHjQ_utlDvBU2Tnegdw5W4S4gahEW7rWRuJZROKc5DqrgnoFPuZsEW9RD7MWrYQ3sP_81WRYZgPBQWhW6_hV5-iK35vgCZK9AiGHOzWvjdUv0zJ8zUDmnChb4_ByI9YbVYABcwLsegODnXpNTbAW7dI7zmbPZSrOIbyg87xjqH5CZXbNDe8AHXVE_P7y2d3ly9FBz_ULqPVO9JUPlwtVa4eAOSLPtQt9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa8f6077e.mp4?token=Q07-QwJ4YBVQ4SEAKUNn-x_DjFOIyFoc5fwjWoArP3bHsEBsacE7If0mCC1xolSDPbkqKPL5t8ytTKh6bxQWJrYEIY4liGb_ZZED-Kvjcp0wwncDBIip9LHjQ_utlDvBU2Tnegdw5W4S4gahEW7rWRuJZROKc5DqrgnoFPuZsEW9RD7MWrYQ3sP_81WRYZgPBQWhW6_hV5-iK35vgCZK9AiGHOzWvjdUv0zJ8zUDmnChb4_ByI9YbVYABcwLsegODnXpNTbAW7dI7zmbPZSrOIbyg87xjqH5CZXbNDe8AHXVE_P7y2d3ly9FBz_ULqPVO9JUPlwtVa4eAOSLPtQt9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانو زهرا گونش ستاره درخشان والیبال ترکیه
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 308 · <a href="https://t.me/Futball180TV/91336" target="_blank">📅 19:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91334">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1Pp_IbR7xza-FAeZ2N1ri3isokiW5Klo8YcGrhgnnmW8z7nMuu4f3fm7A4ABrdV3rYDREZEmOCZPiaSfeYoIu2CuPDpfQ-NjhRll4eIOXB2idh8sSnCDXLZPqc08mxBbQPKMyTcCQOWmSnHMJGO_FtzqcUmYedj3TAdeu1EjLinm2uTe3RsDssYhjUZNlb7hnTuu6I0zoeP-ckrS-Tq3VuBXpeFRGqTmKtcYAfV4h-dj-8EtVu6NnHYymV2tBKVvXkrK4anril5spgUkCzZanZ1HMh4nigXsCNomaPxHvJB-85vj9K0GenYVDyWSifaOPlFXLhIu4AXfGhuh_0OFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZ0P1_-KHfjaRXXHXIGPQUs-rAgrHbnMVg7Hr-mf1JMuVXrEL6Py41i_j0LBvrJfWc0pgUQmXerPYu4YMIccl0Bokn3flMMvwismJw-uBrPcfvWaVIlypXYVnkfncSuZZnQSyG83UpXwVcLwFpbYkE0BpDRXrtWey0NySm55WDaORw_GdhXLPcSRvP42twd3dVkVbhGnUUtDdz4r-RhYjTHqjKEKTZ6GpPvDSr4MKz9Axa9R2ULp0V1h8j7dID6nNozwH1gMA8JCwEkygfIeRqKzP_n7tPhjbdLbe-31DYEcwgJpRz7VqVRKOr6AVMPJHFiedf1RoONImj--LH-qg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حتی یک درصد هم نیازی به تست DNA نیست...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/91334" target="_blank">📅 19:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91333">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6ddb8bf2.mp4?token=Tu11dcLz6wAL5arkzC-GFvrGUS5m7qfm5dWds9WZcNDq0qupx8Ja22puCmxiSHsH2O_SiwYrMuwibF-wSp6bT8cqXnSAC1Efo1HokR6otPtg04FtjtiONYkhQgGdSfPSOKQpiI77xCwAVNr23nwxrV1tFUR0xTjV6t9FKhbBBT7WCsC0nLB-14gw8RI2vq2KDRsNEAWp_yz6lVmTlzWnHDnmO4qlwzLLiVwi4skOH_FrWqpsX-321hwigQsSaNiCRFwUqXhTq6T1ezDOBNLE8YVApu8GCJnrPyW-EBDYcmKuZI7qbFzx7uXMPkaAEcEdxghgvUI7jIPmYpbRCRe77A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6ddb8bf2.mp4?token=Tu11dcLz6wAL5arkzC-GFvrGUS5m7qfm5dWds9WZcNDq0qupx8Ja22puCmxiSHsH2O_SiwYrMuwibF-wSp6bT8cqXnSAC1Efo1HokR6otPtg04FtjtiONYkhQgGdSfPSOKQpiI77xCwAVNr23nwxrV1tFUR0xTjV6t9FKhbBBT7WCsC0nLB-14gw8RI2vq2KDRsNEAWp_yz6lVmTlzWnHDnmO4qlwzLLiVwi4skOH_FrWqpsX-321hwigQsSaNiCRFwUqXhTq6T1ezDOBNLE8YVApu8GCJnrPyW-EBDYcmKuZI7qbFzx7uXMPkaAEcEdxghgvUI7jIPmYpbRCRe77A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیروس دین محمدی: در یک بازی وقتی گل زدم، پدرم در استادیوم بود و از شدت خوشحالی سکته کرد و فوت شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/91333" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91332">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmOIVaDQ3wS9K_E87F2tsXrXVjS-zaFllg4riy3tksx7-ms1yf3qDZXpqOJj7OA_dFvkath1xjD_sr19ciLjuKBB4XIDn_n1CzX26MojsaOWQT0Z76GBOFnhFdTwbCYxPRcL3Tpo8y28N06tcB6mzIj613d4SZb9M8Ib_zv4KWqt3z61Axqq-xjfPRYQh9cKCiEjlSBSOqdfm9qfNBdgGYc3gSygO7ruk3w0pcJ46qJ47f1-B353TFpqTbqpHFTu0_Tf-Bt4-6BjzjwIP6eBHfkPSafN82RF4-_wh77rnuofMkSY8EIVHAuXdKwekhF6KBay7LUwHa76C05bBTQrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال:
اگه جام جهانیو ببریم، به مدت 3 هفته ریش و سبیلمو نمیزنم و میذارم‌‌ رشد کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/91332" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91331">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwCKw0GjP-bXzChqKNg6CfVI_6KBwncVSW4hawYWC6eNZReMVIQpBoBsHB7IgZf-05gz-g2fHskQfphwmBXA-dP1-dtsKYhcwLTALZbmH2qh2XdlfFtWRFu4MneewUPK9Z580JJlOtMZtxDHfGRtjSqJYPv1vSOHYQtSfyW9yqbOHi4CdyIgCDp-L4BH7w48M6gxHqhJvycfaqBj80MhPuteJjYK2nCQiMsPTTCF7u-j9KTGYsWStKn8nntT5um9F9qtAphGKXjCkPNMreVjnaIpPfohKYdNFpeQ5ZYtMmclJSEfKjng00SLYKIREgm8XzmjQz_B63o-lPfSzsFW9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش کنید دوستان ورزش
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/91331" target="_blank">📅 19:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91330">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67083b7bc8.mp4?token=JTEqDzVU45hsuGEKRJSnmNkX00DU97jsmBUDklnPgJYxyUBv1T9PUqQBWXqNPrjZTULPwgSLvq_bGmQiULmwIF21avKjL_pCqRxctvA6lah3mFUZHREuJYUzOMvV5-l_uqNDtsO_brJ48RDf-g_7j41krKP-Xg7yyKmOwd0AqTZ4J3wkNPiIDSWQNcMOUxEabIbsVVWHUW4DAK5PAw1etu0lemcJziykERE-d1hd-Y21z6poFtxueDCIU-WFlrAwiEZJ-MtT_pV2QGoUtiKz4Ohk8JxpakqBOGZPbuiwkNcB0K_XPr3w_9SgEHCVIGk4PE3koL7-zKURZN2buNH9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67083b7bc8.mp4?token=JTEqDzVU45hsuGEKRJSnmNkX00DU97jsmBUDklnPgJYxyUBv1T9PUqQBWXqNPrjZTULPwgSLvq_bGmQiULmwIF21avKjL_pCqRxctvA6lah3mFUZHREuJYUzOMvV5-l_uqNDtsO_brJ48RDf-g_7j41krKP-Xg7yyKmOwd0AqTZ4J3wkNPiIDSWQNcMOUxEabIbsVVWHUW4DAK5PAw1etu0lemcJziykERE-d1hd-Y21z6poFtxueDCIU-WFlrAwiEZJ-MtT_pV2QGoUtiKz4Ohk8JxpakqBOGZPbuiwkNcB0K_XPr3w_9SgEHCVIGk4PE3koL7-zKURZN2buNH9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
از ایرانی‌های خوب هوادار ازبکستان‌
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/91330" target="_blank">📅 19:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91329">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxrWp2E9ixTOvPIG3Qyc9XjZ3Jv142ZXn3s-OKE8YMDNtWdKftmUv_kDyMbk0ib3r_J4UGRWPvsQuYufznFfFIEkZ76iIthHwUTMpD9ntkqvFbZcoqFlM9XPRBLHINhEbzOwbxJ3BMK7mW8nDTv5aj9UXxlm26Nn9p4xC-Q8Xofz_mDRc46wLz93J_le7TdrOk2589LaTneLKi_NY_TK9f0TqifxkUketlcXuuNl9nSRUh8npdVFhD1ckgX_X3HA6zmLr1xiBepNQsvE9OiNgvqvKjGDKNGEjBnZmXK2tZhDJvSE7EcFgqwkapPq2-3GZ8Vcqf8WHZa22P4D-4Mykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال درباره توپ طلایی که دمبله برد: راستش، اون روز فکر میکردم قراره من توپ طلا رو ببرم، اینکه دمبله هم برد باعث خوشحالیم شد، من با اون خیلی خوب کنار میام و میدونم که هنوز زمانش نرسیده بود که به توپ طلا برسم، اما مطمئنم یک روزی که پخته تر شدم به این جایزه…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/91329" target="_blank">📅 19:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91328">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcYynsUpjzSPr7OTAuxaCytJ1TpP_zcOtg6X48qawEGc_GiGAXVljRu600kyEwnysVqLECLu8MsWhuvZ08j84WUVQeah0WUF-LxmwRdqPxDRyYqOALdSJlmEqVDYxknPDv5VZLCYfRYHrsz1CJW7gJcFsXG2rFGNWTFaUkiDlO1GHTuiAWhVwBQjE5kY6Qu0WYWnlRpbQYgii6PH-thnD72Pe935SNqn2xM0wGoVAoWPhDmfGgu87Fyuha7mAlgIRx5d6OolyD62SD9mLDYFYmRIf7iQLbEsfFjwx49oDKPcw7NMSWFJ8AMdnMsuPUTQh087lKyDUcrLF9eBiUruTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال درباره توپ طلایی که دمبله برد:
راستش، اون روز فکر میکردم قراره من توپ طلا رو ببرم، اینکه دمبله هم برد باعث خوشحالیم شد، من با اون خیلی خوب کنار میام و میدونم که هنوز زمانش نرسیده بود که به توپ طلا برسم، اما مطمئنم یک روزی که پخته تر شدم به این جایزه میرسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/Futball180TV/91328" target="_blank">📅 18:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91327">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02ef042a5.mp4?token=Oz7dn0EY5DwNwKgOuA-yuw6CL4Kmxowh7hx6FaVfM-gsatfLr-_s_UPcgHYLcIUgnSLJ0Y3SDELIJQxZfZqOsJH8PlShRttq69ns50zCYD2asv7c-qq91MssTqB3ElnJOBlOwO5jeokw-wBN-lcA8Q5klilINBe8l79Wu2NTcWYu38VBHPX9uOeTDJrV0v3_Rnd2kVhHQwJwkS055gEu_4ueINJGbk2G1C0oqiOMcECDA-DM8HF7bY44xeG4BNmSH2713rS3oC_saobyoF6Cx-1dOWZMT5MTK7Bo4Nl3zfZOJ-rW-oKKhxsPao8IuU0Ymg1BiL9WM0IGKQLwKgx0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02ef042a5.mp4?token=Oz7dn0EY5DwNwKgOuA-yuw6CL4Kmxowh7hx6FaVfM-gsatfLr-_s_UPcgHYLcIUgnSLJ0Y3SDELIJQxZfZqOsJH8PlShRttq69ns50zCYD2asv7c-qq91MssTqB3ElnJOBlOwO5jeokw-wBN-lcA8Q5klilINBe8l79Wu2NTcWYu38VBHPX9uOeTDJrV0v3_Rnd2kVhHQwJwkS055gEu_4ueINJGbk2G1C0oqiOMcECDA-DM8HF7bY44xeG4BNmSH2713rS3oC_saobyoF6Cx-1dOWZMT5MTK7Bo4Nl3zfZOJ-rW-oKKhxsPao8IuU0Ymg1BiL9WM0IGKQLwKgx0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تنها باری که عمیقا از ریاضی خوشم اومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/Futball180TV/91327" target="_blank">📅 18:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91326">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb7nuldKCxZQwPjYRFxrtJ1LeyF1A2vzyobVMRWPXGAJG__mjBmaj9dGAnnYyss7nEebMCXo5SYJBgMhwnSpjp5CNnj1uifa9xK4I9H_dE-v--ZxgMbBImALiNAfEhuyKtgnD9Xa9FieEHWrIuFHp2B95u_FVFPjiDUpGGiNHI8fq2GlrScyVqGdsGV5XkfLlpIEUkywTM2Nm5gnnLDz6-x4OquaTDnwwVDkIrqyzysgbx-smwjSqIevkwHIOwDeryOGy4aya0G8wVua5ex8U1NtuTEnWBp1C89-49eG3HwNCWLw-qzeEyroBuhEvRv8EGWVRd63Lvv5SmU2idzq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیسیا سر آب و هوای آمریکا اصلا اوضاع خوبی ندارن و انگار قراره تو جام جهانی حسابی به مشکل بخورن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/91326" target="_blank">📅 18:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91325">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
فوری/سخنگوی کمیسیون امنیت ملی: اسرائیل باید تنبیه بشه، امشب آسمان سرزمین‌های اشغالی را نگاه کنید
🔴
@Perspolis @RedStarFc</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/Futball180TV/91325" target="_blank">📅 18:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91324">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E26LoutdEfVJNeJtKNM-dptmmT4oFd9ydvLhoqw_T7Q6X6-5n8EII7aur7YOiLyyPJ9Hoq0-mo5mbfEsx8DWCS-Fjzd65a2JAf0uZT5PnjDXIng0CElX4tSDyoeyVBdFIn75KNKg6pUnG3RDUs9TmRLUK--BBEJjLyy9mNaWq8cnZ_L9y8VmSK4tnm2x0hHc1UEiFy-pnewGYf4lCZSW8iG2zWgIt9_rXJhv8W3YJLTCCBITes5R4_SAv80_BQMR_jfbNXi1BudRVjxDgx9_2qZKVwHsl0yj3--KfeYxr4MgqIb7GYm9u4BsmQuCzKELNt7gT8ynfSBk8HiVaQoAnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
رومانو: در صورت پیروزی پرز در انتخابات، ژوزه مورینیو فردا رسما به عنوان سرمربی رئال مادرید انتخاب خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/91324" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91323">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بازیکنای کوراسائو با این اتوبوس نوستالژی راهی جام جهانی شدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/Futball180TV/91323" target="_blank">📅 18:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91320">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiXw0MO26zGWytn-pKIc7DpTFgmUb9Fk4-dwXaGFzzlq50ibV9grAOGPeWt026tBfMxxYYIqdp5x2ReKiOTabgSTSqemfeCf4zezi89IXvH_PkORy1OEKhxWGytuLo5Moy9zRmlqTXTMVD63CFlrXWyaV-pTYVysTtu9er5lQkawLd_FNMGgolVPhah3uGlxkbQy_sdSqpEcXZbfiTG03PXWOV7_445HPetqH3VO3piqJI2Cu8q3JdqybIv8_VfblFn9vpDFevrkvSQnd9q0dOV-XezX-uMCfW1qiTIjXDXcC9sGcOxQawYgfjkqbrqXFuWwaoYgBxKtT0U7IZRN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HngoCpcrNnf92cDfBzirBOV_H4VJsn6iXbBxVLYR5exC5ZnKAUXZdXmykAFb4jxHv3MBd5rFBhWWBuiCXLts6pWqvqvH47xkaXG0mOeY6DBa_dCOol6vZYnAUsLL167JRopa1yJwjP_m4gKOTFPuo3lmlN5WOmM7EFFfp1OzMiJlyc8PlmmnXp-O1BbsVsTzSkVMPI-6auywn1t94VpEFbf6Emq0L_rvX07rbxdZ5CCrlzdKPr-ErV3wj3nV_GUAK4hu2fbJR05nWFgs2m2Te0Z6zG62RGaH0CPe2IA6TXjgDltoR2yvk6YVB1X2CkAuTA-mH6_ffw4MYX8-FsUkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCcd0H6ruJQvk8QPczvjyCsqB05RwRGPI_GeGTLJoI8GMIQJGczH-EiXZ6UMiDt_xHQgkWflAIfM8aaTtXvYNltxUoHb0SfyqKjHtjpNAORcVQvfMfL9PT7tB_gS_qIZYIE8_wukClWZwthBiAEbR7BnOmWAg2zf8dBxdxP6XekGuukAfnWVcBLDpyoFcQshUBsYjxcxGYoww6xTAiXKq3anJbvF7dWXJjVTLSMlszS70n0fP-QgoXj17gcbLB3SeIhGMBUWgxTRBcLrq5Nf3DKQbizpElXue8w42aJJGFc2uDLEZcrem5BEosH_8mxmnGkQuLRHzYJCyrQBnxtniA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خوشبحال مکزیکیا با این مجریانشون تو جام جهانی؛ ما هم باید میثاقی و احمدی رو تحمل کنیم:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/Futball180TV/91320" target="_blank">📅 18:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91319">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ساسی هم دیده کار و بار خوابیده اومده ادا قلعه‌نویی رو در میاره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/91319" target="_blank">📅 18:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91318">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoF7S2fmSWm9LYAhpWe6v5uYlr6yZqkzqby08CVIRW9TfMzl_jPXMTiuPyJ-1V22AFk62W2u3U5d3754RcYVlSGqbnoHRjpYC2NEtPS01v5-gjzaVbpFABXcXXFjJgIWViAtyTSqmRlwozfxoJ_Z00Kt9SRmVc8mUfZKOja5zgxFtrKkV1G7cD7ucA41wA32dGdXeZrK9M3X7TGH5NfcxXH_RPfeXgGsNla3B-G8SK7XfsKC8YUCByR6m9FRf1X1i72bmaFaDCceT2iU6fvmFlEdi1vazx51aorgN2qcXP-r8xMoLXNjohGshskm-6CCXn9ENJ1ddzUdtWehgIuFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
🇪🇸
رومانو:
ژوزه مورینیو به اندریک گفته فصل بعد یه مهره مهم خواهی بود و خیلی هیجان زده‌ست که با این بازیکن کار کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/91318" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91317">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFcCcChpv0xCk8pafxNcyMc30joFo6cnAQUKasZOMNhoM2TxJ6wF0DcL6Rhn0GrlwsekLewq8xjjbF4_C_kQy4yH1CKvZ6k2nsO_pCP3wqzY4lvu6TviPbcXzh6V05tXgvKzx1yJlcyGMj_-r6iUgPMxQvZjQFE-UGj_HeEELBJkSmmbrQLS9RLzPokg6-1j-aWvnFPHNa2ATeee3O_x7bAuafAGRWEENF7dHfT6X8z9thfhn5RwefR9hKnaKh3b8WRgVZLDH43nFYgVCpnF9rNkR4mQQ4A4EGt0AaSByyNubKGU1RaZ5UlXKy3D8lLkYh4P_TjL4wgf2JkDnQUWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
فوری از رومانو:
پاری سن ژرمن حتی حاضر نیست برای انتقال ویتینیا یا ژائو نوس مبلغی رو مشخص کنه!
هدف ناصر و انریکه مشخصه: نگه داشتن همه ستاره‌ها و تلاش برای بردن یک لیگ قهرمانان اروپا دیگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/91317" target="_blank">📅 18:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91316">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHOH6kKJaHcKLljicZ2WJRverYS8iDkN7GEk0m0vitFiujUBH9G1j2xRIIw1aU-5Y1SJyK7xK5_WSW4PFiTOV39Uym-E_IdiuNTk1eiiol0MRUevMRKQZTZaumvY4KCqdwgfZQaRNVbb7rd3pJlQ5UCCSpb49jH0XSWoj_AEzIf6-BpLnxtZFhIdGLx8o9JkRidP-WmPF8OVPf4c-bJ0RSvOwkaiavI0mK8j4nseura1AlhxJDN3Hq7cRRzOo9gBZL-g9_yGulOGAo349xH7QdakwOgDqzw6dNQRVMX0pdlGVDRQfkbvqyfNnqAmjEd2dhBeShJrYW8SCKmnedDUgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رومانو: در صورت پیروزی پرز که قطعی شده، اولین پیشنهاد برای جذب اولیسه تا روز سه‌شنبه به مبلغ ۱۵۰ میلیون یورو به بایرن ارائه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/91316" target="_blank">📅 18:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91315">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sXVBzDsAxjjKNwgyQp5qhqRpRp-MLCP03x33Ag6ThAhldUkmuOO3CU9l0wdnoC7QbvCPqFVtbmEx-QvzxuPqohn_PdAXqX3QqLxfnblQ8ZZJ5NGEQlIcmwFoVkvSH_4TogPF1wRtVF2WN0jfW-gmu7dpBcyxfmRlPb6deHTGg3yBa6sP4062oXPVIFtY2lbmwqqRC2mGhmtjLFm_eW5krNsI2WRhEW8olnsHGFdzheaA9PZW_0oUgjXtJElzxsgCnVXg_knCMLhnwt9igFSLFOBzJ9mDoSUigttOyGEbYCcCSh9jlGuRPbmeyaf2epkaAcq3LLdkntCmetIeCR13ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
رومانو: در صورت پیروزی پرز که قطعی شده، اولین پیشنهاد برای جذب اولیسه تا روز سه‌شنبه به مبلغ ۱۵۰ میلیون یورو به بایرن ارائه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/91315" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91313">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23ab97717f.mp4?token=qz1SL16xj52FUzp-B2GTUV8jc6YJZSj-k7lULy206JCxMyXgOYPI0pfXqzSWLtUMzJB_Co3dFCocpw7YXHiUy-cpiHdMo6chv_2wlLPN9LUzow-x3Wm_c6-DsUnlmPcT6miQJ4DLoDKhHXrsNDVhg05leODBOC8O69QkRwCvySpkF5HGmduc1qWx_QSoTzIPtMhHL6a4YvNO_dZ0Mt_cj1afAj_eGLRcwJz7VTF6c_DJikysC8oewl36MdbyUb14CAgCuTZOJNnxLL469PLKUx5z1SRMKYwVdWBtjtIX4_7gcNjcQiCjtroISZm5EgGsv7J_s-aJ8cvRfM2qClA-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23ab97717f.mp4?token=qz1SL16xj52FUzp-B2GTUV8jc6YJZSj-k7lULy206JCxMyXgOYPI0pfXqzSWLtUMzJB_Co3dFCocpw7YXHiUy-cpiHdMo6chv_2wlLPN9LUzow-x3Wm_c6-DsUnlmPcT6miQJ4DLoDKhHXrsNDVhg05leODBOC8O69QkRwCvySpkF5HGmduc1qWx_QSoTzIPtMhHL6a4YvNO_dZ0Mt_cj1afAj_eGLRcwJz7VTF6c_DJikysC8oewl36MdbyUb14CAgCuTZOJNnxLL469PLKUx5z1SRMKYwVdWBtjtIX4_7gcNjcQiCjtroISZm5EgGsv7J_s-aJ8cvRfM2qClA-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدترین اظهار نظر وحید قلیچ درباره یحیی‌گل‌محمدی و رفتن به لیگ‌عراق
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/91313" target="_blank">📅 18:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
سخنگوی کمیسیون امنیت ملی: ما پاسخ قاطع و دردناکی به حمله رژیم صهیونیستی به ضایحه خواهیم داد. امشب به آسمان سرزمین‌های اشغالی نگاه کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/91312" target="_blank">📅 18:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rW9FmuNF2Q87La0T-14q06NgmWRSzbxyx3pwgRG-sB_nC__JWv7ddzZU2nvEhDM0OOeKjkdeeSRq1Kg_soThIGGj-IoLcEOiomhzHXlZjlN9bM86YgffyH3NIV9moiF8aoj2LUeBqzRvoBTCTO6khiwU2vxHW9PnKGoQjA0eO9snMjHrGa5tamQhB1JPTDEh4rL5diAtXKf_FmWsR88f0ZrEUcsnfMKRQVn59pIII0BLH3YQP0dZlZuwirqb1H4NpIwnYBOfMZBFmWKSESTpzg8fNHp9WOSlQbLcwgKTQVfOmeOMv8uP1SxHYBQB4iP10m1wKNSCSt7J7qpgK7Aoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضلات مارتین اودگارد در تمرینات نروژ قبل جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/91311" target="_blank">📅 17:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4446042f.mp4?token=J9DqsH0p1GsBmkrO1cHeO2j7c1Z4gEepMk2KL18VMK5hNxAF1VaeCwC-RIiKCA_U2Jx32sKuFP1v07f_7KVp56H4oPwiylkdwlf-dVtuUPrU_Y2vWY_I11bJOOAcwa2VSTLurvU53FN-pQPTrlf8HXmDXq0eSf6fv3JJNG8k6RN1zEQu7xIWsw1mwCoB3MHNqzxXfL178bIO0nwx2sla3lYP7hhpiFSz7ksvBYOtLdkCZGoLpu7CQmRTP-rCR1ae7uxwW_Svwl8hgbNMAcQ0u8OeJ6kDHYDrHFF0zUM8FrHACWq-LP2wHFQwpQx_dskYhYM4SoguGEoSYJWU53xQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4446042f.mp4?token=J9DqsH0p1GsBmkrO1cHeO2j7c1Z4gEepMk2KL18VMK5hNxAF1VaeCwC-RIiKCA_U2Jx32sKuFP1v07f_7KVp56H4oPwiylkdwlf-dVtuUPrU_Y2vWY_I11bJOOAcwa2VSTLurvU53FN-pQPTrlf8HXmDXq0eSf6fv3JJNG8k6RN1zEQu7xIWsw1mwCoB3MHNqzxXfL178bIO0nwx2sla3lYP7hhpiFSz7ksvBYOtLdkCZGoLpu7CQmRTP-rCR1ae7uxwW_Svwl8hgbNMAcQ0u8OeJ6kDHYDrHFF0zUM8FrHACWq-LP2wHFQwpQx_dskYhYM4SoguGEoSYJWU53xQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره باشگاه رفتن و معایب خاص‌خودش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/Futball180TV/91310" target="_blank">📅 17:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IUEsi5VJzMxBL17Qwox_Q2fRjQidBVVli08p3fu41R3bjpgSQzhkFetggKDE8mItmNcLXLL3HyGr8XLtSvcQ9RKWZw3tCeQUixXZgrEK8P5YYMLaztc3y4_bVS2Tu9q_CzQwNOBl1A8VEm8ndxmciqNwtVn9FGoNYxj9HxJs3Jg_yRlNAxeqcw2Mhk42BMR0a9JWHuis_pHJByZvB1Ow5bHjAw1lMDeb2NNYUMtuNYSnOdQ643UKqyiOxjZXXWhGOFO112qeGT6WMWcOAPa78ubjiX2kBH7Iep3ce9gRSAeHk1MRC1lU78R82oDR5A-9_03etvgORKNC3S6B5z7JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی منفورها وارد شهر تیخوانا مکزیک شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/Futball180TV/91309" target="_blank">📅 17:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxdBLZBnQnMUOAysOv4i-S4gz1bUNmBEsxCjr7f7mu3sqfSeSHJHooH7rBrQGdTT88P3Q448IJcg9Fga-iQYVuZo-dN9IR-GPRyd3ckl1DHqQRJqvl18JY0__i_cRrp-fSIGa8W4eKfc9tE193idm3vwkIOKPLj4SOIPOn5_8niDZRb8a0zGR99fOaDZFBs1xlD6JnYlSTLC5MqxaF5hO4CdbYi3qFK9eQKnZziRGMPxpB_Svb1MPeA4ugziC1rHkL8kQOGCxUUtuNsPFSOk3X-nWSB16m9a0-NVprlEZskWiqBWxc2mzqFWsN_py3Mxgm1d2yxyeAYgy51rJOyR6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره قراره این رویا به واقعیت تبدیل بشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91308" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VYzT-T6xgGswDmGrzyL0Mu-eTzybwoElr7b_-Tx4d8M3LspIcuw-MDAonDSeCK0FJIsgtV-6FyAU4MGAo7oxGKRia32Gmjm8dH8Hw_I4r74tE2MErw3cv6aMsw-AuwlXIb7Pc7Di6VIUYfglwFEztCldr6d4Fp5S_9yht1OxDKYsVeb7tvT7zzvAwa3ru0dwtV6RS1sSD_SvJrBkw7vRu8HkQZ36EXsO4PuICqQiFQcOAoE3WXWifZB-Msq4fgCfb47aGAmByODD2L9JVO3pnePlil0rFuzDLf4K5th7El2rVPkFhmQQWAeiqLAIOfYNUOVInB069eNhA8rKBpVSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#غیررسمی
؛ الیوت‌اندرسون ستاره ناتینگهام‌‌فارست با قراردادی به ارزش ۱۱۵ میلیون یورو به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91307" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91306">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmCf9laSKxJw5YMabKvbhoQIJDWO9NjucbTtd2QGHbmndTxJGuFUXTdnHno-NhjHsRyeKx2OjJecKgDRBn-j--MtHl4tMSCcy6oJ80nPld228eEotmIh9Fpoqu5b8MZqKBTKy6ncn8ibYLpNT_rqLJgjq_eaJz-y5fC4f9_s0XbI2G58p793ROMTiACfwHFiKSlA_d2eSQb1Ir6JinF8ciwC_mOfF2t0dtyrCfKSGrSvm-b9epEIAiLXxvbVf_vORYr9OGHfrwMOawfMeCgGYnCrG2wqBhEE5WZ1Nn9q2jhWDB04FqUtg_uCHaCr94PuKIeP2bkCFvy3WI4GYytWVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
شرکت آدیداس در حال آماده‌سازی برای عرضه نسخه رسمی بازطراحی شده لباس سوم رئال مادرید برای فصل ۲۰۱۴/۱۵ است.
❤️
🖤
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91306" target="_blank">📅 17:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91305">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpWHnhBTNYsujBWeV2fJgQb67w_Z63vbR36Cnbnw9vgLc0YGv0gP8wDMGglgL_WLsOuLoxyoNpn5_ll-57NVpBKnLm3CDFaDN9hhsMkN1DfHYvVaTIvJW-RNhyx78mdkZk5BV5975qutYux4781PZIsFkC6ZAH1pVPbL-TjGny74NCLFgb1Ve0v6zzzd9PHRUvoR5l10e3KBNbuU1AZ9maOighIk9LnfbHlYo723vamkkHxG_BXAUJblGYf202Bn7epwZpPYx7Qrij1anFgKcoq6v3cxCIYzQZB_p7z6JzKMBLhwE_1-nZ3Pe8uV09KBX0TFR-bXSeGnM8qFuiLFSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
فلورنتینو پرز برای نقل‌وانتقالات تابستانی رئال رقم ۳۰۰ میلیون یورو بودجه تعیین کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91305" target="_blank">📅 16:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91304">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiy1DoypKKYFoUDwlHWGYTDzJQ3Pqco1q92mo-Onmr57OMUr5bxWVfFF2_-dKHCtOetw0I-2-bAoOgMkyQvX31sSNz2jhZCAKiUZ5zao1QDSWNm5u_HV2dEaeceHcYZ4UxIncCqvbP1a93x3eFtnN4K-x8WZK7mRNpRDB5lb4_ttFmk17Gn94jEOffo-ezz4tYoEVsv5S0DyIU_k6E09TuPkzRtNZ2OKkPU6VgceI5pFRHb4BO2_KqegkOpABtW73B-63EX8C4dmu-fpPEo3vQ_xCsi6wWY9Dn4mUm3alOkj0t4usVc-IzdVXinNndYyZOQZQ8RaloODAV_va4QdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رومانو : پاریسن ژرمن اعلام کرده ویتینیا و ژائو نوس تحت هیچ شرایطی فروشی نیستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/91304" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91303">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfmQh5WdrMLfZ2X-ykJELD4Usvq1frOXeDius--5hcHpz35a67IyyZGxhtaX8jme5o7EGwEjr0lrJjPDVFJ0sgdbWWZSMDmfAX1izT_RZNXJ4LAgu7WbjcxVJSTURIkT3xNCzoXYMChSm73yTDbQ_-j5GviYaWXhV0htT_IzLwMgy_h3WgJa3WsxTyjgb8kVth1Fl5Ea3eUdF0rbWaqoPQLY5ndfRQhtyNtLlMshOvzHyhfkLPHdyWvJXzduhjwIDzffvOt17TfYhlY-52VYyHPEcUO8vlXCadoXlkOthRfR_5TYffcRL2kILRTfJ4uERKk-60jz6FlY7uDCs5v4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ اسپانیا از فینال جام جهانی 2010 تاکنون هیچ بازی را در مرحله حذفی جام جهانی نبرده است.
· جام جهانی 2014: مرحله گروهی
❌
· جام جهانی 2018: مرحله یک‌هشتم نهایی
❌
· جام جهانی 2022: مرحله یک‌هشتم نهایی
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91303" target="_blank">📅 16:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91302">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7bOGioyTcjyA1UGJAbkwLd-Ogh_JeQFgJOx6VmGL0Urck8LmwWXIWt3kHOqV1NV_sm6qJCY8NuuoJszKg6tgG6FK2cJlDwaJ0aeYVXj9TEUkdpMvesptBgf-qoxNJ1adcceHrT2ERSWjCEcF1JLpHC6fGglpcnfu5zqWTN9Kjt4x-MtBtDrBeX5Np-DT6ssi92lm3eYHDf3WXLhL-rjglXO-oVyMtbQMV9WVl4kdjOmlFpFscXDXfqDd_Jhdr5KZ7QqIV1B0wA4efXzMSvxiyOfOuE0XHlDeAJfWApZkQCuB_PLQ2djJJL8TFNMRInsCtd8sW6XjUJSrXWnOCp_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت‌های سکسی پرتغال مناسب برای انواع و اقسام مراسم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91302" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91301">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=jsb-DO6po5VnN4nMXISZuSrMynrScyLF_j_x7qIoP40aJCxKDUO2NpVfx3YtwaVBN7qcVLMY9eLtXosCn7FWPl55njnnhMTa096iFJHgSvbpkrpxLMg62AiMpusLN9L9v1KfdXlHNMwaQ3BRxa3OlYuwkNlDeubbcNl1osEYvvyZMZM3glcMY9BYyW3ICkpUdppEv2XRh3K9qTPjfAIowsHD8ZiV-nEPfwzcLaW8LxZok_RkBfPiwGTPiOqui7ZCMTeNulw533H_4KcQ16oK5jJ8S_dv3h2iWTdyQHyJop5AguS2iuz-b4nY7Z_xd8IfxaTsCnwOKYzdE6knXcKLpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=jsb-DO6po5VnN4nMXISZuSrMynrScyLF_j_x7qIoP40aJCxKDUO2NpVfx3YtwaVBN7qcVLMY9eLtXosCn7FWPl55njnnhMTa096iFJHgSvbpkrpxLMg62AiMpusLN9L9v1KfdXlHNMwaQ3BRxa3OlYuwkNlDeubbcNl1osEYvvyZMZM3glcMY9BYyW3ICkpUdppEv2XRh3K9qTPjfAIowsHD8ZiV-nEPfwzcLaW8LxZok_RkBfPiwGTPiOqui7ZCMTeNulw533H_4KcQ16oK5jJ8S_dv3h2iWTdyQHyJop5AguS2iuz-b4nY7Z_xd8IfxaTsCnwOKYzdE6knXcKLpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
شیث‌رضایی مدافع سابق پرسپولیس: در دربی معروف آی‌بدو آی‌بدو، علی‌دایی تقصیر باخت رو گردن من انداخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91301" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91300">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=sWwwfXi_naZcJRCh7XFoQr4EaxmmEhCo7xrRF7C8ZsbURERhaLDlHhAV33C7FVZKC3Ctku0THEkgIWIL7BEXHjC80mrDYDbgxpn-ocUug4ALCUlSp1XWwZVFlQ8vqsy3k9PdnyfolShy1JO4lES4_VYG7JmydJHaOh7ntD6KYYV6gx51EjHmyati36QYGqIBgGZLfjWeUWliry7a626ZnbPF1_rgwKD2LIbtNRJ0oj4iWEKQqNUUu53i9NERa0DJp7FuXhaTrlioONOxERJYEtMOxGjuIGUOmVPL_ZJb0l5yDOd6EX8zVoEryi-DP8VvbtTtX53Nyg3iScn8ucLqlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=sWwwfXi_naZcJRCh7XFoQr4EaxmmEhCo7xrRF7C8ZsbURERhaLDlHhAV33C7FVZKC3Ctku0THEkgIWIL7BEXHjC80mrDYDbgxpn-ocUug4ALCUlSp1XWwZVFlQ8vqsy3k9PdnyfolShy1JO4lES4_VYG7JmydJHaOh7ntD6KYYV6gx51EjHmyati36QYGqIBgGZLfjWeUWliry7a626ZnbPF1_rgwKD2LIbtNRJ0oj4iWEKQqNUUu53i9NERa0DJp7FuXhaTrlioONOxERJYEtMOxGjuIGUOmVPL_ZJb0l5yDOd6EX8zVoEryi-DP8VvbtTtX53Nyg3iScn8ucLqlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🙂
تنها چالشی که واسه تیم‌قلعه‌نویی ساختن و پسند همه مردم ایرانه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91300" target="_blank">📅 16:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91299">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJkMuepDCQxH56mu-bX1vOMnqklHmK3dkCPjWJM0fBMLERnfZg1uqQA0UDh7GzOmBcjvIzBQoypfUpHN9PBj9Bp9nHaL7qmxMDG1ZfdOxsQg0sl-Z47-P11Lv4ma8At5h7OT-Igfw0hFKwX7QLzDOC9IhcbjxJ6f2BS8gDug1sP_KC1-GmEDliPk0zQC70a30zzC9U9RD5bYxDA-Ebrmrk73YTZ1r0XA9Uc0FVs_2OlHibgs9FQELsVqUKoHRhpZ8kMEouqlS4bZec956cDPJVnugoOsBQh_LrD90_llr9-JeSPi0zwyR2UeUZwe_28dzAqN_ndBNU470ToYA2nGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه دیگه بیخیال رایان چرکی نمیشن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91299" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91298">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDYBYu5CXu56aYMkGV0nj6TRePV1EYtVmvPHglXoC0QRiG2xIXCYLfclXyui9CGRJmTfsqYvDS8EFg9ZlqvsHTP9unQpHV-h1HgiEGQnxrG_9v-JRTOZZyx--MorKUUwY46iBUy7VBxg6MIUR8iKkcF4Cke1REj6SttxWRpVN17Ldi3pX7aBvBGeidsbge1R3dkjwRG21yBoPfV3AQYeMZm3JwUWgYmluDyme-nEaeayyk68YnCzg_ayCma7HyAv0GMONdERiaBdvEAvzSqhXHLcYsdHZsHQcdgoJrmIS2qQUSSFUHeB_T2qd2Z8lZDXilLo_Sc-3JhmcPce6WMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمیز از نظر پسرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91298" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91297">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nBEBtGH5vkGB99XhGdGvxczYLgstdujaREWncObVP0zlSqZRKnMaDOkAt77DRntnDav0_sq-QTomK-CYoJi8wivKWk0kN5EaxYZJbhMhC3RWOAQfu4Tv5zFpoWsuZ9wUFYpgMesfE-w6nkSfTjHEEE1Brcb1DLYeYvLjY6g603p3xRWnHIVnAAs82CfnO6oMCzEr-VGe5zFQErt8Tg-vXPDMQzKW23dOKMq6dTTKls1Z73qLCuKcW9RWtsUeea2U8t5oY_4kFPyNUk9hWBleFDIJE_ryD_DuipMSiZ_Y3KFvkvjO3_C1hgjvg3m-QffSqnUI415bFXn-LhSYmOWVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nBEBtGH5vkGB99XhGdGvxczYLgstdujaREWncObVP0zlSqZRKnMaDOkAt77DRntnDav0_sq-QTomK-CYoJi8wivKWk0kN5EaxYZJbhMhC3RWOAQfu4Tv5zFpoWsuZ9wUFYpgMesfE-w6nkSfTjHEEE1Brcb1DLYeYvLjY6g603p3xRWnHIVnAAs82CfnO6oMCzEr-VGe5zFQErt8Tg-vXPDMQzKW23dOKMq6dTTKls1Z73qLCuKcW9RWtsUeea2U8t5oY_4kFPyNUk9hWBleFDIJE_ryD_DuipMSiZ_Y3KFvkvjO3_C1hgjvg3m-QffSqnUI415bFXn-LhSYmOWVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر تو ایالت هرات که ادعای پیامبری میکرد، این شکلی توسط طالبان بازداشت شده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91297" target="_blank">📅 15:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91296">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeAFcVZhgybxxA_CqFgzeu6OLwNwvgih385HFkprbIgVT8H6MC3DDldLfQ2ubfIhd1ahTkaq8k5DYBj3EQNNFPxNN-ZF9hintf96wpVcCSJq_Uat0e3WXv1NQ2YKvO-tkSpwBHd8-pjjfFRVeFKanFpgJQXFMr_E5vkhWMBUWjnZCi0WYM8uuAz6WomQFAiQ7oEMGalSaVGY7PdaFbgftoroEYpWpnzb3htKn-x-R82vuqDs8k9obPQg0xwHtA-QcQra2K-L__nnJTHvRbcsMkekCwNJqQKGEw9OxHyWQG3srfG7pbt3ghqOZUdui-EQIz1xIatc70Q0-d7uSsYd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 7
🇺🇸
استادیوم آتلانتا (Mercedes-Benz Stadium):
🔴
موقعیت: آتلانتا، جورجیا
🔴
افتتاح: ۲۰۱۷
🔴
ظرفیت: حدود ۶۷ هزار
🔴
سقف متحرک به شکل گلبرگ‌های گل
🔴
یکی از زیباترین طراحی‌های ورزشی مدرن
🔴
صفحه نمایش دایره‌ای عظیم ۳۶۰ درجه اطراف…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91296" target="_blank">📅 15:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91295">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onay55DZDmx20RsuJ-vX8V-q4Qq8Uhgs_odbFAWGUbqZoVvWHRzn7caTwsC7PvnLcwAzRxjNEwhg-vM__KOjDknvEa3Sl6R2Y-O1LjWXwoNdk8cBJ_In75ZBPWDAxziGVEJuuHFza0C7l6JyiSC5Y298ez-u8x12gvR2u1aDAMmRHdxP3Mz5VUEQD18-yIlcpqTQp5rSHCj1C2SoPPa5N7h5_05NSLHa0HA_8t2Ibw6c6WrT9aRme4ayhJWvAMum0u3BqVK_n7n6TDzWWDfCmkW6PAXffjhPoibR0E6HCnyBwBd5AagIinSZ4COj3iPg77cHh08E_m0a5fOuSh5XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 6
🇺🇸
استادیوم منطقه خلیج سان فرانسیسکو (Levi’s Stadium):
🔴
موقعیت: سانتا کلارا، کالیفرنیا
🔴
افتتاح: ۲۰۱۴
🔴
ظرفیت: حدود ۶۹ هزار
🔴
یکی از استادیوم‌های مدرن اولیه آمریکا
🔴
استادیومی هوشمند و دوستدار محیط زیست
🔴
دارای فناوری‌های…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91295" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91294">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6Z_NlXMAnHX5Kx-9Zs6DUV7xpkBKrMFXgAF9a7gWAUu0hfyXHjEmHk92rg0SHf6aCOk0nNoXImdPaM71V_ibNC4PDrH2W9FKEgyOXK1xJz_02JMs-0f0OSl285JUiCJV4HNxh9cKiXtt_SjFZtrmXMxpjtbc1Ml_9XvB92GAi9AO97XRZ4oNI7eMkbKoLkOjmyLhfdEODwFsjE2DhtuZpyz_f0jzsMi9Yu5aeo59LnMwfaxBOLEg8LIqbHNVpcmA4hKqo-3l9IQBZ1mOkt-OMvIKaXacb85JTZbzgfIoS2LdO4oMTLyDC57i5srGSq2owrMlb6d628q2QziTdHHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 5
🇺🇸
ورزشگاه کانزاس سیتی (ورزشگاه اروهید):
🔴
مکان: کانزاس سیتی، میزوری
🔴
افتتاح: ۱۹۷۲
🔴
ظرفیت: حدود ۶۷ هزار
🔴
قدیمی‌ترین ورزشگاه‌های مسابقات
🔴
دارای سر و صدای بسیار زیاد و شناخته شده به عنوان یکی از پر سر و صداترین ورزشگاه‌های…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/91294" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91293">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2aCCnG2nv82574PlJ7Xu-UCtYWhfTRl0wnK7KHZGWPbidbtSdEbrATdIUV0xC12IrcNmZjnRuq8Xu3RBZgWnrLkkuv4aT_BmR06EdCBpY1O7VYe_FAmO4Dy3XYxqLNH25sz0xB_Mg8gOiHCKdtOfJL7uWzTsrard5jShl3GLestTTEhdRaQCWevLzcZDZ_0lRLyiD0O1cz8URZYfHEPzRFBqatqYlElKeid8KMao-BQQ_Ir3yK04LcVl6CLVDdqJJHdwnlKSRTo9iQ5AFFOlRIK0IjzKmS5VLlZlkHfxcX11iQCUISwhReF_4zUXUwbZFpOJoetJtzT1haRmLGwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوناهم مجری دارن ماهم مجری داریم
😔
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91293" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91292">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmvg0vPoEL7CTKsGNoYIy1EWfoqFE-s-0kbC9WB5TjN-H3b6d_9-Mu64kczmVTjvaF89NRlChkJmtDZaZq52DliaoQXv7yU78APRYYkH3pK_F6nQ9Xncx7yECtsgYWHJD75L8JLxe9QZoCNRA3ovX6DWQhysUMJdCZ8n1Tc3Y-2peZssR1NV-aj-StuIgUC1o_Z0o-ZXQI_t2-ID0XYQCh6ReqMoF9zJ1tD7iGGQJicQpzCOCk5NP-9y08Wdlnd0bnurtWwr0-Q8I3WbnyW1NhpfXM2HFpbOWkDPq--JXwb28aGSryijkHPNb0kYzVOD2zcUxVjhjR6v_GuVmEACsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 4
🇺🇸
ورزشگاه فیلادلفیا (Lincoln Financial Field):
🔴
موقعیت: فیلادلفیا، پنسیلوانیا
🔴
افتتاح: ۲۰۰۳
🔴
ظرفیت: ۶۵,۸۲۷
🔴
جو بسیار پرشور و هیجان‌انگیز تماشاگران
🔴
ورزشگاهی باز با سبک سنتی آمریکایی
🔴
خانه تیم Philadelphia Eagles فوتبال…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91292" target="_blank">📅 15:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91291">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrl1uiOdQKReH03QfqshUzVnF_fb3xp46muNtA3qI24h6-NtXuNxyV0UolhSGNx5mWUIvvDq5Mrpy_QAoQYo2mXNVFMuYXJeRA-WZFNHq3FCFzsicfNqoc3ZFexe5zCj9PN9JWlUgde7vjgRpKPmx9V_Z4ThPlqalQifh4fNLXRS69eKn5s1-BNFBGbGZmWnKYYFj7ES03sUVjZI76h5MCwQfnrewg6q4p0VR2zm9SuXvKSeAesqyxI84Iy2IWb-JCKXl2BWYULuK_wfwTe3_z-y7Vrgzo1AEdIGKAXOVdazs_eb9L9Vr0pDo0OherWwHwRSrdEVkr4KcsMt1EB2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 3
🇺🇸
استادیوم دالاس (AT&T Stadium):
🔴
ظرفیت: ۷۰,۱۲۲
🔴
ساخته شده در سال ۲۰۰۹
🔴
استادیوم تیم فوتبال آمریکایی Dallas Cowboys
🔴
سقف بازشو
🔴
صفحه‌نمایش‌های سه‌بعدی غول‌پیکر از بزرگ‌ترین صفحه‌نمایش‌های استادیوم‌ها
🔴
استادیومی با…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91291" target="_blank">📅 14:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91290">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC9baIl9ATl7AZZEbx-OsouxMEmsdJz4-4KjlURTQXlcw6apyMUI5H033PY2Z-QuwnD-IOWC65dOSx66b11Sj_66cjhxtHBKqfR-BhP_8cTACzAUanijYF3oU7KBAU9JEc94wd0Z8mXoqQnSQwwXUVjRwbhforHU7GJu51Yol_bCXCNXpItvSHFeheb30UX4upXXyQhAqcG_NYOeRknM4PM0OI5JNXNqTpi3x7SK4_jTd6aEiEFTPICGny5e-GqLJZZGI6KqLErRFs_GPKFGdGbN-6D7CEhxOr_vZ50EtZV-KGGEEEC13XjPa1Jrx_eFPIrQyruqiWwmZJe_HlQhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های جام‌جهانی؛ شماره 2
🇺🇸
ورزشگاه هیوستون
🔴
مکان: هیوستون، تگزاس
🔴
افتتاح: ۲۰۰۲
🔴
ظرفیت: تقریباً ۶۸ هزار
🔴
بسیار مناسب برای هوای گرم
🔴
اولین ورزشگاه NFL با سقف باز
🟣
خانه تیم Houston Texans فوتبال آمریکایی است.
✅
میزبان ۷ بازی در جام جهانی ۲۰۲۶…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91290" target="_blank">📅 14:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91289">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfRHxoirZXIahbYe28mEMRco1qVFzODMXyLdqiRSBJhqY8I9FraSnYjZ8Z7rt87o68Y8ghfv-QM7ThFPwqLtXF9ro4Qx3nGmZ8wgysEUheyvKsOKApw2X-rPno4aF8YhVuZqjLg2Bs9JRR8w0NoKOi_P6BLYc3i9o9mPCuwUVcNkrPocdx4YfHhAPM3fHf8_saex1fH8I9uALGQdwLm-Bss0rSxXt2-P1uyF9qKOJ_pyXf1onV5tfSQDdZACLlqab79W4g34Z1__8vpyNGVaplsQiFT9Pk1JM7ipogd6rox4XGK4hoCqbFdbvpAxNrRqu-Hbcd_MgwnN6XILzwSStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود. ۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91289" target="_blank">📅 14:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91288">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7J3MV-ZCG2QOQoQBrmhWX7tiuoI-Lv4b4BOT0I3sA8gB3WhNzjG1bhDc9naxyAL3GExakuOqAjXnNfpMebnPQkr7MTrQzV35heuuionUEBNDWexxjV5gkPIjkVqoe5qs4FUu_CUUKonACPKNFY2tf-XPA3k34Ye5yq322ZhRbnqGyI_KMufx6N2ToMMatMoMpnd6bEV9-aCuV_GaJchqEGWWVAhFBcHTm_Jwz_A5AYNwS3kHdYQ77ZRb1m79H8FcFCasn-EckfkAIE8fH6yMRDInOHC9oA5lnONh2gXUOYC8EabAGU4uJ1bGJYHd5ZewFX3iBFInlmUCYSu3tEBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود.
۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲ تیمی + یک بازی در مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91288" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91287">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Vuixj07J0skaWGNHY0eRO106f2Ddp5aZsV4F4zrr9_4lRyqAUXSwB2ltgphXAiv70snJOqMVYoEUI4_7633B6YOzzhL652B6A-jiSk4RdA6IUdFjoTPS8m8s0gG_XrvBcTbny2ReKG9JA4ftYKX4grKjm6G2R56pqNcY9Gl6VOwG3vTd4SSxZOomHONFm_rvgiz_my10KXQIbFMa61Rl9ACd1tYI35z223ORYuJuZMlvxgoSLRIMNP5l2DwlBoQfxpsuJFwnpSw-rxbvvrhBLgcB1GXq15Qaxowd3x2kFFVaJTCz07vp44rIUZEeUHS-PMUih9uCNJ9Lvzkc7-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤩
#فووووووری
؛ رسانه‌گل: الوارز پیشنهاد ارسنال رو رد کرده و اعلام کرده نمیخواد به لندن بره و دوست نداره در تیم رقیب منچسترسیتی بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91287" target="_blank">📅 14:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91286">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIa7CXYMTyQPNs_D7rRncmfTUEKbc9se8d0hYgmvm7p_5J_4UynKAE5_rI2KXsA5vtorvzydTtnqBVJ-KtNrNICtZIuZsHbgtHne3tIlL5zoak6ybZaDwRjnRfpFudJDtdhJnFJnUpeKAwWnEohScYIQ7prHf7XpkPHJ_QdjNQnAz-OjYa2fqkESI49UhQ7vmZnzR-U-xLWDIk2OUGZsfNDzHUOEBDIUxEUow0thsfyJPZkWCLssaMZL_q5PJ11yX_XfK_Clg7siHzn4-T8JqtJJFdP7g1FSM8PKWsObj0uxBjJnV9M_F6f5PMlf2NnbaHbgSCktHWbjL3DVumQ3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ براساس شمارش اولیه انتخابات رئال، پرز بار دیگر برنده شد
- فلورنتينو پرز 65%
- ریکلمه 35%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91286" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91285">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=uYTkc4dtfG3p-_5oWVqNF8IIzku7re0-SUTt2PO5z7-9HV9HLstgsgaaCFo5DPONka5tspbdEbo0iYSL6XCcLOkpLrZQh6tIKYx9VQiZzlgs2tq4Oyt4Y0CtZYtFM_H5EkhHi_l55DLnl4WukQ2oWf1ZhoHy41RmnuKFkpbTK-iIYnan1zZt07AM8fMuRKWdq2kx3LNGnozCoQQ3nfIJ_PeW0Wn7Fb7OtbLtsKUhds8ZUSysMvQgkT8Y0LQ_yc4eUwvqiByQnmxU6DewN4g4EgGbwlDuGka2ZXsKldaXPQ2S71TmwvRxZb8lP4SxMyQ-Jz9nCpmxo_V7TXBrI90c0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=uYTkc4dtfG3p-_5oWVqNF8IIzku7re0-SUTt2PO5z7-9HV9HLstgsgaaCFo5DPONka5tspbdEbo0iYSL6XCcLOkpLrZQh6tIKYx9VQiZzlgs2tq4Oyt4Y0CtZYtFM_H5EkhHi_l55DLnl4WukQ2oWf1ZhoHy41RmnuKFkpbTK-iIYnan1zZt07AM8fMuRKWdq2kx3LNGnozCoQQ3nfIJ_PeW0Wn7Fb7OtbLtsKUhds8ZUSysMvQgkT8Y0LQ_yc4eUwvqiByQnmxU6DewN4g4EgGbwlDuGka2ZXsKldaXPQ2S71TmwvRxZb8lP4SxMyQ-Jz9nCpmxo_V7TXBrI90c0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🐸
قر دادنای شیدا مقصودلو زید مورایس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91285" target="_blank">📅 14:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91284">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=Av0W9u-yr1-A55sUQcBFBat-XLNQs66rsz-opSqkT_m63JD9kaoCMUIpy4tgUhvP6K15ZR80aPyFYaG2rbOjEfCDPdu6HQIS4lh8mG4LjYeLdrrsNLQdgu9n6nNVTBtQr1TcEnLgqjpkiF6KfhuOahG97oFsU_XWg5mxXHBUYleM67MtlCmqhU4KjxCC_04M8hGNx6JegLBLbsmqtSCI2YluOF79tq0iuqt5Xlaa1K7SzQZxAwrFrVSlpPEWt5o2_VEQIbpV8PRnKqVZyKY-BkWO5yL5JNKA3FAroOF4OdVqB-GXTFgY_yahX12jVn6FUgJ8tFHX_aeV7YqCVyVBnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=Av0W9u-yr1-A55sUQcBFBat-XLNQs66rsz-opSqkT_m63JD9kaoCMUIpy4tgUhvP6K15ZR80aPyFYaG2rbOjEfCDPdu6HQIS4lh8mG4LjYeLdrrsNLQdgu9n6nNVTBtQr1TcEnLgqjpkiF6KfhuOahG97oFsU_XWg5mxXHBUYleM67MtlCmqhU4KjxCC_04M8hGNx6JegLBLbsmqtSCI2YluOF79tq0iuqt5Xlaa1K7SzQZxAwrFrVSlpPEWt5o2_VEQIbpV8PRnKqVZyKY-BkWO5yL5JNKA3FAroOF4OdVqB-GXTFgY_yahX12jVn6FUgJ8tFHX_aeV7YqCVyVBnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن مسی ماشالااااا چه بدنی ساخته
💪
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91284" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91283">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=WubxATBxtX2FhUcpDCa1i1XhJBvj_G1YNpoG9vfjvDp8ofgs0W_K1KLiAMBr50TNNUIIIk2sfdN2tjcs70scN5aOs9VBTVWu9Fp-n4JNBp9gjqSuL0XmnsMkIuLMflQ_khZo7mkW3FplKIcR-ZgNUHMqglNjxJjoaDwzf3NCI3L1C0y9IG9RCpHkdqW7dlnfJpwdZm_kVGkZRmyP6a8dgFdbsDIqQKi4GMD903JmfQKZQtSvehG63Is9agDWmPfAZ0xxKcSNmnoU-6Y6T3srTuioBSaKvIdfiRMSgJF_TNVS21gLHIsliqmdgYyUpvUKAXKgOWrLmdUvSKfR_FlJMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=WubxATBxtX2FhUcpDCa1i1XhJBvj_G1YNpoG9vfjvDp8ofgs0W_K1KLiAMBr50TNNUIIIk2sfdN2tjcs70scN5aOs9VBTVWu9Fp-n4JNBp9gjqSuL0XmnsMkIuLMflQ_khZo7mkW3FplKIcR-ZgNUHMqglNjxJjoaDwzf3NCI3L1C0y9IG9RCpHkdqW7dlnfJpwdZm_kVGkZRmyP6a8dgFdbsDIqQKi4GMD903JmfQKZQtSvehG63Is9agDWmPfAZ0xxKcSNmnoU-6Y6T3srTuioBSaKvIdfiRMSgJF_TNVS21gLHIsliqmdgYyUpvUKAXKgOWrLmdUvSKfR_FlJMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
بانوی جذاب آدریانا اولیوارز مکزیکی روند زن برزیلی رو تکرار کرد و بدن خودش رو پر از برچسبای بازیکنا کرد و از دختران سراسر جهان خواست تا قبل از جام جهانی ۲۰۲۶ به این ترند بپیوندن.
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91283" target="_blank">📅 14:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91282">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34842d0797.mp4?token=NtLvrNlg5YCGgOQCwD1FhRmBJK1pAgqrkmm89OTS254v1-0MJgfM7Yl16fKTiyiDp8CBE2XZDNnYTK2N_5x8dHuVGdDSioXi5zCN49Rm5Nn_HSbE0ylwcHEzvRG1xIedYBN4onmfbCWacISDyvzyL8dN4Z8LrgVNB0Rq7h1sn8Oaa-bfBJSYtiGdiaqyPaAYLynmYiWOwcQlonB2i0WGUfvqDHVxpi08BOJaRlkgbX4yXMFdCgKzs4hUmSdUOxgmDQND3lua5ulcGL0ROcpULwAHfmsEpDAqj3KvYmcWmOJw9IwRe0BC27vssuHxpKVjSmgkMJnmcORtEjfTYWj6WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34842d0797.mp4?token=NtLvrNlg5YCGgOQCwD1FhRmBJK1pAgqrkmm89OTS254v1-0MJgfM7Yl16fKTiyiDp8CBE2XZDNnYTK2N_5x8dHuVGdDSioXi5zCN49Rm5Nn_HSbE0ylwcHEzvRG1xIedYBN4onmfbCWacISDyvzyL8dN4Z8LrgVNB0Rq7h1sn8Oaa-bfBJSYtiGdiaqyPaAYLynmYiWOwcQlonB2i0WGUfvqDHVxpi08BOJaRlkgbX4yXMFdCgKzs4hUmSdUOxgmDQND3lua5ulcGL0ROcpULwAHfmsEpDAqj3KvYmcWmOJw9IwRe0BC27vssuHxpKVjSmgkMJnmcORtEjfTYWj6WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گاوی تو تمرینات اسپانیا اینجوری رو پای رودری تکل زد که نزدیک بود مصدوم بشه و کلش کیری شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91282" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u_duVhaZv7-2G3XkWSzY93Ya5PKeMk1DSk4VLcWFayvO_6ToATtQJcEewrtxDA6bu1X6TrxEozoTclwoqkCzSa2MigLZKyK85gsSv28nYSMvggiFhHtCk7RgUU1v26RqS3eqCwLJMypXCosrR5eBkfCyEMCWPSu_4vCtP-oDcQC588N7OoMmuHhGFGXSE7JBfgALiAp2vG7qDZN3VvoiOMUTu11f2bWTh7b5rZGV-cwum4m81-ZUmqPz58GZFvMwF3CLb2KV16EZPyWKwm0yfPhIPyC9hCKPxn-ah_Xbc4OQiDmPY3rcJ3SujU4saBcfBevqID4nQxgY6W6F_2fyNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BRAPlIA81URX-VwwRkZhPe8k3GhqQMPXIe2uiGYEu-rBHVYxH0jkyNTt7xUVkqgE-29DVaVKFUOA0Rkob9CnxRNY-7q0yPQyzWJG7sZioMD_nXTOd_C7RN2cHWcxUn4GF3U4ePJ1lor6CwQgV2VoXDg1HNEoO4NMSxG4vJLM_E1E2wKvyTdi8FO6dY4n35di8xN8k16biQUCu2Z3rt25O1Xf2qqSFGGRMtH7xYeo8W39cXeLNtngFrIrUCwzsRGN7R4-7PxZiopJmBvjcTH2AFS268GrTBcVl0wEHIqjb9OEI6luN_VHdWKKI5P-zExt95V5KjYola_3frm6J6t7pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل مو نیمار برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91280" target="_blank">📅 13:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onYxRtm1JlXgTy6sC9-lCTdjQPE_fY9PDt0HqIgFZm_AeXgfrTMpX1xfWtPjdZ_s6kn58zXKG0OvoWDr8ttXNGmJqQGrU-V5Tv6ovXOmkbUAwwz5vF3h1QW1UxcTFi3dZPEpdAl0uhDKbIqREiKvHK-xpUm2y6U1V-Fssih38R8T1MhEoaD6fJJRHxfsrh1akJguRG9ny1XNUfZ6VfpnrQkQNdm8M7K2tsjGJxb39aRawgO_Av0DRSeeSheEM77WsskQ0UkOcwqqvhXJ_HhQ3jbKD1wPK8l1Dl7IdPnvdcLR00HZfEVYGuqdD93hmTI1ihJVBPg-_bwowOa3C3ytzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qfjyFCKaB_Uq29L9FF9-WhcVuKLHxz3dMVs6jMaS26xzdnNbXtayCWZY8m32602rPybWLvtFXMOcmdOxkDpphWXBXE1dSknkrylpW4SqRfgY4kHT7JKMYZsItlOJm3sNzTc5OOI2r-M_LkOBSruVCzUqhO47Y4gXOdflwjwKee3CZfvlEcrMUcHhDycR3HllUWv4doJXL600u5Nd5U3sJYi4Ed-wuO25c4Pz9tdHeqXskxm8va0mGoHmf74BkwdIjGfZNG1KUSm4WLU4nG4oJSDFbc6r9aN-O6YR2M4G71s-ozleXEH6i5r9-dMGyE_nA9tgbAzmGBMu_VsvE51oKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tp_mDHxZ31Spi2GjybNfI9Htx9xahsF1LwHBfOSmg3tCQGzf6rFY1cXsNAd2IeOnuDlAGOFIfbxbarI09q4Fqn3c-DPnqk-IA5FF_LZ18x254wBdcYpqBUx-65J-v8XpvHVUVQJRDs5LrPGSrA6SSkKRjVhs_uG0s27HmVmNKwM1VFYl3y7lfpgAXXRLmiy75bWbPeioNe-aP0xPttSTDfFsxgT2zA8uOI-ejYroNDZCLUNzSDLf0OyoUglVlOcaoYhIEHyWvjredxtWizDVtIveAK981HmX-8MUCwCXXFfxXOcHXWB2nLwg4q-iz7dlWejQxqEf8zY5fJlYwnQ1Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور پرز و ریکلمه در انتخاب ریاست باشگاه رئال مادرید.
کی رای میاره؟
❤️
فلورنتینو پرز
🔥
انریکه ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91277" target="_blank">📅 13:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqTxZs3xHwK1qHzjNwWiPUmj5q65Pqcfx0O2C0V17Ywo39n2zQSWU9dgpjAO5-PNH0PxRrLJ34mYa5UfD6j-6IlY4DAKbs97LBx0nrezUtqLcpFvxGoeCyqBEdo9OfWLG3OhugnEKbpxF-IIp6rR1dXSH2Cld8oqKXKaId0svwIyo4RNeKtOsewEXaOPG0U5PF-tEyT-o-D8SJHzar9akHNFK2hKogInxc74f7irAPhuB9D94aNvqfIVBj0SI0cKaY8baIiTwgIyfmg3VxcuVm40gICOrDHmCI_kQ0QrKHmmE4qJmWG9AnllOOIfcAOa0tQLwHD4C3udxmISXp1gAT84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqTxZs3xHwK1qHzjNwWiPUmj5q65Pqcfx0O2C0V17Ywo39n2zQSWU9dgpjAO5-PNH0PxRrLJ34mYa5UfD6j-6IlY4DAKbs97LBx0nrezUtqLcpFvxGoeCyqBEdo9OfWLG3OhugnEKbpxF-IIp6rR1dXSH2Cld8oqKXKaId0svwIyo4RNeKtOsewEXaOPG0U5PF-tEyT-o-D8SJHzar9akHNFK2hKogInxc74f7irAPhuB9D94aNvqfIVBj0SI0cKaY8baIiTwgIyfmg3VxcuVm40gICOrDHmCI_kQ0QrKHmmE4qJmWG9AnllOOIfcAOa0tQLwHD4C3udxmISXp1gAT84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاچه‌ارومیه که حسابی جون گرفته، این روزها میزبان پرندگانی هست که چند سالی از این مکان مهم مهاجرت کرده بودن
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91276" target="_blank">📅 13:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXdUcoUwhQbO3kz5hDXnIqrjAUJ6T2QVmB0_l4T9zhxo5dA4BSGQurmzsOG6fXZO24aw11c50_hTxcFtqbWsceQFXZeDxgmXp5ikGLVEDSFKOjCqqo0Nrk4vjyFlw2OEQx9btBQs3NMgxMEvHxbEAP3ckt-hv_aUKckQ6FasclWRKElVQ9ufR0e3lcXyGqltryeIK3olPyM7AmbAhsNBzPKMtmJ2PbzPrXh8bDfiy8zuw00c809XkDvcHqMlebvYoceLvpvRxSoX3NLN61kBr_QxD694enojRo9aLLx80ucZHDN6_ez7KF5KZlQOPZdOli1C_jGH2csPE7POd1yXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ماهشه امیرخان؟
🫃🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91275" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpZFZdM8ZmyNqYe6D5kXOiGUrcu0WzfCzy8aH3kh1ThxAEchG23LxuTvaVz0_fEnbEwpcO4Ye1Ph2GKT0BUaq-438a3l5f7gnVAgoNESR9YJvjPOZ2rm3sqP7dpky4vK67eLZ_Hug0VN8vDUzAw5iQHapFYABvJ1f76R1CSj8gGPEfax2EtRPgpSmcU1BAV8oPPxzkh7ZjNKwvmksUKezgQwb0U3NnVP-uQfssdWPUNKHbPSBP7D_DOWnvRO9xMQI00tSdR8HYgZEOr4v_skY77U-2Ivftf2YJfITiwdI5Y7XY7_jjzR_3y0Drju9P0haFtRKBrVRkKvaMVLQLXXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
ساوینیو و تاتنهام برای قراردادی تا سال ۲۰۳۱ به توافق اولیه رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91274" target="_blank">📅 12:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GujurMdObZ3-nOu6Xyi3YWlzcwCBGaXYuFC3wDjUQMd1WUtsl0vN-SMoyCj00AaZtAEbAjM6eZWaiLJVLyS-wImlMZFpfoQ87gbK7AVySo8sJWN-HggzEh1_HSqXT_x2DePFfsvDcSsHmCKtNDjrFWa-2BGoBR2UMY-qdqNWhFQERZEw27vGGQu9hIDXH5NZdLuG4qBDI8MNuSLUDUaCvI679dgWEGvjSpbq3Jek0xSMNg76FMiahDsqrOmCVHizNFKQpEfiKtZeHc9a2_SUXUVuYkENzA2fq6MFqJ3gM5tDcFKAi8aTwhK-9Jrs1oTfUdpV0Y2IVBZlo9sHYMgoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده دارن شاهکار خلق میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91273" target="_blank">📅 12:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=TO3-sm8xB3pQiIN6ba6jBdqgB8AmB7hrm31_gMwhn7Ub7wuj3bVHzp3x5FE4erK7tlXCPH0y0_oHzUzUywklXHkSZoMuWA6zy2FRZhX3_umwbAlE0gFUJFIlsiSbU2RNuneMsv_4oa7FHIB-lgJHFVwAOor7x_O1ZEri3Ie6EolzXED-8bHi4G8UOMXYxYkV9qzOD88xSJzQe2IDJUh9v2wEuy-k9Plh_ObbJvMeEnNeRocrJZPuQOrEXNOP27_3OK9SyS7byM0ywFf0Nlki9XeNkROwpI9b9OAsxN73W5WeRzp9d3-ucHR5cpGQUWPc13KyFczaAY-xY9_LDRdSkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=TO3-sm8xB3pQiIN6ba6jBdqgB8AmB7hrm31_gMwhn7Ub7wuj3bVHzp3x5FE4erK7tlXCPH0y0_oHzUzUywklXHkSZoMuWA6zy2FRZhX3_umwbAlE0gFUJFIlsiSbU2RNuneMsv_4oa7FHIB-lgJHFVwAOor7x_O1ZEri3Ie6EolzXED-8bHi4G8UOMXYxYkV9qzOD88xSJzQe2IDJUh9v2wEuy-k9Plh_ObbJvMeEnNeRocrJZPuQOrEXNOP27_3OK9SyS7byM0ywFf0Nlki9XeNkROwpI9b9OAsxN73W5WeRzp9d3-ucHR5cpGQUWPc13KyFczaAY-xY9_LDRdSkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گروه E جام‌جهانی فوتبال
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91272" target="_blank">📅 12:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">😂
جمهوری اسلامی پاکستان دسترسی به اینترنت را بدلیل اعتراضات در کشورش قطع کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91271" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niEWt6-gP80WIEoq8eiO1T-B_mdy8_XFdk3lZoiyhuzUYG4dzYkIMCq1MMw4o8w_aq7llbRfRn7_zghZ7YuBUb2vIB4Ro0jlq0Tca5p2oQyuUnWlG1946sD17xkTReRuxReWYiw8B_RGxidom5-gEzcNhnX2GT-BUHhWzlsr7w29bYsqL7XaiKt9uweZ5fOk3oGEEaGAQSFJ0n3J_-GlBNegmSvcftz4MZTJiqU56MWXQCsXCWXFUTy-QZ5lTN4osk9eWa7bRPSZaq4Z2QXwEnCjU4YQCJYX7efPJJY3ZU6Rq1SlZJxBJXXMA5wkvYxcKt6ktnDclMM_5rrQg1jTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفت‌سال پیش در چنین‌روزی ادن هازارد با رقم ۱۰۰ میلیون یورو به عنوان جانشین رونالدو به رئال‌مادرید اومد و‌ در ۷۶ بازی با ثبت ۷ گل این تیم‌رو‌ ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91269" target="_blank">📅 12:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=v-hubd2GBf5LyrpImbveqNT_JS2BKzS6YYO9LZXA8ZcL_FB1kaV3PfCq9Y3ArroycTIRSyXAmUTchHVoLMZodpclrP-Twk9ZZKui_tYiUVB0GkLPSaAdOFXqEbbt3L7PuTqYDUXTyguaW7JByQWLZrHtO0UqCkHPdiFLMdFiJ6s5Yy4ZwX9MxI2Zk30QPlbFuDROgT9Q_kjH1MVtG4gIURBSYeCrWdE7w-wkPBBoV-YRcFEQ5JLcqZiZ5gfiQdXD6GMXk--HG7jsmF-inHXW6ZLYPRkMChR30xHnP78hLRDegXlHYfMJkKVau4r8JLnXYVVclrP4z0iqRfDI8br2aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=v-hubd2GBf5LyrpImbveqNT_JS2BKzS6YYO9LZXA8ZcL_FB1kaV3PfCq9Y3ArroycTIRSyXAmUTchHVoLMZodpclrP-Twk9ZZKui_tYiUVB0GkLPSaAdOFXqEbbt3L7PuTqYDUXTyguaW7JByQWLZrHtO0UqCkHPdiFLMdFiJ6s5Yy4ZwX9MxI2Zk30QPlbFuDROgT9Q_kjH1MVtG4gIURBSYeCrWdE7w-wkPBBoV-YRcFEQ5JLcqZiZ5gfiQdXD6GMXk--HG7jsmF-inHXW6ZLYPRkMChR30xHnP78hLRDegXlHYfMJkKVau4r8JLnXYVVclrP4z0iqRfDI8br2aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باباها جام جهانی امسال ساعت ۳ صبح:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91268" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=QzGyQtROXzZpFW9aEPhalJXN7eT0R_njiwt-2GvyT0wOCrxEPLCDrA_EaTDEXgSTkVEukOoaAKSndqqzVuPF_KoIvow5I5Cvrcd0TKStsWHAstZ0dzsxIurUimr_TcLA2jwLPJp55ILQ-zZKdFQLQnr7zxc1mPJEAlWjxw4Y76tycG9X9OQJlY6xggdZ3uFvFUvlAlFefmY3QXLS99xN-vYk15CAGw08TT0bMMy13__x8GqG43l9CCxSjx-XRgwTxlGKpndh6UjfuwvwqEeSCDynSiYpAmXrRSQtnVUKJj4p__C6A2xU3k2Uvef_w1-2EY_rK9Ee9AiEA4O0s7WFFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=QzGyQtROXzZpFW9aEPhalJXN7eT0R_njiwt-2GvyT0wOCrxEPLCDrA_EaTDEXgSTkVEukOoaAKSndqqzVuPF_KoIvow5I5Cvrcd0TKStsWHAstZ0dzsxIurUimr_TcLA2jwLPJp55ILQ-zZKdFQLQnr7zxc1mPJEAlWjxw4Y76tycG9X9OQJlY6xggdZ3uFvFUvlAlFefmY3QXLS99xN-vYk15CAGw08TT0bMMy13__x8GqG43l9CCxSjx-XRgwTxlGKpndh6UjfuwvwqEeSCDynSiYpAmXrRSQtnVUKJj4p__C6A2xU3k2Uvef_w1-2EY_rK9Ee9AiEA4O0s7WFFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
رأی دادن فلورنتینو پرز در انتخابات ریاست باشگاه رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91267" target="_blank">📅 12:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDWiRALm1TAbN5bekzyRqUHvacIePwSmOLM4iQzuk1EE20q-6LhxCrWQJpPOE4DcpAZa-0E3c7aU0BizwuPa1WXikhMhoePkIihRyxgcmcTLSsoRedNPm89fQLdkJ3Z3HvnIBZKgkHYWm0p3YYOg_dj1-7sE1K_XDnEjYE_N1kxBFzrsefGO-EK_moB66_VVd-rSPNs-4luLbv1_F89Qo6WakazGbS2N1lPIw2k6bGf1nXNo1SG77Co9CNjDADPjpouX8E0ycP_n3xsvJFx9GuufUqDyERQC5sKZn_R3cIjNvJnicPAert9diCtBw9xYZds7QNqTxBlgHFPdis2DSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
«سال 2003 پِرِز به خاطر سیا‌ه‌پوست بودن رونالدینیو از قرارداد با او خودداری کرد»
+ بازیکنان رئال مادرید در فصل آینده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/91266" target="_blank">📅 12:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=VtEByax7j-CQu25aEfj30uK36aWDQ4h1mZSh510axRHre_JD_mjr-VoeqY8pzAIf-myBLWwpI1oZg9dBR_-Mry2jMkSLje1wGQjS1R9NMEFw2XnX9GCs1nTAj8QUfw4BVP0hGPmvhOzRHLfKr6y2rNanwuWw-QmNZJNaa5yoyMmVedl0kcyQMkUF-YdMcA1NFouvkqh_u6zqrDmE-wy7AL-tdTVGDUrRmob-YgEmz88HJuFrxKArvCwC39fgfWNmhBn29CukJfP927UNuw7JO_xZGPkRwMiH6Lm2kEKaO6C7gTbhMv8SvsKaPtXg37BR-zfRNGAaCiSOHfGiQSwqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=VtEByax7j-CQu25aEfj30uK36aWDQ4h1mZSh510axRHre_JD_mjr-VoeqY8pzAIf-myBLWwpI1oZg9dBR_-Mry2jMkSLje1wGQjS1R9NMEFw2XnX9GCs1nTAj8QUfw4BVP0hGPmvhOzRHLfKr6y2rNanwuWw-QmNZJNaa5yoyMmVedl0kcyQMkUF-YdMcA1NFouvkqh_u6zqrDmE-wy7AL-tdTVGDUrRmob-YgEmz88HJuFrxKArvCwC39fgfWNmhBn29CukJfP927UNuw7JO_xZGPkRwMiH6Lm2kEKaO6C7gTbhMv8SvsKaPtXg37BR-zfRNGAaCiSOHfGiQSwqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
پشت‌صحنه تصویربرداری جذاب از نروژی‌ها به سبک وایکینگ‌ها؛ ایده و زیبایی 10/10
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/91265" target="_blank">📅 11:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNnZTsgfKKV7nN2b3PnSdfe7xuNkZ-TMAlV8QNALBJ5TVJN6upmhPBTrcMvSeV7Tk_AJXMmNBHVK4jTHGLuJcPrwMk8V0H6fVAUd6_ZR21V6eF_liVupFCMhUIkKQkvNk_5Fw3lHuhtClBYEzroNzwG4cE0fDijaXHunpAeghThM7xw_4_SUQMrjLagO5aSwGgpEJ_4-C5KPPVCliQGfKodH61rbKu4gAOudhZMN-dxkg6agSgU1MCkiT34Akx8L0eQDZNefqHBr30eFmQ7vV81mBrg-nBCilXMth0ZNSoLC4mSGHL7lHO8Ba-nWZ1oQeQydrcca0ppJk_fEo4W69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ قرارداد جرمی‌دوکو پس از جام‌جهانی با سیتیزن‌ها تا ۲۰۳۱ تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91264" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSLtW-5--bmpR0JgJf3qo8gdeUQURpHPBMzBlHYqcLi7Rs8nXgh-koj-ruPUj5Dqf06XMthPZRclOE0sRobvwACCo4IUidEWuyYE7MiQXfGI7HaoWkA5R_gWzMP1ajskx5lzksK22mqDtBfE_r-4b-Ek-X5XMEpWmHXxE9vQlOrMkdJnIpLI_x5WWsdXDyQkQEKrdH-DxfIok5K_yVjGUIc9gLl_4GFLKlrxN0jCJT9cWwem5LueWTkJD0Dm8KmIO3bcovozzXJS8PUJHNdog41oEiBP-I5W3gMrwvl9iPjOk_J0Oolj-jI_jnvV4IzJpxRJqXHxdEUMsQX6OhKnDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Milan 2009
🙂‍↔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91263" target="_blank">📅 11:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
❌
امیر تتلو واسه ماه محرم درخواست مرخصی داده که بیاد مداحی‌ کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91262" target="_blank">📅 11:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGspSN1BeyIQZSUSUn7A-A89-wpVALbRiAq9r6FlhmP8N9ku4y77zrFQmNG266LkWXnfK6-3xG8Qxn86cTjw60VI9y9OjxEM6JEMztUdq4GO7v-oEITsmP2QO0KuzcBYI3FqN08WWDZYKZFvEIXIPxDjCrscgVB8vvrz0bc1oW27z2bkWI5W-SI-fiHF3948To3146FTJ6pwGhRx4jxfv5GztXUvlkRPtp0os5bWUvEzVMTJC3w377dmom2PCGqAzbj7hdZBlIwNE0lg0eTHEzFtzFmUZLnjFMC5FQkqmqy7mcGFvxD-D5VQFR9DncOwV-kUtOCz6vyglPPsZYjgDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RhTqvPoFjoLwkbxq7SasmuUzuAtF6epoqtPRl8s-cnacKE-HN82aQG7_Q9EmRWQoSuxDE5Fi9ujeWpMbuzUoKdTK_6ocAcuLMtnLKg5KQO5yZUkqI8pMeBkG-SHQKNz36aTwYUI1uFK1YmlSVZiPBnGKXgPg-4bHvLxrLn3Phw_SEBUUkmGwdkrkBBwPP5yh3qsdPBiu2Ci2sG4bOmPXY_-xFpuPJVk1wKgP5tyNlALw2GPkrZoDwRFW1EeIB4ErZlNKp60pldiCOupdxboT2LE5sskv0GHjfWRe6dik9kbX9FasKYSDWgu3txX1f7PZexrk3E-Phj3e0v1JRf5MiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KntwEHlZWgEWuPCHF-usB5Te2Z2V6dndpwE919bPqDZlHFLOiGtbmJw08InaCoD-tufMR5_q9uGyWlk_guIU38AOFE18d5UJ_zce1icFF2V1iFCnEmiMSLd0clYi2IHRkhb57qpWHnWvGf0MpEswEBQTTvaVM3p_Hsz1tjEwIkYin0oRROwdCKApxo30T0NoSY7lhTUZ5_ChysCH0wejQKwWD9dHnUuRxWLhcQZDUew_9EPftrDJRg3OKUeSNBp3dx6AY_6haIjKNT-1Pipcul7buq73F2EtgpacADzpVLofCAoLu4AxRHoKN_jwr5s14TD3MADX0v-mmgBChGDNPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسم ازدواج عمر مرموش ستاره سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91259" target="_blank">📅 11:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b13497284.mp4?token=LNkEAaGgrQmTDze3eRlPCUVofVPkcRAeZJFBls3AvV5u0R0vQ-CalN34kVeIrHnJkBMgJyHF8hCAeYC39ibSbG5q7pM2GeWS7B8FcHYkAu8e88bY-hrOEYgDhsFi-V9RR0ufUqDKYoyriIfF-_SZGsrgt2mCczB9xliUxdBPcp9t-Ge24fNrNDbuN3TE80wLHVC-08JRRcE_l0NC_RHsSH1XJOa0nq5CQXyxfhFKEExjHRJSAVbTCHqpQKo0giulScUTQi8xWxToAp2X1ze3xQuPtdRLOEounpyy-paaDzqzeuKmECsHdRoaKbIJGRpR3a9TsTn8MmYBRNPMYUYoq4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b13497284.mp4?token=LNkEAaGgrQmTDze3eRlPCUVofVPkcRAeZJFBls3AvV5u0R0vQ-CalN34kVeIrHnJkBMgJyHF8hCAeYC39ibSbG5q7pM2GeWS7B8FcHYkAu8e88bY-hrOEYgDhsFi-V9RR0ufUqDKYoyriIfF-_SZGsrgt2mCczB9xliUxdBPcp9t-Ge24fNrNDbuN3TE80wLHVC-08JRRcE_l0NC_RHsSH1XJOa0nq5CQXyxfhFKEExjHRJSAVbTCHqpQKo0giulScUTQi8xWxToAp2X1ze3xQuPtdRLOEounpyy-paaDzqzeuKmECsHdRoaKbIJGRpR3a9TsTn8MmYBRNPMYUYoq4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
امی‌مارتینز دیشب حوصلش نشد بره رو نیمکت آرژانتین و شروع کرد به عکاسی از بازیکنای تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91258" target="_blank">📅 10:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91257">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea9b401d.mp4?token=PBf2MfxHIYiVU9OfbucUYCu_CDs-CgXDN9Ja1iWKIJxFPccg8rl6_jvmg9xywfePBdzjXSd4V4-QVTXTIj6ccSvs0VTvrcWwKEGQfFz9dQbKTtcX8h2tYo_GVZOiy7gwtvNzi89jW08YpPCqMsoiPlTOzNAgm3qRTtoXgXQL8yiz6fJJPJBokzbuIU0bovMcO4C2vPGKUfgAJSWaFv1hbwoNPQWc38kSG0H_63FF5iuDwArhba--rdUiz7ICJT7ayXPYtkl4fQ3jYz7ge9xqGngZZUsrkDRRI-m9PA3JNnaui9iVigvn5i8YOf-uJT1xV4DimQxBhGOux4WF7HfTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea9b401d.mp4?token=PBf2MfxHIYiVU9OfbucUYCu_CDs-CgXDN9Ja1iWKIJxFPccg8rl6_jvmg9xywfePBdzjXSd4V4-QVTXTIj6ccSvs0VTvrcWwKEGQfFz9dQbKTtcX8h2tYo_GVZOiy7gwtvNzi89jW08YpPCqMsoiPlTOzNAgm3qRTtoXgXQL8yiz6fJJPJBokzbuIU0bovMcO4C2vPGKUfgAJSWaFv1hbwoNPQWc38kSG0H_63FF5iuDwArhba--rdUiz7ICJT7ayXPYtkl4fQ3jYz7ge9xqGngZZUsrkDRRI-m9PA3JNnaui9iVigvn5i8YOf-uJT1xV4DimQxBhGOux4WF7HfTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">30 ثانیه از اولین بازی لوکا مودریچ در جام جهانی
و حالا اون آخرین جام جهانیش رو به عنوان اسطوره کرواسی و رئال مادرید تجریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91257" target="_blank">📅 10:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91256">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a80a11077.mp4?token=ul-_hHKLlTWeW0mEa9hbMESS8syG-SxotNLsFsquPHHxXXOnX-Sl8vPqj8OfrwjJYo-QrMHDCN5897Z63oJGGMv4KAJrRgcZBb6WCS_Zohl9AqAWserXp3BFgXGw4NOH6kVFp9uIWFtblt3Ib0emh42zBjfRGu8qMD8te9CzZvwQe53ZEmPHnj50HYZk9g5c5YJCLlE15JakWeib2MfKsUQCfUnEqGYM9fYFQLK9B9wShk9M8oYen9B4xuiQmw25Sb7GTPRIi2pX9-X92bRZsIWQr3SiThy4DxtRodycOuXSEiYb_OQkiqnKeUBUS71e-lTKtqDl94nKA3m8rbI8OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a80a11077.mp4?token=ul-_hHKLlTWeW0mEa9hbMESS8syG-SxotNLsFsquPHHxXXOnX-Sl8vPqj8OfrwjJYo-QrMHDCN5897Z63oJGGMv4KAJrRgcZBb6WCS_Zohl9AqAWserXp3BFgXGw4NOH6kVFp9uIWFtblt3Ib0emh42zBjfRGu8qMD8te9CzZvwQe53ZEmPHnj50HYZk9g5c5YJCLlE15JakWeib2MfKsUQCfUnEqGYM9fYFQLK9B9wShk9M8oYen9B4xuiQmw25Sb7GTPRIi2pX9-X92bRZsIWQr3SiThy4DxtRodycOuXSEiYb_OQkiqnKeUBUS71e-lTKtqDl94nKA3m8rbI8OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی تاج: اصلاً برای ویزا درخواست نداده بودم که آمریکا بخواهد به من ویزا بدهد یا ندهد؛ خودم هم کلاً نمی‌خواستم به آنجا بروم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91256" target="_blank">📅 10:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91255">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇲🇽
صدها نفر روز شنبه ۱۶ خرداد در بلوار «پاسئو د لا رفورما» در مکزیکوسیتی گرد هم آمدند تا رکورد جهانی بزرگ‌ترین «موج مکزیکی» را ثبت کنند. این رویداد به مناسبت چهلمین سالگرد مشهور شدن این حرکت در جام جهانی ۱۹۸۶ برگزار شد، اما گینس هنوز شکسته شدن این رکورد را تایید نکرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91255" target="_blank">📅 10:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91254">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
😡
هواشناسی: امسال سال خیلی گرمتری نسبت به پارسال هست و به طور خلاصه کونمون پارست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91254" target="_blank">📅 10:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91253">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇪🇸
دقایقی‌پیش انتخابات رئال‌مادرید آغاز شده و تا امشب مشخص میشه که ریاست جدید این باشگاه به پرز میرسه یا ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91253" target="_blank">📅 10:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91252">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e8a50238.mp4?token=d8z5TW89E_QF_KtQFea59UUmHFb2R17Hrt3bMR7obKulAgGFSHOgydBk-r4IirkkdKkllPKoT0ul5q6wkTtmHjElB9a2i6R-sNhrhw02lHStff7-hnokmmWlODVvPbaWzPUalWu867mGqYEcVPuQ3KJrmf0_DCxjtAbh6WmoIzmb3YXj1CzDonIIDzzIvHRsUrWr1VM5oLy1lVLqUyJjzd9k30kS7iDJFq8VjhXQvhIyr_q1FIPDzSkpdgiZ_iEpdcDhHciASQ_c9oGkECTsPmfGMk2PonU0TBJzlBE2Fc5vCbLTezgzTZX_tA1_hhbl6cgKFrjEzB1yW1kbQBeKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e8a50238.mp4?token=d8z5TW89E_QF_KtQFea59UUmHFb2R17Hrt3bMR7obKulAgGFSHOgydBk-r4IirkkdKkllPKoT0ul5q6wkTtmHjElB9a2i6R-sNhrhw02lHStff7-hnokmmWlODVvPbaWzPUalWu867mGqYEcVPuQ3KJrmf0_DCxjtAbh6WmoIzmb3YXj1CzDonIIDzzIvHRsUrWr1VM5oLy1lVLqUyJjzd9k30kS7iDJFq8VjhXQvhIyr_q1FIPDzSkpdgiZ_iEpdcDhHciASQ_c9oGkECTsPmfGMk2PonU0TBJzlBE2Fc5vCbLTezgzTZX_tA1_hhbl6cgKFrjEzB1yW1kbQBeKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
واقعا جای چین با اینهمه استعدادش تو جام‌جهانی امسال خیلی خالیه
🐸
🐸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91252" target="_blank">📅 10:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91251">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ffffee7d.mp4?token=cBphpIqxawAELF7QNSgc0z2DTqBFqqwfWRw5wIXl5D73wR2ZZUSpVLXZR4NyhdY0--ZFCWhdJKiMX6qjX2QIb6Xj3GlIif7xuW7rB23Nl-i6o-ABrsVBTH8DaM2Lz4edjzu6TWu0VvC8Gcs5Sm5ku9Zl-_ekeybIEqLGveJnW0O5S-Nck7dPRpp6r5qWhABmr63-ohid4347O7De4j17ePTrRa7k-vYP_RaBGZ2u7G2cNWTdCh_-5_-zzsWHhsbgWvS3bcsaiShBe1NP4Mao-_2E96oeukuScQLdy-kRaTfXEa1-xj0KjUt_uDbfvGmp9RcSXRKocjbAu-XxMnzD7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ffffee7d.mp4?token=cBphpIqxawAELF7QNSgc0z2DTqBFqqwfWRw5wIXl5D73wR2ZZUSpVLXZR4NyhdY0--ZFCWhdJKiMX6qjX2QIb6Xj3GlIif7xuW7rB23Nl-i6o-ABrsVBTH8DaM2Lz4edjzu6TWu0VvC8Gcs5Sm5ku9Zl-_ekeybIEqLGveJnW0O5S-Nck7dPRpp6r5qWhABmr63-ohid4347O7De4j17ePTrRa7k-vYP_RaBGZ2u7G2cNWTdCh_-5_-zzsWHhsbgWvS3bcsaiShBe1NP4Mao-_2E96oeukuScQLdy-kRaTfXEa1-xj0KjUt_uDbfvGmp9RcSXRKocjbAu-XxMnzD7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇳
🔥
هوادار تونس در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91251" target="_blank">📅 09:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91250">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f42ba19fd.mp4?token=dJBpTNdSfI0CtYG4Ziy9lEOhKVAq_h2Ie0t8WiET-BLgiyJfsKKtb3B9DfzJqHb_A53400qhYMljqZChppn71nEmnZLjbE_a9C_yrIHDyxljuiryUm2ty3kayNZ9iql0a-uI2xfU8SyHwYRWEIX5SidyWLyNSwXY9GtaEJBTYc8joQp74RvDiMFAs4fyunnoVBK9YEDHR6LK7F638zbAhSxuOWvGf-pCQ2PQ-mxPOCYAlsMRpfo-OB_3LGaXXbTGMxFsTWyqLqfme4ZHghXaiMC97NbkUskhrp22mes4zUv8XEx55_p8ZNIBlXJLXa_NFZo_ZZxduUaRS0id0_WlJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f42ba19fd.mp4?token=dJBpTNdSfI0CtYG4Ziy9lEOhKVAq_h2Ie0t8WiET-BLgiyJfsKKtb3B9DfzJqHb_A53400qhYMljqZChppn71nEmnZLjbE_a9C_yrIHDyxljuiryUm2ty3kayNZ9iql0a-uI2xfU8SyHwYRWEIX5SidyWLyNSwXY9GtaEJBTYc8joQp74RvDiMFAs4fyunnoVBK9YEDHR6LK7F638zbAhSxuOWvGf-pCQ2PQ-mxPOCYAlsMRpfo-OB_3LGaXXbTGMxFsTWyqLqfme4ZHghXaiMC97NbkUskhrp22mes4zUv8XEx55_p8ZNIBlXJLXa_NFZo_ZZxduUaRS0id0_WlJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت چهارم ورزش در خانه برای دوستان گلم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91250" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91249">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859cb5ce7.mp4?token=grpLZtiP00vYkYdTk7PGJVFJhQpWNK8rLC505gfgmVYeUvcYSkwGYPuhwbsPjqD5jASg3OJzJFpBUMzJp6LtPntvsF6PRCjXnOAPDghMjFpOc2LjifyRS0LtK9vZ5aQpoHIuxEPA2upm8Y6SQz1im6B3Y0X0cCZdDeTdYZCeKXNCuy6-k9_rISCwF7AO8brv7pJTUvr920NykrmaG1EarYuvW9U64cnx_PiV5AnnKFbuVCNCvZ0CSi_uZ2KPeQeCsKGiY1xJFQ9oqMwgqbmwAGPcgXFdwaWADXBAUWo2GbKD67z5rcEv2-l_XCkqvxGIU3OeXqtH-m2cXOdf8WSt0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859cb5ce7.mp4?token=grpLZtiP00vYkYdTk7PGJVFJhQpWNK8rLC505gfgmVYeUvcYSkwGYPuhwbsPjqD5jASg3OJzJFpBUMzJp6LtPntvsF6PRCjXnOAPDghMjFpOc2LjifyRS0LtK9vZ5aQpoHIuxEPA2upm8Y6SQz1im6B3Y0X0cCZdDeTdYZCeKXNCuy6-k9_rISCwF7AO8brv7pJTUvr920NykrmaG1EarYuvW9U64cnx_PiV5AnnKFbuVCNCvZ0CSi_uZ2KPeQeCsKGiY1xJFQ9oqMwgqbmwAGPcgXFdwaWADXBAUWo2GbKD67z5rcEv2-l_XCkqvxGIU3OeXqtH-m2cXOdf8WSt0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
به‌بهههههههه یچی آوردم عشق کنیددددد. آقای کوکسل‌ بابا برآب کشورش ترکیه چالش رفته
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/91249" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUDx3qP7aaDp_PfpFP5Ija3cHb0FCwLZ3QgjQ9Ki8TucBqicPjb1wO1m0-JVEeLHFHUTT7AkAeKlOpvsVG0Ka551lWFs8gHIAh0OQL5vUXY6w-kTSo6NDJJQxeMzHoBe1FFXH-2R3UVQr_Z1mHzryUU73RYm5_QLdh4qyRUmLO00RALyJ-o16uRLmaazhWaasnqL39b9fei33mY5oKr5jnJlkYHViomvuqiipQ8XJzsN4JkapstNNpAqnZmfavv8HbYpPBOBin3NaVDysn0yc_R2pv5V0UyBeUbU3rgq70wxYEvtcn5EL3mSCBhB5454qQYPRnuru7PGzS0qRI9Vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هموطن ایرانی صبحت بخیر باشه؛ در ادامه فیلم‌های هالیوودی که تو مملکت رخ میده، توی ورامین چنتا دوست صمیمی سر یه دختر باهم دعواشون میشه، در نهایت در جریان درگیری ۴ تاشون به قتل میرسن و ۳ تاشون متهم به قتل هستن و منتظر حکم دادگاه!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91248" target="_blank">📅 08:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0NI4Z01dycLXU_tR_maHSWRE4ZRFnrkfKVs1jIvnuEKSFua-jvP4yha3y4-AhiQclHdotcVHmttCmeCZPFUv_HT23XrVGqh2TCcsasmkMjsJge8layCXTPvn8ba6A02DJk6wO8_RJjGakASLzh6EsZjJL7jvvu3mGGibPNqmx89Iu2TyyqVmIeJKqsBL4NyD0ZVuDSBGH-gAOG4CwSNg32khkYqF602bD0oujXVrBpWr-G0kSXCaBWlSqH9npUraGHntTGoU0G5RDvwdMfan9wBDS0wLrxqZXX42r4Pbp78jL7NpaCsofqor0RhZ_hxbFggcWGE6Pkd4PrlKSrtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91247" target="_blank">📅 07:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=pQOt9SGT2mMxdYqRoGQzMFKdH62zQH92G7S5wF0i0jsLi3qh-enT7r6qLuBSF9AppgekoDIf0B7Idxv59tGCm9Q_e6mdTmQAI1vNRoLmT7qftIfRtleYTEqTZwDye3UWcJLTEbsx2BbBx1o8hPCaLq_IbJMqrECTV6-V2QDgWsuy0SKbmosa3nf1-GvRqwQ-a601548l12BgN5b4nhv26ySqAcuxi6YGbxvFRgV_48PYAR3r5gmEEPRGXs-TT8CCt015jwG7KvhLirV6iKnoIBRggtJJdMXWtJh04QGbua9uLYSXOwhFubY9iK0AsdJDcDPYG3fhn06F6MxF3-MXYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=pQOt9SGT2mMxdYqRoGQzMFKdH62zQH92G7S5wF0i0jsLi3qh-enT7r6qLuBSF9AppgekoDIf0B7Idxv59tGCm9Q_e6mdTmQAI1vNRoLmT7qftIfRtleYTEqTZwDye3UWcJLTEbsx2BbBx1o8hPCaLq_IbJMqrECTV6-V2QDgWsuy0SKbmosa3nf1-GvRqwQ-a601548l12BgN5b4nhv26ySqAcuxi6YGbxvFRgV_48PYAR3r5gmEEPRGXs-TT8CCt015jwG7KvhLirV6iKnoIBRggtJJdMXWtJh04QGbua9uLYSXOwhFubY9iK0AsdJDcDPYG3fhn06F6MxF3-MXYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو کوتاه و جالب محمدرضا سنگ‌سفیدی بازیکن تیم‌ملی فوتسال از مراسم ازدواجش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/91246" target="_blank">📅 02:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJbUyj-7RI6T0cYsS2tXY2doFr9eEFpbFGZNua7jnwEGGx2oWv3PcUOhwV1Rx1vRsxrh6G3p72OFrNekfsmfq8FTXg8HVsDaHKIXCbR2frZsPcTvIi9jsme_kVv0hrc1KS3CyJsr-86ViKvKUATSj4zScfEzDLPkce6INEjDt70NfnopkOhL7o_MFkhq7Bj_gMYMT99hbEE2svZ5cK9ximbKza2ffdfzoWMrvFLP5ZSiLoZBG8nFrybIRkIjZwytyieVqzJKYHCNhLVexcLRhQvXS5gs2JhouXSqj6BNHmN7mAD-5a3L3epnE2PVE-9dFqcZtfY2eO_2IKpZ60yTyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/91245" target="_blank">📅 01:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🎙
برناردو سیلوا: بارسلونا یکی از تیم‌های خواهان منه. چند گزینه خوب دیگه هم در دسترس قرار دارن اما در نهایت تیمی رو انتخاب می‌کنم که عاشقانه من رو بخوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91244" target="_blank">📅 01:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBKySLjaeS3JdHy4vcBXpN8G6aSXDKcJvmVOKexab77j7IRC_Ize044uVh_RqqLcjcFiw-X0c6sjCHniExwI5K2bGbm9Hyaddap8P3px5O_Iq7pdT-FmL-Kx4pcKSzJL-ab6jTraGLcawB-uDnUO5PmQJt5q8_8rGKO4sbFyYppbb-8sqye_1L6iRiMnExprlDe5hlOQ0LiBGE87opkGf_t-wFX4QjwIzksWXiEybLPn6CSw63sOlWbHs0xxfsByBZe0CiCVHLN5CVMgz4mVNdY4eDj8oJ6FthRwbtCWWLDSIyFGKyI6ehqygZzXH-OmnN9llaVoRP-hbsunZeU3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری استایل زدن که انگار نیسان رو اسپورت کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/91243" target="_blank">📅 01:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42162246f8.mp4?token=H39sUy-BwSs99EB-UidNkCOOpwpNse0-tXEp2HPA9od-XW30EBRwCLxJocIPtPjnM75r9fqCLTX-lJXSLmPqfeMqbwKCzxSi0kyB27cwOzPGaFoYcFxZ1iCKIK2-xL8ihEQyhVFPQWBCyqnzNSI20nWfFDTaE_duu44Q1-fgN1G14PFEHilzJZSk7nsApsKjKTr5eIdFOuBUTjPzNdb0uzfduYVLN9bCv8XdVw_b_HNZkgEvzYHCdZuphwqu_Gjr9TybeZ7p5cJRW6qnmWzGkh8DzKfIDu5y2HhPk2DTHE-w_PQGVC3POGHnha3GfrQHfSG5ZfiqH8vB48YU7aoHo2cQAb3FKUpjCUdNJI4Us9xw6a_Rle9u6_iVcDAzjkjeLZg9T5GGRAzaCmeMVe4ipS0Qxv8GT1r9c-QEXkww8UYyfznjPqPPLr6vfoGVJGsHEoq9gWIXwQzF2HUrgLU7rQLgzvGBtEOcEvL0Pyk0Re3ajPENAW0qJPaLhFCIndDbRQv06ioo605PRvjcLsTT4kEigrElD0LaVE9ZLNiRH3hXveQx4UCdBcZ1X3wKlhpg3WzXmFgv1erEMXQ5ks9P83F__3KPozblTF9KTuzVW7wth35Bcxzqck-FtZWFpZYakUHxxDxVaY_5HTcx7cmWzsmu1WBTmVjh2e0baAP1AOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42162246f8.mp4?token=H39sUy-BwSs99EB-UidNkCOOpwpNse0-tXEp2HPA9od-XW30EBRwCLxJocIPtPjnM75r9fqCLTX-lJXSLmPqfeMqbwKCzxSi0kyB27cwOzPGaFoYcFxZ1iCKIK2-xL8ihEQyhVFPQWBCyqnzNSI20nWfFDTaE_duu44Q1-fgN1G14PFEHilzJZSk7nsApsKjKTr5eIdFOuBUTjPzNdb0uzfduYVLN9bCv8XdVw_b_HNZkgEvzYHCdZuphwqu_Gjr9TybeZ7p5cJRW6qnmWzGkh8DzKfIDu5y2HhPk2DTHE-w_PQGVC3POGHnha3GfrQHfSG5ZfiqH8vB48YU7aoHo2cQAb3FKUpjCUdNJI4Us9xw6a_Rle9u6_iVcDAzjkjeLZg9T5GGRAzaCmeMVe4ipS0Qxv8GT1r9c-QEXkww8UYyfznjPqPPLr6vfoGVJGsHEoq9gWIXwQzF2HUrgLU7rQLgzvGBtEOcEvL0Pyk0Re3ajPENAW0qJPaLhFCIndDbRQv06ioo605PRvjcLsTT4kEigrElD0LaVE9ZLNiRH3hXveQx4UCdBcZ1X3wKlhpg3WzXmFgv1erEMXQ5ks9P83F__3KPozblTF9KTuzVW7wth35Bcxzqck-FtZWFpZYakUHxxDxVaY_5HTcx7cmWzsmu1WBTmVjh2e0baAP1AOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
به‌روزرسانی شبکه World Cup HD
🔴
شبکه +Mifa از مجموعه GEM با هدف پوشش برنامه‌های مرتبط با جام جهانی ۲۰۲۶، با نام جدید World Cup HD فعالیت خود را ادامه می‌دهد.
📡
اگر این شبکه در لیست کانال‌های شما دیده نمی‌شود، لطفاً فرکانس زیر را دوباره اسکن کنید:
Yahsat                 /          12034 V 27500
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/91242" target="_blank">📅 01:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
#فوری از خوزه فلیکس دیاز:    ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91241" target="_blank">📅 01:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmyXCkAcGTZyy2VeQeu7ca71JaZS13pnj_mbYWXvMrWnnwPLg_nIQzYFzGPKOO-Ctd9Kc_OTt448CVY5H0zZnDBLVp1Xid2fx9nGzHfblmfmp7yhAYiauIxKVwx1nzuBjsWzNwh1V3vWhZgrckBBDDI4mKAQM7jn4PM7L3v9hrTSPVlQkTA-c7EqeSayMGELxhpwR3FuRKOcxu-x6R4GHk8RjjsheUQfF_c8AbQUmFZF0ts063L-p2Y_tK1ctcQSntsVQM5aZbIH0tPTvWzp21EiUXUD4ByH8C1zpuYDaMRmOHsszlS9F6ozaWo3HnLoFVnKSc_u8FWhZVs6adggpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
از خوزه فلیکس دیاز:
ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/91240" target="_blank">📅 01:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-wZGjnbnmS5jP2HMEVUDKQOFIgkS5pZIX5T3X9Ga8gZINgZ7I8Ey0_y2WNwvtUp40L_pIlqZtDrMKDtV1DxbkSZAG44Mcws7g_pxemcQs9wUzFYkifVNvlleYSvM2ND9oMjLFbRKkbBkIrPM6-AoWjZ3K00tRzKr8IGQhmwsw0JbhH-t4ANFuLQB0vzCn3IGDuZYOpeEgVruvB4Un3ucL9k-0Xw3jLSCeO4r3zMkyrCS6aC-7rK8eXZstSVSh2Yl-QOY7lL6jT7RbF8XoSWoCUOqidLjE-Gq5v6vWZ8Q_cnjli-UI5-wCaD65S1BfH3f_pAI7L6pV9cBGQNdALGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 روز تا جام جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91239" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=PoBiHCCAuJuVc2Auq23LLTQKyzk8Uxzf5h7kAuYxyM7374tqzW7NFWSKTqFSwWwNt6Q8IIt8XNVTUuIV7U6TK_7ywd7vKed4Uow12NjJkE7OQavZvgmDuMUR0xN3W8MheoVpvoVgGW8z2LI0NZ00Bnvj1HnRti_hT5xQvj8n3QtUVRsh_voqq9EkqLsfzKRgxh3FOY92lUiRyioezwmAeUUIprYvS_Pcgbf0_rvvmHGtISLZA_omOrsBySvNDr9eHNphbbH_BK79oIWzKHVfuieU9FFq2gRoQLfMSpmnhUYTB78gh2YmMSbZ5FkHqDcB_5kQte-wK4lLCteVxaJlMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=PoBiHCCAuJuVc2Auq23LLTQKyzk8Uxzf5h7kAuYxyM7374tqzW7NFWSKTqFSwWwNt6Q8IIt8XNVTUuIV7U6TK_7ywd7vKed4Uow12NjJkE7OQavZvgmDuMUR0xN3W8MheoVpvoVgGW8z2LI0NZ00Bnvj1HnRti_hT5xQvj8n3QtUVRsh_voqq9EkqLsfzKRgxh3FOY92lUiRyioezwmAeUUIprYvS_Pcgbf0_rvvmHGtISLZA_omOrsBySvNDr9eHNphbbH_BK79oIWzKHVfuieU9FFq2gRoQLfMSpmnhUYTB78gh2YmMSbZ5FkHqDcB_5kQte-wK4lLCteVxaJlMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🔥
پیش‌بینی مارادونا از قهرمان جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/91238" target="_blank">📅 00:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5l96xt1_KhlXRJEuL7027sQYlvoLnL9z3JoSFxaOM-cNCE-Mvwv8NvhkoJ0Dk87G5y0EE-66LWH6e6jjKzQuNC9QSjbl48m7PzheyCAoO1Y_n-KcTaFofnYLn36qmY_pzf4AzEeBfds1_cnDrBXnBFAHpQjUtUDbgp6jzkN4Gs2oYkC5VqwH1Mjrzu6N99zYaiRpwtK4US6Ku2e75QovsgPo4utqAhH6KGgrHnYfX8VBpDbHOSEzU98WcvnL4eu4pJJs7vP_EHdWFhaVi4KZZl86uXUiccaYvy8SUOX1iW5Y5W8lFGmV4_CjTbsnzL-ysQ60M5MBjNHKRzpgnFQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پردرآمدترین سرمربی های ملی حال حاضر جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91237" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daZuOTORkQVzoVHbxKbenn8NC0RZb0c5QdEWv2PLcQEIzYRsMeHfwsPX9i7OPWOLKiYcP-56O0HNViwUiWO35PuAWXFrlDIbh1TWOmZV18WRx9pAzTWnEzbzsXYWex-SpscjacIkbSjaIyItXd2lokm3jM6h8APpLUJFtCpUl7qiC31eJIwo6f2-oAnpEOQqSNPwqdpzfZQyaenPPhJ75Hb9TQt4hsp4F6AgEtWrmkinOt-YMR_rGP-1zGDL8FOt2ufTt2GwUNRjHCYX5pEB6vgs8lCD9VSShYb6NHADRGDNASyTVcIRKDC625vH9mbzB2XTxqAv_fJVB6iTb9Fe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیلور سوئیفت و شوهرش قراره یه مراسم عروسی با حضور هزار نفر بگیرن که اینم قیمت بلیت جایگاه هاشه، ارزون‌ترین جا 8035 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/91236" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇦🇷
#رسمیییییی؛ مارکوس سنسی جانشین لئوناردو بالردی در تیم‌ملی آرژانتین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91235" target="_blank">📅 00:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSqujZ1vZwjHGSXUqzlcP_xS9dg1bLJe_CEW-eMOKDwZWa1IAELjITisMjH4a7dRO6A64GObjjU3dxFGcY2mbYSy_V2ZIs29OFqTzAre1ZhcCqoDqJ-2j8LT2k_2_VjY8S1t2X1GMueZJGUhro4M2PGnpt6K6Y9ihcaNssbAiN3RnGZKxVwCX1bmwkumT1jn9_JwLvry7xZHNzNR5DOwDi2TsctoRIct2LwMwFuAEGf7B1qMIWkOKBRv0SrzcY-cV1WIxNkYt3Zn3GZtllYbH5ywu5ynVMEBClxOF1au9maM-kpai5SiyJ48CVbPdXN9QslaaWjLMvNxGJ9UesM0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
اعلام ترکیب برزیل مقابل مصر؛ نیمار در این بازی بدلیل مصدومیت غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/91234" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=iHoE21Nz9fYNKh7SzOAR-YHXdTZ5-nGG4eTtUNGMiojdZS2ux9jdMT9TDWTc8Oby-wtUNA-o6rv5TwU1fp_2Ue6ppEpc1ujvk5doXCxdys4x_8GsMn30wOqmUHb5n0YkDPlhm4PexiNQxdWL-sTXxeQEIYRk6PVkpFUUXZxl3PB--9vu1d3q2wDmjPZJFW8VNa8M_TdMiLBOqIzoQDfAWOXJxsCdvg-FX40fbcKqXrKyVMGBpUFYQWs4Wy8U71n_0mhA69PNqCK3lmta3goIYxA30shwO6PY2UC-mIgn7w1JmjaZI8XEckJyv57hIe5aZt1Jp3VCdJvRH1j6JVOW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=iHoE21Nz9fYNKh7SzOAR-YHXdTZ5-nGG4eTtUNGMiojdZS2ux9jdMT9TDWTc8Oby-wtUNA-o6rv5TwU1fp_2Ue6ppEpc1ujvk5doXCxdys4x_8GsMn30wOqmUHb5n0YkDPlhm4PexiNQxdWL-sTXxeQEIYRk6PVkpFUUXZxl3PB--9vu1d3q2wDmjPZJFW8VNa8M_TdMiLBOqIzoQDfAWOXJxsCdvg-FX40fbcKqXrKyVMGBpUFYQWs4Wy8U71n_0mhA69PNqCK3lmta3goIYxA30shwO6PY2UC-mIgn7w1JmjaZI8XEckJyv57hIe5aZt1Jp3VCdJvRH1j6JVOW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی داماد فوتبالی و رونالدو فن هست و اضطراب اجتماعی نداره. خداوکیلی حرکتش شاهکار بووووود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/Futball180TV/91233" target="_blank">📅 23:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyk-1HPo5aWzVrkaWM_WK1nw2NL2ivQkULlEJxcMe-_eXHW3IcxzEiC75cLqs1ADicEroBmHp0e1pVmPHAkMP9yGBczDajE4z11DZSkAFyo-m59PmL2YpzqMKN_HDsUIqY15uO2t_171EroKFfoNd7FGScYZ76fXiIqrl9yHJ87TJZP6ZmuBif36n_z5Fy1qqDBycXpOuh7i06xIB4WrNcnKEZ2DUItWvNx2xvmO0NhWZct7GpnWzQK7sON4zB5B8zzpd88pnr00xZC3icHo-YH--_xdQu8vILswTDVM5rl4FrKTvaI51pYWB9Oi94IVx0tXgDv11OJaDsr5IFL80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
مونا آذر پورن استار ایرانی هم اعلام کرد که قراره به کشور برگرده و مجوز داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/Futball180TV/91231" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=a4FZp9ZEKeMrHJy0KuWdhMYjqCjYVvyQ2k9snphmBGa505XfiqtiyC2teHs42zYVc6KNmRGnWG-bzqBz4vlW5bT26Mx9TUkjBVizfbVMo_kQ1Q_A-NfUoLATzILWSjOet6J6VASdNa090R9b6f0p2feikMUN4xeEoX0SkGkftoo81WIoevgEYRKTqLYJbtWpucleLIgCVcHgI0iDNhHbJU_NDiG9R8ucW9xITv3wsRFYSSBuJstNGMFK5SkZDzNvvJr4QK1tD6vmsEOej--9Q28F9JB95Grr1nvmqIfMyU4Q-PZRD_U7bF1_lLF1evO2QQOv5FfkuOUvvQJ2d4Cymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=a4FZp9ZEKeMrHJy0KuWdhMYjqCjYVvyQ2k9snphmBGa505XfiqtiyC2teHs42zYVc6KNmRGnWG-bzqBz4vlW5bT26Mx9TUkjBVizfbVMo_kQ1Q_A-NfUoLATzILWSjOet6J6VASdNa090R9b6f0p2feikMUN4xeEoX0SkGkftoo81WIoevgEYRKTqLYJbtWpucleLIgCVcHgI0iDNhHbJU_NDiG9R8ucW9xITv3wsRFYSSBuJstNGMFK5SkZDzNvvJr4QK1tD6vmsEOej--9Q28F9JB95Grr1nvmqIfMyU4Q-PZRD_U7bF1_lLF1evO2QQOv5FfkuOUvvQJ2d4Cymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
گل‌تماشایی برونو فرناندز مقابل شیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/Futball180TV/91230" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q07qLguzus-NASIdEqV_3KJVgN6C8I1O_KMAGLY3NHpB_kJyYsXSanJ2Ffaw2yeJa7SJQIkpKHza2QMx1jmKFXmzHKBFilRl03cDJviL_bGw5HNCik9HS9bcyyJH_tXeo7dZmURuooRwkJf4BgY7ntF_hYzTrq531EzNmaWe2LtaSSULeLUU0kYfjrEjnU4j4d85IaGitjO0fGGhS4_8wNfAqmvv8kaEyclJ7U-utTzYaaoqkrlrnUESfTXBXXn1kqa2uprlkFvV0-3y69xySeLT5B1txcZ5DNbAAB61VO6rvJmb2PA3VAhWl6e4iyhSqrB9G1NOP-sPUhDLb84VjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وقتی میگن پرتغال قهرمان جام‌جهانی میشه
همون لحظه پرتغال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/Futball180TV/91229" target="_blank">📅 22:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=e7vSW1Pg-YdTz6W40pDFEKQJX0aVj_oT6PvLuCcY8xOtPujGvUalwxhEWpMt9VGaZ4mMAT_szI9stekDOYVNoKVStgfifw6R9kSdG38jZYQrBr9jKp6pkQIWEoKGYywZyPF5E84Qw7ICX21TlKm3fKuMlZEPLWgBucHmQbR-f7FfXOhflRTBp27ZPtKvjzse8G1c-1KMLuPCISEe4KHUg1YJQlIoe5eewbYpDUAFWCjnIz2Ne4CppG_cogIW2eyHtzYNog0hm38_vtZixRMMTQeVwIZ8BpGwCKz-0gcGFT5we_OqwQSNI_NfPth4H7yPNJkWOdm10bav98GfcSMFWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=e7vSW1Pg-YdTz6W40pDFEKQJX0aVj_oT6PvLuCcY8xOtPujGvUalwxhEWpMt9VGaZ4mMAT_szI9stekDOYVNoKVStgfifw6R9kSdG38jZYQrBr9jKp6pkQIWEoKGYywZyPF5E84Qw7ICX21TlKm3fKuMlZEPLWgBucHmQbR-f7FfXOhflRTBp27ZPtKvjzse8G1c-1KMLuPCISEe4KHUg1YJQlIoe5eewbYpDUAFWCjnIz2Ne4CppG_cogIW2eyHtzYNog0hm38_vtZixRMMTQeVwIZ8BpGwCKz-0gcGFT5we_OqwQSNI_NfPth4H7yPNJkWOdm10bav98GfcSMFWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
سوپرگل تماشایی آمریکا مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/Futball180TV/91228" target="_blank">📅 22:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91226">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tJL94gWq6q9M8W8cyPS7VxNTn1wGTuuZKBGGSOY_jx-UDzRAZRvLKLeNrskBWF1d2dNhp0X9mfO5MTBpLmQp0wLTsAUx-qHliPyilNPpBSU9scuGBOz8Defy3wZ3gz5pq3yaHzBsIwj6XHwjHXcYf99daOh1ydxW_OZf5B9KOYmKJlWP2EFh3PaYBKUUjUb7RhAHyO2K1wS_BfrWs7J-hsGm_sdm2Y3DZv2o3b_rDvGuCV_-gytoAnk-Kc0I4-QtVugdkvjNvKV31TgxKWpKBOcFtL4HIr8Z7xwg37jry4LRekyDS5vhiyZz2xYavVCEwGAzVtmyLmYklzxHiwEnxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7G22MYqA3dbYIVdKAeIoN5A85d5rkSx3iDS2GnYAOXMvTJiVWtE7T8rtbZEZjZrwAKR4OW_y6_wyqJdJoGs-vZHa-Hvf4iQYya-GgGv0Ztzuqi-KA0uziwHj6mLWyZcytNbNlJD3_adg717o183H3fPGSeSdRp29M5W-YQ001L1-sSXKW1QGs-R1m49gqF5N7MK-inonm9F9gB-jo_y1wvJrwW3w1QlMoTPL1jVkallLU2nZbTZMzcXVC76qmFQWZtpJc3bh9ak0pbftFPj05pJviFjaz8PncuLPIkqvXTVjoouIvXdYfakENFnjhErPDv7CjSmoBk0V8GGf8Y4vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
🐸
ضمن عرض تسلیت به برادران سرزمینم ایران باید اعلام کنم که کراش والیبالی شما یعنی خانم آیتک‌سلامت از خوبای والیبال بانوان ایران، امروز رسما و شرعا ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/91226" target="_blank">📅 22:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91225">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkRVpb2iHLS7_s88woSYOAIuyh19m4wRXX04lLkcppHsathTfZtOwD3AiyteAHRF6GPzKGQDw8N6MqgPwt1pV9w1Bu3yKtC7MY_TwR30NnEOmcfNtlHWrxptZtaXjKDsrliCW4f4bDWR3y1T_sPGr2qCj8o_RLxyi77SaZJt-GIHNhOqd9IgYwI6Kw0xR-30NDNMA34FIBaGctucUhrVlUbtDXOi3yV_pcITyYYitFZp3p9xietwGXaPE7wX30iinDiIKveWK0Cjifen6VcbaRxQdwsq7lrcjl-QElmlC1YoQwGsokLFBZm_Okj320IhVEmzB_7-fTMbN09eyLxJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
شرکت EA پیش‌بینی می‌کند اسپانیا قهرمان جام جهانی ۲۰۲۶ شود
🏆
.
⚽️
• این شرکت از سال ۲۰۱۰ هرگز در پیش‌بینی قهرمان جام جهانی اشتباه نکرده است:
• ۲۰۱۰ → پیش‌بینی قهرمانی اسپانیا
🇪🇸
• ۲۰۱۴ → پیش‌بینی قهرمانی آلمان
🇩🇪
• ۲۰۱۸ → پیش‌بینی قهرمانی فرانسه
🇫🇷
• ۲۰۲۲ → پیش‌بینی قهرمانی آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/91225" target="_blank">📅 22:41 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
