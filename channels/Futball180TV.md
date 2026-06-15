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
<img src="https://cdn5.telesco.pe/file/nsTl0sBdmqKtcYk2XxsvZzO3MDGr_0MmKNM2vPW6cUdNGivhTgOpC3D2O9WdMpTfXkxdy_X_3YHCtxsg9MGjBc_AITRIpG0fpJeWJ7mJa80CHfXAosuk4tpgCaSW7YKyE2NIkkcL-37f-ZrqH_ROAk3NZfOmFsd-8ZR9MiVuRYefRGDilIMXPobAyyzMr7v_s4K9Kee1rYPETDpAyThQnwZwL1tr3HwJky8Ha9xBUCaCRkSux18tdJ5eD-sgN8wDLjdy913hrksyJkDjR3PoHvJ-fy1cy65iog5x31JFVW67Udi9RmYhYdAGnOB6Ga3IiNbPV0NyLyF4p0XI5j3AVA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 577K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 01:29:10</div>
<hr>

<div class="tg-post" id="msg-93380">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کم کم بریممممممم سراغ نبرد اروگوئه و عربستان</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/Futball180TV/93380" target="_blank">📅 01:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93379">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCnk6WmH13yH-hIHX1X0RMuk7Ydxsi6nfpqYlamKT49Qvm8uBYx0b3mQ7QIdXY96cMreBvhx6CmHAT9Z0bVa7VKYvvCbMnz369dN2gds7fMsAWtMjWcebB7IGrpkVwLcvqTGnRCqMvpuTTEKk7UZ11UJzYwAHdCp1026_ZqQAOd-lLVqkkanOtD2ux3NsGqwrGnQkqdNErCQAK2vhay0p3bJwgcqlWCN4fLIVKyJNgEsb2WOWCpA4cr0EEzN1fvt409yCfMHnavT534wIeWWTXMwUwcW4MkZ1yR92Kx0i5uNRW8ozJV0VgNP4HyFFqPPytneRVV-qQQEnJq8ZTBjzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
رونالدو حسابی بدنو ساخته برا دشت جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/93379" target="_blank">📅 01:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93377">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dEsecEBeITIR6DzmKj88ZXeF0sRpurzUf0dtugCY-r-XHyZy_qOmM9cEiRGPEWxf0uwzaS9k9wjbvIaLB_Bh0Wkeen5Fxvw2EJh_e1mgk858gAIO_fJ-d7U7Qob2R_9_lgxrrqytPm0cY9yP3MiegDLajoFtR1tK-qH3Kfz9kO5hzVeaOEgf8VZJGVfar9Xt2Er0NteH7Gt6VqlVf9f9otUL4xVa6WdttVJ9MVfputej9jKmFV8j03PyWwuf3D_bWOZyEx-MPKFh8wU-FGkjjdC2CD_O_V84yqxrSBnDXGy76deQdAOLll10uxj5AFZx73HbwElOxwL1kExKcVdGPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLJ_oo8upVlnMD1yrZ6cTsi_8ow8aQzFERzvpd1YmY-uuKWxFlQh1BszuE3jLz2SC6eGTDR7OgR27DX2i-jEG3jdXVSEM74gA4kIgLDZoXNSDRbrmtJpmmaC-CtfIrgi2Efi1UZjfr9xWTUmguZ87tLiTPTKLIHEOeaaOePaojnRFPCU9CXgC-BX37NLSnZq0cS0lM7gLHlM7VnthvSyfWmarL21mS9HeRB_U-lnQGs2UVS3s5teNVzdozCzqtVQLT-9Bb7hzjKuVqcobsI_TEBxR0IrsE3s7yH2P7WCfUdMY-aKSWpboHR8u-3sYCIYZjLLiQdEuwaHTCylclbQhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسپانیا بر خلاف بازیاش بیرون از زمین حسابی ترکونده
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/Futball180TV/93377" target="_blank">📅 01:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93376">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgfj-9x2_RDEnTFm8rxElEBM7bcZ3oTMBHrfeT6W4cy0hGVMvEzKGd-UeYFL0OH92aPy4SN05p83Lt3z2b0AUX9CAIm8vzkG97LkhwnfAy8foVdcp-0ig51Fnh8rHRaxRISmPd7Y1ng1l4klVUcJ17RNj4cvxEMMjiUBd61U5blDUU-OiSi7xfi2JMjfyZ5AnHCIhcxRtMHmfgfe-P2ESg4M6B6RTWKHwJGUL0PeG83IGzMuW8-hrtdtLQccT82vCLZaEhZBQaTKCxPIdnUfdTMpPEF-Y25736cXJQliqRdxd-nzN-zviVt4-BdZbVhsenMAwIYbQsl8uD1jDzUp1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
بنر یکی از هواداران اسپانیا: پدری بیا با مادر زنم بخواب ولی کیت‌ خودتو بهم بده
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93376" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93375">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhOlCQyu32vdClAljFX3ZoYVuAq_kpXDvROS-BUCedN0vl44hdYH9ucTLj9ytNrvwGi8C8VOOWlGvRCoQr0mBcDm6L-4QWUMvPh7EG-A4OI8aHm3VIUgZnnCjvCfJnEfDEhOQ_gARgsUEdDORfh4MDCP1a3mIiO0TRYg1oCiQIWjlaAF3OQGSP9qhYvwJTnmpL7qpwWbjgAHEmORiVskO2qz7wHqHw5XtwlooIMv-a2-n4adk5LK5kqjJ3LkO7BfOeHV1EAetUwmenZvVFClQYnzszpsCF9LzKONH1cUXxKIndb3j6HDwM2hOp8Y7DuhuPljdSlvLQAsXxLbNh4T_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
تیم‌های اروپایی در ۱۰ بازی در جام جهانی ۲۰۲۶ تا کنون:
✅
• [۳] پیروزی.
🤝
•
[۵] تساوی‌
❌
• [۲] شکست‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/93375" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93374">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVWECt0M4XN3-Nn3K08jxqRZvzLJgeBVAfCXFJFBSdrUbwKDP7Ko9NPlVy91-jAD0ZLxSL6qYkrmzMc87SP5wHGzzVdEPjkQ4kjYL3nwX6XiG-ZXdMdPfIvjh21rakZfMJndLunY39hvAZ1AKg_VnWGKTyzzqghmKsUBpJuP3dux4EIqtezBcBzD0qvgSxylP--BXuEsIfnP5WBvUQP0700HZmcCiT0xOj_GILBpFe5RvDhdohVdNeT7PTaP066QxSFa2dHkUTqZaLA5p6IffEPPHl6YayzweBaDE90MpxxIzEp2Pc6uSZt_VZTNoHvdJV6GXeY_4PiCEONmcoAxQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
تیم‌های آفریقایی پس از ۶ بازی اول خود در جام جهانی ۲۰۲۶، ۶ امتیاز کسب کردن.
🔥
🌍
◀️
‏
این بهترین شروع اونا در یک دوره از مسابقات از سال ۲۰۰۲ است (که در اون هم پس از ۶ بازی اول، ۶ امتیاز کسب کرده بودند).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/93374" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93373">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/93373" target="_blank">📅 00:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93372">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromProxy MTProto | پروکسی(|•𝓗𝓸𝓼𝓼𝓮𝓲𝓷🥀•|)</strong></div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/93372" target="_blank">📅 00:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93371">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtRiKRn5V_SOVex1XktKvJxwZtOQmvP-e0N-Ts1yPiFt5oo6cyXyHMktIQT_gbigm11A5Ec26rBKD6iAY9oiLghVPkg4FrCquRpfOmuq2PHOOVbZeVDgjnaIXnFv5G2LscLoWLLGvFj_UGg_imrkrQlImDceTimZDPb4LeCHwDwot1UnK3FhMkY2B-VmGIww08Cdm-fOIpzG97MclogT5zCvBH5aldldUeJDNgQngzeidbJ-K2F7G9OjAGeeAPVVhVNHzsU4M7hlxczcAqHdyl4BN0XLch9agH4PdjruxaRDtMERfymEMa6YmZ3DeilFeksiZd19qeqSxoK8_ROxWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببینید امشب تصویربردارا چی شکار کردن.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/93371" target="_blank">📅 00:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93370">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYT3ENSS5qETKDQBV7Htv7ykWwU3qbLriHD3rYBFgKPa6MeDRpUvFMpBJHaT3xl9iekVbLg2NCctYUIzfS1ip0UejpvHIytsOKagKij8hSp84ER_Z9EIi34QnznuccY_sSQF8oyhv0UZZjuWnVSxSR-nkjSkwq3J6xPe70SQ38lTrtYfqiNYATd6uTIYjagSf3Ku_Y-McVnoriELE2rdLq5Oa4EwDTPE8CVpbmC7Gzn45eMBSQBqQIVEsj-G1K-frZC4kQnIUEWGV8ZfPIDkHni7B3k5KFCIZCVgoh-etpg1Cv2C7x6G24wiXJ4WfPvlsxPZx1ZNE0eeFJZ-5P5MtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
تیم ملی مصر برای اولین بار از جام جهانی ۱۹۹۰، در جام جهانی امتیاز کسب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/93370" target="_blank">📅 00:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivUkShdmYBz6JEkRzAgRnzAepgBlQtm5WF9BhRzlskkECmFN5J50GVM9vnA0WXVOECGTdpgf_0THV0ic8bDP5peBRuE3IDS1oNAOdle8gX8miFdl-XWorWmkGOqIUe0x9twT1bws4WQMICFwynXWQOus00-2E0FVBv6Wrk6wwvbcmaqGfQaD6VfKuvaGrBIueIkKKdh-gHK2Xi_uQe4AKb-qj3polBZWHCvT1dAlVD7E76aqeznzoN1kF0gna4D8NzVPls5TVXaZqXHbkhHVxH38CR8GFpF9jTl8ChCPYYI8wwhPVGaDXXGJYPcqEs4Uqjqkldpf17Id3q4qd3bqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم برای دلت مَرد، ضربه ای که تو با شرط بستن روی اسپانیا خوردی هیچکس نخورد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/93368" target="_blank">📅 00:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hY2i9_iKML8d-KtZDdQlnxuh_64DgdO4X9jzO26fR1Y1r5oLBHueJvQiS2dljZGrvCLpp36LDoH1uu5BOJQnpI_9VTxptLGQFSm5uK7JF-q3YxrqgQ4E41EST9G1UDNBFSALjFNzKEY2z0RI3WzBRy4y1SHc5iPRtpJf-cV9rgKVbTh6r8zO1OyLRdYnvRoMNW55-u6Pt2gfnmg_Z5iVPmIaeUJf8r5PF4HyF2i8a1ZArVRoRhEjRHQXJOEACX763MUZRl9WlSmnsZB4zfSfnTDvwRCui9TJihcSshIihHa9XE-re0yPP-AK8d-HGuMLeTwTAge5CuQcincRSmQdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امام عاشور به عنوان بهترین بازیکن دیدار بلژیک و مصر انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93367" target="_blank">📅 00:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNvUO0jvAfg2rRi-WZ_NpWMwY9AnIgeitIRJ0qLQl1O9d9tGhzvvoOgpkKzdRH_0mqYzeq8e4KbvJxRf6Jpsj0pQ98NncLL-hp9CWDWiNkkjn7-BM5k6x4klDjeB-aAvxrV9GRljEXIfnGRI4PS-OFYfx618yL6g6axE5VCeuYsQuXNCvxf6M_5Y6qGt3sX2wpQw74H17bGDWjiCFVQhlILDFIfY4OR0OM_aC6TeXC1KMBYNi5OjV1Vxhwnn3IHYDGFk2lSOHerFZ2B1nM_BnlSoy4LMxIJW7Omt-zk9aeI-p4np92Zry1BypbIMHoIqY9dSE9jNbOsa77rgLGJYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
🇪🇬
🇧🇪
آمار بازی امشب دو تیم بلژیک و مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93366" target="_blank">📅 00:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYJEipZZUArWxpbslsL4yV6T5aH7oF4sfS1RgIuJlCOf8nAwsOvO2JwhfXXHTBG9GsydkthYmHoqIOy2VjpFUa2TvPJpQDXtZqF71rCqJX8RZXdhK7Gvmq8awXOCDM6Neg8h-TfcdgdF9Era2PCVfaMK-bPlyuvIpgm5gxFxcM3iT7PkR1xV5YMfeEHP0AU4mbmbF2rn1zbmi6WbSiXH3L9BOwxvns5Lf5JC2y5oZua9KAo_sBzCZy2HqsrSHFbzEE-B7m1TaUXeXB_u0zUSplX2wmEaR-gRyD7ZLvNvFsabFIG0aYJ_XFTbc6rdVVZdhl957EXjKZOr6s-FUME7lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
پایان بازی | حریفان ایران به یک امتیاز بسنده کردند
🇧🇪
بلژیک 1 -
🇪🇬
مصر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93365" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch-w7U9F3IpTUDcNPoZAK0ZZ1qqOrPt3gotFBE8HVBFqFz9OBsVQCQixHGWJ-Yb0VldzK245SytmQel_lJZM2hO3VSqrwQWnPzyui-ItcKQnUqHLa5tdV5B-BR6jXE6G-SlGUzqE0VAbD0ES0gEtE3zQT3DrIdK84kVGDx6gy82lwmhmWocA2OeBLqlgd06HkQe7l9ubpIL3DK8Pmb_ZhNqKqLjhP0v84xRzVe4KIwyGchdv8lErTw8icve0UyN1cHO-bqByXL9lOQvEW_73TgiCUD_hgy-bI0CV-GNb3z_8Fb9Z3U8v73YmwqBqjGsiGHpK9rdCmI4aLEWWqmYzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
تعداد تماشاگران بازی بلژیک و مصر اعلام شد : 66775
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93364" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">واااااااای چیووووو دراورد گلررر مصر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93363" target="_blank">📅 00:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلللللللللل بلژییییییک لوکاکو</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93362" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a05a2beef1.mp4?token=QNi41FKduY8KYmywtIJsv4ZqibOw1j11O0r19tzLbe9NV3fu-xmL8CHkc-cEKKYd9CGP9yH_7wwnimDVL7YHgATY33hcSpjjyerv5szC_UXp1mUpccB5Py2aF0x7HPd_k3HVYvV3dCY27p4CZMNSVqW3fdYal-SyilHJCTl0a_nYW4P2GRSnoEBDSkVCfisza554Zkbr7lkBbk5WGQdn_h5sKwzmnvJWRgRE2nIuduUT88S41OeIBJWC6Hl2CoymA3ZiRHIrms7phO8fUjI5nb8URHFCKOMfHQRHhamnBeTpjh-V7KS3tRAo6-saOCvxEHob0llNOmVW1kUC4QVKpgZms_jm25eBKzHSbMQ-aYOWfGBFJ4LcbtGH-ncPHfneQcDEGt7VdJi8tJRXTGDS_XNhpBZxtsypkjrkVQ3tznBvxqpgAXzn2PSwv6aYjaeYPxPcLHX3WE72nQOf22PXXfxj_1ddsDf9fJvxXsnkt0DgIVJuX7B-hTFrCPkrsVkjmhYZdItqs4ifcRPLjUREvUkr_9cchnNNCK1-8xFpN1OlwbVuJgoQwF6BueQsxyIZH-1gR7S2FFUvmFiHwF8jx3B7GecNr_pV8QCeX4cVJnTjCBKvigQIIWWJfYTfNSWh2k7nZGkTaJTdSvKWPLZ8-SppSxgO18uBAkNXrRwxlNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a05a2beef1.mp4?token=QNi41FKduY8KYmywtIJsv4ZqibOw1j11O0r19tzLbe9NV3fu-xmL8CHkc-cEKKYd9CGP9yH_7wwnimDVL7YHgATY33hcSpjjyerv5szC_UXp1mUpccB5Py2aF0x7HPd_k3HVYvV3dCY27p4CZMNSVqW3fdYal-SyilHJCTl0a_nYW4P2GRSnoEBDSkVCfisza554Zkbr7lkBbk5WGQdn_h5sKwzmnvJWRgRE2nIuduUT88S41OeIBJWC6Hl2CoymA3ZiRHIrms7phO8fUjI5nb8URHFCKOMfHQRHhamnBeTpjh-V7KS3tRAo6-saOCvxEHob0llNOmVW1kUC4QVKpgZms_jm25eBKzHSbMQ-aYOWfGBFJ4LcbtGH-ncPHfneQcDEGt7VdJi8tJRXTGDS_XNhpBZxtsypkjrkVQ3tznBvxqpgAXzn2PSwv6aYjaeYPxPcLHX3WE72nQOf22PXXfxj_1ddsDf9fJvxXsnkt0DgIVJuX7B-hTFrCPkrsVkjmhYZdItqs4ifcRPLjUREvUkr_9cchnNNCK1-8xFpN1OlwbVuJgoQwF6BueQsxyIZH-1gR7S2FFUvmFiHwF8jx3B7GecNr_pV8QCeX4cVJnTjCBKvigQIIWWJfYTfNSWh2k7nZGkTaJTdSvKWPLZ8-SppSxgO18uBAkNXrRwxlNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل اول بلژیک به مصر توسط هانی ( گل بخودی )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93361" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلللللللللل بلژییییییک لوکاکو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93360" target="_blank">📅 23:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIXD71rRyfqWL-gfIUPLxd_x046xQuwmoK6ZUoy8qSoC2xsJFKpGjdQ1NzFmDujv9UVaOvBSd6T1hQsP_gfVasmeNKsKNSabb_sGbW7uqacKKsbfBBadGUu1Lj4E1IMnb9Jf3CLTBx_1g6X9ka8F7A3ZEhPCZ5OBYyKgZfqCfcS6e1CT3B15k1wXvMDx52g7MRrj9Ss2XN-mFdv9fPSpb2qaRtnacoFtmOb0SJOqi9k6RME68XSMgl-nOXOpKcJ9H1c_PJa_7IH04Pkd80zPwlubRRPUe7k1j6csfnjhmsh7HgBJFUXfk1Asf2_Hd93DCum0Wrc4tJKyPhFEAPzO4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇸🇦
ترکیب عربستان مقابل اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93359" target="_blank">📅 23:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وای مصر نزدیک بود دومی بزنه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93358" target="_blank">📅 23:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لوکاکو داره میاد تا کارو واسه بلژیک در بیاره</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93357" target="_blank">📅 23:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مرموش هم توپو زد به کص گاو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93356" target="_blank">📅 23:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUlmQQyz_pxWUiJzSGqwx8wqbD28KrLSLYPUunfN4HhhSTyoc05kcACbXER8LXPSBZjSQpS2wsN5PYAK6dkBIWH-T2PFeVJRpgEQS5axCM1gd3kICnUnqbL5LRafyM0w94Z1g9YovxYxPJa2pjvN2srCaJ0b3xPUs9DdOU6P-9NpLiAo9DJXme5QI6r4SYNvtafcPLAb4wNh09wqKRUlh5yqjAau_kiALLsLUHLdYlv-xI0L0ZfepwRBLMeycLLBzjTwni8odUzkMMROIE-btuOws5zyQQoFkuhrn8--EvZXfBsv-oaqmX7I_8dMv1DYhpwVYDkpQioZ5XesvZfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکن مصر این توپو به اوت زد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93355" target="_blank">📅 23:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rs_ajTOVslEOwxr-_AvpwZnA-i5zf8pe2ritM9ydYIFOvaQ_TsqTj7VhQ3UUcBR9hWGjJmTLQO6Ht04BXeoyL53wLKchXvxmkPp6TNvauBPd95RQ1CuEiWMLCwlvK_N6jC1ppZXZ9Ey5fhCUe6LqoD1UY_AMaM-ihVjxJrd7KiCloW43Yg5qkpXI_LHOf-xB8vd01ad70-JVsQJ0TTw8-HxafdSaYTnc5KsA2GCQHIuyTswFIMpKhvCXDW27efe6UZHC4ILiG2-fOf_ISjQxfirdJRkdX5nAPMbyoqsFvQQ7-d5oPE4OXyqeyrjL4cMlbi-WxE_RFhtYomOEvB-j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
لامین‌یامال: به هواداران اسپانیا قول می‌دهم به آن‌چیزی که در ذهنشان است با قاطعیت دست پیدا خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93354" target="_blank">📅 23:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پشمام مصر چجوری این توپو گل نکرد
😐</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93353" target="_blank">📅 23:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e1c9a760.mp4?token=BZs5uOOGaeLurEoUolAEAAcMRIiebmdzL8oFAuiVBWowRGGhd3AbbpUD0zk4JW-AeVBhgpBXVgnmuIBtEq0o4eTpY60l1_7bZQZ47ScR9VwPsku45O8JDls-PAxOyJ3WkKPZgYB2phFiF7MpFIYmujJe05DKfaFua455pqcpckcfO6D9s0IFGOPz-DSWJ_kB7tMc5GxTlU_ChqdhmTnqWBn3ZXKZCSrREyHm8LcLkavdfKe2aHIM6kM-q6hwK-q16IPOpnIQHPjM5_kkOfVqlcMuIKm2uYjynpfglypC9udiHXfGgxn6XqhAX_hoGHbU5ncS1xFxm0NrVp04mEmETw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e1c9a760.mp4?token=BZs5uOOGaeLurEoUolAEAAcMRIiebmdzL8oFAuiVBWowRGGhd3AbbpUD0zk4JW-AeVBhgpBXVgnmuIBtEq0o4eTpY60l1_7bZQZ47ScR9VwPsku45O8JDls-PAxOyJ3WkKPZgYB2phFiF7MpFIYmujJe05DKfaFua455pqcpckcfO6D9s0IFGOPz-DSWJ_kB7tMc5GxTlU_ChqdhmTnqWBn3ZXKZCSrREyHm8LcLkavdfKe2aHIM6kM-q6hwK-q16IPOpnIQHPjM5_kkOfVqlcMuIKm2uYjynpfglypC9udiHXfGgxn6XqhAX_hoGHbU5ncS1xFxm0NrVp04mEmETw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دروازه بان کیپ ورد بعد بازی وقتی میبینه فالوورهاش 2 میلیون شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93352" target="_blank">📅 23:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇪🇸
#فووووووری
؛ فدراسیون فوتبال ایران با پرداخت مبلغی به فدراسیون اسپانیا خواستار حضور هواداران این کشور با پرچم رسمی ایران در بازی امشب شده است تا در مقابل ایرانیان با پرچم شیر و خورشید قرار بگیرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93351" target="_blank">📅 23:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fabd41212.mp4?token=ZdRhXeZieFbk4OHjJ8WLSrHsemvhP5f7YQ8YzYzz671dP9Y_yN6MgGT0WX4mPBt8POb44cGfDrXwvnUi3UcPbvghm0m9XsatNgZp2HDxaesF3Sxtxt1TmFG148klRzbBe_KBhQk-Rwir_pyIwJhQv3-i351nv-2115NEM-z_h_70xNxwUcr73Fj8ejBJNXRUizoGj-YsOxGYQlsySrbweV2hEceyILKE8JsOd9CdMU_tfEU9Sb92ZfW_j9reMcx8trZSMeLkvHgmNpeGxriFH_GKQOOD4LisvEK4nV5AiOkKEgcbh-LHL3DNpLxnLgp1upH78ecnbt743-iZEwc0mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fabd41212.mp4?token=ZdRhXeZieFbk4OHjJ8WLSrHsemvhP5f7YQ8YzYzz671dP9Y_yN6MgGT0WX4mPBt8POb44cGfDrXwvnUi3UcPbvghm0m9XsatNgZp2HDxaesF3Sxtxt1TmFG148klRzbBe_KBhQk-Rwir_pyIwJhQv3-i351nv-2115NEM-z_h_70xNxwUcr73Fj8ejBJNXRUizoGj-YsOxGYQlsySrbweV2hEceyILKE8JsOd9CdMU_tfEU9Sb92ZfW_j9reMcx8trZSMeLkvHgmNpeGxriFH_GKQOOD4LisvEK4nV5AiOkKEgcbh-LHL3DNpLxnLgp1upH78ecnbt743-iZEwc0mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
من بعد اینکه 10 فوتبال رو توی 4 روز دیدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93350" target="_blank">📅 23:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !  هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/93349" target="_blank">📅 23:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddjn_pP2ONHvmtPa6DxHVYD0IRP7YUnia9GbWlWlzkRzp3Pq0__wkJppQxE3k4HuHQHBUke-7fvsw9E3VqsvGoOyS5oJxxkhDyD6Yi0aJPy8QvhZXjyGPMM4RYO2kxs6CCKJS7ojVFzB7MB29Ovk0hAlxPEd2AFpaA9YaISnp99MpPWFhHQbjByBdlIGG3QFfU9TXH2eHckAJDbaQTkOhh6AUB9cjbjXpquJ8U3PqbaOmTWaKbEadjemGodLKM-nXYuPlAyhsf40VjMyTJUhqjJ5f_njRhjwOorzPiq-CC7vLj-6aqxBMBUuVwBLVeqv0vWyXbXtEFybh30Zrmc8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو فاک بت یجوری وین میدن انگار بت زدن ساده ترین کار دنیاست
🔥
از جام جهانی تا تنیس های کصشر دنیا !
هیچ فوتبال و ورزشی و از دست گروه انالیز حرفه ای ما در فاک بت در نمیره !
💵
@FutballFuckBet
💵
@FutballFuckBet
💵
@FutballFuckBet</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93348" target="_blank">📅 23:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93347" target="_blank">📅 23:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhnRuhLSl6f-MTseUKmKc_9wHczmTaQvKAGO9NC396KBSMAXVq9TkLAGhswXJNJIKoI9RGDO0U87HsLuhkzgUGWJ7tBtHYhXaD0WCrc6LFrP8XwHlSQ6oKww348dSe9DWxwr7JNPLOSOWSwvNI1i1O6bQmYZ10eSNhp7bCwkXjWku-3JJfa-xneZP4kT3Rql2MHcB1xXj8tBV9n320PVP8K4o51jX8hUOun2XQ8v14DVuE74pAyiQc9jqP1NxclOo748mPyseRuoo9cpZhUrKubYKpbNZgTyncuRlnF-riGy6PD5c9CUCT7SLmrMl9ve4LpWvEHATZQ6Vt4c19modQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مانوئل نویر یک بازی دیگه تا تبدیل شدن به دروازه‌بانی با بیشترین حضور در تاریخ جام جهانی فاصله داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93346" target="_blank">📅 23:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRtMTMQjSmXJpdAx1ZzylQZ3lY3AYFrvca84-ZGZXLg5uTcO9-F7itQhZI5Xg-Ow-ipBIuy_nhlsIVNDtmgxTcfSAhOOR8HxrVi_WIh7akis5j1_fReJxd5RYcB42LS2c9-lbPTsRFBE2yfmqlwK40DA0ag5brbVvNYutVGQYtfN3VugKbpGUujB_lT8OO0ze3DP3a1ZPlDGMvgrm6znZg0WRMqR3IR3xANAY5XfFoesnEInBskZUeOVgci8_jq6ffFui3YV-pPYos4UWB6ySIq0g03XK1H4CooE0P3-OxQ3NtXzS5-7gSCTGJg_3Kn_fzkUzAEWF3UFKs2YpBqZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیکلاس اوتامندی:
ما تیمی هستیم که همه به دنبال شکست دادن ما هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93345" target="_blank">📅 23:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fym56uA5IIZP54Ag8NgoikmETrm1upLv-A7FoGaq13W5stJ5ex7Wb06srLw3h-TTYoNykDqus-4gJn0kc2x_cL7Vhzz-jKvhTirRjEu5jQKR-jHdXwzLnTGE9R1MkXJRaiBqpyJVX662yIBY5ujvAs__MgAJa6nV0pCraNkPXFTa92uK27hkcGjyToD2TvJ9Sj2NlCbV6YOtnLYzMoCJrpDXFWGXxy8zpP1iQEVcseNzH10T6CyyKGrxYvGjkBCg5Nx014PZYQFlQmDXLE6tSithLMGUcx3FKOK3oz4DR8J6QXHV4FxP925iLjo4SWICAOu5qaH1D6N23tOMgeQvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرعت شوت امام عاشور بازیکن مصر به 123 کیلومتر در ساعت رسید.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93344" target="_blank">📅 23:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پایان نیمه اول
🇪🇬
مصر 1 -
🇧🇪
بلژیک 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93343" target="_blank">📅 23:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPAmw0UQQUuifIkmgKBX74aznFOMScSGljr15WCUWdCzuVEiDoNdj18AkGxHsi8-BGkn8Io_ClSMT3jC84qdj3bhhD00YX2kx03i_ttSbld8RQYR0tYESMGnE22k4fBk2foTnKi6WSmdbDK2-vC85ji3ddtIMRip3MX93CjdmJg9KiRhGAYOcUL0Aqlz_-4a5SrL_3W2ZXJnWfrPg-KNcFNCiR6BT5JPP0DXSLtXL7GtgEVbRGuiojb5UVvboX-D0k5v9BOjP2KIAkI9y1N1OTjkdB6T9XT2C9_4H03xue678snC02tg7xzPQMpCVJ0tbFSSgwCxTujQxkrhLwQgTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
شات بازیکن های تیم ملی فرانسه با کیت اولین باشگاهشون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93342" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df284ec986.mp4?token=GtCmj-azJvCfKlkacVdebmEwHllYoK8aGkj3k2RyhyFOfn0moMTOGdlRndisdgUH0BhobG9_OnhjPbDwd4Sf6O2tuHR70q0tdrTKgT6D3_X4bV7q4iSdCiV_Jx0tGufmTAMykqZXeQmvA0O7CtiK07yIGrwyrkxK4loS5GDi5WdNQiar0zluf3sCs30W0rNSxjoBk7GgQ2XVVvc1_uuD3K1kxRaAhWVl12bi7OUUvlJyF9gJCz3Ierxa-oXdhtualKo6DXrIO5uMRaKfSaAURvkUdaIOXXqBEwbTzNVUJoXCliT5OKn0LvHViammMxJ1mlA2Vgl9hwxIlem5EsIyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df284ec986.mp4?token=GtCmj-azJvCfKlkacVdebmEwHllYoK8aGkj3k2RyhyFOfn0moMTOGdlRndisdgUH0BhobG9_OnhjPbDwd4Sf6O2tuHR70q0tdrTKgT6D3_X4bV7q4iSdCiV_Jx0tGufmTAMykqZXeQmvA0O7CtiK07yIGrwyrkxK4loS5GDi5WdNQiar0zluf3sCs30W0rNSxjoBk7GgQ2XVVvc1_uuD3K1kxRaAhWVl12bi7OUUvlJyF9gJCz3Ierxa-oXdhtualKo6DXrIO5uMRaKfSaAURvkUdaIOXXqBEwbTzNVUJoXCliT5OKn0LvHViammMxJ1mlA2Vgl9hwxIlem5EsIyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
😂
شکم امیرحسین قیاسی از خنده درد گرفت؛ خاطره خنده دار بیگ زاده از حج
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93341" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMain Online پشتیبانی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5nu1O8jxgY-BXAel441duUo-vuNVP-5DtAZcMRpEpm3dwtTJLC_G-o5CapG1UYF-DeSPXkzZE3mprr36xrV4_Rxlc3OlZ0TM1kwyxL_4UmCS7MUgQFXK8In3oPfzUtMsfjpYGbnX1KTMZJdcg5gDaEWMOZ9IawlS5vFtJcFf49ot9DCaemDHiPge5hmdfiZupVm0Czh-lSY3M0r1Z1zdxbwmQj0Vahny1E8bwnGgMxpu6RxckyBj6BPDE9bIq2g0afpNZNGlwA2aAFfGqEU8Do7JmNQyC-3H8pEREvh3rTVWWPyvr7I9RvKY27ZIFNJCjoarXxd_6MV9aDg2hE2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فیلترشکن فقط گیگی ۵ هزار تومان
✅
👥
| بدون محدودیت کاربر 999+ نفر
🔥
| بالاترین کیفیت یعنی تانل شده
🎁
| کد تخفیف : 50
▫️
5 گیگ 25 هزار تومان
▫️
10 گیگ 50 هزار تومان
▫️
15 گیگ 75 هزار تومان
▫️
20 گیگ 100 هزار تومان
▫️
30 گیگ 150 هزار تومان
▫️
40 گیگ 200 هزار تومان
▫️
50 گیگ 250 هزار تومان
⚠️
| تنها راه خرید مراجعه به ربات
🤖
| ربات :
@YOUPINGROBOT
⚡️
| ارزون ترین قیمت بالاترین کیفیت</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93340" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سوپر سیو کورتوا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93339" target="_blank">📅 23:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93338">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOtfUhW147QUHadSm4lxQSWy19qQv_lYXI80H84xonB2R1CoqzoawLEkvul6iSbfpVqQR2big3gF7Q2-aB9_5W8SHUf2jCjtmi3-qtpyQGQsvdtJDhRKJkcqttao5-cImRbFdM186C95kWyoRGguXrpIlS-CwwkAIKH6M-BM2PpR1IYQRB2t-U-nmF_8r3PcUqa-KMHeEQ6i69ydUm4Hg00OzVJxj6fhNavsCqknua3whx-pEew2wDh6-l8CNMVx4xH43WD8aPMNo2pfNmjfad1RDX4XORSIQsBQ_mUqBz7UsOAzZORlqaOp7x4v6jTR1kngK7IjCqTdjP1OPz_4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه ای که کورتوا هرچقدر به خودش کش داد نتونست توپو مهار کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93338" target="_blank">📅 23:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93337">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tn_EEbS658q4R8M3cd-Ta6tX9iT6nlneT2dO1KSLkfgBiv7qQfT3OHfcE6IznX7ZhxJkljMLF5wTaZOJh5P09bw8VEfRUhOE_dvK_iXfi4Sq7_C4HeFc3ixKBVMlk1Nl3dhT4FUy66lmpbnfWFsaf8D7-CWZ8rBx9CIkFlflDhYHvkt3inGiSK_d8nacGIVDR1W3DzjCZy34_g078cDj9M7OIZHAqUGrvMzh2B_z2pPi59Lv0e9jb7rc5ymB3EEbM9nxN5wDJNB4H8pusd-VU6tG8yHtxF2jXKArB-X0XrIEW59r7nZ8azsmop_M2Cx6Xv6wSjZWclrde3G_ho5xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یک بمب‌افکن استراتژیک B-52 نیروی هوایی آمریکا بلافاصله پس از برخاستن در پایگاه نیروی هوایی ادواردز سقوط کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93337" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93336">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99491ee01b.mp4?token=PsFW2wPfd6e776eL_snkcEfXlykVp0Na30_jbc1QzMN2nnvbuHixYmTHdQDy53xVrEmLHIZ4cr9Poz6Z9REHVp3OjDfScqTvl0y-TyoL3FoKPfjLXOqA7Umf3aQtBkvbysH4vyrdcA-bBcnJFAHVWoe1PLZZMvDcc8ZpSw8EPlln3M3ncuqRu3JMe5ZUrr1OHOyuf5aaZPQ748ui5ZOf58gJjTnqNtCnM6i0l1UMqexXn97ygZPnbbQC7GJ-lLaFM__5_mn-6YCJNx3RSq0HI2Z7dc27JYJt1eENpxiJGkyOBSW6f2GPiwjTPt4f6-yaSKxl41v0tz1Mo4RU_UnceA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99491ee01b.mp4?token=PsFW2wPfd6e776eL_snkcEfXlykVp0Na30_jbc1QzMN2nnvbuHixYmTHdQDy53xVrEmLHIZ4cr9Poz6Z9REHVp3OjDfScqTvl0y-TyoL3FoKPfjLXOqA7Umf3aQtBkvbysH4vyrdcA-bBcnJFAHVWoe1PLZZMvDcc8ZpSw8EPlln3M3ncuqRu3JMe5ZUrr1OHOyuf5aaZPQ748ui5ZOf58gJjTnqNtCnM6i0l1UMqexXn97ygZPnbbQC7GJ-lLaFM__5_mn-6YCJNx3RSq0HI2Z7dc27JYJt1eENpxiJGkyOBSW6f2GPiwjTPt4f6-yaSKxl41v0tz1Mo4RU_UnceA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر قلعه‌نویی: به خاطر خط خوردن برخی بازیکنان از تیم ملی، شب‌ها خوابم نمی‌برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93336" target="_blank">📅 23:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93335">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/883c9456a5.mp4?token=aQmNAKAVXJqv2QOKXUsOpnMbOKLGpdzxw2G-9xZOA3Q5f87hWxpv77qUUc6eBKI0SPw5bomTRK8Difi2WNzd--DilQat3MaZNChsxx2AymRfpaHuMcdAU2FsVgBhHlni7d4b70u_l2wKseaIOoSwsWiRXuBiFhc-Vc4yKNkesssjDcnWxzCRmSwDOvFu6Kzcn10fN2KK3ka68VeKTdE3ou6FoJ5eUV5PNdj-73mh4m_SP2Gmkb8TBHZPpn7EArb0q93zmeCI4OZkqGb91oBfadjBqn5sO1dpZipSQdxFI4TXAN-pzqj6nNyv-4IWiFu9nxNykXmokBOVTjr7hm2EU2Hu1p5_zAEV_sVGLfGBqeZPc5hZeVJUfq806lNd_KbU7m6vkykw2SrxQ5HbHkkhsxNQQlnC4vmT3dA5CBTSnYoJM1GC13enDI9O5xqEC28NmBQCDYNp42D-BGqrq9MevWVHjOlR4MqlRQIXM5f8_ZK-xPYbpK2Eo7d3d2-x4W3DdXesRCk7eL6YQh79zsvQpR5_JU3ARo3rj1jOlUSSzDp9pkh13pngYbHD1ZGXOCakWvKnW2jLA93TFAHgkje-35BhcRJ7-yb1pNlW6-EolHfMzjnGgAZN0EY0vBzlNQZr7y5QGZZ8vx1muWSF0sJLC48u2rDNuSoY1LsEBQumufE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/883c9456a5.mp4?token=aQmNAKAVXJqv2QOKXUsOpnMbOKLGpdzxw2G-9xZOA3Q5f87hWxpv77qUUc6eBKI0SPw5bomTRK8Difi2WNzd--DilQat3MaZNChsxx2AymRfpaHuMcdAU2FsVgBhHlni7d4b70u_l2wKseaIOoSwsWiRXuBiFhc-Vc4yKNkesssjDcnWxzCRmSwDOvFu6Kzcn10fN2KK3ka68VeKTdE3ou6FoJ5eUV5PNdj-73mh4m_SP2Gmkb8TBHZPpn7EArb0q93zmeCI4OZkqGb91oBfadjBqn5sO1dpZipSQdxFI4TXAN-pzqj6nNyv-4IWiFu9nxNykXmokBOVTjr7hm2EU2Hu1p5_zAEV_sVGLfGBqeZPc5hZeVJUfq806lNd_KbU7m6vkykw2SrxQ5HbHkkhsxNQQlnC4vmT3dA5CBTSnYoJM1GC13enDI9O5xqEC28NmBQCDYNp42D-BGqrq9MevWVHjOlR4MqlRQIXM5f8_ZK-xPYbpK2Eo7d3d2-x4W3DdXesRCk7eL6YQh79zsvQpR5_JU3ARo3rj1jOlUSSzDp9pkh13pngYbHD1ZGXOCakWvKnW2jLA93TFAHgkje-35BhcRJ7-yb1pNlW6-EolHfMzjnGgAZN0EY0vBzlNQZr7y5QGZZ8vx1muWSF0sJLC48u2rDNuSoY1LsEBQumufE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇬
گل اول مصر به بلژیک توسط امام عاشور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93335" target="_blank">📅 22:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مصر اولی رو زد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93332" target="_blank">📅 22:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93331" target="_blank">📅 22:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔥
🏆
🇦🇷
پست جدید لیونل‌مسی: بیایید یکبار دیگر در جام‌جهانی کنار یکدیگر باشیم
این پست مسی با بیش از ۲ میلیون لایک در فضای مجازی حسابی وایرال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93330" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93329">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10e04857a.mp4?token=gSBDb5YXDoDXcx_iKMrSLGzb7tDKuXUYKUxCQmDzWCVhqFryG7Xc2-PvnxIL40ffw5ayWpyGKaKiAImu91g6VwlqZis4dfb8jUlq8C-Ku0SBqmMz2uoEEOuaivruG1tjXcV-kiES88vkKf4VpEfPi8tRuU65ZWHJ_yPVaP6cYz-yF2zm4QrGrpvpVmovMf3U4xu0ilqO3CVS_dd41RbNx2Cr6Epw1SS-wkRTPuHQW-7KZyFIegxzzO99PBeKLWryeYxzOfFs50xnXo2NbxoX32Qsa1nrZaBSI476KQfRDltFlz8DPMbhBzLnXahtxM00ViNegKqiYOEKEXYMG4LwhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10e04857a.mp4?token=gSBDb5YXDoDXcx_iKMrSLGzb7tDKuXUYKUxCQmDzWCVhqFryG7Xc2-PvnxIL40ffw5ayWpyGKaKiAImu91g6VwlqZis4dfb8jUlq8C-Ku0SBqmMz2uoEEOuaivruG1tjXcV-kiES88vkKf4VpEfPi8tRuU65ZWHJ_yPVaP6cYz-yF2zm4QrGrpvpVmovMf3U4xu0ilqO3CVS_dd41RbNx2Cr6Epw1SS-wkRTPuHQW-7KZyFIegxzzO99PBeKLWryeYxzOfFs50xnXo2NbxoX32Qsa1nrZaBSI476KQfRDltFlz8DPMbhBzLnXahtxM00ViNegKqiYOEKEXYMG4LwhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدل پدری هم پیدا شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93329" target="_blank">📅 22:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93328">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvgfmpZZSDlxsRuczPlKn8xY9KAjA_tEIKUadHMzjtn-WBNlEyt0bss7lbRkCFJFSoeY1pGc3MnnDqGqq30OQxIKnCXyqPczdw_fn67gfyyoP8r1hqoxPrh3GxQM-tYMGK3wCiXXVy9hu1Kc6Dg-9bNEgQnX-d6eFyjxModfKgQ7ahORfCU7g6WJRFAokatVFUVn2TfM8Uh7rT41C6208r54EkvE_GfH7kxouP93oy5RkuLk2Me2gTF1b0uYYQb4_M6JXh5rTv4Noy7Jrb2cyx-B8-D_t83zyZ-fCYvOMxlnVL7aGrrYFJ4utpsKrRiyNMbf0suhsJd5Ih1aYvx1aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ووزینیا، بهترین بازیکن کیپ‌ورد و اسپانیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93328" target="_blank">📅 22:48 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeUlp5RmhCvOH8d5diRX9HQccO4cSCi_lyFffue7J5oMR-4Z52osnDk1Vc1BJ-nTsq1PkZfd-JVMqq91d2D1bgs2uFmI4g8T7ApeCXQUKG6HwagWyTK8PdJi1Le0JjYV1hDp1EJiA3zPXnoIr7WPs4RcnkdCwkjjGl_YBrobVMbTLSJ6nRxDBAiZF85dOWdeASWJ8LIW5jdO9DR689RCuSyfw2CR7uncb07dD1qlN2jisSbxlKte1lFqF3qv-nrCesqYRyAsK9PQgQDriT7VKE8wNO6W-M2GgCKBDFtMQvoJ-1fH7jqfPvq1hqkwH2v8gsuIdjlR3pfKH37MlEFHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای مصر تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93327" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmEcizo3FRykZMlKQUwcrdInG2ou3htWoj3hQtB3M2jvkLGYiVNCzw0f7RmfwJCxBvmUS98yBNNN1sSPAPR5Jb0CVbd-Sh11O4QQMUfsUMEO3F-tNZYCo_sx4xNYm-Fi8sfTJ85Scv_Y45h0GSGys06iVa0-Vqh0PvnMxUO65KBUSezrv1VUDpPYwYzqFVkQCXig4r-ZNMLLdeNu_SI_dnTczQ9UGDYoLcpxrFleduWoFizt0J-CRlQGbqZJc5vqjEwtVnuiuxOMQjxKJ2phjWJde24OFAwBBXZ5Hxa8z-mpI-UFO9CwDvhGIngKSwcyRE6A5qWMPOQIXTLpS6ZU0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
⚽️
۳۵۹ نفر فقط با یک پیش‌بینی دقیق، ۷۰۰ هزار تومان جایزه گرفتند!
🔹
در بازی سوئد و تونس، ۳۵۹ نفر نتیجه مسابقه و تعداد گل‌های دو تیم را درست حدس زدند و از جایزه ۲۵۰ میلیون تومانی این بازی سهم بردند.
🔹
سهم هر نفر حدود ۷۰۰ هزار تومان بود که مستقیم به کیف پول همراه من واریز شد.
🔹
در این کمپین ۳۴ میلیارد تومانی، قرعه‌کشی در کار نیست؛ هر روز ۱ میلیارد تومان به ازای تمامی مسابقات همان روز، جایزه نقدی بین پیش‌بینی‌کنندگان دقیق تقسیم می‌شود.
🔹
شما هم با پیش‌بینی دقیق نتایج هر بازی، می‌توانید جایزه نقدی‌تان را مستقیم در کیف پول
همراه من
دریافت کنید.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93326" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93325">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بازی فعلا درگیرانه دنبال میشه و تا دقیقه 15 دو تا کارت زرد ثبت شده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/93325" target="_blank">📅 22:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93324">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjhUKudnQ-uiwq43cf2yQbURvWMtYDa2CKaQcRA-n8kEyYX-_Oq4kiglEVE_WZIrx6ThM4hLdNaXnN7XE7j-6zNpmk9973pntK2OHs_LHvaYhocEMFih9AGWzjdty-s6xWM4w3ey6sTaBdTqQXtLvdkFXsSODVcWEjLQMx_CJ4-aGgFC6kzwmp72z5z_YNUXi3nuUjo0OowabWo468P9N2kICWpVc6BZnavF9gSqdOMontfHbz2JBmwbUofvjCsGqdZZp1gQyvHaaSp6tMsIkOGd_gx3lhLmgHOzAqwPQFJvpT4buT39TR47mJWSAuI0OJNIHWXQ0EF7axhfmTcPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
اسپانیا در اولین دیدار از پنج جام جهانی اخیر تنها یک بازی را برده است.
‼️
❌
۲۰۱۰: شکست ۱-۰ مقابل سوئیس
❌
۲۰۱۴: شکست ۵-۱ مقابل هلند
➖
۲۰۱۸: تساوی ۳-۳ مقابل پرتغال
✅
۲۰۲۲: پیروزی ۷-۰ مقابل کاستاریکا
➖
۲۰۲۶: تساوی ۰-۰ مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93324" target="_blank">📅 22:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93323">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بریم سراغ بازی مصر و بلژیک
🔥</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93323" target="_blank">📅 22:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93322">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9bSQRBpXCXwS1D--MWimaetKlaCgHQrGwNMpcSoHQw8oKSfNWKCWqmcazplAVVCSmlLnUNp6T_pmMSv2XcS-eO10P_3lD8wQn8nZoZQf-ezunrq62vAnZoxvTVKvizmNwbz80JlskMJn5BSSz0nLqZtzDX428N4QaYYFB1f5KjCyceJZGr_9d4EQ7TzjxdeS5l1y6apoqDnbzpHXErsPu-ST2d67IKdDr3BSE-y1WJZlvlvMG6LL7KXTbhEdUfVt8Ny3Sl89C5B0Jhr-baxlegPKU6otV-E3jX48y0Wj4JCjtdWmfK3asOEUDHz_J-ClY62-4C96lhVsrQL9pnBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
پشماتون بریزه ووزینیا بعد از درخشش امشبش جلوی اسپانیا تعداد فالووراش از 50 هزار تا به 1.6 میلیون نفر رسیده و همینجور داره میره بالا.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93322" target="_blank">📅 22:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93321">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6DziTL09Hy31QykbtMdWwVcRxU0CDcAV34wVxrZsezyS1xG6L3NWWI9ZqVmOU3Vbj3ZXs827eOHWTJg11VAPOT59kdLis7Z7EITqW6k5Y69To_RLmrtDhPL0UGf76yJxmwujyYUZFX1GDOQorck8Viaf-e5aK3x8mOgBSSNoe7yWPS6EBJZC4NV6ERgOyMPq_5Utphqy99ZrzvAtW-2JnpeE_mZuFY7U5Y2mHUM-XKxpLNPm9hiQBNlk89Nsybv-Wp1M_UBd9HmMzcT4c5mf48_n6kaCWHI25KtEEoVfJAUVRliBKWwQb8nkmJjDEzyfb_lNa-CGtg6PcjKUa_DTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا بدون وینگر تفاوتی با یه تیم معمولی نداره.
۷۰ دقیقه بدون یامال، کل پلن این بود که توپ بدید پدری یه کاری کنه!
با یامال و ویلیامز اسپانیا میرسه به ورژن یورو ۲۰۲۴، ولی بدون اونا حتی توان بردن کیپ ورد هم نداشتن…
البته گلر کیپ ورد هم کار بزرگی کرد و یه امتیاز برای تیمش گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93321" target="_blank">📅 22:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93320">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZhQSsnugrByJYgyrZeE5DNisQMlB8hbDdVWtUeRLRaeZOGVVRJnM3zGJ37eyc1LGaUUZ73VuW9fvcNJgJWssGq04OLVDuP_uESDNfSe-y9kSOxz0SELlMYQ41sAraCITHzMAgDwhCuqZuFXqy2UA4SHkWZtlTPUAZidODmJqn7TKRqOYYSC8qXlor_HdRkN8UMTkjOLmZo4HRKOSX3i56gSmWonUzh7Pr4fZvwcmAinjrRcfQFldevpJHTGRipnBML8D7wXGadSu8oJDhosm1D1f76jFWr9qhke-rkEaejKo9X-vbHrOnnpmOJaJtYb974WT2sXwM_zrD9HwEqk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم برای دلت مَرد، ضربه ای که تو با شرط بستن روی اسپانیا خوردی هیچکس نخورد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93320" target="_blank">📅 22:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93319">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b27f7be0b.mp4?token=roqwQsAN6aRS0iN6crT3LHx5dekpnMVrR2AB4vXjij94VlMWtR2Ku1NnoKzCJyIX5KV2L5kyb8ZOJpKnamx38gViBZF_rptxBi3kwF5XnS2Hmg97oBHysV96Dk8sMokM4jAU_jHYEAquuXj6M2TorRhFI5IN7sIgFeE-4zrsyXxG3YPpBUxjWH2oUeZdH06bBzMH5f_tdQAxe3Lr5pw87icLJMu8V2N-EC0WCTodDAr-hxE8Ntz_HdBZf7VEmIppgSe59PaJRO-XoR2cuqz_vXOuOZhhqRM8Yn-DATlIM_VqbloKeL-Ce3yYbW2JNp1Ep60qUXaiYZK_UxkYjvXkKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b27f7be0b.mp4?token=roqwQsAN6aRS0iN6crT3LHx5dekpnMVrR2AB4vXjij94VlMWtR2Ku1NnoKzCJyIX5KV2L5kyb8ZOJpKnamx38gViBZF_rptxBi3kwF5XnS2Hmg97oBHysV96Dk8sMokM4jAU_jHYEAquuXj6M2TorRhFI5IN7sIgFeE-4zrsyXxG3YPpBUxjWH2oUeZdH06bBzMH5f_tdQAxe3Lr5pw87icLJMu8V2N-EC0WCTodDAr-hxE8Ntz_HdBZf7VEmIppgSe59PaJRO-XoR2cuqz_vXOuOZhhqRM8Yn-DATlIM_VqbloKeL-Ce3yYbW2JNp1Ep60qUXaiYZK_UxkYjvXkKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
ایرانیا لس‌آنجلس سازشون کوکه انگار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93319" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93318">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/678ca94f4f.mp4?token=asHUbM1meWxQlFuUKbF-0O9L_rWoSCrAPUjT8qozYOdLBSOs9USJ7tBSspgnaY1ETn32KaUn0ZILqljgpph5YNTItj5BVhdX04jb9C1bBswT5POpwnUJcR46PegHPoTQyRzb7-0NGN-1-pXa7DZcKA5zpZVmnzX1k2r8BLSIebbAha9V0Djs360lIZad2aWN9L7oGekB0M32Pc6lFEhLqopiUDVwgMqHRBm0hYBvVwfFjLkOGLhsw5UYkuFem5XsVzdj-0I4OKGCwMbOwTz4JYUctRH0edjqrY7GUizzpgZhAP1x0na9S4xxB_oI5jeqlag3GC3Rs7PgpbAWk9L9NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/678ca94f4f.mp4?token=asHUbM1meWxQlFuUKbF-0O9L_rWoSCrAPUjT8qozYOdLBSOs9USJ7tBSspgnaY1ETn32KaUn0ZILqljgpph5YNTItj5BVhdX04jb9C1bBswT5POpwnUJcR46PegHPoTQyRzb7-0NGN-1-pXa7DZcKA5zpZVmnzX1k2r8BLSIebbAha9V0Djs360lIZad2aWN9L7oGekB0M32Pc6lFEhLqopiUDVwgMqHRBm0hYBvVwfFjLkOGLhsw5UYkuFem5XsVzdj-0I4OKGCwMbOwTz4JYUctRH0edjqrY7GUizzpgZhAP1x0na9S4xxB_oI5jeqlag3GC3Rs7PgpbAWk9L9NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🏆
انتقاد ویرجیل فن‌دایک کاپیتان هلند از هایدریشن بریک در بازی های جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93318" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93317">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ffi3Y6t6mUG3N_mk_5Y9ChOe4a_4JMunvq6QIF-Xye6ElN8k0SepHmqOWF_e6lx1PcUTe3BR9AoEuyRVcIb-GadFGH3pZ5gRZ6CuEKmDIQ7R5T3UpwPMntDfKcISyWycKxyRt-h3obcLW6w68C2mPf6446X9hyVo2WsgEHXDOea_3LPNjqQ1v7pIXaempoYfGqT09aLNWo7uGb62zuN3q4BdD4LCOz-anENFDgGsYs2XnUDwPJUolViUgoWffk-dx5w94S7qTdNybCmqz3NLOhJX-lPS0xHoKN4WtLZT5UMH_-eweYG7exPVLbgacLzZsDi7bL6VC_O43SqZpUa2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🆚
🇳🇿
ایران
🆚
نیوزلند
🔥
نبردی که برای ایران فقط یک بازی نیست؛
شروع مسیر اثبات قدرت در جام جهانی 2026 است.
تیم ملی ایران با میلیون‌ها هوادار پرشور،
با انگیزه‌ای بزرگ وارد میدان می‌شود تا اولین قدم را محکم بردارد
⚽️
🇮🇷
اما نیوزلند…
تیمی جنگنده، منظم و خطرناک در ضدحمله‌ها که آمده تا معادلات را به‌هم بزند
👀
⚡️
🏆
آیا ایران می‌تواند با یک شروع قدرتمند، پیامش را به تمام مدعیان جام ارسال کند؟
یا نیوزلند یکی از غافلگیری‌های بزرگ تورنمنت را رقم خواهد زد؟
🕟
ساعت ۴:۳۰ صبح
📅
سه‌شنبه ۲۶ خرداد
📺
پخش آنلاین بازی منتخب داخل کانال زنده
🎁
شرط رایگان ورزشی ویژه کاربران جدید
⚡️
هیجان لحظه‌به‌لحظه جام جهانی 2026
🚀
امشب فقط تماشا نکن… هیجان را زندگی کن
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93317" target="_blank">📅 21:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93316">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
#فوووری
؛ نتانیاهو: بلایی که سر غزه آمد را بر سر جنوب لبنان خواهیم آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93316" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93315">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBEhQzUmerzqgBzPHPUKUPy7UtH9IUEiy_SL3KRXmiBP_3MkQ8aK1b0EUFYs3zum-5eL9GpAUQcKuLzvRn83n_ulng_yGybERnWKi5Lu7qdVfvH-qbFri7k4CBkgYcNck6bWMgoVZ2uy1H456oAx8oYPAawB7bjFFUG38eChbTQUPgee_wLsJaHUEPiQV8R2uxopzy8Iblbz7nRtpPxVhE-VlT2SiT_uvNJN8Hrx152RwX9Q8YZreE0UNiobS7Qy8YN7Y7YCVXw52PUkNSTRfFeAadjlQfx3IvXRLBU_H6EBJrTY9DhhPAU9IjTy-MfvpFML_RHuW0FneTpUOwJexg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
ووزینیا گلر کیپ ورد بعد از درخشش مقابل اسپانیا اینجوری احساساتی شد و حسابی گریه کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93315" target="_blank">📅 21:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93314">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9Kp6a8w64bXf8aMymC7aG_-IF4rmusdGST8auVi-WadGiz_oqPewZuajYxj8-A6E9-tDix8ZKLXJy5TBjda1lbfLCLLlQ6t8sseMF6LHnczXcyfWQjWDp-8VygW1osLji9aF1to939nu27uSIYX5wchWI7-SfY7TG3GkSYbA5S4_KJHbt4UrvbFKGEbKkDJhrpD1PLCnXc54sFMX0_NeO9KYpNsgln06HGoX8m1kUwHqbJA7pCDGk6dOUTeov-ssoM1YZJ1M--bj9RB7HBVUh1nwBGkw7sJZNu2N0p-1ZlTxWr39BV-vSAiBoduwDe7rXwQOognwnxxX324CarhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری:
سبک بازی حریف بد بود، اون‌ها اینجوری بازی میکنن، حتی از خط میانی عبور نکردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93314" target="_blank">📅 21:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93313">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0IO-eTRo8VkEpLCbuZUjWneGCHBhpmGgBMcqThoJREoyGHQkeqg1UiTLpc6xZB5_H5MmdEZZWMBdMXugaT-_UU_p7D3PVaK_KsQtM8Oe3Airb70N7xrSYHzQhmo92PJAhr5QxwZ5AC-X7n9UjW7slYZaKtrSs1KR_iXM8_v2r_w66wLTbMBdtWOCHOkQfLcKFp5F0CahpmAptiCSRx-tz-uRS1b-BuwmMNWKzT8aTPcOB_1DpgPjTHShzBFaacquauZWXyNIl6lbjyQS03whbsOpu_STbYssRcm-7NUFIwHMt7cmti8s9ITSuT5AGbSvQKo6PRfregBFGuQiaLl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا برای اولین بار از جام جهانی ۲۰۱۰ نتونست در بازی افتتاحیه خودش در جام جهانی گلزنی کنه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/93313" target="_blank">📅 21:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93312">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
اسپانیا در 4 بازی اخیر جام جهانی:
تساوی مقابل آلمان
شکست مقابل ژاپن
تساوی مقابل مراکش و ترک مسابقات در ضربات پنالتی
تساوی امروز مقابل کیپ ورد‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93312" target="_blank">📅 21:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93311">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtOGMwXqmwP-yDQfv9tnIkJggoIfGkX50QUGLmh08w7Bu59KuHxE1i4VEOqfVA_F3YjGyWe9c5w3IC1fY5UY-sg3vfgMBLcq_OzkytdDEvmKleM4BvGLsCuH2tX65H5VKPnBXrLkvy5vfpMeH-2ywfF_boarhoRXPEDr8U2I1tgyIlt17H1W1WApBpvI-vTXv_F9FOo7crZDNR88344j-NGNhE9MP6mc47J6PU9HTWVxbKJ1vWGx0EFUhgdq85HRN10vZvKM9wuh_z4bzh6Sy2RQAF-116LqZLbM2zdcnR61iwgKjY8LEN1mxAXGtX9Dj77v4FGiR1m3ybtE6j2StA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دروازه بان 40 ساله کیپ ورد امروز 7 سیو داشت
وژینا تو لیگ دسته 2 پرتغال بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93311" target="_blank">📅 21:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93310">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2308e52e5.mp4?token=GCl2a-quA2bVmat9Go3Bm-R9KCWx8-9OZDT9g29IJYVH7cVvSx1n_9LxNiMEp7I5nLOZUKBlj3wSFCnxseqHCDU9WF9IXuHy_AZTsbsE_Xj5CR436ggKGauUgtBHTcM_eZgBXkxM1g9az8nuujBb4SIqmD6hDX_FjQiCnD-I9PRAteFEbI7v8lTdQiup_Y2xdy5dQsUd6GlH446-jNKyzsrQVKrLuPq40v2l1BmQh7f3ec1U7KuHN-AnP4G_gFWtRwxg9iXuQgGmMo4pGqrzqVLiO-eE87ZPmPraK8AmkY4SJZY0EdunDyjhetkF_3mKRvx9HzjpTjqcbzNC6YfZ06f55b-NSXB-oGPgl4RLji8X6Glj13nLeNsr30PU4FkwPK7fCCv5BK2LPPJ42i5dNOyeKj9OcSCLMVHrH9fqYlfwZSsSebWOK7x7W7cJnQoMHX8abQSSO_D0OYBHgM2iZ_wcCRUIN8u4C_dCzfy1YEM70t1WsYram_O7AxVu9GmPXxoPeShiqILxauly5TVvlsUSGx8-e0ZVfGECMNaMi1-at_corlp1rlvnQFFZkYPeWP-3e54Kv73Ub0KBN0W_YqPcvu8c58J6IlR3iWpe0Za35m4nyBULN8nQF31NqzpCy_JwFrFkvgMuv5USlH5SjLgPC2L4v6Y1Zk0BoexZxQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2308e52e5.mp4?token=GCl2a-quA2bVmat9Go3Bm-R9KCWx8-9OZDT9g29IJYVH7cVvSx1n_9LxNiMEp7I5nLOZUKBlj3wSFCnxseqHCDU9WF9IXuHy_AZTsbsE_Xj5CR436ggKGauUgtBHTcM_eZgBXkxM1g9az8nuujBb4SIqmD6hDX_FjQiCnD-I9PRAteFEbI7v8lTdQiup_Y2xdy5dQsUd6GlH446-jNKyzsrQVKrLuPq40v2l1BmQh7f3ec1U7KuHN-AnP4G_gFWtRwxg9iXuQgGmMo4pGqrzqVLiO-eE87ZPmPraK8AmkY4SJZY0EdunDyjhetkF_3mKRvx9HzjpTjqcbzNC6YfZ06f55b-NSXB-oGPgl4RLji8X6Glj13nLeNsr30PU4FkwPK7fCCv5BK2LPPJ42i5dNOyeKj9OcSCLMVHrH9fqYlfwZSsSebWOK7x7W7cJnQoMHX8abQSSO_D0OYBHgM2iZ_wcCRUIN8u4C_dCzfy1YEM70t1WsYram_O7AxVu9GmPXxoPeShiqILxauly5TVvlsUSGx8-e0ZVfGECMNaMi1-at_corlp1rlvnQFFZkYPeWP-3e54Kv73Ub0KBN0W_YqPcvu8c58J6IlR3iWpe0Za35m4nyBULN8nQF31NqzpCy_JwFrFkvgMuv5USlH5SjLgPC2L4v6Y1Zk0BoexZxQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی مردم کیپ‌ورد از تساوی مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93310" target="_blank">📅 21:27 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93309">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVJ9eIIRqACq6pTCfRGiIAK_iur_h9lV8WzDrlj0q0He5KJuY8Fg1txczPT2STx0ZbQrCtltRGAkZgjI0at_WK96JVXUs_6M3B_VAA7hXSyvuLA9U3t3Df2K8nNVk4xxhgLdcqEzRQtvcwUtL78P6HquRbvuXLkisMnVD0sTf0IDCdRMNPcMYRWgeInLvmcLNtC5OHriLQIX4AxcJUze-58YpR9HuFGkNDh_Bvwze0jNBt0s3WBh6S81gLj7JcU_JhBBdnlQ7SVxOTWk8GdyqTsyYKF61e46rod-29Ktwyly0BmaGfQ5V5bndCErhvFO38nCfMxRPBwjBXfkORA85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
پایان بازی | اولین تساوی بدون گل جام رقم خورد
🇪🇸
اسپانیا 0 -
🇨🇻
کیپ ورد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93309" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93308">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کیپ ورد نزدیک بود گل بزنه
😐
😂</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93308" target="_blank">📅 21:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93307">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چه دفاعی میکنه کیپ ورد</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/93307" target="_blank">📅 21:19 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93306">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3MmkpP2P9zkDtSsrPnZYI3fYDr7rZv7l_ohEAXKLDXYL9LATK6kZCUXtB-fjmqws7P-AwWaljZN6rorRAbpHQ7xwOZ8rEQLcYI75lX6MhZU0i-DqKAq2ArIsFR3D3_oArRpE-5nPUWLxcMvZV7h6MJ9eU-0B1Pl4kd-ua0kTkBCwv-ena_hm6BB5zzge5NbrDi1gJgN06tTi6v2uuFm57UzjeV-qCPhyR30x4zHS75iXt9GtrBzTUSnWuomXzBK1vuN8i0G3d2TkCiBRHLnnAvsTnUVb3zBxEnF4-7XzzbYAE0XYZhT_5QIlA5s0Slruybos7U2bgvGc6uhNtRTsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
ترکیب مصر مقابل بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/93306" target="_blank">📅 21:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93305">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اگه این تیم اسپانیا با این بازي قهرمان جام بشه سردر جام باید شاشید</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93305" target="_blank">📅 21:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93304">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6f49769b.mp4?token=P6ywHbS60OGV5LvyOQhjvXuRRXJj8xsdA2aGkE55V-Cf0006QFA7vjZS657G62s9vQ5Bwa9eULIc6CAIH3O-fqRnrN_UjlIH4_Qw-ar28PPbeT7ieV2xAGWY2m_J7jXthxGepi6n0Ryjgv5gpGRx-GwbVTRcPyifU_t7jC9euIB_tvGN7SNTC6yEwfATexpmOtbSfMxxb0sU6m4dSOhIY6A5AFx5G7YHUHsUqCwujzKOtXeVqYC6WJS6sYVWMRscqt8_1E2_yNObNbsE_QSyKLRrss_U5et6quNFrSaKAvAl5P9Mx3TToCUR_h2IGioI0_yqPzjYEBhAZbEBAZjNHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6f49769b.mp4?token=P6ywHbS60OGV5LvyOQhjvXuRRXJj8xsdA2aGkE55V-Cf0006QFA7vjZS657G62s9vQ5Bwa9eULIc6CAIH3O-fqRnrN_UjlIH4_Qw-ar28PPbeT7ieV2xAGWY2m_J7jXthxGepi6n0Ryjgv5gpGRx-GwbVTRcPyifU_t7jC9euIB_tvGN7SNTC6yEwfATexpmOtbSfMxxb0sU6m4dSOhIY6A5AFx5G7YHUHsUqCwujzKOtXeVqYC6WJS6sYVWMRscqt8_1E2_yNObNbsE_QSyKLRrss_U5et6quNFrSaKAvAl5P9Mx3TToCUR_h2IGioI0_yqPzjYEBhAZbEBAZjNHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🇮🇷
🇳🇿
پیش‌بینی جغد معروف از بازی امشب ایران‌ و نیوزیلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93304" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93303">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
‼️
درگیری شدید طرفداران تیم ایران با مخالفان تیم قلعه‌نویی در لس‌آنجلس ساعاتی قبل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93303" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93301">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a429dbfe1a.mp4?token=oyQNufY6p0FjqAAlvJ7fPRHbPy11N3BUWlkA3S7ToztN31OHitIU614i46Lzz5evQrtEIPUjt9_JEjvwqQPkyphCJU7xehEPyN71eXtioaG-9fxayDEX8PEMDlMfRPojgP_0hd_rJlSs20tKa4pAwazw5Zs624x8KEjyeC3th4EGlTyRC5HWtdIeOEXxMb3hgG2mwY69ZQ2n-rhYOKaLuLCZtp0mwfPCt1aTYW5J5lpGdRtWJI24WuBDoziNIfxmgNyFLzHBR_Rc8aAez-2K9TbIR-IOVZvXTW9a5QitDqw9dwlCcoOf_8ujqp4Sx4fSObn6dDuSZvGoS61VPfm9bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a429dbfe1a.mp4?token=oyQNufY6p0FjqAAlvJ7fPRHbPy11N3BUWlkA3S7ToztN31OHitIU614i46Lzz5evQrtEIPUjt9_JEjvwqQPkyphCJU7xehEPyN71eXtioaG-9fxayDEX8PEMDlMfRPojgP_0hd_rJlSs20tKa4pAwazw5Zs624x8KEjyeC3th4EGlTyRC5HWtdIeOEXxMb3hgG2mwY69ZQ2n-rhYOKaLuLCZtp0mwfPCt1aTYW5J5lpGdRtWJI24WuBDoziNIfxmgNyFLzHBR_Rc8aAez-2K9TbIR-IOVZvXTW9a5QitDqw9dwlCcoOf_8ujqp4Sx4fSObn6dDuSZvGoS61VPfm9bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هواداران ژاپنی برای جشن گرفتن تساوی خود مقابل هلند به تقاطع معروف شیبویا در توکیو دویدند.
✔️
آنها فقط به مدت ۴۰ ثانیه در حالی که چراغ عابر پیاده سبز بود جشن گرفتند.
آنها هیچ قانونی از قوانین ترافیکی را نشکستند!
😭
😂
به محض اینکه چراغ قرمز شد، همه جشن را متوقف کردند و به پیاده‌رو بازگشتند.
😂
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93301" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X70YGpxLOAXHbI5tvgPWfkHHravo9pCfegb0izpO_DhLuZKJAljMrSICESGzPA_Qp_7tOS4kRI8CCQPBTTUTHoax2aa9gn_mSSPkBa7fJqLwjVV-xAUe8X02GXDGAJupaRuA8IRyGstedOcTeySxWXBWk7lOr0xIdP0LUKUd54uEoqxM7QhV4n1xdTKVUnjbdOdSpGlkQ5X9pLPDNL5_ehstI6N0ze6AJm2c2XnQkM1ycv8D5Zz2O3Map0KrIqO-ZZcVuXOiNdGiEZvHsMUZ8K4pgh-Fk9QaIC87HWWkZSRNDGoVvm3GHXwLgjuzxjDrW95gOYtPHzgYrscCsDBumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد از تلگرام بدون نیاز به ممبر و تولید محتوا؟
سیستمی به اسم MTP وجود داره که باهاش میتونی وارد پروژه‌های واقعی بشی و درآمد کسب کنی.
✅
بدون نیاز به ممبر
✅
بدون نیاز به فالوور
✅
بدون نیاز به تولید محتوا
✅
شروع سریع
✅
آموزش کامل و پشتیبانی
🎁
فقط برای ۳۰ نفر اول:
سه پروژه اولیه بهت داده میشه
مبلغ هر پروژه ۲۵ میلیون تومنه
یعنی از همون ابتدا امکان رسیدن به درآمدهای بالا برات فراهمه
اگر میخوای جزو ۳۰ نفر اول باشی، وارد کانال شو و شمارت رو ارسال کن:
👇
👇
👇
https://t.me/+QpsFnjSfC382MGQ0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/93299" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dy71FOsLbl6t3buuz27jPw15K6jgeQ_IDwz4NdESTbBma8wq-kYV1zWfkU9s-UgwPlCFAKTFFY-ubGecRWio7A9vtC6615lzlYuSAvuZLuQjJ-6tKTGfWrJ6Jsw1rdp3VP1WCTiKuBRPtbWYXWVj3K58ckaIbYYpAfcn_uqOww_rs19BSAj4GukwLpDXnU9_qixXMcHn5dxPVZ7719as7zyeB4CB14syWhJu8MNDIg8V6SdGFg2AmPnzjl7UL_RmYnttL_C6xYN-zkKEISn5pWM8e3OH9EwWc-3QzWbDxwxrCMTLlNLOpjmXmgIKQa_MjaIZkUDjb_TQ8IrLuzH_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر کشتی کج دیشب تو ورزشگاه برای بازی ژاپن و هلند حضور داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/93298" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93297">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evjGjmYEFRz-xX3hEy1TMvKKr-AWaJsekf-0nlj5aA-Hpxo-br4OoMy42ImnFUjFPMdNV0089IoUjy7NB1UjMMEvKjFMlAj7DznCaL9ZX_upQDoMbeQVk7uRlfkp8230LCOKln61BMGUfQUuhDnObrQbxuUVSreSIvmVtKbugVmdWBo9qjv9ewdl02JLAd6WgAsTHL281pz2SyBZObbxR_o_1_GG7hnQlZWMXKSUJNSK9kj5ZBWanvphl--bDpx8GGAbgM3ygJG5lw-EIxA88Tmi5TO2p1heaNWDx6_FyXqq-7IwUk2WmiVWGIKi0e__hLQNsQ0Z5ihib23tlRMtHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇾
👀
🔞
ایشون یکی از که مدل های معروف اونلی فنز؛ برای بازی امشب رو برد اروگوئه بت زده و قول داده این سری به جای عکس؛ فیلم خودشو بزاره
✔️
⚠️
🔖
🤤
عکس قبلی که سر برد قبلی گذاشته بود رو داخل ربات پایین گذاشتم
💥
🆕
🖥
🔞
https://t.me/FoootyHub_Bot?start=v4ujXYFM
💦
⚠️</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/93297" target="_blank">📅 21:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93296">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یامال بالاخره وارد زمین شد</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93296" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93295">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دوای درد این بازی یاماله</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93295" target="_blank">📅 20:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93294">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کیپ ورد عجب اتوبوسی چیده</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93294" target="_blank">📅 20:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93293">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسپانیا از موقعیت هاش استفاده نمیکنه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/93293" target="_blank">📅 20:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93292">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93292" target="_blank">📅 20:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93291">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOLD0sKW1vhyn5GUsazVhmQdGiQWdYo8jhVOuFMmplqMgy3ciwyHq71XZWWT6K2CxWMC9iIfibmEgPO8W0iXYng2faOJd8yJMDZcAtx7vBigZH3HDiDGfMMDr7PUG5dWZtWDZ2gohiEHmBEy2Z1t3ytASM-QswoOa-COQKKsfa4b06UmKxBIC31Pj0e2a9NLfb4YM6UEZS96r-XPYqcrrKvkq3Uhp3WCT7jpyp8XjG1eoWDnnB2feV5icZ6OpkfD-cOQvmP0q4UH--V1qVzCLVT1PThpei0bn0DnN0WOQdouWv0P9Xk-Q2NY7ZIICn3c9mYHlkCgGYZko7Tx5ZQZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تام‌هالند(مرد عنکبوتی) راجب خولیان آلوارز:
🗣️
تو یک مرد عنکبوتی فوق‌العاده خواهی بود، دوست دارم روزی با تو ملاقات کنم، من از طرفداران پروپاقرص تو هستم و امیدوارم جام جهانی فوق‌العاده‌ای داشته باشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/93291" target="_blank">📅 20:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93290">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/510d539031.mp4?token=BD6rEE6P3-RX4sZrrdoyI4gW2xeUBwDBe8fdiLhJLNz0dRcMQXPtank0pXthVdnUqkxjmDn_k2l-LHx-oU7Z0b3MvvrnfW9WWFhTHpOb-oBf47y54pvqr6Tx-9Imq-jadzES34OoEdzvtatrNqPNv7eouyUAXZa1B42UoBBDOnYwRFhZdeimeaZM48UukAPbwNbU0W03WXkdlt-pF3dabAuPRcvUJCfTMuhbcyS8yhuxbxB5IipH-0clOFCBP0qWjg9RNV3k-oC_KEt3rr06v4lGPbcaSFbO2wbg3wu5jGYkx0NpLk1XJ2rYhFBOb7_l6m218Uu3218xUWRsEeSebQExQN_ugfBy729xwZ293R1_9Zl3aDOySK3RplR68BSr6f8b5Wij8wKZJ8IcJvG9yyFapXmIScA_NyUYHZUKmmfXhp9JVlx-kIiG7nD7ZTjf_aZ3KKq4f2Ql9mh8YukSYjVFoOXeTAojHneszfqRh7XT0puAHK6t9qlmRwqHG2yBbs7VxgpYsdzHwItKy6QIHBUJsg8A2wXKrRlWq7kFWNAPEDuvaU9GbaFMH0UHespbNvUFAz2OB3IWc013oxR_5TmzAkP1p7RKozBk3DI7X97kA4FgtnGfHgLCXPb5yCe98LNQLsJXen7AuuDwIdKlrcxv6y67mS11qoimfE-MhXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/510d539031.mp4?token=BD6rEE6P3-RX4sZrrdoyI4gW2xeUBwDBe8fdiLhJLNz0dRcMQXPtank0pXthVdnUqkxjmDn_k2l-LHx-oU7Z0b3MvvrnfW9WWFhTHpOb-oBf47y54pvqr6Tx-9Imq-jadzES34OoEdzvtatrNqPNv7eouyUAXZa1B42UoBBDOnYwRFhZdeimeaZM48UukAPbwNbU0W03WXkdlt-pF3dabAuPRcvUJCfTMuhbcyS8yhuxbxB5IipH-0clOFCBP0qWjg9RNV3k-oC_KEt3rr06v4lGPbcaSFbO2wbg3wu5jGYkx0NpLk1XJ2rYhFBOb7_l6m218Uu3218xUWRsEeSebQExQN_ugfBy729xwZ293R1_9Zl3aDOySK3RplR68BSr6f8b5Wij8wKZJ8IcJvG9yyFapXmIScA_NyUYHZUKmmfXhp9JVlx-kIiG7nD7ZTjf_aZ3KKq4f2Ql9mh8YukSYjVFoOXeTAojHneszfqRh7XT0puAHK6t9qlmRwqHG2yBbs7VxgpYsdzHwItKy6QIHBUJsg8A2wXKrRlWq7kFWNAPEDuvaU9GbaFMH0UHespbNvUFAz2OB3IWc013oxR_5TmzAkP1p7RKozBk3DI7X97kA4FgtnGfHgLCXPb5yCe98LNQLsJXen7AuuDwIdKlrcxv6y67mS11qoimfE-MhXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
هاجیمه موریاسو سرمربی ژاپن بعد بازی هلند:
چون هدف گرفتن ۳ امتیازه در نتیجه تساوی برای ژاپن ناامید کننده است.⁣ فوتبال ژاپن قویتر شده، چون هم رشد بازیکنای جوان در جی-لیگ بهتر شده و هم تعداد بازیکنای ژاپنی شاغل در خارج از کشور که در سطح بین‌المللی فعالیت میکنن بیشتر شده
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93290" target="_blank">📅 20:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93289">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs06Np4_mCOh55z-bHbwcaAUYw2RC1SYrQWKf48EGn-KfW7sM6Z8xwlviXY_ad_6320VVzrxZTXRCU87nbalmxGI6ahhyO6DqSK-jnrJ-DfFhCR9OSuWCiSgDuWK3_sAhM4KasoQrV36_9LZeJT8ZRcnUCSJ3wIpKVLvMwVQpGVzF8DBvpD3Mcbj5EToJ6xb5WD-mRAmzsZ9iOuaheerz6ZiBZEVy2aWv4QwY-EmyLjXBIiOWRJf0MHJD6RwRnhmm3NGOJt0j_R17njcBZ7aYwC7Xkz19ow93sq0-hGE5aFPQ4KCLVkePtPXT_tFz2yvK3P0jN-8hwY90vBS6-ZkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادار کیپ ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93289" target="_blank">📅 20:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93288">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/93288" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93288" target="_blank">📅 20:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93287">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRfyYw6FgxUwZ_kVcNn-mhvTJ0tWVresThMhM1GAyP-6COXbGkh8X5-9proXdMpxisLJoHF8j2dI8XbbZnKNV9-NfxE82CkGX3WPQ_OEJRYh8rjxTHBbQwp6H1x2ztJcN8X7w4EsZW8D4qQfULSGH0Wmc0Iq-zmZo47CME_HaQftC8d5ndkFpWdlTL7MGdlN2za8peUdkARTF7iQFSGdjEcT4TLDi9MeQ2YIxFaWMAEkRBU9IBPI9ZjxkgJzcnjI1up5r6EIqyH2VpWN5KwPNZPxFc4-sFUw1xqX7KFgTU10qM7wZLv-W3S_W-BODH2mSbehdrWSatAUNm2GsvnokA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93287" target="_blank">📅 20:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93286">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ih1GkZssBy2MCNuj01z7xvbCOTLe9_GTAyaqTuEwvR9eWHoBsx5PHZ4Wn4pdTJ433yTsmSFA8vAPdRD_I99979vyOpGMP25Z-fznNqZ0yIodZOk31jgGqSUzhQwJGHUTCsuGMEsljkJH8z63opRi0eC-BC31nFUxj72EFA3wVBNJazaEdchWvC7zvVgkFtCrIKjwdvErLHZ_R3WU31VMuAAw5zEvV4sIlaAXrjcbIjW0v6wjJTgHVhtizpAQ-jEVvuguHEEUP-Gl6yHy0wAXXUjs3wf9veYbxMtRvELYdrRPjUPPcfsGuwFF6UO3u6CkuCn9PGGEVGfbvpshZNDNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلر چهل ساله کیپ ورد که نیمه اول ترکوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/93286" target="_blank">📅 20:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93285">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6cm7hjWOd9SFW7iRjGzv-boCXmqkdsVs8X_0AlMtiY4hOOaFpgYS12MpLXr77c2kEmDKNC3UdMGjTxzhfwjGCZWOGROBX4fn2hquObuiTs2TcAjs4pbOMqpGaeez71KEog8x-RsIrz-9M7hYafjWr09bfKiE5ChrHlcj32b44_OKGAW9V9Lvpu-Q93QE5U7rc3Uc0FeaiSEW5wpwwkwf1cTboXOwC0GDFaGOumxLiB59R2-RqpnIcqWkc1PaSS5lB_I0ZumO3Lbog78sdKMRTcwm_-ju0Jzu8ck1k9uwZxqpvfo66eni1IMVz03mSsSRmSOQaLmdTOyoUazlbjnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🏆
🇪🇸
#فکت
؛ پشمامممممممم!!! میکیل اویارزابال اولین بازیکن در تاریخ از سال ۱۹۶۶ است که در ۳۰ دقیقه اول یک بازی در جام جهانی فوتبال حتی یک بار هم توپ را لمس نکرده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93285" target="_blank">📅 20:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93284">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پایان نیمه اول
🇪🇸
اسپانیا 0 -
🇨🇻
کیپ ورد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93284" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93282">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کوکوریا چقدر خوبه رئال واقعا سود کرد بابت خریدش</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/93282" target="_blank">📅 20:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93281">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عجب گلری داره این کیپ ورد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93281" target="_blank">📅 20:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93280">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">عجب گلری داره این کیپ ورد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93280" target="_blank">📅 20:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93279">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK6ZqkYEC84EVJcXhjfodzpqE_Itzqlix5y8z0xcJrViQGRzhGzB-gUFPj5bnMmillrICCFg1u3QIRlUtiM_btTyJCQWw0KAnRgXSGxBKR5kQ5BH-mFrLfZnX-HFhLk7_LecHuVsmEhUICTa9PdzUrUkwLM_PNDpJmbTLmHI7DLwL-vj-57vJjDQ407g9e01mdXeNVczUYFlUkJauimO96ZIzqiTD9ERifsdQ8HCYW1HahzhgTfavgEP8KgJx09cuYnnSozvpfgknFyOZqQNVf1E5biffc4FnJtC8nelGmWvUeIgiU_i8bMX7BnuhkonHBoQQ1V6X9r6CmTyQCESmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تصویر منتخب امروز جام‌جهانی؛ پیراهن زیدان در دستان بازیکنان بزرگ سابق و فعلی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/93279" target="_blank">📅 20:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93278">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpX8JzJirHPBh1MJpPMHK5DPNtOb9j6_M-imAbQ0UrvZK0PzOU4CBKLiYcwdbD1C5qwj_mfFzeyuEA6p7dM-BdcYa988cKb7g9rBE-FWvzRG6lZkPfo7dPVKh6cbTgKrx-RwdhVducYyNhiOrHX25JGU2z7jdP48SOaAtELCsWszSRSJ2V0blwzXkbntpSqLX1YJ2hORyH-c01_ouGdn6xGBb-EaiV5qJ238nOWlMVvXjyarrZjAEylqm-q-rD2bX4LpKo9Usk93TY05yiaB27PnhtjArjeoY5xd1DsqBeqCuuY84C0C2QfZN4uY7ojvEedx3g_krnwvfuOKCih9wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو حالت عادی همه فکر میکنن این توپ گل شده‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93278" target="_blank">📅 20:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93277">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فران کوسه چجوری گل نکردی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/93277" target="_blank">📅 20:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93276">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پشمام اسپانیا تو شیش قدمی زد تو تیر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/93276" target="_blank">📅 20:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93275">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسپانیا یه موقعیت عالی داشت اونم آفساید اعلام شد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93275" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-93274">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خوابمون گرفت از این بازی</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/93274" target="_blank">📅 20:05 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
