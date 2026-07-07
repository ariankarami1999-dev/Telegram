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
<img src="https://cdn5.telesco.pe/file/MmVNw1imC60hETuqpU757ZhlgTDiyd4iDODdNCq437amDmWYoU4nYDbrBjItlj9HWvXutnlx_HylkupMIsL0Cy3CFqsDQJK95s4VW9Qt36QbklsNp3-2x2D0JfGFjcCEI00jArdJe6sQ88QUx7YWF1hTeh7K9EmpiQSONaE-JJXVY8_n3lPubkuVXp7CbZwrfjR-aTSrClHUmldCMQmw0F80gHgbC6a934Vfv2nQyxxMtm-eclCunApE4ygWWJ04Njun1JpZMNIFYO4Y8TupHfjshe4qDO-Gf67aK3_fYrwC6Z32M8zlgQ5eZwwrzLkltHofrIzw-EnRtLnltfvD3Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 621K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-98777">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09d155e75a.mp4?token=TBESBV10AT_DL3RykQThCyCq5W2UVB84QMR7iFwwhdTIFqxfHOAYAbNohJ2YTk4nG5GSvhlFrAkrE2iUx_YYz4fPZVLZK4zGL1dGBQiqL6x-9hbbpuEbIVzcs0EIr3gIHDy4h3T_KKJmRisFKg99yd7-VRcbaru_dooyvpo6qkfak7dfnAlwdyylri-5MOByRuoYIkAG1XfJZ98SrDO876tN4yiMRnrAsKIu3orTKRxxLeH7G4tXVHHQVKF0Z0vah1YJ5V-p7xF46-wj84gN9uAk2nzg40B8WoV4CXi6w7-FsU5HdCBZXFBVpmI--NEbEApNvS4pT_rF6guzi-BHZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09d155e75a.mp4?token=TBESBV10AT_DL3RykQThCyCq5W2UVB84QMR7iFwwhdTIFqxfHOAYAbNohJ2YTk4nG5GSvhlFrAkrE2iUx_YYz4fPZVLZK4zGL1dGBQiqL6x-9hbbpuEbIVzcs0EIr3gIHDy4h3T_KKJmRisFKg99yd7-VRcbaru_dooyvpo6qkfak7dfnAlwdyylri-5MOByRuoYIkAG1XfJZ98SrDO876tN4yiMRnrAsKIu3orTKRxxLeH7G4tXVHHQVKF0Z0vah1YJ5V-p7xF46-wj84gN9uAk2nzg40B8WoV4CXi6w7-FsU5HdCBZXFBVpmI--NEbEApNvS4pT_rF6guzi-BHZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
رویای‌علیرضا فغانی: قضاوت فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/98777" target="_blank">📅 14:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98776">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca02eb2095.mp4?token=pe8fAv_7LUXq1QQ1BLMSXbAflcG1R_QrKdDhmdsJopXosTEWVJkB8Hx1LuwfsKeDjazeCu-aQ0dTO3CDvRjernwzXuy0Zz4Mznjbq0fWyKcJBRLUBXzE04l0EYGoT42_9q_n61zWjIQVGdGcmdYj7t5hHA5Itco9qDGAA7ZCtGgfDZhUIVMUk4riXmldrxIptrm07ZFyFX1hWqT90sJNVKYDOh3jH94HDrl-qIkTUmZver6B8XhgsGjEOsA5HDMzXuKVOXNZ30vqKgzgtlVN_auKrGPNw9_DhrBMEljpJQdtwawabTHxuM8yISaxrrzYTJeKgtkG7ZJz7h3JTuBCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca02eb2095.mp4?token=pe8fAv_7LUXq1QQ1BLMSXbAflcG1R_QrKdDhmdsJopXosTEWVJkB8Hx1LuwfsKeDjazeCu-aQ0dTO3CDvRjernwzXuy0Zz4Mznjbq0fWyKcJBRLUBXzE04l0EYGoT42_9q_n61zWjIQVGdGcmdYj7t5hHA5Itco9qDGAA7ZCtGgfDZhUIVMUk4riXmldrxIptrm07ZFyFX1hWqT90sJNVKYDOh3jH94HDrl-qIkTUmZver6B8XhgsGjEOsA5HDMzXuKVOXNZ30vqKgzgtlVN_auKrGPNw9_DhrBMEljpJQdtwawabTHxuM8yISaxrrzYTJeKgtkG7ZJz7h3JTuBCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇪🇬
آماده‌سازی ورزشگاه بازی مصر و آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/98776" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98773">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_kYQq4Ho84F-SnVIIL73uwwpdRTXu3bmqOciu9sveLft2cKrE-jHmZMQZRK9NRfdrNtHUDwOmuxygyZnZvKGv3py86MKz4nyCcBXWidTRrPxyLctp3iM-BRfZf71u_AE5iju18mTMpTnbRAoAVy7a0QxSqIepShDEroSD4jfCNjn_iCm4FcIKB1yplaHCmOnl0_M4uQ2pHTM1qd_98ifefax92jk41RsQSxPfAqeC8H51nenorSurg1QFROKwDyQYf-NEelrbtPI71nypgtigtevVkYt9IQihxce8J0lENwxR0BO2M9jLxBkeocC_iUjZTaSosqdSuMmUjthCi8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXwdO4ynZI2Qpn-JZcmD2wPSYopTKxQKFAtrHgv9h_w3Po15dM_F66n4jrhjjzng4Iv2hrBgEgGTmU9XySEJpcgJB-0iqKpzHcmISjjjbphfJMM4pxsr_pQXeA8Jbw_uRYstfg3euLSpLCGSx9Hlrve8l8uP7nO1Q4IRuejpYVahY9C6X6Lef8ziSfVdh-2qsuzFetiKBUBc41AONuk1-c4dLHif_ikgbKruaJ2Csw8n8tvO0oGX0VTHK6b7ff2coypq_YPrU10UwJmllTetYPLql3hNbw3xaZuBXYhq_-Pr4ExlrXx3d477DkKAus_OV_2hK4GM-bzSHMPmUeDuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utl_IU7n7F5r79p1VcouvflAzfDkelz62RbDzlq-O-IwX7vntweCt-JsRAAgVSopi_LO7FVCGv66Fn3Vs_1ucxN2rXsgApk8tPyaxDnwTPXoQElFPXyjrTrpP6Ak51eB8g4QSAe3U4qm6qjiTimB49Xcru72QMDxy2Rcv8gEQZpua439EE3Vv9S3rzuBGy8nTG7geKt1yatOIG9lBy_scplX-vHue7ge3oMPW67Ui-D2LXKyDtHO1MGyP-jumQ81L8LUb4-p4PCFsSGSBxAIyj8bDDDgEGeNlxVjy7QndXwcCEXrCaJFkw3PGpURrDQ2fg6fHCByhi5pXrKxISh-mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
💥
دوس‌دختر ژائو نوس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/Futball180TV/98773" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98772">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jtc78GXfYb_IAGwc7N8JDa9UZOa-5mEcpQOipixSr37CRNzeG3Zj1MybtKBCsw5YXpjTxUAHLptyA1q1nWR3PpgExW30u0pBlavnNLFS2nDNmBxacMAHoFIg9uRn7fw0uWVJGeXCnjMPtUoyNFpCwRIYpZB1034O-gwgf1RGOfUnVf869Dq56EdA3rGVgHHd-zV5vRmovL-biUC18uglmoKQHsb7GlLJZeohQygFO0jPV5lQmXrD4H04BHH5UZfLoTX4nyb-W1jpSbvCWViCFiOtiO9lGQuEWv1vD_Vc6TIOFGq-_Cu-S-OomHjsNFoi1uNtCdYiUjnNKpQdmubWbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق
🫠
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/98772" target="_blank">📅 14:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98771">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9e2f1596.mp4?token=H7C7d7bouV94cjyNuYIR_MyxRSfmvigI5LVqHZ0t_8QRcwg5eR8xy57CIjDeRVOAec5viMr3B20WDI2cshGuWZNHLraionF5qKt9KXM9T2DhCJ-LdkRndsgJIUo62rwUjHQ_aH1HnPN9XhO3Or2wm0mlaaBggVmJeszpy8L-n8f8PcB_Z7J7LVhcECgI80USD3oNxkiECE7jmPWSCENmvk7GzNl5dZcfaHpKiOBxqxlTIYdmqNm9ZxyZQaVMN_w850Za9rGvsAJFxYImzXzmU2ogk_tnSLiniAEDfT2gUEnSzqLYgr45oT4O3SrseSaBR5TN9RrERrxGY0IAwn8MyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9e2f1596.mp4?token=H7C7d7bouV94cjyNuYIR_MyxRSfmvigI5LVqHZ0t_8QRcwg5eR8xy57CIjDeRVOAec5viMr3B20WDI2cshGuWZNHLraionF5qKt9KXM9T2DhCJ-LdkRndsgJIUo62rwUjHQ_aH1HnPN9XhO3Or2wm0mlaaBggVmJeszpy8L-n8f8PcB_Z7J7LVhcECgI80USD3oNxkiECE7jmPWSCENmvk7GzNl5dZcfaHpKiOBxqxlTIYdmqNm9ZxyZQaVMN_w850Za9rGvsAJFxYImzXzmU2ogk_tnSLiniAEDfT2gUEnSzqLYgr45oT4O3SrseSaBR5TN9RrERrxGY0IAwn8MyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
🤣
🤣
💸
💸
وضعیت دیشب اهل دلا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/Futball180TV/98771" target="_blank">📅 14:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98770">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2lkJParYxFRaDzCk3yXTlm_l9GHPFv-9HWUtgIQBqdeDAiKkeAp2ynA5gM360El43mKdd_Iumaj75p1dVuNPdk5KxQgBf2EYmgGUUUszCz2QFCzwPpS5jNpAdHm3ZLFme0g2WmniPJN_vpHgAyxehrAPJHorYSKpUa4MxxJwIkiAhS5tv7zCMx3ef9bQvILLMbKwB0ZH6Qq7Z65AeAlKR_xJtCUBOxfdTt04qCcEUhlw_0v7kTbw3al-hnrnUTfeON1Qllfr-fLfx_WoC4_kBdqFzCGxXctuwkrQ3jTCzGBGRHpp7PhiaYNXGbDw7otL7mDxwu2oio1oN5TNIhs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
آمار لیونل‌مسی، در بازی‌های مرحله حذفی رقابت‌های جام جهانی:
• 13 مسابقه.
• 6 گل.
⚽️
• 6 پاس گل.
🔴
• 12 مشارکت.
🔥
• بیشترین مشارکت در گلزنی در تاریخ بازی‌های حذفی جام جهانی.
🇦🇷
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/98770" target="_blank">📅 13:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98769">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_8IqI8HA-dJIqmhLqpN3wv5WD4FmwVQBGi73aVqbSEoBL7GWsmjE37IR0nfcB_Pe_XhZrvuAm0-5pDCUSdbBxdZdbVfljNO9o5Gzhf4V9HN5y6DxkMvrspcRPrvCpUZeH2PwagLQKNs8EfO1b1JSWHOfvoqcE6IVokzxL7gM4JsvqjxdzShyO5weFrbkmz8sDQXuecLxuuWNlvxIubALV6uXHDXHrVMHkSchLGxmZANbOMvrMXy_88XLFM5jwi2J_GmydWJkJ3wq2jZBCspQFKYAtRr62uZIb3ygbaXcDfL-2pSxjJtWY4BvrZOfgtQoejAtVVJph-QyCBVe1rtQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری
؛ باشگاه بارسلونا در آستانه تکمیل قرارداد ژائو کانسلو با پرداخت ۱۰ میلیون یورو به تیم فوتبال الهلال عربستان قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/98769" target="_blank">📅 13:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98768">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3126b51523.mp4?token=eKWOkYKU6ypgxg1ghJgQcoND9fOqWln8sIMHS9zq1F4igAhjm22R8t08KoKyalbcr6Y-rh0qT-jyz4ztj3BULIw_-9wxCnlujSvhvHxRBAY9PTlv8JVphg-kyZT2Hc9mWm4Jv9ZMN52RxI7mo90ya5yIuQdKIUovTF7EpiXnVIsomSHaglzrUXJGwKzYs1_fmA4EVr_ecU7_kLYEu_mLDDsqdqv5IJKrPQR3KpgWBP653hLHsok4e_Ih4GMoellkfGoo3VtozuCrs3-7YtbamaikS7YcyYNYIok86DPdvH3zGXo1yEEtYlnNvtX1WT-SO0Zi_nPIRdiNefVcjrp-Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3126b51523.mp4?token=eKWOkYKU6ypgxg1ghJgQcoND9fOqWln8sIMHS9zq1F4igAhjm22R8t08KoKyalbcr6Y-rh0qT-jyz4ztj3BULIw_-9wxCnlujSvhvHxRBAY9PTlv8JVphg-kyZT2Hc9mWm4Jv9ZMN52RxI7mo90ya5yIuQdKIUovTF7EpiXnVIsomSHaglzrUXJGwKzYs1_fmA4EVr_ecU7_kLYEu_mLDDsqdqv5IJKrPQR3KpgWBP653hLHsok4e_Ih4GMoellkfGoo3VtozuCrs3-7YtbamaikS7YcyYNYIok86DPdvH3zGXo1yEEtYlnNvtX1WT-SO0Zi_nPIRdiNefVcjrp-Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😂
وقتی با رفیق بی‌اعصاب فوتبال میبینی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98768" target="_blank">📅 13:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98767">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a26046d5a.mp4?token=v5m728CnenH-FdFteDWBdK0P1SLAzVb6G2RDBlP3k1ZMMXqtQikTetASJRD3SCUEIBdgiyRZSv0BxECxIeBZbafU30o03XuZhik3oQa7RiheLVI_wcnGCgQBowV5h1rNQSJl1OU6sTXndp0VFrJpzlVpmhBr7brR6c07nE0YucCS7p0afc6MYShD2VBsNmD1X7nJCYs6w_aSzedcKbVxiIRXVb3elcfhtGdxnxi5VLTo26OW78IYOfrixtZmULoHtcciGQdozozAKXq5lPNii0rPXo8rvI9q8TLTmbfEF3LYScP6H6FJuRzEc_ZzgncVtTgCPpVCxQiRIPFW1nBrig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a26046d5a.mp4?token=v5m728CnenH-FdFteDWBdK0P1SLAzVb6G2RDBlP3k1ZMMXqtQikTetASJRD3SCUEIBdgiyRZSv0BxECxIeBZbafU30o03XuZhik3oQa7RiheLVI_wcnGCgQBowV5h1rNQSJl1OU6sTXndp0VFrJpzlVpmhBr7brR6c07nE0YucCS7p0afc6MYShD2VBsNmD1X7nJCYs6w_aSzedcKbVxiIRXVb3elcfhtGdxnxi5VLTo26OW78IYOfrixtZmULoHtcciGQdozozAKXq5lPNii0rPXo8rvI9q8TLTmbfEF3LYScP6H6FJuRzEc_ZzgncVtTgCPpVCxQiRIPFW1nBrig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇵🇹
مشکلات‌رونالدو و بازیکنان پرتغال در همین ویدیو کوتاه کاملا واضح و مشخصه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/98767" target="_blank">📅 13:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98766">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
#فوری
؛ پائولو دیبالا ستاره آرژانتینی قرارداد خود را با آاس‌رم تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/98766" target="_blank">📅 12:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98765">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c01d0028.mp4?token=lnwQB29F8ruPJe6CPTvQIPVd48S3m1c9LJEYXACVVxx0ZpHFkipaP-4ItrEwSue97T9ZWrKrqUhy4TQse5Ir5oxbpU86wyQZnI9ozaql0PdPPXZyAchuDTPpa7siuxKLUJmFN1bSPYJTD5JZ9ReA3uv-IPsl058-xa0Zzj54X5yyKwDactOrAANZP6Af3kSZcK6Ht4fJ2wFLLbmgs_lngJeOjZe1UT7QPCGnzeda_L_3ifjxDe0rE53OhKVLwSh1lxRr7xa4UJ4zxzg1NKorNT-D8czRlb09YAakP0NVq9B8JPJf24qGo01n6xR9ZjgOxUbUqKO4I6OLcHy94r4_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c01d0028.mp4?token=lnwQB29F8ruPJe6CPTvQIPVd48S3m1c9LJEYXACVVxx0ZpHFkipaP-4ItrEwSue97T9ZWrKrqUhy4TQse5Ir5oxbpU86wyQZnI9ozaql0PdPPXZyAchuDTPpa7siuxKLUJmFN1bSPYJTD5JZ9ReA3uv-IPsl058-xa0Zzj54X5yyKwDactOrAANZP6Af3kSZcK6Ht4fJ2wFLLbmgs_lngJeOjZe1UT7QPCGnzeda_L_3ifjxDe0rE53OhKVLwSh1lxRr7xa4UJ4zxzg1NKorNT-D8czRlb09YAakP0NVq9B8JPJf24qGo01n6xR9ZjgOxUbUqKO4I6OLcHy94r4_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه‌های شدید نوجوان ایرانی طرفدار CR7
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/98765" target="_blank">📅 12:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98764">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac4eb6bae.mp4?token=eU_i5rmrJhAzcn90pluHUzFiInAkmAV1MjdJ3OaO7VBbt621FL4IWBBCZZSb1nZUkm7CEPc2q6SKxyearJ60R6q808rJsg91ssbcPxsDnc3tPArcpL0P8Jt7ePuXQpRnEnpUtbfrPwyo4xcClyfKtJ23Fid15UVhv8nsenb5MDwa2tF1LXV_NhnYpp6iM7CTCnXJtFxv6DEhowalvq8Sak6HHn2rN-r3FFmLMlxr3EarS0AO7MK7rJhaNGuv5VCpPqK29RyaJZwuNBty_8ICJXS1FKhxi62jeepgb6YTztsda8s7_-pjtAsy1DlSby2ekF2r9lJmmqSdlkIZm6UaVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac4eb6bae.mp4?token=eU_i5rmrJhAzcn90pluHUzFiInAkmAV1MjdJ3OaO7VBbt621FL4IWBBCZZSb1nZUkm7CEPc2q6SKxyearJ60R6q808rJsg91ssbcPxsDnc3tPArcpL0P8Jt7ePuXQpRnEnpUtbfrPwyo4xcClyfKtJ23Fid15UVhv8nsenb5MDwa2tF1LXV_NhnYpp6iM7CTCnXJtFxv6DEhowalvq8Sak6HHn2rN-r3FFmLMlxr3EarS0AO7MK7rJhaNGuv5VCpPqK29RyaJZwuNBty_8ICJXS1FKhxi62jeepgb6YTztsda8s7_-pjtAsy1DlSby2ekF2r9lJmmqSdlkIZm6UaVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
😆
😆
پرزیدنت دونالد ترامپ در بازی دیشب:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/98764" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98763">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5f978d2d1.mp4?token=RgZ19zE2EKVasBtldGrC-zuC-rO7tSZ7t5P401TT_LiBE29bQh09G63Y1tH0EEfCWzYsbl3bPImX8RNb0U5Zj7wfrh-W59PvXDezZnH9xv0FU-bXXAgdvPGb3NHAdPunpZ10VG4RHRJY7UCNDiK39RPYzHZfw1KbBOaEZtHIq79PQSkrtOkOascHoP2jCs3mzP9srDPhSjlq8rTZSffVgik0ZGQynfomb2nTpHP0vRk8pw-vdWpCLuDGDAHKociL5r9TWuJq7YC5BJZP2gzYc7C9lSF6qz5LxrCNpB7fospYmVAMBBunWz2qnwZDUe7jg6_DsJKBxlTrAC1E6V9izg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5f978d2d1.mp4?token=RgZ19zE2EKVasBtldGrC-zuC-rO7tSZ7t5P401TT_LiBE29bQh09G63Y1tH0EEfCWzYsbl3bPImX8RNb0U5Zj7wfrh-W59PvXDezZnH9xv0FU-bXXAgdvPGb3NHAdPunpZ10VG4RHRJY7UCNDiK39RPYzHZfw1KbBOaEZtHIq79PQSkrtOkOascHoP2jCs3mzP9srDPhSjlq8rTZSffVgik0ZGQynfomb2nTpHP0vRk8pw-vdWpCLuDGDAHKociL5r9TWuJq7YC5BJZP2gzYc7C9lSF6qz5LxrCNpB7fospYmVAMBBunWz2qnwZDUe7jg6_DsJKBxlTrAC1E6V9izg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ویدیو لو رفته از رونالدو در رختکن پرتغال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98763" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98762">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpOgTlZrHhBrbHfF8wS_s8izBhKrIdYqB7P95fEaXWpR-XM8rFHpxSR4pugTRygLeYHo70DbqQo_zl61y0i-5tpRGjkVkZasjkRafkhoryPvAcwMtaKRMAjmtu-wn4a_ZIS7cb3ZFBIgTfvFII0PHCfrzKy8DkuTbu99zfB2CkkoDLStWsrXOyyjj-1--Q9pxP73zzQnfQy0QvXQCvbZpb4v_OCAxAO2YOylJ7FeTKE4sneJs9p-HWY4vCXkx4wPeIV2nh8ACqTApJzovfBjJFJrJ2WFxS7Di8iIn9K1ZqfE1J1cKxD3dsDjTZcm68p4OqYaRF5LgBNAxYuZxbJnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇧🇪
اونانا هافبک تیم‌ملی بلژیک در بازی دیشب دچار پارگی رباط صلیبی شده و ماه‌ها قادر به حضور در میادین فوتبال نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/98762" target="_blank">📅 11:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔥
🏆
فقط چند روز تا نبرد حساس مراکش - فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/98761" target="_blank">📅 11:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4HSIayb7GyKDWWTAaEYmiYN_7j4W9qIeAHi_xpMaLp-l9Zfzb1-Mz5iK4mrgxUZttaTmp4uao6E43JMTFFeum0gH1ePcNw3Xe7VTL2ZqQ8nCnikajpr6icAUyAEUenhE3nzh6jJoVtEWpKrqDhvYsRUw4Gb80tfzaq9n3UFc9KXWMvFEUm6GpODTyu-_Aux8BJNYomajX52tGwdbX1ZGONpsXXOcKJOuw4bcggEGokX5pybfdaews1tKOzpIQ0z0cagHScicJy12kfrejxTpy_iKRFeViHReQrOknCQIGWIFDzDSiacuAPlvW6xsGfm0fRs-LwZicQE4YUktd9MPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
اینیگو مارتینز با النصر عربستان برای تمدید قرارداد یک ساله به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98760" target="_blank">📅 11:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3Pxc_emWVzkWgBneIfrs9DjSz7PRMk4MfENlqZ_16Zzd4REOdT1YaTOG91mzN4MdxWDnCnJMVj3IIHQhXcJedqsplPJqyrKDwF3WUJa75plxKXWJhC73zTiQ987wh8ke4bzUcN_kt86MyIwH8r-oEJ3Qje1GvpITUMM4WeQ3uXbmQSUdGlfqdfb1q3a2mquTq52ZemAFj3t9nz_eV-d-XhbDi0eI2XH3F6Nrw15ucHYVUQOf9IcYH3XvxQ-3RY5K1LpejVyCWm9fROHx6snu1dCoCssrldxszFXjzmUZooI_XmDlz-azODfagQ0Apmiys6HB1YlM9iSDqoJIt_Agw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بازیکنان رئال مادرید تا به امروز، از بین تمام تیم‌ها، بیشترین تعداد گل را در جام جهانی به ثمر رسانده‌اند.
⚽️
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98759" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8801234d0.mp4?token=HT2CWRq3kwdfuJrhCcG6z1VbBVXmkEaTqVhubDmju0UykU6NU6YZ6Zg42lA_R7TBkdRrP3xL9jDe4kKBYAq8BgA3guRisJD04HRixAEyuJAzerbJ11xE9qxnaJns6dyDEhrwPedOAIVtkS1IF_k2LOPq7qoQ8ugPhY9Ooj_8ZKeN_cGU-GpFcq6HIzR8VnX37Fyc0TbSECQCXJf3AyS7c8C7aic9bs_mvC96h-cWkyLdiNeOQ4t1xDgP4v9wjad9O1mgfMbB-C8GapefOu8Fobfh8dV4OtOLizVF_0wolw_oolPSzDFMJUELM_sJ6h0A-eDEb1J1hAWsgThX4TTTSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇺🇸
🇧🇪
خلاصه تقابل آمریکا و بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98758" target="_blank">📅 10:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ-1rofA9pYvpp6gt4kP3N8KW2A4Xn2Gymqhn2bMpA6uo3kSUCy2DXG2UwHRTJjNZpMjZqtrxF6f6TW-sPZNA4EK_BpxUmAvf7rYwQqWTgFQK4Pmsp0zUA1ZCaZjbcMV4LL7fV1nCgXL28DQmP2JYA4BTB7cna_sqIMWj5iFfR_BBHNQhW0LPnGt9bblfdvMg-w6kMwISDAmjQB_oeBIIkiJcn0o7mdYpu4EV8RvqOftXawnM6upWI_Z8pOoEJYeKCIFenOo9OwR5kZ3wd0XGT4bMVYLcZ9t-6tSeezLw5CvOF517ifzhwCU7Rm9XnMbpFedpL9DILB0feNBze-Cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
استوری پیج تیم ملی و کنایه به حذف آمریکا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/98757" target="_blank">📅 10:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6KyX4WQKOVwirJpxEjrG_LKB-RkgZQT-SlUK9jQG8wpX-rpwxSlxdQ_JYKWSp_-hrvYWNOPW2L-7rMd9r0ruR6LqX6eNCugrpYMx8T9pvsbmtWpCGq5BOoyz3edTOdvnjryo2BaLHm-KDBTjSk7zNevoo3ZEM0RNRawArf_Y5Z8AhR5HjakP1tBlkqeXAMwKEkdJgk_NMgWuFzp_8Npx1GhaHTZhnTkQUFkW0S0LWzn04fitt_SaR0G-kKqU9ig80aoKyx4JDq_XBGNSRfXKnZfKGejgj_iIJF9k1nOLV9P7bqNpbEqbVhYGAiF53X_ccVlqoWfJK7RU1UJG1JjI-c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d094fe0d5.mp4?token=WCOayQxfav-A-JoCratW3bGkJF0re6sx-R0U8FAfyhNtgRwFPP6ciT6mfY5K3c5ZgYbQpD94QXlGfg9oZWdh4Vob88XNQ4gccHIWRcLACk_4LcKVonjfWuKaL_JbHiqrdfxPns8OtkZlpAq9yk6XtGXTPJlYFNkaMI96kOIlKHEl7jP5DNCmFi6HWE-YBbORm7eQvtJ6qJAKUfJpNdoGCYIamfF0alXPw4gmGk7eHv6oWwUgSLqTLI193aJ1JMYMfXZJKHuqRn0vrXVClgOfMRvGNn5jnkyLGDcqpd9oTICyfxo6RtFSqWNiJLCIlN-NST33GMBInWsLoEySJ4QLc6KyX4WQKOVwirJpxEjrG_LKB-RkgZQT-SlUK9jQG8wpX-rpwxSlxdQ_JYKWSp_-hrvYWNOPW2L-7rMd9r0ruR6LqX6eNCugrpYMx8T9pvsbmtWpCGq5BOoyz3edTOdvnjryo2BaLHm-KDBTjSk7zNevoo3ZEM0RNRawArf_Y5Z8AhR5HjakP1tBlkqeXAMwKEkdJgk_NMgWuFzp_8Npx1GhaHTZhnTkQUFkW0S0LWzn04fitt_SaR0G-kKqU9ig80aoKyx4JDq_XBGNSRfXKnZfKGejgj_iIJF9k1nOLV9P7bqNpbEqbVhYGAiF53X_ccVlqoWfJK7RU1UJG1JjI-c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
مشکلات واضح کریستیانو با برونو فرناندز و سایر بازیکنان پرتغال در بازی دیشب...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98756" target="_blank">📅 10:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b541523a.mp4?token=mmdyR3EhrnI9haPstaAp2hU-IqGgKGACItpi2QdYsr66oY8bJQYh7x0hgmqPsB8TbFHBs67Epl5aigJx1RX5QzFQ1vvXCR5jaNa11mTU1eZjn37ITgtZGzhinXJ3RnwMz3xpcawkAhmZoJ-CvKPSF_YRNw9mJrA45yHnT0sRYPMtoqo_5L4ZrRoARBaLLXyx8FSfwN0J8muXgPNJpua1a3iY6DI_fSsXFKPoBME5e6XbdAc70NKeG1Nxs1zjxZkf5xrrRNXBu4uE7ge8BmrH3cBoXQC38TRuN2SUjfJ5sYqbBUwAtwGuxrP7cy7motNBYGqunHr-mltMBJWTSTCz6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b541523a.mp4?token=mmdyR3EhrnI9haPstaAp2hU-IqGgKGACItpi2QdYsr66oY8bJQYh7x0hgmqPsB8TbFHBs67Epl5aigJx1RX5QzFQ1vvXCR5jaNa11mTU1eZjn37ITgtZGzhinXJ3RnwMz3xpcawkAhmZoJ-CvKPSF_YRNw9mJrA45yHnT0sRYPMtoqo_5L4ZrRoARBaLLXyx8FSfwN0J8muXgPNJpua1a3iY6DI_fSsXFKPoBME5e6XbdAc70NKeG1Nxs1zjxZkf5xrrRNXBu4uE7ge8BmrH3cBoXQC38TRuN2SUjfJ5sYqbBUwAtwGuxrP7cy7motNBYGqunHr-mltMBJWTSTCz6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
خوشحالی شدید میثاقی و دیگر مجری شبکه سه سیما از باخت و حذف تیم‌ملی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/98755" target="_blank">📅 10:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2731679c05.mp4?token=mIDEamKAi6dvygxQ5lhWFHYlUdpRpgIiq9s-oeBIEGI-ziIB2VH4qTfr5wk20Z31j0-5h2qpJenhZCn5VpcUwcdjB2ZTKjzIxCbvTHseS8jBGxEf_zFyodZ_K2tzFJGf4_hmbZqttp4WgR3B4tL9tKOXrDCjAatiJJJK4_FPHxsJetLplk6P-2zxaLP9JQ_BuC5sN7ZNk80MQCyIlGNy5liqtOg9r122-ntVEc8DIGPLZLiWFppSczi7qpo6LJmyUix0vX0XEKnUPm9223ra13pndZEMOMK0MJyYyMpCff-4vT44l7hMH92IW3_FFZdA6SP7D5P41Ki70u2Xw_h0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2731679c05.mp4?token=mIDEamKAi6dvygxQ5lhWFHYlUdpRpgIiq9s-oeBIEGI-ziIB2VH4qTfr5wk20Z31j0-5h2qpJenhZCn5VpcUwcdjB2ZTKjzIxCbvTHseS8jBGxEf_zFyodZ_K2tzFJGf4_hmbZqttp4WgR3B4tL9tKOXrDCjAatiJJJK4_FPHxsJetLplk6P-2zxaLP9JQ_BuC5sN7ZNk80MQCyIlGNy5liqtOg9r122-ntVEc8DIGPLZLiWFppSczi7qpo6LJmyUix0vX0XEKnUPm9223ra13pndZEMOMK0MJyYyMpCff-4vT44l7hMH92IW3_FFZdA6SP7D5P41Ki70u2Xw_h0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💔
💔
The End
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/98754" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=YyKAeTCTU8dmP3QqyLgP6P_kF416GiIyp-d_lN7N9FJtgZq1NThV1e9kw_HrooQNsKbCrG_c8iL274mnCpMwG_4CduUPpihUzrxilqFmltdAfpSuqOiQys3PJgR3t2FPPZXKBQxSNxlj_-Xe8kiR0iybBtVQa8l2nJx5TrkIops3UDknCLGscdnlNAk8zdqQ4iu8r54zE54KlE9zBRtCQa-xRnEgF4Icz0jUbTQVyqyzhoXxFlJ3al8LQP3XteQJUHzVLO7Xxo0od2lO1nS13BLjJtKgJVenTf2Muq7S9B76bkFD61LCuHPGHXBGwbqx_aQVhj1K54sniFLHHTIDfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6be3fa0b5.mp4?token=YyKAeTCTU8dmP3QqyLgP6P_kF416GiIyp-d_lN7N9FJtgZq1NThV1e9kw_HrooQNsKbCrG_c8iL274mnCpMwG_4CduUPpihUzrxilqFmltdAfpSuqOiQys3PJgR3t2FPPZXKBQxSNxlj_-Xe8kiR0iybBtVQa8l2nJx5TrkIops3UDknCLGscdnlNAk8zdqQ4iu8r54zE54KlE9zBRtCQa-xRnEgF4Icz0jUbTQVyqyzhoXxFlJ3al8LQP3XteQJUHzVLO7Xxo0od2lO1nS13BLjJtKgJVenTf2Muq7S9B76bkFD61LCuHPGHXBGwbqx_aQVhj1K54sniFLHHTIDfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب فوتبال گریست.
💔
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/98753" target="_blank">📅 09:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=Cif3qn6QSFK7np1xwD9XX6hYrANoVAaKRQoDyVA6CtqnV32fipiiQi3khom2KwmpJCvTX4affVpdQbn7X6ZPvPDv2FjxEboUbD6YWUA1-gM1zmZNO0ygkFy-mJnz3xOMfJUP4Isie8a7jzYTZ4KO6abJcoxWRpxTEnCX2H2NGSKAtybZHDkrGDmhoJFaqqj1hRibz7JcitmDgl6gtGWZq0PqKTfx2aXAzXVqfpkYs1DSsB8g1_TL3iSJE1iTNSpRSwxAclqOkeoOoF-_owc2xMBlkF9wVPUwFMZvvZpUhn9L_1eEI0I9mlp0CIPZZ-UjZyudreiH0F-vxxClVhGQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1d0006e7.mp4?token=Cif3qn6QSFK7np1xwD9XX6hYrANoVAaKRQoDyVA6CtqnV32fipiiQi3khom2KwmpJCvTX4affVpdQbn7X6ZPvPDv2FjxEboUbD6YWUA1-gM1zmZNO0ygkFy-mJnz3xOMfJUP4Isie8a7jzYTZ4KO6abJcoxWRpxTEnCX2H2NGSKAtybZHDkrGDmhoJFaqqj1hRibz7JcitmDgl6gtGWZq0PqKTfx2aXAzXVqfpkYs1DSsB8g1_TL3iSJE1iTNSpRSwxAclqOkeoOoF-_owc2xMBlkF9wVPUwFMZvvZpUhn9L_1eEI0I9mlp0CIPZZ-UjZyudreiH0F-vxxClVhGQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خداحافظی رونالدو و پرتغال با جام جهانی 2026! اسپانیا به یک چهارم نهایی رسید.
🇪🇸
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98752" target="_blank">📅 09:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=AWpPwpvRFeOfsohb8GdensTGIf-cdsGJ8DjEG1Iy2BaDupggMgFYp7Wleqsn0WTVZxes49f0YabtfVXdqt4UlAD--Mnqkky7zydKL5antRqGKKHP38GzmQ1e6bZEpGRva4tLcTAMDhqhXDC2fboaQXYwjkd4EsA9I6YzXiUNHGpoxEV35m3okWmSAekqAuVTZS-wo18KD_5N-4Z_j1lZL7XlImGhME-6b_As2uUN3Me_s-F9mChax4I27Gz05Qx7oFxn1ARff1bIRXXccmA0fVKaard9CMRYg_tI3ac3yuykswGXsDp2eSwkF4P__niTdcyuizt09mosjJLDg8NetD6Scdk2b3I3Q7TjJBjyBGdMlf8TIt02KnM88ud644_1rFNvNSTc9dKCeCxOWUhumsRsjAzW3YEY9r097fkWDkb_qLfsADOYf7zN3ka_m-vZ6MXsP6OWEEq3LIkMBZbrlW6SNxCPcX1I9XKUqm1laK9k34Xi8pnwUNUeRxwbZ1BWVhzaxuOpQm_d3cGjgM8xRDAIj_xeBHMqlYxfkrxb_sFgY0qoqTv_eUWB9pusseOnMPU7FSM5gu1jtYGaUQG2XhEb41wuRAlCD5AR-5UVeDNVWK06VL0Xi2TAX61Q8YcQki9KHI8taMhTjcyJ-BnRg1S_TTJdbWSt1I0TDPG1De4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbf2cb410.mp4?token=AWpPwpvRFeOfsohb8GdensTGIf-cdsGJ8DjEG1Iy2BaDupggMgFYp7Wleqsn0WTVZxes49f0YabtfVXdqt4UlAD--Mnqkky7zydKL5antRqGKKHP38GzmQ1e6bZEpGRva4tLcTAMDhqhXDC2fboaQXYwjkd4EsA9I6YzXiUNHGpoxEV35m3okWmSAekqAuVTZS-wo18KD_5N-4Z_j1lZL7XlImGhME-6b_As2uUN3Me_s-F9mChax4I27Gz05Qx7oFxn1ARff1bIRXXccmA0fVKaard9CMRYg_tI3ac3yuykswGXsDp2eSwkF4P__niTdcyuizt09mosjJLDg8NetD6Scdk2b3I3Q7TjJBjyBGdMlf8TIt02KnM88ud644_1rFNvNSTc9dKCeCxOWUhumsRsjAzW3YEY9r097fkWDkb_qLfsADOYf7zN3ka_m-vZ6MXsP6OWEEq3LIkMBZbrlW6SNxCPcX1I9XKUqm1laK9k34Xi8pnwUNUeRxwbZ1BWVhzaxuOpQm_d3cGjgM8xRDAIj_xeBHMqlYxfkrxb_sFgY0qoqTv_eUWB9pusseOnMPU7FSM5gu1jtYGaUQG2XhEb41wuRAlCD5AR-5UVeDNVWK06VL0Xi2TAX61Q8YcQki9KHI8taMhTjcyJ-BnRg1S_TTJdbWSt1I0TDPG1De4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
▶️
امیر مهدی‌ژوله یکی‌دوسال پیش این حرف طلایی رو به عادل فردوسی‌پور گفت. بفرستید برا هوادارای فوتبال خصوصا رونالدو فن‌ها که بدونن ناراحتی هیچ فایده‌ای نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98751" target="_blank">📅 08:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=SFBh_KLLI15cSMwzCismcaPQAkN5sco1nnSVvr0JkHSi6ocG3ClUTOOeSvF8PuMs_RHeLohpVeeir189m9feLe6vC_r-3OQYQ3rALzqklktE2PTe-G08h69_1HO7Ab4dsYS8ldYjRK88dC9muOgDdsx4cpOp6f2bx5V5Alh54JkpHHMsllsdBjAdiUOKCmLMTJbh_RcJ4XMUsVSA52V7ZSgqdtCcokmMB2p15yFFM6xg194VlV0Mci9Dz8kJTExBUwFatedt4_Vqd5YeBmiUngICHLMmaQov-wAVyslTf3qbfbFxcq1jIHifnjeX5WzfcSD7oPeWx0A41JxBvxM55g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/898c349cd0.mp4?token=SFBh_KLLI15cSMwzCismcaPQAkN5sco1nnSVvr0JkHSi6ocG3ClUTOOeSvF8PuMs_RHeLohpVeeir189m9feLe6vC_r-3OQYQ3rALzqklktE2PTe-G08h69_1HO7Ab4dsYS8ldYjRK88dC9muOgDdsx4cpOp6f2bx5V5Alh54JkpHHMsllsdBjAdiUOKCmLMTJbh_RcJ4XMUsVSA52V7ZSgqdtCcokmMB2p15yFFM6xg194VlV0Mci9Dz8kJTExBUwFatedt4_Vqd5YeBmiUngICHLMmaQov-wAVyslTf3qbfbFxcq1jIHifnjeX5WzfcSD7oPeWx0A41JxBvxM55g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
وضعیت آسمون بلژیک بعد از بازی امروز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/98750" target="_blank">📅 06:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3BFj3-MOKZLZmal3j8mBHdAZh301MVEoNo53oAhYeciT7MmG7-BcKQSntxSwI1uiD4xvIOxBWmYRTigK7LSs4gC0tS-_pAhl_UC_vDdZdling3JjYWH89qRZqjSxFYUy3HAdwjM9lfjsujcsYiGVIhqlpiM5YPbdwT8a6vFyPcFJrwHoES3PzX2iaIs_MPelTsApI4tuJt3IYaGpUFoG3CcN4YKMUIlkW60f3FfBg1OUXxWIAFKG04yNpbaV3sm0N0-D7O01j724lUjaX-PuP049Li9ESVgKYBTev9TcGXMXMiajWlf3IziXk-f-dhpGdz_AT653hcfN5voGNMqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98749" target="_blank">📅 06:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGtaNIDXH6KGUryDa63rOy1EcFoPD-hMZBW2nWp7Q_LYw1jctLbIEzU8kTPyR4Menm3oKAPh3HFnx_L9ayA-OR_IVY2dagQgl2VC2IUTEjeQOWxYFDOmOZT6CkZjsTkbF6BoX2QYZZOxsr0gn20vC5nz5ZvzMREU0Ntt_BqZwTHCCfLu2nv1SUrS9vTgkuGNASn-N0xNwuZ_-Tsc2dAVzXma2TEzBnr2VA6gadYRGflk_IWM6fyiseF7IK3OnCRA8hx4ouNV2L-4o9TmN9q3o7oeHAHRZYmhK9IWzZ47IXDc7nYgDEtK6B7ZIBuAPJI5Gp7UUDkCAB4zLDvN_2T_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
| روملو لوکاكو اولین بازیکنیه که در چهار بازی جام جهانی، به عنوان بازیکن تعویضی گلزنی کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98748" target="_blank">📅 06:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkanwpFZVwpe3Yp685742g4NKbpIHxK8QvK-6WmC0tFl-hAw4EzePFL09gUGz8ptcVz-HwoucDGgiE-aRaPwb7rxjxKbs0Coj-Dv9yqDjgx5hgPqS9jmqJoEo8aA0rO-bWGjnsftc8jhtHtk6iAdVRSm01ETJawm6yPeTsrOtfrwJblNRNlK6Thb1lPioQ-igDIy10F3qxmqAApooqP1UC4Gc4q9pIsoxOv_FGWeYbZAMrWE43A2V4aAS6UczlQY_7NWVe0DR4jqTBog1joOBRZufqpS9mET1Hrw5hENtZYhfvtdfUEZOhqy_VSMwDDvllo39FeXiuGv4T4OBHJ0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس پیج توییتر تیم ملی بلژیک به آمریکا: به این میگن
ساکر
فوتبال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/98747" target="_blank">📅 06:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYpY1AJ3i8d-SboAIocxbFPGeBk6XmYPPrjzpy2MPB5yIyLaZePUcRUHh-mNkYGagAG2AeqnDUftK5nwc3uIa0E6s3Lt4xaFvpDWfiYrjbhlHJvld0RitupJaI7cX9fOKQOVKHjq8Wu6_dOYtPjf1p3XSKREjlBHHxJBZ08kFxQkkg6yafU4g7QCja4S8iVYCymokW20RAwEVfOk9cX8o8Rht36x2SshhC_sL6GbDFLF0fBFycLgwRp7mHcxYI_Bh_MYpTNUJkF5fXI8aqlDWPoqVDvQj2J_niI2BmQ4Y40Ej7LFHlOa6xxl1rbtQ6jddoNV404ivbkOR0MoKR3eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابل جذاب دو ستاره این‌بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98746" target="_blank">📅 05:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BobE2QSoKQ80LuQIdmNFVWb5_InAdBn0pTLontmVSqDEBxrGcrH2hGAlAd7akXdjKpxvlouOUv3s2n0VUaj0tkJwkaQJ5cMcKt2LaCHDwwdNHliIgN2QadJG0J4mOEXg-7PXTd0zSWCa1bnfZAk-TOlgLQaGxNfsr_8P5EObpwrCq21DL3m3nc7puNIQkfNxCvOgOI6IlSVlwEcExvmS3YvLCgFP1odqoTMLZ3qO93uZ43ebEeS4oDEOFDARptc1NaKoZu4XsY0umVM1pOGkKXM85h5ycXQAhRUB3Cz0wXxHrvw1npb9ul0x8o73QVEtopJbke6D5art5bIK_sjOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مرحله یک چهارم نهایی جام جهانی
🇪🇸
اسپانیا - بلژیک
🇧🇪
📆
جمعه، 19
تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/98745" target="_blank">📅 05:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7macHP-2wy2mN5StMVRQy6FUOwGyTk65FnOgrxnE76Pmrpl5Kv_pCnH8I9lDXJaRbwcpQZFK2S1ygy17pJyq4TtP8gLYdqYjGAi1DwidRNgxOsIDyWgsAhv_7I7vP_6zCQMu0tCJBn-qnomryAHFc53LUUapUBsfRWcceeq2zjD2fZgssxlFOMF9gwpY9q7NwcdqUg2OWBzBPpNNgxMg31WNV6e66psMlbt9FAIEM3a-YcM0CZ-3if7UnDfTuVZhQ-Y6DTdewoeFW86kSDVou0UKIN1manqys-RktAY8snnsUh0adKILVO8OCm8gOoEW2wZG9IaE8vC5uBvQ-A6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت نمودار مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98744" target="_blank">📅 05:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAMua9AER_YSgBShkJe3qT4OI5AZwtGxHRZ0OGBp4sDv278MKI6FBf-IBWTI0EGRMTEyr2Eip3bWdW1oghXf5jYWx-E9TQXA-rwlPzMJT6gUMbG4V6DbU1gslV-PmlRTFcewd6mBzeZJLe1MjxKeueLoNTqXvi-KHHBPKnu-Yv8RvIwipiazGqlUa3fCV6q4doNBOMbo0F_pxZ0esQL8ReJuA0VXX9Eq9jXxI_TsNP_8duip09Orp2NP8wHBHIsObz9BtsYycZVEak9joeqKo0SUn8B626_0CokUyWsklqexw72xJHkHKhk6AGwim6hsmtZrDh3XtiGHhTelmhBLVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برد قاطعانه بلژیک مقابل آمریکا در سیاتل؛
کارمای بالوگان!
🇧🇪
بلژیک
4️⃣
-
1️⃣
آمریکا
🇺🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/98743" target="_blank">📅 05:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=hbCwasM_FVldeawmGoLBopdpW8_4AvDNY4QFkHRWfu2MWckGsInLSrtSCPrhFNGXVENkPWcut87BwvNyWzXmQ1qvlkZ1M0E39ZZUHvhJspKQp0GU57UtqmiN8H2tx0NOo6YVKDTTGfuZBYH8h7ofJeIq_G5zquu652X-z4YEwH87b3eHgxmlZNihRF91MOeBCnf_v1Z09qs17qTV1vKPY9yVyiVmune9NojXPJYmQ-WRM6vGnpr4dw-hSv0Pk5Agmp2K9uBl1xR678CS835KzrMLi8TcyeMPPBqZomBtA7ezyGAsJH8pUjRjEgVsOkfpeXpfkLmPosPZOMjG0juQbw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f32a4acd3.mp4?token=hbCwasM_FVldeawmGoLBopdpW8_4AvDNY4QFkHRWfu2MWckGsInLSrtSCPrhFNGXVENkPWcut87BwvNyWzXmQ1qvlkZ1M0E39ZZUHvhJspKQp0GU57UtqmiN8H2tx0NOo6YVKDTTGfuZBYH8h7ofJeIq_G5zquu652X-z4YEwH87b3eHgxmlZNihRF91MOeBCnf_v1Z09qs17qTV1vKPY9yVyiVmune9NojXPJYmQ-WRM6vGnpr4dw-hSv0Pk5Agmp2K9uBl1xR678CS835KzrMLi8TcyeMPPBqZomBtA7ezyGAsJH8pUjRjEgVsOkfpeXpfkLmPosPZOMjG0juQbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🔥
تقه چهارم بلژیک به آمریکا توسط لوکاکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/98742" target="_blank">📅 05:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بالوگان فردا املاکی کونت میذاره.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98741" target="_blank">📅 05:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">جوری که بلژیک داره میرسه به یکچهارم نهایی ماتحت خیلی از تیمایی که حقشون بود تو اون مرحله باشن رو به آتش میکشه...</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98740" target="_blank">📅 05:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=MbyrfCBJph8M8OwNksOpEaGUYsJiYqaog2M51Ul_KJEjDfCmsbbNtPTX3Z-9d3XmjBFzV5l9RPY7i7J1sD-K-mvpRv_2r6OsPiVengewkkUoRyVPxidUW264Asqa29AfkNTk0QhBegdPuMdq9qbGdePEQX0U7h0WbUaEiZe-4_SkPTJmdwLJuODwfCO_OI7o9mPHVdjwJneFrYVdLCm6wvp5NdHote-_dTq4aToaG4AIojFb6_68hp2-n34gdzz36XNXWkNnWRZVh6qLZBkMW-iN90lWKK0h-5V5jSjeQhNhPrUXga937CcAdqIdI2XAcI2Yk_qnFkeUWusQ8BiBQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2f766a24c9.mp4?token=MbyrfCBJph8M8OwNksOpEaGUYsJiYqaog2M51Ul_KJEjDfCmsbbNtPTX3Z-9d3XmjBFzV5l9RPY7i7J1sD-K-mvpRv_2r6OsPiVengewkkUoRyVPxidUW264Asqa29AfkNTk0QhBegdPuMdq9qbGdePEQX0U7h0WbUaEiZe-4_SkPTJmdwLJuODwfCO_OI7o9mPHVdjwJneFrYVdLCm6wvp5NdHote-_dTq4aToaG4AIojFb6_68hp2-n34gdzz36XNXWkNnWRZVh6qLZBkMW-iN90lWKK0h-5V5jSjeQhNhPrUXga937CcAdqIdI2XAcI2Yk_qnFkeUWusQ8BiBQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل سوم بلژیک به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/98739" target="_blank">📅 04:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/palChTQ3vk7u2ycn8I6HuBnF2PVmkfQ0KZYcnC-5QdOil6fj0rPcrZCubRmkIsHZJ95Tf8G0W4ISpIbY9OB84pqzjELTykTrw2JgOit9k-SvQ9KmLflRDWnPu1JRbxJp23OSRkmn6Tf0EtPYUFibr80FEhcvo0H2jC1swEZdsWltKnSiuDyCEEiRotPJeNpFE_ck148NQrKAPNtwNSt8bQdBS7LcDJP9G2SeIuWG82X19hQPiJgLoWxPOdLoDFS1A-DuvL-zNtVj36XxvJf9sEICPpydBPmuLYvo3U1LbamN7fkWpWbZ2OzeiciMpvgVyk4T0Kc7Ug5L3mbpztZDgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی ترامپ قرار نیست برای گل‌زدن بلژیک به آمریکا با سنگر‌شکن B2 حمله کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98738" target="_blank">📅 04:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=mlqrccZ7TaB_nHIvOy1DANSKOI0aR3Yovz36FAEsV5T4piVPALgxDGnx8e0hoYvqHYEjRXnX-cMPkFjCjhGf12YFz9eXsib4C3hV2QL5H50ltgrHbk6fx09kcy_UfOiwvKk-S3q_rSyAVQYmSjtVJWgsBzA3W9gFP7D0O81rtEe8gyy1zaqMym2rtdbQKAOqNe-R9nKcWHuoP1pJzkSQMNa8hPNuWeqsFBtvHxe0p98Kd1ZpzJDxPmwz8sFHZVqG1iI_8tKjedTzqsmnwYt7l8FHWCE0DLTzTyP-_Ad5XBlMd8Sno5XbdkKJNDchxZ90s0568j40ofu4c2F9bz6lmg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1e15b6c1dd.mp4?token=mlqrccZ7TaB_nHIvOy1DANSKOI0aR3Yovz36FAEsV5T4piVPALgxDGnx8e0hoYvqHYEjRXnX-cMPkFjCjhGf12YFz9eXsib4C3hV2QL5H50ltgrHbk6fx09kcy_UfOiwvKk-S3q_rSyAVQYmSjtVJWgsBzA3W9gFP7D0O81rtEe8gyy1zaqMym2rtdbQKAOqNe-R9nKcWHuoP1pJzkSQMNa8hPNuWeqsFBtvHxe0p98Kd1ZpzJDxPmwz8sFHZVqG1iI_8tKjedTzqsmnwYt7l8FHWCE0DLTzTyP-_Ad5XBlMd8Sno5XbdkKJNDchxZ90s0568j40ofu4c2F9bz6lmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل دوم بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/98737" target="_blank">📅 04:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=U3Y_1E0cU4h50tqfEiTkV2z2sXAIR4WS8LBOfvbmGw05sBOD_j9IT2rgqu_6CNt7IGEWIv7BqyQC_mVAlgRFk-HvD2PFRpbwu6BC1M-zP77obHFpXphauT2n1sfvPVLYnDNQO5psa7k51s4585FjDgXC3wl9iHDpHT7yaf6GVm_xgZNvq-OMTUkq61laMKdcBBX_uvr_eYvvp0Qgd-ygdCBQNol2_tzaEj9gv3vX3szLDvT7LfNnVFLAVRZ5AfKD8hpht4JTyyQ4ubgwGjRdcENTydepuETZd0c6V2ewrR1OV_-zY_J8Ejq5_I4C8kACiC8GsVceFMzyYfSUwofwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275ce58db7.mp4?token=U3Y_1E0cU4h50tqfEiTkV2z2sXAIR4WS8LBOfvbmGw05sBOD_j9IT2rgqu_6CNt7IGEWIv7BqyQC_mVAlgRFk-HvD2PFRpbwu6BC1M-zP77obHFpXphauT2n1sfvPVLYnDNQO5psa7k51s4585FjDgXC3wl9iHDpHT7yaf6GVm_xgZNvq-OMTUkq61laMKdcBBX_uvr_eYvvp0Qgd-ygdCBQNol2_tzaEj9gv3vX3szLDvT7LfNnVFLAVRZ5AfKD8hpht4JTyyQ4ubgwGjRdcENTydepuETZd0c6V2ewrR1OV_-zY_J8Ejq5_I4C8kACiC8GsVceFMzyYfSUwofwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کاشته خوشگل و گل تیلمن به بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/98736" target="_blank">📅 04:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98735">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=lduB8LpMRKD_kUZwPqnJGMaeDnYWCEGkYtayqlmi2eU3N2221xN091nAP2637V3qh9H72WVwKXm95NRt10PAvUFuvbxwG8w7DHTArngQawk2vmYu1eCSlAiCUpxf3aTOVTj5KWQhoApEZjcBX6ekqDHsp7reafy3MIfcrYwZJzobyUcO6L7VOuYjYxgdZKvn28aZdVZQxDPxtu1RQM3PmKzsMGqy07sffs4xsBqk23D4GP5lcPVtyFwOgRBdyCJ3NZKr1RcB8biWUFqq59VbtN77f1lRHDeuLAMJpM2HUcEETTrXv3h6OuyiKsk00UfUXZNLff9S2-VL5F2w9AeA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd14e6484.mp4?token=lduB8LpMRKD_kUZwPqnJGMaeDnYWCEGkYtayqlmi2eU3N2221xN091nAP2637V3qh9H72WVwKXm95NRt10PAvUFuvbxwG8w7DHTArngQawk2vmYu1eCSlAiCUpxf3aTOVTj5KWQhoApEZjcBX6ekqDHsp7reafy3MIfcrYwZJzobyUcO6L7VOuYjYxgdZKvn28aZdVZQxDPxtu1RQM3PmKzsMGqy07sffs4xsBqk23D4GP5lcPVtyFwOgRBdyCJ3NZKr1RcB8biWUFqq59VbtN77f1lRHDeuLAMJpM2HUcEETTrXv3h6OuyiKsk00UfUXZNLff9S2-VL5F2w9AeA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
گل اول بلژیک به آمریکا توسط دکتلاره
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98735" target="_blank">📅 03:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98734">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9kkJhglmMjlEXD763G7ssT-_F4VAz7laEG_RMapExJTaWcX2z_K2c4WYBpbS_-yqdhlxrHEFsTfJZv0Xr-wY3v6Cby4r7y090WskTI5jHqxoL5DTS_YWXSs7-yub836BHubXOq4-RC7dAjpuFPKXBY96Z-wu4B9XgjDtsLlCEpzY6vIgAMTnFkx6-Wq_kAB3cFlFl9E6rTvSSmuPQ0IEE0RkBwQ3udUXwB0GkUfH63-rS19zPL6pcndU_zagWOULRMmLERF_K863RGBQswxbo_v1cGWF2D5OceEWTvLzHSjsUMaGgCFX-4bJYhE5UQiEG9vSA_x2bR9pJfUcRYkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اینفانتینو بعد گل خوردن آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98734" target="_blank">📅 03:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98733">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXAoXhSIoggCSFYxsG-T7yI9ckb7poBDEXuNyPXyHzXFmbnBo5lP_KIoD5eOSZW6BqhCsZCCefbmV0klbKG3GeZIqvpWJue3_JU1_58PUSF1CPAilgYTHWE0vmZxPVOVb3BQZURgKoTDRU-TfFLDmol6lIM-Y8SgCE2YbCC9HuD9Td_yBOMXI-hhGKHJJjIpEJ7kQRBlYczBBEkK5mjOWy2pJG4wnADUG8BmebmaCByK35je203kiYOjVE7VmcZ6RwbYyXFuRy-6znPFPVsK_cSISzhje2bH0zEAImgtsXj0hrZyk0sPYitE6ylZfITXiFNcGOJr_rq0YpYmS3wRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای رونالدو کامنتای مرینو رو بعد بازی حسابی گاییدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98733" target="_blank">📅 03:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98732">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گللللللللللللل بلژیک
🔥
🔥</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/98732" target="_blank">📅 03:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98731">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بریم برا بازی آمریکا - بلژیک</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/98731" target="_blank">📅 03:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98730">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDiMAboBWIrXZpTn76zTQltUvXmSDM5z4-TXat077flw_BZTQVyiYSYpEDKbFr2xZAz-_SCJTGzO6rwbJ5kAr12idKs43UkbCvA8eFCosmFTKdR2AzCASV3mrd2OqsUZm0Hu2zuZ-bXAvDXNrMszwGTg-oA4SLxf7sSbQarepnZo1HeAcUK7Vc1IUnXccfPTdI_kCT0kzML4zm-xjUloxZsiVg-bZYrBQOR0Enyjqmz6hfohZTI_vedkh4UHwF5nKNN9vE3yXWC_Ry9ygDuPMLqheULQEM_ogalXUlyN5xClYbWwhbxnSltrWvd45LdMylmmg0Rlj2nw6m7ZFMxqkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
مقایسه عملکرد هالند و امباپه در تیم‌ملی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98730" target="_blank">📅 03:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98729">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98729" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mANrtYm_nNXXz-LPpqonBs5-GfpcGKX57nFsXnoHbwIiKF2snsLlP1ypYykKOiuKiFn381mEL0jJ7J22vBD01fLCyGypKqlSTD8sw50T5AZwzz4erXKGRIAJCtl2eFqmynqkV4d-IQM0Mc0j_IvXpGSUh4icyd5w0nRH2EHd8YgghaFkzkW3pcK1W2ttcshaB02Tw9j9QehEpK8Ncqpq5jl5GcrUQ5i2BJbRiEqfRnc5eN6Pvy-S3cyRy41TztCgrTohg8bn8Caz97ndcEteWtNNNSJATdRkHuehkzx_8JxYzi2lDX2aZ9KPslfDORb5rZm2JvfGDp0eTgbkmprIoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98727" target="_blank">📅 03:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce0afd819.mp4?token=IRAKIRyzxtvoItmKN6bSnxyEfC3QJGDBV5ycmkTp5Y4LR-rDKxO3vsmvF9JXV0nKAN74mzLq6pZmu4BWx06iR71ewzTBqIZSN2ngJNMuNua48DuXDFpsokhi6oTijaqZedufFrS-sQCIn3Fivct5lpZ9mlgn9Xyyxy1K0zdH5dy8l1a5QfD7G1Lbg8e0mxrzpJUvwgHH9fq0M4GZA_5KtyskKyI2Cu_WhlIrZdgIWVFnkGN2amVnky-GnqOdfdJ8FSypaqqxet3Y3sfOk4Mmr11U8jw48fUxfG4BwDrY47QI55syCUfiCFBJgI5cCmFYHSQ2ZggbFjSPeNDKTeQkyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های اسپید بعد حذف پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98726" target="_blank">📅 02:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuIOTmTgbIW65pfgADkF-jLohcpVo55bmc4bBtCIeQkj630krXd6H9C4RHtMcq4OSNW0YXLttuAuo_HEZs290KzVL73IfqiSV3ggzEO6OKK9haxlBydhVqYn9GlKH0Xpx36eCO0ZAzRiMkVyQY9IWsv10YVZB2wCgScH03gqk-Rfvb5IT5p3vDc098MULSa853PfYnp_AQUtUW_Mlshk7K69V430Ydl-nCT-6tARyumuaMGauK6KY1jTRcxNbtS9Fu7m7JSkqZlIopC0_8f2kyl97M_6ZsVZlYB8QCGOZBj84kBfW4OpqV3PdG1dxmCNocVXkn78JZbnPxd52qXyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn5bXCM2HLxteAfILY9fIRqe7nl37FoZYlY_uNBhKS6T_wzPh-HPaNu2Zo_rJOHn8ka5H7yoPL6YE1w0xmFukIlalDlnTZdatmlfAk9EgviWeNoTjBfeh9Mn9K8I6G5dlaZevJ-MQ1e8Zd1rJvkSi84WB9nJeCsyfSxCIlB_mU4SP5qWbjrtTVnPZKK5DMlz0_FoCz9MRU__KAAN4zO7gHCjt0JJ7kZbe9D_R6jQE7HJ5GYjDN44bMgcAgiS36YUA6UjJkEJSvIeaGIHaioU5LB6pf5J_VL64D9ZFQv126tVEIEykUaNcQJqK5sA71cbuZwlAmuMUUPzfiDGBrn7bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">-
First dance.
🫣
- Last dance.
🤕
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98724" target="_blank">📅 02:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
رونالدو: از فردا در آغوش جورجینا خواهم بود و با فرزندانمان تعطیلات را با لذت و آرامش پیگیری خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98723" target="_blank">📅 02:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🔥
👀
#فوووووری از جورجینا بعد از بازی:   برای امشب و تعطیلات تابستانی برنامه ویژه‌ای برای ریکاوری ذهنی و جسمی همسرم کریستیانو دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98722" target="_blank">📅 02:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98721" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98718">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoG1XxNRATTLPPEqz3ZcULpK1eJR24v9t_Atb-PS-e5_kXR2xRY1wkYN-p6FouaEtl473dFQ-KT8IFc5iMf-YD7Rdibxjl0ZdMNYCISRIpGPk_LMdinnhDhf5zJVJdIF0bF9N59MyjUE88sIpmLjnvRQiXNsEOcpSI4JqA790KMHI7cQ1WMi19_j1JwyzO2R8wj-CLpwVOlFhgeFm8Q9XhByyjQ31T6gHbQ6-jOE0hqUsObGgVEszJykFqbZBe8iDDk0zUvFTAIIT2gV64mgOVTMpBaM-VFV9sTZnJI9XCJVvaa0YVP3w2zLb2tP4P0zvN_De_uS3kcubPWo6ILNFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇧🇪
ترکیب تیم‌های بلژیک و آمریکا با حضور ثابت بالوگون بازیکن جنجالی آمریکایی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/98718" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98717">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98717" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98716">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:  ‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."  "زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98716" target="_blank">📅 02:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98715">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgEI8hBkJOinUw3GK30zzAb6csi8NWTK3kVKJILZa-BzSvU3KNDIZyu8zkEQnruset927LL8p-1zch8FAHrN1oYJ9OCscfPUQneyrjE3HlGYqVmTTUevTGp_lLbFZg33N1awB3MCDYgqTPscs55vLdawjCWevim0kGh581b1pjjT8mdfxBpY-BUgBfQCD0a5EK1YaWzGnA1cXkZbClCxLXYmyMA-wKPfNbg5Y2VYmivI7t0iYhB6gdLaXOIN7HmpUoCM2-sXxBlSuJ-sVg10xIXd7WVmQmhYd5oEiB2lFjpNRFOZMbCAMue8eH-sJD2NlhjHovSjCOkka-KkQAyOcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
اسطوره، کریستیانو رونالدو:
‏"من ناراحت هستم، اما تمام تلاشم را کردم. من با آرامش خداحافظی می‌کنم؛ این آخرین جام جهانی من بود و حالا باید فکر کنم، با خانواده‌ام باشم و به زندگی‌ام ادامه دهم."
"زندگی ادامه دارد، و فردا یک روز جدید است. بزرگترین پیروزی من با تیم ملی در سال 2016، با قهرمانی در یورو بود. برای من، این مساوی جام جهانی بود."
🥶
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/98715" target="_blank">📅 01:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98714">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1tsTqAW0Hncl2p9ohYF-OGPRxOPqZEK2VQ2kWC6e6DhliZZ3dFbJemXz0cWyIxNA34t5JxwXrwPkmiQpxdz31fPczxYaH2eoWxzCkY90Ef9o2rjRtpRPr7AdH40On4TerR9fytQWvsCZpU0Ztt9Q37YHILbQmEJhv0C9fQM3nYmulzpcsK3Zzho61igLkPnmj3Nt6jnS7MGved3cWa4K9SqrSPRStE_myO3p0OdArMOm2BupoAtRP76O1n9qlSaa5-Lh23ZhtsN2CeZCPdFKwF8QCr5uXBDVKuXVG3iF4zMyI0XpmOlqAAlcba57NxE8QpWONFMD99-RMgvM2x6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خورخه ژسوس گزینه اصلی جانشینی روبرتو مارتینز در تیم ملی پرتغال است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/98714" target="_blank">📅 01:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98713">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhz1-QMAS4YilNnn51xvHdETJT4_GKxpFJc7KsCSvffnFVsNkL95m8Oc3_pTI3iTXYbUkaraQbiKT4x_DO5aKc_ab8lRdra6jWQRqbssxm1b2UFnbA6pW_5erAvVvzrbR28h9jo_RLS_FYyGxFb-p6seTKhH1W4AP7nyYreXTSEAFSRaWerM7CsYjKLU60gg2cUAIzKeaNruiuYA3la8SR9pPw5ksW5h3quWp0pbxQwU5dEcMlgwnRYRRhKXeUWKYGN7jCzHSKq-StWEiGpaO1K7dlRo5cUn18AUsONX9Vq37VMckZZxd8DHwN8DUPKFjDrLK8sP8gsqB0f2Se-rOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
کسشر و خیانت‌کار اگه قاب بود:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98713" target="_blank">📅 01:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98712">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOmWgwO3U2FvOu9BiRVtEbufMmzXdKE9IqSP40qm3eOYDV61p6pOb7iUKBiyoM9VTHyfFNSPQoMIooMph_pV0LZpY8Mqj7zG2xcXuiqzVNNGWh-v2DXrECJA-t1SLe-i8SeVXifsQuX5Z6kXADnb403XkiWw2_Tw4NrnNBoM4aDhHrCwsVe9-hoXZcB5puLCUkYciwWhgv5nFxC6mzUE4c_OCoU8Lc8NvhrXUAVHYuwdsig6jCi_hnfu-F5qvd-8UnlpqKPStnQ5Kgw1F8Y81Bl_wWx0itUJAxrC2z1J0yStgio1aKEZPKmbO9RBC4V3c155GZ-ZWO5AGWJDdllkYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
👀
🙂
ژست لامین‌یامال در رختکن اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98712" target="_blank">📅 01:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98711">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmIo-10Dw-vksksFuyaoowN_f1SXQcnJsgFK49OLrwnfVUUdAZhTexkCTjnjytE2J7_3tb0l7_RlB7gbyGVnPxWimdVz6SDqOsrnu4Fhwr5EoeB1KhB6cp_6lEj-a5fa4BgxkChTps0WMybb2flE8W4Zg1c6j2QaO13xHxVQcG0PfELFEW8TEmJh-BQVyoMJnvZJkeikFBZrVaUCl-C9-vrC1oLy2rX82KTfLKNiKzIq5tYfML5mmdYtd0TewC2EBT5QFjv1GtT9Qt4HMsfXrvDGwZICxCckoMa-wrI5wv5-Kl_P-CaCyD_yK5dSZ56smFzQvQ-ax0gcvHHgGVXvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی؛ حریف اسپانیا تا ساعاتی دیگر مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98711" target="_blank">📅 01:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98710">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejgppp6awqSCnew2O3XaZf-FZ3-1F1XkHYpMpOzEo7LV2nMilYNltTDw-P-TS22WHUO8MuGBvzHdRecTDOgNi4T0rz4ejAsQdNMnM_ZnrRhRzjwDuOQevSWBvpsUWy0WZtzxGbuzvrG68p1XX_zbXlMnh-PXeTO44cpiVt1bhLE72YDc80zDo3XDgIak4OcsWUyf706dGMQN4SR6BKEJHKAhP6vZOrJajfBk3M5GA5ho5KLNaQOLAslRR6eHg56PGDBlKFe-aVIdcuUVt1WiHdHTBJ05OwYsUpciaCBWpFs31Pkbnpid4EyDVcq50ICgDm3ZkxpQg8Z_tR-pW-znAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
پرتغال قبل کریستیانو
🇵🇹
:
❌
در 3 دوره از 17 جام جهانی شرکت کرده است.
❌
در 3 دوره از 11 مسابقات یورو شرکت کرده است.
❌
0 قهرمانی.
📊
• پرتغال با کریستیانو
🇵🇹
:
✅
در 6 دوره از 6 جام جهانی شرکت کرده است.
✅
در 6 دوره از 6 مسابقات یورو شرکت کرده است.
✅
قهرمان یورو
🏆
.
✅
قهرمان لیگ ملت‌های اروپا
🏆
✅
قهرمان لیگ ملت‌های اروپا
🏆
— پرتغال بدون کریستیانو، هیچ چیز نیست
🐐
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98710" target="_blank">📅 01:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98709">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98709" target="_blank">📅 01:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98708">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxGp_kOm5zDUcWmjvETW474QzJtq6vKTPEAKInEAZty-N5V7pQK4ptou8AIBfjsn5vPO3ejBHwbHwMTAEI7GUXP8HVRs19lDDWlBwOm7Guh0QCeSZ9QkH4n9ovy2N9lV1yUqFZTVzF-LCBUQ_6o3y9ZL6fYX8o1d5aVaHD42LXLa9IAjof0UUeAZefAEVQd8mEjj5pFUYDMFdbZkpnL6bmsPMH0xjsu7IPIGr9SaM32D5cteMfhY76e0mwmJOwYFh0Hkv1RYI281yLlZRRoBD0OMV65Tq6eZTQt8znnpYhPG8i6-IFqW0H0Dy7MKMVdGo0tyA3mNOHMkghM-s_9rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🏆
واقعیتی که دنیای فوتبال دیدند اما بازیکنان بی‌غیرت پرتغال تکذیب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98708" target="_blank">📅 01:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98707">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxT85dFW5gi6UQwAeKIeiBgsAUeBPvZ48IKe7kKyL6UcseQ4IzVmWjZnpUXEIHoKH5NV5uCEoNPaWT02qEdcCONZLZSsEWFlBDAtNQK7YJnU5pU0zqkNaxpYH-Bol6OF-alA2PiO7q5hBhhfaopIIsOA9WR87onKmouRh_mRH00xxqCsfHE1sUylOFSYEYwx5JmgFpvyDpKd5TjpCunz6r3ehPYfxtJzE8roTtfrsWyMqgEx5fb0ps6wKRvvO6uSnpYOv7saAFw_i189I-XCT7_e-gofrTwru0j4YL1AuOQa4v29TQ_3ehVXqte-F1Pa1a-IoI2xw1aeZnc0UTc43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
بیانیه فرانس‌فوتبال برای رونالدو: - از شما برای خاطرات بی‌نهایتی که به ما دادید، سپاسگزاریم. میراث شما و پنج جایزه توپ طلایی‌تان، ابدی هستند.
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98707" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98706">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UePB9sx1-VgCjbYX0QvSvUMpITpRpHhU1hhhfZCAEdk5Ctamh2dxKp5a_0QIYoGIXy7j20Q2OzN14EAijqGetpBtwZltQXIFUP6Ch_V713qPOud5X89C8vVccPrA3-CNX_CyZXC8Dyt0DTdhK4EwlzHspk98I81XVGnHE0zgZheqR-QYZqX2qn3VExSPCy_WoAtbrKIDrOQPE7ukQFB6XyyJGEfHIe3iYWN6Cb6hpvbk1GWFAhS6_OOBCjWE0x1sy6ZdA9gq594BJkECpc4dgKPkgQ2K58Vdkjckh1R0AJsnpn4PB2WdtVe5VX_EezvGKfZhgE5IBWbewnZMpFN3fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مارتینز از تیم ملی پرتغال جدا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/98706" target="_blank">📅 01:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98705">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153aac5990.mp4?token=OT7mR_eZ-SrmlFCSVSspXXU3F8LPH98ykw7wpGRb2DuUwafzl3eX7aPVvUiPwErMuYgeUAvFSuYXn02i-2fUI2-xSBq1ICtdq-h-H-LA8woz6SUHc4bYjqSa4mYmnxt6-CeIiVC5iR3H-Q6a1zeP_tkDL_QESu1yISJvRVrHJ1QApTWJt-Q-NERjTuRuslqL1bLtdlj8bEp4QHTmNLx3X2JmyAxvWIV4GbCYV6wFE6h8CD0fjSdCmP2f3KYV9fGn99iafM2HF4fMEXWlFXAWOAqAdgAuSKr05ptnBKe8VcO-8pnjjZlmtXXmIFPe3wL2xTygxoeH-nbBo5qOQlKmjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153aac5990.mp4?token=OT7mR_eZ-SrmlFCSVSspXXU3F8LPH98ykw7wpGRb2DuUwafzl3eX7aPVvUiPwErMuYgeUAvFSuYXn02i-2fUI2-xSBq1ICtdq-h-H-LA8woz6SUHc4bYjqSa4mYmnxt6-CeIiVC5iR3H-Q6a1zeP_tkDL_QESu1yISJvRVrHJ1QApTWJt-Q-NERjTuRuslqL1bLtdlj8bEp4QHTmNLx3X2JmyAxvWIV4GbCYV6wFE6h8CD0fjSdCmP2f3KYV9fGn99iafM2HF4fMEXWlFXAWOAqAdgAuSKr05ptnBKe8VcO-8pnjjZlmtXXmIFPe3wL2xTygxoeH-nbBo5qOQlKmjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
💔
💔
▶️
عادل فردوسی‌پور کاری کرد که امشب هر فوتبال دوستی بابت رونالدو اشک بریزه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/98705" target="_blank">📅 01:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98704">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=LYtbd6DURgk2EqtglDyGznWPZTsdE3jJP3kbNnA7TGjK3QiHg8KE2HMWrImrl_TCd5xKhYAeVe8nLkCPr9Fk6x9JqCHgJtRNcxjRos20FymnH1EDxnDhL9Py7ziy86tt3zD2XRNzxfPeBSUgpl3FCLfb9F9it5A-qDg8LOn-PnL7qAsh2VQOPlWT9f3ZRhYx86htwB6K4xIpP0riBC1hrQRye9PNyGdVEvMhY2ZnAsxS3MjXSA4qSqHBfqH7_HB4I3LJo2D6t4vOCc2-SHHti1xNB0x32CEvibzqMXAcqW9LFItm5Ta_JSPeZlD9l9IgiYkUmmwuap7JTiyj0_doWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cc0463de5.mp4?token=LYtbd6DURgk2EqtglDyGznWPZTsdE3jJP3kbNnA7TGjK3QiHg8KE2HMWrImrl_TCd5xKhYAeVe8nLkCPr9Fk6x9JqCHgJtRNcxjRos20FymnH1EDxnDhL9Py7ziy86tt3zD2XRNzxfPeBSUgpl3FCLfb9F9it5A-qDg8LOn-PnL7qAsh2VQOPlWT9f3ZRhYx86htwB6K4xIpP0riBC1hrQRye9PNyGdVEvMhY2ZnAsxS3MjXSA4qSqHBfqH7_HB4I3LJo2D6t4vOCc2-SHHti1xNB0x32CEvibzqMXAcqW9LFItm5Ta_JSPeZlD9l9IgiYkUmmwuap7JTiyj0_doWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حرف‌های رونالدو قبل بازی: شاید این آخرین جام جهانی‌ام باشد، اما امیدوارم این‌طور نشود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98704" target="_blank">📅 01:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98703">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZRSsvhgwCya1gYhl-HBAJB4DNlPNYT4CGLXcRlNRpnCdBpzh3eI0cIUDafXtMQo5PmpJJusd9VJhPEYYa-SQe0zobU6Pe9aRxcTLJNi_YRj7Kq6V08VLo29YFLFIqzKQIPsWhy3DDedq0TZ-A27SXp1hoSq2ut71_HmHv316phN0T7iIlnKdcBDaddIyvRt9L0zXpwr8PraBtpCsYIF6iHAQ6Ic83d59d8OsYnLMjrMe0o3euMzUiRhxCUoC5uYkhEO8KBQWT1RHWKtz-BObxWij4dzsGME1p1g2gHoAKQTqv5Vk2Gp_AZwfPs9ljXQAeI-meQFffgVazuim8E5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گل میکل مرینو به پرتغال ، اولین گل اسپانیا در مرحله یک هشتم نهایی جام جهانی پس از گل داوید ویا به پرتغال در سال 2010 است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/98703" target="_blank">📅 01:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98702">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICvqkBOXgfUZZ-teFvqO8-QCPWcXIKyrKkQfYSXTU-ztkhE1NgQ-qq4Ypo9Gks2VGK-y0BOI0ZrIc_zkFU7OYqrj6xBqUJ1csdQsxr_bav5QFsJW4laPwkQIG91tAZH674R2IUnU6Q_DLKosp36tBBsG8j5vUb7GFtlPDIuwSKIr254AUjEDkTtwr6dLy8uViugPBYBnyCQGJXimQJRh54-AuWsbTWt_v5ItxzWvWj7PCh6sQFithfXek-jp3nEuNk6QnNdsn8tpFyXtOTjzL4_vhuaT5aK4Ntik1Thr_kpFa1GmqaJBgEaRHyJP4CF3QgweKQGqp6RGMJt66hjrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
♥️
کاتیا آویرو (خواهر کریستیانو):
سر بلند بدار، برادرم.
تاج تو هرگز نخواهد افتاد.
تو یک غول هستی، تو سرنوشت‌مند و انتخاب شده‌ای.
تو فوق‌العاده هستی.
از تو برای همه چیز سپاسگزارم.
از تو برای خیلی چیزها سپاسگزارم.
از تو برای رویاها سپاسگزارم.
از تو برای شادی‌ها سپاسگزارم.
از تو میلیون‌ها بار سپاسگزارم.
تا ابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98702" target="_blank">📅 01:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98701">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ijQGrZPt1lyQ5tgTT-xUlRSX2GfH_wNkuVxOv06ZkxQZ0mTn61jhjgMXpEen8HYbaG0HpciorRNLJMAlDCXsQgtmfNPLeBWUNpX4cgZzIIRiTcxyIzYDH2S0VUP7RBevWgTruAVQmezgwgJ3wk1jS4BgYCCKSqjxuolTZzFq7EKiNsHHsR4B3oMbtV4O3M2KlaMiOZJAu41CHIHFjhja06Ak98WPlaMY6FwrsmiGBb4hIPam2-NW7UMCm2BMxc211SebqTmFW0HRcSHDjlkAo8r_jz7JIc9ir2pPUnmhsPmJM5loy_5vH2K32mt3LQFkby2Wcv6N-Zkz-lVwOzFiJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج بازی پنج کلین‌شیت
✅
خانم ها و آقایان معرفی میکنم بهترین مدافع فعلی جهان پا پا پائو کوبارسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98701" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98700">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCV8oDN_ZIoFci6gSBUNZWK0JlAPY_1sxIJKVLbUb-cLKCcjRkSWm89RgrlluZ1LwJqlJnrxDRHlmlOYDT6wtXDC6gi1mFmkdfz2QIiJ3CMo54w8A8bStqKOluV8_J6BOrKbCywqUdAvXi2k38RNhxIG0bZBZTBBNaONedQDXglorNFT5L7zqjNL5meZwemvgMV6BKQ0O88mG-Ifnp-neOfKDfBF-Xli1l76Lbloi62CbZVHOSyOCz8Loc2rIaRsmaMgbXvSuGuUdGIVP-9YXRw0TsUbnWHD5WGjC0tuaULpt5ZZWi1bCvY-5tqEYez-BG7LABEXFCAOUHxsiLc66w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🎙️
رودری [
🇪🇸
] :
"از برناردو سیلوا بابت تمسخر کردنش به خاطر از دست دادن فرصت در آخر بازی، عذرخواهی می‌کنم. اشتباه من بود."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98700" target="_blank">📅 01:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFy4OV8hGsgI-1g-YUQcn9UEOK1yGkIHX9ph8qW2YUUFok_k_k0uOiOwlkoLmglnGB-EI7YEGzjDeXiiDg47WU_s4qbwnk033k-CMYvaXSgEBbENeOIzYeGLNkJELalSJJfRSftwUx5dr0_vXffL84HWirH9oIfnRWOBR5WiYl0ZVhWIxJpiOL0dOIb6ke31rvc1pVhTqlmOJJvBiZM0LX6bKQPdBHHk_GgweeKYMHgRWtL2gw1OpO_mTSrTYVx4xk8-RLTfMXcj2FtOd5GB97dRFBD8TYUdvY49wSCyExe783iBJ6AqnkM1ZDrVu0mWojgSMhdFW9lGFY2mgK5FNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
و تنها یک‌اسطوره همچنان باقی‌مانده؛ آیا تاریخ را رقم خواهد زد؟ برای گرفتن پاسخ کمتر از ۲۴ ساعت صبوری میکنیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98699" target="_blank">📅 01:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این جام هم مثل جام جهانی ۲۰۲۲ به کام بارسایی هاست
😉
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98698" target="_blank">📅 01:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/98697" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXjjSkT7I1HvigLTgWtF5ODDcbzDQ0kXjq-2FMgek6quMWB4elKhQrgl-gey4zKweXGpE7wCptbLW9uCsJKrH6OO8TxHDHfBH142K8YqNgVePyl26J3ANWZ6_y33ksDM-Xa1gzzRIKKQvd0gvmGi7cDfAyCQQBOZg-yWRvr-EF5FoEVqgpNJUL-PfDPjSrv2OeRYCBXw-6M1p5v1-HoUjqkm_Adl2uZc7aVTwxi2HutaWNpIbVuQkPvYR0LLR0RPFLUc6MEYcXeeNhyNp9y1Ob0LOe-vdAaFjyx1EHWwx8vvqNtO3UlL_pEy6B28CQNoTgf0NLMaQtX_KY-atoapLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇵🇹
سجده شکر مدافع پرتغالی‌ها پس از حذف شدن از مسابقات جام‌جهانی
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/Futball180TV/98696" target="_blank">📅 01:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIA-QoAV1vFq65aHd8iHlnYhbaJOg8blU6qDboidsWrK7yLtJkqB2pNDUlPR9bw2LnSEek8_-19kXOSBhDiaepqDRKI0yyRlGGj-inBQPLc9N9JgVyMhAOjW0k1AeJGoyYVV5cJDCSYrQeazVTyjDj6ixl-0RnDwWx8xFAT9Wo7wTxpr1GNOtbw88SOSLjEY_-newoEUZ4vbK8pZ2fHP5Kf-H-yHtjkXMp9c0FywdttXKWrgm-wazyytZWzvyZBLvDh8he1Xt7dRCwMCwX6WSSa1hCCRAjx2gLRPPwDFslGgQiTWuZgebMxSS3KwOSw9053WdteSUzDMJLReuVQzPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
تمسخر پرتغالی‌ها توسط مرینو
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98695" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UK6feyj0fp-j6NIoKApJ6vD6WeiMo_bCvGzHrtz-FR6nFnoxLffRxUdFZQhq3aEkpVWpS0wi9DOpHaaZF0NCetZSxQsUS34J5QiCZ23fLrS9nXi0P48Xn56IlxHfPYUpwkFIrABUjWFq4DFnCIz0AjPeM1sxbdyWwqThNQkz88KG0RUhIk5miWGjIRDzwkXtlsgy92jc60oZ08PQLOXcJX3znJb346D-nk0bX4Z0uX1-50b68qG_jb5dIKWV6n3ziMEr3lfA_LiwqE7limM_NV1g0ENpdRImcuAtnArGnwno2t6d7i2S7J8yl_pTypiYNlLALD2FEW_ywu7axtX3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
تیم ملی اسپانیا، اولین تیمی در تاریخ جام جهانی است که ۶ بازی متوالی را بدون گل خورده به پایان رسانده است:
🇲🇦
مقابل مراکش.
🇨🇻
مقابل کیپ ورد.
🇸🇦
مقابل عربستان سعودی.
🇵🇾
مقابل اروگوئه.
🇦🇹
مقابل اتریش.
🇵🇹
مقابل پرتغال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/98694" target="_blank">📅 00:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=p2lEVxzqIyq8p3X9Vb5dWqRKvIy60mpdzvliyAl5lJzLYY1ABePAAoNL6AtOyXmKLDHf43LXozW__k_EVGFEYn1q9W-w2iQGdbSmPjIgoO9AN5mFK5N-1nAzckBfYZ1-nMFw38PMRW1E-4MT7-Bb5ACNi6UYj0yQVQgPmd7QIwvSVhUx8ZIsYgIvRgNd7Bx9tEwnWQcxDHZ4MwGxOKAhRTiwT-PnI34Y9UYTKxY4x1dOHx9UOvNDydtlage0LNAQyqyz18XO2lN47bbaJhmo9468PTEb3SqizMOOE7dctQyIM3nGVP5IO58qpnyqYvohxidabuMCd9IUjoim_x1pTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba77c1d49.mp4?token=p2lEVxzqIyq8p3X9Vb5dWqRKvIy60mpdzvliyAl5lJzLYY1ABePAAoNL6AtOyXmKLDHf43LXozW__k_EVGFEYn1q9W-w2iQGdbSmPjIgoO9AN5mFK5N-1nAzckBfYZ1-nMFw38PMRW1E-4MT7-Bb5ACNi6UYj0yQVQgPmd7QIwvSVhUx8ZIsYgIvRgNd7Bx9tEwnWQcxDHZ4MwGxOKAhRTiwT-PnI34Y9UYTKxY4x1dOHx9UOvNDydtlage0LNAQyqyz18XO2lN47bbaJhmo9468PTEb3SqizMOOE7dctQyIM3nGVP5IO58qpnyqYvohxidabuMCd9IUjoim_x1pTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
ادامه گریه‌های رونالدو در مسیر رختکن پرتغال
؛ واقعا غم انگیزه
😞
😞
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/98693" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98692">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoVi-_8qcjdANf0b-EWEndMoYgibzBHNdoOOksoQEGzzFCpcsjOcVhYGjoB9h1AS0qd9dluLQazLpwWVuRWYLYQEHdznN1kQAM37ot3Emb7HvgC4H3IyEWPC1O2XHxx8cm-RzZ8b4ipnrBC1A6t7WYGjSOyOYQi3nXMwtdttMYZIp0FKrjEPgSkQ4MN_scDyDgo-hBpPLw5wNPqLjmTp4B6UVORUL3s1VrbkxPaAm43HhzymbAMXcPgceK8bvwOVLCoxTFtam7O1zV3YVdPVhsglkxNwPlM4-64_sZAcHEAhDPB7szRs-gr7DLm36kkwNf6Syt9Dt-3KLQ5d_GIVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید هم یه گوشه کز کرده و فقط گریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/Futball180TV/98692" target="_blank">📅 00:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98691">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i7sS-YQdHAuOCd2U34OBA39EXScBOfvQtP3fjsc800yxzoX6cKN-Y3ZErix4H9tGKLL8NJNZR3qz7ShSC1C1QKB6n2u1owcL55wn478VhlSfe1KnuNTyhuqsq2THA7XfpoerZv5h2Z9xKFLO_G8saveQYm6Mf8DaxiPAHA0qvNvdmQ_Wlt1oHAypv_R2wWO_EK-xrgYSyI-3-fD6Ch1QEUzruzf0nCGcciS0zjOo0XfWnULqRfGwh0eK1Wv5zRQVFRZtboGM4A_HcYw38iyXzNMnVj_3b5C27ZD831ZiAe3cYYGao5CTglAILl5jZM-60pYwx0mfLVKDtfxwnpBHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
📊
🇵🇹
مسیر اسطوره، کریستیانو رونالدو در تاریخ جام‌های جهانی:
‏•
2006: حذف از نیمه‌نهایی.
❌
‏• 2010: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2014: حذف از مرحله گروهی.
❌
‏• 2018: حذف از مرحله یک‌هشتم نهایی.
❌
‏• 2022: حذف از مرحله یک‌چهارم نهایی.
❌
‏• 2026: حذف از مرحله یک‌هشتم نهایی.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/98691" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98690">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
‼️
⚠️
🇵🇹
روبرتو مارتینز سرمربی کسخل پرتغال: این بهترین بازی تیمم در جام‌جهانی بود و اگر بدشانس نبودیم به راحتی برنده می‌شدیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/98690" target="_blank">📅 00:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98689">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/98689" target="_blank">📅 00:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=DYcMUIwTOrLLMceKDqgkKqi0kwvBWThat5yp9-l7PGGh5FgK26_P9NyRMisLrxGR7QFjOuKfTT1y-fHN5i1N6jgbKZpg75JZOng2BX7-g8JSTtbagYMiahK_1Zwv0UEEZyfaovFq1aQRLviOPDIyzEGmR4s3e0gUdo5JTRVNK7dqdSXc843LrROXzez93XUKcsinPbAEcgiByh1xTQ5AvVYr8UFjeuZOTXikAMVDBeY-8O37F2aTofIdoKtKj2nxwqTujb-AKQJ05uhryWSeeceDB8rYFean2daRq31wdMZc5c8ZKUg5HIHfggATmRv3wtienoxWjpecmQ5mJFJ6woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=DYcMUIwTOrLLMceKDqgkKqi0kwvBWThat5yp9-l7PGGh5FgK26_P9NyRMisLrxGR7QFjOuKfTT1y-fHN5i1N6jgbKZpg75JZOng2BX7-g8JSTtbagYMiahK_1Zwv0UEEZyfaovFq1aQRLviOPDIyzEGmR4s3e0gUdo5JTRVNK7dqdSXc843LrROXzez93XUKcsinPbAEcgiByh1xTQ5AvVYr8UFjeuZOTXikAMVDBeY-8O37F2aTofIdoKtKj2nxwqTujb-AKQJ05uhryWSeeceDB8rYFean2daRq31wdMZc5c8ZKUg5HIHfggATmRv3wtienoxWjpecmQ5mJFJ6woi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
😞
سپاس‌بابت خلق تمام لحظات بی‌نظیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/Futball180TV/98688" target="_blank">📅 00:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeHeOCJ8FzDu5twIeZWNOk2GUI50ZahhDcBUcvW798PxiACiMKgYEH542KfPqLPWR5Ttn8TvSGBEDR8DnJtbXrx2Iap7ORDa5WfFAAMXV-evzq1Vxc9k8JLrqZ0OVw7nT3W92ePW7QBH2N6ZKOXBki_-usQoNe7k1t6YF2wjPHPzIw2FlD0I-uZXvMwnbhh1V91YlkrsCFcC8uidgXTFZ3i9APkrH9JfN5uWE_OboUAHAbkCpoKa_AOKYx1bvi3Q3oHALDsVHwaqwqJg38PBeihVz4NwIVTL_u5uNQqtTH_zZmPEJZHGvLXan1Y_KzBqnQQYVdz60G6EPgWg00p-IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🏆
خلاصه جام‌جهانی ۲۰۲۶ در یک‌نگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/98687" target="_blank">📅 00:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8JHX8wf0zcL4X8JmGc9fJlfFJhZJRdrYgPbtvV8-6x0ivbJA-6s9nHN4K7udwcteFBVNuQdJ2AQbAGdBueQLHkgSlJ7lAMHZw_BypqEKtAiliTK6kepo-ljH7r3ONmiPYaqfcyOWVWSK7tOIKocaQ0YXa02x29mooMcMxeq5DxOgjxbovnNYSUPPw-hWa0PE4Paa6Y5XUt2NiFpEmhDAdtgu1okCULTnm_iFdCLZiJ1W8NEj-bS_Ac0NsM4h3Yimn7btMVxJuv0TUo35vzidU9-jb97s7BWjAkykp-CWf66HlB8_AZO2FsYzv4PScFZzEC8aQ9FdDKpqnIQQkcELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
👑
👑
🔥
🔥
🔥
۱۸ سالگی و اولین حضور در ¼نهایی جام‌جهانی در اولین تجربه جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/98686" target="_blank">📅 00:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98685" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98684">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ib2GmXZfzF_IDS4JtgPhh0Ua_xESWc3z-JLtvC4-w6S30X-GA0iFaHKdMOcgX9x_vPwwBQDf2w0DwtvDzVdMAltbkCdvjSZSUC9XBcRkh4Bq-QAM50ZzudCsv4AH9IS0-uMk_CrMM3DgqFGep5FN1qvG0lXSjLRc4xKyxb_QZ5SZ1YWWWqPDXV-_boaoHGKVepFvGfTsG1sj5NcE4siwu3-SGW3VOrWYZkIMrm8xjE6z9f6ekOGfZovYfrdpfFxPXNq9PAHD0dUgucBGxzs_8RAHDR0hYXoTsfE-tmV0Y2wVEjWirK8921bvuMbgRKGDEpmglqnu1EusTXHZ3ZgPbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
🇵🇹
تواضع اسطوره و عذرخواهی از پرتغالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/Futball180TV/98684" target="_blank">📅 00:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98683">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5IDFDQAUpoI7eyWm355ND7gE4VtE7FTXUpmlPggnFIpnrLjKv9YvTYv5G2DAN5KWJyF4mKksrocnaiw3HKE37FndP_OXb0sYM3-kNLgW9sK75bmciSBhHKR9abmFGZMKyEhIKdH1ABiN0tjRFUKy0nmm8KJKZ3Crxuq9H28JsvfRrHsIZRMQKv-vSfVoZyknQkqanYdT5WNJgpK3_a5iVxIJEw9WCL6UwNn7mpOBitXVYYo1FI4XfWJzjvMsuwWOgMcsKCRz76TWY1A79Bl_TjStU3t6Hjzh-IKrSGTOQ2dxq8VRJnY4JynRkC3CVXsBFhUfQjEdtsknr1CurE_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
💔
💔
💔
بدرود کریس؛ تاریخ فوتبال پرتغال بعدها حسرت داشتن چنین بازیکنی رو خواهد خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/Futball180TV/98683" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/98682" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ichWi9ZBB56zSVj0SIfh4sizev-mp1e4_Ytpw0TEDQnGbNwrTJvD3G3_aV3XpQM-STJzMgp5ORKEOfvJyhuwTQ-VKhFMiSL0ZMkTwZ8K6vDvJTvQtAci1jjumndwg-NdrYC57Hb-dKJFrPKMq5qMEDpd9eqe55Y2L5c785Hq8_HR0sX3-YSSeH4O_9J-97wEHR73CeDlSFVnYR-Lxm2XeE0m0Mt4nQombBLFmfcdAkD_Kh__au8_EmN9kSe813SDZj7EyOlRsjJEe3pcI-Chz0u1TZftYAdCQNFneqhrm603BPdZKrbK727Nyy-xQvRFpxunToRfrK2TvVXnalOvdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/98681" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JePEoTgXcYXWjc4jMdGn6Xyomalg78EJoxnzJ_Q9qTbENP_MIJcgXfs-etuShjvR8vAULdLUNGUYZUNiXPzi4uvmdzy_DfBUDjNsjGdLbzXSKi4ZInFOgk6tTTUu7hpZed8wC4apR8n3qm9QErYtcj_oE_KaWC9uSfKYcN9GZE09EOemWyb9Srwrgv9bJtbMFSfUTYbFnpgEYCsms0B1Rd82bTle6Ds3vn5eR_QcRwGdmVPQDl193zy3ehm9TEydDaGqS3a9KqLe-v2YV9dMxIZqvrr1dyqcdwBDU0csgswZXugHBb-yqseHY8HSo_w0kTvOh9rs4OPpAD5nsPleOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و فوتبالی که همینقدر میتونه بی رحم باشه.
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/98680" target="_blank">📅 00:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWRCFWcp3YtSiPY48mZ145jsVhm3YvnDAQskNmk5X4oRdOQY7LxkLswKRCvm_-YxFlhzeE4Whd5_E-JOu9ehKf9CvkAFCYg2ZsdImst6ji3fOK8YXRqtf1dJ_GgnwrivpaGMgdmNOZ4UJcpb07b1LP43xo3sPGb6PPoAqOEs31QnaNxF-ZLwNiJLOUbex4h3Z29hragM88Ml4DzI0UW0_vT6c-d_NSjYGAgrygs5Nhu5DZsmZDZRqZMRnB92NmAiqdGPxLrVmYxDhaPqzd2tOQLWDb3AD-UpY_x-kVeeCkZTLP70YylDr54Y3tMD4GiXNkmc7q-82Qfk67Z9NQU4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
😔
اشک های رونالدو بعد از حذف پرتغال در مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/98679" target="_blank">📅 00:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b45fc1c41.mp4?token=dSmeqPR5RBsk3IWOjj0DhOMFeymA9rM10weApBpRgz7LUUNaZiJ4CiWiB3Y0sAODISB38Snmo1ywfQ9bkhUIZgnVSbnEstaJmPVVjzodiAI-j4dgft04knlrcyNLyVchqNIW0HhlqbZ2U9byMkJNI49mbWdzPrzQg388Tg5TJCeNkoNfzE_K4idprqHVY_O34thluy21W3vnCqmuipZZ6qfHhaxTi6dq0WNXdzm24m1r1m391XfBRovMb7M3vlJ1Ge57bkUFXvY5YnXXm4MN83Mwb1pyYpuB-G9GaiLyWIO_RoSp4Wn40Ig89Tpl5gTtM1zWyz4bWT27ro50saRmxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b45fc1c41.mp4?token=dSmeqPR5RBsk3IWOjj0DhOMFeymA9rM10weApBpRgz7LUUNaZiJ4CiWiB3Y0sAODISB38Snmo1ywfQ9bkhUIZgnVSbnEstaJmPVVjzodiAI-j4dgft04knlrcyNLyVchqNIW0HhlqbZ2U9byMkJNI49mbWdzPrzQg388Tg5TJCeNkoNfzE_K4idprqHVY_O34thluy21W3vnCqmuipZZ6qfHhaxTi6dq0WNXdzm24m1r1m391XfBRovMb7M3vlJ1Ge57bkUFXvY5YnXXm4MN83Mwb1pyYpuB-G9GaiLyWIO_RoSp4Wn40Ig89Tpl5gTtM1zWyz4bWT27ro50saRmxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
😔
اشک های رونالدو بعد از حذف پرتغال در مقابل اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/98678" target="_blank">📅 00:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jgjz58UkWLU4notsgU7i7vdgOHvvOg4BFQem--q25CV4qGSvmWRg7Bnw4yczWJIxc7KGNgoF3CsGXsC96c2YRDW4dhkW2rr-Xat5qHqC0EXdWa1gLgiMqDweKyKVjbJ-Qs9WdUsY4YFg0kJ3QVkAi4RuZ-hNVYiuNGrzkOrMDxr-s_j1dDt4sV1_cQu0dZWrjKQriPnS85knnGAqTt6mUgfh8VrrIX3Fkc_lfB5Gh0tYL78qa9t2-mJMgAodednCDvZ2mF6MdXdfpX5ByYEz6PikY4DYmtA80Pvd_vlout3hPv70HnAPFu_la4nMvSazojn91RrRzY4Wm5IAW212HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
دوتا کچل اما تفاوت زمین تا آسمون؛ یکی با تعویض بازیکناش ورقو برگردوند اون یکی با تاکتیک کیری باعث شد ۹۰ دقیقه رونالدو تو زمین راه بره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/98677" target="_blank">📅 00:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98676">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGWbUCUymtQMTYyHvuSACyATcTGmSqv6_83Wey6evWK_dyr2l2q8SLdOO_rp12CmNBOFGNDFsOtuC_14WRFjblpmgYvaYXSon1cnpg1rKz6H587ZBvjwHLoCvKy910JkR7NTRLw3LqGUSdFNRzG0MahTTKtgWAYoy-EIyRJy3xLE5ahPS83OsZC3tD9iOxKy8Lsby1SV1tPvQYZeyZW0-ofkV3SVOBidGx3ScDoRvTuFTYDSgmClFIZ2XvOQxPPXFnVdl1FJzeZqVkTsArRIY-tpES87EJeCG3GdylZ_DBUQrEaKebMMIqjeuZidZd3Z8sC1ozD6EdLR1TeXo_Fnjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔥
رودری بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98676" target="_blank">📅 00:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98674">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DOz2zBttrquQs8UH3VuWJ-E_xogL1wZ15FGoWge_5bjkt-qk4CjSi40pZDLAMu7MKV7XTQXZIRwa3DWSPKwmSLlwTy2HVrx4Xo5IXaZpo3DMCSNHZyJ83QRLrNvNamISMaF0YMNWULJ29oU3Mm_luv1NTsF294GLsiZo4TJCTLKJXfs2KylE4fiBbNTJlyMvS7FnaAqq2i_xkgSV5rgJIut1tA1iQ434j479NMcg_tWLUkDfzlhlKxzwRxSTJODv4e_o9Y6z9zeiCLmmNc3NLFVr1wmgFI_8M0-EWNiKd5kEMl_gq0sDMTliBTBH2VL_18vKO8mk3a1ssApD7usKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPKwZthQ7eVB1DSCh1mE_SKH1eU7bvc8xMEvEWoBL1uI1YmU1efvsyYy5t6I40J1MTMXCWs7s_6ysnhs2merQ3O0sOisTSfj2HQAu8dWAEBqhEYJiv9awYfnIC4BQFbDXaKq9ff-9AXzZxUeW20RbIlxNJcgmvBQ9b3FNWg37HHc2oE6qhb0j9baXiolCHhD28_GdmDZI70D-CjMXRwxmw5HrTkyJ28I8WKUpnmZGYMbsp9Fro9ioqOaqYkF7qsq01KFy6OZgEaCiekr4i47rIvLsrRKJvMMfX8jnYt7Ic3RwCk8mNKLj1SZLyu2eo1ZhIyTE89bZ65P9hQZrcHRDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
❌
و رویای رسیدن به قهرمانی جام جهانی که برای همیشه به پایان رسید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98674" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98673">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsJDfkA9s9AOQHfD9pr10PAS5shHNRRrQ6EknYKJBZlMJOOrEZn1-Y39npK5vbryUtLmNeo_PhgjKmql5XwkSnJMsz-TRos-iKbXUH7_S2T5l9RNXMa1hAUvlsshnjIAniSKNtocoEuA6mXDhYRPPq6_vTa6YCBIaDxigspzuwr58PgU-bjdLhtU8Y0e38zwnpcn1n-PVuHhLxLVaRqmiPGPP4LgHxQ2UXbimthaungq_fVOV2DOgs-7oiAtkl7B8wPW9LGj01G_F3XN_fUcRyRVqIKn_eX1DYdplQtxKLHbjLtv_XpNeEkVgrxp6AcAn9WzMYbnC8nrceY2yZ_CSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آغوش لامین‌یامال و کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98673" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98672">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4E17VrpTuSnXyCs4Y_iK3oanHzsKd6qEBGVFjIZDF_F49pdb4T0srxzRSBCTTjXljMnCBAIn3aajxImrRHbVHuND4-1rYY6PrI_RwOaLOxarZytA3DGPfRSxSLPYHYLF9im1f-4bOkoBZstiDp_5mu1ijSpVxsA3DEXsqJtJ22THPvn47ICY8l379ROOkMI4cLsr2dPS_1YWwSTUmxjRjT6r8QISWVcqDg_Cq9mrlWydMJVC4mgy4Jgniyyj_Y2UVje5ezqHVDDRYP5N2B29M3-DQPa1N_wTWnjKYbyRf5Fl4wok4-oX-Jn4Gj9A_A7xLkz9_mUBlN38h1d25ZBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😔
🚨
🚨
🚨
🚨
پایان عصر یک اسطوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98672" target="_blank">📅 00:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98671">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAaZSILiYoOxSgj5XHE2iip5JFVON7Hg54c-SMp2yd0ZYlWb2K4M1RLBocP2vvmM2ZqINRky4Wa9prp6rivTNyYqmSEzw0CfnqG3LU53qyv8KPpNIys_nuT7oqeOif1c2xzjGdctHow0rwte-TMT2iBCahE0dO4ootnr6TXZ0sMhr0GIAT2NEYUeFKcTP1sq1T8GBem-X0De1wBLPQCf9usLxethVHooM-99k3JrhrABakQyQQpHZD5SNEJDLyo-_SXGk84_-B_M02UNXyqcmYtzq4THcjUTV0ZZC7dGNHLmszKVYCRm0JJKGK4TcVVTkG_gqPYhcmKXMihe__0t2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
پایان‌بازی؛ رویای قهرمانی جهان برای CR7 نابود شد! بازیکنان ذخیره اسپانیا شاهکار کردند! پرتغال و ستاره‌هایش با جام‌جهانی خداحافظی کردند!
🇵🇹
پرتغال
😏
-
😃
اسپانیا
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98671" target="_blank">📅 00:31 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
