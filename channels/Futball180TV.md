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
<img src="https://cdn5.telesco.pe/file/gw7Tg4_vfh-B8uR4AuNRTXYvezKa7no1Vc46KaIG3kxTHJeIMgmWahIZbJQrE2LrNyISWBvQM6L3bzJYkm6n-Xaka59Ah6VotXaLl0z2VBU2S52btaUi6Gk7ELruInhWbAHF3hv-N7Iy1ToqhNzs5Xqf5mdhPeHXMlBqZQbWOvXb88pRJbAVFR-2tZP6Wiq79WDm-0HP9q-iXl1u-QhDOn7XhS0b3u7GAe5_4jLy2yfjSx78G2NcEu8AbAFEM2HZG8aDrJ1h91plFZp8SbNw9g4u7qecxGpuwV94SOjZLUEZ4GwYf6AVOlFSlpQrUCAXJchwX_bv_v4LeHq6a7f9tw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 419K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-106141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=HPLKX8--fsdffAsHday-XHNZKmsTlZZQrEiWjyyW5N0yF0TfKuhqyiGzL5eawvuWyp-ajerCVs6qvOaQxwo3LAM1hyfrr9r0WHKbSiJ1-ONQxgtEpuVxXgtP0nMHnrSS3oAHYyvP2ryqZGKjcY0YfdYVBttMv8TYtj44aelyu8ERoPQ7aHg-pTjMkJJlMErJr1PyWw5-fss2FA25cMAL8SjRU3oFwRsrWoRoE9CXdI9Pk2CoX7c2j37Y7HXsVqRhbmod_ea8zUXxVis40MKPxoiWF5nVROZno5mxnLs9kfuEKNQh-c_6eTMc9fzTMHfQPro0V-8DWkCUsUBEdr4nTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d99249b1.mp4?token=HPLKX8--fsdffAsHday-XHNZKmsTlZZQrEiWjyyW5N0yF0TfKuhqyiGzL5eawvuWyp-ajerCVs6qvOaQxwo3LAM1hyfrr9r0WHKbSiJ1-ONQxgtEpuVxXgtP0nMHnrSS3oAHYyvP2ryqZGKjcY0YfdYVBttMv8TYtj44aelyu8ERoPQ7aHg-pTjMkJJlMErJr1PyWw5-fss2FA25cMAL8SjRU3oFwRsrWoRoE9CXdI9Pk2CoX7c2j37Y7HXsVqRhbmod_ea8zUXxVis40MKPxoiWF5nVROZno5mxnLs9kfuEKNQh-c_6eTMc9fzTMHfQPro0V-8DWkCUsUBEdr4nTTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
شعار خاص هواداران استقلال: بختیاری، حردانی، می‌ریم برای قهرمانی
؛ این شعار به نوعی درخواست هواداران از سهراب بختیاری‌زاده برای بخشش کاپیتان آبی‌پوشان بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 312 · <a href="https://t.me/Futball180TV/106141" target="_blank">📅 19:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106140">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=tmMbFgKmf9fXs598QeMXnKAYlV-VBlKc8EtIcAQFv56r5EY7burx8pCNdpTEEFc7SrePNpgwNpPCnd5EwiDMTovg_cuSCsHnzNfkM9Oz9_46LE54JUur86cv6yNGM01Hr2KkoihOt-JmHCOq-AjtpX280ooBdcGqaWS7zK_FilV4jrpy5QM-x9-fSRAucj62l1ZAx_2VdtJKtK-4LPipYO4F1-wozsh2dmPNXYgGfCEFVMDU-HY_HfqHG5Jp3ybadSVvA-SSOQLFD1M94Fjb2YLRAGxpKTaYAMbEH7yeONY-2mH3L1IVVSzmishTbfFct7N4ZW5w_29v4jHUq6YiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac6e743e8.mp4?token=tmMbFgKmf9fXs598QeMXnKAYlV-VBlKc8EtIcAQFv56r5EY7burx8pCNdpTEEFc7SrePNpgwNpPCnd5EwiDMTovg_cuSCsHnzNfkM9Oz9_46LE54JUur86cv6yNGM01Hr2KkoihOt-JmHCOq-AjtpX280ooBdcGqaWS7zK_FilV4jrpy5QM-x9-fSRAucj62l1ZAx_2VdtJKtK-4LPipYO4F1-wozsh2dmPNXYgGfCEFVMDU-HY_HfqHG5Jp3ybadSVvA-SSOQLFD1M94Fjb2YLRAGxpKTaYAMbEH7yeONY-2mH3L1IVVSzmishTbfFct7N4ZW5w_29v4jHUq6YiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
هوادار پرسپولیس: به عشق رضا شکاری آمدم پیکان را تشویق کنم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/Futball180TV/106140" target="_blank">📅 18:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=feB900E-H3l6_dTu--wjaeZvcqV6Hi_iCVVXtTLKVhME5Ow3p6_z7oulQ7WJqaD9nEFwMcdw1R8zjz3YPJIBM4GZv2cgBAJq8jmVAlqMDax_krBsa6ysWXOAd45b5PqFuZBFS4I5hD4zGeNHuv0WW4vOKuVrtqptAilQv27Vmnhnx6sHbHzfMNRh9IpmV3i49iL6a7zmnEX8nRQ-X-5QQZWjHo2i3H8Un3cRBptL5Y-zWqZUsAdWM1DOuboVMDak3v-fFAFP1VdOb-kKwN_16NLRA01fBSXNYGeSxvUWXbHN-ovmPsqmEHrt-bY34tQ7ihTsuS0kVZ3qxehTmy7VEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d4f3e014.mp4?token=feB900E-H3l6_dTu--wjaeZvcqV6Hi_iCVVXtTLKVhME5Ow3p6_z7oulQ7WJqaD9nEFwMcdw1R8zjz3YPJIBM4GZv2cgBAJq8jmVAlqMDax_krBsa6ysWXOAd45b5PqFuZBFS4I5hD4zGeNHuv0WW4vOKuVrtqptAilQv27Vmnhnx6sHbHzfMNRh9IpmV3i49iL6a7zmnEX8nRQ-X-5QQZWjHo2i3H8Un3cRBptL5Y-zWqZUsAdWM1DOuboVMDak3v-fFAFP1VdOb-kKwN_16NLRA01fBSXNYGeSxvUWXbHN-ovmPsqmEHrt-bY34tQ7ihTsuS0kVZ3qxehTmy7VEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: سهراب هم مثل فرهاد بدون باخت قهرمان می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/106139" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8269376a.mp4?token=M-qU7p0vFOFBqfTUKZWodM5irKORJjvwVmxBLqso69t4Tc6qY7oT75EeoGuiJLX2t-fMB35EHOVmLX2dW0R-sYKdoMVZfXmpFiFprKHk3yp23SOm8K8B9fBtrMO-du5Sa6Xl7HO2Lv7mMJEZCUOmlWaLDb3PL3Ugv6P7ciUFN9CQmzNaVlw_huxGSfWT8NJJL6cIK1G6EembisASwDfcgXVMEZgQ9_qyGoyBHAp7DwJnA96doQ6LDDMsuHHF3hr4jlxdE-6d2jOS1EsOqvyu4FXozpL03QoQxghcL8tlc3gt22XMpthY73IpXZ3GOV1IUw_HWxP1_8rJTYWT88zy4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8269376a.mp4?token=M-qU7p0vFOFBqfTUKZWodM5irKORJjvwVmxBLqso69t4Tc6qY7oT75EeoGuiJLX2t-fMB35EHOVmLX2dW0R-sYKdoMVZfXmpFiFprKHk3yp23SOm8K8B9fBtrMO-du5Sa6Xl7HO2Lv7mMJEZCUOmlWaLDb3PL3Ugv6P7ciUFN9CQmzNaVlw_huxGSfWT8NJJL6cIK1G6EembisASwDfcgXVMEZgQ9_qyGoyBHAp7DwJnA96doQ6LDDMsuHHF3hr4jlxdE-6d2jOS1EsOqvyu4FXozpL03QoQxghcL8tlc3gt22XMpthY73IpXZ3GOV1IUw_HWxP1_8rJTYWT88zy4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
هوادار استقلال: مشکل فدراسیون با ماست؛ وگرنه جام را می‌دادند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/106138" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/Futball180TV/106137" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZBiIhikbmA5iS2Sq0EtFicwNZxDtGXYtYDDUPMo__uekquBsW3d8STYjAcr8kcTqmP4l6FCbLcPmoP-LrNJ7spNvlpTt9lTaKZjODB_kzQfZGb-tG_lnghKWGiTw3wKRUmyNUb5rTf6jS7iWgn7rJBKYl8or-hWf5yEQQaVCGXDyHnzw0Blp9yQnnL_9WCVld_J-ChrAAypmYdeKhtJjeIcFtcS623_HpBO-xrZKkISbQq6ORsuQmhhDGQMMsbp3LOpZS6oZq-snk13qJ__roOBFl35XKzVt4x-VdrJfB5UUoR5Wc1mQf5ikBMc1x7bO9FR2l09CGf1CHkRcLWhBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
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
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/106136" target="_blank">📅 18:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106135">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjxaLreDIG2GySHPVBkU5PSSK2JLaK7AZ5xi9z7JrnzKlJwW3thDAzWy6myfv--zWrkrFw-aT3LRpEVhEe3AovQnI8AZzsg3TGCGKntQKhDwEpULVgI-sRBNBjXQINmCmh1Ux9bbZf1JWxlWPPWGFpBU_w6y6BFvjbiFxrRvqC9bHWePxwqP0-ivyicUfSFm8bpzACRI3HOBpH-NP3uXwPPaUNlA01fk_NhfNbCboSFS4uvwFyHlUta5LESOb4X3Om38yKR3tpQmEX5yalcUOxutBiVGnT6U0_9dfHHRor2f7NTZh0hW5AlYRb7565mRrRV4DdfZr7uEmkeR535dVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/106135" target="_blank">📅 18:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106134">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZe9qQhpidL0tJDdlxBfQhNmVYM3H8CjWbTg_jIcbwZAgPSF0SQ6xDajtgDEpo7BqTHtPdyQ-8j8-0n2rwvAXoAHnJeTFZANKfYUYdjkSppvUZOsm6lUMRWkEbcZSInsx7258G73rf-dF1RsaA9S4V8emx-nM9xoy119HZZj3ERRUXtY5vbvEOwsAPmfxwitKzkwE7Avj_4twgiknLo6-7eToc5wDhcmvMYqtl78iHv9irPkJYJIELxql394HrkrWMDo_fIcUsQMJ8FcbKK4N-OLTipoQIEmuRwFnPWQfvgFCifdpSTKYwzsviCOEXcUdCm5PcsPKl_XmqgCRb3vGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇷
ترکیب استقلال مقابل پیکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/Futball180TV/106134" target="_blank">📅 18:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
ترکیب تراکتور برابر
استقلال
خوزستان
علیرضا بیرانوند، شجاع خلیل‌زاده، محمد دانشگر، صادق محرمی، دانیال اسماعیلی‌فر، محمد نادری، مهدی حسینی، اودیل‌جان خامروبکوف، امیرحسین حسین‌زاده، مسعود زائر کاظمینی و شهریار مغانلو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/Futball180TV/106133" target="_blank">📅 17:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d73a4eaf66.mp4?token=pxQTSd8fkKgyXLgMu6CsL2NyYsNQz8H_ipv1dSsauQxzzDGVLEV15heBP7o3RDP5NeWiqTPr0AkUB5r7j5c882Rwfs6Q8Wvf2c_PGe-mvzZPZ-p8numxW2hTViin76CyQKtZccVJoaRV4A94kDt5oZEstqnjZWzdZxtKXkcBSbz8g5OouH-w1aJYqBgQuojAOOxDFaWN6HJbQF7oL-XXppvQRh90g5vaGBleBBMHYWmQhSlUT-TVjYh2yWOg6S6bw2XUpsV9VE6_cEb479ITsqU8RKH46J9wVvJ4HhyTMRtKSozuRaXFVf9BiJZFIH47QK-o0XzK0NepmF8UTUa6xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d73a4eaf66.mp4?token=pxQTSd8fkKgyXLgMu6CsL2NyYsNQz8H_ipv1dSsauQxzzDGVLEV15heBP7o3RDP5NeWiqTPr0AkUB5r7j5c882Rwfs6Q8Wvf2c_PGe-mvzZPZ-p8numxW2hTViin76CyQKtZccVJoaRV4A94kDt5oZEstqnjZWzdZxtKXkcBSbz8g5OouH-w1aJYqBgQuojAOOxDFaWN6HJbQF7oL-XXppvQRh90g5vaGBleBBMHYWmQhSlUT-TVjYh2yWOg6S6bw2XUpsV9VE6_cEb479ITsqU8RKH46J9wVvJ4HhyTMRtKSozuRaXFVf9BiJZFIH47QK-o0XzK0NepmF8UTUa6xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
حمله تند هوادار استقلال به بختیاری‌زاده: برای دلخوشی پرسپولیسی‌ها صالح را اخراج نکن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/Futball180TV/106132" target="_blank">📅 17:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106128">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E7cjigX5rqAo7Ea1cdwzlCVU_BSzLWA5GJ_yWE8GVEuKY_JwI9NooLdwb1Xpq4c_FlryabL1vgZpjKxO0tGPJQpGOmzW0H3vYScUYa30vxWIIOrGFl36CdKlTnaXOvq2fqOFzpMYUCZGEb_g9azgOaFuBgI3wbbAwTQrCl7apUPdLnlI65CdmxCYfKxEjXFujjjetADThs-OW40E_lXZeYwXJO2jWLZaMR1e2UgQzdqq6hsZJV5rRUCCYOLhegKpY92Wkm1JYj_8SCD0iIlKIqaieEXuwgT0go6wGdlHrJGhpRZ31aq-YTTimDh-SnbjpOvIhtrbUQ4_HyJbbnwPWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aidq1biBAip7YYFu__T2E3mzQvqgXYhqyjKxlcx0aPoesCG2iJVEPobGbzSRz-kyZa8ZvsdgYtNGriGvWhmcs7P3dIAAjpObCOpdDQkpTwz8AZe9-x9zEtQGO9_sWHFgwsL2N-ZtL1UsIGKL4bvZx3B7QEeR8vX58zjaoPjDUUGk31yyu18ijNZ8p5UpZLgumHYPt12boswLv8YX1wiW5Z--hQu9mGug9C3DkDJ-5lLn6gnywBHES88O-uXdaJe3tlsczOL01cdVjfGfNYDY1oGK_3RmJf2DlnRm9nZbLANm-aR1sSH_RjC7Bj89O_H-N-sI4yTBWiKQYpRMCG2I3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rn5YSKic75DiTjXoEgKkX82C5XGASfbn-ATfcpkyVSblWehhqYzOe9yh6lIaWKYWt5w_8h-RmH1gK-paVslNdxLcOsiy4371948uYrUZ2mVSnqX3FfU7omlURvVeX5FIVku4ocsBW_mzimirPwkqemusi3rIIwZcPtk-6JbuYHHMAyPtw065T7mXzZN3ykWt-nCP7LsYyYMtX0uAvS6ZzpS_Tz-PGsWdzGopoCNT6_fMC1hxd3_wlIj7PxTwCO0e3A9KvCCX-Em5e0j5w4Tnz5J9Ts5cDMKVoe7K2VQfTZa_owPTsjkEALFmwb6SKuzyiuK-eAwkbKoQ3EvLjc5uPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qNii3K7PwKefW7Qi5qhn5Q2u1DWlXsncEaMQjf53cyDIQIO_jQZtYvFhpRsmJqOpvndMLCu2MUKKHHrtIl_enE52Z-IrGgVfdYVDFdXFIMI4gl_qQQxy_K76VHItBDwuxAg_4np-1lZ8KogUtNPLrLWXWjbZx3qDxT0hadJrGCVfqPH7NyIe7RnTqPwqFeqZIaQRJpx8dxrNw_LgmzIY94OcXwKt6xD8CuOAfezJnDFY7xmX9BsXevB5RU_v0PMPBUCkCUz8CubQbC2BRE5qWGmDgqVCw3HV1apPHP6TgYMnE2ncNGn8S_2O52vJHkjVzK6BOJ2I2tRh6YnN_OheIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😍
زیدی خوشکل و سکسی امباپه تو فیلم جدیدش یعنی "Drawn Together"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/Futball180TV/106128" target="_blank">📅 17:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106127">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81979f53d.mp4?token=ph3ExifzRF9jm_gK7UvvnFv7xWCo2ciFCxEbgjjIqC3ID05ngVlvsnPVogJp-PjfoU3DMOiU_ozM-vwnwMkO2qRPLkNC2l7z3cDjAXXXEc7qBXDZjla7tCvUXVS_Ilu2f6vQfbYRtBihjvIGCXnViBvHPnCIu_FOy520FcWwXXavjKuTK8nvgkWgggwjBBwM79shFDztxKcvhDST6yrC6-49eV0zMvXdoDO1o4xKQivywi9FjGgPNUpQsYPnB8RtBZ-NiMBy_BexuIUJt8gubWTj9zGLVDCyDVgS0Y2_d1XYrHnt4o9I0KEGVT7sA8sq4T7t6WAv-p4m2ZSXB6wPYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81979f53d.mp4?token=ph3ExifzRF9jm_gK7UvvnFv7xWCo2ciFCxEbgjjIqC3ID05ngVlvsnPVogJp-PjfoU3DMOiU_ozM-vwnwMkO2qRPLkNC2l7z3cDjAXXXEc7qBXDZjla7tCvUXVS_Ilu2f6vQfbYRtBihjvIGCXnViBvHPnCIu_FOy520FcWwXXavjKuTK8nvgkWgggwjBBwM79shFDztxKcvhDST6yrC6-49eV0zMvXdoDO1o4xKQivywi9FjGgPNUpQsYPnB8RtBZ-NiMBy_BexuIUJt8gubWTj9zGLVDCyDVgS0Y2_d1XYrHnt4o9I0KEGVT7sA8sq4T7t6WAv-p4m2ZSXB6wPYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار استقلال: سهراب باید صالح را ببخشد؛ ستاره سوم را می‌گیریم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/Futball180TV/106127" target="_blank">📅 17:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106126">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59106dd8ec.mp4?token=gk8t4I9xmF0O_5wWr6cr5IGh2VwzmzUSkIAoGao2LoQOwEKFzRahvSh6O8m93hWxftpvhGfLTbaJeg294kRAKs7bopXeSBc-EZuUfw4kzTvM2dFzU_Spxk12v94JO35WeuZUd9ql-Ek7aT5cGXuASPyqOyAasZH93vvEz_Ttz5q8oHlS4Nuxpf4rpaVVpxzujjSYPS5I9su6wlCNbPK2P75JlSmL0TmT5zz-cOUGeWRpNLIbANwkDmw4IpNBwsMXLNXAIg0pSxDMcdvzuiuvr7MCOymfjnPTrPZiCM1ejEbiH56i6SIz_EIIhHry6AozYIyWNk6j8DnMXE8oDHCXIhbV_UzdoH267gmXBFHNRJPtUW8H8GDWI3tdpSX5fDjJPIhbweaMhhT2U6OnbF4qsbrP2UaXTqEHc087iWTjZ4T3oECBwzv7etUHhOdPO5QzjrUvOPJn_-5eoVA5ypUv2m72NAhr9eqYYTyt_8IZo0nFbUXBicKanLDW4Nti_TfNRtXvSZA_dmNSrVvUPYpk23D3QB25kxUlI8IfEl_qdwo3jMB-8aqdDtEoNyMsbeAI-SA8ouehVLER7RU-UfyEN5Z44X-CTLK6vrAL6RycR4nwVdFk8QvhvUx-TdVP29CROQRkaN9MYlsPmE-crkynDTlck8Ey4T4leG3I4vYz250" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59106dd8ec.mp4?token=gk8t4I9xmF0O_5wWr6cr5IGh2VwzmzUSkIAoGao2LoQOwEKFzRahvSh6O8m93hWxftpvhGfLTbaJeg294kRAKs7bopXeSBc-EZuUfw4kzTvM2dFzU_Spxk12v94JO35WeuZUd9ql-Ek7aT5cGXuASPyqOyAasZH93vvEz_Ttz5q8oHlS4Nuxpf4rpaVVpxzujjSYPS5I9su6wlCNbPK2P75JlSmL0TmT5zz-cOUGeWRpNLIbANwkDmw4IpNBwsMXLNXAIg0pSxDMcdvzuiuvr7MCOymfjnPTrPZiCM1ejEbiH56i6SIz_EIIhHry6AozYIyWNk6j8DnMXE8oDHCXIhbV_UzdoH267gmXBFHNRJPtUW8H8GDWI3tdpSX5fDjJPIhbweaMhhT2U6OnbF4qsbrP2UaXTqEHc087iWTjZ4T3oECBwzv7etUHhOdPO5QzjrUvOPJn_-5eoVA5ypUv2m72NAhr9eqYYTyt_8IZo0nFbUXBicKanLDW4Nti_TfNRtXvSZA_dmNSrVvUPYpk23D3QB25kxUlI8IfEl_qdwo3jMB-8aqdDtEoNyMsbeAI-SA8ouehVLER7RU-UfyEN5Z44X-CTLK6vrAL6RycR4nwVdFk8QvhvUx-TdVP29CROQRkaN9MYlsPmE-crkynDTlck8Ey4T4leG3I4vYz250" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صحبت‌های عجیب و وایرال شده امیرمحمد زند درباره تفاوت زنان ایرانی و خارجی که در فضای مجازی موافقان و مخالفان خاص خودشو داشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/Futball180TV/106126" target="_blank">📅 17:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106125">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8dcdf837b.mp4?token=bDqZHhN_VGkaSfZuLVyccQ7Kg6S7XAhnUKhtGJmMBduWYyGfLYHkk9uhgxq2lp3ZMcOf0JwzaB0veCZmxMbN8HiTWk7XkYpW11FxaU-molRc09QttF9hrFfT0Ue7-F5YB0WH8PpBCvYfxigtW_4jH2GOVIgWmZTknZDWwuKrcNJOU30FWR9Gym0T3yTyJYJGtrTlBTtrRqFnn2k-P-WcKDXiIzWc7ZgCaEqZPTalsEKcj8AK17THEVp8I-v50F_6iuV5emfqQAXzeaM6OIZdm7zc4nuPzKYlFlWWM5Kuj0qGsCqmSfpdVDAVo6miX_GHOUVQ7zpq-MWGsV3fJZzRoicyqR3X_G3m-y4TcCmKgrs5Q1YnkgrVTp8GEHs3I3T2_nhijNDfZh6IIEnNZFh6nX0f03xj7ol1GGhlXNyPWH390s_WA3jkiRAk0f-rlL0QByOaXMbgrSWpIi-Zzvqsv3_vHfk2r82QGf8w0o4YZs4FCN_SV1vbMe5GDe6sO6_I0I3J1DXu6Ch8VKuOZ6e2GkJoB4xsKHneRK3v_IrjjxDTW4zSFZ75HlEel33Pt15LoG-DlmmIM-Hq9cDR4hCRZqDXIM462t1yxC1e8z0ucWNf6IT_T0QoaspiYOK2BySvnhOvz1pS7qcopvUUBeyxWUpoAtJ4qlz9Qrva7vGRqIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8dcdf837b.mp4?token=bDqZHhN_VGkaSfZuLVyccQ7Kg6S7XAhnUKhtGJmMBduWYyGfLYHkk9uhgxq2lp3ZMcOf0JwzaB0veCZmxMbN8HiTWk7XkYpW11FxaU-molRc09QttF9hrFfT0Ue7-F5YB0WH8PpBCvYfxigtW_4jH2GOVIgWmZTknZDWwuKrcNJOU30FWR9Gym0T3yTyJYJGtrTlBTtrRqFnn2k-P-WcKDXiIzWc7ZgCaEqZPTalsEKcj8AK17THEVp8I-v50F_6iuV5emfqQAXzeaM6OIZdm7zc4nuPzKYlFlWWM5Kuj0qGsCqmSfpdVDAVo6miX_GHOUVQ7zpq-MWGsV3fJZzRoicyqR3X_G3m-y4TcCmKgrs5Q1YnkgrVTp8GEHs3I3T2_nhijNDfZh6IIEnNZFh6nX0f03xj7ol1GGhlXNyPWH390s_WA3jkiRAk0f-rlL0QByOaXMbgrSWpIi-Zzvqsv3_vHfk2r82QGf8w0o4YZs4FCN_SV1vbMe5GDe6sO6_I0I3J1DXu6Ch8VKuOZ6e2GkJoB4xsKHneRK3v_IrjjxDTW4zSFZ75HlEel33Pt15LoG-DlmmIM-Hq9cDR4hCRZqDXIM462t1yxC1e8z0ucWNf6IT_T0QoaspiYOK2BySvnhOvz1pS7qcopvUUBeyxWUpoAtJ4qlz9Qrva7vGRqIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
علیرضا مرزبان مربی سابق سپاهان: اگر بجای خداداد عزیزی شخص دیگری بود، قطعا محرومیت سنگینی برایش لحاظ میشد. عزیزی دارای مصونیت از سوی حکومت است و در رای کمیته انضباطی نیز همین موضوع مشهود بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/Futball180TV/106125" target="_blank">📅 16:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106124">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlZzb8WVmlQIQvtE2GbT-_CVJhR_IRiVmb6qvSxBThfBA6pTt4k1s5md_o0cvUFfRW21ZV_lR7gwFsVOoFvCqa8VBten0B__sFeo4royj9HKc3v00N2EilRftsVQGvEksQhOygJOzd2ZH-f_zeNM9IbKTwGXnbiiWTNK3Jg40Uc8CMlhNoHfcR8jtQ2G2dMINb4EQIVIFgU0WdMGuz0zeGAA83-DGen8K_FifcrqYFnq6a049c6GI2RPpVnB7ZCrxczbm1WrDbNqAWw0VwenbLCfXp4MKEIU9xeNEn1s65AXdbOPSdyeDck0TGRZBVuJlK4kYPTJaZ3rX6fC5BagpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید بزودی قرارداد آردا گولر رو تا سال 2031 تمدید خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/106124" target="_blank">📅 16:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106123">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5becd61f50.mp4?token=pCD2WIomqApoKpKa5n-qmz_yCuIDYJfogaNfpeBncdf3qwRDsKL38md_rMfETWdcaN2zJbimK_qLXDAZ-3rJPz8-QvIIU0kQPwqS0gDIO8yovJJp1RTPkNW6FDGmswZq9ZUcpat5wV7l3i4qR2DNxdtsMl2WGAJMhRT_SHKnRCqfYSIPRRC3Mq8jn_BJRqM1pi0IZqvDoS4FqQORoKY-_xSftTE0iP87BArue2GgTzhK8CxK2_zbTROMACNeZPAEDzrhkKzS2OWahCBvC4vZkyc8YJVs_KLS8tRxGAtUsaqKULf5l773dLPvYHuRwe8bnEAFrXQQtttibtTx0xAbkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5becd61f50.mp4?token=pCD2WIomqApoKpKa5n-qmz_yCuIDYJfogaNfpeBncdf3qwRDsKL38md_rMfETWdcaN2zJbimK_qLXDAZ-3rJPz8-QvIIU0kQPwqS0gDIO8yovJJp1RTPkNW6FDGmswZq9ZUcpat5wV7l3i4qR2DNxdtsMl2WGAJMhRT_SHKnRCqfYSIPRRC3Mq8jn_BJRqM1pi0IZqvDoS4FqQORoKY-_xSftTE0iP87BArue2GgTzhK8CxK2_zbTROMACNeZPAEDzrhkKzS2OWahCBvC4vZkyc8YJVs_KLS8tRxGAtUsaqKULf5l773dLPvYHuRwe8bnEAFrXQQtttibtTx0xAbkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
جیمی کرگر درباره هالند
: "من اصلاً نمی‌تونم تصور کنم که هالند هزار تا گل نزنه یا بهترین گلزن تاریخ نشه. تا حالا هیچ‌کس رو مثل اون از نظر تعداد گل و آمار و ارقام ندیدم!"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/Futball180TV/106123" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106122">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a155534f18.mp4?token=b3TNPoHy9akBAoIjBGT3N-7YSqDzEEhcxNe1Fq9Nfu8_Ndv5QR2PsQPr9sQKGkuw9gsmnyoQNidbWV0-gwTNj22Kk-RjSfzrR00r0rzorJwS2wCnGMrkk-eiczkXFnSEIaBZASa0RqpQ6uPHm5YoL_jSsCzNaejlaAJDmlSnuOyzY3eyP2gBF7gr9K9aELjfufQt--R1cHb-VUzy2zJf3Oousu4tvA0y5FAMlE1pA3yyJyU0fGZOZFoO9wDN5dnHbw3EUJ-vSQegZu4JzJMtYk3e-DPQUbXhyf44z0oqEIuU1q8D47XJMWUAuC9BmcLLwDJhcByNUgNZEwZsL-dilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a155534f18.mp4?token=b3TNPoHy9akBAoIjBGT3N-7YSqDzEEhcxNe1Fq9Nfu8_Ndv5QR2PsQPr9sQKGkuw9gsmnyoQNidbWV0-gwTNj22Kk-RjSfzrR00r0rzorJwS2wCnGMrkk-eiczkXFnSEIaBZASa0RqpQ6uPHm5YoL_jSsCzNaejlaAJDmlSnuOyzY3eyP2gBF7gr9K9aELjfufQt--R1cHb-VUzy2zJf3Oousu4tvA0y5FAMlE1pA3yyJyU0fGZOZFoO9wDN5dnHbw3EUJ-vSQegZu4JzJMtYk3e-DPQUbXhyf44z0oqEIuU1q8D47XJMWUAuC9BmcLLwDJhcByNUgNZEwZsL-dilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سی نامزد نهایی توپ طلای ۲۰۲۶ معرفی شدن.
🥇
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106122" target="_blank">📅 16:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106121">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eeeaa17c6.mp4?token=SOgb-RBR3JQC53CvZAJCyDdqVkhaFulyZgeNGM5L9i9DusngJujU7J3J3FWuTfT_C7E7LMd6Ia3jquvCTBE2hrxJ45e5CkyQB40S9_poX4lNFCJJnDj41x_4tKFISnriF1pC16jGcHOEDWQZGTZiAd8bhY20xJF0WTK4mOKzlMaka0AJix6F1WdsN5_MnVgAQZb8OlGpcy8K081Sy9x0TDCHLzt-UEQ8g0-oUqLQJF9fSD6aNmnsCw1pZgDBpJ65XgNyQo5ihUIjua-dicvI7G0F8aMFc3AraOmoyqkV-gnFOLAk_pVOMMhWDf0mT-_IGmI-XobCCi7A7gFosuKzGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eeeaa17c6.mp4?token=SOgb-RBR3JQC53CvZAJCyDdqVkhaFulyZgeNGM5L9i9DusngJujU7J3J3FWuTfT_C7E7LMd6Ia3jquvCTBE2hrxJ45e5CkyQB40S9_poX4lNFCJJnDj41x_4tKFISnriF1pC16jGcHOEDWQZGTZiAd8bhY20xJF0WTK4mOKzlMaka0AJix6F1WdsN5_MnVgAQZb8OlGpcy8K081Sy9x0TDCHLzt-UEQ8g0-oUqLQJF9fSD6aNmnsCw1pZgDBpJ65XgNyQo5ihUIjua-dicvI7G0F8aMFc3AraOmoyqkV-gnFOLAk_pVOMMhWDf0mT-_IGmI-XobCCi7A7gFosuKzGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🔥
🇮🇷
تیکی‌تاکا جالب ملوانی‌ها در هفته‌گذشته مقابل تیم مس‌شهربابک که منجر به گلزنی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106121" target="_blank">📅 15:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106120">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aglWgk5XyYIHJr7XXAdNfmx8C-WMhk_PpxnWsnPEiOFt59DeSAqa7nemrxnJ5DwraqK7AcSUXmPNZ6wjIU7J-e5KjdZhS1H6bj2LH_F4-mwsoKTng1xs5fqN76iTnJdcCNSG06ynhwdMjzjhYbDpgVm8ekAaS_S_k7FgFIOfIYyGC9wiCAtLvLnNy-UF8x33Dfso7Mnt9GJ3faTQdW7bWKm8Es83YuijhtmAAGqT056Tpn88-bkjC_7IItkOjQCqf-yWVQu184gzpVBn-L6yQeBxuzfB_n8ZwWpNOhuo-5KDKN9YHC_dQvPPaYl1i0oU0THfvsDa6vplHQJq-FJOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🥶
🥶
🐐
🐐
فقط یک لحظه به این موضوع فکر کنید. بیش از 20 سال است که آن‌ها در بالاترین سطح، هم‌زمان حضور داشتند. ثبات آن‌ها واقعاً ﺷﮕﻔﺖ‌آﻧﮕﯿﺰ است
💪
⚽️
رونالدو: 18 بار نامزد، 5 توپ طلایی
⚽️
مسی: 17 بار نامزد، 8 توپ طلایی
👀
✔️
امسال مسی برای اولین بار از سال 2023، نامزد دریافت توپ طلایی شد و با این نامزدی، تعداد کل نامزدی‌های خود را به 17 رساند و تنها یک بار از رکورد تاریخی رونالدو با 18 نامزدی، عقب است
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/106120" target="_blank">📅 15:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106119">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61ab051ddf.mp4?token=CCeGIBLbkZ0NAOvoufiwEV6HPaUXynGn1cm8JcvpM5WTxFb63jjz4XOZJx0xY8F-VbsVAxjWLWPN0T_OvwWX514xRT43HQf_GJ4ZygW7cgUTBYX4XvXC0nobzbWwyj8_Y7ImFUol1vjkJSrDZ4Hi2DNvKD5SVYRFiSXETRZ87T0PiSEbvf76sioConQMH-Qk0DAPblthIDB69V9JEEVra3Bx8DRBWuqR8gcsuJCEaCHW87gzqYMlgMZzilZ9DbTuF-BTP5Xgm0NAC9YAaOECCCL7D3kQXEPlqiluNhoXC98cjSOp22hxKBOU1RFsU78MZWmnHHI5nWXS6lHu80gfkR83sp21m2heTZKfUwJc2fih63lwAg8NCQ6HoJgHzvJnOFLE0zcBTzt_xmbu9ibJDjI2DvqrGoTHJrW4ECLkGzZZp1k8Y19S11keFxURl-Z-j-lo_5fYPbHLY_wNxxC5SFmD8BBBoYRkc15a-VOEuHqUeJGFkyJbICL5ymguMFumsW0tPL4QM2pxfniiExaWppOTBFJxKzKEYmpamRQmt92D_pB7uOKpXuk8uOi_BxSYE4lYNmsf-1W0c9YtXk6R6WC97WQsGcgdzDj6hfOM39VIyf5qZngfuGUWbCjIOS8xXXF2s0_wGbPJycY3Ph8v5a8gqMZGBX49BQmtzSAeER8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61ab051ddf.mp4?token=CCeGIBLbkZ0NAOvoufiwEV6HPaUXynGn1cm8JcvpM5WTxFb63jjz4XOZJx0xY8F-VbsVAxjWLWPN0T_OvwWX514xRT43HQf_GJ4ZygW7cgUTBYX4XvXC0nobzbWwyj8_Y7ImFUol1vjkJSrDZ4Hi2DNvKD5SVYRFiSXETRZ87T0PiSEbvf76sioConQMH-Qk0DAPblthIDB69V9JEEVra3Bx8DRBWuqR8gcsuJCEaCHW87gzqYMlgMZzilZ9DbTuF-BTP5Xgm0NAC9YAaOECCCL7D3kQXEPlqiluNhoXC98cjSOp22hxKBOU1RFsU78MZWmnHHI5nWXS6lHu80gfkR83sp21m2heTZKfUwJc2fih63lwAg8NCQ6HoJgHzvJnOFLE0zcBTzt_xmbu9ibJDjI2DvqrGoTHJrW4ECLkGzZZp1k8Y19S11keFxURl-Z-j-lo_5fYPbHLY_wNxxC5SFmD8BBBoYRkc15a-VOEuHqUeJGFkyJbICL5ymguMFumsW0tPL4QM2pxfniiExaWppOTBFJxKzKEYmpamRQmt92D_pB7uOKpXuk8uOi_BxSYE4lYNmsf-1W0c9YtXk6R6WC97WQsGcgdzDj6hfOM39VIyf5qZngfuGUWbCjIOS8xXXF2s0_wGbPJycY3Ph8v5a8gqMZGBX49BQmtzSAeER8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
پشت‌پرده جنجال‌های اخیر امید عالیشاه در تبریز؛ خصومتی که سال‌هاست ادامه دارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/106119" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106118">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc99cf37e.mp4?token=T_kRMoW5lxJ5dGDei0hH0jbwr3hSYgXTYZPZgIR8tLJV52LVyJFv8Bpe5pMLdOzFBFWoxB_cyq4rtglElTxOEi-r7SwgQGg0-SvJI0wr-zR2t_GIV30SZwUskIcT_MWk4alimkNfmEEllcrciSPPAMPrkihF4tDQOGtuhKphA0fwSzKqQiWXn558IfLWRh54-ShIW9fMMVeyDr02PxRF5hzidHPQ3y2sFannTVQfre9ESOsWeypi0GUX0UbEHs2adJeR55GvjU2JOnOe3ppTHqAOol42qu0r0Kkl1fN2E2YNdtxafQOpd5AcR5Ff_OVIdTR9VUfwBfUCThLF1MRjYq-HYxcedaqRxBaPYucLYzOxruDrCIq5bMwJDJAI_m46bQ8bOW9Ls5mrgRLtwtvmYSZJzyDLfGlinPb1j2PPFMu6XPlX5Jg7mT9NcHYViTcl4GA0ckMsaOhraynYLdnTkor_DtUEbBOxF-EkZAE_15dRuCx52-JPSx_Ez3V67PocyBEq_JUXk7NOFsePsdnmZU5t6B_R33QafguROIkBokE3x_wnxLw1_uemmcR2qd3NOlThOq3UKqPZZNKfmCUb2oPnpJJU268BK2gV3lqfu3tTSoZ_4fWiYRkTitP7SFkXFzXhNgVZWyn88QdzqnSOiR94KlI6KSghefTVBolZ8Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc99cf37e.mp4?token=T_kRMoW5lxJ5dGDei0hH0jbwr3hSYgXTYZPZgIR8tLJV52LVyJFv8Bpe5pMLdOzFBFWoxB_cyq4rtglElTxOEi-r7SwgQGg0-SvJI0wr-zR2t_GIV30SZwUskIcT_MWk4alimkNfmEEllcrciSPPAMPrkihF4tDQOGtuhKphA0fwSzKqQiWXn558IfLWRh54-ShIW9fMMVeyDr02PxRF5hzidHPQ3y2sFannTVQfre9ESOsWeypi0GUX0UbEHs2adJeR55GvjU2JOnOe3ppTHqAOol42qu0r0Kkl1fN2E2YNdtxafQOpd5AcR5Ff_OVIdTR9VUfwBfUCThLF1MRjYq-HYxcedaqRxBaPYucLYzOxruDrCIq5bMwJDJAI_m46bQ8bOW9Ls5mrgRLtwtvmYSZJzyDLfGlinPb1j2PPFMu6XPlX5Jg7mT9NcHYViTcl4GA0ckMsaOhraynYLdnTkor_DtUEbBOxF-EkZAE_15dRuCx52-JPSx_Ez3V67PocyBEq_JUXk7NOFsePsdnmZU5t6B_R33QafguROIkBokE3x_wnxLw1_uemmcR2qd3NOlThOq3UKqPZZNKfmCUb2oPnpJJU268BK2gV3lqfu3tTSoZ_4fWiYRkTitP7SFkXFzXhNgVZWyn88QdzqnSOiR94KlI6KSghefTVBolZ8Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
✅
🍏
توضیحات بسیار کاربردی برای آشنایی با آپشن‌های سه‌مدل جدید آیفون 18
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106118" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106117">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f226d46bbd.mp4?token=gp56subNeCnTlMdD1IuEIpudpmqylmpRXpzkSyBwiN3tghx-yW5JR7xY4TzBJI6gFp2q6OWoXmYBM7U21h0Ky66HGLU36KywZxYM-hsThTRVAe_EjuqU7RoaO2VDUGh3pdarhidhHEzukBYopXZhV52rvSLX53EyLwYktze17i-z55GYhOBTgVAMAfh1eOwfmW9MYo_7O8X1isKQQnh7OcumGUuGLjlbnwi0ADIbPvTeoThvF3Nnomg3t0giIhb_VF5WJvn3nEC4INcNoh7FDUvVqwVqv1uMZHJJdo2Kokh1CrfmYGJeOEAOcasZJunnxsesiGW2ORfysPQ6KGgfSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f226d46bbd.mp4?token=gp56subNeCnTlMdD1IuEIpudpmqylmpRXpzkSyBwiN3tghx-yW5JR7xY4TzBJI6gFp2q6OWoXmYBM7U21h0Ky66HGLU36KywZxYM-hsThTRVAe_EjuqU7RoaO2VDUGh3pdarhidhHEzukBYopXZhV52rvSLX53EyLwYktze17i-z55GYhOBTgVAMAfh1eOwfmW9MYo_7O8X1isKQQnh7OcumGUuGLjlbnwi0ADIbPvTeoThvF3Nnomg3t0giIhb_VF5WJvn3nEC4INcNoh7FDUvVqwVqv1uMZHJJdo2Kokh1CrfmYGJeOEAOcasZJunnxsesiGW2ORfysPQ6KGgfSYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
تشویق وایکینگ‌ها در قلب قزوین :))))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/106117" target="_blank">📅 14:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106116">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faf79d5ef7.mp4?token=SUMWtA1jZ2EbSbkTxEeICrA7OIGUvayIue6TlObRksZwBJiWDlqso2PXc8HVj-UkGljHO-KsBAFm8o04WU63hbcxiSvKxSVSyfyxLQ9w0m8JBXR3VIsyXPyKvanrpSQpk2RxXv8HXtrPdTY7XNLcGONQIVp0nbrUzx-J9TPMauojKiIaEVSim5KBNX6xWT7KYE3xl7A2PX3FlS5MXAPbOJpuDx7I2GJcZrQy7OrVFJ8WJYN_dq-OCprsGhXmP3SiCTAnBgmFapFr8ES-ANmmc_vHT88F_2d-KLDUl6y8Nb7g35hLnN3OOD7uj1y--Wes-rX3SNJYMrLJuVvz1SHMOHcPXAvHHH9tV_Mdq3gOzx6eGi0hQD83Rhc6Nw03Dx9_HzpX00n-acOlWH8VJxUf1gluEWCK4K1e9_o4NHnjFk55Jh4QnozUDFLuvRZSdiWGDAhZNSpTJdxmq18TaFn9JHuzky_9sNrx--EJoQ2z9dsk9QvJD1thL-ASD6lk2TkuTbB7VQC86oR6po5huYrcfjJh9VyRz6BDa7yyOkM-hGPduudNChQP98qh2-0hwGoxm2AmS10sHtssFuoN816MuLsciksPcf5-nMJIbQRhCocgEpdPKlwZOLkQO0nnLapIDorZ9QA-2zeeZ0AJlgt7hG8ydU0vli3ij4nwDNFGdgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faf79d5ef7.mp4?token=SUMWtA1jZ2EbSbkTxEeICrA7OIGUvayIue6TlObRksZwBJiWDlqso2PXc8HVj-UkGljHO-KsBAFm8o04WU63hbcxiSvKxSVSyfyxLQ9w0m8JBXR3VIsyXPyKvanrpSQpk2RxXv8HXtrPdTY7XNLcGONQIVp0nbrUzx-J9TPMauojKiIaEVSim5KBNX6xWT7KYE3xl7A2PX3FlS5MXAPbOJpuDx7I2GJcZrQy7OrVFJ8WJYN_dq-OCprsGhXmP3SiCTAnBgmFapFr8ES-ANmmc_vHT88F_2d-KLDUl6y8Nb7g35hLnN3OOD7uj1y--Wes-rX3SNJYMrLJuVvz1SHMOHcPXAvHHH9tV_Mdq3gOzx6eGi0hQD83Rhc6Nw03Dx9_HzpX00n-acOlWH8VJxUf1gluEWCK4K1e9_o4NHnjFk55Jh4QnozUDFLuvRZSdiWGDAhZNSpTJdxmq18TaFn9JHuzky_9sNrx--EJoQ2z9dsk9QvJD1thL-ASD6lk2TkuTbB7VQC86oR6po5huYrcfjJh9VyRz6BDa7yyOkM-hGPduudNChQP98qh2-0hwGoxm2AmS10sHtssFuoN816MuLsciksPcf5-nMJIbQRhCocgEpdPKlwZOLkQO0nnLapIDorZ9QA-2zeeZ0AJlgt7hG8ydU0vli3ij4nwDNFGdgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
قدرت نمایی رئیس جمهوری مغولستان با وزنه!
رئیس جمهوری ۵۸ ساله مغولستان، هنگام بازدید از یک واحد نظامی، ۱۰۰ کیلوگرم وزنه را به مدت ۲۰ تکرار پرس سینه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106116" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea95c3de.mp4?token=c3BZQI39-3dl3gkXv9odradvXTNYln3VRf28H83bA9pqh1Lw2r5gSYb5xw_RwqdyO6n3ei22IV0IpkGS5A1AubPD3yfguEYes7u9ULtPMJIxv4ReVrXHCVYiS0XW3z5NZyMxoQIigiPG-q36HjTkpZnX3WcF_b3_nZN4O58nl49KNMm_tKJvHlNA0jaTCvuCfIvK_Fde_OcgP0BYE-IOD9lUqXUEn5tzoSqt3b2u-24Smg3GIjHquWz2yJ3aUwSKmk_S9WICAp7GRYGH7duZ2o-LTUV2Gpt3Hpf8hfTXAiqGH6iGDMuhEEvCHYGajhb0fLDyE4mAoDB3jhwm9KRzug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea95c3de.mp4?token=c3BZQI39-3dl3gkXv9odradvXTNYln3VRf28H83bA9pqh1Lw2r5gSYb5xw_RwqdyO6n3ei22IV0IpkGS5A1AubPD3yfguEYes7u9ULtPMJIxv4ReVrXHCVYiS0XW3z5NZyMxoQIigiPG-q36HjTkpZnX3WcF_b3_nZN4O58nl49KNMm_tKJvHlNA0jaTCvuCfIvK_Fde_OcgP0BYE-IOD9lUqXUEn5tzoSqt3b2u-24Smg3GIjHquWz2yJ3aUwSKmk_S9WICAp7GRYGH7duZ2o-LTUV2Gpt3Hpf8hfTXAiqGH6iGDMuhEEvCHYGajhb0fLDyE4mAoDB3jhwm9KRzug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد ایوب‌بوعدی در نخستین بازی سیتیزن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/106115" target="_blank">📅 13:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
✅
🇮🇷
بیانیه باشگاه پرسپولیس: از سوی باشگاه ما هیچ درخواستی برای لغو بازی با خیبر خرم‌آباد وجود نداشته و آمادگی لازم برای تقابل با این تیم در روز یکشنبه را داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106114" target="_blank">📅 13:19 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106113">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da7a59d4f1.mp4?token=kla2MvKD-MkLdUvXTaA67RYqomVfyrVuis_rGVRw13JYW1mdPJETrUkS7YviAvxHhXxpEiQ-RD_-1b7eWwB8pnddlg-b2QhYIs5VHh6KtsmUAJG7msYXFCi77E_f3WEZ_EgJ3rMXZtksoQoSj6qkXjFQRdbQJ-b-SZbXdpsT9BFXP-qh7v3QSE-clktghh_S7O1DVyxh_Lj7879LdmYXOV9naAXgz_PhZFX9smS5yuitEMdZPedRaimRqu7bkGrcCNgUV8i86XvuJOp4PHHI7dtHjS72MtWXslgwlmRwInks9r71jZr-PaWBK3oymcaHDPmqm98o7USd0sXps-8d2HBLcWgzBDJIQFukvHVqWfZ6KdXD6B8NrFuxHPzdpRN-uWPNVnZjCqwDrJpZySiSX2_y63wsW8vBjNbPSRvfIE_50yjvqkLhbFkSWs_NbrZj8XsosXQZJ35P0C35YxJa1j1inO4fcshNY0hxAuaMJZv6Z4fMmsKooYvxCMxIG6xqcpYM14lWuHSIkVtTHpkSRfvE3M3QoGH4tLpwcmC-vY4Mrc31D8Frv_Hzn28tlsfXhCY2vk4A7nFmM2PMhaqEUIAEL1hfbQpyijg3UisWvgVV-mTlQXGpwhrBWe5MZZDQq7w1_Pk6s_ZkqDAA1CESt-1oD1TtJmuGAqH8PGGNqa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da7a59d4f1.mp4?token=kla2MvKD-MkLdUvXTaA67RYqomVfyrVuis_rGVRw13JYW1mdPJETrUkS7YviAvxHhXxpEiQ-RD_-1b7eWwB8pnddlg-b2QhYIs5VHh6KtsmUAJG7msYXFCi77E_f3WEZ_EgJ3rMXZtksoQoSj6qkXjFQRdbQJ-b-SZbXdpsT9BFXP-qh7v3QSE-clktghh_S7O1DVyxh_Lj7879LdmYXOV9naAXgz_PhZFX9smS5yuitEMdZPedRaimRqu7bkGrcCNgUV8i86XvuJOp4PHHI7dtHjS72MtWXslgwlmRwInks9r71jZr-PaWBK3oymcaHDPmqm98o7USd0sXps-8d2HBLcWgzBDJIQFukvHVqWfZ6KdXD6B8NrFuxHPzdpRN-uWPNVnZjCqwDrJpZySiSX2_y63wsW8vBjNbPSRvfIE_50yjvqkLhbFkSWs_NbrZj8XsosXQZJ35P0C35YxJa1j1inO4fcshNY0hxAuaMJZv6Z4fMmsKooYvxCMxIG6xqcpYM14lWuHSIkVtTHpkSRfvE3M3QoGH4tLpwcmC-vY4Mrc31D8Frv_Hzn28tlsfXhCY2vk4A7nFmM2PMhaqEUIAEL1hfbQpyijg3UisWvgVV-mTlQXGpwhrBWe5MZZDQq7w1_Pk6s_ZkqDAA1CESt-1oD1TtJmuGAqH8PGGNqa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
سرگیجه جذاب و سخت این‌فصل کارشناسان برای انتخاب مناسب‌ترین گزینه برای بردن توپ طلا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106113" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106112">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
⭕️
🇮🇷
با توجه به حضور سه بازیکن پرسپولیس در اردوی تیم‌ملی امید، احتمالا دیدار سرخ‌پوشان مقابل خیبر خرم‌آباد لغو خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106112" target="_blank">📅 12:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106111">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkrUsS1qVoxGq3pg68fTDrmyUng3qYTs0gI7OcOS9trQJB1vrvmF29zl9n0fcA294wb6OkL9-t4ogRXIO_6h6U282qPfyhG7duDRZdLkSNg89T31YycCROFaoqM1uY432B3awd2SQNIRAIYS9lXe9kCqN6tlB6x5M2KQTneKj0VWQ3-Wbn07LiaktK786tq7U0aUnKPjiqYCvZfZSXMyQWfuS7l-GGFqobvfuKUQ-TvfiWqi3k3RlC3Q1IHgYfrUUCZCd7zVGJOyF4TFDYi_29foeVVeKMzoK-ttvn4wt4I8DQJxFQYosKOvGCLEoW_DIyNWbMhE1FkZognn6-vX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⁉️
با پول پژو ۲۰۷ در ایران در کشورهای مختلف چه ماشینی میشه خرید؟
🇦🇪
امارات: لکسوس ۲۰۱۶ تا ۲۰۱۸
🇩🇪
آلمان: بی ام و سری ۳- ۲۰۱۵ تا ۲۰۱۷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106111" target="_blank">📅 12:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106110">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
‼️
⚔️
کل‌کل و دعوای دیشب رودریگو دی پائول با روبرت لواندوفسکی در لیگ‌آمریکا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106110" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106109">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72b9052ac6.mp4?token=ZRP_A7Q7jp8MzRA3DJAUENduaO9qRoESCCmm3cdaKs7idx7dflzDg0iqsimMbBz2gEWO3AcsRvUo_3_3duQbIKA5CE2pUZrqpRGVFVKHNGoHFUhpdcs_cxmBnBsdHrusTgHtNfjDsomc28noCP9OVhY1m-803McgDT4cVU7ELa38kOkZo2zlia1gnv9iZPkyXfx-WY5GMG-voc5Baj_9XW9PyMT67sHhkUb5ttT9TpkCZ-g7c87887MAKpICxR75JTWL1pOlebA5UYBLl66Jv2bjnGymiB0Oc2pSAHhzkHEkMzDDvh2y_Bk1NXra4PCFJpPpDruOO-Zd2eyKLYDYcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72b9052ac6.mp4?token=ZRP_A7Q7jp8MzRA3DJAUENduaO9qRoESCCmm3cdaKs7idx7dflzDg0iqsimMbBz2gEWO3AcsRvUo_3_3duQbIKA5CE2pUZrqpRGVFVKHNGoHFUhpdcs_cxmBnBsdHrusTgHtNfjDsomc28noCP9OVhY1m-803McgDT4cVU7ELa38kOkZo2zlia1gnv9iZPkyXfx-WY5GMG-voc5Baj_9XW9PyMT67sHhkUb5ttT9TpkCZ-g7c87887MAKpICxR75JTWL1pOlebA5UYBLl66Jv2bjnGymiB0Oc2pSAHhzkHEkMzDDvh2y_Bk1NXra4PCFJpPpDruOO-Zd2eyKLYDYcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
کنایه‌سنگین مهدی مهدوی‌کیا ستاره سابق ایران در مصاحبه جدیدش به عادل فردوسی‌پور
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106109" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106108">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff5f3cdb2.mp4?token=lmzHot7iuUDCZp9sT_2J9i098y1dzwzWzv2WC_VpipvNLS8vYrqoN7cT6A3MAaM5WfuksZiU8c21xGJ6M7xq8arUUK4Nl5VBg8K6i1Y0o6Kmxg124ihLJVgMtGwR9H7f97yLSut2WeVbMlAPuY6bWjZG6OBwTKIAh7VaZJEzx2Jm89q4pt-0IUgFJ0pZDwqCb488wsR3XF4jeJc2SDKzyJJ5EB-zyuEjqN7NQf6sfSFbR5FqIQlHJGLW1piSofT_-6rgA-ZCasqyC1zSb_3rwjXJ6BBFH8lKGghWQXEywXXD8yzf2MGTjpj3U-p3g9PzQY7bRMrqov776eAaFDlZjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff5f3cdb2.mp4?token=lmzHot7iuUDCZp9sT_2J9i098y1dzwzWzv2WC_VpipvNLS8vYrqoN7cT6A3MAaM5WfuksZiU8c21xGJ6M7xq8arUUK4Nl5VBg8K6i1Y0o6Kmxg124ihLJVgMtGwR9H7f97yLSut2WeVbMlAPuY6bWjZG6OBwTKIAh7VaZJEzx2Jm89q4pt-0IUgFJ0pZDwqCb488wsR3XF4jeJc2SDKzyJJ5EB-zyuEjqN7NQf6sfSFbR5FqIQlHJGLW1piSofT_-6rgA-ZCasqyC1zSb_3rwjXJ6BBFH8lKGghWQXEywXXD8yzf2MGTjpj3U-p3g9PzQY7bRMrqov776eAaFDlZjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
لواندوفسکی بعد جدا شدن از بارسلونا تو لیگ آمریکا هم هربازی داره گل‌میزنه و چه گلایی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106108" target="_blank">📅 11:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106107">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c9d287e7a.mp4?token=VbbmeUpa-nTqiKAJwSxMLo2vxqgePTPe5igjYukKcrkLSAECOK_j6oO3RBiiFAM2e5pTy-TMmwK2TEQZRP5lV2MnwFGRib7uDZ_tY4Glc9myNU_5NOdunjgprdCZX-D1g5dgBjQZ1b40WJjs1g0VaXtZOKqYFnwp6nRplhzf834ZDMl503sIVe9qlNRTTHA-wg9y3Yf6YQDau8RGwAtHYxRS1MXR5OduTU3alksnvRv8CENxsSeY3kypgOsaSiHBKhnOshO3yEgqcIRRSkXZNugKFPTWJRpUZS7WahKnygrjfuP8NsiA9iZF6da7vKdWZKzdfSmKuAGsYaDVRMRotQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c9d287e7a.mp4?token=VbbmeUpa-nTqiKAJwSxMLo2vxqgePTPe5igjYukKcrkLSAECOK_j6oO3RBiiFAM2e5pTy-TMmwK2TEQZRP5lV2MnwFGRib7uDZ_tY4Glc9myNU_5NOdunjgprdCZX-D1g5dgBjQZ1b40WJjs1g0VaXtZOKqYFnwp6nRplhzf834ZDMl503sIVe9qlNRTTHA-wg9y3Yf6YQDau8RGwAtHYxRS1MXR5OduTU3alksnvRv8CENxsSeY3kypgOsaSiHBKhnOshO3yEgqcIRRSkXZNugKFPTWJRpUZS7WahKnygrjfuP8NsiA9iZF6da7vKdWZKzdfSmKuAGsYaDVRMRotQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
شفاف‌سازی عادل فردوسی‌پور از ویدیو جنجالی که به بوسیدن دست وزیر مرتبط بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106107" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106106">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106106" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106106" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106105">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJwU3YDSARQlmj6hS6mvRTmuj48sFrM51VpBlCDjHNNLCCYtjE-jwmdHTgVr0x3URCh1RtvHJ-EUrEoVxl1EG6H14rYOBIao7ep6I-8iOAzP2wyCWh77PthbOgzA2Aebf7VpsoSqS7QMhdYmIMF8p3ireAypBZVXE39Fg9rGfggeuGdL8Rxf9mfv8IlJYkvq00QhSRSxeVG5M0NWpzb7E_8mPaJNS0KYgOYdVd1Ld7n7j0NP-DzpHcNZlypIQRsaroXu6Hp1mFZGWPGewAOsCAEKoTiCxgqdkVEnPd_4v9uTq_ugLUKL3lv6IDtQfoTdz5ef65XEJO_IkY3SBSes9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/106105" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106104">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evVjjYFYtZ_sx5jZv4i1tEkKCPG2_7wualG-CiPAJmJg-6e0AcF5SJ21FyhPcswEYqgWfX6wOSQ2-EC93Kv0lTQ71WDsGHt3-AtWG-J714nQgAj3iTQkSgJT3Bx9fuQ0ndQawkQ3DWsdtJTbFGk2O3FES1RmnNyhoKSMmxr4z3fsOIQr3hTA_9Pso8AaL-DgIPUMKS4K4FB1q5hjhgWG0q7GAYcYRgTA0jyqUIuZnmyRhGu3iWMgOsQieWeRER_OeUUcEJP2NKt_Yr5YqDeQf-KaKnGlXqbEKQ2UP3nOvsn2NhkqQrihOlaV6N9KbdvMrpOp8veTVv3JF7qLGl-Vcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
تیم‌منتخب غایبان لیست توپ‌طلا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106104" target="_blank">📅 11:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106103">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1619d9ae.mp4?token=WQSrG3HZGHjMgrs7BcwTLTXbaL1H2YN3D1qJS3nNBNQ7aMYkdxT9IdKWzCaP36m8CJ2BhhFWFX9r9Qr8DKqV7qmUHEahz6upqmxEHUL9LCe4A1cPugWz3Gf3IEpJQp7vutjOqvysSdvukt75XUjy-mA9dzAa0_dM1_Y2GCOBDIna-x7WKIMnXMc_EhmX6bfyLafAzprO0RRMmWuf-WedXRRg6h4Izv8pN02daQrl3SlYhSnj96DM4yREFg3HSCRqwYU1CThNQ186XR71iX0V2ofwfdUnlopgWvY9WRqfxTH8S3_PKIlpxjG_Z9sqhvKPhztysPGL2BMnt37eXxFJWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1619d9ae.mp4?token=WQSrG3HZGHjMgrs7BcwTLTXbaL1H2YN3D1qJS3nNBNQ7aMYkdxT9IdKWzCaP36m8CJ2BhhFWFX9r9Qr8DKqV7qmUHEahz6upqmxEHUL9LCe4A1cPugWz3Gf3IEpJQp7vutjOqvysSdvukt75XUjy-mA9dzAa0_dM1_Y2GCOBDIna-x7WKIMnXMc_EhmX6bfyLafAzprO0RRMmWuf-WedXRRg6h4Izv8pN02daQrl3SlYhSnj96DM4yREFg3HSCRqwYU1CThNQ186XR71iX0V2ofwfdUnlopgWvY9WRqfxTH8S3_PKIlpxjG_Z9sqhvKPhztysPGL2BMnt37eXxFJWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🤯
رکورد لیفت دنیا شکسته شد...
۵۱۱ کیلو رکورد از یک جوان ۲۰ ساله مکزیکی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106103" target="_blank">📅 10:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106102">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef0e259b6.mp4?token=Rty7cTZ1fUx94NP6f9-lrKAA5nH0yPBrn2B0dWR46JuD_tC9NNX1jJisFEPVXuxTCNBgsIG_YCTrU3861ofoS4FQngN1cl-RUkdqAUcWQV59riWdbL3D874tGqIk0IEsc7ECPTXIYs4cK6EXvu9BhY7Os0x3freEX77Mep0TjdlXqfyaqeXxJVqgLfvXry6TzzXUCc-5m0FhQDqUVyQrs5CtToNh6Je1lIOxfWUKppKqLzTbNJNZNEfDBZATj9-2pfDi55X1WknDmivfSxrcG26-rIMhC9WaBTBoMqWltEc4fGKSsjmdPXYZDO4MO-sxlobSmlmzuddAMfxwTx1REA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef0e259b6.mp4?token=Rty7cTZ1fUx94NP6f9-lrKAA5nH0yPBrn2B0dWR46JuD_tC9NNX1jJisFEPVXuxTCNBgsIG_YCTrU3861ofoS4FQngN1cl-RUkdqAUcWQV59riWdbL3D874tGqIk0IEsc7ECPTXIYs4cK6EXvu9BhY7Os0x3freEX77Mep0TjdlXqfyaqeXxJVqgLfvXry6TzzXUCc-5m0FhQDqUVyQrs5CtToNh6Je1lIOxfWUKppKqLzTbNJNZNEfDBZATj9-2pfDi55X1WknDmivfSxrcG26-rIMhC9WaBTBoMqWltEc4fGKSsjmdPXYZDO4MO-sxlobSmlmzuddAMfxwTx1REA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔻
🎙
ماجرای ازدواج محمد پروین با آناهیتا درگاهی عمه دنیس‌درگاهی مهاجم تیم‌ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106102" target="_blank">📅 10:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106101">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9e4c6ba5.mp4?token=bb1twOLZjJwV0OSg_E901SqXgj-2xM2NgDOqrXsSBeMHXkwMlR8lJTHNwbMdudj_jcrbqXMp7PLEBD_jkJ39IpmQh3sWq4c9pq674yUrrAK597UyIesFuv8g1LVTMk4LRTdBDUxNm-gSh_0lH3b0mJUXwT65mJRsuN_MgHol8TaHSA6k3znLJ3rHfqcKczvkWAXsz2PD73Wa2KzjLo3_WL9My6fCQUXLlpc1rZQl0AC4DoipDzrk9ZycD60WlG9WsRkzPikmhRuEKY7cyJlRmw89Fck3TsnyFFPGVTJR3s3RDtD0tiVUoOZ0ZJkp5-ltj6Npix0ONZR7aI0ilWVm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9e4c6ba5.mp4?token=bb1twOLZjJwV0OSg_E901SqXgj-2xM2NgDOqrXsSBeMHXkwMlR8lJTHNwbMdudj_jcrbqXMp7PLEBD_jkJ39IpmQh3sWq4c9pq674yUrrAK597UyIesFuv8g1LVTMk4LRTdBDUxNm-gSh_0lH3b0mJUXwT65mJRsuN_MgHol8TaHSA6k3znLJ3rHfqcKczvkWAXsz2PD73Wa2KzjLo3_WL9My6fCQUXLlpc1rZQl0AC4DoipDzrk9ZycD60WlG9WsRkzPikmhRuEKY7cyJlRmw89Fck3TsnyFFPGVTJR3s3RDtD0tiVUoOZ0ZJkp5-ltj6Npix0ONZR7aI0ilWVm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
ریما رامین‌‌فر بازیگر معروف سریال پایتخت و پسرش روی فرش‌قرمز جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106101" target="_blank">📅 10:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106100">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/710d093c91.mp4?token=UZ5midjJsOxEVJdezhpDY85DcQrIMOO-uQ7bD_b3xV3CMt_CnpAqO_kFQfg6hTTfXP-JR8t0Gpo8q8o9X0I-nJNGcXGFkfP8izhbLyyVmaInDFJHurf7EE4MLscxioZ0BGQfjztiJr1etfmu6uawx1-NpwokV2971LoxwxEQcTSO5TvtcqF51ktV_-0xcE8Kj-MHfAGZdVJAj6kY1BuAyy-5YY9nNjbKIHtyyvjhRq12wJ_525TN_UezEWPa9H1PlYBUCLp943r8SG5VrnH5C0jwCR13mPSgIx9SNrBppLrPl4rRdPMTtb0jn2Ym6PVCOCIzj0PmoP2iBcg5gf-qqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/710d093c91.mp4?token=UZ5midjJsOxEVJdezhpDY85DcQrIMOO-uQ7bD_b3xV3CMt_CnpAqO_kFQfg6hTTfXP-JR8t0Gpo8q8o9X0I-nJNGcXGFkfP8izhbLyyVmaInDFJHurf7EE4MLscxioZ0BGQfjztiJr1etfmu6uawx1-NpwokV2971LoxwxEQcTSO5TvtcqF51ktV_-0xcE8Kj-MHfAGZdVJAj6kY1BuAyy-5YY9nNjbKIHtyyvjhRq12wJ_525TN_UezEWPa9H1PlYBUCLp943r8SG5VrnH5C0jwCR13mPSgIx9SNrBppLrPl4rRdPMTtb0jn2Ym6PVCOCIzj0PmoP2iBcg5gf-qqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇮🇷
هوادار جذاب و خوشکل تیم فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106100" target="_blank">📅 09:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106099">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=fkZ4xy5S2tV-hN0f6zUo-vO2UfMHXFyNCSagrKyDBMeXmg35YBevDwmdH0joYEJ7HP1GKPQKwrhTHR-ei1JiNeVmr5nT1FLKOnfaRPKYFZ6-t1kRXFOINU09nvyGgRWrTrW317ezu_bt2hRKVm22OSctGvqT-EFZLX1wK3Wsp5MFvBovSa6sHZJrSIiyvArjouivNsZoacFBV7ZhuBx2Mwp5SK7pJg_QlKiXDaDtHrsO4O9CLgE-vOyERIMNM8fohGtj7RV5FpJJ4cdvdQytg5tPOPWVUVIImpFqxoqL1YIJqxw47JDsRFj66k-Hs_76ioIQC8EipKOiZVU6zYjvsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe421b6527.mp4?token=fkZ4xy5S2tV-hN0f6zUo-vO2UfMHXFyNCSagrKyDBMeXmg35YBevDwmdH0joYEJ7HP1GKPQKwrhTHR-ei1JiNeVmr5nT1FLKOnfaRPKYFZ6-t1kRXFOINU09nvyGgRWrTrW317ezu_bt2hRKVm22OSctGvqT-EFZLX1wK3Wsp5MFvBovSa6sHZJrSIiyvArjouivNsZoacFBV7ZhuBx2Mwp5SK7pJg_QlKiXDaDtHrsO4O9CLgE-vOyERIMNM8fohGtj7RV5FpJJ4cdvdQytg5tPOPWVUVIImpFqxoqL1YIJqxw47JDsRFj66k-Hs_76ioIQC8EipKOiZVU6zYjvsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
داماد سابق علی پروین: بعد ۶ سال جدایی هنوز لادن پروین رو دوست دارم!
🔻
لادن پروین رو خیلی دوست داشتم الانم خیلی دوسش دارم. لادن سوگلی خانواده‌ بود، دليل طلاقمون قماربازی من بود. چندین فرش ابریشم زیرپامون رو تو این راه به فنا دادم و ماشین بی‌ام‌و که داشتم رفت.. لادن هیج تقصری نداشت خودم مقصر اصلی این جدایی بودم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106099" target="_blank">📅 09:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106098">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=WnyA0R-bD2SIMnOgJqd4dqgwaYcycfabnthVbYzG0s18KuYLQOyKEvn8oZWXnFHBJIErF_m04P1_0t0EpCGSnf0G1hPluco1VPAHqJZFmlUvZOCJ4T0Q5zsK3t_qq5eXzHpkIsQ3ZFpcJ7GWq5A0tiBLBVZlQLXvYCMqicwWh_UCaPWzfIoerfkWjYUWQz6aO18TmNk6qONYupwxLkTgaF4ByAzaG009Rp-mrDKo3OMJV_u0A96WuMkO1S8_SLCpjr7qdsc15oGmbJ4JzFdpBEB0ZIeAZa8cyUstcySoj0VJPrPFfRtjFQ6TjaZ6MFC5AIdMcdQu6IH7fCPpuAIqCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36609cb5e6.mp4?token=WnyA0R-bD2SIMnOgJqd4dqgwaYcycfabnthVbYzG0s18KuYLQOyKEvn8oZWXnFHBJIErF_m04P1_0t0EpCGSnf0G1hPluco1VPAHqJZFmlUvZOCJ4T0Q5zsK3t_qq5eXzHpkIsQ3ZFpcJ7GWq5A0tiBLBVZlQLXvYCMqicwWh_UCaPWzfIoerfkWjYUWQz6aO18TmNk6qONYupwxLkTgaF4ByAzaG009Rp-mrDKo3OMJV_u0A96WuMkO1S8_SLCpjr7qdsc15oGmbJ4JzFdpBEB0ZIeAZa8cyUstcySoj0VJPrPFfRtjFQ6TjaZ6MFC5AIdMcdQu6IH7fCPpuAIqCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
🇮🇷
🇮🇷
بدشانسی دختر کوچولوی یزدی در حاشیه بازی چادرملو مقابل شمس‌آذر قزوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106098" target="_blank">📅 09:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aN5V94wUuk-vZ0nzxv6oLNMjjYSlMT4saoh0DIqPhRhGSnA6dy_1VBBhAxO0jcvfXRGaPtSGeVhjzKQHKY5LPjz1gzCL46GK5nnQyzsGMiGxAnLDtZcuVf26YkWL3DyV5HTWGJuRWwyAMPtCyOZFmAWyWAvtAfZ9OYLYdgBRsoOcyitWAw9VnoQkNI_Oq6yaQRLhDMznBG2pqnPSDQFt9-sLDjbzODsXnOAjDKFCIZEpze6GUD9Xw8G1QBn67szW_Qic-FrQxqQqVpdAmhBY7SsW3zVA5W3ufBwFvJbK-b1PF6ioPobzAZ-oe1ycmd4H8f2oDPBywHn6c9wHNeoGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mUCZLZWLjPGbONFXv9JC1gER8qusld9tCxFBJqEAZqBmGQoigUSaCV42B_PenGSPJU37ZbCAfbywT2SOBIieuaokqig5pFg8Hdkrg5WnJ8HC94mnvgqp6tFO58YN76NaS3gqCzi-f6aAKfsylbFTbPk6Y4vpCDjzBj8RPYFuzmoCjtC1DOnSJg3lIQoetYgK7-iLZc7GtmB2aMm2C1r5LV9jDH7cDtct4Y_RzSv5Kv3jjUvKGZZlX5PwHvAioPBukkwkpQcdQ6l2gz7Fg4DtgCBvlml-DexWC_IkC0kdWAoVVZzh7QDqZs9kkY49YbZz-jiJW6rQFsJN6x1gRAAGag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AbnDZA-NRfM_tUX-U8qZRqNw26Rink7eud_JEghDVRK6boaSl_FXaBxqW97OLfLWhP-RCsQ8K5xKQnwo4P7hbMWmjU4Xvnn2xCTHGh4lwSMXwc7JxCFRjAIwZEXZI-u_ZamVaBsXzonL0xdMhvpMsj0pcUOq9mDS2wGZ63fNgwGwE3M1Fpj1mlLXbMw0dwXBOUc_Vi8Vw8UBREjasaPsPg4sLUsGEcU2n0HPZ8pq7fp8FYHzgClLQW5boewwyy8086yBZPnWtLo2RZHLXBEnM0ZLMR9Nk8SOIZH9SSfIjUnstiC4lNqtoPdaY6IGwev65hpW5QuAcpJ6vSaB8K6AAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzGwwyW3xb2RP19sKNeUOH_ak5SxgSHMnM3gHmIaGqLo1kj8-ywm5vXopBMi-9Cuzakx7EYMX03a8JC8y5Re4IpyI9pIEfJIgrymxcPf61mvDkFgAP2NFv9l3UakFk_qK98_DF6nonNPZVotm7SpPtKq8BJ9nKqtcsASrx2_IaZotKlk5T4JMy9eJKT34swwuzwj9FepQmzSPQKI3XRTo0R1AnweS5wLx3G6wx567zfNCBbdIwIP7pXltlbpo1PvCxy_154GQky7KK2zrJHWv52ztrgU4HQb5msw0pVRqyG3k15MEwatlpLSISVYwAON4ybl3sylMnzvA2Pi4EFN5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇮🇷
دختر پرسپولیسی حاضر در بازی ذوب‌آهن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106094" target="_blank">📅 08:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/970c991132.mp4?token=KVmBL4K1R8sD2sHXxrM1h63g1LzQZoojdHfHPsVt95iSJRGQbxCxkpy0Rs3SFBaGKJIqRhNGPp7orhQv3F9yuMT_YLd9ZfdTm08sWYRmZ95EhpDuW-Ox-TnQJ9Zyj3lfVTb5w-XinRM5rBhqtYBVqdlYchLar3ZA0m5FSC1XMLKbo5ygABbWckHXqhUGH5pYhsOXp4TejJ_g4wouKCC7dxU15z_FhWdIY18EunWUEbW2BnCe8gmW6XnGXiBrqkwDvfRwVZ9yISAxgJOzGVWKQDkHCTrFw3Z49jfEwXRK4Iyc3ms4ygdRdv4VcJ3wfLgOYDDMG357n8jEg7Zr5-fBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/970c991132.mp4?token=KVmBL4K1R8sD2sHXxrM1h63g1LzQZoojdHfHPsVt95iSJRGQbxCxkpy0Rs3SFBaGKJIqRhNGPp7orhQv3F9yuMT_YLd9ZfdTm08sWYRmZ95EhpDuW-Ox-TnQJ9Zyj3lfVTb5w-XinRM5rBhqtYBVqdlYchLar3ZA0m5FSC1XMLKbo5ygABbWckHXqhUGH5pYhsOXp4TejJ_g4wouKCC7dxU15z_FhWdIY18EunWUEbW2BnCe8gmW6XnGXiBrqkwDvfRwVZ9yISAxgJOzGVWKQDkHCTrFw3Z49jfEwXRK4Iyc3ms4ygdRdv4VcJ3wfLgOYDDMG357n8jEg7Zr5-fBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤔
🖤
ایرانی بیا که یه حسرت جدید به حسرت‌های بیشمار زندگیمون اضافه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106090" target="_blank">📅 01:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d64db334.mp4?token=s_4Khgm1lMl8ry4JPJr0NXLYkPiE3I878HHccrebDL7hbV_ShdmlnGdRUy_JxkQr4piYsfmYL1BGVczejDQnOSi3hnBFwG4ud_qSCEQyvQu1CqFdjxqwf0Vwdi_6AhMPuC35EKTuqpHz1vShxNVLjbBVN1Hyvs9gKz_QML-eTYuKDrB9IUVAIzoto7rstFAz2ywab8Mp028ic6OcmuLAnzVLPxirRDmPG3oeBun4jqEwyNTrJWOwDxs8bDyL5uCGmkUAM6T7VkIRBKJA26POKH4RyUAo_9DJG0cyhW5QlK4OoB0k6TxsVGxrMv46UHwn5sl6t2xjrNbknPK0gRiVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d64db334.mp4?token=s_4Khgm1lMl8ry4JPJr0NXLYkPiE3I878HHccrebDL7hbV_ShdmlnGdRUy_JxkQr4piYsfmYL1BGVczejDQnOSi3hnBFwG4ud_qSCEQyvQu1CqFdjxqwf0Vwdi_6AhMPuC35EKTuqpHz1vShxNVLjbBVN1Hyvs9gKz_QML-eTYuKDrB9IUVAIzoto7rstFAz2ywab8Mp028ic6OcmuLAnzVLPxirRDmPG3oeBun4jqEwyNTrJWOwDxs8bDyL5uCGmkUAM6T7VkIRBKJA26POKH4RyUAo_9DJG0cyhW5QlK4OoB0k6TxsVGxrMv46UHwn5sl6t2xjrNbknPK0gRiVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لامین‌یامال
❌
لیونل‌مسی
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106089" target="_blank">📅 01:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
⭕️
🇺🇸
رسانه‌های مملکت: آمریکا ساعاتی‌پیش به مناطقی از سیریک حمله کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106088" target="_blank">📅 01:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaKvwo_hwxgR3oIuzZ3HVx74FyTD7G1fjTCWmeoSZciTcMITkeKd_3kBReO1n0jJMfYWNyn81jbrSdQfzMbYvedV7bd6Fpd8WGSlWfeik9dS7gb8lsLkHqV8qTlxGO6MwGjbl4Rk-ET3G1D6QC2U2fSZcct6Iz7uwNgJ21tCfcnlONJblTo6rG90hNCBfayARVuBrck4KEFpO3PFjG_qa_hDCm7LDLMYAPDRWzafueb3t900U6Qj15ERjYYldsq8yLkxEHsG-SQVqw1Mgy-5rNJYmSYV6Ib26_PDMzWAOSe4Ei4GnGlbYJnmPk2Drpsx-9hdbCxJ0CWJKbzZX-MTTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🐐
🇫🇷
آمار فران‌تورس در بازی امشب تیمش
:
🔺
15 پاس موفق از 16 پاس. 6 شوت. 3 گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106087" target="_blank">📅 01:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-Tz6-zxrP-vLJjA3ZDmvCtJ0fCJe_oGvmEeqGkMMlrRZ5ewOyrMDrP12Xc-IGTPbYrr0HbyAbhrCgXKxKWWcor5Bq7gu0wF_OZvVyVMkKBzelceKUOYnz64GgFz4bJPE38suUO9Y8j3SkY7-pnXqPf3u_ButG5GRtZQ--ZvyS2mq4VhfywXbH4SOVunZyLzd7LcgN4OCzs_iXWqBpyUzVQkopuXg6mPTp4Vuq1-ytDm-L4sR_eoPH6uFSYklEWZgWmgbbg--tuYUOVUKUw1Fmk-Q98AG79C7wGQHlRPsgPvZ84tAUQuylmFyEz4P5ElwEezJ_fvKlUG98CquT9x3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برای اولین بار در تاریخ، آرسنال موفق به ثبت ۱۶ بازی شکست‌ناپذیری پیاپی در لیگ‌قهرمانان شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106086" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
دیدار ذوب‌آهن و سپاهان از هفته هفتم لیگ برتر که قرار بود روز شنبه برگزار شود، لغو شد. دلیل این تصمیم حضور بازیکنان سپاهان در اردوی تیم امید برای شرکت در بازی‌های آسیایی ناگویا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106085" target="_blank">📅 00:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LF5IzU1znFccvGbUrdpTFBCFairgVWlB4PCHtymSxnX_s6xv1ssvLScm_hiBJRUALfCkxI5aOvNJv_yyo-yqsEJDRPp7be4QtxK8gMNwRAqVTN-OeN4-QHG_U0BNJILA_SnkqqwEGXd7rlcBIHrONavYp1jfNYT86VcL2Uxvr6r4wH4L9SJyF9ZOr4VLxuPv29-uGkGETnOFAOUYvumr6ufDLVZtcp_pZE7rZrwpyF3cVRvSjCDs37uqkDWBw6AYBZ40uHNkufWybj-B75CN260Ip0Sngzsm8UAmRBZbSnDj6eisrRIaDgNjDj5YW2F-yoS_sGGITT7oTDo3j5HAKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
📊
نتایج روز دوم از هفته‌اول مسابقات لیگ‌قهرمانان اروپا به شرح زیر است:
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
🇩🇪
اشتوتگارت
3️⃣
-
1️⃣
وایکینگ
🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
2️⃣
-
1️⃣
اتلتیکومادرید
🇪🇸
🇫🇷
پاری‌سن‌ژرمن‌
6️⃣
-
1️⃣
اسلوان
🇸🇰
🇵🇹
اسپورتینگ
3️⃣
-
1️⃣
گالاتاسرای
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
ناپولی
🇮🇹
…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106084" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ2CPXt5XjRWZ5fiefZXmf_3QvY7g0VrwFN1vdlOFCJAAcJcjYHQyOacN3bQWu_7YSHUVoyaobBzcyeaGLc_GWkKfky3fkBfHTkBFp1G33GIUcHot5rIQmmsZVKhUoAENNvKoQD7cmUcX_zQsgQ5zK-gMiEFar0P_tNc88f3ML1zktXOBYObgt_QUzQZ6knjSFHGCQKq4AqGVvSSoX8o9BjxQ9NVpQnKrYhj-6W63_DNQerdBr8Y5v03WL0HveY4VbFB2l8Na5Z-S1XNw0GPBuB4nL3js51Q8y5TAqXmlRC5Kc-b0Qxzems-BKSn3fP4pmKjV1K2aU8QTY2VQlsj_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
📊
نتایج روز دوم از هفته‌اول مسابقات لیگ‌قهرمانان اروپا به شرح زیر است
:
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
🇩🇪
اشتوتگارت
3️⃣
-
1️⃣
وایکینگ
🇳🇴
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
2️⃣
-
1️⃣
اتلتیکومادرید
🇪🇸
🇫🇷
پاری‌سن‌ژرمن‌
6️⃣
-
1️⃣
اسلوان
🇸🇰
🇵🇹
اسپورتینگ
3️⃣
-
1️⃣
گالاتاسرای
🇹🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
ناپولی
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106083" target="_blank">📅 00:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106080" target="_blank">📅 23:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106079" target="_blank">📅 23:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG65tcEt6jm4Qnv-pjpCfOYg0pElJpQCY7M-pr3-WBsgrBrZ5ftxVB_BxkbbKI7S-7IJ-Fb24F90zzkyE8p52ba23WYF0J_hCE6x8bDLapUdctBjHL_gsUUuOc7Y3z6WrjBU32Ui6xJKurr3JvBSHsFVWZFs5A2uACnkUw4Hsbkybr_o-Z9nOBZ2c3I0SDwsfS0KVJliNbSLBgTBoE963l9N5gUx6vAGBnBLgjKgfb-xpfmHXRmUzHDgtAwBngP1MGyystuWpBUrR1DzjJqJ7ISmlIpar8y1L6GYLTqtMHTN-iw_UXxaxJZOlbofrPwKiKbealuDt0eIgkUiZRg25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
▶️
🇪🇺
📊</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106078" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فران تورس خارکوسه هتریکککککک کرده برای پارس</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106077" target="_blank">📅 23:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپووووووپوول دومییییییییییی</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106075" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
مک آلیستررررررررررر</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106074" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106073">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلگلگلگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106073" target="_blank">📅 23:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106072">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVwrvd47kLt5w8ZMUKFJnDYFQuFU1ry9XMlCQjOrQeCGsIFIn8lWcWMuH3dTDquEiRMNfzDHsRoMjAIxGviPaB2sF9ZxsUJNz9XMpnqcEb0him78pyBcxusenedg2-Y59IqmVAKytPOCXeWIFmdNHnmpX4P3dXTK0BWRm9vhs4K-vFhTGojeFyJ0BUzTE_HFtl3GpzL3I_jiqGb-9hQsc0LNgeLXCxjrlMLdoQKWIrqUaVN7X8o2qNvaakD20zBeKhfwWajoCQOXiveCnm_SV3R_dVFfrRjLaTCUf5Pbpph-tV0FbJ_gMydeWwc4d_SKsP-dr7VIqZSE_gcltbEnWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
نیمه‌دوم مسابقات با این نتایج آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/106072" target="_blank">📅 23:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106071">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPgUbDnNtMk6eOa1YLwhUe0E5XpHoIge77DymfzpojspqsVEcqT_WdhhfqDYTSDaCRUwn8uKpMpOv4GHvU2ZS1Z80d-N9sJFAkYgNbIGbhtC3eIWS6jUCrZfbcwSD3q1avWHDlGTyQ_W_T2ZmypvcmefMxtkoFWi8_qWxbeGoMgGjMQVsQJXJsCfRAlfanPungF3Hb2RzWTrSxZPK0XO5YMkwHFksy_OtGbc4Mo2w-ExyQzdPbWPNMdwedXtaOKWkb7faA_A09BiAFh3K453R9NuA9Svj7NhPXEDl1YTqGPjT98vkML5aswFkZJpcWLkxT0tJKyOYvzgCX_JJXx0sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
دیدار ذوب‌آهن و سپاهان از هفته هفتم لیگ برتر که قرار بود روز شنبه برگزار شود، لغو شد. دلیل این تصمیم حضور بازیکنان سپاهان در اردوی تیم امید برای شرکت در بازی‌های آسیایی ناگویا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106071" target="_blank">📅 23:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارائوخو پاس گل داد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106069" target="_blank">📅 23:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سوبوسلایییییییییییییییی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106068" target="_blank">📅 23:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">لیورپول زدددددددد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106067" target="_blank">📅 23:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106066" target="_blank">📅 23:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2sc5Nz4o8fRo4nuoy8BHbTLWABvUm5tct1hgpuQFGDApRy6sdLZdXMC34BCy3hXvazC2Cd6M08h5lb-s-P1mxaV5Ozph9jetWtiC_kbPGfpMFJeSiPq1okrbCVqt5_ubqXU9KOiZiZ-H-I5ZsR6j7fiajZs064nXxdc_ZQQv4LEMba9QaNYmIs8CfjwJisd1wH2SrMPARq6YONBBuv7qayK0-MQj7duc4dHojqYGtHeiD2oF-S7t9J0VbX5DAgWyJr7XRrSVO0FQbqpxy2uas6lVTKNnH1Cb5mP2b7YvwSrb_wCus36yFsDXcsgOrgH0n5TQ4oPtNs9Dl-rE5XSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.   چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106065" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106062">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پاس کل از آلوارز</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106062" target="_blank">📅 22:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106061">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یورنتههههههههه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/106061" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106060">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتلتیکومادرید زددددددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106060" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106059">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/106059" target="_blank">📅 22:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106058">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSXwRzi_Ee5DFk1QLFmlCuMS3KH0A3ODavGJc360_nCfnoqw89EZZceuAwP0_-j9l6ikdc0jUx5DQRW2uc9dRfu2eMuzUXIYXWHBFSPkbOLZg2VLH5FWIIbFul-32OsrQccTPMB7-ro8JWEykIh61NTZ1v9aB9R8UgOtbUbVvyVM8IYXMHzHPq9LD5_bljkGGgb9u1Ojr5kBWQI4l9uB9q50QoEcKxaa6tRa4t3M76tz7Dy2wtfCpHSPJuugoaWyLC4EU6eIRgM09JQBzcVr6wTprYwJGnH0Xp-ijcEOm5Y7w-tYo5lz2CWxlW7qLsNBY2Uu0XxPjq7QbGCz03vDrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
🇪🇸
🇪🇸
لب خوانی صحبت های رودری در جریان دیدار بارسلونا مقابل والنسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106058" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106057">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M62OZa4eFvILn47yGQfx73Xz2ao81zAey-GIRYBkDfstKGW5Pd60Gqz8tbxIbM_YIBPo9_GuTUj-mAhC3isHcmlJN3MOhH3XgIK8gIQKcP0qe36xA0gtvKdfTg-KS5qrhoE0t_8Ej7P4ApY5YdLV84aMfUK6fdE4Z-HzwW_hfjvJKZOxucG5xQwhxDYSzSlqA0b-yOtnMbrs4DFur97ut33R9ck-6i9AMxFro9b8GJngfHcKlQg6KF70sQ2N2xM-YqLOsOInxpReakCWtnCIdn2Qe33Sf8q3g7warfEXUihZTVp7CcneMraScVPYkEsM7QLGvNPR8LlC5zylC1TuAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106057" target="_blank">📅 22:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106056">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=gcNUAgOr_w_s6dqohRMlEqZhiSXKJNREz23e7U2oX496pqGlT7M2LZJV3Y7qYd6ne65X0mqTLcaHUhMK9GJVyE3kGOZDfRr_llsYZULOzHMoE9BYDHfTaaxyjWy3icIFU3odBP4C3SGWt7Nha_6POEeh5UPGQopRtXdrWfuc-RKYLtr-eU7tP21FPiPoYfcasoUEsy_Amf1PowLKwU3QPe5b6yghSzKxa1qpFs16P4slxLWs-URz-uS0wnLeIqqYZa2aKLRYEBeCh-9Vhcaybk2P5U3BBPa_PZNwvMdP59RYn6NcBbLGIFzEePeuD62qpsCdkKnnlJHYd7FznzDkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcba68c3d.mp4?token=gcNUAgOr_w_s6dqohRMlEqZhiSXKJNREz23e7U2oX496pqGlT7M2LZJV3Y7qYd6ne65X0mqTLcaHUhMK9GJVyE3kGOZDfRr_llsYZULOzHMoE9BYDHfTaaxyjWy3icIFU3odBP4C3SGWt7Nha_6POEeh5UPGQopRtXdrWfuc-RKYLtr-eU7tP21FPiPoYfcasoUEsy_Amf1PowLKwU3QPe5b6yghSzKxa1qpFs16P4slxLWs-URz-uS0wnLeIqqYZa2aKLRYEBeCh-9Vhcaybk2P5U3BBPa_PZNwvMdP59RYn6NcBbLGIFzEePeuD62qpsCdkKnnlJHYd7FznzDkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حملات بیشتری در تنگه‌هرمز از سوی ما رقم خواهد خورد. فقط کمی صبور باشید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106056" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106055">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Tk32CQSXehn1o66tzNwRW7lCqN0dF4VkbUu1Wi7sFZOJHQOZ-jSNjtQkn14HnO3w8rx_NEdSwWAeHHtCdwQLTDWyYMZ13x6jRZgUtxb76bcgKRe6F6m7VUVN52kUY6DYC1kNi12xgWshhYuqp1J0PFce6dulQwT5YxLnV3QRsY1e_feGuTjnYAET0L2EDm6j2pG0YvipMp7Gvpteyeh_6SekRWdOwuX6iAkEgB2q3X1WyIC8BTiOqDX2aTT9jBVq0dVtBGnpA9J5Vy1BEpZaYfMibq5G2k--YF-_6AjqwT_qDCuwy9qWie2dbNUwORNeAfVxsixfcq2bPfn7Tykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106055" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106054">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5y_R6Jxb73ysmMUTCmUPvH-fAUVyWDeqJWaGDL0bSe1EYCcgxOeKhW5NJD0bkUm0bXstUTxaOjNdk-e-wk2RIDyxb3TyMsuseCcgA7bQ3QjrRvduFPPGXSulPafjP5_m3dMNe1YLC3EAMz38n4tFVfVmYOGg5jQU8tsrCQXnwLr0fDX54NQAA6XUyzvgoQ3a2307pGLERNdO5RvxMt2v98HgfJwNbChCJepv-YLIG7P766t0CKyOM7hqMkgmVDSi9bSc-BKlfagTRkfHs_Y_d8lDK5rlQ0bvb3txQQpTaKEsd4cm2hJT83VbjBRVj26rUAkDEx7te5ZONvJvUPChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
هفته‌اول لیگ‌قهرمانان اروپا؛ معرفی قربانی جدید تجاوزهای بارسلونا؛ فاینورد در نیوکمپ تحقیر شد؛ رافینیا و یامال مجددا درخشیدند
🇪🇸
بارسلونا
5️⃣
-
1️⃣
فاینورد
🇳🇱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106054" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106052">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گابریل ژسوس
😂
😂
😂
😂
😂
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/106052" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106051">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پنجممییییییی بارساااااا</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106051" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106050">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگلگگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106050" target="_blank">📅 22:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=G2ppwBCLEFBCE6XKao95MkloSRWStIfniRpOa4dS0wNxKe8_Xve1uzGmWdUkOIeEuj5P7rgWjcUDepW2r-Eej2v83fn5k3OYMxAhDSJJLckBq_PRt1z0ZKlC8Lq8PpCnEwx6GjEG2mJc0ygf4_228TG_3CGW1a0OrkPLjspdjb1gP1WEeUn8eLFs0wnI2u1xpqbp2_gsYK4rJrE6YDUTEJTt7war7N05_2PGPv_GF-a9oEXfojo8OJt4T-Vfyqm8lBaaZeuWm8I56K_Sc43Or-BIdM4R3TNhncD3GC21BcIClEaZEzXzoWTP-Fiu7gXTfnUdse2McweZyAcXvHDWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cbc91a214.mp4?token=G2ppwBCLEFBCE6XKao95MkloSRWStIfniRpOa4dS0wNxKe8_Xve1uzGmWdUkOIeEuj5P7rgWjcUDepW2r-Eej2v83fn5k3OYMxAhDSJJLckBq_PRt1z0ZKlC8Lq8PpCnEwx6GjEG2mJc0ygf4_228TG_3CGW1a0OrkPLjspdjb1gP1WEeUn8eLFs0wnI2u1xpqbp2_gsYK4rJrE6YDUTEJTt7war7N05_2PGPv_GF-a9oEXfojo8OJt4T-Vfyqm8lBaaZeuWm8I56K_Sc43Or-BIdM4R3TNhncD3GC21BcIClEaZEzXzoWTP-Fiu7gXTfnUdse2McweZyAcXvHDWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔥
🐐
گل‌شماره ۹۷۹ اسطوره کریس‌رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106048" target="_blank">📅 21:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فاینورد بالاخره یکی زدددد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106047" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گگلللگللگ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106046" target="_blank">📅 21:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سوپرررررررر کاشته تماشایی لامین‌یامال</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106044" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گلگلگلگلگلگللگلگلگل</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106043" target="_blank">📅 21:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✅
🇮🇷
👤
برانکو ایوانکوویچ: بزودی برای تماشای یکی از بازی‌های پرسپولیس به ایران می‌آیم و عشق و علاقه خودم را به این تیم بزرگ و تماشاگرانش تقدیم میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106042" target="_blank">📅 21:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGxYbeHyqr7WiFX5M7XK7xtKS9Ddifi1mT06a_TpKZ_V9PS5NiuizaYP150HYkY14TA-3B8rfAr58bupmas5M65BkmNe356oWlb3lkP2d3cuzxqNMcW7ZPrK_CLX357bIzNJ1MkM39XkEixfagXTPiYP3oyAuk-PJEMg9o1y1PLQnzCM9jJa3b6yZv_e9eih0eNLba01ePDqgzXjIGUQioQZAEIjExtlXmbMzwKUfcAejIbLuczcbWKZa7Wo3uqTAqiAHh-KpgA8rVpsmIdGJdJmOSTP1Ys0jtSUGR75f4KL6xB-yM-Mkh-50MHhFnkB8ep1Pn8a02iIQBXyyJ9SjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
گل فاینورد آفساید اعلام شد</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/106041" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
گل فاینورد آفساید اعلام شد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106040" target="_blank">📅 21:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106038">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگلگلگلگگلگلل اول فاینوردددددددد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106038" target="_blank">📅 21:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پدری چه سوپر پاس گلی دادددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/106036" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رافینیاااااااا دبل کردددددددد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106035" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گلگلگگلگلگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106034" target="_blank">📅 21:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1LT5__9zBngAmgGAGZcBJXMazHCbR77PEkmvvslOfIlqn7Kel3MJF7eexxJVl0cc6eHncFz6o1esH9LKbPFZ7A_hM_-ttoCs57dN4K4KnW6WemoOm9lsdsAy4GfVNGxmqTMIUlWtHs1safABHqpzyPjZ-h0n_Lmx35GHj6sAOCsrf9HU47lhRO_gAxBcg9tufNZAaL_5T4iOXBoTYaW2Zmj90ne77wZMXPo16oiYPOaFkRzdFsAOWhLsPOPG4Op05AU-r9yRxi0ltf8yBf0KJpxL4RP22XoFXSUGwjPPvWa7ex6SU1bePHu_FwEHY69TAo0atqU1CSAM3Nvssp0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚡️
🔴
از آیفون 18 رونمایی شد.
چهار رنگ آبی، آلبالویی، مشکی و نقره‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106033" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDYStVaIUsymotf7UFEpCz-jS9kAyFQfb5s5lNcNqQhOSx0sEYvPJmXX6TIAszv8GZ2hNKnBrZWNc8IoEsRJUNEUyinLgfATEMqki4Y3M67i6NiZ3Etc8NmlGpQ-fVtPx5RXGqoSWOCpw4bXIpn0bRqmuiPKjQ8iP_lvnOsibijdSuafhzqW2yIlZUL0YNrTQrX59ThRFU0XEkcqTzCZqTo-B9Wrn72NrTfZ6yVW77iwmqAtknNuK4Cilg2tgFZ7QRKykQ9PUHZaPEy86foho02YIzThKt1YwJLpBi72GNCBjJEEdJVuUag56f5U1F7z-_w_BUdRWLDWrxM7etVNqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
ترکیب لیورپول و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/106032" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxVDOEpSK6_lr-IlN20Nlkko1G-UVNr67FOskFR-f3VyBt3cmluez0QAJicT6ukZA4eCbWnDav2bWsg76ya1SOwLTStr6soaQ7Yf8Ed8-TluvhIzhqA74RVltbUCVvrTOah3rA5dzCD7l0Bxsy08o4q8-HI5jQz-9TB0OPErE1hyQuvcii7sIA7H7hH8GpeavMPdy-Jorn7c3GoQ59yj7LRKYj_PsveXjqdO6onC04dAm0ZEJ2huTFU7CI_5p2tz9dXPoSY1gUB_Dt_jaDOufjO0ziNqEY7RElVV9T0oLyq2sLi2KCWftOlOuFqZJ3ZTaen6i-u_lmZzFUQzFJJKug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
ترکیب تیم‌های ناپولی و آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106031" target="_blank">📅 21:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRqj-Tb3A3rMM081ZyUoz-E96qR7QTr-9Ity7zbx4v-Ak2LjWvykJAZzk3nXEBz95EDBCGbSpbJUC-Ofu0H54ok6Iz3FtjmiCTfT3YtjOoklYCjQbgQb0lShGyFbcbr7OrqqsX3ILZJBg6sTgQ7_evbjtNGsKxhIoBnt6mpK6Q_HneSe93sAWIRyEdB-OmsrlbRlYB0UNOnMVdzyvHhTuUNq7I5z6g7usNYvqDtvQbtq_dFQ_m6EC02FpYzZeN_YymJHOiRP6i_sZZ5Fvf0Br8IiSPxBIegEcG-nEXS8IyNk3jFKo6lCuX6ZKwbojuqQCFK7gPD0riwut9LXVkfGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
پوستر باشگاه پیکان برای بازی با استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106030" target="_blank">📅 21:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106028">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JD0tCP7Bevx1DDkCy-GwCkqLn2TV67fJi9oK2yT6a9cL8gLDg-tVzAW-4d-m2m-1uZnpd2dKhwl1JRh9p76gV_BZxGNosCEMRvQIwZ_Ex6kpq8cVp4PtatHWxYcJSEu0iKcMhYLJBDbbZ3gswFyMcbJA8y-0PBqEoIYZd3hYG2v-ykb3OojjVk1D-ZjBdw6jh2Cju73TWtS_V0EDbdOMQL_aEwJNTztEucKD0d2WBWDsO3aYPvmjhuWIZmKm-udK4N_TTx7k9NQhUlzSgt2D7vtWhsr8v3t8J3wJQMW0_PTt7CK2PU9qYc6q3sc1XfZ_yn6f3jfgdQncOIZ2a9E96Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شادی بعد گل کریم آدیمی
😐
🔥
😐
🔥
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/106028" target="_blank">📅 20:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوپرگلگلگلگلگلگلگگلگل کریمممممم آدیمی
😐
😐
😐
😐
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106027" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106026">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گلگلگلگگلگلگغگلگغگلگلگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106026" target="_blank">📅 20:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106025">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6q0WlEMQdiDIbX6prcp3amUD_okc6dw3WaS5btUMfopM39NZRg7Z4B2wE5g1n8q_tDCyrdu9X8NH-Ke6f8PDrxRIzbboCWkS_FRLoWF7fbaQkaPPCmA9_aw2vOxfshDp8RK4Ot2MxAPIyBLyx0rylHKgjonWzSZem7jISgCaIA6MRVBQyB_HmdkRNkf7HddtXbRL70vgoPA_FEuiYM5XcUf8OUD7VncntpIWbEoBVIE0nknF41FMCXNTQ6lj-l49b1gio_IXavriN5w9EbqIXeSTJ47icJM1XEEd3tx0GJY9XY-volsTR4GAQvmH_GBV61Ufs2GqVlEfbQpwoay8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106025" target="_blank">📅 20:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106024">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=RgPGkijrg9Y7rUz8-WuOQenRaBItGGtlqsgGZmZweGzSCC3lUZHIZRD91P5mK6r5ilZdxTBQyCraOTZVia7yv9g_CvFR_vNgnOmCShn7Y_UxMTIzTQ7Rc7eB6g_iyKT0b16iijk4NFMoGLRE5LL7pp3qsxHknZbLJqeRgDHC8xxgBzj1cTduQeqH-NuJkNIue9OpHm6U_7bDqtMjHyinBzXQCzERD8HCMpFOy1bzIpC-7_OhuaKeSndD1-X8gPDSJvmKFPlGRJp3Rbrwc689pmy5wu9xxLOQ5kNKgNahcF8Glh6HclPDvrQefqoSHdRqWk01pPRTqTwceUhssxOL0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1f0f0fa3.mp4?token=RgPGkijrg9Y7rUz8-WuOQenRaBItGGtlqsgGZmZweGzSCC3lUZHIZRD91P5mK6r5ilZdxTBQyCraOTZVia7yv9g_CvFR_vNgnOmCShn7Y_UxMTIzTQ7Rc7eB6g_iyKT0b16iijk4NFMoGLRE5LL7pp3qsxHknZbLJqeRgDHC8xxgBzj1cTduQeqH-NuJkNIue9OpHm6U_7bDqtMjHyinBzXQCzERD8HCMpFOy1bzIpC-7_OhuaKeSndD1-X8gPDSJvmKFPlGRJp3Rbrwc689pmy5wu9xxLOQ5kNKgNahcF8Glh6HclPDvrQefqoSHdRqWk01pPRTqTwceUhssxOL0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گلووووووو ببینیددددددد ناموسا
😐
😐
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106024" target="_blank">📅 20:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106023">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGQAL6QTR2ApEX0ka5gLxO2cASoG8a8lubLXgbLY1jmmagxzGm8Yt-eBp5eApJfO2qQz0dYeCCv5AG8-9V5wEhMjiHCqpKQQu5j_WplXZh2Q425clCv_o0pWG-zfbH3q7-iRW2ZRFmX7rIpwf-C0UbidaydCJUPNnnXv6BrFcI-9dlXl8WZy24PPQL4FkU_aKl8ZSO0Gz2qNQG7rcpXT_HfunNMVm5RmrRpB-m9i1qcon0VCL_rzNbHy9iumMEuZOf6FcsJ-kME4GG3CRtIyFS88QGsQXFBWnkW5fvJUShu0wHvUGQqoftpnZyQnKQ8rO6J1tN3E7JxaxBCuyHtCwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که سر مدافعان فاینورد آورد
😐
😐
😐
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106023" target="_blank">📅 20:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106022">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینا چرا این فصل اینقدر وحشین رحمی به هیچ تیمی ندارن
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106022" target="_blank">📅 20:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عجب سوپرگلیییییی زدددددددددد</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106021" target="_blank">📅 20:20 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
