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
<img src="https://cdn5.telesco.pe/file/XlSyKenPPXmNxR2dMCPJzt-Efpbs88W-pHjrRzoHx7BHOklkPwBAwUzYcfW5OiUHuOa_ELyxHzadS94V3TbB9VQZV761JlUaXZqUSWXqtAR72rCIpBkfLQoFVTr_a_uB3d9wrZYz-VpT2OMrtsvLYnTphAAj0-fPHKJ_QOublKqsL3vvhjKnTp9K08u0ACbPhXVS5CLNkxlh8FT2wenB1JV3cr2K3uV0uqv5SFsaCEchBVMnV2HoB5MDFTOu1B7_XeXWlFAUCFinVwQrSVgM6UJpbq9dslaZPaDCrajWIzNyUejQmg_gyeI9yKroKSEp9lA4CdewoP7iYo0GPCXKXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 673K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 09:01:53</div>
<hr>

<div class="tg-post" id="msg-94373">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=EfOm8o6KKIbAsXx5DxNy3v-NtM3ZthRiVRlTS8Eidgwosfs4cCSJ9XeHukPUqIUOCjooGS5GX95E2ZQKtxs2XP5odEUoP0IxD3cEs3eDHcerV6LhMEM1h4GSdkHRUUDePEYzKJiQ3FyfjBhhivdY1UoHgK-ecS9A3CujaKBdkQyNQy-xp19_v1gAbA-tD2H6W7Ppa7K7Q7B-zKvaD8qirc8EllA6VDpyR_Z9tpt2-moaDGS_6ynTIx0Ijonzo39I7RbnfvWbg-nKW4Wby4fRfRUcabJDIGtJeOg8oxlXzMwUen-xHAWzrOZNCJrBU7GDZ89XSJW0LuHj5_4fnN0ciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d0441ead.mp4?token=EfOm8o6KKIbAsXx5DxNy3v-NtM3ZthRiVRlTS8Eidgwosfs4cCSJ9XeHukPUqIUOCjooGS5GX95E2ZQKtxs2XP5odEUoP0IxD3cEs3eDHcerV6LhMEM1h4GSdkHRUUDePEYzKJiQ3FyfjBhhivdY1UoHgK-ecS9A3CujaKBdkQyNQy-xp19_v1gAbA-tD2H6W7Ppa7K7Q7B-zKvaD8qirc8EllA6VDpyR_Z9tpt2-moaDGS_6ynTIx0Ijonzo39I7RbnfvWbg-nKW4Wby4fRfRUcabJDIGtJeOg8oxlXzMwUen-xHAWzrOZNCJrBU7GDZ89XSJW0LuHj5_4fnN0ciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇳🇴
پارلمان نروژ تو جلسه دیروزش بابت برد کشورشون در جام‌جهانی اینجوری جشن گرفتن. خداوکیلی کشورو میبینی ارضا میشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 311 · <a href="https://t.me/Futball180TV/94373" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94372">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=IcdqtGSfP3hLiMZenwPp_TT2BvufoS2QRxAI54S8o0T8eoBDj1mhtAcD4pr-whSF_un_tNKLFlEp-QFggEPEjMeV-OT58LLcckDZFYTW93elovMKlcEp2F7lICDMa-37EM3ty9lfUxWDm4rk5aZJvWM6fucV4akGbm6HQ1BmEr59bbdkSVrapULSB6wa9koPE9LXec6260XbRFF7SWCCfOm71dUi7ubr6yhPA46r5uMLJtEHv9Rpaej0opJzgYJdMwKhov9R-npZXW8BDn-iPCMH5jogvOBiPqaBQb3vOveozMTuS6FuYxv6tiPDpvon1Nqu5ssrCD6661rTXDsqAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b1fbc3691.mp4?token=IcdqtGSfP3hLiMZenwPp_TT2BvufoS2QRxAI54S8o0T8eoBDj1mhtAcD4pr-whSF_un_tNKLFlEp-QFggEPEjMeV-OT58LLcckDZFYTW93elovMKlcEp2F7lICDMa-37EM3ty9lfUxWDm4rk5aZJvWM6fucV4akGbm6HQ1BmEr59bbdkSVrapULSB6wa9koPE9LXec6260XbRFF7SWCCfOm71dUi7ubr6yhPA46r5uMLJtEHv9Rpaej0opJzgYJdMwKhov9R-npZXW8BDn-iPCMH5jogvOBiPqaBQb3vOveozMTuS6FuYxv6tiPDpvon1Nqu5ssrCD6661rTXDsqAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
🇫🇷
دیکتاتور امباپه تو تمرین دیروز فرانسه رفته جای دشان نشسته و عملکرد بازیکنا رو میبینه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/Futball180TV/94372" target="_blank">📅 08:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94371">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSJGGPD7ggA2svwyXNXCSPON5xxbbFpWjkUVweJQEUD9nPm3PcqGIb4ImDN0poAPomd3M6V-9WhoesE-3TvQa53RCn6dF8JgD0_vdOyLstzP4MQ1hqEKRT0x1TTWARu8VmXy21Ka0fejgLHz3MVxWfm5MKkR0bv5wm72URSdz-uQ2sjr6TOMUKY2jFSkjtTzhnt3dgTIK_8VKYtg-LZnaBK0oF0rbhckgtgUQTVRrd57_fLw08xfTT6z_YzzIi6eIl-2Y24nCUZgXb9eHR1ZwjVJILMHf3kIVIF-YvDxESq_QETwQwrgB3CcGdIu0xedmFgZW8ze5Ax2tHy15KVLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇦
#فووووری؛ اسماعیل کونه بازیکن کانادا بدلیل شکستگی استخوان درشت نی و نازک نی حدود ۵ ماه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/Futball180TV/94371" target="_blank">📅 08:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94370">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/Futball180TV/94370" target="_blank">📅 08:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94369">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyNX-WADRY6xAinqEH9xcUSs1BcySafhrbCxJVl7fEyyqslb1YiFBHvnCfDMojuloRUv2hdgoAJ2szmCCk1uHcnSqdnvj8sG3MHgLDEmCFUoYDWrskT18eL5MEGykQ1aAQNOHb4-vTlXIS2fqV8qtMw_qTvu9Mc6wgqxeQPopqKYWDbRSMsVUHYnzTC9QFyppAwUadiYSu_pPeZEnuCD4nOJwMDVv8G6MVzh95AGR9EzMKyUSiy05HwDUbJhaYAosHz6HBbfc-8EayPmQYJVKardd-hRPAPl6wGHkP_4D8D3uU1f6ETmW-6aj1pMjpdcmJmktb2DVCVaVwyMuA8DkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لوئیز رومو بهترین بازیکن دیدار مکزیک و کره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/94369" target="_blank">📅 06:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94368">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drtfcjlHqnMyNA7Pv8zWD_4qTe574jwa2C6w6SzBvIR_Wke_i9Vh2sX9OibiaWsG2OjSsRRap2yDlte3oloT0sZ5b-OrqjsXw2nDdGklVYzJRFeaVAMnoeyPGNzEsSIXZ8Jw13yBJv6jK6fkCGI4Qy19cw8SaIOcVHoKcHdk97Z1V-p8cLfwgX14l-IVcfPQnMTMQRGR88V_fBrFiH4strFDrPE_VNmH_zZrooCZZ_04PWzu8Q6VkvvpHprdtA9cHJB1PVYW6_z7CLIpAHxE7iUgGrqTZPxAKxPr6_PNeXzEwwM7LlVbs7It6bDhAfOujtpYrf6CvddM2Y__g_3ciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول گروه A جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/94368" target="_blank">📅 06:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94367">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vw-PQY2QOhqCAclKtUA4RbrvsSdyEWkf2MzKIxlN6DgSJsP59XLotqhOZCQx8WA6n_A6HJKVDAm8u8SXVPyCtvih7MHgwOQTgLFIl3mGUXsE1pC_OpYpXDWEFyQEsYvbCdFd7_PZhEG5dvM93aFPFb9JA2dl8tdDnOmSMtKuD4En1jEaaL77CaxL7qb3Jh4fTXzG-Uv69lQ1ugLaECdyqPdQjkpgHdFDFOyM0_cz4V4j6syx-KEaocoiOY4nRnRxFdVnpmXXQyM9oYbSmdTR9NG9fgghhOX0GZg7SBmRXGlB9NinX7zVL6NFO2zgP2_KIFWdaF9fo3xwOf5w7VfM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🇲🇽
تیم‌ملی مکزیک به عنوان اولین تیم راهی مرحله یک شانزدهم نهایی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/94367" target="_blank">📅 06:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94366">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10d309995.mp4?token=dH5s7-bH_1ct7jbhCQiPBWdWesy295PjlZTTGAtRI9ZSWtBLo4Q2lKPIiEpySZppQu0OSak4aid7YvNw8sMb5yqt23jPKYUKT-Yda_bYVDktK1q7ORURmo3IDfO6rV0jJygbF7M6cRqIdgvXNWi4OPbCQqHOGkoqh0hN9PkkV4Pk8BRx11b2OtoXTEfYu5Gp6drUC35bEaeg4z0cSs0le9PpuiiZcpGerwijpWs-5_jCjXmzK-GV4WLrarPBUv842xvFKuKrivfmSHeiRXSHSq_NwgDwDrWtUHxiPOqUuj0q4DGVJ7-qqdiFgvxCyhOW04uYVwY2s8WsCQeN-QNCxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10d309995.mp4?token=dH5s7-bH_1ct7jbhCQiPBWdWesy295PjlZTTGAtRI9ZSWtBLo4Q2lKPIiEpySZppQu0OSak4aid7YvNw8sMb5yqt23jPKYUKT-Yda_bYVDktK1q7ORURmo3IDfO6rV0jJygbF7M6cRqIdgvXNWi4OPbCQqHOGkoqh0hN9PkkV4Pk8BRx11b2OtoXTEfYu5Gp6drUC35bEaeg4z0cSs0le9PpuiiZcpGerwijpWs-5_jCjXmzK-GV4WLrarPBUv842xvFKuKrivfmSHeiRXSHSq_NwgDwDrWtUHxiPOqUuj0q4DGVJ7-qqdiFgvxCyhOW04uYVwY2s8WsCQeN-QNCxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل مکزیک به کره‌جنوبی توسط لوئیس رومو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/94366" target="_blank">📅 05:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94364">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گلر کره رو
😂
😂
😂</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/94364" target="_blank">📅 05:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94363">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مکزیک زد.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/94363" target="_blank">📅 05:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94362">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گلللللللللل</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/94362" target="_blank">📅 05:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94360">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnBuiUK36y6fa2tzyCwQiXqC9Lh16NRmIaw4FuZASiPV5Ercm_CipBV7_3ysdA1FZu4K1hZu7SGLj1BG_oAy4bW3yjZT8-oH9HSTi5ZB4SOhTwZOkFRREcJLQ8zn9Ar9GeZbpp1jVujy6r0cIIQPIMtpJPEkwFJSV3Y3OXFLhwVdSS3OKcmB0_Si9IJLk4D7Cdzb8JsBtrUWhNdsn7Wqy0zGT1ThL9Eyi7sj-YlPE1BhjGv8jEq0kJ5-5qfujw2Jk3Ov0GFxOl50dzVbd9wnIPjPl248yt5lDvsZqZ9FFCZNb0nfQdO56-8wfDTJbXXpka_EC3GefTzZTAZA08tINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/STOx51UQiO5uh36mH8HI3jY7temzF6jePfOJ0Pv78RxakuIm20Hv2BXIwvnnVgbiAG4iW4zJXrexzRAY9aqAPS7fpBWqpIPNROCUwXMYanNkK_s0jwPixTMjgsc6R4c5TLtMIZlFDK1Az1EeXWePrRUwL2ObXoJsicIeQ6GYrcFc-2mjkqUSLAYFFFN1XVZxC2S1SUA0dF3TU95wx837vAlKsamPsI0SO1KiPBxdhoaUbadPGUJTNEteshjzzkDT3dug1CadqLr5BZCKkXbCBNOWwyJYqzfYos7qCsmTp9zzEHhjjVHYWSVzmmp-l10vw3IroGah_vbm3oG2tOjQ7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لاشی داری به کجا نگاه میکنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/94360" target="_blank">📅 05:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94359">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAPJeK6n27IYOHYb1nBTWZ5655N4ZfcdpJ55zBHAhdVm7TAq19HRZmQ7fEW5ZjB76sKzjrDb5KZ9-ShU__E-l9kYhBoj7PSF-HVrICAJoEU7cMkBpsXjhjhDtiBJE5oOWHZC7jiAnYZZpeW_dYFRSY3Gil9GrBwFqlFDz0MVJe5bbApg8iUfILOdiQ8uDscXuGf5Kshm6wQN8lii0BcdDAB6XFA5hMkLKcaafbQZDylj2AmOsLFJ91AR0vuoRxnXl9GeqaXnrw_ng6KXAFxQKzgbXb7ME-HoQyQi8DbP_9JW-2eRrtDEjLn7oZ2IGNGaDj_jdgr0XdlL99yjSNo_3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کوچولو تنها کسیه که میتونه بگه از نوزادی طرفدار تیفوسی مکزیک بودم
💗
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/Futball180TV/94359" target="_blank">📅 05:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94358">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">پایان نیمه اول
🇰🇷
کره‌جنوبی 0 -
🇲🇽
مکزیک 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/Futball180TV/94358" target="_blank">📅 05:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94357">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عجب بازی ای شدههههه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94357" target="_blank">📅 04:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94356">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efe5f007bb.mp4?token=lWfqUUa9MsL6wRktYQHYIvnGtZC-duy-ShdN1abPxrbvdFfYBepYEuiqfeqXXZkQJFZwofvJyuJcBmx8j8YgW97yV58G1ctZT6DVnSyXkVRtCbmKnuJdoPn8SV3s5EBq4uve_ZINJL_-p_SeCPlYiqQ2vLSBKekFtyyAXlvcsyWv3Wld9_4vTeMN5P8VI9sfGtqPkeyfK-lvNACHxbcHsbAMx_KNbO0eJ3ZOr_3XBPWOTqzK48iYL1y8V8oo5fxP2yT1EcmWLSM23zCQ26qFs3iHMOJFg_siYxymLP4m4Di_opVXfUKc-z0j9mzQT-3m5_Ywdrn3oAmZXLaFhvvsZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efe5f007bb.mp4?token=lWfqUUa9MsL6wRktYQHYIvnGtZC-duy-ShdN1abPxrbvdFfYBepYEuiqfeqXXZkQJFZwofvJyuJcBmx8j8YgW97yV58G1ctZT6DVnSyXkVRtCbmKnuJdoPn8SV3s5EBq4uve_ZINJL_-p_SeCPlYiqQ2vLSBKekFtyyAXlvcsyWv3Wld9_4vTeMN5P8VI9sfGtqPkeyfK-lvNACHxbcHsbAMx_KNbO0eJ3ZOr_3XBPWOTqzK48iYL1y8V8oo5fxP2yT1EcmWLSM23zCQ26qFs3iHMOJFg_siYxymLP4m4Di_opVXfUKc-z0j9mzQT-3m5_Ywdrn3oAmZXLaFhvvsZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمامممم دفاع مکزیک عجب توپیو در آورد
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/94356" target="_blank">📅 04:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94355">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JurK5lqF64iJxqmvUT9hoRGTYLb9bj2gsrch7x9pr7EfXvD3TZ5wV5EE1e0MTKuPso5TM8Jn8SGVn37vt3s2Ksr_pD4gynnI2bcBU625sbstQXu-YzRkTDqLS02QI1DRlCdMGYA50r0y4VwoIrxXQ-jWSx94P_8Kjlg3dz_xNwMDfOJKjCPfBUn3tCrXreiDerzs51Yxz3g2w2yMlw_ec2vr1imuqkoNvzEdloIXATeYbeL-S7H0HonJCaQh_zRwum5F3-IhCi6mhe28j1gVq6F4U6H5SI5J9rhM__0fF_GvXYuDWutDWYJJllob6Ka0v0i1RHi-DayMd6d7F7nZsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ تنبیه و مجازات قطری‌ها توسط میزبان در شب تلخ مصدومیت بازیکن کانادا
🇨🇦
کانادا
😃
😏
قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/94355" target="_blank">📅 04:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94354">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/466d0061e2.mp4?token=vocil7r5lsLL2y4Dw8-3Wd0iDGzCqAKrWWkptLD0d7q_mO_zFTEf0cJwHDFs2VgYjC0ulM2YmzUJFC2mjdLUYxS7Gs4hBJF6eXU-Lfdr-eibXnhR4_DVrz_G4fteo1FfkXFiFgi1ahI6nTTUnkZDhzbRPSvJlS8Uc-oP6UOCgvjyO6G6jXhLulXhZN2KkBycutQan9J3yRlGIoOIITEAkVRk2LagAsAqTX108-_S4FFGJo1WrprGLj1RcqSKvJaAYEPoppMflgZYhgfFDZ4x12Cm2-W319hbUmKjsrhqHwp5nzMuoXIXZ_0ry0xAB2BVLxqO7d3sLt25ABxM6sbEnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/466d0061e2.mp4?token=vocil7r5lsLL2y4Dw8-3Wd0iDGzCqAKrWWkptLD0d7q_mO_zFTEf0cJwHDFs2VgYjC0ulM2YmzUJFC2mjdLUYxS7Gs4hBJF6eXU-Lfdr-eibXnhR4_DVrz_G4fteo1FfkXFiFgi1ahI6nTTUnkZDhzbRPSvJlS8Uc-oP6UOCgvjyO6G6jXhLulXhZN2KkBycutQan9J3yRlGIoOIITEAkVRk2LagAsAqTX108-_S4FFGJo1WrprGLj1RcqSKvJaAYEPoppMflgZYhgfFDZ4x12Cm2-W319hbUmKjsrhqHwp5nzMuoXIXZ_0ry0xAB2BVLxqO7d3sLt25ABxM6sbEnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⭐
هدیه جالب یولیان ناگلزمن سرمربی آلمان به هارتموت شرزر ۸۸ ساله، خبرنگاری که هفدهمین جام جهانی خود را پشت سر می‌گذارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/94354" target="_blank">📅 04:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94353">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بریم برا شروع بازی مکزیک - کره‌جنوبی</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/94353" target="_blank">📅 04:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94350">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWslKHE_uuMdAkk320v_aF56_nFWT693wWVxqsvnMFRAs2QMucydiBZxeT1xdaE67RFmRKA7M3NaoIOdxHQvgiEfSyC6ozS7bo1fiCykveA6WpUntJFzmhuxIINxtVpzQd9Bf7ASGgWfRgb1zZTXDL69tx-adovye0epX5J8b9KwTzSWB_I0JNpubRIz8RhZIdsQNzzqUBtPN-BnongLsx7odXzDj2HTWkwScIYZYJHFSSckXoPzVn_PE9GMyRQSZ6QLvHUtZj-yr4TbxP0-oiQPxRNoXTq3_WfeDXyKN2ihBGZm-ZzTV4ZAjOQfr5gJisrFMPtGRz-rplMFnN7kVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSeAbNRQrT4NJKwNbQf3GBGp552SyWuv3emw_0qtEiiK32es4iRJT3lMD8raDrs7z4diSxxRUuN-Miv_ltEBFCtXxK43yE4ru94f4csgvC-_ue2hPWKB7OVv9zBvZjeG48jT9wqDvhP4nR2iAghEgxRzV7V2c11aj7Q_GBv7goFZ16yYz7YQyksNbuvIrMNq_wx4scDed_e4zmOrZVC3TABrLpGfAo_xkcGlq3SiMTuApUAZHAYsQsqPSkhif5qddoH0J72XgJs1eXYruD-n0w8GF3nwPNihnEx_FE00aSfifd6lRlzyjYuaY8kNgRnztDwrTu2nzHASusGbOqKTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXkEJRxMxDEMABvkjFYipV9e2XqYbRO46OKwl5z2lFVWMCD8uQPG7Og0cej1so4V_6Zmrjghf-RB_KkFUf7ynB80yek8qFOeZ_USwoLikLk5TSPUyC7eOg70FcPMvt3O1VoTIgVmZ3q_5D6UJmX1yYrqqf-tAiKcLZj5QUd2w9Deb2TgjQTo-UNvqQJuNpIgX06E6Y3QeKO0F2O0kL8WpgkaKyJGZYfKypCgIMOrvjrigsCBPQY-hvQHbOmkkHJaCnapK-rJ1sGvVBorAFylvXqsJlYWwWh-ZNwaEobbnjDSoou8y4T932Sbx--IAhOVFNjjBiirXknQ4YdUZdv6jA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قهرمان دو دوره متوالی جام ملت های آسیا مقابل کانادا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/94350" target="_blank">📅 04:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94349">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c256eff540.mp4?token=jD-kIUWZjhv8_d4_jr9IlaRiyIEKU7VyWWP4NfrVu4InYYB8OOMUUhggD8cnsT7eHN3WtpVl1KfFUL6uAv6ze1qrr0ME7IZhoByr9xxLVx9TdDB8gPgTp5CESEzd4o7jA3oERJaZbfNZv9B3eQCZmkSWAg0Nrv4JmywYj3FX8qDiT8LnFpDPFh2R6s-WprA3zhhjZhqY9i3HwVYJbZrD8BpoGpqTxTxwludR3h21emtJsvE870lubqgELW75zc6-ckvJSSH33gJYv8lL-xDYPIiE8aTtaSbYZ-lxoLxJwQALiQNm89IKjIBc1Zc2G6U6V1FL8e8ogMrcGHroyS564g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c256eff540.mp4?token=jD-kIUWZjhv8_d4_jr9IlaRiyIEKU7VyWWP4NfrVu4InYYB8OOMUUhggD8cnsT7eHN3WtpVl1KfFUL6uAv6ze1qrr0ME7IZhoByr9xxLVx9TdDB8gPgTp5CESEzd4o7jA3oERJaZbfNZv9B3eQCZmkSWAg0Nrv4JmywYj3FX8qDiT8LnFpDPFh2R6s-WprA3zhhjZhqY9i3HwVYJbZrD8BpoGpqTxTxwludR3h21emtJsvE870lubqgELW75zc6-ckvJSSH33gJYv8lL-xDYPIiE8aTtaSbYZ-lxoLxJwQALiQNm89IKjIBc1Zc2G6U6V1FL8e8ogMrcGHroyS564g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁳󠁣󠁴󠁿
🇲🇦
بارندگی شدید در شهر بوستون قبل بازی فردا مراکش و اسکاتلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/94349" target="_blank">📅 04:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94348">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz3018yVS1JllsTJs2BiKdDdeDS9VRD7aG_1AmYwEItjLDvmtXja2MywhDXAbFfu6DUdpNu8dQRcUQBuhzQ5jt0PhqsjVk456nrr8mUpywOem3c54OgSWqUGOxvPsPj5iWJpzzEbPffY7HkhTMoiQT70xViCa5dSMZlG2s2z3MN1ZOAXqColY3IkWd6RkE1X0BwWiG_DZWxP0GSi9ZvyJc9UsdCN-J_-S1zuxS4x_QYSztjl0NKHvHjZFzmWbQlQzsx8URoYMlbmg6e8VliP3FRvFRUXtP1C5gwDioEhTlw0JdnOj3gHGOedyjBXnFupjpKPb27rX50a-MHj6mxKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جاناتان دیوید به عنوان بهترین بازیکن دیدار قطر و کانادا انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94348" target="_blank">📅 04:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94347">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgQQY2ZlA00WxIQbjghdXygGUc6vVSz1-zT29lWvd0Ks8AoPYngLmvbjzauX3MSiaEpxA59ylAKen5Nu3U8GX_zvmgjnkm3gizdX0WojUj_5b7HUo86JfedKSPfagk2uqiwDWj94IxMglpWV9FUf00HZt2vOODIsT7ePmpPiL2jzTVyZ4WoH94WpaIymvbT2WokLcPfCZfP6WvyfydnXHNcCvBL-qKldDH2-rpt3hIyMXXNV1Sldbyndikhlnt-V5kBH7434pSXqmJOd9ITLJmX8wGP-PO5_kMy0SyTWYVS1W-bdvR25zTt-FVK7oDY9nW3vvCvtGvV-Tkh6V8y0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
کانادا درحالیکه در جام‌های جهانی قبلی موفق به کسب هیچ امتیازی نشده بود در این جام‌جهانی تونسته 4 امتیاز کسب کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/94347" target="_blank">📅 04:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94346">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d24c944.mp4?token=b_J9BnxvvMVurf8DNkFmjEENSYBIu8bM9gcLS_OEyWBL8ZKkp3MSqddW5bN2wE4_bj3tJurET4bCI67svLVTf_psQj5HixWY94kxWQjQlrXilLzLz7Cpnj5M3faSvnDLlc330MHavMgqdgDhToJkXmr2BYgYUfRRbRh5jfvAhVrepqBzltdwAfo_mBsRG4ciKGc0xeJ_9uQ9mDSB5KUW3S8j-hakzVub-mr4o1qQAdL30ix190Tp1o6oAT_i0OptKdAQDmZqJZ4FUgAPWOGsEvvt3f8xX0TzsIbJhvbmSTbfTuCP_4HMLb-09CCWCJE8EnomLzmAzU9Ra-0Tmxt2nmHdcP9KIqwldDlPCmnQlJZn6xw_4Ix9tF0XfPoYUDOO1I-PTEIOoF7wYLj8rSVAAnpajqs91MCn3npP3_8UbjiBodLvUMgbAnR-AUl8Vb2CBhZxdqNKVJ8AjIdOTCFupaf7ccB99uhLpIwgRqZaoQnrpBriWjXcz_Is8KfXQc2eVHRludriMZs3pYaxGW-4ZQT1v430GGA57S87uN5OFvEuekRNdU2MqCPz9HATPe9M80HJB7XMIelf_7ei4IFDVCn9CEmLAqwtem_FHNJjPPeOyn7OWHeBULrMdqJYn2-ktpMRqYyinetmN-QPepEl3ztLQSv7Uqo32kdJICHxrEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d24c944.mp4?token=b_J9BnxvvMVurf8DNkFmjEENSYBIu8bM9gcLS_OEyWBL8ZKkp3MSqddW5bN2wE4_bj3tJurET4bCI67svLVTf_psQj5HixWY94kxWQjQlrXilLzLz7Cpnj5M3faSvnDLlc330MHavMgqdgDhToJkXmr2BYgYUfRRbRh5jfvAhVrepqBzltdwAfo_mBsRG4ciKGc0xeJ_9uQ9mDSB5KUW3S8j-hakzVub-mr4o1qQAdL30ix190Tp1o6oAT_i0OptKdAQDmZqJZ4FUgAPWOGsEvvt3f8xX0TzsIbJhvbmSTbfTuCP_4HMLb-09CCWCJE8EnomLzmAzU9Ra-0Tmxt2nmHdcP9KIqwldDlPCmnQlJZn6xw_4Ix9tF0XfPoYUDOO1I-PTEIOoF7wYLj8rSVAAnpajqs91MCn3npP3_8UbjiBodLvUMgbAnR-AUl8Vb2CBhZxdqNKVJ8AjIdOTCFupaf7ccB99uhLpIwgRqZaoQnrpBriWjXcz_Is8KfXQc2eVHRludriMZs3pYaxGW-4ZQT1v430GGA57S87uN5OFvEuekRNdU2MqCPz9HATPe9M80HJB7XMIelf_7ei4IFDVCn9CEmLAqwtem_FHNJjPPeOyn7OWHeBULrMdqJYn2-ktpMRqYyinetmN-QPepEl3ztLQSv7Uqo32kdJICHxrEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه کمم به جو سکسی هوادارای آلمان در حمایت از تیمشون کف خیابون بپردازیم. هر چی عشق و حاله برا ایناست..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/94346" target="_blank">📅 03:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94345">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH0QEkORMP6wKaZnAD87NpVavwrkjnMqA71olaXKAgC4UPDTJ96j9FsVJYF_WYKNgdIh2FYnwKN0KaRgL8xHDwNKZyBuHivLlLH39B-v8BvIDvGRJ_p_uEExvNsl02yBjN5MIm8_IrjDirJrYGoj77gcjT1EjcuSDpwHuwLZ9tsAGIDXSncBzEgASloSfzJwVm41goaRHTox2VxlQ0q_txnYiJRyovsEIgOR7O4QtduFwE6maLKwOHKdc9Ihkz9xAue0Gvd7Xs9JJQyObVICMM4lDHGsJQqq5qmQGWC6EREsRxLoVwUa62WsPQvWp22Av_aUuQdgRXZnNWvGCAiLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
این جام‌جهانی برای رامین‌رضاییان از طلا بهتره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94345" target="_blank">📅 03:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94344">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_3P_xgzTi4Sfn6VgZwXYqK2BB7XoI-tfZN4dClBzL5b4lSkdsry4YwUKLUYa3577pGujKogk-PCDBWDI0Ei51VrGji87_P7Mjujqs0AQ0osdyg9Q37xE0-v8msfkbpb5Js7YH2qBIU2Dlc6oy8d02cGGNkNsTcAuOaXYW5NJvsReOGP4cRG6vB7T9YvxjS9XeHxEl6jdErlRksxVdQb1mIB49d6dKxnhWiZ12F2RtWQJZQjlB-WTHcJ2pweydRGdxkshvxJoOgHu-Dy83Yr7NN8za_0E-MWXh5xut4pPj8mcqvPbadbghTuVNY4h4viHW9cdfr9ryRI_ejLlz7Kag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
جدول گروه B جام‌جهانی که تقریبا باید گفت قطر و بوسنی برای صعود باید برای جایگاه سومی تلاش کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/94344" target="_blank">📅 03:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94343">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9jGHx4-AZByKewkogkhEgRQkgGGkAwgDcQwdbZRR3gOp7acLLhsdTKOMZ0b1vLUhYOkxLjMX55-iAxMbZQt4du1Q1uZWyXaJD71lDI-ByrF5MjtYghZBI2Y5NmEi0RG2JRYl8y1NMW1s1YFemg8XTmfbMsRt5C6a98kFwJV-gOuKCQJem1V5vXCgdlgyrJ_gSW1KEDkDhvPRX8wwd8x4Xin7SoI98DW4_H5tT3Gjoxk4gnl4AYkfgLcGynHZfFLeyfSOg4YU2cMDyYGS3gJMLwX9-k7OWBV6qL2IVVWc0rjMuKpTrAdFd7b3XEAOfapNTeCL5QBPyNSdCfAf-Qryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ تنبیه و مجازات قطری‌ها توسط میزبان در شب تلخ مصدومیت بازیکن کانادا
🇨🇦
کانادا
😃
😏
قطر
🇶🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/94343" target="_blank">📅 03:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94342">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=mtxJckcfTYWJjDnc4iUUYIC2VP88_FKKL9QGM-pCHRPXFYa3fTUeEek-O6P9N6zfQySwuqTdpY2vOVBaY9WJ7GewXtEE0oLm8gZvgm4d6X_S8Xz8YJqc7s67Nh7KhchuW_3uwe1LNZ0JbuMXfyfQAVrcblKg2dRWmhAbic1JbseDpyu_AdggBg7n7kYcwQgIHsSYwMDv3ifAi8w43YHmTSopqff_UTyfXtT1ugUKUUdnweo6dY7sojPtu5iVQrkzZ6SIyjQO0ODHCrYSarJsjiRqDs0iTtyAi-u8Nh9s0zGaHuuYsGdJmSwUqzz9TwsgwkAAPucqImylF8GHRzZF7X1DmBk-Bt4ThoQZG29Y-j9pPqUflswNX6ieR3fQ8PnsCuLbowDwQ9ficfzEkxA_y0K9W5JpWX-jt7cj8pzfsmnj6plb8GXPMKwV9_oHGldXNTCQyo115FqGb5Bv1aTSHUQ1Ugrq3n87giRpKy2XQB_RWWzCJtD73AbXg96hoyfWSrS8XB7MT_u-oDPDdZEITVkCqQuWC6gIWcby5OOOFPNAYMWiE7VxOp5motrIDzMTbB7si6VwhNHpjFqCNLrRXVjRLb8r_oMiU0fcUy2DUGyfKCGOlUnTjhICUakvW2F70_HJtKzxhwlOG_SPs9qKCZc6-QH-z6QoA7kdUMDLXv8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5f11b6cff5.mp4?token=mtxJckcfTYWJjDnc4iUUYIC2VP88_FKKL9QGM-pCHRPXFYa3fTUeEek-O6P9N6zfQySwuqTdpY2vOVBaY9WJ7GewXtEE0oLm8gZvgm4d6X_S8Xz8YJqc7s67Nh7KhchuW_3uwe1LNZ0JbuMXfyfQAVrcblKg2dRWmhAbic1JbseDpyu_AdggBg7n7kYcwQgIHsSYwMDv3ifAi8w43YHmTSopqff_UTyfXtT1ugUKUUdnweo6dY7sojPtu5iVQrkzZ6SIyjQO0ODHCrYSarJsjiRqDs0iTtyAi-u8Nh9s0zGaHuuYsGdJmSwUqzz9TwsgwkAAPucqImylF8GHRzZF7X1DmBk-Bt4ThoQZG29Y-j9pPqUflswNX6ieR3fQ8PnsCuLbowDwQ9ficfzEkxA_y0K9W5JpWX-jt7cj8pzfsmnj6plb8GXPMKwV9_oHGldXNTCQyo115FqGb5Bv1aTSHUQ1Ugrq3n87giRpKy2XQB_RWWzCJtD73AbXg96hoyfWSrS8XB7MT_u-oDPDdZEITVkCqQuWC6gIWcby5OOOFPNAYMWiE7VxOp5motrIDzMTbB7si6VwhNHpjFqCNLrRXVjRLb8r_oMiU0fcUy2DUGyfKCGOlUnTjhICUakvW2F70_HJtKzxhwlOG_SPs9qKCZc6-QH-z6QoA7kdUMDLXv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇦
گل‌ششم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/94342" target="_blank">📅 03:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94341">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جاناتان دیوید هتریک کردددددد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94341" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94340">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گلگلگلگگلگلگل ششممممممم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/94340" target="_blank">📅 03:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94339">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLs8DR1rD-Wl_L-jxTjzEWBVQTjyqT5JPsI65LMv2_eMnAwStkIXL1mFB0i4_QfNEHFl_Gfi_cydub7AgtLnZm7KTh1vYEE_vnxycxmOsJmGXm9xOGY0jYnlhxbZlxPxc5VH3bhzRTCgTxJYIgfr2KXIk-y6N5HPlOC8Ly77_oRHHYHdwWQhLfDaGQhyeHWAyPY9Qw1lDxQJeaJi0HO2oUTCuKOCnSHPbF02BCCU01ia-V7RRCFHYAe5KbxKhOl4WHTFicUGPX0kmngNGHJx1KyYg9XCR1xkBxa7RWe6LpXK9YT6jIYYIQuD2maMMyNq7ng17RJVzH7HjYre0oI2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇳🇱
#فووووووری
؛ با اعلام تیم‌ملی هلند، کوینتن تیمبر بازیکن این تیم بدلیل ضربه مغزی خفیف در تمرینات روز پنجشنبه، از حضور در بازی سوئد منع شد
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94339" target="_blank">📅 03:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94337">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhQjTYPaBZ9IvDsDh5wwf9hDJknrhoXqU4cTsC5HtDpn32RVkhG1Klj6-R5QbND12VqgiBhY6pGsczkVb8PfQVrYQslLQx6V-fK7m2WuzEDp9Xn3hwb2PdTK1cr-ClxkjjT4N95ne4GnTiSAEvetXhriSP5j_oA4z6g8ndnp8ajxLUfL2Pr1GDUSAJrS_kc5TwxMhhpG8Rt8mjpIuksafZv_lcbnWI4z6jojfvcGnINWWal6XmvmBg9sYo4I5--sJ5salIv7OyShfElPYxH9T0vwyoauxqva8ZIAlu1ei9xOZ6AeNKCSLhbZ39ToFnyOWVW9nodkLgLUADtSfa1o9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxggmGsASc7F7q4RuAxp5J2XaLM6tXrvNrg_Ja9YMD6dM6Mvmtbn79LDYBlEixS70Z2iXYZeQdI7MCtDSBpbyPV2MPbNhwVQ78idnCJtOP1fruOnbuNQiJ93Tzn6UOMrWxqFEzyB67oe8ImzbB2PdDPh5Qw0MHJLWgiz-5Vjp_5-wxj7e_ed7qFQ706meA20e7gN7JepofOGJE_1u2C0AQyDfA4HJtiDriXmM5XBljg7wl3H7NldJ8Mora1K7X5xAzqsd-G4lQnz5UZ2l-EQ7r1acyBoTrGro8CHNZyuqKEQ8RG3A6EyaRql4G5ZSObvSsrJdGwsuD8n8WypmG1w5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
ترکیب کره جنوبی و مکزیک؛ ساعت ۰۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/94337" target="_blank">📅 03:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94336">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3ddbc8ce8.mp4?token=mYae2dtgsg-MX9SDEKt8efdVXcT6Cqg2t7lHkjHuPNGOP2fTScE-ymTaSvgFr8i86FIXnN74aaGbTIHDMZYcO1TiPlFw7PVJrfSbjkaKcRdKk_zEizdnlg8xegr4jvik31YF-l7jzP29W4KdomnTphqRhj_ttxOvlC1M2Q7SsR0nCrogeKPLfklMe-tsSbcnaWFyHM7FNCgtfO1CMbn83Jdsr4bTA2E15EyN07HMQ9XHzVV0XY3ll9FUk7fVSH564I3di_t28VrztCdtF2McrrQxWhCKtgHquvaC0xLSxOaBDXhbuENgEXYNQXm-C84XoS9yHGkwI61y9EOJiklDJ6-Ag6mG2RqZVxps7LmXYs6qVXvm0vDNpvjtgIZ9yid_gi9fiT3wiT7TYTJ7EIN628jq_Hd9n3xWAis9XAWPatquxbcg1UXfCYZIeCryvenmCcip41ry5bbhg4BaS9ZXVFtg1OtAf735Rs3buPbm9CGK03kZNj042sRxqOQFP57PGmA6IWgD8p17QxeGCN29t4ncF4tNKHhI0GcWUl1z5GZrsiFb25yNOKUOlhACYj5ynwtrw9sGSPDohPzQAgNbJ13bitcngjMkQHFaSO1kqFt2AA75Lq8MgtWWVK1y_9eiQDGIO3rn2DbrripPd9GIbmj7WNbcJuGzkoO6yQB5r64" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3ddbc8ce8.mp4?token=mYae2dtgsg-MX9SDEKt8efdVXcT6Cqg2t7lHkjHuPNGOP2fTScE-ymTaSvgFr8i86FIXnN74aaGbTIHDMZYcO1TiPlFw7PVJrfSbjkaKcRdKk_zEizdnlg8xegr4jvik31YF-l7jzP29W4KdomnTphqRhj_ttxOvlC1M2Q7SsR0nCrogeKPLfklMe-tsSbcnaWFyHM7FNCgtfO1CMbn83Jdsr4bTA2E15EyN07HMQ9XHzVV0XY3ll9FUk7fVSH564I3di_t28VrztCdtF2McrrQxWhCKtgHquvaC0xLSxOaBDXhbuENgEXYNQXm-C84XoS9yHGkwI61y9EOJiklDJ6-Ag6mG2RqZVxps7LmXYs6qVXvm0vDNpvjtgIZ9yid_gi9fiT3wiT7TYTJ7EIN628jq_Hd9n3xWAis9XAWPatquxbcg1UXfCYZIeCryvenmCcip41ry5bbhg4BaS9ZXVFtg1OtAf735Rs3buPbm9CGK03kZNj042sRxqOQFP57PGmA6IWgD8p17QxeGCN29t4ncF4tNKHhI0GcWUl1z5GZrsiFb25yNOKUOlhACYj5ynwtrw9sGSPDohPzQAgNbJ13bitcngjMkQHFaSO1kqFt2AA75Lq8MgtWWVK1y_9eiQDGIO3rn2DbrripPd9GIbmj7WNbcJuGzkoO6yQB5r64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇦
گل‌پنجم کانادا به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94336" target="_blank">📅 03:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94335">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پنجمییییییییی</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/94335" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94334">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کانادااااااا</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/94334" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94333">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">Goallllllllllllll</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/94333" target="_blank">📅 03:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94332">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04b4f64290.mp4?token=CQ8e1DwrDAyGC0MoQ_UfeWGAbfju-h-N-BxlQ3gdFku6V18MyryWDUmneY4cvnJbWqeDMwC8iXmwnmlI_ugEU0JpgldWC_m7EMZFjcbHH0EubwQ5H-fj_0faBEaYFj-BbYgo7YVXijx_Xzk-tDrQQQf02MQB2eO8ax5Yb_c3UHSmgJH1ZRT1OWgG78F-vBg4XyxQz-CKXRyeELuM0FzR1qcyAVLir7wsudaWYdFljwWrHt5llTDPPVoX20NBK_7sxULoZOCebgjz0UBR2OAcsI9yoCsXCpPgrvOrNQAvCER4HcGWz1rbfjIrp8NfNHccnyEQJySWCDAzHLW6H5uN7S-QgzrIl6BrffzKNWgKsvw8DQvBT58rtnVGpRh8IoALJq75xyy51AkV5pWuPwrwMkPkRi4rmp5SSHctkPc3RgKDD6iHUt5cvPURDI_qZEO6Ntg5v2CY2l8GRsnEF80o8pkVjGWO6t9MA7-cS2dfl30YrbwLESnqZmu6ioWnVqKBHm55PHbKSQ6NQztfMjPm9qZqbCTPTCATKLqfA96vmkZnmZixVhuhQe5fxWj3LtrSPmI8k11-vmcvfRGpEDkKJvoycllPN11TTcDZSO5gsfKW00piovv30LhuMnZ91G2xb9OMm3gj36VRw0WC6d7i_jXgE_nC-K1eUZBT7punr7s" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04b4f64290.mp4?token=CQ8e1DwrDAyGC0MoQ_UfeWGAbfju-h-N-BxlQ3gdFku6V18MyryWDUmneY4cvnJbWqeDMwC8iXmwnmlI_ugEU0JpgldWC_m7EMZFjcbHH0EubwQ5H-fj_0faBEaYFj-BbYgo7YVXijx_Xzk-tDrQQQf02MQB2eO8ax5Yb_c3UHSmgJH1ZRT1OWgG78F-vBg4XyxQz-CKXRyeELuM0FzR1qcyAVLir7wsudaWYdFljwWrHt5llTDPPVoX20NBK_7sxULoZOCebgjz0UBR2OAcsI9yoCsXCpPgrvOrNQAvCER4HcGWz1rbfjIrp8NfNHccnyEQJySWCDAzHLW6H5uN7S-QgzrIl6BrffzKNWgKsvw8DQvBT58rtnVGpRh8IoALJq75xyy51AkV5pWuPwrwMkPkRi4rmp5SSHctkPc3RgKDD6iHUt5cvPURDI_qZEO6Ntg5v2CY2l8GRsnEF80o8pkVjGWO6t9MA7-cS2dfl30YrbwLESnqZmu6ioWnVqKBHm55PHbKSQ6NQztfMjPm9qZqbCTPTCATKLqfA96vmkZnmZixVhuhQe5fxWj3LtrSPmI8k11-vmcvfRGpEDkKJvoycllPN11TTcDZSO5gsfKW00piovv30LhuMnZ91G2xb9OMm3gj36VRw0WC6d7i_jXgE_nC-K1eUZBT7punr7s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌چهارم کانادا به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94332" target="_blank">📅 02:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94331">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گاگلگل چهارم کاناداااا</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94331" target="_blank">📅 02:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94330">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94330" target="_blank">📅 02:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94329">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bee3c1e76.mp4?token=eyi9bhw6TL-6aer-XTz7VI4ZleuP7rSeX5wCGeC54727GSSdJKRMZCWppNJOqKxJMiUYlhTQaVa-TMLFWChw1JMz1yfEOl92Hla1Ck9HDbLhmft0R0WwOI0su3610xZvEBSIxNroDMtTbdjP5jmkGqVlgabge-I_uVbp8wGyGvkeMjv6ZFmxe727l_5I2WEquIx9kHeDO6DK1RYBLSEDF0BaKkNRKyva6TCllMxhXmEWT2Jgl15EiKiUmgoK9m81gbPpb-TwcntKv4q5uEbxTpBYcPF7tD6KWoWmJH2rXQDdr7hGxAybX-c8rGmGw-WXS6kigAzSiQ_5ihAQZ7J8lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bee3c1e76.mp4?token=eyi9bhw6TL-6aer-XTz7VI4ZleuP7rSeX5wCGeC54727GSSdJKRMZCWppNJOqKxJMiUYlhTQaVa-TMLFWChw1JMz1yfEOl92Hla1Ck9HDbLhmft0R0WwOI0su3610xZvEBSIxNroDMtTbdjP5jmkGqVlgabge-I_uVbp8wGyGvkeMjv6ZFmxe727l_5I2WEquIx9kHeDO6DK1RYBLSEDF0BaKkNRKyva6TCllMxhXmEWT2Jgl15EiKiUmgoK9m81gbPpb-TwcntKv4q5uEbxTpBYcPF7tD6KWoWmJH2rXQDdr7hGxAybX-c8rGmGw-WXS6kigAzSiQ_5ihAQZ7J8lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پشماممممم صدای شکستن پاشوووووو
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/94329" target="_blank">📅 02:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94328">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUmquspf_PFxPEgCI-jH1G3jMFovnfCo5cpHfHKc7EMPMIYeOLTDwu1Pbq71Y8r3qsJfLjUyq260Z7jOdzhJgSLCwZnSyMRudIasXg67CC6x5VJnYHOk2p9Wkf-P_DfarJH75vePy1kro9sesVjmFsQsHMH-5sltv2ndfoS6emzca5jO8HKHsx2sV6vrwzanq9wAnkb--WlA7Ymuhvrvo1skFWqKEc7yBJq48YoPsli1NJZj_nGJodx1gzOkqwGSZ9IzUpkMBjEOUidJOdEfaoH_wOBJaDE5KhtSXGjV5LD5P5mD0qTod-GpEHqOvoDPOBj1HEf5D_gYPlZwdAzTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسکش قطری بازیکنو بگا داده زبونشم درازه
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94328" target="_blank">📅 02:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94327">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzuMVgxUwdx5ung1-sQlpZ2cgt3KnWlLNlGiO4n0wFbyX-7CpBZSNqLzaucwclwNMJCxUMuEXIG5k_RFAWQrilieU7cCidHDyzFGRUUW1LX1cULg6PMcosTguVccZ0qDEoVAgdzF8k8A_I0-k_y1Cm81foKblyUchlvvqRjdUReebtZQWMW9xsEloE2fT4cpb6Aigp5QgcLMxfZNti6TKQnNRXzunq1lzF0oY3u2DFBgZOKlXSI7BiBSHvtj98It3hwcWT67711xqKFkTXGGiDtjvR_6YkQm1rSSuW85UMCC9Xd9ZOzSG_QpcU1PkqwUzO4PicHJvsSVDhv3l8XoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
ریدمممم حاجییییی شانسشوووووو
😐
😐</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/94327" target="_blank">📅 02:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94326">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtmoaC8m8FqMkC9ltpJGK0ASLAn-tCLZICU9Hd2cmHIpPye4ntQGv8IO1ehK0arGWkj72SroD97F9p0mjhGIBPCZCIsjTqpegoluGRiKNL-9HQwcwFlVHuJEKYs93yF-U-4tHS5nqnEpqZle9caqBYxIIn024itCHS3HgnvuMl08-qaK6AKU32bJJgPlh0X9Gcsti3-CeBdQP6wWE9qWazkr995CAg1SxnfgTPgdTEj4omM0Y5ph4_gD9cUq2OzL2Ese20BQ05SGPjgA2WOYlqg6ywXmxZbaNt3Mf_mPjSigdDkUYWH-dd_WC4hq5m7NWZi-SNMwlcJNKrtsn0b-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
شکستگی پای بازیکن کانادااااا
دلشووووو نداری نبیننننننننن
❌
❌
❌
❌
❌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94326" target="_blank">📅 02:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94325">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بازیکنو با آمبولانس بردنننننن
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94325" target="_blank">📅 02:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94324">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBdDV8rvzb6QxAWrR2csf0_IMARgkcytNmKJgs_5HiJReg77wbpGEwigfG5FsLKr23PfqkNE21tUQIsn4ck5DbsUYxvDpkQuiAJif0VKnOspS0NTNDXwF2_QTgplPA3P9QzciKTB5Gp7ucCFfr_-l6H8hPIA3vZ1WJbDpCcI-OsRucWCsMPReNZzQTe2jTdrBHCYbNGqNSB-tirLXcLvbidGWyLxCgycW0t6P5pZmw7usXPR9IIHpYbOUB_6oKI9wCKReEOcsTqsdC9yGTnBpDBLdguhBfXSjvCvJS4qgDGYCoBbL79Eur-ll4rm0g7oyEkuR1p5e4DeDUCm4_Uvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دور بازیکن کانادا حلقه زدنننننن
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94324" target="_blank">📅 02:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94323">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🟥
بازیکن قطررررر اخراج شددددددد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94323" target="_blank">📅 02:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94322">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
😐
بازیکن کانادا بگاااا رفتتتتتت</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94322" target="_blank">📅 02:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94321">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94321" target="_blank">📅 02:44 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94320">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">لحظاتی‌پیش نیمه دوم آغاز شد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94320" target="_blank">📅 02:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94319">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پایان نیمه‌اول بازی قطر و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94319" target="_blank">📅 02:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94318">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4cb48e4de.mp4?token=Zn85Ncc0Epoti1F7mxEesUUhd8MnLlJ_bZCvPQ7sMyNXhijNGL7RRB680QlkVIR6wIRaYrinCfSrMgAHqmoojKcDsShZAnDuY_Z1VrZzkbFkL0Lcuw1FLekxsxjpZRszM07c7dcQjBbFepOnZs9nY-3VRUWgymDdZym-FnP3Iyn0Dar9dEWUOUCVCT1-Jw-8Mzu9aRqbzWnCBh-w-1wpHrVKk7w-gZUijIfrdzLMvIIZFTSHV3fnz0xSZ3aUCT_tZcsLlzp7Kl0nJxatjKSLn1qTW2YTD-4-np5jhrYah8wjx7Bn8w85ZkPnHBH9vk4cR9PcGlLroUU_J4kiaQaYvKiI3eWxKD4Oyw22DSDnOwRMvzkxldvtAFVKhtnjlEOnScqqZclfK5oXyHq-UdYogVEwcp5XS8q4PWFzUEy7OenoaWG_7ol5rADVnGZQk2s2okj-WtWKEj9wqO95XokowefNzYVw8y2CLseDVEBcp70QBN1kq-RdjuZllffn-WRsG9eXx-q-0BEpIf5jiN1cCuZTt7jc6NVJR7lz51XvzRosEHGTGI94xj8M7KFAaCOCOb2hfYE1jW_JibFNhHJEP3IM0zK9ViylorUOB-HSB360yFmF8aImvAXXRScHzo5jGe6o7XpZmFeRpB3mwqzTBuaTjPeLAEzRB6npxQNNzdM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4cb48e4de.mp4?token=Zn85Ncc0Epoti1F7mxEesUUhd8MnLlJ_bZCvPQ7sMyNXhijNGL7RRB680QlkVIR6wIRaYrinCfSrMgAHqmoojKcDsShZAnDuY_Z1VrZzkbFkL0Lcuw1FLekxsxjpZRszM07c7dcQjBbFepOnZs9nY-3VRUWgymDdZym-FnP3Iyn0Dar9dEWUOUCVCT1-Jw-8Mzu9aRqbzWnCBh-w-1wpHrVKk7w-gZUijIfrdzLMvIIZFTSHV3fnz0xSZ3aUCT_tZcsLlzp7Kl0nJxatjKSLn1qTW2YTD-4-np5jhrYah8wjx7Bn8w85ZkPnHBH9vk4cR9PcGlLroUU_J4kiaQaYvKiI3eWxKD4Oyw22DSDnOwRMvzkxldvtAFVKhtnjlEOnScqqZclfK5oXyHq-UdYogVEwcp5XS8q4PWFzUEy7OenoaWG_7ol5rADVnGZQk2s2okj-WtWKEj9wqO95XokowefNzYVw8y2CLseDVEBcp70QBN1kq-RdjuZllffn-WRsG9eXx-q-0BEpIf5jiN1cCuZTt7jc6NVJR7lz51XvzRosEHGTGI94xj8M7KFAaCOCOb2hfYE1jW_JibFNhHJEP3IM0zK9ViylorUOB-HSB360yFmF8aImvAXXRScHzo5jGe6o7XpZmFeRpB3mwqzTBuaTjPeLAEzRB6npxQNNzdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل سوم کانادا به قطر توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94318" target="_blank">📅 02:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94317">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">درحال تجاوزووووو به قطرررر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94317" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94316">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94316" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94315">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گل سوممممممم</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94315" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94314">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگلگگلگلگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94314" target="_blank">📅 02:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94313">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قطر ده نفره باید نیمه دوم کون بده گل نخوره</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94313" target="_blank">📅 02:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94312">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پنالتیییی برای کانادا</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/94312" target="_blank">📅 02:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94311">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/87926f8e15.mp4?token=XgxY9ZSHRrHyFcC87kR4xMCqQHz7xw0g2qYNYgTj9vycMvln_LQNy96j6CHdg-3mqg_MY9ZyO7kN6WFAwZ2HSqIoYkGIWiRLDe4xUQbLlUGJw5TBQiGX1T_-Ln3tWfrewKoAhUQL6wkYFJqyiaHjW6Rh92fUfyXedXAz-JUIoT15fWlYtirnn0G6MbnAyfUUbU63oYwJKbzHqIDvtg8g8JpUqBi0hXUlc1Qyu8xFKEzWLPsB1QUmQuSqLxdq6lYk6B-vsg3U3vcf16cokkNGY0hK8ui17hBwMMsTUUZn5_ZBJh_teDk2p-vJN5Es3EuG2DGkuXATaduC5oHh9nrXh0IDOlv6Sy2PTPW2kvhZ-ucHEd_KWbT72VgTGWpYqH7MIss0Vexvsx8B_gGtHDsKU0ACfZ8M9Ho4jjDXfo0SheS5ouedHYle-2XXpfvdfYzKwKsoolEz5VylIH-wrKf9hLc_nQ4GpA9HPjWDzyFfQQ615wqfFVtdXgEbjUOOkWF0q-IRwKgYUbindBP18Z27IbXB82kdnpf1c7gSKAG215MJMXfV63GgsHdWTnJ2tbLFrWK7vc6_XlGeigvgqws_ui0Hta13e7HnZd-cBQZDXGkbfhFqtgZBItMi98yGbI6wByhlFcpiWM1uMVOJdXvSEHONWjRHSGMGuGuwKqUKSAc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/87926f8e15.mp4?token=XgxY9ZSHRrHyFcC87kR4xMCqQHz7xw0g2qYNYgTj9vycMvln_LQNy96j6CHdg-3mqg_MY9ZyO7kN6WFAwZ2HSqIoYkGIWiRLDe4xUQbLlUGJw5TBQiGX1T_-Ln3tWfrewKoAhUQL6wkYFJqyiaHjW6Rh92fUfyXedXAz-JUIoT15fWlYtirnn0G6MbnAyfUUbU63oYwJKbzHqIDvtg8g8JpUqBi0hXUlc1Qyu8xFKEzWLPsB1QUmQuSqLxdq6lYk6B-vsg3U3vcf16cokkNGY0hK8ui17hBwMMsTUUZn5_ZBJh_teDk2p-vJN5Es3EuG2DGkuXATaduC5oHh9nrXh0IDOlv6Sy2PTPW2kvhZ-ucHEd_KWbT72VgTGWpYqH7MIss0Vexvsx8B_gGtHDsKU0ACfZ8M9Ho4jjDXfo0SheS5ouedHYle-2XXpfvdfYzKwKsoolEz5VylIH-wrKf9hLc_nQ4GpA9HPjWDzyFfQQ615wqfFVtdXgEbjUOOkWF0q-IRwKgYUbindBP18Z27IbXB82kdnpf1c7gSKAG215MJMXfV63GgsHdWTnJ2tbLFrWK7vc6_XlGeigvgqws_ui0Hta13e7HnZd-cBQZDXGkbfhFqtgZBItMi98yGbI6wByhlFcpiWM1uMVOJdXvSEHONWjRHSGMGuGuwKqUKSAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌تماشایی جاناتان دیوید به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94311" target="_blank">📅 02:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94310">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پنالتیییی برای کانادا</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/94310" target="_blank">📅 02:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94309">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94309" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94308">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوووووممممم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94308" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94307">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94307" target="_blank">📅 02:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94306">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=L0jtL0tXazvoCxKeXzYosfc6_kYOUm7D4q2AaWXrc4BMzXXj3I37-whr80w5sEAqJ0wJiBUJBpoxXpR3W5ENXe1Tahhz8cwmHlxZlXc7wVZ6-0bHvN1IuHpSwOqxPCBJvbVoG651ilQUUgKprm7PuPcoiiJWRG0aJxilZePRi6VfBs8ATaLfhmjUJoeakMEtlYqPw51eVZVgHHpwUmoOwY230P1253Ghhj0L1YigLsNVMNYogEGeb4m-_7Z_9oVrlLWmUHq64MO4u5y2G0f_uzLE3_rRq32H70BF_bjviDgJ4O3dFHku_m6rviubLqFyx3caxL9ic3I82R5taPPFqwtTU77Oq3K99trZMpEAboTYuEGItdKko6w4ODDFeMYB8ljLTJadbmR8i5T06rgTT8GCjtqOveVrHRFjTLNdFQTsCLFbI2WUTapvcQnHZtLQ7n4iL6KDB5SgoSkIi63s_BvH78k_e1V8qtRgTnkko6jqm4A1K5iDg6k4M_CsT3bYfylQpBkXobh1xOEztASb3j6-MHINHDhjFnclTGV7IhiSdXQoN5T3bS3mtXiROtimewsa9Rv0PcysVhcRk7a013oq3TEz_U89VzBY6d0HztLzZAGD4a1sIoe-jjG-0hgPNSwOmM6eaS6WsUr7q-qKWYq7q9aejiZUASSPe0sPuzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a94bfbfc0f.mp4?token=L0jtL0tXazvoCxKeXzYosfc6_kYOUm7D4q2AaWXrc4BMzXXj3I37-whr80w5sEAqJ0wJiBUJBpoxXpR3W5ENXe1Tahhz8cwmHlxZlXc7wVZ6-0bHvN1IuHpSwOqxPCBJvbVoG651ilQUUgKprm7PuPcoiiJWRG0aJxilZePRi6VfBs8ATaLfhmjUJoeakMEtlYqPw51eVZVgHHpwUmoOwY230P1253Ghhj0L1YigLsNVMNYogEGeb4m-_7Z_9oVrlLWmUHq64MO4u5y2G0f_uzLE3_rRq32H70BF_bjviDgJ4O3dFHku_m6rviubLqFyx3caxL9ic3I82R5taPPFqwtTU77Oq3K99trZMpEAboTYuEGItdKko6w4ODDFeMYB8ljLTJadbmR8i5T06rgTT8GCjtqOveVrHRFjTLNdFQTsCLFbI2WUTapvcQnHZtLQ7n4iL6KDB5SgoSkIi63s_BvH78k_e1V8qtRgTnkko6jqm4A1K5iDg6k4M_CsT3bYfylQpBkXobh1xOEztASb3j6-MHINHDhjFnclTGV7IhiSdXQoN5T3bS3mtXiROtimewsa9Rv0PcysVhcRk7a013oq3TEz_U89VzBY6d0HztLzZAGD4a1sIoe-jjG-0hgPNSwOmM6eaS6WsUr7q-qKWYq7q9aejiZUASSPe0sPuzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل‌اول کانادا به قطر توسط لارین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94306" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94305">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">کاناداااااا</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94305" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94304">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گگگگلگگلگلگل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94304" target="_blank">📅 01:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94303">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کم کم بریم سراغ بازییییی</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/94303" target="_blank">📅 01:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94302">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prq3VHHwgiSb4wdDECryJyNcUwIFw5zGSQXX1sGrSGHfEA5aAkQ-j8z47PTS71Vutj97Vcx_som90S_g475vWD8G1YOHjn6eci49pkJm7ecFVR85Y5x5u8gd1BkPQJ-SeYXMjcpXucf6cRZcMxwn9RkO-9S5uVTRZesf7QFj570-nqt1XVIKK7ohANE7wFrTI8SM8Ycs0XdtNXWZz_TgRkKYQXY0mFjpyN_4j8bqzEUfufcVUh5Eo_Iqjz8iYUVukisGmyMOauIXfB6ItQLxOoofRl1mDFsR5BWDcJPoyw-SkVyJnRLGk3_DqbDZj7UVHnzXL8weaYiUCVYvVuIArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
🇪🇸
گاوی: انتقادات نسبت به من همیشه هست اما بهشون توجهی ندارم. اسپانیا واقعی رو از بازی بعدی خواهید دید. هدف ما فقط قهرمانیه و برای رسیدن بهش حاضرم جانفدا بشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94302" target="_blank">📅 01:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94299">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCUi2BIT8KaOWH7XECOd79c7An22B1aXvKfabS7zzU0FFyVqsthqxmq4lFpt1JVvO17JUrbo814JyMXMnRupE3SEoFjgB5eaVgafuGCpJyXNgugdwGgqsMLIr03UXGB-5rZf-4ypKOi1gXYu2MWHM9u7swkkA8HsFL_S3gjnORyUiebPL-6j5FuEi8xwXqKRDXZ8Hw91y6TwNyNqygB4-X9VyMNJ3E1Ti_muJwvJrC0mswnNGd6f6fGS4RuNlTuP8pbtj2GSzfqA6mSfIUiARCdIVzwoi2L_zeE1dUoFWn0ROPq-QAQNF7CmNS9PRV40j_50HF_gZNgzC28uIDaPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
🎙
دنی‌اولمو درباره انتقال کوکوریا به رئال: فکر میکردم به بارسلونا بیاد چون قلبا طرفدار تیم بود اما حالا که خیانت کرده باید کونشو سفت بچسپه چون فکر میکنم لامین یامال راحتش نمیذاره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94299" target="_blank">📅 00:59 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94298">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq290afVd9cVgr34Z56kOUR9ujS9QpORZDJNb1ZUgcmOmMN1oRgwjRBDawgvkwlGmxCSx7Ju64p8cjvOObEftdDSUN_3LTvXyEdYfn4DE026MgeDcdTFST3u9svo7jQRzdjhXn3VZv4PPvNF-0_BLwb95WXR8e8cZuYVNFQGe5VE9ldZNqTH-VBGURgDUdaYlMNUcZhjYa1Vx-Yjl2PQeq-x3KYdCugLUVGkgRbXwnfyge-1bs8prI2sayZLvg21pVSKNP7SWjNVnNNA2BEI9iJqUdZnA9tW2ZAvPnkNel3UPgCXMAmX_cVrHemirXTdzhLA1cq73dL0FPfhXLtyCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آرشیو VAR:
پنالتی سوئیس به اشتباه اعلام شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/94298" target="_blank">📅 00:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94297">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O41IpBm3bD7gsLjuEkwhzR6qLsY-YBTEQA4dX_y7jhmLWV-GdRR4C66dlua4eZyr3kixLzyQafDgeRB_OaKvSGffZVOs92Q78SXs114_qXPtsxikoeIhQGhTR76rMqAHk4bo17aNYRtCFe56eVaDOn8jf_PubLrcYgYWXRkaAATltJRSFg7gPsEGHPe49ObEwDEgIgWXoaSooqWhTzVYvjQEl3lNIP73jTOCMbrUv-KJLJ7Q8wfw5-ETV6L6A01AqfOFBPX7lq4QgrJq20q0FyJlEu5vGT6M2mapT7KE20lLT1MQu9dZ4S_FyNZaWy2_haSHXwR9TY3WRnhGKpo1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🏆
#فکت
؛ یوهان مانزامبی (۲۰ سال و ۲۴۷ روز) جوان‌ترین بازیکن تاریخ جام جهانی است که به عنوان بازیکن تعویضی وارد زمین شده و در یک بازی دو گل زده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/94297" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94296">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94296" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94295">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BlFoWqAdseE4yHapPRADZ1Uf_OTCoX_1UDLAGe0o4QiT8vehnevOt-_8Um5JG65VRtKLV6B2c_048eGhIIk0bFfmsI2AjRKYkElIU6-J8QCv3dNTE58y09zmkyP9Qc016YoydoqbFfBXHbq0Sn-YzCMloLkGxSXU4xmNsb_FsY52jK5hPODy9FYxgBmU2PtxsVBpQp7-oGarGJ8hgCnwAzskRmNX5DHbTUDhUunomkD6hmRLQLMJgdnBMrdzbf-l83yb_W_dKSqQQ-q8VoyNFj0QHAufTifFik9QbkFRbEqXyq4M-kWLQkcYEvnIybIOm_OPMBc7hZMvPpm_FN2q-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94295" target="_blank">📅 00:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94294">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ4FvjB7lusabPzCk24bOGEaWB8dIKBJKntj6PXEUztdgoByv3kn8DTnv_-bS1fIKXDg6evMUS5r_4Ze53YyLCCtSj5DSkN67BuoojZ4H7BVdjP-fModHZHxwpHvc6S2ORuWm_eccbm2wNKNwIA1BRWwTLY9iFz7IFtC7I63GtJqxSMLQvTdepRHw3OzbK5Iyh0dpByfs-NGKQZezSlxR7xSNGmpzydYHzM5gSOSMrxeqRoGvm_ZdRAOyjO0lccEdfWxL6S5kYEVkvMQ6OaweaFFH6U1IyIut7AOg67G0YxYYAQNZO-h2kMPDo-W7R-c54pi2hnCMuTO3dzFLTD5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تا اینجا جام جهانی 4 کارت قرمز داشتیم، به اندازه کل جام جهانی قبلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94294" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94293">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyl5ihN0EAhXsPyIjyoHFLAlFHvnK9MoUBU_2Uw05xkSHZfb2mCuJ4LSOEycepoub46JMFA32SdOpsYUw2DIeKVI9UmS8kBm_Ae4aaLBBoI5DiUFE_GfO5ubmm_QxU309R0N64q6JrlL7yi5rDiF6EiyXo8J9fZ1AAO4sibRxhqf6AE5McZoifDdgs8HYeMsxp2E_7DP-q8jhZyijvIG3Dv9LR9hRBaLhqGyI50TTdHgdsjpf8fvDIqlEbTSz6X_rABIj4f9N-l5ADdJluPkobuj2GVAsexVB9mOTubc8x7UDZYRVajmNvNMDO0JMtaSOTNMugB2aqZtxgHwZgtYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگه تا دقیقه 74 بازیو نمیدیدین چیزیو از دست نمیدادین ولی از 74 به بعد:
◀️
دقیقه 74 |
🇨🇭
گل اول سوئیس
◀️
دقیقه 80 |
🇧🇦
کارت قرمز برای بوسنی
◀️
دقیقه 84 |
🇨🇭
گل دوم سوئیس
◀️
دقیقه 90 |
🇨🇭
گل سوم سوئیس
◀️
دقیقه 93 |
🇧🇦
گل اول بوسنی
◀️
دقیقه 97 |
🇨🇭
گل چهارم سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94293" target="_blank">📅 00:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94292">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8sGGO7xq207MQoim977vkrtkkIelnLWBLC61StsKy6E1q6ubk4nwrgEEGIjDDfsytlFegva5GcdcjtZsNrY-JX6Ms3Em0uzIimFutR6-N7iKyB0KBc3mFhdTcWtfwdfNvIHWCBYuOm3IFC4zt5b5NbnViw3siDsYGZooCNij09Mb045ozRwk3MwHgbjW-tjYv1N5q9G9Bin6OcD2LqeXLMRNOgCq2fyLN8sG3ttMODYMGTL7z6_RfNUXb3veNnpg4gQ8toM00b0kmvarap0CwprdKJx7Sddj4HrxmoZrcg7vwOMimigyT4G5kIn24EGgMT_dR-AOB4liJ-WaJgnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یوهان مانزامبی به عنوان بهترین بازیکن دیدار سوئیس و بوسنی انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94292" target="_blank">📅 00:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94291">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlSfONj_LBsmYn6DPWEV6bLH_7LjeeMUqgcp5zdqZOQo1TFcmOAiCvqCZDLTA8OtED7ZLg-ZviV0WsZZvKGoFYGY-V5CxAOGbIvbH3FPYOcPwzC29YHh_oOUAMEENRTvaJSJJslyXxadHrrlNPBXjCiPBXUcGAex1v7pcEsIUh46KxgV4nnNGBBC-pSLBfIH_WgB4hLGe-sbk4-sWMmdPPT122l-iz66mn_8spJLDobknHWz8TvDjqoDiQKZP0m2KQ-9ZiX95b616fhiTd2J7GdsBkUehWLLLPTnB46fP_vlQa0QnVNThseR8nmyNbALfF9rYF6cB6LK43JXJloTPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇭
📊
سوئیس با کسب ۴ امتیاز، طبق آمار شانس ۹۹.۸۱ درصدی برای صعود به مرحله بعد داره و عملاً اولین تیمی محسوب میشه که یک قدم تا صعود فاصله داره. جالبه بدونید در این دوره از جام جهانی، ۳ امتیاز حدود ۶۶.۷٪ شانس صعود به تیم‌ها میده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94291" target="_blank">📅 00:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94290">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E64l8I7htdMJ1oA27hbIe9wN4XegMxRD6FkCorRqddYUtQMReSaun8Mp4OYZDcA2M2Fr3PF_1J833TMx7JqDHVXDNUJGChV6ZvTD5u0CUKZB00wwyztwYsjtE01IXx3Iw0MRPSuOpDgkMhVRP1UGMK5I6XTt1eYABEX3Qn_OYtLfY0Io2alZMrSEY5o-8zYC4QYi0PWvyAhHDAZoWkHAbFYhUUjJ1HxB4Ls4ZP8iq764ZproJN6wGtmysdO7Q6Ut2_w_jIx6Hxm5pjtMlMuvAU_av7cNTpmDqYsjwnwN1ALQ2h62-S9qwhHpdEh0_coAOaMQbiDh_FMVSeDQ8t8Now.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آمار نهایی بازی سوئیس و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94290" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94289">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY4QP3uA_4_GSbE5HAbaXxoCxjgkOsuVogRKKGaR3giH32DVg3lgQfM6M6mkRiD2e9xeg18ksq5OqpjryCvX0Lf8kzHipg7Ll6CfuqxNdzFTI2O5WczpONuDl0YHW03o1MVmUGwTaQA7qwbzvaTNFJ-FD03XipTcZ0phb3RpEwBOCt4Jd-vpX8ghixh4wTSWHyC7mq2SKxFaNh65aDPvrP4FZzCWZ58dzUmh5SRhwVYjktVGgYS_s_qO9IjJPFroJs5evi8xy9jsAYmcY11S8tvTHjU4FciSJ6HC9csBn-fPoSKUfAgzdvf8zyaa6URyhDIH6BnWAG7hsJp46A7wIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|سه امتیاز ارزشمند در جیب سوئیسی ها در شب گلباران بوسنی.
🇨🇭
سوئیس
😀
-
😃
بوسنی
🇧🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94289" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94288">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eca495a4d2.mp4?token=jdkdGLpQWnJK3IHJpPWLzgm5-mTdHpwEBY5ASRcdP12iwFDRhYaL75UOh5sZvmmRLNgA0thd9jfGR3PDcjNR9ksASHc_LMwxk-4_9OrKW7z-mxj99VK9nn7Bfdb9BO3n4hN-HHa77gytNXFJDuzvu9ot2Pix9J3DUNWIJ-JVyquwNtIzSGGOhyhMKdp0nA3GNNRZu313rud40yaizGPmSaOMj9-y2xPqND4pCG8I_HbaF7anUxkS5FwgjhiKGbHZ7KUJhIBEfCVLmoK8HfSW5-EpsMW5HYMDhZWpSO2WigZiKIYKksTRFTQGBd3Kpj0F8DR8whGP6MnemoDt6XrWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eca495a4d2.mp4?token=jdkdGLpQWnJK3IHJpPWLzgm5-mTdHpwEBY5ASRcdP12iwFDRhYaL75UOh5sZvmmRLNgA0thd9jfGR3PDcjNR9ksASHc_LMwxk-4_9OrKW7z-mxj99VK9nn7Bfdb9BO3n4hN-HHa77gytNXFJDuzvu9ot2Pix9J3DUNWIJ-JVyquwNtIzSGGOhyhMKdp0nA3GNNRZu313rud40yaizGPmSaOMj9-y2xPqND4pCG8I_HbaF7anUxkS5FwgjhiKGbHZ7KUJhIBEfCVLmoK8HfSW5-EpsMW5HYMDhZWpSO2WigZiKIYKksTRFTQGBd3Kpj0F8DR8whGP6MnemoDt6XrWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل چهارم سوئیس توسط ژاکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94288" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94286">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سوئیس گل چهارم رو زد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94286" target="_blank">📅 00:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94285">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پنالتی برای سوئیس</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94285" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94284">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/01debfe500.mp4?token=SuPpQDrGTp2vIOwSRGKXlcEhB9oYfaSgKvKmefc994pbZDfyWDX2hBdG51ff1dl6HnLT6dQSFSpg-2mXVLSJpABGb6lSoRJnSlSA6S0p5-uA-y3GDYgsrrQwXq1ZKDwkEIQ2URN9Ba5WGl-slr_OIf2JYNIX9e72XkVN7yrOF7OywTbDZLSvn4IrIef7X3gJIwfZXfIR9r0ggj5HFJwwUP5dhENixmgKwPM34Im86LCykiEZeUJEOisYTetn6LCQLoHZ6pViNigBLHg0HCZ3L463QZAacQOLcpyIj4WvPsu054REAKuetHC4h9o83qOEg5OAdSuAEqT9o2Wcd6jrZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/01debfe500.mp4?token=SuPpQDrGTp2vIOwSRGKXlcEhB9oYfaSgKvKmefc994pbZDfyWDX2hBdG51ff1dl6HnLT6dQSFSpg-2mXVLSJpABGb6lSoRJnSlSA6S0p5-uA-y3GDYgsrrQwXq1ZKDwkEIQ2URN9Ba5WGl-slr_OIf2JYNIX9e72XkVN7yrOF7OywTbDZLSvn4IrIef7X3gJIwfZXfIR9r0ggj5HFJwwUP5dhENixmgKwPM34Im86LCykiEZeUJEOisYTetn6LCQLoHZ6pViNigBLHg0HCZ3L463QZAacQOLcpyIj4WvPsu054REAKuetHC4h9o83qOEg5OAdSuAEqT9o2Wcd6jrZYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
سوپرگل یار تعویضی بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/94284" target="_blank">📅 00:24 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94283">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلللللللللللل اول بوسنی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94283" target="_blank">📅 00:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94282">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcd1a5f6db.mp4?token=nL_ARD_MB34Uj6Yg98BNWJhE5mURkCLq5LRb2A2lp4CO6YFC6s_RB0jQ7OsBSHT7Ocu7MmNnsYP3fuOd77MXEjygSCMPQXY1nkoYY-7xeqrUYpkfNjCK27DK1ZuxwvtWICjHB2mTQjIn_keKm3B9sH7v63xoM4SJNNPMUTY5ImVkTngwiWzoJ2AItpIsrxf4gvmrRp-kOceKwg4KTzRYrJu0FkYxTbxPGSzIDA6WmKpLQTONWlzDy8-xyYzOYiA96vcJFzYm8jppWgBsEctvKXTM4JPCdKlvXtwZJxIr_qz7f2BT-nTcvYZ4joCBsDzz41bENOn0e9L37kfDq31yew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcd1a5f6db.mp4?token=nL_ARD_MB34Uj6Yg98BNWJhE5mURkCLq5LRb2A2lp4CO6YFC6s_RB0jQ7OsBSHT7Ocu7MmNnsYP3fuOd77MXEjygSCMPQXY1nkoYY-7xeqrUYpkfNjCK27DK1ZuxwvtWICjHB2mTQjIn_keKm3B9sH7v63xoM4SJNNPMUTY5ImVkTngwiWzoJ2AItpIsrxf4gvmrRp-kOceKwg4KTzRYrJu0FkYxTbxPGSzIDA6WmKpLQTONWlzDy8-xyYzOYiA96vcJFzYm8jppWgBsEctvKXTM4JPCdKlvXtwZJxIr_qz7f2BT-nTcvYZ4joCBsDzz41bENOn0e9L37kfDq31yew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل سوم سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94282" target="_blank">📅 00:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94281">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مانزامبی دبل کرد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94281" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94280">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سوئیس گل سوم هم زددد</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/94280" target="_blank">📅 00:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94279">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2dc23848e2.mp4?token=TZt9U34xXmoyQvepDNPSxzzYQ0ipvR5-9YsINQmH4g-kGoIGwWOUcEkX0xRPumJzPJcEjmrgJQsW3TMG9OexVKEqPuRMI3U0f5LZoDy9OQslLezYWopTK9dOMB9h23pOAJqbGUBd6fd8CTAQENBfVt6MhXvWar54mobw9wGSaKY6EtRSPrFvHyn_Uu4hp9nsZtz-Y7TqTF9ImSiCekUCAhi91GKNzJ_D2Ev44TeM6d_eC5kOIprvGv9aU3Uq9MTIZORFdZmqcMSQRP-QVzduPTftE6qpPhpx3Shftxyh03raWcGArtbl2gKY5leN3131LhbVsGo-qgehLkirF0lbkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2dc23848e2.mp4?token=TZt9U34xXmoyQvepDNPSxzzYQ0ipvR5-9YsINQmH4g-kGoIGwWOUcEkX0xRPumJzPJcEjmrgJQsW3TMG9OexVKEqPuRMI3U0f5LZoDy9OQslLezYWopTK9dOMB9h23pOAJqbGUBd6fd8CTAQENBfVt6MhXvWar54mobw9wGSaKY6EtRSPrFvHyn_Uu4hp9nsZtz-Y7TqTF9ImSiCekUCAhi91GKNzJ_D2Ev44TeM6d_eC5kOIprvGv9aU3Uq9MTIZORFdZmqcMSQRP-QVzduPTftE6qpPhpx3Shftxyh03raWcGArtbl2gKY5leN3131LhbVsGo-qgehLkirF0lbkoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/94279" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94278">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سوئیس دومی رو زددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94278" target="_blank">📅 00:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94277">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/94277" target="_blank">📅 00:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94276">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بوسنی ده نفره شد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94276" target="_blank">📅 00:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94274">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/usFnwpQuav2aZy-RzMmoCaJiaJNtNmDAoYHy8ydVbmarjjoLlVGBIPLcZnk83sCDUfmDKHbvbKWXRbwc35vNRnVGEXnQgEsX8IhvkviHJVH8ZJaE1fIHHOEMeEkHX6cDRhyNXb8sc2gjxQQejwDIGwBEjAMtG7t7rqViE7Pk6iaqGcw4s3d-y5NcWCgxa99JHCvQ8P8BFo7QYSMLZXiOgv0yQNN9dg4bhzqrdzE3fSzMOpZ69LON4_Yw5LKs37nngiMnDY9LLY2kaj7Q4kYWtNQTQONQXWR38DYig2Scz-83-Sd2xBbhGyFcnthpkieWL2pM7OFBk0YpFgGME3YjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNwYdSqAP-rGd8Hynw8Uz7leAQl_j5ZCldmVmACqCNiamB825iiqSZYZh9OnH1ThMR9CwsS0pwtYPD7b02cui8aRNZnVbaDG7JOX47UA5FCkmibeCF9Wv8W_WSaW_grrQN9eJ81jXXyf_QBDhAz8AS_bzQg1FO5ikOXVaV63o7f3_HJker2Cbwjk7W4RXJGUkHVP6Wpbs6DQu2gpjE30oz2oOYQcz20InVjG57ZXIpUBKCSsniQE_xz4mjLkaZznGsGcoIq2tJHRKjOSsdPbBqmn3hI-gkrr_vC23o0KfQG0qREH7BPUbutPR8v_M1nPaLrflonB1tbn3C2ZZGt5cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
🇨🇦
ترکیب رسمی قطر و کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/94274" target="_blank">📅 00:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94273">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/04d0160117.mp4?token=IsbKEtt1nA3K-iD9jhS2b4W5Vi_2VjhT4FYcTCbX-cZ3-HDn2dYbINDzOv44XPEdSX8U5V1DZrpq8sLshr63RSpAWx9Q61g_8RLf11Sajxz_fihm3KxLQPm8Vzn03qCeOM4F9laaqJbwTxpzaXGW0tfAD7aJ4spi7Do-l-AveKiNhrvPcFjEzut17T5RHDPRLy0OvKplly4giFBlNnkWfAhiFlvXnr9eip--1l79qTACaIUyA0Qutzxu_tx7-9L4ZzNuzi5u7jbKZGypo2jaVKENTJRUEX-AHX3FxlqaVJeY69rzzskmkfhcQGW1H8Zb04vkAQ21B1foxKzX2cuwfTY_uyaxrO0yCjdTcMqUBpaVbzCAhwHzG260kkvLfrLY2EUqdNqBTwsDm6GGSpBZvmboV6vMwJ42H188ud4gcpOcmRT6CMhO4_ixKmTGqwJfZlfzUQmgniHgN9RvhJrbvHrOcYbRWpUyokMD6KnZVRTeEaYsrliAiW3p6r6TTLC3XTPSIpur8l9TyCRWUyF2JKy-_XDULwKUgjejdlcEysD5QFAjcDvUZA8AGrpnRFGo0ZdcrLAyiJvRzqndqirFUCjzwq0zF-eQ6BxgqC5mMQ7AvIpHlZS3K4PnntJ1VC5Xy69rDMY5_8dADmKskxw6l1pSDe8ovuO7qw1lcLMwn6k" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/04d0160117.mp4?token=IsbKEtt1nA3K-iD9jhS2b4W5Vi_2VjhT4FYcTCbX-cZ3-HDn2dYbINDzOv44XPEdSX8U5V1DZrpq8sLshr63RSpAWx9Q61g_8RLf11Sajxz_fihm3KxLQPm8Vzn03qCeOM4F9laaqJbwTxpzaXGW0tfAD7aJ4spi7Do-l-AveKiNhrvPcFjEzut17T5RHDPRLy0OvKplly4giFBlNnkWfAhiFlvXnr9eip--1l79qTACaIUyA0Qutzxu_tx7-9L4ZzNuzi5u7jbKZGypo2jaVKENTJRUEX-AHX3FxlqaVJeY69rzzskmkfhcQGW1H8Zb04vkAQ21B1foxKzX2cuwfTY_uyaxrO0yCjdTcMqUBpaVbzCAhwHzG260kkvLfrLY2EUqdNqBTwsDm6GGSpBZvmboV6vMwJ42H188ud4gcpOcmRT6CMhO4_ixKmTGqwJfZlfzUQmgniHgN9RvhJrbvHrOcYbRWpUyokMD6KnZVRTeEaYsrliAiW3p6r6TTLC3XTPSIpur8l9TyCRWUyF2JKy-_XDULwKUgjejdlcEysD5QFAjcDvUZA8AGrpnRFGo0ZdcrLAyiJvRzqndqirFUCjzwq0zF-eQ6BxgqC5mMQ7AvIpHlZS3K4PnntJ1VC5Xy69rDMY5_8dADmKskxw6l1pSDe8ovuO7qw1lcLMwn6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل اول سوئیس به بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94273" target="_blank">📅 00:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94272">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سوئیس گل اول رو زد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94272" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94271">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلللللل</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94271" target="_blank">📅 00:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94270">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaoIUERdD8PlM57G78KFSLtVzGNrJ7WbtjMX5I9ZCc4COgYuQT3qRHoKDoNc66ziDsf1oHB6h37DGN66NztxUz94MctOh4271lYKEdUpCTBojjV54D2jyXg8XJ__kD2nBa3nZvvHIlzvaCCcA1dowfZzPNGodB6iDExJLU3mYNteWgLchZRFZB5RJaoD8hR9MhWN4YtBWDM6ENhxGz2b7hfqnPiqTuDJyQ4UQLbb-E7kb2XV2SeL5JyvHSpmZceWHPIxf58T7CMg9dcqKFM9KOe3labRF0PebbuxjrqARGqRTZyH1NSkJL0tCWnWfwdtp00Indb827Fxy12BOJVVCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این گلر کصخل کیپ‌ورد 1.3 میلیون فالوور میخواد تا به تعداد فالوورای نویر که 20 ساله داره کون خودشو تو فوتبال پاره میکنه برسه
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94270" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94269">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkI9r8UQlWPSp5lRDSo343iffYCI7Fw1zKdsOrjMDy4kEtqBqMJ4x_A6TU6OLXNy5UHzW8YDdyC7cFRuBzUx7kTfgTQ7Uxev0xh9rZA8gsC41Mv_QENpRZaKDWNSDeZRU0nZXMS8KoycoMTez2EFn-juJAStXMAocLb6q3tKJXXNivuxzo8T6N_ZLe8b-q2XHq-FO1XiaLqBWkAbOxLVCx7m77K6rclfxaDkitVTUvTY7DAdlaTFxuOJfh_QCVU0m-qMMg32LmaXf8wereSh2E75qNLgS0qRSnotEibIGoFx9QSjiBD-ucl2hwCLcPZBs1UAAggT1u5Ha3_VpLzfTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇿🇦
خوشحالی بعد گل بازیکنای آفریقا به سبک رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94269" target="_blank">📅 00:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94268">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUhiowiGF4hIzyB-rWOFdGmzThh3U6hTomTYRRa7tUxn1EmJf719GJVuC8saFEnfnhd1n6X3mXdOproS1qxB0EO556Wz0yA5f46iCUChbBIbHRt6J7cMLmU-yDz41iYNmwfogn1_6-CXkzCeFsengfgktmHfu3t0D4a5yMfIF0F6aZM_NjP0dgxvkzfKeyRa3E0OPcwjUbJcrfkURRGQKm_oLbdb01Kz7Xn9ZQoSlXNaRPQvIa9p-dYYOUtOXfI-Kn3jClPXUbcYjwB3BsRwDYh4ThkJmkLIwujk2KR59KhXD80zu2tw46nnXQTdbzQ_PYJEY2eOfIhf5kuhKsV9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بن جیکوبز:
انزو فرناندز فقط به یک باشگاه فکر می‌کنه و اونم رئال مادریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/94268" target="_blank">📅 23:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94267">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بازی سوئیس و بوسنی چنگی به دل نمیزنه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/94267" target="_blank">📅 23:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94266">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=Q2qGBth9t9W4lHuk46eZtvhLreAv_aTf4MKaKdD9Mm1Q-E0mWyceOAWl_kjI5IqJCTFlCLPYYJlmbSfBvOO69uwTZJPquYfDWxmnOA6KHEO_Ntj9XP74X9oWyNoF7AQ2TGB3RYEZIEvvVMB6_YByT2tf3VRuKTaX2QCitP9KnWmN_MJcwaK8q_O5Czm8xL5eDT891OzegaYSc717FbZnAXrT_lOPWUJ0qoth20VONtCORrpfwEjgnSu2NwSMCl9p9axPWPB5NP2yzx9Uv9nNNAxyE0hrRDG5Dk0ETHnZ_MsrOTWWT5_6NypQFVGuH0W5taxVIMGyil72uJ9Dq2Ggtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a9674b76.mp4?token=Q2qGBth9t9W4lHuk46eZtvhLreAv_aTf4MKaKdD9Mm1Q-E0mWyceOAWl_kjI5IqJCTFlCLPYYJlmbSfBvOO69uwTZJPquYfDWxmnOA6KHEO_Ntj9XP74X9oWyNoF7AQ2TGB3RYEZIEvvVMB6_YByT2tf3VRuKTaX2QCitP9KnWmN_MJcwaK8q_O5Czm8xL5eDT891OzegaYSc717FbZnAXrT_lOPWUJ0qoth20VONtCORrpfwEjgnSu2NwSMCl9p9axPWPB5NP2yzx9Uv9nNNAxyE0hrRDG5Dk0ETHnZ_MsrOTWWT5_6NypQFVGuH0W5taxVIMGyil72uJ9Dq2Ggtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیمار وقتی آنجلوتی‌ گفت بره انفرادی تمرین کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94266" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBJ61kTDWmQYjy3PJYg648pOcjEaLX0pp6l_KbUV9A4fly0c_v54CoM_5C9U3ScXcdKIH6Ye3oAup1FiVGjQq1iSPP08b6BOjFcw5wdmSvzBK_KH4IaV-cBLcDfwYd0MmJxQEd2nWtCtjNjW4ousSbmTQ-k8j3lkMuzepPADCuGy3U5oE30R9cWl6Dkmurtseta6VFW0RaNEzLlEV7Xyixb_P7_Gg9SlCftRtnJoZW4pBwnyrj0Rm2_TmDnCj-98GXJKqSEwEYHSHmEu2-aJIPgUikBCfDrH0_pK_tliWDMv9ki_nn8ceqlECFuPZX_-VWTB0dLJFXoOviFaG5u34g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فابریزیو رومانو:
فعلا خبر پیوستن انزو فرناندز به رئال فیکه و باور نکنید، خودم روزهای آینده دربارش صحبت میکنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/94265" target="_blank">📅 23:36 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
