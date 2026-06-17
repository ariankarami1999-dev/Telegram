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
<img src="https://cdn4.telesco.pe/file/hIuGvJSyWv7e0pfT0duJG5ZKbWz1UJ47rSzSkhdTTafNlcq2NCdhPlaoyoqxJiAXGfzuKj1hBWkBhNkPAshTSIJ-OJG8Gb_zWzKs3RGUXoOaeZGpugzuAECazilHsIaZN0GKqFWD2pSKdib8O_p9_7aNnJ_iaQg_YvoeOnqGjd91c4ixQEzSzZ5SO4n9YOlUolfJmODdHo-Xn1eJ-lCO5l-FfI9SCp4QCLdvSMKM4DQJCQoVY49wPhYm8cXRqqdj4THEGDCMOUATxBeu3EwZpE3zj5OsVUI5s6la5TwL_iATw302ssiPoY-wUwYjfxmnzp0deFimXp43qg3IQVsXfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 17:36:46</div>
<hr>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3uSPtskXzNgUsIvsQjgC-J7KgnGN83yiVHewGMfJ6LwPuIJDgo6q5A-vNalccuhMMmXEhHd4SNcb_TSAFeZ83LsCVA4Ff4f__lYfTNTdcNOb9keG5G_L1lezPLXN1FdXNB5Zb8gR1q5su1GrE7Nm8hv5MS2HWD6IV9zt7jg5BBpHEPBI8JercZDV6Nwli2beTIXG4aA4twrYHtlQV0PfVfUQSHHSCwnVu33f36oUj9J1mwWbNks8sWSKo20UjXeMlux7qqTvXY0H_GAGOZJwU9U_m2KEkJRlvOpH0de8xr8wWQPCgKJAU8isJI8P7KL_Tho9G_ThxeltUrOeJTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=Yvud_BAQjTTMUiiFI_emQbzFd-QjDYSMrLGwiokDnxRpFhKJ5GwjLk7AEm6TTm3JwswcQTv5VJgxWQYS6MxI0dWSM5tp_rWrscLsxxi89OdXagc83_SFalyIQkM3ZNPZ03T02xfWmfy_x6gWb86DrbRAs-SAyuIr-SYOPxrKUoZkfOZ4hQT_cbtdAmI3ci0CdC65YIKyEy-SdOtUPWW9voRac0x7QpyHfFUz2HRiVqKi5_-VRkHOCbTida4C753ZCWUg7BdAwp50Gk-IOUwba3jDqeTuU30GHFMGZAvUfwKSrGjmdbgPSqTlFfJIdAmGDWhEuvRK74FJeYFOZaHGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=Yvud_BAQjTTMUiiFI_emQbzFd-QjDYSMrLGwiokDnxRpFhKJ5GwjLk7AEm6TTm3JwswcQTv5VJgxWQYS6MxI0dWSM5tp_rWrscLsxxi89OdXagc83_SFalyIQkM3ZNPZ03T02xfWmfy_x6gWb86DrbRAs-SAyuIr-SYOPxrKUoZkfOZ4hQT_cbtdAmI3ci0CdC65YIKyEy-SdOtUPWW9voRac0x7QpyHfFUz2HRiVqKi5_-VRkHOCbTida4C753ZCWUg7BdAwp50Gk-IOUwba3jDqeTuU30GHFMGZAvUfwKSrGjmdbgPSqTlFfJIdAmGDWhEuvRK74FJeYFOZaHGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=nA_pUY5seoJ7GHFJFcjpUjGgd16hqiKcPZMMU_AbDSPEL1eYL5SR2Lc3yHKXcwgJ1O4zQEHhx0GfYPPFw8ygf4aLeDAXCUS2x4qOy8ZKL26njVn4pR_Fqn03S9Mn989tXirWaSprZSrXg_TWp4gTLS3aGVHcEnIQ0wB79A-ejLBDQYykr-SrlHrkGPPpV-vdegI7UPaCNwAi83IudeYRfesIL9zjdDO8ZGhyU_kmTGpjqliieG3funN5iDs2lX8sTy2urUcueTkh7tWkXR0NaHsg1Arw-I1cTVB8o61oc_t4FBEHBSWZRF4MIWh7iwK1lN11SyYOCmVDfZ0n6Yitcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=nA_pUY5seoJ7GHFJFcjpUjGgd16hqiKcPZMMU_AbDSPEL1eYL5SR2Lc3yHKXcwgJ1O4zQEHhx0GfYPPFw8ygf4aLeDAXCUS2x4qOy8ZKL26njVn4pR_Fqn03S9Mn989tXirWaSprZSrXg_TWp4gTLS3aGVHcEnIQ0wB79A-ejLBDQYykr-SrlHrkGPPpV-vdegI7UPaCNwAi83IudeYRfesIL9zjdDO8ZGhyU_kmTGpjqliieG3funN5iDs2lX8sTy2urUcueTkh7tWkXR0NaHsg1Arw-I1cTVB8o61oc_t4FBEHBSWZRF4MIWh7iwK1lN11SyYOCmVDfZ0n6Yitcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=CMLyp7-i9p8NUczICg6FC5RZk183dVsF5zcgxeoWDUsbeVoyKIjyWZH_Rq0X82tTsJjU2ufjakbsrgkpta5NaSfjdZoHXvOm_weeF2jdG02WSOpvgE-LQ_-nicRP8qbjjN895qZ3WlNFug1g2DpT5Rmk85kGuyyDVltyud2ihFKlPtiadzf1qw9HZccCsaU7aHioC9wjLeNZoHMqBqd-bDkvTygG0wAVi6r4VodfkEoPM5cOwL9GMNGOmzJ8fFD20IKaVMP7uRdlXAM-7dAFNUHwi_p25dBHMuQl0z9toUyqIHtJS0cg3gqhA3VqmbrnfDeqiJgGQ9Th5b8d0IUBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=CMLyp7-i9p8NUczICg6FC5RZk183dVsF5zcgxeoWDUsbeVoyKIjyWZH_Rq0X82tTsJjU2ufjakbsrgkpta5NaSfjdZoHXvOm_weeF2jdG02WSOpvgE-LQ_-nicRP8qbjjN895qZ3WlNFug1g2DpT5Rmk85kGuyyDVltyud2ihFKlPtiadzf1qw9HZccCsaU7aHioC9wjLeNZoHMqBqd-bDkvTygG0wAVi6r4VodfkEoPM5cOwL9GMNGOmzJ8fFD20IKaVMP7uRdlXAM-7dAFNUHwi_p25dBHMuQl0z9toUyqIHtJS0cg3gqhA3VqmbrnfDeqiJgGQ9Th5b8d0IUBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=e2YCkTGrcGXkbH_6SA8K4x_uP3glLRVzoSqH78JKHbIqJDKYoToPthakiW6gdpXsko65UhR88JnBbO6lLOWf5T3Cd9DJEpyqa1qSsantY6szZfRDOso_uOtcJVLMCz02nPFltARhfy4cYOmw7dz_clOYGSOGtOR13XMCbmOPUwGEM83irMhRs1FNfSY9xOQMoCo2sok9JEl5N2WGDS8WiUFJ4dbW6zCnDEaOoUHEeDgKJbDJ9QC0ESP3_ZADAUbycfr_w_aeR61vJSOIlCKrOxI902m-v7ZazUFnisGM5CGghj3yFXRR0AeL6KG1biIV_H_lhsz88E1nY17Khp3zsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=e2YCkTGrcGXkbH_6SA8K4x_uP3glLRVzoSqH78JKHbIqJDKYoToPthakiW6gdpXsko65UhR88JnBbO6lLOWf5T3Cd9DJEpyqa1qSsantY6szZfRDOso_uOtcJVLMCz02nPFltARhfy4cYOmw7dz_clOYGSOGtOR13XMCbmOPUwGEM83irMhRs1FNfSY9xOQMoCo2sok9JEl5N2WGDS8WiUFJ4dbW6zCnDEaOoUHEeDgKJbDJ9QC0ESP3_ZADAUbycfr_w_aeR61vJSOIlCKrOxI902m-v7ZazUFnisGM5CGghj3yFXRR0AeL6KG1biIV_H_lhsz88E1nY17Khp3zsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=b0aASqVQqLnoZrYqsZVF0a4VDIGhIQh3aIZUG2wJMbTbwl20PJtnpCWp3cMBjN54FFmEjOjupWmg_M6IPByMmwp9_6BtzgLY51dBzl9DhBaVMgZTOkdCahDJ0g2f6Ch1H-R2vtMVoUMeMuS9CtVmOErZbhZylc8WWUD8fspBlnL3ipdyhmcmL41ys-xW02m89Ljl_-TrZeojDHbcx3NV39FjQd4I3cI-XtAT-dB5xbiT_RqWNmLsgGTrkPT-deDG2PMEfcfkBa0kRVLqCdrNuREVMYLNr_eQ33fj4qFUUiL5Lah_BFi2QU0fNDzG-4mvBesJDQf5haZAbA8KqXm7Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=b0aASqVQqLnoZrYqsZVF0a4VDIGhIQh3aIZUG2wJMbTbwl20PJtnpCWp3cMBjN54FFmEjOjupWmg_M6IPByMmwp9_6BtzgLY51dBzl9DhBaVMgZTOkdCahDJ0g2f6Ch1H-R2vtMVoUMeMuS9CtVmOErZbhZylc8WWUD8fspBlnL3ipdyhmcmL41ys-xW02m89Ljl_-TrZeojDHbcx3NV39FjQd4I3cI-XtAT-dB5xbiT_RqWNmLsgGTrkPT-deDG2PMEfcfkBa0kRVLqCdrNuREVMYLNr_eQ33fj4qFUUiL5Lah_BFi2QU0fNDzG-4mvBesJDQf5haZAbA8KqXm7Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=Yg2382s4D_ieH7UGaHFtKN4AbhuGbzLK8rPE-1FBMd6VKY8pcXuHws87sN_EhsTvL_Hyr2aLCnLMXWCBd8PRhbIbFiwOgTJuV89FKnUGJu39Gm-6s1tDJHhUhG1TgyWGEa4BbP_ChmzIkrJYTKggLPcbeFrWw5YZu62fV2fLuj0PibKD5BDj_VHVmqu8XkvS6oqr1_RJWkK6nwk2ATwXS5eE-i8pi2KACoN6ZlrKk9nGsJFBzeYeN5PfP4Z4DhEZbXlchYVuwwNVeBPa1j2YUMB_k0nxTE7gcrsCl9EhU0piKW9Xme6wVW0gy9qL5z8iZVBKe4Ae2nusExlThbsZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=Yg2382s4D_ieH7UGaHFtKN4AbhuGbzLK8rPE-1FBMd6VKY8pcXuHws87sN_EhsTvL_Hyr2aLCnLMXWCBd8PRhbIbFiwOgTJuV89FKnUGJu39Gm-6s1tDJHhUhG1TgyWGEa4BbP_ChmzIkrJYTKggLPcbeFrWw5YZu62fV2fLuj0PibKD5BDj_VHVmqu8XkvS6oqr1_RJWkK6nwk2ATwXS5eE-i8pi2KACoN6ZlrKk9nGsJFBzeYeN5PfP4Z4DhEZbXlchYVuwwNVeBPa1j2YUMB_k0nxTE7gcrsCl9EhU0piKW9Xme6wVW0gy9qL5z8iZVBKe4Ae2nusExlThbsZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=uOYfCd4QH66qLIfW3d12ezrjtJG8osdsEqSPIjhwweXDkn4czDNgcobmxRxFow9o0hc6FCVVu4WWByQ_XFHyBtA4-PlU0vED1txa1yVIu9EWMCymMHvt23wOEPk5bbVqtdx7xWyxZyfKKlqGltlSHOnRTiiXno_wBDVkHfkT9AxD5hALtMyyKo-K1OVwJM1H7_bQU7rkzC8sO8tOjazgctwQkwVzkQT3YdCwT4Cv-iW-cb6mC15QbST23h4hTtqP1VJkkET_DUlLvW8RbfC7WD41ZnqFVzCn02CAwPSY9kmMOYLVl4RFHUmeTvcDWk2t2cAH5QiVJaqI0WPINJ9rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=uOYfCd4QH66qLIfW3d12ezrjtJG8osdsEqSPIjhwweXDkn4czDNgcobmxRxFow9o0hc6FCVVu4WWByQ_XFHyBtA4-PlU0vED1txa1yVIu9EWMCymMHvt23wOEPk5bbVqtdx7xWyxZyfKKlqGltlSHOnRTiiXno_wBDVkHfkT9AxD5hALtMyyKo-K1OVwJM1H7_bQU7rkzC8sO8tOjazgctwQkwVzkQT3YdCwT4Cv-iW-cb6mC15QbST23h4hTtqP1VJkkET_DUlLvW8RbfC7WD41ZnqFVzCn02CAwPSY9kmMOYLVl4RFHUmeTvcDWk2t2cAH5QiVJaqI0WPINJ9rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=KHbeQGXAjKmHGO0h-EVxAEG_Olys0u6OHY6UWXLV1IrfxvRfThZloiZUTwexkH8GLjydwMpJDxk_B9exWiHTQSRMWF0LCvhMloi5jnEMaujGz-81r3wYDNrcRwHGmROScbrCZYOSGWMGUosFvGCI4ptMGd8aS7dDIdC-6GZCgoWnz7ngVoLL8y77XAPUbK1vORC4tlv_-iiFtook-mulwcuve-zvs9Hl6TSpYPpEzKNiY7a_A67uvVBOD-et1bdet6FIZB9d0c42SyA6KNwkA26JXbUmM3-KFN7XPSJgSBbqFu-w45GdUwUCW8N50bJ7e3rzuZnikOFgyhh-HJ7Dxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=KHbeQGXAjKmHGO0h-EVxAEG_Olys0u6OHY6UWXLV1IrfxvRfThZloiZUTwexkH8GLjydwMpJDxk_B9exWiHTQSRMWF0LCvhMloi5jnEMaujGz-81r3wYDNrcRwHGmROScbrCZYOSGWMGUosFvGCI4ptMGd8aS7dDIdC-6GZCgoWnz7ngVoLL8y77XAPUbK1vORC4tlv_-iiFtook-mulwcuve-zvs9Hl6TSpYPpEzKNiY7a_A67uvVBOD-et1bdet6FIZB9d0c42SyA6KNwkA26JXbUmM3-KFN7XPSJgSBbqFu-w45GdUwUCW8N50bJ7e3rzuZnikOFgyhh-HJ7Dxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=oZsLvQYx3QCXQii7Tn1z5wo3mHhBsMSRBwWAV6pQdNN4eoYdrIOUx0K4qlfhrg38ESchkMWY7Xn0oQPWF6tjJm6JMiEZky6pbOWuBAY5vHyZBzwL1BI_XL4FyAFXz67WqOnItVRF7K9kFOze4obqEL8zy1iy2AhkpLpRtfTxVAUt7PX3n6Fj0Xvqn9h01cYY9AsXkc9SojXPGskHDryUUwIsF8NIXGxOtw_AQ5uat3XWpZVzX70WFmHaT1WYNmQac6az847GTn9_5OkRDQEIAAiYa4MBSpmLhCp4Trm6rLXO6M7pMROt2AcR2ReOTCcXU0T3ewWKOMIH0TPALbRD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=oZsLvQYx3QCXQii7Tn1z5wo3mHhBsMSRBwWAV6pQdNN4eoYdrIOUx0K4qlfhrg38ESchkMWY7Xn0oQPWF6tjJm6JMiEZky6pbOWuBAY5vHyZBzwL1BI_XL4FyAFXz67WqOnItVRF7K9kFOze4obqEL8zy1iy2AhkpLpRtfTxVAUt7PX3n6Fj0Xvqn9h01cYY9AsXkc9SojXPGskHDryUUwIsF8NIXGxOtw_AQ5uat3XWpZVzX70WFmHaT1WYNmQac6az847GTn9_5OkRDQEIAAiYa4MBSpmLhCp4Trm6rLXO6M7pMROt2AcR2ReOTCcXU0T3ewWKOMIH0TPALbRD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=dxNSe7dzjBUe7jHOPzatp0_DhkWivvu0ywrb7A7oVhOiRQTv1IhbHXCEfSUlxsDFoic4v3RcGsmEIwijdMTl1AHOunlqa4Zg9xAGxxM5BkKXh0nN9GSv1YZFRU5EDRTsZo_FpHEFNuMI6E1GtYvD_32X61ea1byhl2_wksrSeYWS1wRtefYaYLxzYAUg-a_-A1W_o8S26bVg3-XWs7iN2kzdoFLRk-6IYoAYq7_dd9awAxLDUHEqG3OXDNiYCF95JI-BhdSwoXIO8ODaj4YPwG6je5IWQ3xwHYOIDI0y08rzvcv2YkL00BWPNFcIKm5RnoFBxWis-U7FPfJ073YIjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=dxNSe7dzjBUe7jHOPzatp0_DhkWivvu0ywrb7A7oVhOiRQTv1IhbHXCEfSUlxsDFoic4v3RcGsmEIwijdMTl1AHOunlqa4Zg9xAGxxM5BkKXh0nN9GSv1YZFRU5EDRTsZo_FpHEFNuMI6E1GtYvD_32X61ea1byhl2_wksrSeYWS1wRtefYaYLxzYAUg-a_-A1W_o8S26bVg3-XWs7iN2kzdoFLRk-6IYoAYq7_dd9awAxLDUHEqG3OXDNiYCF95JI-BhdSwoXIO8ODaj4YPwG6je5IWQ3xwHYOIDI0y08rzvcv2YkL00BWPNFcIKm5RnoFBxWis-U7FPfJ073YIjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJszvPg2qluYm2yiUpKE40nwVl7yFYiQH2_HAuERTekoNFTueZZTQ-9-EyDUTY04fj7JJd1p5dRwmsaM8vB_CO7yT8Kwt7chlF0fD_t1nn0a_U1N1RCzY241qVDN8JVRl9nLhaLda5bn4PBlalk7oOOi3T-NOyL2XV0abVsUyq93US67jcPvkP2jDLlv-WTzZ-zTkZuJ7nlIy1ytACMhyws2IXJZF5NqDHsPkzvV8ldo3bMbN6gLxPUAGX6hGirWQR30Taa_-kcZCA1_bZRxWbOFLAxMjiVvn7MWceRLxQsOvfoA1EAvHVCArGRiGIQden63eL-btvL5Lmm1oUNH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScyjBYR4GBbhLlK57qhkyU2lC96IWZFOdYhPtup0bPv6prC8VHRJqhQWyirZrQylaakjnLzH6A6MKWwXeNwqqOhT5MiS8tVLAl3Gw5a3CkfH9DDMf_cikXUP-hCxTOEcheLn-jQh8vaXIYcixpHwCNvUluw39ZfBOQm9pD_30VLW0yFjC83kKsSQMhoZqv_4MiB2IpCXU3aC2HeUIA6ewDAh4Svbwfx4l3PH2ZSI4YkvbNzRKVRQSnD23g5vAVrpLcc83e4HxzAhk4IPtk2_Mw1uu0pHAT3anO8ufnrRW_gYMLrJO_VcYNQJOcKm_0eY_BF6g8PSVwQx4ERhzqDcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHrzQoQ2IKPffqgwpgWQjCZVKY0Z-8lyVKf05aIm26hUoi6dpaFdZm03gsckCLbBksAgmcN4ZZ2Ci9DW86m_j5uilXJH6et2a8hABlUMLUffOD40D78yxTDVrE3GnVqsBj1IVLCZUQJ9r4MDXxNjIfNvs1gVA_AiJxCr0ItOMFM2-GKjFoL-J-bYZbNbVDPXHQigDdF5htu2hgODT49njilX69dNeKQgYFpW53uSBIoQ2KK_YH1e-KLLNCxK_20TVd4y8xmrU-mDq5C9IKT5NTsy9OCwPwIHlKkGhd2-KUu9LkM0aID83nfMvq14V42038lFAAd6oC5fwpfdoYyUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIhpvwUUlx76VuZjsVmmhDm0Y7JfyuhqJ1mBmsly49i1jqWRLTnZ2RhZbBlWk-u4mHz5m1kKPhYuEzkbL4o9x3iPeY9CTs_Ao_5bg499g0gR2BmNSH3yaInMV2h75sRN1V8gfhKEKVzy-TEee3MQzN7vvvBXdDzpNDkauUSZXrSr7U7lIjd29fyBuM0o3EBACTPdHN7WbaFu1OEo_LlaZMgcVbFjuwztGR4xWjKUtK6sKSk5g_j_SqJZJ2gW95g2kARG_gS6iRVDxdY6Z0Hn3HsV1WevEQjJ2eJT5m1XgzIX9GY7Dp_LOq3pifBW2qoEJ7jqs8IrpI-HVk4t6tnrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=QCCA-mFVRRbQ2YSwt92VG3PFhZ9LiLBgNSPeWcgsVhg46tuhr361cVMkHj7t90C4ffUhiFSFNYDeMJqCwd4sI9BEcEb3FBTiBsIuJEPuGC6FhczkWErfcguVFnhaqcckGrxLb3COREoBSziVts_OZUbSepswWFM3l4Eco0rBfNKE7IayYZmJOJZH-6EZikHtSbRT380Me56MaNDU3kXfMs56ZXkrZCshf-YrykYguULuTaVYDnTClFM6gQeWrGOW7GXwlKMKTMAKmYaJboLWy8HRxFCZu6JaeRoC4-B1VPqKSD0J3TZFE9bCpDnHLy2j1rWUFjubKl7skIFrZWIb1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=QCCA-mFVRRbQ2YSwt92VG3PFhZ9LiLBgNSPeWcgsVhg46tuhr361cVMkHj7t90C4ffUhiFSFNYDeMJqCwd4sI9BEcEb3FBTiBsIuJEPuGC6FhczkWErfcguVFnhaqcckGrxLb3COREoBSziVts_OZUbSepswWFM3l4Eco0rBfNKE7IayYZmJOJZH-6EZikHtSbRT380Me56MaNDU3kXfMs56ZXkrZCshf-YrykYguULuTaVYDnTClFM6gQeWrGOW7GXwlKMKTMAKmYaJboLWy8HRxFCZu6JaeRoC4-B1VPqKSD0J3TZFE9bCpDnHLy2j1rWUFjubKl7skIFrZWIb1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=jm2tOWWzLZgkxTZ1evE2dcu1j88cRbmRGAF45Ga8v6S40MDuwd5YUYFFpMcrG6uH3H2oXEi_uDRv991XZG3RSPww2utQD3_uqPfKU0zWis1J1NiR75lcRZgDVQUq_RbNfoW8ZrA3LJNKTixbnU2LxAvDBwibpe-TPBWxIYl6hJ1A0QkChw56d78m9XPjErZq0iQX5wrt_6Di-g-htgVLDa1nJRtid4CsQKhJ3INPlSLLHBZVgAKmv0mUoJf34wBno787BhY_kOaNACZKWrUhA9lEuTlK2ChoEAcipnpTi1Z1hRbtJIceqUTkEXY4O5-gk3_nii86hxFHiqcLyQnsSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=jm2tOWWzLZgkxTZ1evE2dcu1j88cRbmRGAF45Ga8v6S40MDuwd5YUYFFpMcrG6uH3H2oXEi_uDRv991XZG3RSPww2utQD3_uqPfKU0zWis1J1NiR75lcRZgDVQUq_RbNfoW8ZrA3LJNKTixbnU2LxAvDBwibpe-TPBWxIYl6hJ1A0QkChw56d78m9XPjErZq0iQX5wrt_6Di-g-htgVLDa1nJRtid4CsQKhJ3INPlSLLHBZVgAKmv0mUoJf34wBno787BhY_kOaNACZKWrUhA9lEuTlK2ChoEAcipnpTi1Z1hRbtJIceqUTkEXY4O5-gk3_nii86hxFHiqcLyQnsSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=tr7aex7J9PpV9hgvQjkKfoLRu3-lE7HgdedlUcoPKJjrfxyDwoeIyD2tNy_j5IGC2VqDGrRm-pmTIMvAdAz_kr6CtTrUKosXC1eQ3JJM0ItK0Sc7jGILcEm-xrO_SVfcseTUDBnbLV-kaslMAYXljMZwUPe3AUjuDkhjF_slhXwetz_IupakAY86Z4YOmAaYY7EMDLEkjMUgWaUdp8a0sp6MhCN6AK5j_kLTo4huW1jzG0FGjan9tIV_XqXqOYTFtPUesI7GFW8VHBTvjrAyD4O4T0l61pHSv0oMiQUE69GHGC8XwJsaMhVbYpFcOUNJBJbnqFDZLfEAYIXgwg6Ibg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=tr7aex7J9PpV9hgvQjkKfoLRu3-lE7HgdedlUcoPKJjrfxyDwoeIyD2tNy_j5IGC2VqDGrRm-pmTIMvAdAz_kr6CtTrUKosXC1eQ3JJM0ItK0Sc7jGILcEm-xrO_SVfcseTUDBnbLV-kaslMAYXljMZwUPe3AUjuDkhjF_slhXwetz_IupakAY86Z4YOmAaYY7EMDLEkjMUgWaUdp8a0sp6MhCN6AK5j_kLTo4huW1jzG0FGjan9tIV_XqXqOYTFtPUesI7GFW8VHBTvjrAyD4O4T0l61pHSv0oMiQUE69GHGC8XwJsaMhVbYpFcOUNJBJbnqFDZLfEAYIXgwg6Ibg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLhKoGGJ1n2xaOu3BfjYEgdMsZGXXwOvfjK95AcsbrfGF6HCkzIXje3vFj2vJalZYMJ-YdBoRIOixjSQvHPEJMIbPOCTNz8LuwzgX4jA0GGIcEd2py6whRpJSB5PTutCI4Us0tBaV7vjheA1slp_HH-KbD97z-9fhtcx-kMSVoniy8HlMee0TLlJjOHGSwZBouQ2-lXKv5-g-nGKqGo31tPOCGTyCvO7LoqhkaQDi5l06Al7nmvtSBV3sJmVDiNYqWvcE-gf1YADUvBmef37h9trSTnknBgEwf6xOolHxvQCwcA4of15Ubo8peXyOIXkBgxGVU0omvAJEjv33AI4pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=ZgFOj8tv4WzeHke8S-zg5sOdwpSBHINig3fo6i81CXe5H051ii3-MFVqBC4hnQmNpxnpEso5RI69jBgmNc5N8dlvj95JkTlCcj1-_EstaWu73oHex5741ScI4lpl6wTHAAKq4uXEdPMdP4fP-q8sCsuZ1utPNJUyuQ2yV-E25iuE9Artoa28Xr-61IaAK1oabU1rp33za4UVjdSp7ODD8j3YXV5ZCDye4oznwuPgcpacENGsw1uYIODIM74jLafoM46AcSKTD1o9xvVZ7ge_xYGkDszR7LuQzU_zSFnRJO7MX1Yehw_cYSUSDXdoNg6f8W3sCUBut0HxvsoXa8bz6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=ZgFOj8tv4WzeHke8S-zg5sOdwpSBHINig3fo6i81CXe5H051ii3-MFVqBC4hnQmNpxnpEso5RI69jBgmNc5N8dlvj95JkTlCcj1-_EstaWu73oHex5741ScI4lpl6wTHAAKq4uXEdPMdP4fP-q8sCsuZ1utPNJUyuQ2yV-E25iuE9Artoa28Xr-61IaAK1oabU1rp33za4UVjdSp7ODD8j3YXV5ZCDye4oznwuPgcpacENGsw1uYIODIM74jLafoM46AcSKTD1o9xvVZ7ge_xYGkDszR7LuQzU_zSFnRJO7MX1Yehw_cYSUSDXdoNg6f8W3sCUBut0HxvsoXa8bz6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=WXMXb34ih5L4VC1mtd14LvheITyzyWSQUWiRxkLPGA4dxzUAJlPofxbI8aD6wqFyWC383OB0K2qVCFKx1dDixJUHNOH-SvNPmoEgDLMVS4Ju-quCl30lyV3OGl-xyJ5rZ-07M-Hcw9dH9-Zis11AYefNMDBKcoehVDlUp4x-AC2rIIlUIWk6cClEYhZ7iINtXXeYU5gCoNFyHqdNETfFmrXgimVgG2d6Pw9NJ41wWLP_AHV-GIx1PKuY5agivcyeET3pF92o47mLGCLspEC8S_HUzl5nM6Aw7s5km1B8_Hu2z0CImtykHXcC0h31QvflfCOIeNM601t43rlA9ZapSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=WXMXb34ih5L4VC1mtd14LvheITyzyWSQUWiRxkLPGA4dxzUAJlPofxbI8aD6wqFyWC383OB0K2qVCFKx1dDixJUHNOH-SvNPmoEgDLMVS4Ju-quCl30lyV3OGl-xyJ5rZ-07M-Hcw9dH9-Zis11AYefNMDBKcoehVDlUp4x-AC2rIIlUIWk6cClEYhZ7iINtXXeYU5gCoNFyHqdNETfFmrXgimVgG2d6Pw9NJ41wWLP_AHV-GIx1PKuY5agivcyeET3pF92o47mLGCLspEC8S_HUzl5nM6Aw7s5km1B8_Hu2z0CImtykHXcC0h31QvflfCOIeNM601t43rlA9ZapSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jTpz8YuEtHv3EWYM4DgdBd66W9JrdJyI4VZOBCvCKmv50lhPdu32hAI96tr0DVa1dfcI49t0i6g_imbyfe3eId1Ib5TnyjB4slCeab5OUFz2v6oxifCTVzv-VRkLv0QKYOd-UhWRRyR0TzHvLPnHporumlM7SgKydUe3NTi08veKK81pom48fNdjTJwZZrgElQ6h8UxeNQBnyMgu26zIsK8L7dGOxp96nlwUf4QQI3oGaDm8XTMRQTAz4pF9ALVbZLyy-5xrX8GuhWBsb5avTWpJYutNkhslbY1FjeolqqKxAl7XINAo_8ojPiolBXsMc4JemtX5OYDe1LBoNsUCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=DlCvA-Ppuoce8qQCp3mAihszzejvoZ5L6tU_i5Dv0oMOqukNMmshgybS5CRg3e3N_bN_4NnExe0V6eNfYrYXjIkbkxJUUeLo7CF6IYzABl8NpiPocg5eqhvko0No2hcEZL9aLgOj7b5EiGaP3XDZXSuewyY5vzfKopXwM_cNTCeKlyn_3m0-2h9OHVvTqHn-O75YoSIr4bYJCqlPu2W8PgVY1dc6GRv-JDX8RzkRl40swHLZLXlZhEE417mM59-kDmf7NqJz7k61mll_t3GhVkgSvl7HCKRTrHTVZmBHVdwOvWvB-PLEIJhekdJYyr9wE8-9Ab9m4kTvsvr7doK6O29Rt4Y3e5z7HuHBixQPYOFOHnzQrz_tj8wLvzY75LwRM2faCSwZvNIeqhRUOld6AV47Cb_dvXR6ocEXCgMszib-eKG1kyLGNPP5BsRCt43-YHO0uSOgq8D8QHWyFBqIEQKHgEEJnQSZsiEUHSiZIl0ueS2apzeajXQvFQSDvk3ZCShiXxahYfod0yYwS63JP74XktpKn4z7JWAYi0fuOjfHdpWL6_vaZsAOPrkRJvhvQVJhUYLleOyFlBHlXGUrcu_rrWVKk37aAp-LhRnn2EzVfxYauuC-Z1ArbJp3xV8xvn2vCFp2cp8gY1EG3YYDkYpHcJMpfM9mdT3RxA1XueQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=DlCvA-Ppuoce8qQCp3mAihszzejvoZ5L6tU_i5Dv0oMOqukNMmshgybS5CRg3e3N_bN_4NnExe0V6eNfYrYXjIkbkxJUUeLo7CF6IYzABl8NpiPocg5eqhvko0No2hcEZL9aLgOj7b5EiGaP3XDZXSuewyY5vzfKopXwM_cNTCeKlyn_3m0-2h9OHVvTqHn-O75YoSIr4bYJCqlPu2W8PgVY1dc6GRv-JDX8RzkRl40swHLZLXlZhEE417mM59-kDmf7NqJz7k61mll_t3GhVkgSvl7HCKRTrHTVZmBHVdwOvWvB-PLEIJhekdJYyr9wE8-9Ab9m4kTvsvr7doK6O29Rt4Y3e5z7HuHBixQPYOFOHnzQrz_tj8wLvzY75LwRM2faCSwZvNIeqhRUOld6AV47Cb_dvXR6ocEXCgMszib-eKG1kyLGNPP5BsRCt43-YHO0uSOgq8D8QHWyFBqIEQKHgEEJnQSZsiEUHSiZIl0ueS2apzeajXQvFQSDvk3ZCShiXxahYfod0yYwS63JP74XktpKn4z7JWAYi0fuOjfHdpWL6_vaZsAOPrkRJvhvQVJhUYLleOyFlBHlXGUrcu_rrWVKk37aAp-LhRnn2EzVfxYauuC-Z1ArbJp3xV8xvn2vCFp2cp8gY1EG3YYDkYpHcJMpfM9mdT3RxA1XueQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=WOK4ClN3qswfY2auQQJhRTsm7P4r825Zk9MZ1-0Bu8RynDGahYPLEKqG1B7TDFto-iVnTvx-6OPUOy4hZc4uVwW8T-qzX7CJ2crsqxUxSxZgFwOoaF-U9W_enaqb9ubYv9p11sZm5SJlermhQsAB_hf6D45LfQ8l3QTE1Q6QLL24S6G-TfsGltcP_Ain0YcUxUWxN-vd2RNUAgUvzV4xTKFBfQ_FPAgejLOfLp8ZH2fqIRw9eSaZDDoX4cOR0lV8YbWFrjR32-covsFAIKtkTpO51XqhtU1j44l4brcpjjPG9mINwOy651u-XFH55hGBJVHkoLFJBmS-mDV66-pFcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=WOK4ClN3qswfY2auQQJhRTsm7P4r825Zk9MZ1-0Bu8RynDGahYPLEKqG1B7TDFto-iVnTvx-6OPUOy4hZc4uVwW8T-qzX7CJ2crsqxUxSxZgFwOoaF-U9W_enaqb9ubYv9p11sZm5SJlermhQsAB_hf6D45LfQ8l3QTE1Q6QLL24S6G-TfsGltcP_Ain0YcUxUWxN-vd2RNUAgUvzV4xTKFBfQ_FPAgejLOfLp8ZH2fqIRw9eSaZDDoX4cOR0lV8YbWFrjR32-covsFAIKtkTpO51XqhtU1j44l4brcpjjPG9mINwOy651u-XFH55hGBJVHkoLFJBmS-mDV66-pFcoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=twf-8c9Mk6exaHa-BXrCIhjXZuQ8Ghuylzs2D8dUyT-6VRlsswdsAKrEnuc21GDPCSF14OROyIkwx1G0Dxy_nXKME6OWsysPdXN8Oqo8_hxYYe19xDPmHykEvcIUnXSBt30IqNMwwt4UGjrnd3WN6Gvjt7ff49wxmcQZucSvZOW-_FVgTpQZIuJ-52EmpTiZMP153mhsP_G8Eh9eLcRU6ZM-4S3b_wZQ3iHGi4V3A5B_FJJwM2d-zbhaKldxBN1NI-w9w6M6kxH0L2lsH6UHwEHa0pAF7rhopHdULSC-WmKB93yt94OhdmeSp94ev5XEPAcFLFWIb8O3joQjZohe1xMwcRwmZMNKTIXtPQoirgelxVuZX86czn88_mJPqElj9tvdy74qsfhLm_TxUT64zSuV5n5qmvTgL9Cg6tmIuPeyh3X_RLObBsC_6WdViLyyiscs4M3UsuKqJRomZj0-6UqF_XqqwWEAJPV1u0x2J_RjeMIlV9FBUhKIkSCN0joc10HQsnL7DJyAm4AmKt0XjLqgovMwRamUWpA--WoZpT3Gs7ZUULekXqxqika19cMA2Hz6CXXe0zFGRM1OuBaGpF0iDR0eu26MqElGzic3LdyO8pkxNPE2p6MdhALQ9HomaibSgb89oSP5UUXhYr-Y0Xzb6uOCSoDAbIdiG0a3FSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=twf-8c9Mk6exaHa-BXrCIhjXZuQ8Ghuylzs2D8dUyT-6VRlsswdsAKrEnuc21GDPCSF14OROyIkwx1G0Dxy_nXKME6OWsysPdXN8Oqo8_hxYYe19xDPmHykEvcIUnXSBt30IqNMwwt4UGjrnd3WN6Gvjt7ff49wxmcQZucSvZOW-_FVgTpQZIuJ-52EmpTiZMP153mhsP_G8Eh9eLcRU6ZM-4S3b_wZQ3iHGi4V3A5B_FJJwM2d-zbhaKldxBN1NI-w9w6M6kxH0L2lsH6UHwEHa0pAF7rhopHdULSC-WmKB93yt94OhdmeSp94ev5XEPAcFLFWIb8O3joQjZohe1xMwcRwmZMNKTIXtPQoirgelxVuZX86czn88_mJPqElj9tvdy74qsfhLm_TxUT64zSuV5n5qmvTgL9Cg6tmIuPeyh3X_RLObBsC_6WdViLyyiscs4M3UsuKqJRomZj0-6UqF_XqqwWEAJPV1u0x2J_RjeMIlV9FBUhKIkSCN0joc10HQsnL7DJyAm4AmKt0XjLqgovMwRamUWpA--WoZpT3Gs7ZUULekXqxqika19cMA2Hz6CXXe0zFGRM1OuBaGpF0iDR0eu26MqElGzic3LdyO8pkxNPE2p6MdhALQ9HomaibSgb89oSP5UUXhYr-Y0Xzb6uOCSoDAbIdiG0a3FSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=C1Y-wv1zMK4rQRU6rCxDvoWaHs_lKmazjvJWnW5bUwpn622TgleuL_n3J4wCT9q6DjBsvtyFTjfWKCfv6BtMk-uQczFkwF1CfVXQBLkhLH5Fi2_5fSSNvtjxdshQlfapK9bvKu4ED1_vD12JCYk-g2F1yz0QQqqSIyh4J1FkU0ZjLRno4gnqGR9BYFbr5XBKLOW7oLgefc5egpr7Q5KeGMimi1fvKNg-OrPPgzefhHxu6Ru78gNBsgHc9BDXOw6gHyLEdvPDsRhF1Zu3hZmZWlfY7Kj0jxIQu37Iukup9gfgj6DZ0aKbGxwZFM_vwGg6zajRK8kzeFjvLpuJJYvXlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=C1Y-wv1zMK4rQRU6rCxDvoWaHs_lKmazjvJWnW5bUwpn622TgleuL_n3J4wCT9q6DjBsvtyFTjfWKCfv6BtMk-uQczFkwF1CfVXQBLkhLH5Fi2_5fSSNvtjxdshQlfapK9bvKu4ED1_vD12JCYk-g2F1yz0QQqqSIyh4J1FkU0ZjLRno4gnqGR9BYFbr5XBKLOW7oLgefc5egpr7Q5KeGMimi1fvKNg-OrPPgzefhHxu6Ru78gNBsgHc9BDXOw6gHyLEdvPDsRhF1Zu3hZmZWlfY7Kj0jxIQu37Iukup9gfgj6DZ0aKbGxwZFM_vwGg6zajRK8kzeFjvLpuJJYvXlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=mN-K8KBjOJnlvKEK5kjHpQXNfpr326lDyy-VjKXa2miSeqJ5_AlXCcfvbstLpcWoqa0fP2dce0OEnvtN7yEzwquABH89l3Y1LO4cgmyjZOBs4B6o9HU8CeVu7b9rXL9CVYDdM_oXKtP0n5DSRgee-wCbwjVt4GEvcNd6YUwVp__NDkopbik6ZE1KcQL68QQO4WzDAkSVuLeLmjx4_h2AsO-VlhlroCEXjEmHWQTb9N8FyjcpwrS9EREqImpu4ZB4Ygro5AitNKvT2DmskzElMIk2Eb6SYvuMzmaz4s-nWvTCChqm8rt1hDxFKVgHLMalcrwhoRf6wk8fIFObYsH2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=hEXAyEjrCTwWreUISMzGbHHYE2Xj7IBv54k0xUe9pOTkktQSrVo7uVpwH3SGqCjzO9muZAOzmmWBoBMvDUhB8xRRlShr-mzPGRJ3-l4OP3jGuOp90P4k1XSYDQZ019yZA1JTI2cZyPn-XfuEp8zDdJk9bvHliVIxOOnp4OStrlY7Zlpxm3Eu2WKaf8Nwa7FLR6U6MqEycEiOxWrLk-DNsymNlwI-LB_4T3p8PnmT0hNszbc1P0uM4MBmotKjyGD7lJKFTB_RZLBQZ6WG5G8Z9A5m1SuKr4j_viy1yDdtOHDaBq_4EJJs0QfACG6qzlYXeC9Lu2XjvuDJWnEtnomqIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=hEXAyEjrCTwWreUISMzGbHHYE2Xj7IBv54k0xUe9pOTkktQSrVo7uVpwH3SGqCjzO9muZAOzmmWBoBMvDUhB8xRRlShr-mzPGRJ3-l4OP3jGuOp90P4k1XSYDQZ019yZA1JTI2cZyPn-XfuEp8zDdJk9bvHliVIxOOnp4OStrlY7Zlpxm3Eu2WKaf8Nwa7FLR6U6MqEycEiOxWrLk-DNsymNlwI-LB_4T3p8PnmT0hNszbc1P0uM4MBmotKjyGD7lJKFTB_RZLBQZ6WG5G8Z9A5m1SuKr4j_viy1yDdtOHDaBq_4EJJs0QfACG6qzlYXeC9Lu2XjvuDJWnEtnomqIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=JTMnEcaWDRKMMsb1-prxweKQPOupUu4gJ5RzLuZqiaxNsVKc_hwc1HFiyXxUOIAU2a09IqjmiORMezgl5qJPJf9MMCKTeiDP1l5PZRyuiK9Jwm_oourfnPEpmt28nEvknxcqyC3fY8QNJBOBPjGeUbbTzvd0Vtj-VIarK9inJk6RIXSixwBaKPKLRt8NPjbfU_iIg3930gMsQnF3rV5ozOvRgXnUlTXRynHi1e3QQXmFmz7tj3AVXR-q3ysBx8rBw_yAhEcedkLAo6H4-Kt4xYDr7j1N0N3A2wSZF8fxGcLgPZNak45jumiLcc32yngJLEhtbTVdIM4TQvSb3BIpTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=JTMnEcaWDRKMMsb1-prxweKQPOupUu4gJ5RzLuZqiaxNsVKc_hwc1HFiyXxUOIAU2a09IqjmiORMezgl5qJPJf9MMCKTeiDP1l5PZRyuiK9Jwm_oourfnPEpmt28nEvknxcqyC3fY8QNJBOBPjGeUbbTzvd0Vtj-VIarK9inJk6RIXSixwBaKPKLRt8NPjbfU_iIg3930gMsQnF3rV5ozOvRgXnUlTXRynHi1e3QQXmFmz7tj3AVXR-q3ysBx8rBw_yAhEcedkLAo6H4-Kt4xYDr7j1N0N3A2wSZF8fxGcLgPZNak45jumiLcc32yngJLEhtbTVdIM4TQvSb3BIpTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=RAHRO5PMpJI-z-pAjombzjloxkFuh58HNn7RK-bbkphQ1KEm5Iv08S7U8vceMfkY66bIk4D4q8_tBwtLFPZZCpfBfIBbMjTkf64PxRvvSVY-QjaM8446p7pAoI-65642_2S-v0tTYyodZXYDmOXzPNMCjVLDwtH1z9JN7xBJboX4RFPAsme1N_gvHTJhi_ehJ4_Z2_HpQyTrA-rji4a1LVcLmR0lp2PtN2Whc0oVNAaLk_81ZK4l3r2ys8VXjPUQc5SF2wAu9o4pOMEdKdcTGrX2lLlmWZhNdHtPnt_O7ANvNHkNJ9LdX-q8W-kvyHjnKNNG7VI3Fb-ZPgsyaRcXOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=RAHRO5PMpJI-z-pAjombzjloxkFuh58HNn7RK-bbkphQ1KEm5Iv08S7U8vceMfkY66bIk4D4q8_tBwtLFPZZCpfBfIBbMjTkf64PxRvvSVY-QjaM8446p7pAoI-65642_2S-v0tTYyodZXYDmOXzPNMCjVLDwtH1z9JN7xBJboX4RFPAsme1N_gvHTJhi_ehJ4_Z2_HpQyTrA-rji4a1LVcLmR0lp2PtN2Whc0oVNAaLk_81ZK4l3r2ys8VXjPUQc5SF2wAu9o4pOMEdKdcTGrX2lLlmWZhNdHtPnt_O7ANvNHkNJ9LdX-q8W-kvyHjnKNNG7VI3Fb-ZPgsyaRcXOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5aJZJ58_hrpDnpCPD7Sw6bH0yQxkc5_Th2YcV15oNtKBZk8jGxdmgCyYocXF2j7MGBCYp8rF7wMJIWVezx2hJi92LDGddIXyIqWmXV69VJo6mEvtl2ry-SMW5Qt7vEkYSiRxAzO5U4cY9XmpSP86_a-99aUFRqLxnJdijwdfBxZzmDWG8cqdMbmz8GcnCmLgH-MviOkBdEWP9O9ZArRv8tc365wU5jIjOWZABnQXlQrPu_n-r0NqRNx-Rre7_lfq8aUWnagiN_o8hSD04eV2kTLmRXFYqva7anZZkn8fJ7-LfD8nZo1rls8FAVJr7073ZBqkOYdmNRByosVQHZhHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=SSh-UchfwkxJ3veZihtATbrX8bhPjHGwAFv2TOnM4U2Ue-7Y58IcJW9OGcvl-zATXopV8XnaBFwZgcGGt-E1XnCJZCcZ98Rcy9nsHX_ICPQO3MKNMr_xZy_lOYM1-k6pgOJLGGzHqS7Tkg9sqy_XtLQR4uRViZc6rUrl_bN2FH9QwmyBTFzM7QKSvBrTbw79fIFPyn2ASCMILXFJX91mkVQFu9-4zxLSrfcsRIHwc6Yy4TizprkyWXPpf3PI1MWilefkaOK7Ym1k787d0LCjy716B6yx5tn09LDQzMOPk4RSTF3P8BPrcrAvERrwR3EiBBk6dYyn4BGDaUtgxUhPhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=SSh-UchfwkxJ3veZihtATbrX8bhPjHGwAFv2TOnM4U2Ue-7Y58IcJW9OGcvl-zATXopV8XnaBFwZgcGGt-E1XnCJZCcZ98Rcy9nsHX_ICPQO3MKNMr_xZy_lOYM1-k6pgOJLGGzHqS7Tkg9sqy_XtLQR4uRViZc6rUrl_bN2FH9QwmyBTFzM7QKSvBrTbw79fIFPyn2ASCMILXFJX91mkVQFu9-4zxLSrfcsRIHwc6Yy4TizprkyWXPpf3PI1MWilefkaOK7Ym1k787d0LCjy716B6yx5tn09LDQzMOPk4RSTF3P8BPrcrAvERrwR3EiBBk6dYyn4BGDaUtgxUhPhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66317">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحامیان جبهه اصلاحات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHU5mcmXPM8gclN0RArjokxGeoPPIAf_unDx0ouGZ0j6YW70BAR65vjAtwtG8lR1rZ18hFgLug6VdLbZBjvta5toWHQxn-2iU4g_qKo1uaq-qYGetXqBFaod9NYWN7uSUNhHpp7plV7td00vdhC7YbniIqh2GT--GzffX4IMFmzIjFmBDjYjBSNZQQp_mPbCx_l7B_GRtzyaOa7P7SNyjK6sx4CRG5o4VWUmu9lMYagaxcGnnBTA0_9gRFCcI561AtAjvsYt_9ugmGWuHOq6FetrEKPx8vzDKqqJI-iqhzgZBwnJVj8ahK4FyD9a1BNxp7PvcYh3OqaolvCrOGZ3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح!
@iranwprldnews</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66317" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIWseUWh4iH2Ga9SnvhKQAPYOHXCE1cs0cGBfrRlUtUEmAmiPdQzNIUttC75RRp0wcRQYR3SwiyvJ5f5zRVKyECyD4tBc6BjJJ4WdA663HC8MzO6riG9a9zOFMbdMdJcRWJ5h48keo90vqViCRtJeFV6CJEVp8gBXvL_nRs-0Alf5JY8bu1aazyQiiNoO3PfGd-_liQ5gNhNSVqk7d8OHBF9jxSlfyZuXNXrHkTIrPuhoHr05rrb7YjzSt1c56GW5k1S9H6jOGNVvxjOthFAyhM_Eu7KicC2YNADBhL4JiR60mBVLLxVWJAI_53gAsbIFkPl1GS99365Xg46ucttzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0-x1BdMdSa-8x77nAjzTMLx6ic1Xt0Sr12EWkJoBx0hXIJ8BZdr-oSVp_QCYqhbAiN6r_PwH9GxKRjpEoQg4EE0TJcJxLkVWv1VZNZGFK5_C24ezmzXprN9ovpMO0UgB2voy4gRsGsaeUC-_3SvjtGe0U4EEXXzEDp0b5B71Me-qzYhJyiq_2cTQVyQMUd2wGyF-K1cc_n38U_-fglh2HF-E53362AAOCsimRTVShrrwoYHKdXb1zNPJ2g0ouBNWbMFf4xpAYh_9blJryXOZySbqzMTlxh4abSUm2y7GWZYNGLSSEOctgn0-KsBSDrRm6KR0vW7mYF3VIMcNwrVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6pagGXr8Z4pnZJwJGWCv5sNwnp049JDQv9La9SYXQ0sdrCTuns8ke9aHPILIIzlG9u-4wXUpC6_7lDfMKM6l1r07q0szeCZnnCVpJ1M0ZSxB1Bj0G_LFNS_j1s63gyP5gCzSVf6iWPT96PJ1SlZs5tQIN_a5CPFZPJF0z_Pg5iqqb1kCz61Y0oFmwZcmNeIwbU3h1Nrq8GFmhEmlXRj22iF4gO6HzB9LvOpVMLuDW8yYgkHsAiiIhQv3chvIkReEWl8DVoQv0vRncAELzThGHef3pdp0bsQIN4ygrlQGFpQZUFm4tsRvXvm5taA15eYwj2D2ECxv2yJKjOb5FrL-zh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6pagGXr8Z4pnZJwJGWCv5sNwnp049JDQv9La9SYXQ0sdrCTuns8ke9aHPILIIzlG9u-4wXUpC6_7lDfMKM6l1r07q0szeCZnnCVpJ1M0ZSxB1Bj0G_LFNS_j1s63gyP5gCzSVf6iWPT96PJ1SlZs5tQIN_a5CPFZPJF0z_Pg5iqqb1kCz61Y0oFmwZcmNeIwbU3h1Nrq8GFmhEmlXRj22iF4gO6HzB9LvOpVMLuDW8yYgkHsAiiIhQv3chvIkReEWl8DVoQv0vRncAELzThGHef3pdp0bsQIN4ygrlQGFpQZUFm4tsRvXvm5taA15eYwj2D2ECxv2yJKjOb5FrL-zh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66310">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66310" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66310" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66309">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAONoys_m9Lj5QjfL9P_yvy2byAFCH-JEKMR9TAWCeTjij-A0vkg_tX-JSb6lOov8fM2kUlkdvjnxW7x8hlmLFpxu5GctYQkk4nFLfnV6CBwJPDkS1mPDCqlNjR9s35INoH2THQFReORH-Bgbc60QkcBEHGciFg46fOtVofX-3wUouIuFSw-IlshcB3_y9r96K0FOhL3PS4KlVGhKfn3KHy_hmx62FDtNaRhq3114w3hSO74jq4ESOEhFqD0vVQnu_xusl68e06eybN9iPRpVDoKhDCtBejvi5Y__CRrLOaWxEcYb1UoMrrTGvxsQnVbHSKvOf5XzXFFnQW--Lsktw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66309" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMAYaMhetpwAFFKdxbtzmEkBHc1ynBVfTVjRqznf6-SMfGeAgtQYOdGKB58PE6YMeO8pxMgGfddhjmoIVdInxkjncUsWHcQ96SmbLtmw6meNODq-aSZCb-JZacE0tRYBGHU6dhUqGIQpsd-362hx-2fXictxLlPTO_m6xF8A1RNfex3wMXPp2tV6USb2DZXSTrAOVL45-iYg0_8CMfP2lQO7wokAteQ3NwBiNZiOqlfM32-1O4Ia47YKhn1NxmcnPmSq4nsZu7k2fzE31SIppClSVv2DxM7LJ6p6TOy9PGk15Y2UFpjCxDfK6phEUPnbvO_gYoCWwWF7RjcrGazLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRjONr0assyrcgUjnESdbXJT7tfypW6XfAa87eoR_beaJGRt-0PcO-m7nHjqiRQ_mQaG359mcuC9Ewqawc3dDl95q-swvrWu1us-cXp--jddxyovOgTVIW5KTSTQe8n2q9l83GlSUqEwmwjK8nEuHUlAfncmgGeKAd0QMD2Y0GmvMBG9GDdUqAzgte6qtlibY_vSGjX_3CHY1P6Fy5B4kCR33GEk5NPrqN9RBhdjiKBbanz6AADDIt8KZ1V3bDrITrCWDv2ZW3glvG5UHPSmv1uijU77SdA7GDaMXuCRYkDzX77nSN_sT1fNLlMq-tsvecEZwFPe6xa9deImvUNCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=ZrwB81Eo5OHFMbLXvJftAqk4IqC1ej847spyqjwstNRaXxyvUTMMCZtcnP4UVejy-VqgJG8HaEVFKy0geoh8-LSFGG5S4_I3oosdYjlkJ6AnQeu26x6VJzkWc8wElkkPe6Nj9kLr4NjgdQHqxnp4HwoiE3M_IVQ_3V_tz5dszr8Us_M9npPAx5s7Nb5Pl-tXjMAmzD65THFasBNW4zy64SY8t_-dah14l0tJuk8yt6aM1w0z9wx6VB99pkvR3ujOnP3PzZeI4l56U5TW49275hCysTRMC-kVcd5Ljl79SdEv3RJY-rTI1SQcGz7IHLDNHrgSn33xnLXI-_BliDMoog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=ZrwB81Eo5OHFMbLXvJftAqk4IqC1ej847spyqjwstNRaXxyvUTMMCZtcnP4UVejy-VqgJG8HaEVFKy0geoh8-LSFGG5S4_I3oosdYjlkJ6AnQeu26x6VJzkWc8wElkkPe6Nj9kLr4NjgdQHqxnp4HwoiE3M_IVQ_3V_tz5dszr8Us_M9npPAx5s7Nb5Pl-tXjMAmzD65THFasBNW4zy64SY8t_-dah14l0tJuk8yt6aM1w0z9wx6VB99pkvR3ujOnP3PzZeI4l56U5TW49275hCysTRMC-kVcd5Ljl79SdEv3RJY-rTI1SQcGz7IHLDNHrgSn33xnLXI-_BliDMoog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66305">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOyW5eK_A5V93R9JjU9xLeM8o6rsVWEwODX5dsEjUVRbwOuTg42miyeyAhGErNjeoU5Hkuf2Oi9ZeWi7jZPELxFfSjuUODxDtSCNtGokzDMshoAU7kwFAtlGv3Llh9c7Thu-tviXP9TzdgzjukVH3QkZtdQ6bX68cxgLLRSUNlpIM7hqNTquktdrbxivjesRf7R-QJQaFRnJTktr_oyNKqZ3BQgPRkr89_IJpXt4VrYlv-WhDdrdKGV0LAdf-8b5ZO-efGp2NzHBAMrM1STRUg03t4oSJsaMz5epLQrJrscJwVwcn7RVTzMerTyZZknx8ZGYFrDwKJbWvUhf6onR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی رو پیش‌بینی کن و جایزه ببر
🏆
با ربات تلگرامی «نتیجه‌باز» می‌تونین بازی‌های جام جهانی رو پیش‌بینی کنین و جوایز نقدی برنده شین.
😎
۶۰میلیون تومان جایزه برای نفرات برتر
⚽️
تازه امکان دعوت دوستاتون رو هم دارین و به کسی که بیشترین دعوت رو داشته باشه هم یه جایزه ۱۰میلیون تومنی تعلق میگیره.
فرصت رو از دست ندین و همین حالا از طریق لینک زیر وارد ربات شین:
@NatijehBaz_bot</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66305" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcoSjIvy5D1iYPeadjMWO5SU0Ew8_qeAPRaS-mGKMTYaq9ZaRA5Bic07obiw1uZ4yQzsICeqaSSLtoI4Xo4hiLwCSoUALD9j7z_TEeZpgnuai0gEJmukpvtIGrxEDGOs1KgocbYNW8ulGQHWLKCemLVLaoOVO0PNPQU5xTs_N1KA0djc8sNXM1ib-VWIwe5BaNvT07z7MXtyztOeIs-qoRCDcJ1Yfwbq9cZb4eVwFfX6Y9iCm0XGCGQgfXkL32wAUHpIUvxdXoo_11Pw7sz2K9nMhix1h1qUyiI2lKN6v8IwYdpwVX3UG-PbSHUDVSMUsqUJulu2sdn2ioqG-a0L8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1kUAipm1zEx0AmbF67AiNd0YsJ1PSaME0QUd2-2mCkziuHrq3jJ5EMs4x1TO9OSMcG5qMexFRM3guGFUYTBrXhFjyNHrFR_lg7dkVdyEI-7wGkESmXzV8f4fk4gVTXWAhShROyyRXJkOZYS9hsV9FxjnM6-lG5jhPcJYBQ7QznrLrut0cirthzsUUsCR1ZAgEwl35sS22RuJaDYTY8em_JtxrhvOSVDC6qfBga32W926W_6h6dg8Z6zr6HDTajSOdQYWFHdsLUsACxd-TLnGJccLFED3xMLaRyHZUMXkTXNOmho2yRgMhbcs2RNmyajvuDa49ep3fBsWzjBj-EP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66302">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66302" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66302" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66301">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_sl5kEVLXHobT2UYM-GAYurkHfavtmSCWLC0VfcT1I-k5tVh5VNn-Y8JOvIJ6aTaXgn5AW8Eaz6aMeslgHfj7-n9Cx1Q4n71Yg2bdXHDE4zZs8XI7guFdWcQlCrm6qXHRL5gqT9aW15GIEkeEqpPHkXbTXp2qPYp-uwSEDTjF0LR0f1pmZ9NMPRyVPgY-OjoGHKPqc9O6Eb1e8-AXJp7E4SyXXOGg07TlxXbq-Ol1BApQZpB86i_GPSldyN7FGdXLMt35z0GR8a3hqhWtPmv96TdYL8Cqcp8Tt291IM1NS1f_LMJvTZvXSGIGrcL7B02b5IXmN1LB8f-z_aBxHVTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66301" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=LRD27iQcwagI-vj80f_65AuL19YecVfhI-8GnblvM8lA8SNSH3GkFb_sQGVL8yx0uvkW36IJPMnNesQ5ZeUPtifHUy5fvUtg_Ew6DvdWVjIRYQSXCPfNsbCOjso2ymC0OVYPjJIXkM0oQ4Uy0DWCw8AeGEA44pk4crTAOZrtWpTqYFqc4CDysn9NbTgIzwKXRAOwIhvaiUFla3vpyuz5kVWsAPM2JnNi7bA31ew9AspZ8vCuDQWC-6vDwXPMztgrc626egEFPKqygtGZuU9eX3CN93OZqkImci83IET93JssuD4WqYm7mxoJsA4TLONbE8tFd6FflaoMzA3vdg7R5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=LRD27iQcwagI-vj80f_65AuL19YecVfhI-8GnblvM8lA8SNSH3GkFb_sQGVL8yx0uvkW36IJPMnNesQ5ZeUPtifHUy5fvUtg_Ew6DvdWVjIRYQSXCPfNsbCOjso2ymC0OVYPjJIXkM0oQ4Uy0DWCw8AeGEA44pk4crTAOZrtWpTqYFqc4CDysn9NbTgIzwKXRAOwIhvaiUFla3vpyuz5kVWsAPM2JnNi7bA31ew9AspZ8vCuDQWC-6vDwXPMztgrc626egEFPKqygtGZuU9eX3CN93OZqkImci83IET93JssuD4WqYm7mxoJsA4TLONbE8tFd6FflaoMzA3vdg7R5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kk32wVPwSI1Z4oe-p9VxeHWWnCcviav_oNBqFOWL9Qr7huWwqjwNq74qtc-AH58GmSDv2bhm1-222JY1lxC5T55gWjGuIvxrO1F15Tc78rKwdrju2v9SMLUf6GNPVaWWewBQFL0Hquo7RwZ-yP4V7efIVclpj5vfzDB2CdkVxnl_FLx5qRvwQu9HLK064XHgl9wPe8cSjB8ZOqE8B14gQiDbS_vxgXJ8_wnpRuEEHiV1xzWRZQsneNdQgn9PuKaBi4pK_IGnMGZAy7c2GvzY9w8fIqQ96c55JhlwH1Ggq4BxADOaxgrsEjRhIfmf-7IrNO2wGoq4HnvedOk6MJy3bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R8JTXMNEMTKrqFgSwERlzMGjSUGOSyTIkQqty5tVPHjjsisCtDJVT1eADd5IwK5ffSk2cQH03LIEnbB2A2FeTTrx327PimAu37D6ZZCdP-oiFif_Xhrs55MHwPERLWvyQchXRo8uV_SmUJGg2BWDaxcA3mIj799dYytB7kUkrsinwkVv4aADhVyOfYftNwWXnVoY0jM3mRGPxO35wWnnUlqx0jzTCQaKmsNAc4t6mNnNc2jHDi7zSeWcj4fiOTipk3CegXgPbQ9m5GZ-wN1GXtUsOvH6PzdrQ4naT5CQmesazgWhpLIZzpFfPkLe7MfMVEsV9uW_HQ-JUchfypktMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SyHCsWqfM_LPinWpO9MDJY__5U-K4EDy6U-nlFouXlvU-jDWdlGq-IxU9lZko37RdXzZcB0vnrWi07WYDM3Ae3WDJ49A0dWjWio-OIi_PR4iNj3Qc2b80OaSFneIsubWNVroxW-RMTfWZRBJLR8wKXtocey1NI3yMrkJuFyJ6cIRWxcgOdGXzWYKMRpfAI5WQwWuAq4D9D1sCrJVffU8Y-LjjljqcFB2OT-AZ0XfRE3CtNfjUhFgrlpHukNyne0A2_G8FjQi6KWp5ZBo3kSqCcMJ_XUNsXejWWeuE4_ThAANJP2MpizZzezAYOg4Njpu42M3xnKdM-OCaRPv3N6zLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HcVKJKCd0Fkg5AoHGXjZHta8s004GUZDQOSSGYpQzgQA3znbkUCY8j-5xt1NNifrU5fv19gd1COTB34nfnphgY4Urf64RWdQPQ6F55ynROGXP68VXI12us43OQasuSquj0rmHfjgdhQGMpZPJ-3-KNQ0f-mM8UiaTbtfGUldL5kZhoRu95pnX5D3i1SZCQBrFSARxXbiFiD28Eemp9XjW5nQheJ8qhrcAt9rlyB6r84zMGkquadFH1rpT2JGqobLkF7KhwfeaY8S_I36ANjC-gi_x_vqL4TOz4zXX9HVgliF_E1SyHoyWLsSSn7JERvw_I07sB1f3KyDQumQjkHtiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=TaCphKNsMvYywzZCmVSN5GYxxykWjriLWqBM6Iv0rJSkSw8E43wqNDyfOo_DwYVh2P35fgpn3Jc15Cv4WqBsHeV7QD1upyl5BhMHeo2lHoCDev46Ihp8sSNK57vWccXPbbISrUylciM3CdLfNUou8hIPGlg-ZTLmF5iT4D-387xVy2_6FdZXgxxjOMjycW0gnV8sByE0JhGfOaM1ZHKo6jfjwkS9SHiKEuGQwsA8x3SpdAn5UYlHHJti2xU_iTFgPV2hxylchqz2m7BJ911pujxsZ8AMoX776lCy-W7mYi4LWMWGvxBDI8M5yFVDA6JgtteBcWloVcvv8VDh_eF1fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=TaCphKNsMvYywzZCmVSN5GYxxykWjriLWqBM6Iv0rJSkSw8E43wqNDyfOo_DwYVh2P35fgpn3Jc15Cv4WqBsHeV7QD1upyl5BhMHeo2lHoCDev46Ihp8sSNK57vWccXPbbISrUylciM3CdLfNUou8hIPGlg-ZTLmF5iT4D-387xVy2_6FdZXgxxjOMjycW0gnV8sByE0JhGfOaM1ZHKo6jfjwkS9SHiKEuGQwsA8x3SpdAn5UYlHHJti2xU_iTFgPV2hxylchqz2m7BJ911pujxsZ8AMoX776lCy-W7mYi4LWMWGvxBDI8M5yFVDA6JgtteBcWloVcvv8VDh_eF1fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66294">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">واقعا حق اسپانیا تو بازی اول خورده شد باید ۱۶ تا به کیپ ورد میزدن   @sammfoott</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66294" target="_blank">📅 15:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krJkWS_9kbifVDaTO3ch_ABGabi21PU-C_IeiYKtuKVckJotkXlJXnyiiCwyjNjTq9bqRUUvACEVcv5xgT3EaZkLfMzR5ZEbaBmMgXaoPGbdqJTf9RZn7k9WrgSY6bRgRsrtEktXfFiPeUVP_BB_dTuBlYqCvzn4mV9WFWHEqlknpeuJwVM2gGSSg3upw7HAsP9VFGVx1M-SQCRUJsc7H0-9SSczLjWlz-08IRv6EbRqyRwS-AMQNKOYa0GEeSJ8p-7ziKfMdh4qZw_FeVVntrGCgqP2NNWrsssJbyR-whXgS2lKVhftC-IKlFkd5zvZCTsISXBKYJNIhQFq_kYllQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=OcZHH0QREP2l0IGATmxl0vTBCIb9FIn_Qmum3hpuIWg0UMI7XNPmaDUsT9KIg_CrvxN2LgjwS8397UDBuSWEEg_5WuT6EssP4I6wA8lfKdkRrxn7cP7eomFzYTN-LBpjvtKUCL1RrgQXoAFFqGfDXUFYr7uC25wxJMnLK9Os3RJMT8wdTnYPCAgPW93clPOwQJxW3I1v9Cu9uzTitOdCed0RkT4xbnT-yzGnAO2UzHZ-kdhnAgTTL6jHmvxB9zn4Ej7QahyveY2z-sjm-UiuCm_DITy0FYzmHVCKQ8RE92zgnYp1JizbwL1GB2m4txAktVuHVItZHtrWsSe_Eb3F1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=OcZHH0QREP2l0IGATmxl0vTBCIb9FIn_Qmum3hpuIWg0UMI7XNPmaDUsT9KIg_CrvxN2LgjwS8397UDBuSWEEg_5WuT6EssP4I6wA8lfKdkRrxn7cP7eomFzYTN-LBpjvtKUCL1RrgQXoAFFqGfDXUFYr7uC25wxJMnLK9Os3RJMT8wdTnYPCAgPW93clPOwQJxW3I1v9Cu9uzTitOdCed0RkT4xbnT-yzGnAO2UzHZ-kdhnAgTTL6jHmvxB9zn4Ej7QahyveY2z-sjm-UiuCm_DITy0FYzmHVCKQ8RE92zgnYp1JizbwL1GB2m4txAktVuHVItZHtrWsSe_Eb3F1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=Z9FeiL3v9FHiWI4cspAMF948DS-WdwJBKI3Lteq6p_Q3-_mqA8dBwjuXI8Qb8KTezUTybpm0LjQFCZ83N_yIbpC1lweS_pRduO3wcOy3e2nxk_luqTYwGGfQSHBYGSGZ3eDqlIpd9xldix31CJKN47HicVoooBPElqJuuc-pfMvkExrc2h6cp5fl_8UJWyfXXAL1Y-7suWNbq2SpMvB8KFpjc2YNQVqvyYZK7U6qb69zVe1r-Y3SKE-TC2wcr09wjF2CW3WVB7-UkLX6AfL1Xcd0UeqWlsZV0fkv2cjSiWKXASxKbe4EKSJM7LtjHu3mZVb5NBQCjxdno-KPq8lWsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=Z9FeiL3v9FHiWI4cspAMF948DS-WdwJBKI3Lteq6p_Q3-_mqA8dBwjuXI8Qb8KTezUTybpm0LjQFCZ83N_yIbpC1lweS_pRduO3wcOy3e2nxk_luqTYwGGfQSHBYGSGZ3eDqlIpd9xldix31CJKN47HicVoooBPElqJuuc-pfMvkExrc2h6cp5fl_8UJWyfXXAL1Y-7suWNbq2SpMvB8KFpjc2YNQVqvyYZK7U6qb69zVe1r-Y3SKE-TC2wcr09wjF2CW3WVB7-UkLX6AfL1Xcd0UeqWlsZV0fkv2cjSiWKXASxKbe4EKSJM7LtjHu3mZVb5NBQCjxdno-KPq8lWsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=Yv_SYOE4buoXQrw1C1zvGRLfi_szjZ7ZNFvQZZrHI8wcLjDAk9MLvC9VaDecdctktd4UPaf3rw1EXs4PTyzks3EO8h_5Zm9IrFhAhyVJNRnqYh07dV10xN3SBLsPLZq67P1bqWXo25gseY5qXgXEGa0E5wWcKmkYvuBBLsbBPZTQD0e2VrO9CtSvp1a4vpQwARpkWQLkPholDfBI8_ZCAIEa725vQvMStzh84-dIZkTWbXC5jakY-nwjI-Wz7tTffuxnzty29bT1Fmsc8-ZVwI91klS-nzRqtywpgGa6Rc-nhPaSakU87gWvbo6-7ay74cVD_pMEaW2nNAd34anSbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=Yv_SYOE4buoXQrw1C1zvGRLfi_szjZ7ZNFvQZZrHI8wcLjDAk9MLvC9VaDecdctktd4UPaf3rw1EXs4PTyzks3EO8h_5Zm9IrFhAhyVJNRnqYh07dV10xN3SBLsPLZq67P1bqWXo25gseY5qXgXEGa0E5wWcKmkYvuBBLsbBPZTQD0e2VrO9CtSvp1a4vpQwARpkWQLkPholDfBI8_ZCAIEa725vQvMStzh84-dIZkTWbXC5jakY-nwjI-Wz7tTffuxnzty29bT1Fmsc8-ZVwI91klS-nzRqtywpgGa6Rc-nhPaSakU87gWvbo6-7ay74cVD_pMEaW2nNAd34anSbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=hvQdUZ6hCLCGbCi0FCjMZzmxc_CkrMrY7cXMLKF8h11Z7ptpw1rQ_fnkydm4xqk4TMGEUV3vfiUpt2zdgcRd53gVMYSJWrqkp81XrfAyoqWqWRGzozkdE0ajmyLZKRSbptGwjcDmodS6ETYTQcWSbM1Mb1mcFAOP58bX6kDAjIDpLtKFaMAJKcNe-d6izDCgjyGxC1mc_dIk3mYynUTOx5KMvo6uJEDZYG0uXWgnURGdiLSf-UbH22FiNerTYamhRew5Di7hTtxNwaqRPyqLDd0R4sINxBaIm89D1lcw2CIk99fZJvEmYUnoGrZzt_tPtg2I8TNk2JYwmmyK5c3N8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=hvQdUZ6hCLCGbCi0FCjMZzmxc_CkrMrY7cXMLKF8h11Z7ptpw1rQ_fnkydm4xqk4TMGEUV3vfiUpt2zdgcRd53gVMYSJWrqkp81XrfAyoqWqWRGzozkdE0ajmyLZKRSbptGwjcDmodS6ETYTQcWSbM1Mb1mcFAOP58bX6kDAjIDpLtKFaMAJKcNe-d6izDCgjyGxC1mc_dIk3mYynUTOx5KMvo6uJEDZYG0uXWgnURGdiLSf-UbH22FiNerTYamhRew5Di7hTtxNwaqRPyqLDd0R4sINxBaIm89D1lcw2CIk99fZJvEmYUnoGrZzt_tPtg2I8TNk2JYwmmyK5c3N8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=bqNmat2RcYY3800hhjCHDJjeOO8K-qQCogrhXhRTjsMxPdteBcnMyCuR9pzBK3tKEqN4u8vD80PsaD8GXw8CoUHnwqNczWU0uratQqUIcctEb2u8plDBhjqo1PmiKXZXAI3etGxXM70Xik1TOfIBw4Q0xNi7QCPK3gqgzm31i3-kGRb4ilytrUSATv_KXGGjF0bT_5RGoI_19CRvu9bak-3oNfWYZ1Dv_SPFWGxbk9U_IU3mYMev4vVmKO_HyQ4ZwNJSHZFO80iLVGlvEQ_p8XYV9fisTghrcSmQUmJ9D_x13RZgWUOdYbGZ71dJi1axIcXsCdXAVf1zPYOuS4yiEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=bqNmat2RcYY3800hhjCHDJjeOO8K-qQCogrhXhRTjsMxPdteBcnMyCuR9pzBK3tKEqN4u8vD80PsaD8GXw8CoUHnwqNczWU0uratQqUIcctEb2u8plDBhjqo1PmiKXZXAI3etGxXM70Xik1TOfIBw4Q0xNi7QCPK3gqgzm31i3-kGRb4ilytrUSATv_KXGGjF0bT_5RGoI_19CRvu9bak-3oNfWYZ1Dv_SPFWGxbk9U_IU3mYMev4vVmKO_HyQ4ZwNJSHZFO80iLVGlvEQ_p8XYV9fisTghrcSmQUmJ9D_x13RZgWUOdYbGZ71dJi1axIcXsCdXAVf1zPYOuS4yiEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=D9yZcEE31i4EO3JZrPBcAatbXtHA2OinyGjBNqKrjDRtAF5uNFINoDMQTf1dcmJcIZBqdXjq9OJVTdOwGDEnWEbcTEI5e8ei3AmFuJQgtyhTnq-RQ2SevXUQ12ZfIS6cFaFszn9LgNO20d2mWTYfr93s5rAwZKafZoFXuYe_oivw009ZW_fxu4wsHGE6P5pMtOVqDdyPppU6mkpAzLLNI0G21KDJoXtpahNG42mkBwisPQwv7E7aA3Sdz9U5t9MFJcobhCV3cVksXMbX2GXyohYWoL5i8I3i0FsX91DVIw1DOueKB3VTR7KvlQHNgqOltd-BRPOm0f36jioRUr1Yng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=D9yZcEE31i4EO3JZrPBcAatbXtHA2OinyGjBNqKrjDRtAF5uNFINoDMQTf1dcmJcIZBqdXjq9OJVTdOwGDEnWEbcTEI5e8ei3AmFuJQgtyhTnq-RQ2SevXUQ12ZfIS6cFaFszn9LgNO20d2mWTYfr93s5rAwZKafZoFXuYe_oivw009ZW_fxu4wsHGE6P5pMtOVqDdyPppU6mkpAzLLNI0G21KDJoXtpahNG42mkBwisPQwv7E7aA3Sdz9U5t9MFJcobhCV3cVksXMbX2GXyohYWoL5i8I3i0FsX91DVIw1DOueKB3VTR7KvlQHNgqOltd-BRPOm0f36jioRUr1Yng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66286">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=PaJmNTRt7UQvWGnYshvFTcogSAlix5fFZ-ySrylrwIVao5HmKvkJ8mN98JHk9RGGroMKoPb7SztHvPYfbaA6fA5mO9M47i6YvlkT-1LMaCKKnPb925YWA46iOu-PC3oWlPXNbZuJOpDJfbbbVJvcUbzR-T7x43ZgxNT2yiyGt67WuyWOZ_CA_COSUHwF9Y3-1dvP9lVnhbJtgEv14uz8eXo6doKJs6-HHACHtkRVPIT2pnMvO6CxPw6Z2fkokXliytWEfsz4Oi7_dmmhMbB99dup_0O6RcJ_vAV5RPSXXLKaAyQtGKKEjjSajj9_CJGAaT8XIrPX8yj5LgSI4talAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5225dce7ab.mp4?token=PaJmNTRt7UQvWGnYshvFTcogSAlix5fFZ-ySrylrwIVao5HmKvkJ8mN98JHk9RGGroMKoPb7SztHvPYfbaA6fA5mO9M47i6YvlkT-1LMaCKKnPb925YWA46iOu-PC3oWlPXNbZuJOpDJfbbbVJvcUbzR-T7x43ZgxNT2yiyGt67WuyWOZ_CA_COSUHwF9Y3-1dvP9lVnhbJtgEv14uz8eXo6doKJs6-HHACHtkRVPIT2pnMvO6CxPw6Z2fkokXliytWEfsz4Oi7_dmmhMbB99dup_0O6RcJ_vAV5RPSXXLKaAyQtGKKEjjSajj9_CJGAaT8XIrPX8yj5LgSI4talAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگن مجتبی تو LA رویت شده
😐
😐
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66286" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66284">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P_riWPuiUms2wTftB_Gr27L4wWK6ggukFEciRxT1AoW0ScTHLeymdwhZ0ybBbADBgEIpw1__UclPVByAcGO1bPRjlpF1yQ2JH4ragygaIZ869UFaOcDHdiOrRv95i4VPf_AtUMEH74S4WQU9-IX-jwm43SVKNJpQgw2K5LGffD6WDNixypOP1UFFFW67--Kqt-7ja4FBrqAeqDukVljfagvFyN0Uars2OFmRIIwbUVS7yRldl6_hs3YqrUDSpWVCD-JRH4Rs_KCmqm_pkc9g8QXIyPDgqHQ2o8VhG_c7rFYRgxAu2bd8stNSRqozaYH_tWXudajjAx1eEKOhD1ynwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_-uOMpFFD_d4z9Kvpe19Dl8FKJ6NNLrBeUL44DlTCkd3L2E8D3rtP4jiuJGbWHhpoFuXep_Tf_0D_GdGjj17Wwkfsi44GcQFk2D_lPd7sJE_cUFQ1ORWxuNgAXebRnE6BqB14KtSXKfynHyfAszKHaPkxyHRIXuUMSctzoAf7N1vZH2L1w_dNZbz3jrcjaFnmC1E7ox4te1-YI-GCWp060j0FpePpmpRIyckX6GBXPXs9nmDQ47AYiOywwxzyiPjhjP_qwg_mIFTq-zq6rEf2RPDNf_VjdaR5Nz722yOupppdjHqEahi99wU0pni7r5GBTtuw3P3eZbvL5Vo1H3rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
برنامه جدید امتحانات نهایی پایه های یازدهم و دوازدهم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66284" target="_blank">📅 13:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66283">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ:
من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
جنگ لبنان مسئله‌ی فرعی است و توافق هسته‌ای با ایران می‌تواند پابرجا بماند.
به اسرائیل گفتم حمله اش به بیروت برایم خوشایند نیست.
نتانیاهو اکنون باید در قبال لبنان مسئولیت‌پذیرتر باشد.من از نحوه برخورد اسرائیل با لبنان و حزب‌الله راضی نیستم.بدون من اسرائیل وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66283" target="_blank">📅 13:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66282">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
ترامپ:تلاش هایی برای تغییر رژیم در ایران وجود داشت اما موفق نشدند.
اگر ما برنامه جامع اقدام مشترک اوباما با ایران را لغو نمی‌کردیم، ممکن بود این کشور به سلاح هسته‌ای دست یابد.
ما می‌خواستیم برای گرفتن اورانیوم غنی‌شده به ایران برویم، اما این اتفاق نیفتاد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66282" target="_blank">📅 13:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66281">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
ترامپ:
توافق با ایران به مرحله دوم منتقل میشود.ما یک توافق منصفانه و خوب با ایران داریم، اما هیچ پولی در آنجا سرمایه‌گذاری نمی‌کنیم.
چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، تضمین این بود که ایران سلاح هسته‌ای نخواهد داشت.
چیزی که برای من مهم است این است که ایران به هیچ شکلی سلاح هسته‌ای نداشته باشد.
اگر ایران به دنبال سلاح هسته ای برود جهنم به روی او گشوده خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66281" target="_blank">📅 13:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66280">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=O3L5pxBo9GOYFMYHdab6GCLyFjOL8YkqR6FrUio9QkwYp-bDp6XD7uKy8HYdfPv3au5y7lXnkzbJuwKneXmLp35UFKRkKn1z4ymDf-h_pbX4HLs3up1LK4avOgnsbrJLff0TVWixTHZU84J26cSYrZLVZ5LgsNDPC7MHTWXgnQq0xXDw3vcVc4lIuXmzlwREYN02UEiOH7OcZmS5fZx2IDeT0sfxanbS1nnP9BVizoYdMVVqpa4yq2-u9XybSZZebs10-0qQF-5mZekv2ujki8UKGyRsNJ6I8VyzUKYJubCwQfft4X6pzAghxYuabcq0LuSXmHK7CPQHmcmkYQArBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b4a7171c.mp4?token=O3L5pxBo9GOYFMYHdab6GCLyFjOL8YkqR6FrUio9QkwYp-bDp6XD7uKy8HYdfPv3au5y7lXnkzbJuwKneXmLp35UFKRkKn1z4ymDf-h_pbX4HLs3up1LK4avOgnsbrJLff0TVWixTHZU84J26cSYrZLVZ5LgsNDPC7MHTWXgnQq0xXDw3vcVc4lIuXmzlwREYN02UEiOH7OcZmS5fZx2IDeT0sfxanbS1nnP9BVizoYdMVVqpa4yq2-u9XybSZZebs10-0qQF-5mZekv2ujki8UKGyRsNJ6I8VyzUKYJubCwQfft4X6pzAghxYuabcq0LuSXmHK7CPQHmcmkYQArBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هادی هوتیت، خبرنگار  پرس تی‌وی، وارد منطقه‌ای در جنوب لبنان شد که نیروهای ارتش اسرائیل هنوز در آنجا مشغول عملیات هستند. فیلم نشان می‌دهد که او در جریان این حادثه مورد اصابت ترکش قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66280" target="_blank">📅 13:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66279">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b685347f.mp4?token=ABxH_SXq2iBlolLzxaYN7HsgU0uOZj-jlJbhmCrd-Os1mJQ3rqYIjWlaW1xl9Of7p4sjJnb3-BBuAlkHlZrSmQU1Ev9nHc9f1gASY1ICC0hzxASu-IkgT1Z5wIChSzEGa-vz5WytzCeNDj-ofXbGaaEJ90r-40JiY3A-jOW2fiBLQ8Cb0cgSa7EdM_Ob8Q-263kdEPhsFTr_t9fXDOc71Pg3RnMEjaIBuE4xqdFutODog3Kd0KvpkcLl8Dcj1m9pxYNnfvz6Cq-eDSTpZdtmKPbAc_YXMxh2iOBB5tfRRqdPTIRP40vxWtbZlYXKPmZow96cQij8H-FjCZZf5GBYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b685347f.mp4?token=ABxH_SXq2iBlolLzxaYN7HsgU0uOZj-jlJbhmCrd-Os1mJQ3rqYIjWlaW1xl9Of7p4sjJnb3-BBuAlkHlZrSmQU1Ev9nHc9f1gASY1ICC0hzxASu-IkgT1Z5wIChSzEGa-vz5WytzCeNDj-ofXbGaaEJ90r-40JiY3A-jOW2fiBLQ8Cb0cgSa7EdM_Ob8Q-263kdEPhsFTr_t9fXDOc71Pg3RnMEjaIBuE4xqdFutODog3Kd0KvpkcLl8Dcj1m9pxYNnfvz6Cq-eDSTpZdtmKPbAc_YXMxh2iOBB5tfRRqdPTIRP40vxWtbZlYXKPmZow96cQij8H-FjCZZf5GBYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمدرضا شاه پهلوی مردی بود که دستش نمک نداشت
👑
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66279" target="_blank">📅 12:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66278">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
عراقچی:
ما واشنگتن و اسرائیل را یک طرف این یادداشت تفاهم می‌دانیم، در حالی که ایران و حزب‌الله طرف دیگر را نمایندگی می‌کنند.
پایان جنگ در لبنان بخش جدایی‌ناپذیر پایان جنگ در ایران است و شامل خروج اسرائیل از خاک لبنان نیز می‌شود.
هرگونه حمله نظامی اسرائیل به لبنان و ادامه اشغال، نقض تفاهم‌نامه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66278" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66277">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=NxN7LAXYx1szqG5Tws8I6A1Np-RBVtgtaau2jJgopTXd5coWKfb-g-T2QlCH4fybXspIDgojurnmLrVf8JyoCsDX_oYVu4SYNRWjzmdE07wMVRB5kbcZPw84CUdbTdHdFxp0TqRSfliKS1A6ZO-GoTL3hC6yHnuVxLO-7nzYf-mhLKxEMAcaQyUa6pIe9jEhq2DbIp19Ge2U0PCD07jiG0GPt_kHC0kLHOLE2FfMHvPJ3njuQ7fi_VkH-zpyNY_NrVOoILq0DydX8PfxMGpnon3coRbzbyJ-0O-l1cnsRS6QR9VelPi4g31b9rn8gd60K9Z3SAl9VZN_XVOK54KERQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d988cc6faa.mp4?token=NxN7LAXYx1szqG5Tws8I6A1Np-RBVtgtaau2jJgopTXd5coWKfb-g-T2QlCH4fybXspIDgojurnmLrVf8JyoCsDX_oYVu4SYNRWjzmdE07wMVRB5kbcZPw84CUdbTdHdFxp0TqRSfliKS1A6ZO-GoTL3hC6yHnuVxLO-7nzYf-mhLKxEMAcaQyUa6pIe9jEhq2DbIp19Ge2U0PCD07jiG0GPt_kHC0kLHOLE2FfMHvPJ3njuQ7fi_VkH-zpyNY_NrVOoILq0DydX8PfxMGpnon3coRbzbyJ-0O-l1cnsRS6QR9VelPi4g31b9rn8gd60K9Z3SAl9VZN_XVOK54KERQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ایرانیان وطن پرست سنگ تموم گذاشتن و اینقد پرچم شیروخورشید زیاد بوده که میساکی فشاری شده و پرچم جمهوری اسلامی نشون میده میگه این پرچم ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66277" target="_blank">📅 11:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66276">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=facs8gjRpvrxMAqYEPXdTUNxGG-PBJ4CtOGOOrNUx-NuyppmWahdllbFKw5rj_47zhiGRA2TOLJhJbxA44iAoYAB_LmOq9l64-8rXg0Sqv0V-Ll2dQJnFwguDz2vy5E3mW_EjXQRxz3Zp9JzkyBXrb8nE55fYRg5O07rcVrycMWkEE08xjRlAxB8meu_TtV3KcTxS8tzPAwMHaAdsvsrij7jiKIDOmRI7KRe7I6q1xOchkXPnr0IaIVkZvRsI789kJnql-LbGqDeqF8NOot3xMrzgVybejFspYwoQs7CQ8JuQW2Up9Xguo8cDOX8ckyjUQZwbg7RKY0ziEfLd0FA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944350c2ea.mp4?token=facs8gjRpvrxMAqYEPXdTUNxGG-PBJ4CtOGOOrNUx-NuyppmWahdllbFKw5rj_47zhiGRA2TOLJhJbxA44iAoYAB_LmOq9l64-8rXg0Sqv0V-Ll2dQJnFwguDz2vy5E3mW_EjXQRxz3Zp9JzkyBXrb8nE55fYRg5O07rcVrycMWkEE08xjRlAxB8meu_TtV3KcTxS8tzPAwMHaAdsvsrij7jiKIDOmRI7KRe7I6q1xOchkXPnr0IaIVkZvRsI789kJnql-LbGqDeqF8NOot3xMrzgVybejFspYwoQs7CQ8JuQW2Up9Xguo8cDOX8ckyjUQZwbg7RKY0ziEfLd0FA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دلیل سود نکردن من تو بازار بعد چندسال
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66276" target="_blank">📅 10:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66275">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78c971246f.mp4?token=slBpRzkS8jIiU4crylXf-jy_3Kl4lDG6WY9ZtzSBwOuRBe3H50Rts9kZY7B5dQy3JAXwMpBDyn9koEG8dn5hGdsbTa36EPs1MCT2hawxGyL460MJXukJ_NIGEiIuH9hMzhAfvQh8O_Vp0Y_1YrsueLhXMfZvnypSg1d0b1DkKudUgMnYI47vFGm14W_06A093GesD99DgbTE2AKBk8PIA2yTqh9uwUd4ZwvtRiaBW7_OnvmHuDbccMaIq4nD81Fmhkpt8fLDXpSaLQgKzNxBVAxA6zn0kww5O41wjvzu9KXiSrjb9PbopjtxhPxGJJk7BrCx_cJV1Sz89gr-wMCyUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78c971246f.mp4?token=slBpRzkS8jIiU4crylXf-jy_3Kl4lDG6WY9ZtzSBwOuRBe3H50Rts9kZY7B5dQy3JAXwMpBDyn9koEG8dn5hGdsbTa36EPs1MCT2hawxGyL460MJXukJ_NIGEiIuH9hMzhAfvQh8O_Vp0Y_1YrsueLhXMfZvnypSg1d0b1DkKudUgMnYI47vFGm14W_06A093GesD99DgbTE2AKBk8PIA2yTqh9uwUd4ZwvtRiaBW7_OnvmHuDbccMaIq4nD81Fmhkpt8fLDXpSaLQgKzNxBVAxA6zn0kww5O41wjvzu9KXiSrjb9PbopjtxhPxGJJk7BrCx_cJV1Sz89gr-wMCyUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از پالایشگاهی در حومه مسکو که در اثر حمله پهبادی اوکراین دچار آتش سوزی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66275" target="_blank">📅 10:05 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66274">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=RR7Wtj6f1XETI_1yZ6QLuhPgQldwuYlRfpV7b5py6m8V6D7qrkup3iqho5tj0GqXTuOxpum2SyIi3muwlPcv4f0GcBynDZmuU_ZVFJaIhxYaJXmLEvUAPrWeblfS6GWpt28UqLWIN3Lu3Ndu5-67-MdSRgQ_AtyL6NaGWtjXfvF51GghkLWQzu_PjFwgc7rXcwbIYLqBBtcwd3iefWH6CSDa0OStN86qMi4QC8F3iB9rdf5LwhYQ7SJNF8KUqlRAdllxb9UwOSLCxdJOTZsfhvShuQ2odoH8RUU_SA8P1ms59Czxv9EWCu17gFH2iB4ni-KYJkkQ5Hj2Ul-vzLYy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696afa1a70.mp4?token=RR7Wtj6f1XETI_1yZ6QLuhPgQldwuYlRfpV7b5py6m8V6D7qrkup3iqho5tj0GqXTuOxpum2SyIi3muwlPcv4f0GcBynDZmuU_ZVFJaIhxYaJXmLEvUAPrWeblfS6GWpt28UqLWIN3Lu3Ndu5-67-MdSRgQ_AtyL6NaGWtjXfvF51GghkLWQzu_PjFwgc7rXcwbIYLqBBtcwd3iefWH6CSDa0OStN86qMi4QC8F3iB9rdf5LwhYQ7SJNF8KUqlRAdllxb9UwOSLCxdJOTZsfhvShuQ2odoH8RUU_SA8P1ms59Czxv9EWCu17gFH2iB4ni-KYJkkQ5Hj2Ul-vzLYy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هو کردن هوادارن حاضر در ورزشگاه هنگام پخش شدن سرود تیم جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66274" target="_blank">📅 09:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66273">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=VthrXYYm4c8KL9cURglttQO1GJ_BJr0xh1M9SSkVZ4_cSNOq0M0D0SCZompObvP3Ax30E6b9KS2wS1E3RqOsnkzmPUbziDVaX0gJR30pVvURqldIow70uDlzOp4QScdB0l1nYpGvxKtQvsUJKzY1bHjNjZbuuN03zl6QWfh_47SWTJcB3q1SG18BEbZpb3QSwjVrWOObldiu2XUxvNdh_5gFvYknC6_-rrB_ts6CypFypVghes39URG77H3E7lvAOJRFTE2x92LKr37J4S921O-NbYHZfo0wLReJnUTSmLH5JZ0bQ_TUvbN3R_lc1kOw99Acv-ZJeOLVlyEhFYAznQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f96ea995.mp4?token=VthrXYYm4c8KL9cURglttQO1GJ_BJr0xh1M9SSkVZ4_cSNOq0M0D0SCZompObvP3Ax30E6b9KS2wS1E3RqOsnkzmPUbziDVaX0gJR30pVvURqldIow70uDlzOp4QScdB0l1nYpGvxKtQvsUJKzY1bHjNjZbuuN03zl6QWfh_47SWTJcB3q1SG18BEbZpb3QSwjVrWOObldiu2XUxvNdh_5gFvYknC6_-rrB_ts6CypFypVghes39URG77H3E7lvAOJRFTE2x92LKr37J4S921O-NbYHZfo0wLReJnUTSmLH5JZ0bQ_TUvbN3R_lc1kOw99Acv-ZJeOLVlyEhFYAznQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ثابتی نماینده مجلس:
عراقچی نوچه و اراذل اوباش آمریکا در کشور است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66273" target="_blank">📅 09:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66272">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNfXSISjbc7xZFCoDCDsCdONXHksYTXjQ1nA8GXqzyifboJAotCmNJ7WbE6ENEhG3n8j4Cy_FPZxuAJsQw06W1ngVE3cEv5ZQXkMMTFQhN01-sEOWPYjhDRYPW3Pu9WCmCLiTc14QgW1ViTxSfFVkgKlXCISt5tzSI8yvvHUHIeHe1_liLCXkzbyeA8NJq0-Acgr5uoT8H-rsu0o28ZtGu4OrkTzLGh3jZ-Uc00sAEp6Livq_m9VmoxxP_B3Jz4H7046XIw-7aI9lKg50d1lqiWWMUC8Zp7Yl3MbPywkhBS2TD3Exkzec81XfPPdtiZUuvZNYp-qQrqWuvwqh0Igew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
پایان‌بازی
🇳🇿
نیوزیلند
😀
-
😀
ایران
🇮🇷
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66272" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66266">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گل دوم محبی
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66266" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66263">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇳🇿
گل‌دوم نیوزیلند به منتخب ایران دقیقه ۵۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66263" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66258">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
سخنگوی قرارگاه خاتم‌الانبیا: گل زدن نیوزلند به ایران قطعا بی پاسخ نخواهد ماند
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66258" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66257">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پایان نیمه اول
فرزندان برحق وینتون روفرو ۱
کاکولد های گروهبان قندلی ۱
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66257" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه حسی بم‌ می‌گه بازی مساوی تموم می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66255" target="_blank">📅 05:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🏆
گل‌تساوی توسط رامین‌رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66254" target="_blank">📅 05:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66251">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/La3-TYQv1IFuzyGc-jAdlzijJKt7lXYyEkHCNY5y8-J49igpoA7uF_F9ZF5w2kdidIHpMsnEqHYFL3KXNm224AQA1yGhYzGMZnG8cIy2gt7A9Hj3yzE1w9T23g3EkRVMfKH1enzJ6U7bkhCawg5BO63jRLWV1MpR1GMum3W2A4ZSr7o_DcakH_2nlZS7t_plqPo6tEUULpGyNNKBr8OBxtFCjwKxpb4ArzQJbjeJhlo098SdQoitQfoWvvmz22bIMPsK5L5p40Kt5AV6CmpJrW_vrUzUVb5MP36RIdubbGmmYvqp7HZf0LIqi24skoKtK7UFqY0LQ6JxEV26U1i-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظه بازگشایی تنگه بیرانوند
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/66251" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66248">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇳🇿
گل‌اول نیوزیلند به منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66248" target="_blank">📅 04:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-poll">
<h4>📊 دوست دارین کدوم تیم ببره؟</h4>
<ul>
<li>✓ تیم منتخب امیرقلعه‌نویی🇮🇷</li>
<li>✓ تیم ملی نیوزلند🇳🇿</li>
</ul>
</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66244" target="_blank">📅 04:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66243">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QScL15EZ4qtzTazp7KzuK3S8Rxg6g-NVHC3I129_Uno4eUJBPyhhGDTW8jYEKPpPCuAoEqmXbw1WglnDnBdlzNWFvHJytG2HTyUnkiJiFRSJCucmbWXbJsZSB544GUtW1m9GfY6n51f4YifAzGDGNjYXVbnWSAhbif7irMsuROdO3vn5klWoVAU4h781eZKffgQF5ADJivesD4-mAk9Dl0Uojc0pUJWudpua9PxJ6aNE7YZORqRdT75kqn_SgQSBnhBLP4V0rPwya4awobfdeKB8t5FZA0QyoUvnuyMHtbDy5HvVpWJquHbQCreEHgmJ2JbQIO_2GUvqgkoFQfpCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل بازی
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66243" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66242">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66242" target="_blank">📅 03:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66241">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein ؛)</strong></div>
<div class="tg-text">حاج علی یکمی تحلیل کن</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66241" target="_blank">📅 03:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66240">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66240" target="_blank">📅 03:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66239">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66239" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66238">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GIMO-A5sosHN64z0PLJluDiBges0ylAl8vqpVkaV8UQNt48tBjwLApqp16j77LcACTMFIvqaAi7rfFUHDQahbGjALTms1B_PFo0AOKB7yYOw0WoekGYZ38BQtJdc-ckMiTwggqZz6E8x2A8541_UNoesLSZ5b4dOPX94vttkJrseqZrIg1JvwYW9wbfDzVgQwAl6AzUJVo-VKqsP0XOHRqIZhYwMaX3MSPRYKoafPJAgNwFbJgRWqX9AbxaSMGUDQVM5xSCMryC2hdQPDdNRVBjDt0xvrqJhIIkMwuQAb9wqBhVawP6466vVaA2KuvRH3CmllLw32O1vqYHsapZu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
👌
تصویر تراز امشب:
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66238" target="_blank">📅 03:21 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66237">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
صحبت‌های ایرانیان مقیم آمریکا قبل ورود به استادیوم
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66237" target="_blank">📅 03:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66236">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZEvAMalyg7po1ergvrb9ZVF-UQ28S4pnrzbrvR7auijJNhSiomq4jcTEmIuwg8Tt9E6Uhxwlq2CsoQba4bvZeSgNqV_fCUaBEXZ1QZ-Jn9zW5Eja_KMTiRGwuCZEKzd9EFeJ0VU1EFIGwM4WYyOpcJ7QlkIvsC0ORvLUGks7bwLUHAFfLzwaWkvzZ6zNToLyfF7eGc08iu4JTYQ0C2z_IE3dMdMDte-Pf5C6bSjke1-KmjZQX_S-pHIFcwCjILjQ4xKPd6Nxr_yp7taMMelK2JxcQNq-f3bY98fzr5iCQa5yiJbD3jm1Bknk8_ZXRofu0u25atK0t9S_7GAzaqDOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66236" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=OFkEC07-H__h1pAxIos6BMR4fBxNhMh0rX9sUOscu2a3ctQimYeMAOG3Du1dtBlqFqIwQxQbkw82mIhKPUfsDsbd_50uqnSNhL0nMJjzrlb98FnpqCEYeHLQ16--_HVVllKM-ek067gmKgJRlXqnbWe3xTQzNAK9yvEfhciWaLLKREraKz121YbIl8UmU_R-9E3B9AM4CshbHXqq27CyNokCR0oa9IMmzS35Q3uL4uKrYa9mq0msKEjoMA50y76iqlfKYCoHOHiFPoGdWERQq7npkXQEeLnIKvTd-h2YCZyCC2P3JUsX8-S-mE8zh8FadIZu6s8vsZiXZ_r7nzKpeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c366b2c0bb.mp4?token=OFkEC07-H__h1pAxIos6BMR4fBxNhMh0rX9sUOscu2a3ctQimYeMAOG3Du1dtBlqFqIwQxQbkw82mIhKPUfsDsbd_50uqnSNhL0nMJjzrlb98FnpqCEYeHLQ16--_HVVllKM-ek067gmKgJRlXqnbWe3xTQzNAK9yvEfhciWaLLKREraKz121YbIl8UmU_R-9E3B9AM4CshbHXqq27CyNokCR0oa9IMmzS35Q3uL4uKrYa9mq0msKEjoMA50y76iqlfKYCoHOHiFPoGdWERQq7npkXQEeLnIKvTd-h2YCZyCC2P3JUsX8-S-mE8zh8FadIZu6s8vsZiXZ_r7nzKpeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
تجمع هموطنان خارج از کشور مقابل ورزشگاه محل بازی تیم جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66234" target="_blank">📅 02:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8_NoxtjJJmuezakRNtyhnlQpVYKGfJqBlRQ7yxsFvwDMO7SiZN6ke2PH49xVuRW3AtyuYR8xEkVuKBnEHsLWAydOZRlfuglkvND41hwV2BJIszch2VldL2Zj59RdXtMIW8qx1KWayCjgLY6_GepQ5eXVNhUnwT2ppotX1ooLobcSrffyHn6MurNqoHLKa0dBIPeyFdSeLailNy8mWRk22zU0glX4w3QZ_k_FS4ux_z24A_w6HyBX-QgpGizzgjX_z0Ui3RYT2Sys6dmq-RdR-NEiT6AK3jjAYHL8ZcPN5g8b4eKW_IMRwdsuZ47nwgb5bLT1oyiZ0TjuBHfi8IEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی از اسمش مشخصه، باید برای ملت باشه، من نمی‌تونم رو این تیم، پسوند ملی بزارم، یه مشت آدم منفعت‌طلب جیر‌ه‌خورن که برای ۱۰ دلار بیشتر ناموسشونم در اختیار ج.ا می‌زارن همونطور که تو ۲۰۲۲ وقتی مردم داشتن کشته می‌شدن اینا دنبال حواله خودرو بودن.  آخرین باری…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66232" target="_blank">📅 02:57 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
