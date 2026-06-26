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
<img src="https://cdn5.telesco.pe/file/sP7IuOnoEyfCSWWMsQho6qEvmTbDcEeMrfmZwXgQJSs_rOi7UgDa6MgtI-aqFPlMFcmOIVdyjf7EFfVJMZ3H_-xSkjEwIoNpoqKSL-ccuWUSSNnJgfitez3v1K4RP0XOKB4qMmwn1wTJak6wrMXzcBpNrgC6sNKky-9kY5b4qKVwqKm09TNFCziG9xpaF27MhLZKcwd--1UOqBTeMawzoZ4l9p0d1hT8_wjBb3JExjY0UvIsyR6AD9TG1NDWLBovrR0N1jtcH_mDAI_wpR4WgykxR7Fiqu1RU1DsxC8aguQi-Xw35qMf2dlioaFqt7uNEny0ITcsuDVvvWMe5SWbHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 695K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-96010">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89114baf09.mp4?token=EH_r4hDuP5pzqP7UZlJDrtx_8aB4wVMHBHMGlwCK-_qNBeZSZUrKOWSKM-Fj0DyYkk0n25u76WF4ZmcWP98SkuEPk2qYjAdMO3cciDwM1hmesp1sajB3Nd6PZTIjjND3XD_smpPQ_kco9X8TZSJEZ2vmHnP6HImOMHdSVukI56PCT7fzg5BysUsBl1TQaGSNKg6uOXR2cvNfKcZ_eonpngsndZe9EKPtbIpsRYw2A0XrrEQgebEx1HCKZ4CDPTSNWZeO5fh35iIWnuCmpVoNmFmtXkm1jwc6moN60jFLC1cyqwEwLQ-n190vCjuhcXsha8EVG9P0M6LN__VuReEObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89114baf09.mp4?token=EH_r4hDuP5pzqP7UZlJDrtx_8aB4wVMHBHMGlwCK-_qNBeZSZUrKOWSKM-Fj0DyYkk0n25u76WF4ZmcWP98SkuEPk2qYjAdMO3cciDwM1hmesp1sajB3Nd6PZTIjjND3XD_smpPQ_kco9X8TZSJEZ2vmHnP6HImOMHdSVukI56PCT7fzg5BysUsBl1TQaGSNKg6uOXR2cvNfKcZ_eonpngsndZe9EKPtbIpsRYw2A0XrrEQgebEx1HCKZ4CDPTSNWZeO5fh35iIWnuCmpVoNmFmtXkm1jwc6moN60jFLC1cyqwEwLQ-n190vCjuhcXsha8EVG9P0M6LN__VuReEObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🇳🇱
دیشب مکزیکی‌ها به هوادار هلند یه حال اساسی دادن
😂
😂
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/Futball180TV/96010" target="_blank">📅 10:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96007">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvWKSb-jJQ6DCkvMadd-iTv-ze9bIuNeRw6EvYIXz0l7J5hurtDueDq3hoDFkutdi5TirqOgy8d866B8CVJaDhawaPeMCmKj6g9yl9R0GOq5j0DGt0eiS7IYVTpZWGqXLBUi1FrArAOtotMrNdgPFmwscOlGY3QIVaXKYSKyvTHTXajmfujg1Bx1kTR-XCiLtC67vRCApbOZd-gxZWgpT2TabYxbe35eDgy6RGB19UjQl7nTMSn7ZuqL4LIjQ9mY5jdCdc50PwZKDNVRk67SKnhJehQw_wAUOHrABGhf006DWF1rXkpa3-6tzXAEU0cWf3_Odt7AwQckGeqL6gyLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phVierVWSZv5l4OgpW3LTobKxZdPmHwe-gTz9ICUT0QeL2imlcXnySrCBEBiWbcGAoyDmg2Cp-FusXcbXELsMzdGb9bfLNnC0bG7WKqkzq-kY7dc1-JRWHd1AqwxdJa8P26eeuKwmQaFrfs__nTXdnB4HSGGOxE_Q-WWhYEPzINKu0aqKXet8VjkTBshsPCgO91uxiHBcPYY-KiGD6fFgfi2gYUVkz9TTao-CwqK1gut-6-4a0RvU2jGSuLHCcKyNaXtzCa0WajrrCU0bYfWQS1jX1U954SlKK0TyGCyLpIJoIX56sXeI3lg9KBfOxT-XGyjuXHggBnk0uzmTOA--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuH7Mxzn5XTIqDCcoQhn0IWeiiWxPhkuLatEmabwPdrYQxqh5QLQKCLXRHP4x-lLdxHs-I5ub400NaB-sSuV8EIzAIZ0XD4UNmDh9iNj6hsTYKNbz4iDkDZUG5ZiL0ihH43oqhWF86eQtSwhhjqBIFLpHaexrTLitEKcAeEuaGYpliEATAsDCx3LBCL6VXZ1Yx6ZViMAMXgB8xPSvlPayzdmdZIiiNoNaxX-tHn6FNI51j1l_Ew0YP6ONViItEva56OAOuNV4-o-vjcn1qouUdebC_upJByH2WVnLL308jNmVEcIXY_CKCDCLa6TFq6DltfAYxUIpv61HHe_s56bdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چی از کیوت بودن فنای مکزیک بگیم بازم کمه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/96007" target="_blank">📅 09:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
ویدیویی عجیب دیروز از درگیری سر گرفتن یه ظرف نذری تو شهر همدان
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/96004" target="_blank">📅 09:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96003">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=LBGjz2DNn0NTy97dyLziGihaY8TuVAA34yT9Rjk0Ah6h7CxI8z-yWmK8ifNzW21qNjkAbvxGfmvJiA125EV4l_bd3TLOK_TS5HtyFsQJ6qNl-yWdjXIpjNgz_LSzZiu4taqne47isyPaB_YsGQa79iZkIaH5G-LI0p3ri3K6FY0nmaEmnxMf5zz_fzpsaxjvHHPxkMW2S30RdOiQ5PaEe6A-Y0jiQ4y4IZQ_Xosa6t81YBrSbQiYVXs9fwXW06yL59RRs7L4KopY4p_YqguyG8Y2wEsJrKblYdjtHKbZs7ddb9BpRMBrF5Ofiz2o6FbpOJZ57QGY16DzR57i304v1FgsFQ8QLlVzLyxGizEtRs3XPFJYCNM-zu4Z27gpP-KynNvqNX_vOOWgZ3EINHCP-Id1qf07h6QUCUbxQKDZKAixb_p_Fx9C4kAm2R3ENhlDNG0XoS-6kJxy1cPU-X5qSbQhOUyT9mITEHzfO5eP5LcHgEoodJ-CIPmtGp4NH86-Amf8O7vbdPhwYVo6u9YNufgsBj7NxR1_Yk75Da9W6qF4MuVzSYnCSphtJ-FjXEPZCqtj_rAOooDWBl-H2nfIRAyNPmF5lIGnJ3xu_yNPNqY_nDozOasDZa6vVFR1tSCN6RbyQHrD0iTft_37vD8t2WSKCe4Y69GSlPB6H_MKAT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=LBGjz2DNn0NTy97dyLziGihaY8TuVAA34yT9Rjk0Ah6h7CxI8z-yWmK8ifNzW21qNjkAbvxGfmvJiA125EV4l_bd3TLOK_TS5HtyFsQJ6qNl-yWdjXIpjNgz_LSzZiu4taqne47isyPaB_YsGQa79iZkIaH5G-LI0p3ri3K6FY0nmaEmnxMf5zz_fzpsaxjvHHPxkMW2S30RdOiQ5PaEe6A-Y0jiQ4y4IZQ_Xosa6t81YBrSbQiYVXs9fwXW06yL59RRs7L4KopY4p_YqguyG8Y2wEsJrKblYdjtHKbZs7ddb9BpRMBrF5Ofiz2o6FbpOJZ57QGY16DzR57i304v1FgsFQ8QLlVzLyxGizEtRs3XPFJYCNM-zu4Z27gpP-KynNvqNX_vOOWgZ3EINHCP-Id1qf07h6QUCUbxQKDZKAixb_p_Fx9C4kAm2R3ENhlDNG0XoS-6kJxy1cPU-X5qSbQhOUyT9mITEHzfO5eP5LcHgEoodJ-CIPmtGp4NH86-Amf8O7vbdPhwYVo6u9YNufgsBj7NxR1_Yk75Da9W6qF4MuVzSYnCSphtJ-FjXEPZCqtj_rAOooDWBl-H2nfIRAyNPmF5lIGnJ3xu_yNPNqY_nDozOasDZa6vVFR1tSCN6RbyQHrD0iTft_37vD8t2WSKCe4Y69GSlPB6H_MKAT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇩🇪
زندگی باورنکردنی دنیز اونداف
سرگذشت عجیب ستاره تیم ملی آلمان در جام جهانی ۲۰۲۶ که با شادی‌اش، اصالت خود را با افتخار به دنیا اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/96003" target="_blank">📅 09:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96002">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAmhUr5tX3fI7mD-HAhB4_yDPa3gCSplH6V-0HOFxGeFGmUiiz49hYLFDO-5WFHVIVs9MouJaP1d-UuKhPaeiO7li1x46uzq0C6Owu3PjRLxT_GnS6JtNL35Vk3TFsoy-t6h7TgOPC-8uNnGOU8VhrdnhYzPtZ9vDcSHdEwiKgL7UWidABuj-6S45a_XSJD4MHJSJosTwGrvW3X6CAxngSNShO6zN5Ee1nw9NfEALRgd6pUew6no9c8wOQUrJIAfwb6Pa8AvPJdrIUmRlbNQk09J17SXPysEboeQOPYOLdqqMIo0SscsJqhL2R75ON56BZdMxFmKy2I7LYN507Q1XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
💥
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/96002" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQup4afvtsZf8wAQXXSLkl5whAbCOENXKUIAsnZacIv1YCPwcks71Am0XHq2HEwhUhPKzJrhGR2TnxooS_PtOVeFrDfoZ2N1Av5__BZHmKZYBINb1tQQbO-pIQkPz13fhLYVSGLz3wmUsMUEkFwPaJi-X6o2RDfzxwe4WbPGYbN9_1Kj0tHjuZm6-Q7j6LFDwcnzsIP5omBJZvEzF6xK5AK9aBc-xlSkGlLR8-HNJXUDT-HNIcA-UvZ9o8aB8lAbqJ0AIre0GuaGrm7U_lSohjbpnB6HcO_S_KX2BMHHyB11sSH9IXXMU9a138Z9DejAew0x8ePvgvqhGdUfS67VYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofxzi7gW_YbstvTNO-cDcd5FKTjDhpjarwuYthf5xYmjm2xBKL5nQGqkHLYUrwSM2wLK1_eqktKkDfQe7c0eXn3WLYXy8QLoi49vQ1_1vTSmFZ3Ex7MBL7MM9jAfmLxmy-r9HQS7rlS2pRByZHaNLiZuVHIyrjBU7umJ0d0SJ-Dv3MB92afEMwmwMNQ0JYQZ-MhKlJYsmi1LxnQWuN7sCaihZwEh6pT0u2_hd0eQ4FS9DkPgdn2v2oBxoOtufP6X2KgoU9TNy4O_0caqdVjW9YuxFTvW5rqWvk3Wq1GFfphm8kna8XraSZj3ViLBLKNJq7Qimuw2XbuUzkKiBajJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFeIG2TVrGN9iumTYDEYA821FEvjMmjqPv8W0WiB8VnxqulXraOJl_9oPGfeSy79k9G8Xa4y-DAmfZSXpIYELmIUrw0-6-2UnfrB67Spl7bIVZ0WPfFc8ILhCpL0NTXHpa3GcXriZt9Z1WzMNNc86hazJtutVK_TuionIpruGqu0EIyUIJliv7aqws4kDi_arq0MnYcYfyn7khge2V9GiTiICTn61rEHfHUrQ30ojcxvRLqS_A5BlPlW6qwJ7xjE9bCDhEOwfLQOEeKXYcSf5mbRPo_pa7KinyTLeCueglykajxQBloGSSXhGcEUfACGx8rd7WWudONuyny-WABwvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/95999" target="_blank">📅 08:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYYRFkXfUqmHU6TykxUV7rJcrspbZ686yb20938lNxP870hZtw6j1D9m38lu7Lo6VdRyJJ7_PnsKQ6CLSleKlsP4Vzj-kZZbP2kpN6d2LkQISvftejaXHI3tmOZ9YHWeuH-wdxeHfYsioEGEL1VaOnNuJjTnZqMAuJKAeBCjhNCu0I7EjDbHJa_iIH8I1Ldss2JzQ0ouKZWFKP6I-01beQ-jiJlZ_I_dOICPi7Be6eHHFtV_uyDF90R-3vtm1WDN8tzqPVF4UnnbWJKTNs7gDNCNIbzR_FANBW4XUfjqqQfe2yqzvZqyLqqLHznx5KsyDZ5EzxOzGYpeUgPIIQQYpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/95998" target="_blank">📅 07:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIlh3sboKLda6ykzgVfC8lw9agz4ih5XGHyg7sJEkoZLLKce86pAm6Y4HCc9wwJ4o8KewRTDUSTjUOpFliGK39nzCXwUyfTTId1vAYSRani9y4ApDD3cnCsMSX5FJmhuYfyG9lLNNAQPqAd-dVj5PiBMWWgO7BVZMp4HTcyfjGIuVqONqWyjCV4bkt4Zby-ti8_C7EHaHMTsBPa_3s_li4KJhMWf4QOiOr0Xnt8oEhZVpHX7c8NC4hy-OuLc_3Maic2qmLljAG8thvjgEfRlKtyHzDpTSaF5wezme-qysM34SKKy4HVrEYfN8m_IDCC_DALGk-y8RO0dcxj2rkdztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول بهترین تیم‌های سوم مسابقات؛ سه تیم اول تصویر مجوز مرحله بعدی را کسب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95997" target="_blank">📅 07:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqROEhxMICGZsGpooG0zrOZYomB5o3w8GsPzOwHIDUPvo_VBSAleV1ibq021x6gx9qZ_EKYHryMzWcXc2_6jooKvZ_tNdD-CmHcVdxdWRJ1DedaMLk9dIWQfJHo7tXxxPACkSz22jJ5-0DOn4KodWkf4P4fYthYzKyIn2uwvGf8yTaUl9yy9-XjlNYA_tkO51f2eeSVCC3DwLsDpgv-XyWf3IZY7BdR23ApQNwA9DvfyjtZhe69fkR5Ta7C9BOYU-K0IT91uueZN2snx_Hk3PNMD8kpiWnrkc6d1kViMouM7GGS3pvnBQ0n83Rhb44HRLRtC402VKrVUwAQibA6TuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه D در پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95996" target="_blank">📅 07:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aO4mFXbaj49toZU1wQCDQXkXI3iKyALD1t6MzuPr_fFDejBCBm_zWRw5xAx171rXwTkcwyOtd3mpu-yA5mFGmZ6FcUVfffhDG5zqrcVBPrDY5EbaazEzOSqgNYbYmpX8gP5gO3edeBXzYeo1onlMUeBbk7vvqZflYHu9cJCk1UWiK1N3zGLR0JyuA-fNC38cU-F1yrOHq4d374btC_qqgzIc4hK0ZTyTGhXacHu9lY3-atNj3Atv6E6uYIrjhZsmch28T2F0ivu9aXJbK5WZyWCuzAhgvVI21G1rEQdu-JlgDCzZB8G3V0K2Sl5dQzBy6-Dunj32EDmBAuSUHmP-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95995" target="_blank">📅 07:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLAKEekG1-UDCNN7_5OySEr5OanzGgH52AmVlzj36ur1fy6iN9xxaimPm3CKsbgs7kn_ZhOoYef0hwPaoIYiWwADP-S4u-rURQuAHNrslSCm1oUuqhabmLaHtqRL1SQnQ4N4nj--nKRYAs4I3NATZtJC-IlZ5ToTrnD-ZGUvccdP9q_YevmM2tD52PuJEbIgq3zPsS5R9hvAlQsQnmObHM5ZVCrDxlSc4wSEJiv9XudJfSrzEP-cC-B08zzbWj85Cedsm_YoPPjaGZz71EZeoqeZhDvJia4uaam4C4WdXY2w7EMY5aiXP3O-cxPcE0cCS5WWGGQhL8e0-7kqd9j4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
تیم‌ملی ترکیه در آخرین بازی خود در جام‌جهانی مقابل آمریکا صدرنشین به برتری رسید و با کسب دو باخت و یک برد از مسابقات کنار رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/95994" target="_blank">📅 07:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی گروه D جام‌جهانی
🇺🇸
آمریکا
2️⃣
3️⃣
ترکیه
🇹🇷
🇦🇺
استرالیا
0️⃣
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/Futball180TV/95993" target="_blank">📅 07:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی گروه D جام‌جهانی
🇺🇸
آمریکا
2️⃣
3️⃣
ترکیه
🇹🇷
🇦🇺
استرالیا
0️⃣
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/Futball180TV/95992" target="_blank">📅 07:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwp5yQcxvxGigWKD1r4RDTDy_EAi2YvNLRcRj0O71OZE1a06BKZtG__w_BbY22kcOhrzwrStN4Hz-CZ6yqacHkmXfMBSM2VZpZf4asSaGIxeY3m_iLyC-iptOjiIpGF4rPlbjwW74e9RehZcPwdozS65I4YlyQgSPicKRPRyvu-2xc5sabkzLIPVAa9iVmnTE_ikO8NKkGxwsppqvi0_lAg4LedQ6zCdNALSCUiJaeTULxeQ8QBfEL6JHdcMDF6QTM9bed_pVJCZiQQGndWl2w5mQCVnDlTeI2CmGlGGr7DobPV11fJ7fo3vD-f8M5RAZVJeGHARaG8A_sCQuT8r7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت قاره آمریکا مقابل اروپا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/95991" target="_blank">📅 07:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8XdaNouNdGFUNnWJOWFx1E8brk7nkRzCST-5qMY6uq-rjsUNTevJhJz-ocBf-uPCOj9qPuDoZ1kDA4k57UY9EjamXxRlg8SCK0DjOpmSSO6pcismsIBaMXOtWTF_LSOlKoKRq3VsqgrN5Yu6sQNQDHt5kr1gUiusRFm0SGown8PReq6zK6hDzeWRmt7l79Yi4rlhZx4YC1ph6ZPtacvWHqMUf99TUngkJSa5VjIzy10folEn7U-zXDqeK6lxWMMOLUleyRgGprtGOmn1kSj3gv_2gT1dQ9wvAYqP4oR2lNXbMtn0QbHjuYxw2rzbXPvHfd_mSwp2GoASye_zxx1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا رو ببین خدا وکیلی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95990" target="_blank">📅 07:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a795f9561.mp4?token=ergp4jr8keX_se8i3bl-I5WTxbNnMN03FRPbMFBJ0gz6oSG97vIncp-fFXZ3j-dF3eI0eWwhbdjnwgl3quurSJ7lnBpDe9spHWCt15x3fueRZ2r0Ox3-abPHMuXz2XM40ZZiL-e0gsDYMfTV1_ajjc7aiqaqv4ZU4aB7Ehq8Vtqr2W0WKdRlcGG_1Tv1Epx_2MNTsDiJ8XWyIHBdczs_cWzxQEZQUnYoOaiv1N4u4GptraIB2CjedOqbgHHkW__yGG-2oUjyt3pTU6K-TGu79ZYm0e6v_4mCY0H0uOHlvR0OZEwhKK4rphiY9B2O5vvfQmS5WRqGn0jNlBeNEPBDcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a795f9561.mp4?token=ergp4jr8keX_se8i3bl-I5WTxbNnMN03FRPbMFBJ0gz6oSG97vIncp-fFXZ3j-dF3eI0eWwhbdjnwgl3quurSJ7lnBpDe9spHWCt15x3fueRZ2r0Ox3-abPHMuXz2XM40ZZiL-e0gsDYMfTV1_ajjc7aiqaqv4ZU4aB7Ehq8Vtqr2W0WKdRlcGG_1Tv1Epx_2MNTsDiJ8XWyIHBdczs_cWzxQEZQUnYoOaiv1N4u4GptraIB2CjedOqbgHHkW__yGG-2oUjyt3pTU6K-TGu79ZYm0e6v_4mCY0H0uOHlvR0OZEwhKK4rphiY9B2O5vvfQmS5WRqGn0jNlBeNEPBDcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر تقه آمریکا به ترکیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95989" target="_blank">📅 06:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چه فلک زده ایه ترکیه
😂
😂</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95988" target="_blank">📅 06:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95987" target="_blank">📅 06:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80336e0918.mp4?token=a7DCoQhM-CLeN1Ib8cNdq9rcbHARcFziKVFqMvFzXZHg3pDVNlLG6XUZWE0bZPDpUL8uQcAALvvzKH__3_QNJef2ITUT6KOPILkMygIi_W_itJrDVnxDMO5vYc-pg5ju3BMK0vsFysY1P4ackUnRy6p1T-lT8TdzFXl71e3EDC0a3t6bg-xkBAZFFeiLxy9ws5wJLFhVV5RhYP6x_pRH5K14lpBcQA2V8oxAZ2bFACQ0Oea8Rj7Ebo-sNurorr94zyaWmcA1SCyEAOSTAMbHxfbyBvmZ1ZcYVgHCCiEbOxWqmCzyD-NnjzyPzTB9btJdLWxmH-ZektHxkxOVEDP13A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80336e0918.mp4?token=a7DCoQhM-CLeN1Ib8cNdq9rcbHARcFziKVFqMvFzXZHg3pDVNlLG6XUZWE0bZPDpUL8uQcAALvvzKH__3_QNJef2ITUT6KOPILkMygIi_W_itJrDVnxDMO5vYc-pg5ju3BMK0vsFysY1P4ackUnRy6p1T-lT8TdzFXl71e3EDC0a3t6bg-xkBAZFFeiLxy9ws5wJLFhVV5RhYP6x_pRH5K14lpBcQA2V8oxAZ2bFACQ0Oea8Rj7Ebo-sNurorr94zyaWmcA1SCyEAOSTAMbHxfbyBvmZ1ZcYVgHCCiEbOxWqmCzyD-NnjzyPzTB9btJdLWxmH-ZektHxkxOVEDP13A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ترکیه به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95986" target="_blank">📅 06:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai9W8XEhBUV_SBeMMMZHY7JO0wUwjyNOrK9tyEUPqxGF3ZAKScmn3JynvREyNDV_FHx6D1phgMerRl11jd-UgqrzdQd8U4tWuGmK7SnftPgz-VL0KNwwqB1UvvfGMBm1TN274WEmFFakPRu4c45Pw49oLpC30U4DP1Q7ZAm4HD3bD6gHtPn-1GOcPTuhmSHbKzgJ0vCH1N93Rob4xdiGuy8DSRh4CXrlxK0lQiWm7SSF9fkSGKeYqyXVr41dCu1HqTb39ax9tQhftW09zrU1h_A1dzmn1cMlyXKzaNMWPtI8-m3FLxUB-OwYRX5Suf-iblX6excZ8n-xFXyc9F5d9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایلر دردن در حال تماشای بازی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/95985" target="_blank">📅 05:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=i6_ctgNSTqcZR4lS7VXpBIClDvYxvRQkraWhXXy8oJcUHio1Ud8IkXmA2_BFkhNR648DHGPFiOKUmFwemTNhHkPp2SfQcXA-IlvTzrece3C4IMLCDwKIBsJ4EZ52v2ZJLoTM-6GfKDZxZIDoq3_BBd37h1xVjRlMf6bvoGPYFPivoOfcOJNTC3nD19q8XqcT17DYEc2ddWqH7uzv8wkD51iaJl1iTH_4-njwg2xOFn0RpjU9sEf5FlvdCG_kzQMdQZCzSODkYEwV8POvLI1W0d5mNDTyxRY17CwS5OZUvpISitJO80WqVivMoPKWpK-5vGrG4rFarPQGKrK42EfTbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=i6_ctgNSTqcZR4lS7VXpBIClDvYxvRQkraWhXXy8oJcUHio1Ud8IkXmA2_BFkhNR648DHGPFiOKUmFwemTNhHkPp2SfQcXA-IlvTzrece3C4IMLCDwKIBsJ4EZ52v2ZJLoTM-6GfKDZxZIDoq3_BBd37h1xVjRlMf6bvoGPYFPivoOfcOJNTC3nD19q8XqcT17DYEc2ddWqH7uzv8wkD51iaJl1iTH_4-njwg2xOFn0RpjU9sEf5FlvdCG_kzQMdQZCzSODkYEwV8POvLI1W0d5mNDTyxRY17CwS5OZUvpISitJO80WqVivMoPKWpK-5vGrG4rFarPQGKrK42EfTbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/95984" target="_blank">📅 05:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=jyOVnuCm4hsFg4H-r4rOQFGEynPKyPICywP5-ALAIt-6JJT_bwXXLuZoQfGMc0bT6ckMcpAh--WkBAzSHHimVbMlnttNnrLHsPOoTuNQlfWenLv_UFBMAv7x-ZN_2YcdTpm-CsAZP25WjPr08JBKbb5D_Wd0zk8Se4F_n8TJRW39Xt6w1knx69APPBDY0v1-DJFPkK0bKKyrRZ0GPn2-6urLmUu3_LfUbDoFhv8iwCJn4H4rfYxLN-lCkgzP56vdkik-nPyttK6yneS6T7Jn2rVtqcE4w-J1Yg8kBfbhzmFhlfs8v4HdXok5qWS5oY21me-nFRspNLZUuQKYdNyp2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=jyOVnuCm4hsFg4H-r4rOQFGEynPKyPICywP5-ALAIt-6JJT_bwXXLuZoQfGMc0bT6ckMcpAh--WkBAzSHHimVbMlnttNnrLHsPOoTuNQlfWenLv_UFBMAv7x-ZN_2YcdTpm-CsAZP25WjPr08JBKbb5D_Wd0zk8Se4F_n8TJRW39Xt6w1knx69APPBDY0v1-DJFPkK0bKKyrRZ0GPn2-6urLmUu3_LfUbDoFhv8iwCJn4H4rfYxLN-lCkgzP56vdkik-nPyttK6yneS6T7Jn2rVtqcE4w-J1Yg8kBfbhzmFhlfs8v4HdXok5qWS5oY21me-nFRspNLZUuQKYdNyp2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/95983" target="_blank">📅 05:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPuA71DilijM7caK2jMeZX_eybS_ceiSV9PGKGBgC2C84-7YiwcXzasI7DQfOmEa_krC7ja8iJ8ZzlNt2yUypFbX-xY3NDbScNZrBsxHvLlNLOnvgt0m9oT2CdpEPLdJiOya_vqN2e3ptWD_t7xIeGrP408ExaYOOX0eUZRvUzZtDb63nuttFOUfFsFDG57GSuA9CzIArosSLxqoOTMH8GKrjjG7-2EF-To5lOJg13i3Ze3XH1Q1SyX5xDMfEW9xxGRwmkLZ7BxR7eVDMW1NBETJTdoN4vxNfnxtXQcVHgqsyeWi2Y1S720fTPoq3GMJ0IdY9qfSOqJ3xvMrxTNcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
جدول فعلی برترین تیم‌های سوم مرحله گروهی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95982" target="_blank">📅 05:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0ZoaUZEOppC9RqnFr4uQHTIUUOgW0zG4AczsNVV_Tr1bsMUMTPr-390SHLYRjfAOmATi4WxawFbPEWovPgs09AYGVj9HPVb09kVO9NLn-xqAkTSwgUqohqgguNpZPyoc0BcGy88-zVzBjReY-RneTx8RdnKQRkEOn5UGUh1wVfK7bCB32Nlugt8MPyJOpvErF93ZL8oB3QqRK2VjmMbse6Q97sqPWIdwfArVIS378txlIucECq_Nfks9H-mTOQlY0_eEiTGGC91h1PTY7ZPfhHcN42M9kuv73LBUllD-SaoF_jhF_zerNlblvI7KqQfIB0U9pxn8O1weW-iT85qIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین حضور تیم‌های آسیایی در مرحله حذفی جام جهانی:
5 بار —  ژاپن
4 بار —  کره جنوبی
3 بار —  استرالیا
1 بار —  عربستان سعودی
1 بار —  کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/95981" target="_blank">📅 05:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBAz1WH_eaXPMBhuOA1CQpCnDDLN1S8Fstr1rchFCfYu3KJgutXJ71ckSN0AfD5jTcGmFY2pbPB7wiN6LW1daNH-uU23tlYcY2cqwB-F9VsXj_I9dvxKTp4lhYdvZFoecm1I_c2oryxGzw7cm3pOxXnPoITf0a-Tx6CVY9aRzJ9vAykIJEuPFVcj_z55EtLzG4iz0eDK3hnxa8_td6qZyjrQU2BXfEyhBy9qptMZGizLCl6hAxikiwobWnUkdV-cMk-Ebxrv9-RTaGvU1a97ZkZwo110_Bz4Ta1DPJrxugMckYRsFOcirJj8upffcdMlfr8uW1dLx4A00Udqu0q_7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
بازیکنان رئال مادرید با 9 گل‌زده بیشترین گل را بین دیگر باشگاه های جهان در جام جهانی ۲۰۲۶ زده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/95980" target="_blank">📅 04:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf6SP-vwOCUzDQUeTSsegrB1dSpcm1TBE5LqvodfIqqsg_E7RuBioVle_kynm_KQLrfbLDY87gvu-wDrh-R937-UNLvOCQlSfiwAIZwe88Sjd6CfO4LYdMtg_m13ky8Dt8slVTnFFkVStRO0hE4wchdEHhk19WwhQzcvKVFd0glEyu4lWt9dDCh0SF-6b525LaC2xHHpLU7IDGaMHfqrGIggKbQuUyVcHU4Uw8_ow5kfD_N8flyF22UJHvwXlBFOyvCcIJcwB-Tcsn7BpQidwiVs2cvuCvbCWLhIdbLzqNU_E1C1EtJSit-hmxtFS6U3TLWlSZaF5nKmQMgsl_WKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95979" target="_blank">📅 04:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIwf_GUG3qU0OybCOgUdSylyC0_6qbFmNfqzkPv6T2op2vNCJwXAgIul5MVCCTQcosf4Z6qz79BHy1jEWSZyljm3wixvdlrc3rco-TEB_3ySXA18_9yiAutN8-WZ2RhEwpgSVbcy-NaNSNWljExXjshU53zXiXM8E78qA1csWfseuSxS_ADGLHBfQYXEeDhY16fgwMZTHLh5R07KN_ZKpITkGbRmtBcz-PUElElkeLiW5Mk4ZU6FmKe3kjPXrf7OGZrbxZoEOMMdo_2jkb7mEQHxBWj4n-TJktTH4C-jN-6_ij_i4UHOWfOBWlo4Hx8GXoJgOUsaQ4zPZA01WwweMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/95978" target="_blank">📅 04:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETeBojntr2W4s-MoerO-VRiCFspN6LV_EpZWXujSOcRltTV-I76b_4BErdvLBbnwHXK6voCS95jvc48thwlFMgcI8xpC0BJ59OsweIqG_SpMDs33WGalV8J9uIGJk2ELAJgPntdsVl9YPHFvPwbxxLIMsd4ybBr142OoTs6CUf-33ZLnI90_wcsojS5fXdFgmbl18QAbGBUfQEVfVit6gLwsrZJtokumzICnk7k3YF210RyrWCCIK0c2quGsi4i1WyYt-GCoNThoba9GRBq5FMGv3Pni8A4Wt2rlQPYcNnTaPEg4H0A9rXBfSYkrb_63U-_ldYgopdOpkjn1AqCiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سوئد دست در دست هلند و ژاپن صعود کرد!
🇸🇪
سوئد 1 -
🇯🇵
ژاپن 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95977" target="_blank">📅 04:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESAYOHAvaeaQxXfjNLqpdkOfWF2KBdp7HTOnvkcoJjtFZ7nJXTbkX_lGP-m0n0V1EjTJxkpoWBeGuzCDf3UdPEBFSw_FCXpOzm_FnGApYFQJKuhmoEbH11E6FD-6LSkevoU9rGyAEsh9FDyqQKfOd0Ja0f7rPAt1VJ6hGEZqyqzCfPHqD7zjUQQhi9AUVFp96H2_x-ReUALLU78yoqBIyHB2_Pwqhr2dkb0_f3_PavgYWcEQEIV8CObh92570sPROoKBRdXPYtKmPMc2C4MQ2Z5608UEdqcohzz61zJRgwH5mFpAYsxxS6VwTiNeLyyeEjyxZXjXlQBurd0_LfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | زیبا مثل لاله‌های نارنجی؛ تیم کومان احتمالا حرف‌های مهمی برای گفتن دارد
.
🇳🇱
هلند 3 -
🇹🇳
تونس 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/95976" target="_blank">📅 04:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95974">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qj6x6myutTPxWVBSBgZh9Wh70ZvFibGkFyrESTCHfpbNRu5Comuper4j9F9RZw31NhKVZ0wpSudHgtZzQfc1uLWWW09ss8RcWmEoTOF-jpqXk_7dnEg5Dje3OhzwOVXnhjpEUkReXgHO5t-T0mPLTbJMQYt1gLA7GDnPTpHkG_4bZfJ_GlJq2VWF6vJSI_sEugD2AjzAzTDiCPZH6qgpw5hRpCOd3X08-N_W7n0RNUXGrOJvx5Nt5uKEcxJEsaEU-gNTWe4nVO5iGvIvI2IqYUyG-lfJDJR_g4YMFbwqb7qDoV9F73yTmGhhaRkYwvUwppSf1wbw5H8W-G_QnaQlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v95LBZwOIg8gaoT18ayJZwYLEtRZZUV-bx0hvdClwzW6UGKlVUARvyYpIbq1dXcBsPvkaEulbNjiDyoqlRJrydtzh89b_mJHvE6P5wUlhmEpcrJMfrp2BE662GzrvhtR7VTu9-K-tXWuTJ1-UPzt4lhC2qXx2At1xe2VwOgZ3pxxZCxqYjJR6ia5TwZxaZfy6kHrOWh-vKQILB8g8iJfKPBcogbqF8KyV1RDK4ZDyF8oTax70JW14Vh0n5OyRvsGXOwrEOf1mgSuZTUI6NuZ8LuFYCI40AGacjtuF4vHCUHb8dKn-bUxuYkM12lX2hD6X-Q6Lo1LjHxSUKVclSFMgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
🇺🇸
ترکیب رسمی ترکیه و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/95974" target="_blank">📅 04:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlhUr0uCV-BCfDsqn_1-w3nXp4HPE47Lp3Njqcg4tkgp9PiOceom2ghxSeLKFgh43VNNWkoGIDIAqHBJG3w3dgmH9KxFIBYd3j8Jmx_YJuD-jrukE61fzNVm53gSjnNSA_Ur6c9Q4MMe3qRZ2zpbaOC2DDYXZ9On6UNkyHdvozvHRECJKZyxNoJQxhu_BY2fK7gDn-dbITVNxFyV3pE-ljIo2r7vcoBwSXjDub5ZBqhWvshW5LfumA6UiNnYdqxW-h98dBZKBUSlFxN0Hc9Tey9cUYyey2LJuY7HvYSM4asqKcrLfXaT4PDBEuzS2_Fwm7mVxt98SPmmwOVkR9EDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpwZHb-202GkVKsKs3pNhLUXfQZZU1HKvwI4uNfx2OoZGRNVOaez9wERUobCCXQMfapDvMu8Lr8WSwRboEDh-Mrwq2NdhRDOldtLWehPLuEkK414c8Hh2aUXjlhBaJ55cAO_dH1bX8HQBO384b1YB9rsyhwP_WiItifTfCRpLR4nT88xBRMWWLSRu3ZBPj_cyGhPFThZHwSFfV9MCPf63blO2L5n4B1tFwUKnTqFWugUdsDmu6_HyHDh3-coDcbtavGtejECoGug-m1MB5xCxU4a_qr1fVNe3ZLWr4PKijbzKtE3Rx9B7mKUJTeKpzLOrfiCGBJ9w3ckD0IVgtO_oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇺
🇵🇾
ترکیب رسمی پاراگوئه و استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/95972" target="_blank">📅 04:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b281416ebf.mp4?token=RWhmLE4rhfJHv8XbheTqOWQLh5YTNZzzSkttz6OAHdjIy5CTz9G0JTfruqS35aBOueAk8lwzWdNYPFDaADsE-Bh-qr__c32P0WvUWwjicTtZZ6mX2E39r7WbkL8HLvYeDD-H5mtzxq5mYJbJkM3MyxBMyo0fqnCIXL_M3sK9l-3I8nciC3qe9H5kxxDyKf-JPYJhSGHA9-VsgxnfrCLh-LGKCN1CvPZXNwf6uDKMWX2X_lYYLPoudiXzGH_lReFj-hBZ1vCrNYhtNJ4amjlvk3dmnUp9b3FVnU94_vJifZ1Ko1U0sAetTekj-v9VXxJqZupKjwBhS7mmpmhjAu1a8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b281416ebf.mp4?token=RWhmLE4rhfJHv8XbheTqOWQLh5YTNZzzSkttz6OAHdjIy5CTz9G0JTfruqS35aBOueAk8lwzWdNYPFDaADsE-Bh-qr__c32P0WvUWwjicTtZZ6mX2E39r7WbkL8HLvYeDD-H5mtzxq5mYJbJkM3MyxBMyo0fqnCIXL_M3sK9l-3I8nciC3qe9H5kxxDyKf-JPYJhSGHA9-VsgxnfrCLh-LGKCN1CvPZXNwf6uDKMWX2X_lYYLPoudiXzGH_lReFj-hBZ1vCrNYhtNJ4amjlvk3dmnUp9b3FVnU94_vJifZ1Ko1U0sAetTekj-v9VXxJqZupKjwBhS7mmpmhjAu1a8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللللل اول تونس به هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/95971" target="_blank">📅 04:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac282eb0c.mp4?token=TpNfaX-VswD3t8AHOqtvc-XqcQV2-BchAnR5NkDml6xmPhCtCgix_4Vp02-xsskO-4bKhz8UhW7IMIMmr2eP9cihqX4cDBTVB4LDWODqlbSnZJzRF7K5S0CVHXGBZvA_10GFXAX1iPXpDPo-7NRHPMhA2SeM4xANEgDrA741dQZRvjaY2GE3qdah4K0YbX18EDcIP0ppYvr4sTdXgI7T3b2XuEgKIFR2DNIiUSWWpTYz44vRcefVozWYPftGnmMF00BZQKLXu4uzBvSJmjxnSsvUFvhnmhyrytwJ9w1nBCo_Lpq9VlgAp_vmJos0fFdVilAB1Niu7XoUeHkP1-bH2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac282eb0c.mp4?token=TpNfaX-VswD3t8AHOqtvc-XqcQV2-BchAnR5NkDml6xmPhCtCgix_4Vp02-xsskO-4bKhz8UhW7IMIMmr2eP9cihqX4cDBTVB4LDWODqlbSnZJzRF7K5S0CVHXGBZvA_10GFXAX1iPXpDPo-7NRHPMhA2SeM4xANEgDrA741dQZRvjaY2GE3qdah4K0YbX18EDcIP0ppYvr4sTdXgI7T3b2XuEgKIFR2DNIiUSWWpTYz44vRcefVozWYPftGnmMF00BZQKLXu4uzBvSJmjxnSsvUFvhnmhyrytwJ9w1nBCo_Lpq9VlgAp_vmJos0fFdVilAB1Niu7XoUeHkP1-bH2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
🇳🇱
هلند 2 -
🇹🇳
تونس 0
🇯🇵
ژاپن 0 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/95970" target="_blank">📅 04:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nup9UzP5pUqP7Bi1Sn3F2vxAJSl7sQiQlgMo6oGCrNHlnR5tVMotz27gGg1ouTCC03c18WhGIDreA46gtzhM9BJkP2iij9R0Eqm80R346ivP3i0cN_9ZkH-CFiNSQGbQksNS75PvXBRNNdFBkls_BmoN0iRJTcywGln74i50u5hCyTtCHeZBMss3AdP6yUG0F0lxbNId-0bnsaAo1gSvCf5YA-RvUT-FoYPouosIIZ26ktUnGxKDtWWofzpnJ5uRTgXV0-QbDXw9tZVhTToJZ6Oh0oI-OiRmf-g_mGOwLt8w716jXenHfWGoA7KL72X-ZvVLGaS57Vze9w35oF8KVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cP8GT97xwdwfXz673bFxa5Sij3NbDL-Al8LPSd6_CO6bWdmEjbKHV1owAIMvmlYl_Ggge7-rL0bl62WR3o94PevjYhyMm-uFB4Uytdf2Ashz4fvDVU3DhDSFWxNptD7PlLmxjv6xuWmQB2sRlaM--GaJTrc9MiQQbxNYERXUGhvWTHC4dhdjqj9uRTePzffusw13idD3Gj1M3m6Mbx_nbTs1lRjEpjL6KHUe0a7HYcpF_cQGQXEDaHUJl8rr0_GRAm7BNTus2-HBs4-zf-G1zRA86bgj6HzHhyqzXC3eD5cSUkzouQKnT8xjUdqMcJK_n7_29vu9hj9gjUyJd4IuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXKubBtRIPwtIqqZuPuFJMhnH7GdFj3y9OoQs56QGh_nDozc6VO3FDLeTmCOoYyfCkNth5NVXoWR5wjjWqFsmfvSTDIz48wsDT6Yky8Kqzx4iv9D86T__uLYYPre2Up6Ekp7CgY_ekKnqhGMgOcX1N5FkwbLh-OxvWHPcHcaVJDywOL9-Kadwx7aiXCVq9bPqna0tG0szFVEbLRamupjqJkYBi6fNgIa8gbeVScsRjVqTpHHmKwSbuWD4nMaHUh0mtG2uGSx74aZP15Ty7vfpvm991NAjHjwQvHm4dx22YmAKfGOk7BZpTlDkIV1_LXrxV9L_HSdKzWP3t_NwTc1hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKwLqvuHiKuxmGqH59C9Vfp3xyGC-D491KeFFVE6XSMAHrwKHjDa9SP-jcMecyoifL8PEPk6RFY9LGfSlPDKqqFqS___6_6RJOMSuUsRigUW7B1P14ijX5qoqyb3MXHxWLnVjUq1f_9k1EB_hbBnLUB9TbcH3NHx1GAOTypDZdjkgoEqhDXTru7Zwh4dFt7BcR7Sfs9Y74-kwFzg1OKktTHewZs4F0rnMSbx5VW_kMzovpJMvfb1fFbp-QQWI0jqP05e919Q9enmZgy_DBkzrPFv8qq1WZTp7j1FptsRo6XFJomAvo4YTeWghRpPiyVDpHWRGVP9QvZznFImB-mVdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اندریک برای احترام به زیدی تو بازیای جام‌جهانی یه چسب زخم دور انگشتش میپیچه تا نماد حلقه ازدواج باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95966" target="_blank">📅 03:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پایان نیمه اول بازیهای همزمان
🇳🇱
هلند 2 -
🇹🇳
تونس 0
🇯🇵
ژاپن 0 -
🇸🇪
سوئد 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/95965" target="_blank">📅 03:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPxmfdi2HUR2Fal1Nn4v0XUlCLPLvlKbIpD7FYZcACMD6PQfEEIxg8wQy9K-bTNHNWUjdGwjWtVymAijqOiEJx5M1M-KSi_NIMimTLNGof9TrnwV-7uaiFCapJCs_OeUfeWHyxhoh3kW-2RhqnZSHE2OSVFdODlPPmuGNcylQre79W91VSduL4WFsZj2IK_VzkwnQ7ePZBGiTPpn3Fnn6kvKthMfzrq65kZgzkaPW9nuQU0s1vrn_Y8tA5Ujsl8WfUHPyTyCHm22M0oPp0kI9WmN-B4JwTLCQ3FrHxna30bct49kYzAHkolxlO5Mfinsdz9xeajuhvWTrPHvp-YZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبه برزیل تو گروه خودش در جام جهانی تو 44 سال اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/95964" target="_blank">📅 03:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1CpA5azl7as-Vuv4DuuQ2-kWxS0aws96XA2vpDP2_fxw7PnWmQAozQR-FyjMrPyVN23Qbag5Zz_jspqOzs9SgL6nDYOcP1hJPo3lBNIMylQf2Lgoa0NLGMCXSJZL-nd3tXUEiPv0crlIod4wADYgGM-l9n4m3vbZIB45TLvh04XM1i9HeW9c8VRWMIm4R-TLgxJPVU0x3lAqa9W4ySJLk-qgXyj3wqi7fGgwjbz35ZuNes0HfgH-MylEthmhz3JnglyeJzexmLrqJXeuqeF5f_9_XDjZGUrAC1p2n0CGAdkiw4GBYNbMK4VFc37Es32xsr7Chxm11EeBw5eigPb0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم طرفدار کدوم تیمه ولی نباید از دستش بدید
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95963" target="_blank">📅 02:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a48b42c7dc.mp4?token=id-IVacWSOvR8NT34LcATQGLJzmY5fMSlPshsq8zkJv1vi1MbdIEyEVBznlkcalHHs7ZO4PIYUBUjmUdsBJ9Xczl7vw_VnV5zz55W5RWPdqH3IrAimRUtn4JvC1cS0dDlE73nYyQCbi2n-tgcOG-F1x-lTsqvclaO7ek0VyULBuA2f-coGn63bAs8lxWO0OGn3iIKsSGmi7uMk91iCiawdZD8WL2r3KAmroFk1wZE8io8d_O7OTAU2ZGYOQZqhrMcHMAXeDTnMNqHtVR0YqNURc60F4zF04-EOwhJNgy5et0gF8I7bGqPvYcO7t7o9MgoUEu9ZNZ3WVFAsM_KiyWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a48b42c7dc.mp4?token=id-IVacWSOvR8NT34LcATQGLJzmY5fMSlPshsq8zkJv1vi1MbdIEyEVBznlkcalHHs7ZO4PIYUBUjmUdsBJ9Xczl7vw_VnV5zz55W5RWPdqH3IrAimRUtn4JvC1cS0dDlE73nYyQCbi2n-tgcOG-F1x-lTsqvclaO7ek0VyULBuA2f-coGn63bAs8lxWO0OGn3iIKsSGmi7uMk91iCiawdZD8WL2r3KAmroFk1wZE8io8d_O7OTAU2ZGYOQZqhrMcHMAXeDTnMNqHtVR0YqNURc60F4zF04-EOwhJNgy5et0gF8I7bGqPvYcO7t7o9MgoUEu9ZNZ3WVFAsM_KiyWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم هلند به تونس توسط بروبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95962" target="_blank">📅 02:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOvUIKO_U99IDN2EKTXblyKC5ai3vl1XiETfeKQ1EzFadGLkqqBZs9vFkJTbIVxlYreqABmMbdx3yL5HQrz0fiZY8jR9TbhNR87dzQhbPIscdX3vWm0Oq9VjIWUmGRe-27b0GPyyjFZvHDPKfqOosUCsHbWTSagbQocpK9_ujk9VtIuZU_hY0o2mO3l4OfPeAo3tAOnFSIUwXcEVs3gtTesKuTNtlMuMMuNM64sCu5S4wCy7z4pTNjsLAIOBfbFPHsaP5pmBCWqQKYRqHxcfap0_q56m-BflSOV7d3cTQHl4YKeXO7Yf2U-V-fDKZa0cTF9E183Bu4kbp_gaRt7aZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای ژاپن تو استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95961" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf81f3272d.mp4?token=QL6J0hsG0u1FMGCZX6pvZ2ALQscf9NhzCVEu_t7p7bmwJPKJmz2YS_QVdCaOIkojIzT3yz7gPSAKRDYaFqZ23QFYhyoCBgjBX8M0gdkXiAmrIOV9ZjeB9xeZWLmKCSSH_wwecqpFzj1wDYRRmCnM6Vrx6rRJX_sN4dSdYvmV0CacrTpSoOCqeMrwVu9h4xuivKBnE937-IciB62f4YS4__anA9vZVe6v8PBgqkAJbZ9jxSYdDIpW1Ba9y2MFuEoTxiwa58MjzsWpOmCTtqxgI4qKXJfVVrlOnbuyrqkGcXCKA2yrTtlPK9s-TuipvccqO2tD7qYO1-3tzQZl1VRY2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf81f3272d.mp4?token=QL6J0hsG0u1FMGCZX6pvZ2ALQscf9NhzCVEu_t7p7bmwJPKJmz2YS_QVdCaOIkojIzT3yz7gPSAKRDYaFqZ23QFYhyoCBgjBX8M0gdkXiAmrIOV9ZjeB9xeZWLmKCSSH_wwecqpFzj1wDYRRmCnM6Vrx6rRJX_sN4dSdYvmV0CacrTpSoOCqeMrwVu9h4xuivKBnE937-IciB62f4YS4__anA9vZVe6v8PBgqkAJbZ9jxSYdDIpW1Ba9y2MFuEoTxiwa58MjzsWpOmCTtqxgI4qKXJfVVrlOnbuyrqkGcXCKA2yrTtlPK9s-TuipvccqO2tD7qYO1-3tzQZl1VRY2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول هلند به تونس توسط اسخیری (گل‌به‌خودی)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95960" target="_blank">📅 02:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95959">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هلند دومی هم زد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95959" target="_blank">📅 02:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95958">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هلند دقیقه 2 زد</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95958" target="_blank">📅 02:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95957">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های برتر سوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/95957" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95956">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2dYvUBrYKjo-EOB5P2adZOwgBkBTYiVG4fUtDJW53Zp7fuk-P3SyDC25pYIgbu1JAdA1MUO5IWeEspQzgDuq_fv3Hm8QWKoVm8DdQZHNvH68I19BBRo8CuirJZia5xlI9vCLTIhaJhw-zwPSiVp4_4dPJ3r0sEpA_z_j_jDcWU7CTu3TfdIJrwOYKN_jJUoVpIzYiZQ6h-uk2zi-0PQ09bsbTeu2fyODmfMKF6CoHrCQZBXc1aink6ZaMZHk9JTSLqKxk40ToiihCVy_qruF3S8YMi6ruR3xCsLA5xRZqsnGchsOThDa4XW5KvpSapFupkEC2u1jT-psrCMYinsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های برتر سوم جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/95956" target="_blank">📅 02:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95955">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZcHGxjIRhjIHbU2kk8yV3MuzH1-CUCbjZepS6pAv8vc9OqPN2dJF-JWFeLqAcV1BnrabhdYq-i__jML4UubjxZqfXWJeF886mhPwF3wlUzmwRJ4kmMp0LmpqYac_hI1UvBUBkne3_mdMuts0iNuVZPWVhDaVAxN9RymKgLz_y3BpqwjkbV1AJRHnTbSpwEe6_LXpLJY9xqVFebEhHfrEwNAeLYxBEQ1rGr6HJ9s9L3kvSJGv5gMvHc4ri1Oj5SguoKA5WD9vt4Zb55BadN639AZ_Q0WeV2h51usn2H5FQtG7Uh4I_DyBQbZYVbXnzoydK33WITCFC7X-GciRwPoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌های که تاکنون صعودشان به مرحله بعدی رقابت‌ها قطعی شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95955" target="_blank">📅 01:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95953">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hRvhlcB_rMoFmHhbArtcYI7hOi4ziHk5K2H_2LhbuyYTK3GS6kFbJJJDonKOI2Azdgs6G8ipI_eKFDeoArhP3vUcRc3DUcHhNh68O7jJqTuyMqi7oIcLc6A1C1qGbvTl15jQRPbTKF_N4YLQYV2lRoOxpuDFi2ekXXXZtgSOpyH8oIOt7d_iPdV-L-mJ6svAYs-_PYzBy7vksdnQDo0786o_1c8rc3dlECoK0wpFd7VhHfAoDZupSiIIbvbBiO46RNyIQ2mhI_c5mAi9-2Db0dnAVHX6k92NQUucGTMq6WoiF-l9QfXwLk4HaGIxSgBoN4YCI5AovSddHshYwOyxcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3ph3cwU7Zec8oleEvhtnPpN7jRtG4PLLuXMJ5hJZd-WuCk-1n7GzMoXagxQdstNB356HAvni12IpZnM7PhZqdFh5zPNpeJkkDFavK9AGFs_mG8sJsClkAOiUHhCjiCpn_UokzRVvU9DnkPuamedvWFjwwzde7p8TiKIow-I45AanTtPr7YwoshhNXMG4X7ZfQjo29740YoI7uTylFrt_KfXUEIKxsppvDeEcRHCN_H4ZgssxYquSwh6bq4MPmCLQsb05oOX2Kr3kuDqM41mXsy2Syl_1Lzya7rTSKSOTdmfeGIvDcX8vyJ7TVvHGw5YKOqlxrfYkWKrhrS9JOM09Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇹🇳
🇳🇱
ترکیب دو تیم تونس و هلند
ساعت ۰۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95953" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95952">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYtdGlLw0bb2r6lETtmYf4ckSH8nn7ZFD6bKYNTSj_F-J1SR1d_vM1i9cB_rVdx5WEthXvL-Lpio55WtUqZxtaMffdHZIJrPtXgqFbtHVcxoVPeB2tsnuhlNVzWB3P2ualYaOWTGMmLxrXdJsdcFIg4Bi9FirAZj7pFGnhPk12zF2KqHVDA9QSCow0DtfPsZHa-J5rmaQ3EBnLeK2verKT5pCX4Y0f4VLXM0cMICRXW_O-BwSFer69xeQXjYrDOkyDnavOTZ9MuwykBrO_bC87eFi4Rz0kn5dn5PFLAnBIBYAOy4XHHsvRGSYvvc_T-ngPm2ox7PzOPw9d3pZYZ6GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
تیم ملی ساحل عاج برای اولین بار در تاریخ خود در یک دوره جام جهانی به دو پیروزی دست یافت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95952" target="_blank">📅 01:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95951">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOo5VuzO2AEY68NzQA61b6lI16Kb5nnxNnFDYo8UxE0Y62TUUycUx0mM2oLg-tiWwO863Vnml8j4CY9bo1l-4bv3h5Dhhn86dIEWPu8E0DmVPmIXw6-Yw17JjcasSv25-CHDY5qAxkTtTzyw_1j6EfMrUrksMGnJh8AwA2NOiECrH3TX_qf5Ge7l8h8nPlKTzrBYEWJ3KiZ22OHgp8h7QRA-7DrrrtlWqvOgfSdEOHdxqtBRakfk7OO7DfbJUeLGRunrCJuAhK5shos5UvYoVKOV2bMvntCU_GWdxALtBJk8MTR5k5vqOu59CBVCdan_4wKFoKCfjhjj_oq9WO2MTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مانوئل نویر در 9 بازی متوالی در جام جهانی گل دریافت کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95951" target="_blank">📅 01:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95950">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UINVvF-Zyx2taY8gXx9Fl_jcUJ_3rkWVDjGIziheqCJPT4471KOCvcOy7d8Po4j1tTIRUoUCv9VNOQL6VyN2rN4F2Yry9bOqVS3zugExTFIqv0KBYJu1ptVZDLUX-k1Hj-U5Lw-qo-2Op6-JXnljyFeropKYfRjSTJby2C5j0kgdE-GFzMW6LgkeSHrWsu6jgL4zsOWjL3Tbzawpwyv46jf8l9cJei4nmJv_YNzueCZ-Un33r6H-jN-oOSkTaHsdSei74rSyK1wZrD9xt6KRD4kF661sV3JWRtjRSLdBzMJKs0WVlPdrRE0X4IxoCP3MoBAZAL7PEXWRID6mZNJJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇮
🚨
🔥
🏆
یان دیوماندی تنها بازیکن این قرن است که در سه بازی اول خود در جام جهانی به دو دستاورد زیر رسیده است:
💥
بیش از ۱۰ دریبل کامل
💥
ایجاد بیش از ۱۰ موقعیت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95950" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95949">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95949" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95948">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEhPuDlRsS5gDOQcV-0qYzNjr2h6qE0s5LwzvWRxdKjSTIuzC8kPCaBm3YPE-p3b4UnI3X3rcTj5LjgjbWg8lkZroA-sAQdWPzBWShivND26woXyK5b23wv7QP5FuOdpDfLVeUj_8sMG4aVLMUEKtGEge6MyJz0TG0VkDHEANpvtkZ1g6RVC9gHqAMgCl92xBl5RChC2jUpHkPkrKw76ogeCGZfaV-CGUp-DgT2tYWFXptVvWe5v5lEY0cCmUWs9QfAbhmm_LZX5xcnRN7pQw288w2PV1YYjlCJieBnMFYrdI_-t0PxH-53XiWOvSEtMnvZG8VQ6SniXlTI2n56yIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95948" target="_blank">📅 01:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd2WukgEDCW7Tb8MI6Rd4uPkYsAFHHX0WcbLlGx4QzPBYd4A6HS1IzKxKyU3iCK7o0a1LzRMxPrfvsNkERg9hVSVoCSdvzXi0ajrkCKxYWICztFtgykUiU54wfOdzze4P6NXZOIlnhJRqZ_-2HvS7IKD8EZ5xG4Ty5oNGUh678Bpj0GRoUCrA6lg4u_5KB9lGceKph_kbSEDDPyfhn55Kt5NzPXIr9BaF08qD3c5KLK5SOl9NP_zbDLZ9A8bSqnwpDKvlzD1iKIckrae_W2SavxNiNDJ8SbN-zJm7dYmVUH-6fngEMpx91bgYEMAJSqIDU3D3-gpdorwxK0sEwfF9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
❌
تیم‌هایی که بیشترین باخت را در تاریخ جام جهانی داشته‌اند:
‏
🇲🇽
مکزیک — ۳۱ باخت
‏
🇩🇪
آلمان — ۲۵ باخت
‏
🇦🇷
آرژانتین — ۲۴ باخت
‏
🇧🇷
برزیل — ۲۱ باخت
‏ ‏
🇪🇸
اسپانیا — ۱۹ باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95946" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جام جهانی 2026 با حضور 3,605,357 هوادار، به بزرگترین جام جهانی تاریخ تبدیل شد، البته که هنوز تو مرحله گروهی هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95945" target="_blank">📅 01:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNBsAwnURBEvj7_kEaSkTmBWDKwLtxUqYGJ-2ntLOBYND4UisI5RGwAkC3zQ8hNGnkXt9bhyb0lbkxQjmB_-Qgsqv04ZfMjL_-8eDzgnuZTWitucCx2BYun_v1lqRQE20BuzZL-o-z6euxu1o1ntHEud7exmv4OTGmLZsqSl8TX0zhQFXUQckOaVQOt6E1NnOsnldaIfDoM2ZpcN5jBId4ZOxwDFiuBAmx1WhQYYhJrYVLeqq4BiRwwlpb3mDF0NvDZUFcHt1wwexmhcCtQKo47giPNYZbWN3mWWwN_ISDdXudB6Sej_USMp6uqkShj-GAqw1l7IXIE31a5YIip-bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی اکوادور بعد گل تیمش رفت با زنش لب گرفت
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95944" target="_blank">📅 01:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95943">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVzDFrTA_kkvIWgEJj_Oj_-AXGOdwYoBBpcrYzmSCrTj7b8w-JyDjl5HFWODNmJSqDNeLEOIJvn_cb1_eaT70n_8GoDUttTzx20XJh5M2w_G2egwvnxdvmcNAZIEFSHGrZ4mfdHynSfGAmKygzWiu-NIy2H1x0JTyVoCgTppPhb7SzvmS0aTKe8eMUeaYpE8YPuC3gOmJ6puqeqdbmmrAwrTZL431hOuw5bO0mewNqUop6NCN4FohkAISLX6OdwBARwxv5Zg7FEXioTvOevnN6Irp0vZoAGqWTdBX96WTVOHSw90eSJjJv58UUyq9yuJNIchO4KzLK83P5imUEKbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه E جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95943" target="_blank">📅 01:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95942">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇨🇼
تیم ملی کوراسائو در مرحله گروهی با جام جهانی 2026 خداحافظی کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95942" target="_blank">📅 01:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95941">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpHUvhdhcKmOvyTihHpLe6vPmxZrIH0c1APbOoiQ2_a_jCn-WM09lKYvv84ldvv9hyPNq-ciTUZOaokhOx_tjAd9-DraBipf-josYj3dDIKWRgnzaiW-nRG_s7skETQWP4wqBfK4603AIWc5Jxz-O3ra_ERkhqHv9mnRtqtxei3KU5ex7uGPBnCG9M8b3TfBZkyjYX9w_oKAtqAttbOdOMpyzGLCHYWo8xYZJF4O6MW5_KXJYEXAoNHBc_VMlftR2xvHfIf0OOhKVAVpt2bwYXcbWCsCF3-8Ll8lD2NqMqSRojogyYSxECA38m3sHHYPbrIhkWtLvgmVwp82wD6IZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | رستگاری اکواردوری ها در هفته آخر و صعود به دور حذفی
🇩🇪
آلمان 1 -
🇪🇨
اکوادور 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/95941" target="_blank">📅 01:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95940">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🏆
پایان بازی | نیکولاس پپه امضای صعود ساحل عاج را نهایی کرد
🇨🇮
ساحل عاج 2 -
🇨🇼
کوراسائو 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/95940" target="_blank">📅 01:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95938">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ96U_816GH6kxS4QPj8MxHOuGmEFBpjnQOAnIORdWIYT1bIYkh8I0vxWzZKiq4jrN-cbV0BgqdrQp4ldKLIlcViqELWWaC7_rPvtXaFBGHiw0r4HwT1TIWxt_DNVFBmMfvp5Ax4LDtFihIdyTC1dHdNAd7yOyrBBTR5bfUIXYR2EhPZwfucogfFVdvGqCikyZGV_7sv34VD8u9TG5Ky0MvDeHWDf9oq8R1in61c7XW6L7ukNq2iHcNTT7sPYJ1f710PORUGdk4s2it6QxHyRRyXMAm3pA9DsjqKVAXT5MvhYNUyUX8b8s6GHf1X8dR0AZBhocSUQ3CxDnurE-tW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoImRXVP6oNQaNdhersYpwgTKxc--FT9Rz5mkeaD3xejTVEgptfelUVpzln5LKZMw-N80tshlddylQNKqDEb3hjkyVGp-IIFCYg0s406PxB34VEP07MiM7pQa940cwx9GcrlL1kDvHDqcD-qcdRdattaNepMIrKO59HuXRescP3-YKmLvP9DOsJJRwKMotRwxO8SkNguvTNqCB8bWAIboOx19bHySB1fqfABFVKvE3EyPhEviS5ev9aRlsglHsQsGZkuATgj7v3g3Azm67XjGIEAUHRMPz-LuUUZuVFjRr7nvN8iE6vxri5qmYbz4dAMsSzgE0vBzO4sZNLLMKVZcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
🇸🇪
ترکیب ژاپن و سوئد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95938" target="_blank">📅 01:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95937">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dbd9f7642.mp4?token=uqpDyXFv5ZbUI4QsZ6Z7O6ejft0GEpIzD08kHi5dUlWcOEE51sVtku_M1sZi5KtGMUwNvLjL8eMq7ztZWSs2gJAhE50mPZ3lIiW41Qc00MbXDzwyl9glL95X5j2unX3SAMAaJ9jrCwDg5qxvwdNbq3_ZgZbbmGPtM7NQcMaZoXN_r1wnSB9MtjS8SPq6wgd6cqpAp7pUWVapeyVu8xlnalYI8kTKTy82-zxbOPGor02aCXusHgEO2s49ZR6aOQk5HhkzwxyV0x2LjJVkiLwxE6suYXEbku7j4j7V1CWIGoOxoBM9EfbvT-2S75VIaqZtqU1xM9LehHSXGRPzmVhyLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dbd9f7642.mp4?token=uqpDyXFv5ZbUI4QsZ6Z7O6ejft0GEpIzD08kHi5dUlWcOEE51sVtku_M1sZi5KtGMUwNvLjL8eMq7ztZWSs2gJAhE50mPZ3lIiW41Qc00MbXDzwyl9glL95X5j2unX3SAMAaJ9jrCwDg5qxvwdNbq3_ZgZbbmGPtM7NQcMaZoXN_r1wnSB9MtjS8SPq6wgd6cqpAp7pUWVapeyVu8xlnalYI8kTKTy82-zxbOPGor02aCXusHgEO2s49ZR6aOQk5HhkzwxyV0x2LjJVkiLwxE6suYXEbku7j4j7V1CWIGoOxoBM9EfbvT-2S75VIaqZtqU1xM9LehHSXGRPzmVhyLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اکوادور به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95937" target="_blank">📅 01:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95936">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKXy3HgM1TB4_H2BmP5Ny25bOy5BQthk_GCJbsxyBGA2-dJqQU3ndWvYE0igybKSnIDnOcq3giVX7WcqaIzFFEgVs2w881Cuk9bxcMjIjFRyc5ZQVx7Sh3SJIYvxDLd738HXqn99MAaKd-Bc0T8dvnFOzfIESx6m3kCZ3beJ6LjUqxvZca3uqNbfWWDEoL935h4gS2JCjeUTMm6rnDlJ5kP7CIcmjy25BcG3EgBKt5F5fNkg3vykJvpg1ghvIIZFArxVirjYIxhK2dw63qDTRPxd9ouwlKQ-Vp4o0iWo1t1zFOfRlWCeqWHiJiIXDrSuCWbIXOyKSFshQWltiFaE1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مربی اکوادور بعد گل تیمش رفت با زنش لب گرفت
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95936" target="_blank">📅 01:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95935">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نویر اینجا هم رید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95935" target="_blank">📅 01:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95934">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اکوادور دومی رو زددددد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95934" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95933">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95933" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95932">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShrZdR8MYlfh-KXlBxYAcF-hfBr-t8HWDUXdc9MhRHfbDLFp5eM3Hz3huEW5PMyARMSgpwu7dHKrVW4tzl1IjNR-6kHsU5sTsX9GoYvtK3YIASTdlxEQ7klPNAM9ZSusnciV-x6xt3ViZGQyINZv4Zz2r9TFGl_hTstihVVxWpTwjIbGQqyMr3C24y2wo0xsJmgcfQYrlbGL0latJn2WsNnbR80nXeS04MzoNtWRzdyQvNUpvlejq5S0THVVwh4y-q2pv8c_lwHYeEgnDJj7Srnmar62Z_yb5l22uY3N7Ebd7IB0a7eOeTPNWr_U9Cvwux52ZeGsEY37mCPOnmpFNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نویر
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95932" target="_blank">📅 01:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95931">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3fb1037b27.mp4?token=em1EqUynySh34PZr9gGzcai5ufczNig8iIZJag44lgkbJPnznVW-KUTwebxaYE6Foyrijm9XYsYY1oKUFfsD3XXvCXNqrVqtRlzPVqiX_-Fq7JMmFF15Fp7zM_YgKszz5A8wplTBnkwy27HyNkKOCrjOuO6Kabv4k1N30n77DSirmDxH3RaqU9RKKFcRe9oawcdGepyqbbWpHce6Cts07aMufSVxtPEmk5exUq5ora_8K0uu145Q7h4JzKAoSSnKXsIevpDWSJNtdA1bIJ9G78HGnGjGD3S8b7j-bLAA6A27qSsY7Gfhr8Zc8-Kb6OQQKiCaru01kSdo06fmo9aoCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3fb1037b27.mp4?token=em1EqUynySh34PZr9gGzcai5ufczNig8iIZJag44lgkbJPnznVW-KUTwebxaYE6Foyrijm9XYsYY1oKUFfsD3XXvCXNqrVqtRlzPVqiX_-Fq7JMmFF15Fp7zM_YgKszz5A8wplTBnkwy27HyNkKOCrjOuO6Kabv4k1N30n77DSirmDxH3RaqU9RKKFcRe9oawcdGepyqbbWpHce6Cts07aMufSVxtPEmk5exUq5ora_8K0uu145Q7h4JzKAoSSnKXsIevpDWSJNtdA1bIJ9G78HGnGjGD3S8b7j-bLAA6A27qSsY7Gfhr8Zc8-Kb6OQQKiCaru01kSdo06fmo9aoCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ساحل عاج به کوراسائو روی دبل نیکولاس پپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95931" target="_blank">📅 01:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95930">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلللللللللللل دوم ساحل عاج</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95930" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95929">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کار زیبا و قشنگ این پدر که برای کودک نابیناش بازی رو اینطوری گزارش‌ میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95929" target="_blank">📅 00:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95928">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95928" target="_blank">📅 00:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95927">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzML0Tg2IiyVDwAovJsUDJFJHXRke0e2zPISfJa5x4Q6ImEvyOz4ejphcWIuwKX01_4Afi9JXKgn695eRvSChHUTn5yOgUB2Oiuh6BN3uOnvrNBwAK1BESCJx3GQI0A09XkNhl-56k6CnVBzizV47yHmswYniJTVlARkYGd4mXDCYvYg1hXtT1716oaNIHhi4VWVgg-kUpAK_GRSIGN8BuQ098mn2RcqFtHPinjls7gIqIgW3rljM_d0kE89BZ27VS2R81WjJRWFVbXfxXWNvFE6yidaGYGX3N9k2ib8GkU2iA6sS83HEhDDmTbEhOCOsX8ALWhqX-B7iBUgELLGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95927" target="_blank">📅 00:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eW32l5q0CPSs2MACJanpZhir3EPrvluBhzG_YckCAadM91r5Q7SbcRLsPHQIGBEZiUfIFns4jCNjkJEt6AHQjGqn11Thr1l8MQNsNWXIBluyYNwWLjk89gOzSnUpAOMRL7Cwd2YAuri8GDsxxo939N5wZ9b75W0GGj_dlsPWvfikSi2H1kvdFerRoi-GA0vKond-i7yBHiRCZ0dYva1whjdbkW_MMCdCe-3z-KvNnU8B49y57EYot3U3IrN6yhcBpWOztuPG2T_v_jo_7v8AQ0i2717pDwfM0Yte7ZDx-h6TIzl6o7y7fEUz2N0WRZAY395ao8ncR9E3P1eagfW9lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشلوتربرگ تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95926" target="_blank">📅 00:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae9310246.mp4?token=JdGpOAB1CtFH64oPP_dGIK72EtOqH6G6XLdG9I2JBMF7N1dWDIHwuxgyaIY4Uu9Tx0kLBlaEqoi4zun531f0DU-iMlCOBvWVwWi7YrEQAsrdp3my2RdLhKVaqJ5LUsjmWvsjEkiLWp-dFEHraeSFp5RpaB7h9yzUTIOq1A9RqJpNJozOdeKg4HnmSxticrVcy_Q8pifHw3MhwGJ4__kxwUP9lFF63qF9X-l8sVthJCz_k-Mi5Xa4OLCBfJqJzRND70jf1alPx4Lbyi1C0iZxOkiPhMq27wWVh9nhZQsgWZ20XopU_U6hC-S5ycPT5KGWUZm4QMChujtN_3z3ndO1GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae9310246.mp4?token=JdGpOAB1CtFH64oPP_dGIK72EtOqH6G6XLdG9I2JBMF7N1dWDIHwuxgyaIY4Uu9Tx0kLBlaEqoi4zun531f0DU-iMlCOBvWVwWi7YrEQAsrdp3my2RdLhKVaqJ5LUsjmWvsjEkiLWp-dFEHraeSFp5RpaB7h9yzUTIOq1A9RqJpNJozOdeKg4HnmSxticrVcy_Q8pifHw3MhwGJ4__kxwUP9lFF63qF9X-l8sVthJCz_k-Mi5Xa4OLCBfJqJzRND70jf1alPx4Lbyi1C0iZxOkiPhMq27wWVh9nhZQsgWZ20XopU_U6hC-S5ycPT5KGWUZm4QMChujtN_3z3ndO1GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مورینیو : امیدوارم بازیکن های رئال از جام جهانی سریع تر حذف شن و برگردن تا پیش فصل حاضر باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95925" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95924" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtOrrHvVyH7KH4ooevEI4fD4WttnKdRiAEZvmj5xon7bad_cuqN-OcW58BqcNhTmXNjZLQn-ZHdDFk8PAvllkjgTKs1cKzAtfJPmxg4cavTVu2yy5qL3HscClnsCT6AEgxvYWvYoEKI0tVITCYsB-40qocRZHV3g3fVQlC4CRUBg8DsSsukbG6HDB4WQQPkVGUqPm6XyVJFUza6luW_T_kdiU7MYWNjBRe3NhGsMrHzCYL4eMUbDSEN_RWIIaz0OCo3360B3LBPY0RYwrzMbOKvcYCtC-8NEn8W6eY4u3ztPciASq3co9U461jjlMyL4TJxX1Zq6AU7C_8JqbGPAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو، ببین من خسته شدم نشستم. مردک یه بازیو از دست نمیده.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95923" target="_blank">📅 00:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کی گفته تو داور باشی آخه</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95922" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پنالتییییییی برای آلمان</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95921" target="_blank">📅 00:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پنالتییییییی برای آلمان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95920" target="_blank">📅 00:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
الیوت اندرسون با قراردادی ۵ ساله به منچسترسیتی پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95919" target="_blank">📅 00:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRX-LS6afgkdUu5SG2I3s3zZcsbH8OUqPRpXYmtAbsVDaEgEwMPp4Y9kou8Ub6eFklcJ3T_Slb9-IC6r2YU1n81G2dgflvpvmZ9gAzpGe0KgIGteLfb9rlIQcz1dl7zdgpry-t5cR9U6qhP0n7u0HaCstiFaP5_S6O185eYp1kCa0RSs1jMTDH71oOPA7o_BNiMNZZjWwDg57QbZSH7meZY0F-TZyfV13VYYj1jZWO3lYxltqp7PORqZVFt_uKvZpRiLHgWwy_AuHx4IaUc5hWpt5DlqM04n6o8l9pLpuPnrvjX8ZdKBdwagSIay6wESJj_og9BJzlbGUZS_stbK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری؛ منچسترسیتی با الیوت اندرسون به توافق دست یافت و حالا مذاکرات با ناتینگهام برای تکمیل قرارداد درحال انجام است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95918" target="_blank">📅 00:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">پایان نیمه اول بازی های گروه E؛
🇩🇪
آلمان 1 - 1 اکوادور
🇪🇨
🇨🇮
ساحل عاج 1 - 0 کوراسائو
🇨🇼
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95917" target="_blank">📅 00:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOAjPf6nitkN_lGwGbtZWtlQk0BBxnyJ849CMxvjbZUOQFZAqUa6CbOkliwR7Ek9ZzVpBhy54Zwi6xgpMN2vFSi-y0RBU78gkzS1Ck8xqILCU9sXVS4aiijgQDmHWcMYixCUm1KiaQP9TygYOaEAZN7a7X8bUQX2oIa4r1HGtS5bPnhnuNjp1B7cxMQWtDEn_dWvVk1ckqPqC8-ubzz13T93Nz4TfchyEQH4ynQ9Vey1tZWWLG30zRBV01cStLXvwONqeKv5LF183Alt8DsfKeU0v-rJgEs4M_H15s5x0QP_DR1iEiED8QdeMA1bZgUx9wluthqoJxQA3R1BUgPmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
❌
فووووری آرشیو وار: گل آلمان بخاطر خطای پاولوویچ باید رد میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95916" target="_blank">📅 00:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بازی رفت آب درنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95915" target="_blank">📅 23:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95914">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇩🇪
گل اول آلمان به اکوادور توسط سانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95914" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95913">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5rDWRF6N1czeL1YNoteBcJDJteds1JVHb0s2NUuAhqxeIFrETkJh9PjLo3CBC5kqv_LnqLRV6L45vL949BSrJlUU7dPXI6PlaiSRjJ4Vd_jnKbRAxc-uWfPVv7qHBYIKNtQIr8wHs7OV3PSd3qlQQWhpa3WGQjR5v01TNQHbg5q-sEKDtXE0MjCJkUV3mx5_EQTr-S3e_olKJ05Uf-zEo4o36D81V7RHmLv178WLLnwhM4Fa0Lo5oTFeAA7uj7nfJ2e-if9vO5-BGSxrphScbq9gNMaZfc-etckuFHJBUs2x3spN66_S6JWpkEzUyTCe_Lav3ZleigYVVqmCJX2oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو، ببین من خسته شدم نشستم. مردک یه بازیو از دست نمیده.
😦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95913" target="_blank">📅 23:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95912">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986547037.mp4?token=Y4_w07KYcarxRy2nOaQdM6DXjvH0t-xRKPj2SMq6UGXJR5Uh-pNKD62oedy_WfP4q8K5rJUTs2FE_4T9TsTaYEHq5EAtxPz0zTWP2WxDg4cCmAMfgRaRLaFpz1mUoFAO5WB_dnz1LQnkt4LAGlbQqzMX1wJ-9j1Yaj29PQMqMnF3dAfNz3HcbVzjBX9McN3TYTgQ1EMJhauXGB42usv_VGFrtWQfF40VEXdvrz8tIHFIR8Ui5lhD8L8sFGZxgu0SoOublfF7F3Z7t3QDoHsImrZPWQDJhTzWKG3RQj6RUCHAg0DG3GeEgRMwj7sKkUQrbXUsP6H4AS0XSRCAOxBsG1YsaXt34lUCTJPOm3ZY6BHq3-CJCLzalnYJn3rSlqA_cFcfO-HcqtUtF4cuHspy1FuWM7cp1hQT2VFAgqMIEN9yLA5Xq3CF9hGcUjjWtyFV4eaHVUPli3lJjIasrayNGJc-fdCy4xlasSGUPw7xw9fhxkX-hOLj8xsF5Y68dmrWPLEqG2J8x0E5hA2HIrwrMiDzy5wvhRGg0qsRitiSEqLtcSoMdt5lb8opv6bbdaZ297nUtvTJeXwq2pivDaSloXuyI60CRHNC2l6CZk7lb7SIJX6A_b2LMkm1izQ5tLbZOVafH_aNvKVN0hJtjwioexfqP6dgwxcY0HfzQ9TTf5E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986547037.mp4?token=Y4_w07KYcarxRy2nOaQdM6DXjvH0t-xRKPj2SMq6UGXJR5Uh-pNKD62oedy_WfP4q8K5rJUTs2FE_4T9TsTaYEHq5EAtxPz0zTWP2WxDg4cCmAMfgRaRLaFpz1mUoFAO5WB_dnz1LQnkt4LAGlbQqzMX1wJ-9j1Yaj29PQMqMnF3dAfNz3HcbVzjBX9McN3TYTgQ1EMJhauXGB42usv_VGFrtWQfF40VEXdvrz8tIHFIR8Ui5lhD8L8sFGZxgu0SoOublfF7F3Z7t3QDoHsImrZPWQDJhTzWKG3RQj6RUCHAg0DG3GeEgRMwj7sKkUQrbXUsP6H4AS0XSRCAOxBsG1YsaXt34lUCTJPOm3ZY6BHq3-CJCLzalnYJn3rSlqA_cFcfO-HcqtUtF4cuHspy1FuWM7cp1hQT2VFAgqMIEN9yLA5Xq3CF9hGcUjjWtyFV4eaHVUPli3lJjIasrayNGJc-fdCy4xlasSGUPw7xw9fhxkX-hOLj8xsF5Y68dmrWPLEqG2J8x0E5hA2HIrwrMiDzy5wvhRGg0qsRitiSEqLtcSoMdt5lb8opv6bbdaZ297nUtvTJeXwq2pivDaSloXuyI60CRHNC2l6CZk7lb7SIJX6A_b2LMkm1izQ5tLbZOVafH_aNvKVN0hJtjwioexfqP6dgwxcY0HfzQ9TTf5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇨
گل مساوی اکوادور به آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95912" target="_blank">📅 23:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95911">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a82b1e615b.mp4?token=itI3AXWsUmp7ZyvFeA0eNLsgdu9XGkyxFbvtTHyQmOffwqIYQwbvLzRPW55ykZHnqsMSEswQNY4fcPLvhRLHUq4qRZWaUrYc4mtndVDSnJqR5-2fmkSuOJUFpX6P9Qp8O-o7hOWoTL20okfLNeWYH_kTDlVVVOFyXLVp3tGubXqcAUwqoaXmyMmA-cG-EMyQJ5nrlD8KY4vAZrPB8NBPJ3bjCWcJG99x251oZmqy9OABbucgsqCcu_VYntenld27To1PzKsDCuRRPEsGQQYUXS2tIHS8X6Z9pWW85GHQlkYOHnFbRhenXUY-ZOYJmaED3rjlD0gKnBU4TokVuD0kZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a82b1e615b.mp4?token=itI3AXWsUmp7ZyvFeA0eNLsgdu9XGkyxFbvtTHyQmOffwqIYQwbvLzRPW55ykZHnqsMSEswQNY4fcPLvhRLHUq4qRZWaUrYc4mtndVDSnJqR5-2fmkSuOJUFpX6P9Qp8O-o7hOWoTL20okfLNeWYH_kTDlVVVOFyXLVp3tGubXqcAUwqoaXmyMmA-cG-EMyQJ5nrlD8KY4vAZrPB8NBPJ3bjCWcJG99x251oZmqy9OABbucgsqCcu_VYntenld27To1PzKsDCuRRPEsGQQYUXS2tIHS8X6Z9pWW85GHQlkYOHnFbRhenXUY-ZOYJmaED3rjlD0gKnBU4TokVuD0kZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇮
گل اول ساحل عاج به کوراسائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95911" target="_blank">📅 23:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95910">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گللللل مساوی اکوادور</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95910" target="_blank">📅 23:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95909">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گللل ساحل عاج زد</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95909" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95908">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ae52ce55.mp4?token=kpB3PBKoZ_-RUAnIcWXFww-DU8PAAhAbGYPwPcWIMSsKxErUUlhcz9j2vJAfs6kGykF_syy02UAO-0GGlKf9k4mqNnD97HjUxNyNydAiDjAf18ORVge_Fz35NwNgSJDYnTDcUnTfSDjQAYPUnDB2QlZCR1f3QZ0koxKi7gorF63N0l6VeTNkdT4UuVM6At21VeVikCkaR9dydT66LCsdNJl0uBBEbCGPPcxBCF5l-Arvjsy72NWKwmKO07eyhjCnMLOd2FoSjJPbPQRafEhC14HVSad8X9dSfBPI3NvAxXijyk2r8-bmyYaU9uh3W7vOL2mFUsneRx1ikD1WY7OySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ae52ce55.mp4?token=kpB3PBKoZ_-RUAnIcWXFww-DU8PAAhAbGYPwPcWIMSsKxErUUlhcz9j2vJAfs6kGykF_syy02UAO-0GGlKf9k4mqNnD97HjUxNyNydAiDjAf18ORVge_Fz35NwNgSJDYnTDcUnTfSDjQAYPUnDB2QlZCR1f3QZ0koxKi7gorF63N0l6VeTNkdT4UuVM6At21VeVikCkaR9dydT66LCsdNJl0uBBEbCGPPcxBCF5l-Arvjsy72NWKwmKO07eyhjCnMLOd2FoSjJPbPQRafEhC14HVSad8X9dSfBPI3NvAxXijyk2r8-bmyYaU9uh3W7vOL2mFUsneRx1ikD1WY7OySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
گل اول آلمان به اکوادور توسط سانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95908" target="_blank">📅 23:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95907">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سانههههههه</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95907" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95906">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گللللل اول آلمان</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95906" target="_blank">📅 23:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95905">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بازیای گروه E شروع شددد
کوراسائو
🆚
ساحل عاج
آلمان
🆚
اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95905" target="_blank">📅 23:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95903">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne--BQ4Srv30nferF-27kJJyAQ3i-qOFyuqFcZTaxZvhQWoKZRcMh_6-7K8Wx2425iAdu72ssbPoeFGN1B3VWS-T_KZ1_egFopDNvkMbyfcUtXAjit06j3ZIoDQNSqvZiol00uYSqwKw6LFHYuHwBroxNOl0xNCEk87uimWTNRnL4iBFgc17LwO2mn-NKmRDNCLryUMS7DUrkJyIs8Py3nC611u4G7e7RBwv-4DpQTxXcoQ7Tb-HjOkqFHGtQzcMbmn9lYrSWCq02YYcJA57hqKpqsFaU7aIzDUnLZ-CpGBXm0YqJB3ss9v3gypKOJX8TpNyXUIcjSXfkmJG9ZwHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AUrJv7RzhjsdVl0FgY6Kc1aO5hznGmkrwTZzWxJZ9vcNTP2O8JwH36DDVWjTel4dTVMLgQ2AzzFenTXNtA_w-tM6GWhgbFh1xmGcnsDLGus_mk6VnmPOszD0ww6aSdRcXIVWfWISLN0XGoWlnJvyAcjHXTtjFgidWtCXRGVRVdIWKP44OqrLpQ3IODP1RyVWaQYyssyU2lkC2IZVwlcc2qVVX8z2PwQ6u2ILQRy8gjuROR6VqszClYLmFneNBqgJ32fD55M4f4xlAqOnTJBGdxdWiwsm2yGcffK47BNJfJybjRmwDsA3uxjFyvfLOIVjsDSXIKSyfOIqhKRcXVmvfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسی سر شوخیو با ژنرال باز کرد.🫪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/95903" target="_blank">📅 23:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95902">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7dcfaf7a.mp4?token=HvkaYJtkU8cr5cB5pCcEs6S5HvMH6YlQTW34_7VN1S187AVe9ZF_hpzxL6KucYxsnKGzYP5ezJR94H-cMaR__BY5ykqYRPT9RHoroYyWhG8wtqhd4REv7wXZoYf_NnbkE82yNh4iTg1dT6Q0CBzwkPKDgoU76TrtTbjx_FmcNV_StkR1IGMI-m1TmSmfxJTG9FS873h2SZQKxffv8PsXJAQTbr0EJVH9GUTeR-5mENsBfQ7QzDP2bUnrCgFKAlfkRUJooXZZRkcPVvdi-6YJ2AWswcJ2oBx0bsmgS6a3w6btlowColB89EqhuBJ9nJ2OBlXzDA22MJx2Xhp0zQC2rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7dcfaf7a.mp4?token=HvkaYJtkU8cr5cB5pCcEs6S5HvMH6YlQTW34_7VN1S187AVe9ZF_hpzxL6KucYxsnKGzYP5ezJR94H-cMaR__BY5ykqYRPT9RHoroYyWhG8wtqhd4REv7wXZoYf_NnbkE82yNh4iTg1dT6Q0CBzwkPKDgoU76TrtTbjx_FmcNV_StkR1IGMI-m1TmSmfxJTG9FS873h2SZQKxffv8PsXJAQTbr0EJVH9GUTeR-5mENsBfQ7QzDP2bUnrCgFKAlfkRUJooXZZRkcPVvdi-6YJ2AWswcJ2oBx0bsmgS6a3w6btlowColB89EqhuBJ9nJ2OBlXzDA22MJx2Xhp0zQC2rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلفظ اسم بازیکنای بارسا توسط داداش یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95902" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95901">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1bmpddHubQGbmWvSiBfOuTuiskeoLxigewiEbDJmesOuIWCbv0fcX4w7YYf36a9m08IgUh8DBekVTIFOQ0FMeukZdszabnvInBirzu6aw2rUDsTnPDHoYIdCBRWyfSbGfAk_w3FfZzfj-NczXyK3jwbsU7rSw0iADWO20YN-ftLxw1IIXL8g_Hc4xabVwJov1e9OX0Dr7e6oAq0-MdnT8Njet3zepvey-4reqo1yKgazU8DHCMaf1HvFpjuAtz2oqagsSjHtSChfhENNQATQpO-c7V94luSWSW-4ujdTx7J3PqacsM9PKf8Wa5qH5VSqv_xv6SiD18GMLgMf8Ctnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
رنکینگ آنلاین توپ طلای جام جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95901" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95900">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKSsWOBVijesOvZjUx3-NcQiyS2QsjatKISXztYvnTEliSQe1Fcci2wxc9A0_dCtb0I-EJ9_asI65tFYi5U46VtplHUr-Oci1vtTWGXgtPcKpRLLI40KvRUcMllqU4MMOrMelKXVPEWYRSsKy7fl5KsCoZvPMEiGEe4cUjUZSsvr375M-150qiRBTMM_selxb7Oh8fiw3NKZ8q9hR4P6qdwvSpGR3iD20mtP_xWCbkNwoLHq0U54f6VdvVEAaR0WgSgiKSng_tmOLVHmTkKbEGNiTNHvQwhpvSFVNZ7Uj37sjwOApKQOl5nzeq7JvzvOD7AS-eOEypvB7Kl8ELg5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو مسیر متفاوت پیش روی کریس و رفقا در صورت صدرنشینی گروه یا دوم شدن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95900" target="_blank">📅 23:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95898">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYG_sW0NgG9BgsjoxlzZPKVtqNA3pw6UJVyC0LUCILhG0juKQTMrB-O0DVqP76tVnpBnlaP7jlMxAF8-cP-q6MyqSay5RosAAnwWUqoO-p-9_ftimV3CJz7KA-BkRysZJYBxMm3A5x8Ge9lJ-lfwN595so32U63zmMgDh_LwSguVLpCy1yGVrsKudNEnMDpnDD9lPerKVmDQg7XRVfSAlSUa6XyDbXNJzp3n1yq-LYiyINLK9nbxJD4V0qUnQQOav-VTIcFKL_TzEpnUiaVAyTdWX7zhvDgErxJoOF1RXix5YXT2ZVE-VqnbB9PjpolYCz76GOoZwCnbWACo1df3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9_lshUziFGohJB6akMs1uvFIrWa7jVtnZpYD9Ma5nvru9uoas7XOmzWU1zdYa5Q0g__VZhoeyoY-eJ3i1FY6qvdecJfddMUiDAxdiYY2QP1aK_bCrjwHBdRSdmFMdZXo8i21VJ99be-4joLIHswuK-uiZwmYmgXMUbWCYU0dfrTYD6-KY80YXjvU7DHHAyiREAJw-ehOFooynb-KAFKgyVsOhPFENH4yTI6JuXgAQ7ud3WiJhqu90JFuDBH9wR0PG2HJXMpS0C2oechfF9wQBqEExSt0_HPSe_zke1baHurAM05a8x0lLUghQT2-UQiYjuHdu-o_1vxTaGSyKreow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
فرانک کسیه صد و پنجمین بازی خود را برای تیم ملی ساحل عاج انجام میدهد و با رکورد دیدیه دروگبا برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95898" target="_blank">📅 22:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95897">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ8zzlvFy7rvdqSEX44GsaN-r7ITGq7F15d4bOjPNCagheRxWLGQHiltmVLYYWFO9Cp9khJyr664hstYAfRJbTHZki8dBBDLNfJLXg5sV_pZPhnEzcsX83giWRoCaEOf9Yzf8_QDbu8qH4RP8YhqjTIBvWRpaisI6sEAXkuGGG1CUgZDVzhfwE9faibGHenpFX5lrNwcWmG5LfZLe58iFmZC2tZdy82QZN3fWfMRjYPlx4kIFzjCvLiahcO7-30hcjiNck7wyzk40Ryu0QAyQ7i7BAmJFheTeQQ4WB7wxFQj-tKhPMJM3Fpv7HALj7JlvhrCzBE-2rfm8fd2b1cSRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری کریم بنزما در حمایت از وینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95897" target="_blank">📅 22:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95895">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vw37Py0hZVf79vtlPHWHNduPrxvFAErcQzSGeH7IZuyuGU9jV_dPGkV5JD7W8hWTdDr9yIlRTp4qXa2Aw0Fq7UVCgEUxp3speTeyVVCKDBSp3rQJ62h48JIP7tUJvaKSi9BD5RHV-RuazBFshZRAVjQhW7Mbsvygx1u-6mEhqUWHUrc_UBbrAMD_wxq-VqUMpS_4EQpzC6rUIdyccWrql-ihejoz79Ahmsy_RLdEAjyoM1Wi0i_aDoR_8ZFrw19ZArevsYVkfXzR1nA5ug5Gu9UcS3Dgio8wiu98bDouRFb4jT_hsM3CLQHNC3M9r7nG21_hWx5_DPdC_wd95rpBfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uMuiq_lMUzAE9XB-lI2tSf5sFVUqYZ6CvbVIDUH7Tx80Wi9Hd26MfuvlFCzCbD30D6QTB72XZ7JKOxNig1oEJ3ZSCs5IIh3ubnNkxLl08jXnVKNmt2A6vyznnS7-VWYKZWzXclo7uDb3XbyP5eQC4gjr2gTcNhPog3OQtYNjF8JtCStWmRcrE20iXfqQeRsUfeiwvz50WoJEoZSXzD15sfkinWFOtBo7k_3e3P7GGGOzXG1K_yR2j7KV4LH9_27kgi1Zr48X0FhIRkM3EVzZgRQejXNIPkiCYYqMoQriKOU8pSWmpJ8odeledncY2e5CtFXpxK8pOikdGP9p7VIi0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇪
😀
ترکیب رسمی آلمان و اکوادور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95895" target="_blank">📅 22:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95893">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdj-AVdzDMASWru8hmM3WbzMIrEBL8lAFfPorhYj6wbDIO4o-4RkjRbZ0VDYkQ8oXNMw69Euh0Q8XX5KNsO0fT0EsmLzeZRGxxb6HDtWZB2Le2hfuD6i5owoj8OGMnpFOV_0wGWRcYITs4WpeTfDU04qXs2laZyIM0L_BnBU0xxb127uCGKmCLYS_79AuQ1Hw5DmUjpelr7ShMm1vYW2lYNcO9A0YB37ALGJvSw7q3yZDCbwlqODEFpdMUTENS1tNp2N-lApD5mPVps7SUeymCtV2lFVIQwlzFSxjQFqjNfGo9H1GT3JBK0zjfz1MuS4TLfjgVOBf750kJHq-28NNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHRIO__0Sa1vmqeEcNklQQcFOg3JenOb-_3IHnPkywgZ1tCemHkAp3ZpBM1g_dlxbwCDBbMiFAyIw8OB7RzWbcD-X7y3cT89SHoQ20_lAqr-uAdVsD8rlcvK-njMhDLN0ybq8aWEU2Hf1qWmdGe6iOkeQxFa0Zp1AEXyAo1JyOkKjk0lC5TM5j0O9NOuxOXBe37T-Sq2hpUopm1obUjICDy3QHZ5CS7EKi83nfBA9sLTAjfdhfvp94C4FjyAt34XgSNaDr5cje5vNMTBcHTaSLzkqKOexhkfa6Foynddkl8wfzXdmGp766McGnsmXYmRUDZOR1uu6SS4aZ08KKI2Kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب ساحل‌عاج و کوراسائو؛ ساعت ۲۳:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95893" target="_blank">📅 22:10 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
