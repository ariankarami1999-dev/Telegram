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
<img src="https://cdn5.telesco.pe/file/llK7IPcic6konEPbVGFxlEjg5XxBRTDtANNjc6nAKnpw1qBD3rJLmwSkSzBL2Fimt7EzXMHkFsnJXfZ1HBDDHHTT_vo6S8de0DXo0RpXETArp5Viz_5_Sbjmn41zy4rUV5-BdG73iXAjDIOI8paJvoEyvbqtGbjNVOZ4KiqKGsz_RGS0XZCuTyjTG-2oyiGkoBtApPEygPkYLwDfEzNhtHDxKbzyktig0B8iE8Xd-JbxkKcscWo4U9Ueua8d0-fZhzW65gIBxZ9vLu7w30nf6YeaWXAuechbYkDyqPwU1Itk-NdvvBLuhBhBsVrwp8QXgzrVbg21dIu4Cw7K0PqPYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 280K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 23:33:16</div>
<hr>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-u6drWgG___NA6L4vXR93Lfy64EdagUnH1wRR5figihyyepMSBvXQMNIIFefV97T7zOEwpqtvde_aHxNfj3Mb-T6xk351QaeWymLPFiNRsWFLpTKBwTDa5pA1A49JBP362BlZmjQlBxcCbPtIjxRX-5mhl6wygz0bwD-OiKzBPE3OIjl3Onm5NRZZfjN2Bt1CD6nPZA9aQ8_dd8s1apNHT7nxXQmKyZRNCN2BKewhnbzFjXmDtdj1e-FnM8io9JPLZZWBw_C8Ao9lPbqQz2t6VCiFKXszz4ZyRlQVXuxJljN4JszW5B5t_uJFwn_6MpWTPH3ss2KRdZqtx6ao-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اولین خاطره‌ای که از جام جهانی داری ؟
🎙
یامال : بازی آلمان و برزیل و فینال 2014
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/Futball180TV/91610" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jT-dgQwUjmOTyBLP8ZwFgWfK4InpZrxzlKnoF5C8r31SilmiX7K6dpP87V4IykmItrhiyf7UGElKOX2HlK9IUc9bEexQqMrWsAbLBRgpUkFBD_hHL8sobchKd_FCc8LgRukgLB_o1JJxzYQE557FimB6GakFbeHcyhx9GWMcIEAVC-AD_gSGwC9yW6iXfnVuXJNIlJq-j3GpS11zmU6S49RozIwKsu1hkUSQT7sIfoQPDahiD6xmiklE9xJ1u7CfjuNx4NJyHylQaFl6QJkHqxW32IPwpjGzn0ALdR2GP0sHnvUlr70piG8lkF4niV7ZR6ZIgav3_-e8bvAgD8Wt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کیلیان امباپه دهمین بازیکن با بیشترین بازی برای تیم ملی فرانسه با ۹۸ بازی ملی شد و از لوران بلان، وینسنتی لیزارازو و کریم بنزما پیشی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/Futball180TV/91609" target="_blank">📅 23:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43547db82.mp4?token=FoLiowOkxpTS3PuZ-ELkZr-nJMMISgwa7TvRd3zb7Ml0RCJbbgfz23PjyCmrR-WNHgMa3Dne-loaU7gG1zc6yI-RgStgR9WkaTd8wNEKwXbC-wDF4EB_M7HhV7oM13p4Ev2u1KgU_BEJpolvyPWfBsARoDzwexMZG9yVtC83H1u_UMmr5sLRVKKIrdU64MweMC6ISaU3jJ5_Ia_Xr6_7_pj3jAzgDMDTbFsESpFwPw_wnc3JRZ7p_UKspQhA0AD-ateDJ5_GL6twuMhjSvXWY9tdqVTcNS7EMV8kwrLGQQqMMTxWt8cnzZr0E3q5tLLPFMpTQFIoWA4DFiA6S7fJ5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم اینترنتا وصل شد گیر این فن پیجا افتادیم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/Futball180TV/91608" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Yyo0AnNU2pOVj9W5f_oNnE21hsp0nZTLIhPEqU0ZEp_nLaA51CsY-5mdTUGU-pZkRACAyFBj3ih0ESKQa2uBlcQ1xY6VAW0p8p99avmCHBqR4W8_5fKawLW5G015G7O5yAIYbp2fQUQZOesNqy0QEne1m1ozqPHrWIrEbBB9f3GtxY5RrxiJBqe6PRLRfU1_vB3yy8Dyi8f-vQZ0g-CNE_4qqRokuLdxUIKrdtvAyVw3OgRUskHQisCmMJIOUIrkRTS_Ot41p72QV2PFaY6oVHpZvoaKJO7qIjJ4rwda2xocsyKSeKTRhRV_hmUk3sOllg-Lq8mpG-qm-YPWjNCbyYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این طرف تو جام جهانیم ول کن گورتزکا نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/91607" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=AJjV-Ie_sP4W9iT8H9yhksR03l6tNnmrZunUpw-nJy_CfcSlb9v7wnbUD_iBEkUUYAUFb4OiUqKDlVmphV9lIGVpk0U7whZY__Lf0-xK1mx1DDFiQObsd6CoL8cdYdQnQGw_5P-Ki3Em27BZmlK4dwU97-K9CzbuKHl0R9NIZ89adFxzLlBPHgUfJJqikuPe7f5k75v4K7b895tFhHiwemNS9L0QxmU-dURikBSE5nR4Af1aYS5Di4bK8pCGSh0GdK9Wu-ieIorhUUF4XrC_-qcDCnVKDAbZKyMTsLeZKtxDYwYww81DoyoWljOXh2xtPJomAEqAvB83yJ2C76TDwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=AJjV-Ie_sP4W9iT8H9yhksR03l6tNnmrZunUpw-nJy_CfcSlb9v7wnbUD_iBEkUUYAUFb4OiUqKDlVmphV9lIGVpk0U7whZY__Lf0-xK1mx1DDFiQObsd6CoL8cdYdQnQGw_5P-Ki3Em27BZmlK4dwU97-K9CzbuKHl0R9NIZ89adFxzLlBPHgUfJJqikuPe7f5k75v4K7b895tFhHiwemNS9L0QxmU-dURikBSE5nR4Af1aYS5Di4bK8pCGSh0GdK9Wu-ieIorhUUF4XrC_-qcDCnVKDAbZKyMTsLeZKtxDYwYww81DoyoWljOXh2xtPJomAEqAvB83yJ2C76TDwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار ریدمانی امشب امباپه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/Futball180TV/91606" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUoUt_SJj8C3eOn08m7cHXCjki7V3DCbvs-FPe3lw3p_IUd21L2S_PqIc85zAamD26na7meJI4n5udXTZVBLpJxcSw0NUlAFtF_umKf5LJRKZLxmQV6uC2Nvj-DegNU5g_oIGakInYzNWiCwi7b3tm76kvGwVplKvVB6pgKafFg-TczhmlJJ0qF8uNVSbrGK_7OO84kvwcA-y1sL5gC8YepFdOFMEbQQPWyihGpastIl_l7gdYX3VNdKkcHQR4tjY4U-xO0dpU7TYfrjH-HTFF9hH9v4PwncIrS8FiM-3Sso30d7TEaFG1ciJOgP5-yjG67nlcVrrpkGdj9jpdMFXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فورییییی
؛ در نزدیکی کمپ تمرینی تیم ملی سوئیس در سن دیگو آتش‌سوزی رخ داده
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/Futball180TV/91605" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=WkmMhO-obXCIy5i7xJAiXSEn3aBAeszoPJwNlEECx1_V5oiyWdkdijveQnk-ZK10turLSTVKXNNOX6cH5ibv-uuB5EcEnw-OwVteHHhsbTlHpzw9FaUtrceBm9B65z_QeKLpsWtOCQxnpUESWM9-ioXh_4lMuUYNI7FKGmvZQvwNx74l0WdwLUS_qjJv-0NrgmJtB2moFSvWYFjLLTn53pAM_hH0BMHG4FHvVV1V8qTCyNsMU_EneHTMzdF9vDEi8vRqaX5-01JYx_kanwOcH58FG1AJgnFHFa8EiGFcr6Gh2gTijHxLv0Z_VT-32jdQxsjpT3WKc0dbgyVVqkt6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=WkmMhO-obXCIy5i7xJAiXSEn3aBAeszoPJwNlEECx1_V5oiyWdkdijveQnk-ZK10turLSTVKXNNOX6cH5ibv-uuB5EcEnw-OwVteHHhsbTlHpzw9FaUtrceBm9B65z_QeKLpsWtOCQxnpUESWM9-ioXh_4lMuUYNI7FKGmvZQvwNx74l0WdwLUS_qjJv-0NrgmJtB2moFSvWYFjLLTn53pAM_hH0BMHG4FHvVV1V8qTCyNsMU_EneHTMzdF9vDEi8vRqaX5-01JYx_kanwOcH58FG1AJgnFHFa8EiGFcr6Gh2gTijHxLv0Z_VT-32jdQxsjpT3WKc0dbgyVVqkt6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زلزله 7/8 ریشتری‌ فیلیپین اینجوری باعث شد این 3 ساختمان متصل به هم از هم جدا شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/91604" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=c8wOahAZJpwLOSu2UNXhW7akuqVhjnOs9bL2a1ta6brCGj9AenWfPKduod9oHeC0LgquMFMNO_rM0eHAFSiZEVey2eFufG2CcTjppNcy3Wu8UgqpmxCWrjX8QmfqYz86aMMK_a2ec3L5CIUPl07e8PacAXBP7KMzKmGBFBlxmynsbcWsHvrFTa5CWi8s0RFHecvFUnTUJ11c79mNvfQkVG8gM3DHOhaVg3DVRqaa0qmRaY8O8LedBUopsgA3MszMr3eJm49KBiLI_8eRDCXWiqTfC6ABoSVeXmLsIHrSrdSV615UfuiXFsg-dnfu-0MiwQYpI5Ib4HcdJOv2PdEbWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=c8wOahAZJpwLOSu2UNXhW7akuqVhjnOs9bL2a1ta6brCGj9AenWfPKduod9oHeC0LgquMFMNO_rM0eHAFSiZEVey2eFufG2CcTjppNcy3Wu8UgqpmxCWrjX8QmfqYz86aMMK_a2ec3L5CIUPl07e8PacAXBP7KMzKmGBFBlxmynsbcWsHvrFTa5CWi8s0RFHecvFUnTUJ11c79mNvfQkVG8gM3DHOhaVg3DVRqaa0qmRaY8O8LedBUopsgA3MszMr3eJm49KBiLI_8eRDCXWiqTfC6ABoSVeXmLsIHrSrdSV615UfuiXFsg-dnfu-0MiwQYpI5Ib4HcdJOv2PdEbWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ایکر کاسیاس در مصاحبه با روماریو: «مسی خواب و خوراک رو ازم گرفته بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/Futball180TV/91603" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIeEBP_-ql9LrejKB4ljS6WBwD4cNC6eHiyhLgPyvc2v72c5kMgudypCNhMdWhKoQk-nOT6lt9L_Lr45J2rCBCpNaG1bMRUGNHCeK-BJRPHtr48zzKYI_0bDJqqjXyTGU-_NSE2i2LaxUoPypJavEwgmGEqZ102yqNnh_oEQu91ZWYiGVD7g7CAcg36bFpZGQAlyADtjSqjJtZjHIsGx0Pfjbw6UNVRkeJUDWwQ4OcSgrVYqq190Zk5nsN4ZjRCGp2U5n--ELhudmAXY_G93T_w_7Q6Co691VGfbNyFjU29U3dZeHMHMEEVcEQgkvN8efrQlHuqJ4pjZbeZ_z-w5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو گیمارش:
«برزیل هر تورنمنتی بره مدعی قهرمانیه. پنج‌تا قهرمانی جام جهانی داریم و این اتفاقی نیست. فقط باید تمرکزمون رو روی هر بازی بذاریم؛ اگه همه‌چی خوب پیش بره، دوباره قهرمان جهان میشیم.»
🇧🇷
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/Futball180TV/91602" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzMbeR5mUo5KQA5ye6xLpaowNTsPbJZyp10j-KUpeRug0TkObMmOJE0u8HFT6aTW94e3KXiQ8XMtTOAvtmjP9-xqHYVRFDcEjKPZKTCKK2pMpuSN8N5uwG021J8EvR5sRkfcQT_qddGqm9jzw7Z0O_UPgE1eJvA2EeC1Y3ZE0-rLrstKkXZ_sJ6JjjSRrKavsT0ZAApx-_d5at3humsRHWrX8gX6Si_nUr9jEul_BPGvxtY7oJcrJ2Qlk4gYAR8Yndz3FTsTtRn3jSY7sKP6JIJGZTtC8J-LtCSKi-8BEOo0oUNUpYeJc0FuFsbvhV8izuHzINFFvUdmMJP5Q13UZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDhdnTG4K8xUXaEpeT7D6KCFMXYAOtQWkyo1Rj3cBbUWWUkztBKgWnLQ0G-P3ua43zRaii_GngtSXW1ilN-jPf0eDJBcneyLix_bD47XlySRDwCim7EXviF9tIW0GfsIjIe7OuG6WMAbjU30wwgh5IM5hiIMiqGDjpSEPe-_BJYJ-Gpe8npf-mCUjsWS2pSijXqvyOkLOqzD1SZvnwiuZzw0GN10lJXDd3VJldOCFf8uKb9n0q5lvhNjI77fpG4k08L5IFRTwJnBQNywLcUuQprWk9MSR7JSvJGj4NhRx63kXJ-mbfFG6gQO00HO-dGC1UEgbC5LMDJM8Wui_ZFwtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/Futball180TV/91600" target="_blank">📅 22:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYO8_vrVA5qOnImAiDC_F6Jv0Ia285JxDhyUxsSk3YX3fwX8vQANUWXay61F4oVvosiKpCUO3OXfAgFDuXUUaIEA5TJPzvljsYSdHOr6rStrWM_HuUY4KHlFBJ0T5zty_91TeuyNXnNHq0zU2cLKO2NimwaDm2Hyb4DRNr0EaONiyzXo_JQt1l8RP1SFeOQruylcfBt8uwe11x-NEMPOxZHesYbB9WVPYAE4Kq6B0eALgtZ-rcvfFqEt_gylO8J-qdxNkg7Hb3KqGoVexVkSLudPx56QnA9kIzDWhpg4pVg9kO4-puJjnWFxibScjpQWSrjn1TxJjZmzQay3sYK7lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خوزه فلیکس دیاز :
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گواردیول میخواد به رئال مادرید بپیونده
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/91599" target="_blank">📅 22:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q61Ovr9EXDIlncjpghHPTI5QN563ApXdoetAeIIVCZ4Qp04RrtGI1CnHSFrhPPIyTi3qRGH4VhWHWrq6yBHSJT3AyGZ0cGin5vRcnZDHatPDqDNAr745GOIH-3AfefgAw6cSdW4hB1faIX25KBB-yRJ6bp1ZFJrHsADyZaBWie_CxifjSbqcTsYpd-Q3D4gDCiBKJfRw5gASGK7IVVpu4_pvrpFpYKVwz2XfQbjhn5bl5mYM3yQsCf2rE4L8C0PtTvs6Xz1ZFJYG82tEZZ_8VAT33IJzzmJBn4STFIY7ZWeU7mVdfMMW_FPuOM6ktys6msZ9-EsnVZuE9IztlVoPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل: نیمار روز دوشنبه MRI انجام داده و آزمایش‌ها نشان داد که درمان او به خوبی پیش رفته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/Futball180TV/91598" target="_blank">📅 22:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkXjQHc67SSBEygb77z9tN-2gAkHxawtDmHnLH90DPMQWlJkafFScfTdi6goWOisy5jkaTOZQftjsMgi_H9GrEA70CX7bQP1A3lmHfvFiZGmCO999cu-BnG0ddDfJ4GJzeEpe09fDImudeD0lbvQ32HtY1yR0009PPb_lGT-rlqOCq22lC75ljLNwtuNTOtNMeALSakdV3MHXGlCFPbJJyGv_A2s1kxEGLhrxSHXXLUpKGHsenI2zU6E4EgXsG_3X4Pga5kJeBPmhmoI3UPwJZTaylqiJq72DNKkcDonB1WEaq-SmBgXmG51Ay9hbLunkzkveqHbGOrvZp26QMohoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رومانو: برناردو سیلوا تصمیم گرفته مقصدشو بعد جام جهانی مشخص کنه
❗️
بارسلونا و اتلتیکو مدت هاست که با ژرژ مندس، مدیر برنامه‌های برناردو سیلوا در ارتباطن ولی خوب هنوز با هیچ تیمی به توافق نرسیده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/Futball180TV/91597" target="_blank">📅 22:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVPwXO6f_bx7EVKFL45ZlOdIYyOQxbNj4TakspW-ej8S4BJCXfM60OHUNb0qiYGYScNbRF9YKs_mOhMYpKIIjFXtbPFeNVH9laQaN9blHQlrDdWw28g7q7vNrx7__ih4n7_HsLYgvnsmEndf1FWhLwwB2L3TpENsGMuVkChyi41ZCyHSfkXBibejrby2cqhEat3KV2XZ3528ocwm73CbNRDEptpLDfXUQW3z5B-M1dN0RzIqKrnArDfITcImtJLOxdaSWkJ_veSxLJ9G4x9DStfvGbfdjfZH3Ny--4-9W6ILdSmN4jwR6UPSLJ0px1TW5A_eqkkMvKmp8EpLjRnEOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
#فکت
؛ مسی زیر نظر اسکالونی داخل تیم ملی آرژانتین در 7 سال اخیر جام های بیشتری نسبت به تعداد شکست‌هایش داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/91596" target="_blank">📅 22:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=QC-3F7pvBk4if0lKo0SjUFBbJsoFoavHnmY_Jel79CA8BueYHukhQrE5hbIzyHkJhIpMPbUp514kybyul3aYrQMdqR3rQy4-hMAjXS77IaoB8muMnCaPGMWWUafjI4tHq6soMEKNpSXZPuJRVpXBQVH8-yFepf6SkGdrpJQtpu9PzIES52x20jNLwufdjPuopcZHeC6Wt2OpHpHk1GexB0gh1_gVCjLhLzCg8BCM579CTAlgjYY2R8xcR7-cLLtK0u31WODb2m0BytZkAzR6ANS8Kxgceue3Z1S7pLDIFpaXlf1PYTTJBJHyNpFamrtfuiouIpCyNt5cPLKAupDKNx2mecFKwgl5Y7sENS0VBuSy-FZKEC7c5fYAi8aP9ZloFpahy697P0F5c2F00YJ3X__uj-chMpVrCFw0rCvltA2N3psvVdBDved9hBf5TxxPaNtibIlqNaMkCjKknsm2smsjdBP_juBvehAeljqrFYNXd7-GQWlCN_1-WuKD5e7eH2ZBzXX2JC3uuFiD_uzUO6g2uhUtqW3p5nF82easWX_Mu1IrDuMoMJtzt_0LskuYh1GcNwvY2dZo6EbP4Wl71DwiOMfZs_B5FiPWaSzq5kyBzNewYv8NvyKCGRjZmfDb7EUnpkGelNsKbi7J9lG5vbLvTEiCE9uySXvDMC-O9DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f1d33e7b.mp4?token=QC-3F7pvBk4if0lKo0SjUFBbJsoFoavHnmY_Jel79CA8BueYHukhQrE5hbIzyHkJhIpMPbUp514kybyul3aYrQMdqR3rQy4-hMAjXS77IaoB8muMnCaPGMWWUafjI4tHq6soMEKNpSXZPuJRVpXBQVH8-yFepf6SkGdrpJQtpu9PzIES52x20jNLwufdjPuopcZHeC6Wt2OpHpHk1GexB0gh1_gVCjLhLzCg8BCM579CTAlgjYY2R8xcR7-cLLtK0u31WODb2m0BytZkAzR6ANS8Kxgceue3Z1S7pLDIFpaXlf1PYTTJBJHyNpFamrtfuiouIpCyNt5cPLKAupDKNx2mecFKwgl5Y7sENS0VBuSy-FZKEC7c5fYAi8aP9ZloFpahy697P0F5c2F00YJ3X__uj-chMpVrCFw0rCvltA2N3psvVdBDved9hBf5TxxPaNtibIlqNaMkCjKknsm2smsjdBP_juBvehAeljqrFYNXd7-GQWlCN_1-WuKD5e7eH2ZBzXX2JC3uuFiD_uzUO6g2uhUtqW3p5nF82easWX_Mu1IrDuMoMJtzt_0LskuYh1GcNwvY2dZo6EbP4Wl71DwiOMfZs_B5FiPWaSzq5kyBzNewYv8NvyKCGRjZmfDb7EUnpkGelNsKbi7J9lG5vbLvTEiCE9uySXvDMC-O9DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یورگن کلینزمن: در فینال جام یوفای سال ۱۹۸۹ اشتوتگارت در برابر ناپولی، با دیدن گرم کردن معروف مارادونا قبل از بازی، شکست خوردیم. همواره او را به چشم هنرمندی میدیدم که با ذهن خود درگیر بود. این ویژگی در داخل زمین برای او یک مزیت بود اما در خارج از زمین او را گرفتار مواد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/91595" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqgoU6GylIxWN587D5RqvgY2YwjSFYj1UhwdDG-lfyQr0W0DuNwlKop-YsZFWrvdqyviSEz-Sjjtiy8abx6N93Q7t3GufhmXtIoglvCab5ZYhrplfnHHAXkEvu5JPVJcHNwg6X1PQbc_VnGfhyPViP-AFix6yKf4_r6gCmxjqpzwouPDNq1C5K23nG06neElG8w0XIUQYOjwYl-1ONTBxZDCbpCv6tiSaHXn7RaSiQX1c2cdqF-9zl8PEv6R-UdCm9U-0h-qCOR8kgAkerigycdbgIBiz2YfKgzAXqV2dCBMHs_U3P5xVtNpPdjYHoaeJS47eWOFeqZIUrZ5O4_1Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇮🇸
ایسلند
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
ورزشگاه جردن-هیر
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
آرژانتین در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایسلند در
۱۰
دیدار اخیر خود،
دو
برد و
سه
تساوی کسب کرده و در
پنج
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر آرژانتین
۲
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایسلند
۳
.
۵
گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/Futball180TV/91594" target="_blank">📅 22:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxN4rUHtrkna6dO64o5FP4tBqsmt6ZhJEDZX_iIMq2W5EDPhmj4qyOfZGOvOwbDIQMJdxL36sbjXzCUBIXjXvmnXeP5Ajf-VRH6Nwaky4rEnoawpCLit598lKvxQfcVt2eyD5mwPaOqt9E7HWMHYdSqSnNQnbfrAVBVeHVr3aGNqb6d6cz_PIxia0WVmiA6SBgHM1wFyrdbStdJ6hT6Wq5dxu8AF_wTHU8lY6aofGN_5uBA0ZiJLDMkIXVtOHf4rEsKeWfWlTl68L3s8znHJYeDqjjO3-uyZktD9Yk2QIe2C2NHXrPXownmCQickzq4E-EDBdbkW-kUvGICFLrLF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شیا رائل ویتست، بازیکن آمریکایی تیم بسکتبال بانوان استقلال، با یه فرد ایرانی ازدواج کرد!!
چرا اونا میان اینور ازدواج میکنن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91593" target="_blank">📅 21:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxJwFLu6PWpLDDQ1lciEOLFapHQLOf63FDLVF7uLk-dyo1JkzF_AJRYPc7z7oQZ6cXajmts_HOlgY4N9Quf1SihFUlYJ0PCnTWrovFU7SN_9M8mT1YzAcfI-fSY772xxsnSU05Y_AAolO-jnBQe0op8bylxkwhgOWQnuhvvNxDXTtJKcFIjS-miyUScU2Zk7Gtxl_bzYdblw8RL231ArOtkwJsZfR6de6rLV9tuHE6KWK8F-MZ3-Ziw-aqjKn0sI_gRKIMvIaeIx4Gc-5PMXF8Hxynjc4lXiqdpgXUZ1pr2MvIJ69W187t3DWWA3vSim07CK4dm55R265etW9wLu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشرف حکیمی: به مردان میگم دوستانتان و همسرانتان ممکن است به شما خیانت کنند، اما عشق مادر بالاتر از همه چیز است
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/91592" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0l4Xv2pLhNwLRyJtWCnmT_3pZNe0t_Q6wy89U5pMUELEMfWPM_GSu_JYtws6kPhL4sOMFoblPkqKATVrqjSJVWSs_tHBwdbv9-7ownf8dgxDziClAj5C8YbzsfzAPfFCg-Ry4d6AeJSXbXQhygB4PX1O2_Yn6UDo4dlh4sU2TMvapUlTs4XkoIV5Inb8qLs5kPC3ZmYrI9iojBWPzJx0bFveuhVsQ51Hn1LPFkWC7NOt2z88XeAbsoB_XKx8CTaFquJ8EYW-nqs1PrHQGg97zFOfItwubLIQ9lfR33EfQ8LvOVUgWoOOiUNoNdeAK3D7jT-eulJsqH1AQFGPZ154Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تیم ملی ایران در جام جهانی 1978، آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91591" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFjYCKYCa3GBL_1o0d_JyitawBDB2uGBluXckUzNb9xP1lKdFDfxpHAXcFRQ6f_zQROefVBWWp27VXmL2Zw9qy6fQgTbz5158vbf-3_I79r76aAxFCBMeJkvnyykM3p__WkbsAjnG78yS-v9qtcQB5nvvIBQIwuiQCCyIAtiS8pnguUTSpnB1W4k_9kwhEJ2TfU1Vk4uGOU15zxV_ht8jBQtwhX-p6CuLFAFiBJQBcXxnojrQHRScryStRpa5qVQ-Y2nQ6Td157PbCdg35lWUt50TCA2bS0A_DQUUUDcDzILoVaDBVoXPFPjnjfHkvxNcDARBuX86mgahzJAup1SOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمان ⁧ جام جهانی⁩ ۲۰۲۶ کیه؟
‏اگر جواب رو می‌دونید، وقتشه که در لیگ پیش‌بینی جام جهانی «همراه من» ثبتش کنید!
‏پیش‌بینی‌ها از امروز، ۱۹ خرداد شروع می‌شه. رقابتی که فقط به شانس نیست، به تحلیل و شناخت فوتبال هم بستگی داره
‏اولین پیش‌بینی شما چیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/91590" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICCP7iw8v2PHp-1ZjYAA_ej8OPL2Q0_86H2tHKixzHhbOUOjNpWE9N7jWOOPQhmJFjVhwi6gBR2-jAwuLWZMXJ7NJC8RvJh2oEAmR-7zkLPT2YXcEvMW4R7EQ8ovVly7EDePiLaE5d-iAEJbTjRDg6s5WFLjzt2uIp1U7HqxlrPsTT1_iYWu8PRmS_SQmYNaBGl9NPGOtJKBtCk_wC-03M20UR4BfdKwALoEW9wave7CJweLMYCI0PY-cmwG-OhNMdOuwlo76ABTZI57EMSO1Df8s1xzpjMx-tJBlqL-SMszeueADrjMrDQVgJUOasuVrX_q8642I2glVmOcfEEr8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
اسکای آلمان:
بایرن مونیخ در صورت داشتن پیشنهاد 200 میلیون یورویی با فروش مایکل اولیسه موافقت خواهد کرد
!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91589" target="_blank">📅 21:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91588">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYQMxBzbQhchUlubgl7TyeZGHpHgs1t-O5pcDVEIuzbJ1uP0ti6iQvX2HprcTztTNaarvkq836rfRhASB0TS-ZMViKUBtYs8y-16uRj15bKHeSIAZwCXYwX9Q4zgD82v19a0khzgZ1WdoGaVi5lI4iOL86FxM7ubEwCDs6nTNyTEOHOlRbEBTTwNeg2ZUPH_6TYqsg4TD4XbxmmUsVOWEhT_1C89l3Kj1J2fHdxoVTu2Ql9f2E0cFD_o1a6BHn7VYkWAarJVZjmRffdbR0fWphTAHf9bSBqoC2vwBlbl_PMdqkWd6t_JBSN4OVDKpHBqHHnzbHi4pP7EwRymt-l4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇱
تیمبر به دلیل مصدومیت از لیست تیم ملی هلند برای حضور در جام جهانی خط خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91588" target="_blank">📅 21:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91587">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🏅
تاجرنیا و جویباری بزودی برای کسری طاهری و محمد جواد حسین نژاد اقدام میکنند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/91587" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91586">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQAzSAoqKyxJYwKwrhR_D9jDEH8reY1z7mlRsw7b5fYyjn3HcVsMHJAn2xKVoyNmNIea2mLyF4z7a7fC6OXMd6Qv650G1IaLHbUmL3ZzrvqneK8wgCPZwJH_D6SX9PIM9CO4tVjjPR-4LZXdreg9NVZyilas-w8vmWKHOpg4PvGikJLcjxGL5p4542PjAwT5gHgg8gWRno7PW6xAthVa8PRpt_ZKY-5zmZYiELUFJ4SeocRYqaSXBsWCQBjKYaYTNC1zE-y0TJFqsAI43EHRTt-ivo4EW-_4K_Gh9nIlXqSDcjzhi5Q6XgiE9iKHXEPL-vw_dIpX8_rqcZY9lrqX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب ازبکستان مقابل هلند با حضور فیکس آشورماتوف و اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/91586" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91585">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2mM-Y22TbCMpG_sWrKYdoE_8nB9dRAWSthMPg6u-PRtjoQWfedUzgSOVx2VK3uq0uthCIph2XAR479O60g0oa1tv9Q7vGvvGpW8YsRuvLgH-Lc-j9e3o8QjMmBX-EXF8j7lag0anpB4_6GuWKlHVPgYap7csRwop_M7NXw9oUyG1gf6emOYSGPtuP7c_1pn-RlutcB_XU_Slr5tC7-XGIrJhdFqpEPxmbc4E3xVcuEomosFS6c-7OVxWn0YjUHvI04eugUa9asVgsug5RBuVIOfkdUatNpAnqwwp_CVUgx7niVMB7TmJIeBK_imb62CucfGihLwe4EDSndA-ShIzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
کارلو آنچلوتی انتظار داره نیمار این هفته به تمرینات گروهی برزیل اضافه بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/91585" target="_blank">📅 21:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91584">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlnJrrhLIgfDAE3vxRxn_iPBa2SY0QC0KpQmV7llyLo92AHEIPQ58QcBlBocNraCfWu_BdYeviBDNG590LTpOmfaHh05R8se1glRT8sdDZWUlRePMW1f6Z_wRohIA1RwPKVjFMrHoE-nre4HRfYehU2vrXxS7HUQ8vscqnINQsFEE_JqpovDW63eplHYR12C6UOTxVQdY-eCxq53sgqhyf2YOcFuBir7-0yMP1RHLKHrCEC-02HCDVHacuAqgrP8MDB5L4gJ_bKVrBbTmw1IAj0Zg-9e708wouT-5K8e68GtKFFQiVCdEnTYO3sscYZ-Hqj58nIw6VEM-iCkEq6yJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنایی که بیشترین دقایق بازی رو در جام جهانی داشتن؛
لیونل مسی قلب‌ها در صدر
🫶
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91584" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91583">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jos7uu4iLiL1ZCVPpb0w5OhzM23JG8NvrYMhOIlRU5UB6Zdua7V67Y-KZD9Gtfs_PnQs1zopE7EAayL9qANBmpDIwPbOU3ZGvVmAAVWT9j7sb6VedzU9pAIcRT_SqIX-1uAMVybdlNhX9XUf0ErgYTR-kUqt0NURDuILlMl7cVZA9vAcocgsnXKJbmP9bIWTzSGtM27GCasWRzns_lMwnDPqZT7p8EEU_XNy6LPspipjTLWe539LDSY52g8NuJk3xZriHSvAorJb9sdxIjXw4ENOU9z0dh_IQ9NCfOl0rLv3Pu7B2ogDAlhFqOVFX6ko5RSkUHkoqdImdFvN9TaarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر سپهر حیدری هم پرقدرت فعالیتشو شروع کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/91583" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91581">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXsO1rG4LM5H7WnvNJ6LQPHzy-tmMp3eQpzg6loO4asvSn5F0BBXfFraI4jnxOJBeA7Ls6AAI4kdkczjeKc7sDUGafwdLbtjtRVtxvtGBNcQTsSQnacnYtyn-1ivInmVV8609SYpHmONiRB5cohaoeUlDoQpQ6noxLwA7hPP4dBiYk-Bl_UY4LYv12xM6tdNmuCXs0JWB5a418AsKLVL9XpYEFjRqnlwLiojfflXzdSZe9jcLBFRSPkSFlFemE9gnDcLLVZIGnRosmjF7-Xjyx2Rwg5n1ovUF-7QZRmhnWFjgZFIfyFWnx8ACDjqsXuKYMc40g8hOe39H6GdU-q_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpsV37sbgyS7WkTqFSV_aTAfNZL1kqjHm-2msQB9NAMiO2rB0teGXwPXthvhUoz0zPYS8dv5kkzGHKETtFhnyaPPOtVHwSAKcui41JmG2jiq5gHd3D7wE9fzBZ8Y5PRooez7kbvw8LGLudTTzfnnPHBq67aQDRRMq_X81j2z7rZlnq6ipy7REuv__SHArBtsMyvkl78uK4er0WhfBX2m8XGBArb4l9GBQFJ6_ro6K5r2NFzmLeotBrM0i4RIR8ZS6k13W1UtUOHH8tPv7f-hRC0YUkum2G7WFMGjvh0mXpkxM3vZ7jrHf0gAxDXgtjET3JCf_RpeVIwS6xO9FycTEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه. واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91581" target="_blank">📅 19:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91580">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cO_GwGAaZtPbkQ_WUY5WKyOMjkWDfnxLnocuVVrn1hEbYoEcwR6e76eVitvU8aNYUxfRSBHXsPK5TRrOlg6aQ_Pp_SlAW16AAU5r3rHjKTwqZ6tQzZlVss1ArL6hxEMieyW9_JupzclNlZWyKENwb-OQWuOREArjvathyPqVkOfHTKGeDCfSTDjrVeVU_9kjmwBoEaJEGVSFvm6sBFemdyJsghKMRgNg1COToC5jvw7i2SK9edICAJz_C4P6oEJw6CMssmcrH9psxd1FzlwHQGBOMRznpFdF-i78bwYp10jDEzbstZesyYMLRZ9GqRdf2pVB98rYh9XoZf7eo9T80g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab5cab715c.mp4?token=cO_GwGAaZtPbkQ_WUY5WKyOMjkWDfnxLnocuVVrn1hEbYoEcwR6e76eVitvU8aNYUxfRSBHXsPK5TRrOlg6aQ_Pp_SlAW16AAU5r3rHjKTwqZ6tQzZlVss1ArL6hxEMieyW9_JupzclNlZWyKENwb-OQWuOREArjvathyPqVkOfHTKGeDCfSTDjrVeVU_9kjmwBoEaJEGVSFvm6sBFemdyJsghKMRgNg1COToC5jvw7i2SK9edICAJz_C4P6oEJw6CMssmcrH9psxd1FzlwHQGBOMRznpFdF-i78bwYp10jDEzbstZesyYMLRZ9GqRdf2pVB98rYh9XoZf7eo9T80g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد مقامات آمریکایی با بازیکنان تیم ملی سنگال
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/91580" target="_blank">📅 19:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91579">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjwDKJUF0tvvR3R1Vb8cYTzTtldQyvfNYqVzx6bk6wF42O0rEzOY7rHfhXIk_HAfrqjXHf9OLjC8eiUUN1njqvnas169B8CAbZfOBjstKCDXme11r_D8uagq_gI2vpEBdcIEjl1QgmwiX4lWAnQpkekF6sHg7qdDZWAGlESJbjdMX5avFXRzGYmK0-lLDLCPMXVkTYSpFMx_hoMxgZL5St8sasRzRTiDrp4FIEGhNqB_y6NGvJKo6ms3Xzi49ZkAra3VEWTzRSn0FQkwEIrsGpCA8AyYzii_BxO4ZoH0YoHKJT2Oy31nJr9W8w6HAtay9RiENxJ1DQYgLFNIj18wlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
کادنا سر:
رئال مادرید پرقدرت وارد رقابت برای جذب برناردو سیلوا شد. مورینیو این بازیکن رو میخواد و اکنون این احتمال واقعی شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91579" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CGEcqCqxGB4ekNg0ICYXXntf2EScRInG-IyVMYrjhs-FIacaHGdER8Oisnsa337orcllwIYpBWNukZj9Mclt-Aj8OCOLI8ClENW74pX_ceqoyhzEtA2KxygqGpyhhP3SNZtscJ-AoN45hCEsDOpKkYI7aCaLspnQ3Fgg5LLsJCFPYA7fyL-nJVLMrJ3T8StqaY4oL6TvamXPcYMM52lCf9jXk8wY92tTr10efCL-ovAaf2NvBAze7UuP0eJ6OABV2nP61Zv8EroV2OZMsLWlWz3DuLTBbxysNzSWz5nTtUBeMgXwoKEZVbLI6EGuWO_1vJAH6LSJmTZClvjifsficQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYvDDgtU0yS5S1vw7p56w3t-UP-4O0sd3nPD-QHtH605DpTC9vsKSy05pTroaB9iYW-jSRyzniaN8lDDoKcohUQmk4A1sHPIxRTuIkkwXeFDHn1Pd4x2ynkuERHQzn_YXl8zqXZtfB4ALxveZQazbHL8D52r7ccpJ13ENRwAO-OX3JGXdiPQky_IcVSkKEiID08vPIVOPrner9HQq6RBT63fu14nfGxm5J95tpajGZtALXT1hzOumPg9IjuhPdrldBfz9bB5SGrD9BI3peRHTua9hXQJpCM_2oevSZhwebqMrqqmyaFRwE47JaLCRlQUH400P45kUoA2u86M7LFk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XXQJL7ObyAVoRJNIoi_wkvROh6cZY_f11TJSL2NIYvO9haWXXsuoyvi2ctmZzSa8YmvY_ebxSKiSo0sl0Hu-aIGTd6gBAX0WLJXsF354cGp14cfHxQuDxBeLZX-VTinD-ujxtmrMgzrAjzL3I7PMPxAbxa4iUO-IMBIVoBh3U9Ywn4CRVAPj4dWE0ZXhb_8F9vXxq1loZ1Lp2XLE25wwn9QXEaLvo43tF7okyHT12XQOTEMGlZNDRNH1PMHQdjciKvFSEBS6G7g0J2F5tB13UF8AfKeaFHeASahPYPuMRoryMPPlRoGXW7-8o9p_miyNshaTAqcE-lcSataBkuLlfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله دلیتای عزیز هم که معرف حضورتون هست تو جام جهانی مجری خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91576" target="_blank">📅 19:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=BnFS13c4xBKmxxav-4UqU2eJY-_K5Wh7maCr8VASIwB7dk45wSlTjl8scEIVhRUhwOB3MJyqwBr-1MHqkWbaPSzx-eK4gxqCv4lL3-5pkVnkZwWlBQsAlDOMv-5TJL6MpoX2DufZEgSXN2OrGW0QxzeLo1XTCR6AFGjAI9cNGsu1AmmaY4MLQ00DvuvLEOE9EeMWO4OzOBh78_fqWjzwGE8mBwVQSTAd4MjsDDJMRkb7JCaeBlwDQlmMTrEg2nSl9BAwJg7UkOg7-XPje1FxYH4_pwu1IQHQ7u8P5AfbY3x4lEF2BeMnn4FQ5Fb9YZm-bO0Dm4QHmCL0iCO8nJNVw1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe52300bf.mp4?token=BnFS13c4xBKmxxav-4UqU2eJY-_K5Wh7maCr8VASIwB7dk45wSlTjl8scEIVhRUhwOB3MJyqwBr-1MHqkWbaPSzx-eK4gxqCv4lL3-5pkVnkZwWlBQsAlDOMv-5TJL6MpoX2DufZEgSXN2OrGW0QxzeLo1XTCR6AFGjAI9cNGsu1AmmaY4MLQ00DvuvLEOE9EeMWO4OzOBh78_fqWjzwGE8mBwVQSTAd4MjsDDJMRkb7JCaeBlwDQlmMTrEg2nSl9BAwJg7UkOg7-XPje1FxYH4_pwu1IQHQ7u8P5AfbY3x4lEF2BeMnn4FQ5Fb9YZm-bO0Dm4QHmCL0iCO8nJNVw1mpsUibvSrK-BWG9R3-ylm58YjKNIfhrOpqJOjlCadeO50V3KfZc6RsqZgCCpoAxdGf-2eAXw4-CV9ZWB3F1EdsUadulI4PkUOVB8s1z5PqBAmaISjNnChJ3hgpLXH8y_fEW9l8FKx5R2tO1lEkS_X2AcOJOmaLnUIuW-vfQXcZV3nw9sbjEn0ba1gv__obAU-ktFQpTNIa8GbfdZo11cCq-fJLZhDDp5nb6p4d7dIeJvbBGnmkxecbx5HTxpFyJoi6eBtdfTkTwd45onV_6I9u796YTJLA1i76f1p1_hUPnMBsme8rziUhi1WIzCucc7HBoVL1OxV2-ZIr86ie4DU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیمار؛
بزرگترین «چی میشد اگه..» در دنیای فوتبال..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91575" target="_blank">📅 19:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=tcKqaODvz4buBT-4BppsuK0j_0BMpEuWhZht68NW6h7D07Nv0jAtUnPow5XWv0EbmrWJttglgdVbD6bQ6rs0irSeqOfEuc-7KmwnBtPyWilqJ5m9NUkG5Q8vEEfrlvGZwBPxQZ8Vm7wlMIZWtW2okCdB4Slrtd2Bh167TBt1pS7V_zEIyzg4NwWjsTPEdSoEE6Y1Bpa-fD_2u0vUCQ73qzuHyitXiRzRE59fKaOaRtZlBPbMALgUzp8gN8L5Pmy3KWgAcgzjwoeBH-Gn3UwNipGppjC24llCZDu512wHk3OW46aunmMl0DhxhxdfOuj6_RRM2l7l3sDI78JnQcb_Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bde175f21b.mp4?token=tcKqaODvz4buBT-4BppsuK0j_0BMpEuWhZht68NW6h7D07Nv0jAtUnPow5XWv0EbmrWJttglgdVbD6bQ6rs0irSeqOfEuc-7KmwnBtPyWilqJ5m9NUkG5Q8vEEfrlvGZwBPxQZ8Vm7wlMIZWtW2okCdB4Slrtd2Bh167TBt1pS7V_zEIyzg4NwWjsTPEdSoEE6Y1Bpa-fD_2u0vUCQ73qzuHyitXiRzRE59fKaOaRtZlBPbMALgUzp8gN8L5Pmy3KWgAcgzjwoeBH-Gn3UwNipGppjC24llCZDu512wHk3OW46aunmMl0DhxhxdfOuj6_RRM2l7l3sDI78JnQcb_Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91574" target="_blank">📅 19:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91572">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nm5u5jaT89TAulFV2_ce3pCIEDUXmE-TLZ47LwxLY85g81EE1cBTwAPap3pf7hx_FxCIl3QYJwobwHtophZXMwAQ4GINmZgUQsXt9thxcWUIkj5Rxy6ReWRkrz5kv6DtdNiBP_VHCL7d4rb1kyNqx5U7iKRZos_FwHl3OhkzI5kgmgO6Mvl-drIM_bLYbfSNXuJPfOhYoBlicnTz_IqMnyKaOHsN9qC-xPyL6Aq7YXY0HPIVDBisPkfCUBsyf3kztRUvx1TI_AKF_jWksTSePE7W50hAMmAlzN0NftFfex7wtiVIgoWo8dtq5Ev7NGgalYJxtKPRaAN0H5Ea966HiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kBGz5zG4cirmzdko-GyhA2z-QUwjjzalDyt2Z6xpPobtrPCcYXrKDhhGa_dVN17DGpX1kDk0RJyNjgd8upbcIXADLY9ywdXPI-A2ip8ZOQGNYAJaJ2HiGWjF8xqUUUw8dScqZYSZAFKqVNiyfjSQwlVJHrbpWuB8BRxSWcbjNN6nD79yDQYrK5aGr_gMu5zKuklFEOr7212m5hL15KZS5xbnUolThiFyW9y0qmmCM5MSN0_h0AwzvhMVu4ipwQznFSX3Hh6JANPxg3bddHdEKnqfN-YxuZyFJYREGvJqlKYjtd2XDWk6e7SUbaWKHOsTliU0vaVEikyIQNSaoUfibw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اوریگی عشق بارساییا از دنیای فوتبال خدافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91572" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91571">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPGZrYWob8Ozgyf8_Z2nY3nbEtw1BbBXWTHT_X16K0NbctXFH09E2IAHL62y0nQV_yt6ltuKBzemIvavj7B1x_J_c0_6l0YLiapCy7NgLuyDoPBE4AOBa81G_5BEZzedFP1YyPZXao6yrEv5c4-tvAmmAQKAd1sMZonKAjxBhsl2qHek0yu1M3dPJMQshFPApA15gKHYOu9j0aJ0JeemldkL2g4xEUO2I00QY8P5QRtqaqLbhVvneLL4yaTQj857RuZWY87uEA1SIGkngZxYjVpdSZlXSyT59FArMrf8hjZ-WngI6RXb9fOm70eDryc_M9cug0RQeoIN8BcOlkOTGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کروس : بهترین بازیکنی که در دوران حرفه‌ایم باهاش بازی کردم بدون شک کریستیانو رونالدوی افسانه‌ای بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91571" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91570">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tX2XTYJwQo-bCVY_fYT9DWaPJpJKjBpGA0JRyN92lUqklhu2V6u-_U6LASy4xAQ_G0jSlzNgHkJ-8HilImczNKJ991BwYg9BnYcwSuB6jD0w0KQJT3BBRsyobFftp_BjiCyhuBxlG-gGr7EMRsENeWZftIKrxrtfernk4tLAdNY8YMUdsFPaBbZNXTFg10P-q--jiFYKIbvS7NCotAT_umMpzP_16y3l_OYQmJUoxCvjsMlTio4uZzsLY7KmLYOm-i96vfV3c43jJapbNkEIkpFgRfSdVGdwWgjwoPe4NrKnaGSvrjWx6ZBoyU1_A0-dMFBDDz5xLYJ8Tt8VfdigOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
دیلی میل: چلسی ۱۳۹ میلیون یورو برای انزو فرناندز میخواد
🔵
مسئولان چلسی
میدونن که رئال مادرید به این بازیکن علاقه‌مند است.
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91570" target="_blank">📅 18:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91568">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=mlEtnGSB-UosBdDcNQhNr-WqIjpmuzLyAhFY-ufZjgM-QCQiaydv6wawWTj4-1qYzYzASSRYt66-FddO1T7mCgdUOJA7r3Uz8BoLbbqo7mRpYL7C1CgD_5prtx10NsWCS9aAN8ewzVY3kzPisnkKhbUIv8VP7nXeLnYhJHf3beUgPiKc0X9vFwCt82T90u-rRqcIcd5ls1CQdcoBK9DGnk35vsFpr7fIEYP25oYuI3fULh5CWksy_5yi03d2OuHmWn-6NPhx7M4PU3X2hCF1nSqJI-GGvgvtQlqfX07wv21nwZWRPpJOTnlKK7nMkBZRgwAfwT9d2ewBi6jVsLKqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0de371fc06.mp4?token=mlEtnGSB-UosBdDcNQhNr-WqIjpmuzLyAhFY-ufZjgM-QCQiaydv6wawWTj4-1qYzYzASSRYt66-FddO1T7mCgdUOJA7r3Uz8BoLbbqo7mRpYL7C1CgD_5prtx10NsWCS9aAN8ewzVY3kzPisnkKhbUIv8VP7nXeLnYhJHf3beUgPiKc0X9vFwCt82T90u-rRqcIcd5ls1CQdcoBK9DGnk35vsFpr7fIEYP25oYuI3fULh5CWksy_5yi03d2OuHmWn-6NPhx7M4PU3X2hCF1nSqJI-GGvgvtQlqfX07wv21nwZWRPpJOTnlKK7nMkBZRgwAfwT9d2ewBi6jVsLKqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
هیچوقت این‌صحنه تاریخی از لیگ‌رومانی فراموش نمیشه که وسط صحبت سرمربی یه توله شیر میارن رو گردن مربی و همه خایه‌چسپون میشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/91568" target="_blank">📅 18:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91567">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0LVv3mYnZM0pTV8eLFkpZJDdFu5MKVXpA4gNRs4TogdqAfoR7OaeBujKiuO0ud4CLprZwBEXGLCHqjA-bO8IHbp81JExn3acEIgrO_-cjyDSpv3Tk5HpbC3wxuqy2eATdVlYEDrLRrnADXKR2zTpL8C7X54iDnHR35UEKwytbk4NQ2-9HwegbUfSB-c5QZKPdhLUylIUSH-ZcTQ0uBKfClH3VvHy7Mkl9flen1CBKLo_clUDHcf7sQV0IyXmSsdtvc_Qf7HKvxtQnU-53wgZVBiqzbUKKNzrZXc2fM2SeYW9uepjQZ-MeHAsW6hnG3NUBImbBNQE8oIGfWIIReO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه قاب تر و تمیزی حاجی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91567" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91566">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=c7fUsPoiZciZmKFZSTeut9_S4SAPVHwiSmFV1am3EjauhHcUWgSCUzMjaucGQDoA2d-rlPWfVyYFGOuoXGOAUkaeTV3QStx7jXGEA48uhFwENHLmzemKUBbipPI9yqqR3Aglf1gxYLKXXRS5x_FiY42vpowiGcpdn8JidJM09m9TicKtq_k2O6xsWK49U181zPawo1yPwXah31OWeISK9e32boLJGDfqHHW5xRLQApdiFSf7TwL1u3WdjqLAhnvtgSzUeVkyRAb4PY63xtMx_LcL7Kd5OMaQEKY8csROr4zkC18lwc4l_euFT5mfjIegS3wSiNMeJA5N08IR1f3qcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585ec3a1b4.mp4?token=c7fUsPoiZciZmKFZSTeut9_S4SAPVHwiSmFV1am3EjauhHcUWgSCUzMjaucGQDoA2d-rlPWfVyYFGOuoXGOAUkaeTV3QStx7jXGEA48uhFwENHLmzemKUBbipPI9yqqR3Aglf1gxYLKXXRS5x_FiY42vpowiGcpdn8JidJM09m9TicKtq_k2O6xsWK49U181zPawo1yPwXah31OWeISK9e32boLJGDfqHHW5xRLQApdiFSf7TwL1u3WdjqLAhnvtgSzUeVkyRAb4PY63xtMx_LcL7Kd5OMaQEKY8csROr4zkC18lwc4l_euFT5mfjIegS3wSiNMeJA5N08IR1f3qcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
نیمار جونیور ورژن برزیل در کوپا آمریکا 2021
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91566" target="_blank">📅 18:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91565">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=izVeBWpXYMnyHwA4CQFprwOlOfnTbWArxIPZSc7NUX0b9yHIx4WHCLKtgXYGqnJCq3T_Evbah2cZjy3bHMV865qnfjnukfPpN-ZroOKVUJvZYyYWVouHhnGszBncW0yCdnit2OsV2QiRMZZBZ6C2bMBOJ0Za_m4WAtxoStlK8DHHm8vpVSdLdR0pzZcrI5qKmOmnvCoJH8du-uiYmnaq_g-idreVqGCsMdNQcj3Vp8xuo6ie1-Os0doBIbMCdjiHsepavD4p2hf48JPmVzMUpwK0Odcnq52u-0z6-vseX5elxzhHwAT8SZ_QjkiAyFMKHMXBAjrN8QbMpaVBBULfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a249a370c.mp4?token=izVeBWpXYMnyHwA4CQFprwOlOfnTbWArxIPZSc7NUX0b9yHIx4WHCLKtgXYGqnJCq3T_Evbah2cZjy3bHMV865qnfjnukfPpN-ZroOKVUJvZYyYWVouHhnGszBncW0yCdnit2OsV2QiRMZZBZ6C2bMBOJ0Za_m4WAtxoStlK8DHHm8vpVSdLdR0pzZcrI5qKmOmnvCoJH8du-uiYmnaq_g-idreVqGCsMdNQcj3Vp8xuo6ie1-Os0doBIbMCdjiHsepavD4p2hf48JPmVzMUpwK0Odcnq52u-0z6-vseX5elxzhHwAT8SZ_QjkiAyFMKHMXBAjrN8QbMpaVBBULfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
۱۶ سال از این ویدیو سمی بازیکنان تیم فوتبال منچستریونایتد گذشت
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91565" target="_blank">📅 17:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91564">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqSgk5BkKMn3ORdt2Ry_UIrFbFdcdgQzzwwkrx4qZCmdBg12sigw_CxLvcSkhyzvEuqHqmVFbgxyFCPTYcjETTV8kL47MZfx0eI1YhryjFBelaXxOHaOQipWIPdlzS2WLcO3u8iZui43ZgAM7PicEFAMttJy-CB5lAl7kKzFCzP33HGQ-JwHZ8Rxh3V6KBs4hbJNQsd9JYwcjsolq-p-oPegk_l-zCjpQB6UB5PD-pODqBQB0WJCjnzuCMu5NAC2RQFQmtIQTvAhV_dWyvr2zaMQjtl4oiLOTBdzrbcpINX15lmQbNcAOKOw-Fql6WC8CfVA0agCQFcZvAGWck8iIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
متئو مورتو:
روبرتو مانچینی در آستانه کامبک به نیمکت تیم ملی ایتالیا قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91564" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91563">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=i2B9_borYsJapdKkGWGjGpD-ERrK7VLOSjnWIi8swUjt8jV-kGYOGWDDl1fcTs3cq81z74XGMSLJw8LNgHLn6S-vOARttEl7js6UD1bG-Kwvqdd1CxFusxzSna_kobNnf0NB-o8YNC3uD099b4Xr9gJvqua4MlS4fmVFmu1BlI_hJHPoDcN7qORQmON7HDceTgYMVoLzGNcycbcZSLTRBLtwax_2wubzhzl9o5ZuBYfWmOmwAbVJ4cjvaO6I0bfS-pnC394SD_ofItlRyPFSlMM6WXGXJtrxdrV87YIJmepud-MDebP_xiLECrVk8r3sHI_3ValT_4CidYz5asKUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d3e3015.mp4?token=i2B9_borYsJapdKkGWGjGpD-ERrK7VLOSjnWIi8swUjt8jV-kGYOGWDDl1fcTs3cq81z74XGMSLJw8LNgHLn6S-vOARttEl7js6UD1bG-Kwvqdd1CxFusxzSna_kobNnf0NB-o8YNC3uD099b4Xr9gJvqua4MlS4fmVFmu1BlI_hJHPoDcN7qORQmON7HDceTgYMVoLzGNcycbcZSLTRBLtwax_2wubzhzl9o5ZuBYfWmOmwAbVJ4cjvaO6I0bfS-pnC394SD_ofItlRyPFSlMM6WXGXJtrxdrV87YIJmepud-MDebP_xiLECrVk8r3sHI_3ValT_4CidYz5asKUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اتحاد و همدلی بازیکنان اوکراین و دانمارک در صحنه بازی دیشب و سکته اریکسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/91563" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91562">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyfLrxQ1ZvSYO59UfPFBS--NhfwGN0u7Lw8G2aBQWY2HcQfKe8plpjtbWL7X6GJbjU5ZW-VmIMm8d_iVLTLI8BVWnyHJ4uhGtY5YAIeiiEfO9woffJJEPPkkXy3qSQbDQVxG-73-IZMk6jsrenNcbN1KdEs0-YMGZMEA8hi7i7Gy0bpIpEykyqLAAxAM0oBg1Yci0CSOeZRgAAkYEa6mAPLtplH9BN9Z252gxZvnddkzRmx2iAIpsb1oBCABH_MdK9FeAWK3kysj-4RZzopU21uxvrUNf0SdQ40TQvTvZHjcHNTV5JF8_0nv3HvMFQU9FXAOkUBPvcAHwYWprUDnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وام ۱۰۰ میلیونی، از اینجا ارزون‌تر درمیاد!
😎
💸
وام بانکی از اسنپ‌پی
با ۲۰% تخفیف
خرید اشتراک
📱
💙
✅
تا ۲۴ماه
مهلت پرداخت اقساط
✅
بدون ضامن!
ارزون‌تر از همه‌جا، آنلاین وام بگیر
👇
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh
https://l.snpy.ir/aqijh</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91562" target="_blank">📅 17:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91561">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=Glte11rWyRvJtouvAze1_J8HBroaI-nrfLixFHsUtTVtlGwkwnLlQeiESV2jErbatjB-YSi_EhvSAq5FVnvm6rDxuqvEUMGVJJ6qr1PEkdDLrs4HiWw82VdZAnlNIcm0Bc67KMhG1Tn0wOaSzrgAUShc2EUr0jtl5GvYJ_hcKKaqAvoE9tLQvihdx3ckowAH1VHVkE8tmQh3xa_YgOR2TC5h8KtBzh9KrvjJRHoRHra3lw0CpgWVH1TTYZSkLRmGib9X9yEpAmQkGMtuqX_kcCZwQDzsb1HKQ9_0S3sB8ixPtaMCPzgCStqwPsnuaMIgTa_A1EpDi7LDSjb7kbhGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7cfe2ee7b.mp4?token=Glte11rWyRvJtouvAze1_J8HBroaI-nrfLixFHsUtTVtlGwkwnLlQeiESV2jErbatjB-YSi_EhvSAq5FVnvm6rDxuqvEUMGVJJ6qr1PEkdDLrs4HiWw82VdZAnlNIcm0Bc67KMhG1Tn0wOaSzrgAUShc2EUr0jtl5GvYJ_hcKKaqAvoE9tLQvihdx3ckowAH1VHVkE8tmQh3xa_YgOR2TC5h8KtBzh9KrvjJRHoRHra3lw0CpgWVH1TTYZSkLRmGib9X9yEpAmQkGMtuqX_kcCZwQDzsb1HKQ9_0S3sB8ixPtaMCPzgCStqwPsnuaMIgTa_A1EpDi7LDSjb7kbhGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ناصر الخلیفی در شبکه الکاس قطر : لوئیس انریکه به مدت ۸ ماه پیاپی از مرکز تمرینات باشگاه خارج نشد او هر روز از ساعت ۸ صبح تا ۹ شب کار می‌کرد؛ تا جایی که نگران شده بودیم مبادا از شدت فشار کار دچار مشکل روحی شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91561" target="_blank">📅 17:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91559">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ta6TjXPn62W46M_Tt7waOcdhWD1zwPgWhLv8L6007O5PWoZhur9mqrZ4X46xDWNrc29nJqAMXqQ3_WFTmJnrySvE_JoIdw3QnwHSCw_ULWXFKimfx9iJSHdJmScnsJ-DoGdtXQXcrrp2gSVGzOerxjbXvNahmxcnXjmFWDhvtZNvzu3mw3u-nnLpKkw1AOdJyT4wPVFXRBKxrWv41r0uXHkFNdIFaVe_cP4IbZ-g2IWEABWudEPdEgIZHsNL7HlVSqbUHdWUvXWKdZX46CPhqN6mkDCWOPrDnVeWREVD-p-k5V5aFvmghWCHabMYy64X0ESiHI_ljzSf4hJfkO3oRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/byToLpbzL7Z-kG7I1nU99FcW0-s4y8zwW3h_UXx2KkxXj6TCOZihLwoeWJtCpXg_a3zSXuM0LNF33hM9NH2o2P-iYmuhSiNNsgs42JhcU3dZSreWMmGUIc9KKsuy9CWEReMmJw_h0LKPViK-F-emunhWN9GkZnMVj71hHEtj4RzsU_Oznvc0YF2Lboj2mXP4y7XphlpO2WMv-nmpV6VYIarjHdMou71adIREv7PGPBC72nJrWeWgifXi59iRkXd3RgSgkV_Cwllvd0UU17F1rTye9Hk_FQdUwSZwh5hn62rIXvwn8lq-YMBUhoSNJeSYZsfVpJ97G7WU0WVk2QqzKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاله وندا بهتون سلام میرسونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91559" target="_blank">📅 17:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91558">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-y41K04oTsbz4VYTFGdHBLWzi1tjByOfZCVhTZLNL4X3OO11XZdHKaBRUf7TsN_s791YKTw1-LUE22oEt-bKNoUqxvnUD6xGM2vXVF6xrAZOQ4_mzvVp1B-dRGtQo72tMJ97-5IMdYRQjW0klU09oOEHEyQqvUMbx35wurja_AgD9aSCF5zCAsc2QwwlpywfK8kDKeABP4-p4ZDM-PdxAHucBwDfy7txT5pEQqC_1NGWNoGoXaoujjD5AHsDwL-sMhwdjXQgtwh4_-X8tBzJ0GUGKgcR5dCyJUuiV-nAs0NJwBRHCliXBHOD1gxefPrIrYIYeqDpAJ5C-f9GIBf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91558" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91557">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2681453adb.mp4?token=SvgcceANYxFa8blukNu0X9-mvnPt9Gbyj1lrTYOK06JC9kIUoEYiEtz5UKICE-H0CCHZvPNazBmfECAssR7_IeebcSPEY2HV9j2PJ0YhiSYfj3CQyTZnJ-ldLhacjSSLd9HJuVdP3r31SE3Ll2FCnfYxU30990GitetRoN9W1oGxofimyoX2-TbzgbByn83Qt_IqNnomE3yWTWcdpV5PJ-yYQq0oQGD5XhA4xkRWyPTxGC_fK2v8d2F4RnK3NbE-BiVVoOaIBO_k3JboTA7jFoLQ9EZmEdjSM66G8-Zrm8uBPAWuM46xSSQrIs21MW8i14M9C3aA4FGrnieiMnZEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2681453adb.mp4?token=SvgcceANYxFa8blukNu0X9-mvnPt9Gbyj1lrTYOK06JC9kIUoEYiEtz5UKICE-H0CCHZvPNazBmfECAssR7_IeebcSPEY2HV9j2PJ0YhiSYfj3CQyTZnJ-ldLhacjSSLd9HJuVdP3r31SE3Ll2FCnfYxU30990GitetRoN9W1oGxofimyoX2-TbzgbByn83Qt_IqNnomE3yWTWcdpV5PJ-yYQq0oQGD5XhA4xkRWyPTxGC_fK2v8d2F4RnK3NbE-BiVVoOaIBO_k3JboTA7jFoLQ9EZmEdjSM66G8-Zrm8uBPAWuM46xSSQrIs21MW8i14M9C3aA4FGrnieiMnZEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🧑‍🎨
اثر هنری جدید حمید سحری: تاریخ دوباره برای اسپانیا تکرار میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/91557" target="_blank">📅 16:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91556">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5-KbuhgAjumcPTYxV4jvorEwGzxHma5UKCg6g2aoMrQ5kcjqHtlQUvIohRkVUg_R5SVAxMq0niBYNENTN_2g3WMnUsaANjgtHyLEZEh3k8Kf0ykBwCxwSJNs0W0e-FcZSUOkbb3M7dEArWxqEjzGoV0wXgpD0GKXEM1HB5H82J3vj7dnl2I-feFUXQZIURJO9i5dA0wMXyEUECKjd1-dU_hRxNhrRCH6JdWob1g05RtIQRhA4ScICpR07uuMapoTe2LH22ES0ZWMNK8iPnOwVnrlx86AAGg-AJzIPEivWCZCpmuT4uE3pC5HvYpzOIfZ33zidVaNcMpZKJc0XGJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
زین‌الدین زیدان:
🔸
قبلاً بازیکنان آزاد شماره ده بازیکنان باهوشی بودند که بازی را به شکل دیگری درک می‌کردند. حالا همه چیز فیزیکی‌تر، منظم‌تر و کنترل‌شده‌تر شده است اما فوتبال بدون شماره ده شعر و شاعری‌اش را از دست می‌دهد. فوتبال بیش از حد فیزیکی و تاکتیکی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91556" target="_blank">📅 16:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91555">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
اسرائیل دقایقی پیش جنوب لبنان رو زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91555" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91554">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.  امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91554" target="_blank">📅 15:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91553">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrQzBDk8xzlkvL2ljA00sVKvbY9qUdnt-e7Yn44DLVtbiRFYGgkAQUvVGyWhZ3PVQ9zveP6DZx-uTaioYwhjjJeST0CYoMPpWEDKXrNeiMhzXHOzJ__c5W29Ef5ImQjr0h7fjoxizGb-iofMxKjZcB_e7RuHgzW870GMcFYmrX1F_PBFSzEEvr7UpAHuCh4GyBrCp8fDlAeURa3bVtviOPgvLTuYl4Wno6vlEqb5H6GGaL6cvcHjzbQNqtl6PWNdvc--l46qEQy5NUseUrRgXz-OkmTfbpyJ0Maj5YVpQpNuz8TMqmzxVupSnt8faCflNQm1JQ2ogw6IGzALDSRSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/91553" target="_blank">📅 15:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91552">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQ1qWMjPIOuks-B_I-VGBj7TVKKRxe9YIAKhfVJ4u0p4yxb0GDu5NL6_QKJxXPcKsqmi9kXQb4jZHV59Ye-YqdS5Di2v_zUly973iW6p4NR57p-ViaXVnwoJT1evkyjkakL5eQmvKNnV_fYqM3RTopKl8b8kzEfQvMN4JJxAJ-xzGENnLT5qyFX8z3vA7S_TkCZttY7HpfbCAunBHI5g6tZfA3fxvvJEuRCJ0FPnYdvWYimDGUpEK_mQKnq2Zq0hHFLWGqFAG3di7H6SMy_JYZPIsZ1U0YPKRbjm6JB8i1GLCUQlJUOptMuuQqyDuzlW6ul-76U6MCRf-Qgd3E_caA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
اونورم سانتی آیونا گفته که رئال مادرید به شدت روی مک آلیستر هافبک لیورپول کراش زده.
امروز عجب روز نقل و انتقالاتی جذابی شده
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91552" target="_blank">📅 15:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91551">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQsZcgNcA3Osdv8tTnO9yj1AlzUNjHCkelSqssQbUh07Fl4UeeqNzCJhLEZ-SE7MH1YimzgDp4YI6LWpPA5k3cTi8I93YMaQHrRYl1yWNcDFVnQXjyjCSqolRqvF7UlpjsyoGTWC1zcKJarWA2ZlQ2UjeBqTDi6lTRukSMTvRgNZDoSWCFJ0Aenl2Zu8a9wvZfMrrWeGZbBpFTRyxThtQomLKW9ycejNHJg86xzyYz2Y2uJdjt7LpfUk2IRnqrOtyJoWSPpJQuBzUXV2ANh6tU7vLrrMTQdXhP8mK2s2xvthr6QfiZqkDZ17X2k1uwU_zTjREXwYBqIlliW4rfDqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خوزه لوئیز سانچز:
به شما می‌گویم بازیکنی که ارزشش ۱۵۰ میلیون یورو است و پرز زیر نظر دارد بمب است بمب
‼️
کاملاً باور نکردنیه و وقتی اسمش رو شنیدم بدنم یخ زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91551" target="_blank">📅 15:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91550">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1C9Fj1BhrZRU5deVi4D2ZndZZZ1Y0fdg4fnHSZfytb71vvg8mMudH0aeyI4Vvj1pw7jq6WdtBixcyTPqmOj7oZ7cS74AUIrsichak-mXX6b1l3jm9jJPfiboWvm_-F27uJR6V1R_gRUKsPS8HxWaJs92O4SAexVdGJFDdIr4r5Vfc4I4z5O5V0zd9dj5YAC5JEMK15pG6BIHwGDmlftgfWTner-DJjoyEDJkXZpb8CCSMlPazmbsuqbnQeGln_B58z8uTijK9pPAqTIAJJnGkZZC-dMdp_W93eTrQ8Bi0YzUlGwd7kJSs4pkq1oXxzdjm-8l4Cjlb8dlaExQLG01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
سانتی اونا
:
⚠️
اولیسه در بایرن مونیخ موندگاره و به هیچ وجه راهی برای خروج از بایرن نداره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91550" target="_blank">📅 15:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91549">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LsWSzs_5y-LIoqtDINRHuQP3JtHZoxJd6aZChIFsLHmVg-ufKnC2aPXlMyrMHPPbA4-dn2k9uo91_bzuRkdoZd8MllC_AgLV3R7dHw0sdta1jsyB1N99lDRegM2UXmHTraOugyNf8sYT-HvjeNoh9fGFRRmgQYdQV2LNv_Yla4GR7B_7amA8uZ2a6Ulaz8NE1NdTS6v5032HG1PiD5QhqHSw0Q2--5IEE7ykdCgV1iJgbPCXCUjwn3biotQD57iaI1ZnK9E6NX2dm_4tuYy_7caXK7KfSMCQBj8-oicwwgwMXMIQgsJWowfTKun-fCrxSiRVjssNEpww5tbIcrx-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرارد رومرو:
🔺
پیشنهاد آخر لاپورتا برای جذب آلوارز: 120 میلیون یورو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91549" target="_blank">📅 15:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91548">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
‼️
دونالد ترامپ : یک جنگ دیگر را پایان دادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91548" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91546">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ocwB4tf2x5LiUWkf1Yms-JSqdC14CulcgNZFh9ulNjlT16Ug1D4yDkb78Y3JMdW7ybVZ0d0LvU4xHT9GgYodxjGyIdCtdnxT7-NwbPp5aI_6FULIUWs-yA-ZEdhuVc_hTtx_2nsi0AWHhKd1ypDJ_KJynsv3aTCUJTRFOYP7lSbrjclNO-oawfyX1Cm3zPkw5gf2JJ2cxZ3hYhUhJg2IcudTVVaAXryyllC__9v3WxYw4DxDkEesuS-Ly_5thX8-H73dr5NIe9HiItgGFr8flugAcbzeksQwk258AfMeagGqefKZ0x-jwody3MFhKRagnuwHs8eOPW5yFK84jTyk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RLqMKsM3iq3TesSIFGuDk-IefPNr2nwEIW2rCBrozGOAQ8LRpX6yCj2-0z4FhQNDwnNF3jE6MoeM3GPdU8FDw22PL9Zm9_4a02eRrW_DNW9RXHioKBc2ApsCuRBMwAqhQ3dXtGHDH33izecJ6pqTcjZidP57koePgKf7eaKG7lYBPDR7Ajvuw8W0hKDMRkfUQ8pmgauYrs9w8sKtLvjWYe8EhJw9cfW4IlBpQZKgFQabLtS7iUqvz6vyr3oRaTRWf0S7xI8uBpeG8nGOHv_JEdfpd-Regaflj1z_nahMBIK191hIJVJntZgQ-u1ISsXl7TAY8Ng-4KfiThaPt3sBRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
#فورییییی از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/91546" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91545">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV0khpivu8Ydpynkv_r0yxbeIfEpPVfWCcAYDEG8MdiqvgRzT6hLgpj7SWCrbq7bhq9fOLa-MgrT_h6q5wAncsPVd8Rq6PQIEC000spI7hwQ2CnxUW2SrYh8vWWrpcVEd9yU3oSNWKHUiLtQsX-OFMv9wvyWasAj9IBdZCBaJ_6A6BNaf6ZolbnfESUrvUuHKBk7lvQNHtvv6UcPzT_FNZb-G_glgMzXOKEO6HzlDbBMpwU0HlZilWkusJIHyZ_XT7ejYJ7_-ut9X_23dTMgWcDBuKtC64rXCMbI_7-WlpH9whucKIjR_6o9ZAtRNIWkCQRl_x6z_s4vojMxhrarSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فورییییی
از اسکای آلمان:
⚪️
رئال مادرید آلوارز رو بازیکن ارزشمندی میدونه.
🔴
اتلتیکو در صورت دریافت پیشنهاد 150 میلیون یورویی آلوارز رو خواهد فروخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91545" target="_blank">📅 15:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91544">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml46vGQE9TkqophdxGXJ5eNh8P9v4edOkZwqS2nIn_sIavg5iN1TS1HZVr64G3CsDra4IEDsQCw04PjpB4-S6sayQvjYF1vAxdGqClHTqXMiCSGzGz3dG35joPrM8DzpbrIMxYmyIqerQJQsJAsAuGAnXYFnY0k-6KjZANUrVtkqD-dPhA3qSUMjvcxsF8LzRYy3z1wfv7ulKO8VxX51FbWMXNDRwmwqEIWcBDsKy9JNVXJ0OJMNmABVj5mbBtS8WNkUJea0m5BFs2_jkJJEyDgC_devJcrMv3i35O7Iz03p-ckOxuY6YHpEfoyyz6_q6E-zG3cb7NrkM1y0wxVV_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
من درباره شایعاتی که آلوارز را به باشگاه رئال مادرید لینک میکنند پرس‌وجو کردم.
پاسخ رئال مادرید: هیچ نظری نداریم.
نزدیکان خولیان آلوارز: هیچ نظری نداریم.
باید صبور باشیم و ببینیم چه اتفاقی خواهد افتاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/91544" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91543">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D4p-E6YxA2GnrWR4ZlA9lfMWfa32knkHsqhA03QNTw3tVfVslY9jyxteOPc9Imq-VUMty2sHTPZaBE-A2lN8n8-DnWtZxEC33lqYnCwCFk2piW9jiajWry5Q7HB5k0jao_fUq4guVB_HGtuwFXcRdrUYRBVFxhU3w0ZpExlgJEqHtIRKVd0XvNzp-R9OZ98omnarEY6C43Lof4yu18QjiaC3s-fjEc_ly5-AK544R7g9vNBqNy1yXrMwf8QtbxtkI2dhF-BShdl6G5NTQixl4cVifsYTrB7X1GQER81uQXHtnA1s9oBDwFv3SKF4b-P_NtuIGe1WVgL1ME4CrknrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📰
رومانو:
🔵
منچستر سیتی آماده ارائه پیشنهاد جدیدی برای الیوت اندرسون است. باشگاه به نهایی شدن این قرارداد اطمینان دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/91543" target="_blank">📅 15:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91541">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlsIycYOtsJ1xuXVEBuDtKAFwDFdlKR4cJowwhapxi0SEXUmcq66ZregezHyELRpgj1n-xMoOFR4rreIaRpY_2ZcTFt3J257dft1qLMU5ywEYS9PHIfj54rfUbRAb27BGmySNJBBBnA6m7tsSO1d_TJFaHfbX2yTtZmE6iCzdRgZXUAtqNvKcHvOU-hOHoGsdWCvxTrKrXq-is09tABj2-PnHixJaEeW3z6HGH65Y8KqvXcHayixQxeGJ9TAkBWW7SopAxs-TJlcP_8jHWqnkqf4dnE5PXeYzwgiz-RPYUu_TENGElzpeQt0cYidejQ5Y0pTq4StFvAUMUPa97qgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVDK2wQ0ZKVOySVYpRSsQM4g-vX10eL55Ee7OKrO_kAdBXWuq-o46IGOCsfYq5gCj6y7bOFAqsf-K6V2_wt5tNaYvGi2jnSgY2P18r25mpKc9K65Gr_B_7ONnrn4UqiMRBRATvn2ETh7PRwSIiIZE-X8EDsSpBn1j4UN4lVFx1YKguqqDiz5vLF8B_OmNceq8sI2rcOecLW7N6jK8o97pp9_T0jBbY0mAxApBKCtcoHQtQTKkTDN_qCXsvQ9aQJW2xTGQ5dtyMrMYGY33wHyC-Hd_sgqDFNhUzzApr3wxbL1TVLEO-ei_a50if1wU4oMpAiMGb6WP2Wq8wAOQ7SvlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇷
#فوری
؛ قرارگاه خاتم‌الانبیا: پاسخ دردناک داده شد و پایان عملیات اعلام می‌شود
.
🚨
🇮🇱
#مهم
؛ اسرائیل هیوم: اگر ایران حمله نکند، اسرائیل هم حمله دیگری نخواهد کرد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91541" target="_blank">📅 14:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91539">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
فوری | قرارگاه خاتم الانبیاء:
ما توقف عملیات نظامی را اعلام می‌کنیم و تأکید می‌کنیم که اگر حملات، به ویژه در جنوب لبنان، ادامه یابد، پاسخ ما بسیار قوی‌تر خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91539" target="_blank">📅 14:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91538">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_kvna0Aki8i-djRFJBVLsfq7b8lZEyDfdXR7EOutPObTibkLTeSPBos5NtdzyrQz5Yg2uiJatoZdsJaccy81LhC2kKu0Sun9AxYpbP4LbB8dzVDQkfDuIs0hE7aFjATqbAl41u_lG858fWQRrCdEvxgAL74QerrPbdAf-H5TphwmEw1B_dm17Hvp4VWeDRjN7VM3eDBT3ZQP8TsCpCCJVcvVUFID4HShCecWtA91rcuSxF4uTolhaIhtkuUoKsEpqSXVPJEMh7pNsLQOs-nO7-fPsvKkzY3LFnGpoW9k60I-aj1xTwNt7lpnfYjJ48qAjYTjIsqXwS5QevXG6codg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف تو من هستم نتانیاهوی قمارباز
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91538" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91537">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoyZUGeBuR-0x-mAZZ8YTmCUMn-gD6crpIZvJJR7nCM8o3VS5WgkNZVgdZQNMQveq132cLcy0jf29GgFKUwBQH16HZa7lcwYDvjBV3ZfQQ7vZNlZcqeVecDwd4zqieg8idtVmgB6O2bA75SttwWooOfR4k8_ODF-xqE7Rmo4eEEUcrCE13gOxDvhACoqu9PNVg5EZ_Ii2Ped6aUtmhZkCTwXuEKFhFMiHUqM_XKAqZ6ssh1Abbs9yW8tKw_uHaZ0Kfi510342xZ0moVfbRYJGuoQBRYhhHvLrLp_65zRiUtmTH-U1i6xKVJXWVTj5f41IchIp99oC-qzgYJoaBTowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفده‌سال پیش در چنین‌روزی کاکا با رقم 68 میلیون یورو به رئال‌مادرید اومد و‌ در 129 بازی با ثبت 29 گل، 39 پاس گل و 2 جام این تیم‌رو‌ ترک کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91537" target="_blank">📅 14:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91536">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=XXGL4VTSnC7de-ZrqMPsl80pP7VZV4R17t2GpHArahRx-286dp-VLF-_2V6xhj62G81WE4OLbGrGMbgvrMDDoVtySXM16Yt0x_XKjHCBaFYCk1s4Y7qx-Jp8Dau33y0mG7_bGZSk72pwWbg9UL9dAWqZ2Prr6fdNqryg00eBO6ff2Slh_OJKSCFvZN9sTncsq5GaXRwQkXUiXvuujooFxhx_PjtJMc_7t68xrsmcbiso5cJml0hfRe1nk0Vugi4mJwyyZEIKRy2WKrj8dXIzyVghAH3M2XDoq5E_LLw9oLz7mYOaNDQagl5H7xsAU-h06CF9Jf3O6vh7_Whg7uyvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662d05e7ae.mp4?token=XXGL4VTSnC7de-ZrqMPsl80pP7VZV4R17t2GpHArahRx-286dp-VLF-_2V6xhj62G81WE4OLbGrGMbgvrMDDoVtySXM16Yt0x_XKjHCBaFYCk1s4Y7qx-Jp8Dau33y0mG7_bGZSk72pwWbg9UL9dAWqZ2Prr6fdNqryg00eBO6ff2Slh_OJKSCFvZN9sTncsq5GaXRwQkXUiXvuujooFxhx_PjtJMc_7t68xrsmcbiso5cJml0hfRe1nk0Vugi4mJwyyZEIKRy2WKrj8dXIzyVghAH3M2XDoq5E_LLw9oLz7mYOaNDQagl5H7xsAU-h06CF9Jf3O6vh7_Whg7uyvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد باقری هم سایدشو برای جام جهانی مشخص کرد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91536" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91534">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LesQaejXdCYxw-OJTRNDqA6PwPXAnJC6vo98BU_Fflsx31ZOxvr8OENV18X6-NYtqN8ZpCWIgrNey00zbuzkjs-BnECLI5JPwPuBYbLWMx7U17eYESNIT2PncwcUAlaz9u310wn1ESoI19wcRFt_vqEqEnbgBqDyLvl1atAN-4uoMx2cgdXLNt5fOAZD-rGFg1maX7fVcOU8OtAdYkhOrLst8e6-zen54aZze21WgyHhFi0qP4McA4y2p6cHaxBqciBUBpxB-xZRpY4N6F2-p7kJSQkBrR08u33Z-kjaH-A0iIIW0HWnvJBL54HZuvJz4uobs3ilipHWeY8Rlpz0Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا یا من پولدار بشم یا دنیا جهانبخت تو روبیکا و بله چنل بزنه.
واکنش خدا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91534" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91532">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ir7o5Nc_oAL_6oH-1MNv_uLku8MGRwFNDBrIefgu1rbwxjufVxFW8ltp-bOcaUGIdB-BiPwI3DF5G4C8iJELYgvZCXtxsFY26JgPj_rTu0-oFpmK5qjXO9fX5pL_wJfD60i6m4LFNAkKz2-xlIw7jmzFr7FQGWkh6ouSQrw_g5ko-0OUXeX5xOSWSoo5lgSUJk6yYmUxLqhOPXk0w0Tcupd0H68-tpoW2j8qSxyXf-zHBvM2orRCWfj5Hqebk7wU7qBpibuP-36OufAUiYD2nTahU9p3HL1vCY-oc7zab_AcT-PIGEfgNAC4hTyz564qaRh4Xb5PVr7bMswYRWvlOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⭕️
🚨
تنها 3 روز تا شروع جام جهانی
تلویزیون دولتی ترکیه مسابقات جام جهانی فوتبال را به صورت زنده و با کیفیت 4K و Super HD در ماهواره ترکست پخش خواهد کرد.
TRT 4K
TURKSAT 42°E
11767 V 15000
TRT SPOR HD
TRT 1 HD
TURKSAT 42°E
11054 V 30000
11794 V 30000
تلویزیون دولتی ترکیه با بهره‌گیری از تجهیزات مدرن پخش، استانداردهای فنی بالا و جلوگیری از فشرده‌سازی‌های مکرر به‌واسطه دسترسی به پهنای باند مناسب، تصاویری با کیفیت بسیار بالا ارائه می‌دهد. به همین دلیل، حتی در مواردی که بیت‌ریت برخی شبکه‌ها تقریباً برابر است، کیفیت تصویر TRT بالاتر به نظر می‌رسد. برای نمونه، شبکه TRT 1 HD با وجود بیت‌ریت نسبتاً مشابه با بین اسپورت، در بسیاری از برنامه‌ها تصویری شفاف‌تر، رنگ‌هایی طبیعی‌تر و جزئیات بیشتری را به بیننده ارائه می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91532" target="_blank">📅 13:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ملی شکن⚡🔥.npvt</div>
  <div class="tg-doc-extra">2.3 KB</div>
</div>
<a href="https://t.me/Futball180TV/91529" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
🚨
🚨
✅
به اشتراک بذارید دوستاتون وصل‌شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91529" target="_blank">📅 13:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLjkTeuEic16YS1WvbROcDl2scBSBGq5Ml7fJhBBkfZ4r10rM2dAPG1Mr5L40cTXw3QNO2De1DCeEuQ94JV_7ui2ssxNa_Cbd4yfzZWJeGkn0BFgICTagDIU9SEV_FCCrtFA52u-yL8Mx_8XNoqTP-iLdEdZcYpPv5p5QA5wy3kAjc94U0SBjvvsNvY2_oYb6NUYI2tImT93FH8ZtopU2SUmGZv_fKftkR-AziaP_BL2livM6Ex5IrB384nCKOknfmFoE2D5V5pY2zcKcxFxS3EF8Gko9679X_UNmw6n19y5ipJ9Q-8PY9pyamjrMZk6JeMaeF13VXOpaDuftZU1-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91528" target="_blank">📅 13:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:   اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/91527" target="_blank">📅 13:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91525">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
فورییییی ترامپ:
اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/91525" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91524">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سازمان ملل باز هم ابراز نگرانی کرد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91524" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91523">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/91523" target="_blank">📅 12:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XclGtGXxD1h6puRYs35fFk1wh8P8cJhM7GEMFvY10MnCEA31kIGi_5w2OSLEEFCZNym9oIg34WAsbaKMDZhMz-_hOxrHtAmUBbHt1S-yq7jq5-cEZHtN0hCYweTD_6RqNabX4vDBfx_CKjRDP7JbHkIw3nbm7dJTmPxRVNQyow74zW2ZtxC1X3UJ1xAN30FFrsin1dAu3G8fKeXTUMKOdK5x19J8DA9293cLrDGLcOOo-JJ5p4sD_0HdFjbwyj3WvWWurtWPXRqm1tjb-vQp3QwJtDIc3dhRpANp3Bet_Cq26LphIv4JXbJ-DdM8QdWA8pwHv7EWX7sHH4TZSO_G8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عموی ترامپ الانا زیر پتو کنار یا روی زنش خوابیده. تا بیدار بشه یه حرکتی بزنه یکی دو ساعت دیگه زمان میبره. احتمالا این سری علاوه بر ایران، کیرشو سفت حواله نتانیاهو هم بکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/Futball180TV/91522" target="_blank">📅 12:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/Futball180TV/91521" target="_blank">📅 12:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91518">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loxSHXmp-TwRzYaIQIB9s3sC9Nsg3Ml6i7bJqm7ZobhdWPum8E3zN369QKru-zRMeLGDx6FZXt8aSsR5Yg9HfLwA6FllyHqGGUuaFe1yFalSJgpwmVRrecGFr8H6fXOIaMt8s9GDE4esDFInEzjyxJ_VMesVjFd72POz0bxAeii_RaAFi3cYHs-jfNgT6W3Kdi7IeNf0bZidgrMF80yd33eAeQHy0eywvx4t2Vuxk7GKWiFUWFYn0kEI8cTuYLqsctPQTFJK9F3iC3NYw0bmlVd3N7-RhitS3J9Fb58EKoagsG6_e5Dcfmp5oBh8_YCXksRuPToQrb8VChOssmIiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
#فووووری
؛ عبدالصمد الزلزولی ستاره مراکش بدلیل مصدومیت از ناحیه رباط جانبی جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/Futball180TV/91518" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91517">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKggjMKdpW-scenFZORrIe67Oaz5XBfrE1dpHLehmW59V8Y87KCL6F19ht03uCQ4w0PQs5vF9HlYRBgvY53Ujni_A5gM0irzIGAu4lqoECb4G2invyNOnQOXc7IPPwc4dE9WlNIH9yizxTfo0SoF8XNUUqSDg1YMk4jym7MYRANpyfJKpP9n5MLfWIEFBPD-jJRE325Rsu5uk2Lv4uWcCzur6bjNIDc8OGQLLjjIpbZxC0dmtPxmccIzT0byPLUWzx30VSpgM7gSotmnRhZ4o36WClicdoy06KiuBewEpumM6gaVBVFsjZJkOzSrgAtTe4vjviF_YAUF-IkNIccVWvpE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3302fb4017.mp4?token=cq6UcyB53PwegMWf4y7xA4ftSMJwZCgXGDEA4P-zKz2DLPjlyZokQb5JZdP-X592lZG9I0Z0PqF159P-FoT4KcwIOZaV7n_fE10d5iKZm1aKCAHiHRBpxCas7oUYBZRz8wSLZy025OmOQZFXMj3fUnG8E0aSbduJ36Va1AtrLJLH1tfFhmV7-HibSmz34AWX0rCYD7XETG-u8K27LKS67gxj395RaKtMcCyIg2qxKcztX9Pm70pJz_U8dZL9C8CPwpZjqOZgjtOJWIgYs1mECkKyD-ZgbtSsa4ANHAivqKIUFVZdhG4HC_yU9umbhP-hD3ZHS-kxcBkezHHZALzHKggjMKdpW-scenFZORrIe67Oaz5XBfrE1dpHLehmW59V8Y87KCL6F19ht03uCQ4w0PQs5vF9HlYRBgvY53Ujni_A5gM0irzIGAu4lqoECb4G2invyNOnQOXc7IPPwc4dE9WlNIH9yizxTfo0SoF8XNUUqSDg1YMk4jym7MYRANpyfJKpP9n5MLfWIEFBPD-jJRE325Rsu5uk2Lv4uWcCzur6bjNIDc8OGQLLjjIpbZxC0dmtPxmccIzT0byPLUWzx30VSpgM7gSotmnRhZ4o36WClicdoy06KiuBewEpumM6gaVBVFsjZJkOzSrgAtTe4vjviF_YAUF-IkNIccVWvpE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
سر صبحی خواهران منصوریان اینجوری به شکل عجیبی به دفتر رئیس فدراسیون ووشو حمله ور شدن و خیلی وضع بگایی رقم خورده
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/Futball180TV/91517" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91516">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
تا این لحظه دستوری از سوی شعام برای قطعی اینترنت صادر نشده و شاید دلیلش این باشه که حملات دو طرف بزودی با میانجیگری برخی کشورها متوقف بشه و‌ دو طرف شرایط سکوت نظامی رو در پیش بگیرن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/Futball180TV/91516" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91515">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کاش یکی به این کصمشنگا بگه اگه با قطع اینترنت فکر می‌کنید اسرائیل حمله نمیکنه و فیلمی منتشر نمیشه از خر، خرترید  اونی که بخواد فیلم بفرسته نیاز به نت کسشر بین‌المللی که به خرد مردم میدید نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/Futball180TV/91515" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91514">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!  +منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/91514" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91513">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
حمید رسایی: از آن فرد بی‌خردی که اینترنت را وصل کرد در مراجع قانونی شکایت می‌کنیم. در شرایط جنگی و حتی پساجنگ بازگشت اینترنت یعنی خیانت به جمهوری اسلامی!!
+منظورش مسعود پزشکیان هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/Futball180TV/91513" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91512">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
لشکر10 سیدالشهداء سپاه کرج مورد حمله اسرائیل قرار گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/91512" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91511">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9YPeaZOz5rVvTLFl6XPx8PodT5yxXcrZ582BebLK5Y_UTb9JRfSRsZTZebkz7cBIeGjtkkEf6Ebthqh_IelHHgAMCmbnDHkQU3z9l32cP4IxxGiuujOxlQXrG3_ef1sjGOLmh3uBwMa2xf0loafgRNHfmsukdVqn3wqbSjjliKi5_85X8l4cx9v384sfV1axojrl574F2HLEyS8Q4fNM6TJHFaba1ZsqGxa2vcavtMmepmTTeio5eVjWcUDQv6Zz2DBR3V5X8yGuTo7CSiClSWiVyHzLJrhggURZC2sEBxtV7cqpFfnXQCKWlRD9S6DK-snBG3GO7e6Jm6Qvw8MSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب ایتالیا در آخرین جام جهانی که حضور داشتن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/Futball180TV/91511" target="_blank">📅 12:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91510">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/91510" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91509">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هنوز آتش بس نقض نشده!
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/Futball180TV/91509" target="_blank">📅 11:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91502">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i7QpYgUluH3Clk0awpq8w6OhtFdQ6mMrGzLvpSLFVTGysjufMK3I-8kDS5M-tKhaTDecEiDQZXAqMDs9o6zIL0wMnfn9m2x9tcBcCekjGeQ9RA9UHaqykIN_dcsfLioRh4uvnJ29UQLuhMAjgzbe6kDF4JhHbhEsIZq7F9_71lV5xXmDqT8fCd0podHafFKySFfjmhidB4Z5vl6nzCnq_pRdfbMs4muMnxVBdjPYACxXZhJ2oozVvOtjxHb3VQROaZIpXdcmTnNAdHN2wurKjwy1HWUuBVbMiK2kmPpUfpUwas3tuG1-3LZlZ2pDl0W-bqoMfKIsqgVdxLDSko1Zfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/amfaCR5g2Z3uP-Q1x0FFuuiTenh8T0IDrKXZVCeWTevSpbv4STP-588TIYoaoyH5wFcqy1s05rXVhcZx4IbXa5F_Kd7M2SFrF1-Au7MEsiQuqr5uiaNwTIVzuR9Cacj4qYBgDpdvmhcT79sZdCUMTUhr4GqoNGtXuS6roOZug3u1QuHbAD1_2HHZjJN3C9BOZV_3hbhMoxx7Q4NRikpn3eWKtC9fmO3VJS6ytzwtEg_Rqvv3nvPIwKMHW4u6xhDUhjP21jY7dxu2VVQPmb5FTXzdwuEzrcYYSOWRN8dWUvP71jiEnJz9Mt0UqNt5DTCNQAGUiWkbR_FgHG_TFlgWFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDVfEuUkzywkhqlpVog9-3BhUqmJrH7GLJFBAT-3YXu5-5ZBtdvMzoSVDAGgDtEH6_1dM4pC5tBu_wNS2m81wKJFxB_icNrP7auMCygU2fpg9PgV4k9iVL9qlC4IL6rwJUhHUcE9j30Ae7pXBdPKbEcy1keDLQ6cYnWZEcYtr5_GW8pM2Q-tusKRUC5g8ndKRSxa7FZDZYBKlY2UNJmOzDy9-kpQhOszixZxehmQnbZiAKODElePADwytEx-5TQjiTs8UdiO69h9pIgPrsqaYIL09C5urBa56mysOTz7YGsTaLBRkobQpF7n-_AFONGr8iVbi7GF-bhskJr_IvL9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lmYZaX0dAazTkEUNqMhyaL0cytPE_aJpJJLgD7hrEfAJRzL8Z_GGzKnsq8Lm8C2P9_Zk0QdNZYLX7QGfSC3uK1ZukNsHsfbXL3csT8mrY5QdhqpDpbzA8FH1ZDarn8hFZBpYy5T-KSW_QDBtexjzlbyDEesRR67UVX6RhGJGMKxNQAexc__HFdTBsqAj5WIB78cFIL6PLbvHITKII-Uui0Hw_73PlJruH3zwygPXPozeyLUUVNfKSGhiM2t3c82JpJaV6AFTkdJTF4wW0tHKmJsD_zeLZfn85HdZsp-7IDaym7ojrB6mWh9ozRW5NT5Yr5s6UyfvXDOO9e2p8t7OvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TOoqy0BC5JVURm6LsC2k7gfncMmnX5hmQY1QpMfoQE96iyCz2EiCWJKWSz-mNYVp6k-G6zl9J-PU7FHjT3Pz1AR7vXZyF2O1FnxjJyKJBJriKs_mJ1BSxlSdlINgEPG1qqNMfmYGd2NO8W38iCtP07IK6kbA07crrVgBrpjZ18mPzg93QFqYBOZAdWniFLgFEiTsDAmJQ_j8IVEDNVTgBj_BjTpehkFcSW07GfhZ24Il65-YT5oNZzPUWuBHqDjbZEdrYs0TsmXRh6j5UPmWC3ZADoNqtygTIwNPqGei9cr_6t14uzlIYx66z7Rozu6PDuaIA8KXwOqSamI1E7zQPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/axCFswY5HKT6hjWLzVT1B_bcCNJ3mhhMLpUw79ZOp9pXBYoKDtPuhwMXOdxeAfKEXc_Nij5q27RkSdkYNWq0g52q-t5hrBP7BGmWX2hJd-gImON8hAxQTfeXZkO8ccJogj2DiX-gyRGLDpg4uQfsN4R5VAjwZqD-T8hTzztuZKplMvNDKvP7X5PUvP7yG6NaegZykdzQjRLUHj5RHyhtA6NgyAb74WefrXkcOZ9MJDW-ZFoAEwcRSAWBBg-THMljkLloNTB_WHOoFdHi7dh6N4cdmYdp6zXGDkUEmPGUIQ-ZT-ql2Z5IJbFXyscb4J8iorrAHeKwoMpAxT34-yVfdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUmn9K8uffmJqN_PrMdSeSY7fuNbT7HltUW_KyBLu-mbxtVxmwxcL3WafE78CVSB4DqO2m4z0uUBzGKqPvW56NF4AvuXM8BtPNeqfwMDhjp9OXPOWfabWOl552uxB3aDu3QGV_58nIEzZDCqWPIaRBpN5szx_wKlhG4iRzQNX4CMqgp_gowHDPKeRpXtyQ91_lCf0kxlJRBgPjJV0qW1g3yv56pG_GDZ_P-z9t50j-plli3QoWmjAPr49_OEk8eM7yNQsgI5JvT7D8cMz5w_1DLuA7LTvCm9LSeKCFf4v-y9522y8DVyPBHsVl2rW30O6VUwyVu9kjuX1D_i_eEzyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
تیم افسانه‌ای رئال مادرید 2010/11 و وضعیت فعلی آن‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/Futball180TV/91502" target="_blank">📅 11:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91501">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91501" target="_blank">📅 11:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91500">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
فوووریییییی
صدای انفجار در تهران!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91500" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91499">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I873D-p7Ux1VG5IWaMt72iOuIggqvxj39aXFO7craUuwSlJJJwUOnGioqn2XCOgsxoUJ101USC5tNYrGH3JhUKx1azqrzC-2GL7y5M-Vycf4-1t2iMirHWCxQg7pNswVjbD__x7DXSYdn4wi9swzWFJpto4RBpWRfumwbSwy0arFrmiDZtMc-EvYocPA9OR0grifZBkASJ1yLHVwoUiUsnMyd3OUzpJovEdJvxNMgKbGaiXVk60hs3Se2W2QKYeRpPvXnUNkgtHyR2qY64HOfpHBQ0ePZyW-s3S6PuJuzqva8SDn0RgNxT_AzkZfTJ2ZSGngcKFdKDXY2Z4nX1WbFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووووری؛ فدراسیون دانمارک اعلام کرد که خطر از سر اریکسن رفع شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/91499" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91498">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeO8MXmEhGSxJBEccBmcLjqDX8ALGnegZ0ft8kAXbYvoAa8l9aRI82LzpKpBWmTt2hyw2okwms9fQevUTPBF5x0jVgzNqIWhNWtwEqOB-P4p_dq4bDpRNQqlPjAjcqLm6p55JG2mCH65fhZMmbplYccVwZzHEMmforYYRBJ2b8-A-KgQoz_tAzAir01HZUhVZEYe2g17jRE2ukYUJqEQ6yGgDAGBsH2Q90xg_1rVXJTRfdJVEumKER4_SYJlpazdM7Z0Y-Ssa6qFVNjxSdd4QEour2RsnR0Kpq12F4YPzXuxKgWZH1jW6UO_oAvB_B-nn6wG9aaOK9hoHBtOnWFXYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
پوستر رسمی باشگاه استقلال پس از دریافت مجوز حرفه‌ای AFC و قطعی شدن حضورشان در فصل آینده لیگ نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/91498" target="_blank">📅 11:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91497">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
موج بعدی حملات‌ اسرائیل شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91497" target="_blank">📅 11:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91496">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eObR7-3ln9veze9pbwm34coGalusjNxcnt8-3-hbUugoUZFA03uBhglqmGiuN-hT1wMBwonH1u0i_am8kSI6VIgUaQMe2lDAk2EyMP6N_sefh_PIKQWhIiChywfORJknCoGxn8E6xOlNE0iEaY9haMl-26HS0AsrjpAGUD0uacW5pL61nb92jGAE2p1ySS2SIiX-FjpY7m9T9ED0XPhS_vjAkC41eSIKKBLf-Wx4NzDRZQi6DqU3ct07ngTt2ZkNQW1IxHwSwh2DqkA4NHG7hcPyD5zg4BIrpZI2hddIgPYYhQIArfKmxt2m4JIPjj39nd1rAQbmza7dsWjn6Fsbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ایلان ماسک: تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91496" target="_blank">📅 10:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91495">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚬
بیانیه اتحادیه اروپا: جنگ خوب نیست. متوقف بشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/91495" target="_blank">📅 10:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91494">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی ایران به مرکز انرژی اسرائیل در حیفا و ناصره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91494" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91493">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dik9LBl0D4eUHrzPNxZDDe7VKqAr-5bNoS-StzHxw_b-a21edrGemC35oITjvweYKhPIXIVjv2uqXqUK3pKleaxW-TewkzVIdNc13Oyqo_McIkX3dgJX-zc74O1KwldD5jgiItqCwNa7I1Wmhop7ox6bluTf8UMbRnTKd_LDxlw5ZPYhOXG-q1jWdgtRSKr8VTgBEmgKYXA_-GSxJZu8KzCzENYNWYnpo9W5d_4rber9O3t5HxTcanfavkMWgdNlQ7jcuWHgK5pqqzB_D1Q1HImbtU8yo9iEpXPVZYS46xZQUfu_uCIOzqvDPhngF2zpLQZqJYuZZY5OmaJqB_-flw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مرکز اسرائیل هم اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/91493" target="_blank">📅 10:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91492">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووری؛ موج جدید حملات سپاه به اسرائیل هم‌اکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/91492" target="_blank">📅 10:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoGvZMsdtYh9MqxjOLwnpeq530AYOpU0wijVyapzmdJDgLHavOBT86RZjQyIySF9IQfs1reAK4EtyCewLwTIHTRRd5MxRsZzhqwP5PPH3jmUuL5GpnwxlPWXASQG9F7letXttggE70Ew8jwjp9TkcCb2RBMOMsaAmjK1RVzE2Jqd4I8McGsqGT3N8E8kaQ16XlnNLLqelYLQ9TkX_nMxrOzYhMjC5ByIRb7zcBAKjdmV7EYGcaPH2-jgyzPDC9bPf-M_jvhjwQTZa7Oc9W_mmEWOL-3oM1eo8n73b8UZ9i6JG_6EoZO5_EDavBG9Hd8e7rVYLZ2ODUWL09TAcmKIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تفاوت‌قدی عجیب هافبک و دروازه‌بان پاناما که در فضای‌مجازی حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91491" target="_blank">📅 10:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91490">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران: ثابت کردیم آسمان اسرائیل در اختیار ماست و هر جا رو که اراده کنیم میزنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91490" target="_blank">📅 09:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91489">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فوووووری از رویترز: با اعلام انصارالله یمن، یکی از مهمترین تنگه های جهانی باب‌المندب برای آمریکا و اسرائیل و متحدانش بسته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91489" target="_blank">📅 09:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91488">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=uFHfQJZc2vVKI8LR0pLThKOixkkY8FJvvJZ0ayPVlbNb42qoHGiQfuvWO7llNmnkmOmFCOJFpzh1A2sFBYK250gPKXcwSnWqICH0xaHd_vK6gG2v6nfzvRTRkAErdvk4dEvoiUi3CyQzvIqsm0cMxnfWoDM4PibaUx0ARSpsq9C-KAzSQvzLiFZlFlhebwS5mvLaALTZiAWrQMzZwGebvJ0u_sCFc0Oi674Tfp5fdzDhdmQyTES9RjPPUgSk9HnqgG2AemO5ORHa0HMKB15QAEhKrZ-MsaAdA7aX1Xsb6UDGXZaoUW3w7jcY7vs_rRy8lPT-1JKONT7WtZ4o0o7LHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d14bce5f84.mp4?token=uFHfQJZc2vVKI8LR0pLThKOixkkY8FJvvJZ0ayPVlbNb42qoHGiQfuvWO7llNmnkmOmFCOJFpzh1A2sFBYK250gPKXcwSnWqICH0xaHd_vK6gG2v6nfzvRTRkAErdvk4dEvoiUi3CyQzvIqsm0cMxnfWoDM4PibaUx0ARSpsq9C-KAzSQvzLiFZlFlhebwS5mvLaALTZiAWrQMzZwGebvJ0u_sCFc0Oi674Tfp5fdzDhdmQyTES9RjPPUgSk9HnqgG2AemO5ORHa0HMKB15QAEhKrZ-MsaAdA7aX1Xsb6UDGXZaoUW3w7jcY7vs_rRy8lPT-1JKONT7WtZ4o0o7LHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ورزش عجيب و غريب تو اروپا اختراع شده به اسم اسب چوبی که هرچی از سم بودنش بگم کمه و تازه براش مسابقات قهرمانی اروپا هم گذاشتن. فقط این ویدیو رو ببینید
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91488" target="_blank">📅 09:40 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
